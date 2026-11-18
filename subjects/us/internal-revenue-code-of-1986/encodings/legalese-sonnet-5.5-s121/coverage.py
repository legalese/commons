#!/usr/bin/env python3
"""coverage.py RAW [--audit]   Build the coverage table of 26 U.S.C. section 121 from the text itself.

It reads RAW (usc26-s121.txt), cuts it into units (the header, the title, and every subsection, paragraph,
subparagraph, clause and subclause, each from its label line to the line before the next label), adds the
defined-term rows, gives every row one disposition from the MAP below, and checks that
  * every unit has a disposition and every disposition names a unit;
  * every rule named in a row is defined in the named module (a name that starts with the given words);
  * every test file named exists beside this script;
  * every non-blank line of RAW falls in at least one row.
It prints the table as markdown (rows only with --table, the audit counts with --audit, both by default).
Run:  python3 -I coverage.py ../../../inputs/usc26-s121.txt
"""
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = sys.argv[1]
lines = open(RAW, encoding="utf-8").read().split("\n")

LAB = re.compile(r"^(\s*)\[?(\((?:[a-z]|\d+|[A-Z]|[ivx]+|[IVX]+)\))")
units = []          # [first, last, path]
stack = []
for i, l in enumerate(lines, 1):
    if i < 13 or not l.strip():
        continue
    m = LAB.match(l)
    if m and i <= 156:
        ind = len(m.group(1)); label = m.group(2)
        while stack and stack[-1][0] >= ind:
            stack.pop()
        stack.append((ind, label))
        units.append([i, i, "".join(x[1] for x in stack)])
    elif i <= 156 and units:
        units[-1][1] = i
# lines 1-11 (header), 12 (title), 157 (source credit), 158 (footnote) are rows of their own
EXTRA = [(1, 11, "header"), (12, 12, "title"), (157, 157, "source credit"), (158, 158, "footnote")]

N, A, B, C, D1, D9, E, W = ("s121-nouns.l4", "s121-a-exclusion.l4", "s121-b-limitations.l4", "s121-c-reduced.l4",
                           "s121-d1-special.l4", "s121-d9-service.l4", "s121-efg.l4", "s121-whole.l4")
TA, TB, TC, TD1, TD9, TW, CS = ("s121-tests-a.l4", "s121-tests-b.l4", "s121-tests-c.l4", "s121-tests-d1.l4",
                                "s121-tests-d9.l4", "s121-tests-whole.l4", "s121-cases-seat.l4")
ENC, INERT, FORK, REP = "encoded", "inert", "fork", "repealed or blank in this text"

# path -> (disposition, [(module, name-prefix)], [tests], [forks or inert reason])
MAP = {
 "header": (INERT, [], [], ["1: not operative (the converter's header: source, release point, licence note)"]),
 "title": (INERT, [], [], ["1: not operative (the section's number and heading)"]),
 "(a)": (FORK, [(A, "s 121(a)"), (W, "s 121(a)")], [TA, TW, CS], ["F1", "F2", "F3", "F4", "F5", "F6"]),
 "(b)": (INERT, [], [], ["1: not operative (heading: Limitations)"]),
 "(b)(1)": (ENC, [(B, "s 121(b)(1)")], [TB, TW, CS], []),
 "(b)(2)": (ENC, [(B, "s 121(b)(2)(A) paragraph (1) is applied"), (W, "s 121(b) the limitation before")], [TB, TW, CS], []),
 "(b)(2)(A)": (ENC, [(B, "s 121(b)(2)(A) paragraph (1) is applied"), (B, "s 121(b)(2)(A) the limitation")], [TB, TW], []),
 "(b)(2)(A)(i)": (ENC, [(B, "s 121(b)(2)(A)(i)")], [TB, TW], []),
 "(b)(2)(A)(ii)": (ENC, [(B, "s 121(b)(2)(A)(ii)")], [TB, TW], []),
 "(b)(2)(A)(iii)": (ENC, [(B, "s 121(b)(2)(A)(iii)")], [TB, TW], []),
 "(b)(2)(B)": (FORK, [(B, "s 121(b)(2)(B)"), (W, "s 121(b)(2)(B)")], [TB, TW, CS], ["F13", "F16", "F27"]),
 "(b)(3)": (FORK, [(B, "s 121(b)(3)"), (W, "s 121(b)(3)")], [TB, TW, CS], ["F26", "F29"]),
 "(b)(4)": (FORK, [(B, "s 121(b)(4)")], [TB, TW, CS], ["F5", "F14"]),
 "(b)(5)": (INERT, [], [], ["1: not operative (heading: Exclusion of gain allocated to nonqualified use)"]),
 "(b)(5)(A)": (ENC, [(B, "s 121(b)(5)(A)")], [TB, TW, CS], []),
 "(b)(5)(B)": (FORK, [(B, "s 121(b)(5)(B)")], [TB, TW], ["F9"]),
 "(b)(5)(B)(i)": (ENC, [(B, "s 121(b)(5)(C) the aggregate days")], [TB, TW], []),
 "(b)(5)(B)(ii)": (FORK, [(W, "s 121 the treatment of the gain")], [TW], ["F16"]),
 "(b)(5)(C)": (ENC, [(B, "s 121(b)(5)(C) the aggregate days")], [TB, TW, CS], []),
 "(b)(5)(C)(i)": (FORK, [(B, "s 121(b)(5)(C)(i)")], [TB, TW, CS], ["F22"]),
 "(b)(5)(C)(ii)": (ENC, [(B, "s 121(b)(5)(C) the aggregate days")], [TB, TW], []),
 "(b)(5)(C)(ii)(I)": (FORK, [(B, "s 121(b)(5)(C)(ii)(I)")], [TB, TW], ["F23", "F28"]),
 "(b)(5)(C)(ii)(II)": (FORK, [(B, "s 121(b)(5)(C)(ii)(II)"), (D9, "s 121(d)(9)(A) the days of service on qualified official")], [TB, TD9, TW], ["F10", "F30"]),
 "(b)(5)(C)(ii)(III)": (FORK, [(B, "s 121(b)(5)(C)(ii)(III)")], [TB, CS], ["F10"]),
 "(b)(5)(D)": (ENC, [(B, "s 121(b)(5)(D)")], [TB, TW], []),
 "(b)(5)(D)(i)": (ENC, [(B, "s 121(b)(5)(D)(i)")], [TB, TW, CS], []),
 "(b)(5)(D)(ii)": (ENC, [(B, "s 121(b)(5)(D)(ii)")], [TB, TW, CS], []),
 "(c)": (INERT, [], [], ["1: not operative (heading: Exclusion for taxpayers failing to meet certain requirements)"]),
 "(c)(1)": (ENC, [(C, "s 121(c)(1) the ownership and use requirements"), (C, "s 121(c)(1) the dollar limitation")], [TC, TW, CS], []),
 "(c)(1)(A)": (FORK, [(C, "s 121(c)(1) the dollar limitation as reduced")], [TC, TW, CS], ["F9"]),
 "(c)(1)(B)": (ENC, [(C, "s 121(c)(1)(B)(i) the shorter"), (C, "s 121(c)(1)(B)(ii)")], [TC, TW], []),
 "(c)(1)(B)(i)": (FORK, [(C, "s 121(c)(1)(B)(i) the shorter")], [TC, TW], ["F11"]),
 "(c)(1)(B)(i)(I)": (FORK, [(C, "s 121(c)(1)(B)(i)(I)")], [TC, TW], ["F1"]),
 "(c)(1)(B)(i)(II)": (FORK, [(C, "s 121(c)(1)(B)(i)(II)")], [TC, TW, CS], ["F25"]),
 "(c)(1)(B)(ii)": (FORK, [(C, "s 121(c)(1)(B)(ii)")], [TC, TW], ["F6"]),
 "(c)(2)": (ENC, [(C, "s 121(c)(2) this subsection applies")], [TC, TW, CS], []),
 "(c)(2)(A)": (ENC, [(C, "s 121(c)(2)(A) subsection (a)")], [TC, TW], []),
 "(c)(2)(A)(i)": (ENC, [(C, "s 121(c)(2)(A)(i)")], [TC, TW], []),
 "(c)(2)(A)(ii)": (ENC, [(C, "s 121(c)(2)(A)(ii)")], [TC, TW], []),
 "(c)(2)(B)": (ENC, [(C, "s 121(c)(2)(B)")], [TC, TW, CS], []),
 "(d)": (INERT, [], [], ["1: not operative (heading: Special rules)"]),
 "(d)(1)": (FORK, [(D1, "s 121(d)(1)"), (W, "s 121 the treatment of the gain")], [TD1, TW], ["F12"]),
 "(d)(2)": (FORK, [(D1, "s 121(d)(2)"), (W, "s 121(d) the individual's holding")], [TD1, TW, CS], ["F24"]),
 "(d)(3)": (ENC, [(W, "s 121(d) the individual's holding")], [TW], []),
 "(d)(3)(A)": (ENC, [(D1, "s 121(d)(3)(A)")], [TD1, TW], []),
 "(d)(3)(B)": (ENC, [(D1, "s 121(d)(3)(B)")], [TD1, TW, CS], []),
 "(d)(3)(C)": (ENC, [(D1, "s 121(d)(3)(C) the instrument is a divorce")], [TD1, CS], []),
 "(d)(3)(C)(i)": (ENC, [(D1, "s 121(d)(3)(C)(i)")], [TD1], []),
 "(d)(3)(C)(ii)": (ENC, [(D1, "s 121(d)(3)(C)(ii)")], [TD1], []),
 "(d)(3)(C)(iii)": (ENC, [(D1, "s 121(d)(3)(C)(iii)")], [TD1], []),
 "(d)(4)": (ENC, [(W, "s 121(d) the individual's holding")], [TW], []),
 "(d)(4)(A)": (ENC, [(D1, "s 121(d)(4)(A)")], [TD1], []),
 "(d)(4)(B)": (ENC, [(D1, "s 121(d)(4)(B)")], [TD1], []),
 "(d)(5)": (INERT, [], [], ["1: not operative (heading: Involuntary conversions)"]),
 "(d)(5)(A)": (ENC, [(D1, "s 121(d)(5)(A)"), (W, "s 121(d)(5)(A)")], [TD1, TW, CS], []),
 "(d)(5)(B)": (ENC, [(D1, "s 121(d)(5)(B)")], [TD1, CS], []),
 "(d)(5)(C)": (ENC, [(D1, "s 121(d)(5)(C)")], [TD1], []),
 "(d)(6)": (FORK, [(D1, "s 121(d)(6)"), (W, "s 121 the treatment of the gain")], [TD1, TW, CS], ["F20"]),
 "(d)(7)": (FORK, [(D1, "s 121(d)(7)")], [TD1, TW, CS], ["F21"]),
 "(d)(7)(A)": (ENC, [(D1, "s 121(d)(7)")], [TD1, CS], []),
 "(d)(7)(B)": (FORK, [(D1, "s 121(d)(7)")], [TD1, CS], ["F21"]),
 "(d)(8)": (ENC, [(D1, "s 121(d)(8)(A)"), (W, "s 121 whether the section reaches")], [TD1, TW], []),
 "(d)(8)(A)": (ENC, [(D1, "s 121(d)(8)(A)")], [TD1, TW, CS], []),
 "(d)(8)(B)": (ENC, [(D1, "s 121(d)(8)(B)")], [TD1, TW, CS], []),
 "(d)(9)": (INERT, [], [], ["1: not operative (heading: Uniformed services, Foreign Service, and intelligence community)"]),
 "(d)(9)(A)": (FORK, [(D9, "s 121(d)(9)(A) the service is qualified"), (D9, "s 121(d)(9)(A) the running")], [TD9, TW, CS], ["F7", "F19", "F30"]),
 "(d)(9)(A)(i)": (ENC, [(D9, "s 121(d)(9)(A) the service is qualified")], [TD9, CS], []),
 "(d)(9)(A)(ii)": (ENC, [(D9, "s 121(d)(9)(A) the service is qualified")], [TD9], []),
 "(d)(9)(A)(iii)": (ENC, [(D9, "s 121(d)(9)(A) the service is qualified")], [TD9, CS], []),
 "(d)(9)(B)": (FORK, [(D9, "s 121(d)(9)(B)")], [TD9, TW, CS], ["F7"]),
 "(d)(9)(C)": (ENC, [(D9, "s 121(d)(9)(C)(i)")], [TD9], []),
 "(d)(9)(C)(i)": (ENC, [(D9, "s 121(d)(9)(C)(i)")], [TD9, CS], []),
 "(d)(9)(C)(ii)": (ENC, [(D9, "s 121(d)(9)(C)(ii)")], [TD9], []),
 "(d)(9)(C)(iii)": (ENC, [(D9, "s 121(d)(9)(C)(iii)")], [TD9], []),
 "(d)(9)(C)(iv)": (ENC, [(D9, "s 121(d)(9)(C)(iv) the person is an employee")], [TD9, CS], []),
 "(d)(9)(C)(v)": (ENC, [(D9, "s 121(d)(9)(C)(v)")], [TD9, CS], []),
 "(d)(9)(D)": (INERT, [], [], ["1: not operative (heading: Special rules relating to election)"]),
 "(d)(9)(D)(i)": (ENC, [(D9, "s 121(d)(9)(A) the running")], [TD9, TW, CS], []),
 "(d)(9)(D)(ii)": (FORK, [(D9, "s 121(d)(9)(A) the running")], [TD9, TW], ["F19"]),
 "(d)(10)": (ENC, [(D9, "s 121(d)(10)"), (W, "s 121 whether the section reaches")], [TD9, TW, CS], []),
 "(d)(11)": (REP, [], [], ["the text shows `[(11) Repealed. Pub. L. 111-312, title III, s 301(a), Dec. 17, 2010, 124 Stat. 3300]` and nothing else"]),
 "(d)(12)": (INERT, [], [], ["1: not operative (heading: Peace Corps)"]),
 "(d)(12)(A)": (FORK, [(D9, "s 121(d)(12)(A)")], [TD9, TW, CS], ["F30"]),
 "(d)(12)(A)(i)": (ENC, [(D9, "s 121(d)(12)(A) the service is serving")], [TD9], []),
 "(d)(12)(A)(ii)": (ENC, [(D9, "s 121(d)(12)(A) the service is serving")], [TD9, CS], []),
 "(d)(12)(B)": (FORK, [(D9, "s 121(d)(12)(B)")], [TD9], ["F8"]),
 "(e)": (FORK, [(E, "s 121(e)"), (W, "s 121 whether the section reaches")], [TC, TW, CS], ["F18"]),
 "(f)": (ENC, [(E, "s 121(f)"), (W, "s 121 whether the section reaches")], [TC, TW, CS], []),
 "(g)": (FORK, [(E, "s 121(g)"), (W, "s 121(g) the days added")], [TC, TW, CS], ["F15"]),
 "source credit": (INERT, [], [], ["1: not operative (the date of enactment and the amendments)"]),
 "footnote": (INERT, [], [], ["1: not operative (a pointer to the OLRC's notes, which are context and get no rows)"]),
}
# the ten offices of (d)(9)(C)(iv), each a row, each a constructor of `Office of the intelligence community`
OFFICES = {
 "(I)": ["the Office of the Director of National Intelligence"],
 "(II)": ["the Central Intelligence Agency"],
 "(III)": ["the National Security Agency"],
 "(IV)": ["the Defense Intelligence Agency"],
 "(V)": ["the National Geospatial-Intelligence Agency"],
 "(VI)": ["the National Reconnaissance Office"],
 "(VII)": ["another office within the Department of Defense for the collection of specialized national intelligence through reconnaissance programs"],
 "(VIII)": ["an intelligence element of the Army", "an intelligence element of the Navy", "an intelligence element of the Air Force",
            "an intelligence element of the Marine Corps", "an intelligence element of the Federal Bureau of Investigation",
            "an intelligence element of the Department of Treasury", "an intelligence element of the Department of Energy",
            "an intelligence element of the Coast Guard"],
 "(IX)": ["the Bureau of Intelligence and Research of the Department of State"],
 "(X)": ["an element of the Department of Homeland Security concerned with the analyses of foreign intelligence information"],
}
for k, v in OFFICES.items():
    MAP["(d)(9)(C)(iv)" + k] = (ENC, [(N, "`Office of the intelligence community` constructor: " + "; ".join(v)),
                                     (D9, "s 121(d)(9)(C)(iv) the clause that names the office")], [TD9], [])

# defined-term rows: they share lines with the provision that defines or borrows them
TERMS = [
 ("term: divorce or separation instrument", (122, 0), "(d)(3)(C)", (ENC, [(D1, "s 121(d)(3)(C) the instrument is a divorce")], [TD1], [])),
 ("term: qualified official extended duty", (0, 0), "(d)(9)(C)(i)", (ENC, [(D9, "s 121(d)(9)(C)(i)")], [TD9], [])),
 ("term: uniformed services", (0, 0), "(d)(9)(C)(ii)", (ENC, [(D9, "s 121(d)(9)(C)(ii)")], [TD9], [])),
 ("term: member of the Foreign Service of the United States", (0, 0), "(d)(9)(C)(iii)", (ENC, [(D9, "s 121(d)(9)(C)(iii)")], [TD9], [])),
 ("term: employee of the intelligence community", (0, 0), "(d)(9)(C)(iv)", (ENC, [(D9, "s 121(d)(9)(C)(iv) the person is an employee")], [TD9], [])),
 ("term: extended duty", (0, 0), "(d)(9)(C)(v)", (ENC, [(D9, "s 121(d)(9)(C)(v)")], [TD9], [])),
 ("term: period of nonqualified use", (0, 0), "(b)(5)(C)(i)", (FORK, [(B, "s 121(b)(5)(C)(i)")], [TB], ["F22"])),
 ("term: 5-year period described in subsection (a)", (0, 0), "(a)", (ENC, [(A, "s 121(a) the 5-year period")], [TA], [])),
 ("term: tenant-stockholder, cooperative housing corporation (section 216)", (0, 0), "(d)(4)", (ENC, [(D1, "s 121(d)(4)(A)")], [TD1], ["borrowed term, asked as a fact"])),
 ("term: depreciation adjustments (section 1250(b)(3))", (0, 0), "(d)(6)", (ENC, [(D1, "s 121(d)(6)")], [TD1], ["borrowed term, asked as a fact"])),
 ("term: divorce or separation instrument kinds (section 1041(a) transfer)", (0, 0), "(d)(3)(A)", (ENC, [(D1, "s 121(d)(3)(A)")], [TD1], ["borrowed term, asked as a fact"])),
]

def defined(mod, prefix):
    if prefix.startswith("`Office"):
        return all(("`" + n + "`") in open(os.path.join(HERE, mod), encoding="utf-8").read() for n in prefix.split(": ", 1)[1].split("; "))
    src = open(os.path.join(HERE, mod), encoding="utf-8").read()
    return re.search(r"^`" + re.escape(prefix), src, re.M) is not None

rows, problems = [], []
paths = {u[2]: u for u in units}
for e in EXTRA:
    paths[e[2]] = [e[0], e[1], e[2]]
for p in paths:
    if p not in MAP:
        problems.append("no disposition for " + p)
for p in MAP:
    if p not in paths:
        problems.append("disposition for a unit that is not in the text: " + p)

def snippet(first):
    t = lines[first - 1].strip()
    t = re.sub(r"^\[?\((?:[a-z]|\d+|[A-Z]|[ivx]+|[IVX]+)\)\s*", "", t)
    return (t[:60] + "...") if len(t) > 60 else t

order = [EXTRA[0], EXTRA[1]] + [tuple(u) for u in units] + [EXTRA[2], EXTRA[3]]
for first, last, path in order:
    if path not in MAP:
        continue
    disp, rules, tests, notes = MAP[path]
    for m, pre in rules:
        if not defined(m, pre):
            problems.append("%s: rule not defined in %s: %s" % (path, m, pre))
    for t in tests:
        if not os.path.exists(os.path.join(HERE, t)):
            problems.append("%s: test file missing: %s" % (path, t))
    rows.append((path, first, last, snippet(first), disp, rules, tests, notes))
n_units = len(rows)
for name, _, base, (disp, rules, tests, notes) in TERMS:
    first, last = paths[base][0], paths[base][1]
    for m, pre in rules:
        if not defined(m, pre):
            problems.append("%s: rule not defined in %s: %s" % (name, m, pre))
    rows.append((name, first, last, "(the defining or borrowing provision is row " + base + ")", disp, rules, tests, notes))

covered = set()
for r in rows:
    for ln in range(r[1], r[2] + 1):
        covered.add(ln)
uncovered = [i for i, l in enumerate(lines, 1) if l.strip() and i not in covered]
if uncovered:
    problems.append("lines in no row: " + ",".join(map(str, uncovered)))

def cell(r):
    path, first, last, snip, disp, rules, tests, notes = r
    rl = "; ".join("%s: %s" % (m.replace(".l4", ""), pre if len(pre) < 70 else pre[:67] + "...") for m, pre in rules) or "none"
    tl = ", ".join(t.replace(".l4", "") for t in tests) or "none"
    fk = ", ".join(notes) if notes else ""
    rng = str(first) if first == last else "%d-%d" % (first, last)
    return "| %s | %s | %s | %s | %s | %s | %s |" % (path, rng, snip.replace("|", "/"), disp, rl, tl, fk)

if "--audit" not in sys.argv or "--table" in sys.argv:
    print("| row | lines | text | disposition | rule (module: name begins) | tests | forks / reason |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        print(cell(r))
    print()
if "--table" not in sys.argv:
    from collections import Counter
    cnt = Counter(r[4] for r in rows)
    nonblank = sum(1 for l in lines if l.strip())
    print("audit: text lines %d, non-blank %d, covered by a row %d, uncovered %d" % (len(lines), nonblank, nonblank - len(uncovered), len(uncovered)))
    print("audit: rows from the text's units %d (of which the office rows %d), defined-term rows added %d, rows in all %d" % (n_units, len(OFFICES), len(TERMS), len(rows)))
    print("audit: dispositions " + ", ".join("%s %d" % (k, cnt[k]) for k in (ENC, FORK, INERT, REP)))
    inert1 = sum(1 for r in rows if r[4] == INERT and r[7] and r[7][0].startswith("1:"))
    print("audit: inert rows by reason: 1 -> %d, 2 -> 0, 3 -> 0" % inert1)
    print("audit: problems %d" % len(problems))
for p in problems:
    print("PROBLEM:", p)
sys.exit(1 if problems else 0)
