# Jurisdiction of Courts (Cross-vesting) Act 1987 (Qld): baseline encoding for the party to a civil proceeding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is cross-vesting: which court may hear a civil claim that touches Queensland and another Australian jurisdiction, when it must or may be moved, what follows a move, and where an appeal goes. The Act is short, so the whole of its operative text is encoded (scope below).

It is written in layers:

- **`jcxv-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the Supreme Court", "the first court", "the other court", "State matter", "special federal matter"). Each rule is preceded by the words of the section it encodes. One regulative rule (`DEONTIC`): the s 6(5)(b) notice a party is directed to give to the Attorneys-General, within the days the court allows. Two small date helpers on the stable prelude (`DATE_SERIAL`, `DATE_FROM_SERIAL`); `daydate` is not imported and no `YMD` is defined.
- **`jcxv-seat.l4`**, the party's seat: 27 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a proceeding runs; groups that arise only in a situation (a special federal matter, an appeal) say so in the heading. It builds the core's inputs from plain answers and restates no rule. Inputs with the same meaning carry the same name in every question.
- **`jcxv-cases-party.l4`**, the cases.

No earlier encoding of this Act exists. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Jurisdiction of Courts (Cross-vesting) Act 1987** (Qld) (act-1987-088), the version in force from 2011-01-01, current on 6 November 2026, as deposited at `../../registers/source-bundle/act-1987-088.txt` (retrieved 2026-11-06, unofficial conversion of the HTML view).

Not deposited, and so asked as facts: the Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987 (the definition of "special federal matter" and its paragraphs; the Schedule of Acts in s 7), the Administrative Decisions (Judicial Review) Act 1977 (Cth) (paragraphs (ca), (cb) of "enactment", for s 6A), the Australian Consumer Law provisions s 10 lists, the Corporations Act part 9.6A division 1 (s 3A), and the Family Law Act 1975 (Cth) s 41 proclamations (State Family Court).

## Checks

| Module | Run | Result |
|---|---|---|
| `jcxv-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `jcxv-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `jcxv-cases-party.l4` | `l4 run` | 0 errors, 0 warnings; **110 assertions written, 110 satisfied** |

In addition, 2 `#TRACE`s of the s 6(5)(b) rule carry an `-- expect:` line (notice on the last day: FULFILLED; nothing by the day after: BREACH by the directed party); both were read and match.
`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07, and again after the fix of 2026-11-07 below). Every expected value was written by hand from the text.

## Seat

**The party to a civil proceeding**: the individual who brings or answers a claim (plaintiff, applicant, defendant, respondent), or a person who intervenes (s 3(1) "party ... includes a person who intervenes"), whose proceeding touches Queensland and another Australian jurisdiction. They ask:

- "Does the Act reach my proceeding? Is my claim a State matter? Can another State's Supreme Court hear it?"
- "Must my proceeding be moved, may it be, and to which court? Can I ask for that? Does my related proceeding follow? Can my lawyer act for me there?"
- "My proceeding raises a special federal matter: must it go to the Federal Court or the Family Court? Can the Supreme Court keep it? By when must I give the notice I was directed to give?"
- "Where must my appeal go? Can I appeal from the Federal Court to the Court of Appeal?"
- "Can my case be removed from the Magistrates Court, District Court or a tribunal into the Supreme Court, and sent back? Can my consumer law claim go down to a lower court?"
- "Which law will the court apply? Do the earlier steps count? Who orders the earlier costs? Can I appeal the transfer? Can I enforce the judgment?"

There is **no second seat**: the Act puts no duty on a private party other than one a court directs (s 6(5)(b)), which is in the first seat. The courts and the Attorneys-General are not seats; their powers and duties appear only as what they mean for the party.

The 2026-10-18 defaults:

- **The Act alone.** It has no regulations setting numbers. The Commonwealth Act's definition of "special federal matter" and its Schedule are borrowed terms (below), asked as facts.
- **The actors the text names:** the Supreme Court (of Queensland), the Supreme Court of another State or of a Territory, the State Family Court, the Federal Court, the Family Court, the first court, the transferee court, a party, the Attorneys-General.
- **Judgments left to others are answered conditionally, as inputs:** every "it appears to the court", "in the opinion of", "more appropriate", "the interests of justice", "special reasons", "a reasonable time", "considers it appropriate", and the days a court's direction allows.
- **The Act's own definitions are worked out from facts:** proceeding (not criminal), party (includes an intervener), State matter (s 3(1)), the application of s 6A (s 6A(1)), Full Court. Borrowed terms are asked as facts: special federal matter (and which paragraph), the Commonwealth Schedule, the ADJR enactment paragraphs, the listed Australian Consumer Law provisions, Corporations Act part 9.6A division 1, State Family Court.
- **One case:** one proceeding (with any related proceeding as a fact about it).
- **The Act's own terms**, quoted in the comment above each rule; plain glosses in the `@desc`s ("Court of Appeal" for the Full Court of the Supreme Court).
- **Machinery out** (below).

## Scope

**In:** s 3 (the definitions the operative sections use), s 3A, s 4, s 5(1)-(4), (6)-(8), s 6(1)-(9) (s 6(9) including a pre-1993 s 6(1) order), s 6A(1)-(3), s 7(1)-(7), s 8(1), (3), s 9, s 10, s 11(1), (3), s 12, s 13, s 14(1).

**Out, and why:**

- ss 1-2 (short title, commencement), s 16 (suspension or cessation by proclamation), s 17 (saving for proceedings pending in 1993): machinery and transitional.
- s 5(9), s 6A(4) ("nothing ... confers on a court jurisdiction that the court would not otherwise have") and s 6A(5) (the meaning of "interests of justice" elsewhere): interpretive limits with no fact for the party to state; noted in the core's comments.
- s 6A(6) (Commonwealth authority, officer of the Commonwealth): folded into the s 6A(1)(b) fact.
- s 6(5)(a) (adjournment and its costs) and s 6(6) (what the court must consider for special reasons): what the court weighs, taken within the "special reasons" input.
- s 8(2) ("this Act applies ... as if it were a proceeding pending in the Supreme Court"): reflected by asking s 5 and s 6 questions of a removed proceeding as a Supreme Court proceeding, and by State matter (b).
- s 11(1)(c) (rules of evidence and procedure as the court considers appropriate): stated in the question's text; nothing to compute.
- s 14(2) (a State law's reference to a thing done by the Supreme Court read as a reference to the other court): interpretive, with no fact a party could state usefully.
- The preamble: not operative.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

Answers say no only where the text does: "does not include" (s 3(1) proceeding), "does not apply" (s 3A, s 6(9)), "does not invest ... or confer" (s 4(3)), "shall not be instituted" (s 7(1), (2)), "does not lie" (s 13), "if"/"where" conditions (ss 5, 6(3)-(4), 6A(1), 7(6), 8, 10, 11(3), 12). Where the text is silent or its list is open, the answer is `NOTHING` (or an enumerated "the Act does not deal with ..." answer).

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 4, `the court has jurisdiction in the State matter under s 4`: a matter that is not a State matter, or a court s 4 does not name, answers NOTHING (scope limit, no "only"); the other reading is no.
2. s 5(7), `may apply for a transfer (s 5(7))`: someone other than a party or intervener answers NOTHING (the list is not closed with "only"); the other reading is no.
3. s 5(8), `the lawyer may practise in the other court (s 5(8))`: a lawyer not entitled in the first court, or a related proceeding not to be decided together, answers NOTHING (limit in the grant's own wording); not transferred answers no (the "if" fails).
4. s 6(7), `s 6 does not stop urgent interlocutory relief (s 6(7))`: when the interests of justice do not call for relief, NOTHING (the "nothing prevents ... if" form says nothing when unmet); the other reading is no.
5. ss 6(8), 7(7), `s 6 invalidates the decision`, `s 7 invalidates the decision`: outside inadvertence (or the s 7(6) route), NOTHING; the other reading is that the decision is open to attack (a yes), which the text does not say.
6. s 7(1), `an appeal may be instituted from the federal court (s 7(1), (2))`: an appeal from a Full Court of the Federal Court or Family Court to the Court of Appeal answers NOTHING; the other reading is no, by analogy with s 7(1).
7. s 11(3), `the earlier step counts in the transferee court (s 11(3))`: an order of the transferee court about the step answers no ("subject to any order" read as displacing the step); the other reading is NOTHING (the order's terms decide).
8. s 13, `an appeal lies from the decision (s 13)`: any other decision answers NOTHING.

## What the Act turns out to say (findings)

1. **s 5(1) has no "otherwise in the interests of justice" limb.** s 5(2), (3) and (4) each add a free-standing paragraph (iii) ("it is otherwise in the interests of justice"); s 5(1) (Supreme Court to the Federal Court or Family Court) makes the interests of justice only one factor in "more appropriate". A finding of the interests of justice alone requires a move between Supreme Courts, or from a federal court to the Supreme Court, but not from the Supreme Court to a federal court. Asserted.
2. **s 5(2)(b)(i) needs the related proceeding to be pending** in the other Supreme Court; a court finding "more appropriate" without one must rely on (ii) or (iii). Asserted.
3. **A State Act directing federal courts (READING).** s 5(4), s 6A(2) and s 7(4), (6) speak of what the Federal Court, the Family Court and their Full Courts "shall" do. A Queensland Act cannot by itself bind a federal court; the matching provisions of the Commonwealth Act are taken to do the work. Encoded as written, from the party's side ("must my proceeding be transferred").
4. **"Family Court" is still "the Family Court of Australia"** (s 3(1)). The deposited version has been in force since 2011-01-01 and was not amended for later changes to the federal courts' structure; whether and how its references carry over is a question of Commonwealth law, outside the deposited sources. The encoding keeps the Act's names.
5. **"Territory" excludes the NT and the ACT** (s 3(1)), and "State" includes them. "The Supreme Court of another State or of a Territory" therefore covers the NT and ACT Supreme Courts as "States", and "a Territory" means another (external) Territory. The `@desc`s say so.
6. **State Family Court.** s 3(2), s 4(2) and s 7(5) speak of a State Family Court, a court to which Family Law Act 1975 (Cth) s 41 applies by proclamation. Whether Queensland has one is outside the deposited sources; s 7(5) is asked as a fact. s 3(2) makes every reference to "the Supreme Court of a State" other than in s 4(1) include that State's State Family Court, so the State Family Court of another State (in practice the Family Court of Western Australia) is treated as "the Supreme Court of another State" in s 5(2), (3) (transfers both ways with the Supreme Court of Queensland), s 8(1)(b)(i) (the related proceeding) and s 10(a) (consumer law transfers down). Asserted. A Queensland State Family Court, if there were one, would likewise be within "the Supreme Court"; the court list has no value for it.
7. **Missing subsections.** The deposited text has no s 5(5) and no s 11(2), with no "[Repealed]" marker (amendment-history notes were removed in conversion). Taken as repealed; nothing is encoded for them.
8. **s 6(5)(b) fixes no time.** The court "may direct a party to ... give a notice"; the days come from the direction. The rule takes them as an input and treats the last day as the day the direction was given plus those days. Asserted (14 days from 3 March 2026 ends 17 March 2026; a notice on 18 March is late).
9. **s 6(1A) transfers only part.** The Supreme Court must transfer "only ... so much of the proceeding as is ... within the jurisdiction" of the federal court; the answers say "the part within ...". The rest stays in the Supreme Court, which the Act does not say more about.
10. **s 13 says "under this act".** The bar on appeals covers a transfer or removal under the Queensland Act; a transfer under the Commonwealth Act or another State's Act is outside its words (their own provisions may bar an appeal). Answered NOTHING for "some other decision" (fork line 8).
11. **s 11(1)(b) reads "another State or Territory" from where the court sits (READING)**, not from Queensland: a Queensland Supreme Court hearing a right of action under a NSW statute applies NSW written and unwritten law. Asserted.

## Fix of 2026-11-07 (after independent verification)

- s 3(2) was applied only to s 4. It now also reaches s 5(2), (3), s 8(1)(b)(i) and s 10(a) (finding 6); 5 assertions added.
- s 6(9) also covers an order under s 6(1) as in force before the 1993 amendment Act; the input and its `@desc` now say so; 1 assertion added.
- Not changed: s 5(8) "not transferred" still answers no (fork line 3). The convention used here counts an unmet "if" as the text saying no, as for ss 5, 6(3)-(4), 8, 10, 11(3) and 12; the fork line is there for a reviewer to overrule.

## Before relying on it

- Deposit the Commonwealth Jurisdiction of Courts (Cross-vesting) Act 1987 and encode its definition of "special federal matter" and its Schedule, so they can be worked out from facts instead of asked.
- Check the current names and structure of the federal courts against finding 4.
- Have a lawyer check readings 3 and 11 and the fork lines.
- An independent test pass, and the human gates.
