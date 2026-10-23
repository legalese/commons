# Fair Entitlements Guarantee Act 2012 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; the cases outside the encoding answer `not covered`, and tests assert them.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0066` in `subjects/au/requirements.jsonl` (priority 2, the 20 topics: losing a job). No scenario life raised it, so every case is hypothetical. There was no earlier encoding of this Act to keep.

**Added 23 October 2026 (REQ-0088):** `feg-maximum-weekly-wage.l4`, a module beside `feg-employee.l4` that IMPORTs it, works the maximum weekly wage out for a financial year under the deposited Fair Entitlements Guarantee (Indexation of Maximum Weekly Wage) Regulations 2023 and the Australian Statistician's estimates deposited beside them, and asks the advance question again with that figure in place of the input (two more exported questions; three in all). Nothing in `feg-employee.l4` was changed: its question with the maximum weekly wage as an input stays, for a year this module does not reach.

Every question is a function named as the former employee would ask it, with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order, so it can be deployed to Legalese Cloud.

## Edition

Compilation No. 5, compilation date 21 February 2025, includes amendments up to Act No. 14, 2025 (register id **C2025C00164**, Federal Register of Legislation, retrieved 22 September 2026), as deposited at `../../registers/source-bundle/C2012A00159.txt`.

`feg-maximum-weekly-wage.l4` also reads the **Fair Entitlements Guarantee (Indexation of Maximum Weekly Wage) Regulations 2023**, register id F2023L00381 (made 30 March 2023, commenced 31 March 2023, unamended; retrieved 23 October 2026), deposited at `../../../fair-entitlements-guarantee-indexation-of-maximum-weekly-wage-regulations-2023/registers/source-bundle/F2023L00381.txt`, and, beside it, the ABS *Average Weekly Earnings, Australia* releases for November 2021 to November 2025 (CC BY 4.0), whose full-time adult AWOTE figures the Regulations index by.

In `feg-employee.l4` the **maximum weekly wage** (s 5) is still an input: $2,364.00 in the Act "or the result of indexation ... in accordance with the regulations". The PAYG withholding s 24 deducts comes from the withholding schedules (not deposited) and is an input too.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `feg-employee.l4` | `feg-cases-employee.l4` | 70 written, 70 satisfied |
| `feg-maximum-weekly-wage.l4` | `feg-cases-maximum-weekly-wage.l4` | 17 written, 17 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The former employee of an insolvent or bankrupt employer**: "My employer went into liquidation owing me wages, leave and redundancy pay. Can I claim under the Fair Entitlements Guarantee, by when, and how much will I get?"

The Act is addressed almost entirely to the Secretary. Its provisions are encoded as what they mean for that person: when I am eligible (if the Secretary is satisfied of what I state), by when I must claim, what the Secretary must pay and may take off, where I can take the decision, and what I owe back if I am paid later from elsewhere.

No second seat. The Act puts no duty on the employer (which is insolvent) and none on the liquidator that the person can enforce under it; the Secretary is an official and gets no seat.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its number.** The indexation Regulations are brought in by `feg-maximum-weekly-wage.l4`; the PAYG amount is still an input.
- **The actors the text names:** me, my employer, the insolvency practitioner (liquidator, administrator, bankruptcy trustee), the Secretary, a transferee of the business, the Administrative Review Tribunal.
- **Judgments handed to others are answered conditionally.** Section 10 makes eligibility turn on what "the Secretary is satisfied" of; the answer is "eligible, if the Secretary is satisfied of the facts I have given". The Secretary's satisfaction under ss 12(1)(c) and 27(4), and the Secretary's discretionary reductions under ss 17 and 18, are inputs.
- **The Act's own definitions are worked out from facts:** wages (s 7), the wages entitlement period (s 5), insolvency event (s 5), the employment entitlements and their basic amounts (ss 6, 19 to 24, 26, 27). Borrowed terms are asked as facts: an "excluded employee" under Corporations Act s 556, "relative", permanent and special category visas, PAYG withholding.
- **One case:** one person's employment by one employer.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** ss 1–4, 8, 9, 9A, Part 4 payment mechanics, Part 5 Division 1 (the Commonwealth's recovery in the winding up), Part 6 Division 3 (information), ss 47, 48, 50 to 55.

## Scope

**In:** s 5 (insolvency event; wages entitlement period; maximum weekly wage as an input), s 6, s 7, s 10(1), s 11(1), (2), s 12(1), s 13, s 14(1)–(5), s 16(1)–(4), s 17, s 18, s 19, ss 20–24, s 26, s 27, s 34, s 36 (in comments), s 38(1), (2), s 40(1), s 41.

**Out:** employment for a partnership by two or more partners (ss 10(2), 11(3), 12(2), 25(3), 33) and an employer in administration under a Minister's s 49 declaration answer `not covered`. Section 25 (recently agreed changes in favour of the employee, which the Secretary may disregard): the person states the entitlement under the terms the Secretary applies. Costs of the winding up or bankruptcy (ss 20–23, 19(2)(c)): the person states each entitlement without them. Section 28 (to whom and in what instalments the advance is paid), ss 29–33, s 35, s 37 (the Secretary's own-initiative review), s 38(3)–(6), s 39, s 40(3), Part 6 Division 3, s 50 (contractor schemes by regulation).

## What the Act turns out to say

1. **An administration alone is not an insolvency event, but an administrator's appointment starts the 6-month window.** Section 10(1)(b) needs a liquidator's appointment or the employer's bankruptcy (s 5 "insolvency event"); a voluntary administration counts only through a s 49 declaration (not covered). But s 10(1)(c) asks about "the appointment of an insolvency practitioner", which includes an administrator, a receiver and a restructuring practitioner. So a job ended by the administrator is connected with the insolvency whatever the reason, once a liquidator follows. Asserted (Sam; "none of these").
2. **"Less than 6 months before" excludes exactly 6 months.** A job that ended on 10 September 2025 for some other reason, with the administrator appointed on 10 March 2026, is not connected; one that ended on 11 September 2025 is. Asserted.
3. **The 13-week wages entitlement period is counted here as 91 days ending on the earlier of the end of the job and the day a practitioner first had power to control employment.** Section 5 speaks of "the 13 weeks ending at the earlier of the following times"; the Act counts in times, the encoding in whole days, with the day of the event as the last. With the administrator in control from 10 March 2026, the period is 10 December 2025 to 10 March 2026, and wages for the last ten days of Sam's job fall outside it. An interpretive choice. Asserted.
4. **The claim must be made within 12 months after the later of the insolvency event and the end of the job (s 14(2)), and, for a bankrupt employer, before the discharge (s 14(3)).** The 12 months after 14 April 2026 end on 14 April 2027. "Before the discharge" is read as by the day before the day of discharge: an interpretive choice. A claim made after a GEERS claim for the same job is not effective, unless GEERS rejected it because the insolvency was before 5 December 2012 (s 14(4), (5)). Asserted.
5. **The maximum weekly wage caps leave, notice and redundancy pay by scaling the rate (s 26), and caps the limits in ss 22(b) and 23(b) too.** Section 26 works the basic amount out "as if the governing instrument had provided for the relevant wage rate to be the maximum weekly wage rate"; leave, notice and redundancy pay are weeks at a rate, so the entitlement is scaled by the ratio of the two rates, and the 5-week and 4-weeks-a-year limits use the capped rate (the s 26 Note). One weekly rate is asked for all four entitlements; where an award uses different rates for different entitlements the answer will differ. Asserted (the higher earner: $60,400).
6. **The redundancy limit is 4 weeks' pay for each year of service, not the National Employment Standards scale.** Section 23(b) limits the basic amount to 4 weeks' pay per full year of service for which the instrument requires redundancy pay, with a proportion for a part year only where the instrument pays for part years. An entitlement of 16 weeks for 3 years is limited to 12 weeks. Asserted.
7. **Tax is taken off the whole wages entitlement, so what was already paid must be counted after tax.** Section 24 takes from the wages entitlement "any amount required to be withheld" under PAYG "from the wages covered by the entitlement", and s 6(7) keeps wages already paid inside the entitlement; s 19(2) then takes off amounts "paid by anyone". Read literally with the gross amounts paid, tax on the weeks already paid would be taken off twice. This encoding asks for what was paid after tax (the amount that reached the person, the PAYG having been withheld separately), which gives back the unpaid wages less the tax on them. An interpretive choice, not tested against any decision. Asserted (Sam: $3,600).
8. **Section 27 caps wages three ways.** By a regular rate above the maximum weekly wage (s 27(2)); or, where no regular rate is set (s 27(3)) or the Secretary is satisfied there was no regular pattern (s 27(4)), by an average weekly wage above it, the average being the wages entitlement divided by the weeks employed in the period, "need not be a whole number" (s 27(5)). Asserted.
9. **The "offer of similar work" exclusion is closed for every insolvency from 1 July 2014.** Section 16(2) leaves notice and redundancy out where a transferee offers the same work within 14 days, but s 16(4) disapplies it for insolvency events on or after 1 July 2014, and s 16(3) undoes it if the transferee later makes the job redundant or becomes insolvent. Asserted.
10. **The reductions are the Secretary's, and one of them the Tribunal cannot touch.** Section 17 lets the Secretary reduce the advance by up to the person's debts to the employer; s 18 lets the Secretary reduce it to nil where the liquidator or trustee expects to pay in full within 112 days. Both are inputs. The Tribunal "cannot review the exercise of" the s 17 power (s 41), and it reviews only decisions that have been through the Secretary's review on application (s 40(1)), which must be sought within 28 days of the notice (s 38(2)). Asserted.
11. **A later payment from the liquidator creates no debt; one from anyone else does, capped at what is still unrecovered.** Section 34 makes the person owe the Commonwealth the lesser of the later amount and the advance less what the Commonwealth has recovered in the winding up and less earlier s 34 debts, but only where the later payer is not the Commonwealth, the liquidator or trustee, or the intermediary that paid the advance. Asserted.
12. **The ledger entry's question cannot be answered in dollars from the Act alone.** "How much will I get" turns on the maximum weekly wage as indexed under the Regulations and on the PAYG amount from the withholding schedules; the encoding computes the advance from both as inputs. A new ledger entry asks for the Regulations. Not asserted (a finding about the sources). Since 23 October 2026 the maximum weekly wage is worked out (findings 13 to 15).
13. **The indexation is in the 2023 Regulations, not the "Fair Entitlements Guarantee Regulations 2012".** REQ-0088 named the 2012 Regulations; on the Register they are repealed, and the indexation was in the Fair Entitlements Guarantee (Indexation of Maximum Weekly Wage) Regulation 2013, itself repealed by the Fair Entitlements Guarantee (Indexation of Maximum Weekly Wage) Regulations 2023. Section 6(2) of the 2023 Regulations fixes 2022-23 at $2,585; s 6(3) indexes each later year by the ratio of the last two AWOTE estimates published before 1 July, rounded to 3 places and never below 1, and rounds to the dollar. Section 7 saves the indexation done under the 2013 Regulation, so 2013-14 to 2021-22 answer `not covered` (that instrument is not deposited); 2012-13 is the Act's $2,364. Worked by hand: 2023-24 $2,673, 2024-25 $2,793, 2025-26 $2,921, 2026-27 $3,032. Asserted.
14. **The "seasonally adjusted" estimate the Regulations' notes point to is not seasonally adjusted.** Steps 1 and 2 take "the last assessment of current average weekly ordinary time earnings published by the Australian Statistician before 1 July"; the notes say the seasonally adjusted full-time adult figure. Each deposited release marks that row "(a) This component is not seasonally adjusted", repeating the original figure, so there is only one figure to take. The last estimate published before each 1 July is the previous November's, released in February (the May estimate comes in August). Not asserted (a finding about the sources).
15. **The cap is the rate "at the end of the employment".** Sections 26 and 27 apply the maximum weekly wage rate at the end of the employment (or of the wages entitlement period, which ends no later); the module takes the financial year in which the employment ended. An employment ending on 30 June 2026 is capped at $2,921, one ending on 1 July 2026 at $3,032. Asserted.

## What would need doing before this is worth relying on

- **The indexation for 2013-14 to 2021-22** (the repealed 2013 Regulation and its amendments, which paused indexation for some years), if an employment that ended then matters; and each February's AWOTE release, deposited, to carry the maximum weekly wage past 2026-27.
- **The PAYG withholding schedules**, so s 24's deduction can be computed rather than asked.
- **Partnerships and s 49 administrations**, if a case needs them.
- **Wider sources.** No departmental guideline, AAT or ART decision or case law was read; findings 3, 4, 5 and 7 are interpretive choices.
