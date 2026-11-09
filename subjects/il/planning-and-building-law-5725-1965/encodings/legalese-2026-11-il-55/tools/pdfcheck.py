#!/usr/bin/env python3
# Row il-55 (2026-11-10): the instruments are Sefer HaChukim pages (tag SH) and Kovetz HaTakanot pages (tag KT).
# Written for row il-43 (2026-11-10); adapted for row il-48, and again for row il-49 (2026-11-10): every instrument of this row is a Sefer HaChukim page with a text layer.
"""Check the Hebrew of every official-instrument quotation in a .l4 file against the text layer of the page it names.

A quotation line has the form
    -- ext:[SH 2713 p.524, read from the page image] | <Hebrew typed from the page image>
The tag (`SH <issue> p.<page>`) is looked up in MAP below, which names the deposited PDF and the page of the PDF.
The check is deliberately weak: it extracts the page's text layer with pdftotext, removes bidirectional marks, quotation marks,
geresh and whitespace, and requires every Hebrew word of the quotation to occur somewhere in that text.
It catches a typing slip; it does not prove that the words stand in the order typed, because the text layers of these PDFs
reverse and interleave runs. The page image is what the typed text was read from.

Usage: pdfcheck.py FILE.l4 [FILE.l4 ...]      exit 1 if any word is missing or a tag is unknown.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.normpath(os.path.join(HERE, "..", "..", "..", "registers", "source-bundle"))
MAP = {
    "SH 2450 p.510": ("amending-laws/sh2450-5774-p510-page-extract.pdf", 1),
    "SH 2635 p.920": ("amending-laws/sh2635-5777-pp920-923-page-extract.pdf", 1),
    "SH 2635 p.923": ("amending-laws/sh2635-5777-pp920-923-page-extract.pdf", 2),
    "SH 2165 p.634": ("amending-laws/sh2165-5768-p634-page-extract.pdf", 1),
    "KT 7682 p.1512": ("official/kt7682-5776-pp1512-1535-page-extract.pdf", 1),
    "KT 7682 p.1535": ("official/kt7682-5776-pp1512-1535-page-extract.pdf", 2),
    "KT 6729 p.194": ("official/kt6729-5769-p194-page-extract.pdf", 1),
    "KT 6922 p.1556": ("official/kt6922-5770-p1556-page-extract.pdf", 1),
}
LINE = re.compile(r"^\s*--\s*ext:\[((?:SH|KT) \d+ p\.\d+)[^\]]*\] \|\s*(.*)$")
CACHE = {}


def norm(s):
    s = re.sub("[‎‏‪-‮]", "", s)
    s = re.sub("[\"'״׳“”‘’]", "", s)
    return s


def page_text(tag):
    if tag not in CACHE:
        pdf, page = MAP[tag]
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", os.path.join(SB, pdf), "-"],
                             capture_output=True, text=True).stdout
        CACHE[tag] = re.sub(r"\s+", "", norm(out))
    return CACHE[tag]


bad = 0
checked = 0
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            m = LINE.match(line)
            if not m:
                continue
            tag, text = m.group(1), m.group(2)
            if tag not in MAP:
                bad += 1
                print(f"{os.path.basename(path)}:{n}: unknown tag {tag}")
                continue
            checked += 1
            hay = page_text(tag)
            for w in re.findall(r"[א-ת]{2,}", norm(text)):
                if w not in hay:
                    bad += 1
                    print(f"{os.path.basename(path)}:{n}: word not in the text layer of {tag}: {w}")
print(f"pdfcheck: {checked} quotation lines checked, {bad} problems")
sys.exit(1 if bad else 0)
