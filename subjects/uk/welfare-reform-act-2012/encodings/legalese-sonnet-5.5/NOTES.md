# NOTES: Welfare Reform Act 2012 (United Kingdom), 2012 c. 5, whole Act with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written 2026-11-04 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel on the stable `l4` 1.6.98, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module also runs on the main build 1.6.108 with the same four counts.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`wra-core.l4`, `wra-definitions.l4` and their tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
4 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `wra1` (lines 2 to 517), `wra2` (lines 518 to 1343), `wra3` (lines 1344 to 1519), `wra4` (lines 1520 to 2474).
The lead agent verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the core identical to the keel's) and then merged them with a script; nothing in a part's modules was edited at the merge.
Every note a part wrote is kept, unchanged except that the lead's scratchpad path is replaced by a placeholder, as `notes/<part>-NOTES.md`, with its `PROGRESS.md`, `SEAMS.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the briefs each agent was given are `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `wra-seat.l4` and `wra-cases-seat.l4`, with one banner comment per part; the text under each banner is the part's, unchanged. Each part's questions are still those of its range of the text.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (`notes/<part>-SEAMS.md` lists what each part asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** A part that found the core lacking a type or field recorded it in its `NEEDS-CORE.md` and, where it needed it, declared its own type in its own module. The lead did not add them to the core: `wra4-NEEDS-CORE.md`.
- **Part-local types and helper names stay where they are.** A crude scan (`dupscan.py`, not shipped: backticked names at the start of a line, and `DECIDE` and `DECLARE` heads) of 1,441 defined names found none defined in more than one module.
- **The merge lost nothing:** the merged folder was gated as it stands, and its total is 4,475 = 1,101 (wra1) + 1,407 (wra2) + 812 (wra3) + 1,117 (wra4) + 38 (the keel's tests), the parts' own totals as the lead measured them.

## Where things are

| agent | text (lines of `ukpga-2012-5.txt`) | modules | assertions in its test modules | seat questions |
| --- | --- | --- | --- | --- |
| keel | 1 to 1 | 2 | 38 | 0 |
| wra1 | 2 to 517 | 7 | 902 | 48 |
| wra2 | 518 to 1343 | 9 | 1146 | 63 |
| wra3 | 1344 to 1519 | 12 | 529 | 69 |
| wra4 | 1520 to 2474 | 11 | 974 | 49 |
| seat cases, all parts | | 1 (`wra-cases-seat.l4`) | 886 | |

The seat layer is `wra-seat.l4` (229 `@export` questions in all) and `wra-cases-seat.l4`; every other module is layer 1, one module per run of sections, each with a tests module beside it.

## The source

The only source is `../../registers/source-bundle/ukpga-2012-5.txt`, a plain-text rendering made by a converter script from legislation.gov.uk (`ukpga/2012/5`, point-in-time version 2026-07-01).
It is not the official text, and nothing here is "verified against the official text".
`../../registers/source-bundle/ukpga-2012-5.meta.json` records that the revised text "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish".
A provision that appears to say two things may therefore be two extent versions, which is not a fork.
Licence: Crown copyright, Open Government Licence v3.0 (`../../registers/source-bundle/STUB-SOURCE-LICENSE.md`): "Contains public sector information licensed under the Open Government Licence v3.0."

## The seat

From the keel's notes:

The seat the parts serve is the individual: a person who claims, receives or is moved to Universal Credit, or who claims Personal Independence Payment, or whose benefits are capped (brief, "The subject and the sources").
No seat for an official: the Secretary of State, the tribunals and the rest appear in the core only as the other party to what the individual is owed or owes.

## What check.sh prints

Run as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` on the merged folder, exit 0, before the independent test pass was added:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wra-cases-seat.l4                              0       886       0        0         0 |      0       886       0        0  same
wra-core-tests.l4                              0        38       0        0         0 |      0        38       0        0  same
wra-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
wra-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra1-ch1-entitlement.l4                        0         0       0        0         0 |      0         0       0        0  same
wra1-ch2-responsibilities.l4                   0         0       0        0         0 |      0         0       0        0  same
wra1-ch3-general.l4                            0         0       0        0         0 |      0         0       0        0  same
wra1-sch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra1-sch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra1-sch5-6.l4                                 0         0       0        0         0 |      0         0       0        0  same
wra1-tests-ch1.l4                              0       171       0        0         0 |      0       171       0        0  same
wra1-tests-ch2.l4                              0       335       0        0         0 |      0       335       0        0  same
wra1-tests-ch3.l4                              0       103       0        0         0 |      0       103       0        0  same
wra1-tests-sch1.l4                             0        48       0        0         0 |      0        48       0        0  same
wra1-tests-sch2.l4                             0       116       0        0         0 |      0       116       0        0  same
wra1-tests-sch5-6.l4                           0       110       0        0         0 |      0       110       0        0  same
wra1-tests-three-valued.l4                     0        19       0        0         0 |      0        19       0        0  same
wra1-three-valued.l4                           0         0       0        0         0 |      0         0       0        0  same
wra2-part3.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra2-s44-jsa-commitment.l4                     0         0       0        0         0 |      0         0       0        0  same
wra2-s46-jsa-sanctions.l4                      0         0       0        0         0 |      0         0       0        0  same
wra2-s49-jsa-requirements.l4                   0         0       0        0         0 |      0         0       0        0  same
wra2-s50-esa-entitlement.l4                    0         0       0        0         0 |      0         0       0        0  same
wra2-s54-esa-commitment.l4                     0         0       0        0         0 |      0         0       0        0  same
wra2-s57-esa-requirements.l4                   0         0       0        0         0 |      0         0       0        0  same
wra2-s58-is-and-work.l4                        0         0       0        0         0 |      0         0       0        0  same
wra2-sch.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra2-tests-part3.l4                            0        96       0        0         0 |      0        96       0        0  same
wra2-tests-s44-jsa-commitment.l4               0        72       0        0         0 |      0        72       0        0  same
wra2-tests-s46-jsa-sanctions.l4                0       171       0        0         0 |      0       171       0        0  same
wra2-tests-s49-jsa-requirements.l4             0       277       0        0         0 |      0       277       0        0  same
wra2-tests-s50-esa-entitlement.l4              0        40       0        0         0 |      0        40       0        0  same
wra2-tests-s54-esa-commitment.l4               0        39       0        0         0 |      0        39       0        0  same
wra2-tests-s57-esa-requirements.l4             0       287       0        0         0 |      0       287       0        0  same
wra2-tests-s58-is-and-work.l4                  0       100       0        0         0 |      0       100       0        0  same
wra2-tests-sch.l4                              0        64       0        0         0 |      0        64       0        0  same
wra3-pt4-s77-84.l4                             0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s85-90.l4                             0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s92.l4                                0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s95.l4                                0         0       0        0         0 |      0         0       0        0  same
wra3-pt6-misc.l4                               0         0       0        0         0 |      0         0       0        0  same
wra3-pt7-final.l4                              0         0       0        0         0 |      0         0       0        0  same
wra3-sch10.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch11.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch12.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch13.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra3-sch9.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra3-tests-pt4-s77-84.l4                       0       184       0        0         0 |      0       184       0        0  same
wra3-tests-pt4-s85-90.l4                       0        73       0        0         0 |      0        73       0        0  same
wra3-tests-pt4-s92.l4                          0         8       0        0         0 |      0         8       0        0  same
wra3-tests-pt4-s95.l4                          0        20       0        0         0 |      0        20       0        0  same
wra3-tests-pt6-misc.l4                         0        79       0        0         0 |      0        79       0        0  same
wra3-tests-pt7-sch10.l4                        0        15       0        0         0 |      0        15       0        0  same
wra3-tests-sch11.l4                            0        49       0        0         0 |      0        49       0        0  same
wra3-tests-sch12.l4                            0        26       0        0         0 |      0        26       0        0  same
wra3-tests-sch13.l4                            0        16       0        0         0 |      0        16       0        0  same
wra3-tests-sch4.l4                             0        36       0        0         0 |      0        36       0        0  same
wra3-tests-sch9.l4                             0        23       0        0         0 |      0        23       0        0  same
wra4-regulative.l4                             0         0       0        0         0 |      0         0       0        0  same
wra4-s105-recovery.l4                          0         0       0        0         0 |      0         0       0        0  same
wra4-s120-taxcredits.l4                        0         0       0        0         0 |      0         0       0        0  same
wra4-ss106-112.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss113-116.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss117-119.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss121-126.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss127-129.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss130-134.l4                              0         0       0        0         0 |      0         0       0        0  same
wra4-ss96-97.l4                                0         0       0        0         0 |      0         0       0        0  same
wra4-ss98-104.l4                               0         0       0        0         0 |      0         0       0        0  same
wra4-tests-regulative.l4                       0         0       0        0         0 |      0         0       0        0  same
wra4-tests-s105-recovery.l4                    0       149       0        0         0 |      0       149       0        0  same
wra4-tests-s120-taxcredits.l4                  0       124       0        0         0 |      0       124       0        0  same
wra4-tests-ss106-112.l4                        0        71       0        0         0 |      0        71       0        0  same
wra4-tests-ss113-116.l4                        0        88       0        0         0 |      0        88       0        0  same
wra4-tests-ss117-119.l4                        0        97       0        0         0 |      0        97       0        0  same
wra4-tests-ss121-126.l4                        0        53       0        0         0 |      0        53       0        0  same
wra4-tests-ss127-129.l4                        0       110       0        0         0 |      0       110       0        0  same
wra4-tests-ss130-134.l4                        0       141       0        0         0 |      0       141       0        0  same
wra4-tests-ss96-97.l4                          0        94       0        0         0 |      0        94       0        0  same
wra4-tests-ss98-104.l4                         0        47       0        0         0 |      0        47       0        0  same
TOTAL (82 modules)                             0      4475       0        0           |      0      4475       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 4,475 assertions satisfied over 82 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each part read its own traces on both builds by hand (see its NOTES).

## What each part's notes hold

**keel**
- `notes/keel-NOTES.md:7` The source is not the official text
- `notes/keel-NOTES.md:15` What the keel covers
- `notes/keel-NOTES.md:24` Seat
- `notes/keel-NOTES.md:29` Coverage table (my range only)
- `notes/keel-NOTES.md:37` Fork register
- `notes/keel-NOTES.md:52` Marginal readings for a lawyer
- `notes/keel-NOTES.md:58` Jural relations
- `notes/keel-NOTES.md:66` Design of the core: what I chose, and what I assumed (not ruled by a lawyer)
- `notes/keel-NOTES.md:83` Findings
- `notes/keel-NOTES.md:103` Open questions for a domain expert
- `notes/keel-NOTES.md:109` What check.sh prints

**wra1**
- `notes/wra1-NOTES.md:7` The source is not the official text
- `notes/wra1-NOTES.md:15` My ranges, and the seat
- `notes/wra1-NOTES.md:22` Files
- `notes/wra1-NOTES.md:45` Coverage (wra1)
- `notes/wra1-NOTES.md:517` Fork register (wra1)
- `notes/wra1-NOTES.md:608` Jural relations (wra1)
- `notes/wra1-NOTES.md:762` Marginal readings for a lawyer (wra1)
- `notes/wra1-NOTES.md:895` Seams (wra1)
- `notes/wra1-NOTES.md:923` The seat layer (wra1-seat.l4, wra1-cases-seat.l4)
- `notes/wra1-NOTES.md:1004` What the text turns out to say (numbered findings)
- `notes/wra1-NOTES.md:1044` What the text does not answer
- `notes/wra1-NOTES.md:1048` Test method and its limits
- `notes/wra1-NOTES.md:1061` What the stable binary does not accept
- `notes/wra1-NOTES.md:1083` What check.sh prints
- `notes/wra1-NOTES.md:1141` peeked

**wra2**
- `notes/wra2-NOTES.md:21` What is in this folder
- `notes/wra2-NOTES.md:42` Coverage (wra2)
- `notes/wra2-NOTES.md:1036` Fork register (wra2)
- `notes/wra2-NOTES.md:1065` Jural relations (wra2)
- `notes/wra2-NOTES.md:1356` Marginal readings for a lawyer (wra2)
- `notes/wra2-NOTES.md:1400` Seams (wra2)
- `notes/wra2-NOTES.md:1416` What the text turns out to say
- `notes/wra2-NOTES.md:1460` What the text does not answer
- `notes/wra2-NOTES.md:1473` What the stable binary does not accept
- `notes/wra2-NOTES.md:1497` The seat (layer 2)
- `notes/wra2-NOTES.md:1519` What check.sh prints
- `notes/wra2-NOTES.md:1576` What went wrong
- `notes/wra2-NOTES.md:1582` Revision after the independent test review (4 November 2026)
- `notes/wra2-NOTES.md:1598` Notes on the notes

**wra3**
- `notes/wra3-NOTES.md:8` About the source
- `notes/wra3-NOTES.md:37` Coverage (wra3)
- `notes/wra3-NOTES.md:750` Fork register (wra3)
- `notes/wra3-NOTES.md:767` Jural relations (wra3)
- `notes/wra3-NOTES.md:1001` Marginal readings for a lawyer (wra3)
- `notes/wra3-NOTES.md:1070` Seams (wra3)
- `notes/wra3-NOTES.md:1085` What the text turns out to say (numbered findings)
- `notes/wra3-NOTES.md:1125` The seat layer (wra3)
- `notes/wra3-NOTES.md:1135` What check.sh prints

**wra4**
- `notes/wra4-NOTES.md:14` Files
- `notes/wra4-NOTES.md:29` Seat
- `notes/wra4-NOTES.md:63` Coverage (wra4)
- `notes/wra4-NOTES.md:1040` Fork register (wra4)
- `notes/wra4-NOTES.md:1109` Jural relations (wra4)
- `notes/wra4-NOTES.md:1251` Marginal readings for a lawyer (wra4)
- `notes/wra4-NOTES.md:1299` Seams (wra4)
- `notes/wra4-NOTES.md:1327` Findings (what the text turns out to say)
- `notes/wra4-NOTES.md:1356` What the stable binary does not accept
- `notes/wra4-NOTES.md:1378` What went wrong
- `notes/wra4-NOTES.md:1386` What check.sh prints

## What would need doing before the encoding is worth relying on

- A lawyer reads each part's coverage table, forks and marginal readings against the official text (this is a converter's rendering).
- The FALSE and NOTHING readings the parts flag for a lawyer are decided (the 2026-10-29 rule leaves two readings open; no ruling has been made).
- The seams are wired or kept as questions, and the NEEDS-CORE requests are taken into the core or refused.
- The prescribed figures and rates that the text leaves to regulations or orders are supplied as inputs; this encoding does not hold them unless a part's notes say so.

## Source not official

The quoted text is a plain-text rendering of the Act as deposited in `../../registers/source-bundle/`; it is not the official text. See 'The source' above and `SOURCE-LICENSE.md`.

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, briefs or tests wrote `ANSWERS.md` from the text of the Act alone before it opened any `.l4` file: 635 scenarios, spread over the four quarters of the text by line (Q1 164, Q2 181, Q3 166, Q4 124), and a sample of seat questions from every quarter.
It then wrote `tests-independent.l4`: 480 assertions, 260 of them on 148 distinct seat questions (Q1 36, Q2 47, Q3 35, Q4 30), covering 404 of the 635 scenarios, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the numbers in the comments of `tests-independent.l4` refer to it.
The author was given the family's rule for "no" and "not said" in its brief (see "Reading a result: FALSE and NOTHING" above) and wrote its expected values by it.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as first merged | 480 | 451 | 29 | 0 |
| after the encoder's repair below, before the reconciliation | 480 | 454 | 26 | 0 |
| after the reconciliation below | 479 | 479 | 0 | 0 |

**What the 29 first-run failures turned out to be.**

- **Three were one encoder defect, repaired; the author's assertions stand unchanged (S165, S166 and S168).**
  Employment and Support Allowance s 11E(1)(a) (text line 1020) puts a single person responsible for a child "aged at least 1 and under a prescribed age (which may not be less than 3)" in the work-focused-interview group.
  With the prescribed age unknown the encoding answered `NOTHING`, though the text bounds it: a child aged 1 or 2 is under every age that may be prescribed, and a child under 1 is not "aged at least 1" and falls under s 11D(2)(c) instead.
  The encoder changed only the unknown-age branch of `s 57 WRA2007 11E(1) the person falls within section 11E` (a child under 1 answers `JUST FALSE`, aged 1 or 2 `JUST TRUE`, aged 3 or more `NOTHING`); the group function, the 11D, 11E and 11F "may impose" functions and the seat questions take its answer and needed no change, and no function signature changed.
  It swept for the same shape (an unknown input bounded by the text, with the same answer inside the bound), found no other, and listed four near-misses as candidates in its notes.
  One of the encoder's own expected values changed with the repair: `wra2-tests-s57-esa-requirements.l4`, line 192, for a child aged 2 with the prescribed age unknown, went from `NOTHING` to `JUST TRUE`.
  It added 31 assertions of its own (19 in that tests module, 12 seat cases).
- **One was a limit of the encoding, kept as a `-- GAP` line (S77c).**
  s 26(2)(d) sanctions one who "ceases paid work or loses pay" by misconduct, or voluntarily and for no good reason.
  For a cessation of work with the disregard of s 26(5)(b) left unknown, the author expected `JUST TRUE`, because a cessation is not a loss of pay and the disregard cannot matter to it; the encoding folds the two into one kind and takes the disregard as an input, so it answers `NOTHING`.
  The author called it minor.
  The assertion is now a `-- GAP` comment quoting what the author wrote, so the file has 479 assertions.
- **Seven were one convention disagreement, reconciled to the encoding's `NOTHING` (S91, S232, S293b, S331, S332, S336b and S425).**
  Each is a condition stated in the text's own wording that the case fails: "regulations may make hardship payments where the award is reduced under section 26 or 27" (s 28(1)), "this section applies to a person who ... has made a claim expressly on the ground of terminal illness" (s 82(1)), "if regulations so provide" (s 103(2)(b)), "applies where ... fails to take reasonable steps" and "has not been charged ... or given a notice" (SSAA 115C(1)), "a penalty may be imposed where ... without reasonable excuse" (SSAA 115D(1)), and "guilty of an offence if ... which comes to the person by virtue of section 131(1), (3) or (4)" (s 132(1)).
  The author expected `JUST FALSE` (reading (a) of the 2026-10-29 rule: a failed condition is the text's no); the encoding tags these branches "NOTHING-kind (limited by its own wording)".
  Other branches of this same encoding take reading (a) and answer `JUST FALSE` for the same kind of wording (s 26(2) and ESA 11E(1) are two), so the parts do not apply one reading throughout.
  **This is the second of the two readings that the 2026-10-29 rule leaves for a lawyer, and these seven, with the inconsistency, are the first thing for a lawyer to look at.** No ruling has been made.
- **Five were genuine forks, reconciled to the encoding's answer (S9, S41, S329b, S175b and S175c).**
  S9: s 4(1)(a) asks for a person "at least 18 years old" and s 4(3) lets regulations set another minimum age for prescribed cases, so the encoding does not say that a 17-year-old fails outright.
  S41: whether an interview about housing costs is a "work-focused interview", which s 15(2) defines as one "for prescribed purposes relating to work or work preparation"; the author expected `NOTHING`, the encoding answers `JUST FALSE` (restated to that).
  S329b: s 115(2) changes only the number of days in SSAA 115A(5) (14 for 28), and the rest of that subsection is not in the text.
  S175b and S175c: s 58(2) names a category of "lone parents with a child under 5 ... to be included in regulations"; whether a lone parent whose youngest child is 5 or 6 is outside it, or only not placed in it by this provision, is not settled (the author first called these its own errors; the encoder's code comment gives the second reading).
  **Which reading is right is for a lawyer.**
- **Thirteen were the author's own scenarios, reconciled with the reason in the file (S162, S169b, S292b, S314b, S312, S398, S414, S424, S436, S437, SQ3-138(5)a, S579 and S583b).**
  The author conceded all of them.
  Most are the family's convention applied to a list or a condition the text does not close: a list introduced by "are" or "applies to" and not closed with "only" (S398, S414, S424), "may only ... if" as a necessary condition and not a sufficient one (S436, S437, S583b), and silence about days before a commencement date (S292b, S314b).
  The rest are scenarios that asked the wrong question of the right function (S162, S169b), took an exclusion not applying as a positive (S312), left how a limit is applied to the Secretary of State (SQ3-138(5)a) or derived an answer from silence (S579).
  Each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote.

**The gaps.**
231 of the 635 scenarios have no assertion, in eight groups, each kept as a `-- GAP` line at the end of the file with the scenario numbers and the author's reason (the author's partition: 28 + 8 + 7 + 4 + 9 + 72 + 28 + 75 = 231).
28 turn on the commencement rules of s 150(1), (2) and (4), which have no function; 8 on s 149 (extent), which has none; 7 on silences that no function has an input to express; 4 cannot be decided from the converted text, which lost a heading or an entry; 9 meet a type that cannot carry them (an enumeration missing a value, or a plain `BOOLEAN` that cannot say `NOTHING`); 72 are for provisions with no function, which the author could not tell was deliberate; and 28 ask what an amendment says, so there is no logic to run.
**The last 75 are the author's own gap and the largest honest hole in this pass:** a function exists for each and the author wrote no assertion for it (in 8 the expected answer is a value, such as a punishment or a day, and not yes or no, which may be why).

**What the author could not decide from the text** (for comparison with the fork register), in brief:
whether a 17-year-old fails s 4(1)(a) given s 4(3); whether a negative balance floors at zero (s 8(1)); how a period of months is counted when the end month lacks the start day's number, and whether "N days from X" excludes X (JSA ss 9(7)(a), 10(6)(a), 19B(5), and s 150(2)); whether a housing-costs interview is a work-focused interview (s 15(2)); lists introduced by "is" or "are" and not closed with "only" (ss 58(2), 84(2), 96(5A), 127(7), 128(2), 130(6), 132(2)); "applies where" and "applies to a person who" (SSAA 115C(1), 115D(1), s 82(1)); whether an s 23 interview can be required of an s 19 claimant; whether "an Act" in s 40 includes an Act of the Northern Ireland Assembly; which of the inserted caution limb (s 6B(1)(c), s 36A(1)(c)) and its repeal by s 121 governs; immigration detention against "detention in legal custody" (s 87); what follows the number in SSAA 115A(5); the prescribed age in ESA 11E(1)(a) (now decided by the repair above); whether ESA 11F(2) gives the power without ESA entitlement; the dates in ss 103(2) and 109(3), and "if regulations so provide"; whether a court proceeding is an "action" (Limitation Act 38(11) via s 108(3)); "may only make arrangements if" (CSA 4(2A)) and how the limit in CSA 9A(5) is applied; permission with conditions (CSA 9A(2)); and converter damage (Schedule 14 repeal groups lost their Act headings from line 3659, the Schedule 9 insertions into ITEPA are empty, and paragraph numbers are missing from Schedules 1, 2, 5, 6, 10 and 13, which the author cited by line).

**Independence, as far as it went.**
The author did not open `NOTES.md`, `PROGRESS.md` or any brief or `notes/` file, any other encoding, or any other run's directory.
It opened the modules to learn names and types only after `ANSWERS.md` was written, and after the run read function bodies and comments to diagnose failures (it saw the encoder's fork F-57-1 comment that way).
About 38 of its 480 assertions were written after the modules were open: 18 are tagged `SQ3-` or `SQ4-` and about 20 more are variants of numbered scenarios (S162b, S292b, S314b, S483b to d and the like); it took their expected values from the text and did not add them to `ANSWERS.md`.
After runs it changed arguments and never an expected value to match the encoding: S77 was split (the original is kept as S77c), S252 had its argument count fixed and S253 was added, S435 had one argument flipped because the scenario says "before accepting", S536 got parentheses, and `IMPORT wra3-sch13` was added.
After its context was compacted, the harness attached to it, unasked, the full text of three files from the lead's working directory that it had not opened: the "Independent test pass" write-ups of two other encodings and a shipping script.
The two write-ups discuss the same question of "no" against "not said" as its disagreement groups.
The author says it did not use them, that its expected values and failure groups were fixed before they arrived, and that two things were done after (re-checking that the 29 failures matched the run, and partitioning the 231 gaps), neither helped by them; it offered to move four borderline failures (S232, S331, S332, S336b) from "the encoding is wrong" to "arguable", and the lead has treated those four as convention disagreements on its own reading of the text.
The encoder of the part that was repaired (the one of ESA 11E) was given the same kind of attachment after its own compaction, and says it used none of it and had fixed its expected values for 11E(1) from text line 1020 before.
The harness also loaded user-level instructions and a memory index into the author's context at the start, and a 2 KB preview of an oversized tool output; the author opened no memory file.
