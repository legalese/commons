# Road Traffic Act 1974 (WA) — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as
advice. There was no earlier encoding of this Act.

**Edition.**

- The Act: the compilation on legislation.wa.gov.au (mrdoc 48198, retrieved
  7 September 2026), deposited at `../../registers/source-bundle/mrdoc_48198.txt`.
  It names no compilation number. Its compilation table ends with the Towing
  Services Act 2024 (No. 37 of 2024, in force 10 January 2025).
- The Road Traffic Code 2000: version 05-aa0-00, current from 14 May 2026
  (mrdoc 49388, retrieved 19 October 2026), deposited at
  `subjects/au/wa/road-traffic-code-2000/registers/source-bundle/mrdoc_49388.txt`.
- The Road Traffic (Vehicles) Regulations 2014: version 01-av0-00, current from
  2 October 2026 (mrdoc 49887), deposited at
  `subjects/au/wa/road-traffic-vehicles-regulations-2014/registers/source-bundle/mrdoc_49887.txt`.
  Only r 15 is used.
- The Road Traffic (Administration) Regulations 2014: version 00-ay0-00, current from
  9 July 2026 (mrdoc 49740), deposited at
  `subjects/au/wa/road-traffic-administration-regulations-2014/registers/source-bundle/mrdoc_49740.txt`.
  Only r 23 and r 24 are used.
- Two instruments the plan did not name are used for one or two provisions each:
  - the Road Traffic (Authorisation to Drive) Regulations 2014, version 00-ba0-00
    (mrdoc 49701), r 55 and r 65 only;
  - the Road Traffic (Administration) Act 2008 (mrdoc 48196), s 4 and s 7 only.
    This Act's s 5 says that Act supplies its terms, and s 7 sets the penalty unit
    at $50.

All are encoded as they stand in those versions. No amendment is unwound.

**Checks.** The encoding has one module (`rta-road.l4`) and one case file
(`rta-cases-road.l4`, built by the scratchpad generator
`gen_wa_road-traffic-act-1974_baseline.py`). Run with the stable `l4` from VS Code
extension 1.6.98, all 68 assertions are satisfied, with 0 errors and 0 warnings.
Every exported decision carries `@export` and `@desc`.

## Seat

**The rider and the driver.** That is the person the Act, the Code and the
regulations act on: the one who rides the eRideable on the footpath, is caught
speeding, drives without a licence or after drinking, and is fined, given points or
disqualified. The decisions are phrased as that person would ask them: "Is my device
an eRideable", "May I ride my eRideable here", "What is the fastest I may ride my
eRideable here", "What is my speed limit", "How many demerit points does my speeding
carry", "Am I driving at a reckless speed", "What is the most I can be fined for
driving unlicensed", "Which blood alcohol offence do I commit".

How each 2026-10-18 default was applied:

- **The Act, plus the instruments that set its numbers.** Followed, with two
  departures. The rider's questions are answered almost entirely by the Code, so the
  Code is brought in for the eRideable rules, the speed limits and the speeding table.
  The Act's s 5 hands its definitions to the Road Traffic (Administration) Act 2008,
  so s 4 and s 7 of that Act are used for "motor vehicle", "power assisted pedal
  cycle" and the dollar value of a PU. The Authorisation to Drive Regulations r 55 and
  r 65 are used because they settle two things for Jake's eRideable: no licence is
  needed, and no demerit points apply.
- **The actors the text names.** Followed: the court, the police, the CEO (helmet
  exemption) and the Minister (other approved eRideable dimensions).
- **A judgment handed to someone else is asked as a fact or given as a range.**
  Followed.
  - Whether driving was "dangerous" or "without due care" is the court's judgment. It
    is the premise of the penalty questions, never decided here.
  - The sentence is given as the range the court must stay within: the most and
    least fine, the longest imprisonment, the shortest disqualification.
  - The CEO's medical exemption, the Minister's approval of other dimensions,
    "built-up area" and the holiday period are asked as facts.
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed:
  - "electric rideable device" (Code r 3A) is worked out from the device's wheels,
    motor, brakes, top speed, size, mass and pedals;
  - "above the speed limit" (s 49AAA), "circumstances of aggravation" (s 49AB),
    "default speed limit" (Code r 3) and the speed limit (Code r 11, r 13) are worked
    out;
  - "novice driver" is asked: it is the Authorisation to Drive Act's term, worked out
    in that baseline.
- **One case is the natural unit.** One ride, one drive, or one offence.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. Left out: testing and evidence
  (s 65 to s 73), impounding and confiscation, road closures, towing, and the
  regulation-making powers.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| **k042** Jake, 14 Jul 2027, age 20: "On the footpath at 10 km/h, which is lawful; then on a 60 km/h road, which is not: an infringement" ("Where may an eRideable be ridden?") | `What kind of device am I riding`, `Am I old enough to ride an eRideable`, `May I ride it without a driver's licence`, `Does my eRideable need a vehicle licence`, `May I ride my eRideable here`, `What is the fastest I may ride my eRideable here`, `What is the modified penalty for riding my eRideable on this carriageway`, `How many dollars is this many penalty units`, `How many demerit points does my speeding carry` (on an eRideable) | His e-scooter (HYPOTHETICAL specifications) is an eRideable. He is old enough (16, r 228), and needs no licence and no registration. On the footpath he may ride at 10 km/h, which is the limit, not over it. On a 60 km/h carriageway he may not ride at all (r 210B): 2 PU, $100, no demerit points. He may cross it by the shortest safe route |
| **k083** Jake, 19 Jul 2049, age 42: "Motorcycle, 25 km/h over: an infringement and demerit points" | `What is my speed limit`, `By how many km/h am I above the speed limit`, `How many demerit points does my speeding carry`, `What is the modified penalty for my speeding`, `Am I driving in circumstances of aggravation`, `Am I driving at a reckless speed` | 105 km/h in an 80 zone (HYPOTHETICAL) is 25 over: 3 points (6 in a holiday period) and 8 PU, $400 (Code r 17). That is not aggravated (which needs 30 over, s 49AB(1)(b)) and not a reckless speed (which needs 45 over or 155 km/h, s 60A) |

## Why this scope

The seat asks "Where may I ride, and what does speeding cost me?". The brief also
asks for this Act's own offences that the events touch: driving without a licence,
dangerous driving, and drink-driving as far as needed.

The scope covers:

- **eRideables:** the definition (Code r 3A), who may ride and how (r 5, r 212(5),
  r 223B, r 228), where (r 210B, r 215, r 218, r 218A), how fast (r 15), and licences
  and points (ATD Regulations r 55, r 65(4); Vehicles Regulations r 15);
- **speed:** the speed limit (Code r 11, r 13), the speeding table (r 17), the court
  maximum (r 9(2)), reckless speed and its penalties (s 60A, s 60B), and aggravation
  (s 49AB);
- **this Act's offences:** driving without authorisation (s 49 with Administration
  Regulations r 23), dangerous and careless driving (s 61, s 62), and the four
  blood-alcohol offences with their penalty tables (s 64, s 64AA, s 64A, s 64AAA).

Left out:

- s 59 to s 59B (driving causing death or harm), s 60's reckless manner except its
  penalties, and s 63 (under the influence);
- drugs (s 64AB to s 64D) and testing and evidence (s 65 to s 73);
- police disqualification (s 71C) and impounding;
- the Code's wider eRideable and bicycle rules (lights, lanes, hook turns, keeping
  left, giving way on a path, r 229's careless or drunk riding);
- bicycles and power assisted pedal cycles beyond telling them apart from an
  eRideable;
- school zone hours and the holiday-period calendar;
- paying or contesting an infringement notice (Fines, Penalties and Infringement
  Notices Enforcement Act 1994).

## What the Act turns out to say

1. **The lives cite s 59 for speeding, but s 59 is dangerous driving causing death
   or grievous bodily harm.** Ordinary speeding is an offence against the Road Traffic
   Code 2000 (r 11 to r 16), with the points and modified penalties in r 17. Jake's
   25 km/h over carries 3 points (6 in a holiday period) and 8 PU, which is $400.
   These are the same figures, under the same decision names, as the Authorisation to
   Drive baseline. Asserted.
2. **This Act's own speeding offence is "reckless speed" (s 60A).** It means 155 km/h
   or more anywhere, or 45 km/h or more over the limit. A first offence carries a fine
   of 120 PU or 9 months' imprisonment, and at least 6 months' disqualification. A
   third offence brings permanent disqualification. Escaping police makes it a crime:
   5 years, at least 6 months of it not suspended (s 60B). At 30 km/h over, any
   Division 1 offence is committed "in circumstances of aggravation" (s 49AB(1)(b)).
   Asserted.
3. **The eRideable rules are in the Code, not the Act or the Vehicles Regulations.**
   The Vehicles Regulations only borrow the Code's r 3A definition. An eRideable must:
   - be electric;
   - be for one person;
   - have brakes;
   - do no more than 25 km/h on its motor;
   - be no more than 1 250 × 700 × 1 350 mm and 25 kg, unless the Minister approves
     other limits;
   - have **no pedals**.

   The scenario's prose calls Jake's device an "e-bike". If it has pedals it is not an
   eRideable (r 3A(3)(d)). It may then be a power assisted pedal cycle, which is a
   "bicycle", and none of the eRideable rules below would apply to it. Asserted.
4. **The footpath at 10 km/h is lawful, and the 60 road is not.** Nothing in the Code
   forbids an eRideable on a footpath. r 15(3) caps it at 10 km/h ("exceeding 10
   km/h"), so 10 is within the limit. r 210B(1) forbids any carriageway with a limit
   over 50 km/h. The modified penalty is 2 PU ($100), or 10 PU above 70 km/h. (r 210B
   was last amended by SL 2026/66, listed at 13 May 2026; what that amendment changed
   was not read.) There are exceptions for crossing by the
   shortest safe route and for going round an obstruction. On roads of 50 km/h or
   less, and on shared and bicycle paths, the cap is 25 km/h. A lower signed limit on
   a carriageway governs, by r 15(1). Asserted.
5. **An eRideable needs no licence and no registration, and carries no demerit
   points.** The sources are ATD Regulations r 55(2)(h), Vehicles Regulations
   r 15(2)(e) and ATD Regulations r 65(4). So Jake, riding without a licence, does not
   commit s 49. His r 210B infringement costs money but no points. Asserted.
6. **Yet for this Act an eRideable appears to be a "motor vehicle".** This Act takes
   the Administration Act s 4 meaning: "a selfpropelled vehicle ... not operated on
   rails", excluding only a power assisted pedal cycle. The Code's own narrower
   definition is for the Code alone. ATD Regulations r 55 and r 65(4) also call an
   eRideable a motor vehicle. If that is right, drink-driving (s 64 to s 64AAA) and
   dangerous or careless driving (s 61, s 62) reach the eRideable rider. This is an
   INFERENCE from the definitions; no case was searched. Asserted as encoded.
7. **Driving without authorisation (s 49) has three tiers.**
   - **Ordinary** (never licensed, licence lapsed or surrendered): 6 PU, or 12 PU for
     a subsequent offence. The infringement penalty is 2 PU, or 4 PU for a type 1A
     novice driving between midnight and 5 a.m. or over the passenger limit
     (Administration Regulations r 23).
   - **Lost the licence under penalty enforcement laws:** 4 to 30 PU and up to
     12 months, with discretionary disqualification.
   - **Refused, disqualified, cancelled or suspended:** 8 to 40 PU and up to
     12 months (20 to 80 PU and 18 months for a subsequent offence), and the court
     *must* disqualify for 9 months to 3 years. No infringement notice is available.

   Arrest without warrant is allowed only in the last two tiers (s 49(3)). Asserted.
8. **Drink-driving has four thresholds.**
   - **Novices and others listed in s 64A(2), or the vehicles in s 64A(5)** (a bus
     with passengers, hire passengers, 22.5 t GCM): any alcohol is an offence
     (s 64AAA: 8 to 15 PU, infringement 8 PU), and 0.02 or more adds at least
     3 months' disqualification (s 64A).
   - **Everyone, at 0.05:** a first offence is at most 25 PU, with no compulsory
     disqualification and an infringement penalty of 20 PU (s 64AA, r 23).
   - **Everyone, at 0.08:** the s 64 table sets a minimum fine and minimum
     disqualification by band and by first, second or later offence, from 15 PU and
     6 months up to 48 to 90 PU and 30 months.

   Asserted.
9. **Dangerous driving (s 61).** A first offence carries 60 PU. A subsequent one
   carries 120 PU or 9 months, and at least 12 months' disqualification. Escaping
   police raises it to 720 PU or 3 years, with at least 2 years' disqualification.
   Earlier offences against s 59, 59A, 60 or 60A count as earlier s 61 offences
   (s 61(4)). Reading the "in any event" disqualification as attaching only to a
   subsequent offence is the encoder's. Careless driving is 30 PU, or 6 PU on an
   infringement notice (s 62, r 23). Asserted.
10. **A PU is $50** (Administration Act s 7(b)). A Code offence in court is capped at
    64 PU, or 96 PU for a subsequent offence (Code r 9(2)). No infringement notice may
    be given to a child under 14 (Code r 5). Asserted.

## What would need doing before this is worth anything

- Ask the scenario whether Jake's device has pedals. If it is a power assisted pedal
  cycle, encode the bicycle rules instead, and read the prescribed power in the
  Vehicles Regulations.
- Unwind the Code to the edition in force on 14 July 2027 and 19 July 2049. This uses
  the May 2026 version. r 210B was last amended by SL 2026/66; read what it changed.
- Encode the holiday-period calendar (ATD Regulations r 67), school zone hours,
  s 59 to s 59B, s 63 and the drug offences, impounding, and police disqualification
  (s 71C).
- Test the inference that an eRideable is a "motor vehicle" for this Act's offences
  against case law and Department of Transport guidance.
- Encode the Fines, Penalties and Infringement Notices Enforcement Act 1994 Part 3,
  which the k042 event also cites.
- No case law was searched.
