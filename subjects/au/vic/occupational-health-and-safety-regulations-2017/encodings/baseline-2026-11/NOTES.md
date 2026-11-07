# Occupational Health and Safety Regulations 2017 (Vic) -- baseline encoding, the worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). A seat-neutral core (`ohsr-core.l4`), date helpers
(`ohsr-dates.l4`, prelude only: no daydate import, no `YMD`), and a seat layer (`ohsr-seat.l4`) that builds the core's
inputs from plain answers and restates no rule. Three regulative rules (r 195(1), r 200(1), r 355(1)) run by `EVALTRACE`
inside exported questions that take only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulations; nothing existing was touched. The parent Act has its own baseline
(`../../../occupational-health-and-safety-act-2004/encodings/baseline-2026-11/`); a module cannot import across subjects,
so what this encoding needs from the Act is restated narrowly, with the section: the penalties of ss 21 and 22(1)
(the "Act compliance" route of r 7), the reach of s 21(3)(b) (with r 8), and s 37(2)(e)(i) as the provision r 124 serves.

## Edition

- **Regulations:** Occupational Health and Safety Regulations 2017, S.R. No. 22/2017, Version No. 018, incorporating
  amendments as at 20 October 2026 (the current version on 2026-11-07), deposited at
  `../../registers/source-bundle/occupational-health-and-safety-regulations-2017.txt` (committed text sha256
  c1d58bdebce4f125517c4f2907a86fcca5bda6a7c11c98be00eb0ae1f8d17e60, as in its meta.json; reconverted on 2026-11-07 to restore 9 raised decimal points the first conversion dropped, first deposit 4141667af879fb2e0f3f9cfee9238b4781d3bdd0dd9d27a0b050db8ff604e72b), a plain-text conversion of the Word
  file the owner saved by hand on 7 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not
  checked against the authorised PDF, which was not saved.
- **Formulas sidecar:** the one embedded equation (17-22sr018-F1, Sch 14 cl 3.1, the major hazard facility aggregation
  formula) is in Part 5.2, which is out of scope; nothing here reads it.
- **Commencement dates read from the endnotes:** S.R. No. 71/2018 commenced on 5 June 2018, so the "2-year anniversary"
  that switches the lead figures (rr 186(1A), 193(2), 198(1A), 199(1A), 200(3), 201(3A)) is 5 June 2020; S.R. No. 63/2024
  (the present r 319Y) commenced on 1 July 2024.
- **Numbers the Regulations borrow:** the exposure standards (Safe Work Australia's Workplace Exposure Standards for
  Airborne Contaminants) are not deposited and are inputs; the value of a penalty unit is not deposited, so every penalty is
  in penalty units. The Authority's determinations (record periods, lead processes, excluded activities) are inputs.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (and a
deliberately false assertion was seen to be reported as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ohsr-dates.l4` | 0 | 0 | 6 | 6 |
| `ohsr-core.l4` | 0 | 0 | 0 | 0 |
| `ohsr-seat.l4` | 0 | 0 | 0 | 0 |
| `ohsr-cases-physical.l4` | 0 | 0 | 171 | 171 |
| `ohsr-cases-substances.l4` | 0 | 0 | 202 | 202 |

Five `#TRACE`s, each with an `-- expect:` line, each giving what it expects (r 195(1): fulfilled on day 7, breached
after day 7; r 200(1): fulfilled on day 7; r 355(1): fulfilled when work begins on day 3, breached on day 2).

Every expected value was worked by hand from the text, with the edges: 85 and 85.1 dB(A), 140 and 140.5 dB(C) (r 5); a
15 dB and a 14 dB fall in hearing, and tests exactly 2 years and 2 years and a day apart (r 38); 30 November + 3 months
and 29 February + 24 months (r 37); a fall of exactly 2 m and of 2.1 m (rr 5, 41); 19.4, 19.5, 23.5 and 23.6% oxygen (r 5);
4.9, 5, 9.9 and 10% of the LEL with and without a detector (r 60); 4 and 5 June 2020 for the lead standard (r 186); each
blood lead figure and the figure just under it, before and after 5 June 2020 (rr 198, 199, 201); the 7th and 8th day
(rr 195(1), 200(1)); one month after 31 January (r 196(2)); 0.1 and 0.11 f/ml (r 210), 0.01 and 0.02 f/ml (r 216);
exactly 1 and 2 years since the last asbestos medical (rr 262, 282); 15 December + 30 days; 10 and 10.5 square metres and
23, 24, 100, 120 hours (r 298); 0.9 and 1% silica (r 5); 30 June and 1 July 2024 (r 319Y); a 2 m and 2.5 m fall, a 1.5 m
and 1.6 m trench (r 322); $349 999 and $350 000, $250 000 on 30 June and 1 July 2014 (rr 332, 558); the day 2 years after
the last construction work and the day after (r 349); a 1, 1.5 and 1.6 m trench and a 2 and 2.1 m shaft (r 5 "construction
excavation", rr 354, 355); work beginning on the day of the notice, 2 days and 3 days after it,
and before it (r 355).

## Seat

**The worker.** An employee, and where r 8 or a regulation extends the duty, an independent contractor engaged by the
employer or a contractor's employee, on matters within the employer's control; including one who has been injured, has
fallen ill or fears an illness from the work, and a person applying for such work. Every exported question is one that
person would ask ("Did my employer have to do this?", "Has it breached the regulation?", "Is my exposure over the
limit?", "When is my next test due?", "Must I be taken off the work, and when may I go back?", "How long must my records be
kept?", "Was WorkSafe told in time?", "What is the most the employer can be fined?"). Provisions addressed to the employer,
the licence holder, the principal contractor or the Authority are encoded as what they mean for that person: a duty owed to
them, a test or examination due to them by a date, a record they may see or that must be kept, a notice that should have
been given, a penalty the duty-holder faces.

No second seat. The employer is the obvious candidate under the guide's "more than one seat" ruling; its seat is left for a
later layer over the same core (`ohsr-seat-employer.l4`). Officials (WorkSafe, inspectors) get none.

The 2026-10-18 defaults:

- **The instrument alone, with the instruments that set its numbers.** Followed. The Regulations set their own figures
  (noise, lead, asbestos, oxygen, LEL, heights, depths, costs, periods); the exposure standards they borrow from Safe Work
  Australia are not deposited and are inputs; the Act's penalties are restated with the section.
- **The actors the text names.** Followed: the employer, the employee, the independent contractor, the self-employed
  person, the person who manages or controls a workplace, the asbestos removal licence holder, the principal contractor, the
  registered medical practitioner, the health and safety representative, the Authority (WorkSafe).
- **Judgments answered conditionally.** Followed: "so far as is reasonably practicable" (which control measure was the
  highest reasonably practicable; whether the risk was reduced so far as reasonably practicable), "uncertainty (based on
  reasonable grounds)", "reasonably likely" (lead-risk work, high risk crystalline silica work, adverse health effects), "do
  not adequately control", a practitioner's opinion or certificate, and every determination of the Authority are inputs.
- **The instrument's definitions worked out; borrowed terms asked.** Followed: hazardous manual handling, musculoskeletal
  disorder, noise exposure standard, fall, confined space, safe oxygen level, asbestos exposure standard, engineered stone,
  lead-risk work, high risk crystalline silica work, construction work, high risk construction work are worked out. Lead
  process (r 178, nineteen heads) and crystalline silica process (r 319B) are asked as facts, with the heads in the
  `@desc`; "notifiable incident", "exposure standard" and "hazardous substance" (GHS) are asked.
- **One case.** One worker, one employer, one hazard, one test result or one excavation.
- **The instrument's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative provisions in; machinery out.** Followed (see Scope).

## Scope

**In:**
- **Reach and enforcement** -- r 7 (as the penalty route), r 8 (with Act s 21(3)(b)).
- **Part 2.1** -- rr 18, 19, 20.
- **The orders of control and reviews** -- rr 27, 34(2)-(5), 44, 56, 98, 163, 184, 238, 325 (one ranked order, one
  function); rr 28, 36, 48, 62, 164, 185, 239, 326 (the review occasions).
- **Part 3.1** -- r 5 (hazardous manual handling, musculoskeletal disorder), rr 26, 27.
- **Part 3.2** -- r 5 (noise exposure standard), rr 32, 34, 37, 38, 40(1).
- **Part 3.3** -- r 5 (fall), rr 41, 44, 45, 49.
- **Part 3.4** -- r 5 (confined space, safe oxygen level), rr 50, 58(2)-(3), 60, 63, 64, 65-67, 69, 73.
- **Part 3.5** -- rr 74, 98, 99(3), 124.
- **Part 4.1** -- rr 154(2), 163, 165, 166, 168, 169, 171 with Schedule 9.
- **Part 4.2** -- rr 174, 175(3), 176 with Schedules 10 and 11 (as classes).
- **Part 4.3** -- rr 179, 184, 186, 193-196, 198-201, 204.
- **Part 4.4** -- r 5 (asbestos exposure standard), rr 210, 216, 225, 237, 238, 262, 263, 282, 283, 298(1), 311, 313.
- **Part 4.5** -- r 5 (engineered stone), rr 319C, 319J(4), 319L, 319S, 319V, 319Y, 319Z, 319ZA, 319ZB.
- **Part 5.1** -- r 5 (construction excavation), rr 321, 322, 325, 327, 332, 341, 342, 349, 354, 355, 558(1).
- **Penalties** -- 68 provisions, with the Act's ss 21 and 22(1) for "Act compliance" provisions; r 205 (the employee's
  own offence) asked from the worker's seat, the rest as the employer's or other duty-holder's.

**Regulative rules:** three. r 195(1) (the employer MUST notify the Authority in writing WITHIN 7 days after identifying
lead-risk work, LEST breach); r 200(1) (the employer MUST provide a medical examination WITHIN 7 days after a removal under
r 199(1)(a) or (c), LEST breach); r 355(1) (the employer SHANT begin the construction excavation work on the day of the
notice or the 2 days after, the reading of "at least 3 days before commencing"). Each runs by `EVALTRACE` inside an exported
question that takes dates. The other time limits (rr 37, 38, 64, 175(3), 196(2), 198, 262, 282, 311, 349 and the 30-year
records) are dates and yes/no answers.

**Out, and why:**
- Duties of designers, manufacturers, suppliers and importers (Part 3.2 Division 1, Part 3.4 Division 2, Part 3.5
  Divisions 2-4, Part 4.1 Division 2, rr 173, 319G, 319H): not the worker's employer; their seat is the business's.
- Part 2.2 (issue resolution): procedure under s 73 of the Act; the health and safety representative's seat.
- Part 3.2 rr 29-31, 33, 35, 39, 40(2)-(3); Part 3.3 rr 42, 43, 46, 47; Part 3.4 rr 51-57, 59, 61, 68, 70-72; Part 3.5
  rr 75-97, 100-123 and Divisions 6-7 (registration of designs and items): either duties the worker meets through the
  order of control already encoded, record-keeping and signage (their penalties are in), or the registration machinery.
- Part 3.6 (high risk work licences), Chapter 6 (licensing and registration): licensing machinery, as the brief directs.
- Part 4.1 rr 153 (Schedule 6 prohibitions), 155-162 (safety data sheets, labels, register: penalties only), 167, 170.
- Part 4.3 rr 178 (as a fact), 180-183, 187-192, 197, 202, 203, 205 (penalties only where listed).
- Part 4.4 Divisions 3-4 except their penalties; Division 5 rr 226-236 (the person who manages or controls a workplace,
  and the register's content); Division 6 (demolition and refurbishment); Division 7 except rr 262, 263, 282, 283, 298(1);
  Division 8 except rr 311, 313, 318.
- Part 4.5 Division 2, rr 319J(1)-(3), 319K, 319M-319R, 319T, 319U, 319W, 319X, Division 5 (transitional).
- Part 5.1 rr 323, 324, 326, 328-331, 333-337 (the principal contractor's plan beyond its threshold), 338-340, 343-348,
  350-353 (card administration).
- Part 5.2 (major hazard facilities, including r 360) and Part 5.3 (mines, including r 423A): out, as the brief directs.
- Chapters 1 (except rr 5, 7, 8), 7, 7A, 7B and 8 (except r 558(1)); Schedules other than 9, 10 and 11.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** r 8 -- `the employer's duty reaches the person (r 8)` -- neither an employee nor a contractor: `JUST FALSE` --
  `NOTHING` (s 23 of the Act may protect them, and some notes name s 23).
- **F2** r 7 notes naming several sections -- `the maximum fine in penalty units` -- the penalty of the section protecting
  an employee of the employer (s 21, or s 22(1) where the note names it) -- the highest of the sections named, or the
  section matching the offender.
- **F3** rr 198, 199, 201 -- `the next biological monitoring is due by (r 198)` and others -- the lead figures in force on
  the day of the blood test -- on the day the duty falls to be performed.
- **F4** r 200(2), (3) -- `the employee must be kept off lead-risk work (rr 200, 201)` -- after a removal for failed
  controls, `JUST TRUE` until the level is below the removal figure and the practitioner agrees -- `NOTHING` (r 200(2) is
  only a permission).
- **F5** r 195(1) -- `Was WorkSafe told of the lead-risk work in time` -- a process not identified either way (deemed
  likely by r 194(4)): `NOTHING` -- the duty to notify arises from the deeming.
- **F6** r 355(1) "at least 3 days before" -- `r 355(1) -- no excavation work until 3 days after the notice` -- work may
  begin on the 3rd day after the notice -- 3 clear days (the 4th day).
- **F7** r 298(1) "at least 5 days" -- `the hours of notice required (r 298)` -- 120 hours -- 5 calendar days.
- **F8** rr 168, 171, 204, 263, 283, 313 -- `the record must be kept until` -- 30 years from the day the record was made
  -- from the end of employment, or from the last exposure (as r 175(3) says for carcinogens).
- **F9** r 349 -- `the construction induction card is current (r 349)` -- current through the day 2 years after the last
  construction work -- lapsed on that day.
- **F10** r 64 "notifiable incident" -- `the entry permit must be kept until (r 64)` -- an incident s 38 of the Act
  requires to be notified -- any Part 5 incident.
- **F11** r 74 -- `Part 3.5 applies to the plant (r 74)` -- other plant: `NOTHING` (an open "applies to") -- `JUST FALSE`.
- **F12** r 124 -- `the plant is prescribed for incident notification (r 124)` -- any other plant: `JUST FALSE` (the
  Regulations close the list the Act hands them, ruling (a) on delegated definitions) -- `NOTHING`.
- **F13** r 319Y -- `the engineered stone work is prohibited (r 319Y)` -- before 1 July 2024, and for engineered stone that
  is not a benchtop, panel or slab: `NOTHING` -- `JUST FALSE`.
- **F14** r 99(3) -- `the rank of the guarding (r 99(3))` -- a fixed barrier where access is needed, or an interlocked one
  where it is not, is not a kind (a)-(b) permits (rank 99) -- it counts with the guarding of (c).
- **F15** the orders of control -- `the control duty was contravened` -- a measure the Part does not name counts as no
  measure (a contravention unless the risk was eliminated) -- `NOTHING`.
- **F16** r 37(c) "at least every 2 years" -- `the last day for the next audiometric test (r 37(c))` -- the same date 2
  years on -- the day before it.
- **F17** the reviews -- `the controls must be reviewed` -- plant (r 121, not encoded): `NOTHING` -- its occasions.
- **F18** r 176 -- `a written statement of carcinogen work is due (r 176)` -- no scheduled substance: `JUST FALSE` ("This
  regulation applies if") -- `NOTHING`.
- **F19** r 237 -- `the employee may see the employer's asbestos register (r 237)` -- a non-employee: `NOTHING` (r 237(b)-(d)
  give others copies or access on other terms) -- `JUST FALSE`.
- **F20** r 196(2) -- `r 196 was contravened` -- no monitoring yet and the month still running: `NOTHING` -- `JUST FALSE`.
- **F21** r 169 with r 154(2) -- `health monitoring is required (r 169)` -- lead in a lead process: `JUST FALSE` (Part 4.3
  governs) -- `NOTHING`.
- **F22** r 311 -- `an asbestos examination is required before starting` -- no examination before starting asbestos-related
  activities: `NOTHING` (silence) -- `JUST FALSE`.
- **F23** r 210 -- `r 210 was contravened` -- the standard and the duty to eliminate or reduce read together, so exposure
  at or under the standard can still be a contravention -- r 210(1) alone.
- **F24** r 200(1) -- `Was my medical examination after removal in time` -- removal on a medical practitioner's opinion
  (r 199(1)(b)), where r 200(1) "If an employee has been removed ... under 199(1)(a) or (c)" is unmet: `NOTHING` (the
  duty does not arise, so there is no deadline to meet) -- `JUST FALSE`.
- **F25** r 355(1) -- `Was WorkSafe notified of the excavation in time` -- Division 4 does not apply (r 354(2), (3), not
  enterable and no risk, or not a construction excavation under r 5): `NOTHING` (no notice was due, so it cannot be in or
  out of time), while `Must WorkSafe be notified of the excavation` answers `JUST FALSE` for the same facts -- `JUST TRUE`
  (nothing was late).
- **F26** r 205 -- `What is the most I can be fined` -- any provision other than r 205, which binds the employer or another
  duty-holder and not the employee: `NOTHING` -- `JUST 0`; and `What is the most the employer can be fined` gives `NOTHING`
  for r 205 (the employee's own offence) -- its 100 penalty units.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING` answers of the kinds the rulings describe. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "if" conditions (rr 19, 32, 37, 38, 49, 60, 166, 169, 176, 199, 262, 311, 332), "unless" (rr 63, 174, 216,
319L, 327, 341, 342), "means" and "is" definitions (r 5, rr 193, 319C, 321, 322), "does not apply" (rr 18(2), 41(2), 50,
154(2), 225(2), 354(2)-(3)), "while" (r 40(1)), the closed "except" of r 20, the periods the text fixes (rr 37, 64, 175(3),
195, 196, 198, 200, 262, 282, 311, 349, 355) and the "until" bar of r 201 (ruling (d)) give `JUST FALSE`; r 124 closes the
list s 37(2)(e)(i) hands to it (ruling (a)); open lists and scope limits with no "only" (r 74, r 237 for others, r 319Y
outside benchtops, panels and slabs), silence (r 311 before starting, r 195 unidentified processes) and figures outside the
deposit give `NOTHING`.

## What the Regulations turn out to say

1. **Withdrawn 2026-11-07: not a finding about the Regulations.** The first deposit had lost raised decimal points in r 5
   "safe oxygen level" ("195%", "235%", "198" and "239 kilopascals"), r 5 "construction excavation" ("15 metres") and
   r 178(n) ("01 square metres"). That was the converter dropping Word's Symbol-font decimal point, not the register. The
   deposit is now corrected and reads 19·5%, 23·5%, 19·8 and 23·9 kPa, 1·5 metres and 0·1 square metres (and 0·1% in the
   Schedule 10 and 11 carcinogen definitions, 0·1 tonnes for arsenic trioxide in Sch 14). The encoding had already read
   19.5%, 23.5% and 1.5 metres, so no value changed; the edges stay asserted. The number is kept so that the references
   to findings 2-11 still hold.
2. **The two units of the lead figures disagree near each figure.** Every blood lead figure is given in umol/L and ug/dL,
   but they are not exact conversions (1 umol/L is about 20.7 ug/dL): 0.48 umol/L is 9.95 ug/dL, not 10; 0.24 is 4.97, not
   5; 0.97 is 20.1, not 20; 0.72 is 14.9, not 15; 2.41 is 49.9, not 50. A result of 9.97 ug/dL is under "10 micrograms/
   decilitre" but over "0·48 micromoles/litre", so a woman of reproductive capacity must be removed under r 199(1A) on one
   unit and not on the other. Encoded in ug/dL; a lawyer should say which governs.
3. **Since 5 June 2020 pregnancy has no figure of its own.** r 199(1)(a)(iii) removed a pregnant or breastfeeding woman at
   15 ug/dL; r 199(1A) keeps only the man and the woman of reproductive capacity. A pregnant woman is removed at 10 (as a
   woman of reproductive capacity), or at 30 if she has given the r 179 written statement. Asserted (9 ug/dL, pregnant, 2026:
   not removed; 15 ug/dL, pregnant, 2019: removed).
4. **r 198(1A) has no interval for a woman of reproductive capacity at 10 ug/dL or more.** The old r 198(1)(b)(ii) covered
   "10 or more"; the new (1A)(b)(ii) stops at "less than 10", because r 199(1A) now removes her at 10. Asserted (`NOTHING`).
5. **The pre-start asbestos medical differs between the two kinds of removal work.** A limited asbestos removal worker needs
   none if examined "within the preceding 2 years" (r 262(3)(a)); a licensed removal worker needs one unless examined
   "within the preceding year" (r 282(2)(a)). r 311 (asbestos-related activities) sets no pre-start examination at all.
   Asserted.
6. **r 45 (ladders) carries no enforcement route.** It has neither an "Act compliance" note nor a penalty, unlike rr 44 and
   47 beside it. Read with s 21 of the Act it is still part of the s 21 duty, but r 7 does not say so. Asserted (`NOTHING`).
7. **"Notifiable incident" (r 64(b)) is defined neither in the Regulations nor in the Act** (the Act's Part 5 speaks of an
   "incident" and of notifying the Authority). Read as an incident s 38 requires to be notified (F10).
8. **Six 30-year record periods have no starting point.** rr 168, 171, 204, 263, 283 and 313 say "30 years" without saying
   from when; r 175(3) alone says "from the date on which the person last worked with" the substance (F8).
9. **The Regulations hold more incident and exposure notices than the Part-specific ones.** Besides r 355 (excavation),
   r 360 (major hazard facilities) and r 423A (mines), r 124 supplies the plant limb of the Act's s 37(2)(e)(i) (which
   plant's collapse or failure must be notified under s 38), and the Authority must be told of lead-risk work (r 195),
   removals from it (r 203), health monitoring recommending no exposure (r 170), engineered stone health monitoring
   (r 319ZD) and asbestos removal work (rr 298, 299). r 124 and r 195 are encoded.
10. **A road vehicle used off public roads is prescribed plant.** r 74(1)(b) excludes vehicles "except as provided in
   subregulation (4)", and r 74(4) applies Division 5 -- where r 124 sits -- to a vehicle used at a workplace other than a
   public road or rail. Asserted.
11. **Falls of 2 metres or less are outside Part 3.3 but not outside the law.** r 5 limits "fall" to more than 2 metres; the
   note to r 41(1) says s 21 of the Act still requires those risks to be managed. Asserted (Part 3.3: no at 2 m).

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Safe Work Australia's Workplace Exposure Standards (the figures r 165, r 166 and r 319C use) and the value of a penalty
  unit.
- The employer's seat over the same core; the designers', manufacturers' and suppliers' duties; Part 3.5 rr 100-123 for
  specific plant; Part 4.4 Divisions 5-8 in full; the principal contractor's plan (rr 333-337).
- A lawyer's view on findings 2, 3, 6 and 7 and on F2, F3, F4, F6 and F8; an independent test pass and a human gate.
