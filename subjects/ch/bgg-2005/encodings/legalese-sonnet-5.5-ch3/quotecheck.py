#!/usr/bin/env python3
"""quotecheck.py: check that every German phrase quoted in a `-- ...` comment of an .l4 file is in the text.

usage: python3 -I quotecheck.py RAWTEXT FILE.l4 ...   (a FILE.md is checked on every line)

A quoted phrase is anything between double quotes in a comment (after `--`).  A phrase is split at `...`
(an elision) into fragments; each fragment is compared with the text after whitespace is collapsed and the
footnote markers `[^N]` are removed.  Straight quotes only; a fragment shorter than 3 characters is skipped.
Prints each fragment that is not in the text, and a summary line.  Exit status 1 if any is missing.
It checks that the words quoted ARE in the text, not that the comment draws the right conclusion from them.
"""
import re, sys
raw = open(sys.argv[1], encoding="utf-8").read()
raw = re.sub(r"\[\^\d+\]", "", raw)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
hay = norm(raw)
total = bad = 0
for path in sys.argv[2:]:
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("-- src:") or line.startswith("-- src "):
            continue
        if path.endswith(".md"):
            comment = line                      # a Markdown file: every double-quoted phrase is German
        else:
            i = line.find("--")
            if i < 0:
                continue
            comment = line[i:]
        for q in re.findall(r'"([^"]+)"', comment):
            for frag in re.split(r"\s*\.\.\.\s*|\s*…\s*", q):
                frag = norm(re.sub(r"\[\^\d+\]", "", frag)).strip(" ;,")
                if len(frag) < 3:
                    continue
                total += 1
                if frag not in hay:
                    bad += 1
                    print("%s:%d: not in the text: %r" % (path, n, frag[:140]))
print("quotecheck: %d quoted fragments checked, %d not found in the text" % (total, bad))
sys.exit(1 if bad else 0)
