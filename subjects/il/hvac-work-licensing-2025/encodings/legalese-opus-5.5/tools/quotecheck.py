"""Check that Hebrew quoted in fees-regulations.l4 is a substring of the gazette
text, after normalising whitespace, bidi controls, and dash/quote glyphs.

Usage: python3 -I quotecheck.py FEES_L4 KT11951_TXT KT12383_TXT FEES_WIKI
"""
import re
import sys

fees_l4, kt11951, kt12383, wiki = sys.argv[1:5]

BIDI = re.compile("[‎‏‪-‮⁦-⁩﻿]")


def norm(s):
    s = BIDI.sub("", s)
    s = re.sub(r"\{\{ח:הערה\|[^}]*\}\}", "", s)  # drop the wiki's own notes first
    s = re.sub(r"\{\{ח:[^|}]*\|([^}]*)\}\}", r"\1", s)  # then unwrap simple wiki templates
    for a in "”“״\"'׳’‘":
        s = s.replace(a, '"' if a in "”“״\"" else "'")
    for d in "–—־-":
        s = s.replace(d, "-")
    s = re.sub(r"\s+", "", s)
    return s


src_made = norm(open(kt11951, encoding="utf-8").read())
src_amend = norm(open(kt12383, encoding="utf-8").read())
src_wiki = norm(open(wiki, encoding="utf-8").read())

text = open(fees_l4, encoding="utf-8").read()

# The `the words` strings, keyed by the definition they sit in.
words = {}
for m in re.finditer(r"^`([^`]+)` MEANS\n(?:.*\n){0,6}?\s+`the words`\s+IS \"([^\"]+)\"", text, re.M):
    words[m.group(1)] = m.group(2)

checks = []
for name, w in words.items():
    if name.startswith("draft"):
        continue  # transcribed from an image; nothing to check against
    if "as amended" in name:
        checks.append((name, w, [("KT 12383", src_amend), ("wiki", src_wiki)]))
    else:
        checks.append((name, w, [("KT 11951", src_made), ("wiki", src_wiki)]))


# Comment quotes for regs 3 and 4 (the "AS MADE" blocks).
def comment_block(after):
    i = text.index(after)
    lines = []
    for line in text[i:].splitlines()[1:]:
        if not line.startswith("--"):
            break
        if line.startswith("-- ") and not line.startswith("--   ") and not line.startswith("-- (") and lines:
            break
        lines.append(line[2:])
    return " ".join(lines)


reg3 = comment_block("§§ `Regulation 3 — updating the fees`\n\n-- AS MADE (unchanged by KT 12383):")
reg4 = comment_block("§§ `Regulation 4 — payment as a condition`\n\n-- AS MADE (unchanged by KT 12383):")
checks.append(("reg 3 comment quote", reg3, [("KT 11951", src_made), ("wiki", src_wiki)]))
checks.append(("reg 4 comment quote", reg4, [("KT 11951", src_made), ("wiki", src_wiki)]))

bad = 0
for name, w, sources in checks:
    n = norm(w)
    res = []
    for label, src in sources:
        res.append(f"{label}:{'yes' if n in src else 'NO'}")
    ok = any(r.endswith("yes") for r in res)
    bad += 0 if ok else 1
    print(f"{'ok ' if ok else 'BAD'} {name}: {' '.join(res)}")
    if not ok:
        print("    quoted:", n[:200])
print("checked", len(checks), "bad", bad)
