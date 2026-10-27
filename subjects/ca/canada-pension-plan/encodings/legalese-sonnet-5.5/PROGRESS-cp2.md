# PROGRESS: piece cp2 (Part I, Divisions C, D, E: Act lines 587-920)

Last updated 2026-10-24: everything is DONE: eight layer-1 modules and their tests (sections 21 to 41), the seat layer, the seat cases and NOTES.md; the final gate has run (see "State at the final check"). Re-read this, NOTES.md and the text after a compaction or an interruption, never a summary.

## Method

- Layer 1 modules are `cp2-*.l4`, one per natural group of the text.
- Drafts are `work/src/<module>.l4.src` (outside the deposit, in `../../../work/src/`). A line `@@Q N M@@` in a draft is expanded into the `-- src:N | text` quote lines by `python3 -I ../../../work/expand.py <draft>`, which writes the module into this folder. Quote lines are never typed by hand.
- `../../../work/gate.sh` runs `check.sh` (L4_TARGET=unstable), `srcrefs.py check --refs` on the Act file for all `cp2-*.l4`, and `l4 check` on each `cp2-*.l4` for warnings and `@ref` placement. It takes over 120 s once there are many test files: run it in the background.
- NOTES.md fragments (coverage rows, fork rows, cross-reference rows, jural-relation rows) are kept in `../../../work/notes/{cov,fork,xref,jural}-NN.md`, one set per module, and were pasted into NOTES.md by `../../../work/assemble_notes.py`; NOTES.md is filled.
- Binary: stable `l4` 1.6.98. The brief's `check.sh` command: `L4=<bin> L4_TARGET=unstable ./check.sh`.

## Plan (modules) and status

| module | sections | status |
| --- | --- | --- |
| `cp2-employer-deduct-and-remit.l4` + `cp2-tests-employer-deduct-and-remit.l4` | 21, 21.01, 21.1 | DONE: 0 errors, 108 satisfied; notes fragments 01 written |
| `cp2-assessment-and-recovery.l4` + `cp2-tests-assessment-and-recovery.l4` | 22, 23 | DONE: 0 errors, 66 satisfied; notes fragments 02 written |
| `cp2-records-and-inspection.l4` + `cp2-tests-records-and-inspection.l4` | 24, 25, 26 | DONE: 0 errors, 117 satisfied; notes fragments 03 written |
| `cp2-rulings-and-appeals.l4` + `cp2-tests-rulings-and-appeals.l4` | 26.1, 27, 27.1, 27.2, 27.3, 28, 29 | DONE: 0 errors, 84 satisfied; notes fragments 04 written (F15, F16, F17) |
| `cp2-self-employed-returns.l4` + `cp2-tests-self-employed-returns.l4` | 30, 31, 32, 35 | DONE: 0 errors, 60 satisfied; notes fragments 05 written (cov, fork F18-F23, xref, jural) |
| `cp2-self-employed-payment.l4` + `cp2-tests-self-employed-payment.l4` | 33, 34, 36, 37 | DONE: 0 errors, 98 satisfied; srcrefs 0 problems (run on the module alone) |
| `cp2-refunds.l4` + `cp2-tests-refunds.l4` | 38, 39 | DONE: 0 errors, 99 satisfied; notes fragments 06 written (F24, F25) |
| `cp2-regulations-and-offences.l4` + `cp2-tests-regulations-and-offences.l4` | 40, 41 | DONE: 0 errors, 66 satisfied; notes fragments 07 written (F26, F27, F28; includes the Division E heading rows and the s 40(1) paragraph rows) |
| `cp2-seat.l4`, `cp2-cases-seat.l4` | seat layer | DONE: 177 questions; cases file 397 satisfied |
| NOTES.md | all sections | DONE: assembled from the fragments, check.sh output pasted |
| coverage rows for the Division/group headings | | written inside cov-04/05/06/07 |

Last gate run (23 modules, the final one): 0 errors, 1095 assertions satisfied, 0 failed, 0 refused; `srcrefs check --refs`: 313 src: lines, 113 runs, 197 locators, 0 problems.

## Decisions taken (with the section that licenses each)

- Constitutive rules, not deontics: a "must" is the BOOLEAN that the duty arises, a "may" the BOOLEAN that the power exists (phrasebook 5.1, 5.2, 5.5); penalties and consequences are separate NUMBER rules. Licensed by the text's own modals throughout.
- "employer", "employee", "employment" reached through the record `cp2 Employment relationship` and the keel's `s 2(1) — an employer` etc. (ss 21(1), 24(1)).
- Time limits go through the keel's `a date is within a time limit after a start date` and `the date a time limit ends`: the last day is inside (keel F1, F7).
- Income Tax Act and other Acts not deposited: the rule says the provision applies and takes its effect as a supplied BOOLEAN (fork F10).
- The Regulations are cr1's and cr2's: amounts, prescribed rates and prescribed persons are inputs with a comment `-- out of range: ...`.
- Fork numbers used: F1 to F32 (the register in NOTES.md). The fragments are fork-01 to fork-08.

## Files written (all in this folder)

Layer 1 (8 modules): cp2-employer-deduct-and-remit.l4, cp2-assessment-and-recovery.l4, cp2-records-and-inspection.l4, cp2-rulings-and-appeals.l4, cp2-self-employed-returns.l4, cp2-self-employed-payment.l4, cp2-refunds.l4, cp2-regulations-and-offences.l4.
Layer-1 tests (8 files, one per module): cp2-tests-<same suffix>.l4.
Layer 2: cp2-seat.l4 (177 questions) and cp2-cases-seat.l4 (397 assertions).
PROGRESS.md; NOTES.md (assembled from the fragments in ../../../work/notes/).

## Seat layer: how it is being built (read this after an interruption)

- Drafted in chunks under `../../../work/seat/`: header.l4 (imports), a.l4 (helpers + employee Division C questions), b.l4 (s 25 inspections), c.l4 (self-employed returns and payment), d.l4 (refunds), e.l4 (offences), f.l4 (employer, director, representative group). Each chunk is checked with `../../../work/seatbuild.sh <chunks>` (concatenates header + chunks into work/merge/seat-test.l4 and runs `l4 check`; it takes about 35 s, run it in the background). The final `cp2-seat.l4` is header + intro comment + all chunks in order; then `cp2-cases-seat.l4`.
- Status: DONE. `../../../work/assemble.py` builds the deposit's `cp2-seat.l4` (header + intro + a part 1 + f + b + a part 4 + a2 + c + d + e) with 177 `@export` questions; `cp2-cases-seat.l4` is generated by `../../../work/cases/gen.py` from the hand-written table `cases.py` (plus `cases_new.py` for the last eight questions) and has 397 assertions, all satisfied in the final gate.
- Rules learned: arguments of a rule call on continuation lines must be indented MORE than the column where the function name starts (so put `MEANS` body on its own line); a call used as an argument must be in parentheses; take no MAYBE or LIST inputs (split into a BOOLEAN plus a DATE or NUMBER and build JUST/NOTHING with the helper `cp2 seat — the day it happened, if it did`); enumerations from layer 1 may be inputs ("a choice from a list") but the `@desc` must list the choices; a rate is asked in per cent per year and divided by 100 inside.
- Seat questions are named `<question> (s N)`; every `@export` text ends with `(s N)?`.

## State at the final check (read this after an interruption)

- DONE. All .l4 files are written, and nothing in them has been edited since the final gate ran.
- Final gate, run after the last .l4 edit: `L4_TARGET=unstable ./check.sh` printed `TOTAL (23 modules)  0 errors  1095 satisfied  0 failed  0 refused`, exit status 0 (the eight tests files 698, the seat cases file 397); `srcrefs.py check --refs` 0 problems (313 src: lines, 113 runs, 197 locators); the `l4 check` placement and warning scan printed nothing.
- The check.sh output is pasted verbatim into NOTES.md under `## What check.sh prints`, with the `--strict` result (10 problems, not asked for by the brief, left as they are).
- Coverage table: 129 rows (86 encoded, 22 fork, 19 inert, 2 repealed or blank); all 27 section labels have a row.
- What is left: the advisor call and the final report. No .l4 or NOTES.md edit is pending.
- Do not use broad `pkill -f` patterns: an earlier one may have killed another agent's `./check.sh` (the lead has been told).

## Facts for NOTES.md (found while working)

- The range holds no date of enactment, assent or commencement: the only dates are the days the Act counts from, and the effective-date rules at s 40(3) and (4), which are encoded.
- `5%` followed by further arguments is a loud arity error (the postfix `%` absorbs the following tokens): write `(5%)` in an argument list. `5% EQUALS` is fine.
- `MAYBE LIST OF NUMBER` is a parse error; write `MAYBE (LIST OF NUMBER)`.
- macOS `sed -i` needs a backup-suffix argument; a helper script of mine used python instead (not a finding about L4).
- `IF NOT f x THEN` inside BRANCH needs `IF (NOT ...)`; the brief already says parenthesise NOT.
