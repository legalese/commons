# Social Security Contributions and Benefits Act 1992 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the employee position for` (`sscba-goal.l4`). It answers:

- **Class 1 contributions:** primary and secondary, on a week's earnings.
- **Statutory sick pay:** the weekly rate, the daily amount, the entitlement limit, and whether two periods of incapacity link.
- **Statutory maternity pay:** entitlement, the earliest start of the maternity pay period, and the two weekly rates.

The rules are in `sscba-rules.l4`:

1. **Class 1 contributions:** ss 8(1)-(2) and 9(1)-(2).
2. **Statutory sick pay:** ss 152(2)-(3), 155(2)-(4) and 157(1), (3).
3. **Statutory maternity pay:** ss 164(2), 165(2), 166(1)-(2) and 171(1A).

The thresholds, the lower earnings limit and the prescribed SMP rate are set by regulations, so they are inputs. The percentages and the SSP cap are printed in this version and are used as written: 8%, 2%, 15% and £123.25.

## Seat

The encoding is written from the seat of **the employee**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "What National Insurance is due on my pay; what statutory sick pay do I get; and am I entitled to statutory maternity pay, from when and how much?"

The facts it asks for are ones that person can state, or findings made about them.

The secondary Class 1 contribution is the employer's. It is shown because it is charged on the employee's earnings.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope |
| s 5 | input: limits and thresholds |
| ss 6-7 | out of scope: liability and earnings |
| ss 8-9 | encoded (goal 1); the s 9A table is lost, so the secondary percentage is an input |
| ss 9B-150 | out of scope: Classes 2-4, benefits, industrial injuries, income-related benefits |
| s 151 | the liability, applied |
| s 152(2)-(3) | encoded (goal 2) |
| s 153 | out of scope: the end of the period of entitlement |
| s 154 | input: qualifying days |
| s 155(2)-(4) | encoded (goal 2) |
| ss 156, 158-163 | out of scope |
| s 157(1), (3) | encoded (goal 2) |
| s 164(2) | encoded (goal 3); the (4)-(9) notice and other conditions are out of scope |
| s 165(1)-(2) | encoded (goal 3); the duration (39 weeks) is set by regulations |
| s 166(1)-(2) | encoded (goal 3) |
| ss 167-171 | s 171(1A) is used; the rest is out of scope |
| Parts XIIZA onwards | out of scope: paternity, adoption, shared parental, bereavement and neonatal pay |

## Forks (readings taken)

- **F1, s 171(1A): "week".** Seven days beginning with Sunday. The expected week of confinement starts on the Sunday on or before the expected date.
- **F2, s 164(2)(a): "26 weeks ending with the week immediately preceding the 14th week before".** That week is the 15th week before. Employment must have begun on or before the Sunday that starts the first of the 26 weeks, which is the 15th week's Sunday − 175 days. Still being employed in the 15th week is an input. The regulations' treatment of part weeks is not applied.
- **F3, s 164(2)(c).** The woman has reached the 11th week before on the date in question, or has been confined before it.
- **F4, s 152(3): "separated by a period of not more than 8 weeks".** The days strictly between the two periods number 56 or fewer.
- **F5, s 157(3).** The daily amount is the weekly rate divided by the qualifying days in that week, with no rounding.
- **Known limits (from the independent pass).**
  - "But has ceased to work for him" (s 164(2)(a)) is not modelled.
  - Confinement before the 11th week is a flag, not a date.
  - A week with 0 qualifying days gives an evaluation error.
  - Overlapping periods of incapacity count as linked.
  - Only the entitlement limit is given; whether it has been reached is not tracked.
  - The secondary percentage is entered as a whole number (15, not 0.15).
  - The s 6 age conditions are not inputs.
  - The goal gives £0 SMP rates where there is no entitlement.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 5 modules: 125 assertions satisfied, 0 failed, 0 other errors — 28 the encoder's (`sscba-tests.l4`), 97 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** confirm the 26-week employment test, including partial first weeks under the regulations.
