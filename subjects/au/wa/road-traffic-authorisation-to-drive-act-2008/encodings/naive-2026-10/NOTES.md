# Road Traffic (Authorisation to Drive) Act 2008 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 47952,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_47952.txt`. The deposit names no compilation
number. Its compilation table ends with the Road Traffic (Authorisation to Drive)
Amendment (Driving Restrictions) Act 2024 (No. 45 of 2024, in force 16 November 2024);
the only reprint listed is Reprint 1 as at 3 July 2015. The uncommenced provisions
table lists the Towing Services Act 2024 Pt 11 Div 4, which is not shown and not
encoded.

**Checks:** one module (`rtad-drivers.l4`), one case file (`rtad-cases-drivers.l4`),
52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0008** (priority 1), raised **5 times** by the three Western
Australian cradle-to-grave lives: Chloe **c021** (2019-03-14, turns 16: "a learner's
permit — at what age, and with what conditions?") and **c022** (2020-03-14, turns 17:
a provisional licence); Jake **k032** (2023-08-30, turns 17: a provisional driver's
licence) and **k083** (2049-07-19, 25 km/h over on a motorcycle: an infringement and
demerit points); Daniel **d012** (2012-10-15, turns 16: a learner's permit). The
ledger names "s 8 (learner's permit)", "provisional licence" and "Part 4 (demerit
points)".

So the encoding takes commencement (s 2) and the transition of old permits (s 66);
the learner's permit (ss 10, 11A); when a driver's licence cannot be granted (ss 8,
9); loss of a provisional licence (ss 16-18); and Part 4 as far as a fined driver
meets it: novice drivers (s 40), the registry jurisdiction (s 43), when points are
incurred (ss 40(1A), 44-46), expiry (s 48), the 12-point notice (s 49), the novice
notice (s 50), and the good behaviour election and its breach (ss 51, 52).

Not encoded: identity information (Part 2 Division 3A); the regulation-making
powers (ss 4, 5A, 11-15) beyond comments; disqualification generally (Part 3
Division 2) and extraordinary licences (Division 3); ss 53-60; Parts 5 and 6 other
than s 66. The minimum age for a learner's permit, who receives a provisional
licence and on what conditions, licence classes, which offences carry demerit points
and how many — all are left to the regulations (ss 4, 10(5), 41). The Road Traffic
(Authorisation to Drive) Regulations 2014 (the name c021 gives them) were not retrieved, so each is an input,
and no figure from them appears in the encoding.

The scenarios are in the workbench repository (`scenarios/au/wa/cradle-to-grave-*`),
not under `subjects/au/scenarios` as the task named.

## What the Act turns out to say

### 1. The Act states no driving age at all

The lives ask "at what age?" (c021) and expect a permit at 16 and a provisional
licence at 17. The Act gives neither figure. s 10(5) lets the regulations "fix the
minimum age below which, unless the CEO is satisfied that denial of the permit would
occasion undue hardship or inconvenience, a person cannot be issued with a learner's
permit". So the minimum is an input, and the Act has its own exception: below that age
the CEO may still issue a permit on undue hardship. s 4(5)(c) leaves the provisional
licence to the regulations too. The cases use 16 because c021 assumes it, and say so.
Asserted.

### 2. Daniel's 2012 permit was not issued under this Act

d012 cites this Act for a learner's permit on 2012-10-15. Apart from ss 1 and 2, the
Act came into operation on **27 April 2015** (compilation table, s 2(b)). Daniel's
permit would have been issued under the Road Traffic Act 1974 s 43(1). s 66 deems such
a permit, if "in effect immediately before commencement day", to be a s 10(1) permit
from that day. That is an inference about what governed in 2012, from the
transitional provision; the 1974 Act was not read. Asserted (commencement and s 66).

### 3. Section 8 is not about learner's permits

The scenarios cite "s 8 (learner's permit)". s 8 bars the CEO from granting a
**driver's licence** unless the person usually resides in WA (or resides nowhere
else and never held an interstate licence) and has given up and notified any earlier
Australian or foreign licence. s 3 says a driver's licence "does not include a
learner's permit". The learner's permit is s 10. Both are encoded. Asserted.

### 4. A learner's permit lasts three years and only covers instructed driving

s 10(2): the permit "does not authorise driving except in the course of driving
instruction" by a licensed instructor or a person prescribed by regulations (the
regulations would say who else may supervise). s 10(4): it expires "at the end of a
period of 3 years after the day on which it is issued". Chloe's permit of 2019-03-14
is in force on 2022-03-14 and gone on 2022-03-15. Asserted.

### 5. A newly licensed 17-year-old loses the licence at 4 points

On a provisional licence Chloe (c022) and Jake (k032) are novice drivers (type 1):
s 40(2) counts only time holding an Australian driver licence, and a learner's
permit is not one. Points reaching 4 for an offence committed as a type 1 novice bring
an excessive demerit points (novice driver) notice and 3 months' disqualification
(s 50); at type 2 (after a year) the figure is 8. s 16(3) then cancels the provisional
licence. No s 51 election is open to a novice or a provisional driver (s 51(2)).
The reading of s 50(2) — total postcommencement points, with the threshold set by the
novice type at the time of the offence that reaches it — is the encoder's. Asserted.

### 6. Jake's speeding brings points when he pays, not when he is caught

For k083 the points for 25 km/h over are a regulation figure (s 41) and are not used.
What the Act settles: demerit point action is taken when the offence is "dealt with
by infringement notice", which under s 40(1A) is the first part payment (even a
dishonoured one) or an order to pay or elect. The points expire three years after the
day of the offence (s 48), not of payment: an offence on 2049-07-19 is current on
2052-07-19 and not on 2052-07-20. At 42, licensed since 2023, Jake is not a novice
(an inference from k032 that his licence has run since). Twelve current points bring
3, 4 or 5 months by s 49(2), or a good behaviour year under s 51; 2 points in that year
double the period (s 52(4)). Asserted.

### 7. Holding two licences makes WA the registry

s 43(4): "If this section does not otherwise identify one, and only one,
jurisdiction", WA is the demerit point registry jurisdiction. A person holding both a
WA and an interstate authorisation is identified twice, so falls to WA. Asserted.

### 8. Losing a provisional licence: a floor of 3 months

s 16(1) cancels a provisional licence on conviction of a listed offence or on a court
disqualification; s 16(2) disqualifies for the later-ending of the court's period
and 3 months from the conviction. The encoding assumes both run from the conviction.
A fines enforcement suspension only suspends it (s 17). Asserted.

### 9. A renewing licence-holder and s 8(1)(b)

Read literally, s 8(1)(b) requires anyone who "has held any Australian driver
licence" to have ceased holding it before a grant, and "grant includes to grant by way
of renewal" (s 3). A WA licence is an Australian driver licence. The encoding does not
resolve this; the regulations on renewal were not read. Not asserted.

## What would need doing before this is worth anything

- Retrieve the Road Traffic (Authorisation to Drive) Regulations 2014: the ages,
  provisional conditions and periods, licence classes, supervising drivers, and the
  demerit point offences and their points.
- Read the Road Traffic Act 1974 as in force in 2012 for Daniel's permit (d012).
- Encode s 54 postponement and s 49(2)'s commencement day ("the 28th day after the
  notice is given or a later day") with dates.
- No case law or Department of Transport guidance was searched.
