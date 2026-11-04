#!/usr/bin/env python3
"""qx.py: expand `--@Q` macros into quotation lines copied out of a deposited text (a tool, not law).

usage: python3 -I qx.py IN.l4 OUT.l4               (RAW is ../../registers/source-bundle/BA1994.txt)
       python3 -I qx.py --raw ID IN.l4 OUT.l4        (RAW is the deposit of instrument ID, e.g. BA1994-RG3; locators are plain src:N)

A macro line:   --@Q 1033-1035,1038 | s 8(1)
  becomes       -- src:1033 | A person must not provide any licensable broadcasting
                -- src:1034 | ...
                @ref s 8(1) (src:1033-1038)
The quote lines are the raw lines named, with whitespace squeezed to single spaces and NFC (as srcrefs.py quote does);
blank lines, page furniture and amendment notes "[Act 38 of 2022 wef ...]" are left out (srcrefs allows gaps in a range).
The locator spans exactly the first and last line quoted, so `srcrefs.py check --strict` is satisfied by construction.
For an instrument, write  `--@Q 12-14 | reg 3(2) @ID`  where ID is the instrument's deposit id; its quote lines carry `src:ID:N`
and the raw file is looked up beside BA1994.txt's subject as ../../../<slug>/registers/source-bundle/ID.txt via INSTR.
The macro line is replaced by the quote lines and the @ref; nothing else in the file is touched.
"""
import re, sys, unicodedata, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(HERE, "..", "..", "registers", "source-bundle")
SUBJ = os.path.join(HERE, "..", "..", "..")
FURN = [
    re.compile(r"^\s*Informal Consolidation . version in force from"),
    re.compile(r"^\s*\d+\s+Broadcasting Act 1994\s+2020 Ed\.\s*$"),
    re.compile(r"^\s*2020 Ed\.\s+Broadcasting Act 1994\s+\d+\s*$"),
]
ANNOT = re.compile(r"^\s*\[(Act \d+ of \d{4}|S \d+/\d{4}|G\.N\.|\d+/\d{4}|Deleted)[^\]]*\]\s*$")


def norm(s):
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", s)).strip()


def load(path):
    t = open(path, encoding="utf-8").read().split("\n")
    if t and t[-1] == "":
        t.pop()
    return t


def instr_path(ident):
    # find the deposit of an instrument by id
    for d in os.listdir(SUBJ):
        p = os.path.join(SUBJ, d, "registers", "source-bundle", ident + ".txt")
        if os.path.exists(p):
            return p
    raise SystemExit("no deposit for " + ident)


def expand(src, raws):
    out = []
    for ln in src.split("\n"):
        m = re.match(r"^--@Q\s+([0-9,\- ]+?)\s*\|\s*(.*?)\s*(?:@([A-Za-z0-9][\w.\-]*))?\s*$", ln)
        if not m:
            out.append(ln)
            continue
        spec, cite, ident = m.group(1), m.group(2), m.group(3)
        L = raws[ident or ""]
        lines = []
        for part in spec.split(","):
            part = part.strip()
            a, _, b = part.partition("-")
            a = int(a)
            b = int(b) if b else a
            for n in range(a, b + 1):
                if n < 1 or n > len(L):
                    raise SystemExit("line %d outside %s" % (n, ident or "BA1994"))
                raw = L[n - 1]
                if not raw.strip() or any(p.match(raw) for p in FURN) or ANNOT.match(raw):
                    continue
                lines.append((n, norm(raw)))
        if not lines:
            raise SystemExit("macro quotes nothing: " + ln)
        pre = "src:" + (ident + ":" if ident else "")
        for n, t in lines:
            out.append("-- %s%d | %s" % (pre, n, t))
        lo, hi = lines[0][0], lines[-1][0]
        loc = "%s%d" % (pre, lo) if lo == hi else "%s%d-%d" % (pre, lo, hi)
        out.append("@ref %s (%s)" % (cite, loc))
    return "\n".join(out)


def main():
    a = sys.argv[1:]
    if a[0] == "--raw":
        raws = {"": load(instr_path(a[1]))}
        a = a[2:]
    else:
        raws = {"": load(os.path.join(SB, "BA1994.txt"))}
    inp, outp = a[0], a[1]
    src = open(inp, encoding="utf-8").read()
    for ident in set(re.findall(r"^--@Q\s+[0-9,\- ]+?\s*\|.*?@([A-Za-z0-9][\w.\-]*)\s*$", src, flags=re.M)):
        raws[ident] = load(instr_path(ident))
    open(outp, "w", encoding="utf-8").write(expand(src, raws))


if __name__ == "__main__":
    main()
