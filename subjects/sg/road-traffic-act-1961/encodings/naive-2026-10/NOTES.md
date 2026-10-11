# Road Traffic Act 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, incorporating the Road
Traffic (Miscellaneous Amendments) Act 2025, which restructured ss 64 and 65.

**Checks:** three case files (`rta-cases-driving-offences.l4`, `rta-cases-forfeiture-accidents.l4`, `rta-cases-speeding.l4`), 220 assertions satisfied, 0 errors, 0 warnings.

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
