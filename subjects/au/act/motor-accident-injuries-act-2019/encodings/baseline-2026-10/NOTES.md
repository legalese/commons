# Motor Accident Injuries Act 2019 (ACT): baseline encoding for the injured person and the relevant insurer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A day with no deposited AWE indexed amount, a WPI that is not a whole number, or a work situation for which s 101 gives no start date answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in three layers:

- **`mai-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms: the person injured in a motor accident, the dependant, the person who has paid or is liable to pay the funeral expenses, the applicant, the relevant insurer. Computations (the income replacement formula, the payment periods, the period payable, table 167, the death and funeral amounts, every deadline) are functions. Where the text says "must" or "may" or sets a deadline, there is a regulative rule (`DEONTIC`): seven in all (ss 59, 60, 65, 66, 102, 154-157 and 176).
- **`mai-seat.l4`**, the individual's seat. It asks 28 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings: applying, income replacement, treatment and care, quality of life and suing, death benefits, funeral benefits. It builds the core's records from plain answers and restates no rule.
- **`mai-seat-insurer.l4`**, the relevant insurer's seat. It asks 15 questions, on the same core: when it must give the receipt notice and decide liability, whether it is taken to have accepted, what it must pay or offer, when it may apply to the ACAT.

No earlier encoding of this Act existed to keep. No requirement ledger covers the ACT, so no ledger line is closed. No scenario life raised the Act; every case is HYPOTHETICAL.

## Edition

- **Act:** Motor Accident Injuries Act 2019 (A2019-12), Republication No 8, effective 26 December 2025 (last amendment A2025-29), from the ACT Legislation Register, as deposited at `../../registers/source-bundle/A2019-12.txt`. The deposit is a conversion of the register's unauthorised DOCX; the authorised text is the PDF.
- **Indexed amounts:** Motor Accident Injuries (Indexation of Benefits) Declaration 2026 (No 2), NI2026-402, notified 3 September 2026, amounts applying on and from the 1 October 2026 indexation day, as deposited at `../../../motor-accident-injuries-indexation-of-benefits-declaration-2026-no-2/registers/source-bundle/NI2026-402.txt` (same licence: CC BY 4.0, © Australian Capital Territory; see that subject's `SOURCE-LICENSE.md`). It is brought in under the default "the Act alone, with the instruments that set its numbers".

The amounts are two dated tables in the core:

| Amounts | Day range in this encoding | Figures used |
|---|---|---|
| ss 96, 97, 103 (biannual, 1 April and 1 October) | 1 April 2026 to 30 September 2026 | the Declaration's "1 April 2026" column |
| | 1 October 2026 to 31 March 2027 | its "1 October 2026" column |
| ss 167, 174, 181 (annual, 1 October) | 1 April 2026 to 30 September 2026 | its "1 October 2025" column |
| | 1 October 2026 to 30 September 2027 | its "1 October 2026" column |

A day outside those ranges is `not covered`. The ranges end at the next indexation day, because the figures after it are not deposited. They begin on 1 April 2026 for every amount, as the task set. The annual comparison column would in fact cover 1 October 2025 to 31 March 2026 as well, if relied on. Both earlier columns are marked "* For information/comparison" in the Declaration, so they come from earlier declarations that are not deposited (finding 19).

Inputs, because the instrument that fixes them is not deposited:

- the period for a receipt notice (MAI guidelines, s 60);
- the interim weekly payment percentage (regulation, s 103 (3));
- pre-injury income, already AWE adjusted (ss 80-88, 94; the s 95 adjustment declarations are not deposited);
- post-injury earning capacity (the insurer's decision under s 100);
- the superannuation guarantee charge percentage (see finding 20);
- pension age, asked as the date the person reaches it (Social Security Act 1991 (Cwlth), s 23);
- ACT public holidays falling in the five business days of s 176 (Holidays Act 1958, indexed but not deposited);
- the funeral expenses that count (MAI guidelines, s 182).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mai-core.l4`, `mai-seat.l4` | `mai-cases-injured.l4` | 202 written, 202 satisfied |
| `mai-core.l4`, `mai-seat.l4`, `mai-seat-insurer.l4` | `mai-cases-insurer.l4` | 68 written, 68 satisfied |

In addition, 9 `#TRACE`s in `mai-cases-insurer.l4` carry an `-- expect:` line: five breaches by the insurer (a late receipt notice, the wrong kind of receipt notice, an ACAT application made too early, a wrong fortnightly amount, a late WPI notice) and four obligations still pending (payment after acceptance, the defined benefits notice after deemed acceptance, the ACAT application with no latest day, payment after deemed acceptance of a WPI offer). Each was read and matches its expectation.

`l4 run` on all five files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

Every expected value was written by hand from the text and the Declaration, with the arithmetic in the comment above the assertion. Dates and the arithmetic were then checked independently against a calendar with Python's `datetime`, not against the encoding.

The Declaration itself was checked against s 18 (1) (c). Every one of its 30 "1 October 2026" amounts equals the comparison-column amount times the stated factor, rounded up as s 18 (1) (c) requires:

- for the biannual amounts, the factor is 1.025, rounded up to the dollar;
- for the annual amounts, the factor is 1.031, rounded up to the whole $10.

## Seats

**The individual (first, required).** The person injured in a motor accident in the ACT; and, after a death, a dependant of the person who died, the personal representative, or the person who has paid or is liable to pay the funeral expenses. Those are the people s 55 lets apply. They ask:

- "May I apply, and by when? Is my late application taken to be accepted?"
- "Has the insurer accepted my application, or is it taken to have?"
- "Am I entitled to income replacement benefits? How much a week and a fortnight, in each payment period, and from when until when?"
- "Am I entitled to treatment and care benefits, and for what period?"
- "When may I apply for quality of life benefits? How much does my WPI give me? What must the insurer offer, and by when must I reply? Can I sue?"
- "Am I a dependant? What death benefits are payable, and when may the insurer go to the ACAT?"
- "How much funeral benefit can I be paid?"

**The relevant insurer (second).** The Act puts hard duties with deadlines on the relevant insurer (s 34: the CTP insurer of the vehicle, an interstate insurer, or the nominal defendant). Those are a genuine second seat, as the guide allows for "the insurer's customer and the insurer". The duties:

- a receipt notice within the MAI guidelines' period (s 60);
- the liability decision within 28 days after the receipt notice, failing which it is taken to accept (s 65 (4));
- a response to a late application's explanation within 28 days, failing which it is taken to accept (s 59 (4));
- payment of the defined benefits (s 66), every 14 days for income replacement benefits (s 102);
- the WPI notice and offer within 14 days (ss 154-157);
- the application to the ACAT for the death benefits order, but not before the s 176 (3) day.

The insurer's seat asks the same questions from its side. **Mirror cases** in `mai-cases-insurer.l4` assert that the two seats agree on the receipt notice and decision days, deemed acceptance, a late application, the weekly amount, the period payable, the interim payment, the WPI section, notice day and offer, the ACAT day, the most the ACAT can order, s 175, and the funeral maximum.

Officials get no seat: not the MAI commission, the ACAT or the court. Their acts (an MAI commission declaration or notice, an ACAT order, a conviction) appear only as facts or as what they mean for the person.

Where the insurer states a single fact for a group of exclusions (for example "a limitation in ss 43 to 50 ends the injured person's income replacement benefits"), the seat carries it in one field of the core's record that the rule reads, and passes FALSE for the others. Each place has a comment saying so.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed: NI2026-402. Not deposited, so not used: the MAI guidelines (DI2025-158 to -160, -308), the Motor Accident Injuries (Premiums and Administration) Regulation 2019, the 2026 Adjustment of Pre-injury Income Declarations, and earlier indexation declarations. What they would supply is an input (see Edition).
- **The actors the text names.** Followed: the injured person, the applicant, the dependant, the personal representative, the guardian, the funeral payer, the relevant insurer, the MAI commission, the ACAT, a coroner.
- **Judgments left to someone else, answered conditionally.** Followed:
  - the insurer's satisfaction with "a full and satisfactory explanation" (s 59 (2) (b)) is reported as "may accept, if satisfied";
  - "exceptional circumstances justifying earlier payment" (ss 101, 128) is an input;
  - post-injury earning capacity (s 100) is an input;
  - the ACAT's share for each dependant (s 177 (1)) is not decided: only the cap is encoded;
  - "entitled to make a motor accident claim" (ss 156, 157) is asked as whether someone else is liable in damages.
- **The Act's own definitions worked out, borrowed terms asked.** Followed. Worked out:
  - paid work and capable of being in paid work (ss 78, 79), from the person's work situation on the day of the accident;
  - the payment periods (s 93), P, N and SG (ss 96, 97);
  - the application period (s 58), the period payable (s 101), table 167 (s 167);
  - dependant (s 168), and person who died as a result of a motor accident (s 36, its 2-year limb).

  Asked as facts:
  - pension age;
  - "child" (not defined in the Act);
  - domestic partner (Legislation Act);
  - a driving offence or serious offence conviction, a detainee;
  - the LTCS scheme;
  - workers compensation acceptance;
  - "foreign national".
- **One case is the text's natural unit.** Followed: one injured person and one accident; one death; one application.
- **The Act's own terms, each glossed.** Followed: the comment above each rule quotes the provision.
- **Machinery out.** Followed: the MAI commission and its staff (pt 1.3), licensing (ch 7), premiums and the nominal defendant fund (ch 6), enforcement, information and review of commission decisions.

## Scope

**In:**

- ss 18-19, read through NI2026-402 (the dated tables);
- s 36 (b), the 2-year limb;
- ss 43-50, as facts, with which benefit each limits (from the "subject to" lists in ss 89 (3), 112 (2), 132 (2));
- s 55;
- ss 58-59, the application period and late applications, including deemed acceptance (s 59 (4)) and the limit (s 59 (5));
- s 60 (1) (a)-(b), the receipt and late receipt notice;
- s 65 (1)-(4), the liability decision and deemed acceptance; s 66 (1);
- ss 78-79 and 89-92, entitlement to income replacement benefits;
- s 93, ss 96-98, the formula with N, SG, the P cap and the workers compensation reduction;
- s 101 (2)-(5), the period payable;
- s 102, fortnightly payment (regulative);
- s 103 (2)-(3), interim weekly payments;
- ss 112 and 118, and s 128, treatment and care: entitlement and period only;
- ss 132-136 and s 137 (2), quality of life benefits: entitlement and when to apply;
- ss 154-157: which section applies, the 14-day notice, the reply period, what silence means (regulative);
- s 167 and table 167;
- s 239 (1), the WPI threshold for damages ("can I sue?");
- ss 168-177, death benefits: dependant, entitlement and exclusions, the s 174 amounts, s 175, the earliest day under s 176, the s 177 (2) cap;
- ss 178-181, funeral benefits.

**Out**, each returning nothing or a `not covered` value where a question touches it:

- treatment and care benefits beyond entitlement and period: what is "reasonable and necessary" (s 120), recovery plans (ss 122-127), the expense-specific exclusions of ss 116, 117 and 119, and allowable expenses (ss 61-64);
- the WPI assessment process: ss 137 (3)-(4) and 138-153, the excess payment of s 139, second WPI reports and final offers (ss 158-165). The WPI is a fact;
- the significant occupational impact assessment (ch 3; its result enters s 239 as a fact);
- future treatment payments (ch 4);
- common law damages and their amounts (ch 5 beyond s 239 (1));
- insurance, premiums and the nominal defendant (ch 6), and licensing (ch 7);
- how the disentitling offences are proved (ss 41-50 beyond the facts), and the s 44 (4), 45 (4) and 48 (4) declarations;
- dispute resolution (pt 2.10), and changes of decision and transfers (ss 67-70);
- the duties to give fitness for work evidence and notify changes (ss 104-106);
- notice before reducing or stopping payments (s 107);
- Australians living overseas and foreign nationals' lump sums (ss 183-184), except the s 184 (6) route in s 239 (1) (b);
- the apprentice increments of s 99 (pre-injury income is an input);
- pre-injury income itself (ss 80-88) and its AWE adjustment (s 94).

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social Security Act 1991 (Cwlth)**, `../../../../social-security-act-1991/`. The Act's "pension age" is that Act's s 23 (dictionary): it ends a pension-aged worker's income replacement benefits 2 years after the accident (s 101 (2) (b) (i)) and everyone else's 2 years after reaching pension age (s 101 (2) (b) (ii) (A); s 51 (2) (b)). The baseline there answers `What is my pension age in months`; here it is the input `the date I reach pension age`. Compensation recovery (Part 3.14) decides how MAI income replacement benefits, and a later lump sum such as a damages settlement, reduce a Commonwealth payment. Its questions `Is my payment compensation affected` and `By how much is my daily rate reduced for periodic compensation` take the MAI payments as their facts.
- **Superannuation Guarantee (Administration) Act 1992 (Cwlth)**, `../../../../superannuation-guarantee-administration-act-1992/`. Section 96 (2) takes "SG" from that Act's s 19 (2). The deposited compilation (No 78, 1 July 2026) no longer has it (finding 20). The charge percentage is an input.
- **Income Tax Assessment Act 1997 (Cwlth)**, `../../../../income-tax-assessment-act-1997/`. Income replacement benefits replace lost earnings, and compensation of that kind is ordinary income (s 6-5), which that encoding asks as a fact. Quality of life, death and funeral benefits are lump sums for injury or death. Their tax treatment is not worked out in either encoding.
- **Workers Compensation Act 1951 (ACT)**, `../../../workers-compensation-act-1951/encodings/baseline-2026-10/` (encoded by another session on 2026-10-24, at the same time as this one). Its weekly payments reduce income replacement benefits week for week (s 98). An accepted workers compensation claim ends income replacement, treatment and care and quality of life benefits (s 50). Its death and funeral payments exclude MAI death and funeral benefits (ss 173, 180). A successful workers compensation claim opens s 239 (1) (d).

## What the Act turns out to say

1. **N applies to the whole of (P − A), so the income replacement formula has cliffs.** From 1 October 2026, in the first payment period, P = $1 051 with SG 12 gives 1 051 × 1.12 = $1 177.12 a week. P = $1 052 gives 1 052 × 0.95 = $999.40: one dollar more of pre-injury income costs $177.72 a week. In the second period the cliff is at $1 279 indexed: P = $1 279 gives $1 215.05, and P = $1 280 gives $1 024.00, a drop of $191.05. The Act's own example (Kristin, s 96) sits below the first cliff. Asserted.
2. **An indexation day can move a person across a threshold.** A person with P = $1 040 in the first payment period gets $988.00 a week in September 2026 (N = 0.95, since $1 040 ≥ $1 026). On 1 October 2026 the $800 indexed threshold rises to $1 052, so N becomes 1.12 and the benefit rises to $1 164.80 with no change in the person's circumstances. Asserted.
3. **A casual worker with fewer than 260 hours in the year before has no start date and no pre-injury income rule.** Someone in casual paid work on the day of the accident is "in paid work" (s 78), so entitled (s 89). But s 83 defines a casual worker only by 260 hours in the 52 weeks before, and none of ss 81-87 defines that person's pre-injury income. Section 101 (3)-(5) gives them no start date. The encoding answers entitled, and the period and amount `not covered`. Asserted.
4. **Someone already receiving income replacement benefits for an earlier accident is in the same gap.** Section 79 (1) (b) makes a person receiving "a weekly payment ... in relation to loss of income under this Act or the Workers Compensation Act 1951" capable of being in paid work. But s 84 and s 101 (3) speak only of a person receiving workers compensation. Entitled; period `not covered`. Asserted.
5. **The Act does not say what happens when post-injury earning capacity is at least P.** (P − A) × N is then nil or negative. The encoding reads it as nil: P = $600 and A = $700 gives $0. Asserted.
6. **Read literally, s 59 (4) deems acceptance of any late application, even one past the limit.** Section 59 (4) says an insurer that does not respond to the explanation within 28 days "is taken to have accepted the application". Section 59 (5) says the insurer "need not accept an application if made after" the 2-year (or 1-year) limit. Nothing ties (4) to (2) (a). The encoding gives (5) priority: an application on 4 August 2028, for an accident on 3 August 2026, is "too late" whatever the insurer does. That is a reading. Asserted.
7. **For a late application, s 65 does not say from which notice its 28 days run.** Section 65 (1) counts 28 days "after the date of the receipt notice". For a late application, s 60 (1) (b) provides a different notice, the "late receipt notice". The encoding counts from the late receipt notice. That is a reading, traced.
8. **After indexation the bands of table 167 no longer meet.** Each AWE indexed figure is rounded separately, so the formula items no longer join at their edges.

   | WPI | Earlier item gives | Next item starts from |
   |---|---|---|
   | 10% | item 3: $8 960 + 5 × $2 720 = $22 560 | item 4: $22 360 |
   | 20% | item 4: $53 960 | item 5: $53 620 |
   | 50% | item 5: $161 620 | item 6: $160 770 |

   Moving from 10% to 11% therefore adds $2 960, not $3 160. Asserted at 10%, 11%, 20%, 21%, 50% and 51%.
9. **With separate physical and psychological reports, s 167 does not say which WPI goes into table 167.** Sections 154-157 and s 239 (3) use the higher of the two, and s 153 (2) lets the insurer "take into account" both for its offer. The encoding uses the higher one. That is a reading.
10. **Silence on the WPI notice means different things, and s 154 has no duty to pay.**
    - Under ss 154 (4), 155 (5) and 156 (5), a person who does not reply within 26 weeks is "taken to have accepted" the offer, which must then be paid (ss 155 (7) (b), 156 (7) (b)).
    - Under s 157 (6), where the person is entitled to sue, silence until the due date ends the entitlement to quality of life benefits.
    - Section 154 lets the insurer make an offer below 5%, but says nothing about paying an accepted offer (contrast ss 155 (7) (b), 156 (7) (b), 157 (5) (b)). Below 5% there is no s 132 entitlement either. The regulative rule therefore ends the s 154 path FULFILLED.

    Asserted and traced.
11. **Sections 174 and 181 do not say on which day the AWE indexed amount is taken.** Section 167 (1) fixes the quality of life amount "as at the date of the" WPI report. Sections 174 (death benefits) and 181 (the funeral maximum) give no day. The encoding asks for "the day the benefits are worked out" (for example the date of the ACAT order, or of payment).
12. **The s 177 (2) cap is read on the order as a whole.** The ACAT's order "must not be for more than an amount stated in section 174". The encoding reads the cap as the s 174 amounts added together, on the whole order. With a partner and 2 children from 1 October 2026 that is $242 400 + $102 090 = $344 490. An order of $344 491 is over it. That is a reading. Asserted.
13. **Section 174 counts dependants on a different day from s 168.** Section 174 counts the partner and dependent children "at the date of the motor accident". Section 168 defines a dependant "when the person died", including "a child born after the person's death". A child born between the accident and the death, or after it, is a dependant, but s 174 (b) does not count them. A partner whose relationship began after the accident is in the same position. The encoding follows s 174: the inputs ask about the date of the accident. Noted, not asserted.
14. **Section 176 (3) sets only the earliest day for the ACAT application.** The application "must be made after the later of" 5 business days after accepting liability and 28 days after a notice asking a dependant for information. There is no latest day: the obligation stays pending, and a trace 400 days on is still waiting. Where liability is accepted on Thursday 1 October 2026, with Labour Day on Monday 5 October, the application may be made from Saturday 10 October 2026. Traced and asserted.
15. **Section 101 (2) (b) (ii) does not say which of its two end dates applies.** It gives "(A) 2 years after the person reaches the pension age; or (B) 5 years after the date of the motor accident". Section 51 (2) supplies the earlier: the entitlement ends "on the first occurring". Someone reaching pension age on 1 January 2028 after an accident on 3 August 2026 is paid until 1 January 2030. Asserted.
16. **Interim weekly payments can run one day longer than the first payment period.** Section 103 (2) (c) stops them "13 weeks after the date of the motor accident" (day 91). The first payment period is "13 weeks beginning on the date of the motor accident" (days 0 to 90). After an accident on 3 August 2026 the first payment period ends on 1 November, and interim payments may run to 2 November 2026. Asserted.
17. **NI2026-402 is signed "31 August 2025" but was notified on 3 September 2026.** It declares the amounts for the 1 October 2026 indexation day and gives the 1 April 2026 figures for comparison, so the year on the signature looks like a slip for 2026.
18. **Item 8's table heading in NI2026-402 cites the wrong section.** Item 8 is for "the AWE indexed amount mentioned in section 181 of the MAI Act for the maximum amount of funeral benefits payable", but its table heading reads "AWE indexed amount mentioned in section 243". Section 243 is quality of life damages, which is item 9. The amount ($15 000 → $19 160) is the s 181 figure, and the encoding uses it as such.
19. **The Declaration's arithmetic checks out, but its earlier columns are for information only.** Every "1 October 2026" amount is the comparison amount times the factor, rounded up as s 18 (1) (c) requires (see Checks). The comparison columns are marked "* For information/comparison". The figures in force from 1 April 2026 (biannual) and 1 October 2025 (annual) were declared by earlier instruments, which are not deposited.
20. **Section 96 (2) cites a provision of the Superannuation Guarantee (Administration) Act that no longer sets the rate.** Section 96 (2) takes "the superannuation guarantee charge number set out in the Superannuation Guarantee (Administration) Act 1992 (Cwlth), section 19 (2)". In the deposited compilation of that Act (No 78, 1 July 2026, under Payday Super), s 19 is "When this Subdivision applies" and has no subsection (2). The rate now appears as "charge percentage means 12" in s 17A (2). For contributions paid or payable from 1 July 2026, the cross-reference has nothing to point to. The encoding asks for the percentage.
21. **The growth of the indexed amounts differs widely and cannot be checked here.** By 1 April 2026, $100 had become $170 (× 1.70) and $800 had become $1 026 (× 1.28). Over the same period $1 000 had become $1 247 (× 1.25) and $2 250 had become $2 794 (× 1.24). Rounding up to the dollar on each indexation day since 2020 cannot add $46 to the $100 figure. Without the AWE series and the earlier declarations this cannot be checked. Not asserted; worth checking against those declarations.
22. **The s 94 example divides by a figure the example does not give.** The example gives the AWE for November 2019 as "$1 856.80" but divides by "$1 856.0" ("$1 884.30 ÷ $1 856.0 = 1.015"). Both give 1.015 to three decimals (1.01481 and 1.01525), so the answer is unaffected. The slip is in the deposited text; the authorised PDF was not compared.

## Before relying on it

- An independent test pass, and a check of the deposited texts against the authorised PDFs (the Act's, and the Declaration's signature date and item 8 heading).
- Deposit the MAI guidelines (the receipt notice period, funeral expenses, exceptional circumstances), the Motor Accident Injuries (Premiums and Administration) Regulation 2019 (the interim payment percentage; the indexation and adjustment days), the 2026 adjustment of pre-injury income declarations, and the 2026 (No 1) and 2025 indexation declarations behind the comparison columns (findings 19, 21).
- The next declarations, for 1 April 2027 (biannual) and 1 October 2027 (annual). Add them as rows of the dated tables.
- Pre-injury income (ss 80-88, 99) worked out from facts, and the AWE adjustment (s 94) once the s 95 declarations are deposited.
- The WPI assessment process (ss 137-165), treatment and care beyond entitlement, the significant occupational impact assessment (ch 3), and damages (ch 5), each as its own pass.
- A pass reading s 98 and s 50 against the Workers Compensation Act 1951 (ACT) baseline, which was committed alongside this one.
- A ruling, or the authorised text, on findings 3, 4, 6, 7, 9, 11, 12 and 13.
