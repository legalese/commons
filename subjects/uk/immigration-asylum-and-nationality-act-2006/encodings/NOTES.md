# Immigration, Asylum and Nationality Act 2006 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

Most of this Act amends other Acts. The part that works by itself for a person is the employment of illegal workers (ss 15-25), and that is what is encoded. There is one top-level goal, `the illegal working position for` (`iana-goal.l4`). For an employer who employed a person, it answers:

- whether the employment was contrary to s 15;
- if a penalty notice was given: the penalty payable, the earliest pay-by date the notice may specify, and the last day to appeal;
- if the offence is in question: whether it is committed, and the maximum imprisonment on indictment and on summary conviction.

Three goals sit under it:

1. **Employment contrary to s 15** (`iana-employment.l4`): ss 15(1), 21(1B), 24 and 25.
2. **The civil penalty** (`iana-penalty.l4`): ss 15(2)-(6), 16(4)(a) and 17(4A)-(4E).
3. **The offence** (`iana-offence.l4`): ss 21(1)-(2), (4) and 22(1)-(1A).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-14 | out of scope: they amend the law of appeals and leave in other Acts |
| s 15(1)-(6) | encoded (goals 1-2); (7)-(10) govern the content of orders and are out of scope |
| s 16 | encoded in part: the objection's outcome is an input; the "prescribed period" is an input date |
| s 17(1)-(3), (6) | out of scope: the court's decision |
| s 17(4A)-(4E) | encoded (goal 2) |
| ss 18-20 | out of scope: enforcement, code of practice, orders |
| s 21(1)-(2), (4) | encoded (goal 3); (3)-(3B) are out of scope |
| s 22(1)-(1A) | encoded as inputs (the body's knowledge); (2)-(4) officers' liability are out of scope |
| s 23 | out of scope: discrimination code |
| s 24 | encoded (goal 1) |
| s 25 | encoded (goal 1) |
| ss 26-64 | out of scope: documents, fingerprinting, information, accommodation, nationality, refugees, deprivation |

## Forks (readings taken)

- **F1, s 25(a): "adult" means "attained the age of 16".** The employee is an adult during the employment if their 16th birthday falls on or before its last day. The employer acts contrary to s 15 by employing them from that day. A 29 February birthday falls on 28 February in a non-leap year (daydate's `add years` clamps).
- **F2, s 15(6)(c): "a date, at least 28 days after the date specified ... as the date on which it is given".** The earliest pay-by date is the given date + 28.
- **F3, s 17(4B): "the period of 28 days beginning with the relevant date".** It ends on the relevant date + 27.
- **F4, s 15(3)-(4).** The excuse needs compliance with the prescribed requirements (an input). It is lost if the employer knew, at any time during the employment, that the employment was contrary to s 15.
- **F5, the penalty payable.** It is the amount specified, if a notice may be given, the employer is not excused, and the penalty was not cancelled on objection. A reduced or increased amount is entered as the amount specified.
- **F6, s 21(2)(b)(i), (4).** In England and Wales the summary maximum is the general limit in a magistrates' court (an input). It is 6 months for a conviction before 2 May 2022, and 6 months in Scotland and Northern Ireland.
- **Known limits (from the independent pass).**
  - Adulthood is tested against the last day of the employment, so the period before the 16th birthday is not separated out.
  - s 22 is folded into the knowledge inputs.
  - The goal does not say whether s 21(1) or (1A) is met.
  - After an objection, the caller enters the reduced or increased amount and the new notice date.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 120 assertions satisfied, 0 failed, 0 other errors — 45 the encoder's (`iana-tests.l4`), 75 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** confirm the 29 February birthday reading for "attained the age of 16".
