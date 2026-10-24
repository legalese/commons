# The Income Tax Act, 2000 (Saskatchewan) — baseline encoding, 2026 taxation year

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the Act's own terms in `sk-pit.l4`, with the two regulative rules there. The taxpayer's questions are in `sk-pit-seat.l4`, which IMPORTs the core and calls its rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Act to keep.

## Licence and notice

The Act and Reg 7 are quoted under the Government of Saskatchewan's non-commercial reproduction terms, with the **owner's ruling of 24 Oct 2026** that such texts (reproduction permitted, adaptation not addressed) may be quoted in L4 encodings in Commons. Every module opens with the "unofficial version, not an official version" notice and "© 2026, Government of Saskatchewan." The CRA page is quoted under the Government of Canada's non-commercial reproduction terms, with its title, author and URL. See `SOURCE-LICENSE.md` (a copy of the subject's).

## Edition

- **The Income Tax Act, 2000**, S.S. 2000, c. I-2.01, King's Printer consolidation, "Last update posted: 16 Sep 2026" (amended to S.S. 2026, c. 20), deposited at `../../registers/source-bundle/S.S.-2000-c.-I-2.01.txt`.
- **The Saskatchewan Low-income Tax Credit Regulations**, R.R.S. c. I-2.01 Reg 7, last update posted 13 Jan 2026, at `../../registers/source-bundle/R.R.S.-c.-I-2.01-Reg-7.txt` (s 3: C and D for 2026).
- **Canada Revenue Agency, "Current year tax rates and income brackets (2026)"**, page dated 2026-06-25, retrieved 2026-10-24, at `../../registers/source-bundle/cra-tax-rates-brackets-2026.txt`: used only for the two 2026 Saskatchewan bracket thresholds. It is an official publication, not law (finding 1).

**Taxation year 2026 only.** It is the one year for which the Act itself states the main credit amounts (ss 11(3)(b), 12(3)(b), 13(3)(b), 19(4)(b), 20(1.2)(b)) and Reg 7 states the low-income credit figures. Other years answer `not covered`.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sk-pit.l4`, `sk-pit-seat.l4` | `sk-pit-cases.l4` | 75 written, 75 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Three `#TRACE`s, each with its expected result in an `-- expect:` comment and each read as expected: a payment on day 130 against the 120-day balance-due day (breach by the individual), a creditor garnishing the low-income credit refund (breach by the creditor), and a year in which no creditor acts (fulfilled). Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**: "Must I pay Saskatchewan tax? How much? What credits do I get? How much low-income tax credit will I be paid, and when? Must I file, and by when must I pay? Can a creditor take my credit?"

Provisions addressed to the minister (the federal Minister of National Revenue under the collection agreement, s 2(s), s 68) are encoded as what they mean to that person: the s 39 amount "is deemed to be an amount paid ... on account of the individual's tax payable" in the specified months, i.e. it is paid to them.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers:** Reg 7 (the 2026 C and D of s 39) is brought in. The indexation of s 51(3) and (5) needs the Consumer Price Index, which no deposited instrument states; where the Act leaves a 2026 figure to it, the figure is taken from the deposited CRA page (the two thresholds) or is an input (finding 2). Where the law lets the minister fix portions between claimants (ss 16.2, 19.12(8)), nothing is encoded.
- **The actors the text names:** the individual, and (s 40) anyone who would charge, assign, garnish, attach, seize or set off the refund.
- **Judgments handed to others are answered conditionally:** none arise in the encoded sections, apart from the federal minister's designation between spouses for the low-income credit (federal s 122.5(5), adopted by s 39(11)): the encoding asks the individual whether they are the eligible individual.
- **The Act's own definitions are worked out from facts:** appropriate percentage (s 5(1)(a)), liability (s 6(1)), the credit amounts, the s 19(1.1) rule between spouses, B, C, D and A of s 39. **Borrowed federal terms are asked as facts:** taxable income (s 7), income for the year, "income earned in the taxation year in Saskatchewan" (federal regulations), the federal s 118(1)(a) and (b) statuses, qualified dependant (s 122.6), eligible individual, qualified relation and adjusted income (s 122.5), shared-custody parent, the s 118(3) pension amount, the s 118.7 contributions, s 118.3 eligibility, the filing-due date and balance-due day.
- **One case:** one individual's return for one taxation year.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** collection agreements (Part V), assessments, objections and appeals, administration and enforcement (Parts VI and VII, except ss 75 and 81), regulation-making, transitional provisions.

## Regulative rules

Two, in `sk-pit.l4`:

1. `my duty to file and pay` (s 75, adopting federal s 150; s 81(b)): where the individual has tax payable, they MUST file the return WITHIN the days from 31 December to the filing-due date, and MUST pay the tax as estimated WITHIN the days to the balance-due day, joined by RAND, each with `LEST BREACH ... BECAUSE`. With no tax payable, FULFILLED.
2. `the protection of my low-income tax credit refund` (s 40): outside the s 40(2) cases, a creditor SHANT charge, assign, garnish, attach, seize or set off the s 39 refund, `LEST BREACH ... BECAUSE`.

## Scope

**In:** ss 5(1)(a), 6(1), 7 (as an input), 8(1)-(3) for 2026; Division 2 for 2026: ss 11(3)(b), 12(3)(b), 13(3)(b), 17 (indexed figures as inputs), 18, 19(1.1)-(4)(b), 20(1.2)(b) and (2), 21, 23 (2026 figure as an input), 28; the basic tax after those credits (other credits as one input); s 39(3), (3.1), (4), (5.2)(c), (6.3) with Reg 7 s 3, (7), (8), (9); s 40; s 75 (filing) and s 81(b) (payment).

**Out:** taxation years other than 2026; trusts (s 9); s 6(2) exemptions (`not covered`); ss 14, 15, 16, 16.2 (caregiver and infirm dependant credits and their limits), 19.1-19.5, 22 (medical expenses), 24-27, 29 and Division 3 (dividend, foreign tax and other credits), entered as one input total; the under-18 impairment supplement (s 23(2.4)); the active families benefit (s 39.3, which needs The Active Families Benefit Act, 2021, not deposited), the graduate tuition credits, the fertility treatment credit (s 39.5), the expired s 38 child benefit and s 39.4 affordability credit; Division 5 apportionment for part-year residents and non-residents beyond s 8(3); minimum tax and tax on split income (Division 6); instalments (ss 79, 80); interest and penalties.

Read with the federal Income Tax Act, `subjects/ca/income-tax-act/` (being encoded by another session on 2026-10-24): taxable income, net income, the federal statuses and amounts above are inputs that encoding could supply. Cross-folder IMPORT is not possible in the stable `l4`.

## What the Act turns out to say

1. **The bracket thresholds in s 8(1) are the 2018 ones.** Section 8(1) states $45,225 and $129,214 "for the 2018 through 2020 taxation years", and s 8(2) indexes them from 2021 under s 51(3) by the Consumer Price Index. The 2026 thresholds are therefore in no Saskatchewan text, except indirectly: Reg 7 s 3's formula D = $54,532 − $460/0.03029 uses MB, "the dollar value for the taxation year as determined in clause 8(1)(a), subject to subsection 8(2)" (s 39(6.3)), so the 2026 first threshold is $54,532. The CRA page gives $54,532 and $155,805; both are used. Asserted ($54,532: $5,725.86; $200,000: $24,793.26).
2. **The main 2026 credit amounts are written into the Act; the rest are indexed out of sight.** The 2024-2026 amendments wrote the 2025 and 2026 basic personal ($20,381), spousal and equivalent-to-spouse ($20,381 less income over $2,038), dependent child ($8,358) and senior supplementary ($2,569) amounts into the text, with a further $500 a year for 2027 and 2028. The age amount and threshold, the impairment amount and the low-income credit's child amount are still left to s 51 indexation, so for 2026 they are inputs; the cases use hypothetical figures. Asserted.
3. **Reg 7 states the 2026 low-income credit base amount.** Section 39(5.2)(c)(i) defines the 2026 amount L by a chain ("[$429 adjusted in accordance with subsection 51(5)] × 1.05", then × 1.05 and adjusted again), which the text never evaluates. Reg 7 s 3 does, as the numerator of D: $460. The encoding uses $460 for B's individual, qualified relation and (iii) amounts. Asserted.
4. **Some formulas have no floor.** The spousal and equivalent-to-spouse TCA ($20,381 − (SI − $2,038)) and the low-income credit A = ¼ × (B − C) carry no "if any". A negative amount would add tax or claw back other payments, which nothing else in the Act suggests. The encoding reads each as nil when negative, as the federal models (s 118(1), s 122.5(3)) do. Interpretive. Asserted (spouse with $25,000: nil; single with $60,000 of adjusted income: nil).
5. **The low-income credit counts at most two children, and fewer for a single parent.** Under s 39(5.2)(c)(iv), the child amount is paid once, or twice "if ... the individual has two or more qualified dependants". A single parent who claims the eligible-dependant amount gets the full $460 for that child under (iii) and then a single child amount however many others there are. A couple with four children gets the same as one with two. Asserted.
6. **Between cohabiting spouses, the dependent child credit goes to the lower earner.** Section 19(1.1)(b) allows it to an individual whose spouse's "taxable income ... is greater than the individual's", and on a tie only if the other renounces. Asserted.
7. **The low-income credit is paid in one lump if it is small.** Section 39(9) adopts federal s 122.5(3.1) and (3.2), but with "$7" for the federal $50: a quarterly amount under $7 is paid as the year's total in July. Asserted ($5 a quarter: $20 in July 2027).
8. **The refund is protected from creditors, with two exceptions.** Section 40(1) puts the s 39 refund beyond charge, assignment, garnishment, attachment, seizure and provincial set-off, but s 40(2) keeps the federal s 164(2) set-off against other debts and garnishment for family support under the federal Family Orders and Agreements Enforcement Assistance Act. Asserted.
9. **The Saskatchewan child benefit is closed.** Section 38(4): no overpayment arises "after June 30, 2006". It is left out. Section 39.4's affordability credit was a one-time $500 for 2021 filers. It is left out too.
10. **Section 18's $1,000 pension amount and s 21's $200 gifts threshold are not indexed**, and s 21 gives the 14.5% top rate on gifts over $200 whatever the donor's bracket. Asserted.
11. **Filing and payment dates are federal.** Section 75 adopts federal s 150 (the filing-due date) and s 81 the federal "balance-due day" (s 2(d)), so the encoding takes both as dates. For a living individual both are usually 30 April of the next year (unverified (general knowledge): 15 June for filing where the individual or spouse carried on a business). Asserted for 30 April 2027.
12. **Source formatting.** The deposited text flags the 2016-2019 formula for D in s 39(6) as unresolved. It is not used. The 2026 formula in Reg 7 s 3 was read as positioned on the page: "$54,532 − $460 / 0.03029", matching the form of s 39(6.2) and (6.3).

## What would need doing before this is worth relying on

- **The 2026 indexed amounts** (age amount and threshold, impairment amount, low-income child amount) from a deposited official publication, so they need not be inputs. The CRA's form SK428 and the TD1SK are in a folder canada.ca's robots.txt disallows; a Saskatchewan Ministry of Finance publication may serve.
- **The other Division 2 credits** (ss 14-16, 22, 24-27, 29) and the dividend credit (s 32), now one input.
- **2027 and later**, once their indexed figures are deposited.
- **The federal inputs** from the federal Income Tax Act encoding.
- **An independent test pass**, and a check of findings 4 and 5 against CRA or Saskatchewan guidance (none was read).
