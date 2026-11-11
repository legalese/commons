# Progress

This file records where the encoding stands.
It is rewritten as the work moves.

## Method

- One agent working alone, from `BRIEF.md`, with the stable build 1.6.98 as the writing binary and 1.6.110 as the second build for `check.sh`.
- Sources: `../../registers/source-bundle/act-1954-003.txt` (plain-text rendering, not the official text).
- Layer 1 modules are written from templates in which a line `@@ref CITATION | N-M` is expanded into the quote lines of raw lines N to M and the `@ref` with its locator; the expanded files are the ones in this folder.
- The provision index, the cross-reference rows, the coverage table and the statements in `NOTES.md` are written by scripts that read the text and the module files.
  The scripts are kept outside this folder.

## Done

- `qld-interpretation-time.l4` (the time rules) and `qld-tests-time.l4`.
- `qld-provisions.l4`, `qld-xrefs.l4` and `qld-tests-xrefs.l4` (index of 1310 entries; 227 cross-references within the Act; 112 references to other instruments).
- Layer 1 modules and tests for Parts 1 to 14: `qld-part01` to `qld-part14` with `qld-tests-part01` to `qld-tests-part14` (Part 8 is in three groups, 8a, 8b, 8c; Part 12 is followed by 12A and 12B).
- Schedule 1: `qld-schedule1-table.l4` (every defined term) and `qld-schedule1-terms.l4` (terms that turn on a fact), with tests.
- Layer 2: `qld-seat.l4` (26 questions) and `qld-cases-seat.l4`.
- `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`.
- `check.sh` run over the folder with both builds; `srcrefs.py` run with `--refs` and with `--strict` over every `.l4` file.

## Next

- Nothing is left in scope.
  What would need doing before the encoding is relied on is listed in `NOTES.md`.

## Decisions taken, with the section that licenses each

- A period "beginning on a given day" excludes that day for every unit of period (s 38(1)); a period of calendar months begins at the beginning of the day after the given day.
- N calendar months are N calendar months in succession (Schedule 1, "calendar month", "month").
- A period of years is 12 calendar months for each year (Schedule 1, "calendar year" is a period of 12 months; "financial year" is a period of 1 year beginning on 1 July; s 15DA example).
- The rest-day rule of s 38(2) is applied to a last day however the period was counted.
- A period of weeks is not covered: the Act does not define "week".
- Where an "unless" or an "except" is met, the section answers NOTHING (case-by-case rule; the fork register in `NOTES.md` gives the other reading at each site).
- Where a grant or definition limited by a bare "if" is not satisfied, the section answers NOTHING; a "means" definition answers JUST FALSE outside it.
