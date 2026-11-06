#!/usr/bin/env python3
"""Check every #TRACE in this encoding against the outcome written beside it.

check.sh counts error diagnostics and assertion lines, and a #TRACE prints neither, so a trace whose
outcome is wrong (or differs between two builds) moves no count there.  A DEONTIC value cannot be
the operand of #ASSERT on a main build, so this script is where the traces are held to account:

  * the line before each #TRACE must be  `-- TRACE-EXPECT: FULFILLED | BREACH | RESIDUAL  (why)`
    written from the text before the trace was run;
  * the file is run with L4 and with L4_MAIN, and each build's outcome for that trace must equal the expectation.

  L4=<l4> L4_MAIN=<another main l4> python3 -I trace-check.py [DIR]

Exit status 1 on any mismatch or any #TRACE without an expectation.
"""
import os, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
d = sys.argv[1] if len(sys.argv) > 1 else here
bins = [("L4", os.environ.get("L4", "l4")), ("L4_MAIN", os.environ.get("L4_MAIN", ""))]
bins = [(k, v) for k, v in bins if v]

def outcomes(binary, path):
    env = dict(os.environ); env.pop("JL4_LIBRARY_PATH", None)
    out = subprocess.run([binary, "run", os.path.basename(path)], cwd=os.path.dirname(path), env=env,
                         capture_output=True, text=True).stdout
    res = {}
    for m in re.finditer(r"^Evaluation\[\d+\] @ [^:]+:(\d+):[^\n]*\n\nResult:\n(.*?)\n\n\nTrace:", out, re.S | re.M):
        line, body = int(m.group(1)), m.group(2)
        if "DEONTIC BREACHED" in body: kind = "BREACH"
        elif body.strip() == "FULFILLED": kind = "FULFILLED"
        else: kind = "RESIDUAL"
        res[line] = kind
    return res

total = bad = 0
for name in sorted(os.listdir(d)):
    if not name.endswith(".l4"): continue
    path = os.path.join(d, name)
    lines = open(path, encoding="utf-8").read().split("\n")
    traces = [(i + 1) for i, l in enumerate(lines) if l.startswith("#TRACE")]
    if not traces: continue
    exp = {}
    for ln in traces:
        j = ln - 2
        while j >= 0 and lines[j].strip() == "": j -= 1
        m = re.match(r"-- TRACE-EXPECT: (FULFILLED|BREACH|RESIDUAL)\b", lines[j]) if j >= 0 else None
        if not m:
            print(f"{name}:{ln}: #TRACE with no `-- TRACE-EXPECT:` line above it"); bad += 1; continue
        exp[ln] = m.group(1)
    for label, binary in bins:
        got = outcomes(binary, path)
        for ln, want in exp.items():
            total += 1
            g = got.get(ln, "NO-RESULT")
            if g != want:
                bad += 1
                print(f"{name}:{ln}: {label} printed {g}, expected {want}")
print(f"trace-check: {len(bins)} build(s), {total} trace outcome(s) checked, {bad} problem(s)")
sys.exit(1 if bad else 0)
