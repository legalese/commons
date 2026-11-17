# PROGRESS.md -- ccc15 (Criminal Code (Canada), lines 8524-8718, Part XIV Jurisdiction, sections 468 to 482.1)

Status (2026-11-16, part agent `ccc15`): everything the brief asks for is written, and every number below was produced by a command run after the last edit to a `.l4` file.
Commands: `check.sh` (target main, `l4` 1.6.110 against 1.6.109), `srcrefs.py check --refs` and `--strict` over every `ccc15-*.l4`, `work/lint.py`, `work/coverage.py`, and a diff of the `ccc15-tests-duties.l4` run output on the two builds.

## Done

- Layer 1: `ccc15-general.l4` (ss 468-475), `ccc15-special.l4` (ss 476-477.4), `ccc15-venue.l4` (ss 478-481.3), `ccc15-rules.l4` (ss 482, 482.1), `ccc15-duties.l4` (the regulative rules of ss 473(1.1), 474(1) and (2), 475(1)(b)(i), (ii), the proviso and (2), 478(1), 478(3), 479, 482.1(2) and (3)).
- Tests: `ccc15-tests-general.l4` (109 assertions), `ccc15-tests-special.l4` (138), `ccc15-tests-venue.l4` (98), `ccc15-tests-rules.l4` (99), `ccc15-tests-duties.l4` (17 assertions on rules whose gate is unmet, and 26 `#TRACE`s; a `DEONTIC` whose gate is met cannot be compared on the stable binary).
- Layer 2: `ccc15-seat.l4` (59 `@export` questions, each beginning "Under section N,") and `ccc15-cases-seat.l4` (198 assertions).
- `check.sh`: 659 assertions satisfied on both builds, 0 errors, 0 failed, 0 refused, all 15 modules `same`.
- `srcrefs.py check --refs` and `--strict`: 220 quotation lines, 63 runs, 103 locators, 0 problems.
- `work/lint.py`: 59 `FALSE-kind` and 138 `NOTHING-kind` branches, 226 quoted fragments, 0 problems; 59 seat questions, none without a case.
- `work/coverage.py`: 138 units, 191 non-blank lines, each covered exactly once; 88 encoded, 42 fork, 4 inert, 4 repealed.
- `#TRACE` output of `ccc15-tests-duties.l4`: identical on the two builds.
- NOTES.md: coverage table, fork register F1 to F21, name-test sweep, jural relations, marginal readings, seams, findings, what the binary does not accept, what the text does not answer, limits, the seat list, the seat-title audit, and the `check.sh` output verbatim.
  `work/notes_build.py` assembles it, and stops if a count in the prose differs from the code or a backticked name is not in the code.

## Not done

- The independent test pass (the brief forbids subagents, so none was used).
- `NEEDS-CORE.md`: nothing was missing from the core.

## Files

All under `DEPOSIT/encodings/legalese-sonnet-5.5/`: the modules above, `NOTES.md`, `PROGRESS.md`.
The sources the modules are assembled from (with the quotation lines inserted by script from the text) are in `DEPOSIT/../work/src/`, with `build.py`, `lint.py`, `coverage.py`, `notes_build.py` and `run.sh`.
