# Work Health and Safety Act 2012 (SA) -- baseline encoding, the worker

UNOFFICIAL. Based on content from the South Australian Legislation website at 6 November 2026; (c) State of South
Australia, licensed under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version (the authorised version is the
register's PDF).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on
2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`sawhs-dates.l4`,
built-in date functions only, no daydate), the rules in `sawhs-rules.l4`, and the worker's questions in `sawhs-seat.l4`,
which imports the rules and restates none. The cases are in `sawhs-cases.l4`. The shape follows the Work Health and Safety
Act 2012 (Tas) baseline (`subjects/au/tas/work-health-and-safety-act-2012/encodings/baseline-2026-11/`), since both Acts
follow the model WHS law; every provision was read again in the SA text, and the SA departures (industrial manslaughter
in s 30A with gross negligence and recklessness defined in s 4(2)-(4), SAET instead of a court for Part 6 civil
proceedings, Part 5 Division 7A disputes, s 103, the wider s 231 and s 232(1)(ba), s 260A) are encoded from it. The stable
`l4` cannot IMPORT across subjects, so nothing is shared in code.

## Edition

- **Act:** Work Health and Safety Act 2012 (SA), the South Australian register's current unauthorised RTF, version
  1.7.2025 (in force from 1 July 2025), retrieved from www.legislation.sa.gov.au on 6 November 2026 and deposited at
  `../../registers/source-bundle/work-health-and-safety-act-2012.txt` (text sha256 dcf67689...19bf0e per the meta). Unlike
  the SA texts taken earlier from the Open Australian Legal Corpus (collected 10 March 2025), this one comes from the
  official register; the register's Current Titles list of 22 September 2026 gave it as current. It may still have been
  amended since: check legislation.sa.gov.au before relying on anything here.
- **Regulations that set its numbers:** Work Health and Safety Regulations 2012 (SA), version 1.7.2026, deposited at
  `subjects/au/sa/work-health-and-safety-regulations-2012/registers/source-bundle/work-health-and-safety-regulations-2012.txt`
  (text sha256 df471426...c857887 per the meta). Brought in: reg 24 (the "prescribed purposes" of s 88), reg 699
  (serious illnesses added to s 36), reg 699A (a dangerous incident added to s 37), reg 8A (emergency ambulance staff as
  emergency services workers, s 108(3), in a gloss), reg 7 (bodies that may be taken not to conduct a business, in a
  gloss). The Regulations were searched for anything made "for the purposes of" ss 7, 35-39, 83-115, 184, 223-232 and
  267-273: nothing else was found, so the s 7(1)(i) class, the s 36 and s 37 exclusions "of a prescribed kind" and further
  s 37(l) events are empty, and the "means" definitions answer `JUST FALSE` outside their lists. Item 13 of the s 223
  table (decisions under the regulations, reg 676) is not encoded.
- **Borrowed terms asked as facts:** "business or undertaking", "employee", "volunteer", "officer" (defined by reference
  to the Corporations Act 2001 (Cth)), "body corporate", "detriment", "hazard", "personal representative", "Criminal
  Procedure Act 1921".

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; a
deliberately wrong assertion was run once in a scratch file in this folder (deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `sawhs-dates.l4` | 0 | 0 | 0 | 0 |
| `sawhs-rules.l4` | 0 | 0 | 0 | 0 |
| `sawhs-seat.l4` | 0 | 0 | 0 | 0 |
| `sawhs-cases.l4` | 0 | 0 | 261 | 261 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the
s 113(1) last day and the day after (10 / 11 March 2026; 28 February / 1 March 2025 from 29 February 2024); the 48th and
49th hour of s 38(4)(b); the 23rd and 24th hour of s 102B; the s 260A(2) month (15 February / 16 February; 28 February /
1 March from 31 January 2026); the s 224 14 days and an improvement notice's shorter compliance period; the s 229(2)
14th / 15th day and the 28-day forfeiture limit, with and without a statement of reasons; the s 231(1b) window at the
6-month day and the day before, the 24-month day and the day after, from 31 August (6 months is 28 February), and the
coronial 12 months either side; the s 231(2) last day and the day after, answered and not; the s 232 periods with a
coroner's report, a DPP referral and a breached undertaking, each later and earlier than the 2 years; every fine and
prison term in ss 30A, 31-33, 38, 39, 102C(4), 104, 107-109 and 273 for each kind of offender.

## Seat

**The worker** (`sawhs-seat.l4`): the individual (or prospective worker) who is hurt, put at risk, stops unsafe work, or
is dismissed or otherwise treated badly for raising safety, and who brings or presses a claim about it -- or, where a
worker has died, the family member or personal representative asking on the worker's behalf. "Am I a worker?", "Does the
business owe me the duty?", "Must I follow this instruction?", "Is my injury notifiable, and was it notified?", "May I
stop this work, and is my job safe if I do?", "Can I take my safety dispute to SAET?", "Can I take them to SAET for
sacking me over a safety complaint, and by when; what can SAET order?", "What offence did they commit and what can they
get?", "Can I have the inspector's decision reviewed, and by when?", "Can I ask for a prosecution, and by when must the
regulator and the DPP answer?", "By when can they be prosecuted?", "Does the Act let me sue?", "Is this contract term
void?", "Can they charge me for safety gear?". No seat for the business, the regulator, inspectors, the Director of
Public Prosecutions, SAET or the courts: their judgments and findings are asked as facts. A business seat
(`sawhs-seat-business.l4`) would be a natural further layer.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulations' regs 24, 699 and 699A are
  brought in (see Edition).
- **The actors the text names.** Followed: the worker and prospective worker, the person conducting a business or
  undertaking, the officer, the health and safety representative, the personal representative of a deceased worker, the
  regulator (the Executive Director), the inspector, the internal reviewer, SAET, the Director of Public Prosecutions,
  the court, the State.
- **Judgments answered conditionally.** Followed: "reasonable concern" (ss 84, 85), "reasonably considers" (s 231),
  "reasonable instruction" and "reasonably able" (s 28), "without reasonable excuse" (s 31), "merits criminal punishment"
  (s 4(2)), "unjustifiable" (s 4(3), a question of fact by s 4(4)), "unreasonably failed" (s 88), "just" (s 184),
  "frivolous, vexatious, misconceived" and "without reasonable cause" (s 102F), "contrary to the interests of justice"
  (s 260A(4)), "reasonable in the circumstances" (s 113(3)) and what a court or SAET finds proved (ss 110, 113) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: worker (s 7), gross negligence and recklessness
  (s 4(2), (3)), notifiable incident, serious injury or illness, dangerous incident (ss 35-37 with regs 699, 699A), cease
  work (s 83), dispute and WHS matter (s 102A), discriminatory conduct and prohibited reason (ss 105, 106), eligible
  person (ss 112(6), 223) are worked out from facts.
- **One case.** One incident, one piece of conduct, one dispute, one decision, one offence.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4(2)-(4); s 5(1), (7), (8) (so far as they decide who is a worker); s 7; s 19(1), (2); s 28(c); Part 2
Division 5 (ss 30, 30A, 31-34); Part 3 (ss 35-39); Part 5 Division 6 (ss 83-88, 85A); Part 5 Division 7A (ss 102A, 102B,
102F; s 102C(4)'s penalty); s 103; Part 6 (ss 104-115); s 184; Part 12 ss 223, 224, 226, 228, 229; ss 230(1), (9) (in a
gloss), 231, 232; s 260A; s 267 (with s 260); ss 272, 273. Regs 24, 699, 699A (and 7, 8A in glosses). s 38(2)-(6) (how
notice is given) and s 86(b), s 87 (alternative work) are in the descriptions of the questions they bear on.

**Regulative rules:** five, each run by EVALTRACE inside a question that takes only plain facts: the s 113(1) time bar
(`PARTY the applicant MUST commence the proceeding WITHIN` the days to the first anniversary, `LEST BREACH ... BECAUSE`),
inside `Can I apply to SAET about discrimination or coercion` and `Can SAET make this order for me`; the s 38(4)(b)
written notice (`PARTY the business MUST give the written notice of the incident WITHIN 48` hours), inside `Was the
written notice given in time`; the s 231(2) advice (`PARTY the regulator MUST advise the requester in writing WITHIN` the
days to the 3-month day), inside `Did the regulator advise me in time`; the s 229(2) external review application, inside
`Can I apply to SAET for external review`; the s 260A(2) proceeding for a contravened arbitration order, inside `Can I
bring proceedings for a breached SAET order`.

**Exported questions (47):** `Am I a worker`; `Does the business owe me the primary duty of care`; `Must I follow this
instruction`; `Is my injury a serious injury or illness`; `Was it a dangerous incident`; `Must the business notify the
regulator`; `Was the written notice given in time`; `Until when must the record of my incident be kept`; `Does the Act
forbid disturbing the incident site`; `May I cease or refuse this work`; `Could the representative direct me to cease
work`; `Must I tell the business I ceased work`; `Is the continuity of my engagement unaffected`; `Can I take my safety
dispute to SAET`; `Could SAET order me to pay costs of the dispute`; `Can I bring proceedings for a breached SAET order`;
`By when must I bring proceedings for a breached SAET order`; `Should SAET order my costs for the breached order`; `Was
it discriminatory conduct for a prohibited reason`; `Can I apply to SAET about discrimination or coercion`; `By when must
I start my SAET proceeding`; `Can SAET make this order for me`; `Can the criminal court order compensation or
reinstatement for me`; `Is the discrimination offence made out`; `Was the representation to me prohibited`; `What is the
most they can be fined for this contravention`; `Which offence do these facts make out`; `What is the maximum fine for
the offence`; `What is the longest prison term for the offence`; `Can I seek review of this decision`; `By when must I
apply for internal review`; `By when must my internal review be decided`; `Is the decision stayed while it is reviewed`;
`By when must I apply to SAET for external review`; `Can I apply to SAET for external review`; `Can I ask for a
prosecution`; `By when must the regulator advise me`; `Did the regulator advise me in time`; `By when is my next
investigation update due`; `By when must my matter be referred to the DPP`; `By when must the DPP advise the regulator`;
`By when can they be prosecuted`; `Can they still be prosecuted on this day`; `Does the Act give me a right to sue`; `Is
this term of my contract void`; `Can the business charge me for this`; `Can the court order the State to compensate me`.

**Out, and why:**
- ss 1, 3, 6, 8-12, Part 1 Division 5 (ss 12A-12G, the SafeWork SA Advisory Committee) and the Schedules: short title,
  object, supply, application, the Crown, extraterritoriality, the advisory committee, regulation-making subjects,
  administration, transitional provisions. s 8 (workplace) is glossed in a `@desc`.
- Part 2 Division 1 (ss 13-18): principles and "reasonably practicable"; whether a duty was met is a judgment, entered as
  the fact "they failed to comply with that duty". s 19(3)-(5) and ss 20-26 (the further duties of designers,
  manufacturers, importers, suppliers, installers, and of those who manage workplaces or plant), s 27 (officers' due
  diligence), s 28(a), (b), (d) and s 29: duties whose content is a judgment; they enter the offence question as "a
  health and safety duty was owed". Officers are folded into the "individual conducting the business, or an officer of
  it" kind (s 27(2)); s 27(3)'s penalty for an officer's breach of a non-Part 2 duty is not encoded.
- Part 4 (authorisations), Part 5 Divisions 1-5 and 7 (consultation, health and safety representatives and their
  election, committees, issue resolution, provisional improvement notices), ss 102C-102E (how SAET deals with a dispute;
  its powers, not the worker's questions; s 102C(4)'s penalty is in), s 89 (a request for an inspector, asked as a fact in
  the s 102B question).
- Part 7 (entry by WHS entry permit holders, including the s 142 entry disputes; s 142(3) orders appear only in s 260A),
  Parts 8-11 (regulator, inspectors' powers, notices, enforceable undertakings) apart from s 184: powers of officials
  and unions.
- Part 12 ss 225, 227 (who reviews; the duty to give reasons, no time stated beyond "as soon as practicable") and the
  regulations' reviewable decisions (s 223 item 13, reg 676).
- Part 13 apart from ss 230-232, 260A and 267: s 230(2)-(12) (which court tries what), s 233, sentencing orders,
  infringement notices, bodies corporate, the Crown, public authorities, WHS civil penalty proceedings (brought only by
  the regulator or an inspector, s 260, which is cited).
- Part 14 apart from ss 272, 273: false information, privilege, immunity, confidentiality, s 272A (insurance against
  penalties, a rule for the business and its insurer), codes of practice, regulations, reviews.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "not more than 1 year after the date" (s 113(1)), "within 2 years after" (s 232(1)(a)), "for at least 5 years
  from the day" (s 38(7)), "within 3 months after" (s 231(2)), "at least every 3 months" (s 231(2a)), "within 1 month of"
  (s 231(3)(b)), "within 1 month after" (ss 232(1)(ba), 260A(2)), "within 6 months after" (s 232(1)(c)), "within 14 days
  after the day" (ss 224, 226, 229) -- `the anniversary`, `the date ... months after`, `the day ... days after` -- the day
  itself is excluded, so the last day is the same day of the month a year or months later, or the day that many days
  later; a day the later month lacks falls on its last day (29 February + 1 year = 28 February; 31 August + 6 months = 28
  February) -- the Acts Interpretation Act 1915 (SA), not deposited, may differ at month ends.
- **F2** s 231(1b)(a) "at least 6 months, but no more than 24 months after", (b) "within 12 months after the report" --
  `s 231(1) -- I may request a prosecution` -- the 6-month day and the 24-month day are both in the window; a request on
  the report's own day is in -- the 6-month day itself not "at least 6 months after".
- **F3** s 7(1)(i) -- `s 7 -- I am a worker` -- JUST FALSE where no limb holds, the Regulations having been searched and
  no class prescribed -- NOTHING, if a prescribed class were missed.
- **F4** s 19(1), (2) -- `s 19 -- the business owes me the primary duty of care` -- a worker engaged or directed by the
  business but not at work in it, and not at risk under (2): JUST FALSE (the "while"); neither engaged, directed nor at
  risk: NOTHING (a duty limited in its own wording) -- JUST FALSE for both.
- **F5** s 28(c) -- `s 28(c) -- I must comply with the instruction` -- an instruction that is not reasonable, not given
  to allow the business to comply, or beyond what the worker is reasonably able to do: NOTHING -- JUST FALSE, reading
  the qualifications as conditions.
- **F6** s 37(l) with reg 699A -- `s 37 -- it is a dangerous incident` -- reg 699A's event is read as an event under
  (l), so the incident must still expose someone to a serious risk from an immediate or imminent exposure -- reg 699A
  read literally ("is a dangerous incident"), so that any such loss of control is one.
- **F7** duties and powers whose "if" is unmet -- `s 38(1) -- the business must notify the regulator` (not arising out of
  this business: JUST FALSE), `s 38(4)(b) -- the written notice was given in time` (no requirement: NOTHING),
  `s 86(a) -- I must notify the business that I ceased work` and `s 88 -- ...` (not ceased under the Division: NOTHING),
  `s 111 -- the criminal court may make the order for me` (no conviction: NOTHING) -- the opposite answer at each site.
- **F8** s 104(2) with s 110 -- `s 104 -- an offence of discriminatory conduct is made out` -- no evidence that the
  conduct was for the reason: NOTHING (the presumption is not engaged; dominance is for the court) -- JUST FALSE.
- **F9** s 112(1), (6) -- `s 112 -- I may apply to SAET` -- a person neither affected nor authorised: NOTHING (a grant
  limited in its own wording) -- JUST FALSE, reading (6) as a closed list. The same reading for s 260A(1) ("a person
  affected").
- **F10** s 112(3)(b), (c) -- `s 112(3) -- SAET may make the order for me` -- compensation for s 108 coercion, and
  reinstatement outside (2)(a) or for a worker who was not an employee: NOTHING, since (d) "any other order that SAET
  considers appropriate" may reach them -- JUST FALSE, reading (b) and (c) as the only routes.
- **F11** s 232(1)(c) -- `s 232 -- the time for prosecution` -- the 6 months run from the latest of the breach, its
  coming to the regulator's notice and the withdrawal, entered as one day -- each trigger its own period (the same
  result under "the latest of the following periods").
- **F12** Part 2 offences -- `the most serious offence made out` -- the most serious offence the facts make out is
  answered, industrial manslaughter before Category 1, though s 31 needs exposure without reasonable excuse rather than a
  breach -- the offence charged.
- **F13** s 39(1) "so far as is reasonably practicable" -- `s 39 -- the site must not be disturbed by the action` -- not
  asked: the duty is answered as if practicable -- the judgment as an input.
- **F14** s 229(2)(c) -- `s 229(2) -- the last day to apply for external review` -- where SAET requires a statement of
  reasons, the last day is the later of the (a)/(b) day and 14 days after the statement -- (c) replacing (a)/(b) even if
  earlier.
- **F15** s 231(4) "within 1 month" -- `s 231(4) -- the last day for the DPP's advice` -- 1 month from the referral --
  from the request for referral, or from the DPP's receipt.
- **F16** s 102B(1) "at least 24 hours after" -- `s 102B -- I may give SAET notice of the dispute` -- whole hours since
  the request, 24 or more -- counted from the request reaching the regulator.
- **F17** s 223(1) table -- `s 223 -- I am an eligible person` -- the table read as the closed list of who may apply:
  JUST FALSE where the person is not named (a worker and a s 72(7) training decision) -- NOTHING for an unnamed person.
- **F18** s 229(1) -- `s 229 -- I may apply to SAET for external review` -- an inspector's decision not yet through
  internal review: JUST FALSE -- NOTHING.
- **F19** s 228(5) -- `s 228 -- the decision is stayed pending internal review` -- an application for a stay of a
  prohibition or non-disturbance notice not decided within 1 working day: a stay, as (5) deems -- read only for the
  reviewer's own-motion stays.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" and "if" definitions of ss 4(2), 4(3), 7, 35, 36, 37 (with the regulations they hand to,
deposited), 102A, 105 and 106, the "while" of ss 19(1) and 28, the "if" of ss 84, 85(1), 88, 102F(2), 184(1) and
260A(1), "unless" in ss 85(2), (6), 86(a), 228(1) and 260A(4), "only if" in ss 104(2), 112(4) and 184(3), "applies if"
in ss 102B(1) and 231(1), "may only be made" (s 231(1b)), "cannot" in ss 114 and 115, "nothing in this Part applies"
(s 103), "must be commenced not more than 1 year after" (s 113(1)), "within 48 hours" (s 38(4)(b)), "within 3 months"
(s 231(2)), "within 1 month after" (s 260A(2)), "within 14 days" and "28 days" (s 229(2)), "does not commit an offence"
(s 34), "until" and "does not prevent" (s 39), "does not apply" (ss 109(2), 232(3)), "is not an action with intent"
(s 108(3)), "may only be brought by" (ss 230(1), 260) and "nothing in this Act is to be construed as conferring"
(s 267(a)) give `JUST FALSE`. The s 113(3) defence, once proved, gives `JUST FALSE` for the orders. `NOTHING` is
answered where a grant, duty or prohibition is limited by its own wording and the facts fall outside it (ss 19, 28(c),
108, 109, 112(1), 112(3), 260A(1), 272, 273), where the text is silent (s 109 civil remedy, no fine for industrial
manslaughter by an individual), where the encoding leaves the question to the regulations (s 223 item 13), and while a
deadline has not yet passed. Date questions answer `NOTHING` where no day is due (ss 224 for the regulator's own
decision, 231(2a) once the investigation is complete, 231(3)(b) without the advice or for a Category 3 offence).

## What the Act turns out to say

1. **South Australia's prosecution-request scheme is wider than the model's.** The request may be made from 6 to 24
   months after the occurrence (the model: after 6 but within 12), or within 12 months after a coroner's report or
   inquest; industrial manslaughter is included, both in the request and in the referral to the Director of Public
   Prosecutions (s 231(1)-(3)); the regulator must update the person at least every 3 months while the investigation is
   open (s 231(2a)); the DPP must advise within 1 month (s 231(4)); and a referral extends the limitation period to 1
   month after that advice (s 232(1)(ba)). Asserted at each edge.
2. **The DPP's month has no stated start.** s 231(4) says the DPP must advise the regulator "within 1 month", without
   saying of what. Read from the referral (F15); s 232(1)(ba) then runs from the advice itself, so nothing in the
   limitation period turns on the reading.
3. **Misrepresentation has no civil remedy.** s 109 sits in Part 6, which s 267 excepts, but s 112(2) lists only
   ss 104/107 conduct and s 108; s 109 carries no note that civil proceedings may be brought, as ss 104, 107 and 108 do.
   `Does the Act give me a right to sue` answers NOTHING for s 109. Asserted.
4. **Only some listeners count.** s 106(h) protects raising a safety concern with the persons it lists (the business, an
   inspector, a permit holder, a representative, a committee member, another worker, another duty holder, anyone
   exercising powers under the Act). A worker dismissed for going to the media or a member of Parliament is not protected
   by Part 6. Asserted (JUST FALSE).
5. **Industrial manslaughter: no fine for an individual, no time limit, and only the business and its officers.** s 30A's
   penalty is 20 years' imprisonment for an individual and $18 000 000 for a body corporate; an individual faces no
   stated fine. s 232(3) takes it out of the limitation period, and, unlike the Tasmanian text, nothing bars it while
   other charges stand. A worker or other person whose grossly negligent conduct causes a death commits at most a
   Category 1 offence under this Act. Asserted.
6. **Two different tests of motive.** The offence needs the prohibited reason to be the "dominant reason" (ss 104(2),
   110); the SAET proceeding only "a substantial reason" (ss 112(4), 113(2)). A worker may win in SAET on facts that would
   not convict. Encoded separately.
7. **The criminal and civil remedies exclude each other.** After a s 112 order a criminal court cannot order
   compensation or reinstatement under s 111 for the same conduct, and the other way round (s 114(2), (3)); and a worker
   with another proceeding on foot about the same matter (an unfair dismissal or general protections claim, say) cannot
   start one under s 112 at all (s 115(a)). Asserted.
8. **s 86 excludes a representative-directed worker twice, and so from (b) as well.** Its opening words ("(otherwise
   than under a direction from a health and safety representative)") and (a)'s "unless" both take that worker out of
   the duty to notify; the opening words also take them out of (b), the duty to remain available for suitable
   alternative work, which the model text imposes on every worker who ceases work. Encoded for (a); (b) is stated in the
   question's description.
9. **s 103 takes prisoners out of all of Part 5**, so a worker in custody has neither the right to cease unsafe work nor
   access to a SAET dispute -- but keeps Part 6's protection against discriminatory conduct. Asserted for ss 84, 85, 86
   and 102B.
10. **The SAET dispute clock starts at the request for an inspector.** s 102B(1) counts the 24 hours from a party's
    request to the regulator to appoint an inspector, not from the failure of issue resolution; a dispute can reach SAET
    a day after that request, whatever the inspector has done. Asserted at 23 and 24 hours.
11. **s 34(1) is subsumed by s 34(2).** The volunteer officer of a strata or community titles corporation is already a
    volunteer who does not commit an offence for a failure to comply with a duty other than under ss 28, 29; s 34(1)
    says "to avoid doubt". Encoded through s 34(2).

## Before this is worth relying on

- Check the text against the authorised version on legislation.sa.gov.au, and that version 1.7.2025 is still current.
- Read the Acts Interpretation Act 1915 (SA) for counting periods (F1) and the Criminal Procedure Act 1921 for which
  court a prosecution goes to (s 230, out of scope).
- Encode the s 223 item 13 decisions (reg 676), Part 5 Divisions 5 and 7 (issue resolution, provisional improvement
  notices) and the further Part 2 duties if wanted; a business seat layer.
- A lawyer's view on findings 2, 3, 8 and 10 and forks F2, F4, F6, F9, F10, F14, F17; an independent test pass and a
  human gate.
