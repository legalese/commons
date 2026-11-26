#!/usr/bin/env python3
# notes/expand-quotes.py -- P2's helper: expands quote markers in a .l4 file, in place, into the `-- src:N | ...` lines
# and the `@ref` line that srcrefs.py checks.  Markers (a line that is only the marker):
#   @@R N[-M] | label                  quote raw lines N..M whole (blank raw lines left out), then `@ref label (src:N-M)`
#   @@S N :: start words :: end words | label     quote the slice of raw line N from `start words` to `end words`, then `@ref label (src:N)`
#   @@Q N[-M]                          quote lines only (no @ref), for a block that gets one @ref from an @@A line
#   @@QS N :: start :: end             quote a slice only
#   @@A N[-M] | label                  the @ref line only, with the locator written out
# Usage: python3 -I notes/expand-quotes.py FILE...     (RAW is the consolidated text, given by the constant below)
import os
import re, sys, unicodedata
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "registers", "source-bundle", "eu-gdpr-2016-679-consolidated-20160504.txt")
raw = open(RAW, encoding="utf-8").read().split("\n")
def sq(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
def quote_lines(n, m):
    out = []
    for i in range(n, m + 1):
        t = sq(raw[i - 1])
        if t:
            out.append("-- src:%d | %s" % (i, t))
    return out
def slice_line(n, a, b):
    t = sq(raw[n - 1])
    i = t.find(a)
    assert i >= 0, ("start not found", n, a)
    j = t.find(b, i)
    assert j >= 0, ("end not found", n, b)
    return "-- src:%d | %s" % (n, t[i:j + len(b)])
def rng(s):
    m = re.match(r"^(\d+)(?:-(\d+))?$", s.strip())
    n = int(m.group(1)); k = int(m.group(2)) if m.group(2) else n
    return n, k
for f in sys.argv[1:]:
    src = open(f, encoding="utf-8").read().split("\n")
    out = []
    for line in src:
        s = line.rstrip()
        m = re.match(r"^@@R\s+(\S+)\s*\|\s*(.*)$", s)
        if m:
            n, k = rng(m.group(1)); out += quote_lines(n, k); out.append("@ref %s (src:%d%s)" % (m.group(2), n, "-%d" % k if k != n else "")); continue
        m = re.match(r"^@@S\s+(\d+)\s*::\s*(.*?)\s*::\s*(.*?)\s*\|\s*(.*)$", s)
        if m:
            n = int(m.group(1)); out.append(slice_line(n, m.group(2), m.group(3))); out.append("@ref %s (src:%d)" % (m.group(4), n)); continue
        m = re.match(r"^@@QS\s+(\d+)\s*::\s*(.*?)\s*::\s*(.*?)\s*$", s)
        if m:
            out.append(slice_line(int(m.group(1)), m.group(2), m.group(3))); continue
        m = re.match(r"^@@Q\s+(\S+)\s*$", s)
        if m:
            n, k = rng(m.group(1)); out += quote_lines(n, k); continue
        m = re.match(r"^@@A\s+(\S+)\s*\|\s*(.*)$", s)
        if m:
            n, k = rng(m.group(1)); out.append("@ref %s (src:%d%s)" % (m.group(2), n, "-%d" % k if k != n else "")); continue
        out.append(line)
    open(f, "w", encoding="utf-8").write("\n".join(out))
