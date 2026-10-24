# Safety, Rehabilitation and Compensation Act 1988 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; an employer outside the Comcare scheme answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0068` in `subjects/au/requirements.jsonl` (priority 2, the 20 topics: work injury and workplace safety). No scenario life raised it, so every case is hypothetical. There was no earlier encoding of this Act to keep.

## Edition

Compilation No. 82, compilation date 1 July 2026, includes amendments up to Act No. 17, 2025 (register id **C2026C00285**, Federal Register of Legislation, retrieved 22 September 2026), as deposited at `../../registers/source-bundle/C2004A03668.txt`.

The formulas the deposit lost are taken from the sidecar `../../registers/source-bundle/C2004A03668.formulas.md` (transcribed 2026-10-24 from the authorised Word rendering of the same compilation, each checked against its equation image), used by `src-formulas.l4` (added 2026-10-24).

Nothing else is brought in. The approved Guide to the Assessment of the Degree of Permanent Impairment (s 28), the Minister's travel rate (s 16(6)) and the Regulations are not deposited. The CPI- and WPI-indexed amounts (ss 13, 13AA) are inputs.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `src-employee.l4` (11 questions) | `src-cases-employee.l4` | 60 written, 60 satisfied |
| `src-formulas.l4` (5 questions, imports `src-employee`) | `src-cases-formulas.l4` | 38 written, 38 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-23; again 2026-10-24 with the formulas module, the 60 earlier assertions unchanged and still satisfied). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The injured employee** of the Commonwealth, a Commonwealth authority or a licensed corporation: "I was injured at work as a Commonwealth employee. Am I covered (Comcare), and what compensation, incapacity payments and medical costs do I get?" For compensation on death the question is the dependant's, asked about the employee.

Comcare (or the licensee) determines every claim. Its determinations are encoded for what they mean to the employee: whether it must find an injury, whether it is liable, which weekly rate applies, how much permanent impairment compensation follows from the percentage it determines, and how to challenge it.

No second seat. The employer's duties under this Act are rehabilitation duties in Part III (out of scope); the determining authority is an official or, for a licensee, acts as one.

The 2026-10-18 defaults:

- **The Act alone.** The approved Guide, the travel rate and the indexed amounts are not deposited; the percentages Comcare determines under the Guide and the indexed amounts are inputs.
- **The actors the text names:** the employee, the employer (the Commonwealth, a Commonwealth authority, a licensed corporation), Comcare and licensees as determining authorities, dependants, the Administrative Review Tribunal.
- **Judgments handed to others are answered conditionally:** whether employment contributed "to a significant degree" (s 5B), whether administrative action was reasonable (s 5A), serious and wilful misconduct and "serious and permanent impairment" (s 14(3)), the degree of impairment (s 24(5)), whether a late notice is excused (s 53(3)).
- **The Act's own definitions are worked out from facts:** employee (s 5), injury and disease (ss 5A, 5B), the s 6 circumstances, maximum rate compensation week and adjustment percentage (s 19), dependant (s 4). Borrowed terms are asked as facts: licensed corporation, pension age (Social Security Act 1991).
- **One case:** one employee and one injury.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Part VII (Comcare, the Commission), Part VIII (licences), Part X, ss 13 and 13AA as computations (their results are inputs).

## Scope

**Added 2026-10-24 (`src-formulas.l4`):** s 8(1), (2) (normal weekly earnings), s 16(6)(c) (the travel amount), s 19(2), (2B)–(2D), (3), (5)–(11) (the weekly amount, the split week, the 150% AWOTE cap, minimum earnings with the dependant additions), s 27 (non-economic loss), ss 13(4)–(6), 13AA(2)–(4) (one year's indexation of an amount). Still out: s 8(3)–(10), s 19(3A), (4) as a computation (what the employee is able to earn is Comcare's determination, an input), ss 20–22.

**In (2026-10-23):** ss 5(1) (employee), 5A, 5B, 6(1)(a)–(d), (1C), (3) and 6(1)(e)–(g) as one case, 14, 16(1), (2), (6) (eligibility only), (7), 17(2)–(4), 19(2), (2A), (3) (which rate, and the adjustment percentage), 23(1), (1A), (2), 24(1)–(9), 25(4), (5), 26(1), (2), 53(1), (3), 54(1)–(3), (5), 60(1), 62(3), 64(1).

**Out:** s 7 (diseases listed by the Minister); s 8 (normal weekly earnings: its formulas are lost, see finding 1); s 15; s 16 amounts; s 17(5) and s 18 amounts; s 19(2B)–(2D) (a week split at the 45-week mark), (3A)–(14) (superannuation, the 150% cap and minimum earnings, which act on the lost formula's result); ss 20 to 22, 23A, 25(1)–(3), 27 (non-economic loss: formula lost), 29, 29A, 30, 31; Part III (rehabilitation); Part IV (common law and third parties); ss 55 to 59; Part VI beyond ss 60, 62(3) and 64(1); Parts VII onwards; Defence service (s 4AA; the Military Rehabilitation and Compensation Act 2004 and the DRCA).

## What the Act turns out to say

1. **The deposit has lost the formulas that turn the rules into dollars.** Sections 8(1), (2), 16(6)(c), 19(2), (2C), (2D), (3), 27(2) and 13AA(3) each read "the formula: where:" with the definitions of the terms but no formula between. The encoding does not supply them from memory. It answers which weekly rate applies and the adjustment percentage (s 19(2A), (3)), not the weekly amount; and leaves out non-economic loss (s 27) and normal weekly earnings (s 8). A `C2004A03668.formulas.md` sidecar transcribed from the authorised rendering is needed (raised in the ledger). Not asserted (a finding about the deposit).
2. **A journey between home and the usual workplace is not covered by s 6 on its own.** Section 6(1C) deems that travel not to be at the employer's direction, so s 6(1)(d) does not reach it; the injury is covered only if it otherwise arose out of or in the course of employment. Asserted.
3. **A psychological condition that develops over time is a "disease", with a higher test.** Under s 5B the employment must have contributed "to a significant degree", defined as "substantially more than material" (s 5B(3)); and s 5A excludes anything resulting from reasonable administrative action taken in a reasonable manner, such as a reasonable performance appraisal. Asserted.
4. **The abnormal-risk exclusion is narrow.** Section 6(3) disapplies s 6(1) only for injuries at a place it refers to or in an ordinary recess; it does not reach an act of violence (s 6(1)(a)) or directed travel (s 6(1)(d)) in this encoding's reading. Asserted for the workplace and violence cases.
5. **Misconduct bars compensation unless the result is death or serious and permanent impairment; self-infliction always bars it.** Section 14(2), (3). Medical expenses are payable whether or not the injury causes death, incapacity or impairment (s 16(2)). Asserted.
6. **No claim counts without a medical certificate, except for medical expenses or a death.** Section 54(2)(b), (3); substantial compliance with the form is enough (s 54(5)), and a late notice is excused if the authority is not prejudiced or for a reasonable cause (s 53(3)). Asserted.
7. **The maximum rate lasts 45 weeks of normal hours, counted in hours, not weeks.** A week is a maximum rate compensation week while the hours lost "in that week and in all previous weeks" do not exceed 45 times the normal weekly hours (s 19(2A)); for a 38-hour employee that is 1,710 hours. After it, the adjustment percentage steps from 75% (not working) through 80%, 85%, 90% and 95% to 100% by the share of normal hours worked (s 19(3)); the bands' boundaries (25%, 50%, 75%) belong to the lower band. Asserted at each boundary.
8. **Weekly compensation stops at pension age, unless the injury came within the 2 years before it, when it runs for up to 104 weeks.** Section 23(1), (1A). Asserted.
9. **Permanent impairment compensation is a straight percentage of the maximum amount, with thresholds.** Nothing below 10% (other than hearing loss, and the loss of a finger, toe, taste or smell, which have no threshold), nothing for a binaural hearing loss below 5% (s 24(7), (7A), (8)); later increases count only if 10% or more (5% for hearing) (s 25(4), (5)); payment is due within 30 days of the assessment, with interest after (s 26). The $80,000 maximum is indexed each year by CPI under s 13; the encoding takes the figure in force as an input. Asserted.
10. **The death lump sum is all or a determined share.** Where any dependant was wholly dependent, the full s 17(3) amount ($400,000 printed, indexed by the Wage Price Index under s 13AA) is payable for all dependants; where only partly dependent dependants are left, Comcare determines an amount up to it; where there are none, only medical and funeral costs. Asserted.
11. **The Tribunal reviews only a reconsidered decision.** A reviewable decision is one made under s 62 (or s 38(4)) (s 60(1)), and s 64(3) excludes any other application; reconsideration must be asked within 30 days after the determination first came to the person's notice (s 62(3)). Asserted.

12. **The formulas are now in, from the sidecar (2026-10-24).** Finding 1 is answered for ss 8(1), (2), 16(6)(c), 19(2), (2C), (2D), (3), 27(2) and 13AA(3): `src-formulas.l4` computes normal weekly earnings ((NH × RP) + A, plus NH × OR for regular overtime), the travel amount, the weekly amount and non-economic loss in dollars. No earlier case supplied a dollar amount that a formula now produces (the earlier cases asserted the rate and the adjustment percentage, which the new module reuses), so there is nothing to compare. Asserted.
13. **The 150% AWOTE cap and the minimum earnings act only on the s 19(3) amount, and the minimum only in a week the employee is not employed.** Section 19(5) caps "an amount of compensation calculated under subsection (3)"; (6) raises only "an amount ... calculated under paragraph (3)(a)". A maximum rate week is uncapped, and a reduced rate week with any employment is not raised to the minimum however low it is. Asserted.
14. **The dependant additions have a quirk at (10) and (11).** A dependent child of 16 or more is a prescribed person as well as a prescribed child. If it is the only prescribed person, (10) removes its $25 and the $50 is added for it; if two or more such children depend on the employee, (11) puts one of them under (8) whether or not a spouse is also dependent, so that child earns no $25. With a spouse and a single child of 16 or more, neither applies and both $50 and $25 are added. Encoded literally. Asserted.
15. **A negative result is read as nil.** Where AE exceeds NWE (or the percentage of it), each formula goes below zero; the Act says nothing of a negative amount, and the encoding returns 0 (an INFERENCE). Asserted.
16. **X in the split week is an inference where the incapacity is partial.** Section 19(2C) defines X by the normal hours of the week that "elapse before" the 45-week total is passed. With the employee's inputs (hours prevented before and during the week) the encoding takes the week's prevented hours as spread evenly across its normal hours, so X = NWH × (hours left ÷ hours prevented this week); in a week of total incapacity this is exactly the hours left. The "reduced rate compensation entitlement" of s 19(2D) is read as the s 19(3) amount after the (5) cap and (6) minimum. Both INFERENCES. Asserted.
17. **"Calculated to 3 decimal places" is read as truncation**, so that the s 13(6) and s 13AA(4) increase of 0.001 when the fourth place is over 4 completes a round-half-up. Indexation substitutes an amount only when the factor is greater than one, and applies it to the last substituted amount; no rounding of the dollar amount is prescribed. Asserted. The amounts in force cannot yet be computed without inputs: no CPI or WPI index numbers are deposited, and amending Acts reset several bases (REQ-0101, left open).

## What would need doing before this is worth relying on

- **The indexed amounts** in force each year (s 24(9), s 17, s 18, s 19(7)–(9), s 27(2)): deposit the ABS December-quarter CPI and WPI index numbers and the amending Acts' application provisions that reset the bases (REQ-0101); `src-formulas.l4` then computes each year's amount. The approved Guide's percentages for a real assessment.
- **The Minister's rate per kilometre** (s 16(6)) and the published AWOTE (s 19(5)), now inputs.
- **Part III (rehabilitation)**, which carries the employer's duties and the suspension of compensation for refusing a program.
- **Wider sources.** No Comcare guidance, AAT or ART decision or case law was read; finding 4 is an interpretive choice.
