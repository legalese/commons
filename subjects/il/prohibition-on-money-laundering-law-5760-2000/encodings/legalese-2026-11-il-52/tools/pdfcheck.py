#!/usr/bin/env python3
# Written for row il-43 (2026-11-10); adapted for rows il-48 and il-52. Every PDF of this row has a text layer, so the Kovetz HaTakanot quotations (`ext:[KT ...]`) are checked too; a `cover` tag is page 1 of an issue.
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
    "SH 2876 cover": ("amending-laws/sh2876-5781-p136-extension-law-2020.pdf", 1),
    "SH 2876 p.136": ("amending-laws/sh2876-5781-p136-extension-law-2020.pdf", 2),
    "SH 3571 cover": ("sh3571-5786-instrument-of-27-7-2026.pdf", 1),
    "SH 3571 p.985": ("sh3571-5786-instrument-of-27-7-2026.pdf", 39),
    "KT 12422 cover": ("official/kt12422-5786-p2196a-order-of-8-6-2026.pdf", 1),
    "KT 12422 p.2196א": ("official/kt12422-5786-p2196a-order-of-8-6-2026.pdf", 2),
    "KT 7721 cover": ("official/kt7721-5777-pp37-44.pdf", 1),
    "KT 7721 p.38": ("official/kt7721-5777-pp37-44.pdf", 2),
}
# The file of Sefer HaChukim 3571 is NOT deposited (it holds the whole amendment of another Law). Its lines are checked only when SH3571_PDF names a copy of the file as downloaded
# (sha256 and size in registers/source-bundle/SOURCES.json); otherwise they are skipped, and the final line says how many.
NOT_DEPOSITED = {"SH 3571 cover", "SH 3571 p.985"}
LINE = re.compile(r"^\s*--\s*ext:\[((?:SH|KT) \d+ (?:p\.[0-9א]+|cover))[^\]]*\] \|\s*(.*)$")
CACHE = {}


def norm(s):
    s = re.sub("[‎‏‪-‮]", "", s)
    s = re.sub("[\"'״׳“”‘’]", "", s)
    return s


def page_text(tag):
    if tag not in CACHE:
        pdf, page = MAP[tag]
        path = os.environ.get("SH3571_PDF", "") if tag in NOT_DEPOSITED else os.path.join(SB, pdf)
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", path, "-"],
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
            if tag not in MAP:
                bad += 1
                print(f"{os.path.basename(path)}:{n}: unknown tag {tag}")
                continue
            if tag in NOT_DEPOSITED and not os.path.exists(os.environ.get("SH3571_PDF", "")):
                skipped += 1
                continue
            checked += 1
            hay = page_text(tag)
            for w in re.findall(r"[א-ת]{2,}", norm(text)):
                if w not in hay:
                    bad += 1
                    print(f"{os.path.basename(path)}:{n}: word not in the text layer of {tag}: {w}")
print(f"pdfcheck: {checked} quotation lines checked, {skipped} skipped (the file of Sefer HaChukim 3571 is not deposited; set SH3571_PDF to a copy of it as downloaded to check them), {bad} problems")
sys.exit(1 if bad else 0)
