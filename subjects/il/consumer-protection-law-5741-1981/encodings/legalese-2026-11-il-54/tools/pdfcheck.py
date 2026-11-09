#!/usr/bin/env python3
# Written for row il-43 (2026-11-10); adapted for row il-54. Every official page of this row is a Sefer HaChukim page with a text layer, so every `ext:[SH ...]` quotation is checked here.
# Row il-54, second change (2026-11-10): the whole Sefer HaChukim 3569 and 3572 PDFs are no longer deposited. SH 3572 is an extract of three pages (MAP below).
# SH 3569 has no PDF in the row: its quotations carry the tag form `SH 3569, p.907 image only`, which this script does not match, and were checked against the text layer of the whole file
# as downloaded (sha256 79212abfbf0871f2eae88eb19bca791cc3675dbfa09ad424392e1de91891e738) before it was removed: 19 quotation lines, 0 problems.
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
    "SH 2159 p.576": ("amending-laws/sh2159-5768-pp576-577-consumer-protection-amendment-24.pdf", 1),
    "SH 2159 p.577": ("amending-laws/sh2159-5768-pp576-577-consumer-protection-amendment-24.pdf", 2),
    "SH 2310 p.1022": ("amending-laws/sh2310-5771-pp1022-1023-consumer-protection-amendment-31.pdf", 1),
    "SH 2310 p.1023": ("amending-laws/sh2310-5771-pp1022-1023-consumer-protection-amendment-31.pdf", 2),
    "SH 3572 p.1029": ("amending-laws/sh3572-5786-pp1029-1035-1036-page-extract.pdf", 1),
    "SH 3572 p.1035": ("amending-laws/sh3572-5786-pp1029-1035-1036-page-extract.pdf", 2),
    "SH 3572 p.1036": ("amending-laws/sh3572-5786-pp1029-1035-1036-page-extract.pdf", 3),
}
LINE = re.compile(r"^\s*--\s*ext:\[(SH \d+ p\.\d+|order p\.\d+)[^\]]*\] \|\s*(.*)$")
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
