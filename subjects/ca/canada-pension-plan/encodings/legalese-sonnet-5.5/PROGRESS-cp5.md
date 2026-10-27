# PROGRESS: piece cp5

Working file for the cp5 agent. After a compaction, re-read this file, NOTES.md and the source ranges, not a summary.

## Toolchain

- L4_BIN: l4 (1.6.98)
- Check: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` in this folder (takes more than two minutes; run it in the background and read the output file).
- Source check: `python3 -I srcrefs.py check --refs ../../registers/source-bundle/R.S.C.-1985-c.-C-8.txt cp5-*.l4` (it also checks the Regulations locators `src:C.R.C.-c.-385:N` against the Regulations file in the same directory).

## WORKFLOW (important after a compaction)

- The `cp5-*.l4` files in this folder are BUILT from templates in the scratchpad: a scratch folder outside this folder (not committed: tools5)/src/<name>.l4.in
  A line `@@Q A B` in a template is replaced by the `-- src:N | text` quote lines of Act lines A..B; `@@QR A B` does the same for the Regulations.
  Edit the template, then run `python3 -I .../tools5/build.py <file.l4>`; never edit the built `.l4` by hand.
- `.../tools5/t.sh <file.l4>` runs one file and prints errors, warnings and the satisfied count.
- NOTES.md is assembled from `.../tools5/notes_text.py` (the prose sections) and `.../tools5/rowspec.py` (the coverage rows) by `assemble.py` and `fillrows.py`; the coverage rows are kept in NOTES.md itself between runs.

## State

Layer 1 (the Act's text, with the Regulations read where a section points to them): complete.
Layer 2: `cp5-seat.l4` (91 questions) and `cp5-cases-seat.l4` (179 assertions) complete.
NOTES.md: all ten headings written; the coverage table has 166 rows and none is `deferred`.
The final check.sh output is in NOTES.md under "What check.sh prints".

## Files

Layer 1: cp5-months.l4, cp5-d-retirement.l4, cp5-d-disability.l4, cp5-d-reinstatement.l4, cp5-d-death-survivor.l4, cp5-d-child.l4, cp5-d-post-retirement.l4, cp5-e-amount.l4, cp5-f-appeals.l4, cp5-g-general.l4, cp5-related-provisions.l4.
Tests: cp5-tests-months.l4, cp5-tests-d-retirement.l4, cp5-tests-d-disability.l4, cp5-tests-d-reinstatement.l4, cp5-tests-d-death-survivor.l4, cp5-tests-d-child.l4 (covers cp5-d-child and cp5-d-post-retirement), cp5-tests-e-amount.l4, cp5-tests-f-appeals.l4, cp5-tests-g-general.l4, cp5-tests-related-provisions.l4.
Layer 2: cp5-seat.l4, cp5-cases-seat.l4.
Notes: NOTES.md, PROGRESS.md.
