# PROGRESS (iaw-wa: Interpretation Act 1984 (WA), whole, Sonnet 5.5 solo)

Read this first after any compaction, then NOTES.md, then the text (../../registers/source-bundle/mrdoc_49111.txt, 1118 lines).

## Paths
- DEPOSIT dir (this folder): /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-wa/deposit/encodings/legalese-sonnet-5.5
- scratch work (probes, templates, build scripts) lives in `scratch/` UNDER this folder's parent `deposit/`, i.e. deposit/scratch/ (brief: write only under DEPOSIT). Delete deposit/scratch at the end.
- L4_BIN (stable 1.6.98, sha256 82ea44ad...): .../scratchpad/bin/l4-stable-98 ; L4_MAIN (1.6.102): .../scratchpad/bin/l4-stable-102

## Plan (modules; flat folder; all names distinct across modules)
1. wa-interpretation-time.l4   imports ONLY prelude + daydate. Defines YMD shim. ss 20,21,22,23,25(3),27,41,42 timings, 48A, 61, 62, 63, 64, 75 time of deemed service, s 5 year/month/financial year, Second Schedule B-E (1918 Act, via s 77(4)).
2. wa-interpretation-nouns.l4  shared types (no rules)
3. wa-interpretation-part1-3 ... one module per Part (see below)
4. wa-interpretation-s5-definitions.l4 generated defined-term table
5. wa-seat.l4 + wa-cases-seat.l4 (layer 2)
6. wa-tests-*.l4 test files, check.sh, srcrefs.py, NOTES.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md

## Decisions taken (with licensing text)
- (to fill)

## Facts learned about the stable binary (98 and 102 agree)
- mixfix definitions: parameter ORDER in GIVEN must equal the order the params appear in the name; name phrase first then params works.
- `Day (x's field)` needs parentheses (function application binds tighter than genitive).
- no `find`/`head`/`length`/`last`; use filter + `WHEN c FOLLOWED BY rest` / `WHEN EMPTY`. CONSIDER cannot be inlined in a one-line #ASSERT: use helper functions.
- constructor patterns bind positionally: `WHEN `ctor` x THEN` (no WITH).
- YMD shim `Date d m y` fine on both builds; `add months` clamps; `is weekend` ok on DATE.
- chk script: deposit/scratch/chk.sh FILE [check|run]; templates deposit/scratch/tmpl/*.l4.in expanded by scratch/build.py (--@Q N-M lines -> quote lines).

## Status (final, 2026-10-29)
- All deliverables written: 12 layer-1 modules + s5 definitions, 13 test files, wa-seat.l4 (32 questions), wa-cases-seat.l4 (109 assertions), coverage.py + coverage_data.py, NOTES.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md, check.sh, srcrefs.py, fetch-main-l4.sh.
- check.sh (98 vs 102): 28 modules, 0 errors, 1213 assertions satisfied, 0 failed, 0 refused, all `same`.
- srcrefs --refs: 0 problems.  coverage audit: 1105 lines, 790 rows, 0 deferred.
- If resumed: re-read NOTES.md; the generator scripts and templates in deposit/scratch were deleted (the .l4 files are the source now).

## Status after pass 2 (2026-10-29, the fix list from the independent test pass)
- check.sh (98 vs 102): 31 modules, 0 errors, 1487 assertions satisfied, 0 failed, 0 refused, all `same`.
- srcrefs --refs and --strict: 606 src: lines, 350 runs, 432 locators, 0 problems each.  coverage audit: 1105 lines, 790 rows, 0 deferred; inert reasons 238 / 2 / 1.
- What changed and why is in NOTES.md under "Changes to existing modules"; forks F11 to F20 are in the Fork register; limits are under "Known limits".
- The pass-2 generator scripts (deposit/scratch-pass2) were deleted; the .l4 files are the source.


Note added 2026-10-29, after the run: the date shim described above no longer exists. Every module writes dates as `Date day month year`, and this encoding defines no `YMD` or `YearMonthDay`.
