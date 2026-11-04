# PROGRESS (snap6)

Updated as work lands; re-read this file, NOTES.md and the text after any compaction, not a summary.

## Baseline the gate replaced

Before this work `check.sh` printed 1 module (snap-core.l4), 0 errors, 0 assertions satisfied, 0 failed, 0 refused.

## Final state: all deliverables written, gate green

`L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` printed 15 modules, 0 errors, 1628 assertions satisfied, 0 failed, 0 refused, and the same four counts on the main build for every module (exit 0). The full output is at the end of NOTES.md.

| section | module | tests (satisfied / failed / traces) |
| --- | --- | --- |
| s 2026 | `snap6-s2026.l4` | `snap6-tests-s2026.l4`: 575 / 0 / 39 |
| s 2031 | `snap6-s2031.l4` | `snap6-tests-s2031.l4`: 478 / 0 / 19 |
| s 2033 | repealed; no module (a coverage row only) | none |
| s 2034 | `snap6-s2034.l4` | `snap6-tests-s2034.l4`: 123 / 0 / 3 |
| s 2035 | `snap6-s2035.l4` | `snap6-tests-s2035.l4`: 96 / 0 / 6 |
| s 2036 | `snap6-s2036.l4` | `snap6-tests-s2036.l4`: 66 / 0 / 3 |
| s 2036a | `snap6-s2036a.l4` | `snap6-tests-s2036a.l4`: 167 / 0 / 10 |
| seat | `snap6-seat.l4` (41 questions) | `snap6-cases-seat.l4`: 123 / 0 |

80 traces in all: 75 print `FULFILLED`, and 5 are deliberate breaches that print `BREACH BY ...` (s 2031 lines 655, 662, 689; s 2035 lines 171, 183), each with an "Expected: BREACH" comment. Stable and main print identical outcomes for all six tests files.

Strict source locators (`srcrefs.py check --refs` and `--strict`) over every snap6 `.l4` file: 1356 `src:` lines, 599 runs, 331 locators, 0 problems.

Coverage audit (`work/coverage.py`): 533 units, 533 rows, 652 non-blank lines in the ranges, 0 uncovered, 0 in two rows, 0 unmapped. Encoded 416, fork 49, inert (reason 1) 67, repealed 1.

## Other deliverables

`NOTES.md` (assembled by `work/notes.py` from `work/notes/*.md`, the coverage table, `SEAMS.md`'s ASKS and the gate log), `SEAMS.md`, `NEEDS-CORE.md`.

## Work folder (not shipped): `../work/`

`build.py` (expands `src/*.l4.in` into the deposit), `units.py` / `units.txt` (the text units), `coverage.py`, `results.py` / `results-main.py` (trace outcomes and assertion counts), `gen_touch26.py`, `gen_seat.py` with `seat/specs.py`, `sigs.py`, `seams.py`, `notes.py`, `map/*.map` (the disposition of each unit), `notes/*.md`, `src/` (sources of every .l4 file), `probe/` (stable and main trace outputs), `check-final.log`. No binaries are kept there.

## Decisions taken (the section that licenses each is in NOTES.md, fork register)

FR-26-1 to FR-26-4, FR-31-1 to FR-31-12, FR-34-1, FR-35-1 to FR-35-4, FR-36-1 to FR-36-4, FR-36a-1 and FR-36a-2.
Assumed, not ruled: a time bound on a duty ("not later than", "within 40 days") and a positively phrased cap ("up to") are read as the text's no (marginal reading (a)); every such branch is listed in NOTES.md.

## Remaining

Nothing in this part's brief. Open for the lead: wire the seam inputs at the merge (`SEAMS.md`), hoist the constructors in `NEEDS-CORE.md`, and a lawyer's ruling on the marginal readings.
