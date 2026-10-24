# MFIP (Minnesota Statutes ch. 142G, with ch. 256P) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `mfip.l4`: the statute's terms (assistance unit, transitional standard, family wage level, earned income disregard, initial income test, assistance payment, housing assistance grant) and the exported questions for the caregiver, each calling those rules. The duty to report a change by the tenth of the next month (256P.07, subd. 2) is a regulative rule. One case file, `mfip-cases.l4`; expected values worked out by hand.

There was no earlier encoding of this subject.

## Edition

- Minnesota Statutes 2025, ch. 142G (retrieved 2026-10-19), at `../../registers/source-bundle/mn-stat-ch-142G-2025.txt`. Eight provisions amended by the 2026 session (listed in the file's header: 142G.01, subd. 3; 142G.12, subd. 2; 142G.22, subd. 1; 142G.25; 142G.40, subd. 1; 142G.53; 142G.57, subds. 2, 4) are not in the deposited text; 142G.40, subd. 1 (the 60-month limit) is one of them.
- Minnesota Statutes 2025, ch. 256P, **deposited 2026-10-24 for this encoding** as its own subject, `../../../minnesota-statutes-chapter-256p-economic-assistance-program-eligibility-and-verification/`.
- The DCYF notice of the MFIP Transitional Standard effective 1 October 2026, 51 SR 472, at `../../../minnesota-state-register-mfip-transitional-standard-2026/registers/source-bundle/`. The notice cites 142G.17, subd. 5c, which the 2025 edition does not contain (the 2025 text has subd. 5(c) to the same effect).

**Inputs, not deposited:** the housing assistance grant as adjusted each October 1 (142G.32, subd. 1(b); $110 in the statute); which income is earned, unearned or excluded (256P.06 is deposited but not encoded); the 142G.33 allocation; deemed income (142G.31, subds. 1 to 4); the general conditions of 142G.11 to 142G.15 (one fact).

## Checks

- `mfip-cases.l4`: 22 assertions written, 22 satisfied, 0 errors, 0 warnings. One `#TRACE` (no report by day 10) prints `BREACH` by the assistance unit, as its `-- expect:` comment says.
- `mfip.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The caregiver** who applies for, or receives, MFIP for the family: "Can we get MFIP? How much a month? How much of my pay is disregarded? When must I report a change?"

Defaults:

- **The Act with the instruments that set its numbers.** The Transitional Standard from the deposited State Register notice; the housing grant's adjusted figure is an input.
- **The actors the text names.** The caregiver, the assistance unit, the agency, the commissioner.
- **Judgments and borrowed terms.** Certification of illness or incapacity (142G.31, subd. 6(b)) and the general conditions are asked as facts.
- **One case is one assistance unit in one month.**

## Scope

In: 142G.10, subd. 1; 142G.16, subds. 1, 2; 142G.17, subds. 1, 5, 7; 142G.31, subd. 6; 142G.32, subd. 1(a); 142G.40, subds. 1(a), 4(a) (as a count); 256P.02, subd. 2; 256P.03; 256P.07, subd. 2.

Out: 142G.11 to 142G.15 in detail; employment and training, sanctions and good cause (142G.50 to 142G.71); the diversionary work program (142G.90); proration in the month of application; hardship extensions (142G.42); vendor payments; the split of the payment into cash and food portions; the income rules of 256P.06 in detail.

## Links

MFIP is Minnesota's TANF programme: the commissioner spends the federal block grant (142G.03); Title IV-A is deposited in `subjects/us/social-security-act/` (42 U.S.C. 601-619). SSI recipients are excluded from the unit (142G.17, subd. 3(a)(1)); SSI is Title XVI of the same Act. The food portion of the Transitional Standard is SNAP under a federal waiver (142G.17, subd. 6; `subjects/us/food-and-nutrition-act-of-2008/`).

## What the Act turns out to say

1. **"Subtract this amount".** 142G.16, subd. 2(a) says "Apply an income disregard ... to gross earnings and subtract this amount from the family wage level". Read literally, "this amount" is the disregard, which would *raise* the payment as earnings rise. 142G.17, subd. 7 says "earned income is subtracted from the family wage level", so the encoding subtracts the earnings left after the disregard. Asserted (a family of three earning $1,065 gets $1,117).
2. **Where the support and unmet-need deductions go.** Subd. 2(b) disregards court-ordered support "from the income of the person with the legal obligation to pay support", and (c) makes the 142G.33 allocation, without saying against which income or in which order with (a) and (d). The encoding takes support off earned income and adds the allocation back to the result, capped at the transitional standard (142G.17, subd. 7: "The assistance payment may not exceed the transitional standard").
3. **Dependent care counts for the initial test only.** 142G.16, subd. 1(b)(2) deducts dependent care (up to $200 a child under 2, $175 for older children) in the initial income test, but subd. 2, which fixes the payment, has no such deduction. A family can pass the initial test and still get nothing. Asserted (earnings $3,400 with $400 of infant care).
4. **The "Over 10" figure.** The State Register prints "Over 10 | 256" with no rule for using it; the encoding adds $256 for each person beyond ten, as the deposit's header reads it (unverified there).
5. **The $1 floor.** Subd. 2 requires the result to be "at least $1": a family whose unearned income is just below the family wage level passes the initial test but gets no payment. Asserted.
6. **The reporting date.** 256P.07, subd. 2 sets "the tenth of the month following the month that the assistance unit's circumstances changed", a calendar date rather than a number of days; the regulative rule counts from the first of that month.

## Before relying on it

- Deposit the 2026 session laws amending 142G (notably 142G.40, subd. 1) and the commissioner's adjusted housing assistance grant.
- Encode 256P.06 (what counts as income) and 142G.31, subds. 1 to 4 (deeming), and 142G.11 to 142G.15.
- An independent test pass, and a person's check of findings 1 to 3.
