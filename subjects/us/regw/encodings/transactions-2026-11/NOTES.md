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
| 223.3(h), (i) | covered transaction, its five limbs; credit transaction (the kinds of transaction (j) and (o) describe are the stated `kind`) | done |
| 223.3(a), (d) | the aggregate amount; capital stock and surplus, as a stated number | done (an input) |
| 223.11, 223.12 | the 10 percent and 20 percent limits | done |
| 223.13 | safety and soundness, a stated judgement | not started |
| 223.14 | collateral requirements: the percentages, ineligible collateral, priority deductions, exceptions; the replacement rule (e) as the same test at one instant | done |
| 223.15, 223.3(v) | low-quality assets, and the exception for renewals of participations | done, with a fork on (b)(3) |
| 223.16 | transactions treated as with an affiliate | (a), (b) and the exemptions in (c) done |
| 223.41 (a)-(d) | exemptions: parent and sister depository institutions, nonrecourse loan purchases, internal reorganizations | done (each a predicate on stated facts) |
| 223.42 (a)-(o) | exemptions: deposits, uncollected items, cash and government security collateral, servicing affiliates, liquid assets, marketable and municipal securities, repurchase agreements, new banks, bank mergers, nonrecourse extensions of credit, intraday credit, riskless principal, securities financing and commercial paper | done (each a predicate on stated facts) |
| the top-level assessment | one proposed transaction: covered, valued, limits, collateral, what stays live | not started |
| 223.21(b), 223.22(b)(2), 223.23(b)(2) | timing, and the sequence rule | out of scope: sequences are a separate phase |
| 223.31 to 223.33, 223.43, 223.51 to 223.56, 223.61, 223.71, 223.72 | acquisitions, financial subsidiaries, derivatives, section 23B, other | out of scope |

## Forks and open questions

**223.15(b)(3) "by more than 5 percent" (a switch, default: five percentage points; assumed, not ruled).**
223.15(b)(3): "The participating member bank's share of the renewal or extension of additional credit does not exceed its proportional share of the original transaction by more than 5 percent, unless the member bank obtains the prior written approval of its appropriate Federal banking agency".
It can mean five percentage points of the transaction above the proportional share, or five percent more than the proportional share itself.
With a proportional share of 25 percent the first allows a share up to 30 and the second up to 26.25; the tests assert both readings at 29 and at 26.25 and 26.3.

**223.42(c): what counts as "secured by" (assumed, not ruled).**
The printed example uses market values.
The encoding uses the collateral's effective value (223.14(d): perfected, after the deduction for a senior interest), so a transaction is exempt only "to the extent that" it is secured by interests that would count under 223.14; the text of (c) does not say.
In the printed example, with perfected first-priority collateral, it makes no difference.

**Dates in 223.42(n) and (o).**
(n) runs "From September 15, 2008, until October 30, 2009 (unless further extended by the Board)" and (o) needs a purchase "on or after September 19, 2008".
Whether a period is running, as the Board may have extended it, is a stated input, so the encoding does not read a calendar.

**223.14(d)(1): collateral whose security interest is not perfected (assumed, not ruled).**
The text says the member bank "must maintain a security interest in collateral required by this section that is perfected and enforceable under applicable law" and does not say how an imperfect interest is valued.
The encoding gives such collateral no effective value.

**223.14(b)(2): combining several kinds of collateral.**
The printed example secures a $1,000 loan with $500, $480 and $130 of three kinds, and says each secures "$500 of the loan", "$400 of the loan" and "$100 of the loan".
The encoding sums, over the items, each effective value divided by its percentage, and compares the sum with the amount to be secured; the text does not state the general rule, only the example, so this is the reading of it.

**223.24(b): a negative value.**
The text says the value is the lesser of "(1) The total value of the extension of credit less the fair market value of the nonaffiliate collateral" and the affiliate securities' fair market value if verified.
If the nonaffiliate collateral is worth more than the extension of credit, the first figure is negative, and the text does not say whether the value is then zero.
The encoding follows the words and returns the negative figure.

**223.21(a)(4)(ii): the "principal amount" of a revolving credit facility.**
The text does not say whether it is the amount drawn or the amount of the facility.
It does not matter for the printed example, because the sum under (a)(1)(iii) gives $300 on either reading, and the tests state the principal as the amount drawn.

## Copied modules

The three modules below are copied byte for byte from `../affiliates-2026-11/` (the stable `l4` resolves `IMPORT` only within the importing file's folder), at the commit that deposited them; they are not edited here.
A fix is made in `../affiliates-2026-11/` first and the copy is refreshed.

| module | sha256 |
| --- | --- |
| `regw-nouns.l4` | `e007695972e9d6e5d52c11441714e0153b1be06094bab55c650f07df2a6d310f` |
| `regw-control.l4` | `739ab38aa36741d3dad900a132ee6999c802b125b4e04be8bf79ae9c3daab1da` |
| `regw-affiliate.l4` | `ae84eafb392c0010086ebef24ce563b1b9876c2b909dea903f16111857af88a6` |
