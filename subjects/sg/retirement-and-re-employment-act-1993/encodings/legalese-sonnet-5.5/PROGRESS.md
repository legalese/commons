# PROGRESS (iaw-rra: Retirement and Re-employment Act 1993, Singapore; encoding legalese-sonnet-5.5)

Read this first after any compaction, then NOTES.md, then the text (inputs/RRA1993.txt, 1,390 lines).

## Paths (do not retype from memory)
- INPUTS_DIR = <run>/inputs
- DEPOSIT   = .../runs/iaw-rra/deposit ; this folder = DEPOSIT/encodings/legalese-sonnet-5.5
- L4_BIN  = <bin>/l4-main-109 (1.6.109) ; L4_MAIN = <bin>/l4-main-108 (1.6.108)
- unstable (optional second encoding only) = <bin>/l4-unstable-1104
- DEPOSIT/probes/ is scratch: delete before the final report.

## Tools in this folder
- `python3 -I fillquotes.py RAW FILE...` expands `-- @@QUOTE N-M` placeholder lines into `-- src:N | text` quote lines (copied from the raw text by srcrefs.py).
- `python3 -I coverage.py audit RAW` / `write RAW NOTES.md`: the ROWS block in coverage.py is the single source of truth for the coverage table and the jural-relations table; rules are found in the .l4 files by name prefix (`s 4(2) ...`).
- `L4=.. L4_MAIN=.. python3 -I trace-check.py`: every #TRACE needs a `-- TRACE-EXPECT: FULFILLED|BREACH|RESIDUAL` line above it; both builds must print it.
- `python3 -I srcrefs.py check --refs RAW *.l4` must say 0 problems.

## Conventions decided
- Layer 1 rules take plain inputs / the `Employment` record; no section GIVEN (rejected on main). Every decision answers `MAYBE BOOLEAN` (JUST TRUE / JUST FALSE / NOTHING) via rra-logic.l4 helpers.
- Rule names begin with the citation: `s 4(2) ...`; a paragraph rule begins `s 7(1)(a) ...`. Each FALSE branch carries `-- FALSE-kind (the text says no in its own words): "..."`, each NOTHING branch `-- NOTHING-kind (<why>)`.
- Dates: `Date day month year`; calendar months by daydate `add months` (clamps 31 Jan to 28/29 Feb; fork F3).
- Regulative rules: `#TRACE` + `-- TRACE-EXPECT:`; each has a decision-function twin that is asserted (a DEONTIC cannot be asserted on main).
- Test files: rra-tests-*.l4 (layer 1), rra-cases-seat.l4 (layer 2). Seat: rra-seat.l4.

## Status
COMPLETE (2026-11-05). Everything below is on disk and was last run after the final edit to any .l4 file.
- Layer 1: rra-logic, rra-nouns, rra-part1-preliminary (ss 2, 3), rra-part2-minimum-retirement-age (ss 4, 6), rra-part3-re-employment (ss 7-7C), rra-part4-remedies (ss 8-8C), rra-part5-general (ss 9-13); tests rra-tests-part1..5.
- Layer 2: rra-seat.l4 (77 questions), rra-cases-seat.l4 (228 assertions).
- check.sh: 14 modules, 0 errors, 742 satisfied, 0 failed, 0 refused; main columns (1.6.108) the same for every module.
- trace-check.py: 27 traces, 54 outcomes (2 builds), 0 problems. srcrefs.py check --refs: 0 problems. coverage.py audit: AUDIT OK (208 rows, 159 rules).
- NOTES.md, encoding.json, SOURCE-LICENSE.md written. NOTES tables are generated: `python3 -I coverage.py write RAW NOTES.md` and `python3 -I marginal.py NOTES.md`.
- No second (unstable) encoding was written; NOTES.md says so under "Unstable dialect" and names the main-build workaround.
- fillquotes.py is kept: it is the quote expander (all placeholders are expanded).
