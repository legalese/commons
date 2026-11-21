# Regulation W (12 CFR Part 223) — the affiliate definition

Status, 2026-11-21: **partial.** The rows marked `done` below are encoded and their tests pass; the rest are `not started`.
This file is updated after each section lands; a row moves only when its tests pass.

## Scope

This encoding covers the definition of "affiliate" in 12 CFR 223.2(a)–(c), and the definitions it rests on in 12 CFR 223.3: company, person, subsidiary and control.
It does not cover investment-fund affiliates (223.2(a)(6)), merchant-banking affiliates (223.2(a)(9)), covered transactions, the quantitative limits, valuation, the exemptions or the sequence provisions.
The source is the Part 223 slice of the annual CFR edition revised as of 2025-01-01, deposited under `../../source/` with its hashes.

## Target and checks

Target compiler: `main`.
The modules were run and checked with `1.6.112 (main, e4f4bf3, 2026-11-18)`, the newest main build available locally; `check.sh` compared that build with itself, so it says only that the modules read on main and does not test them against an `unstable` build.

## Seat

The seat is the member bank to which the regulation is applied (a company, not an official): "Is this company my affiliate?"
No seat is written for the Board of Governors, which is the regulator.

## Coverage table

Dispositions: `done` (encoded and tested), `WIP` (encoded, not yet passing), `not started`.

| provision | what it says, in short | disposition |
| --- | --- | --- |
| 223.3(f) company | the nouns: what counts as a company | done |
| 223.3(bb) person | the nouns: what counts as a person | done |
| 223.3(ii) subsidiary | a company controlled by another | done |
| 223.3(g)(1)(i) | control: 25 percent of any class of voting securities | done |
| 223.3(g)(1)(ii) | control: electing a majority of directors (a stated input) | done |
| 223.3(g)(1)(iii) | control: a Board determination (a stated input) | done |
| 223.3(g)(3) | control: attribution through subsidiaries | done |
| 223.3(g)(2) | control: fiduciary holdings | done, except the (a)(3) exception (see forks) |
| 223.3(g)(4) | control: convertible instruments | not started |
| 223.3(g)(5) | control: nonvoting equity | not started |
| 223.2(a)(1)–(5) | affiliate prongs: parent, common control, interlocking directorates, sponsored and advised | not started |
| 223.2(a)(7), (8) | affiliate prongs: depository institution subsidiary, financial subsidiary | not started |
| 223.2(a)(10), (11) | affiliate prongs: partnerships, subsidiaries of affiliates | not started |
| 223.2(a)(12) | affiliate prong: a Board or agency determination (a stated input) | not started |
| 223.2(b)(1)–(5) | exclusions | not started |
| 223.2(c) | subpart F: depository institutions are not affiliates | not started |
| 223.2(a)(6), (a)(9) | investment funds; merchant banking and its own exemptions (a)(9)(ii)-(v) | out of scope: each takes a percentage over the set of affiliates |
| everything outside 223.2 and the control definitions of 223.3 | covered transactions, limits, valuation, exemptions, sequences | out of scope |

## Forks and open questions

**Cross-holdings: control has two fixed points (open question).**
223.3(g)(3): "A company controls securities, assets, or other ownership interests owned or controlled, directly or indirectly, by any subsidiary"; 223.3(ii): "a company that is controlled by the specified company".
Control is defined through control.
Take A holding 15 percent of B and of C, and B and C each holding 15 percent of the other.
If A controls neither, it holds 15 percent of each and the test is not met; if A controls both, it controls their holdings and so holds 15 + 15 = 30 percent of each, and the test is met.
Both states agree with the text.
This encoding takes the least fixed point (A controls neither), and `regw-control-tests.l4` asserts both halves: the step leaves the empty set and the set {A controls B, A controls C} each unchanged, and the result is the empty set.
The text does not say which is meant; it is a question for a lawyer.

**(g)(3) applied to an individual controller (assumed, not ruled).**
(g)(3) opens "A company controls securities...", and an individual is not a company; (g)(1)(i) says "directly or indirectly, or acting through one or more other persons".
The encoding attributes a subsidiary's holdings to any controller, company or individual, reading (g)(1)(i) as the licence.

**(g)(2) fiduciary shares: the exception "as provided in paragraph (a)(3) of § 223.2" is not encoded.**
The business-trust exception is.
The (a)(3) exception turns on shares held "by or for the benefit of" shareholders, which needs beneficiaries as a noun.

**What "voting securities" and "percent of a class" are.**
223.3(jj) takes "voting securities" from 12 CFR 225.2, which is not deposited.
The encoding takes holdings as given per voting class with a percentage; it does not decide which instruments are voting securities, nor "power to vote" held other than by owning shares.

**"Directors" in (g)(1)(ii) and a Board determination in (g)(1)(iii)** are stated inputs, per pair: the encoding does not decide whether a majority of directors is elected.

## What `check.sh` prints (2026-11-21, build 1.6.112)

```
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
regw-control-tests.l4                          0        38       0        0         0 |      0        38       0        0  same
regw-control.l4                                0         0       0        0         0 |      0         0       0        0  same
regw-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
```

One assertion failed on the first run, and the failure was a defect in the rule, not in the expected value: `NOT (x) OR y` reads as `NOT ((x) OR y)` on main, so a fiduciary holding by a business trust was wrongly dropped; the rule now brackets the `NOT`.
