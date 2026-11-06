# Mental Health and Wellbeing Act 2022 (Vic) -- baseline encoding, the person the Act is applied to

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Five files:

- `mhw-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`): plain days, months, and
  business days (weekends worked out, weekday public holidays asked as a count);
- `mhw-rules.l4` -- the law more than one question uses: the s 3 orders and kinds of patient, s 4 mental illness, the s 142
  and s 143 criteria, s 87 capacity, what the Tribunal must do with an order (ss 192, 194, 204, 207), and seven duties with
  deadlines as regulative rules (ss 97(1), 124, 189(1), 204(1), 73/74/90, 76(1), 380(4)) with one trace helper;
- `mhw-seat.l4` -- 54 exported questions of the person the Act is applied to;
- `mhw-cases.l4` -- the cases.

## Edition

- **Act:** Mental Health and Wellbeing Act 2022, Act No. 39/2022, Version No. 010, incorporating amendments as at 30
  September 2026 (the register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/mental-health-and-wellbeing-act-2022.txt` (sha256 3836e5b3...5c3b as committed), a
  plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act fixes its own periods (24 and 72 hours; 7 and 28 days; 3, 6 and 12 months; 2, 5, 10, 20
  and 30 business days) and its limits (12 electroconvulsive treatments). Not deposited, and so asked or left out: the
  Mental Health and Wellbeing Regulations (prescribed information in orders and statements, prescribed persons under s
  54(3)(h)); the Interpretation of Legislation Act 1984 (the meaning of "business day", fork F2); the Public Holidays Act
  1993 (which weekdays are public holidays: asked as a count); the Sentencing Act 1991 (court assessment orders) and the
  Crimes (Mental Impairment and Unfitness to be Tried) Act 1997 (forensic patients), whose terms are asked as facts.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch copy, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `mhw-dates.l4` | 0 | 0 | 0 | 0 |
| `mhw-rules.l4` | 0 | 0 | 0 | 0 |
| `mhw-seat.l4` | 0 | 0 | 0 | 0 |
| `mhw-cases.l4` | 0 | 0 | 335 | 335 |

Every expected value was worked by hand from the text and a calendar, with the edges: an examination 24 hours before
the assessment order and 25; every route to the expiry of an assessment order (community, inpatient received early and
late, not received, both variations, two extensions, an extension over 24 hours); the third extension; the 7 days of s
176; the 28th day of a temporary treatment order across a month end, and a s 374 extension of 5, 10 and 12 business days
with and without a public holiday; the s 189 and s 204 hearings on the last day, the day after, still open and not owed;
the 6 and 3 months of s 193 at 17 and 18 and into a short February; s 191 at 10 and 9 business days and with a holiday;
the 20 business days of s 226 and s 380 and s 383 (from the determination, from the reasons, across Christmas with two
holidays); the 10 business days of ss 73, 74, 90 and s 76 (Melbourne Cup Day); the 5 and 30 business days of ss 97, 124;
the 2 business days of s 373 back over a weekend and a holiday; each person who may act for the patient, and a parent at
15 and 16; every combination of ss 98-117 for adults and young people, patients and not; each way a course of
electroconvulsive treatment ends, for each kind of order; every route of ss 127, 128 and 132 (who may authorise which
intervention); the s 137 minimum frequencies at the limit and just over; the s 434 12 months on the last day and the day
after.

## Seat

**The person the Act is applied to** (`mhw-seat.l4`): the person examined for, or made subject to, an assessment order,
a court assessment order, a temporary treatment order or a treatment order; a patient asked to consent to treatment,
medical treatment, electroconvulsive treatment or neurosurgery for mental illness; a person in a designated mental health
service who may be secluded or restrained; a party before the Mental Health Tribunal; and a consumer who wants to
complain. Questions are asked as that person asks them: "Would I be considered to have mental illness?", "Can an
assessment order (a temporary treatment order) be made on me, and can it be inpatient?", "When does it expire?", "Was my
hearing held in time?", "What must the Tribunal do?", "Who may apply to revoke my order, or seek a second opinion, or ask
for review of my transfer?", "Is my order still in force?", "Can I have leave?", "Did I get written reasons in time?",
"Have I given informed consent, and can I be treated without it?", "Who may consent to my medical treatment?", "Can
electroconvulsive treatment or neurosurgery be performed on me?", "Can I be secluded or restrained, and was I monitored
as required?", "Can my communication be restricted?", "Is my advance statement (my nomination) in effect?", the Tribunal's
procedural deadlines, VCAT review, and complaints.

No seat for the authorised psychiatrist, the chief psychiatrist, the Mental Health Tribunal, VCAT or the Mental Health
and Wellbeing Commission: their satisfaction, determinations and decisions are asked as facts; their duties to the person
with a fixed deadline (ss 73, 74, 76, 90, 97, 124, 189, 204, 373, 380) are encoded as what the person must be given or
have done, by when. No further seat is added: the duties of carers, nominated support persons and service providers
under this Act are owed to the patient and are not ones a private party would ask about as their own liability.

**Design defaults** (ruled 2026-10-18), each followed: the Act alone, with nothing else deposited to bring in; the actors
the text names (the registered medical practitioner, the authorised mental health practitioner, the authorised
psychiatrist, the chief psychiatrist, the Tribunal and its principal registrar and President, VCAT, the Commission); every
judgment ("satisfied", "appears", "reasonably available", "exceptional circumstances", "special circumstances") an input,
never decided; the Act's own definitions worked out (patient, eligible patient, young patient, mental illness, capacity,
informed consent, bodily restraint), borrowed terms asked (instructional directive, medical treatment decision maker,
guardian, forensic patient, child protection order, public holidays); the natural unit is one person and one order; the
Act's terms with plain glosses in each `@desc`; the operative sections in, the machinery out (below).

## Scope

**Focus:** mental health services, compulsory assessment and treatment, rights, the Mental Health Tribunal. The Act has
18 Chapters and about 800 sections; Chapters 2, 3 and 4 (rights, treatment, compulsory assessment and treatment) are
encoded nearly whole for the person's questions, with the Tribunal's procedure that the person meets.

**In:** s 3(1) (patient, eligible patient, young patient, young person, bodily restraint, restrictive intervention), s 4,
s 5 (as a gloss); Chapter 2: ss 53, 54, 57-59, 62-65 (in effect, revoked), 67, 68, 69(2), 73(2)-(3), 74(3)-(4), 75, 76(1);
Chapter 3: ss 85(2), 86, 87(1), 89, 90, 91, 92, 93, 94-117 (electroconvulsive treatment, all four Divisions), 119, 120,
121(1)-(2), 124, 126-128, 132, 137; Chapter 4: ss 142-147, 153-155 (durations), 160, 161, 164, 165, 175, 176, 180, 181,
183, 189, 191, 192-194, 200, 204, 205-209, 212, 217, 226, 227; Part 7.5: ss 363(a), 373(1), (8), 374, 376, 380, 383;
Part 9.2: ss 431-434.

**Out, and why:**
- Chapter 1 Parts 1.3-1.6 (objectives, statement of recognition, principles) and Part 3.1 (decision making principles):
  s 10(2) and (3) say the principles create no legal right and no cause of action; they shape how decisions are made,
  which the encoding takes as the decision-maker's judgment.
- The duties to tell, explain and give copies "as soon as practicable" (ss 32-40, 150-152, 156-158, 162-163, 166-169,
  171-173, 177-179, 186-188, 198-199, 202-203, 210-211, 215-216, 218-220, 225): no fixed day; the person's entitlement
  to a statement of rights (ss 36-40) and to be told of each order are real but have no deadline to run. Candidates for a
  later layer as untimed duties.
- Part 2.3 (advocacy services, protocols, opt-out register) except as glossed; ss 47-49: the advocate's powers.
- Part 4.3 Division 1 and s 177 (reports to the court), s 170 (assessment change), Part 4.8 s 223 (the power to move a
  person; s 226 review is in), ss 221, 224.
- Part 3.7 ss 129, 131, 133-136, 138, 139 (the considerations, documentation, notice, facilities, review and transport
  sedation): ss 127, 128, 132 and 137 carry the person's questions.
- Chapter 5 (crisis response, care and control by authorised persons, entry, search, bodily restraint by police and
  paramedics): outside the focus; a natural next layer.
- Chapter 6 (administration), Chapter 7 Parts 7.1-7.4 and 7.6 (the Tribunal's establishment), Part 7.5 ss 362, 364-372,
  375, 377-379, 381, 382, 384-388 (procedure without a person's question, or offences with penalties in units not
  encoded), Chapter 8 (community visitors), Chapter 9 except ss 431-434 (the Commission's handling and investigation),
  Chapter 10 (security patients), Chapter 11 (forensic patients), Chapter 12 (intensive monitored supervision, except its
  effect on leave in s 212(3)), Chapter 13 (interstate), Chapters 14-16 (institutes, the Collaborative Centre, youth
  services), Chapter 17 (general: information, offences, regulations), Chapter 18 (transitional).

## Fork register

- **F1** Counting days. "within 7 days ... after" (s 176): the day itself not counted, so the last day is 7 days after.
  "28 days after it is made, beginning on and including the day the order was made" (s 183) and the same words in s 204(1):
  day 1 is that day, so the 28th day is 27 days after it, and the order is in force through that day. Other reading: the
  order runs to the same time of day 28 days later.
- **F2** Business days. Not defined in the Act; the Interpretation of Legislation Act 1984 (not deposited) excludes
  Saturdays, Sundays and public holidays. Weekends are computed; the person is asked how many weekday public holidays
  fall in the period, and the period is lengthened by that many business days. A holiday in the lengthened tail is the
  person's to count.
- **F3** Months. "6 months" (ss 193, 96) and "12 months" (s 434): the same date that many months on, or the last day of a
  shorter month (31 August 2026 + 6 months = 28 February 2027). s 193 "must not exceed 6 months" is read as ending on
  that date; other reading: the day before.
- **F4** "at least n business days before" (ss 191(1)(a), 373(1)): the later day (the order's last day, the hearing day)
  counted, the earlier day not. Other reading: n clear business days between them, one more.
- **F5** ss 86(1) and 87(1) say "may be given ... if" and "has capacity ... if": read as full tests, so a failed limb
  answers no (JUST FALSE). Other reading: sufficient conditions only, NOTHING when a limb fails.
- **F6** s 165 "extend an assessment order for up to 24 hours": the extension's hours are added to the time the order
  would otherwise expire. Other reading: up to 24 hours from the moment of extension.
- **F7** ss 161 and 205 "must immediately revoke ... if the authorised psychiatrist determines": a duty whose "if" is
  unmet (no determination yet) answers JUST FALSE (the duty is not engaged). Other reading: NOTHING.
- **F8** ss 58(2) and 62(2) "must be signed ... witnessed ...": a statement or nomination without them is read as not made,
  so not in effect (JUST FALSE). Other reading: a "must" not done, NOTHING. Prescribed information (s 58(2)(e), s 59(2)(e))
  is not asked.
- **F9** s 193: the person's age is read at the making of the order.
- **F10** "the date by which the course ... must be completed is reached" (ss 102, 107, 112, 117): reached on that day, so
  the course has ended on it.
- **F11** s 119 with s 121(2): an approval is counted only where the person's written consent and the Tribunal's
  satisfaction of benefit are both given.
- **F12** s 212: outside s 212(3) the psychiatrist "may grant" leave for any purpose and period they think appropriate;
  the answer JUST TRUE means leave may be granted, not that it must.
- **F13** s 90 is checked only where the treatment decision departs from the preferred treatment in an advance statement
  that is in effect.
- **F14** "the DFFH Secretary, who has parental responsibility for me" in the list of who may act is read as the Secretary
  with parental responsibility "under a relevant child protection order" (ss 67(2)(d), 206(2)(e), 226(2)(d)).
- **F15** s 132: "reasonably available" (s 132(1)(b), (2)(b)) and "immediately available" (s 132(4)(a)) are asked as
  separate facts.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 and s 4(1) and the flat negative of s 4(2) answer TRUE/FALSE; the "if"
conditions of ss 144(1), 165, 180(1), 217, 75(1), 86, 87 (F5), the "must not ... unless" of ss 145(2), 160, 175, 181(2),
194(2), 119, 121(2), 128(2), 374(1), 376, the "only" of ss 54(2), 90(1), 127, 128(1), 132, 212(3), the "cannot" of s
54(3), the "must not ... other than" of s 94, the periods of ss 144(1)(a) ("within the previous 24 hours"), 206 ("while
the order is in force"), 212(3) ("a maximum period of 7 days"), 226 ("within 20 business days"), 374(2) ("not exceeding
10 business days") and the minimum frequencies of s 137 give `JUST FALSE`. `NOTHING` is answered where a grant does not
reach the person or the actor (ss 54 for a person not an inpatient; 67, 75, 206, 226 for a person not in their lists;
67 for an assessment patient; 89, 92 for a person not a patient; 180, 200, 205, 206, 212 for orders outside them; 383 for
a non-party; 431, 432 for a matter outside their heads) (*limited by its own wording*). The Treatment without consent
and Temporary treatment order answers say the same in words ("s 89 does not reach me", "s 180 does not reach me").

## What the Act turns out to say

1. **s 154(1) has a redundant limb.** An inpatient assessment order varied to a community order expires at "the earlier
   of" 24 hours after the patient was received (if received before the variation) and 24 hours after the variation. Where
   (a) applies it is always the earlier, so (b) bites only when the patient was never received. Asserted (29, 44, 27).
2. **An assessment order can last 120 hours.** An inpatient assessment order runs to 72 hours at most (s 147(2)(b)), and
   s 165 allows two extensions of up to 24 hours each. Asserted (120).
3. **s 204(3) has a gap.** The Tribunal must confirm if satisfied the patient "cannot" be treated in the community, and
   vary if satisfied the patient "can"; if it is satisfied of neither, neither limb applies. The encoding asks one yes/no.
4. **A temporary treatment order made inpatient gets no s 204 hearing.** s 204 applies only to a community treatment
   order varied to an inpatient treatment order; a temporary treatment order varied the same way (s 200(1)(a)) is heard
   only at the s 189 hearing before it expires. Asserted (not owed).
5. **A mental health advocate may apply to revoke an order, but not for review of a transfer.** s 206(2)(c) names "a
   mental health advocate"; s 226(2) does not, though s 45(a)(viii) says an advocate's role includes assisting the
   consumer "to apply to the Mental Health Tribunal". Asserted (JUST TRUE under s 206, NOTHING under s 226).
6. **An assessment patient cannot seek a second psychiatric opinion.** s 67 gives the right to an "eligible patient",
   which s 3(1) limits to temporary treatment, treatment, security and forensic patients. Asserted (NOTHING).
7. **Drafting slips in the deposited text** (check against the authorised PDF): s 43 "the primary non-legal mental health
   service provider" (the defined term has "advocacy"); s 51(3) "The Chief Office must publish"; s 86(2)(c) "treatments
   that are reasonable available"; s 90(1) "advance statement of preference" (the defined term is "preferences"); s
   109(1)(b) "capacity to give informed consent the course" (a missing "to"); s 112(2)(d)(ii) "electroconvulsive therapy"
   (the defined term is "electroconvulsive treatment"). None changes an answer here.
8. **Seclusion needs no continuous observation.** s 137(2) requires continuous observation for bodily and chemical
   restraint only; a secluded person is reviewed every 15 minutes and examined every 4 hours. Asserted.
9. **A registered nurse may authorise physical restraint only to prevent harm.** s 132(4)(b) ties it to s 127(a), so a
   nurse cannot authorise restraint to give treatment, and never mechanical restraint or seclusion. Asserted.
10. **Custody suspends but does not extend an order.** s 227(2), (3): an order has no effect while the person is in a
    prison, youth justice centre, police gaol or (unless treated as an inpatient) immigration detention, but still expires
    on time. Asserted.
11. **Young people and electroconvulsive treatment.** A person under 18 cannot consent to it alone (ss 108, 113: only a
    Tribunal order), but the Tribunal may authorise it on their written consent (ss 110(a)(i), 115(a)(i)), and the course
    then ends if they withdraw it, not when they "regain" capacity (ss 112(2)(c), 117(2)(c)). Asserted.
12. **No time limit for a revocation application.** s 206 allows one "at any time while the order is in force", and s
    207(1) requires a hearing only "as soon as practicable"; neither has a day to run. Not encoded as a deadline.

## Before this is worth relying on

- Check the conversion of each quoted section against the authorised PDF (not saved).
- Bring in the Mental Health and Wellbeing Regulations (prescribed information, prescribed persons) and the
  Interpretation of Legislation Act 1984 definition of business day; replace the public-holiday count with the Public
  Holidays Act 1993 calendar if it is deposited.
- Decide forks F1 (whether the 28th day ends the order at its start or end), F3, F4 and F6 with a lawyer; they move
  deadlines by a day or more.
- Add the untimed duties to inform and give copies (the statement of rights, notice of each order) as a later layer, and
  Chapter 5 (crisis care and control) and Chapter 10 (security patients) as further encodings.
- An independent test pass and the human gates.
