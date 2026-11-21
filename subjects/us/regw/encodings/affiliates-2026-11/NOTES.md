# Regulation W (12 CFR Part 223) — the affiliate definition

Status, 2026-11-21: **partial.** The rows marked `done` below are encoded and their tests pass (85 assertions); the rows marked `not started` are not encoded.
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
| 223.2(a)(1)–(5) | affiliate prongs: parent, common control, interlocking directorates, sponsored and advised | done, with forks on (a)(2) and (a)(4), and (a)(3) for one shareholder only |
| 223.2(a)(7), (8) | affiliate prongs: depository institution subsidiary, financial subsidiary | done |
| 223.2(a)(10), (11) | affiliate prongs: partnerships, subsidiaries of affiliates | done, with a fork on (a)(11) |
| 223.2(a)(12) | affiliate prong: a Board or agency determination (a stated input) | done |
| 223.2(b)(1)–(5) | exclusions | done, with a fork on (b)(1)(iii), and (b)(1)(iii)(B) for one shareholder only; (b)(5)'s period is a stated input |
| 223.2(c) | subpart F: depository institutions are not affiliates | done (the purpose is an input) |
| 223.2(a)(6), (a)(9) | investment funds; merchant banking and its own exemptions (a)(9)(ii)-(v) | out of scope: each takes a percentage over the set of affiliates, so (a)(9)(ii), a showing that modifies only (a)(9)(i), is left out with it |
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

**The member bank is its own affiliate on the literal words (a switch, default: it is not; assumed, not ruled).**
223.3(f): "Company means a corporation ... and, unless specifically excluded, includes a member bank and a depository institution."
223.2(a)(2): "Any company, including any subsidiary of the member bank, that is controlled by a company that controls the member bank."
A member bank that has a parent is a company controlled by a company that controls it, and 223.2(b) does not exclude it, so on the literal words it is its own affiliate.
The `Self-affiliation` reading switches this on; the default reading leaves the member bank out, because the section's purpose is the bank's dealings with others.
With the literal reading and a member bank not flagged as a depository institution, (b)(1)(iii)(A) would count the bank as an affiliate directly controlling its own subsidiaries; flag the member bank as a depository institution.

**"any such office with the member bank or any company that controls the member bank" (a)(4) (a switch, default: one board at a time; assumed, not ruled).**
223.2(a)(4): "a majority of its directors, trustees, or general partners (or individuals exercising similar functions) constitute a majority of the persons holding any such office with the member bank or any company that controls the member bank."
One reading takes the offices of the member bank, or of one controlling company, a board at a time; the other pools the offices of the member bank and of every controlling company.
The test uses the bank's three directors p1, p2, p3, a controlling company's p4, p5, p6, and a company X with directors p1, p2, p4, p5: one board at a time, two of X's four directors sit on each board, which is not a majority of X's board, so X is not an affiliate; pooled, all four are among the six office holders, so it is.
Both halves are asserted.
Both readings count "a majority" as more than half of each group.

**"directly controlled" in (b)(1)(iii)(A) and (B) (a switch, default: the controller's own holdings; assumed, not ruled).**
223.2(b)(1)(iii): "Directly controlled by: (A) One or more affiliates (other than depository institution affiliates) of the member bank; or (B) A shareholder that controls the member bank or a group of shareholders that together control the member bank".
223.3(g) defines "control" and does not define "directly".
Take a member bank with a parent P and a subsidiary Sub, P holding 100 percent of the bank and the bank 100 percent of Sub, and P holding nothing in Sub itself.
If "directly" means control by the controller's own holdings and elections, P does not directly control Sub, so Sub is excluded as a subsidiary of the bank.
If it includes securities attributed from subsidiaries under 223.3(g)(3), P controls Sub through the bank, so Sub is an affiliate.
The second reading would make the exclusion do almost no work for a subsidiary of a bank that has a corporate parent.
Both halves are asserted.

**(a)(11) "a company described in paragraphs (a)(1) through (10)" (a switch, default: literal; assumed, not ruled).**
223.2(a)(11): "Any subsidiary of a company described in paragraphs (a)(1) through (10) of this section".
The prong does not say "of an affiliate", and a company that is an affiliate only through (a)(11) is not described in (1) through (10), so on the literal words the prong does not chain.
The chain still arises through control: a parent controls the securities its subsidiaries hold (223.3(g)(3)), so a subsidiary of a subsidiary held by securities is a subsidiary of the parent too.
What the literal reading drops is a company controlled by an (a)(11) affiliate in a way that is not securities, such as by electing its directors.
The test has F sponsored by the bank, Q held 100 percent by F, and R controlled by Q only through its directors: literal, R is not an affiliate; chaining, it is.
The coordinating brief assumed a chain; this default departs from it, on the words.

**(a)(3) and (b)(1)(iii)(B): one shareholder at a time.**
223.2(a)(3) says "shareholders who ... control", and (b)(1)(iii)(B) says "a shareholder ... or a group of shareholders that together control".
Whether (a)(3) aggregates a group is not stated, and the contrast with (b)(1)(iii)(B), which says so, can be read either way.
The encoding takes one shareholder in both places and does not aggregate groups.

**(a)(2) takes a company as the controller; (a)(3) takes any shareholder.**
The words are "controlled by a company that controls the member bank" in (a)(2) and "shareholders" in (a)(3), so an individual who controls the bank is a shareholder for (a)(3) only, and is not a company described in (a)(1) through (10) for (a)(11).

**What is stated, not computed.**
A Board determination under 223.3(g)(1)(iii), the election of a majority of directors under (g)(1)(ii), a determination under 223.2(a)(12), whether a company is a depository institution or a financial subsidiary, what it engages in solely, whether (b)(5)'s authorized period is still running, and the purpose (section 23A or subpart F) are inputs.

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
regw-affiliate-tests.l4                        0        47       0        0         0 |      0        47       0        0  same
regw-affiliate.l4                              0         0       0        0         0 |      0         0       0        0  same
regw-control-tests.l4                          0        38       0        0         0 |      0        38       0        0  same
regw-control.l4                                0         0       0        0         0 |      0         0       0        0  same
regw-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
```

Three assertions failed across the first runs, and each failure was a defect in a rule, not in the expected value.
On main, `NOT (x)` binds looser than `OR` and `AND`, so `NOT (x) OR y` and `a AND NOT (x) AND b` read as `NOT ((x) OR y)` and `a AND NOT ((x) AND b)`.
That wrongly dropped a business trust's fiduciary holding, and wrongly let a depository institution affiliate count as a direct controller in (b)(1)(iii)(A).
Every `NOT` that precedes another operand is now bracketed as `(NOT (x))`.

## Open questions for a lawyer

1. Control on cross-holdings has two fixed points; is the least the meaning (above)?
2. "directly controlled" in (b)(1)(iii): own holdings only, or attribution included (above)?
3. (a)(4): one board at a time, or the offices pooled (above)?
4. (a)(11): does the prong chain through its own subsidiaries (above)?
5. Does (a)(3) aggregate a group of shareholders (above)?
6. Is the member bank its own affiliate on the literal words (above)?
