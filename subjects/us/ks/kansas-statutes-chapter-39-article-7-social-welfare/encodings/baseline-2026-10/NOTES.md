# Kansas TANF (K.S.A. 39-702, 39-709, 39-719b, 39-7,124, 39-7,127; K.A.R. 30-4-100, 30-4-101) — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ks-tanf.l4`) states the rules in the act's own actors and terms (applicant, recipient, dependent child, family group, the secretary, the assistance plan, the basic and shelter standards), with three regulative rules: the recipient's duty to report changes (39-719b(a)), the applicant's duty to complete a work program assessment module (39-709(b)(6)), and the bar on prohibited uses of TANF (39-709(b)(10)).
A **seat layer** (`ks-tanf-seat.l4`) asks the applicant's questions, each with `@export` and a `@desc` on every input.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

- Kansas Statutes online (Office of Revisor of Statutes, read 2026-10-20; 2025 session laws), deposited at `../../registers/source-bundle/ksa-39-7-public-assistance-tanf.txt` (retrieved 2026-10-19 UTC). Unofficial; 2026 session laws not checked.
- **The instrument that sets the numbers:** K.A.R. 30-4-100 and 30-4-101 from the Secretary of State's 2022 Kansas Administrative Regulations, Volume 3 (regulations filed through 31 December 2021), deposited in `../../../kansas-administrative-regulations-30-4-100-to-30-4-102-tanf-payment-standards/registers/source-bundle/`. Any later Kansas Register amendment was not checked.

The basic and shelter standards are **deposited**. The rules that count income against them (K.A.R. 30-4-110 to 30-4-113) are **not**, so the encoding gives the payment standard (the most a plan can receive before income), not the grant.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ks-tanf.l4` (core), `ks-tanf-seat.l4` (applicant seat) | `ks-tanf-cases.l4` | 46 written, 46 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Expected values worked by hand before the run.
Regulative rules: 3. Two asserted FULFILLED when kept; the assessment duty and the prohibition `#TRACE`d to breaches with `-- expect:` lines.

## Seat

**The applicant**: the parent or relative applying for, or receiving, TANF for a child. "Is my child a dependent child? Do we meet the general requirements? Have we used up the time limit? How many hours a week must we work? How long is my penalty? What is the most TANF pays a family our size in our county?"
The secretary's determinations (insufficient income and resources, a hardship extension, good cause, the premature-child extension) are inputs, worded as what the department has found.

Defaults (2026-10-18):
- **The act and the instrument that sets its numbers.**
- **Actors the text names:** applicant, recipient, the secretary for children and families, the department.
- **Judgments left to others:** as above, asked as facts.
- **Definitions:** dependent child (39-702(g)), the general requirements (39-709(a)), the time limit (39-709(b)(3)), the work hours (39-709(b)(8)(B)) worked out from facts; "gross misconduct", "non-cooperation" (39-702(n), by rules) asked as facts.
- **One case:** one family group, one application.
- **Machinery out:** food assistance, child care subsidy and medical assistance (39-709(c) to (e)), drug screening (39-709(f)), liens, waivers (39-7,130, 39-7,131, 39-7,165), the corporate tax credit (39-7,132).

## Scope

**In:** 39-702(g); 39-709(a)(1), (a)(2) first sentence; 39-709(b)(3), (5), (6), (8)(B), (8)(D), (8)(G), (9), (10); 39-719b(a); 39-7,124; 39-7,127(a)(1); K.A.R. 30-4-100(b), 30-4-101(a), (b).
**Out:** the grant after income (rules not deposited); 39-7,125 (family cap on additional children), because its increments depend on the schedule of benefits and income rules not deposited; drug screening; the food assistance, child care and medical programs in the same section.

## What the texts turn out to say

1. **The time limit is 24 months, 36 with a hardship extension**, counted for any adult in the family group from October 1996, including TANF from another state; no extension beyond 36 months (39-709(b)(3)). Asserted.
2. **The payment standard is the basic standard plus a county shelter standard**: a mother and two children in Johnson County have $429 a month before income is counted; in Sedgwick County, living with a relative outside the plan, $359.40, because the shelter standard is cut by 40% (K.A.R. 30-4-100(b)(2)). Asserted.
3. **The statute and the rules disagree on the earned income disregard's status.** 39-7,127(a)(1) states "a $90 work expense plus 40% of the gross monthly earned income above the $90", but (b) says it is to be implemented "only if such waivers to federal program requirements have been obtained". Whether the waivers exist is not in the deposited text; the encoding computes the statutory figure. Asserted.
4. **Penalties escalate to ten years**: 3 months, 6 months, a year and full cooperation, then 10 years, for non-cooperation with work programs (39-709(b)(8)(G)) and, separately, with child support services (39-709(b)(9)). Asserted.
5. **"Immediately" has no number.** 39-719b(a) makes it the recipient's duty "to notify the secretary immediately" of a change. The rule is encoded with no deadline, so it cannot be traced to a breach by time alone; a trace shows it fulfilled when the notice is given.
6. **A minor parent's grant depends on where she lives** (39-7,124), with three exceptions. Asserted.
7. **The 39-709(a)(2) bar is wide**: anyone who "voluntarily quits employment" is ineligible for public assistance, with no period stated and no good-cause exception in the text (rules may define one). Asserted.
8. **The 39-7,124 and 39-7,125 sections still say "aid to families with dependent children"**, the program TANF replaced; they are read as applying to TANF.

## Before relying on it

- K.A.R. 30-4-110 to 30-4-113 (income) deposited, so the grant can be computed; any Kansas Register amendment after 2021 checked.
- Whether the 39-7,127 waivers were obtained.
- An independent test pass.
