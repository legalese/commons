# Employment Rights Act 1996 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the dismissal position for` (`era-goal.l4`). For an employee whose contract has ended, it answers:

- the minimum notice each side had to give;
- the effective date of termination, and the later date used for the qualifying period and the basic award;
- whether the employee was dismissed and meets the unfair dismissal qualifying period;
- the last day to present an unfair dismissal complaint;
- the basic award;
- whether the employee is entitled to a redundancy payment, and how much;
- the last day of the s 164(1) claim period.

Three goals sit under it:

1. **Minimum notice** (`era-notice.l4`):
   - s 86(1) for the employer and s 86(2) for the employee, measured on the day notice is given (s 211(1)(b));
   - the day the employer's statutory notice would expire;
   - from that, the later effective date of termination in s 97(2) and (4), and the later relevant date in s 145(5).
2. **Unfair dismissal** (`era-unfair-dismissal.l4`):
   - dismissal (s 95(1));
   - the qualifying period (s 108(1)-(5));
   - the time limit (s 111(2)(a), (2A), (3)), with early conciliation (s 207B);
   - the basic award (ss 119-122, with the cap in s 227(1)).
3. **Redundancy payment** (`era-redundancy.l4`):
   - dismissal (s 136(1));
   - redundancy, with the s 163(2) presumption;
   - the exclusions in ss 140 and 141 (others as an input);
   - the qualifying period (s 155);
   - the claim steps (s 164(1)-(2)), with s 207B for a tribunal reference and for (2) (s 164(5));
   - the amount (s 162, with the cap in s 227(1)).

`era-periods.l4` holds the counting the goals share: periods "beginning with" a day, continuous employment "ending with" a day, years reckoned backwards with the age bands, and s 207B.

As the user asked, this covers only the sections those goals need. The rest of the Act was left out on purpose (see the table).

Dates are computed as the Act words them. The UK has no general next-working-day rule, so no date moves for a weekend or bank holiday.

## Coverage

| Provision | Disposition |
|---|---|
| Part I (particulars), Part II (wages), Parts III-VIII (guarantee pay, Sunday work, protected disclosures, time off, suspension, leave) | out of scope: not needed for the three goals |
| Part IX: s 86(1)-(2) | encoded (goal 1) |
| s 86(3), (6) | out of scope: waiver and payment in lieu, and conduct-based termination, are not computed |
| s 86(4) | out of scope: the length of the notice is the same once the contract is treated as indefinite |
| ss 87-91 | out of scope: pay during notice is not computed |
| s 92-93 | out of scope: written reasons for dismissal |
| s 94 | the right, which the goal assumes |
| s 95(1) | encoded (goal 2); s 95(2) (counter-notice) is not |
| s 97(1)-(5) | encoded (goal 1, and used in goals 2 and 3) |
| s 98-107 | input: the tribunal's finding that the dismissal is unfair, and its reason |
| s 108 | encoded (goal 2); the reasons in (3)-(5) are one input |
| s 110 | out of scope: designated dismissal procedures agreements |
| s 111(1)-(3) | encoded (goal 2); (5) blacklists: the late-complaint allowance is one input |
| ss 111A-118 | out of scope: evidence, remedies by reinstatement and re-engagement |
| s 119 | encoded (goal 2) |
| s 120(1), (1C) | encoded (goal 2) |
| s 121 | encoded (goal 2) |
| s 122 | encoded (goal 2): (1)-(3A) reductions as an input amount; (4) as an input amount; (5) folded into the reductions |
| ss 123-134A | out of scope: the compensatory award is "just and equitable" and is not computed |
| s 135(1)(a), (2) | encoded (goal 3); (1)(b) lay-off and short-time is not |
| s 136(1) | encoded (goal 3); (2)-(5) are not |
| ss 137-138 | out of scope |
| s 139 | input: whether the dismissal is by reason of redundancy |
| s 140(1) | encoded as an input finding (goal 3); (2)-(5) are not |
| s 141 | encoded as an input finding (goal 3) |
| ss 142-144, 146-154 | out of scope |
| s 145(2), (5)-(6) | encoded (goal 1); (3)-(4) are not |
| s 155 | encoded (goal 3) |
| ss 157-161 | one input: excluded otherwise |
| s 162(1)-(3) | encoded (goal 3) |
| s 163(2) | encoded (goal 3) |
| s 164(1)-(3), (5) | encoded (goal 3); (3) is the tribunal's input |
| ss 165-206 | out of scope |
| s 207B | encoded (goals 2 and 3) |
| s 211(1) | encoded; (3) postponement is applied to the input start day |
| ss 212-219 | out of scope: continuity rules; the start day is an input |
| ss 220-226, 228-229 | out of scope: a week's pay is an input |
| s 227(1) | encoded |
| Parts XV-XVI, Schedules | out of scope |

## Forks (readings taken)

- **F1, s 86(1), notice on day d.** A week's notice given on day d runs from the next day, so it expires at the end of d + 7. The length of service is measured on the day the notice is given.
- **F2, "a period of n months beginning with" day x.** The period ends on the day before the corresponding date n months later. Where that month has no corresponding date, it ends on the last day of that month. Examples:
  - three months from 31 August end on 30 November;
  - three months from 30 November end on 28 February;
  - one month from 31 January ends on 28 February.
- **F3, s 211(1): "continuously employed for a period of not less than two years ending with" day E.** E is on or after the last day of the two years beginning with the start of continuous employment. From 29 February 2024, the two years end on 28 February 2026.
- **F4, ss 119(1)(b), 162(1)(b): reckoning backwards.** Year k begins on the corresponding date, k years back, of the day after the end day. Where 29 February makes this differ from "the day after the corresponding date k years before the end day", the later of the two is taken, so no year is longer than a year. For example, the year ending 28 February 2025 begins on 1 March 2024. A year counts only when it is complete. This was corrected after the independent pass (B21, B22, P32).
- **F5, ss 119(2), 162(2): "a year of employment in which the employee was not below the age of forty-one".** The employee must be that age or over throughout the year, so on its first day. A birthday falling inside the year does not raise that year's rate.
- **F6, s 97(4) and s 145(5).** Section 97(4) extends the effective date of termination when the employee terminates (constructive dismissal). Section 145(5) has no such limb, so for redundancy the relevant date is not extended when the employee terminates.
- **F7, ss 97(2), 145(5): "the notice required by section 86 ... if duly given on the material date".** The length is measured by service up to the material date. When there was less than one month's service, s 86 requires no notice and the date does not move.
- **F8, s 111(2)(a) and s 164(1).** These periods run from the s 97(1) and s 145(2) dates. The later dates in ss 97(2) and 145(5) apply only to the provisions those subsections name.
- **F9, s 164(2): "the period of six months immediately following the period mentioned in that subsection".** It runs from the day after the unextended s 164(1) period. Section 207B extends both its end and a tribunal reference under (1)(c). It does not extend (1)(a), (b) or (d).
- **F10, s 163(2).** If it is not proved either way whether the dismissal was by reason of redundancy, it is presumed to be. The encoding answers as a tribunal would on a reference.
- **F11, s 120(1).** The minimum is applied before the s 122 reductions, so it is the greater of the s 119 amount and £9,157. Section 121 replaces the s 119 amount with two weeks' pay.
- **F12, s 122.** The reductions are taken off and the result is floored at 0.
- **F13, s 111(3).** A complaint presented after notice is given but before the effective date of termination may be considered, even before the s 111(2) period begins. A complaint presented on the day notice is given counts as after it.
- **F14, s 207B(3): "the period beginning with the day after Day A and ending with Day B is not to be counted".** Only the days of conciliation within the period the limit counts are stopped, from the later of the day after Day A and the period's first day, to Day B. For example, conciliation that ended before employment did stops nothing. This was corrected after the independent pass (T22, T23). Section 207B(4) is unchanged.
- **Known limits (from the independent pass).**
  - The s 111(5) blacklist late-complaint test shares one flag with s 111(2)(b).
  - The s 122(3) limit on conduct reductions is not enforced.
  - Sections 136(3), 140(2)-(3) and 145(3)-(4) are not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18. The run is slow, taking about five minutes. It shows:

- 8 modules: 245 assertions satisfied, 0 failed, 0 other errors;
- 97 are the encoder's (`era-tests.l4`);
- 148 are independent (`tests-independent.l4`).

The independent pass found five disagreements, all fixed in the encoding (F4, F14). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F5:** confirm the age reading for the year in which a birthday falls.
- **F14:** confirm that conciliation begun before the effective date of termination stops only the days after it.
- **F9:** confirm that s 207B extends the end of the s 164(2) period for a written claim as well as for a tribunal reference.
- The text as at 29 July 2026 still gives two years in s 108(1). Confirm that no prospective amendment (for example under the Employment Rights Act 2025) is in force for the dismissal dates in question.
