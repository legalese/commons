# County Court Act 1958 (Vic) -- baseline encoding, the individual party to a civil proceeding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`cc-rules.l4`), the dates
in another (`cc-dates.l4`, built-in date functions only, no daydate), and the party's questions in `cc-seat.l4`, which
imports the rules and never restates one.

The focus asked for: the court that hears most personal injury and workers' compensation common law claims, its
jurisdiction and procedure. The Act itself holds little that is specific to injury claims (s 37(1)(b) on councils, s 39A on
children's injury settlements, ss 39B-39C on money for children and persons under disability); the thresholds, caps and
gateways those claims turn on are in the Wrongs Act 1958, the Workplace Injury Rehabilitation and Compensation Act 2013, the
Accident Compensation Act 1985 and the Transport Accident Act 1986, each with its own baseline beside this one in
`subjects/au/vic/`. What the County Court Act gives a claimant is where the claim can go, how it is tried, what the judgment
carries, and where an appeal goes; that is what is encoded.

## Edition

- **Act:** County Court Act 1958, Act No. 6230/1958, Version No. 186, incorporating amendments as at 30 September 2026,
  deposited at `../../registers/source-bundle/county-court-act-1958.txt` (sha256 b89208ff...22833b5b as committed, per its `.meta.json`),
  a plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the penalty interest rate (Penalty Interest Rates Act 1983 s 2, not deposited) is asked; the
  court fees and jury fees (regulations and Rules, not deposited) are not computed; the contributory negligence reduction
  (Wrongs Act 1958 Part V) is the Court's and is asked as a percentage. The Act's own figures are used: $5000 (s 67(1)),
  $20 (s 33), four days (s 72(3)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, to confirm that a failure shows as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cc-dates.l4` | 0 | 0 | 0 | 0 |
| `cc-rules.l4` | 0 | 0 | 0 | 0 |
| `cc-seat.l4` | 0 | 0 | 0 | 0 |
| `cc-cases.l4` | 0 | 0 | 138 | 138 |

Every exported question has cases, with the edges: $5000 and $5000.01 (s 67(1)); $20 and $20.01 (s 33); a verdict $1
over the amount sought, equal to it, and reduced below it (s 37(3)); the fourth and fifth day after notice of trial, the
same day, and across 29 February 2028 (s 72(3)); interest for one day, 73 days, a common year, a leap year (366 days), the
same day and a day before the start (s 73(4)); every constructor of every choice.

## Seat

**The individual party to a civil proceeding in the County Court** (`cc-seat.l4`): usually the plaintiff with a personal
injury or workers' compensation common law claim; also, for the provisions that speak of them, the parent or other person
acting for an injured child (s 39A), the person on either side of a Supreme Court re-hearing (s 72), the judgment creditor
(s 86), and the employee whose earnings are attached to pay a judgment (s 49A(3)). "Can the County Court hear my claim?",
"Can I recover more than I claimed?", "Can I settle my child's injury claim?", "Where does my child's money go?", "Can I
have a jury?", "Must I pay the jury fees?", "How much interest does my judgment carry?", "Where does my appeal go?", "Can my
fee be waived?".

No seat for the Court, the registrar, or the defendant (in these claims usually an employer, insurer, council or other
body). The Court's and registrar's findings, opinions, leave, consent and orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no instrument that sets a number here is
  deposited (penalty interest rate asked; fees not computed).
- **The actors the text names.** Followed: plaintiff, defendant, parties, the parent, guardian, next friend, person in loco
  parentis, the State Trust, administrator, Senior Master, registrar, judge, associate judge, judicial registrar, the Court
  of Appeal, the Trial Division, the prothonotary, the employer.
- **Judgments answered conditionally.** Followed: "satisfied that it is in the interests of justice" (s 36AA), "satisfied
  with respect to" (s 39A(6)), "unless the court otherwise orders" (ss 39B, 39C), "in the opinion of the court" (s 34),
  "in the registrar's opinion" (s 79A(6)), leave and consent are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "person under disability" (s 39C(1)) is worked
  out; "minor" and "child" (asked as under 18), "motor car" (Transport Accident Act 1986), "contributory negligence"
  (Wrongs Act 1958 Part V), "judicial resolution conference" (Civil Procedure Act 2010) are asked.
- **One case.** One civil proceeding, seen by one party.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 36 (cause of action outside Victoria); s 36AA (deciding without an oral hearing, civil only); s 37(1), (2), (3)
(jurisdiction, no money limit, recovering above the amount sought); s 39(2) and s 55 (a proceeding beyond jurisdiction);
s 39A(1), (2)(b), (4), (6), (8), (10) (a child's injury settlement); s 39B(1) and s 39C(1), (3) (money awarded to a child or
person under disability); s 46(2), (4), s 47, s 47A (arbitration awards), s 47B (mediation evidence); s 49A(3) (prejudice to
an employee for an attachment order); s 51 (counter-claims beyond jurisdiction); s 67(1) (party's jury), s 68(2) (jury
fees), s 70 (judgment on a verdict), s 73(3), (3A) (new trial), s 73(4) (interest on judgment debts); s 74(1), (6), (7),
s 75, s 17V(3), (4), s 47 (appeals), s 77 (no prerogative writ, in a question's description); s 72 (jury on a Supreme Court
re-hearing, with s 72(3) as a regulative rule); s 86 (certificate to take a judgment to the Supreme Court); s 33 (costs on
a recovery of $20 or less), s 34 (excessive lawyer's fees), s 79A(6) (fee waiver for hardship).

**Regulative rule:** one. s 72(3), the defendant DOes the jury notice WITHIN 4 days of receiving notice of trial (day 0),
LEST no jury as of right (fork F9). Run by EVALTRACE inside an exported question that takes only dates and facts, through a
helper of the shape the Accident Compensation Act 1985 and Supreme Court Act 1986 encodings use. The s 39A(4) "until" bar is
encoded as the bar, per ruling (d); no other provision sets a duty with a period.

**Out, and why:**
- Part I Divisions 1-6, 8 (establishment, Drug Court and Koori Court Divisions, sittings, judges, pensions, associate and
  reserve judges, judicial registrars other than s 17V, registrars, Aboriginal elders, bailiffs, officers, ss 29-32) and
  s 28A (fees in the criminal and appellate jurisdiction, for officials): machinery.
- s 36A (criminal jurisdiction) and s 53A (criminal and other appeals to the County Court): outside the focus.
- s 39A(2)(a), (3), (5), (7), (9) (filing place, submission, the order's terms, recording, scope): procedure and the Court's
  orders; s 39B(2)-(6), s 39C(2), (4)-(6) (pre-2004 money, administrators' and the Senior Master's duties): no fact test
  for the party beyond those encoded.
- s 40, ss 46(1), (3), 48-48D, 49, 49B, 50, 52, 53, 54, 65, 66, 68(1), 73(1), 76: powers of the Court or the general rule
  with no fact test for the party (s 65, trial by a judge alone, is the default every jury question starts from).
- s 78A (costs in the Court's discretion, may be ordered against a lawyer, may go to the Costs Court): no test to encode;
  noted in s 33's answer.
- Part VII (Rules, regulations) other than s 79A(6): regulation-making.
- s 80A (offence of publishing names of debt defendants before judgment): a debtor's protection outside the claims focus;
  worth a debtor question later. ss 82-84, 87, 88: machinery or Supreme Court and bailiff powers.
- ss 89-105 (transitional), the Schedules, s 3(2)-(5): spent or machinery (s 3(3)-(5), see finding 7).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 37(1)(a) "as are not ... excluded" -- `s 37 -- the County Court has jurisdiction over the kind of proceeding` --
  a claim another Act excludes answers NOTHING (the grant limited in its own wording; the excluding Act answers) -- JUST
  FALSE, as no jurisdiction.
- **F2** s 36 -- `s 36 -- where the cause of action arose is no bar` -- part of the cause of action outside Victoria with no
  material part within it, the defendant resident when served: NOTHING (finding 1) -- JUST TRUE a fortiori from the
  whole-outside proviso.
- **F3** ss 39(2), 55 -- `ss 39(2), 55 -- what becomes of a proceeding beyond jurisdiction` -- wholly beyond, no consent:
  must be struck out unless the Court first amends it or stays it for transfer (finding 2) -- s 55 alone (strike out) or
  s 39(2) alone (any of three).
- **F4** s 39A(1) "(other than injury caused by or arising out of the use of a motor car ...)" -- `s 39A(1), (10) -- I may
  agree for the child to accept the offer` -- read inside the "if": JUST FALSE -- NOTHING (a scope limit without "only").
- **F5** s 39A(2), (3), (4) -- `s 39A(2), (6) -- the Court may approve the agreement` -- no filed agreement with the
  affidavit, no approval: JUST FALSE -- NOTHING (s 39A(6) lists only the three satisfactions).
- **F6** s 39B(1) "a child" (undefined in the Act) -- `ss 39B, 39C -- where the money awarded goes` -- read as a minor
  (under 18) -- a narrower meaning from another Act.
- **F7** s 73(4) -- `s 73(4) -- the interest on the judgment debt` -- simple interest by the day over a 365-day year (366
  days in a leap year give 366/365 of a year), the rate held for the whole period -- a 366-day divisor in leap years, or the
  rate changing during the period (the Act's "for the time being" suggests it changes; ask period by period).
- **F8** s 74(6) "Nothing herein contained" -- `ss 17V, 47, 74, 75 -- where my appeal goes` -- "herein" read as the whole
  Act, so the bar reaches s 75 and s 17V too -- s 74 only.
- **F9** s 72(3) "The defendant may have a jury by giving ... within four days" -- `s 72(3) -- the defendant's jury notice
  within four days` -- a condition of a right written as DO ... WITHIN 4 ... LEST BREACH (the "breach" is losing the jury as
  of right, not a wrong); day 0 is the day notice of trial is received (Interpretation of Legislation Act 1984 s 44), the
  fourth day after is in time, the fifth late -- counting the day of receipt.
- **F10** s 72(2) "when giving notice of trial" -- `s 72 -- where my jury on the re-hearing stands` -- the plaintiff's
  jury notice is in time only on the day notice of trial is given; while notice of trial has not been given, still open --
  a jury notice given before the notice of trial, or a short time after.

Two sites follow the case-by-case convention without a fork line of their own: s 68(2) outside "of his own motion" and
s 49A(3) outside "by reason of" answer NOTHING (limited by their own wording).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "does not have jurisdiction" (s 37(2)), "shall not be allowed ... unless" (s 33), "must not be made unless"
(s 39A(6)), "Nothing in this section applies" (s 39A(10)), "does not have any force or effect until" (s 39A(4), as a bar),
"no evidence shall be admitted ... unless" (s 47B), "neither party shall be liable" (s 68(2)), "does not apply so as to
authorize" (s 73(3A)), "no appeal shall lie" (s 74(7)), "shall not be subject to question or appeal" (s 47), "No such
certificate shall be granted" (s 86(2)), "no relief ... unless" (s 51), "unless there is an enforceable costs agreement"
(s 34(2)), the "if" conditions of ss 36AA, 39A(1), 79A(6), the "where" of s 67(1), the "when" of s 39A(8) and the
"provided that" of s 36 give `JUST FALSE`; the excluding Act (s 37(1)(a)), a judicial resolution conference (s 47B) and jury
fees outside s 68(2) give `NOTHING` (*points outside the text*, *limited by its own wording*); ss 36 (finding 1), 37(3),
49A(3), 51, 70, 72(1), 33 above $20 and 34 outside the persons or events they speak of give `NOTHING` (*silent*, *limited
by its own wording*).

## What the Act turns out to say

1. **A gap in s 36.** The first proviso covers a cause of action partly outside Victoria "provided that a material part
   ... arose within Victoria"; the second covers one arising wholly outside Victoria "provided that the defendant ...
   resided within Victoria" when served. A cause of action partly outside Victoria with no material part within it, against
   a Victorian resident, is in neither limb, though it is closer to Victoria than the wholly-outside case the second limb
   allows. Answered `NOTHING` (F2). Asserted.
2. **s 55 and s 39(2) overlap.** s 39(2) (substituted 1987) gives the Court three options for a proceeding "wholly or partly
   beyond the jurisdiction" (amend, stay for a Courts (Case Transfer) Act 1991 application, strike out with costs); s 55
   (from 1958, amended 2008) says that for a proceeding over which the Court "has no jurisdiction" the judge "shall, unless
   the parties consent ..., order it to be struck out". Read together: struck out unless first amended or stayed (F3).
   s 55's consent route also sits oddly with s 37, which no longer has a money limit for consent to cure. Asserted.
3. **ss 39B and 39C both direct a minor's money.** s 39B(1): money adjudged to be paid to a child "is to be paid into
   court" and, unless the Court otherwise orders, paid out to an administrator. s 39C(3): money adjudged to be paid for a
   person under disability, which by s 39C(1)(a) includes every minor, "must be paid into the Supreme Court" to the Senior
   Master unless the Court orders otherwise. s 39C(6) says s 39C does not affect s 39B, but does not say which governs when
   both reach the same money. The encoding returns both directions for a minor rather than choose. Asserted.
4. **"the State Trust" and "State Trustees".** s 39A(1), (2)(b) and (6)(a) speak of "the State Trust" and "a director of
   the State Trust"; s 39B(4) speaks of "State Trustees within the meaning of the State Trustees (State Owned Company) Act
   1994". The Act does not define "the State Trust"; read as the same body, offered as a choice of who acts for the child.
5. **Two money figures left from another era.** s 33 bars lawyers' costs "in any civil case in which the amount recovered
   does not exceed $20", and s 67(1) lets a party require a jury only where the amount claimed or value "exceeds $5000".
   Both are the Act's own figures and are used as written; neither is indexed. Asserted at the edges.
6. **s 74(6) has little left to bite on.** It bars appeals on "any question as to the value of ... property for the
   purpose of determining the question of the jurisdiction of the court". Since No. 50/2006 repealed the jurisdictional
   limit and s 38, the Court's civil jurisdiction no longer turns on value, so the bar's first limb is close to spent.
   Encoded as written (F8). Asserted.
7. **s 3(3)-(5) point at the 1989 Rules.** They give the "County Court Rules of Procedure in Civil Proceedings 1989"
   precedence over procedure in other Acts and require proceedings to be commenced, conducted and enforced under them. The
   civil procedure rules of the County Court have been remade since 1989 (the current rules are not deposited here); whether
   the Interpretation of Legislation Act 1984 carries the references over is a question for a lawyer. Out of scope; noted.
8. **No day count for judgment interest.** s 73(4) fixes the rate (by reference) and the start, but not how the interest
   is computed between days, nor what happens when the rate "for the time being" changes. Encoded as simple interest by
   the day over 365 days at one rate (F7). Asserted, including a leap year.
9. **The jury on a re-hearing is a right with a short clock for the defendant.** s 72(3) gives the defendant four days
   after receiving notice of trial; the plaintiff must give the jury notice "when giving notice of trial" (s 72(2)), so the
   plaintiff has no separate period at all (F10). Asserted.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Penalty Interest Rates Act 1983 (the rate), the County Court Civil Procedure Rules (jury notices, appeals from
  judicial registrars, fees), the court fees regulations, and the Courts (Case Transfer) Act 1991, none deposited.
- A lawyer's view on findings 1, 2, 3 and 7, an independent test pass and a human gate.
