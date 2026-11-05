# PROGRESS -- mlr2 (regs 33 to 45ZB, lines 1009-1585)

Status (2026-11-05): every deliverable is written and checked, and was revised the same day under the rulings of 2026-11-05 (periods, "where", scope limits, delegated definitions); the final report is the next and last step.
`check.sh` (main 1.6.109, second build 1.6.108): 14 modules, 0 errors, 1490 assertions satisfied, 0 failed, 0 refused, same counts on both builds.
`srcrefs.py check` and `--strict`: 0 problems on every own file.
`l4 check`: no "end of the file" or "follows code" warning on any layer-1 or seat file.

## Done
- Layer 1: `mlr2-helpers.l4`, `mlr2-ecdd.l4` (regs 33-36), `mlr2-sdd-emoney.l4` (37-38), `mlr2-reliance-records.l4` (39-41), `mlr2-trusts.l4` (42-44), `mlr2-register.l4` (45, 45ZA, 45ZB).
- Tests: `mlr2-tests-ecdd.l4` (370), `-sdd` (136), `-reliance` (121), `-trusts` (227), `-register` (412); 14 `#TRACE`s read by hand and compared across the two builds.
- Layer 2: `mlr2-seat.l4` (49 questions, 6 `§§` groups in text order), `mlr2-cases-seat.l4` (224 assertions).
- `NOTES.md`: coverage table (568 rows, generated), fork register (E1, N2, the two rulings of 2026-11-05, plus 32 forks), merge note, jural relations, marginal readings, reading a result, seams, dependencies, unstable line, findings, traces, what main does not accept, `check.sh` output.

## How the files are made (work/ is not shipped)
- `work/src/*.l4.in` are the sources; `work/tools/gen.py` expands `%%QREF`/`%%REF`/`%%Q`/`%%INCLUDE` into `-- src:N | ...` lines (copied by `srcrefs.py quote`) and `@ref` locators, and writes the `.l4` files into the deposit folder.
- `work/tools/listgen.py` (specs in `lists.py`) generates the enumerated lists of the text (type, membership function, wording function, tests) from the raw text by line number.
- `work/tools/seatcases.py` turns the hand-written `work/src/seatcases.spec` (question number, plain inputs, expected value) into `mlr2-cases-seat.l4`.
- `work/tools/units.py` lists the 568 text units; `coverage.py` builds the coverage table; `forks.py` is the fork register as data; `mknotes.py` assembles `NOTES.md` (static prose in `notes_static.py`).
- `work/tools/chk.sh FILE...` runs a file on main 1.6.109 and prints errors / warnings / satisfied / failed.

## Decisions taken (the full register is in NOTES.md)
Forks: F33-1, F33-2, F33-3, F35-1, F35-2, F35-3, F37-1, F38-1, F38-2, F38-3, F39-1, F39-2, F39-4, F40-1, F40-2, F40-3, F42-1, F43-1, F43-2, F43-3, F44-1, F45-1, F45-2, F45-3, F45-4, F45-5, F45-6, F45-7, F45ZB-1, F45ZB-2, F45ZB-3, FW-1.
Stated departure: helper and seat-wiring names begin `mlr2 ` and `mlr2 seat ` (not provisions; no other part can define them).
Seat scope: the business as a relevant person; no questions on the trustees' own filing duties or on officials' duties (stated in `mlr2-seat.l4` and NOTES.md, Seams).
