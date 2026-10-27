#!/usr/bin/env python3
"""Quote the LINDB text mechanically, without Planalto's editorial notes, and check the quotations.

  python3 -I quote-lines.py quote RAW N [M]   print `-- src:N | text` for raw lines N..M
  python3 -I quote-lines.py check RAW FILE... verify every `-- src:N | text` line in FILE...
  python3 -I quote-lines.py expand RAW FILE... replace each marker line `-- @@N@@` or `-- @@N-M@@` in FILE
                                              by the quote lines `quote RAW N M` prints (so no Portuguese is typed)

Why this exists beside srcrefs.py.
STUB-SOURCE-LICENSE.md says the encodings quote the statute's text, not Planalto's notes
("(Redação dada pela ...)", "(Incluído pela ...)", "(Vide ...)", "(Vigência)", "(Regulamento)", and the bare link label "Vigência").
`srcrefs.py quote` prints whole raw lines, notes included.
This script prints each raw line with those trailing notes removed, and nothing else changed:
whitespace squeezed to single spaces, NFC, as srcrefs.py does.
A line that is nothing but notes prints nothing.
"(Revogado pela ...)" and "(VETADO)" are NOT notes: they are the text, so they stay.

`check` is stricter than srcrefs.py's R1, which compares case-folded text with punctuation collapsed.
For every single-line quote `-- src:N | text` it requires
  (1) the text is exactly the raw line N, squeezed and NFC, up to its trailing editorial notes
      (so a changed semicolon, a dropped clause or a cut word is a problem), and
  (2) whatever the quote leaves off the end of the raw line is editorial notes only,
      so the quotation cannot silently truncate statute text.
It reads quote lines only; it does not read `@ref` locators (srcrefs.py check --refs does).
Exit status 1 on any problem.
"""
import re
import sys
import unicodedata

NOTE = re.compile(
    r"\s*(?:\((?:Redação dada|Incluído|Incluída|Vide|Vigência|Regulamento)[^)]*\)\.?|(?<=\s)Vigência(?=\s|$))"
)
QUOTE = re.compile(r"^\s*--\s*src:(\d+)(?:-(\d+))?\s*\|\s?(.*)$")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def squeeze(s):
    return re.sub(r"\s+", " ", nfc(s)).strip()


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read().split("\n")


def split_notes(line):
    """Return (text, notes): the line with every editorial note at its END removed, and the removed tail."""
    s = squeeze(line)
    tail = ""
    while True:
        m = None
        # find the last editorial note that ends the string
        for cand in NOTE.finditer(s):
            if cand.end() == len(s) or s[cand.end():].strip(" .") == "":
                m = cand
                break
        if m is None:
            break
        tail = s[m.start():] + tail
        s = s[: m.start()].rstrip()
    return s, tail


def cmd_quote(raw, n, m):
    lines = load(raw)
    for i in range(n, m + 1):
        text, _ = split_notes(lines[i - 1])
        if text:
            print(f"-- src:{i} | {text}")


MARKER = re.compile(r"^(\s*)--\s*@@(\d+)(?:-(\d+))?@@\s*$")


def cmd_expand(raw, files):
    lines = load(raw)
    for f in files:
        out = []
        n_expanded = 0
        for l4 in load(f):
            m = MARKER.match(l4)
            if not m:
                out.append(l4)
                continue
            indent, a = m.group(1), int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            for i in range(a, b + 1):
                text, _ = split_notes(lines[i - 1])
                if text:
                    out.append(f"{indent}-- src:{i} | {text}")
            n_expanded += 1
        with open(f, "w", encoding="utf-8", newline="") as fh:
            fh.write("\n".join(out))
        print(f"{f}: {n_expanded} markers expanded")


def cmd_check(raw, files):
    lines = load(raw)
    problems = 0
    count = 0
    for f in files:
        for ln, l4 in enumerate(load(f), 1):
            q = QUOTE.match(l4)
            if not q:
                continue
            n, m, text = int(q.group(1)), q.group(2), squeeze(q.group(3))
            count += 1
            if m is not None:
                print(f"{f}:{ln}: range quotes are not used in this row; quote one raw line per quote line")
                problems += 1
                continue
            if not (1 <= n <= len(lines)):
                print(f"{f}:{ln}: raw line {n} does not exist")
                problems += 1
                continue
            want, tail = split_notes(lines[n - 1])
            if text != want:
                print(f"{f}:{ln}: src:{n} text differs from raw line {n} without its editorial notes")
                print(f"    quote: {text}")
                print(f"    raw:   {want}")
                problems += 1
    print(f"quote-lines check: {count} quote lines, {problems} problems")
    return 1 if problems else 0


def main(argv):
    if len(argv) >= 4 and argv[1] == "quote":
        n = int(argv[3])
        m = int(argv[4]) if len(argv) > 4 else n
        cmd_quote(argv[2], n, m)
        return 0
    if len(argv) >= 4 and argv[1] == "expand":
        cmd_expand(argv[2], argv[3:])
        return 0
    if len(argv) >= 4 and argv[1] == "check":
        return cmd_check(argv[2], argv[3:])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
