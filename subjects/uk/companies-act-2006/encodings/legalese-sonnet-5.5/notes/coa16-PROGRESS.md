# PROGRESS (coa16: Companies Act 2006, lines 9669-9961, Parts 19 and 20, ss 738 to 767)

Written for a reader who has lost the context: re-read this file, NOTES.md and the text, not a summary.

## Working method (so the work can be resumed)
- Scratch lives in `../../../work/` (not shipped): `src/*.l4.in` are the templates; `build.py` expands the `{{Q a b}}` lines into the `-- src:` quote lines of lines a..b of `inputs/ukpga-2006-46.txt` (via `srcrefs.py quote`, never retyped) and writes the `coa16-*.l4` here; `coverage.py` + `coverage-map.tsv` build the coverage table into NOTES.md between the COVERAGE markers (`coverage.py render`) and audit it (`coverage.py audit`).
- Edit the templates in `work/src/`, not the generated `coa16-*.l4` files here (they are overwritten by `build.py`).
- Run: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh`; srcrefs: `python3 -I srcrefs.py check --strict ../../../inputs/ukpga-2006-46.txt coa16-*.l4`.

## Decisions taken (with the provision that licenses each)
- Layer 1 imports `coa-definitions` (which brings `coa-core`) and CALLS the keel's `s 4(1)`, `s 4(2)`, `s 4(3)` (public and private company, from a `Company profile`); where a keel answer needs a list or a calendar (`s 1166`, working days) or belongs to another part (`s 1121` officer in default, `s 112` member, `s 1136`, `s 2(1)`) it is an input. (Brief governs over PLAN.md section 4.1, which says parts cannot import the definitions module.)
- Working days (s 745(1)): the count of working days is an input (the caller counts them with the keel's `s 1173(1)`).
- Signposts: s 741(4), s 766(5) inert reason 1 (as the keel's fork F7); ss 763(2) to (5), 764, 766 order- and regulation-making powers inert reason 2, except where the text fixes a sum the person is affected by.

## Status (update after each step)
- DONE (2026-11-13): layer 1 (five modules + five tests files), layer 2 (`coa16-seat.l4`, 57 `@export` questions in five `§` groups; `coa16-cases-seat.l4`, 141 assertions), coverage table (303 rows: encoded 168, fork 75, inert 60; every non-blank line of 9669-9961 in some row), NOTES.md (all sections the brief names), final `check.sh` on 1.6.110 and 1.6.109: 14 modules, 690 assertions satisfied, 0 errors, 0 failed, 0 refused, every module `same` on main; srcrefs `--refs` and `--strict`: 271 src lines, 29 runs, 150 locators, 0 problems; traces (all tests files and the seat cases) byte-identical on both builds.
- NOT DONE: nothing owed. `NEEDS-CORE.md` was not written (no core type or constructor was missing).
- To resume or rebuild: edit `work/src/*.l4.in`, run `python3 -I work/build.py <module>`, `python3 work/make-map.py` then `python3 -I work/coverage.py render`, then `python3 work/make-notes.py` (it keeps the rendered coverage block); `notes-static.md` is the source of the prose sections of NOTES.md.
- Forks: the register in NOTES.md carries F1 to F38 (F1 to F19 are cited in the module comments; F20 to F31 are cited by the coverage rows and the marginal-readings table; F32 to F38 are the rows of the name-test sweep table).
- DONE (2026-11-12 instructions, run 2026-11-13): second seat-question audit pass (20 of 57 retitled, subject only; see NOTES.md "Second seat-question audit pass") and the name-test sweep (0 flipped, 3 kept, 7 + 1 listed; see NOTES.md "Name-test sweep of 2026-11-12"). Only `coa16-seat.l4`, `coa16-cases-seat.l4`, NOTES.md and this file changed; check.sh TOTAL 690 satisfied before and after.
