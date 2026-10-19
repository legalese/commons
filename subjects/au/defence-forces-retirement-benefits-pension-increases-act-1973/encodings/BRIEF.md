# Encoding brief: the Defence Forces Retirement Benefits (Pension Increases) Act 1973 (Cth), in L4

## The subject

**Defence Forces Retirement Benefits (Pension Increases) Act 1973**, Commonwealth of Australia, as made (assented to 19 June 1973), deposited at `../registers/source-bundle/C2004A00007.txt` (CC BY 4.0).

**Formulas missing from the deposited text.** The two formulas in s 4(2) are images in the official print. Read with the definitions of A-D, they are taken as the percentage rise in the CPI, ((A − B) ÷ B) × 100, and the percentage rise in average weekly earnings, ((C − D) ÷ D) × 100; this must be checked against the print.

## Seat

**The DFRB pensioner, or the widow** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level: *"By how much does my annual pension increase from 5 July 1973?"* Sections 4(2), (4), (5), 5, 7(1)(a), (2), (4), (5) and 12. Sections 6, 7(1)(b), (3), (6), 8-11 (suspended pensions, s 82ZB pensions, other DFRB sections, commutation, appropriation) are out of scope.

- s 5(1): only if A > B and C > D; not for a child's pension.
- s 4(2): the prescribed percentage is the lower of 1.4 × the CPI rise and the earnings rise; s 4(4): a fraction of a tenth below half is dropped, a half or more counts as a tenth.
- s 5(2): the increase is the prescribed percentage of 77.5% of the annual pension payable immediately before 1 July 1973.
- s 7: for a retirement or death on or after 1 October 1971, the increase is scaled by the months from the day after it to 30 June 1973, over 21; a part month of half or more counts, less is dropped (s 7(5)); under a month counts as one (s 7(4)).
- s 12: from the instalment due on 5 July 1973.

## Inputs

A, B, C, D; the annual pension immediately before 1 July 1973; the day of retirement or death; whether it is a child's pension.

## Rules that matter

- A failing assertion is a finding. Never edit an expected value to match the code.
