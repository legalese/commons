# PROGRESS -- Child Benefit (Rates) Regulations 2006 (S.I. 2006/965), agent `cbr`

Read this first after any compaction, then NOTES.md, then the text (../../registers/source-bundle/uksi-2006-965.txt, 87 lines).
Paths: INPUTS_DIR, DEPOSIT and L4_BIN are in the task message; the brief is `ta/cbr/BRIEF.md`.

## Status

- [x] orientation: brief, guide, both skills (selected references), dialects.md, source-locators.md, example seat
- [x] probes of the stable binary (1.6.98)
- [x] cbr-nouns.l4, cbr-reg1.l4, cbr-reg2-benefits.l4, cbr-reg2-couples.l4, cbr-reg2-rate.l4, cbr-reg3.l4, cbr-reg4.l4
- [x] cbr-tests-reg1, -reg2-benefits, -reg2-couples, -reg2-rate, -reg3, -reg4 (178 assertions, written equal to satisfied)
- [x] cbr-seat.l4 (13 questions), cbr-cases-seat.l4 (83 assertions, written equal to satisfied)
- [x] srcrefs check: 143 src: lines, 38 runs, 48 locators, 0 problems
- [x] check.sh (L4_TARGET=unstable): 15 modules, 0 errors, 261 satisfied, 0 failed, 0 refused
- [x] NOTES.md filled (all sections)
- [x] second advisor call before the final report
- [x] `ta/cbr/scratch/` deleted

## Decisions taken (with the text that licenses each)

See NOTES.md, "Fork register" (F1 to F15), for the readings and the text behind each.
In short: target dialect `main` (binary 1.6.98); not covered is `NOTHING`, never `FALSE` or `0`; every fact is tested on the first day of the week (reg 1(3)); the order of application is (1)(a), (4), (5), (2); the figures are those of the version of 2026-04-06 and earlier weeks are NOTHING; entitlement to child benefit is an input; reg 4 is data.

## Files written

All in `ta/cbr/deposit/encodings/legalese-sonnet-5.5/`:
cbr-nouns.l4, cbr-reg1.l4, cbr-reg2-benefits.l4, cbr-reg2-couples.l4, cbr-reg2-rate.l4, cbr-reg3.l4, cbr-reg4.l4, cbr-seat.l4,
cbr-tests-reg1.l4, cbr-tests-reg2-benefits.l4, cbr-tests-reg2-couples.l4, cbr-tests-reg2-rate.l4, cbr-tests-reg3.l4, cbr-tests-reg4.l4, cbr-cases-seat.l4,
NOTES.md, PROGRESS.md.
(check.sh and srcrefs.py were already there and are unchanged.)

## Next

Nothing: the final report is the next and last step.
