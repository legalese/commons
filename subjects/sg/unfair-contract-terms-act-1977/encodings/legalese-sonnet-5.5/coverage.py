#!/usr/bin/env python3
"""Coverage audit for the UCTA encoding.

usage: python3 -I coverage.py RAW_TEXT coverage-rows.tsv [--md]

Reads the rows (id, lines, unit, label, disposition, where, fork) and the raw text, and checks:
  * every non-blank line of the raw text falls inside at least one row's line ranges;
  * every row has exactly one disposition: encoded, inert, fork or repealed-or-blank;
  * an `inert` row names its reason as "inert reason 1", "inert reason 2" or "inert reason 3";
  * an `encoded` or `fork` row names `file.l4::function name`, the file exists beside the TSV, and the
    function name appears in that file between backticks;
  * a `fork` row names at least one fork id (F1 ...) and an `encoded` row names none;
  * if NOTES.md is beside the TSV, every fork id used has an entry "**Fn**" in it.
Prints the counts, then (with --md) the table as markdown.  Exit status 1 on any problem.
"""
import sys, os, re

def parse_ranges(s):
    out = []
    for part in s.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.append((int(a), int(b)))
        else:
            out.append((int(part), int(part)))
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    md = "--md" in sys.argv
    raw, tsv = args[0], args[1]
    here = os.path.dirname(os.path.abspath(tsv))
    text = open(raw, encoding="utf-8").read().split("\n")
    rows = []
    for i, ln in enumerate(open(tsv, encoding="utf-8").read().split("\n")):
        if i == 0 or not ln.strip():
            continue
        f = ln.split("\t")
        f += [""] * (7 - len(f))
        rows.append(dict(id=f[0], lines=f[1], unit=f[2], label=f[3], disp=f[4], where=f[5], fork=f[6]))
    problems = []
    covered = set()
    cache = {}
    for r in rows:
        for a, b in parse_ranges(r["lines"]):
            for n in range(a, b + 1):
                covered.add(n)
        d = r["disp"]
        if d not in ("encoded", "inert", "fork", "repealed-or-blank"):
            problems.append(f'{r["id"]}: unknown disposition {d!r}')
        if d == "inert" and not re.fullmatch(r"inert reason [123]", r["where"]):
            problems.append(f'{r["id"]}: inert row needs "inert reason 1|2|3", has {r["where"]!r}')
        if d == "repealed-or-blank" and not r["where"].startswith("the text shows"):
            problems.append(f'{r["id"]}: repealed-or-blank row must say what the text shows')
        if d in ("encoded", "fork"):
            if "::" not in r["where"]:
                problems.append(f'{r["id"]}: {d} row needs file::function')
            else:
                fn, name = r["where"].split("::", 1)
                p = os.path.join(here, fn)
                if not os.path.exists(p):
                    problems.append(f'{r["id"]}: no file {fn}')
                else:
                    if p not in cache:
                        cache[p] = open(p, encoding="utf-8").read()
                    if "`" + name + "`" not in cache[p]:
                        problems.append(f'{r["id"]}: `{name}` not found in {fn}')
        if d == "fork" and not re.fullmatch(r"F\d+(,F\d+)*", r["fork"]):
            problems.append(f'{r["id"]}: fork row needs fork ids')
        if d == "encoded" and r["fork"]:
            problems.append(f'{r["id"]}: encoded row must not name a fork')
    notes = os.path.join(here, "NOTES.md")
    if os.path.exists(notes):
        nt = open(notes, encoding="utf-8").read()
        ids = sorted({x for r in rows for x in r["fork"].split(",") if x})
        for x in ids:
            if "**" + x + "**" not in nt:
                problems.append(f"fork {x} is named in the table but has no entry in NOTES.md")
    uncovered = [n for n, ln in enumerate(text, 1) if ln.strip() and n not in covered]
    nonblank = sum(1 for ln in text if ln.strip())
    counts = {}
    for r in rows:
        counts[r["disp"]] = counts.get(r["disp"], 0) + 1
    reasons = {}
    for r in rows:
        if r["disp"] == "inert":
            reasons[r["where"]] = reasons.get(r["where"], 0) + 1
    print(f"rows: {len(rows)}")
    for k in ("encoded", "fork", "inert", "repealed-or-blank"):
        print(f"  {k}: {counts.get(k, 0)}")
    for k in sorted(reasons):
        print(f"    {k}: {reasons[k]}")
    print(f"non-blank text lines: {nonblank}; not in any row: {len(uncovered)}")
    if uncovered:
        print("  uncovered lines: " + ", ".join(f"{n}: {text[n-1].strip()[:50]}" for n in uncovered[:60]))
    for p in problems:
        print("PROBLEM " + p)
    if md:
        print()
        print("| id | lines | unit | provision | disposition | where | fork |")
        print("|---|---|---|---|---|---|---|")
        for r in rows:
            w = r["where"].replace("|", "\\|")
            print(f'| {r["id"]} | {r["lines"]} | {r["unit"]} | {r["label"]} | {r["disp"]} | {w} | {r["fork"]} |')
    sys.exit(1 if (problems or uncovered) else 0)

main()
