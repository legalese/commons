# State Administrative Tribunal Act 2004 (WA) -- baseline encoding, the applicant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`sat-dates.l4`,
built-in date functions only, no daydate), the rules in `sat-rules.l4`, and the applicant's questions in `sat-seat.l4`,
which imports the rules and restates none. The cases are in `sat-cases.l4`.

The Act is procedural: it is the machinery through which many WA claims and reviews are run (the enabling Acts send the
matter to the Tribunal). The focus taken is the provisions a person bringing or answering a matter meets: which
jurisdiction, notice and reasons, the effect of a review, representation, starting and losing a proceeding, evidence,
decisions and reasons, enforcement, costs, more time, minor proceedings, offences, and appeal.

## Edition

- **Act:** State Administrative Tribunal Act 2004 (WA), No. 54 of 2004, compilation as deposited at
  `../../registers/source-bundle/mrdoc_49227.txt` (sha256 6f343d91...c4d07fc8 as committed), retrieved from the Western
  Australian Legislation website on 7 September 2026. Its compilation table runs to the Towing Services Act 2024 (No. 37 of
  2024, from 10 January 2025). Two amendments are listed as uncommenced: the Aquatic Resources Management Act 2016 s 371 and
  the Evidence Act 2025 s 492(1); neither is encoded.
- **Numbers set elsewhere:** the State Administrative Tribunal Rules 2004 and Regulations 2004 are not deposited. Where the
  Act hands a time limit, an exemption, a fee or a class of proceeding to them (ss 20(2)(b), 22(2), 39(1)(f), (4), 43, 45(2)(c),
  (6), 84(3), (4), 92(1), 93(1)(b), 105(11), (14)(b)), the fact is asked. The Act's own numbers are encoded: 28 days
  (ss 21(3), (4), 78(1), 105(5)), 90 days (ss 76, 78(2)), 21 days (s 105(6)), the specified amount ($7,500; $10,000 on and
  after 1 January 2009, s 93(1)) and the penalties of ss 95-99 and 103(3).
- **Borrowed terms asked as facts:** "legal practitioner", "judicial review proceedings" (defined in s 19(1), but whether
  they were started is a fact), "vocational regulatory body" (turns on regulations), "monetary order" (s 3, asked as a
  fact about the order), "protected matter" (Freedom of Information Act 1992 Schedule 1, s 159 certificates).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch copy, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `sat-dates.l4` | 0 | 0 | 0 | 0 |
| `sat-rules.l4` | 0 | 0 | 0 | 0 |
| `sat-seat.l4` | 0 | 0 | 0 | 0 |
| `sat-cases.l4` | 0 | 0 | 195 | 195 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; each
28-day period on its last day and the day after (30 / 31 March 2026, the 28th day being Sunday 29 March; 7 / 8 April 2026
from a s 20 notice; 20 / 21 March 2026 for leave; 30 April / 1 May 2026 from written reasons, and an application within
28 days of the decision after reasons were asked for); a period ending on 29 February 2028; the 21 days for instituting
(1 / 2 July 2026); 90 days across February (1 December 2025 to Sunday 1 March 2026, so Monday 2 March; 30 November 2025 to
Saturday 28 February 2026, so Monday 2 March; 1 December 2026 to 1 March 2027); a statement due on Saturday 17 January
2026, so Monday 19 January; the s 21(4) statement on the last day, late, and after the application; a court extension after the time passed
(15 / 16 May 2026); the specified amount at $10,000 / $10,001 on 1 January 2009 and $7,500 / $7,501 / $10,000 on
31 December 2008; the regulative rule on day 28 and day 29.

## Seat

**The applicant, and the individual party** (`sat-seat.l4`): the individual who brings a matter to the Tribunal -- most
often a person asking for review of a decision made about them (a licence, a registration, a benefit, a planning or
guardianship decision) or bringing a claim an enabling Act sends to the Tribunal -- and the individual who is a party to a
Tribunal proceeding. "Is this a review?", "Must I be told of the decision, and can I get reasons, by when?", "Does my
review stop the decision?", "Who may represent me?", "Must I serve my application?", "What can the Tribunal do if I miss
the conference?", "Can I start again?", "Will I pay costs?", "Can I get more time?", "Is my case minor?", "Is not
complying an offence?", "Can I appeal, to which court, by when?". No seat for the Tribunal, the executive officer, the
President, the decision-maker or the courts: their satisfaction, belief, leave, orders and extensions are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, except that the Rules and Regulations are not
  deposited; what they decide is asked (see Edition). The Interpretation Act 1984 (WA) s 61(1)(e) is read for its rule
  that a time limit ending on an excluded day runs to the next day that is not one (deposited at
  `subjects/au/wa/interpretation-act-1984/registers/source-bundle/mrdoc_49111.txt`; fork F12).
- **The actors the text names.** Followed: the applicant, the parties, the decision-maker, the executive officer, the
  Tribunal, a judicial member, the President, the Supreme Court and the Court of Appeal.
- **Judgments answered conditionally.** Followed: "satisfied" (s 84(5)), "believes" (s 48), "considers" (ss 50, 105(12)),
  "reasonable excuse", "frivolous or vexatious", "genuinely attempted", "prejudice ... that cannot be remedied" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "review jurisdiction" and "original jurisdiction"
  (ss 15, 17), "minor proceeding" and "specified amount" (s 93(1)), "relevant hearing" (s 84(1), in the description),
  "relevant Act" (s 105(14), with Schedule 1 listed in the description) are worked out or asked with their definition.
- **One case.** One proceeding, of one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 13-15, 17 (jurisdiction), 19 (Tribunal review and judicial review), 20, 21, 22, 23(2) (notice and reasons),
25, 26, 29(5), 82(1) (effect of the review and of the decision), 39 (with 93(3)), 41 (representation, interpreters),
42(3), (4), 44(3), (5), (6), 45(1), (2) (commencing, rejection, copies), 48, 49, 53, 55 (disadvantaging conduct, starting
again, missed conferences, conference evidence), 64(3), 66(5), 68 (expert costs, witness fees, self-incrimination), 74,
76, 78, 84, 85, 86 (decisions, reasons, absent parties, enforcement), 87(1), (3), 88 (costs), 92 (more time), 93 (minor
proceedings and elections), 95-99, 103(3) (offences and penalties), 105, 106 (appeals); s 44(5) and s 93(5) through the
appeal question and the s 84 question. ss 20(4), (5), 22(2), 23(1), 25(2)-(6), 29(3), 42(2), 54, 79, 81, 87(3), 105(12) appear in descriptions.

**Regulative rule:** one, used for five steps. Each time limit the Act fixes is modelled as a duty: `PARTY` the person (or
the decision-maker) `MUST` take the step `WITHIN` the days allowed, `LEST BREACH ... BECAUSE` the time has passed. It runs
by EVALTRACE inside the questions "Can I still ask for reasons on this day" (s 21(3)), "Can I apply for an order for
reasons" (the decision-maker's s 21(4) duty, s 22), "Can I still ask for the Tribunal's written reasons on this day"
(s 78(1)), "Is my leave application in time" (s 105(5)) and "Is my appeal instituted in time" (s 105(6)). Each takes only
plain facts.

**Out, and why:**
- ss 1-7A, Part 2 (ss 7-12), Part 6 (ss 107-147), Part 7 (ss 148-151), ss 152-155, 157, 158, 161, 162, 168-173, Schedule 2:
  machinery -- commencement, constitution of the Tribunal, members, staff, rules committee, regulation-making.
- s 24: the decision-maker is to give the Tribunal its statement of reasons and the relevant documents "in accordance
  with the rules" (not deposited); a duty owed to the Tribunal, with no step, time limit or right for the person.
- ss 16, 18, 27, 28, 29(1)-(4), (6)-(9), 30, 31: how the Tribunal conducts a review (de novo, correct and preferable
  decision, government policy); they bind the Tribunal and give the person no step, time limit or right a fact can test.
- ss 32-38, 40, 46, 47, 50-52, 54, 56-63, 65, 66(1)-(4), (6), 67, 69-73, 75, 77, 79-81, 83, 89-91: the Tribunal's powers and
  procedure, exercised at its discretion; no question the person can answer from facts beyond "the Tribunal may".
- s 94 (documents to the Supreme Court), ss 100-102, 103(1), (2), 104 (contempt and arrest warrants), s 156, ss 159, 160
  (protected matter), ss 163-166 (immunities), s 167 (transfer of jurisdiction from former adjudicators, transitional).
- The enabling Acts: each sets its own time to apply for review and its own parties; they belong to their own encodings.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within the period of N days after the day on which" (ss 21(3), (4), 76, 78, 105(5), (6)) -- `the date ... days
  after` and the regulative rule -- the day of the event excluded, the last day N days after it -- the event day counted.
- **F2** s 49 when the earlier dismissal was not under ss 46-48 or not the same kind and matter -- `s 49 -- I may commence
  again` -- `NOTHING` (limited by its own wording) -- `JUST TRUE`.
- **F3** "unless" met (ss 20(2), 21(2), 41, 87(1)) -- the s 20, s 21, s 41 functions answer `JUST FALSE` (the duty or right
  is switched off); s 87(1) answers `NOTHING` (the order or enabling Act decides what is borne) -- `NOTHING` throughout, or
  `JUST FALSE` for s 87(1).
- **F4** s 21(3)(a) "or" (b), and s 105(5)(a) "or" (b) -- `s 21(3) -- the time limit to request reasons`, `s 105(5), (7)
  -- the time limit for leave` -- either period suffices, so the later last day, counted from the decision; with s 20(1)
  applying and no notice given, or s 78 reasons asked for and not yet given, no limit runs yet -- (b) displacing (a)
  entirely, or (a) running anyway.
- **F5** s 21(4) "as soon as practicable, and in any case within ... 28 days" -- the regulative rule -- only the 28 days
  are encoded -- a breach once "as soon as practicable" has passed, which is a judgment.
- **F6** s 22(1) where the statement came after the 28 days but before the application -- `s 22(1) -- ...` -- the failure
  "contrary to section 21(4)" happened, so `JUST TRUE` -- `JUST FALSE` (nothing left to order).
- **F7** s 68(2) "other than proceedings for perjury or [a false-answer offence]" -- `s 68(2) -- ...` -- `NOTHING` (s 68
  leaves those proceedings to the general law of evidence) -- `JUST TRUE`.
- **F8** s 88(3)(b) "section 87(4) applies to the party" -- `s 88 -- ...` -- read as: the party failed the genuine-attempt
  test of s 87(4)(a) (or, as decision-maker, (b)) -- s 87(4) applying to every party in the review jurisdiction, which
  would empty s 88(3).
- **F9** s 93(1) "specified amount means $7 500 and, on and after 1 January 2009, means $10 000" -- `s 93(1) -- the
  specified amount` -- as at the day the proceeding commenced -- as at the election, or the day the question is decided.
- **F10** s 45(1) for a person outside (a)-(c) -- `s 45(1), (2) -- ...` -- `NOTHING` (an open list; silent) --
  `JUST FALSE`.
- **F11** s 105(5)(b) "the party then requests [written reasons] under section 78" -- the leave time limit -- any request
  under s 78 moves the start to the day the reasons are given, and until then no limit runs -- only a request within the
  s 78(1) 28 days counts (asked in the description, not tested).
- **F12** Interpretation Act 1984 (WA) s 61(1)(e), (2): a time limit that "expires or falls upon an excluded day" runs to
  the next day that is not one -- `the date ... days after` (sat-dates.l4), so every period of ss 21(3), (4), 76, 78,
  105(5), (6) -- a last day on a Saturday or Sunday moves to the Monday; public service, bank and public holidays are not
  computed (no holiday list is deposited), so a last day on one, or a Monday after a weekend that is one, reads a day
  early -- the holidays asked as a fact, or s 61(1)(e) read as not applying to the decision-maker's and the Tribunal's
  own deadlines (ss 21(4), 76, 78(2)), which this encoding moves too.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "cannot" (ss 19(3), 26, 39(3), 42(4), 49, 88(3), 92(4), 93(3)), "is not admissible ... unless" (ss 55, 68(2)),
"does not apply ... unless" and "only applies ... on" (ss 64(3), 95(2)-(4)), "does not affect ... unless" (ss 25(1), 106(2)),
"has to be made within" (s 84(3)), "is not subject to appeal or review" (s 93(5), for s 105 and s 84), "means" (s 93(1)), the periods of ss 21(3), 78(1), 105(5), (6), and the "if" or "when"
conditions of ss 20, 22(1), 44(3), 45(1), 74, 78(1), 84(2), (5) give `JUST FALSE`. `NOTHING` is answered where the enabling
Act, the rules or a costs order decide (ss 25, 87(1), 92: *points outside the text*); where s 26, s 49, s 66(5), s 84 or
s 105 speak only of their own case (*limited by its own wording*); for s 45(1) outside its open list and s 68(2) in the
excepted proceedings (*silent*, *"(other than X)"*); and for a step asked about before its period begins. Three "unless"
sites are fork F3; s 68(2) is F7.

## What the Act turns out to say

1. **s 21(3) joins two periods with "or".** (a) runs from the decision, (b) "if section 20(1) applies" from the notice.
   Read as giving whichever ends later (F4); where s 20(1) applies but no notice was ever given, (b) has not begun, so the
   request can still be made. Asserted (29 March / 7 April 2026; no notice).
2. **s 22(1) turns on a failure "contrary to section 21(4)".** A statement given on day 29 or later is still a failure;
   whether an order can then be sought for a statement already in hand is not said (F6). Asserted.
3. **s 88(3)(b) cross-refers to s 87(4)**, which is a list of matters the Tribunal must "have regard to" for every costs
   order in the review jurisdiction; read literally it "applies" to every party and s 88(3)'s limit would never bite. Read
   as the party's failure of the genuine-attempt test (F8). Asserted.
4. **s 93(3)(b) repeats s 39(1).** After a no legal representation election a party "cannot be represented by any other
   person except as authorised by section 39(1)(a) to (f)", which s 39(1) already says of non-lawyers; only (a) changes the
   law. Asserted (a lawyer and an interstate practitioner barred; an experienced friend allowed).
5. **s 93(1)'s specified amount has no reference day** for the change on 1 January 2009 (F9). Encoded as at commencement of
   the proceeding. Asserted ($10,000 on 31 December 2008 is not minor; on 1 January 2009 it is).
6. **s 19(5) qualifies (3)(c) only.** Judicial review started at the same time as the Tribunal review stays a bar under
   (3)(a) even if later dismissed for a procedural defect. Asserted.
7. **s 105(5)(b) does not say the s 78 request must itself be in time** (F11). A late request would postpone the leave
   period indefinitely on a literal reading; the description asks about a request "under section 78".
8. **The Act's own time limits are few.** The time to apply to the Tribunal is set by the enabling Act or the rules (s 44(1)(b)),
   and the rules may extend almost any time limit (s 92). This encoding therefore asks "am I within the rules' time" (s 84)
   and "do the rules allow more time" (s 92) rather than computing them.
9. **The penalties in ss 95-99 and 103(3) are maxima for an individual;** no separate figure is given for a body corporate.

## Before this is worth relying on

- Check the text against the authorised PDF and the current compilation (retrieved 7 September 2026); watch the
  uncommenced Evidence Act 2025 s 492(1).
- Deposit the State Administrative Tribunal Rules 2004 and Regulations 2004, then encode the time limits for applying for
  review and under s 84, the s 22(2) notice, the fees and s 105(11)'s prescribed proceedings.
- The public, bank and public service holidays for the Interpretation Act 1984 (WA) s 61(1)(e) (F12).
- A lawyer's view on findings 1-3 and 7 and forks F3, F4, F6, F8, F11; an independent test pass and a human gate.
