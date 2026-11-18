#!/usr/bin/env python3
"""coverage.py [--md]  -- build the coverage table of chapter 4 from the text, by script, and check it against the .l4 files.
  python3 -I coverage.py            print the summary and every check (exit 1 on a failed check)
  python3 -I coverage.py --md       print the coverage table as Markdown, then the summary
The rows come from the text (coverage_rows.py): one per heading, paragraph, list item and sentence split.  The disposition,
the fork marks and the function-to-row map come from coverage_data.py and from the function names in the .l4 files.
Checks: every non-blank line of the text is in some row; every row has exactly one disposition; every layer-1 function is
mapped to a row; every function has a test line that names it (or is a composite whose parts do); every seat question calls
a layer-1 function and has a case; no row is out-of-scope or deferred; inert rows give reason 1, 2 or 3."""
import glob, os, re, sys
sys.dont_write_bytecode = True   # leave no __pycache__ in the deposit
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coverage_rows import load, rows, sentence_text
from coverage_data import EXTRA, FORKS, JURAL, TEXTOVER, TEXTROWS
HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.join(HERE, '..', '..', '..', 'inputs', 'ch-bgg-sr173110-ch4-art-90-112-20260401.txt')
if not os.path.exists(TEXT): TEXT = os.path.join(HERE, 'ch-bgg-sr173110-ch4-art-90-112-20260401.txt')
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
if _args: TEXT = _args[0]            # python3 -I coverage.py <text file> [--md|--jural|--forks|--noseat|--modules]
raw = load(TEXT)
R = rows(raw)
byid = {r['id']: r for r in R}
# ---- layer-1 functions (names) by module
def functions(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    for i, l in enumerate(lines):
        if l.startswith('`') and ' MEANS' in l:
            out.append(l.split('` MEANS')[0][1:])
    return out
L1FILES = [f for f in sorted(glob.glob(HERE + '/bgg4-*.l4')) if not any(x in os.path.basename(f) for x in ('tests', 'seat', 'cases'))]
FN = {}
for f in L1FILES:
    for n in functions(f): FN[n] = os.path.basename(f)[:-3]
# ---- map functions to rows
def rows_for(name):
    if name in EXTRA: return EXTRA[name]
    m = re.match(r'^(Art (\d+[a-z]*))((?:\([0-9a-z]+\))*)', name)
    art, num, tail = m.group(1), m.group(2), m.group(3)
    limbs = re.findall(r'\(([0-9a-z]+)\)', tail)
    ids = []
    if not limbs:  # whole article
        ids = [r['id'] for r in R if r['kind'] in ('para', 'item', 'sentence') and r['id'].startswith(art + '(') or r['id'] in (art, art + ' (intro)')]
    else:
        p = limbs[0]
        if len(limbs) >= 2:
            ids = [f'{art}({p})({limbs[1]})']
            if f'{art}({p})({limbs[1]})' not in byid: ids = [f'{art}({p})({limbs[1]})']
        else:
            # a bare letter limb with no paragraph (Art 91(a)) is an item; a number is a paragraph
            if p.isdigit():
                ids = [r['id'] for r in R if r['id'] == f'{art}({p})' or r['id'].startswith(f'{art}({p})(') or r['id'].startswith(f'{art}({p}) ')]
            else:
                ids = [f'{art}({p})']
    return ids
FROWS = {}
for n in FN:
    ids = rows_for(n)
    FROWS[n] = ids
# ---- tests
TESTS = {}
for f in sorted(glob.glob(HERE + '/bgg4-tests-*.l4')):
    for i, l in enumerate(open(f, encoding='utf-8'), 1):
        if l.startswith('#ASSERT') or l.startswith('#TRACE') or l.startswith('#EVAL'):
            for n in FN:
                if '`' + n + '`' in l:
                    TESTS.setdefault(n, set()).add((os.path.basename(f), i))
# ---- seat
seat = open(HERE + '/bgg4-seat.l4', encoding='utf-8').read()
SEAT = {}  # seat question -> layer-1 names it calls
for m in re.finditer(r'DECIDE `([^`]+)` IS\n((?:    .*\n)+)', seat):
    called = [n for n in FN if '`' + n + '`' in m.group(2)]
    SEAT[m.group(1)] = called
cases = open(HERE + '/bgg4-cases-seat.l4', encoding='utf-8').read()
SEATCASES = {q: len(re.findall(r'#ASSERT \(?`' + re.escape(q) + '`', cases)) for q in SEAT}
# ---- dispositions
forkrows = {}
SEAMFORKS = {'F28', 'F29'}   # forks about how the sections are put together in bgg4-seams: listed in the register, they do not mark the rows' own dispositions
for fid, title, frows, taken, other in FORKS:
    for r in frows:
        assert r in byid, (fid, r)
        if fid not in SEAMFORKS: forkrows.setdefault(r, []).append(fid)
STUBS = {'Art 100(6)', 'Art 111(3) second sentence'}
def disposition(r):
    k = r['kind']
    if k == 'header': return 'inert (reason 1: not operative, the file header)'
    if k == 'heading': return 'inert (reason 1: a heading)'
    if k == 'footnotes': return 'inert (reason 1: not operative, amendment history; footnotes 9 and 15 show the two repealed rows)'
    if r['id'] in STUBS: return 'repealed or blank in this text'
    if r['id'] in forkrows: return 'fork ' + ', '.join(forkrows[r['id']])
    return 'encoded'
problems = []
def check(cond, msg):
    if not cond: problems.append(msg)
cov = set()
for r in R:
    for n in range(r['a'], r['b'] + 1): cov.add(n)
for n, l in enumerate(raw, 1):
    check(l.strip() == '' or n in cov, f'text line {n} is in no row')
for n, fs in FROWS.items():
    check(fs, f'function with no row: {n}')
    for i in fs: check(i in byid, f'{n}: row {i} does not exist')
rowfun = {r['id']: [] for r in R}
for n, fs in FROWS.items():
    for i in fs:
        if i in rowfun: rowfun[i].append(n)
for r in R:
    d = disposition(r)
    if d.startswith('encoded') or d.startswith('fork'):
        check(rowfun[r['id']], f'row {r["id"]} is {d} but no function implements it')
L1TEXT = ''.join(open(f, encoding='utf-8').read() for f in L1FILES)
STUBFN = {n for n in FN if n.endswith('is shown repealed in this text and is not encoded')}
for n in FN:
    if n in STUBFN: continue
    if not TESTS.get(n):
        # a function used only inside others is exercised through them: accept if another definition calls it (the count minus its own definition line)
        check(L1TEXT.count('`' + n + '`') - 1 >= 1, f'function with no test and no caller: {n}')
for q, called in SEAT.items():
    check(called, f'seat question calls no layer-1 function: {q}')
    check(SEATCASES.get(q, 0) >= 1, f'seat question with no case: {q}')
def row_tests(r):
    s = set()
    for n in rowfun[r['id']]: s |= TESTS.get(n, set())
    return len(s)
# call graph among layer-1 functions (a function's block runs from its definition line to the next definition line)
CALLS = {}
for f in L1FILES:
    t = open(f, encoding='utf-8').read().split('\n')
    starts = [(i, l.split('` MEANS')[0][1:]) for i, l in enumerate(t) if l.startswith('`') and ' MEANS' in l]
    for k, (i, n) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(t)
        block = '\n'.join(t[i:j])
        CALLS[n] = [m for m in FN if m != n and '`' + m + '`' in block]
def closure(names):
    seen = set(); todo = list(names)
    while todo:
        n = todo.pop()
        if n in seen: continue
        seen.add(n); todo += CALLS.get(n, [])
    return seen
SEATCLOSURE = {q: closure(called) for q, called in SEAT.items()}
def row_seat(r):
    qs = []
    for q, cl in SEATCLOSURE.items():
        if any(n in rowfun[r['id']] for n in cl): qs.append(q)
    return qs
def row_seat_old(r):
    qs = []
    for q, called in SEAT.items():
        if any(n in rowfun[r['id']] for n in called): qs.append(q)
    return qs
counts = {}
for r in R:
    d = disposition(r).split(' ')[0] + (' ' + disposition(r).split(' ')[1] if disposition(r).startswith(('repealed', )) else '')
    key = 'inert' if d.startswith('inert') else ('fork' if d.startswith('fork') else ('repealed or blank' if d.startswith('repealed') else 'encoded'))
    counts[key] = counts.get(key, 0) + 1
inert_reasons = {1: 0, 2: 0, 3: 0}
for r in R:
    d = disposition(r)
    if d.startswith('inert'): inert_reasons[int(re.search(r'reason (\d)', d).group(1))] += 1
if '--md' in sys.argv:
    print('| row | lines | German begins | disposition | modules | tests | seat questions |')
    print('| --- | --- | --- | --- | --- | --- | --- |')
    for r in R:
        d = disposition(r)
        mods = sorted({FN[n] for n in rowfun[r['id']]})
        txt = sentence_text(raw, r['a'], r['id']) if r['kind'] == 'sentence' else raw[r['a'] - 1]
        txt = re.sub(r'^\s*[0-9a-z]\.(\[\^\d+\])? ?', '', txt).strip() if r['kind'] == 'item' else re.sub(r'^\d+ ', '', txt) if r['kind'] in ('para', 'sentence') else txt
        txt = txt[:44].replace('|', '/')
        lines = f'{r["a"]}' if r['a'] == r['b'] else f'{r["a"]}-{r["b"]}'
        sq = len(row_seat(r))
        print(f'| {r["id"]} | {lines} | {txt} | {d} | {", ".join(m.replace("bgg4-", "") for m in mods)} | {row_tests(r) or ""} | {sq or ""} |')
    print()
def fork_text(fid, frows):
    if fid in TEXTOVER:
        t, ln = TEXTOVER[fid]
        if t == 'CH3':
            ch3 = os.path.join(os.path.dirname(TEXT), 'ch-bgg-sr173110-ch3-art-72-89-20260401.txt')
            return 'chapter 3, Art 77(2), line %d: "%s"' % (ln, re.sub(r'^\d+ ', '', open(ch3, encoding='utf-8').read().split('\n')[ln - 1].strip()))
        return t
    out = []
    for rid in TEXTROWS.get(fid, [frows[0]]):
        r0 = byid[rid]
        t = sentence_text(raw, r0['a'], r0['id']) if r0['kind'] == 'sentence' else raw[r0['a'] - 1]
        t = re.sub(r'^\s*[0-9a-z]\.(\[\^\d+\])? ?', '', t).strip() if r0['kind'] == 'item' else re.sub(r'^\d+ ', '', t) if r0['kind'] in ('para', 'sentence') else t
        if len(t) > 300: t = t[:300].rsplit(' ', 1)[0] + ' ...'
        out.append(rid + ' "' + t + '"')
    return ' / '.join(out)
DEONTIC = set()
for f in L1FILES:
    txt = open(f, encoding='utf-8').read().split('\n')
    for i, l in enumerate(txt):
        if l.startswith('GIVETH A DEONTIC'):
            for k in range(i + 1, min(i + 3, len(txt))):
                if txt[k].startswith('`') and ' MEANS' in txt[k]: DEONTIC.add(txt[k].split('` MEANS')[0][1:])
for r in R:
    if r['kind'] in ('para', 'item', 'sentence'):
        check(r['id'] in JURAL, f'no Jural relations entry for {r["id"]}')
def rule_cell(r):
    names = rowfun[r['id']]
    own = [n for n in names if n.startswith(r['id'].replace(' (intro)', '').replace(' first sentence', '').replace(' second sentence', '').replace(' third sentence', '')) and not n.startswith(r['id'] + 'x')]
    label = re.sub(r' (\(intro\)|first sentence|second sentence|third sentence)$', '', r['id'])
    exact = lambda n: bool(re.match(re.escape(label) + r' (?!to |and )', n))
    pick = sorted(set(own or names), key=lambda n: (not exact(n), n not in DEONTIC, len(n)))
    if not pick: return ''
    cell = '`' + pick[0] + '`'
    if len(pick) > 1: cell += f' (+{len(pick) - 1} more)'
    return cell
if '--jural' in sys.argv:
    print('| provision | kind (holder / bearer) | holder | bearer | rule |')
    print('| --- | --- | --- | --- | --- |')
    for r in R:
        if r['kind'] not in ('para', 'item', 'sentence'): continue
        kind, holder, bearer = JURAL[r['id']]
        if kind == 'none':
            print(f'| {r["id"]} | none | {holder} | | {rule_cell(r)} |')
        else:
            print(f'| {r["id"]} | {kind} | {holder} | {bearer} | {rule_cell(r)} |')
    print()
if '--forks' in sys.argv:
    for fid, title, frows, taken, other in FORKS:
        names = []
        for r in frows:
            for n in rowfun[r]:
                if n not in names: names.append(n)
        labels = [re.sub(r' (\(intro\)|first sentence|second sentence|third sentence)$', '', r) for r in frows]
        exact = lambda n: any(re.match(re.escape(l) + r' (?!to |and )', n) for l in labels)
        names.sort(key=lambda n: (not exact(n), n not in DEONTIC, len(n)))
        ex = [n for n in names if exact(n)]
        show = ex[:5] if ex else names[:3]
        shown = ', '.join('`' + n + '`' for n in show) + (f' (and {len(names) - len(show)} more, with the composites and the seams that call them)' if len(names) > len(show) else '')
        txt = fork_text(fid, frows)
        print(f'- **{fid}. {title}.**')
        print(f'  Text: {txt}' + ('.' if fid in ('F4', 'F28') else ''))
        print(f'  Readings: (i) {taken}; (ii) {other}.')
        print(f'  Taken: (i).')
        print(f'  Rows: {", ".join(frows[:8])}' + (f' and {len(frows) - 8} more' if len(frows) > 8 else '') + '.')
        print(f'  Rule: {shown}.')
    print()
if '--noseat' in sys.argv:
    for r in R:
        if r['kind'] in ('para', 'item', 'sentence') and disposition(r) != 'repealed or blank in this text' and not row_seat(r):
            print(r['id'])
if '--modules' in sys.argv:
    mods = {}
    for n, m in FN.items(): mods.setdefault(m, []).append(n)
    for m in sorted(mods): print(f'{m}\t{len(mods[m])}\t{sum(1 for n in mods[m] if n in DEONTIC)}')
nonblank = sum(1 for l in raw if l.strip())
print(f'text lines: {len(raw)}, non-blank: {nonblank}, rows: {len(R)}; operative rows: {sum(1 for r in R if r["kind"] in ("para","item","sentence"))}; heading rows: {sum(1 for r in R if r["kind"]=="heading")}')
print('dispositions:', ', '.join(f'{k}: {v}' for k, v in sorted(counts.items())), '; inert by reason:', inert_reasons)
print(f'layer-1 functions: {len(FN)} (regulative rules: {sum(1 for f in L1FILES for l in open(f, encoding="utf-8").read().split(chr(10)) if l.startswith("GIVETH A DEONTIC"))}); forks: {len(FORKS)}; seat questions: {len(SEAT)}; seat cases: {sum(SEATCASES.values())}')
direct = sum(1 for n in FN if TESTS.get(n)); stubs = len(STUBFN)
print(f'functions tested by an assertion or trace that names them: {direct}; only exercised through a caller: {len(FN) - direct - stubs}; labelled repealed stubs (no outcome, nothing calls them): {stubs}')
print('problems:', len(problems))
for p in problems: print('  PROBLEM', p)
sys.exit(1 if problems else 0)
