#!/usr/bin/env python3
# Adapted for row il-67 from the srcquote.py of row il-45. Two changes: the source is the EXCERPT of the consolidation, not the whole page,
# and a line number N in a marker is the line number in the whole page, which the excerpt's header lists ("lines copied, by line number ...").
# The template reducer below is copied unchanged from il-45.
"""Expand source-quotation markers in .l4 files, in place, from the deposited excerpt of the consolidation.

A line   `<indent>--@SRC 4351`      or `<indent>--@SRC 4351-4353`
or a previously expanded line `<indent>-- src:4351 | ...`
becomes one comment line per source line:
         `<indent>-- src:4351 | (1) ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their visible text,
editorial notes kept and marked [note: ...]. Nothing is typed by hand.
A line number the excerpt does not hold is an error.

Usage: srcquote.py EXCERPT.he.wiki.excerpt.txt FILE.l4 [FILE.l4 ...]        expand in place
       srcquote.py --check EXCERPT FILE.l4 [...]                            exit 1 if any src line differs from its source
"""
import re
import sys

args = sys.argv[1:]
check = False
if args and args[0] == "--check":
    check = True
    args = args[1:]
src_path, files = args[0], args[1:]
with open(src_path, encoding="utf-8") as fh:
    ALL = fh.read().split("\n")
spec = next(l for l in ALL if l.startswith("# lines copied, by line number"))
nums = []
for part in spec.split(":", 1)[1].split(","):
    part = part.strip()
    a, _, b = part.partition("-")
    nums.extend(range(int(a), int(b or a) + 1))
body = ALL[ALL.index("# ---") + 1:]
if body and body[-1] == "":
    body = body[:-1]
if len(body) != len(nums):
    sys.exit(f"srcquote.py: the excerpt header lists {len(nums)} lines and the body holds {len(body)}")
SRC = dict(zip(nums, body))

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
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(\d+)(?:-(\d+))?(?:\s*\|.*)?$")
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
        indent, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        for n in range(a, b + 1):
            if n not in SRC:
                sys.exit(f"srcquote.py: line {n} is not in the excerpt ({path})")
            text = clean(SRC[n])
            if text:
                out.append(f"{indent}-- src:{n} | {text}")
    if check:
        if out != lines:
            bad += 1
            print(f"{path}: a src line differs from the excerpt (or a marker is unexpanded)")
    else:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
