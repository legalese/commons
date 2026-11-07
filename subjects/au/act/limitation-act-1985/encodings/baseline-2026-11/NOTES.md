# Limitation Act 1985 (ACT), Parts 2 and 3 -- baseline encoding, the person bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. This encoding covers the Act's own time limits for claims for
personal injury, death, defamation and contribution, the general 6-year rule, and the whole of Part 3 that bears on
them (postponement for disability, the child-injury notice, the child health-service limit, notice to proceed,
confirmation, fraud and concealment, mistake, and the court extensions of Division 3.2). The choice-of-law provisions
(Division 4.4, s 54, s 21BC (3) (b)) are the separate `baseline-2026-11b` encoding beside this one, which was not touched;
nothing is imported from it.

Three modules: `lact-dates.l4` (date arithmetic, built-in date functions only, no daydate), `lact-claims.l4` (the rules,
the regulative rules and the 24 exported questions), `lact-cases.l4` (the worked cases). Three regulative rules (bring the
action by the last day; give a child's notice of intended claim within the relevant period, s 30A (2); begin a proceeding
within 6 months of a defendant's notice, s 30A (6)) are run by EVALTRACE inside the questions; no question takes a DEONTIC
or an EVENT.

## Edition

- **Act:** Limitation Act 1985 (ACT), A1985-66, Republication No 28 (R28), effective 26 November 2025, last amended by
  A2025-29, as deposited at `../../registers/source-bundle/A1985-66.txt` (converted from the register's DOCX, which the
  register marks as an unauthorised version; the authorised text is the register's PDF).
- **Numbers set elsewhere:** none that an answer needs. The information a s 30A notice must contain is prescribed by
  regulation (s 30A (4)); no regulation is deposited, and the encoding asks whether the notice had it.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (an action brought the day after the last day asserted to be in time) was run once in a
scratch copy, since deleted, and showed as "assertion failed" (148 satisfied, 1 failed, before the fix of 2026-11-07 added 8 cases).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lact-dates.l4` | 0 | 0 | 0 | 0 |
| `lact-claims.l4` | 0 | 0 | 0 | 0 |
| `lact-cases.l4` | 0 | 0 | 156 | 156 |

Every exported question has cases with hand-worked values, edges included: the last day and the day after; an action
brought before time began; 29 February to a common year; each kind of injury claim and each of the s 16A conditions
failing; s 10 for a work-related motor accident; s 16 with either period ending later; s 30B (3) with either period
ending first; a child injured at 9 and a worker injured at 17 (s 30 minority); each limb of "under a disability" and the
27th/28th day; s 30 with the disability beginning on and after the last day, ending before time began, still running,
ending in death, overlapping the start, ending on the day time began, beginning on it; s 4 for the last day and in-time
questions; the s 21B window at 55 and 56 days, on the last day and after it; s 30A's relevant
period ending on and the day before the limitation period's end; 6 months from 31 August; s 32 on the last day and the
day after, the day after time began, and a year with no 29 February; s 33 discovery before time began and after the period would have ended; every answer of s 36 and s 37.

**No mirror cases.** One seat.

## Seat

**The person bringing a claim** (`lact-claims.l4`): the plaintiff -- the injured person, the person defamed, the
relatives or personal representative of someone who died, the child (or the child's parent or guardian), the executor
of an estate, the wrongdoer who seeks contribution from another. "Which time limit applies to my claim?", "What is the
last day?", "Am I in time?", "Does being under 18 stop the clock?", "Must I give notice for my child's injury, and by
when?", "Does their acknowledgment give me more time?", "Can I ask the court for more time?".

The court gets no seat: what it decides ("just and reasonable", "compelling reason", "materially different", "reasonable
diligence") is asked as a fact or left to it in the answer's words. No second seat was written: the person answering the
claim meets the same limits as defences, with the same answers (s 30A (5), (6) and s 31 give the defendant steps; they are
encoded for what they mean to the claimant).

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed; no instrument sets a number used here.
- **The actors the text names.** Followed: the plaintiff (with the parent or guardian, s 30A), the defendant, the
  insurer (s 30A (3)), the guardian (s 31), the executor or administrator and personal representative (ss 37-39), the court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: "materially different" manner
  (s 21BA), "compelling reason" (s 30A (7)), discovery "with reasonable diligence" (ss 33, 34), "ought reasonably to have
  known" (s 30B); for "just and reasonable" (ss 21BB, 36, 38, 39, 40) the answers say the court may extend if it so
  decides and give the furthest day the Act allows.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "under a disability", "associate"
  (s 21BA), "relevant period" (s 30A), "confirms", "bound", "benefit" (s 32), "answerable" (s 33). Asked: "compensable
  injury" (Workers Compensation Act 1951), "motor accident claim" (Motor Accident Injuries Act 2019 ch 5), "child abuse"
  (Civil Law (Wrongs) Act 2002 s 114AA), "health service" (Human Rights Commission Act 2005 s 7), "concerns notice"
  (Civil Law (Wrongs) Act s 124A), "associated entity" (Corporations Act s 50AAA), "guardian" (Guardianship and
  Management of Property Act 1991).
- **One case is the text's natural unit.** Followed: one cause of action.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed: s 35 (application of Division 3.2 to every accrual date) and s 42
  (evidence of a deceased's knowledge) ask nothing of the claimant; s 41 (prior bar ineffective) is stated in the s 36
  answer.

## Scope

**In.** s 4 ((a) and (b), asked as one fact); the dictionary's "under a disability"; Part 2: s 10, s 11, s 16, s 16A, s 16AA, s 16B, s 21, s 21B, s 21BA,
s 21BB, s 21C; Part 3: s 30 (except (1) (e) and (3) (a)), s 30A, s 30B, s 31, s 32 (1), (2) (a), (4)-(6), s 33, s 34,
Division 3.2 (s 36, s 37, s 38, s 39, s 40; s 35, s 41, s 42 as above).

**Out, and why.**
- ss 5-8A (land, stolen goods, acquiescence, governments, derived rights, accrual for this Act only): preliminary and
  not met by a person bringing an injury, death, defamation or contribution claim; s 8 (claiming through another) is
  folded into the `@desc` texts.
- ss 12-15, 17-20 (accounts, deeds, judgments, penalties, arbitral awards, successive wrongs to goods, shipping, arrears
  of interest), s 21A (ACT revenue), Divisions 2.3 and 2.4 (mortgages, trusts): outside the focus (claims for injury,
  compensation and damages). Each is a fixed period like s 11 and could be added in the same shape.
- s 30 (1) (e) and (3) (a): the 2-year rule for s 15 and s 19 claims and the penalty exception go with those sections.
- s 32 (2) (b), (c), (3), (7): interest, income, mortgages and possession of property.
- s 21BC: its (3) (b) is in `baseline-2026-11b`; (1)-(3) (a) give no answer a claimant asks beyond s 21B.
- Part 4: extinction of title, arbitration, set-off, joint rights and liabilities, s 54 and Division 4.4 (in
  `baseline-2026-11b`), Division 4.5 (machinery).
- Several disabilities in one period (s 30 (2)) are not combined: the s 30 question takes one disability period (fork F7).
- What the court weighs when it decides (s 21BB (3), s 30B (4), s 36 (3), s 38 (2), s 39 (3), (5), s 40 (2)):
  considerations addressed to the court, not questions the claimant answers; the answers leave the decision to the court
  in its own words ("just and reasonable" and the like).
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** every "N years running from" / "N years or more after the day" -- `lact-dates.l4` -- the day itself is excluded and
  the last day is the same date N years on (29 February to 28 February); "within 6 months after" ends on the same date 6
  months on, or the month's last day; no move for weekends or holidays (Legislation Act 2001 s 151 not deposited) -- the
  day included (last day one day earlier), or a last day on a non-working day moved to the next working day.
- **F2** s 38 (1), s 39 (2), s 40 (1) "beginning on the day" -- the s 38, s 39 (1) route and s 40 questions -- that day counts,
  so the furthest day is the day before the anniversary -- read like "from" (the anniversary itself).
- **F3** s 30B (3) (a) "first knows ... (i) ...; or (ii) ..." -- `the Part 2 last day for` -- the earlier of the two days of
  knowledge -- the later (as "and" in s 16B and s 30A); see finding 3.
- **F4** s 30B and s 16B -- `the Part 2 time limit for` -- for a child's health-service claim s 30B alone sets the limit (s 9:
  Part 2 is subject to Part 3) -- s 16B also applies and the earlier ends the time; see finding 2.
- **F5** s 32 (1), s 33 (1), s 34 (1) "does not count" -- the s 32, s 33, s 34 questions -- the days on which the period ran
  "before the date" of the confirmation or discovery (from the day after time began, fork F1, to the day before that
  date) are added to the last day as plain days, so the date itself counts as a day of the period; whether a 29 February
  falls among the uncounted days or the added ones can move the result a day against a count in years -- the period
  counted again in years from that date, or that date itself also not counted (a day later).
- **F6** s 30 and s 16 -- `the last day for my injury claim` -- no minority postponement for a death claim (the claimants'
  ages are not asked); the s 30 question can be used for them -- postpone for a minor relative.
- **F7** s 30 (1), (2) -- `s 30 -- my last day after a disability` -- one disability period; while it continues, no last
  day (NOTHING: the period is suspended, the text gives no end) -- several periods combined; or a JUST answer.
- **F8** s 30A (1) (b) "a notice of claim has not been given ..., or a proceeding has not been begun" -- `s 30A -- must
  notice of the intended claim be given` -- neither has happened -- either has not happened.
- **F9** all Part 2 bars, an action brought before the day time began -- `the timing` -- in time (day 0) -- premature, a
  matter for the general law.
- **F10** s 21B (2), (3) -- `s 21B -- the last day for my defamation claim` -- "days remaining after the notice day" are the
  days after it up to the last day; the window is a notice day 0-55 days before the last day; new last day 56 days after
  the notice day -- the notice day itself counted as remaining (a day less).
- **F11** s 21C -- `the last day for my injury claim` -- NOTHING here means "the Act sets no last day" (the text's own
  words: "maintainable at any time"), not "the text is silent" -- an enumerated answer.
- **F12** s 16A and s 16AA for a work-related motor accident -- `the Part 2 time limit for` -- both apply and s 10 takes the
  earlier (3 years) -- the Motor Accident Injuries Act's ch 5 claim excludes s 16A.
- **F13** s 4 and s 21C (2) -- `which time limit applies to my injury claim` -- s 21C first ("despite ... another
  territory law"), then s 4 -- s 4 first.
- **F14** ss 16A, 16AA, 16B, 30B (2), (3) "not maintainable if brought N years after" -- every Part 3 question -- each is
  "a limitation period fixed by this Act" for Part 3 (as ss 30A (1) (c), 36 (5) treat it) -- they are bars, not periods,
  and Part 3's postponements do not touch them.
- **F15** s 30A (1) (d) "does not end within the relevant period" -- the same function -- a limitation period ending on the
  last day of the relevant period ends within it (s 30A does not apply) -- "within" excludes the last day.
- **F16** s 30 (1) (b), (c) -- `s 30 -- the last day after the disability` -- a disability that begins on or before the last
  day and ends on or after the day time began counts; the suspended days are those on which the period runs (from the
  day after time began, fork F1) and the person is under the disability (from the day it began up to, not including,
  the day it ends) -- only a disability present on the day time began.

Sites decided without a fork line: the dictionary's "under a disability", s 21BA (6) "associate", s 32 (2) (a), (5), (6)
and s 33 (4) ("if, but only if") are closed: FALSE (or the unchanged last day) when they fail; s 36 (5), (6) and s 37 (2)
are flat negatives, answered as the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

Most questions answer with a date or a choice from a list rather than a MAYBE BOOLEAN. The yes/no questions (under a
disability, s 30A must notice be given, s 31) answer FALSE as the text's no, from a closed definition or an "if" list.
Where a postponement section does not apply, its question returns the last day unchanged. Two questions use NOTHING:
the last day for a child abuse claim (fork F11) and the last day while still under a disability (fork F7). The rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The duties with a deadline are the regulative rules (`MUST ... WITHIN`, `LEST BREACH`): outside the period the answer is
"out of time" (ruling (a)); a bare "must" not done in s 30A is decided by s 30A (7) itself (damages for earlier services
lost unless the court excuses it).

## What the Act turns out to say

1. **Most personal injury time limits cannot be extended by the court.** s 36 (5) takes s 16AA (motor accidents), s 16B
   (every other personal injury claim) and death claims out of s 36. What remains for s 36 is s 16A (a common law claim for
   a compensable work injury) and the disease limb of s 30B. s 35 still names s 16 and s 16A, and the s 16 claim keeps its
   own extension in s 39. Asserted (the s 36 cases).
2. **s 16B and s 30B overlap on their words.** s 16B (1) covers every personal injury claim except those under ss 16, 16A,
   16AA, so it literally covers a child's health-service claim; s 36 (5) (b) would then shut s 36 to it, which would make
   s 36 (6) and the note to s 30B (3) ("can be extended under s 36") pointless. The encoding reads s 30B as displacing
   s 16B (fork F4). For the reviewer.
3. **s 30B (3) (a) says "or" where s 16B (2) (a) and s 30A (8) say "and".** Time runs from the day the child (or parent)
   first knows (i) of the disease "or" (ii) its link to someone else; elsewhere both must be known. Read as written: the
   earlier day (fork F3). Asserted. Possibly a drafting slip.
4. **An estate can get more time than the injured person could.** s 38 lets the court extend an estate's personal injury
   claim up to 6 years from the death whether or not the period had ended; s 36 (5) (b) does not reach s 38, so a s 16B
   claim closed to the living person can be extended for the estate. Not asserted beyond s 38's furthest day.
5. **s 21B's example agrees with the rule.** "7 days before ... 6 days left ... 50 days" and the rule as encoded both give
   a new last day 56 days after the notice day (fork F10). Asserted.
6. **s 39 (2) says "beginning on the day of death", s 39 (4) says "from the date of death".** Read as written, the two
   routes of s 39 end a day apart (fork F2). Asserted.
7. **For a 3-year limit, s 30 (1) (f) decides a minor's last day.** Where the person is under the disability when time
   begins (as a minor always is), the suspension counted in days never ends after "3 years after" the day the
   disability ends, so (f) gives the last day. A worker injured at 17 on 1 January 2020 (18 on 1 June 2020) has 151
   days suspended and gets 1 June 2023 either way. Asserted. (Corrected 2026-11-07: the first version counted the day
   time began as a suspended day and gave 2 June 2023, blaming 29 February.)
8. **The notes to s 16AA point to the Motor Accident Injuries Act's own 3-month windows** (ss 166, 220). Notes are not
   part of the Act (s 3); only s 16AA's 5 years is encoded.
9. **s 21C is the only bar the Act lifts entirely**, "despite anything elsewhere in this Act or another territory law",
   and it keeps the court's power to stay a proceeding unfair after long delay (s 21C (3)). Asserted (no last day).

## Before this is worth relying on

- The Legislation Act 2001 (ACT) for the counting of periods (forks F1, F2), not deposited.
- The regulations prescribing the s 30A notice's content, not deposited.
- The borrowed definitions (Workers Compensation Act 1951, Motor Accident Injuries Act 2019, Civil Law (Wrongs) Act
  2002 s 114AA, Human Rights Commission Act 2005 s 7), deposited in Commons under their own subjects but not linked here
  (the stable `l4` imports only within a folder).
- A lawyer's view on forks F2-F5, F8, F12, F14 and on findings 1-4; an independent test pass and a human gate.
