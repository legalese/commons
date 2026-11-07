# Queensland Civil and Administrative Tribunal Act 2009 -- baseline encoding, the applicant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The focus is **the provisions a person
bringing a claim or application to the tribunal meets**: the minor civil dispute jurisdiction, reasons for and review of
government decisions, starting a proceeding, representation, ending early, decisions by default, settlement, costs,
reasons for the tribunal's decision, enforcement, renewal, reopening, stays and appeals. The Act is a procedural Act
of about 300 sections; its establishment, membership, registry, offences, rules and transitional chapters are out
(see Scope).

Files: the dates in `qcat-dates.l4` (built-in date functions only, no daydate), the rules and the exported questions
in `qcat-applicant.l4` (each exported question calls a rule defined beside it or is the rule), and the worked cases in
`qcat-cases-applicant.l4`.

## Edition

- **Act:** Queensland Civil and Administrative Tribunal Act 2009 (Qld), Act No. 23 of 2009 (`act-2009-023`), the version
  in force from 22 October 2026, current on 6 November 2026, deposited at `../../registers/source-bundle/act-2009-023.txt`
  (text sha256 `4acebadcf0a585572d04f8d762ee0d9f27aac6be5816725be3460a29acd41ca2` per its `.meta.json`; a Windows checkout
  with CRLF line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the
  authorised PDF.
- **Numbers in the Act itself:** the prescribed amount of $25,000 (schedule 3); 28 days (ss 33(3), 143(3), (4)(b),
  151(2)(b), 158(4)); 14 days (ss 122(2), 158(3)); 45 days (s 122(3)); 7 days (s 86(3)); 21 days (s 143(4)(a)).
- **Number brought in from another Act:** 12 years, from the Limitation of Actions Act 1974 s 10(4), which s 130 applies to
  a final decision (fork F11; that Act is deposited under its own subject in this repository).
- **Not deposited, and asked as facts:** the QCAT Rules 2009 (the period to respond, the period for giving the
  application to the other parties, for renewal and reopening, the minor civil dispute costs and the costs scale); the
  QCAT Regulation (prescribed fees); every enabling Act (whether it sets another period, provides for costs, confers
  jurisdiction on a debt claim, or allows representation); "impaired capacity" (Guardianship and Administration Act
  2000); "Australian legal practitioner" and "government legal officer" (Legal Profession Act 2007).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied"; the other two files report
"Checking succeeded" with no diagnostics.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `qcat-dates.l4` | 0 | 0 | 0 | 0 |
| `qcat-applicant.l4` | 0 | 0 | 0 | 0 |
| `qcat-cases-applicant.l4` | 0 | 0 | 222 | 222 |

Every exported question has cases, with the edges: a debt of $25,000 and of $25,001; a fence claim of $25,000 and
$26,000; a tenancy matter of $100,000; each kind of claim; consumer and trader worked out from facts (a tenant and a
landlord, a business purchase, two traders, a trader suing a consumer, a professional, a company); the cap at, below and
over $25,000; a s 158 request on the day of notice, the 14th day and the 15th; the review deadline for each paragraph of
s 33(4), with statements given before and after they fell due, a s 159 order made, refused and undecided, the 28th day,
the 29th and an extension; ages 17 and 18 for representation and costs; a settlement withdrawal notice on the day of
filing, the 7th day and the 8th; reasons asked on the 14th and 15th day after a decision that takes effect on a later
day; 12 years from 29 February to a leap year and to 2100; each appeal route, leave requirement and excluded decision;
appeal deadlines across a year end and in a leap year; an outstanding request for reasons or reopening application.

## Seat

**The applicant** (`qcat-applicant.l4`): an individual who brings a claim or application to the Queensland Civil and
Administrative Tribunal -- a minor civil dispute (a debt, a consumer claim against a trader, damage to property caused
by a vehicle, a tenancy matter, a fences, trees or pool barrier dispute), an application in another original
jurisdiction, or an application to review a government decision -- and who may later need to enforce, renew, reopen
or appeal the decision. "Is my claim a minor civil dispute?", "By when must I apply?", "Can I have a lawyer?", "Can I
get a decision by default?", "Can I be made to pay costs?", "How do I enforce it?", "Can I appeal, and by when?". Two
questions also take the respondent's position where the text gives the same person rights either way (s 89 on a broken
settlement offer, and the appeal and reopening questions, which belong to any party).

The respondent and the decision-maker meet the same rules from the other side; no seat is written for them. No seat
for the tribunal, the principal registrar, the appeal tribunal or the Court of Appeal.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. Its numbers are in its own text, except the
  12 years s 130 borrows from the Limitation of Actions Act 1974 s 10(4), brought in (F11). The rules and regulation are
  not deposited; what they set is asked.
- **The actors the text names.** Followed: the applicant, the respondent, the decision-maker, the principal registrar,
  the tribunal, the appeal tribunal, the president and deputy president, the Court of Appeal.
- **Judgments answered conditionally.** "the interests of justice require", "reasonable excuse", "significant new
  evidence ... not reasonably available", "substantial injustice", whether the tribunal "could make a decision in the
  terms of the settlement", whether a person is "an appropriate person to represent", whether extending time would cause
  irremediable prejudice: all asked, never decided. Each "may" of the tribunal is answered as what the tribunal may do.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: schedule 3 "minor civil dispute", "consumer",
  "trader", "prescribed amount", "child" (from age), "reopening ground"; s 33(4) and s 143(5) "relevant day"; s 127 when
  a decision takes effect; s 129 "final decision" for enforcement. Asked: "impaired capacity", "Australian legal
  practitioner", "tenancy matter" (as a kind of claim), "liquidated demand", "judicial member" (as who decided).
- **One case.** One applicant's claim or application in one proceeding.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** See Scope.

## Scope

**In (34 exported questions):**
- Minor civil disputes: ss 11, 11A, 12, schedule 3 "minor civil dispute", "consumer", "trader", "prescribed amount" (is my
  claim a minor civil dispute); s 13(3)-(5) (the most the tribunal can order); s 14 (interest).
- Reasons for a reviewable decision: s 158(3) (by when I must ask; whether I can ask); s 158(4) (by when the
  decision-maker must answer).
- Starting: s 33(3)-(4) with ss 158, 159 (by when I must apply for review; am I in time, with s 61); ss 33(2), 35 (can my
  application be rejected); ss 36, 38 (has my proceeding started); s 37 (must I give a copy); s 61 (can the tribunal
  extend my time).
- s 43 (representation); s 46(1)-(2) (withdrawing); ss 46(3), 49 (starting again).
- ss 50, 50A (decision by default).
- ss 84-88 (can our settlement be made an order; the s 86(3) withdrawal day); s 89 (an accepted offer not kept).
- ss 100-103, 107 (costs); s 109 (security for costs).
- ss 122, 127 (written reasons: can I ask, by when, by when the tribunal answers).
- ss 129-132 (how to enforce); s 130 with the Limitation of Actions Act 1974 s 10(4) (last day to sue on the decision);
  ss 133, 134 (renewal).
- ss 136-140, schedule 3 "reopening ground" (reopening).
- ss 22(1)-(2), 51A, 138A, 145, 152 (does the decision keep operating).
- ss 139(5), 141, 142 (can I appeal to the appeal tribunal); s 143 (by when; am I in time, with s 61).
- ss 149, 150 (can I appeal to the Court of Appeal); s 151 (by when).

**Regulative rules:** four, each run by EVALTRACE inside an exported question that takes only plain facts (a CONSIDER on
an EVALTRACE matches FULFILLED only):
- s 158(3)(b): I DO ask the decision-maker for a written statement of reasons WITHIN 14 days;
- s 33(3): I DO file my application for review WITHIN the days from the relevant day to the 28th day after it;
- s 122(2): I DO ask the tribunal for written reasons WITHIN 14 days after the decision takes effect;
- s 143(3), (4): I DO file my appeal or application for leave WITHIN its period.
Each BREACH marks only that the time passed; not asking, not applying and not appealing are not wrongs.

**Out, and why:**
- ss 1-10, 15-21, 23-32 (objects, enabling Acts, jurisdiction generally, the review hearing and the decision-maker's
  duties, practice and procedure): the tribunal's functions and duties, giving the applicant no question answerable
  from facts beyond those in scope. s 21(2) (the decision-maker's 28 days to give the tribunal its reasons and
  documents) and s 23 (reconsideration) are noted, not encoded.
- s 34 (referrals): made under enabling Acts, not by an individual applicant on this Act alone.
- ss 39-42, 44, 45 (parties, intervention, joinder, interpreters, the duty to act quickly): s 45 has no deadline or
  sanction of its own (its consequences are ss 48 and 102, folded into the costs question, F9).
- ss 47, 48 (dismissal for an unjustified proceeding or for causing disadvantage): the tribunal's powers, turning on its
  view; their consequence for starting again (s 49) is in.
- ss 51 (setting aside a decision by default, on the respondent's application), 52-60, 62-83, 90-99, 110-121, 123-125,
  128, 135, 144, 146-148, 153-156: the tribunal's procedural powers, conferences, mediation, hearings, evidence,
  assessors, the form of decisions, correcting mistakes, transfer to the Court of Appeal, and how appeals are decided.
- s 126 (effect of a decision): noted in the answers, not a question.
- ss 157, 159, 160 (information notices, orders for reasons): the decision-maker's and the tribunal's duties; s 159 is
  used for the s 33(4)(c) relevant day.
- Chapters 4-10 and schedules 1-2 (establishment, members, registry, offences and contempt, rules, confidentiality,
  immunity, transitional provisions): machinery. s 213 (contravening a decision, 100 penalty units) binds the person
  who must comply, not the applicant; s 239 (contracting out void) is noted.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** Schedule 3, minor civil dispute 1(d), (f) -- `Is my claim a minor civil dispute` -- a tenancy matter and a pool
  barrier matter are minor civil disputes at any amount (the definition states none) -- an implied cap for tenancy
  matters from s 13(3).
- **F2** s 13(3) -- `What is the most the tribunal can order in my minor civil dispute` -- the smaller of the claim and
  $25,000 -- the cap alone ($25,000), the tribunal making the orders it considers fair and equitable (s 13(1)) without a
  ceiling at the amount claimed.
- **F3** "within N days after" (ss 33(3), 86(3), 122(2), (3), 143, 151, 158) -- `the day ... days after` -- the named
  day is not counted (Acts Interpretation Act 1954 s 38, not deposited), so the last day is that day plus N -- the
  named day counted, one day less.
- **F4** s 158(3)(a) "must be in writing" -- `Can I ask the decision-maker for reasons` -- a request not in writing is not
  a request under s 158: JUST FALSE -- a defective request still counts (a bare "must" not done).
- **F5** s 33(4)(b) and (c) -- `s 33(4) -- the relevant day` -- where a s 159 application was made, paragraph (c)
  governs -- the earlier of the (b) and (c) days.
- **F6** s 33(4)(b) "applied ... under section 158" -- same function -- a request made after the 14 days is not one
  under s 158, so the relevant day is the day of notice -- any request moves the relevant day.
- **F7** s 35(3), (8) -- `Can my application be rejected` -- with no ground the answer is "no" (s 35(8)'s "only if" read
  as governing the registrar too) -- "not covered" (s 35(3) a grant limited in its own words, ruling (c)).
- **F8** s 86(3) "within 7 days after the written terms are filed" -- `Can our settlement be made an order` -- a notice
  on the day of filing or on the 7th day after it counts; a notice after that does not stop the orders -- a late notice
  still weighs with the tribunal.
- **F9** ss 47(2)(c), 48(2)(c), 102 -- `Can I be ordered to pay the other party's costs` -- the costs orders of ss 47
  and 48 are folded into the "interests of justice" input -- separate questions on the s 47 and s 48 grounds.
- **F10** s 141 -- `Can I appeal to the appeal tribunal` -- the bar applies only to an appeal against the final
  decision, as its words say -- any decision in a proceeding with a reopening application pending.
- **F11** s 130 -- `What is the last day to bring an action on the decision` -- the 12 years of the Limitation of Actions
  Act 1974 s 10(4) are brought in as the number s 130 uses -- asked as an input, the default for a borrowed term.
- **F12** "12 years from the date" -- `the date ... years after` -- the last day is the same day 12 years on, and
  29 February in a year that has none is 28 February -- the day before the anniversary; 1 March.
- **F13** s 43(2)(b)(i) "child" -- `Can I be represented`, the costs questions -- worked out from age (schedule 3 "an
  individual under 18 years") at the time of asking -- age at the time of the proceeding or the order.
- **F14** s 109 and s 101 -- `Can I be ordered to give security for costs` -- for a child: "not covered" (finding 4) --
  "no", reading s 109(1) as unmet where costs cannot be awarded against the party.
- **F15** s 12(4)(b) "subject to paragraphs (c) to (f)" -- `Is my claim a minor civil dispute` -- a contract claim is
  open to the consumer (against a trader) and to either trader (between traders); a trader suing a consumer on the
  contract is answered "no" for paragraph 1(b) -- the trader may still claim the price as a debt under 1(a) (said in
  finding 1, not computed).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the schedule 3 "means" definitions, the "if" conditions of ss 12(1), 50(1), 50A(1), 86(3), 89(1), 122(1),
133(1), 158(1) and 43(2)(b), the "only" of ss 46(2), 87, 136, 142(3), 149(3), 150(3), the flat negatives of ss 43(4),
46(3), 49(2), 61(3), 101(1), 133(6), 134(4), 138(5), 139(5), 140(6), 141, 142(2), 149(4) and schedule 3 paragraphs 2-4,
and the periods of ss 46(1), 122(2), 143 and 158(3) give "no" or `JUST FALSE`; s 129's "includes" and s 150's open list
give "not covered"; a review where an enabling Act provides otherwise (s 22(2)(a)) and a time limit another Act sets give
`NOTHING`; s 158(3)(a)'s bare "must" is the case-by-case site F4.

## What the Act turns out to say

1. **Only the consumer can bring a consumer contract claim.** s 12(1) lets the tribunal hear a minor civil dispute only
   on a "relevant person"'s application, and s 12(4)(b) names, for a claim on a contract between a consumer and a
   trader, "the consumer". A trader whose customer has not paid must bring a debt claim (paragraph 1(a)) instead; a
   trader's claim for, say, return of goods from a consumer is not a minor civil dispute. Asserted.
2. **Tenancy matters have no limit in the definition but a cap on orders.** Paragraph 1(d) admits any tenancy matter,
   and s 13(3) still forbids an order over $25,000 (subsection (4) exempts only pool barrier matters), so a tenant with a
   larger claim is inside the jurisdiction yet cannot be awarded more. Asserted.
3. **Appeal time can run while an appeal is barred.** s 141 bars an appeal against a final decision until an
   application to reopen is dealt with, but s 143(5)(a) moves the relevant day only for an application made "within 28
   days after the person is given written reasons". With no written reasons, the 28 days run from notice of the decision
   (s 143(5)(b)) while s 141 stops the appeal; the applicant then needs an extension under s 61. Asserted. Relatedly,
   where reasons were requested under s 122 and must be given, no paragraph of s 143(5) gives a day until they are
   given (paragraph (c)). Asserted (NOTHING).
4. **Security for costs against a child is not addressed.** s 101(1) forbids costs against a child, yet s 109 lets the
   tribunal order "another party" to give security wherever it "may award a party's costs". Asserted (`not covered`).
5. **Every minor civil dispute appeal needs leave, even on law alone.** s 142(3)(a)(i) applies to "a decision in a
   proceeding for a minor civil dispute" without distinguishing the question. Asserted.
6. **A cost-amount decision goes only to the Court of Appeal.** s 142(2)(c) excludes it from the appeal tribunal, and
   s 149(1) allows a Court of Appeal appeal on a question of law, with leave, whoever constituted the tribunal -- so a
   dispute about the amount of costs in a small claim lies to the Court of Appeal or nowhere. Asserted.
7. **The 14 days for reasons and the 28 days to appeal start at different points.** s 122(2) runs from when the
   decision "takes effect under section 127" (possibly a later stated day); s 143(5)(b) runs from "the day the person
   received notice of the decision". Asserted for s 122.
8. **Rejection can be reviewed, but not appealed.** s 35(4) gives a free referral to the tribunal; ss 142(2)(a) and
   149(4) bar any appeal from the tribunal's s 35 decision. Asserted.
9. **A decision keeps operating through every challenge** unless stayed: review (s 22, subject to the enabling Act),
   set-aside of a default decision (s 51A), reopening (s 138A), and both appeals (ss 145, 152). Asserted.
10. **Withdrawal is a one-way door.** After withdrawing, a further application "relating to the same facts or
    circumstances" needs the tribunal's leave (s 46(3)); after dismissal under s 47 or s 48 it needs the president's or
    deputy president's leave (s 49(2)). Asserted.

## Before this is worth relying on

- Deposit the QCAT Rules 2009 and the QCAT Regulation, and bring in the periods and the minor civil dispute costs they
  set (the time to respond for a decision by default, the periods for giving the application, renewal and reopening).
- Deposit the Acts Interpretation Act 1954 (s 38, reckoning of time) and check fork F3.
- Check the conversion against the authorised PDF.
- A lawyer's view on findings 1, 3 and 4 and forks F2, F5, F6, F7, F11 and F14.
- Link to the Residential Tenancies and Rooming Accommodation Act 2008, the Neighbourhood Disputes (Dividing Fences and
  Trees) Act 2011 and the Limitation of Actions Act 1974 encodings once IMPORT can reach another subject.
- An independent test pass and a human gate.
