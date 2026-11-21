# Regulation W (12 CFR Part 223) — covered transactions, limits, collateral and exemptions

Status, 2026-11-21: **in progress.** The rows marked `done` below are encoded and their tests pass; the rest are `not started`.
This file is updated after each section lands; a row moves only when its tests pass.

## Scope

This encoding takes the member bank's question about one proposed or existing transaction: may the member bank enter into it with this company, and what does it count for?
It covers the valuation sections 223.21(a) and 223.22 to 223.24, the definition of a covered transaction in 223.3(h), the attribution rule in 223.16, the quantitative limits in 223.11 and 223.12, the safety and soundness requirement in 223.13, the collateral requirements in 223.14, the low-quality asset prohibition in 223.15 and the exemptions in 223.41 and 223.42.
It does not cover the sequence rule in 223.21(b)(2) and the matching rules in 223.22(b)(2) and 223.23(b)(2), section 23B (223.43, 223.51 to 223.56 and the market-terms conditions that other sections cross-refer to), 223.31 to 223.33, 223.61, 223.71 and 223.72.
Who is an affiliate is the definition encoded in `../affiliates-2026-11/`; this encoding takes that answer from copies of its modules (see "Copied modules").
The source is the Part 223 deposit under `../../source/`.

## Target and checks

Target compiler: `main`.
Checked with `1.6.112 (main, e4f4bf3, 2026-11-18)`.

## Seat

The seat is the member bank to which the regulation is applied (a company, not an official): "may I enter into this transaction with this company, and what does it count for?"

## Conventions assumed for this encoding (assumed, not ruled)

- Dollar amounts are plain numbers in one currency unit; percentages are compared exactly, with no rounding anywhere.
- Capital stock and surplus (223.3(d)) is a stated number: the encoding does not compute it from the capital rules.
- Whether a transaction is on terms consistent with safe and sound banking practices (223.13) is a stated judgement.
- Each function answers for one instant, from the facts stated to it.
  How a value moves over time (an amortization, a carrying value, a collateral value) is an input, not a computation.
- A determination or approval by the Board or an appropriate Federal banking agency is a stated input.

## Coverage table

Dispositions: `done` (encoded and tested), `WIP` (encoded, not yet passing), `not started`.

| provision | what it says, in short | disposition |
| --- | --- | --- |
| 223.21(a) | valuation of a credit transaction: the greater of three amounts; an acquired credit transaction | done |
| 223.22 | valuation of an asset purchase, and which rule values each kind of purchase | done |
| 223.23 | valuation of a security issued by an affiliate | done |
| 223.24 | valuation of credit to a nonaffiliate secured by affiliate securities; eligible affiliated mutual fund securities | done |
| 223.3(h), (i), (j), (o) | covered transaction, its five limbs; credit transaction | not started |
| 223.3(d) | capital stock and surplus, as a stated number | not started |
| 223.11, 223.12 | the 10 percent and 20 percent limits | not started |
| 223.13 | safety and soundness, a stated judgement | not started |
| 223.14 | collateral requirements | not started |
| 223.15 | low-quality assets, and its exception | not started |
| 223.16 | transactions treated as with an affiliate | not started |
| 223.41, 223.42 | exemptions | not started |
| the top-level assessment | one proposed transaction: covered, valued, limits, collateral, what stays live | not started |
| 223.21(b), 223.22(b)(2), 223.23(b)(2) | timing, and the sequence rule | out of scope: sequences are a separate phase |
| 223.31 to 223.33, 223.43, 223.51 to 223.56, 223.61, 223.71, 223.72 | acquisitions, financial subsidiaries, derivatives, section 23B, other | out of scope |

## Forks and open questions

**223.24(b): a negative value.**
The text says the value is the lesser of "(1) The total value of the extension of credit less the fair market value of the nonaffiliate collateral" and the affiliate securities' fair market value if verified.
If the nonaffiliate collateral is worth more than the extension of credit, the first figure is negative, and the text does not say whether the value is then zero.
The encoding follows the words and returns the negative figure.

**223.21(a)(4)(ii): the "principal amount" of a revolving credit facility.**
The text does not say whether it is the amount drawn or the amount of the facility.
It does not matter for the printed example, because the sum under (a)(1)(iii) gives $300 on either reading, and the tests state the principal as the amount drawn.
