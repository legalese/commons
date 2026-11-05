# PROGRESS.md -- roc10 (Rules of Court 2021, lines 6102-6795: Orders 46, 46A, 47 to 56)

Written by the part agent roc10.  Updated as work lands; if my context was compacted, re-read this file, NOTES.md and the text, not my summary.

## Paths

- DEPOSIT (this folder's parent two levels up) = <run>/deposit
- RUN = .../runs/iaw-roc10 ; INPUTS = RUN/inputs ; text = RUN/inputs/SCJA1969-S914-2021.txt (my lines 6102-6795)
- L4 (main 1.6.109) = <bin>/l4-main-109 ; L4_MAIN (1.6.108) = <bin>/l4-main-108
- Scratch/work (not shipped) = RUN/work/ (probes in RUN/work/probe, generator inputs in RUN/work/src)

## Plan (written 2026-11-05, before any module exists)

1. Orders in my range: 46, 46A, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56 (RULE-INDEX gives the rule starts).
2. One module per Order: roc10-order-46.l4, roc10-order-46a.l4, roc10-order-47.l4 ... roc10-order-56.l4; tests roc10-tests-order-NN.l4; regulative duties in roc10-duties.l4 (+ tests); seat roc10-seat.l4 and roc10-cases-seat.l4.
3. Sources are written as `work/src/*.l4.in` with macros that a script (`work/build.py`) expands by reading the raw text (quote lines, @ref with locators), so quotation is mechanical.
4. Coverage table is generated from `work/coverage.tsv` (hand-maintained rows: unit, line range, disposition, L4 name) and checked so that every non-blank line of 6102-6795 falls in some row.
5. Fork register "Judgment calls" is generated from `-- JUDGMENT` tags in the .l4 files so that file:line cannot drift.
6. Conventions: the brief governs where PLAN.md differs (periods: outside a stated period = JUST FALSE; "where" unmet = JUST FALSE; scope limit with no "only" = NOTHING).
7. Time: each period is counted under O 3 r 3 (lines 323-329); the last day is the seam input `o 3 r 3 the last day for doing the act` (S-T1).

## How the files are built (read this after a compaction)

- Layer-1 modules are written as `RUN/work/src/roc10-order-NN.l4.in`; `@@Q <lines> | <label>` expands to mechanical quote lines + `@ref label (src:lo-hi)`; `@@R` emits only the `@ref` (for a second declaration under the same quote).  Build: `python3 -I RUN/work/tools/expand.py RUN/work/src DEPOSIT/encodings/legalese-sonnet-5.5 RUN/inputs/SCJA1969-S914-2021.txt` (writes `roc10-order-NN.l4`).  NEVER edit the generated `roc10-order-*.l4` by hand: edit the `.in`.
- Tests `roc10-tests-order-NN.l4` are written directly in the deposit (no macros).
- Seat: `RUN/work/seatparts/NN.l4` + `RUN/work/seat-header.l4`; cases: `RUN/work/casesparts/NN.l4` + `cases-header.l4`; build with `RUN/work/build-seat.sh` (writes `roc10-seat.l4` and `roc10-cases-seat.l4`).  Edit the parts, never the generated files.
- Tags in the `.in` files above a function: `-- COVERS <unit>; <unit>` (coverage rows, prefix match) and `-- JUDGMENT Qx | provision | answer taken | other reading` (the fork register's Judgment calls).
- NOTES.md is assembled from `RUN/work/notes/*.md` + generated sections by `python3 -I RUN/work/tools/mknotes.py RUN`; manual dispositions (inert, fork, repealed) go in `RUN/work/coverage-manual.tsv` (prefix TAB disposition TAB text); extra units the parser cannot see in `RUN/work/units-extra.tsv`.  NEVER edit NOTES.md by hand.
- Checks: `cd DEPOSIT/encodings/legalese-sonnet-5.5; B=<scratch>/bin; L4=$B/l4-main-109 L4_MAIN=$B/l4-main-108 ./check.sh`; `python3 -I srcrefs.py check --refs RAW roc10-order-*.l4` and `--strict`; `l4 check FILE | grep -E 'is at the end of the file|follows code on its line'`.
- Gotchas found: `NOT (a) OR b` must be written `(NOT (a)) OR b`; a record fixture needs all fields (use `OF` positional); regulative rules need `GIVETH A DEONTIC ...`/`DECIDE`; `#ASSERT` on a DEONTIC value is unsupported.

## Conventions taken (apply to every Order; the brief governs over PLAN.md)

- Period outside = JUST FALSE; "where/when/upon/whenever/if/unless" unmet = JUST FALSE; scope limit with no "only" = NOTHING; bare "must" not done = NOTHING (QB); duty not arising: compliance NOTHING + companion "the duty arises" (QD); lifted bar: permission NOTHING + barred-twin (QA).
- Each period is a `Period` constant named for its section; timeliness compares the act date with the seam input `o 3 r 3 the last day for doing the act`.
- Seat helper names start `roc10 `; seat questions start "Under Order N, rule M,".

## Status

Written 2026-11-05 at the point the work was ready for review.

- Done end to end (module, tests, seat, cases): Orders 46, 46A, 47, 48, 49, 50, 51, 52, 53, 54, 55 and 56.
- Regulative rules: `roc10-duties.l4` (O 46A r 2(b), O 52 r 2(3), O 53 r 21(3)-(4), O 55 r 5, O 54 r 2(3)) with `roc10-tests-duties.l4` asserting the decision-function twins; the trace outcomes are written beside each `#TRACE` (`#ASSERT` on a DEONTIC is unsupported).
- `check.sh` (main 1.6.109, second column main 1.6.108): 30 modules, 0 errors, 1963 satisfied, 0 failed, 0 refused, identical on both builds (1932 before the fix round of 2026-11-05).
- `srcrefs.py check` and `--strict` over `roc10-*.l4`: 0 problems.
- NOTES.md assembled: coverage 581 units / 581 rows / 0 missing / 0 uncovered lines (438 encoded, 34 fork, 109 inert); fork register with 26 forks (46.1-46.4, 46A.1-5, 47.1-2, 48.1-3, 49.1, 52.1, 53.1-4, 54.1, 55.1, 56.1-4; the coverage rows number more than the forks because one fork can sit on several rows) and 156 judgment sites (QA 23, QB 94, QD 36, QE 3; QC none, QF not applicable); jural relations; marginal readings (Tables A, B, C); seams with the Time table; unstable dialect (no second encoding); findings; check output.
- Not written, on purpose: SOURCE-LICENSE.md, encoding.json, subject.json, README.md (the lead writes them); NEEDS-CORE.md (nothing needed from the keel beyond the S-T1 input, and the O 51 r 4(3) wiring note is in NOTES under Seams).
- Fix round of 2026-11-05 (after an independent review), applied: `check.sh` 1963 satisfied on both builds, seat 362 questions and 530 cases, srcrefs 637 src: lines and 421 locators, 0 problems in both modes; changes, one line each:
  - 1(a) `o 46A r 3(4)`: fees unpaid and not waived now JUST FALSE ("upon" counts as "where"); no special circumstances stays NOTHING (fork 46A.3). Sweep result, same ruling: `o 46A r 3(5)` no application now JUST FALSE; `o 46A r 1(7)(a)`, `(b)`, `(c)` no placing or removal order now JUST FALSE (fork 46A.5). The sweep is listed in NOTES under the Fork register.
  - 1(b) `o 56 r 6(1) issue of the enforcement order is barred`: firm against firm with no member in common now JUST FALSE; (a) still bars.
  - 1(c) `o 49 r 2(2)(b)`, `o 49 r 2(3)(b)`, `o 49 r 2(4)(b)`: input `the person is a lessee` split from `the person is a mortgagee, chargee or other person`; a lessee answers JUST FALSE.
  - 2 `o 47 r 2(3) production of the document by the Comptroller is barred` added (twin); `o 53 r 12(2)` takes the day in question and the day fixed (included, fork 53.4); `o 46 r 2(1)` functions renamed to name the Commissioner for Labour.
  - 3 forks 46A.3, 46A.4, 47.1, 47.2, 48.2 (`o 48 r 4(1)` without permission now JUST FALSE), 48.3, 49.1, 56.4, 46.4 (wording).
  - 4 Seams: which functions take the last day (checked, no change).
  - 5 new section "What the text does not answer (roc10)", built from this part's own NOTHING-kind comments.
- Left to do: nothing in this part.
