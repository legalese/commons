# Delaware Code Title 31, chapter 5, with DSSM 4000: Temporary Assistance for Needy Families — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, from the seat of the applicant or recipient, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

- **The Act:** The Delaware Code Online, Title 31, chapter 5, "includes all acts enacted as of September 10, 2026, up to and including 85 Del. Laws, c. 518", deposited at `../../registers/source-bundle/de-code-t31-ch05-2026-09-10.txt` (retrieved 2026-10-19).
- **The instrument brought in:** the Delaware Social Services Manual 4000, Financial Responsibility (16 Del. Admin. Code 4000), as published in the Delaware Administrative Code on 2026-10-19 (latest amendment cited 29 DE Reg. 530 (12/01/25)), deposited in the sibling subject at `../../../delaware-administrative-code-title-16-dssm-4000-financial-responsibility/registers/source-bundle/de-admin-code-16-dssm-4000-financial-responsibility.txt`. s 503(d) leaves "Eligibility for and the amount of assistance ... under Temporary Assistance for Needy Families" to "rules and regulations made by the Department", and DSSM 4000 is that rule; it is brought in under the 2026-10-18 scope default (the Act with the instruments that set its numbers). The encoding sits in the Act's folder because the stable `l4` cannot IMPORT across folders. `SOURCE-LICENSE.md` here holds both subjects' terms.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `de-tanf.l4` | `de-cases-tanf.l4` | 38 written, 38 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Expected values were worked by hand from the steps in DSSM 4008.1.1 and 4008.1.2.

## Seat

**The applicant for, or recipient of, TANF:** the parent or caretaker relative who applies for the family. Questions: "What are the standards for my family?", "Does my family pass the TANF tests?", "How much would our grant be?" (with the printed standards, or with the current notice's), "Until when may I appeal?", "May I appeal?".

The Department of Health and Social Services (Division of Social Services) appears only as what it must or may do to the family. The Superior Court appears as where the appeal goes.

The 2026-10-18 defaults:

- **Scope:** the Act with the instrument that sets its numbers (DSSM 4000).
- **Actors:** the applicant or recipient, the family budget group, the Department, the Superior Court.
- **Judgments handed to others:** none needed; the disregard stage, the budget group size and applicant or recipient status are facts the person can state.
- **Definitions** worked out from facts: the net incomes and the grant (DSSM 4008); "applicant" and "recipient" (DSSM 4008: no assistance "in at least one of the four months immediately preceding the application") is asked as one fact.
- **One case:** one family budget group, one month.
- **Departure:** the earned-income questions take one wage earner; the core takes a list of earners.
- **Machinery out:** ss 512, 513, 519, 521, 522 and the Medicaid coverage sections.

## Scope

**In:** 31 Del. C. s 503(a), (d); s 510; s 520. DSSM 4002.2 (TANF resources), 4004.2 (the $90, $30 plus 1/3 and $30 disregards, dependent care), 4004.5 (EITC disregarded), 4004.6 (children's earnings disregarded), 4005.1 (child support), 4007 (the $10 floor), 4007.2 (the printed standards), 4008, 4008.1.1, 4008.1.2.

**Out:** General Assistance (DSSM 4004.3, 4007.1, 4009, s 503(c)); pregnant women (4010); sponsored aliens (4011); the budget group rules (4001: the size is an input); resources other than the limit (4002.1, 4002.3 to 4002.7); step-parent and grandparent income (4005.3, 4005.4); excluded income (4006); reduced employment (4004.4); the child support supplemental payment (4008.2); technical eligibility, time limits and work rules (DSSM 3000, not deposited); sanctions (s 518).

## Read with

- `subjects/us/social-security-act/` (Title IV-A, TANF, not deposited there).
- `../../../delaware-code-title-30-state-taxes-chapter-11-personal-income/encodings/baseline-2026-10/`: the Delaware EITC. DSSM 4004.5 disregards "All EITC payments" for eligibility and payment, so EITC is not entered as income here.

## What the texts turn out to say

1. **The deposited standards are dated 2002-03.** DSSM 4007.2 heads its table "Current for 10/2002 - 9/30/2003". DSSM 4007 ("See Current COLA Administrative Notice") and 4008 ("refer to the most recent Cost Of Living Adjustment (COLA) Administrative Notice for the up to date Income Eligibility Standards") send the reader to a notice that is not in the Administrative Code and not deposited. So the questions come in two forms: one with the printed figures (family of 3: $1,737 / $939 / $338), and one taking the current standards as inputs. The standard of need is described as "75% of the Federal Poverty Level". Asserted.
2. **Two of the worked examples in DSSM 4008.1.3 do not follow from the steps.** Applicant Example #2 prints a deficit of $600 and a grant of $300. The steps give net earnings of $186.67 (the example's $186), a deficit of $752.33 and half of it $376.17, capped at the $338 payment standard: $338. Applicant Example #1 prints "$460 < $338" where $460 exceeds $338 (it reaches the right result, denial), and both it and the Recipient Example print "$500 < $1,737" for a gross income of $550. The encoding follows the steps. Asserted (Example #2: $338; Example #1: denied).
3. **"Exceeds" in the steps, "less than" in the overview.** Each step says "Deny assistance if the income exceeds" the limit. The opening of DSSM 4008 says "A family's income must be less than the gross and net income limits". They part only when income equals the limit. The encoding follows the steps, so income equal to the limit passes. Asserted (gross income $1,737 passes).
4. **No rounding is stated for TANF.** The Recipient Example rounds the one-third disregard up ($93.33 to $94) and the grant down ($301.50 to $301); the GA rule in DSSM 4009 says "Round remainders by dropping the cents", but the TANF steps say nothing. The encoding does not round. Asserted (Recipient Example: $1,807/6, about $301.17).
5. **Child support counts for eligibility but not for the grant.** DSSM 4005.1: the first $50 a month is disregarded for eligibility, the rest is counted, and "If a unit is determined financially eligible, child support is disregarded in determining the amount of the grant". Asserted ($800 unearned and $200 support: denied; with $50 support: a grant of $69.50 not reduced by the support).
6. **Applicants and recipients face different net tests.** An applicant's net income takes only the $90 and dependent care, and is compared with the payment standard; a recipient's takes the $30 plus 1/3 too, and is compared with the standard of need. The grant for both uses all the disregards. Asserted.
7. **Fill the Gap pays half the deficit, up to the payment standard.** "Multiply the deficit by 50% ... The grant is either the remainder or the payment standard whichever is less", and nothing under $10 is paid (DSSM 4007). Asserted ($19.50 paid; $7 not).
8. **The resource limit is $10,000 for TANF** (and $1,000 for GA, not encoded): "not eligible for TANF if its available resources exceed $10,000.00". Asserted.
9. **The Act's own bars sit outside the regulation:** a transfer of property worth $500 or more without fair consideration within 2 years (s 503(a)), being an inmate of a public institution (s 503(a)), and not suing or cooperating for nonsupport (s 503(d)). Asserted.
10. **The reporting duty has no deadline.** s 510 says the recipient "shall notify the Department promptly"; its only stated consequence is that an excess paid "shall be recoverable in a civil action". The rule has no `WITHIN`. The appeal to the Superior Court must be filed "within 30 days of the day of the final administrative decision", and only where the decision "would result in financial harm" (s 520). Asserted.

## Before relying on it

- Deposit the current COLA Administrative Notice and use its standards (finding 1).
- Deposit DSSM 3000 (technical eligibility, time limits, work requirements) and DSSM 5000 (fair hearings).
- Encode the budget group (4001) and the excluded income list (4006).
- An independent test pass.
