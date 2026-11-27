#!/usr/bin/env python3
# notes/gen-recitals.py -- writes recitals/gdpr-recitals.l4: the preamble's six citation formulae and the 173 recitals of
# Regulation (EU) 2016/679 as INERT text (the `hierarchy` library's `item` outline), from the deposited as-published text.
#
# Run:   python3 -I notes/gen-recitals.py [--out FILE] [--explain]
#   --out FILE   write FILE (default: recitals/gdpr-recitals.l4 in the encoding folder); "-" writes to stdout
#   --explain    also print, to stderr, every corrigendum correction that was applied
# Deterministic: no clock, no environment, no absolute path in its output; the same inputs give the same bytes.
# Standard library only.  Its inputs are untrusted data: run it with `python3 -I`.
#
# Source and edition.  The consolidated text of 4.5.2016 (the text the rest of this encoding quotes) has NO recitals, so
# the recitals come from the as-published text, eu-gdpr-2016-679.txt, lines 14-186 (rows `| (n) | text |`), and the one
# correction of the 2018 corrigendum that falls in the recitals (recital 71) is read from the corrigendum file and applied.
# Nothing else is changed: each recital is the text of its row, byte for byte, between the row's frame `| (n) | ` and ` |`.
#
# What it refuses (loud): a source whose sha256 is not the one its .meta.json records; a number of citations other than
# six or of recitals other than 173; a recital number out of order; a line in the recitals region that is not a row; a
# corrigendum passage that is not found exactly once in its recital; a control character in a text.
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ENC = Path(__file__).resolve().parent.parent            # the encoding folder
BUNDLE = ENC.parent.parent / "registers" / "source-bundle"
SOURCE = BUNDLE / "eu-gdpr-2016-679.txt"
CORRIGENDUM = BUNDLE / "eu-gdpr-2016-679-corrigendum-20180523.txt"
DEFAULT_OUT = ENC / "recitals" / "gdpr-recitals.l4"

# The source's own shape, pinned: if the deposit is re-rendered and these change, the generator stops.
N_CITATIONS = 6
N_RECITALS = 173
HEAD = "THE EUROPEAN PARLIAMENT AND THE COUNCIL OF THE EUROPEAN UNION,"
WHEREAS = "Whereas:"
ADOPTED = "HAVE ADOPTED THIS REGULATION:"
ROW = re.compile(r"^\| \((\d+)\) \| (.+) \|$")

# Repo-relative names, as they are written into the header of the .l4 file.
SRC_NAME = "subjects/eu/gdpr-2016-679/registers/source-bundle/eu-gdpr-2016-679.txt"
COR_NAME = "subjects/eu/gdpr-2016-679/registers/source-bundle/eu-gdpr-2016-679-corrigendum-20180523.txt"


def die(msg):
    sys.stderr.write("gen-recitals: " + msg + "\n")
    sys.exit(1)


def read_checked(path, meta_name):
    """The lines of a deposited text, after checking its sha256 against the text_sha256 of its .meta.json."""
    raw = path.read_bytes()
    want = json.loads((BUNDLE / meta_name).read_text(encoding="utf-8"))["text_sha256"]
    got = hashlib.sha256(raw).hexdigest()
    if got != want:
        die("%s has sha256 %s, but %s records %s" % (path.name, got, meta_name, want))
    return raw.decode("utf-8").split("\n")


def parse_source(lines):
    try:
        i_head = lines.index(HEAD)
        i_where = lines.index(WHEREAS)
        i_end = lines.index(ADOPTED)
    except ValueError as e:
        die("an anchor line is missing from the source: %s" % e)
    if not (i_head < i_where < i_end):
        die("the anchor lines are out of order")
    citations = lines[i_head + 1:i_where]
    if len(citations) != N_CITATIONS or any((not c) or c.startswith("| ") for c in citations):
        die("expected %d citation formulae between the heading and 'Whereas:', found %d" % (N_CITATIONS, len(citations)))
    recitals = []
    for line in lines[i_where + 1:i_end]:
        m = ROW.match(line)
        if not m:
            die("a line in the recitals region is not a row: %r" % line[:80])
        n = int(m.group(1))
        if n != len(recitals) + 1:
            die("recital %d is out of order (expected %d)" % (n, len(recitals) + 1))
        recitals.append(m.group(2))
    if len(recitals) != N_RECITALS:
        die("expected %d recitals, found %d" % (N_RECITALS, len(recitals)))
    return citations, recitals


def parse_corrigendum(lines):
    """Every correction whose heading says `recital N`: [(N, heading, for_text, read_text)]; also the count of all corrections."""
    found = []
    total = sum(1 for l in lines if l == "for:")
    for i, l in enumerate(lines):
        m = re.match(r"^On page \d+, recital (\d+),", l)
        if not m:
            continue
        if lines[i + 1] != "for:" or lines[i + 3] != "read:":
            die("the corrigendum entry %r does not have the shape heading / for: / text / read: / text" % l)
        n = m.group(1)
        pat = r"^\| ‘\(%s\) \| … (.+)’(?:,|\.) \|$" % n
        mf, mr = re.match(pat, lines[i + 2]), re.match(pat, lines[i + 4])
        if not (mf and mr):
            die("the for/read lines of the corrigendum entry %r are not in the expected frame" % l)
        found.append((int(n), l, mf.group(1), mr.group(1)))
    return found, total


def apply_corrigendum(recitals, corrections):
    out = list(recitals)
    log = []
    for n, heading, for_text, read_text in corrections:
        text = out[n - 1]
        if text.count(for_text) != 1:
            die("the corrigendum's 'for' passage of recital %d occurs %d times in the as-published recital, not once" % (n, text.count(for_text)))
        out[n - 1] = text.replace(for_text, read_text)
        log.append((n, heading, for_text, read_text))
    return out, log


def l4_string(s):
    """An L4 string literal: only the double quote and the backslash need an escape; a control character is refused."""
    for ch in s:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            die("a control character (U+%04X) in a text" % ord(ch))
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render(citations, recitals, corrected):
    L = []
    w = L.append
    w("-- gdpr-recitals.l4 -- the preamble's citations and the 173 recitals of Regulation (EU) 2016/679, carried as INERT text.")
    w("--")
    w("-- Recitals are reading aids, not rules: nothing here is decided, worked out or read by any rule of this encoding, and no")
    w("-- article is linked to a recital.  Each recital is carried so that the encoding mirrors the Regulation, as the")
    w("-- `hierarchy` library's outline: an `item` is text and nothing more.")
    w("--")
    w("-- Source: %s, the recitals as published in the Official Journal, L 119, 4.5.2016, p. 1 (rows (1) to (173))," % SRC_NAME)
    w("-- text byte for byte, including the inline footnote markers such as \"( 4 )\" and the curly quotes.  The footnote TEXTS")
    w("-- (1) to (18) are not carried, and neither are the title block and \"HAVE ADOPTED THIS REGULATION:\".")
    n_cor = len(corrected)
    if n_cor:
        nums = ", ".join(str(n) for n in corrected)
        w("-- Corrected: recital%s %s, by the corrigendum of OJ L 127, 23.5.2018, p. 2 (%s)," % ("" if n_cor == 1 else "s", nums, COR_NAME))
        w("-- the only correction of that corrigendum that falls in the recitals.")
    w("-- The licence of the source text is UNDETERMINED: see the subject's SOURCE-LICENSE.md.")
    w("--")
    w("-- Numbering: each recital is an automatically numbered item of one level in the Decimal style, so the library's renderer")
    w("-- gives \"1\" to \"173\" (a tab, then the text).  The Official Journal prints the number in brackets, \"(1)\"; the brackets are")
    w("-- not carried.  The preamble's citations are not numbered in the source, so they are rendered with the Bulleted style.")
    w("-- The trailing `-- (n)` on each line is a comment for the reader; the number the renderer gives is the item's position.")
    w("--")
    w("-- Generated by notes/gen-recitals.py; checked by notes/check-recitals.py.  Do not edit by hand.")
    w("-- Needs an unstable build of `l4`: the main build 1.6.112 (measured 2026-11-27) has neither the `hierarchy` library nor the bullet syntax.")
    w("")
    w("IMPORT hierarchy")
    w("")
    w("`GDPR citations scheme` MEANS LIST Bulleted")
    w("`GDPR recitals scheme` MEANS LIST Decimal")
    w("")
    w("-- The preamble: the six formulae between the title block and \"Whereas:\".")
    w("`GDPR preamble citations` MEANS")
    w("  item %s" % l4_string(HEAD))
    for c in citations:
        w("    • item %s" % l4_string(c))
    w("")
    w("-- The recitals, (1) to (173).")
    w("`GDPR recitals` MEANS")
    w("  item %s" % l4_string(WHEREAS))
    for n, r in enumerate(recitals, 1):
        w("    • item %s  -- (%d)" % (l4_string(r), n))
    w("")
    w("#ASSERT `count nodes` `GDPR preamble citations` EQUALS %d" % (1 + len(citations)))
    w("#ASSERT `count nodes` `GDPR recitals` EQUALS %d" % (1 + len(recitals)))
    w("#ASSERT depth `GDPR recitals` EQUALS 2")
    w("#ASSERT count (`render outline` `GDPR recitals scheme` `GDPR recitals`) EQUALS %d" % (1 + len(recitals)))
    w("")
    w("#EVAL `render outline` `GDPR citations scheme` `GDPR preamble citations`")
    w("#EVAL `render outline` `GDPR recitals scheme` `GDPR recitals`")
    w("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="write recitals/gdpr-recitals.l4 from the deposited as-published text")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--explain", action="store_true")
    a = ap.parse_args()

    citations, recitals = parse_source(read_checked(SOURCE, "eu-gdpr-2016-679.meta.json"))
    cor_lines = read_checked(CORRIGENDUM, "eu-gdpr-2016-679-corrigendum-20180523.meta.json")
    corrections, total = parse_corrigendum(cor_lines)
    recitals, log = apply_corrigendum(recitals, corrections)
    if a.explain:
        sys.stderr.write("the corrigendum has %d corrections; %d fall in the recitals\n" % (total, len(log)))
        for n, heading, f, r in log:
            sys.stderr.write("recital %d (%s)\n  for:  %s\n  read: %s\n" % (n, heading, f, r))
    text = render(citations, recitals, [n for n, _, _, _ in log])
    if a.out == "-":
        sys.stdout.write(text)
    else:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
