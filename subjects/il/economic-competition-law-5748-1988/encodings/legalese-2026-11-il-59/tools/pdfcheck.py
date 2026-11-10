#!/usr/bin/env python3
# Written for row il-59 (2026-11-10), from the il-52 pdfcheck.py. No PDF is deposited in this row (every official page is a cropped image), so the check runs only when the whole files are at hand:
# set SH2781_PDF, KT11002_PDF, KT10454_PDF and KT12149_PDF to copies of the files as downloaded (sha256 and size in registers/source-bundle/SOURCES.json). Without them every line is skipped and the last line says so.
# Kovetz HaTakanot 5164 is a scan with no text layer, and the footer lines (tagged `footer`) of the other files have a reversed, garbled text layer; neither can be checked this way, and both were typed from the cropped image.
"""Check the Hebrew of every official-instrument quotation in a .l4 file against the text layer of the page it names.

A quotation line has the form
    -- ext:[SH 2781 p.246, read from the cropped image] | <Hebrew typed from the cropped image>
The tag (`SH <issue> p.<page>`) is looked up in MAP below, which names the environment variable holding the whole file and the page of the PDF.
The check is deliberately weak: it extracts the page's text layer with pdftotext, removes bidirectional marks, quotation marks and whitespace, and requires every Hebrew word of two or more letters
of the quotation to occur somewhere in that text. It catches a typing slip; it does not prove that the words stand in the order typed. The cropped image is what the typed text was read from.

Usage: pdfcheck.py FILE.l4 [FILE.l4 ...]      exit 1 if any word is missing or a tag is unknown.
"""
import os
import re
import subprocess
import sys

MAP = {
    "SH 2781 p.246": ("SH2781_PDF", 2),
    "SH 2781 p.247": ("SH2781_PDF", 3),
    "KT 11002 p.948": ("KT11002_PDF", 4),
    "KT 10454 p.598": ("KT10454_PDF", 2),
    "KT 12149 p.482": ("KT12149_PDF", 6),
}
NO_TEXT_LAYER = {"KT 5164 p.473"}
LINE = re.compile(r"^\s*--\s*ext:\[((?:SH|KT) \d+ p\.\d+)( footer)?[^\]]*\] \|\s*(.*)$")
CACHE = {}


def norm(s):
    s = re.sub("[‎‏‪-‮]", "", s)
    return re.sub("[\"'״׳“”‘’]", "", s)


def page_text(tag):
    if tag not in CACHE:
        var, page = MAP[tag]
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", os.environ[var], "-"],
                             capture_output=True, text=True).stdout
        CACHE[tag] = re.sub(r"\s+", "", norm(out))
    return CACHE[tag]


bad = checked = skipped = notext = 0
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            m = LINE.match(line)
            if not m:
                continue
            tag, footer, text = m.group(1), m.group(2), m.group(3)
            if tag in NO_TEXT_LAYER or footer:
                notext += 1
                continue
            if tag not in MAP:
                bad += 1
                print(f"{os.path.basename(path)}:{n}: unknown tag {tag}")
                continue
            if not os.path.exists(os.environ.get(MAP[tag][0], "")):
                skipped += 1
                continue
            checked += 1
            hay = page_text(tag)
            for w in re.findall(r"[א-ת]{2,}", norm(text)):
                if w not in hay:
                    bad += 1
                    print(f"{os.path.basename(path)}:{n}: word not in the text layer of {tag}: {w}")
print(f"pdfcheck: {checked} quotation lines checked, {skipped} skipped (set SH2781_PDF, KT11002_PDF, KT10454_PDF, KT12149_PDF to the files as downloaded), {notext} not checkable (Kovetz HaTakanot 5164 has no text layer; footer lines have a garbled one), {bad} problems")
sys.exit(1 if bad else 0)
