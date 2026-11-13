# PROGRESS (coa8: Companies Act 2006, lines 4656-5417, ss 362 to 414B)

Status on 2026-11-13: finished. Every file compiles on 1.6.110 with 0 errors and 0 warnings; `check.sh` printed TOTAL (29 modules) 0 errors, 1587 satisfied, 0 failed, 0 refused, the same on 1.6.109; `srcrefs.py check --refs` and `--strict` report 0 problems.
Scratch and generators are in DEPOSIT/../work/ (not shipped): `gen.py` expands the `@@Q`/`@@REF` placeholders of `work/src/*.l4.in` into the deposit, `genseat.py` and `seatspec.py` build `coa8-seat.l4`, `gencases.py` and `casespec.py` build `coa8-cases-seat.l4`, `cov.py` and `mknotes.py` build the coverage table and `NOTES.md`. Edit the sources there, never the generated deposit files.

## Files written
- Layer 1: coa8-helpers, coa8-part14-meanings, -authorisation, -remedies, -exemptions, coa8-part15-small, -records, -year, -accounts, -group, -notes, -approval, coa8-regulative.
- Tests: coa8-tests-helpers and one coa8-tests-<module> for each of the other eleven non-regulative modules (1173 assertions).
- Seat: coa8-seat.l4 (171 questions), coa8-cases-seat.l4 (414 cases).
- NOTES.md, NEEDS-CORE.md, PROGRESS.md.

## Decisions taken (with the section that licenses each)
See the fork register (F1 to F15), "Marginal readings for a lawyer" and the numbered findings in NOTES.md.
- Strong Kleene composition of limbs (helpers): a limb that decides decides; NOTHING survives only where no limb decides.
- s 366(2) with (3): NOTHING from (3) means no relief shown, so the company's own resolution is required (F6).
- s 391(5): the day of incorporation is day one of the first period (F7); an expectation of mine on this was wrong and was corrected from the text (finding 1).
- s 388(4): the anniversary day answers NOTHING (F8).
- Seat: borrowed seams are asked as plain true-or-false and passed as JUST; an optional date is asked with a yes-or-no input (finding 11).

## Inert rows
Reason 1: headings and cross-headings, s 362, s 364(1), s 380(2), s 382(7), s 391(7). Reason 2: s 377(2) and (4), s 385(4) to (6), s 409(1) to (3), s 412(1) to (3). Repealed or blank in this text: s 380(3) and (4), s 398, s 399(1), s 400(6), s 401(6), s 408(2), s 410, and the heading shown as dots.

## If this run is resumed
Re-run `python3 -I work/gen.py`, `genseat.py`, `gencases.py`, `./work/build.sh`, `check.sh`, then `python3 -I work/mknotes.py` after saving the check.sh output to `work/check-final.txt`.

## Follow-up of 2026-11-12 (done)
- Seat audit: 171 questions read; 0 direction mismatches, 14 subject mismatches retitled; 34 case assertions restated in place with `-- RECONCILED 2026-11-12`.
- Name-test sweep: 1 function flipped to NOTHING (s 405(2), fork F15, caller s 405(1) adjusted), 11 kept, 8 listed (where/when/upon, including the "provided" sites s 395(4A) and s 403(5A), first flipped and then put back and listed), 4 listed (entitled); 7 layer-1 assertions carry a RECONCILED comment (2 for s 405, 5 restoring s 395(4A), its caller s 395(3) and s 403(5A)); one new seat case (question 131).
- Details are in NOTES.md under "Seat audit of 2026-11-12" and "Name-test sweep of 2026-11-12".
