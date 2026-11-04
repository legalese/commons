#!/usr/bin/env python3
"""Re-disposition audit for the Penal Code 1871 row (completion pass 2026-11-04).

Usage (from the encoding folder):
    python3 -I generators/deferred/audit.py [RAW] > logs/audit.txt

It reads the raw text (default ../../registers/source-bundle/PC1871.txt) and the
`notes/*-coverage.md` tables, and prints:

  1. the text's units, counted by script: section headings in the table of
     contents, section starts in the body, subsection markers `(1)` `(2)` ...,
     defined-term entries in the Interpretation sections, Schedule items;
  2. the coverage rows of the pass-1 notes, by disposition, and every section
     the text has that no row names (and every row naming a section the text
     does not have);
  3. for every row pass 1 called `repealed` or `inert`: what the text shows.

It reads files only; it writes nothing.
"""
import re
import sys
import os
import glob
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RAW = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "..", "..", "registers", "source-bundle", "PC1871.txt")

SEC = r"\d{1,3}[A-Z]{0,3}"
FOOT = re.compile(r"\s*(Singapore Statutes Online)?\s*Current version as at .*$")

with open(RAW, encoding="utf-8") as fh:
    lines = fh.read().split("\n")

# ---------------------------------------------------------------- the text's regions
toc_start = 6
toc_end = next(i for i, l in enumerate(lines) if l.startswith("THE SCHEDULE Specified offences"))
body_start = next(i for i, l in enumerate(lines) if l.strip() == "PENAL CODE 1871" and i > toc_end)
body_end = next(i for i, l in enumerate(lines) if l.strip() == "LEGISLATIVE HISTORY" and i > body_start)

# ---------------------------------------------------------------- table of contents
def sec_key(s):
    m = re.match(r"(\d+)([A-Z]*)", s)
    return (int(m.group(1)), m.group(2))


prev_key = (0, "")
toc = {}  # section -> heading
toc_gaps = []  # "[There are no sections 13 to 16.]" lines
cur = None
for i in range(toc_start, toc_end):
    l = FOOT.sub("", lines[i]).rstrip()
    if not l.strip() or l.strip().startswith("Singapore Statutes Online"):
        continue
    m = re.match(r"^\s*(%s)\s+(\S.*)$" % SEC, l)
    if m and not re.match(r"^\s*Chapter", l) and sec_key(m.group(1)) > prev_key:
        # a wrapped heading can start a line with a number ("18 years of age"); a real entry
        # always has a section number larger than the one before it
        cur = m.group(1)
        prev_key = sec_key(cur)
        toc[cur] = m.group(2).strip()
        continue
    g = re.match(r"^\s*\[There (?:is no section|are no sections) (.*?)\.?\]\s*$", l)
    if g:
        toc_gaps.append(g.group(1))
        continue
    if cur and not re.match(r"^\s*Chapter", l):
        toc[cur] += " " + l.strip()

# ---------------------------------------------------------------- the body
starts = {}  # section -> body line (1-based)
for i in range(body_start, body_end):
    m = re.match(r"^\s*(%s)\.(?:\s|—|\Z)" % SEC, lines[i])
    if m and m.group(1) in toc and m.group(1) not in starts:
        starts[m.group(1)] = i + 1

order = list(toc.keys())
order_idx = {s: k for k, s in enumerate(order)}


def span(sec):
    """Body line range of a section: its start to the line before the next section's start."""
    s = starts.get(sec)
    if s is None:
        return None
    k = order_idx[sec]
    for nxt in order[k + 1:]:
        if nxt in starts:
            return s, starts[nxt] - 1
    return s, body_end


sub_re = re.compile(r"^\s{0,12}\((\d+[A-Z]{0,2})\)\s")
first_sub_re = re.compile(r"^\s*%s\.—\((\d+[A-Z]{0,2})\)" % SEC)
subs = {}
for sec in starts:
    a, b = span(sec)
    found = []
    for i in range(a - 1, b):
        l = lines[i]
        m = first_sub_re.match(l) or sub_re.match(l)
        if m:
            tok = m.group(1)
            if tok.isdigit() or re.match(r"^\d+[A-Z]{1,2}$", tok):
                found.append(tok)
    # keep the numeric subsection series only (1), (1A), (2) ...; letters (a) (b) are paragraphs
    subs[sec] = found

# ---------------------------------------------------------------- pass-1 coverage rows
rows = []  # (file, section, heading, disposition, rest)
for f in sorted(glob.glob(os.path.join(ROOT, "notes", "*-coverage.md"))):
    base = os.path.basename(f)
    for ln in open(f, encoding="utf-8"):
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        # find the section cell: the first cell that is a bare section token, taking the SECOND
        # candidate where the first is a Chapter number (state-public: "| Ch | s |")
        idx = None
        if re.fullmatch(SEC, cells[0]):
            idx = 0
            if len(cells) > 1 and re.fullmatch(SEC, cells[1]) and base.startswith("state-public"):
                idx = 1
        elif re.fullmatch(r"s " + SEC, cells[0]):
            continue  # an illustration row, not a section row
        if idx is None:
            continue
        sec = cells[idx]
        head = cells[idx + 1] if len(cells) > idx + 1 else ""
        disp = cells[idx + 2] if len(cells) > idx + 2 else ""
        rest = " | ".join(cells[idx + 3:])
        rows.append((base, sec, head, disp, rest))


def kind(disp):
    d = re.sub(r"^\(\d+[A-Z]?\)\s*", "", disp.lower()).lstrip("— ")
    for k in ("repealed", "inert", "deferred", "out-of-scope", "encoded", "partly encoded", "none exists", "n/a", "not a section"):
        if d.startswith(k) or (k in d and k in ("repealed",)):
            return k
    return d.split()[0] if d else "?"


best_rank = {"encoded": 0, "partly encoded": 1, "inert": 2, "repealed": 3, "deferred": 4, "out-of-scope": 5}
best = {}
rows_by_sec = defaultdict(list)
for r in rows:
    rows_by_sec[r[1]].append(r)
for sec, rs in rows_by_sec.items():
    kinds = [kind(r[3]) for r in rs]
    best[sec] = min(kinds, key=lambda k: best_rank.get(k, 9))

# ---------------------------------------------------------------- report
out = []
P = out.append
P("# Audit of units, %s" % os.path.basename(RAW))
P("")
P("## 1. The text's units, by script")
P("raw file: %d lines; table of contents lines %d-%d; body lines %d-%d" % (len(lines), toc_start + 1, toc_end, body_start + 1, body_end))
P("section headings in the table of contents: %d" % len(toc))
P("  of which `(Repealed)` in the contents: %d" % sum(1 for h in toc.values() if h.startswith("(Repealed)")))
P("section starts found in the body: %d" % len(starts))
P("TOC sections with no start in the body: %s" % (sorted(set(toc) - set(starts), key=lambda s: order_idx[s]) or "none"))
P("gaps announced in the contents: %s" % "; ".join(toc_gaps))
nsubs = sum(len(v) for v in subs.values())
P("numbered subsection markers in the body, (1) (2) (1A) ... at line start: %d, across %d sections" % (nsubs, sum(1 for v in subs.values() if v)))
body = lines[body_start:body_end]
paras = sum(1 for l in body if re.match(r"^\s{0,40}\([a-z]{1,2}\)\s", l))
illus = sum(1 for l in body if re.match(r"^\s*Illustrations?\s*$", l))
expl = sum(1 for l in body if re.match(r"^\s*Explanations?[.\u2014 ]", l))
exc = sum(1 for l in body if re.match(r"^\s*(First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth)\s+Exception", l, re.I))
defs = sum(1 for l in body if re.match(r"^\s*\u201c[^\u201d]{1,80}\u201d(, .{0,80})? (means|includes|has the meaning|have the meanings|denotes|is)", l))
P("lettered paragraph markers (a) (b) ... at line start: %d" % paras)
P("Illustration headings: %d; Explanation paragraphs: %d; named Exceptions: %d" % (illus, expl, exc))
P("defined-term entries (a quoted term followed by means/includes/has the meaning/denotes/is): %d" % defs)
chapters = [l for l in lines[toc_start:toc_end] if re.match(r"^Chapter ", l)]
P("chapters in the contents: %d" % len(chapters))
sched_items = len(re.findall(r"^\s*\d{1,2}\. ", "\n".join(lines[next(i for i, l in enumerate(lines) if "THE SCHEDULE            Section 4B" in l):body_end]), re.M))
P("items in the Schedule: %d" % sched_items)

P("")
P("## 2. The pass-1 coverage rows")
P("rows read from notes/*-coverage.md: %d, naming %d distinct sections" % (len(rows), len(rows_by_sec)))
c = Counter(best.values())
P("best disposition per section: " + ", ".join("%s %d" % (k, v) for k, v in sorted(c.items())))
miss = [s for s in toc if s not in rows_by_sec]
P("")
P("sections in the text's contents that NO coverage row names (%d): %s" % (len(miss), " ".join(miss) or "none"))
extra = [s for s in rows_by_sec if s not in toc]
P("sections named by a row that the contents does not list (%d): %s" % (len(extra), " ".join(sorted(extra)) or "none"))

P("")
P("## 3. Rows pass 1 called repealed: what does the text show?")
bad_rep = []
n_rep = 0
for sec in order:
    rs = rows_by_sec.get(sec, [])
    if not any(kind(r[3]) == "repealed" for r in rs):
        continue
    n_rep += 1
    a, b = span(sec) if sec in starts else (None, None)
    show = ""
    if a:
        seg = " ".join(l.strip() for l in lines[a - 1:min(b, a + 3)])
        seg = re.sub(r"\s+", " ", seg)
        mm = re.search(r"\[?\(?Repealed[^\]\n]{0,60}\]?", seg)
        show = mm.group(0) if mm else ""
    toc_rep = toc[sec].startswith("(Repealed)")
    ok = bool(show) or toc_rep
    if not ok:
        bad_rep.append(sec)
    P("  s %-6s toc:%-9s body:%s  %s" % (sec, "Repealed" if toc_rep else toc[sec][:8], (show or "-")[:60], "ok" if ok else "NO REPEAL SHOWN"))
P("repealed rows: %d (sections); with no repeal shown by the text: %s" % (n_rep, bad_rep or "none"))
rep_in_toc_not_row = [s for s in toc if toc[s].startswith("(Repealed)") and not any(kind(r[3]) == "repealed" for r in rows_by_sec.get(s, []))]
P("sections the contents marks (Repealed) that no row calls repealed: %s" % (rep_in_toc_not_row or "none"))

P("")
P("## 4. Rows pass 1 called inert (section-level best disposition = inert)")
inert_secs = [s for s in order if best.get(s) == "inert"]
P("inert sections: %d: %s" % (len(inert_secs), " ".join(inert_secs)))
for sec in inert_secs:
    r = [x for x in rows_by_sec[sec] if kind(x[3]) == "inert"][0]
    a, b = span(sec) if sec in starts else (0, 0)
    P("  s %-5s %-60s lines %d-%d (%d subsections)  %s" % (sec, toc.get(sec, "")[:60], a, b, len(subs.get(sec, [])), (r[3] + " " + r[4])[:110]))

P("")
P("## 5. Sections whose best disposition is something else")
for k in ("deferred", "out-of-scope", "partly encoded"):
    ss = [s for s in order if best.get(s) == k]
    P("%s: %d: %s" % (k, len(ss), " ".join(ss)))

print("\n".join(out))
