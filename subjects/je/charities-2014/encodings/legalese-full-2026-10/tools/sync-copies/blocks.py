"""The list of copied blocks, used by sync-check.py (which diffs the copies against their sources).

Each block is (kind, name, subject, module, article, new_ref).
  kind     "noun" (a DECLARE) or "fn" (a function definition whose first line starts with the backticked name)
  subject  the subject directory, under SUBJECTS, and the encodings row
  module   the source module file
  new_ref  for a function, the plain-text @ref that replaces the source's @ref (which carries a locator); None for a noun
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))  # <Charities row>/tools/sync-copies
_ROWDIR = os.path.dirname(os.path.dirname(_HERE))  # <Charities row>
# The row sits at subjects/je/charities-2014/encodings/<row>, so the subjects are three directories above it.
SUBJECTS = os.environ.get("JE_SUBJECTS", os.path.dirname(os.path.dirname(os.path.dirname(_ROWDIR))))
CHAR = os.environ.get("JE_CHAR", _ROWDIR)
MINE = "g7-interpretation-laws.l4"

ROW = {
    "interpretation-1954": SUBJECTS + "/interpretation-1954/encodings/legalese-2026-10",
    "legislation-2021": SUBJECTS + "/legislation-2021/encodings/legalese-2026-10",
}

L54 = "Interpretation (Jersey) Law 1954"
L21 = "Legislation (Jersey) Law 2021"
V1 = "text of 1 January 2019 to 27 September 2021"
F54 = "(subject je/interpretation-1954, file source/l_17_1954_20210927.txt, "
F21 = "(subject je/legislation-2021, file source/l_8_2021.current.txt, "

# (heading, description, [blocks])
SECTIONS = [
    ("Copies from the Interpretation (Jersey) Law 1954: Article 1(5) and 1(6)", "The day on which an enactment expressed to come into operation on a particular day comes into operation, under the text of the Law in force from 1 January 2019 to 27 September 2021.", [
        ("noun", "Basis of a reading", "interpretation-1954", "je54-nouns.l4", "Article 1 (how sure an answer is)", None),
        ("noun", "How an enactment expresses the time of its commencement", "interpretation-1954", "je54-nouns.l4", "Articles 1(4) to 1(7)", None),
        ("noun", "Commencement as stated", "interpretation-1954", "je54-nouns.l4", "Articles 1(4) to 1(7)", None),
        ("noun", "Day with its basis", "interpretation-1954", "je54-nouns.l4", "Article 1 (answers that carry how sure they are)", None),
        ("fn", "Article 1(5): the enactment is expressed to come into operation on a particular day but names none", "interpretation-1954", "je54-art01-commencement.l4", "Article 1(5)",
         f"@ref {L54}, Article 1(5), {V1} {F54}line 9)"),
        ("fn", "Article 1(5) and 1(6): a time calculated from promulgation is not given a day by these Articles", "interpretation-1954", "je54-art01-commencement.l4", "Article 1(7)",
         f"@ref {L54}, Article 1(7), {V1} {F54}line 11)"),
        ("fn", "Article 1(5) and 1(6): the day under the text", "interpretation-1954", "je54-art01-commencement.l4", "Article 1(5) and 1(6)",
         f"@ref {L54}, Article 1(5) and 1(6), {V1} {F54}lines 9 and 10)"),
    ]),
    ("Copies from the Legislation (Jersey) Law 2021: Article 3", "The moment legislation expressed to come into force on a particular day does so (Article 3(2)), and whether Article 3 governs legislation that has already commenced (Article 3(6)).", [
        ("noun", "Time of day", "legislation-2021", "je21-nouns.l4", "Article 3", None),
        ("noun", "Reading L2 of a stated time of day", "legislation-2021", "je21-nouns.l4", "Article 3(2)", None),
        ("noun", "Reading L3 of the time at which the Law came into force", "legislation-2021", "je21-nouns.l4", "Article 3(6)", None),
        ("noun", "Moment of coming into force", "legislation-2021", "je21-nouns.l4", "Article 3", None),
        ("fn", "Article 3(2): the moment legislation expressed to come into force on a particular day does so", "legislation-2021", "je21-art03-commencement.l4", "Article 3(2)",
         f"@ref {L21}, Article 3(2) {F21}line 48)"),
        ("fn", "Article 3(6): Article 3 governs when the legislation commenced", "legislation-2021", "je21-art03-commencement.l4", "Article 3(6)",
         f"@ref {L21}, Article 3(6) and the endnotes' Table of Legislation History {F21}line 54 and lines 258 to 261)"),
    ]),
    ("Copies from the Legislation (Jersey) Law 2021: Articles 2, 9(5) and 9(6)", "What the power to make incidental, supplemental or consequential provision does for an instrument that amends other legislation (Article 9(5), limited by Article 9(6)).", [
        ("noun", "Form of legislation", "legislation-2021", "je21-nouns.l4", "Articles 1, 2, 7, 9 and 11", None),
        ("noun", "Reading L5 of legislation made by the States", "legislation-2021", "je21-nouns.l4", "Article 9(6)(b)", None),
        ("noun", "Reading L6 of the limits in Article 9(6)", "legislation-2021", "je21-nouns.l4", "Article 9(6)", None),
        ("noun", "Legislation to be amended", "legislation-2021", "je21-nouns.l4", "Article 9(5) and 9(6)", None),
        ("noun", "What the incidental power does", "legislation-2021", "je21-nouns.l4", "Article 9(5) and 9(6)", None),
        ("fn", "Article 2: the legislation was made by the States", "legislation-2021", "je21-art02-making.l4", "Article 2(1)(a) and 2(3)(a), as Article 9(6)(b) needs them",
         f"@ref {L21}, Article 2(1)(a) and 2(3)(a) {F21}lines 33 and 38)"),
        ("fn", "the limit in Article 9(6)(a) is met", "legislation-2021", "je21-art09-10-subordinate-powers.l4", "Article 9(6)(a)",
         f"@ref {L21}, Article 9(6)(a) {F21}line 99)"),
        ("fn", "the limit in Article 9(6)(b) is met", "legislation-2021", "je21-art09-10-subordinate-powers.l4", "Article 9(6)(b)",
         f"@ref {L21}, Article 9(6)(b) {F21}line 100)"),
        ("fn", "Article 9(5) and (6): what the incidental power does for the provision", "legislation-2021", "je21-art09-10-subordinate-powers.l4", "Article 9(5) and 9(6)",
         f"@ref {L21}, Article 9(5) and (6) {F21}lines 97 to 100)"),
    ]),
]


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def is_comment(line):
    return line.lstrip().startswith("--")


def paragraphs(lines):
    """The file as blank-line-separated paragraphs: a list of (first line number, [lines])."""
    out, cur, start = [], [], 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            if cur:
                out.append((start, cur))
                cur = []
        else:
            if not cur:
                start = i + 1
            cur.append(line)
    if cur:
        out.append((start, cur))
    return out


def find_block(lines, kind, name):
    """The one paragraph of the file that defines the noun or the function, as (first line number, [lines])."""
    hits = []
    for start, par in paragraphs(lines):
        for line in par:
            if kind == "noun":
                if line == f"DECLARE `{name}`" or line.startswith(f"DECLARE `{name}` "):
                    hits.append((start, par))
                    break
            else:
                if line.startswith(f"`{name}`") and " MEANS" in line:
                    hits.append((start, par))
                    break
    if len(hits) != 1:
        raise SystemExit(f"{kind} `{name}`: expected exactly one paragraph, found {len(hits)}")
    return hits[0]


def code_of(par):
    """The paragraph without its comment lines, with every @ref line reduced to the bare @ref (its text is the one thing a copy changes)."""
    out = []
    for line in par:
        if is_comment(line):
            continue
        if line.startswith("@ref"):
            out.append("@ref")
        else:
            out.append(line)
    return out
