# PROGRESS: ei1

Piece ei1: Act lines 133-669 (Part I, ss 6 to 23.3(5)).
My working files (not deliverables) are in `inputs/work/`: `tpl/*.l4` are the module sources with `--@@ N M` quote markers, `build.py` expands the markers with `srcrefs.py quote` into this folder, `cov.py`/`apply.py`/`setrow.py` write coverage rows into NOTES.md, `run.sh` runs one file and prints the problem lines.
After a compaction: re-read this file, NOTES.md, and the module sources in `inputs/work/tpl/` (layer 1 is built from them, tests and seat files are written directly into this folder).

## State (2026-10-24, later)

Layer 1 is complete for the whole range (ss 6 to 23.3(5)). Every module compiles clean, srcrefs reports 0 problems, and every test file has assertions written equal to assertions satisfied:
- ei1-interpretation.l4 (s 6)                                  tests: ei1-tests-interpretation.l4 (64)
- ei1-qualifying.l4 (ss 7, 7.1, 8)                             tests: ei1-tests-qualifying.l4 (180)
- ei1-payment.l4 (ss 12, 13, 13.1)                             tests: ei1-tests-payment.l4 (123)
- ei1-benefit-period.l4 (ss 9, 10, 11)   [imports ei1-payment]  tests: ei1-tests-benefit-period.l4 (156)
- ei1-rate.l4 (ss 14, 15, 16, 17)                              tests: ei1-tests-rate.l4 (64)
- ei1-disentitlement-deductions.l4 (ss 18, 19, 20)             tests: ei1-tests-disentitlement-deductions.l4 (58)
- ei1-illness-pregnancy.l4 (ss 21, 22)                         tests: ei1-tests-illness-pregnancy.l4 (44)
- ei1-parental.l4 (s 23)   [imports ei1-payment, ei1-benefit-period]   tests: ei1-tests-parental.l4 (79)
- ei1-caring.l4 (ss 23.1, 23.2, 23.3(1)-(5)) [imports ei1-benefit-period]   tests: ei1-tests-caring.l4 (113)

Coverage table in NOTES.md: all rows filled (headings, sections, subsections, and paragraph rows for s 6(1), 6(4), 7(2), 7.1(5), 8(1), 10(6), 10(8), 12(2.3), 12(4), 18(1), 19(3)).

## Seat layer (layer 2) (2026-10-24, after the usage-limit interruption)

DONE: ei1-seat.l4 (112 questions, 17 `§§` groups, compiles clean) and ei1-cases-seat.l4 (438 assertions, all satisfied; a mutation of three expected values gave three failures, so the harness can fail; every question has at least one case, `casegen` reports none missing).
Both are GENERATED from `inputs/work/seat/` (edit `seat_g1..g6.py`, `seat_inputs.py`, `cases_defs.py`; run `python3 seatgen.py g1 g2 g3 g4 g5 g6` then `python3 cases_run.py`). Do not hand-edit the .l4 files.

## Still to do (NEXT: the NOTES.md sections, then the gates)

(superseded: every NOTES.md section is now written; see the FINISHED state above.)
Then: srcrefs gate on every ei1 file (`python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/S.C.-1996-c.-23.txt ei1-*.l4` from this folder), `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` after the last .l4 edit, the loud-vs-silent grep (`l4 check` per file, grep 'follows code on its line|at the end of the file|Unknown annotation'), remove inputs/work only if nothing in DEPOSIT depends on it (it does not; it is outside DEPOSIT anyway).

## Decisions taken (all "assumed, not ruled", each in the fork register when NOTES.md is finished)

- Regulations are inputs, never encoded: every "prescribed" figure or condition is a plain input with a comment `out of range: reg N (piece X)`.
- s 7.1(1) with violations of several classes: the largest figure of the classes in the window (F-several).
- s 7.1(5): (b) subsequent prevails over (a) value classes (F-subsequent).
- s 8(1): the shorter is judged before extension; no preceding benefit period means (a) (F-no-prior, F-shorter).
- s 10(9) "paragraph 8(d)" read as 10(8)(d) (F-9).
- s 10(13) extension = s 10(15) length less 52 weeks (F-13); s 10(13.02) shortfall is an input (F-13.02).
- s 12(2.3) "established" read as "began" for earlier benefit periods (F-established); (2.3) before (2.1) (F-overlap); "around the same time of year" window (F-around).
- The 260 weeks before an initial claim end the day before the claim (F-window).
- Seat for a violation: one violation (the highest class), not a list (F-seat-violation).
- s 14(2): weekly insurable earnings capped at the maximum weekly insurable earnings (F-cap); s 17 caps the s 14(1) rate only (F-17).
- s 19(2): each percentage amount rounded under s 6(2) (F-round); a deduction cannot take the week below nothing (F-floor). s 20: 1/5 of the rate rounded per day (F-day).
- s 22(2), s 23(2): the period runs to the last day of the week 17 / 52 weeks after (F-22-2). s 23(3.2) extension = s 10(13) extension (F-23-3.2); (3.3)/(3.4) limits on the whole period (F-23-3.4); s 23(6)(b) 'that claimant' = the individual (F-23-6).
- s 23.1(4): when (a)(i), (ii), (iii) all apply, (iii) then (ii) then (i) (F-23.1-4).
- Regulations facts found by grep (no reg names a shorter period for s 23.1(5), nor 'other circumstances' for ss 10(5.1)-(5.3), 23.1(6), 23.2(5), 23.3(4), nor 'prescribed requirements' for the deferrals): inputs.

## Files written

NOTES.md, PROGRESS.md; layer 1: ei1-interpretation.l4, ei1-qualifying.l4, ei1-payment.l4, ei1-benefit-period.l4, ei1-rate.l4, ei1-disentitlement-deductions.l4, ei1-illness-pregnancy.l4, ei1-parental.l4, ei1-caring.l4; tests: ei1-tests-interpretation.l4, -qualifying, -payment, -benefit-period, -rate, -disentitlement-deductions, -illness-pregnancy, -parental, -caring; layer 2 (partial): ei1-seat.l4

## State: FINISHED (2026-10-24)

All deliverables are written and checked after the last edit to any .l4 file:
- check.sh (`L4_TARGET=unstable`): 24 modules, 0 errors, 1,345 assertions satisfied (464 seat cases + 881 in the nine layer-1 test files), 0 failed, 0 refused, exit 0, 167 s. Pasted in NOTES.md `## What check.sh prints`.
- srcrefs `--refs`: 432 src lines, 164 runs, 231 locators, 0 problems.
- `l4 check` on all 20 ei1 files: Check succeeded, no annotation-placement warnings.
- Coverage table: 195 rows = 149 encoded + 21 fork + 11 inert + 14 repealed or blank, over 23 sections and 9 headings; every non-blank line of 133-669 is in exactly one row.
- Seat: 119 questions in 17 `§§` groups; cases: 464 assertions, at least one per question, with explicit not-covered (NOTHING) cases.
Nothing remains but the final report. The working scripts are in `inputs/work/` (outside the deposit) and are not deliverables.

## Decisions taken (all "assumed, not ruled", each in the fork register when NOTES.md is finished)

- Regulations are inputs, never encoded: every "prescribed" figure or condition is a plain input with a comment `out of range: reg N (piece X)`.
- s 7.1(1) with violations of several classes: the largest figure of the classes in the window (F-several).
- s 7.1(5): (b) subsequent prevails over (a) value classes (F-subsequent).
- s 8(1): the shorter is judged before extension; no preceding benefit period means (a) (F-no-prior, F-shorter).
- s 10(9) "paragraph 8(d)" read as 10(8)(d) (F-9).
- s 10(13) extension = s 10(15) length less 52 weeks (F-13); s 10(13.02) shortfall is an input (F-13.02).
- s 12(2.3) "established" read as "began" for earlier benefit periods (F-established); (2.3) before (2.1) (F-overlap); "around the same time of year" window (F-around).
- The 260 weeks before an initial claim end the day before the claim (F-window).
- Seat for a violation: one violation (the highest class), not a list (F-seat-violation).
- s 14(2): weekly insurable earnings capped at the maximum weekly insurable earnings (F-cap); s 17 caps the s 14(1) rate only (F-17).
- s 19(2): each percentage amount rounded under s 6(2) (F-round); a deduction cannot take the week below nothing (F-floor). s 20: 1/5 of the rate rounded per day (F-day).
- s 22(2), s 23(2): the period runs to the last day of the week 17 / 52 weeks after (F-22-2). s 23(3.2) extension = s 10(13) extension (F-23-3.2); (3.3)/(3.4) limits on the whole period (F-23-3.4); s 23(6)(b) 'that claimant' = the individual (F-23-6).
- s 23.1(4): when (a)(i), (ii), (iii) all apply, (iii) then (ii) then (i) (F-23.1-4).
- Regulations facts found by grep (no reg names a shorter period for s 23.1(5), nor 'other circumstances' for ss 10(5.1)-(5.3), 23.1(6), 23.2(5), 23.3(4), nor 'prescribed requirements' for the deferrals): inputs.

## Files written

NOTES.md, PROGRESS.md; layer 1: ei1-interpretation.l4, ei1-qualifying.l4, ei1-payment.l4, ei1-benefit-period.l4, ei1-rate.l4, ei1-disentitlement-deductions.l4, ei1-illness-pregnancy.l4, ei1-parental.l4, ei1-caring.l4; tests: ei1-tests-interpretation.l4, -qualifying, -payment, -benefit-period, -rate, -disentitlement-deductions, -illness-pregnancy, -parental, -caring; layer 2 (partial): ei1-seat.l4

## State at the final check (2026-10-24)

ALL .l4 FILES ARE FINAL. The seat has 119 questions (the seven extra questions are in; `inputs/work/seat/seat_extra.py`), the cases file 464 assertions, all satisfied; srcrefs 0 problems before the last seat edits (re-run in step 2).
NOTES.md is complete except `## What check.sh prints` and the timing sentence in `## What the stable binary does not accept` (check.sh's real time).
NEXT, in this order:
1. `L4=<L4_BIN> L4_TARGET=unstable ./check.sh > ../../../inputs/work/check-final.txt` (running in the background; read check-final.txt when the notification arrives) and paste into NOTES.md `## What check.sh prints`;
2. `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/S.C.-1996-c.-23.txt ei1-*.l4`, paste its summary line;
3. the final report: files; check.sh output; coverage 195 = 149 encoded + 21 fork + 11 inert + 14 repealed over 23 sections and 9 headings; forks; the 119 questions; not-covered cases; cross-references (39 rows); what the source does not answer; peeked: nothing. The advisor was rate-limited and not usable.
