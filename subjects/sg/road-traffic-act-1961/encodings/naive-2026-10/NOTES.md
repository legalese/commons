# Road Traffic Act 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating the Road
Traffic (Miscellaneous Amendments) Act 2025, which restructured ss 64 and 65.

**Checks:** four case files (`rta-cases-driving-offences.l4`, `rta-cases-forfeiture-accidents.l4`, `rta-cases-speeding.l4`, `rta-cases-demerit-points.l4`), 279 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**34 of the 527 Singapore Acts** deposited here cite it. Its 447,000 characters
cover vehicles, licensing, schools, charges and parking; this row takes the
offences a driver can commit and what follows them.

## What the Act turns out to say

### 1. s 65AA(2) forfeits a vehicle for an offence under a subsection that is not an offence

s 65AA(2): forfeiture follows a conviction for dangerous driving causing death "or
section 26(2) of the Police Force Act 2004 (which offence is committed on or after
1 November 2019)". In the Police Force Act as deposited here (see the
`police-force-act-2004` row), s 26(2) is the police officer's **power to order** a
driver to stop at a barrier; the offence of failing to stop is s 26(5), punished
under s 26(8). Act 21 of 2021 rearranged s 26 with effect from 1 January 2022; s 65AA
was not updated. Read literally, no one can be convicted "under section 26(2)".
Asserted as that pair.

### 2. The 2025 restructuring dropped the base offences from the enhanced-penalty list

s 67A lets a court triple the punishment on a third "specified offence". Since the
2025 amendments, dangerous and careless driving with no harm are s 64(5) and s 65(5).
s 67A(3) lists s 64(1) and s 65(1) only "as in force immediately before" the
amendments, and the new harm offences (ss 64(2) to (4), 65(2) to (4)). **Neither
s 64(5) nor s 65(5) is on the list**, and the deposited text cites "64(5)" nowhere.
The same dangerous driving counts towards enhancement if committed before the
amendment and not if committed after, unless it hurt someone. Asserted.

### 3. Driving without a licence outranks dangerous driving

s 35(3): driving without a licence carries up to **3 years** (6 for a repeat
offender). Dangerous driving that harms no one carries up to 12 months (s 64(5)(a));
careless driving 6 months (s 65(5)(a)). Asserted.

### 4. No minimum disqualification for a sober first offender who kills

s 64(9) and s 65(9) prescribe minimum disqualifications for repeat, serious
(drink-driving) and serious repeat offenders -- up to 15 years, and life on a third
drink-related conviction (s 64(10)). They prescribe **none** for a sober first
offender, whatever the harm: dangerous driving causing death by a first offender
attracts up to 8 years' imprisonment and no minimum disqualification under s 64(9).
(The general disqualification power in s 42 is not encoded.) Where a driver is both
a repeat and a serious offender, (9) does not say which period applies; the encoding
takes the longer. Asserted across twenty driver profiles.

### 5. Lending your car to a drunk friend can cost you the car

s 65AA(1): where a drunk (serious or serious repeat) driver causes death or grievous
hurt, the court "is to" forfeit the vehicle unless the offender is not the owner
**and** used it without the owner's consent. A lent car is used with consent, so it
goes, and there is no residual discretion. Under s 65AA(2), for a sober driver who
kills by dangerous driving, the court may decline for "other good reasons". Asserted.

### 6. The phone offence needs hand, operation and motion

s 65B(1): a driver who "holds in his or her hand" a device and "operates" a function
"while the vehicle is in motion". A cradled phone, a phone used at a red light, and
a smartwatch worn as intended (s 65B(1A)) are all outside it. Asserted.

### 7. After a minor accident, a note may not be enough

s 84(1), (2): after damage with no one at the scene, the driver must take reasonable
steps to tell the owner, and must report to the police within 24 hours **unless** the
owner then contacts the driver. A note left on a windscreen that brings no call does
not discharge the duty to report. Asserted.

### 8. Smaller things worth recording

- **s 67:** drink-driving carries a **minimum** fine of $2,000 ($5,000 and mandatory
  imprisonment on a second conviction), and disqualification of at least 2 years,
  5 on a repeat, life on a third.
- **s 64(11)(b):** two earlier convictions for speeding by more than 40 km/h within
  five years make a driver a "repeat offender" for dangerous and careless driving.
- **s 64(6)(b), (7)(b):** a repeat dangerous driver who kills faces at least 2 years;
  one who causes grievous hurt at least 1 year.

## What would need doing before this is worth anything

- **The prescribed alcohol limit and the rules** were not retrieved.
- **No case law was searched.** Sentencing frameworks for ss 64 and 65 are extensive.
- The general disqualification power (s 42) and speeding (s 63) are now in `rta-speeding.l4` as far as the Act goes; the remaining Parts
  are not encoded.

## Speeding (added 11 October 2026 for REQ-0273)

`rta-speeding.l4` and `rta-cases-speeding.l4` (56 assertions). The question (Jun Hao scenario, event j084): a
motorcyclist caught 25 km/h over the limit on an expressway -- the composition sum, the demerit points, and when the
licence is suspended. **The Act answers the ceiling and the machinery, not the figures.**

1. **The offence and its maximum.** s 63(4) makes it an offence to drive "at a speed exceeding any speed limit imposed by
   or in exercise of powers conferred by this Act". It carries no penalty of its own, so the general penalty in s 131(2)
   applies: a fine of up to **$1,000** or up to **3 months'** imprisonment or both for a first offence; **$2,000** or
   **6 months** for a second or subsequent one. No minimum fine, and no speed bands: 1 km/h and 60 km/h over carry the
   same maximum. Neither the motorcycle nor the expressway changes the punishment; they matter only to which limit applies.
2. **The composition sum is capped at $500.** s 135(1) lets an authorised officer compound an offence "prescribed as a
   compoundable offence" for a sum not exceeding the lower of half the maximum fine and $5,000: **$500** for a first
   offence, $1,000 if the second-offence maximum is the one meant (inference: the Act does not say which maximum applies
   before conviction). The $5,000 limb never bites for speeding. Whether speeding is compoundable and **the actual sum**
   are for rules under s 135(2) and the published scale -- not deposited. Asserted with an illustrative $300.
3. **Points and suspension are wholly in the rules.** s 45(2) to (4) require rules that specify the points for each
   offence, the **suspension threshold**, and the period over which it is counted. Reaching the threshold makes
   suspension *available* ("may", s 45(3)), for up to **5 years** (s 45(1)), after a notice giving at least **4 weeks**
   (s 46(1)); a warning is due at **50%** of the threshold (s 45(5)); only the largest-points offence counts when several
   are committed on one occasion (s 45(7)); points are cancelled at the end of a s 45(1) suspension (s 47(3)) and on a
   court disqualification (s 45(6)); a suspension of a year or more needs a fresh test (s 47A). Points and threshold
   are inputs, asserted with illustrative figures.
4. **A new driver can lose the licence outright.** s 35A: within 12 months of the grant, the Deputy Commissioner may
   *revoke* rather than suspend, on a separate **revocation threshold** fixed by rules; revocation while a new driver
   takes the holder's other licences with it unless he is no longer a new driver on them (s 35A(7A)). Whether Jun Hao is
   a new driver in 2049 is a scenario fact.
5. **The court may disqualify, but need not.** s 42(1) lets a court disqualify for any period on conviction for an
   offence "in connection with the driving of a motor vehicle" (inference: speeding is one). Nothing in the Act makes
   disqualification for speeding mandatory or sets a minimum. Under a year, the licence is suspended for the period;
   a year or more, it is of no effect and a new test is needed (s 43(1)).
6. **25 km/h over does not count towards anything worse.** Speeding feeds the repeat-offender test for dangerous and
   careless driving (s 64(11)(b), s 65(11)(b)) and the enhanced-penalty power (s 67A(2)) only where the excess was **more
   than 40 km/h**. s 67A(2)'s "the offence in respect of which he or she had been previously convicted" is singular
   against the "2 or more" of s 67A(1); read here as at least one earlier conviction over 40 km/h (inference).
7. **Compounding is not wiped clean.** s 139AA lets a court treat an offence compounded on or after 1 November 2019 as an
   aggravating factor in a later sentence. And s 63(4) is in Third Schedule Part 1, so an owner who holds a licence and
   fails to identify the rider is presumed to have been riding (s 81(1B)).

**What needs subsidiary legislation (not deposited):** the expressway speed limit (rules under s 63(1) or a notification
under s 63(2)); the composition rules made under s 135(2), believed to be the Road Traffic (Composition of Offences) Rules,
and the published scale of composition sums; the points rules made under s 45(2) and s 35A(2) (the scheme known as the
Driver Improvement Points System), for the points for exceeding the limit by 25 km/h, the suspension threshold and
its period, and the new-driver revocation threshold. The titles are as recalled, not verified against SSO.

## Composition and demerit points (added 12 October 2026 for REQ-0273)

`rta-demerit-points.l4` and `rta-cases-demerit-points.l4` (59 assertions), from the two rules deposited on 13 October 2026:
the Road Traffic (Composition of Offences) Rules (R 29, in force from 6 September 2023, `RTA1961-R29.txt`) and the Road
Traffic (Driver Improvement Points System) Rules (R 25, in force from 1 January 2026, `RTA1961-R25.txt`). They supply the
figures `rta-speeding.l4` held as illustrative inputs; that module and its cases are unchanged (one pointer line in its header).

1. **The answer, as far as the deposit goes.** 25 km/h over the limit falls in Schedule item (2)(b) (s 63(4), "more than 20
   but not more than 30 kilometres per hour"): **8 demerit points**. They are awarded whether he is convicted or pays a
   composition sum (rule 3(1)(a), (b)), and "shall" leaves no discretion. Speeding under s 63(4) **is compoundable** (R 29 rule
   2(a)). **No composition sum is fixed by the rules**; the only figure is the Act's ceiling, **$500** on a first offence
   (s 135(1), and the inference in the section above about which maximum applies). On a clean record the licence is **not**
   liable to suspension: that needs **24 or more points within 24 months** (rule 4(1)), so 16 more after these 8; after an
   earlier suspension or liability to one, **12 or more within 12 months** (rule 4(2)), until 24 clean months have passed
   (rule 4(3)). Suspension is then *available* ("may"), for **up to 36 months** (rule 4(1), (2)), within the Act's 5-year cap.
2. **The ledger's description is right on the points and thresholds and wrong on one item.** R 25 holds **no new-driver
   threshold**: it takes the meaning of "new driver" from the Road Traffic (New Drivers) Rules (R 32), which is where the
   revocation threshold under s 35A would be. R 32 is not deposited. What R 25 says about new drivers is only that they are
   not eligible for the safe-driving course (rule 3A(1)(a)(i)(A)).
3. **Motorcycle or expressway makes no difference to the points.** Item (1) ("Exceeding speed limit for vehicle", the class
   limit) and item (2) ("on a road") carry identical bands. Item (1) cites "Section 63(1) of the Act", which is a prohibition,
   not the offence-creating subsection (that is s 63(4)); R 29 lists only 63(4). Noted, not resolved.
4. **8 points is the course trigger.** Rule 3A(1)(b)(iii): points bringing a holder to "8 or more demerit points within a
   period of 24 months" oblige the Deputy Commissioner to issue a notice of eligibility for the safe-driving course (4 in 12
   months for a rule 4(2) person), if the other criteria hold -- not a new driver, not liable to suspension, no more than one
   earlier disregard in 10 years and none in 12 months. Completing the course lets the Deputy Commissioner disregard 4 points
   (rule 3A(3), "may"). So Jun Hao's 8 points, on a clean record and not as a new driver, should bring a notice. Asserted.
5. **The zone supplement.** In a school zone, silver zone or "Friendly Streets" zone the Deputy Commissioner may add **2**
   points for speeding, and not more than 2 where zones overlap (rule 3(1A), (1B)). An expressway is unlikely to be any of
   these (inference).
6. **Two notice periods.** Rule 5(1) requires the holder to show cause **within 14 days** of the notice; the Act's s 46(1)
   requires the proposed suspension date to be **at least 4 weeks** after it. Both are encoded; they do not conflict.
7. **Clean year.** Twelve consecutive months without a scheduled offence (suspension and disqualification periods excluded)
   wipe the earlier points for the suspension count (rule 4(5)); rule 4(6), the late award for an older offence, is not
   encoded. The windows run "from the date of the first award" (rule 4(4)); points within the window are inputs here.
8. **Foreign licences.** Rule 7: a prohibition order at 13 points within 12 months of the grant (for 12 months), or 24 within
   24 months (up to 36). Asserted, as the visitor's analogue.

**Still outside the deposit:** the expressway speed limit (rules under s 63(1) or a notification under s 63(2)); the sum
actually offered on composition (no scale is in R 29; presumably an administrative scale -- an inference, nothing deposited says so); the
Road Traffic (New Drivers) Rules (R 32) for the new-driver revocation threshold under s 35A.
