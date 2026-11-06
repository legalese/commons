# Civil Liability Act 2002 (WA) — baseline-2026-11: child sexual abuse actions, dust diseases, the CISS and structured settlements

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. Checked with the
stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

**A layer beside `baseline-2026-10`, not a replacement.** That encoding covers ss 3-13 (the reach of the Act, Part 1A's
liability rules and Part 2's thresholds and caps) and left out Part 2 Divisions 4 and 5, s 13A and Part 2A. This one
encodes those, for the claims they belong to: child sexual abuse actions against institutions, dust disease claims, and
claims by people in the catastrophic injuries support scheme. Nothing in `baseline-2026-10` was changed. The stable
`l4` resolves IMPORT only within a folder, so this encoding cannot call the earlier one; the s 3A Table is restated here
(`cla2-common.l4`) only so far as Divisions 3, 4 and 5 of Part 2 need it.

Every question is published with `@export` and a plain-words description, and every input carries an `@desc`.

## Edition

- **The Act:** the Civil Liability Act 2002 (No. 35 of 2002), compilation as deposited at
  `../../registers/source-bundle/mrdoc_49335.txt` (legislation.wa.gov.au mrdoc 49335, retrieved 7 September 2026). It
  carries Part 2A as inserted by the Civil Liability Legislation Amendment (Child Sexual Abuse Actions) Act 2018 (No. 3
  of 2018, in operation 1 July 2018), s 15L as amended by No. 9 of 2022, and Part 2 Division 5 as inserted by the Civil
  Liability Amendment (Provisional Damages for Dust Diseases) Act 2024 (No. 32 of 2024, in operation 1 December 2024).
  Both dates are from the compilation's own table.
- **No regulations.** No regulation under s 15G(5) (naming a successor institution) is deposited, and none sets a number
  these provisions use. Whether a regulation names a successor is asked as a fact. The costs determination in s 15L is
  made under another Act (Legal Profession Uniform Law Application Act 2022 s 133); its figure is an input.

## Checks

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `cla2-abuse-cases.l4` | 51 | 51 | 0 | 0 |
| `cla2-dust-cases.l4` | 46 | 46 | 0 | 0 |
| `cla2-care-cases.l4` | 25 | 25 | 0 | 0 |

`l4 run` on each module (`cla2-common.l4`, `cla2-abuse.l4`, `cla2-dust.l4`, `cla2-care.l4`) succeeds with no
diagnostics. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A negative control (three
expected values altered in a copy of `cla2-abuse-cases.l4`) gave three "assertion failed". Expected values were worked
by hand from the text.

## Seat

**The individual bringing the claim:**

- in Part 2A, the person who was sexually abused as a child and sues, or may sue, the institution or its office
  holder: "Whom can I sue?", "Can my judgment be paid from the institution's trusts?", "How much of my redress payment
  comes off?", "Is my fee agreement void?";
- in Division 5, the person with a dust disease who sues for it: "Is mine a dust disease?", "Can I be awarded
  provisional damages?", "Can I sue again when I develop the later disease?";
- in s 13A and Division 4, the injured person: "Can I be paid for my care needs while I am in the CISS?", "Can the
  court approve instalments?".

The provisions speak mostly to the court ("may award", "must deduct", "must take into account") or to the institution
("may satisfy the liability"). Each is encoded as what it means for the claimant. No seat for the court, the Minister,
the institution, the insurer or the law practice.

Each 2026-10-18 default:

- **The Act alone, plus the instruments that set its numbers.** Followed. None is deposited or needed; see Edition.
- **The actors the text names.** Followed: the person abused, the institution, the office holder and the current
  office holder, the head of the institution, the trustee, the plaintiff and defendant, the Court (the Supreme Court,
  s 15AA), the law practice, the CISS participant.
- **Judgments handed to others, asked as inputs.** Followed: whether an institution is "substantially the same"
  (s 15F(1)); whether the court is satisfied what share of a payment was for the abuse (s 15K(4)); whether the person
  could maintain the action against the office holder (s 15B(1)(f), s 15D(1)(e)). Every "may" of the court is answered
  as "can", never "will".
- **The Act's own definitions worked out from facts.** Followed for "institution" (s 15A), the continuity rules
  (ss 15F-15H), "compensation payment" (s 15K(1)), "dust disease" (s 15AB), "structured settlement" (s 14). Borrowed
  terms asked as facts: "child sexual abuse", "child sexual abuse action" and "child sexual abuse cause of action"
  (Limitation Act 2005 s 6A(1)); "costs determination", "law practice" (s 15L(1)); "lifetime participant", "interim
  participant", "motor vehicle injury", "workplace injury" (the Motor Vehicle and Workplace Accidents (Catastrophic
  Injuries) Act 2016).
- **One case is the text's natural unit.** One claim; one earlier payment for s 15K (several: add the deductions); one
  later disease for s 15AG.
- **The Act's terms, each with a plain gloss.** In the comments and the `@desc` lines.
- **Operative sections in, machinery out.** Followed. Out: s 15J (a Corporations Act s 5G declaration), s 15M (the
  Minister's review), the regulation-making power in s 15G(5)-(7) (kept only as a fact), s 15AH(3)-(7) (the court's
  suppression orders), s 15AI (evidence), s 15AN (costs), s 15AD (finding 9).

## Scope

In:

- **Part 2A** (ss 15A-15L): who can be sued when the institution was unincorporated (ss 15A, 15B, 15D, 15F-15I), what a
  judgment or settlement can be paid from (ss 15C, 15E), the deduction of earlier redress payments (s 15K), the cap on
  legal fees (s 15L).
- **Part 2 Division 5** (ss 15AA-15AO): dust disease (s 15AB), provisional damages and the transitional amendment
  (ss 15AC, 15AO), subsequent actions (ss 15AG, 15AJ), settlement agreements and their consequences (ss 15AE, 15AF,
  15AL, 15AM), earlier amounts to be taken into account (s 15AK).
- **s 13A** (CISS) and **Part 2 Division 4** (ss 14, 15, structured settlements).
- **s 3A**, so far as it takes Divisions 3, 4 and 5 away, and **s 6(4)** (Part 2's start date).

Out, and why:

- Everything `baseline-2026-10` encodes (ss 3-13): it stays the encoding of those.
- Parts 1B-1F and Part 1A Division 7: defendants' protections and narrower claims, not this focus.
- Part 3 (advertising and touting): addressed to lawyers and touts, not the claimant.
- The machinery listed above.
- **The time limit for a child sexual abuse action** is in the Limitation Act 2005 (s 6A and the removal of the
  limitation period), not this Act; it belongs in that Act's encoding.

## Exported questions

`cla2-abuse.l4`:
`Whom can I sue for abuse in an institution that was unincorporated`,
`Can my judgment or settlement be paid from the institution's assets and trusts`,
`Can the office holder's personal assets be used to pay me`,
`How much of an earlier payment is deducted from my damages`,
`How much will I be awarded after the deduction`,
`Is my fee agreement void`,
`How much of my legal fees can I get back`.

`cla2-dust.l4`:
`Is my condition a dust disease`,
`Can I be awarded provisional damages`,
`Can I bring a subsequent action for a later dust disease`,
`Does my settlement agreement say what the Act requires`,
`What happens to my settled dust disease action`,
`What earlier amounts count against my subsequent damages`.

`cla2-care.l4`:
`Can I be awarded damages for my care needs in the CISS`,
`Can the court approve my structured settlement`.

No exported question takes a DEONTIC or EVENT input. None of these provisions sets a duty with a deadline on the
claimant, so no regulative rule is written: s 15L(2) ("An agreement must not be made") has no deadline and is encoded
as its consequence, a void agreement.

## Rulings on negatives and legal effects (2026-11-04/05), as applied here

The rows follow the corpus rule: `JUST FALSE` only where the text says no in its own words; `NOTHING` where it is silent
or the case is outside its scope. As applied:

- "means" definitions (s 15A institution, s 15AB dust disease, s 15K(1) compensation payment): `JUST FALSE` / `JUST 0`.
- "can only be awarded if" (s 15AC(2)), "must be in respect of", "cannot", "is barred" (s 15AG): `JUST FALSE`.
- "No damages can be awarded" (s 13A(5), (8)), "cannot be used" (s 15C(3)): `JUST FALSE`.
- "This section does not apply" (ss 15C(7), 15E(5)) and the s 3A Table's "do not apply": `NOTHING` (the general law
  decides).
- A scope with no "only" (s 15AC for a condition that is not a dust disease; s 13A for a need that arose before
  participation): `NOTHING`.

### Fork register (questions with no convention, decided case by case)

- **F1** s 15B, `Whom can I sue …`: where the office holder still holds the office, the answer is "Part 2A is not
  needed", not "no one". Other reading: report only that s 15B gives nothing.
- **F2** s 15G, `it is the relevant successor`: a regulation naming a different successor is read to displace a
  successor by merger or remainder (s 15G(7)(a), one successor). Other reading: two institutions can each be a
  relevant successor.
- **F3** s 15AO, `Can I be awarded provisional damages`: an action started before 1 December 2024 and amended under
  s 15AO(2) is read as meeting s 15AC(2), wherever it was started (s 15AO(4) transfers it). Other reading: s 15AC(2)'s
  "commenced in the Court by ... writ" still bites, so only a writ in the Supreme Court qualifies.
- **F4** s 15AG(6)(a), `Can I bring a subsequent action …`: a settlement that bars a subsequent action for one disease
  is read to bar only that disease, matching s 15AE(c)'s "in relation to a subsequent dust disease". Other reading: any
  bar in the agreement bars every subsequent action.
- **F5** s 15K, `How much will I be awarded after the deduction`: a deduction larger than the damages gives 0, never a
  debt. Other reading: none plausible; the text is silent.
- **F6** ss 15AE(c), 15AL(c), `Does my settlement agreement say …`: the statement about a bar is required only where the
  agreement lists a later disease. Other reading: the agreement must always say whether the plaintiff is barred.

## What the Act turns out to say

1. **"Part 2N" is Part 2A.** The child sexual abuse provisions are Part 2A, "Child sexual abuse actions" (ss 15A-15M),
   and s 8 makes Part 2A the one Part of the Act that can create or confer a cause of action. Not asserted.
2. **Part 2A reaches every class of claim.** It is in no item's third column of the s 3A Table, so it applies to a
   sexual-offence claim even though item 1 takes Parts 1A and 2 away from it. Not asserted (no input could change it).
3. **Accrual is always the time of the abuse** for Part 2A's purposes (s 15I), so "at the time of the accrual" in
   ss 15B(1)(c) and 15D(1)(c) asks about the institution at the time of the abuse. Built into the inputs.
4. **An incorporated institution is liable even while the office holder is still there.** s 15D, unlike s 15B, has no
   "no longer holds the office" limb. Asserted.
5. **The 50% rule.** If the court is not satisfied what part of a redress payment was for the abuse sued on, half the
   payment comes off (s 15K(4)); a judgment or settlement of an earlier action is not a "compensation payment" at all
   (s 15K(1)(b)) and is left to the court (s 15K(5)). Asserted.
6. **A void fee agreement returns everything paid**, not only the excess over the costs determination (s 15L(3)), save
   money for services before 1 July 2018 (s 15L(4)). s 15L(3)(b) catches pre-2018 agreements by asking whether they
   "would have been contrary ... if made after" 1 July 2018; which determination that test uses is not said. Asserted
   for the amount; the pre-2018 test is not.
7. **A gap in s 15AF.** An initial action settled by an agreement that bars some of the writ's later diseases but leaves
   none it lists open falls under neither s 15AF(1) (discontinued) nor (2) (dismissed). Asserted as "the Act does not
   say".
8. **s 15AK says "take into account", not "deduct".** Earlier provisional damages, subsequent damages and settlement
   receipts must be weighed, but the Act does not say they are subtracted. The question returns their total only.
   Asserted.
9. **s 15AD is a direction to the court** ("must not assume that the plaintiff will develop a subsequent dust disease");
   no fact of the claimant's changes it, so it is not a question. Not asserted.
10. **Division 5 has no start-date limit for dust claims.** s 6(4) confines Part 2 to incidents after it commenced. But
    s 6 is in Part 2 Division 1, and items 3 and 6 of the s 3A Table take away all of Part 2 except s 10A and Divisions
    4 and 5. So for asbestos and silica claims s 6(4) does not apply, and provisional damages reach exposure from any
    date, as the s 15AO transitional rules assume. The same holds for Division 4 under items 2, 3, 4 and 6. Asserted
    (structured settlements with no s 6(4) date; dust cases take no date). `baseline-2026-10` applies the s 6(4) date
    before the class for its own questions; for its outputs (Part 2's limits off either way) that makes no difference.
11. **Division 5 is off for a dust claim that is also a CTP, tobacco, aviation or intentional-harm claim** (items 1, 2, 4,
    5 keep no Division 5). Asserted.
12. **s 13A bites only outside CTP and employer claims** (the baseline-2026-10 finding 3, confirmed): every s 3A item
    takes Division 3 away. It reaches, for example, a workplace injury claimed against a third party. Asserted.
13. **An interim participant is barred for future needs too** (s 13A(6)); one who leaves the scheme as an interim
    participant is barred only for the interim period (s 13A(8)). Asserted.

## What would need doing before this is worth relying on

- Encode the Limitation Act 2005 s 6A and the child sexual abuse limitation rules, which decide whether the claim can be
  brought at all, and the Law Reform (Contributory Negligence and Tortfeasors' Contribution) Act 1947 s 7, which
  ss 15B(5) and 15D(5) bring in.
- Search for any regulation under s 15G(5) naming successor institutions, and for the costs determination in force.
- A lawyer's reading of forks F1-F6 and findings 6, 7 and 10.
- Check the deposited text against the current compilation: it was retrieved on 7 September 2026.
