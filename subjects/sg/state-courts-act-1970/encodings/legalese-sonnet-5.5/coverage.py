#!/usr/bin/env python3
"""Coverage table for the State Courts Act 1970 (SCA1970.txt), built from the text by script.

  python3 -I coverage.py RAW DISPOSITIONS [--md | --check | --deferred]

RAW is SCA1970.txt.  DISPOSITIONS is coverage-dispositions.txt: one line per pattern,
    <unit id or prefix> | <disposition> | <detail>
The first pattern that matches a unit id (equal, or the id continues with "(" or " ") wins.
Dispositions: encoded | inert | fork | repealed.  A unit no pattern matches is `deferred` (and --check fails).

Units are found by script: every section, subsection, paragraph, sub-paragraph, defined term and Explanation
in lines 190-2438; the Schedule's three oaths; the heading blocks (Part, sub-Part and section headings);
the front matter; the Legislative History.  Every non-blank line of the file falls in exactly one unit, one
heading block, one front-matter row, or the page-furniture class (page footers); --check proves it.
A converter artefact: lines 1628 and 2295 repeat a paragraph label ((a) in s 52(1B), (f) in s 69(3)) that
continues the paragraph above; they are not units."""
import re, sys, pathlib, collections
raw = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").split("\n")
N = len(raw)
FOOT = [re.compile(p) for p in [
    r"^\s*Informal Consolidation",
    r"^\s*\d+\s+State Courts Act 1970\s+2020 Ed\.\s*$",
    r"^\s*2020 Ed\.\s+State Courts Act 1970\s+\d+\s*$",
    r"^\s*2020 Ed\.\s*State Courts Act 1970\s*\d+\s*$",
    r"^\s*\d+\s+State Courts Act 1970\s*2020 Ed\.\s*$",
    r"^\s*(?:ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix|xx|xxi)\s*$",
]]
AMEND = re.compile(r"^\s*\[[^\]]*\]\s*$")
def blank(i): return not raw[i-1].strip()
def foot(i): return any(p.match(raw[i-1]) for p in FOOT)
def amend(i): return bool(AMEND.match(raw[i-1]))
BODY_START, BODY_END = 190, 2438
IGNORE = {1628, 2295}
sec_re = re.compile(r"^\s*(\d+[A-Z]{0,2})\.(?:—\((\d+[A-Z]{0,2})\)|\s)")
sub_re = re.compile(r"^\s*\((\d+[A-Z]{0,2})\)\s")
par_re = re.compile(r"^\s*\(([a-z]{1,2})\)\s")
rom_re = re.compile(r"^\s*\((i|ii|iii|iv|v|vi|vii|viii)\)\s")
term_re = re.compile(r"^\s*“([^”]+)”")
expl_re = re.compile(r"^\s*Explanation\.")
marks = []
sec = sub = par = None; roman_seen = False
for i in range(BODY_START, BODY_END + 1):
    if i in IGNORE or blank(i) or foot(i): continue
    t = raw[i-1]
    m = sec_re.match(t)
    if m and not t.lstrip().startswith("("):
        sec = m.group(1); sub = par = None; roman_seen = False
        if m.group(2):
            sub = m.group(2); marks.append((i, f"s {sec}({sub})"))
        else:
            marks.append((i, f"s {sec}"))
        continue
    m = sub_re.match(t)
    if m:
        sub = m.group(1); par = None; roman_seen = False
        marks.append((i, f"s {sec}({sub})")); continue
    m = rom_re.match(t)
    if m and not (par == "h" and roman_seen and m.group(1) == "i"):
        roman_seen = True
        base = f"s {sec}" + (f"({sub})" if sub else "") + f"({par})"
        marks.append((i, f"{base}({m.group(1)})")); continue
    m = par_re.match(t)
    if m:
        par = m.group(1); roman_seen = False
        marks.append((i, f"s {sec}" + (f"({sub})" if sub else "") + f"({par})")); continue
    if expl_re.match(t):
        marks.append((i, f"s {sec}({sub}) Explanation")); continue
    m = term_re.match(t)
    if m:
        marks.append((i, f"s {sec}" + (f"({sub})" if sub else "") + f" term {m.group(1)}")); continue
# a section line that is also its subsection (3.—(1)) was added once; dedupe ids
seen = {}
units = []   # (start, id)
for line, id_ in marks:
    if id_ in seen: id_ = f"{id_} [again at {line}]"
    seen[id_] = line; units.append((line, id_))
# headings: lines just before a section's first unit that are not terminated by punctuation
def heading_before(start):
    lines = []
    j = start - 1
    while j >= BODY_START:
        if blank(j) or foot(j): j -= 1; continue
        t = raw[j-1].strip()
        if amend(j) or (t[-1] in ".;,:—]" and not t.endswith("etc.")) or j in IGNORE or sec_re.match(raw[j-1]) or sub_re.match(raw[j-1]) or par_re.match(raw[j-1]): break
        lines.append(j); j -= 1
        # a heading continues over a single blank line only if the previous non-blank is also heading-like
    return sorted(lines)
rows = []   # dict(id, start, end, lines(set), kind)
owned = {}
def own(i, rid):
    assert i not in owned, (i, rid, owned.get(i))
    owned[i] = rid
unit_starts = [u[0] for u in units]
heads = {}
for k, (start, id_) in enumerate(units):
    first_of_section = (id_.startswith("s ") and re.match(r"^s \d+[A-Z]{0,2}(\(\w+\))?$", id_)
                        and (k == 0 or units[k-1][1].split("(")[0].split(" term")[0] != id_.split("(")[0].split(" term")[0]))
    if first_of_section:
        h = heading_before(start)
        if h: heads[id_] = h
head_lines = {l for h in heads.values() for l in h}
for k, (start, id_) in enumerate(units):
    nxt = units[k+1][0] if k + 1 < len(units) else BODY_END + 1
    lines = [l for l in range(start, nxt) if not blank(l) and not foot(l) and l not in head_lines]
    # include l in IGNORE (continuation line) naturally
    rows.append(dict(id=id_, lines=lines, kind="unit"))
for id_, h in heads.items():
    rows.append(dict(id=f"heading before {id_}", lines=h, kind="heading"))
# lines at the start of the body before the first unit (Part 1 heading)
pre = [l for l in range(BODY_START, units[0][0]) if not blank(l) and not foot(l) and l not in head_lines]
if pre: rows.append(dict(id="Part 1 heading (PART 1 PRELIMINARY)", lines=pre, kind="heading"))
# Schedule
sched = [("Schedule heading (THE SCHEDULE, Forms of oaths and affirmations)", [2439, 2441]),
         ("Schedule para 1 (oath of office and allegiance of a judicial officer)", [2443, 2459]),
         ("Schedule para 2 (oath of office of an interpreter)", [2461, 2473, 2478, 2484]),
         ("Schedule para 3 (oath of office of other officer of a court)", [2486, 2507])]
for name, rng in sched:
    ls = []
    for a, b in zip(rng[::2], rng[1::2]):
        ls += [l for l in range(a, b + 1) if not blank(l) and not foot(l)]
    rows.append(dict(id=name, lines=ls, kind="schedule"))
# front matter and history
fm = lambda a, b: [l for l in range(a, b + 1) if not blank(l) and not foot(l)]
rows.append(dict(id="Title page and revised-edition notice", lines=fm(1, 16), kind="front"))
rows.append(dict(id="Arrangement of Sections (table of contents; converter output misaligns its headings)", lines=fm(17, 181), kind="front"))
rows.append(dict(id="Long title", lines=fm(183, 184), kind="front"))
rows.append(dict(id="Amendment mark [5/2014] after the long title", lines=fm(186, 186), kind="front"))
rows.append(dict(id="Date of commencement [1 January 1971]", lines=fm(188, 188), kind="front"))
rows.append(dict(id="Legislative History (not part of the Act) and Abbreviations", lines=fm(2510, N), kind="history"))
for r in rows:
    for l in r["lines"]: own(l, r["id"])
furniture = [i for i in range(1, N + 1) if not blank(i) and i not in owned]
bad = [i for i in furniture if not foot(i)]
disp = []
dpath = sys.argv[2]
for ln in pathlib.Path(dpath).read_text(encoding="utf-8").split("\n"):
    if not ln.strip() or ln.startswith("#"): continue
    p = [x.strip() for x in ln.split("|", 2)]
    assert len(p) == 3, ln
    disp.append(p)
used = set()
def lookup(rid):
    for n, (pat, d, det) in enumerate(disp):
        if rid == pat or rid.startswith(pat + "(") or rid.startswith(pat + " ") or (pat.endswith("*") and rid.startswith(pat[:-1])):
            used.add(n); return d, det
    return "deferred", ""
order = sorted(rows, key=lambda r: min(r["lines"]) if r["lines"] else 10**9)
mode = sys.argv[3] if len(sys.argv) > 3 else "--check"
tally = collections.Counter(); inert_reason = collections.Counter()
table = []
for r in order:
    d, det = lookup(r["id"])
    tally[d] += 1
    if d == "inert": inert_reason[det.split(":")[0].strip()] += 1
    ls = r["lines"]
    first = raw[ls[0]-1].strip()[:50].replace("|", "/") if ls else ""
    rng = f"{min(ls)}-{max(ls)}" if ls else ""
    table.append((r["id"], rng, len(ls), first, d, det))
if mode == "--md":
    print("| unit | lines | disposition | where / why |\n| --- | --- | --- | --- |")
    for id_, rng, n, first, d, det in table:
        print(f"| {id_} | {rng} | {d} | {det} |")
    print()
print(f"rows: {len(table)}; by disposition: " + ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
if inert_reason: print("inert by reason: " + ", ".join(f"{k}={v}" for k, v in sorted(inert_reason.items())))
nb = sum(1 for i in range(1, N + 1) if not blank(i))
print(f"non-blank lines: {nb}; in a row: {len(owned)}; page furniture (footers): {len([i for i in furniture if foot(i)])}; unassigned: {len(bad)}")
unused = [disp[n] for n in range(len(disp)) if n not in used]
if unused: print("dispositions matching no unit:", unused)
if mode == "--deferred":
    for t in table:
        if t[4] == "deferred": print(t[0], t[1])
ok = (not bad) and tally["deferred"] == 0 and not unused
print("COVERAGE OK" if ok else "COVERAGE NOT YET OK")
sys.exit(0 if (mode != "--check" or ok) else 1)
