# Northwest Territories Income Tax Act (personal tax, NWT Child Benefit, Cost of Living Offset) — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the Act's own terms in `nt-pit.l4` (computations) and `nt-pit-duties.l4` (the dated duties, kept apart so that only it loads the date library). The individual's questions are in `nt-pit-seat.l4`, which IMPORTs both and calls their rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Edition

- **Income Tax Act**, R.S.N.W.T. 1988, c.I-1, office consolidation dated **2023-11-23** (last amendment SNWT 2023, c.30), English version: `../../registers/source-bundle/income-tax.a.2023-11-23.txt`.
- **Income Tax Regulations**, R.R.N.W.T. 1990, c.I-1, consolidation dated **2025-06-02** (last amendment R-038-2025, in force 1 July 2025): `../../../income-tax-regulations/registers/source-bundle/income-tax.r1.2025-06-02.txt`. It sets the NWT Child Benefit amounts and thresholds (s 1.1) and the Cost of Living Offset zone amounts (s 1.2).
- **Canada Revenue Agency, "Current year tax rates and income brackets (2026)"** (page details 2026-06-25, retrieved 2026-10-24): `../../registers/source-bundle/cra-tax-rates-brackets-2026.txt`. Not law: deposited for the 2026 tier thresholds, which the Act produces by indexation and does not print (finding 1).
- The federal provisions the Act applies (s 11 applying federal s 150; the federal "balance-due day" in s 248(1)) are read in the federal Income Tax Act deposited at `subjects/ca/income-tax-act/registers/source-bundle/R.S.C.-1985-c.-1-5th-Supp..txt` (current to 2026-09-30).

The French version of the Act and Regulations is equally authoritative (Official Languages Act, s 7(1)) and is not deposited.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nt-pit.l4`, `nt-pit-duties.l4`, `nt-pit-seat.l4` | `nt-pit-cases.l4` | 78 written, 78 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Three `#TRACE`s show a breach (a return filed after 30 April 2027; a June instalment paid late; a late s 3.3(3) notice), each with its expected result in an `-- expect:` comment, because a breached `EVALTRACE` can be asserted neither way in the stable `l4`; each produced exactly the breach and reason expected. Every expected value was worked by hand from the texts.

## Seats

**The individual taxpayer resident in the Northwest Territories**, and **the parent** who claims the NWT Child Benefit and the Cost of Living Offset: "Do I pay NWT tax? How much, before and after credits? Must I file, and by when must I pay? How much NWT Child Benefit do I get, from which year's income, and by when must I apply or tell the CRA of a change?"

Provisions addressed to officials are encoded as what they mean to that person: the deemed overpayment of s 3.2 is the benefit the person is paid; the Minister's power to extend the notice period (s 3.3(2)) is an input to whether the notice was in time.

The 2026-10-18 defaults:

- **The Act, with the instruments that set its numbers:** the Income Tax Regulations (s 1.1, s 1.2). The indexed figures the Act produces but does not print are taken from the deposited CRA page where it states them (2026 thresholds) and are otherwise inputs (finding 2).
- **The actors the text names:** the individual, the Minister (of National Revenue, under the collection agreement, s 57) and the Commissioner.
- **Judgments handed to others are answered conditionally:** who "primarily fulfils the responsibility for the care and upbringing" (determined under the federal prescribed factors, s 3.1(1)(f) to (h)), and whether the Minister extended the notice period, are inputs.
- **The Act's own definitions are worked out from facts:** liability (s 2(1)), the tier rates and thresholds (s 2.11), appropriate and highest percentage (s 2.1), eligible individual and qualified dependant (s 3.1), base taxation year (s 3.1), the Cost of Living Offset's eligible individual (s 3.5(1)). **Borrowed federal terms are asked as facts:** residence, taxable income, net income, the federal credit bases, adjusted income (federal s 122.6), the federal disability tax credit entitlement (s 118.3), the federal instalment requirement (s 156.1).
- **One case:** one individual's return for one taxation year; for the Child Benefit, one month.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the collection agreement (Part III), the regulation-making power (s 33), appeals (Division E), offences (Part II).

## Regulative rules

Three, in `nt-pit-duties.l4`, each `LEST BREACH ... BECAUSE`:

1. `my duty to file` (s 11, applying federal s 150(1)(d)): where a return is required, the individual MUST file it WITHIN the days from 1 January of the year to 30 April of the next (15 June where the individual or the cohabiting spouse carried on a business).
2. `my duty to pay the tax` (ss 16, 17): where federal instalments are required, the individual MUST pay the March, June, September and December instalments by the 15th of each and the remainder by the balance-due day, joined by RAND; otherwise (s 17) MUST pay the tax by the balance-due day.
3. `my duty to notify that I ceased to be eligible` (s 3.3(3)): a person who ceases to be an eligible individual (other than because the child turned 18) MUST notify the Minister before the end of the month following.

The s 3.3(1) notice is a condition of eligibility, not a duty, so it is a date function (`the last day to file the s 3.3(1) notice for a month`) and an input to the amount.

## Questions exported (23)

§ Do I pay NWT income tax: liability (s 2(1)).
§ My territorial tax: the 2026 tax before credits; the tax before credits for another year, given its thresholds.
§ My territorial credits: basic (ss 2.14-2.16); age (s 2.2); pension (s 2.21); donations (s 2.22); disability (s 2.24(1), adult); education (s 2.26); tuition, student loan interest, CPP/EI (ss 2.25, 2.28, 2.29); dividend (s 2.32); the tax payable after credits.
§ Filing and paying: must I file; the filing date; the balance-due day; each instalment.
§ NWT Child Benefit: eligible individual; qualified dependant; the monthly amount; the base taxation year; the last day to apply for a month; the last day to report ceasing to be eligible.
§ Cost of Living Offset: the amount for a specified month.

## Scope

**In:** ss 2(1)(a), 2.1, 2.11(2)-(7), 2.13 (as the reason the amounts are inputs), 2.14, 2.15, 2.16, 2.2, 2.21, 2.22, 2.24(1) (adults), 2.25, 2.26, 2.28, 2.29, 2.32; 3.1, 3.2(1), (2), (2.1), 3.3(1), (3); 3.5(1)-(3); 11 (federal s 150(1)(d), (1.1)(b)); 16(1), 17; Regulations ss 1.1, 1.2.

**Out:** s 2(1)(b) non-residents and s 2.44 apportionment (`not covered`); taxation years before 2005 (`not covered`); ss 2.12, 2.42, 2.43 (additions and the split-income tax); ss 2.17, 2.18, 2.19 (in-home care, infirm dependant, additional dependant); s 2.23 (medical expenses); s 2.24(1)(c)(i) (supplement for a person under 18) and s 2.24(2) (transfer from a dependant); s 2.3 (transfers from a spouse, parent or grandparent); s 2.31 (minimum tax carry-over); ss 2.34-2.41 (the federal restrictions applied); s 3 (foreign tax); s 3.2(3)-(6), 3.3(4)-(6), 3.4 (the Child Benefit's special cases and elections); s 3.6 (the 2019-2020 first offset year); corporations (ss 4-4.1); political contributions (ss 5, 6); the investment tax credit (s 6.1); s 15 (farmers and fishers); the Regulations' payroll withholding (ss 2-5).

## What the Act turns out to say

1. **The Act does not print its own thresholds after 2004, so the 2026 thresholds come from the CRA.** Section 2.11(3) gives $33,245, $66,492 and $108,101 for 2004, and s 2.11(6) indexes them each year from the Consumer Price Index. The CRA page for 2026 prints $53,003, $106,009 and $172,346, with the rates 5.9%, 8.6%, 12.2% and 14.05%. Those rates are the s 2.11(2) rates, which is a check that the 2023 consolidation's rates are still the ones in force. The encoding uses the CRA's thresholds for 2026 and asks for them in any other year. The indexing rule itself is encoded and tested on hypothetical index values. Asserted.
2. **Almost every credit amount is indexed, and the deposited texts do not state the indexed figures.** Section 2.13 indexes every dollar amount in ss 2.14, 2.15, 2.16, 2.2 and 2.24(1)(b) (from 2004) and in ss 2.17, 2.18, 2.2(c), 2.23 and 2.24(1)(c) (from 2002). The figures printed in the Act ($11,050, $5,405, $26,941, $8,961) are the figures for 2003 or earlier. The NWT forms that print the indexed figures (TD1NT, the T4127 tables) are in a folder that canada.ca's robots.txt disallows, so they were not fetched. Those figures are therefore inputs, and the cases use hypothetical ones. The amounts that are not indexed are computed from the text: the $1,000 pension cap (s 2.21), the $200 donations step (s 2.22), the $400 and $120 a month education amounts (s 2.26), and the 6% and 11.5% dividend rates (s 2.32).
3. **"Adjusted in the manner that may be prescribed by federal regulations."** Sections 2.11(6) and 2.13 allow the CPI factor to be adjusted as federal regulations prescribe. No such adjustment is encoded. The factor is A/B - 1, rounded to the nearest one-thousandth with ties going up. The unrounded threshold carries forward to the next year, and the rounded one is used for the year (s 2.11(6)(a) reads "the amount that would, but for subsection (7), be the amount of the threshold for the preceding taxation year"). Asserted (33,876.655 is carried forward, 33,877 is used).
4. **No "if negative, nil" in the credits.** In ss 2.14 and 2.15, part (B) of B is "$11,050 - C", and the text does not say what happens when the spouse's or dependant's income C exceeds $11,050. Read literally, a spouse with high income would make the 2.14 credit smaller than the single status credit, and s 2.16 then excludes "an individual entitled to a deduction under section 2.14". The encoding reads (B) as nil when it is negative, as the federal Act does, so the credit never falls below the single amount. Asserted (a spouse with $20,000 of income gives 1,052.678, the single amount). It likewise reads B - C in s 2.2 as nil when negative, and does not let the credits take the tax below nil. The credits "may be deducted in computing the tax payable", and none of them is refundable. Asserted.
5. **The Child Benefit counts the two age groups separately.** Regulations s 1.1(1)(b) sets C by the number of qualified dependants under six ($815 for one, $1,467 for two, and so on), and (c) sets D by the number "not described in paragraph (b)". A family with one child under six and one child six or over therefore gets $815 + $652 = $1,467 a year, the same as two children under six. It does not get the "two qualified dependants" amount in both scales. Asserted.
6. **Above $80,000 the formula goes negative.** Section 3.2(2) phases the benefit out between B ($30,000) and E ($80,000). At E the result is exactly nil, and above E the formula gives a negative amount. The text states no floor. The encoding reads it as nil, because a deemed overpayment cannot be negative. Asserted.
7. **Shared custody gives half.** Under s 3.2(2.1) a shared custody parent gets (A + B)/2. B is the formula "calculated without reference to ... subparagraph (c)(ii) of the definition eligible individual". Subparagraph (c)(ii) is what makes a shared custody parent an eligible individual, so without it B is nil and the parent gets half of A. Asserted.
8. **The Cost of Living Offset is currently $0.** Regulations s 1.2(2) (R-022-2023, R-022-2024, R-038-2025) sets A, B and C at $0 in all three zones, so the s 3.5(3) deemed payment is 25% of nil. The machinery of s 3.5 is encoded so that a future regulation only has to change the three amounts. Asserted.
9. **The consolidation is old.** The Act is consolidated to 23 November 2023. The 2026 rates on the CRA page match s 2.11(2), but the deposited text does not show any change after 2023 to the credits or the Child Benefit. Before relying on the encoding, check the Annual Volumes for 2024 to 2026. Not asserted.

## What would need doing before relying on it

- Deposit the year's indexed credit amounts from an official, fetchable source, or confirm them with the Department of Finance, and add 2025 and 2027 thresholds as they are published.
- Check the Annual Volumes for amendments after SNWT 2023, c.30, and R-038-2025's successors.
- Encode the s 2.44 apportionment, the medical expense and caregiver credits, and the transfers.
- An independent test pass, and the human gates.

Cross-encoding link: the federal Income Tax Act encoding at `subjects/ca/income-tax-act/` (taxable income, net income, adjusted income and the federal credits are inputs here).
