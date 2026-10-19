# First Home Super Saver Tax Act 2017 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my first home super saver tax for` (`fhss-rules.l4`). It gives the first home super saver tax: 20% of the assessable FHSS released amount. The whole operative Act is encoded: ss 2-4. The source is the Act as made (No. 133, 2017).

## Seat

The encoding is written from the seat of **the person whose first home super saver amounts were released**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "How much first home super saver tax must I pay?"

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | out of scope |
| s 2 | applied: commencement on 1 July 2018 |
| s 3 | encoded: whether tax is payable under s 313-60 of the Income Tax Assessment Act 1997 is an input |
| s 4 | encoded |

## Forks (readings taken)

- **F1.** The "assessable FHSS released amount", and liability under s 313-60, are terms of the Income Tax Assessment Act 1997. They are inputs.
- **F2.** A release before 1 July 2018 attracts no tax under this Act, and the answer is NOTHING.

- **Known limits (from the independent pass).** A negative amount is not rejected. The commencement date comes from column 3 of the s 2 table, which is not part of the Act.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 14 assertions satisfied, 0 failed, 0 other errors — 6 the encoder's (`fhss-tests.l4`), 8 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
