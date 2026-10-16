# NOTES: the Customs and Excise Act 2018 (New Zealand), Customs value, duty and refunds, row `legalese-aswathy`

**Draft. No New Zealand lawyer or customs broker has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Customs and Excise Act 2018 (version as at 4 September 2026, from the text converted from the PCO XML) on the Customs value of imported goods, the duty and its payment, late payment penalties, and refunds. They sit under one top-level goal, `the import position for` (`cea-goal.l4`), which gives the Customs value, the duty at the Tariff rates, the last day for payment and the late payment penalties accrued. Four goals sit under it:

1. **Customs value** (`cea-value.l4`): s 101, Schedule 4 cls 2(2), 3-5, 7, 9-12.
2. **Duty and its payment** (`cea-duty.l4`, `cea-dates.l4`): ss 120, 122-124, with the Legislation Act 2019 working day.
3. **Late payment penalties** (`cea-duty.l4`): ss 159-160.
4. **Refunds and appeals** (`cea-refunds.l4`): ss 142-143 and the 20-working-day appeal periods.

Modules: `cea-types.l4` (nouns only), `cea-dates.l4`, `cea-value.l4`, `cea-duty.l4`, `cea-refunds.l4`, `cea-goal.l4`; tests in `cea-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Arrival, departure, entry and examination procedure (Parts 2-3), the Tariff rates themselves (Tariff Act 1988: inputs), Schedule 4 cl 6 evidence and methods 4-6 (refused), excise duty under Schedule 3, interest under ss 154-158 and 161-165 (rates by regulation), drawback (s 147: prescribed amounts), offences and penalties under Part 6, and the rest of the Act.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 101 | Customs value on entry | encoded |
| s 102 | provisional Customs value | inert (its refund, s 143, is encoded) |
| s 120 | proportionate duty | encoded |
| s 122 | time for payment: general | encoded |
| s 123 | deferred payment | encoded (the deferred date is an input) |
| s 124 | other times for payment | encoded: (2)-(7) ((7) added after the independent pass) |
| s 142 | refunds of duty paid in error | encoded |
| s 143 | refunds on a provisional value | encoded |
| ss 144-149 | other refunds, drawback | out of scope: discretion or prescribed amounts |
| ss 159-160 | late payment penalties | encoded: (3)-(6) of s 160; Schedule 3 excise not |
| Schedule 4 cl 2(2) | related persons | encoded |
| Schedule 4 cl 3 | financing interest | encoded |
| Schedule 4 cls 4-5 | primary basis, transaction value usable | encoded |
| Schedule 4 cl 6 | related-party evidence | an input |
| Schedule 4 cl 7 | transaction value | encoded (each amount an input) |
| Schedule 4 cl 8 | buyer's assists | inputs |
| Schedule 4 cls 9-12 | identical and similar goods | encoded: the lowest qualifying value |
| Schedule 4 Parts 4-6 | deductive, computed, fallback | refused |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 113, 123-124, 142 | "Working day" | The Legislation Act 2019, s 13 definition | The Act does not define it |
| F2 | s 159 | When is each penalty counted at a given day? | Once the close of its day (the payment date, the 7th day after) falls on or before that day | Penalties arise "as at the close of" those days |
| F3 | s 142(1) | "Within 4 years after the duty has been paid" | Up to and including the 4th anniversary, or the next working day if that is not one | Legislation Act 2019 s 55 (added after the independent pass) |
| F4 | Schedule 4 cls 9-12 | Which comparable values qualify? | The caller supplies the qualifying, adjusted values; the lowest is taken | cls 9(2), 11(2) |
| F5 | s 122 | When must duty on entry be paid? | On the day of the s 122 event | "must be paid ... when" the event occurs |
| F6 | s 159(4) | The base of the 4% | The duty still unpaid, not the 1% penalty | "4% of the amount of the duty still to be paid" |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `cea-tests.l4` (encoder) | 0 | 52 | 0 |
| `tests-independent.l4` | 0 | 100 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 152 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found that the Legislation Act 2019 s 55 extension was missing from s 142 (F3) and that s 124(7) had no payment occasion. Both are fixed; no encoder test had encoded the old reading.

**Known limits.** The cl 6 evidence, the cl 4(4) duty to seek an explanation, and the qualification of comparable values are inputs. The Tariff rates are inputs. Methods 4-6 are refused. Excise under Schedule 3 is not encoded.

**Note for the other New Zealand encodings.** Legislation Act 2019 s 55 (a thing to be done within a period may be done on the next working day when the last day is not one) applies to time limits across New Zealand legislation. This encoding applies it to s 142; the s 124 periods already end on working days.

## Open questions for a New Zealand customs specialist

1. F2: is a penalty under s 159 "payable" from the close of its day, or from the next day?
2. Should s 55 extend the s 123 deferred payment date when it falls on a non-working day?
