# Jurisdiction of Courts (Cross-vesting) Act 1987 (SA) -- baseline encoding, the party to a civil proceeding

> **Edition.** The text encoded is the register's current version of 4 September 2006, fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons it does **not** come from the Open Australian Legal Corpus, so the corpus's
> "may be out of date" warning does not apply; but the Act's own note warns that references to other legislation and to
> bodies are not updated, and several are stale (findings 3, 4 and 5). Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`jccv-core.l4`) holds every rule; the seat layer (`jccv-seat.l4`) asks the
questions and restates none of them; the cases (`jccv-cases.l4`) assert every question. Answers are named outcomes
(enumerations), not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used: where the text says no in its own words the
outcome is a "no: ..." naming the provision, and where the text is silent or its list is not closed the outcome says
"not covered" or "s N does not help", which follows the 2026-11-04 and 2026-11-05 rulings in substance. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

**No regulative rules.** The Act fixes no time limit and puts no duty with a deadline on a person: its "shall" and
"must" bind courts (transfer, s 5, s 6, s 7(6)) and have no period, and its one step a party may be told to take (give
the s 6(4) notice when directed under s 6(5)(b)) has none either. A `DEONTIC` would add nothing a decision function does
not say, so none is written.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Jurisdiction of Courts (Cross-vesting) Act 1987 (SA), version 4.9.2006 (the last amendment, the Statutes
  Amendment (New Rules of Civil Procedure) Act 2006, Part 42), deposited at
  `../../registers/source-bundle/jurisdiction-of-courts-cross-vesting-act-1987.txt` (text sha256 a62df615...8483ac553 per
  its `.meta.json`). The Current Titles list of 22 September 2026 gave the same version.
- **No regulations.** The Act sets no numbers and has no regulations.
- **Not deposited, so inputs:** the Commonwealth Act's definition of "special federal matter" (s 3(1) borrows it) and its
  Schedule (s 7); the Administrative Decisions (Judicial Review) Act 1977 (Cth) definition of "enactment" (s 6A); the
  Corporations Act 2001 (Cth) Part 9.6A (s 3A); the Trade Practices Act 1974 (Cth) Part V (s 10).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `jccv-core.l4` | 0 | 0 | 0 | 0 |
| `jccv-seat.l4` | 0 | 0 | 0 | 0 |
| `jccv-cases.l4` | 0 | 0 | 120 | 120 |

Negative control: with s 7's single-judge branch keyed on "another matter too" instead of "a Schedule Act matter", and
s 6(9) moved below the s 6(3) order, the cases failed exactly the 2 predicted assertions (the single-Schedule-matter
appeal; the (ab) appeal with every flag set); the core was restored and rechecked (120 of 120).

The Act has no numbers or dates, so the edges are logical: each limb of every "or" (s 3(1) State matter (a)/(b); s 5(2),
(3), (4) (i)/(ii)/(iii); s 8(1)(b)(i)/(ii)), each conjunct of every "and" (s 5(6), s 5(8), s 6A(1)(a)-(c), s 7(6), s 10
(a)-(e)), and the order in which provisions displace one another (criminal before court in s 4; s 6(9) before a s 6(3)
order before s 6A(4); convenience before special reasons before notice before time in s 6(3)-(4); s 6A(3) before
s 5(4)'s grounds).

## Seat

**The party (required): the person bringing a civil claim, or answering one, whose proceeding may be in or move between
the Supreme Court of South Australia, another State's or Territory's Supreme Court, the Federal Court and the Family
Court** (`jccv-seat.l4`, 24 questions). Every question is one that person would ask: "Does the scheme cover my
proceeding?", "Can a court outside South Australia hear my claim?", "Must my proceeding be transferred, and where?",
"Can I ask for a transfer?", "Can my lawyer follow it?", "Can the Supreme Court keep my special federal matter?", "Can I
get urgent orders meanwhile?", "Is the decision invalid?", "Where does my appeal go?", "Can I appeal the transfer?",
"Which law applies to my claim?", "Do the steps already taken count?", "Who pays the costs so far?", "Can I enforce the
judgment?". Provisions addressed to the courts are encoded as what they mean for the party: where the proceeding goes,
what the party may ask for, what is barred.

No seat for any court or Attorney-General. A second party seat (the defendant) would ask the same questions with the
same answers, so none is written.

The 2026-10-18 defaults:

- **The Act alone.** Followed: no regulations exist; the Commonwealth Act's definitions and Schedule are asked as facts.
- **The actors the text names.** Followed: party (including an intervener), the Supreme Court, the Full Court, the
  Supreme Courts of other States and Territories, the State Family Court, the Federal Court, the Family Court, the High
  Court, the Attorneys-General, a barrister or solicitor, a tribunal.
- **Judgments answered conditionally.** Followed: "it appears to the court", "more appropriate", "the interests of
  justice", "special reasons", "satisfied", "a reasonable time", "considers appropriate" are all inputs worded "the court
  finds ...".
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 3(1) "proceeding" (no criminal proceeding),
  "party" (includes an intervener), "State matter" ((a) or (b)), "State" and "Territory" (in the court choices), s 6A(1)
  "federal matter proceeding"; borrowed: "special federal matter" and the Schedule (Commonwealth Act), "enactment"
  (ADJR Act), the Corporations Act Part 9.6A jurisdiction, Trade Practices Act Part V matters, "written law", "Act" in
  s 8(1)(a)(ii).
- **One case:** one proceeding (with, where the text needs it, the one related proceeding).
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** s 1, s 15 (suspension and expiry by proclamation), the preamble (read for purpose only).

## Scope

**In (the whole operative Act):** s 3 (definitions), s 3A, s 4(3)-(5), s 5(1)-(4), (6)-(9), s 6 (all of it), s 6A (all
of it), s 7, s 8, s 9 (folded into the transfer answers: the Supreme Court may hear what is transferred to it), s 10,
s 11(1), (3), s 12, s 13, s 14(2), (3).

**Out, and why:**

- s 1 (short title), s 15 (the Governor's proclamations suspending, modifying or ending the Act): machinery; the
  person can do nothing under it. The Act "will expire on a date to be fixed by proclamation" (s 15(3)); none is
  recorded in the deposited text, so the encoding assumes the Act is in force.
- s 5(9) and s 6A(5) ("nothing in this section confers jurisdiction ...") and s 6A(6) (the meaning of "interests of
  justice" elsewhere): interpretive, with no answer of their own; s 6A(6)'s point is carried in the s 6A answers.
- s 3(2) (a Supreme Court of a State includes its State Family Court) and s 3(3) (Commonwealth Acts as amended):
  used in reading, no question of their own.
- The 1993 transitional provision (s 7 of the Statutes Amendment (Attorney-General's Portfolio) Act 1993, in the
  legislative history): it governs proceedings pending in December 1993 only.

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** s 4, `may that court hear the State matter (s 4)`: for the Federal Court, the Family Court, a South Australian
  lower court or another court, "not covered: ... this Act does not say", because s 4 is silent about them; the other
  reading is a flat "no" (s 4(1) and (2), which reached the federal courts, were deleted).
- **F2** s 5(7), `who may apply for a transfer (s 5(7))`: a non-party gets "the Act gives you no application", not
  "no", because s 5(7)'s list is not closed with "only".
- **F3** s 6, `must the special federal matter be transferred (s 6)`: the order is s 6(9) (appeal), then a s 6(3)
  order, then s 6A(4), then the destination; the other reading lets s 6A(4) answer before a s 6(3) order (the result is
  "no transfer" either way, the reason differs).
- **F4** s 6(3), `may the Supreme Court keep the special federal matter (s 6(3)-(5))`: reasons that are only the
  parties' convenience answer "no" even if the court says it is satisfied; mixed reasons are left to the court (input
  "special reasons"). The other reading asks only whether the court is satisfied.
- **F5** s 7(3), (4), `where does the appeal go (s 7)`: an appeal with one Schedule Act matter among others goes under
  s 7(4) ("a matter ... is a matter arising under an Act specified in the Schedule"); s 7(3) needs all ("the only
  matters") to be non-Schedule.
- **F6** s 7(5): applies only to an appeal from a judge of a State Family Court with both kinds of matter; every other
  State Family Court appeal is "not covered". The other reading routes those under s 7(3) or (4) via s 3(2).
- **F7** s 13(a), `can the decision be appealed (s 13)`: "a decision ... in relation to the transfer or removal" is
  read to include a refusal to transfer; the other reading confines it to orders that transfer or remove.
- **F8** s 14(3), `does South Australian law treat it as done by the Supreme Court (s 14(3))`: a law relating to the
  enforcement of judgments gets "not under s 14(3)", not "no" ("(not being a law relating to ...)" is the kind of
  "(other than X)" the 2026-11-05 ruling leaves to the encoder).
- **F9** s 11(1)(b), `which law will the court apply (s 11(1))`: "another State or Territory" is read as other than the
  one where the court sits, so a South Australian statutory claim heard in Victoria takes South Australian written and
  unwritten law.
- **F10** s 5(1) and s 6A(4): s 6A(4) is asked only once s 5(1) would otherwise bite; it lifts the duty, and the answer
  says the court still may transfer.
- **F11** s 8(1)(a)(ii), "a tribunal established by or under an Act": "Act" is asked as a fact (read with the Acts
  Interpretation Act 1915 it would mean a South Australian Act).

## What the Act turns out to say (findings)

1. **s 4 now begins at (3).** Subsections (1) and (2), which vested State jurisdiction in the Federal Court and the
   Family Court, were deleted in 2001 (Statutes Amendment (Federal Courts--State Jurisdiction) Act 2000). The Act still
   transfers proceedings to those courts (s 5(1), s 6) and receives them (s 5(4), s 6A(2)), so what they can do with a
   South Australian matter now depends on federal law (their accrued jurisdiction), which this Act does not supply
   (s 5(9)). Asserted (F1).
2. **s 5(1)(b)'s numbering is what deletion left.** s 5(1)(b) reads "(b) --" followed by "(ii)" alone (its
   (i) and (iii) were deleted in 2001), so the only ground left for sending a proceeding to a federal court is the
   factor test in (ii); s 5(2), (3) and (4) keep three grounds each. Asserted.
3. **s 10 points at repealed law.** It speaks of Divisions 1 and 1A of Part V of the Trade Practices Act 1974 (Cth)
   ("Part V" in the heading, "Part 5" in the text). s 3(3) reads Commonwealth Acts as amended; to the encoder's
   knowledge (not from a deposited source) that Act was renamed the Competition and Consumer Act 2010 and those Divisions
   were replaced by the Australian Consumer Law in 2011, so s 10 may now have nothing to apply to. Encoded as written,
   with the matter asked as a fact.
4. **"The Family Court" is stale.** To the encoder's knowledge (not from a deposited source) the Family Court of
   Australia became Division 1 of the Federal Circuit and Family Court of Australia in 2021; the Act's references were
   not updated (its own note says such references are not updated automatically). Encoded as written.
5. **s 7(4)'s exception for s 7(5) cannot operate.** s 7(4) is about appeals from a single judge of the Supreme Court of
   South Australia, and excepts "a proceeding to which subsection (5) applies"; s 7(5) is about appeals from a judge of
   a State Family Court, and South Australia has none (only Western Australia). s 3(2) reads a "Supreme Court of a
   State" as including its State Family Court, but s 7(3)-(4) say "the Supreme Court" (of South Australia). Encoded
   with s 7(5) reached only from a State Family Court (F6).
6. **"Territory" means an external territory.** s 3(1) puts the Northern Territory and the ACT inside "State" and
   outside "Territory", so "the Supreme Court of a Territory" in ss 4, 5 and 10 is an external territory's (in practice
   Norfolk Island's); s 6(2)(b) names the Supreme Court of the Northern Territory separately because it is a "State"
   court there. The court choices say so.
7. **No time limits.** Nothing in the Act runs against the party: no period to apply for a transfer, no period for the
   s 6(4) notice (only "a reasonable time" for the Attorneys-General), no limitation period. Limitation is left to the
   law the court applies under s 11(1).
8. **s 6(4) notice goes to "the Attorney-General of the State"**, that is South Australia's (and the Commonwealth's); not
   to other States' Attorneys-General even if their law is involved.

## Before relying on it

Check the register for a version later than 4 September 2006 and for a proclamation under s 15; deposit the
Commonwealth Act (its "special federal matter" definition and Schedule) and encode the borrowed terms from it; have a
lawyer review the forks and findings 3 to 5; run an independent test pass.
