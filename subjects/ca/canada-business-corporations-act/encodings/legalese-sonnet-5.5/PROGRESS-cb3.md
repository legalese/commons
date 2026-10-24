# PROGRESS -- piece cb3 (CBCA Parts XI to XIV.1, src lines 1550-2095)

Last updated 2026-10-22 at the end of the run: every section of the range is encoded, tested and asked about from the seat.
`L4=<L4_BIN> L4_TARGET=unstable ./check.sh` over this folder: exit 0, 25 modules, 0 errors, 1900 satisfied, 0 failed, 0 refused (the output is in NOTES.md under "What check.sh prints").
`python3 -I srcrefs.py check --refs <raw text> cb3-*.l4`: 0 problems.

## State of the work

The scratch workshop that generated the modules (templates, test generators, the coverage-table and seat generators, probes) was kept in a `work/` directory beside this folder while the work was done, and was deleted at the end of the run (checked: `DEPOSIT` holds only `encodings/`).
From now on the `.l4` files in this folder are the source: edit them directly.
`NOTES.md` was assembled from pieces by a script that no longer exists; edit `NOTES.md` directly too, and keep its coverage table, fork register and findings in step with any change to a rule.

## Modules (all `cb3-` prefix, flat folder)

| module | sections | tests | status |
| --- | --- | --- | --- |
| cb3-nouns.l4 (the `Penalty ceiling in Parts XI to XIV` type only) | - | - | done |
| cb3-part11-insider-trading.l4 | 126-131 | cb3-tests-part11-insider-trading.l4 (193) | done |
| cb3-part12-meetings.l4 | 132-136 | cb3-tests-part12-meetings.l4 (109) | done |
| cb3-part12-proposals.l4 | 137 | cb3-tests-part12-proposals.l4 (109) | done |
| cb3-part12-voting.l4 | 138-142 | cb3-tests-part12-voting.l4 (110) | done |
| cb3-part12-requisition-agreements.l4 | 143-146 | cb3-tests-part12-requisition-agreements.l4 (97) | done |
| cb3-part13-proxies.l4 | 147-154 | cb3-tests-part13-proxies.l4 (224) | done |
| cb3-part14-statements.l4 | 155-160 | cb3-tests-part14-statements.l4 (110) | done |
| cb3-part14-auditor.l4 | 161-172 | cb3-tests-part14-auditor.l4 (239) | done |
| cb3-part14-1-diversity.l4 | 172.1 | cb3-tests-part14-1-diversity.l4 (22) | done |
| cb3-seat.l4 | the seat layer, 299 questions in 28 groups | cb3-cases-seat.l4 (687 cases) | done |

Counts: 1213 assertions in the tests of layer 1, 687 in the seat's cases, 1900 in all.

## Decisions taken (with the text that licenses each)

1. Duties are encoded as assertion-testable decision rules (does the duty arise; the last day; was it met), not as DEONTIC or `#TRACE` state machines: `check.sh` counts only `#ASSERT` lines. No regulative wrappers.
2. Rule heads are one backtick segment followed by arguments, named `<what it decides> within s N`; no multi-segment mixfix, so no head keyword can collide across pieces.
3. Every "prescribed" thing is a plain input (the regulations are not a source).
4. Time limits use the core's `Time limit`; "forty-eight hours", "business day" and "trading days" are not in the core's units, so the computed cut-off or average is a plain input (NOTES.md, "Needs from the core").
5. The range holds no enactment, assent or commencement provision: nothing is carried as a date.
6. Each marginal-note heading is covered by the row of the subsection it heads and named in that row's provision cell; the five Part headings have their own inert rows.
7. A court's or the Director's discretion is never decided; the rules say who may apply and on what ground.
8. The seat layer calls the layer-1 rules and restates none; a conclusion the person cannot state (for example whether management must send a form of proxy) is computed inside the question from facts the person can state.
9. The seat asks a value that may be absent as a yes-or-no flag plus the value, rebuilt as a `MAYBE` inside the question.
10. Each of the twelve offences with a stated ceiling is asked in a set: whether the duty arises, whether it was met, whether it is an offence, and two ceilings (the fine in dollars, and the imprisonment in months as a `MAYBE NUMBER`, `NOTHING` where the text states a fine only).

## Corrections made after a failing run (recorded as findings in NOTES.md)

- The reimbursement of s 143(6): the seat case was first written with the wrong expectation and corrected from the text (finding 26, F-143-6).
- The unanimous written resolution under s 162(1): the seat case was first written as `TRUE` and corrected to `FALSE`, because the written route is s 142(1)(a) (finding 56).

## Not done, and why

- Nothing in the range is left out; the coverage table has 252 rows (212 encoded, 28 fork, 7 repealed or blank, 5 inert Part headings).
- No check against the other pieces' names has been possible: the lead will find a clash only at the merge.
- The seat's wording has not been tried on the website's Interact form.
