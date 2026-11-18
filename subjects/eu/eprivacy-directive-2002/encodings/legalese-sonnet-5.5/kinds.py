#!/usr/bin/env python3
"""kinds.py RAW FILE...  -- the FALSE/NOTHING comment rule of the brief, checked mechanically.

For the layer-1 and seat modules it checks:
  1. every result branch `JUST FALSE` carries a `FALSE-kind (the text says no in its own words): "<quoted words>"` comment
     on its own line or in the three lines above it, and every quoted string occurs in the raw text (whitespace collapsed);
  2. every result branch `NOTHING` carries a `NOTHING-kind (<why>)` comment there, <why> being one of: silent, list not
     closed, includes, undefined term, points outside the text, limited by its own wording.
Lines that begin with #ASSERT or #EVAL or #TRACE, comment-only lines and type signatures are not result branches.
Exit status 1 on any problem.  Run as: python3 -I kinds.py RAW epd-art*.l4 epd-seat*.l4"""
import re, sys, unicodedata
WHY = ("silent", "list not closed", "includes", "undefined term", "points outside the text", "limited by its own wording")
def norm(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
raw = norm(" ".join(open(sys.argv[1], encoding="utf-8").read().split("\n")))
problems = 0; nfalse = 0; nnothing = 0
for path in sys.argv[2:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        code = line.split("--")[0] if not line.lstrip().startswith("--") else ""
        if not code.strip(): continue
        if re.match(r"\s*#(ASSERT|EVAL|TRACE|CHECK)", code): continue
        window = "\n".join(lines[max(0, i - 3): i + 1])
        res_false = re.search(r"\bJUST FALSE\b", code) is not None
        res_nothing = re.search(r"\bNOTHING\b", code) is not None and not re.search(r"\bWHEN NOTHING THEN\b(?!.*\bNOTHING\b)", code) \
                      and not re.search(r"^\s*(GIVEN|GIVETH)\b", code)
        # a line that only matches a MAYBE input (WHEN NOTHING THEN x) is not a result branch
        if re.search(r"\bWHEN NOTHING THEN\b", code) and not re.search(r"THEN\s.*\bNOTHING\b", code):
            res_nothing = False
        if res_false:
            nfalse += 1
            m = re.findall(r'FALSE-kind \(the text says no in its own words\): "([^"]+)"', window)
            if not m:
                print(f"{path}:{i+1}: JUST FALSE without a FALSE-kind comment"); problems += 1
            else:
                for q in m:
                    if norm(q) not in raw:
                        print(f"{path}:{i+1}: FALSE-kind quotation not in the text: {q[:80]!r}"); problems += 1
        if res_nothing:
            nnothing += 1
            m = re.findall(r"NOTHING-kind \(([^)]*)\)", window)
            if not m:
                print(f"{path}:{i+1}: NOTHING without a NOTHING-kind comment"); problems += 1
            elif not any(w.startswith(why) for w in m for why in WHY):
                print(f"{path}:{i+1}: NOTHING-kind reason not one of the six: {m}"); problems += 1
print(f"kinds check: {nfalse} JUST FALSE branches, {nnothing} NOTHING branches, {problems} problems")
sys.exit(1 if problems else 0)
