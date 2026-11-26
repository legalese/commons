#!/usr/bin/env python3
# notes/trace-view.py FILE... -- prints, for every #TRACE of each file, the comment line above it (the expected result) and the result the main build gives.
import re, subprocess, sys, os
L4 = os.environ.get("L4", "l4")
env = {k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"}
for f in sys.argv[1:]:
    out = subprocess.run([L4, "run", f], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env).stdout
    src = open(f, encoding="utf-8").read().split("\n")
    res = {}
    for b in re.split(r"(?m)^File:\s+", out)[1:]:
        if "eval/result" not in b: continue
        rng = re.search(r"Range:\s+(\d+):", b)
        msg = " ".join(b.split("Message:", 1)[1].split())
        res.setdefault(int(rng.group(1)), msg)
    for ln in sorted(res):
        why = src[ln - 2] if ln >= 2 else ""
        r = res[ln]
        r = re.sub(r"DEONTIC BREACHED: BREACH BY controller BECAUSE .*", "BREACH", r)
        r = re.sub(r"DEONTIC BREACHED: party controller who did action .*", "BREACH (act)", r)
        r = re.sub(r"PARTY controller (MUST|MUST NOT) .*", "STANDING: " + r[:60], r)
        print("%s:%d  %s\n      => %s" % (os.path.basename(f), ln, why.strip()[:150], r[:90]))
