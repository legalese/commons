# Progress

Read this file, NOTES.md and the text again after any compaction.
The scripts that build the generated parts are kept outside the deposit; this file records what each deposited file is and what was decided.

## Done
- `lga-provisions.l4` and `lga-xrefs.l4`: written by script from the text file; 112 index entries; 304 references to provisions of this text and 17 to other instruments; every row resolves; 115 and 323 assertions.
- `lga-time.l4` and `lga-tests-time.l4`: every date, period and sitting-day count the in-scope text states; 204 assertions.
- `lga-nouns.l4`, `lga-defs.l4` and `lga-tests-defs.l4` (ss 4, 5, 6, 8 to 11): 147 assertions.
- `lga-instruments.l4` (ss 12 to 14): 90 assertions.
- `lga-register.l4` (ss 15A to 15L): 194 assertions.
- `lga-compilations.l4` (ss 15P to 15X): 173 assertions.
- `lga-authorised.l4` (ss 15Z to 15ZB): 98 assertions.
- `lga-drafting.l4` (ss 16, 17, 19): 25 assertions.
- `lga-scrutiny.l4` (ss 38 to 48): 109 assertions.
- `lga-repeal.l4` (ss 48A to 48E): 50 assertions.
- `lga-sunset.l4` (ss 50 to 54): 82 assertions.
- `lga-seat.l4` (47 questions, each with `@export`, each input with `@desc`) and `lga-cases-seat.l4` (176 cases).
- `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`.

## In progress
Nothing.

## Next
- A domain expert reads every rule against the authorised text.
- Each fork in the fork register is ruled on.

## Method
Each module is written as a template; a script copies the quote lines from the text file with `srcrefs.py` and expands the `@@Q` and `@@R` directives into `-- src:` lines and `@ref` lines.
Each test file is written by a script from expected values typed by hand from the text, never from the encoding's own output.
The coverage table, the jural table, the fork-site list and the cross-reference counts in `NOTES.md` are generated from the modules, the text and a table of declared dispositions, and the script checks that every non-blank line of the text falls in exactly one coverage row.
The binary is the stable build, 1.6.98; `check.sh` compares every module with 1.6.110.

## Decisions taken, with the provision that licenses each
- "N days after E" excludes E and "within" includes the last day (ss 15R(3), 15T(2), 46(2)): fork F01.
- "N months after D" and "the Nth anniversary": the same day number; where the text does not say which day is meant the answer is NOTHING (ss 48(1), 50(1)): fork F02.
- Sitting days of a House are an input calendar; the first sitting day after the event is day 1 (ss 38(1), 39(2), 15DA(2), 42(1)): forks F03 and F04.
- The later of the two Houses' last days where a copy was not laid before both (ss 38(3), 46(2)(c)): fork F05.
- Events in ss 48A to 48D are instants: a commencement or registration at the start of its day, the end of the last day of disallowance at the end of that day: fork F08.
- A permission, deeming or effect introduced by "if", "where", "when" or "unless" answers JUST FALSE when the condition fails; a duty or a bar whose condition fails answers NOTHING: fork F09, with every site listed in `NOTES.md`.
- Section 8: subsection (8) first, then (2) and (3), then (6) displacing (4) and (5) only (s 8(6) and (7)): fork F17.
- The first possible day in s 52(1) is an input: fork F18.

## Files
`lga-*.l4` (the modules and their tests), `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `PROGRESS.md`; `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` and `BRIEF.md` were already present and are unchanged.
