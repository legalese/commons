# Iowa Code chapter 239B (family investment program) with IAC 441-41.27 and 41.28 — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ia-fip.l4`) states the rules in the chapter's and the rules' own terms (child, family, specified relative, eligible group, payment standard, standard of need, the department), with three regulative rules: the department's 30-day decision (239B.3(1)(b)), the participant's 10-day answer to a JOBS reminder letter (239B.9(3)(a)), and the duty to cooperate with child support (239B.2(6)).
A **seat layer** (`ia-fip-seat.l4`) asks the applicant's questions, each with `@export` and a `@desc` on every input, built only from the core.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

- **Iowa Code 2026** (Legislative Services Agency; laws through the 2025 regular session), chapter 239B, deposited at `../../registers/source-bundle/ia-code-ch-239B-2026.txt` (retrieved 2026-10-19). 2026 session Acts not applied.
- **The instrument that sets the numbers:** the Iowa Administrative Code, publication of 10/14/2026 (official edition), rules 441-40.21, 41.27 and 41.28, deposited in the sibling subject `../../../iowa-administrative-code-441-chapters-40-41-family-investment-program-need-standards/registers/source-bundle/ia-iac-441-40-21-41-27-41-28-fip.txt` (retrieved 2026-10-19). The Schedule of Needs (41.28(2)) is copied into the core from that deposit's table, row by row.

The payment standard is therefore **deposited**, not an input. Special needs (41.28(3)) are an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ia-fip.l4` (core), `ia-fip-seat.l4` (applicant seat) | `ia-fip-cases.l4` | 47 written, 47 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Expected values worked by hand from the texts before the run.
Regulative rules: 3. Each is asserted FULFILLED where it is kept; the two with deadlines are `#TRACE`d to a breach with an `-- expect:` line.

## Seat

**The applicant**: the parent or other specified relative applying for FIP for a child, and the participant family once it receives it. "Is my grandchild a child for FIP? Can I apply? Are our savings under the limit? Does our income pass? How much would we get each month? When must the department decide? I got a JOBS reminder letter: by when must I answer? May I reconsider my limited benefit plan?"
The department's duties (to decide within 30 days, to pay toward a child's funeral) are encoded as what they mean for the applicant: a date, and the most that may be paid.

Defaults (2026-10-18):
- **The Act and the instrument that sets its numbers:** chapter 239B and IAC 441-40.21, 41.27, 41.28.
- **Actors the text names:** the applicant or participant, the specified relative, the department.
- **Judgments left to others:** good cause for not cooperating with child support, the department's allowance of special needs, exemption from the written statement, are inputs.
- **Definitions:** child (239B.1(3)), family (239B.1(6)), specified relative (239B.1(13)), the resource limitation and disregards (239B.7(6)-(8)), countable gross and net income (IAC 41.27) worked out from facts. "Earned" and "unearned" income are asked as facts, with the rules' examples in the `@desc`.
- **One case:** one family's application, in one month.
- **Machinery out:** PROMISE JOBS administration, the department's role, fraud recovery, child care assistance.

## Scope

**In:** 239B.1(3), (6), (13); 239B.2(1), (2), (4), (5), (6); 239B.2C (in the eligible-group `@desc`); 239B.3(1)(b), (2), (4); 239B.7(1), (2), (6), (7), (8); 239B.9(1)(b)(1)-(2), (3)(a), (4); IAC 441-40.21 (payment standard, standard of need); 441-41.27 (the three-step initial and two-step continuing tests, the grant, the 20% deduction and 58% disregard); 441-41.28(2) (the Schedule of Needs).

**Out:** 239B.2B (noncitizens; borrowed immigration statuses), 239B.2(3) (unemployed parent), 239B.8 (the content of family investment agreements), 239B.9(2) (to whom a limited benefit plan applies), 239B.10 (minor parents), 239B.11 (diversion), the FIP time limit (IAC 441-41.30, not deposited), the detailed exempt-income list in 41.27(7), stepparent and self-supporting parent deeming (41.27(8)), prorating and lump sums (41.27(9)), special needs amounts (41.28(3)).

## What the texts turn out to say

1. **The statute sets the deductions; the rules set the money.** Chapter 239B fixes the 20% work expense deduction, the 58% work-and-earn incentive and the $2,000 / $5,000 resource limits (239B.7), but every dollar of need comes from IAC 441-41.28(2). The payment standard for a parent and two children is $426 a month. Asserted.
2. **Three tests on application, two after.** On application the family's gross income must be within 185% of the standard of need, its net income before the 58% disregard must be less than the standard of need, and its net income after the disregard must be less than the payment standard (IAC 41.27, paragraph 1). A family already receiving FIP skips the middle test (paragraph 2), so a family earning $1,100 is refused on application but stays eligible once it receives FIP. Asserted.
3. **The 185% figures are the schedule's**, from the schedule of living costs alone; the rules do not add special needs to them. The encoding uses the printed figures.
4. **"Within available funding"** opens both 239B.2 and 239B.3(1)(a): the department's duty to pay is subject to appropriation. The encoding computes the grant the rules give and does not model a shortfall.
5. **Not answering a JOBS reminder letter in ten calendar days is treated as choosing a limited benefit plan** (239B.9(3)(a)). It is encoded as the participant's obligation with the plan as its LEST consequence, because the person's question is "by when must I answer?". A first limited benefit plan lasts until the participant makes significant contact with the JOBS program; it can be reconsidered "at any time following the effective date", read here as from the effective date itself. A subsequent one only after the specified period (up to six months). Asserted.
6. **The funeral payment is a power, not a duty** ("may pay ... a maximum of four hundred dollars", from appropriated funds). The question asks the most the department may pay. Asserted.
7. **No rounding** of the grant is stated in the deposited rules; none is applied (case D gives $175.80).

## Before relying on it

- An independent test pass; a check of the cases against a department notice of decision.
- The FIP time limit (IAC 441-41.30), the exempt income list (41.27(7)), deeming (41.27(8)) and special needs (41.28(3)) deposited and encoded.
- The 2026 session Acts and later IAC publications applied: the Schedule of Needs changes by rule.
