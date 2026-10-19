# Taxation (Cross-border Trade) Act 2018 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the import position for` (`tcta-goal.l4`). For imported goods it answers:

- the liabilities to import duty, and when each arises;
- the persons liable;
- the ad valorem duty;
- for the first liability, the last day for HMRC to notify it and whether it is enforceable.

The rules are in `tcta-rules.l4`:

1. **Liability:** ss 2(1), 3(3)-(4), 4(1)-(4) and 5(1)-(2).
2. **Persons liable:** s 6(1)-(4), (7).
3. **Amount and notification:** ss 7 and 16(2)-(3), and Sch 6 paras 1 and 4.

## Seat

The encoding is written from the seat of **the importer (or other person who may be liable for import duty)**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "I am bringing goods in. Do I owe import duty, and from when; am I one of the people liable; how much is it; and until when can HMRC still notify me of it?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-6 | encoded (goals 1-2) |
| ss 7, 16 | encoded (goal 3): the applicable rate is an input |
| ss 8-15, 17-19 | input: the rate after the tariff, preferences, quotas, suspensions, remedies, origin and reliefs |
| ss 20-30 | out of scope, apart from Sch 6 paras 1 and 4 |
| ss 30A-30C | out of scope: Northern Ireland |
| ss 31-38 | definitions used; the rest is out of scope |
| Part 1 Schedules other than Sch 6 paras 1, 4 | out of scope |
| Parts 2-3 (export duty, VAT, excise) | out of scope |

## Forks (readings taken)

- **F1, s 4(3).** For storage, transit and inward processing:
  - an unentitled declaration incurs liability when it is made;
  - otherwise liability arises only at the first breach.
- **F2, s 4(4).** For authorised use and temporary admission:
  - liability arises at acceptance, at the reduced rate if entitled and the applicable rate if not;
  - a breach gives a further liability at the normal rate, less the earlier liability.
- **F3, s 6(2).** Possession or control on entry makes a person liable only for s 5 liabilities, that is, goods not presented or not declared.
- **F4, Sch 6 para 4.** The notification must come before the end of the 3 years (or 20 years) beginning with the day the liability was incurred. That period ends on the day before the corresponding date, or on the last day of the month if it has none.
- **F5.** The top-level duty amount is 0 where no liability is incurred. Only the first liability's notification date is reported.
- **F6, s 6 (changed after the independent pass).** No one is liable where no liability is incurred.
- **Known limits (from the independent pass).**
  - "Jointly and severally" (s 6(7)) is not an output; the goal returns the list of persons.
  - The s 6(4) knowledge test is one input.
  - A notification dated before the liability was incurred is not rejected.
  - Goods not presented with no forfeiture date, and a breach under authorised use or temporary admission with no acceptance date, give no liability rather than a refusal.
  - The s 4(4)(d) further liability is not computed as an amount, and only the first liability's notification limit is reported.
  - One offence flag applies the 20-year limit to every liability in the case.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 5 modules: 85 assertions satisfied, 0 failed, 0 other errors — 23 the encoder's (`tcta-tests.l4`), 62 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** how is the further liability on a breach computed where partial relief already applied?
