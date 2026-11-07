# Jurisdiction of Courts (Cross-vesting) Act 1987 (NT) -- baseline encoding, a party to a civil proceeding

UNOFFICIAL. Copyright in Northern Territory legislation is owned by the Northern Territory. This encoding quotes the Act
under the NT copyright policy of 8 October 1996 and the licence ruling of 24 October 2026 (`SOURCE-LICENSE.md`); it is
not an official version of the Act.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module
(`ntjcxv-dates.l4`, built-in date functions only, no daydate), the rules and the 21 exported questions in
`ntjcxv-claims.l4`, and the worked cases in `ntjcxv-cases.l4`. The shape follows the Western Australian baseline of the
same scheme Act (`subjects/au/wa/jurisdiction-of-courts-cross-vesting-act-1987/encodings/baseline-2026-11/`), but every
rule and every expected value was written again from the Northern Territory text, which differs from the Western
Australian one in several places (findings 1, 2, 3 and 6).

The focus asked for: cross-vesting, as a claimant meets it. The Act is short (sections 1 to 16), so the whole operative
Act is encoded: which proceedings it reaches (s 3, s 3A), which courts outside the Territory may hear a Northern
Territory matter (s 4), when a proceeding must be transferred and who may ask (s 5), special federal matters (s 6),
where an appeal goes (s 7), removal into the Supreme Court (s 8), consumer law matters sent down to a lower court
(s 10, s 16), which law the court applies and what survives a transfer (s 11), costs (s 12), no appeal from a transfer
(s 13), and enforcement (s 14). The one duty with a deadline a party meets -- to give the Attorneys-General written
notice of a special federal matter within the time the Supreme Court directs (s 6(4), (5)(b)) -- is a regulative rule
run by EVALTRACE inside an exported question.

The Act sits in the claims set because a claim (an injury claim with a federal element, a claim related to proceedings
in another State, a consumer claim) can meet it at any stage: where it may be heard, whether it will be moved, which
law applies, and where an appeal lies.

## Edition

- **Act:** Jurisdiction of Courts (Cross-vesting) Act 1987 (NT), Act No. 41 of 1987, assented 15 October 1987,
  commenced 1 July 1988. The deposited text is reprint REPJ005, as in force at 1 January 2022 (the last amendment
  recorded being the Interpretation Amendment Act 2021), retrieved from the Northern Territory Legislation website on
  6 November 2026: `../../registers/source-bundle/Jurisdiction-of-Courts-Cross-vesting-Act-1987-NT-current-reprint-REPJ005.txt`.
  The register showed the Act in force, reprint REPJ005 current, on that day.
- **Numbers set elsewhere:** none. The Act fixes no period, amount or fee. The only time limit is one a court sets by
  direction (s 6(5)(b)), asked as a number of days.
- **Not deposited:** the Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987, whose definition of "special
  federal matter" (s 3(1)) and Schedule this Act borrows; the Family Law Act 1975 (Cth); the Competition and Consumer
  Act 2010 (Cth), Schedule 2 (the Australian Consumer Law); the Trade Practices Act 1974 (Cth); the Corporations Act
  2001 (Cth). Each is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 6(5)(b) rule with notice on day 29 of 28 asserted to be in time) was run once in a
scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ntjcxv-dates.l4` | 0 | 0 | 0 | 0 |
| `ntjcxv-claims.l4` | 0 | 0 | 0 | 0 |
| `ntjcxv-cases.l4` | 0 | 0 | 152 | 152 |

Every exported question has cases, with the edges: each route of s 5 on each finding, including the "otherwise in the
interests of justice" limb of s 5(1) (finding 2), the Family Court of Western Australia read in by s 3(2) as source
(s 5(3)) and destination (s 5(2)), and the routes s 5 does not name (one court to itself, another Supreme Court to the
Federal Court, a lower court); s 4 for each of the four courts, a matter that is not a Northern Territory matter, and the
s 3(1)(b) removed-matter limb; each paragraph group of the special federal matter definition and a paragraph s 6(2)
does not name; s 6(9) and an s 6(3) order together; notice to one Attorney-General only; the s 6(5)(b) notice before
the direction, on the day of it, on the last day and the day after, and not given with today the last day and the day
after; the regulative rule alone on day 0, the last day and the day after; each limb of s 7, a federal judge to his or
her own Full Court (not this Act), and s 7(5) with each of its two matters missing; each condition of s 10 failing in
turn, an Australian Consumer Law provision outside the list (Part 3-5), and s 16; s 11(1)(b) before s 11(2); s 14 for
each court, and s 14(3) with each condition failing.

**No mirror cases.** One seat.

## Seat

**A party to a civil proceeding** (`ntjcxv-claims.l4`), usually the person bringing a claim (the plaintiff, applicant or
claimant): "Does this Act deal with my proceeding?", "Can a court outside the Territory hear my Northern Territory
matter?", "Must my proceeding be transferred, and where?", "Must my related proceeding follow?", "Can I apply for it?",
"Can my lawyer follow it?", "Must my special federal matter go to a federal court?", "Can the Supreme Court keep it?",
"Have I given the notice the court directed?", "Can I still get urgent interim relief?", "Is the decision invalid
because it was not transferred?", "Where can my appeal go?", "Must the Full Court send my appeal on?", "Can my case be
removed to the Supreme Court?", "Can my consumer law case go to a lower court?", "Which law will the court apply?", "Do
the steps already taken count?", "Can the new court order the costs of the earlier stage?", "Can I appeal the
transfer?", "Can I enforce the judgment in the Territory?", "Does a Territory law that speaks of the Supreme Court cover
what the other court did?".

The Act speaks almost entirely to courts ("the Supreme Court shall transfer", "may order") and to the Administrator
(s 15); the encoding turns that into what it means for the party. The courts, the Administrator and the
Attorneys-General get no seat: what a court finds, considers or is satisfied of is asked as a fact. No second seat was
written: the party answering the claim asks the same questions with the same answers (any party may apply, s 5(7)).

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number. The Commonwealth
  cross-vesting Act's definitions are not brought in (not deposited): asked as facts.
- **The actors the text names.** Followed: the Supreme Court and its Full Court, the Federal Court, the Family Court,
  the Supreme Courts of other States and Territories, a State Family Court, the High Court, lower Territory courts,
  tribunals, the Attorneys-General, a party, a barrister or solicitor.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the court finds a transfer
  "more appropriate" or "otherwise in the interests of justice" (s 5); special reasons and a reasonable time (s 6(3),
  (4)); urgent relief in the interests of justice (s 6(7)); inadvertence (s 6(8), s 7(7)); whether the interests of
  justice require the Full Court to go on (s 7(6)); the s 8 grounds; the s 10 conditions.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "proceeding" (excludes criminal),
  "party" (includes an intervener), "Northern Territory matter", the s 3(2) reading of "Supreme Court of a State",
  "Full Court" (includes the court of appeal). Asked: "special federal matter" and its paragraph, the Schedule Acts,
  Division 1 of Part 9.6A of the Corporations Act, the Australian Consumer Law and Trade Practices Act provisions, "State
  Family Court" (taken as the Family Court of Western Australia).
- **One case is the text's natural unit.** Followed: one proceeding (or one appeal, one judgment).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** ss 3, 3A, 4, 5, 6 (other than s 6(10)), 7, 8, 10, 11, 12, 13, 14, 16; s 9 folded into the s 4 and s 5 answers
(the Supreme Court may exercise cross-vested jurisdiction and hear a proceeding transferred to it).

**Out, and why.**
- s 1 (short title), s 2 (commencement): no rule.
- s 15 (suspension or cessation of the Act by the Administrator's notice in the Gazette): machinery addressed to the
  Administrator. No notice under it is recorded in the reprint's endnotes, so the Act is taken as in force in relation
  to the Commonwealth and every State.
- s 6(10) (the former s 6 continues for proceedings pending before 1 March 1993): transitional, spent in practice.
- s 16(1)'s "on or after the commencement of this section" (1 January 2011): always met now; not asked.
- The Commonwealth definitions and Schedule: not deposited; asked.
- No requirement ledger exists for the Northern Territory, and none was raised: no scenario life has reached this Act.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(1) "proceeding does not include a criminal proceeding", s 3A -- every question about a pending proceeding
  (ss 4, 5, 5(6), 6, 7, 8, 10, 16) -- a criminal proceeding or the Corporations Act jurisdiction gets the text's no
  first -- for s 7(1), (2) and (4), which speak of "an appeal", the gate not applying.
- **F2** s 3(2) -- `a Supreme Court of another State, read with s 3(2)` -- "the Supreme Court of another State" in s 5(2),
  (3), s 10(1)(a) and s 16(1)(a) includes the Family Court of Western Australia (the only State Family Court); s 4(3) is
  excepted, and s 4(4) covers that court separately -- reading s 3(2) as reaching only the bare words "the Supreme Court
  of a State".
- **F3** s 5(1)-(4), limbs (i) and (ii) -- `s 5 -- must my proceeding be transferred` -- one input, "more appropriate",
  stands for both (each ends "it is more appropriate that ... be determined by" the other court) -- two inputs, with
  the relationship to another pending proceeding asked separately.
- **F4** "the State" in s 5(3)(b)(ii)(B), s 5(4)(b)(ii)(B), s 6(4)(a), s 8(1)(a)(i), s 10(1)(e), s 16(1)(e) -- the s 6(3),
  s 8 and s 10 questions -- read as the Northern Territory (the Act's "State" includes it, and these places speak of the
  enacting jurisdiction) -- a State of the Commonwealth.
- **F5** s 6(9), s 6(3) -- `s 6 -- must my special federal matter go to a federal court` -- order of answers: s 6(9),
  then an s 6(3) order made -- the other order (the outcome, no required transfer, is the same).
- **F6** s 5(7) -- `s 5(7) -- can I apply for a transfer` -- a person who is neither a party nor an intervener gets
  NOTHING-kind (the list is not closed with "only") -- the text's no.
- **F7** s 6(5)(b) -- `s 6(5)(b) -- have I given the notice in time` and the regulative rule -- the deadline is the number
  of days the direction allows, counted from the day of the direction; a notice on the last day is in time, the day
  after is not; a notice given before the direction counts as day 0 -- the direction may fix a date or count
  differently (the Act sets no time).
- **F8** s 7(4) "as the case requires" -- `s 7 -- where can my appeal go` -- either federal Full Court (or the High
  Court) is a "yes" -- asking which Full Court the Schedule Act matter belongs to.
- **F9** s 7(6) "unless the interests of justice require" -- `s 7(6) -- must the Full Court send my appeal to a federal
  Full Court` -- once the "unless" is met, "no" (the Court may go on, and s 7(7) saves its decision) -- NOTHING (the text
  says only that it need not transfer). One of the six site-by-site questions of 2026-11-05.
- **F10** s 6(8), s 7(7) -- `s 6(8), s 7(7) -- is the decision invalid because it was not transferred` -- outside
  inadvertence (and s 7(6)): NOTHING-kind, "this Act does not say" -- "invalid" (the text's no to the saving).
- **F11** s 5, a route the Act does not name (one court to itself; another Supreme Court to a federal court; a federal
  court to another Supreme Court; a lower court) -- `s 5 -- must my proceeding be transferred` -- NOTHING-kind ("the
  cross-vesting Act of the Commonwealth or of a State may") -- the text's no.
- **F12** s 6(1), (2) -- `s 6 -- must my special federal matter go to a federal court` -- a special federal matter under
  a paragraph s 6(2) does not name: the duty to transfer stands (s 6(1)), NOTHING-kind as to where (finding 3) -- no
  duty at all.
- **F13** s 6(7) -- `s 6(7) -- can the Supreme Court still give me urgent interim relief` -- relief not urgent and
  interlocutory: NOTHING-kind (outside the subsection's wording); urgent interlocutory relief not in the interests of
  justice: the text's no (its "if") -- the text's no for both.
- **F14** s 13 -- `s 13 -- can I appeal that decision` -- other decisions: NOTHING-kind -- the text's no.
- **F15** s 14(1), (2) -- `s 14(1), (2) -- can I enforce the judgment in the Northern Territory` -- a judgment of another
  court, or not given in cross-vested jurisdiction: NOTHING-kind -- the text's no.
- **F16** s 7 -- `s 7 -- where can my appeal go` -- a federal judge's decision appealed to that court's own Full Court,
  and an appeal from a State Family Court judge lacking either of the s 7(5) matters: NOTHING-kind (Commonwealth or
  Western Australian law governs) -- the text's no.
- **F17** s 10(1)(b), s 16(1)(b) "any of the following provisions" -- `s 10, s 16 -- can my consumer law case go to a lower
  court` -- a provision outside the list (for example Part 3-2 or Part 3-5 of the Australian Consumer Law): the text's
  no (a closed list after "applies if") -- NOTHING-kind.
- **F18** s 8(1)(a)(ii) "a tribunal established by or under an Act" -- `s 8 -- can my proceeding be removed to the
  Supreme Court` -- asked as the person's statement, "Act" taken as a Northern Territory Act -- any Act, including a
  Commonwealth one.

Sites decided without a fork line: s 3(1) and s 3A are flat negatives (the text's no); s 4(5), s 7(1), (2) and s 13 are
flat negatives ("does not", "shall not be instituted", "does not lie"); s 7(3), (4) are closed with "only"; ss 5, 5(6),
7(6), 8, 11(1), 11(3), 12, 14(3) fail on "where" (ruling (b) of 2026-11-05), s 5(8), 6(3), 6(7), 12 on "if", s 10 and
s 16 on "applies if": the text's no; "Northern Territory matter" is a "means" definition.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding answers with a choice from a list rather than a MAYBE BOOLEAN: the answers marked "NOTHING-kind" are the
NOTHING answers, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The notice the court directs under s 6(5)(b) is the regulative rule (`MUST give ... WITHIN` the days directed, `LEST
BREACH`), run by EVALTRACE inside the question; outside the period the answer is the text's no (ruling (a), read with the
direction).

## What the Act turns out to say

1. **The Territory Act still gives the federal courts Territory jurisdiction.** s 4(1) and (2) say the Federal Court and
   the Family Court "ha[ve] and may exercise" original and appellate jurisdiction in Northern Territory matters. The
   Western Australian Act deleted its equivalents in 2001, after the High Court held in Re Wakim; Ex parte McNally
   (1999) 198 CLR 511 that a State cannot confer jurisdiction on a federal court. Whether that reasoning reaches a law of
   a self-governing Territory is a question of Commonwealth constitutional law not deposited here. Encoded as written,
   with the answer saying "as the text reads" and pointing here. Asserted.
2. **The NT s 5(1) has an "otherwise in the interests of justice" limb.** Unlike the Western Australian s 5(1), the
   Territory's s 5(1)(b)(iii) lets the Supreme Court transfer to the Federal Court or the Family Court where it is
   "otherwise in the interests of justice", not only where "more appropriate". Asserted.
3. **The paragraph letters of the special federal matter definition do not agree across the scheme.** NT s 6(2) sends
   matters under paragraphs (a) to (e) to the Federal Court and paragraph (ab) to the family courts; the Western
   Australian s 6(2) names paragraph (ba) for the family courts. One of them follows a superseded lettering of the
   Commonwealth definition, which is not deposited. The encoding asks the paragraph and offers a third choice for a
   paragraph s 6(2) does not name: the duty to transfer stands, the destination is NOTHING-kind (fork F12). Asserted.
4. **s 6(6)(a) has words missing.** It reads "special federal matters should be heard by the Federal Court or mentioned
   in subsection (2)(b)"; s 6(1) shows the intended words, "or a court mentioned in subsection (2)(b)". Read that way; no
   answer turns on it.
5. **"That other court" in s 5(4)(b)(iii) has no antecedent.** s 5(4) runs from the Federal Court or the Family Court
   (the "first court") to the Supreme Court; limb (iii) speaks of the proceeding being determined "by that other court",
   though no "other court" is defined in the subsection (the words look carried over from s 5(5)). Read as the Supreme
   Court, the destination named in the closing words. Asserted (s 5(4) on an "interests of justice" finding).
6. **s 8(1)(b) has limbs (i) and (iii) but no (ii).** The Western Australian s 8(1)(b) has (i) and (ii) with the same
   words as the NT (i) and (iii). Whether the gap is a former limb omitted without renumbering, or an artefact, cannot
   be told from the reprint; the two limbs present are encoded.
7. **Personal injury consumer claims are not among the s 10 matters.** s 10 lets a superior court send a consumer case
   down to a lower Territory court only for matters under Part 3-1 Divisions 1, 2, 4 or 5, Part 3-3 and Part 3-4 of the
   Australian Consumer Law (as a law of the Commonwealth). Part 3-2 (consumer guarantees) and Part 3-5 (manufacturers'
   liability for goods with safety defects), the provisions a claim for injury from a defective product usually rests
   on, are not listed. Asserted (Part 3-5: the text's no, fork F17).
8. **s 3(2) and s 7(5) have little or no Territory field.** The Territory has no State Family Court, so s 3(2) changes
   nothing about "the Supreme Court"; it matters only where the Act speaks of the Supreme Court of another State (fork
   F2). s 7(5) governs appeals from a judge of a State Family Court -- in practice the Family Court of Western Australia,
   whose appeals a Territory law would not ordinarily govern. Encoded as written.
9. **"Family Court" is not defined in the Act**, and the Family Court of Australia was restructured by Commonwealth law
   in 2021. Whether the reference now reaches its successor depends on Commonwealth and Territory interpretation law not
   deposited here. Not checked.
10. **s 16 may be spent.** It covers matters under Part V, Divisions 1 and 1A of the Trade Practices Act 1974, since
   renamed and its consumer provisions moved into the Australian Consumer Law. Encoded as written.
11. **The Act sets no time limit of its own.** The only deadline a party meets is the time the Supreme Court sets when
   it directs a party to notify the Attorneys-General (s 6(5)(b)); the encoding takes it as a number of days (fork F7).

## Before this is worth relying on

- The Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987 (its "special federal matter" definition and its
  Schedule), so those can be worked out rather than asked, and finding 3 settled.
- A check of findings 1, 6, 9 and 10 against current law and an authorised print of the Act.
- A lawyer's view on forks F2, F4, F9, F11, F12, F16 and F17; an independent test pass and a human gate.
