# Judiciary Act 1903 — baseline encoding, the claimant's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (regulative rules for the duties the text puts on me, the court, the Registrar and the paying Minister or Treasurer).
There is no REFUSE in it; a question that reaches a gap answers `not covered` with the reason, or `NOTHING`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It sits **beside** `../baseline-2026-10/` (the accused's seat, ss 68, 68A, 79, 80 on the criminal side). Nothing there was changed or imported; this module keeps its own names. No ledger entry asked for it; it was written as part of a run over the Acts behind compensation and other civil claims, with the focus "the provisions a claimant meets".

Every question is a function named as the claimant would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 24 exported questions, grouped under `§§` headings in the order a claim meets them (where to sue; competent court; suing a State; service; rights and costs; which law; invalid State taxes; review of a Commonwealth officer; constitutional points; interest; remittal; getting paid; being sued by the Commonwealth; Legal Services Directions). Headings for situations the person may not be in say so in brackets ("if you have a judgment against a government").

**Regulative rules.**

| Rule | Party | Modal | Seat question that reads the same text |
|---|---|---|---|
| `s 63 -- I must serve process on the Attorney-General or the person appointed to receive service` | me | MUST serve the Attorney-General or the appointed person (no time limit) | `Whom must I serve question` |
| `s 78B(1) -- the court must not proceed until the Attorneys-General have had notice and a reasonable time` | the court | SHANT proceed with an ordinary step before notice and time; s 78B(2)(c), (5) steps excepted | `Must the court wait for the Attorneys-General question` |
| `s 65 -- I must not issue execution against the property or revenues of the Commonwealth or a State` | me | SHANT issue execution or attachment | `Can I execute against the government question` |
| `ss 65, 66 -- the Registrar must certify my judgment and the government must then satisfy it` | the Registrar, then the Minister for Finance or the State's Treasurer | MUST certify, HENCE MUST pay exactly the judgment sum | `How is my judgment against a government paid question` |

None of these duties has a deadline in the Act, so no rule has a `WITHIN`. The case file asserts, through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`), that a trace ends FULFILLED or that it does not; breaches are also `#TRACE`d with an `-- expect:` line, because on the stable `l4` a breached trace cannot be compared with `EQUALS`.

## Edition

The compilation registered as **C2024C00864** (Compilation No. 51, compilation date 11 December 2024, including amendments up to Act No. 115, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C1903A00006.txt`. Part IX (ss 56–67) is at line 495 of the deposit, s 39B at 182, s 44 at 264, ss 77MA–77N at 866, s 78B at 1084, s 79 at 1096, ss 82–83 at 1121, the Schedule at 1154. The commencement of s 77MA is read from endnote 3 and its note (g) (lines 1470–1475 and 1800–1801).

Nothing else is brought in. The Constitution (ss 75, 76, which settle the matters in which the High Court has or can be given original jurisdiction, and s 75(v)) is not deposited; those matters are asked as facts. The High Court Rules (the s 77N rate) are not deposited; the rate is not given. The National Security Information (Criminal and Civil Proceedings) Act 2004, which s 39B(3) borrows, is not read; the kind of decision is asked as a fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `jc-claimant.l4` | `jc-cases-claimant.l4` | 107 written, 107 satisfied; 5 traces, each as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. Every exported question has cases, with the edges: the day before and the day of s 77MA's commencement, exclusions equal to the judgment sum and $1 over it, a payment $1 short of the judgment, each branch of s 39B and s 56(2).

## Seat

**The claimant**: an individual with a civil claim against the Commonwealth, a State or a Commonwealth officer (for an injury, a breach of contract, review of a decision, recovery of an invalid tax), or in a suit in federal jurisdiction; and the same individual when the Commonwealth sues them for a penalty or a tax or enforces a judgment against them. The questions are the ones that person asks: "Where can I sue the Commonwealth for my injury?", "Whom do I serve?", "Can I get costs?", "Which State's law applies?", "Must the court wait for the Attorneys-General?", "Do I get interest?", "How do I get paid?", "Where can the Commonwealth sue me?".

The provisions are addressed to courts, Registrars, the Minister for Finance, State Treasurers and the Attorney-General. They are encoded as what they mean for the claimant. No question is asked from the seat of the court, the Commonwealth or a State.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is brought in (see Edition).
- **The actors the text names:** the person making the claim, the Commonwealth, the States (and, where the Act names them, the Northern Territory and the Australian Capital Territory), the Attorneys-General, the Registrar or other appropriate officer, the Minister for Finance, the State Treasurer, the High Court, the Federal Court, the Federal Circuit and Family Court of Australia, the Supreme Courts and other courts of competent jurisdiction, the prosecutor.
- **Judgments handed to others are answered conditionally:** the court's satisfaction of notice and reasonable time (s 78B(1)), what it "thinks necessary in the interests of justice" (s 78B(5)), good cause against interest (s 77MA(1)), the s 39B(1E) determinations. All are inputs.
- **The Act's own definitions are worked out from facts:** court of competent jurisdiction (s 56(2)), the place in which federal jurisdiction is exercised (s 79(1A)(b)), the laws s 79(3) covers, "State" for s 78B (s 78AA), the Attorneys-General who must get notice (s 78B(3)(b)), the parts of a judgment that cannot carry interest (s 77MA(2)(a), (3), (4)). Borrowed terms (contract, tort, federal jurisdiction, "related criminal justice process decision", "Legal Services Direction") are asked as facts with a gloss.
- **One case:** one claim, one suit, one judgment.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

`JUST FALSE` where the text says no in its own words: s 56(2)(b) ("is not a court of competent jurisdiction"), s 65 and s 67E ("No execution ... shall be issued"), s 55ZI ("is not liable"), s 55ZG(3) ("may not be raised ... except"), s 77MA(2)(b), (e) ("does not apply", "does not authorize"), a failed "where" or "if" (s 78B(1), s 39B(1E)), "upon application" (read as "where", ruling (c) of 2026-11-05). `NOTHING` where the text is silent or a scope limit without "only" fails: s 64 outside a suit with the Commonwealth or a State; s 79(2) for a suit that is not to recover an invalid tax; s 77MA outside the High Court, outside money claims, or for a cause of action before 22 November 1984; s 77N for another court's judgment; s 44 where neither subsection reaches; s 78B for a tribunal; s 55ZI where the act was not under a Direction (or bad-faith purported compliance by someone other than the Attorney-General); s 65 and s 67 for the Australian Capital Territory or another Territory.

Fork lines (case-by-case sites, for the reviewer to overrule):

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| s 56(1)(b), (c) "court of competent jurisdiction" | `Is this court competent for my suit against the Commonwealth question` | a court competent on no ground: `JUST FALSE` | `NOTHING` (the term left to State and Territory law) |
| s 78B(1) "unless and until" once met | `Must the court wait for the Attorneys-General question` | `JUST FALSE` (the duty is spent) | `NOTHING` |
| s 77MA(1) "other than proceedings on appeal" | `Must the High Court give interest up to judgment question` | `JUST FALSE` | `NOTHING` |

## Scope

**In:** s 39B(1), (1A) (as the general Federal Court head, not separately asked), (1B)–(1EA), (2); s 44(1), (2A), (3); ss 55ZG(3), 55ZI; s 56(1), (2); s 58; s 63; s 64; s 65 and the Schedule (named, not reproduced); s 66; s 67; s 67E; s 77MA (with its commencement); s 77N; ss 78AA, 78B(1), (2)(c), (3)(b), (5); s 79(1), (1A)(b), (2)–(4); s 80A; ss 82, 83.

**Out, and why:**
- Parts I–V except s 44 (the High Court's internal procedure, appeals and special leave: the court's machinery, not a claimant's entitlement), including s 25A summary judgment, s 26 costs and s 27 appeals as to costs (High Court only; left for a High Court practice encoding).
- ss 38, 39, 39A (exclusive and invested jurisdiction: what they give a claimant is asked in s 56, s 58 and s 39B as facts), s 39B(1A) beyond its role as the general head, s 39B(3) definitions beyond the decision kinds.
- ss 40–43, 45 (removal into the High Court: the Attorney-General's or the Court's step), s 44(2), (4).
- Part VIII (ss 46–51: orders in the Victorian criminal proceedings about the 1983 Sheraton Hotel incident, limited by s 51 to orders made within two years of a 1984 Victorian Act), Part VIIIA except ss 55ZG(3), 55ZI (the right to practise, the Register, the AGS).
- ss 57, 59–62 (suits by or between governments: no individual seat), s 60, s 67A–67D, 67F (Part IXA except the s 67E bar).
- Part X (criminal jurisdiction: see the accused's seat in `../baseline-2026-10/`).
- ss 77M, 77P–77V (High Court enforcement detail, interpleader, receivers, suppression and non-publication orders, vexatious proceedings orders, appeals): High Court practice.
- s 78 (appearance), s 78A (intervention: the Attorney-General's step), s 78B(2)(a), (b), (3)(a), (4).
- s 80 (common law to govern; encoded in the accused's seat; the civil reading is the same words), s 81, ss 84–85 (seizures and forfeiture of property), ss 86–88 (Rules of Court, regulations).
- What the State or Territory law that s 79 picks up says (its limitation periods, notice rules, procedure).

## What the Act turns out to say

1. **Section 56 is worded for claims "in contract or in tort".** A claim against the Commonwealth of another kind (restitution, a statutory entitlement, judicial review) finds its forum elsewhere (s 39B, s 39(2) and the Constitution). The encoding answers `not covered` and says so. Asserted.
2. **Section 56(2)(a) and (b) overlap.** A court sitting in a State capital that would be competent if the Commonwealth resided there "is" competent under (a), while (b) says "any other court is not" competent if its competence would depend on the Commonwealth's residence. Read as written, (b) reaches only courts outside (a); the encoding tests (a) first. Asserted (the Perth District Court case).
3. **The Territories fall through ss 63, 65 and 66.** They name only "the Commonwealth or a State". There is no Judiciary Act rule on whom to serve in a suit against a Territory, and no certificate-and-payment route for a judgment against one. Section 67E bars execution against the Northern Territory's property, but nothing in this Act bars it against the Australian Capital Territory, and nothing says who pays a judgment against either. Asserted: `not covered` for service and payment; `JUST FALSE` for execution against the Northern Territory; `NOTHING` for the ACT.
4. **Nine Attorneys-General get notice of a constitutional point.** Section 78AA makes the ACT and the Northern Territory "States" for Division 1A, so s 78B(1) reaches the Commonwealth's and eight others'; a government party's own Attorney-General is dropped (s 78B(3)(b)). An external Territory is not a "State" here, so a suit against Norfolk Island's administration still needs all nine. Asserted.
5. **The Attorney-General's s 55ZI immunity has no good-faith condition.** Subsection (1) covers "compliance, or purported compliance"; subsection (2), for everyone else, only "compliance, or in good faith in purported compliance". Asserted.
6. **Section 39B(2) takes only Division 1 Judges out of "officer of the Commonwealth".** A Judge of the Federal Circuit and Family Court of Australia (Division 2) is not excluded, so read literally s 39B(1) reaches mandamus against one in the Federal Court. Section 39B(2) also does not mention (1EA), which concerns the Attorney-General's or a Minister's national security decisions, so the omission has no visible effect. Recorded, not asserted beyond the Division 1 case.
7. **Section 77MA commenced on 22 November 1984** (No. 165, 1984, assented to 25 October 1984, in force on the twenty-eighth day after assent). The text says a cause of action "that arises after the commencement"; a cause arising on 22 November 1984 is read as after it, because an Act commences at the start of its day. Asserted at both edges.
8. **Interest up to judgment and on judgment debts are High Court rules only** (ss 77MA, 77N). A claimant in a State court or the Federal Court meets that court's own law. The encoding answers `NOTHING` outside the High Court. Asserted.
9. **Section 77MA(4) restores interest on a liability the plaintiff has met, from the date it was met**, not from the date the cause of action arose. Asserted.
10. **No time limit for paying a judgment against the Commonwealth or a State.** Section 66 says the Minister for Finance or the Treasurer "shall satisfy the judgment out of moneys legally available" on receiving the certificate, with no period. The rule has no `WITHIN`; a payment $1 short does not discharge it. Asserted.
11. **Whether a State limitation period binds a suit against the Commonwealth is not answered by the text alone.** Section 64 ("rights of parties ... as nearly as possible the same") and s 79(1) ("in all cases to which they are applicable") are the routes, and the courts have read them; no case was read here. Section 79(3)(a) shows the drafter treating a State limitation law as "applicable" in at least one kind of suit (recovering an invalid State tax), which the encoding asserts.

## Raised in the ledger

Nothing. The State and Territory law s 79 picks up (limitation periods, Crown proceedings, procedure) is the next thing a claimant needs; for Western Australia, see the WA subjects.

## Links

- **Accused's seat** (`../baseline-2026-10/`): ss 68, 68A, 79 and 80 on the criminal side. The two encodings answer s 79(1) with the same rule from different seats; they cannot be joined in L4 (two seats in different encoding folders), so the link is this note.
- **Evidence Act 1995 baseline** (`subjects/au/evidence-act-1995/encodings/baseline-2026-10/`): the Commonwealth law that "otherwise provides" on evidence points under s 79(1).

## What would need doing before this is worth relying on

- **The Constitution** (ss 75, 76), deposited, so the High Court's original jurisdiction in s 56, s 58 and s 39B can be worked out rather than asked.
- **The High Court Rules** (the s 77N rate) and the Federal Court of Australia Act 1976 (interest and costs in the Federal Court).
- **The State and Territory Crown proceedings and limitation Acts** that s 64 and s 79 pick up.
- **Case law.** No case was read. The reach of s 64 and s 79 over limitation laws, the meaning of "court of competent jurisdiction", and "matter arising under the Constitution" are worked out by the courts; this encoding takes the text.
- An independent test pass and a human review.
