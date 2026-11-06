# Long Service Leave Act 2018 (Vic) -- baseline encoding, the employee

## Method

**Baseline.** Written straight from the deposited text and its formulas sidecar with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on
2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in `lsl-dates.l4` (built-in date
functions only, no daydate), the rules in `lsl-rules.l4`, and the employee's questions in `lsl-seat.l4`, which imports the
rules and never restates one. `lsl-cases.l4` holds the worked cases.

The focus asked for: long service leave entitlement, continuous employment, payment on termination, and the three
normal-weekly-hours formulas. The Act is small (58 sections, many repealed or machinery), so Part 2 is encoded nearly
whole, with the Part 3 recovery and adverse action provisions, the Division 3 duties an employee meets, and Parts 4 to 6.

## Edition

- **Act:** Long Service Leave Act 2018, Act No. 12/2018, Version No. 006, incorporating amendments as at 12 December 2025,
  deposited at `../../registers/source-bundle/long-service-leave-act-2018.txt` (sha256 b322f19a...0b92349 as committed,
  per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that
  file's `.meta.json` and `subjects/au/vic/README.md`). The version was the current one ("In force") on the register on
  6 November 2026. Not checked against the authorised PDF, which was not saved.
- **Formulas:** the three s 16(2) equations are embedded objects in the Word file and are read from the sidecar
  `../../registers/source-bundle/long-service-leave-act-2018.formulas.md` (18-12a006-F1 to F3: A = (B + C) / (52 - D),
  A = (B + C) / (260 - D), A = (B + C) / (D - E)), which is itself not yet checked against the authorised PDF. The "where"
  lists in the text agree with the letters used.
- **Numbers set elsewhere:** none of the Act's own figures depends on regulations (the Act has no regulations deposited
  and none sets an entitlement figure). The value of a penalty unit (Monetary Units Act 2004) and the penalty interest rate
  (Penalty Interest Rates Act 1983, s 26(7)) are not deposited: penalties are given in penalty units in the question
  descriptions, and the interest question answers only whether interest may be ordered. The Act's figures used: 7 years
  (ss 6, 50), 1/60th (s 6), 12 weeks (ss 11(5), (7), 12(3), (6)(a), (b), 19(1)), 52 weeks (ss 12(6)(c), 13, 14, 15(2),
  16(2), 27(2)), 104 weeks (ss 12(2)(d), 16(1)(b)), 260 weeks (ss 15(2), 16(2)), 1 day (s 18(1)), 6 years (s 26(4)),
  7 years (s 37(3)), 7 days (s 50(1)), 27 March 2006 (s 47).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lsl-dates.l4` | 0 | 0 | 0 | 0 |
| `lsl-rules.l4` | 0 | 0 | 0 | 0 |
| `lsl-seat.l4` | 0 | 0 | 0 | 0 |
| `lsl-cases.l4` | 0 | 0 | 195 | 195 |

Every exported question has cases, with the edges: 7 years completed on the last day and a day short; a week that does
not count pushing the 7 years back; 29 February as the day employment is counted from; re-employment on the last day of
12 and 52 weeks and the day after; casual parental leave at 104 weeks and just over; a casual gap of 12 and 13 weeks;
unpaid leave of 52 weeks and just over, with and without an agreement; each s 16 formula, a zero divisor in each, and
the greatest of three; payment of s 9 money on the day employment ends, before it, the day after, and a payment $1 short;
6 years to the day and a day over, from 29 February; 12 weeks' notice to the day and a day short; 7 days' notice to the
day and a day short; 7 years of record keeping to the day and a day over; every constructor of every choice that changes
an answer.

## Seat

**The employee** (`lsl-seat.l4`): the employee or former employee to whom the Act gives long service leave, including
casual and seasonal employees, apprentices, public sector employees and police. "Does the Act apply to me?", "From what
day is my employment counted?", "Does this absence break my continuous employment, and how much of it counts?", "Am I
entitled yet, and to how many weeks?", "What is my ordinary pay, and my normal weekly hours?", "Must my employer grant my
request?", "Must I go on leave when directed?", "What must I be paid when my employment ends, and was it paid on time?",
"By when must I sue?", "Did my employer take adverse action against me?". One question, s 10, is asked from the seat of
the **personal representative** of an employee who died, the person to whom s 10 gives the money and s 24(2) the right to
apply.

No seat for the employer, the Industrial Division of the Magistrates' Court, the Workforce Inspectorate Victoria or an
authorised officer. A seat for the employer could be added later as `lsl-seat-employer.l4` over the same rules.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no instrument sets an entitlement figure. The
  Fair Work Act 2009, awards and agreements are referred to only as facts (whether an agreement counts an absence, gives
  more favourable leave, or permits a payment in lieu).
- **The actors the text names.** Followed: employee, employer, one employer and new owner, personal representative,
  organisation (union), Industrial Division of the Magistrates' Court.
- **Judgments answered conditionally.** Followed: "reasonable business grounds" (ss 18, 22), "in the opinion of the
  Industrial Division" (ss 5(b), 23(2)), "is satisfied" (s 26(6)), "considers that it would be impracticable" (s 27(2)),
  "cannot reasonably be held responsible" (s 12(7)), "reasonable expectation of being re-engaged" (s 12(3)(d)),
  "reasonable concern" (s 12(10)(c)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: one employer (s 11), continuous employment
  (s 12), industrial action (s 12(9), (10)), the periods that count (ss 13, 14), ordinary pay and ordinary time rate of
  pay (s 15), normal weekly hours (s 16), adverse action (s 36(6)), protected accrued entitlement (s 48, as one fact).
  Asked: employee (s 3's open definition, as one fact), award (s 46), suitable employment (WIRC Act 2013), fair work
  instrument, reasonable business grounds (an open definition, its heads in the `@desc`).
- **One case.** One employment with one employer (as s 11 defines it), one absence per absence question.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3(1) definitions used (employee as a fact, reasonable business grounds as a fact); s 5; s 6; s 7; s 8(3) (s 8(2)
through the weeks taken); s 9; s 10(1), (3) (in the inputs); s 11; s 12 (including (9), (10)); s 13; s 14; s 15; s 16
with formulas F1 to F3; s 17; s 18; s 19; s 20; s 21; s 22; s 23; s 24(1)(g), (2) (in the question descriptions); s 26(2)
to (7); s 27(2) (and (1) in the description); s 34(2); s 35(1); s 36; s 37(2), (3), (6); ss 46, 47; ss 48, 49; s 50.

**Regulative rules:** two. s 9(2), (3) (the employer MUST pay the full amount WITHIN 0 days of the day employment ends,
a payment short of it not counting, LEST a breach that continues until paid) and s 26(4), (5) (the employee DOes commence
a proceeding, after a written demand, WITHIN the days to the last day of the 6 years, LEST out of time). Each is run by
EVALTRACE inside an exported question that takes only dates and facts, through the helper the County Court Act 1958 and
Victims of Crime encodings use (a CONSIDER on an EVALTRACE matches FULFILLED only).

**Out, and why:**
- ss 1, 2, 4 (purposes, commencement, Crown): no fact test.
- s 8(1) (the employer may agree to leave in advance): a permission of the employer with no test; s 8(2) is reflected in
  the weeks taken.
- s 10(2) (onus in a prosecution about the length of employment): prosecution procedure.
- s 11(3)(b), (6)(b), (11) (the new owner or contractor must not refuse accrued leave): reflected in the day employment is
  counted from; no separate question.
- s 24(1), (3) to (5), s 25, s 28 (jurisdiction, procedure, orders on conviction): the court's powers; the 6-year window of
  s 24(1)(g) is in the s 26 descriptions (finding 9).
- ss 29 to 33, 38 to 44 (authorised officers, information notices, self-incrimination, who may prosecute, judicial notice,
  imputed conduct, officers' liability, unincorporated associations): enforcement machinery; officers are not seats.
- s 34(1), s 35(2), s 37(4), (5) (the employer's and other persons' offences): the employer's side; s 37(7) (6 years to
  prosecute): prosecution procedure.
- s 45 (Part 4 applies despite anything else): reflected in s 47's question.
- ss 52, 53, Part 8 (Supreme Court jurisdiction, regulations, repeal of the 1992 Act, transitional provisions):
  machinery. **s 57 is not encoded**: an absence that started before the 2018 Act commenced is governed by the 1992 Act's
  rules for interruption and counting, so the absence questions can give the wrong answer for such an absence.
- Penalties: given in penalty units in descriptions only; the value of a penalty unit is not deposited.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 26(4), 37(3) "within 6 years after", "at least 7 years after" -- `the same day ... years after` -- the period
  ends at the end of the same day of the month that many years later; for 29 February in a common year, 28 February --
  the day before the anniversary, or 1 March.
- **F2** ss 11(5), 11(7)(d), 12(6)(a), (b), (c), 13(2) "within 12 [52] weeks after" -- `re-employed ... within ... weeks
  after` -- re-employment on the day 84 (364) days after is in time -- the 83rd (363rd) day as the last.
- **F3** s 6 "after completing 7 years of continuous employment" -- `s 6 -- I have completed 7 years` -- completed when the
  days counted (the day asked about included, less 7 days for each week that does not count) are at least the days in the
  7 calendar years after the day employment is counted from; so from 29 February 2016 the 7 years are complete with
  27 February 2023 counted -- 7 x 52 weeks, 7 x 365.25 days, or the anniversary taken from the shifted start.
- **F4** s 12(2)(d) "parental leave that is not longer than 104 weeks" -- `s 12 -- my employment is continuous despite the
  absence` -- for a casual, longer than 104 weeks: JUST FALSE (a period the text fixes) -- NOTHING (a scope limit with no
  "only").
- **F5** s 12(3) speaks only of a casual's gap "longer than 12 weeks" -- `s 12 ...`, `ss 13, 14 ...` -- a gap of 12 weeks or
  less is read as an ending and re-employment within 12 weeks under s 12(6)(a): continuous, and 0 weeks counted (s 14(b));
  a longer gap kept continuous by s 12(3): weeks counted NOTHING (finding 5) -- a short gap not an "absence" at all, or
  counted in full.
- **F6** s 6 "1/60th of the employee's total period of continuous employment less any period of long service leave taken
  during that period" -- `s 6 -- the weeks of long service leave` -- (the period / 60) less the weeks taken; the period in
  days / 7, so 7 years is 2557/420 = 6.088 weeks, not the 6.0667 weeks of 7 x 52 / 60 -- 1/60th of (the period less the
  leave taken) (finding 2), or a year of 52 weeks.
- **F7** s 8(3) "the amount paid ... for the leave (if any) in respect of which the employee will not become entitled" --
  `s 8(3) -- the most that may be deducted` -- the pay for the advance weeks beyond the weeks the employee had become
  entitled to at the end, in proportion -- all of it whenever the leave was taken in advance, or none once 7 years are
  completed.
- **F8** s 15(2) "the employee's ordinary time rate of pay is the greatest of ... the average weekly rate earned" --
  `s 15 -- my weekly ordinary pay` -- the greatest average is the weekly pay, not multiplied by hours (finding 1) --
  multiplied by normal weekly hours as s 15(1)(a) says, which would give hours squared in dollars.
- **F9** s 17(2) "normal weekly hours and ordinary time rate of pay are to be taken to be the greater of" two pairs --
  `s 17 -- my weekly pay on the hours and rate taken` -- the pair giving the greater weekly pay -- the greater hours and the
  greater rate taken separately.
- **F10** s 18 -- `s 18 -- my employer must grant my request` -- a request for less than 1 day is not a s 18(1) request:
  JUST FALSE; an employee with no leave to take: NOTHING (a duty whose "if" is unmet) -- JUST FALSE for both.
- **F11** s 19(1) "by giving the employee at least 12 weeks' written notice" -- `s 19 -- I must comply with the direction`
  -- the leave may start on the day 84 days after the notice; an unwritten or short notice is not a direction under s 19(1),
  so JUST FALSE -- 12 clear weeks (both days excluded), or a short notice valid from the day 12 weeks after it.
- **F12** ss 9(1), 10 -- `ss 9, 10 -- the full amount` -- the day employment ends (or the day of death) is counted as a day
  of employment -- not counted, as s 9(1)(a) puts the employee on leave that day.
- **F13** s 34(2) "except as permitted" -- `s 34 -- I may accept a payment in lieu` -- once the exception is met, JUST TRUE
  -- NOTHING (the Act only lifts the prohibition).
- **F14** s 37(6) -- `s 37(6) -- my employer must give me a copy of my record` -- no request yet: NOTHING (a duty whose
  "if" is unmet) -- JUST FALSE.
- **F15** s 50(1) "At least 7 days before entering into" -- `s 50 -- I was notified in time` -- notice on 1 March for an
  agreement on 8 March is in time -- 7 clear days (9 March).
- **F16** s 12(10)(a), (b) -- `s 12(9), (10) -- it is industrial action` -- the employees' action authorised by the employer
  and the employer's action authorised by the employees are one input ("the other side") -- two inputs.
- **F17** s 16(2) -- `s 16 -- my normal weekly hours` -- a formula with nothing to divide by gives nothing, and the
  greatest of the others is taken; NOTHING where none can be worked -- the formula failing the whole question.
- **F18** s 13(1)(d)(iii), s 14(a)(iii) "or is any other form of leave provided for under the relevant employment
  agreement" -- `ss 13, 14 -- the weeks of the absence that count` -- reached only by the choice "other leave my employment
  agreement provides for"; annual, parental and carer's leave unpaid beyond 52 weeks count only with an agreement that
  counts them (finding 3) -- any unpaid leave an agreement provides for counted in full.
- **F19** s 36 -- `s 36 -- my employer took adverse action against me` -- no reason of s 36 alleged: NOTHING -- JUST FALSE.
- **F20** s 23 -- `s 23 -- the term can have effect` -- a term that does not annul, vary or exclude the Act: NOTHING -- JUST
  TRUE.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "does not apply" of s 5 (flat negative); the period of s 6 ("after completing 7 years"); the "if"
conditions of ss 11(5), (7), 12(3), (6), (7), 13(2), 16(1), 17(1), 26(6), 27(2), 36(6), 47; the "unless" of ss 18(2),
22(2), 23(2); the "means" definitions of industrial action (s 12(9), (10)) and protected accrued entitlement (s 48); the
flat negatives of ss 23(1), 34(2), 35(1); the periods of ss 19(1), 26(4), 50(1) give `JUST FALSE`. The open definition of
employee (s 3(1) "includes"), the absences s 12 or ss 13, 14 do not speak of, a zero divisor in a s 16 formula, and the
scope limits of ss 23, 26 (before the money is owed), 35, 36, 37 give `NOTHING` (*open definition*, *silent*, *limited by
its own wording*).

## What the Act turns out to say

1. **s 15(2) defines a rate of pay as a weekly amount.** s 15(1)(a) calculates ordinary pay "on the employee's normal
   weekly hours at the employee's ordinary time rate of pay"; s 15(2), where no rate is fixed, makes the ordinary time rate
   of pay "the greatest of ... the average weekly rate earned". Read literally, a weekly figure is multiplied by weekly
   hours. Encoded as the weekly pay itself (F8). Asserted.
2. **s 6 can be read two ways.** "1/60th of the employee's total period of continuous employment less any period of long
   service leave taken during that period" may subtract the leave taken from the entitlement (taken here) or from the
   period before dividing (F6). After 10 years with 2 weeks taken the two give 6.698 and 8.664 weeks. Asserted on the
   reading taken.
3. **The 52-week cap on unpaid leave may rarely bite.** s 13(1)(d)(iii) and s 14(a)(iii) count unpaid leave beyond 52 weeks
   in full where it "is any other form of leave provided for under the relevant employment agreement". Since awards and
   agreements commonly provide for parental and carer's leave, read widely this lets most long unpaid leave count in full;
   encoded narrowly (F18). Asserted.
4. **The gap after an apprenticeship is neither counted nor excluded.** s 12(6)(c) keeps employment continuous where an
   apprentice is re-employed within 52 weeks; s 14(b) excludes only the absences after s 12(6)(a) and (b), and s 13 does not
   mention (6)(c) (s 13(2) counts the apprenticeship itself). Answered NOTHING. Asserted.
5. **A casual's long gap kept continuous by s 12(3) is not dealt with by ss 13 or 14.** Answered NOTHING (F5). Asserted.
6. **The s 16 formulas assume a long enough employment.** F1 and F2 divide by 52 and 260 weeks less unpaid leave even where
   the employee has worked fewer weeks (leave in advance under s 8, a short employment ended by death under s 10), and F1
   divides by zero after 52 weeks of unpaid leave. Answered NOTHING for a zero divisor (F17). Asserted.
7. **s 43(2)(j) specifies s 37(1), which was repealed** by No. 14/2021 s 68. A dangling reference; not encoded.
8. **s 19 does not limit a direction to leave the employee has.** An employer may direct "long service leave at a specified
   time and for a specified period" on 12 weeks' notice; nothing ties the period to the employee's entitlement, or
   requires 7 years; s 24(1)(d) lets the court decide "the length of long service leave". The question asks only the notice
   and any court order.
9. **Two six-year windows.** s 26(4) runs 6 years from when "the employee's entitlement to the money arises"; s 24(1)(g)
   gives jurisdiction over amounts owing "within the 6 years immediately before the day on which the application is made".
   Encoded s 26(4); the s 24 window is named in the description.
10. **No payment before 7 years, whatever ends the employment.** s 9 pays out only leave "to which the employee is entitled",
    and s 6 gives none before 7 years: the Act has no pro rata payment on dismissal, illness or death before 7 years.
    Asserted (0).
11. **Small inconsistencies of terms.** s 10(3)(a) speaks of "ordinary rate of pay" where the Act defines "ordinary time
    rate of pay"; s 50(2)(a) of "7 years of continuous service" where s 6 says "continuous employment". Read as the same.

## Before this is worth relying on

- Check the conversion and the formulas sidecar against the authorised PDF.
- Encode s 57 (absences that started before the Act commenced) so that the absence questions can take a start date.
- A lawyer's view on findings 1 to 3 and forks F3, F5, F6, F7, F8, F9 and F18, an independent test pass and a human gate.
- An employer seat (`lsl-seat-employer.l4`) with mirror cases, over the same rules.
