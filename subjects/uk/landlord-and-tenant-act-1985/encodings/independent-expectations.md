# Independent expectations: Landlord and Tenant Act 1985

Written from BRIEF.md and the revised text (point in time 29 June 2026) only, before any `.l4` file was opened. Each scenario gives the inputs, the expected answer and the Act's words. Date arithmetic follows the brief's readings.

## Date conventions used (from the brief)

- "N days beginning with X" ends on X + N − 1.
- "N months beginning with X" ends on the day before the corresponding date N months later, or, where that month has no corresponding date, on the last day of that month.
- "Term of less than seven years": the term, counted from the grant, ends before the last day of the seven years beginning with the grant.
- s 20B(1): barred when the demand is served after the last day of the 18 months beginning with the day the costs were incurred. s 20B(2) notice saves if given on or before that last day.
- s 3(1): the rent day is "within two months" if on or before the corresponding date two months after the assignment (month-end fallback: last day of the month); then the deadline is that corresponding date ("the end of that period of two months"); otherwise the deadline is the rent day.
- s 22(2): request on or before the corresponding date six months after obtaining the summary. s 22(4): facilities start on or before the corresponding date one month after the request.

## Goal 1a: s 11 application (ss 13, 14)

Default lease unless stated: dwelling-house in England, granted 1 Jan 2020, term from grant, no break, no renewal option, no exclusion facts.

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R1 | Term 1 Jan 2020 – 31 Dec 2022 (3 years) | s 11 applies | s 13(1) "granted on or after 24th October 1961 for a term of less than seven years" |
| R2 | Term 1 Jan 2020 – 30 Dec 2026 (one day short of 7 years) | applies | s 13(1) |
| R3 | Term 1 Jan 2020 – 31 Dec 2026 (exactly 7 years) | does not apply | s 13(1) "less than seven years" |
| R4 | Term 1 Jan 2020 – 31 Dec 2029 (10 years) | does not apply | s 13(1) |
| R5 | Granted 29 Feb 2020, term ends 27 Feb 2027 | applies (7 years beginning 29 Feb 2020 end 28 Feb 2027) | s 13(1); brief's month-end rule |
| R6 | Granted 29 Feb 2020, term ends 28 Feb 2027 | does not apply | same |
| R7 | Term stated to start 1 Jan 2019, 8 years (ends 31 Dec 2026), lease granted 1 Jun 2020 | applies (from grant, term 1 Jun 2020 – 31 Dec 2026 < 7 years) | s 13(2)(a) "any part of the term which falls before the grant shall be left out of account" |
| R8 | 10-year term from grant 1 Jan 2020, lessor may determine at 5 years | applies | s 13(2)(b) "determinable at the option of the lessor before the expiration of seven years ... treated as ... less than seven years" |
| R9 | 3-year term, lessee option to renew for 4 more years (total 7) | does not apply | s 13(2)(c) "together with the original term, amounts to seven years or more" |
| R10 | 3-year term, lessee option to renew for 3 years (total 6) | applies | s 13(2)(c) not met |
| R11 | 3-year term, lessee renewal option (total 7+) AND lessor break before 7 years | applies | s 13(2)(c) "(other than a lease to which paragraph (b) applies)" |
| R12 | 3-year lease granted 23 Oct 1961 | does not apply | s 13(1) "granted on or after 24th October 1961" |
| R13 | 3-year lease granted 24 Oct 1961 | applies | s 13(1) |
| R14 | Dwelling in Wales, subject to an occupation contract, 3 years | does not apply | s 13(1ZA) |
| R15 | Dwelling in Wales, not an occupation contract, 3 years | applies | s 13(1) |
| R16 | England, assured tenancy immediately before RRA 2025 commencement, granted for 10 years, by a private landlord (not PRP) | does not apply | s 13(1ZC) |
| R17 | Same as R16 but granted by a private registered provider, and within (1AA) (fixed term > 7 years, would be assured but for term, not shared ownership, granted after 1 Apr 2012) | applies | s 13(1ZC)(b)(ii) not met; s 13(1AA) |
| R18 | England, secure tenancy, fixed term 10 years, by s 80(1) landlord, granted 1 Jan 2020 (after Localism s 166, 1 Apr 2012) | applies | s 13(1A)(a) "secure tenancy for a fixed term of seven years or more" |
| R19 | As R18, term exactly 7 years (1 Jan 2020 – 31 Dec 2026) | applies | s 13(1A)(a) "seven years or more" |
| R20 | As R18 but granted 1 Jan 2011 (before Localism s 166) | does not apply | s 13(1A) "granted on or after the day on which section 166 ... came into force" |
| R21 | England, 10-year fixed term, would be assured but for term, not shared ownership, granted by PRP, 1 Jan 2020 | applies | s 13(1AA) |
| R22 | As R21 but a shared ownership lease | does not apply | s 13(1AA)(b) |
| R23 | As R21 but granted by a private landlord (not PRP) | does not apply | s 13(1AA)(c) |
| R24 | As R21 but term exactly 7 years | does not apply (not "more than seven years", and not "less than seven years") | s 13(1AA) "fixed term of more than seven years" |
| R25 | 3-year lease granted to an existing tenant whose previous lease was not an s 11 lease (e.g. 21-year lease) | does not apply | s 14(1) |
| R26 | 3-year lease granted to an existing tenant whose previous lease was an s 11 lease | applies | s 14(1) not met |
| R27 | 3-year lease to existing tenant; previous lease granted before 24 Oct 1961, would have been s 11 lease if granted after | applies | s 14(1) "(and, in the case of a lease granted before 24th October 1961, would not have been ...)" |
| R28 | 3-year lease that is an agricultural holding (AHA 1986 applies) / farm business tenancy | does not apply | s 14(3) |
| R29 | 3-year lease granted 1 Jan 2020 to a local authority | does not apply | s 14(4) |
| R30 | 3-year lease granted 2 Oct 1980 to a local authority | applies | s 14(4) "granted on or after 3rd October 1980" |
| R31 | 3-year lease granted 3 Oct 1980 to a local authority | does not apply | s 14(4) |
| R32 | 3-year lease granted to the Crown, not Crown Estate managed | does not apply | s 14(5)(a) |
| R33 | 3-year lease granted to the Crown, under Crown Estate Commissioners' management | applies | s 14(5)(a) "(unless ...)" |

## Goal 1b: s 9A application and first day it bites (s 9B)

Commencement date (input) 20 Mar 2019. Default: dwelling in England, let wholly or mainly for human habitation, fixed 1-year term from grant.

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| F1 | Granted 20 Mar 2019, term begins 20 Mar 2019 | applies; bites 20 Mar 2019 | s 9B(3)(a) "before the commencement date" not met; s 9A(1)(a) "at the time the lease is granted" |
| F2 | Granted 19 Mar 2019, fixed term, not periodic/secure | does not apply | s 9B(3)(a) |
| F3 | Granted 1 May 2019, term begins 1 Jun 2019 | applies; bites 1 Jun 2019 | s 9A(1)(a) "or, if later, at the beginning of the term" |
| F4 | Granted 1 May 2019 under an agreement made 1 Mar 2019 | does not apply | s 9B(3)(b) |
| F5 | Periodic tenancy granted 1 Jan 2015, in existence on 20 Mar 2019 | applies; bites 20 Mar 2020 | s 9B(4): 12 months beginning 20 Mar 2019 end 19 Mar 2020; "the time that begins at the end" |
| F6 | Secure tenancy granted 1 Jan 2000, existing on commencement | applies; bites 20 Mar 2020 | s 9B(4) |
| F7 | Same as F5 with commencement date 31 Jan 2019 (hypothetical input) | bites 31 Jan 2020 | s 9B(4) |
| F8 | Fixed term granted 1 Jan 2018 for 2 years; on expiry a periodic tenancy arises 1 Jan 2020 | applies; bites 1 Jan 2020 | s 9B(5) |
| F9 | Fixed term granted 1 Jan 2018, renewed for a further fixed term on 1 Jan 2020 | applies; bites 1 Jan 2020 | s 9B(6) "treated as a grant of the lease on or after that date" |
| F10 | Dwelling in Wales | does not apply | s 9A(1) "of a dwelling in England" |
| F11 | Not let wholly or mainly for human habitation | does not apply | s 9B(1) |
| F12 | Granted 1 Jan 2020, 10-year term, no break | does not apply | s 9B(1)(a) |
| F13 | Granted 1 Jan 2020, 10-year term, lessor break at year 3 | applies; bites 1 Jan 2020 | s 9B(8)(b) |
| F14 | Granted 1 Jan 2020, 3 years + lessee renewal of 5 years | does not apply | s 9B(8)(c) |
| F15 | Granted 1 Jan 2020, 10-year secure tenancy by s 80(1) landlord (s 13(1A) kind) | applies; bites 1 Jan 2020 | s 9B(1)(b) |
| F16 | Granted 1 Jan 2020, 1-year term, to a local authority | does not apply | s 9B(2) via s 14(4) |
| F17 | Granted 1 Jan 2020 to existing tenant whose previous lease was not an s 11 lease | does not apply | s 9B(2) via s 14(1) |
| F18 | Term exactly 7 years from grant 1 Jan 2020 (ends 31 Dec 2026) | does not apply | s 9B(1)(a) "less than 7 years" |

## Goal 2: service charges

Each item: amount, reasonable part (s 19 input), date incurred, optional date of s 20B(2) notice. Demand date. Qualifying works: appropriate amount, complied / dispensed.

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| S1 | One item 1000, reasonable 800, incurred 1 Jan 2025, demand 1 Feb 2025 | payable 800 | s 19(1)(a) "only to the extent that they are reasonably incurred" |
| S2 | Items 1000 (reasonable 1000) and 500 (reasonable 300), recent | payable 1300 | s 19(1) |
| S3 | Item incurred 15 Jan 2023, demand 14 Jul 2024 | not barred (18 months beginning 15 Jan 2023 end 14 Jul 2024) | s 20B(1) "more than 18 months before" |
| S4 | Same, demand 15 Jul 2024, no notice | barred: item contributes 0 | s 20B(1) |
| S5 | Same as S4, s 20B(2) notice 14 Jul 2024 | not barred | s 20B(2) "within the period of 18 months beginning with" |
| S6 | Same as S4, notice 15 Jul 2024 | barred | s 20B(2) |
| S7 | Incurred 31 Aug 2023, demand 28 Feb 2025 | not barred (no 31 Feb 2025 → period ends 28 Feb 2025) | s 20B(1); month-end rule |
| S8 | Incurred 31 Aug 2023, demand 1 Mar 2025 | barred | s 20B(1) |
| S9 | Incurred 31 Aug 2023, demand 1 Mar 2025, notice 28 Feb 2025 | not barred | s 20B(2) |
| S10 | Incurred 28 Aug 2023, demand 28 Feb 2025 | barred (period ends 27 Feb 2025) | s 20B(1) |
| S11 | Incurred 29 Feb 2024, demand 28 Aug 2025 → ok; demand 29 Aug 2025 → barred | period ends 28 Aug 2025 | s 20B(1) |
| S12 | Incurred 30 Aug 2023: last day 28 Feb 2025 (no 30 Feb) | demand 28 Feb 2025 ok; 1 Mar 2025 barred | month-end rule |
| S13 | Two items: A 1000 incurred 1 Jan 2023, B 500 incurred 1 Jan 2025, demand 1 Mar 2025 | payable 500 (A barred) | s 20B(1) "so much of the service charge as reflects the costs so incurred" |
| S14 | Qualifying works, tenant contribution 2000 (reasonable 2000), appropriate amount 250, not consulted, not dispensed | payable 250 | s 20(1), (7) |
| S15 | Same, consultation complied with | payable 2000 | s 20(1)(a) |
| S16 | Same, dispensed with by tribunal | payable 2000 | s 20(1)(b) |
| S17 | Qualifying works contribution 250, appropriate 250, not consulted | payable 250 (s 20 does not apply: does not exceed) | s 20(3) "exceed an appropriate amount" |
| S18 | Qualifying works, contribution 3000, reasonable 2000, appropriate 250, not consulted | payable 250 | s 19 then s 20 |
| S19 | Qualifying works, reasonable 200, appropriate 250, not consulted | payable 200 | cap not binding |
| S20 | Qualifying works item barred by s 20B | payable 0 | s 20B(1) |
| S21 | Ordinary item 400 + qualifying works 2000 capped at 250 | payable 650 | ss 19, 20 |
| S22 | Demand accompanied by s 21B summary | may not withhold | s 21B(3) |
| S23 | Demand not accompanied by summary | may withhold | s 21B(3) "may withhold payment ... if subsection (1) is not complied with" |
| S24 | No items | payable 0 | — |

## Goal 3: information about the landlord

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| I1 | s 1 request received 1 Mar 2025 | last day 21 Mar 2025 | s 1(1) "within the period of 21 days beginning with the day on which he receives the request" |
| I2 | received 15 Feb 2024 (leap) | 6 Mar 2024 | s 1(1) |
| I3 | received 25 Dec 2025 | 14 Jan 2026 | s 1(1) |
| I4 | received 10 Feb 2025 | 2 Mar 2025 | s 1(1) |
| A1 | Assignment 10 Jan 2025, next rent day 1 Feb 2025 | deadline 10 Mar 2025 | s 3(1) "if that is within two months of the assignment, the end of that period of two months" |
| A2 | Assignment 10 Jan 2025, next rent day 10 Mar 2025 | 10 Mar 2025 | s 3(1) (rent day within two months) |
| A3 | Assignment 10 Jan 2025, next rent day 11 Mar 2025 | 11 Mar 2025 | s 3(1) "not later than the next day on which rent is payable" |
| A4 | Assignment 10 Jan 2025, next rent day 1 Jun 2025 | 1 Jun 2025 | s 3(1) |
| A5 | Assignment 31 Dec 2024, rent day 1 Jan 2025 | 28 Feb 2025 | s 3(1); month-end fallback |
| A6 | Assignment 31 Dec 2024, rent day 1 Mar 2025 | 1 Mar 2025 | s 3(1) |
| A7 | Assignment 31 Dec 2023, rent day 1 Jan 2024 | 29 Feb 2024 | s 3(1) |
| A8 | Assignment 31 Dec 2024, rent day 28 Feb 2025 | 28 Feb 2025 | s 3(1) |
| A9 | Assignment 30 Apr 2025, rent day 1 May 2025 | 30 Jun 2025 | s 3(1) |
| L1 | Assignment 1 Mar 2025; new landlord notice 1 May 2025; old landlord notice 15 Apr 2025 | relevant period ends 15 Apr 2025 | s 3(3B) "whichever happens first" |
| L2 | Only new landlord notice 1 May 2025 (late or not) | ends 1 May 2025 | s 3(3B)(a) "(whether in accordance with subsection (1) or not)" |
| L3 | No notice at all | no end yet | s 3(3B) |
| L4 | Old landlord liable for breach on 10 Apr 2025, period ending 15 Apr 2025 | liable | s 3(3A) |
| L5 | Breach on 20 Apr 2025, period ending 15 Apr 2025 | not liable | s 3(3A) |
| P1 | Summary obtained 15 Mar 2025 | last day for s 22 request 15 Sep 2025 | s 22(2) "within six months of obtaining the summary" |
| P2 | Summary obtained 31 Aug 2025 | 28 Feb 2026 | s 22(2); month-end fallback |
| P3 | Summary obtained 31 Aug 2023 | 29 Feb 2024 | s 22(2) |
| P4 | Request 15 Jan 2025 | facilities start no later than 15 Feb 2025 | s 22(4) "beginning not later than one month after the request" |
| P5 | Request 31 Jan 2025 | 28 Feb 2025 | s 22(4) |
| P6 | Request 31 Jan 2024 | 29 Feb 2024 | s 22(4) |

## Ambiguities and readings

1. **s 13(1ZC) and s 13(2)(b)**: a 10-year assured tenancy with a lessor break before 7 years. s 13(2) applies "in determining whether a lease is one to which section 11 applies", so arguably (1ZC)(b)(i) "granted for a term of seven years or more" is read through s 13(2)(b) and the exclusion fails. Not asserted.
2. **Breach on the very day the relevant period ends (s 3(3A))**: "occurring before the end of the relevant period", the period "ending with the date" of notice. I read the notice day as inside the period (old landlord liable). Low confidence; asserted only if the encoding exposes it.
3. **Localism Act 2011 s 166 commencement**: 1 April 2012 (outside the Act's text). Scenarios avoid dates near it.
4. **s 3(1) month-end**: the brief gives no explicit fallback for s 3(1); I apply the general month rule (last day of the month).
5. **s 9A bite day under s 9B(4)**: "the time that begins at the end of the period of 12 months" is read as the day after the last day (20 Mar 2020 for commencement 20 Mar 2019).
6. **s 20 cap kind**: the regulations (SI 2003/1987) set a (5)(b) per-tenant amount (£250). I treat the appropriate amount as a cap on the tenant's contribution to the works, applied after s 19.
7. **s 13(1AB)**: referred to in s 9B(1)(b) but absent from s 13 as revised; nothing asserted.
