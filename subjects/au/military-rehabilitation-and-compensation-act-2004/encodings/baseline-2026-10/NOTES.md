# Military Rehabilitation and Compensation Act 2004 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a condition from before 1 July 2004 answers `not covered`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0071` in `subjects/au/requirements.jsonl` (priority 2, the 20 topics: pensions and retirement savings). No scenario life raised it, so every case is hypothetical. There was no earlier encoding of this Act to keep.

## Edition

Compilation No. 77, compilation date 29 September 2026, includes amendments up to Act No. 94, 2026 (register id **C2026C00443**, Federal Register of Legislation, retrieved 13 October 2026), as deposited at `../../registers/source-bundle/C2004A01285.txt`.

Nothing else is brought in. The Guide to Determining Impairment and Compensation (s 67), the Statements of Principles, the Defence Minister's determinations of warlike and non-warlike service, and the indexed s 74 maximum (s 404) are not deposited; they are inputs.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mrca-member.l4` (12 questions) | `mrca-cases-member.l4` | 47 written, 47 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The member or former member of the Australian Defence Force**: "I was injured or became ill in ADF service after 1 July 2004. Is my condition accepted, and what compensation, incapacity payments and permanent impairment payments do I get?"

The Military Rehabilitation and Compensation Commission determines everything. Its determinations and opinions are encoded as what they mean for the member: when it must accept liability, what standard of proof it must apply, when permanent impairment compensation is payable and what lump sum choices are open, which incapacity rate applies, and how to take a determination to the Veterans' Review Board and the Tribunal.

No second seat. The other parties the text names are the Commonwealth, the Commission, the Chief of the Defence Force and the Board, all officials.

The 2026-10-18 defaults:

- **The Act alone.** The Guide, the Statements of Principles and the indexed amounts are not deposited.
- **The actors the text names:** the member or former member, the Commission, the Chief of the Defence Force, the Veterans' Review Board, the Administrative Review Tribunal, a medical practitioner.
- **Judgments handed to others are answered conditionally:** the Commission's opinions under s 27(c) and (d), its satisfaction that an impairment is indefinite and stabilised (s 68), the impairment points under the Guide, serious default and "serious and permanent impairment" (s 32), the s 35 risk questions.
- **The Act's own definitions are worked out from facts:** service injury and disease (s 27), the exclusions (ss 32–36), the threshold (s 69), the lump sum bands (s 78), maximum rate week and adjustment percentage (ss 129, 131). Borrowed terms are asked as facts: the kind of service (the Defence Minister's determinations), pension age (Social Security Act 1991).
- **One case:** one person and one condition.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Chapter 10 (the Commission, the Board, the Repatriation Medical Authority), Chapter 11.

## Scope

**In:** ss 6(1A), (1) (kinds of service), 23(1), 27, 32(1), (2), 33(1), 34(1), 35(1)–(5), 36, 68(1), (3), 69, 74(1), 77(1), 78(1)–(4), 79(1), (2), 118(1), (2), 120, 121, 122, 129(2), 131(2)(a)–(f)(i), 319(2), (2A), 335(1)–(3), 345(1), 346(5), 352A, 352B(1), 354(1).

**Out:** conditions before 1 July 2004 (`not covered`); s 24 and Chapter 5 (service death and dependants); s 27A presumptions and the Statements of Principles (ss 338, 339); ss 23(2), (3), 29, 30 (treatment and signs and symptoms); ss 32(3)–(5), 33(2)–(3), 34(2)–(4) (aggravations, asked within the main exclusions); ss 70–72, 75 beyond its existence, 76, 80–83A; Chapter 3 (rehabilitation); Part 3 of Chapter 4 (incapacitated current members); s 130 (the week split at 45 weeks); s 131(2)(f)(ii), (3)–(6); Divisions 3 to 7 of Part 4 of Chapter 4 (normal and actual earnings); Part 6 (Special Rate Disability Pension); Chapter 6 (treatment); ss 320–343 beyond ss 319 and 335; ss 347–350 (reconsideration, except as a route to a reviewable determination); ss 352C onwards (Board procedure).

## What the Act turns out to say

1. **The deposit has lost the formulas for the money.** Sections 78(5) (the lump sum), 129(1), 130(2), (3) and 131(1) (weekly incapacity compensation) read "the following formula:" with nothing after. The encoding answers which incapacity rate applies and the adjustment percentage, and which lump sum percentages are open, not the dollar amounts. A `C2004A01285.formulas.md` sidecar is needed (raised in the ledger). Not asserted (a finding about the deposit).
2. **Two standards of proof, by kind of service.** For warlike, non-warlike (including peacekeeping), British nuclear test defence and hazardous service, the Commission must accept the connection unless satisfied beyond reasonable doubt that the material raises no reasonable hypothesis connecting the condition with the service (s 335(1), (2)); for peacetime service it must be reasonably satisfied (s 335(3)). Asserted.
3. **Peacetime commuting is covered, with travel exclusions.** Section 27(e) covers an accident on a journey to or from duty in peacetime service; s 35 takes out a substantial delay, an indirect route or a substantial interruption, unless for duty or the risk did not substantially change. Asserted.
4. **Serious default bars acceptance, except for serious and permanent impairment.** Section 32(1), with s 32(2) (alcohol or drugs not lawfully taken); s 33 (reasonable and appropriate counselling, or a missed promotion); s 34 (a wilful false statement about the condition); s 36 (tobacco after 1997). Asserted.
5. **The permanent impairment threshold is in impairment points: 5 for hearing, a finger or toe, taste or smell (from a single condition), 10 otherwise.** Section 69; points from more than one condition may be combined (note 1 to s 68(1)). Before the condition stabilises, interim compensation is available (s 75). Asserted.
6. **The weekly amount of permanent impairment compensation is the Guide's, not the Act's.** Section 74(1) caps it at $233.07 a week (indexed under s 404); s 74(2) leaves the amount to the Commission's assessment under the Guide (s 67), which is not deposited (raised in the ledger). Not asserted.
7. **Weekly permanent impairment compensation runs from the claim, or from the first of the month the condition stabilised.** The entitlement date is the later of the claim and the medically estimated date of stability and permanence (s 68(3)); if it is the claim, compensation runs from that day, otherwise from the first day of that calendar month (s 77(1)). Asserted.
8. **The lump sum choice depends on the weekly amount's share of the maximum.** 100% may always be converted; at 10% to 20% of the maximum, 50% too; above 20%, 25%, 50% or 75% too (s 78(1)); the choice is irrevocable, in writing, within 6 months of receiving the notice (s 78(2), (3)), and the lump sum is due within 30 days after the Commission learns of it, with interest after (s 79). Asserted, including the 20% boundary.
9. **Former members' incapacity compensation follows the Comcare pattern.** Maximum rate weeks while the hours lost total no more than 45 times normal weekly hours (s 129(2)), then 75% to 100% by hours worked (s 131(2)); none at pension age, except up to 104 weeks for a condition that began within 2 years before it (ss 120, 121); none in prison (s 122); the Special Rate Disability Pension, if chosen, instead (s 118(2)(a)). Asserted.
10. **The Veterans' Review Board comes before the Tribunal.** An application to the Board must be in writing within 12 months after notice of the original determination (s 352B(1)); only a reviewable determination, made on reconsideration or by the Board, goes to the Tribunal (ss 345(1), 354(1)). Asserted.
11. **The Act does not itself say which pre-2004 conditions it covers.** Sections 3 to 359 commenced on 1 July 2004 (s 2); what governs a condition from before then is in the Consequential and Transitional Provisions Act, which has a subject but no encoding (raised in the ledger). The encoding answers `not covered`. Asserted.
    **Update, 2026-10-23 (`REQ-0109`).** The Consequential and Transitional Provisions Act now has a baseline, `subjects/au/military-rehabilitation-and-compensation-consequential-and-transitional-provisions-act-2004/encodings/baseline-2026-10/`. Its `Which Act governs my claim question` answers the pre-2004 case for any claim made on or after 1 July 2026: the MRCA, "whether the injury is sustained ... before, on or after that date" (that Act's s 7(1), (2), as substituted by Act No. 17, 2025). This Act's own simplified outline (s 2) says the same: "From the date of commencement, the benefits and assistance provided for by this Act cover all members and former members, regardless of when they rendered service". So this finding's first sentence is too strong for the deposited compilation, and the `not covered` reason ("governed by the transitional provisions, the DRCA or the VEA") is out of date for new claims: it remains right only for a claim pending under the DRCA or VEA on 1 July 2026 (that Act's ss 88, 89) or decided before then. The code and its test are left unchanged, because IMPORT cannot reach the other folder and the answer would change this encoding's tests; the next revision should drop the `it began before 1 July 2004` input or ask instead whether the claim was made before 1 July 2026.

## What would need doing before this is worth relying on

- **The lost formulas** (ss 78(5), 129–131) and the earnings provisions they rest on.
- **The Guide to Determining Impairment and Compensation**, for the weekly permanent impairment amount.
- **The Statements of Principles** and the s 27A presumptions, which decide most liability claims in practice.
- **The Consequential and Transitional Provisions Act**, for conditions straddling 1 July 2004: encoded on 2026-10-23 (see finding 11's update); its answer still needs joining to this encoding's `not covered`. The **DRCA** and **VEA** for claims pending on 1 July 2026.
- **Chapter 5** (death and dependants) and **Part 6** (the Special Rate Disability Pension).
- **Wider sources.** No DVA guidance, Board or Tribunal decision or case law was read.

## The Guide to Determining Impairment and Compensation brought in (added 2026-10-24, REQ-0108)

**Module:** `mrca-guide.l4`, beside `mrca-member.l4`, which it imports (it reuses that module's `Kind of service` and its s 78 lump-sum question); cases in `mrca-cases-guide.l4` (19 written, 19 satisfied; `l4 run` 0 errors, 0 warnings; `mrca-cases-member.l4` still 47 of 47). Seat: the current or former member.

**Instrument:** the Guide to Determining Impairment and Compensation 2026 as made (F2026L00595, made 4 May 2026 under s 67(1)), deposited whole at `subjects/au/guide-to-determining-impairment-and-compensation-2026/` with `parent_act` this Act (about 396 000 characters of text; the 13.5 MB Word file is mostly images, which are not deposited). The one image formula used, Chapter 23's weighted average for mixed service, is transcribed in `F2026L00595.formulas.md`; the Guide's other image formulas (lung function, hearing, renal, Combined Values Chart) are listed there as not transcribed.

**What the module computes:** the compensation factor from Table 23.1 (warlike and non-warlike service) or Table 23.2 (every other service) for an impairment rating and a lifestyle rating; the weekly amount as factor × the s 74 maximum (an input, indexed under s 404); the weighted factor and amount for conditions from both kinds of service; and the s 78 lump-sum shares on that amount through the baseline's question. The impairment rating and the lifestyle rating themselves (Chapters 1–22) are inputs. Finding 6's weekly-amount input is no longer needed where the ratings are known.

12. **Two tables of 616 factors each turn points and lifestyle into a fraction of the maximum.** Rows are impairment ratings 0 and 5 to 80, columns lifestyle ratings 0 to 7; 80 or more points pays the full maximum whatever the lifestyle rating or service. The tables were transcribed from the deposited text by script and checked (77 rows each, every row and column non-decreasing) and against the Guide's own examples (15 points, lifestyle 1, non-warlike: 0.155; 44 and 42 points, lifestyle 4: 0.478/0.268 and 0.461/0.258). Hazardous service and British nuclear test defence service take the peacetime table, because s 67(2)(a) of the Act divides only "warlike service or non-warlike service" from "other". Asserted.
13. **The mixed-service formula does not round, but the Guide's example does.** CF = (A × CF^wl + B × CF^pt) / (A + B). For Warrant Officer Smith the formula gives 0.3798; the Guide prints 0.380 and $160.25 a week at $421.72, which is 0.380 × $421.72 rounded to cents. The module follows the formula (0.3798, $160.169256 a week) and does not round the amount; whether the Commission rounds the factor to three places is a practice the text does not state. Asserted on the formula.
14. **The tables stop at 5 points.** There are no rows for 1 to 4 impairment points (s 69's lowest threshold is 5), so the module returns no factor there; nor for a lifestyle rating outside 0 to 7. Asserted.
