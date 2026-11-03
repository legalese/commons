# PROGRESS (iaw-wa: Interpretation Act 1984 (WA), whole, Sonnet 5.5 solo)

Read this first after any compaction, then NOTES.md, then the text (../../registers/source-bundle/mrdoc_49111.txt, 1118 lines).

## Paths
- DEPOSIT dir (this folder): <the lead's scratchpad>/runs/iaw-wa/deposit/encodings/legalese-sonnet-5.5
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


## Fix run fix-wa, 2026-11-04 (catch-all pass: plain-BOOLEAN functions that answered FALSE for a catch-all)

Read this first after any compaction, then NOTES.md ("Catch-all pass 2026-11-04", "Reading a result: FALSE and NOTHING", "Marginal readings for a lawyer"), then the text.
Brief: <the lead's scratchpad>/runs/fix-wa/BRIEF.md.
Work copy of the .l4 files for trial edits: ../../scratch/work/ (deposit/scratch/work); the real files in this folder are changed only after the baseline finished.

### Status (updated as I go)
- DONE (all steps of the brief): baseline, find-them-all, change, tests, NOTES, encoding.json (version 0.1.1), check.sh after, srcrefs. Nothing is staged, committed or pushed.

### Decisions taken (with the section that licenses each)
- s 13(2) `a person with none of those statuses` -> NOTHING-kind (list not closed): s 13(2) "shall be read as a reference to an Australian citizen and to any other person who ... has the status ...", no "only".
- s 13(3) function keeps delegating to the s 13(2) function (same persons, same words), so it becomes MAYBE BOOLEAN with it.
- s 19(1) `for some other reason` -> NOTHING-kind (limited by its own wording): "may be given to that material ... (a) to confirm ...; or (b) to determine ... when ...", no "only".
- s 19(1) material not capable of assisting -> JUST FALSE (FALSE-kind): "if any material ... is capable of assisting in the ascertainment of the meaning of the provision". Rests on reading (a) of the brief (a failed "if" is the text's no), so it is listed under "Marginal readings for a lawyer", with the other reading (NOTHING). The old function answered FALSE for it too.
- s 45A(2) `any other expenditure` is KEPT as plain BOOLEAN FALSE (deviation from the brief's premise, reported to the lead): "Expenditure is not relevant for the purposes of subsection (1) unless it has been or is to be incurred" is a flat negative with "unless" (src:539). The caller `a power to prescribe a fee allows it to recover the expenditure` is a site NOTES marks "marginal, kept, for a lawyer", out of scope, and stays as it is.

### Facts
- No function in wa-seat.l4 reaches s 13 or s 19: the seat imports time, part3, part5, part6, part7, part9, part10 and not part2. Seat questions returning MAYBE: 20 before and 20 after (11 MAYBE BOOLEAN, 8 MAYBE DATE, 1 MAYBE NUMBER).

### baseline 2026-11-04
Run before any change, in this folder: `L4=.../bin/l4-stable-98 L4_MAIN=.../bin/l4-main-108 ./check.sh` (log: ../../logs/baseline.log).
Result: 32 modules, 0 errors, 2051 satisfied, 0 failed, 0 refused, every module `same` on the main build `1.6.108 (main, 2ae7c9b, 2026-11-02)`; exit 0.
Per module counts that matter here: tests-independent 565, wa-cases-seat 109, wa-tests-part2 116, wa-tests-part6 113; the other 28 modules as printed in the log.
srcrefs (`--refs`, and again with `--strict`, over wa-*.l4): 606 src: lines, 350 runs, 432 locators, 0 problems; run after the .l4 edits, same numbers.

### Files changed in this run (all in this folder)
- wa-interpretation-part2.l4 (3 functions, s 13(2), s 13(3), s 19(1); comment above s 19(1))
- wa-interpretation-part6.l4 (comment only, on the s 45A(2) `any other expenditure` branch; no behaviour change)
- wa-tests-part2.l4 (11 restated, 4 added)
- tests-independent.l4 (8 restated)
- NOTES.md (sections "Catch-all pass 2026-11-04" and "Marginal readings for a lawyer" added; the "Not changed, and open" paragraph rewritten; "What `check.sh` prints" and "Changes to existing modules" extended)
- encoding.json (version, checks, notes)
- PROGRESS.md (this section)
- ../../logs/baseline.log and ../../logs/after.log (the two check.sh runs, outside the folder)

### After the change (check.sh, log ../../logs/after.log)
32 modules, 0 errors, 2055 satisfied, 0 failed, 0 refused, every module `same` on 1.6.108; exit 0.
A diff of the two printed tables shows only wa-tests-part2.l4 (116 to 120, both builds) and the TOTAL line (2051 to 2055).
The NOTES claims about the after-run (Catch-all pass, Changes to existing modules, What `check.sh` prints) were checked against this log.
srcrefs (--refs and --strict, wa-*.l4): 606 src: lines, 350 runs, 432 locators, 0 problems each.
No DiagnosticSeverity_Error or _Warning in the four changed files run on their own.
deposit/scratch (probe scripts, the work copy) is deleted at the end; deposit/logs is kept.
