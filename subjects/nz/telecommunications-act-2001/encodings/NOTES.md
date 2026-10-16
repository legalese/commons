# NOTES: the Telecommunications Act 2001 (New Zealand), consumer matters, row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The consumer-facing rules that the Telecommunications Act 2001 itself makes computable (version as at 4 September 2026, from the text converted from the PCO XML). They sit under one top-level goal, `the telecommunications position for` (`tel-goal.l4`), which gives: whether Chorus may stop supplying an end-user's copper service, whether a party may appeal a dispute determination, and the interest on late levy. Three goals sit under it:

1. **Copper withdrawal** (`tel-consumer.l4`): ss 69AC-69AE and Schedule 2A cl 1(3).
2. **Disputes and periods** (`tel-consumer.l4`, `tel-dates.l4`): ss 239(3), 242-244, 246(1), (6), Schedule 2A cl 2(2), with the s 5 working day.
3. **Levy** (`tel-levy.l4`): s 14.

Modules: `tel-types.l4` (nouns only), `tel-dates.l4`, `tel-consumer.l4`, `tel-levy.l4`, `tel-goal.l4`; tests in `tel-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Consumer terms are mostly in codes.** The retail service quality codes, the 111 contact code and the copper withdrawal code are secondary legislation or industry codes, not in the source. The programme asked for "consumer terms"; only what the Act states is encoded.

**Not encoded.** Access regulation (Parts 2-2AA), fibre regulation (Part 4AA), the TSO cost determinations, network operators' powers, the Telecommunications Forum, and the rest of the Act; ss 241-242 are carried as text.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 5 | working day | encoded (local anniversary days are an input) |
| s 14 | late payment of levy | encoded |
| ss 69AC, 69AD | copper withdrawal | encoded (refused where neither applies) |
| s 69AE | TSO instruments in fibre areas | encoded: (a) |
| Schedule 2A cl 1(3) | minimum protections | encoded: (a)-(d), (f)-(g); (e) and (h) not |
| s 239(3) | submissions on a Commission code | encoded |
| Schedule 2A cl 2(2) | submissions on the copper withdrawal code | encoded |
| ss 241-242 | referral and binding effect | inert |
| ss 243-244 | appeals | encoded |
| s 246 | review of schemes | encoded: (1), (6) |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 69AC(2)(a), 69AD(2)(a) | Does complying with the copper withdrawal code include the Schedule 2A protections? | Yes: both are required | The code must contain them (Schedule 2A cl 1(3)) |
| F2 | s 239(3); Schedule 2A cl 2(2) | "Not later than 30 working days after" and "before the date that is 30 working days after" | The 30th working day; the calendar day before it | The different words; the independent author agreed |
| F3 | s 14 | How are months "or part of each month" counted? | One month for each month, or part of a month, after the due date, by calendar months | Ordinary reading; simple interest on the unpaid amount |
| F4 | ss 69AC-69AD | A service neither section covers | Refused | The sections restrict only the services they describe (changed after the independent pass) |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `tel-tests.l4` (encoder) | 0 | 29 | 0 |
| `tests-independent.l4` | 0 | 107 | 0 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 0 | 136 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) failed no assertion. It led to refusing a service outside ss 69AC-69AD (F4) and correcting a comment. The working-day module was also corrected for a Sunday 1 January (found by the Electricity Industry Act pass). **The encoder's test that encoded the old F4 reading was removed** and marked. While writing its own tests, the encoder also corrected a hand count that had missed the Mondayised Waitangi Day in 2027.

**Known limits.** Several Schedule 2A protections are single inputs. Matariki and anniversary days are an input list.

## Open questions for a New Zealand lawyer

1. F3: for a levy due on the 31st, is a payment on the last day of the next month within the first month?
