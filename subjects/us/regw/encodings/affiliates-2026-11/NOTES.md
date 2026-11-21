# Regulation W (12 CFR Part 223) — the affiliate definition

Status, 2026-11-21: **every in-scope row is encoded, and its tests pass (664 assertions: 123 written with the encoding, 541 independently).**
The rows marked `out of scope` are not encoded, and neither is anything else in Part 223.
No domain expert has read this against the source.
An independent test author wrote 541 of the assertions from the source before reading the encoding (the encoding skill's step 8); see "The independent test pass".
This file is updated after each section lands; a row moves only when its tests pass.

## Scope

This encoding covers the definition of "affiliate" in 12 CFR 223.2(a)–(c), and the definitions it rests on in 12 CFR 223.3: company, person, subsidiary and control.
It does not cover investment-fund affiliates (223.2(a)(6)), merchant-banking affiliates (223.2(a)(9)), covered transactions, the quantitative limits, valuation, the exemptions or the sequence provisions.
The source is the Part 223 slice of the annual CFR edition revised as of 2025-01-01, deposited under `../../source/` with its hashes.

## Target and checks

Target compiler: `main`.
The modules were run and checked with `1.6.112 (main, e4f4bf3, 2026-11-18)`, the newest main build available locally, and `check.sh` compared it with a second compiler, a `dev` build from a working tree of the language's repository (`l4 --version` prints `dev`, which does not say which line it was built from).
The counts were the same on both.
No run of the modules has been made with an `unstable` prerelease from the shelf.
No module produces a warning on 1.6.112.

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
| 223.3(g)(1)(ii) | control: electing a majority of directors (a stated input, counted through subsidiaries) | done |
| 223.3(g)(1)(iii) | control: a Board determination (a stated input) | done |
| 223.3(g)(3) | control: attribution through subsidiaries, and their subsidiaries, whatever the link that makes them subsidiaries | done |
| 223.3(g)(2) | control: fiduciary holdings | done; the exception "as provided in paragraph (a)(3)" is encoded for a shareholder who controls the bank, and not for the "for the benefit of" limb (see forks) |
| 223.3(g)(4) | control: convertible instruments | done (the showing is a stated input) |
| 223.3(g)(5) | control: nonvoting equity | done (the showing is a stated input) |
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
The heading is "Subsidiaries of affiliates", but the words are not "of an affiliate": a company that is an affiliate only through (a)(11), or only through (a)(12), is not described in (1) through (10), and a company the exclusions in (b) take out is still described.
The default reading takes the words as they stand.
The other reading takes the heading: a subsidiary of any affiliate found, after the exclusions, so that the prong chains; it replaces the literal reading and does not add to it.
The two differ in both directions.
A subsidiary of a company determined under (a)(12) is an affiliate only on the chaining reading, and so is a company that a Board determination, which is passed up to nobody, makes a subsidiary of an (a)(11) affiliate.
A subsidiary of a company that (b)(2) excludes (a company that holds only the bank's premises and is sponsored by the bank) is an affiliate only on the literal reading.
Where the link is securities or directors the control test already carries it up (223.3(g)(3) and (g)(1)(ii)), so the two readings agree.
Each case is asserted on both readings.

**(a)(3) and (b)(1)(iii)(B): one shareholder at a time.**
223.2(a)(3) says "shareholders who ... control", and (b)(1)(iii)(B) says "a shareholder ... or a group of shareholders that together control".
Whether (a)(3) aggregates a group is not stated, and the contrast with (b)(1)(iii)(B), which says so, can be read either way.
The encoding takes one shareholder in both places and does not aggregate groups.

**(a)(2) takes a company as the controller; (a)(3) takes any shareholder.**
The words are "controlled by a company that controls the member bank" in (a)(2) and "shareholders" in (a)(3), so an individual who controls the bank is a shareholder for (a)(3) only, and is not a company described in (a)(1) through (10) for (a)(11).

**(g)(4) and (g)(5): one list of showings, and equity figures given per holding.**
223.3(g)(4) and (g)(5) each end "unless the company or shareholder presents information to the Board that demonstrates, to the Board's satisfaction, ...".
The encoding takes the outcome of the showing as a stated input, one pair (company, other company) in `showings`: for a convertible instrument it removes that holder's convertible holdings of that issuer from the count, and for nonvoting equity it removes the (g)(5) route to control of that company.
A showing never removes control by 25 percent of a voting class under (g)(1)(i), which is asserted.
The pair names the holder in (g)(4) and the controller in (g)(5), so a showing by a parent about securities its subsidiary holds is not distinguished from one by the subsidiary.
The percentage a convertible instrument would convert into, and the holder's percentage of equity capital, are inputs on each holding; "equity capital" (223.3(n)) is not computed.
In the test fixtures that state only a voting percentage, the equity figure is 0.

**The affiliate definition has two fixed points as well (open question; the least is taken).**
P holds 100 percent of Bank; Bank holds 30 percent of S1 and of S2; S1 and S2 each hold 25 percent of the other.
Each of S1 and S2 is controlled by P through Bank, so (a)(2) describes it, and each is a subsidiary of Bank, so (b)(1) excludes it unless it is "directly controlled by ... affiliates (other than depository institution affiliates)".
The other of the two is such an affiliate if it is one: with only P found, neither is an affiliate; with P, S1 and S2 found, each is, and the set holds.
The encoding takes the least, P alone, and `regw-affiliate-tests.l4` asserts both halves.
Under the other reading a cross-holding between two bank subsidiaries would lift the exclusion from both.

**There is no seat layer.**
The commons guide asks for a seat layer with plain inputs, one per fact the person can state; this encoding takes an ownership graph (holdings, offices, links), which is not a list of plain facts, so no `@export` or `@desc` is written and a seat layer would have to be built over a fixed shape of structure.
The seat is recorded in `encoding.json`.

**What is stated, not computed.**
A Board determination under 223.3(g)(1)(iii), the election of a majority of directors under (g)(1)(ii), a determination under 223.2(a)(12), whether a company is a depository institution or a financial subsidiary, what it engages in solely, whether (b)(5)'s authorized period is still running, and the purpose (section 23A or subpart F) are inputs.

**(g)(3) applied to an individual controller (assumed, not ruled).**
(g)(3) opens "A company controls securities...", and an individual is not a company; (g)(1)(i) says "directly or indirectly, or acting through one or more other persons".
The encoding attributes a subsidiary's holdings to any controller, company or individual, reading (g)(1)(i) as the licence.

**(g)(2) fiduciary shares.**
223.3(g)(2): "no company will be deemed to control another company by virtue of its ownership or control of shares in a fiduciary capacity, except as provided in paragraph (a)(3) of § 223.2 or if the company owning or controlling the shares is a business trust."
The bar is on a company: fiduciary shares held by an individual or by a trust that is not a business trust (not a "company" under 223.3(f)) still count towards control.
That is the reading of the words; the other reading, that no holder's fiduciary shares count, would need "no person".
The exception "as provided in paragraph (a)(3)" is encoded for the limb that needs no beneficiary: for 223.2(a)(3), a shareholder that controls the member bank controls Co through shares it holds as a fiduciary too ("by trust or otherwise"); its control of the member bank itself is judged without them.
The limb "for the benefit of shareholders", which turns on who the beneficiaries are, is not encoded.

**(g)(1)(ii) through a subsidiary.**
223.3(g)(1)(ii): "controls in any manner the election of a majority of the directors".
An election link from a company's subsidiary, or from a subsidiary of that subsidiary, counts for the company, as (g)(3) counts the securities they hold.
A Board determination under (g)(1)(iii) is about the pair it names and is not passed up.

**What "voting securities" and "percent of a class" are.**
223.3(jj) takes "voting securities" from 12 CFR 225.2, which is not deposited.
The encoding takes holdings as given per voting class with a percentage; it does not decide which instruments are voting securities, nor "power to vote" held other than by owning shares.

**"Directors" in (g)(1)(ii) and a Board determination in (g)(1)(iii)** are stated inputs, per pair: the encoding does not decide whether a majority of directors is elected.

## What `check.sh` prints (2026-11-21, build 1.6.112)

```
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
regw-affiliate-tests.l4                        0        64       0        0         0 |      0        64       0        0  same
regw-affiliate.l4                              0         0       0        0         0 |      0         0       0        0  same
regw-control-tests.l4                          0        59       0        0         0 |      0        59       0        0  same
regw-control.l4                                0         0       0        0         0 |      0         0       0        0  same
regw-independent-tests.l4                      0       541       0        0         0 |      0       541       0        0  same
regw-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
```

Three assertions failed across the first runs, and each failure was a defect in a rule, not in the expected value.
On main, `NOT (x)` binds looser than `OR` and `AND`, so `NOT (x) OR y` and `a AND NOT (x) AND b` read as `NOT ((x) OR y)` and `a AND NOT ((x) AND b)`.
That wrongly dropped a business trust's fiduciary holding, and it made every affiliate that is not a depository institution count as a direct controller in (b)(1)(iii)(A), whether or not it controlled the company directly.
Every `NOT` that precedes another operand is now bracketed as `(NOT (x))`.
A later review found that attribution under (g)(3) stopped at a controller's direct subsidiaries; it now follows every chain of control links, and the test that exposed it (A controls S1, S1 controls S2 only through its directors, S2 holds 25 percent of T) fails against the earlier rule.

## The independent test pass

The independent author, a reader who started with only the text of 223.2 and 223.3, the nouns module and an interface whose function bodies answered FALSE, wrote 541 assertions into `regw-independent-tests.l4` and listed the points where it found the text open in `independent-readings.md` (R1 to R16).
It did not read the encoding or its tests, and no expectation in the file has been changed since it was written: the header says so, and the edits it made after its first run were syntax fixes and corrections from the text.
Run against the encoding for the first time, 532 passed and 9 failed.
Each of the nine was settled from the text; none was a misreading by the author, and four rule defects were fixed, each with tests of its own:

1. **The chaining switch for (a)(11) was a union, not the reading its name states** (three failures).
   The constructor reads "a subsidiary of any affiliate, so that the prong chains", and the code counted a subsidiary of a described company as well.
   It now takes a subsidiary of an affiliate found so far, after the exclusions, as the author expected; see the (a)(11) fork above.
2. **(g)(1)(ii) was not passed up through subsidiaries** (two failures).
   "controls in any manner the election of a majority of the directors" includes control through a subsidiary; the encoding only counted an election link from the controller itself.
3. **(g)(2) barred every holder, not only a company** (two failures).
   The text says "no company"; see the fork above.
4. **The exception "as provided in paragraph (a)(3)" was not encoded at all** (two failures).
   The author's readings R14 and R16 put a controlling shareholder who holds as a fiduciary into (a)(3); see the fork above.

The encoding's own test for (a)(11) had used an election link as its discriminating fixture, which defect 2 made agree on both readings; it now uses a Board determination and the (a)(12) and (b)(2) cases, with expectations rewritten from the text.
Of the author's other readings, R1 to R4 are the encoding's defaults (self-affiliation off, one board at a time, own holdings for "directly", literal (a)(11)); R5, R6, R8 to R13 and R15 agree with it; the file asserts both constructors for each of R1 to R4.
The points the author lists as not expressible in the inputs (beneficiaries, groups of shareholders, power to vote other than by owning shares, (a)(6), (a)(9), the period in (b)(5)) are the encoding's own stated limits.
Its interface questions have these answers: there is one list of showings for both (g)(4) and (g)(5); `control step` and `affiliate step` read the lists they are given and do not derive them; `current` in `affiliate step` is the set of names already found, and the chaining reading of (a)(11) reads it.

## Open questions for a lawyer

1. Control on cross-holdings has two fixed points; is the least the meaning (above)?
2. "directly controlled" in (b)(1)(iii): own holdings only, or attribution included (above)?
3. (a)(4): one board at a time, or the offices pooled (above)?
4. (a)(11): does the prong chain through its own subsidiaries (above)?
5. Does (a)(3) aggregate a group of shareholders (above)?
6. Is the member bank its own affiliate on the literal words (above)?
7. Does the affiliate definition have two fixed points on cross-holdings, and is the least the meaning (above)?
8. Is the bar in (g)(2) on companies only, as written, or on every holder (above)?
9. Is control through a subsidiary's election of directors attributed up under (g)(1)(ii) (above)?
