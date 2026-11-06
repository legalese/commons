# Australian Human Rights Commission Act 1986 (Cth), Part IIB -- baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

Three files: `ahrc-dates.l4` (date arithmetic with the built-in date functions, not the daydate library),
`ahrc-complaints.l4` (the rules and the 30 exported questions, each with `@export` and a `@desc` on every input) and
`ahrc-cases.l4` (the worked cases). The duties with deadlines the person meets are regulative rules (`PARTY ... MUST ...
WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE`), run by `EVALTRACE` inside questions that take only plain facts:

- s 46PH(1)(b): lodge within 24 months of the acts, or the President may terminate;
- s 46PI(2) with s 46PM: give the President the information or documents within the period the notice specifies, or
  commit an offence unless there is a reasonable excuse;
- s 46PO(2): apply to the court within 60 days after the date of issue of the termination notice, unless the court
  allows further time.

No question takes a DEONTIC or an EVENT input.

This is the first encoding of this Act. The Age Discrimination Act 2004 baseline
(`subjects/au/age-discrimination-act-2004/encodings/baseline-2026-10/`) encodes ss 3(1), 46P, 46PH(1)(b) and 46PO(2) of
this Act for age complaints only; it stays as it is. In the ordinary case the two count the 24 months and the 60 days
the same way; their handling of month ends (29 February, 31 January) was not compared.

## Edition

- **The Act:** Compilation No. 58, compilation date 18 September 2026 ("Includes amendments: Act No. 87, 2026";
  register id C2026C00416), deposited at `../../registers/source-bundle/C2004A03366.txt` (retrieved 2026-10-13).
- **s 46PSA** in that compilation is the section substituted by the Australian Human Rights Commission Amendment (Costs
  Protection) Act 2024 (No. 89, 2024; the endnotes give "rs No 89, 2024", and Schedule 1 items 1-3 and 7 commencing on
  2 October 2024). The amendment history also shows No 89, 2024 amending ss 46PH and 46PO; the compiled text has s 46PH(2A)
  (the termination notice must explain costs) and s 46PKA(2) (conciliation evidence admissible for s 46PSA).
  The amending Act itself, with its application provision, is not deposited (finding 1).
- No regulations set a number this encoding needs. Penalty unit values (Crimes Act 1914 s 4AA) are not deposited:
  penalties are given in penalty units.

## Checks

- Stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset: `l4 run ahrc-dates.l4`, `l4 run
  ahrc-complaints.l4`, `l4 run ahrc-cases.l4`.
- **170 assertions written, 170 satisfied, 0 errors, 0 warnings** in every file (2026-11-07).
- Every expected value was worked by hand from the text before the file was run. On the first run seven assertions
  failed; all seven were mistakes in the hand-worked facts (7 November 2026 had been taken as within 24 months of
  15 March 2024, which it is not). The facts were corrected to 7 November 2025, and a case asserting that 7 November
  2026 is more than 24 months on was added. No expected value was copied from the encoding's output.
- One expectation was changed in a scratch copy (1 October 2026 plus 60 days given as 1 December 2026); the run reported
  it as failing, so the runner catches a wrong expectation.

## Seat

**The person aggrieved by alleged unlawful discrimination** (`ahrc-complaints.l4`): the worker, job applicant, tenant,
customer or student who says they were discriminated against unlawfully under the Age, Disability, Racial or Sex
Discrimination Act, lodges a complaint with the Australian Human Rights Commission, takes part in the President's
inquiry and conciliation, and, if the President terminates the complaint, may apply to the Federal Court or the Federal
Circuit and Family Court of Australia (Division 2). The same person is also asked about as a class member of a
representative complaint and as a person on whose behalf a representative application is made. Questions: "Is this
unlawful discrimination?", "Can I lodge a complaint?", "Can I amend or withdraw it?", "Can it be ended, and on what
ground?", "Must I give the information, or go to the conference?", "May someone represent me there?", "Can I go to
court, and by when?", "What can the court order?", "Will the respondent pay my costs, and can I be made to pay theirs?".

The Commission, the President, the person presiding at a conference, the court and the Attorney-General get no seat:
their opinions and decisions are asked as facts. The respondent is a party the Act puts duties and liabilities on (costs
under s 46PSA, information under s 46PI); no respondent seat was written (see "Before this is worth relying on").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number. Whether an act is
  unlawful under the Age, Disability, Racial or Sex Discrimination Act is borrowed and asked as a fact (the person names
  the Act and Part); those Acts are not read here.
- **The actors the text names.** Followed: the complainant, the affected person, the class member, the person or trade
  union lodging for others, the respondent, the Commission, the President, the person presiding at a conference, the
  Federal Court, the Federal Circuit and Family Court of Australia (Division 2), the Attorney-General.
- **Judgments handed to someone else are answered conditionally.** Followed. Every "the President is satisfied", "in the
  opinion of", "the court is satisfied", "the court grants leave" and "the Attorney-General is satisfied" is an input; so
  are "reasonably arguable" (s 46P(1A)), "reasonable excuse" (s 46PM(1A)), and "significant power advantage" and
  "significant financial or other resources" (s 46PSA(6)(c)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: unlawful discrimination (from the
  Act and Part named), representative complaint (from who lodges and for whom), affected person and complainant (in the
  choices offered). Asked: disability (s 46PK(7) borrows the Disability Discrimination Act 1992), statutory authority,
  trade union.
- **One case is the text's natural unit.** Followed: one complaint, and the one court application that may follow it.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 3(1) (affected person, class member, complainant, representative application, representative complaint,
respondent, unlawful discrimination); Part IIB Division 1: ss 46P, 46PA, 46PB, 46PC(1), 46PD, 46PE(1)-(3), 46PF(1),
(1B), (3)-(5), (7), (8), (10), (11), 46PG, 46PH (all of it), 46PI(2), 46PJ(3)-(7), 46PK(2), (4)-(7), 46PKA, 46PM(1),
(1A), (3), 46PN; Division 2: ss 46PO (all of it), 46POA, 46POB(1)-(3), 46PP, 46PQ, 46PSA (all of it), 46PT, 46PU.

**Out, and why.**
- Part I other than the s 3(1) definitions used; Part II (the Commission, its functions and members), Part IIA
  (Commissioners), Part III and the Schedules: machinery and institutions.
- Part II Divisions 3 and 4 (ss 20-35: inquiries into acts or practices inconsistent with human rights, and into
  discrimination in employment under ILO Convention 111). A person may complain under them, but they end in a report to
  the Minister, not a remedy the person can enforce; they would be a separate encoding.
- s 46PC(2), (3), s 46PE(4), s 46PF(2), (6), (12), s 46PI(1), (3)-(5), s 46PJ(1), (2), s 46PK(1), (3), s 46PM(2): the
  President's and the presiding person's procedure, with nothing for the person to state or decide beyond what is
  encoded (s 46PF(6) and (10) are not enforceable in court, s 46PF(11)).
- s 46POB(4)-(7) (extending the opt-out date, the hearing date, settlement approval and distribution): the court's
  management of a representative proceeding; the opt-out question treats an extended date as the date.
- s 46PR (court not bound by technicalities), s 46PS (the President's report to the court), s 46PV (amicus curiae):
  nothing for the person to ask.
- Part IIC (ss 46PW-46PY, referral of discriminatory industrial instruments and determinations): a different complaint,
  ending in a referral, not a remedy for the person.
- s 46PZ (transfers from the Inspector-General of Intelligence and Security): the transferred complaint is then treated
  as lodged under s 46P, which is encoded.
- The application provision of the 2024 costs amendment (in the amending Act, not deposited) and the courts' general
  costs powers (Federal Court of Australia Act 1976 s 43, Federal Circuit and Family Court of Australia Act 2021 s 214,
  cited in the notes to s 46PO(4)): not deposited.
- No requirement-ledger entry exists for this Act in `subjects/au/requirements.jsonl`, and none was raised: no scenario
  life has reached it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 46P(1A) "must be reasonably arguable", s 46P(1B) "must set out ... the details", s 46PB(2) "must describe ...
  specify ..." (a bare "must" not met) -- `ss 46P, 46PB -- may I lodge this complaint` -- the text's no ("no" for (1A),
  "not as it stands" for (1B) and s 46PB(2)) -- the complaint is still lodged, and the President may or must terminate
  it (for example under s 46PH(1B)(a), lacking in substance).
- **F2** s 46PH(1)(b) "more than 24 months after", s 46PF(10)(b) "within 12 months after" -- `plus calendar months`
  (ahrc-dates.l4), `s 46PH(1)(b) -- the last day to lodge without the lateness ground`, `s 46PF(10) -- the 12-month
  target for finishing my complaint` -- the day 24 (or 12) calendar months on is the last day, and a day the later month
  lacks becomes that month's last day (29 February 2024 plus 24 months is 28 February 2026) -- the period ends the day
  before, or rolls into the next month (1 March).
- **F3** "unless" met: s 46PF(7)(a) ("unless the President is satisfied that notification would be likely to prejudice
  the safety of a person") and s 46PQ(1)(c) ("unless the court is of the opinion that it is inappropriate") -- `s 46PF(7)
  -- will the respondent be told of my complaint`, `s 46PQ -- may they represent me in court` -- no (the duty or the
  permission does not reach the case) -- NOTHING (the text says only what happens when the "unless" is not met).
- **F4** s 46PJ(4) "must specify ... a time ... not ... less than 14 days after the notice is given; and must set out the
  effect of subsection (5)" -- `s 46PJ -- must I attend the conference` -- a notice that fails (4) is answered
  NOTHING-kind (the Act does not say whether it still binds) -- it is not a notice under s 46PJ(3), so no offence (the
  text's no).
- **F5** s 46PH(1)(b) "after the alleged acts, omissions or practices took place", for acts over a period -- the 24-month
  questions -- the person gives the last day of the acts -- the first day, or each act counted separately.
- **F6** s 46PH grounds -- `s 46PH -- can my complaint be terminated` -- one ground is reported, the mandatory grounds
  ((1B)(a), (1B)(b), (1C)) first and then (1)(a)-(h) in the text's order -- all grounds reported together. The ground
  the President actually uses decides leave (s 46PO(3A)) and is asked separately in the court question.
- **F7** s 46PH(1) "may terminate a complaint on any of the following grounds" (no "only") -- the same function -- with
  no ground made out, NOTHING-kind, pointing to s 46PF(1)(b) -- the text's no.
- **F8** s 46PSA(1) "This section applies to proceedings ... that relate to an application ... under section 46PO" --
  both costs questions -- outside it, NOTHING-kind (a scope limit with no "only": ruling (c) of 2026-11-05) -- the
  text's no.
- **F9** s 46PI(2) "within a reasonable period specified in the notice" with s 46PM(1) "refuse or fail ... when so
  required" -- `ss 46PI, 46PM -- must I give the information` -- days are counted from service (day 0), the last day of
  the period is in time, and giving the information after the period without reasonable excuse is still an offence --
  late compliance curing the failure.
- **F10** s 46PO(2) "within 60 days after the date of issue of the notice" -- `s 46PO(2) -- the last day to apply to the
  court`, `s 46PO(2) -- is my court application in time` -- counted from the date of issue (not receipt), the 60th day
  after being the last day (1 October 2026 gives 30 November 2026) -- the day before, or counted from receipt.
- **F11** s 46PC(1) "by notice in writing" and s 46POB(3) "by written notice", without the notice -- the withdrawal and
  opt-out questions -- NOTHING-kind ("not yet") -- the text's no.
- **F12** s 46PSA(6)(b) "caused the other party to incur the costs" -- `s 46PSA -- can I be made to pay their costs` --
  only the costs the unreasonable act or omission caused -- all the other party's costs, once some were so caused.

Sites decided without a fork line: the "means" definition of unlawful discrimination (s 3(1)) and its "other than"
exclusions answer the text's no; so do the flat negatives and "only if" or "unless" bars of ss 46P(3), 46PB(1), 46PF(4),
46PG(2), 46PK(4)(a), 46PKA(1), 46PO(3), (3A), 46POA(1), 46POB(1), 46PP(3), 46PSA(5) and (7); the "if" conditions of ss
46P(4), 46PE(1), (2), 46PF(7), 46PO(1), 46PSA(2) and 46PU(2); "on request" (s 46PH(3)) and "when so required" (s 46PM(1))
as "where" conditions; and the periods the text fixes in s 46PC(1) ("at any time before the President terminates"),
s 46PH(4) ("but not after an application is made"), s 46POB(3)(a) ("before the date so fixed") and s 46PP(1) ("at any
time after a complaint is lodged"). s 46PN outside its own wording answers NOTHING. The s 46PO(4) question answers an
empty list when the court is not satisfied of unlawful discrimination (its "if" fails).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags in the s 46P, s 46PA, s 46PC, s 46PH, s 46PJ, s 46PKA, s 46PO, s 46POB, consent
and s 46PSA questions (F4, F7, F8, F11, the person s 46P(2) or s 46PO(2A) does not list, the Part IVA proceeding, and
amending without leave), and a NOTHING answer in the s 46PN question. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (s 46PH(1)(b)'s 24 months, s 46PI(2)'s period in the notice, s 46PO(2)'s 60 days) are
regulative rules (`MUST ... WITHIN`, `LEST BREACH`), run by EVALTRACE inside the questions; outside each period the
answer is the consequence the text gives (the President may terminate; an offence; out of time unless the court allows
further time).

## What the Act turns out to say

1. **The 2024 costs rule's reach in time is not in the deposited text.** s 46PSA was substituted by the Costs Protection
   Act 2024 (in force 2 October 2024 by the endnotes); which proceedings it governs (by the date of the complaint, the
   termination, the application or the hearing) is set by that Act's application provision, which is not deposited.
   The encoding answers every s 46PO proceeding by the compiled s 46PSA. A proceeding begun earlier may be under the
   earlier s 46PSA.
2. **The costs rule is asymmetric by design.** A successful applicant gets a mandatory order against each respondent
   it succeeds against (s 46PSA(2): "must"), on an indemnity basis if the court so orders (s 46PSA(3)); an unsuccessful
   applicant "must not" be ordered to pay costs (s 46PSA(5)) except in the three cases of s 46PSA(6). Asserted.
3. **Partial success.** s 46PSA(2) turns on success "on one or more grounds" and orders "the applicant's costs" without
   apportioning between grounds won and lost; only the applicant's own unreasonable act or omission (s 46PSA(4)) lets
   the court leave costs out. The encoding gives the full order (subject to (4)). Asserted.
4. **s 46PSA(6)(c) is a double negative on undefined terms.** The applicant may be ordered to pay a successful
   respondent's costs where the respondent "does not have a significant power advantage" and "does not have
   significant financial or other resources relative to the applicant". "Significant" is undefined; both are asked as
   facts, and either one present protects the applicant. Asserted (three cases).
5. **The notes to s 46PO(4) were not updated for s 46PSA.** Notes 1 and 2 still say the courts "may award costs ... in
   certain circumstances" under Federal Court of Australia Act 1976 s 43 and Federal Circuit and Family Court of
   Australia Act 2021 s 214, while s 46PSA now says when costs must and must not be ordered. Notes are not operative; a
   reader of s 46PO alone would miss s 46PSA. s 46PH(2A) makes the termination notice explain that the courts "can
   award costs ... in certain circumstances", which says nothing of the protection.
6. **Withdrawing closes doors that termination opens.** A withdrawn complaint (s 46PG) is not a terminated one, so no
   application to the court under s 46PO(1) follows it, and no interim injunction under s 46PP may be granted after it
   (s 46PP(3)). A complainant who wants to go to court needs a termination, not a withdrawal. Asserted.
7. **Leave is the rule, not the exception.** Only a complaint terminated for public importance (s 46PH(1)(h)) or for no
   reasonable prospect of conciliation (s 46PH(1B)(b)) goes to court without leave (s 46PO(3A)); a complaint terminated
   without inquiry (s 46PF(1)(b)), on request under s 46PE, or on any other s 46PH ground needs the court's leave.
   Asserted.
8. **Consent runs opposite ways at the two stages.** A representative complaint to the Commission needs no consent from
   the class (s 46PB(4)); a representative application to the court needs each person's written consent (s 46POA(1)).
   A person in a representative application who did not make it cannot be ordered to pay costs (s 46PSA(7)). Asserted.
9. **Gaps in the numbering are repeals, not errors.** s 46PF(7) runs (a), (b), (d) and s 46PF runs (8), (10): paragraph
   (7)(c) and subsection (9) were repealed. s 3(1) "unlawful discrimination" includes offences under ADA Part 5
   Division 2 and DDA Part 2 Division 4 but expressly not ADA ss 51, 52 or DDA s 42 (asserted). The 24 months in
   s 46PH(1)(b) run from when the acts "took place", which for a continuing practice the text does not fix (F5).

## Before this is worth relying on

- A lawyer's review of the fork register (F1-F12), above all F1 (a complaint that is not reasonably arguable or lacks
  details), F4 (a defective conference notice) and F12 (which costs (6)(b) reaches).
- Depositing the Costs Protection Act 2024 and encoding its application provision, so that the costs questions can ask
  when the proceeding began.
- Depositing Federal Court of Australia Act 1976 Part IVA and s 43 and the Federal Circuit and Family Court of Australia
  Act 2021 s 214, for representative proceedings and costs outside s 46PSA.
- Linking the questions to the Age, Disability, Racial and Sex Discrimination Act encodings, which answer whether an act
  is unlawful (asked here as a fact), in a register, since the stable `l4` cannot IMPORT across subjects.
- A respondent seat (the employer or service provider complained of): costs (s 46PSA(2), (6)), information
  (ss 46PI, 46PM), the conference (s 46PJ), with mirror cases against this seat.
- Part II Divisions 3 and 4 (human rights and ILO 111 complaints), as a separate encoding.
- An independent test pass.
