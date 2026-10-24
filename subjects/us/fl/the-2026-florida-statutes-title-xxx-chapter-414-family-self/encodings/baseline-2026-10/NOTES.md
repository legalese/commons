# The 2026 Florida Statutes, chapter 414: temporary cash assistance — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the applicant, with the design defaults ruled on 2026-10-18.
No REFUSE: a family larger than the chart answers `not covered`, asserted.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

The 2026 Florida Statutes, chapter 414, from Online Sunshine (www.leg.state.fl.us), deposited at `../../registers/source-bundle/fla-stat-ch414.txt` (retrieved 2026-10-19). The Legislature's editorial notes were left out of the deposit; none of the encoded sections carries one that changes its text, so far as the deposit shows.

**Figures.** In the statute: the three-tier payment standard chart (s 414.095(10)), the $2,000 resource limit and $8,500 vehicle exclusion (s 414.075), the $200-plus-half disregard (s 414.095(11)), 48 months (s 414.105), and every deadline. **Input:** 185% of the federal poverty level (s 414.085(1)(a)). The DCF ESS Program Policy Manual, Appendix A-5, deposited in the sibling subject `../../../florida-dcf-ess-program-policy-manual-appendix-a-5-and-a-12-cash-assistance-and-oss-standards/`, prints it "effective April 2026" ($4,212 for a family of 3); the cases use that figure and the question's description names it, but it is not built in (finding 2).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `fl-tca.l4` | `fl-cases-tca.l4` | 37 written, 37 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s end in a breach, each with an `-- expect:` line; both were read and match.

## Seat

**The applicant for temporary cash assistance:** the parent or caretaker relative. Questions: "What are the payment standards for my family?", "How much would we get?", "Do we meet the other conditions?", "How does the 48-month limit apply to me?", "From when does our TCA begin?", "By when must I report my child's absence, and what if I do not?".

The Department of Children and Families appears only as what it must or may do: decide eligibility, deny a request after 30 days without response, grant hardship exemptions.

The 2026-10-18 defaults:

- **The Act alone.** Chapter 414; work requirements (ch. 445) and the Florida Administrative Code (65A-4, not reachable: flrules.org answered HTTP 522) are out.
- **Actors:** the applicant, the parent or caretaker relative, the family, the department.
- **Judgments handed to others, answered conditionally:** good cause for not cooperating on child support (s 414.095(6)); hardship exemptions (s 414.105(1), (2)); a physician's restriction (s 414.095(5)).
- **Definitions:** "gross family income", the disregards, the net income and the amount are worked out from facts. Borrowed: what counts as a resource or as income under the food assistance regulations (7 C.F.R. ss 273.8, 273.9), asked as counted figures; "qualified noncitizen" (s 414.095(3)) as a fact.
- **One case:** one family, one month.
- **Machinery out:** audits, waivers, the Office of Continuing Care, the food assistance sections.

## Scope

**In:** s 414.075(1), (2)(a) (as an input); s 414.085(1)(a) to (c); s 414.095(2)(a), (5), (6), (7), (8), (8)(a), (10), (11), (12)(a), (b), (14)(a), (d) to (h); s 414.105 (opening words, (1), (2), (4), (7), (8), (9)).

**Out:** s 414.065 (work sanctions); s 414.0652 (drug screening); s 414.115 (family cap; Appendix A-5's half-person rows); s 414.095(3) beyond the citizenship question, (4) (caretaker excluded), (14)(b), (c) (teen parents), (14)(i) to (l), (16) (proportional reduction), (17); the diversion programmes; fraud.

## Read with

- `subjects/us/social-security-act/` (Title IV-A): "temporary cash assistance" is cash assistance under the programme certified under Title IV-A (s 414.0252).
- `../../../the-2026-florida-statutes-title-xxx-section-409-212-optional-supplementation/`: the state supplement to SSI. s 414.085(1)(b) excludes SSI from TCA income.
- `../../../florida-constitution-article-vii-finance-and-taxation/encodings/baseline-2026-10/`: Florida levies no personal income tax.

## What the chapter turns out to say

1. **The payment standard is a three-tier chart set in 1996 and still in the statute.** s 414.095(10) gives a standard by family size and shelter obligation (none; over $0 to $50; over $50 or homeless): family of 3, $198, $258 and $303. Appendix A-5 prints the same figures "Eff. Date July 1996". The chart is "for implementation purposes", the standard is "subject to availability of funds", and (16) allows a proportional reduction if funds run short. Asserted.
2. **The income limit moves with the poverty level; the payment standards do not.** s 414.085(1)(a) limits participation to "gross family income ... equal to or less than 185 percent of the federal poverty level". The figure for a year is federal; DCF's Appendix A-5 prints it "effective April 2026", but A-5 is a manual appendix, not a rule, so it is an input here. Asserted at $4,212 (passes) and $4,300 (fails).
3. **The $200-plus-half disregard is for participants, and for applicants who would qualify without it.** s 414.095(11)(a) gives the disregard only to "A current participant" or one "Eligible for participation in the program without the earnings disregard". This encoding reads the second as: income counted without the disregard is below the payment standard. So a new applicant earning $600 gets nothing, while a participant earning the same gets $103. Interpretive. Asserted.
4. **A high-school child's earnings are left out entirely.** s 414.095(11)(b) disregards the earnings of a family member who "attends high school or the equivalent, and is 19 years of age or younger". This encoding leaves them out of the 185% test as well as the amount. Asserted.
5. **All child support counts.** s 414.085(1)(c): "The first $50 of child support ... may not be disregarded", unless federal law requires it. Asserted ($100 support: $203).
6. **No deduction for child care.** s 414.095(12)(b). The only deductions are the two disregards.
7. **The 48-month lifetime limit has standing exemptions and discretionary ones.** Child-only cases, SSI and SSDI recipients and full-time carers of a disabled family member are not subject to it; an SSI or SSDI applicant "must be granted an extension" until the final decision; anyone else past 48 months needs a hardship exemption (capped at 20% of the caseload). Months of TANF in other states count. Asserted.
8. **A child's absence of 30 days or more must be reported within the 5-day period.** s 414.095(14)(h); failure disqualifies the parent for 30, 60 or 90 days on the first, second and third or later occasions. Asserted and traced.
9. **An application lapses after 30 days without response; eligibility starts on approval or on day 30.** s 414.095(8), (8)(a). Asserted and traced.
10. **Pregnancy alone qualifies only at the end.** s 414.095(5) and (14)(a): the ninth month, or the last trimester where a physician restricts work. Asserted.

## Before relying on it

- Deposit Florida Administrative Code ch. 65A-4 if flrules.org becomes reachable.
- Encode the work requirements and sanctions (s 414.065, ch. 445) and the family cap (s 414.115).
- An independent test pass.
