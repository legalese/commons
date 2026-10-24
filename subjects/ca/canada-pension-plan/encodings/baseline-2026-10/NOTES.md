# Canada Pension Plan: baseline encoding for the contributor and the survivor

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit `not covered` value (a year or death before 2019; a survivor who also has a retirement pension), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`cpp-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the employee", "the contributor", "the survivor", "the estate", "the Minister"). Contributions and benefits are functions. Where the text says "shall" or sets a period, there is a regulative rule (`DEONTIC`): six in all.
- **`cpp-seat.l4`**, the individual's seat: 11 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings (Part I contributions; Part II retirement pension; disability pension and after a contributor's death, both marked as situations). It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed. No requirement ledger covers Canada, so no ledger line is closed.

## Edition

- **Act:** Canada Pension Plan, R.S.C., 1985, c. C-8, Justice Laws consolidation **current to 2026-09-30**, last amended 2024-12-17, deposited at `../../registers/source-bundle/R.S.C.-1985-c.-C-8.txt` (from justicecanada/laws-lois-xml commit `0507465393c2`).
- **Regulations:** Canada Pension Plan Regulations, C.R.C., c. 385, same consolidation, last amended 2026-01-01, at `../../registers/source-bundle/C.R.C.-c.-385.txt`. Used for the adjustment factors (ss 78.3, 78.4), cancellation (s 46.2), return to work (s 70.1) and reinstatement (s 71).
- **Figures.** The rates are the Act's Schedules 1 and 2, written in, from 2019 (an earlier year answers `not covered`). The Year's Basic Exemption is the Act's $3,500 (s 20(2)). The **Year's Additional Maximum Pensionable Earnings is computed** from the YMPE (s 18.1). The **Year's Maximum Pensionable Earnings is an input**: s 18 sets it each year from Statistics Canada's wage measure, and no publication of it is deposited. The flat rate benefits (ss 56(2), 58(1.1)) are indexed to the Pension Index and are inputs. The contributor's average, first additional and second additional monthly pensionable earnings (ss 48-53) are inputs, as on the Statement of Contributions: they depend on a lifetime Record of Earnings (s 95) and the drop-out rules. The case file uses **hypothetical** values and says so.

Unofficial reproduction; not an official version. Contains information licensed under the Open Government Licence - Canada.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cpp-core.l4`, `cpp-seat.l4` | `cpp-cases-contributor.l4` | 73 written, 73 satisfied |

In addition, 3 `#TRACE`s carry an `-- expect:` line: two breaches by the contributor and one obligation of the Minister still pending. Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The individual**: the worker or self-employed person who contributes, the contributor who claims a retirement or disability pension, and the survivor of a contributor (who also asks about the death benefit paid to the estate). They ask: "How much must I contribute this year?", "Can I get a retirement pension, from when, and how much if I start early or late?", "Can I get a disability pension, how much, and from when?", "Am I the survivor, and how much is the survivor's pension?", "How much is the death benefit?".

Part I's collection duties fall on the employer (s 21: deduct and remit) and on the Minister of National Revenue. The employer is not given a seat here; a later `cpp-seat-employer.l4` could ask the employer's questions from the same core. The Minister's duties under Part II are encoded for what they mean to the person: the reconsideration they may ask for and the Minister's duty to decide it with reasons.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers**: the Regulations for the adjustment factor. The YMPE and the indexed flat rates are not in a deposited instrument and are inputs.
- **The actors the text names:** the contributor or beneficiary and the Minister.
- **Judgments left to others are answered conditionally, as inputs:** "determined in prescribed manner to have a severe and prolonged ... disability" (s 42(2)(a)), asked as two facts; the Minister being "informed and satisfied" of a conviction (s 44.1).
- **The Act's own definitions are worked out from facts:** "contributor", "survivor" (s 42(1)), maximum pensionable and contributory earnings, basic exemption, minimum qualifying periods (s 44(2), (3)), the adjustment factor, the s 48(4) drop-out count, the commencement month. Borrowed terms are asked as facts: income from pensionable employment and self-employed earnings under the Income Tax Act, residence for the Income Tax Act.
- **One case:** one contributor and one year (contributions) or one benefit.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Investment Board and the Canada Pension Plan Account, assessments and appeals under Part I, rulings, administration (Part III), agreements with provinces and other countries, offences, the Chief Actuary's reviews (s 113.1).

## Scope

**In:**

- Part I: ss 8(1)-(1.2) and 10(1)-(1.2) (base, first additional and second additional contributions, employee and self-employed), ss 11.1(2), 11.2 and Schedules 1-2, ss 12(1)(d), 16, 17(a), 17.1(a), 18.1, 19(a), 20(2)
- Part II: s 2 "contributor", s 42(1) "survivor", s 42(2)(a)-(b), s 44(1)(a)-(d), (2)(a), (3), ss 44.1(1)(a), 44.2, s 46(1), (3.1) with Regulations ss 78.3-78.4, s 48(4) (the count of months dropped), s 56(1), (3)-(4), s 57(1)(b), (1.2), s 58(1)(a.1), (b), s 67(3.1), s 69
- Duties: s 30(1), s 66(1), s 81(1)-(2); Regulations ss 46.2(1), (4), 70.1, 71(2), as regulative rules

**Out:**

- the employer's contributions (s 9) and duties (ss 21-24); overpayments and refunds (ss 38-39) except as noted in finding 3; provincial pension plans (Quebec): one employer and no provincial plan are assumed
- the elections to stop contributing after 65 (s 12(1)(c)(ii), ss 17(b)-(c), 19(b)-(d)) and the religious-sect election (s 11)
- computing average monthly pensionable earnings from a record (ss 48-53, the child-rearing drop-out, the Maximum Pensionable Earnings Average adjustment): inputs
- divisions of pensionable earnings and pension sharing (ss 55-55.3, 65.1); s 46(2), (4)-(6)
- the survivor's pension combined with a retirement or disability pension (s 58(2), (6)), the post-retirement benefit (s 59.1) and post-retirement disability benefit (s 59.2), children's and orphan's benefits (ss 59, 74-76)
- the annual indexation of benefits (s 45(2), s 43), and retirement pensions starting before 2016 (other factors in Regulations s 78.3)
- the s 57(1)(a) death benefit for deaths before 2019; s 44.1(1)(b)-(c) (the death benefit or orphan's benefit to a person convicted)
- the recovery of debts, penalties, offences (ss 66(2)-(4), 90-90.2)

## Read with the Income Tax Act encoding

`../../../income-tax-act/encodings/baseline-2026-10/` (being encoded on 2026-10-24 by another session) answers this encoding's borrowed terms and uses its answers:

- **Contributory salary and wages** (s 12(1)) is "income for the year from pensionable employment, computed in accordance with the Income Tax Act"; **self-employed earnings** (s 14) are business income under that Act.
- **The filing date** of the return of self-employed earnings (s 30(1)) is that of the return of income under ITA Part I (s 150).
- **CPP contributions** give the employee a credit (ITA s 118.7) and the enhanced (first and second additional) contributions a deduction (ITA s 60(e), (e.1)); the self-employed person deducts the employer-equivalent half of the base contribution (s 60(e)). CPP benefits are income under ITA s 56(1)(a)(i).

Also read with `../../../old-age-security-act/encodings/baseline-2026-10/`: CPP benefits are income for the GIS (OAS Act s 2), while CPP contributions are deducted from it and a CPP death benefit is excluded. The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

## What the Act turns out to say

1. **The Year's Additional Maximum Pensionable Earnings is fixed by the Act from the YMPE.** Section 18.1 gives 1.07 times the YMPE for 2024 and 1.14 times from 2025, rounded down to $100: 68,500 gives 73,200 and 71,300 gives 81,200. So only one annual figure, the YMPE, needs publishing. Asserted.
2. **The contributions are three bands.** The base and first additional contributions are on earnings between the $3,500 exemption and the YMPE (ss 8(1), (1.1)); the second additional contribution is on earnings between the YMPE and the YAMPE, with no exemption (s 8(1.2)). For a self-employed person each rate is doubled (Schedules 1 and 2). Asserted.
3. **On the words of s 10(1.2), a person with both wages and self-employed earnings can pay no second additional contribution though their combined earnings exceed the YMPE.** Section 10(1.2) compares "the individual's contributory self-employed earnings" alone (not exceeding the YAMPE) with the maximum pensionable earnings, and only then subtracts wages on which a second additional contribution was made. With $70,000 of wages and $10,000 of self-employed earnings (YMPE $70,000), neither s 8(1.2) nor s 10(1.2) reaches the $10,000 above the YMPE. By contrast s 8(2)(a.2), on overpayments, combines salary and self-employed earnings. The encoding follows s 10(1.2) as written. Whether CRA practice combines them is not in the deposited text. Asserted.
4. **Starting late helps only to 70, and starting at 60 costs 36%.** Regulations ss 78.3 and 78.4 count at most 60 months each way (and s 46(7) says the interval "is deemed never to exceed five years"): 0.6% a month before 65 (64% of the pension at 60), 0.7% a month after (142% at 70). A pension starting at 75 gets the same 42% as at 70. Asserted.
5. **A pension applied for after 65 is paid back at most 11 months, and never before 65.** Section 67(3.1)(c). Applying at 66 years 8 months gives a pension from 65 years 9 months, and the adjustment factor is the one for that month. Asserted.
6. **A survivor under 65 now gets the survivor's pension whatever their age or family, and with no age reduction.** For months after 2018, s 44(1)(d)(ii) pays the survivor of any contributor who met the minimum qualifying period, and s 58(1)(a.1) drops the 1/120-a-month reduction for survivors under 45 that s 58(1)(a) still carries for earlier months. A 30-year-old gets the flat rate plus 37.5%. Asserted.
7. **A common-law partner displaces a married spouse.** Under s 42(1), a married person is the survivor only "if there is no person described in paragraph (b)", the common-law partner at death. Asserted.
8. **The death benefit doubles only where nobody else benefits.** Section 57(1.2) pays $5,000 for a death after 2024 only if the contributor never received a retirement or disability pension and no survivor's pension is payable; otherwise $2,500 (s 57(1)(b)). Asserted.
9. **The minimum qualifying period for survivor's and death benefits has a floor of three years.** Section 44(3)(a): one third of the contributory period, "but in no case for less than three years"; or (b) ten years. Two years of a six-year period is a third but not enough. Asserted.
10. **A disability pension can be paid back at most 11 months before the application.** The person is never "deemed to have become disabled earlier than fifteen months before" the application (s 42(2)(b)), and payment starts "with the fourth month following" that month (s 69). With a disability pension in the previous five years the figures are twelve months and the next month, again 11. Asserted.
11. **The disability pension carries no early-retirement reduction.** Section 56(1)(b) takes 75% of the retirement pension computed under s 56(3)-(3.2), 25% of average monthly pensionable earnings to the month of disability (at least 48 months, s 56(4)) plus the additional portions, with no adjustment factor. Asserted.
12. **Several duties have no period.** Section 66(1) ("forthwith"), Regulations s 70.1 ("without delay") and the Minister's duty to reconsider (s 81(2), "without delay") have no `WITHIN`; a trace stays pending. The 12 months of Regulations ss 46.2 and 71(2) are taken as 365 days, though s 46.2(4) runs to the end of the twelfth month after the month of the grant: readings.

## Before relying on it

- Deposit the official YMPE and flat-rate figures for the year (ESDC and CRA publish them) and encode them as dated tables.
- Encode the employer's seat (ss 9, 21) from the same core, with mirror cases.
- Encode the computation of average monthly pensionable earnings from a year-by-year record (ss 48-53), and s 58(2) for survivors with their own retirement pension, which most survivors over 65 are.
- An independent test pass against CRA's payroll tables and ESDC's benefit statements; and a ruling or CRA practice on finding 3.
