# PROGRESS: piece ei7 (Act lines 3599-4201)

Working log. Re-read this, NOTES.md and the text after any compaction, not a summary.

## Working method

- Source lines are quoted by script: the `.l4.in` sources live in `inputs/gen/` (marker lines `--%Q N M`); `inputs/gen/build.sh` runs `expand.py`, which writes the `.l4` in this folder using `srcrefs.py quote`.
  Edit the `.l4.in` and re-run `build.sh`; never hand-edit a quote line.
  The tests and the seat files (`ei7-tests-*.l4`, `ei7-seat.l4`, `ei7-cases-seat.l4`) are written directly in this folder.
- Rule names for provisions in this range begin `Act RP <amending Act citation> s. N(M) ...` (RP = related provision) so that they cannot clash with er6, which meets the same amending provisions in the Regulations' file (2009 c. 2 s. 226 and 2009 c. 30 s. 7 appear in both files).
- Types and constructors begin `ei7 `.
- The 20 amendments not in force (src:4003-4201) are all `inert`: no module; they are in the coverage table only.

## Status (2026-10-24, final)

ALL DONE. Nothing is in progress.
Final check.sh after the last .l4 edit: 0 errors, 509 assertions satisfied, 0 failed, 0 refused (19 modules; the 4 eia-core modules unchanged and not counted in the 509's source); srcrefs --refs over ei7-*.l4: 369 src lines, 53 runs, 161 locators, 0 problems; no `l4 check` warning on any ei7 file.
NOTES.md is generated (inputs/gen/notes_build.py from notes_rows.py and checkout.txt): 141 coverage rows (89 encoded, 51 inert, 1 fork) over 90 block headings + 2 division headings; 16 forks F1-F16; 69 seat questions in 8 groups, each with at least one case.
The advisor was rate-limited and could not be consulted; the self-review was: every definition has an @ref, every question has @export, @desc on every input and a case, every line of 3599-4201 lies in exactly one coverage row, mutation spot checks (changing AT LEAST to GREATER THAN in two rules) made tests fail, then were reverted by rebuilding from the .in sources.

## Decisions taken (each with the text that licenses it)

- A related provision that picks the version of the Act for a benefit period, a week or a claim is encoded, however old its dates, because it still decides which text governed a past period (the consolidation is current to 2026-09-30). Source: the brief ("Encode a related provision for what it still decides for a person").
- Provisions about government accounts, audits, office tenure and regulation-making are `inert` (machinery; `spent` named where every date is past): 2008 c. 28 s. 122; 2010 c. 12 ss. 2195-2200; 2012 c. 19 ss. 263, 264; 2012 c. 31 s. 456; 2016 c. 7 ss. 228, 229. 2018 c. 12 s. 292(1) and 2021 c. 23 s. 331 are `inert` as pure pointers at the Act's definitions.
- A day fixed by an order of the Governor in Council, or "the day on which this Act comes into force" of an amending Act, is not in the inputs: each is a DATE input with a comment, listed in NOTES under cross-references.
- The 2021 c. 23 bands (before Sep 27 2020; to Sep 25 2021; Sep 26 2021 to Sep 24 2022; Sep 25 2022 on) are one enum and one rule, read by ss. 332 to 335 and 2022 c. 10 s. 411.
- The entry labelled 2026, c. 22, s. 39 (src:4196-4201) repeats word for word the body of ss. 38(1), (3), (4) (src:4189-4194), including its opening "38 (1)"; recorded as a finding, no guess at what s. 39 says.

## Files written

ei7-related-nouns.l4, ei7-related-2003-2010.l4, ei7-related-2012-tribunal.l4, ei7-related-2012-2015.l4, ei7-related-2016-2018.l4, ei7-related-2018-elections.l4, ei7-related-2020-2023.l4, ei7-tests-related-{2003-2010,2012-tribunal,2012-2015,2016-2018,2018-elections,2020-2023}.l4, ei7-seat.l4, ei7-cases-seat.l4, NOTES.md, PROGRESS.md.
Sources and tools (not part of the deposit): inputs/gen/*.l4.in, expand.py, build.sh, probe-a.l4.
