# Progress

This file states where the encoding stands.
It is rewritten as work lands.

## State

Status: draft; the encoding is complete for the scope in `BRIEF.md`.

- Layer 1 holds 16 modules, one per chapter or group of parts or kind of generated index, with 14 test files.
- Layer 2 holds `act-seat.l4` (24 questions) and `act-cases-seat.l4` (90 assertions).
- `check.sh` runs 32 modules on the stable build 1.6.98 and on the main build 1.6.110 and finds 0 errors, 2598 assertions satisfied, 0 failed and 0 refused, with the same four counts on both builds.
- `srcrefs.py check --refs` and `check --strict` report 1440 quotation lines, 672 runs, 673 locators and 0 problems.
- The coverage table in `NOTES.md` has 1142 rows (802 encoded, 270 inert, 52 fork, 18 out of scope), and no non-blank line of the in-scope text lies outside a row.
- The fork register in `NOTES.md` holds forks F1 to F16.

## Files

- `NOTES.md`: seat, jural relations, scope, coverage table, forks, what the Act turns out to say, worked cases, cross-references, the check output, and what would need doing before the encoding is relied on.
- `encoding.json` and `SOURCE-LICENSE.md`: the facts about this encoding and the terms of the quoted text.
- `act-provisions.l4` and `act-xrefs.l4` (with `act-tests-xrefs.l4`) are written by scripts that read the text file; quote lines and `@ref` locators in the other modules are written the same way.

## Decisions taken (and the text that licenses each)

- A period "from" or "after" a stated day does not include that day (s 151 (2), table 151 item 2); a period beginning "on" it does (item 1).
- A month is counted by the dictionary definition of month; N months are N successive months (fork F9).
- A year is a calendar year (dictionary: year, calendar year); a period of years is computed only where it begins on 1 January, and the other reading is a separate, labelled function (fork F10).
- s 151A applies to periods of every unit, because it speaks of "the last day of the period".
- The seat asks up to three days "that do not count" and uses them for public holidays, bank holidays and days an office is closed alike.

## Open

- None of the forks is ruled; each stands as the reading taken.
- The items under "What would need doing before this encoding is worth relying on" in `NOTES.md` are not done.
