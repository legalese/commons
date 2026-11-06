# Road Traffic (Authorisation to Drive) Act 2008 (WA) — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as
advice. It replaces the first-pass encoding `naive-2026-10`, and covers everything
that one did, using the regulations the first pass did not have.

**Edition.**

- The Act: the compilation on legislation.wa.gov.au (mrdoc 47952, retrieved
  7 September 2026), deposited at `../../registers/source-bundle/mrdoc_47952.txt`.
  It names no compilation number. Its compilation table ends with No. 45 of 2024,
  in force 16 November 2024.
- The Road Traffic (Authorisation to Drive) Regulations 2014: version 00-ba0-00,
  current from 1 July 2026 (mrdoc 49701, retrieved 19 October 2026), deposited at
  `subjects/au/wa/road-traffic-authorisation-to-drive-regulations-2014/registers/source-bundle/mrdoc_49701.txt`.
  Its compilation table runs to SL 2026/63.
- The Road Traffic Code 2000, r 17 only: version 05-aa0-00, current from 14 May 2026
  (mrdoc 49388), deposited at
  `subjects/au/wa/road-traffic-code-2000/registers/source-bundle/mrdoc_49388.txt`.

**Checks.** The encoding has one module (`rtad-drivers.l4`) and one case file
(`rtad-cases-drivers.l4`, built by the scratchpad generator
`gen_wa_road-traffic-authorisation-to-drive-act-2008_baseline.py`). Run with the
stable `l4` from VS Code extension 1.6.98, all 70 assertions are satisfied, with
0 errors and 0 warnings. Every exported decision carries `@export` and `@desc`.

## Seat

**The learner and the licensed driver.** They are the person the Act and the
regulations act on: the one who applies for a permit, drives under it, collects
points and loses a licence. The decisions are phrased as that person would ask
them: "Am I old enough to hold a learner's permit", "May this person supervise
me", "May I drive between midnight and 5 am", "How many demerit points does my
speeding carry", "Are these demerit points current", "May I make a section 51
election".

How each 2026-10-18 default was applied:

- **The Act, plus the instruments that set its numbers.** Followed. The Act fixes
  almost no number a driver meets: no ages, no stages, no points. The Regulations
  2014 fix them and are brought in. There is one departure. The speeding points
  come from the Road Traffic Code 2000 r 17, because Regulations r 65(3) makes "that
  number of points" the demerit points. The plan did not name the Code, but it is
  the instrument that sets the number Jake's event (k083) asks for, and it is
  deposited, so it is used.
- **The actors the text names.** Followed: the CEO, a court, the driving
  instructor, the r 43 supervisor, an employer and a parent.
- **A judgment handed to someone else is asked as a fact.** Followed. Examples are
  the CEO's waiver for undue hardship (r 22, r 44(3)), the CEO's written permit
  (r 57), passing the hazard test and the driving assessment (r 16A), a court's
  disqualification, and whether a day falls in a holiday period (r 67).
- **The Act's own definitions are worked out; borrowed terms are asked.**
  Followed. "Novice driver" and its types (s 40, r 4), "provisional licence"
  (r 9), "unlicensed person" (s 18), "experienced driver" (r 11(4)), "dealt with by
  infringement notice" (s 40(1A)) and "current demerit points" (s 48) are all
  worked out from facts.
- **One case is the natural unit.** One drive, one offence, or one licence.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. Left out: the
  regulation-making powers, Part 2 Division 3A, extraordinary licence procedure,
  the register (s 56), interstate recognition and fees.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| **c021** Chloe, 14 Mar 2019, turns 16: a learner's permit, "at what age, and with what conditions?" | `Am I old enough to hold a learner's permit`, `Can I be issued a learner's permit`, `Is my learner's permit in force`, `May this person supervise me`, `Does my learner's permit authorise this drive`, `What is the fastest I may drive on my learner's permit` | 16 (r 44); she must be supervised by an instructor or by someone licensed 4 years (r 43), and accompanied (r 47(3)(a)); 100 km/h at most; the permit runs 3 years but ends when she is licensed |
| **c022** Chloe, 14 Mar 2020, turns 17: a provisional licence | `Am I old enough to hold a driver's licence`, `Have I shown I can drive safely for a car licence`, `Must my licence be provisional`, `What P plates must I display`, `May I drive between midnight and 5 am`, `May I carry these passengers` | 17 (r 15); 50 hours (5 at night), a hazard test at 16½ and 6 months into the permit, then the assessment at 17 (r 16A); provisional until 14 Mar 2022 (r 9); red P plates and no driving from midnight to 5 a.m. for 6 months (r 10, r 36); no passenger limit in 2020 (r 11 began 1 Dec 2024) |
| **d012** Daniel, 15 Oct 2012, turns 16: a learner's permit | `Does this Act govern my authorisation to drive on`, `Is my old permit taken to be a learner's permit under this Act` | No: the Act and the regulations began on 27 Apr 2015; s 66 carries a 1974 Act permit across |
| **k032** Jake, 30 Aug 2023, turns 17: a provisional licence | `Am I old enough to hold a driver's licence`, `What kind of novice driver am I`, `What P plates must I display` | Yes; type 1A until 1 Mar 2024, then green plates |
| **k083** Jake, 19 Jul 2049, 25 km/h over on a motorcycle | `How many demerit points does my speeding carry`, `What is the modified penalty for my speeding`, `Am I dealt with by infringement notice`, `Will demerit points be recorded against me`, `Are these demerit points current`, the s 49 to s 52 decisions, `Am I authorised to drive` | 3 points (6 in a holiday period), 8 PU; recorded when he pays anything; current until 19 Jul 2052; not a novice, so 12 points would bring 3 months or a good behaviour year |

## Why this scope

The seat asked four things:

- when may I drive (the permit, supervision, the provisional stages and their
  conditions);
- what my points do and when my licence goes;
- disqualification as far as the Act states it;
- driving unlicensed.

The scope covers the Act's Part 2 Division 2, Part 3 Division 1, the parts of
Division 2 a driver meets (s 21, s 23, s 24) and Part 4 Divisions 1 to 3. From the
regulations it takes Part 2 Divisions 1, 2 and 5 as far as the provisional stages
go, Part 3, Part 3A, r 55, r 57, and Part 5's points table.

On driving unlicensed, the offence is not here. The offence and its penalty are in
the Road Traffic Act 1974 s 49. The encoding instead answers the question this Act
and the regulations do settle, "Am I authorised to drive". It also covers what the
Act does to someone convicted of driving unlicensed (s 18) and the points it
carries for a type 1A novice (r 65).

Left out:

- s 8 and s 9, the residence and earlier-licence bar on a driver's licence; the
  lives cite s 8, but it is not about age or permits (see finding 3);
- interstate and foreign licences;
- extraordinary licences;
- the alcohol interlock scheme;
- heavy vehicle classes and prerequisites;
- renewal and fees;
- postponement under s 54 and s 55;
- the holiday-period calendar.

## What the Act turns out to say

1. **The Act fixes no driving age; the regulations do.** A learner's permit is
   available at 16, or at 15 years 6 months for a moped only (r 44). A licence is
   available at 17, or 16 for a moped licence (r 15). The CEO may waive either age
   for undue hardship. For a licence, that waiver also needs a parent's written
   consent, or an employer's confirmation if no parent lives in WA (r 22(2)–(4)).
   Asserted.
2. **Daniel's 2012 permit predates the Act.** The Act (other than ss 1, 2) and the
   regulations began on 27 April 2015. A permit issued under the Road Traffic Act
   1974 s 43(1) and in effect the day before is taken to be a s 10 permit (s 66).
   The 1974 Act, which governed in 2012, was not read. Asserted.
3. **Section 8, which every life cites, is not about the permit or age.** It bars
   the grant of a *driver's licence* unless the person usually resides in WA and
   has given up any other licence. A learner's permit is not a driver's licence
   (s 3). The permit is s 10, and the ages are r 44 and r 15. Not encoded beyond
   this note.
4. **A learner who drives without the supervisor is not authorised at all.**
   Speeding is different. r 48(1) ends the authorisation when the condition to be
   accompanied (r 47(3)(a)) is broken. Exceeding 100 km/h only breaches a condition
   (4 PU, r 48(2)), and the learner is still authorised. Asserted.
5. **Who may supervise.** A licensed driving instructor (s 10(2)(a)), a youth
   driver education course instructor, or anyone who has held a licence for that
   kind of driving for 4 years (2 for a moped) (r 43). A provisional licence counts
   towards the 4 years; a learner's permit does not. Asserted.
6. **The permit ends in two ways.** It ends 3 years after issue (still in force on
   the anniversary, s 10(4)). It also ends as soon as the holder is licensed for
   that driving (r 42(3)). Asserted.
7. **The route to a car licence for someone under 25 (r 16A).** It needs:
   - 50 logged supervised hours, 5 of them at night, in a CEO-approved logbook;
   - a hazard perception test at 16½ or older, taken at least 6 months after the
     permit;
   - after that, a practical assessment at 17 or older.

   Chloe's own dates fit exactly: permit at 16, licence at 17. Asserted (her hours
   and test dates are hypothetical).
8. **Provisional means a novice, or under 19.** The endorsement lasts until both
   are behind the holder (r 9). Chloe and Jake, licensed on their 17th birthdays,
   stop being novices and turn 19 on the same day: 14 March 2022 and 30 August 2025.
   A provisional licence is granted for one year at a time (r 37(3), not encoded).
   Asserted.
9. **The first six months are "type 1A".** That status is the regulations' own
   (r 4). It brings:
   - red P plates (green after) (r 36(3));
   - no driving between midnight and 5 a.m., except working, travelling to or from
     work, school or training by the shortest route, leaving promptly, or under
     instruction (r 10);
   - from 1 December 2024, no more than one passenger unless one is an experienced
     driver, the rest are immediate family, or an employer requires it in writing
     (r 11, applying to licences granted before as well, r 94).

   Neither Chloe (2020) nor Jake (2023–24) was subject to the passenger limit.
   Breaking either restriction makes the drive unauthorised. A first offence carries
   2 points (r 65 table, s 49(1) row). Asserted.
10. **Novice thresholds are 4 and 8 points; for everyone else, 12.**
    - Type 1 (under 1 year): 4 points.
    - Type 2 (1 to 2 years): 8 points.

    Either brings 3 months' disqualification starting as early as the next day,
    with no good behaviour option (s 50). The disqualification also cancels a
    provisional licence (s 16(3)). For others, 12 points bring 3, 4 or 5 months
    from the 28th day after the notice (s 49). A non-provisional, non-novice
    holder may instead elect a good behaviour year within 21 days (s 51). Two
    points in that year double the period (s 52). The s 50(2) reading is the
    encoder's: the threshold is set by the novice type at the time of the offence
    that reaches it. Asserted.
11. **Jake's 25 km/h over carries 3 points (6 in a holiday period) and an 8 PU
    modified penalty.** The source is Code r 17(1)(c), adopted by Regulations
    r 65(3). Points are recorded once the notice is "dealt with": on any payment,
    even a part or dishonoured one, or on an order to pay or elect (s 40(1A),
    (1B)). They expire 3 years after the *offence* day (s 48): current on 19 July
    2052, gone on 20 July 2052. The scenario cites the Road Traffic Act 1974 s 59
    for the speeding, but the speeding offences and their points are in the Road
    Traffic Code 2000 (r 13 to r 17). Asserted (the holiday-period answer is an
    inference).
12. **What disqualification does to the licence depends on the licence.**
    - A provisional licence is cancelled by a listed conviction, a court's
      disqualification or a Part 4 disqualification (s 16). For a conviction, the
      disqualification is at least 3 months (s 16(2)). A fines-enforcement
      suspension only suspends it (s 17).
    - A full licence or a learner's permit is only suspended for the length of a
      disqualification (r 53C). The exception is a court disqualification for an
      alcohol interlock offence or a repeat prescribed drink- or drug-driving
      offence, which cancels it (r 53B).

    A licence obtained while disqualified "is of no effect" (s 23). Asserted.
13. **A person without a licence who would get a provisional one is disqualified.**
    Conviction of driving without authorisation (RTA s 49(1)(a)) or of a listed
    offence disqualifies them, for at least 3 months (s 18). Asserted.
14. **Removing a long disqualification.** Only a court disqualification of more
    than 3 years can be removed (s 24). The application may be made after 3 years
    (up to 6 years' disqualification), after half the period (up to 20 years), or
    after 10 years (longer, or permanent). Asserted.

## What would need doing before this is worth anything

- Read the Road Traffic Act 1974 s 49 for the offence of driving without
  authorisation and its penalty, and the 1974 Act as in force in 2012 for Daniel's
  permit (d012).
- Unwind the regulations to the edition in force on each life date. The encoding
  uses the July 2026 version throughout. Only r 11 carries its start date. r 10
  and r 65 were also amended by SL 2024/237 (1 December 2024), and what they said
  before was not read.
- Encode the r 67 holiday-period calendar, and postponement under s 54 and s 55.
- Encode s 8 and s 9 (grant of a licence: residence, earlier licences, identity),
  interstate recognition, and heavy vehicle classes.
- The dollar value of a penalty unit is not in these instruments.
- No case law or Department of Transport guidance was searched.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026 (batch qa13), on the pattern of the Graffiti Vandalism Act 2016 encoding's `gva-seat.l4` (its
design D2, D4 and D8). The layer is `rtad-qa.l4`, with cases in `rtad-qa-cases.l4`. It imports `prelude`, `daydate`
and `rtad-drivers`; `rtad-drivers.l4` and `rtad-cases-drivers.l4` are unchanged. Every exported question takes
`my role` first (`@desc Which of these describes you`) and answers `does not arise for you`, reading nothing else, for
the role it is not about. Every answer type carries that value: `Yes or no`, and `Penalty units`, `Demerit points`,
`Months`, `Speed`, `Date answer`, with four wrappers round the baseline's own answer types (`Permit answer`,
`Novice answer`, `Plates answer`, `Licence answer`). No exported question takes a DEONTIC or EVENT input.

### Roles

- `I am learning to drive, or hold a driver's licence`: the baseline's seat. Its 35 questions are the baseline's 35
  exports, each calling the baseline function and wrapping its answer. Where its situation holds, each answer is the
  baseline export's.
- `I supervise a learner driver, or ride with a new driver`: 8 questions. They cover who may supervise (s 10(2),
  r 43(2)), whether the learner is authorised with me (r 47(3)(a), r 48(1)), the learner's 100 km/h limit (r 47(3)(b)),
  and whether my hours count towards the 50 logbook hours (r 16A(2)(a), (b)). They also cover the L plates of r 49(3)
  (my duty as the person in charge of the vehicle, and its 2 PU fine) and of r 49(4) (when I may drive with L plates
  up), and whether I am an "experienced driver" who lifts a type 1A novice's passenger limit (r 11(3)(a), (4)). They
  use the baseline's rules: `May this person supervise me`, `Does my learner's permit authorise this drive`, and
  `May I carry these passengers`, run for a type 1A novice on 1 December 2024 with two passengers, so that only my
  years decide it. Two helpers are added in the layer: `the supervisor I am`, which maps my standing to the baseline's
  `Supervisor`, and r 49(4)(b).
- Not seats: the CEO, the police and the courts. The employer and the parent are not seats either. They give the
  documents of r 11(3)(c) and r 22(3), (4), but the regulations put no duty on them that they would ask about.

### Situation inputs

Each is a BOOLEAN, placed second, straight after `my role`. FALSE gives `does not arise for you`, and nothing else is
read. Each has one name and `@desc` in all its questions (checked by script).

| Input | Role | Questions that take it |
|---|---|---|
| `I hold a learner's permit` | driver | 5: permit in force, may this person supervise me, does my permit authorise this drive, fastest on a permit, fine for a permit condition |
| `I hold a driver's licence` | driver | 5: novice type, provisional, P plates, midnight to 5 a.m., passengers |
| `I have committed, or am said to have committed, a traffic offence` | driver | 9: speeding points, modified penalty, Road Traffic Act offence points, dealt with by infringement notice, registry jurisdiction, points recorded, points current, s 49 months, s 50 novice notice |
| `I have been given a demerit points notice` | driver | 2: earliest start of the disqualification, the s 51 election |
| `I have made a good behaviour election` | driver | 2: broken election, its doubled period |
| `I have been convicted of a driving offence, or disqualified` | driver | 5: s 23, what happens to my licence (s 16, 17, r 53B, 53C), the s 16(2) period, s 18, s 24 |
| `I am the person in charge of the vehicle the learner drives` | supervisor | 2: must I see L plates are displayed, the r 49(3) fine |

These driver questions take no situation input, since they arise in every situation of the role: s 2, s 66, the two
learner's permit questions (r 44-46), the two licence questions (r 15, r 22, r 16A), and authorisation to drive at all
(r 35(1)). Nor do the supervisor's other six.

### Decisions

- **Q1. The situations follow what the text ties each rule to.** These are the permit (s 10, Part 3), the licence
  (r 9, 10, 11, 36), the offence (Part 4), the notice (s 49-51), the election (s 52), and a conviction or
  disqualification (s 16-18, 23, 24). Getting a permit or licence arises for anyone, including a licence holder learning
  a new class, so it takes none. The baseline's s 18 and s 51 questions also read whether I hold a driver's licence.
  They take the same input, `I hold a driver's licence`, with the same type and `@desc`, so the form asks it once; there
  it is an ordinary input after their own situation, not a gate: s 18 is about someone who does not hold one.
  (Until the independent check it was a separate input, `I hold a driver's licence now`, so the form asked it twice.)
- **Q2. Shared non-situation inputs were made identical,** so that a form merging by name cannot mix them. `the day` is
  "The day the question is about" throughout. The baseline's two `months held` texts became one. `the drive` of r 35(1)
  became `my drive`, since its type (`My drive`) differs from the learner's `the drive` (`My learning drive`).
  `provisional` has one text.
- **Q3. A person in charge of the vehicle (r 49(3)) is a borrowed term,** and is asked as a fact (the 2026-10-18
  default). The supervisor's two r 49(3) questions answer on the situation alone: yes, and 2 PU.
- **Q4. r 16A hours, moped:** r 16A is for a car (or restricted motor cycle) licence, so the hours question passes
  "not a moped" to r 43, and the 4-year rule applies.

### Not covered for the supervisor

The supervisor's blood alcohol limit and any offence of supervising while impaired (Road Traffic Act 1974; not
deposited). Whether a provisional licence counts towards the 4 years is answered as the baseline reads r 43(3) (an
Australian driver licence, which a provisional licence is). r 49(1) as it applies to the learner, and the modified
penalties of r 49 (1 PU). A youth driver education course instructor's own conditions.

### Checks

- `l4 run rtad-qa.l4`, `l4 run rtad-qa-cases.l4`, and the baseline's `rtad-drivers.l4` and `rtad-cases-drivers.l4`
  (unchanged): 0 errors and 0 warnings. `l4 check rtad-qa.l4` succeeds.
- `rtad-qa-cases.l4`: 217 assertions, 217 satisfied. They break down as 43 asking each question for the role it is not
  about, with every other input ASSUMEd, and 30 asking each situation question with its situation FALSE (28 for the
  driver, 2 for the supervisor), every later input ASSUMEd. The other 144 are in the role and situation that hold, and
  35 of them check the answer against the baseline export's own answer on the same facts. With the baseline's 70, the
  encoding has 287 assertions.
- A parameter script (scratchpad `qa/b13/check_params.py`) listed the 43 exports. It found `my role` first in each,
  each situation input second and identical in name, type and `@desc`, and each situation's role branch reading it
  first. It found no DEONTIC or EVENT input, and no shared input with two types or texts.
- Limit (graffiti finding 31): the baseline reads `Supervisor`, `Night purpose`, `How I am disqualified`, `What I was
  convicted of` and `How my offence ended` through OTHERWISE, so an ASSUMEd value of those types that is read is not
  caught. The situation inputs are all BOOLEAN and are caught, and the layer's one enumeration helper
  (`the supervisor I am`) lists every value.

### After the independent check (6 Nov 2026)

- **r 11(4)(a) was not asked (fixed).** The experienced-driver question took only the years held, so a passenger now
  disqualified, or not licensed for the novice's class, but with 4 years or more behind them got yes. r 11(4) needs
  both: "(a) is authorised to drive a motor vehicle of the class that the novice driver is authorised to drive; and
  (b) has held that authorisation ... at least 4 years". The baseline's `My passengers` carries only (b), so the
  question now takes `I am authorised now to drive the new driver's class of vehicle` (BOOLEAN) before the years:
  FALSE gives no; TRUE gives the baseline's answer on the years, as before. One case added (FALSE with 10 years: no).
- **The same fact under two names (fixed).** The s 18 and s 51 questions took `I hold a driver's licence now`, and the
  licence questions `I hold a driver's licence`. They now share `I hold a driver's licence`, with one type and
  `@desc` (see Q1). The cases are positional and did not change.
- **The jl4-service build rejects the deployment (not changed).** That build's own `daydate` library defines
  comparisons that clash with the baseline's `is on or after` (`rtad-drivers.l4`, defined on `Day` from the stable
  `daydate`). The stable l4 1.6.98 gives 0 errors, and the baseline's rules may not be changed by this layer. The
  verifier deployed with the stable `daydate.l4` bundled, which is the fix on the service side.
- Assertions: 217 in `rtad-qa-cases.l4` (was 216), 287 with the baseline's 70, all satisfied; 0 errors, 0 warnings.
