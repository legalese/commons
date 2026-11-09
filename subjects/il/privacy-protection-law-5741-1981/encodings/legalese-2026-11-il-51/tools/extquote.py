#!/usr/bin/env python3
# Adapted for row il-51 (2026-11-10) from the il-48 copy: TAGS lists the consolidations deposited in this subject's source-bundle, three of them as EXCERPTS
# (the Law and two sets of regulations: a header gives the original line numbers, and a tag cites the ORIGINAL line number of the whole page),
# and, read in place and not copied, the Interpretation Law consolidation held in its own subject.
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
SUBJECTS = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
TAGS = {
    "law": os.path.join(SB, "excerpts", "privacy-protection-law-5741-1981.he.wiki.excerpt.txt"),
    "eea": os.path.join(SB, "excerpts", "eea-regulations-5783-2023.he.wiki.excerpt.txt"),
    "pb": os.path.join(SB, "excerpts", "public-bodies-regulations-5746-1986.he.wiki.excerpt.txt"),
    "inspect": os.path.join(SB, "inspection-regulations-5741-1981.he.wiki.txt"),
    "abroad": os.path.join(SB, "transfer-abroad-regulations-5761-2001.he.wiki.txt"),
    "fine": os.path.join(SB, "fixed-fine-regulations-5764-2004.he.wiki.txt"),
    "interp": os.path.join(SUBJECTS, "interpretation-law-1981", "source", "law.wiki"),
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
    prev = None
    while prev != line:
        prev = line
        line = INNER.sub(reduce_template, line)
    line = re.sub(r"<[^>]+>", " ", line)
    return re.sub(r"\s+", " ", line).strip()


def lines_of(tag):
    """A list of lines for a whole page; for an EXCERPT, a dict from the original line number to the line."""
    if tag not in SRC:
        with open(TAGS[tag], encoding="utf-8") as fh:
            raw = fh.read().split("\n")
        if raw and raw[0].startswith("# EXCERPT"):
            spec = [l for l in raw if l.startswith("# original-lines:")][0].split(":", 1)[1].strip()
            nums = []
            for part in spec.split(","):
                lo, _, hi = part.partition("-")
                nums += list(range(int(lo), int(hi or lo) + 1))
            body = [l for l in raw if not l.startswith("#")]
            while body and body[-1] == "":
                body.pop()
            assert len(body) == len(nums), (tag, len(body), len(nums))
            SRC[tag] = dict(zip(nums, body))
        else:
            SRC[tag] = {i + 1: l for i, l in enumerate(raw)}
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
            if n not in lines_of(tag):
                print(f"{path}: {tag} line {n} is not in the deposit")
                bad += 1
                continue
            text = clean(lines_of(tag)[n])
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
