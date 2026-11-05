#!/usr/bin/env python3
"""Coverage table for the Minors' Contracts Act 1987 row.

Usage (run with -I, from the encoding folder):
  python3 -I coverage.py RAW.txt                 check the table and print the counts
  python3 -I coverage.py RAW.txt --markdown      print the table as markdown
  python3 -I coverage.py RAW.txt --notes NOTES.md [--brief BRIEF.md]
                                                 rewrite the marked regions of NOTES.md: the coverage table
                                                 and the verbatim rulings (copied from BRIEF.md by script)
  python3 -I coverage.py RAW.txt --verify-notes NOTES.md
                                                 check that every `name` (file.l4:LINE) reference in NOTES.md
                                                 points at a line that defines that name

A PRIMARY row covers lines of the text and the primary rows PARTITION the non-blank lines: every non-blank
line is in exactly one primary row (checked here).  A SUB row refines lines already covered by a primary
row (a limb, a parenthesis, a defined term, an entry of a table); it adds a disposition of its own and
cannot leave a line uncovered.  Dispositions: encoded, inert (reason 1, 2 or 3), fork, repealed.
"""
import re
import sys
import glob
import os

# (id, kind, first line, last line, text of the unit, disposition, reason-or-pointer)
# kind: P primary, S sub.  disposition: encoded | inert | fork | repealed
# pointer for encoded/fork rows: the L4 rules (backticked names must exist as definitions in mca-*.l4)
ROWS = [
    ("P01", "P", 1, 4, "Title block: The Statutes of the Republic of Singapore; Minors' Contracts Act 1987; 2020 Revised Edition", "inert", "reason 1 (not operative: title)"),
    ("P02", "P", 6, 7, "Revised-edition statement: incorporates amendments to 1 December 2021, comes into operation on 31 December 2021", "inert", "reason 2 (machinery: the revised edition's own commencement)"),
    ("P03", "P", 9, 13, "Publisher legend: Law Revision Commission; Revised Edition of the Laws Act 1983", "inert", "reason 1 (not operative)"),
    ("P04", "P", 15, 16, "Banner: Informal Consolidation, version in force from 1/4/2022; 2020 Ed.", "inert", "reason 1 (not operative; it names the version encoded)"),
    ("P05", "P", 18, 18, "Running title", "inert", "reason 1 (not operative: title)"),
    ("P06", "P", 20, 26, "Arrangement of sections", "inert", "reason 1 (not operative: headings)"),
    ("P07", "P", 28, 28, "Long title: An Act to amend the law relating to minors' contracts", "inert", "reason 1 (not operative: long title)"),
    ("P08", "P", 29, 29, "[12 November 1993]", "inert", "reason 2 (machinery: the date the Act took effect in Singapore; s 4 states its own 12 November 1993, which is encoded in P27)"),
    ("P09", "P", 31, 31, "Heading of s 1: Disapplication of Infants Relief Act 1874", "inert", "reason 1 (not operative: heading)"),
    ("P10", "P", 32, 36, "s 1: the Infants Relief Act 1874 shall not apply to any contract made by a minor after 9 April 1987", "fork", "F2, F7; `s 1 the disapplication reaches the contract`, `s 1 the Infants Relief Act 1874 applies to the contract`, `s 1 the Infants Relief Act 1874 invalidates the contract`, `s 1 the Infants Relief Act 1874 bars an action on the contract ratified after majority`"),
    ("P11", "P", 38, 38, "Heading of s 2: Guarantees", "inert", "reason 1 (not operative: heading)"),
    ("P12", "P", 39, 39, "s 2 chapeau: Where --", "encoded", "`s 2 the guarantee is saved from unenforceability on that ground alone` (a failed \"where\" is JUST FALSE: ruling of 2026-11-05 (b))"),
    ("P13", "P", 40, 41, "s 2(a): a guarantee is given in respect of an obligation of a party to a contract made after 9 April 1987", "encoded", "`s 2(a) a guarantee is given in respect of an obligation of a party to a contract made after 9 April 1987` (date: F2)"),
    ("P14", "P", 42, 44, "s 2(b): the obligation is unenforceable against him (or he repudiates the contract) because he was a minor when the contract was made", "fork", "F1; `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made`"),
    ("P15", "P", 46, 47, "s 2 tail: the guarantee shall not for that reason alone be unenforceable against the guarantor", "encoded", "`s 2 the guarantee is unenforceable against the guarantor for that reason alone`"),
    ("P16", "P", 49, 49, "Heading of s 3: Restitution", "inert", "reason 1 (not operative: heading)"),
    ("P17", "P", 50, 50, "s 3(1) chapeau: 3.-(1) Where --", "encoded", "`s 3(1) the conditions for the court's power are met`"),
    ("P18", "P", 51, 52, "s 3(1)(a): a person (the claimant) has after 9 April 1987 entered into a contract with another (the defendant)", "encoded", "`s 3(1)(a) the claimant has after 9 April 1987 entered into a contract with the defendant` (date: F2)"),
    ("P19", "P", 54, 54, "Page number 1", "inert", "reason 1 (not operative: page furniture)"),
    ("P20", "P", 56, 57, "Page header: Informal Consolidation banner; 2020 Ed. Minors' Contracts Act 1987, page 2", "inert", "reason 1 (not operative: page furniture)"),
    ("P21", "P", 59, 61, "s 3(1)(b): the contract is unenforceable against the defendant (or he repudiates it) because he was a minor when the contract was made", "fork", "F1; `s 3(1)(b) the contract is unenforceable against the defendant, or he repudiates it, because he was a minor when the contract was made`"),
    ("P22", "P", 63, 65, "s 3(1) tail: the court may, if it is just and equitable to do so, require the defendant to transfer to the claimant any property acquired by the defendant under the contract, or any property representing it", "fork", "F4; `s 3(1) the court may require the defendant to transfer property to the claimant`, `s 3(1) the property is within what the court may require to be transferred`, `s 3(1) the court's permission to require the transfer`"),
    ("P23", "P", 67, 67, "Amendment note: [Act 25 of 2021 wef 01/04/2022]", "inert", "reason 1 (not operative: an editorial note; the amendment's effect is in the in-force wording encoded; the pre-amendment wording is not among the sources)"),
    ("P24", "P", 69, 70, "s 3(2): Nothing in this section shall be taken to prejudice any other remedy available to the claimant", "fork", "F5; `s 3(2) this section prejudices another remedy available to the claimant`"),
    ("P25", "P", 72, 72, "Amendment note: [Act 25 of 2021 wef 01/04/2022]", "inert", "reason 1 (not operative: an editorial note)"),
    ("P26", "P", 74, 74, "Heading of s 4: Contracts before 12 November 1993", "inert", "reason 1 (not operative: heading)"),
    ("P27", "P", 76, 79, "s 4: Nothing in this Act applies in relation to a contract made after 9 April 1987 and before 12 November 1993 except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before 12 November 1993", "fork", "QA, F2, F3, F6; `s 4 this Act is barred from applying to the contract`, `s 4 the provision of this Act is open to apply to the contract`, `s 4 what this section does to a provision of this Act`, `s 4 the band a contract made on a day falls in`"),
    ("P28", "P", 81, 81, "Heading of s 5: Short title", "inert", "reason 1 (not operative: heading)"),
    ("P29", "P", 82, 82, "s 5: This Act may be cited as the Minors' Contracts Act 1987", "inert", "reason 2 (machinery: short title)"),
    ("P30", "P", 84, 84, "Banner: Informal Consolidation, version in force from 1/4/2022", "inert", "reason 1 (not operative: page furniture)"),
    ("P31", "P", 85, 86, "Legislative History: title lines", "inert", "reason 1 (not operative: the history is not part of the Act, line 89)"),
    ("P32", "P", 88, 89, "Statement that the Legislative History is a service, not part of the Act", "inert", "reason 1 (not operative)"),
    ("P33", "P", 91, 120, "Legislative History entries 1 to 4", "inert", "reason 1 (not operative: not part of the Act, line 89; see finding 8 on 'sections 1(b) and 4(1)' and fork F11 on '9 June 1987')"),
    ("P34", "P", 122, 123, "Banner and page number ii", "inert", "reason 1 (not operative: page furniture)"),
    ("P35", "P", 125, 125, "Heading: Abbreviations", "inert", "reason 1 (not operative: heading)"),
    ("P36", "P", 127, 152, "Abbreviations table", "inert", "reason 1 (not operative: a glossary of the abbreviations used in the legislative history)"),
    ("P37", "P", 154, 154, "Banner: Informal Consolidation, version in force from 1/4/2022", "inert", "reason 1 (not operative: page furniture)"),
    # ---- sub rows
    ("S01", "S", 22, 22, "Arrangement entry 1: Disapplication of Infants Relief Act 1874", "inert", "reason 1 (heading)"),
    ("S02", "S", 23, 23, "Arrangement entry 2: Guarantees", "inert", "reason 1 (heading)"),
    ("S03", "S", 24, 24, "Arrangement entry 3: Restitution", "inert", "reason 1 (heading)"),
    ("S04", "S", 25, 25, "Arrangement entry 4: Contracts before 12 November 1993", "inert", "reason 1 (heading)"),
    ("S05", "S", 26, 26, "Arrangement entry 5: Short title", "inert", "reason 1 (heading)"),
    ("S06", "S", 32, 32, "s 1 names the Infants Relief Act 1874 (a statute not among the sources)", "encoded", "named in `s 1 the Infants Relief Act 1874 applies to the contract`; what it says is not asked: s 1 only turns it off"),
    ("S07", "S", 32, 35, "s 1 parenthesis: (which invalidates certain contracts made by minors and prohibits actions to enforce contracts ratified after majority)", "encoded", "`s 1 the effects the Act describes the Infants Relief Act 1874 as having`, `s 1 the Infants Relief Act 1874 invalidates the contract`, `s 1 the Infants Relief Act 1874 bars an action on the contract ratified after majority`; F7"),
    ("S08", "S", 35, 36, "s 1 scope: any contract made by a minor after 9 April 1987", "fork", "F2; `s 1 the contract was made by a minor after 9 April 1987`"),
    ("S09", "S", 42, 43, "s 2(b) parenthesis: (or he repudiates the contract)", "fork", "F1; read inside `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made`"),
    ("S10", "S", 51, 51, "Defined term: the claimant", "encoded", "`s 3(1)(a) the terms the Act defines`, `s 3(1)(a) the Act's definition of`"),
    ("S11", "S", 51, 52, "Defined term: the defendant", "encoded", "`s 3(1)(a) the terms the Act defines`, `s 3(1)(a) the Act's definition of`"),
    ("S12", "S", 51, 51, "s 3(1)(a) 'a person' (read through the Interpretation Act 1965 s 2(1))", "encoded", "`s 3(1)(a) the Act's word a person reaches the claimant` (mca-reading.l4)"),
    ("S13", "S", 42, 43, "s 2(b) 'him', 'he' (read through the Interpretation Act 1965 s 2(1))", "encoded", "`ss 2(b) and 3(1)(b) the masculine word he reaches the party` (mca-reading.l4)"),
    ("S14", "S", 59, 60, "s 3(1)(b) parenthesis: (or he repudiates it)", "fork", "F1; read inside `s 3(1)(b) the contract is unenforceable against the defendant, or he repudiates it, because he was a minor when the contract was made`"),
    ("S15", "S", 63, 63, "s 3(1): if it is just and equitable to do so", "encoded", "judgment taken as a plain input, `s 3(1) the court may require the defendant to transfer property to the claimant`"),
    ("S16", "S", 64, 65, "s 3(1): any property acquired by the defendant under the contract, or any property representing it", "encoded", "`s 3(1) the property is within what the court may require to be transferred`; F4"),
    ("S17", "S", 63, 64, "s 3(1): require the defendant to transfer to the claimant", "encoded", "`s 3(1) the property is within what the court may require to be transferred` (the transferee), `s 3(1) the court's permission to require the transfer`"),
    ("S18", "S", 69, 70, "s 3(2): any other remedy available to the claimant", "encoded", "`s 3(2) this section prejudices another remedy available to the claimant`; F5"),
    ("S19", "S", 76, 77, "s 4: a contract made after 9 April 1987 and before 12 November 1993 (the band)", "encoded", "`s 4 the band a contract made on a day falls in` (F2)"),
    ("S20", "S", 77, 79, "s 4: except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before 12 November 1993", "fork", "QA, F6; `s 4 what this section does to a provision of this Act`, `s 4 this Act is barred from applying to the contract`"),
    ("S21", "S", 78, 78, "s 4 names section 5 of the Civil Law Act 1909 (an Act not among the sources)", "encoded", "taken as the input `section 5 of the Civil Law Act 1909 made the provision applicable` (mca-nouns.l4), listed under Dependencies"),
    ("S22", "S", 91, 101, "History entry 1: U.K. 1987, c. 13; commencement 9 June 1987; application 12 November 1993 (except sections 1(b) and 4(1)); note on the Application of English Law Act 1993", "inert", "reason 1 (not part of the Act)"),
    ("S23", "S", 103, 105, "History entry 2: 1994 Revised Edition; operation 20 May 1994", "inert", "reason 1 (not part of the Act)"),
    ("S24", "S", 107, 109, "History entry 3: 2020 Revised Edition; operation 31 December 2021", "inert", "reason 1 (not part of the Act)"),
    ("S25", "S", 111, 120, "History entry 4: Act 25 of 2021 (Courts (Civil and Criminal Justice) Reform Act 2021) s 163; commencement 1 April 2022", "inert", "reason 1 (not part of the Act)"),
]


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def abbreviation_rows(lines):
    """One sub row per entry of the abbreviations table (lines 127 to 152).
    An entry starts at a line with little indent; a line indented by 10 or more continues the entry before it,
    even across a blank line (the table wraps long entries)."""
    groups = []
    for no in range(127, 153):
        txt = lines[no - 1]
        if not txt.strip():
            continue
        indent = len(txt) - len(txt.lstrip(" "))
        if indent >= 10 and groups:
            groups[-1].append(no)
        else:
            groups.append([no])
    rows = []
    for n, g in enumerate(groups, 1):
        text = "Abbreviation: " + " ".join(lines[x - 1].strip() for x in g)
        rows.append(("A%02d" % n, "S", g[0], g[-1], text, "inert", "reason 1 (not operative: glossary entry)"))
    return rows


def l4_files(here):
    return sorted(f for f in glob.glob(os.path.join(here, "mca-*.l4")))


def defined_names(here):
    """Map: name -> list of (file, line) where a definition starts with that backticked name at column 1,
    or where a DECLARE / constructor line mentions it."""
    out = {}
    for f in l4_files(here):
        with open(f, encoding="utf-8") as fh:
            for i, ln in enumerate(fh, 1):
                for m in re.finditer(r"`([^`]+)`", ln):
                    out.setdefault(m.group(1), []).append((os.path.basename(f), i, ln))
    return out


def check(rawpath, here):
    lines = read_lines(rawpath)
    rows = ROWS + abbreviation_rows(lines)
    problems = []
    nonblank = [i for i, ln in enumerate(lines, 1) if ln.strip()]
    covered = {}
    for rid, kind, a, b, text, disp, why in rows:
        if kind == "P":
            for i in range(a, b + 1):
                if lines[i - 1].strip():
                    covered.setdefault(i, []).append(rid)
    for i in nonblank:
        c = covered.get(i, [])
        if len(c) == 0:
            problems.append("line %d is in no primary row: %r" % (i, lines[i - 1]))
        elif len(c) > 1:
            problems.append("line %d is in %d primary rows: %s" % (i, len(c), c))
    for rid, kind, a, b, text, disp, why in rows:
        if disp not in ("encoded", "inert", "fork", "repealed"):
            problems.append("%s: bad disposition %r" % (rid, disp))
        if disp == "inert" and not re.match(r"reason [123]\b", why):
            problems.append("%s: inert without reason 1, 2 or 3" % rid)
        if disp in ("encoded", "fork") and not why:
            problems.append("%s: no pointer" % rid)
        if kind == "S":
            prim = [r for r in rows if r[1] == "P" and r[2] <= a and b <= r[3]]
            if not prim:
                problems.append("%s: sub row %d-%d lies inside no primary row" % (rid, a, b))
        # pointers: every backticked name must be defined or declared in some mca-*.l4
    names = defined_names(here)
    for rid, kind, a, b, text, disp, why in rows:
        if disp in ("encoded", "fork"):
            for m in re.finditer(r"`([^`]+)`", why):
                nm = m.group(1)
                if nm not in names:
                    problems.append("%s: pointer `%s` is not in any mca-*.l4" % (rid, nm))
    return rows, nonblank, problems


def counts(rows):
    c = {}
    for kind in ("P", "S"):
        for rid, k, a, b, text, disp, why in rows:
            if k != kind:
                continue
            key = disp if disp != "inert" else "inert (%s)" % re.match(r"(reason \d)", why).group(1)
            c.setdefault((kind, key), 0)
            c[(kind, key)] += 1
    return c


def markdown(rows, lines):
    out = []
    out.append("| row | lines | provision (the Act's words, shortened) | disposition | pointer or reason |")
    out.append("| --- | --- | --- | --- | --- |")
    for rid, kind, a, b, text, disp, why in rows:
        rng = str(a) if a == b else "%d-%d" % (a, b)
        text = re.sub(r"\s+", " ", text)
        out.append("| %s | %s | %s | %s | %s |" % (rid, rng, text.replace("|", "/"), disp, why.replace("|", "/")))
    return "\n".join(out)


def replace_region(text, name, body):
    pat = re.compile(r"(<!-- %s:BEGIN -->\n).*?(\n<!-- %s:END -->)" % (name, name), re.S)
    if not pat.search(text):
        raise SystemExit("NOTES.md has no <!-- %s:BEGIN --> ... <!-- %s:END --> region" % (name, name))
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text)


def verify_notes(notes_path, here):
    problems = []
    with open(notes_path, encoding="utf-8") as f:
        text = f.read()
    n = 0
    # pattern: `name` (file.l4:LINE)  or  `name` | file.l4:LINE
    for m in re.finditer(r"`([^`]+)`\s*(?:\(|\|\s*)(mca-[a-z0-9-]+\.l4):(\d+)", text):
        name, fn, line = m.group(1), m.group(2), int(m.group(3))
        n += 1
        path = os.path.join(here, fn)
        try:
            with open(path, encoding="utf-8") as fh:
                src = fh.read().split("\n")
        except OSError:
            problems.append("%s:%d: no such file" % (fn, line))
            continue
        if not (1 <= line <= len(src)) or ("`" + name + "`") not in src[line - 1]:
            problems.append("`%s` is not on %s:%d" % (name, fn, line))
    # references written "at mca-x.l4:N" or "at mca-x.l4:N-M": check that the lines exist and are not blank
    for m in re.finditer(r"\bat (mca-[a-z0-9-]+\.l4):(\d+)(?:-(\d+))?", text):
        fn, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        n += 1
        try:
            with open(os.path.join(here, fn), encoding="utf-8") as fh:
                src = fh.read().split("\n")
        except OSError:
            problems.append("%s:%d: no such file" % (fn, a))
            continue
        if not (1 <= a <= b <= len(src)) or any(not src[k - 1].strip() for k in range(a, b + 1)):
            problems.append("%s:%d-%d: a line is out of range or blank" % (fn, a, b))
    return n, problems


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    raw = args[0]
    here = os.path.dirname(os.path.abspath(__file__))
    if "--verify-notes" in args:
        n, problems = verify_notes(args[args.index("--verify-notes") + 1], here)
        for p in problems:
            print("PROBLEM:", p)
        print("verify-notes: %d line references checked, %d problems" % (n, len(problems)))
        return 1 if problems else 0
    rows, nonblank, problems = check(raw, here)
    lines = read_lines(raw)
    if "--markdown" in args:
        print(markdown(rows, lines))
    if "--notes" in args:
        npath = args[args.index("--notes") + 1]
        with open(npath, encoding="utf-8") as f:
            text = f.read()
        text = replace_region(text, "COVERAGE", markdown(rows, lines))
        if "--brief" in args:
            bpath = args[args.index("--brief") + 1]
            with open(bpath, encoding="utf-8") as f:
                brief = f.read().split("\n")
            want = ("- **E1** (", "- **N2** (", "- **Periods, \"where\" and scope limits** (", "- **Delegated definitions, defences and \"until\" bars** (")
            picked = [ln for ln in brief if ln.startswith(want)]
            if len(picked) != 4:
                problems.append("expected 4 ruling bullets in the brief, found %d" % len(picked))
            else:
                text = replace_region(text, "RULINGS", "\n".join(picked))
        with open(npath, "w", encoding="utf-8") as f:
            f.write(text)
    c = counts(rows)
    prim = [r for r in rows if r[1] == "P"]
    sub = [r for r in rows if r[1] == "S"]
    print("text lines (newlines): %d; non-blank lines: %d; words: %d" % (sum(1 for _ in open(raw, encoding="utf-8").read() if _ == "\n"), len(nonblank), sum(len(ln.split()) for ln in lines)))
    print("primary rows (partition of the non-blank lines): %d; sub rows (limbs, parentheses, defined terms, table entries): %d; total rows: %d" % (len(prim), len(sub), len(rows)))
    for kind, label in (("P", "primary"), ("S", "sub")):
        print(label + " dispositions: " + ", ".join("%s %d" % (k[1], v) for k, v in sorted(c.items()) if k[0] == kind))
    allc = {}
    for (kind, key), v in c.items():
        allc[key] = allc.get(key, 0) + v
    print("all rows by disposition: " + ", ".join("%s %d" % (k, v) for k, v in sorted(allc.items())))
    for p in problems:
        print("PROBLEM:", p)
    print("coverage check: %d problems" % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
