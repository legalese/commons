# Public Interest Disclosures Act 2012 (Vic) -- baseline encoding, the person who makes a disclosure

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Four files and the cases:

- `pid-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`), in the shape of the
  Health Complaints Act 2016 encoding's;
- `pid-rules.l4` -- the law the questions share: the s 4 meaning of improper conduct, the enumerations of s 9, the
  destinations of ss 13 to 17 and the permitted persons of Schedule 2, the s 3 and s 43 meaning of detrimental action in
  reprisal, the receiving entity's s 24 duty to advise as one regulative rule with its trace helper, the s 54
  circumstances and the s 52(3) and s 53(2) exceptions, and the table of offences and penalties;
- `pid-seat.l4` -- 27 exported questions of the person who makes the disclosure;
- `pid-cases.l4` -- the cases.

## Edition

- **Act:** Public Interest Disclosures Act 2012, Act No. 85/2012, Version No. 032, incorporating amendments as at 2 October
  2026 (the register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/public-interest-disclosures-act-2012.txt` (sha256 38d72d67...4eee88 as committed), a
  plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act fixes its own periods (28 days, 30 days, 6 and 12 months) and its penalties in
  penalty units. Not deposited, so inputs or left in units: the Public Interest Disclosures Regulations (prescribed public
  bodies and officers in s 6, prescribed public officers in ss 13(5) and 15(3), prescribed entities in s 13(4), prescribed
  services in s 54(2)(l), the prescribed matters of s 28(3)); the value of a penalty unit (Monetary Units Act 2004).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pid-dates.l4` | 0 | 0 | 0 | 0 |
| `pid-rules.l4` | 0 | 0 | 0 | 0 |
| `pid-seat.l4` | 0 | 0 | 0 | 0 |
| `pid-cases.l4` | 0 | 0 | 257 | 257 |

Every expected value was worked by hand from the text, with the edges: the 28 days of ss 19(2), 21(2) and 24(4) on the
28th and 29th day, across February in a leap year (10 February 2028 to 9 March 2028); the s 24 duty done on the last day,
done the day after, still open on the last day and late the day after; the 6 months of s 38A(3)(a) on the last day and the
next; the 30 days of s 38A(3)(b) and (4)(c) with a response on the 30th and the 31st day; the 12 months of s 38A(4)(a)
with completion inside and outside; the 6 months after a response of s 38A(4)(c)(ii); 6 months from 31 August 2027 (29
February 2028); every s 14 and s 17 subject against its destinations and the wrong ones; each insider route of ss 15,
16(2), 16A(3) and its exclusions; each Schedule 2 row; each exception of ss 52(3), 53(2) and a s 54 circumstance; each
penalty for a person and a body corporate.

## Seat

**The person who makes, or is thinking of making, a public interest disclosure** (`pid-seat.l4`): the whistleblower,
and with them the person who suffers detrimental action for a disclosure (who may be a witness who cooperated with an
investigation, s 43(1)(a)(ii)). "Is it improper conduct?", "Is my disclosure a public interest disclosure, and by when
must I say if I don't want it treated as one?", "Can I make it to this entity, to this person, in this way?", "Is it a
misdirected disclosure?", "By when must I be told, and have I been told in time?", "Can the IBAC send it elsewhere
without my consent?", "Does Part 6 protect me, can I go external, am I protected from this liability?", "Is this
reprisal, may my manager do it, is it an offence, what can a court order, can I sue the person and the public body, can I
be made to pay costs, can I go to the Supreme Court, can I be transferred?", "Can my disclosure or my identity be passed
on?", and the penalties.

No second seat. The Act puts duties on the receiving entities and the integrity bodies (officials: no seat) and on the
person who takes reprisal action, whose duty (s 45) is a prohibition the first seat's questions already answer. An
employer or manager seat could be added (s 44, s 48(2), s 51).

No seat for the IBAC, Integrity Oversight Victoria, the Integrity and Oversight Committee, the Ombudsman, a receiving
entity, a court or a Head: their considerations, beliefs and determinations are asked as facts; their duties to the
person (ss 24, 26(6)) are encoded as what the person must be given or asked.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own periods; the regulations
  and the penalty-unit value it relies on are not deposited and are inputs or left in units.
- **The actors the text names.** Followed: the person who makes the disclosure, the receiving entity, the IBAC,
  Integrity Oversight Victoria, the Integrity and Oversight Committee, the Presiding Officers, the other entities of
  ss 13 to 17, the investigating entity, the manager, the public body, the Heads of s 51, the court.
- **Judgments answered conditionally.** Followed: "shows or tends to show", "reasonably believes", "considers",
  "honestly believed", "trivial", "substantial", "reasonable precautions", "reasonable grounds to suspect", "vexatious",
  "conduct the litigation reasonably" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "improper conduct" (s 4), "public interest
  disclosure" (s 9 with ss 19, 20), "misdirected disclosure" (s 18), "external disclosure" (s 38A), "detrimental action"
  and "in reprisal" (ss 3, 43), "assessable disclosure" (s 3) are worked out; "corrupt conduct" (IBAC Act 2011), "public
  officer" and "public body" (s 6, via the IBAC Act), "public service body" and "public entity" (Public Administration Act
  2004), "Councillor" (Local Government Act 2020), "relevant Act" heads are asked.
- **One case.** One disclosure, and one action taken or threatened against one person for it.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).
- **Departure: chained answers as inputs (fork F12).** Five questions (misdirected disclosure, Part 6, the immunities,
  reprisal, suing the public body) take the answer of an earlier question as a yes/no input whose description names that
  question, instead of repeating its 6 to 19 facts. The form should ask the earlier question first.

## Scope

The focus: public sector whistleblower disclosures and protection against detrimental action. Parts 2 and 6 are encoded
whole, with s 4, the claims machinery of Part 7 (confidentiality), the discloser's side of Part 3 (ss 21(2), 24, 26(5),
(6)) and the offences.

**In:** s 3 (assessable disclosure, detrimental action, Presiding Officer), 4, 9, 12, 12A, 13, 14, 15, 16, 16A, 17, 18,
19, 20, 21(2) (the date), 24, 26(5), (6), 38, 38A, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 72 and
73 (penalties, and s 72 as the bar of ss 39(2), 40(2), 41(2), 43(2)), Schedule 2.

**Regulative rule:** one. s 24(2), (3), (4): the receiving entity MUST advise the person in writing WITHIN 28 days of the
disclosure, LEST breach; run by EVALTRACE inside `Has the entity told me in time`, which takes only dates and yes/no
facts, with the s 24(1) scope, s 24(5) and s 12A(2) worked out before the duty arises.

**Out, and why:**
- ss 1, 2, 7, 8 (purposes, commencement, other protections, Crown): machinery; s 7 is why a case outside Part 6 answers
  NOTHING, not no.
- ss 5, 6: the meanings of "police complaint disclosure", "public body", "public officer" lean on the Victoria Police Act
  2013 and the IBAC Act 2011; asked as facts in the `@desc`s.
- ss 10, 11 (a disclosure may be made without naming anyone, or as a complaint under another Act): no fact test.
- ss 21(1), (4), 22, 23: which integrity body an entity notifies; only the date reaches the person (s 21(2)).
- ss 26(1) to (4), (7), 26A, 27 to 31B (assessment and determination by the integrity bodies); ss 28, 29 advice "within a
  reasonable time" could be added as "what must I be told". Parts 4 and 4A (investigation); s 33E(1)(b) (the Committee may
  decline where the disclosure came more than 12 months after the person became aware) could be added.
- Part 5 (related disclosures); s 37's 28-day advice could be added beside s 24.
- Parts 8, 9, 10 (functions, guidelines, procedures, reports), ss 74 (repealed), 75 to 79: machinery (s 76 protects
  officers of the receiving entity, not the discloser).
- Part 12 and Schedule 1: transitional (disclosures under the Whistleblowers Protection Act 2001, s 81's offence).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 6 months after", "within 12 months after" (s 38A) -- `the date` n `months after` -- the same day of the
  month, or that month's last day where it is shorter (31 August 2027 plus 6 months is 29 February 2028), the last day
  inside the period -- 1 March 2028 (rolling over).
- **F2** s 19(2) "must be given ... no later than 28 days after the disclosure is made" -- `Is my disclosure a public
  interest disclosure` -- a statement given later does not take the disclosure out (it stays a public interest
  disclosure) -- (2) is only a duty and a late statement still works under (1).
- **F3** s 13(1) "Unless required to be made to another entity under section 14 or 17, a public interest disclosure must be
  made to a person or entity in accordance with this section" -- `Division 2 -- the entity may receive it` -- ss 15, 16,
  16A add routes beside s 13 -- s 13 alone governs where s 14 or 17 does not (finding 1).
- **F4** s 16(1) (a disclosure about "a member ... of a Council" may go to that Council) against s 14(ea) (one about a
  Councillor "must be made" to the IBAC, the Ombudsman or the Chief Municipal Inspector) -- `s 16 -- Councils` -- s 14
  governs, so a Councillor's own Council is not a destination -- s 16(1) adds the Council (finding 2).
- **F5** s 12(2), (5) and Schedule 2 -- `Could this person receive my disclosure for the entity` -- a person not listed:
  JUST FALSE ("listed in Schedule N", decided case by case) -- NOTHING (the entity's own procedures may name others; only
  the rows for public service bodies, Councils and Gellung Warl say so).
- **F6** s 26(5) "a disclosure which has been notified to the IBAC under section 21 or 22" -- `Can the IBAC send my
  disclosure elsewhere` -- a disclosure made to the IBAC directly: JUST FALSE, since s 26(3)(a) then requires a public
  interest complaint determination where the IBAC considers it shows improper conduct -- NOTHING (the IBAC's other powers
  under its own Act).
- **F7** s 26(6) "Before determining ..., the IBAC must (a) consult ...; and (b) unless the disclosure was made
  anonymously, obtain the consent" -- the same question -- a precondition not met: JUST FALSE (the determination cannot be
  made) -- a duty whose breach does not undo the determination.
- **F8** s 38A(3)(a) "has not been notified ... within 6 months after", (3)(b), (4)(c)(i) "has not received a response
  within 30 days after that request" -- `Can I make an external disclosure` -- met only once the period has run on the day
  of the external disclosure (the last day itself is still inside) -- met as soon as nothing has come so far.
- **F9** s 38A(3)(b), (4)(b) "has requested advice on the progress" -- the same -- the request may be made at any time,
  even before the 6 or 12 months have run -- the request must follow the period.
- **F10** s 38A(4)(c)(ii) "has not been advised that the investigation has been completed within 6 months after that
  response" -- the same -- "within 6 months" qualifies "advised" (no advice of completion in the 6 months) -- it qualifies
  "completed" (finding 8).
- **F11** s 47(7) "costs ... must not be awarded unless the court is satisfied" -- `Can I be ordered to pay costs` -- once
  the "unless" is met: JUST TRUE (the court may) -- NOTHING (the Act says only that the bar lifts).
- **F12** design -- the five chained questions -- a yes/no input naming the earlier question -- the earlier question's
  facts repeated.
- **F13** s 51(4) "An employee may only be transferred under subsection (2) or (3) if" -- `Can I be transferred there` --
  a destination (2) or (3) does not list (a public entity employee to another public entity), and terms less favourable
  overall: JUST FALSE -- NOTHING (other law may allow it) (finding 10).
- **F14** s 24(4) "no later than 28 days after the disclosure is made" -- `Has the entity told me in time` -- advice on the
  28th day after the disclosure day is in time (`WITHIN 28` counted from the disclosure day as 0) -- the disclosure day
  counted as day 1.
- **F15** s 43(1)(a)(i) "has made, or intends to make, the disclosure" -- `Is it detrimental action in reprisal` -- an
  intended disclosure counts if it would be one Part 6 protects (the input says "made or intended") -- Part 6 applies only
  "from the time the disclosure is made" (s 38(3)), so reprisal before it is not reached (finding 12).
- **F16** s 47(1) "liable in damages for any injury, loss or damage" -- `Can I sue for damages for the reprisal` -- no
  loss: NOTHING (exemplary damages under (3) are the court's) -- JUST FALSE.
- **F17** s 9(1)(b) "reasonably believes" and ss 21(1)(b)(ii), 26(3)(a)(ii) "believes on reasonable grounds" -- the s 9
  question -- read as the same test -- two tests.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of ss 3 ("assessable disclosure"), 4 ("improper conduct") and 9 ("a public interest
disclosure is"), the "if" definitions of ss 18 and 38A(2), the flat negatives of ss 4(2), 4(3), 9(3), 19(1), 20(1),
38A(5), 39(2), 40(2), 41(2), 42, 43(2), the "must be made" of ss 12, 13, 14, 17, the "only if" of ss 44(2) and 51(4), the
"must not ... unless" of s 47(7), the "does not apply if" exceptions of ss 52(3), 53(2), the defences of ss 45(2), (3) and
48(2), and the 28-day periods give `JUST FALSE`. `NOTHING` is answered where a grant or prohibition does not reach the case
(ss 38, 43 outside Part 6, 44, 50, 51(1), 51(2) for another employer, 52(1), 53(1) for a disclosure that is not
assessable) (*limited by its own wording*), for an action outside the open list of s 3 "detrimental action includes"
(*open list*), and where the Act is silent (s 47 with no loss; the body corporate penalty of ss 45, 72, 73) (*silent*).

## What the Act turns out to say

1. **s 13(1) reads as if s 13 were the only route.** "Unless required to be made to another entity under section 14 or
   17, a public interest disclosure must be made to a person or entity in accordance with this section." Read alone it
   would exclude the routes of ss 15, 16 and 16A (to one's own public service body, a Council, the Chief Municipal
   Inspector, Gellung Warl), which are expressed as "may be made". Encoded with those routes added (F3). Asserted.
2. **A Councillor and their Council.** s 16(1) lets a disclosure about "a member ... of a Council" go to that Council; s
   14(ea), added in 2024, says one about a Councillor "must be made" to the IBAC, the Ombudsman or the Chief Municipal
   Inspector. A Councillor is a member of a Council. Encoded with s 14 governing (F4), so a disclosure about a Councillor
   made to the Council is at best misdirected. Asserted.
3. **s 73(2) misses the Integrity and Oversight Committee.** It forbids falsely claiming that a matter is the subject of
   a disclosure "that the IBAC or Integrity Oversight Victoria has determined to be a public interest complaint"; the
   Committee also determines public interest complaints (s 31B) and is named beside them in ss 45(3), 52(3)(b), 53(2)(c).
   A false claim about a Committee determination is not an offence under s 73(2). Recorded in the offence's name.
4. **s 76 was not updated for the 2019 and 2024 changes.** It protects a public officer who discloses information "in the
   course of notifying a disclosure to the IBAC under section 21 or 22" or "to the IBAC under section 23"; s 21 now
   notifies Integrity Oversight Victoria or the Committee too, and s 23 any of the three. Out of scope; recorded.
5. **s 52 does not bind the person who made the disclosure.** Its list (s 52(1)) names those to whom it was made, who
   received it in their duties, who were given its content by an integrity body, or who received it in an excepted or
   unlawful disclosure; the discloser is none of these. The Act does not forbid the discloser to talk about their own
   disclosure (other Acts' confidentiality notices may). Encoded as the "binds" input, NOTHING when it does not.
6. **The two confidentiality offences have different exceptions.** Content (s 52(3)) may be passed on by direction or
   authorisation of the investigating entity, or as necessary for lawful action including discipline, but there is no
   consent exception; identity (s 53(2)) may be passed on with the discloser's written consent, but not by direction or
   for lawful action (except through s 54). So the discloser's consent does not free the content, and an investigator's
   direction does not free their identity. Asserted.
7. **The consent protection of s 26(6) is the IBAC's alone.** ss 31(5) and 31B(5) apply ss 27 to 30, not s 26(5) or (6),
   to Integrity Oversight Victoria and the Committee; neither has a power to send a notified disclosure elsewhere, so the
   question is asked of the IBAC only.
8. **The external disclosure timetable.** s 38A(3) needs no notice of action within 6 months and no answer within 30 days
   of a request, but does not say when the request is made (F9); (4)(c)(ii) is ambiguous between "not advised within 6
   months" and "not completed within 6 months" (F10). The earliest external disclosure under (3) is the day after the
   later of the 6 months and the 30 days. A person who disclosed anonymously can never make one (s 38A(2)(a)). Asserted.
9. **No body corporate figure for ss 45, 72, 73.** ss 52 and 53 give 120 penalty units for a natural person and 600 for a
   body corporate; ss 45, 72 and 73 give one figure with imprisonment, though a public body or company can take reprisal
   action. A general rule outside the Act (not deposited) may supply one. Asserted as NOTHING.
10. **A public entity employee cannot be moved to another public entity.** s 51(2) lets a public service body employee go
    to another public service body, "a public entity" or another area; s 51(3) lets a public entity employee go only to
    "a public service body" or another area of the same entity. Asserted (F13).
11. **Defence to the offence, not to the claim.** s 45(3) gives a defence where the disclosure was determined not to be a
    public interest complaint and the person knew it, but the notes to ss 26(3), 31(2), 31B(2) say Part 6 applies "whether
    or not" such a determination was made, and ss 47 to 49 have no such defence: the civil claim survives. Asserted (the
    offence is no, the damages claim yes, on the same facts).
12. **Reprisal before a disclosure is made.** s 43(1)(a)(i) catches action taken because a person "intends to make" a
    disclosure, but s 38(3) applies Part 6 to a disclosure "from the time the disclosure is made". Encoded on the reading
    that an intended disclosure counts if it would be protected (F15).
13. **Conversion and drafting.** s 13(3) refers to "section (4)(1) of the Public Administration Act 2004", read as s 4(1);
    s 14(e) keeps (ii) and (iii) after (i) was repealed in 2024; s 14(eb) and some definitions print without their indent;
    the text is otherwise as the Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Public Interest Disclosures Regulations (prescribed bodies, officers, entities, services and matters) and the
  penalty unit value, none deposited.
- A lawyer's view on findings 1, 2, 5, 6, 8, 11, 12 and forks F2, F3, F4, F5, F6, F8, F9, F10, F15; an independent test
  pass; a human gate.
- A seat for the employer or manager (ss 44, 48(2), 51) if wanted; ss 28, 29, 33E and 37 for what the person must be told
  later.
