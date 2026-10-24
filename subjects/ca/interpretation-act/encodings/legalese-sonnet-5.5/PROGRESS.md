# PROGRESS (row legalese-sonnet-5.5, Interpretation Act (Canada), R.S.C., 1985, c. I-21)

Updated: see the timestamp at the foot of this file.

## Plan (decided before any L4 was written)

1. NOTES.md first: coverage table (every section, subsection group and the Schedule), answer table with the EXPECTED values for the worked cases, written from the text before any module existed.
2. `ca-interpretation-time.l4`: the reusable time module (imports only `prelude` and `daydate`).
3. `ca-interpretation-calendar.l4`: ss 29, 35(1) "holiday" and "standard time" helpers (imports the time module).
4. `ca-interpretation-repeal.l4`: ss 2(2), 39(2), 42-46.
5. `ca-interpretation-rules.l4`: the other computable rules (ss 3, 8, 9, 11, 17, 19, 20, 22, 23(1), 25, 31, 32, 34, 36, 41(1) ...).
6. Tests: `ca-tests-*.l4`; deliberately failing expectations only in `ca-tests-red.l4`.
7. `check.sh` with `L4_TARGET=unstable` (the brief never names a target; it requires `REFUSE`, `@lang en` and `#ASSERT REFUSED`, which `main` does not read).
8. `encoding.json`, `SOURCE-LICENSE.md`, final report.

## Decisions taken (with the licensing text)

- Holidays, days of rest and recess are an INPUT (a function `DATE -> BOOLEAN`), never computed in the time module (brief).
- "From a day" and "after a day" exclude that day: s 27(4), s 27(5); s 28(b) for months.
- A year is twelve consecutive months (s 37(1)), so N years after a day is s 28 with 12N months.
- Weeks: the text has no provision (no occurrence of "week"); named REFUSE.
- Commencement: the day is s 5(2) / s 6(1); the moment is "the expiration of the previous day" (s 6(1), s 6(2)).
- s 26 moves the last day on which a thing may be done, not the period; it names "holiday" only (Saturday is not a holiday in s 35(1)).

## Sections done

All modules WRITTEN, typecheck clean (one Hint each: the linter says `@lang en` can go, which the brief requires, so it stays), `srcrefs.py check --strict` clean:

- `ca-interpretation-time.l4`: ss 2(1) "regulation", 5, 6, 7, 18(3), 23(2)(3)(5), 26, 27, 28, 30, 35(1) "month", 37, 39(1), weeks/service refusals.
- `ca-interpretation-calendar.l4`: s 35(1) "holiday" (the three days the text dates, the rest an input), "commencement", "standard time", "local time", s 29.
- `ca-interpretation-repeal.l4`: ss 2(2), 39(2), 43, 44, 46.
- `ca-interpretation-rules.l4`: ss 3(1), 8(1) 8(2) 8(2.1) 8(2.2) 8.2, 9, 11, 17, 19, 20, 21, 22, 23(1), 25(1), 32, 34, 35(1) "corporation" and "security", 41(1), Schedule, 35(2).
- Tests, all passing: `ca-tests-periods.l4` (193), `ca-tests-counting.l4` (73), `ca-tests-holidays.l4` (105), `ca-tests-commencement.l4` (60), `ca-tests-other.l4` (59), `ca-tests-rules.l4` (120), `ca-tests-repeal.l4` (53); `ca-tests-red.l4`: ten deliberately failing expectations, `expected_failed` = 10 in check.sh.
- check.sh: `expected_failed` set; the `srcrefs.py check --strict` step added (raw text from SRC_TXT or `../../source/`).

## Sections in progress

None. Everything in the plan is written.

## Done

- NOTES.md complete: sections 0 to 8 (source, what is encoded, coverage table of 94 rows, 36 forks, expected answers, answer table, the real check.sh output, open questions, process notes).
- `encoding.json` and `SOURCE-LICENSE.md` written; the licence question is recorded as open, not decided.
- `_probes/` deleted; no `zz-*.l4` left.
- Final check.sh run saved in `check-output.txt`: 12 modules, 663 satisfied, 10 failed (all in `ca-tests-red.l4`, expected 10), 0 refused, 0 other errors; srcrefs gate 381 quotation lines, 0 problems; exit 0.

## Next

Nothing, for this run. Final report to the team lead.

## Files written

BRIEF.md (copy of the brief), check.sh and srcrefs.py (from the encoding-a-subject skill; check.sh edited as above), requote.py, the four modules and eight test files, NOTES.md, encoding.json, SOURCE-LICENSE.md, check-output.txt, this file.
last update: 2026-10-21 (after the final check.sh run)
