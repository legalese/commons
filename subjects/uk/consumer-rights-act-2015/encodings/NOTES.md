# Consumer Rights Act 2015 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the consumer position for` (`cra-goal.l4`). When goods or services do not conform, it answers:

- **Goods:**
  - the last day for the short-term right to reject;
  - whether the fault is presumed to have existed on delivery;
  - whether the tier-two remedies are available;
  - the refund on final rejection, and the last day to pay it.
- **Services:** whether repeat performance can be required, whether a price reduction is available, and the last day for its refund.

Three goals sit under it:

1. **The short-term right to reject** (`cra-goods.l4`): s 22(1)-(8).
2. **The presumption and the final right to reject** (`cra-goods.l4`): ss 19(14)-(15), 20(15), and 24(5), (8)-(11).
3. **Services** (`cra-services.l4`): ss 54(3), 55(3), and 56(3)-(4).

Whether goods or a service conform to the contract (ss 9-18, 49-53) is an input. Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the consumer**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "The goods or service I bought are faulty. Until when can I reject them; will the fault be presumed to have been there from the start; can I now reject them for good or get money off, and how much will I get back and by when; and for a service, can I insist it is redone or get a reduction?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-18 | input: whether the goods conform |
| s 19(1)-(13) | the remedies structure, applied; (14)-(15) encoded |
| s 20 | (15) encoded; the rest is not computed (refund mechanics, hire and hire-purchase variants) |
| s 21 | out of scope: partial rejection |
| s 22 | encoded (goal 1) |
| s 23 | input: whether repair or replacement can be required, and the trader's delay |
| s 24(5), (8)-(11) | encoded (goal 2); the price reduction amount ("appropriate amount") is not computed |
| ss 25-32 | out of scope |
| Chapter 3 (digital content) | out of scope |
| ss 48-53 | input: whether the service conforms |
| ss 54-56 | encoded (goal 3) |
| s 57 onwards, Parts 2-4, Schedules | out of scope |

## Forks (readings taken)

- **F1, s 22(3): "the end of 30 days beginning with the first day after these have all happened".** The last event is day E; the limit is E + 30.
- **F2, s 22(4).** For perishable goods, the limit is the earlier of the 30 days and the end of the shorter period.
- **F3, s 22(6)-(8).** The waiting period counts both the request day and the day the goods are received. The limit moves later by that many days. A request made after the limit has passed changes nothing.
- **F4, s 22(7).** If the goods supplied still do not conform, the limit is the later of the day received + 7 and the extended limit.
- **F5, s 19(14).** The fault must appear within the six months beginning with delivery, which end on the day before the corresponding date.
- **F6, s 24(10)-(11).** The first 6 months begin on E + 1. Exercising the right on or before their last day means no deduction for use, unless the goods are a motor vehicle or specified goods. Otherwise the deduction claimed is taken off the price.
- **F7, ss 20(15), 56(4).** The refund is due within 14 days beginning with the day the trader agrees, so by that day + 13.
- **Known limits (from the independent pass).**
  - The refund on final rejection is 0 when the tier-two remedies are not available, so read it with that answer.
  - s 24(9) (use while the trader failed to collect) is not modelled.
  - The goods refund date is given only for tier-two remedies, and the agreement date is a required input.
  - Impossible inputs (goods received back before the request, a fault before delivery) are not checked.
  - The services price reduction under s 54(4)-(5) is not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 120 assertions satisfied, 0 failed, 0 other errors — 38 the encoder's (`cra-tests.l4`), 82 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F3:** does the waiting period "stop the period running" by its full inclusive length, even where the request comes on the last day?
