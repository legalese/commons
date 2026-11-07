# Supreme Court Act 1986 (Vic), Part 4A -- baseline encoding, the group member and the representative plaintiff

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`gp-part4a.l4`); each
seat asks its questions from its own module, importing the rules, so the two seats cannot disagree about the law.

## Edition

- **Act:** Supreme Court Act 1986, Act No. 110/1986, Version No. 113, incorporating amendments as at 15 April 2026,
  deposited at `../../registers/source-bundle/supreme-court-act-1986.txt` (sha256 805d8413...4186880a since the 2026-11-07 reconversion; encoded from d3cf698a...b88c7e, which differs only in the decimal point noted in finding 10), a
  plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** Part 4A fixes no amounts. The percentage of a group costs order is the Court's, the limitation
  period comes from the Limitation of Actions Act 1958 (not deposited), and the time for an appeal from the rules of court
  (not deposited): all three are asked.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once to confirm that a failure shows as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `gp-dates.l4` | 0 | 0 | 0 | 0 |
| `gp-part4a.l4` | 0 | 0 | 0 | 0 |
| `gp-seat.l4` | 0 | 0 | 0 | 0 |
| `gp-seat-plaintiff.l4` | 0 | 0 | 0 | 0 |
| `gp-cases-member.l4` | 0 | 0 | 106 | 106 |
| `gp-cases-plaintiff.l4` | 0 | 0 | 38 | 38 |

Every expected value was worked by hand from the text, with the edges: 6 and 7 persons with claims; the day before and the
day of the opt-out date (and 29 February 2028); a cause of action accruing on the day of commencement, the day after, and on
the date fixed with leave; the s 33ZE day count across a leap year and with the last day on the day of commencement and the
day before; the step taken on the day of the order, on the date and the day after; the fund claim on the day fixed and the
day after; the 21 further days for an appeal (the first and last day, and across the new year); the month-end cases of
"6 months or more"; the s 33ZJ excess at $1 and $0. Seven mirror cases put the same facts to both seats.

## Seats

**First seat: the group member** (`gp-seat.l4`): a person with a claim who is, or may be, a member of the group on whose
behalf a group proceeding (class action) is brought in the Supreme Court of Victoria. "Can my claim be brought as a group
proceeding?", "Am I a group member?", "By when must I opt out?", "What happens to my time limit?", "What costs can I be made
to pay?", "How much of my recovery goes in legal costs?", "Must I be given notice?", "Where do I stand on the step the
Court set?", "Is my fund claim in time?", "Am I bound by the judgment?", "May I appeal for the group?".

**Second seat: the representative plaintiff** (`gp-seat-plaintiff.l4`): the person with a claim who commences the group
proceeding as representative party, or is substituted as plaintiff (s 33A). Also an individual, and the person the Part
puts its costs and settlement rules on. "Can I bring a group proceeding for us all?", "May I continue after my own claim
ends?", "Who answers for the defendant's costs?", "May the Court make a group costs order on my application?", "How much of
my costs can come out of the damages?", "May I settle my own claim, and stop being the plaintiff?".

No seat for the Court or for the defendant (the defendant is usually a company, and Part 4A's defendant-side provisions,
ss 33M, 33N, 33U, are applications to the Court whose outcome is the Court's). The Court's findings, leave, approvals and
orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: no instrument sets a Part 4A number; the
  percentage, the limitation period's last day and the appeal time are inputs.
- **The actors the text names.** Followed: the plaintiff, group members, sub-group representative party, the defendant,
  the law practice, the Court.
- **Judgments answered conditionally.** Followed: "substantial common question", "sufficient interest", "satisfied that
  it is appropriate or necessary to ensure that justice is done", "if it is just", leave, approval and orders are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: group member (s 33A with ss 33E, 33J, 33KA), person
  under disability and handicapped person (s 33A), group costs order (s 33ZDA(5)) are worked out; minor (asked as under 18),
  sufficient interest, legal costs (Legal Profession Uniform Law) and the limitation period are asked or taken as given.
- **One case.** One group proceeding, seen by one person.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope). The focus asked for is Part 4A and s 33ZDA; the rest of
  the Act (the Court's constitution, divisions, officers, and Parts 5-8) is out.

## Scope

**In (Part 4A, nearly whole):** ss 33A (definitions), 33B(2), 33C(1), (2) (as not asked), 33D, 33E, 33F, 33G, 33J(1)-(3),
(5) (read with s 33ZE), (6), 33K(1)-(3), 33KA(1), (3), 33P, 33Q(3), 33R(2), 33V(1), 33W(1), (2), (4), 33X(1)-(6), 33Y(7) (in
the notice question's description), 33ZA(3)(c), (4), 33ZB, 33ZC(5), 33ZD, 33ZDA(1)-(3), (5), 33ZE, 33ZG, 33ZJ.

**Regulative rules:** two. s 33ZG (the group member MUST take the step the order sets out WITHIN the days to the date, LEST
breach: not entitled to the relief, payment or benefit) and s 33ZA(3)(c) (the group member is to claim from the fund WITHIN
the days to the day fixed, LEST a later claim only under s 33ZA(4)). Both run by EVALTRACE inside exported questions that
take only dates and facts, through a helper copied in shape from the Accident Compensation Act 1985 encoding.

**Out, and why:**
- s 33B(1) (causes of action before or after 1 January 2000): every cause of action is in; nothing to ask.
- s 33H (the writ's indorsement), s 33Y(1)-(6) (form, content and manner of notices), s 33ZC(1)-(4), (6)-(8) (who the
  parties to an appeal are): forms and procedure for the lawyers and the Court; nothing a member decides.
- s 33J(4) (trial not before the opt-out date), s 33K(4), s 33KA(2) (grounds), ss 33L, 33M, 33N (the Court may stop the
  proceeding continuing under Part 4A): the Court's judgments on the defendant's or its own motion; their consequence for
  the plaintiff is encoded through s 33P(a). s 33P(b) (a former member may apply to be joined) is a bare power of the Court.
- ss 33Q(1), (2), 33R(1), 33S, 33T (directions, sub-groups, substitution of the plaintiff), s 33U (stay of execution),
  s 33V(2), s 33W(3), (5), s 33Z (the heads of judgment), s 33ZA(1), (2), (3)(a), (b), (d), (5), ss 33ZF, 33ZH: powers of
  the Court with no fact test for the person; the costs consequences of ss 33Q and 33R are in.
- s 33ZDA(4) (effect despite the Legal Profession Uniform Law): a rule of priority, noted.
- s 33ZK (transitional, proceedings under the 1996 Rules in 2000): spent.
- The rest of the Act. Of most use to claimants next would be s 101 (interest on judgment debts at the Penalty Interest
  Rates Act 1983 rate, not deposited) and Part 5 Division 7 (interest).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 33J(2) "before the date so fixed" -- `s 33J(2) -- the last day to opt out`, `s 33J(2) -- I may opt out today` --
  the last day is the day before the date fixed -- a notice posted or sent on the last day but received on the date.
- **F2** s 33X(2) -- `s 33X -- notice of the matter must be given to me` -- a dispensation given where damages are claimed
  is not effective, so notice is still required -- the order stands until set aside.
- **F3** s 33K(2) -- `s 33K -- the group may be altered to include me` -- without leave the answer is JUST FALSE (only an
  amendment with leave includes the person) -- NOTHING (the section is silent on the person until leave is sought).
- **F4** s 33ZDA(1) "On application by the plaintiff" -- `s 33ZDA(1) -- the Court may make a group costs order` -- no
  application, no power: JUST FALSE -- NOTHING, as a scope limit without "only" (2026-11-05 ruling (c)).
- **F5** s 33ZDA(1)(b) "shared among the plaintiff and all group members" -- `s 33ZDA(1)(b) -- my share under the group
  costs order` -- a person's share is computed only where the order shares in proportion to recovery, else NOTHING -- pro
  rata as the default reading of "shared".
- **F6** s 33ZE -- `s 33ZE -- my limitation period` -- the days from the day of commencement to the day of the opt-out (or
  the final determination) are added to the last day -- the day of commencement or the day of resumption counted as a day
  of running.
- **F7** s 33ZA(3)(c) "6 months or more after" -- `the date` n `months after` -- the same day of the month 6 months on, or
  that month's last day where it is shorter (31 August -> 28 February) -- the first day of the next month.
- **F8** s 33ZC(5) "does not commence an appeal within the time provided ... within a further 21 days" -- `s 33ZC(5) -- I
  may appeal as representative today` -- while the representative's time runs a member may not appeal (JUST FALSE), and the
  21 days run from the day after the representative's last day -- the member may appeal at any time up to 21 days after.
- **F9** s 33ZB "subject to section 33KA" -- `s 33ZB -- the judgment binds me` -- an order after judgment that the person
  cease to be a member and be taken never to have been one releases them (JUST FALSE) -- it operates only from the order.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "does not apply" (s 33B(2)), "may not be commenced" (s 33G), "is a group member unless" (s 33E(2)), "may not
order" (s 33ZD(1)(b)), "may not be settled ... without" (s 33V), "must not be made unless" (s 33W(4)), "may only" (s 33F(2)),
the "if" conditions of ss 33C(1), 33X(3), 33ZA(4), 33ZDA(1), 33ZJ, and the periods "before the date so fixed" (s 33J(2)),
"within a further 21 days" (s 33ZC(5)) and the s 33ZG date give `JUST FALSE`; the Legal Profession Uniform Law and the terms
of a group costs order give `NOTHING` (*points outside the text*, *silent*); ss 33D(2), 33F, 33K, 33P, 33W(2) outside the
persons or events they speak of give `NOTHING` (*limited by its own wording*). s 33ZE outside its reach answers "not
suspended by s 33ZE" (this section gives no suspension on these facts), in the manner of ruling (b) on defences.

## What the Act turns out to say

1. **"Chapter I of the Rules" points at revoked Rules.** s 33A defines it as "the Supreme Court (General Civil Procedure)
   Rules 2015", which were revoked (last version 052, to 31 March 2025) and replaced by the Supreme Court (General Civil
   Procedure) Rules 2025 (`subjects/au/vic/README.md`). s 33B(2)(c) (no group proceeding under Order 18 of Chapter I) and
   the s 33A definition have not been updated in Version No. 113; whether the Interpretation of Legislation Act 1984 carries
   the reference over to the 2025 Rules is a question for a lawyer. Encoded as the excluded kind "a proceeding commenced
   under Order 18 of Chapter I of the Rules", whichever Rules that is.
2. **Opting out and the limitation period.** s 33J(5) says a person who opts out "must be taken never to have been a group
   member" unless the Court orders otherwise; s 33ZE(1) suspends the limitation period only for "the claim of a group
   member". Read literally together, an opt-out would undo the suspension back to commencement, yet s 33ZE(2) says the
   period "does not begin to run again unless ... the member opts out", which only makes sense if the suspension survives.
   Encoded on s 33ZE(2): the period runs again from the opt-out, with the suspended days added. Asserted (10 March 2027).
3. **A substituted plaintiff has no s 33D(2).** s 33D(2) keeps standing for a person who "has commenced" the group
   proceeding. A group member substituted as plaintiff under s 33T(1) or s 33W(3) is a "plaintiff" by s 33A but did not
   commence it; if their own claim ends, s 33D(2) is silent. Answered `NOTHING`. Asserted.
4. **Group costs orders: who else is liable, and in what shares.** s 33ZDA(2)(a) makes the law practice "liable to pay
   any costs payable to the defendant" but does not say that the plaintiff ceases to be liable under s 33ZD(1)(a); and
   s 33ZDA(1)(b) makes the legal costs "shared among the plaintiff and all group members" without saying in what shares.
   The encoding names the law practice and computes a person's share only where the order shares by recovery (F5).
   Asserted.
5. **No limit on the percentage.** s 33ZDA fixes no maximum or minimum percentage and no matters the Court must weigh,
   beyond "appropriate or necessary to ensure that justice is done"; the percentage is wholly the Court's and may be
   amended during the proceeding (s 33ZDA(3)). Asserted only as arithmetic (25% of $10,000,000 is $2,500,000).
6. **s 33ZD(1)(b) "authorised by section 33Q or 33R".** ss 33Q(3) and 33R(2) do not authorise an order; they state that the
   sub-group representative or the individual member "is liable" for certain costs. Encoded as liability. Asserted.
7. **s 33X(4) is a bar, not a duty.** It forbids determining a settlement approval without notice "unless the Court is
   satisfied that it is just to do so"; it does not itself say notice must be given. Encoded as "notice must be given unless
   the Court is satisfied", which is its practical effect for the member. Asserted.
8. **s 33K(2)(b) is hard to parse.** "who would have been included in the group or, with the consent of the person would
   have been included in the group" lacks a comma after "person"; read as covering a person who would have been included
   only with their consent (a person in s 33E(2)). Asked as one fact.
9. **No step to be in the group.** Membership needs no consent or act (s 33E(1)), not even for a person under disability
   (s 33F(1)); the first thing a member must do is opt out, if they want out, by the date the Court fixes. Asserted.
10. **Reconverted, 7 November 2026.** The converter that made the first deposit dropped the Word file's Symbol-font
    characters, which here were only the raised decimal point of "0·10%" in s 113(21) (the Common Funds Guarantee and
    Reserve Account), printed twice as "010%". The text was reconverted with the fixed converter and the decimal point is
    restored; no multiplication or minus sign or bullet was lost. The encoding does not rely on s 113 (the
    Common Funds, in Part 7, is out of scope), so no value, case or finding changed.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Limitation of Actions Act 1958 (for the last day s 33ZE extends) and the Supreme Court (General Civil Procedure)
  Rules 2025 (Order 18 and the appeal times), neither deposited.
- The Legal Profession Uniform Law (Victoria) and its Application Act (for "legal costs" and the costs regime outside a group
  costs order).
- A lawyer's view on findings 1, 2 and 4, an independent test pass and a human gate.
