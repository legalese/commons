#!/usr/bin/env python3
"""Check and print the Jural relations table.

usage:  python3 -I jural.py check    every layer-1 function is matched by a row, every row matches a function, and every function is named in a test or a case
        python3 -I jural.py table    print the table as markdown
A key that begins with ~ names a provision that is not encoded (machinery, inert reason 2) and is not checked against the functions.
A row's keys are section tags, such as `s 3(2)`; a function matches a row when the function's section tag
equals a key or lies below it (`s 3(2)(a)` lies below `s 3(2)`).
"""
import re, sys, os, glob

def functions(folder):
    out = []
    for f in sorted(glob.glob(os.path.join(folder, "eca-*.l4"))):
        b = os.path.basename(f)
        if re.match(r"eca-(tests|cases|seat)", b) or b == "eca-nouns.l4":
            continue
        for l in open(f, encoding="utf-8"):
            m = re.match(r"^`([^`]+)` MEANS", l)
            if m:
                out.append((b, m.group(1)))
    return out

def tags_of(name):
    """The section tags a function name carries; `s 5(1) to (3)` carries s 5(1), s 5(2) and s 5(3)."""
    m = re.match(r"^((?:s|sch) \d+[A-Z]?)\((\d+)\) (to|and) \((\d+)\)", name)
    if m:
        a, b = int(m.group(2)), int(m.group(4))
        return [f"{m.group(1)}({n})" for n in range(a, b + 1)]
    m = re.match(r"^((?:s|sch) \d+[A-Z]?(?:\([A-Za-z0-9]+\))*)", name)
    return [m.group(1)] if m else []

def load(folder):
    rows = []
    for l in open(os.path.join(folder, "jural-relations.tsv"), encoding="utf-8").read().split("\n"):
        if not l.strip() or l.startswith("#"):
            continue
        p = l.split("\t")
        rows.append(p)
    return rows

def below(tag, key):
    return tag == key or tag.startswith(key + "(") or (key.startswith("sch ") and tag.startswith(key))

def check(folder):
    fs = functions(folder)
    rows = load(folder)
    keys = [(i, k.strip()) for i, r in enumerate(rows) for k in r[0].split(",") if not k.strip().startswith("~")]
    miss = []
    for b, n in fs:
        ts = tags_of(n)
        if not ts or not all(any(below(t, k) for _, k in keys) for t in ts):
            miss.append((b, n))
    unused = [k for _, k in keys if not any(below(t, k) for _, n in fs for t in tags_of(n))]
    tests = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(folder, "eca-tests-*.l4")) + [os.path.join(folder, "eca-cases-seat.l4")])
    unused_fn = [(b, n) for b, n in fs if "`" + n + "`" not in tests]
    for b, n in unused_fn:
        print("FUNCTION NEVER USED in a test or a case:", b, n)
    for b, n in miss:
        print("NO ROW for", b, n)
    for k in unused:
        print("ROW KEY matches no function:", k)
    print(f"{len(fs)} functions, {len(rows)} rows, {len(keys)} keys; {len(miss)} functions without a row; {len(unused)} keys matching no function; {len(unused_fn)} functions not named in any test or case")
    return 1 if (miss or unused or unused_fn) else 0

def table(folder):
    print("| Provision | Holder | Kind | Bearer | How it is encoded |")
    print("| --- | --- | --- | --- | --- |")
    for r in load(folder):
        r = [r[0].replace("~", "")] + r[1:]
        print("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 1 and sys.argv[1] == "table":
        table(here)
    else:
        sys.exit(check(here))
