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

## Q&A layer (seat and situations as parameters)

Added 6 November 2026: `rtva-qa.l4` (IMPORTs `prelude` and `rtva-licensing`) and its cases `rtva-qa-cases.l4`. It
follows the graffiti Q&A design (Graffiti Vandalism Act 2016 baseline, D2, D4, D8). `rtva-licensing.l4` and
`rtva-cases-licensing.l4` are unchanged. Every exported question takes `my role` first (`@desc Which of these describes
you`) and answers `does not arise for you`, without reading any other input, for a role it is not about. No exported
question takes a DEONTIC or EVENT input.

**Roles** (`Role`):

| Role | Why | Questions |
|---|---|---|
| `I own a vehicle` | the baseline's seat, as licence holder and responsible person | 14 |
| `I am selling, or have sold, a licensed vehicle` | the baseline's seat as the seller (s 10(1), r 51, Administration Act s 6(2)) | 6 |
| `I am buying, or have bought, a licensed vehicle` | the baseline's seat as the buyer (ss 5, 7(2), 10(2), (6), (7), r 21, r 100, MVTPI s 20(1)) | 10 |
| `I drive or ride a vehicle that is not mine` | new: s 4(2) makes "each person who uses the vehicle on a road" liable, not only its responsible person | 11 |

30 questions in all; several serve two or three roles (the licensing questions, the penalties and CTP). The CEO, the
court and the Insurance Commission are not seats.

**Situation inputs** (one parameter per situation, with an identical name, type and `@desc` wherever it is taken,
checked by script):

| Name | Type | Does not arise when | Taken by |
|---|---|---|---|
| `what the vehicle is` | `Kind of vehicle` (the baseline's) | every value but `a bicycle with an auxiliary motor (an e-bike)` | owner and user: "Is the e-bike a power assisted pedal cycle" (2nd). The two licensing questions take it as an ordinary input; the four offence questions take `the vehicle, as the licensing rules see it` instead (QA1) |
| `my vehicle has been used on a road` | BOOLEAN | FALSE | owner: the s 4(2) offence and the s 4(6) conviction ("Do I commit the unlicensed-vehicle offence as its owner", "As its owner, can I be convicted of the unlicensed-vehicle offence") |
| `I have used the vehicle on a road` | BOOLEAN | FALSE | user: the same two questions ("... as its user", "As its user, can I be convicted ...") |
| `the CEO has issued me a notice to apply for transfer` | BOOLEAN | FALSE | buyer: s 10(6) and s 10(7) |

The seller's questions arise for every seller, and the penalties, charges and CTP for every role they are about, so
they take no situation input.

**Decisions.**

- The baseline's one seat (the owner) is split into owner, seller and buyer, because the Act puts different duties on
  each (s 10(1) and (2)) and the form then asks each only their own. The new seat is the user who is not the owner.
- The baseline's records (`My vehicle`, `The use`, `My transfer application`, `The CEO's transfer notice`) are built from
  plain answers. Fixed placeholders are used where no rule on the question's path reads a field: the GVM in the
  licensing and offence questions (r 15 and s 4(2)-(5) do not read it), and every field but the GVM in the
  infringement question, and but the pedals, EN 15194 and output in the e-bike question.
- Where a situation is the record's own first field (`it was used on a road, and I am its responsible person or I used
  it`; `the CEO has issued me a notice to apply for transfer`), the field is TRUE by the situation's own terms.
- For the owner the use situation reads "while you were its responsible person": the layer, like the baseline, assumes
  the owner is the responsible person (Administration Act s 6(2)) while the vehicle is theirs.
- Answers in the baseline's own types (`Licensing answer`, `CTP answer`) are mapped value by value onto Q&A types, with
  `does not arise for you` added. Dollar answers are `Amount`; the notice periods are `Days`.

- **QA1. The offence questions in a form the site can drop** (fixed 6 November 2026, after verification). The site's
  question form proves that a question does not arise for a role by trying every combination of its open yes/no and
  choice inputs, and gives up past 1 024. The four s 4(2)-(6) questions took the vehicle as the baseline's record (the
  kind, 7 values, and five yes/no facts) and the use as six facts (the licence state, 4 values, and four yes/no facts):
  with the use situation, 28 672 combinations (57 344 with the s 4(6) fact). So the form kept them open for the seller,
  the buyer and the other of owner and user, and for the owner or user when the vehicle had not been used on a road,
  though the code answers `does not arise for you` from the role or the situation alone (verification: 315 such
  states). They now take:
  - `the vehicle, as the licensing rules see it` IS A `The vehicle, as the licensing rules see it` (12 values): a car,
    motor cycle, bus, truck or other self-propelled motor vehicle; a motor vehicle or e-bike built so that it cannot go
    faster than 10 km/h; an agricultural implement towed by a licensed or permitted vehicle; any other trailer; an e-bike
    driven by its pedals that is a pedalec meeting EN 15194; any other e-bike driven by its pedals; an e-bike not driven
    by its pedals; a bicycle without a motor; an electric rideable device; a motorised scooter; a declared electric
    personal transporter; any vehicle being towed by a licensed or permitted tow truck. With the output in watts (a
    number), these are the cases `Must my vehicle be licensed` tells apart: every vehicle towed by a licensed or permitted
    tow truck needs no licence (r 15(2)(b), or it is not a motor vehicle or trailer at all), and so does a self-propelled
    vehicle or e-bike built not to exceed 10 km/h (r 15(2)(c), or as a power assisted pedal cycle).
  - `it was used under a s 13(1) permit or with s 13(2) number plates` (s 4(4)(a) and (b), which the baseline reads only
    as "neither"), and `its use is authorised interstate and no responsible person lives in WA` (s 4(5), which the
    baseline reads only as that conjunction). The licence state and the days since expiry are unchanged.
  `the offence vehicle from` and `the offence use from` build the baseline's `My vehicle` and `The use`, so each answer is
  the baseline's for every vehicle and use the inputs describe. The largest question now has 768 combinations (12 x 4 x
  2 x 2, with the situation and the s 4(6) fact). The two licensing questions keep `what the vehicle is` and the five
  facts (224 combinations), because their answer names the r 15 exception, which the folded value would not always
  pick as the baseline does (an agricultural implement that is also being towed by a tow truck). The owner or user who
  asks both kinds of question is asked the vehicle twice, in two forms. Run on a local jl4-service through the site's form engine (100 random completions
  per question, for each role and each value of each situation input), the layer shows no ground-truth issue.
- **QA2. Names that agree as the site cuts them** (fixed 6 November 2026). The site's engine names each function by its
  first 60 characters (letters, digits, `-` and `_`). "Can I be convicted of the unlicensed-vehicle offence as its
  owner" and "... as its user" agreed in those, so the site ran the owner's question when asked the user's (verification:
  every completion failed for want of the owner's input). They are now "As its owner, can I be convicted of the
  unlicensed-vehicle offence" and "As its user, can I be convicted of the unlicensed-vehicle offence". No two of the
  deployment's 57 functions (30 of the layer, 27 of the baseline) now agree in their first 60 characters (checked by
  script).
- **QA3. The regulations' figures** (checked 6 November 2026, after verification asked). The r 57 rate and $586 cap, the
  r 99(1) $9.70 recording fee, the r 100 $20.50 transfer fee and the r 22 penalty units are not in this Act's deposit,
  which holds only the Act; they are in the regulations' own deposits, named under Sources above
  (`subjects/au/wa/road-traffic-vehicles-regulations-2014/registers/source-bundle/mrdoc_49887.txt`: r 57, for
  a car, "$13.20 plus $29.76 per 100 kg, or part of 100 kg, of tare, subject to a maximum charge of $586.00"; r 99(1)
  "$9.70"; r 100 "$20.50"; and `subjects/au/wa/road-traffic-administration-regulations-2014/registers/source-bundle/mrdoc_49740.txt`:
  r 22, s 4(2) 5 PU, s 10(1) and s 10(2) 2 PU). Re-read there; they agree.

**Not covered for the user.** Whether the user is also a "responsible person" in any other way (Administration Act s 6
beyond s 6(2)), the uninsured-vehicle offence itself (MVTPI s 4(3A), for that Act's baseline), and the driver's own
licence (the Road Traffic (Authorisation to Drive) Act 2008).

**Cases.** `rtva-qa-cases.l4`, generated by `gen_rtva.py` in the session scratchpad (the four offence questions'
cases rewritten for QA1 by `rtva_cases.py`): **252 assertions written, 252 satisfied, 0 errors, 0 warnings** (213
before QA1; 39 added, among them each value of the folded vehicle and use against the baseline on the facts it stands
for). They were 116 content cases (each baseline-seat answer also asserted equal to the
baseline's export on the same facts, in the baseline's own c074 figures), 79 role cases (every question for each role
it is not about, every other input ASSUMEd) and 18 situation cases. `l4 check rtva-qa.l4` succeeds. `l4 run` gives no
diagnostics on `rtva-licensing.l4` or `rtva-qa.l4`, and `rtva-cases-licensing.l4` still gives 43 of 43.
