# Pensions Act 2008 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the workplace pension position for` (`pa08-goal.l4`). For one worker and one pay reference period it answers:

- the worker's status;
- their qualifying earnings and the minimum contributions;
- whether given contributions meet s 20;
- the fixed and escalating penalty answers.

Three goals sit under it:

1. **Status** (`pa08-status.l4`): ss 1(1), 3(1)-(4), (6B), 7(1)-(2) and 9(1).
2. **Qualifying earnings and contributions** (`pa08-status.l4`): ss 13(1)-(2) and 20(1)-(1A).
3. **Penalty notices** (`pa08-penalties.l4`): ss 40(4)-(5) and 41(2), (4)-(6).

The amounts are those printed in this version: £10,000 (s 3), £6,240 and £50,270 (s 13), £50,000 (s 40) and £10,000 a day (s 41).

## Seat

The encoding is written from the seat of **the worker (and, for penalties, the employer)**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Must my employer enrol me in a workplace pension, or can I opt in or ask to join; what are my qualifying earnings and the least that must be paid in; and (for an employer) what penalty can the Regulator impose?"

The facts it asks for are ones that person can state, or findings made about them.

The worker's seat governs the status and contribution goals. The penalty goal is written from the seat of the employer, the person penalised.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1, 3, 7, 9 | encoded (goal 1); s 3(5)-(8) and the regulation powers in ss 7 and 9 are out of scope |
| s 2, ss 4-6, 8, 10-12 | out of scope |
| s 13 | encoded (goal 2) |
| ss 14-15A | out of scope: review powers, the pay reference period (an input), rounding orders |
| ss 16-19 | input: a qualifying or automatic enrolment scheme |
| s 20(1)-(1A) | encoded (goal 2); Conditions 1 and 2 are an input |
| ss 21-34 | out of scope |
| ss 35-39 | out of scope: compliance and unpaid contributions notices (the underlying notice is assumed) |
| ss 40-41 | encoded (goal 3) |
| ss 42-44 | out of scope, apart from the s 41(2) bars |
| the rest of the Act | out of scope |

## Forks (readings taken)

- **F1, the day of assessment.** Ages and pensionable age are judged on the first day of the pay reference period.
- **F2, ages.** A person is aged at least 16 or 22 from that birthday, and under 75 before the 75th birthday. A 29 February birthday falls on 28 February in a non-leap year.
- **F3, s 3(1)(c): "more than £10,000".** Earnings must be strictly more, scaled to the period by months ÷ 12. No rounding order is applied.
- **F4, s 13.** Qualifying earnings are the part of gross earnings above the scaled lower limit and not above the scaled upper limit.
- **F5, s 1(1)(c) and s 9.** Qualifying earnings are payable only where earnings exceed the scaled lower limit. Otherwise the worker falls under s 9, unless already in a s 9 scheme.
- **F6, s 20(1)(a).** The employer must pay something: an employer contribution of 0 fails.
- **F7, s 40(5)(b): "at least 4 weeks after the date on which the notice is issued".** The earliest payment date is the issue date + 28.
- **F8, s 41(6)(e).** The escalating penalty runs from its start date until the compliance date, not counting that date. A start date before the fixed penalty's earliest payment date, a daily rate over £10,000, or a s 41(2) bar gives 0.
- **F9, s 3(3)-(4).** These disapply only s 3(2). The jobholder then falls to s 7: outside the duties if already an active member of a qualifying scheme, otherwise able to opt in. This was changed after the independent pass.
- **Known limits (from the independent pass).**
  - s 41(2)(a) bars an escalating notice for a pending review only where the underlying notice is under s 35, 36 or 37. There is no input for the kind of notice, so any pending review bars it.
  - An escalating penalty that may not be imposed is given as 0.
  - With nil qualifying earnings, the employer must still pay something (F6).

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 131 assertions satisfied, 0 failed, 0 other errors — 41 the encoder's (`pa08-tests.l4`), 90 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F8:** is the day of compliance itself a day on which the escalating penalty is payable?
