#!/usr/bin/env python3
"""Mechanical Hebrew quoting from the input files (no retyping).
usage: quote.py FILE LINE [LINE ...]      (1-based line numbers in FILE)
Strips Wikisource templates and bidi control marks; prints one cleaned line per requested line."""
import re, sys
BIDI = re.compile('[‎‏‪-‮⁦-⁩﻿️]')
def clean_wiki(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\{\{ח:(?:פנימי|חיצוני)\|[^{}|]*\|([^{}]*)\}\}', r'\1', s)
        s = re.sub(r'\{\{ח:(?:פנימי|חיצוני)\|([^{}|]*)\}\}', r'\1', s)
        s = re.sub(r'\{\{ח:הערה\|[^{}]*\}\}', '', s)
        s = re.sub(r'\{\{ח:תת+\|([^{}|]*)(?:\|[^{}]*)?\}\}', r'\1', s)
        s = re.sub(r'\{\{ח:ת(?:\|[^{}]*)?\}\}', '', s)
    s = s.replace('<br>', ' ')
    return re.sub(r'\s+', ' ', s).strip()
def main():
    path = sys.argv[1]
    lines = open(path, encoding='utf-8').read().split('\n')
    wiki = path.endswith('.wiki')
    for n in sys.argv[2:]:
        drop = 0; cut = None
        if '~' in n:
            n, cut = n.split('~', 1)
        if ':' in n:
            n, d = n.split(':'); drop = int(d)
        t = lines[int(n) - 1]
        if wiki:
            t = clean_wiki(t)
        else:
            t = re.sub(r'\s+', ' ', BIDI.sub(' ', t)).strip()
            t = re.sub(r'\s+([,.;:])', r'\1', t)
        if drop:
            t = ' '.join(t.split(' ')[:-drop])
        if cut:
            t = re.sub(cut, '', t).strip()
        print(t)
main()
