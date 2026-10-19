# Commonwealth Entities (Payment Surcharges) Act 2024 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the surcharge position for` (`ceps-rules.l4`). It answers:

- whether this Act authorises a surcharge on a payment to a Commonwealth entity;
- that a refund is in the entity's discretion;
- that non-compliance with the surcharging policies does not invalidate the decision.

The operative ss 4-6 and 7(1)-(2) are encoded. The source is the Act as made (No. 101, 2024), which commenced on 3 December 2024.

## Seat

The encoding is written from the seat of **the person making a payment to a Commonwealth entity**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "May the Commonwealth entity charge me a surcharge for how I pay; can I get it refunded; and if the entity did not follow the surcharging policies, is the charge invalid?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope |
| s 4 | "payment surcharge" and "surchargeable payment" applied; the rest are out of scope |
| s 5 | encoded |
| s 6 | encoded: the refund is discretionary |
| s 7 | (1)-(2) encoded; (3)-(7) (the Minister's policies and directions) are out of scope |

## Forks (readings taken)

- **F1, s 5(1)(b) (changed after the independent pass).** Where another law already lets the entity surcharge the payment, or the amount is not a payment surcharge, this Act does not authorise it: the answer is FALSE. That other law governs.
- **F2, s 5(2), "must not be such as to amount to taxation".** This is a finding, and it is an input. A surcharge that amounts to taxation is not authorised.
- **F3, s 6.** A refund is possible only for a surcharge charged under s 5, and is in the entity's discretion. The encoding does not decide whether one will be given.

- **Known limits (from the independent pass).** The s 7(1) duty is to take all reasonable steps, and whether it was breached is not reported. An amount that is both kinds of surcharge cannot be entered. A charge before 3 December 2024 is not distinguished.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 31 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`ceps-tests.l4`), 22 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
