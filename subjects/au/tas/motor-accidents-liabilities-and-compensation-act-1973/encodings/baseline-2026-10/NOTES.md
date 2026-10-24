# Motor Accidents (Liabilities and Compensation) Act 1973 (Tas): baseline encoding of the MAIB scheduled benefits, for the injured person and the Board

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
The Act's Part IV is read with the Motor Accidents (Liabilities and Compensation) Regulations 2020, whose reg 10 and Schedule 1 hold every number a claimant needs. Under the default "the Act alone, with the instruments that set its numbers or dates brought in", the two are encoded together.
There is no REFUSE in it. Four cases answer `not covered`, and tests assert each one:

- an accident before 17 February 2020 (for the allowances, the cap and the death benefit);
- funeral benefits for an accident before 1 December 2007;
- a s 6 (1) conviction below 0.05, which the s 24 (4) table has no row for;
- (through the same answer types) anything that depends on the 2010 or 2000 Regulations.

It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in three layers:

- **`maib-core.l4`**, the seat-neutral core. It uses the texts' own actors and terms: the Board, a resident of this State, a person who suffers personal injury resulting directly from a motor accident, the dependants, the personal representative, a family member, the Tribunal. Computations are functions: the s 23 ground, the s 24 exclusions, the cl 8 cap, medical benefits, the funeral limit, the death lump sum, the cl 7 average weekly earnings, the allowance rates and periods, counselling, and the reg 10 dates. Where the text says "must" or "may" or sets a deadline, there is a regulative rule (`DEONTIC`). There are three:
  - reg 10 (2)-(4): the claimant must give written notice and bring the claim in time;
  - s 28 (1)-(2): the Board determines, and a person aggrieved may refer the matter to the Tribunal;
  - s 23 (1), (1A), (2): the Board must pay.
- **`maib-seat.l4`**, the individual's seat. It asks 23 questions, each with `@export` and a `@desc` on every input, under `§§` headings: am I covered; claiming; medical benefits and the cap; disability allowances; accidents in another State; after a death; counselling for family members; damages and daily care. It builds the core's records from plain answers and restates no rule.
- **`maib-seat-board.l4`**, the Board's seat, limited to its duty to pay scheduled benefits under s 23 (1), (1A) and (2). It asks 7 questions on the same core.

No earlier encoding of this Act existed to keep. No requirement ledger covers Tasmania, so no ledger line is closed. No scenario life raised the Act; every case is HYPOTHETICAL.

## Edition

- **Act:** Motor Accidents (Liabilities and Compensation) Act 1973 (No. 71 of 1973), the consolidated version published 2026-01-28 and current on Tasmanian Legislation Online at 2026-10-20, as deposited at `../../registers/source-bundle/act-1973-071.txt`.
- **Regulations:** Motor Accidents (Liabilities and Compensation) Regulations 2020 (S.R. 2020, No. 7), the consolidated version published 2021-06-15 and current at 2026-10-20, as deposited at `../../../motor-accidents-liabilities-and-compensation-regulations-2020/registers/source-bundle/sr-2020-007.txt`. The licence is the same (CC BY 4.0, © State of Tasmania); both subjects' terms are in `SOURCE-LICENSE.md`.
- Both deposits are unofficial plain-text conversions; the authorised versions are on the site. Uncommenced amendments are not in a consolidation.
- **Formula from an image.** The Sch 1 Pt 3 cl 2 (1) funeral formula, A = 7 500 × I%, appears in the source only as an image. It was transcribed in the deposit and is encoded as transcribed. Check it against the image (`malcam07.gif`) before relying on it.

Inputs, because what fixes them is not deposited or is someone else's judgment:

- **Adult average weekly earnings** (ABS 6302.0, s 2 (1)):
  - the figure last published before the accident (Pt 5 cl 3 (5) (b), cl 4 (4) (b));
  - the figure released on the 2007 release day, and the most recent one for a period ending in May (Pt 3 cl 2).
- **The Board's determinations and judgments:**
  - whether a failure to report to police is excused (s 23 (2A));
  - whether a premium was known, or ought to have been known, to be unpaid (s 24 (1) (g));
  - whether the alcohol did not contribute (s 24 (4A));
  - the provider for travel (Pt 2 cl 1 (3) (j), (k));
  - the value of a self-employed person's hours (Pt 5 cl 4 (5));
  - average weekly earnings, in the Board's seat (Pt 5 cl 7).
- **The Tribunal's extensions** of the reg 10 (2) periods (reg 10 (3)-(4)), asked as the day to which it extended each period.
- **Medical judgments:** whether treatment is warranted, beneficial and curative (Pt 2 cl 1 (4) (b)), its most economical practicable cost, and the Commonwealth (Medicare) amounts.
- **Borrowed terms, asked as facts:** "as soon as practicable"; the conviction offences of the Road Safety (Alcohol and Drugs) Act 1970, the Traffic Act 1925 and the Criminal Code; "significant relationship" and "caring relationship" (Relationships Act 2003); workers compensation and interstate motor accident compensation being payable; the asbestos-related disease entitlement.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `maib-core.l4`, `maib-seat.l4` | `maib-cases-injured.l4` | 198 written, 198 satisfied |
| `maib-core.l4`, `maib-seat.l4`, `maib-seat-board.l4` | `maib-cases-board.l4` | 44 written, 44 satisfied |

The 44 in `maib-cases-board.l4` include 12 mirror assertions: the same facts asked from both seats, with answers that agree. They cover liability, claim timing, the cap, the employed person's allowance, the s 24 (4) proportion, the death benefit and the funeral limit. The file also has 6 `EVALTRACE` assertions of the regulative rules ending FULFILLED.

In addition, 4 `#TRACE`s in `maib-cases-board.l4` carry an `-- expect:` line:

- two breaches by the claimant: written notice one day late (day 366), and the claim one day late (day 449);
- two obligations still pending: a payment of the wrong amount (the Board must still pay EXACTLY $1 120), and an adverse determination (the claimant still MAY refer the matter to the Tribunal, with no time limit).

Each was read and matches its expectation.

`l4 run` on all five files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

Every expected value was written by hand from the deposited texts, with the arithmetic in the comment above the assertion. The calendar dates (the 7-day, 26-, 39-, 104- and 260-week ends, the one-year days, the trace day numbers) were then checked independently with Python's `datetime`, not against the encoding.

## Seats

**The individual (first, required).** The person who suffers personal injury resulting directly from a motor accident. After a death, the seat is also:

- the dependants, for death benefits (s 23 (4) (c));
- the personal representative, for funeral benefits (s 23 (4) (b));
- the family members, for counselling services benefits (s 23 (4) (f)).

They ask:

- "Is MAIB liable to pay me scheduled benefits for this accident, and which ones? Do I require daily care?"
- "What must I do, and by when: report to police, give written notice within a year, claim within a year? Was I in time? Can I go to the Tribunal? Does my Commonwealth pension reduce my benefits?"
- "What cap applies to my medical and disability benefits, and how much is left? How much of this bill will MAIB pay?"
- "Which disability allowance applies, at what weekly rate, and from and until when? What are my average weekly earnings? Can it be paid for this day? What is left after a drink-driving conviction?"
- "For an accident interstate, what does MAIB pay after the other State's benefits?"
- "Am I a dependant? What death benefit and funeral benefit does my family get? What counselling benefit can I get?"
- "After my damages, does MAIB still pay for this item?"

**The Board (second, limited).** The Motor Accidents Insurance Board is the insurer, and s 23 puts a "must pay" duty on it: "The Board must pay the benefits prescribed by the regulations if ...". That justifies a second seat, as the guide allows for "the insurer's customer and the insurer". The seat is confined to that duty. Premiums (Part V), the Part III indemnity, administration and the Injury Prevention and Management Foundation are out. It asks:

- "Must I pay scheduled benefits for this injury, and which?"
- "Was the claim made in time?"
- "What is the most I must pay under the cap?"
- "What employed person's allowance must I pay this week, on the earnings I determined?"
- "What part must I pay after a drink-driving conviction?"
- "What death benefit must I pay?"
- "What is the most I must pay as funeral benefits?"

The regulative rules give the Board's duties a trace: a determination (s 28 (1)), then payment (s 23). Neither text sets a time for either (finding 13).

Where the Board states one fact for a group, the seat carries it in one field of the core's record that the rule reads, and passes fixed placeholders for the others. Each place has a comment saying so. There are two:

- daily care, as the Board's determination, carried in the s 27A (2) field;
- entitlement under cl 3 (2), carried in the cl 3 (2) (a) field.

Officials get no seat: not the Tribunal, the police, the Registrar or the courts. Their acts (an extension, a conviction, a certificate) appear only as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed: the Regulations 2020 are brought in for reg 10 and Schedule 1 (and reg 11 (2), the prescribed trailers).
  - Not deposited, so not used: the 2010 and 2000 Regulations, which govern earlier accidents (`not covered`), and the ABS AWE series (inputs).
  - The Road Safety (Alcohol and Drugs) Act 1970, the Traffic Act 1925, the Relationships Act 2003, the Vehicle and Traffic Act 1999 and the Monetary Penalties Enforcement Act 2005 are cited, and their terms are asked as facts.
- **The actors the text names.** Followed: the Board, the injured person, the dependants, the personal representative, the family members, a police officer, the Tribunal, a medical practitioner, the Public Trustee (named, not encoded).
- **Judgments left to someone else, answered conditionally.** Followed. Each is an input worded as the judgment, for example "the Board has determined that the failure to report should be excused", "the treatment is warranted, beneficial and curative", or the day to which the Tribunal extended a period. The Board's apportionment of the death benefit between dependants (Pt 4 cl 1 (4) (b)) is not computed: only the lump sum is.
- **The Act's own definitions worked out, borrowed terms asked.** Followed. Worked out from facts:
  - resident (s 2B);
  - personal injury from a motor accident (s 2 (4));
  - a vehicle registered in this State, and an interstate motor vehicle, "involved" (s 23 (2B), (2C));
  - requires daily care (s 2 (5), s 27A (2)-(3));
  - family member (s 23 (8));
  - dependant, dependent child, dependent parent, dependent carer, survivorship and the unborn child (Sch 1 Pt 1 cl 1, 4-7);
  - prescribed trailer (reg 11 (2));
  - employed person (Pt 5 cl 3 (2));
  - average weekly earnings (Pt 5 cl 7).
- **One case is the text's natural unit.** Followed: one injured person and one accident; one death; one claim; one family member; one week of allowance.
- **The Act's own terms, each glossed.** Followed: the comment above each rule quotes or paraphrases the provision.
- **Machinery out.** Followed: the Board's constitution and powers (Part II), the Foundation (Part IIA), premiums (Part V) and the regulation-making power.

## Scope

**In:**

- the Act:
  - s 2 (1): interstate motor vehicle, interstate premium, motor accident, daily care, registered, family member;
  - s 2 (4), s 2 (5), s 2B;
  - s 23 (1), (1AA), (1A), (2), (2A), (2B), (2C), (3), (8);
  - s 24 (1) (a)-(h) with (1A); s 24 (2), (3), (3A); s 24 (4) and (4A);
  - s 26 (no regulation made);
  - s 27A (2)-(6);
  - s 28 (1)-(2);
- the Regulations:
  - reg 10 (2)-(4);
  - reg 11 (2);
  - Sch 1 Pt 1 (cl 1, 2, 4-8);
  - Pt 2 (medical benefits, with the taxi and travel conditions);
  - Pt 3 (funeral benefits);
  - Pt 4 cl 1 (1)-(4) and cl 2 (death benefits for accidents from 17 February 2020);
  - Pt 5 (disability allowances: cl 1-7);
  - Pt 7 (counselling services benefits).

**Out**, each returning nothing or a `not covered` value where a question touches it:

- Part III: common-law liability, the Board's third-party indemnity, recovery from owners and drivers, unidentified vehicles, ss 14-22;
- Part V premiums; Part II and IIA (the Board's administration and the Injury Prevention and Management Foundation);
- the rest of Part IV:
  - s 24 (5), the Board's power to suspend an allowance pending court proceedings: noted, not encoded;
  - s 25 (infants);
  - s 27 (scheduled benefits and damages), except s 27A;
  - s 27B (examinations and rehabilitation programs);
  - ss 28A-28C (redemption and recovery);
- Sch 1 Pt 6, disability benefits in detail (prostheses, alterations, attendant care, domestic services, gratuitous services). Only the cl 8 cap counts them;
- death and funeral benefits for accidents before 17 February 2020 and 1 December 2007 (the 2010 and 2000 Regulations, not deposited);
- Pt 3 cl 2 (2) and Pt 4 cl 1 (5)-(8) (the same earlier accidents);
- regs 1-9 (premium certificates, records, refunds, prescribed jurisdictions for s 20).

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social Security Act 1991 (Cwlth)**, `../../../../social-security-act-1991/encodings/baseline-2026-10/`. MAIB disability allowances are periodic compensation, and a later damages settlement is a compensation lump sum. Both fall under the compensation-recovery rules of Part 3.14. That baseline's questions take the MAIB payments as their facts:
  - `Is my payment compensation affected`;
  - `By how much is my daily rate reduced for periodic compensation`;
  - `What is the compensation part of my lump sum`;
  - `How many weeks is my lump sum preclusion period`.

  The Tasmanian s 26 power to reduce benefits for a Commonwealth pension is unused (finding 12), so the reduction runs one way only: from MAIB into the Commonwealth payment.
- **Income Tax Assessment Act 1997 (Cwlth)**, `../../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/`. Disability allowances replace earnings, and periodic compensation of that kind is ordinary income (s 6-5), so it is assessable. That encoding asks ordinary income as a fact. The death benefit, funeral benefit and medical benefits are lump sums or reimbursements for injury or death. Their tax treatment is not worked out in either encoding.
- **Health Insurance Act 1973 (Cwlth)**, `../../../../health-insurance-act-1973/encodings/baseline-2026-10/`. Pt 2 cl 1 (2) reduces a medical benefit by "any sums ... paid, or required to be paid, under a law of the Commonwealth" for the treatment, chiefly Medicare benefits. That baseline's `How much Medicare benefit do I get for my service, in dollars` supplies the figure this encoding asks for as `Medicare or other Commonwealth amounts for it`.
- **Workers Rehabilitation and Compensation Act 1988 (Tas)**, `../../../workers-rehabilitation-and-compensation-act-1988/`. Where workers compensation is payable for the injury, s 24 (1) (b) excludes every scheduled benefit. The fact is asked here, not worked out.

## What the Act turns out to say

1. **Section 23 (1) (a) needs no registered vehicle, but s 23 (1A) does.** A Tasmanian resident hit in Hobart by an unregistered car is covered: (1) (a) asks only that the accident occur in this State. A visitor hit by the same car is not: (1A) needs "a motor vehicle registered in this State" involved, and (2) needs an interstate vehicle and daily care. Asserted (L1, L5a).
2. **Section 23 (1A) reaches visitors from overseas; s 23 (2) gives an interstate resident only part of the scheme.**
   - "A person who is not a resident of this State" includes a resident of another country. An overseas visitor struck by a Tasmanian-registered car gets every scheduled benefit (L5).
   - An interstate resident in an accident involving only interstate vehicles is covered only if they require daily care. Even then they get only medical benefits, disability benefits and counselling: no disability allowance, no death benefit and no funeral benefit (L6, B2).

   Asserted.
3. **Section 24 (1) (ba) leaves s 23 (1AA) nothing to do.** For a Tasmanian injured interstate, s 23 (1AA) pays "the prescribed benefits less any benefits payable ... under the law of that other State or Territory". But s 24 (1) (ba) applies "notwithstanding section 23" and excludes every scheduled benefit "where compensation is payable in respect of the personal injury under any law of ... any other State or a Territory ... relating to the payment of compensation in respect of personal injury resulting directly from motor accidents". Read literally, whenever the other State's scheme pays anything, nothing is payable, so the netting never bites. It would bite only if "benefits" in (1AA) reached something that is not "compensation" in (ba). The encoding asks the two separately and lets (ba) win when it applies. Asserted (L15). Where the other law pays more than MAIB would, the encoding reads (1AA) as nil, not negative.
4. **Read literally, s 24 (1) (e) and (g) would exclude every interstate resident who drives their own interstate vehicle.** "Premium" means a premium payable under s 30 (s 2 (1)), the Tasmanian premium, which is never paid for an interstate vehicle. Paragraph (g) would then exclude such a driver, as its owner, in every accident: the very person for whom (ga) (an unpaid interstate premium) and s 23 (2) were added in 2013. The encoding applies (ea) and (ga), not (e) and (g), to an interstate resident's interstate motor vehicle. That is a reading. For a resident of this State, (g) applies to any vehicle, as s 24 (1A) shows it must: (1A) saves a Tasmanian driving a permitted out-of-State vehicle with a third party policy, a saving that would be needless otherwise. Asserted (L6, L12, B2).
5. **Section 24 (2) does not reach funeral, death or counselling benefits.** A conviction for dangerous driving, or driving unlicensed, ends "a medical benefit, disability benefit or disability allowance". If the driver dies, the dependants' death benefit and the funeral benefit are untouched, and so is the family's counselling. Asserted (L19, L20, B4).
6. **The deposited s 24 needs reading past its layout.**
   - Each paragraph label of s 24 (1) and (2) sits on its own line, followed by its amendment notes and then its text. Read past them, s 24 (1) has twelve paragraphs: (a), (b), (ba), (bb), (c), (d), (e), (ea), (f), (g), (ga), (h).
   - The closing words of (e), (ea), (g) and (ga) ("and the injured person was the owner or driver of that motor vehicle") sit after sub-paragraph (ii) and govern the whole paragraph.
   - So does "arising out of his driving of a motor vehicle at the time of the motor accident", after s 24 (2) (a) (iv), for every listed offence.
   - The history notes of s 24 (1A) are listed out of date order ("inserted ... 2002", "inserted ... 1988", "omitted ... 1995"), but the text printed is in force.

   The encoding follows that reading. Each paragraph is tested at least once (L10-L18).
7. **Most of the money figures are fixed, and below $320 a week the employed person's allowance replaces all of the person's earnings.** These are not indexed:
   - the $400 threshold and the $320 floor of Pt 5 cl 3 (5)-(6);
   - the $250 housekeeping cap;
   - the $400 000 and $500 000 caps;
   - the $88 000 death benefit and its increments;
   - the $1 270 counselling limit.

   Only the funeral limit moves with AWE, and the ceilings of the employed and self-employed allowances (3 × adult AWE). The resulting rates:

   | Average weekly earnings | Allowance | Share of earnings |
   |---|---|---|
   | $300 | $300 | 100% |
   | $350 | $320 | 91% |
   | $400 | $320 | 80% |
   | $401 | $320.80 | 80% |

   Asserted.
8. **The s 24 (4) table has no row for a s 6 (1) conviction below 0.05.** It reduces the allowance for a s 6 (1) conviction at 0.05 to under 0.12 (two thirds), 0.12 to under 0.24 (one third) and 0.24 or more (nil). Section 6 (1) of the Road Safety (Alcohol and Drugs) Act 1970 is an offence of a prescribed concentration of alcohol. Where that Act prescribes a lower concentration for some drivers (it is not deposited, so this is not checked), a conviction below 0.05 has no proportion. Subsection (4) still says the allowance "is to be calculated in accordance with the table". The encoding answers `not covered`. Asserted.
9. **Medical treatment must be "curative" to be necessarily incurred.** Pt 2 cl 1 (4) (b): an expense is "unnecessarily incurred if the treatment is not warranted, beneficial to the person and curative of the person's injury". Read literally, care that maintains or manages an injury that will not be cured is not payable as a medical benefit. That includes nursing care and rehabilitation for a person who requires daily care, though cl 1 (3) (i) lists them. Disability benefits (Pt 6) carry no such word. The encoding asks the three together as one fact, and nothing is payable when it is FALSE. Asserted.
10. **The death benefit's increase for children needs "2 or more dependants", and its three paragraphs are joined by "or".**
    - Pt 4 cl 1 (3) increases the $88 000 for each dependent child only "if the deceased is survived by 2 or more dependants". A child of 5 who is the only dependant gets $88 000. Two children of 3 and 7, with no other dependant, get $140 000.
    - Paragraphs (a), (b) and (c) (under 9, 9 to 17, 18 to 24) are joined by "or". The encoding adds each child's increase in its own band ($132 200 for a spouse and children of 5, 12 and 20). That is a reading.
    - The Schedule does not say on which day a child's age is taken. The encoding asks the age on the day of the death.

    Asserted.
11. **Pt 5 cl 2 (3) says a person is not entitled to both the employed and the self-employed allowance, but not which one they get.** An employee with a business on the side may qualify for both (cl 3 (2) (a), cl 4 (2)). The encoding flags the overlap and computes each allowance on its own; it does not choose. Asserted (the flag).
12. **Section 26 is unused.** The Act lets regulations reduce, withhold, postpone or apportion a scheduled benefit for a person entitled to a Commonwealth pension. The 2020 Regulations make no such provision, so a Commonwealth pension does not reduce MAIB benefits. Asserted.
13. **No time is set for the Board's determination, its payment, or a reference to the Tribunal.**
    - Section 28 (1) says the Board "is to determine", and s 23 that it "must pay", with no time in either text.
    - Section 28 (8) (b) lets regulations prescribe the time for a reference to the Tribunal; the 2020 Regulations prescribe none. The Tasmanian Civil and Administrative Tribunal Act 2020 may, but it is not deposited.

    So the Board's obligations stay pending until done, and the claimant's s 28 (2) permission never lapses. Traced.
14. **Two ways of counting weeks sit side by side in Pt 5.**
    - The employed and self-employed allowances run for "the period of 104 weeks beginning on the day of the motor accident", whose last day is the accident date plus 727 days. The 156-week prescribed period then ends 1 819 days after the accident.
    - The housekeeping allowance runs "within 26 weeks after the day of the accident", whose last day is the accident date plus 182 days, a day later on the same count.
    - After an accident on 10 March 2026, the employed allowance's first period ends on 6 March 2028 and the housekeeping allowance on 8 September 2026 (8 December 2026 after more than 4 days in hospital).

    Asserted.
15. **The funeral formula compares a February figure with a May figure, and does not say how to round.** I% runs from "the adult average weekly earnings released on the 2007 release day" (the February 2007 quarter, released in May 2007) to "the most recently released adult average weekly earnings for the period ending in May". So the base and the comparison are taken at different points of the year. No rounding is stated, and the encoding keeps the exact amount. Where AWE has fallen there is no "increase", and the encoding reads the additional amount as nil, not negative ($7 500). Asserted.
16. **Section 24 (4) does not say whether its proportion comes before or after the cl 3 (7) reduction for earnings.** The table gives the "proportion of disability allowance otherwise payable". The encoding reads "otherwise payable" as after cl 3 (7): on AWE $1 500, a 0.08 reading and $300 earned that week, (1 200 − 300) × 2/3 = $600. Taking the proportion first would give 800 − 300 = $500. That is a reading. Asserted.
17. **The 2020 Regulations speak to earlier accidents only for funeral, death and counselling benefits.** Pt 3 cl 2 (2), Pt 4 cl 1 (5)-(8) and Pt 7 cl 1 (2) (a) send earlier accidents to the 2010 or 2000 Regulations, or give their own earlier figure ($1 000 for counselling). For the disability allowances and the cl 8 cap, they give no transitional rule. The encoding answers `not covered` for an accident before 17 February 2020. The exception is the daily-care exemption from the cap, which is the Act's own (s 23 (4) (a), (e)) and holds for any accident. Medical benefits (Pt 2) carry no figure, and the encoding applies Pt 2 whatever the date; that is a reading. Asserted.
18. **Regulation 10's one-year periods and the Tribunal's 5 years are read as dates.**
    - "Within one year after" a date is read as ending on the same date a year later. An accident on 29 February 2028 is read to give 28 February 2029.
    - The Tribunal may extend a period "by such period not exceeding 5 years as it thinks fit". An extension to a later day is cut to 5 years after the original last day.
    - The written notice and the claim are separate conditions with separate starting dates. Either may come first, and one document may serve as both.

    Each is a reading. Asserted and traced.
19. **The cl 8 cap counts medical benefits (Pt 2) and disability benefits (Pt 6), not disability allowances (Pt 5).** The weekly payments of a person on a high income run outside the $400 000 or $500 000. The cap's trigger is a continuous hospital stay of "more than 4 days commencing on the date of the accident": 4 days gives $400 000, 5 gives $500 000. How the days are counted (calendar days or nights) is not said, and the encoding asks the number. Asserted.

## Before relying on it

- An independent test pass, and a check of both deposited texts against the authorised versions, including the funeral formula image (`malcam07.gif`).
- Deposit the Motor Accidents (Liabilities and Compensation) Regulations 2010 and 2000 (earlier accidents), the Road Safety (Alcohol and Drugs) Act 1970 (ss 4, 6 (1), 14; finding 8) and the Tasmanian Civil and Administrative Tribunal Act 2020 (time limits for a reference; finding 13).
- The ABS adult average weekly earnings series, or a dated table of it, so the cl 3 (5) (b) ceiling and the funeral limit need no input.
- Sch 1 Pt 6 (disability benefits) in detail, s 27 and ss 27B-28C, and Part III (common-law damages and the Board's indemnity), each as its own pass.
- A ruling, or the authorised text, on findings 3, 4, 9, 10, 15, 16 and 18.
- A pass reading s 24 (1) (b) against the Workers Rehabilitation and Compensation Act 1988 (Tas), once it is encoded.
