# Jurisdiction of Courts (Cross-vesting) Act 1987 (WA) -- baseline encoding, a party to a civil proceeding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`jcxv-dates.l4`,
built-in date functions only, no daydate), the rules and the 20 exported questions in `jcxv-claims.l4`, and the worked
cases in `jcxv-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act is short (sections 1 to 16), so the whole operative Act is
encoded: which proceedings it reaches (s 3, s 3A), which courts outside Western Australia may hear a Western Australian
matter (s 4), when a proceeding must or may be transferred and who may ask (s 5, s 6A), special federal matters (s 6),
where an appeal goes (s 7), removal into the Supreme Court (s 8), Trade Practices Act matters (s 10), which law the court
applies and what survives a transfer (s 11), costs (s 12), no appeal from a transfer (s 13), and enforcement (s 14). The
one duty with a deadline a party meets -- to give the Attorneys-General written notice of a special federal matter within
the time the Supreme Court directs (s 6(4), (5)(b)) -- is a regulative rule run by EVALTRACE inside an exported question.

The Act sits in the claims set because a claim (an injury claim against a Commonwealth body, a claim with a federal
element, a claim related to proceedings in another State) can meet it at any stage: where it may be heard, whether it
will be moved, and where an appeal lies.

## Edition

- **Act:** Jurisdiction of Courts (Cross-vesting) Act 1987 (WA), Act No. 68 of 1987, assented 22 November 1987, in
  operation (other than s 1) from 1 July 1988. The deposited text is the compilation on the Western Australian
  Legislation website when retrieved on 7 September 2026, the last amendment recorded being the Legal Profession Uniform
  Law Application Act 2022 s 424 (in force 1 July 2022): `../../registers/source-bundle/mrdoc_45308.txt`.
- **Numbers set elsewhere:** none. The Act fixes no period, amount or fee. The only time limit is one a court sets by
  direction (s 6(5)(b)), asked as a number of days.
- **Not deposited:** the Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987, whose definition of "special
  federal matter" (s 3(1)) and Schedule this Act borrows; the ADJR Act 1977 (Cth); the Family Law Act 1975 (Cth); the
  Trade Practices Act 1974 (Cth). Each is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 6(5)(b) rule with notice on day 29 of 28 asserted to be in time) was run once in a
scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `jcxv-dates.l4` | 0 | 0 | 0 | 0 |
| `jcxv-claims.l4` | 0 | 0 | 0 | 0 |
| `jcxv-cases.l4` | 0 | 0 | 144 | 144 |

Every exported question has cases, with the edges: s 5(1) with only an "interests of justice" finding (no transfer);
each route of s 5 and the routes it does not provide; the Family Court of Western Australia read in (s 3(2)) and read out
(s 5(3)); s 6A with one element missing; each paragraph group of the special federal matter definition, and paragraph
(ba) with the s 6A facts (s 6A cannot apply); notice to one Attorney-General only; the s 6(5)(b) notice on the day of
the direction, before it, on the last day and the day after, and not given with today the last day and the day after; the
regulative rule alone on day 0, the last day and the day after; each condition of s 10 failing in turn; each limb of the
appeal rules in s 7.

**No mirror cases.** One seat.

## Seat

**A party to a civil proceeding** (`jcxv-claims.l4`), usually the person bringing a claim (the plaintiff, applicant or
claimant): "Does this Act deal with my proceeding?", "Can a court in another State hear my matter?", "Must my proceeding
be transferred, and where?", "Can I apply for it?", "Can my lawyer follow it?", "Must my special federal matter go to a
federal court?", "Can the Supreme Court keep it?", "Have I given the notice the court directed?", "Can I still get urgent
interim relief?", "Where can my appeal go?", "Can my case be removed to the Supreme Court?", "Which law will the court
apply?", "Do the steps already taken count?", "Who orders the costs of the earlier stage?", "Can I appeal the transfer?",
"Can I enforce the judgment?".

The Act speaks almost entirely to courts ("the Supreme Court shall transfer", "may order"); the encoding turns that into
what it means for the party. The courts and the Attorneys-General get no seat: what a court finds, considers or is
satisfied of is asked as a fact. No second seat was written: the party answering the claim asks the same questions with
the same answers (the defendant may apply for a transfer as any party may, s 5(8)).

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number. The Commonwealth
  cross-vesting Act's definitions are not brought in (not deposited): asked as facts.
- **The actors the text names.** Followed: the Supreme Court (and, by s 3(2), the Family Court of Western Australia), the
  Court of Appeal, the Federal Court, the Family Court, the Supreme Courts of other States and Territories, the High
  Court, courts of summary jurisdiction, tribunals, the Attorneys-General, a party, a legal practitioner.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the court finds a transfer
  "more appropriate" or "otherwise in the interests of justice" (s 5); whether it considers transfer appropriate (s 6A);
  special reasons and a reasonable time (s 6(3), (4)); urgent relief in the interests of justice (s 6(7)); inadvertence
  (s 6(8), s 7(8)); whether the interests of justice require the Court of Appeal to go on (s 7(7)); the s 8 grounds.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "proceeding" (excludes criminal),
  "party" (includes an intervener), "State matter", the s 3(2) reading of "the Supreme Court", "federal matter
  proceeding" (s 6A(1)). Asked: "special federal matter" and its paragraph, the Schedule Acts, the ADJR Act enactments,
  Part 9.6A Division 1 of the Corporations Act, Part V Divisions 1 and 1A of the Trade Practices Act.
- **One case is the text's natural unit.** Followed: one proceeding (or one appeal, one judgment).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** ss 3, 3A, 4, 5, 6, 6A, 7, 8, 10, 11, 12, 13, 14; s 9 folded into the s 4 and s 5 answers (the receiving court may
exercise the jurisdiction and hear the transferred proceeding).

**Out, and why.**
- The preamble, s 1 (short title and commencement), s 2 (purpose): no rule.
- s 15 (reading down to the State's legislative power): a rule of construction for the court, nothing a party can state.
- s 16 (suspension or cessation by proclamation): machinery; no proclamation under it is recorded in the compilation, so
  the Act is taken as in force in relation to every State and the Commonwealth.
- The transitional s 7 of the Jurisdiction of Courts (Cross-vesting) Amendment Act 1994 (in the notes): proceedings
  pending before 26 September 1998 under the former s 6; spent in practice.
- The Commonwealth definitions and Schedule: not deposited; asked.
- No requirement-ledger entry exists for this Act in `subjects/au/wa/requirements.jsonl`, and none was raised: no
  scenario life has reached it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(1) "proceeding does not include a criminal proceeding", s 3A -- every question about a pending proceeding
  (ss 4, 5, 5(7), 6, 7, 8, 10) -- a criminal proceeding or the Corporations Act jurisdiction gets the text's no first --
  for s 7(1), (2) and (4), which speak of "an appeal" rather than "a proceeding", the gate not applying.
- **F2** s 3(2) -- `the Supreme Court, read with s 3(2)` -- "the Supreme Court" in ss 5(1), (2), (5), 6, 6A, 8 and 14
  includes the Family Court of Western Australia, but not in ss 4(3), (6), (7), 5(3), (4), 7(4) -- reading s 3(2) only
  where the context fits (it makes s 6(2)(b)(ii) odd: finding 2).
- **F3** s 5(2)-(5), limbs (i) and (ii) -- `s 5 -- must my proceeding be transferred` -- one input, "more appropriate",
  stands for both (each ends "it is more appropriate that ... be determined by" the other court) -- two inputs, with the
  relationship to another pending proceeding asked separately.
- **F4** s 6A(2), (3) "considers it appropriate, having regard to the interests of justice" -- the same function -- either
  a "more appropriate" or an "interests of justice" finding counts -- only an express "appropriate" finding.
- **F5** s 5, a route the Act does not name (Federal Court to Family Court; another Supreme Court to the Federal Court;
  another Supreme Court to the Family Court of Western Australia) -- the same function -- NOTHING-kind ("the
  cross-vesting Act of the Commonwealth or of another State may") -- the text's no.
- **F6** s 6(1)(b), (9), s 6A(3) -- `s 6 -- must my special federal matter go to a federal court` -- order of answers: s
  6(9), then s 6A(3), then an s 6(3) order made -- answering an s 6(3) order first where several apply (the outcome,
  no required transfer, is the same).
- **F7** s 6(5)(b) -- `s 6(5)(b) -- have I given the notice in time` and the regulative rule -- the deadline is the number
  of days the court's direction allows, counted from the day of the direction; a notice on the last day is in time, the
  day after is not; a notice given before the direction counts as day 0 -- the court's direction may fix a date or
  count differently (the Act sets no time).
- **F8** s 7(5) "as the case requires" -- `s 7 -- where can my appeal go` -- either Full Court (or the High Court) is a
  "yes" -- asking which Full Court the Schedule Act matter belongs to.
- **F9** s 7(7) "unless the interests of justice require" -- `s 7(7) -- must the Court of Appeal send my appeal to a Full
  Court` -- once the "unless" is met, "no" (the Court may go on, and s 7(8) saves its decision) -- NOTHING (the text says
  only that it need not transfer). One of the six site-by-site questions of 2026-11-05.
- **F10** s 8(1)(a)(i) "a court, other than the Supreme Court, of the State", read with s 3(2) -- `s 8 -- can my proceeding
  be removed to the Supreme Court` -- the Family Court of Western Australia is not a source court for removal -- it is
  (s 3(2) read as not reaching "other than" phrases).
- **F11** s 7(4) "to the Supreme Court" -- `s 7 -- where can my appeal go` -- includes the Court of Appeal -- the Supreme
  Court at first instance only.
- **F12** s 5(8) -- `s 5(8) -- can I apply for a transfer` -- a person who is neither a party nor an intervener gets
  NOTHING-kind (the list is not closed with "only") -- the text's no.
- **F13** s 6(7) -- `s 6(7) -- can the Supreme Court still give me urgent interim relief` -- relief not urgent and
  interlocutory: NOTHING-kind (outside the subsection's wording); urgent interlocutory relief not in the interests of
  justice: the text's no (its "if") -- the text's no for both.
- **F14** s 4(3), (4) -- `s 4 -- can a court outside Western Australia hear my matter` -- a federal court, or a matter
  that is not a State matter: NOTHING-kind (no "only") -- the text's no.
- **F15** s 6A(3)(b) -- `s 5 ...` and `s 6 ...` -- not asked separately: s 6A(1)(c) already requires the State matter
  proceeding to be pending in a Western Australian court (finding 6) -- a separate input.
- **F16** s 13 -- `s 13 -- can I appeal that decision` -- other decisions: NOTHING-kind -- the text's no.
- **F17** s 6(8), s 7(8) -- `s 6(8), s 7(8) -- is the decision invalid because it was not transferred` -- outside
  inadvertence (and s 7(7)): NOTHING-kind, "this Act does not say" -- "invalid" (the text's no to the saving).

Sites decided without a fork line: s 3(1) and s 3A are flat negatives (the text's no); s 7(1), (2), (4) and s 13 are flat
negatives ("shall not be instituted", "does not lie"); s 7(3), (5) are closed with "only"; ss 5, 5(7), 7(7), 8, 10, 11(1),
11(3), 12 fail on "where" (ruling (b) of 2026-11-05), s 5(9), 6(1), 6(3), 6(7), 12 on "if": the text's no; the
"State matter" and "federal matter proceeding" definitions are "means" definitions.

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

1. **The Western Australian Act no longer gives the federal courts any State jurisdiction.** s 4(1) and (2) are deleted
   (Acts Amendment (Federal Courts and Tribunals) Act 2001, Part 6); what remains vests Western Australian jurisdiction
   only in the Supreme Courts and State Family Courts of other States and Territories (s 4(3), (4)). Transfers into the
   Federal Court and the Family Court under s 5(1) and s 6 remain, resting on federal jurisdiction (s 5(10): nothing
   confers jurisdiction a court would not otherwise have). Asserted (s 4, federal court: NOTHING-kind).
2. **s 3(2) reaches further than it seems to mean.** Reading "the Supreme Court" as including the Family Court of
   Western Australia everywhere except the listed subsections makes that court a "first court" under s 5(1) and (2), a
   destination under s 5(5) and s 6A(2), a court that must transfer special federal matters under s 6 -- and so, for a
   paragraph (ba) matter, s 6(2)(b)(ii) names the Family Court of Western Australia as a destination for a proceeding
   that may already be in it. Encoded as written (fork F2); asserted for s 5(1), s 5(5), s 6 and s 14.
3. **s 5(1) has no "otherwise in the interests of justice" limb.** s 5(2), (3), (4) and (5) each allow a transfer that is
   "otherwise in the interests of justice"; s 5(1), to the Federal Court or the Family Court, only where it is "more
   appropriate" (the interests of justice being one of the matters weighed). Asserted.
4. **"Family Court" means the Family Court of Australia** (s 3(1)). The text has not been updated for the Commonwealth's
   restructuring of that court in 2021; whether the reference now reaches its successor depends on Commonwealth law not
   deposited here. Not checked against a deposited source.
5. **s 10 may be spent.** It refers to Divisions 1 and 1A of Part V of the Trade Practices Act 1974 (Cth). That Act has
   since been renamed and its consumer protection provisions moved into the Australian Consumer Law; whether anything
   now "arises under" those Divisions is a question of Commonwealth law not deposited here. Encoded as written.
6. **s 6A(3)(b) repeats s 6A(1)(c).** A "federal matter proceeding" already requires the related State matter proceeding
   to be pending in a court of this State; s 6A(3)(b) asks it again. Not asked twice (fork F15).
7. **s 4(4) depends on another State having a State Family Court.** Only Western Australia has one (a court to which s
   41 of the Family Law Act 1975 applies by proclamation), so s 4(4) may have no present field. Not checked; encoded as
   written.
8. **The Act sets no time limit of its own.** The only deadline a party meets is the time the Supreme Court sets when it
   directs a party to notify the Attorneys-General (s 6(5)(b)); the encoding takes it as a number of days (fork F7).
9. **Conversion artefacts in the deposited text.** The body reads "Crossvesting", "AttorneyGeneral",
   "firstmentioned" and "subsubparagraph" where the authorised text has hyphens; the short title and the compilation
   notes have "Cross-vesting". Not law; the deposited text is not altered.

## Before this is worth relying on

- The Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987 (its "special federal matter" definition and its
  Schedule), so those can be worked out rather than asked.
- A check of findings 4, 5 and 7 against current Commonwealth law.
- A lawyer's view on forks F1, F2, F5, F9, F10 and F11, and on finding 2; an independent test pass and a human gate.
