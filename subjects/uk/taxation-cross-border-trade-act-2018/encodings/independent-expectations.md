# Independent expectations: TCTA 2018 Part 1 (liability, persons, amount, notification)

Written from BRIEF.md and the source text (ss 2-7, 16; Sch 6 paras 1, 4) only, before any `.l4` file was opened.

Date convention (Sch 6 para 4(1), "before the end of the period of 3 years beginning with the day on which the liability was incurred"): the period includes the day of incurrence, so the last day for notification is the day before the corresponding date 3 (or 20) years later; where that later year has no corresponding date (29 February), the last day is the last day of February. The brief's convention and my reading agree; a notification given on the last day is in time, one given the day after is not.

## Goal 1: when a liability is incurred

| # | Facts | Expected | Source |
|---|---|---|---|
| L1 | Domestic goods, declared for free circulation, accepted 10 Mar 2026 | not chargeable; no liability | s 2(1) "chargeable goods ... unless they are domestic goods" |
| L2 | Non-domestic goods, free circulation, accepted 10 Mar 2026 | chargeable; liability incurred 10 Mar 2026 | s 4(1) "at the time of the acceptance" |
| L3 | Free circulation, declaration made 10 Mar 2026 but not (yet) accepted | no liability incurred under s 4(1) | s 4(1)(b) "HMRC accept the declaration" |
| L4 | Storage, entitled, no breach | no liability | s 4(2) "general rule ... not incurred" |
| L5 | Transit, entitled, no breach | no liability | s 4(2)(b) |
| L6 | Inward processing, entitled, no breach | no liability | s 4(2)(c) |
| L7 | Storage, no entitlement, declaration made 5 Apr 2026 | liability on 5 Apr 2026 | s 4(3)(a) "at the time the (purported) declaration is made" |
| L8 | Transit, entitled, breach first occurs 20 Jun 2026 | liability on 20 Jun 2026 | s 4(3)(b) "at the time at which the breach first occurs" |
| L9 | Inward processing, entitled, breach 31 Dec 2026 | liability on 31 Dec 2026 | s 4(3)(b) |
| L10 | Storage, no entitlement (declared 5 Apr 2026) and a breach 1 May 2026 | liability on 5 Apr 2026 (the earlier of the two exceptions; liability is first incurred on the purported declaration) | s 4(3)(a),(b) |
| L11 | Authorised use, entitled, accepted 1 Feb 2026, no breach | liability on 1 Feb 2026 at the reduced (lower) rate | s 4(4)(a),(b) |
| L12 | Temporary admission, not entitled, accepted 1 Feb 2026 | liability on 1 Feb 2026 at the normal rate | s 4(4)(a),(c) |
| L13 | Authorised use, entitled, accepted 1 Feb 2026, breach 1 Aug 2026 | liability on 1 Feb 2026 (reduced rate) and a further liability on 1 Aug 2026 at the normal rate less the earlier liability | s 4(4)(a),(d) |
| L14 | Goods imported 3 Mar 2026, not presented to Customs (required) | liability on 3 Mar 2026, the time of importation/forfeiture | s 5(1), 5(2)(a) |
| L15 | Goods presented but no declaration made; liable to forfeiture 17 Mar 2026 | liability on 17 Mar 2026 | s 5(2)(b) "at the time at which the goods become liable to forfeiture" |
| L16 | Domestic goods, not presented | no liability (not chargeable) | s 2(1), s 5(1) "chargeable goods" |
| L17 | Domestic goods, storage, no entitlement | no liability | s 2(1) |

## Goal 2: who is liable

| # | Facts | Expected | Source |
|---|---|---|---|
| P1 | Free circulation; declaration in the name of A, no one else | {A}; not joint | s 6(1) |
| P2 | Declaration in name of agent A on behalf of B | {A, B}; jointly and severally | s 6(1), 6(3)(a), 6(7) |
| P3 | Goods not presented; C in possession on entry | {C} | s 6(2) |
| P4 | Not presented; C in possession; D participated in the breach knowing of it | {C, D}; joint and several | s 6(2), 6(3)(d), 6(4)(c), 6(7) |
| P5 | Declaration by A; E provided false information and ought reasonably to have known | {A, E} | s 6(4)(a) |
| P6 | Declaration by A; F involved in breach but neither knew nor ought to have known | {A}; F not liable | s 6(4) "knew, or ought reasonably to have known" |
| P7 | Declaration by A on behalf of A (same person) | {A} once; not joint | s 6(1), 6(7) "two or more persons" |
| P8 | No liability incurred (e.g. storage, no breach), declarant A | no one liable | s 6 presupposes a liability |
| P9 | Declaration by A on behalf of B; D knowingly involved | {A, B, D}; joint and several | s 6(3), 6(7) |

## Goal 3: amount, time limit and enforceability

Amount (s 7, s 16(2)-(3)): ad valorem duty = rate x transaction value.

| # | Facts | Expected | Source |
|---|---|---|---|
| A1 | rate 12%, value 10,000 | 1,200 | s 7(1), s 16(2) |
| A2 | rate 0%, value 50,000 | 0 | s 7 |
| A3 | rate 2.5%, value 3,333 | 83.325 (exact) | s 7 |
| A4 | rate 100%, value 1 | 1 | s 7 |

Last day for notification (Sch 6 para 4):

| # | Incurred | Offence? | Expected last day | Source |
|---|---|---|---|---|
| N1 | 15 Mar 2026 | no | 14 Mar 2029 | para 4(1) |
| N2 | 15 Mar 2026 | yes | 14 Mar 2046 | para 4(2) "extended to a period of 20 years" |
| N3 | 29 Feb 2024 | no | 28 Feb 2027 (no 29 Feb 2027) | para 4(1); brief convention |
| N4 | 29 Feb 2024 | yes | 28 Feb 2044 (29 Feb 2044 exists; day before it) | para 4(2) |
| N5 | 1 Mar 2025 | no | 29 Feb 2028 (day before 1 Mar 2028, a leap year) | para 4(1) |
| N6 | 1 Jan 2026 | no | 31 Dec 2028 | para 4(1) |
| N7 | 31 Jan 2026 | no | 30 Jan 2029 | para 4(1) |
| N8 | 31 Dec 2026 | no | 30 Dec 2029 | para 4(1) |
| N9 | 1 Mar 2024 | no | 28 Feb 2027 | para 4(1) |

Enforceability (Sch 6 para 1, para 4):

| # | Facts | Expected | Source |
|---|---|---|---|
| E1 | Incurred 15 Mar 2026, no offence, notified 13 Mar 2029 | enforceable | para 1, para 4(1) |
| E2 | same, notified 14 Mar 2029 (last day) | enforceable | para 4(1) |
| E3 | same, notified 15 Mar 2029 (day after) | not enforceable | para 4(1) |
| E4 | same, never notified | not enforceable | para 1 "may not be enforced unless ... notified" |
| E5 | Incurred 15 Mar 2026, offence, notified 15 Mar 2029 | enforceable | para 4(2) |
| E6 | Incurred 15 Mar 2026, offence, notified 14 Mar 2046 | enforceable | para 4(2) |
| E7 | Incurred 15 Mar 2026, offence, notified 15 Mar 2046 | not enforceable | para 4(2) |
| E8 | Incurred 29 Feb 2024, no offence, notified 28 Feb 2027 | enforceable | para 4(1) |
| E9 | Incurred 29 Feb 2024, no offence, notified 1 Mar 2027 | not enforceable | para 4(1) |
| E10 | Incurred 1 Mar 2025, no offence, notified 29 Feb 2028 | enforceable; notified 1 Mar 2028 not enforceable | para 4(1) |
| E11 | Incurred on the notification day itself (15 Mar 2026, notified 15 Mar 2026) | enforceable | para 4(1) period includes the first day |

## End-to-end (top-level goal)

| # | Facts | Expected |
|---|---|---|
| T1 | Free circulation, accepted 10 Mar 2026, A declarant on behalf of B, rate 10%, value 20,000, no offence, notified 9 Mar 2029 | liability 10 Mar 2026; A and B jointly and severally; duty 2,000; last day 9 Mar 2029; enforceable |
| T2 | Same but notified 10 Mar 2029 | not enforceable |
| T3 | Storage, entitled, no breach | no liability, nothing due |

## Points where the Act may not answer

- A notification dated before the liability was incurred: para 4 sets only an end, but para 2 requires HMRC to "consider that a person is liable", so I would not treat it as valid; not tested.
- Free circulation not accepted (L3): s 4(1) gives no liability; whether s 5(2)(b) applies depends on whether a declaration counts as "made", which is not an input.
