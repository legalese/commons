# PROGRESS (coa22: Companies Act 2006, lines 13934-14665, ss 994-1043)

Status (2026-11-13): finished. Every file named below was written and gated; `check.sh` is green on both stable builds (1284 assertions, 0 failed, 0 refused). The numbers are in `NOTES.md` section "What check.sh prints", copied by script from the last run.
Read after any compaction: this file, `NOTES.md`, `BRIEF.md` (run folder), `PLAN.md` (inputs) and the text; not a summary.

## How the files are made
- The `.l4` files are generated from `DEPOSIT/../work/src/*.l4.in` by `DEPOSIT/../work/build.py <module>` (`@@R label A-B` = quote lines A..B copied from the raw text plus the `@ref`; `@@REF` = an `@ref` only; `@@Q` = quote only; `@@M name a | b` = a macro of `work/macros.py`). Edit the `.in` files, never the generated `.l4`. The seat is `work/src/coa22-seat.head` + `.body1` + `.body2`; its cases are generated from `work/cases_data.py` by `work/gencases.py`.
- `work/run1.sh FILE...` runs the stable binary on files in the deposit; `work/show1.sh` and `work/evalfails.py` show a failed assertion's actual value.
- `work/coverage.py` (with `work/forks.py`) writes the coverage table; `work/mknotes.py` writes `NOTES.md` from it, the gate outputs and the text; `work/runcheck.sh` runs the whole gate. None of `work/` is shipped.

## Files (all in DEPOSIT/encodings/legalese-sonnet-5.5/)
| file | content | assertions |
| --- | --- | --- |
| coa22-part30.l4, coa22-tests-part30.l4 | ss 994-999 | 128 |
| coa22-part31-ch1.l4, coa22-tests-part31-ch1.l4 | ss 1000-1011 | 308 |
| coa22-part31-ch2.l4, coa22-tests-part31-ch2.l4 | ss 1012-1023 | 142 |
| coa22-part31-ch3.l4, coa22-tests-part31-ch3.l4 | ss 1024-1034 | 368 |
| coa22-part32.l4, coa22-tests-part32.l4 | ss 1035-1039 (the inserted CA 1985 text encoded; the amending instructions inert 2; s 1039 blank) | 81 |
| coa22-part33.l4, coa22-tests-part33.l4 | ss 1040-1043 | 52 |
| coa22-seat.l4, coa22-cases-seat.l4 | layer 2: 88 questions, 205 cases | 205 |
| check-traces.py | compares each `#TRACE` with its `-- EXPECT:` line (24 traces) | |
| NOTES.md, NEEDS-CORE.md, PROGRESS.md | | |

## Decisions (each with its licensing text in NOTES.md, fork register F1 to F15 and seat assumptions S1 to S7)
F1 counting; F2 default derived; F3 officer in default; F4 two months expire at the end of the day; F5 bare "must publish" with no striking off is NOTHING; F6 a bare "must" not done is FALSE; F7 previous three months; F8 "other than"; F9 a late disclaimer has no deeming effect; F10 flat negative with exception; F11 consideration; F12 creditor in s 1029(2)(i); F13 s 1033(5)(c) no deadline; F14 two fine wordings in s 1033(7); F15 s 1013(5) both periods.

## Done
All of the above. Remaining by the lead, not by me: the merge wiring of the seam inputs (`s 1(1)`, `s 112`, `s 1121`, `s 29`, `sch 4`, `s 66`) and the hoist in `NEEDS-CORE.md`.

## Seat audit of 2026-11-12 (requested by the lead)
88 seat questions read; 0 direction, 3 subject (ss 996(2)(e), 1012(1), 1026(1)) and 2 scope (s 1038, for ss 434(7) and 447(9) of the 1985 Act) mismatches; those 5 were retitled in `coa22-seat.l4` and the 11 assertions that carry their names are restated in place in `coa22-cases-seat.l4` with `-- RECONCILED 2026-11-12`. Nothing else changed. See `NOTES.md`, "Seat audit of 2026-11-12".

## Name-test sweep of 2026-11-12 (requested by the lead)
34 layer-1 functions named for a grant or power answered JUST FALSE: 11 flipped to NOTHING (forks F16 to F26: ss 995(2), 996(1), 996(2), 1000(1), 1000(3), 1002(1), 1002(2), 1002A(1), 1018(4), 1022(4), 1031(1)), 15 kept (gate closed by the text), 8 listed as "may" with where/when/upon (not flipped), 0 "entitled". 22 assertions restated in place (16 layer-1 tests, 6 seat cases) with `-- RECONCILED 2026-11-12`. check.sh unchanged at 1284 satisfied on both builds. See `NOTES.md`, "Name-test sweep of 2026-11-12".
