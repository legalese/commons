# PROGRESS (coa9: lines 5418-5894, ss 414C to 440)

Re-read this, NOTES.md and the text after any compaction, not a summary.

## State: finished (2026-11-13). Everything below is done and on disk.

| item | state |
| --- | --- |
| layer 1: coa9-penalties, -strategic, -directors-report, -remuneration, -circulation, -publication, -laying, -approval | written; every declaration has an `@ref`; `srcrefs.py check --strict` 0 problems on each |
| layer-1 tests: coa9-tests-strategic (198), -directors-report (79), -remuneration (55), -circulation (75), -publication (194), -laying (24), -approval (78) | 703 assertions, 0 failed; 14 traces read on both builds |
| layer 2: coa9-seat.l4 (128 questions, 7 sections), coa9-cases-seat.l4 (320 assertions) | 0 failed |
| check.sh (target main, 1.6.110 vs 1.6.109) | 19 modules, 1023 satisfied, 0 failed, 0 errors, same four counts on both builds |
| NOTES.md | coverage (477 rows), fork register F1-F34, Jural relations, Marginal readings, Reading a result, Seams, findings, stable-binary traps, traces, direction audit, check.sh output, rulings word for word |
| NEEDS-CORE.md | the s 438(4) "greater of" fine constructor |

## Follow-up of 2026-11-12 (team-lead): two tasks, both done

- **Name-test sweep** (`NOTES.md`, `### Name-test sweep of 2026-11-12`; fork register rows S1 to S8): 19 functions carry "may", "entitled" and the like in the name; flipped 0, kept JUST FALSE with the gate closed by the text 0, listed "may" with where/when/upon 3 (s 415(3), s 414CB(4A), s 426(1)), listed "entitled" 5 (ss 415A(1), 431(1), 431(2), 432(1), 432(2)); "it is lawful" 0. No layer-1 answer changed, so no assertion was restated.
- **Second seat-question audit** (`NOTES.md`, "Direction audit of the seat layer"): 128 read, 17 further mismatched (15 names, 2 export texts); old and new names are in the table there. Edits were made in `work/seat/q1.py` to `q4.py` and the seat and cases regenerated; no answer changed.
- **Period repair** (team-lead, 2026-11-13, after a blind reviewer's finding on s 421(3)): fork F35. JUST FALSE, not NOTHING, outside a period the text fixes in its own words, at `s 421(3)` (not a director now and not at any time in the preceding five years), `s 416(1)(a)`, `s 439A(1)(a)` and `s 439A(3)`. Eight assertions restated in place with `-- RECONCILED 2026-11-12: was ...`: 2 in `coa9-tests-remuneration.l4` (s 421(3)), 1 in `coa9-tests-directors-report.l4` (s 416(1)(a)), 2 in `coa9-tests-approval.l4` (s 439A(1)(a), s 439A(3)) and 3 in `coa9-cases-seat.l4` (the seat questions under s 421(3) twice and s 439A(1)(a) once). check.sh TOTAL unchanged at 1023 satisfied.
- `check.sh` (same L4 and L4_MAIN): 19 modules, 1023 satisfied, 0 failed, same on both builds, before and after. `srcrefs.py check --refs` and `--strict`: 0 problems.

## How the files were made (scratch lives in DEPOSIT/../work/, not shipped)

- `work/src/<module>.l4` are templates; a line `@@Q N M` becomes `srcrefs.py quote` of raw lines N..M (`work/expand.py`). `work/build.sh <file>` expands, runs `l4-main-110 run`, prints the counts, and runs `srcrefs.py check --strict`.
- `work/tests/<name>.spec` -> `coa9-tests-<name>.l4` by `work/gentests.py` (short keys for long names; every expected value is hand-written in the spec beside the assertion).
- `work/seat/q1-q4.py` + `sections.py` + `header.txt` -> `coa9-seat.l4` by `work/seatgen.py`; `work/tests/seat-cases.spec` -> `coa9-cases-seat.l4`.
- `work/coverage_map.py` + `work/units.json` -> `work/coverage-table.md` by `work/coverage.py` (validates every name and every line); `work/notes/*.md` + generated parts -> NOTES.md by `work/mknotes.py`.
- To regenerate after any change: `python3 -I work/expand.py`; `python3 -I work/gentests.py <names>`; `python3 -I work/seatgen.py`; `python3 -I work/coverage.py`; run check.sh (target main, with L4_MAIN set) to `work/check-final.log`; `python3 -I work/mknotes.py`.

## Decisions taken (with the text or ruling that licenses each)

- The brief says import coa-core and coa-definitions; PLAN 4.1 says take keel answers as inputs. Measured: a GIVEN named like an imported keel function does not collide. Layer-1 modules import both; seam inputs keep the PLAN/keel names (NOTES.md, Seams).
- A bare "must" (a content or duty requirement with no stated consequence) is a compliance answer: JUST TRUE when met, JUST FALSE when a stated item is missing (forks F1-F32; case-by-case ruling of 2026-11-05).
- An "if" or "where" that fails (offences, duties, deeming rules): JUST FALSE (marginal reading (a), ruling (b)); a limb introduced by "who" that the person is outside: NOTHING (marginal reading (b)); scope limits with no "only": NOTHING (ruling (c)).
- Bars (s 434(2), s 435(2)): the function is the bar (JUST TRUE = barred); NOTHING when not engaged.
- Regulative rules (ss 424(3), 431(3), 432(3), 437, 439(1)) each have a decision-function twin with `#ASSERT`s, because a `#TRACE` adds no assertion line and a DEONTIC value cannot be compared on the stable binary.
- Merged-version artifacts are forks, not choices: s 415A(2) (F10), s 438(4) (F30).
- Trap met: `(NOT (a) OR b)` reads as NOT (a OR b); the circulation test for s 426A(2) caught it (the only failing assertion of the work, before the fix).

## What a successor should not redo

Layer 1, its tests, the seat and its cases all pass on both builds; do not edit an expected value to match code. If the text file changes, re-run `work/expand.py` (quote lines are copied from it) and `srcrefs.py check --strict`.
