# General Statutes of Connecticut, chapter 319s: temporary family assistance — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the applicant, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

The General Statutes of Connecticut revised to January 1, 2025, chapter 319s, at `../../registers/source-bundle/cgs-chap-319s-rev2025.txt`, read with the 2026 Supplement (revised to January 1, 2026) at `../../registers/source-bundle/cgs-chap-319s-sup2026.txt`. Encoded from the Supplement: ss 17b-80, 17b-104, 17b-112. From the 2025 revision: ss 17b-75, 17b-85. Both retrieved 2026-10-19 from cga.ct.gov.

**Figures.** Every TFA figure is in the statute, as a percentage or a dollar amount: standard of need 55% of the federal poverty level (s 17b-104(a)), payment standard 73% of that (s 17b-104(c)), 8% attributed for subsidized housing (s 17b-104(d)), the 100%, 171% and 230% earnings points (s 17b-112(d)), the $6,000 asset limit, the $50 child-support and $90 extension disregards. **The federal poverty level itself is an input**: a federal figure, published each year by HHS and not in commons. The cases use a HYPOTHETICAL $2,000 a month.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ct-tfa.l4` | `ct-cases-tfa.l4` | 47 written, 47 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s end in a breach, each with an `-- expect:` line; both were read and match. Expected values were worked by hand from the text.

## Seat

**The applicant: the parent or other caretaker relative who applies for the family.** Questions: "Is this child a dependent child?", "Is my family eligible this month?", "Must the Commissioner give us an extension?", "What are the standard of need and the payment standard for my family?", "Roughly how much would we get?", "By when must the Department act on my application, and may I ask for a hearing if it has not?", "By when must I report new income or a change?", "May I have a hearing on a decision?".

The Commissioner of Social Services appears only as what the Commissioner must do for or to the family: act on the application within 45 or 60 days (s 17b-80(a)), reinvestigate at least every twelve months (s 17b-104(a)), grant an extension (s 17b-112(c)), provide a hearing (s 17b-112(h)).

The 2026-10-18 defaults:

- **The Act alone.** Chapter 319s only. The Uniform Policy Manual, which holds the benefit computation, is not deposited.
- **Actors:** the applicant or beneficiary, the family, the Commissioner of Social Services.
- **Judgments handed to others, answered conditionally:** whether a s 17b-112(b) exemption applies (the list is open, and several limbs are the Commissioner's call: "incapacitated or of an advanced age, as defined by the commissioner"); good cause for late reporting (s 17b-85, in the breach message); "good faith effort" (s 17b-112(c)); a relative "approved by the commissioner" (s 17b-75).
- **Definitions** worked out from facts: "dependent child" (s 17b-75); the counted gross earnings (s 17b-112(d), with s 17b-80(b)). Borrowed and asked: the federal poverty level; domestic violence (s 17b-112(c) refers to P.L. 104-193 s 402(a)(7)(B)).
- **One case:** one family and one month for the tests; one application, or one change, for the deadlines.
- **Machinery out:** pilot programmes, reports, the TANF Emergency Fund sections, the two-generational initiative.

## Scope

**In:** s 17b-75 ("dependent child"); s 17b-80(a) (investigation within 45 or 60 days, and a hearing if not acted on), (b) (students' earnings); s 17b-85 (report within 10 days); s 17b-104(a) (standard of need; reinvestigation every 12 months), (c), (d); s 17b-112(a) (36 months), (b) (exemptions, as a fact), (c) (extensions; 60-month limit), (d)(1) (earnings test, earned-income disregard, $6,000 assets, $50 child support), (d)(2) (six-month disregard to 230%, 20% reduction), (e) (child-support cooperation), (h) (hearing).

**Out:** s 17b-112(d)(3), (4) (pilot cash transfers and job-training stipends; they would reduce counted income); (f) (exit interview); (g) (cost-of-living adjustment, finding 4); s 17b-112c (non-citizens); ss 17b-112a, 17b-112b; s 17b-112g (diversion); the state supplement to SSI (s 17b-104 first sentence, s 17b-106, s 17b-80(c)); SAGA (its own subject, `../../../regulations-of-connecticut-state-agencies-17b-198-state-administered-general-assistance/`); SNAP (federal: `subjects/us/food-and-nutrition-act-of-2008`).

## Read with

- `subjects/us/social-security-act/` (Title IV-A, TANF; Title IV-D, child support): s 17b-112(a) runs TFA "in accordance with the temporary assistance for needy families program", and (e) requires cooperation under Title IV-D. The Title IV-A text is not deposited there.
- `../../../general-statutes-of-connecticut-title-12-taxation-chapter-229/encodings/baseline-2026-10/`: s 12-704e(d) says a state or federal earned income tax credit is not counted as income or resources for need-based programmes, so it does not belong in `other countable unearned income` here. s 17b-104(a) likewise disregards tax refunds to the extent 26 USC 6409 does.

## What the chapter turns out to say

1. **The payment standard is fixed in the statute as a share of the poverty level: 73% of 55%, or 40.15%.** No dollar table is needed, and the old Uniform Policy Manual "Standards of Need" by region (UPM 4510.15) is superseded for TFA. With a monthly poverty level of $2,000, the standard of need is $1,100 and the payment standard $803. Asserted.
2. **The statute does not say how income is netted against the payment standard.** s 17b-80(a) gives aid "in such amount, determined in accordance with levels of payments established by the commissioner, as is needed". This encoding reads the amount as the payment standard, less the subsidized-housing attribution, less counted unearned income, less earnings above the disregard, then the 20% reduction. That reading is the encoding's; the Department's computation is in the Uniform Policy Manual, not deposited. The exported question says "on this encoding's reading". Asserted ($300 unearned: $503).
3. **The six-month disregard is stated "for purposes of eligibility", but its 20% reduction can only bite if the earnings are disregarded in the amount too.** Under (d)(1), earned income is disregarded in the amount only "up to the federal poverty level". If that applied in a (d)(2) month, earnings of 171% to 230% would wipe out the benefit, and the 20% reduction "for the months in which earnings are between one hundred seventy-one per cent and two hundred thirty per cent" would never apply. So this encoding disregards earnings up to 230% in the amount as well in those months, and reads "between" as including 171% and 230%. Interpretive. Asserted ($3,600, 180%: $642.40; $3,420, 171%: $642.40).
4. **The cost-of-living adjustment cannot be computed from the text.** s 17b-112(g) gives a COLA "whenever funds appropriated for temporary family assistance lapse at the close of any fiscal year and such adjustment has not otherwise been included in the budget", and a prorated increase when the lapsed funds are not enough. Whether that happened in a year is a budget fact. So the payment standard here is the s 17b-104(c) figure, and the one paid may be higher.
5. **The two extensions need a good-faith effort plus either low income or circumstances preventing employment.** The sentence could be read with the good-faith effort attached only to the income limb; this encoding attaches it to both. The $90 disregard is of earned income, so it lowers only earned income. A third or later extension is a "may". Asserted ($2,050 earned: shall grant; $2,050 unearned: not required).
6. **The 36-month limit gives way to a (b) exemption; the 60-month limit gives way only to domestic violence.** Each extension adds six months to the 36. The 60-month count leaves out months during the COVID-19 emergency and includes months of TANF from other states (the input says so). Asserted.
7. **The asset test is "shall not deny ... unless such assets exceed six thousand dollars".** $6,000 passes; $6,001 fails. Asserted.
8. **Gross earnings "exceeding the federal poverty level" fail the test, but a student child's earnings do not count** (s 17b-80(b), 2026 Supplement: "any earned income of a child who is a student"). Asserted ($2,500, of which $600 a student's: passes).
9. **The Department has 45 days to act, or 60 where disability must be determined, and the remedy is a hearing.** s 17b-80(a). The hearing may be asked for from the 46th (or 61st) day after receipt. Asserted, and the rule traced.
10. **The reporting duty has two triggers and one deadline.** s 17b-85: ten days after receiving or learning of property, wages, income or resources, and ten days after a change in the information on the application. Good cause excuses, "as determined by the commissioner". Asserted, and the rule traced.

## Before relying on it

- Deposit the Uniform Policy Manual's TFA computation and replace the reading in finding 2.
- Source the current TFA payment standards notice (finding 4) and the HHS poverty guidelines.
- Encode s 17b-112c (non-citizens) and the domestic-violence standards.
- An independent test pass.
