# Judiciary Act 1903 — baseline encoding, the accused's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (regulative rules for the duties the text puts on courts).
There is no REFUSE in it; a charge that is not for a Commonwealth offence, in a court not otherwise exercising federal jurisdiction, answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0085` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

Every question is a function named as the accused would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 8 exported questions, grouped under `§§` headings in the Act's order of use (can this court deal with my charge; whose procedure; whose evidence law; gaps; sentence; committal).

**Regulative rules.** Sections 68 and 79 are addressed to courts ("shall apply and be applied", "shall ... be binding on all Courts"), so four rules are written as `PARTY … SHANT/MAY … LEST BREACH … BECAUSE`, and the seat questions are derived from the same definitions:

| Rule | Party | Modal | Seat question that reads the same definitions |
|---|---|---|---|
| `s 79(1) -- the court must apply the law of evidence of the State or Territory in which it exercises federal jurisdiction` | the court | SHANT apply another State's or Territory's evidence law | `Which evidence law governs`, `Whose law decides who can be a witness` (both through `the State or Territory in which the court exercises federal jurisdiction`, s 79(1A)) |
| `s 68(1) -- the court must apply that State's or Territory's law of arrest, custody, bail and procedure` | the court | SHANT apply another's | `Whose procedure governs` |
| `s 68(5A) -- the court may decline summary jurisdiction ...` | the court | MAY decline | `Can the court refuse to deal with my charge summarily` |
| `s 68A(3), (4) -- the committals court must invite the Director's suggestion and consider it before committing` | the committals court | SHANT make the committal order without both | `Which court can I be committed to` |

The "binding" duties in ss 68(1) and 79(1) have no deadline: they are kept by not being broken, so they are written as prohibitions on applying the wrong law. The case file asserts each question, asserts the one rule whose trace ends `FULFILLED` (the s 68(5A) permission used), and `#TRACE`s the others with an `-- expect:` line (a breach, or the prohibition still standing). On the stable `l4`, `EVALTRACE … EQUALS FULFILLED` is TRUE when the trace is fulfilled, but neither TRUE nor FALSE when it ends in a breach (an assertion and its negation both fail), so a breach cannot be asserted; it is traced.

## Edition

The compilation registered as **C2024C00864** (Compilation No. 51, compilation date 11 December 2024, including amendments up to Act No. 115, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C1903A00006.txt`. Section 68 is at line 579 of the deposit, s 68A at 608, s 79 at 1096, s 80 at 1114.

Nothing else is brought in. Section 80 of the Constitution (jury trial on indictment), to which s 68(2) is made subject, is not deposited and is quoted only as s 68 points to it. The Evidence Act 1995 provisions named in the evidence question's answer and `@desc` (ss 4, 5, 128(12)–(14), 131B, 185–187) are read from that Act's deposit (`subjects/au/evidence-act-1995/registers/source-bundle/C2004A04858.txt`) and not encoded here.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ja-accused.l4` | `ja-cases-accused.l4` | 36 written, 36 satisfied; 6 traces, each as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The accused person**: someone charged with an offence against a law of the Commonwealth, whose case is in a State or Territory court (or, for comparison, a federal court). The questions are the ones that person asks: "Can the Magistrates Court deal with my Commonwealth charge?", "Whose bail law applies to me?", "Which Evidence Act governs my trial?", "Can the court send my case back to the State where it happened?", "Can I be sent up for sentence after pleading guilty?", "Which court will I be committed to?".

The provisions are addressed to courts. They are encoded as what they mean for the accused: which law binds the court in my case, what the court may do with my charge, and what it must do before committing me. No question is asked from the seat of the court, the Director of Public Prosecutions or the police.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is brought in. Whether the State or Territory has a particular procedure (committal for sentence after a guilty plea, s 68(7)) is asked as a fact, and so is whether a Commonwealth law makes its own provision on a point.
- **The actors the text names:** the person charged, the courts of a State or Territory, the committals court and the superior State or Territory court, the Federal Court of Australia, the Director of Public Prosecutions.
- **Judgments handed to others are answered conditionally.** The court's satisfaction that declining jurisdiction is appropriate (s 68(5A)) is an input. Whether a State or Territory law is "applicable" (ss 68(1), 79(1)) is left in the answer's words ("so far as it is applicable"), not decided.
- **The Act's own definitions are worked out from facts:** federal jurisdiction from a Commonwealth charge (ss 39(2), 68(2)); the State or Territory in which a court exercises federal jurisdiction (s 79(1A)(b)); when limits as to locality are lifted (s 68(5), (5C)). "Offence against a law of the Commonwealth", "indictable", "federal court" are asked as facts with a gloss.
- **One case:** one accused, one charge, one court.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Parts I–VIII except as noted, ss 69–78B, Part IXA onwards.

## Scope

**In:** s 68(1), (2), (5), (5A), (5B), (5C), (7)–(10); s 68A(1)–(5); s 79(1), (1A)(b); s 80; with s 39(2) as the source of the federal jurisdiction.

**Out:** s 68(4) (amending an information), (6) (arrest at sea), (11); s 68A(6); ss 68B–68D and s 79(1A)(a) (Federal Court indictable and related summary proceedings); ss 69–78B (indictments, reserved points, High Court procedure); s 79(2)–(4) (recovering invalid State taxes); s 80A; Parts IXA onwards; civil matters throughout. What a State's or Territory's law of evidence, procedure or bail actually says is not encoded.

## What the Act turns out to say

1. **For a Commonwealth prosecution in a State or Territory court, that State's or Territory's evidence law governs,** because s 79(1) makes "the laws of each State or Territory, including the laws relating to procedure, evidence, and the competency of witnesses" binding on every court exercising federal jurisdiction there, "except as otherwise provided by the Constitution or the laws of the Commonwealth". The Evidence Act 1995 reaches such a court only through its own extended-application provisions (s 4 Note 3: ss 5, 185–187; and s 131B, s 128(12)–(14)), which are a Commonwealth law "otherwise providing" on their points. That is `REQ-0085`'s assertion. Asserted (Bea, in the Magistrates Court of Western Australia, the entry's first test).
2. **"In that State or Territory" follows the proceeding, not the offence.** Under s 79(1A)(b) the court is taken to exercise federal jurisdiction in the State or Territory where the proceeding was commenced, or, if transferred or remitted, where it went. A case started in Perth and transferred to Darwin takes Northern Territory evidence law. Asserted.
3. **Competency of witnesses goes with the evidence law.** Section 79(1) names it expressly, so whether the accused or a spouse can be made to give evidence in a State court is a question for that State's law (or a Commonwealth provision that otherwise provides), not the Evidence Act 1995's ss 12–20. Asserted.
4. **Section 79 needs federal jurisdiction, and a Commonwealth charge supplies it** (s 68(2), with s 39(2)). A State charge alone does not, so the encoding answers `not covered`; a State charge in which a constitutional point is raised does, and s 79 then picks up the same State's law. Asserted.
5. **The State's procedure, bail and arrest law applies to the Commonwealth charge** (s 68(1)) "so far as [it is] applicable"; where a Commonwealth law makes its own provision on a point, that law governs the point. Asserted, with the Commonwealth law asked as a fact.
6. **Limits as to locality are lifted unevenly.** Summary jurisdiction and committal for sentence are conferred "notwithstanding any limits as to locality" (s 68(5)); committal and trial on indictment only for an offence committed outside every State and Territory, such as at sea (s 68(5C)); an appeal never. Asserted.
7. **A State court may send a summary Commonwealth charge back to the State where it happened** — it may decline jurisdiction over an offence committed in another State or Territory if satisfied it is appropriate, "including the public interest" (s 68(5A), (5B)). A permission, so not using it is no breach. Asserted.
8. **A guilty plea in a summary court can lead to sentence in a higher court, as if on indictment** (s 68(7), (10)), even for an offence that must otherwise be prosecuted on indictment (s 68(8)), if the State or Territory has the procedure. Asserted.
9. **Where both the Federal Court and a State court can try the offence, the committals court chooses,** but must first invite the Director of Public Prosecutions to suggest a court and must consider specifying it (s 68A(3), (4)), "even if the Director of Public Prosecutions is not a party" (Note). The accused is not invited to suggest one. Asserted; the duty is traced.
10. **A trial on indictment of a Commonwealth offence is "subject to ... section 80 of the Constitution"** (s 68(2)), which requires a jury. The Constitution is not deposited, so the answer quotes s 68's pointer rather than encoding s 80. Asserted.

## Raised in the ledger

Nothing new. The State and Territory law that s 79 picks up is the next thing an accused needs (see below); for Western Australia it is already deposited.

## Links

- **Evidence Act 1995 baseline** (`subjects/au/evidence-act-1995/encodings/baseline-2026-10/`): its s 4 question answers `not covered` for a State or Territory court and names s 79 as the reason. This encoding's `Which evidence law governs question` is the answer that `not covered` points at. The two cannot be joined in L4 (IMPORT does not cross folders), so the link is this note and that encoding's NOTES.
- **Criminal Code baseline** (`subjects/au/criminal-code-act-1995/encodings/baseline-2026-10/`): a s 474.17 charge tried in a State court is the worked case here.
- Not yet entered in `docs/au-baseline-links.md`, which covers the 118 baselines of 21 October 2026.

## What would need doing before this is worth relying on

- **The State and Territory law** s 68(1) and s 79(1) pick up: for Western Australia, `subjects/au/wa/evidence-act-1906/` and `evidence-act-2025/` (deposited without an encoding), and the WA Bail Act and Criminal Procedure Act.
- **Section 80 of the Constitution**, deposited, so the jury answer can be encoded rather than quoted.
- **Sections 68B–68D and 79(1A)(a)**, for an accused tried on indictment in the Federal Court.
- **Case law.** No case was read. Whether a State law is "applicable", when a Commonwealth law "otherwise provides", and whether a Territory court exercises "federal jurisdiction" in the sense of s 79 are worked out by the courts; this encoding takes the text.
- An independent test pass and a human review.
