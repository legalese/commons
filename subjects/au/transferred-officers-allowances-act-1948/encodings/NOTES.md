# Transferred Officers' Allowances Act 1948 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my allowances for` (`toa-rules.l4`). It gives the allowances payable to a transferred officer, or a widow, on a pension or retiring allowance at a given date. Sections 4-7 are encoded, as amended to 1956.

## Seat

The encoding is written from the seat of **the transferred officer, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What allowances are payable to me on my pension or retiring allowance, at a given date?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | the definition of "transferred officer" is assumed |
| s 4 | encoded |
| s 5 | encoded |
| s 6 | encoded, for 12 November 1955 to 31 December 1956 |
| s 7 | encoded: half rates for a widow, computed on the husband's pension |
| s 8 | out of scope |

## Forks (readings taken)

- **F1, the versions.** The compiled text carries the rates as amended in 1954 (from 31 October 1953) and 1956 (from 12 November 1955). Earlier rates are not in the text, so an earlier date answers NOTHING.
- **F2, s 5(1), "not ... exceeding Seven hundred and two pounds".** At exactly £702 no rate in (3)-(5) applies, so the allowance is nil.
- **F3, s 7.** The widow's allowances are half those her husband would receive on his pension. His pension rate is the input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 94 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`toa-tests.l4`), 76 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** is the widow's allowance computed on her husband's pension rate, or on her own widow's pension?
