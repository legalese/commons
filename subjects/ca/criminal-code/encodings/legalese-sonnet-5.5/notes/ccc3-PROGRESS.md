# PROGRESS.md -- ccc3 (Criminal Code (Canada), lines 1249-1903: Part II.1, Terrorism, ss 83.01 to 83.33)

Written by part agent ccc3, run dst-ccc3. After a compaction: re-read this file, `NOTES.md` and the text, not a summary.

## How the work is organised (read this first after a compaction)

- Scratch and scripts live in `../../work/` relative to this folder (`runs/dst-ccc3/work/`, not shipped).
- `work/src/*.l4` are the TEMPLATES of the layer-1 modules, their tests and the cases; `work/seat/*.l4` are the seat fragments (`work/mkseat.sh` joins them into `work/src/ccc3-seat.l4`); `work/cases_gen.py` writes `work/src/ccc3-cases-seat.l4`.
- `python3 -I work/build.py` expands the `@@Q/@@R/@@N/@@REC` placeholders into verbatim `-- src:` quotation lines and `@ref` lines and writes the `.l4` files here.
  Never edit a generated `.l4` in this folder by hand: the next build overwrites it.
- `work/rows.py` (the rows of the text), `work/coverage.py` (coverage table from the `-- COVERS:` lines and `work/inert.tsv`), `work/mark_forks.py` (fork marks on the COVERS lines), `work/lint.py`, `work/trace_check.py` (the `#TRACE` outcomes against their `-- EXPECT` comments), `work/namesweep.py` + `work/namesweep.tsv` (the name-test sweep), `work/seatparse.py` (the seat questions and their callees), `work/notes.py` + `work/notes/*.md` (assembles `NOTES.md`; run it last, it checks that each heading appears once).
- Gates: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` from this folder; `python3 -I srcrefs.py check --refs <raw text> <files>` and `--strict`; `python3 -I work/lint.py`; `python3 -I work/trace_check.py <files>` (with `L4_TRACE` set to each binary in turn).

## Status

- 2026-11-13: layer 1 (nine modules and their tests) and the seat layer (`ccc3-seat.l4`, `ccc3-cases-seat.l4`) written and green on 1.6.110 and 1.6.109.
- 2026-11-16 (resumed after the weekly-limit stop of 2026-11-12): baseline `check.sh` on both builds, 23 modules, 1457 satisfied, 0 failed, 0 refused, every module "same".
  Then: `NOTES.md` assembled by `work/notes.py`, `NEEDS-CORE.md`, the second seat-question audit pass and the name-test sweep of 2026-11-12 (see `NOTES.md`).
- 2026-11-16 (end of the resumed run): the sweep made four group (i) limbs answer JUST FALSE (`s 83.032(1)`, `s 83.13(2)`, `s 83.14(7)`, `s 83.3(13)`), the audit retitled 3 of 117 seat questions, and `check.sh` prints 23 modules, 1459 satisfied, 0 failed, 0 refused, every module "same" on 1.6.110 and 1.6.109; the other gates are in the final report and in the log below.

## Decisions taken (with the section that licenses each)

See the fork register of `NOTES.md`; forks F-ccc3-1 to F-ccc3-21.

## Files written

All under this folder: `ccc3-interpretation`, `-financing`, `-authorization`, `-listing`, `-freezing`, `-forfeiture`, `-participation`, `-proceedings`, `-recognizance` (`.l4`); the same nine as `ccc3-tests-<name>.l4`; `ccc3-seat.l4`; `ccc3-cases-seat.l4`; `NOTES.md`; `NEEDS-CORE.md`; this file.
The supplied files (`ccc-core.l4`, `ccc-definitions.l4`, `ccc-interpretation.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`) are not edited.

## Log (newest last)

- 2026-11-13 modules done and green on 1.6.110 and 1.6.109: interpretation (s 83.01), financing (ss 83.02-83.04), authorization (ss 83.031-83.0392), listing (ss 83.05-83.07), freezing (ss 83.08-83.12), forfeiture (ss 83.13-83.17), participation (ss 83.18-83.23, 83.231), proceedings (ss 83.24-83.27), recognizance (ss 83.3-83.33).
- 2026-11-13: seat layer written; five failing cases found: three wrong hand-written expectations, two exposing the s 83.3(8)(a)/(8.1) seam (fixed in layer 1, see NOTES.md Seams).
- 2026-11-16: resumed; baseline green; NOTES.md draft assembled before any `.l4` edit.
- 2026-11-16: sweep and audit applied; `NOTES.md` regenerated (25 headings, none twice); coverage 451 rows (inert 24, encoded 195, fork 217, repealed or blank 15), uncovered none.
