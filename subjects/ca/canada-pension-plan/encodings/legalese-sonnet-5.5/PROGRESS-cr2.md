# PROGRESS: piece cr2 (Canada Pension Plan Regulations, Part V, regulations 37 to 78.4)

Re-read this file, NOTES.md and the text after any compaction.

## How the files are made
The `.l4` files in this folder are generated from templates under `INPUTS_DIR/work/tmpl/` by `INPUTS_DIR/work/build.py`; quote lines are copied from the text by `srcrefs.py quote` (directive `@@Q first last`). NOTES.md is assembled by `INPUTS_DIR/work/assemble.py` from fragments in `INPUTS_DIR/work/notes/` and `INPUTS_DIR/work/cov/`. Edit the templates and fragments, not the generated files. `INPUTS_DIR/work/check.sh` runs check.sh, srcrefs and the `@ref` placement warnings.

## State (2026-10-24, after the usage-limit interruption)
DONE: layer 1 (17 modules + cr2-nouns), 17 test files, layer 2 `cr2-seat.l4` (130 `@export` questions, every input has `@desc`) and `cr2-cases-seat.l4` (245 assertions, every question has a case, 6 asserted NOTHING cases), NOTES.md assembled with every section written.
Last full `work/check.sh` (after the last .l4 edit): TOTAL 42 modules, 0 errors, 923 satisfied, 0 failed, 0 refused; srcrefs 446 src lines, 120 runs, 185 locators, 0 problems. Output saved in `work/last-check.txt`.
FINISHED. The three bare `NOT`s were parenthesised and the check rerun after the last `.l4` edit: TOTAL 42 modules, 0 errors, 923 satisfied, 0 failed, 0 refused; srcrefs 446 src lines, 120 runs, 185 locators, 0 problems; no `@ref` placement or unknown-annotation warning. The exact output is in NOTES.md under `## What check.sh prints`. `work/probes` was deleted. Nothing is left to do except the final report; if anything is edited later, edit the templates under `work/tmpl/`, rebuild with `work/build.py`, rerun `work/check.sh` and `work/assemble.py`.

## Module plan (text order) and state
| module | regulations | state |
| --- | --- | --- |
| cr2-nouns | declarations for all modules | done |
| cr2-interpretation | 37 | done, tests done |
| cr2-earnings-record | 39, 40, 41 | done, tests done |
| cr2-applications | 42, 43, 44, 45, 46, 46.1 | done, tests done |
| cr2-cancellation | 46.2 | done, tests done |
| cr2-age-and-identity | 47 to 51 | done, tests done |
| cr2-information-and-evidence | 52, 53, 54, 54.1 | done, tests done |
| cr2-division-dates | 54.2, 54.4 | done, tests done |
| cr2-payment-of-benefits | 55 to 59 | done, tests done |
| cr2-retirement-and-adjustment | 61, 62 | done, tests done |
| cr2-determination-and-death-benefit | 63, 64 | done, tests done |
| cr2-maintenance-and-school | 65, 65.1, 66, 67 | done, tests done |
| cr2-disability | 68 to 72 | done, tests done |
| cr2-reconsideration | 74, 74.1, 74.2 | done, tests done |
| cr2-pension-index | 75 | done, tests done |
| cr2-deductions-and-family-allowance | 76, 76.1, 77 | done, tests done |
| cr2-cohabitation | 78, 78.1, 78.2 | done, tests done |
| cr2-pension-adjustments | 78.3, 78.4 | done, tests done |
| cr2-seat, cr2-cases-seat | all questions | done |

## Decisions taken (and the provision that licenses each)
- GIVEN names in a rule head must be exactly the names in the GIVEN list (the stable binary rejects a mismatch); heads are therefore long. Keep input names short complements.
- Duties are BOOLEAN rules (the duty arises) plus a BOOLEAN form rule; no DEONTIC (not assertable). Licence: source-patterns 5.2 test; stated in NOTES.md intro.
- Rates are fractions except reg 41, where the text multiplies by 100 and halves the rate (fork F-41).
- "Reaches 60/65" always through the core's s 2(2) rule with `any other provision` (reg 43(1.1), 78.3, 78.4).
- Items lists (regs 46(2), 52, 53, 54, 54.1, 68(1), 72(2), 74.1(1)) are enumerations in cr2-nouns; which items "apply" is an input (the text says "as applicable" and does not say when).

## Files written
Layer 1: cr2-nouns.l4, cr2-interpretation.l4, cr2-earnings-record.l4, cr2-applications.l4, cr2-cancellation.l4, cr2-age-and-identity.l4, cr2-information-and-evidence.l4, cr2-division-dates.l4, cr2-payment-of-benefits.l4, cr2-retirement-and-adjustment.l4, cr2-determination-and-death-benefit.l4, cr2-maintenance-and-school.l4, cr2-disability.l4, cr2-reconsideration.l4, cr2-pension-index.l4, cr2-deductions-and-family-allowance.l4, cr2-cohabitation.l4, cr2-pension-adjustments.l4.
Tests: cr2-tests-{interpretation, earnings-record, applications, cancellation, age-and-identity, information-and-evidence, division-dates, payment-of-benefits, retirement-and-adjustment, pension-index, determination-and-death-benefit, maintenance-and-school, disability, reconsideration, deductions-and-family-allowance, cohabitation, pension-adjustments}.l4.
Layer 2: cr2-seat.l4, cr2-cases-seat.l4.
Notes: NOTES.md, PROGRESS.md.
