# Pension Schemes Act 1993 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the leaver position for` (`psa93-goal.l4`). For a member leaving an occupational scheme early it answers:

- whether they are entitled to short service benefit, and the latest age from which it must be payable;
- whether they may instead elect a cash transfer sum or a contribution refund, and the amount of the refund;
- for a transfer of a cash equivalent: the last day to apply, whether the right is lost, and the trustees' last day to carry out the transfer.

Two goals sit under it:

1. **Early leavers** (`psa93-leavers.l4`): ss 71(1), (3), (7), (10)-(11), 101AA(1)-(2), and 101AB(1), (4).
2. **Cash equivalent transfers** (`psa93-transfers.l4`): ss 94, 95(1A), 98(1), and 99(2)-(3), (7).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the scheme member leaving early**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "I have left my job before pension age. Am I entitled to a preserved pension, or can I take a transfer or a refund, and how much; and if I transfer, by when must I apply and by when must the trustees pay out?"

The facts it asks for are ones that person can state, or findings made about them.

The trustees' deadline and the duty to tell the Regulator state the trustees' duties. For the member, they are the dates by which the transfer must reach them, and the point at which a delay must be reported.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| Parts I-III | out of scope: contracting out, guaranteed minimum pensions |
| s 69 | the scope of Chapter I is assumed |
| s 71 | encoded (goal 1); (4)-(6), (8)-(9) are out of scope (whether earlier service counts is an input) |
| ss 72-92 | out of scope: the form and computation of short service benefit, revaluation |
| s 93A | input: the guarantee date |
| s 94 | encoded (goal 2) |
| s 95(1A) | encoded (goal 2); (1)-(6) the ways of taking the cash equivalent are out of scope |
| s 97 | out of scope: the calculation of cash equivalents |
| s 98(1) | encoded (goal 2); (2)-(4) are out of scope |
| s 99(2)-(3), (7) | encoded (goal 2); (2ZA)-(2A), (4)-(4B) and (8) are out of scope |
| s 101AA-101AB | encoded (goal 1); the cash transfer sum amount is not computed |
| ss 101AC onwards | out of scope |

## Forks (readings taken)

- **F1, "2 years' qualifying service" made of several periods.** Earlier counting service (in days) is placed before the latest period. The two years are then measured as a single run from that adjusted start. This is exact for one period, and close where there are several.
- **F2, s 71(1)(aa).** Thirty days is met at the adjusted start + 29.
- **F3, s 101AA.** The three-month condition is measured the same way. A member with short service benefit has "relevant accrued rights", so is outside Chapter 5.
- **F4, s 101AB(4).** The refund is the employee contributions plus the transfer-related contributions, the latter capped at the transfer payment.
- **F5, s 95(1A)(a): "within the period of 3 months beginning with the guarantee date".** The last day is the day before the corresponding date. Limb (b) is the corresponding date one year before normal pension age. The earlier of the two applies to benefits that are not flexible.
- **F6, s 99(2).** The 6 months begin with the guarantee date (for benefits other than money purchase) or the application date (for money purchase), ending on the day before the corresponding date. For s 99(3), "the end of the period of 3 months after the conclusion" is the corresponding date, and it applies where it is later.
- **F7, s 99(7): "within six months of the date".** Read like s 99(2): within the 6 months beginning with the date. Changed after the independent pass.
- **Known limits (from the independent pass).**
  - s 99(3) takes only the date proceedings concluded. Running proceedings, and the trustees' view that forfeiture may follow, are not inputs.
  - There is no as-at date: with no application, s 98(1) answers "lost", and with no transfer date, s 99(7) answers "notify".
  - Normal pension age is entered both as an age and as a date.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 112 assertions satisfied, 0 failed, 0 other errors — 31 the encoder's (`psa93-tests.l4`), 81 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** how should discontinuous periods totalling 2 years be counted?
