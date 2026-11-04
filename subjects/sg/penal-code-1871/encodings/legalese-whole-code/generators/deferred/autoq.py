#!/usr/bin/env python3
"""Rewrite `-- @sec LABEL` lines of a hand-written module into `-- @quote N M` lines (for expand.py).

Usage (from the encoding folder):
    python3 -I generators/deferred/autoq.py IN.l4 OUT.l4 [RAW]

`-- @sec 2` quotes the whole of section 2: from its heading (the unindented lines just above the numbered line)
to the line before the next section's heading.  The numbered line is found as `^ *LABEL\\.` (a bare label such as
"2", "6A", "22A") outside the table of contents.  Section ranges are computed from the text, not typed in.
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
raw_path = sys.argv[3] if len(sys.argv) > 3 else "../../registers/source-bundle/PC1871.txt"
raw = open(raw_path, encoding="utf-8").read().split("\n")
BODY = 1222  # the body starts after the contents; section lines are searched for from here
FOOT = re.compile(r"Singapore Statutes Online|PDF created date on")
AMEND = re.compile(r"^\s*\[(Act \d+ of \d{4}[^\]]*|S \d+/\d{4}[^\]]*|\d+/\d{4}(;[^\]]*)?)\]\s*$")

# every numbered section line in the body, in order: (line number, label)
starts = []
for i in range(BODY, len(raw)):
    m = re.match(r"^\x0c? {0,6}(\d+[A-Z]{0,2})\.(?:—\(1\)|[ —.]|$)", raw[i])
    if m and i < 12650:
        starts.append((i + 1, m.group(1)))


def heading_start(n):
    """First line of the heading block directly above numbered line n (1-based)."""
    k = n - 1  # index of line n-1 (0-based = n-2)
    j = n - 2
    # skip blank lines, then take consecutive unindented non-blank lines
    while j >= 0 and (not raw[j].strip() or FOOT.search(raw[j])):
        j -= 1
    top = j + 1
    while j >= 0 and raw[j].strip() and not raw[j].startswith(" ") and not FOOT.search(raw[j]):
        top = j + 1
        j -= 1
    return top


def section_range(label):
    for idx, (n, lab) in enumerate(starts):
        if lab == label:
            hs = heading_start(n)
            if idx + 1 < len(starts):
                nxt = starts[idx + 1][0]
                end = heading_start(nxt) - 1
            else:
                end = n + 5
            # drop trailing blanks, footers, amendment notes, and "[There are no sections ...]" notes
            while end > hs and (not raw[end - 1].strip() or FOOT.search(raw[end - 1]) or AMEND.match(raw[end - 1]) or raw[end - 1].strip().startswith("[There ")):
                end -= 1
            return hs, end
    sys.exit("section %r not found" % label)


out = []
for ln in open(src, encoding="utf-8").read().split("\n"):
    m = re.match(r"^-- @sec (\S+)\s*$", ln)
    if m:
        a, b = section_range(m.group(1))
        out.append("-- @quote %d %d" % (a, b))
    else:
        out.append(ln)
open(dst, "w", encoding="utf-8").write("\n".join(out))
