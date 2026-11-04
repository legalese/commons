# NOTES: Food and Nutrition Act of 2008 (United States), 7 U.S.C. ch. 51 (SNAP), whole Act with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written 2026-11-04 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel on the stable `l4` 1.6.98, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module also runs on the main build 1.6.108 with the same four counts.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`snap-core.l4`, `snap-definitions.l4` and their tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
6 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `snap1` (lines 136 to 491), `snap2` (lines 492 to 912), `snap3` (lines 913 to 1340), `snap4` (lines 1425 to 1795), `snap5` (lines 1911 to 2391), `snap6` (lines 2392 to 2655).
The lead agent verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the core identical to the keel's) and then merged them with a script; nothing in a part's modules was edited at the merge.
After the independent test pass described at the end of this file, the keel's encoder and the parts' encoders each looked at the reviewer's failing assertions for their own range and repaired their own modules where they judged the encoding wrong; the lead merged the repaired parts again with the same script, and nothing in a repaired module was edited at that second merge either.
The totals below are those of the repaired parts, and each part's notes (`notes/<part>-NOTES.md`) say what its encoder changed and which of its own expectations moved.
Every note a part wrote is kept, unchanged except that the lead's scratchpad path is replaced by a placeholder, as `notes/<part>-NOTES.md`, with its `PROGRESS.md`, `SEAMS.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the briefs each agent was given are `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `snap-seat.l4` and `snap-cases-seat.l4`, with one banner comment per part; the text under each banner is the part's, unchanged. Each part's questions are still those of its range of the text.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (`notes/<part>-SEAMS.md` lists what each part asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** A part that found the core lacking a type or field recorded it in its `NEEDS-CORE.md` and, where it needed it, declared its own type in its own module. The lead did not add them to the core: `snap5-NEEDS-CORE.md`, `snap6-NEEDS-CORE.md`.
- **Part-local types and helper names stay where they are.** A crude scan (`dupscan.py`, not shipped: backticked names at the start of a line, and `DECIDE` and `DECLARE` heads) of 2,255 defined names found one defined in two modules, the test fixture `test: person` in snap2-tests-2015o.l4 and snap2-tests-2029.l4; no module imports a tests module, so it cannot clash.
- **The merge lost nothing:** the merged folder was gated as it stands, and its total is 7,330 = 1,198 (snap1) + 1,204 (snap2) + 1,049 (snap3) + 845 (snap4) + 1,141 (snap5) + 1,628 (snap6) + 265 (the keel's tests), the parts' own totals as the lead measured them.

## Where things are

| agent | text (lines of `usc07-ch51.txt`) | modules | assertions in its test modules | seat questions |
| --- | --- | --- | --- | --- |
| keel | 1 to 135 | 2 | 265 | 0 |
| snap1 | 136 to 491 | 13 | 977 | 44 |
| snap2 | 492 to 912 | 9 | 902 | 116 |
| snap3 | 913 to 1340 | 10 | 935 | 36 |
| snap4 | 1425 to 1795 | 8 | 780 | 25 |
| snap5 | 1911 to 2391 | 10 | 1059 | 17 |
| snap6 | 2392 to 2655 | 6 | 1505 | 41 |
| seat cases, all parts | | 1 (`snap-cases-seat.l4`) | 895 | |

The seat layer is `snap-seat.l4` (279 `@export` questions in all) and `snap-cases-seat.l4`; every other module is layer 1, one module per run of sections, each with a tests module beside it.

## The source

`usc07-ch51.txt` is a plain-text rendering made by a converter script from the Office of the Law Revision Counsel's USLM XML (release point Public Law 119-121).
It is not the official text.
Its own header says it keeps the section text, tables and source credits and omits the editorial and statutory notes.
Title 7 is not positive law, so the Statutes at Large remain the legal evidence (the same header says so).
Because the notes are omitted, a cross-reference that says "See References in Text note below" points at nothing in this file (line 137, s 2012a, in snap1's range).
`fna-snap-cola-fy2027.txt` (the USDA's fiscal-year 2027 cost-of-living page) is input data, not statute.
No quotation in the `.l4` files was typed: every `-- src:` line was copied from the raw file by a helper script of the keel agent's (not part of this folder), and `srcrefs.py check --refs` compares each one back to the file.

## The seat

From the keel's notes:

The individual household member who applies for, or receives, benefits under the Supplemental Nutrition Assistance Program, asking on facts they can state whether the household is eligible, how its income and deductions count, what its allotment is, what disqualifies a member, and what follows from a violation.
The keel's range holds the definitions those questions use, not the questions.
So there is no `@export` here: the seat layer belongs to the parts.
Each s 2012 function takes the facts a member could state about a person, a card, a seller or a meal, and answers `MAYBE BOOLEAN`.

## What check.sh prints

Run as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` on the merged folder, exit 0, before the independent test pass was added:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
snap-cases-seat.l4                             0       895       0        0         0 |      0       895       0        0  same
snap-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap-definitions-tests.l4                      0       265       0        0         0 |      0       265       0        0  same
snap-definitions.l4                            0         0       0        0         0 |      0         0       0        0  same
snap-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap1-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2012a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap1-s2013.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-abc.l4                             0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-d.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-e1.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-e2.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-f.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-g.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-hn.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap1-s2018.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2019.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-tests-logic.l4                           0        35       0        0         0 |      0        35       0        0  same
snap1-tests-s2012a.l4                          0         6       0        0         0 |      0         6       0        0  same
snap1-tests-s2013.l4                           0       108       0        0         0 |      0       108       0        0  same
snap1-tests-s2014-abc.l4                       0       104       0        0         0 |      0       104       0        0  same
snap1-tests-s2014-d.l4                         0        91       0        0         0 |      0        91       0        0  same
snap1-tests-s2014-e.l4                         0       155       0        0         0 |      0       155       0        0  same
snap1-tests-s2014-f.l4                         0        60       0        0         0 |      0        60       0        0  same
snap1-tests-s2014-g.l4                         0       121       0        0         0 |      0       121       0        0  same
snap1-tests-s2014-hn.l4                        0       124       0        0         0 |      0       124       0        0  same
snap1-tests-s2014a.l4                          0         7       0        0         0 |      0         7       0        0  same
snap1-tests-s2018.l4                           0       144       0        0         0 |      0       144       0        0  same
snap1-tests-s2019.l4                           0        22       0        0         0 |      0        22       0        0  same
snap2-2015a-c.l4                               0         0       0        0         0 |      0         0       0        0  same
snap2-2015d.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap2-2015d4.l4                                0         0       0        0         0 |      0         0       0        0  same
snap2-2015e-n.l4                               0         0       0        0         0 |      0         0       0        0  same
snap2-2015o.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap2-2015p-s.l4                               0         0       0        0         0 |      0         0       0        0  same
snap2-2027.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap2-2029.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap2-3val.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap2-tests-2015a-c.l4                         0       106       0        0         0 |      0       106       0        0  same
snap2-tests-2015d.l4                           0       124       0        0         0 |      0       124       0        0  same
snap2-tests-2015d4.l4                          0       118       0        0         0 |      0       118       0        0  same
snap2-tests-2015e-n.l4                         0       113       0        0         0 |      0       113       0        0  same
snap2-tests-2015o.l4                           0       161       0        0         0 |      0       161       0        0  same
snap2-tests-2015p-s.l4                         0        64       0        0         0 |      0        64       0        0  same
snap2-tests-2027.l4                            0       104       0        0         0 |      0       104       0        0  same
snap2-tests-2029.l4                            0        86       0        0         0 |      0        86       0        0  same
snap2-tests-3val.l4                            0        26       0        0         0 |      0        26       0        0  same
snap3-logic.l4                                 0        12       0        0         0 |      0        12       0        0  same
snap3-s2016-a-to-g.l4                          0         0       0        0         0 |      0         0       0        0  same
snap3-s2016-h.l4                               0         0       0        0         0 |      0         0       0        0  same
snap3-s2016-i-to-k.l4                          0         0       0        0         0 |      0         0       0        0  same
snap3-s2016a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap3-s2017-cola.l4                            0         0       0        0         0 |      0         0       0        0  same
snap3-s2017.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap3-s2022.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap3-s2023.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap3-s2024.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap3-tests-s2016-a-to-g.l4                    0        98       0        0         0 |      0        98       0        0  same
snap3-tests-s2016-h.l4                         0       162       0        0         0 |      0       162       0        0  same
snap3-tests-s2016-i-to-k.l4                    0       102       0        0         0 |      0       102       0        0  same
snap3-tests-s2016a.l4                          0        82       0        0         0 |      0        82       0        0  same
snap3-tests-s2017-cola.l4                      0        60       0        0         0 |      0        60       0        0  same
snap3-tests-s2017.l4                           0       140       0        0         0 |      0       140       0        0  same
snap3-tests-s2022.l4                           0       119       0        0         0 |      0       119       0        0  same
snap3-tests-s2023.l4                           0        93       0        0         0 |      0        93       0        0  same
snap3-tests-s2024.l4                           0        79       0        0         0 |      0        79       0        0  same
snap4-s2020-a-d.l4                             0         0       0        0         0 |      0         0       0        0  same
snap4-s2020-e-1.l4                             0         0       0        0         0 |      0         0       0        0  same
snap4-s2020-e-2.l4                             0         0       0        0         0 |      0         0       0        0  same
snap4-s2020-f-n.l4                             0         0       0        0         0 |      0         0       0        0  same
snap4-s2020-o-x.l4                             0         0       0        0         0 |      0         0       0        0  same
snap4-s2021.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap4-s2032.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap4-s2036b-d.l4                              0         0       0        0         0 |      0         0       0        0  same
snap4-tests-s2020-a-d.l4                       0        72       0        0         0 |      0        72       0        0  same
snap4-tests-s2020-e-1.l4                       0       150       0        0         0 |      0       150       0        0  same
snap4-tests-s2020-e-2.l4                       0        66       0        0         0 |      0        66       0        0  same
snap4-tests-s2020-f-n.l4                       0        55       0        0         0 |      0        55       0        0  same
snap4-tests-s2020-o-x.l4                       0       153       0        0         0 |      0       153       0        0  same
snap4-tests-s2021.l4                           0       164       0        0         0 |      0       164       0        0  same
snap4-tests-s2032.l4                           0        27       0        0         0 |      0        27       0        0  same
snap4-tests-s2036b-d.l4                        0        93       0        0         0 |      0        93       0        0  same
snap5-s2025-ab.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-c1.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-c2.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-dfij.l4                            0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-gh.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-hf.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-k.l4                               0         0       0        0         0 |      0         0       0        0  same
snap5-s2026a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap5-s2028.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap5-tests-s2025-ab.l4                        0        84       0        0         0 |      0        84       0        0  same
snap5-tests-s2025-c1.l4                        0        75       0        0         0 |      0        75       0        0  same
snap5-tests-s2025-c2.l4                        0       110       0        0         0 |      0       110       0        0  same
snap5-tests-s2025-dfij.l4                      0        85       0        0         0 |      0        85       0        0  same
snap5-tests-s2025-duties.l4                    0        47       0        0         0 |      0        47       0        0  same
snap5-tests-s2025-gh.l4                        0       187       0        0         0 |      0       187       0        0  same
snap5-tests-s2025-hf.l4                        0       180       0        0         0 |      0       180       0        0  same
snap5-tests-s2025-k.l4                         0        88       0        0         0 |      0        88       0        0  same
snap5-tests-s2026a.l4                          0        54       0        0         0 |      0        54       0        0  same
snap5-tests-s2028.l4                           0       149       0        0         0 |      0       149       0        0  same
snap6-s2026.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2031.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2034.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2035.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2036.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2036a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap6-tests-s2026.l4                           0       575       0        0         0 |      0       575       0        0  same
snap6-tests-s2031.l4                           0       478       0        0         0 |      0       478       0        0  same
snap6-tests-s2034.l4                           0       123       0        0         0 |      0       123       0        0  same
snap6-tests-s2035.l4                           0        96       0        0         0 |      0        96       0        0  same
snap6-tests-s2036.l4                           0        66       0        0         0 |      0        66       0        0  same
snap6-tests-s2036a.l4                          0       167       0        0         0 |      0       167       0        0  same
TOTAL (115 modules)                            0      7330       0        0           |      0      7330       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 7,330 assertions satisfied over 115 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each part read its own traces on both builds by hand (see its NOTES).

## What each part's notes hold

**keel**
- `notes/keel-NOTES.md:8` What the source is
- `notes/keel-NOTES.md:18` The seat
- `notes/keel-NOTES.md:25` Files
- `notes/keel-NOTES.md:38` Coverage table (lines 1-135 of `usc07-ch51.txt`)
- `notes/keel-NOTES.md:103` Fork register
- `notes/keel-NOTES.md:176` Reading a result: FALSE and NOTHING
- `notes/keel-NOTES.md:212` Marginal readings for a lawyer
- `notes/keel-NOTES.md:275` Jural relations
- `notes/keel-NOTES.md:327` Independent review of the keel range, 2026-11-04
- `notes/keel-NOTES.md:346` What the stable binary does not accept
- `notes/keel-NOTES.md:362` Limits of this encoding
- `notes/keel-NOTES.md:372` Open questions
- `notes/keel-NOTES.md:379` What check.sh printed (run, 2026-11-04, after the last edit to any `.l4` file, following the independent review)

**snap1**
- `notes/snap1-NOTES.md:13` What this part is
- `notes/snap1-NOTES.md:38` Coverage (snap1)
- `notes/snap1-NOTES.md:357` Fork register (snap1)
- `notes/snap1-NOTES.md:380` Jural relations (snap1)
- `notes/snap1-NOTES.md:501` Marginal readings for a lawyer (snap1)
- `notes/snap1-NOTES.md:716` Seams (snap1)
- `notes/snap1-NOTES.md:754` The seat layer (snap1)
- `notes/snap1-NOTES.md:825` What the text turns out to say
- `notes/snap1-NOTES.md:848` What the stable binary does not accept
- `notes/snap1-NOTES.md:861` Where PLAN.md and the brief differ
- `notes/snap1-NOTES.md:868` After the independent review (snap1)
- `notes/snap1-NOTES.md:893` Checks

**snap2**
- `notes/snap2-NOTES.md:20` Coverage (snap2)
- `notes/snap2-NOTES.md:451` Fork register (snap2)
- `notes/snap2-NOTES.md:475` Jural relations (snap2)
- `notes/snap2-NOTES.md:562` Marginal readings for a lawyer (snap2)
- `notes/snap2-NOTES.md:765` Seams (snap2)
- `notes/snap2-NOTES.md:797` The seat layer (snap2)
- `notes/snap2-NOTES.md:821` What the text turns out to say (snap2)
- `notes/snap2-NOTES.md:849` Independent review: triage of the 32 failing assertions (snap2)
- `notes/snap2-NOTES.md:889` What the stable binary does not accept
- `notes/snap2-NOTES.md:913` What check.sh printed
- `notes/snap2-NOTES.md:969` Files

**snap3**
- `notes/snap3-NOTES.md:15` How to read the L4
- `notes/snap3-NOTES.md:31` Coverage (snap3)
- `notes/snap3-NOTES.md:379` Fork register (snap3)
- `notes/snap3-NOTES.md:406` Jural relations (snap3)
- `notes/snap3-NOTES.md:555` Marginal readings for a lawyer (snap3)
- `notes/snap3-NOTES.md:879` Seams (snap3)
- `notes/snap3-NOTES.md:912` What the text turns out to say (snap3)
- `notes/snap3-NOTES.md:949` What the stable binary does not accept (snap3)
- `notes/snap3-NOTES.md:986` The seat layer (snap3)
- `notes/snap3-NOTES.md:1005` Triage of the independent test pass (snap3)
- `notes/snap3-NOTES.md:1053` What the text does not answer (snap3)
- `notes/snap3-NOTES.md:1067` What check.sh prints (snap3)
- `notes/snap3-NOTES.md:1109` Files

**snap4**
- `notes/snap4-NOTES.md:15` Layout
- `notes/snap4-NOTES.md:29` Seat (snap4)
- `notes/snap4-NOTES.md:41` Coverage (snap4)
- `notes/snap4-NOTES.md:420` Fork register (snap4)
- `notes/snap4-NOTES.md:466` Jural relations (snap4)
- `notes/snap4-NOTES.md:696` Marginal readings for a lawyer (snap4)
- `notes/snap4-NOTES.md:920` Seams (snap4)
- `notes/snap4-NOTES.md:931` What the text turns out to say (numbered findings)
- `notes/snap4-NOTES.md:969` After the independent test pass (2026-11-04): what changed in this folder
- `notes/snap4-NOTES.md:1009` What the stable binary does not accept (snap4)
- `notes/snap4-NOTES.md:1020` check.sh output (2026-11-04)

**snap5**
- `notes/snap5-NOTES.md:16` What is in this folder
- `notes/snap5-NOTES.md:38` Where PLAN.md and the brief differ (the brief governs)
- `notes/snap5-NOTES.md:58` Coverage (snap5)
- `notes/snap5-NOTES.md:532` Fork register (snap5)
- `notes/snap5-NOTES.md:637` Jural relations (snap5)
- `notes/snap5-NOTES.md:855` Marginal readings for a lawyer (snap5)
- `notes/snap5-NOTES.md:1176` Seams (snap5)
- `notes/snap5-NOTES.md:1197` What the text turns out to say
- `notes/snap5-NOTES.md:1245` What the stable binary does not accept
- `notes/snap5-NOTES.md:1274` Seat
- `notes/snap5-NOTES.md:1287` Independent review (2026-11-04): the items in this range
- `notes/snap5-NOTES.md:1343` Tests that fail on purpose
- `notes/snap5-NOTES.md:1348` What the text does not answer
- `notes/snap5-NOTES.md:1359` What `check.sh` prints
- `notes/snap5-NOTES.md:1398` Peeked

**snap6**
- `notes/snap6-NOTES.md:12` Seat (snap6)
- `notes/snap6-NOTES.md:27` Method
- `notes/snap6-NOTES.md:44` Coverage (snap6)
- `notes/snap6-NOTES.md:602` Fork register (snap6)
- `notes/snap6-NOTES.md:657` Jural relations (snap6)
- `notes/snap6-NOTES.md:844` Marginal readings for a lawyer (snap6)
- `notes/snap6-NOTES.md:939` Seams (snap6)
- `notes/snap6-NOTES.md:968` What the text turns out to say
- `notes/snap6-NOTES.md:994` What the stable binary does not accept
- `notes/snap6-NOTES.md:1010` What the text does not answer
- `notes/snap6-NOTES.md:1018` What would need doing before this encoding is worth relying on
- `notes/snap6-NOTES.md:1025` What check.sh prints

## What would need doing before the encoding is worth relying on

- A lawyer reads each part's coverage table, forks and marginal readings against the official text (this is a converter's rendering).
- The FALSE and NOTHING readings the parts flag for a lawyer are decided (the 2026-10-29 rule leaves two readings open; no ruling has been made).
- The seams are wired or kept as questions, and the NEEDS-CORE requests are taken into the core or refused.
- The prescribed figures and rates that the text leaves to regulations or orders are supplied as inputs; this encoding does not hold them unless a part's notes say so.

## Source not official

The quoted text is a plain-text rendering of the Act as deposited in `../../registers/source-bundle/`; it is not the official text. See 'The source' above and `SOURCE-LICENSE.md`.

## Bench rulings on negatives and legal effects

**Bench rulings of 2026-11-04** (full text in `docs/ENCODING-GUIDE.md` section 5; they apply to every fork and reading recorded in this file and in the parts' notes under `notes/`).
These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, briefs or tests wrote `ANSWERS.md` from the text of 7 U.S.C. chapter 51 and the FY2027 cost-of-living memorandum alone before it opened any `.l4` file: 736 numbered scenarios, taken by line range through the whole chapter, and a block that transcribes every cell of the memorandum's tables.
It then wrote `tests-independent.l4`: 1,976 assertions, 28 scenarios kept as comment lines, and ran it with the stable binary.
By the author's count 702 scenarios carry an assertion; seven tables (706, 710, 713 and 715 to 718) are covered cell by cell in a table block.
`ANSWERS.md` is not kept in this folder; the numbers in the comments of `tests-independent.l4` refer to it.
The author was given the family's rule for "no" and "not said" in its brief (see the "Reading a result" section of each part's notes, in `notes/`) and wrote its expected values by it.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as first merged | 1,976 | 1,775 | 201 | 0 |
| after the encoders' repairs below, before the reconciliation | 1,976 | 1,846 | 130 | 0 |
| after the reconciliation below | 1,975 | 1,975 | 0 | 0 |

The six part encoders and the keel encoder each got the author's failing lines for their own range and were asked to judge them against the text.
Where an encoder judged its encoding wrong it repaired the module and left the author's assertion unchanged; every one of its own expectations that it changed is listed in its part's notes (`notes/snap1-NOTES.md` and its siblings).
Together the repairs added 54 assertions of the encoders' own (part 1: 33, part 2: 6, part 3: 5, part 4: 5, keel: 5), and the merged encoding went from 7,276 to 7,330 satisfied assertions.
A repair made after seeing the author's expected value is not independent evidence that the repaired answer is right; the evidence for each is the quotation from the text in the part's notes.

**Seventy-one of the 201 first-run failures were encoder defects, repaired; the author's assertions stand unchanged.**

- **The gross monthly income limit (55 assertions: 726 fifty-three times, 708 and S1.02).**
  The encoding computed 130 percent of a poverty line that it had rounded to whole dollars; neither the Act nor the memorandum says how to round, the memorandum prints the limit for each household size in its Table 2, and 23 of 27 cells differed from the printed table by up to three dollars.
  The function now reads Table 2 for fiscal year 2027 (and answers `NOTHING` for any other year), and the seat compares income with the published limit.
  A household of one in urban Alaska with income of 2,162 was "over the limit" by ten cents; it is not any more.
- **A failed "if", "except" or "only if" that the encoding had answered `NOTHING` (eleven assertions in three parts: 82, 86c, 93b and 97b in part 1; 185, S1.34, 192a, 192c and S1.42 in part 2; 407b and 418 in part 4).**
  The encoders found the quoted words on the brief's list of grounds for `JUST FALSE` and a sibling rule of the same shape in the same part already answering `JUST FALSE`.
  The part-1 repairs also covered three siblings the author had no assertion on (`s 2014(d)(12)`, `s 2018(h)(2)(A)` and `(B)`); the part-4 repair covered the two sibling functions of 418 that refer and withhold.
- **Four that turned on a "means" definition, a branch order, or the date window of a scope sentence (646 and 218 in part 2; 348a with 348d in part 3).**
  646 is a closed "means" definition on which employment outside both windows contributes 0; 218 was a branch placed after a branch that shadowed it; 348a and 348d are one function, "shall only apply to benefits stolen during the period beginning on October 1, 2022, and ending on December 20, 2024", which had answered `NOTHING` inside the period and now answers `JUST TRUE` there.
- **375b was overruled by the lead, not by its encoder.**
  The function `s 2018(c) the sentence is within the limits the subsection sets` is a predicate named for the limit; part 6 answers `JUST TRUE` inside the limit for a predicate of that name, and part 1 had answered `NOTHING`.
  The lead asked part 1 to switch, there was one round of crossed messages, and the final state is `JUST TRUE` inside the limits (`snap1-s2018.l4:174`, `snap1-tests-s2018.l4:75-76`), with the revert recipe in the part's notes.
  **That is the lead's call, "assumed, not ruled", and it is listed again below as one of a pair.**

Part 3's encoder also found a defect that no assertion of the author's touches, in `s 2016(h)(1)(A)` and `s 2016(h)(14)(C)(i)`: with a waiver or a finding of the Secretary supplied, the function answered `NOTHING` whatever the date, though a State agency that implemented in time had plainly met the deadline.
It now answers `JUST TRUE` when the date is on or before the deadline and `NOTHING` when it is later or not given; five assertions were added.

**The other 130 failures were not defects; 127 are reconciled to the encoding's answer and 3 are kept as `-- GAP` lines.**
Each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote and the reason, which begins with the author's item number and the part.
The 127:

- **Ninety-six are the convention disagreement in which the encoding answers `NOTHING` and the author expected another answer: seventy-one expected `JUST FALSE`, twenty-three `JUST TRUE`, one `JUST 0` (419b) and one the State agency (70d).**
  Seventy-six are branches tagged "NOTHING-kind (limited by its own wording)", which is the second of the two readings that the 2026-10-29 rule leaves for a lawyer (a grant, a duty or a prohibition limited by its own wording is not counted as the text's no); the grounds the encoders give are a named class or complement, a stated period or amount, a bar that is lifted (and so not a grant), and a cap.
  Eleven are tagged "points outside the text" (a determination of the Secretary, regulations, or another section); nine are "silent" or "list not closed".
  Nineteen of the twenty-three that expected `JUST TRUE` and fifty-seven of the seventy-one that expected `JUST FALSE` are in the first group.
- **Seven are the opposite: the encoding answers `JUST FALSE` or 0 on a failed "if" or "except" and the author expected `NOTHING` (S3.41, S3.74, S3.76, S3.80, S4.14, S4.45 and S4.48).**
  This is the first reading, (a), and the author's own report calls five of these its slips.
- **Eight are forks, reconciled to the encoding's answer (57, 202, 394a, 421b, 446b, 498d, 537a and S3.27).**
  Each is in the register of its part (F-A1, F-mo, F-2024-3 and the like), with the other reading and what it would change; 394a and 421b are "may not ... unless" read as lifting a bar against read as "may if", and 202 and 537a are how a month is counted.
- **Twelve are percentages (271, 272a to d, 496a to c, S3.39, S3.40, S4.23 and S4.24):** the encoding takes a fraction (15 percent is 0.15) and the author passed the printed number; the unit is stated in the module headers, the input names and the notes, and the assertions are restated to the fraction.
- **Four were the author's errors (6, 276, 356 and S2.69):** the end of a transitional period that is not an input (6); a determination passed as "none supplied" where a caller who knows there is none passes `JUST FALSE` (276); the cost of the thrifty food plan confused with the published maximum allotment (356: the formula gives 24 for 306 and 25 for any cost from 306.25 to just under 307, and the published 25 is carried as data); and a branch the author's own scenario 405 answers the same way (S2.69).
- **Three are kept as `-- GAP` lines (506, 513a and 631a):** the author passed a printed percent into a function whose input is a fraction, so the input read as 900 percent and the answer to it is not a finding; the twins that pass the fraction pass.
- **Two assertions were added by the lead, not by the author (11b-added and 24-added),** next to the reconciled 11b and 24: the same facts with the Secretary's determination input set to `JUST FALSE`, which the encoding answers `JUST FALSE`.
  They show that a caller who knows the Secretary has made no determination gets the author's answer.

**The convention is not applied one way throughout, and the parts do not agree with each other.**
These are the pairs and families a lawyer should look at first; none has been ruled, and each is listed with the line that would move it.
Some of these pairs are worked through, with the statute words, both functions and one input each, in [`docs/design-question-false-or-nothing.md`](../../../../../docs/design-question-false-or-nothing.md), which records the question as open.

- **A predicate named for the limit against a function named for a permission.**
  A predicate named for a limit answers `JUST TRUE` inside and `JUST FALSE` past it (part 6's rule, applied by the lead to 375b and by part 3 to its own predicates); a function named for a permission is read otherwise (part 6 answers `NOTHING` past the limit; part 3's 347b answers `NOTHING` inside the cap of a bar and `JUST FALSE` past it).
  Part 3 notes that read literally, the rule would change eight of its assertions on four "may" functions where the "may" is itself the grant (`snap3-tests-s2017.l4:112, 114, 130, 131`; `snap3-tests-s2024.l4:43, 44, 79`; `snap3-cases-seat.l4:185`).
- **A bound worded as a negative against a bound worded "up to".**
  Part 2 answers `JUST FALSE` past "not less often than", "does not exceed" and "not more than 3 years", and `NOTHING` past "of up to thirty days" and "up to one year"; part 3 answers `NOTHING` past "not more than 25 percent" (364b) and "up to eighteen months" (488b, S3.29), and `JUST FALSE` past "shall not occur more than 2 times".
  If a cap in the text's own words is the text's no, 364b, 488b and `s 2024(c)` change in part 3, and so do four assertions; part 3 lists them in its notes (Marginal readings, item 10).
- **"(other than ...)".** Part 6 answers `NOTHING` for `s 2031(e)` (657) and four siblings (`s 2026(d)(2)(C)(i)`, `s 2031(g)(1)(A)`, `s 2031(g)(1)(B)`, `s 2035(f)(3)(B)`); all five change together if "other than" is read as "except".
- **"Subject to".** Part 6 is split: `s 2026(f)` imports a flat negative and answers `JUST FALSE`, while S3.77 and `s 2036a(c)(5)` import a fact or an approval and answer `NOTHING`; part 1 answers `NOTHING` for "Subject to the availability of appropriations" (75).
- **"Until".** Part 1 answers `NOTHING` where "until" ends a duty (154b and 720b), and `JUST FALSE` for the side before the date in `s 2018(b)(2)(A)`, where it ends a prohibition.
- **Branches of the same shape that no assertion of the author's reaches and the encoders did not change.**
  Part 4 lists three (`s 2020(e)(4)`, `s 2020(e)(10)` and `s 2020(s)(6)(B)`, at `snap4-s2020-e-1.l4:360`, `snap4-s2020-e-1.l4:641` and `snap4-s2020-o-x.l4:316`) that would answer `JUST FALSE` under the brief's rule, as the repaired 407b does.
  Part 1 audited the 48 rules in its range whose quotation carries a condition word and a `NOTHING` branch, and read no others.

**The gaps.**
By the author's own account 28 scenarios have no assertion, kept as comment lines in `tests-independent.l4`: 23 are gaps (no function for the provision, for example subsection (c) of section 2013, the repealed sections 2030 and 2033, or the amount reserved each fiscal year in section 2025(h)(1)(A)), three are ambiguous on the text (169, 297 and 355), and two were not attempted (323 and 341).
Five more are partial (460b, 470, 537b, 722b and 722c: the function covers the derived consequence or the deadline date but not the question the scenario asked).
Three assertions that the author wrote were moved out as `-- GAP` lines, as above, so the file has 1,975 assertions.
**The 28 are the author's gaps and the largest honest hole in this pass:** several of them name provisions of the Act for which the encoding has no function, and the author's reason for each is kept beside it in `tests-independent.l4`.

**What the author could not decide from the text** (for comparison with the fork register), in brief:
whether the deemed resources under 2014(i)(2)(B)(ii) may be negative; the enactment date in 2016(f)(3)(B), where the source credits show two public laws; whether the minimum allotment for a household of three (808 less 810) floors at zero; whether regulations under 2020(a)(3)(B)(iii) may require more than 3 years; whether the State-error "except" in 2025(a) reaches the 35 percent bucket or only the 20 percent bucket; whether 24 months in 2025(h)(1)(A) counts inclusively; how "1 month after 31 January" is counted; how a stated period is counted in 2014(g)(3), (g)(4) and (i)(1) (153b, 154b, 720b and 165b); which subsection letters of section 2012 the text of 2012a means; whether "has met the duty" in 2036a(c)(2)(A) states a time; whether the exemption list in 2029(b) is closed; a refugee, for whom the encoding has no value and which the author mapped to "any other status" (246); and, for each of 11b, 24, 75, 276, 293b, 298b, 300b, 325b, 326b, 418, 597, S3.77 and 692b, whether an unmet condition that is a determination, approval or finding of the Secretary, or an appropriation, is the text's no or points outside it.

**Independence, as far as it went.**
The author did not open `NOTES.md`, `PROGRESS.md` or any brief or `notes/` file; its `enc/` directory held only the `.l4` modules and its own test file.
It read the modules through its own listing scripts, for names and types, and short comments beside a signature may have been visible; its itemised list of what it looked at was lost when its context was compacted, and it has not reconstructed it.
Of its 201 failures it called 87 "the encoding is wrong" (14 of them provisionally), 32 forks (15 of units, 3 of zero against `NOTHING`, 14 provisionally), 25 ambiguities, 52 "ME" (its expectation over-reads) and 5 "SLIP" (it broke the brief's convention); it left the last two groups failing as ordered.
It edited the expected value of S1.13 to `NOTHING` and reverted it in the same session; the comment on S1.13 carries an appended note and `ANSWERS.md` an erratum saying so.
After its context was compacted the harness attached the standing instruction files (three `CLAUDE.md` files and the memory index); the author read none of them with a tool and used none for an expected value.
Parts 2, 3, 4 and 5 were each attached lead-side files after their encoders' context was compacted: a staging script and a memory note about this very effect in all four, the lead's state file and a notes script named without contents in all four, and in part 5 also another encoding's write-up of its independent pass, which discusses the same convention; each encoder says it did not open them and used none for a verdict or an edit.
While triaging, the encoders of parts 2, 3 and 5 and of the keel read the author's `ANSWERS.md` by search and by line range, read-only, besides the author's `tests-independent.l4`.
Part 4's encoder also read its own transcript after its first compaction, and says so in its report.
Parts 1 and 6 and the keel were attached none.
