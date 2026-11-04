# PROGRESS (snap4): lines 1425-1795, 2951-2978, 3265-3325 of usc07-ch51.txt

Status as of 2026-11-04: every layer-1 module, its tests, the seat layer, its cases, NOTES.md and SEAMS.md are written.
`check.sh` (stable 1.6.98 and main 1.6.108): 19 modules, 0 errors, 845 assertions satisfied, 0 failed, 0 refused, the same on both builds, exit 0.
`srcrefs.py check --refs` and `--strict`: 223 locators, 0 problems.
Coverage: 356 units, 0 uncovered, 0 rules untested.

## Paths
- DEPOSIT dir: <the lead's scratchpad>/runs/iaw-snap4/deposit/encodings/legalese-sonnet-5.5
- work dir (not shipped): .../runs/iaw-snap4/work (tools in work/tools; sources with quote markers in work/src; gen/ holds the generated tables)
- L4=.../scratchpad/bin/l4-stable-98   L4_MAIN=.../scratchpad/bin/l4-main-108
- Check: `cd $DEPOSIT && L4=$L4 L4_MAIN=$L4_MAIN ./check.sh`; refs: `python3 -I srcrefs.py check --strict <raw> snap4-*.l4`

## Method
- Quotes are `--QUOTE N M` markers in work/src/*.l4, expanded by work/tools/expand-quotes.py into `-- src:` lines copied from the raw file; the deposit module files are the expanded output (edit work/src and run work/b.sh NAME, never the deposit file). `snap4-seat.l4` and `snap4-cases-seat.l4` have no quotes and are written directly in the deposit.
- NOTES.md is assembled by work/tools/notes.py from work/notes/*.md and the generated tables in work/gen (coverage.py, marginal.py, seams.py); re-run it after any change to a module, then re-run check.sh and paste its output (the script reads work/check-run1.log).
- Duties with a named party and a deadline: a regulative rule (traced; the stable binary cannot #ASSERT a DEONTIC) AND a decision function (asserted).

## Done
- snap4-s2020-a-d, -e-1, -e-2, -f-n, -o-x (+ tests: 72, 150, 66, 55, 153 assertions; 6 traces)
- snap4-s2021 (+ tests, 164), snap4-s2032 (+ tests, 27), snap4-s2036b-d (+ tests, 93)
- snap4-seat (25 questions), snap4-cases-seat (65 assertions)
- NOTES.md, SEAMS.md; no NEEDS-CORE.md (nothing missing from the core)

## Decisions taken (with the provision that licenses each)
- Forks F-1 (s 2020(s)(2) last day counted), F-2 (s 2021(b)(4) against the tiers), F-3 (s 2036c(a) 180-day period): see NOTES.md.
- A failed "if" and a flat negative are `JUST FALSE`; a case outside a grant's own wording is `NOTHING`; a ceiling or floor beyond its limit is `JUST FALSE` (the last is snap4's own extension of the first reading): NOTES.md, "Marginal readings for a lawyer".
- "Rural Alaska" (s 2020(m), line 1583) is the core's `Alaska, rural 1` and `Alaska, rural 2`.
- `s 2012(j)` is asked as a list of per-member answers (s 2020(w)); PLAN.md names the per-member function.

## Files written
Everything in the deposit folder except snap-core.l4, check.sh, srcrefs.py and fetch-main-l4.sh (supplied).

## After the independent test pass (2026-11-04)
- Three branches changed, in snap4-s2020-e-1 (s 2020(e)(8)(E)) and snap4-s2020-f-n (s 2020(g) refer and withhold), with 5 test assertions added and 4 changed; two comments relabelled (s 2020(h), s 2021(e)(1)); every function signature unchanged. NOTES.md, "After the independent test pass", has the ground for each answer that was kept.
