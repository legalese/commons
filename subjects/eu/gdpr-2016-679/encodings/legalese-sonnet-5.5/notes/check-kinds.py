#!/usr/bin/env python3
# notes/check-kinds.py -- P2's audit of the answer tags (run from the deposit folder: python3 -I notes/check-kinds.py).
#  (1) every branch of a P2-art-*.l4 module that answers JUST FALSE, `the duty does not arise`, NOTHING or `the duty arises and is not met`
#      has a FALSE-kind or NOTHING-kind comment in the next three lines (a "no" or a "not covered" is never silent);
#  (2) every piece in double quotes inside a FALSE-kind or NOTHING-kind comment is found, word for word (case, punctuation and
#      spacing ignored; "..." splits a quotation into pieces), in the consolidated text.
import re, sys, glob, unicodedata
RAW = "../../registers/source-bundle/eu-gdpr-2016-679-consolidated-20160504.txt"
def norm(s):
    s = unicodedata.normalize("NFC", s).casefold()
    s = re.sub(r"[‘’“”'\"`]", "", s)
    s = re.sub(r"[^\w\s]", " ", s)
    return " " + re.sub(r"\s+", " ", s).strip() + " "
raw = norm(open(RAW, encoding="utf-8").read())
bad1 = bad2 = n_tags = n_pieces = 0
for f in sorted(glob.glob("P2-art-*.l4")):
    ls = open(f, encoding="utf-8").read().split("\n")
    for i, l in enumerate(ls):
        code = l.split("--")[0]
        if re.search(r"(THEN|ELSE|OTHERWISE)\s+(JUST FALSE|NOTHING|JUST `the duty does not arise`|JUST `the duty arises and is not met`)\s*$", code) or re.search(r"THEN IF .* THEN NOTHING ELSE JUST `the duty arises and is not met`\s*$", code):
            window = ls[i + 1:i + 4]
            if not any(re.match(r"^\s*-- (FALSE-kind|NOTHING-kind)", w) or "-- the provision's own question" in w or "-- the bar stands" in w or "-- the text says no" in w for w in window) and not re.search(r"-- (FALSE-kind|NOTHING-kind)", l):
                print("%s:%d: no FALSE-kind/NOTHING-kind tag after: %s" % (f, i + 1, l.strip()[:110])); bad1 += 1
        m = re.match(r"^\s*-- (FALSE-kind|NOTHING-kind)\b(.*)$", l)
        if m:
            n_tags += 1
            for piece in re.findall(r"\"([^\"]+)\"", m.group(2)):
                for part in re.split(r"\.\.\.|…", piece):
                    p = norm(part)
                    if len(p.strip()) < 4: continue
                    n_pieces += 1
                    if p not in raw:
                        print("%s:%d: quoted piece not in the text: %s" % (f, i + 1, part.strip()[:120])); bad2 += 1
print("tags %d, quoted pieces %d; untagged branches %d; pieces not found %d" % (n_tags, n_pieces, bad1, bad2))
