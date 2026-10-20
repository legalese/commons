# Control of Naval Waters Act 1918 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the naval position for` (`cnw-rules.l4`). It answers:

- whether my craft is exempt;
- whether failing the superintendent's direction is an offence, and the maximum penalty units;
- whether I must pay the removal expenses on demand;
- the earliest day it may be sold at auction;
- the surplus paid to me, or the deficiency I still owe, after a sale.

The encoded provisions are ss 2, 6(1)-(2A), 6A(1)-(2) and 8. The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the master, person in charge or owner of a vessel, aircraft or vehicle in naval waters or on their foreshore**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Must I obey the superintendent's direction; must I pay for the removal; when can my property be sold, and what do I get back or still owe?"

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | out of scope |
| s 2 | encoded: exempt vessel; the other definitions are folded into the inputs |
| s 3-3C | out of scope: extension, Criminal Code, Proclamations, appointments (whether waters are naval waters is an input) |
| s 4 | out of scope: regulations |
| s 5 | out of scope: the Minister's prohibition |
| s 6 | (1)-(2A) encoded; (3) is an input to s 8 |
| s 6A | (1)-(2) encoded; (3) is an input to s 8 |
| s 7 | an input to s 8 |
| s 8 | encoded; (2) (detention) is noted |
| ss 9-10 | out of scope |

## Forks (readings taken)

- **F1, s 2(2).** Exempt vessels are outside every reference to a vessel, so neither the s 6 direction offence nor s 8 reaches them.
- **F2, s 6 and s 6A.** Section 6 covers only vessels within naval waters; s 6A covers aircraft, vehicles and vessels on the foreshore.
- **F3, s 8(3).** "After the expiration of 3 months after the making of a demand": the 3 months end on the corresponding day (or the month's last day where there is none), and a sale may be made from the next day.
- **F4, s 8(5)-(6).** The surplus or deficiency is the sale proceeds less the removal expenses and the expenses of the sale.
- **Known limits (from the independent pass).**
  - There is no input for whether a sale happened, so the surplus and deficiency are given whenever a sale day exists; with no sale, the deficiency is all the expenses.
  - The amount owed under s 8(1), detention (s 8(2)) and deemed ownership (s 8(4)) are not outputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 47 assertions satisfied, 0 failed, 0 other errors — 17 the encoder's (`cnw-tests.l4`), 30 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** may the sale happen on the corresponding day itself?
