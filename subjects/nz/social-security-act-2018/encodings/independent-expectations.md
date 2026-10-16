# Independent expectations: Social Security Act 2018 (NZ), main benefits

Written from BRIEF.md and the Act (as at 26 September 2026) before any `.l4` module was opened.
These expected values are fixed. They must not be changed after the encoding is read.

## Conventions and readings taken

- **R1. Ages.** "at least 18 years old" is met on and after the 18th birthday. Where the encoding takes a date of birth, a person born 2009-04-10 is 18 on 2027-04-10 and 17 on 2027-04-09. Where it takes a whole-number age, I pass the whole years.
- **R2. "at least 2 years".** Two years of continuous residence, exactly, satisfies s 16 ("for a period of at least 2 years"). Where residence is an input in days, 730 days satisfies and 729 does not. Where it is a start date, 2025-03-01 to 2027-03-01 satisfies and 2025-03-02 to 2027-03-01 does not.
- **R3. Income tests.** All four tests reduce "the applicable rate of benefit" on "the total income of the beneficiary and the beneficiary's spouse or partner". Income up to and including $160 a week brings no reduction. Income Tests 1 and 2 are banded: income between $160 and $250 a week ("more than $160 a week but not more than $250 a week"), then income over $250 ("more than $250 a week"). A rate never goes below zero.
- **R4. Lost tables.** I chose these Schedule 4 Part 1 and Part 3 inputs myself; they are not the Act's figures. Jobseeker support base rate **$342.00**, subject to **Income Test 1**. Supported living payment base rate **$420.00**, subject to **Income Test 1**. Some scenarios use other tests on purpose. With $342 under Income Test 1, the rate reaches zero at exactly $700 of weekly income (27 + 0.7 x 450 = 342).
- **R5. s 24.** "income of less than the amount that would reduce the applicable rate of jobseeker support to zero" is a strict inequality. Income that reduces the rate to exactly $0 is not "less than" that amount, so it fails s 24(1)(b). I read s 24 as measuring the person's income through the income test that governs the rate, and that test counts partner income as well. This is **ambiguous**: s 24 says "P has ... income", but the reduction-to-zero amount can only be worked out with the income test, which adds the partner's income. I take the combined reading because "the amount that would reduce the applicable rate ... to zero" is defined by that test.
- **R6. s 24(2).** If income is enough to bring the rate to zero only "during a temporary period", and P otherwise meets the requirements, entitlement "is not affected by that income". So a temporary-period flag overrides the s 24(1) failure.
- **R7. Childcare disregard (Sch 4 Pt 2 cl 2).** "MSD may disregard up to $20 a week of the beneficiary's personal earnings used to meet the cost of childcare". Where MSD applies it, the amount disregarded is min(20, childcare costs, personal earnings). This applies to sole parent support only.
- **R8. Stand-down arithmetic.** The regulations set the length (an input). A stand-down of N days that starts on day S ends on day S+N-1, and "the day after the stand-down period ends" is S+N. If the encoding takes the end date instead, I pass S+N-1. With N = 7 and S = 2027-03-01, it ends 2027-03-07 and the benefit commences 2027-03-08.
- **R9. "within 28 days after".** For an entitlement date of 2027-03-01, receipt on 2027-03-29 (day 28) is within, and receipt on 2027-03-30 (day 29) is not.
- **R10. s 316(2) gap.** If the benefit is listed in s 316(2)(a)-(g) but the application arrives after the 28 days, s 316(3) does not literally apply ("If the benefit is not one specified in subsection (2)(a) to (g)"). The Act is **silent** on this case. Following BRIEF.md, I expect REFUSE (no date). I note that the purposive reading would apply the s 316(3) "later of" rule instead. See CM-20 and CM-21.
- **R11. s 18.** A person receiving another main benefit, NZ superannuation or a veteran's pension fails the general requirements for a new main benefit ("not entitled to receive at the same time").
- **R12. s 19.** "only by virtue of holding a temporary entry class visa" or "unlawfully resident or present" means the person is not entitled to any benefit, whatever else holds.
- **R13. s 33.** "aged under 14 years": a child who turns 14 on 2026-11-05 is under 14 on 2026-11-04 and not under 14 on 2026-11-05.

## Goal 1: General requirements (ss 16, 18, 19)

Baseline for G-scenarios: the person applies on 2027-03-01, is a NZ citizen, is ordinarily resident in NZ when first applying, has resided continuously for 3 years since becoming a citizen, is not a refugee, is not unlawfully present and holds no temporary visa, and receives no other main benefit, NZ superannuation or veteran's pension.

| id | inputs (changes from baseline) | expected | provision relied on |
|---|---|---|---|
| G-01 | baseline | residential requirement met; general requirements met | s 16(2)(a)(i) "is a New Zealand citizen ... ordinarily resident ... resided continuously ... at least 2 years" |
| G-02 | residence 2 years exactly (730 days) | met | s 16(2)(a)(i) "at least 2 years" (R2) |
| G-03 | residence 729 days | not met | s 16(2)(a)(i) |
| G-04 | residence-class visa holder instead of citizen, 3 years | met | s 16(2)(a) "or holds a residence class visa" |
| G-05 | citizen, 3 years, NOT ordinarily resident when first applying | not met (no reciprocity) | s 16(2)(a) "and is ordinarily resident in New Zealand when P first applies" |
| G-06 | residence-class visa, 1 year, recognised refugee | met | s 16(2)(a)(ii) "is recognised as a refugee or a protected person" |
| G-07 | residence-class visa, 1 year, protected person | met | s 16(2)(a)(ii) |
| G-08 | residence-class visa, 1 year, not refugee or protected | not met | s 16(2)(a) |
| G-09 | neither citizen nor resident-visa holder; ordinarily resident in a reciprocity country; 2 years continuous NZ residence before applying | met | s 16(2)(b) "ordinarily resident in a country with which New Zealand has a reciprocity agreement, and ... at least 2 years before applying" |
| G-10 | as G-09 but 1 year | not met | s 16(2)(b) |
| G-11 | as G-09 but the country has no reciprocity agreement | not met | s 16(2)(b), (3) |
| G-12 | refugee status, but no citizenship or residence class visa | not met (the refugee limb hangs off the citizen/resident stem) | s 16(2)(a) stem "P is a New Zealand citizen or holds a residence class visa ... and— ... (ii)" |
| G-13 | baseline but unlawfully present | not entitled to any benefit | s 19(a) "unlawfully resident or present in New Zealand" |
| G-14 | present only on a temporary entry class visa | not entitled | s 19(b) "only by virtue of holding a temporary entry class visa" |
| G-15 | baseline, receiving another main benefit (e.g. supported living payment) | general requirements fail | s 18(a) "more than 1 main benefit" |
| G-16 | baseline, receiving NZ superannuation | fail | s 18(b) |
| G-17 | baseline, receiving a veteran's pension | fail | s 18(c) |
| G-18 | baseline, receiving none | pass | s 18 |
| G-19 | reciprocity route with exactly 2 years (730 days) | met | s 16(2)(b) "at least 2 years" |

## Goal 2: Entitlement

### Jobseeker support (ss 20-24, 26)

Baseline JS: general requirements met (as G-01); applies 2027-03-01; born 1995-06-01 (31); no dependent child; not in full-time employment; available for and seeking full-time employment, willing and able, has taken reasonable steps; weekly income $0, partner none; not a full-time student; no strike; no training belief; base rate $342 under Income Test 1 (R4).

| id | inputs | expected | provision |
|---|---|---|---|
| JS-01 | baseline | entitled | s 20(a)-(e) |
| JS-02 | in full-time employment, not losing earnings | not entitled (no work gap) | s 21(1)(a) "P is not in full-time employment" |
| JS-03 | in full-time employment but losing earnings through a health condition | work gap; entitled (if availability via s 22(c)) | s 21(1)(b) "is in employment but is losing earnings through a health condition or injury" |
| JS-04 | not available: not seeking work, no exemption, no health limit | not entitled | s 22 |
| JS-05 | seeking FT work, willing and able, but has NOT taken reasonable steps | not available; not entitled | s 22(a)(ii) "has taken reasonable steps to find it" |
| JS-06 | would satisfy (a) but for circumstances qualifying for a work-test exemption | available; entitled | s 22(b) |
| JS-07 | willing and able but limited by disability | available; entitled | s 22(c) |
| JS-08 | age 18 exactly (born 2009-03-01, applies 2027-03-01), no dependent child | meets age; entitled | s 23(a) "at least 18 years old, in the case of an applicant without a dependent child" |
| JS-09 | age 17 (born 2009-03-02, applies 2027-03-01), no dependent child | not entitled | s 23(a) |
| JS-10 | age 19 with a dependent child | not entitled | s 23(b) "at least 20 years old, in any other case" |
| JS-11 | age 20 exactly with a dependent child (born 2007-03-01) | entitled | s 23(b) |
| JS-12 | age 19 without a dependent child | entitled | s 23(a) |
| JS-13 | income $699, partner $0 | entitled (rate $0.70) | s 24(1)(b) "income of less than the amount that would reduce ... to zero" |
| JS-14 | income $700 | not entitled (rate exactly 0) | s 24(1)(b) (R5) |
| JS-15 | income $800 | not entitled | s 24(1)(b) |
| JS-16 | income $800 but during a temporary period, otherwise eligible | entitled | s 24(2) "P's entitlement ... is not affected by that income" |
| JS-17 | income $160 | entitled | s 24(1)(b) |
| JS-18 | own $400 + partner $400 (total $800) | not entitled (combined reading R5) | s 24 with Sch 2 Income Test 1 "total income of the beneficiary and ... spouse or partner" |
| JS-19 | full-time student | not entitled | s 26(a) "P is a full-time student" |
| JS-20 | unemployed because of own participation in a strike | not entitled | s 26(b) |
| JS-21 | unemployed because fellow union members at the same place of employment strike | not entitled | s 26(b) "or participation by fellow members of the same union at the same place of employment" |
| JS-22 | MSD reasonably believes P became unemployed to undertake employment-related training | not entitled | s 26(c) |
| JS-23 | took leave without pay for employment-related training (MSD reasonably believes) | not entitled | s 26(c) "took leave with or without pay" |
| JS-24 | baseline but residential requirement not met | not entitled | s 20(d) |
| JS-25 | baseline but on a temporary visa | not entitled | s 19(b) |
| JS-26 | baseline but receiving NZ superannuation | not entitled | s 18(b) |

### Sole parent support (ss 29, 30, 32, 33)

Baseline SPS: general requirements met; applies 2027-03-01; aged 30; mother of, and caring for, one dependent child born 2020-05-01 (aged 6); single; no split care.

| id | inputs | expected | provision |
|---|---|---|---|
| SP-01 | baseline | entitled | s 29, s 30(a) "P is single" |
| SP-02 | spouse died | entitled | s 30(b) |
| SP-03 | marriage dissolved | entitled | s 30(c) |
| SP-04 | living apart and lost support of spouse | entitled | s 30(d) "is living apart from, and has lost the support of" |
| SP-05 | living apart, inadequately maintained | entitled | s 30(d) "or is being inadequately maintained by" |
| SP-06 | living apart but still adequately supported by spouse | not entitled | s 30(d) needs both limbs |
| SP-07 | partner in a relationship, living together, no limb applies | not entitled | s 30 |
| SP-08 | lost regular support because partner is serving a prison sentence in prison | entitled | s 30(e)(i) |
| SP-09 | partner on home detention with conditions preventing employment | entitled | s 30(e)(ii) |
| SP-10 | partner on home detention without conditions preventing employment, still living together | not entitled | s 30(e)(ii) "subject to conditions ... that prevent ... undertaking employment" |
| SP-11 | applicant aged 19 | not entitled | s 29(d) "is aged 20 years or over" |
| SP-12 | applicant aged 20 exactly | entitled | s 29(d) |
| SP-13 | only child turns 14 on the application date (born 2013-03-01, applies 2027-03-01) | not entitled | s 30 "dependent child aged under 14 years" (R13) |
| SP-14 | only child 13 (born 2013-03-02, applies 2027-03-01) | entitled | s 30 |
| SP-15 | caring for child but not the mother or father (and s 31 not applied) | not entitled | s 30 "is the mother or father of, and caring for" |
| SP-16 | split care, applicant already receiving SPS for one of the children | applicant entitled; other parent not | s 32(2)(a) |
| SP-17 | split care, neither receiving; applicant was principal caregiver before separation | applicant entitled | s 32(2)(b) |
| SP-18 | split care, neither receiving; other parent was principal caregiver before separation | applicant not entitled | s 32(2)(b), s 29(b)(ii) |
| SP-19 | split care, neither receiving, no prior principal caregiver; applicant cares for the youngest | applicant entitled | s 32(2)(c) |
| SP-20 | as SP-19 but other parent cares for the youngest | applicant not entitled | s 32(2)(c) |
| SP-21 | split care resulting from court day-to-day care orders for each parent | s 32 does not apply; both entitled | s 32(3) |
| SP-22 | residential requirement not met | not entitled | s 29(c) |
| SP-23 | receiving SPS; youngest child turns 14 on 2026-11-05; on that date | SPS expires; replaced with jobseeker support commencing 2026-11-05 | s 33(2) |
| SP-24 | as SP-23 but MSD reasonably believes P would not meet JS conditions | SPS expires, not replaced; MSD must invite JS application | s 33(3) |
| SP-25 | as SP-23, date 2026-11-04 | SPS continues (no expiry) | s 33(2) "On the date that the youngest dependent child ... turns 14" |
| SP-26 | two children, older turns 14 on 2026-11-05, younger aged 9 | no expiry (youngest not 14) | s 33(2) "youngest" |

### Supported living payment (ss 34-36, 40)

Baseline SLP: general requirements met; aged 40; health condition expected to continue for at least the regulation period (permanent); incapable of regularly working 15 hours a week; not blind; not self-inflicted.

| id | inputs | expected | provision |
|---|---|---|---|
| SL-01 | baseline | entitled | s 34, s 35 |
| SL-02 | permanent; capable of regularly working 15 hours a week (incapable only of 20) | not entitled (not severely restricted) | s 35(3) "incapable of regularly working at least 15 hours a week" |
| SL-03 | permanent; can work at most 14 hours a week | entitled | s 35(3) |
| SL-04 | severe but not permanent (expected shorter than the regulation period, not terminal) | not entitled | s 35(2) |
| SL-05 | not expected to live for that period, condition terminal; severe | entitled | s 35(2)(b) |
| SL-06 | totally blind, not otherwise restricted | entitled | s 34(a) "or is totally blind" |
| SL-07 | aged 16 exactly | entitled | s 34(c) "aged 16 years or over" |
| SL-08 | aged 15 | not entitled | s 34(c) |
| SL-09 | self-inflicted with a view to qualifying for a benefit | not entitled | s 36 |
| SL-10 | self-inflicted but NOT with a view to qualifying | entitled | s 36 "self-inflicted and brought about ... with a view to qualifying" |
| SL-11 | residential requirement not met | not entitled | s 34(b) |
| SL-12 | carer: full-time care at home of a parent who would otherwise need institutional care; aged 30; no dependent child | entitled | s 40(1) |
| SL-13 | carer: the cared-for person is the carer's spouse | not entitled | s 40(1)(a) "and who is not C's spouse or partner" |
| SL-14 | carer: cared-for person would not otherwise need institutional care | not entitled | s 40(1)(a) |
| SL-15 | carer aged 18, no dependent child | entitled | s 40(1)(c)(i) |
| SL-16 | carer aged 17, no dependent child | not entitled | s 40(1)(c)(i) |
| SL-17 | carer aged 19 with dependent child | not entitled | s 40(1)(c)(ii) |
| SL-18 | carer aged 20 with dependent child | entitled | s 40(1)(c)(ii) |
| SL-19 | carer, residential requirement not met | not entitled | s 40(1)(b) |
| SL-20 | carer, care stopped 20 days ago; MSD continues the payment | continues (discretion) | s 40(2): **not expressible** as an entitlement-on-application test, because it is a discretion about continuing a payment already granted |

## Goal 3: Rates and commencement

### Income tests (Sch 2), applied to a base rate B

| id | test, B, total weekly income | expected rate | provision |
|---|---|---|---|
| RT-01 | IT1, 521.52, $160 | 521.52 | IT1 "more than $160" |
| RT-02 | IT1, 521.52, $250 | 494.52 (reduction 27.00) | IT1 30c over $160 up to $250 |
| RT-03 | IT1, 521.52, $300 | 459.52 (27 + 35) | IT1 "70 cents for every $1 ... more than $250" |
| RT-04 | IT1, 521.52, $200 | 509.52 | IT1 |
| RT-05 | IT2, 400, $160 | 400.00 | IT2 |
| RT-06 | IT2, 400, $250 | 386.50 (13.50) | IT2 15c |
| RT-07 | IT2, 400, $350 | 351.50 (13.50 + 35) | IT2 35c over $250 |
| RT-08 | IT3, 400, $160 | 400.00 | IT3 |
| RT-09 | IT3, 400, $250 | 337.00 (63) | IT3 70c over $160 |
| RT-10 | IT4, 400, $160 | 400.00 | IT4 |
| RT-11 | IT4, 400, $250 | 368.50 (31.50) | IT4 35c over $160 |
| RT-12 | IT1, 342, $700 | 0.00 | IT1, floor (R3) |
| RT-13 | IT1, 342, $1000 | 0.00 (not negative) | R3 |
| RT-14 | IT1, 521.52, $0 | 521.52 | IT1 |
| RT-15 | IT3, 400, $1000 | 0.00 | R3 |

### Sole parent support rate (Sch 4 Pt 2)

| id | inputs | expected weekly rate | provision |
|---|---|---|---|
| RS-01 | personal earnings $0, partner $0 | 521.52 | Sch 4 Pt 2 cl 1 "$521.52 a week, subject to Income Test 1" |
| RS-02 | earnings $160 | 521.52 | cl 1 + IT1 |
| RS-03 | earnings $250 | 494.52 | cl 1 + IT1 |
| RS-04 | earnings $180, childcare $20, MSD applies disregard | 521.52 (counted income $160) | cl 2 "may disregard up to $20" |
| RS-05 | earnings $180, childcare $30, disregard applied | 521.52 (capped at $20 → $160) | cl 2 "up to $20" |
| RS-06 | earnings $180, childcare $10, disregard applied | 518.52 (counted $170 → reduction 3) | cl 2 (R7) |
| RS-07 | earnings $270, childcare $20, disregard applied | 494.52 (counted $250) | cl 2 + IT1 |
| RS-08 | earnings $270, childcare $20, NOT applied | 480.52 (27 + 14) | IT1 |

### Jobseeker support and SLP rate (inputs per R4)

| id | inputs | expected | provision |
|---|---|---|---|
| RJ-01 | JS, B 342, IT1, income $250 | 315.00 | s 17, Sch 4 Pt 1 (input), IT1 |
| RJ-02 | JS, B 342, IT1, income $400 | 210.00 (27 + 105) | IT1 |
| RJ-03 | SLP, B 420, IT1, income $160 | 420.00 | Sch 4 Pt 3 (input) |
| RJ-04 | SLP, B 420, IT2 (my choice), income $250 | 406.50 | IT2 |
| RJ-05 | JS, B 342, IT1, own $200 + partner $100 = $300 | 280.00 (27 + 35) | IT1 "total income of the beneficiary and the beneficiary's spouse or partner" |

### Commencement (ss 313-316)

Stand-down length N = 7 days throughout (input, s 316(1)(b)), with R8 arithmetic.

| id | benefit and inputs | expected | provision |
|---|---|---|---|
| CM-01 | SPS; entitled 2027-03-01; applied 2027-03-05; no employment end | stand-down starts 2027-03-01; commences 2027-03-08 | s 316(1)(a)(i), (2)(a) |
| CM-02 | SPS; entitled 2027-03-01; employment ceased 2027-03-03 before applying 2027-03-10 | starts 2027-03-04; commences 2027-03-11 | s 316(1)(a)(ii) "the day after the date on which the person's employment ceased" |
| CM-03 | SPS; entitled 2027-03-01; employment ceased 2027-02-20 (before entitlement); applied 2027-03-02 | starts 2027-03-01 (later of 03-01 and 02-21); commences 2027-03-08 | s 316(1)(a) "later of" |
| CM-04 | SPS; entitled 2027-03-01; applied 2027-03-02; employment ended 2027-03-10, AFTER applying, with no notice before applying | starts 2027-03-01 (employment limb not engaged); commences 2027-03-08 | s 316(1)(a)(ii) "if, before the person applied" |
| CM-05 | SPS; entitled 2027-03-01; notice of termination given 2027-02-15 before applying 2027-03-02; employment ceased 2027-03-12 | starts 2027-03-13; commences 2027-03-20 | s 316(1)(a)(ii) "or the person is given notice of termination" |
| CM-06 | SPS; entitled 2027-03-01; applied 2027-03-29 (day 28) | commences 2027-03-08 (before the application date) | s 316(2) "within 28 days after" (R9) |
| CM-07 | SLP; entitled 2027-03-01; applied 2027-03-20 | 2027-03-08 | s 316(2)(b) |
| CM-08 | JS on health ground; entitled 2027-03-01; applied 2027-03-20 | 2027-03-08 | s 316(2)(c) |
| CM-09 | JS granted to a sole parent; same dates | 2027-03-08 | s 316(2)(d) |
| CM-10 | JS to a person to whom s 30(e) applies; same dates | 2027-03-08 | s 316(2)(d) |
| CM-11 | JS to a person recently losing a partner's support (death or separation); same dates | 2027-03-08 | s 316(2)(e) |
| CM-12 | ordinary work-tested JS; entitled 2027-03-01; applied 2027-03-20 | 2027-03-20 (later of 03-08 and 03-20) | s 316(3)(b) |
| CM-13 | ordinary JS; entitled 2027-03-01; applied 2027-03-03 | 2027-03-08 | s 316(3)(a) |
| CM-14 | ordinary JS; entitled 2027-03-01; applied 2027-03-08 | 2027-03-08 | s 316(3) (both equal) |
| CM-15 | ordinary JS; employment ceased 2027-03-05 before applying 2027-03-06; entitled 2027-03-01 | starts 2027-03-06; ends 03-12; commences 2027-03-13 | s 316(1)(a)(ii), (3) |
| CM-16 | ordinary JS applied 2027-04-15 (well after 28 days), entitled 2027-03-01 | 2027-04-15 | s 316(3)(b) |
| CM-17 | SPS; stand-down N = 14 days; entitled 2027-03-01; applied 2027-03-02 | 2027-03-15 | s 316(1)(b), (2) |
| CM-18 | year boundary: SPS entitled 2027-12-28, N 7, applied 2027-12-29 | 2028-01-04 | s 316(2) |
| CM-19 | leap year: SPS entitled 2028-02-25, N 7, applied 2028-02-26 | 2028-03-03 | s 316(2) |
| CM-20 | SPS; entitled 2027-03-01; applied 2027-03-30 (day 29) | **ambiguous**: s 316(2) is not met and s 316(3) is literally inapplicable. I expect REFUSE (R10) | s 316(2), (3) |
| CM-21 | SLP; entitled 2027-03-01; applied 2027-05-01 | same as CM-20: REFUSE expected | s 316 |
| CM-22 | JS with non-entitlement period (not s 314(1) case); entitled 2027-03-01; applied 2027-03-05 | commences 2027-03-05 with no stand-down | s 314(2) "later of ... entitled ... application ... received" |
| CM-23 | which benefits are subject to stand-down: SPS, SLP, JS-health | all subject | s 313(b) |
| CM-24 | s 315 regulations exempt benefit | not subject; commencement per regs | s 315: **not expressible** (regulations not in source) |
| CM-25 | s 316(4) delayed redundancy / seasonal workers | **not expressible** (regulations) | s 316(4) |

## Top-level goal

| id | inputs | expected |
|---|---|---|
| TOP-01 | SPS baseline (SP-01), earnings $250, entitled 2027-03-01, applied 2027-03-05, N 7 | entitled; $494.52; commences 2027-03-08 |
| TOP-02 | JS baseline (JS-01), income $400, entitled 2027-03-01, applied 2027-03-20, N 7 | entitled; $210.00; commences 2027-03-20 |
| TOP-03 | SLP baseline, income $0, B 420 IT1, entitled 2027-03-01, applied 2027-03-10 | entitled; $420.00; commences 2027-03-08 |
| TOP-04 | JS baseline but on a temporary visa | not entitled |

## Not expressible (from the outset)

- SL-20 (s 40(2) continuation discretion), CM-24 (s 315), CM-25 (s 316(4)). Also s 31 (MSD regarding a child as the applicant's), unless the encoding has an input for it.
- The discretions in s 33(4)-(5), which carry obligations over.
