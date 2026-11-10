#!/usr/bin/env python3
# Written for row il-43 (2026-11-10); adapted for row il-51. Only the Sefer HaChukim PDF (issue 3287) is checked here. Quotations from Kovetz HaTakanot (`ext:[KT ...]`) and Yalkut HaPirsumim (`ext:[YP ...]`) are NOT checked: those pages are typed from a page image, and no text layer is checked.
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
    "SH 3287 p.1430": ("amending-laws/sh3287-5784-p1430-1433-1461-1472-1495-privacy-protection-law-amendment-13-extract.pdf", 1),
    "SH 3287 p.1433": ("amending-laws/sh3287-5784-p1430-1433-1461-1472-1495-privacy-protection-law-amendment-13-extract.pdf", 2),
    "SH 3287 p.1461": ("amending-laws/sh3287-5784-p1430-1433-1461-1472-1495-privacy-protection-law-amendment-13-extract.pdf", 3),
    "SH 3287 p.1472": ("amending-laws/sh3287-5784-p1430-1433-1461-1472-1495-privacy-protection-law-amendment-13-extract.pdf", 4),
    "SH 3287 p.1495": ("amending-laws/sh3287-5784-p1430-1433-1461-1472-1495-privacy-protection-law-amendment-13-extract.pdf", 5),
}
# Pages deposited only as cropped images (the rest of each page is not deposited): their lines are not checked here.
IMAGE_ONLY = {"SH 3287 p.1438", "SH 3287 p.1474"}
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
skipped = 0
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            m = LINE.match(line)
            if not m:
                continue
            tag, text = m.group(1), m.group(2)
            if tag in IMAGE_ONLY:
                skipped += 1
                continue
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
print(f"pdfcheck: {checked} quotation lines checked, {skipped} lines of image-only pages not checked, {bad} problems")
sys.exit(1 if bad else 0)
