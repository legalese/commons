#!/usr/bin/env python3
"""check-traces.py L4_BINARY FILE.l4...

`l4 run` prints the result of a #TRACE but never counts it as an assertion, and a DEONTIC cannot be compared with
EQUALS on the stable binary. So the expected outcome of every #TRACE is written in a comment on the line above it:

    -- TRACE-EXPECT: FULFILLED | BREACH | STANDING

(FULFILLED = the result is FULFILLED; BREACH = it begins DEONTIC BREACHED; STANDING = a residual obligation is printed back.)
The expectation is written from the text before the run. This script runs each file with the binary it is given and
compares each #TRACE with its expectation; it prints one line per file and exits 1 on any mismatch, any #TRACE without
an expectation, or any file that printed nothing it recognises (a run that did not happen must not read as a pass)."""
import re, subprocess, sys
l4 = sys.argv[1]; bad = 0; total = 0
for path in sys.argv[2:]:
    src = open(path, encoding="utf-8").read().split("\n")
    traces = {}   # line number of #TRACE -> expected
    for i, line in enumerate(src, 1):
        if line.startswith("#TRACE"):
            exp = None
            j = i - 2
            while j >= 0 and src[j].strip().startswith("--"):
                m = re.match(r"\s*-- TRACE-EXPECT: (FULFILLED|BREACH|STANDING)", src[j])
                if m: exp = m.group(1); break
                j -= 1
            traces[i] = exp
    if not traces: continue
    out = subprocess.run([l4, "run", path], capture_output=True, text=True, cwd=None).stdout
    if not re.search(r"^(Checking succeeded|File:|Evaluation\[)", out, re.M):
        print(f"{path}: the binary printed nothing it recognises"); bad += 1; continue
    blocks = re.split(r"(?m)^Evaluation\[\d+\] @ ", out)[1:]
    got = {}
    for b in blocks:
        m = re.match(r"\S+?:(\d+):", b)
        if not m: continue
        res = b.split("Result:", 1)[1].strip().split("\n")[0].strip() if "Result:" in b else ""
        got[int(m.group(1))] = res
    ok = 0
    for ln, exp in traces.items():
        total += 1
        if exp is None: print(f"{path}:{ln}: #TRACE without a TRACE-EXPECT comment"); bad += 1; continue
        res = got.get(ln)
        if res is None: print(f"{path}:{ln}: no result printed for the #TRACE"); bad += 1; continue
        kind = "FULFILLED" if res == "FULFILLED" else ("BREACH" if res.startswith("DEONTIC BREACHED") else ("STANDING" if res.startswith("PARTY") else "OTHER:" + res))
        if kind != exp: print(f"{path}:{ln}: expected {exp}, got {kind}"); bad += 1
        else: ok += 1
    print(f"{path}: {ok} of {len(traces)} traces as expected")
print(f"traces checked: {total}, mismatches: {bad}")
sys.exit(1 if bad else 0)
