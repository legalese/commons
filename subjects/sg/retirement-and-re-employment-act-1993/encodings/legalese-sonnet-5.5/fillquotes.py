#!/usr/bin/env python3
"""Expand `-- @@QUOTE N` / `-- @@QUOTE N-M` placeholder lines in .l4 files into `-- src:N | text` quote lines,
read mechanically from the raw text with srcrefs.py's own `quote` command (so the text is copied, never retyped).

  python3 -I fillquotes.py RAW FILE...
"""
import re, subprocess, sys, os

def main():
    raw = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    pat = re.compile(r'^(\s*)-- @@QUOTE (\d+)(?:-(\d+))?\s*$')
    for f in sys.argv[2:]:
        out = []
        n = 0
        with open(f, encoding='utf-8') as fh:
            for line in fh:
                m = pat.match(line.rstrip('\n'))
                if not m:
                    out.append(line)
                    continue
                a, b = m.group(2), m.group(3) or m.group(2)
                q = subprocess.run([sys.executable, '-I', os.path.join(here, 'srcrefs.py'), 'quote', raw, a, b],
                                   capture_output=True, text=True, check=True).stdout
                out.append(m.group(1) and ''.join(m.group(1) + l + '\n' for l in q.splitlines()) or q)
                n += 1
        if n:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(''.join(out))
        print(f"{f}: expanded {n} placeholder(s)")

main()
