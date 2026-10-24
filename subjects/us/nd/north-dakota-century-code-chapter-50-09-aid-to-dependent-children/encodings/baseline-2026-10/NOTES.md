# North Dakota Century Code chapter 50-09 (TANF), with N.D. Admin. Code chapter 75-02-01.2 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. What is outside the encoding is listed below and is not reachable from the questions.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the statute's and the rules' own terms in `nd-tanf.l4`. The applicant's questions are in `nd-tanf-seat.l4`, which IMPORTs the core and calls its rules. Each question has `@export` and every input a `@desc`. There was no earlier encoding of either text to keep.

## Edition

- **N.D.C.C. ch. 50-09**, the Legislative Council's 07/01/25 update (2025 session), deposited on 2026-10-20 at `../../registers/source-bundle/ndcc-t50c09.txt`.
- **N.D. Admin. Code ch. 75-02-01.2**, sections -01, -22, -42, -43, -47, -48, -50 and -51 (the chapter is amended as late as 1 April 2026). It was deposited on 2026-10-20 in the sibling subject `../../../north-dakota-administrative-code-chapter-75-02-01-2-tanf-income-and-standards/registers/source-bundle/nd-admin-code-75-02-01-2-tanf-income-and-standards.txt`, and its terms are in that subject's `SOURCE-LICENSE.md` (same register, same verdict: clean).

The rules are brought in under the default "the Act, plus the instruments that set its numbers". Chapter 75-02-01.2 is made under ch. 50-09 ("General Authority: NDCC 50-09-02, 50-09-25"). The encoding sits under the Act, because the stable `l4` cannot import across subject folders and a second encoding under the rules' subject would only repeat it.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nd-tanf.l4`, `nd-tanf-seat.l4` | `nd-tanf-cases.l4` | 37 written, 37 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. One `#TRACE` shows a breach (a payment issued in a month in which none may be), with its expected result in an `-- expect:` comment. Every expected value was worked by hand from the text.

## Seat

**The applicant**: a parent or caretaker relative applying for the household, or a pregnant woman. "Can we get TANF? Are our savings too high? How much of my pay counts? How much will we get a month? Is there a time limit?"

Provisions addressed to the state agency or the human service zone are encoded as what they mean for that person:
- the hardship exemption and the absence exception, which the agency determines, are asked as facts;
- the agency must not issue a payment under $10 or beyond sixty months;
- the agency must afford a fair hearing on appeal.

The 2026-10-18 defaults:

- **The Act and the instruments that set its numbers:** ch. 50-09 with ch. 75-02-01.2. The department's standard of need, income incentive limit, personal needs allowance and special items are not in either text, so they are inputs.
- **The actors the texts name:** the applicant or recipient, the state agency (the department of health and human services), the human service zone.
- **Judgments left to others, answered conditionally:** hardship (s 50-09-29(1)(c), s 50-09-31(1)(d)), the absence exception ((1)(s)), "reasonable costs" of liquidation (-22).
- **Definitions worked out from facts:** net earned income, countable earned income, adjusted net income, the asset limit. Borrowed terms (a disability, domestic violence as defined in s 14-07.1-01) are asked as facts.
- **One case:** one household, one benefit month.
- **The texts' own terms**, quoted in the comments.
- **Machinery out:** the state plans, data systems, funds and reimbursement (ss 50-09-02 to 02.7, 16-22), and child support enforcement.

## Regulative rules

Two, in `nd-tanf.l4`:

1. `no payment for the month` (N.D.A.C. 75-02-01.2-43; N.D.C.C. s 50-09-29(1)(b)): where the calculated benefit is under $10, or the household is past sixty months without an exemption, the state agency SHANT issue a benefit payment WITHIN the month, LEST BREACH.
2. `my fair hearing on appeal` (s 50-09-14(1)): on an appeal, the state agency MUST afford reasonable notice and an opportunity for a fair hearing. No time is set in the chapter.

## Scope

**In:** N.D.C.C. s 50-09-06.1 (assignment of support), s 50-09-14(1), s 50-09-29(1)(a)-(c), (f), (g), (m), (s), (v); N.D.A.C. 75-02-01.2-22, -42, -43, -47, -48, -50(6), (7), -51(2)(a)-(c), (g), (h), (3).

**Out:** the work requirements, the individual employment plan and sanctions (s 50-09-29(1)(h), (q), (r), (t)); noncitizens ((1)(e), (j)); the department's choice to disregard more than the minimum percentages (-51(2)(c)); self-employment income (-50(3)); lump sums and contract income (-50(4), (5)) except as inputs; stepparent and minor parent budgeting (-51(4)); the domestic violence screening duties (s 50-09-31) except as the hardship input; child support enforcement.

Read with the federal Social Security Act encoding (`subjects/us/social-security-act/`, Title IV-A, being encoded on 2026-10-24). Section 50-09-29(1)(b) carries out 42 U.S.C. 608(a)(7). Cross-folder IMPORT is not possible in the stable `l4`.

## What the texts turn out to say

1. **The Act sets almost no amounts.** Chapter 50-09 tells the state agency to limit benefits to sixty months, to exempt hardship cases, to limit assets "of a value established by the state agency" and to "Exclude one motor vehicle of any value" (s 50-09-29(1)(b), (c), (f), (g)). Every figure is in the rules. Asserted (time limit, vehicle exclusion through the asset question).
2. **The amount actually paid depends on a figure in neither text.** The rules match income against "the standard of need" (-47, -48), but chapter 75-02-01.2 does not print it. The standard of need, the "income incentive limit" (-51(1), (2)(b)) and the personal needs allowance are the department's, and are inputs. The cases use hypothetical figures ($600 and $1,000).
3. **The asset limit is generous and counts the household, not the children.** It is $9,000 for one person, $15,000 for two and $500 more for each additional person (-22), with one vehicle of any value excluded. Asserted.
4. **The earned income incentive is a floor, not a fixed rate.** Rule -51(2)(c) says "at least fifty percent" may be disregarded in months one to six, "at least thirty-five percent" in months seven to nine and "at least twenty-five percent" in months ten to twelve, and none after (also s 50-09-29(1)(v): "no more than twelve months"). The department may disregard more; the encoding applies the minimums. Net earned income above the income incentive limit always counts in full ((2)(b)). Asserted.
5. **The standard employment expense allowance is the greater of $180 or 27% of gross earnings** (-50(7)), so it takes all of a small wage below $180. Asserted.
6. **Income equal to the standard of need is too much.** Rule -47(2) says a household is "ineligible" where income "equals or exceeds" the standard of need. Rule -48's net income test is passed only where adjusted net income is "less than" the need plus allowances. A calculated benefit under $10 is not issued, but the household is still treated as one that is paid (-43). That keeps the earned income incentive clock running (-51(3)(a)). Asserted.
7. **Section 50-09-06.1(5) refers to a benefit cap that is no longer there.** The assignment of support "Is not effective as to any child subject to a benefit cap imposed under section 50-09-29", but s 50-09-29 as deposited imposes no benefit cap (unverified (general knowledge): North Dakota's former family cap provision appears to have been repealed). Not asserted.
8. **The application assigns the support rights.** Under s 50-09-06.1 the application itself "is deemed to create and effect an assignment" of all support rights to the state agency, up to the total cost of benefits. Asserted.

## What would need doing before this is worth relying on

- **The standard of need, the income incentive limit and the personal needs allowance**, from a deposited department publication (the TANF policy manual, service chapter 400-19: unverified (general knowledge)), so they need not be inputs.
- **The work requirements and sanctions**, and the application and decision timelines (not in the deposited sections).
- **The rest of chapter 75-02-01.2**: household composition, unearned income, deeming.
- **An independent test pass.**
