#!/usr/bin/env python3
# Row il-78 (2026-11-10) adapted the il-71 copy in TWO ways, and left the rest unchanged:
#  (1) more than one deposited excerpt: every leading argument that ends in `.excerpt.txt` is a source, and a run of Hebrew must occur in one of them
#      (or on an `ext:` line of the checked files, see (3)); the first argument that does not end so starts the list of checked files;
#  (2) a quotation line from an excerpt may carry a tag, `-- src:regs:158 | ...` (srcquote.py of this row), and is skipped like an untagged one.
# Earlier history of this file, from the il-71 copy: the body of every `-- ext:[tag] ... | text` line in the checked files is added to the
# text a run of Hebrew is looked up in, as well as the excerpt. Reason: a typed STRING that carries words printed only on an official page
# (the words of a paragraph as an amending instrument printed it) is not in the consolidation excerpt, and the ext: line directly above it is the
# quotation of the page that it was copied from. A run outside a quotation line must therefore occur in an excerpt OR on an ext: line of the row.
# Earlier history of this file: Copied from ../../legalese-2026-10-il-06/tools/hebcheck.py on 2026-10-09 (row IL-34), with one more change: an ext: line may carry the
# source line number (`-- ext:[tag] 12 | ...`, written by extquote.py). Row il-45 adds the form `-- ext:[tag] p17:15 | ...` (page and line of a PDF text layer). Earlier history of this file:
# Copied from ../../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-03/tools/hebcheck.py on 2026-10-06,
# with one change: a line carrying `-- ext:[TAG] |` quotes a source OTHER than the Law (the
# Institute's pages, the amending Law's PDF), and is skipped like a `src:` line. Those
# quotations are listed in NOTES.md with the file each was checked against.
"""Every run of Hebrew in a .l4/.md file, outside a `src:N |` quotation line, must occur
verbatim in the source files. Prints each run that does not, with file:line. Exit 1 if any.

Usage: hebcheck.py EXCERPT.excerpt.txt [EXCERPT.excerpt.txt ...] FILE [FILE ...]

A run starts and ends on a Hebrew letter (or geresh/gershayim) and may contain spaces,
digits, Hebrew punctuation, the maqaf and the en dash in between. ASCII quotes and
brackets end a run, so a run is never padded with the encoder's own punctuation."""
import re
import sys

_args = sys.argv[1:]
_excerpts = []
while _args and _args[0].endswith(".excerpt.txt"):
    _excerpts.append(_args.pop(0))
_checked = _args
if not _excerpts or not _checked:
    sys.exit("usage: hebcheck.py EXCERPT.excerpt.txt [EXCERPT.excerpt.txt ...] FILE [FILE ...]")
_raw = "\n".join(open(_p, encoding="utf-8").read() for _p in _excerpts)
# The template reducer below is copied verbatim from srcquote.py, so the text checked
# against is exactly what the src: quotations show.
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


src = _raw + "\n" + "\n".join(clean(l) for l in _raw.split("\n"))
EXT = re.compile(r"--\s*ext:\[[^\]]+\] (?:(?:\d+|p\d+:\d+) )?\|(.*)$")
_ext_bodies = []
for _path in _checked:
    with open(_path, encoding="utf-8") as _fh:
        for _line in _fh:
            _m = EXT.search(_line.rstrip("\n"))
            if _m:
                _ext_bodies.append(_m.group(1).strip())
src = src + "\n" + "\n".join(_ext_bodies)
LETTER = "א-ת׳״"
INNER = LETTER + "־– 0-9,.;:"
HEB = re.compile(f"[{LETTER}][{INNER}]*[{LETTER}]|[{LETTER}]")
bad = 0
for path in _checked:
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if re.search(r"--\s*src:(?:[a-z]+:)?\d+ \|", line) or re.search(r"--\s*ext:\[[^\]]+\] ((\d+|p\d+:\d+) )?\|", line):
                continue
            for m in HEB.finditer(line):
                run = m.group(0).strip()
                if run not in src:
                    bad += 1
                    print(f"{path.split('/')[-1]}:{n}: NOT IN SOURCE: {run}")
sys.exit(1 if bad else 0)
