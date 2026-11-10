#!/usr/bin/env python3
# Adapted for row il-68 from the srcquote.py of row il-45. The reducer below is copied unchanged. One change: the deposit is the EXCERPT of the Hebrew Wikisource page
# (registers/source-bundle/*.he.wiki.excerpt.txt), not the whole page, so a marker `--@SRC N` names line N of the WHOLE page, and the line is found in the excerpt by the
# list of line numbers its header gives (the body lines are those lines, in order). `--check` exits 1 if any `src:N` line differs from its source line.
"""Expand or check source-quotation markers in .l4 files from the deposited excerpt.

A line   `<indent>--@SRC 4351`  or  `<indent>--@SRC 4351-4353`  or an expanded line `<indent>-- src:4351 | ...`
becomes one comment line per source line:  `<indent>-- src:4351 | (1) ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their visible text, editorial notes kept and marked [note: ...].
Nothing is typed by hand.

Usage: srcquote.py EXCERPT.txt FILE.l4 [FILE.l4 ...]          expand in place
       srcquote.py --check EXCERPT.txt FILE.l4 [FILE.l4 ...]  exit 1 if any src line differs from its source
"""
import re
import sys

args = sys.argv[1:]
CHECK = False
if args and args[0] == "--check":
    CHECK = True
    args = args[1:]
src_path, files = args[0], args[1:]
with open(src_path, encoding="utf-8") as fh:
    ALL = fh.read().split("\n")
if ALL and ALL[-1] == "":
    ALL.pop()
COMMENTS = [l for l in ALL if l.startswith("<!--")]
BODY = [l for l in ALL if not l.startswith("<!--")]
listing = [c for c in COMMENTS if "Lines copied unchanged" in c][0]
listing = listing.split(":", 1)[1].split("(numbers")[0]
NUMS = []
for a, b in re.findall(r"(\d+)(?:-(\d+))?", listing):
    NUMS.extend(range(int(a), int(b or a) + 1))
assert len(NUMS) == len(BODY), "the header lists %d lines, the excerpt holds %d" % (len(NUMS), len(BODY))
SRC = dict(zip(NUMS, BODY))
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
                print(f"{path}: line {n} of the whole page is not in the excerpt")
                bad += 1
                continue
            text = clean(SRC[n])
            if text:
                out.append(f"{indent}-- src:{n} | {text}")
    if CHECK:
        if "\n".join(out) != "\n".join(lines):
            print(f"{path}: a src line differs from its source")
            bad += 1
    else:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
sys.exit(1 if bad else 0)
