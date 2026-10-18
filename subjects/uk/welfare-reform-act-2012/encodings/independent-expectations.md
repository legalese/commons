# Independent expectations: Welfare Reform Act 2012 (ss 3-5, 8; 77-83; 96)

Written from BRIEF.md and the Act (revised text, point in time 1 July 2026) only,
before any `.l4` file was opened. Amounts are exact rationals (pounds).

## Readings adopted (following the brief)

- R1. s 4(1)(a) "at least 18 years old": met from (and including) the 18th birthday.
- R2. s 4(1)(b) "has not reached the qualifying age": met only on days strictly before
  the qualifying-age date; on that date the condition fails.
- R3. s 5(1)(a)/(2)(a) "not greater than a prescribed amount": capital equal to the limit passes.
- R4. s 5(1)(b)/(2)(b) "would not be less than any prescribed minimum": the notional award
  (s 8 amount) equal to the minimum passes; one penny below fails.
- R5. s 8(1) "the balance of ... less ...": maximum amount minus deductions, floored at 0
  (brief: "not below nothing").
- R6. s 3(2): joint claimants entitled only if EACH meets the basic conditions and they jointly
  meet the financial conditions (combined capital, combined income).
- R7. PIP s 78/79: "severely limited" -> enhanced; "limited" (not severely) -> standard; both
  need the required period condition (an input). "Not limited" -> no component.
- R8. s 82: applies only if terminally ill AND claim made expressly on that ground. Then
  daily living = enhanced regardless of finding and required period; mobility keeps the
  limitation and age tests but the required period condition is dropped.
- R9. s 77(4): entitled to a Scottish payment -> no PIP at all (both components none),
  even if terminally ill.
- R10. s 83: relevant age date = later of pensionable-age date and 65th birthday. Entitled
  ON that date; not entitled on any day after it.
- R11. s 79(1)(a)/(2)(a) mobility age condition is an input; false -> no mobility component
  (daily living unaffected).
- R12. s 96: relevant amount = annual limit x days / 365, no rounding. Reduction =
  total - relevant amount if positive, else 0. Exactly at the relevant amount -> 0 ("exceeds").

## Ambiguities recorded

- A1. 29 February birthdays: the 18th birthday in a non-leap year (28 Feb or 1 Mar?) is not
  answered by the Act. Not asserted except 1 March (18 under either reading).
- A2. s 96(2) says "reduced by an amount up to or equalling the excess"; the brief tells us
  the reduction is the excess. I assert the excess.
- A3. Whether the award (s 8) is reported when entitlement fails: I only assert the award amount
  through the award function and entitlement separately.
- A4. Whether an "infinite"/missing prescribed minimum means none: not tested.

## Scenarios

Base UC claimant ("Alice"): born 15 Mar 1990; qualifying age 15 Mar 2056; in GB; not in
education; commitment accepted. Day 1 Jul 2026. Capital £5,000, limit £16,000. Elements:
standard 400.14, children 339, housing 600, other 0 -> maximum 1339.14. Earned deduction 200,
unearned 100 -> award 1039.14. Minimum 0.01.

### Universal credit — basic conditions (s 4(1))

| # | Scenario | Expected | Act |
|---|---|---|---|
| U1 | Alice on 1 Jul 2026 | basic conditions met | s 4(1)(a)-(e) |
| U2 | born 1 Jul 2008, day 1 Jul 2026 (18th birthday) | met | "at least 18 years old" |
| U3 | born 1 Jul 2008, day 30 Jun 2026 | not met | same |
| U4 | born 2 Jul 2008, day 1 Jul 2026 | not met | same |
| U5 | qualifying age 1 Jul 2026, day 30 Jun 2026 | met | "has not reached the qualifying age" |
| U6 | qualifying age 1 Jul 2026, day 1 Jul 2026 | not met | same |
| U7 | qualifying age 1 Jul 2026, day 2 Jul 2026 | not met | same |
| U8 | not in GB | not met | (c) "is in Great Britain" |
| U9 | receiving education | not met | (d) |
| U10 | commitment not accepted | not met | (e) |
| U11 | born 29 Feb 2008, day 1 Mar 2026 | met (A1) | (a) |

### Universal credit — financial conditions and entitlement (ss 3, 5)

| # | Scenario | Expected | Act |
|---|---|---|---|
| U12 | Alice single | entitled | s 3(1) |
| U13 | capital 16,000 = limit | entitled | "not greater than" |
| U14 | capital 16,000.01 | not entitled | same |
| U15 | award equals minimum (max 500, ded 400, min 100) | entitled | "not be less than any prescribed minimum" |
| U16 | award 99.99 vs minimum 100 | not entitled | same |
| U17 | deductions exceed maximum (award 0), minimum 0.01 | not entitled | same |
| U18 | single, under 18 | not entitled | s 3(1)(a) |
| U19 | joint, both meet basic, combined capital 10,000 | entitled | s 3(2) |
| U20 | joint, second claimant 17 | not entitled | s 3(2)(a) "each of them" |
| U21 | joint, first claimant reached qualifying age | not entitled | s 3(2)(a) |
| U22 | joint, combined capital 16,000.01 (each under limit, e.g. 8,000 + 8,000.01) | not entitled | s 5(2)(a) "combined capital" |
| U23 | joint, combined award below minimum | not entitled | s 5(2)(b) |

### Universal credit — award (s 8)

| # | Scenario | Expected | Act |
|---|---|---|---|
| U24 | elements 400.14 + 339 + 600 + 0 | maximum 1339.14 | s 8(2) |
| U25 | max 1339.14, ded 200 + 100 | award 1039.14 | s 8(1),(3) |
| U26 | ded 1339.14 exactly | award 0 | s 8(1) |
| U27 | ded 1000 + 1000 > max 1339.14 | award 0 (not negative) | brief "not below nothing" |
| U28 | no deductions | award = maximum 1339.14 | s 8(1) |
| U29 | only standard allowance 400.14, earned ded 50.5 | 349.64 | s 8 |

### PIP — components (ss 77(4), 78, 79, 81, 82, 83)

Base person "Pat": born 1 Jan 1980, pensionable age 1 Jan 2047 (67), day 1 Jul 2026, mobility
age condition met, not terminally ill, no Scottish payment.

| # | Scenario (DL finding / DL RPC / Mob finding / Mob RPC) | Expected DL / Mob | Act |
|---|---|---|---|
| P1 | limited / yes / limited / yes | standard / standard | 78(1), 79(1) |
| P2 | severely / yes / severely / yes | enhanced / enhanced | 78(2), 79(2) |
| P3 | limited / no / limited / no | none / none | 78(1)(b), 79(1)(c) |
| P4 | severely / no / severely / no | none / none | required period |
| P5 | not limited / yes / not limited / yes | none / none | |
| P6 | severely / yes / limited / yes | enhanced / standard | |
| P7 | limited / yes / severely / no | standard / none | |
| P8 | not limited / no / severely / yes | none / enhanced | |
| P9 | P2 with mobility age condition not met | enhanced / none | 79(1)(a),(2)(a) |
| P10 | terminally ill + express claim, DL not limited, no RPC; mob severely, no RPC | enhanced / enhanced | 82(2),(3) |
| P11 | terminally ill + express claim, mob limited, no RPC | DL enhanced / mob standard | 82(3) |
| P12 | terminally ill + express claim, mob not limited | enhanced / none | 82(3) drops only (c) |
| P13 | terminally ill but claim NOT express, DL not limited | none / per normal rules | 82(1)(b) |
| P14 | terminally ill + express, mob age condition not met, mob severely | enhanced / none | 79(2)(a) still applies |
| P15 | P2 but entitled to Scottish adult disability payment | none / none | 77(4) |
| P16 | terminal + express but Scottish payment | none / none | 77(4) |

### PIP — relevant age (s 83)

| # | Scenario | Expected | Act |
|---|---|---|---|
| P17 | born 1 Jan 1960, pensionable 1 Jan 2027 (67) — relevant age date | 1 Jan 2027 | 83(2) "or if higher, 65" |
| P18 | same, day 1 Jan 2027 (P2 findings) | enhanced / enhanced | "after the person reaches" |
| P19 | same, day 2 Jan 2027 | none / none | 83(1) |
| P20 | born 6 Mar 1950, pensionable 6 Nov 2011 (below 65) — relevant age date | 6 Mar 2015 | 83(2)(b) |
| P21 | same, day 1 Jan 2013 (after pensionable, before 65) | P2 rates (entitled) | |
| P22 | same, day 6 Mar 2015 | entitled | |
| P23 | same, day 7 Mar 2015 | none / none | |
| P24 | pensionable age = 65th birthday (born 1 Jun 1955, pensionable 1 Jun 2020) | relevant 1 Jun 2020; 2 Jun 2020 none | |
| P25 | terminally ill + express, day after relevant age | none / none | 83(1) applies to both |

### Benefit cap (s 96)

| # | Scenario | Expected | Act |
|---|---|---|---|
| C1 | London, higher limit | 25,323 | 96(5A)(a) |
| C2 | London, lower | 16,967 | same |
| C3 | elsewhere, higher | 22,020 | 96(5A)(b) |
| C4 | elsewhere, lower | 14,753 | same |
| C5 | elsewhere higher, 365 days | relevant 22,020 | 96(5) |
| C6 | elsewhere higher, 7 days | 22020*7/365 | |
| C7 | London higher, 30 days | 25323*30/365 | |
| C8 | elsewhere lower, 28 days | 14753*28/365 | |
| C9 | London lower, 1 day | 16967/365 | |
| C10 | elsewhere higher 365 days, total 22,020 | reduction 0 | "exceeds" |
| C11 | same, total 23,000 | 980 | |
| C12 | same, total 20,000 | 0 | |
| C13 | London higher 7 days, total 600 | 600 - 25323*7/365 | |
| C14 | elsewhere lower 30 days, total = 14753*30/365 exactly | 0 | |
| C15 | London lower 365 days, total 17,000 | 33 | |
| C16 | elsewhere lower 365, total 15,000 | 247 | |
| C17 | London higher 365, total 25,324 | 1 | |
