# Health Practitioner Regulation (Adoption of National Law) Act 2009 (NSW) -- baseline encoding, the complainant and the practitioner

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 1 July 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Three regulative rules (the Council's 30 days
to tell the complainant the outcome, s 145BA(2); the 28 days to appeal, s 161; the 28 days for a point of law appeal
during an inquiry, s 158A(2)(a)) run by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human
gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is how the Act applies the National Law
with NSW variations: s 4 applies the Health Practitioner Regulation National Law "with the modifications set out in
Schedule 1", s 6 takes NSW out of the national health, performance and conduct process, and Schedule 1 item [15] puts
the NSW Part 8 in its place. That Part is what a patient with a medical negligence or treatment claim meets when they
also complain about the practitioner, and what the practitioner meets in answer. It is encoded; the rest of Schedule 1
is listed under Scope.

## Edition

- **Act:** Health Practitioner Regulation (Adoption of National Law) Act 2009 No 86, corpus document
  `nsw_legislation:2024-07-01/act-2009-086` (in force 1 July 2024), deposited at
  `../../registers/source-bundle/act-2009-086.txt` (text sha256 e7d75b20...f472, per the meta file), taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text.
- **Not deposited:** the Health Practitioner Regulation National Law itself (the Schedule to the Queensland Act: only
  the NSW modifications quoted in Schedule 1 are in the deposit); the NSW regulations under s 247A (prescribed financial
  interests, s 139B(2)(d)); the Health Care Complaints Act 1993 (lodging with the Commission, s 9; conciliation); the
  Civil and Administrative Tribunal Act 2013; the Crimes (Sentencing Procedure) Act 1999 (the value of a penalty unit,
  s 17); the Interpretation Act 1987 (which s 7(2) applies to the NSW provisions; its s 36 day-counting rules). Each is
  asked as a fact, or noted.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hpr-law.l4` | 0 | 0 | 0 | 0 |
| `hpr-seat.l4` | 0 | 0 | 0 | 0 |
| `hpr-seat-practitioner.l4` | 0 | 0 | 0 | 0 |
| `hpr-cases.l4` | 0 | 0 | 149 | 149 |
| `hpr-cases-practitioner.l4` | 0 | 0 | 71 | 71 |

Every expected value was worked by hand from the text, with the edges: a 5% shareholding and 4.99% (s 139B(2)(a));
disclosure meeting the "unless" (s 139B(1)(i)); profession-specific heads asked of the wrong profession (ss 139C, 139D);
the outcome notice on day 0, 30 and 31, and its last day over February in 2026 and 2028 (s 145BA); an appeal on day 28
and 29, across a year end and across February in a common and a leap year (s 161); a point of law appeal on day 28 and 29
(s 158A(2)(a)); 14 and 13 clear days' notice of an inquiry, across a month end (s 171(4)); each fine cap, with a court
penalty, no "no other order" finding, the wrong body for the profession, and a penalty unit of 100 and 110; each limb of
s 149C; each document of ss 147B, 147C, 148I, 150, 150A, 150B; for s 163A, a suspension or conditions made by a Council
by urgent action (s 150) against the same order made at a Council meeting or by a named body. Mirror cases ask the same
facts from both seats.

The periods of the three regulative rules are named once in `hpr-law.l4` (`the s 145BA(2) period`, `the s 161 period`,
`the s 158A(2)(a) period`); each rule takes its period after `WITHIN`, the last days (`last day to give notice of the
outcome`, `last day to appeal`) are worked from the same names, and "not yet due" is asked of the s 145BA(2) rule
itself, so no date can drift from its rule. The earliest day of a Professional Standards Committee inquiry (s 171(4))
is not a regulative rule: it is 14 clear days, worked as the day of notice plus 15.

**Fix after an independent check (2026-11-08).** `Can I apply for review of the order` answered yes to any suspension
or conditions without asking who made the order. s 163A(4) makes a "relevant order" one "made by a decision-making
entity", and a Council counts "but only" for orders under Division 8, Subdivision 5 of Division 3 or s 155C(1)(f); a
Council's urgent suspension or conditions under s 150 is outside it. The question now asks who made the order (fork
F12). The deadlines were also re-tied to the rules' periods (above), and the Out list now names every operative section
of the Part that is not encoded.

## Seats

**First seat (required): the complainant** -- `hpr-seat.l4`. A patient hurt or let down by a registered practitioner, a
family member, or anyone else (s 144B(1): "Any person can make a complaint"), who is often weighing or bringing a civil
claim over the same treatment. Questions: "Can I complain?", "Where do I lodge it?", "Could it be unsatisfactory
professional conduct / professional misconduct?", "Must it go to the Tribunal?", "Which bodies can hear it?", "By when
must the Council tell me the outcome?", "Can I have a lawyer?", "Is my appeal in time?", "What can happen to the
practitioner?", "Can my fees be refunded?", "Can I be made to pay costs?", "Can this be used in my civil claim?".

**Second seat: the practitioner complained about** -- `hpr-seat-practitioner.l4`. The registered health practitioner
who answers the complaint (and often the civil claim). Questions: "Must the Council suspend me now?", "What must it do on
my review application?", "Can I appeal, and is it in time?", "Does the decision bind me while I appeal?", "Can I apply
for review of the order?", "Can I register again?", "What follows if I did not attend the examination?", "What is the
most I can be fined?", "Can I have a lawyer?".

Both seats IMPORT `hpr-law.l4`, which holds the shared definitions and rules, so they cannot disagree; each keeps its own
names. Officials (the Councils, the Health Care Complaints Commission, the Committees, the Panels, the Tribunal, the
National Boards, the Secretary) get no seat: their duties and powers appear as what they mean for the two parties.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The value of a penalty unit is set outside the
  Act and is asked; the NSW regulations are not deposited and the one thing they prescribe here (s 139B(2)(d)) is asked.
- **The actors the text names.** Followed: Council, Executive Officer, Commission, Professional Standards Committee,
  Assessment Committee, Impaired Registrants Panel, Tribunal, Tribunal List Manager, National Board, complainant,
  registered health practitioner.
- **Judgments answered conditionally.** Followed: "satisfied", "of the opinion", "thinks", "sufficiently serious",
  "sufficient", "reasonable excuse" are inputs, and each `@desc` says whose judgment it is.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "competent" (s 139), "financial interest"
  (s 139B(2)), "unsatisfactory professional conduct" (ss 139B-139D), "professional misconduct" (s 139E), "relevant
  health practitioner" (ss 146, 147, 168), "notifiable outcome" (s 145BA(1)), "relevant order" (s 163A(4)) are worked
  out; "impairment", "critical compliance order or condition" (beyond the fact of it), "suitable person" are asked.
- **One case.** One complaint about one practitioner.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 and s 6 (framing: the National Law applied with modifications, NSW out of the national process; no question
of their own); Schedule 1 item [13]: ss 139, 139B, 139C, 139D, 139E, 139G, 139H; item [15]: ss 144, 144B, 144C, 144D,
144E, 145B(1), 145BA, 145D, 145F, 145G, 145H, 145I, 145J, 146, 146C, 146D, 147, 147A, 147B(3), 147C(3), (7), 147E, 148,
148D(6), 148E(1)(b), 148F, 148G, 148H(1), 148I, 149, 149B, 149C (incl. (4A), (5), (5A)), 149E, 150(1)-(4), 150(6A),
150A, 150B(2), 158, 158A(2), 159, 159B, 161, 161B, 163(2), 163A, 165J, 168, 171(4), 171B; Schedule 5D cl 13.

**Out, and why:**

- ss 1-3, 5, 6A-6C, 7-9: names, commencement, generic terms, declarations of bodies, the Acts that do and do not apply,
  regulations and review -- machinery. ss 6A-6C are reflected in who the bodies are.
- Schedule 1 [1A] (ss 3A, 3B guiding principles): give the individual no rule to apply; [1]-[6] definitions notes;
  [7] (s 26A, the complaints element of registration fees), [8] (Part 5A, the Councils): machinery.
- [9]-[10A] (s 121A general anaesthesia and sedation in dentistry; s 127AA review body): practice rules and their
  offences, a different seat (the dentist running a practice), and not part of the complaints route.
- [11A] (s 136A, directing or inciting unsatisfactory professional conduct, max $60,000 / $120,000): an offence by a
  third party (typically an employer); a third seat, not written.
- s 139I, [14AC] s 142A, [14A] s 143A (mandatory notifications taken to be complaints): the notification duties are in
  National Law Part 8 Division 2, not deposited.
- s 144A and the student provisions (ss 145E-145F as to students, 148E(2), 149A(2), 149C(2), 152C, 152M, 159A): the
  seat is a patient's complaint about a practitioner.
- ss 145A, 145B(2)-(4), 145C, 145E, 146A-146B, 146E, 147B(1)-(2), 147C(1)-(2), (4)-(6), 148A-148C, 148D(1)-(5),
  (7), 148E(1)(a), (c)-(g), 148H(2)-(8), 149A, 149D, 150(5)-(7), 150C-150J: the bodies' procedure and the list of
  non-monetary orders, which give the parties nothing to compute beyond what the encoded questions already answer.
- Divisions 4 and 5 (ss 152-157: impairment and performance assessment): a referral there "ceases to be a complaint"
  (s 145B(3)); a separate pathway with the practitioner as the only party. Its notice to the complainant is encoded
  through s 145BA(1)(b).
- Division 8 ss 163B-163C (powers on review), Division 9 (enforcement), Divisions 10-14 (constitution of the bodies),
  ss 165A-165I, 165K-165M, 169-171A, 171C-171G, 172-174D: machinery; Division 14A (ss 175-175C): appeals against
  National Board registration decisions, not the complaints route; Division 14B (ss 176-176F): notices to employers
  and protections, addressed to bodies.
- ss 139A (confidential information in a statement of a decision), 139F (a "complaint" includes a matter arising from
  its investigation), 144F (a Council or the Commission may ask the complainant for further particulars), 144G (a
  Council must notify the Commission and the National Board of a complaint): definitions and steps addressed to the
  bodies, with no period and no answer the parties compute. s 144F's consequence for the complainant (a complaint may
  then not be referred, s 145J) is encoded through `Can my complaint be referred for a hearing`.
- s 147D (the Assessment Committee's recommendations): (1) and (4) are the bodies' procedure. (3)(b) does give the
  practitioner (and the Commission) a period: the Council must allow "not less than 21 days after they have been given
  a copy of the Committee's report" to make submissions, unless the Committee recommended an inquiry at a Council
  meeting ((3)(a)). It is a minimum the Council must allow, with no last day the practitioner must meet, and it arises
  only for an Assessment Committee, which hears complaints about medical and nursing and midwifery practitioners
  (s 147); not encoded in this pass, and left for a later one. (An earlier version of this note said s 147D gave
  "nothing to compute"; that was wrong as to (3)(b).)
- s 159C (the Tribunal's powers on an appeal against a Council's decision): confirm, set aside, or set aside and
  substitute; (2) a suspension or conditions imposed by a Council cannot, by the Tribunal's order, outlast the day a
  related complaint is disposed of. It describes what the Tribunal may do once an appeal is heard, not whether the
  practitioner may appeal or by when; not encoded. (2) matches s 150(2), which is encoded.
- ss 160, 160A (Division 6 Subdivision 3: appeals against a Performance Review Panel's decisions, including a point of
  law appeal "within 28 days after the date of the Performance Review Panel's decision" during a performance review):
  they arise only from a performance review under Division 5, the separate pathway left out below, and the
  complainant is not a party to it.
- Schedule 5D cl 12 (an inquiry may be ended; it must end if the practitioner dies): consistent with s 145H, which is
  encoded; not encoded separately. Schedule 5D cll 1-11, Schedules 5A-5C, 5E, 5F (including pharmacy business
  ownership), items [16]-[25] (confidentiality, protection from liability, evidentiary certificates, regulations,
  savings and transitional): machinery, or a different seat.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 139 "competent ... only if" -- `competent to practise` -- all four limbs met answers `JUST TRUE` (read as a
  definition) -- `NOTHING`, since "only if" states only necessary conditions.
- **F2** s 139B(2) "has a financial interest ... if ..." -- `has a financial interest` -- none of (a)-(d) answers `JUST
  FALSE` (an "if" condition) -- `NOTHING`, as a list not closed with "only".
- **F3** s 171(4) "not less than 14 days' notice" -- `given enough notice of the inquiry` -- 14 clear days (neither the
  day of notice nor the day of the inquiry counts) -- 14 days counting the inquiry day (one day earlier).
- **F4** ss 146C(2)(a), 148F(2)(a) "guilty of unsatisfactory professional conduct" -- `maximum fine in dollars` -- a
  finding of professional misconduct meets it (s 139E: it is unsatisfactory professional conduct of a serious kind) --
  only a finding framed as unsatisfactory professional conduct does.
- **F5** s 159(1) "A person may appeal" (paragraphs (a1), (a), (d) do not say whose decision) -- `Can I appeal against
  the Council's decision` -- the practitioner the decision is about; the complainant has no s 159 appeal -- anyone,
  including the complainant, may appeal a reprimand or a s 148E order.
- **F6** ss 145BA(2), 158A(2)(a), 161 "within N days after" -- the three regulative rules -- the day of the event is day
  0 and day N is the last day; Interpretation Act 1987 s 36 (a last day falling on a weekend or holiday) is not applied,
  the Act not being deposited -- extend the last day to the next working day.
- **F7** s 144 "The following complaints may be made" -- `Can I make a complaint` -- a ground outside the list, or a
  person never registered, answers the "not provided for" constructor -- a firm no.
- **F8** ss 145B(1)(d), 146, 169A -- `Which bodies can hear my complaint` -- a Professional Standards Committee only for
  medical and nursing and midwifery practitioners (its powers and constitution reach only them), so not listed for
  others -- s 145B(1)(d) lets a Council refer any complaint to "a Committee".
- **F9** ss 149E, 163A -- `Can I apply to be registered again`, `Can I apply for review of the order` -- facts outside
  the bars answer `NOTHING` (Part 7 of the National Law, not deposited, governs registration) -- `JUST TRUE`.
- **F10** s 148E(1)(b) -- `Can my fees be ordered refunded` -- a Council meeting may order a refund whether or not the
  complaint is proved (Subdivision 5 has no "if proved" condition) -- the power arises only on a finding.
- **F11** s 150(1) "must, if ... satisfied" -- `Must the Council act against me now` -- a duty once the Council is
  satisfied, and no action if not ("if") -- a discretion.
- **F12** s 163A(4) "decision-making entity ... (b1) a Council, but only in relation to orders made under this
  Division, Subdivision 5 of Division 3 or section 155C (1) (f)" -- `Can I apply for review of the order` -- a Council's
  suspension or conditions under any other provision (such as urgent action under s 150) answers `JUST FALSE` (a limb
  the text closes with "only"; the routes are s 150A and ss 159, 159B) -- `NOTHING`, as a scope limit of the right to
  review. An order by a body s 163A(4) does not name answers `NOTHING`.
- **F13** s 145BA(1)(b) "refers ... for assessment under section 145B (1) (f)" -- `When must the Council tell me the
  outcome` -- a referral to an Impaired Registrants Panel (s 145B(1)(f)(ii)) is grouped with a health assessment
  ((f)(i)): both are referrals under s 145B(1)(f), and s 145BA(5) ties (1)(b) to the s 145B(3) effect of any (f)
  referral -- only a health assessment under (f)(i) is a referral "for assessment", so the outcome of a Panel referral
  is not a notifiable outcome.
- **F14** s 139H(3) "applies only to the extent (a) a notification about the person's behaviour could have been made
  under the corresponding prior Act; and (b) proceedings of that type could have been taken under the corresponding
  prior Act" -- `Can I make a complaint` -- only (a) is asked: it limits the complaint, while (b) limits the
  proceedings that may follow it, which the question does not ask (the answer says "to the extent that Act allowed")
  -- both limbs gate the complaint, so (b) would be asked too.

## What the Act turns out to say

1. **The NSW complaints scheme is wholly NSW's own.** s 6 declares NSW out of Divisions 3-12 of Part 8 of the National
   Law, and Schedule 1 item [15] omits them and inserts a different Part 8. A patient in NSW complains to a Council or
   the Health Care Complaints Commission, not to the national agency; the hearing bodies are NSW Committees, Councils
   and NCAT. Only the NSW modifications are in this deposit; the unmodified National Law (registration, Part 7) is not.
2. **A refund of fees is available only at a Council meeting, and never for doctors or nurses.** s 148E(1)(b) lets a
   Council at an inquiry at a meeting order fees withheld or refunded; s 148 says that Subdivision "does not apply" to
   medical or nursing and midwifery practitioners; neither the Professional Standards Committee's list (s 146B) nor the
   Tribunal's (s 149A) mentions refunds. A doctor's patient seeking money must use a civil claim. Asserted.
3. **The Council meeting's general powers are not conditioned on proof.** ss 146A and 149 let a Committee and the
   Tribunal act only "if it finds the subject-matter ... proved" or it is admitted; Subdivision 5 has no such condition
   for s 148E (only the fine, s 148F(2)(a), needs a finding). Fork F10.
4. **No period for a point of law appeal after a Committee inquiry ends.** s 158A(2) allows a point of law appeal
   "during an inquiry" (within 28 days of the decision on the point) or "before the commencement ... but after ...
   notice", and s 161 excepts appeals on a point of law. After the inquiry, the text gives no time at all. Asserted
   (`NOTHING`).
5. **The complainant has no stated place at a Council meeting.** s 148D gives the practitioner a right to attend and make
   submissions, and the Commission and the Committee rights to make submissions, but says nothing of the complainant,
   who is entitled to attend and be represented before a Professional Standards Committee (s 171B) and the Tribunal
   (s 165J). The complainant gets only the written statement of the decision (s 148H). Asserted; a mirror case shows
   the two seats differ here.
6. **Representation turns on the body.** Before an Assessment Committee neither side may be legally represented
   (s 147E); before a Professional Standards Committee both may (s 171B); at a Council meeting the practitioner may not,
   but may bring a support person who "can be an Australian lawyer" (s 148D(6)). Asserted.
7. **Not every step is notified to the complainant.** s 145BA's notifiable outcomes leave out a referral to the
   Commission for investigation, to the Tribunal or to a Committee, and the Council's own inquiries. Asserted.
8. **The Council, not the parties, decides whether an Assessment Committee's advice can be used in a civil claim**
   (s 147B(3) "unless otherwise ordered by the Council"); a Council meeting's finding is admissible in any legal
   proceedings (s 148I); the Council's reasons for urgent action, and the recording of its meeting, are not admissible
   in civil proceedings (ss 150(6A), 150A(6), 150B(2)). Asserted.
9. **A civil claim does not hold up the complaint** (s 145G), but the practitioner's death ends it (s 145H; Schedule 5D
   cl 12(2)). Asserted.
10. **s 150(1) is a duty.** "A Council must, if at any time it is satisfied ...", suspend or impose conditions. Fork F11.
11. **Fines are in penalty units; the dollar value is outside the Act.** 50 (Committee, Council meeting) or 250
    (Tribunal). At $110 a unit (Crimes (Sentencing Procedure) Act 1999 s 17, not deposited) $5,500 and $27,500. Asserted
    at 110 and 100.
12. **s 159 does not say whose decision "a person" may appeal** in paragraphs (a1), (a) and (d). Fork F5.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags and follows these rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
> The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
> Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

> - **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means" definitions (ss 139E, 146, 147, 168), "only if" and "if" conditions (ss 139, 139B(2), 147A, 149C,
150(1), 150A(4)), "unless" (ss 139B(1)(i), 139C(c), 146C(2), 148F(2), 149B(2), 149E, 161B), flat negatives (ss 145H,
147E, 148, 148D(6), 159(2), 163A(3)) and periods the text fixes (ss 145BA(2), 158A(2)(a), 161) answer no when they fail;
the "includes" list of s 139B(1), the open lists of s 144 and s 163A, silence (costs and refunds before other bodies,
the stages s 158A(2) does not cover) and matters outside the deposit (Part 7 registration) answer `NOTHING` or a "not
covered" constructor. Sites with no convention have fork lines (F7, F9, F10, F11, F12, F13, F14).

## Questions (exported)

`hpr-seat.l4` (22, the complainant): `Can I make a complaint` (ss 139G, 139H, 144, 144B), `How do I lodge my complaint`
(ss 144C-144E), `Could it be unsatisfactory professional conduct` (ss 139B-139D), `Could it be professional misconduct`
(s 139E), `Is the practitioner competent to practise` (s 139), `Can my complaint be referred for a hearing` (ss 144D(3),
145G-145J), `Must my complaint go to the Tribunal` (s 145D), `Which bodies can hear my complaint` (ss 145B, 146, 147A,
148), `When must the Council tell me the outcome` (ss 145BA, 148H), `Was I told the outcome in time` (s 145BA, regulative
rule), `Was I given enough notice of the inquiry` (s 171(4)), `Can I have a lawyer at the hearing` (ss 147E, 148D, 165J,
171B), `Can I be ordered to pay costs` (Sch 5D cl 13), `What is the most the practitioner can be fined` (ss 146C, 148F,
149B), `Can the registration be suspended or cancelled` (ss 146D, 148G, 149C), `Can the practitioner be prohibited from
providing health services` (s 149C(5), (5A)), `Can my fees be ordered refunded` (s 148E(1)(b)), `Can I appeal against
the Committee's decision` (s 158), `Is my appeal in time` (s 161, regulative rule), `By when must I appeal` (s 161(a)),
`Can I appeal on a point of law now` (s 158A(2), regulative rule), `Can it be used in my civil claim` (ss 147B(3),
147C(7), 148I, 150(6A), 150A(6), 150B(2)).

`hpr-seat-practitioner.l4` (14, the practitioner): `Must the Council act against me now` (s 150), `What must the Council
do on my review application` (s 150A), `Can I appeal against the Council's decision` (ss 159, 159B), `Can I appeal
against the Committee, as the practitioner` (s 158), `Is my appeal in time, as the practitioner` (s 161), `Can I appeal
on a point of law now, as the practitioner` (s 158A(2)), `Does the decision still bind me while I appeal` (s 161B), `Can I
apply for review of the order` (s 163A), `Can I apply to be registered again` (ss 149C(4A), 149E), `What follows if I did
not comply` (ss 145F, 147C(3)), `What is the most I can be fined`, `Can I have a lawyer, as the practitioner`, `Was I
given enough notice, as the practitioner`, `Can I be ordered to pay costs, as the practitioner`.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 144B | any person | power (to complain) | `Can I make a complaint` |
| s 145BA(2) | the Council | duty to the complainant, 30 days | regulative rule (`MUST ... WITHIN 30 ... LEST BREACH`) |
| s 145D(1) | the Council, the Commission | duty (refer to the Tribunal) | `Must my complaint go to the Tribunal` |
| s 150(1), (3) | the Council | duty (on satisfaction) | `Must the Council act against me now` |
| ss 158, 159, 161 | complainant, practitioner | power with a time limit | regulative rule (`MUST ... WITHIN 28 ... LEST BREACH`, modelling the lapse) |
| s 147E | both parties | disability (no legal representation) | `representation before the body` |
| Sch 5D cl 13 | complainant, practitioner | liability (costs) | `may be ordered to pay costs` |
| s 149E | the practitioner | disability (cannot apply) | `Can I apply to be registered again` |

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the National Law (the Queensland Schedule) to encode registration (Part 7) and the Division 2 notification
  duties; deposit the NSW regulations (prescribed financial interests), the Interpretation Act 1987 (day counting) and
  the Crimes (Sentencing Procedure) Act 1999 (penalty unit).
- Have a lawyer review the forks, especially F3 (clear days), F5 (who may appeal under s 159) and F10 (refunds without
  a finding).
