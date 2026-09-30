#!/usr/bin/env python3
"""Merge the per-agent register fragments under registers/parts/ into the three
pipeline deposits: encoding-roadmap.json, fork-register.json and
external-modifications.json.

Usage: python3 merge-parts.py [--check]

The encoding was written by a team working in parallel on disjoint ranges of
articles: an ontology pass (g0), encoders g1a..g6b, and three sweep agents. Each
owned only its own fragments, so this merge is the one place their work meets,
and it REFUSES rather than guesses:

  - a roadmap unit claimed by two parts with different dispositions,
  - a fork id or an external-modification id that appears twice,
  - a reserved fork id (F-sweep-*) that a sweep routed to but no encoder created,
    which is reported, not invented: the pipeline's p4/p5 joins then fail on it,
    and that failure is the finding.

--check prints what it would write and exits 1 on any refusal.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
SUBJECT = "br-codigo-penal"
ENCODING = "legalese-2026-09"
problems = []


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def line_of(anchor):
    m = re.search(r":(\d+)$", anchor or "")
    return int(m.group(1)) if m else 10**9


# --- roadmap --------------------------------------------------------------
units = {}
for p in sorted(glob.glob(os.path.join(PARTS, "*.roadmap.json"))):
    for u in load(p)["units"]:
        prev = units.get(u["id"])
        if prev and prev[1] != u:
            problems.append(f"roadmap: {u['id']} is in {prev[0]} and {os.path.basename(p)} with different content")
        units[u["id"]] = (os.path.basename(p), u)
def article_key(uid):
    # "art. 359-M-A" -> (359, ["M", "A"]); an article with no suffix sorts before
    # its lettered insertions. Anchors are no longer usable for ordering: some
    # encoders re-pointed them at module anchors (g1c, g5; 85 units, found by
    # integ-titles 2026-09-30), so the order is the Code's own numbering.
    m = re.match(r"art\. (\d+)((?:-[A-Z]+)*)$", uid)
    if not m:
        problems.append(f"roadmap: unit id {uid!r} is not an article id")
        return (10**9, [])
    return (int(m.group(1)), [x for x in m.group(2).split("-") if x])
roadmap_units = [u for _, u in sorted(units.values(), key=lambda t: article_key(t[1]["id"]))]
tally = {}
for u in roadmap_units:
    tally[u["disposition"]] = tally.get(u["disposition"], 0) + 1
    if u["disposition"] == "deferred" and u.get("reason", "").startswith("NOT YET ENCODED"):
        problems.append(f"roadmap: {u['id']} is still deferred with the starting reason, never touched by its encoder")
roadmap = {
    "kind": "encoding-roadmap",
    "roadmap_version": "1.0.0",
    "subject": SUBJECT,
    "encoding": ENCODING,
    "granularity": "section",
    "source": {
        "document_id": "cp-planalto-compilado",
        "enumeration_basis": "Every line of source/codigo-penal-1940.txt that opens an article ('Art. N', 'Art N', 'Art. N-X', 'Art. N-X-Y', revoked ones included), enumerated mechanically by the conductor and checked against 'every article number 1-361 is present'. Units are articles; an article's paragraphs, incisos and alíneas are within its unit. Merged by registers/merge-parts.py from one part per encoder.",
        "enumeration_complete": True,
    },
    "units": roadmap_units,
}
if len(roadmap_units) != 434:
    problems.append(f"roadmap: {len(roadmap_units)} units, expected 434")

# --- forks ----------------------------------------------------------------
forks, fork_src = [], {}
for p in sorted(glob.glob(os.path.join(PARTS, "*.forks.json"))):
    for e in load(p):
        if e["id"] in fork_src:
            problems.append(f"forks: {e['id']} in both {fork_src[e['id']]} and {os.path.basename(p)}")
        fork_src[e["id"]] = os.path.basename(p)
        forks.append(e)
fork_register = {
    "kind": "fork-register",
    "register_version": 1,
    "subject": SUBJECT,
    "note": "Merged by registers/merge-parts.py from each encoder's registers/parts/<group>.forks.json. Fork ids F-sweep-* were reserved by the P2 sweep agents and created by the encoder of the article concerned.",
    "entries": forks,
}

# --- external modifications -------------------------------------------------
searches, entries, dispositions, seen = [], [], [], set()
for p in sorted(glob.glob(os.path.join(PARTS, "sweep-*.external-modifications.json"))):
    d = load(p)
    for kind, bucket in (("searches", searches), ("entries", entries)):
        for x in d.get(kind, []):
            if x["id"] in seen:
                problems.append(f"external-modifications: {x['id']} twice")
            seen.add(x["id"])
            bucket.append(x)
    dispositions.extend(d.get("dispositions", []))
for e in entries:
    for fid in e.get("routing", {}).get("fork_ids", []):
        if fid not in fork_src:
            problems.append(f"external-modifications: {e['id']} routes to {fid}, which no encoder created")
ext = {
    "kind": "external-modifications",
    "register_version": 1,
    "subject": SUBJECT,
    "swept": "2026-09-29",
    "note": "Merged by registers/merge-parts.py from three sweep agents' registers (sweep-a: arts. 1-120; sweep-b: 121-212; sweep-c: 213-361). The two whole-document marker classes (RedacaoNotes, VigenciaLinks) are disposed by the conductor below.",
    "searches": searches,
    "entries": entries,
    "dispositions": dispositions,
}

out = {
    "encoding-roadmap.json": roadmap,
    "fork-register.json": fork_register,
    "external-modifications.json": ext,
}
print(f"roadmap: {len(roadmap_units)} units {tally}")
print(f"forks: {len(forks)}")
print(f"external-modifications: {len(searches)} searches, {len(entries)} entries, {len(dispositions)} dispositions")
for pr in problems:
    print("REFUSED:", pr)
if "--check" in sys.argv:
    sys.exit(1 if problems else 0)
for name, doc in out.items():
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")
sys.exit(1 if problems else 0)
