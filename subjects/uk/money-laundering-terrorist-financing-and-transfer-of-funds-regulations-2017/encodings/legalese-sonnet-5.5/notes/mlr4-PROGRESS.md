# PROGRESS -- mlr4 (lines 2200-3054 of uksi-2017-692.txt)

STATUS (2026-11-05): every deliverable in the brief exists in this folder and has been run; the last full `check.sh` is at the end of NOTES.md (13 modules, 1734 assertions satisfied, 0 errors, 0 failed, 0 refused, identical counts on main 1.6.109 and 1.6.108).
`srcrefs.py check --refs` and `--strict` report 0 problems on every module of this part.
This file records what was done and what was decided; NOTES.md is the record of the encoding.

## Sections done
- Part 8, regulations 65 to 74C: `mlr4-part8.l4`, tests `mlr4-tests-part8.l4` (445 assertions).
- Part 9, regulations 75 to 92: `mlr4-part9.l4`, tests `mlr4-tests-part9.l4` (565 assertions).
- Part 10, regulations 93 to 100: `mlr4-part10.l4`, tests `mlr4-tests-part10.l4` (192 assertions).
- Part 11, regulations 101 to 110: `mlr4-part11.l4`, tests `mlr4-tests-part11.l4` (139 assertions).
- Schedules 1, 2, 3 and 3AZA: `mlr4-schedules.l4`, tests `mlr4-tests-schedules.l4` (103 assertions).
- Seat layer: `mlr4-seat.l4` (99 questions) and `mlr4-cases-seat.l4` (290 assertions).
- NOTES.md: coverage, fork register, jural relations, marginal readings, reading a result, seams, dependencies, unstable dialect, findings, what main does not accept, check.sh output.

## Method (how the files are made)
- The modules and tests are generated from templates and a small test language kept outside this folder; every `-- src:` quote line is copied from the raw text by `srcrefs.py quote`, never retyped.
- The coverage table is generated from the text's structural units and the modules' `@ref` locators, and checked so that every non-blank line of the range is in one row.
- The marginal-readings table is a count of the `-- FALSE-kind ... [marginal ...]`, `[ruled 2026-11-05 (a) period]` and `[ruled 2026-11-05 (b) where]` tags and the `-- NOTHING-kind (limited by its own wording)` comments in the modules.

## Decisions taken (with the text that licenses each)
- Forks: F-OFFICER, F-ARRANGEMENTS, F-PERIOD, F-72-1, F-86-FINE, F-101-OFFICER, F-SCH3-NUMBERS, F-3AZA-NUMBERS, F-3AZA-INCLUDING, F-69-1, F-69-2, F-CHAPEAU, F-77-4, F-77-79, F-SCH3-36, F-WHEN (NOTES.md, fork register); design entries on the 2026-11-05 ruling, the 41 companion functions, polarity and F-95-1 are in the same register.
- "officer" inside Part 8 is regulation 65(2)'s own definition (regulation 3(1) says "except in Part 8 and Schedule 5"), so Part 8 has no S-K4 input; in Part 9 "officer" is regulation 3(1)'s and is the S-K4 input.
- A flat negative that names its bearer gets a derived prohibition (ruling N2): regulations 74(4), 76(4), 84(1) (two bearers), 95(2), 95(3) and 105(2) (two bearers).
- Regulations 104A, 108, 109 and 110(1) are encoded, not inert (the brief allows no such reason).
- The seat asks the answer of another section as "Yes / No / I am not sure"; ask that section's question first.

## Rework of 2026-11-05 (ruling: periods (a), "where" (b), scope limits (c))
- Unmet "where", "if" and period conditions now answer `JUST FALSE` across the range (list in the fork register); scope limits stay `NOTHING`.
- 41 companion functions (`... the duty ... arises`) say whether a duty arises; the compliance functions keep `NOTHING` where it does not.
- Seat: the regulation 99(1) input carries the regulation 58(3) exception; regulation 103(1) has both a "triggered" and a "must I" question.
- Schedule 3 paragraph 28 has the express exclusion for section 173 of the Data Protection Act 2018.
- Second ruling of 2026-11-05 ("when", "upon", "whenever" and "before" count as "where"; unproved defences; "until" bars; delegated definitions): five openers (F-WHEN: 74B(3), 81(1), 81(1A), 83(1), 83(1A)) now answer JUST FALSE outside their case, regulation 88(4) answers JUST FALSE ("gives no defence on these facts") when neither belief is proved, and section 133A(1) in 93(3)(b) has a bar twin; no site fits the delegated-definitions rule.
- Regulations 69(2) and 69(3) answer JUST FALSE when regulation 69(1) ("Paragraph (2) applies where") does; a sweep of every function with an "applies" or "arises" input found no other site (NOTES.md, fork register, F-CHAPEAU).
- Stated gaps are in the coverage rows (regulations 65(1) "tribunal", 74C(18), 77(2) with 79, 77(4), 78(2), 101, 102(4), 107, 108(1)).

## Open
Nothing is left undone in the brief.
What the text does not answer is listed in NOTES.md (every `NOTHING-kind` branch) and in the final report.
