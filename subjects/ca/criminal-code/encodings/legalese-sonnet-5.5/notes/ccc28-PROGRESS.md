# PROGRESS.md -- part ccc28 (Criminal Code (Canada), lines 16296-16683: PART XXIV, PART XXV, PART XXVI)

State at 2026-11-17: everything in the brief and in the two resume tasks is written and checked; what remains is the final report.

## How the files are produced
- Sources are templates in `../../../work/src/*.l4.in` (outside the deposit: scratch). `work/build.py` expands `{{Q a b}}` into `-- src:` quote lines by calling `srcrefs.py quote`, and `{{T name}}` into table assertions parsed from the text lines by `work/tables.py`, and writes the layer-1 and test `.l4` files here.
- `work/seatgen.py` writes `ccc28-seat.l4` and `ccc28-cases-seat.l4` from one question list (expected values hand-written in that list).
- `work/coverage.py` writes the coverage table, `work/lint.py` checks the FALSE-kind and NOTHING-kind comments, `work/marginal.py` lists the branches that rest on a marginal reading, and `work/notes.py` (with `work/notes_data.py`) assembles `NOTES.md`.
- The `.l4` files and the three `.md` files here are the deliverable; the work folder is not shipped.

## Commands
- `S=<scratchpad>; L4=$S/bin/l4-main-110 L4_MAIN=$S/bin/l4-main-109 ./check.sh`
- `python3 -I srcrefs.py check --refs ../../../inputs/R.S.C.-1985-c.-C-46.txt ccc28-*.l4` and `--strict`

## Numbers
- Baseline before any edit of mine (2026-11-16): 3 modules (the keel's), 0 errors, 0 satisfied, 0 failed, 0 refused, same on 1.6.109.
- Last check.sh (2026-11-17, after the seat layer, the seat audit and the name-test sweep): 17 modules, 0 errors, 999 satisfied, 0 failed, 0 refused, identical on 1.6.109.
- Before the seat audit and the sweep (seat layer first written): 17 modules, 998 satisfied. After: 999 (one both-gates-fail assertion added for s 753.01(3)); the audit and the sweep otherwise changed names, comments and notes only.
- Per module satisfied: s752 tests 227, part24a 127, part24b 137, part24c 58, part25 189, part26 124, seat cases 137.
- srcrefs `--refs` and `--strict`: 307 src: lines, 153 runs, 180 locators, 0 problems over every `ccc28-*.l4`.
- #TRACE outputs of the two builds with `JL4_LIBRARY_PATH` unset: the full outputs are byte-identical (diff of 0 lines) for the five test files with regulative rules, and the `#TRACE` count of each file equals the evaluations printed by each build (part24a 10, part24b 3, part24c 7, part25 9, part26 3).

## Done
- Layer 1: `ccc28-part24-s752.l4`, `ccc28-part24a-dangerous-offender.l4`, `ccc28-part24b-long-term.l4`, `ccc28-part24c-hearing-appeal.l4`, `ccc28-part25-forfeiture.l4`, `ccc28-part26-extraordinary-remedies.l4`, each with its `ccc28-tests-*.l4`.
- Layer 2: `ccc28-seat.l4` (38 questions) and `ccc28-cases-seat.l4` (137 assertions).
- `NOTES.md` (coverage of all 383 non-blank lines, fork register, jural relations, marginal readings, seams, seat audit, name-test sweep, findings, stable-binary notes, check.sh output), `NEEDS-CORE.md`.
- Task 1, the second seat-question audit: 38 read, 4 retitled (ss 753(5), 753.1(3), 753.2(3), 774.1), 34 read and left; 15 assertions restated in place with `-- RECONCILED 2026-11-12`.
- Task 2, the name-test sweep: 8 flipped (written `NOTHING` from the first pass), 8 kept `JUST FALSE`, 17 listed (where/when/upon-kind), 1 listed (entitled); 0 functions named "it is lawful".

## Decisions taken (with the text that licenses each)
- Import `ccc-core` only; every section 2 answer is an input named `s 2 <term>: <the thing asked>` (PLAN.md section 4); the only one used is `s 2 superior court of criminal jurisdiction`, in two functions. The brief says layer 1 imports `ccc-definitions` too; where the brief and PLAN differ the brief governs, but nothing in the range needs a call into it.
- "means" definitions of s 752 close their lists: `JUST FALSE` when no limb holds (quote the "means" words).
- A provision is stated down to the paragraph the list names; a coarser statement is not matched (a limit of the inputs, said in NOTES).
- `ccc28-part24a` and `ccc28-part24b` take the answers of s 752 and s 753.1(2)(a) as inputs named for those sections; the seat passes one into the other.
