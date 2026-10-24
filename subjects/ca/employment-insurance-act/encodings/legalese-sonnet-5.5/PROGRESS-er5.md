# PROGRESS: piece er5 (Regulations Part IV pilot projects and Part V administrative provisions, lines 1394-1708)

Written by the piece agent `er5` (Sonnet 5.5). Re-read this file, NOTES.md and the text after any compaction, not a summary.

## State (2026-10-24)

Everything the brief asks for is written and checked; what remains is review.

| module | regs | tests (assertions satisfied) |
| --- | --- | --- |
| `er5-pilot-claims.l4` | 77 (Pilot No. 1), 77.1 (No. 5) | `er5-tests-pilot-claims.l4` (72) |
| `er5-pilot-weeks.l4` | 77.2 (No. 6), 77.3 to 77.6 repealed, 77.91 (No. 14), 77.92 (No. 15), 77.992 (No. 21), 77.993 (No. 22) | `er5-tests-pilot-weeks.l4` (107) |
| `er5-pilot-rate.l4` | 77.7 (No. 11), 77.93 (No. 16) | `er5-tests-pilot-rate.l4` (32) |
| `er5-pilot-earnings.l4` | 77.8 (No. 12), 77.9 repealed, 77.94 (No. 17), 77.95, 77.97, 77.99 (Nos. 18 to 20) | `er5-tests-pilot-earnings.l4` (79) |
| `er5-pilot-elections.l4` | 77.96, 77.98, 77.991 | `er5-tests-pilot-elections.l4` (77) |
| `er5-pilot-hours.l4` | 77.994 (No. 23) | `er5-tests-pilot-hours.l4` (42) |
| `er5-pilot-24.l4` | 77.995 to 77.999 (No. 24) | `er5-tests-pilot-24.l4` (57) |
| `er5-admin-reconsideration.l4` | 78 to 82, 83 to 87 repealed | `er5-tests-admin-reconsideration.l4` (50) |
| `er5-admin-coverage-decision.l4` | 88 | `er5-tests-admin-coverage-decision.l4` (19) |
| `er5-admin-sin.l4` | 89 | `er5-tests-admin-sin.l4` (36) |
| `er5-admin-electronic-systems.l4` | 90, 91 | `er5-tests-admin-electronic-systems.l4` (29) |
| `er5-admin-direct-deposit.l4` | 92 | `er5-tests-admin-direct-deposit.l4` (27) |
| `er5-seat.l4` | layer 2: 115 questions under `§§` headings | `er5-cases-seat.l4` (150) |

`check.sh` (target unstable, binary 1.6.98): 30 modules, 0 errors, 777 assertions satisfied, 0 failed, 0 refused.
`srcrefs.py check --refs SOR-96-332.txt er5-*.l4`: 384 src lines, 193 runs, 230 locators, 0 problems.
NOTES.md is complete (all ten headings); it was assembled by a script from parts kept outside the deposit (coverage rows, fork register, jural relations, cross-references), so a later edit to the rules means regenerating or editing it by hand.

## Decisions taken (with the provision that licenses each)

- Every pilot is `encoded` though all sixteen windows have now closed (No. 24's closed October 10, 2026): the brief's `inert` list has no "spent" reason. The date of the fact (benefit period, week, earnings week) is an input to each rule.
- A purpose subsection is a named STRING constant with its `@ref` (phrasebook 9.3), not `inert`; a repealed section is a labelled stub (strings) with a coverage row `repealed or blank in this text`.
- "The day on which this section comes into force" (77.1(2),(6), 77.994(2), 77.999(2)) is a DATE input; the text never states it.
- Duties are BOOLEAN rules and DATE-returning deadline rules (DEONTIC cannot be `EQUALS`-asserted on this binary).
- Where regs 77.7/77.93, 77.8/77.94 and 77.95/77.97/77.99 say the same thing in the same words, one rule carries all the locators; what differs (windows, cessation days) is a rule apiece.
- "Ceases to have effect on D" for the five weekly sections is read as effect through D (all D are Saturdays that close a Sunday-to-Saturday window): fork F-reg77.8c. Reg 77(7), with no week to anchor it, is read as out of force from April 1, 1997.
- No rounding under s 6(2) of the Act (fork F-reg77.8d).

## Helper scripts (outside the deposit, in the lead's scratchpad)

`er5run.sh FILE...` runs files and prints satisfied/errors/warnings; `er5fill.sh FILE...` fills `@@Q n m` lines with `srcrefs.py quote` output and runs `srcrefs check --refs`; `er5strings.py` checks string literals against the source; `work/seatgen.py` + `seatspec1-3.py` generate `er5-seat.l4`; `work/casesgen.py` generates `er5-cases-seat.l4` (arguments and expected values written by hand in the script); `work/coverage.py`, `forks.md`, `notesgen.py` build NOTES.md.

## Peeked

I listed the names (not the contents) of the folders in `tb/eia/` once, by mistake, while checking a relative path. I opened no file of another piece.
