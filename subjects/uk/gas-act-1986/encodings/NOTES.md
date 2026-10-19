# Gas Act 1986 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the gas consumer position for` (`gas-goal.l4`). It answers:

- **Connection:** whether the gas transporter must connect the premises, or keep them connected; what the consumer can be charged; and whether the consumer's own pipe vests in the transporter.
- **Cutting off for debt:**
  - the earliest day the supplier may cut off the supply or fit a prepayment meter;
  - whether it may do so on the day it did;
  - whether its officer may enter;
  - whether restoring the supply oneself is an offence;
  - whether the supplier may refuse to restore it.
- **Redress and resale:**
  - whether a consumer redress order can be made for the supplier's contravention;
  - whether the order's compliance date is lawful, the supplier's last day to appeal, and from when interest runs on unpaid compensation;
  - the most compensation in all;
  - what can be recovered on gas resold above the maximum price.

Three goals sit under it:

1. **Connection** (`gas-connection.l4`): ss 10(1)-(5A), (6), (8)-(10) and 11(1)-(2).
2. **Cutting off for debt, and entry** (`gas-cutoff.l4`): Schedule 2B paras 7, 11, 19, 24(1)(a), (2) and 28(1)(a).
3. **Redress and resale** (`gas-redress.l4`): ss 30G(1), (5), 30K, 30M(2), (5), 30N(1)-(2), (4), 30O(2)-(4) and 37(2)(b), (4)-(5).

The source is the revised text at 13 November 2025. Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the gas consumer**: the owner or occupier who wants a connection, takes a supply, or was affected by the supplier's breach. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Must the gas transporter connect my premises, or keep them connected, and what can I be charged? Can my supplier cut off my gas or fit a prepayment meter for an unpaid bill or deposit, from when, and may its officer enter; can I restore it myself; can it refuse to restore it? And if Ofgem acts on my supplier's breach, can a redress order still be made, by when must I be paid, and what can I recover on gas resold to me?"

The facts it asks for are ones that person can state, or findings made about them (the transporter's circumstances under s 10(9), the Authority's view under s 30N(2)).

The redress-order provisions address the Authority and the supplier. The encoding gives what they mean for the consumer: whether an order can still be made, when payment is due, and when interest runs.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-9 | out of scope: the regulators' duties and licensing |
| s 10(1)-(5A), (6), (8)-(10) | encoded (goal 1); whether a main is a relevant main (s 10(12)-(14)) is an input |
| s 10(7), (11) | out of scope: powers to make regulations |
| s 10A | out of scope: pipe-lines of the former public gas transporter |
| s 11 | encoded (goal 1) |
| ss 12-30 | out of scope: meters, safety, licences, enforcement orders (a final or provisional order is an input) |
| ss 30A-30F | out of scope: penalties are the supplier's matter; only the penalty amount enters, through s 30O(4) |
| s 30G | (1), (5) encoded (goal 3); (2)-(4), (6)-(8) are the order's content |
| ss 30H-30J | out of scope: content, procedure and policy (the s 30I(1) notice date is an input) |
| s 30K | encoded (goal 3) |
| s 30L | out of scope: enforcement of the order |
| s 30M | (2), (5) encoded (goal 3); the court's powers are not |
| s 30N | (1), (2), (4) encoded (goal 3); (3) is inert |
| s 30O | (2)-(4) encoded (goal 3); (1) concerns penalties alone; turnover is an input |
| ss 31-33AB | out of scope: standards of performance are set by regulations, which are not in the deposited text |
| ss 33B-36 | out of scope |
| s 37 | (2)(b), (4)-(5) encoded (goal 3); the direction's maximum price is an input |
| ss 38 onwards | out of scope (a s 38(1) notice date is an input) |
| Schedule 2B paras 1-6, 8-10 | out of scope |
| Schedule 2B para 7 | encoded (goal 2) |
| Schedule 2B para 11 | encoded (goal 2): whether there is consent |
| Schedule 2B paras 12-18, 20-23 | out of scope |
| Schedule 2B para 19 | encoded for cut-offs by a supplier under para 7 (goal 2) |
| Schedule 2B para 24 | (1)(a), (2) encoded (goal 2) |
| Schedule 2B paras 25-27 | out of scope |
| Schedule 2B para 28 | (1)(a) encoded (goal 2) |
| other Schedules | out of scope |

## Forks (readings taken)

- **F1, s 10(1)(a) and (b).** Premises within 23 metres of a relevant main are treated as (a) premises even if they could also be connected by the consumer's own pipe. The transporter then lays the pipe.
- **F2, Sch 2B para 7(3).**
  - "Within 28 days after the making of the demand": payment by the demand day + 28 is in time.
  - The power arises on the demand day + 29, or for a deposit, the request day + 8.
  - The notice of intention must be given on or after that day. The earliest day to act is the notice day + 7.
- **F3, Sch 2B para 7 (changed after the independent pass).** Once the 28 (or 7) days have passed unpaid, the power stays open: a later payment, deposit or prepayment agreement does not end it. Para 7 says nothing to the contrary; para 19 deals with restoring the supply once the default is made good.
- **F4, Sch 2B para 19.** It is encoded only for cut-offs that para 7 allowed. After any other cut-off, para 19 gives the supplier no right to refuse.
- **F5, "N months from", "5 years from".** Each is the corresponding date N months on, or the last day of the month where it has none. So 29 February 2020 gives 28 February 2025.
- **F6, s 30K(3).** The s 30I(1) notice must be served on or after the final order, confirmation or provisional order, and within the 3 (or 6) months from it.
- **F7, s 30M(5).** Only an appeal made within the 42 days suspends compliance. Interest then runs from the day after the original compliance date once the appeal is determined. Any new date the court sets (s 30M(3)) is not modelled.
- **F8, s 30O(4).** The most compensation is 10% of turnover less any penalty for the same contravention, not below 0.
- **F9, s 37(4).** The excess over the applicable maximum price, plus the interest the direction provides for, is recoverable; nothing if there is no excess.
- **Known limits (from the independent pass).**
  - s 10(3): "connected" and "still required" are one input.
  - s 10(5), (5A): whether the licence allows the charge is not an input, and no amount is computed.
  - s 10(9)(b): danger and reasonable steps are one input.
  - Para 11: the exclusion of cut-offs under paras 20-22 and safety regulations is not modelled, nor the supplier's power to cut off again.
  - Para 24(3): notice fixed to unoccupied premises is not modelled.
  - s 37(2)(b): a reduction by an amount or percentage must be given as the reduced maximum.
  - s 30G(1)(b): asked as "I suffered loss", though an order can be made where only other consumers did.
  - The para 7(3) notice is required on or after the day the power arises, and counted as notice day + 7, not clear days; both readings are open.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 7 modules: 207 assertions satisfied, 0 failed, 0 other errors — 110 the encoder's (`gas-tests.l4`), 97 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F3:** does a late payment, made after the 28 days but before the cut-off, end the para 7(3) power? The encoding says it does not.
- **F2:** may the 7 days' notice be given during the 28 days, so that it runs in parallel?
