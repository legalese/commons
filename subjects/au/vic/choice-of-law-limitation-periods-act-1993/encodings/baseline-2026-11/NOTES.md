# Choice of Law (Limitation Periods) Act 1993 (Victoria) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The dates are in `clpa-dates.l4` (built-in
date functions only, no daydate), the rules and the claimant's exported questions in `clpa-claimant.l4` (each exported
question calls a rule defined beside it), and the worked cases in `clpa-cases-claimant.l4`.

The Act is six sections, so **the whole Act is encoded**. It is a gate in front of a limitation period: when the law of
another State, a Territory or New Zealand governs a claim before a court (or arbitrator) in Victoria, that place's
limitation law counts as substantive and the court applies it (s 5), and any discretion it gives, such as a power to
extend time, is exercised as that place's courts would (s 6). For a person injured interstate and suing in Victoria,
this decides whether the Limitation of Actions Act 1958 or the other place's limitation law sets the time to sue.

## Edition

- **Act:** Choice of Law (Limitation Periods) Act 1993, Act No. 100/1993, Version No. 003, version as at 16 August 2012,
  deposited at `../../registers/source-bundle/choice-of-law-limitation-periods-act-1993.txt` (text sha256
  91f67e97...037ffcc49 per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on
  7 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Version 003 was the current version
  ("In force") on 2026-11-07; the endnotes record no amendments. Not checked against the authorised PDF, which was not
  saved.
- **Numbers set elsewhere:** none. The Act's one day is its commencement, 23 November 1993 (s 2 with the endnotes). No
  regulations are made under it.
- **Not deposited, and asked as facts:** the other place's limitation law (its period, the day the period runs from,
  whether it gives a discretion, and any extension the court grants under it); which place's substantive law governs
  the claim (the court's choice-of-law decision). The Limitation of Actions Act 1958 is deposited and encoded beside this
  subject (`subjects/au/vic/limitation-of-actions-act-1958/encodings/baseline-2026-11/`); it applies where Victorian law
  governs, and is named in the answers, not encoded here, since IMPORT cannot reach another subject's folder.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `clpa-dates.l4` | 0 | 0 | 0 | 0 |
| `clpa-claimant.l4` | 0 | 0 | 0 | 0 |
| `clpa-cases-claimant.l4` | 0 | 0 | 83 | 83 |

Every exported question has cases, with the edges: proceedings instituted on 22 and 23 November 1993 (s 4), a cause of
action arising on 22 and 23 November 1993; each kind of place and each forum (s 5, s 6); a law with and without a
discretion (s 6); the last day of the period, the day before and the day after; an extended day and the day after it;
a 29 February start (3, 4 and 6 years on), a 31 August start with a 6-month period, a period of no length, and a
proceeding started before the period runs.

## Seat

**The claimant** (`clpa-claimant.l4`): the person who brings a claim before a court or an arbitrator in Victoria where
the law of another State, a Territory or New Zealand governs it -- typically someone injured in another State who sues
in Victoria. "Is the time limit I face a limitation law?", "Does the Act reach my proceeding?", "Whose limitation law
will the court apply?", "How will the court use a discretion under that law?", "Am I in time?", "By when must I start?".

The Act puts no duty or liability on any party; the person who answers the claim meets the same rules from the other
side (the same answers tell a defendant which limitation defence is available), so no second seat is written. No seat
for the court, the arbitrator or the courts of the other place.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: there are none.
- **The actors the text names.** Followed: a court of the State (including an arbitrator), the courts of the other place.
- **Judgments answered conditionally.** Which place's substantive law governs (the court's choice of law), whether the
  court extends time, and how it exercises a discretion "as far as practicable" in "comparable cases" are asked or
  stated, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: s 3 "limitation law" (from two facts) and
  "court includes arbitrator". Asked: "State", "Territory" (by choice from a list), "substantive law" and its governing
  place, and everything the other place's limitation law says.
- **One case.** One claim, one proceeding (or arbitration).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** s 1 (purpose) is noted only; s 2 (commencement) is in, because s 4 turns on
  the day it gives.

## Scope

**In:** s 2 (as the day s 4 counts from); s 3 (limitation law; court includes arbitrator); s 4 (causes of action that
arose earlier are reached; proceedings instituted earlier are not); s 5 (another place's limitation law is part of its
substantive law and is applied); s 6 (that place's discretions exercised as its courts would). What s 5 means for the
claimant in days -- in time or not under that place's period, and the last day -- is worked out from the period and
starting day asked as facts.

**Regulative rule:** one. s 5: I DO start my proceeding or arbitration WITHIN the days that place's limitation period
allows (counted from the day that law says the period runs from), LEST the period is not met. It is run by EVALTRACE
inside the exported questions, which take only dates, numbers, yes/no facts and choices, through the helper the Health
Practitioner Regulation National Law (Victoria), Victims of Crime and County Court encodings use (a CONSIDER on an
EVALTRACE matches FULFILLED only). The BREACH marks only that the period was not met: not suing is not a wrong.

**Out, and why:**
- s 1 (purpose): no rule.
- The other place's limitation law (for example the Limitation Act 1969 of New South Wales, the Limitation Act 2010 of
  New Zealand): not deposited here, and not this Act. Its period, starting day and discretions are inputs.
- The choice of law itself (which place's substantive law governs a claim): the Act takes it as given ("is to govern").
- Victoria's own limitation law where Victorian law governs, and the limitation law of any country other than New
  Zealand: the Act says nothing; the answers say "outside this Act".

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3 "court includes arbitrator", read into s 5 "a court of this State" and s 6 "a court of the State" --
  `ss 3, 5, 6 -- a court of this State` -- an arbitrator counts when the arbitration is in Victoria -- an arbitrator
  counts wherever seated, if Victorian law (and so this Act) is applied by them; or "of this State" limits the
  definition to Victorian courts only.
- **F2** s 5, s 6 "another State, a Territory" (undefined in the Act) -- `Place`, `ss 5, 6 -- another place being
  another State, a Territory or New Zealand` -- any Australian State other than Victoria, and any Australian Territory
  (the person picks) -- the Interpretation of Legislation Act 1984's definitions (not deposited) may narrow "Territory"
  (for example to internal Territories).
- **F3** s 4 "instituted before the commencement" -- `s 4 -- instituted before the commencement` -- a proceeding
  instituted on 23 November 1993 is reached (the Act operates from the start of the day of assent) -- one instituted
  earlier on that day than the assent is not.
- **F4** s 5 and s 6 "If ..." unmet -- `s 5 -- the limitation law the court applies`, `s 6 -- how the discretion is
  exercised` -- "s 5 (or s 6) does not apply" (a condition the text introduces with "if": JUST FALSE kind), with "which
  limitation law applies is outside this Act" -- "not covered" (NOTHING kind), since the Act is silent on what the court
  does instead.
- **F5** s 5 applied to a period of years and months -- `the date ... years and ... months after`, `started by the last
  day` -- the period ends at the end of the corresponding day (the day the period runs from is excluded), so starting on
  that day is in time and the day after is not -- the period ends the day before the corresponding day. How the other
  place counts its own period is that place's law, not deposited.
- **F6** same functions, a start on a day the end month lacks (29 February, 31 August plus 6 months) -- the last day of
  that month (28 February) -- the first day of the next month.
- **F7** `started by the last day` -- a proceeding started before the day the period runs from is in time -- "not
  covered" (a claim started before its cause of action accrues may fail for other reasons; that is not this Act).
- **F8** s 6 -- `s 6 -- how the discretion is exercised` -- s 6 applies whenever a Victorian court exercises a discretion
  under another place's limitation law, whether or not s 5 is what brought that law in; it is not tied to s 5 -- s 6
  reaches only a discretion in a limitation law applied under s 5.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 3 is a "means" definition (`JUST FALSE` when a limb fails); s 4's "does not apply" is a flat negative
(a "no" constructor); s 5's and s 6's "If" conditions, when unmet, give "does not apply" constructors (F4); the
"by when" question answers `NOTHING` where s 5 does not apply, because the Act then sets no period at all.

## What the Act turns out to say

1. **The Act decides whose limitation law, never what it says.** Every answer about time depends on the other place's
   limitation law, which is not deposited here. The encoding asks its period and starting day, and so cannot tell a
   claimant what the period is (for example, whether the other place uses a discoverability start or an accrual start).
2. **New Zealand is the only foreign place.** s 5 reaches the law of another State, a Territory or New Zealand. Where the
   law of any other country governs, the Act is silent, and the deposited Limitation of Actions Act 1958 has no
   provision on foreign limitation laws either (a search of its text for "foreign" and "substantive" finds only s 5B(3),
   on defamation). Which limitation law a Victorian court applies to a claim governed by, say, English law is outside
   both deposited Acts. Asserted ("s 5 does not apply ... outside this Act").
3. **"A court of this State" and arbitrators.** s 3 makes "court" include an arbitrator, but the Act does not say what
   makes an arbitrator "of this State" (F1).
4. **s 3 names no extension law, but s 6 assumes one.** "Limitation law" is defined by a law that limits liability or
   bars an action "by reference to the time when a proceeding ... is commenced"; it does not mention laws that extend
   or shorten that time. s 6 nonetheless speaks of "a discretion conferred under a limitation law", so a power to
   extend is treated as part of the limitation law it qualifies. The Workplace Injury Rehabilitation and Compensation
   Act 2013 s 322 is more explicit: its "substantive law" includes "a law prescribing the time within which an action
   must be brought (including a law providing for the extension or abridgment of that time)".
5. **A notice step is not a limitation law.** A requirement to give notice of a claim within a time (common in injury
   schemes) bars nothing "by reference to the time when a proceeding ... is commenced", so s 3 does not make it one, and
   s 5 does not carry it across as part of the other place's limitation law (it may still come across as substantive
   law under the general choice-of-law rules, which are outside the Act). Asserted (`Is this a limitation law` TRUE
   FALSE is JUST FALSE).
6. **Work injury claims have a second gate.** For a claim for damages against an employer for a work injury, the
   Workplace Injury Rehabilitation and Compensation Act 2013 Part 7 Division 1 (s 319) picks the governing law (the law
   of the State whose workers' compensation scheme gives the entitlement; s 319(5): "State includes Territory", not New
   Zealand), and s 322(b), (c) make time limits part of that substantive law. Where both Acts apply they point the same
   way; this encoding does not import that Division (it is another subject).
7. **"Is to govern" is borrowed.** s 5 applies only "if the substantive law of another place ... is to govern a claim";
   which law governs is the court's choice-of-law decision (for a wrong done within Australia, the High Court's choice
   of law rule generally points to the law of the place of the wrong). The rule is case law, not deposited, and is
   asked as a fact.
8. **A stray "s. 5" line.** The deposited text has a line "s. 5" between the heading of s 6 and its text. It looks like a
   running-head or margin reference that the conversion kept; it has no effect on the encoding. Check against the
   authorised PDF.

## Before this is worth relying on

- Check the conversion against the authorised PDF (finding 8).
- Deposit and encode the limitation laws of the other States, the Territories and New Zealand, so that the period and
  its starting day can be worked out rather than asked; then a seat layer could join them to this gate (in one folder).
- Deposit the Interpretation of Legislation Act 1984 and check F2 and F3 and how a period is counted (F5, F6).
- A lawyer's view on findings 2, 4 and 5 and forks F1, F4, F5 and F8, an independent test pass and a human gate.
