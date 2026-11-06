# Competition and Consumer Act 2010 — baseline encoding, the claimant's seat (defective goods, damages, Part VIB)

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `NOTHING` or a "not covered" constructor, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

This is a new layer beside the two existing encodings of this Act, which stay untouched: `baseline-2026-10` (the consumer's seat over Schedule 2: s 18, the consumer guarantees, unfair terms, unsolicited agreements, Part IVA) and `naive-2026-10`.
Neither covers what a person bringing a claim for injury or loss meets after the contravention: Part 3-5 of the Australian Consumer Law (manufacturers' liability for goods with safety defects), the s 236 action for damages and the s 237 compensation order, the Act's own limits on those (ss 137A-137C, 137E), and Part VIB (time limits and caps on personal injury damages).
No ledger entry asked for it; it was written as part of a run over the Acts behind personal injury, compensation and other claims, with the focus "the provisions a claimant meets".
Nothing is imported from the other encodings, and none of their names is reused.

Every question is a function named as the claimant would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are **34 exported questions**, grouped under `§§` headings in the order a claim meets them: who the manufacturer is; the manufacturer's liability (ss 138-141, with s 142 defences and s 146); defective goods actions (time, the unknown manufacturer, joint liability, the Commonwealth standard, the regulator, void terms); damages and compensation orders for a contravention; whether Part VIB reaches the claim; Part VIB time limits; Part VIB limits on non-economic loss; on lost earnings, care and superannuation; interest, exemplary damages and structured settlements. The Part VIB groups arise only for a person claiming personal injury or death damages; the heading of each says so.

**Regulative rule.** One, run inside a question that takes plain dates; no question takes a DEONTIC or an EVENT.

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `s 147 -- the supplier must name the manufacturer within 30 days` | the supplier | MUST give particulars WITHIN 30 (days from my written request); LEST BREACH BY the supplier BECAUSE … (the supplier is taken to be the manufacturer, s 147(2)) | `Is the supplier taken to be the manufacturer question` |

The case file asserts through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`) that the trace ends fulfilled or does not; the breach is also `#TRACE`d with an `-- expect:` line, since a breached trace cannot be compared with `EQUALS` on the stable `l4`.

**Dates.** `cca-claims-dates.l4` uses the built-in date functions only (no daydate). The periods ("within 3 years after", "6 years after the day", "12 years following", "within 10 years of") are counted with the Acts Interpretation Act 1901 (borrowed, not deposited): the day of the event is excluded (s 36(1)) and a year is 12 months (s 2G). The last day of 3 years after 10 March 2023 is 10 March 2026; a period starting on 29 February ends with February in a year that has none. Weekends and public holidays are not rolled forward (fork F6); every "By when" question says so.

## Edition

- **The Act:** Compilation No. 166, compilation date 27 August 2026 (includes amendments up to Act No. 76, 2026), register id C2026C00389, deposited at `../../registers/source-bundle/C2004A00109.txt`. The deposit's metadata warns that a version in force from 16 September 2026 had no registered compilation when fetched, so amendments from that date may be missing. Part VIB is at line 12547 of the deposit, ss 137A-137H at 16723, ACL s 7 at 24104, s 9 at 24124, Part 3-5 at 25851, ss 236-237 at 27191.
- **The formulas** of s 87M(1)(b) and s 87Z, lost in the text deposit, are taken from `../../registers/source-bundle/C2004A00109.formulas.md`.
- **The commencement of Part VIB** (for s 87M(1)(a)) is from the deposit's endnotes: Trade Practices Amendment (Personal Injuries and Death) Act (No. 2) 2004, No. 113, 2004, commenced 13 July 2004.
- **The Regulations:** the Competition and Consumer Regulations 2010 (Compilation No. 100, register id F2026C00856), deposited at `../../../competition-and-consumer-regulations-2010/registers/source-bundle/F1996B01420.txt`, were searched: they prescribe no discount rate (s 87Y), no interest rate (s 87ZA) and no substitute for average weekly earnings (s 87V(1)(b)). So the Act's own defaults apply: a 5% discount rate, and the 10-year benchmark bond rate.
- **Not deposited, so inputs:** the CPI index numbers (s 87N) and so the current maximum amount for non-economic loss (s 87M); average weekly earnings (s 87V); the bond rate itself; the superannuation guarantee charge percentage (Superannuation Guarantee (Administration) Act 1992 s 17A(2)).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cca-claims-dates.l4` | (exercised through the cases) | 0 errors, 0 warnings |
| `cca-claims.l4` | `cca-cases-claims.l4` | 179 written, 179 satisfied; 1 `#TRACE`, a BREACH as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Every expected value was written by hand from the text before the run. A three-value mutation of the case file (the s 87M rounding, the s 87K last day, the s 87R 32% row) was caught (176 of 179 satisfied), so the assertions are live.
Every exported question has cases, with the edges: the last day of each period and the day after (s 143 both limbs, s 236(2), s 237(3), s 87F); a period starting on 29 February and on 28 February of a leap year; day 30 and day 31 of s 147; death exactly 3 years after the deceased's date of discoverability and one day later (s 87G(6)(a)); an extension beyond and within the s 87H(2) cap; s 87J days; the s 87K 25th birthday; the s 87M $5 round-up and a round-down; severity at 14, 14.9, 15, 25, 28, 32, 33, 99 and 100 per cent; 5.5 and 6 hours, 5 and 6 months (s 87W, s 87X); 39, 40 and 60 hours of care; the bond-rate month on 28 February, 1 March, 31 August, 1 September.
Every `NOT` is parenthesised.

## Seat

**The claimant**: the individual injured by goods with a safety defect, or the person who suffers loss through another's injury or death or through damage to household goods or a home (ss 138-141), and the person who suffers loss because someone contravened Chapter 2 or 3 of the Australian Consumer Law and sues for damages (s 236) or applies for a compensation order (s 237). In s 87G(6) the seat is the personal representative bringing a deceased person's claim. The questions are the ones that person asks: "Is the manufacturer liable for my injuries?", "By when must I start?", "Is the supplier taken to be the manufacturer?", "Can I sue for the loss the breach caused me?", "Does Part VIB limit my claim?", "Is my claim out of time?", "What is the most for my pain and suffering?", "Can I get damages for the care my family gives me?".

The manufacturer, the supplier, the regulator, the Commonwealth and the court get no seat. What they must do is encoded as what it means for the claimant (s 147: the supplier taken to be the manufacturer; s 148: the Commonwealth pays instead; s 149: the regulator needs my written consent), and the court's judgments are inputs. A further seat for the manufacturer (its defences and its exposure) would fit the guide's "other seats" rule and is left for a later layer.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Regulations are deposited and were read; they set none of Part VIB's numbers, so the Act's defaults apply. The published indices are inputs (see Edition).
- **The actors the text names.** Followed: the manufacturer (and deemed manufacturers, s 7, s 147), the supplier, the injured individual, the person who suffers loss, the regulator, the Commonwealth, the court, the plaintiff, the personal representative, the capable parent or guardian.
- **A judgment handed to someone else is answered conditionally.** Followed. Inputs: whether goods have a safety defect (s 9(1): "not such as persons generally are entitled to expect"); whether a s 142 defence is established; the court's reduction for the claimant's share (ss 137A, 137B); when the cause of action accrued; the date the claimant "knows or ought to know" (s 87G); whether and to when the court extends the long stop (s 87H); the severity of non-economic loss as a percentage of a most extreme case (ss 87P-87S); the court's satisfaction under s 87W(2)(a)-(c).
- **The Act's own definitions worked out; borrowed terms asked.** Worked out: manufacturer (s 7, as far as its open list goes); defective goods action and the s 142 defence; proceeding to which Part VIB applies (s 87E with ss 137C, 137E); date of discoverability (s 87G(1), (4)-(6)); long-stop period (s 87H); maximum amount (s 87M); the caps of ss 87Q-87S, 87U, 87W, 87X, 87Z; the 10-year benchmark bond rate's month (s 87ZA(4)). Asked: "trade or commerce", "injuries", "involved", "incapacitated person" (a definition, but its facts are a judgment), workers' compensation law, the State dependency law of s 87X(2)(b), the superannuation charge percentage.
- **One case is the text's natural unit**: one claim about one injury, loss or contravention.
- **The Act's own terms**, quoted in the comment above each rule, with plain glosses in the `@desc`s.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The rulings, word for word as section 5 of `docs/ENCODING-GUIDE.md` records them: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit. Periods ruling: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`. Delegated definitions and defences: (b) "it is a defence ... to prove that X": when X is not proved, `JUST FALSE` for that provision's defence.

Applied here: `JUST FALSE` for s 143 and s 237(3) out of time (periods ruling (a)); s 149(2) without written consent ("may only"); s 150(2) a term neither express nor inconsistent ("is not taken to ... unless"); s 137E(1) ("must not make an order"); s 87W(2) not met ("must not ... except in accordance with this section"); s 87ZA(1) ("must not ... order the payment of interest"); s 87ZB(1) ("must not ... award"); and s 87F, where the question is "out of time?" and on or before the last day the Division's "must not award ... if" does not bite (`JUST FALSE`). The s 138-141 answers and the s 236 answer are enumerations that name the reason (a condition not met, s 146, s 142, s 137C). `NOTHING`: s 7 where no head holds (an open "includes" list); s 144 for one defendant and s 148 where its conditions fail (silent); s 87ZA for "another kind" of damages (the court decides whether interest is payable); s 87ZB for loss not in respect of death or injury, or a proceeding outside Part VIB ((2): unaffected); s 87ZC where Division 7 does not reach the claim; every Part VIB damages question where Part VIB does not apply in full; s 87G(6) where none of its limbs has yet happened.

Fork lines (case-by-case sites, for the reviewer to overrule):

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 143(2) "within 10 years of the supply" | `By when must I start my defective goods action question` | counted like "after": the day of supply excluded, last day the day before the tenth anniversary of the next day | the supply day counted as day one (one day earlier) |
| F2 | s 147(2)(b) "who did not comply with the request" | `Is the supplier taken to be the manufacturer question` | did not comply within the 30 days; a late answer does not undo the deeming | did not comply at all, so a late answer before trial undoes it |
| F3 | s 87K(1)(c), (d) "disregard any period before the victim turns 25 / before the victim's death" | `By when must I start my personal injury claim question` | counting starts on the 25th birthday (or the day of death), which is counted | counting starts the day after |
| F4 | s 87J "disregard any period during which" | same | the disregarded days, entered as a number, are added to each last day | the period is cut out of the running only if it falls inside the period (a day-by-day count) |
| F5 | s 87H(2) "not ... more than 3 years beyond the date of discoverability" | same | the extended long stop ends no later than the last day of 3 years after the date of discoverability, without s 87J or s 87K adjustments | the cap moves with those adjustments |
| F6 | Acts Interpretation Act s 36(2), a last day on a Saturday, Sunday or holiday | every "By when" question | the last day as counted, not moved; the descriptions point to s 36(2) | move a weekend last day to the Monday (holidays would still need a calendar) |
| F7 | s 87M(1)(a) "during the year in which this Part commences" | `What is the maximum for non-economic loss for the year question` | the calendar year 2004 | the 12 months from 13 July 2004, or the financial year |
| F8 | s 87R table, a severity between two rows (for example 20.5%) | `What is the most for my non-economic loss question` | `NOTHING` (not in the table) | the lower row |
| F9 | s 87ZA(4)(b) "the first business day of July in the preceding year" | `Which month's bond rate sets my interest question` | literal: a day from 1 September to 31 December takes July of the year before | July of the same year (see finding 1) |
| F10 | s 237(1) "Chapter 2, 3 or 4", for "another provision" | `Can I apply for a compensation order question` | `NOTHING` (a Chapter 4 offence is reached by s 237 but not listed here) | `JUST FALSE` |
| F11 | s 236(1) "a provision of Chapter 2 or 3", for Part 3-5 | `Can I recover my loss for the contravention question` | Part 3-5 counted as a Chapter 3 provision, as the text places it | excluded: Part 3-5 imposes liability, not a duty that can be contravened (see finding 8) |

## Scope

**In:** Schedule 2 (Australian Consumer Law) s 7 (manufacturer), s 9 (safety defect, as an input), ss 138-141, 142, 143, 144, 146, 147, 148, 149(2), 150, 236, 237(1)-(3); the Act's ss 137A, 137B, 137C, 137E; Part VIB ss 87D (definitions used), 87E, 87F, 87G, 87H, 87J, 87K, 87L, 87M, 87P, 87Q, 87R, 87S, 87U, 87W, 87X, 87Y, 87Z, 87ZA, 87ZB, 87ZC(1).

**Out, and why:**
- ACL s 18 and the consumer guarantees (ss 54-64A, 259-263): already encoded in `baseline-2026-10`, which stays.
- ACL s 138(3) and s 145 (death and survival under State and Territory law): they hand the claim to State law, which is not part of this Act; named in the descriptions.
- ACL Part 5-4 Division 2 (ss 271-277, actions against manufacturers for consumer guarantee failures): outside this focus; the Part VIB questions accept it as a Part the claim relates to. A later layer.
- ACL ss 238-243 (orders in other proceedings, non-party orders, the kinds of order): the court's powers; s 237 is the claimant's own route.
- The Act's s 137D (the court may consider post-contravention conduct), ss 137F, 137G (preservation orders on the Minister's or the Commission's application), s 137H (findings as evidence): the court's and the regulator's powers.
- Part VIA (proportionate liability, ss 87CB-87CI): it divides an economic-loss s 18 claim among concurrent wrongdoers; a claimant layer for it is possible and would sit beside this one.
- Part VIB s 87F(2) (a diagram), s 87N (index numbers: the CPI is an input), s 87T (earlier decisions: procedure), s 87V (average weekly earnings: an input), s 87ZC(2), (3).
- Machinery: jurisdiction (ss 86, 138-138D), commencement, regulation-making.

## What the Act turns out to say

1. **The bond-rate rule looks back further in late-year awards (s 87ZA(4)).** For a day from 1 March to 31 August the rate is January's of the same year; "otherwise" it is July's "in the preceding year". So damages determined on 31 August 2026 use January 2026's rate, but damages determined a day later use July 2025's, an older rate. July of the same year was probably meant for September to December. Encoded literally (fork F9). Asserted (1 September and 15 October 2026 give 1 July 2025).
2. **An extension of the long stop can never outrun the basic period (s 87H(2)).** The court "must not extend the period by more than 3 years beyond the date of discoverability", which is exactly when the basic 3-year period ends. An extension therefore only helps a claimant whose injury was discovered so late that the 12-year long stop ran out first, and at most it brings the long stop up to the basic period. Asserted (an extension to 1 January 2037 is cut to 1 March 2036).
3. **The s 87K rule moves both clocks.** For a child hurt by a parent, guardian or someone close to them, nothing before the victim turns 25 counts, for the 3-year period and the long stop alike: the claim runs until 3 years after the 25th birthday even when the injury was discovered in childhood. Asserted (14 May 2030 for a 25th birthday on 15 May 2027).
4. **Two clocks run on a defective goods injury claim.** Section 143 runs from awareness of the loss, the defect and the manufacturer's identity, with a 10-year limit from supply; Part VIB runs from the date of discoverability (which needs no knowledge of who made the goods) with a 12-year long stop from the act or omission. A claimant who knew of the injury but not the maker can be inside s 143 and outside s 87F. The two questions are asked separately; the descriptions say both apply.
5. **A relative's s 139 claim is cut for the injured person's own fault.** Section 137A(1) reduces a s 139 claim "having regard to that individual's share", the individual being the one injured, not the claimant. Encoded in the description of the s 137A question.
6. **The s 87R table has only whole percentages, and a step at 33%.** A severity of 32% gives 30% of the maximum; 33% gives 33%. A severity between rows is not in the table (fork F8). Asserted.
7. **Drafting slips with no effect on the answers.** Section 87W(3) joins its paragraphs with "or", s 87X(3) the same paragraphs with "and"; s 87X(4)(c), (d) speak of services that "were provided" where the subsection is about services the plaintiff "would have provided". Recorded.
8. **Section 236 and Part 3-5.** Part 3-5 sits in Chapter 3 but imposes liability rather than a duty that can be contravened, so a s 236 action "because of" a Part 3-5 contravention is hard to see; the defective goods action is the route. The encoding follows the text's placement (fork F11). Recorded.
9. **Personal injury from misleading conduct is shut out entirely, except tobacco.** Sections 137C and 137E bar both damages and compensation orders for death or personal injury from Part 2-1 or 3-1 contraventions, unless the injury results from tobacco, where Part VIB's time limits and structured settlements apply instead (and s 236(2)'s 6 years is overridden, per the note to s 137C(2)). Asserted.
10. **The non-economic loss maximum cannot be computed from the deposit.** It has been indexed every year since 2004 by the September CPI, which is not deposited. The question takes the year's maximum as an input, and a separate question does one year's indexation step. Recorded.

## Raised in the ledger

Nothing. The ledger `subjects/au/requirements.jsonl` was not changed. The published figures the Part VIB questions need (the current s 87M maximum, average weekly earnings, the bond rate) are statistics, not law, and are inputs.

## Before relying on it

An independent test pass; a lawyer's view of forks F1-F11; a holiday calendar for s 36(2); the current s 87M maximum from the CPI series; and the next layers (the manufacturer's seat, Part 5-4 Division 2, Part VIA).
