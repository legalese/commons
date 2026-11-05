#!/usr/bin/env python3
"""List every branch of the layer-1 modules that rests on one of the readings flagged "for a lawyer", and write the list
into NOTES.md between <!-- BEGIN marginal --> and <!-- END marginal -->.

  python3 -I marginal.py NOTES.md

Reading (a): a failed "if", an "unless" that applies, or a requirement ("must ...") that is not met, answers JUST FALSE.  Tag: `marginal reading (a)`.
Reading (c): a contrary affirmative statement answers JUST FALSE ("disregarded" is false because the text says "reckoned").  Tag: `marginal reading (c)`.
Reading (b): a grant or prohibition limited by its own wording does not answer no outside the limit: NOTHING.  Tag:
`NOTHING-kind (limited by its own wording)`.
The branches are found by those tags in the comments of the rra-part*.l4 files, so the list cannot drift from the code.
"""
import glob, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
rows = {"a": [], "c": [], "b": [], "ra": [], "rb": [], "rab": []}
for fn in sorted(glob.glob(os.path.join(here, "rra-part*.l4"))):
    rule = None
    for i, l in enumerate(open(fn, encoding="utf-8"), 1):
        m = re.match(r"^`(s [^`]*)`\s", l)
        if m: rule = m.group(1)
        if "-- FALSE-kind" in l and "ruled 2026-11-05 (a) and (b)" in l: rows["rab"].append((os.path.basename(fn), i, rule))
        elif "-- FALSE-kind" in l and "ruled 2026-11-05 (a)" in l: rows["ra"].append((os.path.basename(fn), i, rule))
        elif "-- FALSE-kind" in l and "ruled 2026-11-05 (b)" in l: rows["rb"].append((os.path.basename(fn), i, rule))
        elif "-- FALSE-kind" in l and "marginal reading (a)" in l: rows["a"].append((os.path.basename(fn), i, rule))
        elif "-- FALSE-kind" in l and "marginal reading (c)" in l: rows["c"].append((os.path.basename(fn), i, rule))
        elif "-- NOTHING-kind (limited by its own wording)" in l: rows["b"].append((os.path.basename(fn), i, rule))
def group(rs):
    g = {}
    for fn, i, rule in rs: g.setdefault((fn, rule), []).append(i)
    return g
out = []
out.append("These counts are produced by `marginal.py` from the tags in the code, so they cannot drift from it.")
out.append("")
nr = len(rows["ra"]) + len(rows["rb"]) + len(rows["rab"])
out.append(f"**Ruled 2026-11-05: a period the text fixes in its own words, and a \"where\" condition, answer `JUST FALSE` outside the period or when the condition fails ({nr} branches).** These are not marginal: the ruling is in the fork register beside rulings E1 and N2. They are listed so that a lawyer sees every place it is used; (a) is a period, (b) is a \"where\" (which includes \"when\", \"upon\" and \"whenever\": ruled 2026-11-05 at 06:04, fork F24).")
out.append("")
out.append("| Rule | File | Lines | Ruling |"); out.append("| --- | --- | --- | --- |")
for key, lab in (("ra", "(a)"), ("rb", "(b)"), ("rab", "(a) and (b)")):
    for (fn, rule), ls in group(rows[key]).items(): out.append(f"| `{rule}` | {fn} | {', '.join(map(str, ls))} | {lab} |")
out.append("")
out.append(f"**Reading (a): a failed \"if\", an \"unless\" that applies, or a \"must\" that is not met, is the text's no ({len(rows['a'])} branches).** It covers, among others, section 7B(1) (\"Unless otherwise agreed\", fork F8), section 7C(4) (\"the payment is (a) ... or (b)\", read as naming the only two forms, fork F11), sections 7A(3)(a)(ii) and 8C(1) (a permission \"if\" its condition holds, forks F20 and F21), and the carry of section 7(1)'s no into section 7A(1) (fork F19). The other reading: \"if A then B\" does not itself say \"if not A then not B\", and \"must\" says what is required, not that its absence is a no, so each of these would answer `NOTHING`.")
out.append("")
out.append("| Rule | File | Lines |"); out.append("| --- | --- | --- |")
for (fn, rule), ls in group(rows["a"]).items(): out.append(f"| `{rule}` | {fn} | {', '.join(map(str, ls))} |")
out.append("")
out.append(f"**Reading (c): the text's own contrary affirmative is read as its no ({len(rows['c'])} branches).** Section 7B(1) disregards earlier service, \"subject to\" section 7B(2), which reckons it for annual leave and paid sick leave, so \"disregarded for annual leave\" is answered `JUST FALSE`; and section 2(3) says a person is regarded as attaining an age on or after the anniversary, so a date before it answers `JUST FALSE` to \"has attained\" (fork F2). The other reading answers `NOTHING`: the text says what is reckoned, or when a person is regarded as attaining, and does not say what is not.")
out.append("")
out.append("| Rule | File | Lines |"); out.append("| --- | --- | --- |")
for (fn, rule), ls in group(rows["c"]).items(): out.append(f"| `{rule}` | {fn} | {', '.join(map(str, ls))} |")
out.append("")
out.append(f"**Reading (b): a grant or prohibition limited by its own wording does not answer no outside the limit ({len(rows['b'])} branches, over {len(group(rows['b']))} rules).** Every one answers `NOTHING`. Ruled 2026-11-05 (c): a scope limit with no \"only\" answers `NOTHING` outside the scope; the limits that are a period or a \"where\" are in the ruled table above and are not counted here. The other reading, now ruled out for a scope limit: outside the limit the text means no, so each would answer `JUST FALSE` (for a grant, \"may ... if the conditions hold\" would mean \"may not otherwise\"; for a duty or bar, \"applies to X\" would mean \"does not apply to anyone else\").")
out.append("")
out.append("| Rule | File | Lines |"); out.append("| --- | --- | --- |")
for (fn, rule), ls in group(rows["b"]).items(): out.append(f"| `{rule}` | {fn} | {', '.join(map(str, ls))} |")
body = "\n".join(out)
if len(sys.argv) > 1:
    txt = open(sys.argv[1], encoding="utf-8").read()
    pat = re.compile(r"(<!-- BEGIN marginal -->\n).*?(\n<!-- END marginal -->)", re.S)
    if not pat.search(txt): sys.exit("NOTES.md has no marginal markers")
    open(sys.argv[1], "w", encoding="utf-8").write(pat.sub(lambda m: m.group(1) + body + m.group(2), txt))
    print(f"wrote marginal readings: ruled {nr} (a {len(rows['ra'])}, b {len(rows['rb'])}, both {len(rows['rab'])}), (a) {len(rows['a'])}, (c) {len(rows['c'])}, (b) {len(rows['b'])} branches")
else:
    print(body)
