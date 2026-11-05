#!/usr/bin/env python3
"""Check that the seat layer restates no rule.

usage:  python3 -I seatcheck.py

Every DECIDE in eca-seat.l4 must (1) call at least one layer-1 function (a backticked name that begins `s N` or `sch N`)
and (2) contain none of the words that would make it a rule of its own.
It also checks that every input has an @desc, that every DECIDE has a case in eca-cases-seat.l4 and that every @export has a DECIDE.
Exit status 1 on any finding.
"""
import re, os, sys

here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, "eca-seat.l4"), encoding="utf-8").read()
cases = open(os.path.join(here, "eca-cases-seat.l4"), encoding="utf-8").read()
blocks = re.split(r"(?m)^(?=DECIDE `)", t)
n = 0
bad = []
for b in blocks:
    m = re.match(r"DECIDE `([^`]+)` IS\s*(.*?)(?:\n\s*\n|\Z)", b, re.S)
    if not m:
        continue
    n += 1
    name, body = m.group(1), m.group(2)
    code = "\n".join(l.split("--")[0] for l in body.split("\n"))
    if not re.findall(r"`((?:s|sch) \d[^`]*)`", code):
        bad.append(f"{name}: no layer-1 call")
    ops = re.findall(r"\b(AND|OR|NOT|IF|THEN|BRANCH|CONSIDER|GREATER|LESS|PLUS|MINUS|WHERE)\b", code)
    if ops:
        bad.append(f"{name}: contains {sorted(set(ops))}")
    if f"#ASSERT `{name}`" not in cases:
        bad.append(f"{name}: no case")
# every input line of every question carries an @desc
for b in re.findall(r"(?m)^@export .*\n((?:(?:GIVEN|      ).*\n)+?)GIVETH", t):
    for l in b.rstrip("\n").split("\n"):
        if "@desc" not in l:
            bad.append("input without @desc: " + l.strip()[:80])
exports = len(re.findall(r"(?m)^@export ", t))
if exports != n:
    bad.append(f"{exports} @export lines but {n} DECIDEs")
for x in bad:
    print("FINDING", x)
print(f"seatcheck: {n} questions, {exports} @export lines, {len(bad)} findings")
sys.exit(1 if bad else 0)
