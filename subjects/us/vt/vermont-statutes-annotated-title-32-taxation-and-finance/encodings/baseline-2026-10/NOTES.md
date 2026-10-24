# Vermont personal income tax (32 V.S.A. ch. 151) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
No REFUSE: the one case outside the encoding (a part-year resident or nonresident whose Vermont income is zero or negative) answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding of this chapter to keep.

## Edition

Vermont Statutes Online (Office of Legislative Counsel), **unofficial**, "now include the actions of the 2026 session", fetched 2026-10-19 (UTC), deposited at `../../registers/source-bundle/vt-32-vsa-ch151-2026.txt` (sha256 of the text `3f33f4f4…478968`).
Federal income tax laws are adopted as in effect on 31 December 2025 (s 5824).

**Figures set each year.** The personal exemption, the standard deductions, the additional deduction and the rate-table ceilings are adjusted annually by the Commissioner of Taxes (s 5811(21)(D), s 5822(b)(2)). No Commissioner's publication was deposited, so they are **inputs**; each `@desc` names the figure the statute prints. All cases use the printed figures, so their tax amounts are not the tax for any real year.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vt-income-tax.l4` | `vt-income-tax-cases.l4` | 56 written, 56 satisfied |

Plus four `#TRACE`s of the filing-and-payment rule, each with an `-- expect:` comment (two FULFILLED, two breaches; the breach reasons were read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**: a Vermont resident, part-year resident or nonresident individual, filing alone or jointly. Questions: "Must I file?", "Must we file jointly?", "How much of my Social Security does Vermont exclude?", "What is my Vermont taxable income?", "How much do I owe?", "How much are my earned income, child and child-care credits?".
Provisions addressed to the Commissioner (inflation adjustment) are encoded as what they mean for the person: a published figure the person states.

Defaults (2026-10-18):
- **The Act alone**: chapter 151; the Commissioner's annual figures would be brought in if deposited (they are not: inputs).
- **Actors the text names**: the taxpayer and the Commissioner of Taxes.
- **Judgments left to others**: "unless the Commissioner allows a different filing status" (s 5861(c)) is asked as a fact.
- **Definitions**: Vermont taxable income (s 5811(21)), the Social Security exclusion (s 5830e(a)), the personal exemption count (s 5811(21)(C)(i)) and the residency share are worked out from facts. Borrowed federal terms — federal AGI, filing status, dependants under 26 U.S.C. s 152, the federal EITC, CTC and child and dependent care credit, s 63(f) deductions, the s 213 medical deduction, s 170 contributions — are asked as facts.
- **One case**: one taxpayer (or one joint return) for one taxable year.
- **Machinery out**: purposes, the Commissioner's powers, corporate tax, withholding and estimated tax.

## Read with the federal encodings

Vermont starts from federal AGI and borrows federal credits. The federal text is in `subjects/us/internal-revenue-code-of-1986/` (ss 1, 24, 32, 63, 86, 152, 21 are deposited there; its encoding is being written in parallel). Cross-folder IMPORT is not possible in the stable `l4`, so the link is recorded here only.

## Scope

**In:** s 5861(a), (b), (c); s 5871(3); s 5811(21) (with (A) and (B) other than the Social Security exclusion asked as two totals; (C)(i)-(iv)(I)); s 5830e(a); s 5822(a)(1)-(4), (6), (b), (d)(3), (e); s 5828b; s 5828c; s 5830f(a), (b).

**Out:** estates and trusts (s 5822(a)(5), s 5811(28)); s 5830e(b)-(e) (other retirement income, military retirement, the one-exclusion election: Social Security is taken as the elected exclusion); s 5811(21)(C)(iv)(II) (continuing care retirement community fees, taken as nil); s 5822(c), (d)(1)-(2); ss 5825-5828, 5830b-5830d, 5830g credits; s 5830f(c) (the benefits disregard: stated in finding 7, not computed) and (d) (advance payments, effective only on a contingency); subchapters 4 and 5 (withholding, estimated tax); s 5823 (Vermont income is asked as a fact).

## What the chapter turns out to say

1. **The duty to file has a stand-alone limb.** Section 5861(a) requires a return where the person must file federally and has more than $100 of Vermont income or more than $1,000 of s 5823(b)(1)-(6) gross income, "or has a tax liability under this chapter". The last limb is read as standing alone, so a person not required to file federally who still owes Vermont tax must file. Asserted. Exactly $100 or $1,000 is not "more than": asserted.
2. **The printed fixed amounts in s 5822(a) are the tax on each ceiling at the lower rates, rounded to the nearest dollar.** All twelve printed amounts for the four individual tables check (for example joint: 2,164.10 → $2,164; 8,206.40 → $8,206; 14,423.20 → $14,423; head of household 1,736.975 → $1,737). The statute does not say how the fixed amounts move when the Commissioner adjusts the ceilings; this encoding works them out the same way. Asserted for the printed figures; an interpretive choice for adjusted ones.
3. **The proviso on personal exemptions is read per person.** "No exemption may be claimed for an individual who is a dependent of another taxpayer" removes the taxpayer's own exemption (and the spouse's) where that person is someone else's dependant. Asserted (a student with AGI $8,000: taxable $2,000, tax $67).
4. **The Vermont medical deduction can only help.** Section 5811(21)(C)(iv) allows "an amount equal to the itemized deduction for medical expenses ... minus" the Vermont standard deduction and exemptions. Where the remainder is negative the encoding deducts nothing; the text does not say so, but a negative "deduction" would add income. Asserted ($15,000 federal medical deduction for a single filer adds $4,850; $5,000 adds nothing).
5. **The child tax credit phase-out uses "the individual's adjusted gross income"** (s 5830f(b)) with no "federal" and no reference to the s 5811(21) modifications, while s 5822(e) defines "adjusted gross income" for its own purposes only. This encoding reads s 5830f(b) as federal AGI. "Or fraction thereof" is a ceiling: $130,500 is 6 steps of $20. Asserted.
6. **The 3 percent minimum tax (s 5822(a)(6)) looks at federal AGI, not Vermont taxable income.** A taxpayer with large Vermont subtractions (for example the capital gain exclusion) and federal AGI over $150,000 pays at least 3 percent of federal AGI before the s 5822(e) reduction. AGI of exactly $150,000 does not "exceed". Asserted.
7. **The Vermont child tax credit is not income for benefits.** Section 5830f(c) says the credit "shall not be considered as assets, income, or resources" for State or local programs including Reach Up (33 V.S.A. ch. 11), to the extent federal law allows. That is the link from this encoding to the Reach Up baseline (`subjects/us/vt/vermont-statutes-annotated-title-33-human-services-chapter-11/encodings/baseline-2026-10/`), which takes countable income as an input. Not computed.
8. **The credits for part-year residents use a different fraction from the tax.** The tax reduction in s 5822(e) uses Vermont income over modified AGI; the credits (ss 5828b, 5828c, 5830f) use income "earned or received during the period of the individual's residency" over total income. The two are asked separately. A nonresident all year gets none of the three credits, which are for a "resident individual or part-year resident individual". Asserted.
9. **Section 5828b's text says 38 percent "for an individual who claims one or more qualifying children" and 100 percent for one who does not.** Asserted ($4,000 federal → $1,520; $600 federal, no children → $600).
10. **The subject's `subject.json` still names only subchapter 4** (withholding), as indexed on 2026-09-23, although the whole chapter is deposited (README 2026-10-20). Left unchanged.

## Before relying on it

- Compare the text with the official Vermont Statutes Annotated.
- Deposit the Commissioner's inflation-adjusted figures for the year (exemption, standard deductions, additional deduction, bracket ceilings) and test with them.
- Encode s 5823 (Vermont income), the s 5811(21)(A)-(B) items one by one, s 5830e(b)-(e), and the remaining credits.
- An independent test pass.
