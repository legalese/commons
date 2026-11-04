# PROGRESS: part ssc3 (ss 43 to 62, lines 1230 to 1911 of ukpga-1992-4.txt)

Status 2026-11-04: layer 1 (eight modules, helpers, seven test files), layer 2 (seat and its cases), NOTES.md and this file are written.
Final `check.sh` run (stable 1.6.98 and main 1.6.108, `work/final/check.log`): 19 modules, 0 errors, 1185 assertions satisfied, 0 failed, 0 refused, 19 of 19 module rows `same` on main.
Diagnostics scan of 18 `ssc3-*.l4` files on the stable binary, errors and warnings counted separately (`work/final/diag-summary.txt`): 0 errors, 0 warnings, 1185 assertions satisfied.
`srcrefs.py check --refs`: 622 src: lines, 240 runs, 240 locators, 0 problems; `--strict`: 622 src: lines, 240 runs, 240 locators, 0 problems.

## Done

- [x] Coverage unit splitter and dispositions (`work/units.py`, `work/dispositions.py`): 669 units over 682 non-blank lines, every line in exactly one unit, none unclassified.
- [x] Layer 1: `ssc3-helpers.l4`, `ssc3-a0-s61za-s61zc.l4`, `ssc3-a-s43-s44.l4`, `ssc3-b-s44a-s44c.l4`, `ssc3-c-s45-s46.l4`, `ssc3-d-s47-s48c.l4`, `ssc3-e-s51-s55.l4`, `ssc3-f-s55a-s56.l4`, `ssc3-g-s60-s62.l4`.
- [x] Tests: `ssc3-tests-a.l4` to `ssc3-tests-g.l4` (1024 assertions), expected values written by hand from the text.
- [x] Seat: `ssc3-seat.l4` (42 questions) and `ssc3-cases-seat.l4` (161 cases).
- [x] NOTES.md assembled by `work/notes_build.py` from `work/notes/*.md` plus generated parts (coverage table, marginal readings, question list); `work/checks_fill.py` writes the "What check.sh prints" part from the final logs.

## Decisions taken (with the section that licenses each)

- Fork readings F1 to F8: see NOTES.md, Fork register.
- Seat reading for s 45(2): `s 46(4) ... EQUALS JUST TRUE` is the fact "paragraph (d) is omitted" (s 46(4) applies "in a case where the deceased ... died under pensionable age").
- Seat cases for s 56(3) were first written inverted by me; corrected from the text ("shall not be payable unless one of the conditions specified in subsection (4) below is satisfied"); finding 12.
- Helper names carry the prefix `ssc3 helper` (departure from PLAN 1.2).
- The seat asks no question of the sub-functions of a section; it calls the function that gives the person's answer (NOTES.md, Seat, "What the seat calls").
- Regulation-making powers: inert reason 2, except where the Act makes the content of regulations a condition or a quantity of entitlement (then encoded, content an input).

## Not done

- Schedules 5 and 5A (increase or lump sum on deferment) are not among the sources.

## Files

Everything under `RUN/deposit/encodings/legalese-sonnet-5.5/` named `ssc3-*.l4`, plus `NOTES.md` and this file.
Scratch (not shipped): `RUN/work/` (templates in `work/src/`, `build.py`, `units.py`, `dispositions.py`, `notes_build.py`, `checks_fill.py`, `progress_fill.py`, logs).
Layer-1 modules are generated from `work/src/*.l4.in` by `work/build.py`, which copies the verbatim `-- src:` lines from the text file; edit the templates and rebuild.
