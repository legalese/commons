#!/usr/bin/env python3
"""Coverage table for the Frustrated Contracts Act 1959 text, built from the text itself.

  python3 -I coverage.py RAW [--table]      audit (and with --table, print the markdown table for NOTES.md)

RAW is FCA1959.txt (the deposited plain-text rendering).  Each ROW below names the raw lines (1-based, split on "\\n") it
covers.  The audit reads RAW and checks that
  * every non-blank line of RAW falls in at least one primary row (rows with overlay=False);
  * no primary row names a line past the end of RAW, and no primary row covers only blank lines;
  * the first line of each operative row really starts with the provision's marker (so a regenerated, shifted raw file fails loudly).
It prints the counts per disposition.  Dispositions: encoded | inert (reason 1, 2 or 3) | fork | repealed.
"""
import os
import re
import sys

# (id, label, ranges, kind, disposition, inert_reason, where, overlay)
# 'where' is the L4 function(s) that encode the row, or the reason for inert.
ROWS = [
    ("R01", "Cover page: title, edition banner, publisher", [(1, 14)], "front matter", "inert", 1,
     "Not operative: title, edition banner (2020 Revised Edition, in operation 31 December 2021), publisher.", False),
    ("R02", "Arrangement of Sections (as the converter printed it, garbled)", [(16, 23)], "contents list", "inert", 1,
     "Not operative: a table of contents.  The converter has split each entry across lines (finding 1).", False),
    ("R03", "Long title: 'An Act relating to the frustration of contracts.'", [(25, 25)], "long title", "inert", 1,
     "Not operative: long title.", False),
    ("R04", "Date of enactment: [13 February 1959]", [(27, 27)], "enactment date", "inert", 1,
     "Not operative: the date of enactment.  The same date is used by s 3(1) as a date the Act's application does not depend on (R18).", False),
    ("R05", "Heading: 'Short title'", [(29, 29)], "heading", "inert", 1, "Not operative: heading.", False),
    ("R06", "s 1: This Act is the Frustrated Contracts Act 1959.", [(31, 31)], "section", "inert", 2,
     "Machinery: the short title.", False),
    ("R07", "Heading of s 2: 'Adjustment of rights and liabilities of parties to frustrated contracts'", [(33, 34)], "heading", "inert", 1,
     "Not operative: heading.", False),
    ("R08", "s 2(1): when section 2 has effect", [(36, 40)], "subsection", "fork", None, "@S21", False),
    ("R09", "s 2(2): sums paid are recoverable; sums payable cease to be payable", [(42, 47)], "subsection", "fork", None, "@S22", False),
    ("R10", "s 2(3): the court may allow expenses to be retained or recovered", [(49, 53), (60, 61)], "subsection", "fork", None, "@S23", False),
    ("R11", "s 2(4) (chapeau): a sum is recoverable for a valuable benefit", [(63, 70)], "subsection", "fork", None, "@S24", False),
    ("R12", "s 2(4)(a): the benefited party's expenses", [(72, 77)], "paragraph", "encoded", None, "@S24a", False),
    ("R13", "s 2(4)(b): the effect of the circumstances giving rise to the frustration", [(79, 80)], "paragraph", "encoded", None, "@S24b", False),
    ("R14", "s 2(5): overhead expenses and personal work in estimating expenses", [(82, 86)], "subsection", "encoded", None, "@S25", False),
    ("R15", "s 2(6): insurance sums are not taken into account", [(88, 94)], "subsection", "fork", None, "@S26", False),
    ("R16", "s 2(7): a benefit conferred on another person treated as obtained by the obligor", [(96, 100), (103, 104)], "subsection", "encoded", None, "@S27", False),
    ("R17", "Heading of s 3: 'Provision as to application of Act'", [(106, 106)], "heading", "inert", 1,
     "Not operative: heading.", False),
    ("R18", "s 3(1): which contracts the Act applies to, by the time of discharge", [(108, 111)], "subsection", "encoded", None, "@S31", False),
    ("R19", "s 3(2): contracts to which the Government is a party", [(113, 114)], "subsection", "encoded", None, "@S32", False),
    ("R20", "s 3(3): the contract's own provision for frustration", [(116, 123)], "subsection", "encoded", None, "@S33", False),
    ("R21", "s 3(4): severance of a part wholly performed", [(125, 132)], "subsection", "encoded", None, "@S34", False),
    ("R22", "s 3(5) (chapeau): the Act shall not apply to (a), (b) or (c)", [(134, 134)], "subsection", "encoded", None, "@S35", False),
    ("R23", "s 3(5)(a): charterparties and carriage of goods by sea", [(136, 139)], "paragraph", "fork", None, "@S35a", False),
    ("R24", "s 3(5)(b): contracts of insurance, except as provided by s 2(6)", [(140, 141)], "paragraph", "fork", None, "@S35b", False),
    ("R25", "s 3(5)(c): s 7 Sale of Goods Act 1979 and other contracts for the sale of specific goods that have perished", [(143, 146), (149, 153)], "paragraph", "fork", None, "@S35c", False),
    ("R26", "Legislative History: heading and statement that it is not part of the Act", [(154, 158)], "legislative history", "inert", 1,
     "Not operative: line 157-158 says 'It is not part of the Act'.", False),
    ("R27", "Legislative History entry 1: Ordinance 6 of 1959 (commencement 13 February 1959)", [(160, 169)], "legislative history row", "inert", 1,
     "Not operative: history of the text, not part of the Act.", False),
    ("R28", "Legislative History entry 2: L.N. 40/1965 (commencement 18 February 1965)", [(171, 175)], "legislative history row", "inert", 1,
     "Not operative: history of the text.", False),
    ("R29", "Legislative History entry 3: 1970 Revised Edition (operation 1 March 1971)", [(177, 179)], "legislative history row", "inert", 1,
     "Not operative: history of the text.", False),
    ("R30", "Legislative History entry 4: 1985 Revised Edition (operation 30 March 1987)", [(181, 183)], "legislative history row", "inert", 1,
     "Not operative: history of the text.", False),
    ("R31", "Legislative History entry 5: Act 7 of 1997, Statutes (Miscellaneous Amendments) Act 1997 (1 October 1997)", [(185, 196)], "legislative history row", "inert", 1,
     "Not operative: history of the text (an amendment already made into the text above).", False),
    ("R32", "Legislative History entry 6: 2014 Revised Edition (operation 31 July 2014)", [(198, 200)], "legislative history row", "inert", 1,
     "Not operative: history of the text.", False),
    ("R33", "Abbreviations: heading", [(205, 205)], "heading", "inert", 1, "Not operative: heading.", False),
    ("R34", "Abbreviation C.P. (Council Paper)", [(207, 207)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R35", "Abbreviation G.N. No. S (N.S.)", [(209, 209)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R36", "Abbreviation G.N. No.", [(211, 211)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R37", "Abbreviation G.N. No. S", [(213, 213)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R38", "Abbreviation G.N. Sp. No. S", [(215, 215)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R39", "Abbreviation L.A. (Legislative Assembly)", [(217, 217)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R40", "Abbreviation L.N. (Legal Notification)", [(219, 221)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R41", "Abbreviation M. Act", [(223, 223)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R42", "Abbreviation M. Ordinance", [(225, 225)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R43", "Abbreviation Parl.", [(227, 227)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R44", "Abbreviation S.S.G.G. (E) No.", [(229, 230)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R45", "Abbreviation S.S.G.G. No.", [(232, 232)], "abbreviation row", "inert", 1, "Not operative: key to the legislative history.", False),
    ("R46", "Page furniture: page numbers, running heads, the date stamp 31.12.2021", [(55, 55), (57, 58), (101, 101), (147, 148), (202, 203)], "page furniture", "inert", 1,
     "Not operative: printed page numbers and running heads (lines 55, 57, 58, 101, 147, 148, 202, 203; line 233 is a form feed and blank).", False),
    # --- overlay rows: defined terms and labels (they sit inside the operative rows above; not needed for the line audit)
    ("T01", "Defined term: 'the time of discharge' (s 2(2))", [(43, 45)], "defined term", "encoded", None, "@TERM_TOD", True),
    ("T02", "Label: 'the benefited party' (s 2(4)(a))", [(72, 73)], "defined term", "encoded", None, "@TERM_BP", True),
]


# where each operative row is encoded: (file, function name) pairs resolved to file:line by loc(), plus a note.  A name that is
# not found in its file makes the audit fail, so the table cannot name a function that does not exist.
S2 = "fca-s2-adjustment.l4"
S3 = "fca-s3-application.l4"
CT = "fca-court.l4"
DF = "fca-definitions.l4"
WHERE = {
    "R08": ([(S2, "s 2(1) section 2 has effect in relation to the contract")], "fork F1 (subject to section 3)"),
    "R09": ([(S2, "s 2(2) a sum paid is recoverable from the party who received it"), (S2, "s 2(2) a sum payable ceases to be payable"),
             (S2, "s 2(2) subject to s 2(3) the amount of the sum paid that is recoverable"), (S2, "s 2(2) subject to s 2(3) the amount of the sum payable that remains payable")],
            "fork F2 (the time bound on the sums)"),
    "R10": ([(S2, "s 2(3) the court may allow the party to retain or recover the whole or part of the sums"), (S2, "s 2(3) the most the court may allow to be retained or recovered"),
             (S2, "s 2(3) the amount the court allows is within the limit"), (CT, "s 2(3) the court's permission to allow the party to retain or recover"),
             (S2, "s 2(3) the most the court may allow to be retained or recovered from the sums taken together"),
             (S2, "s 2(3) the amount the court allows from the sums taken together is within the limit")],
            "fork F2 (the time bound) and fork F6 (the sums taken together)"),
    "R11": ([(S2, "s 2(4) a sum is recoverable from the party who obtained a valuable benefit"), (S2, "s 2(4) the most that is recoverable for the valuable benefit"),
             (S2, "s 2(4) the sum the court considers just is within the limit")],
            "fork F3 (the time bound in a Where) and judgment call QE (the money-payment parenthesis)"),
    "R12": ([(S2, "s 2(4)(a) the amount of the benefited party's expenses that the court has regard to")], ""),
    "R13": ([(S2, "s 2(4) the court is to have regard to this matter")], ""),
    "R14": ([(S2, "s 2(5) the court may include a reasonable sum for overhead expenses and for work performed personally"), (S2, "s 2(5) the expenses as estimated"),
             (S2, "s 2(5) the amount of the expenses as estimated, counting none incurred as 0"), (CT, "s 2(5) the court's permission to include overhead expenses and personal work")], ""),
    "R15": ([(S2, "s 2(6) the court shall not take the insurance sums into account"), (S2, "s 2(6) the court may take the insurance sums into account"),
             (CT, "s 2(6) the court's prohibition on taking the insurance sums into account")],
            "fork F4 ('In considering' as a 'where') and judgment call QA (the 'unless')"),
    "R16": ([(S2, "s 2(7) the court may treat the benefit conferred on another person as a benefit obtained by the person who assumed the obligations"),
             (CT, "s 2(7) the court's permission to treat the benefit as obtained by the person who assumed the obligations")], ""),
    "R18": ([(S3, "s 3(1) this Act applies to a contract whether made before or after 13 February 1959"), (S3, "s 3(1) this Act applies to the contract by its time of discharge")], ""),
    "R19": ([(S3, "s 3(2) this Act applies in like manner to a contract to which the Government is a party")], ""),
    "R20": ([(S3, "s 3(3) the court is to give effect to the provision of the contract"), (S3, "s 3(3) the amount of section 2 that is given effect"),
             (CT, "s 3(3) the court's duty to give effect to the provision of the contract")], "judgment call QD (no compliance function)"),
    "R21": ([(S3, "s 3(4) the court is to treat the part of the contract as a separate contract that has not been frustrated"), (S3, "s 3(4) section 2 applies to this portion of the contract"),
             (CT, "s 3(4) the court's duty to treat the part of the contract as a separate contract")], "judgment call QD (no compliance function)"),
    "R22": ([(S3, "s 3 this Act applies to the contract")], "the composite of s 3(1) and s 3(5)(a) to (c)"),
    "R23": ([(S3, "s 3(5)(a) this Act shall not apply to the contract")], "judgment call QE (twice: the exception and the parenthesis)"),
    "R24": ([(S3, "s 3(5)(b) this Act shall not apply to the contract"), (S3, "s 3(5)(b) section 2(6) still applies although the contract is a contract of insurance")], "judgment call QA (the exception)"),
    "R25": ([(S3, "s 3(5)(c) this Act shall not apply to the contract")], "fork F5 (the 'where' of the second limb); s 7 of the Sale of Goods Act 1979 is an input"),
    "T01": ([(DF, "s 2(2) definition of the time of discharge"), (DF, "s 2(2) the time of discharge"), (DF, "s 2(2) there is a time of discharge")], ""),
    "T02": ([(DF, "s 2(4)(a) label for the benefited party")], ""),
}


def loc(fname, name):
    """file:line of the definition of `name` in fname (the line that holds the backticked name followed by MEANS)."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if line.startswith("`" + name + "` MEANS"):
                return f"{fname}:{n}"
    return None

MARKERS = {
    "R08": r"^\s*2\.—\(1\)",
    "R09": r"^\s*\(2\) Subject to subsection \(3\)",
    "R10": r"^\s*\(3\) If the party",
    "R11": r"^\s*\(4\) Where any party",
    "R12": r"^\s*\(a\) the amount of any expenses",
    "R13": r"^\s*\(b\) the effect",
    "R14": r"^\s*\(5\) In estimating",
    "R15": r"^\s*\(6\) In considering",
    "R16": r"^\s*\(7\) Where any person",
    "R18": r"^\s*3\.—\(1\)",
    "R19": r"^\s*\(2\) This Act shall apply to contracts to which",
    "R20": r"^\s*\(3\) Where any contract",
    "R21": r"^\s*\(4\) Where it appears",
    "R22": r"^\s*\(5\) This Act shall not apply",
    "R23": r"^\s*\(a\) to any charterparty",
    "R24": r"^\s*\(b\) to any contract of insurance",
    "R25": r"^\s*\(c\) to any contract to which section 7",
    "R06": r"^\s*1\. This Act is",
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    with open(args[0], encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    n = len(lines)
    nonblank = [i + 1 for i, l in enumerate(lines) if l.strip() != ""]
    problems = []
    covered = {}
    for rid, label, ranges, kind, disp, reason, where, overlay in ROWS:
        for a, b in ranges:
            if a < 1 or b > n or a > b:
                problems.append(f"{rid}: range {a}-{b} outside the raw file (1-{n})")
                continue
            if not overlay and all(lines[i - 1].strip() == "" for i in range(a, b + 1)):
                problems.append(f"{rid}: range {a}-{b} covers only blank lines")
            if not overlay:
                for i in range(a, b + 1):
                    covered.setdefault(i, []).append(rid)
        if rid in MARKERS and not overlay:
            a = ranges[0][0]
            if not re.search(MARKERS[rid], lines[a - 1]):
                problems.append(f"{rid}: line {a} {lines[a-1]!r} does not start with the expected marker {MARKERS[rid]!r}")
    for rid, (funcs, note) in WHERE.items():
        for fname, name in funcs:
            if loc(fname, name) is None:
                problems.append(f"{rid}: no function `{name}` in {fname}")
    for r in ROWS:
        if r[4] != "inert" and r[0] not in WHERE:
            problems.append(f"{r[0]}: operative row with no WHERE entry")
    uncovered = [i for i in nonblank if i not in covered]
    for i in uncovered:
        problems.append(f"line {i} not in any row: {lines[i-1]!r}")
    multi = {i: r for i, r in covered.items() if len(r) > 1 and lines[i - 1].strip() != ""}
    for i, r in multi.items():
        problems.append(f"line {i} is in more than one primary row: {r}")
    prim = [r for r in ROWS if not r[7]]
    over = [r for r in ROWS if r[7]]
    count = {}
    for r in ROWS:
        key = r[4] if r[4] != "inert" else f"inert (reason {r[5]})"
        count[key] = count.get(key, 0) + 1
    print(f"raw lines: {n}; non-blank lines: {len(nonblank)}; primary rows: {len(prim)}; overlay rows (terms): {len(over)}; total rows: {len(ROWS)}")
    print("dispositions (all rows):", ", ".join(f"{k}: {v}" for k, v in sorted(count.items())))
    print(f"non-blank lines covered by a primary row: {len(nonblank) - len(uncovered)} of {len(nonblank)}")
    print(f"problems: {len(problems)}")
    for p in problems:
        print("  ", p)
    if "--table" in flags:
        print()
        print("| row | provision | raw lines | kind | disposition | where / why |")
        print("| --- | --- | --- | --- | --- | --- |")
        for rid, label, ranges, kind, disp, reason, where, overlay in ROWS:
            rng = ", ".join(f"{a}" if a == b else f"{a}-{b}" for a, b in ranges)
            d = disp if disp != "inert" else f"inert (reason {reason})"
            if rid in WHERE:
                funcs, note = WHERE[rid]
                where = "; ".join(f"{loc(f, n)} `{n}`" for f, n in funcs) + (f" ({note})" if note else "")
            print(f"| {rid} | {label} | {rng} | {kind} | {d} | {where} |")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
