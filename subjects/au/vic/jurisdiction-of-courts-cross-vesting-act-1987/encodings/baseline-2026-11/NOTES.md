# Jurisdiction of Courts (Cross-vesting) Act 1987 (Victoria) -- baseline encoding, a party

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The rules and the party's exported questions
are in `jcv-party.l4` (each exported question calls a rule defined beside it, named for its section); the worked cases
are in `jcv-cases-party.l4`. No dates are needed, so there is no dates module and no daydate import.

The Act is short, so **every operative section is encoded**: ss 3, 3A, 4, 5, 6, 6A, 7, 8, 10, 11, 12, 13 and 14(2). For
a party to an injury claim with an interstate side it answers: which courts can hear a Victorian claim (s 4); when the
claim must move between the Supreme Court of Victoria and another Supreme Court or a federal court (s 5, the interests
of justice test and related proceedings); what happens to a special federal matter (ss 6, 6A); where an appeal goes
(s 7); moving a claim up from or down to a lower Victorian court (ss 8, 10); which law, and whose limitation law, the
court applies (s 11, read with the Choice of Law (Limitation Periods) Act 1993); what carries over after a transfer
(ss 5(8), 11(3), 12); and that a transfer decision cannot be appealed (s 13).

## Edition

- **Act:** Jurisdiction of Courts (Cross-vesting) Act 1987, Act No. 29/1987, Version No. 026, incorporating amendments
  as at 1 July 2015, deposited at `../../registers/source-bundle/jurisdiction-of-courts-cross-vesting-act-1987.txt`
  (text sha256 5aed7444...6f59440f per its `.meta.json`; a checkout with CRLF line endings hashes differently), a
  plain-text conversion of the Word file the owner saved by hand on 7 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Version 026 was the current version ("In force") on 2026-11-07. Not checked against the
  authorised PDF, which was not saved.
- **Numbers set elsewhere:** none. The Act sets no amounts or time limits, and no regulations are made under it.
- **Not deposited, and asked as facts:** the Commonwealth's Jurisdiction of Courts (Cross-vesting) Act 1987 (its
  definition of "special federal matter", by paragraph, and its Schedule of Acts for s 7); Division 1 of Part 9.6A of
  the Corporations Act 2001 (s 3A); the Family Law Act 1975 s 41 Proclamation (which court is a "State Family Court");
  Parts 3-1, 3-3 and 3-4 of the Australian Consumer Law (s 10); the Administrative Decisions (Judicial Review) Act 1977
  definition of "enactment" (s 6A); which place's substantive law governs a claim (the choice-of-law rules).
- **Restated narrowly from another subject:** the Choice of Law (Limitation Periods) Act 1993 (Victoria) s 5 (another
  State's, a Territory's or New Zealand's limitation law is part of its substantive law and is applied by a Victorian
  court), with the section, beside the one question that needs it (`Whose limitation law applies after cross-vesting`).
  Its s 4 (proceedings instituted before 23 November 1993) is not restated. That Act's own encoding is at
  `subjects/au/vic/choice-of-law-limitation-periods-act-1993/encodings/baseline-2026-11/`.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `jcv-party.l4` | 0 | 0 | 0 | 0 |
| `jcv-cases-party.l4` | 0 | 0 | 126 | 126 |

Every exported question has cases, with the edges: each limb of s 5(2), (3), (4) alone and none of them; the repealed
limbs of s 5(1) (a related proceeding and the bare interests of justice give no duty to transfer to a federal court);
the State Family Court reached through s 3(2); each pair of courts s 5 does not deal with; each s 6A limb missing in
turn; each s 6(4) step missing; each branch of s 7; s 10 with each Part alone, none, and each other paragraph failing;
s 11 with and without a statutory right of another place, in Victoria, another State, a Territory and abroad; and the
`NOTHING` answers.

## Seat

**A party** (`jcv-party.l4`): a person who brings or answers a civil claim (typically an injury claim with an
interstate side: an accident in another State, a defendant or insurer there, a related claim in another court) and asks
which court can or should hear it. "Can that court hear my Victorian claim?", "Must my proceeding be transferred to that
court?", "Must my special federal matter be transferred?", "Where does my appeal go?", "Which law will the court apply
to my claim?", "Can I appeal the decision?".

The Act names no claimant or defendant and puts no duty on either: transfer, removal and the choice of law are the
same for both, so one seat is written for "a party" and "my proceeding" is either side's. No seat for a court, a
tribunal or an Attorney-General; their powers appear only as what they mean for the party.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: there are none. The Choice of Law (Limitation
  Periods) Act 1993 s 5 is restated narrowly because s 11(1)(a) points to Victoria's "choice of law rules" and the brief
  asks for it to be read with s 11; nothing else is brought in.
- **The actors the text names.** Followed: the Supreme Court (of Victoria), the Supreme Courts of other States and
  Territories, State Family Courts, the Federal Court, the Family Court, the High Court, lower courts and tribunals,
  parties, interveners, Australian lawyers, Attorneys-General.
- **Judgments answered conditionally.** Every "it appears to the court", "in the opinion of the court", "more
  appropriate", "the interests of justice", "special reasons", "a reasonable time" is an input worded as the court's
  view, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: s 3 "State matter" (from two facts), "State"
  and "Territory" (in the choice lists), "party" (intervener included), "proceeding" (criminal excluded), "Full Court"
  (the Court of Appeal), s 3(2) (a State Family Court counts as a Supreme Court of a State outside s 4(3)). Asked:
  "special federal matter" and its paragraphs, the Schedule Acts, Corporations Part 9.6A, the ACL Parts, "State Family
  Court" (by naming the Family Court of Western Australia), "a right of action arising under a written law".
- **One case.** One proceeding (with, where the text needs it, the related proceeding).
- **The Act's terms with plain glosses.** Followed, in the `@export` and `@desc` text.
- **Operative sections in; machinery out.** See Scope.

## Scope

**In:** s 3 (definitions, as above); s 3A (the Corporations Act exclusion); s 4(3)-(5) (vesting in the other Supreme
Courts and State Family Courts; no criminal jurisdiction); s 5(1)-(4) (transfer, with every limb still in force), s 5(6)
(related proceedings follow), s 5(7) (who may apply), s 5(8) (a lawyer's entitlement after transfer), s 5(9) (stated
in the export text: a transfer confers no jurisdiction); s 6(1)-(9) and s 6A(1)-(3) (special federal matters); s 7
(appeals); s 8 (removal into the Supreme Court; (2) and (3) in the answer); s 9 (the Supreme Court may exercise
cross-vested jurisdiction and hear a transferred proceeding: implied in the s 5(3), (4) answers); s 10 (sending an ACL
matter down); s 11(1) and (3) (which law; steps carry over); s 12 (costs); s 13 (no appeal); s 14(2) (enforcement).

**No regulative rule.** The Act sets no time limit for a party and puts its duties ("shall transfer", "must transfer")
on courts, which get no seat; the one time-like step, a "reasonable time" after notice to the Attorneys-General
(s 6(4)(b)), is the court's judgment. A DEONTIC rule would add nothing a party can act on, so none is written.

**Out, and why:**
- s 1 (purpose), s 2 (commencement): machinery.
- s 6A(4)-(6), s 5(9): no rule of their own beyond what the answers say (no new jurisdiction; "interests of justice"
  includes keeping related proceedings together, which the `@desc` text mentions; the definitions in (6) are asked).
- s 14(3) (a reference to the Supreme Court in another Victorian law reads as the court doing the thing): an
  interpretation rule with no question a party asks.
- s 15 (read down to the State's power), s 16 (suspension and cessation by proclamation), s 17 (alteration of s 85 of
  the Constitution Act 1975), s 18 (saving for proceedings pending before the Courts (General Amendment) Act 1995):
  machinery or transitional; s 6(9)'s reference to the pre-1995 s 6(1) is folded into "an order under s 6(3)".
- The Commonwealth's and the other States' cross-vesting Acts, which give the mirror powers (for example a transfer
  from the Supreme Court of New South Wales to the Federal Court): not this Act; the answer says "not covered".
- What a court decides on any discretion, and the law it then applies in substance.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3 "Territory does not include the Northern Territory or the Australian Capital Territory" -- `Court`, `Place`
  -- "the Supreme Court of a Territory" is that of a Territory such as Norfolk Island; the Northern Territory and the
  ACT are "States" -- the definition is read differently in a provision that lists them separately.
- **F2** s 3 "State Family Court" (a court to which Family Law Act s 41 applies by Proclamation) -- `Court` -- the Family
  Court of Western Australia, the only such court named in the list -- another court so proclaimed (none is known; not
  checked, the Proclamation is not deposited).
- **F3** s 5(7) who may apply -- `s 5(7) -- I may apply for a transfer` -- a person who is neither a party nor an
  Attorney-General: NOTHING (the list is not closed with "only") -- FALSE (the list is exhaustive).
- **F4** s 5(8) -- `s 5(8) -- my lawyer keeps the right to act` -- a lawyer not entitled to practise in the first court:
  NOTHING (outside the subsection's subject) -- FALSE.
- **F5** s 6(7) -- `s 6(7) -- urgent interlocutory relief is not prevented` -- relief that is not urgent and
  interlocutory: NOTHING (s 6(7) is silent) -- FALSE (s 6(1) requires transfer, so other relief must wait).
- **F6** s 6(8) -- `s 6(8) -- s 6 invalidates the decision` -- a decision made deliberately without the steps: NOTHING --
  TRUE (invalid by implication).
- **F7** s 8(1) "a court, other than the Supreme Court" and "a tribunal established by or under an Act" -- `s 8 -- it can
  be removed into the Supreme Court` -- a Victorian court or tribunal (an Act of Victoria; s 15 reads the Act down to the
  State's power) -- any court, or a tribunal under any Act.
- **F8** s 10(b) "a matter arising under Part 3-1, Part 3-3 and Part 3-4" -- `s 10 -- it may be sent to a Victorian
  lower court` -- a matter arising under any one of the three Parts ("and" read as "or", as the earlier text did with
  "Division 1 or 1A of Part V", which the heading still names) -- a matter arising under all three Parts at once.
- **F9** s 11(1)(b) "the written and unwritten law of that other State or Territory" -- `s 11(1) with CLLPA s 5 -- whose
  limitation law` -- includes that place's limitation law -- only the law that creates and measures the right.
- **F10** s 11(3) "subject to any order of the transferee court" -- `s 11(3) -- earlier steps count in the new court` --
  an order of the new court that the steps (or the step asked about) not count: FALSE -- the order modifies but does not
  displace.
- **F11** s 13(a) "in relation to the transfer or removal" -- `s 13 -- an appeal lies` -- covers a refusal to transfer
  as well as a transfer -- covers only an order that transfers or removes.
- **F12** s 5(1)-(4) "shall transfer" -- `s 5(1)-(4) -- it must be transferred` -- the duty arises whenever a limb
  appears to the court, without asking whether the receiving court has jurisdiction (s 5(9) says the section confers
  none, which the export text states) -- the answer should also ask whether the receiving court has jurisdiction.
- **F13** s 6A(1)(c)(i), (ii) -- `ss 6, 6A -- what happens to my special federal matter` -- asked in one yes/no fact
  with the related State proceeding -- asked as three facts.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 3 "State matter" is a "means" definition (FALSE when neither limb holds); s 3 "proceeding does not
include a criminal proceeding", s 3A "does not apply", s 4(5) "does not invest", s 13 "does not lie" are flat negatives
(a "no" constructor or `JUST FALSE`); the "where" and "if" conditions of ss 5(1)-(4), 5(6), 5(8), 6(3)-(4), 6(7), 8,
10, 11, 12 give a "no" constructor or `JUST FALSE` when they fail; where the text is silent (a pair of courts s 5 does
not deal with, a decision s 13 does not name, a judgment outside s 14(2)) the answer is "not covered" or `NOTHING`.

## What the Act turns out to say

1. **Since 2000, Victoria vests nothing in the federal courts, and the related-proceedings limb to them is gone.**
   s 4(1), (2) and s 5(1)(b)(i), (iii) are repealed (Federal Courts (Consequential Amendments) Act 2000, after the High
   Court held such vesting invalid). So the Federal Court and the Family Court cannot hear a Victorian "State matter" by
   this Act, and a claim in the Supreme Court of Victoria must go to them under s 5(1) only if it is more appropriate
   there having regard to (A)-(C); a related proceeding there, or the bare interests of justice, no longer founds the
   duty. Transfers the other way (s 5(4)) keep all three limbs. Asserted.
2. **"A Territory" is not the Northern Territory or the ACT.** Those two are "States" under s 3, so "the Supreme Court of
   a Territory" can only be the court of a Territory such as Norfolk Island (F1). Asserted (Norfolk Island cases).
3. **The Family Court of Western Australia counts as another State's Supreme Court in s 5.** s 3(2) reads "the Supreme
   Court of a State" as including a State Family Court everywhere except s 4(3), so a claim can be transferred between
   the Supreme Court of Victoria and the Family Court of Western Australia under s 5(2), (3), and that court has its own
   vesting in s 4(4). Asserted.
4. **s 10 is conjunctive on its face, and misses product liability.** s 10(b) says a matter arising under "Part 3-1,
   Part 3-3 and Part 3-4" of the Australian Consumer Law; read literally a single matter would have to arise under all
   three. It is read as "or" (F8), the sense of the provision it replaced, whose heading ("Division 1 or 1A of Part V of
   the Trade Practices Act") was never updated. Part 3-5 (manufacturers' liability for safety defects), the Part an
   injury claim about defective goods usually arises under, and Part 3-2 (consumer guarantees) are not named, so s 10
   does not reach a claim under them alone. Asserted.
5. **The Act still names the Family Court of Australia.** Version 026 (as at 1 July 2015) is the current version; the
   Family Court of Australia has since been continued under Commonwealth law as part of the Federal Circuit and Family
   Court of Australia. How references to it in this Act now read is a matter of Commonwealth law, not deposited. The
   answers use the Act's words.
6. **Choice of law follows the court that sits, with one exception.** s 11(1)(a) applies the law where the court sits,
   "including choice of law rules"; in Victoria those include the Choice of Law (Limitation Periods) Act 1993, under
   which the limitation law of the place whose law governs the claim (another State, a Territory or New Zealand) applies.
   s 11(1)(b) instead applies the whole law of another State or Territory where the right of action arises under its
   statute. Whether a common-law claim whose damages another State's statute limits is "a right of action arising under a
   written law" is not said; it is asked. Asserted (both routes).
7. **A transfer decision cannot be appealed, whichever way it goes.** s 13(a) bars an appeal from a decision "in relation
   to" a transfer or removal under this Act; that covers a refusal (F11). The bar is this Act's: a transfer made under
   the Commonwealth's or another State's Act is outside it (answered `NOTHING`). Asserted.
8. **The Supreme Court Act 1986 meets this Act at group proceedings.** The Supreme Court Act's s 33C bars a group
   proceeding where the Court's jurisdiction over every claim is solely by cross-vesting; that is encoded in
   `subjects/au/vic/supreme-court-act-1986/encodings/baseline-2026-11/gp-part4a.l4`, not here.
9. **s 7(5) is about an appeal from a State Family Court**, a court Victoria does not have; it can matter only where the
   Family Court of Western Australia exercises jurisdiction under this Act (s 4(4)). Encoded as written.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit the Commonwealth's Jurisdiction of Courts (Cross-vesting) Act 1987 (the special federal matter definition and
  the Schedule) and the other States' cross-vesting Acts, so the mirror transfers can be answered rather than "not
  covered".
- A lawyer's view on findings 4, 5 and 6 and forks F1, F2, F8, F9, F11 and F12, an independent test pass and a human
  gate.
