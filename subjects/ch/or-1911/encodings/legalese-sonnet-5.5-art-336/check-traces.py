#!/usr/bin/env python3
"""Compare the printed outcome of every #TRACE in a module with the
`-- EXPECT:` comment written on the line above it, with each stable build.

check.sh counts assertion lines and a #TRACE prints none, so this is the
check that exercises the regulative rules.

  L4=<l4 binary> L4_MAIN=<second stable l4 binary> python3 -I check-traces.py [FILE...]

Default FILE: or336-traces.l4 beside this script.  Exit 0 only when every
trace agrees with its expectation on both builds.  Expectations:
  FULFILLED  the printed value is FULFILLED
  BREACH     the printed value starts with DEONTIC BREACHED
  RESIDUAL   the printed value is an obligation still standing (starts with PARTY)
"""
import json, os, re, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
EXPECT = re.compile(r"^\s*--\s*EXPECT:\s*(FULFILLED|BREACH|RESIDUAL)\s*$")

def classify(value: str) -> str:
    v = value.strip()
    if v == "FULFILLED":
        return "FULFILLED"
    if v.startswith("DEONTIC BREACHED"):
        return "BREACH"
    if v.startswith("PARTY"):
        return "RESIDUAL"
    return "OTHER:" + v[:60].replace("\n", " ")

def expectations(path):
    """line number of each #TRACE -> expectation written on the line above it."""
    exp, prev = {}, None
    for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        m = EXPECT.match(line)
        if m:
            prev = m.group(1)
            continue
        if line.startswith("#TRACE"):
            exp[i] = prev
            prev = None
        elif line.strip() and not line.strip().startswith("--"):
            prev = None
    return exp

def run(binary, path):
    env = {k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"}
    p = subprocess.run([binary, "run", path.name, "--json"], cwd=path.parent, env=env,
                       capture_output=True, text=True)
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return None

def main():
    files = [pathlib.Path(a).resolve() for a in sys.argv[1:]] or [HERE / "or336-traces.l4"]
    builds = [("L4", os.environ.get("L4", "l4")), ("L4_MAIN", os.environ.get("L4_MAIN", ""))]
    builds = [(n, b) for n, b in builds if b]
    bad = total = 0
    for f in files:
        exp = expectations(f)
        for name, binary in builds:
            data = run(binary, f)
            if data is None:
                print(f"{f.name} [{name}]: no JSON from {binary}")
                bad += 1
                continue
            res = {}
            for r in data.get("results", []):
                m = re.match(r".*:(\d+):\d+-", r["range"])
                if m:
                    res[int(m.group(1))] = classify(str(r.get("value", "")))
            for line, want in sorted(exp.items()):
                total += 1
                got = res.get(line)
                if want is None:
                    print(f"{f.name}:{line} [{name}]: no EXPECT comment above this #TRACE")
                    bad += 1
                elif got != want:
                    print(f"{f.name}:{line} [{name}]: expected {want}, printed {got}")
                    bad += 1
    print(f"check-traces: {total} trace checks ({len(exp)} traces x {len(builds)} builds), {bad} problems")
    sys.exit(1 if bad else 0)

main()
