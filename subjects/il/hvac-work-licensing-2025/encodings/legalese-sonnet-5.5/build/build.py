#!/usr/bin/env python3
"""Expand @@Q <file> <spec...>@@ placeholders into '-- ' comment lines of mechanically quoted Hebrew.
spec: N | N:dropWords | N~regex  (regex may use \\s for space). Reads build/src/*.l4.in, writes deposit/*.l4"""
import re, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
WORK = HERE.parent
INP = WORK / 'inputs'
DEP = WORK / 'deposit'
FILES = {'law': 'law.wiki', 'fees': 'regulations-fees.wiki', 'made': 'kovetz-hatakanot-11951-p2116.txt',
         'amend': 'takanot-12383.txt', 'gaz': 'sefer-hachukim-3349-pp182-209.txt'}
PH = re.compile(r'^(\s*)@@Q\s+(\w+)\s+(.*?)@@\s*$')
def expand(line):
    m = PH.match(line)
    if not m:
        return [line]
    indent, key, specs = m.groups()
    out = subprocess.run([sys.executable, '-I', str(HERE / 'quote.py'), str(INP / FILES[key])] + specs.split(),
                         capture_output=True, text=True, check=True).stdout.rstrip('\n').split('\n')
    return [f'{indent}-- {t}' for t in out]
def main():
    names = sys.argv[1:] or [p.name[:-3] for p in sorted((HERE / 'src').glob('*.l4.in'))]
    for name in names:
        src = (HERE / 'src' / (name + '.in')) if name.endswith('.l4') else (HERE / 'src' / (name + '.l4.in'))
        out = []
        for line in src.read_text(encoding='utf-8').split('\n'):
            out.extend(expand(line))
        target = DEP / (src.name[:-3])
        target.write_text('\n'.join(out), encoding='utf-8')
        print('wrote', target.name, len(out), 'lines')
main()
