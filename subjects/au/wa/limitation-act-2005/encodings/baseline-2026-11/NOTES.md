# Limitation Act 2005 (WA) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`la-dates.l4`, built-in
date functions only, no daydate), the rules in `la-rules.l4`, and the claimant's questions in `la-seat.l4`, which imports the
rules and restates none. The cases are in `la-cases.l4`.

## Edition

- **Act:** Limitation Act 2005 (WA), No. 19 of 2005, compilation as deposited at
  `../../registers/source-bundle/mrdoc_47979.txt` (sha256 b194c75d...4ea48e as committed), retrieved from the Western
  Australian Legislation website on 7 September 2026. It includes the amendments of No. 3 of 2018 (child sexual abuse
  actions, from 1 July 2018), No. 21 of 2023 (workers compensation, from 1 July 2024) and No. 32 of 2024 (provisional
  damages for dust diseases, from 1 December 2024).
- **Numbers set elsewhere:** none. The Act fixes all its own periods; no regulations set them. The days fixed in the Act or
  its compilation table are encoded: commencement day 15 November 2005 (s 3, s 2 and the table), 1 July 2018 (s 89),
  1 January 1984 (s 56(1)(b)), 14 November 2005 (s 56(4)(b)(ii), in the @desc).
- **Borrowed terms asked as facts:** "sexual abuse" (s 6A, undefined); "subsequent action", "subsequent damages",
  "subsequent dust disease" (Civil Liability Act 2002 Part 2 Division 5, not deposited here); the workers' compensation
  injury of s 56(4A) and the medical panel findings (Workers' Compensation and Injury Management Act 1981, Workers
  Compensation and Injury Management Act 2023); "guardian" in the Guardianship and Administration Act 1990 sense.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `la-dates.l4` | 0 | 0 | 0 | 0 |
| `la-rules.l4` | 0 | 0 | 0 | 0 |
| `la-seat.l4` | 0 | 0 | 0 | 0 |
| `la-cases.l4` | 0 | 0 | 145 | 145 |

Every expected value was worked by hand from the text, with the edges: each exported question at least twice; the last
day to commence and the day after (10 March 2023 / 11 March 2023; 31 May 2026 / 1 June 2026 at the 21st birthday); a period
from 29 February; the day before and the day of commencement day (14 and 15 November 2005); the 15th and 18th birthdays;
the s 32 and s 35 suspensions just inside and far past their caps; the s 36 30-year cap; each medical panel threshold at
and just under it (30 / 29, 25 / 24, 25 / 24.9); s 7 on 15 and 16 November 2011; a confirmation on the accrual day, on
the last day and the day after; the regulative rule on its last day and the day after.

## Seat

**The claimant** (`la-seat.l4`): the individual to whom a cause of action accrues and who brings or proposes to bring the
action -- the injured person, a worker with an asbestos or silica dust disease, a survivor of child sexual abuse, a family
member suing for a death under the Fatal Accidents Act 1959, a party to a contract or deed. "When did my claim accrue?",
"Is my dust injury significant, and do I know the relevant facts?", "Is there no limitation period for my abuse claim?",
"By when must I start my action?", "Can I still start it on this day?", "Can the court give me more time, and to when?",
"Who has to prove it?", "Does my agreed time limit work?", "Did their acknowledgment or payment give me more time?",
"Can I sue now on a claim barred or settled before 1 July 2018?". One question (s 81) is asked by the same individual
when answering a claim with a counterclaim. No seat for the court, the defendant, an insurer or the Minister: the
court's satisfaction, leave and orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; none is borrowed.
- **The actors the text names.** Followed: the plaintiff, the defendant (and a person for whom the defendant is vicariously
  liable), the guardian, the person in a close relationship, the personal representative, the court, the Supreme Court.
- **Judgments answered conditionally.** Followed: "satisfied", "reasonable", "ought reasonably", "just and reasonable",
  "sufficiently serious", "not insignificant" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "child sexual abuse action" (s 6A(1), (6)),
  "previously barred / settled cause of action" (s 89), "knowledge of the relevant facts" and "significant" (s 56(2)-(4)),
  "cause of action (childbirth)" (s 7(1)), "confirmation" (s 46) are worked out; "mental disability" (s 3) and "person in a
  close relationship" (ss 33(3), 36(4)) are asked with their definitions in the @desc, because each turns on a judgment
  ("unable to make reasonable judgments", "reasonable ... not to commence").
- **One case.** One cause of action, of one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 4(1), 6, 6A (and 90), 6B, 7, 12(1), 13, 14, 16, 17, 18, 30, 31, 32, 33, 35, 36, 38, 39, 41, 42, 45, 46(1)(a), (b),
47, 48, 49 and 50 (one fact: whether the confirmation binds the person sued), 52, 53, 55, 56, 57, 79, 81, 89, 91(1)-(3),
(6), 92(2), (3), (7). ss 43, 44, 92(4)-(6) and 91(4), (5) are in the descriptions of the questions they bear on; ss 34, 37,
38(4), 41(4), 42(4) (defamation exclusions) and s 58 (when a contribution claim accrues) are in the descriptions only.

**Regulative rule:** one. The time bar ("cannot be commenced if ... have elapsed") as what the plaintiff must do to keep the
action: `PARTY the plaintiff MUST issue the writ or other originating application WITHIN` the days from accrual to the
last day, `LEST BREACH ... BECAUSE` the limitation period has expired. It is run by EVALTRACE inside the exported question
`Can I still commence my action on this day`, which takes only plain facts, through a helper in the shape of the Civil
Procedure Act 2010 (Vic) encoding's.

**Out, and why:**
- ss 1, 2, 3 (as a whole), 6A(7), (8), 10, 11, 12(2): machinery and interpretation (s 3's definitions used where the
  rules need them; the Minister's review in s 6A(7), (8) gives no one a right).
- s 5 (no revival of actions barred under the repealed law): affects only causes barred before 15 November 2005, which
  the encoding answers "the law before 15 November 2005 decides"; ss 6A(3), 89 carry its disapplication for abuse claims.
- s 8, s 15, s 40 (defamation): not in the claims focus.
- s 9 (limitation provisions in other written laws prevail, except s 6A): a pointer outside the Act; other Acts' time
  limits (workers' compensation, motor injury) are for their own encodings. Said in the main question's description.
- ss 19-29 (land, mortgages, interest, possession, foreclosure, redemption, accounts, equitable actions, tax, arbitration),
  s 46(1)(c), s 51, s 54, ss 59-64, Part 4 Division 2 (ss 65-73), Part 5
  (ss 74-78), ss 80, 82-88: property, trust, tax and arbitration law, not in the claims focus; the main question answers
  "not answered by this encoding" for those kinds of action.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "if N years have elapsed since" (ss 13-18, 30, 35(2), 36) -- `the anniversary` -- the day of the event excluded, so
  the last day is the anniversary; from 29 February, 28 February in a year without one -- 1 March.
- **F2** "if the person has reached 21 [25] years of age" (ss 31, 32, 33) and "up to when the plaintiff reaches 21" (s 41) --
  `Division 1 -- the last day of`, `s 41 -- ...` -- the age is reached on the birthday, so the last day is the day before --
  the birthday itself.
- **F3** "a longer limitation period" (ss 30(2), 31(2), 33(2), 36(2)) -- `Division 1 -- ...`, `Division 2 -- ...` --
  compared by the day each period ends -- compared by length in years.
- **F4** s 33 -- `Division 1 -- the last day of` -- where it applies it replaces ss 30-32 (s 32(3): "subject to section 33"),
  giving until the day before the 25th birthday -- a further bar cumulative with ss 30-31, which would make it pointless.
- **F5** s 32(2) -- same -- the 21st-birthday cap applies to the s 30 (under 15) period with its suspension; where Part 2
  gives longer, that period applies unchanged -- (a) and (b) as two bars, the earlier winning.
- **F6** s 35 -- `Division 2 -- the last day of` -- the suspension extends the Part 2 period, capped at 12 years, and never
  shortens it -- the 12-year cap as an absolute bar even where the Part 2 period is 12 years.
- **F7** s 36(1) where the relationship has not ceased -- same -- only s 36(3)'s 30 years bound the time -- the period
  otherwise applicable.
- **F8** s 56(3), (4) -- `s 56(3), (4) -- the dust injury is significant` -- both must hold: the panel threshold (or
  agreement) is necessary, not sufficient -- the panel finding settles significance by itself.
- **F9** s 47 "(a) after the limitation period ... begins to run; and (b) before that limitation period expires" --
  `ss 46-50 -- what the confirmation does` -- a confirmation on the accrual day or on the last day counts, and the whole
  Part 2 period runs again from it -- "after" excluding the accrual day; or the Division 1 and 2 periods restarting too.
- **F10** s 7: a cause of action that is not a childbirth one -- `s 7(2) -- ...` -- `NOTHING` (a scope limit) -- `JUST
  FALSE`. A childbirth one accrued on or after commencement day: `JUST FALSE` (the "if" fails).
- **F11** s 92(7) where the settlement related solely to the abuse -- `s 92(7) -- ...` -- `NOTHING` (the Act is silent) --
  the whole amount.
- **F12** s 6A(6) -- the main question -- a Fatal Accidents Act claim marked as child sexual abuse takes the ordinary
  3 years; an estate's survival claim is excluded through the s 6A question -- a survival claim brought through the
  "any other" kind treated as abuse.
- **F13** s 53(2) -- `Division 1 extends the claim`, `Division 2 extends the claim` -- "a further extension of time is not
  allowed" read as switching off Divisions 1 and 2 entirely for the inheriting person -- only the court extensions of
  ss 41, 42.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (s 6A(1), s 89) and "does not include" (s 6A(6)), "cannot be commenced if" (the time
bar, s 7(2)), "is of no effect if" (s 45(2)), "is of no effect unless" (s 48), "must not be treated as significant unless"
(s 56(4)), "is not to extend time ... unless" (ss 41(3), 42(3)), "may not" (s 91(6)), the "if" conditions of ss 38(2), 39(3),
56(3), 91(3), 92(7) and the "when" of s 56(2) give `JUST FALSE` (or "this section gives no extension on these facts").
`NOTHING` is answered before accrual and where the old law or another kind of action decides (*points outside the text*), for
s 7 outside childbirth and for s 92(7) where the settlement was solely about the abuse or said the share (*limited by its
own wording*, *silent*).

## What the Act turns out to say

1. **s 33 is drafted as a bar, not a grant.** "An action ... cannot be commenced if person A has reached 25 years of age"
   would, read alone, add a bar to ss 30 and 31 and change nothing. Read with its place in a Division headed "Extension"
   and with s 32(3) ("subject to section 33"), it gives until the 25th birthday. Encoded so (F4). Asserted.
2. **s 32(2) joins two bars with "or".** Read literally, "(a) if the person has reached 21 ... or (b) in the case where
   Part 2 ... provides for a longer limitation period, if that limitation period has expired" would cut a longer Part 2
   period at 21. Encoded with (a) for the s 30 and s 31 periods and (b) for the Part 2 period (F5). Asserted.
3. **s 33(2) compares with Division 3 only,** where ss 31(2), 32(2) and 36(2) compare with Divisions 2 or 3. No case
   arises in which the general 6 years from an accrual under 18 run past the 25th birthday, so nothing turns on it.
4. **s 39(5): "either that person or a guardian".** Whose ignorance at the expiry, and whose awareness starts the 3 years,
   when the child (or the person with a disability) and the guardian knew different things, is not said. Encoded as one
   set of facts "you (or your guardian)". Not asserted either way.
5. **s 55(1)(b) has no verb.** "the first symptom, clinical sign or other manifestation of personal injury consistent with
   ..." is listed as an "event" that "occurs"; read as the day it first appears. Asserted.
6. **The 1981 Act thresholds in s 56(4)(b)** (30% disability under s 93D(2), 25% whole of person impairment under ss 146A
   and 146C) remain in force for injuries before the 2023 Act's Part 7 Division 2 commenced (s 56(4A)). Encoded with all
   three panel findings; which one a worker has is asked. Asserted at each threshold.
7. **s 6(1) applies s 56 to dust injuries whose cause accrued before 15 November 2005,** but s 6(2) then keeps the old
   period. The accrual question answers such dates; the time-limit question answers "the law before 15 November 2005
   decides". Asserted (14 and 15 November 2005).
8. **s 7's six years ended on 15 November 2011.** The section still matters only through the Part 3 extensions it keeps
   (ss 32, 33, 35, 36, 38, 39, 41, 42, counting from 15 November 2005); those are not wired into the s 7 question, which
   says so in its description.
9. **"Sexual abuse" (s 6A) is not defined** in the Act; asked as a fact. **s 6B depends on terms of the Civil Liability Act
   2002 Part 2 Division 5**, not deposited with this subject; asked as one fact.
10. **s 53(2) says "a further extension of time is not allowed by reason of" person B's age or disability** without saying
    which provisions it switches off. Read as all of Divisions 1 and 2 (F13); the court extensions under ss 41, 42 are not
    wired to it. Asserted.

## Before this is worth relying on

- Check the text against the authorised PDF and the current compilation (retrieved 7 September 2026).
- The Civil Liability Act 2002 (WA) Part 2 Division 5 definitions for s 6B, and the Interpretation Act 1984 (WA) rule for
  reckoning periods (F1).
- Wire the s 7 question into the Part 3 machinery; add s 58 (contribution accrual) as a question; add defamation if wanted.
- A lawyer's view on findings 1, 2, 4 and 10 and forks F3-F6, F9, F13; an independent test pass and a human gate.
