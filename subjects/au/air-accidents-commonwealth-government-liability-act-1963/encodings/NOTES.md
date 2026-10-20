# Air Accidents (Commonwealth Government Liability) Act 1963 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the air position for` (`aa-rules.l4`). It answers:

- the Part that applies;
- the maximum liability;
- the damages recoverable under this Act;
- whether my action can be heard now.

The encoded provisions are ss 4, 6, 8, 10(1), 11, 12, 14, 15(1), 16(1) and 17. The source is the compilation of 17 June 2021.

## Seat

The encoding is written from the seat of **the passenger killed or injured in an air accident, or their dependants**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is the Commonwealth liable under this Act; how much can be recovered; is my claim barred or on hold?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 5 | out of scope: machinery |
| s 4 | passenger encoded; the other definitions are folded into the inputs |
| s 6 | encoded |
| s 7 | applied: the accident must be on board or in embarking or disembarking (Carriers' Liability Act s 28); the other incorporated provisions are out of scope |
| s 8 | encoded |
| s 9 | out of scope: substitution for other liabilities |
| s 10 | (1)(a) encoded; (1)(b), (2)-(3) are out of scope |
| s 11 | encoded |
| s 12 | encoded |
| s 13 | out of scope |
| s 14 | encoded |
| s 15 | (1)(a) encoded; the rest is out of scope |
| s 16 | (1) encoded; (2)-(3) are out of scope |
| s 17 | encoded |
| s 18 | out of scope |

## Forks (readings taken)

- **F1, ss 8, 14.** The damages assessed are capped at the maximum liability, then reduced by the deductions, not below nil.
- **F2, s 14(2)(a).** Under Part III, damages or compensation from the carrier and anyone else other than the Commonwealth are deducted; under Part II only the Commonwealth-funded insurance (s 8(2)).
- **F3, ss 16-17.** They are in Part III and bar or stay only a Part III claim.
- **F4, Part II on-board limit.** Through the incorporated Carriers' Liability Act s 28, a Part II accident must likewise be on board or in embarking or disembarking.
- **Known limits (from the independent pass).**
  - The liable body (the Commonwealth, an authority, the ACT or NT) is not named, and the ACT and NT share one input.
  - The two limbs of the s 4 passenger exclusion are one input.
  - "Can be heard now" is FALSE both for a barred or nil claim and for one stayed by s 17.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 58 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`aa-tests.l4`), 40 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** is the cap applied before or after the s 8(2) and s 14(2) deductions?
