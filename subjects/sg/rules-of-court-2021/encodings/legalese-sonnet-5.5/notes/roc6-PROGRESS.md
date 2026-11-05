# PROGRESS (roc6)

State at this write (5 November 2026): all deliverables are written and checked, after a second pass that followed an independent test pass and the rulings of 2026-11-05 (`## What the second pass changed` in `NOTES.md`).

- Layer 1: `roc6-order-23.l4`, `roc6-order-24.l4`, `roc6-order-24a.l4`, `roc6-order-25.l4`, `roc6-order-26.l4`, `roc6-order-27.l4` (Orders 23 to 27, lines 3556 to 4193 of the raw text).
- Tests: `roc6-tests-order-23.l4` to `roc6-tests-order-27.l4`.
- Layer 2: `roc6-seat.l4` (39 `@export` questions for a party to a civil action) and `roc6-cases-seat.l4` (103 cases).
- `NOTES.md`: coverage table (523 rows), fork register (with F-MUST, F-ASSUMED and F-UNSURE), jural relations, marginal readings, reading a result, seams, dependencies, unstable dialect, findings, what the main binary does not accept, and the `check.sh` output.
- `NEEDS-CORE.md`: a years unit and a reference to a rule.

What the last run of `check.sh` printed is at the end of `NOTES.md`.
The file is regenerated from the files by a script in the working area (not shipped); if a layer-1 file changes, the coverage, fork-row and marginal-reading tables in `NOTES.md` have to be regenerated and `check.sh` run again.

Not done, on purpose: no second, unstable encoding (see `## Unstable dialect` in `NOTES.md`); no `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` or `README.md` (the lead writes those).
