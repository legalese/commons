# NOTES: the Electricity Industry Act 2010 (New Zealand), row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The consumer-facing and enforcement rules that the Electricity Industry Act 2010 itself makes computable (version as at 30 March 2025, from the text converted from the PCO XML). They sit under one top-level goal, `the distributor position for` (`eia-goal.l4`), which gives, for a distributor, a place and a Code breach: whether the supply obligation continues or is suspended, whether the s 105(4) offence is committed, whether the distributor must be in the dispute resolution scheme, whether the Authority may still act on the breach, and the most pecuniary penalty. Three goals sit under it:

1. **Supply obligation** (`eia-supply.l4`): ss 105-107.
2. **Disputes** (`eia-disputes.l4`): ss 95-96.
3. **Enforcement** (`eia-enforcement.l4`, `eia-dates.l4`): ss 52, 54, 66, 80, with the Legislation Act 2019 working day and ss 54-56.

Modules: `eia-types.l4` (nouns only), `eia-dates.l4`, `eia-supply.l4`, `eia-disputes.l4`, `eia-enforcement.l4`, `eia-goal.l4`; tests in `eia-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Billing is not here.** Retail billing, disconnection and consumer care are in the Electricity Industry Participation Code 2010 and regulations under s 113, which are not in the source. The programme asked for "billing"; the Act gives no billing rule to encode.

**Not encoded.** The Authority's constitution and functions, Code-making, the register, ownership separation rules (other than the s 80 penalty caps), customer trusts' accounts, the State-owned enterprise and Waitaki provisions, and levies.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 52 | limitation for Code breaches | encoded |
| s 54(1)(d) | pecuniary penalty for a Code breach | encoded |
| s 54(3) | related breaches as one | not encoded (an input would be the count of breaches) |
| s 56 | pecuniary penalty considerations | out of scope: the Rulings Panel's judgement |
| s 66 | appeals: 20 working days | encoded |
| s 80(2)-(3) | Part 3 pecuniary penalties | encoded |
| s 95 | who may complain | encoded |
| s 96 | membership of the scheme | encoded |
| ss 97-98 | compliance with the scheme | inert |
| s 105 | continuing supply obligation | encoded |
| s 106 | ending and suspension | encoded |
| s 107 | notice of alternative supply | encoded: the 6 months |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 107(1) | When may alternative supply begin after "at least 6 months' notice"? | The day after 6 months that run from the day after the notice | Legislation Act ss 54, 56 (changed after the independent pass) |
| F2 | s 52(1) | "More than 3 years before" the exercise of the power | Before the day 3 years earlier; that day itself is in time | Ordinary reading |
| F3 | s 105(4) | The offence after a suspension's reason has passed | Knowingly not resuming once the s 106(2)(b)-(c) reason has passed is an offence | s 106(3): cessation may continue only as long as the reason |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `eia-tests.l4` (encoder) | 0 | 45 | 0 |
| `tests-independent.l4` | 0 | 82 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 127 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 2 disagreements on s 107 (F1) and two further faults: a working-day error for a Sunday 1 January, shared with four other encodings and fixed in all, and the missing court-satisfied condition in s 80(3)(b)(i). All are fixed. **The encoder's s 107 test that encoded the old reading was changed** and marked.

**Known limits.** The fines return a maximum (or 0) rather than refusing when there is no offence. s 54(3) is not modelled.

## Open questions for a New Zealand lawyer

1. F1: does "at least 6 months' notice" in s 107 count from the day of the notice or the day after?
