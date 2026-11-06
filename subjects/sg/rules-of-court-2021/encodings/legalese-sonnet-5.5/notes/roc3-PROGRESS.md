# PROGRESS (roc3: Rules of Court 2021, lines 1405-2230; Orders 15, 16, 17, 18)

Written 2026-11-05 by part agent roc3 (Sonnet 5.5). The status words below are facts about the tree on that day.

## Done
- Layer 1: Order 15 (rules 1 to 29), Order 16, Order 17, Order 18 (rules 1 to 41), as eight modules with eight test files, and the regulative rules with 19 `#TRACE` runs.
- Layer 2: `roc3-seat.l4` (58 questions) and `roc3-cases-seat.l4` (149 assertions).
- `NOTES.md` (coverage 712 rows, fork register, jural relations, marginal readings, seams, findings), `NEEDS-CORE.md`.
- `check.sh` with both main builds: every module clean, assertions written equal to assertions satisfied (see NOTES.md for the numbers).
- `srcrefs.py check --refs` and `--strict`: 0 problems on every roc3 file.

## In progress
Nothing.

## Next
- The lead copies the E1, N2 and the two ruling bullets of 2026-11-05 (replacing mine with the guide's text) and the fork register into the merged NOTES.md and writes encoding.json.
- The lead wires the seam inputs of NOTES.md "Seams" at the merge.

## Method
- Layer-1 sources were written as `work/src/*.l4` with `--@ LABEL | N-M` directives; `work/build.py` expanded them (the quote lines come from `srcrefs.py quote`, so the quoted text is mechanical, and every quoted-words comment is checked against the text).
- The repeated rules of Order 18 were written from three templates by `work/gen18.py` and `work/asm18.py`; the seat was generated from the layer-1 signatures by `work/gen_seat.py`; the coverage rows by `work/units.py` and `work/map.py`.
  The `work/` folder is not shipped.

## Decisions taken (with the text that licenses each)
See the fork register in NOTES.md: forks 15.1 to 15.15, 16.1, 16.2, 17.1, 17.2, 18.1 to 18.9.
- Periods: where the text fixes a period in its own words, outside it the answer is `JUST FALSE` (brief, ruling of 2026-11-05 (a)); this differs from PLAN.md section 2.
- Timeliness is decided against the seam input `o 3 r 3 the last day for doing the act`; no part but roc1 counts days.

## Files written
`roc3-order-15-hearings.l4`, `roc3-order-15-evidence.l4`, `roc3-order-15-affidavits.l4`, `roc3-order-16.l4`, `roc3-order-17.l4`, `roc3-order-18-general.l4`, `roc3-order-18-lower.l4`, `roc3-order-18-higher.l4`, `roc3-regulative.l4`, the eight `roc3-tests-*.l4` files, `roc3-seat.l4`, `roc3-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`.
