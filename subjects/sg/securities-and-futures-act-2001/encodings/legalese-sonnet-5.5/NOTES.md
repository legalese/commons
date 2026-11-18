# NOTES: Securities and Futures Act 2001 (Singapore), Cut A of a whole-Act encoding with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
**This is Cut A only.** It encodes Part 1 (the interpretation and the definitional core), Part 7 (disclosure of interests), Part 8 (the Securities Industry Council and the Take-over Code provisions of the Act), Part 12 (market conduct) and Part 13 Division 1, Subdivisions (1) to (5) except (1A) (offers of securities and of securities-based derivatives contracts, with debentures); the rest of the Act (listed below) is not encoded.
Written 2026-11-18 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Built with the `l4` 1.6.110 (main, e51181d, 2026-11-11) and compared with 1.6.109 (main, 4c887e0, 2026-11-04); every module has the same four counts on both builds.

## Edition encoded

The Securities and Futures Act 2001, 2020 Revised Edition, in the Singapore Statutes Online (SSO) informal consolidation "version in force from 29/6/2026 to 20/10/2026", retrieved 2026-10-09 (`../../registers/source-bundle/SFA2001.meta.json`, `retrieved_date`), carrying the amendments its amendment marks show.
That file is a plain-text rendering of a PDF: it is **not the official text**, and nothing here is verified against the official text.
A later consolidation may exist and was not read; the encoding is of that text only.
Line numbers (`src:N`) are lines of that file as it is: lines 1 to 4224 are this keel's range (the front matter and arrangement of sections, lines 1 to 1667, are inert; the body starts at line 1668).
Amendment marks (`[4/2017]`, `[Act 12 of 2024 wef 30/08/2024]`) and page furniture are not quoted and are not rules.
The text is quoted only where it is encoded, mechanically (`srcrefs.py` checks every quote line and every `@ref` locator).
Nothing in this folder says or suggests that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.
The text file has sha256 `35f011d3b5ab38d72ec4aeb441d749a5858db44430b92099dd60a39411c033c3`, computed from the file when this folder was assembled.
**No check for a later consolidation has been made for this Act.** The one attempt made for any Act of this work, on 2026-11-18, was the first step of a check aimed at the Companies Act's page on the Singapore Statutes Online site: the request for the site's robots file was refused with HTTP 403 and nothing further was requested, so a later version of this Act is not ruled out.
A reader asking about a date outside 29 June 2026 to 20 October 2026 must check the text for that date before relying on any answer here.

## The Take-over Code is not in the Act

Part 8 of the deposited text is headed "Securities Industry Council and Take-over Offers" and has three sections (lines 31359 to 31514).
Section 138 continues the Securities Industry Council in existence; section 139(2) says the Authority is to issue, under section 321, "a code known as the Singapore Code on Take-overs and Mergers (called in this Act the Take-over Code)"; section 140 prohibits giving notice of, or announcing, a take-over offer that the person has no intention to make or no reasonable or probable grounds to perform, and makes the contravention an offence.
**The take-over regime is mostly in the Code, and the Code is not part of the Act and is not in the deposited text.** Section 139(3) to (8) say how the Code operates: it is deemed not to be subsidiary legislation, it applies to a take-over offer and every party concerned must comply with it, the Council administers and enforces it and may issue rulings on it, and a failure to observe it "does not of itself render that party liable to criminal proceedings" but may be relied on in proceedings.
So Cut A covers only the Council's statutory part and the Act's own sections of Part 8. The Act does not set out the Code's rules, and they are not encoded: an answer here about a take-over says what the Act says, and nothing about what the Code requires.

## What this folder covers

The deposited text has 54,841 lines and 318,478 words. Cut A encodes 102,998 of those words (32.3%), in 5 agents' ranges.

| agent | text (lines of `SFA2001.txt`) | words | what |
| --- | --- | --- | --- |
| keel | 1 to 4224 | 21,476 | the front matter and arrangement of sections (lines 1 to 1667, inert) and Part 1 (ss 1 to 4B: the interpretation section, and the sections on associates (s 3), interests (s 4) and the investor classes (s 4A)), the shared core, and the one module that counts every period |
| sfaa | 27938 to 31051, 31359 to 31514 | 19,675 | Part 7 (disclosure of interests), Divisions 1 to 4: interests in a corporation, in a business trust and in a real estate investment trust, and the civil penalty; and Part 8 (the Securities Industry Council and the Take-over Code provisions of the Act) |
| sfab | 34173 to 37498 | 19,292 | Part 12 (market conduct), Divisions 1 to 6 (ss 196 to 238): prohibited conduct in relation to capital markets products (Division 1) and to financial benchmarks (Division 2), insider trading, civil liability, attributed liability, and the miscellaneous section (s 238, inert) |
| sfac | 37499 to 37947, 38374 to 41832 | 23,622 | Part 13 Division 1, Subdivisions (1) and (2): offers of investments, interpretation and prospectus requirements (ss 239 to 260) |
| sfad | 41833 to 45043 | 18,933 | Part 13 Division 1, Subdivisions (3), (4) and (5): debentures, exemptions and general (ss 261 to 282) |

**Not encoded in Cut A**, by range of the text:

| lines | words | what falls in them |
| --- | --- | --- |
| 4225 to 27937 | 136,371 | Part 2 (Organised Markets); Part 2A (Trade Repositories); Part 3 (Clearing Facilities); Part 3AA (Central Depository System); Part 3A (Approved Holding Companies); Part 4 (Holders of Capital Markets Services Licence and Representatives); Part 5 (Books, Customer Assets and Audit); Part 6 (Conduct of Business); Part 6AA (Financial Benchmarks); Part 6A (Reporting of Derivatives Contracts); Part 6B (Clearing of Derivatives Contracts); Part 6C (Trading of Derivatives Contracts) |
| 31052 to 31358 | 1,768 | Part 7A (Short Selling) |
| 31515 to 34172 | 16,434 | Part 9 (Supervision and Investigation); Part 10 (Assistance to Foreign Regulatory Authorities); Part 11 (Investor Compensation Scheme) |
| 37948 to 38373 | 2,429 | Part 13 Division 1, Subdivision (1A) (offers of units in and recognition of business trusts); in Part 13 (Offers of Investments) |
| 45044 to 54841 | 58,478 | Part 13 Divisions 2 to 4 (Collective Investment Schemes; Hawking of Securities, Securities-based Derivatives Contracts and Units in Collective Investment Scheme; Capital Markets Products), then the rest of Part 13 (Offers of Investments); Part 13A (Modification of Act for Purposes of Dual Listing Boards); Part 14 (Appeals); Part 15 (Miscellaneous) and the Schedules |

The ranges left out include collective investment schemes (Part 13 Division 2); the organised markets, trade repositories, clearing facilities, central depository system, approved holding companies, financial benchmarks and the reporting, clearing and trading of derivatives contracts (Parts 2 to 3A and 6AA to 6C); licensing and conduct of business (Parts 4 to 6); short selling (Part 7A); supervision and investigation (Part 9), assistance to foreign regulatory authorities (Part 10) and the investor compensation scheme (Part 11); and Parts 13A to 15 and the Schedules.
Cross-references from an encoded provision into one of them are taken as inputs, named for the fact (see the seams section).

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`sfa-core.l4`, the definitions of section 2(1), sections 3, 4, 4A and 4B, the one periods module and their tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
4 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `sfaa` (lines 27938 to 31051, 31359 to 31514), `sfab` (lines 34173 to 37498), `sfac` (lines 37499 to 37947, 38374 to 41832), `sfad` (lines 41833 to 45043).
The lead verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the NOT-precedence sweep, the keel's files identical to the keel's, every trace read against its `-- EXPECT` word and compared across the two builds) and then merged them with a script; the part modules are copied unchanged except as the merge decisions below say, and the merge edited no rule.
No independent test pass and no seat audit has been run on this folder. The tests are the agents' own, written from the text.
Every note a part wrote is kept, with names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md` where it wrote one; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
Briefs are shipped verbatim except for lines about tooling.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each agent wrote its own seat questions and cases. The lead concatenated them, in part order, into `sfa-seat.l4` and `sfa-cases-seat.l4`, with one banner comment per agent; the text under each banner is the agent's, unchanged. The keel's own small seat (`sfa-seat-keel.l4`, `sfa-cases-seat-keel.l4`) is merged the same way. The merged seat module imports the layer-1 modules its questions call and checks clean.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section. The merge does not wire one part's output into another's input, so the seat asks the person each such fact. This includes the keel's two seams S1 and S2 (the Securities Industry Council, the Take-over Code), which `notes/keel-PLAN.md` section 4.1 says the lead wires at the merge: **the merge did not wire them**, for the same reason as the other seams (the merge edits no rule). `sfaa`'s `## Seams` section says how: `(s 138(1) ...) EQUALS JUST TRUE` passed to the keel's `BOOLEAN` input, at a layer above both.
- **NEEDS-CORE: nothing hoisted.** None of the four parts wrote a `NEEDS-CORE.md`. The keel's one item (`Period unit` is declared in `sfa-periods.l4`, not in `sfa-core.l4`) is a placement choice, not a gap, and nothing depends on where it lives; it is left where it is.
- **One keel module was edited, by one import line.** `sfa-cases-earlier-pass.l4` imported `sfa-seat-keel`, which the merge folds into `sfa-seat.l4`; the line now imports `sfa-seat`. No rule or assertion changed. The first merged gate, run before this edit, showed 31 errors in that one module and none elsewhere.
- **Part-local types and helper names stay where they are.** Every top-level name carries the label of its provision, so no two modules define the same name, and the merged gate compiles them together. One part-local type, `Subdivision (4) an exemption relied on` in `sfad-exemption-summary.l4`, is named for a Subdivision and not for a section.
- **The merge lost nothing:** the merged folder was gated as it stands: 99 modules, 6,290 assertions satisfied (below), which is the sum of the keel's own gate and the four parts' own gates.

## Where things are

| agent | modules (layer 1) | assertions in its test modules | `#TRACE` blocks | seat questions | coverage rows (encoded / fork / inert / repealed) |
| --- | --- | --- | --- | --- | --- |
| keel | 12 | 956 | 0 | 31 | 209 (199 / 3 / 7 / 0) |
| sfaa | 12 | 1087 | 92 | 40 | 525 (199 / 308 / 18 / 0) |
| sfab | 7 | 1055 | 53 | 50 | 670 (321 / 265 / 76 / 8) |
| sfac | 10 | 1608 | 77 | 21 | 808 (616 / 147 / 39 / 6) |
| sfad | 7 | 1011 | 47 | 40 | 273 (137 / 107 / 27 / 2) |
| seat cases, all agents | | 573 (`sfa-cases-seat.l4`) | | | |

The seat layer is `sfa-seat.l4` (182 `@export` questions in all) and `sfa-cases-seat.l4`; every other module is layer 1, with a tests module beside it.
**The coverage columns are each agent's own count of its own table and are not comparable across agents as a measure of how contestable the text is.** In particular `sfaa` marks a row `fork` whenever the rule that encodes it inherits a fork id from the provisions above it (its coverage section says so), which is why 308 of its 525 rows are `fork`; read each agent's own coverage section for what it counts as `fork`.

## The source

The text is `../../registers/source-bundle/SFA2001.txt` (54,841 lines, sha256 `35f011d3b5ab38d72ec4aeb441d749a5858db44430b92099dd60a39411c033c3`), the Singapore Statutes Online informal consolidation turned from a PDF into plain text; its terms, its attribution wording and its unofficial status are in `../../SOURCE-LICENSE.md`.
Page furniture ("Informal Consolidation – version in force from 29/6/2026 to 20/10/2026", "2020 Ed. Securities and Futures Act 2001 <page>") and the bracketed amendment marks (for example "[4/2017]") are not text of a provision. The arrangement of sections at the head (lines 1 to 1667) is inert; every section number was read from the body (line 1668 on).

## The seat

From the keel's plan (section 7):

The seat is the individual who asks.
A seat question is a decision function whose `@export` line carries the question, ending in `?`, and whose inputs are plain facts the person can state, each with a `@desc` (the question the form asks).
The function's own name is the question without the final `?`.
Every question is named `Under section N, ...` (the Act's own numbering, then a comma, then the question in the person's words: `Under section 4(1), do I have authority over the disposal of these securities, contracts or units?`).
The name asks the question the body answers, in the same direction: `JUST TRUE` is yes, `JUST FALSE` is no in the text's own words, `NOTHING` is "the text does not say".
A part's seat covers its own provisions; the keel's seat covers ss 2(4), 2(6), 3, 4, 4A and 4B only, so a part does not repeat these.

## Seams between parts

A part cannot import another part, so the part that depends on another's answer takes it as an input named for the fact. The keel's plan lists every seam, with the input's name and type: `notes/keel-PLAN.md`, section 4 (4.1: the keel asks and a part answers; 4.2: a part asks and the keel answers, which is an import and not a seam; 4.3: between the parts, S3 to S8). Each part's own `## Seams` section says which it confirmed in the text and what it found that the plan lacks (`sfac` found S9).
**One difference between the two sides of a seam, found at the merge:** for S4 and S5 (`sfac` asks, `sfad` answers), `sfad`'s functions answer `BOOLEAN` and `sfac`'s inputs are `MAYBE BOOLEAN` (`notes/sfac-NOTES.md` says that for S4 only `JUST TRUE` counts as the exemption being shown, and for S5 that the answer is passed through as it is). The merge does not wire them, so the difference changes no answer here; whoever wires them should pass `sfad`'s answer through `JUST TRUE` and `JUST FALSE`.

## Split sites (not harmonised)

Each agent was asked to record, site by site and without harmonising with the others, two questions the Guide leaves to the encoder: (i) an unmet element of an offence or a contravention, `JUST FALSE` or `NOTHING`; (ii) a "may" gated by "where", "when", "upon", "on application" or "with the consent of", `JUST FALSE` (the periods ruling) or `NOTHING` (the grant ruling). Neither question is settled; the open one on the S1 bench card is the second.
A site is a branch line tagged `-- SPLIT-SITE (i)` or `(ii)` in a layer-1 module, and every site also has a fork line in its part's NOTES. **The counts below were made by a script over the merged folder, one site per tagged branch line, with the answer read from the code on that line; each part's own count agrees.** A grep for the tag over the whole folder finds more lines than there are sites, because comments and test files mention it.

| agent | (i) `NOTHING` | (i) `JUST FALSE` | (ii) `NOTHING` | (ii) `JUST FALSE` |
| --- | --- | --- | --- | --- |
| keel | 0 | 0 | 1 | 0 |
| sfaa | 62 | 0 | 18 | 0 |
| sfab | 43 | 24 | 26 | 9 |
| sfac | 43 | 8 | 0 | 8 |
| sfad | 0 | 12 | 2 | 10 |
| all | 148 | 44 | 47 | 27 |

That is 266 sites: 192 of type (i) and 74 of type (ii).
**The agents did not answer alike.** `sfaa` took `NOTHING` at all 80 of its sites; `sfad` took `JUST FALSE` at all 12 of its type (i) sites; `sfac` took `JUST FALSE` at all 8 of its type (ii) sites; `sfab` is mixed at both kinds.
A reader who compares this encoding with another jurisdiction's should treat both kinds as places where the answer comes from the agent and not from the text. A ruling can be applied by flipping the tagged branch, site by site.

## NEEDS-CORE

`NEEDS-CORE.md` gathers the keel's note (the only one written) and says that no part asked for anything (proposed, not landed).

## What check.sh prints

Run as `L4=<stable 1.6.110> L4_MAIN=<main 1.6.109> ./check.sh` on the merged folder, exit 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sfa-application-tests.l4                       0         4       0        0         0 |      0         4       0        0  same
sfa-application.l4                             0         0       0        0         0 |      0         0       0        0  same
sfa-associates-tests.l4                        0        72       0        0         0 |      0        72       0        0  same
sfa-associates.l4                              0         0       0        0         0 |      0         0       0        0  same
sfa-cases-earlier-pass.l4                      0        15       0        0         0 |      0        15       0        0  same
sfa-cases-seat.l4                              0       573       0        0         0 |      0       573       0        0  same
sfa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-benchmarks-tests.l4            0        61       0        0         0 |      0        61       0        0  same
sfa-definitions-benchmarks.l4                  0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-markets-tests.l4               0       116       0        0         0 |      0       116       0        0  same
sfa-definitions-markets.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-persons-tests.l4               0       144       0        0         0 |      0       144       0        0  same
sfa-definitions-persons.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-products-tests.l4              0       107       0        0         0 |      0       107       0        0  same
sfa-definitions-products.l4                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-rest-tests.l4                  0        41       0        0         0 |      0        41       0        0  same
sfa-definitions-rest.l4                        0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-schemes-tests.l4               0       110       0        0         0 |      0       110       0        0  same
sfa-definitions-schemes.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-interests-tests.l4                         0        86       0        0         0 |      0        86       0        0  same
sfa-interests.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-investors-tests.l4                         0       118       0        0         0 |      0       118       0        0  same
sfa-investors.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-periods-tests.l4                           0        82       0        0         0 |      0        82       0        0  same
sfa-periods.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfa-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-beneficial-disclosure.l4             0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-directors.l4                         0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-interpretation.l4                    0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-penalties-court.l4                   0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-register.l4                          0         0       0        0         0 |      0         0       0        0  same
sfaa-div1-shareholders.l4                      0         0       0        0         0 |      0         0       0        0  same
sfaa-div2-officers.l4                          0         0       0        0         0 |      0         0       0        0  same
sfaa-div2-trust.l4                             0         0       0        0         0 |      0         0       0        0  same
sfaa-div3-officers.l4                          0         0       0        0         0 |      0         0       0        0  same
sfaa-div3-reit.l4                              0         0       0        0         0 |      0         0       0        0  same
sfaa-div4-civil-penalty.l4                     0         0       0        0         0 |      0         0       0        0  same
sfaa-part8.l4                                  0         0       0        0         0 |      0         0       0        0  same
sfaa-tests-div1-beneficial-disclosure.l4       0        86       0        0         0 |      0        86       0        0  same
sfaa-tests-div1-directors.l4                   0        86       0        0         0 |      0        86       0        0  same
sfaa-tests-div1-interpretation.l4              0        69       0        0         0 |      0        69       0        0  same
sfaa-tests-div1-penalties-court.l4             0        45       0        0         0 |      0        45       0        0  same
sfaa-tests-div1-register.l4                    0        30       0        0         0 |      0        30       0        0  same
sfaa-tests-div1-shareholders.l4                0        57       0        0         0 |      0        57       0        0  same
sfaa-tests-div2-officers.l4                    0       127       0        0         0 |      0       127       0        0  same
sfaa-tests-div2-trust.l4                       0       158       0        0         0 |      0       158       0        0  same
sfaa-tests-div3-officers.l4                    0       127       0        0         0 |      0       127       0        0  same
sfaa-tests-div3-reit.l4                        0       160       0        0         0 |      0       160       0        0  same
sfaa-tests-div4-civil-penalty.l4               0        64       0        0         0 |      0        64       0        0  same
sfaa-tests-part8.l4                            0        78       0        0         0 |      0        78       0        0  same
sfab-attributed.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-civil.l4                                  0         0       0        0         0 |      0         0       0        0  same
sfab-division-1.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-division-2.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-insider-1.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-insider-2.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-insider-3.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-tests-attributed.l4                       0       352       0        0         0 |      0       352       0        0  same
sfab-tests-civil.l4                            0       189       0        0         0 |      0       189       0        0  same
sfab-tests-division-1.l4                       0       176       0        0         0 |      0       176       0        0  same
sfab-tests-division-2.l4                       0        47       0        0         0 |      0        47       0        0  same
sfab-tests-insider-1.l4                        0        78       0        0         0 |      0        78       0        0  same
sfab-tests-insider-2.l4                        0       105       0        0         0 |      0       105       0        0  same
sfab-tests-insider-3.l4                        0        77       0        0         0 |      0        77       0        0  same
sfab-tests-integration.l4                      0        31       0        0         0 |      0        31       0        0  same
sfac-239.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-240.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-240aa.l4                                  0         0       0        0         0 |      0         0       0        0  same
sfac-241.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-242.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-243.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-249.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-253.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-257.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfac-tests-239.l4                              0       184       0        0         0 |      0       184       0        0  same
sfac-tests-240.l4                              0       152       0        0         0 |      0       152       0        0  same
sfac-tests-240aa.l4                            0       159       0        0         0 |      0       159       0        0  same
sfac-tests-241.l4                              0       210       0        0         0 |      0       210       0        0  same
sfac-tests-242.l4                              0        90       0        0         0 |      0        90       0        0  same
sfac-tests-243.l4                              0       136       0        0         0 |      0       136       0        0  same
sfac-tests-249.l4                              0       296       0        0         0 |      0       296       0        0  same
sfac-tests-253.l4                              0       168       0        0         0 |      0       168       0        0  same
sfac-tests-257.l4                              0       213       0        0         0 |      0       213       0        0  same
sfac-tests-duties.l4                           0         0       0        0         0 |      0         0       0        0  same
sfad-circumstances.l4                          0         0       0        0         0 |      0         0       0        0  same
sfad-debentures.l4                             0         0       0        0         0 |      0         0       0        0  same
sfad-directions.l4                             0         0       0        0         0 |      0         0       0        0  same
sfad-exemption-summary.l4                      0         0       0        0         0 |      0         0       0        0  same
sfad-investor-exemptions.l4                    0         0       0        0         0 |      0         0       0        0  same
sfad-nocons-small-private.l4                   0         0       0        0         0 |      0         0       0        0  same
sfad-ois-intl-gov-atm.l4                       0         0       0        0         0 |      0         0       0        0  same
sfad-tests-circumstances.l4                    0       175       0        0         0 |      0       175       0        0  same
sfad-tests-debentures.l4                       0       302       0        0         0 |      0       302       0        0  same
sfad-tests-directions.l4                       0        29       0        0         0 |      0        29       0        0  same
sfad-tests-exemption-summary.l4                0        12       0        0         0 |      0        12       0        0  same
sfad-tests-investor-exemptions.l4              0       121       0        0         0 |      0       121       0        0  same
sfad-tests-nocons-small-private.l4             0       193       0        0         0 |      0       193       0        0  same
sfad-tests-ois-intl-gov-atm.l4                 0       179       0        0         0 |      0       179       0        0  same
TOTAL (99 modules)                             0      6290       0        0           |      0      6290       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 6,290 assertions satisfied over 99 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each agent read its own traces on both builds, and the lead re-read every part's traces against their `-- EXPECT` words and compared the outcomes of the two builds.

## What would need doing before the encoding is worth relying on

- A lawyer's reading of the fork registers and the marginal readings in `notes/<agent>-NOTES.md`; none has been ruled.
- The rest of the Act (above), the Take-over Code (which is not in the Act), and a decision on the two split-site questions.
- A check of this edition against the current consolidation, if one later than the version in force to 20 October 2026 exists.
- Independent test authors and a seat audit, neither of which has been run on this folder.

## Source not official

The text this encoding quotes is a converter's rendering of an informal consolidation. No sentence here has been verified against the official text.
