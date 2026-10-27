# PROGRESS -- dg9

Piece dg9 of the Delaware General Corporation Law (8 Del. C. ch. 1): Subchapters X, XI and XII, sections 271 to 314, lines 1386 to 1631 of the raw text.
Both layers and NOTES.md are written; the checks below were run on the files as they stand.

## State

- Layer 1: five modules, `dg9-x-sale-of-assets` (ss 271-272), `dg9-x-dissolution` (ss 273-277), `dg9-x-winding-up` (ss 278-285), `dg9-xi-receivers` (ss 291-303), `dg9-xii-revival` (ss 311-314).
- Layer 1 tests: five files, `dg9-tests-*`, 733 assertions satisfied.
- Layer 2: `dg9-seat.l4` (145 questions in five groups) and `dg9-cases-seat.l4` (417 cases).
- `check.sh` (`L4_TARGET=unstable`, binary 1.6.98): 13 modules, 0 errors, 1150 assertions satisfied, 0 failed, 0 refused.
- `srcrefs.py check --refs`: 0 problems.
- NOTES.md carries all ten headings the brief names, in order.

## Method notes (how the files were made)

- Quote lines were copied mechanically from the raw text; the gate is `python3 -I srcrefs.py check --refs <raw> dg9-*.l4`.
- Tests and cases call rules with `WITH` named inputs; every expected value was written by hand from the text.
- The seat file and its cases were generated from a table of questions and hand-written cases; the generator and the table are not kept.

## Decisions taken (fork ids are in NOTES.md)

- Constitutive rules only (BOOLEAN, `MAYBE BOOLEAN`, DATE, NUMBER); no regulative `PARTY ... MUST` rules.
- Time limits are date comparisons on the core's `Period`; the last day is inside unless the text says otherwise.
- A judgment the text hands to the Court or an officer is a plain input; a case the text does not answer is NOTHING (`MAYBE`) and asserted.

## Files

dg9-x-sale-of-assets.l4, dg9-x-dissolution.l4, dg9-x-winding-up.l4, dg9-xi-receivers.l4, dg9-xii-revival.l4, dg9-tests-x-sale-of-assets.l4, dg9-tests-x-dissolution.l4, dg9-tests-x-winding-up.l4, dg9-tests-xi-receivers.l4, dg9-tests-xii-revival.l4, dg9-seat.l4, dg9-cases-seat.l4, NOTES.md, PROGRESS.md.
The keel's `dg-core.l4`, `check.sh` and `srcrefs.py` were already in the folder and are untouched.
