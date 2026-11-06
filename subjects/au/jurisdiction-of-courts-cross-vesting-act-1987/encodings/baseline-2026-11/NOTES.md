# Jurisdiction of Courts (Cross-vesting) Act 1987 — baseline encoding, the party's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (one regulative rule, for the only duty the Act can put on a party).
There is no REFUSE in it; a question that reaches a court or a pair of courts the Act does not speak to answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind compensation and other civil claims. This Act decides which court hears a claim and where it goes when it is in the wrong one, so it is encoded whole (bar machinery). There was no earlier encoding of this Act to keep. No ledger entry was open for it.

There are 19 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: which court can hear my matter (s 4); must my proceeding be transferred, must a related one follow, can I apply, can my lawyer keep acting (s 5); special federal matters, the notice to the Attorneys-General, adjournment costs, urgent interim relief, decisions not invalidated (s 6, with ss 6(9) and 7(8)); s 6A; where must I appeal and what happens in the wrong Full Court (s 7); removal in an external Territory (s 8); sending an Australian Consumer Law claim to a lower court (s 10); which law applies (s 11); what carries over after transfer (ss 11(3), 12); no appeal from a transfer decision (s 13); enforcement (s 14). Headings whose questions arise only in a situation the person may not be in (wanting to appeal, having been transferred, holding a judgment, a case in an external Territory, the Supreme Court being asked to keep a special federal matter) say so.

**Regulative rule.** `s 6(5)(b) -- I must give the notice the court directed`: `PARTY I, the party the court directed MUST give written notice ... to the Attorney-General of the Commonwealth and the Attorney-General of the State or Territory WITHIN <the time the court allowed> HENCE PARTY the Supreme Court MAY order that the proceeding be determined by the Supreme Court LEST BREACH ... BECAUSE`. The Act sets no time; the court's direction does, so it is an input in days. The seat question `Must I notify the Attorneys-General question` takes plain facts (a special federal matter; a direction given). The case file asserts the rule kept on the last day (notice on day 14 of 14, then the order) through `CONSIDER EVALTRACE ... WHEN FULFILLED`, asserts that notice on day 15 is not fulfilled, and `#TRACE`s that breach with an `-- expect:` line. Every other "shall transfer" or "must transfer" in the Act is a duty on a court, and is written as a decision of what the party can expect.

## Edition

Compilation No. 23, compilation date 6 February 2023, including amendments up to Act No. 79, 2022 (the Fair Work Legislation Amendment (Secure Jobs, Better Pay) Act 2022), registered as **C2023C00038**, retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A03433.txt`. No instrument sets a number or date this Act uses; nothing else is brought in.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `jcca-party.l4` | `jcca-cases-party.l4` | 108 written, 108 satisfied; 1 trace, as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The party to a civil proceeding**: usually the claimant who brings it (an injured worker, a road accident victim, a consumer, a business), sometimes the defendant who answers it; an intervener counts (s 3(1): "party ... includes a person who intervenes"). "I have filed in the Supreme Court. Can it hear the federal part of my claim? Must my case go to the Federal Court? Where do I appeal? Can I appeal the transfer? Which State's law applies?"

The Act's operative provisions are addressed to courts. They are encoded as what they mean for the party. No question is asked from the seat of a court or an Attorney-General. A defendant's questions are the same questions, so no second seat is written.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Competition and Consumer Act 2010, the Fair Work Act 2009, the ADJR Act, the Judiciary Act 1903, the Family Law Act 1975, the Acts in the Schedule) are named, not encoded; whether a matter arises under one is asked as a fact. The State and Territory cross-vesting Acts (which give the federal courts State jurisdiction) are a different law and are not encoded.
- **The actors the text names:** the party, the courts by name, the Attorneys-General.
- **Judgments handed to others are answered conditionally:** every "it appears to the first court", "more appropriate", "interests of justice", "special reasons", "considers it appropriate" and "in the opinion of the court" is an input. Whether a court has jurisdiction "apart from this Act" is also asked, as a fact about the other laws.
- **The Act's own definitions are worked out from facts:** "special federal matter" (s 3(1), every paragraph and the closing words); "State", "Territory" and "Full Court" (s 3(1), the last for s 7); the State Family Court rule of s 3(2). "Commonwealth authority" (s 6A(6)) is folded into a factual input; "officer of the Commonwealth" (borrowed from s 75(v) of the Constitution) is asked.
- **One case:** one proceeding (or, for s 5(6), the proceeding and one related to it).
- **The Act's own terms**, quoted in the comment above each rule, and glossed in the `@desc` lines.
- **Machinery out:** ss 1, 2, 15, 16.

## Scope

**In:** s 3(1) (the definitions used, among them "special federal matter", "State", "Territory", "State Family Court" and "Full Court"), s 3(2); s 4(1)–(4); s 5(1)–(9); s 6(1)–(5), (7)–(10); s 6A(1)–(3); s 7(1)–(8) and the Schedule; s 8(1)–(3); s 10; s 11(1)–(3); s 12; s 13; s 14(1), (2).

**Out, and why:** ss 1, 2 (title, commencement); s 3(3) (extension to external Territories: assumed); s 3(4) (ACT and NT application laws of the Competition Code treated as federal jurisdiction: a rule for the courts that changes no answer here); s 6(6) (what the court weighs on "special reasons": its opinion is the input); s 6A(4), (5) (no new jurisdiction; how "interests of justice" is read); s 6A(6) (its two definitions are not encoded as rules but folded into the inputs, as said above); s 9 (the courts' capacity to exercise cross-vested jurisdiction, and s 9(1) saving State laws); s 14(3) (references in other laws); s 15 (reading down); s 16 (suspension or cessation by Proclamation; none is in the deposit). The preamble is quoted in nothing.

## Fork register (questions with no convention, decided case by case)

The Act's answers are rarely a bare yes or no, so every question answers with an enumeration whose wording carries the reach of the "no". The 2026-11-04 and 2026-11-05 rulings were followed in choosing between "no" and `not covered`:

- s 4 for a court s 4 does not name (a district, county or magistrates court): `not covered` (a scope limit with no "only"). The other reading: "no".
- s 4 where the court already has jurisdiction apart from s 4: answered "yes, without this Act" before the criminal and s 4(4) tests, because s 4(1)(b), (2)(b) make s 4 irrelevant then. The other reading: the s 4(4) "no" first.
- s 4 for a criminal proceeding: "no" ("proceeding does not include a criminal proceeding", a flat negative in a "means"-type definition, and s 4's "civil matter" in a "where" clause).
- s 5 for a pair of courts no subsection joins: `not covered`. The other reading: "no" (s 5(9) says the section confers no jurisdiction).
- s 5(7) for a non-party: `not covered` (a grant limited in its own words). The other reading: "no".
- s 7 for a magistrates court decision with no appeal to the State Family Court, and for any other court: `not covered`.
- s 14 for a State Supreme Court judgment: `not covered` (s 14 speaks only of the federal courts and the Territory Supreme Courts).

## What the Act turns out to say

1. **Fair Work claims cannot ride on cross-vesting.** s 4 "does not apply to a matter arising under" the Fair Work Act 2009, its two companion Acts, the Workplace Relations Act 1996, the Conciliation and Arbitration Act 1904, the Federal Safety Commissioner Act 2022, the Native Title Act 1993 and some competition provisions (s 4(4)). A worker who sues in a State Supreme Court for negligence cannot add a Fair Work claim there under this Act. Asserted.
2. **Special federal matters under paragraph (aa) have no receiving court.** s 6(1) requires a transfer "to the Federal Court or a court mentioned in paragraph (2)(b)", but s 6(2) sends paragraphs (a), (b), (c) and (e) to the Federal Court and (ab) to the family courts, and says nothing of (aa) (Competition Code matters of the ACT or the NT, added in 1995). The Federal Court is the likely intent; the text does not say so. Asserted as "yes, but the text names no receiving court". Also: the definition has no paragraph (d).
3. **"Territory" means an external Territory.** s 3(1) puts the ACT and the NT among the "States" and takes them out of "Territory". So s 8 (removal from a lower court or tribunal) and s 14 (enforcement "in a Territory") reach only Norfolk Island, Christmas Island and the Cocos (Keeling) Islands, while s 4(1)(d) names the ACT and NT Supreme Courts expressly. Asserted for s 8.
4. **The Family Court of Western Australia is a "Supreme Court of a State"** everywhere except ss 4(1), 5(3) and 7(4) (s 3(2)). It can therefore receive a transfer from a federal court under s 5(4), transfer to a federal court under s 5(1), get s 4(2) jurisdiction, and its judges' decisions are appealed under s 7(3) and (5), with s 7(6) letting a mixed appeal stay in the State system. Asserted.
5. **The "shall transfer" duties turn wholly on what appears to the court.** None of the grounds in s 5 is a fact a party can prove; each is the court's view. The encoding asks each as an input; the party's practical lever is the application s 5(7) gives it (and which the Attorneys-General also have).
6. **No appeal from a transfer decision** (s 13(a)), nor from the choice of evidence and procedure rules (s 13(b)). Asserted.
7. **The s 6(4) notice is no one's duty until the court directs it.** The court must be satisfied the notice was given before it keeps a special federal matter, but the Act does not say who gives it or by when; s 6(5)(b) lets the court direct a party. Encoded with the court's time as an input.
8. **A right of action under another State's written law carries that State's whole law with it** (s 11(1)(b)), including its unwritten law, while otherwise the court applies the law of where it sits, including choice of law rules (s 11(1)(a)). For a statutory compensation claim heard in another State, that is the claim's own State's Act. Asserted.
9. **The Schedule still names the Trade Marks Act 1955**, repealed and replaced (by the Trade Marks Act 1995); the Schedule's last amendment was in 2008. A matter under the 1995 Act does not appear to be a Schedule Act matter on the text. Not asserted beyond the Schedule's count of thirteen.
10. **Endnote 4 records s 10 as "am No 222, 1922".** Endnote 3 lists the Trade Practices Legislation Amendment Act 1992 as No. 222, 1992; "1922" is a typographical slip in the endnotes. It changes nothing operative.

## Raised in the ledger

Nothing. No ledger entry named this Act, and no scenario life cites it.

## What would need doing before this is worth relying on

- **The State and Territory cross-vesting Acts**, which give the Federal Court State jurisdiction and run in parallel (s 9(1)); after *Re Wakim* (1999) their grant to the federal courts is limited, which this Act's text does not show. No case law was read.
- **The courts' own Acts** for where an appeal lies when s 7 says only where it does not.
- **Wider sources.** No court rules, practice notes or decisions on "interests of justice" were read.
- An independent test pass and a human review.
