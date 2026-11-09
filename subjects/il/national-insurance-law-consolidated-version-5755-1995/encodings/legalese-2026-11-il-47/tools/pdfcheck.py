#!/usr/bin/env python3
# Written for row il-43 (2026-11-10); the map and the tag pattern changed for row il-47 (Sefer HaChukim and Kovetz HaTakanot pages).
"""Check the Hebrew of every official-instrument quotation in a .l4 file against the text layer of the page it names.

A quotation line has the form
    -- ext:[SH 2511 p.248, read from the page image] | <Hebrew typed from the page image>
The tag (`SH <issue> p.<page>` or `KT <issue> p.<page>`) is looked up in MAP below, which names the deposited PDF (relative to registers/source-bundle) and the page of the PDF; a PDF with no text layer maps to None and its lines are counted but cannot be checked.
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
    "SH 1522 p.299": ("amending-laws/13_lsr_203774.pdf", 90),
    "SH 1522 p.301": ("amending-laws/13_lsr_203774.pdf", 92),
    # Sefer HaChukim 2511: no PDF page is deposited, only strips of the page images (official/img/sh2511-p24*-strip.png), so these are not machine-checked.
    "SH 2511 p.247": None,
    "SH 2511 p.248": None,
    "SH 2511 p.249": None,
    # The other official PDFs are page extracts: the page numbers below are PDF pages OF THE EXTRACT, not of the whole issue.
    "SH 2774 p.152": ("official/sh2774-5779-p152-153-nii-amendment-210.pdf", 1),
    "SH 2774 p.153": ("official/sh2774-5779-p152-153-nii-amendment-210.pdf", 2),
    "KT 7669 p.1328": ("official/kt7669-5776-p1328-1329-regulations-9-june-2016.pdf", 1),
    "KT 7669 p.1329": ("official/kt7669-5776-p1328-1329-regulations-9-june-2016.pdf", 2),
    "KT 6573 p.648": ("official/kt6573-5767-p648-regulations-14-march-2007.pdf", 1),
    "KT 3608 p.223": None,  # image only (the extract kt3608-5737-p223-regulations-28-oct-1976.pdf has no text layer)
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
            if MAP[tag] is None:
                skipped += 1
                continue
            checked += 1
            hay = page_text(tag)
            for w in re.findall(r"[א-ת]{2,}", norm(text)):
                if w not in hay:
                    bad += 1
                    print(f"{os.path.basename(path)}:{n}: word not in the text layer of {tag}: {w}")
print(f"pdfcheck: {checked} quotation lines checked, {skipped} on a PDF with no text layer (not checkable), {bad} problems")
sys.exit(1 if bad else 0)
