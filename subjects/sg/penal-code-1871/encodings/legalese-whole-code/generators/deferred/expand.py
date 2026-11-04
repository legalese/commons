#!/usr/bin/env python3
"""Expand the placeholders in a hand-written module of completion pass 2026-11-04, in place.

Usage (from the encoding folder):
    python3 -I generators/deferred/expand.py FILE.l4 [RAW]

The module is written by hand, with three kinds of placeholder line, each on a line of its own
and starting in column 1:

    -- @quote N M       becomes `-- src:N | text` lines copied from line N..M of RAW (the Code's text),
                        leaving out blank lines, page footers ("Singapore Statutes Online ...") and
                        lines that are only an amendment note ("[15/2019]", "[Act 23 of 2021 wef ...]");
                        the quoted lines are the raw lines, whitespace squeezed, so that
                        `srcrefs.py check` can verify them
    @ref ... (src:@@)   the `@@` becomes `lo-hi`, the first and last raw line of the quote run just above
    -- @punish ID       becomes the `@ref` and the `Punishment` record for ID in generators/deferred/punish.py

After expansion no placeholder is left, and the .l4 file is the source of truth: a hand edit is not lost
by a later run (there is nothing left to run).  RAW defaults to ../../registers/source-bundle/PC1871.txt.
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from punish import PUNISH, render  # noqa: E402

path = sys.argv[1]
raw_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "..", "..", "registers", "source-bundle", "PC1871.txt")
raw = open(raw_path, encoding="utf-8").read().split("\n")

FOOTER = re.compile(r"Singapore Statutes Online|PDF created date on")
AMEND = re.compile(r"^\s*\[(Act \d+ of \d{4}[^\]]*|S \d+/\d{4}[^\]]*|\d+/\d{4}(;[^\]]*)?)\]\s*$")


def squeeze(s):
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", s)).strip()


def quote(n, m):
    out, lo, hi = [], None, None
    for k in range(n, m + 1):
        t = raw[k - 1]
        if not re.search(r"\w", t) or FOOTER.search(t) or AMEND.match(t):
            continue  # blank, a bare dash, a page footer, an amendment note
        out.append("-- src:%d | %s" % (k, squeeze(t)))
        lo = k if lo is None else lo
        hi = k
    return out, lo, hi


lines = open(path, encoding="utf-8").read().split("\n")
res = []
run = None
for ln in lines:
    m = re.match(r"^-- @quote (\d+) (\d+)\s*$", ln)
    if m:
        q, lo, hi = quote(int(m.group(1)), int(m.group(2)))
        res.extend(q)
        run = (lo, hi)
        continue
    m = re.match(r"^-- @punish (\S.*?)\s*$", ln)
    if m:
        pid = m.group(1)
        spec = PUNISH[pid]
        a, b = spec["lines"]
        text = squeeze(" ".join(l for l in raw[a - 1:b] if not FOOTER.search(l)))
        text = squeeze(re.sub(r"\((?:[a-z]{1,3}|\d+)\)\s", "", text))  # the enumerators (a) (ii) (1) are not words
        assert squeeze(spec["words"]) in text, "words of %s are not in raw lines %d-%d" % (pid, a, b)
        res.extend(render(pid, spec))
        continue
    if "(src:@@)" in ln:
        assert run, "no quote run above: " + ln
        ln = ln.replace("(src:@@)", "(src:%d-%d)" % run)
    res.append(ln)

open(path, "w", encoding="utf-8").write("\n".join(res))
print("expanded", path)
