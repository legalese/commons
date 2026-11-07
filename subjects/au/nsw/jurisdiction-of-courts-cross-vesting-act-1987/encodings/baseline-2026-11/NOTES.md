# Jurisdiction of Courts (Cross-vesting) Act 1987 (NSW) -- baseline encoding, a party to the proceeding

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 14 July 2023). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of this subject; nothing existing was touched. Two files:

| File | What it holds |
|---|---|
| `xv-rules.l4` | the whole operative Act, ss 3-14, one rule per provision named by section, each with an exported question beside it (22 questions); one regulative rule (s 6(5)(b)) run by `EVALTRACE` inside a question that takes plain facts |
| `xv-cases.l4` | worked cases for every exported question (116 assertions) and one `#TRACE` of the breach |

The Act is short (ss 1-16), so it is encoded whole apart from the machinery. It sets no number of its own that a party
meets: no time limit, cap or threshold. Its only deadline for a party is the one a court gives when it directs a party
under s 6(5)(b) to notify the Attorneys-General; that is the regulative rule, with the period of the direction as
`WITHIN`. Every other provision turns on a court's opinion, which is an input.

## Edition

- **Act:** Jurisdiction of Courts (Cross-vesting) Act 1987 No 125 (NSW), `act-1987-125`, the version of 14 July 2023 as
  collected by the Open Australian Legal Corpus (version 7.1.0, NSW collected 10 March 2025), deposited at
  `../../registers/source-bundle/act-1987-125.txt` (text sha256 `c3c7c16b3c1876ca83a3ef4006321c0b763ff4b39d17787cc40281c5e4708f7a`
  per its `.meta.json`; a Windows checkout with CRLF line endings hashes differently). legislation.nsw.gov.au returned a
  bot challenge, so the official text could not be read. Not the authorised text, and possibly out of date.
- **Instruments that set numbers:** none; the Act has no regulations.
- **Borrowed and not deposited:** the Jurisdiction of Courts (Cross-vesting) Act 1987 (Cth) (the definition of "special
  federal matter" and its paragraphs (a), (ab), (b)-(e); the Schedule of Acts used by s 7), the Administrative Decisions
  (Judicial Review) Act 1977 (Cth) s 3(1) paragraphs (ca), (cb), the Corporations Act 2001 (Cth) Part 9.6A, the Trade
  Practices Act 1974 (Cth) Part V. Each is asked as a fact.

## Checks

Stable `l4` of the L4 VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), from this folder, `JL4_LIBRARY_PATH`
unset, one at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `xv-rules.l4` | 0 | 0 | 0 | 0 |
| `xv-cases.l4` | 116 | 116 | 0 | 0 |

Every exported question has cases: each limb of every "or" on and off, each condition of every "and" failing alone (the
four s 6A(1) conditions against ss 5(1), 5(4) and 6; the five s 10 conditions; the four s 5(6) conditions), the s 6(9)
and s 6A exceptions, and for the s 6(5)(b) notice the day of the direction, the last day of the period and the day
after, a year end and 29 February 2028. One `#TRACE` shows the breach (the stable `l4` cannot compare a breached trace
with `EQUALS`; the question uses `CONSIDER ... WHEN FULFILLED`). Expected values were worked by hand from the text.

## Seat

**A party to a civil proceeding** (s 3(1) "party ... includes a person who intervenes") whose case is in, or may be
moved to or from, the Supreme Court of New South Wales -- for example a person bringing or answering a personal injury,
compensation or other claim that touches another State's law or Commonwealth law. "Does the Act reach my case? Is it a
State matter? Can a court in another State hear it? Must my case be sent to the Federal Court, the Federal Circuit and
Family Court, another Supreme Court, or into the NSW Supreme Court? Can I ask for a transfer? What happens if it raises
a special federal matter, and can the Supreme Court keep it? Have I given the Attorneys-General the notice I was
directed to give, in time? Can my case be taken up from a lower court or tribunal, or sent down? Where does my appeal
go? Which law applies after a transfer; do the steps and costs carry over; can I appeal the transfer; can my lawyer
keep acting; can I enforce the judgment?"

No seat is written for the courts or the Attorneys-General. Their powers and duties appear as what may be done with
the party's case. No other party carries duties or liabilities under the Act, so no second seat is needed (the other
side of the case asks the same questions from the same seat).

The 2026-10-18 defaults, all followed:

- **The Act alone.** No instrument sets its numbers (there are none).
- **The actors the text names:** the Supreme Court, the Supreme Courts of other States and Territories, the State
  Family Courts, the Federal Court, the Federal Circuit and Family Court of Australia, the Full Courts, the High Court,
  the Attorneys-General, the parties, Australian legal practitioners.
- **Judgments handed to others are answered conditionally:** every "it appears to", "in the opinion of", "considers",
  "is satisfied", "the interests of justice", "special reasons" and "reasonable time" is an input.
- **The Act's own definitions are worked out from facts:** proceeding (not criminal), party (includes an intervener),
  State matter, State and Territory (in the glosses), the s 6A(1) conditions. **Borrowed terms are asked:** special
  federal matter and its paragraphs, the Schedule Acts, the ADJR enactment paragraphs, the Corporations Act and Trade
  Practices Act provisions.
- **One case:** one proceeding (with, where the text needs it, the related proceeding).
- **The Act's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines and the answers.
- **Machinery out** (Scope).

## Scope

**In:** ss 3 (definitions used), 3A, 4(3)-(5), 5(1)-(4), (6)-(9), 6, 6A, 7, 8, 10, 11(1), (3), 12, 13, 14(2). Section 9
(the Supreme Court "may exercise" cross-vested jurisdiction and hear transferred cases) is the premise of the transfer
questions and has no question of its own; ss 5(9) and 6A(4) ("nothing ... confers ... jurisdiction") are stated in
finding 2.

**Out, and why:**

- ss 1, 2 (name, commencement), 15 (reading down to the State's legislative power), 16 (suspension or cessation by
  proclamation): machinery. The encoding presumes the Act is in force and not suspended in relation to any State.
- s 14(3) (a reference in a NSW law to a thing done by the Supreme Court read as a reference to the other court): a rule
  of construction for other laws, with no answer a party could be given on its own.
- s 3(2), (3) (State Family Court references; Commonwealth Acts as amended): folded into the glosses.
- s 6(5)(a) (the court's power to adjourn and order costs of an adjournment): the court's own power.
- The repealed provisions (ss 4(1), (2), 5(1)(b)(i), (iii), 5(5), 11(2), 14(1)).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 3(1) "proceeding", 3A -- `ss 3, 3A -- the Act reaches the case` -- asked once, as a gate; the other
  questions presume the case is a civil proceeding outside Part 9.6A of the Corporations Act -- each question could
  take the two facts itself.
- **F2** s 5(7) (a list not closed with "only") -- `s 5(7) -- who may apply` -- a person who is neither a party nor an
  Attorney-General is "not covered" -- "no", reading the list as the whole of who may apply.
- **F3** s 7(6) "unless the interests of justice require that the Court proceed" -- `s 7(6) -- transfer of an appeal
  begun in the Court of Appeal` -- once the "unless" is met the duty to transfer falls away and the answer is "no" --
  the Court may still transfer, the "unless" only lifting the duty.
- **F4** s 11(1) "Where it appears to a court that the court will ... be exercising jurisdiction conferred by this Act
  or by a law ... relating to cross-vesting" -- `s 11(1) -- the law to be applied` -- when the court is not exercising
  cross-vested jurisdiction the answer is "not covered" (the court applies its ordinary law, which this Act does not
  state) -- "no" under the "where" ruling; "not covered" was taken because the question is "which law", not yes or no.
- **F5** s 6(1), (9), 6A(3) -- `s 6 -- transfer of a special federal matter` -- checked in the order s 6(9), s 6A(3),
  s 6(3) order, then the destination; a case caught by two of them gets the first answer -- any order gives "no
  transfer required", so only the wording changes.
- **F6** s 6A(2) "having regard to the interests of justice, including the desirability of related proceedings being
  heard in the same jurisdiction, the Federal Court ... considers it appropriate" -- `ss 5(3), (4), 6A(2) -- transfer
  into the NSW Supreme Court` -- the s 5(4)(b)(iii) input ("otherwise in the interests of justice that NSW decide it")
  stands for the federal court's s 6A(2) view -- a separate input.
- **F7** s 6(5)(b) (no period in the Act) -- `s 6(5)(b) -- the directed notice to the Attorneys-General` -- the period is
  the one the direction gives, counted in days from the day of the direction (that day is day 0; the last day is the
  direction day plus the period); notice is given on the day it reaches the second of the two Attorneys-General -- the
  direction may fix an end date or count clear days.
- **F8** s 7 (who hears an appeal from a decision s 7 does not name, or to a court it does not name) -- `s 7 -- where an
  appeal goes` -- "not covered" -- s 7(1)-(4) read as a complete code.
- **F9** ss 6(7), 6(8), 7(7), 5(8), 14(2) (savings and grants with no "only") -- their functions -- outside their terms
  "not covered" -- "no".
- **F10** s 6(3), (4) -- `s 6(3), (4) -- the Supreme Court keeping the case` -- the s 6(4) conditions are checked before
  the s 6(3) special reasons -- the other order; only the wording of the "no" changes.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags (its "not covered" answers are constructors). The
rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definition of State matter and the "if" conditions of s 6A(1) answer no when they fail; the
"where" conditions of ss 5(1)-(4), (6), 8, 10 answer no when they fail (ruling (b)); the flat negatives of ss 3(1)
("does not include"), 3A, 4(5), 7(1), (2) and 13 answer no (N2); the "only" of s 7(3), (4) answers no for any other
court; "if" in ss 6(3), (4) and 12 answers no when unmet. Unclosed lists and savings (ss 5(7), 5(8), 6(7), 6(8), 7(7),
14(2)) and courts or decisions the text does not name (ss 4, 7, 13) answer "not covered". The case-by-case sites are
forks F3 (an "unless" once met) and F4 (a "where" unmet on a "which law" question).

## What the Act turns out to say

1. **The Act binds courts NSW cannot bind.** Section 5(3) says the Supreme Court of another State "shall transfer", and
   s 5(4) says the Federal Court and the Federal Circuit and Family Court "shall transfer", to the NSW Supreme Court.
   A NSW Act cannot direct those courts by itself. These subsections work only through the matching cross-vesting Acts
   of the Commonwealth and the other States, and s 15 reads the Act down to NSW's power. They are encoded as written,
   and the answer says what the other court must do.
2. **Transfer gives no jurisdiction.** Sections 5(9) and 6A(4) say nothing in them "confers on a court jurisdiction that
   the court would not otherwise have". So a duty to transfer to a court that lacks jurisdiction cannot be performed.
   The encoding does not ask whether the receiving court has jurisdiction. It presumes that it does.
3. **The repeals leave gaps.** Sections 4(1), (2), 5(1)(b)(i), (iii) and 5(5) are repealed. Section 4 no longer vests
   NSW jurisdiction in the federal courts, and the s 5(1) duty to transfer to a federal court now has only one limb,
   (ii). These repeals appear to follow the High Court's decision in Re Wakim (1999). That decision is not part of the
   deposited text, and nothing in this encoding depends on it.
4. **Section 10 appears to have no work left to do.** It reaches matters "arising under Division 1 or 1A of Part V of
   the Trade Practices Act 1974". Section 3(3) reads a Commonwealth Act "as amended and in force for the time being".
   That Act is now the Competition and Consumer Act 2010 (Cth), and the consumer protection provisions moved to the
   Australian Consumer Law. If those Divisions have been repealed, no matter can arise under them. This was not checked
   against a deposited Commonwealth text. The encoding takes the facts as given. Asserted only as written.
5. **NSW has no State Family Court.** Sections 3(2), 4(4) and 7(5) work only for another State's Family Court, which in
   practice means the Family Court of Western Australia. Section 7(5) says an appeal from "a judge of a State Family
   Court" may be dealt with as if it raised no Schedule matter, but s 7 does not say where that appeal goes.
   The encoding answers "yes, s 7(5) applies", and otherwise "not covered". Asserted.
6. **"Territory" excludes the NT and the ACT.** Section 3(1) counts the NT and the ACT as States and says "Territory does
   not include" them. So "the Supreme Court of a Territory" in ss 4, 5 and 8 means an external Territory's court (for
   example Norfolk Island's). The glosses say so.
7. **The Act sets no time limit for a party.** Its only periods are in s 16, the 3 years and the 6 months, which are
   machinery. A party's one deadline is whatever period a court gives when it directs notice under s 6(5)(b). Even
   then, missing that period has no consequence stated in the Act. It only leaves s 6(4)(a) unmet, and the s 6(3) order
   cannot be made until the notice is given. Asserted through the regulative rule.
8. **No appeal from a transfer decision (s 13).** This covers a refusal to transfer as well as a transfer, since both
   are decisions "in relation to the transfer". Section 13 does not address judicial review or prerogative relief, so
   the encoding says nothing about them. Asserted.
9. **Section 6(9) speaks of an appeal "instituted in the Full Court of the Supreme Court"**, while s 7(3) and (4) decide
   which court an appeal must be instituted in. When a special federal matter that the trial court kept arises under a
   Schedule Act, the two sections could pull in different directions. The encoding answers each question under its own
   section.
10. **A slip in s 5(8)(a).** It says "the transferred proceedings" (plural), although the subsection defines "the
    transferred proceeding" (singular). The singular is read.
11. **Two "Attorney-General" spellings.** Most of the Act writes "Attorney-General", but s 16(2) writes "Attorney
    General". This does not matter here, because s 16 is out of scope.

## Before this is worth relying on

- Check the deposited text against legislation.nsw.gov.au for amendments after 14 July 2023.
- Deposit the Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987 (the special federal matter definition, the
  Schedule) and the ADJR Act s 3(1), so that those facts can be worked out instead of asked (findings 4, 5).
- Have a NSW practitioner review forks F3-F6 and findings 1, 2, 4 and 9.
- An independent test pass, and the human gates.

## Licence

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md. The L4 is Apache-2.0.
