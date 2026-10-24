# Workers Rehabilitation and Compensation Act 1988 (Tas): baseline encoding for the injured worker and the employer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case the deposit cannot decide returns an explicit `not covered` value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`wrca-dates.l4`**: the calendar arithmetic (working days by the workplace's normal week, months, years, ages), on the built-in date functions only, so that no module imports the slow daydate library.
- **`wrca-core.l4`**: the seat-neutral core, in the Act's own actors and terms ("the worker", "the employer", "the employer's licensed insurer", "dependants"). Computations (basic salary units, normal weekly earnings, the weekly payment, the step-downs and the floor, the cessation date, the impairment and death lump sums, the expense caps, the deadlines) are functions. Where the text says "must" or "shall" or sets a period, there is a regulative rule (`DEONTIC`): 9 definitions, 8 rules and one composition of three of them. Beside each of the employer's dated duties there is a status function (met, missed, still open, not required) built from the same condition and deadline as the duty's rule.
- **`wrca-seat.l4`**: the injured worker's seat (and the dependants' on a death). It asks 26 questions, each with `@export` and a `@desc` on every input, under `§§` headings. It builds the core's records from plain answers and restates no rule.
- **`wrca-seat-employer.l4`**: the employer's seat, 16 questions. Its names differ from the worker seat's, so a case file can import both. "Have I met my duties on this claim" reads each status from the core's status functions. It cannot read them from the `DEONTIC` rules: on the stable `l4`, the `EVALTRACE` result of a breached rule cannot be compared with anything ("Trying to check equality on types that do not support it", checked 2026-10-24), so a question built on it would fail just when a duty is missed. The rules are exercised by the traces in the case files.

The scope was cut, as the task set it, to the payment rules and the claim deadlines: the Act is 511,000 characters.

No earlier encoding of this Act existed to keep. No requirement ledger covers Tasmania, so no ledger line is closed.

## Edition

- **Act:** Workers Rehabilitation and Compensation Act 1988 (Tas), the consolidation **published 2025-12-01 and current on the site at 2026-10-20**, as deposited at `../../registers/source-bundle/act-1988-004.txt` (retrieved 2026-10-19T17:09:43Z). Uncommenced amendments are not in a consolidation, and the site's uncommenced-legislation feed was not checked.
- **Regulations:** Workers Rehabilitation and Compensation Regulations 2021, the consolidation **published 2022-02-18 and current at 2026-10-20**, as deposited at `../../../workers-rehabilitation-and-compensation-regulations-2021/registers/source-bundle/sr-2021-049.txt`. They supply reg 19 and Schedule 1 (the right-to-claim notice), reg 20 (the hearing-loss table), reg 21 (the funeral and counselling caps, $9,500 and $4,000), reg 22 (the travel amount) and reg 28 with Schedule 2 (infringement notice penalties).
- **Formulas.** The s 71 formulas are images in the source. The encoding uses the deposited transcriptions, `{18 + [6.1 × (WPI - 5)]} × BS` and `3.2 × BS × WPI`. In the encode step they were also checked, on 2026-10-24, against https://www.legislation.tas.gov.au/image/wrcam09.gif and https://www.legislation.tas.gov.au/image/Wkcomam2.gif, fetched once each for that purpose and not deposited. They match. That fetch departed from the brief (see Departures).

**Inputs, because the deposit does not hold them:**

- the **basic salary** for a year (s 3(1): $311.30 for 1991, varied each 1 January by the relevant percentage, s 65, and gazetted under s 66). It is never computed. The cases use an illustrative **$1,200 a week**, not the gazetted figure.
- the worker's **pension age** (s 87(1AA), within the meaning of the Social Security Act 1991 (Cth)), in years;
- the commencement of the **Workers Rehabilitation and Compensation Amendment Act 2022**, read from the history notes ("Applied:01 Mar 2023") as **1 March 2023** (finding 6);
- the Tasmanian State Service Award's occasional-user vehicle rate and its travelling-expense terms (s 76(3), reg 22);
- the workplace's normal working week and its closure days (s 3(1) "working day");
- the value of a penalty unit: penalties are given in penalty units.

## Checks

| Module | Case file | Assertions | Traces |
|---|---|---|---|
| `wrca-dates.l4`, `wrca-core.l4` | `wrca-cases-core.l4` | 238 written, 238 satisfied | 8 |
| `wrca-seat.l4` | `wrca-cases-worker.l4` | 82 written, 82 satisfied | 0 |
| `wrca-seat-employer.l4` (with 18 mirror cases against `wrca-seat.l4`) | `wrca-cases-employer.l4` | 63 written, 63 satisfied | 1 |

383 assertions in all, every one satisfied. `l4 run` on all seven files: 0 errors, 0 warnings (2026-10-24, after the fixes listed under "Corrections after the independent verification"). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

The 9 `#TRACE`s each carry an `-- expect:` line, and every one ends in the breach it expects:

- s 36(1AA), the insurer notified late (twice: once in the core cases, once from the employer's seat);
- s 81, payments started a day late;
- s 39, no status notice from the employer or the insurer;
- s 33A, no right-to-claim notice within 14 days;
- s 81A, no dispute within 84 days (the consequence is deemed acceptance, s 81AB);
- s 36(3), dismissal for claiming;
- s 32(1)(a), no notice of the injury;
- s 32(1)(b), a claim one day after the 6 months.

A breached trace satisfies neither `EQUALS FULFILLED` nor its negation, so breaches are checked this way. The fulfilled paths are asserted with `EVALTRACE ... EQUALS FULFILLED`.

Every expected value was written by hand from the deposited text, with the arithmetic in the comment above the assertion. The cases follow illustrative people:

- **Mia**, a full-time storeperson at a Hobart warehouse, injured on Monday 2 March 2026, with her claim received on Wednesday 11 March 2026;
- **Sam**, a casual on 20 of 38 hours, and **Ivy**, a full-time low earner, for the floor;
- a **police officer** on Mia's figures, for s 69B(2DA);
- **Ray**, born 1960, for the s 87 cut-off;
- **Tom**, a delivery driver who dies on 1 June 2026, leaving **Leo** (his wholly dependent partner) and **Ava** (born 2012).

The employer case file asks Mia's facts from her employer's side. Its **18 mirror cases** assert that the two seats give the same answer on the same facts:

- liability (including the s 25(2)(b) and (c) exclusions);
- the s 33A, s 39 and s 81 deadlines;
- the s 81(3) start date;
- deemed acceptance;
- normal weekly earnings;
- the weekly payment;
- the cessation date.

The employer case file imports both seats and takes about 80 seconds to check with the stable `l4`.

## Seats

**1. The injured worker** (`wrca-seat.l4`), and on a death the worker's **dependants**. They ask:

- "Is my employer liable? By when must I claim? Is my claim in time? Did I give notice?"
- "By when must my employer tell me of my right to claim, tell me whether it accepts liability, and start my payments? From what date am I paid? Is it taken to have accepted my claim?"
- "What are my normal weekly earnings? What is my weekly payment, what is it after each step-down, and on what date does it stop?"
- "What lump sum is payable for my impairment, or my industrial deafness?"
- "If the worker dies: by when must we claim, what lump sum, what weekly payments to the spouse and a child, and what toward the funeral and counselling?"
- "How much of my travel to treatment is paid?"

**2. The employer**, read with its licensed insurer (`wrca-seat-employer.l4`). The text puts real, dated duties on this party, and creates offences only it can commit:

- inform the worker of the right to claim within 14 days (s 33A, reg 19, Sch 1);
- notify the insurer within 3 working days, and forward the claim within 5 (s 36(1AA), (1)(b)), or lose the indemnity for that period's weekly payments (s 36(4));
- notify the status of the claim within 28 days, it or its insurer (s 39);
- start weekly payments on the first pay day or within 14 days (s 81);
- dispute liability within 84 days, or be taken to have accepted it (ss 81A, 81AB);
- not refuse, hinder or dismiss for a claim (s 36(3)).

Its questions are worded "Am I liable?", "By when must I ...?", "Have I met my duties on this claim?" (each duty met, still open with its last day, not required, or missed: a breach), "For which days does my insurer not indemnify me?", "What is the most I can be fined?", "What must I pay, and until when?".

No official has a seat. The Board, the Tribunal, the Registrar and the Minister appear only as what they mean for the worker or the employer.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed: the Regulations set the funeral and counselling caps, the travel amount, the hearing table, the right-to-claim form and the infringement penalties, so they come in. The basic salary is gazetted, not in an instrument deposited: an input.
- **The actors the text names:** the worker, the employer, the employer's licensed insurer, the dependants, the spouse or caring partner, the dependent child.
- **A judgment left to someone else is answered conditionally, as an input.** Examples:
  - "as soon as practicable" (s 32(1)(a));
  - "mistake, absence from the State ... or other reasonable cause" (ss 37, 38);
  - what the worker "would be able to earn in suitable employment" (s 69(1)(b));
  - whether it was "reasonably practicable" to start on the first pay day (s 81(1)(a));
  - the degree of dependency, and what is "reasonable and proportionate" to it (s 67(3)): the answer gives the cap;
  - medical evidence of usual and suitable duties (s 69B(2));
  - whether, had the worker not been a police officer, it is unlikely the worker would have been in the circumstances of the injury (s 69B(2DA));
  - the whole person impairment, as assessed (s 72).
- **The Act's own definitions are worked out from facts:**
  - normal weekly earnings and the relevant period (ss 69(2), (2A), (14), 70(2));
  - the ordinary time rate of pay (s 69(1)(a)(ii));
  - normal weekly hours (s 69B(2B)-(2D));
  - child (s 65), from a date of birth and full-time study;
  - working day (s 3(1)), from the workplace's normal week;
  - the reg 20 whole person impairment, from the binaural hearing impairment.

  Borrowed terms are asked as facts: worker (a contract of service or training contract), disease, injury arising out of or in the course of employment, pension age, police officer, an entitlement under the Workers' (Occupational Diseases) Relief Fund Act 1954.
- **One case:** one worker, one injury, one claim. On a death, one deceased worker and that worker's dependants.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Board, the Tribunal's procedure, licensing, the Nominal Insurer and the Fund.

**Departures:** none from the defaults. The s 25 exclusions are asked as facts, one per exclusion, not worked out.

**Departure from the brief.** The brief says no new law is fetched in the encode, verify or fix steps. The encode step nevertheless fetched the two s 71 formula images (wrcam09.gif and Wkcomam2.gif, see Edition) to check the deposited transcriptions. Nothing in the encoding rests on the fetch: the rules use the deposited transcriptions, and the images were not deposited. If the check is to be relied on, a sourcing step should deposit the images, or a `act-1988-004.formulas.md` sidecar citing them, and record it in the subject's register.

## Scope

**In:**

- **Basic salary and units:** s 3(1) "basic salary" (the 1991 figure, as a constant only), s 65 (unit, child, dependent spouse, child and caring partner), s 66 (as the reason the figure is an input).
- **Liability:** s 25(1), as facts, with the exclusions in s 25(1A), (2)(a), (2)(b), (2)(ba), (2)(c), (6) and (8).
- **The worker's claim:** s 32(1), (2), (3) with s 34(2); s 37 and s 38 (as inputs). Regulative: notice as soon as practicable, and a claim within 6 months.
- **The employer's duties**, all regulative, with the employer as party:
  - s 33A with reg 19 and Sch 1;
  - s 36(1AA), (1)(b), (3), (4), (5);
  - s 39;
  - s 81(1)-(4);
  - s 81A(1), with s 81AB.
- **Weekly payment:** s 69(1), (2), (2A), (3), (14); s 70(2), (3).
- **Step-downs:** s 69B(1), (2), (2A)-(2D), (2DA) with s 164BB, (2E), (3), (4), (6).
- **Cessation:** s 87(1AA), (1), (4).
- **Death:** s 67(1)-(5); s 67A; s 67B(3), (4).
- **Permanent impairment:** s 71(1)-(4); ss 72A(3), (5), 73(1), (4) with reg 20.
- **Expense caps:** s 75(1)(b) with reg 21; s 76(1), (3) with reg 22.
- **Penalties:** the maxima in ss 33A, 36(3), 39 and 81(2), and reg 28 with Sch 2.

**Out:**

- Part V: dispute procedure, conciliation, medical panels, and the Tribunal's powers under s 81A(2)-(6) and s 81AC (beyond naming them).
- Common-law damages and the WPI threshold in s 138AB.
- Part XI return to work, beyond s 69B(2A).
- Licensing of insurers and self-insurers.
- The disease and PTSD presumptions (ss 25A-28A).
- Gradual-process rules (ss 78-80).
- Medical services under Division 2, beyond the regulation caps (s 75(1)(a), (2)-(9)).
- s 86 termination procedure; s 88 review; ss 82-84B (prisoners, residence abroad, holidays and leave).
- s 69(4)-(13): the Tribunal's adjustments, regard to other payments (s 69(4)(a)), and late certificates.
- s 69B(5) (the 2004 amendments' transitional rule: any injury it reaches is before 1 March 2023, and is already `not covered` through s 87(4)).
- The employer's undated or record-keeping duties in the sections that are in: s 33(2) (record a notice of injury), s 36(1)(a) (complete the employer's report section of the claim form "immediately" on receiving it) and s 36(1)(c) (keep a copy of the claim). They set no countable period, carry no penalty of their own, and change nothing the worker is paid or must do, so they are left out rather than given an invented deadline.
- s 36(2): the licensed insurer's duty to forward a copy of the claim to the Board within 5 working days. It is owed to an official, and puts nothing on the worker or the employer.
- s 87(2), (3) (the Tribunal's extension beyond the cessation date).
- ss 67B(1), (2), 67C-67G (the employer's duties on a death claim, their timing and disputes).
- s 72 (how impairment is assessed), s 73(2), (3) and s 73A, beyond inputs.
- The State of connection (Part III Division 2), workers deemed by ss 4A-7, and asbestos-related disease.

## Commonwealth links

Cross-folder IMPORT does not work, so these are links, not code:

- **Social Security Act 1991:** `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`.
  - Pension age (s 23(5A)-(5D)) is the input to s 87 here; that encoding answers "What is my pension age".
  - Tasmanian weekly payments and lump sums are "compensation" for its compensation recovery rules (Part 3.14, s 17): the periodic compensation reduction and the lump sum preclusion period. That encoding answers those questions once the Tasmanian amounts are known.
- **Income Tax Assessment Act 1997:** `subjects/au/income-tax-assessment-act-1997/` (the baseline at `encodings/baseline-2026-10/` does not cover compensation receipts).
  - Weekly payments replace earnings and are assessable as ordinary income.
  - A capital gain or loss from compensation for "any wrong or injury you suffer in your occupation" is disregarded (s 118-37(1)(a), read in the deposited text). That covers the s 71 lump sum.
  - Neither point is encoded there yet.

## What the Act turns out to say

1. **The current basic salary is not in the text.** s 3(1) gives $311.30 for 1991 and varies it each 1 January by the "relevant percentage" (s 65), and s 66 has the Minister gazette it. Every lump sum (ss 67, 71), the s 69B(3) floor and the child's weekly payment (s 67A(1)(b)) turn on it. It is an input, never computed from 1991. The cases use an illustrative $1,200. Asserted (415 units = $498,000).
2. **The s 71 formulas, transcribed from images, check out against the images** (wrcam09.gif, Wkcomam2.gif, 2026-10-24; a fetch that departed from the brief, see Departures). The scale is continuous at the top: 70% gives 414.5 units, more than 70% gives 415 units. The psychiatric scale (s 71(2)(b)) uses the same "(WPI - 5)" although its threshold is 10%. So the first compensable psychiatric impairment, 10%, is worth 48.5 units, while the first physical one, 5%, is worth 18. Asserted.
3. **The s 69B(3) floor is ambiguous.** It reads: "not to be less than 70% of the basic salary or the weekly payment ..., whichever is the lesser". Read here as the lesser of (70% of the basic salary) and (the weekly payment). The other reading, 70% of the lesser of the two, can never exceed the 80% step-down, so it would give the subsection no effect. On the reading taken, a full-time worker whose weekly payment is at or below 70% of the basic salary is never stepped down. Asserted: Ivy, $700 against a $840 floor, keeps $700 in week 80.
4. **The step-down bands mix two measures.** s 69B(1) counts weeks "of the period of incapacity", which adds separate periods together (s 69B(6)), but says "from the date of the initial incapacity". s 69B(2E) ends the entitlement in years after that date. Read here: the band by the week's number in the aggregated period; the cessation by calendar date.
5. **Whether the named last day is paid is not settled.** s 69B(2E) ends the entitlement "on the expiration of 9 years after the date of the initial incapacity"; s 87 says "on the date on which the worker attains the pension age". Read here: a week beginning on or after the named date is not paid. Asserted (Ray, 2 March 2028).
6. **For an injury before the 2022 amendments, the cessation date cannot be given.** s 87(4) keeps s 87 as it stood before the Workers Rehabilitation and Compensation Amendment Act 2022 for an injury before that Act commenced. That version is not deposited, so such an injury's cessation date is `not covered`. The commencement is read from the history notes ("Applied:01 Mar 2023"); the proclamation is not deposited. Asserted (an injury on 15 February 2023: not covered; on 1 March 2023: covered).
7. **A worker injured at or after pension age still gets two years** (s 87(1)(b): "less than 2 years before" includes after). Asserted (born 1958, injured 2026: payments to 2 March 2028).
8. **s 67 does not say which year's basic salary prices the death lump sum.** s 71 says "calculated as at the date of the injury"; s 67 does not. Read here: the figure the caller gives, for the year of payment.
9. **s 67(2) has gaps and a hard edge.** With no dependent spouse or caring partner, it does not say how the lump sum goes:
   - where some children are wholly and some partially dependent;
   - where the only dependants are not a spouse, caring partner or child (a dependent parent, say).

   Both are `not covered`. And under (2)(a), a wholly dependent spouse takes all 415 units even when there are dependent children of that spouse; the children get only the s 67A(1)(b) weekly payment. All asserted.
10. **s 67A(1)(b) states no end, and no division, for a child's weekly payment** of 15% of the basic salary. It ends only when the person stops being a "child" (s 65: under 16, or under 21 and a full-time student) or a dependant. Read here: each dependent child is paid 15%, and payment starts on a day after the 13 weeks from the death. Asserted.
11. **s 69(3) "increased or decreased by the like amount"** does not say like to what. Read here: by the change in the ordinary hourly rate times the hours engaged before the incapacity. Asserted (a $1.50 rise on 38 hours adds $57).
12. **The s 36 deadlines turn on the workplace, not the calendar.** "Working day" means a day on which work is normally carried on at the worker's place of employment (s 3(1)). So s 36's 3 and 5 working days differ for a Monday-to-Friday site and a seven-day site. Asserted (16 or 18 March, or 14 or 16 March). "The employer's insurer" in s 36(1AA) is defined only for Part XI (s 141); read as its licensed insurer, so a self-insurer has none.
13. **Missing the s 36(1AA) deadline costs the employer its indemnity.** The consequence is not a fine: the insurer need not indemnify the weekly payments from the day after the 3 working days to the day of notification (s 36(4), (5)). Asserted (19 March notice: 17 to 19 March).
14. **Missing the s 81A deadline is not an offence either.** An employer that does not dispute within 84 days is taken to have accepted liability (s 81AB). It is encoded as a breach whose reason states that consequence. s 81A(5) still lets the employer refer a later dispute about continuing payments to the Tribunal. Asserted, with a trace.
15. **The s 81 duty to start weekly payments runs from the receipt of a claim, whether or not liability is accepted.** s 81AA makes the payments no admission. Only a Tribunal determination under s 81A(3)(c) stops them. Encoded for a claim for weekly payments.
16. **Industrial deafness has its own claim rules.** There is no notice requirement, and no deadline while the worker stays in the employment (s 32(2)). There is a cliff at 5% binaural hearing impairment: at 5% nothing is paid, but at 6% reg 20 gives 5% whole person impairment, and s 71(1)(b) pays 18 units for that. reg 20 does not say which way a half rounds; read half up. Asserted.
17. **s 71(3), (4): the loss of a foetus counts as 20% "in addition to" any other impairment.** Read here as added to the assessed percentage, not combined through the AMA tables. Asserted (3% + 20% = 23%: 127.8 units).
18. **Every s 67A period is counted from the day after the death.** s 67A(2)(a) pays 100% "for the first 26 weeks following the date of death", so the day of death is not one of those weeks. s 67A(1)(b) starts a child's payments "on the expiration of 13 weeks after the date of death". The same count is used for "78 weeks from the date of death" ((2)(b)), "not exceeding 2 years from the date of death" ((2)(c)) and "on the expiration of 2 years after the date of death" ((4)).
    - The day of death itself is paid at 100%: the spouse's payments run "from the date of the worker's death" (s 67A(1)(a), s 67B(3)(a)), and that day comes before the 90% period.
    - For a death on Monday 1 June 2026: 100% to 30 November 2026 (182 days after the death); 90% from 1 December 2026 to 29 November 2027 (546 days after); 80% from 30 November 2027 to 1 June 2028; nothing from 2 June 2028. A child's 15% runs from 1 September 2026 (the 13 weeks are 2 June to 31 August).
    - s 69B is counted differently, because its text differs: s 69B(6)(a) defines the period of incapacity as "starting on the date of the initial incapacity", so its weeks include that day. s 67A has no such definition.
    - Read the same way, s 69B(2E)'s "on the expiration of 9 years after the date of the initial incapacity" would make the anniversary itself the last day paid. Finding 5 takes a week-by-week reading (a week that begins on the named day is not paid) and is left as it is; the two should be settled together.
    - The Acts Interpretation Act 1931 (Tas) is not deposited, so its rule for reckoning periods was not checked against this.

    **Corrected** after the independent verification: the first version counted the spouse's periods with the day of death as day 0 (30 November 2026 at 90%, $1,260; 1 June 2028 nothing) and the child's from the day after. Asserted: 30 November 2026 $1,400, 1 December 2026 $1,260, 29 November 2027 $1,260, 30 November 2027 $1,120, 1 June 2028 $1,120, 2 June 2028 nothing.
19. **s 25(2)(b), (ba), (c) and s 25(8) are further exclusions.** No compensation is payable for undulant fever or brucellosis without a medical practitioner's written certificate on a blood examination ((2)(b)); for coronary heart disease, a diseased heart valve or an aortic or cerebral aneurism unless the employment contributed to it to a substantial degree ((2)(ba)); for a disease the worker wilfully and falsely denied in writing on entering the employment ((2)(c)); or for a disease compensable under the Workers' (Occupational Diseases) Relief Fund Act 1954 ((8), asked as a fact). "To a substantial degree" is the s 3(2A) test, "only if it is the major or most significant factor", so for a condition given as a disease (ba) adds nothing to s 25(1)(b); it bites where the condition is given as an injury that is not a disease. No injury is prescribed for (ba) in the deposited Regulations. **Corrected** after the independent verification: the first version did not ask these facts, so a case they exclude came back "liable". Asserted, with mirror cases.
20. **s 69B(2DA): a police officer's weekly payment is not stepped down** where, had the person not been a police officer, it is unlikely the person would have been in the circumstances of the injury. Whether that is unlikely is a judgment: an input. s 164BB disapplies (2DA) for a claim made before the Workers Rehabilitation and Compensation Amendment Act 2019 came into force (2 September 2019 by the history note). Any such claim is for an injury before 1 March 2023, which this encoding already answers as `not covered` (finding 6), so s 164BB changes no answer here. **Corrected** after the independent verification: the first version listed (2DA) as out of scope but still gave a police officer the 90% and 80% step-downs. Asserted (1,400 in weeks 30, 80 and 105; 1,260 and 1,120 where (2DA) does not apply).

## Corrections after the independent verification (2026-10-24)

An independent verifier found seven issues. Each was checked against the deposited text before it was fixed.

1. **s 67A counting** (major): the spouse's and the child's periods used opposite conventions. Fixed: one count for all of s 67A, finding 18. Four expected values changed, and cases now sit on both sides of every s 67A boundary.
2. **Cross-reference**: the comment on the child's weekly payment named finding 9. Fixed: finding 10.
3. **Citations in an answer**: one "nothing on this day" answer served both the spouse and the child, and cited s 67A(1)(b) and s 67B(3) for both. Fixed: two answers, s 67A(1)(a) with s 67B(3) for the spouse, s 67A(1)(b) alone for the child.
4. **Scope**: s 69B(2DA) and the s 25(2)(b), (ba), (c) exclusions gave definite wrong answers (findings 19, 20). Fixed by encoding them, and s 25(8) with them. s 33(2), s 36(1)(a), (1)(c) and (2) are now listed as out, with reasons.
5. **A seat restating a rule**: the employer seat had its own test of whether the claim is for weekly payments, and its own mappings of the core's answers to a duty status. Fixed: the status functions are now in the core, beside the rules they mirror. The verifier's wider point, that no seat question uses the `DEONTIC` rules, cannot be met on the stable `l4` (see Method).
6. **Fetch in the encode step**: named as a departure from the brief (Departures).
7. **Week dates in the cases**: week 106 of an incapacity from 2 March 2026 begins on 6 March 2028, not 2 March; and the week beginning 5 March 2035 is week 471, not 470. Fixed, with the date arithmetic asserted. The answers did not change. The boundary case the old date was testing (a week that begins on the cessation day) is kept, as a week 105 after a 3-day break.

## What would need doing before relying on it

- Take the **gazetted basic salary** for each year in issue (and for the year of the injury, for s 71), and the current State Service Award travel rates.
- Check the s 87 commencement date (finding 6) against the proclamation, and deposit s 87 as in force before 1 March 2023 for older injuries.
- Settle findings 3, 4, 5, 10, 11 and 18 with someone who knows how the Tribunal and WorkSafe Tasmania apply them (5 and 18 together), and deposit the Acts Interpretation Act 1931 (Tas) to check finding 18 against its rule for periods.
- Deposit the s 71 formula images or a formulas sidecar (Departures).
- Check the consolidation against the authorised version, and the uncommenced-legislation feed.
- Run an independent test pass, and the human gates.
- Encode the out-of-scope parts a real claim meets:
  - s 69(4)(a), regard to other payments;
  - s 86, termination;
  - Division 2, medical expenses;
  - Part XI, return to work;
  - ss 67B-67G, the employer's duties on a death claim.
