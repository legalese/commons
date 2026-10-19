# Superannuation (Pension Increases) Act 1961 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my annual pension increase for` (`spi61-rules.l4`). It gives the increase in a prescribed pensioner's (or widow's) annual pension, in pounds. Section 4, with the definitions in s 3 that it needs, is encoded. The source is the compilation on the Federal Register of Legislation.

## Seat

The encoding is written from the seat of **the prescribed pensioner, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What increase in my annual pension am I entitled to, and from when?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | "the prescribed amount" encoded; the unit figures, "prescribed pensioner" and "the prescribed time" are inputs |
| s 4 | (1), (2), (4), (6) encoded; (3) and (5) (ss 65-66 of the 1922 Act) are out of scope |
| s 6 | out of scope |
| s 7 | (1) noted: the increase runs from the first fortnightly payment after commencement (an input) |

## Forks (readings taken)

- **F1, s 3 "the prescribed amount" (c)-(d).** The proportions depend on the 1922 Act's scales and on other pension amounts, so the fraction is an input. For (d), the fraction must combine its own proportion with any (b) or (c) proportion. If s 52 applied but the person did not neglect to contribute, the standard case applies.
- **Known limits (from the independent pass).** The s 4(6) exclusions are one input. The s 7(1) start date is not used in any rule. The unit figures are not checked against their definitions.
- **F2, s 4(2).** The 1957 increase is deducted from this Act's increase, which cannot fall below nil.
- **F3, s 4(4).** The widow's increase is five-eighths of her husband's, after s 4(2).
- **F4.** Unit entitlements come from the scale in s 13(1) of the Superannuation Act 1922, which is not in the deposited text. They are inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 29 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`spi61-tests.l4`), 20 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** is the widow's increase computed before or after the s 4(2) offset?
