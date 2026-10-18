# Customs and Excise Management Act 1979 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the customs position for` (`cema-goal.l4`). It answers:

- for seized goods: whether notice of seizure must be given, the last day for a notice of claim, and whether the thing is deemed condemned or must go to court;
- for fraudulent evasion: whether an offence under s 170 is made out, and the maximum penalties;
- the last day to commence proceedings.

Three goals sit under it:

1. **Seizure and condemnation** (`cema-forfeiture.l4`): s 139(6), and Sch 3 paras 1, 3, 4 (as an input), 5 and 6.
2. **Penalties** (`cema-penalties.l4`): ss 149(1), 170(1)-(5), and Schedule 1.
3. **Time limits** (`cema-time-limits.l4`): s 146A(2)-(3).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Coverage

| Provision | Disposition |
|---|---|
| Parts I-XI except as below | out of scope: administration, ports, import and export procedure, warehouses, excise licences, powers, other offences |
| s 139(6), Sch 3 paras 1-6 | encoded (goal 1); paras 7-17 (proceedings, proof, disposal) are out of scope |
| s 146A(2)-(3) | encoded (goal 3); (4)-(7) are out of scope |
| s 149(1), (3) | encoded (goal 2): 15 months |
| s 170(1)-(5) | encoded (goal 2); (6) forfeiture follows from the offence |
| Schedule 1 | encoded (goal 2) |
| ss 50, 68 | out of scope: they share Schedule 1 but are not encoded |
| Schedules 2, 2A, 4-7 | out of scope |

## Forks (readings taken)

- **F1, lost paragraph numbers.** The conversion drops the Schedule paragraph numbers. Schedule 3 is numbered in its printed order.
- **F2, "the prescribed sum £20,000".** The text runs two versions together. The fixed sum is an input, and the seal-skins "statutory maximum £20,000" is taken as the same input.
- **F3, Sch 3 para 3: "within one month of the date".** A claim is in time if made on or before the corresponding date one month later, or the last day of that month if it has none.
- **F4, Sch 3 para 1(2).** The presence exceptions are one input. Its qualifications are the caller's to apply: a master counts only for things seized on or from a ship or aircraft, and a driver only for things seized on or from a vehicle.
- **F5, Schedule 1.** For Class C drugs, the summary maximum is the greater of three times the value and £500, and the fixed sum is not used. For Class A, B and temporary class drugs it is as in s 170(3)(a).
- **F6, s 146A(3).** The last day for a summary offence is the earlier of the end of the 3 years beginning with the day of the offence and the corresponding date 6 months after the evidence date. Where that date is already past when evidence arrives, the proceedings are barred.
- **F7, s 170(5).** The corresponding-offence input is applied as given. The Act limits it to offences in connection with a prohibition or restriction.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 126 assertions satisfied, 0 failed, 0 other errors — 36 the encoder's (`cema-tests.l4`), 90 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** which value of "the prescribed sum" applies, by jurisdiction and date?
