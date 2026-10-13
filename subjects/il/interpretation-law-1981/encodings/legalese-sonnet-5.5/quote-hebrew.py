#!/usr/bin/env python3
"""Print quote lines for wikitext lines, with wiki templates reduced to their display text.

usage: python3 -I quote-hebrew.py law|ordinance N [M]   (reads ../../source/law.wiki or ordinance.wiki)
Each line is split at inner templates (external/internal links, notes) so that every printed
segment is a contiguous, verbatim slice of the raw line (srcrefs R1 compares normalised text).
"""
import re, sys, unicodedata

import os
INPUTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "source") + os.sep

def tokenize(s):
    """Split into [('text', str) | ('tpl', [args...])] at top level, nesting preserved in args as raw strings."""
    out, i, buf = [], 0, []
    while i < len(s):
        if s.startswith("{{", i):
            if buf:
                out.append(("text", "".join(buf))); buf = []
            depth, j = 1, i + 2
            while j < len(s) and depth:
                if s.startswith("{{", j): depth += 1; j += 2
                elif s.startswith("}}", j): depth -= 1; j += 2
                else: j += 1
            inner = s[i+2:j-2]
            # split args at top-level |
            args, d, cur = [], 0, []
            k = 0
            while k < len(inner):
                if inner.startswith("{{", k): d += 1; cur.append("{{"); k += 2
                elif inner.startswith("}}", k): d -= 1; cur.append("}}"); k += 2
                elif inner[k] == "|" and d == 0: args.append("".join(cur)); cur = []; k += 1
                else: cur.append(inner[k]); k += 1
            args.append("".join(cur))
            out.append(("tpl", args))
            i = j
        else:
            buf.append(s[i]); i += 1
    if buf: out.append(("text", "".join(buf)))
    return out

def segments(line):
    """Break a wikitext line into quote segments.

    A segment is text that is contiguous in the raw line once punctuation is ignored:
    the display text of a template together with the plain text that follows it directly,
    or the plain text at the start of the line. A new segment starts at every template."""
    out = []
    buf = []
    def flush():
        t = re.sub(r"\s+", " ", "".join(buf)).strip()
        if t: out.append(t)
        buf.clear()
    def walk(s):
        for kind, v in tokenize(s):
            if kind == "text":
                buf.append(v)
                continue
            name = v[0]
            flush()
            if name in ("ח:ת", "ח:תת", "ח:תתת", "ח:תתתת"):
                labels = [a for a in v[1:] if a and not a.startswith("סוג=")]
                if labels: buf.append(" ".join(labels) + " ")
            elif name in ("ח:חיצוני", "ח:פנימי"):
                walk(v[-1])
            elif name == "ח:הערה":
                walk("|".join(v[1:]))
            elif name == "ח:חתימות":
                walk(v[1])
            else:
                buf.append("{{" + "|".join(v) + "}}")
    walk(line)
    flush()
    return out

def main():
    which, n = sys.argv[1], int(sys.argv[2]); m = int(sys.argv[3]) if len(sys.argv) > 3 else n
    path = INPUTS + {"law": "law.wiki", "ordinance": "ordinance.wiki"}[which]
    lines = open(path, encoding="utf-8", newline="").read().split("\n")
    tag = "" if which == "law" else "ordinance:"
    for k in range(n, m + 1):
        for seg in segments(unicodedata.normalize("NFC", lines[k-1])):
            print(f"-- src:{tag}{k} | {seg}")

if __name__ == "__main__":
    main()
