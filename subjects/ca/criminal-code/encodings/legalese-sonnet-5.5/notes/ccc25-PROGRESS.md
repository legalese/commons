# PROGRESS (ccc25, lines 14872-15170: Part XXII.1 Remediation Agreements and Part XXII.2 Alternative Measures and Restorative Justice Processes)

Final state 2026-11-17. Step A (first pass) and step B (seat-question audit pass 2, name-test sweep) are done; the final report is the last message of the run.
Trust the files in this folder over this note where they differ; NOTES.md carries the coverage table, the fork register and the numbers.

## Done
- Layer 1: ccc25-remediation-negotiation.l4 (ss 715.3-715.35), ccc25-remediation-approval.l4 (ss 715.36-715.43), ccc25-alternative-measures.l4 (ss 715.44-715.6).
- Tests: ccc25-tests-remediation-negotiation.l4 (135 asserts, 10 traces), ccc25-tests-remediation-approval.l4 (148, 38), ccc25-tests-alternative-measures.l4 (196, 20).
- Seat: ccc25-seat.l4 (54 questions), ccc25-cases-seat.l4 (147 asserts); second audit pass retitled 7 questions, 21 assertions carry RECONCILED comments.
- NOTES.md (all sections once), NEEDS-CORE.md, this file.
- Gates after the last edit: check.sh TOTAL 11 modules, 626 satisfied, 0 failed, 0 refused, 0 errors, same on 1.6.110 and 1.6.109 (baseline: 3 modules, 0 assertions; 623 after the first pass, +3 section-716 boundary cases for s 715.56); srcrefs --refs and --strict 0 problems; lint 0 problems; 68 traces match on both builds; 0 warnings.

## Method
- Layer-1 modules are templates in `../../../work/src/*.l4` (`@@Q a-b label@@` quote plus `@ref`, `@@R ...@@` an `@ref` only), expanded by `work/build.py` into this folder. Edit the template and rebuild; never edit a built layer-1 file by hand.
- Tests and the seat are written by `work/gen/gen1.py`, `gen2.py`, `gen3.py`, `gen_seat.py`, `gen_cases_seat.py` (expected values typed by hand in the scripts, cited to the text).
- `work/traces.py`, `work/lint.py`, `work/coverage.py`, `work/build_notes.py` check and assemble; `work/` is not shipped.

## Decisions taken
All forks are in NOTES.md, "Fork register (ccc25)": F1 to F30, with F2.1 to F2.7 (grant named "may" whose "if" gate fails answers NOTHING) and F8.1 to F8.16 (a duty whose gate is unmet answers JUST FALSE).
