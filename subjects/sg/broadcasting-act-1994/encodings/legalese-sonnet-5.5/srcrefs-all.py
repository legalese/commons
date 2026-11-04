#!/usr/bin/env python3
"""Run srcrefs.py --strict over every module of this encoding that quotes a source, against the texts deposited in this repository.

Run:  python3 -I srcrefs-all.py     (prints one line per group and a total; exit 0 only when every group has 0 problems)

Groups:
  1. the Act modules (sgba-p*, sgba-nouns, sgba-vintage, sgba-sched, sgba-versions, sgba-tv-*) against the consolidation BA1994.txt;
  2. the three modules that quote more than one deposit (sgba-versions-acts, sgba-versions-later, sgba-i-s212-2022), through a temporary
     directory of symlinks, because srcrefs.py finds a second deposit only beside the first; the directory is removed when the run ends;
  3. every other instrument module (sgba-i-*), each against its own deposit (the table INSTR below).
sgba-tv-seat, sgba-tv-cases-seat and sgba-tv-s9a quote no source text of their own, so for them this run checks nothing ("included, vacuous");
sgba-seat and sgba-cases-seat likewise.  Whether a locator names the right provision is a person reading the cited lines, not this script.
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJ = os.path.normpath(os.path.join(HERE, "../../.."))
SR = os.path.join(HERE, "srcrefs.py")
ACT = os.path.join(SUBJ, "broadcasting-act-1994/registers/source-bundle/BA1994.txt")
MULTI = [("sgba-versions-acts", "BA1994"), ("sgba-versions-later", "BA1994"), ("sgba-i-s212-2022", "BA1994-S212-2022")]
# module, subject folder under subjects/sg/, stem of the deposited text in that folder's registers/source-bundle/
INSTR = [
    ("sgba-i-tvro-regs", "broadcasting-tvro-system-regulations-1991", "BA1994-RG3"),
    ("sgba-i-composition", "broadcasting-composition-of-offences-regulations-2004", "BA1994-RG2"),
    ("sgba-i-class-licence", "broadcasting-class-licence-notification-1996", "BA1994-N1"),
    ("sgba-i-digital-panels", "broadcasting-class-licence-digital-display-panels-notification-2020", "BA1994-S477-2020"),
    ("sgba-i-exempt-1996", "broadcasting-exemption-order-1996", "BA1994-OR1"),
    ("sgba-i-exempt-no2", "broadcasting-exemption-no-2-order-2002", "BA1994-OR2"),
    ("sgba-i-exempt-no3", "broadcasting-exemption-no-3-order-2004", "BA1994-OR3"),
    ("sgba-i-exempt-2008", "broadcasting-exemption-order-2008", "BA1994-S121-2008"),
    ("sgba-i-exempt-2022", "broadcasting-exemption-order-2022", "BA1994-S211-2022"),
    ("sgba-i-exempt-educ", "broadcasting-exemption-educational-institutions-order-2010", "BA1994-S523-2010"),
    ("sgba-i-service-website", "broadcasting-service-of-documents-website-notification-2023", "BA1994-S30-2023"),
    ("sgba-i-online-cop-rules", "broadcasting-online-codes-of-practice-procedure-rules-2023", "BA1994-S47-2023"),
    ("sgba-i-s549-2012", "broadcasting-amendment-of-first-schedule-notification-2012", "BA1994-S549-2012"),
    ("sgba-i-s559-2010", "broadcasting-amendment-of-third-schedule-notification-2010", "BA1994-S559-2010"),
    ("sgba-i-rg1", "broadcasting-television-and-radio-licensing-regulations", "BA1994-RG1"),
    ("sgba-i-s333-2004", "broadcasting-television-and-radio-licensing-amendment-regulations-2004", "BA1994-S333-2004"),
    ("sgba-i-s548-2012", "broadcasting-television-and-radio-licensing-revocation-regulations-2012", "BA1994-S548-2012"),
    ("sgba-i-s212-1999", "singapore-broadcasting-authority-broadcasting-and-television-amendment-regulations-1999", "BA1994-S212-1999"),
    ("sgba-i-s354-2001", "singapore-broadcasting-authority-tvro-system-amendment-regulations-2001", "BA1994-S354-2001"),
    ("sgba-i-s600-2014", "broadcasting-exemption-amendment-order-2014", "BA1994-S600-2014"),
    ("sgba-i-or1-2004", "broadcasting-exemption-order-1996", "BA1994-OR1.20040229"),
    ("sgba-i-s523-2010-schedule", "broadcasting-exemption-educational-institutions-order-2010", "BA1994-S523-2010.20100916"),
    ("sgba-i-s478-2020", "broadcasting-class-licence-amendment-notification-2020", "BA1994-S478-2020"),
    ("sgba-i-s196-2004", "broadcasting-class-licence-amendment-notification-2004", "BA1994-S196-2004"),
    ("sgba-i-s555-2003", "broadcasting-class-licence-amendment-notification-2003", "BA1994-S555-2003"),
    ("sgba-i-s496-2001", "singapore-broadcasting-authority-class-licence-amendment-notification-2001", "BA1994-S496-2001"),
    ("sgba-i-s70-2012", "broadcasting-class-licence-amendment-notification-2012", "BA1994-S70-2012"),
    ("sgba-i-s330-2013", "broadcasting-class-licence-amendment-notification-2013", "BA1994-S330-2013"),
    ("sgba-i-s674-2016", "broadcasting-class-licence-amendment-notification-2016", "BA1994-S674-2016"),
]


def run(raw, mods):
    o = subprocess.run([sys.executable, "-I", SR, "check", "--strict", raw] + mods, capture_output=True, text=True)
    lines = o.stdout.strip().split("\n")
    return o.returncode, (lines[-1] if lines else "")


tot = [0, 0, 0, 0]
bad = 0


def add(line, rc):
    global bad
    m = re.search(r"(\d+) src: lines, (\d+) runs, (\d+) locators, (\d+) problems", line)
    if not m or rc:
        print("PROBLEM:", line)
        bad += 1
        if not m:
            return
    for i in range(4):
        tot[i] += int(m.group(i + 1))


def mod(name):
    return os.path.join(HERE, name + ".l4")


acts = (sorted(glob.glob(os.path.join(HERE, "sgba-p*.l4")))
        + [mod(x) for x in ("sgba-nouns", "sgba-vintage", "sgba-sched", "sgba-versions")]
        + sorted(glob.glob(os.path.join(HERE, "sgba-tv-*.l4"))))
acts = [m for m in acts if os.path.basename(m) not in ("sgba-versions-acts.l4", "sgba-versions-later.l4")]
rc, line = run(ACT, acts)
print("Act modules (%d files): %s" % (len(acts), line))
add(line, rc)

with tempfile.TemporaryDirectory() as raws:
    need = set()
    for m, main in MULTI:
        need.add(main)
        need |= set(re.findall(r"src:([A-Za-z][\w.-]*):\d", open(mod(m), encoding="utf-8").read()))
    for stem in sorted(need):
        hits = glob.glob(os.path.join(SUBJ, "*", "registers", "source-bundle", stem + ".txt"))
        assert len(hits) == 1, (stem, hits)
        os.symlink(hits[0], os.path.join(raws, stem + ".txt"))
    for m, main in MULTI:
        rc, line = run(os.path.join(raws, main + ".txt"), [mod(m)])
        print("%-22s %s" % (m, line))
        add(line, rc)

n = 0
inst = [0, 0, 0, 0]
for m, d, i in INSTR:
    before = list(tot)
    rc, line = run(os.path.join(SUBJ, d, "registers", "source-bundle", i + ".txt"), [mod(m)])
    add(line, rc)
    n += 1
    for k in range(4):
        inst[k] += tot[k] - before[k]
print("%d other instrument modules: %d src lines, %d runs, %d locators, %d problems" % ((n,) + tuple(inst)))
print("TOTAL: %d src lines, %d runs, %d locators, %d problems; groups with a problem: %d" % (tot[0], tot[1], tot[2], tot[3], bad))
sys.exit(1 if bad or tot[3] else 0)
