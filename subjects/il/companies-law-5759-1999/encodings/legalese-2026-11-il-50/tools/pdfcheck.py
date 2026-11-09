#!/usr/bin/env python3
# Written for row il-43 (2026-11-10); adapted for rows il-48 and il-50. Two deposited PDFs have a text layer: the Sefer HaChukim 2708 page extract and the Kovetz HaTakanot 7639 page extract. The Kovetz HaTakanot PDFs of issues 6074 and 6178 are image-only scans, so their quotations (`ext:[KT 6074 ...]`, `ext:[KT 6178 ...]`) are not checked here.
# For `KT 7639` lines the numerals are checked too: every run of digits of the quotation must occur somewhere in the page's text layer (a weak check, since a short numeral occurs anywhere); the text layer's order of words is garbled, so no order is checked.
"""Check the Hebrew of every official-instrument quotation in a .l4 file against the text layer of the page it names.

A quotation line has the form
    -- ext:[SH 2708 p.394, read from the page image] | <Hebrew typed from the page image>
The tag (`SH <issue> p.<page>`) is looked up in MAP below, which names the deposited PDF and the page of the PDF (printed page = PDF page + 296).
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
SH2708 = "amending-laws/sh2708-5778-pp393-394-page-extract.pdf"
KT7639 = "official/kt7639-5776-pp946-949-page-extract.pdf"
MAP = {
    "SH 2708 p.393": (SH2708, 1),
    "SH 2708 p.394": (SH2708, 2),
    "KT 7639 p.946": (KT7639, 1),
    "KT 7639 p.947": (KT7639, 2),
    "KT 7639 p.948": (KT7639, 3),
    "KT 7639 p.949": (KT7639, 4),
}
LINE = re.compile(r"^\s*--\s*ext:\[((?:SH \d+|KT 7639) p\.\d+)[^\]]*\] \|\s*(.*)$")
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
            if tag.startswith("KT 7639"):
                for d in re.findall(r"\d+", text):
                    if d not in hay:
                        bad += 1
                        print(f"{os.path.basename(path)}:{n}: numeral not in the text layer of {tag}: {d}")
print(f"pdfcheck: {checked} quotation lines checked, {bad} problems")
sys.exit(1 if bad else 0)
