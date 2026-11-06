# Workplace Injury Rehabilitation and Compensation Act 2013 (Vic): baseline encoding for the injured worker

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is the first encoding of this Act; nothing beside it was changed.
There is no REFUSE in it. A question the encoding cannot answer returns `NOTHING`, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Three modules:

- **`wirc-core.l4`**, seat-neutral: the date arithmetic (built-in date functions only, no daydate), the varied amounts for two years, and the rules of Parts 2, 3, 5 and 7 in scope, each with the section and the deposited line it comes from. Five duties with deadlines are regulative rules (`DEONTIC`): s 18 (notice of injury, and the employer's acknowledgement), s 75(1) with s 178(3) (decision on a weekly payments claim, deemed acceptance, payments to begin), s 165(3) (decision on a s 165 application), s 330 (advice on a serious injury application), s 335(2)(d) with s 337(1) (applying for leave, or for consent to apply late).
- **`wirc-seat.l4`**, the injured worker's seat: 29 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order. It builds the core's inputs from plain answers and restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`wirc-cases.l4`**, the cases: every exported question, with its edges, and every regulative rule by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

## Edition

**Workplace Injury Rehabilitation and Compensation Act 2013**, Act No. 67/2013, **Version No. 054, as at 2 October 2026**, deposited at `../../registers/source-bundle/workplace-injury-rehabilitation-and-compensation-act-2013.txt` (sha256 `b7b33dfc074ef55499d66fa194717105cbbfce50112275384a97c649366611ad`).
The Word file was saved by hand by the owner on 2026-11-06 from the version page and converted to text; `workplace-injury-rehabilitation-and-compensation-act-2013.meta.json` records the file, its hash and the conversion, and `subjects/au/vic/README.md` records the deposit. Line numbers in the modules are lines of that text.
The version includes the Workplace Injury Rehabilitation and Compensation Amendment (WorkCover Scheme Modernisation) Act 2024 (No. 8/2024; ss 4-26 in force 31 March 2024, endnote at line 10204): the new definition of mental injury and ss 39(1A), (2A), 40(1A), (2A), the substituted s 163(1), and the transitional s 625.

None of the 14 equations or 11 images in the `.formulas.md` sidecar is used. The sidecar's equations are the indexation formulas (ss 542-545), the enhancement formula (s 157), and formulas in sections out of scope. Flow chart 1 (s 15), the one image transcribed, is the notice of injury, and agrees with s 18 as encoded.

**The varied amounts.** The Act prints each dollar amount as it was first written. Division 1 of Part 13 (ss 542-547, lines 7709-7834) varies them every 1 July. The varied amounts are taken from the **Victoria Government Gazette No. S 363 of 30 June 2026**, deposited in `subjects/au/vic/workers-compensation-annual-indexation-notice/registers/source-bundle/GG2026S363.txt` (sha256 `04c8fe556bca3ef38185cf933965d9a6526da59cac06fb470eec02fe5945499a`), the 2013 Act notice at lines 389-733. IMPORT cannot reach another subject's folder, so 20 amounts are copied by hand into `wirc-core.l4`, each with its Gazette line and the Act's own figure. That notice has its own encoding (`workers-compensation-annual-indexation-notice/encodings/baseline-2026-10`), which is left as it is.
The notice's "Rate before 1 July 2026" is read as 1 July 2025 to 30 June 2026 and its "Rate from 1 July 2026" as 1 July 2026 to 30 June 2027, the reading of the notice's own encoding. A question that needs an amount answers `NOTHING` for a day outside those two years (asserted at both edges). The notice for 1 July 2027 should be deposited beside this one, and its figures added to `the varied amount`.
The day that picks the year is the one the Act names where it names one: the relevant date of s 210(1) for the impairment benefit, "the date of the award" for s 340, the financial year of the week for the s 161-165 cap (s 159), the day of the s 165 application for its minimum earnings. Where the Act names none (the death benefits), see finding 3.

## Checks

| Module | Assertions |
|---|---|
| `wirc-core.l4` | none (0 errors, 0 warnings) |
| `wirc-seat.l4` | none (0 errors, 0 warnings) |
| `wirc-cases.l4` | 192 written, 192 satisfied (0 errors, 0 warnings) |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-06). A copy of the case file with one expected value changed was run first, to confirm that a failure is reported; it was not kept.
Every expected value was worked by hand from the deposited text and the Gazette rows, with the arithmetic in the comment above the assertion. The edges asserted include: the 30th and 31st day for notice; 28 February for a 2-year or 6-month period from 29 February or 31 August; the last day for a decision and the day after; weeks 13, 14, 130 and 131; 20 and 21 per cent whole person impairment; 14 and 15 hours and $256 and $257 for s 165; 910 and 911 days before retirement age; 11, 12, 51 and 52 weeks for s 189; each band edge of s 211 (9, 10, 10.5, 11, 29, 30, 31, 70, 71, 79, 80, 85) and of s 212 (29, 30, 31, 81); the maximum and just over it; 1 to 6 dependent children; the s 340 thresholds and a dollar under; 24 December to 9 January in the s 329A count; 30 June 2025 and 1 July 2027 outside the figures.
Breached traces are asserted through a helper (`ends fulfilled`) and `NOT`, because `EVALTRACE ... EQUALS` cannot test a breach.

## Seat

**The injured worker** (`wirc-seat.l4`): a worker injured in employment connected with Victoria, and, under "If the worker dies", the worker's dependent partners, dependent children and close family members, who ask the death benefit questions.
*Am I entitled to compensation? By what day must I give notice? What follows from when I gave it? By what day must I claim? By what day must my claim be decided, is it taken to be accepted, and by when must payments begin? Can I get provisional payments for a mental injury, and until when? Which entitlement period am I in, and how much are my weekly payments? Do I meet the conditions to be paid after 130 weeks, not working or while working? Does my age limit my payments? How much notice must I get before they stop? From when, and on what day, can I claim an impairment benefit, and how much is it for a physical or a psychiatric impairment, and after the limit? What is my share of the death lump sum, and my grief and loss amount? From when can I apply on the ground of serious injury; by when must my application be answered; is my injury taken to be serious; by when must I apply for leave; do I meet the loss of earning capacity requirements; how much damages can I be awarded?*

No employer or insurer seat is written; the employer's duties (registers, forwarding claims, return to work) are out of scope. The Authority and self-insurers get no seat: their duties appear only as what the worker must be given, and by when.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Followed: the Gazette notice that varies the amounts is brought in (copied, see Edition). The Workplace Injury Rehabilitation and Compensation Regulations 2024 are deposited, but no rule encoded here reads a number from them.
- **The actors the text names.** Followed: the worker, the employer, "the Authority or self-insurer" (one party, as the Act pairs them), a court; dependants and close family members. The seat's `@desc` calls the Authority "WorkSafe (the Authority)" as a gloss.
- **A judgment handed to someone else answered conditionally.** Followed. "Reasonable" management action, events that "may be considered usual or typical", the s 163(1) and s 165(4) determinations, the waiver of time limits, the stabilising of an injury, the degree of impairment, and whether an injury is "serious" are facts the worker states, or the answer names what is left to the Authority or the court (s 18(7), s 325, s 335(2)).
- **Definitions worked out, borrowed terms asked.** The Act's own definitions in L4: severe injury (s 40(7)), the entitlement periods (s 152), close family member (s 237A(2)), relevant date (s 210(1)). Asked as facts: mental injury (s 3), current work capacity, pre-injury average weekly earnings (ss 153-158, worked out from a year of pay records), deductible amount, impairment benefit rating (s 210(2), which needs Schedule 3 and the A.M.A. Guides), dependent partner and child, orphan child, retirement age (pension age under the Social Security Act 1991 (Cth)).
- **One case.** One injury to one worker (or one death).
- **The Act's own terms with a plain gloss.** Followed.
- **Operative sections in; machinery out.** Followed: the Authority, Medical Panels, ACCS's procedure, premiums, self-insurers, regulation-making and the indexation arithmetic are out.

## Scope

**In** (the focus: claims, weekly payments and step-downs, the second-entitlement test, impairment and death benefits, Part 7 common law and the serious injury gateway, mental injury, with the 2024 amendments):

- **Entitlement:** s 37(1) (employment connected with Victoria, as a fact), s 39(1), (1A), (2A), s 40(1), (1A), (2), (2A), (3), (4), (5), (6), (7) (severe injury), s 625(1).
- **Notice and claim:** s 18(1), (3), (4), (5), (6), (7); s 20(8), (9) (as a note); s 75(1); s 178(3).
- **Mental injury provisional payments:** ss 263AA, 263B(1), (2), 263I.
- **Weekly payments:** s 152 (entitlement periods), s 159 (twice SAWE, by financial year), ss 161, 162, 163(1), (2), 165(3), (4), (5), s 625(2), ss 169, 171, s 189(1), (3).
- **Impairment benefit:** s 197(2), (3), s 210(1) (relevant date), s 211(2), s 212, s 217(1), (2), s 219.
- **Death:** s 236(1)-(5) (with (6) and s 237 answered `NOTHING`), s 237A.
- **Common law:** s 325(2)(e)-(g), s 328(2)(b), s 329A, s 330(1), (3), s 335(1), (2)(d)(i), s 337(1), s 340.

**Out, and why:**

- **Part 1, Part 2 Division 4 (assessment of impairment), Parts 4, 6, 8-12, most of 13, the Schedules**: machinery, the employer's return-to-work duties, dispute procedure, premiums, self-insurers and the bodies. Schedule 1 (deemed workers) is a large definition of "worker" in its own right, asked here only through the facts.
- **Within Parts 2 and 5, left for a later layer**: s 41 (undisclosed pre-existing condition), ss 42-45 (driving offences), ss 46-51 (journeys, injury abroad, compensation elsewhere, diseases); ss 153-158 (pre-injury average weekly earnings, an input); s 164, s 164A, s 170 (surgery and treatment after the second entitlement period or retirement), ss 167-167K (certificates and the determination procedure), s 168 (superannuation contributions), ss 172-177 (pensions, absence from Australia, imprisonment); ss 180-188, 190-194 (alteration, the deemed entitlement of ss 190(3) and 191(4) until a notice expires, outstanding payments); ss 196, 198-209 (Division 5 claim procedure), s 213, s 214, s 214A (further hearing loss, foetus, further EPD injury), ss 215-216, 218, s 221 and Schedule 4 (no-disadvantage table); Division 7 (medical and like services); s 237(1)-(3), 237AA (shares left to judgment), s 240, s 241 (dependants' weekly pensions), s 243; Division 9 (settlements); the business-day deadlines of s 75A (public holidays are not deposited).
- **Within Part 7**: Division 1 (choice of law); s 326 (other damages routes, transport accidents), s 329 (time hindering a medical examination), ss 331-334 (responses, conference, statutory offers), ss 336, 338, 339, ss 341-347 (jury, reductions under s 343, costs, the end of weekly payments on judgment), s 348, s 349 (limitation periods), Divisions 3-6.

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects" (2026-11-04 and 2026-11-05): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` elsewhere. In this row:

- `JUST FALSE`: s 37(1) ("There is no entitlement ... other than"); s 39 grants introduced by "If" that fail; s 40 ("There is no entitlement"); s 163(1) ("ceases ... unless"); s 165(4) ("must not approve ... unless"); s 237A(2) (a "means" definition, answered as an amount of nil).
- `NOTHING`: a mental injury before 31 March 2024 (the earlier text governs, not deposited); s 625(2) workers (the earlier ss 163, 165, 175); s 20(8)(a) ("as soon as practicable" fixes no day) and a Division 5 claim (s 20(8) is silent); s 189 outside s 189(1) (a scope limit with no "only"); s 236(6) and s 237 (a share set by judgment); s 325(2)(e)(i) for a worker under 26 or in Schedule 2 item 1 (the text gives no measure); any day outside the two years of figures.

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. s 39(2A), `ss 37, 39, 40 -- the worker is entitled to compensation`: "Despite section 40(1A)" read as overriding s 40(1A) only, so reasonable management action (s 40(1)) still bars a traumatic-events claim. Other reading: s 39(2A) entitles whatever s 40 says.
2. s 40(5), (6): an injury that "results in death or severe injury" is built from the severe injury head alone in the seat (the worker is asking, so alive). Other reading: none needed while death claims are out of this question.
3. s 75(1), `s 75(1) -- the claim is deemed accepted`: deemed accepted from the day after the 28th day. Other reading: deemed on the 28th day itself, which moves the s 178(3) day one earlier.
4. s 161, s 162: a "difference" below nil is nil. Other reading: the section does not apply where current weekly earnings exceed the rate.
5. s 189(3)(a), (c): "one year" read as 52 weeks of continuous payments. Other reading: a calendar year, which can be 52 weeks and a day or two.
6. s 169: an injury on the day exactly 130 weeks (910 days) before retirement age is "within the period". Other reading: that day is outside.

## What the Act turns out to say

1. **s 212 prints $555 530 where every other maximum prints $555 350.** s 212(d)(ii) and (e) (lines 3182 and 3184), and items 14 and 15 of the s 545 Table (lines 7781-7782), give the psychiatric maximum as $555 530; s 211(2)(e)(ii), (f), s 217, s 236, s 340(b)(ii) and items 9, 10, 22, 23, 28-38 and 46 give $555 350. The Gazette notice prints the same varied figure, $759 510 and $783 000, for s 212(d)(ii) and (e) as for s 211 (lines 552-570). $555 530 varied as its own amount would not round to $759 510. It looks like a transposition of two digits. The encoding uses the Gazette figure; the two readings differ only for a psychiatric impairment over 70 per cent. Asserted (81 per cent, $783 000).
2. **The 2024 commencement date is only in the endnotes.** s 625(1) applies the new mental injury rules to "injuries that occur on or after the date of commencement of Division 1 of Part 2 of the amending Act"; the date, 31 March 2024, is found only in the endnote (line 10204). Asserted (30 and 31 March 2024).
3. **The Act does not say which year's amount applies to a death.** s 545 varies the s 236 and s 237A amounts "in respect of the financial year", and s 239 adds interest from the claim, but neither says whether the amount is the one in force at the death, the claim or the determination. The encoding uses the day of the death. Asserted (deaths in September 2025 and September 2026).
4. **s 340 tests the threshold before reductions, and says nothing about the maximum.** The thresholds apply to the total "assessed, before the reduction (if any) under section 26(1) of the Wrongs Act 1958 and before the reduction (if any) under section 343(1)"; the maximum is "in excess of" an amount, with no such words. The encoding caps the same pre-reduction total and applies no reduction. Asserted (thresholds and maxima).
5. **s 211(2)(c) and s 211(2)(d) do not meet at 30 per cent.** In the Act's own figures, (c)(i) gives $18 810 + 20 x $2830 = $75 410 at 30 per cent, while the (d) formula starts from $75 260 for "more than 30 per cent"; so a rating a little over 30 would get less than a rating of exactly 30 (for whole-number ratings, 31 per cent gives $79 960, so no worker is worse off). With the varied figures the gap moves with rounding (s 547): for 2025-26, $25 730 + 20 x $3860 = $102 930 against a (d) start of $102 950; for 2026-27 both are $106 130. Noted; the band edges are asserted (30 and 31 per cent).
6. **s 75(1) deems acceptance but does not say when.** The claim "is deemed to have been accepted" if no notice is given within 28 days; s 178(3) then counts 7 days "after the claim is accepted". See fork line 3. Asserted (deemed on 31 March for a claim received 2 March 2026; trace paid on day 36).
7. **s 329A disregards 24 December to 9 January for ss 330-337 only.** The 18 months of s 328(2)(b) and the 28 days of s 75 are not adjusted, and the encoding does not adjust them. Asserted (s 330 and s 335 across the break).

## Before relying on it

- An independent test pass, and a lawyer's review of the fork lines and findings.
- The Gazette notice for 1 July 2027, when published, deposited and added.
- The sections listed as out, especially pre-injury average weekly earnings (ss 153-158), the deemed entitlement until a notice expires (ss 190, 191), dependants' pensions (s 241), the no-disadvantage table (s 221), medical and like services (Division 7), and the limitation periods (s 349).
- A further seat for the employer (registers, forwarding claims, return to work), drawing on the same core.
