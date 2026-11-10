#!/usr/bin/env python3
# Adapted for row il-78 (2026-11-10) from the srcquote.py of row il-71, which was adapted from row il-67 and, before it, row il-45.
# One change in this copy: TWO deposited excerpts are read, each named by a tag on the command line (TAG=EXCERPT), because both excerpts of this row
# hold a line 5 and an untagged number would be ambiguous. A marker names its tag: `--@SRC regs 158` becomes `-- src:regs:158 | ...`.
# The tag form follows row il-55's srcquote.py; the excerpt format (a `# lines copied, by line number ...` header, then `# ---`) is il-71's.
# Everything else is the il-71 copy, unchanged. The template reducer below is copied unchanged from il-45.
"""Expand source-quotation markers in .l4 files, in place, from the deposited excerpts of the consolidations.

A line   `<indent>--@SRC regs 158`      or `<indent>--@SRC regs 114-117`
or a previously expanded line `<indent>-- src:regs:158 | ...`
becomes one comment line per source line:
         `<indent>-- src:regs:158 | ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their visible text,
editorial notes kept and marked [note: ...]. Nothing is typed by hand.
A line number the named excerpt does not hold is an error, and so is a tag no excerpt carries.

Usage: srcquote.py TAG=EXCERPT.he.wiki.excerpt.txt [TAG=EXCERPT ...] FILE.l4 [FILE.l4 ...]        expand in place
       srcquote.py --check TAG=EXCERPT [TAG=EXCERPT ...] FILE.l4 [...]                            exit 1 if any src line differs from its source
A number N in a marker is the line number in the WHOLE page, which the header of the excerpt lists.
"""
import os
import re
import sys

args = sys.argv[1:]
check = False
if args and args[0] == "--check":
    check = True
    args = args[1:]


def load(path):
    with open(path, encoding="utf-8") as fh:
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
        sys.exit(f"srcquote.py: the excerpt {path} header lists {len(nums)} lines and the body holds {len(body)}")
    return dict(zip(nums, body))


SOURCES = {}
files = []
for a in args:
    if "=" in a and not os.path.exists(a):
        tag, p = a.split("=", 1)
        SOURCES[tag] = load(p)
    else:
        files.append(a)
if not SOURCES or not files:
    sys.exit("usage: srcquote.py [--check] TAG=EXCERPT [TAG=EXCERPT ...] FILE.l4 [FILE.l4 ...]")

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


MARK = re.compile(r"^(\s*)--(?:@SRC ([a-z]+) |\s*src:([a-z]+):)(\d+)(?:-(\d+))?(?:\s*\|.*)?$")
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
        indent, tag = m.group(1), (m.group(2) or m.group(3))
        a, b = int(m.group(4)), int(m.group(5) or m.group(4))
        if tag not in SOURCES:
            sys.exit(f"srcquote.py: no excerpt is tagged {tag!r} (in {path})")
        for n in range(a, b + 1):
            if n not in SOURCES[tag]:
                sys.exit(f"srcquote.py: line {n} is not in the excerpt tagged {tag!r} ({path})")
            text = clean(SOURCES[tag][n])
            if text:
                out.append(f"{indent}-- src:{tag}:{n} | {text}")
    if check:
        if out != lines:
            bad += 1
            print(f"{path}: a src line differs from its excerpt (or a marker is unexpanded)")
    else:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
