#!/usr/bin/env python3
"""Audit the FALSE/NOTHING tags of the FALSE/NOTHING rule of 2026-10-29.

For every layer-1 module (poca-*.l4 that is not a test or case file) and the seat layer:
  * a branch whose RESULT is `JUST FALSE` must carry `-- FALSE-kind (the text says no in its own words)` on its line or the comment line above it;
  * a branch whose RESULT is `NOTHING` must carry `-- NOTHING-kind (<why>)`, <why> one of: silent, list not closed, includes, undefined term,
    points outside the text, limited by its own wording;  in the seat layer a wiring line may carry `-- input mapping` instead.
A result is the word after THEN / OTHERWISE / ELSE.  A bare `NOTHING` used as a condition or an argument is not a result.
Run:  python3 -I tags.py        (prints the counts and every violation; exit 1 if any)
"""
import glob, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WHY = ("silent", "list not closed", "includes", "undefined term", "points outside the text", "limited by its own wording")
res_false = re.compile(r"\b(?:THEN|OTHERWISE|ELSE)\s+JUST FALSE\b")
res_nothing = re.compile(r"\b(?:THEN|OTHERWISE|ELSE)\s+NOTHING\b")
bad = 0; nf = nn = nm = 0
for path in sorted(glob.glob(os.path.join(HERE, "poca-*.l4"))):
    b = os.path.basename(path)
    if b.startswith(("poca-tests-", "poca-cases-")) or b == "poca-nouns.l4":
        continue
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines):
        code = ln.split("--", 1)[0]
        prev = lines[i - 1].strip() if i else ""
        if res_false.search(code):
            nf += 1
            if b.endswith("-seat.l4") and "-- input mapping" in ln:
                nm += 1
            elif "FALSE-kind (the text says no in its own words)" not in ln and not prev.startswith("-- FALSE-kind (the text says no in its own words)"):
                bad += 1; print(f"{b}:{i+1}: JUST FALSE without FALSE-kind: {ln.strip()[:120]}")
        if res_nothing.search(code):
            nn += 1
            m = re.search(r"NOTHING-kind \(([^)]*)\)", ln) or (re.match(r"-- NOTHING-kind \(([^)]*)\)", prev))
            ok = False
            if m and any(m.group(1).startswith(w) or w in m.group(1) for w in WHY):
                ok = True
            if b.endswith("-seat.l4") and "-- input mapping" in ln:
                nm += 1; ok = True
            if not ok:
                bad += 1; print(f"{b}:{i+1}: NOTHING without NOTHING-kind (<why>): {ln.strip()[:120]}")
# Second check: every quotation inside a FALSE-kind comment is in the source text (pieces joined by an ellipsis are checked one by one).
def norm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    t = re.sub(r"\((?:[a-z]{1,2}|[ivx]+)\)", "", t)   # paragraph markers (a), (ii): the source puts them on lines of their own after a dash
    t = t.replace("\u2014", "").replace("\u2013", "")
    return re.sub(r"\s+", "", t).lower()
raw = ""
RAWDIR = os.environ.get("RAW_DIR", "")
for name in ("ukpga-2002-29-part-7.txt", "ukpga-2002-29-schedule-9.txt"):
    pth = os.path.join(RAWDIR, name)
    if RAWDIR and os.path.exists(pth):
        raw += open(pth, encoding="utf-8").read() + "\n"
nq = nbad = 0
if raw:
    rawn = norm(raw)
    for path in sorted(glob.glob(os.path.join(HERE, "poca-*.l4"))):
        b = os.path.basename(path)
        if b.startswith(("poca-tests-", "poca-cases-")) or b == "poca-nouns.l4" or b.endswith("-seat.l4"):
            continue
        for i, ln in enumerate(open(path, encoding="utf-8").read().split("\n")):
            if "FALSE-kind (the text says no in its own words)" not in ln:
                continue
            tail = ln.split("FALSE-kind (the text says no in its own words)", 1)[1]
            tail = re.sub(r"\((?:a failed|a definition|a closed|an \"if\"|a condition|a failed condition|marginal reading)[^)]*\)", "", tail)
            for q in re.findall(r'["\u201c]([^"\u201d]+)["\u201d]', tail):
                for piece in re.split(r"\s*(?:\.\.\.|\u2026)\s*", q):
                    piece = piece.strip(" ,;:")
                    if len(piece) < 4:
                        continue
                    nq += 1
                    if norm(piece) not in rawn:
                        nbad += 1; print(f"{b}:{i+1}: quoted words not in the source: {piece[:100]}")
    print(f"quotations in FALSE-kind comments: {nq} checked, {nbad} not found in the source")
else:
    print("quotations in FALSE-kind comments: not checked (set RAW_DIR to the folder holding the two source texts)")
bad += nbad
print(f"tags: {nf} JUST FALSE results, {nn} NOTHING results ({nm} seat input mappings), {bad} violations")
sys.exit(1 if bad else 0)
