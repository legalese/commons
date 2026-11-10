#!/usr/bin/env python3
# Adapted for row il-61 (2026-11-10): two deposits, the second tagged dis:. Adapted for row il-52 (2026-11-10): the deposit is an excerpt whose lines carry the page's line numbers, so SRC is a dict and a line not deposited is a KeyError.
# Otherwise copied unchanged (below this line) from ../../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/tools/srcquote.py on 2026-10-06.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki text.

A line   `<indent>--@SRC 4351`      or `<indent>--@SRC 4351-4353`
or a previously expanded line `<indent>-- src:4351 | ...`
becomes one comment line per source line:
         `<indent>-- src:4351 | (1) על כל שקל חדש ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their
visible text, editorial notes kept and marked [note: ...]. Nothing is typed by hand.

Usage: srcquote.py LAW.excerpt.txt DISABLED-LAW.excerpt.txt FILE.l4 [FILE.l4 ...]   (a marker `--@SRC dis:153-154` reads the second deposit)
"""
import re
import sys

src_path, dis_path, files = sys.argv[1], sys.argv[2], sys.argv[3:]
SRCS = {"": {}, "dis:": {}}  # tag -> (line number in the whole page -> line); the first deposit is the excerpt of the Law's page, the second the excerpt of the Disabled Law's page, tagged dis:
for _tag, _path in (("", src_path), ("dis:", dis_path)):
    with open(_path, encoding="utf-8") as fh:
        for _ln in fh.read().split("\n"):
            _m = re.match(r"^(\d+)\t(.*)$", _ln)
            if _m:
                SRCS[_tag][int(_m.group(1))] = _m.group(2)

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


MARK = re.compile(r"^(\s*)--(?:@SRC |\s*src:)(dis:)?(\d+)(?:-(\d+))?(?:\s*\|.*)?$")

for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln in lines:
        m = MARK.match(ln)
        if not m:
            out.append(ln)
            continue
        indent, tag, a, b = m.group(1), m.group(2) or "", int(m.group(3)), int(m.group(4) or m.group(3))
        for n in range(a, b + 1):
            text = clean(SRCS[tag][n])  # a KeyError means the line is not in the excerpt
            if text:
                out.append(f"{indent}-- src:{tag}{n} | {text}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
