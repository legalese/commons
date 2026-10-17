# NOTES: the Residential Tenancies Act 1986 (New Zealand), row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Residential Tenancies Act 1986 (version as at 1 December 2025, from the text converted from the PCO XML) for the steps a landlord or tenant takes in a tenancy. They sit under one top-level goal, `the tenancy step answer for` (`rta-goal.l4`). For one step (a notice to terminate, a rent increase, a bond demand, a demand for rent in advance, an entry on notice, a boarding house termination, or an application about an unlawful act), it answers whether the Act applies, whether the step is lawful, and the key date: the earliest date to vacate, the earliest date a rent increase may take effect, or the last day to apply. Five goals sit under it:

1. **Application of the Act and working days** (`rta-application.l4`, `rta-dates.l4`): s 5 exclusions, s 7 short fixed terms, s 8 agreement, the s 2 working day, s 136 deemed service, s 136A periods.
2. **Bonds and rent** (`rta-money.l4`): ss 18-18A, 19, 22A(3), 23, 24, 25(2)-(5), 29, 30, 49A-49B, 56B(5)-(6).
3. **Termination** (`rta-termination.l4`): notice periods and who may use each ground on which kind of tenancy (ss 50-59B), the Tribunal's duty under ss 55 and 55A, s 56's remedy period, and the periods in ss 50A, 56D, 60, 60A, 60B, 61, 62A, 62D, 64.
4. **Entry and boarding houses** (`rta-entry.l4`): s 48, ss 66D, 66R-66S, 66U-66X.
5. **The Tribunal** (`rta-tribunal.l4`): ss 54(3), 77(5), 108(7), 109, 109B-109C.

Modules: `rta-types.l4` (nouns only), `rta-dates.l4`, `rta-application.l4`, `rta-money.l4`, `rta-termination.l4`, `rta-entry.l4`, `rta-tribunal.l4`, `rta-goal.l4`; tests in `rta-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Parts 3 (other than the sections above), 4 and 5: the Tribunal's procedure, mediation, enforcement, administration, the Residential Tenancies Fund, regulations and infringement offences; the landlord's and tenant's duties under ss 36-47 (repairs, quiet enjoyment, healthy homes, smoke alarms, assignment, pets and minor changes), which are standards and discretion rather than computation; the Tribunal's discretions (ss 55B, 56, 56A(2), 59(4), 66, 78, 78A) beyond the time limits listed; Schedule 1AA (social housing transitions); the transitional schedules.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 2 | working day | encoded (`is a working day under s 2`); Matariki and anniversary days are inputs |
| s 5 | exclusions | encoded as an input (one constructor per paragraph) |
| s 7 | short fixed terms | encoded (`sections 25 to 28 and 51 apply to`) |
| s 8 | agreement that the Act applies | encoded |
| ss 18, 18AA, 18A | bonds, other security | encoded |
| s 19 | lodging the bond | encoded (23 working days; s 19(1A) boarding house exception) |
| ss 20-22 | chief executive's duties | out of scope: administrative |
| s 22A(3) | landlord's bond application within 2 months | encoded |
| ss 22B-22G | Tribunal bond orders, advertising | out of scope: discretion or no computation |
| s 23 | rent in advance | encoded |
| s 24 | rent increases | encoded (s 24(4)-(6) corrections not encoded: Tribunal consent) |
| s 24A | temporary rent reduction | inert: no computation |
| s 25 | market rent | encoded: time limits (2), (2A) and effective date (5); the market rent itself is the Tribunal's |
| ss 26-28B | duration of orders, improvements | out of scope: Tribunal discretion |
| s 29 | receipts | encoded |
| s 30 | records | encoded (7 tax years) |
| ss 31-47 | rights and obligations | out of scope: standards, not computation |
| s 48 | entry | encoded (subsections (2)(a)-(d), (2A)-(2B)); (2)(e)-(f) and (3) consent are not notice questions |
| ss 49A-49B | damage liability | encoded |
| s 50 | ways a tenancy ends | encoded as which notice grounds suit which tenancy |
| s 50A | death of a sole tenant | encoded |
| s 51 | termination by notice | encoded |
| s 52 | shorter notice with Tribunal consent | out of scope: Tribunal consent |
| s 53 | service tenancies | encoded: (1), (3), (4), (5); (2) and (7) shorter notices are Tribunal questions |
| s 53A | student tenancies | encoded |
| s 54 | retaliatory notices | encoded: the 28 working days in (3) |
| s 55 | termination for arrears, damage, assault | encoded |
| s 55AA | assault with a charge filed | encoded (14 days) |
| s 55A | anti-social behaviour | encoded |
| s 55B | landlord's hardship | out of scope: discretion |
| s 56 | breach with a remedy notice | encoded: the remedy period |
| s 56A | unlawful premises | encoded: (1) 2 days |
| s 56B | family violence withdrawal | encoded: 2 days and the (5)-(6) rent |
| ss 56C, 56E | service and disclosure | out of scope |
| s 56D | remaining tenant's hardship | encoded: the 60-day time limit |
| ss 57, 58 | subtenancies, mortgagees | out of scope |
| s 58A | build-to-rent | encoded (56 days) |
| ss 59-59B | destruction, uninhabitable, contamination | encoded (7 and 2 days) |
| s 60 | remaining in possession | encoded: (2) deemed periodic tenancy |
| s 60AA | terminating without grounds | inert: an unlawful act |
| s 60A | fixed term becomes periodic | encoded |
| s 60B | notice to renew | encoded |
| s 60C | renewed tenancies | inert |
| s 61 | abandonment | encoded: (3) rent liability |
| ss 62, 62A | goods left behind | encoded: the 35-day storage |
| ss 62B, 62C, 62E, 62F | Tribunal disposal, proceeds | out of scope |
| s 62D | claiming proceeds | encoded (1 year) |
| ss 63, 65, 66 | entry without order, squatters, reducing a term | out of scope |
| s 64 | possession orders | encoded: (2) and (4) 90 days |
| s 66D | boarding house bond | encoded |
| ss 66R-66S | entering a boarding room | encoded: (2) 24 hours, 8 am to 6 pm |
| s 66U | boarding house termination by landlord | encoded |
| s 66V | by tenant | encoded (48 hours) |
| s 66W | death of a sole boarder | encoded (48 hours) |
| s 66X | abandonment | encoded: the 24- and 48-hour times |
| s 77(5) | $100,000 limit | encoded |
| s 108(7) | enforcing a work order | encoded (12 months) |
| s 109 | unlawful acts | encoded: time limits and the Schedule 1A cap (an input) |
| ss 109B-109C | pecuniary penalties | encoded: eligibility and the $50,000 cap |
| s 136 | service | encoded: (6), (7), (9) |
| s 136A | periods of notice | encoded |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 51, 136A | When may a tenant be required to vacate under n days' notice given (or deemed given) on day G? | On day G + n or later | s 136A: the period "commences on the first day after the notice is given ... and ... ends with the close of the last day of the period" |
| F2 | s 24(1)(d)-(e) | Is a rent increase on the anniversary "within 12 months after" the start or the last increase? | Yes: the first lawful day is the day after the anniversary | A period "after" a day excludes that day (Legislation Act 2019), so the 12 months end on the anniversary; changed after the independent pass |
| F3 | s 56B(5) | The formula lost in conversion | Rent × remaining tenants ÷ tenants before the withdrawal | Its listed symbols; the obvious proportional reduction |
| F4 | ss 55(1)(aa), 55A(2) | When are 3 occasions "within a 90-day period"? | The first and third are no more than 89 days apart | A 90-day period counted inclusively holds both |
| F5 | s 62A(3), (5) | First day goods stored "not less than 35 days from" possession may be sold | The 36th day after possession | 35 whole days must pass |
| F6 | s 48(2)(b) | "Not more frequently than once in any period of 4 weeks" | At least 28 days after the last inspection entry | Any 4-week window then holds one entry |
| F7 | ss 48(2), 66R(2) | "Between 8 o'clock in the morning and 7 o'clock in the evening" | Inclusive: 8:00 to 19:00 (boarding rooms 8:00 to 18:00) | Ordinary reading |
| F8 | s 56(1)(b) | A remedy period "commencing with the day on which the notice was given" | Includes that day: 14 days end on the 13th day after | The Act's own words override s 136A |
| F9 | s 55(1)(aa)(i) | When was rent "owing for at least 5 working days after the date on which it was due"? | Unpaid at the end of the 5th working day after the due date; the occasion is dated by the due date | Ordinary reading |
| F10 | ss 66U-66X | Do boarding house hour periods allow for s 136 deemed service? | No: counted from when the notice was given | Part 2A notices are mostly put on the door or given in person (s 66S(4)) |
| F11 | s 22A(3) | "Within 2 months of the termination" | The same day 2 months later, or the month's last day | Calendar months |
| F12 | s 30(1A)-(1B) | Tax year of a payment before 1 July 2016 | Refused | s 30(1B) defines no tax year before then |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `rta-tests.l4` (encoder) | 0 | 191 | 0 |
| `tests-independent.l4` | 0 | 246 | 0 |
| the 8 rule modules | 0 | 0 | 0 |
| **total** | 0 | 437 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 3 disagreements, all resolved in its favour: the anniversary is within the 12 months of s 24(1)(d)-(e) (F2), and s 56C makes a posted or delivered family violence withdrawal notice given that day. **The encoder's tests that encoded the rejected reading of s 24 were changed** and marked in `rta-tests.l4`.

**Known limits.** The grounds for each notice, the s 5 exclusions, the 4-week inspection history, the days present and the Schedule 1A amounts are inputs. Boarding house deaths and abandonment (ss 66W, 66X) are given to the calendar day only. The top-level goal tests the s 7 short fixed-term exclusion only for s 51 notices.

## Open questions for a New Zealand lawyer

1. F3: what is the s 56B(5) formula? The converted text lost it.
2. F4: does "3 separate occasions within a 90-day period" put the first and third no more than 89 days apart?
3. F2: is a rent increase on the anniversary of the start of the tenancy, or of the last increase, within the 12 months of s 24(1)(d)-(e)?
4. F1: does s 136A make n days' notice given on day G expire with the close of day G + n, so that the tenant may be required to vacate on that day?
5. The Schedule 1A and 1B amounts are lost in the conversion and are inputs here.

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the deadlines for a landlord's bond application (s 22A(3)), a market rent application (s 25(2)-(2A)), remedying a breach (s 56), a hardship application (s 56D), claiming proceeds of sale (s 62D), possession orders and their filing (s 64), enforcing a work order (s 108(7)) and unlawful act applications (s 109); not earliest dates, effects of termination, the s 60B notice counted back from expiry, or periods already counted in working days. The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `rta-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 438 satisfied (195 encoder, 243 independent), 3 failed (3 independent assertions written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
