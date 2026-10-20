# Protection of Word "Anzac" Act 1920 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the Anzac penalty for` (`anzac-rules.l4`). It answers the most a person can get for a use of "Anzac" that breaches the Regulations. The encoded provisions are s 22(1)(g), (2) and (3). The source is the compilation of 28 February 2014.

## Seat

The encoding is written from the seat of **the person using the word "Anzac"**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "If my use of 'Anzac' breaches the Regulations, what is the most I can get?"

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | out of scope: short title |
| s 22(1) | (e) the Regulations are not deposited: the breach is an input; (g) encoded as the general limit |
| s 22(2) | encoded |
| s 22(3) | encoded |

## Forks (readings taken)

- **F1, s 22(2).** Imprisonment up to 12 months needs both a breach of subregulation 2(1) and one of the listed uses; a breach of 2(1) by another use takes the Regulations' penalty.
- **F2, s 22(3).** Likewise, a breach of subregulation 3(1) by naming a street, road or park.
- **F3, s 22(1)(g).** Any other breach carries the penalty the Regulations set, at most a $1,000 fine; the Regulations' own figure is not encoded.
- **Known limits (from the independent pass).**
  - Whether the Regulations' fine is also available beside the 12 months' imprisonment is not modelled.
  - The Regulations' own penalty is not in the source; only the $1,000 cap is given.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 18 assertions satisfied, 0 failed, 0 other errors — 8 the encoder's (`anzac-tests.l4`), 10 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** what penalty do the current Protection of Word "Anzac" Regulations set?
