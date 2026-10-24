# Virginia individual income tax (Va. Code ss 58.1-300 to 58.1-339.14) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
No REFUSE: a part-year resident answers `not covered` (asserted).
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding to keep.

## Edition

The Code of Virginia as online after the 2026 Session (Virginia Law Portal "Read all" pages for chapter 3, articles 1, 2 and 3 of Title 58.1), retrieved 2026-10-19 (UTC), deposited at `../../registers/source-bundle/title-58-1-chapter-3-article-{1,2,3}-*.txt`. Unofficial conversion. The Internal Revenue Code is adopted as it existed on 31 December 2025 (s 58.1-301).

**Figures.** Virginia fixes its amounts in the statute: the rate bands, the filing thresholds ($11,950 / $23,900), the standard deduction by taxable year (2019 to 2029, falling back to $3,000 / $6,000 from 2030), the $930 exemption, the $800 aged or blind exemption, the $12,000 age deduction and its thresholds, and the s 58.1-339.8 percentages. Only the HHS poverty guideline (s 58.1-339.8 A) is set each year elsewhere; it is an **input**.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `va-income-tax.l4` | `va-income-tax-cases.l4` | 40 written, 40 satisfied |

Plus five `#TRACE`s of the two regulative rules with `-- expect:` comments (three FULFILLED, two breaches by the taxpayer, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**: a Virginia resident, or a nonresident with Virginia-source income. Questions: "Am I a resident?", "Am I below the filing threshold?", "How much is my age deduction?", "What is my Virginia taxable income?", "How much tax do I owe?", "Which low-income or earned income credit do I get?", and, as rules with deadlines, "I got a bill: by when must I pay?" (s 58.1-308) and "The IRS changed my return: by when must I amend?" (s 58.1-311).

Defaults (2026-10-18):
- **The Act alone**: articles 1-3; no instrument needed except the poverty guideline (input).
- **Actors**: the taxpayer and the Department of Taxation.
- **Judgments left to others**: whether the Department "has sufficient information" to compute the tax (s 58.1-311) is asked as a fact.
- **Definitions**: resident (s 58.1-302), Virginia AGI (s 58.1-321), adjusted federal AGI for the age deduction and the deductions are worked out from facts; federal AGI, federal exemptions allowable, s 63(f) status, s 21 expenses and the federal EIC are borrowed and asked.
- **One case**: one return for one taxable year.
- **Machinery out**: the commissioners of the revenue, the Department's powers, information returns.

## Read with the federal encodings

Federal AGI, the s 32 earned income credit and the other federal terms are inputs; the federal text is in `subjects/us/internal-revenue-code-of-1986/`. Social Security benefits (Title II, taxable under IRC s 86) are subtracted in full (s 58.1-322.02(3)); `subjects/us/social-security-act/` holds Title II. Cross-folder IMPORT is not possible; the links are recorded here.

## Scope

**In:** s 58.1-302 ("resident"); s 58.1-308 (regulative: pay within 30 days); s 58.1-311 (regulative: amend within one year); s 58.1-320 (bands from 1990); s 58.1-321 A; s 58.1-322; ss 58.1-322.01, 58.1-322.02 (Social Security apart, as totals); s 58.1-322.03(1), (2), (3), (5) (the rest as one total); s 58.1-325 A; s 58.1-339.8.

**Out:** s 58.1-303 (part-year residents: `not covered`); estates and trusts; s 58.1-321 B, C; s 58.1-322.04; s 58.1-324 (allocation between spouses); s 58.1-326; s 58.1-332 and the other article 3 credits; s 58.1-317 (estimated tax); article 4 (returns, due dates, not deposited).

## What the Code turns out to say

1. **Virginia's rate bands have not moved since 1990.** Section 58.1-320 still lists the bands for 1987, 1988 and 1989 alongside the band "for taxable years beginning on and after January 1, 1990": 2% to $3,000, 3% to $5,000, 5% to $17,000, 5.75% above. The tax at $17,000 is $720. Asserted.
2. **The filing threshold adds the age deduction back.** Section 58.1-321 A compares "the Virginia adjusted gross income plus the modification specified in subdivision 5 of s 58.1-322.03" with $11,950 (single) or $23,900 (married; half for separate returns). So a single person over 65 with $11,000 of income must still file, though they owe nothing, while a younger person with the same income need not. Asserted. Where the threshold applies, "no tax ... is imposed" even though taxable income may be positive (single, $11,000: taxable $1,320, tax nil). Asserted.
3. **The age deduction on a joint return.** Each qualifying individual has a $12,000 deduction, "reduced by $ 1 for every $ 1 that the taxpayer's adjusted federal adjusted gross income exceeds ... $ 75,000 for married taxpayers". The text does not say whether a couple who both qualify lose $1 or $2 for each dollar over. This encoding reduces the combined deduction once (both 65, $85,000: $14,000). An interpretive choice, asserted; the Department's instructions should be checked.
4. **The standard deduction is written year by year, and drops back in 2030.** $8,750 / $17,500 for 2025 and 2026, $9,200 / $18,400 for 2027, $9,300 / $18,600 for 2028 and 2029, and "for taxable years beginning before January 1, 2019, and on and after January 1, 2030, $ 3,000 ... and $ 6,000". Asserted (2026, 2027, 2030). A dependant may compute it "only with respect to earned income". Asserted.
5. **The low-income credit and the earned income credit are alternatives, and the refundable one has a sunset.** Section 58.1-339.8 gives three credits "in lieu of" one another: $300 per person below the poverty guideline (B 1, nonrefundable), 20% of the federal EIC (B 2, nonrefundable), and a refundable 15% (2022-2024) or 20% (2025-2026) of the federal EIC (B 3). From 2027 only B 1 and B 2 remain. B 3 b, unlike B 2 and B 3 a, does not repeat "eligible for a tax credit pursuant to s 32", but its amount is a share of the s 32 credit claimed, so it comes to the same. The B 1 "household" is read as the persons for whom $300 is given; the poverty guideline is for a household "of an equal number of persons". For a nonresident or part-year resident B 3 is capped at the tax (s 58.1-339.8 C), so it is not refundable for them. Claiming the age deduction, the $800 aged or blind exemption or the National Guard subtraction bars all three (D). Asserted.
6. **The two duties with deadlines.** A deficiency bill must be paid "within thirty days after the amount of the tax as computed is mailed" (s 58.1-308); a federal change must be reported on an amended return "within one year after the final determination date", unless the Department already has the information and the tax is paid (s 58.1-311). One year is taken as 365 days. Traced.
7. **The deposited text has no general filing duty or due date.** Section 58.1-321 A says who need not file; the return and due-date sections (s 58.1-341 and following, article 4) were not deposited, so "by when must I file?" is not answered here.

## Before relying on it

- Deposit article 4 (returns and due dates) and s 58.1-303 and encode part-year residence.
- Check finding 3 against the Department's instructions.
- An independent test pass.
