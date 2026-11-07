# Public Interest Disclosure Act 2010 (Qld) — baseline encoding, the discloser's seat

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below).
There is no REFUSE, no `#ASSERT REFUSED` and no BECAUSE; a question that reaches a gap answers with a `not covered: …` constructor giving the reason, and the cases assert it.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

It was written in a run of baseline encodings of the laws behind compensation and other civil claims, here under employment and reprisal claims. The focus was **the provisions a claimant meets**: for this Act, a whistleblower who discloses wrongdoing in the Queensland public sector and may then suffer a reprisal, and the claims that follow (damages in tort, a complaint under the Anti-Discrimination Act 1991, an injunction, an appeal, relocation).
The Act is small (about 68,000 characters), so nearly all of its operative provisions are in; what is out is listed under Scope.
This is the first encoding of this subject; nothing existing was touched. No ledger entry was open for it.

Files:
- `pidq-dates.l4`: the date arithmetic, the only module that imports `daydate`;
- `pidq-discloser.l4`: the rules, the discloser's 19 exported questions and one regulative rule;
- `pidq-cases-discloser.l4`: the worked cases.

The 19 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order:

- can I make a public interest disclosure about this, and under which section (ss 12, 13, 19);
- is this person or body a proper authority for it (ss 5, 6, 14–16, 19(2), 20);
- may I make it this way, or must I use the authority's procedure (ss 17, 19(4), (5));
- once a disclosure is made (the heading says so):
  - may the entity decide not to investigate it (s 30(1), (2));
  - by when must I apply for a review, and is my application in time (s 30(3), 28 days);
  - must the entity tell me what it is doing, and what (s 32);
  - by when must I be told whether it will be investigated, and can I now go to a journalist (s 20, 6 months);
- am I protected from liability, confidentiality duties and defamation (ss 36–39);
- could I be prosecuted for false or misleading information (s 66, with ss 67, 69);
- if something has been done or threatened (the heading says so):
  - was it a reprisal (ss 40, 41, 45, schedule 4 "detriment");
  - can I claim damages (s 42, s 44(3)(b));
  - whom can I sue (s 43);
  - can I complain under the Anti-Discrimination Act 1991 instead, and what do I give up (ss 44, 50);
  - can I appeal on the ground that it was a reprisal (s 46);
  - can I be relocated (s 47);
  - where can I apply for an injunction (ss 48–50);
- can a person who handled my disclosure reveal my identity (s 65, with s 20(3)(c) and s 67).

**Regulative rule.** The one period that bears on what other people do for the discloser, s 20(1)(b)(iii) ("did not notify the person, within 6 months after the date the disclosure was made"), is written as `PARTY … DO … WITHIN … HENCE FULFILLED LEST (PARTY the discloser MAY disclose … to a journalist)`. It is `DO`, not `MUST`, because the Act puts no duty on the entity to notify within 6 months (s 32 requires reasonable information but sets no time): notice in time closes this route to a journalist, and its absence opens it (fork F16, finding 5). The period is written once as a named deadline, and both the seat questions and the rule's `WITHIN` use it. The questions take plain dates. The cases assert the rule through `CONSIDER EVALTRACE … WHEN FULFILLED`: notice on the last day, the day after, a late notice followed by going to a journalist, and going to a journalist too early.

s 30(3) (a review "within 28 days after receiving the written reasons") is the discloser's own permission, not a duty: a `MAY … WITHIN` would read the same whether used in time or not, so it is encoded as two date questions only.

## Edition

- Public Interest Disclosure Act 2010 (Qld), the version in force from 30 August 2024, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2010-038.txt`. It is a plain-text conversion of the Queensland Legislation HTML view, not the authorised PDF.
- No regulation under the Act is deposited. The Act leaves to regulation only further public sector entities and chief executive officers (ss 6(1)(k), 6(2)(d), 8(2), 71(2)); none sets a number used here.
- Not deposited, and so not encoded: the Acts Interpretation Act 1954 (how the periods are reckoned; fork F15, finding 9), the Penalties and Sentences Act 1992 (the value of a penalty unit; answers give units), the Crime and Corruption Act 2001 ("corrupt conduct", asked), the Anti-Discrimination Act 1991 (chapters 6 and 7, how a complaint is dealt with), the Industrial Relations Act 2016 and the Public Sector Act 2022 (the relocation appeal and the injunction procedure), the Limitation of Actions Act 1974 (the time limit for a s 42 claim, which this Act does not set; that Act has its own encoding in `subjects/au/qld/limitation-of-actions-act-1974/`, which IMPORT cannot reach).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error ("assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pidq-dates.l4` | 0 | 0 | 0 | 0 |
| `pidq-discloser.l4` | 0 | 0 | 0 | 0 |
| `pidq-cases-discloser.l4` | 0 | 0 | 145 | 145 |

Every exported question has cases. Expected values were written by hand from the text.

The edges asserted include:
- the 28th day after receipt of reasons, and the 29th; an application dated before the reasons;
- 28 days running from 31 January to 28 February, and across 29 February 2028;
- 6 months from 31 August ending on 28 February 2027 and on 29 February 2028, and from 29 February 2028;
- for the journalist: asked on the last day of the 6 months (not yet) and the day after (yes); told on the last day (no) and a day late (yes);
- the regulative rule: notice on day 181 (fulfilled), day 182 (route opens), a late notice then a journalist, a journalist too early;
- each limb of the "has information" test alone, and neither;
- "substantial" on and off for each kind that needs it, and the policy-disagreement exclusion;
- a disclosure about a chief judicial officer herself (s 16(4));
- each s 17(3) alternative with its condition met and not met; a GOC's procedure with no alternatives;
- a reprisal ground that was the main reason, a substantial one among others, a minor one, and none; an attempt with and without detriment suffered;
- the s 43(2) defence; each half of the s 47(2) ground; the s 47(6) agreement;
- both limbs of s 65(5).

## Seat

**The discloser**: a person who has information about wrongdoing in the Queensland public sector, has made or is thinking of making a public interest disclosure, and may have suffered a reprisal for it. Usually a public officer (a council, department, hospital or police employee), sometimes a GOC employee, sometimes any member of the public (for the s 12 matters). The questions are ones like:
- "Can I report this, and to whom?"
- "Must I use their whistleblower procedure, or can I go to the CEO?"
- "Will they tell me what they are doing? When can I go to the press?"
- "Am I protected if I breach a confidentiality clause?"
- "Was being moved off my job a reprisal? Can I sue, and can I sue the council too?"
- "Can I get an injunction or be moved somewhere safe?"
- "Can they tell the person I reported who I am?"

The Act puts duties on entities, managers and anyone who might take a reprisal; those duties are encoded for what they mean to the discloser. No second seat is written: a seat for the person who is the subject of a disclosure (s 3(c), natural justice under s 65(4)), or for an employer facing a s 43 claim, is left for a later layer. There is no seat for the oversight agency (the Ombudsman), the Crime and Corruption Commission, the industrial relations commission or a court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets every number used: 6 months, 28 days, 167 and 84 penalty units, 2 years. No regulation is needed for them.
- **The actors the text names.** Followed: the discloser, the proper authority (a member of the Legislative Assembly, a public sector entity, a chief judicial officer, the Crime and Corruption Commission), a GOC or rail government entity, a journalist, the person who takes a reprisal, the manager, the employing entity, the industrial relations commission and industrial commission, the Supreme Court.
- **Judgments answered conditionally.** "Honestly believes on reasonable grounds" (ss 12(3), 13(3), 15(1)(b)), "substantial and specific", "reasonable procedure" (s 17(2)), "reasonably considers" (s 30(1)), "would be likely to adversely affect" (s 32(4)), the part the unlawful ground played (s 40(5)), "reasonable management action" (s 45), "reasonable steps" (s 43(2)), "considers the ground is established" (s 47(5)), "essential" and "unlikely" (s 65(5)) and "reasonably believes" (s 65(3)(f)) are all inputs. Whether an injunction is granted (ss 51–54) is the court's, and is not decided.
- **The Act's definitions worked out; borrowed terms asked.**
  - Worked out: "proper authority" (ss 5, 14–16), the s 6(2)(b) exclusion of a GOC, "has information" (ss 12(3), 13(3), 19(3)), "reprisal" (s 40), the schedule 4 heads of "detriment", "reasonable management action" (s 45, as one input), "confidential information" (s 65(7), as the discloser's identity).
  - Asked: "public officer" (s 7, glossed in the `@desc`), "corrupt conduct" (Crime and Corruption Act 2001), "disability", "environment", the schedule 2 provisions (as a choice), "maladministration" (glossed from schedule 4), "public service employee", "employee" for s 48, "rail government entity".
- **One case.** One disclosure, and one act or threat said to be a reprisal for it.
- **The Act's terms with plain glosses.** Followed, in the `@desc` texts and comments.
- **Machinery out.** Followed: ss 1, 2, 4, 9, 71, chapter 5, the offence procedure in ss 68–70 (s 69 named in an answer), chapters 7 and 8.

## Scope

**In:**
- s 3 (objects; quoted in the header), ss 5, 6, 7 (definitions the questions use), s 10 (named in answers);
- chapter 2: s 11; Part 2 ss 12–17; Part 3 s 19; Part 4 s 20.
  - ss 21–25 (an unknown wrongdoer, an involuntary disclosure, a disclosure in court, past or future events, more than one disclosure) only remove conditions; none adds one, so no question needs them. They are in by their effect: the s 12/13 question asks nothing about them.
- chapter 3: s 26 (a GOC counts as a public sector entity in chapter 3; finding 3), s 30, s 32; s 34 (in an answer);
- chapter 4: ss 36–47, ss 48–50; ss 51–56 named in comments;
- chapter 6: s 65, s 66, s 67(1), s 69 (in an answer);
- schedule 4 (dictionary) for the terms used; schedule 2 offered as a choice; schedule 1 (chief executive officers) glossed in s 17(3)(a).

**Out, and why:**
- **s 8 and schedule 1 (who is a chief executive officer):** asked as part of the s 17(3)(a) choice.
- **s 23 (a disclosure to a court) and s 16(5), (6), s 23(3), (4) (onward referral):** the court's or chief judicial officer's.
- **ss 27–29, 33 (procedures, records, information to the oversight agency):** the entity's internal duties; the discloser cannot enforce them.
- **s 31 (referral):** the entity's power. s 31(3), (4) (no referral where there is an unacceptable risk of reprisal; consult the discloser "if practicable") matter to the discloser but turn wholly on the entity's view, and set no time; left for a later layer.
- **s 35:** parliamentary privilege.
- **ss 51–56 (the grounds and terms of an injunction):** the court's or commission's discretion; named in comments.
- **Chapter 5 (ss 57–63, the oversight agency):** its functions, standards and reports, none of which a discloser can use as a right.
- **s 64 (protection of officers acting under the Act), s 67(2), ss 68–70 (offence procedure; s 69 named), s 71 (regulations):** machinery or the prosecution's.
- **Chapters 7 and 8 (repeal of the Whistleblowers Protection Act 1994, transitional):** ss 75 and 76 limit s 42 claims against an employer and s 44 complaints to reprisals after "the commencement", and the deposited text does not state that date. A reprisal that old is not asked about.

## Fork register (questions with no convention, decided case by case)

Each line gives the provision, the function, the answer taken, and the other reading.

- **F1** ss 11–13, a matter neither s 12 nor s 13 lists ("something else"): `Can I make a public interest disclosure question`. Answer taken: "no" (ss 12(1) and 13(1) begin "This section applies if", and s 11 says a public interest disclosure "is a disclosure under this chapter"). Other reading: `not covered`. The answer names s 10, which keeps other laws' protection.
- **F2** s 13 for a person who is not a public officer: same function. Answer taken: "no" (s 13(1) "applies if a person who is a public officer"). Other reading: `not covered`.
- **F3** s 19(2), a GOC employee's s 19 disclosure to anyone but the GOC, the rail government entity or the Crime and Corruption Commission: `Is this a proper authority question`. Answer taken: "no" (no other route exists for corrupt conduct of a fellow employee). Other reading: `not covered`, since s 19(2) has no "only".
- **F4** a rail government entity as recipient of a disclosure under s 12 or 13: same function. Answer taken: `not covered`; whether it is a public sector entity under s 6(1)(j) turns on the Transport Infrastructure Act 1994. A GOC is answered "no" by the flat negative in s 6(2)(b).
- **F5** s 16(4) for a disclosure that is not about a judicial officer, made to a chief judicial officer: same function. Answer taken: "no" ("may receive … only if").
- **F6** s 30(1) when no ground is met: `May the entity decline to investigate question`. Answer taken: "no" ("may decide … if").
- **F7** s 32 for a member of the Legislative Assembly, and for a GOC that received a s 19 disclosure: `What must I be told question`. Answer taken: "no" (s 32(1) binds "A public sector entity to which a public interest disclosure is made under section 15, or referred under section 31 or 34"). Other reading: `not covered` (finding 3).
- **F8** s 32(1) for a referred disclosure: same function. Answer taken: a third answer, "either you or the entity that referred it" (finding 4). Other reading: both.
- **F9** ss 36–39 for a disclosure that is not a public interest disclosure: `Am I protected question`. Answer taken: `not covered` (the sections speak of "A person who makes a public interest disclosure", a scope limit with no "only", and s 10 keeps other laws). Other reading: "no".
- **F10** s 40 for a ground that was only minor, and for a harm outside the schedule 4 list: `Was it a reprisal question`. Answer taken: `not covered` both times (s 40(5) says a substantial ground "is sufficient", not that it is needed; "detriment includes"). Other readings: "no" for a minor ground; "yes" for any harm.
- **F11** s 42 for an attempt that caused the discloser no detriment: `Can I claim damages question`. Answer taken: "no" ("liable in damages to any person who suffers detriment as a result"). Other reading: `not covered`, since s 42(2) allows "any appropriate remedy".
- **F12** s 46 without an existing appeal or review right: `Can I appeal on the ground it was a reprisal question`. Answer taken: "no", worded "s 46 gives no appeal on these facts" ("This section applies to a public officer who, under an Act, may appeal"). Other reading: `not covered`.
- **F13** s 47 for a person who is not a public service employee: `Can I be relocated question`. Answer taken: `not covered` ("gives a public service employee a right", with no "only"). Other reading: "no".
- **F14** s 65 for a person who did not gain the information through the Act's administration: `Can my identity be revealed question`. Answer taken: "s 65 does not bind them" (s 65(1) "If a person gains …"). This says nothing about any other law that may bind them.
- **F15** the reckoning of the 28 days and the 6 months: `pidq-dates.l4`. Answer taken: the day of the event excluded, the period ending on its last day; 6 months ending on the same day number, or the last day of a shorter month; no move past a weekend or public holiday. Other reading: the Acts Interpretation Act 1954 (not deposited) may move a last day that is not a business day (finding 9).
- **F16** s 20(1)(b)(iii) as a regulative rule: `the s 20 six-month rule for a disclosure made on`. Answer taken: `DO` for the entity, `MAY` for the discloser in the `LEST`. Other reading: `MUST`, treating the 6 months as a duty, which the text does not state.
- **F17** s 20 when the entity is told late but is investigating: `Can I go to a journalist question`. Answer taken: "yes" under (iii), since the entity "did not notify the person, within 6 months". Other reading: a late notice that it is being investigated closes the route (finding 5).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they apply here:
- **"no", because the text says no in its own words:**
  - s 6(2)(b) "are not public sector entities" (a GOC) is a flat negative;
  - s 16(2), (3) and (4) are closed with "only";
  - s 30(1), s 47(5), s 65(1) are "if" conditions; s 12(1), s 13(1), s 20(1) "apply if";
  - s 39 ("is not affected"), s 44(3) ("can not subsequently"), s 47(6) ("can not direct"), s 50 ("may not apply") are flat negatives;
  - s 49 "applies only to a person who can not apply under section 48";
  - the 28 days and 6 months are periods fixed in the text's words;
  - s 43(2) is a defence: where the employer does not prove reasonable steps, the answer is that it is liable, not that it has no defence at all.
- **`not covered`, because the case falls outside a scope limit with no "only", or the text is silent or inclusive:**
  - a rail government entity as a public sector entity;
  - ss 36–39 for a disclosure that is not a public interest disclosure;
  - a minor reprisal ground, and harm outside the inclusive "detriment" list;
  - s 47 for anyone not a public service employee;
  - s 32 for the Crime and Corruption Commission (points outside the sources).

## What the Act turns out to say

1. **A reprisal is a tort with unusual features.** Damages (including exemplary damages) are available against the person who took it (s 42(1), (2)), the trial in the Supreme or District Court is by judge alone (s 42(3)), no prosecution is needed (s 42(5)), and the Workers' Compensation and Rehabilitation Act 2003 does not apply to the proceedings (s 42(6)), so a reprisal claim by a worker is not run through that Act's claims process. The employing public sector entity or GOC is jointly and severally liable for an employee's reprisal in the course of employment, unless it proves reasonable steps (s 43). The Act sets no time limit for the claim; the Limitation of Actions Act 1974 governs. Asserted.
2. **A disclosure about a chief judicial officer's own conduct that is not corrupt conduct or a reprisal has nowhere to go.** s 16(3) says it "may be made only to the chief judicial officer of the relevant court or tribunal", and s 16(4) lets a chief judicial officer receive a disclosure "only if the disclosure is about the conduct of another judicial officer". MPs and public sector entities are shut out by ss 14(2) and 15(2). Asserted (both halves).
3. **A GOC that receives a disclosure under s 19 owes the discloser no s 32 information.** s 26 makes "public sector entity" include a GOC for chapter 3, but s 32(1) applies only to a disclosure "made under section 15, or referred under section 31 or 34", and a s 19 disclosure is made under s 19. s 30 (deciding not to investigate, with written reasons and review) does reach the GOC. Equally, a member of the Legislative Assembly owes the discloser nothing under the Act (s 34). Asserted.
4. **For a referred disclosure, s 32(1) does not say who is to be told.** The receiving entity "must give the person who made the disclosure, or the entity that referred the disclosure, reasonable information". Read as alternatives, the entity may satisfy s 32 by telling the referring entity alone. Asserted as the third answer.
5. **The 6 months in s 20 are a trigger, not a deadline.** No section requires the entity to say within 6 months whether it will investigate. Once the 6 months pass without notice, s 20(1)(b)(iii) is met, and a later notice that the matter is being investigated does not, on the words, undo it. The 6 months also run from the date the disclosure was made, even where it was referred onward (s 20(1)(b) points at the referee entity, but the clock is the original date). Asserted (F17, and the regulative rule).
6. **s 40(5) says when an unlawful ground is enough, not when it is needed.** "It is sufficient if the unlawful ground is a substantial ground" leaves open whether a minor ground is enough for "because" in s 40(1). Asserted as `not covered`.
7. **The election between the Anti-Discrimination Act 1991 and the courts is lopsided.** Commencing court proceedings under s 42 bars a later complaint (s 44(3)(a)); a complaint bars later s 42 proceedings only if it "is accepted" (s 44(3)(b)); but merely making the complaint bars an injunction (s 50). Asserted.
8. **A GOC's whistleblower procedure binds its employees more tightly than a department's binds public officers.** s 19(5) requires the procedure to be used and has no counterpart to s 17(3), so a GOC employee cannot instead go to the chief executive or a manager. Asserted.
9. **The Act does not say how its periods are reckoned.** The Acts Interpretation Act 1954 does, and it is not deposited. This encoding excludes the day of the event, ends 6 months on the same day number (or the last day of a shorter month), and does not move a last day past a weekend or public holiday. If the Acts Interpretation Act moves a last day that is not a business day, a review application on the following Monday would be in time where this encoding says it is not (F15).
10. **A member of the public cannot make a public interest disclosure of corrupt conduct.** s 12 lets any person disclose only dangers to a person with a disability, schedule 2 environmental offences and contraventions, and reprisals; corrupt conduct, maladministration, misuse of resources and general dangers are for public officers (s 13). Such a person may still complain to the Crime and Corruption Commission under its own Act (s 19(8)(b) says as much for s 19). Asserted.
11. **A reprisal against a person believed to be a discloser is still a reprisal.** s 40(1) covers detriment caused "because, or in the belief that" the person or "someone else" made or intends to make a disclosure. The question's input is worded to include the belief.
12. **Only a public service employee may apply for relocation (s 47).** Local government, hospital and GOC employees have no such right under this Act. Asserted as `not covered`.
13. **The schedule numbering has a gap and the dictionary has struck entries.** Schedule 3 is absent and several dictionary entries ("agricultural college", "corporate entity", "official misconduct", "university" and others) are shown as "...". Both are repeal artefacts of the conversion; no answer turns on them.

## Raised in the ledger

Nothing. Queensland has no requirement ledger, no ledger entry named this Act, and no scenario life cites it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit and encode the Acts Interpretation Act 1954 rules on time (finding 9), and the Anti-Discrimination Act 1991 complaint process.
- Add s 31(3), (4) (the reprisal risk on referral) and a seat for the person who is the subject of a disclosure, and one for the employer facing a s 43 claim.
- A lawyer's view on findings 2, 3, 4, 5 and 6 and forks F10, F15 and F17, an independent test pass, and a human gate.
