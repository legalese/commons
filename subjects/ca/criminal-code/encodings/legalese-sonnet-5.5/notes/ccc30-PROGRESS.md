# PROGRESS.md -- ccc30 (Criminal Code (Canada), lines 17451-18463: Forms 1 to 23)

Status header: DONE, 2026-11-13, part agent `ccc30`. Every number below was printed by a command run in this session; `NOTES.md` carries the same numbers and the full `check.sh` table.

## What the range is (read, not assumed)
Lines 17451-18463 hold FORM 1 to FORM 23 and their sub-forms: 60 Forms (Forms 3, 13 and 14 shown repealed), 953 non-blank lines, 15,934 words. No section of the Act. The Schedule tariff ends at line 17449 (ccc29); Form 24 begins at line 18464 (ccc31). PLAN.md's "sections 1 to 9 (61 section headings)" is the heading detector reading numbered items inside Forms and the four lines quoting ss 487.0551 and 487.0552 (NOTES.md, Differences, item 3).

## Sections done
All of them: every non-blank line of the range is in exactly one row of the coverage table (314 rows: 108 encoded, 73 fork, 130 inert reason 2, 3 repealed), checked by `work/coverage.py`.

## Decisions taken
The readings taken are the forks F-A to F-X in the fork register of `NOTES.md` (each with the other reading and the words that license each). The disposition rule: a Form's recitals, identification and signature blocks, blank conditions and commands to officers are prescribed wording (inert, reason 2); its warnings, rights, limits, periods, "until"/"unless"/"only" conditions, quoted statute text and defined terms are rules (encoded).
Bugs the tests caught: (1) `NOT a OR b` parsed as `NOT (a OR b)` in Form 11 item 6 (fixed by bracketing); (2) a hand addition slip in a leap-year expected date (corrected by recomputing by hand, not from the output; recorded in NOTES.md finding 13).
Change after review: Form 7's unchecked dwelling-house box was first `JUST FALSE`; it is now `NOTHING` (fork F-V) and the two assertions and one seat case that asserted the first were rewritten from the text.

## Files written (all under DEPOSIT/encodings/legalese-sonnet-5.5/)
Layer 1: `ccc30-forms-register.l4`, `ccc30-forms-actors.l4`, `ccc30-forms-search.l4`, `ccc30-forms-preservation.l4`, `ccc30-forms-dna.l4`, `ccc30-forms-appearance.l4`, `ccc30-forms-warrants.l4`.
Tests: `ccc30-tests-forms-register.l4`, `-search.l4`, `-preservation.l4`, `-dna.l4`, `-appearance.l4`, `-warrants.l4`.
Layer 2: `ccc30-seat.l4` (44 `@export` questions), `ccc30-cases-seat.l4`.
Notes: `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`.
Scratch, not shipped (DEPOSIT/../work/): `build.py` (expands `@@SRC` markers into `src:` quote lines and `@ref`), `gen-*.py` (generators), `coverage.py`, `verify-quotes.py`, `forms.json`, `coverage.json`, `probe/`, `batch/`, `check.log`.

## Numbers
- `check.sh` (L4 1.6.110, main compared with 1.6.109): TOTAL 18 modules, 0 errors, 721 assertions satisfied, 0 failed, 0 refused; every module `same` on the main build. Baseline it replaced: the keel's three modules, 3 modules, 0 assertions.
- Traces: 38 `#TRACE` runs, outcomes identical on 1.6.110 and 1.6.109, and equal to the outcomes written in the comments above them.
- `srcrefs.py check --strict` over `ccc30-*.l4`: 256 src: lines, 213 runs, 220 locators, 0 problems (`--refs` the same).
- `work/verify-quotes.py`: 110 FALSE-kind and 137 NOTHING-kind comments, 216 quoted fragments all found in the text, 0 problems.
- `work/coverage.py`: 953 non-blank lines, 314 rows, 0 missing, 0 double-covered; 217 names defined, all cited by a row.
- Seat audit of 2026-11-12 (lead's request): 44 seat questions read against the functions they call; 7 retitled (1 direction, 6 subject; list in NOTES.md, "Seat audit of 2026-11-12"); 19 case assertions restated in place with `-- RECONCILED 2026-11-12: was ...`. `check.sh` after: TOTAL 18 modules, 0 errors, 721 satisfied, 0 failed, 0 refused, all `same` on 1.6.109 (before: identical); `srcrefs.py check --strict` and `--refs`: 0 problems.
- Name-test sweep of 2026-11-12 (lead's request): 49 layer-1 functions named with "may" or "authorized" (none with "permitted", "power" or "entitled"; 0 named "it is lawful", which is outside the sweep); 9 flipped to `NOTHING` (fork F-W), 21 kept `JUST FALSE` (9 closed by the text, 12 not named for a grant or a power), 1 listed ("may" with "in the case where", F-X), 0 "entitled"; 16 assertions restated in place with `-- RECONCILED 2026-11-12: was ...` (11 in the tests, 5 in `ccc30-cases-seat.l4`). `check.sh` after: TOTAL 18 modules, 0 errors, 721 satisfied, 0 failed, 0 refused, all `same` on 1.6.109 (before: identical); `srcrefs.py check --strict` and `--refs`: 0 problems; the list is in NOTES.md, "Name-test sweep of 2026-11-12".
