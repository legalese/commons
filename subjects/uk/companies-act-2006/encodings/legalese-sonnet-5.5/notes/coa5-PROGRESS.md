# PROGRESS (coa5): Companies Act 2006, lines 2697-3566 (ss 205 to 269)

Read this first after any compaction, then `NOTES.md`, then the text.

## State: DONE

- Layer 1, ten modules, each with a test file: all written, all tests satisfied (1,764 assertions satisfied in all, 0 failed, 0 refused; 27 `#TRACE`s, each matching its `-- TRACE EXPECT:` comment on 1.6.110 and on the main build 1.6.109).
- Layer 2: `coa5-seat.l4` (239 questions in 69 sections) and `coa5-cases-seat.l4` (498 cases, all satisfied).
- `NOTES.md` is assembled (coverage 817 rows with no TODO; fork register; rulings; jural relations; marginal readings; reading a result; seams; eight numbered findings; what the stable binary does not accept; what check.sh prints).
- `check.sh` (target main, 1.6.110 against 1.6.109): 24 modules, 0 errors, 1,764 satisfied, same on main, exit 0.
- `srcrefs.py check --refs` and `--strict`: 910 src lines, 357 locators, 0 problems.

- Seat audit of 2026-11-12 (team lead's request): 239 questions read, 23 mismatched (13 direction, 10 subject), 21 renamed and 2 `@export` texts corrected; 47 assertions restated in place with `-- RECONCILED 2026-11-12`; layer 1 untouched; details in `NOTES.md`, "Seat audit of 2026-11-12".
- Name-test sweep of 2026-11-12: 9 grant-named functions flipped to NOTHING (F-NT-1 to F-NT-9), 16 kept JUST FALSE (gate closed by the text), 0 "may" with where/when/upon, 8 "entitled" listed (F-NT-E1 to F-NT-E8); 20 assertions restated in place; details in `NOTES.md`, "Name-test sweep of 2026-11-12".

## Files in this folder

Layer 1: `coa5-loans-exceptions.l4` (205-214), `coa5-loss-of-office.l4` (215-222), `coa5-ch4-supplementary.l4` (223-226), `coa5-quoted-company-pay.l4` (226A-226F), `coa5-service-contracts.l4` (227-231), `coa5-director-liabilities.l4` (232-239), `coa5-residential-addresses.l4` (240-246), `coa5-director-supplementary.l4` (247-249, 258, 259), `coa5-director-definitions.l4` (250-257), `coa5-derivative-claims.l4` (260-269); tests `coa5-tests-<same name>.l4`.
Layer 2: `coa5-seat.l4`, `coa5-cases-seat.l4`.
Notes: `NOTES.md`, `PROGRESS.md`.
Supplied and not edited: `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `coa-core.l4`, `coa-definitions.l4`.
No `NEEDS-CORE.md`: no type or constructor the core lacks was needed.

## Decisions that a later reader might undo (each is in the fork register with its licensing text)

F-205-1, F-UNLESS-1, F-MUST-1, F-210-1, F-211-1, F-213-1, F-213-2, F-218-1, F-219-1, F-220-1, F-222-1, F-228-1, F-228-2, F-232-1, F-246-1, F-250-1, F-209-1, F-261-1, F-263-1, F-263-2, F-265-1.
Two readings of mine changed during the run because the text said otherwise: s 254(2) now needs equity share capital above nought (finding 6); the seat questions of s 247(3) and s 249(1) were rewritten after a case disagreed with my first reading (s 247(3) speaks only of charities; a failed "if purporting to be authenticated" is JUST FALSE).

## Working method (scratch scripts under `../../../work/`, not shipped)

`work/src/*.l4.in` (the module sources, with `-- @QUOTE N-M` lines expanded to quote lines by `expand.py`), `build.sh`, `coverage.py` and `coverage-map.tsv`, `tracecheck.py`, `gen11.py` and `gentest11.py` (Part 11), `seatlib.py` and `genseat_*.py` (the seat layer and its cases), `assemble.py` (NOTES.md).
