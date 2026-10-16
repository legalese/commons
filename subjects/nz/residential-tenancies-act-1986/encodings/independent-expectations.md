# Independent expectations: Residential Tenancies Act 1986 (NZ)

Written from BRIEF.md and the source text (as at 1 December 2025) **before any .l4 file was opened**.
Expected values below are fixed. Rows that the encoding cannot express are marked at the end
(section "Not expressible"), added after step 3 without changing any expected value.

## Calendar facts used (s 2 "working day")

s 2: "working day means any day other than— a Saturday, a Sunday, Waitangi Day, Anzac Day, the
Sovereign's birthday, Te Rā Aro ki a Matariki/Matariki Observance Day, and Labour Day; and if Waitangi
Day or Anzac Day falls on a Saturday or a Sunday, the following Monday; and the day observed in the
appropriate area as the anniversary of the province …; and a day in the period commencing with Good
Friday and expiring with the Tuesday after Easter; and a day in the period commencing with 24 December
and expiring with 3 January."

| | 2026 | 2027 |
|---|---|---|
| Waitangi Day | Fri 6 Feb | Sat 6 Feb, so Mon 8 Feb also excluded |
| Good Friday to Easter Tuesday | 3-7 Apr | 26-30 Mar |
| Anzac Day | Sat 25 Apr, so Mon 27 Apr also excluded | Sun 25 Apr, so Mon 26 Apr also excluded |
| Sovereign's birthday (1st Mon June) | Mon 1 Jun | Mon 7 Jun |
| Matariki (input) | Fri 10 Jul | Fri 25 Jun |
| Labour Day (4th Mon Oct) | Mon 26 Oct | Mon 25 Oct |
| Christmas block | 24 Dec 2026 - 3 Jan 2027 | |

Anniversary days are inputs (e.g. Wellington Anniversary Mon 25 Jan 2027 when supplied).

## Readings taken where the Act is ambiguous

R1. **Notice periods (s 136A).** "the period— commences on the first day after the notice is given or
deemed to be given under section 136; and ends with the close of the last day of the period." So for
"at least N days' notice" given (or deemed given) on day D, the earliest lawful termination / effective
date is **D + N** (the Nth day of the period is the last day; the tenant may be required to vacate by
that day). Same for s 24(1)(c): "not less than 60 days … after the date on which that notice is given"
gives earliest payable day D + 60.

R2. **Deemed service (s 136).** Post: "deemed … given or served on the fourth working day after the
date on which it was posted" (s 136(6)). Delivery to mailbox/door: "on the second working day after the
date on which it was delivered" (s 136(7)). Electronic after 5 pm: "on the next working day after the
date on which it was transmitted" (s 136(9)). Personal service, and electronic transmission at or before
5 pm, take effect on the day itself (no deeming rule; I read "after 5 pm" strictly, so 5:00 pm exactly
is the same day). A s 56B withdrawal notice by post or delivery is given on the day of posting/delivery
(s 56C).

R3. **"within 12 months after the date" (s 24(1)(d),(e)).** Following the Legislation Act 2019 rule that
a period "after" a day excludes that day, 12 months after 1 Mar 2026 runs 2 Mar 2026 - 1 Mar 2027, so an
increase taking effect on 1 Mar 2027 is **within** 12 months (unlawful); 2 Mar 2027 is the earliest
lawful day. (Ambiguous: popular practice treats the anniversary as allowed. I take the strict reading.)
The same exclusive-start reading is used for "3 months after" (s 25(2)), "12 months after" (s 109(2),
(3); s 108(7) "after the expiration of 12 months"), "1 year after" (s 62D), "90 days after" (s 64),
"within 2 months of" (s 22A(3)), "35 days from" (s 62A(3)), "28 days after" (ss 55(1)(aa)(iv),
55A(2)(c)): in each case the last permitted day is the anniversary/D+N day itself.

R4. **"within a 90-day period" (ss 55(1)(aa), 55A(2)(a)).** Three occasions fall within a 90-day period
iff last occasion minus first occasion ≤ 89 days (a 90-day window counted inclusively).

R5. **"owing for at least 5 working days after the date on which it was due" (s 55(1)(aa)(i)).** An
occasion counts when the rent is still unpaid at the close of the 5th working day after the due date.

R6. **Hours (ss 48, 66R, 66X).** "not less than 48 hours" / "at least 24 hours" measured clock-to-clock
from the time the notice is given; exactly 48 h / 24 h is enough. "between 8 o'clock in the morning and
7 o'clock in the evening" includes 08:00 and 19:00 exactly.

R7. **s 48(2)(b) "not more frequently than once in any period of 4 weeks".** A second inspection is
allowed iff it is at least 28 days after the previous one (no 28-day window contains both).

R8. **s 49B(3).** Careless-damage liability = min(damage, cap), where cap = min(insurance excess, 4
weeks' rent) if insured, else 4 weeks' rent; "rent" is the market rent for 4 weeks where the tenant pays
income-related rent. Intentional / imprisonable-offence / pet damage: liability not capped by s 49B(3)
(subject to s 77(5)). Fair wear and tear: nil (s 49A(2)).

R9. **s 51(2) on a fixed-term tenancy.** s 50(1)(a) only lets fixed-term tenancies end on expiry or
under ss 55AA, 56A(1), 58(1)(d),(da), 58A, 59, 59A, 59B. So s 51 (90/42/21 days) and ss 53/53A are not
available to end a fixed term early. I read s 53 (service) and s 53A (student) as periodic-only because
they are not in s 50(1)(a).

## Goal 1: Application of the Act and working days

| ID | Inputs | Expected | Provision |
|---|---|---|---|
| A01 | Fri 3 Apr 2026 | not a working day | s 2 "a day in the period commencing with Good Friday" |
| A02 | Tue 7 Apr 2026 | not a working day | s 2 "expiring with the Tuesday after Easter" |
| A03 | Wed 8 Apr 2026 | working day | s 2 |
| A04 | Mon 27 Apr 2026 | not a working day | s 2 "if … Anzac Day falls on a Saturday … the following Monday" |
| A05 | Fri 6 Feb 2026 | not a working day | s 2 "Waitangi Day" |
| A06 | Mon 8 Feb 2027 | not a working day | s 2 Waitangi Day Saturday → following Monday |
| A07 | Thu 24 Dec 2026 | not a working day | s 2 "commencing with 24 December" |
| A08 | Sun 3 Jan 2027 / Mon 4 Jan 2027 | not / working day | s 2 "expiring with 3 January" |
| A09 | Mon 1 Jun 2026 | not a working day | s 2 "the Sovereign's birthday" |
| A10 | Fri 10 Jul 2026 (Matariki input) | not a working day | s 2 "Matariki Observance Day" |
| A11 | Mon 26 Oct 2026 / Tue 27 Oct 2026 | not / working | s 2 "Labour Day" |
| A12 | Wed 23 Dec 2026 | working day | s 2 |
| A13 | Fri 26 Mar 2027 / Wed 31 Mar 2027 | not / working | s 2 Easter 2027 |
| A14 | Mon 26 Apr 2027 | not a working day | s 2 Anzac Day Sunday → Monday |
| A15 | Mon 7 Jun 2027 | not a working day | Sovereign's birthday 2027 |
| A16 | Mon 25 Jan 2027, with it supplied as anniversary day / without | not working / working | s 2 "the day observed … as the anniversary of the province" |
| A17 | Mon 16 Nov 2026, no anniversary supplied | working day | s 2 |
| A18 | 4th working day after Thu 2 Apr 2026 | Mon 13 Apr 2026 | s 136(6) |
| A19 | 2nd working day after Fri 18 Dec 2026 | Tue 22 Dec 2026 | s 136(7) |
| A20 | 2nd working day after Tue 22 Dec 2026 | Mon 4 Jan 2027 | s 136(7), Christmas block |
| A21 | 4th working day after Mon 21 Dec 2026 | Tue 5 Jan 2027 | s 136(6) |
| A22 | 2nd working day after Thu 25 Mar 2027 | Thu 1 Apr 2027 | Easter 2027 |
| A23 | 4th working day after Tue 22 Jun 2027 (Matariki 25 Jun input) | Tue 29 Jun 2027 | s 2, s 136(6) |
| A24 | ordinary residential house let to a family | Act applies | s 4 "applies to every tenancy for residential purposes" |
| A25 | premises are commercial premises | Act does not apply | s 5(1)(a) "where the premises are commercial premises" |
| A26 | let for tenant's holiday purposes | does not apply | s 5(1) "let for the tenant's holiday purposes" |
| A27 | landlord continues to live there as principal residence, not a boarding house | does not apply | s 5(1) "not being a boarding house, continue to be used … principally as a place of residence by the landlord" |
| A28 | same but premises are a boarding house | applies | same words "not being a boarding house" |
| A29 | emergency accommodation funded by emergency housing assistance | does not apply | s 5(1) last paragraph |
| A30 | excluded tenancy (holiday) but parties agreed in writing the Act applies | applies | s 8 "agreeing in writing that all or any of the provisions of this Act shall apply" |
| A31 | hotel with on-licence | does not apply | s 5(1) "any hotel in respect of which an on-licence is in force" |
| A32 | fixed term 90 days, written no-extension agreement before commencement | s 51 and ss 25-28 do not apply | s 7(1) "fixed term of not more than 90 days … agree in writing" |
| A33 | fixed term 91 days, written agreement | s 51 / ss 25-28 apply | s 7(1) "not more than 90 days" |
| A34 | fixed term 60 days, no written agreement | s 51 / ss 25-28 apply | s 7(1) requires agreement in writing before commencement |
| A35 | fixed term 60 days with written agreement, then extended so total exceeds 90 days | apply (from day 90) | s 7(2) |

## Goal 2: Bonds and rent

Weekly rent $600 unless stated.

| ID | Inputs | Expected | Provision |
|---|---|---|---|
| B01 | general bond $2,400 | lawful | s 18(1) "no more than 4 weeks' rent" |
| B02 | general bond $2,401 | unlawful act | s 18(1),(4) |
| B03 | max general bond, rent $550/week | $2,200 | s 18(1) |
| B04 | rent increased $600 → $650; further general bond $200 | lawful; $201 unlawful | s 18(2) "not exceeding the amount by which the rent payable for 4 weeks has been increased" |
| B05 | pet bond $1,200, tenant keeps pet with consent | lawful | s 18AA(1) "no more than 2 weeks' rent" |
| B06 | pet bond $1,201 | unlawful | s 18AA(5)(a) |
| B07 | pet bond $500, tenant not keeping/intending pet | unlawful | s 18AA(5)(b) |
| B08 | second pet bond while one already held | unlawful | s 18AA(2) "must not require payment of more than 1 pet bond at any one time" |
| B09 | pet bond, pet kept but landlord has not agreed | not permitted | s 18AA(1)(b) |
| B10 | general $2,400 + pet $1,200 together | lawful (total $3,600) | ss 18, 18AA separately capped |
| B11 | landlord requires credit-card imprint as security | unlawful | s 18A "security … imprint of a credit card" |
| B12 | landlord requires a guarantee | lawful | s 18A(3)(b)(ii) "does not include— … any guarantee" |
| B13 | bond paid Fri 20 Mar 2026; lodge deadline | Tue 28 Apr 2026 | s 19(1)(b) "within 23 working days after the payment is made" |
| B14 | bond paid 20 Mar 2026, lodged 28 Apr / 29 Apr 2026 | compliant / unlawful act | s 19(1)(b),(2) |
| B15 | bond paid Tue 1 Dec 2026; deadline | Tue 12 Jan 2027 | s 19(1)(b) with Christmas block |
| B16 | bond paid Mon 15 Jun 2026 (Matariki 10 Jul input); deadline | Fri 17 Jul 2026 | s 19(1)(b) |
| B17 | bond paid 20 Jan 2027, anniversary Mon 25 Jan 2027 supplied / not | Wed 24 Feb 2027 / Tue 23 Feb 2027 | s 2 anniversary day |
| B18 | boarding house, rent $200/week, bond $200 | need not be lodged; receipt immediately; refund on termination | s 66D(1) "1 week's rent or less … need not be lodged" |
| B19 | boarding house, rent $200, bond $201 | must be lodged within 23 working days | s 19(1A), s 66D only for ≤1 week |
| B20 | receipt for bond not given | unlawful act | s 19(2) |
| B21 | rent $500/wk, landlord requires $1,000 in advance (none outstanding) | lawful | s 23(1)(a) "more than 2 weeks in advance" |
| B22 | requires $1,001 / 3 weeks in advance | unlawful | s 23(1)(a),(3) |
| B23 | requires rent before the already-paid period expires | unlawful | s 23(1)(b) |
| B24 | requires payment by postdated cheque | unlawful | s 23(2) |
| B25 | rent increase notice given (personal) Mon 2 Nov 2026, tenancy commenced 1 Jan 2025, no prior increase, periodic; increase from Fri 1 Jan 2027 | lawful | s 24(1)(c) "not less than 60 days" (R1) |
| B26 | same, increase from Thu 31 Dec 2026 | unlawful (59 days) | s 24(1)(c) |
| B27 | earliest payable day for notice given 2 Nov 2026 | Fri 1 Jan 2027 | s 24(1)(c), R1 |
| B28 | boarding house: notice 2 Nov 2026, increase from Mon 30 Nov 2026 / Sun 29 Nov | lawful / unlawful | s 24(1)(c) "28 days" |
| B29 | notice posted Mon 2 Nov 2026 → deemed given Fri 6 Nov 2026; earliest payable | Tue 5 Jan 2027 | ss 136(6), 24(1)(c) |
| B30 | tenancy commenced 1 Mar 2026; increase to take effect 1 Mar 2027 (notice in time) | unlawful (within 12 months, R3) | s 24(1)(d) |
| B31 | same; increase effective 2 Mar 2027 | lawful | s 24(1)(d) |
| B32 | last increase took effect 15 May 2026; next effective 15 May 2027 / 16 May 2027 | unlawful / lawful | s 24(1)(e) |
| B33 | fixed-term tenancy, agreement has no rent-review clause, increase during term | unlawful | s 24(1)(f) |
| B34 | fixed-term, agreement permits increase, all other conditions met | lawful | s 24(1)(f) |
| B35 | market-rent order in force at $550; increase to $560 | unlawful; $550 lawful | s 24(1)(g) |
| B36 | notice of increase not in writing | unlawful | s 24(1)(a) |
| B37 | reinstatement of rent after temporary reduction | not a rent increase | s 24A(c) |
| B38 | fixed term commenced 10 Feb 2026, no review; market rent application 10 May 2026 / 11 May 2026 | in time / out of time | s 25(2) "later than 3 months after" (R3) |
| B39 | fixed term commenced 10 Feb 2026, last rent review 1 Aug 2026; application 1 Nov 2026 | in time | s 25(2) "whichever is the later" |
| B40 | periodic tenancy, application 3 years after commencement | in time ("at any time") | s 25(1) |
| B41 | application 1 Sep 2026, order 1 Oct 2026; effective date 1 Sep 2026 / 31 Oct 2026 | both allowed | s 25(5) "no earlier than the date of the application … no later than 30 days after the date of the order" |
| B42 | same; effective 31 Aug 2026 / 1 Nov 2026 | not allowed / not allowed | s 25(5) |
| B43 | periodic tenancy market rent order; maximum duration | 1 year | s 26(1)(a) |
| B44 | rent paid in cash; receipt | required forthwith | s 29(2)(a) |
| B45 | rent paid by bank transfer (not automatic payment, not into dedicated account) at 10:00 on 1 Jun 2026; receipt at 10:00 4 Jun / 11:00 4 Jun | compliant / late | s 29(2)(b) "within 72 hours after payment" |
| B46 | rent paid by automatic payment from tenant's account | no receipt required | s 29(3)(a) |
| B47 | rent paid into account nominated by landlord operated exclusively for tenancies | no receipt required | s 29(3)(b) |
| B48 | rent deducted from benefit paid into landlord's nominated account | no receipt required | s 29(3)(c) |
| B49 | record of rent payment made 15 May 2026; keep until | 31 Mar 2034 | s 30(1A) "7 tax years after the tax year"; tax year 1 Apr 2026 - 31 Mar 2027 |
| B50 | record of payment made 1 Apr 2027 | keep until 31 Mar 2035 | s 30(1A),(1B) |
| B51 | record of payment 31 Mar 2027 | keep until 31 Mar 2034 | s 30(1A) |
| B52 | careless damage $3,000, insured, excess $500, rent $600 | liable $500 | s 49B(3)(a) lesser of excess and 4 weeks' rent |
| B53 | careless damage $3,000, insured, excess $3,000, rent $600 | liable $2,400 | s 49B(3)(a)(ii) |
| B54 | careless damage $3,000, not insured, rent $600 | liable $2,400 | s 49B(3)(b)(ii) |
| B55 | careless damage $300, not insured, rent $600 | liable $300 | s 49B(2) "to the extent" / cap only limits |
| B56 | intentional damage $3,000 | liable $3,000 (not capped) | s 49B(1)(a) |
| B57 | damage from tenant's pet $3,000 | liable $3,000 | s 49B(1)(c) |
| B58 | careless, income-related rent $150/wk, market rent $550/wk, not insured, damage $5,000 | liable $2,200 | s 49B(3)(b)(i) |
| B59 | careless, insured excess $1,000, insurance irrecoverable because of tenant's act, rent $600, damage $5,000 | liable $2,400 | s 49B(4)(a) treated as not insured |
| B60 | fair wear and tear | liable $0 | s 49A(2) |
| B61 | damage from imprisonable offence on premises $4,000 | liable $4,000 | s 49B(1)(b) |
| B62 | s 56B: 3 tenants, one withdraws; rent for 2-week period $1,800 | rent for that period $1,200 | s 56B(5) formula (brief: rent × remaining ÷ before) |
| B63 | same but rent is income-related | $1,800 (no reduction) | s 56B(6)(a) |
| B64 | s 56B: 4 tenants → 1 remaining, 2-week rent $2,000 | $500 | s 56B(5) |
| B65 | landlord bond application without agreement, tenancy ended 30 Jun 2026, filed 30 Aug / 31 Aug 2026 | in time / out of time | s 22A(3) "within 2 months of the termination" |
| B66 | tenant bond application without agreement, 2 years after termination | in time ("at any time") | s 22A(3) |

## Goal 3: Termination

Personal service unless stated. "Earliest date" means the earliest termination date the notice may
specify (R1).

| ID | Inputs | Expected | Provision |
|---|---|---|---|
| C01 | landlord, periodic, no reason, served Mon 2 Mar 2026 | earliest Sun 31 May 2026 | s 51(1)(a) "at least 90 days' notice", s 136A |
| C02 | landlord, periodic, owner to live there, served 2 Mar 2026 | earliest Mon 13 Apr 2026 | s 51(1)(b) "at least 42 days' notice" |
| C03 | tenant, periodic, served 2 Mar 2026 | earliest Mon 23 Mar 2026 | s 51(2) "at least 21 days' notice" |
| C04 | landlord 90 days, posted Mon 2 Mar 2026 | deemed served Fri 6 Mar; earliest Thu 4 Jun 2026 | ss 136(6), 51(1)(a) |
| C05 | tenant 21 days, delivered to mailbox Fri 29 May 2026 | deemed Wed 3 Jun 2026 (1 Jun Sovereign's birthday); earliest Wed 24 Jun 2026 | s 136(7) |
| C06 | landlord 90 days, email 2:00 pm Fri 16 Oct 2026 | served same day; earliest Thu 14 Jan 2027 | s 136(1)(f), R2 |
| C07 | landlord 42 days, email 6:00 pm Thu 9 Jul 2026 | deemed Mon 13 Jul 2026 (10 Jul Matariki); earliest Mon 24 Aug 2026 | s 136(9) |
| C08 | landlord 90 days, posted Fri 4 Sep 2026 | deemed Thu 10 Sep; earliest Wed 9 Dec 2026 | s 136(6) |
| C09 | tenant 21 days, posted Thu 22 Oct 2026 | deemed Thu 29 Oct (Labour Day 26 Oct); earliest Thu 19 Nov 2026 | s 136(6) |
| C10 | tenant 21 days, delivered Tue 22 Dec 2026 | deemed Mon 4 Jan 2027; earliest Mon 25 Jan 2027 | s 136(7) |
| C11 | landlord, periodic, served 2 Mar 2026, notice says vacate 30 May 2026 | notice short (invalid) ; 31 May valid | s 51(1)(a) |
| C12 | landlord 42 days for vacant possession under unconditional sale contract | available (42) | s 51(1)(b)(ii) |
| C13 | landlord 42 days for employee use, stated in agreement, premises required | available | s 51(1)(b)(iii) |
| C14 | employee use but not stated in agreement | 42 days not available (90 applies) | s 51(1)(b)(iii)(A) "clearly stated in the tenancy agreement" |
| C15 | school board employees, stated, required, landlord not the Crown | 42 days not available | s 51(1)(b)(iv) "the landlord is the Crown" |
| C16 | landlord wants to end fixed-term tenancy early with 90 days' notice | not lawful (fixed term ends on expiry) | s 50(1)(a), R9 |
| C17 | tenant wants to end fixed-term tenancy early with 21 days' notice | not lawful | s 50(1)(a), s 51(2) "periodic tenancy" |
| C18 | landlord, fixed or periodic, tenant physically assaulted landlord, charge filed; served 3 Aug 2026 | 14 days, earliest Mon 17 Aug 2026 | s 55AA(1) |
| C19 | same, no charge filed | not available | s 55AA(1)(b) |
| C20 | service tenancy, employment contract terminated; either party; served 3 Aug 2026 | 14 days, earliest 17 Aug 2026 | s 53(1) |
| C21 | service tenancy notice served 3 Aug, contract terminates 24 Aug 2026 | cannot take effect before 24 Aug 2026 | s 53(3) |
| C22 | service tenant dies leaving dependant, replacement employee needed, no alternative accommodation | 5 days | s 53(5) |
| C23 | service tenant dies leaving dependant (no urgency) | 14 days | s 53(4) |
| C24 | student tenancy, tenant ceased to be eligible; landlord or tenant | 14 days | s 53A(2) |
| C25 | tenant, premises unlawful residential premises from start; served 3 Aug 2026 | 2 days, earliest Wed 5 Aug 2026 | s 56A(1) |
| C26 | family violence withdrawal, notice posted Mon 7 Sep 2026 | given 7 Sep (s 56C); withdrawal Wed 9 Sep 2026 | ss 56B(1), 56C(1)(a) |
| C27 | family violence withdrawal, sole tenant | tenancy terminates | s 56B(2) |
| C28 | family violence withdrawal, other tenants remain | tenancy continues with remaining tenants | s 56B(3)(b) |
| C29 | build-to-rent fixed term 10 years, tenant, served 3 Aug 2026 | 56 days, earliest Mon 28 Sep 2026 | s 58A(2) |
| C30 | build-to-rent fixed term 9 years | s 58A not available | s 58A(1)(a) "at least 10 years" |
| C31 | premises destroyed (no breach), landlord, served 3 Aug 2026 | 7 days, earliest Mon 10 Aug 2026 | s 59(1A) |
| C32 | premises destroyed (no breach), tenant | 2 days | s 59(1B) |
| C33 | premises uninhabitable through tenant's breach; tenant gives notice | not available (only the party not in breach) | s 59A(3) |
| C34 | rent 21 days in arrear at filing | Tribunal must terminate | s 55(1)(a) "at least 21 days in arrear" |
| C35 | rent 20 days in arrear at filing (no other ground) | not on s 55(1)(a) | s 55(1)(a) |
| C36 | periodic; 3 late-rent occasions on 1 Feb, 15 Mar, 1 May 2026, notices proper, application 29 May 2026 (third notice 1 May) | Tribunal must terminate | s 55(1)(aa), R4 |
| C37 | same but third occasion 2 May 2026 | not within a 90-day period | s 55(1)(aa)(i) |
| C38 | same as C36, application 30 May 2026 | out of time | s 55(1)(aa)(iv) "within 28 days after" |
| C39 | same as C36 but fixed-term tenancy | s 55(1)(aa) not available | "the tenancy is a periodic tenancy" |
| C40 | only 2 occasions | not available | "on 3 separate occasions" |
| C41 | a notice did not state how many other notices given | not available | s 55(1)(aa)(iii) |
| C42 | rent due Mon 3 Aug 2026 still unpaid at close of Mon 10 Aug | counts as an occasion (5 working days) | s 55(1)(aa)(i), R5 |
| C43 | rent due Mon 19 Oct 2026; 5th working day after is Tue 27 Oct (Labour Day) | counts only if unpaid at close of 27 Oct | s 55(1)(aa)(i) |
| C44 | anti-social behaviour, periodic, 3 notices within 90 days, application within 28 days of third | must terminate | s 55A(2) |
| C45 | anti-social, fixed-term | not available | s 55A(1) "periodic tenancy" |
| C46 | anti-social, application motivated by tenant's complaint (not vexatious) | must not make order | s 55A(3)(b) |
| C47 | fixed term expiring Thu 31 Dec 2026, more than 90 days; no notice | becomes periodic | s 60A(1) |
| C48 | same, written notice not to continue given 2 Oct 2026 | valid (effective period starts 2 Oct) | s 60A(3) "starts on the 90th day before" |
| C49 | given 1 Oct 2026 | outside effective period → continues periodic | s 60A(2)(c),(3) |
| C50 | given 10 Dec 2026 / 11 Dec 2026 | valid / too late | s 60A(3) "ends on the 21st day before" |
| C51 | fixed term of 90 days exactly, expiring | does not become periodic | s 60A(1) "more than 90 days" |
| C52 | parties renewed before expiry | does not continue as periodic | s 60A(2)(a) |
| C53 | tenant's notice exercising renewal right, expiry 31 Mar 2027: given 10 Mar / 11 Mar 2027 | in time / late | s 60B(2) "not later than the 21st day before" |
| C54 | periodic, Tribunal-specified abandonment date 1 Jul 2026, no new tenancy | rent liable to Wed 22 Jul 2026 | s 61(3)(a)(i) |
| C55 | same, new tenancy commences 15 Jul 2026 | rent liable to 15 Jul 2026 | s 61(3)(a) "whichever is the earlier" |
| C56 | fixed term expiring 31 Dec 2026, new tenancy from 1 Sep 2026 | rent liable to 1 Sep 2026 | s 61(3)(b) |
| C57 | fixed term expiring 31 Dec 2026, no new tenancy | rent liable to 31 Dec 2026 | s 61(3)(b)(i) |
| C58 | abandoned goods worth more than storage cost, possession taken 1 Aug 2026; sell 5 Sep / 6 Sep 2026 | not yet / may sell | s 62A(3),(5) "not less than 35 days from" |
| C59 | goods worth less than costs of storing/transporting/selling | may dispose immediately | s 62A(2) |
| C60 | perishable goods | may dispose immediately on taking possession | s 62(1) |
| C61 | goods sold 1 Oct 2026; tenant claims proceeds 1 Oct 2027 / 2 Oct 2027 | in time / late | s 62D "within 1 year after the date of a sale" |
| C62 | tenancy terminated 30 Jun 2026; possession order sought 28 Sep / 29 Sep 2026 | may be made / may not | s 64(2) "more than 90 days after" |
| C63 | possession order dated 10 Jul 2026; filed 8 Oct / 9 Oct 2026 | in time / out of time | s 64(4) |
| C64 | death of sole tenant; PR notice 3 Aug 2026, landlord notice 5 Aug, nothing agreed | terminates Mon 24 Aug 2026 | s 50A(1)(a) "21st day after" |
| C65 | same, agreed date 20 Aug 2026 | terminates 20 Aug 2026 | s 50A(1)(c) "earliest" |
| C66 | only landlord notice to vacate 5 Aug 2026 | terminates Wed 26 Aug 2026 | s 50A(1)(b) |
| C67 | s 56D application, fixed term, withdrawal Wed 9 Sep 2026: applied 8 Nov / 9 Nov 2026 | in time / late | s 56D(3) "60 days beginning with the day after" |
| C68 | s 56D, periodic tenancy | not available | s 56D(1) "fixed-term tenancy" |
| C69 | landlord gives termination notice knowing no entitlement | unlawful act | s 60AA |
| C70 | tenant remains 91 days after termination without possession order | deemed periodic tenancy from day 90 expiry | s 60(1A) |
| C71 | fixed term 90 days with s 7 written agreement; landlord gives 90 days' notice | s 51 not applicable | s 7(1) |
| C72 | Tribunal-approved shorter period in agreement | permitted with Tribunal consent | s 52 |

## Goal 4: Entry and boarding houses

| ID | Inputs | Expected | Provision |
|---|---|---|---|
| D01 | inspection: notice 10:00 Mon 8 Jun 2026, entry 10:00 Wed 10 Jun | lawful (48 h) | s 48(2)(b) "not less than 48 hours" |
| D02 | notice 10:00 8 Jun, entry 09:00 10 Jun | unlawful (47 h) | s 48(2)(b) |
| D03 | notice 8 Jun 10:00, entry 22 Jun 10:00 (14 days) / 23 Jun 10:00 (15 days) | lawful / unlawful | s 48(2)(b) "nor more than 14 days" |
| D04 | inspection at 07:30 / 19:30 / 19:00 / 08:00 | unlawful / unlawful / lawful / lawful | s 48(2)(b) "between 8 o'clock in the morning and 7 o'clock in the evening" (R6) |
| D05 | previous inspection 10 May 2026; next 6 Jun / 7 Jun 2026 | unlawful / lawful | s 48(2)(b) "not more frequently than once in any period of 4 weeks" (R7) |
| D06 | necessary repairs, 24 h notice, 10:00 | lawful | s 48(2)(c) "at least 24 hours" |
| D07 | necessary repairs, 23 h notice | unlawful | s 48(2)(c) |
| D08 | healthy homes compliance, 24 h notice, entry 18:00 | lawful | s 48(2)(ba) |
| D09 | emergency, 02:00, no notice | lawful | s 48(2)(a) |
| D10 | tenant consent at time of entry, 21:00 | lawful | s 48(1)(a) |
| D11 | contaminant testing, notice 48 h, within hours | lawful; 24 h notice unlawful | s 48(2)(aa) "at least 48 hours but not more than 14 days" |
| D12 | suspected abandonment, rent 14 days in arrear, 24 h notice | lawful | s 48(2A),(2B) |
| D13 | suspected abandonment, rent 13 days in arrear | not permitted under (2B) | s 48(2A)(a) "at least 14 days in arrear" |
| D14 | showing to prospective purchasers without tenant consent | unlawful | s 48(3) "With the prior consent of the tenant" |
| D15 | landlord uses force to enter while tenant is present | offence; max 3 months / $3,000 | s 48(5),(6) |
| D16 | boarding room entry with 24 h notice, purpose stated, at 17:30 | lawful | s 66R(2) |
| D17 | boarding room entry with 24 h notice at 18:30 | unlawful | s 66R(2)(c) "between 8 am and 6 pm" |
| D18 | boarding room entry with 23 h notice | unlawful | s 66R(2)(a) |
| D19 | boarding room, emergency, reasonable belief | lawful at any time | s 66R(1)(b) |
| D20 | boarding room inspection, previous inspection 3 weeks ago | not a permitted purpose | s 66S(1)(i) "no entry for that purpose … within the last 4 weeks" |
| D21 | landlord enters common facilities of boarding house at any time | lawful | s 66Q(1) |
| D22 | s 66X abandonment notice on door 10:00 1 Jul 2026; enter 10:00 / 09:59 2 Jul | lawful / unlawful | s 66X(2) "at least 24 hours" |
| D23 | s 66X termination notice put on door 10:00 3 Jul 2026; earliest termination | 10:00 5 Jul 2026 | s 66X(4) "no sooner than 48 hours" |
| D24 | boarding house, landlord, no reason, served 2 Mar 2026 | 28 days, earliest 30 Mar 2026 | s 66U(1)(d) |
| D25 | boarding house, also service tenancy | 14 days | s 66U(1)(c) |
| D26 | boarding house, rent-arrears demand period 10 days unmet | 48 hours' notice | s 66U(1)(b)(i) "not less than 10 days" |
| D27 | arrears demand period 9 days | 48-hour ground not available | s 66U(1)(b)(i) |
| D28 | illegal use | 48 hours | s 66U(1)(b)(ii) |
| D29 | tenant caused serious damage | immediately | s 66U(1)(a) |
| D30 | boarding tenant terminates | 48 hours, oral allowed | s 66V(1),(2) |
| D31 | sole boarding tenant dies 14:00 10 Aug 2026 | terminates 14:00 12 Aug 2026 | s 66W "48 hours after the death" |
| D32 | boarding landlord notice without reason, giving 28 days | valid; with 20 days invalid | s 66U(1)(d) |

## Goal 5: The Tribunal

| ID | Inputs | Expected | Provision |
|---|---|---|---|
| E01 | claim $100,000 | within jurisdiction | s 77(5) "in excess of $100,000" |
| E02 | claim $100,001 | outside (unless excess abandoned) | s 77(5),(6) |
| E03 | claim $120,000, claimant abandons $20,000 | within | s 77(6) |
| E04 | termination notice received Tue 1 Sep 2026; no-effect application 9 Oct 2026 | in time (28th working day) | s 54(3) "within 28 working days after receiving" |
| E05 | same, application Mon 12 Oct 2026 | out of time | s 54(3) |
| E06 | notice received 10 Dec 2026; deadline | Thu 28 Jan 2027 | s 54(3), Christmas block |
| E07 | notice declared retaliatory | unlawful act | s 54(6) |
| E08 | work order dated 1 Mar 2026; enforce 1 Mar 2027 / 2 Mar 2027 without leave | allowed / leave needed | s 108(7) "After the expiration of 12 months" |
| E09 | tenant's unlawful-act application, act committed 15 Apr 2026: filed 15 Apr 2027 / 16 Apr 2027 | in time / out of time | s 109(2)(b) "12 months after the date of commission" |
| E10 | failure to lodge bond (s 19(2)) committed Jan 2025; tenancy terminated 30 Nov 2026; filed 30 Nov 2027 / 1 Dec 2027 | in time / late | s 109(2)(a)(i) "12 months after the termination of the tenancy" |
| E11 | failure to keep bond records (s 30(2)) — termination rule | 12 months after termination | s 109(2)(a)(ii) |
| E12 | failure to keep rent records (s 30) | 12 months after commission | s 109(2)(b) (only "records in respect of bonds" get the termination rule) |
| E13 | chief executive aware 1 Jun 2026; applies 1 Jun 2027 / 2 Jun 2027 | in time / late | s 109(2A) |
| E14 | exemplary damages claimed $5,000, Schedule 1A max (input) $4,500 | award at most $4,500 | s 109(4) |
| E15 | claimed $3,000, max $4,500 | up to $3,000 (no cap bite) | s 109(4) |
| E16 | pecuniary penalty $50,000 / $50,001 | within max / exceeds | s 109C "is $50,000" |
| E17 | pecuniary penalty: landlord of 6 tenancies, intentional s 60AA act, CE applies | eligible | s 109B(1)(a)(i) |
| E18 | landlord of 5 tenancies (not boarding house) | not eligible | s 109B(1)(a) |
| E19 | landlord of 1 boarding house | eligible | s 109B(1)(a)(ii) |
| E20 | 6 tenancies, but unlawful act is s 18 bond excess (not listed) | not eligible | s 109B(1)(b) list |
| E21 | CE aware 1 Jun 2026; pecuniary penalty applied 1 Jun 2027 / 2 Jun 2027 | in time / late | s 109B(2) |
| E22 | applicant for exemplary damages is a neighbour (not landlord/tenant/CE) | cannot apply | s 109(1) |
| E23 | unlawful act not intentional (non-s 54(6)) | no exemplary damages | s 109(3) "committed the unlawful act intentionally" |
| E24 | s 54(6) retaliatory notice, intent not shown | exemplary damages may be ordered | s 109(3A) |
| E25 | restraining order term 6 years / 7 years | allowed / not | s 109A(3) "may not exceed 6 years" |

## Not expressible

(Filled in after reading the rule modules; expected values above unchanged.)

The encoding takes these facts as already-decided inputs, or has no function or input for them, so no
input/output test can be written:

- A28 (boarding-house carve-out of the landlord-residence exclusion), A29-A31 only test the exclusion
  as an input constructor, A26/A27 likewise; the facts behind s 5 are inputs by the brief.
- B07 tested; B09 tested. B20 (bond receipt), B37 (s 24A reinstatement), B43 (s 26 duration),
  s 18(3)/18AA(4) refunds: no function.
- C14, C15, C19, C30, C33: the encoding takes the ground as an input constructor (e.g. "s 55AA a
  physical assault for which a charge has been filed"), so the absence of a fact behind a ground
  cannot be put.
- C27, C28 (s 56B(2)-(3) effect of withdrawal), C59, C60 (s 62(1), 62A(2) immediate disposal), C68
  (s 56D on a periodic tenancy), C69 (s 60AA), C72 (s 52): no function or input.
- C70 is tested using a termination date of 30 Jun 2026 (rule as stated: the periodic tenancy runs
  from expiry of the 90 days, i.e. 28 Sep 2026).
- D10 (consent), D14 (showing without consent), D15 (force), D19 (boarding emergency), D20 (s 66S(1)(i)
  4-week rule is folded into a boolean input), D21 (s 66Q): no function or input.
- D22/D23/D31: only the calendar day is computed; the hour-level edge (10:00 vs 09:59) is not
  expressible. D32 is covered by the D24 tests.
- E07 (s 54(6)), E20 (which unlawful act for s 109B(1)(b)), E21 (s 109B(2) time limit), E22 (non-party
  applicant: "Who applies" has no such value), E25 (s 109A(3)): no function or input.
- B66 is tested as "no deadline" (NOTHING).

