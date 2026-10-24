# Motor Accidents (Compensation) Act 1979 (NT): baseline encoding for the person injured, and for those left after a death

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case the deposit cannot answer (an accident before the amendments now in force, a part week, an impairment percentage between the rows of a table) returns an explicit `outside this encoding` value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in three layers:

- **`maca-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms: the injured person, the eligible person, the qualifying person, the claimant, the Commission, the designated person. Computations (the s 7 entitlement, the Part 3 exclusions, the weekly amount, the lump sums, the dates) are functions. Where the text says "must" or sets a deadline there is a regulative rule (`DEONTIC`): five in all (ss 7(3), 18BD(4), 31, 31A, and the review chain of ss 28A, 28B and 28E). The s 31 rule also has a form built from the dates, with `the days from`.
- **`maca-seat.l4`**, the seat of the person injured. 24 questions, each with `@export` and a `@desc` on every input, under `§§` headings.
- **`maca-seat-survivors.l4`**, the seat of those left after a death. 13 questions.

Neither seat restates a rule; both build the core's records from plain answers and call the core. Their names differ, so a case file imports both for the mirror cases.

No earlier encoding of this Act existed to keep. No requirement ledger covers the Northern Territory, so no ledger line is closed.

**Fix pass, 24 October 2026.** An independent verifier raised seven issues. Each was checked against the deposited text; all seven were real and are fixed:

1. For an accident before 1 July 2014, the s 11 and s 11A reductions were applied as amended in 2014, though s 46 keeps the earlier Part 3 for those accidents. Those answers are now `outside this encoding` (finding 24).
2. Four pieces of rule logic sat in the seat layers. They are now core functions that the seats call: whether death benefits apply (ss 7, 20), whether Part 3 excludes them, the s 28A(2) last day for a review, and the s 28E(3)(a)/(b) last day for the Tribunal. The core's unused `excludes death benefits` was folded into the new death exclusion function.
3. The s 18BD(4) duty on the Commission was not encoded. It is now a regulative rule, with a seat question giving the last day (finding 26).
4. Finding 22 gave the wrong payment dates. It is corrected, and the 70% week is asserted.
5. The scope lists contradicted each other on Part 8 and left out ss 18BF, 28C and 33. Section 33 is now encoded as an input (finding 25), and finding 21 is corrected.
6. The date helpers disagreed about a 29 February birthday. A week could pay $0 as a result (finding 27).
7. The reg 4M(5) and (6) fields were fixed to false after a death. They are now asked (finding 28). The s 31 comment promised a seat computation that did not exist; the rule now has a form built from the dates.

The questions whose inputs changed are `Are my benefits reduced for no seatbelt or helmet` and `Are death benefits reduced for no seatbelt or helmet` (they now answer a choice, not yes or no), `When does my weekly compensation stop`, `How much weekly compensation do I get this week`, `Which attendant care benefits can I get` (each gains the s 33 inputs), `May death benefits be reduced under s 20A` (gains the reg 4M(5), (6) inputs), `How much does each dependent parent get` (gains the day of the accident), and the funeral, children's weekly and parents' amounts, which now answer a `Death benefit amount`. Any deployment of these seats must be updated under the same name.

## Edition

- **Act:** reprint **REPM022**, as in force at **31 May 2019**, deposited at `../../registers/source-bundle/Motor-Accidents-Compensation-Act-1979-NT-current-reprint-REPM022.txt`. This is the oldest reprint in the NT sample. Its last amendment is the Motor Accidents (Compensation) Amendment Act 2019 (No. 18 of 2019), commenced 31 May 2019. **Later amendments to the Act may be missing** (finding 2).
- **Regulations:** reprint **REPM022R1**, as in force at **28 August 2026**, deposited at `../../../motor-accidents-compensation-regulations-1984/registers/source-bundle/Motor-Accidents-Compensation-Regulations-1984-NT-current-reprint-REPM022R1.txt`.

The two texts are seven years apart. The Regulations are read against the Act as it stood in 2019.

**Figures not in any deposit are inputs:**

- average weekly earnings under s 4 (the ABS full-time adult ordinary time earnings for the Territory, last published before 1 January);
- the maximum weekly amount MA under s 13(2)(a), which the Commission determines each half-year;
- the CPI figures for the reg 3 "(indexed)" caps;
- the day a person reaches pension age (Social Security Act 1991 (Cth) s 23);
- what reg 19(2) of the Traffic Regulations 1999 requires of a driver;
- whether the Commission has extended a time limit on payment for special hardship under s 33, and to what day (finding 25).

The case files use round illustrative figures for these: average weekly earnings of $2,000, MA of $1,500, CPI of 100 and 150. They are not the published figures.

Figures fixed by the Act or the Regulations are constants:

- 85% (s 13(2)(a)); 104 weeks and 2 years (s 13(5)); 15, 21 and the s 14(2) percentages;
- 5%, the s 17(2) table, 208 (s 17(3));
- 25% (s 11); 5.2 and 156 (s 22); 10% (s 23); 156 (s 24);
- 0.08 g per 210 L of breath and 0.08 g per 100 mL of blood, and 4 hours (regs 4A, 4M);
- 6% (regs 5, 6); $1 million and $300,000 (reg 6(4)); 15% (reg 6(2)(c));
- 6 months and 3 years (s 31); 90 days, 30 business days and 28 days (ss 28A, 28B, 28E);
- 1 year, 3 years and 6 years (ss 18BB, 18BD).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `maca-core.l4`, `maca-seat.l4` | `maca-cases-injured.l4` | 193 written, 193 satisfied |
| `maca-core.l4`, `maca-seat-survivors.l4`, `maca-seat.l4` | `maca-cases-survivors.l4` | 85 written, 85 satisfied (including 5 mirror cases) |

The injured person's case file also has 9 `#TRACE`s, each with an `-- expect:` line: four breaches by the claimant, one breach by the Commission (s 18BD(4)), three obligations still pending, and one late request that leaves nothing owed. Each was read and matches its expectation.

`l4 run` on all five files: 0 errors, 0 warnings (2026-10-24, after the fix pass). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A throwaway file of three deliberately wrong assertions was run to confirm that failures are reported, first at the encoding and again in the fix pass (against the new answer types); it was deleted each time. In the fix pass, the pre-fix modules were also run on the verifier's examples. They gave $0 for the week from 28 February 2027 (born 29 February 2012), $93,600 for an impairment lump sum after an accident on 1 May 2013, and "reduced" under s 11 for that accident. That confirmed issues 1 and 6 before they were fixed.

Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seats

**1. The person injured in a motor accident** (`maca-seat.l4`): the "eligible person" while entitled, and "the claimant" once a claim is made. They ask:

- Am I covered?
- Am I excluded, or are my benefits reduced?
- What weekly amount do I get, and until when?
- What lump sum do I get for my impairment?
- Is this treatment covered? Which attendant care can I get?
- Can I take a lump sum instead?
- When must I claim, and when must I ask for a review?
- While I have interim attendant care, by when must the Commission decide on long-term care?

**2. On a death, those Part 5 pays** (`maca-seat-survivors.l4`): the spouse, a dependent child (or whoever asks for the child), a dependent parent, and the person liable to meet the expense of the funeral. They ask:

- Do death benefits apply?
- Am I a spouse, a dependent child or a dependent parent?
- Are death benefits excluded, or may they be reduced?
- How much is the funeral benefit, the lump sum and each share, the children's weekly benefit, and the parents' benefit?
- Can my spouse, permanently in hospital, be treated as having died?
- By when must I claim?

**The Motor Accidents (Compensation) Commission and the designated person get no seat.** They are the scheme's statutory decision makers. Their duties appear only as what the claimant is owed and by when: the s 28B review decision within 30 business days, the claimant's right to go to the Tribunal if it is late, and the s 18BD(4) decision on long-term attendant care before interim care ceases. Their judgments are inputs, answered conditionally: that earning capacity is reduced, the impairment percentage, an emergency, a reasonable excuse, dependency, the s 20A proportion, and an s 33 extension for special hardship.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed: the Regulations set the alcohol presumption (regs 4A, 4M), the impairment guides (reg 4), the vehicles that cannot be registered (reg 4B), the attendant care criteria (regs 4E, 4F) and commutation (regs 5, 6).
- **The actors the text names.** Followed: the injured person, the eligible person, the qualifying person, the claimant, the spouse, the dependent child and parent, the person liable for the funeral, the Commission, the designated person, the Tribunal.
- **Judgments left to others are answered conditionally, as inputs.** Followed; see the list above.
- **The Act's own definitions are worked out from facts.** Followed for motor vehicle, motor accident (s 4A), resident (s 4B), spouse, dependent child, dependent parent and qualifying person (s 20).
- **Borrowed terms are asked as facts.** Registration under the Motor Vehicles Act 1949, a traffic offence, a licence, a terrorist act, workers compensation legislation and pension age are asked. One departure: the age of majority is fixed at 18 (finding 18).
- **One case is one accident**, and for the weekly amount one week.
- **The Act's own terms**, quoted in the comment above each rule, with a plain gloss in each `@desc`.
- **Machinery out:** Part 2 (indemnity), s 38 (indemnity of the Commission), s 40 (conduct of proceedings), the Tribunal's procedure (ss 29-30B), the regulation-making power, and Part 8 Divisions 1 and 2 (ss 43, 44). Part 8 Divisions 3 and 4 (ss 45-49) are in, but only as the dates that limit the encoding.
- **"Must" makes a regulative rule.** Followed, with one departure. Section 28C(2) says the designated person "must give the claimant written notice of the review decision as soon as practicable after making it". That duty has no fixed period, and s 28C(4) says a breach of it does not affect the decision, so it is not a rule of its own. The day the claimant receives the notice is a fact the claimant states, and the s 28E(3)(a) period counts from it.

## Scope

**In:**

- **Definitions:** s 4 (motor vehicle, Territory motor vehicle as a fact, average weekly earnings as an input, spouse, child, dependent child, dependent parent); ss 4A, 4B; s 4C with reg 4 (the AMA Guides, 6th edition, as a fact; the percentage is the Commission's); s 4DA (registered, conditionally registered and unregistered, as facts).
- **Entitlement:** s 7(1)-(3).
- **Exclusions and reductions:** s 9 with reg 4A; ss 9A-9G with reg 4B (as a fact); ss 10, 10A, 10B, 10C, 11, 11A, 11B.
- **Weekly compensation:** s 13(1), (2), (2A), (3) (the amount as an input; see finding 1), (5), (5A); s 14.
- **Impairment lump sum:** s 17.
- **Medical and rehabilitation:** s 18 with reg 4D, at the level of "is it covered".
- **Attendant care, injuries on or after 1 July 2014:** ss 18BA-18BE with regs 4E and 4F, as eligibility tests. The s 18BD(4) duty on the Commission is a regulative rule (finding 26). Schedule 1 is assessed by the specialist's certificate, an input.
- **Death:** ss 20, 20A with reg 4M, ss 21, 22, 23, 24, 37.
- **Commutation:** s 25 with regs 5 and 6.
- **Claims and review:** ss 31, 31A, 28A, 28B, 28C (only the notice from which s 28E(3)(a) counts, as a fact), 28E.
- **Extension for special hardship:** s 33, as the Commission's determination, an input. It reaches the s 13(5)(a) and s 18BD(3) limits (finding 25).
- **Amendment dates that limit the encoding:** Part 8 Divisions 3 and 4, ss 45-49.

**Out:**

- Part 2 (abolition of common law rights, indemnity of owners and drivers).
- s 12 (the Commission's powers, treatment plans and suspension under s 12(7)).
- s 13(4) (suspension for a long hospital stay) and s 13(6) (instalments).
- Attendant care for injuries before 1 July 2014 (ss 18A, 18B, returned as `outside this encoding`).
- s 18BF (attendant care benefits are determined under the regulations and paid to the provider, or to the injured person if the Commission considers it appropriate), with the amounts (reg 4G, Schedule 2) and approved providers (reg 4J).
- s 18C (emergency travel); s 19 with regs 4K, 4L (appliances and building alterations).
- s 28C(1), (3), (5) (the content and effect of the review decision); s 28D; the Tribunal's procedure (ss 29-30B); s 30C; ss 32, 34, 35; s 38; s 40.
- Part 8 Divisions 1 and 2 (ss 43, 44: the 2007 transitional rule and the 2010 transfer to the Board). Every accident s 43 reaches is before 1 July 2014, so it is already outside this encoding.
- The commuted amount itself (finding 17).

The NT levies no land tax and no personal income tax; neither touches this Act.

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here and not in code.

- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`.
  - s 13(7) borrows *pension age* from s 23. That encoding's `What is my pension age, in months` and `Have I reached pension age` give the day this encoding takes as an input.
  - Its compensation recovery questions (ss 17, 1166-1173: `Is my payment a compensation affected payment`, `What is the compensation part of my lump sum`, `By how much is my daily rate reduced for periodic compensation`) say how the weekly compensation and the lump sums here affect a Centrelink payment.
- **Income Tax Assessment Act 1997 (Cth)**, `subjects/au/income-tax-assessment-act-1997/`. Section 13(2)(d) says the weekly compensation is "paid without any deduction for income tax". Whether it is assessable income is Commonwealth law, not answered here.
- **Return to Work Act 1986 (NT)**, `subjects/au/nt/return-to-work-act-1986/` (being encoded in the same run, 2026-10-24).
  - Under s 10A, an injury "compensable under workers compensation legislation" gets nothing here. That is an input, answered by the Return to Work encoding.
  - The Return to Work Act's s 4(2A) takes most journey injuries in motor accidents out of workers compensation, so they fall back into this scheme.
  - Its s 61(2) makes compensation payable under this Act while it is disputed which Act applies (finding 20).
- **Victims of Crime Assistance Act 2006 (NT)**, `subjects/au/nt/victims-of-crime-assistance-act-2006/` (being encoded in the same run). Its s 17 makes a person who "is entitled to a benefit under the Motor Accidents (Compensation) Act 1979 for the injury, regardless of whether the injured person has made a claim" ineligible to apply as a primary victim for the same injury. Secondary and family victims of that act are ineligible too. This encoding's `Am I entitled to motor accident benefits` answers the first half of that test.

## What the Act turns out to say

1. **The s 13(3) formula did not survive conversion.** The deposited text says the Commission "must calculate the amount ... in accordance with the following formula:" and goes straight to "where:", defining only X (the hours, not exceeding 38, the person can work) and MA (the maximum amount). The formula itself is missing. The encoding takes the weekly amount the Commission calculated under s 13(3) as an input, bounded by MA. It does not compute even the fully incapacitated case, because the text does not say what X = 0 gives. The nil cases are kept: s 13(2)(b) (the day of the accident, a week fit for full-time work, a week earning at least MA) and s 13(5)(b), (c) (prison, outside Australia). Asserted.
2. **The Act's reprint is seven years older than the Regulations'.** REPM022 is the Act as at 31 May 2019, the day the 2019 amendments commenced. The Regulations are as at 28 August 2026. An amendment to the Act made after 31 May 2019 is not in the deposit. The encoding also stops where the deposit stops looking back:
   - s 49 keeps the earlier s 13 for accidents before 31 May 2019;
   - ss 46 and 47 keep the earlier Part 3 and ss 18 and 19 for accidents before 1 July 2014.

   Neither earlier text is deposited, so those accidents answer `outside this encoding`. That includes the reductions in ss 11 and 11A, which are part of Part 3 (finding 24). READING: an accident on 31 May 2019 itself "happens after the commencement". Asserted at both boundaries.
3. **There are three different "average earnings".**
   - The lump sums and death benefits use s 4's *average weekly earnings*: the ABS full-time adult ordinary time earnings for the Territory, fixed for each calendar year.
   - The weekly maximum MA is 85% of "the average weekly earnings for all employees' total employment earnings in the Territory", less notional income tax, set by the Commission each half-year. Section 13(2A) disapplies the s 4 definition here.
   - The s 14(1)(b)(iii) student test uses "the average earnings ... of wage earners in the Territory", in the Commission's opinion.

   All three are inputs.
4. **A death overseas can make a "qualifying person" with no benefits.** Section 20(b) defines a qualifying person as a Territory resident who dies in a motor accident "involving a Territory motor vehicle, occurring outside the Territory". It has no "in Australia". Section 7(2)(a), which gives the entitlement, does. A Territory resident killed in New Zealand in a Territory-registered vehicle is a qualifying person, but no death benefits are payable. Asserted.
5. **Alcohol excludes the injured driver, but only reduces the family's benefits.**
   - The s 9(2) presumption, with reg 4A, reaches only s 9(1)(c), that the alcohol contributed. That the driver was over the limit to the extent of an offence (s 9(1)(b)) is still a fact.
   - Section 9 reaches only the driver: a passenger over the limit is not excluded. Asserted.
   - It excludes only weekly compensation and the impairment lump sum.
   - When the drunk driver dies, s 9 does not touch death benefits at all. Section 20A only lets the Commission reduce them, by a proportion it chooses, and never the funeral benefit (s 20A(6)). Asserted as a mirror case.
6. **The s 17(2) table has gaps.** Its rows are "not less than 5% but less than 10%", then 10%, 11%, 12%, 13% and 14%. An assessment of 12.5% is in no row. Read literally, s 17(2) then does not apply ("as shown in Column 1"), and s 17(1A) pays 12.5% of the prescribed amount, more than the 12% paid for 14%. The encoding does not choose: it answers `outside this encoding`, asserted.
7. **The s 22(3) table's rows overlap.** "Spouse and one child" (10% to the child) is also "Spouse and not more than 5 children" (5% to each child). The row that names one child is read to govern. The rows then join up:
   - one child, 10%;
   - two children, 5% each (10% in all);
   - five children, 25% in all;
   - six or more children share 25%.

   Asserted for one, three, five and eight children.
8. **For an unregistered vehicle, the owner who was a passenger is caught without knowing; the owner who drove is not.** Sections 9D(1)(d) and 9E(1)(d) ask whether "the driver knew, or ought to have known, the vehicle was unregistered". There is no such test for an owner who was not driving. An owner-passenger whose registration lapsed unknown to them loses everything but medical, long-term and interim care and appliance benefits. The same owner driving, with no reason to know, keeps everything. Asserted. Sections 9F and 9G are the other way round: they catch an owner, or a driver who knew.
9. **Claiming damages interstate (s 7(3)).**
   - Notice must be given "immediately". READING: the same day; a trace with notice the next day breaches.
   - The repayment of benefits already paid has no period, and is "from damages or compensation (if any) awarded". READING: limited to what is awarded.
   - Only a person entitled "under subsection (2)" can elect: an accident in the Territory leaves no election, and a claim elsewhere does not end an s 7(1) entitlement.

   Asserted.
10. **The young persons' table reaches every unmarried recipient under 21, not only students.** Section 14(2) applies to any person "entitled or deemed to be entitled" to weekly compensation "who has not attained the age of 21 years and is not married". An 18-year-old apprentice on full wages gets 70% of the s 13 amount. Marriage, a de facto relationship or a dependant restores the full amount (s 14(3)). Asserted.
11. **The s 20A reduction has no method.** Section 20A(5) says "the Commission must reduce the benefits in accordance with the regulations". The only regulation is reg 4M, headed "Reduction of benefits for influence of alcohol", and it prescribes only the 0.08 presumption. Nothing says how to reduce. The proportion is the Commission's, and an input.
12. **The order of reductions is not stated.** Section 11B makes the exclusions and reductions apply "cumulatively", but in no order. For the s 22(1)(b) lump sum, the encoding applies them in this order:
    1. s 22(4), the impairment lump sum already paid, as part of the amount otherwise payable;
    2. s 11, 25% of what is left;
    3. s 20A, the Commission's proportion;
    4. s 11A, the other insurance, as an amount, never below nil.

    How an s 11A entitlement is spread over several benefits is not said either: the amount set against each benefit is an input. Asserted ($312,000 to $177,200).
13. **The seatbelt reduction does not reach the dependent parents.** Section 11(3) lists loss of earning capacity, the impairment lump sum and "compensation under sections 22 and 23". It does not list s 24. The parents' question asks nothing about a seatbelt.
14. **The seatbelt reduction does reach the funeral benefit.** Section 20A(6) expressly shields s 22(1)(a) from s 20A, but s 11 has no such shield, and s 11(3)(c) names "compensation under sections 22 and 23 for a death". READING: the funeral benefit is reduced by 25% for an unbelted deceased aged 16 or more. Asserted ($10,400 to $7,800).
15. **The dependent children's weekly benefit has no stated end.** Section 23 pays 10% of average weekly earnings a week "to or for the benefit of each dependent child". READING: it runs while the child remains a dependent child (under 16, or under 21 and a full-time student or handicapped). The encoding gives the weekly amount, not the period.
16. **Commutation for a person moving overseas does not reach post-2014 long-term care.** Regulation 6(1)(c) names "long-term benefits for attendant care services under section 18B". Section 18B is the long-term benefit for injuries before 1 July 2014. Section 18BC, its successor for later injuries, is not named. A person injured after 1 July 2014 can commute weekly compensation and medical costs before leaving Australia, but not long-term care. Asserted, against an accident in 2013.
17. **The 6% discount rate has no method.** Regulations 5(3) and 6(3)(c) say "a discount rate of 6% will be applied". They do not say whether it is applied weekly or yearly, nor over what expected period. The commuted amount is not computed. Who may commute, and the reg 6(4) caps, are.
18. **"The age of majority" is not defined in the Act.** Section 31(3)(d) gives a claimant under age at the accident until "3 years after the date the claimant attained the age of majority". That is 18 under the Age of Majority Act 1974 (NT), which is not deposited. The encoding fixes it at 18. Asserted (a 14-year-old hurt in 2025 has until 20 August 2031).
19. **"Business day" is not defined in the Act.** The Interpretation Act 1978 (NT) is not deposited. For the s 28B review, a business day is taken as a weekday that is not a Territory public holiday, and the claimant counts the holidays. The s 28B(3) extension is added in calendar days after the 30th business day. Asserted (a request on Monday 1 September 2025 is due by 13 October 2025).
20. **A dispute about which Act applies runs the other way in the Return to Work Act.** Section 10A here gives nothing for an injury "compensable under workers compensation legislation". The Return to Work Act's s 61(2) says that while it is disputed whether compensation is payable under that Act or this one, "compensation is payable under the MAC Act until it is determined" otherwise. Its s 61(3) then lets the Commission recover from the employer. This encoding takes s 10A's input as decided; the interim payment belongs to the Return to Work encoding. Not asserted here.
21. **Weekly compensation can run for decades.** Section 13(5)(a) stops it at pension age if the accident was more than 2 years before pension age, and otherwise 104 weeks after the accident. There is no step-down. The two limbs nearly meet: with pension age exactly 2 years after the accident it stops after 104 weeks, 2 days before pension age; with one day more it stops at pension age. Asserted. *Corrected 24 October 2026:* this finding said there was "no other cap". That was incomplete. Section 33 lets the Commission extend the limit for special hardship (finding 25), so the stop day is the s 13(5)(a) day unless the Commission extends it.
22. **A deferred young person is deemed to have lost earning capacity.** Under s 14(1), a child under 15, or a qualifying student, waits until the later of turning 15 and leaving full-time study (or sooner marrying). They are then "deemed to have suffered a reduction in earning capacity", so the Commission's s 13(1) opinion is not needed. Asserted: a 12-year-old (born 15 January 2013) is hurt in 2025 and leaves school on 1 December 2030. The s 14(1) start is 1 December 2030, the later of that day and her 15th birthday. She is 17 from then until she turns 18 on 15 January 2031, so she is paid 60% from 1 December 2030 (the week from 1 December and the week from 6 January 2031, $720 each on a $1,200 figure) and 70% from 15 January 2031 ($840). *Corrected 24 October 2026:* this finding first said she "is paid 60% from January 2031". That was wrong on both counts: payment starts on 1 December 2030, and from 15 January 2031 the rate is 70%. The assertions were right; the week from 1 December 2030 and the 70% week are now asserted as well. READING: the age on the first day of a week governs that week, so a week in which a birthday falls is paid at the earlier age.
23. **Interim attendant care is once only, and closes off short-term care.** Section 18BD(5) allows interim benefits only once for the same impairment. Section 18BB(1)(c) allows short-term benefits only to a person "not ... assessed as eligible for interim or long-term" care. READING: a person who has had interim care for an impairment gets neither again. Asserted.

Findings 24 to 28 come from the fix pass of 24 October 2026. Each corrects the encoding as first committed.

24. **Section 46 reaches the seatbelt and other-insurance reductions.** Section 46(2) keeps "Part 3, as in force before commencement" for an accident before 1 July 2014. The endnotes show s 11 "sub No. 20, 2014, s 8" and ss 11A-11B "ins No. 20, 2014, s 8": both are the 2014 Part 3. The encoding first checked the date only for the Part 3 exclusions, and applied the 2014 s 11 and s 11A to an earlier accident. It now answers `outside this encoding` for an accident before 1 July 2014 in each of these questions:
    - the s 11 question, from both seats;
    - the impairment lump sum;
    - the funeral benefit;
    - the death lump sum;
    - the children's weekly benefit;
    - the parents' benefit. Section 11A reaches "any statutory benefits", so it is caught too, although the verifier did not list it.

    Sections 17, 22, 23 and 24 themselves were not changed in 2014, so an answer that pays nothing still stands for any accident: an assessment under 5%, no spouse or child, or a surviving spouse for s 24. The weekly benefit was never affected, because s 49 already puts accidents before 31 May 2019 outside the encoding. Section 20A is in Part 5, which s 46 does not reach. Asserted at 1 May 2013, 30 June 2014 and 1 July 2014.
25. **Section 33 lets the Commission extend time limits on payment.** It may, "because of special hardship", determine that "the time limits imposed by this Act on the payment of benefits under Part 3, 4 (other than section 18A or 18BB) or 5 may be extended". That reaches the s 13(5)(a) day weekly compensation stops and the s 18BD(3) day interim attendant care ceases. It does not reach the s 18BB year, which it names as an exception. READING: the s 31 limits are on claims, not on payment, so they are not reached. Whether to extend, and to what day, is the Commission's judgment, so both are inputs. An "extension" to an earlier day leaves the limit as it is. Asserted:
    - the 104-week stop day of 8 March 2027, extended to 30 June 2027;
    - the week from 15 March 2027 paid, the week from 28 June 2027 a part week, and the week from 5 July 2027 after the stop;
    - interim care to 1 October 2028;
    - the short-term year unchanged.
26. **Section 18BD(4) puts a deadline on the Commission.** "The Commission must determine whether an injured person in receipt of benefits under this section is eligible for benefits under section 18BC prior to the expiry of the period in subsection (3)." It is now the fifth regulative rule, with `the Commission` as the party, so the duty appears as what the person receiving interim care is owed. A seat question gives the last day. READING: interim benefits "cease to be payable" on the s 18BD(3) day, so the period expires as that day begins, and the last day for the determination is the day before. A s 33 extension of payment does not move the period in subsection (3). Asserted:
    - an adult claiming on 1 April 2025 must have the determination by 31 March 2028 (day 1,095 from the claim; day 1,096 is a breach, traced);
    - for a child born 1 June 2023, by 31 May 2029;
    - for a child born 29 February 2024, by 28 February 2030;
    - nothing is owed for an injury before 1 July 2014.
27. **A 29 February birthday is now the same day in every rule.** `the age of a person born` puts the birthday on 1 March in a common year. The s 14(1) 15th birthday, the s 18BD(3)(a) 6th birthday and the s 31(3)(d) age of majority were worked out instead by adding months, which gives 28 February. So a child born 29 February 2012 had an s 14(1) start of 28 February 2027 while still 14, and the week from that day paid $0 (s 14(2) has no row for 14). The encoding now has one helper for the day a person attains an age, and it agrees with the age function: 1 March in a common year (READING; neither the Act nor the deposited texts say). Periods of months counted from a day still end on the last day of a shorter month. Asserted:
    - the start of 1 March 2027, the week from 28 February 2027 deferred, and the week from 1 March 2027 paid at 40% ($480);
    - interim care to 1 March 2030 for a child born 29 February 2024;
    - a claim limit of 1 March 2029 for a claimant born 29 February 2008, from both seats.
28. **The reg 4M(5) presumption can arise after a death.** Regulation 4M(5) takes the concentration to exceed 0.08 if "the person is required under the Traffic Act 1987 to submit to a breath analysis or provide a sample of blood and fails to do so". Regulation 4M(6) lifts that if the Commission accepts a reasonable excuse. A qualifying person can be required to give a sample, and fail to, before dying. The s 20A question first fixed both facts to "no", with the comment "not asked after a death", and NOTES did not record that departure. It now asks both. Asserted: a driver over the limit who failed to give a blood sample, with no excuse, may have death benefits reduced; with an excuse accepted, and no opinion of the Commission that the alcohol contributed, may not. In the same pass, the core's s 31 comment ("the seat works out the days to the limit") was corrected. No seat question did that, and the case hand-wrote 1,096 days. The rule now also has a form built from the dates with `the days from` (previously unused). The cases assert it at day 1,096 and, for the claimant born 29 February 2008, at day 1,452, with the breach at day 1,097 traced.

## Before relying on it

- **Transcribe the s 13(3) formula** from the authorised PDF reprint of REPM022 into a sidecar, `Motor-Accidents-Compensation-Act-1979-NT-current-reprint-REPM022.formulas.md`, citing the rendering. Then compute the weekly amount from X and MA instead of taking it as an input (finding 1).
- **Check the Act against the register's history listing** for amendments after 31 May 2019, and deposit a newer reprint if there is one (finding 2).
- Deposit the earlier s 13 (before 31 May 2019) and the earlier Part 3 and ss 18 and 19 (before 1 July 2014), for older claims still running.
- Deposit the published figures as dated tables: average weekly earnings for each calendar year, the Commission's MA for each half-year, and the CPI figures for the reg 3 indexation.
- Deposit the Traffic Regulations 1999 reg 19(2) (s 31A), the Interpretation Act 1978 (business days) and the Age of Majority Act 1974 (findings 18, 19).
- An independent test pass (one verifier pass was made on 24 October 2026; its seven issues are fixed, see Method), and a human gate on the readings in findings 6, 7, 9, 12, 14, 15, 18, 19, 22, 23, 25, 26 and 27.
- Deposit the Interpretation Act 1978 (NT), to settle when a person born on 29 February attains an age and when a period "after" a day expires (findings 26, 27).
- **Further work:**
  - attendant care amounts (Schedule 2), and attendant care for injuries before 1 July 2014;
  - s 18C (emergency travel) and s 19 (appliances and building alterations, regs 4K, 4L);
  - s 12(7) (suspension for not complying with a requirement);
  - the commuted amount, once the discount method is settled.

## Licence

The deposited texts are reproduced under the Northern Territory copyright policy of 8 October 1996. **Owner's ruling, 24 Oct 2026 (Michael): the NT terms permit reproduction but are silent on adaptation; as for the Canadian texts, Northern Territory legislation may be quoted in L4 encodings in Commons**, keeping the NT attribution and the unofficial-copy notice. Every module header carries both, and `SOURCE-LICENSE.md` here copies the licence of the Act and of the Regulations.
