# PROGRESS.md -- roc12 (lines 7400-8829: O 64-70, First to Fourth Schedules)

Paths (so a compacted context can find everything):
- ROOT   = <run>
- DEPOSIT = ROOT/deposit/encodings/legalese-sonnet-5.5   (this folder; run commands from here)
- RAW = ROOT/inputs/SCJA1969-S914-2021.txt  (from DEPOSIT: ../../../inputs/SCJA1969-S914-2021.txt)
- WORK = ROOT/work: t/*.l4.tmpl templates; build.sh expands them into DEPOSIT (do not edit DEPOSIT .l4 by hand for layer 1); cov.tsv / forks.tsv / jc.tsv collected by build
- L4 = <bin>/l4-main-109 ; L4_MAIN = <bin>/l4-main-108 (absolute paths; scratchpad = ROOT/../../../..)
- Template markers: {{Q N M}} quote lines; --@COV lines | prov | disposition | where; --@FORK id | ...; --@JC QA..QE | ...

## Status (updated after each step)
- [x] orientation (brief, PLAN, skills read)
- [x] O 64: roc12-order-64.l4 + roc12-tests-order-64.l4 (194 asserts, 0 fail on 109 and 108); strict srcrefs 0
- [x] O 65: roc12-order-65.l4 + roc12-tests-order-65.l4 (69 asserts, 0 fail); strict 0
- [x] O 66 (89 asserts) and O 67 (127 asserts) done, 0 fail, strict 0
- [x] O 68 (31), O 69 (104), O 70 (53) done, tests pass, strict 0
- [x] ALL layer-1 Orders 64-70 + tests done
- [x] Schedules 1-3 (roc12-schedules-1-3.l4 + tests, 45 asserts) done
- [x] Schedule 4: work/gen_sch4.py (+ work/extras/part-N.tmpl) -> roc12-schedule-4-part-1..5.l4, -types, -fees; tests roc12-tests-schedule-4.l4 (337 asserts); regenerate with: python3 -I work/gen_sch4.py && bash work/build.sh; test file = cat work/sch4-tests-{header,partA,partB}.txt
- [x] seat + cases: work/gen_seat.py -> roc12-seat.l4 (60 questions), work/gen_cases.py -> roc12-cases-seat.l4 (197 asserts, expected values decided from the text before the run; all satisfied on 109 and 108)
- [x] NOTES.md: written by work/gen_notes.py (re-run it after any change: python3 -I work/gen_notes.py); needs work/check-run-final.txt from the last check.sh run
- [x] check.sh: exit 0, TOTAL (28 modules) 0 errors, 1246 satisfied, 0 failed, 0 refused on both builds, every module 'same'; srcrefs check / --refs / --strict over roc12-*.l4: 1424 src: lines, 326 runs, 409 locators, 0 problems; no 'is at the end of the file' or 'follows code on its line' in any file
- [ ] advisor before done; final report items 1-8

## Decisions taken
- Dialect idioms verified: positional GIVEN args; CONSIDER..WHEN JUST x/NOTHING; PARTY/MUST/SHANT/HENCE FULFILLED/LEST BREACH BY .. BECAUSE; #TRACE prints outcome only.
- Regulative sections carry no WITHIN where the text states no deadline.
- Stated periods/limits: JUST FALSE outside (brief governs over PLAN §2).

## SECOND ROUND (started after the first full report)
State before the round: check.sh 28 modules, 1246 satisfied on both builds; seat 60 questions / 197 cases; srcrefs 1424/326/409/0.
Items (numbered 1 to 8 in the instruction): 1 columns of two-cell rows (assign by text, fork A3, count rows/cells mapped); 2 "for each" fees take a count (+ yes/no twin); 3 periods JUST FALSE outside (sch 1 para 1 (a),(d); Part 2 para 2 14 days); 4a item 43 amount NOTHING + "at least $200" twin; 4b Part 4 item 1(b) subscriber input; 4c Hague-only exclusion fork + Third Schedule membership JUST FALSE for unlisted; 5 gap functions or one line each; 6 fork A6 (keep $500 every month); 7 fork lines A1 A2 A4 A5 A7 A8 A9 #192 #85c #229; 8 check #39 input FALSE answers NOTHING.
Checkpoints: end turn with a short status line after item 1, after items 2-3, after items 4-7, then final report.
Done (2026-11-05, end of the round):
- check.sh, 28 modules, TOTAL 1660 satisfied, 0 failed, 0 refused, 0 errors, identical on main 1.6.109 and 1.6.108 (was 1246).
- Per file: tests-order-64 195, -65 69, -66 98, -67 133, -68 31, -69 104, -70 53, tests-schedules-1-3 55, tests-schedule-4 706, cases-seat 216.
- Seat: 64 questions, 216 cases (was 60 and 197).
- srcrefs plain, --refs, --strict over every roc12-*.l4: 1506 src: lines, 361 runs, 429 locators, 0 problems (was 1424/326/409/0).
- Error, Warning, "is at the end of the file", "follows code on its line": 0 lines in `l4 run` output of every roc12-*.l4 on both builds.
- #TRACE: 32 traces read with work/tracecheck.py (outcome against the `-- expected:` comment above each), 0 mismatches on 1.6.109.
- Items 1 to 8 of the lead's message: all done; NOTES.md regenerated (forks 55, judgment calls 75).

Follow-up (2026-11-05, words and seat questions for the hearing-day rows):
- Seat general question: its `units` input is now titled "the number the fee is charged on" and its @desc says what the number is for each kind of row, including that a Part 2 hearing-day row takes the length of the hearing in days (1 for "table 3 item 1" gives 0).
- New functions: `sch 4 part 2 table 3 the fee for one day of the hearing in the proceedings`, `sch 4 part 2 table 4 the fee for one day of the hearing`.
- New seat questions: S4.2.3d (Table 3, one day), S4.2.4 (Table 4, whole hearing), S4.2.4d (Table 4, one day), S4.2.A (Appellate Division and Court of Appeal, whole hearing); S4.2.3 inputs reworded.
- NOTES.md Seams: a bullet on `units` by kind of row.
- check.sh, 28 modules, TOTAL 1705 satisfied, 0 failed, 0 refused, 0 errors on both builds; tests-schedule-4 730; cases-seat 237; seat 68 questions; srcrefs 1506/361/429/0 (plain, --refs, --strict); 32 traces, 0 mismatches; 0 error/warning/misplacement lines on both builds.
