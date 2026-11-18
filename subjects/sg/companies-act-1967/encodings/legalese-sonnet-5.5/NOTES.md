# NOTES: Companies Act 1967 (Singapore), wave 1 of a whole-Act encoding with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
**This is wave 1 only.** It encodes the interpretation section and the definitional core, Part 4's share capital, Part 5's directors, Part 6's accounts and audit, Part 7, minority remedies, Part 10A and Part 11; the later waves (listed below) are not encoded.
Written 2026-11-18 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Built with the `l4` 1.6.110 (main, e51181d, 2026-11-11) and compared with 1.6.109 (main, 4c887e0, 2026-11-04); every module has the same four counts on both builds.

## Edition encoded

This encoding is of the **Companies Act 1967, 2020 Revised Edition**, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 6/5/2026 to 20/10/2026" (the line repeated on each page, `../../registers/source-bundle/CoA1967.txt` line 15), **retrieved 2026-10-09** (`../../registers/source-bundle/CoA1967.meta.json`, `retrieved_date`), carrying the amendments up to **Act 24 of 2025** (the text shows tags such as "[Act 24 of 2025 wef 06/05/2026]", line 1499).
The text file has sha256 `ea9501a3e0829a46b396aa6cb5e7369fc8c1f4c2288ede5748cf3e62c6284303`, computed from the file when this folder was assembled.
**A later consolidation may exist and was not read.**
Nothing here was compared with any other version of the Act, or with an amendment made after the consolidation's last tag.
**The encoding is of that text only**: a rule that holds in this file may not hold in a later version, and a reader asking about a date outside 6 May 2026 to 20 October 2026 must check the text for that date before relying on any answer here.

## What this folder covers

The deposited text has 30,828 lines and 186,847 words. Wave 1 encodes 102,252 of those words (54.7%), in 12 agents' ranges.

| agent | text (lines of `CoA1967.txt`) | words | what |
| --- | --- | --- | --- |
| keel | 1 to 2389, 2736 to 2801 | 12,675 | Part 1 (ss 1 to 7A: interpretation, subsidiary, holding company, related corporations, interests in shares, the solvency statement) and s 10 (who may be a company's auditor), the shared core, and the one module that counts every period |
| sga1 | 6135 to 7320, 28514 to 28876 | 9,134 | Part 4, share capital: issue and kinds of shares, alteration, Sixth Schedule |
| sga2 | 7321 to 8311 | 6,547 | Part 4, financial assistance (ss 76, 76A) |
| sga3 | 8312 to 9881 | 9,600 | Part 4, buy-back, treasury shares, reduction of capital (ss 76B to 78K) |
| sgb1 | 11592 to 13354 | 11,196 | Part 5, directors: appointment to duties (ss 145 to 160D) |
| sgb2 | 13355 to 15410 | 12,983 | Part 5, directors: approvals, loans, loss of office, secretary, indemnity (ss 161 to 173I) |
| sgc1 | 17849 to 19068, 28897 to 29012 | 8,475 | Part 6, financial statements (ss 199 to 204, Twelfth Schedule) |
| sgc2 | 19069 to 20182, 29013 to 29310 | 8,580 | Part 6, audit and the audit exemptions (ss 205 to 209B, Thirteenth Schedule) |
| sgd | 20183 to 21697 | 9,161 | Part 7, arrangements, reconstructions, amalgamations, compulsory acquisition (ss 210 to 215K) |
| sgf | 21698 to 21885 | 1,303 | minority remedies (ss 216 to 216B) |
| sge | 23148 to 23607 | 2,391 | Part 10A, transfer of registration into Singapore (ss 355 to 364A) |
| sgg | 23608 to 25371 | 10,207 | Part 11, foreign companies |

**Not encoded in wave 1**, by range of the text:

| lines | words | Parts they fall in |
| --- | --- | --- |
| 2390 to 2735 | 2,555 | Part 2 |
| 2802 to 6134 | 20,287 | Part 2, Part 3 |
| 9882 to 11591 | 11,659 | Part 4, Part 5 |
| 15411 to 17848 | 15,957 | Part 5 |
| 21886 to 23147 | 8,663 | Part 8, Part 8A, Part 9, Part 10 |
| 25372 to 28513 | 18,790 | Part 11A, Part 12 |
| 28877 to 28896 | 38 | front matter, schedules or the index |
| 29311 to 30828 | 6,646 | front matter, schedules or the index |

Those ranges include Part 2 (administration) and Part 3 (constitution of companies), the rest of Part 4 (shares, debentures and charges), the rest of Part 5 (management and administration), Part 8 and Part 8A (which the text shows as repealed by Act 40 of 2018), Part 9 (investigations), Part 10 (dissolution), Part 11A and Part 12, and every Schedule except the Sixth, the Twelfth and the Thirteenth.
Cross-references from an encoded provision into one of them are taken as inputs, named for the fact (see the seams section).

## Winding up

Winding up has moved out of this Act to the Insolvency, Restructuring and Dissolution Act 2018, and that Act is not a source here.
What remains in the deposited text is Part 10, headed "DISSOLUTION" (lines 22627 to 23147): Divisions 1, 2, 3, 5 and 6 and most of Division 4 are "[Repealed by Act 40 of 2018]", and what survives is Division 4, Subdivision (5), the Registrar's power to strike a defunct company off the register, striking off on application, objections, administrative restoration, restoration by mistake, the effect of restoration and the retention of books (ss 344 to 344H, lines 22700 to 23134), with ss 343 and 345 to 349 repealed.
**Part 10 is not encoded in wave 1** (it falls in the range of lines 21886 to 23147 above). Where an encoded provision turns on a winding up (for example the commencement of winding up in s 4(1), or a liquidator's appointment notified under Part 11), the outcome of the winding up under the 2018 Act is taken as an input.

## Part 10A: a transfer of registration in only

Part 10A provides for a foreign corporate entity to transfer its registration to Singapore as a company limited by shares.
**Finding: nothing in ss 355 to 364A or elsewhere in the encoded ranges provides for a transfer of registration out of Singapore.**
The Part 10A agent read the whole Part (lines 23148 to 23607) and searched it for "transfer", "outside Singapore", "deregist" and "domicile" (`notes/sge-NOTES.md`, finding 1).
The lead then searched every encoded range of the text for "transfer of registration", "outside Singapore", "deregist", "domicile" and "discontinu": outside Part 10A the hits are the table of contents, securities exchanges, offerees, contracts, registers and bodies incorporated outside Singapore, and the restoration of a company deregistered by mistake (s 344F, not encoded in wave 1), and none is a transfer of registration out of Singapore.
This is a statement about the encoded ranges only: this encoding has not looked at the rest of the Act, and says nothing about whether any other provision or Act provides an outward route. No provision is invented for one.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`sg-core.l4`, the keel modules and their tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
11 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `sga1` (lines 6135 to 7320, 28514 to 28876), `sga2` (lines 7321 to 8311), `sga3` (lines 8312 to 9881), `sgb1` (lines 11592 to 13354), `sgb2` (lines 13355 to 15410), `sgc1` (lines 17849 to 19068, 28897 to 29012), `sgc2` (lines 19069 to 20182, 29013 to 29310), `sgd` (lines 20183 to 21697), `sgf` (lines 21698 to 21885), `sge` (lines 23148 to 23607), `sgg` (lines 23608 to 25371).
The lead verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the NOT-precedence sweep, the keel's files identical to the keel's, every trace read against its `-- EXPECT` word) and then merged them with a script; the part modules are copied unchanged except as the merge decisions below say, and the merge edited no rule.
An independent test pass has been run on this wave (the readers' files are `notes/reader-*.md`, described in `notes/reader-README.md`); no seat audit has. The tests in this folder are the agents' own, written from the text; the readers' own test modules are not shipped.
Every note a part wrote is kept, with names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
Briefs are shipped verbatim except for lines about tooling.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each agent wrote its own seat questions and cases. The lead concatenated them, in part order, into `sg-seat.l4` and `sg-cases-seat.l4`, with one banner comment per agent; the text under each banner is the agent's, unchanged. The merged seat module imports every part module and checks clean.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section. The merge does not wire one part's output into another's input, so the seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** They are gathered in `NEEDS-CORE.md` (proposed, not landed); the core is the keel's, unchanged.
- **Part-local types and helper names stay where they are.** Every top-level name carries the label of its provision, so no two modules define the same name; the merged seat module imports all part modules at once and compiles.
- **Eleven trace comments were reworded in place** (`sgb2-tests-s161.l4` lines 17, 21, 25; `sgb2-tests-s162.l4` lines 110, 114, 118, 122; `sgb2-tests-s163.l4` lines 167, 171, 175, 179): the agent had written the expected word at the end of the comment ("... EXPECT BREACH"), and the line now begins `-- EXPECT <word>.`, so the checker that reads the word at the start of the line sees it. No line was added or removed, and no expected word was changed.
- **Two traces a strict checker misreads, and are not defects.** `sgd-tests-acquisition.l4` line 384 and `sgd-tests-compromise.l4` line 400 print `FULFILLED AND PARTY ... MUST ...` (the first limb done, the second still owed), which is a residual duty and what their `-- EXPECT RESIDUAL` says; a checker that reads only a result beginning `PARTY` as residual calls them `OTHER`.
- **The merge lost nothing:** the merged folder was gated as it stands: 173 modules, 10,470 assertions satisfied (below); after the three changes made since, 10,476 (see "What check.sh prints").

## Where things are

| agent | modules (layer 1) | assertions in its test modules | `#TRACE` blocks | seat questions | coverage rows (encoded / fork / inert / repealed) |
| --- | --- | --- | --- | --- | --- |
| keel | 8 | 799 | 12 | 37 | 235 (169 / 39 / 23 / 4) |
| sga1 | 7 | 687 | 44 | 72 | 299 (227 / 35 / 30 / 7) |
| sga2 | 7 | 492 | 19 | 106 | 199 (61 / 136 / 2 / 0) |
| sga3 | 7 | 679 | 46 | 74 | 385 (71 / 284 / 27 / 3) |
| sgb1 | 7 | 651 | 47 | 197 | 319 (207 / 75 / 29 / 8) |
| sgb2 | 11 | 798 | 106 | 84 | 403 (267 / 101 / 26 / 9) |
| sgc1 | 11 | 558 | 54 | 144 | 223 (126 / 68 / 22 / 7) |
| sgc2 | 7 | 742 | 70 | 66 | 302 (100 / 178 / 19 / 5) |
| sgd | 4 | 664 | 95 | 150 | 295 (158 / 112 / 19 / 6) |
| sgf | 3 | 181 | 11 | 39 | 42 (8 / 31 / 3 / 0) |
| sge | 8 | 307 | 36 | 68 | 86 (49 / 32 / 5 / 0) |
| sgg | 7 | 656 | 79 | 177 | 329 (222 / 68 / 29 / 10) |
| seat cases, all agents | | 3,262 (`sg-cases-seat.l4`) | | | |

The seat layer is `sg-seat.l4` (1,214 `@export` questions in all) and `sg-cases-seat.l4`; every other module is layer 1, with a tests module beside it.
**The coverage columns are each agent's own count of its own table and are not comparable across agents as a measure of how contestable the text is.** In particular `sga3` marks a row `fork` whenever the rule that encodes it carries at least one entry in its fork register (its coverage section says so), which is why 284 of its 385 rows are `fork`; read each agent's own coverage section for what it counts as `fork`.

## The source

The text is `../../registers/source-bundle/CoA1967.txt` (30,828 lines, sha256 `ea9501a3e0829a46b396aa6cb5e7369fc8c1f4c2288ede5748cf3e62c6284303`), the Singapore Statutes Online informal consolidation turned from a PDF into plain text; its terms, its attribution wording and its unofficial status are in `../../SOURCE-LICENSE.md`.
Page furniture ("Informal Consolidation - version in force from 6/5/2026 to 20/10/2026", "2020 Ed. Companies Act 1967 <page>") and the bracketed amendment marks (for example "[36/2014]") are not text of a provision. The table of contents in lines 1 to 972 is unreliable, so every section number was read from the body (line 973 on).

## The seat

From the keel's notes:

**The seat.** An individual who is, or is about to become, a director, the company secretary or a member (shareholder) of a company incorporated under the Act, or of a foreign company registered under it, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership. There is never a seat for the Registrar, the Minister, the Authority or the Court.)

## Seams between parts

A part cannot import another part, so the part that depends on another's answer takes it as an input named for the fact. The keel's plan lists every seam, with the input's name and type and whether the keel read the citing lines or only saw them in the cross-reference list: `notes/keel-PLAN.md`, section 4 (table A: the keel asks and a part answers; table B: a part asks and the keel answers; C: cross-reference hits that are not seams; D: the one seam the keel could not close, s 5(3)(b)(ii)).
**One seam the plan lacks, found by `sga3`:** the keel's `sg-interests` asks, as a plain `BOOLEAN`, the fact that an interest is a company's interest in its own shares bought in accordance with ss 76B to 76G. `sga3`'s own function for that answered a `MAYBE BOOLEAN` (`JUST TRUE`, or `NOTHING` when a condition fails, fork F-B11 in `notes/sga3-NOTES.md`), and the merge did not wire it, because carrying a `NOTHING` into a `BOOLEAN` as `FALSE` would turn "not covered" into "no".
After the independent review that function answers `JUST FALSE` when a condition fails, and a second function turns its answer into the `BOOLEAN` (see "Changes made after the independent review" below). **The seam is still not wired in the tree:** no module calls the second function, because the keel cannot import a later part, and the seat asks the field as a question of its own; the three other consumers of the same fact (`s 76(9)(c)`, `s 76H(1)` and `s 78A`) take their own inputs.

## Independent readers

Three reader groups wrote tests from the text alone and ran them against this encoding: 1,969 assertions, 1,884 satisfied, 85 failed, 0 refused, and 122 triage lines (`ENCODER` 2, `SCENARIO` 38, `AMBIGUOUS` 46, `GAP` 36).
Their files, and what is not shipped with them, are in `notes/reader-README.md`.
**Read the failures as findings, not defects left open:** of the 122 triage lines, 84 are `SCENARIO` (the reader's expectation was wrong) or `AMBIGUOUS` (the text and the Guide read both ways).
The two `ENCODER` lines: `s 205B(5)` (changed, below) and `s 149A(3)` (the defence "proves (a) and (b)": the reader reads `JUST FALSE` when only (a) is proved, the encoding answers `NOTHING`; not changed, it turns on the same ruling as the split sites).
The `GAP` lines name rows with no function or no input: repealed rows, duties stated only as deontics, missing penalty functions, `s 201B(2)(b)` (the kind of relative), `s 171(2)`, `s 202(4)` (the hearing duty), `s 145` (citizenship), `s 164` (a secretary's register), `s 76E(3)`, `s 76D(2A)`, `s 78B(5)`, `s 78J`, the Sixth Schedule years count, `s 10(1)` and `(3)` ("is it prohibited"), `s 64(2)` and `s 71(1A)`; they are not repaired.

## Changes made after the independent review (assumed, not ruled)

Each item below is its own commit, so each can be reverted alone.
None is a ruling by the maintainer; the answer taken is the one the text's own words support under any outcome of the open split-site question below.

- **`s 78 the company may pay interest on the paid-up share capital and charge it to capital as part of the cost`** (`sga3-77-78.l4`).
  When the shares were issued for the purpose the section names and a limit the text closes in its own words is not met, the function now answers `JUST FALSE`; it answered `NOTHING`.
  The three limits are "(a) no such payment may be made unless it is authorised ... and is approved by the Court", "(c) the payment is to be made only for such period as is determined by the Court" and "(d) the rate of interest must in no case exceed 5% per annum", and the grant rule of 2026-11-12 keeps `JUST FALSE` where the text closes the gate itself.
  For shares not issued for that purpose the function still answers `NOTHING`: the section describes the shares it is about and does not say interest may not be paid on others.
  Five assertions in `sga3-tests-77-78.l4` and one in `sg-cases-seat.l4` changed from `NOTHING` to `JUST FALSE` with it.
  The fork register entry is F-S4 in `notes/sga3-NOTES.md`.
- **`s 205B(5) the company remains exempt in relation to the accounts for the financial year`** (`sgc2-s205a-exemption.l4`).
  The function took one input, whether the company was dormant throughout the year, and answered `NOTHING` when it was not, so it could not give the answer the text gives for a year in which the company ceased to be dormant: "it thereupon ceases to be so exempt; but it remains so exempt in relation to accounts for the financial year in which it was dormant throughout".
  It now takes a second input, `the company ceased to be dormant during the financial year`, and answers `JUST FALSE` for such a year, `JUST TRUE` for a year of dormancy throughout, and `NOTHING` for a year that is neither.
  `sgc2-tests-s205a.l4` has three assertions in place of two; the function is not asked by any seat question.
  An independent reader triaged this as an encoder gap.
- **`s 76B(1) the interest is a company's interest in its own shares purchased or otherwise acquired in accordance with sections 76B to 76G`** (`sga3-76b.l4`), the seam to `s 7(9)(ca)`.
  The function answered `JUST TRUE` when its four inputs held and `NOTHING` otherwise, so a real no, such as the 20% cap exceeded, reached the keel as "not covered".
  It now answers `JUST FALSE` when one of the four fails, because (ca) is introduced by "if" and the sections say what a failure is: s 76B(3) "must not exceed 20% ... unless", s 76E(1) "must not make a purchase or acquisition ... unless ... authorised in advance", and s 76F(2) "no purchase or acquisition ... is lawful".
  That contradicts the premise on which the part took `NOTHING` (fork F-B11: that the sections never say what a failed acquisition is called), so the register entry says it was overridden.
  A second function, `s 76B(1) the keel's s 7(9)(ca) field: the interest is in accordance with sections 76B to 76G`, is that answer `EQUALS JUST TRUE`, a `BOOLEAN` with no `NOTHING` to convert; the keel's field is unchanged.
  Four assertions of `sga3-tests-76b.l4` changed from `NOTHING` to `JUST FALSE` and five were added for the second function.
  **A caveat that stays:** the function asks four conditions and not all the conditions of ss 76B to 76G. Lodging with the Registrar (s 76B(7)) and the consent of 75% of the holders of the class (s 76D(2A)) are procedural, and the text does not say what a breach of either does to the purchase, so a caller who has not met them can still get `JUST TRUE`. An independent reader noted this.
- **`s 76A(1A) the Court may order the transfer of the shares acquired in contravention of subsection (1)`** (`sga2-s76a-consequences.l4`).
  For a disposition that is not of book-entry securities the function now answers `NOTHING`; it answered `JUST FALSE`.
  The grant is limited to "a disposition of book-entry securities" and says nothing of another disposition, a scope limit with no "only", and the periods ruling of 2026-11-05, item (c), gives `NOTHING` outside such a limit.
  The other two gates of the same sentence, "on being satisfied" and "on the application of the Registrar or any other person", still answer `JUST FALSE` when they fail: they are the open split-site question below.
  One assertion in `sga2-tests-s76a.l4` changed from `JUST FALSE` to `NOTHING`.
- **`s 76A(4) the Court may make an order against the person`** (`sga2-s76a-consequences.l4`).
  For a person who is none of a party to the contract or transaction, the company, or a person who aided, abetted, counselled or procured the contravention, the function now answers `NOTHING`; it answered `JUST FALSE`.
  The subsection names the persons an order may be made against and does not close the list with "only", so for any other person the text says nothing (the periods ruling of 2026-11-05, item (c), and Example 2).
  The "Where (a) ...; (b) ...; and (c) the Court is satisfied" limbs still answer `JUST FALSE` when they fail, for a person in the named class: they are the open split-site question below.
  One assertion in `sga2-tests-s76a.l4` and one in `sg-cases-seat.l4` changed from `JUST FALSE` to `NOTHING`.

## Split sites (not harmonised)

Each agent was asked to record, site by site and without harmonising with the others, two questions the Guide leaves to the encoder: (i) an unmet element of an offence or a contravention, `JUST FALSE` or `NOTHING`; (ii) a "may" gated by "where", "when", "upon", "on application" or "with the consent of", `JUST FALSE` (the periods ruling) or `NOTHING` (the grant ruling).
Each agent's count and answer at each site is in its `## Split sites (<id>)` section (`notes/<agent>-NOTES.md`). **The agents did not answer (ii) alike:** the keel took `NOTHING` at its three sites, `sga1` at its four, and `sgb1` took `JUST FALSE` at all 19 of its sites.
A reader who compares this encoding with another jurisdiction's should treat (ii) as a place where the answer comes from the agent and not from the text.

## NEEDS-CORE

`NEEDS-CORE.md` gathers the requests of the parts that found the core lacking something (proposed, not landed).

## What check.sh prints

Run as `L4=<stable 1.6.110> L4_MAIN=<main 1.6.109> ./check.sh` on the merged folder, exit 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors-tests.l4                           0        32       0        0         0 |      0        32       0        0  same
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-cases-seat.l4                               0      3262       0        0         0 |      0      3262       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions-tests.l4                        0       399       0        0         0 |      0       399       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups-tests.l4                             0        93       0        0         0 |      0        93       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests-tests.l4                          0        76       0        0         0 |      0        76       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation-tests.l4                     0        81       0        0         0 |      0        81       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods-tests.l4                            0        70       0        0         0 |      0        70       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-solvency-tests.l4                           0        48       0        0         0 |      0        48       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sga1-alteration.l4                             0         0       0        0         0 |      0         0       0        0  same
sga1-classes.l4                                0         0       0        0         0 |      0         0       0        0  same
sga1-issue.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga1-redeemable.l4                             0         0       0        0         0 |      0         0       0        0  same
sga1-restrictions.l4                           0         0       0        0         0 |      0         0       0        0  same
sga1-rights.l4                                 0         0       0        0         0 |      0         0       0        0  same
sga1-sixth-schedule.l4                         0         0       0        0         0 |      0         0       0        0  same
sga1-tests-alteration.l4                       0       108       0        0         0 |      0       108       0        0  same
sga1-tests-classes.l4                          0        98       0        0         0 |      0        98       0        0  same
sga1-tests-issue.l4                            0       141       0        0         0 |      0       141       0        0  same
sga1-tests-redeemable.l4                       0        37       0        0         0 |      0        37       0        0  same
sga1-tests-restrictions.l4                     0       109       0        0         0 |      0       109       0        0  same
sga1-tests-rights.l4                           0        90       0        0         0 |      0        90       0        0  same
sga1-tests-sixth-schedule.l4                   0       104       0        0         0 |      0       104       0        0  same
sga2-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga2-s76-exceptions.l4                         0         0       0        0         0 |      0         0       0        0  same
sga2-s76-offence.l4                            0         0       0        0         0 |      0         0       0        0  same
sga2-s76-prohibition.l4                        0         0       0        0         0 |      0         0       0        0  same
sga2-s76-special-resolution.l4                 0         0       0        0         0 |      0         0       0        0  same
sga2-s76-whitewash.l4                          0         0       0        0         0 |      0         0       0        0  same
sga2-s76a-consequences.l4                      0         0       0        0         0 |      0         0       0        0  same
sga2-tests-s76-exceptions.l4                   0        84       0        0         0 |      0        84       0        0  same
sga2-tests-s76-offence.l4                      0        18       0        0         0 |      0        18       0        0  same
sga2-tests-s76-prohibition.l4                  0        56       0        0         0 |      0        56       0        0  same
sga2-tests-s76-special-resolution.l4           0       130       0        0         0 |      0       130       0        0  same
sga2-tests-s76-whitewash.l4                    0       120       0        0         0 |      0       120       0        0  same
sga2-tests-s76a.l4                             0        84       0        0         0 |      0        84       0        0  same
sga3-76b.l4                                    0         0       0        0         0 |      0         0       0        0  same
sga3-76c-76e.l4                                0         0       0        0         0 |      0         0       0        0  same
sga3-76f-76g.l4                                0         0       0        0         0 |      0         0       0        0  same
sga3-76h-76k.l4                                0         0       0        0         0 |      0         0       0        0  same
sga3-77-78.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga3-78a-78c.l4                                0         0       0        0         0 |      0         0       0        0  same
sga3-78d-78k.l4                                0         0       0        0         0 |      0         0       0        0  same
sga3-tests-76b.l4                              0        92       0        0         0 |      0        92       0        0  same
sga3-tests-76c-76e.l4                          0       160       0        0         0 |      0       160       0        0  same
sga3-tests-76f-76g.l4                          0        38       0        0         0 |      0        38       0        0  same
sga3-tests-76h-76k.l4                          0        87       0        0         0 |      0        87       0        0  same
sga3-tests-77-78.l4                            0        48       0        0         0 |      0        48       0        0  same
sga3-tests-78a-78c.l4                          0       104       0        0         0 |      0       104       0        0  same
sga3-tests-78d-78k.l4                          0       150       0        0         0 |      0       150       0        0  same
sgb1-s145-directors.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb1-s148-bankrupt-unfit.l4                    0         0       0        0         0 |      0         0       0        0  same
sgb1-s149b-appointment.l4                      0         0       0        0         0 |      0         0       0        0  same
sgb1-s154-convicted-default.l4                 0         0       0        0         0 |      0         0       0        0  same
sgb1-s155b-debarment.l4                        0         0       0        0         0 |      0         0       0        0  same
sgb1-s156-interests.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb1-s157-duties.l4                            0         0       0        0         0 |      0         0       0        0  same
sgb1-tests-s145.l4                             0       130       0        0         0 |      0       130       0        0  same
sgb1-tests-s148.l4                             0        97       0        0         0 |      0        97       0        0  same
sgb1-tests-s149b.l4                            0        71       0        0         0 |      0        71       0        0  same
sgb1-tests-s154.l4                             0        97       0        0         0 |      0        97       0        0  same
sgb1-tests-s155b.l4                            0        98       0        0         0 |      0        98       0        0  same
sgb1-tests-s156.l4                             0        72       0        0         0 |      0        72       0        0  same
sgb1-tests-s157.l4                             0        86       0        0         0 |      0        86       0        0  same
sgb2-s161-issue-of-shares.l4                   0         0       0        0         0 |      0         0       0        0  same
sgb2-s162-loans-to-directors.l4                0         0       0        0         0 |      0         0       0        0  same
sgb2-s163-loans-to-connected-persons.l4        0         0       0        0         0 |      0         0       0        0  same
sgb2-s164-register-of-shareholdings.l4         0         0       0        0         0 |      0         0       0        0  same
sgb2-s164a-s165-disclosure.l4                  0         0       0        0         0 |      0         0       0        0  same
sgb2-s168-s169-payments-to-directors.l4        0         0       0        0         0 |      0         0       0        0  same
sgb2-s171-secretary.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb2-s172-liability-of-officers.l4             0         0       0        0         0 |      0         0       0        0  same
sgb2-s173-registers.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb2-s173a-s173c-information-duties.l4         0         0       0        0         0 |      0         0       0        0  same
sgb2-s173d-s173i-transitional-and-notice.l4       0         0       0        0         0 |      0         0       0        0  same
sgb2-tests-s161.l4                             0        43       0        0         0 |      0        43       0        0  same
sgb2-tests-s162.l4                             0        91       0        0         0 |      0        91       0        0  same
sgb2-tests-s163.l4                             0       104       0        0         0 |      0       104       0        0  same
sgb2-tests-s164.l4                             0       100       0        0         0 |      0       100       0        0  same
sgb2-tests-s165.l4                             0        86       0        0         0 |      0        86       0        0  same
sgb2-tests-s168.l4                             0        85       0        0         0 |      0        85       0        0  same
sgb2-tests-s171.l4                             0        56       0        0         0 |      0        56       0        0  same
sgb2-tests-s172.l4                             0        29       0        0         0 |      0        29       0        0  same
sgb2-tests-s173.l4                             0        70       0        0         0 |      0        70       0        0  same
sgb2-tests-s173a.l4                            0        52       0        0         0 |      0        52       0        0  same
sgb2-tests-s173d.l4                            0        82       0        0         0 |      0        82       0        0  same
sgc1-s199.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s201-departures.l4                        0         0       0        0         0 |      0         0       0        0  same
sgc1-s201-statement.l4                         0         0       0        0         0 |      0         0       0        0  same
sgc1-s201.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s201a.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s201b.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s202.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s203.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s203a.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s204.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-sch12.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-tests-s199.l4                             0        46       0        0         0 |      0        46       0        0  same
sgc1-tests-s201-departures.l4                  0        22       0        0         0 |      0        22       0        0  same
sgc1-tests-s201-statement.l4                   0        33       0        0         0 |      0        33       0        0  same
sgc1-tests-s201.l4                             0        48       0        0         0 |      0        48       0        0  same
sgc1-tests-s201a.l4                            0        75       0        0         0 |      0        75       0        0  same
sgc1-tests-s201b.l4                            0        55       0        0         0 |      0        55       0        0  same
sgc1-tests-s202.l4                             0        95       0        0         0 |      0        95       0        0  same
sgc1-tests-s203.l4                             0        65       0        0         0 |      0        65       0        0  same
sgc1-tests-s203a.l4                            0        35       0        0         0 |      0        35       0        0  same
sgc1-tests-s204.l4                             0        30       0        0         0 |      0        30       0        0  same
sgc1-tests-sch12.l4                            0        54       0        0         0 |      0        54       0        0  same
sgc2-common.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgc2-s205-appointment.l4                       0         0       0        0         0 |      0         0       0        0  same
sgc2-s205a-exemption.l4                        0         0       0        0         0 |      0         0       0        0  same
sgc2-s205aa-resignation.l4                     0         0       0        0         0 |      0         0       0        0  same
sgc2-s206-208a-duties.l4                       0         0       0        0         0 |      0         0       0        0  same
sgc2-s209-interpretation.l4                    0         0       0        0         0 |      0         0       0        0  same
sgc2-sch13-small.l4                            0         0       0        0         0 |      0         0       0        0  same
sgc2-tests-s205.l4                             0       114       0        0         0 |      0       114       0        0  same
sgc2-tests-s205a.l4                            0       143       0        0         0 |      0       143       0        0  same
sgc2-tests-s205aa.l4                           0       134       0        0         0 |      0       134       0        0  same
sgc2-tests-s206-208a.l4                        0       181       0        0         0 |      0       181       0        0  same
sgc2-tests-s209.l4                             0        54       0        0         0 |      0        54       0        0  same
sgc2-tests-sch13.l4                            0       116       0        0         0 |      0       116       0        0  same
sgd-acquisition.l4                             0         0       0        0         0 |      0         0       0        0  same
sgd-amalgamation-solvency.l4                   0         0       0        0         0 |      0         0       0        0  same
sgd-amalgamation.l4                            0         0       0        0         0 |      0         0       0        0  same
sgd-compromise.l4                              0         0       0        0         0 |      0         0       0        0  same
sgd-tests-acquisition.l4                       0       220       0        0         0 |      0       220       0        0  same
sgd-tests-amalgamation-solvency.l4             0        54       0        0         0 |      0        54       0        0  same
sgd-tests-amalgamation.l4                      0       199       0        0         0 |      0       199       0        0  same
sgd-tests-compromise.l4                        0       191       0        0         0 |      0       191       0        0  same
sge-p10a-355-356.l4                            0         0       0        0         0 |      0         0       0        0  same
sge-p10a-357-358.l4                            0         0       0        0         0 |      0         0       0        0  same
sge-p10a-359.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-360.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-361.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-362.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-363.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-364.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-tests-355-356.l4                           0        28       0        0         0 |      0        28       0        0  same
sge-tests-357-358.l4                           0        38       0        0         0 |      0        38       0        0  same
sge-tests-359.l4                               0        64       0        0         0 |      0        64       0        0  same
sge-tests-360.l4                               0        20       0        0         0 |      0        20       0        0  same
sge-tests-361.l4                               0        26       0        0         0 |      0        26       0        0  same
sge-tests-362.l4                               0        49       0        0         0 |      0        49       0        0  same
sge-tests-363.l4                               0        45       0        0         0 |      0        45       0        0  same
sge-tests-364.l4                               0        37       0        0         0 |      0        37       0        0  same
sgf-s216.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgf-s216a.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgf-s216b.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgf-tests-s216.l4                              0        87       0        0         0 |      0        87       0        0  same
sgf-tests-s216a.l4                             0        65       0        0         0 |      0        65       0        0  same
sgf-tests-s216b.l4                             0        29       0        0         0 |      0        29       0        0  same
sgg-cessation.l4                               0         0       0        0         0 |      0         0       0        0  same
sgg-identity.l4                                0         0       0        0         0 |      0         0       0        0  same
sgg-lodging.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgg-names.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgg-registers.l4                               0         0       0        0         0 |      0         0       0        0  same
sgg-returns.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgg-scope.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgg-tests-cessation.l4                         0       125       0        0         0 |      0       125       0        0  same
sgg-tests-identity.l4                          0        37       0        0         0 |      0        37       0        0  same
sgg-tests-lodging.l4                           0       127       0        0         0 |      0       127       0        0  same
sgg-tests-names.l4                             0       118       0        0         0 |      0       118       0        0  same
sgg-tests-registers.l4                         0        79       0        0         0 |      0        79       0        0  same
sgg-tests-returns.l4                           0       132       0        0         0 |      0       132       0        0  same
sgg-tests-scope.l4                             0        38       0        0         0 |      0        38       0        0  same
TOTAL (173 modules)                            0     10476       0        0           |      0     10476       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 10,476 assertions satisfied over 173 modules (10,470 when the folder was merged; the three changes in "Changes made after the independent review" added six), with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each agent read its own traces on both builds, and the lead re-read every trace against its `-- EXPECT` word.

## What would need doing before the encoding is worth relying on

- A lawyer's reading of the fork registers and the marginal readings in `notes/<agent>-NOTES.md`; none has been ruled.
- The later waves above, and a decision on the `NEEDS-CORE.md` requests.
- A check of this edition against the current consolidation, if one later than the version in force to 20 October 2026 exists.
- A seat audit, which has not been run on this wave, and a ruling on the split-site question below, on which the independent readers did not agree among themselves.

## Source not official

The text this encoding quotes is a converter's rendering of an informal consolidation. No sentence here has been verified against the official text.
