#!/usr/bin/env python3
# Copied from the income-tax-ordinance-new-version subject's row il-03 (tools/srcquote.py, 2026-10-06), changed for row il-49 (2026-11-10): the Law's deposit is an EXCERPT of the
# Hebrew Wikisource page, so a number N names the line N of the WHOLE page, which the excerpt's `#### whole-page lines A-B` marker lines map back to the copied text.
# Changed again for row il-55 (2026-11-10): more than one deposited source. A marker may name a TAG (`--@SRC proc 18`); an untagged marker reads the Law's excerpt.
"""Expand source-quotation markers in .l4 files, in place, from the deposited wiki texts.

A line   `<indent>--@SRC 4351`, `<indent>--@SRC 4351-4353`, or `<indent>--@SRC proc 18`
or a previously expanded line `<indent>-- src:4351 | ...` or `<indent>-- src:proc:18 | ...`
becomes one comment line per source line:
         `<indent>-- src:4351 | (1) על כל שקל חדש ...`        (the Law)
         `<indent>-- src:proc:18 | ...`                        (the source tagged proc)

Templates are reduced mechanically: subsection labels kept, link templates reduced to their
visible text, editorial notes kept and marked [note: ...]. Nothing is typed by hand.

Usage: srcquote.py LAW-SOURCE [TAG=SOURCE ...] FILE.l4 [FILE.l4 ...]
LAW-SOURCE is read by an untagged marker; each TAG=SOURCE argument adds a source for the markers that name TAG.
A source that holds `#### whole-page lines A-B` marker lines is an excerpt and N is a whole-page line number; a source with no such line is a whole page and N is its line number counted from 1.
A number the source does not hold stops the run.
"""
import os
import re
import sys


def load(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = {}
    if any(re.match(r"^#### whole-page lines (\d+)-(\d+)$", ln) for ln in lines):
        cur = None
        for ln in lines:
            m = re.match(r"^#### whole-page lines (\d+)-(\d+)$", ln)
            if m:
                cur = int(m.group(1))
                continue
            if ln.startswith("#%") or cur is None:
                continue
            out[cur] = ln
            cur += 1
    else:
        for n, ln in enumerate(lines, 1):
            out[n] = ln
    return out


SOURCES = {"": load(sys.argv[1])}
files = []
for a in sys.argv[2:]:
    if "=" in a and not os.path.exists(a):
        tag, p = a.split("=", 1)
        SOURCES[tag] = load(p)
    else:
        files.append(a)

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


MARK = re.compile(r"^(\s*)--(?:@SRC (?:([a-z]+) )?|\s*src:(?:([a-z]+):)?)(\d+)(?:-(\d+))?(?:\s*\|.*)?$")

for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    for ln in lines:
        m = MARK.match(ln)
        if not m:
            out.append(ln)
            continue
        indent, tag = m.group(1), (m.group(2) or m.group(3) or "")
        a, b = int(m.group(4)), int(m.group(5) or m.group(4))
        if tag not in SOURCES:
            sys.exit(f"no source is tagged {tag!r} (in {path})")
        for n in range(a, b + 1):
            if n not in SOURCES[tag]:
                sys.exit(f"line {n} is not in the source tagged {tag!r} (in {path})")
            text = clean(SOURCES[tag][n])
            if text:
                out.append(f"{indent}-- src:{tag + ':' if tag else ''}{n} | {text}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
