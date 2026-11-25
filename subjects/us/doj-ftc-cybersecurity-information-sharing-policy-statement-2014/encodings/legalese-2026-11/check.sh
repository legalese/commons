#!/bin/sh
# Checks NOTES.md (the coverage table) against the deposited source text.
# No L4 is involved: this row encodes nothing. Needs only the system python3.
# Exit status 0 = every check passed; non-zero = at least one failed (each failure is printed).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
SUBJ="$HERE/../.."
exec /usr/bin/python3 -I - "$HERE" "$SUBJ" <<'PY'
import sys, re, json, hashlib, os
here, subj = sys.argv[1], sys.argv[2]
bundle = os.path.join(subj, 'registers', 'source-bundle')
meta = json.load(open(os.path.join(bundle, '2014-cybersecurity-information-sharing-policy-statement.meta.json'), encoding='utf-8'))
srcpath = os.path.join(bundle, meta['text_file'])
raw = open(srcpath, 'rb').read()
notes = open(os.path.join(here, 'NOTES.md'), encoding='utf-8').read()
fails = []
def check(ok, msg):
    print(('ok    ' if ok else 'FAIL  ') + msg)
    if not ok: fails.append(msg)
check(hashlib.sha256(raw).hexdigest() == meta['text_sha256'], 'sha256 of the deposited text equals the one in its .meta.json')
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-').replace('‐', '-').replace('‑', '-')
    s = re.sub(r'-\s*\n\s*', '-', s)
    return re.sub(r'\s+', ' ', s).strip().lower()
src = norm(raw.decode('utf-8'))
# the coverage table
sec3 = notes.split('## 3. Coverage table')[1].split('## 4.')[0]
rows = [l for l in sec3.split('\n') if l.startswith('| ') and not l.startswith('| ---') and not l.startswith('| id ')]
cells = [[c.strip() for c in l.strip().strip('|').split(' | ')] for l in rows]
body = [c for c in cells if not c[0].startswith('n.')]
fns = [c for c in cells if c[0].startswith('n.')]
check([c[0] for c in fns] == ['n.%d' % i for i in range(1, 22)], 'footnote rows are exactly n.1 to n.21, once each, in order')
check(len({c[0] for c in body}) == len(body), 'body row ids are unique (%d rows)' % len(body))
OK = {'encoded', 'inert', 'out-of-scope', 'deferred'}
check(all(c[3] in OK for c in cells), 'every disposition is one of encoded, inert, out-of-scope, deferred')
from collections import Counter
cnt = Counter(c[3] for c in cells)
m = re.search(r'Counts, computed from the table by `check.sh`: (\d+) rows \((\d+) body rows, (\d+) footnote rows\); encoded (\d+), inert (\d+), out-of-scope (\d+), deferred (\d+)', notes)
check(bool(m) and tuple(map(int, m.groups())) == (len(cells), len(body), len(fns), cnt['encoded'], cnt['inert'], cnt['out-of-scope'], cnt['deferred']),
      'the counts line in section 3 equals the table: %d rows (%d body, %d footnotes); encoded %d, inert %d, out-of-scope %d, deferred %d' % (len(cells), len(body), len(fns), cnt['encoded'], cnt['inert'], cnt['out-of-scope'], cnt['deferred']))
# per-page text, and the page on which each footnote's text begins (a line holding only the next expected number)
rawtxt = raw.decode('utf-8')
parts = re.split(r'\[pdf page (\d+) of 9\]\n', rawtxt)
pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
fnpage = {}; nxt = 1
for pg in sorted(pages):
    lines = pages[pg].split('\n')
    for i, l in enumerate(lines):
        if l.strip() == str(nxt) and not (i + 1 < len(lines) and re.match(r'^\d+$', lines[i + 1].strip())) and i + 1 < len(lines):
            fnpage[nxt] = pg; nxt += 1
check(len(fnpage) == 21, 'the text has 21 footnotes, each found by position (found %d)' % len(fnpage))
def firstpage(cell): return int(re.findall(r'\d+', cell)[0])
wrong = [(c[0], c[1], fnpage.get(int(c[0][2:]))) for c in fns if firstpage(c[1]) != fnpage.get(int(c[0][2:]))]
check(not wrong, 'each footnote row gives the page on which that footnote begins' + (' (wrong: %s)' % wrong if wrong else ''))
def pagetext(cell):
    ps = [int(x) for x in re.findall(r'\d+', cell)]
    rng = range(ps[0], ps[-1] + 1)
    return norm(' '.join(pages[p] for p in rng))
offpage = []
for c in cells:
    allowed = pagetext(c[1])
    for q in re.findall(r'"([^"\n]*)"', ' | '.join(c)):
        for frag in re.split(r'\.\.\.|\u2026', q):
            frag = norm(frag).strip(' ,.;:')
            if len(frag.split()) >= 5 and frag not in allowed: offpage.append((c[0], c[1], frag[:90]))
check(not offpage, 'every quotation of five words or more in a table row occurs on a page that row cites' + (''.join('\n      %s (pages %s): %s' % o for o in offpage) if offpage else ''))
# pages cited
bad = []
for c in cells:
    for p in re.findall(r'\d+', c[1]):
        if not 1 <= int(p) <= 9: bad.append((c[0], c[1]))
check(not bad, 'every pdf page cited in the table is between 1 and 9')
# quotations of five words or more, in straight double quotes: quotes are paired in order within each line
missing = []; unbalanced = []; n = 0
for ln, line in enumerate(notes.split('\n'), 1):
    pos = [i for i, ch in enumerate(line) if ch == '"']
    if len(pos) % 2: unbalanced.append(ln); continue
    for a_, b_ in zip(pos[0::2], pos[1::2]):
        for frag in re.split(r'\.\.\.|\u2026', line[a_+1:b_]):
            frag = norm(frag).strip(' ,.;:')
            if len(frag.split()) < 5: continue
            n += 1
            if frag not in src: missing.append((ln, frag))
check(not unbalanced, 'double quotes are balanced on every line of NOTES.md' + (' (unbalanced: lines %s)' % unbalanced if unbalanced else ''))
check(not missing, '%d quoted fragments of five words or more all occur in the source text' % n)
for ln, q in missing: print('      line %d not found: %s' % (ln, q[:140]))
# the status paragraph's claim that the text has no sentence about its own legal force
force = re.findall(r'\bforce\b|\bbinding\b|legal advice', src)
check(not force, 'the text has none of the words "force", "binding" or "legal advice" (as NOTES.md section 1 says)')
print('check.sh: %s' % ('all passed' if not fails else '%d FAILED' % len(fails)))
sys.exit(1 if fails else 0)
PY
