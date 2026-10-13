#!/usr/bin/env python3
"""Check that every Hebrew phrase in deposit/*.l4 occurs in an input text file (after normalisation).

Phrases that do not occur are listed with file:line.  The SimpLEX screenshot is an image, so its words
cannot be found in any text input: they are transcribed by eye and are expected to be listed here."""
import re, glob, pathlib

W = pathlib.Path(__file__).resolve().parent.parent
BIDI = re.compile('[‎‏‪-‮⁦-⁩﻿️]')

_src = (pathlib.Path(__file__).resolve().parent / 'quote.py').read_text(encoding='utf-8').split('def main')[0]
_ns = {}
exec(_src, _ns)
clean_wiki = _ns['clean_wiki']


def norm(s):
    s = BIDI.sub(' ', s)
    s = re.sub(r'[֑-ׇ]', '', s)                 # niqqud
    s = re.sub(r'["\'״׳“”‘’„]', '', s)                     # quote marks of every kind
    s = re.sub(r'[–־—\-]', ' ', s)                         # dashes and maqaf
    s = re.sub(r'[^א-ת0-9a-zA-Z]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def load(f):
    t = open(f, encoding='utf-8').read()
    if f.endswith('.wiki'):
        t = '\n'.join(clean_wiki(l) for l in t.split('\n'))
    return norm(t)


corpus = ' '.join(load(f) for f in glob.glob(str(W / 'inputs' / '*.txt')) + glob.glob(str(W / 'inputs' / '*.wiki')))
HEB = re.compile(r'[א-ת][א-ת"״\'׳\s\-–־.,:;()/\d]*[א-ת"״\'׳\d)]')
bad = []
total = 0
for f in sorted(glob.glob(str(W / 'deposit' / '*.l4'))):
    for i, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        pieces = []
        for m in HEB.finditer(line):
            pieces.extend(re.split(r'\.\.\.|\s/\s|",\s"', m.group(0)))
        for piece in pieces:
            ph = norm(piece)
            if len(ph.split()) < 2:
                continue
            total += 1
            if ph not in corpus:
                bad.append((pathlib.Path(f).name, i, piece[:100]))
print('phrases checked:', total, ' not found in any text input:', len(bad))
for b in bad:
    print('  %s:%d  %s' % b)
