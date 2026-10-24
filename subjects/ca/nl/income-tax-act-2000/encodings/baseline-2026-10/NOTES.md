# Newfoundland and Labrador Income Tax Act, 2000 (personal income tax) -- baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the Act's own terms in `nl-pit.l4`; the one rule that needs dates (the s 34(8) duty to notify) is in `nl-pit-notice.l4`, so that only it and the seat import `daydate`. The taxpayer's questions are in `nl-pit-seat.l4`, which IMPORTs both and calls their rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Edition

- **Income Tax Act, 2000**, SNL2000 cI-1.1, House of Assembly consolidation as amended to 2026 c15, retrieved 2026-10-24: sections 2, 5, 6, 6.1, 7, 9, 17, 21.1, 23 and 34, deposited at `../../registers/source-bundle/SNL2000-cI-1.1-selected.txt`.
- **Income Supplement and Seniors' Benefit Regulations**, NLR 32/16, as amended to 17/26 (`NLR-32-16.txt`).
- **Low Income Tax Reduction Regulations for the 2024 Taxation Year**, NLR 60/24 (`NLR-60-24.txt`).
- **Department of Finance**, "Personal Income Tax" page (the 2025 and 2026 brackets and credit amounts), and its Low Income Tax Reduction and Income Supplement pages, retrieved 2026-10-24 (`nl-finance-*.txt`).

Taxation years **2025 and 2026** are encoded, because those are the years whose indexed brackets and credit amounts are published (finding 1).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nl-pit.l4`, `nl-pit-notice.l4`, `nl-pit-seat.l4` | `nl-pit-cases.l4` | 59 written, 59 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. One `#TRACE` shows a breach (notice of a change on day 50 against a 44-day limit), with its expected result in an `-- expect:` comment, because a breached `EVALTRACE` can be asserted neither way in the stable `l4`; the run shows `DEONTIC BREACHED ... BY the individual` as expected. Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**: "Must I pay Newfoundland and Labrador income tax? How much? What credits do I get, and what is paid back to me? What must I tell the CRA?"

The Minister of National Revenue (the Canada Revenue Agency, which administers the tax under a collection agreement) appears only as the person the individual must notify (s 34(8)) and the payer of the supplement (s 34(3)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** NLR 32/16 sets the supplement; NLR 60/24 sets the low income reduction amounts for 2024. The indexed amounts of s 6.1 are set by no instrument in the register; they are taken from the Department of Finance's published table (finding 1). Where no published figure exists, the number is an input (findings 3 and 5).
- **The actors the text names:** the individual, the Minister of National Revenue.
- **Judgments handed to others:** none needed in scope.
- **The Act's own definitions worked out from facts:** appropriate percentage (s 5(a)), eligible individual for s 21.1 (s 21.1(1)(b)). **Borrowed federal terms asked as facts:** taxable income, net income, residence, the s 118.7 base, the s 118(3) pension income amount, "eligible individual", "qualified relation", "qualified dependant" and "adjusted income" of ss 122.5 and 122.6, the disability tax credit (s 118.3(1)).
- **One case:** one individual's return for one taxation year.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** collection agreement, assessments, objections, appeals, regulation-making.

## Regulative rules

One, in `nl-pit-notice.l4`:

1. `my duty to notify the change` (s 34(8)): the individual MUST notify the Minister of National Revenue WITHIN the days from the event to the last day of the following month, `LEST BREACH ... BECAUSE`. Asserted fulfilled on day 30 of 44; the breach on day 50 is shown by `#TRACE`.

The tax itself is not written as a duty to pay because the deposited sections only charge it (s 6(1): "An income tax shall be paid as required by this Act"); the time of payment is in ss 49 to 56, not deposited.

## Questions exported (10, in `nl-pit-seat.l4`)

Must I pay (s 6(1)); the tax on my taxable income (s 7); my personal credits (ss 9, 17); the tax I pay after credits and the low income reduction (ss 23, 21.1); my low income reduction (s 21.1); my income supplement and seniors' benefit for the year (s 34, NLR 32/16 s 3); the amount paid each quarter (s 34(3)); whether it is paid in one amount (s 34(10), (11)); must I tell the CRA about a change, and by when (s 34(8)).

## Scope

**In:** s 6(1); s 7(1) with the s 6.1 indexed thresholds for 2025 and 2026; s 9(1)(a), (b), (c), s 9(2), s 9(3); s 17; s 21.1(1), (2), (2.1), (5); s 23 (the order, as far as it matters to non-refundable credits); s 34(1), (3), (8), (10)-(12) with NLR 32/16 s 3 and 3.1.

**Out:** a non-resident's or part-year resident's tax (ss 6(1)(b), 22, 25, 31, 31.1: `not covered`); trusts; ss 7.1 (the 2016-2019 deficit levy) and 32 (the 2007 surtax), which do not apply to 2025 or 2026; s 8 (lump sums); ss 9(1)(d), (e), (f) (caregiver and infirm dependant amounts); ss 10 to 16, 17.1 to 21 (gifts, medical, disability, tuition, education, student loan, adoption, child care, volunteer, physical activity, transfers, minimum tax carry-over, dividend and overseas credits); ss 29, 30, 33 (split income, minimum tax, foreign tax); s 21.1(3), (4) (the couple's single claim and the spouse's deduction of the unused part); s 34(2), (4)-(7), (9) (exclusions, shared custody, designation, death, bankruptcy); s 38 (the Newfoundland and Labrador child benefit) and the other refundable benefits under the Act's regulations; payment and administration (Part II from s 49).

Read with the federal Income Tax Act encoding, `subjects/ca/income-tax-act/` (being encoded by another session on 2026-10-24): taxable income, net income, the s 118.7 base, the pension income amount and adjusted income are inputs that encoding could supply. Cross-folder IMPORT is not possible in the stable `l4`.

## What the Act turns out to say

1. **The brackets in force are not the brackets in the text.** Section 7(1) prints $38,081, $76,161, $135,973, $190,363, $250,000, $500,000 and $1,000,000 "for the 2022 taxation year and subsequent taxation years", but s 7(2), (3) and s 6.1 index every threshold each year by the provincial CPI, rounded to the dollar. The indexed figures appear in no deposited instrument (the Personal Income Tax Indexation Regulations prescribe the formula, not the results). The Department of Finance publishes them: 2026 thresholds $44,678, $89,354, $159,528, $223,340, $285,319, $570,638, $1,141,275; 2025 thresholds $44,192, $88,382, $157,792, $220,910, $282,214, $564,429, $1,128,858. These are used. Asserted (2025 at $100,000; 2026 at $50,000 and $1,200,000; the printed thresholds at $38,081).
2. **The 2025 basic amount is not in the current text.** Section 9(1) now reads $13,094, and s 9(5) (added by 2026 c14) says that figure "shall not be adjusted ... before the 2027 taxation year". The Finance page gives $11,067 for 2025 and $13,094 for 2026, so the 2026 amendment raised the basic amount. The 2025 figures are the Finance page's, not the deposited text's. The Finance page prints the 2025 age amount as "$7.064", read as $7,064. Asserted ($962.83 of credit at $11,067).
3. **The income thresholds inside the credit formulas are indexed and unpublished.** The spouse and eligible dependant formula ("$6,055 - (C - $606)") and the age amount ("15% of the amount ... by which the individual's income for the year would exceed $33,226") carry thresholds that s 6.1 indexes. The Finance page publishes the indexed maximums ($9,142 and $7,142 for 2026) but not the thresholds, so the thresholds are inputs; the cases use hypothetical $915 and $37,000. Asserted as encoded.
4. **The credit formulas have no "if any".** Section 9(1)(a)(ii) and (b)(iv) and s 9(2) would give a negative amount when the other person's (or the individual's) income is high enough. The encoding treats a negative part as nil, as the federal practice does; the text does not say so. Asserted (a spouse with $20,000 of income leaves the basic amount alone).
5. **The low income reduction amounts are set year by year, and only 2024's is in force in the register.** Section 21.1(2.1) leaves A and B to regulation. The register's table of regulations under the Act (read 2026-10-24) lists only the Low Income Tax Reduction Regulations for the 2024 Taxation Year (A $974, B $544), which repealed the 2023 ones; no 2025 or 2026 regulation was found. A, B and the two indexed thresholds are therefore inputs. The Finance page's 2024 description ("eliminate provincial income tax for individuals with net income up to $23,390 ... partial tax reductions ... up to $29,478"; families $39,551 and $49,039) is consistent with thresholds of $23,390 and $39,551, since 974 / 16% = 6,087.50 and (974 + 544) / 16% = 9,487.50; the cases use those as hypothetical thresholds, not as published law. Asserted as encoded.
6. **The reduction is a deduction from tax and comes last** (s 21.1(5), s 23(2)(r)); it cannot make the tax negative. Asserted (a $974 reduction against $600.82 of tax leaves nil).
7. **The income supplement and seniors' benefit are fully stated in NLR 32/16.** The supplement is $254, plus up to $266 phased in at 5.32% above $15,000, plus $69 for a spouse and $231 a child, less 9% above $40,000; the disability amount is $231 each for the individual and spouse less 1.4% above $29,402; the seniors' benefit is $1,882 for an eligible individual aged 64 or over, one amount for a couple, less 11.66% above $30,409. The Finance page agrees, and its $46,550 end of the seniors' phase-out is 30,409 + 1,882 / 11.66% = 46,549.65. Section 3.1(2) suspends indexation of the seniors' amounts for 2026. The regulation does not say which taxation year its current amounts apply to; the encoding applies them to 2025 and 2026. Asserted (eight cases).
8. **A quarter is paid in each of four months after the year** (July and October of the next year, January and April of the year after: s 34(3), (12)), and all at once in the first month when each quarter would be under $10 (s 34(10), (11)). Asserted.
9. **A change must be notified by the end of the next month, except a child's 19th birthday** (s 34(8)(c): "otherwise than because of attaining the age of 19 years"). Asserted, with the year-end and leap-year cases.
10. **The surtax and the deficit levy are spent.** Section 32 applies only to 2007, s 7.1 only to 2016 to 2019; neither touches 2025 or 2026.

## Before relying on it

- Michael to confirm that the House of Assembly's terms fall within the 24 October 2026 ruling (`SOURCE-LICENSE.md`).
- Replace the hypothetical thresholds with official 2025 and 2026 figures (s 9(1), s 9(2), s 21.1) once a deposit can carry them, and add the 2025 and 2026 low income tax reduction regulations when they are filed.
- Deposit and encode ss 49 to 56 (returns, payment) if the duty to pay is wanted as a regulative rule, and s 38 with the Child and Parental Benefits Regulations for the child benefit.
- An independent test pass, and a cross-check against the federal encoding's taxable income.

## Access

The House of Assembly site (assembly.nl.ca) and gov.nl.ca were reachable over HTTPS with the honest user agent, at least 3 s between requests; robots.txt read first on each host. About 25 requests in all. A request for the CRA's provincial form NL428 on canada.ca was sent before its robots.txt had been read; canada.ca's robots.txt disallows `/content/dam/cra-arc/formspubs/`, so the file was deleted unread and nothing from it is used.
