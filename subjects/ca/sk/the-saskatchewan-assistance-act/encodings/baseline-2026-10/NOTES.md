# The Saskatchewan Assistance Act and The Saskatchewan Income Support Regulations — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. Where a formula has no meaning on the facts, the answer is `NOTHING`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the regulations' own terms in `sk-sis.l4`, with the five regulative rules there. The applicant's questions are in `sk-sis-seat.l4`, which IMPORTs the core and calls its rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of either text to keep. The Act is the enabling statute, and Saskatchewan Income Support (SIS) is a program made under it by regulation. The Act is in force; there is no separate "Saskatchewan Income Support Act".

## Licence and notice

Quoted under the Government of Saskatchewan's non-commercial reproduction terms, with the **owner's ruling of 24 Oct 2026** that texts permitting reproduction but silent on adaptation may be quoted in L4 encodings in Commons. Every module opens with the "unofficial version, not an official version" notice and "© 2026, Government of Saskatchewan." See `SOURCE-LICENSE.md` (a copy of the subject's).

## Edition

- **The Saskatchewan Assistance Act**, R.S.S. 1978, c. S-8, King's Printer consolidation, "Last update posted: 22 Aug 2024" (amended to S.S. 2024, c. 4), at `../../registers/source-bundle/R.S.S.-1978-c.-S-8.txt`.
- **The Saskatchewan Income Support Regulations**, R.R.S. c. S-8 Reg 13, King's Printer consolidation, "Last update posted: 9 Sep 2026" (amended to SR 45/2026), at `../../registers/source-bundle/R.R.S.-c.-S-8-Reg-13.txt`.

The Saskatchewan Assured Income for Disability Regulations, 2012 (Reg 11), deposited beside these, are not encoded.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sk-sis.l4`, `sk-sis-seat.l4` | `sk-sis-cases.l4` | 71 written, 71 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Five `#TRACE`s, each with its expected result in an `-- expect:` comment and each read as expected: four breaches (application confirmed on day 20, a change reported on day 5, a review request answered on day 40, the minister reconsidering on day 10 after the appeal) and one lapse of the appeal right with no breach. Every expected value was worked by hand from the text.

## Seat

**The individual applying for, or receiving, SIS for their household** (the regulations' "applicant", then "client", and the "primary household member"): "Can I apply? Who in my household is left out? How much of our income counts? Do our assets keep us out? Are we eligible, and how much will we get? What must I do, and by when? How do I appeal? What happens if I was overpaid? What can I be fined?"

Provisions addressed to the minister are encoded as what they mean to that person: the household has no budget deficit if the minister is satisfied it disposed of assets to qualify; the minister must reconsider an appeal within 7 days; an overpayment certificate can be filed only after 30 days.

The 2026-10-18 defaults:

- **The Act, with the regulations that set its numbers:** the SIS Regulations are the instrument that sets eligibility and the income and asset rules. They leave the benefit amounts to "the schedule of rates established by the minister" (s 3-1(3)). That schedule is policy, not law, and is not deposited, so the household's total benefit under it is an input (finding 1).
- **The actors the text names:** the applicant or client, the minister, and the appeal committee and appeal board (seen only through the deadlines that bind the applicant).
- **Judgments handed to others are answered conditionally:** whether the minister waives presence or residency (s 2-10(1)(d)), accepts an absence (s 2-5(d)), declines to count an asset (s 2-10), or is satisfied that assets were disposed of to qualify (s 2-6(5)(b)), or that resources are inadequate (s 2-4(1)(a)(iii)). Each is an input.
- **The regulations' own definitions are worked out from facts:** residency requirement, liquid asset (the life insurance threshold), excess asset, earned income, the income exemptions, budget deficit. **Borrowed terms are asked as facts:** spouse (The Family Maintenance Act, 1997, or the 3-month cohabitation test of s 1-2), refugee and permit statuses (IRPA), reserve (Indian Act), the federal benefits named in s 2-7(2).
- **One case:** one household in one month.
- **The regulations' own terms**, quoted in the comment above each rule.
- **Machinery out:** the Act's units, directors, agreements, reimbursement and regulation-making; the appeal hearing procedure (ss 3-13, 3-14(5)-(23)).

## Regulative rules

Five, in `sk-sis.l4`:

1. `my duty to confirm my application` (s 2-2(5), (6)): the applicant MUST confirm the application in person WITHIN 15 days of the request, `LEST BREACH` (discontinued).
2. `my duty to report a change` (s 3-8; Act s 29.2): the client MUST report a change "immediately", encoded WITHIN 1 day (finding 6), `LEST BREACH` (excess benefits are an overpayment, Act s 29.3).
3. `my duty to respond to a review request` (s 3-11(2)(a), (4)): the client MUST respond WITHIN 30 days, plus any extension, `LEST BREACH`.
4. `my right to appeal to the minister` (s 3-12(1), (2)): the applicant DOes appeal WITHIN 15 days, HENCE the minister MUST reconsider WITHIN 7 days `LEST BREACH BY the minister`; with no appeal, LEST FULFILLED (finding 7).
5. `my right to appeal to the appeal board` (s 3-14(1), (2)): the applicant MAY give notice WITHIN 15 days.

The appeal and review deadlines are also given as date functions for the seat.

## Scope

**In:** Reg ss 1-2 (residency requirement, liquid asset, excess asset), 2-1(3), 2-2(5), (6), 2-4, 2-5, 2-6(3)-(5), 2-7(2)(a), (d.1), (w.3) with the other exemptions as one input, 2-7(3), (1.1), (7), 2-10 (as conditional inputs), 3-1(1)-(3), 3-3(1), 3-8, 3-11(2), (4), 3-12(1), (2), 3-14(1), (2); Act ss 27, 28, 29.2, 29.3 (in rule 2's reason), 29.5(2), (5), 29.6(1), 29.7.

**Out:** the amounts of the Part 4 benefits (the minister's schedule); Part 4.1 (education and training incentive); emergency assistance and funeral benefits (ss 4-12, 4-15); supplementary health benefits (ss 2-6(6), 4-17); s 3-2 and s 3-3(2) (disposal of assets, which needs the minister's market value); reassessment timing (s 3-9); the 180-day and 24-month conversion periods of ss 2-8, 2-9 (noted, not computed); s 3-16 (students enrolled on 31 August 2026); SAID.

Read with the federal subjects (`subjects/ca/canada-pension-plan/`, `employment-insurance-act/`, `old-age-security-act/`, `canada-disability-benefit-act/`, `income-tax-act/`): their benefits are this encoding's income inputs, counted or exempt as s 2-7(2) says. Cross-folder IMPORT is not possible in the stable `l4`.

## What the regulations turn out to say

1. **The regulations do not say how much anyone gets.** Section 3-1(3) leaves the amount of the adult basic, shelter, diet, northern, child care, children's, training, relocation and other benefits to "the schedule of rates established by the minister", and s 3-1(5) lets those rates vary by household size, location, date of application "and any other criteria". The encoding can say whether a household is eligible and how its income reduces the benefit, but the benefit itself is an input. The cases use hypothetical totals. Asserted.
2. **Small, fixed exemptions.** Earned income is exempt only to $375 a month (single), $475 (couple) or $500 (with a child) (s 2-7(2)(a)), after income tax, CPP, EI and required employer deductions (s 2-7(3)). Child support is exempt to $600 a month per household, plus any special-expense portion above the Guidelines table (d.1). Gifts, prizes and winnings are exempt to $200 a month (w.3). The Canada Child Benefit, the GST/HST credit, tax refunds, the Canada Workers Benefit and the Canada Disability Benefit are exempt in full. Asserted.
3. **Other federal benefits count dollar for dollar.** Income is everything received "from all sources other than" the listed exemptions (s 2-7(2)). Employment Insurance, Canada Pension Plan and Old Age Security benefits are not listed, so they count in full against the benefit. The subject README marked this "unverified (general knowledge)"; the deposited text bears it out. Asserted (EI of $1,400 counts as $1,400).
4. **The asset limit is $2,000 per household member,** for liquid assets "greater than" that, so exactly $2,000 a person passes (s 2-6(4)). The first $1,500 of a life insurance policy's cash surrender value is not a liquid asset (s 1-2, (e)). Real property other than the home, and secondary or recreational vehicles with more than $5,000 of equity, are excess assets that rule the household out unless the minister decides otherwise (ss 1-2, 2-6(5)(a), 2-10). Asserted.
5. **The self-support period after a lump sum is a fraction.** T = L / (115% × N − I) months (s 3-3(1)). The text does not say whether T is rounded or how a part-month is treated. The encoding gives T unrounded. Where 115% of the benefits does not exceed the household's other income, the formula has no meaning (the divisor is nil or negative), and the answer is `NOTHING`. Asserted.
6. **"Report immediately"** (s 3-8) has no number of days. The encoding uses one day. Interpretive. Asserted as encoded.
7. **A right to appeal written as a right.** With L4's `MAY`, the `HENCE` branch also follows when the period passes unused, which would put the minister under a duty to reconsider an appeal never made. The appeal to the minister is therefore written `DO ... LEST FULFILLED`. Asserted by trace (no appeal: fulfilled; appeal on day 10, reconsideration on day 20: breach by the minister).
8. **A self-employment loss does not reduce other income.** Section 2-7(1.1): deductions "must not exceed[] the amount of income received from self-employment". Asserted.
9. **The minister's waiver does not reach the age of 18.** Section 2-10(1)(d) lets the minister waive "the residency requirement or the requirement to be ordinarily present in Saskatchewan", not the age requirement of s 2-1(3)(b). Asserted.
10. **The Act's penalties are small and old.** The maximum is $100 (three months in default) under s 27 and $200 (six months in default) under s 28, unchanged since 1978 and 1997. Asserted. Payments cannot be garnished, seized or assigned, except that an overpayment may be recovered from future payments (s 29.7). Asserted.
11. **Two appeal routes in the Act.** The Act's s 17.1 provides adjudicators for "income-tested programs" designated in the regulations, while the SIS Regulations send appeals to appeal committees and an appeal board under The Social Services Administration Act (ss 3-12 to 3-14). The SIS route is encoded. The regulations do not designate SIS as an income-tested program in the deposited text.
12. **Day counting.** Deadlines are counted in calendar days from the event. Whether The Legislation Act's rules on holidays extend them is not in the deposited text (not checked).

## What would need doing before this is worth relying on

- **The minister's schedule of rates** (adult basic benefit, shelter benefit by household size and location, and the rest), from a deposited Ministry of Social Services publication, so the benefit can be computed rather than entered.
- **SAID** (the disability program, R.R.S. c. S-8 Reg 11, already deposited), which has its own asset limits and income exemptions and is where many SIS applicants with disabilities belong.
- **Sections 3-2 and 3-3(2)** (disposal of assets) and the conversion periods of ss 2-8 and 2-9.
- **An independent test pass**, and a check of findings 5 and 6 against ministry policy (none was read).
