# Employment Rights Act 2025 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

Most of this Act amends other Acts. The encoding applies the amended rules as the Act states them. There is one top-level goal, `the worker position for` (`era25-goal.l4`). It answers:

- the weekly statutory sick pay, and the first day it is payable;
- whether the six-month unfair dismissal qualifying period is met;
- the last day to present a guaranteed-hours complaint.

Three goals sit in `era25-rules.l4`:

1. **Statutory sick pay**: ss 10-11, amending SSCBA ss 152, 153, 155 and 157, and Sch 11.
2. **The unfair dismissal qualifying period**: s 25, amending ERA 1996 s 108; s 124 is omitted.
3. **Guaranteed-hours complaint time limits**: ERA 1996 s 27BH, inserted by s 1, with ERA 1996 s 207B.

## Seat

The encoding is written from the seat of **the worker**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "What sick pay do I get and from which day; do I have enough service to claim unfair dismissal; and by when must I bring a guaranteed-hours complaint?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-7 (ERA 1996 ss 27BA-27BZ) | s 27BH encoded (goal 3); the guaranteed-hours duty, shifts and payments depend on regulations and are out of scope |
| ss 8-9 | out of scope |
| ss 10-11 | encoded (goal 1) for Great Britain |
| ss 12-13 | out of scope: Northern Ireland |
| ss 14-24 | out of scope: tips, leave, harassment, confidentiality |
| s 25 | encoded (goal 2) |
| ss 26 onwards | out of scope: dismissal protections, collective redundancy, outsourcing, equality plans, the Social Care Negotiating Body, trade unions, enforcement |

## Forks (readings taken)

- **F1, SSCBA s 157(1) as substituted.** The rate is the lower of £118.75 and 80% of normal weekly earnings, with no lower earnings limit. Daily SSP (the weekly rate ÷ qualifying days) is not computed.
- **F2, SSCBA ss 152-155 as amended.** SSP is payable from the first day of incapacity, because a single day is a period of incapacity and the waiting days are gone. Qualifying days, which come from regulations, are not checked.
- **F3, ERA 1996 s 108(1).** Six months ending with the effective date of termination: the EDT is on or after the last day of the six months beginning with the start of continuous employment.
- **F4, s 27BH.** Each period begins with the day after its trigger day, except (8), which begins with the day of awareness. It ends on the day before the corresponding date six months later, or on the last day of that month if it has none.
- **F5, s 207B(3).** Only conciliation days within the period are stopped, as in the Employment Rights Act 1996 encoding (F14 there).
- **F5 and the independent pass.** For conciliation that begins within the period and ends after the original limit, the encoding adds every day from Day A + 1 to Day B. The independent tester would add only the days up to the original limit. Its assertion (line 113) is left failing and the question is put to a lawyer.
- **Known limits.** The first day SSP is payable ignores qualifying days, and s 108(3)-(5) is one input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 5 modules: 84 assertions satisfied, 1 failed — 22 the encoder's (`era25-tests.l4`), 63 independent (`tests-independent.l4`). One assertion is expected to fail: tests-independent.l4 line 113 (scenario 59), the s 207B(3) reading in F5.

## Open questions for a UK lawyer

- **F2:** confirm the effect of the amendments on the first day of payment where qualifying days are set by agreement.
- **F5:** under s 207B(3), are the conciliation days after the original limit also not counted?
