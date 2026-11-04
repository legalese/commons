# NOTES: Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4, whole Act with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written 2026-11-04 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel on the stable `l4` 1.6.98, and merged by the lead agent of the session that ran them.
Target dialect: `main`; every module also runs on the main build 1.6.108 with the same four counts.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`ssc-core.l4`, `ssc-definitions.l4` and their tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
9 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `ssc1` (lines 2 to 710), `ssc2` (lines 711 to 1229), `ssc3` (lines 1230 to 1911), `ssc4` (lines 1912 to 2443), `ssc5` (lines 2444 to 3094), `ssc6` (lines 3095 to 3717), `ssc7` (lines 3718 to 4330), `ssc8` (lines 4454 to 5066), `ssc9` (lines 5067 to 5744).
The lead agent verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the core identical to the keel's) and then merged them with a script; nothing in a part's modules was edited at the merge.
After the independent test pass described at the end of this file, the parts' encoders each looked at the reviewer's failing assertions for their own range and repaired their own modules where they judged the encoding wrong; the lead merged the repaired parts again with the same script, and nothing in a repaired module was edited at that second merge either.
The totals below are those of the repaired parts, and each part's notes (`notes/<part>-NOTES.md`) say what its encoder changed and which of its own expectations moved.
Every note a part wrote is kept, unchanged except that the lead's scratchpad path is replaced by a placeholder, as `notes/<part>-NOTES.md`, with its `PROGRESS.md`, `SEAMS.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the briefs each agent was given are `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `ssc-seat.l4` and `ssc-cases-seat.l4`, with one banner comment per part; the text under each banner is the part's, unchanged. Each part's questions are still those of its range of the text.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (`notes/<part>-SEAMS.md` lists what each part asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** A part that found the core lacking a type or field recorded it in its `NEEDS-CORE.md` and, where it needed it, declared its own type in its own module. The lead did not add them to the core: `ssc2-NEEDS-CORE.md`, `ssc6-NEEDS-CORE.md`.
- **Part-local types and helper names stay where they are.** A crude scan (`dupscan.py`, not shipped: backticked names at the start of a line, and `DECIDE` and `DECLARE` heads) of 2,983 defined names found four defined in more than one module, all in tests modules (`a pensioner attaining pensionable age on` in ssc3-tests-b.l4 and ssc3-tests-c.l4; `a person` in ssc3-tests-d.l4, -e.l4 and -f.l4; `sch 5 test a pension with every named increase` in ssc9-tests-sch5-w.l4 and ssc9-tests-sch5.l4; `ssc1 fixture person` in ssc1-tests-class1.l4 and ssc1-tests-prelim.l4); no module imports a tests module, so none can clash.
- **The merge lost nothing:** the merged folder was gated as it stands, and its total is 9,256 = 780 (ssc1) + 1,254 (ssc2) + 1,185 (ssc3) + 1,213 (ssc4) + 1,038 (ssc5) + 940 (ssc6) + 978 (ssc7) + 745 (ssc8) + 958 (ssc9) + 165 (the keel's tests), the parts' own totals as the lead measured them.

## Where things are

| agent | text (lines of `ukpga-1992-4.txt`) | modules | assertions in its test modules | seat questions |
| --- | --- | --- | --- | --- |
| keel | 1 to 1, 4331 to 4453 | 2 | 165 | 0 |
| ssc1 | 2 to 710 | 6 | 642 | 31 |
| ssc2 | 711 to 1229 | 6 | 965 | 58 |
| ssc3 | 1230 to 1911 | 9 | 1024 | 42 |
| ssc4 | 1912 to 2443 | 7 | 857 | 143 |
| ssc5 | 2444 to 3094 | 6 | 892 | 51 |
| ssc6 | 3095 to 3717 | 5 | 825 | 42 |
| ssc7 | 3718 to 4330 | 4 | 837 | 30 |
| ssc8 | 4454 to 5066 | 7 | 681 | 27 |
| ssc9 | 5067 to 5744 | 11 | 773 | 53 |
| seat cases, all parts | | 1 (`ssc-cases-seat.l4`) | 1595 | |

The seat layer is `ssc-seat.l4` (477 `@export` questions in all) and `ssc-cases-seat.l4`; every other module is layer 1, one module per run of sections, each with a tests module beside it.

## The source

The text is a plain-text rendering by a converter script and not the official text.
What it does, as found in the keel's range and in a read of the headings of the whole file:

- **Tables are omitted.**
  The sentences that introduce them remain.
  Known cases, each a sentence that introduces a table and is followed at once by the next provision: s 9A(3) (src:324), s 21(2) (src:746), Schedule 3 Part I at src:4861, all of Schedule 4 (src:4901-4907, headings only), and Schedule 4A at src:4933-4935, 4960-4962 and 4978-4980.
  A rate that the Act gives only in a table is therefore not in the sources: it is an input.
- **Schedule paragraph numbers are dropped.**
  Lettered paragraphs (5A and the like) exist, so counting headings misnumbers.
  Use the number an in-text citation gives.
- **Some limb labels are dropped.**
  In s 176(1) the list of sections under `(a) regulations made by virtue of--` has no sub-labels.
- **Blank and omitted text.**
  A line of dots (`. . . .`) is text shown repealed or blank; a line reading `...` is an editorial omission.
  In the keel's range these are src:4356, and the ten `...` lines under s 176(1).
- **A revised text can carry more than one extent version** of a provision; the keel's range shows none.

## The seat

From the brief the keel agent was given (its own notes have no seat section):

The seat the parts serve is a person who works, is self-employed, or claims a contributory or non-contributory benefit, statutory pay or Child Benefit in Great Britain, asking on facts they can state whether and how much they must pay in contributions, whether they are entitled to a benefit or to statutory pay, how much, for how long, and what ends or reduces it.

## What check.sh prints

Run as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` on the merged folder, exit 0, before the independent test pass was added:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-cases-seat.l4                              0      1595       0        0         0 |      0      1595       0        0  same
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc-definitions-tests.l4                       0       165       0        0         0 |      0       165       0        0  same
ssc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc1-class1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-class1a1b.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc1-class23.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc1-class4.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-general.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc1-prelim.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-tests-class1.l4                           0       134       0        0         0 |      0       134       0        0  same
ssc1-tests-class1a1b.l4                        0       116       0        0         0 |      0       116       0        0  same
ssc1-tests-class23.l4                          0       160       0        0         0 |      0       160       0        0  same
ssc1-tests-class4.l4                           0        48       0        0         0 |      0        48       0        0  same
ssc1-tests-general.l4                          0        16       0        0         0 |      0        16       0        0  same
ssc1-tests-prelim.l4                           0       168       0        0         0 |      0       168       0        0  same
ssc2-bereavement.l4                            0         0       0        0         0 |      0         0       0        0  same
ssc2-factors.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc2-incapacity.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc2-maternity.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc2-prelim.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc2-tests-bereavement.l4                      0       195       0        0         0 |      0       195       0        0  same
ssc2-tests-factors.l4                          0       134       0        0         0 |      0       134       0        0  same
ssc2-tests-incapacity.l4                       0       237       0        0         0 |      0       237       0        0  same
ssc2-tests-maternity.l4                        0       151       0        0         0 |      0       151       0        0  same
ssc2-tests-prelim.l4                           0       102       0        0         0 |      0       102       0        0  same
ssc2-tests-widow-ib.l4                         0       146       0        0         0 |      0       146       0        0  same
ssc2-widow-ib.l4                               0         0       0        0         0 |      0         0       0        0  same
ssc3-a-s43-s44.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-a0-s61za-s61zc.l4                         0         0       0        0         0 |      0         0       0        0  same
ssc3-b-s44a-s44c.l4                            0         0       0        0         0 |      0         0       0        0  same
ssc3-c-s45-s46.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-d-s47-s48c.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc3-e-s51-s55.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-f-s55a-s56.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc3-g-s60-s62.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-helpers.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc3-tests-a.l4                                0       144       0        0         0 |      0       144       0        0  same
ssc3-tests-b.l4                                0       124       0        0         0 |      0       124       0        0  same
ssc3-tests-c.l4                                0       138       0        0         0 |      0       138       0        0  same
ssc3-tests-d.l4                                0       260       0        0         0 |      0       260       0        0  same
ssc3-tests-e.l4                                0       122       0        0         0 |      0       122       0        0  same
ssc3-tests-f.l4                                0       121       0        0         0 |      0       121       0        0  same
ssc3-tests-g.l4                                0       115       0        0         0 |      0       115       0        0  same
ssc4-attendance-allowance.l4                   0         0       0        0         0 |      0         0       0        0  same
ssc4-carers-allowance.l4                       0         0       0        0         0 |      0         0       0        0  same
ssc4-disability-living-allowance.l4            0         0       0        0         0 |      0         0       0        0  same
ssc4-disablement.l4                            0         0       0        0         0 |      0         0       0        0  same
ssc4-guardians-and-aged.l4                     0         0       0        0         0 |      0         0       0        0  same
ssc4-increases.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc4-industrial-injuries-general.l4            0         0       0        0         0 |      0         0       0        0  same
ssc4-tests-attendance-allowance.l4             0       121       0        0         0 |      0       121       0        0  same
ssc4-tests-carers-allowance.l4                 0        80       0        0         0 |      0        80       0        0  same
ssc4-tests-disability-living-allowance.l4       0       166       0        0         0 |      0       166       0        0  same
ssc4-tests-disablement.l4                      0       213       0        0         0 |      0       213       0        0  same
ssc4-tests-guardians-and-aged.l4               0        80       0        0         0 |      0        80       0        0  same
ssc4-tests-increases.l4                        0        66       0        0         0 |      0        66       0        0  same
ssc4-tests-industrial-injuries-general.l4       0       131       0        0         0 |      0       131       0        0  same
ssc5-logic.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part10.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc5-part6.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part7.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part8.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part9.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-tests-logic.l4                            0        32       0        0         0 |      0        32       0        0  same
ssc5-tests-part10.l4                           0       102       0        0         0 |      0       102       0        0  same
ssc5-tests-part6.l4                            0       249       0        0         0 |      0       249       0        0  same
ssc5-tests-part7.l4                            0       220       0        0         0 |      0       220       0        0  same
ssc5-tests-part8.l4                            0       155       0        0         0 |      0       155       0        0  same
ssc5-tests-part9.l4                            0       134       0        0         0 |      0       134       0        0  same
ssc6-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc6-sap.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-smp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-spp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-ssp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-tests-sap.l4                              0       219       0        0         0 |      0       219       0        0  same
ssc6-tests-smp.l4                              0       205       0        0         0 |      0       205       0        0  same
ssc6-tests-spp.l4                              0       207       0        0         0 |      0       207       0        0  same
ssc6-tests-ssp.l4                              0       194       0        0         0 |      0       194       0        0  same
ssc7-12zc.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12zd.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12ze.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-tests-12zc.l4                             0       353       0        0         0 |      0       353       0        0  same
ssc7-tests-12zd.l4                             0       164       0        0         0 |      0       164       0        0  same
ssc7-tests-12ze.l4                             0       147       0        0         0 |      0       147       0        0  same
ssc7-tests-xiia.l4                             0       173       0        0         0 |      0       173       0        0  same
ssc7-xiia.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch1a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch1b.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch3.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-sch4b.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc8-tests-sch1a.l4                            0       149       0        0         0 |      0       149       0        0  same
ssc8-tests-sch1b.l4                            0       132       0        0         0 |      0       132       0        0  same
ssc8-tests-sch2.l4                             0        73       0        0         0 |      0        73       0        0  same
ssc8-tests-sch3.l4                             0       172       0        0         0 |      0       172       0        0  same
ssc8-tests-sch4.l4                             0         8       0        0         0 |      0         8       0        0  same
ssc8-tests-sch4a.l4                            0        94       0        0         0 |      0        94       0        0  same
ssc8-tests-sch4b.l4                            0        53       0        0         0 |      0        53       0        0  same
ssc9-sch11.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc9-sch12-13.l4                               0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5-w.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc9-sch5a.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc9-sch6.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p1.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p2.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p4.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch7-p6.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-sch9-10.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc9-tests-sch11.l4                            0        44       0        0         0 |      0        44       0        0  same
ssc9-tests-sch12-13.l4                         0        44       0        0         0 |      0        44       0        0  same
ssc9-tests-sch5-w.l4                           0       102       0        0         0 |      0       102       0        0  same
ssc9-tests-sch5.l4                             0        92       0        0         0 |      0        92       0        0  same
ssc9-tests-sch5a.l4                            0        47       0        0         0 |      0        47       0        0  same
ssc9-tests-sch6.l4                             0        53       0        0         0 |      0        53       0        0  same
ssc9-tests-sch7-p1.l4                          0       113       0        0         0 |      0       113       0        0  same
ssc9-tests-sch7-p2.l4                          0        32       0        0         0 |      0        32       0        0  same
ssc9-tests-sch7-p4.l4                          0       103       0        0         0 |      0       103       0        0  same
ssc9-tests-sch7-p6.l4                          0        99       0        0         0 |      0        99       0        0  same
ssc9-tests-sch9-10.l4                          0        44       0        0         0 |      0        44       0        0  same
TOTAL (124 modules)                            0      9256       0        0           |      0      9256       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 9,256 assertions satisfied over 124 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each part read its own traces on both builds by hand (see its NOTES).

## What each part's notes hold

**keel**
- `notes/keel-NOTES.md:14` Files
- `notes/keel-NOTES.md:25` Coverage table (the keel's range)
- `notes/keel-NOTES.md:70` Fork register
- `notes/keel-NOTES.md:93` What the keel chose in the core (assumed, not ruled)
- `notes/keel-NOTES.md:136` Marginal readings for a lawyer
- `notes/keel-NOTES.md:153` Jural relations
- `notes/keel-NOTES.md:176` What the stable binary does not accept
- `notes/keel-NOTES.md:202` The converter text
- `notes/keel-NOTES.md:221` What was run
- `notes/keel-NOTES.md:233` Open questions for the lead

**ssc1**
- `notes/ssc1-NOTES.md:14` Method and files
- `notes/ssc1-NOTES.md:23` Seat
- `notes/ssc1-NOTES.md:77` Coverage (ssc1)
- `notes/ssc1-NOTES.md:776` Fork register (ssc1)
- `notes/ssc1-NOTES.md:791` Jural relations (ssc1)
- `notes/ssc1-NOTES.md:849` Marginal readings for a lawyer (ssc1)
- `notes/ssc1-NOTES.md:1076` Seams (ssc1)
- `notes/ssc1-NOTES.md:1107` Findings: what the text turns out to say
- `notes/ssc1-NOTES.md:1124` What the stable binary does not accept
- `notes/ssc1-NOTES.md:1143` After the independent review (2026-11-04)
- `notes/ssc1-NOTES.md:1148` What `check.sh` prints
- `notes/ssc1-NOTES.md:1181` What the text does not answer, and what needs doing before relying on it

**ssc2**
- `notes/ssc2-NOTES.md:7` About the source text
- `notes/ssc2-NOTES.md:15` What is in this folder
- `notes/ssc2-NOTES.md:39` Where PLAN.md differs from the brief, and from itself
- `notes/ssc2-NOTES.md:48` Seat
- `notes/ssc2-NOTES.md:68` Coverage (ssc2)
- `notes/ssc2-NOTES.md:627` Fork register (ssc2)
- `notes/ssc2-NOTES.md:655` Jural relations (ssc2)
- `notes/ssc2-NOTES.md:730` Marginal readings for a lawyer (ssc2)
- `notes/ssc2-NOTES.md:834` Seams (ssc2)
- `notes/ssc2-NOTES.md:951` What the text turns out to say (ssc2)
- `notes/ssc2-NOTES.md:985` Independent review of 2026-11-04: the 17 failures in this range (ssc2)
- `notes/ssc2-NOTES.md:1013` What the stable binary does not accept (ssc2)
- `notes/ssc2-NOTES.md:1035` Expectations changed after a run (ssc2)
- `notes/ssc2-NOTES.md:1061` What check.sh prints (ssc2)

**ssc3**
- `notes/ssc3-NOTES.md:11` What was written
- `notes/ssc3-NOTES.md:39` Conventions this part departs from, or adds
- `notes/ssc3-NOTES.md:53` Seat (ssc3)
- `notes/ssc3-NOTES.md:186` Coverage (ssc3)
- `notes/ssc3-NOTES.md:560` Fork register (ssc3)
- `notes/ssc3-NOTES.md:605` Jural relations (ssc3)
- `notes/ssc3-NOTES.md:685` Marginal readings for a lawyer (ssc3)
- `notes/ssc3-NOTES.md:829` Seams (ssc3)
- `notes/ssc3-NOTES.md:875` What the text turns out to say (numbered findings)
- `notes/ssc3-NOTES.md:925` What the stable binary does not accept
- `notes/ssc3-NOTES.md:940` What the text does not answer
- `notes/ssc3-NOTES.md:959` What check.sh prints

**ssc4**
- `notes/ssc4-NOTES.md:5` Source, and what "verified" means here
- `notes/ssc4-NOTES.md:12` Seat
- `notes/ssc4-NOTES.md:25` Files
- `notes/ssc4-NOTES.md:53` Test discipline
- `notes/ssc4-NOTES.md:65` Coverage (ssc4)
- `notes/ssc4-NOTES.md:615` Fork register (ssc4)
- `notes/ssc4-NOTES.md:637` Jural relations (ssc4)
- `notes/ssc4-NOTES.md:719` Marginal readings for a lawyer (ssc4)
- `notes/ssc4-NOTES.md:854` Seams (ssc4)
- `notes/ssc4-NOTES.md:887` What the text turns out to say (ssc4)
- `notes/ssc4-NOTES.md:903` What the text does not answer (ssc4)
- `notes/ssc4-NOTES.md:913` What the stable binary does not accept (ssc4)
- `notes/ssc4-NOTES.md:929` The independent reviewer's 13 failures in this range (ssc4)
- `notes/ssc4-NOTES.md:956` What check.sh prints (ssc4)
- `notes/ssc4-NOTES.md:990` Peeked, and files the harness attached

**ssc5**
- `notes/ssc5-NOTES.md:8` Seat
- `notes/ssc5-NOTES.md:17` Files
- `notes/ssc5-NOTES.md:35` Decision procedure (ssc5; applied uniformly, each rule licensed by the text named)
- `notes/ssc5-NOTES.md:53` Coverage (ssc5)
- `notes/ssc5-NOTES.md:733` Fork register (ssc5)
- `notes/ssc5-NOTES.md:814` Jural relations (ssc5)
- `notes/ssc5-NOTES.md:891` Marginal readings for a lawyer (ssc5)
- `notes/ssc5-NOTES.md:1022` Seams (ssc5)
- `notes/ssc5-NOTES.md:1062` Findings: what the text turns out to say (ssc5)
- `notes/ssc5-NOTES.md:1098` Changes after the independent review (ssc5)
- `notes/ssc5-NOTES.md:1123` What the stable binary does not accept (ssc5)
- `notes/ssc5-NOTES.md:1148` What check.sh prints (ssc5)

**ssc6**
- `notes/ssc6-NOTES.md:10` What this is
- `notes/ssc6-NOTES.md:28` Where `PLAN.md` and the brief differ
- `notes/ssc6-NOTES.md:33` Coverage (ssc6)
- `notes/ssc6-NOTES.md:645` Fork register (ssc6)
- `notes/ssc6-NOTES.md:730` Jural relations (ssc6)
- `notes/ssc6-NOTES.md:815` Marginal readings for a lawyer (ssc6)
- `notes/ssc6-NOTES.md:983` Seams (ssc6)
- `notes/ssc6-NOTES.md:1032` What the text turns out to say (ssc6)
- `notes/ssc6-NOTES.md:1102` What the stable binary does not accept (ssc6)
- `notes/ssc6-NOTES.md:1133` What `check.sh` prints (ssc6)
- `notes/ssc6-NOTES.md:1178` Files (ssc6)

**ssc7**
- `notes/ssc7-NOTES.md:45` Coverage (ssc7)
- `notes/ssc7-NOTES.md:647` Fork register (ssc7)
- `notes/ssc7-NOTES.md:669` Jural relations (ssc7)
- `notes/ssc7-NOTES.md:876` Marginal readings for a lawyer (ssc7)
- `notes/ssc7-NOTES.md:981` Seams (ssc7)
- `notes/ssc7-NOTES.md:1016` The seat layer (ssc7)
- `notes/ssc7-NOTES.md:1076` What the text turns out to say (ssc7)
- `notes/ssc7-NOTES.md:1123` What the stable binary does not accept (ssc7)
- `notes/ssc7-NOTES.md:1149` What `check.sh` prints (ssc7)
- `notes/ssc7-NOTES.md:1195` Files, and how to rebuild (ssc7)

**ssc8**
- `notes/ssc8-NOTES.md:6` What this is
- `notes/ssc8-NOTES.md:28` Coverage (ssc8)
- `notes/ssc8-NOTES.md:355` Fork register (ssc8)
- `notes/ssc8-NOTES.md:383` Jural relations (ssc8)
- `notes/ssc8-NOTES.md:449` Marginal readings for a lawyer (ssc8)
- `notes/ssc8-NOTES.md:626` Seams (ssc8)
- `notes/ssc8-NOTES.md:660` Seat (ssc8)
- `notes/ssc8-NOTES.md:683` What the text turns out to say
- `notes/ssc8-NOTES.md:723` What the stable binary does not accept
- `notes/ssc8-NOTES.md:746` What `check.sh` prints

**ssc9**
- `notes/ssc9-NOTES.md:6` Status and how each claim here was checked
- `notes/ssc9-NOTES.md:23` The seat (statement)
- `notes/ssc9-NOTES.md:34` Files
- `notes/ssc9-NOTES.md:57` PLAN.md and the brief: where they differ (the brief governs)
- `notes/ssc9-NOTES.md:78` Paragraph labels that are inferred
- `notes/ssc9-NOTES.md:116` Coverage (ssc9)
- `notes/ssc9-NOTES.md:457` Fork register (ssc9)
- `notes/ssc9-NOTES.md:497` Jural relations (ssc9)
- `notes/ssc9-NOTES.md:595` Marginal readings for a lawyer (ssc9)
- `notes/ssc9-NOTES.md:814` Seams (ssc9)
- `notes/ssc9-NOTES.md:877` What the text turns out to say (findings)
- `notes/ssc9-NOTES.md:938` What the stable binary does not accept
- `notes/ssc9-NOTES.md:952` What check.sh and srcrefs print

## What would need doing before the encoding is worth relying on

- A lawyer reads each part's coverage table, forks and marginal readings against the official text (this is a converter's rendering).
- The FALSE and NOTHING readings the parts flag for a lawyer are decided (the 2026-10-29 rule leaves two readings open; no ruling has been made).
- The seams are wired or kept as questions, and the NEEDS-CORE requests are taken into the core or refused.
- The prescribed figures and rates that the text leaves to regulations or orders are supplied as inputs; this encoding does not hold them unless a part's notes say so.

## Source not official

The quoted text is a plain-text rendering of the Act as deposited in `../../registers/source-bundle/`; it is not the official text. See 'The source' above and `SOURCE-LICENSE.md`.

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, briefs or tests wrote `ANSWERS.md` from the text of the Act alone before it opened any `.l4` file: 669 scenarios, at least 60 from each quarter of the text, and a sample of seat questions from every quarter.
It then wrote `tests-independent.l4`: 1,041 assertions (893 on the modules and 148 on 107 distinct seat questions, 27, 27, 27 and 26 by quarter), covering 506 of the 669 scenarios, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the numbers in the comments of `tests-independent.l4` refer to it.
The author was given the family's rule for "no" and "not said" in its brief (see "Reading a result: FALSE and NOTHING" above) and wrote its expected values by it.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as first merged | 1,041 | 945 | 96 | 0 |
| after the encoders' repairs below, before the reconciliation | 1,041 | 956 | 85 | 0 |
| after the reconciliation below | 1,041 | 1,041 | 0 | 0 |

The nine part encoders each got the author's failing lines for their own range and were asked to judge them against the text.
Where an encoder judged its encoding wrong it repaired the module and left the author's assertion unchanged; every one of its own expectations that it changed is listed in its part's notes (`notes/ssc1-NOTES.md` and its siblings).
Together the repairs added 28 assertions of the encoders' own (part 1: 12, part 2: 2, part 4: 1, part 5: 1, part 9: 12), and the merged encoding went from 9,228 to 9,256 satisfied assertions.
A repair made after seeing the author's expected value is not independent evidence that the repaired answer is right; the evidence for each is the quotation from the text in the part's notes.
The encoders' briefs for this pass quoted two comparators that came out of the triage of the Food and Nutrition Act encoding (a predicate named for the limit answers `JUST TRUE` inside it and `JUST FALSE` past it; a failed "if" whose trigger is a duty or a prohibition is the text's no), and the encoders' reports say how each applied them; neither is a ruling.

**Eleven of the 96 first-run failures were encoder defects, repaired; the author's assertions stand unchanged.**
Three were in the group the author itself called "candidate encoding defects" (S583b, S303b and S649b), and eight were in groups where the author had classed its own expectation as wrong by the convention (S460c and S598b; S120, S368a, S385a, S621a, S643a and SEAT125).

- **S583b, a polarity inversion (part 8).**
  Schedule 4A para 3(3) says Part II "does not apply in relation to the year" if the condition is satisfied in relation to one or more tax weeks; the function `sch 4A para 3(3) Part II does not apply because of the condition` answered `JUST FALSE` for one week, the answer to the question "does Part II apply", not to the question its name asks.
  It now answers `JUST TRUE` for one week or more and `JUST FALSE` for none, as its sibling `sch 4A para 2(1)` does for the same weeks; three of the encoder's own expectations changed (`ssc8-tests-sch4a.l4:123-125`).
- **A failed "if", "so long as" or "unless" that the encoding had answered `NOTHING` (S303b in part 4, S368a and S385a in part 5, S649b in part 9).**
  In each the quoted words are on the brief's list of grounds for `JUST FALSE`, and a sibling rule of the same shape in the same part already answered `JUST FALSE`.
  S303b is s 94(3), "in the absence of evidence to the contrary".
  S368a is s 134(1), "No person shall be entitled to an income-related benefit if his capital ... exceeds the prescribed amount", a function named for the bar's own condition.
  S385a is s 140A(2), "unless she has reached the 25th week of her pregnancy before 1st January 2011", with its two sub-paragraph siblings.
  S649b is Schedule 7 Part VI para 21, "If a person dies as a result of any pulmonary disease and ...", and its flat negative in sub-paragraph (3).
- **A function named for a limit that answered `NOTHING` where a sibling named for the same kind of limit answered `JUST FALSE` (S460c in part 6 and S598b in part 9).**
  S460c is s 171ZE(3), "the qualifying period determined by regulations is long enough" (at least 56 days): 55 days now answers `JUST FALSE`.
  S598b is Schedule 5 para 3C(1)(d), "deferred throughout the period of 12 months": 11 months now answers `JUST FALSE`, and the "where" ground moved to the paragraph that opens with "where".
- **A "shall" duty with a single exception (S120, part 2).**
  Section 23(1)(a) says the amounts "shall be expressed, subject to subsection (2) below, as whole numbers of pounds", so the text says yes in its own words; `s 23(2)` now answers `JUST TRUE` where it had answered `NOTHING`.
- **A scope sentence that says "applies only" or "only has effect" (S621a, S643a and SEAT125, both in part 9).**
  Schedule 7 Part I para 1 and Part VI para 14(1) answered `NOTHING` inside the stated case on the ground that "only" gives a necessary condition and not a grant; a sibling scope sentence without "only" answers `JUST TRUE` inside, so "only" adds the `JUST FALSE` outside and does not take away the `JUST TRUE` inside.
  The encoder called this a new reading, (e), of its own, and listed the one-line revert; it is the same shape as part 3's 348a and 348d in the Food and Nutrition Act encoding.

One more was a defect in the input contract and not in the arithmetic (S145, part 2): the first input of the function is the days of entitlement not counting the first three days of the period of incapacity, which the function adds, and the author passed 10 for "ten days including the first three".
The contract is now written in a comment and in the seat `@desc`, no input was renamed, and two assertions were added (the encoder's pin that the author's facts under the stated contract give 13); the author's assertion is reconciled to the encoding's 16 for the input as passed.

Three encoders also changed rules the author had no assertion on, by applying the same reasoning to the siblings of what the author had found; no reviewer assertion that passed before fails now.
Part 1 changed eight functions from `NOTHING` to `JUST FALSE` on a failed "if" or "except" (`s 11(1)` with its two consumers `s 11(5B)` and `s 11(6)`, `s 4C(7)`, `s 10ZA(2)`, `s 10ZBA(4)`, `s 15(3A)` for its "if" limb, and `s 19A(2)`), and part 5 four (`s 134(2)`, `s 137(1)`, `s 122(1)` and `s 139(5)`).
Part 9 changed three more: paragraph 20 of Schedule 7 Part VI, Schedule 12 para 3(2) for the first day, and Schedule 7 Part IV para 11(6).
**Part 9 also made one judgment that nobody asked for:** Schedule 7 paragraphs 20(3) and 21(3), "does not affect death benefit where the death occurred before ...", now answer `JUST FALSE` as a flat negative, as "does not apply" does elsewhere; a lawyer may read "does not affect" as preserving the earlier position instead, which would make the answer `NOTHING`, and the revert is listed in the part's notes.

**The other 85 failures were not defects and are reconciled to the encoding's answer.**
Each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote and the reason, which begins with the author's item number and the part.

- **Seventy-two are the convention disagreement in which the encoding answers `NOTHING` and the author expected another answer: fifty-four expected `JUST FALSE`, seventeen `JUST TRUE` and one `JUST 0` (S146b).**
  Sixty-eight are branches tagged "NOTHING-kind (limited by its own wording)", which is the second of the two readings that the 2026-10-29 rule leaves for a lawyer (a grant, a duty or a prohibition limited by its own wording is not counted as the text's no); the grounds the encoders give are a clause that opens with "where", a named class or complement, a stated period or amount, a bar that is lifted (and so not a grant), and a relative clause that limits a grant.
  Four are tagged "includes", "silent" or "list not closed" (S31b, S356b, S364b and S560b).
- **One is the opposite: the encoding answers `JUST FALSE` on a failed "if" (S440b, "The notice shall be in writing if the person ... so requests") and the author expected `NOTHING`;** the author concedes it.
- **Eleven were the author's errors, restated with the reason (S94b, S162b, S224a, S224b, S271c, S273, S361, S377b, S441, S450a and S593a):**
  arithmetic on the weeks before an expected week of confinement (S162b, S361, S441); a date edge or a fixture that the author's own comment contradicts (S94b: 30 April is the cut-off date and not before it; S224a and S224b: a woman attaining pensionable age on 5 April and on 6 April 2010 against "before 6 April 2010", and a fixture that left s 51ZA(3) unknown); a bar read with the wrong polarity or the wrong inputs (S271c, S273); a "means" definition on which no match is `JUST FALSE` (S377b); the core's fifth constructor of a week (S450a); and an unrounded quantity against "rounded to the nearest penny" (S593a).
- **One is the input contract above (S145).**

**The convention is not applied one way throughout, and the parts do not agree with each other.**
These are the pairs and families a lawyer should look at first; none has been ruled, and each is listed with the line that would move it.

- **"Where".** Parts 1, 2 and 9 answer `NOTHING` for a failed "where" ("Where in any tax week earnings are paid ...", "applies where", "Where ... the period of deferment is at least 12 months"), on the ground that "where" is not on the brief's list of grounds for `JUST FALSE` and the same text uses "if" where it means a condition; part 7 answers `JUST FALSE` for a failed "where" in eight branches of Part 12ZC and `NOTHING` for s 171B(1) (`ssc7-12zc.l4:117, 222, 397, 444, 555, 654, 786, 827`), and four of those eight are permissions ("V may vary").
  If a ruling goes against reading (a) for "where", those eight flip; if it goes the other way, the `NOTHING` branches of parts 1, 2 and 9 flip together.
- **A predicate named for its class.** Part 2's five predicates named for the class they describe (`s 23A(1)`, `s 38(4)`, `s 40(1)`, `s 41(1)` and `s 39A(1A)`) answer `NOTHING` outside the class; if a ruling gives a class-named predicate `JUST FALSE` outside it, S122b, S123b, S167b, S167c and S183b flip to `JUST FALSE` and S170a to `JUST TRUE`.
  The same question is asked by S301b in part 4, which the encoder left as `NOTHING` and flagged.
- **"Until" and a stated period.** Part 5's S364d ("until the end of the period of 15 days ... section 124(1) above shall have effect") fits both lists, and every other branch of that part limited to a period or to "while" answers `NOTHING` outside it; changing S364d alone would split that class, and the encoder says it is the one item on which it thinks the lead could reasonably rule the other way (one arm, `ssc5-part7.l4:519`).
- **A negative inside a relative clause.** Part 1's S99 and SEAT09 (s 15(1)(c), "are not profits of a trade, profession or vocation carried on wholly outside the United Kingdom") are the encoder's own weakest call; a lawyer who reads (c) as the text's own exclusion changes one line.
- **"Throughout which".** Part 2's S176a reads "shall continue to be entitled ... for any period throughout which she or he ... is under pensionable age" as not on the brief's list; if it is read as "while", every requirement failure of ss 37(3), 38(2) and 39A(4) to (4B) flips together.
- **Branches of the same shape that no assertion of the author's reaches and the encoders did not change.**
  Part 4 lists `s 66(1)(a)(i)` and `s 66(1)(b)` (`ssc4-attendance-allowance.l4:418, 449`), which answer `NOTHING` when the person did not claim expressly on the ground of terminal illness although the subsection opens "If a terminally ill person makes a claim expressly on the ground that he is such a person, then", and S301b.
  Part 6 lists `s 165(3B)` (`ssc6-smp.l4:352-368`).
  Part 3 notes two other branches tagged "silent" in the same shape as its SEAT32 (`ssc3-c-s45-s46.l4:249` and `ssc3-b-s44a-s44c.l4:191`).

**The gaps.**
163 of the 669 scenarios have no assertion, each kept as a `-- GAP` line at the end of the file in eight groups with the scenario numbers and the author's reason (the lead moved them there from the author's report, the reasons are the author's).
Ninety-three are scenarios the author deferred: a function exists, and the author did not attempt it, for budget or because its inputs have mixed meaning; **these are the author's omissions and the largest honest hole in this pass.**
Forty-one are for provisions with no function at all (a power, an authority, a repealed provision), eight are counts that nothing in the encoding makes, two take a figure from a table that the deposited text lacks, and the rest are scenarios with no function that isolates the question, or are covered elsewhere.
Twelve of the 163 are in no gap row of the author's table, which the author says itself.

**What the author could not decide from the text** (for comparison with the fork register), in brief:
whether a stillbirth at exactly 24 weeks is "after 24 weeks" (ss 35(6)(b), 171(1), 171ZA(5), 171ZZ15(a)); whether payment on 5 April 2017 is "before" the cut-off date in s 14A(1); how a person born on 29 February attains an age in a non-leap year (s 173); how a period of months or years that begins on 29 February or on the 31st is counted (ss 176(2A), 13A(4), 14A(1A)(b)); how "within N days from" is counted at the boundary (Schedule 1 "within six years after", Schedule 7 Part III "within a period of 28 days", s 171B(3) "until the 197th day"); a mixed year in Schedule 4A Part III and Schedule 4B, where the condition holds for some weeks and not others; whether the first payable day in s 103(6) "until after the expiry of the period of 90 days (disregarding Sundays)" is the day after the last counted day; whether "at least half that number of years" in Schedule 3 para 5(7) rounds up; and which tables the deposited text lacks (ss 9A(3) and 21(2), Schedule 3 para 5(5), Schedule 4 Parts I and III to V, Schedule 4A Part II and III tables, Schedule 5 paras 3B(3) and 7B(3)).

**Independence, as far as it went.**
The author did not open `NOTES.md`, `PROGRESS.md` or any brief or `notes/` file; its `enc/` directory held only the `.l4` modules and its own test file, and a scan of the first 600 characters of each of its tool calls found no forbidden path.
It re-aimed eight assertions after reading the first run, changing the function it asked, the order of its inputs or a flag (S197, S222, S243, S245, S279b, S225b, S225c and S288b), and corrected the dates of four more (S144, SEAT31, S514 and S649); it says it edited no expected value.
It classified its 96 failures with a provenance code: it re-read the source and opened the encoding function for 13, re-read the source only for 16, checked 2 by arithmetic only, and classified 65 from its own scenario comment and `ANSWERS.md` without re-reading either the source or the encoding.
Late in its work it read its own subagent transcript, only to audit its own tool calls, and says so.
After its context was compacted the harness attached its own assignment, the skill text and the standing instruction files (three `CLAUDE.md` files and the memory index, one line of which names this Act among six planned encodings); it opened none of those files and used none for an expected value.
While triaging, the encoders of parts 2, 4 and 9 read the author's `ANSWERS.md` by search, read-only, besides the author's `tests-independent.l4`; no other encoder's transcript shows a read of it.
Part 9's encoder was attached lead-side files after its context was compacted (a staging script and a memory note about this very effect, the lead's state file and a notes script named without contents, and the list of its own failing lines); it says it used none for a verdict or an edit, and one incidental effect: the staging script's text named a section of this file, which made it search for that heading before regenerating its notes.
The other eight part encoders and the author were attached none.
