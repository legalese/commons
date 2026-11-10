#!/usr/bin/env python3
"""Bind the Latin strings of the modules to the Hebrew they were written from. Written for row il-70.

The modules type every number and quoted word in Latin letters, so that no Hebrew sits outside a quotation line (tools/hebcheck.py).
The Hebrew is on the `ext:` and `src:` lines; the Latin form of the words the row types is on a `tr:` line right after them.
The rule that turns Hebrew into Latin is the one in this file, and nothing else:

  - the prefix vav + maqaf is written `and-`;
  - the word `עד` between two numbers is written ` to `;
  - a Hebrew letter alef, bet, gimel or dalet right after a digit is written A, B, C or D;
  - a letter alef, bet, gimel or dalet alone in brackets is written (a), (b), (c) or (d).
Everything else stays as it is (Hebrew words, digits, commas, spaces, quotation marks).

A line `-- tr:[TAG] | LATIN` is checked in two ways.
  1. LATIN must occur in the transliteration of a line `-- ext:[TAG] | HEBREW` (or, when TAG is `src:N`, of a line `-- src:N | HEBREW`) of any file given.
     If LATIN is written between quotation marks, the marks must be there too: `-- tr:[TAG] | "1A,"` requires `"1A,"` in the transliteration.
  2. LATIN (without those marks) must occur as a string literal "LATIN" on a non-comment line of one of the files given.

Usage: translit.py FILE.l4 [FILE.l4 ...]        exit 1 if any tr line fails either check, and when no tr line is found at all
"""
import re
import sys

LET = {"א": "A", "ב": "B", "ג": "C", "ד": "D"}
LOW = {"א": "a", "ב": "b", "ג": "c", "ד": "d"}


def translit(h):
    h = h.replace("ו־", "and-")
    h = re.sub(r"(?<=\d) עד (?=\d)", " to ", h)
    h = re.sub(r"(?<=\d)([אבגד])(?![א-ת])", lambda m: LET[m.group(1)], h)
    h = re.sub(r"\(([אבגד])\)", lambda m: "(" + LOW[m.group(1)] + ")", h)
    return re.sub(r"\s+", " ", h).strip()


EXT = re.compile(r"^\s*--\s*ext:\[([^\]]+)\] \| (.*)$")
SRC = re.compile(r"^\s*--\s*src:(\d+) \| (.*)$")
TR = re.compile(r"^\s*--\s*tr:\[([^\]]+)\] \| (.*)$")

files = sys.argv[1:]
source = {}  # tag -> list of transliterated Hebrew lines
code = []
trs = []
for path in files:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh.read().split("\n"), 1):
            line = line.rstrip()
            m = EXT.match(line)
            if m:
                source.setdefault(m.group(1), []).append(translit(m.group(2)))
                continue
            m = SRC.match(line)
            if m:
                source.setdefault("src:" + m.group(1), []).append(translit(m.group(2)))
                continue
            m = TR.match(line)
            if m:
                trs.append((path.split("/")[-1], n, m.group(1), m.group(2).strip()))
                continue
            if not line.lstrip().startswith("--"):
                code.append(line)
codetext = "\n".join(code)

bad = 0
for name, n, tag, latin in trs:
    quoted = len(latin) >= 2 and latin[0] == '"' and latin[-1] == '"'
    bare = latin[1:-1] if quoted else latin
    needle = re.sub(r"\s+", " ", latin)
    if not any(needle in s for s in source.get(tag, [])):
        bad += 1
        print(f"{name}:{n}: tr:[{tag}] `{latin}` is not in the transliteration of its source line(s)")
    if '"' + bare + '"' not in codetext:
        bad += 1
        print(f"{name}:{n}: tr:[{tag}] `{bare}` does not occur as a string literal in the code")
if not trs:
    print("translit.py: no tr: line found")
    bad = 1
print(f"translit.py: {len(trs)} tr lines checked, {bad} problem(s)")
sys.exit(1 if bad else 0)
