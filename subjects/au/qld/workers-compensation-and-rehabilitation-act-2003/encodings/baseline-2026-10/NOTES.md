# Workers' Compensation and Rehabilitation Act 2003 (Qld): baseline encoding for the injured worker and the insurer

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A day with no deposited QOTE (any day after 30 June 2027, or an earlier year whose QOTE is not given) answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in three layers:

- **`wcra-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms: "the worker", "the claimant", "the employer", "the insurer" (WorkCover Queensland or a self-insurer), "a dependant". Computations (QOTE, NWE, the weekly amounts, the lump sums, the death benefits, the caring allowance) are functions. Where the text says "must", "may", "must not" or sets a deadline, there is a regulative rule (`DEONTIC`): 13 in all (ss 131, 132AA, 133, 134, 136, 144, 146B, 185 with 189(2), 186, 188-189, 220(3), 232, 232B).
- **`wcra-seat.l4`**, the injured worker's seat. It asks 36 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule.
- **`wcra-seat-insurer.l4`**, the insurer's seat. It asks 16 questions on the insurer's deadline and payment duties. It defines no name the worker's seat defines.

No earlier encoding of this Act existed to keep. Queensland keeps no requirement ledger and no scenario life raises this Act, so no ledger line is closed and no life event is cited.

## Edition

- **The Act:** Workers' Compensation and Rehabilitation Act 2003 (act-2003-027), the current in-force version on 22 September 2026, as deposited at `../../registers/source-bundle/act-2003-027.txt`. The jurisdiction README records it as in force from 1 January 2025 and still current on 20 October 2026. It is an older deposit, converted by an earlier tool, with no notice at its top.
- **The Regulation:** Workers' Compensation and Rehabilitation Regulation 2025 (sl-2025-0116), in force from 1 September 2025, retrieved 20 October 2026, deposited at `../../../workers-compensation-and-rehabilitation-regulation-2025/registers/source-bundle/sl-2025-0116.txt`. Used: ss 15, 105-110, 117-121, 147, 209 and schedules 3, 4 and 8.
- **The QOTE Notice:** Workers' Compensation and Rehabilitation (QOTE) Notice 2026 (sl-2026-0044), in force from 1 July 2026, retrieved 20 October 2026, deposited at `../../../workers-compensation-and-rehabilitation-qote-notice-2026/registers/source-bundle/sl-2026-0044.txt`. QOTE for 2026-27 is **$1,994.50** (s 3(1)), **2.1%** up on 2025-26 (s 3(2)).

QOTE for an earlier financial year is not deposited: the questions take it as an input, and without it they answer `not covered`. QOTE for 2027-28 does not exist yet. Three Commonwealth figures are inputs: the single pension rate (the maximum single disability support pension), the carer pension rate (the weekly maximum carer payment, Regulation s 147(2)), and, for s 154, what a pensioner may earn before the pension is reduced.

All three texts are CC BY 4.0, State of Queensland. The Act's attribution is in `SOURCE-LICENSE.md` (a copy of the subject's). The Regulation and the Notice carry their own: "Based on content from the Queensland Legislation website at 20 October 2026. For the latest information on Queensland Government legislation please go to https://www.legislation.qld.gov.au." (see each subject's `SOURCE-LICENSE.md`). No deposited text was altered.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wcra-core.l4`, `wcra-seat.l4` | `wcra-cases-worker.l4` | 208 written, 208 satisfied |
| `wcra-core.l4`, `wcra-seat-insurer.l4`, `wcra-seat.l4` | `wcra-cases-insurer.l4` | 53 written, 53 satisfied |

The 261 assertions include the core's own checks (QOTE, s 205, the date helpers, the Regulation s 117 example), every regulative rule on a trace that ends `FULFILLED`, and 15 mirror cases: the same facts asked from both seats, with answers that agree.

In addition, 14 `#TRACE`s in the worker case file carry an `-- expect:` line: 8 breaches (by the claimant, the employer, the worker and the insurer) and 6 obligations or permissions still pending. Each was read and matches its expectation.

`l4 run` on all five files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the texts, with the arithmetic in the comment above the assertion, and cross-checked in exact fractions before the run.

## Seats

**First seat: the injured worker** (the claimant, in the Act's words for chapter 3, part 5). They ask: "Am I a worker, and who is my employer?", "Is my injury covered?", "By when must I claim, and how far back will I be paid?", "By when must the insurer decide, and what if it does not?", "How much will I get each week in each period, and when does it stop?", "What lump sum does my DPI give me, and what do I give up by accepting it?", "What do my dependants get if I die?", "Can I be dismissed?". The insurer's and employer's duties are encoded as what the worker is owed and by when. The seat is an individual, so s 11(4) is met by construction (`is an individual` is fixed TRUE). The worker's own claim is not a death claim, so the death inputs of ss 131(3) and 132 are fixed FALSE in that seat (the insurer's seat asks them).

**Second seat: the insurer**, WorkCover Queensland or a self-insurer. The Act puts real deadline duties on it: decide within 20 business days (s 134(2)), give reasons on a rejection (s 134(4)), notify within 5 more business days if it has not decided (s 134(6)), start the basic weekly payment (s 146B(3), up to 300 penalty units), give the notice of assessment within 10 business days (s 185), decide on a request to reassess within 10 business days (s 186(3)), refer to rehabilitation (s 220(3), up to 1,000 penalty units for s 220(1)). It asks "By when must we ...?", "What must we pay ...?", "Must or may we waive ...?". It is not a seat for an official: the Regulator, the medical assessment tribunals and the courts get none. The employer is an actor in the core (ss 133, 144, 232B) but has no seat here.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulation 2025 (NWE, the lump sum calculation and scales, the caring allowance, the excess period, the information statement) and the QOTE Notice 2026.
- **The actors the text names.** Followed: the worker, the claimant, the employer, the insurer, the dependant.
- **A judgment handed to someone else answered conditionally.** Followed: whether employment is "a significant contributing factor" (s 32), whether a delay or deviation is "substantial" (s 36), the insurer's satisfaction for a waiver (s 131(5)-(6)), a medical assessment tribunal's finding (s 131(4)), the insurer's choice of instrument (s 155), its s 148 deduction, its s 109 "fair" NWE (Regulation), what it "considers is reasonable" for partial dependants (s 201), and a reasonable excuse (ss 133, 232) are inputs.
- **The Act's own definitions worked out, borrowed terms asked.** Followed: worker (s 11, schedule 2), employer (s 30, schedule 3), injury (ss 32-36), NWE (s 106, Regulation ss 105-109), the dependency levels (Regulation schedules 4 and 8) are worked out. "Employee for PAYG withholding", "regulated worker", "personal services business determination", "approved program of work for unemployment payment", "connected with this State" (s 113(3)-(7)) are asked.
- **One case is the text's natural unit.** Followed: one worker, one injury (or event), one claim.
- **The Act's own terms, each with a plain gloss.** Followed: the core quotes the text above each rule; the seats gloss DPI, NWE, QOTE and the modified Barthel index in the `@desc`.
- **Machinery out.** Followed: premiums, self-insurance licensing, WorkCover, the Regulator, tribunals and appeals.
- **Departure (business days).** "Business day" is not defined in the Act, and the Acts Interpretation Act 1954 is not deposited. The deadlines count Monday to Friday and add one business day for each Queensland public holiday the person says falls in the period. The person states that count.

## Scope

**In:**

- s 10A with the QOTE Notice 2026 (QOTE for 2026-27; the s 10A(1)(b) floor; an earlier year's QOTE as an input)
- s 11 and schedule 2 (who is a worker, with the hard cases as facts); s 30 and schedule 3 (employer); s 109 (who pays)
- ss 32-36 (injury; at work, recess, journeys and their exclusions); s 113(1) as a single fact
- s 106 with Regulation ss 105-109 (normal weekly earnings)
- ss 108, 119 (entitlement; it ends when damages are settled or judged)
- s 131 (6 months to lodge; back-payment limited to 20 business days before lodgement; the insurer's mandatory and discretionary waivers); s 132 with Regulation s 110; s 132AA with Regulation s 209; s 133; s 134; s 136; s 141
- s 140 (the maximum, 216.15 times QOTE for weekly payments and for lump sums); s 144 (day of injury); s 144A (when weekly payments stop, including at 5 years); s 146B with Regulation s 15 (the basic weekly payment; the excess period)
- ss 147, 148, 150-155 (total incapacity, all three periods); s 163 with s 162 (partial incapacity: the cap and LE only, see finding 1)
- ss 168-170 (s 169 and s 170 encoded; s 168 is a pointer); ss 171-174, 176 (redemption)
- ss 178-181 with Regulation s 117 (lump sum by DPI); ss 185-190 (notice of assessment; disagreement; offer; the decision windows for a DPI of 20% or more and under 20%), with ss 237(3) and 239 for what accepting gives up
- ss 192, 193 with Regulation ss 118, 119, 121 and schedules 3 and 4 (additional lump sums for a DPI of 30% or more and for gratuitous care)
- ss 194-201A (death: total and partial dependency in QOTE multiples, weekly amounts, s 201A; s 199 medical and funeral expenses as a pointer, being reasonable expenses with no formula)
- s 205 (automatic variation and the $5 rounding)
- ss 224-225 with Regulation s 147 and schedule 8 (caring allowance)
- s 220(3)-(4) (referral to rehabilitation); ss 231, 232 (mitigation and participation); s 232B (no dismissal for the injury within 12 months)

**Out:**

- premiums, employer insurance and self-insurance (chapter 2), except s 109 and the excess period amount
- the volunteers, community service workers, students and eligible persons of chapter 1, part 4, division 3 (asked only as the schedule 2, part 1, item 7 exclusion), and ss 156-159, 164-166
- the industrial deafness, terminal latent onset injury and pneumoconiosis divisions (chapter 3, part 3), except the s 194(2) not-covered value; s 193A (the 2013-2015 additional lump sum) and Regulation schedule 5
- chapter 4 (medical treatment, hospitalisation and travel), except as s 144B is mentioned in finding 12
- chapter 4A (serious personal injuries) and the National Injury Insurance Scheme
- the chapter 5 common law damages procedure, beyond what accepting a lump sum gives up (ss 237(3), 239)
- reviews and appeals (chapters 11-13), beyond a pointer: the s 134(6) and s 220(6) review rights
- s 202 (workers under 21 with a surviving parent), s 204 (a dependant who dies before payment), ss 232C-232D (replacement worker, reinstatement)
- the employer's rehabilitation duties (ss 226-229) and the insurer's plan (s 221)

The task brief described the s 151 first-period floor as a Regulation figure. The deposited s 151(1)(a)(ii) says "80% of QOTE", a statutory figure, and that is what is encoded.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code:

- **Social Security Act 1991** (`../../../../social-security-act-1991/`). Weekly compensation is "compensation" for the compensation preclusion and the income tests of Part 3.14 of that Act. The **single pension rate** (schedule 6 of this Act: "the maximum single disability support pension payable from time to time under a Commonwealth law") is an input to s 150(1)(c)(ii), 151(1)(c)(ii) and 152(1)(c)(ii); see finding 13. The **carer pension rate** (Regulation s 147(2): "the weekly amount of the maximum carer payment") is an input to the caring allowance. Under s 154, what a pensioner "is entitled to earn before the maximum pension payable to the worker is reduced" comes from that Act's income test. Schedule 2, part 2, item 5 refers to its ss 601 and 606 (approved programs of work for unemployment payment).
- **Income Tax Assessment Act 1997** (`../../../../income-tax-assessment-act-1997/`). Weekly compensation is assessable income. Schedule 2, part 2, item 6 turns on a personal services business determination under its s 87-60.
- **Taxation Administration Act 1953** (`../../../../taxation-administration-act-1953/`). Section 11(1)(a) turns on being "an employee for the purpose of assessment of PAYG withholding under ... schedule 1, chapter 2, part 2-5".
- **Fair Work Act 2009** (`../../../../fair-work-act-2009/`). Section 11(1)(b) and schedule 3, item 9 turn on chapter 3A (regulated workers and regulated businesses); see finding 3.

## What the Act turns out to say

1. **The partial incapacity formula did not survive conversion.** Section 163(2) reads "The weekly payment is an amount calculated under the following formula--", and the deposited text goes straight on to (3). Section 166(2) has the same gap. The encoding gives what survives: LE and MC (s 162), and the cap, "the amount must not be more than MC" (s 163(3)). The partial incapacity question answers "at most $X a week", and says the formula is missing. A `act-2003-027.formulas.md` sidecar, transcribed from the authorised PDF, would close it. Asserted.
2. **Schedule 2, part 1, item 3(b) is disjunctive.** A contractor whose work is not part of their own regular trade is a worker if they "(i) do not sublet the contract; or (ii) do not employ a worker; or (iii) if the contractor employs a worker, perform part of the work personally". So a contractor who sublets but employs no one is still a worker. The only contractor left out is one who sublets, employs a worker and does none of the work personally. Asserted.
3. **Section 11(1)(b) does nothing yet.** A regulated worker under chapter 3A of the Fair Work Act 2009 is a worker only if "prescribed by regulation to be a worker". The deposited Regulation 2025 prescribes no one, and schedule 3, item 9 is likewise empty. A delivery rider covered by a minimum standards order but not a PAYG employee is not a worker. Asserted.
4. **Amounts stated as "times QOTE" are rounded up to the nearest $5 (a reading of s 205).** Section 205(1) varies "each payment or amount ... that is not expressed as a percentage of QOTE", and a multiple such as "216.15 times QOTE" is not a percentage. Section 205(2) rounds the varied amount "up to the nearest $5". Regulation s 117's example, "The maximum statutory compensation is $422,295", is such a rounded figure: 216.15 × $1,953.70 = $422,292.26.
   - For 2026-27 the encoding therefore takes the maximum as **$431,115**, not $431,111.18. The other multiples are rounded the same way: the s 200(2)(a) death benefit is $807,515, and the schedule 3 and 4 amounts are rounded too.
   - Amounts stated as a percentage of QOTE (70%, 80%, 55%, 8%, 10%, 7%) are not rounded. Neither is s 174, whose part 9 is not in s 205's list.
   - If $1,953.70 was QOTE for 2025-26 (it is not deposited), the rise to $1,994.50 is 2.09%. That matches the Notice's "2.1%" only at one decimal place, although s 10A(3) allows rounding "to the nearest second decimal place". This is not checked.

   Asserted: weekly payments of $431,112 have not reached the maximum.
5. **Low earners keep their full NWE, and the 70%-of-QOTE floor is capped away.**
   - Under s 151 (no industrial instrument), the first-26-week floor of 80% of QOTE ($1,595.60) is more than 85% of NWE for any NWE below $1,877.18, and s 151(2) caps every period at NWE. A casual cleaner on $1,000 a week gets $1,000, all of her NWE, for 26 weeks and on to 2 years. Asserted.
   - Under s 150, the second period's floor of 70% of QOTE ($1,396.15) is capped by s 150(2) at the first-period amount. A storeperson on NWE $1,450 under an award paying $1,180 gets $1,232.50 (85% of NWE) in week 30 as in week 1: the step down to 75% never comes. Asserted.
6. **NWE has rules for what counts, not for how to average.** Section 106 and Regulation ss 105-109 say which earnings count and what to do when they cannot be worked out. They do not say how 12 months of earnings become a weekly figure. READING: the counted earnings divided by the weeks of employment in the period, at most 52.
7. **Two different clocks for the 5 years.** The rates in ss 150-152 change with "the first 26 weeks", "the first 2 years" and "the first 5 years" of the incapacity. Section 144A(1)(b) stops payments when the worker "has received weekly payments for the incapacity for 5 years". For intermittent incapacity these differ. READING: weeks of incapacity 1-26, 27-104 and 105-260, and 260 weeks of payments received, with a year of 52 weeks.
8. **Missing the 20-business-day decision is not a terminal breach.** The Act's response to a late decision under s 134(2) is the s 134(6) duty to give reasons and to say the claimant may seek a review. The regulative rule has that notice as its `LEST`, so a late decision followed by a timely s 134(6) notice ends `FULFILLED`: the s 134(2) failure is the path taken. Section 134(3) sets no time for telling the claimant the decision. A rejection notified without reasons stays pending forever. Asserted by `#TRACE`.
9. **Several duties have no deadline, so time alone never breaches them.** They are:
   - the information statements, "as soon as practicable" (s 132AA, 50 penalty units);
   - the employer's payment for the day of injury (s 144);
   - payment of an accepted lump sum (ss 188(4), 189(5));
   - the referral to a medical assessment tribunal (s 186(6));
   - the referral to rehabilitation (s 220(3)).

   Each is a regulative rule without `WITHIN`. Asserted by `#TRACE` for s 132AA, s 144 and s 188(4).
10. **"Immediately", but only an offence after 8 business days.** Section 133(2) requires the employer to report "immediately". The offence in s 133(3) arises only if the report is not given "within 8 business days ... unless the employer has a reasonable excuse". The rule uses the 8 days. With a reasonable excuse, the report is still owed but there is no breach. Asserted.
11. **Weekly payments end with the lump sum decision, accepted or not.** Under s 190(2), once a notice of assessment is given, the worker "is not entitled to further compensation for the injury" after the decision is notified or 20 business days pass. Lump sums, additional lump sums and chapter 4A are excepted (s 190(3)). Deferring the offer does not keep weekly payments going. Asserted.
12. **Reaching 5 years or the maximum ends everything.** Section 144A(2): "the worker's entitlement to further compensation for the injury stops". Read literally, that includes medical treatment, which is compensation under chapter 4 (s 9). Section 144B gives medical treatment its own stopping rule: weekly payments stopped *and* no further treatment needed. The encoding follows s 144A for weekly payments and does not resolve the tension for chapter 4, which is out of scope.
13. **"Single pension rate" does not say weekly.** It is "the amount of the maximum single disability support pension payable from time to time". That pension is paid fortnightly, and ss 150-152 pay an amount "equal to the single pension rate" "for each week". The Regulation's carer pension rate is expressly "the weekly amount". READING: the weekly equivalent. The input asks for it.
14. **An injury at work still needs employment as a significant contributing factor.** Section 34(1)(a) and (b) deem an injury at or away from the workplace to arise in the course of employment. But s 32(2) waives the significant-contributing-factor test only where "section 34(2) or 35(2) applies", that is, for a recess (s 34(1)(c)) or a journey (s 35). An injury lifting stock at work is not compensable if employment is not a significant contributing factor, while a lunch-break or journey injury is. Asserted.
15. **Schedule 2, part 2 overrides PAYG.** A director employed by their own company under a contract of service and paid through PAYG meets s 11(1)(a). But schedule 2, part 2, item 1 says such a person "is not a worker", and s 11(3) says "However". Asserted.
16. **The Act rarely says which year's QOTE applies.** Section 180(3) fixes the lump sum "as at the day the insurer makes an offer". For the weekly rates and the death benefits the Act says only "QOTE". READING: the QOTE of the financial year containing the week of payment, the day of the offer, or the day of death. Section 206 suggests amounts follow later variations, which this encoding does not model.

## Before relying on it

- An independent test pass, and a check of every figure against the authorised PDFs.
- Transcribe ss 163(2) and 166(2) from the authorised PDF into an `act-2003-027.formulas.md` sidecar (finding 1), and encode the partial incapacity amount.
- Deposit QOTE for 2025-26 and earlier (the 2025 Notice, SL No. 52, repealed by the 2026 Notice) and each later Notice as it is made. The earlier years then stop being an input, and finding 4's arithmetic can be checked.
- Deposit the Acts Interpretation Act 1954 (business day, months, "within ... after") and replace the public-holiday input and the month-end reading.
- Settle the s 205 reading in finding 4 against WorkCover's published figures, which are not deposited.
- Chapter 4 (medical treatment) and s 144B; chapter 5 (damages) beyond the election; the reviews and appeals of chapters 11-13.
- An employer seat (ss 133, 133A, 144, 146A, 226-229, 232B-232D), which the Act would support.
