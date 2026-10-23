# PROGRESS (uro: Social Security Benefits Up-rating Order 2026, S.I. 2026/148)

Last updated: every deliverable is written and green (check.sh 1106 assertions satisfied, 0 failed, 0 refused; srcrefs --refs 0 problems); the advisor review is applied; only the final report remained.

## How the files are made (read this after any compaction)

The deposited `uro-*.l4` module files (everything that is not a test, the seat layer or the cases) are GENERATED. Their sources are
`uro-*.l4.in` in
`a scratch directory outside this folder (not committed)/`.
`work/expand.py` expands the macros (`%%Q` quotes source lines mechanically, `%%SUM` reads "for X substitute Y"
figures from the text file, `%%NDD` the six non-dependant deduction tables, `%%LOOKUP`, `%%DEFS`), and
`work/build.sh` runs expand + `check.sh` (L4_TARGET=unstable, the stable 1.6.98 binary) + `srcrefs.py check --refs`.
Edit the `.in` files, never the generated `.l4`.
The test files `uro-tests-*.l4` are written directly into this folder (two throwaway scripts, `work/gen_jsa_tests.py` and an inline one for `uro-tests-non-dependant-deductions.l4`, only format hand-chosen values so that positions cannot slip).
`uro-seat.l4` and `uro-cases-seat.l4` are written by `work/gen_seat.py` from one hand-written question table (edit the table, not the output).
NOTES.md is written by `work/render_notes.py` (generated tables: coverage, seat questions, dependencies, the check.sh output) and `work/notes_text.py` (the prose); edit those, not NOTES.md.
`work/add_oot.py` put the `-- out of text:` comments into the `.in` files (idempotent).
Generator scripts live in `work/` (not part of the deposit).

## Decisions taken (with the text that licenses each)

- Figures the Order states are values (`a sum and its replacement` record: old and new), cited with `@ref` and src locators. (arts 4(2), 6(1), 8-10, 12-19, 20-33)
- "Increased by 3.8 per cent" is a function of an input sum; the Order states no rounding, so the exact product is returned (F-01). (arts 4(1),(3),(4), 5, 6(2),(3), 11(2)-(4), 21)
- Dates: made 2 March 2026 (title block); art 1(3)(a)-(o) one rule each; art 1(4) override; art 7 one rule per paragraph; art 34 revocation date = art 1(3)(o).
- Benefit-week and assessment-period dates are plain inputs (defined outside the text); a date before 6 April 2026 gives NOTHING (F-06).
- Tables with parent-instrument conditions: the condition is a plain input named for the fact; the first row that holds wins where the text says nothing about overlap (F-10).
- A not-covered case returns NOTHING (a MAYBE) or a named constructor; asserted.
- Where the Order amends a sum "as it has effect in" a stated kind of case the case is a plain input and a person outside it gets NOTHING (F-15).
- Schedule 12 paragraph 1 row (iii) is read as printed ("not entitled to the support component"), so the work-related activity component does not matter under paragraph 1 (F-13); this was changed from a NOTHING reading in the last session, with the tests and seat cases changed to match by reading the text.
- The six pointer paragraphs (arts 20(5), 23(8), 24(8), 26(5), 26(6), 32(2)) are cited by an extra `@ref` on the first rule of the Schedule they point to.

## Files

Layer 1: uro-nouns, uro-part1-intro, uro-part2-arts-3-to-6, uro-part2-art7-effect-dates, uro-part2-arts-8-to-19, uro-schedule1-contributions-act-rates, uro-part3-income-support, uro-part3-housing-benefit, uro-part4-jsa, uro-part5-pension-credit, uro-part6-esa, uro-part7-universal-credit, uro-part8-revocation.
Tests: uro-tests-part1, uro-tests-part2-arts-3-to-7, uro-tests-schedule1, uro-tests-part2-arts-8-to-19, uro-tests-part3-income-support, uro-tests-part3-housing-benefit, uro-tests-part4-jsa, uro-tests-part5-to-8, uro-tests-non-dependant-deductions.
Layer 2: uro-seat (131 questions), uro-cases-seat (one or more cases for every question).
Reports: NOTES.md, PROGRESS.md.

## Done

- Advisor review applied: the seat questions are now in the text's own order (article 7 after article 6, articles 11 to 13 after articles 8 to 10), the arts 22 and 27 jural row has no holder and no bearer, and the stray full stop in a dependency cell is gone.
- Final check.sh and srcrefs runs are the ones printed in NOTES.md.
