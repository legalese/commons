# Duties Act 2001 (Qld): baseline encoding for the buyer of a home, a block or a vehicle

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit `not covered` value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written as a seat-neutral core and a seat layer:

- **`qda-core.l4`**: transfer duty on land. The dutiable value, the general rate (Schedule 3, as a table), the Chapter 2 Part 9 home concessions (Schedule 4A as a table), the s 93 two-buyer case, the Duties Regulation's ELN list, the Part 14 Division 1 clawback, additional foreign acquirer duty, and two regulative rules: lodging (ss 19(3), 20) and the clawback notice (s 155).
- **`qda-admin.l4`**: the Taxation Administration Act 2001 as it applies to duty. Time for payment, unpaid tax interest, penalty tax, objections and appeals, with two regulative rules: payment (ss 30, 54(1)) and the objection-and-appeal chain (ss 63-69).
- **`qda-vehicles.l4`**: Chapter 9 vehicle registration duty, with one regulative rule (s 381).
- **`qda-dates.l4`**: the date arithmetic the three share (prelude DATE builtins only, no daydate import).
- **`qda-seat.l4`**: the buyer's seat. 20 questions, each with `@export` and a `@desc` on every input, under seven `§§` headings. It builds the cores' records from plain answers and restates no rule.
- **`qda-cases-buyer.l4`**: the cases.

All three cores use the Act's own actors (the transferee, the parties to the transaction, the commissioner, the taxpayer, the applicant, the transferor). Computations are functions; where the text says "must" with a time, there is a `DEONTIC` rule.

No earlier encoding of this Act existed to keep. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

- **Duties Act 2001** (act-2001-071), as deposited at `../../registers/source-bundle/act-2001-071.txt`. This is the current in-force version on 2026-09-22, in force from 2026-08-01 according to the jurisdiction README, which also found it still current on 2026-10-20. This older deposit has no notice at its top and an older meta shape.
- **Duties Regulation 2023** (sl-2023-0104), version in force from 2025-05-01, as deposited at `../../../duties-regulation-2023/registers/source-bundle/sl-2023-0104.txt`. It is used only for s 5(1) and Schedule 2 Part 1.
- **Taxation Administration Act 2001** (act-2001-072), version in force from 2025-02-28, as deposited at `../../../taxation-administration-act-2001/registers/source-bundle/act-2001-072.txt`. Section 6(1) makes the Duties Act a revenue law. Section 5 of the Duties Act says the two "must be read together as if they together formed a single Act".

All the rates and thresholds used are in the Act itself: Schedule 3, s 91, s 92(1)(c), Schedule 4A, s 244, s 382, s 383 and Schedule 4C.

Three things the encoding needs are **not deposited**, and are handled as follows:

- **The prescribed rate of interest** (TAA s 54). It is set by the Taxation Administration Regulation 2022, which the README left out as administrative. The rate is an input.
- **The value of a penalty unit** (Penalties and Sentences Act 1992). Offences are stated in penalty units.
- **The s 153(2) formula** did not survive conversion (finding 9). C and OD are computed; TD is not.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `qda-core.l4`, `qda-admin.l4`, `qda-vehicles.l4`, `qda-dates.l4`, `qda-seat.l4` | `qda-cases-buyer.l4` | 148 written, 148 satisfied |

In addition, 6 `#TRACE`s carry an `-- expect:` line, and each was read and matches it:

- 3 breaches: no one lodges by day 30; no s 155 notice by day 28; vehicle duty not paid with the application.
- 3 obligations still pending: tax unpaid after the due date (now owed with interest); an objection lodged but not yet decided; an appeal attempted before paying, with 40 days left.

`l4 run` on all six files gives 0 errors and 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A copy of the case file with one expected value altered (the s 93 figure changed to $10,012.50) was run as a control. The runner reported that assertion failed and 147 satisfied.

Every expected value was worked by hand from the deposited texts, with the arithmetic in the comment above the assertion. The Schedule 3 values used are tabulated at the top of the case file. Two figures come from the Act's own worked examples in TAA s 54: the 13 April start date and the $32.87 of interest.

## Seat

**The buyer.** That is the transferee of a home or of residential vacant land, or the person applying to register a vehicle or to have one transferred into their name. They ask:

- "How much transfer duty must I pay on my home?"
- "Which concession do I get, and what does it save?"
- "We are two buyers and only one of us will live there: what then?"
- "By when must I lodge and pay?"
- "What happens if I rent it out or sell within a year, and by when must I tell the Commissioner?"
- "I am a foreign buyer: what AFAD is due?"
- "What interest and penalty tax can I be charged?"
- "How do I object or appeal?"
- "How much duty is due on registering my car, and am I exempt?"

No second seat. The seller is also liable under s 17(2), and so is the transferor of a vehicle under s 380(2). The rules show them as parties (`another party to the transaction`, `the transferor`), but their duties are the same as the buyer's and are discharged by the buyer's performance. The Commissioner has no seat. The Commissioner's duties (decide an objection, make a reassessment) appear only as what the buyer is owed.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Its numbers are in the Act. The Duties Regulation is brought in only to confirm that the concessions cover ELN transfers. The Taxation Administration Act is brought in for payment, interest, penalty and objection, as the task asked: it is the other half of "a single Act". The Taxation Administration Regulation 2022 is not deposited (see Edition).
- **The actors the text names.** The transferee, the parties to the transaction, the commissioner, the taxpayer, the applicant, the transferor.
- **Judgments left to others are answered conditionally, or left out.** Answered conditionally: the s 58(3) uplift (an input, "the commissioner finds ..."). Not encoded:
  - the s 14(1)(c) opinion on value-reducing arrangements (the unencumbered value is an input);
  - the s 92(3), 92A(5) and 92B(5) waiver of the age requirement;
  - the s 65(2) extension of time to object;
  - the s 60 remission (amounts are before any remission).
- **The Act's own definitions are worked out from facts:**
  - dutiable value (s 11(7)) and the dutiable value of the residential land (s 90);
  - home (s 86(1)), first home (s 86(2)), first home on vacant land (s 86B);
  - the occupancy requirement, specified resident (s 90A), permanent resident and specified foreign retiree (Schedule 6, s 246(2), from visa facts), foreign individual (s 235);
  - liability (Schedule 2);
  - relative (s 379A, from the relationship);
  - the dutiable value of a vehicle (s 378).

  Borrowed terms are asked as facts: Australian citizenship and the Migration Act visas; "new residential premises" for GST (s 86(5)); the Vehicle Registration Act's concessional fees, special vehicle registration and GVM; principal place of residence.
- **One case** is one dutiable transaction, or one application to register or transfer one vehicle. Where several people buy together, each person fact is about every buyer, because Part 9 asks that "the transferees ... are all individuals", that the residence be the first home "of all of the transferees", and that "each" be a specified resident. The s 93 question takes the facts of the one buyer who qualifies.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Commissioner's powers, charges and sale of land for unpaid duty, offences other than as consequences, and commencement and transitional provisions.

**Departures.**

- **AFAD residential land (s 232)** is the Act's own definition, but it is asked as one fact. Its six paragraphs reduce, for a buyer, to "used or to be used solely or mainly for residential purposes, with a single-family dwelling on it or to be built".
- **Residence (s 87) and residential land (s 86A)** are asked through the choice "residential land / vacant land / other".
- **Intervening event (Schedule 6)** is asked as one fact, with its list in the `@desc`.
- **Readings** (Acts Interpretation Act 1954 s 38, not deposited): "within N days after" a day ends N days later; "within 1 year after" a day ends on its first anniversary; an anniversary of 29 February falls on 28 February. A failure to meet the occupancy requirement "happens" on the day after its last day.
- **Where more than one concession applies** (s 91 always does where s 92 or s 92A does), the one with the least duty is taken. The Act leaves the choice to the application (s 95). The answers assume the concession is applied for in the approved form, as s 95 requires.

## Scope

**In:**

- ss 9(1)(a)-(b), 10(1)(a), 11(7), 12(1) (as the input's gloss), 14(1), 16 and Schedule 2, 17, 19(3), 20, 24(2) and Schedule 3;
- ss 85-90A, 91, 92 and Schedule 4A, 92A, 92B; s 93(1)(c)(ii) and (7) for two buyers of whom one qualifies (every other s 93 case is `not covered`); s 95 (as an assumption);
- ss 153, 154 (C and OD; TD missing, finding 9), 155 (regulative, with its LEST);
- Chapter 4 ss 231, 232 (as a fact), 233(1)(a), 234, 235, 240(1), 243, 244(2)(a);
- Chapter 9 ss 377, 378, 379A, 379B, 380, 381 (regulative), 382(2), 383 and Schedule 4C, 390(1)(j)-(m) and (2);
- Duties Regulation 2023 s 5(1) and Schedule 2 Part 1;
- Taxation Administration Act ss 30(1)(b), (e), (2) (with a regulative rule); 54(1), (2), (5)(aa)(i), (c), (e), (6), (7); 58(1)-(3); 63(1), (2)(a), 64(1), 65(1); 67(1), 68(1), 69(1)-(3) (with a regulative rule).

**Out:**

- landholder and corporate trustee duty (Chapter 3);
- trusts and partnerships, including the trustee routes in ss 91(1)(b)(ii), 92(1)(b)(ii) and 94: a buyer that is a trustee or not an individual is `not covered`;
- ss 93A-94A: a two-buyer first home and new home, or vacant land, is `not covered`;
- s 93(1)(c)(i), (2) and (3);
- s 154(2)(c), (2AA) and s 154A; retirement villages;
- mortgage and insurance duty; windfall duty (Chapter 4A);
- AFAD on foreign corporations and trusts, s 240(2) agents, the s 246 exemption for specified foreign retirees (`not covered`), and the Chapter 4 Part 5 reassessments;
- the s 384 vehicle duty reductions; the other vehicle exemptions (ss 385-389, 390(1)(a)-(i), 391, 392);
- the weekly timing of late payment interest (s 54(3)(b)); compromise and return self assessments; TAA s 28 (noted under finding 12); the court and QCAT procedure after s 69.

## Read with the Commonwealth layer

**CGT main residence exemption**, Income Tax Assessment Act 1997 Subdivision 118-B. It is encoded at `../../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/`: ss 118-110 and 118-150 in `itaa-cgt.l4`, with the partial exemption of s 118-185(2) in `itaa-cgt-formulas.l4`.

The Commonwealth "main residence" and the Queensland "home" (s 86) must be kept apart. They answer different questions on different tests:

- **Queensland's home is a test at acquisition.** The buyer must occupy, as owner and as principal place of residence, within 1 year after becoming entitled to possession (2 years for vacant land, s 86B). The concession is then clawed back only for a disposal or lease within the year after moving in (s 153), or for a failure to occupy in time (s 154).
- **The Commonwealth main residence is a test over the whole ownership period** (s 118-110: "throughout your ownership period"). It has its own reliefs: the choice for building on land, up to 4 years (s 118-150); the absence rule (s 118-145); and partial exemptions (ss 118-185, 118-190).

So the two can come apart:

- **A home let out 13 months after moving in** keeps its Queensland concession, but the CGT exemption is only partial unless the absence rule is chosen.
- **A room let to a lodger after moving in** costs nothing under s 153(1C), but may reduce the CGT exemption (s 118-190).
- **A block built on in the third year** has failed the Queensland 2-year occupancy requirement, but can still be a main residence from acquisition under s 118-150.

The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here, not in code.

Other links in Queensland, from the jurisdiction README:

- the first home owner grant (FHOG Act s 15 residence requirement) and land tax's home exemption (Land Tax Act 2010 Part 6 Division 1) turn on the same fact, "this is my home", each with its own definition;
- the principal home is exempt from the Social Security Act 1991 assets test (s 11), on the Commonwealth's own definition.

## What the Act turns out to say

1. **The $100,000 surcharge on vehicles falls on the whole value, not on the part above $100,000.** Section 383(1)(b) adds "$2 for each $100, and each part of $100, of the vehicle's dutiable value" once that value is "more than $100,000". A new 6-cylinder car at $100,000 pays $3,500. At $100,001 it pays 1,001 × $5.50 = $5,505.50. A reading of "$2 per $100 above $100,000" does not match the text. Asserted.
2. **The $700,000 in s 92(1)(c) is not a cap on the first home concession.** It applies only where the price is below the unencumbered value. A buyer paying at least the value gets the Schedule 4A amount up to $799,999.99:
   - a $750,000 unit at arm's length pays $10,925 (s 91 duty of $19,600, less $8,675);
   - the same unit bought for $750,000 when worth $760,000 loses s 92 and pays $20,050 under s 91.

   Asserted.
3. **The first home nil band ends exactly at $700,000.** There the s 91 duty is $3,500 + $24,525 − $10,675 = $17,350, which is the full Schedule 4A amount. At $705,000 the duty is $225. The table then steps down by $1,735 for each $10,000, to nil at $800,000; $799,999 pays $20,115. Asserted.
4. **The first home and new home concession (s 92A) and the vacant land concession (s 92B) have no value limit.** A first home buyer who pays at least the unencumbered value pays nil on the residential land at any price. A $2,000,000 new house saves $95,525. Only other property in the purchase is dutiable: $30,000 of furniture with a $900,000 new apartment costs $1,350. Asserted.
5. **A new home bought below its value gets only the home concession.** Section 92A(1)(d) needs the consideration to be at least the unencumbered value, and s 92(1)(aa) closes s 92 to a new home. A first home buyer paying $650,000 for a new home worth $700,000 therefore pays $17,350 under s 91. Asserted.
6. **Above $350,000, the home concession saves a fixed $7,175.** Under s 91(5) the duty on a home is $3,500 + the general duty − $10,675, so the saving on the land is always $10,675 − $3,500. At $600,000 the duty is $12,850 against $20,025. Asserted.
7. **The s 93 concessional duty for a first home buyer is negative, and must stay negative.** Section 93(8)(a)(ii) takes $3,500 less the s 92(2) deduction, which at $600,000 is −$9,350. Kept negative, the s 93(7) formula gives the s 92 duty (nil) at a 100% interest and the s 91 duty at a 100% home-only interest. For a first home buyer owning half, with a co-owner who will not live there, it gives $10,800, not the $10,012.50 of halving the two duties. Asserted.
8. **The 30 days to lodge run from signing the contract, not from settlement.** Schedule 2 makes liability on an agreement for transfer arise "When the agreement is made", and s 19(3) gives 30 days after that. Section 17(2) makes "the parties to the transaction" liable, which on its words includes the seller, and s 20 relieves the others once one lodges. A contract signed on 3 August 2026 must be lodged by 2 September 2026. Asserted, and #TRACEd for the case where no one lodges.
9. **The s 153(2) clawback formula is missing from the deposit.** The deposited text runs "worked out using the following formula—" straight into "where—" and the definitions of C, OD and TD. The formula itself, probably an image, did not survive conversion. The encoding computes C (duty at the general rate less the duty assessed) and OD (days from moving in to the disposal, both inclusive), and answers that TD is not computed. Before TD can be encoded, the formula must be transcribed into an `act-2001-071.formulas.md` sidecar from the authorised PDF. The s 384(2) vehicle reduction formula is lost in the same way (it is out of scope). Asserted (C and OD).
10. **The s 155 notice is wider than the clawback.** A notifiable event is any "transfer, lease or otherwise granting of exclusive possession of all or part of the land" before, or within 1 year after, the occupation date. It has no exception for an intervening event. So notice is due within 28 days for each of these, although ss 153 and 154 impose no further duty:
    - letting a room;
    - transferring a share to a spouse under s 151;
    - selling after a flood.

    Failure is an offence under TAA s 120 (up to 100 penalty units). Asserted.
11. **Letting before moving in costs the whole concession.** Section 154(2)(b) treats any lease of "part or all of the land" before the occupation date as a disposal, and s 154 has no counterpart to s 153(1C). A first home buyer who lets a room before moving in is reassessed as if no concession applied ($20,025 at $600,000), even if they move in on time. Asserted.
12. **A clawback reassessment attracts penalty tax and back-dated interest.** Under TAA s 58(1)(c), any reassessment that raises the duty carries penalty tax of 75% of the increase: $15,018.75 on a $20,025 clawback, unless the Commissioner remits it under s 60. The uplift of up to 20% in s 58(3)(a) is for not complying with TAA s 28, which requires a taxpayer to report an under-assessment within 30 days. That runs beside the 28 days of s 155. Under s 54(5)(e) and (7), interest on the reassessed duty runs from the original assessment's start date. Asserted (the penalty).
13. **The Act's own interest example accrues late payment interest daily, while s 54(3)(b) makes it accrue weekly.** The s 54(7) example's $32.87 is 10,000 × 10% × 12 / 365 = 32.8767, with the part of a cent dropped. For a revenue law other than a royalty law, s 54(3)(b) makes late payment interest accrue on a prescribed weekday and weekly after. The encoding accrues daily and drops part-cents, as the example does. The prescribed rate and weekday are in the undeposited regulation. Asserted.
14. **Late lodging brings the interest start date forward.** Section 54(5)(c)(ii) moves the start date back by the days of noncompliance with a lodgement requirement, counting the day of compliance (s 54(6)(b)). The Act's example (lodgement due 10 March, made 15 March, duty due 17 April) starts interest on 13 April. Asserted.
15. **A New Zealand citizen on a special category visa is a permanent resident, and a specified foreign retiree is a foreign individual.** The first gets the home concessions and pays no AFAD. A Subclass 405 or 410 retiree gets the home concessions as a specified resident (s 90A(c)), but is a foreign individual for AFAD (s 235). The s 246 exemption from AFAD is not encoded, so that case answers `not covered`. Asserted.
16. **AFAD is not reduced by the home concessions (s 243), and a mixed couple pays both.** Take a citizen first home buyer and a foreign spouse owning half each of a $600,000 house. They pay transfer duty of $10,800 under s 93, and AFAD of 8% × $600,000 × 0.5 = $24,000. Asserted.
17. **The ELN regulation leaves out s 93.** Duties Regulation 2023 Schedule 2 Part 1 prescribes ss 91, 92, 92A and 92B (and ss 105, 105A) for ELN transfers, but not ss 93, 93A or 93B. Under s 156D, a transaction eligible for any concession that is not prescribed cannot be an ELN transfer or a relevant transfer agreement. A two-buyer mixed claim therefore falls outside the ELN duty provisions. Asserted (the list); the consequence is a reading.
18. **A new car's dutiable value is its list price plus options, not the price paid.** Under s 378(1), a car listed at $45,000 with $500 of options and sold for $44,000 pays duty on $45,500 ($910). A used car pays on the greater of the price and the market value. A used vehicle modified for a person with a disability pays on its market value less the modifications, and the price is not used at all (s 378(3)(b)). Asserted.
19. **An appeal or QCAT review needs the duty paid first.** Under TAA s 69(1)(b), the taxpayer must first pay the whole of the tax and late payment interest. The 60 days run from the decision notice regardless, and QCAT may not extend them (s 69(3)). The objection itself must be lodged within 60 days of the assessment notice (s 65(1)(d)). Asserted, and #TRACEd for an appeal attempted before paying.
20. **An assessment notice must allow at least 30 days.** Under TAA s 30(2), a notice given on 1 September 2026 cannot state a payment date before 1 October 2026. The Act does not say what follows if it does, so the encoding reports the shorter date as non-compliant rather than guess. Asserted.

## Before relying on it

- Transcribe the s 153(2) and s 384(2) formulas from the authorised PDF into a formulas sidecar, and encode TD (finding 9).
- Deposit the Taxation Administration Regulation 2022, for the prescribed interest rate and weekday, and encode the weekly accrual of late payment interest (finding 13). Also deposit the penalty unit value.
- Encode s 93(6) (a home buyer with a first home buyer), ss 93A, 93B, the trustee routes and s 94, and the s 246 AFAD exemption.
- Encode s 154(2)(c) and (2AA): buying with a tenant in place, or with the seller staying on.
- Encode the Commissioner's age waiver as a conditional input.
- An independent test pass, and a check against the Queensland Revenue Office's calculators and public rulings, none of which were consulted.
- Link the home concession answers to an encoding of the FHOG Act and the Land Tax Act home exemption, when they exist.
