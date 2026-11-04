#!/usr/bin/env python3
# check-tv-citations.py : the check srcrefs.py cannot make for the sgta-tv-* modules and TV-QUESTION.md.
# Those files carry no `src:` quote lines or @ref locators (so `srcrefs.py check --strict` finds 0 lines in them: that is not a pass of anything),
# they cite deposited texts in comments and strings as FILE.txt:N or FILE.txt:N-M.  This script
#   (1) resolves every such locator to its deposited file (under subjects/sg/*/registers/source-bundle/) and checks that each line number exists and each range runs forwards;
#   (2) checks every fragment in single quotes (12 or more characters) inside the Rg 1 table's strings in sgta-tv-ba-schedule.l4 against the three Broadcasting Act deposits it quotes
#       (BA1994-RG1.txt, BA1994-S333-2004.txt, BA1994-S548-2012.txt), after joining line-end hyphens and squeezing whitespace.
# It does not check that a locator names the right provision.  Exit 1 on any problem.
import re, sys, glob, os
here = os.path.dirname(os.path.abspath(__file__))
subj = os.path.normpath(os.path.join(here, "../../.."))
files = ["sgta-tv-seat.l4", "sgta-tv-cases.l4", "sgta-tv-ba-schedule.l4", "TV-QUESTION.md"]
index = {}
for p in glob.glob(subj + "/*/registers/source-bundle/*.txt"):
    index.setdefault(os.path.basename(p), []).append(p)
nlines = {}
def count(p):
    if p not in nlines: nlines[p] = len(open(p, encoding="utf-8", errors="replace").read().split("\n"))
    return nlines[p]
loc_re = re.compile(r"([A-Za-z0-9][A-Za-z0-9._-]*\.txt):((?:\d+(?:-\d+)?)(?:, ?\d+(?:-\d+)?)*)")
problems = 0; nloc = 0; nfile = {}
for f in files:
    t = open(os.path.join(here, f), encoding="utf-8").read(); n = 0
    for m in loc_re.finditer(t):
        name, spec = m.group(1), m.group(2)
        cands = index.get(name)
        if not cands: print("PROBLEM %s: no deposited file named %s" % (f, name)); problems += 1; continue
        if len(cands) > 1: print("PROBLEM %s: %s is deposited %d times" % (f, name, len(cands))); problems += 1; continue
        top = count(cands[0])
        for part in spec.split(","):
            part = part.strip(); a, _, b = part.partition("-"); a = int(a); b = int(b) if b else a
            n += 1
            if not (1 <= a <= b <= top):
                print("PROBLEM %s: %s:%s is outside 1..%d" % (f, name, part, top)); problems += 1
    nfile[f] = n; nloc += n
# (2) the quoted fragments of the Rg 1 table
def norm(t):
    for a, b in (("‘‘", "'"), ("’’", "'"), ("“", '"'), ("”", '"'), ("’", "'"), ("‘", "'"), ("—", "-"), ("–", "-")): t = t.replace(a, b)
    t = re.sub(r"-\s*\n\s*", "-", t); t = re.sub(r"\s+", " ", t)
    return t.lower().replace("telecom-munications", "telecommunications").replace("receive- only", "receive-only")
deps = " ".join(norm(open(index[n][0], encoding="utf-8").read()) for n in ("BA1994-RG1.txt", "BA1994-S333-2004.txt", "BA1994-S548-2012.txt"))
src = open(os.path.join(here, "sgta-tv-ba-schedule.l4"), encoding="utf-8").read()
i = src.index("`what Rg 1 in the version says in terms about a licence for the kind of receiver in the place` MEANS")
j = src.index("`what Rg 1 says in terms about a licence for the kind of receiver in the place, for the conduct day")
nfrag = 0
for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', src[i:j]):
    for q in re.finditer(r"'([^']{12,}?)'(?= |,|;|\)|$)", m.group(1)):
        for pt in re.split(r"\.\.\.", q.group(1)):
            pt = norm(pt).strip().rstrip(".")
            if not pt: continue
            nfrag += 1
            if pt not in deps: print("PROBLEM Rg 1 table: quoted fragment not in the deposits: %s" % pt[:100]); problems += 1
print("tv citations check: %d locators in %d files (%s), %d quoted fragments of the Rg 1 table, %d problems" % (nloc, len(files), ", ".join("%s %d" % (k, v) for k, v in nfile.items()), nfrag, problems))
sys.exit(1 if problems else 0)
