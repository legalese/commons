# Washington TANF and WorkFirst (chapters 74.12 and 74.08A RCW) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the parent or relative applying for or receiving TANF, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding; the text was first deposited on 2026-10-24 (commit `3266cda0d`).

## Edition

Chapters 74.12 and 74.08A RCW as printed on the full-chapter pages of app.leg.wa.gov/RCW, retrieved 2026-10-24 (UTC), deposited at `../../registers/source-bundle/rcw-74-12.txt` and `rcw-74-08a.txt` (unofficial). Includes RCW 74.08A.035, "Effective July 1, 2029".

**Amounts set by rule (ADMIN-POLICY).** The payment standard and the maximum earned income level are set by the Department of Social and Health Services (WAC chapter 388-478, not deposited): **inputs**. The figures in the cases are hypothetical.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wa-tanf.l4` | `wa-tanf-cases.l4` | 42 written, 42 satisfied |

Plus three `#TRACE`s of the participation rule with `-- expect:` comments (two FULFILLED, one breach by the recipient, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The parent or other relative** applying for or receiving TANF for a dependent child. Questions: "Is my child a dependent child?", "How much of our earnings counts?", "What is our grant?", "Can we still get TANF under the 60 months?", "How long is transitional food assistance?", "Do I have good cause?", "What happens if I do not take part in WorkFirst?", "Can we get diversion assistance?".

Defaults (2026-10-18):
- **The Act alone**: chapters 74.12 and 74.08A, read together as the TANF programme; the WAC amounts are inputs.
- **Actors**: the recipient and the department.
- **Judgments left to others**: hardship by rule, good cause findings, the department's exceptions for students (74.12.035(3)), the federal relative list and the court-ordered placement are asked as facts.
- **Definitions**: dependent child, countable earnings, the 60-month count with its exemptions, good cause are worked out from facts.
- **One case**: one family in one month.
- **Machinery out**: electronic benefit transfer, contracting, outcome measures, the oversight task force, reports.

## Federal frame

TANF is defined by reference to federal requirements (74.12.010: a relative "as specified under federal temporary assistance for needy families program requirements"; 74.08A.010(4)(b): the family violence option of section 402(a)(7) of Title IV-A). Title IV-A is deposited in `subjects/us/social-security-act/` (42 U.S.C. 601-619). Cross-folder IMPORT is not possible.

## Scope

**In:** 74.12.010; 74.12.035(1)-(2); 74.08A.010(1)-(2), (4)-(6); 74.08A.035; 74.08A.039; 74.08A.210; 74.08A.230; 74.08A.260(4), (5), (8); 74.08A.270(1), (5).

**Out:** 74.12.030's reference to RCW 74.08.025 (not deposited: "otherwise eligible" is asked); 74.12.250-.350 (protective payees, suitability of home); 74.12.255 and 74.08A.380 (teen parents); 74.12.450-.460 (the department's notices to an absent parent); 74.12.470 (diaper subsidy, set by rule); 74.08A.100-.130 (immigrants); 74.08A.250 (work activity, asked as a whole); 74.08A.280-.510.

## What the chapters turn out to say

1. **The statute gives the disregard, not the grant formula.** RCW 74.08A.230(1): "In addition to their monthly benefit payment, a family may earn and keep the first $500 of the family's earnings in addition to one-half of the family's remaining earnings". This encoding reads it as: half the earnings above $500 count against the payment standard, and the grant is the standard less countable income. The standard itself and the gross-earnings cutoff are department rules. Asserted on hypothetical figures.
2. **SSI is never counted, and from July 2029 neither is passed-through child support** (74.08A.039; 74.08A.035, "Effective July 1, 2029"). Asserted (grant 300 before, 400 after).
3. **The 60-month exemptions apply only from month 52.** "The department shall not exempt ... until after the recipient has received 52 months of assistance" (74.08A.010(5)). Combined with the pandemic extension (one extra month for each month received since March 2020 at 7 percent unemployment, 74.08A.010(4)(a)(ii); 74.08A.015), a family at month 61 with three such months is covered; at month 64 it is not. Asserted. The "unemployment rate 7 percent or more" hardship (4)(a)(iii) turns on a published rate, asked as a fact.
4. **The work sanction has two steps, months 2 and 12.** After two months of continuous noncompliance the grant is cut by the recipient's share or 40 percent, whichever is greater; after twelve it "must be terminated" (74.08A.260(4)). Good cause waives it (5); a carer of a child under two is outside it altogether (8). Encoded both as a computation (asserted) and as a rule whose `LEST` is a second obligation (traced).
5. **The under-two good cause is capped at 24 months in a lifetime** (74.08A.270(5)), while the work requirements are suspended for any parent or relative personally caring for a child under two (74.08A.260(8)) without that cap. The two overlap; the encoding keeps both as the text has them. Asserted.
6. **Diversion assistance is at most $2,000, once in 12 months, and only for a family otherwise eligible** (74.08A.210). Asserted. If the family goes onto TANF within 12 months the prorated value becomes a loan recovered from the grant; not computed.
7. **Transitional food assistance is five months**, unless the household left TANF in full-family sanction (74.08A.010(6)). Asserted.

## Before relying on it

- Deposit RCW 74.08.025 and the WAC payment standards and income rules (WAC 388-450, 388-478) and replace the inputs.
- An independent test pass.
