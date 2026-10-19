# Customs Undertakings (Penalties) Act 1981 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my undertaking penalty for` (`cup-rules.l4`), answering the question below. The scope is set out in BRIEF.md.

## Seat

The encoding is written from the seat of **the person who gave a Customs undertaking**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What penalty do I owe for breaching my Customs undertaking?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2A, 3A | out of scope |
| s 3 | encoded: the prescribed percentage and value per unit |
| s 4 | encoded |

## Forks (readings taken)

- **F1, s 4(2).** The reduction is the full penalty × (the quantity or value entered ÷ the quantity or value required), capped at the full penalty.
- **F2, s 3(2).** A unit value in the undertaking fixes the value of the goods.

- **Known limits (from the independent pass).** The s 4(2) conditions (the periods, the tariff items) are the caller's: only qualifying entries are entered. More than required caps the reduction at the full penalty.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 15 assertions satisfied, 0 failed, 0 other errors — 4 the encoder's (`cup-tests.l4`), 11 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
