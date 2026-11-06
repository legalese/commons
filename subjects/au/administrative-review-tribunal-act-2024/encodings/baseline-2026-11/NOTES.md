# Administrative Review Tribunal Act 2024 — baseline encoding, the applicant's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `not covered` with the reason, or `NOTHING`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is the first encoding of this Act. No ledger entry asked for it; it was written as part of a run over the Acts behind compensation and other claims, with the focus "the provisions a claimant meets". For a claimant, this Act is the route from a Commonwealth decision on a claim (compensation, social security, veterans' entitlements and the many other decisions an Act or instrument makes reviewable) to merits review, and on to the Federal Court.

Every question is a function named as the applicant would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 37 exported questions, grouped under `§§` headings in the order a review meets them (notice and reasons from the decision-maker; applying; after applying; representation; dismissal and reinstatement; the Tribunal's decision; the guidance and appeals panel; second review; the Federal Court; help with costs). Headings for situations the person may not be in say so in brackets.

**Regulative rules.** Each is run inside a question that takes plain dates; no question takes a DEONTIC or an EVENT.

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `s 18 -- I must apply within the prescribed period` | me | DO apply WITHIN the days the rules (or the enabling law) allow; LEST breach, s 19 extension the route | `Am I in time to apply question`, `Can I apply for second review late after a tax review question` |
| `s 269 -- the decision-maker must answer my request for reasons within 28 days` | the decision-maker | MUST give a statement or a written refusal WITHIN 28 | `Where does my request for reasons stand question` |
| `ss 23, 27 -- the decision-maker must give me the reasons and documents` | the decision-maker | MUST give the statement and documents WITHIN 28, or the period as shortened or extended under s 28 | `Where are the decision-maker's reasons and documents question` |

The case file asserts, through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`), that a trace ends FULFILLED or that it does not; each rule's breach is also `#TRACE`d with an `-- expect:` line, because on the stable `l4` a breached trace cannot be compared with `EQUALS`.

**Dates.** `art-dates.l4` uses the built-in date functions only (no daydate). "Within 28 days after" a day excludes that day (Acts Interpretation Act 1901 s 36(1), borrowed, not deposited): 2 March gives 30 March. The 3 months of s 84(4)(b) use the Acts Interpretation Act month (s 2G, borrowed). Section 174's count skips 24 December to 14 January and the windows of s 174(3) and s 131X by stepping day by day.

## Edition

Administrative Review Tribunal Act 2024, No. 40, 2024, **Compilation No. 5, compilation date 18 May 2026** (register id C2026C00202, includes amendments up to Act No. 3, 2026), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2024A00040.txt`. Part 3 is at line 275 of the deposit, Part 4 Division 8 at 1156, Part 5 Division 3 at 1491, Part 5A at 1601, Part 7 at 2258, Part 10 at 3221, s 294 at 3685.

Nothing else is brought in. **The Administrative Review Tribunal Rules and the practice directions are not deposited**: the period to apply (s 18(1)), the time to pay a fee (s 98), the time for giving the decision (s 111(3)), the kinds of decision the rules take out of ss 123 and 294, and fees (s 296) are inputs or left out. The Acts that make decisions reviewable are not read; whether an Act provides for review is asked as a fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `art-dates.l4` | (exercised through the cases below) | 0 errors, 0 warnings |
| `art-applicant.l4` | `art-cases-applicant.l4` | 196 written, 196 satisfied; 3 traces, each a BREACH as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text before the run. Every exported question has cases, with the edges: day 28 and day 29 of each 28-day period, a February with 28 days, the 3-month period ending in a month with no corresponding day, the 24 December to 14 January break (a period running into it, one starting inside it, one ending on 15 January), an excluded window both ends counted, a rules period shorter than the s 18(3) floor.

## Seat

**The applicant**: a person whose interests are affected by a Commonwealth decision that an Act or legislative instrument makes reviewable (most often, for this run, a claimant whose compensation, social security, veterans' or other claim was refused, reduced or not decided), who asks the decision-maker for reasons, applies to the Tribunal, takes part in the review, and may go on to the guidance and appeals panel, second review or the Federal Court. In s 84 the seat is the person stepping in for an applicant who has died or become bankrupt. The questions are the ones that person asks: "Can I ask for reasons?", "Am I in time?", "Can the Tribunal extend my time?", "Does applying stop the decision?", "Can I get my application reinstated?", "When does the Tribunal's decision take effect?", "By when must I appeal?".

The decision-maker, the Tribunal, the President, the Attorney-General and the Federal Court get no seat. Their duties are encoded as what they mean for the applicant (what must be given to me, by when), and their judgments are inputs.

The 2026-10-18 defaults:

- **The Act alone.** The rules and practice directions are not deposited (see Edition); their numbers are inputs.
- **The actors the text names:** the applicant, the decision-maker, the Tribunal, the President, other parties, the Attorney-General of the Commonwealth, the Commissioner of Taxation (s 131J), the Federal Court.
- **Judgments handed to others are answered conditionally:** what the Tribunal "considers" reasonable (s 19), a reasonable time and special circumstances (s 20), satisfaction that a decision is not reviewable (s 97) or an application frivolous (s 101), desirability of a stay (s 32), the decision-maker's "reasonable time" (s 269(8)(b)), the Attorney-General's hardship and reasonableness (s 294(7)). All are inputs.
- **The Act's own definitions are worked out from facts:** reviewable decision (s 12), an organisation's affected interests (s 15), the deemed decision (s 16), eligible social services decision (s 131C), the review pathway (s 266(3)), end of the appeal period and completion (s 107(7)) as far as the inputs allow. Borrowed terms ("interests are affected", "question of law", child care decision, claimant decision) are asked as facts with a gloss.
- **One case:** one decision, one application.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The rulings, word for word as section 5 of `docs/ENCODING-GUIDE.md` records them: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit. Periods ruling: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`.

Applied here: `JUST FALSE` for s 266(6) ("does not require"), s 269(6) ("must refuse"), s 108(3) ("may not be made"), s 97 (must dismiss), s 31(1) ("may not be altered otherwise than"), s 32(1) ("does not affect"), s 19(4), (7) ("must not extend"), s 102(8) ("cannot apply"), s 123(4)-(6) and s 131W ("does not apply", "cannot be made"), s 131D(2), s 131H, s 172(2), s 294(5); the 28-day periods of s 102(5), (7) and s 131J(2); failed "if" conditions in ss 19(2), 20(1), 270(1), 271(1), 294(7). `NOTHING` where the text is silent: s 266 outside a review pathway or for a person not affected; s 268 for a decision that is not reviewable; s 16 where it deems nothing; s 20 where a period applies; s 31 before any application; s 84 where it is not engaged; s 107 while an appeal is pending; s 108(4) where the Tribunal ordered otherwise; s 111 and s 112(5) outside their reach; s 123 for a non-party or a decision not under s 105; s 131D for a decision outside s 131C; s 172 without a question of law; s 294 for none of its roles.

Fork lines (case-by-case sites, for the reviewer to overrule):

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 266(2) "does not apply in relation to a decision by a court or ... the Tribunal" | `Must the decision-maker tell me of the decision and my review rights question` | `NOTHING` (the section does not reach it) | `JUST FALSE` (a flat negative) |
| F2 | s 17(1) for a person whose interests are not affected | `Can I apply to the Tribunal for review question` | `NOTHING` (a grant to affected persons, silent on others) | `JUST FALSE` (s 97 and s 173 treat standing as something the Tribunal decides against) |
| F3 | s 131D(1) for a person not affected | `Can I apply for second review question` | `JUST FALSE` | `NOTHING`, as F2 |
| F4 | s 172(1) "on a question of law" | `Can I appeal to the Federal Court question` | `NOTHING` | `JUST FALSE` (read as "only on a question of law") |
| F5 | s 174(3), s 131X "any day in the period between" the two days | `By when must I appeal to the Federal Court question` | both end days are not counted | neither end day is excluded (strictly between) |
| F6 | s 32(5) an order's stated period | `Is the decision I applied about stayed question` | in force on the last day of the stated period | ends at the start of that day |

## Scope

**In:** ss 12, 15, 16, 17, 18, 19, 20; ss 23, 27, 28(3)-(9), 29, 131G (the reasons and documents the decision-maker must give); ss 31, 32; s 66; ss 65(2), 83(2), (4) (named in the dismissal answer); s 84; ss 95-102; s 107; s 108(3)-(5); s 111; s 112(5)-(7); ss 123, 124(2) (in the description), 125; ss 131C, 131D, 131H, 131J, 131W, 131X; ss 172, 173, 174; ss 266, 268, 269, 270, 271; s 294.

**Out, and why:**
- Part 1 and Part 2 (ss 1-10: preliminary, establishment, objective, members): machinery. s 13 (instruments may provide for review) is the basis of s 12 and not separately asked. s 14 (who the decision-maker is) is the Tribunal's and President's concern.
- ss 21, 22 (notice of the application; other persons joining as parties): the Tribunal's steps and other people's applications; a later layer could take a joining party's seat.
- ss 24-26, 28(10), 30 (further statements and documents on Tribunal order, copies, privilege): the Tribunal's orders, with periods it sets.
- Part 4 Divisions 3 and 4 (practice directions; constituting and reconstituting the Tribunal, ss 36-48): machinery.
- ss 49-58 (general principles: discretion, informality, accessibility, the rules of evidence, scope of review, the right to present a case, the duty to assist): standards for the Tribunal and the parties with no threshold, deadline or entitlement a question could compute; s 55 in particular is a right with exceptions for non-participating parties and Part 6 that would answer TRUE for every applicant.
- ss 59-65 (Attorney-General as party, non-participating decision-makers, withdrawal of other parties) apart from s 65(2); ss 67, 68 (litigation supporters, interpreters); ss 69-94 (hearings, publication, summons, evidence, witness fees, directions, absence, adjournment, removal of parties, remittal under s 85, dispute resolution, public interest certificates, Attorney-General intervention): the Tribunal's procedure and powers.
- s 103 (agreed decisions), s 105 (the kinds of decision), s 106 (decision without a hearing), ss 109, 110 (guidance decisions), ss 113, 114 (publication, corrections), s 115 (taxing costs: the power to order costs is in other legislation), ss 116-120 (offences).
- ss 121, 122, 126-131 (the President's referral, notices, the panel proceeding): the President's and Tribunal's steps.
- Part 5A ss 131E, 131F, 131K-131V (how the Act applies on second review): mostly modifications of other Acts; ss 131G, 131J, 131W, 131X are in.
- Part 6 (Intelligence and Security jurisdictional area, ss 132-169): a separate jurisdiction with its own parties and certificates.
- ss 175-191 (constitution of the Federal Court, its powers, stays on appeal (s 178), transfer, references of questions of law, sending documents): the court's machinery.
- Parts 8 and 9 (members, management, the Administrative Review Council): machinery.
- s 267, s 272 (the rules on notices; the Attorney-General's certificate itself): s 272's effect is an input to s 269(10).
- Part 11 except s 294 (protected information, delegations, authorisations, advisory opinions, electronic documents, giving documents, s 292 short periods, immunities, review of the Act, rules, fees, regulations): machinery, or (s 292) a count that needs the registry's calendar; fees are set by rules that are not deposited.

## What the Act turns out to say

1. **The 28-day floor binds only the Tribunal's rules.** Section 18(3) forbids rules prescribing a period "ending before the day that is 28 days after the day the decision is made", but the note to s 18(1) says the enabling legislation "may specify a different period", which s 18(3) does not reach. A 21-day period in the enabling Act stands; the same period entered as the rules' answers `not covered`. Asserted.
2. **The floor counts from the decision, not from notice of it.** Section 18(3) runs from "the day the decision is made"; a person who learns of the decision late can have less than 28 days under a rule that counts from the decision. The encoding takes the rules' own start day as an input. Asserted (the 3 February 2026 case gives 3 March).
3. **An applicant who withdrew can still seek reinstatement on the ground of error.** Section 102(8) bars the applicant from the s 102(7) route after a withdrawal, but s 102(5) (error) applies to any dismissal, and s 95(2) makes a withdrawal a dismissal. Asserted.
4. **Section 19(4)(a) may shut out extensions for good.** The Tribunal "must not extend the period if ... section 102 permits the applicant to apply ... to reinstate". Section 102(5) and (7) allow "such longer period as the Tribunal, in special circumstances, allows", so it can be argued that s 102 always "permits" an application, and the extension route is then never open to someone whose earlier application was dismissed. The encoding takes "reinstatement available" as an input. Recorded.
5. **The s 266(6) proviso is placed after paragraph (c).** "and does not adversely affect the interests of any other person" follows (c)(iii) at paragraph level. Read as part of (c) only; read with (a) and (b) as well, a decision covered by another Act's notice rule would again need notice if it harmed someone else, which is unlikely to be meant. Encoded with (c). Asserted.
6. **A request for reasons on day 29 may be refused, not must be.** Section 269(8)(a) is permissive; the encoding answers "may refuse". The 28 days run from when the document was given, not from the decision. Asserted at both edges.
7. **Once a s 70 application is decided, the s 23 duty does not revive by itself.** Section 29(3): the decision-maker "does not need to give the statement or copy unless the Tribunal, after making its decision on the application for the order, orders the decision-maker to do so." The 28-day period does not restart without an order. Asserted (`on hold`).
8. **A public interest certificate keeps documents from me but not from the Tribunal.** Section 27(2) lifts only the duty to give parties copies. Asserted.
9. **The s 84 deadline runs from the Tribunal's awareness**, which the person stepping in may not know. Three months from 30 November ends on 28 February. Asserted.
10. **Section 107(3) overrides a later operative time the Tribunal itself specified**: with a stay in force, the decision waits for the end of the appeal period, even if the decision named an earlier day. Section 107(6) then lets the Tribunal or a court fix another time. Asserted.
11. **"Between" in ss 174(3) and 131X is not defined** (fork F5): whether the day the panel application is made, and the day the President decides, are counted changes the last day by up to two days. Asserted on the reading taken.
12. **Section 174(1)(b) borrows the s 112(5) request period**, 28 days after the decision is made; so where reasons could be requested and were not, the appeal period is in effect 56 days (plus the break) from the decision. Asserted.
13. **Second review time is the ordinary s 18 time "despite a contrary intention in any other law"** (s 131J(1)); the only late route is the child care subsidy tax-review case in (2), counted from the Commissioner's notice. Asserted.
14. **Assistance does not stop the clock** (s 294(9)). Said in the question's description; not computed.

## Raised in the ledger

Nothing. The Administrative Review Tribunal Rules (the s 18 period, fees, the s 123 and s 294 exclusions) are the next instrument an applicant needs; they are not deposited. The ledger `subjects/au/requirements.jsonl` was not changed.

## Links

- **Judiciary Act 1903 baseline, claimant's seat** (`subjects/au/judiciary-act-1903/encodings/baseline-2026-11/`): s 39B judicial review of a Commonwealth officer's decision, the other route from a decision.
- **Federal Court of Australia Act 1976 baseline** (`subjects/au/federal-court-of-australia-act-1976/encodings/baseline-2026-11/`): the court an appeal under s 172 goes to.
- **Safety, Rehabilitation and Compensation (Defence-related Claims) Act 1988 baseline** (`subjects/au/safety-rehabilitation-and-compensation-defence-related-claims-act-1988/encodings/baseline-2026-11/`): a compensation scheme whose reviewable decisions come to this Tribunal.
- **Administrative Decisions (Judicial Review) Act 1977** (`subjects/au/administrative-decisions-judicial-review-act-1977/`): the judicial review alternative.

## What would need doing before this is worth relying on

- **The Administrative Review Tribunal Rules** deposited, so the period to apply, fee deadlines and the excluded kinds can be worked out rather than asked.
- **The practice directions** (time for decisions, manner of application, document requirements).
- **The enabling Acts** whose own periods and modifications override the standard provisions (the Social Security (Administration) Act 1999, the Safety, Rehabilitation and Compensation Act 1988, the Veterans' Entitlements Act 1986, the Migration Act 1958 and others).
- **The transitional Acts** (the Administrative Review Tribunal (Consequential and Transitional Provisions No. 1 and No. 2) Acts 2024, deposited beside this subject) for matters begun in the Administrative Appeals Tribunal.
- **Case law.** No case was read. "Interests are affected", "question of law" and "reasonable in all the circumstances" are worked out by the courts; this encoding takes the text.
- An independent test pass and a human review.
