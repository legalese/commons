# PROGRESS -- ssc7 (lines 3718-4330 of ukpga-1992-4.txt)

Status 2026-11-04: DONE, pending the lead's read.
Verified how: `check.sh` run in this folder after the last edit to any `.l4` file: 11 modules, 978 satisfied, 0 failed, 0 refused, 0 errors, and the same four counts on the main build 1.6.108 for every module (the output is pasted in `NOTES.md`, last section but one).
`srcrefs.py check --refs` and `--strict` over `ssc7-*.l4`: 449 `src:` lines, 182 runs, 182 locators, 0 problems.
The `#TRACE` outcomes (`FULFILLED`) of ss 171ZX(1), 171ZZ8(1) and 171ZZ18(1) were compared by hand on both binaries, because `check.sh` does not count them.

## Method (as it ended)

- Source of L4: `../../../work/src/*.l4.in` written by hand with `@@Q a b` placeholders; `../../../work/build.py` expands each placeholder to `-- src:N | text` lines copied mechanically from `inputs/ukpga-1992-4.txt` and writes the final `ssc7-*.l4` into this folder.
- Generated parts (Part 12ZC condition sets, the parallel tails of Parts 12ZC and 12ZE, the seat and its cases) come from scripts in `../../../work/` (`gen_zc.py`, `tr_zc_tail.py`, `compose_zc.py`, `gen_zc_rest_tests.py`, `tr_ze.py`, `gen_seat.py`, `gen_seat_cases.py`).
  `tr_ze.py` must not be re-run: it would overwrite hand edits made to `ssc7-12ze.l4.in` afterwards.
- Coverage table: `python3 -I ../../../work/coverage.py --md ../../../work/coverage-table.md` (rules in `coverage_rules.py`); `NOTES.md` is assembled by `python3 -I ../../../work/gen_notes.py` from `work/notes/*.md`, `coverage-table.md`, `jural.py`, `marginal.json` (from `extract_marginal.py`) and `check-final.txt`.
- Layer 1 modules: `ssc7-12zc.l4`, `ssc7-12zd.l4`, `ssc7-12ze.l4`, `ssc7-xiia.l4`; tests `ssc7-tests-*.l4`; seat `ssc7-seat.l4` (30 questions) and `ssc7-cases-seat.l4` (141 assertions).

## Decisions (the section that licenses each is in the fork register of NOTES.md)

- F1: ss 171ZU and 171ZV are "Regulations may provide that ... entitled": the Act states the conditions, a plain input says whether regulations so provide, `NOTHING` when not.
- F2-F13 are in the register with every reading.
- A `NOTHING` branch whose reason is "the prohibition or grant stops at its own words" is labelled `limited by its own wording`, not `silent`, so that the marginal-readings list (reading (b)) finds it; this was changed after the first full run (11 branches).

## Done

- [x] read BRIEF, PLAN, KEEL-NOTES, ENCODING-GUIDE, skills, source lines 3718-4330
- [x] Part 12ZD module and tests (164 assertions and a `#TRACE`)
- [x] Part 12ZE module and tests (147 and a `#TRACE`)
- [x] Part 12ZC module and tests (353 and a `#TRACE`)
- [x] Part XIIA module and tests (173), including the composition that answers seam S35
- [x] seat (30 questions) and seat cases (141); the cases found the s 171D(1) conflict flaw, fixed
- [x] coverage table (584 rows; audit 613 lines, 0 missing)
- [x] `NOTES.md` with all sections the brief names
- [x] gates: `check.sh`, `srcrefs.py` refs and strict, layout-message grep, FALSE-kind quote check, TRACE comparison

## Files written

`ssc7-12zc.l4`, `ssc7-12zd.l4`, `ssc7-12ze.l4`, `ssc7-xiia.l4`, `ssc7-tests-12zc.l4`, `ssc7-tests-12zd.l4`, `ssc7-tests-12ze.l4`, `ssc7-tests-xiia.l4`, `ssc7-seat.l4`, `ssc7-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`.
No `NEEDS-CORE.md` (no type or constructor the core lacks was needed).
Supplied and unchanged: `ssc-core.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`.

## Rebuild recipes

- One module: `python3 -I ../../../work/build.py ssc7-xiia`; everything: no names.
- 12ZC from its parts: `cd ../../../work && python3 -I gen_zc.py && python3 -I tr_zc_tail.py && python3 -I compose_zc.py && python3 -I build.py ssc7-12zc ssc7-tests-12zc` (this overwrites `work/src/ssc7-12zc.l4.in`).
- Run one file: `<l4-stable-98> run <file> 2>&1 | grep -E 'Severity|Message'`.
- Full gate, from this folder: `L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh`, then `python3 -I srcrefs.py check --refs ../../../inputs/ukpga-1992-4.txt ssc7-*.l4` and the same with `--strict`.
