# Native Title Act 1993 (Cth): claimant and compensation applications, registration, the right to negotiate and compensation (baseline encoding)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied. It follows the design defaults
ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

The encoding has three files:

- `nt-claims-dates.l4`: date arithmetic with the built-in date functions, not the daydate library.
- `nt-claims.l4`: the rules and the 23 exported questions, each with `@export` and a `@desc` on every input.
- `nt-claims-cases.l4`: the worked cases.

The duties with deadlines the person meets are regulative rules (`PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST
BREACH ... BECAUSE`). Each is run by `EVALTRACE` inside a question that takes only plain facts:

- ss 66(10)(c) and 84(3)(b): notify the Federal Court in writing within the period of 3 months starting on the
  notification day, to become a party to proceedings on an application over land one claims;
- s 30(1)(a)(i): file the claimant application before the end of 3 months after the notification day of a s 29 notice,
  to become a native title party with the right to negotiate;
- s 190E(2)(b): apply to the NNTT for reconsideration within 42 days after the Registrar's s 190D(1) notice.

No question takes a DEONTIC or an EVENT. This is the first encoding of the Act in Commons; there is nothing beside it.

## Edition

- **The Act:** Native Title Act 1993 (No. 110, 1993), Compilation No. 50, compilation date 12 June 2024, includes
  amendments to Act No. 41, 2024 (register id C2024C00224). Deposited at
  `../../registers/source-bundle/C2004A04665.txt` (retrieved 13 October 2026).
- **Not deposited:** the Native Title (Federal Court) Regulations and the Federal Court Rules (the prescribed form,
  information, documents and fees under s 61(5); any time limit for review under s 190F); the Acts Interpretation Act
  1901 (the counting of periods: forks F4, F5, F7); State and Territory laws that confirm extinguishment (ss 23E, 23I)
  or correspond to s 29 (ss 43, 43A). Each is an input or left out, as said below.

## Checks

- Stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. Commands: `l4 run nt-claims-dates.l4`,
  `l4 run nt-claims.l4`, `l4 run nt-claims-cases.l4`.
- **135 assertions written, 135 satisfied, 0 errors, 0 warnings** in every file (2026-11-07, after the fix below).
- Every expected value was worked by hand from the text before the file was run, and none was copied from the
  encoding's output. All 129 passed on the first run of the cases file (after two missing date names were added).
- In a scratch copy, the s 66(10)(c) last day for a notification day of 15 January 2026 was changed from 14 April 2026
  to 15 April 2026. The run reported one error, so the runner catches a wrong expectation.
- **Fix after independent verification (2026-11-07).** The verifier found that month counting went wrong where the
  notification day is the last day of a short month. The first version reused the start day's day of the month even
  when the period starts the next day, and clamped a missing day before subtracting one. Two hand-worked expectations
  were a day off: the s 66(10)(c) last day for 30 November 2025 (asserted 27 February 2026; it is 28 February 2026) and
  the s 30(1)(a) registration day for 30 November 2025 (asserted 30 March 2026; it is 31 March 2026). The same fault made
  s 32(3) end a day early and s 35(1) open a day early from such a day. The dates module now counts months as Acts
  Interpretation Act 1901 ss 2G and 36(1) count them (fork F1), both expectations are corrected, and six assertions were
  added for month-end start days (ss 32(3), 35(1), and the two dates functions). The s 66(10)(c) duty now names the
  person who wants to be a party, not the applicant (who is a party already under s 84(2)). The s 30(1)(a)(i) filing
  input now also covers an application given to a recognised State/Territory body.

## Seat

**A member of the native title claim group, or of the compensation claim group, including the person or persons the
group authorises to be its applicant.** The person asks:

- "Can the person we chose apply for a determination of our native title?" "Can we claim over land that was once
  leased, reserved or granted?"
- "Will the Registrar register our claim? If not, why, and what can we do, and by when?"
- "Someone else has applied over our country: am I a party? By when must I tell the Court?"
- "Can I replace our applicant?"
- "The government wants to grant a mining lease: are we a native title party? Can it go ahead without negotiating with
  us? When can we go to the arbitral body? Is our applicant bound by the agreement? Can I enforce its conditions?"
- "Can we claim compensation, on what basis, how much at most, and can it be land or services instead of money?"

The Federal Court, the Native Title Registrar, the NNTT, the arbitral body and the Ministers get no seat. Their
satisfactions, opinions and determinations are asked as facts. The Government party and the grantee party are parties
the Act puts duties on (notice, good faith negotiation); no seat was written for them (see "Before this is worth relying
on").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Act's own periods (3, 4 and 6 months,
  42 days) are its own; no deposited instrument sets a number these provisions use.
- **The actors the text names.** Followed: the native title claim group and compensation claim group, the applicant,
  registered native title claimants and bodies corporate, representative bodies, the Registrar, the NNTT, the arbitral
  body, the Federal Court, the Government party, the grantee party, the negotiation parties, the relevant Minister.
- **Judgments handed to someone else are answered conditionally.** Followed. Each of these is an input: every s 190B
  and s 190C satisfaction of the Registrar; the s 190A(6A) satisfaction about an amendment; the Court's s 190F(3)
  satisfaction; the arbitral body's s 32(4) determination and its s 36(2) satisfaction about good faith; the s 84(5)
  joinder; the s 51(6) recommendation; the s 53 just terms amount.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: authorisation (s 251B), the s 61A
  restrictions, the ss 47-47B conditions, the s 190A(6) test, native title party (ss 29(2)(b), 30(1)(a), (2)), the
  s 31(1C) majority. Asked: previous exclusive and non-exclusive possession acts (ss 23B, 23F) and the State
  confirmation (ss 23E, 23I), the similar compensable interest test (s 240), the compulsory acquisition law, the
  freehold acquisition amount, resumption process and public purpose reservations (s 47B), occupation.
- **One case is the text's natural unit.** Followed: one application and one claim group; one proposed act and one
  notice; one compensable act.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**

- **Part 3 Division 1:** s 61(1) (native title determination and compensation applications, the rows for a claim group
  and a registered native title body corporate), (2); s 61A(1)-(4); s 66B(1), (2), (2A), (2B) (in an answer); s 66(10)(c)
  with s 84(2), (3), (5).
- **Part 2 Division 3 Subdivision P:** ss 29(2)(b)(i), (4); 30(1)(a), (2); 31(1)(b) (in answers), (1C), (1D); 32(2)-(7);
  33(1) (in an answer); 35(1)-(3); 36(2); 37; 38(1), (2); 41(1), (2).
- **Part 2 Division 4 (in part):** ss 47, 47A, 47B (when earlier extinguishment is disregarded).
- **Part 2 Division 5:** ss 49 (in a comment), 50(2), 51(1)-(8), 51A, 53(1).
- **Part 7:** ss 190A(2), (2A), (6), (6A), (6B); 190B(2)-(9); 190C(2)-(5); 190D(1), (2) (as the trigger); 190E(1)-(4);
  190F(1), (3).
- **Part 15:** s 251B.

**Out, and why:**

- **Who may make the other kinds of application** (non-claimant applications by a non-native title interest holder,
  Ministers' applications, revised determination applications, Division 1A and 2A applications): not this seat's.
- **s 62 (the content of the application and affidavit)** and **s 61(3)-(5)** (form, filing, fees): a checklist the
  applicant meets; folded into the s 190C(2) input ("has everything ss 61 and 62 require"). The prescribed form and fees
  are in regulations and rules not deposited.
- **s 47C** (park areas, by written agreement with the government): it turns on an agreement and its terms; named as
  not encoded in the ss 47-47B answer.
- **The future act regime (Division 3 Subdivisions B-N, Q) and the ILUA provisions:** which acts are valid, and the
  procedural rights other than the right to negotiate. A large separate layer. Whether Subdivision P applies to an act
  (ss 26-26D, 43, 43A) is assumed: a s 29 notice is the starting fact.
- **ss 26A-26D, 27-28, 31(1A), (1B), (2)-(4), 33(2), 34, 36(1), (3), (4), 36A-36C, 38(1A), (1B), 39, 40, 41(3)-(5),
  41A-44:** the arbitral body's and Ministers' procedure and criteria, and the s 36A ministerial route (asked as a fact).
  s 39's criteria go to a determination that is an input.
- **ss 52, 52A (bank guarantees and trust payments):** obligations of the grantee and the Registrar.
- **Validation and extinguishment rules (Part 2 Divisions 2-2B, ss 23A-23JA):** whether an act extinguished native
  title is asked as a fact.
- **ss 190A(1), (1A), (3)-(5A), (7), 190D(3), 190E(5)-(13), 190F(2), (4)-(6):** the Registrar's and the NNTT's
  procedure; s 190F(6) dismissal is mentioned in a comment.
- **ss 66(1)-(9), 84(1), (4), (5A)-(9):** notice by the Registrar, Ministers as parties, and the Court's management of
  parties.
- **ss 62A (the applicant's power to deal with matters arising), 64 (amending applications), 66A (notice of the
  application to the Commonwealth Minister and others) and 66B(3), (4) (the Registrar's steps after a replacement
  order):** machinery of the proceedings once the application is made, or duties of the Registrar. A member meets
  s 62A and s 64 only through the applicant the group authorised.
- **Parts 4-6 and 8-12 (Federal Court procedure, mediation, the NNTT, the registers, representative bodies and
  prescribed bodies corporate):** machinery, or duties of bodies the seat does not occupy.
- **No requirement-ledger entry exists for these provisions** in `subjects/au/requirements.jsonl`, and none was
  raised: no scenario life has reached them. The encoding's priority came from the claims-law baseline request.

## Fork register

Each line gives the provision, the function, the answer taken, and the other reading.

- **F1** Months from a day (ss 29(4), 30(1)(a), 32(3), 35(1), 66(10)(c), 190A(2)). Functions: `the last day of ...
  months starting on` and `plus calendar months` (nt-claims-dates.l4) and every function that uses them. Answer taken:
  the Acts Interpretation Act 1901 (not deposited) counts a month from the start of a day to just before the start of
  the corresponding day of the next month, or to the end of that month if it has no such day (s 2G), and a period
  "after" a day starts the next day (s 36(1)). So a period of months starting on a day ends the day before the
  corresponding day that many months on, or at the end of that month if it has no such day (30 November 2025, 3
  months: 28 February 2026); a period of months after a day is counted the same way from the next day (31 October 2025
  plus 4 months: 28 February 2026; 30 November 2025 plus 4 months: 31 March 2026). A period of several months is
  counted straight to the corresponding day that many months on. Other reading: chain the months one at a time, which
  can move the end of a period that starts on the 29th, 30th or 31st.
- **F2** s 61A(2), (3) "previous exclusive possession act" and the State provision "as mentioned in section 23E" (and
  23F, 23I). Functions: `s 61A -- what it says about our application`, `s 61 -- can we make a native title
  determination application`. Answer taken: asked as facts, one input each, folding in whether the act is attributable
  to the Commonwealth or confirmed by State or Territory law. Other reading: work ss 23B-23I out from the grant's kind
  and date (a separate layer).
- **F3** s 61(1) table, "the persons who may make each of those applications". Functions: the two s 61 questions.
  Answer taken: the table closes the list, so a person not listed (an authorised person outside the group; a group
  member not authorised) gets the text's no. Other reading: the table is a list without "only", and the answer is
  NOTHING-kind. The proviso ("provided the person or persons are also included") is itself a condition, so the first
  branch is the text's no on either reading.
- **F4** s 190E(2)(b) "within 42 days after the notice ... is given". Function: `s 190E -- can I apply for
  reconsideration`. Answer taken: the day the notice is given is day 0, the last day is that day plus 42 (1 June 2026
  gives 13 July 2026). Other reading: the day of receipt rather than the day of giving starts the count, which needs a
  further fact.
- **F5** Three ways of counting 3 or 4 months from the notification day. Functions: `s 66(10)(c) -- the last day to
  notify the Federal Court`, `s 30(1)(a) -- the last day to file and the day to be registered by`, `s 32(3) -- the last
  day to object` and the questions that use them. Answer taken: "the period of 3 months starting on the notification
  day" (s 66(10)(c)) includes that day and ends the day before the same day 3 months on; "before the end of 3 months
  after the notification day" (s 30(1)(a)(i)) and "within the period of 4 months after the notification day" (s 32(3))
  start the day after and end on the same day 3 or 4 months on (at a month end, as F1 counts it). Other reading: all
  three end on the same day (finding 2).
- **F6** s 66B(1) "on the grounds that". Function: `s 66B -- can I apply to replace the applicant`. Answer taken: the
  three grounds in (1)(a) are closed, so with none of them (and no death or incapacity) the answer is the text's no.
  Other reading: NOTHING-kind, leaving the Court's general powers.
- **F7** s 35(1)(a) "at least 6 months have passed since the notification day". Function: `s 35(1) -- the first day to
  apply for a determination`. Answer taken: the 6 months end with the day 6 months on, so the first day to apply is the
  day after (15 January 2026 gives 16 July 2026). Other reading: the day 6 months on itself.
- **F8** s 51A(2) "subject to section 53". Function: `s 51A -- the most compensation for extinguishing all native
  title`. Answer taken: the cap is the greater of the freehold acquisition amount and the amount s 53 requires for just
  terms. Other reading: s 53 is a separate entitlement against the Commonwealth or State, and the Division 5 total stays
  capped while s 53 pays the rest; the total the person receives is the same.
- **F9** s 30(1)(a) "4 months after the notification day, is a registered native title claimant". Function: `ss 29, 30
  -- are we a native title party`. Answer taken: the claim was entered on the Register on or before the day 4 months on
  and is still on it. Other reading: registration at any time during that day (the same answer on a day count).
- **F10** s 41(2) for a person who is neither a negotiation party nor in the claim group of a registered claimant party.
  Function: `s 41 -- can I enforce the conditions as contract terms`. Answer taken: NOTHING-kind (s 41 is silent about
  them; the general law of contract may still apply). Other reading: the text's no.
- **F11** The order of the bars. Functions: the two s 61 questions, `ss 29, 30 -- are we a native title party`, `s 32 --
  can the act go ahead without negotiating with us`, `ss 36-38 -- what the arbitral body must do on our application`.
  Answer taken: the first bar met is reported, in the order the text gives them. Other reading: all reported together.
  The registration question does report every failed condition.
- **F12** s 190A(6A) with an amended application. Function: `ss 190A-190C -- will our claim be registered`. Answer
  taken: when (6A) holds, the claim is accepted whatever the s 190B and 190C inputs say; when it does not, the amended
  claim is tested under (6). Other reading: none needed; (6)(a)(ii) says so.

**Sites decided without a fork line:**

- The text's no, for these flat negatives: s 61A(1)-(3) "must not be made", s 190A(6B) "must not accept", s 190E(3)
  "may not", (4) "no more than once", s 37 and s 36(2) "must not make", s 38(2) "must not determine".
- The text's no, for these conditions: s 251B "if ... where", ss 47(1), 47A(1), 47B(1) "applies if", s 84(3) "if",
  s 30(1)(a) "so long as", s 30(2) "ceases ... if", s 31(1C) "is satisfied if", s 35(1) "if", s 41(1) "if the act is
  done", s 190F(1) "provided", s 51(5) "may only".
- s 51A for an act that does not extinguish all native title: NOTHING (a scope limit, no "only").

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries a `NOTHING-kind` tag in the s 41 question (F10) and returns NOTHING from `s 51A -- the most
compensation for extinguishing all native title`. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (ss 66(10)(c), 30(1)(a)(i), 32(3), 35(1)(a), 190E(2)(b)) answer the text's no outside the
period, with the consequence the text gives: leave of the Court needed, no native title party, no objection, not yet,
or out of time.

## What the Act turns out to say

1. **A claimant meets two deadlines to get the right to negotiate, but the notice mentions only one.** s 29(4)(b)
   requires the notice to say that persons "have until 3 months after the notification day" to take steps to become
   native title parties. Under s 30(1)(a) filing within the 3 months is not enough: the claim must also be on the
   Register of Native Title Claims 4 months after the notification day, and registration is the Registrar's decision.
   s 190A(2)(f) asks the Registrar to use best endeavours to finish by then, but the claimant bears the risk of delay.
   Asserted (N4: filed in time, registered a day late, no).
2. **Two 3-month periods from the same notification day end a day apart.** To become a party to proceedings, "the period
   of 3 months starting on the notification day" (s 66(10)(c)) includes the notification day; to become a native title
   party, the application must be filed "before the end of 3 months after the notification day" (s 30(1)(a)(i)), which
   on the usual counting starts the next day. For a notification day of 15 January 2026 the last days are 14 April and
   15 April 2026. The two notices are different notices (s 66 and s 29), but a claimant can easily confuse them. Asserted.
3. **A failed reconsideration deadline does not close the door to the Court, and the Court has no deadline in the
   Act.** s 190E(2)(b) allows 42 days; s 190F(1) sets no time limit, only that the NNTT not be reconsidering at the
   time. Any limit is in the Federal Court's rules (not deposited). Asserted (the out-of-time answer points to s 190F,
   and the review answer says the Act sets no limit).
4. **s 30(1)(a) can make a registered claimant a native title party where s 29(2)(b) gives it no notice.** s 29(2)(b)
   withholds notice from registered claimants where registered native title bodies corporate cover all of the affected
   land, but s 30(1)(a) has no such exception. Read literally, a claimant whose claim relates to any of the affected land
   and is registered at 4 months is a native title party. Since s 61A(1) bars new claims over determined areas, this
   bites only on claims made before a determination, or claims that also cover land outside it. Asserted (N9).
5. **Only the other side's bad faith stops an arbitral determination.** s 36(2) applies where "any other negotiation
   party (other than a native title party)" did not negotiate in good faith. A native title party's own conduct cannot
   be used to stop the determination. Asserted (the bad faith input is worded for the government or grantee).
6. **The arbitral body cannot award a share of profits, but an agreement can.** s 38(2) forbids a condition paying
   native title parties by reference to profits, income or production; s 33(1) lets negotiations include one. The
   claimant's bargaining position on a royalty-style payment is therefore only in the negotiation. Stated in the s 38
   answer.
7. **Exactly half is not a majority.** s 31(1C)(a) binds the registered native title claimant if "a majority" of the
   persons comprising it are parties. With an even number of joint applicants, half is not enough. Asserted (3 of 6
   no, 4 of 6 yes). Where s 251BA conditions name who must sign, the majority rule gives way entirely, even if more
   than a majority signed. Asserted (6 of 7, not all the named persons, no).
8. **The freehold cap on compensation is not a hard cap.** s 51A(1) limits compensation for an act extinguishing all
   native title to what a compulsory acquisition of freehold would attract, but s 51A(2) makes it subject to s 53, which
   tops up to constitutional just terms. Asserted at the freehold amount, one dollar over it and below it.
9. **s 61A(4) needs the application to say it.** The ss 47-47C exceptions to s 61A(2) and (3) apply only if the
   application "states that section 47, 47A, 47B or 47C ... applies to it". An application that leaves this out is
   barred even where the facts satisfy the section. The encoding folds the facts and the statement into one input,
   whose `@desc` says so.
10. **Gaps in the numbering.** s 39(1) runs (a), (b), (c), (e), (f), and s 66B(1)(a) runs (i), (iii), (iv): paragraphs
    removed by amendment. No effect on the encoding; noted so a reader does not look for them.
11. **The court's physical connection test is easier than the Registrar's.** s 190B(7) needs a member who has or had a
    traditional physical connection (or would have but for the Crown, a statutory authority or a leaseholder); s 190F(3)
    lets the Court order registration if one parent of one member had such a connection at some time in his or her
    lifetime. Asserted (the s 190F(3) route).

## Before this is worth relying on

- An independent test pass, and a lawyer's review of the fork register (especially F3, F5 and F7, which move a
  deadline by a day or turn a no into a NOTHING).
- The Acts Interpretation Act 1901 deposited, to settle the counting of periods (F4, F5, F7).
- The Native Title (Federal Court) Regulations and the Federal Court Rules deposited, for the s 61(5) form and the
  s 190F time limit, if any.
- A layer for ss 23A-23JA (previous exclusive and non-exclusive possession acts), so that F2's inputs can be worked out.
- A layer for the other future act procedural rights (Subdivisions G-N) and ILUAs, which a claimant meets as often as
  the right to negotiate.
- Seats for the Government party and the grantee party under Subdivision P, with mirror cases on the notification day
  and the good faith duty.
