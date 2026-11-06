# Occupational Health and Safety Act 2004 (Vic) -- baseline encoding, the person at work

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). A seat-neutral core (`ohs-core.l4`), date helpers (`ohs-dates.l4`,
prelude only: no daydate import, no `YMD`), and a seat layer (`ohs-seat.l4`) that builds the core's inputs from plain
answers and restates no rule. Two regulative rules (s 38(3), s 131(2)/(2A)) run by `EVALTRACE` inside exported questions
that take only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Occupational Health and Safety Act 2004, Act No. 107/2004, Version No. 045, incorporating amendments as at
  6 August 2025 (the current version on 2026-11-06), deposited at
  `../../registers/source-bundle/occupational-health-and-safety-act-2004.txt` (committed text sha256
  13daf6cabb3ed8a96cd548f002d14f5c735514da680151f5d887bd2b809887a3), a plain-text conversion of the Word file the owner
  saved by hand on 6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not checked against the
  authorised PDF, which was not saved.
- **Formulas sidecar:** the one embedded equation (04-107a045-F1, s 151A, contributions by non-WorkCover employers) is out
  of scope; nothing here reads it.
- **Numbers the Act uses:** penalties are stated in penalty units; the value of a penalty unit (Monetary Units Act 2004)
  is not deposited, so every answer is in penalty units. The regulations (prescribed incidents, labour hire exclusions,
  infringement offences, the issue resolution procedure) are not deposited and are asked as facts.
- **Commencement of Part 5A:** 1 July 2020, read from the endnotes (No. 50/2019 ss 3-8 and No. 16/2020 ss 21, 22, both
  on 1.7.20).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ohs-dates.l4` | 0 | 0 | 4 | 4 |
| `ohs-core.l4` | 0 | 0 | 0 | 0 |
| `ohs-seat.l4` | 0 | 0 | 0 | 0 |
| `ohs-cases-duties.l4` | 0 | 0 | 140 | 140 |
| `ohs-cases-claims.l4` | 0 | 0 | 74 | 74 |

Four `#TRACE`s, each with an `-- expect:` line, each giving what it expects (s 38(3): fulfilled at hour 47, breached
at 49; s 131(2): fulfilled on day 89, breached at 90).

Every expected value was worked by hand from the text, with the edges: the 48th and 49th hour (s 38(3)); the last day of
the 5 years (s 38(4)); 30 June and 1 July 2020 (s 187); the last day of each s 132(1) limb and the day after; the
day 6 months end and the day after (s 131(1)), 31 August + 6 months and 30 November + 3 months (short months), 29 February
+ 1 year (s 78E(1)); day 89 and day 90 of the s 131(2) period; the s 139(2) cap at one fifth of 60 penalty units.

## Seat

**The person at work.** An employee (including a labour hire worker, s 5A, and an independent contractor or a
contractor's employee, s 21(3)), a visitor or member of the public exposed to a business's risks (s 23), and, after a death
at work, the family member asking about it. Every exported question is one that person would ask ("Does my employer owe
me the s 21 duty?", "Has it breached it?", "Have I breached my own duties?", "Must I be consulted?", "Must WorkSafe be
notified?", "Can I see the incident record?", "Am I still paid?", "Has my employer discriminated against me?", "By when must
I start my claim?", "May I ask WorkSafe to prosecute?", "Was it workplace manslaughter?", "What is the most the business
can be fined?"). Provisions addressed to the employer, the Authority or the court are encoded as what they mean for that
person: a duty owed to them, a record they may see, a reply due to them by a date, a penalty the duty-holder faces.

No second seat. The duty-holders (employer, self-employed person, officer) are the obvious candidates under the
guide's "more than one seat" ruling; their seat is left for a later layer over the same core (`ohs-seat-employer.l4`).
Officials (WorkSafe, inspectors, the DPP, the court) get none.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No instrument setting the Act's numbers is
  deposited (the regulations and the penalty unit value): the regulations' heads are asked as facts and penalties are
  answered in penalty units.
- **The actors the text names.** Followed: the employer, the employee, the self-employed person, the officer, the
  health and safety representative, the Authority (WorkSafe), the inspector, the Industrial Division of the
  Magistrates' Court, the DPP.
- **Judgments answered conditionally.** Followed: "reasonably practicable" (s 20, as three inputs: eliminated; elimination
  reasonably practicable; reduced so far as reasonably practicable), "reasonable care", "recklessly", "negligent"
  (s 39E's two limbs), "dominant reason", "substantial reason", "reasonable time", the inspector's determinations, the
  court's satisfaction about fresh evidence and causation are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: employee and labour hire (ss 5, 5A), the reach of
  s 21 (s 21(3)), the s 20 standard, the Part 5 incident (s 37), applicable duty (s 39B), negligent (s 39E), owes an
  applicable duty (s 39F, with membership of the protected class asked), applicable entity (s 39G(3)), workplace
  manslaughter offence (s 132(4)) are worked out. "Officer" (Corporations Act s 9) and "volunteer" are asked.
- **One case.** One person, one employer or duty-holder, one incident or one course of conduct.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**
- **Who is who** -- ss 5(1) (employee, employer), 5A(1)-(3).
- **Part 3 general duties** -- s 20; s 21(1)-(3); s 23(1); s 25(1)-(3); s 32; s 34; with s 152 (compliance with
  regulations or a compliance code). ss 22, 24, 26-31: penalties and indictability only.
- **Part 4 consultation** -- s 35(1), (4) (penalty s 35(6)); s 35A penalty only.
- **Part 5 incidents** -- s 37(1)-(3); s 38(1)-(6); s 39(1)-(3).
- **Part 5A workplace manslaughter** -- ss 39B, 39C, 39E, 39F, 39G(1)-(4); s 187 (s 39D as a gloss).
- **Unsafe work** -- s 74(1); s 75(1), (4).
- **Discrimination** -- ss 76(1)-(4), 77, 78(a)-(b) (via s 78E(5)-(6)), 78A, 78B, 78D(1)-(2), (5), 78E(1)-(3), (5),
  (6).
- **Prosecutions and penalties** -- s 131(1)-(3); s 132(1)-(4); s 139(1)-(2); ss 144(1), (5), 145(1)-(3), (5); s 148A;
  s 148B penalty; s 153 penalty.

**Regulative rules:** two. s 38(3) (the duty-holder MUST give the written record WITHIN 48 hours of the duty to notify,
LEST breach) and s 131(2)/(2A) (the Authority MUST report WITHIN the days to the same day 3 months on, LEST breach). Each
is run by `EVALTRACE` inside an exported question that takes hours or dates. The other time limits (s 78E(1), s 131(1),
(3), s 132, s 38(4)) are periods for the person's own step or for a prosecution, and are encoded as dates and yes/no
answers.

**Out, and why:**
- Part 1 other than ss 5, 5A (purposes, objects, principles, commencement, Crown): machinery or not operative.
- Part 2 (the Authority, information, guidelines, s 16 undertakings, advice, the Advisory Committee): machinery; a s 16
  undertaking appears only as a date in s 132(1)(c).
- Contravention questions for ss 22, 24, 26-31: duties the person at work meets less often, judged in the same way as
  s 21; their penalties are in. s 33 (charging several contraventions together): procedure.
- s 35(2), (3), (5) (how to consult) and s 35A duties between duty-holders: the employer's seat.
- Part 6 (licences, qualifications, permits): regulations not deposited.
- Part 7 Divisions 1-7 (designated work groups, election and powers of health and safety representatives, provisional
  improvement notices, training, committees) and s 73 (the agreed or prescribed procedure, in regulations not deposited):
  a further layer; the representative's own seat.
- Part 8 (entry permits), Part 9 (inspectors' powers and notices), Part 9A: official powers; the notices appear only as
  facts (s 75(4)).
- Part 10 (review of decisions): the reviewable decisions table belongs with Part 7 and Part 9.
- ss 133-138 (evidence, adverse publicity, improvement projects, undertakings), s 143, ss 146-148: sentencing and
  procedure.
- Part 12 except s 152; Part 13 (ss 151A-151F contributions, with the sidecar formula; ss 154-158); Parts 14 and 15
  except s 187 (s 188 changes only s 39G's wording from 1 July 2020, the same day).
- The value of a penalty unit, the regulations, the Sentencing Act 1991, the Criminal Procedure Act 2009 (summary
  limitation periods), the Corporations Act's "officer": not deposited.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 21(3)(b) -- `the s 21 duty is owed (s 21(3))` -- a contractor on a matter outside the employer's control:
  `NOTHING` (a scope limit with no "only") -- `JUST FALSE`.
- **F2** s 20 with s 21(1) -- `the employer contravened s 21(1)` -- s 20's "duty ... to ensure, so far as is reasonably
  practicable" applied to s 21(1)'s "provide and maintain ... so far as is reasonably practicable" -- s 20 governs only
  duties worded "ensure".
- **F3** s 38(4) "for at least 5 years" -- `the record must be made available (s 38(4))` -- 60 months from the day the
  record was given, `JUST FALSE` after (a period the text fixes) -- `NOTHING` after ("at least" is a floor), or counted
  from the incident.
- **F4** s 131(1) "within 6 months of that occurrence" -- `the first day a s 131 request may be made` -- the day after the
  same day 6 months on -- that day itself.
- **F5** s 35(1) -- `the employer must consult the employee (s 35(1))` -- a matter outside (a)-(f) and not prescribed
  under (g): `NOTHING` -- `JUST FALSE` (the list closed by (g)'s hand-off, as s 37 is read under the delegated-definition
  ruling (a)).
- **F6** s 37 -- `Part 5 applies to the incident (s 37)` -- none of the heads: `FALSE` (the heads close by handing the rest
  to the regulations) -- `NOTHING`.
- **F7** ss 21-153 penalties -- `the maximum fine in penalty units`, `the maximum imprisonment in years` -- `JUST 0` where
  the section states only the other kind of penalty -- `NOTHING` (the Sentencing Act 1991, not deposited, may allow a
  fine in place of imprisonment).
- **F8** s 187(2) -- `Part 5A applies to the conduct (s 187)` -- decided by the day the conduct began -- by the day of the
  death.
- **F9** s 74(1) -- `work may be directed to cease (s 74)` -- anyone other than the employer or the representative: `NOTHING`
  (a grant limited in its own words) -- `JUST FALSE`.
- **F10** s 75(1) and s 78D(1) -- `an inspector may be requested (s 75(1))`, `Can the court make a s 78D order for me` -- a
  person outside the class: `NOTHING` -- `JUST FALSE`.
- **F11** s 132 -- `Can it still be prosecuted`, `What is the last day to prosecute` -- a summary offence: `NOTHING`
  (s 132 speaks only of indictable offences) -- the Criminal Procedure Act 2009's period.
- **F12** s 23(1) -- `the employer contravened s 23(1)` -- an employee of the employer, or a risk not from the undertaking:
  `NOTHING` -- `JUST FALSE`.
- **F13** s 39F -- `owes an applicable duty to the deceased (s 39F)` -- membership of the class the duty names or protects
  is one input -- the express and implicit routes asked separately.
- **F14** s 139 -- `the most an infringement notice may specify (s 139(2))` -- `NOTHING` for an indictable or unprescribed
  offence -- a separate `JUST FALSE` "no infringement notice".
- **F15** s 38(3) -- `Was the incident record given in time` -- the 48 hours run from when the business became aware (when
  s 38(1) required it to notify) -- from when it notified.
- **F16** s 131(2)/(2A) -- `s 131(2) -- the Authority must report ...` -- the same day 3 months after receipt is the last
  day -- months of 30 days.
- **F17** s 39G(2) with s 39B(b) -- `Was it workplace manslaughter by an officer` -- the entity's s 32 duty is an
  applicable duty (an entity is not "an employee, but not an officer") -- the officer's own position decides.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING` answers of the kinds the rulings describe. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "if" conditions (ss 74(1), 75(1), 75(4), 76(2)-(3) "only if", 144(1), 145(2)), "while" (s 25), "means"
(ss 5, 39B, 39C, 39E), flat prohibitions (ss 39G, 148A "void", 78E(5)-(6) "cannot"), "Nothing in this Part is to be
construed as conferring a right of action" (s 34), "However ... not required" (s 38(2)) and the periods the text fixes
(ss 38(3), 38(4), 78E(1), 131(1)-(3), 132(1), 187) give `JUST FALSE`; a s 78E(3) defence not proved gives `JUST FALSE`
for that defence; scope limits with no "only" (s 21(3)(b), s 35(1) "directly affected"), grants limited in their own words
(ss 74, 75(1), 78D(1)), silence (s 39 with no duty to notify, s 132 for summary offences) and figures outside the
deposit give `NOTHING`.

## What the Act turns out to say

1. **The s 139(2) "one fifth" never binds here.** The infringement penalty is the lesser of 10 penalty units and one fifth
   of the court maximum, but every summary offence in scope has a maximum of at least 60 penalty units (s 22(2), s 73(2)
   for a natural person), one fifth of which is 12. So 10 penalty units is the cap for all of them. Asserted.
2. **Two routes to an officer for a workplace death, with very different penalties.** An officer of a body corporate whose
   negligence causes a death in breach of the company's duty commits s 39G(2) (25 years' imprisonment); if instead the
   company is charged under s 39G(1) and the officer under s 144(1)(a), the officer's maximum is a fine of 10 000 penalty
   units. Asserted (both figures).
3. **Workplace manslaughter by a natural person carries no fine in the Act.** s 39G(1) gives "Imprisonment for 25 years
   for a natural person; 100 000 penalty units for a body corporate" (F7).
4. **s 132(4)(b) names only s 144.** "Workplace manslaughter offence" covers an officer's s 144(1) offence for a body
   corporate's s 39G(1) contravention, but says nothing of s 145; s 145(1) makes a partnership's s 39G(1) offence the
   officer's own s 39G(1) offence, so it falls under (a) anyway. Encoded so; a lawyer should confirm.
5. **s 39B(b) treats s 32 as a duty.** s 32 is drafted as an offence ("A person who ... is guilty of an indictable
   offence"), not as a duty, yet its heading calls it a "Duty" and s 39B(b) speaks of "a duty imposed by section 32". The
   encoding follows s 39B and treats s 32 as an applicable duty except for an employee who is not an officer.
6. **Offences with no indictability statement.** ss 22, 35, 35A and 73(2) do not say they are indictable, unlike every
   other Part 3, 5 and 5A offence (s 22 has the same 240/1200 penalty as s 38, which is indictable). They are read as
   summary offences: s 132's limitation periods do not cover them and an infringement notice may be prescribed for them.
   Asserted.
7. **s 38(4) has no start date.** The record must be kept "for at least 5 years", without saying from when (F3).
8. **Two discrimination tests.** The criminal s 76 needs the health and safety reason to be the *dominant* reason
   (s 76(3)); the civil s 78A needs only a *substantial* reason (s 78B(2)), and has a defence (s 78E(3)) that s 76 lacks.
   The same facts can fail s 76 and succeed under s 78A. Asserted.
9. **Part 3 gives no right to sue (s 34).** A worker's compensation claim cannot rest on a breach of the general duties
   as such; it lies under the workers' compensation scheme or the common law. Asserted.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The value of a penalty unit (Monetary Units Act 2004 and the Treasurer's notice) to turn penalty units into dollars.
- The Occupational Health and Safety Regulations 2017 (prescribed incidents and exclusions, s 5A exclusions, the issue
  resolution procedure, infringement offences) and the compliance codes.
- The employer's seat over the same core; Part 7 Divisions 1-7 (health and safety representatives and provisional
  improvement notices) for the representative; contravention questions for ss 22, 24, 26-31.
- A lawyer's view on findings 2, 4 and 5 and on F2, F3 and F8; an independent test pass and a human gate.
