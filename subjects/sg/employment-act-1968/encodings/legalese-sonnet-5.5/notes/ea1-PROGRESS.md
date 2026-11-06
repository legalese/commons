# PROGRESS (ea1: Employment Act 1968, lines 785-2596, Parts 2 to 6)

Read this first after any compaction, then NOTES.md, then the text.
Status on 2026-11-05: everything below is written and checked, including the review round of 2026-11-05 (the rulings on periods, "where" and scope limits, and on delegated definitions, defences and "until" bars, a case for every seat question, and the bars as questions of their own); the only open item is the final report.

## Method (how the files are made)
- The source of the L4 layer-1 files is `work/src/*.in` (not shipped); `python3 -I work/tools/build.py <name>` expands `{{cite LABEL A B}}`, `{{quote A B}}` and `{{ref LABEL A B}}` into mechanically copied `-- src:N | text` lines and the `@ref` with computed locators, and writes the `.l4` file into the deposit folder. Edit the `.in`, not the `.l4`.
- The seat (`ea1-seat.l4`) is assembled by `work/seat/asm2.py` from `work/seat/seat-ab.l4`, `helpers-c.l4` and the generators `gen-c.py`, `gen-d.py`, `gen-e.py`; `ea1-cases-seat.l4` is written by hand.
- `work/tools/units.py` parses the text into coverage units (`work/units.tsv`); `work/dispo.tsv` holds each unit's disposition; `work/tools/coverage.py` writes the coverage table; `work/tools/notes.py` assembles NOTES.md from `work/notes/*.md` and generated tables (coverage, jural relations, marginal readings, check.sh output).
- `work/tools/lint.py` checks every quoted phrase of FALSE-kind / NOTHING-kind comments against the raw text; `work/tools/traces.py` prints FULFILLED or BREACH for each `#TRACE`; `work/tools/marginals.py` lists the marginal branches.
- Binaries: `$BASE/bin/l4-main-109` (1.6.109) and `$BASE/bin/l4-main-108` (1.6.108); `JL4_LIBRARY_PATH` unset.

## Status
- [x] Part 2a (ss 8-17): `ea1-part2a-termination.l4`, `ea1-tests-part2a.l4` (142 assertions + 2 traces)
- [x] Part 2b (ss 18-19): `ea1-part2b-continuity.l4`, `ea1-tests-part2b.l4` (98 + 2 traces)
- [x] Part 3a (ss 20-25): `ea1-part3a-payment.l4`, `ea1-tests-part3a.l4` (76 + 13 traces)
- [x] Part 3b (ss 26-34): `ea1-part3b-deductions.l4`, `ea1-tests-part3b.l4` (152 + 1 trace)
- [x] Part 4a (ss 35-41A): `ea1-part4a-rest-hours.l4`, `ea1-tests-part4a.l4` (179 + 3 traces)
- [x] Part 4b (ss 45-53): `ea1-part4b-benefits.l4`, `ea1-tests-part4b.l4` (100)
- [x] Part 5 (ss 54-64): `ea1-part5-truck.l4`, `ea1-tests-part5.l4` (51 + 3 traces)
- [x] Part 6 (ss 65-66): `ea1-part6-contractors.l4`, `ea1-tests-part6.l4` (62 + 5 traces)
- [x] Seat: `ea1-seat.l4` (214 questions), `ea1-cases-seat.l4` (506 assertions, a case for every question)
- [x] `SEAMS-ANSWERED.md`, `SEAMS-FOUND.md`; no `NEEDS-CORE.md` (nothing in the keel had to change)
- [x] `NOTES.md` complete; coverage with zero pending (378 rows, 1319 lines, 0 uncovered)
- [x] `check.sh`: 0 errors, 1366 satisfied, 0 failed, 0 refused, 21 modules, same on 1.6.108; `srcrefs.py check --refs` and `--strict` 0 problems; `lint.py` 0 not found; no warning or error in any `l4 run` on either build.
- No unstable second encoding (NOTES.md, `## Unstable dialect`).

## Decisions log
- P-DEF, P-IF, P-FLAT, P-DATE policies and the forks are in NOTES.md (`## Fork register (ea1)`).
- The seat gates Part 4 on `s 35 Part 4 applies to the employee` and answers `NOTHING` outside it.
- Seat inputs that are borrowed answers (S4, S6, S7) are amounts, 0 meaning unknown, which become `NOTHING`; the s 112 penalty questions always answer `NOTHING`.

## Files written
All under the deposit folder `encodings/legalese-sonnet-5.5/`: the eight modules, the eight test modules, `ea1-seat.l4`, `ea1-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`, `SEAMS-ANSWERED.md`, `SEAMS-FOUND.md`; `sgia-interpretation-time.l4` copied unchanged.
