# Health Practitioner Regulation National Law (Victoria) Act 2009 -- baseline encoding, the health practitioner

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The dates are in `hprnl-dates.l4` (built-in
date functions only, no daydate), the rules and the practitioner's exported questions in `hprnl-practitioner.l4` (each
exported question calls a rule defined beside it), and the worked cases in `hprnl-cases-practitioner.l4`.

The focus: the Act only applies the Health Practitioner Regulation National Law in Victoria; the National Law itself
(the Schedule to the Health Practitioner Regulation National Law Act 2009 of Queensland) is not in the deposited text.
The Act is short (ss 1-9, with s 8 and s 7(e), (i) repealed), so **the whole Act is encoded**. What it gives a person
is small but real: the day the National Law began to apply in Victoria, VCAT as the responsible tribunal, the
Magistrates' Court for the National Law's magistrates, the 28-day limit for applying to VCAT against an appellable
decision (with its transitional rule), and the list of Victorian Acts that do not reach the National Law (Victoria)
(among them the Freedom of Information Act 1982 and the Health Records Act 2001, which a person in a health claim might
expect to use against the national scheme's records).

## Edition

- **Act:** Health Practitioner Regulation National Law (Victoria) Act 2009, Act No. 79/2009, Version No. 006,
  incorporating amendments as at 31 May 2019, deposited at
  `../../registers/source-bundle/health-practitioner-regulation-national-law-victoria-act-2009.txt` (sha256
  d702ff08...26609d7fc8 per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on
  6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Version 006 was the current version
  ("In force") on 2026-11-06. Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** none. The Act sets its own days (1 July 2010, 1 July 2012) and period (28 days). No
  regulations are made under it.
- **Not deposited, and asked as facts:** the National Law (what an "appellable decision" under its s 199 is; which
  matters it gives to the responsible tribunal or to a magistrate). The VCAT Act 1998 is deposited and encoded beside
  this subject (`subjects/au/vic/victorian-civil-and-administrative-tribunal-act-1998/`); its s 126(1) (VCAT may extend a
  time limit fixed by an enabling enactment) is named in the answers but not encoded here, since IMPORT cannot reach
  another subject's folder.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hprnl-dates.l4` | 0 | 0 | 0 | 0 |
| `hprnl-practitioner.l4` | 0 | 0 | 0 | 0 |
| `hprnl-cases-practitioner.l4` | 0 | 0 | 59 | 59 |

Every exported question has cases, with the edges: 30 June and 1 July 2010 (s 2); lodging on 30 June and 1 July 2012
(s 9(1)); 29 and 30 July 2012 (s 9(2)); a decision notified on 30 June 2012 and appealed 29 days later (s 9(2) governs);
the day of notice, day 28 and day 29 (s 6A(2)), across a month end, a year end and 29 February 2028; no notice yet, and
lodging before the day of notice; every Act in s 7 and one that is not.

## Seat

**The health practitioner** (`hprnl-practitioner.l4`): the person to whom the National Law is applied in Victoria -- a
registered health practitioner, an applicant for registration or a student -- and in particular the person who is the
subject of an appellable decision. "Does the National Law apply to me as a law of Victoria?", "Where will my matter be
heard?", "Can I apply to VCAT in time?", "By when must I apply to VCAT?", "Does this Victorian Act apply to the National
Law in Victoria?". The last question is the same for anyone dealing with the scheme, for example a patient who made a
notification about a practitioner.

No other party has duties under this Act. No seat for the National Boards, the national agency, VCAT, the Magistrates'
Court or the Minister.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: there are none.
- **The actors the text names.** Followed: the person who is the subject of an appellable decision, VCAT, a magistrate,
  the Magistrates' Court of Victoria.
- **Judgments answered conditionally.** None in the text.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: s 5 (magistrate, magistrates' court, this
  jurisdiction), s 6 (responsible tribunal), s 3(1) (the name). Asked: "appellable decision" (National Law s 199), and
  which matters the National Law gives to the responsible tribunal or to a magistrate. s 3(2) (terms have the National
  Law's meanings) is why those are asked.
- **One case.** One person, one decision (or one matter).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** s 1 (purpose) is noted only; s 2 (commencement) is in, because the day it
  gives decides whether the National Law applies at all.

## Scope

**In:** s 2 (as the day the National Law began to apply); s 3 (definitions, as noted above); s 4 (the National Law
applies as a law of Victoria); s 5 (magistrate, magistrates' court, this jurisdiction); s 6 (VCAT the responsible
tribunal); s 6A (the right to apply to VCAT and the 28-day limit); s 7 (the excluded Victorian Acts, as at 31 May 2019);
s 9 (the transitional rule for s 6A).

**Regulative rule:** one. ss 6A(2), 9(2): I DO lodge the application for review WITHIN 28 days (counted from the day of
notice, or from 1 July 2012), LEST the limit is not met. It is run by EVALTRACE inside the exported questions, which take
only dates and yes/no facts, through the helper the Victims of Crime, County Court and Legal Profession Uniform Law
encodings use (a CONSIDER on an EVALTRACE matches FULFILLED only). The BREACH marks only that the limit was not met: not
appealing is not a wrong.

**Out, and why:**
- s 1 (purpose): no rule.
- s 7 before 31 May 2019 (for example before (ga) was inserted on 17 September 2014), and the repealed s 7(e), (i) and
  s 8: the deposited version only, and the repealed text is not in it.
- The National Law itself: not deposited (the Schedule to the Queensland Act). Everything it gives a practitioner or a
  patient -- registration, notifications, health and performance assessments, immediate action, panels, tribunal
  powers, and what an "appellable decision" is -- is outside this encoding.
- VCAT's power to extend time (VCAT Act s 126) and how an application is made: in the VCAT Act, named only.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 6A(2), 9(2) "no more than 28 days after" -- `ss 6A(2), 9(2) -- lodge within the days allowed`, `the last
  day to lodge` -- the last day is the day plus 28 (lodging on day 28 is in time, day 29 is not) -- the day plus 27.
- **F2** s 9(2) -- `ss 6A, 9 -- my application to VCAT`, `the last day to lodge` -- for a decision made before 1 July
  2012, s 9(2) alone sets the limit (29 July 2012), whenever notice was given -- s 6A(2) applies as well (s 9(1) makes
  it apply to any application lodged on or after 1 July 2012), and the earlier of the two days governs.
- **F3** s 6A(2) "after the person has been given notice" -- `ss 6A, 9 -- my application to VCAT` -- before notice is
  given, the 28 days have not begun and an application is in time -- an application cannot be lodged until notice is
  given.
- **F4** s 6A(1) "A person who is the subject of an appellable decision ... may appeal" -- `ss 6A, 9 -- my application
  to VCAT` -- a person who is not the subject, or a decision that is not appellable, is "not covered" (a scope limit with
  no "only": NOTHING-kind) -- "no".
- **F5** s 9(1) "Section 6A applies to an application lodged on or after 1 July 2012" -- same function -- an application
  lodged before 1 July 2012 is "not covered" (the section is silent on it) -- "no".
- **F6** s 7 -- `s 7 -- the Victorian Act applies to the National Law (Victoria)` -- a Victorian Act not listed:
  NOTHING (the list is not closed with "only", and other Acts may or may not apply) -- JUST TRUE.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 2's day and the 28-day periods of ss 6A(2), 9(2) are fixed in the text's words, so before 1 July 2010
the National Law does not apply (`JUST FALSE`) and a late application is "no, out of time"; s 7's "do not apply" is a
flat negative (`JUST FALSE`); an Act s 7 does not list, a person who is not the subject of an appellable decision, and an
application lodged before 1 July 2012 are outside scope limits with no "only" (`NOTHING` or a "not covered"
constructor).

## What the Act turns out to say

1. **The Act is a shell; the substance is not deposited.** Everything a practitioner's or patient's claim turns on --
   registration, notifications, immediate action, what is an appellable decision, what VCAT may do -- is in the National
   Law (the Schedule to the Queensland Act), which s 4 adopts "as in force from time to time". Encoding it needs that
   Schedule deposited (as a Queensland or a Victorian subject); until then "appellable decision" is asked.
2. **s 9(2) can close the time before the person is told.** For a decision made before 1 July 2012, s 9(2) sets the
   last day at 28 days after 1 July 2012 with no reference to notice; a person notified after 29 July 2012 of such a
   decision was out of time before notice (F2). Asserted (decided 30 June 2012, never notified, lodged 30 July 2012:
   "no, out of time (s 9(2))"). s 9(1) and (2) also overlap: s 9(1) makes s 6A apply to every application lodged on or
   after 1 July 2012, including one against a pre-July decision, so for a decision notified on 30 June 2012 s 6A(2)
   gives 28 July 2012 and s 9(2) gives 29 July 2012. Asserted on the s 9(2) reading (lodged 29 July 2012: in time).
3. **The limit is not the last word.** VCAT Act s 126(1) lets VCAT extend "any time limit fixed by or under an enabling
   enactment for the commencement of a proceeding", even after it has expired (s 126(3)), unless that would cause
   irremediable prejudice (s 126(4)). The answers say "out of time" and name s 126; they do not decide an extension.
4. **The Interpretation of Legislation Act 1984 is shut out of the National Law but not out of s 6A.** s 7(f) excludes
   it from "the Health Practitioner Regulation National Law (Victoria)" and its instruments; s 6A and s 9 are this
   Act's own provisions, so the Interpretation of Legislation Act's rules on reckoning periods would reach them. That
   Act is not deposited; if its rules move a last day that falls on a weekend or holiday, the answers here would change
   at that edge. Not checked.
5. **"Appeal ... by lodging an application for review".** s 6A(1) calls the step an appeal and the document an
   application for review; s 9(2) speaks only of the application. The encoding uses "apply to VCAT for review".
6. **Freedom of information and health records.** s 7(c) and (d) mean the Victorian Freedom of Information Act 1982 and
   Health Records Act 2001 do not apply to the National Law (Victoria) or its instruments. A person seeking records held
   under the national scheme has to look to whatever the National Law itself provides (not deposited, not checked).
7. **s 8 was repealed by this Act itself.** The side note records s 8 inserted by No. 13/2010 and "repealed by No.
   79/2009 s. 8(5)", that is by a subsection of the inserted section, on 1 July 2014 (endnote 2). A self-repealing
   section; nothing turns on it now.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit the Health Practitioner Regulation National Law (the Schedule to the Queensland Act) and encode its s 199
  and the notification and registration provisions a practitioner or patient meets; then "appellable decision" can be
  worked out rather than asked.
- Deposit the Interpretation of Legislation Act 1984 and check finding 4.
- A lawyer's view on findings 2 and 4 and forks F1, F2 and F3, an independent test pass and a human gate.
