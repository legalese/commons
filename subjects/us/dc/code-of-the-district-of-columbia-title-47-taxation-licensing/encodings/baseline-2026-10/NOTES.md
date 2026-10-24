# D.C. Code Title 47, chapter 18 (individual income tax): the resident — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the resident taxpayer, with the design defaults ruled on 2026-10-18.
No REFUSE: nonresidents, part-year residents, years before 2022 and the child tax credit after 2025 answer `not covered`, asserted.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this title to keep.

## Edition

The Code of the District of Columbia "through 2026-09-26" (last codified D.C. Law 26-187), from the Council's bulk XML (github.com/DCCouncil/law-xml-codified, branch `publication/2026-05-23`, commit `9c950ac5`), deposited at `../../registers/source-bundle/dc-code-47-ch18-subch-i-vi-individual-income-tax-2026-10.txt` and `../../registers/source-bundle/dc-code-47-ch18-subch-xii-xvi-assessment-collection-2026-10.txt` (retrieved 2026-10-19). The deposit was made from the Council's bulk download, as its site asks, with the owner's approval of 2026-10-20; it is for public reference and encoding, not model training (the site's robots.txt signals `ai-train=no`).

**Figures.** The rate table, the exemption phase-out, the EITC percentages, the childless EITC phaseout percentage and base, and the 2025 child tax credit and thresholds are in the statute. The federal figures the Code borrows (the IRC s 63(c) standard deduction, the s 151 exemption amount, the s 32 childless percentage and earned income amount) and the cost-of-living adjusted DC figures for later years (the childless phaseout amount; the child tax credit from 2026) are inputs or `not covered`. The cases use HYPOTHETICAL federal figures.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `dc-income-tax.l4` | `dc-cases-income-tax.l4` | 52 written, 52 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s end in a breach, each with an `-- expect:` line; both were read and match.

## Seat

**The individual taxpayer resident in the District.** Questions: "Am I a DC resident?", "Must I file?", "What is the tax on my taxable income?", "How much DC EITC do I get, with or without a qualifying child?", "Will it be paid monthly?", "How much child tax credit?", "How much do I owe?", "By when must I file and pay?", "How long an extension can I get?", "By when must I pay an assessed deficiency?".

The Chief Financial Officer and the Mayor appear only as what they may do (grant an extension, assess a deficiency); the Superior Court as where an appeal goes.

The 2026-10-18 defaults:

- **The Act alone.** Title 47 chapter 18, subchapters I to VI and XII to XVI as deposited.
- **Actors:** the taxpayer, the person aggrieved by an assessment, the Chief Financial Officer, the Mayor, the Superior Court.
- **Judgments handed to others:** the extension ("whenever in his judgment good cause exists") is answered as its maximum length only.
- **Definitions** worked out from facts: "resident" (s 47-1801.04(42)); the exemption phase-out (s 47-1806.02(h-1)); the child tax credit reduction. Borrowed and asked: domicile; whether a federal return is required (IRC s 6012); the federal standard deduction and exemption amount; the federal EIC; "qualifying child".
- **Departures:** DC adjusted gross income (s 47-1803.02) is asked as an input, as is the number of exemptions (s 47-1806.02(b) to (f)).
- **One case:** one return for one calendar year.
- **Machinery out:** the check-offs, the reports, regulations, the business taxes.

## Read with the federal encodings

`subjects/us/internal-revenue-code-of-1986/` (a baseline being written on 2026-10-24 by another session): IRC ss 2, 24(c), 32, 63(c), 151, 6012. DC gross income has "the same meaning as defined in § 61" (s 47-1803.02(a)), so IRC s 61 is the start of DC AGI. The stable `l4` cannot IMPORT across subject folders; the link is recorded here.

## Scope

**In:** s 47-1801.04(42); s 47-1801.04(44)(iv) (as an input); s 47-1805.02(1) (residents); s 47-1805.03(a)(2), (b); s 47-1806.01; s 47-1806.02(h), (h-1), (i)(2); s 47-1806.03(a)(11), (c), (e); s 47-1806.04(f)(1)(B-1) to (B-3), (C), (f)(3)(A), (B)(ii-a), (C); s 47-1806.17(a) to (d), (e)(5)(A); s 47-1812.07(a)(1) to (3); s 47-1815.01.

**Out:** nonresidents and part-year residents (`not covered`); years before 2022 (`not covered`); s 47-1803.02 (DC AGI, an input); the exemption count; itemized deductions; s 47-1806.04(a) to (e) and (g), and the other credits (Schedule H, s 47-1806.06; the keep child care affordable credit; and the rest); the child tax credit after 2025 (`not covered`); withholding and estimated tax; penalties and interest (subchapter XIII is repealed and its successor provisions are not deposited).

## What the Code turns out to say

1. **One rate table for every filing status.** s 47-1806.03(a)(11) imposes one table "on the taxable income of every resident"; (c) treats a person not living with a spouse on the last day as single, and (e) treats spouses filing separately as single. There is no joint table. Asserted (the table at seven points).
2. **The DC personal exemption is the federal amount, so it follows federal law to nil.** From 2018 the deduction for each exemption is "the personal exemption amount prescribed in section 151 of the Internal Revenue Code" (s 47-1806.02(i)(2)). Where that amount is nil, so is every DC exemption, whatever the count under (b) to (f). The phase-out of (h-1) (2% for every $2,500 over $150,000; none over $275,000) and the (c) head-of-household rule (off when the amount is $2,200 or more) only bite when the federal amount is above nil. The amount is an input; what it is for a year is an IRC question. Asserted.
3. **The standard deduction is the federal one.** s 47-1801.04(44)(iv): "the standard deduction as prescribed in section 63(c)". It is an input.
4. **The EITC paragraphs overlap; the specific ones are read as displacing (A).** (f)(1)(A) gives 40% of the federal credit to "an individual who is allowed an earned income tax credit"; (B-1) to (B-3) give 70%, 85% and 100% to "an individual with a qualifying child"; (C) gives a worker with no qualifying child a credit worked out on its own formula. Read literally, (A) would add 40% on top of each. This encoding reads (A) and (B) as superseded for the people (B-1) to (B-3) and (C) describe, which is how the later paragraphs make sense, but the text does not say so. Interpretive. Asserted (with a child, 2025: 85% only).
5. **The childless EITC uses the federal credit percentage and earned income amount but a DC phaseout.** (C)(ii): 8.48% of AGI (or earned income if greater) over $17,235 "increased annually by the cost-of-living adjustment", and the federal "limit in section 32(a)(2)" is disregarded. The adjusted phaseout amount for a year is not deposited: an input. Asserted.
6. **A DC EITC of $1,200 or more may be paid in 12 monthly payments.** (f)(3)(B)(ii-a), for years after 2023, at the taxpayer's election; under $1,200 it is one lump sum. Payments are not income for public assistance ((f)(3)(C)). Asserted.
7. **The child tax credit is new for 2025 and needs a year of prior residence.** s 47-1806.17: $420 per qualifying child under 6, up to three, less $20 per $1,000 (or fraction) of AGI over $160,000, $240,000 or $120,000, refundable, but not for a taxpayer who "was not a resident of the District for the entire calendar year preceding the year in which a claim ... is filed". From 2026 the amounts are cost-of-living adjusted: `not covered`. Asserted.
8. **A deficiency is due in 10 days; the appeal window is 6 months.** s 47-1812.07(a)(3) and s 47-1815.01. The six months are given to the appeal rule in days, because the Code does not say how a month that runs short is counted. Asserted, and the rules traced.
9. **The chapter's own penalty sections are repealed.** Subchapter XIII (ss 47-1813.01 to 47-1813.07) reads "Repealed"; the additions to tax are elsewhere in Title 47 and not deposited, so the filing duty's breach says so.
10. **Residence turns on domicile at any time, or 183 days of abode.** Senate-confirmed appointees, elected federal officers, certain congressional staff and Supreme Court Justices are excluded from the 183-day limb unless domiciled in DC at some time in the year. Asserted.

## Before relying on it

- Encode s 47-1803.02 (DC gross income, the exclusions including Social Security and unemployment benefits) and the exemption count.
- Deposit the additions to tax (Title 47 ch. 42) and the Office of Tax and Revenue's annual cost-of-living figures.
- Schedule H (s 47-1806.06) is the credit most used by low-income renters and should be next.
- An independent test pass.
