#!/usr/bin/env python3
# Written for row il-43 (2026-11-10).
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
SB = os.path.normpath(os.path.join(HERE, "..", "..", "..", "registers", "source-bundle", "amending-laws"))
MAP = {
    "SH 2407 p.227": ("sh2407-5773-p227-extract.pdf", 1),
    "SH 2459 p.600": ("sh2459-5774-p600-p604-extract.pdf", 1),
    "SH 2459 p.604": ("sh2459-5774-p600-p604-extract.pdf", 2),
    "SH 2504 p.2": ("sh2504-5776-p2-extract.pdf", 1),
    "SH 2713 p.524": ("sh2713-5778-p510-p524-p527-extract.pdf", 2),
    "SH 2713 p.527": ("sh2713-5778-p510-p524-p527-extract.pdf", 3),
}
LINE = re.compile(r"^\s*--\s*ext:\[(SH \d+ p\.\d+)[^\]]*\] \|\s*(.*)$")
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
