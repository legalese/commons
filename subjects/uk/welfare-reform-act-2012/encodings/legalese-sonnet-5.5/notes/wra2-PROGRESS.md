# PROGRESS (wra2)

Status at 4 November 2026: repair after the independent test review is done, including the one changed expectation of my own (see below).

## Done (verified by running, 4 November 2026)

- Layer 1: nine modules (`wra2-s44-jsa-commitment`, `-s46-jsa-sanctions`, `-s49-jsa-requirements`, `-s50-esa-entitlement`, `-s54-esa-commitment`, `-s57-esa-requirements`, `-s58-is-and-work`, `-part3`, `-sch`), each with a `wra2-tests-*` module; every one imports `wra-core` and `wra-definitions` (the brief governs over PLAN.md on this).
- Layer 2: `wra2-seat.l4` (63 questions) and `wra2-cases-seat.l4` (261 cases).
- `check.sh` with the stable 1.6.98 and the main 1.6.108: 22 modules, 1,407 assertions satisfied, 0 failed, 0 refused, 0 errors, every module "same" on main (the output is at the end of `NOTES.md`).
- `srcrefs.py check` and `check --strict`: 0 problems.
- `l4 check` notice grep (`follows code on its line|end of the file`) over all 20 `wra2-*.l4` files, both builds: 0.
- `NOTES.md`: coverage (957 rows, one disposition each; 967 lines in exactly one row), fork register (15), Hohfeld table (280 rows), marginal readings, "Reading a result: FALSE and NOTHING", seams, findings, what the text does not answer, what the stable binary does not accept, the seat, and the `check.sh` output.

## Where the sources are (not shipped)

`runs/iaw-wra2/work/`: `src/*.l4.in` (layer-1 sources; `%%REF cite :: N-M, N` lines expand to quote lines and `@ref`; build with `python3 -I expand.py src/NAME.l4.in`), `coverage.py`, `jural.py`, `jural_rules.py`, `build_notes.py` with `notes_part1.md` and `notes_part2.md`.
Do not re-run `gen_part3.py`, `gen_sch.py` or `gen_s57.py`: the `.in` files were edited by hand after generation.

## Decisions taken that the lead may want to overrule

- Fork readings F-44-1 to F-76-1 (listed with their licences in `NOTES.md`).
- Regulation-making powers and amendments of other Acts are inert 2; everything that states a limit a person can rely on, and every inserted operative text, is encoded.
- Seam 10 (which regime applies) is not taken as an input: the two regimes are separate modules.

## After the independent review (4 November 2026)

- Repaired the unknown-prescribed-age branch of `s 57 WRA2007 11E(1) the person falls within section 11E` (text line 1020: "a prescribed age (which may not be less than 3)"): a child under 1 gives `JUST FALSE`, aged 1 or 2 `JUST TRUE`, aged 3 or more `NOTHING`. No signature changed. Fork F-57-3, marginal reading 11, findings 12 and 13 in `NOTES.md`.
- 19 new assertions in `wra2-tests-s57-esa-requirements.l4` (lines 193 to 217) and 12 new cases in `wra2-cases-seat.l4` (lines 203 to 215).
- **Changed expectation of my own (1):** `wra2-tests-s57-esa-requirements.l4` line 192, `11E(1)` for a single person responsible for a child aged 2 with the prescribed age unknown: was `NOTHING`, now `JUST TRUE`, licensed by text line 1020 ("a prescribed age (which may not be less than 3)"). Edited after the lead's "edit 192"; only the expected value changed.
- Re-run after the edit: `check.sh` 22 modules, 1,407 satisfied, 0 failed, 0 refused, 0 errors, exit 0, every module "same" on main; `srcrefs.py check --refs` and `check --strict --refs` 0 problems (739 src: lines, 293 runs, 337 locators).
