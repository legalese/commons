# tracetable.py: print every #TRACE of the test files with its clock, event and outcome (one line each); the traces are printed, not asserted.
import subprocess, re, sys, os, glob
DEP = os.path.dirname(os.path.abspath(__file__)); L4 = os.environ['L4']   # run in this folder with L4 set to the l4 binary
rows = []
for f in sorted(glob.glob(DEP + '/bgg4-tests-*.l4')):
    src = open(f, encoding='utf-8').read().split('\n')
    out = subprocess.run([L4, 'run', os.path.basename(f)], cwd=DEP, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True).stdout
    blocks = re.split(r'\nEvaluation\[\d+\] @ ', out)
    res = {}
    for b in blocks[1:]:
        m = re.match(r'[^:]+:(\d+):', b)
        r = re.search(r'Result:\n((?:  .*\n?)+)', b)
        if m and r: res[int(m.group(1))] = ' '.join(x.strip() for x in r.group(1).strip().split('\n'))
    for i, l in enumerate(src, 1):
        if l.startswith('#TRACE'):
            name = re.search(r'`([^`]+)`', l).group(1)
            args = l[l.index('`', l.index(name)) + 1:].strip()
            nxt = src[i].strip() if i < len(src) else ''
            ev = re.search(r'DOES `([^`]+)` AT (\d+)', nxt)
            clock = re.search(r'AT (\d+) WITH', l)
            outcome = res.get(i, '?')
            outcome = re.sub(r'\s+', ' ', outcome)
            rows.append((os.path.basename(f), i, name, (args.split(' AT ')[0] or '').strip(), clock.group(1) if clock else '', (ev.group(1) + ' at ' + ev.group(2)) if ev else 'no event', outcome[:110]))
for r in rows: print(' | '.join(str(x) for x in r))
