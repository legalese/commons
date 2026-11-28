# Regulation W (12 CFR Part 223) — covered transactions, limits, collateral and exemptions

Status, 2026-11-21: **in progress.** The rows marked `done` below are encoded and their tests pass; the rest are `not started`.
This file is updated after each section lands; a row moves only when its tests pass.
No domain expert has read this against the source.
An independent test author has since written 966 assertions from the regulation text alone; see "The independent test pass".
That author was an AI, a separate Claude agent, and not a person.
The open questions are recorded in `registers/fork-register.json`, which holds 18 entries, all open; recorded in this file and in `independent-readings-b.md`, and not entered in the register: R6 (nothing turns on it in an assessment, as the paragraph on 223.16(c) and 223.15 says), R11 (slice A's switch passed through), IA1 to IA14, and the paragraphs of this file on the principal amount of a revolving credit facility, collateral and a partial exemption, what the assessment takes from the caller, the dates in 223.42(n) and (o), and the conventions of the encoding.

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
| 223.41, 223.42, 223.16(c) effects | which requirements each exemption leaves in force | done |
| the top-level assessment | one proposed transaction: covered, what counts toward the limits, both limits, collateral, safety and soundness, low-quality assets, and whether it may be entered into | done (30 end-to-end tests) |
| 223.21(b), 223.22(b)(2), 223.23(b)(2) | timing, and the sequence rule | out of scope: sequences are a separate phase |
| 223.31 to 223.33, 223.43, 223.51 to 223.56, 223.61, 223.71, 223.72 | acquisitions, financial subsidiaries, derivatives, section 23B, other | out of scope |

## Forks and open questions

**223.15(b)(3) "by more than 5 percent" (a switch, default: five percentage points; assumed, not ruled).**
223.15(b)(3): "The participating member bank's share of the renewal or extension of additional credit does not exceed its proportional share of the original transaction by more than 5 percent, unless the member bank obtains the prior written approval of its appropriate Federal banking agency".
It can mean five percentage points of the transaction above the proportional share, or five percent more than the proportional share itself.
With a proportional share of 25 percent the first allows a share up to 30 and the second up to 26.25; the tests assert both readings at 29 and at 26.25 and 26.3.

**223.12 and a financial subsidiary (the words as printed).**
223.11 says "(other than a financial subsidiary of the member bank)" and 223.12 has no such words: "any affiliate", "all affiliates".
223.2(a)(8) makes a financial subsidiary an affiliate, so the encoding counts a loan to one toward the 20 percent limit and not toward the 10 percent limit; a test asserts both.

**Do exempt transactions count toward the aggregate amount? (assumed, not ruled).**
223.3(a) defines the aggregate amount as the transaction about to be engaged in added to "the current amount of all outstanding covered transactions", and 223.41 and 223.42 say exempt transactions are "not subject to the quantitative limits".
The text does not say whether an exempt transaction is itself counted among the outstanding covered transactions.
The 223.42(c) example does: it values the covered transaction at the unsecured $50 of a $100 loan, so the exempt part is not counted.
The encoding follows that: the outstanding amounts are stated by the caller, and the part of a transaction an exemption removes (`value exempt`) does not count toward the limits or the collateral requirement.

**223.16(c) and 223.15 (assumed, not ruled).**
223.41 says its transactions are "subject to ... the prohibition on the purchase of a low-quality asset of § 223.15" and 223.42 says they are "not subject to" it; 223.16(c) says neither.
Every transaction it describes is an extension of credit to a nonaffiliate, to which 223.15 (a purchase of an asset from an affiliate) does not apply, so the encoding leaves 223.15 in force for it and nothing turns on that.

**A transaction that meets a 223.41 exemption and a 223.42 exemption (open; not ruled).**
223.41(c) exempts the purchase of a loan on a nonrecourse basis from an affiliated depository institution, and 223.42(k) exempts the purchase of an extension of credit from an affiliate on a nonrecourse basis, on conditions, so one purchase can satisfy both.
223.41 leaves the transaction "subject to" the low-quality asset prohibition of 223.15, and 223.42 says it is "not subject to" it, so the two lead-ins give opposite instructions for a purchase in both lists.
The text does not say whether the exemptions are cumulative (the stricter lead-in wins) or whether the more favourable one applies.
The encoding takes the exemption family as one stated input (`Exemption claimed`), so the caller names the family, and there is no default for a purchase that fits both.

**A transaction that is exempt in part (assumed, not ruled).**
223.42(c) exempts an extension of credit "to the extent that the transaction is and remains secured by" the listed collateral, so a loan of 100 with Treasuries of 50 has 50 that is not exempt.
The part an exemption does not remove is not exempt, so the limits and the collateral requirements apply to it in full, whichever exemption removed the rest.
The assessment therefore tests the limits and the collateral requirement for the remainder (the amount that counts toward the limits) without asking which exemption family was claimed; the family decides only what the exempt part still owes (`requirement still applies`).
An earlier version switched the limits and the collateral requirement off for the whole transaction as soon as a 223.42 exemption was claimed, while still reporting the remainder as the amount that counts (see "The independent test pass", D2).

**223.14(f)(2): the unused portion (a reading of the words, not ruled).**
The exception speaks of "the unused portion of an extension of credit", and 223.3(i) lists an extension of credit and a guarantee, acceptance or letter of credit as different credit transactions, so the exception is taken to reach an extension of credit only.
An earlier version applied it to every credit transaction (see D1).

**223.14(b)(1) and (c)(4): an intangible asset the Board has approved (assumed, not ruled).**
223.14(c)(4) makes an intangible asset eligible collateral "if specifically approved by the Board", and 223.14(b)(1) gives no percentage for it.
It is taken as "other real or personal property" under (iv), 130 percent.
An earlier version gave it no percentage, so that dividing its value by the percentage raised a division by zero (see D4).

**Collateral and a partial exemption (convention).**
When 223.42(c) exempts part of a loan, the collateral that supports the exempt part is not listed among the collateral for the rest, so that no collateral is counted twice; the printed example is tested that way.

**What the assessment takes from the caller.**
The assessment takes a transaction at one instant with its value already worked out under 223.21 to 223.24 (`regwb-valuation.l4`), and the part of it an exemption removes; it does not choose among the exemptions or test their conditions, which are the predicates in `regwb-exemptions-41.l4` and `regwb-exemptions-42.l4`.
For a transaction with a nonaffiliate whose proceeds go to an affiliate, the caller states the amount 223.16 treats as a transaction with the affiliate, as the value, and the affiliate it benefits.

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

**223.24(b): a negative value (assumed, not ruled).**
The text says the value is the lesser of "(1) The total value of the extension of credit less the fair market value of the nonaffiliate collateral" and the affiliate securities' fair market value if verified.
If the nonaffiliate collateral is worth more than the extension of credit, the first figure is negative, and the text does not say what then.
The encoding stops the value at zero, as it does for 223.22(a)(1), because a covered transaction cannot be worth less than nothing and a negative value would reduce the aggregate amount of covered transactions.
An earlier version followed the words and returned the negative figure; the independent test author found that result implausible, and it was changed (see "The independent test pass", D3).

**223.22(a)(1): a reduction larger than the initial value.**
The text lets the value after the purchase "be reduced to reflect amortization or depreciation of the asset, to the extent that such reductions are consistent with GAAP".
A reduction cannot take the value below zero, so the encoding stops at zero (assumed).

**223.21(a)(4)(ii): the "principal amount" of a revolving credit facility.**
The text does not say whether it is the amount drawn or the amount of the facility.
It does not matter for the printed example, because the sum under (a)(1)(iii) gives $300 on either reading, and the tests state the principal as the amount drawn.

## The independent test pass

The independent author was a fresh reader who started with only the text of 223.3, 223.11 to 223.16, 223.21 to 223.24 and 223.41 to 223.42, the slice A modules (the definition of affiliate, which it was told not to test) and an interface for this encoding: every type, every function signature and every `@ref`, with each body answering FALSE, 0 or the first constructor of its result type, and every comment removed.
It wrote 966 assertions into `regwb-independent-tests.l4` (68 end-to-end scenarios of the assessment) and listed the 11 points where it found the text open in `independent-readings-b.md` (R1 to R11), with the assertions that depend on each in the file's last section.
516 of the 966 fail against the interface, so they can fail a real encoding; the 450 that pass are the cases that expect FALSE, 0 or a first constructor, and the readings file lists them by line.
No expectation was edited after the author wrote it.
Run against this encoding as it stood, 958 assertions passed, 5 failed and 3 could not be evaluated.
Each disagreement was settled from the text, and every fix was made in the encoding:

| id | assertion (test file line) | what the encoding did | who was right, and why |
| --- | --- | --- | --- |
| D1 | 471: the unused-portion exception for a guarantee | applied (f)(2) to a guarantee, so a guarantee of 300 with 200 unused needed 100 of collateral | the author: (f)(2) says "an extension of credit", and 223.3(i) separates that from a guarantee, acceptance or letter of credit |
| D2 | 1515, 1516: scenario 67, a loan of 100 under 223.42(c) with Treasuries of 50 and capital stock and surplus 499 | reported 50 as the amount that counts and did not apply the limit to it, so 50 against 10 percent of 499 (49.9) was not a breach | the author: the part not exempt is not exempt; the encoding was inconsistent with itself, counting a remainder and then not testing it (R7) |
| D3 | 1527: R9, 223.24(b) with nonaffiliate collateral above the credit | returned -50 | the author, as a reading: the words are silent and a negative covered transaction is not plausible (R9) |
| D4 | 1529 and 1530 to 1532: R10, an intangible asset the Board has approved | gave it percentage 0, so the amount it secures divided by zero | the author's reading A, 130 percent, because (iv) is the residual class and the encoding cannot give a percentage of 0 to eligible collateral (R10) |

The other R-entries were already answered the way the author took them, and the file asserts them: R1 the affiliate is the `affiliate concerned`; R2 both constructors of the 223.15(b)(3) switch; R3 over-encumbered collateral adds 0; R4 an unperfected interest is eligible and worth 0; R5 the exempt part under 223.42(c) is net of a senior lien; R6 223.15 still applies to a 223.16(c) transaction; R8 the amount that counts is the transaction's own, less the exempt value; R11 the readings reach the affiliate lookup.
The author's own interface assumptions (IA1 to IA14: percentages written as 10, share units, the meaning of a few fields) are in its readings file; none of them failed against this encoding.
What the author could not test, because the interface has no function for it: 223.14(e), the timing rules of 223.21(b), 223.22(b) and 223.23(b), and the twelve-month arithmetic of 223.16(c)(4)(iii).
A single author wrote the expectations and the readings, so the file shows consistency with the words, not that the readings are right.

## Copied modules

The three modules below are copied byte for byte from `../affiliates-2026-11/` (the stable `l4` resolves `IMPORT` only within the importing file's folder), at the commit that deposited them; they are not edited here.
A fix is made in `../affiliates-2026-11/` first and the copy is refreshed.

| module | sha256 |
| --- | --- |
| `regw-nouns.l4` | `950ff5c950fcebb70fa747a26df7d54b4501c0945d1a24e55ee7c99abc6e45f9` |
| `regw-control.l4` | `047bf0b15eb71cff16da800a9f56d306530ffb579a6e15a55c7926d9659b76da` |
| `regw-affiliate.l4` | `6e092d9ffe47ac05fd01d8e6cf976e4e8026152857abca97aa62098a4a629ecd` |
