# Road Traffic (Vehicles) Act 2012 (WA) — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as
advice. There was no earlier encoding of this Act.

**Edition.**

- The Act: the compilation on legislation.wa.gov.au (mrdoc 47806, retrieved
  7 September 2026), deposited at `../../registers/source-bundle/mrdoc_47806.txt`.
  It names no compilation number. Its compilation table ends with the Road Traffic
  Legislation Amendment (Infringement Management Reform) Act 2024 Pt. 4 Div. 6
  (No. 15 of 2024, in force 7 October 2024).
- The Road Traffic (Vehicles) Regulations 2014: version 01-av0-00, current from
  2 October 2026 (mrdoc 49887), deposited at
  `subjects/au/wa/road-traffic-vehicles-regulations-2014/registers/source-bundle/mrdoc_49887.txt`.
  Used: r 3, 15, 16, 21, 30(1), 31(1), 51, 54(1)-(3), 54A, 57, 99(1), 100.
- The Road Traffic (Administration) Regulations 2014: version 00-ay0-00, current from
  9 July 2026 (mrdoc 49740), deposited at
  `subjects/au/wa/road-traffic-administration-regulations-2014/registers/source-bundle/mrdoc_49740.txt`.
  Used: r 4 (the power limit of a power assisted pedal cycle) and r 22 (infringement
  penalties).
- Two Acts the plan did not name are used for a few provisions each:
  - the Road Traffic (Administration) Act 2008 (mrdoc 48196), s 4 ("motor vehicle",
    "power assisted pedal cycle"), s 6 (the "responsible person") and s 7 (PU = $50).
    This Act's s 3(2) says that Act supplies its terms;
  - the Motor Vehicle (Third Party Insurance) Act 1943 (mrdoc 47506), s 4(3A), (3B),
    (8), (8A), s 20(1) and s 21 only: the provisions that tie CTP to the vehicle
    licence, which the seat asks about.

All are encoded as they stand in those versions. No amendment is unwound.

**Checks.** The encoding has one module (`rtva-licensing.l4`) and one case file
(`rtva-cases-licensing.l4`, built by the scratchpad generator
`gen_wa_road-traffic-vehicles-act-2012_baseline.py`). Run with the stable `l4` from
VS Code extension 1.6.98, all 43 assertions are satisfied, with 0 errors and 0
warnings. A deliberately wrong assertion was checked to fail. Every exported decision
carries `@export` and `@desc`.

## Seat

**The vehicle owner.** That is the person Part 2 acts on. The owner applies for the
licence and pays for it, commits the s 4(2) offence when the car is used unlicensed
(as its "responsible person"), and must notify the CEO on a sale or purchase. The
decisions are phrased as the owner would ask them: "Must my vehicle be licensed",
"Is my e-bike a power assisted pedal cycle", "Do I commit the offence of using an
unlicensed vehicle", "What can a court make me pay for using my unlicensed car",
"Within how many days must I notify the CEO", "Must the CEO transfer the licence to
me", "What must I pay to transfer the licence", "Is my vehicle covered by CTP".

How each 2026-10-18 default was applied:

- **The Act, plus the instruments that set its numbers.** Followed. The Vehicles
  Regulations set the classes, the grace period, the minimum age, the charges and
  fees; the Administration Regulations set the e-bike power limit and the
  infringement penalties. Two departures: the Administration Act is used for its
  definitions and the responsible person (this Act's s 3(2) sends the reader there),
  and four provisions of the MVTPI Act are used because the seat asks how CTP
  follows the licence.
- **The actors the text names.** Followed: the CEO, the court, the Insurance
  Commission (through the premium), the new and former owner.
- **A judgment handed to someone else is asked as a fact.** Followed. Whether the
  vehicle meets the prescribed standards, whether the CEO is satisfied where it is
  kept, and whether there was "good reason" (s 10(6)(c), (d)) are inputs.
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed.
  "Light vehicle" (s 3(1)), the days of grace (s 4(3) with r 16, r 30) and "power
  assisted pedal cycle" (Administration Act s 4 with Administration Regulations r 4)
  are worked out. "Electric rideable device" and "motorised scooter" are the Road
  Traffic Code's terms, so they are asked: the Road Traffic Act 1974 baseline works
  out r 3A from a device's specifications. "Heavy vehicle" for r 21 (an MRC over
  4 500 kg, r 12) is asked. The duty (Duties Act 2008) and the CTP premium are dollar
  inputs.
- **One case is the natural unit.** One vehicle, one use on a road, one sale.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. The register, labels,
  inspection orders and regulation-making powers are out.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| **c074** Chloe, 15 Jun 2034, age 31: "A used car: vehicle licence duty, registration, compulsory third party through the Insurance Commission" ("What duty on a $28,000 car; what does the CTP cover?") | `Must my vehicle be licensed`, `Am I old enough to apply for a vehicle licence`, `Must the CEO transfer the licence to me`, `What must I pay to transfer the licence`, `Within how many days must I notify the CEO`, `Have I failed to notify the CEO in time`, `Is my vehicle covered by CTP`, `What is my car's annual vehicle licence charge` | Her car must be licensed. At 31 she is old enough (16, r 21). The CEO must transfer the licence once the s 5(3) conditions hold. The transfer costs $20.50 plus the duty: $790.50 if the duty is the scenario's $770 (the Duties Act 2008 was not read here). She has 14 days to notify the CEO (by 29 June 2034, counted by hand). The car's CTP policy goes with the licence and enures to her as the new owner (MVTPI s 20(1)); no premium is due until renewal. On renewal a 1 400 kg tare (HYPOTHETICAL) costs $429.84 a year, less $6.60 for a 1-year election, plus the $9.70 recording fee and the premium |

The duty figure itself, and what the CTP policy covers, are the Duties Act's and the
MVTPI Act's questions and are left to those baselines.

## Why this scope

The seat asks "Must my car be licensed?". The prompt also asks about an eRideable and
an e-bike, the offence of driving unlicensed, the transfer on a sale, and the CTP
link. So the scope is Part 2 Division 1's operative core:

- **what must be licensed:** s 4(1) with r 15, including the e-bike reading;
- **the offence:** s 4(2)-(6) with the days of grace (r 16, r 30(1)), its penalty and
  the infringement alternative (Administration Regulations r 22);
- **what it costs:** the car charge (r 57), periods (r 31(1), r 54, r 54A), the
  recording fee (r 99(1)) and the transfer fee (r 100);
- **a sale:** the transfer conditions (s 5(3), r 21), the notices (s 10(1), (2)),
  the document handover (r 51), the CEO's notice to apply (s 10(3)(b), (6), (7)) and
  who is the responsible person (Administration Act s 6);
- **CTP:** MVTPI s 4(8), (8A), s 20(1), s 21, and the double-conviction bar (this
  Act's s 4(6), MVTPI s 4(3B)).

Left out:

- s 6 beyond the grace period, s 8 (dishonoured cheques), s 9 (cancellation and
  suspension) beyond treating a suspended licence as not current, s 11 and s 12, s 13
  beyond the permit and trade-plate defences, s 14 to s 19B;
- Parts 3 to 12 (overseas vehicles, mass, dimension and loading, defect and
  improvement notices, container weights, heavy vehicle sanctions);
- charges for motor cycles, trailers, heavy vehicles and special purpose vehicles
  (r 58 to r 67), all exemptions and concessions (r 68 to r 85, including pensioners
  and seniors), direct-debit recording fees (r 99(1A)), examination fees;
- the licence classes (r 33 to r 42) and permits (r 43 to r 47) in detail.

## What the Act turns out to say

1. **A car must be licensed; an eRideable, a motorised scooter, a declared electric
   personal transporter and anything that cannot exceed 10 km/h need not.** r 15(1)
   requires a licence for "a motor vehicle or a trailer"; r 15(2)(c)-(e) exempt the
   others. This agrees with the Road Traffic Act 1974 baseline, which reached
   r 15(2)(e) from the Code's r 3A. Asserted.
2. **The e-bike is not named in r 15(2). The encoder reads a power assisted pedal
   cycle as outside r 15(1).** The Administration Act s 4 "motor vehicle" excludes
   it. The Code's "bicycle", which the Regulations adopt, includes it. The
   Regulations treat bicycles in Part 11, apart from motor vehicles (r 228(c)). But
   the Regulations' own r 3 "motor vehicle" ("a vehicle to be propelled by a motor
   that forms part of the vehicle") could be read to catch it, so this is an
   INFERENCE and the weakest point of the encoding. The power limit, which the Road
   Traffic Act 1974 baseline did not read, is in the Administration Regulations r 4:
   250 W for a pedalec (EN 15194), 200 W for any other. So a 250 W e-bike that is
   not a pedalec is not a power assisted pedal cycle and is read as a motor vehicle
   that must be licensed. Asserted.
3. **Fifteen days' grace, but CTP grace only if you do renew.** s 4(3) with r 16
   means no s 4(2) offence within 15 days after expiry, whether or not the licence is
   later renewed. MVTPI s 21(2) extends the CTP policy over those days only "if the
   vehicle licence is renewed within the period of 15 days"; otherwise s 21(4) makes
   the vehicle uninsured from the day after expiry. So an owner who drives on day 10
   and never renews commits no Vehicles Act offence but drove uninsured (MVTPI
   s 4(3A)). Asserted (both halves).
4. **The fine comes with the unpaid licence.** s 4(2): a fine of 10 PU ($500) "and
   in addition" a further penalty equal to six months' charges. For a 1 400 kg car
   that is $214.92, so $714.92 in all. The encoder reads "charges" as the vehicle
   licence charge, not the recording fee (INFERENCE). For a light vehicle an
   infringement notice of 5 PU ($250) is available; a heavy vehicle's offence is not
   in the r 22 Table. Asserted.
5. **You cannot be convicted twice for one unlicensed, uninsured drive.** s 4(6) of
   this Act and MVTPI s 4(3B) each bar a conviction once the person has been
   convicted or acquitted of the other offence for the same use. Asserted.
6. **The seller has 7 days, the buyer 14.** s 10(1) and (2), each 10 PU, or 2 PU by
   infringement notice. The seller who has notified stops being the "responsible
   person" (Administration Act s 6(2)(b)); one who has not remains liable for the
   car's unlicensed use. Asserted.
7. **The licence and its CTP pass with the car; a transfer costs only the fee and the
   duty.** MVTPI s 20(1): the policy enures to every new owner during its period.
   s 7(2), r 100: a $20.50 transfer fee; s 5(1)(b)(ii): the Duties Act duty. No
   licence charge, recording fee or premium is due on a transfer. Asserted (the fee
   and the CTP; the absence of other charges is a reading of s 7 and MVTPI s 4(8)).
8. **Ignoring the CEO's notice to transfer costs far more than the transfer.**
   s 10(6): 50 PU ($2,500) if no application within 28 days (or longer allowed), and
   s 10(7) adds the transfer fee and the duty. Asserted.
9. **The car charge is capped.** r 57: $13.20 plus $29.76 per 100 kg "or part" of
   tare, at most $586.00, so a car of more than 1 900 kg tare pays the cap. A 1-year
   election takes $6.60 off (r 54A). Asserted.

## What would need doing before this is worth anything

- The e-bike reading (finding 2) wants an authority: a case, a Department of
  Transport statement, or a closer reading of r 3 against the Administration Act.
- The days of grace are counted in whole days from the expiry; the counting rule
  (Interpretation Act 1984 s 61) was not read.
- Whether "a fine of 10 PU" is a fixed amount or a maximum depends on the Sentencing
  Act 1995, which was not read; it is given as the figure the Act sets.
- Suspended, cancelled and void licences are treated as not current for s 4(2), but
  their CTP effect is left to the MVTPI Act baseline.
- The duty and the CTP premium are inputs; the Duties Act 2008 Chapter 5 and the
  Insurance Commission's premium schedule would supply them.
- Concessions (pensioners, seniors, carers), other vehicle classes and direct-debit
  fees are not encoded.
- No independent test pass and no human gate.
