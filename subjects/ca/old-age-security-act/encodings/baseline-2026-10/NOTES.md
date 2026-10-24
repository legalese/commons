# Old Age Security Act: baseline encoding for the person applying for, or receiving, Old Age Security

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit value (`no pension: ... unless a social security agreement applies`, or `NOTHING` from the core), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`oas-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the applicant", "the pensioner", "the spouse or common-law partner", "the survivor", "the Minister"). The computations (income, the pension in fortieths, deferral, the supplement and its top-up, the allowances) are functions. Where the text says "shall" or sets a period, there is a regulative rule (`DEONTIC`): six in all.
- **`oas-seat.l4`**, the applicant's seat: 9 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings (Part I pension; Part II supplement; Part III Allowance; Part III Allowance for the Survivor, the last two marked as situations). It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed. No requirement ledger covers Canada, so no ledger line is closed.

## Edition

- **Act:** Old Age Security Act, R.S.C., 1985, c. O-9, Justice Laws consolidation **current to 2026-09-30**, last amended 2025-10-01, deposited at `../../registers/source-bundle/R.S.C.-1985-c.-O-9.txt` (from justicecanada/laws-lois-xml commit `0507465393c2`).
- **Regulations:** Old Age Security Regulations, C.R.C., c. 1246, same consolidation, last amended 2026-06-12, at `../../registers/source-bundle/C.R.C.-c.-1246.txt`.
- **Indexed figures are inputs.** Every dollar amount in the Act is indexed each quarter to the Consumer Price Index (ss 7(2), 12(2), 12.1(3), 22(4.2), 22.1(4); Regulations ss 8-9). No official table of the indexed amounts is deposited, so the six figures for the payment quarter (`OAS quarter figures`: the full monthly pension, the two statutory maximum supplements, the survivor's supplement equivalent, and the two top-up "A" figures) are asked. The case file uses round **hypothetical** figures and says so. The Act's constants (40 years, fortieths, 0.6%, 10%, $5,000, $2,000, $4,000, the $2, $3 and $4 rounding multiples, 90 days, six months) are written in.

Unofficial reproduction; not an official version. Contains information licensed under the Open Government Licence - Canada.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `oas-core.l4`, `oas-seat.l4` | `oas-cases-applicant.l4` | 72 written, 72 satisfied |

In addition, 5 `#TRACE`s carry an `-- expect:` line: three breaches by the applicant and two obligations still pending. Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The individual applying for, or receiving, an Old Age Security benefit**: the pensioner, the pensioner's spouse or common-law partner aged 60 to 64, or the survivor. They ask: "Can I get the pension, and how many fortieths?", "How much, if I defer it, and after 75?", "Will it stop while I am abroad?", "What is my income for the GIS?", "How much GIS?", "Can I (or my spouse) get the Allowance, or the Allowance for the Survivor, and how much?".

Much of the Act addresses the Minister. Those provisions are encoded for what they mean to the person: when no supplement or allowance may be paid to them, what they must state and tell the Minister, and the reconsideration they may ask for (with the Minister's duty to reconsider and notify, as the HENCE branch).

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** The Regulations are brought in for residence (s 21(1)), rounding (ss 7, 8), the $2 minimum allowance (s 6), the duties to report absence (s 25) and the cancellation periods (s 26.1). The quarterly indexed amounts are not in a deposited instrument and are inputs.
- **The actors the text names:** the applicant or beneficiary and the Minister.
- **Judgments left to others are answered conditionally, as inputs:** "the Minister is informed and satisfied" of a conviction (s 21.1), separation for s 15(4.1) (asked as "living with or separated three months or less"), legal residence (asked as a fact; Regulations s 22 not encoded), the Minister's waiver of the income statement (s 14(1.01)).
- **The Act's own definitions are worked out from facts:** "income" (s 2, for months after June 2020), "special qualifying factor" and "specially qualified individual" (s 2), "monthly base income" (s 12(6)), "monthly joint income", "residual joint income", "rounded pension equivalent" (s 22(1)), "survivor" (s 2). Borrowed terms are asked as facts: income under the Income Tax Act, EI premiums, CPP contributions, a sponsorship undertaking under the Immigration and Refugee Protection Act.
- **One case:** one person and one month (with the base calendar year's incomes).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** agreements with provinces and other countries (ss 39-43), offences and penalties (ss 44-44.2), the Consumer Price Index mechanics (s 27; Regulations s 9), appeals to the Tribunal (s 28), administration.

## Scope

**In:**

- s 2 "income" (paragraphs (a)(ii)-(iii), (b), (b.1), (c), (c.1), (d), (e)), "special qualifying factor", "specially qualified individual", "survivor"; s 2.1
- s 3(1)(b)-(c), (2)-(4): full and partial pension; s 4(1) legal residence
- s 7(5), s 7.1(1)-(6): the 10% from 75 and voluntary deferral
- s 9(1)-(4): suspension outside Canada
- s 11(7)(b)-(e): months for which no supplement
- s 12(5)-(6) and s 12.1(1)-(2): the supplement and its top-up
- s 19(1)-(2), (6)(b)-(d): the Allowance; s 21(1)-(2), (9)(b)-(c), s 21.1(1): the Allowance for the Survivor
- s 22(1)-(4), (6) and s 22.1(1)-(3): the amounts under Part III
- Regulations ss 6, 7, 8(2), 21(1), 25(1), 26.1
- Duties: s 14(1), s 15(9), s 27.1(1)-(2), s 37(1), s 9.3 with Regulations s 26.1, Regulations s 25(1)

**Out:**

- s 3(1)(a) (a pensioner on 1 July 1977) and the pre-1996 and pre-2001 savings in "specially qualified individual"
- benefits through a social security agreement (s 40): a person with under 10 years' residence is answered "unless a social security agreement applies"; the special qualifying factor is computed for such a person but the agreement's totalisation is not
- retroactivity and commencement (ss 8, 11(7)(a), 19(6)(a), 21(9)(a), 23; Regulations ss 10-12), the waiver of applications (ss 5(4)-(8), 11(3.1)-(6), 19(4.1)-(4.3), 21(5)-(5.3)), and estimated income on retirement or loss of pension income (s 14(2)-(7))
- the income definitions for months before July 2020 and s 13
- the s 12(5.1) couple enhancement (a "may" for the Minister), incarceration rules (ss 5(3), 8(2.1), 9.2, 19(6)(f), 21(9)(d), 22(2.1)), s 12(1)(b)(i) for the months before a spouse's pension begins
- the OAS recovery tax ("clawback"): that is Part I.2 of the Income Tax Act (s 180.2), for the Income Tax Act encoding
- overpayment recovery machinery (s 37(2)-(4)), the Minister's remedial power (s 32)

## Read with the Income Tax Act encoding

`../../../income-tax-act/encodings/baseline-2026-10/` (being encoded on 2026-10-24 by another session) answers the borrowed terms this encoding takes as inputs:

- **"income ... computed in accordance with the Income Tax Act"** (s 2): the starting figure of the GIS income question is the person's net income under the ITA.
- **The s 121 dividend tax credit and "tax for the year otherwise payable"** (s 2(d)), and **ss 56(1)(q.1), 56(6), 60(y), (z)** (s 2(e)).
- **The OAS recovery tax** under ITA Part I.2 (s 180.2), which recovers the pension from higher incomes; the pension itself is income under ITA s 56(1)(a)(i).

Also read with `../../../canada-pension-plan/encodings/baseline-2026-10/` (CPP contributions are deducted in s 2(a)(iii) and (b)(i); a CPP death benefit is deducted in s 2(c)(ii)) and `../../../employment-insurance-act/encodings/baseline-2026-10/` (EI premiums, s 2(a)(ii) and (b)(ii)). The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

## What the Act turns out to say

1. **A partial pension carries the 10% from 75 through the full pension it is a fraction of.** Section 3(3) relates the partial pension to "the amount of the full monthly pension for that month", and s 2.1(1) defines that amount as "calculated in accordance with section 7", which includes the s 7(5) increase. Section 7.1(6) separately adds 10% to a partial pension increased for deferral. Either route gives 825 x 15/40 = 309.38 on the hypothetical figures. Asserted.
2. **Deferral stops counting at 70, and months abroad do not count.** Section 7.1(4)(b) and (c). Deferring to 71 gives the same 36% as to 70; ten months abroad cut a 60-month deferral to 50 (30%). Asserted.
3. **For a partial pensioner, the GIS makes up the gap to the full pension.** Section 12(5) computes `[(A - B) x C] - D/2` with A the maximum supplement plus the full pension and B the pensioner's own pension. With 20 years (375 of 750), the supplement at the same income is 375 more than for a full pensioner (1,242 against 867). The s 12(5) heading is "Guaranteed minimum income for pensioners". The 10% from 75 does not reduce the supplement, because it raises A and B alike. Both asserted.
4. **Section 12(6)(b) can give a negative monthly base income, and the Act does not say what then happens.** For a pensioner whose spouse is not a pensioner, the base income is "A/24 - B/2", B being the full pension rounded up to $4. With little joint income this is negative (0 - 376 on the hypothetical figures), and `D/2` would then add to the maximum. The encoding reads a negative base income as nil: s 12(1) and (2) take "one dollar for each full two dollars", and a negative income has none. That is a reading. Asserted (1,200, not 1,388).
5. **"1/12 of the pensioner's income ... in excess of $2,000"** (s 12.1(1)(a), s 22.1(3)) is read as one twelfth of (income - $2,000), and the couple's "1/24 of the aggregate ... in excess of $4,000" likewise. The words also bear "the amount by which one twelfth of income exceeds $2,000", which would make the top-up almost unreduced for every real pensioner. The first reading gives the first $2,000 of annual income free of the top-up reduction. Asserted.
6. **The s 2 earnings exemption ignores a self-employment loss, but the loss still lowers income.** Paragraph (b.1) adds self-employment earnings into the combined amount only "if those reduced self-employment earnings are greater than zero", while the loss is already netted in Income Tax Act income. So $6,000 of wages and a $2,000 loss give $4,000 of ITA income, a $5,500 exemption, and an income of -$1,500. Asserted. Whether a negative income then raises a benefit is the question of finding 4.
7. **When the spouse gets the Allowance, s 22(6) can raise the pensioner's supplement above the s 22(2) amount.** At a joint income of $30,000 the allowance and the s 22(2) supplement are $225 each, less than the $563 the pensioner would get under Part II, so the pensioner "may ... be paid" $563 - $225 = $338. The encoding gives that amount as the most the Act allows; the "may" is the Minister's. Asserted.
8. **The Allowance threshold is a single number, and the formulas meet at it.** At a monthly joint income equal to four-thirds of the rounded pension equivalent (1,000 on the hypothetical figures), s 22(3)(b) and (c) give the same amount, as do s 22(4)(b) and (c) for the survivor. The survivor's (c) branch reduces by half the residual income (C/2), the spouse's by a quarter (C/4). Asserted.
9. **Several duties are "forthwith" or "without delay", with no period.** Section 15(9) (report a separation or a new spouse), s 37(1) (return an overpayment), Regulations s 25(1) (notice of an absence of more than a month), and the Minister's duty under s 27.1(2) to reconsider and notify. With no `WITHIN`, those obligations never become a breach by time alone; a trace 400 days on is still pending. Asserted by `#TRACE`. Regulations s 25(1)'s "within one month of his return" is taken as 30 days, and Regulations s 26.1's "six months" as 182 days: readings.
10. **A request for reconsideration is a permission with a 90-day window that the Minister can extend** (s 27.1(1), "or within any longer period that the Minister may ... allow"). The rule encodes the 90 days; an extension would be a different window, not asked.
11. **"Income" for a calendar year after June 2020 has no (a)(i) amount.** Subparagraph (a)(i) gives a deduction only for months before July 2020; paragraph (b.1) replaces it. The encoding answers only for current months and so applies (b.1) only.

## Before relying on it

- Deposit an official table of the quarterly indexed amounts (ESDC publishes them), and encode it as a dated table so the amount questions need no figures from the user.
- An independent test pass, by someone who has not seen the encoding, against ESDC's published GIS and Allowance tables.
- Encode the commencement and retroactivity rules (ss 8, 11(7)(a), 23; Regulations ss 10-12), the waiver of applications, and s 14(2)-(7) estimated income, which decide the months a person is actually paid.
- Settle findings 4 and 5 against ESDC practice or a decision of the Social Security Tribunal.
- Social security agreements (s 40) for people with under 10 years' residence.
