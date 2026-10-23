# Evidence Act 1995 — baseline encoding, the accused's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the two cases outside the encoding (a trial in a State or Territory court, and comment on silence at a summary trial) answer `not covered`, and tests assert both.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0084` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

Every question is a function named as the accused would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 23 exported questions, grouped under `§§` headings whose wording says the situation ("if you have been charged", "if the prosecution relies on something I said", "if I was not cautioned").

## Edition

The compilation registered as **C2025C00340** (Compilation No. 35, compilation date 10 June 2025, including amendments up to Act No. 118, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A04858.txt`.

Nothing else is brought in. No regulation or rule of court is needed for the provisions encoded, except the form of a s 67 or s 97/98 notice (ss 67(2), 99), which is taken as given.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ea95-accused.l4` | `ea95-cases-accused.l4` | 91 written, 91 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The accused person**: the defendant in a criminal proceeding, from charge through trial. The questions are the ones that person asks: "Can they make me give evidence?", "Can my wife be made to give evidence against me?", "Must I answer a question that incriminates me?", "Can what I told the police be used against me?", "I wasn't cautioned — does that matter?", "Can they bring up what I did before?".

Most of the Act is addressed to the court ("the court may refuse", "is not to be admitted unless") or limits the prosecutor. Those provisions are encoded as what they mean for the accused: whether the evidence can be used against me, what the prosecutor may not say, what I may do in my defence. No question is asked from the seat of the court, the prosecutor or the police.

The 2026-10-18 defaults:

- **The Act alone.** No other instrument is brought in. Who bears the burden of proving a fact (for s 141) is for the law creating the offence — for a Commonwealth offence, Criminal Code Part 2.6 — and is asked as a fact.
- **The actors the text names:** the defendant, an associated defendant, the defendant's spouse, de facto partner, parent and child, a witness, an investigating official, the prosecutor, the court.
- **Judgments handed to others are answered conditionally.** Every finding, satisfaction or discretion of the court is an input worded as "the court finds …" or "the court is satisfied …": reasonable grounds (s 128), harm outweighing the evidence (s 18(6)), reliability (s 85), unfairness (s 90), the s 138 balance, significant probative value (ss 97, 98), the s 101(2) balance, the s 137 and s 135 weighing. None is guessed.
- **The Act's own definitions are worked out from facts:** "federal court", "criminal proceeding", "associated defendant", "admission" (as a first-hand admission), arrest as extended by s 139(5) and (6). Borrowed or evaluative terms ("de facto partner", "investigating official", "available to give evidence" in Dictionary Part 2 cl 4) are asked as facts with the definition in the `@desc`.
- **One case:** one accused, one piece of evidence (or one question in the witness box).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** ss 1–3, 8–11 (except as noted), Chapter 5.

## Scope

**In:** s 4 (to which proceedings the Act applies) with the Dictionary's "federal court" and "criminal proceeding"; ss 12, 13, 17, 18, 20 (competence and compellability of the accused and family, comment on not giving evidence); ss 59, 60, 65, 66, 67 (hearsay as it affects the accused, including s 65(8) for the defence); ss 81, 82, 83, 84, 85, 86, 89, 90 (admissions and silence); ss 94, 97, 98, 100, 101 (tendency and coincidence); ss 110, 112 (good character); ss 118, 119, 122, 123 (client legal privilege; ss 121, 124–126 asked as one fact); s 128(1)–(10) (self-incrimination and its certificate; (12)–(14) noted); ss 135, 137, 138, 139 (exclusions); s 141 (standard of proof).

**Out:** the rest of Chapter 2 (oaths, examination and cross-examination, documents); Part 3.3 (opinion); ss 87, 88; Part 3.5 (judgments and convictions); Part 3.7 (credibility); s 111; Part 3.9 (identification evidence — the accused would meet it, and it is the next thing to add); s 120, ss 126A–127, s 128A, Division 3 of Part 3.10 (public interest immunity); ss 136, 140, 142 onwards; Chapter 5; everything that applies only in civil proceedings. Other hearsay exceptions (ss 63, 64, 66A, 69–75) are asked as one fact.

## What the Act turns out to say

1. **The Act does not govern most Commonwealth prosecutions.** It applies to "all proceedings in a federal court" (s 4(1)), and a "federal court" is the High Court or another court created by the Parliament, not the Supreme Court of a Territory (Dictionary). Most people charged with a Commonwealth offence are tried in a State or Territory court, where s 79 of the Judiciary Act 1903 (s 4 Note 4) picks up that State's or Territory's evidence law. That law is not encoded, so such a case answers `not covered`. Asserted (Bea, in the Magistrates Court of Western Australia). In NSW, Victoria, Tasmania, the ACT and the NT the local Evidence Acts largely mirror this one; that is not encoded here either. A new ledger entry is raised for the Judiciary Act s 79 (see below).
2. **A sentencing hearing is governed only by direction** (s 4(2)–(4)), and **an appeal from a State court is not governed at all** (s 4(5)). Asserted.
3. **A prescribed taxation offence is not a "criminal proceeding"** (Dictionary), so the protections for defendants in criminal proceedings (ss 17, 18, 20, 85, 86, 89, 90, 101, 137, 141) do not apply to it as such. Asserted (the answer says so; the other questions do not repeat the check).
4. **The prosecution can never call the accused** (s 17(2): "not competent to give evidence as a witness for the prosecution"). Asserted.
5. **There is no longer any offence for which a spouse, partner, parent or child cannot object.** Former s 19 was repealed by Act No. 113, 2015 (endnotes). The s 18 objection is open on any charge, and decided by the court's weighing of harm against the desirability of the evidence. Asserted (no question asks the offence).
6. **Section 20 applies only to indictable offences.** For a summary charge the Act says nothing about comment on the accused's silence at trial; the encoding answers `not covered` rather than guess the common law. Asserted.
7. **The privilege against self-incrimination does not cover the accused's own acts and state of mind in issue** (s 128(10)). In the witness box at their own trial the accused cannot object to questions about the very acts and intent charged; s 128 protects them on collateral matters only. Asserted.
8. **A certificate protects derivative evidence too, but not against perjury or at a retrial** (s 128(7), (9)). Asserted.
9. **The accused's own hearsay is easier to admit than the prosecution's.** For the prosecution, an absent maker's first-hand statement needs a s 65(2) circumstance; for the defendant, s 65(8) needs only first-hand evidence and notice. Asserted.
10. **Silence before police is protected only against an investigating official.** Section 89 forbids any unfavourable inference — including on credibility (s 89(4)) — from refusing to answer an investigator, but does not reach questions from a private person (an employer, a victim). Asserted.
11. **A police officer's notes of oral answers need the accused's mark; a recording does not** (s 86(2), (4)). Asserted.
12. **"Under arrest" for the caution rule includes being held for questioning** (s 139(5)), except at the border or under a power to detain and search or to require answers (s 139(6)). An official without arrest power must caution once they believe there is sufficient evidence (s 139(2)). Asserted.
13. **Section 138 puts the burden on the prosecution.** Improperly or illegally obtained evidence "is not to be admitted unless" the desirability of admitting it outweighs the undesirability; the encoding excludes it unless the court so finds. Admissions after knowingly impairing questioning or a knowingly false statement are improper by definition (s 138(2)). Asserted.
14. **Prosecution tendency and coincidence evidence must clear a higher bar than the defence's:** significant probative value (ss 97, 98), and then probative value that "substantially outweighs" its prejudicial effect (s 101(2)), unless it answers the accused's own tendency or coincidence evidence (s 101(3), (4)). Asserted.
15. **Who bears the burden of proof is not in this Act.** Section 141 sets the standards (beyond reasonable doubt for the prosecution's case, the balance of probabilities for the defendant's), but a "case of a party" is defined by the legal burden, which the law creating the offence allocates. Asserted as an input.

## Raised in the ledger

- **Judiciary Act 1903 s 79** (`subjects/au/requirements.jsonl`, raised by this encoder): which State or Territory law of evidence governs a Commonwealth prosecution tried in a State or Territory court. Finding 1 turns on it. Satisfied on 2026-10-23 by the Judiciary Act's accused seat (`subjects/au/judiciary-act-1903/encodings/baseline-2026-10/`, `Which evidence law governs question`): the evidence law of that State or Territory, except where a Commonwealth law (such as this Act's ss 5, 131B, 128(12)–(14), 185–187) otherwise provides. This encoding still answers `not covered` for a State or Territory court, because the State's or Territory's evidence law itself is not encoded; the link cannot be joined in L4 across folders.

## What would need doing before this is worth relying on

- **The State and Territory evidence law** for the courts where Commonwealth offences are actually tried (for Western Australia, `subjects/au/wa/evidence-act-1906/` and `evidence-act-2025/`, both deposited without an encoding), with the Judiciary Act s 79 link.
- **Part 3.9 identification evidence** and **Part 3.7 credibility**, which an accused meets often.
- **Case law.** No case was read. The s 138 balance, "significant probative value", the s 18(6) weighing and unfairness under s 90 are worked out by the courts; this encoding asks each as the court's finding.
- **Rules of court** for the form of s 67 and s 97/98 notices (ss 67(2), 99).
- An independent test pass and a human review.
