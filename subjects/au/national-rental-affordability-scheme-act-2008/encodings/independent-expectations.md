# Independent expectations: National Rental Affordability Scheme Act 2008

Written from BRIEF.md and the source text only, before any L4 was read.

## Rental dwelling (s 4)

| # | Kind | Rent payable | Rental dwelling? | Section |
|---|---|---|---|---|
| R1 | dwelling / separately habitable part | yes | yes | s 4 "rental dwelling" (a) |
| R2 | strata unit | yes | yes | s 4 (b), "unit" |
| R3 | caravan, houseboat or mobile dwelling | yes | no | s 4 exclusion |
| R4 | dwelling the regulations exclude | yes | no | s 4 exclusion |
| R5 | dwelling | no | no | "a dwelling for which rent is payable" |

## Incentive period end (s 4 "incentive period": a 10 year period that starts on or after 1 July 2008)

A 10-year period starting on day D ends on the day before the 10th anniversary of D.

| # | First day | Valid incentive period? | Last day | Note |
|---|---|---|---|---|
| P1 | 1 July 2008 | yes | 30 June 2018 | boundary: "on or after 1 July 2008" |
| P2 | 30 June 2008 | no | n/a | one day before the earliest permitted start |
| P3 | 1 May 2010 | yes | 30 April 2020 | |
| P4 | 15 March 2012 | yes | 14 March 2022 | |
| P5 | 29 February 2012 | yes | 28 February 2022 (low confidence: the anniversary falls on 28 Feb or 1 Mar; I take the period to end 28 Feb 2022) | |

## NRAS year (s 4)

| # | Day | NRAS year starts | NRAS year ends |
|---|---|---|---|
| Y1 | 30 June 2008 | none (before the first NRAS year) | |
| Y2 | 1 July 2008 | 1 July 2008 | 30 April 2009 |
| Y3 | 30 April 2009 | 1 July 2008 | 30 April 2009 |
| Y4 | 1 May 2009 | 1 May 2009 | 30 April 2010 |
| Y5 | 30 April 2015 | 1 May 2014 | 30 April 2015 |
| Y6 | 1 May 2015 | 1 May 2015 | 30 April 2016 |
| Y7 | 1 January 2020 | 1 May 2019 | 30 April 2020 |

## Conditions for the year (s 7(2), (3), (5))

Base case: never lived in before the period; rented to prescribed tenants; market value rent 500; every charge 400; no disapplication; vacancy 0, allowed 30 days. Each row changes only what it names.

| # | Change | Meets the Act's conditions? | Section |
|---|---|---|---|
| C1 | base (rent exactly 20% below) | yes | s 7(2)(b)(ii) "at least 20% less" |
| C2 | one charge 401 (19.8% below) | no | s 7(2)(b)(ii) |
| C3 | charges 300 and 400 | yes | each charge |
| C4 | charges 300 and 450 | no | "each charge" |
| C5 | C2 but Secretary disapplied the rent condition | yes | s 7(5) |
| C6 | tenants not of the prescribed kind | no | s 7(2)(b)(i) |
| C7 | tenants not prescribed and rent condition disapplied | no | s 7(5) only disapplies (b)(ii) |
| C8 | lived in before the period, not the unfit route | no | s 7(2)(a)(i) |
| C9 | lived in before, but was unfit and not lived in since made fit until the period started | yes | s 7(2)(a)(ii) |
| C10 | not rented this year, vacancy 30 days, allowed 30 | yes (tenant and rent conditions do not bite: "to the extent that the rental dwelling is rented") | s 7(2)(c) "not vacant for longer than" |
| C11 | not rented, vacancy 31, allowed 30 | no | s 7(2)(c) |
| C12 | not rented, tenants not prescribed, vacancy 10, allowed 30 | yes | s 7(2)(b) applies only to the extent rented |
| C13 | rented (part of year), vacancy 31 > 30 allowed | no | s 7(2)(c) applies to the extent not rented |

Confidence: high, except P5 (low) and whether a year in which the dwelling is rented also tests vacancy (C13, medium: the "to the extent" wording means both (b) and (c) apply to a partly rented year).
