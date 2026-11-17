#!/usr/bin/env python3
"""quotecheck.py TEXT[,TEXT2...] FILE...  -- every double-quoted fragment inside a `--` comment of the .l4 files that looks German,
or that is found in the text, is checked to be a verbatim slice of the text (NFC, case-folded, whitespace and footnote
markers collapsed; ' ... ' or an ellipsis inside a quotation means a gap).  Prints the fragments that are NOT found, so a
typo in a German quotation shows.  A quotation that is plain English (no German word) is ignored and counted.
Exit 1 if any German-looking fragment is not found."""
import re, sys, unicodedata
def norm(s):
    s = unicodedata.normalize('NFC', s).casefold()
    s = re.sub(r'\[\^\d+\]', '', s)
    s = s.replace('‑', '-').replace('–', '-').replace('’', "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return s
texts = [norm(open(t, encoding='utf-8').read()) for t in sys.argv[1].split(",")]
GERMAN = re.compile(r'[äöüß]|\b(der|die|das|den|dem|des|und|oder|wenn|nicht|sind|kann|soweit|sofern|eines|einer|einen|nur|über|gegen|jederzeit|innert|tage|tagen|diese|dieser|diesen|wird|werden|solange|bei)\b')
bad = 0; ok = 0; eng = 0
for f in sys.argv[2:]:
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        if '--' not in line: continue
        com = line[line.index('--'):]
        if com.startswith('-- src:'): continue
        for m in re.finditer(r'"([^"]+)"', com):
            frag = m.group(1)
            parts = [p for p in re.split(r'\s*(?:\.\.\.|…)\s*', frag) if norm(p)]
            if not parts: continue
            found = all(any(norm(re.sub(r'[,;:.]+$', '', p)) in t for t in texts) for p in parts)
            if found: ok += 1
            elif GERMAN.search(frag.casefold()):
                bad += 1; print(f'{f}:{i}: not in the text: "{frag}"')
            else: eng += 1
print(f'quotecheck: {ok} fragments found in the text, {bad} German-looking fragments NOT found, {eng} English fragments ignored')
sys.exit(1 if bad else 0)
