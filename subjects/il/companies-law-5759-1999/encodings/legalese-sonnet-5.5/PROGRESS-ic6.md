# PROGRESS: piece ic6 (Part 9 chapters 2 to 6, Part 10, the Schedules, the signature block), src:2956-3556

Written by the piece agent ic6. State when the work was handed back: every deliverable below is written and runs clean; nothing is left to do inside this piece.
Re-read this file, NOTES.md and the text (not a summary) after any compaction.

## Working method

- Helper scripts and sources live in `inputs/work/` (the piece's own INPUTS_DIR), never in this folder:
  - `inputs/work/tpl/*.l4` are the module templates. A line `@@Q N` or `@@Q N M` is expanded by `inputs/work/build.py` into `-- src:N | ...` quote lines copied by `srcrefs.py quote`; the expansion is written to this folder. `ic6-seat.l4` and `ic6-cases-seat.l4` are generated into `tpl/` by `inputs/work/seatgen/gen_seat.py` from the question specs in `seatgen/sp1.py` to `sp5.py`.
  - `inputs/work/cov/*.md` are the coverage rows; `python3 -I inputs/work/cov_check.py` lists the non-blank lines of src:2956-3556 that no row covers (none).
  - `inputs/work/notes/*.md` are the parts of NOTES.md; `inputs/work/build_notes.py` assembles it (the coverage table is sorted by first source line and gets the seat questions that reach each rule).
- Every module is run with `l4 run` and `srcrefs.py check --refs` straight after it lands (`inputs/work/run.sh <module>`).

## Modules and tests (assertions satisfied, from check.sh)

| module | range | tests |
| --- | --- | --- |
| ic6-repealed.l4 | stubs for 350(ב)-(ח), 350א-350כד, 365(ג), First Schedule item 8 | none (inert strings or used by every test file) |
| ic6-common.l4 | the record of a body that is a company, a foreign company or a partnership, and two rules | none (inert strings or used by every test file) |
| ic6-foreign-company.l4 | ss 346-349א | ic6-tests-foreign-company.l4 (65) |
| ic6-arrangement.l4 | ss 350, 351, 351א | ic6-tests-arrangement.l4 (78) |
| ic6-striking-off.l4 | ss 351ב-351ח | ic6-tests-striking-off.l4 (118) |
| ic6-remedies.l4 | ss 352-353א | ic6-tests-remedies.l4 (19) |
| ic6-sanction-registrar.l4 | ss 354-362 | ic6-tests-sanction-registrar.l4 (167) |
| ic6-defaulting-company.l4 | s 362א | ic6-tests-defaulting-company.l4 (34) |
| ic6-sanction-securities.l4 | ss 363א-363ב | ic6-tests-sanction-securities.l4 (54) |
| ic6-scope-abroad.l4 | ss 364-365א | ic6-tests-scope-abroad.l4 (21) |
| ic6-transitional.l4 | ss 367-378 and the days of passing and commencement | ic6-tests-transitional.l4 (84) |
| ic6-schedule-1.l4 | First Schedule | ic6-tests-schedule-1.l4 (63) |
| ic6-schedule-1a.l4 | First A Schedule | ic6-tests-schedule-1a.l4 (47) |
| ic6-schedule-2.l4 | Second Schedule | ic6-tests-schedule-2.l4 (15) |
| ic6-schedule-3.l4 | Third Schedule | ic6-tests-schedule-3.l4 (77) |
| ic6-schedule-4.l4 | Fourth Schedule | ic6-tests-schedule-4.l4 (10) |
| ic6-seat.l4 | layer 2: the seat's questions | ic6-cases-seat.l4 (708) |

Total for the ic6 files: 1560 assertions satisfied, 0 failed, 0 refused, 0 error diagnostics.

## Decisions taken (with the provision that licenses each)

- Duties are stated as compliance predicates over facts and dates, not as `PARTY ... MUST` regulative rules: the stable binary does not report a mismatched party, a `DEONTIC` cannot be asserted, and `#TRACE` moves no `check.sh` count. (The brief: encode each time limit so it is testable.)
- Time limits: "within N days of X" is `AT MOST (X PLUS N)`; months and years use `add months` and `add years`; "have passed" (חלפו) is strictly after the last day; fork entries F-ic6-2, 7 and 8 say why.
- The Registrar's "reasonable basis" and the court's findings are plain inputs (ss 354, 351ה(א), 351ח(א), 362א).
- Section 354(א): the Act's 6,000 is the constant; the Wikisource note's 9,380 is not (F-ic6-13).
- Section 351ו opens twice (src:3135 and 3140): one set of rules, two coverage rows each (F-ic6-9).
- The seat (layer 2) asks about the person who founds, directs or holds shares; it has 180 questions and 708 cases; every layer-1 rule except seven is reached by a question (NOTES.md says which seven and why).

## Files written

Under this folder: the `ic6-*.l4` modules, tests and seat listed above, `NOTES.md`, `PROGRESS.md`.
Untouched: `check.sh`, `srcrefs.py`, the six `ic-core*.l4` keel modules.
