# Jurisdiction of Courts (Cross-vesting) Act 1993 (ACT) — baseline encoding, the party's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (one regulative rule, for the only duty the Act can put on a party).
There is no REFUSE in it; a question that reaches a court or a pair of courts the Act does not speak to answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind compensation and other civil claims. This Act is the ACT's part of the national cross-vesting scheme: it decides which other courts can hear an ACT civil claim and when a claim must move between the ACT Supreme Court and the federal and other State courts. It is short, so it is encoded whole, bar machinery. There was no earlier encoding of this Act to keep. No ledger entry was open for it (the ACT has no requirement ledger). Its Commonwealth counterpart, the Jurisdiction of Courts (Cross-vesting) Act 1987, has its own baseline at `subjects/au/jurisdiction-of-courts-cross-vesting-act-1987/encodings/baseline-2026-11/`; nothing is imported from it (the stable `l4` cannot import across subjects), and the two were written to ask the same kind of questions in the same order.

There are 19 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: can this court hear my ACT matter (s 4, with s 9); must my proceeding be transferred, must a related one follow, can I apply, can my lawyer keep acting (s 5); special federal matters, the notice to the Attorneys-General, adjournment costs, urgent interim relief, decisions not invalidated (s 6, with s 7(7)); s 6A; where must I appeal and what happens to an appeal begun in the wrong Full Court (s 7); removal from a lower ACT court or an ACT tribunal (s 8); sending an Australian Consumer Law claim to a lower ACT court (s 10); which law applies (s 11); what carries over after transfer (ss 11(3), 12); no appeal from a transfer decision (s 13); enforcement in the ACT (s 14). Headings whose questions arise only in a situation the person may not be in (wanting to appeal, having been transferred, holding a judgment, a case in a lower ACT court or tribunal, the Supreme Court being asked to keep a special federal matter) say so.

**Regulative rule.** `s 6(5)(b) -- I must give the notice the court directed`: `PARTY I, the party the court directed MUST give written notice of the nature of the special federal matter to the Attorney-General of the Commonwealth and the Attorney-General of the ACT WITHIN <the time the court allowed> HENCE PARTY the ACT Supreme Court MAY order that the proceeding be determined by the ACT Supreme Court LEST BREACH ... BECAUSE`. The Act sets no time; the court's direction does, so it is an input in days. The seat question `Must I notify the Attorneys-General question` takes plain facts (a special federal matter; a direction given). The case file asserts the rule kept on the last day (notice on day 14 of 14, then the order) and early (day 1) through `CONSIDER EVALTRACE ... WHEN FULFILLED`, asserts that notice on day 15 is not fulfilled, and `#TRACE`s that breach with an `-- expect:` line. Every other "must transfer" in the Act is a duty on a court, and is written as a decision of what the party can expect.

## Edition

Republication No 4 (R4), effective 21 March 2025, last amendment made by the Justice and Community Safety Legislation Amendment Act 2025 (No 2) (A2025-3), retrieved from the ACT Legislation Register on 6 November 2026, as deposited at `../../registers/source-bundle/A1993-60.txt` (converted from the register's DOCX, which the register marks as an unauthorised version). No instrument sets a number or date this Act uses; nothing else is brought in.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `jccv-party.l4` | `jccv-cases-party.l4` | 115 written, 115 satisfied; 1 trace, as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. Edge cases: the last day of the notice period and the day after; each ground of s 5 alone and none; s 5(5)'s missing "having regard to" ground; each of the four s 6A(1) conditions failing alone; each s 10 condition failing alone; every special federal matter paragraph; each court in the `Court` list against s 4.

## Seat

**The party to a civil proceeding**: usually the claimant who brings it (an injured worker, a person hurt in an accident, a consumer, a business), sometimes the defendant who answers it; an intervener counts (dictionary: "party, in relation to a proceeding, includes a person who intervenes in the proceeding"). "My claim is in the ACT Supreme Court. Must it go to the Federal Court? Can it be moved to New South Wales, where the other case is? Where do I appeal? Can I appeal the transfer? Which law applies?"

The Act's operative provisions are addressed to courts. They are encoded as what they mean for the party. No question is asked from the seat of a court or an Attorney-General. A defendant's questions are the same questions, so no second seat is written.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Commonwealth cross-vesting Act and its Schedule, the Competition and Consumer Act 2010, the ADJR Act, the Judiciary Act 1903, the Family Law Act 1975) are named, not encoded; whether a matter arises under one is asked as a fact.
- **The actors the text names:** the party, the courts by name, the Attorneys-General.
- **Judgments handed to others are answered conditionally:** every "it appears to the Supreme Court", "more appropriate", "interests of justice", "special reasons", "considers it appropriate" and "in the opinion of the court" is an input. Whether the ACT Supreme Court has jurisdiction "otherwise than by reason of a law of the Commonwealth or of another State" is asked as a fact about the other laws.
- **The Act's own definitions are worked out from facts:** "ACT matter" (both paragraphs), "State", "Territory", "State Family Court" and the s 3 reading-in of the State Family Court; "proceeding" (no criminal proceeding); "party". **Borrowed terms are asked:** "special federal matter" is a signpost to the Commonwealth Act, so the person states which paragraph of that definition the matter falls under; "officer of the Commonwealth" (Constitution s 75(v)); the Commonwealth Act's Schedule; "Commonwealth authority" (s 6A(8)) is folded into a factual input.
- **One case:** one proceeding (or, for s 5(6), the proceeding and one related to it).
- **The Act's own terms**, quoted in the comment above each rule, and glossed in the `@desc` lines. "Family Court" keeps the Act's name (finding 1).
- **Machinery out:** ss 1, 2, 15, 16, 17.

## Scope

**In:** s 3; s 4(1)–(5); s 5(1)–(8); s 6(1)–(8); s 6A(1)–(5) and the s 6A(8) definitions (as inputs); s 7(1)–(7); s 8(1)–(3); s 9 (in the s 4 answer for the ACT Supreme Court); s 10; s 11(1)–(3); s 12; s 13; s 14(1), (2); the dictionary definitions used.

**Out, and why:** ss 1, 2 (name; the dictionary is part of the Act); s 6A(6) (no new jurisdiction: changes no answer here); s 6A(7) (how "interests of justice" is read elsewhere: the court's opinion is the input); s 14(3) (references to the Supreme Court in other ACT laws: construction, not a party's question); s 15 (suspension by Executive declaration), s 16 (cessation), s 17 (cessation and reapplication in relation to another jurisdiction): machinery, and no declaration is in the deposit, so the encoding assumes the Act is in force in relation to every jurisdiction. The preamble is quoted in nothing.

## Fork register (questions with no convention, decided case by case)

The Act's answers are rarely a bare yes or no, so every question answers with an enumeration whose wording carries the reach of the "no". The 2026-11-04 and 2026-11-05 rulings in `docs/ENCODING-GUIDE.md` §5 were followed in choosing between "no" and `not covered`:

- s 4 for a court s 4 does not name (an ACT or other lower court or tribunal): `not covered` (a scope limit with no "only"). The other reading: "no".
- s 4 for the ACT Supreme Court: answered with what s 9 says rather than `not covered`, since an ACT matter is by definition within its jurisdiction. The other reading: `not covered`.
- s 4 for a matter that is not an ACT matter: "no", worded "section 4 of this Act gives the court nothing" (s 4 is limited to ACT matters in its own words). The other reading: `not covered`, since the Commonwealth's or another State's Act may give the jurisdiction; the wording says so.
- s 4 for a criminal matter: "no" (s 4(5), a flat negative).
- s 5 for a pair of courts no subsection joins (another State's Supreme Court and a federal court; two other States' courts): `not covered`. The other reading: "no".
- s 5(7) for a non-party: `not covered` (a grant limited in its own words). The other reading: "no".
- s 6 for a proceeding not in the ACT Supreme Court: "no" (an "if" condition, rule (b) of 2026-11-05).
- s 6(8) when the Supreme Court acted deliberately, not through inadvertence: answered "section 6(8) does not save it", never "invalid". The other reading: `not covered`.
- s 7 for a decision of a court s 7 does not name, and for a Family Court of Western Australia appeal without both kinds of matter: `not covered`.
- s 8 for a criminal proceeding: "no" (the definition of "proceeding" excludes it).
- s 14 for another State's judgment, or one not given in cross-vested jurisdiction: `not covered`.

## What the Act turns out to say

1. **"Family Court means the Family Court of Australia."** That court has been called the Federal Circuit and Family Court of Australia (Division 1) since 1 September 2021. The dictionary was not updated, though the Act was amended in March 2025 (A2025-3). Whether the old name reads as the new court depends on Commonwealth transitional law, which was not read. The encoding keeps the Act's name and glosses it with the new one.
2. **Section 7(5) cannot apply to any appeal that s 7(4) governs.** Section 7(4) covers an appeal "from a decision of a single judge of the Supreme Court (not being a proceeding to which subsection (5) applies)", and in this Act "the Supreme Court" is the ACT Supreme Court. Section 7(5) covers an appeal "from a decision of a judge of a State Family Court", which is the Family Court of Western Australia. The s 3 reading-in applies to "the Supreme Court of a State", not to "the Supreme Court". So the carve-out in s 7(4) never bites. It is copied from the Commonwealth s 7, where both subsections speak of the Supreme Court of a State. An ACT appeal with a Schedule matter and another matter goes under s 7(4). Asserted.
3. **Special federal matters under paragraph (aa) have no receiving court.** Section 6(1) requires a transfer "to the Federal Court or a court mentioned in subsection (2) (b)". Section 6(2) sends paragraphs (a), (b), (c) and (e) to the Federal Court and paragraph (ab) to the family courts, and says nothing of (aa) (Competition Code matters of the ACT or the NT). This is the same gap as in the Commonwealth s 6(2). Asserted as "yes, but the text names no receiving court".
4. **The ACT s 6 is shorter than the Commonwealth's.** It has no counterpart to the Commonwealth's s 6(1A) (transfer only so much of the proceeding as is within the receiving court's jurisdiction), s 6(7) (the Commonwealth may pay a party's adjournment costs) or s 6(10) (no s 6 transfer of an appeal where the court below made a s 6(3) order). On the ACT text, the whole proceeding goes. Asserted.
5. **Section 10's heading is out of date.** It still refers to "the Competition and Consumer Act, pt 5, div 1 or div 1A" (the old consumer protection provisions), while the body, amended in 2010, refers to schedule 2, parts 2-2, 3-1, 3-3 and 3-4 (the Australian Consumer Law). The body governs. Paragraph (b) also lacks the "and" that ends paragraphs (a), (c) and (d). This changes nothing.
6. **In this Act the ACT is a "State", and "Territory" means an external Territory.** So "the Supreme Court of another State or of a Territory" (ss 4(3), 5(2), (3), 8, 10) is the NT Supreme Court, the six States' Supreme Courts (with the Family Court of Western Australia, s 3) and the Supreme Courts of Norfolk Island, Christmas Island and the Cocos (Keeling) Islands. The definition of "Full Court" ("in relation to a Supreme Court of a State, includes a court of the State to which appeals lie from a single judge of that Supreme Court") therefore reaches the ACT Court of Appeal for s 7. Encoded on that reading.
7. **Section 8 reaches the ACT's own lower courts and tribunals.** Unlike the Commonwealth s 8, which covers external Territories, the ACT s 8 lets the ACT Supreme Court remove a case from the Magistrates Court or an ACT tribunal (for example ACAT) to consider transferring it. Removal is a discretion and is not appealable (s 13(a)). Asserted.
8. **Section 6A(4)(b) repeats s 6A(1)(c).** Section 6A applies only where the related ACT matter proceeding is "pending in any ACT court", and s 6A(4)(b) asks for the same thing again. The encoding asks it once.
9. **The grounds for a mandatory transfer turn wholly on what appears to the court.** None of the s 5 grounds is a fact a party can prove; each is the court's view. The encoding asks each as an input. The party's lever is the application that s 5(7) gives it, and an Attorney-General has the same.
10. **The text does not show its constitutional limits.** In *Re Wakim* (1999) the High Court held that the States cannot confer State jurisdiction on the federal courts. Whether, and how far, that touches the ACT's s 4(1), (2) and s 5(4), (5) was not examined, and no case law was read. The encoding answers on the text.

## Raised in the ledger

Nothing. The ACT keeps no requirement ledger, and no scenario life cites this Act.

## What would need doing before this is worth relying on

- **The Commonwealth and State cross-vesting Acts**, which run in parallel. The Commonwealth Act has its own baseline; the State Acts are not deposited. Read with them, *Re Wakim* and the later case law on "interests of justice" (for example *BHP Billiton Ltd v Schultz* (2004)).
- **Commonwealth transitional law** on references to the Family Court of Australia (finding 1).
- **The courts' own Acts** for where an appeal lies when s 7 says only where it does not.
- An independent test pass and a human review.
