# NOTES: the Social Security Act 2018 (New Zealand), main benefits, row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

Entitlement to, rates of, and commencement of the three main benefits for adults under the Social Security Act 2018 (version as at 26 September 2026, from the text converted from the PCO XML). They sit under one top-level goal, `the benefit position for` (`ss-goal.l4`). For a person applying for jobseeker support, sole parent support or the supported living payment, it answers whether they are entitled, the weekly rate after the income test, and the day the benefit commences. Three goals sit under it:

1. **General requirements** (`ss-general.l4`): ss 16, 18, 19.
2. **Entitlement** (`ss-entitlement.l4`): ss 20-24, 26, 29-30, 32-36, 40.
3. **Rate and commencement** (`ss-rates.l4`, `ss-commencement.l4`): s 17, Schedule 2 Income Tests 1-4, Schedule 4 Part 2, ss 313 and 316.

Modules: `ss-types.l4` (nouns only), `ss-general.l4`, `ss-rates.l4`, `ss-entitlement.l4`, `ss-commencement.l4`, `ss-goal.l4`; tests in `ss-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Youth and young parent payments, emergency benefits, orphan's and unsupported child's benefits, supplementary and hardship assistance, obligations and sanctions, debt, reviews and appeals, and the rest of the Act. MSD's judgements (availability for work, permanent and severe restriction, the need for full-time care, split care priority) are inputs.

**Lost in conversion.** Schedule 4 Parts 1 and 3: the jobseeker support and supported living payment rates and the income test each is subject to. Both are inputs. The sole parent support rate ($521.52, Income Test 1) and the Income Tests survive and are encoded.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 16 | residential requirement | encoded (residence periods are inputs in years); (4)-(5) and regulations not |
| s 17 | rates | encoded |
| s 18 | one main benefit | encoded |
| s 19 | unlawful presence, temporary visas | encoded (s 205 not) |
| ss 20-24 | jobseeker support | encoded (s 22 availability is an input) |
| s 25 | hardship grant | out of scope: discretion |
| s 26 | ineligibility | encoded |
| ss 27-28 | certificates, examinations | out of scope: procedure |
| ss 29-30 | sole parent support | encoded |
| s 31 | child regarded as applicant's | out of scope: discretion |
| s 32 | split care | encoded as an input (the (2) priority rules are not) |
| s 33 | expiry at 14 | encoded: the expiry; replacement by jobseeker support not |
| ss 34-36 | supported living payment: restricted capacity or blindness | encoded |
| ss 37-39 | examinations, apportionment, open employment | out of scope |
| s 40 | supported living payment: carers | encoded: (1); the (2) 28-day continuation not |
| ss 313-315 | which benefits stand down | out of scope: the stand-down length and exemptions come from regulations |
| s 316 | stand-down and commencement | encoded: (1)-(3); (4) regulations not |
| Schedule 2 | Income Tests 1-4 | encoded |
| Schedule 4 Part 2 | sole parent support rate | encoded |
| Schedule 4 Parts 1, 3 | jobseeker and supported living rates | inputs (lost in conversion) |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 316(2)-(3) | When does a listed benefit applied for more than 28 days after entitlement commence? | Refused | (2) needs an application within 28 days; (3) covers only benefits not listed in (2). Changed after the independent pass from applying (3)'s rule |
| F2 | s 316(1) | When does a stand-down of n days starting on day S end? | Day S + n − 1 | n days counted inclusively of S |
| F3 | s 24 | Whose income decides "no or minimum income"? | The person's and partner's, as the income test uses | The test is whether income "would reduce the applicable rate ... to zero" |
| F4 | ss 29-30 | Is a sole parent with a supporting partner excluded? | Yes | s 30's limbs all describe a parent without a partner's support |
| F5 | s 33 | On the youngest child's 14th birthday | No longer entitled from that day | "On the date that the youngest dependent child ... turns 14, P's sole parent support expires" |
| F6 | Schedule 4 Part 2 cl 2 | The $20 childcare disregard | Up to $20 of the earnings used for childcare, taken off the total income | Those earnings are part of the total income |
| F7 | s 16 | "At least 2 years" | Residence periods as a number of years | The caller converts days |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `ss-tests.l4` (encoder) | 0 | 66 | 0 |
| `tests-independent.l4` | 0 | 126 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 192 | 0 |

`tests-independent.l4` has 128 assertions: the other **2 are refused, as their author expected** (fork F1). `check.sh` counts a refused assertion as neither satisfied nor failed.

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found the s 316 gap (F1), now refused, and two inputs that were missing: whether employment ended before the person applied (s 316(1)(a)(ii)), and whether the carer is caring for their own spouse or partner (s 40(1)(a)). **The encoder's test that encoded the old F1 reading was removed** and marked.

**Known limits.** The base rates and income tests for jobseeker support and the supported living payment are inputs. So are MSD's judgements. Residence periods are numbers of years. Split care is one input.

## Open questions for a New Zealand lawyer

1. F1: when does sole parent support, the supported living payment, or a listed kind of jobseeker support commence if the application comes more than 28 days after entitlement?
2. The Schedule 4 Part 1 and Part 3 rates, and their income tests, are lost in the converted text.

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the 28 days within which an application must be received for a listed benefit to start after the stand-down (s 316(2)). The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `ss-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 194 satisfied (67 encoder, 127 independent), 0 failed; 1 independent assertion (CM-20) is still refused as its author expected, and CM-21 now passes because s 55 brings its application within the 28 days. The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
