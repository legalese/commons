# NOTES: the Civil Aviation Act 2023 (New Zealand), domestic carriage and passenger delay, row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The rules on passenger compensation for delay in domestic air carriage, in the domestic carriage subpart of Part 5 of the Civil Aviation Act 2023 (version as at 23 September 2026, from the text converted from the PCO XML). They sit under one top-level goal, `the delay position for` (`caa-goal.l4`). For a passenger's claim it answers whether the subpart applies, whether this carrier answers for the delay, the most it must pay, the last day to bring the action, and whether the action is in time. Three goals sit under it (all in `caa-liability.l4`):

1. **Application and carriers**: ss 270-273, 275.
2. **Liability and its limit**: ss 274, 276-279.
3. **Time limits**: ss 281(2), 283.

Modules: `caa-types.l4` (nouns only), `caa-liability.l4`, `caa-goal.l4`; tests in `caa-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** International carriage under the Montreal and Warsaw Conventions (ss 257-268), which carry their own limits in special drawing rights, and the rest of the Act (safety, security, airports, offences).

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 269 | interpretation | inert |
| s 270 | application | encoded |
| s 271 | combined carriage | encoded (an input) |
| s 272 | exclusions | encoded |
| s 273 | contracting and actual carriers | encoded: (a); (b) not |
| s 274 | liability for delay | encoded: (1)-(2) |
| s 275 | successive carriers | encoded (successive carriage added after the independent pass) |
| s 276 | avoidance of liability | encoded |
| s 277 | limitation of liability | encoded: (1)-(2) |
| s 278 | contracting out | encoded: (1)-(2); (4) not |
| s 279 | wilful or reckless misconduct | encoded |
| s 280 | just and equitable orders | out of scope: the court's discretion |
| s 281 | contribution proceedings | encoded: (2) |
| s 282 | relationship between carriers | inert |
| s 283 | limitation of actions | encoded: (1) |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 277(2) | A special contract with a limit below 10 times the fare | The 10 times limit still applies | s 278 makes terms limiting liability unenforceable; the independent author agreed |
| F2 | s 283(1)(b) | Without arrival, which date starts the 2 years? | The later of the expected arrival and the day carriage stopped | "the later of the following dates"; the independent author agreed |
| F3 | ss 281(2), 283 | 2 years after 29 February | 28 February two years on | The date library clamps; the independent author agreed |
| F4 | s 277(1)(b) | Free carriage | A cap of 0 | 10 times nothing; the author flagged it as ambiguous |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `caa-tests.l4` (encoder) | 0 | 30 | 0 |
| `tests-independent.l4` | 0 | 76 | 0 |
| the 3 rule modules | 0 | 0 | 0 |
| **total** | 0 | 106 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) failed no assertion. It found that a contracting carrier in successive carriage was always answerable, contrary to s 275. That is now fixed and tested; no encoder test had encoded the old reading.

**Known limits.** s 273(b) (a special contract binding the actual carrier only if it agreed) and s 278(4) (more favourable terms) have no inputs. Negative amounts are computed rather than refused.

## Open questions for a New Zealand lawyer

1. F4: does the 10 times limit in s 277 leave a passenger on a free ticket with no compensation for delay?

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the 2-year limits for actions against carriers (s 283) and for contribution proceedings (s 281(2)). The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `caa-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 99 satisfied (32 encoder, 67 independent), 9 failed (9 independent assertions written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
