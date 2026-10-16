# Independent expectations: NZ Superannuation and Retirement Income Act 2001

Written from the Act (version as at 10 July 2026) and BRIEF.md only, before
any `.l4` module was opened. Each scenario gives the facts, the expected answer
and the words that give it. "TTR" = total time requirement. Periods are given
in years unless said otherwise; a "year" of residence is taken as 365 days
where days are needed. Rates are inputs: unless stated, the Schedule 1 rates
used are 1(a) single living alone = 600, 1(b) single sharing = 550,
1(c) married/partnered (each) = 450, clause 3 hospital rate = 300.

## A. Age (s 7)

| # | Facts | Expected | Authority |
|---|---|---|---|
| A1 | Born 1 Jan 1961; date 1 Jan 2026 (65th birthday) | meets age | s 7(1) "attains the age of 65 years" |
| A2 | Born 1 Jan 1961; date 31 Dec 2025 | does not meet age | s 7(1) |
| A3 | Born 29 Feb 1960; date 28 Feb 2025 | not 65 (birthday treated as 1 Mar in non-leap year under NZ convention; Act silent) | s 7(1); ambiguous. Best reading: attains 65 on 1 Mar 2025 (Age of Majority/Interpretation practice: a person attains an age at the start of the anniversary; for 29 Feb, 1 Mar). A date of 1 Mar 2025 meets age. |
| A4 | Born 1 Jan 1961; date 1 Jan 2030 (69) | meets age | s 7(1); no upper limit |
| A5 | Aged 66, has an election in force under Sch 1AA cl 5(4) ACC Act to take weekly compensation | not entitled for that period | s 7(2) "not entitled ... in respect of the period for which the person has made an election" |
| A6 | Aged 66, Veterans' Support Act Sch 1 cl 16(3) election | not entitled for that period | s 7(2)(b) |
| A7 | Aged 66, no election, meets residence | entitled | s 7(1), s 8 |
| A8 | Aged 64, election in force | not entitled (age fails anyway) | s 7(1) |

## B. Residence (s 8)

| # | Facts | Expected | Authority |
|---|---|---|---|
| B1 | TTR 20; NZ 20; realm 0; since-50 5; ordinarily resident on application | meets | s 8(1),(2),(3) |
| B2 | TTR 20; NZ 10; Cook Is/Niue/Tokelau 10; since-50 5 | meets | s 8(2)(a) "in New Zealand for 10 years", (b) "remaining time ... Cook Islands, Niue, and Tokelau" |
| B3 | TTR 20; NZ 9.9; realm 15 (total 24.9) | fails: NZ under 10 years | s 8(2)(a) |
| B4 | TTR 20; NZ 15; realm 4.9 (total 19.9) | fails: total under TTR | s 8(2) "totalling not less than the total time requirement" |
| B5 | TTR 14 (example B in s 8); NZ 12, Cook Is 1, Niue 1; since-50 14 | meets | s 8 example |
| B6 | TTR 14; NZ 13.99, realm 0 | fails | s 8(2) |
| B7 | TTR 10; NZ 10, since-50 5 | meets | s 8(2) |
| B8 | TTR 20; NZ 25; since-50 4.99 | fails s 8(3) | s 8(3) "not less than 5 years" |
| B9 | TTR 20; NZ 25; since-50 exactly 5 (all in realm) | meets | s 8(3) "any 1 or more of New Zealand, the Cook Islands, Niue, and Tokelau" |
| B10 | Time in Samoa (Pacific country but not realm) 10 years counted toward remainder | does not count; with NZ 10 and Samoa 10, TTR 20 → fails | s 8(2)(b) lists only NZ, Cook Is, Niue, Tokelau |
| B11 | Meets 8(2),(3), not ordinarily resident in NZ on application, s 31(4) not applying | not entitled | s 8(1)(a) |
| B12 | Meets 8(2),(3), resident in Niue on application, applies under s 31(4) | the ordinary-residence requirement is excused | s 8(1)(a) "unless section 31(4) ... applies" |
| B13 | Time treated as residence under s 9/10/10A (CE satisfied): NZ actual 8 + treated 2 = 10, TTR 10 | meets | ss 9-10A "must be treated as having been both resident and present in New Zealand" |

## C. Refugees (s 8A)

| # | Facts | Expected | Authority |
|---|---|---|---|
| C1 | Refugee, aged 44 on relevant date; s 8(4) TTR 20 | TTR 20 (s 8A does not apply) | s 8A(1)(b) "45 years of age or older" |
| C2 | Refugee, exactly 45 on relevant date; s 8(4) TTR 20; days to 65th birthday = 20 years | TTR = lesser = 20 years | s 8A(3) |
| C3 | Example: born 1 Jan 1975, relevant date 1 Jan 2025 (50); s 8(4) TTR 20 | TTR = days 1 Jan 2025 → 1 Jan 2040 = 5478 days (15 years) | s 8A(3)(a), example |
| C4 | Refugee aged 54 on relevant date (born 1 Jan 1971, relevant date 1 Jan 2025); 8(4) TTR 20 | TTR = 1 Jan 2025 → 1 Jan 2036 = 4017 days (~11 years) | s 8A(3)(a) |
| C5 | Refugee exactly 55 on relevant date | TTR 10 years | s 8A(4) "55 years of age or older" |
| C6 | Refugee aged 70 on relevant date | TTR 10 years | s 8A(4) |
| C7 | Not a refugee, aged 55 on relevant date, 8(4) TTR 20 | TTR 20 | s 8A(1)(a) |
| C8 | Refugee aged 50, 8(4) TTR 12 (shorter than 15 years to 65) | TTR 12 years | s 8A(3)(b) lesser |
| C9 | Relevant date is date first both resident and present, even if refugee recognition came later | age measured at first resident-and-present date | s 8A(5) |
| C10 | Refugee aged 55 on relevant date, NZ 10 years, since 50 10 | meets s 8(2),(3) | s 8A(4), s 8 |

Ambiguity: s 8A(3)(a) is "calculated in days" while the s 8(4) table is in
years. Comparison needs a common unit; I take 1 year = 365 days is NOT what the
Act says; the natural reading is to compare the actual day count of the period
with the date at which the 8(4) requirement would be met, i.e. calendar years.
The tests compare lengths and accept either representation if the encoding
reports the lesser one.

## D. Commencement (s 11)

| # | Facts | Expected | Authority |
|---|---|---|---|
| D1 | Entitled 1 Mar 2026, application received 10 Mar 2026 | 10 Mar 2026 | s 11(1) "whichever is the later" |
| D2 | Application received 1 Feb 2026 (in advance), entitled 1 Mar 2026 | 1 Mar 2026 | s 11(1) |
| D3 | Both same day 1 Mar 2026 | 1 Mar 2026 | s 11(1) |

## E. Living alone (s 4A)

| # | Facts | Expected | Authority |
|---|---|---|---|
| E1 | Single, house, nobody else | living alone | s 4A(2)(a),(3) |
| E2 | Married person in house alone | not "living alone" (definition is of a single person) | s 4A(1) "A single person" |
| E3 | Single, house, shares with adult (30) lodger | not living alone | s 4A(3) |
| E4 | Single, shares with 17-year-old grandchild | living alone | s 4A(3) "18 years old or older" |
| E5 | Single, shares with dependent child aged 18, not financially independent, at school, before 31 Dec of year turning 18 | living alone | s 4A(4) |
| E6 | As E5 but on 1 Jan of the year after the child turned 18 | not living alone | s 4A(4)(b) "only until the close of 31 December" |
| E7 | As E5 but child financially independent | not living alone | s 4A(4)(a)(ii) |
| E8 | As E5 but child not at school/tertiary | not living alone | s 4A(4)(a)(iii) |
| E9 | Dependent child aged 19 at university | not living alone | s 4A(4)(a)(i) "is 18 years old" |
| E10 | Temporary visitor staying 12 weeks in a 26-week period | living alone | s 4A(5) "less than 13 weeks" |
| E11 | Temporary visitor staying exactly 13 weeks | not living alone | s 4A(5) |
| E12 | Boat moored in NZ territorial sea | qualifying accommodation | s 4A(2)(b) |
| E13 | Mobile home, CE not satisfied it is self-contained | not living alone | s 4A(2)(f) |
| E14 | Mobile home, CE satisfied | living alone | s 4A(2)(f) |
| E15 | Rest home room (not a listed kind, no regulations) | not living alone | s 4A(2) closed list |
| E16 | Hotel room / boarding house room / caravan park unit | qualifying | s 4A(2)(c)-(e) |

## F. Rate category (s 12, Sch 1, ss 17-19)

| # | Facts | Expected | Authority |
|---|---|---|---|
| F1 | Single living alone | Sch 1 cl 1(a) = 600 | s 12, Sch 1 |
| F2 | Single not living alone | 1(b) = 550 | Sch 1 |
| F3 | Married, partner also qualified | 1(c) = 450 | Sch 1 |
| F4 | Partner in long-term residential care in rest home; person entitled in own right, living alone | single living alone rate 600 | s 17(2)(a), s 18 |
| F5 | As F4, person not living alone | single rate: 1(b) 550 | s 17(2)(a) "appropriate rate payable to a person who is single" |
| F6 | Partner in LTRC; person not entitled in own right; partner made pre-1 Oct 1991 election | NZS at single rate | s 17(2)(b) |
| F7 | Partner in LTRC; person not entitled in own right; no election | not NZS (emergency benefit) | s 17(2)(c) |
| F8 | Single, hospital 13 weeks exactly (91 days) | rate unaffected 600 | s 19(3) "13 weeks or less" |
| F9 | Single, hospital 92 days (into 14th week) | hospital rate 300 | s 19(4) "on and after the commencement of the 14th week" |
| F10 | Single, hospital 20 weeks, resident assessed as requiring care, funder paying contracted care | s 19(4) does not apply: rate unaffected | s 19(6) |
| F11 | Married with dependent children, hospital 20 weeks | s 19 does not apply: rate unaffected 450 | s 19(2) "who has no dependent children" |
| F12 | Married no children, hospital 20 weeks | hospital rate 300 | s 19(2),(4) |
| F13 | Hospital rate reduced; absent from hospital 28 days, returns | rate on return as if absence had not occurred (still hospital rate) | s 19(9) "not more than 28 days" |
| F14 | Absent 29 days, returns | s 19(9) does not apply; new stay: 13-week rule restarts, rate unaffected | s 19(9) |
| F15 | CE pays higher rate after regard to finances | CE discretion permits > 300 | s 19(5) |
| F16 | Married person reduced under s 19; spouse's specified benefit | spouse increased by single max − partnered max | s 19(7),(7A) |
| F17 | As F16 but spouse in hospital > 13 weeks too | no increase | s 19(8) |
| F18 | Spouse in hospital 13 weeks exactly | increase applies | s 19(8) "more than 13 weeks" |
| F19 | Hospital means a Health NZ hospital; private hospital stay 20 weeks | s 19 not engaged | s 19(1) |

## G. Temporary absences (ss 21-25)

| # | Facts | Expected | Authority |
|---|---|---|---|
| G1 | Absent 10 weeks | payable throughout | s 22(a) |
| G2 | Absent exactly 30 weeks; week 20 | payable | s 22(a) "does not exceed 30 weeks" |
| G3 | Absent 30 weeks; week 27 | not payable (only first 26) | s 22 "first 26 weeks" |
| G4 | Absent 31 weeks, no CE satisfaction; week 5 | not payable | s 22(b) |
| G5 | Absent 31 weeks, CE satisfied beyond control and unforeseen; week 5 | payable | s 22(b) |
| G6 | As G5, week 28 | not payable | s 22 |
| G7 | Receiving NZS overseas under s 26 | s 22 does not apply | s 22 "(other than a person who is receiving ... under section 26)" |
| G8 | Absent 2 years for own MoH-assisted treatment | CE may pay | s 23 |
| G9 | Absent 2 years + 1 day for medical treatment | s 23 not available | s 23 "not exceeding 2 years in total" |
| G10 | Absent for sibling's MoH-assisted treatment, 1 year | CE may pay | s 23 "sibling" |
| G11 | Absent for parent's treatment | s 23 not available | s 23 closed list |
| G12 | Absent for treatment without MoH assistance | not available | s 23 |
| G13 | Aid work 156 weeks, unpaid full-time humanitarian, recognised agency, no displacement | CE may pay | s 24 |
| G14 | Aid work 157 weeks | not available | s 24(1)(b) |
| G15 | Aid agency deprived another of paid employment | not available | s 24(1)(c)(ii) |
| G16 | Would have reached 65 while abroad on 1 Mar 2026 | absence regarded as commencing 1 Mar 2026 | s 25 |

## H. Overseas proportion (ss 26, 26A, 26B, 28)

| # | Facts | Expected | Authority |
|---|---|---|---|
| H1 | Resided 540 months aged 20-65 | proportion 1 | s 26A(1)(d) "dividing by 540" |
| H2 | 270 months | 1/2 | s 26A |
| H3 | 120 months + 29 days | 120/540 = 2/9 | s 26A(1)(b) "disregarding any remainder" |
| H4 | 120 months + 30 days | 121/540 | s 26A(1)(b) |
| H5 | Two periods: 100m 20d and 100m 20d | 201/540 | s 26A(1)(a)-(c) days summed then ÷30 |
| H6 | 120 months + 61 days | 122/540 | s 26A |
| H7 | Single, proportion 1/2 | 1/2 × 1(b) = 275 | s 26(6)(a) "amount stated in clause 1(b)" (not 1(a) even if living alone) |
| H8 | Married, proportion 1/2 | 1/2 × 1(c) = 225 | s 26(6)(b) |
| H9 | Single living alone, proportion 1 | 550 (1(b), not 600) | s 26(6)(a) |
| H10 | Intends to reside 40 weeks in a non-reciprocity country | s 26 applies | s 26(1)(b)(i) "longer than 26 weeks" |
| H11 | Intends 26 weeks exactly | s 26 does not apply | s 26(1)(b)(i) |
| H12 | Intends > 52 weeks in Samoa (specified Pacific) | s 26 does not apply (s 31) | s 26(1)(b)(i) "but not intending to reside for a period longer than 52 weeks in a specified Pacific country" |
| H13 | Intends to reside 40 weeks in Fiji (Pacific, ≤ 52) | s 26 applies | s 26(1)(b)(i) |
| H14 | Intends to travel 30 weeks, not reside anywhere | s 26 applies | s 26(1)(b)(ii) |
| H15 | Reciprocity country (e.g. one with an agreement under SSA s 380) | s 26 does not apply | s 26(1)(a) |
| H16 | No application made under s 26 | not entitled | s 26B(a) |
| H17 | Application made while not ordinarily resident and present | not entitled | s 26B(b) |
| H18 | Applied while 64, will turn 65 before leaving | entitled | s 26B(b)(ii) |
| H19 | Departure 10 Mar 2026 | commencement = first pay day after departure | s 28(1) |
| H20 | Time treated as residence under s 9 counts in proportion | counts | s 26A(2) |
| H21 | Residence before 20 or after 65 | excluded | s 26A(1)(a) "aged 20 or more and less than 65" |

## I. Pacific rate (ss 31, 32, 33)

Base rate: single = 1(b) 550; partnered = 1(c) 450 (s 32(2)).

| # | Facts | Expected | Authority |
|---|---|---|---|
| I1 | Single, 20 years since 20 | 550 | s 32(1)(a) |
| I2 | Single, 30 years | 550 | s 32(1)(a) "20 or more" |
| I3 | Single, 10 years | 550 × 10/20 = 275 | s 32(1)(b) |
| I4 | Single, 15 whole years | 550 × 15/20 = 412.5 | s 32(1)(b) |
| I5 | Single, 15.9 years | uses whole number 15: 412.5 | s 32(1)(b) "whole number of years" |
| I6 | Single, 19.99 years | 550 × 19/20 = 522.5 | s 32(1)(b) "fewer than 20" |
| I7 | Partnered, 12 years | 450 × 12/20 = 270 | s 32(1)(b),(2)(b) |
| I8 | Single, 9 years | Act gives no rate: refuse / not payable | s 32(1) silent below 10 (s 8(2)(a) would normally already bar) |
| I9 | Pre-1999 recipient paid 500, now would get 412.5 | 500 (higher) | s 32(1)(c) |
| I10 | Pre-1999 recipient paid 300, now 550 | 550 | s 32(1)(c) |
| I11 | SSA ss 187-191 deduction 50 from single base | base 500 | s 32(3) |
| I12 | Intends to reside > 52 weeks in Tonga, resident & present on application, entitled | s 31(2) applies | s 31(2) |
| I13 | Intends exactly 52 weeks | s 31(2) does not apply | s 31(2)(a) "more than 52 weeks" |
| I14 | Resident in Cook Is on application, met s 8(2),(3) | s 31(4) applies | s 31(4) |
| I15 | Resident in Samoa on application (not realm) | s 31(4) does not apply | s 31(4)(b) |
| I16 | s 31(4): age met 1 Mar 2026, application 1 Jun 2026 | commencement 1 Jun 2026 | s 33(1A) later |
| I17 | s 31(4): application 1 Jan 2026, age met 1 Mar 2026 | 1 Mar 2026 | s 33(1A) |
| I18 | Ceases to be resident in a Pacific country when a payment is due | not payable | s 31(2)(d) |

## J. End of overseas payment on death (ss 29(2), 33(2))

| # | Facts | Expected | Authority |
|---|---|---|---|
| J1 | s 26 recipient dies 1 Mar 2026; CE picks 29 Mar 2026 (28 days) | permitted | s 29(2)(b) "not more than 4 weeks" |
| J2 | CE picks 30 Mar 2026 (29 days) | not permitted | s 29(2)(b) |
| J3 | CE picks date of death | permitted | s 29(2) |
| J4 | s 31 recipient dies 1 Mar 2026; termination 29 Mar | permitted | s 33(2) |
| J5 | s 31 recipient, termination 30 Mar | not permitted | s 33(2) |
| J6 | CE picks a date before death | Act says "not more than 4 weeks after"; best reading: date must be on/after death; ambiguous | s 29(2) |

## K. Annual adjustment and s 16 relationships

| # | Facts | Expected | Authority |
|---|---|---|---|
| K1 | Net couple amount 700 vs net avg wage 1000 (70%) | within band | s 16(a) 66%-72.5% |
| K2 | 660 vs 1000 | within (66% inclusive) | s 16(a) "not less than 66%" |
| K3 | 725 vs 1000 | within (72.5% inclusive) | s 16(a) "or more than 72.5%" |
| K4 | 659 vs 1000 | below band | s 16(a) |
| K5 | 726 vs 1000 | above band | s 16(a) |
| K6 | Couple net amount 1000 | single living alone net = 650 | s 16(b) 65% |
| K7 | Couple net 1000 | single sharing net = 600 | s 16(c) 60% |
| K8 | CPI moved +2%, net rate 500 | new net 510 | s 15(2) |
| K9 | CPI moved −1% | no reduction: 500 | s 15(2) "percentage movement upwards", s 15(4) |

Note: the "couple" amount in s 16 is the amount payable to the couple (both
qualified), i.e. the combined amount, so per-person 1(c) is half of it.

## L. Fund (ss 43, 44, 47, 71)

| # | Facts | Expected | Authority |
|---|---|---|---|
| L1 | Percentage 0.05 (5%), GDP 400,000, net cost 15,000 | 5,000 | s 43 read as P × GDP − NC |
| L2 | 3%, GDP 400,000, NC 15,000 | −3,000 | s 43 |
| L3 | 0%, GDP 400,000, NC 0 | 0 | s 43 |
| L4 | Required 5,000; Government intends to pay 4,000 | s 44 statement required | s 44(1) |
| L5 | Required 5,000; intends 5,000 | not required | s 44(1) "less ... than" |
| L6 | Required −3,000; intends 0 | not required | s 44(2) "less than zero" |
| L7 | Required 0; intends 0 | not required | s 44(1) |
| L8 | Required −3,000; FY commencing 1 Jul 2021 | withdrawal up to 3,000 allowed | s 47(1) |
| L9 | Required −3,000; FY commencing 1 Jul 2019 | no withdrawal | s 47(2) "commencing before 1 July 2020" |
| L10 | Required −3,000; FY commencing 1 Jul 2020 | allowed (up to 3,000) | s 47(2) |
| L11 | Required +5,000 | no withdrawal | s 47(1) |
| L12 | Required 0 | no withdrawal | s 47(1) "less than zero" |
| L13 | Proposed withdrawal 3,500 against required −3,000 | exceeds limit | s 47(1) "up to that amount" |
| L14 | Previous review 1 Jul 2020, next 1 Jul 2025 | complies (no more than 5 years) | s 71(3) |
| L15 | Previous 1 Jul 2020, next 2 Jul 2025 | breach | s 71(3) |
| L16 | Previous 1 Jul 2020, next 30 Jun 2025 | complies | s 71(3) |

## M. Overall entitlement (goal)

| # | Facts | Expected | Authority |
|---|---|---|---|
| M1 | 66, single living alone in NZ, TTR 20 met, since-50 met, no election | entitled, rate 600 | ss 7, 8, 12, Sch 1 |
| M2 | 64, otherwise as M1 | not entitled | s 7 |
| M3 | 66, NZ 9 years | not entitled | s 8(2)(a) |
| M4 | 66, absent overseas 40 weeks without s 26 application, no CE satisfaction | not payable while absent (after 26 weeks rules) | ss 21, 22 |

## Cannot be decided from the Act alone

- The s 8(4) table values (lost; input).
- Whether the s 8A day-count is compared with the s 8(4) years in calendar
  years or 365-day years (C2-C4 chosen so either reading gives the same lesser
  value where possible).
- s 32 below 10 years: no rate given; I expect a refusal.

## Added before running the tests (still from the Act)

| # | Facts | Expected | Authority |
|---|---|---|---|
| D4 | The s 8 example person B (born 30 Jun 1967, 65 on 30 Jun 2032) first meets the TTR on 1 Jul 2036; application received 1 Jan 2036 | commences 1 Jul 2036, the date B "becomes entitled" (later than the application) | s 11(1), s 8 example |
| C4c | Refugee born 2 Jan 1970, relevant date 1 Jan 2025 (54, one day short of 55); NZ 10 | s 8A(3) applies: TTR is about 11 years, so 10 years fails | s 8A(3) "younger than 55 years" |
| L17 | Last performance review 29 Feb 2024 | next due no later than 28 Feb 2029 | s 71(3); 5-year period ends on the last day of the month where there is no corresponding day |
| F12b | Single person with dependent children, 20 weeks in hospital | hospital rate (s 19(2) children limit is for couples only) | s 19(2) |

## Scenarios the encoding cannot express (phase 2)

- E4-E14, E16: s 4A's exceptions (dependent student child until 31 Dec of the
  year they turn 18; visitor under 13 weeks in 26; the kinds of accommodation,
  the boat waters, the mobile home test) are collapsed into two booleans on
  `Household`; only the result can be tested.
- A3: the encoding's age uses `add years`, which takes a 29 Feb birthday to 28
  Feb in a common year (a different reading from mine; see report).
- B12: no input for s 31(4) excusing ordinary residence on application.
- B13, C9, H20, H21: periods treated as residence and the date rules are
  folded into numeric inputs.
- F6, F7: s 17(2)(b)/(c) (not entitled in own right; pre-1991 election;
  emergency benefit) are not represented.
- F13, F14: the s 19(9) 28-day absence from hospital rule is not represented
  (only "weeks in hospital").
- F15-F19: s 19(5) discretion, s 19(7)-(8) spouse increase, s 19(1) meaning of
  hospital: not represented.
- G7: s 22 exclusion of s 26 recipients; G10, G11: who the medical treatment is
  for (s 23 list); G15: s 24 displacement condition; G16: s 25.
- H7-H9: no function computes the s 26(6) amount (proportion × 1(b) or 1(c));
  the test multiplies by hand. H10-H19: s 26 applicability, s 26B and s 28 are
  not encoded.
- I9, I10: s 32(1)(c) pre-1999 "higher of" not encoded. I11: s 32(3) reduction
  only via the base-rate argument. I12-I18: s 31 applicability and s 33(1),(1A)
  commencement not encoded.
- J6: a termination date before death.
- K8, K9: s 15 CPI adjustment not encoded.
- L13: the withdrawal limit is returned, but there is no check of a proposed
  amount (testable by comparison only).
- M4: the goal ignores absence entirely.
