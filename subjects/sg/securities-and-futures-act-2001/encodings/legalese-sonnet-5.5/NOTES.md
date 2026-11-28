# NOTES: Securities and Futures Act 2001 (Singapore), Cut A of a whole-Act encoding with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
The open questions that the text does not settle, and the recorded limits of this row, are in `registers/fork-register.json` (10 entries, each with status `open`).
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
An independent test pass has been run (four reader groups, below); no seat audit has been run. The tests in this folder are the agents' own, written from the text, and the readers' own test modules are not shipped.
Every note a part wrote is kept, with names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md` where it wrote one; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
Briefs are shipped verbatim except for lines about tooling.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each agent wrote its own seat questions and cases. The lead concatenated them, in part order, into `sfa-seat.l4` and `sfa-cases-seat.l4`, with one banner comment per agent; the text under each banner is the agent's, unchanged. The keel's own small seat (`sfa-seat-keel.l4`, `sfa-cases-seat-keel.l4`) is merged the same way. The merged seat module imports the layer-1 modules its questions call and checks clean.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section. The merge does not wire one part's output into another's input, so the seat asks the person each such fact. This includes the keel's two seams S1 and S2 (the Securities Industry Council, the Take-over Code), which `notes/keel-PLAN.md` section 4.1 says the lead wires at the merge: **the merge did not wire them**, for the same reason as the other seams (the merge edits no rule). `sfaa`'s `## Seams` section says how: `(s 138(1) ...) EQUALS JUST TRUE` passed to the keel's `BOOLEAN` input, at a layer above both.
- **NEEDS-CORE: nothing hoisted.** None of the four parts wrote a `NEEDS-CORE.md`. The keel's one item (`Period unit` is declared in `sfa-periods.l4`, not in `sfa-core.l4`) is a placement choice, not a gap, and nothing depends on where it lives; it is left where it is.
- **One keel module was edited, by one import line.** `sfa-cases-earlier-pass.l4` imported `sfa-seat-keel`, which the merge folds into `sfa-seat.l4`; the line now imports `sfa-seat`. No rule or assertion changed. The first merged gate, run before this edit, showed 31 errors in that one module and none elsewhere.
- **Part-local types and helper names stay where they are.** Every top-level name carries the label of its provision, so no two modules define the same name, and the merged gate compiles them together. One part-local type, `Subdivision (4) an exemption relied on` in `sfad-exemption-summary.l4`, is named for a Subdivision and not for a section.
- **The merge lost nothing:** the merged folder was gated as it stands: 100 modules, 6,293 assertions satisfied (below), which is the sum of the keel's own gate (1,069) and the four parts' own gates (1,218, 1,175, 1,683 and 1,145), plus the 3 assertions of `sfac-tests-reader.l4`, added after the readers (below).

## Where things are

| agent | modules (layer 1) | assertions in its test modules | `#TRACE` blocks | seat questions | coverage rows (encoded / fork / inert / repealed) |
| --- | --- | --- | --- | --- | --- |
| keel | 12 | 956 | 0 | 31 | 209 (199 / 3 / 7 / 0) |
| sfaa | 12 | 1087 | 92 | 40 | 525 (199 / 308 / 18 / 0) |
| sfab | 7 | 1055 | 53 | 50 | 670 (321 / 265 / 76 / 8) |
| sfac | 10 | 1611 | 77 | 21 | 808 (616 / 147 / 39 / 6) |
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

## Independent readers of Cut A (assumed, not ruled)

Four reader groups, each of which wrote its own answers to scenarios taken from the text and then ran them against this encoding, covered every range encoded in Cut A: the keel's Part 1 (with `sfad`), `sfaa`, `sfab` and `sfac`.
A failing assertion was left failing and triaged as `ENCODER` (the encoding is wrong), `SCENARIO` (the reader's mistake), `AMBIGUOUS` (the text and the Guide read both ways) or `GAP` (no function can answer the scenario).
Their triage files are `notes/reader-sfa-g1-triage.md` to `notes/reader-sfa-g4-triage.md`; `notes/reader-sfa-README.md` says what is not shipped with them.

| group | read | words | assertions | satisfied | failed | refused | `ENCODER` | `SCENARIO` | `AMBIGUOUS` | `GAP` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | the keel (Part 1, lines 1668 to 4224) and sfad | 32,982 | 531 | 514 | 17 | 0 | 2 | 6 | 9 | 4 |
| 2 | sfaa | 19,675 | 474 | 457 | 17 | 0 | 0 | 4 | 13 | 31 |
| 3 | sfab | 19,292 | 563 | 507 | 56 | 0 | 12 | 6 | 38 | 11 |
| 4 | sfac | 23,622 | 596 | 555 | 41 | 0 | 1 | 2 | 38 | 14 |
| all | Cut A | 95,571 | 2,164 | 2,033 | 131 | 0 | 15 | 18 | 98 | 60 |

The assertion counts are the lead's own rerun of each group's test file on the stable build (1.6.110, `JL4_LIBRARY_PATH` unset), and each equals the group's own count. Group 1 also wrote nine `#TRACE` duty scenarios, which are not assertions and are not in the table; all nine gave the expected result.
The readers' test modules and answer files are not shipped, so a line number in a triage file points at a file you do not have; the provision, the text line and the two answers in each line are enough to rerun the scenario by hand.
**How independent each group was.** In every group the scenarios written before any module was opened are blind; the rest are not. Group 1: scenarios 1 to 438 of 544. Group 2: 1 to 445 of 505, with 446 to 470 written after reading module names and types and 471 to 505 after the first run. Group 3: the first 499 of 574, the other 75 written before they were run. Group 4: all 610, by the statement at the head of its `ANSWERS.md` ("before any `.l4` file was opened"). Each reader says it changed no expected value to match the encoding; the lead's scan of each transcript found no tool use outside the reader's own folder, and cannot see what a reader did not write down.

### The `ENCODER` lines (15)

**Fourteen of these were not applied.** 13 of the 15 are a `where` or `if` gate read the other way from the part that wrote the function (group 3: 12 lines; group 1: `s 276(7)(a)`), which is the open split-site question (above) and not a defect the text settles; group 1's `s 4(10)(f)` is a scope limit read the other way.
**One is a different kind: group 4's `s 239(3A)(b)` is a naming defect.** The function is named "the document issued by the prescribed entity is not a debenture" and answers `JUST FALSE` for a certificate of deposit, where `JUST FALSE` means "it is a debenture: no"; so its name and its value read in opposite directions, and `s 239(3A)(a)` ("the invitation by the prescribed entity is not an offer of debentures") has the same shape. The lead read both functions and the text (`sfac-239.l4`) and agreed the name and the value disagreed. **Changed, in its own commit (assumed, not ruled):** the two functions are renamed `s 239(3A)(a) the invitation by the prescribed entity is an offer of debentures` and `s 239(3A)(b) the document issued by the prescribed entity is a debenture`, so that each name asks what its value answers; the values are unchanged (the combined function `s 239(3) and (3A)` already read them that way), the tests and the notes follow, nothing else in the folder called them, and the reader's scenarios #51 to #53, recast to the new names, are kept in `sfac-tests-reader.l4`.

Each line below is in the reader's own words.

| group | scenario | provision | reader expected | encoding answers | the two readings |
| --- | --- | --- | --- | --- | --- |
| 1 | 160 | s 4(10)(f) (3977-3980), "for the purposes of Part 7, an interest in a ... derivatives contract ... cash settlement only" | NOTHING | JUST FALSE | The limb is confined by its own words to Part 7 and has no "only" closing the scope, so for a provision other than Part 7 the answer is NOTHING (scope limit, ruling (c); Guide: "a scope limit with no only answers NOTHING"). The encoder's own comment records NOTHING as the other reading. |
| 1 | 393 | s 276(7)(a) (44540-44543), "Subsections (1), (3) and (4) do not apply where the securities ... are (a) ... of the same class as other securities ... listed" | JUST FALSE | NOTHING | , a close call. The only gate is a "where" condition, and ruling (b) says a failed "where" answers JUST FALSE. The encoder read "where" as the limit of an exemption (its fork note s276-7 records JUST FALSE as the other reading), which the grant and prohibition sentence of the Guide supports; I weigh ruling (b) as the more specific, but a reader who prefers the other sentence should treat this as AMBIGUOUS. |
| 3 | S31 | s197(3)(b) [L34333] | JUST FALSE | NOTHING | Guide: a condition the text introduces with "if" answers JUST FALSE when unmet ("it is presumed ... if the person ..."); the encoding answers NOTHING citing "Without limiting subsection (1)" (that phrase says the presumption does not cut down s197(1); it does not make the presumption question open; other reading: the purpose stays open to proof) |
| 3 | S220 | s218(4)(b) [L35326] | JUST FALSE | NOTHING | periods ruling (b): a "where ..." condition ("where the prosecution or claimant proves ...") that fails answers JUST FALSE; the encoding answers NOTHING with no fork line |
| 3 | S523 | s197(3)(b) [L34333] | JUST FALSE | NOTHING | Guide: a condition the text introduces with "if" answers JUST FALSE when unmet ("it is presumed ... if the person ..."); the encoding answers NOTHING citing "Without limiting subsection (1)" (that phrase says the presumption does not cut down s197(1); it does not make the presumption question open; other reading: the purpose stays open to proof) |
| 3 | S527 | s218(4A) [L35342] | JUST FALSE | NOTHING | Guide: "if the prosecution or claimant proves ..." unmet answers JUST FALSE; the encoding answers NOTHING with no fork line (and s218(4) shows the same pattern) |
| 3 | S561 | s234(1)(b)(ii)(A) [L35992] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S563 | s234(1)(b)(ii)(B) [L35998] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S564 | s236D(1)(b)(ii)(A) [L36575] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S565 | s236D(1)(b)(ii)(B) [L36585] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S566 | s236G(1)(b)(ii)(A) [L36904] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S567 | s236G(1)(b)(ii)(B) [L36910] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S568 | s236I(1)(b)(ii)(A) [L37073] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 3 | S569 | s236I(1)(b)(ii)(B) [L37083] | JUST FALSE | NOTHING | periods ruling (b): "in the case where [s218/219 contravention]" / "in any other case" is a case split in the text's own words: for the other case the text names the other comparison price, so this one is JUST FALSE; the encoding answers NOTHING. Same pattern in the (A)/(B) functions of s234, s236D, s236G and s236I |
| 4 | 52 | s 239(3A)(b), text line 37749-37752 | JUST TRUE | JUST FALSE | Certificate of deposit issued by a licensed bank: debenture? / Naming or polarity defect at sfac-239.l4:573. The function is named "the document ... is not a debenture", so for a certificate of deposit issued by a prescribed entity it should answer JUST TRUE (the text: "are not debentures"). It answers JUST FALSE, which its own comment uses to mean "debenture: no", the opposite of its name. (3A)(a) at sfac-239.l4:554 has the same shape and the combined function reads its JUST FALSE as "not an offer", so the pair is consistent only if the name is read with the "not" dropped. Fix the name or the value. |

### The `AMBIGUOUS` lines (98)

Each line gives the reader's expectation, what the encoding answers, and the two readings. Nothing was changed.
Across the `AMBIGUOUS` and `ENCODER` lines that give two answers: the reader expected `JUST FALSE` and the encoding answers `NOTHING` in 93; the reader expected `NOTHING` and the encoding answers `JUST FALSE` in 15; other pairs 5.

| group | scenario | provision | reader expected | encoding answers | the two readings |
| --- | --- | --- | --- | --- | --- |
| 1 | 162 | s 4 as a whole (3783-3994), a person with none of the listed routes to an interest | NOTHING | JUST FALSE | Reading 1 (mine): s 4 lists ways a person has an interest and never closes the list with "only", so silence, NOTHING. Reading 2 (encoder): each route is an "if" and with no route holding the text's own answer is no, JUST FALSE. |
| 1 | 230 | s 266(2) (42107-42113), the trustee has formed no such opinion | NOTHING | JUST FALSE | , split site ("may" gated by "where"). Reading 1 (mine, grant ruling): a power whose gate failed answers NOTHING. Reading 2 (encoder, ruling (b)): a failed "where" answers JUST FALSE. |
| 1 | 402 | s 277(1AB) (44686-44703), the listed entity has not guaranteed the subsidiary | NOTHING | JUST FALSE | , same split site as 230 (the Authority "may" declare, "where" the guarantee exists). |
| 1 | 256 | s 268(10)(b) (42345-42352), annual accounts, trustee has not consented | JUST FALSE | NOTHING | , case-by-case ("a duty whose if is unmet"). Reading 1 (mine): "need not be audited ... if the trustee has consented" is an "if" condition, so unmet answers JUST FALSE. Reading 2 (encoder): the dispensation is a grant and its gate failed, so NOTHING. |
| 1 | 290 | s 271(1) (42605-42611), a clause that exempts the trustee only where the trustee shows the required care | JUST FALSE | NOTHING | Reading 1 (mine, ruling (b)): "void insofar as ... where the trustee fails to show the care", the "where" fails, so not void, JUST FALSE. Reading 2 (encoder): "insofar as" limits a prohibition in its own wording and the case falls outside the limit, NOTHING. |
| 1 | 389 | s 276(3) (44459-44461), the holding corporation is itself an accredited investor | JUST FALSE | NOTHING | , case-by-case ("(other than X)"). Reading 1 (mine): the carve-out takes the corporation outside the bar, so the bar answers no. Reading 2 (encoder): the text is silent about a carved-out corporation, NOTHING. |
| 1 | 263 | s 268A(2) (42401-42404), report period ended 30 June 2026, lodged 31 August 2026 | JUST TRUE | JUST FALSE | , period count. Mine: "not later than 2 months after the end of that period" ends 31 August (the end of the month, because 30 June is the last day of June). Encoding: ends 30 August (same day of the month, P4). My own header convention in `ANSWERS.md` ("N months after D ends on the same day of the month") gives 30 August, so my scenario was not consistent with my own header; I keep the verdict AMBIGUOUS because the end-of-month reading is a recognised alternative. |
| 1 | 351 | s 273(5) (44044-44057), declaration 1 March 2026, offer 1 September 2026 ("for a period of 6 months from the date") | JUST TRUE | JUST FALSE | , period count. Mine: the 6 months run through 1 September. Encoding: through 31 August (the date counts as day 1, P10); checked by `#EVAL` with offers on 31 August (JUST TRUE) and 1 September (JUST FALSE). The same words "6 months from the date of the initial acquisition" in s 276(1) are counted through 1 September by the encoding (my 383 and 384 pass), so the encoding counts the same phrase two ways. |
| 1 | 398 | s 277(1A) (44679-44682), statement lodged 1 March 2026, offer 1 September 2026 ("within a period of 6 months from the date") | JUST TRUE | JUST FALSE | , period count. Same two counts as 351: mine through 1 September, encoding through 31 August (checked by `#EVAL`). |
| 2 | 78 | s133(4)(a) [28224] | JUST FALSE | NOTHING | The family member is herself a director: the text says '(not being himself or herself a director or chief executive officer of the corporation)'. Reading 1: the carve-out says no (JUST FALSE). Reading 2: the deeming is silent about that person (NOTHING). This is the case-by-case question '(other than X)'. |
| 2 | 88 | s134(1)(a) [28275] | JUST FALSE | NOTHING | Intentional breach of s133(1)(a)(ii) (shares in a related corporation) is outside the heavier tier of s134(1) (the tier lists (a)(i), (b)(i), (c)(i), (d)(i), (f)). Reading 1: the provision's own question is unmet, so JUST FALSE. Reading 2: unmet element of an offence, the text only says who is in tier (1), not that others are not: NOTHING. The brief names this split site. |
| 2 | 123 | s137(1) [28412] | JUST FALSE | NOTHING | A person who has not ceased to be a substantial shareholder: 'A person who ceases to be ... must give written notice'. Reading 1: the condition is unmet, so no duty (JUST FALSE). Reading 2: a duty whose condition is unmet is silent (NOTHING). Case-by-case question 'a duty whose if or where is unmet'. |
| 2 | 207 | s137G(1)(a) [28864] | JUST FALSE | NOTHING | A notice from a director about shares in a related corporation (s133(1)(a)(ii)), which s137G(1)(a) does not list. 'Where a corporation has been notified ... under ...' is a where-gate on a duty: periods ruling (b) says JUST FALSE; the encoding says NOTHING (its fork line). Case-by-case question. |
| 2 | 208 | s137G(1)(a) [28864] | JUST FALSE | NOTHING | Same as 207, for a notice about participatory interests (s133(1)(e)). |
| 2 | 218 | s137G(5)(d) [28931] | JUST FALSE | NOTHING | The corporation has committed no offence under s137G(3) or (4), and the officer caused the contravention: 'Where an offence has been committed by a corporation ..., any officer who ... must (d) if ...'. Reading 1: where-gate unmet, JUST FALSE (periods ruling (b)). Reading 2: unmet element of an offence, NOTHING. |
| 2 | 344 | s137ZD(1)(a) [30897] | JUST FALSE | NOTHING | A negligent (neither intentional nor reckless) contravention of s135: (a) is 'intentionally or recklessly contravened'. Reading 1: the provision's own question, unmet, JUST FALSE. Reading 2: unmet element of a contravention, NOTHING. The brief names this split site. |
| 2 | 353 | s137ZD(1)(c) [30897] | JUST FALSE | NOTHING | An officer who acted merely negligently: (c) needs 'intentionally or recklessly committed an act'. Same split as 344. |
| 2 | 398 | s138(6) [31398] | JUST FALSE | NOTHING | An advocate and solicitor who does not refuse to produce: 'who refuses ... is nevertheless obliged to give the name and address'. Reading 1: the relative clause is unmet, so no duty here (JUST FALSE). Reading 2: silent when the condition is unmet (NOTHING). Case-by-case question. |
| 2 | 429 | s139(10) [31480] | JUST FALSE | NOTHING | The Council has no reason to believe any breach or misconduct: 'Where the Council has reason to believe ..., the Council has power to enquire'. A 'where'-gated power: periods ruling (b) says JUST FALSE, the grant ruling says NOTHING (the brief names this split site). |
| 2 | 434 | s140(1) [31499] | JUST FALSE | NOTHING | A person who does intend to make a take-over offer and announces it: 'A person who has no intention ... must not give notice'. Reading 1: the prohibition's own question, unmet, JUST FALSE. Reading 2: a scope limit with no 'only' (ruling (c)) and the text is silent about someone who does intend: NOTHING. I lean to the encoding. |
| 2 | 438 | s140(2) [31503] | JUST FALSE | NOTHING | The person has reasonable grounds: 'must not make a take-over offer ... if the person has no reasonable or probable grounds'. Reading 1: an 'if' condition unmet gives JUST FALSE (Guide, worked example 1). Reading 2: a prohibition whose 'if' is unmet is silent (case-by-case 'a duty whose if or where is unmet'): NOTHING. |
| 2 | 442 | s140(3) [31509] | JUST FALSE | NOTHING | An officer of the corporation who is not in default: 'every officer of the corporation who is in default shall be guilty'. Reading 1: the element 'in default' is unmet, so no offence under this section (JUST FALSE). Reading 2: unmet element of an offence, NOTHING (the brief names this split site). |
| 3 | S27 | s197(2) [L34307] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S43 | s198(1) [L34405] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S44 | s198(1) [L34405] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S47 | s198(2) [L34428] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S54 | s199 [L34469] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S61 | s200(1)(b) [L34507] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S74 | s201(c) [L34558] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S76 | s201 [L34549] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S78 | s201A(1) [L34572] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S79 | s201A(1) [L34572] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S81 | s201A(2) [L34581] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S92 | s202(1)(a) [L34610] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S93 | s202(1)(c) [L34636] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S96 | s202(1) [L34605] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S117 | s204(2) [L34726] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 3 | S118 | s204(2) [L34726] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 3 | S145 | s209 [L34843] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S150 | s210(2) [L34873] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 3 | S213 | s218(2) [L35265] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S237 | s221(2) [L35523] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 3 | S292 | s232(1) [L35868] | JUST FALSE | NOTHING | two readings: a "may" gated by "with the consent of the Public Prosecutor": JUST FALSE (gate closed in the text's own words) or NOTHING (grant ruling; the encoding records SPLIT-SITE (ii) [CONSENT]) |
| 3 | S293 | s232(1) [L35866] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S327 | s234(1A)(a) [L36010] | JUST FALSE | NOTHING | two readings: unmet element of the s234(1A) liability: JUST FALSE ("if", as the same section answers JUST FALSE for the "if" profit gate of s234(1), S323 satisfied) or NOTHING (encoding: SPLIT-SITE (i), and the inner s234(1A)(a)/(b) answer NOTHING) |
| 3 | S328 | s234(1A)(b)(i) [L36022] | JUST FALSE | NOTHING | two readings: unmet element of the s234(1A) liability: JUST FALSE ("if", as the same section answers JUST FALSE for the "if" profit gate of s234(1), S323 satisfied) or NOTHING (encoding: SPLIT-SITE (i), and the inner s234(1A)(a)/(b) answer NOTHING) |
| 3 | S329 | s234(1A)(b)(ii) [L36031] | JUST FALSE | NOTHING | two readings: unmet element of the s234(1A) liability: JUST FALSE ("if", as the same section answers JUST FALSE for the "if" profit gate of s234(1), S323 satisfied) or NOTHING (encoding: SPLIT-SITE (i), and the inner s234(1A)(a)/(b) answer NOTHING) |
| 3 | S356 | s236(1) [L36223] | JUST FALSE | NOTHING | two readings: "may, after [the conviction/order] has been made final, fix a date": JUST FALSE (periods ruling (a)) or NOTHING (grant ruling; the encoding records SPLIT-SITE (ii) [AFTER]) |
| 3 | S358 | s236(1)(b) [L36216] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S359 | s236(1)(b) [L36217] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S387 | s236B(3) [L36382] | JUST FALSE | NOTHING | two readings: a "may" gated by "with the consent of the Public Prosecutor": JUST FALSE (gate closed in the text's own words) or NOTHING (grant ruling; the encoding records SPLIT-SITE (ii) [CONSENT]) |
| 3 | S402 | s236C(1)(a) [L36481] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S403 | s236C(1)(b) [L36484] | JUST FALSE | NOTHING | two readings: unmet element of an offence/contravention: JUST FALSE here, NOTHING in the encoding (recorded by it as SPLIT-SITE (i)) |
| 3 | S440 | s236H(1)(a) [L36989] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S443 | s236H(1) [L36996] | JUST FALSE | NOTHING | two readings: a "may" gated by "with the consent of the Public Prosecutor": JUST FALSE (gate closed in the text's own words) or NOTHING (grant ruling; the encoding records SPLIT-SITE (ii) [CONSENT]) |
| 3 | S462 | s236K(1) [L37258] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S463 | s236K(1)(b) [L37253] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S471 | s236L(1)(b) [L37306] | NOTHING | JUST FALSE | two readings: a "may" gated by "where/whenever": NOTHING (grant ruling, limit 1) or JUST FALSE (periods ruling (b)); the encoding took JUST FALSE and lists it as GRANT-GROUP [WHERE-LISTED] (limit 3 says list, not change) |
| 3 | S540 | s236L(10) [L37422] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 3 | S541 | s236L(10) [L37422] | JUST FALSE | NOTHING | two readings: "No proceedings ... after [event]" with the event not yet happened: JUST FALSE (periods ruling (a), the bar is stated in the text's own words) or NOTHING (an event, not a fixed period; the encoding marks MARGINAL-READING (b)) |
| 4 | 10 | s 239(1) "dealing in capital markets products", text line 37540-37542 | NOTHING | JUST FALSE | Product is a futures contract (not securities or securities-based derivatives): dealing under this definition? / Readings: (1) a "means" definition is closed, so a futures contract is outside it and the answer is JUST FALSE (the encoding); (2) the definition is limited in its own head to "in respect of capital markets products that are securities or securities-based derivatives contracts", a scope limit with no "only", so ruling (c) gives NOTHING (mine). |
| 4 | 44 | s 239(1) "underlying entity", text line 37711 | NOTHING | JUST FALSE | Direct offer of ordinary shares (not units): is the share-issuing entity an "underlying entity"? / Readings: (1) "means" definition closes it, so a direct share offer has no underlying entity and the answer is JUST FALSE (the encoding); (2) the definition is limited to "in relation to an offer of units of shares or debentures", a scope limit, so ruling (c) gives NOTHING (mine). |
| 4 | 88 | s 239A(2), text line 37920-37921 | NOTHING | JUST FALSE | Ordinary shares offered by a company: does 239A(2) say anything? / Readings: (1) "does not apply ... where (a)/(b)" with the where-limbs unmet gives JUST FALSE under ruling (b), and the encoding extends that to an offer that is not of business-trust units at all; (2) an ordinary share offer is outside the subsection's scope, so ruling (c) gives NOTHING (mine). |
| 4 | 120 | s 240(5), text line 38541-38543 | JUST FALSE | NOTHING | Offer in respect of an existing company: contravenes 240(5)? / Split site (i), an unmet element of a contravention. Readings: (1) the prohibition names only offers for an entity not yet formed, so for an existing entity the text says nothing (NOTHING, the encoding, limit on a prohibition in its own wording); (2) an existing entity is outside the contravention, so the answer is JUST FALSE (mine). |
| 4 | 158 | s 240(17), text line 38795-38797 | JUST FALSE | NOTHING | A clerk who is not knowingly a party to the circulation: guilty? / Split site (i), an unmet element of an offence. Readings: (1) "the person making the offer and every person who is knowingly a party" names who is liable and is silent on the rest, so NOTHING (the encoding); (2) a clerk who is not knowingly a party is outside the offence, so JUST FALSE (mine). |
| 4 | 213 | s 241(1A), text line 39140-39141 | JUST FALSE | NOTHING | Same, lodges 2026-03-16: may lodge? / Readings: (1) ruling (a), a period fixed in the text's own words (before the expiration of 24 months) gives JUST FALSE outside it (mine); (2) the Grant ruling, a "may" function whose "if" gate fails gives NOTHING (the encoding, which uses its gate NOTHING branch here). Lodging on 2026-03-16 is outside the 24 months under either count of the month. |
| 4 | 283 | s 242(9)(b), text line 39782-39783 | JUST TRUE | JUST FALSE | Same: in force on 2026-03-16 (day 14)? / Period count. The text says "for a period of 14 days from the day on which the interim stop order is served". Mine counts under P1 (the day of service is not counted), so served 2026-03-02 gives day 14 as 2026-03-16 and the order is in force. The encoding counts the 14 days beginning with the day of service (P10, day of service is day 1), so the last day is 2026-03-15 and it answers JUST FALSE on 2026-03-16. |
| 4 | 298 | s 243(3)(b), text line 39844-39846 | JUST FALSE | NOTHING | Offer of units in a business trust: is 243(3)(b) (issuer's finances) a required matter? / Case-by-case site (the paragraphs of 243(3)). Readings: (1) "in the case of an offer ... other than units ... in a business trust" excludes business trust units in its own words, so JUST FALSE (mine); (2) a paragraph that says what to disclose in one case is silent on the other cases, so NOTHING (the encoding). |
| 4 | 300 | s 243(3)(c), text line 39853-39861 | JUST FALSE | NOTHING | Underlying entity controlled by neither the offeror nor its related parties: required under (3)(c)? / Case-by-case site (the paragraphs of 243(3)). Readings: (1) "if the underlying entity is controlled by ..." is an "if" gate, so unmet gives JUST FALSE (mine); (2) the paragraph says what is required in that case and is silent otherwise, so NOTHING (the encoding). |
| 4 | 302 | s 243(3)(d), text line 39866-39877 | JUST FALSE | NOTHING | Offer of units of shares; neither the offeror nor any entity it controls has such obligations: required under (3)(d)? / Case-by-case site (the paragraphs of 243(3)). Readings: (1) "in the case of an offer of units ..., where (i) ... or (ii) ..." unmet where-limbs give JUST FALSE under ruling (b) (mine); (2) the paragraph states a requirement for one case and is silent on the rest, so NOTHING (the encoding). |
| 4 | 326 | s 245(1), text line 40067-40069 | JUST FALSE | NOTHING | Subscriptions accepted do not exceed the amount of the issue: contravenes 245(1)? / Split site (i), an unmet element of a contravention. Readings: (1) subscriptions not in excess of the issue are outside "must not accept or retain ... in excess", so JUST FALSE (mine); (2) a prohibition limited in its own wording says nothing outside it, so NOTHING (the encoding). |
| 4 | 342 | s 246(2)(b), text line 40158-40159 | JUST FALSE | NOTHING | Profile statement contains only immaterial extra information: breach? / Split site (i), an unmet element of a contravention. Readings: (1) only immaterial extra information is not "material information not in the prospectus", so the breach is JUST FALSE (mine); (2) the prohibition is limited to the three listed kinds of content and says nothing of anything else, so NOTHING (the encoding). |
| 4 | 405 | s 251(3)(b), text line 40525-40530 | JUST FALSE | NOTHING | Same but an application form is attached: does 251(3) shelter the dissemination? / Safe-harbour site stated with "may" and an "if" gate. Readings: (1) the Grant ruling, a "may" function whose "if" gate fails gives NOTHING (the encoding, which flags it GRANT-RULING (1)); (2) the clause is a shelter, a defence not proved, so JUST FALSE "this section gives no defence on these facts" (mine). Gate failed: an application form is attached. |
| 4 | 406 | s 251(3)(a)(iii), text line 40519-40523 | JUST FALSE | NOTHING | No bold statement on the front page: shelter? / Safe-harbour site stated with "may" and an "if" gate. Readings: (1) the Grant ruling, a "may" function whose "if" gate fails gives NOTHING (the encoding, which flags it GRANT-RULING (1)); (2) the clause is a shelter, a defence not proved, so JUST FALSE "this section gives no defence on these facts" (mine). Gate failed: no bold no-offer statement. |
| 4 | 407 | s 251(3)(c), text line 40532-40535 | JUST FALSE | NOTHING | No notice to recipients after registration: shelter? / Safe-harbour site stated with "may" and an "if" gate. Readings: (1) the Grant ruling, a "may" function whose "if" gate fails gives NOTHING (the encoding, which flags it GRANT-RULING (1)); (2) the clause is a shelter, a defence not proved, so JUST FALSE "this section gives no defence on these facts" (mine). Gate failed: no notice after registration. |
| 4 | 410 | s 251(4)(a)(ii), text line 40557-40562 | JUST FALSE | NOTHING | Oral material fails to state no offer may be made on its basis: sheltered? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Gate failed: no statement that no offer may be made on the basis of the material. |
| 4 | 413 | s 251(4)(b), text line 40582-40596 | NOTHING | JUST FALSE | Same material shown to retail investors in general: does 251(4)(b) shelter it? / Readings: (1) "for the sole purpose of equipping any of the following persons" is a closed list and a shelter not proved, so JUST FALSE for retail investors (the encoding); (2) the list has no "only" and the shelter is silent about people it does not name, so NOTHING (mine). |
| 4 | 418 | s 251(5)(b), text line 40626-40628 | JUST FALSE | NOTHING | PHS not lodged (240AA(1)(b) not complied with): sheltered by (5)(b)? / Readings: (1) "a person may disseminate ... (b) a product highlights sheet in respect of which ..." is a grant limited in its own wording, so NOTHING when the limit is not met (the encoding, consistent with the Grant ruling); (2) a shelter not proved gives JUST FALSE "no defence on these facts" (mine). |
| 4 | 422 | s 251(6), text line 40636 | JUST FALSE | NOTHING | Contains (a), (b), (c) and an indicative price: sheltered? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). The gate here is "if it contains only the following" with an indicative price added. |
| 4 | 425 | s 251(8)(c), text line 40692-40693 | JUST FALSE | NOTHING | Ad contains information not in the prospectus: sheltered? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Gate failed: the advertisement contains information not in the prospectus. |
| 4 | 426 | s 251(8)(d), text line 40695-40696 | JUST FALSE | NOTHING | Ad does not comply with the prescribed requirements: sheltered? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Gate failed: the prescribed requirements are not met. |
| 4 | 432 | s 251(9)(f)(iii), text line 40783-40785 | JUST FALSE | NOTHING | Report about the securities published by a person with an interest in the success of the issue: does (9)(f) shelter it? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Here the exclusion is in the text's own words ("a person other than" the four), and the publisher has an interest in the success of the issue. |
| 4 | 434 | s 251(9)(c)(ii), text line 40730-40731 | JUST FALSE | NOTHING | Same report but it refers indirectly to the offer: sheltered? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Gate failed: the report refers indirectly to the offer. |
| 4 | 437 | s 251(10)(b), text line 40831-40833 | JUST FALSE | NOTHING | Newspaper knew: sheltered by (10)? / Safe-harbour site. Readings: (1) the function states that the person "does not contravene (1)" and a failed gate under an "if"/"only" or an unproved defence gives JUST FALSE ("this section gives no defence on these facts"), my answer; (2) JUST FALSE on a function named "does not contravene (1)" would assert that the person does contravene (1), which the text never says, so the failed gate leaves it NOTHING (the encoding). Gate failed: the newspaper knew or had reason to suspect. |
| 4 | 446 | s 252(1), text line 40926 | JUST FALSE | NOTHING | The person making the offer himself (254(3)(a)): does 252(1) bind him? / Case-by-case site. Readings: (1) "(other than paragraph (a))" excludes the person making the offer in the text's own words, so JUST FALSE (mine); (2) the exclusion only limits who is bound and the function is then silent about him, so NOTHING (the encoding). |
| 4 | 447 | s 252(1), text line 40932-40935 | JUST FALSE | NOTHING | Becomes aware only after the offer closed: duty? / Duty site, unmet "if" gate. Readings: (1) "if the person becomes aware at any time after registration but before the close of the offer" and "the failure ... would have been materially adverse" are "if" gates, and the window is a period fixed in the text's own words, so JUST FALSE under ruling (a) and the "if" rule (mine); (2) the function reports whether the person notified, so when no duty arises it is silent and the answer is NOTHING (the encoding). Gate failed: the person became aware only after the offer closed. |
| 4 | 448 | s 252(1), text line 40932-40934 | JUST FALSE | NOTHING | Becomes aware before the prospectus is registered: duty? / Duty site, unmet "if" gate. Readings: (1) "if the person becomes aware at any time after registration but before the close of the offer" and "the failure ... would have been materially adverse" are "if" gates, and the window is a period fixed in the text's own words, so JUST FALSE under ruling (a) and the "if" rule (mine); (2) the function reports whether the person notified, so when no duty arises it is silent and the answer is NOTHING (the encoding). Gate failed: the person became aware before registration. |
| 4 | 449 | s 252(1), text line 40958-40959 | JUST FALSE | NOTHING | Failure to notify would not have been materially adverse: duty? / Duty site, unmet "if" gate. Readings: (1) "if the person becomes aware at any time after registration but before the close of the offer" and "the failure ... would have been materially adverse" are "if" gates, and the window is a period fixed in the text's own words, so JUST FALSE under ruling (a) and the "if" rule (mine); (2) the function reports whether the person notified, so when no duty arises it is silent and the answer is NOTHING (the encoding). Gate failed: the failure to notify would not have been materially adverse. |
| 4 | 462 | s 253(2), text line 41018-41022 | JUST FALSE | NOTHING | Same statement made with reasonable grounds: taken to be false or misleading? / Deeming or "is ... if" site. Readings: (1) the "if" rule gives JUST FALSE when the condition is not met (mine); (2) a deeming or "is reckless if" clause adds a sufficient case and is not "only if", so it is silent when unmet, NOTHING (the encoding). Here the statement about a future matter was made with reasonable grounds. |
| 4 | 464 | s 253(4)(b)(ii), text line 41041 | JUST FALSE | NOTHING | Offeror entity is not the issuer: is a proposed director of the issuer guilty under (b)(ii)? / Case-by-case site (the persons listed in 253(4)). Readings: (1) "if the entity is also the issuer" is an "if" gate, so JUST FALSE when the entity is not the issuer (mine); (2) the list names who is guilty and is silent on anyone else, so NOTHING (the encoding). |
| 4 | 468 | s 253(4)(d), text line 41060-41080 | JUST FALSE | NOTHING | Issue manager named with consent, merely negligent, no knowledge: guilty? / Case-by-case site and an unmet element of an offence. Readings: (1) paragraph (d) applies "if (i), (ii) or (iii)" and a merely negligent issue manager meets none, so JUST FALSE (mine); (2) the paragraph names who is guilty and is silent on the merely negligent, so NOTHING (the encoding, F47). |
| 4 | 475 | s 253(4)(g), text line 41116-41118 | JUST FALSE | NOTHING | Any other person who merely negligently makes it: guilty? / Case-by-case site and an unmet element of an offence. Readings: (1) "any other person who intentionally or recklessly makes the statement" excludes the merely negligent, so JUST FALSE (mine); (2) the paragraph names who is guilty and is silent on anyone else, so NOTHING (the encoding, F47). |
| 4 | 477 | s 253(5)(b), text line 41149-41156 | JUST FALSE | NOTHING | Put upon inquiry; made all reasonable inquiries; took the remedial action warranted: reckless? / Deeming or "is ... if" site. Readings: (1) the "if" rule gives JUST FALSE when the condition is not met (mine); (2) a deeming or "is reckless if" clause adds a sufficient case and is not "only if", so it is silent when unmet, NOTHING (the encoding). Here the person was put upon inquiry, made all reasonable inquiries and took the remedial action warranted. |
| 4 | 486 | s 254(1), text line 41197-41199 | JUST FALSE | NOTHING | Claimant suffered no loss: liable to compensate? / Elements of a civil liability. Readings: (1) the persons are liable to compensate "any person who suffers loss or damage as a result of" the statement, so a claimant with no loss is outside it and the answer is JUST FALSE (mine); (2) the limit is in the wording of the grant of liability and the text says nothing about a claimant with no loss, so NOTHING (the encoding, F51). |
| 4 | 514 | s 257(3), text line 41424-41432 | JUST FALSE | NOTHING | Allotment 2026-01-01; offer for sale 2026-07-02; whole consideration received: sufficient evidence under 257(3)? / Readings: (1) "if it is shown (a) ... within 6 months after the allotment; or (b) ... the whole consideration had not been received" is an "if" with a period fixed in the text's own words, so unmet gives JUST FALSE (mine); (2) an evidentiary rule says what is sufficient evidence and is silent on other ways to show the purpose, so NOTHING (the encoding, F56). The offer on 2026-07-02 is outside the 6 months after 2026-01-01 under P4 either way. |
| 4 | 520 | s 258(1), text line 41459-41460 | JUST FALSE | NOTHING | After allotment, are the moneys still required to be held on trust under 258(1)? / Readings: (1) "must, until the allotment, be held ..." is a time bound in the text's own words, so after allotment ruling (a) gives JUST FALSE (mine); (2) the function reports whether the person holds the moneys on trust, so after allotment the duty has ended and the function is silent, NOTHING (the encoding, F18). |
| 4 | 547 | s 259(9), text line 41605-41611 | JUST FALSE | NOTHING | Directors gave only an oral undertaking: deemed granted? / Deeming or "is ... if" site. Readings: (1) the "if" rule gives JUST FALSE when the condition is not met (mine); (2) a deeming or "is reckless if" clause adds a sufficient case and is not "only if", so it is silent when unmet, NOTHING (the encoding). Here the directors gave only an oral undertaking. |
| 4 | 581 | s 260(7C), text line 41786-41788 | JUST FALSE | NOTHING | Director of a trustee-manager who did not know: guilty under 260(7C)? / Split site (i), an unmet element of an offence. Readings: (1) a director who did not know is outside "knowingly contravenes or permits or authorises", so JUST FALSE (mine); (2) the offence names the guilty and is silent on a director without knowledge, so NOTHING (the encoding). |

### The `GAP` lines (60)

A `GAP` is a scenario the reader could not pose: no function answers it, or the function has no input for the point, or its type cannot say the answer. They are grouped by the reason, and none was repaired.

#### Operative text with no function of its own (inert by design, or one function covers several limbs) (15)

| group | scenario | provision | what the reader found |
| --- | --- | --- | --- |
| 1 | 197 | s 261(1A) (41840-41841) | NOTHING / no function asks whether s 268A is disapplied for a prescribed entity |
| 1 | 299 | s 272(1) (42649-42650), "(other than section 257)" | N / no function asks whether s 257 still applies to an offer exempt under s 272 |
| 2 | 43 | s132 [28091] | my expected: see ANSWERS.md #43 / the encoding: no function can be asked / the Authority's regulation-making power to extend Division 1 is not encoded (the encoding says: inert) |
| 2 | 232 | s137IA [29074] | my expected: see ANSWERS.md #232 / the encoding: no function can be asked / regulation-making power to extend Division 2 is not encoded (inert) |
| 2 | 305 | s137TA [30033] | my expected: see ANSWERS.md #305 / the encoding: no function can be asked / regulation-making power to extend Division 3 is not encoded (inert) |
| 2 | 383 | s137ZG [31038] | my expected: see ANSWERS.md #383 / the encoding: no function can be asked / Rules of Court: a rule-making power, not encoded |
| 3 | S496 | s238(1)(a) [L37470] | see ANSWERS.md / no function / s 238 (Rules of Court) has no function in the sfab modules |
| 3 | S497 | s238(2)(a) [L37484] | see ANSWERS.md / no function / s 238(2)(a) (Rules of Court) has no function in the sfab modules |
| 3 | S498 | s238(2)(c) [L37494] | see ANSWERS.md / no function / s 238(2)(c) (Rules of Court) has no function in the sfab modules |
| 3 | S499 | s238(1) [L37470] | see ANSWERS.md / no function / s 238 (Rules of Court) has no function in the sfab modules |
| 4 | 89 | s 239B, text line 37939-37944 | Authority thinks regulations necessary for the protection of investors, offer is of a prescribed kind: may modify the Division by regulations? / s 239B: the encoding has no function for the Authority's power to modify by regulations (its source marks it inert) |
| 4 | 137 | s 240(12), text line 38655-38658 | May the Authority publish a lodged prospectus for public information? / s 240(12): the encoding has no function for the Authority's power to publish a lodged prospectus (only for the offeror's duty to supply a copy) |
| 4 | 162 | s 240(20), text line 38823-38825 | Regulations under 240 may set a fine of up to $50,000: allowed? / s 240(20): no function for the regulation-making power (penalty cap $50,000) |
| 4 | 350 | s 247(3), text line 40187-40191 | Class exemption under 247(3), Authority has neither 247(2) opinion: may the Authority grant it? / s 247(3): no function asks whether a class exemption under (3) needs the (2) opinion; the 247(2) function is stated only for (1) |
| 4 | 358 | s 248(3), text line 40220-40223 | May the Authority require a minimum number of Singapore-resident directors to sign? / s 248(3): the Authority's power to require a minimum number of resident directors has no function (only the signing requirement is a function) |

#### The function exists but has no input for the point asked (43)

| group | scenario | provision | what the reader found |
| --- | --- | --- | --- |
| 1 | 234 | s 266(1) (42083-42100) | NOTHING / no function gives a penalty for a trustee's breach of s 266(1); the text states none |
| 1 | 356 | s 273(8A) (44079-44084) | NOTHING / no function takes the offer's paragraph, so an advertisement of an offer under paragraph (i) cannot be asked |
| 2 | 19 | s130(6) [27991] | my expected: see ANSWERS.md #19 / the encoding: no function can be asked / '136(1) is in the list' is a boolean input of the function, not a provision name; cannot be asked by section number |
| 2 | 20 | s130(6) [27991] | my expected: see ANSWERS.md #20 / the encoding: no function can be asked / '137E(6) is in the list' likewise a boolean input |
| 2 | 44 | s132(aa) [28091] | my expected: see ANSWERS.md #44 / the encoding: no function can be asked / same |
| 2 | 45 | s132(b) [28091] | my expected: see ANSWERS.md #45 / the encoding: no function can be asked / same |
| 2 | 46 | s132 [28091] | my expected: see ANSWERS.md #46 / the encoding: no function can be asked / same |
| 2 | 47 | s132 [28091] | my expected: see ANSWERS.md #47 / the encoding: no function can be asked / same |
| 2 | 59 | s133(1)(f) [28177] | my expected: see ANSWERS.md #59 / the encoding: no function can be asked / whether the Authority has prescribed the security is not an input; the matter is named 'the Authority prescribes' |
| 2 | 83 | s133(1) [28130] | my expected: see ANSWERS.md #83 / the encoding: no function can be asked / a holding in an unrelated company: the matter type has no such constructor; cannot be asked |
| 2 | 96 | s134(2) [28309] | my expected: see ANSWERS.md #96 / the encoding: no function can be asked / 'the person is neither director nor CEO' is not an input; the function is for the director/CEO |
| 2 | 139 | s137C(2) [28471] | my expected: see ANSWERS.md #139 / the encoding: no function can be asked / 'is $3 permitted' cannot be asked: the function returns the cap (2), which #138 asserts |
| 2 | 140 | s137C(2) [28471] | my expected: see ANSWERS.md #140 / the encoding: no function can be asked / 'is $1.50 permitted' cannot be asked; same |
| 2 | 141 | s137C(3) [28480] | my expected: see ANSWERS.md #141 / the encoding: no function can be asked / a 2.2-page copy: the function gives the per-page figure only (asserted in #467) |
| 2 | 163 | s137D(1) [28523] | my expected: see ANSWERS.md #163 / the encoding: no function can be asked / s136(3) is not a listed provision: the function takes one boolean 'contravened 135, 136(1) or (2), 137, 137A or 137B'; a provision cannot be named |
| 2 | 169 | s137E(1)(e) [28587] | my expected: see ANSWERS.md #169 / the encoding: no function can be asked / list membership of an order kind is a type (`s 137E(1) kind of order`), not a question |
| 2 | 170 | s137E(1) [28587] | my expected: see ANSWERS.md #170 / the encoding: no function can be asked / an order of imprisonment: no constructor, cannot be asked |
| 2 | 171 | s137E(1)(c) [28587] | my expected: see ANSWERS.md #171 / the encoding: no function can be asked / same as 169 |
| 2 | 235 | s137J(1)(a) [29110] | my expected: see ANSWERS.md #235 / the encoding: no function can be asked / whom the unitholder notifies (the trustee-manager) is not a question |
| 2 | 244 | s137K(3) [29223] | my expected: see ANSWERS.md #244 / the encoding: no function can be asked / 3 pages: the function gives per-page only (asserted in #468) |
| 2 | 262 | s137N(1) [29547] | my expected: see ANSWERS.md #262 / the encoding: no function can be asked / shares of an unrelated company: no matter type; cannot be asked |
| 2 | 306 | s137U(1)(a) [30076] | my expected: see ANSWERS.md #306 / the encoding: no function can be asked / whom the substantial unitholder of a REIT notifies (trustee AND responsible person) is not a question |
| 2 | 307 | s137U(1)(a) [30076] | my expected: see ANSWERS.md #307 / the encoding: no function can be asked / same |
| 2 | 316 | s137W(1)(i) [30222] | my expected: see ANSWERS.md #316 / the encoding: no function can be asked / list membership of an order kind is a type, not a question |
| 2 | 361 | s137ZD(3) [30958] | my expected: see ANSWERS.md #361 / the encoding: no function can be asked / a consent order of $30,000 under 'Despite subsection (2)': the function takes no amount |
| 2 | 382 | s137ZF [31031] | my expected: see ANSWERS.md #382 / the encoding: no function can be asked / the High Court's jurisdiction: no function; the function takes 'brought in a District Court' |
| 2 | 400 | s138(7) [31406] | my expected: see ANSWERS.md #400 / the encoding: no function can be asked / the Minister consulting the Council: the function is for the Authority; no input for another person |
| 2 | 426 | s139(9) [31474] | my expected: see ANSWERS.md #426 / the encoding: no function can be asked / imprisonment as a sanction: the function takes 'the sanction is one the Council decides to invoke'; no sanction type |
| 2 | 443 | s140(3) [31509] | my expected: see ANSWERS.md #443 / the encoding: no function can be asked / 'no minimum is stated' cannot be asked: the Penalty type has no minimum field |
| 3 | S83 | s201A(1) [L34572] | see ANSWERS.md / no function / s 201A(1) has one input merging "knowingly executed" with "an order for a derivatives contract"; an order for a security cannot be asked apart from a non-knowing execution |
| 3 | S103 | s203(2)(b) [L34701] | see ANSWERS.md / no function / s 203(2) merges the category with "whose securities are listed" in one input: a trustee-manager of an unlisted trust cannot be asked apart from a person in no category |
| 3 | S113 | s204(1) [L34723] | see ANSWERS.md / no function / s 204(1) states the maximum as a record; there is no function that asks whether a given fine is within it |
| 3 | S114 | s204(1) [L34724] | see ANSWERS.md / no function / s 204(1) states the maximum as a record; there is no function that asks whether a given term is within it |
| 3 | S139 | s208 [L34825] | see ANSWERS.md / no function / s 208 has one function, for s207 only; whether s208 exempts s209 cannot be asked |
| 3 | S241 | s222 [L35540] | see ANSWERS.md / no function / s 222 has one function, for 218(2) and 219(2) only; its application to a communication under 218(3) cannot be asked |
| 4 | 90 | s 239B, text line 37939-37940 | Authority does not think it necessary: may it modify under 239B? / s 239B: same |
| 4 | 163 | s 240(20), text line 38824-38825 | Regulation providing a fine of $60,000: allowed by 240(20)? / s 240(20): no function |
| 4 | 164 | s 240(20), text line 38824-38825 | Regulation providing imprisonment: allowed by 240(20)? / s 240(20): no function |
| 4 | 193 | s 240AB(3), text line 39008-39009 | May the Authority vary or revoke a condition of an exemption at any time? / s 240AB(3): the power to vary or revoke a condition is not a function (the encoding only answers whether a condition is in force) |
| 4 | 375 | s 249(1B), text line 40272-40276 | A member of the public with no role asks to inspect: must the issuer allow it? / s 249(1B): no function takes who asks to inspect (member, creditor, subscriber, or stranger) |
| 4 | 566 | s 260(4), text line 41718-41719 | Conditions satisfied before the 4 months expire: must moneys be repaid? / s 260(4): no function answers "must the moneys be repaid" (the function asks only whether they have been repaid) |
| 4 | 576 | s 260(7), text line 41741-41744 | Is the allotment in contravention voidable at the applicant's option? / s 260(7): no function answers whether the contravening allotment is voidable (the function asks only whether the option was exercised in time) |
| 4 | 579 | s 260(7B), text line 41770-41773 | Maximum fine for the offence in 260(7B)? / s 260(7B): no penalty function for the offence in 260(7B) (the text states no number) |

#### Repealed or deleted: a coverage row, no function (by design) (2)

| group | scenario | provision | what the reader found |
| --- | --- | --- | --- |
| 3 | S151 | s211 [L34888] | see ANSWERS.md / no function / s 211 is repealed: no function |
| 4 | 321 | s 244, text line 40062 | What does section 244 provide? / s 244: repealed, no function (the encoding needs none) |

The `SCENARIO` lines (18) are the readers' own mistakes; the encoding is unchanged by them.

## Split sites (not harmonised)

Each agent was asked to record, site by site and without harmonising with the others, two questions the Guide leaves to the encoder: (i) an unmet element of an offence or a contravention, `JUST FALSE` or `NOTHING`; (ii) a "may" gated by "where", "when", "upon", "on application" or "with the consent of", `JUST FALSE` (the periods ruling) or `NOTHING` (the grant ruling). Neither question is settled; the open one on the S1 bench card is the second.
A site is a branch line tagged `-- SPLIT-SITE (i)` or `(ii)` in a layer-1 module, and every site also has a fork line in its part's NOTES. **The counts below were made by a script over the merged folder, one site per tagged branch line, with the answer read from the code on that line; each part's own count agrees.** A grep for the tag over the whole folder finds more lines than there are sites, because comments and test files mention it.

| agent | (i) `NOTHING` | (i) `JUST FALSE` | (ii) `NOTHING` | (ii) `JUST FALSE` |
| --- | --- | --- | --- | --- |
| keel | 0 | 0 | 1 | 0 |
| sfaa | 62 | 0 | 16 | 2 |
| sfab | 43 | 24 | 26 | 9 |
| sfac | 43 | 8 | 0 | 8 |
| sfad | 0 | 12 | 0 | 12 |
| all | 148 | 44 | 43 | 31 |

That is 266 sites: 192 of type (i) and 74 of type (ii).
**The agents did not answer alike.** `sfaa` took `NOTHING` at 78 of its 80 sites (the two it answers `JUST FALSE` are the failed gates on a public body's power at s 139(6) and s 139(10), turned by the S1b ruling, 2026S1bC); `sfad` took `JUST FALSE` at all 12 of its type (i) sites; `sfac` took `JUST FALSE` at all 8 of its type (ii) sites; `sfab` is mixed at both kinds.
A reader who compares this encoding with another jurisdiction's should treat both kinds as places where the answer comes from the agent and not from the text. A ruling can be applied by flipping the tagged branch, site by site.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

This ruling answers split-site question (ii) for the pure gates of this encoding, the functions that stay Boolean after the protocol split.
The protocol-shaped sites wait for their re-encode as DEONTIC and keep limit 3 of the grant ruling until then, so the question stays open for them.
The parts that changed a site under it, and the sites, are named at the end of each part's `## The S1b ruling on failed gates (2026S1bC)` section in `notes/<part>-NOTES.md`: sfaa (s 139(6), s 139(10)) and sfad (s 282AA(1), s 281(1)).

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
sfac-tests-reader.l4                           0         3       0        0         0 |      0         3       0        0  same
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
TOTAL (100 modules)                            0      6293       0        0           |      0      6293       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 6,293 assertions satisfied over 100 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each agent read its own traces on both builds, and the lead re-read every part's traces against their `-- EXPECT` words and compared the outcomes of the two builds.

## What would need doing before the encoding is worth relying on

- A lawyer's reading of the fork registers and the marginal readings in `notes/<agent>-NOTES.md`; none has been ruled.
- The rest of the Act (above), the Take-over Code (which is not in the Act), and a decision on the two split-site questions.
- A check of this edition against the current consolidation, if one later than the version in force to 20 October 2026 exists.
- A seat audit, which has not been run on this folder.

## Source not official

The text this encoding quotes is a converter's rendering of an informal consolidation. No sentence here has been verified against the official text.
