# Superannuation (Pension Increases) Act 1967 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my annual pension increase for` (`spi67-rules.l4`). It gives the increase in an eligible pensioner's (or widow's) annual pension. Section 4, with the s 3 definitions it needs, is encoded.

## Seat

The encoding is written from the seat of **the eligible pensioner, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What increase in my annual pension am I entitled to?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | "the relevant amount" encoded; the unit figures and "eligible pensioner" are inputs |
| s 4 | encoded |
| s 6 | out of scope |
| s 7 | (1) noted: from the first fortnightly payment after commencement |

## Forks (readings taken)

- **F1, s 3 "the relevant amount" (c)-(e).** The proportions depend on the 1922 Act's scales and on pensions that would otherwise have been payable. The fraction is an input.
- **F2, s 4(2).** The three earlier increases are summed and deducted, and the result cannot fall below nil.
- **F3, s 4(3).** The widow's share (one-half or five-eighths) is taken of her husband's increase after s 4(2).

- **Known limits (from the independent pass).** The s 4(4) exclusion is one input. The actual unit entitlement is an input, and case (b) is not checked against it. The s 7(1) date is not computed. For a widow, s 4(2) speaks of an "eligible pensioner"; the offset is applied to her husband's increase.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 26 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`spi67-tests.l4`), 17 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** is the widow's share computed before or after the s 4(2) offset?
