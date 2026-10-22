# PROGRESS (piece uc1)

Read this first after any compaction, then NOTES.md, then the text (../../registers/source-bundle/uksi-2013-376.txt lines 1-11 and 118-742).

## Status

All deliverables of the brief are written, and the last `check.sh` run (after the last edit to any `.l4` file) printed 25 modules, 0 errors, 1567 satisfied, 0 failed, 0 refused.
`srcrefs.py check` and `--strict` over `uc1-common.l4` and the nine `uc1-part*.l4` modules report 0 problems.
`l4 run` on each of the twenty-one `uc1-` files shows no warning.
NOTES.md has all ten headings filled; its "What check.sh prints" section holds the output of that last run.
What is not done is listed in NOTES.md under "Before this is worth relying on".

## Module layout (flat folder; every rule name begins `reg N...` or `uc1 —`)

| module | regs | lines in text | tests |
| --- | --- | --- | --- |
| uc1-common.l4 | helpers: age, leap year, last day of a month, absences, 1st September | | tested in the other tests files |
| uc1-part1-introduction.l4 | 1 (dates), 3, 4, 4A, 5, 6(2) | 1-11, 118-178 | uc1-tests-part1-introduction.l4 |
| uc1-part2-age-and-place.l4 | 8, 9, 10, 11 | 185-320 | uc1-tests-part2-age-and-place.l4 |
| uc1-part2-education-and-commitment.l4 | 12, 13, 14, 15, 16 | 321-398 | uc1-tests-part2-education-and-commitment.l4 |
| uc1-part2-finance-and-restrictions.l4 | 7, 17, 18, 19, 19A | 179-184, 399-425 | uc1-tests-part2-finance-and-restrictions.l4 |
| uc1-part3-awards.l4 | 20, 20A, 21, 21A, 22, 22A | 426-496 | uc1-tests-part3-awards.l4 |
| uc1-part4-children-housing.l4 | 23, 24, 24A, 24B, 25, 26 | 497-558 | uc1-tests-part4-children-housing.l4 |
| uc1-part4-needs.l4 | 27, 27A, 28, 29, 30 | 559-625 | uc1-tests-part4-needs.l4 |
| uc1-part4-childcare.l4 | 31, 32, 33, 34, 34A, 35 | 626-710 | uc1-tests-part4-childcare.l4 |
| uc1-part4-amounts.l4 | 36, 37 | 711-742 | uc1-tests-part4-amounts.l4 |
| uc1-seat.l4 | layer 2: 116 `@export` questions under 12 `§§` headings | | uc1-cases-seat.l4 (670 assertions, every question covered) |

## Decisions taken (with the text that licenses each; the full list is the Fork register in NOTES.md)

- Lost formulas: regulation 21A(2)(b), 22A(2) and 34A(2) show the variables of a formula and not the formula; the rules and seat questions return `NOTHING` (fork F-FORMULA).
- Regulation 7 only introduces Part 2; the join "basic and financial conditions met and no regulation 19 bar" is a reading (fork F-7-JOIN).
- Dates: made 25 Feb 2013, in force 29 Apr 2013 (title block lines 4-5, regulation 1 line 11) are defined values with `@ref`.
- Composition: a layer-1 rule that uses a defined term takes it as a plain yes or no; the seat builds the records in `WHERE` from plain inputs and calls the same module rule.
- Regulation 2: `reg 2 — blind`, `close relative` and `paid work` are called inside the modules; `terminally ill`, `prisoner`, `looked after by a local authority` and `foster parent` are called from the seat; the places that keep plain yes-or-no facts are listed in NOTES.md under "Needs from the core".
- Officials: no seat for the Secretary of State; a judgment the regulations leave to the Secretary of State is a yes-or-no fact the person states.
- Out-of-range facts (the Act, the Schedules, Parts 5 and 6, other instruments) are plain inputs commented `-- out of range: ... (piece X)`.

## Files written

All under `DEPOSIT/encodings/legalese-sonnet-5.5/`:
the ten modules `uc1-common.l4` and `uc1-part*.l4`, the nine `uc1-tests-*.l4` files, `uc1-seat.l4`, `uc1-cases-seat.l4`, `NOTES.md` and `PROGRESS.md`.
The keel's files (`uc-core*.l4`, `check.sh`, `srcrefs.py`) are in the same folder and were not edited.
