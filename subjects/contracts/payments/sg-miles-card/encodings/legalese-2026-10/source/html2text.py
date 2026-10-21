#!/usr/bin/env python3
"""html2text.py START END < page.html > clause.txt
Deterministic text extraction for an HTML terms page: drops script/style, turns tags into
newlines, unescapes entities, collapses blank lines, and keeps the text from the LAST line
equal to START through the first line equal to END (inclusive) that follows it."""
import sys, re, html
start, end = sys.argv[1], sys.argv[2]
s = sys.stdin.read()
s = re.sub(r'<(script|style|noscript)\b.*?</\1>', '', s, flags=re.S | re.I)
s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
s = re.sub(r'<[^>]+>', '\n', s)
s = html.unescape(s).replace('\xa0', ' ')
lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in s.split('\n')]
lines = [l for l in lines if l]
i = max(k for k, l in enumerate(lines) if l == start)
j = next(k for k in range(i, len(lines)) if lines[k] == end)
sys.stdout.write('\n'.join(lines[i:j + 1]) + '\n')
