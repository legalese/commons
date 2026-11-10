#!/usr/bin/env python3
# Adapted for row il-57 (2026-11-10) from the il-52 copy. NO PDF is deposited by this row: only cropped page images, because each page carries text outside the three items the row records.
# The words of every `ext:[SH <issue> p.<page>, ...]` quotation are checked against the text layer of the page they were read from, in the FILE AS DOWNLOADED, whose path is given by an environment variable
# (SH3482_PDF, SH3513_PDF, SH3525_PDF; url, sha256 and size of each file are in registers/source-bundle/SOURCES.json). Without the variable the lines for that issue are skipped, and the final line says how many.
"""Check the Hebrew of every official-instrument quotation in a .l4 file against the text layer of the page it names.

A quotation line has the form
    -- ext:[SH 3525 p.563, read from the page image] | <Hebrew typed from the page image>
The check is deliberately weak: it extracts the page's text layer with pdftotext, removes bidirectional marks, quotation marks, geresh and whitespace,
and requires every Hebrew word of the quotation to occur somewhere in that text. It catches a typing slip; it does not prove that the words stand in the order typed,
because the text layers of these PDFs reverse and interleave runs (the text layer of Sefer HaChukim 3513 p. 461 holds each line twice). The page image is what the typed text was read from.

Usage: pdfcheck.py FILE.l4 [FILE.l4 ...]      exit 1 if any word is missing or a tag is unknown.
"""
import os
import re
import subprocess
import sys

# tag -> (environment variable naming the file as downloaded, page of that file)
MAP = {
    "SH 3482 p.214": ("SH3482_PDF", 2),
    "SH 3513 p.461": ("SH3513_PDF", 5),
    "SH 3525 p.562": ("SH3525_PDF", 20),
    "SH 3525 p.563": ("SH3525_PDF", 21),
}
LINE = re.compile(r"^\s*--\s*ext:\[((?:SH|KT) \d+ (?:p\.[0-9א]+|cover))[^\]]*\] \|\s*(.*)$")
CACHE = {}


def norm(s):
    s = re.sub("[‎‏‪-‮]", "", s)
    s = re.sub("[\"'״׳“”‘’]", "", s)
    return s


def page_text(tag):
    if tag not in CACHE:
        var, page = MAP[tag]
        path = os.environ.get(var, "")
        out = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-layout", path, "-"],
                             capture_output=True, text=True).stdout
        CACHE[tag] = re.sub(r"\s+", "", norm(out))
    return CACHE[tag]


bad = checked = skipped = 0
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
            if not os.path.exists(os.environ.get(MAP[tag][0], "")):
                skipped += 1
                continue
            checked += 1
            hay = page_text(tag)
            for w in re.findall(r"[א-ת]{2,}", norm(text)):
                if w not in hay:
                    bad += 1
                    print(f"{os.path.basename(path)}:{n}: word not in the text layer of {tag}: {w}")
print(f"pdfcheck: {checked} quotation lines checked, {skipped} skipped (set SH3482_PDF, SH3513_PDF and SH3525_PDF to the files as downloaded to check them), {bad} problems")
sys.exit(1 if bad else 0)
