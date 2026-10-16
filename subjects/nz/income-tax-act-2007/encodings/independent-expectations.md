# Independent expectations: Income Tax Act 2007 (NZ), personal income tax

Written from BRIEF.md and the Act's text (as at 4 September 2026) only, before any `.l4` file was opened. Values here are not changed after the encoding was opened.

Conventions:
- Table 1 for 2026-27, built from the Act's thresholds: $0-$15,600 at 0.105; $15,600.01-$53,500 at 0.175; $53,500.01-$78,100 at 0.30; $78,100.01-$180,000 at 0.33; above $180,000 at 0.39.
- Amounts are exact (rational) unless the Act states a rounding rule. The Act states none for the LC 13-LC 15 formula or for table 1, so where a credit period gives a fraction I expect the exact fraction (e.g. 62920/365), not a rounded cents figure.
- "Expected" is my reading of the Act; quoted words are the Act's.

---

## Goal 1: Residence (YD 1, YD 1B)

| id | inputs | expected | provision / words relied on |
|---|---|---|---|
| R01 | permanent place of abode (PPA) in NZ; 0 days present | resident | YD 1(2) "Despite anything else in this section, a natural person is a New Zealand resident if they have a permanent place of abode in New Zealand" |
| R02 | PPA in NZ and also a PPA elsewhere | resident | YD 1(2) "even if they also have a permanent place of abode elsewhere" |
| R03 | no PPA; 184 days present in a 12-month period | resident | YD 1(3) "personally present in New Zealand for more than 183 days in total in a 12-month period" |
| R04 | no PPA; exactly 183 days present | not resident | YD 1(3) "more than 183 days": 183 is not more than 183 |
| R05 | no PPA; 0 days present | not resident | YD 1(3) not met; nothing else applies |
| R06 | no PPA; arrives 1 May 2026 and stays continuously; 184-day test met on 31 Oct 2026 | resident from 1 May 2026 (first of the 183 days, i.e. the first day present) | YD 1(4) "treated as resident from the first of the 183 days" |
| R07 | resident only under (3); absent 326 days in a 12-month period | stops being resident (non-resident) | YD 1(5) "absent from New Zealand for more than 325 days in total in a 12-month period" |
| R08 | resident only under (3); absent exactly 325 days | still resident | YD 1(5) "more than 325": 325 is not more |
| R09 | resident only under (3); leaves NZ, first full day absent 1 June 2027, stays away > 325 days | non-resident from 1 June 2027 (first of the 325 days) | YD 1(6) "treated as not resident from the first of the 325 days" |
| R10 | PPA in NZ; absent 400 days | resident | YD 1(2) "Despite anything else"; (5) only applies to a person "treated as a New Zealand resident only under subsection (3)" |
| R11 | resident only under (3); absent 400 days in the service of the NZ Government | resident | YD 1(7) "Despite subsection (5), a natural person who is personally absent ... in the service, in any capacity, of the New Zealand Government is treated as a New Zealand resident during the absence" |
| R12 | resident only under (3); absent 400 days, not Government service | not resident | YD 1(5) |
| R13 | day of arrival / departure (part day present) | counts as a day present and not a day absent | YD 1(8) "present ... for part of a day is treated as present ... for the whole day; and not absent ... for any part of the day" |
| R14 | person present 183 full days plus one part day (arrival day) in 12 months, no PPA | resident (184 days) | YD 1(3) + YD 1(8) |
| R15 | person away for 325 full days plus departure and return part days | not more than 325 days absent (part days are not absent) - still resident | YD 1(5) + YD 1(8) |
| R16 | non-resident seasonal worker employed under RSE instructions; present 200 days; no PPA | non-resident | YD 1(9) "Despite subsection (3), a non-resident seasonal worker is treated for the duration of their employment under the recognised seasonal employer (RSE) instructions as a non-resident" |
| R17 | RSE worker with a PPA in NZ | resident | YD 1(2) "Despite anything else" prevails over (9), which only displaces (3) |
| R18 | visitor: visit 200 days, 200 days present in 18 months, not resident immediately before, no work, no family scheme, lawfully present, resident abroad; no PPA | non-resident (non-resident visitor) despite >183 days present | YD 1B(2); YD 1(9B) "Despite subsection (3), if a person is a non-resident visitor, they are treated as a non-resident" |
| R19 | as R18 but visit exactly 275 days (arrival and departure each a whole day) and 275 present in 18 months | non-resident visitor - non-resident | YD 1B(2)(b) "275 or fewer days, counting the days of arrival and departure as a whole day each"; (c) "275 or fewer days in total in an 18-month period" |
| R20 | as R18 but visit 276 days | not a non-resident visitor; 276 > 183 so resident under YD 1(3) | YD 1B(2)(b) |
| R21 | visit 200 days but 276 days present in the 18-month period | not NRV; resident | YD 1B(2)(c) |
| R22 | as R18 but was resident immediately before first day present | not NRV; resident | YD 1B(2)(d) |
| R23 | as R18 but works for a NZ resident | not NRV; resident | YD 1B(2)(e)(i) |
| R24 | as R18 but works offering goods or services in NZ / work requires physical presence | not NRV; resident | YD 1B(2)(e)(ii), (iii) |
| R25 | as R18 but partner receives family scheme entitlement | not NRV; resident | YD 1B(2)(f) |
| R26 | as R18 but not lawfully present | not NRV; resident | YD 1B(2)(g) |
| R27 | as R18 but neither resident nor citizenship-taxed abroad | not NRV; resident | YD 1B(2)(h) |
| R28 | NRV with a PPA in NZ | resident | YD 1(2) "Despite anything else"; YD 1(9B) only displaces (3) |
| R29 | NRV starts working for a NZ resident on 1 Sep 2026 (stops being NRV under YD 1B(5) that day); arrived 1 Apr 2026; meets the 183-day test | resident from 1 Sep 2026, not from 1 Apr 2026 | YD 1(9C) "the person is only treated as a resident from the first day the person stops being a non-resident visitor"; YD 1B(5) "stops being a non-resident visitor on the date the cessation occurs" |
| R30 | NRV ceases to be lawfully present (YD 1B(2)(g)); arrived 1 Apr 2026; meets 183-day test | treated as never NRV: resident from 1 Apr 2026 (first of the 183 days) | YD 1B(3)(a) "treated as if they were never a non-resident visitor"; YD 1(9B) "unless section YD 1B(3)(a) applies"; (9C) only covers YD 1B(4) or (5) |
| R31 | NRV ceases to be resident abroad on 1 Oct 2026 (YD 1B(4)); arrived 1 Apr 2026 | resident from 1 Oct 2026 | YD 1B(4); YD 1(9C) |
| R32 | natural person acting as trustee | same tests apply | YD 1(8B) - not expressible as a distinct test (no output differs) |

Ambiguity noted: the "12-month period" in YD 1(3)/(5) is any 12-month period, not the tax year. If the encoding takes a day count as input, the tests just feed counts.

## Goal 2: Taxable income and liability (BC 1-BC 7, Schedule 1 cl 1)

| id | inputs | expected | provision |
|---|---|---|---|
| L01 | assessable income 80,000; deductions 5,000 | annual gross income 80,000; net income 75,000; net loss 0 | BC 2, BC 3, BC 4(1) "the difference is their net income" |
| L02 | assessable 30,000; deductions 30,000 | net income 0; net loss 0 | BC 4(2) "their net income for the year is zero" |
| L03 | assessable 10,000; deductions 15,000 | net income 0; net loss 5,000 | BC 4(3) "the difference is their net loss ... and their net income for the year is zero" |
| L04 | net income 75,000; available tax loss 10,000 | taxable income 65,000 | BC 5 "subtracting any available tax loss ... from their net income" |
| L05 | net income 5,000; available tax loss 8,000 | taxable income 0 (loss subtracted "so far as it extends"; balance carried forward) | BC 5 "under Part I"; IA 4(1)(a) "subtracted from their net income, so far as it extends". Ambiguity: BC 5 alone could give -3,000; Part I limits it, and BC 6(2) makes the liability 0 either way |
| L06 | net income 0; no loss | taxable income 0 | BC 5 |
| L07 | taxable income 0 (filing) | liability 0 | BC 6(1), table 1 |
| L08 | taxable income 10,000 | tax 1,050 | Sch 1 cl 1, table 1 (0.105) |
| L09 | taxable income 15,600 | 1,638 | first band boundary |
| L10 | taxable income 15,700 | 1,655.50 | 1,638 + 100 x 0.175 |
| L11 | taxable income 53,500 | 8,270.50 | 1,638 + 37,900 x 0.175 |
| L12 | taxable income 53,600 | 8,300.50 | + 100 x 0.30 |
| L13 | taxable income 65,000 | 11,720.50 | 8,270.50 + 11,500 x 0.30 |
| L14 | taxable income 78,100 | 15,650.50 | 8,270.50 + 24,600 x 0.30 |
| L15 | taxable income 78,200 | 15,683.50 | + 100 x 0.33 |
| L16 | taxable income 180,000 | 49,277.50 | 15,650.50 + 101,900 x 0.33 |
| L17 | taxable income 180,100 | 49,316.50 | + 100 x 0.39 |
| L18 | taxable income 200,000 | 57,077.50 | 49,277.50 + 20,000 x 0.39 |
| L19 | filing taxpayer, assessable 80,000, deductions 5,000, loss 10,000, no schedular income | liability 11,720.50 | BC 2-BC 6 combined |
| L20 | filing taxpayer with net loss (assessable 10,000, deductions 15,000) | liability 0 | BC 6(2) "zero or negative ... zero" |
| L21 | non-filing taxpayer (e.g. NR seasonal worker), tax withheld 2,100 on income 20,000 | liability 2,100 (not table tax 2,253) | BC 1(1) "the total tax withheld from amounts of income included in the taxpayer's annual gross income" |
| L22 | non-filing taxpayer, tax withheld 0 | liability 0 | BC 1(1) |
| L23 | filing taxpayer, taxable income 50,000 of which 1,000 is schedular income (HC 35 beneficiary income of minors, schedular liability 390) | 390 + tax on 49,000 (7,483) = 7,873 | BC 7(1) "the total of (a) their schedular income tax liability ... and (b) the amount that would be their income tax liability for the year if they had no schedular income"; Sch 1 cl 15 0.39 |
| L24 | two kinds of schedular income: liabilities 390 and 280; other taxable income 20,000 | 670 + 2,408 = 3,078 | BC 7(3) "the total of the amounts calculated for each kind"; tax on 20,000 = 1,638 + 4,400 x 0.175 = 2,408 |
| L25 | filing, schedular liability 390, other taxable income 0 | 390 | BC 7(1)(a)+(b) with (b) = 0 |
| L26 | taxable income $15,600.50 | ambiguous: cl 1 taxes "each dollar" and "taxable income means the number of dollars"; not tested |
| L27 | filing taxpayer with assessable 20,000 deductions 0 loss 0 | liability 2,408 | |

Schedule 1 flat rates (cls 2-7, 15-16), the rate for each class of person:

| id | person / income | rate |
|---|---|---|
| F01 | company (cl 2) | 0.28 |
| F02 | trustee (cl 3) | 0.39 |
| F03 | taxable distribution, non-complying trust (cl 4) | 0.45 |
| F04 | trustee, category A income (cl 5) | 0.28 |
| F05 | trustee of certain funds (cl 6) | 0.28 |
| F06 | trustee of disabled beneficiary trust / estate / lines / de minimis trust (cl 6B) | 0.33 |
| F07 | Maori authority (cl 7) | 0.175 |
| F08 | beneficiary income of minors (cl 15) | 0.39 |
| F09 | beneficiary income of certain close companies (cl 16) | 0.39 |

## Goal 3: Credits, terminal tax and refunds (BC 8, LA 2-LA 7, LC 13-LC 15)

Independent earner tax credit (IETC), full year 2026-27, eligible resident, no exclusions:

| id | net income | expected credit | provision |
|---|---|---|---|
| C01 | 23,999 | 0 | LC 13(4) "if the person's net income ... is equal to or more than $24,000, $520. Otherwise it is zero" |
| C02 | 24,000 | 520 | LC 13(4) |
| C03 | 44,000 | 520 | no abatement below $66,000 |
| C04 | 66,000 | 520 | LC 13(5) "greater than $66,000" |
| C05 | 66,001 | 519.87 | LC 13(5) "13 cents for each complete dollar of the excess" |
| C06 | 66,000.99 | 520 | no complete dollar of excess |
| C07 | 66,001.50 | 519.87 | 1 complete dollar |
| C08 | 67,000 | 390 | 1,000 x 0.13 = 130 |
| C09 | 69,999 | 0.13 | 3,999 x 0.13 = 519.87 |
| C10 | 70,000 | 0 | 4,000 x 0.13 = 520 |
| C11 | 75,000 | 0 (not negative) | LC 13(2) "the positive amount" |
| C12 | 0 | 0 | |

Part-year credit periods (LC 13(6) "number of whole months in the credit period"; brief: x months / 12):

| id | inputs | expected | |
|---|---|---|---|
| C13 | net income 40,000; credit period 6 whole months | 260 | 520 x 6/12 |
| C14 | net income 68,000; 6 months | 130 | (520-260) x 6/12 |
| C15 | net income 40,000; 0 months | 0 | |
| C16 | net income 40,000; 12 months | 520 | |
| C17 | net income 40,000; 3 months | 130 | |

Exclusions (each alone, net income 40,000, full year; expected credit 0):

| id | exclusion | provision |
|---|---|---|
| X01 | receiving a main benefit | LC 13(1)(a) |
| X02 | receiving a veteran's pension | (b) |
| X03 | receiving NZ superannuation | (c) |
| X04 | entitled to and receiving a WFF tax credit | (d) |
| X05 | entitled to WFF but not receiving it | (d) "is not entitled to or is not receiving": AMBIGUOUS. Literal logic (not-E or not-R) would let this person qualify; I read (d) as excluding a person who is entitled to *or* receiving WFF ("not entitled to or receiving"), contrasting with (e)'s deliberate "entitled to and is receiving". Expected: 0. |
| X06 | receiving WFF but not entitled | 0 under my reading (receiving) |
| X07 | partner entitled to and receiving WFF | (e) - 0 |
| X08 | partner entitled to but not receiving WFF | (e) "entitled to and is receiving" - not excluded: 520 |
| X09 | receiving an overseas benefit/pension/super/WFF-equivalent | (f) - 0 |
| X10 | partner receives overseas WFF-equivalent | (g) - 0 |
| X11 | not resident in NZ | (h) "is resident in New Zealand" - 0 |
| X12 | none of the exclusions | 520 |

2024-25 split (LC 14: 1 Apr-30 Jul 2024 = 121 days; LC 15: 31 Jul 2024-31 Mar 2025 = 244 days; tax year 2024-25 = 365 days; brief: x credit period days / days in tax year):

| id | net income, credit period | expected LC 14 part | LC 15 part | total |
|---|---|---|---|---|
| S01 | 40,000, whole year | 520 x 121/365 = 62920/365 | 520 x 244/365 = 126880/365 | 520 |
| S02 | 44,000, whole year | 62920/365 | 126880/365 | 520 (LC 14 abatement starts above $44,000) |
| S03 | 45,000, whole year | (520 - 130) x 121/365 = 47190/365 | 126880/365 | 174070/365 |
| S04 | 50,000, whole year | 520 - 780 < 0 -> 0 (positive amount, LC 13(2)) | 126880/365 | 126880/365 |
| S05 | 67,000, whole year | 0 | (520-130) x 244/365 = 95160/365 | 95160/365 |
| S06 | 23,000, whole year | 0 | 0 | 0 |
| S07 | 40,000, credit period 31 Jul 2024 - 31 Mar 2025 only | 0 | 126880/365 | 126880/365 |

Ambiguity: LC 14/LC 15 do not repeat "positive amount"; I take LC 13(2) as still governing ("the tax credit ... calculated using the formula" replaces only the formula).

Use of credits (LA 2-LA 5, BC 8), natural person, no other tax years:

| id | inputs | expected | provision |
|---|---|---|---|
| U01 | liability 2,000; NR credits 300; PAYE 1,000 | terminal tax 700; refund 0; extinguished 0 | BC 8(3) "the difference is the person's terminal tax"; LA 3 |
| U02 | liability 1,300; NR 300; PAYE 1,000 | terminal 0; refund 0; extinguished 0 | LA 3 "less than"; LA 4 "greater than" - equal case: all used |
| U03 | liability 1,000; NR 300; imputation 400; PAYE 900 | uses NR 300, imputation 400, PAYE 300; terminal 0; refund 600; extinguished 0 | LA 4(1) "first, a non-refundable tax credit ... third, ... imputation credit ... sixth, a refundable tax credit" |
| U04 | liability 200; NR 500; PAYE 1,000 | NR 200 used, 300 extinguished; refund 1,000; terminal 0 | LA 5(2) "A non-refundable tax credit is extinguished"; LA 5(6), LA 6(2)(e) refund |
| U05 | liability 0; NR 520 (IETC); PAYE 400 | extinguished 520; refund 400 | IETC is "a tax credit under subpart LC" - non-refundable (YA 1) |
| U06 | liability 100; imputation 500; no others | imputation 400 remaining - not refunded (carried forward, LE 3); refund 0 | LA 5(4); LE 3 |
| U07 | liability 1,000; imputation 300; PAYE 500 | terminal 200 | BC 8(3) |
| U08 | liability 0; PAYE 1,500 | refund 1,500 | LA 5(6), LA 6 |
| U09 | liability 1,000; no credits | terminal 1,000 | BC 8(3) |
| U10 | liability 500; NR 500 | terminal 0; extinguished 0 | |
| U11 | liability 300; IETC 520 non-refundable; PAYE 400 | IETC 300 used, 220 extinguished; refund 400 | LA 4, LA 5 |
| U12 | WFF credit 2,000 (LB 4) with liability 1,000 and PAYE 1,000 | WFF not used against liability; refunded under LA 7; terminal 0 from PAYE | LD 1(5)-style exclusion; LA 7. Not expressible unless the encoding has an LA 7 input |
| U13 | non-filing taxpayer: liability = withheld 2,100, PAYE credit 2,100 | terminal 0, refund 0 | BC 1(1), BC 8 |
| U14 | supplementary dividend credit remaining | used under LP 3 - not a refund | LA 5(3) - expressible only if input exists |
| U15 | R&D credits (LA 4(1)(d),(e)) | out of scope (companies); not expressible |

## Goal 4: Secondary tax codes (Schedule 2, part A cls 3-9), payment $1,000

| id | code | expected tax | provision |
|---|---|---|---|
| T01 | non-notified | 450 | cl 3 "0.45" |
| T02 | S | 175 | cl 4 "0.175" |
| T03 | SH | 300 | cl 5 "0.300" |
| T04 | ST | 330 | cl 6 "0.330" |
| T05 | SA | 390 | cl 6B "0.390" |
| T06 | CAE | 175 | cl 7 "0.175" |
| T07 | EDW | 175 | cl 7 |
| T08 | NSW | 105 | cl 8 "0.105" |
| T09 | SB | 105 | cl 9 "0.105" |
| T10 | M / ME | not computable from the Act (Commissioner's weekly PAYE table); expect a refusal | cls 1-2 - not expressible as a value test |
| T11 | S code, payment 0 | 0 | |

## Not expressible (to be confirmed against the encoding's inputs)

R32 (trustee capacity), L26 (fractional dollars), U12/U14/U15 unless inputs exist, T10 (refusal is not testable with #ASSERT).

### Recorded after opening the encoding (no expected value above changed)

Not expressible against the encoding's inputs and functions:
- R13-R15: part days are counted by the caller; the encoding takes day counts as inputs, so YD 1(8) cannot be tested.
- R25-R27: `Residence facts` has no input for YD 1B(2)(f) family scheme, (g) lawful presence or (h) residence/citizenship-taxation abroad; the encoding's NRV test checks only (b)-(e).
- R29-R31: no input for the date a person stops being a non-resident visitor, so YD 1(9C) and YD 1B(3)(a) cannot be tested.
- R32 (trustee capacity), L26 (fractional dollars - the encoding floors, fork F1).
- F01-F09: no function for the Schedule 1 flat rates (cls 2-7, 15-16).
- X05/X06: the encoding takes a single boolean "entitled to or receiving a WFF tax credit, or the partner of someone receiving one"; its name adopts my reading of LC 13(1)(d), so the ambiguity is settled by the input, not testable.
- U14 (no concrete numbers), U15 (R&D, out of scope), T10 (REFUSE cannot be asserted).
