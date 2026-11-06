#!/usr/bin/env python3
"""Check that every double-quoted string that follows 'FALSE-kind (...)' or the yes-comments in the
ma-*.l4 modules is a verbatim slice of the deposited text (whitespace collapsed).
Pieces joined by ' ... ' are checked one by one.
Usage: python3 -I check-quotes.py RAW FILE...
Only comment lines are read.  A quoted string that is not in RAW is reported and the exit status is 1."""
import re, sys
import os
raw = open(sys.argv[1], encoding='utf-8').read()
# The copied Interpretation Act module quotes its own words with escaped quotation marks; its entries are checked against it too.
_ia = os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])), 'sgia-p1-definitions.l4')
if os.path.exists(_ia):
    raw += '\n' + open(_ia, encoding='utf-8').read().replace('\\"', '"')
ALLOW = {'include', 'includes', 'means', 'deducted'}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
src = norm(raw)
pat = re.compile(r'--[^"\n]*?\b(?:FALSE-kind|NOTHING-kind|the text.s yes)[^"\n]*?:?\s*"((?:[^"\\]|\\.)*)"')
bad = n = 0
for f in sys.argv[2:]:
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        if not line.lstrip().startswith('--') and ' -- ' not in line:
            continue
        for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', line[line.index('--'):] if '--' in line else ''):
            text = m.group(1)
            # only strings in kind-comments, not strings that quote another Act
            head = line[:m.start()]
            if not re.search(r'FALSE-kind|NOTHING-kind|text.s yes|"\(a\)', head) and 'yes:' not in head and 'THEN JUST TRUE --' not in head:
                continue
            text = text.replace('\\"', '"')
            for piece in [p for p in re.split(r'\s*\.\.\.\s*', text) if p.strip()]:
                if piece in ALLOW or piece.startswith('Reading a result'):
                    continue
                n += 1
                if norm(piece) not in src:
                    bad += 1
                    print(f'{f}:{i}: not in the text: {piece[:100]!r}')
print(f'check-quotes: {n} quoted pieces checked, {bad} not found')
sys.exit(1 if bad else 0)
