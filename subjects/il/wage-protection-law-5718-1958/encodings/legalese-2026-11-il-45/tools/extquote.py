#!/usr/bin/env python3
# Adapted for row il-45 from the extquote.py of row il-42. Two changes: the tags name this row's deposits, and a second kind of marker quotes the
# TEXT LAYER of a page of a deposited Sefer HaChukim PDF. The template reducer is copied unchanged from srcquote.py in this directory.
"""Expand quotations of the instruments OTHER than the Law, in place, from their deposits.

From a Hebrew Wikisource consolidation (an aid, UNOFFICIAL):
    `<indent>--@EXT tag 12`  or  `<indent>--@EXT tag 12-14`
    or an expanded line  `<indent>-- ext:[tag] 12 | ...`
  becomes one comment line per source line:  `<indent>-- ext:[tag] 12 | text`

From the text layer of a page of a Sefer HaChukim PDF (an official instrument):
    `<indent>--@PDF tag p17:15-16`
    or an expanded line  `<indent>-- ext:[tag] p17:15 | ...`
  becomes one comment line per line:  `<indent>-- ext:[tag] p17:15 | text`
  where 17 is the PDF page (not the printed page) and 15 is the line of `pdftotext -f 17 -l 17 FILE -` counted from 1, blank lines counted.
  The text layer of these PDFs is partly out of order (brackets, numerals and some lines of a table come out reversed or split); a line is quoted
  only where it reads in order, and the NOTES.md of the row says which quotations were read from the page image instead.
  Bidirectional control marks are removed and whitespace is collapsed; nothing else is changed.

(srcquote.py does the same for the Law itself, with `src:N |`; hebcheck.py skips all three kinds of line.)

Usage: extquote.py FILE.l4 [FILE.l4 ...]        expand in place
       extquote.py --check FILE.l4 [...]       exit 1 if any ext line differs from its source
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.normpath(os.path.join(HERE, "..", "..", "..", "registers", "source-bundle"))
WIKI = {
    "enforcement": "other-laws/enforcement-of-labour-laws-law-5772-2011.he.wiki.txt",
    "interp": "other-laws/interpretation-law-5741-1981.he.wiki.txt",
    "penal": "other-laws/penal-law-5737-1977.he.wiki.txt",
    "severance": "other-laws/severance-pay-law-5723-1963.he.wiki.txt",
    "cash": "other-laws/cash-reduction-law-5778-2018.he.wiki.txt",
    "postal": "other-laws/postal-law-5746-1986.he.wiki.txt",
    "ni1995": "other-laws/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt",
}
SRC = {}
PAGES = {}
INNER = re.compile(r"\{\{([^{}]*)\}\}")


def reduce_template(m):
    parts = m.group(1).split("|")
    name = parts[0]
    args = [p for p in parts[1:]]
    if name in ("ח:פנימי", "ח:חיצוני"):
        return args[-1] if args else ""
    if name == "ח:הערה":
        return "[note: " + "|".join(args) + "]"
    if name.startswith("ח:ת"):  # ח:ת ח:תת ח:תתת ח:תתתת
        labels = [a for a in args if not a.startswith("סוג=")]
        return "".join(labels)
    if name == "ח:סעיף":
        num = args[0] if args else ""
        head = args[1] if len(args) > 1 else ""
        amend = [a for a in args[2:] if a.startswith("תיקון")]
        tail = (" [" + amend[0] + "]") if amend else ""
        return (f"סעיף {num} – {head}".rstrip(" –")) + tail
    if name == "ח:סעיף*":
        return ""
    if name == "ח:קטע1":
        return args[-1] if args else ""
    return m.group(0).replace("{{", "⟦").replace("}}", "⟧")


def clean(line):
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


def wiki_lines(tag):
    if tag not in SRC:
        with open(os.path.join(SB, WIKI[tag]), encoding="utf-8") as fh:
            SRC[tag] = fh.read().split("\n")
    return SRC[tag]


def pdf_for(tag):
    hits = glob.glob(os.path.join(SB, "amending-laws", tag + "-*.pdf"))
    if len(hits) != 1:
        sys.exit(f"extquote: tag {tag} names {len(hits)} PDFs in amending-laws/")
    return hits[0]


def pdf_lines(tag, page):
    key = (tag, page)
    if key not in PAGES:
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), pdf_for(tag), "-"], capture_output=True, text=True, check=True).stdout
        out = re.sub(r"[‪-‮‎‏]", "", out)
        PAGES[key] = out.split("\n")
    return PAGES[key]


WMARK = re.compile(r"^(\s*)--(?:@EXT (\S+) |\s*ext:\[([^\]]+)\] )(\d+)(?:-(\d+))?(?:\s*\|.*)?$")
PMARK = re.compile(r"^(\s*)--(?:@PDF (\S+) p|\s*ext:\[([^\]]+)\] p)(\d+):(\d+)(?:-(\d+))?(?:\s*\|.*)?$")
check = sys.argv[1] == "--check"
files = sys.argv[2:] if check else sys.argv[1:]
bad = 0
for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln in lines:
        m = WMARK.match(ln)
        if m:
            indent, tag = m.group(1), m.group(2) or m.group(3)
            a, b = int(m.group(4)), int(m.group(5) or m.group(4))
            for n in range(a, b + 1):
                text = clean(wiki_lines(tag)[n - 1])
                if text:
                    out.append(f"{indent}-- ext:[{tag}] {n} | {text}")
            continue
        m = PMARK.match(ln)
        if m:
            indent, tag = m.group(1), m.group(2) or m.group(3)
            page, a, b = int(m.group(4)), int(m.group(5)), int(m.group(6) or m.group(5))
            L = pdf_lines(tag, page)
            for n in range(a, b + 1):
                text = re.sub(r"\s+", " ", L[n - 1]).strip()
                if text:
                    out.append(f"{indent}-- ext:[{tag}] p{page}:{n} | {text}")
            continue
        out.append(ln)
    if check:
        # a check run compares only previously expanded lines, one by one
        exp = [l for l in lines if re.match(r"^\s*-- ext:\[[^\]]+\] p?\d", l)]
        got = [l for l in out if re.match(r"^\s*-- ext:\[[^\]]+\] p?\d", l)]
        for e, g in zip(exp, got):
            if e != g:
                bad += 1
                print(f"{path}: ext line differs from source: {e[:80]}")
        if len(exp) != len(got):
            bad += 1
            print(f"{path}: ext line count differs")
    else:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
