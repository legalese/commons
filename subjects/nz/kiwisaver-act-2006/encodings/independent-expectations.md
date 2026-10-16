# Independent expectations: KiwiSaver Act 2006 (as at 1 April 2026)

Written from the statute and BRIEF.md alone, before any `.l4` module was opened.
Each scenario gives the facts, the expected answer, and the provision. Ids (M = membership,
C = contributions, W = withdrawals) are reused in `tests-independent.l4` comments.

Default facts unless stated: NZ superannuation qualification age (NZSQA) = 65; the person lives
in NZ and is a NZ citizen; the employer is a NZ resident, not exempt; the employment is permanent
and new; the person is not already a member.

## Conventions I adopt for days and dates

- "the Nth day after date D" = D + N (s 16, s 17(4), s 12(2)(b), s 51(4)). So for a start on
  1 March 2026: the 13th day after = 14 March; the 55th day after = 25 April; the 28th day after =
  29 March.
- "within 7 days of starting" (s 42, s 18(1)(b)(i)) = on or before start + 7.
- "the period that ends 92 days after" first contribution (s 18(2)) includes first + 92.
- "more than 62 days have passed since" (s 48(1)(d)) first applies on first + 63.
- "less than 92 days apart" / "for less than 92 days" (ss 64(6), 101S(2), 108(2)): exactly 92 days
  is permitted, 91 is not.
- "within 92 days of giving" (s 112B(3)): AMBIGUOUS. My reading: a revocation given on or before
  given + 92 is within the 92 days (forbidden without agreement); given + 93 is allowed.
- "after 12 months have expired since D" (s 102(b)): AMBIGUOUS on the anniversary. The day of D is
  excluded (Legislation Act 2019 rule that a period after a day excludes that day), so 12 months
  expire at the end of the anniversary; the first day one may apply is the day after it. Clear
  sides: anniversary − 1 = no; anniversary + 1 = yes.
- "at least 3 years have expired after" first contribution (cl 8(1)(a)): same reading — clear
  sides are anniversary − 1 (no) and anniversary + 1 (yes); on the anniversary itself I read no.
- "no earlier than 1 year after" emigration (cl 14(1)): the anniversary itself is permitted
  ("no earlier than"), the day before is not.
- Ages: a person "is aged 18 years or more" from their 18th birthday; they reach NZSQA on their
  65th birthday (cl 4(2) "on and after the date on which the member reaches").

## Part 1 — application (s 6)

| id | facts | expected | provision |
|---|---|---|---|
| M1 | lives in NZ, NZ citizen | Act applies | s 6(1)(a),(b) |
| M2 | lives in NZ, not a citizen but entitled to be in NZ indefinitely | applies | s 6(1)(b) "entitled ... to be in New Zealand indefinitely" |
| M3 | lives in NZ on a temporary work visa | does NOT apply | s 6(1)(b) fails |
| M4 | NZ citizen normally living in Australia, private employer | does NOT apply | s 6(1)(a) fails |
| M5 | NZ citizen, State services employee serving overseas, on NZ terms, in a jurisdiction where KiwiSaver offers are lawful | applies | s 6(1)(a)(i)-(iii) |
| M6 | as M5 but not employed on NZ terms and conditions | does NOT apply | s 6(1)(a)(ii) |
| M7 | as M5 but in a jurisdiction where offers are unlawful | does NOT apply | s 6(1)(a)(iii) |
| M8 | employer is NZ resident | Act applies to employer | s 6(2)(a) |
| M9 | non-resident employer with fixed establishment in NZ | applies | s 6(2)(b) |
| M10 | non-resident employer, no fixed establishment, does not choose | does NOT apply | s 6(2) |
| M11 | as M10 but employer chooses to apply the Act | applies | s 6(2)(c) |

## Automatic enrolment (ss 10-15)

| id | facts | expected | provision |
|---|---|---|---|
| M12 | aged 30, new permanent job, non-exempt employer | AE applies | s 10 |
| M13 | starts on their 18th birthday | AE applies | s 10(c)(i) "18 years or more" |
| M14 | starts the day before their 18th birthday | AE does NOT apply | s 10(c)(i) |
| M15 | aged 17 at start, turns 18 a week later in the same job | AE does not apply (age tested "when they start"); no later trigger | s 10(c) |
| M16 | starts the day before their 65th birthday (aged 64) | AE applies | s 10(c)(ii) "less than" NZSQA |
| M17 | starts on their 65th birthday | AE does NOT apply | s 10(c)(ii) |
| M18 | aged 40, employer is exempt | does NOT apply | s 10(a), s 146(1) |
| M19 | secondee on employer B's payroll | does NOT apply | s 10(b), s 11(3) |
| M20 | fixed-term contract of 28 continuous days | temporary, AE does NOT apply | s 12(1)(b) "28 continuous days or less" |
| M21 | fixed-term contract of 29 days | not temporary, AE applies from start | s 12(1)(b) |
| M22 | 28-day contract starting 1 Mar 2026, employment continues | AE applies, as if new employment started on 29 Mar 2026 | s 12(2)(b) "on the 28th day after the employee started" |
| M23 | casual agricultural worker; ceases to be one on 10 Jun 2026 | AE applies from 11 Jun 2026 | s 12(2)(a) "the day after" |
| M24 | employment described in Holidays Act s 28(1)(a)(ii) | temporary, AE does NOT apply | s 12(1)(c) |
| M25 | stays on the same payroll as immediately before | not new employment | s 11(1)(b) |
| M26 | new employer carries on the same business (amalgamation / going concern) | not new employment | s 11(1)(c), (2) |
| M27 | re-employed by the home employer at the end of a secondment | not new employment | s 11(1)(d) |
| M28 | employee only because receiving ACC payments (RD 5(1)(b)(iii)) | AE does NOT apply | s 14(1)(a)(i) |
| M29 | employee only because of parental leave payments | AE does NOT apply | s 14(1)(a)(vi) |
| M30 | employee only because of working-partner payments | AE does NOT apply | s 14(1)(a)(iii) |
| M31 | election day worker | AE does NOT apply | s 14(1)(b) |
| M32 | private domestic worker | AE does NOT apply | s 14(1)(b) |
| M33 | no PAYE deductions required | AE does NOT apply | s 14(1)(c) |
| M34 | PAYE withheld solely because ITA YD 1(7) applies | AE does NOT apply | s 14(1)(d) |
| M35 | already a KiwiSaver member | AE does NOT apply | s 14(2) |
| M36 | already a member: is the new employer to deduct? | yes, liable to deductions from new employment | s 15(1)(a)(ii), s 36(1)(a)(ii), s 146(2)(b) |
| M37 | aged 30 but does not live in NZ / not resident (s 6 fails) | AE does NOT apply (Act does not apply) | s 6(1) |

Note on M15: the brief's question "until when may they opt out" presupposes AE applies; s 10 tests
age only at the start date.

## Opting out (ss 16-21) — start date 1 March 2026

13th day after = 14 Mar 2026; close of 55th day after = 25 Apr 2026.

| id | facts | expected | provision |
|---|---|---|---|
| M38 | window | opens 14 Mar 2026, closes 25 Apr 2026 | s 16 |
| M39 | notice given 13 Mar 2026 (12th day) | outside the s 16 time limit — not a valid opt-out under s 17(1). AMBIGUITY: s 17(4)(a) suggests early receipt was contemplated; I read s 16/17(1) as controlling | s 16, 17(1) |
| M40 | notice given 14 Mar 2026 | within time | s 16 |
| M41 | notice given 25 Apr 2026 | within time | s 16 "close of the 55th day" |
| M42 | notice given 26 Apr 2026 | outside time (late) | s 16 |
| M43 | notice given to employer, received 20 Mar 2026 | takes effect 20 Mar 2026 | s 17(4) later of 14 Mar and receipt |
| M44 | notice given to Commissioner 20 Apr 2026, accepted 30 Apr 2026 | valid (given within time); takes effect 30 Apr 2026 | s 17(1), 17(4)(b)(i) |
| M45 | notice received by employer 14 Mar 2026 | takes effect 14 Mar 2026 | s 17(4) |
| M46 | effect of opt-out | person ceases to be a member on the effective date | s 20(1) |
| M47 | opted out of job A; later starts new job B | AE applies afresh to job B | s 21 |

### Late opt-out (s 18) — first contribution received by Commissioner 10 Apr 2026 (first + 92 = 11 Jul 2026)

| id | facts | expected | provision |
|---|---|---|---|
| M48 | late notice 1 May 2026; employer did not give info pack within 7 days | Commissioner MAY accept (discretion) | s 18(1)(b)(i), (2) |
| M49 | late notice received 11 Jul 2026 with a ground | may accept (period "ends 92 days after") | s 18(2) |
| M50 | late notice received 12 Jul 2026 with a ground | may NOT accept | s 18(2) |
| M51 | late notice, no s 18(1)(b) ground | no extension; Commissioner treats it as a savings suspension application if eligible | s 18(1), (3) |
| M52 | info pack supplied on day 7 (8 Mar) | ground (b)(i) NOT met | s 18(1)(b)(i), s 42(1)(a) |
| M53 | info pack supplied on day 8 (9 Mar) | ground (b)(i) met | s 18(1)(b)(i) |
| M54 | late notice; s 59A(b)(i) mistake occurred | ground met | s 18(1)(b)(v) |

## Opting in (ss 33-35)

| id | facts | expected | provision |
|---|---|---|---|
| M55 | aged 30, not a member, not subject to AE | may opt in (direct or via employer) | ss 33, 34(1) |
| M56 | already a member | may NOT opt in | s 33(a) |
| M57 | currently subject to AE | may NOT opt in | s 33(b) |
| M58 | aged 18, acting alone | may opt in | s 34 |
| M59 | aged 15, guardian contracts in the person's name | may opt in | s 35(2) |
| M60 | aged 15, acting alone | may NOT | s 35(1),(2) |
| M61 | aged 16, jointly with a guardian | may | s 35(3) |
| M62 | aged 17, alone, but has a guardian | may NOT | s 35(3) requires joint contract |
| M63 | aged 17, no guardian, alone | may | s 35(4) |
| M64 | aged 17, by notifying employer (s 34(1)(b)) | may NOT (under 18 may only opt in under s 35, which is direct contracting) | s 35(1) |
| M65 | aged 12 with an Oranga Tamariki guardian who contracts | may | s 35(5) |
| M66 | aged 17 with only an Oranga Tamariki guardian, jointly | may | s 35(3) |

## Information packs and allocation (ss 42, 48, 51)

| id | facts | expected | provision |
|---|---|---|---|
| M67 | AE employee starts 1 Mar 2026 | info pack due by 8 Mar 2026 | s 42(1)(a) |
| M68 | employee opts in via employer on 10 May 2026 | info pack due by 17 May 2026 | s 42(1)(b) |
| M69 | first contribution 10 Apr 2026; provisionally allocated; no own choice | final allocation date "as soon as practicable after" 11 Jun 2026 (62nd day after) | s 51(4)(a) |
| M70 | employer's chosen scheme effective; first contribution 10 Apr 2026 | s 48 first applies 12 Jun 2026 ("more than 62 days") | s 48(1)(d) |
| M71 | person in M69 chose own scheme before final allocation date | no default allocation | s 51(1) |
| M72 | dispute under s 212 underway on the final allocation date | date moves to the effective date of resolution notice | s 51(5) |

## Contribution rate and deduction (ss 60-66)

Gross pay $2,000 unless stated. Deduction = rate × gross (s 66). No rounding rule in the Act.

| id | facts | expected | provision |
|---|---|---|---|
| C1 | s 60 first applied 1 May 2026, no notice | 3.5%, $70 | s 64(1)(a)(i), s 66 |
| C2 | s 60 first applied 1 Mar 2009, no 8% notice | 4%, $80 | s 64(1)(aa) |
| C3 | s 60 first applied 1 Apr 2009 | 3.5% | s 64(1)(a)(i) "on or after 1 April 2009" |
| C4 | s 60 first applied 31 Mar 2009 | 4% | s 64(1)(aa) "before 1 April 2009" |
| C5 | chose 6% | 6%, $120 | s 64(2) |
| C6 | chose 10% | 10%, $200 | s 64(2) |
| C7 | chose 8% | 8%, $160 | s 64(1)(b), (2) |
| C8 | chose 4% (post-2009 starter) | 4%, $80 | s 64(2) |
| C9 | purported choice of 5% | not a notice "under subsection (2)" (rates 3.5, 4, 6, 8, 10 only), so s 64(1)(a)(i) still applies: 3.5% | s 64(1)(a)(i), (2) |
| C10 | rate reduction; pay calculated 1 Apr 2026 | 3%, $60 | s 64(1)(c), s 101O |
| C11 | rate reduction flag but pay calculated 31 Mar 2026 | 3% does NOT apply (no rate reduction before 1 Apr 2026, s 4 definition); text-as-in-force default 3.5% | s 64(1)(c), s 4 "rate reduction" |
| C12 | rate reduction, but employee had chosen 8% | 3% — s 101O obliges deduction at s 64(1)(c) rate | s 101O, s 64(1)(c) |
| C13 | on 2% chosen rate immediately before the first pay period on/after 1 Apr 2013 | 3.5% | s 64(1)(a)(iii) |
| C14 | s 66A applied immediately before 1 Apr 2009 | 3.5% | s 64(1)(a)(ii) |
| C15 | pre-2009 starter who gave an 8% notice | 8% | s 64(1)(b) |
| C16 | employee opted out and s 20(2) stopped deductions | no deduction (subpart 1 does not apply) | s 62(a) |
| C17 | employee on savings suspension | no deduction | s 62(b) |
| C18 | valid non-deduction notice | no deduction | s 62(bb) |
| C19 | no PAYE deduction required on the payment, not a PDW | no deduction | s 62(c) |
| C20 | gross $1,234.56 at 3.5% | $43.2096 (no rounding rule in the Act) | s 66 |
| C21 | rate last changed 1 Jan 2026; new change 2 Apr 2026 (91 days) | not permitted unless employer agrees | s 64(6) |
| C22 | as C21 but 3 Apr 2026 (92 days) | permitted | s 64(6) |
| C23 | as C21 with employer's agreement | permitted | s 64(6) |
| C24 | new rate notified to employer 10 May; next pay calculated 12 May | new rate applies from the 12 May payment | s 64(4) (the "(2E)" subsection) |

## Compulsory employer contributions (ss 101C-101FC)

| id | facts | expected | provision |
|---|---|---|---|
| C25 | aged 30, deductions required, gross $2,000, no other contributions | CEC $70 | s 101D(1),(4)(b) |
| C26 | aged 16 | CEC payable | s 101C(b) "aged 16 or over" |
| C27 | aged 15 (opted in, deductions made) | no CEC | s 101C(b) |
| C28 | aged 64 | CEC payable | s 101C(c) |
| C29 | aged 65 (NZSQA reached, entitled under cl 4) | no CEC | s 101C(c) |
| C30 | made a cl 12B congenital-condition withdrawal | no CEC | s 101C(d); cl 12B(5) |
| C31 | defined benefit scheme member | no CEC | s 101C(e) |
| C32 | not paid salary from which deduction is required (e.g. savings suspension) | no CEC | s 101C(a) |
| C33 | gross $2,000, other contributions $30 | CEC $40 | s 101D(1),(5) |
| C34 | gross $2,000, other contributions $100 | CEC $0 (positive amount, floored) | s 101D(1); BRIEF |
| C35 | rate reduction granted AND employer chooses 3% | CEC $60 | s 101D(4)(a) |
| C36 | rate reduction granted, employer does NOT choose 3% | CEC $70 | s 101D(4)(b) |
| C37 | no rate reduction, employer would like 3% | CEC $70 (3% requires a rate reduction) | s 101D(4) |
| C38 | gross $2,000, hybrid schemes amount $20 | CEC $50 | s 101D(1),(6) |
| C39 | gross $2,000, other $30, hybrid $20 | CEC $20 | s 101D(1) |
| C40 | s 101D(5)(b) other contributions = 3.5% of salary | no CEC (de minimis "equal to or more") | s 101FC(a) |
| C41 | s 101D(5)(b) other contributions = 3.4% of salary | de minimis not met; CEC = 2000×3.5% − 68 = $2 | s 101FC, 101D |
| C42 | AE employee, employer has not deducted, no opt-in or s 61 notice, pay 6 months after start | no CEC (grace period 1) | s 101FB(1),(2)(a) |
| C43 | as C42 but employer did deduct | CEC payable | s 101FB(1)(b) |
| C44 | as C42, pay 18 months after start, still no deduction or notices | no CEC (grace period 2) | s 101FB(2)(b) |
| C45 | as C44 but s 61 notice received before the payment | CEC payable | s 101FB(1)(c), (2)(b)(ii) |
| C46 | no agreement on allocation between KiwiSaver and complying fund | KiwiSaver scheme first up to the obligation | s 101E(2) |
| C47 | CEC for complying fund | due to the fund's provider within 1 month after the payment | s 101F(2) |

## Rate reductions (ss 101L-101S)

| id | facts | expected | provision |
|---|---|---|---|
| C48 | application for 91 days | not in accordance with s 101L; not granted | s 101L(3), 101M |
| C49 | application for 92 days | granted for 92 days | s 101L(3), 101M ("must grant") |
| C50 | application for exactly 1 year (365 days) | granted | s 101L(3) |
| C51 | application for 1 year + 1 day (366 days, non-leap) | not granted | s 101L(3) |
| C52 | person not subject to subpart 1 (no deductions) applies | cannot apply | s 101L(1) |
| C53 | revoke after 91 days without employer agreement | not permitted | s 101S(2) |
| C54 | revoke after 92 days | permitted | s 101S(2) |
| C55 | revoke after 30 days with employer agreement | permitted | s 101S(2) |
| C56 | grant notified to employer; deductions at 3% from | next payment the employer calculates | s 101O |

## Savings suspensions (ss 102-112B)

| id | facts | expected | provision |
|---|---|---|---|
| C57 | hardship; first contribution already received | may apply | s 102(a) |
| C58 | hardship; no contribution yet received | may NOT apply under (a) | s 102(a) "after the Commissioner receives the first contribution" |
| C59 | no hardship; first contribution 1 Apr 2025; applies 31 Mar 2026 | may NOT | s 102(b) |
| C60 | as C59, applies 2 Apr 2026 | may | s 102(b) |
| C61 | as C59, applies 1 Apr 2026 (anniversary) | AMBIGUOUS; my reading: not yet (12 months expire at end of the anniversary) | s 102(b) |
| C62 | no hardship; Commissioner first contribution 1 Jan 2026 but first member of a complying fund 1 Jan 2020 | may apply in 2026 (earliest of the dates) | s 102(b)(iii) |
| C63 | hardship grant | 92 days, unless Commissioner agrees longer | s 104(2) |
| C64 | non-hardship, asked for 60 days | granted for 92 days (minimum) | s 104(3)(a) |
| C65 | non-hardship, asked for 200 days | 200 days | s 104(3)(b)(ii) |
| C66 | non-hardship, asked for 500 days | 1 year | s 104(3)(b)(i) |
| C67 | revoke suspension after 91 days, no agreement | not permitted | s 108, s 112(1) |
| C68 | revoke after 92 days | permitted | s 108 |
| C69 | aged 64 tries to give a non-deduction notice | may NOT (only a person who may withdraw under cl 4) | s 112B(1) |
| C70 | aged 65 gives non-deduction notice | valid; deductions stop from the next payment | s 112B(1),(2), s 62(bb) |
| C71 | non-deduction notice 1 Jan 2026; revocation 3 Apr 2026 (92 days) | AMBIGUOUS "within 92 days"; my reading: still within, not permitted without agreement | s 112B(3) |
| C72 | revocation 4 Apr 2026 (93 days) | permitted | s 112B(3) |

## Schedule 1 withdrawals

Standard member: accumulation $50,000; Crown contribution $5,000 (tax-credit part $4,000,
kick-start s 226 part $1,000); amount transferred from an Australian scheme $8,000.

| id | facts | expected | provision |
|---|---|---|---|
| W1 | on 65th birthday | may withdraw up to $50,000 | cl 4(2) "on and after the date" |
| W2 | day before 65th birthday | not permitted (under cl 4) | cl 4(1) |
| W3 | aged 70 | up to accumulation | cl 4(2) |
| W4 | aged 60, Australian retirement occurred | may withdraw $8,000 | cl 4B |
| W5 | aged 59, retired | not permitted | cl 4B "60 years or more" |
| W6 | aged 60, not retired | not permitted | cl 4B |
| W7 | first home: 3+ years since first contribution, never held an estate, principal residence, NZ land | $50,000 − $1,000 − $8,000 = $41,000 | cl 8(1)(a), (3)(b), (4) |
| W8 | as W7, no Australian amount | $49,000 | cl 8(4) |
| W9 | as W8 but accumulation $900 | $0 (cannot go below nil) | cl 8(4) |
| W10 | accumulation exactly $1,000, no Australian amount | $0 | cl 8(4) |
| W11 | made a cl 8 withdrawal before (any scheme) | not permitted | cl 8(1) |
| W12 | only 2 years 11 months since first contribution, and combined membership < 3 years | not permitted | cl 8(1) |
| W13 | 2 years since first IRD contribution, but 3+ years combined in a complying fund + KiwiSaver | permitted | cl 8(1)(b) |
| W14 | has previously held a fee simple estate, not a qualifying person, no prescribed circumstances | not permitted | cl 8(3)(b)(ii) |
| W15 | previously held only a leasehold estate | disregarded; permitted | cl 8(6)(b) |
| W16 | previously held an estate only as bare trustee | disregarded; permitted | cl 8(6)(a) |
| W17 | previously held an estate, but is a qualifying person under the regulations, principal residence | permitted | cl 8(3)(c) |
| W18 | land overseas | not permitted (estate in land located in NZ) | cl 8(3) |
| W19 | not intended as principal residence, no prescribed circumstances | not permitted | cl 8(3)(b)(i) |
| W20 | interest in a dwellinghouse on Maori land, principal residence, never held estate | permitted, same cap | cl 8(3B), (4) |
| W21 | 3-year anniversary − 1 day of first contribution (no other route) | not permitted | cl 8(1)(a) |
| W22 | anniversary + 1 day | permitted | cl 8(1)(a) |
| W23 | death | personal representative paid $50,000 (accumulation at acceptance date) | cl 9(a) |
| W24 | significant financial hardship, alternatives exhausted | up to $50,000 − $5,000 = $45,000 | cl 10(2),(3)(a) |
| W25 | as W24 with direction limiting to $10,000 | $10,000 | cl 10(3)(b) |
| W26 | hardship, alternatives NOT exhausted | not permitted | cl 10(3)(a) |
| W27 | serious illness | up to $50,000 | cl 12(2) |
| W28 | life-shortening congenital condition (listed, certificate) | up to $50,000 | cl 12B(3) |
| W29 | permanent emigration (not to Australia), exactly 1 year after | $50,000 − $4,000 (tax-credit Crown only) − $8,000 = $38,000; the kick-start $1,000 is NOT deducted | cl 14(1) |
| W30 | 364 days after emigration | not permitted to withdraw | cl 14(1) |
| W31 | transfer to authorised foreign scheme, any time after emigration (e.g. 1 month) | $38,000 | cl 14(2) |
| W32 | emigrated permanently to Australia | cl 14 not available; whole accumulation ($50,000) transferable to an Australian complying scheme | cl 14B |
| W33 | cl 14C tax liability $3,000, terminal tax $2,500 | $2,500 | cl 14C(2)(a) |
| W34 | cl 14C student loan obligation $1,200 | $1,200 | cl 14C(2)(b) |
| W35 | cl 14C tax liability $60,000, terminal tax $60,000 | capped at $50,000 − $5,000 = $45,000 | cl 14C(3) |
| W36 | cl 14C application 25 months after end of the assessment month | not permitted | cl 14C(4)(a) |
| W37 | cl 14C application 24 months after end of the assessment month | permitted | cl 14C(4)(a) |
| W38 | any cl 4-14C withdrawal where no residence statutory declaration given | tax-credit Crown contribution ($4,000) may not be withdrawn: e.g. death payout $46,000 | cl 17(a) |

## Ambiguities and reasons (summary)

1. Early opt-out notice (M39). s 17(1) requires the notice "within the time limit in section 16";
   the s 16 window opens on day 13. s 17(4)(a) ("later of the 13th day...") only makes sense if an
   earlier-received notice could be effective, so a reader might treat early notices as valid with
   effect on day 13. I prefer the s 16/17(1) reading because s 17(1) is the operative requirement.
2. Anniversary days (C61, W21-22). "after 12 months have expired since" / "at least 3 years have
   expired after" — the anniversary is the edge case.
3. s 112B(3) "within 92 days" (C71) — inclusive reading preferred, unlike s 108's "less than 92 days".
4. 3% with a rate reduction before 1 April 2026 (C11): a rate reduction cannot exist before that
   date by definition; the Act as at 1 April 2026 no longer contains the old default (3%), so the
   text in force gives 3.5%. A careful encoding might REFUSE for pre-2026 dates.
5. Rate reduction v chosen rate (C12): s 64(2) says "despite subsection (1)", but s 101O imposes
   a specific duty to deduct at 3%; the specific, later duty wins.
6. cl 8(4) result below nil (W9): the Act states a maximum; a negative maximum means nil.
7. cl 10 deducts "the Crown contribution" (all of it), but cl 14 deducts only the tax-credit part:
   the kick-start is withdrawable on emigration. This is deliberate in the text.
8. s 101D formula symbols were lost; read per BRIEF as gross × rate − other − hybrid, floored at 0.

## Additional scenarios fixed after reading the record shapes (phase 2)

These were derived from the statute, not from the encoding's output; they only re-state phase 1
scenarios in the encoding's vocabulary.

| id | facts | expected | provision |
|---|---|---|---|
| C73 | employee who chose 2% before 1 April 2013, still recorded as a 2% notice | 3.5% | s 64(1)(a)(iii) |
| C74 | rate reduction starting 1 Apr 2026, last day 1 Jul 2026 (92 days counted inclusively) | granted | s 101L(3). AMBIGUOUS whether the "ending" date is the last day of the period; I read it as the last day, so the period's length is end − start + 1 |
| C75 | rate reduction 1 Apr 2026 to 30 Jun 2026 (91 days inclusive) | not granted | s 101L(3) |
| C76 | rate reduction 1 Apr 2026 to 31 Mar 2027 (exactly 1 year) | granted | s 101L(3) |
| C77 | rate reduction 1 Apr 2026 to 1 Apr 2027 (1 year and 1 day) | not granted | s 101L(3) "no more than 1 year" |
| M20g | top-level goal for M20 (28-day contract, not continued) | AE false, no opt-out window | s 12(1)(b) |
| M73 | 17-year-old whose only guardian is an Oranga Tamariki guardian | must contract jointly with that guardian (s 35(3) "with a guardian or an Oranga Tamariki guardian"); s 35(4) "no guardian" alone does NOT apply | s 35(3),(4) |

## Scenarios the encoding could not express

- M5-M7: s 6(1)(a) State-services limbs are a single input boolean; the three limbs cannot be
  tested separately (an input, so nothing to test).
- M8-M11: s 6(2)-(3) application to employers is not modelled at all.
- M15: covered implicitly (age at start); no "later birthday" trigger exists, consistent.
- M23: s 12(2)(a) — the day after a casual agricultural worker ceases to be one, AE applies. The
  encoding treats casual agricultural work as permanently temporary; there is no field for the date
  the person stops being a casual agricultural worker. OMISSION.
- M22 (continuing 28-day contract) and M20 (contract that really ends within 28 days) cannot be
  distinguished: the encoding has no "employment continued" fact. It assumes continuation, so M20
  is asserted and fails. Also, for a continuing contract s 12(2) says AE applies "as if the employee
  then started new employment", so the s 16 window should run from the 28th day; the top-level goal
  computes the window from the original start date.
- M36, M46, M47, M51, M54, M71, M72: effects and grounds that are not computed by any function.
- M48/M52/M53: the s 18 ground is a single boolean input; s 42 information-pack timing as a ground
  cannot be tested through s 18.
- M64 (opt-in channel by employer notice for under-18s): no channel in the opt-in function.
- M70: s 48's "more than 62 days" (first + 63) has no function; only the s 51 date exists.
- C14: s 64(1)(a)(ii) (s 66A transitional) has no fact; such a person would be recorded as
  "first applied before 1 April 2009" and receive 4% instead of 3.5%. OMISSION.
- C19: s 62(a) (opted out) and s 62(c) (no PAYE) have no fact in Contribution facts; only a
  suspension / non-deduction notice flag.
- C24, C56: "next payment calculated after the notice" timing is not modelled.
- C42-C45: s 101FB grace periods are a single input boolean; the 1-year boundary and the effect of a
  s 61 notice cannot be tested.
- C46, C47 (partly): s 101E allocation not modelled; s 101F(2) date only.
- C52, C69/C70: who may apply for a rate reduction / give a non-deduction notice is not modelled
  (s 112B(1) eligibility on reaching the withdrawal age).
- C62: the "earliest of three dates" in s 102(b) is left to the caller (single date input).
- W11 (prior cl 8 withdrawal) is expressible; W15-W17, W18, W20 collapse into input booleans
  (leasehold/bare-trustee disregard, NZ location, Maori land) — no logic to test.
- W21/W22: cl 8(1) years is a number input; anniversary days cannot be tested.
- W31: cl 14(2) transfer to a foreign scheme (any time after emigration) is not modelled.
- W32: cl 14B Australian transfer is not modelled (only excluded by the purpose label).
- W33: cl 14C(2)(a) "lesser of the tax liability and the terminal tax" — only one liability input,
  so the terminal-tax cap cannot be expressed. OMISSION.
- W36/W37: cl 14C(4)(a) 24-month application window is not modelled (no assessment date).
- W38: cl 17 (tax-credit Crown contribution not withdrawable without a residence statutory
  declaration, "despite rules 4 to 14C") is not modelled. OMISSION.

## Result of running tests-independent.l4 (2026-10-16)

167 assertions: 160 satisfied, 5 failed, 2 refused, 0 other errors.

- Failed: M20 (line 118), M20g (line 441) — a 28-day contract is treated as enrolled.
- Failed: M73 (line 200) — 17-year-old with only an Oranga Tamariki guardian is sent to s 35(4).
- Failed: C74 (line 323), C77 (line 331) — s 101L(3) period counted end − start (exclusive end).
- Refused: C9 (line 233) 5% notice; C73 (line 235) pre-2013 2% chosen rate (s 64(1)(a)(iii)).
- C71 (s 112B(3) day 92) could not be asserted: the encoding uses its s 64(4) helper, which permits
  day 92; on my inclusive reading of "within 92 days" it should not.
