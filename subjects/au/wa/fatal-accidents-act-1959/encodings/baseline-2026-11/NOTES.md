# Fatal Accidents Act 1959 (WA) — baseline encoding, the relative's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind compensation and other civil claims. The Act is short, so it is encoded whole (bar machinery). There was no earlier encoding of this Act to keep. No ledger entry was open for it.

There are 12 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: am I a relative (Sch 2, s 3, s 6(3)); does the death give a claim (s 4); can a claim be made for my benefit (ss 4, 6(1A), Sch 2 together); who brings the action and can I bring it myself (ss 6(1B), 7, 9); what I must tell the defendant (s 8); can I be added, can I be separately represented (s 9A — arises only once an action is brought without naming me); medical and funeral expenses (s 5(1)); benefits left out of the damages (s 5(2), (3)); how much there is to share and my share (s 6(4)); money paid into court (s 6(5)–(7) — arises only if the defendant pays money in).

**Regulative rule.** `s 9 -- the executor's 6 months, then mine`: `PARTY the executor or administrator DO bring the action WITHIN <days to the end of the 6 months> HENCE FULFILLED LEST PARTY I, a relative ... MAY bring the action`. `DO`, not `MUST`: s 6(1B) says who brings the action, and s 9(1) makes the executor's failure a hand-over to the relatives, not a breach. The seat question `Can I bring the action myself question` takes plain facts (dates, whether there is an executor, who has sued). The case file asserts through `CONSIDER EVALTRACE ... WHEN FULFILLED`: the executor suing on day 181 of 181 (fulfilled); suing on day 182 (not fulfilled: the relatives' permission is left open); the executor late and then a relative suing (fulfilled); a relative suing inside the executor's 6 months (not fulfilled). One residual is `#TRACE`d with an `-- expect:` line.

Date arithmetic is kept in one small module, `faa-dates.l4`, the only one that imports `daydate`.

## Edition

The compilation on the Western Australian Legislation website (mrdoc_49105), retrieved 7 September 2026, last amended by the Statutes (Repeals and Minor Amendments) Act 2011 s 5 (in operation 26 October 2011), as deposited at `../../registers/source-bundle/mrdoc_49105.txt`. The compilation lists the Assisted Reproductive Technology and Surrogacy Act 2025 Pt 17 Div 8 as an uncommenced amendment; its text is not deposited and it is not encoded (it may touch s 6(3a), which names the Artificial Conception Act 1985). No regulation sets a number or date this Act uses.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `faa-dates.l4`, `faa-relative.l4` | `faa-cases-relative.l4` | 96 written, 96 satisfied; 1 trace, as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. Edges asserted: a de facto relationship of exactly 2 years on the day of death and one day short; one that began on 29 February; the last day of the executor's 6 months and the day after; 6 months from 31 August ending on 28 February; a death on the day the Act came into operation; unrecovered costs equal to and above the damages.

## Seat

**The relative of the person who died**: the family member for whose benefit the action is brought (spouse, de facto partner, former partner owed maintenance, parent, grandparent, step parent, child, grandchild, stepchild, brother, sister, half-brother, half-sister, and anyone in loco parentis either way: Schedule 2). "My husband was killed at work. Can I claim? Who brings the claim? Can I bring it myself? Will his life insurance be taken off my damages?" A relative who is also the executor or administrator asks the same questions. The Act puts no duty on a defendant that a defendant's seat would need, so no second seat is written.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Law Reform (Miscellaneous Provisions) Act 1941, the Artificial Conception Act 1985, the pension Acts in s 5(2)(c), the Limitation Act 2005) are named, not encoded; whether a benefit is paid under one is asked as a fact.
- **The actors the text names:** the relative, the executor or administrator, the plaintiff, the defendant, the court, a judge.
- **Judgments handed to others are answered conditionally:** "wrongful act, neglect or default", "entitled ... to maintain an action", "reasonable" (s 4(2)), "the court is satisfied" (s 9A(1)), "sufficient" (s 6(7)), the court's shares (s 6(4)) are inputs.
- **The Act's own definitions are worked out from facts:** "relative" (Sch 2, every paragraph), with s 3(2), (4) and s 6(3), (3a); the 2 years of cl 1(a)(ii) from dates. "De facto relationship", "in loco parentis", "legally obliged" and "executor or administrator" are borrowed and asked.
- **One case:** one death.
- **The Act's own terms**, quoted in the comment above each rule, and glossed in the `@desc` lines.
- **Machinery out:** s 1.

## Scope

**In:** s 3(1) "relative", s 3(2)–(4); s 4(1), (2); s 5(1)–(3); s 6(1A), (1B), (2)–(7) and (3a); s 7, with compilation note 1 (the former s 7 for causes of action accrued before 15 November 2005, answered `not covered`); s 8; s 9(1), (2); s 9A(1), (2); s 11 (folded into the s 4 answer); Schedule 2 cl 1.

**Out, and why:** s 1 (short title); s 3(1) "court" (no answer turns on it); s 9A(3), (4) (the court's procedural orders, and saving its other powers: nothing a relative can state changes them); ss 2, 10 and Schedule 1 (omitted or deleted). The **time limit** for bringing the action is not in this Act; it is in the Limitation Act 2005 and is not encoded.

## Fork register (questions with no convention, decided case by case)

The 2026-11-04 and 2026-11-05 rulings were followed in choosing between "no" and `not covered`:

- Schedule 2 for a relationship it does not list (aunt, cousin, fiancé): "no" (a "means" definition).
- Schedule 2 cl 1(a)(ii), (d), (e), (g) when "immediately before the death", "at least 2 years" or "legally obliged" fails: "no" (the definition's own terms).
- s 6(3) when parentage was not admitted or established in time: "no" ("shall be recognized only if").
- s 3(2)(a) for the birth family of an adopted person: `not covered` (silent). The other reading: still related by birth, since s 3(2)(a) does not say the birth relationship ends.
- s 3(4) for a grandchild born after the death: `not covered`. The other reading: "no", since a person not yet born "was" not a grandchild at the death.
- s 4(2) when the deceased's time had run and none of (a)–(c) applies: "no: s 4(2) does not treat the deceased as entitled". The other reading: `not covered`, since s 4 does not itself say that an expired limitation period stops the deceased being "entitled to maintain an action".
- s 5(1) for other expenses, and for a death not after 8 October 1959: `not covered` (scope limits with no "only"). For expenses not incurred by the beneficiaries: "no" (an "if").
- s 5(2) for a benefit it does not list: `not covered` (the general law of damages decides). For (d) in an action finalised before 19 May 2008: "no" (s 5(3) "does not apply to").
- s 5(1) "after the coming into operation": a death on 8 October 1959 itself is taken as not after it.
- s 6(4) when unrecovered costs equal or exceed the damages: nothing to divide (0). The text does not say who bears the rest.
- s 6(7) when the plaintiff takes no issue, or the court finds the money not enough: "s 6(7) does not give the defendant the verdict" (a "where" and an "if").
- s 7 once any action has been brought: "no" (a flat negative), except where the executor's action came within the 6 months (answered "no need", because s 6(1A) makes it for all relatives).
- s 8 for a relative who is not the plaintiff: "nothing under s 8".
- s 9A(2) for a person for whose benefit no action was brought: `not covered`.
- s 9(1) "within 6 months after the death": the period ends on the same day number 6 months on, or the last day of a shorter month; the Interpretation Act 1984 rules on time are not encoded (for example a period ending on a day the court registry is closed).

## What the Act turns out to say

1. **A relative's action under s 9 is for the relatives who bring it, not for the whole family.** s 6(1A) says every action is for the benefit of the relatives, but s 9(2) says an action brought by relatives "shall be for the benefit of that or those persons", and s 7 then allows no second action. A relative left out must apply under s 9A(1), and the court must be satisfied the name "should have been" included. Asserted (s 7 answer; s 9A answers).
2. **An executor who sues late still shuts out the relatives.** s 9(1) lets relatives sue when the executor "does not bring an action ... within 6 months", but once the executor sues, even late, s 7 allows no other action. Asserted.
3. **A separated spouse counts; a de facto partner needs 2 years and must still be living together.** cl 1(a)(i) asks only whether the person was the spouse "immediately before the death"; cl 1(a)(ii) adds both living together then and 2 years on that basis. A former partner counts only if the deceased was legally obliged to support them (cl 1(g)). Asserted.
4. **Adoption is spoken of only from the adopters' side.** s 3(2)(a) treats an adopted person as the child of the adopters; the Act does not say whether the birth relationship survives. Answered `not covered`.
5. **s 3(4) reaches only "a child of the deceased person" born after the death.** A grandchild in the womb at the death is not mentioned. Answered `not covered`.
6. **s 6(3) still restricts relationships through an "illegitimate" child, although s 3(2)(b) treats an illegitimate person as the legitimate child of the parents.** The encoding applies s 6(3) as written, as the more specific rule for an action; how the two fit is for a court. s 6(3)(a) speaks of "the deceased parent", which reads naturally only when the parent in the relationship is the person killed; for a relationship traced through an unmarried parent who is not the deceased (a half-sister through an unacknowledged father), whose lifetime counts is not clear. The encoding asks whether parentage was admitted or established in "the lifetime s 6(3) requires".
7. **s 5(2)(c)(i), (ii) name Acts repealed decades ago** (the Repatriation Act 1920–1957 and the Social Services Consolidation Act 1947–1953), saved by "any Act ... amending or replacing any of those Acts". Whether today's veterans' and social security Acts "replace" them is a question of construction, asked as a fact. The deposited text runs the years together ("19201957", "19471953"): the dash was lost in conversion; the encoding writes them with a dash.
8. **s 4(2) treats a deceased whose own time had run as still entitled** only in its three circumstances; the Act does not otherwise say that the deceased's lapsed time defeats the family's action (fork above).
9. **The Act sets no time limit of its own.** Since 15 November 2005 the time limit is the Limitation Act 2005's; the former s 7 (which set one) continues for causes of action that accrued before then, and its text is not deposited.
10. **s 8 sets no time** for the particulars; the rules of court do.
11. **The Crown is bound** (s 11), so a death caused by a State agency's negligence gives the same action. Folded into the s 4 answer and asserted.

## Raised in the ledger

Nothing. No ledger entry named this Act, and no scenario life cites it.

## What would need doing before this is worth relying on

- **The Limitation Act 2005**, for the time to bring the action, and the former s 7 for deaths before 15 November 2005.
- **The Law Reform (Miscellaneous Provisions) Act 1941 s 4**, for the estate's own action that runs alongside this one (s 5(2)(d)).
- **The Adoption Act 1994 and the Artificial Conception Act 1985**, for the relationships s 3(2) and s 6(3a) leave to them; and the uncommenced 2025 amendments.
- **Case law** on what damages are "proportioned to the injury resulting from the death" (s 6(2)), on de facto relationships and on in loco parentis. None was read.
- An independent test pass and a human review.
