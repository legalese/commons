# Labour Hire Licensing Act 2018 (Vic) -- baseline encoding, the provider, the host and the worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Seven modules:

- `lhl-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`);
- `lhl-rules.l4` -- the law: who provides labour hire services and who is a worker (ss 7 to 11), the s 3 tiers, whether a
  licence is in force (ss 26, 28, 39, 40), the Part 2 prohibitions (ss 13 to 16) and s 95, the s 18 bar, what goes with an
  application (ss 17, 23, 28, 29), what the Authority must decide (ss 24, 29, 32(4)), the holder's dates (ss 26, 29(7),
  32(3), 34, 35, 42, 67), three duties with deadlines as regulative rules (ss 16(3), 34, 43/44) with their trace helper,
  ss 46, 86 and 91, the penalty table (s 94 and the offences), Part 6 (ss 93, 97, 98), s 102 and s 105;
- `lhl-seat.l4` -- the provider's 26 questions;
- `lhl-seat-host.l4` -- the host's 9 questions;
- `lhl-seat-worker.l4` -- the worker's 5 questions;
- `lhl-cases.l4`, `lhl-cases-host.l4` (with the mirror cases across all three seats), `lhl-cases-worker.l4` -- the cases.

Every question has `@export` and a `@desc` on every input, and is grouped under `§§` headings in the Act's order.

## Edition

- **Act:** Labour Hire Licensing Act 2018, Act No. 25/2018, Version No. 009, incorporating amendments as at 1 October 2026
  (the register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/labour-hire-licensing-act-2018.txt` (sha256 f6e42b90...10f4d8 as committed), a plain-text
  conversion of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and `subjects/au/vic/README.md`).
  Not checked against the authorised PDF, which was not saved. This version includes the amendments of the Labour Hire
  Legislation Amendment (Licensing) Act 2025 (No. 57/2025: new ss 7, 8, 22, 49, 67A, the financial viability tests, s 12
  repealed) and No. 15/2026.
- **Numbers set elsewhere:** the Act fixes its own periods and penalties. The Labour Hire Licensing Regulations (the classes
  excluded by ss 10 and 11, the circumstances of ss 7(3), 8(4) and 18(1), the renewal period of s 28(1), the fees, the number
  of nominated officers, the prescribed changes of s 44, other tier amounts) are not deposited: each is a yes/no input, or
  the Act's own figure is used (the tier amounts). The value of a penalty unit (Monetary Units Act 2004) is not deposited:
  penalties are answered in penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lhl-dates.l4` | 0 | 0 | 0 | 0 |
| `lhl-rules.l4` | 0 | 0 | 0 | 0 |
| `lhl-seat.l4` | 0 | 0 | 0 | 0 |
| `lhl-seat-host.l4` | 0 | 0 | 0 | 0 |
| `lhl-seat-worker.l4` | 0 | 0 | 0 | 0 |
| `lhl-cases.l4` | 0 | 0 | 150 | 150 |
| `lhl-cases-host.l4` | 0 | 0 | 49 | 49 |
| `lhl-cases-worker.l4` | 0 | 0 | 22 | 22 |

Every expected value was worked by hand from the text, with the edges: every head of ss 7, 8 and 9 with and without each
element, the s 10 and s 11 exclusions and the prescribed circumstances; the licence on its first day, the day before, the day
before the expiry date and on it, a cancellation's day and the day before, a renewal pending, decided, out of the prescribed
period, made after the expiry date and made on it; each s 18 bar on its last day and the next, 3 months from 30 November;
each tier boundary and the one-dollar gap; each 14, 28 and 30-day period on its last day and the next; anniversaries of 29
February; each penalty column and the s 93(6) split for an individual and a company; each eligible applicant under s 102.

## Seats

**The provider** (`lhl-seat.l4`, the first seat): the person who provides, or wants to provide, labour hire services -- a
sole trader, partners in a business run jointly, or the officer answering for a company -- as applicant and as licence
holder. This is the person the licensing system is applied to. "Do I provide labour hire services?", "Is my licence in
force?", "Am I breaking s 13, may I advertise?", "May I apply yet?", "What must go with my application?", "Must the
Authority grant it?", "How long can it last?", "By when must I report, pay, respond, notify?", "Must I show my licence to
this person?", "Can I refuse to answer?", "Can I go to VCAT, by when?", "What is the most I can be ordered to pay, and until
when can I be pursued or prosecuted?".

**The host** (`lhl-seat-host.l4`): the business that uses labour hire (s 3 "host") and the "client" of s 16 -- the person
the focus's "offences for using an unlicensed provider" are aimed at. "Is my arrangement labour hire?", "May I use this
provider (s 15)?", "Is it an avoidance arrangement (s 16(2)), and did I report it in time (s 16(3))?", "Am I caught as
someone involved (s 95)?", "Must the provider show me its licence?", penalties and time limits.

**The worker** (`lhl-seat-worker.l4`): the individual supplied, recruited or placed (s 9). "Am I a worker under the Act?",
"Is the business that supplies me unlicensed?", "Must it show me its licence?", "Is it forbidden to sack or threaten me for
using the Act (s 86)?", "What is the most the person who did it can be ordered to pay?". The Act gives the worker no claim
of their own: only the Authority applies for civil penalties (s 93(1)) and only the Commissioner prosecutes (s 104).

The three seats draw on the same rules, so they cannot disagree about the law; the mirror cases in `lhl-cases-host.l4` ask
the same facts from all three. Each keeps its own names.

No seat for the Labour Hire Licensing Authority, the Commissioner, inspectors, police, VCAT or the courts: their
satisfaction, beliefs, decisions and orders are asked as facts; their duties to the person (s 32(3) time to respond, s 42
show cause, s 46 inspection on request) are encoded as what the person must be given, and by when.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the regulations are not deposited, so what they
  prescribe is an input and the Act's own tier amounts are used. A prescribed other amount, period or date would change the
  answers.
- **The actors the text names.** Followed: provider, host, client, supplier, worker, applicant, holder, relevant person,
  nominated officer, interested person, the Authority, the Commissioner, inspectors, police, VCAT, the Magistrates' and
  Supreme Courts.
- **Judgments answered conditionally.** Followed: "satisfied", "believes on reasonable grounds", "reasonable excuse",
  "knows or has reasonable grounds to suspect", "appropriate in all the circumstances", "wholly or principally" and "as soon
  as reasonably practicable" (a number of days) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "provides labour hire services" (ss 7, 8, 10),
  "worker" (ss 9, 11), the tiers, "eligible applicant" (s 102(2)) and the licence's being "in force" are worked out;
  "employee", "independent contractor", "accommodation", "detriment", "incriminate" are asked.
- **One case.** One arrangement, one licence, one application, one decision.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The focus: licensing of labour hire providers, and the prohibitions on using an unlicensed one. Parts 1 (Division 2), 2 and
3 are encoded where they give the person a fact test; Parts 5 to 7 for what the person meets.

**In:** ss 3 (provides labour hire services, worker, tier 1, 2 and 3 business, host, provider), 7, 8, 9, 10, 11, 13, 14, 15,
16, 17(4), (5), (5A), 18, 23, 24(1) to (3), 26, 28(1) (the prescribed period as an input), (2)(d), (3), (4), 29(1) to (3),
(7), 32(3)(b), (4)(a), 34(3), (5), 35(1), (2), 36 (penalty), 39(3), 40(2)(b), 42(2)(c), 43, 44(1), 46, 67(2), (4), 67A(4),
86, 91, 93(2)(a), (6), (7), 94, 95, 97, 98(1), 101, 102, 105, and the penalties written under ss 46, 67(5), 67A(5), 74(2),
79(2), 84(2), 85(2), 87, 88.

**Regulative rules:** three. s 34: the licence holder MUST give the annual information WITHIN 28 days of the start of the
reporting period, LEST breach of a condition (s 36); run inside `Did I give my annual information in time`. ss 43, 44: the
holder MUST notify a change WITHIN 30 days, LEST breach; run inside `Did I notify the change in time`. s 16(3): the client
MUST notify the Authority WITHIN the days that were reasonably practicable, LEST breach; run inside `Did I report the
avoidance arrangement in time`. Each takes only dates, numbers and yes/no facts.

**Out, and why:**
- ss 1, 2, 4, 5, 6 (purposes, commencement, objects, the Crown, extraterritorial application): no fact test for the person.
  s 6(2) (work performed in Victoria; arrangements made in Victoria for work outside it) is assumed to hold.
- ss 17(1) to (3), (6) to (8), 19, 20, 21, 30, 31, 47: what an application must contain and the Authority's power to ask for
  more. They enter s 24 as yes/no inputs ("the application includes the required information"); s 17(7) and s 29(8) (joint
  applications) could be added.
- s 22 (fit and proper person): matters the Authority "must have regard to", with no outcome fixed by the Act; the
  Authority's satisfaction is an input to s 24.
- ss 25, 29(5), (6) (the contents of the notices of decision), s 27 (not transferable), ss 33, 35A, 37, 38, 39(1), (2), 40(1),
  41, 45, 48, 49: the Authority's powers and discretions, or administration. Their penalties are in the table; their review
  is in s 102. s 41 (cancellation on request) and s 48(4), (5) (searching the Register) could be added.
- Part 4 (the Authority and the Commissioner): machinery.
- Part 5 ss 64 to 66, 67(1), (3), 67A(1) to (3), (5), 68, 70 to 84, 85(1), (3), 89, 90, 92: inspectors' powers and duties,
  except the penalties a person meets (in the table) and s 67(4); s 82 (copies within 21 days, return after 3 months) could
  be added for the person whose documents were seized; s 90 needs the prescribed infringement offences (not deposited).
- ss 96, 99, 100 (payment to the Consolidated Fund, criminal proceedings after civil, inadmissibility): no fact test the
  person states that changes an answer here.
- ss 103, 103A (secrecy, public interest disclosure): duties of officials. s 104 (who prosecutes) is noted in the worker's
  seat. ss 106 to 115: machinery.
- Part 8 (ss 116 to 119): transitional. Part 2 commenced on 29 April 2019 (endnotes), so the transition period ended on 29
  October 2019; s 117(2) to (6) help only a person who applied before then and whose application or review is still
  undecided. Part 9 (ss 120, 121): transitional.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "3 months" (s 18(1)(b)), "12 months" (s 34(5)), "anniversary" (s 35(1)), "years" (ss 18, 26, 29(7), 67(2), 93(7),
  105) -- `the date` n `months on from` -- the same day of the month, or that month's last day where it is shorter (29 February
  2028 plus 12 months is 28 February 2029; 30 November 2026 plus 3 months is 28 February 2027) -- 1 March (rolling over).
- **F2** s 26(b)(i) "remains in force until the date (the expiry date)" -- `the licence is in force on`,
  `ss 26, 29(7) -- the last day the licence can be in force` -- the expiry date is the first day not in force (read with s
  28(4) "in force from the expiry date"), so the last day in force is the day before the third anniversary -- in force on
  the expiry date itself.
- **F3** s 28(4) "taken, despite the expiry of the licence, to have been in force from the expiry date" -- `the licence is in
  force on` -- once the late application is made, the licence counts as in force for the gap between the expiry date and the
  application too -- only from the application.
- **F4** s 18(1)(a) "within the preceding 2 years", (b) "during the period of 3 months immediately preceding" -- `s 18 -- the
  first day I may apply` -- barred until the day before the second anniversary of the cancellation, or the day before the day
  3 months after the refusal; free on that day; only a cancellation or refusal on or before the proposed day counts -- the
  anniversary itself still barred.
- **F5** s 23(2) "an application for a licence" -- `ss 17, 23, 28, 29 -- what must go with the application` -- a renewal by a
  holder not conducting a labour hire business gets no s 23 compliance declaration (s 23(1) and (2) both fail) -- s 23(2)
  applies to renewals too.
- **F6** s 34(3)(a) "within 28 days of the start of the reporting period" -- `s 34(3) -- the last day for the annual
  information` -- the 28th day after the first day of the period -- the 27th (the first day counted).
- **F7** s 46 "upon request" -- `s 46 -- the licence must be produced` -- nobody has asked: JUST FALSE (a duty whose "if" is
  unmet, decided case by case) -- NOTHING.
- **F8** "within 6 years of the contravention" (s 93(7)), "within 6 years after the date" (s 105), "during the period of 6
  years after" (s 67(2)) -- the sixth anniversary is the last day -- the day before it.
- **F9** s 102(1)(g) "a decision to vary a licence under section 38" -- `s 102 -- I may apply to VCAT for review` -- a refusal
  to vary on the holder's application: NOTHING (finding 5) -- JUST TRUE, reading s 102(4) and VCAT Act s 4 (a refusal is a
  decision) into "a decision to vary".
- **F10** s 16(3) "as soon as reasonably practicable" -- `s 16(3) -- notify the Authority of the avoidance arrangement` -- the
  days that were reasonably practicable are an input (a judgment) -- a fixed period.
- **F11** the worker's `Is the business that supplies me unlicensed` -- the regulations' deeming of ss 7(3), 8(4) is fixed at
  no (a worker cannot state it); the s 10 and s 11 exclusions are asked -- ask the deeming too.
- **F12** the provider's s 13 and s 14 questions take "my licence is in force" as yes/no (the answer to the in-force question),
  so the in-force question's NOTHING (finding 3) must be resolved by the person first -- take the in-force facts again.
- **F13** s 3 tiers, paragraph (a) "for the 4 quarters immediately preceding" and (b) "did not operate in the 4 quarters" --
  `s 3 -- the tier of the business` -- one turnover figure, actual or projected, is asked; a business that operated for part
  of the 4 quarters is taken under (a) on the turnover it had -- under (b), projected (finding 7).
- **F14** s 24(2), s 29(2) "may grant ... if ... satisfied that it is appropriate" -- `ss 24, 29, 32(4) -- what the Authority
  must do` -- when satisfied, the answer is "may grant" (the Authority may still decide not to, and must then refuse under (3))
  -- "must grant".

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "has the meaning given" definition of providing labour hire services (ss 3, 7, 8, with the flat "does not"
of s 10), the "if" definition of worker (s 9, with the flat "is not" of s 11), the "means" definitions of the tiers and of
eligible applicant (s 102(2)), the "unless" of ss 13, 14, 15(1), the "does not apply if" of s 15(2), the "applies if" and
"if the client knows" of s 16(1), (2), the "if" of s 18(1), the flat "is not in force" of s 39(3), the flat "not a
reasonable excuse" of s 91(2), and the periods of ss 18, 28, 34, 42, 43, 93(7), 102 give `JUST FALSE`. The scope limits of
ss 13, 15(1), 86, 91 and 95 (conduct the provision does not name), the unclosed list of s 46, the decisions s 102 does not
list, and the renewal application made on the expiry date give `NOTHING` (*limited by its own wording*, *silent*). s 46 with
no request (fork F7) and s 18 events after the proposed day are decided case by case.

## What the Act turns out to say

1. **A recruitment or placement business is caught only if it also arranges accommodation.** s 8(1)(d) makes procuring or
   providing accommodation an element; an agency that places workers whom the host pays, and arranges no accommodation, is
   not providing labour hire services under s 8(1) (it may still be under s 7 if what it supplies is labour by workers it
   pays). Asserted (the mirror cases).
2. **The tier ranges leave a one-dollar gap.** Tier 1 is "no more than $2 000 000", tier 2 "between $2 000 001 and $10 000
   000": a turnover of more than $2 000 000 but less than $2 000 001 (say $2 000 000.50, turnover being "total ordinary
   income") is in no tier. The Act uses the tiers only in s 17(2)(fa); what turns on them (fees) is in the regulations.
   Asserted.
3. **A renewal application made on the expiry date is neither "before" nor "after" it.** s 28(3) speaks of an application
   "before the expiry date", s 28(4) of one "after the expiry date"; neither covers the expiry date itself, so on that day and
   after the Act does not say whether the licence is in force. Asserted (NOTHING).
4. **s 15(2)(a) asks less of the Register than s 16(1)(b).** A host is excused under s 15(2)(a) if the provider "was included
   in the Register as the holder of a licence" -- not "a licence that is in force", the words s 16(1)(b) uses. A Register
   entry for a suspended or lapsed licence still excuses the host. Asserted.
5. **s 102 does not list a refusal to vary.** s 38(7)(b) requires the notice of a refusal to vary a licence on the holder's
   application to state "that the holder of the licence may apply to VCAT for review of the decision", but s 102(1)(g) lists
   only "a decision to vary a licence". s 102(4) (VCAT Act s 4: a refusal is a decision) may close the gap. Asserted
   (NOTHING; fork F9).
6. **The annual information is due at the start of the period it reports on.** s 34(1) requires information "in respect of
   each reporting period" (workers placed "during the reporting period", compliance "throughout the reporting period"), but s
   34(3)(a) makes it due "within 28 days of the start of the reporting period" -- before most of the period has happened. The
   preceding period is probably meant; the encoding gives the date the text states. Asserted (the dates).
7. **Part-year businesses and the tiers.** Paragraph (a) of each tier needs turnover "for the 4 quarters immediately
   preceding", paragraph (b) a business that "did not operate in the 4 quarters"; a business that operated for some of them
   fits neither cleanly (fork F13).
8. **Every new applicant declares compliance, even one not yet in business.** s 17(4)(b) requires "a declaration of
   compliance with the laws specified in section 23(1A)" with every application for a licence, while s 23(2) gives an
   applicant not yet conducting a business a plan declaration instead of the s 23(1) one. The encoding lists both for a new
   entrant. Asserted.
9. **s 117(5), (6) speak of an "offence" under ss 15 and 16, which are civil penalty provisions** (s 94 items 3 to 5), and s
   101 says a contravention of one "is not an offence". Transitional and spent (the transition period ended on 29 October
   2019); out of scope, noted.
10. **The worker has no claim under the Act.** Civil penalties are sought only by the Authority (s 93(1)), prosecutions only by
    the Commissioner or a person the Commissioner authorises (s 104), and penalties go to the Consolidated Fund (s 96). s 93(3)
    lets the court make orders "to stop the conduct or remedy its effects", but only on the Authority's application.
11. **The conversion drops "Penalty:" before some penalties.** In the deposited text the penalties of ss 46, 85(2), 87(1),
   (2), 88(1), (2) and 103(2) stand on their own lines without the "Penalty:" label the others carry; read here as penalties.
   Check against the authorised PDF.

## Before relying on it

- Deposit the Labour Hire Licensing Regulations 2018 and replace the prescribed-matter inputs (ss 7(3), 8(4), 10, 11, 18(1),
  28(1), 44) and the fees, and check whether they prescribe other tier amounts or reporting periods.
- Check the conversion against the authorised PDF (finding 11).
- A lawyer's view on findings 3, 5 and 6 and on forks F2, F3 and F4; an independent test pass; the human gates.
- Penalty units in dollars need the Monetary Units Act 2004 value for the financial year.
