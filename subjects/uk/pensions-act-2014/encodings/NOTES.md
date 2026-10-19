# Pensions Act 2014 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the pension position for` (`pa14-goal.l4`). For one person it answers:

- which state pension under Part 1 they are entitled to on reaching pensionable age, and its weekly rate;
- if they deferred it: the whole weeks deferred and the weekly increase;
- if a partner died: whether they are entitled to bereavement support payment.

Three goals sit under it:

1. **State pension** (`pa14-state-pension.l4`): ss 1(2), 2, 3, 4, 5(1), and Sch 1 paras 2, 4, 6 and 7.
2. **Deferral** (`pa14-deferral.l4`): s 17(1)-(4).
3. **Bereavement support payment** (`pa14-bereavement.l4`): ss 30(1), (6), and 31.

As the user asked, this covers only the sections those goals need. The rates are inputs, because the Act prescribes none.

## Seat

The encoding is written from the seat of **the pensioner or bereaved claimant**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Which state pension do I get and how much a week; how much more if I put it off; and can I get bereavement support payment?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | encoded (goal 1) |
| s 6 | out of scope: recalculation after a contracting-out reinstatement |
| ss 7-15 | out of scope: survivor's pensions, inheritance, reduced rate elections, pension sharing |
| s 16 | input: suspension is the start of a deferral period |
| s 17(1)-(4), (7) | encoded (goal 2); (6) up-rating is out of scope |
| ss 18-20 | out of scope: these are regulation powers; prisoners and overseas residents |
| ss 21-22 | definitions, used |
| ss 23-25 | out of scope |
| s 26 | out of scope: it amends the pensionable-age table in the Pensions Act 1995, which the conversion drops; the day of pensionable age is an input |
| ss 27-29 | out of scope |
| s 30(1), (5)-(6B) | encoded (goal 3); (1A)-(1D) priority among several claimants is out of scope |
| s 31 | encoded (goal 3) |
| ss 32-56 (Parts 3-6) | out of scope: private pensions, automatic enrolment, the Pensions Regulator, the PPF |
| Sch 1 Parts 1-3 | encoded (goal 1); Step 1 (para 3) and para 5 are inputs |
| Schs 2-10 and the rest | out of scope |

## Forks (readings taken)

- **F1, lost formulas.** The conversion drops the formulas in s 3(2) and Sch 1 paras 4(4) and 7(3). Each is used in its printed form, N ÷ 35 of the full rate.
- **F2, s 1(2).** Reaching pensionable age on 6 April 2016 is not "before 6 April 2016", so it brings entitlement under this Part.
- **F3, ss 2 and 4.** A person with at least one pre-commencement qualifying year and at least the minimum number of years in total is under s 4 (transitional), never s 2. The minimum counts pre- and post-commencement years together.
- **F4, Sch 1 para 6.** The part of the foundation amount up to the 2016 full rate is revalued by the ratio of the full rate at pensionable age to the 2016 full rate. The excess is increased by the revaluing percentage.
- **F5, s 5(1).** The transitional rate is the greater of two amounts: the pre- and post-commencement amounts together, capped at the full rate; and the pre-commencement amount alone.
- **F6, s 17(3): "each whole week in the period".** It is the number of days, counting the first and last days, divided by 7 and rounded down.
- **F7, s 17(2).** No increase is made when the increase would be under 1% of the weekly rate.
- **F8, s 30(1)(b): "under pensionable age when the spouse ... dies".** The death is before the day the claimant reaches pensionable age.
- **F9, s 31(1).** One tax year, with contributions actually paid, whose earnings factor is at least 25 × that year's lower earnings limit.
- **Known limits (from the independent pass).**
  - s 30(6) (a death before s 30 came fully into force, which was 6 April 2017 under the commencement order) is a yes/no input.
  - Where there is no entitlement, the weekly rate is 0, so read it with the kind.
  - One minimum number of years serves both s 2(3) and s 4(2).
  - Reaching pensionable age is assumed.
  - A deferral ending before it starts gives 0 weeks.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 128 assertions satisfied, 0 failed, 0 other errors — 38 the encoder's (`pa14-tests.l4`), 90 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F4:** confirm the revaluation split at the 2016 full rate.
