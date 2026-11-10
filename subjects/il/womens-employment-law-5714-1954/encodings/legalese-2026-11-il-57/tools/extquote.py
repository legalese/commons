#!/usr/bin/env python3
# Adapted for row il-52 (2026-11-10) from the il-48 copy: TAGS lists the National Insurance Law consolidation (tag ni), deposited in this subject's source-bundle as an excerpt whose lines carry the page's line numbers.
# Written for row IL-34 (2026-10-09). The template reducer is copied unchanged from srcquote.py in this directory.
"""Expand quotations of the instruments OTHER than the Law, in place, from their deposited wiki text.

A line   `<indent>--@EXT tag 12`      or `<indent>--@EXT tag 12-14`
or a previously expanded line `<indent>-- ext:[tag] 12 | ...`
becomes one comment line per source line:
         `<indent>-- ext:[tag] 12 | text`

(srcquote.py does the same for the Law itself, with `src:N |`; hebcheck.py skips both kinds of line.)

Usage: extquote.py FILE.l4 [FILE.l4 ...]        expand in place
       extquote.py --check FILE.l4 [...]       exit 1 if any ext: line differs from the source
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.normpath(os.path.join(HERE, "..", "..", "..", "registers", "source-bundle"))
TAGS = {
    "ni": os.path.join(SB, "national-insurance-law-5755-1995.he.wiki.excerpt.txt"),
}
SRC = {}
INNER = re.compile(r"\{\{([^{}]*)\}\}")


def reduce_template(m):
    parts = m.group(1).split("|")
    name = parts[0]
    args = [p for p in parts[1:]]
    if name in ("ח:פנימי", "ח:חיצוני"):
        return args[-1] if args else ""
    if name == "ח:הערה":
        return "[note: " + "|".join(args) + "]"
    if name.startswith("ח:ת"):  # ח:ת ח:תת ח:תתת ח:תתתת
        labels = [a for a in args if not a.startswith("סוג=")]
        return "".join(labels)
    if name == "ח:סעיף":
        num = args[0] if args else ""
        head = args[1] if len(args) > 1 else ""
        amend = [a for a in args[2:] if a.startswith("תיקון")]
        tail = (" [" + amend[0] + "]") if amend else ""
        return (f"סעיף {num} – {head}".rstrip(" –")) + tail
    if name == "ח:סעיף*":
        return ""
    if name == "ח:קטע1":
        return args[-1] if args else ""
    return m.group(0).replace("{{", "⟦").replace("}}", "⟧")


def clean(line):
    line = re.sub(r"\{\{ח:סעיף\|([^{}|]*)\|([^{}|]*)\|$", r"{{ח:סעיף|\1|\2}}", line)  # a heading line deposited only as far as its title
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


def lines_of(tag):
    if tag not in SRC:
        SRC[tag] = {}  # line number in the whole page -> line; the deposit is an excerpt, one "<number>\t<line>" per line
        with open(TAGS[tag], encoding="utf-8") as fh:
            for _ln in fh.read().split("\n"):
                _m = re.match(r"^(\d+)\t(.*)$", _ln)
                if _m:
                    SRC[tag][int(_m.group(1))] = _m.group(2)
    return SRC[tag]


MARK = re.compile(r"^(\s*)--(?:@EXT (\S+) |\s*ext:\[([^\]]+)\] )(\d+)(?:-(\d+))?(?:\s*\|.*)?$")
check = sys.argv[1] == "--check"
files = sys.argv[2:] if check else sys.argv[1:]
bad = 0
for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln in lines:
        m = MARK.match(ln)
        if not m:
            out.append(ln)
            continue
        indent, tag = m.group(1), m.group(2) or m.group(3)
        a, b = int(m.group(4)), int(m.group(5) or m.group(4))
        for n in range(a, b + 1):
            text = clean(lines_of(tag)[n])  # a KeyError means the line is not in the excerpt
            if text:
                out.append(f"{indent}-- ext:[{tag}] {n} | {text}")
    if check:
        # a check run compares only previously expanded lines, one by one
        exp = [l for l in lines if re.match(r"^\s*-- ext:\[", l)]
        got = [l for l in out if re.match(r"^\s*-- ext:\[", l)]
        for e, g in zip(exp, got):
            if e != g:
                bad += 1
                print(f"{path}: ext line differs from source: {e[:80]}")
        if len(exp) != len(got):
            bad += 1
            print(f"{path}: ext line count differs")
    else:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
