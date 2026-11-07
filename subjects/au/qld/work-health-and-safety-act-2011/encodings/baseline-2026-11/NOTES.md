# Work Health and Safety Act 2011 (Qld) -- baseline encoding, the worker

UNOFFICIAL. Based on content from the Queensland Legislation website at 6 November 2026; (c) The State of Queensland,
licensed under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`qwhs-dates.l4`,
built-in date functions only, no daydate), the rules in `qwhs-rules.l4`, and the worker's questions in `qwhs-seat.l4`,
which imports the rules and restates none. The cases are in `qwhs-cases.l4`. The shape follows the Limitation of Actions
Act 1974 (Qld) baseline.

The focus was the provisions a person bringing or answering a claim meets. The Work Health and Safety Act is not a
compensation Act: it gives no civil right of action for a breach of its duties (s 267), and workplace injury
compensation is under the Workers' Compensation and Rehabilitation Act 2003. What a claimant meets here is: whether the
injury was a "serious injury or illness" and the incident notifiable (evidence that must be reported, kept and left
undisturbed); the right to stop unsafe work and its protection; the one civil claim the Act gives (Part 6,
discriminatory or coercive conduct, to the Industrial Relations Commission) with its time limit, presumption, defence,
orders and bars; the orders a criminal court can make for the person discriminated against; the victim's or family's
right to ask for a prosecution and the time to bring one; the maximum penalties; review of inspectors' decisions; and
the general rules on civil liability, contracting out and levies. Part 6 is encoded whole.

## Edition

- **Act:** Work Health and Safety Act 2011 (Qld), Act No. 18 of 2011, the version in force from 3 August 2026 (current on
  6 November 2026), as deposited at `../../registers/source-bundle/act-2011-018.txt` (text sha256 43496be6...1db40add),
  converted from the Queensland Legislation HTML view, retrieved 6 November 2026.
- **Numbers set elsewhere, not deposited:** the Work Health and Safety Regulation 2011 (prescribed serious injuries and
  exclusions, s 36; prescribed dangerous incidents and exclusions, s 37; the "prescribed purposes" of continuity of
  engagement, s 88; regulation-prescribed reviewable decisions, schedule 2A item 13; regulation exclusions from s 5).
  Each is asked as a fact, or the answer says the regulation decides. The value of a penalty unit (Penalties and
  Sentences Act 1992 and its regulation) is not deposited, so penalties are given in penalty units.
- **Borrowed terms asked as facts:** "business or undertaking"; "hazard"; "suitable entity" (s 112(6)(b)); "employee";
  "commercial arrangement"; "corresponding WHS law"; whether a coronial report showed an offence.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two
deliberately wrong assertions were run once in a scratch file (deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`. Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `qwhs-dates.l4` | 0 | 0 | 0 | 0 |
| `qwhs-rules.l4` | 0 | 0 | 0 | 0 |
| `qwhs-seat.l4` | 0 | 0 | 0 | 0 |
| `qwhs-cases.l4` | 0 | 0 | 186 | 186 |

Every expected value was worked by hand from the text, with the edges: every exported question at least once, most
several times; the last day and the day after for the s 113 year (10 / 11 March 2026), the s 231 window (14 July 2025
closed, 15 July 2025 and 15 July 2026 open, 16 July 2026 closed), the s 231(2) answer (30 November / 1 December 2025),
internal review (15 / 16 March 2026) and external review (31 March / 1 April 2026); month counts into shorter months (31
August plus 6 months, 30 November plus 3 months, 31 January plus 1 month); 29 February plus 1 and 5 years; the lesser
of a 7-day compliance period and 14 days; the s 232 "latest of" with the coronial year ending before and after the
2-year period; the fresh-evidence rule for category 1 and not category 2; each penalty tier; the volunteer exceptions.

## Seat

**The worker** (`qwhs-seat.l4`): the worker or prospective worker to whom the Act is applied when hurt or put at risk at
work, when stopping unsafe work, when treated badly for raising safety, when seeking a prosecution, or when affected by
an inspector's decision. "Am I a worker?", "Was my injury a serious injury?", "Must the business notify the regulator?",
"May I stop this work?", "Can I apply to the commission, by when, and for what orders?", "Can I ask for a prosecution
on this day, and by when must I be answered?", "Can I have this decision reviewed, and by when?". The s 231 questions
serve equally the family of a worker who died ("a person"). No seat for the business, its officers, the regulator, an
inspector, the WHS prosecutor, the DPP, the commission or a court: their duties are encoded as what the worker is owed
and by when; their judgments are inputs.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, except that the regulation is not deposited:
  its inclusions and exclusions are asked as facts (see Edition).
- **The actors the text names.** Followed: the person conducting a business or undertaking, the worker, the health and
  safety representative, the inspector, the regulator, the WHS prosecutor, the director of public prosecutions, the
  commission, the court, the internal reviewer, the eligible person.
- **Judgments answered conditionally.** Followed: "reasonable concern" (s 84), "reasonably considers" (s 231), "suitable"
  and "safe and appropriate" (ss 87, 88), "unreasonably failed" (s 88), "substantial reason" and "reasonable in the
  circumstances" (s 113), "just" (s 184), "fresh evidence" (s 232(2)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: worker (s 7), notifiable incident (s 35), serious
  injury or illness (s 36), dangerous incident (s 37), discriminatory conduct (s 105), prohibited reason (s 106), eligible
  person (s 112(6), schedule 2A).
- **One case.** One worker, one incident or one course of conduct, one decision.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5(1), (4), (6), (7), (8); s 7; ss 31, 32, 33, 34, 34B(1), 34C, 34D (maximum penalties); ss 35-39 (Part 3, whole);
ss 83, 84, 86, 87, 88 (s 85 and s 89 in the descriptions); **Part 6, ss 104-115 (whole)**; s 184; ss 223, 224, 226,
228, 229, 229B (schedule 2A items 4-13); ss 231, 232; s 267; s 272; s 273.

**Regulative rules:** two. The time limits the worker must meet (s 113(1) application to the commission; s 224(1)
internal review; s 229B(2) external review) as `PARTY the applicant MUST ... WITHIN` the days to the last day, `LEST
BREACH ... BECAUSE`; and the WHS prosecutor's duty to answer a request within 3 months (s 231(2)) as `PARTY the WHS
prosecutor MUST advise the applicant in writing WITHIN ...`. Each is run by EVALTRACE inside an "on this day" question
that takes only plain dates.

**Exported questions (39):** Am I a worker under the Act; Was my injury or illness a serious injury or illness; Was what
happened a dangerous incident; Is what happened a notifiable incident; Must the business notify the regulator of my
incident; Until when must the business keep the record of my incident; Does the duty to leave the site undisturbed stop
this action; May I stop or refuse this unsafe work; Must I tell the business that I have stopped work; Must I stay
available for suitable alternative work; Can the business direct me to other work; Is my continuity of engagement
protected; Was it discriminatory conduct for a prohibited reason; Was it prohibited coercion or inducement; Was it a
prohibited misrepresentation; Can I apply to the commission for orders; By when must I apply to the commission; Can I
still apply to the commission on this day; Can the commission find a prohibited reason; Do they have the s 113(3)
defence; What orders can the commission make for me; What can the court order for me on a conviction; What is the most
the person responsible can face; Can I ask for a prosecution on this day; By when must the WHS prosecutor answer me; Was
the WHS prosecutor's answer in time; By when must my matter be referred to the DPP; By when must the DPP advise on my
matter; Until when can the person responsible be prosecuted; Can I apply for review of this decision; What is my first
review step and by when; Is my review application in time on this day; By when must I apply to the commission for
external review; When is my internal review decision taken to be confirmed; Does my internal review application stay
the decision; Does the Act give me a right to sue; Is this term of my contract void; Can the business charge me for
this; Can I get compensation for an inspector's entry.

**Out, and why:**
- Part 1 ss 1-4, 6, 8-12 and schedule 1: title, commencement, objects, supply, application to other Acts (machinery).
- Part 2 Divisions 1-4 (ss 13-29, the primary duty of care and the further duties): the standards are enforced by
  prosecution, not by the worker, and s 267 gives no civil right of action for them; the worker meets them through the
  category offences (in, as penalties) and through the general law of negligence (another Act's encoding). s 33A, s 34(2),
  (3) (unincorporated associations), s 34A definitions and s 34E (alternative verdicts): for the court.
- Part 4 (authorisations), Part 5 Divisions 1AA-5, 7, 7A, 8 (consultation, representatives, committees, issue resolution,
  provisional improvement notices, WHS disputes), Part 5A (WHS officers): workplace representation machinery, not a
  claim; a worker affected by a provisional improvement notice decision reaches it through review (schedule 2A item 4).
  s 85 (a representative's direction) is encoded only as a way the worker ceased work.
- Part 7 (entry permits), and the s 260(4) civil penalty applications an affected person may bring for ss 126, 144(1),
  145-147(1): entry-permit holders' conduct, rarely a worker's claim. s 261 (2 years) noted for a later layer.
- Parts 8-10 (the regulator, inspectors' powers, notices, remedial action, injunctions) except s 184: powers of officials;
  the worker meets them through review (in).
- Part 11 (enforceable undertakings): only as a date in s 232(1)(c).
- Part 12 ss 225, 227, 229A, 229C-229F: who reviews, reasons, the commission's procedure, costs and appeals (machinery
  for the commission); s 229(2) QCAT reviews (the QCAT Act, not deposited).
- Part 13 Division 1 ss 230, 233, 233A (who prosecutes, charging); Divisions 2-6 (sentencing orders other than s 111,
  bodies corporate, the Crown, public authorities): for the court and prosecutor. Division 7 (civil penalties) except as
  noted.
- Part 14 apart from ss 272, 273 (false information, privilege, immunity, confidentiality, insurance against penalties,
  codes of practice, regulation-making): machinery, or duties owed to the regulator.
- Parts 15-16, schedules 2-3: repeals, transitional provisions, the regulator's boards and committees, regulation powers.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "N months after/since" (ss 231(1B), (2), (3)(b), (4), 232(1)(c)), "N years after/from" (ss 38(7), 113(1),
  232(1)(a), (b)), "within N days after the day" (ss 224, 226, 229B) -- `the day n months after`, `the day n days after`
  -- the first day is left out, so the period ends on the same day of the later month (the last day of a shorter month;
  28 February for 29 February) -- the Acts Interpretation Act 1954 (Qld) s 38 (not deposited) governs; 1 March is the
  other reading for a count from 29 February or 31 August.
- **F2** s 106(h) the nine listed persons -- `s 106 -- a prohibited reason` -- one choice "with a listed person" -- a
  separate choice per person, with "another person" answering JUST FALSE.
- **F3** s 36 "requiring the person to have" treatment -- `s 36 -- serious injury or illness` -- whether the injury
  required it, asked as a fact -- whether the treatment was actually received.
- **F4** a duty whose condition is unmet (s 38(1) for an incident not arising out of the business; s 86(a), (b) for a
  worker who did not cease work under the division; s 87) -- JUST FALSE (no such duty or power on these facts) -- NOTHING.
- **F5** s 108(1), s 109(1) where an element of the prohibition fails (no intent, another aim, not knowing or reckless,
  another subject) -- JUST FALSE -- NOTHING (a prohibition limited in its own wording).
- **F6** s 112(6) and schedule 2A eligible persons -- `s 112(1), (6) -- the applicant may apply`, `schedule 2A -- I am an
  eligible person` -- closed lists ("each of the following is an eligible person"; the table "states ... who is
  eligible"), JUST FALSE for anyone else -- NOTHING.
- **F7** s 228(1), (2) for a prohibition or non-disturbance notice with no stay -- JUST FALSE (not stayed) -- NOTHING.
- **F8** s 231(4) "advise ... within 1 month" with no starting point -- `s 231(4) -- the DPP must advise by` -- 1 month
  from the referral -- 1 month from the applicant's request (finding 4).
- **F9** s 267 "part 6 and part 7 and division 7" -- `s 267 -- the Act gives me a civil right of action` -- Part 13
  Division 7 (civil penalty provisions), answered NOTHING with Part 7 as outside this encoding -- Part 5 Division 7
  (provisional improvement notices) (finding 2).
- **F10** s 88 where the worker unreasonably refused suitable, safe alternative work -- NOTHING (the Act withdraws its
  protection but does not say continuity is broken) -- JUST FALSE.
- **F11** s 232(1)(c) three alternative events -- one event day, asked as the day of the contravention, notice or
  agreement (the worker gives the latest) -- each day separately.
- **F12** s 39 for an incident that is not notifiable -- NOTHING (outside the duty's own wording) -- JUST FALSE.
- **F13** s 273 for a charge not for work health and safety, or a person who is not the business's worker -- NOTHING --
  JUST TRUE (the business may charge).
- **F14** s 113(3) for coercion (s 112(2)(c)) -- JUST FALSE, worded "the section gives no defence on these facts" --
  NOTHING (the defence is limited to (2)(a), (b) in its own wording).
- **F15** s 224(1)(b) "the longer period the regulator allows" -- taken in days after the decision came to notice, and
  used only if longer -- a period counted from the regulator's decision to allow it.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (ss 35, 36, 37), the "if" conditions (ss 7, 84, 87, 105, 106, 184), "only if"
(ss 112(4), 184(3)), "may only be made if" (s 231(1B)), "unless" (ss 86(a), 113(2)), "does not include" (ss 36, 37), "does
not apply" (s 109(2)), "does not prevent" (s 39(3)), "does not conduct" (s 5(7)), "can not" (ss 114, 115), "must not"
(s 273, read under N2 as "the business may not charge"), the s 113(3) defence (ruling (b)) and the periods the Act fixes
(ss 113, 224, 229B, 231) give `JUST FALSE`. `NOTHING` is answered where the person says there is no business or
undertaking (an undefined term), for s 39 outside a notifiable incident and s 273 outside its prohibition (*limits a
prohibition in its own wording*), for s 88 outside the division or after an unreasonable refusal (*limited by its own
wording*, *is silent*), for s 272 where a term does none of the listed things (*is silent*), for s 267 for a regulation's
duty and the civil penalty and entry provisions, and for schedule 2A item 13 (*points outside the sources*).

## Jural relations

| Provision | Bearer | Kind | Counterparty |
|---|---|---|---|
| s 38(1), (7) | person conducting the business or undertaking | duty | the regulator (for the worker's benefit) |
| s 39(1) | person with management or control of the workplace | duty (prohibition on disturbance) | the regulator |
| s 84 | worker | privilege (may cease work) | the business |
| s 86 | worker | duty (notify; remain available) | the business |
| s 87 | the business | power (direct alternative work) | worker |
| s 88 | worker | immunity (continuity not affected) | the business |
| ss 104, 107, 108, 109 | any person | duty (prohibitions) | the worker or other person |
| s 112 | eligible person | power (apply for orders) | the commission |
| s 113(1) | applicant | disability after 1 year | the person complained of |
| s 231(1A) | applicant | power (request a prosecution) | the WHS prosecutor |
| s 231(2)-(6) | WHS prosecutor, DPP | duties (advise, refer, give reasons) | the applicant |
| s 224, s 229B | eligible person | power (apply for review), within the period | the regulator, the commission |
| s 272 | -- | the term is void | -- |
| s 273 | the business | duty (no levy) | worker |

## What the Act turns out to say

1. **No compensation for coercion, and no civil remedy for misrepresentation.** s 112(3)(b) limits compensation to
   conduct in s 112(2)(a) or (b) (discriminatory conduct and procuring it); a worker coerced under s 108 may get an
   injunction or "any other order" but not compensation by name. s 109 (misrepresentation about the worker's rights) is
   not in s 112(2) at all, although Part 6 is headed "Discriminatory, coercive and misleading conduct": it is an offence
   only. Asserted.
2. **s 267 "part 6 and part 7 and division 7".** The model Act says "Division 7 of Part 13"; the Queensland text drops
   "of part 13", so "division 7" stands alone in a section that sits in Part 13 Division 8. Read as Part 13 Division 7
   (F9). A possible drafting slip.
3. **A two-test reason.** The offence (s 104(2)) needs the prohibited reason to be the *dominant* reason, with the onus
   reversed (s 110); the civil claim (s 112(4)) needs only a *substantial* reason, also presumed (s 113(2)). The same
   conduct can found an order and not a conviction. Encoded for the civil test; the dominant-reason test is in the
   description only.
4. **s 231(4) has no starting point.** The DPP "must consider the matter and advise ... within 1 month": 1 month from
   the referral is the natural reading (F8). s 231(1B)(c) gives a coronial-report route for category 1 and 2 offences
   only; a coronial report showing industrial manslaughter falls under (1)(a)(ii), which has no upper limit.
5. **The s 113 year cannot be extended.** s 229B(3) lets the commission extend the review period, s 224(1)(b) lets the
   regulator allow a longer internal review period, but s 113(1) has no extension power. Asserted (11 March 2026 is out).
6. **A short improvement notice shortens the review period.** For an improvement notice the internal review period is
   the notice's compliance period "or 14 days, whichever is the lesser" (s 224(3)(a)): a notice to comply in 7 days
   leaves 7 days to seek review. Asserted.
7. **s 88 protects, but says nothing of the other case.** Continuity of engagement is preserved "for prescribed purposes
   if the worker has not unreasonably failed" to do suitable, safe alternative work; the Act does not say what happens if
   the worker did (F10). The purposes are in the regulation, not deposited.
8. **Volunteers.** A volunteer commits no category offence except under the worker's and other persons' duties (ss 28,
   29) (s 34(1)), and no industrial manslaughter (s 34B(1)). Asserted.
9. **s 232 "latest of".** A coronial report ending inside the 2-year period does not shorten it; the latest period
   wins; industrial manslaughter has no limit (s 232(3)), and on an industrial manslaughter indictment the jury may still
   convict of a category 1 or 2 offence out of time (s 34E(2)). Asserted for the first two.

## Before this is worth relying on

- Check the text against the authorised PDF on legislation.qld.gov.au.
- Deposit the Work Health and Safety Regulation 2011 (Qld) and bring in its prescribed injuries, incidents, exclusions,
  the s 88 purposes and the item 13 decisions, so the worker states facts rather than regulation answers.
- The Acts Interpretation Act 1954 (Qld) s 38 for reckoning periods (F1), and the penalty unit value.
- Encode the duties of Part 2 and the representation machinery of Part 5 if wanted, and the s 260(4) civil penalty
  applications.
- A lawyer's view on findings 1, 2, 4 and 7 and forks F4-F10; an independent test pass and a human gate.
