# Welfare Reform Act 2012 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the welfare position for` (`wra-goal.l4`). It answers:

- whether universal credit is payable, and the award;
- the personal independence payment components and their rates;
- the benefit cap reduction.

Three goals sit under it:

1. **Universal credit** (`wra-universal-credit.l4`): ss 3, 4(1), 5 and 8(1)-(3).
2. **Personal independence payment** (`wra-pip.l4`): ss 77(4), 78(1)-(2), 79(1)-(2), 82(2)-(3) and 83.
3. **The benefit cap** (`wra-cap.l4`): s 96(2), (5) and (5A).

The amounts of the elements, deductions, PIP rates and capital limits are set by regulations, so they are inputs. The benefit cap annual limits are printed in s 96(5A) and are used as written.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | the claim structure, applied |
| ss 3-5 | encoded (goal 1); the s 4(2)-(7) regulation powers are out of scope |
| ss 6-7 | out of scope: waiting days and assessment periods |
| s 8 | encoded (goal 1) |
| ss 9-12 | input: the amounts of the elements |
| ss 13-76 | out of scope: requirements, sanctions, migration, Parts 2-3 |
| ss 77-79 | encoded (goal 2); the rates are prescribed |
| ss 80-81 | input: the assessment findings and the required period condition |
| s 82 | encoded (goal 2) |
| s 83 | encoded (goal 2); exceptions by regulations are out of scope |
| ss 84-95 | out of scope |
| s 96(2), (5), (5A) | encoded (goal 3) |
| ss 96(5B)-(10), 96A-97 | regulation powers; which limit applies is an input |
| the rest | out of scope |

## Forks (readings taken)

- **F1, s 4(1)(a)-(b).** A claimant is 18 from the 18th birthday, and below the qualifying age for state pension credit before that date.
- **F2, s 3(2).** Joint claimants are entitled only if each meets the basic conditions. An empty claimant list is not entitled.
- **F3, s 5(1)(b).** The financial condition is tested on the award as computed, which must be at least the prescribed minimum.
- **F4, s 8.** The award is the maximum amount less the deductions, floored at 0.
- **F5, s 83(1): "for any period after the person reaches the relevant age".** The person is entitled up to and including the later of the day of pensionable age and the 65th birthday.
- **F6, s 82.** A terminally ill person claiming on that ground gets the enhanced daily living rate, and needs no required period for mobility; the mobility rate still follows the assessment.
- **F7, s 96(2), (5).** The relevant amount is the annual limit × reference period days ÷ 365, with no rounding. The reduction is the full excess, although the Act permits "up to" it.
- **F8, 29 February birthdays.** A person born on 29 February is taken to reach an age on 28 February in a non-leap year. The Family Law Reform Act 1969 s 9 reading (1 March) would differ by a day.
- **Known limits (from the independent pass).**
  - s 82(1)(a)-(b) is one input, and s 82(5) is not shown.
  - The relevant age is applied, not reported as a date.
  - For joint claimants, capital and the deductions are entered combined.
  - The top-level award is 0 where the claimant is not entitled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 139 assertions satisfied, 0 failed, 0 other errors — 37 the encoder's (`wra-tests.l4`), 102 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F7:** confirm the 365-day apportionment of the annual limit, which regulations under s 96(5B)(c) may vary.
