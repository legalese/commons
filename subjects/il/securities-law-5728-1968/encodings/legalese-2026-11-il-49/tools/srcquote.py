#!/usr/bin/env python3
# Copied from the income-tax-ordinance-new-version subject's row il-03 (tools/srcquote.py, 2026-10-06), with one change for row il-49 (2026-11-10): the deposit is an EXCERPT of the
# Hebrew Wikisource page, so `--@SRC N` names the line number N of the WHOLE page, which the excerpt's `#### whole-page lines A-B` marker lines map back to the copied text.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki text.

A line   `<indent>--@SRC 4351`      or `<indent>--@SRC 4351-4353`
or a previously expanded line `<indent>-- src:4351 | ...`
becomes one comment line per source line:
         `<indent>-- src:4351 | (1) על כל שקל חדש ...`

Templates are reduced mechanically: subsection labels kept, link templates reduced to their
visible text, editorial notes kept and marked [note: ...]. Nothing is typed by hand.

Usage: srcquote.py SOURCE.wiki.excerpt.txt FILE.l4 [FILE.l4 ...]
N is a whole-page line number; a number the excerpt does not hold stops the run.
"""
import re
import sys

src_path, files = sys.argv[1], sys.argv[2:]
SRC = {}
_cur = None
with open(src_path, encoding="utf-8") as fh:
    for _ln in fh.read().split("\n"):
        _m = re.match(r"^#### whole-page lines (\d+)-(\d+)$", _ln)
        if _m:
            _cur = int(_m.group(1))
            continue
        if _ln.startswith("#%") or _cur is None:
            continue
        SRC[_cur] = _ln
        _cur += 1

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
                sys.exit(f"whole-page line {n} is not in the excerpt (in {path})")
            text = clean(SRC[n])
            if text:
                out.append(f"{indent}-- src:{n} | {text}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
