# Workers' Compensation and Rehabilitation Regulation 2025 (Qld): baseline encoding for the injured worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
The focus was the provisions a person bringing or answering a workers' compensation or work-injury damages claim meets.
There is no REFUSE in it. Out-of-scope inputs answer `NOTHING` (or a named "does not apply" value), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`wcrr-core.l4`**, the seat-neutral core, in the Regulation's own actors and terms ("the worker", "the claimant", "the applicant", "the insurer", "the registered person", "the panel", "the court"). The tables (schedules 2-8, 17 and the s 187 and s 190 tables) are lists transcribed from the text. Where the text sets a deadline on someone, there is a regulative rule (`DEONTIC`): 4 in all (s 115(4); s 130; ss 131-132; ss 136-137).
- **`wcrr-seat.l4`**, the injured worker's seat. It asks 49 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Regulation's order. Groups that arise only in a situation (section 193A compensation, pneumoconiosis, a serious personal injury, a damages claim, a costs hearing) say so in a comment under the heading. It restates no rule.

This is the first encoding of the Regulation. The Act's own encoding (`../../../workers-compensation-and-rehabilitation-act-2003/encodings/baseline-2026-10/`) already uses Regulation ss 15, 105-110, 117-121, 147, 209 and schedules 3, 4 and 8 inside its own modules. It is untouched; this encoding is a separate layer beside it in the Regulation's own subject. Where both answer the same question, the figures differ only by the Act's s 205 rounding (finding 9).

Queensland keeps no requirement ledger and no scenario life raises this Regulation, so no ledger line is closed and no life event is cited.

## Edition

- **The Regulation:** Workers' Compensation and Rehabilitation Regulation 2025 (sl-2025-0116), the version in force from 1 September 2025 and current on 20 October 2026, as deposited at `../../registers/source-bundle/sl-2025-0116.txt` (retrieved 20 October 2026; converted from the HTML view, so not the authorised version).
- **QOTE:** the Workers' Compensation and Rehabilitation (QOTE) Notice 2026 (sl-2026-0044), deposited in its own subject: QOTE for 2026-27 is **$1,994.50** (s 3(1)). It is built in for days from 1 July 2026 to 30 June 2027. For an earlier year the person gives the figure; without it, and for any later day, an amount stated "times QOTE" answers `NOTHING`.
- **Borrowed from the Act** (act-2003-027): s 140's 216.15 times QOTE as the maximum statutory compensation for s 117, and the Act's tests in ss 36EB-36ED (first responders, eligible employees, the PTSD presumption), s 306M(1) and s 306R(2), each as plain facts or a fixed figure, with the section quoted in the core.
- **Commonwealth figure:** the carer pension rate (the weekly maximum carer payment) is an input.

The licence is CC BY 4.0, State of Queensland; the attribution is in `SOURCE-LICENSE.md` (a copy of the subject's). No deposited text was altered.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wcrr-core.l4`, `wcrr-seat.l4` | `wcrr-cases.l4` | 243 written, 243 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (7 November 2026). `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. In addition, 3 `#TRACE`s carry an `-- expect:` line, and each ends in the breach expected: by the registered person (s 115(4)), and twice by the insurer (s 130(3), s 132(3)). Every regulative rule also has at least one `EVALTRACE` asserted `FULFILLED`, including the paths where the worker does nothing and nobody is in breach.

Every expected value was worked by hand from the text, with the arithmetic in the comment above the assertion. The weekday of each date used was checked against a calendar. The edges tested are: the last day of 2026-27; each schedule's first and last rows and one past them; the "more than" and "or more" thresholds of ss 155-159 and 194; the last business day of each period; and the caps in ss 113, 196 and schedule 7.

## Seat

**The injured worker**, who is also the claimant. For the damages and costs questions the claimant may instead be a dependant of a worker who died. They ask: "What counts in my NWE?", "What can stand in for a medical certificate?", "What lump sums do my DPI, my age, my care needs and my pneumoconiosis give me?", "Am I entitled to section 193A compensation, and by when must I act?", "Does my injury meet the treatment, care and support criteria?", "What general damages does my ISV give?", "What legal costs can I recover?" and "Is my PTSD presumed to be a work injury?".

The insurer's, the examiner's and the court's duties are encoded as what the worker is owed and by when. No other seat is written. The insurer and the employer carry duties here (the s 193A decisions, the examination report, premiums), but the premium and self-insurance parts are out of scope, and the insurer's claims duties are few enough to stay inside the worker's questions.

The 2026-10-18 defaults:

- **The Regulation, with the instruments that set its numbers.** Followed: the QOTE Notice 2026.
- **The actors the text names.** Followed: the worker, the claimant, the applicant, the insurer, the registered person, the panel and the court.
- **A judgment handed to someone else answered conditionally.** Followed. These are inputs: the insurer's view that the NWE calculation is unfair (s 109); the insurer's satisfaction that the employer is liable (s 126); a FIM assessor's accreditation and approval (s 160); "equivalent" visual loss (s 159); the magistrate's or commission's satisfaction (s 191(3)); the court's ISV (s 189); and proof rebutting the PTSD presumption (Act s 36ED(4)).
- **The Regulation's own definitions worked out, borrowed terms asked.** Followed: consecutive categories, the pneumoconiosis score, the MBI ranges, net damages and the eligibility criteria are worked out. "Excluded treatment, care or support", "approved service", "relevant volunteer", and the Act's definition of wages, paragraphs (a)-(d), are asked as facts.
- **One case.** Followed: one worker, one injury or event, one claim.
- **The Regulation's terms, each with a plain gloss.** Followed: the core quotes the text above each rule, and the `@desc`s gloss DPI, NWE, QOTE, ISV, FIM and MBI.
- **Machinery out.** Followed (see Scope).
- **Departure (business days).** "Business day" is not defined in the Regulation, and the Acts Interpretation Act 1954 is not deposited. Deadlines count Monday to Friday, adding one business day for each Queensland public holiday that the person says falls on a weekday in the period.
- **Departure (s 117's maximum statutory compensation).** The person cannot state it, so it is computed as the Act's 216.15 times QOTE, not asked.

## Negatives and legal effects (rulings quoted)

The answers follow the conventions in `docs/ENCODING-GUIDE.md`, section 5. The two rulings relied on are quoted word for word:

- "**Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
- "**Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule".

Fork lines:

- **s 115(1)-(3)**, `the examination requirement is made as s 115 requires`: a bare "must" not done. The answer taken is FALSE ("not made as s 115 requires"). The other reading is that the requirement stands with a defect of form.
- **s 194(4)**, `the s 194 costs`: net damages of nil or less, which the text does not address. The answer taken is 0. The other reading is that (4) gives no amount at all.

The schedule scales answer `NOTHING` outside their range under ruling (c). These are a DPI under 30% for schedule 3, under 15% for schedule 4 and outside 1-5% for schedule 5; an MBI of 75 or more for schedule 4 and of 100 for schedule 8; and an injury before 1 July 2010 for the damages tables. Section 106 answers `NOTHING` where it is silent. Section 174 answers `NOTHING` where (3) does not oblige the insurer but (5) still lets it approve.

## Scope

**In:**

- s 15 (the excess period amount)
- ss 105-109 (NWE: what may be counted; comparable persons; concurrent employers; the insurer's fair calculation)
- ss 113-115 (a declaration or an out-of-State document in place of a medical certificate; the examination notice and the 10-day report)
- s 117 (lump sum by DPI); s 116 and schedule 2 (terminal latent onset injury); s 118 and schedule 3 (DPI of 30% or more); s 121 and schedule 4 (gratuitous care); s 119 as the MBI ranges
- ss 124-126, 130-132, 136-137 and schedule 5 (section 193A compensation: the qualifying condition, the amounts and the legal cost amounts, the worker's and the insurer's deadlines)
- ss 145-146 and schedules 6-7 (the pneumoconiosis score from 2, 3 or 5 readings; the lump sum and the lodgement age reduction)
- s 147 and schedule 8 (the caring allowance: maximum hours and the hourly rate)
- ss 153-160 (treatment, care and support: the eligibility criteria and the FIM assessor rule); s 173 (payment requests and the 6 months); s 174(2)-(5) (when the insurer must approve); s 176(2) (20 business days' notice of a review)
- s 185 (the time for adding a contributor); s 187 with Act s 306M(1) (loss of consortium or servitium); s 189 and schedule 17 (general damages, tables 1-10); s 190 with Act s 306R(2) (structured settlement notice)
- s 191(3) (costs up to 1.5 times scale C); ss 193-194 and schedule 9 (pre-proceeding legal costs); s 196(1)(d), (f) and (2) (the capped outlays)
- ss 206-208 and schedules 10-11, with Act ss 36EB-36ED (first responders, eligible employees, the PTSD presumption)

**Out, and why:**

- Part 1 and Part 2, divisions 1 and 3 (premiums, wage declarations, board as wages, instalments, self-insurance levies), Part 3 (actuarial calculations of self-insurer liability) and schedule 1 (additional premium): employer and insurer machinery that a claimant does not meet.
- ss 110-112 (the evidence that must accompany an application), ss 177-184 (the particulars in a notice of claim) and s 186 (contribution notice): checklists of content with no test or number. A form, not a rule.
- s 120 (the occupational therapist's report contents), ss 127-129, 133-135 and 138-144 (the content of notices, the meeting, the panel's procedure and constitution): process, except where they set the worker's or the insurer's deadlines, which are encoded.
- Part 5 (rehabilitation coordinators, scheme directions): employer duties.
- ss 161-172 (needs assessment and support plans) and s 175 (the payment limit, which points to the table of costs and Act ss 217, 218A): process and figures not deposited.
- s 195 (costs after a proceeding starts, by the court scale in the Uniform Civil Procedure Rules, not deposited), s 196(1) items other than (d) and (f) (no figures), and s 192 (additional costs, the Regulator's or insurer's discretion).
- Schedules 13-16 (the ranges of ISV and the PIRS): these are rules for the court's assessment. The ISV is an input.
- Part 10 (medical assessment tribunals), ss 209-213 and 215 (information statements, which the Act's encoding covers; designated courts and schedule 12; WorkCover funding; records; reasons), s 214 (witness allowances, by a District Court scale not deposited) and Part 12 (savings and transitional provisions): machinery.

## What the Regulation turns out to say

1. **Schedule 2's entry for age 74 is out of line.** The scale falls by about 21.61 times QOTE a year (216.15, 194.54, 172.92, 151.31 ...). At 74 it reads 126.69, a fall of 24.62, and the next fall, to 108.08 at 75, is 18.61. The two together (43.23) match two ordinary steps. So the entry reads like a slip for about 129.70. It is encoded as printed. Asserted.
2. **Schedule 7's age-reduction example does not follow its own rule.** Section 3(2) reduces the prescribed amount by "5% of the prescribed amount" for each whole year over 70. The example takes $149,365 at age 72 and reduces it "by $6,000 for each of the 2 years", giving $137,365. 5% of $149,365 is $7,468.25, so the rule gives $134,428.50. The rule is encoded. Asserted (both that the rule gives $134,428.50 and that it does not give $137,365). The $149,365 is 80.97 times about $1,844.70, an earlier year's QOTE, so the example probably dates from an earlier figure or rate.
3. **Schedule 6, s 5(4) has no rule for two "0" categories.** Under s 4(3)(a), two readings that are any mix of 0/-, 0/0 and 0/1 score 0. But where a third reading is needed and differs from both, s 5(4) settles only consecutive categories and categories A-C. So 0/0, 1/1 and then 0/1 cannot be scored under s 5 and need a fourth and fifth reading, although two of the three readings would have scored 0 between them under s 4. Asserted.
4. **Schedule 6, s 5(4)(a) does not say which pair to use when two pairs are consecutive.** With 2/1, 2/3 and then 2/2, both 2/1-2/2 (55) and 2/2-2/3 (60) are consecutive. READING: the higher pair's score, 60. Asserted.
5. **Which QOTE applies to "times QOTE" in the damages tables is not said.** Section 187 item 10, s 190 item 10 and schedule 17 table 10 apply to an injury "on or after 1 July 2020" and are stated "times QOTE". They do not say whether that is the QOTE at the injury, at the assessment or at the award. READING: the QOTE for the financial year of the day the person names (the assessment or the decision). The `@desc` says so.
6. **Section 187's and s 190's item 6 covers two years (1 July 2015 to 30 June 2017), and so does schedule 17's table 6.** This is as printed, and the encoding maps 2015-16 and 2016-17 to the same item. Tables 1-9 were checked: each item's base amount equals the previous item's base plus the band width times the previous rate, in every table.
7. **Section 196(1)(d) is ambiguous.** It allows "1 report fee of an expert investigating liability, of not more than $1,000, less any proportion of the fee agreed to be paid by the insurer". It can mean the fee capped at $1,000, less the insurer's share of the whole fee ($1,500 with half from the insurer: $250). It can also mean the worker's own share capped at $1,000 ($750). READING: the first, which follows the order of the words. Asserted.
8. **The scales list whole percentages only.** Schedule 3 lists each DPI from 30 to 74 and then "75-100". Schedule 4 uses bands ("15-39", "40-49", ...). Schedule 5 lists 1 to 5. A DPI that is not a whole percentage (30.5%) is in no row of schedules 3 and 5, and answers `NOTHING`. For schedule 4, a band is taken from its lower bound, so 39.5% goes to "15-39". The MBI ranges are treated the same way. Both readings matter only if a DPI or MBI score is ever fractional.
9. **Amounts here are unrounded; the Act's s 205 may round them.** The Regulation states amounts as multiples of QOTE. Act s 205 varies amounts under chapter 3, parts 6, 10 and 11 (among others) when QOTE varies, "rounded up to the nearest $5". The s 117 example uses a rounded maximum ($422,295). The Act's baseline reads s 205 as rounding the multiples, so its 2026-27 maximum is $431,115, where this encoding gives 216.15 × $1,994.50 = $431,111.175. A person reading both will see differences of under $5 per amount. The damages amounts (chapter 5) are outside s 205 in any case.
10. **Section 113's limit is per event, and none applies to a fatal injury.** A declaration "may be accepted ... only once for injury to the worker in any 1 event" and proves "not more than 3 days". Both limits are "for a non-fatal injury". A later event allows another declaration. Asserted.
11. **Section 132(3)(b)'s meeting window is read inclusively.** A s 133 meeting "within 60 business days after receiving the information" is taken to include a meeting on the 60th business day, which then extends the decision time to 10 business days after the meeting. Asserted.
12. **Section 176(2), "at least 20 business days before carrying out the review".** READING: 20 or more business days fall strictly between the day of the notice and the day of the review. Asserted at the edge.

## Before relying on it

- An independent test pass, and a check of every figure against the authorised PDF (the deposit is converted from HTML).
- A reviewer's ruling on the readings in findings 4, 5, 7 and 8, and on the two fork lines.
- If the Act's s 205 rounding is to apply to the schedule 2, 3, 4 and 7 amounts, apply it here as the Act's encoding does.
