# Privacy Act 1988 (Cth): the statutory tort, representative complaints and compensation (baseline encoding)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied. It follows the design defaults
ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

The encoding has three files:

- `pa-tort-dates.l4`: date arithmetic with the built-in date functions, not the daydate library.
- `pa-tort.l4`: the rules and the 22 exported questions, each with `@export` and a `@desc` on every input.
- `pa-tort-cases.l4`: the worked cases.

The duties with deadlines the person meets are regulative rules (`PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST
BREACH ... BECAUSE`). Each is run by `EVALTRACE` inside a question that takes only plain facts:

- Schedule 2 cl 14: commence proceedings before the cl 14(1) day, or before the day in the court's order;
- s 52A(1)(b): the respondent gives the complainant a copy of the statement within 14 days after receiving the
  determination, or within the longer period the Commissioner allows;
- ss 25(2)(b) and 25A(4)(b): apply for a compensation order within 6 years of the day the cause of action accrued.

No question takes a DEONTIC or an EVENT input.

**This is a layer beside two existing encodings, which stay as they are.** `baseline-2026-10` covers who is bound, APPs
7, 12 and 13, the credit reporting provisions the WA lives need, the notifiable data breach scheme (Part IIIC) and the
s 36/40/41 complaint gate. `naive-2026-10` was its first pass. This folder adds the provisions a person bringing a claim
meets that neither encodes:

- the statutory tort for serious invasions of privacy (Schedule 2, in force since 10 June 2025);
- representative complaints and the Commissioner's determination and its enforcement (Part V);
- the court's compensation orders for credit reporting contraventions (Part IIIA Division 7).

Nothing here is imported from, or restates a rule of, the other two folders.

## Edition

- **The Act:** Compilation No. 104, compilation date 4 June 2026, "includes amendments to Act No. 75, 2025" (register
  id C2026C00227). Deposited at `../../registers/source-bundle/C2004A03712.txt` (retrieved 13 October 2026).
- **Schedule 2** was added by the Privacy and Other Legislation Amendment Act 2024 (No. 128, 2024). Endnote 3 gives its
  commencement as 10 June 2025 (s 2(1) item 8). The amending Act itself, with its application provision, is not
  deposited (finding 1).
- **Not deposited:**
  - the State and Territory defamation Acts, which set the defamation maximum for non-economic loss that cl 11(5)(d)
    borrows. That maximum is an input.
  - the Criminal Code's definition of "reckless", borrowed by cl 6(1). Recklessness is asked as a fact.
  - the Corporations Act 2001 definition of "associated entity", borrowed by cl 19(4). It is folded into one input.
  - the Regulatory Powers Act's civil penalty orders, used by ss 25 and 25A. Whether an order has been made is asked as
    a fact.

## Checks

- Stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. Commands: `l4 run pa-tort-dates.l4`,
  `l4 run pa-tort.l4`, `l4 run pa-tort-cases.l4`.
- **137 assertions written, 137 satisfied, 0 errors, 0 warnings** in every file (2026-11-07).
- Every expected value was worked by hand from the text before the file was run, and none was copied from the
  encoding's output. All 137 passed on the first run of the cases file.
- In a scratch copy, the cl 14(1) last day for the first adult case was changed from 31 August 2026 to 1 September 2026.
  The run reported one error, so the runner catches a wrong expectation.

## Seat

**The individual whose privacy was invaded.** That person is:

- the plaintiff under Schedule 2: the person filmed, recorded, followed, or whose health, intimate or financial
  information was collected, used or disclosed;
- the complainant, or a class member of a representative complaint, under Part V: for example one of many customers
  affected by a data breach;
- the person who suffered loss from a credit reporting contravention, under ss 25 and 25A.

The person asks:

- "Can I sue?" "Is the person who did it exempt?" "Do they have a defence?"
- "By when must I start?" "Does a repost restart the clock?"
- "What damages can I get, and what is the cap?" "What else can the court order?" "Does their apology count as admitting
  it?"
- "Can I complain for the whole group?" "Can I leave the group, or complain on my own?"
- "What can the Commissioner's determination give me? Must I be sent the statement, and by when? Can I enforce it?"
- "Can I get compensation for the credit reporting breach, and by when must I apply?"

The court, the Information Commissioner and the Administrative Review Tribunal get no seat. Their findings,
satisfactions and opinions are asked as facts. The defendant and the respondent are parties the Act puts liabilities
on. No defendant seat was written (see "Before this is worth relying on").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The one number the Act borrows (the
  defamation maximum in cl 11(5)(d)) comes from Acts that are not deposited, so it is an input.
- **The actors the text names.** Followed: the plaintiff, the defendant, journalists and those working with them,
  agencies, State and Territory authorities, law enforcement bodies, intelligence agencies, the publisher and its
  associates, the complainant, the class members, the respondent, the Commissioner, the courts and the Tribunal.
- **Judgments handed to someone else are answered conditionally.** Followed. Each of these is an input:
  - cl 7(1)(b), (d), (e): the reasonable expectation of privacy, seriousness, and the public interest balance;
  - cl 8(1)(c): "reasonably believed";
  - cl 8(1)(d)(ii): "proportionate, necessary and reasonable";
  - cl 8(2)(c): whether the defendant "would be able to establish" a defamation defence;
  - cl 10: "no reasonable prospect";
  - cl 11(4): "exceptional circumstances";
  - cl 14(3): "not reasonable";
  - cl 19(1)(c): "not materially different";
  - cls 16 and 16A: good faith.
- **The Act's own definitions are worked out; borrowed terms are asked.**
  - Worked out: journalist (cl 15(2)), journalistic material (cl 15(3)), the cl 6(1) lists of intrusion and misuse (as
    open lists), and the single publication rule (cl 19).
  - Asked: reckless (Criminal Code), associated entity (Corporations Act), Australian law and court/tribunal order
    (s 6(1), used as a fact), and whether a body is a law enforcement body or intelligence agency. The person picks
    from the closed lists in cl 6(1).
- **One case is the text's natural unit.** Followed: one invasion of privacy and one defendant; one complaint and one
  determination; one contravention and one application.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**

- **Schedule 2:**
  - cl 6(1): "intruding upon the seclusion", "misusing information", journalist and journalistic material by
    cross-reference, and the closed lists of law enforcement bodies and intelligence agencies, offered as choices;
  - cl 7(1), (2), (7);
  - cls 8, 10, 11, 12 (with cl 9(1)), 13 and 14;
  - cls 15 (all), 16, 16A, 16B, 17 and 18;
  - cl 19 and cl 20(1).
- **Part V:** ss 36(1)-(3), (5), 38, 38B(2), 39, 52(1)(b), (1AB), (1B), (3), (4), 52A(1)(b), 54(1) (by its effect),
  55A(1), (5), (8), and 62(1)-(3), (5), (6).
- **Part IIIA Division 7:** ss 25 and 25A.

**Out, and why:**

- **The APPs, Part IIIA's rules on credit reporting bodies and providers, Part IIIC (notifiable data breaches) and the
  s 36/40/41 complaint gate.** `baseline-2026-10` encodes APPs 7, 12 and 13, Part IIIC and the gate. The other APPs
  (1-6, 8-11) are duties on the entity. For a claimant they matter only as the breach that makes an act an
  "interference with privacy" under s 13. Here that is asked as a fact ("may be an interference with the privacy of 2 or
  more individuals"). Encoding APPs 1-6 and 8-11 would be a separate layer.
- **Schedule 2, Part 1** (cls 1-5: objects, outline, Crown, constitutional basis): machinery. Clause 5's extended
  operation is not tested; the encoding assumes the invasion is within the Schedule's reach (finding 9).
- **cl 7(3), (5), (6) and cl 11(6):** matters the court may consider. They go to findings that are inputs.
- **cl 8A** (deciding whether an exemption applies, at any stage) and **cl 9(2)** (regard to the public interest
  in publication): the court's procedure. The injunction itself is in the cl 12 list.
- **cl 20(2)** (costs of discontinued proceedings), **cl 21** (other laws saved), **cl 22** (the Commissioner's
  intervention) and **cl 23** (jurisdiction): nothing for the person to state or decide. cl 21 means that State and
  Territory remedies remain alongside this one.
- **ss 36(4), (6)-(8), 36B, 37:** who the respondent is, and staff assistance. Naming the respondent is asked as a fact.
- **ss 38A, 38B(1), (3), 38C:** the Commissioner's management of a representative complaint.
- **ss 40-51:** investigation, conciliation and the Commissioner's powers. The gate in ss 40(1A), (1B) and 41(1)(c) is
  in `baseline-2026-10`.
- **s 52(1)(a), (1A), (1AAA), (1AA), (2), (3A), (5), (5A), 52A(1)(a), (c), (d), (2), 53-53B, 55, 55B, 56-61, 63 onwards:**
  the Commissioner's procedure, determinations after own-motion investigations, and agencies' internal steps.
  s 55(d) is mentioned in an answer.
- **ss 13G-13K, 80U-80W and Part VIB:** civil penalties and injunctions the Commissioner seeks. The person cannot bring
  them.
- **ss 25B and following:** reviews and codes.
- **The application provision of No. 128, 2024:** not deposited (finding 1).
- **No requirement-ledger entry exists for these provisions** in `subjects/au/requirements.jsonl`, and none was
  raised: no scenario life has reached them. The encoding's priority came from the claims-law baseline request.

## Fork register

Each line gives the provision, the function, the answer taken, and the other reading.

- **F1** Anniversaries and birthdays (cl 14(1)(a) "21st birthday" and "under 18"; cl 14(1)(b), (4) "1 year", "3 years",
  "6 years"; ss 25(2)(b), 25A(4)(b) "6 years"). Functions: `plus calendar years` (pa-tort-dates.l4) and every function
  that uses it. Answer taken: the same day of the month that many years on. A 29 February start falls on 28 February in
  a common year, so a person born 29 February 2008 turns 18 on 28 February 2026. Other reading: 1 March.
- **F2** cl 14(1) "before the plaintiff's 21st birthday" and "before the earlier of ... the day that is 1 year after
  ...". Functions: `cl 14(1) -- the last day to start proceedings` and `cl 14 -- are my proceedings in time`. Answer
  taken: the last day to commence is the day before; an awareness day before the invasion counts as the day of the
  invasion. Other reading: "before" a day includes that day.
- **F3** cl 14(4) "must not be later than 6 years after". Function: `cl 14 -- are my proceedings in time`. Answer taken:
  an order naming a later day is read as naming the sixth anniversary. Other reading: such an order is beyond power and
  gives no extension at all.
- **F4** "To the extent that" in cls 15(1), (1A), 16, 16A, 16B(c), (d) and 17(b), (c). Function: `Part 3 -- is the
  invasion exempt`. Answer taken: the whole invasion is exempt when the exempt element is present. Other reading: only
  that part of the invasion is exempt, and the rest stays actionable.
- **F5** The order of the bars. Function: `Schedule 2 -- can I sue`. Answer taken: cl 20, then Part 3, then the cl 7
  elements, then the cl 8 defences, with the first one met reported. Other reading: all of them reported together. The
  component questions report each bar on its own.
- **F6** cl 11(3) damages "for emotional distress". Functions: the two cl 11(5) questions. Answer taken: they are
  counted as non-economic loss inside the cap. Other reading: a separate head outside cl 11(5).
- **F7** s 36(3) and (5) "shall", and s 38(2) "must", when not met. Function: `ss 36, 38 -- can I lodge a representative
  complaint`. Answer taken: "not as it stands". Other reading: the complaint is still received, and the Commissioner
  may seek the missing particulars.
- **F8** s 52(3) "(other than a determination made on a representative complaint)". Function: `s 52 -- what a
  determination can give me`. Answer taken: no reimbursement of expenses on a representative complaint. Other reading:
  the text says nothing for class members, so the answer would be NOTHING rather than a no.
- **F9** ss 25(2)(b) and 25A(4)(b) "within 6 years of the day the cause of action accrued". Functions: `ss 25, 25A --
  the last day to apply` and the compensation question. Answer taken: the sixth anniversary is the last day. Other
  reading: the day before it.
- **F10** s 52A(1) "within 14 days after receiving the determination (or such longer period as the Commissioner
  allows)". Function: `s 52A -- has the respondent given me the statement in time`. Answer taken: count from receipt as
  day 0, so the last day is receipt plus 14; a period shorter than 14 days is read as 14. Other reading: the period runs
  from the day after receipt, with no difference in the result, or the person's figure is taken as given.
- **F11** cl 18 "a person who is under 18 years of age". Functions: the Part 3 question and the cl 18 input. Answer
  taken: under 18 when the invasion happened (the `@desc` says so). Other reading: under 18 when the action is brought,
  which the present tense also allows (finding 6).
- **F12** cl 15(2) and (1A): one set of journalist inputs. Function: `Part 3 -- is the invasion exempt`. Answer taken:
  the journalist the person names is the one for both cl 15(1) and (1A). Other reading: under (1A) the journalist who
  prepared the material may be a different person from the one acting. The person answers about the journalist who
  prepared it.
- **F13** s 39 "a person who is a class member". Function: `s 39 -- can I lodge my own complaint`. Answer taken: a
  person who has withdrawn under s 38B(2) is no longer a class member, as the note to s 38B(2) says. Other reading: none
  needed.
- **F14** ss 55A(1) and 62(3) after an own-motion determination (s 52(1A)). Function: `ss 55A, 62 -- can I enforce the
  determination`. Answer taken: NOTHING-kind, because the lists of who may sue name the complainant only for s 52(1),
  and the lists are not closed with "only". Other reading: the text's no.

**Sites decided without a fork line:**

- The text's no, for these flat negatives: cl 11(2) "must not", cl 13 "does not constitute ... is not relevant", cls
  15-18 "does not apply", cl 20(1) "cannot", s 39 "is not entitled", s 62(5) "may not ... until".
- The text's no, for these conditions: cl 7(1) "if", cl 14(1) as a period, s 38(1) "only if", s 38B(2) "at any time
  before" (a period), s 52A(1)(b) "if required by the declaration" (a "where" condition), s 62(1) "if an agency fails",
  and ss 25(1) "if" and 25(2) "only if".
- "It is a defence ... if": when no ground holds, this clause gives no defence on these facts (ruling (b) of
  2026-11-05).
- The open lists in cl 6(1) ("includes, but is not limited to"): NOTHING-kind when none of the listed acts happened and
  the court has made no finding.
- cl 11(4) "may award ... in exceptional circumstances", outside those circumstances: NOTHING-kind (a grant limited in
  its own wording).
- cl 10 without the court's satisfaction, and cl 13 with no apology: NOTHING-kind.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags in the cl 7 question (the open cl 6(1) lists), the cl 10, cl 11(4) and
cl 13 questions, and the s 55A/62 question (F14). It returns NOTHING from the helper `cl 7(1)(a) -- did they invade my
privacy`. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (cl 14, s 52A(1), ss 25(2)(b) and 25A(4)(b)) are regulative rules run by EVALTRACE. Outside
each period, the answer is the consequence the text gives: out of time unless the court orders a later day; the
respondent in breach; or the court may not make the order.

## What the Act turns out to say

1. **Whether Schedule 2 reaches an invasion that happened before 10 June 2025 is not in the deposited text.** The
   compilation gives Schedule 2's commencement (endnote 3), but the reach in time is set by the application provision
   of the Privacy and Other Legislation Amendment Act 2024, which is not deposited. The encoding does not test the
   date of the invasion. An invasion before 10 June 2025 may not be actionable under the Schedule at all.
2. **A merely negligent invasion is not actionable.** cl 7(1)(c) requires the invasion to be "intentional or reckless".
   A data breach caused by carelessness alone gives no cause of action under the Schedule, however serious, so the
   Part V complaint (and, for credit information, ss 25 and 25A) stay the routes for most breach victims. Asserted
   (`C7 NOT INTENTIONAL`).
3. **The damages cap follows the defamation cap upwards but never falls below $478,550.** cl 11(5) fixes $478,550 and
   takes the greater of it and the defamation maximum for non-economic loss "under an Australian law". The defamation
   maximum is set by the State and Territory defamation Acts (not deposited) and may differ between them; the text does
   not say which applies where they differ. The $478,550 is not indexed in the Schedule. Asserted at the cap, one dollar
   over and with a higher defamation figure.
4. **Economic loss is outside the cap; emotional distress is read as inside it.** The cap covers non-economic loss and
   exemplary or punitive damages only. Damages "for emotional distress" (cl 11(3)) are not named in cl 11(5); this
   encoding counts them as non-economic loss (fork F6). Aggravated damages are barred outright (cl 11(2)). Asserted.
5. **A child's time limit can run far longer than the court could ever extend an adult's.** A plaintiff under 18 at the
   time has until the 21st birthday (cl 14(1)(a)), with no 3-year or 6-year outer limit. For a 5-year-old, that is 16
   years. Yet the court's power to extend (cl 14(2)-(4)) is capped at 6 years after the invasion. For a young child,
   an extension can therefore never help, because it ends before the time they already have. For a 17-year-old, the
   21st birthday comes about 4 years on, and an extension can reach 6 years. Asserted (the aged-15 cases).
6. **cl 18 is in the present tense.** "A person who is under 18 years of age" does not say at what time. Read as at the
   time of the invasion (fork F11), it exempts teenagers' conduct for good. Read as at the time of the action, the
   exemption would end on the defendant's 18th birthday, and the plaintiff could wait for it, within cl 14.
7. **cl 15(1A) exempts anyone who publishes or distributes a journalist's material.** Unlike cl 15(1), (1A) does not
   limit who the invader is. A person who reposts a news report that invades someone's privacy is exempt "to the
   extent" the invasion involves that distribution. Asserted (`X 15(1A)` for a person not listed).
8. **cls 16B(c), (d) and 17(b), (c) exempt anyone, for information passing to or from the police or an intelligence
   agency, with no good-faith condition.** A private person or business disclosing information about someone to a law
   enforcement body, or using information such a body disclosed, is outside the Schedule to that extent. Contrast cls
   16 and 16A, which require good faith of agencies and their staff. Asserted.
9. **cl 7 has no subclause (4).** The deposited text runs (1), (2), (3), (5), (6), (7), and the amendment history shows
   only "ad No 128, 2024" for the clause. The gap is in the compiled text; this encoding reads nothing into it.
10. **A determination after an own-motion investigation can declare individuals entitled to compensation (s 52(1A)(d)),
    but only the Commissioner can enforce it.** ss 55A(1)(a) and 62(3)(a) give the complainant standing only for a
    determination "made under subsection 52(1)". Asserted as NOTHING-kind (fork F14).
11. **A representative complaint cannot recover the class's expenses.** s 52(3) leaves representative complaints out of
    the reimbursement of expenses (fork F8). Asserted.
12. **Compensation for credit reporting contraventions depends on the regulator going first.** ss 25 and 25A need a
    civil penalty order or a finding of guilt under Part IIIA. The person cannot bring the contravention to court
    themselves. The 6 years run from the day "the cause of action that relates to the contravention ... accrued", which the
    Act does not define. If that is the day of the contravention, a penalty order made more than 6 years later leaves
    the person without these orders. Asserted (the six-year edge).
13. **The single publication rule moves the start of the clock backwards.** Under cl 19(2), a materially similar
    republication is taken to occur on the day of the first publication. Someone who first learns of a post through a
    repost years later may find the 3-year limb already run, even though the 1-year limb from awareness has not.
    Asserted (cl 19 cases).

## Before this is worth relying on

- Deposit the Privacy and Other Legislation Amendment Act 2024, and encode its application provision for Schedule 2
  (finding 1).
- Deposit the State and Territory defamation Acts' damages provisions, to replace the defamation-maximum input.
- A defendant's seat (the publisher, the business, the employer) over the same Schedule 2 rules.
- Encode APPs 1-6 and 8-11 as a separate layer, so that "an interference with privacy" (s 13(1)) can be worked out rather
  than asked.
- An independent test pass and the human gates.
