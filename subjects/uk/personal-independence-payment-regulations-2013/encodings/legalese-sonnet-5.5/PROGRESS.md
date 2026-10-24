# PROGRESS (encoding agent `pip`, Social Security (Personal Independence Payment) Regulations 2013)

## Status

Finished first pass, unreviewed.
Layer 1 (15 rule modules, 11 test files), layer 2 (`pip-seat.l4` with 80 questions, `pip-cases-seat.l4` with 453 cases) and `NOTES.md` (every heading filled) are written.
The author's scratch folder (the templates from which the rule modules were generated, the build script, the per-file counter and the coverage checker) was deleted at the end; the `.l4` files, `NOTES.md` and this file are the deliverable.

Files: `pip-nouns`, `pip-dates`, `pip-part1-general`, `pip-sch1-definitions`, `pip-sch1-daily-living-table`, `pip-sch1-mobility-table`, `pip-part2-assessment`, `pip-part3-required-period`, `pip-part4-residence`, `pip-part4-special-cases`, `pip-part5-rates`, `pip-part6-age`, `pip-part7-periods`, `pip-part7-payability`, `pip-sch2-forces`, `pip-seat`.
Tests: `pip-tests-part1`, `pip-tests-sch1-definitions`, `pip-tests-sch1-tables`, `pip-tests-part2`, `pip-tests-part3`, `pip-tests-sch2`, `pip-tests-part4-residence`, `pip-tests-part4-special-cases`, `pip-tests-part5-6`, `pip-tests-part7-periods`, `pip-tests-part7-payability`.
Cases: `pip-cases-seat`.
Provided and unchanged: `check.sh`, `srcrefs.py`.

## Last gates run (the last edits to any `.l4` came before them; after them only `NOTES.md` and this file changed)

- `L4=<stable 1.6.98 binary> L4_TARGET=unstable ./check.sh`: 28 modules, 0 errors, 1633 satisfied, 0 failed, 0 refused (output verbatim in `NOTES.md`, "What check.sh prints").
- `python3 -I srcrefs.py check --refs ../../registers/source-bundle/uksi-2013-377.txt pip-*.l4`: 0 problems (621 src lines, 272 runs, 347 locators).
  `--strict` reports 66 problems and is not claimed.
- `l4 check` on every `pip-*.l4`: no diagnostic; `l4 run` on every `pip-*.l4`: 0 linter warnings.

## Still open (for whoever reviews this)

- The forks in `NOTES.md` have not been ruled on.
- The deposited text is a converter's rendering, not the official text, and one amendment to Schedule 1 Part 3 is listed as unapplied in its metadata.
- Nobody but the author has run the cases.
- The seat has not been through the Interact form.
