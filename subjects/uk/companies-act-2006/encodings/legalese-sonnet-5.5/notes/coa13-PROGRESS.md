# PROGRESS (coa13: Companies Act 2006, lines 7556-8205, ss 540-609)

Status 2026-11-13: DONE. All sections encoded, tested, seat layer and cases written, NOTES.md assembled.

Authoring method: files are written as `work/src/<name>.in` (under DEPOSIT/../work/, not shipped) with `@@Q a b@@` macros that `work/gen.py` expands into `-- src:N | text` quote lines via `srcrefs.py quote`; `gen.py` writes the deposit files. `work/coverage.py` + `work/coverdata.py` build the coverage rows from the text and the `@ref` lines; `work/build_notes.py` + `work/notes_text.py` assemble NOTES.md; `work/traces.sh` runs the regulative traces on both builds; `work/s.sh` summarises one file.

Binary: L4_BIN = `<scratchpad>/bin/l4-main-110`, L4_MAIN = `.../bin/l4-main-109`. Baseline `check.sh` before my work: 2 modules (coa-core, coa-definitions), 0 assertions, 0 errors. After: 18 modules, 1122 assertions satisfied, 0 errors, same on both builds.

| module | sections | tests | status |
| --- | --- | --- | --- |
| coa13-ch1-shares.l4 | ss 540-548 | coa13-tests-ch1.l4 (73) | DONE |
| coa13-ch2-allotment.l4 | ss 549-559 | coa13-tests-ch2.l4 (183) | DONE |
| coa13-ch3-preemption.l4 | ss 560-577 | coa13-tests-ch3.l4 (247) | DONE |
| coa13-ch4-undersubscribed.l4 | ss 578-579 | coa13-tests-ch4.l4 (49) | DONE |
| coa13-ch5-payment.l4 | ss 580-592 | coa13-tests-ch5.l4 (156) | DONE |
| coa13-ch6-valuation.l4 | ss 593-609 | coa13-tests-ch6.l4 (276) | DONE |
| coa13-regulative.l4 | the duties that name a party | coa13-tests-regulative.l4 (3 asserts + 23 traces read by hand) | DONE |
| coa13-seat.l4, coa13-cases-seat.l4 | 59 questions | 135 assertions | DONE |
| NOTES.md, NEEDS-CORE.md | | | DONE |

## Decisions taken (and the section that licenses each)

All are in NOTES.md "Fork register (coa13)": F-signposts, F-substitution, F-exception, F-periods, F-interest, F-546, F-547, F-549, F-551(4)(a), F-554, F-557(2)(b), F-561(5), F-562(4), F-562(5), F-574(2), F-578, F-AFTER, F-ceased, F-586(4), F-588, F-596(5), F-597(2), F-598(2), F-599(1), F-company-A, F-ordinary, F-seat, F-defence, and the 33 bare-"must" sites.

## If this run is resumed

Re-read NOTES.md, this file and the text, not a summary. To change a module edit `work/src/*.in`, run `work/gen.py`, then `check.sh`, then `work/coverage.py` and `work/build_notes.py` (after re-running `check.sh > work/checkout.txt`).

## Seat audit and name-test sweep of 2026-11-12 (lead's requests)

Seat audit: 59 seat questions read against the functions they return; 1 direction mismatch (s 571) and 7 subject mismatches retitled (ss 549(4), 554(1), 554(4), 556, 572, 586(1), 587(1)).

Name-test sweep (by `instructions/name-test-sweep.md`, which supersedes the first version): 56 functions whose names contain may / permitted / power / entitled / authorised read; 12 flipped to NOTHING for a failed "if" gate (fork F-grant-gate), 18 kept JUST FALSE, 5 "may"-with-"where" and 3 "entitled" functions listed in the fork register and not flipped. The first version's flips of `s 550`, `s 570(1)`, `s 571(1)`, `s 604(2)(a)` and the "where" branches of `s 581(c)` and `s 606(6)` were reverted.

Assertions restated in place with `-- RECONCILED 2026-11-12: was ...`: 17 in the layer-1 tests and 22 in `coa13-cases-seat.l4` (18 retitles, 4 value changes). check.sh TOTAL unchanged: 18 modules, 1122 satisfied, 0 errors, same on both builds.
