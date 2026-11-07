# Work Health and Safety Act 2012 (Tas) -- baseline encoding, the worker

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`twhs-dates.l4`,
built-in date functions only, no daydate), the rules in `twhs-rules.l4`, and the worker's questions in `twhs-seat.l4`,
which imports the rules and restates none. The cases are in `twhs-cases.l4`. The shape follows the Limitation Act 1974
(Tas) baseline in `subjects/au/tas/limitation-act-1974/encodings/baseline-2026-11/`.

## Edition

- **Act:** Work Health and Safety Act 2012 (Tas), No. 1 of 2012, consolidated version published 2025-09-16 and current at
  point in time 2026-11-06, as deposited at `../../registers/source-bundle/act-2012-001.txt` (text sha256
  20762d69...6a41a1e), retrieved from legislation.tas.gov.au on 6 November 2026. It includes the industrial manslaughter
  amendments of No. 15 of 2024 (ss 29A-29D, s 231(1), (1A), s 232(3), (4); applied 2 October 2024).
- **Numbers set elsewhere:** the Act states its own fines in dollars and its own periods. The Work Health and Safety
  Regulations, which add to or take from "serious injury or illness" (s 36) and "dangerous incident" (s 37), name the
  "prescribed purposes" of s 88, the "prescribed class" of worker (s 7(1)(i)) and the initial training of s 85(6), are
  **not deposited**: where they could change an answer the answer is `NOTHING` or the matter is asked as a fact (F6).
- **Borrowed terms asked as facts:** "business or undertaking", "employee", "volunteer", "officer" (defined by reference
  to the Corporations Act 2001 (Cth)), "body corporate", "commercial arrangement", "detriment", "hazard", "Criminal Code".

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
a deliberately wrong assertion was run once in a scratch file (deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `twhs-dates.l4` | 0 | 0 | 0 | 0 |
| `twhs-rules.l4` | 0 | 0 | 0 | 0 |
| `twhs-seat.l4` | 0 | 0 | 0 | 0 |
| `twhs-cases.l4` | 0 | 0 | 210 | 210 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the
s 113(1) last day and the day after (10 / 11 March 2026; 28 February / 1 March 2025 from 29 February 2024); the 48th and
49th hour of s 38(4)(b), given and not given; the s 231(1) window at the 6-month day, the day after, the 12-month day and
the day after, and from 31 August (6 months is 28 February); the s 231(2) last day and the day after, answered and not;
the s 232 periods with and without a coroner's report and a breached undertaking, either one later and earlier than the
2 years; every fine and prison term in ss 29C, 31-33, 38, 39, 104, 107-109 and 273 for each kind of offender.

## Seat

**The worker** (`twhs-seat.l4`): the individual (or prospective worker) who is hurt, put at risk, stops unsafe work, or
is dismissed or otherwise treated badly for raising safety, and who brings or presses a claim about it -- or, where a
worker has died, the family member asking on the worker's behalf. "Am I a worker?", "Does the business owe me the duty?",
"Must I follow this instruction?", "Is my injury notifiable, and was it notified?", "May I stop this work, and is my job
safe if I do?", "Can I take them to the Magistrates Court for sacking me over a safety complaint, and by when; what can
the court order?", "What offence did they commit and what can they get?", "Can I ask for a prosecution, and by when must
the regulator answer?", "By when can they be prosecuted?", "Does the Act let me sue?", "Is this contract term void?",
"Can they charge me for safety gear?". No seat for the business, the regulator, inspectors, the Director of Public
Prosecutions or the courts: their judgments and findings are asked as facts. A business seat (`twhs-seat-business.l4`)
would be a natural further layer.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, except that the regulations are not deposited
  (see Edition, F6).
- **The actors the text names.** Followed: the worker and prospective worker, the person conducting a business or
  undertaking, the officer, the health and safety representative, the regulator, the inspector, the Director of Public
  Prosecutions, the Magistrates Court, the State.
- **Judgments answered conditionally.** Followed: "reasonable concern" (ss 84, 85), "reasonably considers" (s 231),
  "reasonable instruction" and "reasonably able" (s 28), "without reasonable excuse", "reckless", "negligent" (ss 29B,
  29C, 31), "unreasonably failed" (s 88), "just" (s 184), "reasonable in the circumstances" (s 113(3)) and what a court
  finds proved (ss 110, 113) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: worker (s 7), notifiable incident, serious injury
  or illness, dangerous incident (ss 35-37), cease work (s 83), discriminatory conduct and prohibited reason (ss 105,
  106), negligent (s 29B), eligible person (s 112(6)) are worked out from facts.
- **One case.** One incident, one piece of conduct, one offence.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5(1), (7) (so far as they decide who is a worker); s 7; s 19(1), (2); s 28(c); Part 2 Division 4A (ss 29B,
29C, 29D) and Division 5 (ss 30-34); Part 3 (ss 35-39); Part 5 Division 6 (ss 83-88); Part 6 (ss 104-115); s 184;
ss 231, 232; s 267 (with s 260); ss 272, 273. s 38(2)-(6) (how notice is given) and s 86(b), s 87 (alternative work) are
in the descriptions of the questions they bear on.

**Regulative rules:** three, each run by EVALTRACE inside a question that takes only plain facts: the s 113(1) time bar
(`PARTY the applicant MUST commence the proceeding WITHIN` the days to the first anniversary, `LEST BREACH ... BECAUSE`),
inside `Can I apply to the Magistrates Court` and `Can the court make this order for me`; the s 38(4)(b) written notice
(`PARTY the business MUST give the written notice of the incident WITHIN 48` hours), inside `Was the written notice
given in time`; the s 231(2) advice (`PARTY the regulator MUST advise the requester in writing WITHIN` the days to the
3-month day), inside `Did the regulator advise me in time`.

**Exported questions (34):** `Am I a worker`; `Does the business owe me the primary duty of care`; `Must I follow this
instruction`; `Is my injury a serious injury or illness`; `Was it a dangerous incident`; `Must the business notify the
regulator`; `Was the written notice given in time`; `Until when must the record of my incident be kept`; `Does the Act
forbid disturbing the incident site`; `May I cease or refuse this work`; `Could the representative direct me to cease
work`; `Must I tell the business I ceased work`; `Is the continuity of my engagement unaffected`; `Was it discriminatory
conduct for a prohibited reason`; `Can I apply to the Magistrates Court`; `By when must I start my civil proceeding`;
`Can the court make this order for me`; `Can the criminal court order compensation or reinstatement for me`; `Is the
discrimination offence made out`; `Was the representation to me prohibited`; `What is the most they can be fined for
this contravention`; `Which offence do these facts make out`; `What is the maximum fine for the offence`; `What is the
longest prison term for the offence`; `Can I ask for a prosecution`; `By when must the regulator advise me`; `Did the
regulator advise me in time`; `By when must my matter be referred to the DPP`; `By when can they be prosecuted`; `Can
they still be prosecuted on this day`; `Does the Act give me a right to sue`; `Is this term of my contract void`; `Can
the business charge me for this`; `Can the court order the State to compensate me`.

**Out, and why:**
- ss 1-4, 6, 8-12 and the Schedules: commencement, definitions used only elsewhere, supply, application, the Crown, the
  regulator and the WorkCover Tasmania Board, regulation-making subjects. s 8 (workplace) is glossed in a `@desc`.
- Part 2 Division 1 (ss 13-18): principles and "reasonably practicable"; whether a duty was met is a judgment, entered as
  the fact "the duty was not complied with". s 19(3)-(5) and ss 20-26 (the further duties of designers, manufacturers,
  importers, suppliers, installers, and of those who manage workplaces or plant), s 27 (officers' due diligence), s 28(a),
  (b), (d) and s 29: duties whose content is a judgment; they enter the offence question as "a health and safety duty
  was owed". Officers are folded into the "individual conducting the business, or an officer of it" kind (s 27(2));
  s 27(3)'s penalty for an officer's breach of a non-Part 2 duty is not encoded.
- Part 4 (authorisations), Part 5 Divisions 1-5, 7 and 8 (consultation, health and safety representatives and their
  election, committees, issue resolution, provisional improvement notices): workplace representation machinery rather
  than claims. s 89 (request for an inspector) gives no time or entitlement to encode.
- Part 7 (entry by WHS entry permit holders), Parts 8-11 (regulator, inspectors' powers, notices, enforceable
  undertakings) apart from s 184, Part 12 (review of decisions): powers of officials and unions; not the claimant's
  questions in this focus. Part 12 could be a later layer (a worker may seek review of some decisions).
- Part 13 apart from ss 231, 232 and 267: sentencing orders, infringement notices, bodies corporate, the Crown, public
  authorities, WHS civil penalty proceedings (brought only by the regulator or an inspector, s 260, which is cited).
- Part 14 apart from ss 272, 273: false information, privilege, immunity, confidentiality, codes of practice,
  regulations, administration.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "not more than 1 year after the date" (s 113(1)), "within 2 years after" (s 232(1)(a)), "for at least 5 years
  from the day" (s 38(7)), "within 3 months after" (s 231(2)), "within 1 month of" (s 231(3)(b)), "6 months after"
  (s 232(1)(c)) -- `the anniversary`, `the date ... months after` -- the day itself is excluded, so the last day is the
  same day of the month a year or months later; a day the later month lacks falls on its last day (29 February + 1 year
  = 28 February; 31 August + 6 months = 28 February) -- the Acts Interpretation Act 1931 (Tas) rule, not deposited, may
  differ at month ends.
- **F2** s 231(1)(b) "after 6 months but not later than 12 months after that occurrence" -- `s 231(1) -- I may request a
  prosecution` -- the request may be made from the day after the 6-month day to the 12-month day inclusive -- the 6-month
  day itself counted as "after 6 months".
- **F3** s 7(1) -- `s 7 -- I am a worker` -- JUST FALSE where no limb holds (an "if" definition) -- NOTHING, because a
  "person of a prescribed class" (s 7(1)(i)) may be added by regulations not deposited.
- **F4** s 19(1), (2) -- `s 19 -- the business owes me the primary duty of care` -- a worker engaged or directed by the
  business but not at work in it, and not at risk under (2): JUST FALSE (the "while"); neither engaged, directed nor at
  risk: NOTHING (a duty limited in its own wording) -- JUST FALSE for both.
- **F5** s 28(c) -- `s 28(c) -- I must comply with the instruction` -- an instruction that is not reasonable, not given
  to allow the business to comply, or beyond what the worker is reasonably able to do: NOTHING -- JUST FALSE, reading
  the qualifications as conditions.
- **F6** ss 7(1)(i), 36, 37, 85(6), 88 (regulations not deposited) -- `s 36 -- it is a serious injury or illness`,
  `s 37 -- it is a dangerous incident` -- a listed head: JUST TRUE (though the regulations may exclude "an injury or
  illness of a prescribed kind" or "an incident of a prescribed kind"); anything else: NOTHING; s 85(6) training and
  s 88 "prescribed purposes" asked or described as facts -- a listed head answered NOTHING until the regulations are
  deposited.
- **F7** duties and powers whose "if" is unmet -- `s 38(1) -- the business must notify the regulator` (not arising out of
  this business: JUST FALSE), `s 38(4)(b) -- the written notice was given in time` (no requirement: NOTHING),
  `s 86(a) -- I must notify the business that I ceased work` and `s 88 -- ...` (not ceased under the Division: NOTHING),
  `s 111 -- the criminal court may make the order for me` (no conviction: NOTHING) -- the opposite answer at each site.
- **F8** s 104(2) with s 110 -- `s 104 -- an offence of discriminatory conduct is made out` -- no evidence that the
  conduct was for the reason: NOTHING (the presumption is not engaged; dominance is for the court) -- JUST FALSE.
- **F9** s 112(1), (6) -- `s 112 -- I may apply to the Magistrates Court` -- a person neither affected nor authorised:
  NOTHING (a grant limited in its own wording) -- JUST FALSE, reading (6) as a closed list.
- **F10** s 112(3)(b), (c) -- `s 112(3) -- the court may make the order for me` -- compensation for s 108 coercion, and
  reinstatement outside (2)(a) or for a worker who was not an employee: NOTHING, since (d) "any other order that the court
  considers appropriate" may reach them -- JUST FALSE, reading (b) and (c) as the only routes.
- **F11** s 232(1)(c) -- `s 232 -- the time for prosecution` -- the 6 months run from the latest of the breach, its
  coming to the regulator's notice and the withdrawal, entered as one day -- each trigger its own period (the same
  result under "the latest of the following periods").
- **F12** Part 2 offences -- `the most serious offence made out` -- a body corporate is taken to be the person conducting
  the business (for industrial manslaughter); the most serious offence the facts make out is answered, Category 1 before
  Category 2 though s 31 does not need a failure to comply -- the offence charged.
- **F13** s 39(1) "so far as is reasonably practicable" -- `s 39 -- the site must not be disturbed by the action` -- not
  asked: the duty is answered as if practicable -- the judgment as an input.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" and "if" definitions of ss 7, 29B, 35, 36, 37, 105 and 106, the "while" of ss 19(1) and 28,
the "if" of ss 84, 85(1), 88 and 184(1), "unless" in ss 85(2), (6) and 86(a), "only if" in ss 104(2), 112(4) and 184(3),
"cannot" in ss 114 and 115, "must be commenced not more than 1 year after" (s 113(1)), "within 48 hours" (s 38(4)(b)),
"within 3 months" (s 231(2)), the s 231(1) window, "does not commit an offence" (s 34), "until" and "does not prevent"
(s 39), "does not apply" (s 109(2)), "is not an action with intent" (s 108(3)), "may only be brought by" (s 260) and
"nothing in this Act is to be construed as conferring" (s 267(a)) give `JUST FALSE`. The s 113(3) defence, once proved,
gives `JUST FALSE` for the orders. `NOTHING` is answered where the regulations (not deposited) decide (F6), where a
grant, duty or prohibition is limited by its own wording and the facts fall outside it (ss 19, 28(c), 108, 109, 112(1),
112(3), 272, 273), where the text is silent (s 109 civil remedy, s 231(3) for industrial manslaughter, no fine for
industrial manslaughter by an individual), and while a deadline has not yet passed.

## What the Act turns out to say

1. **The 2024 amendments left s 231(3) behind.** s 231(1) now lets a person ask for a prosecution of an industrial
   manslaughter offence, but s 231(3) still requires a referral to the Director of Public Prosecutions only where the
   regulator declines a "Category 1 or Category 2 offence". A family who asks about a workplace death and is told there
   will be no industrial manslaughter prosecution has no s 231(3) referral (the DPP may still prosecute, s 230(4)).
   Asserted (`By when must my matter be referred to the DPP` answers NOTHING for industrial manslaughter).
2. **Two different tests of motive.** The offence needs the prohibited reason to be the "dominant reason" (ss 104(2),
   110); the civil proceeding only "a substantial reason" (ss 112(4), 113(2)). Both are presumed once raised, with a legal
   burden on the other side. A worker may win the civil case on facts that would not convict. Encoded separately.
3. **Misrepresentation has no civil remedy.** s 109 sits in Part 6, which s 267 excepts, and s 108 carries a note that
   civil proceedings may be brought; s 109 carries none, and s 112(2) lists only ss 104/107 conduct and s 108. Encoded:
   `Does the Act give me a right to sue` answers NOTHING for s 109. Asserted.
4. **The criminal and civil remedies exclude each other.** After a s 112 order a criminal court cannot order
   compensation or reinstatement under s 111 for the same conduct, and the other way round (s 114(2), (3)); and a worker
   with another proceeding on foot about the same matter (an unfair dismissal or general protections claim, say) cannot
   start one under s 112 at all (s 115(a)). Asserted.
5. **Only some listeners count.** s 106(h) protects raising a safety concern with the persons it lists (the business, an
   inspector, a permit holder, a representative, a committee member, another worker, another duty holder, anyone
   exercising powers under the Act). A worker dismissed for going to the media or a member of Parliament is not protected
   by Part 6. Asserted (JUST FALSE).
6. **No fine for industrial manslaughter by an individual.** s 29C's penalty is imprisonment up to 21 years for an
   individual and a fine up to $18 000 000 for a body corporate; an individual faces no stated fine (the Sentencing Act
   1997 (Tas), not deposited, may allow one). The Category 1 penalty for an individual is a fine "or" imprisonment "or
   both". Asserted.
7. **Industrial manslaughter has no time limit but can be blocked.** s 232(3) takes it out of s 232, so no limitation
   period applies; s 232(4) bars it while Criminal Code charges for the same conduct stand. Asserted.
8. **"After 6 months but not later than 12 months after"** (s 231(1)(b)) attaches the window to "no prosecution has been
   brought", not to the request; read as a window for the request (F2). Asserted at both edges.
9. **Compensation for coercion is not named.** s 112(3)(b) gives compensation only for (2)(a) and (b) conduct; for s 108
   coercion only (a) an injunction and (d) "any other order" remain (F10). Asserted as NOTHING.
10. **s 88's protection is "for prescribed purposes"**, which the Act does not name; the regulations are not deposited.
    The protection is encoded as stated and the purposes left to them.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- Deposit the Work Health and Safety Regulations (Tas) and revisit ss 7(1)(i), 36, 37, 85(6) and 88 (F6), and the Acts
  Interpretation Act 1931 (Tas) for counting periods (F1).
- Encode Part 12 (review of decisions) and the further Part 2 duties if wanted; a business seat layer.
- A lawyer's view on findings 1, 3, 5 and 8 and forks F2, F4, F9, F10; an independent test pass and a human gate.
