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
