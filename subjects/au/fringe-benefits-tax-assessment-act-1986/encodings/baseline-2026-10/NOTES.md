# Fringe Benefits Tax Assessment Act 1986 — employee and employer baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18, and an employer seat layer under the ruling of 21 October 2026 on more than one seat.
There is no REFUSE in it; a question that reaches a gap answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0075` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

## Edition

**Compilation No. 97**, compilation date 1 July 2026, includes amendments up to Act No. 49, 2026 (register id C2026C00332, two volumes), as deposited at `../../registers/source-bundle/C2004A03280.txt`.

**Formulas.** The formulas in ss 5B(1B), 5B(1C), 9(1) and 135P(2) were equation images the text deposit dropped. They are transcribed, with the image hashes and the words drawn in each, in the new sidecar `../../registers/source-bundle/C2004A03280.formulas.md`, from the authorised Word rendering of the same compilation (both volumes fetched from the Federal Register of Legislation API on 2026-10-23, two requests). The deposit itself is unchanged.

**Brought in:** the rate of tax from the Fringe Benefits Tax Act 1986, Compilation No. 9, compilation date 19 June 2018, deposited at `../../../fringe-benefits-tax-act-1986/registers/source-bundle/C2004A03281.txt`: 47% (s 6), 49% for the years of tax starting 1 April 2015 and 2016 (s 6A). Same CC BY 4.0 terms (that subject's `SOURCE-LICENSE.md`).

**Inputs, not deposited:** the benchmark interest rate (the Reserve Bank's published rate, s 136(1); REQ-0110 asks for it); the GST rate (the GST Act's); the employer's type 1 and type 2 aggregate amounts.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `fbtaa-employee.l4` (employee, 9 questions) | `fbtaa-cases-employee.l4` | 42 written, 42 satisfied |
| `fbtaa-seat-employer.l4` (employer, 7 questions) | `fbtaa-cases-employer.l4` | 20 written, 20 satisfied (13 in the mirror section, 10 of them five pairs asked from both seats) |
| `fbtaa-formulas.l4` (24 October 2026: s 135Q, the s 10 cost basis; 6 employee and 2 employer questions) | `fbtaa-cases-formulas.l4` | 22 written, 22 satisfied |

`l4 run` on all six files: 0 errors, 0 warnings (2026-10-23; 2026-10-24 with `fbtaa-formulas.l4`, 84 assertions in all). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text and the sidecar.

## Seats

**The employee receiving a benefit** (`fbtaa-employee.l4`), first and required. The questions are the employee's: "Is this a fringe benefit?", "Is my electric car exempt?", "Is my work phone or laptop exempt?", "Is this small gift exempt?", "Is my loan exempt?", "What is the taxable value of my car, or my loan?", "What is my reportable fringe benefits amount, and my total?". The tax falls on the employer (s 66), but the employee meets the Act through the exemptions, the taxable values and above all the reportable fringe benefits amount, which shows on the income statement and feeds the income tests in other Acts.

**The employer** (`fbtaa-seat-employer.l4`), a second seat, because the text puts the tax and the return on the employer. Its own questions are the fringe benefits taxable amount (s 5B), the tax (s 66 and the rates Act) and the due date (ss 68, 90). Its other questions mirror the employee's, calling the same rules: the car's and the loan's taxable values, the electric car exemption, and the reportable amount. Every name in the layer begins "As the employer, ".

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** Followed: the rate comes from the deposited rates Act. The benchmark interest rate is an RBA figure, not an instrument; it is an input. Departure: none.
- **The actors the text names:** the employee and associate, the employer and associate, the arranger, the provider, the Commissioner.
- **Judgments handed to others are answered conditionally:** whether it would be "unreasonable" to treat a minor benefit as a fringe benefit (s 58P(1)(f)); whether an item is "primarily for use in the employee's employment" (s 58X(2)).
- **The Act's own definitions are worked out from facts:** fringe benefit (s 136(1), in outline), zero or low emissions vehicle (s 8A(2)–(4)), eligible work related item (s 58X(2)), base value of a car (s 9(2)(a)), notional amount of interest (s 136(1)), year of tax (s 136(1)), reportable fringe benefits amount (s 135P). Borrowed terms (associate, salary or wages, employee share scheme, complying superannuation fund, luxury car tax, GST-creditable benefit) are asked as facts.
- **One case:** one benefit, one employee, one employer, one year of tax.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** assessments, objections, collection, instalments, record keeping, administration.

## Scope

**In:** s 5B(1A)–(1C), (3) (employer); s 5C(3)–(4) only as the employer's two totals; s 5E(2)–(3) (as the employee's input); ss 8A, 9(1)–(2), 16 (as the benefit), 17(1), (3), 18(1), 58P(1), 58X, 66(1), 68, 90, 135N, 135P, 136(1) (fringe benefit, benchmark and statutory interest rate, notional amount of interest, year of tax); Fringe Benefits Tax Act 1986 ss 6, 6A.

**Added 24 October 2026** (`fbtaa-formulas.l4`, from the formulas recovered into the sidecar that day):

- **s 135Q.** `My reportable fringe benefits amount` answers `not covered` for an employee of a s 57A or s 58 employer, and still does. The new `My reportable fringe benefits amount from a s 57A or s 58 employer` computes it under s 135Q(2) to (4): (individual fringe benefits amount + individual quasi-fringe benefits amount) × 1 / (1 − rate of tax), if the sum is more than $2,000. `My reportable fringe benefits amount, any employer` routes between ss 135P and 135Q.
- **The cost basis for cars.** This is s 10(2) and (3)(a), with the deemed depreciation and interest of an owned car (s 11(1A), (1), (1AA), (1B), (2)), the depreciated value (s 12(1)) and the business use percentage (s 136(1)). Section 10(5) is encoded too: a cost basis value above the s 9 value gives way to the s 9 value, which comes from `The taxable value of my car`.

**Inputs these formulas still need:**

- the statutory interest rate (REQ-0110);
- the Income Tax Assessment Act 1997 diminishing value percentage (200%, its s 40-72) and the Commissioner's effective life;
- the car expenses and lease charges.

The seat question takes the holding period to be all the days the car was owned in the year.

**Out:** the other kinds of benefit and their valuation (debt waiver, expense payment, housing, living-away-from-home, board, meal entertainment, tax-exempt body entertainment, car parking, property, residual); s 8 and s 10 (other exempt cars; the cost basis); ss 11–13; s 17(2), (4); the otherwise deductible rules (ss 19, 24, 37, 44, 52); exemptions other than ss 8A, 17(1), (3), 58P and 58X; reductions (ss 59–65CC); s 65J rebate; s 5B(1D)–(1M) (s 57A employers); s 135G; s 135Q (`not covered`); years of tax before 1 April 2015 (`not covered`: the rates Act compilation deposited does not give earlier rates); Parts IV onwards except ss 66, 68, 90.

## What the Act turns out to say

1. **The employee never pays FBT, but carries its number.** Tax "is payable by the employer" (s 66(1)). What reaches the employee is the reportable fringe benefits amount: the individual fringe benefits amount grossed up by 1/(1 − rate of tax), reported only where that amount is more than $2,000 (s 135P(1)–(2)), summed across employers (s 135N). At 47%, $5,300 of benefits reports as $10,000. Asserted.
2. **An exempt electric car still shows on the income statement.** Section 8A exempts a battery electric or hydrogen fuel cell car on which no luxury car tax was payable, but s 135P(3) says to "disregard section 8A" when working out the reportable amount. The deposited text has no plug-in hybrid exemption: a car with an internal combustion engine is neither kind of zero or low emissions vehicle (s 8A(3)–(4)). Asserted.
3. **The gross-up formulas.** The fringe benefits taxable amount is Type 1 × (FBT rate + GST rate) / ((1 − FBT rate) × (1 + GST rate) × FBT rate) plus Type 2 × 1/(1 − FBT rate) (s 5B(1B)–(1C), from the sidecar). At 47% and 10% the exact type 1 factor is 0.57/0.27401 = 2.08022…; the Act prescribes no rounding of the factor. The type 2 factor is 1/0.53 = 1.88679…. The cases use amounts that gross up to whole dollars. Asserted.
4. **A car's statutory formula value can come out negative on the text; this encoding stops it at nil.** Section 9(1) is (base value × 0.2 × days provided / days in the year) − the recipient's payment, with no "(if any)" or floor, unlike s 18 ("the amount (if any) by which"). A recipient's payment above the first term is read here as reducing the taxable value to nil, not below. Interpretive. Asserted.
5. **The loan's notional interest is computed on a constant daily balance at 1/365 of the annual rate.** Section 136(1) says "calculated on the daily balance of the loan", at the benchmark rate (the RBA's large bank housing lenders variable owner-occupier rate last published before 1 April). This encoding takes the balance as constant and a day's interest as 1/365 of a year's; a leap year or a changing balance is not modelled. Interpretive. Asserted.
6. **The base value drops by a third only after a car has been held for more than four years at the start of the FBT year.** "in a case where the commencement of the year of tax is later than the fourth anniversary of the earliest holding time—⅔" (s 9(2)(a)); a car first held on 1 April 2022 still has its full value for the year starting 1 April 2026. Asserted.
7. **Minor benefits under $300 are exempt only if it would be unreasonable to treat them as fringe benefits.** Section 58P(1)(e) is a bright line ("less than $300"), but (f) is a judgment on frequency, total value, difficulty and circumstances, and in-house expense, property and residual benefits are outside it (s 58P(1)(c)). Asserted, with the judgment as an input.
8. **Work items are exempt only outside salary packaging.** A phone, laptop, software, protective clothing, briefcase or tool of trade is exempt if primarily for use in the employment and "not provided to the employee under a salary packaging arrangement" (s 58X(2)). Asserted.
9. **The return and the tax are due on the same day.** 21 May after the FBT year ends (ss 68, 90), unless the Commissioner allows a later date for the return. Asserted.
10. **The 2018 rates Act still gives 47%.** Fringe Benefits Tax Act 1986 s 6 at Compilation No. 9 (19 June 2018); whether a later amendment changed the rate is not known from the deposit, whose compilation is older than the Assessment Act's. Not asserted.

11. **Under the cost basis, the employee's payment can only lower the value to nil.** Section 10(2) is (C × (100% − BP)) − R, again with no floor. This encoding reads it as it reads s 9 (finding 4): nil, not below. Section 10(5) then caps the cost basis at the s 9 value. On the cases' car ($40,000, a $16,500 operating cost, 30% business use, $1,000 paid), the cost basis gives $10,550 and the statutory formula $7,000, so $7,000 applies. At 80% business use the cost basis gives $2,300, which applies. Asserted.

## What would need doing before this is worth relying on

- **The benchmark interest rate** for each FBT year (REQ-0110).
- **A current compilation of the Fringe Benefits Tax Act 1986**, to confirm the 47% rate (finding 10), and earlier rates for years before 2015.
- **The other benefit types** and the otherwise deductible rules (the cost basis for cars was added on 24 October 2026; the housing (s 26), car parking (ss 39DA to 39GB), otherwise deductible (ss 19, 24, 37, 44, 52), long service award (s 58Q), rebate (s 65J) and instalment (ss 111, 112B) formulas are in the sidecar, not yet encoded) — the bulk of the Act, left out by design.
- **s 135Q and s 57A** for employees of charities, hospitals and ambulance services.
- **ATO rulings and case law** were not read; findings 4 and 5 are interpretive.
