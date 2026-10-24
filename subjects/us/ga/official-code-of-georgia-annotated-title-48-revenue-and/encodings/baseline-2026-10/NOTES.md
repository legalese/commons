# Georgia individual income tax: baseline, October 2026

## Method

Written directly from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18. The checks used the stable `l4` of the VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. There was no pipeline, no coverage table, no independent test pass and no human gate.

The Georgia Code itself could not be deposited, because the O.C.G.A. public access site (LexisNexis) puts every section behind a CAPTCHA. This encoding is therefore written from **the two 2026 session laws** that set the individual income tax for 2026 onward, as passed by both houses and published by the General Assembly:

- `ga-2026-act-465-hb-463-ap.txt`: HB 463, the "Georgia Economic Growth and Tax Relief Act of 2026" (Act 465, signed 11 May 2026, applicable to taxable years beginning on or after 1 January 2026).
- `ga-2026-act-374-hb-1000-ap.txt`: HB 1000, which adds Code section 48-7-20.4, the one-time refund (Act 374, effective 20 March 2026).

A Georgia bill that revises a Code section prints the whole revised text, striking through deleted words and underlining new ones. Plain text loses both marks. They were read back from the PDF's drawn rules and recorded in `ga-2026-act-465-hb-463-ap.formulas.md`, and this encoding follows that record. Expected values in the case file were worked out by hand from the text as the sidecar reads it.

## Edition

- HB 463/AP and HB 1000 (LC 59 0225-EC/AP), both retrieved 2026-10-24 from www.legis.ga.gov.
- Taxable years 2026 onward.
- Encoded: 48-7-20(a) and (a.1)(1); 48-7-26(b); 48-7-27(a) intro and (a)(1), (1.1), (5)(A)(xiii)-(xiv), (16), (17); 48-7-20.4.

## Checks

| file | errors | warnings | assertions | satisfied |
|---|---|---|---|---|
| `ga-income-tax.l4` | 0 | 0 | 0 | 0 |
| `ga-income-tax-cases.l4` | 0 | 0 | 58 | 58 |

The case file also runs three `#TRACE`s whose outcome cannot be asserted on the stable `l4`. Each has an `-- expect:` line, and each gave what it says: a residual Department duty to credit $500 after a $499 credit, the employer's breach, and the overtime-and-tips duty breached at day 31.

## Seat

**The individual taxpayer resident in Georgia for the whole taxable year.** Their questions: what rate do I pay; what standard deduction and dependent exemption do I get; how much of my retirement income, overtime and cash tips is left out; how much do I owe; do I get the one-time refund, and how much is it?

Provisions addressed to others are encoded for what they mean to that person:

- the Department of Revenue must credit and pay the one-time refund (48-7-20.4(b)(1), (d));
- the employer must report overtime and tips data with each withholding return (48-7-27(a)(16)(C), (17)(B));
- the Office of Planning and Budget's December 1 determinations, which delay each annual step (48-7-27(a)(1.1)), are a judgment left to someone else. They are asked as a fact: how many determinations found a delay.

## Defaults followed, and departures

- **Scope: the Act alone.** Followed for the deposited text. The Code sections the bills only partly print (the rest of 48-7-27(a), 48-7-27(b), and 48-7-27(a)(5)(D)) are asked as facts, not guessed.
- **Actors as named.** The taxpayer, the department, the employer and the Office of Planning and Budget.
- **Judgments left to others, as conditions.** The Office of Planning and Budget's determinations, and which division of (a)(5)(D) a retiree meets.
- **Definitions from facts, borrowed terms as facts.** "Federal adjusted gross income", the federal itemized deductions and "qualified overtime compensation" (IRC s 225) are borrowed federal terms. They are answered by the Internal Revenue Code encoding being written alongside this one (`subjects/us/internal-revenue-code-of-1986/`). Cross-folder IMPORT is not possible in the stable `l4`, so the link is stated here.
- **One case is one return for one taxable year.**
- **Departure: two Acts, not one.** HB 1000 is a separate Act. It is encoded in the same module because it is a refund of the same tax to the same person.

## Scope

**In scope:**
- the rate, and its annual steps and delays;
- the standard deduction or the federal itemized deductions;
- the dependent exemption;
- the retirement income exclusion amounts;
- the overtime and cash-tips subtractions, and the employer's duty to report them;
- Georgia taxable net income and the tax for a full-year resident;
- the one-time refund: who qualifies, how much, and the Department's duty to credit and pay it.

**Out of scope:**
- nonresidents and part-year residents for the tax itself. Their Georgia taxable net income is prorated under 48-7-85, which is not deposited, so they answer `not covered`;
- taxable years before 2026 (`not covered`);
- who must file a return (48-7-56, not deposited);
- residency (48-7-1, not deposited);
- the other subtractions of 48-7-27(a) and the additions of 48-7-27(b), which are taken as one net figure;
- credits, including the low-income credit and those repealed by Part IV;
- withholding;
- Part III, the Revenue Shortfall Reserve and the Taxpayer Relief Fund;
- corporate and partnership rates.

## Questions exported

10 questions, each with `@export` and `@desc`, under four `§§` groups:
- "The rate and the deductions" (4): the rate, the standard deduction, which deduction is better, the dependent exemption;
- "Retirement income, overtime and tips" (3);
- "What I owe" (1): the tax;
- "The one-time refund (HB 1000)" (2): am I a qualified taxpayer, and how much.

## Regulative rules

There are 2 `DEONTIC` rules:
- 48-7-20.4(a), (b)(1), (d): I file my 2025 return by the due date (DO ... LEST FULFILLED: filing late is no breach, it only earns no refund). The Department must then credit the refund amount, and then pay it net of any outstanding liability. No time is set for the Department.
- 48-7-27(a)(16)(C), (17)(B): my employer must report overtime and tips data by the due date of the corresponding withholding return. The number of days is an input.

## What the Acts turn out to say (findings)

1. **"0.125 percent" is a step of 0.125 percentage points.** (a.1)(1) reduces "4.99 percent ... by 0.125 percent annually ... until the rate reaches 3.99 percent". Read as a relative cut, 0.125 percent of 4.99 percent would never reach 3.99 percent in any sensible time. The struck text it replaces ("5.19 percent ... reduced by 0.10 percent ... until the rate reaches 4.99 percent") is the same pattern in percentage points. Encoded as points. Asserted.
2. **"Reductions in the standard deduction" means its increases.** (a.1)(1) delays the rate cut "by one year for each year that prospective annual reductions in the standard deduction are delayed". The standard deduction only ever increases (48-7-27(a)(1)(B), (1.1)(A) "Each prospective increase"). Read as the increases. The rate's own delay tests in old (a.1)(2) and the OPB reporting in (a.1)(3) are struck through in full (sidecar), so the rate now moves only in step with the deduction.
3. **The four figures step together and finish together.** The rate falls 0.125 to 3.99 (8 steps from 4.99). The joint deduction rises $750 to $36,000 (8 steps from $30,000), the other deduction $375 to $18,000 (8 steps from $15,000), and the dependent exemption $125 to $6,000 (8 steps from $5,000). All four share the (1.1) delays. With no delays the final figures apply from 2034. Each delay pushes all four back a year. Asserted (2034, 2040, and 2030 with two delays).
4. **Cash tips have no end year in (A), but (E) repeals the paragraph on 31 December 2028.** (17)(A) reads "For all taxable years beginning on or after January 1, 2026". (17)(E) reads "This paragraph shall stand repealed and reserved on December 31, 2028". Overtime ((16)(A)) says "ending on December 31, 2028" outright. The encoding subtracts both for 2026-2028 and neither from 2029. Whether a repeal "on" 31 December 2028 still reaches the 2028 return is a reading. The encoding reads it the same as (16). Asserted.
5. **The retirement exclusion is per taxpayer.** (xiii) and (xiv) give each amount "for each taxpayer meeting the eligibility requirement". On a joint return each spouse has their own cap. (xiii) is cut off at taxable years "ending on or before December 31, 2026", and (xiv) raises the division (iii) amount from $65,000 to $70,000 from 2027. That change is not subject to the (1.1) delays. Asserted.
6. **Eligibility for the exclusion is in 48-7-27(a)(5)(D), which is not deposited.** The bill prints only "division (i) or (ii)" and "division (iii)" of subparagraph (D). The person states which they meet. (It is commonly described as age 62-64 or disabled for (i)/(ii) and 65 or older for (iii): unverified, general knowledge, and not encoded.)
7. **Nothing in the deposited text deals with a negative Georgia taxable net income.** The encoding taxes nil when the figure is negative. `Georgia taxable net income for` itself returns the negative figure. Asserted (the retired couple, -750).
8. **The election in 48-7-27(a)(1) is the taxpayer's.** (A) is "the sum of all itemized nonbusiness deductions used in computing such taxpayer's federal taxable income". Read literally, that needs the taxpayer to have itemized on the federal return. The encoding takes the figure the person states (0 if they do not itemize federally) and answers with the larger of the two.
9. **The 2026 cuts are retroactive.** HB 463 was signed on 11 May 2026 and applies to "all taxable years beginning on or after January 1, 2026" (Section 5-1).
10. **The one-time refund is fixed to the 2024 return's line numbers.** 48-7-20.4(b) measures the refund by "Line 16 of the 2024 Georgia Form 500 or Line 4 of the 2024 Georgia Form 500EZ". Proration uses "Schedule 3, Line 9". These are asked as facts. The text sets no date by which the Department must credit or pay, so the rule has no `WITHIN`. The refund carries no interest ((e)) and is subject to setoff ((f)). The due date for the 2025 return is not in the deposited text, so the days to it are an input.
11. **The qualifying test is about filing, not paying.** A dependent for 2024 is out unless they had earned income for 2024 ((a)(1)(B), (a)(2)). The refund can never exceed the 2024 liability ((b)(1)(A), (b)(3)). Asserted.

## Before relying on it

- Deposit the codified O.C.G.A. sections 48-7-1, 48-7-20, 48-7-26, 48-7-27 (all of it) and 48-7-56 from a source that permits it. That would replace the session-law reading and the sidecar, and bring in residency, filing, the other subtractions and additions, and (a)(5)(D).
- Bring in the Department of Revenue's published figures for each year (any OPB delay), or the OPB determinations themselves.
- Add 48-7-85 for part-year residents and nonresidents.
- Run an independent test pass, and link the federal AGI computation once the IRC encoding has one.
