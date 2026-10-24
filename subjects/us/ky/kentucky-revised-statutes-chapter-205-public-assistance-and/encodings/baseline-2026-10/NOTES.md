# KTAP (KRS 205.193, 205.200, 205.210 with 921 KAR 2:016) — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ky-ktap.l4`) states the rules in the texts' own terms (benefit group, payment maximum, standard of need, gross income limit, ratable reduction, work expense standard deduction, the cabinet), with two regulative rules: the recipient's ten-day report of an increase in earnings (921 KAR 2:016 Section 5(4)(b)) and the restriction on cash withdrawn with the EBT card (KRS 205.193(2)).
A **seat layer** (`ky-ktap-seat.l4`) asks the applicant's questions, each with `@export` and a `@desc` on every input.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

- Kentucky Revised Statutes (LRC; enactments through the 2026 Regular Session; database updated 10/19/2026), deposited at `../../registers/source-bundle/krs-205-public-assistance-ktap-ssp.txt` (retrieved 2026-10-19 UTC).
- **The instrument that sets the numbers:** 921 KAR 2:016 as current on the LRC register on 2026-10-19 (eff. 2-16-2023; expires 2/16/2030), deposited in `../../../kentucky-administrative-regulations-921-kar-2-015-and-2-016-state-supplementation-and-ktap-standards/registers/source-bundle/921-kar-2-016-ktap-standards-of-need-and-amount.txt`.

The payment maximum, standard of need and gross income limits are **deposited**. Section 9(6) adds Social Security cost-of-living adjustments since 2023 "to the extent funds are available"; those adjustments are not deposited, so the factor is an **input** (1 for the printed figures).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ky-ktap.l4` (core), `ky-ktap-seat.l4` (applicant seat) | `ky-ktap-cases.l4` | 25 written, 25 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Expected values worked by hand before the run; one hand figure (case J) was wrong in the first draft (it left out the $175 deduction) and was corrected from the text.
Regulative rules: 2. The report is asserted FULFILLED on day 8 and `#TRACE`d to a breach on day 12; the EBT restriction is `#TRACE`d to a breach.

## Seat

**The applicant**: the parent or relative with whom a needy child lives, applying for or receiving KTAP. "How much would we get each month? What is the most a family our size can get? Are our savings under the limit? I turned down a job: am I barred? My pay went up: by when must I report it?"
The cabinet's determinations (good cause, potential responsibility, the cost-of-living factor) are inputs.

Defaults (2026-10-18):
- **The Act and the regulation that sets its numbers.**
- **Actors the texts name:** applicant, recipient, the cabinet.
- **Judgments left to others:** as above.
- **Definitions:** the benefit group's size, countable income and the payment worked out from facts; "needy child", "full-time" and "part-time" employment, excluded income (Section 5(2)) asked as facts.
- **One case:** one benefit group, one month.
- **Machinery out:** appeals procedure (205.231), Medicaid verification (205.200(10)), state supplementation (205.245, 921 KAR 2:015), recoupment and refunds (Sections 11 to 14), the best-estimate method (Section 10).

## Scope

**In:** KRS 205.193(2), (3)(b); 205.200(2), (7); 921 KAR 2:016 Sections 3(2), 4(1), (2), 5(3)(a)-(e), 5(4), 9(2)-(6).
**Out:** technical eligibility (921 KAR 2:006, not deposited), the time limit, deeming of stepparent, minor parent and sponsor income (Sections 7, 8), lump-sum ineligibility periods (Section 4(3)), the two-time six-month new-employment disregard (Section 5(3)(g)), the state supplement to SSI.

## What the texts turn out to say

1. **A cliff at the first dollar of income.** KRS 205.200(2) says "In no instance shall grants to families with no income be less than the appropriate grant maximum", and 921 KAR 2:016 Section 9(4)(b) applies that to a family with no income. Every other family gets 55% of the deficit below the standard of need, capped at the payment maximum. For a family of three, no income gives $524; $100 of income gives 55% of $531 = $292.05. Asserted (cases A, B).
2. **The 45% ratable reduction is in both texts**: the statute allows 40% to 45%, the regulation takes 45%. Asserted.
3. **Three tests, then the payment**: gross non-KTAP income within the gross income limit (Section 4(1)); countable income, after the $175 work expense, dependent care and (for six months) 50% disregards, not over the standard of need (4(2)(b)); and a payment above zero (9(5)). Asserted (cases E, F, H).
4. **The earnings deductions are forfeit for a month** in which a worker, without good cause, cut or refused work in the previous 30 days or did not report a pay rise within ten days (Section 5(4)). Asserted (case J) and traced.
5. **The printed figures may be stale.** Section 9(6) makes the figures "the amount established in this section in addition to" SSA cost-of-living adjustments since 2023, "to the extent funds are available". Whether, and by how much, the cabinet has raised them is not in the deposited text.
6. **Assigned child support forwarded to the cabinet is deducted**, but the family is not a "no income" family, so it gets 55% of the deficit, not the payment maximum. Asserted (case K).

## Before relying on it

- 921 KAR 2:006 (technical eligibility, time limits) and the cabinet's current figures with COLAs deposited.
- An independent test pass; a check against a KTAP notice.
