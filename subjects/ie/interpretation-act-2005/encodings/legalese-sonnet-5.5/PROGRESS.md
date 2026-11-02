# PROGRESS (Interpretation Act 2005, Ireland; row legalese-sonnet-5.5, completion pass 2)

This file is the run's memory.
After a context compaction, re-read this file, `NOTES.md` and the statute text (`../../registers/source-bundle/No.-23-of-2005.txt`, sha256 0108a07d...), not a summary.
The pass-1 PROGRESS.md, NOTES.md and encoding.json were kept in a scratch directory `_work/` while pass 2 rewrote all three; the directory is deleted.

## Baseline (step 1), measured 2026-10-29 before any change

Binary: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528`, `l4 --version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`.
Command: `SRC_RAW=<registers/source-bundle/No.-23-of-2005.txt> L4=<binary> L4_TARGET=unstable ./check.sh`.
Printed (the full output was kept in `_work/baseline-check.txt`, now deleted):

```
module                                    errors satisfied  failed  refused  expected
ie-general.l4                                  0         0       0        0         0
ie-interpretation-time.l4                      0         0       0        0         0
ie-month-year-readings.l4                      0         0       0        0         0
ie-operation-and-construction.l4               0         0       0        0         0
ie-powers-and-service.l4                       0         0       0        0         0
ie-repeal.l4                                   0         0       0        0         0
tests-commencement.l4                          0        57       0        0         0
tests-general.l4                               0       102       0        0         0
tests-operation.l4                             0       112       0        0         0
tests-periods.l4                               0        96       0        0         0
tests-powers-service.l4                        0        31       0        0         0
tests-readings.l4                              0        59       0        0         0
tests-red-control.l4                           8         0       8        0         8
tests-repeal.l4                                0       105       0        0         0
tests-rest-days-and-words.l4                   0        57       0        0         0
tests-worked-cases.l4                          0        26       0        0         0
TOTAL (16 modules)                             8       645       8        0
srcrefs check: 261 src: lines, 132 runs, 172 locators, 0 problems
```

Baseline numbers that must still hold at the end: 16 modules, 645 satisfied, 8 failed (all in tests-red-control.l4, expected), 0 refused, 261 src lines, 132 runs, 172 locators, 0 problems.
The pass-1 binary printed `dev`; this pass uses the unstable prerelease above, and the baseline numbers are identical on it.

## Plan, in order

1. Audit (step 2): count units with `_work/units.py`; write `## Re-disposition audit` in NOTES.md BEFORE any new L4.
2. Encode what the audit moves (step 3), new modules beside the existing ones.
3. Tests from the text (step 4), one test file per new module.
4. Bookkeeping (step 6): NOTES.md coverage table (one row per unit), fork register, `## Jural relations`, `## Changes to existing modules`, `check.sh` output; encoding.json 0.2.0.

## Status (2026-10-29, bookkeeping done)

DONE: audit (before any new L4); five new modules and five new test files; NOTES.md (all sections, 256-row coverage table, fork register F1 to F48, `## Jural relations`, `## Changes to existing modules`, numbered findings, check.sh output); `encoding.json` 0.2.0; `SOURCE-LICENSE.md` pointing at `../../SOURCE-LICENSE.md`.
Final `check.sh`: 26 modules, 1322 satisfied (645 baseline + 677 new), 8 failed (all expected, tests-red-control.l4), 0 refused; srcrefs 438 src lines / 254 runs / 312 locators / 0 problems under both `--strict` and `--refs`.
All 16 baseline modules print exactly their baseline numbers.
New modules and tests (each rule has an `@ref` with src locators):
- `ie-schedule-definitions.l4` + `tests-schedule-definitions.l4` (421): Schedule Pt 1 (32) and Pt 2 (8) as a defined-term table, appliers, s 21(1) and (2).
- `ie-words-and-meaning.l4` + `tests-words-and-meaning.l4` (64): s 18 lead-in, 18(a), 18(c), 18(j), 18(i) with the 1971 offset as an input, s 19, s 20(2).
- `ie-powers-duties-continuing.l4` + `tests-powers-duties.l4` (57): s 10, 22(1), 22(2), 23(1), 23(2), 24.
- `ie-citation-and-text.l4` + `tests-citation-and-text.l4` (67): s 7(1)(a), (b), (c), s 14(2), s 14(3), s 15(2).
- `ie-acts-referred-to.l4` + `tests-acts-referred-to.l4` (68): the 18-row table.
No pass-1 module or test was edited (every pass-1 file keeps the modification time of the copy made at the start of pass 2); `ie-schedule-definitions.l4` and `tests-schedule-definitions.l4` were edited once afterwards, for Update 3 below.
The scratch directory `_work/` was deleted at the end.

Decisions taken this pass, each with the text that licenses it:
- s 14(3): "that is not required for the purpose of punctuation" is read as governing both commas (F39).
- Sch Pt 1 "President": "exercising the powers and performing the duties" read as both (F40).
- "pre-union Irish statute" passed on 1 January 1801 itself: not answered (F41).
- s 18(c): the list of kinds is not closed by the text; a party of another kind is not answered (F42).
- s 15(2): "immediately" gives no measure; the latest moment is not answered (F43).
- ss 22(2), 23(2): two holders on one day is not answered; a vacancy gives NOTHING (F44).
- s 7(1)(b), (c): both map to limb (b) of "Act" in s 2(1) (F45).
- s 18(j): "whether punishable on indictment or on summary conviction" read as naming the two ways; another way is not answered (F46).
- Entries that say "includes" are open lists and entries that say "does not include" exclude only what they name (F47).
- The members of an "includes" entry are the things the line lists, one member each (F48; added by the fix of 2026-10-29).

## History

- Update 0: baseline run, pass-1 files read, unit counter written.
- Update 1: audit written; Schedule module and tests; words-and-meaning, powers-duties, citation-and-text and Acts-Referred-to modules and tests; full check.sh run (numbers above).
- Update 2: coverage table (256 rows) generated and inserted; forks F39 to F47; Jural relations; encoding.json 0.2.0; SOURCE-LICENSE.md; final check.sh and srcrefs runs; `_work/` deleted.
- Update 3 (2026-10-29): reviewer's defect fixed. The lookup for "includes" entries held whole phrases as members; Pt 1 "land" and "writing" and Pt 2 "functions" now hold both the items as the line prints them and the things each lists (F48, reading c; see Update 4). Edited `ie-schedule-definitions.l4` and `tests-schedule-definitions.l4` only; 383 to 403 assertions at that point; check.sh 26 modules, 1304 satisfied, 8 failed (expected), 0 refused; srcrefs unchanged. See NOTES.md `## Changes to existing modules`.
- Update 4 (2026-10-29): over-correction undone. After the split the Act's own printed phrases ("houses and buildings", "powers and duties", ...) refused; land, writing and functions now hold both the printed items and their constituents (F48, reading c). 383 to 411 assertions; check.sh 26 modules, 1312 satisfied, 8 failed (expected), 0 refused.
- Update 5 (2026-10-29): F48 extended to Pt 1 "oath", "swear" and "Great Britain" after a script sweep of all 40 Schedule entries (7 not `means`: 6 extended, "affidavit" left; 33 `means` entries left, since the applier refuses for them). 411 to 421 assertions; check.sh 26 modules, 1322 satisfied, 8 failed (expected), 0 refused.
