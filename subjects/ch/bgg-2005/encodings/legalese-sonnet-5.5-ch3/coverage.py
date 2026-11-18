#!/usr/bin/env python3
"""coverage.py: build the coverage table of the BGG chapter 3 encoding from the TEXT, and check it.

usage: python3 -I coverage.py RAWTEXT [--table]        (run it in the folder that holds the .l4 files)

What it does
  1. Reads the text file and cuts it into units: the file header, the chapter and section headings, one heading
     per Article, every numbered paragraph, an Article's unnumbered body, every list item (a., b., fbis., zter.)
     and every sub-item (1., 2.).  Footnote lines [^N] are attached to the unit that carries the marker [^N]
     (the brief: footnotes are not operative text and get no rows of their own).
  2. Looks each unit up in the layer-1 modules: a function whose name begins with the unit's key
     (for example `Art 74(1)(a) ...` for the unit Art 74(1)(a)); a unit with no function of its own but whose
     sub-items have one is encoded through them.
  3. Counts, for each unit, the assertions and traces in the test files that call its functions, and the seat
     questions that call them.
  4. Applies coverage-map.tsv: the fork register's unit lists (a unit named there is a `fork` row).
  5. CHECKS: every non-blank line of the text falls in exactly one row; every `encoded` or `fork` row has at
     least one function and at least one test; every function named `Art ...` in layer 1 belongs to a row.
     Prints COVERAGE OK or the problems, and exits 1 on any.
  With --table it prints the table as markdown (that is what NOTES.md embeds).
Dispositions: encoded | fork | inert (reason 1: not operative: a heading or the file header) |
              repealed or blank in this text.
"""
import re, sys, glob, os

RAW = sys.argv[1]
SHOW = "--table" in sys.argv
HERE = os.getcwd()
lines = open(RAW, encoding="utf-8").read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

# ---------------------------------------------------------------- 1. units from the text
units = []          # dicts: key, kind, lines(list of 1-based), text, notes(list of footnote numbers), repealed
cur_art = cur_par = cur_item = None
def add(key, kind, n, text):
    u = dict(key=key, kind=kind, lines=[n], text=text, notes=[], repealed=False, children=[])
    units.append(u)
    return u
MARK = re.compile(r"\[\^(\d+)\]")
first_op = next(i for i, l in enumerate(lines) if re.match(r"\d+\. Kapitel:", l))
pre = [i + 1 for i in range(first_op) if lines[i].strip()]
u = add("file header", "header", pre[0], lines[pre[0] - 1][:60])
u["lines"] = pre
for i in range(first_op, len(lines)):
    n, l = i + 1, lines[i]
    if not l.strip() or l.startswith("[^"):
        continue
    m = re.match(r"(\d+)\. (Kapitel|Abschnitt): (.*)", l)
    if m:
        add("%s %s" % (m.group(2), m.group(1)), "heading", n, l[:60]); cur_art = None; continue
    m = re.match(r"Art\. (\d+[a-z]*)((?:\[\^\d+\])?) (.*)", l)
    if m:
        cur_art = "Art " + m.group(1); cur_par = cur_item = None
        u = add(cur_art + " heading", "heading", n, l[:60])
        u["notes"] += MARK.findall(l)
        u["art"] = cur_art
        continue
    m = re.match(r"(\d+(?:bis|ter)?)((?:\[\^\d+\])?) (.*)", l)
    if m and cur_art:
        cur_par = "%s(%s)" % (cur_art, m.group(1)); cur_item = None
        u = add(cur_par, "paragraph", n, m.group(3)[:60]); u["art"] = cur_art
        u["notes"] += MARK.findall(l)
        continue
    m = re.match(r"  ([a-z]+)\.((?:\[\^\d+\])?) (.*)", l)
    if m and cur_art:
        base = cur_par or cur_art
        cur_item = "%s(%s)" % (base, m.group(1))
        u = add(cur_item, "item", n, m.group(3)[:60]); u["art"] = cur_art
        u["notes"] += MARK.findall(l)
        if m.group(3).strip() in ("…", "..."):
            u["repealed"] = True
        continue
    m = re.match(r"    (\d+)\.((?:\[\^\d+\])?) (.*)", l)
    if m and cur_art:
        u = add("%s(%s)" % (cur_item, m.group(1)), "subitem", n, m.group(3)[:60]); u["art"] = cur_art
        u["notes"] += MARK.findall(l)
        if m.group(3).strip() in ("…", "..."):
            u["repealed"] = True
        continue
    if cur_art and not cur_par:                       # the unnumbered body of an Article
        u = add(cur_art, "paragraph", n, l[:60]); u["art"] = cur_art; u["notes"] += MARK.findall(l)
        cur_par = cur_art
        continue
    raise SystemExit("line %d does not fit any unit: %r" % (n, l[:80]))

# footnote lines go to the unit that carries the marker
fn_line = {}
for i, l in enumerate(lines):
    m = re.match(r"\[\^(\d+)\] ", l)
    if m:
        fn_line[m.group(1)] = (i + 1, l)
for u in units:
    for k in u["notes"]:
        if k in fn_line:
            u["lines"].append(fn_line[k][0])
            if re.search(r"Aufgehoben", fn_line[k][1]) and u["kind"] != "heading":
                u["repealed"] = True
# a unit with a footnote that says "Aufgehoben" but also real text (a footnote on a name, not on the provision) is not repealed:
for u in units:
    if u["repealed"] and u["text"].strip() not in ("…", "...", ""):
        u["repealed"] = False

# ---------------------------------------------------------------- 2. functions in layer 1, tests, seat
def names_in(path):
    out = []
    for l in open(path, encoding="utf-8"):
        m = re.match(r"`(Art [^`]+)` MEANS", l)
        if m:
            out.append(m.group(1))
    return out
layer1 = {}
for f in sorted(glob.glob("bgg3-*.l4")):
    if "tests" in f or "cases" in f or "seat" in f or "nouns" in f:
        continue
    for nme in names_in(f):
        layer1[nme] = f
seat_q = {}
cur = None
seat_text = open("bgg3-seat.l4", encoding="utf-8").read()
for blk in re.split(r"\n(?=@export )", seat_text)[1:]:
    mm = re.search(r"\n`(Art [^`]+)` MEANS", blk)
    if mm:
        seat_q[mm.group(1)] = blk
tests = ""
for f in sorted(glob.glob("bgg3-tests-*.l4")) + ["bgg3-cases-seat.l4"]:
    tests += open(f, encoding="utf-8").read() + "\n"
def count_calls(name):
    pat = "`" + name + "`"
    return sum(1 for l in tests.split("\n") if (l.startswith("#ASSERT") or l.startswith("#TRACE")) and pat in l)
# who calls whom among the layer-1 functions (a backticked `Art ...` name inside another function's text)
callees = {}
for f in sorted(glob.glob("bgg3-*.l4")):
    if "tests" in f or "cases" in f or "seat" in f or "nouns" in f:
        continue
    curn = None
    for l in open(f, encoding="utf-8"):
        m = re.match(r"`(Art [^`]+)` MEANS", l)
        if m:
            curn = m.group(1); callees.setdefault(curn, set()); continue
        if re.match(r"(GIVEN|GIVETH|@ref|-- src:|§|DECLARE|@export|#)", l):
            curn = None
        if curn:
            for t in re.findall(r"`(Art [^`]+)`", l):
                if t != curn and t in layer1:
                    callees[curn].add(t)
def closure(names):
    seen, todo = set(), list(names)
    while todo:
        x = todo.pop()
        if x in seen:
            continue
        seen.add(x); todo += list(callees.get(x, ()))
    return seen
seat_reach = {q: closure([t for t in re.findall(r"`(Art [^`]+)`", blk.split("MEANS", 1)[1]) if t in layer1]) for q, blk in seat_q.items()}
def seat_calls(name):
    return sorted(q for q, r in seat_reach.items() if name in r)

def key_matches(key):
    return [n for n in layer1 if n.startswith(key + " ")]
for u in units:
    key = u["key"]
    u["funcs"] = key_matches(key) if u["kind"] in ("paragraph", "item", "subitem") else []
    # an Article-level function (`Art 72 ...`) gathers the Article's own numbered paragraphs: it belongs to each of them
    if u["kind"] == "paragraph" and key != u.get("art"):
        u["funcs"] += key_matches(u["art"])
# a unit with no function of its own is encoded through its sub-items
for u in units:
    if u["kind"] in ("paragraph", "item", "subitem") and not u["funcs"] and not u["repealed"]:
        kids = [n for n in layer1 if n.startswith(u["key"] + "(")]
        u["via_children"] = bool(kids)
        u["funcs"] = kids
    else:
        u["via_children"] = False

# ---------------------------------------------------------------- 3. the fork register's unit lists
forks = {}           # unit key -> [fork ids]
if os.path.exists("coverage-map.tsv"):
    for l in open("coverage-map.tsv", encoding="utf-8"):
        if l.startswith("#") or not l.strip():
            continue
        fid, ukeys = l.rstrip("\n").split("\t")[:2]
        for k in ukeys.split(","):
            forks.setdefault(k.strip(), []).append(fid)

# ---------------------------------------------------------------- 4. dispositions and checks
problems = []
rows = []
for u in units:
    k = u["key"]
    if u["kind"] in ("header", "heading"):
        disp, why = "inert", "reason 1, %s" % ("the file header and source note" if u["kind"] == "header" else "a heading")
    elif u["repealed"]:
        disp, why = "repealed or blank in this text", "shown as an ellipsis, with a footnote saying it is repealed"
    else:
        disp, why = ("fork" if k in forks else "encoded"), ""
        if not u["funcs"]:
            problems.append("%s: no function found" % k)
    u["disp"], u["why"] = disp, why
    u["forks"] = forks.get(k, [])
    ts = 0 if disp in ("inert", "repealed or blank in this text") else sum(count_calls(f) for f in u["funcs"])
    sq = sorted(set(q for f in u["funcs"] for q in seat_calls(f)))
    u["tests"], u["seat"] = ts, sq
    if disp in ("encoded", "fork") and ts == 0:
        problems.append("%s: no assertion or trace calls its functions" % k)
    rows.append(u)
# every non-blank line is in exactly one row
seen = {}
for u in rows:
    for n in u["lines"]:
        if n in seen and seen[n] is not u:
            problems.append("line %d is in two rows: %s and %s" % (n, seen[n]["key"], u["key"]))
        seen[n] = u
for i, l in enumerate(lines):
    if l.strip() and (i + 1) not in seen:
        problems.append("line %d is in no row: %r" % (i + 1, l[:60]))
# every Art function belongs to a row
owned = set(f for u in rows for f in u["funcs"])
for nme in layer1:
    if nme in owned:
        continue
    if any(nme.startswith(u["key"] + " ") for u in rows):
        continue
    problems.append("function not owned by any row: %s" % nme)
# fork ids named in the map exist as rows
rowkeys = set(u["key"] for u in rows)
for k in forks:
    if k not in rowkeys:
        problems.append("coverage-map.tsv names a unit that is not in the text: %s" % k)

# ---------------------------------------------------------------- 5. report
from collections import Counter
cnt = Counter(u["disp"] for u in rows)
nb = sum(1 for l in lines if l.strip())
body = sum(1 for l in lines[first_op:] if l.strip() and not l.startswith("[^"))
fnl = sum(1 for l in lines if l.startswith("[^"))
if SHOW:
    print("| unit | text lines | German text begins | disposition | modules | assertions + traces | seat questions |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for u in rows:
        ls = sorted(set(u["lines"]))
        own = [n for n in ls if not lines[n - 1].startswith("[^")]
        fnn = [n for n in ls if lines[n - 1].startswith("[^")]
        lr = ("%d" % own[0]) if len(own) == 1 else ("%d-%d" % (own[0], own[-1]) if own else "")
        if fnn:
            lr += " (+fn %s)" % ",".join(re.match(r"\[\^(\d+)\]", lines[n - 1]).group(1) for n in fnn)
        mods = sorted(set(layer1[f].replace("bgg3-", "").replace(".l4", "") for f in u["funcs"]))
        disp = u["disp"] + ("".join(" " + x for x in u["forks"]) if u["forks"] else "")
        if u["why"]:
            disp += ": " + u["why"]
        if u["via_children"]:
            disp += " (through its sub-items)"
        txt = u["text"].replace("|", "/")
        sq = ", ".join(s.split(" ")[0] + " " + s.split(" ")[1] for s in u["seat"]) if u["seat"] else ""
        print("| %s | %s | %s | %s | %s | %s | %s |" % (u["key"], lr, txt, disp, ", ".join(mods), u["tests"] if u["tests"] else "", sq))
else:
    print("coverage: %d units in %d non-blank lines of the text (%d operative lines + %d footnote lines + %d header/source lines)"
          % (len(rows), nb, body, fnl, nb - body - fnl))
    for d in ("encoded", "fork", "inert", "repealed or blank in this text"):
        print("  %-34s %3d" % (d, cnt[d]))
    print("  layer-1 functions: %d; seat questions: %d" % (len(layer1), len(seat_q)))
    if problems:
        print("COVERAGE PROBLEMS (%d):" % len(problems))
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("COVERAGE OK: every non-blank line of the text is in exactly one row; every encoded or fork row has a function and a test")
