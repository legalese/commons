# Transport Accident Act 1986 (Vic): baseline encoding for the person injured in a transport accident

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is the first encoding of this Act; nothing beside it was changed.
There is no REFUSE in it. A question the encoding cannot answer returns `NOTHING`, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Three modules:

- **`taa-core.l4`**, seat-neutral: the date arithmetic (built-in date functions only, no daydate), the Act's printed figures, and the rules of Parts 3, 4 and 6 in scope, each with the section and the deposited line it comes from. Five duties with deadlines are regulative rules (`DEONTIC`): s 70(1) with s 70(3) (the Commission's response to a claim, and the deemed rejection), s 70(4) (complying with a request, or the claim lapses), s 64(1) with ss 65(2), 66 (the driver's report, and the $50 penalty), ss 49(4), 50(4), 51(5) (the statement of earnings), s 46A(1A) (an impairment determination, advice or written application within 6 years, three ways joined by `ROR`).
- **`taa-seat.l4`**, the injured person's seat: 49 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order. It builds the core's inputs from plain answers and restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`taa-cases.l4`**, the cases: every exported question, with its edges, and every regulative rule by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

## Edition

**Transport Accident Act 1986**, Act No. 111/1986, **Version No. 159, incorporating amendments as at 1 November 2026**, deposited at `../../registers/source-bundle/transport-accident-act-1986.txt` (sha256 `12651ae2a85982608f9e5c4478f99171ead53a712486b8c1ea2ca6fe954b8df3`).
The owner saved the Word file by hand on 2026-11-06 from the version page, and it was converted to text; `transport-accident-act-1986.meta.json` records the file, its hash and the conversion, and `subjects/au/vic/README.md` records the deposit. Line numbers in the modules are lines of that text.
Version 159 replaced 158 (2 October 2026) on 1 November 2026. It includes No. 45/2026: the new s 59(1), s 59(3A) (the surviving child's weekly payment doubled from 1 November 2026), s 59A (an education allowance for every dependent child), and s 60(11C). Each is encoded, and s 59(3A) is asserted on both sides of 1 November 2026.

**The formulas sidecar.** Of the 23 equations in `transport-accident-act-1986.formulas.md`, F1 (s 51), F2-F5 (s 57) and F6-F7 (s 58) are used, as transcribed there from the Word file. F8-F13 (s 61 indexation) are described but not worked, since the ABS figures are not deposited; F14-F23 (ss 110, 142, 143) are out of scope. The sidecar has not been checked against the authorised PDF, and nor has this encoding.

**The figures.** The Act prints each dollar amount as it was last written into it (most in 1994 or 2004), and s 61 (lines 2083-2142) varies them every 1 July: the weekly amounts by Victorian average weekly earnings (s 61(1), (2B), (2C)), the lump sums, caps and thresholds by the Melbourne CPI (s 61(2), (2A), (2D)). No instrument stating the varied amounts is deposited. None was found in the Gazette on 2026-10-24 (`subjects/au/vic/README.md`), and the Act requires none: s 61 varies them by formula. So **every question that needs an amount asks for the current figure** (which the Transport Accident Commission publishes), and its `@desc` gives the figure the Act prints. The cases use the printed figures, or round made-up figures where the case says so. The impairment benefit is offered both ways: at the table's printed amounts (s 47(2), a base that has been varied every year since 2005), and at the current amounts of the person's band, entered as two inputs.

## Checks

| Module | Assertions |
|---|---|
| `taa-core.l4` | none (0 errors, 0 warnings) |
| `taa-seat.l4` | none (0 errors, 0 warnings) |
| `taa-cases.l4` | 323 written, 323 satisfied (0 errors, 0 warnings) |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-06). A copy of the case file with one expected value changed was run first, to confirm that a failure is reported (312 satisfied, 1 failed); it was not kept.
Every expected value was worked by hand from the deposited text, with the arithmetic in the comment above the assertion. The edges asserted include: the last day and the day after for the claim (s 68), the Commission's 21 days (s 70), the 28 days and 14 days (ss 64, 66, 70(4)), the 18 months (s 44(4), with s 3(4) and s 46(2)), the 3 years and the age of 21 (s 53), the 6 years (s 46A(1A)) and the 3 years (ss 60(1A), 60A); 29 February, month ends and the turn of the year; the fifth and sixth day of lost earnings (s 43); each band edge of s 47(2) (10, 11, 19, 20, 49, 50, 59, 60, 79, 80, 89, 90, 99, 100, 101); 29 and 30 per cent (s 93); 49 and 50 per cent (ss 53, 54A); 0.05, 0.06, 0.119, 0.12, 0.239 and 0.24 (s 40); 9.49 and 9.5 (s 46C); 9.9, 10 and 10.5 per cent NAL (s 46A(3)); the 10 per cent difference of s 52 and a dollar over it; each maximum, the amount equal to it and a dollar over it (s 93(7)); ages 20, 25, 26, 75 and 80 (s 57); 31 October and 1 November 2026 (s 59(3A)).
Breached traces are asserted through a helper (`ends fulfilled`) and `NOT`, because `EVALTRACE ... EQUALS` cannot test a breach. A trace notices a passed deadline only at the next event or `WAITUNTIL`, and the rule that follows counts from there, so the s 66 penalty trace pays on day 43 (14 days from the `WAITUNTIL 29`), where the date question gives 42 days after the notice.

## Seat

**The person injured in a transport accident** (`taa-seat.l4`): a person injured in an incident directly caused by the driving of a motor car or motor vehicle, a railway train or a tram (s 3(1)). The person asks as the injured person, or as the driver the Commission has asked to report (s 64). Under "If the person dies", the questions are asked by the surviving partner of a person who died as a result of a transport accident, or for a dependent child of that person (by the child or the person caring for the child).
*Am I entitled to compensation? What does a conviction, or being unlicensed or uninsured, do to my benefits? By what day must I claim, and is my claim in time? By when must the Commission respond, decide, or be taken to have rejected it? By when must I comply with its request, report, or pay the penalty? By when can I apply to VCAT? On a given day, am I paid for lost earnings? How much are my weekly payments in the first 18 months, as a self-employed person, and after 18 months, as an earner or not? When do they stop? By when must I give my statement of earnings or my seasonal election? Am I entitled to the safety net benefit, and what is its most? What is my degree of impairment, rounded or for hearing loss; from when can it be determined; by when must I ask, and is it taken to be 0%? How much is my impairment benefit? From when are my medical expenses covered; how many hours of child care; what for lost wages at my child's bedside or after a later hospital stay? Is my injury taken to be serious; can I sue; how much for pecuniary loss and for pain and suffering; when does my cause of action arise? What does my family get if I die: the partner's lump sum and weekly payments and until when, the child's share, weekly payment, lump sum and education allowance, the funeral, and damages for the death?*

The Transport Accident Commission, VCAT and the courts get no seat: their duties and judgments appear only as what the person must be given, by when, and what follows. No seat is written for an insurer or for the person at fault.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Departed from of necessity: s 61 sets the numbers by formula from ABS figures, and no statement of the varied amounts is deposited, so they are inputs (see Edition). The Transport Accident Regulations 2017 are indexed but not deposited; nothing encoded reads a number from them, and the questions that need them (s 47(4) periodic payments, s 56 redemption, the regulations' further severe injuries) are out or take the fact as an input.
- **The actors the text names.** Followed: the person injured, the earner, the driver, the surviving partner, the dependent child, the responsible person, the Commission, the Tribunal, a court.
- **A judgment handed to someone else answered conditionally.** Followed. The Commission's satisfaction (s 36, s 39(2), s 40's "did not contribute", s 43(2), s 68(2)'s reasonable grounds, s 93(4)(c)), a court's leave (s 93(4)(d)), the earning capacities the Commission determines (ss 49(5), 50(5)), the degree of impairment, "reasonably likely not to be employed" (s 51), "unreasonably refuses" (s 54A(2)) and the court's assessment of damages are inputs the person states.
- **Definitions worked out, borrowed terms asked.** Worked out in L4: severe injury (s 3(1)), the period of entitlement (ss 44(4), 45(6)), assessed earnings (s 58(6)), A in s 57(2), the s 46C rounding and the s 46A(3) hearing conversion. Asked as facts: earner (s 3(2)), dependant, dependent partner, dependent child, pre-accident weekly earnings (ss 4, 4A, 5, worked out from a year of pay), pension age (the Social Security Act 1991 (Cth)), the offences of the Road Safety Act 1986 and the Crimes Act 1958, and a serious injury (s 93(17)).
- **One case.** One transport accident and one injured person (or one death).
- **The Act's own terms with a plain gloss.** Followed; the seat says "showed itself" for "manifested itself" in input names, and the `@desc` gives the Act's word.
- **Operative sections in; machinery out.** Followed: the Commission, the Fund, the transport accident charge, the indexation arithmetic and regulation-making are out.

## Scope

**In** (the focus: no-fault benefits for loss of earnings, impairment, medical and like expenses and death, and the s 93 thresholds for common law):

- **Entitlement:** s 35(1), s 36, ss 37, 38A (as one fact), s 39(1), (2), (3), s 40(1)-(6), s 41(1)-(1C), s 41A, s 41B, s 42(2).
- **Loss of earnings (first 18 months):** s 3(4), s 43(1), (2), s 44(2)-(4), s 45(2)-(6), s 45AA(2), s 45AC(4), s 46(2).
- **Loss of earning capacity (after 18 months):** s 49(2), (3), (4), s 50(2)-(4), s 51(2), (5), s 52, s 53(1), (1B), (2)(a), (3)-(5).
- **Safety net:** s 54A(1)-(5), s 3(1) severe injury.
- **Impairment:** s 46A(1AA), (1A), (1B), (3), s 46C(2), s 47(1), (2), s 47(6)(b) (with s 93(3)).
- **Death:** s 57(2)-(6), s 58(2)-(8), s 59(1)-(4), (6), (8)-(10A), s 59A.
- **Medical and like:** s 60(1A), (2)(c), (2AB), (2A)(b), (2CA)-(2CD), s 60A(1)(b), (2)(a), (3), (4).
- **Claims, decisions, review:** s 64(1), (3), (4), s 65(2), s 66(1)(a), s 68(1)-(3), s 70(1)-(4), s 77(1A), (2).
- **Common law:** s 93(1), (2), (3), (4), (6), (7), (8), (9), (11), (11A), (19).

**Out, and why:**

- **Part 1 ss 4-7, s 3(2)**: pre-accident weekly earnings and the earner test are worked out from pay records and the Commission's assessment (s 5); asked as facts.
- **Part 2** (the Commission, the Board, the Fund): machinery.
- **Part 3, left for a later layer:** s 38, s 38AA (reimbursement between schemes, pre-1992 injuries); s 40A (withholding pending a charge); s 42(3)-(5) (recovery, notice of an interstate claim); s 45A (notice of a return to work "immediately", no fixed period); s 45AB (reconciling interim payments); ss 46(1), 55 (reviews, Commission procedure; s 55(3) appears in a rule's breach reason); s 46A(1), (1AB)-(1F), (2)-(10), ss 46AA, 46B (the timing and method of determining impairment; the A.M.A. Guides are not deposited); s 47(3)-(5), (7)-(8) (how the benefit is paid, interim benefits, determinations for damages); s 48 (more than one accident; needs the notional pre-2004 amounts); s 49(6)-(9), s 50(6), (7), s 50A (age rates, supported employment, a return to work); **s 54** (minors' additional benefit: the deposited text reads "$59A", see finding 2); ss 56, 56A (redemption, by the regulations); s 59(4A), (5), (7), (11)-(17) (trustees, refunds, notices by the responsible person); s 60(2)(a), (b), (ca), (d), (2AAA), (2AC), (2A)(a), (2BA), (2C), (2D)-(2EB), (2F)-(13) (reasonable costs, the Commission's judgment; caps of a single figure would add little); s 60B, ss 61A-61D (agreements); s 61 (the indexation arithmetic, see Edition); s 62, s 62A.
- **Part 4, left out:** s 65(3), (4), s 66(1)(b), (2), s 67, s 67A, s 69 (Part 10 accidents), ss 71-76, Division 2A, ss 77(1), (3), (4), 78-82 (review procedure).
- **Part 5** (trailers), **Part 6 Division 2 and ss 104-107A** (indemnity and recovery between the Commission and others), **s 93(5), (6A)-(6C), (10), (12)-(18B), ss 93A, 93D** (procedure, evidence, costs, the excluded heads of damages, which the input's `@desc` names), **Part 7** (the transport accident charge), **Part 8** (offences), **Part 9**, **Part 10** (accidents before 1987), **Part 11** (transitional: the encoding applies the text as it now stands, for accidents after the amendments).

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects" (2026-11-04 and 2026-11-05): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` elsewhere. Questions that can only be answered yes or no by the text are typed `BOOLEAN`. In this row:

- **No (`FALSE`, `JUST FALSE`, or nil for an amount):** s 35(1) (an "if" list); the flat "not liable" and "not payable" of ss 37, 38A, 39, 40, 41, 41A, 41B, 42(2), 43(1), 52, 53, 54A(2), (3), 57(5), (6), 58(7), (8), 59(8)-(10A); the periods the text fixes (ss 44(4), 45(6), 46A(1A), 53(3), 59(3), 59(6), 60(1A), 60A(1)(b), 68); s 93(2) and (4) ("may not ... unless"); s 93(7) ("only if"); s 60(2A)(b) ("where", fork line 2).
- **`NOTHING`:** s 51 at or over pension age (the formula cannot be worked); s 47(2) over 100 per cent (outside the table); s 57 and s 58 with more than one partner and no years of dependency; s 57(4)(c) and s 59(4) with no children to divide among; s 77 for an interim benefit decision (fork line 5); s 93(2)-(6) after more than one accident where neither s 93(3) nor (4) applies (finding 9).

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. s 45, `s 45 -- the weekly payment for partial loss of earnings`: "current weekly earnings" ((2)(a), (3)(a), defined in (6)) and "actual weekly earnings" ((2)(b), (c), (3)(b), undefined) are one figure, the earnings in the week. Other reading: actual weekly earnings are something else, such as the earnings over a longer period.
2. s 60(2A)(b), `s 60(2A)(b) -- what is paid for funeral expenses`: "where the total amount of the expenses does not exceed $14 135" is a condition, so a total over the figure gets nothing under (b). Other reading: a cap, as in (a) ("not exceeding $15 000"), paying up to the figure.
3. s 93(7)(a)(i)-(ii), (b)(i)-(ii), `s 93(7) -- the damages that can be recovered`: an assessment exactly equal to the maximum meets neither "less than" nor "more than", so nothing can be recovered. Other reading: the maximum.
4. s 93(9), (11A), `s 93(8), (9), (11A) -- the damages for a death`: the $500 000 limit applies to the damages after the ss 57-59 reduction. Other reading: the limit first, then the reduction, as s 93(7) says expressly for injuries.
5. s 77(2), `s 77(1A) -- the last day to apply to the Tribunal for review`: no date for an interim benefit decision, answered `NOTHING`. Other reading: `JUST FALSE` to a separate "Can I apply?" question.
6. s 59(3A), `s 59(3), (3A) -- the weekly payment for a child on the day`: the doubling applies to the amount as varied under s 61(1). Other reading: double the printed $59, varied separately.
7. s 43(1), `ss 43, 44(4), 45(6) -- the day is in the period of entitlement`: "the first five days ... in respect of which, or any part of which, the earner suffers any loss of earnings" read as the first five days on which earnings are lost. Other reading: the first five calendar days after the accident or manifestation.
8. s 53(1)(c), (d), `s 53 -- the weekly payments are stopped on the day`: "injured" read as the day the injury first manifested itself, from which the 36 months run. Other reading: the day of the accident for (c) and (d).
9. s 68(3), `s 68(1), (3) -- the last day to claim`: "before attaining the age of 21 years" ends on the day before the 21st birthday. Other reading: on the birthday.
10. ss 45, 50, 57, 93: an amount the formula takes below nil is nil. Other reading: the provision does not apply at all.
11. s 39(1), `s 39(1) -- the Commission is not liable because no report was made`: (a) and (b), joined by "and", are read as one test for each kind of accident; the s 39(2) excuse, for an accident "involving a motor vehicle", is read as covering the pedal cycle accidents of (a) too. Other reading: no excuse for a pedal cycle accident with no motor vehicle.
12. s 58(5), `s 58(5) -- the last day of a surviving partner's weekly payments`: payments "continue ... until the surviving partner ceases to have a dependent child" run to the day before. Other reading: to that day.
13. s 47(6)(b) with s 93(3), (4), `s 93(2)-(6) -- the person may bring proceedings for damages for the injury`: after more than one accident, "the degree so determined" in s 93(4)(b) is the total degree, so with 30% or more in all but under 30% from any one accident neither (3) nor (4) applies and the answer is `NOTHING` (finding 9). Other readings: (a) the degree is taken per accident, as s 47(6)(b) measures it "as the result of one of the transport accidents", so s 93(4) applies and the Commission's certificate or a court's leave opens the way; (b) with (3) and (4) both out, s 93(2) governs alone and the person may sue if the injury is in fact a serious injury.

## What the Act turns out to say

1. **The child's weekly payment doubled on 1 November 2026.** No. 45/2026 s 18A inserted s 59(3A): "on or after 1 November 2026, the sum of a weekly payment ... is double the amount that would otherwise be payable under subsection (3)(a)". It took effect the day version 159 begins. It does not say whether the varied amount or the printed $59 is doubled (fork line 6). Asserted (31 October and 1 November 2026).
2. **The conversion lost decimal points and signs in running text.** The text has "024" and "005" for 0·24 and 0·05 in s 40(3)(b), (3A)(b) and (4)(b) (lines 918, 923, 932), though s 40(5) and s 40A(5)(c) keep "0·05"; "10 + [0278 (NAL 10)]" in s 46A(3) (line 1292) for 10 + [0·278 × (NAL − 10)]; "95% ... 10%" and "84% ... 8%" in the s 46C example (line 1347) for 9·5% and 8·4%; and no multiplication sign in the s 47(2) table ("((D – 10) $1000)"). These are text, not equation objects, so the sidecar does not carry them. The encoding uses the readings given, which the surrounding text supports (s 40(5)'s bands; s 46C's own rule; the table's arithmetic). **s 54(2) prints "$59A"**: it could be $59 × A or a lost decimal, and the two differ tenfold, so s 54 is left out. Check all of these against the authorised PDF. Asserted for the readings used (0.24 and 0.05 edges, NAL 10.5 and 100, 9.5 and 8.4, the band edges).
3. **Alcohol and drugs together cost less than alcohol alone at 0.24.** For a s 49(1)(b), (f) or (g) conviction at 0.24 or more, s 40(5)(c) takes away all loss of earnings compensation; for a s 49(1)(bc) or (j) conviction (alcohol and drugs) at the same concentration, s 40(5B) reduces it by one-third only (the further third is for 0.12 to under 0.24). Both lose the impairment and earning capacity benefits (s 40(3)(b), (3B)). Asserted.
4. **s 45 uses two terms for the earner's earnings.** See fork line 1.
5. **The minor's "3 years after the transport accident" in s 68(3) never adds a day.** A person under 18 at the accident turns 21 more than 3 years later, so "before attaining the age of 21" always ends no earlier than "within 3 years after the transport accident"; they meet when the accident is the day before the 18th birthday. Asserted (born 2 December 2007, accident 1 December 2025: both give 1 December 2028).
6. **s 54A states a maximum and no amount.** The safety net payment "must not exceed" the lesser of $965 and 80% of the greater of two earnings figures; nothing says what it is below that. The encoding answers the maximum only. Asserted.
7. **The funeral limit is worded as a condition.** See fork line 2. Asserted ($14 135 paid, $14 136 nothing).
8. **s 93(7) has a gap at each maximum.** See fork line 3. Asserted ($686 840 and $305 250 give nothing; a dollar under gives the assessment, a dollar over the maximum).
9. **Two accidents can leave no way to sue.** s 47(6)(b) says that after two or more accidents with a total over 10%, "section 93(3) does not apply unless the degree of impairment is determined to be 30 percent or more as the result of one of the transport accidents". If the total is 30% or more but no one accident gave 30%, s 93(3) does not deem the injury serious, and s 93(4) does not apply either, because the degree determined is not "less than 30 per centum". s 93(2) still needs a serious injury, but neither the Commission's certificate nor a court's leave is provided for. The encoding answers `NOTHING`; the other readings are fork line 13. Asserted (35% in all, 20% from one).
10. **s 59A carries none of s 59's bars.** The education allowance under s 59A goes to a dependent child "if the child is not entitled to an education allowance under section 59". A child barred under s 59 by an award of damages (s 59(10)) or by the child's own conviction (s 59(10A)) is then entitled under s 59A, literally. s 59A also says "dies in a transport accident", where s 59 says "as a result of". The encoding's education allowance question asks none of the bars, as the text reads.
11. **s 61's lists are out of date.** s 61(2D) varies "the amount of $5000 referred to in section 60(2A)(a)", but s 60(2A)(a) has said $15 000 since No. 71/2013 (and $15 000 is in the s 61(2) list). s 61(2) lists $144 500 and $61 940, which appear nowhere else in the Act. It also lists $1500, which appears only in the s 47(2) table, and that table is varied by s 61(2A). Nothing encoded turns on these, since the varied amounts are inputs.
12. **The child's lump sum leaves out apprentices.** A dependent child includes one of 18 to 24 who is a full-time student or an apprentice (s 3(1)). But s 59(4)(a) pays the death benefit only to a child "under 18 years of age or, if a full-time student, under 25 years of age", while s 59(4)(b) divides by "the number of dependent children", apprentices included. Asserted (18 and not a student: nothing; 20 and a student: a share).
13. **s 93(19) does not say which day.** The cause of action "arises on the day of the transport accident or on the day on which the injury first manifests itself". The encoding reads it as the later of the two. Asserted.
14. **The binaural hearing formula reaches 36%, not 35%.** At 100% NAL, 10 + 0·278 × 90 = 35·02, which "rounded up to the next whole number" is 36. Asserted.

## Before relying on it

- Check the conversion against the authorised PDF, especially finding 2 and the sidecar's equations, and then encode s 54.
- An independent test pass, and a lawyer's review of the fork lines and findings.
- The Commission's current indexed amounts, deposited as a source. They are published by the Commission rather than gazetted. A layer could then fill the figure inputs, as the workers' compensation encoding does from its Gazette notice.
- The Transport Accident Regulations 2017, saved and deposited (s 47(4) periodic payments, s 56 redemption, further severe injuries, prescribed benefits for "earner").
- The sections listed as out, especially pre-accident weekly earnings (ss 4-5), the timing of impairment determinations (s 46A(1)-(1E)), several accidents (s 48), the other heads of s 60, and the limitation periods of the Limitation of Actions Act 1958 (not deposited), which s 93(19) feeds.

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Workplace Injury Rehabilitation and Compensation Act 2013** (`../../../workplace-injury-rehabilitation-and-compensation-act-2013/encodings/baseline-2026-11/`): s 38A and s 37 here turn on entitlement under that Act (asked here as a fact). A road accident in the course of employment goes there first.
- **Social Security Act 1991 (Cth)** (`subjects/au/social-security-act-1991/`): pension age (ss 53, 58(5)) and the compensation preclusion rules that the weekly payments and lump sums here meet.
