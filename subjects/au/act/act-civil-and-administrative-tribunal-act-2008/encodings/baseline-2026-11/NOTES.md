# ACT Civil and Administrative Tribunal Act 2008 -- baseline encoding, the person bringing or answering an application

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. The Act is mostly procedure and tribunal machinery; the encoding
takes the path a person walks through ACAT -- whether the tribunal can hear the claim (Part 3, Part 4), the review time
limit and deemed refusals, reasons statements and assistance in administrative review (Part 4A), what happens on absence
or non-compliance, costs, interim orders, deciding on the papers, the copy of the order and the tribunal's reasons
(Parts 5 and 6), notice of reviewable decisions, enforcement (Part 7), and appeals and removal (Part 8). Part 4 (civil
disputes, the $25 000 limit) is encoded whole; Part 3 is encoded whole; the rest is selected as listed under Scope.

This is the first encoding of the Act; nothing existed to extend. Three files: the dates (`acat-dates.l4`, built-in
date functions only, no daydate), the rules and the 23 exported questions (`acat-claims.l4`), and the worked cases
(`acat-cases.l4`). The two duties with deadlines the person meets -- the applicant's duty to apply for review within 28
days (s 10) and the decision-maker's duty to give a reasons statement within 28 days of a request (s 22B (2)) -- are
regulative rules (`PARTY ... MUST ... WITHIN ... HENCE ... LEST BREACH ... BECAUSE`), run by EVALTRACE inside exported
questions that take only plain facts.

## Edition

- **Act:** ACT Civil and Administrative Tribunal Act 2008 (ACT), A2008-35, Republication No 42 (R42), effective
  23 February 2026, last amended by A2026-4, as deposited at `../../registers/source-bundle/A2008-35.txt` (converted from
  the register's DOCX, which the register marks as an unauthorised version; the authorised text is the register's PDF).
- **Numbers set elsewhere:** none deposited. The Act leaves to the tribunal's rules (ACAT procedure rules) any longer
  periods (s 25 (1) (e), (2)), the time for an appeal within the tribunal, and who may not represent a party; and to a
  regulation the applications outside the $25 000 limit (s 18 (3) (b)) and the cap on a payment to the Territory for
  non-compliance (s 74 (2) (a)). Each is asked as a fact or named in the answer. The Magistrates Court's civil limit
  (Magistrates Court Act 1930, for s 69A) is asked. The Legislation Act 2001 (ACT) counting rules (s 151, s 151C) are not
  deposited (fork F2).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 10 last day put one day late) was run once in a scratch copy in this folder, since
deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `acat-dates.l4` | 0 | 0 | 0 | 0 |
| `acat-claims.l4` | 0 | 0 | 0 | 0 |
| `acat-cases.l4` | 0 | 0 | 144 | 144 |

Every exported question has cases, with the edges: the two rules alone on day 0, the last day and the day after; notice
given on the 5th day after the decision (not "later than 5 days") and on the 6th; notice required and not given; a
deemed s 12 decision; a longer period in the rules, barred and not barred, and a shorter one ignored; applying on the
last day and the day after; exactly $25 000, $25 001 and $25 000.50; interest taking a $26 000 claim under the limit;
each of s 20, s 21 and s 18 (3); asking for reasons on the last day and the day after; each "unless" limb of s 22B (2);
each costs head for and against, including the successful respondent who gets none of the s 48 (2) heads; each role on
absence and non-compliance, with and without a reasonable excuse; a s 54 shorter period of 7, 21 and none; a copy of an
order asked for on the 4th, 7th and 8th day; reasons asked for on the 14th and 15th day; each appeal route.

**No mirror cases.** One seat; the costs question is asked both ways (for me, against me) from the same internal rule.

## Seat

**The person bringing or answering an application to ACAT** (`acat-claims.l4`): the individual with a civil dispute
(a debt, a contract, goods or services, a damages claim in negligence such as a small personal injury claim, a nuisance or
trespass) worth up to $25 000, or who wants a government decision reviewed under an authorising law; and the same
individual as respondent where the question is the respondent's (costs against me, what happens if I do not appear).
"Can ACAT hear my claim for this amount?", "By when must I apply for review?", "Must I be given reasons, and by when?",
"What costs can be ordered?", "What happens if I do not turn up?", "Can I appeal?", "Where do I enforce the order?".

The tribunal, the president, the registrar, the decision-maker, the Minister and the regulatory bodies get no seat. What
they must do is encoded as what the person must be given and by when (ss 22B, 22D, 59, 60, 67A, 67B); what they may
decide is asked as a fact ("if the tribunal considers", "if the Minister is satisfied"). No second seat was written:
the party answering a civil dispute asks the same questions, and the questions that differ by role take the role as an
input.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument is deposited; each number the
  Act leaves to the rules or a regulation is asked (see Edition).
- **The actors the text names.** Followed: the applicant, the respondent, other parties, the decision-maker, the
  tribunal, the president, the Minister, the Magistrates Court and the Supreme Court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the tribunal is satisfied
  the parties understand the excess is not abandoned (s 21), considers a party caused unreasonable delay (s 48 (2) (b)),
  is satisfied costs are in the interests of justice (s 49), is satisfied of disadvantage or harm (s 53), considers
  removal appropriate (s 83 (2)); the Minister's satisfaction (s 22T); a reasonable period (s 12); a reasonable excuse
  (s 74).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "civil dispute application" and
  the kinds in s 15 (as a list), "appropriate court" (s 69A), "decision" kinds as needed. Asked: "authorising law" in
  any particular case, "fair work claim" (Magistrates Court Act 1930 s 266E), "reviewable decision" and "internally
  reviewable decision" (which depend on the authorising law), money and non-money orders (Court Procedures Rules 2006).
- **One case is the text's natural unit.** Followed: one application (or one appeal) by or against the person.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (Scope).

## Scope

**In.** Part 3 whole (s 9, s 10, s 11 (by the "authorising law allows it" fact), s 12); Part 4 whole (ss 15-22: s 22
only as the reason the tribunal has Magistrates Court powers, not encoded beyond that); s 22B, s 22D, s 22T; s 25 (2),
(3) (the longer periods); s 47A, s 48, s 48A, s 49, s 53, s 54 (2), s 56 (c) (i) (named in the absence answer); s 59,
s 60; s 67A, s 67B; s 69A, s 71, s 74; s 79, s 80 (1) (the 21 days), s 82A, s 83, s 86 (with s 85 as a route into it).

**Out, and why.**
- Parts 1 and 2 (name, dictionary, objects, tribunal principles, s 7A duties of parties, rules of evidence): no facts to
  apply; s 7A's duty to cooperate has no deadline or consequence of its own.
- s 22A, s 22C (the tribunal's declaration that reasons are insufficient: its judgment; only its consequence, s 22D, is
  encoded), ss 22E-22S (Minister's and Commonwealth certificates, non-disclosure procedure, the 120-day target for
  planning reviews, bodies whose interests are affected): official machinery; s 22E (3)'s 28-day duty is named in the
  s 22B answer but not run as a rule.
- ss 23-28 (procedure, rule-making), s 29 (parties), s 30 (representation: a plain permission whose only limit is
  persons the rules prescribe, not deposited), ss 31-36 (case management: tribunal discretions; the s 32 grounds appear
  only as a fact in costs), ss 37-46 (hearings, witnesses, warrants), s 47, ss 50-52, ss 55-58 (agreements and other
  orders), ss 61-63 (when orders take effect, corrections), Division 6.2 (occupational discipline of licensees: not a
  claimant's provision), ss 68-69 (the tribunal's options on review: no facts to apply), s 70, ss 72-73 (faulty orders,
  between court and tribunal), ss 75-76 (licensees' warning notices), ss 77-78 (referrals and corrections within the
  tribunal), s 80 (2), (3), ss 81-82 (appeal tribunal constitution and powers), s 84, s 87, Parts 9, 9A and 10, the
  schedule: machinery.
- The time limit for bringing a civil dispute (Limitation Act 1985), the Magistrates Court Act 1930 and the Court
  Procedures Rules 2006: other instruments.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 10 (1) "must" (form of an application) -- `s 10 (1) -- is my application properly made` -- a requirement
  missing is the text's no (FALSE) -- NOTHING (a bare "must" not done says nothing about validity).
- **F2** "within 28 days after the day" (ss 10, 22B, 22D; 7, 14, 21 days in ss 54, 59, 60, 80) -- every date question --
  the day itself excluded, last day = day + n; not moved off a weekend or public holiday -- Legislation Act 2001 s 151C
  moving the last day to the next working day (not deposited).
- **F3** s 10 (3) "However" -- `s 10 -- the last day to apply for review` -- the later of the s 10 (2) day and the s 10 (3)
  day -- s 10 (3) replacing s 10 (2) outright (the same answer unless awareness came before the decision).
- **F4** s 25 (2), a longer period in the rules -- s 10 and s 22B questions -- counted from the same day as the Act's
  period -- counted from a day the rule chooses.
- **F5** s 19 (2) "the following amounts are to be considered" -- `ss 18-21 -- can ACAT hear my claim for this amount` --
  read as what the total for a goods application includes (stated in the `@desc`) -- read as the only amounts counted.
- **F6** s 20 and s 21 both open -- the same function -- the s 21 answer (the whole amount) first -- the claimant's own
  choice, which the encoding cannot know.
- **F7** s 22B (2) "unless" once met (decided case by case) -- `s 22B -- must I be given a reasons statement` -- the
  duty does not arise (the text's no) -- NOTHING.
- **F8** s 48 (2) (c) "contravenes an order", with no "reasonable excuse" -- `ss 47A, 74 -- what can happen ...` -- costs
  may still be ordered if the tribunal finds it in the interests of justice -- a reasonable excuse excludes s 48 (2) (c)
  as it excludes s 74.
- **F9** s 54 (2) (b) (ii) "a shorter period" -- `ss 54, 80 -- the last day for my representations` -- counted from the
  day the notice is given; a "shorter" period of 21 days or more ignored; s 80 has none -- counted from the decision to
  shorten.
- **F10** s 86 (4) "However, the appeal may be brought only with the Supreme Court's leave" -- `s 86 -- can I appeal to
  the Supreme Court` -- leave needed for every appeal under s 86 -- leave needed only for the s 86 (3) appeal it follows.
- **F11** s 86, a decision not in the list for the kind of application -- the same function -- NOTHING-kind (the list is
  not closed with "only") -- JUST FALSE.
- **F12** s 79 (3) "A party to the original application may" -- `s 79 -- can I appeal within ACAT` -- for a non-party,
  NOTHING-kind (a grant limited in its own wording) -- JUST FALSE. The same reading for s 86 "a party".
- **F13** ss 67A, 67B for a decision ACAT cannot review -- `ss 67A, 67B -- must I be told of the decision` --
  NOTHING-kind -- JUST FALSE.
- **F14** s 59 (2) a request made more than 7 days after the order -- `s 59 -- by when must I get a copy of the order` --
  the request gives no right of its own; the s 59 (1) day stands -- a late request still to be answered within 7 days.
- **F15** s 16 "consists of 1 or more of the following" -- `s 16 -- is my claim a civil dispute application` and
  `ss 18-21` -- one kind chosen per question; a mixed application is a civil dispute application if any part is -- each
  part tested apart.

Sites decided without a fork line: the s 16 "means" list and s 16 (2)'s "does not include" answer FALSE outside the
list; "if" conditions in ss 12, 22B (1), 22T (1) ("This section applies to"), 53, 79 (1), 82A, 83 and the flat negatives
of ss 59 (4), 60 (4), 67A (2), 67B (2), 79 (2), 83 (3) answer as the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries four `NOTHING-kind` answers (F11, F12 twice, F13). Most questions answer with a choice from a list
rather than a MAYBE BOOLEAN: the answer marked "NOTHING-kind" is the NOTHING answer, and the answers marked "the text's
no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (28 days in ss 10 and 22B, 14 in s 60, 7 in s 59) answer the text's no outside the period
(ruling (a)).

## What the Act turns out to say

1. **The note to s 60 is copied from s 59.** Both read "The rules may prescribe a longer period for asking for order
   details"; s 60 is about asking for a statement of reasons, not order details. The note is not part of the Act (s 4),
   and s 25 (1) (e) allows a longer period for either anyway; encoded as allowing a longer period for asking for
   reasons. A likely drafting slip.
2. **s 18 (1) relies on "the tribunal's jurisdictional limit", which is not defined.** Neither s 18 nor the dictionary
   defines it; s 18 (2) and the heading ("$25 000 limit") supply $25 000. Encoded as $25 000. Asserted (the $25 000 and
   $25 001 cases).
3. **A damages claim in negligence, including a small personal injury claim, is a civil dispute application** (s 15
   "damages application" covers negligence "or any other tort except nuisance or trespass"), so ACAT can hear one up to
   $25 000, or above it by agreement under s 21. Asserted.
4. **The Act sets no time for an appeal within the tribunal (s 79) and none for a civil dispute application.** The first
   is left to the rules; the second to the Limitation Act 1985. The appeal answer says so.
5. **s 60 sets no time for the tribunal to give its statement of reasons**, unlike s 59 (7 days for a copy of the order)
   and s 22B (28 days for a decision-maker's reasons). Encoded as a duty without a deadline (no rule).
6. **s 48 (1) already gives an open costs discretion** ("unless ... the tribunal otherwise orders"), so the "However"
   heads in s 48 (2) are not the only orders open; and s 48 (2) (a) helps only a successful applicant. A successful
   respondent's costs rest on s 48 (1) alone. The costs questions list only the s 48 (2) and s 48A heads and say so.
   Asserted (the successful respondent gets an empty list).
7. **s 48 (2) (c) costs for contravening an order are not limited by "reasonable excuse"**, unlike s 74 (1) (fork F8).
   Asserted.
8. **s 86 (4) is ambiguous** between all appeals to the Supreme Court and the MAI appeal in s 86 (3) only (fork F10).
9. **Asking for a reasons statement does not stop the s 10 clock.** s 22B gives 28 days to ask and 28 more for the
   statement, but the 28 days to apply for review run from the decision (or notice) regardless; a person who waits for
   the statement can run out of time unless the rules give longer. Not asserted as a single case; the two deadlines are.
10. **s 10 (3) (a) turns on notice "later than 5 days after"**: notice on the 5th day leaves the 28 days running from the
   decision. Asserted (7 March and 8 March cases).

## Before this is worth relying on

- The ACAT procedure rules (longer periods, appeal time, prescribed representatives) and any ACAT regulation (s 18 (3)
  (b), s 74 (2) (a)), not deposited.
- The Legislation Act 2001 (ACT) for counting time (fork F2), not deposited.
- A lawyer's view on forks F3, F6, F8, F10 and F14, and on findings 1, 6 and 8; an independent test pass and a human
  gate.
