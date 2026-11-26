#!/usr/bin/env python3
# notes/run-summary.py FILE [--traces] -- runs the main build on FILE and prints: the four counts, each error or failed assertion with
# its line and source text, and (with --traces) each #TRACE result next to the line of the directive.  P2's helper; reads diagnostics, not exit codes.
import os
import re, subprocess, sys
L4 = os.environ.get("L4", "l4")
f = sys.argv[1]; traces = "--traces" in sys.argv
out = subprocess.run([L4, "run", f], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env={k: v for k, v in __import__("os").environ.items() if k != "JL4_LIBRARY_PATH"}).stdout
src = open(f, encoding="utf-8").read().split("\n")
blocks = re.split(r"(?m)^File:\s+", out)
seen = set(); ok = bad = ref = err = 0
for b in blocks[1:]:
    rng = re.search(r"Range:\s+(\d+):(\d+)-(\d+):(\d+)", b)
    sev = re.search(r"Severity:\s+(\S+)", b); code = re.search(r"Code:\s+(\S+)", b)
    msg = b.split("Message:", 1)[1].strip() if "Message:" in b else ""
    line = int(rng.group(1)) if rng else 0
    key = (line, code.group(1) if code else "", msg[:60])
    if key in seen: continue
    seen.add(key)
    c = code.group(1) if code else ""
    if c == "eval/assertion-passed": ok += 1
    elif "assertion" in c and "fail" in c or "could not be evaluated" in msg:
        bad += 1; err += 1; print("FAILED line %d: %s\n    %s" % (line, src[line-1][:260], msg[:200].replace("\n", " ")))
    elif "refused" in c: ref += 1; print("REFUSED line %d: %s" % (line, src[line-1][:200]))
    elif sev and sev.group(1) == "DiagnosticSeverity_Error":
        err += 1; print("ERROR line %d [%s]: %s" % (line, c, " ".join(msg.split())[:400]))
    elif c == "eval/result" and traces:
        print("TRACE line %d: %s\n    -> %s" % (line, src[line-1][:150], " ".join(msg.split())[:230]))
print("errors %d, satisfied %d, failed %d, refused %d" % (err, ok, bad, ref))
