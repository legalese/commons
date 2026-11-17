# NOTES: Criminal Code (Canada), R.S.C., 1985, c. C-46, whole Act with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written 2026-11-12 to 2026-11-17 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel. They were stopped by a weekly usage limit on 2026-11-12 and again on 2026-11-16, and resumed from their own transcripts. The lead agent of the session that ran them merged the result.
Built with the `l4` 1.6.110 (main, e51181d, 2026-11-11) and compared with 1.6.109 (main, 4c887e0, 2026-11-04); every module has the same four counts on both builds.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`ccc-core.l4`, `ccc-definitions.l4` and `ccc-interpretation.l4`, with the tests of the last two) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
32 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `ccc1` (lines 273 to 849), `ccc2` (lines 850 to 1248), `ccc3` (lines 1249 to 1903), `ccc4` (lines 1904 to 2381), `ccc5` (lines 2382 to 2989), `ccc6` (lines 2990 to 3518), `ccc7` (lines 3519 to 4117), `ccc8` (lines 4118 to 5031), `ccc9` (lines 5032 to 5568), `ccc10` (lines 5569 to 6176), `ccc11` (lines 6177 to 6510), `ccc12` (lines 6511 to 7144), `ccc13` (lines 7145 to 7874), `ccc14` (lines 7875 to 8523), `ccc15` (lines 8524 to 8718), `ccc16` (lines 8719 to 9543), `ccc17` (lines 9544 to 10274), `ccc18` (lines 10275 to 10956), `ccc19` (lines 10957 to 11031), `ccc20` (lines 11032 to 11828), `ccc21` (lines 11829 to 12462), `ccc22` (lines 12463 to 13305), `ccc23` (lines 13306 to 14068), `ccc24` (lines 14069 to 14871), `ccc25` (lines 14872 to 15170), `ccc26` (lines 15171 to 15768), `ccc27` (lines 15769 to 16295), `ccc28` (lines 16296 to 16683), `ccc29` (lines 16684 to 17450), `ccc30` (lines 17451 to 18463), `ccc31` (lines 18464 to 19055), `ccc32` (lines 19056 to 19797).
The lead verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the core identical to the keel's) and then merged them with a script. The merge edited no rule. What it did change: it copied the part modules unchanged, except that `ccc4-cases-seat-expected-red.l4` imports the merged seat module instead of its part's; it concatenated the parts' seat files; it replaced the maintainer's and the coordinator's names, and local paths, in comments and notes, and proved line by line that no code part of any `.l4` line changed; and it wrote this file and the other top-level files. Before the merge, `ccc29` renamed its own top-level definition `s 787(1) the general penalty for an offence punishable on summary conviction` to `s 787(1) the general penalty as stated in section 787(1)`, because the same name is a seat input of `ccc10` and made the merged seat module ambiguous (assumed, not ruled; see its notes).
After the parts returned, five further things were done, each by the part's own agent resumed with a short task, or by a separate reader; they are described in their own sections below:
1. a **seat-question audit** (section 'The seat-question audits');
2. a **name test for functions named for a grant or a power** (section 'The grant and power name test');
3. an **independent test pass** by six readers who saw only the text and the modules (section 'The independent test pass');
4. the **follow-ups** that the readers' findings and the merge called for, made by the part agents (`ccc9` added a bar for s 278.2(3) after a reader found no function for it; `ccc29` renamed one definition and added breach traces);
5. the **merged gate**, below.

Every note a part wrote is kept, with names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md` and, where it wrote one, its `NEEDS-CORE.md`; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `ccc-seat.l4` and `ccc-cases-seat.l4`, with one banner comment per part; the text under each banner is the part's, unchanged. The merged seat module imports every part module and was checked on its own before the gate: no error and no warning.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (each part's notes have a Seams section). The merge does not wire one part's output into another's input, so the seat asks the person each such fact. A scan of the part modules for inputs named `s 2 <term>: <fact>` (names only, made at the merge) found 109 distinct inputs; the keel has 86 `s 2` functions with typed arguments, and 1 input name equals a keel function name. An input is a proposition ("the thing is a firearm") and a keel function is the term ("firearm"), so none can be wired by name; connecting them is later work. Information, not a defect.
- **NEEDS-CORE requests are not hoisted.** They are gathered in `NEEDS-CORE.md` (proposed, not landed); the core is the keel's, unchanged.
- **Part-local types and helper names stay where they are.** Every top-level name carries the label of its section or its part prefix; the merged seat module imports all part modules at once and compiles, so no two modules define the same name.
- **The merge lost nothing:** the merged folder was gated as it stands: 555 modules, 45,541 assertions satisfied (below).

## Where things are

| agent | text (lines of `R.S.C.-1985-c.-C-46.txt`) | modules | assertions in its test modules | seat questions |
| --- | --- | --- | --- | --- |
| keel | 1 to 272 | 3 | 691 | 0 |
| ccc1 | 273 to 849 | 14 | 1114 | 107 |
| ccc2 | 850 to 1248 | 9 | 713 | 107 |
| ccc3 | 1249 to 1903 | 9 | 1013 | 117 |
| ccc4 | 1904 to 2381 | 4 | 1376 | 121 |
| ccc5 | 2382 to 2989 | 7 | 1477 | 268 |
| ccc6 | 2990 to 3518 | 15 | 1093 | 175 |
| ccc7 | 3519 to 4117 | 10 | 1054 | 61 |
| ccc8 | 4118 to 5031 | 11 | 1277 | 201 |
| ccc9 | 5032 to 5568 | 5 | 881 | 68 |
| ccc10 | 5569 to 6176 | 8 | 1059 | 205 |
| ccc11 | 6177 to 6510 | 7 | 731 | 106 |
| ccc12 | 6511 to 7144 | 11 | 1079 | 233 |
| ccc13 | 7145 to 7874 | 12 | 1205 | 205 |
| ccc14 | 7875 to 8523 | 8 | 1084 | 101 |
| ccc15 | 8524 to 8718 | 5 | 461 | 59 |
| ccc16 | 8719 to 9543 | 7 | 1370 | 79 |
| ccc17 | 9544 to 10274 | 7 | 1110 | 52 |
| ccc18 | 10275 to 10956 | 8 | 1076 | 58 |
| ccc19 | 10957 to 11031 | 5 | 161 | 21 |
| ccc20 | 11032 to 11828 | 11 | 1383 | 36 |
| ccc21 | 11829 to 12462 | 6 | 1245 | 96 |
| ccc22 | 12463 to 13305 | 13 | 1284 | 104 |
| ccc23 | 13306 to 14068 | 14 | 1116 | 81 |
| ccc24 | 14069 to 14871 | 7 | 1022 | 136 |
| ccc25 | 14872 to 15170 | 3 | 479 | 54 |
| ccc26 | 15171 to 15768 | 9 | 1044 | 213 |
| ccc27 | 15769 to 16295 | 10 | 1004 | 68 |
| ccc28 | 16296 to 16683 | 6 | 862 | 38 |
| ccc29 | 16684 to 17450 | 10 | 1359 | 74 |
| ccc30 | 17451 to 18463 | 7 | 619 | 44 |
| ccc31 | 18464 to 19055 | 6 | 528 | 56 |
| ccc32 | 19056 to 19797 | 8 | 683 | 147 |
| seat cases, all parts | | 1 (`ccc-cases-seat.l4`) | 10195 | |
| independent tests, six readers | | 6 (`tests-independent-g1.l4` to `g6`) | 2693 | |

The seat layer is `ccc-seat.l4` (3,491 `@export` questions in all) and `ccc-cases-seat.l4`; every other module is layer 1, with a tests module beside it.

## The source

The text is `../../registers/source-bundle/R.S.C.-1985-c.-C-46.txt` (19,797 lines, sha256 `a2ba9a394f5acd23ccd9f825df1d423204e20e1fa53d33096b549c480a49cdf2`), a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation of the Criminal Code (R.S.C., 1985, c. C-46), current to 2026-09-30 and last amended 2026-07-18. It is not the official text, and nothing here is claimed verified against the official text. "Verified" in this folder means only that every quotation in the `.l4` files was checked, by `srcrefs.py`, against that rendering. The French version is equally authoritative and was not among the sources.

## The seat

From the keel's notes:

The seat is a person who is, or may be, accused of an offence under the Criminal Code, asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply from arrest through trial, sentence and appeal, and what follows from a conviction (assumed, not ruled: Singapore's Penal Code is the model, per the maintainer's instruction of 2026-11-09, but this is a plain seat layer; no charge-generator contract).
This range holds no question the accused asks directly: it holds the vocabulary every other part reads. So there is no `@export` and no `@desc` here, and no seat layer; the lead's seat layer is built after the merge. Provisions that address only an official (section 2.3, the Attorney General) are encoded for what they mean for the accused: who may prosecute them.

The keel's own range holds no seat question; each part wrote the seat questions of its own range.

## What check.sh prints

Run as `L4=<stable 1.6.110> L4_MAIN=<main 1.6.109> ./check.sh` on the merged folder, exit 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-cases-seat.l4                              0     10195       0        0         0 |      0     10195       0        0  same
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions-tests.l4                       0       557       0        0         0 |      0       557       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation-tests.l4                    0       134       0        0         0 |      0       134       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc1-s21-24-parties.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc1-s25-law-enforcement.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc1-s25-reports.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc1-s26-33-force.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc1-s3-6-interpretation.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc1-s33-45-defences.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-aircraft-platforms-ships.l4            0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-base.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-citizens-and-procedure.l4              0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-definitions-and-evidence.l4            0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-persons-and-terrorism.l4               0         0       0        0         0 |      0         0       0        0  same
ccc1-s7-space.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc1-s8-20-general.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc1-support.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc1-tests-s21-24-parties.l4                   0        63       0        0         0 |      0        63       0        0  same
ccc1-tests-s25-law-enforcement.l4              0       134       0        0         0 |      0       134       0        0  same
ccc1-tests-s25-reports.l4                      0        29       0        0         0 |      0        29       0        0  same
ccc1-tests-s26-33-force.l4                     0       107       0        0         0 |      0       107       0        0  same
ccc1-tests-s3-6-interpretation.l4              0        73       0        0         0 |      0        73       0        0  same
ccc1-tests-s33-45-defences.l4                  0        82       0        0         0 |      0        82       0        0  same
ccc1-tests-s7-aircraft-platforms-ships.l4       0        84       0        0         0 |      0        84       0        0  same
ccc1-tests-s7-citizens-and-procedure.l4        0        84       0        0         0 |      0        84       0        0  same
ccc1-tests-s7-definitions-and-evidence.l4       0        58       0        0         0 |      0        58       0        0  same
ccc1-tests-s7-persons-and-terrorism.l4         0       169       0        0         0 |      0       169       0        0  same
ccc1-tests-s7-space.l4                         0        95       0        0         0 |      0        95       0        0  same
ccc1-tests-s8-20-general.l4                    0       136       0        0         0 |      0       136       0        0  same
ccc10-conversion.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc10-hate-crime.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc10-hate.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc10-kidnapping.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc10-libel.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc10-marriage.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc10-records.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc10-sexual-services.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc10-tests-conversion.l4                      0        31       0        0         0 |      0        31       0        0  same
ccc10-tests-hate-crime.l4                      0        43       0        0         0 |      0        43       0        0  same
ccc10-tests-hate.l4                            0       192       0        0         0 |      0       192       0        0  same
ccc10-tests-kidnapping.l4                      0       241       0        0         0 |      0       241       0        0  same
ccc10-tests-libel.l4                           0       177       0        0         0 |      0       177       0        0  same
ccc10-tests-marriage.l4                        0        87       0        0         0 |      0        87       0        0  same
ccc10-tests-records.l4                         0       162       0        0         0 |      0       162       0        0  same
ccc10-tests-sexual-services.l4                 0       126       0        0         0 |      0       126       0        0  same
ccc11-definitions.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc11-evidence.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc11-general.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc11-investigation.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc11-offences.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc11-orders.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc11-punishment.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc11-tests-definitions.l4                     0        73       0        0         0 |      0        73       0        0  same
ccc11-tests-evidence.l4                        0       122       0        0         0 |      0       122       0        0  same
ccc11-tests-general.l4                         0        53       0        0         0 |      0        53       0        0  same
ccc11-tests-investigation.l4                   0       112       0        0         0 |      0       112       0        0  same
ccc11-tests-offences.l4                        0       129       0        0         0 |      0       129       0        0  same
ccc11-tests-orders.l4                          0       111       0        0         0 |      0       111       0        0  same
ccc11-tests-punishment.l4                      0       131       0        0         0 |      0       131       0        0  same
ccc12-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-break-enter.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-criminal-interest.l4               0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-false-pretences.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-forgery.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-interpretation.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-possession.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-resembling-theft.l4                0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-robbery-extortion.l4               0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-theft.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-break-enter.l4                     0       125       0        0         0 |      0       125       0        0  same
ccc12-tests-criminal-interest.l4               0        90       0        0         0 |      0        90       0        0  same
ccc12-tests-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-false-pretences.l4                 0        82       0        0         0 |      0        82       0        0  same
ccc12-tests-fixtures.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-forgery.l4                         0       137       0        0         0 |      0       137       0        0  same
ccc12-tests-interpretation.l4                  0        41       0        0         0 |      0        41       0        0  same
ccc12-tests-logic.l4                           0        28       0        0         0 |      0        28       0        0  same
ccc12-tests-possession.l4                      0        75       0        0         0 |      0        75       0        0  same
ccc12-tests-resembling-theft.l4                0       216       0        0         0 |      0       216       0        0  same
ccc12-tests-robbery-extortion.l4               0       103       0        0         0 |      0       103       0        0  same
ccc12-tests-theft.l4                           0       182       0        0         0 |      0       182       0        0  same
ccc13-animals.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc13-arson-property.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc13-contract-intimidation.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc13-documents-identity.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc13-fares-minerals.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc13-fraud.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc13-index.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc13-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc13-mischief.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc13-securities-title.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc13-tests-animals.l4                         0       143       0        0         0 |      0       143       0        0  same
ccc13-tests-arson-property.l4                  0        98       0        0         0 |      0        98       0        0  same
ccc13-tests-contract-intimidation.l4           0       143       0        0         0 |      0       143       0        0  same
ccc13-tests-documents-identity.l4              0       109       0        0         0 |      0       109       0        0  same
ccc13-tests-fares-minerals.l4                  0       114       0        0         0 |      0       114       0        0  same
ccc13-tests-fraud.l4                           0        93       0        0         0 |      0        93       0        0  same
ccc13-tests-index.l4                           0        50       0        0         0 |      0        50       0        0  same
ccc13-tests-logic.l4                           0        16       0        0         0 |      0        16       0        0  same
ccc13-tests-mischief.l4                        0       169       0        0         0 |      0       169       0        0  same
ccc13-tests-securities-title.l4                0       132       0        0         0 |      0       132       0        0  same
ccc13-tests-support.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc13-tests-trademarks.l4                      0        54       0        0         0 |      0        54       0        0  same
ccc13-tests-wreck-stores.l4                    0        84       0        0         0 |      0        84       0        0  same
ccc13-trademarks.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc13-wreck-stores.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc14-helpers.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc14-part12-currency.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc14-part122-disclosure.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc14-part122-forfeiture.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc14-part122-offence.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc14-part122-warrants.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc14-part13-attempts.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc14-part13-criminal-organization.l4          0         0       0        0         0 |      0         0       0        0  same
ccc14-tests-part12-currency.l4                 0       159       0        0         0 |      0       159       0        0  same
ccc14-tests-part122-disclosure.l4              0       148       0        0         0 |      0       148       0        0  same
ccc14-tests-part122-forfeiture.l4              0       247       0        0         0 |      0       247       0        0  same
ccc14-tests-part122-offence.l4                 0        55       0        0         0 |      0        55       0        0  same
ccc14-tests-part122-warrants.l4                0       274       0        0         0 |      0       274       0        0  same
ccc14-tests-part13-attempts.l4                 0       113       0        0         0 |      0       113       0        0  same
ccc14-tests-part13-criminal-organization.l4       0        88       0        0         0 |      0        88       0        0  same
ccc15-duties.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc15-general.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc15-rules.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc15-special.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc15-tests-duties.l4                          0        17       0        0         0 |      0        17       0        0  same
ccc15-tests-general.l4                         0       109       0        0         0 |      0       109       0        0  same
ccc15-tests-rules.l4                           0        99       0        0         0 |      0        99       0        0  same
ccc15-tests-special.l4                         0       138       0        0         0 |      0       138       0        0  same
ccc15-tests-venue.l4                           0        98       0        0         0 |      0        98       0        0  same
ccc15-venue.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc16-dna-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc16-officials.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc16-open-court.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc16-preservation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc16-production-orders.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc16-publication-bans.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc16-search-warrants.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc16-tests-dna-definitions.l4                 0       156       0        0         0 |      0       156       0        0  same
ccc16-tests-dna-rows.l4                        0       247       0        0         0 |      0       247       0        0  same
ccc16-tests-officials.l4                       0        77       0        0         0 |      0        77       0        0  same
ccc16-tests-open-court.l4                      0       236       0        0         0 |      0       236       0        0  same
ccc16-tests-preservation.l4                    0       111       0        0         0 |      0       111       0        0  same
ccc16-tests-production-orders.l4               0       272       0        0         0 |      0       272       0        0  same
ccc16-tests-publication-bans.l4                0       185       0        0         0 |      0       185       0        0  same
ccc16-tests-search-warrants.l4                 0        86       0        0         0 |      0        86       0        0  same
ccc17-dna-orders.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc17-dna-samples.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc17-journalists.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc17-privilege.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc17-seizure.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc17-sor.l4                                   0         0       0        0         0 |      0         0       0        0  same
ccc17-tests-dna-orders.l4                      0       174       0        0         0 |      0       174       0        0  same
ccc17-tests-dna-samples.l4                     0       146       0        0         0 |      0       146       0        0  same
ccc17-tests-journalists.l4                     0        84       0        0         0 |      0        84       0        0  same
ccc17-tests-privilege.l4                       0        73       0        0         0 |      0        73       0        0  same
ccc17-tests-seizure.l4                         0       129       0        0         0 |      0       129       0        0  same
ccc17-tests-sor.l4                             0       366       0        0         0 |      0       366       0        0  same
ccc17-tests-warrants.l4                        0       138       0        0         0 |      0       138       0        0  same
ccc17-warrants.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc18-forfeiture.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-additional.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-foreign.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-itoa.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-notice.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-offences.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc18-tests-forfeiture.l4                      0       198       0        0         0 |      0       198       0        0  same
ccc18-tests-soira-additional.l4                0        87       0        0         0 |      0        87       0        0  same
ccc18-tests-soira-foreign.l4                   0       174       0        0         0 |      0       174       0        0  same
ccc18-tests-soira-itoa.l4                      0       119       0        0         0 |      0       119       0        0  same
ccc18-tests-soira-notice.l4                    0       190       0        0         0 |      0       190       0        0  same
ccc18-tests-soira-offences.l4                  0        69       0        0         0 |      0        69       0        0  same
ccc18-tests-tracking.l4                        0       119       0        0         0 |      0       119       0        0  same
ccc18-tests-weapons-evidence.l4                0       120       0        0         0 |      0       120       0        0  same
ccc18-tracking.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc18-weapons-evidence.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-21-to-24.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-25.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-26.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-27-to-3.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-31.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-tests-s492-21-to-24.l4                   0        30       0        0         0 |      0        30       0        0  same
ccc19-tests-s492-25.l4                         0        14       0        0         0 |      0        14       0        0  same
ccc19-tests-s492-26.l4                         0        13       0        0         0 |      0        13       0        0  same
ccc19-tests-s492-27-to-3.l4                    0        92       0        0         0 |      0        92       0        0  same
ccc19-tests-s492-31.l4                         0        12       0        0         0 |      0        12       0        0  same
ccc2-drilling-entry.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc2-explosives.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc2-nuclear-prize-fights.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc2-official-documents.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc2-piracy-air-sea.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc2-prohibited-acts.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc2-riots.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc2-sedition.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc2-tests-drilling-entry.l4                   0        38       0        0         0 |      0        38       0        0  same
ccc2-tests-explosives.l4                       0        58       0        0         0 |      0        58       0        0  same
ccc2-tests-nuclear-prize-fights.l4             0        77       0        0         0 |      0        77       0        0  same
ccc2-tests-official-documents.l4               0        88       0        0         0 |      0        88       0        0  same
ccc2-tests-piracy-air-sea.l4                   0       105       0        0         0 |      0       105       0        0  same
ccc2-tests-prohibited-acts.l4                  0       121       0        0         0 |      0       121       0        0  same
ccc2-tests-riots.l4                            0        93       0        0         0 |      0        93       0        0  same
ccc2-tests-sedition.l4                         0        57       0        0         0 |      0        57       0        0  same
ccc2-tests-treason.l4                          0        76       0        0         0 |      0        76       0        0  same
ccc2-treason.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-arrest.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-failure-and-delay.l4              0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-interim-release.l4                0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-interpretation.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-notices.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-principles.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-prisoners-and-entry.l4            0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-process.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-reverse-onus.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-review.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-taking-before-justice.l4          0         0       0        0         0 |      0         0       0        0  same
ccc20-tests-arrest.l4                          0        85       0        0         0 |      0        85       0        0  same
ccc20-tests-failure-and-delay.l4               0       224       0        0         0 |      0       224       0        0  same
ccc20-tests-fixtures.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-tests-interim-release.l4                 0       218       0        0         0 |      0       218       0        0  same
ccc20-tests-interpretation.l4                  0        45       0        0         0 |      0        45       0        0  same
ccc20-tests-notices.l4                         0        85       0        0         0 |      0        85       0        0  same
ccc20-tests-principles.l4                      0        52       0        0         0 |      0        52       0        0  same
ccc20-tests-prisoners-and-entry.l4             0       117       0        0         0 |      0       117       0        0  same
ccc20-tests-process.l4                         0       160       0        0         0 |      0       160       0        0  same
ccc20-tests-reverse-onus.l4                    0       205       0        0         0 |      0       205       0        0  same
ccc20-tests-review.l4                          0       140       0        0         0 |      0       140       0        0  same
ccc20-tests-taking-before-justice.l4           0        52       0        0         0 |      0        52       0        0  same
ccc21-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc21-part-17.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc21-part-18-1.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc21-part-18.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc21-part-19-absolute.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc21-part-19.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc21-tests-part-17.l4                         0        92       0        0         0 |      0        92       0        0  same
ccc21-tests-part-18-1.l4                       0       102       0        0         0 |      0       102       0        0  same
ccc21-tests-part-18-election.l4                0       242       0        0         0 |      0       242       0        0  same
ccc21-tests-part-18-inquiry.l4                 0       316       0        0         0 |      0       316       0        0  same
ccc21-tests-part-19-absolute.l4                0        59       0        0         0 |      0        59       0        0  same
ccc21-tests-part-19.l4                         0       434       0        0         0 |      0       434       0        0  same
ccc22-amendment.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc22-at-large.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc22-counts.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc22-evidence.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc22-indictments.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc22-joinder.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc22-juries.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc22-jury-defects.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc22-nunavut.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc22-organizations.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc22-pleas.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc22-tests-amendment.l4                       0        83       0        0         0 |      0        83       0        0  same
ccc22-tests-at-large.l4                        0        46       0        0         0 |      0        46       0        0  same
ccc22-tests-counts.l4                          0        77       0        0         0 |      0        77       0        0  same
ccc22-tests-evidence.l4                        0       149       0        0         0 |      0       149       0        0  same
ccc22-tests-indictments.l4                     0       100       0        0         0 |      0       100       0        0  same
ccc22-tests-joinder.l4                         0        55       0        0         0 |      0        55       0        0  same
ccc22-tests-juries.l4                          0       171       0        0         0 |      0       171       0        0  same
ccc22-tests-jury-defects.l4                    0        21       0        0         0 |      0        21       0        0  same
ccc22-tests-nunavut.l4                         0        82       0        0         0 |      0        82       0        0  same
ccc22-tests-organizations.l4                   0        34       0        0         0 |      0        34       0        0  same
ccc22-tests-pleas.l4                           0       148       0        0         0 |      0       148       0        0  same
ccc22-tests-trial.l4                           0       177       0        0         0 |      0       177       0        0  same
ccc22-tests-verdicts.l4                        0       141       0        0         0 |      0       141       0        0  same
ccc22-trial.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc22-verdicts.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc23-appeals.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc23-assessment.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc23-disposition-information.l4               0         0       0        0         0 |      0         0       0        0  same
ccc23-dispositions.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc23-fitness.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc23-hearing-procedure.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc23-hearings.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc23-high-risk.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc23-interpretation.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc23-publication.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc23-review-boards.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc23-reviews.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc23-tests-appeals.l4                         0        66       0        0         0 |      0        66       0        0  same
ccc23-tests-assessment.l4                      0       135       0        0         0 |      0       135       0        0  same
ccc23-tests-disposition-information.l4         0        55       0        0         0 |      0        55       0        0  same
ccc23-tests-dispositions.l4                    0        88       0        0         0 |      0        88       0        0  same
ccc23-tests-fitness.l4                         0        79       0        0         0 |      0        79       0        0  same
ccc23-tests-hearing-procedure.l4               0       105       0        0         0 |      0       105       0        0  same
ccc23-tests-hearings.l4                        0        51       0        0         0 |      0        51       0        0  same
ccc23-tests-high-risk.l4                       0        80       0        0         0 |      0        80       0        0  same
ccc23-tests-interpretation.l4                  0        60       0        0         0 |      0        60       0        0  same
ccc23-tests-publication.l4                     0        58       0        0         0 |      0        58       0        0  same
ccc23-tests-review-boards.l4                   0        37       0        0         0 |      0        37       0        0  same
ccc23-tests-reviews.l4                         0       147       0        0         0 |      0       147       0        0  same
ccc23-tests-transfers.l4                       0       122       0        0         0 |      0       122       0        0  same
ccc23-tests-verdict.l4                         0        33       0        0         0 |      0        33       0        0  same
ccc23-transfers.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc23-verdict.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc24-appeal-procedure.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc24-appeal-right.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc24-appeal-scc.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc24-attendance.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc24-evidence.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc24-ministerial-review.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc24-remote.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc24-tests-appeal-procedure.l4                0       274       0        0         0 |      0       274       0        0  same
ccc24-tests-appeal-right.l4                    0       145       0        0         0 |      0       145       0        0  same
ccc24-tests-appeal-scc.l4                      0        71       0        0         0 |      0        71       0        0  same
ccc24-tests-attendance.l4                      0       179       0        0         0 |      0       179       0        0  same
ccc24-tests-evidence.l4                        0       131       0        0         0 |      0       131       0        0  same
ccc24-tests-ministerial-review.l4              0       130       0        0         0 |      0       130       0        0  same
ccc24-tests-remote.l4                          0        92       0        0         0 |      0        92       0        0  same
ccc25-alternative-measures.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc25-remediation-approval.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc25-remediation-negotiation.l4               0         0       0        0         0 |      0         0       0        0  same
ccc25-tests-alternative-measures.l4            0       196       0        0         0 |      0       196       0        0  same
ccc25-tests-remediation-approval.l4            0       148       0        0         0 |      0       148       0        0  same
ccc25-tests-remediation-negotiation.l4         0       135       0        0         0 |      0       135       0        0  same
ccc26-discharge.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc26-fines.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc26-hearing.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc26-interpretation.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc26-principles.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc26-probation-orders.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc26-probation.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc26-punishment.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc26-reports.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc26-tests-discharge.l4                       0        76       0        0         0 |      0        76       0        0  same
ccc26-tests-fines.l4                           0       158       0        0         0 |      0       158       0        0  same
ccc26-tests-hearing.l4                         0       178       0        0         0 |      0       178       0        0  same
ccc26-tests-interpretation.l4                  0        89       0        0         0 |      0        89       0        0  same
ccc26-tests-principles.l4                      0        90       0        0         0 |      0        90       0        0  same
ccc26-tests-probation-orders.l4                0       115       0        0         0 |      0       115       0        0  same
ccc26-tests-probation.l4                       0       133       0        0         0 |      0       133       0        0  same
ccc26-tests-punishment.l4                      0        89       0        0         0 |      0        89       0        0  same
ccc26-tests-reports.l4                         0       116       0        0         0 |      0       116       0        0  same
ccc27-length.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc27-s737-1-restitution.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc27-s737-surcharge.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc27-s742-4-breach-and-transfer.l4            0         0       0        0         0 |      0         0       0        0  same
ccc27-s742-conditional-sentence.l4             0         0       0        0         0 |      0         0       0        0  same
ccc27-s743-imprisonment.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc27-s745-6-review.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc27-s745-life-sentence.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc27-s746-parole.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc27-s748-pardons-disabilities.l4             0         0       0        0         0 |      0         0       0        0  same
ccc27-tests-s737-1.l4                          0       100       0        0         0 |      0       100       0        0  same
ccc27-tests-s737.l4                            0        59       0        0         0 |      0        59       0        0  same
ccc27-tests-s742-4.l4                          0       167       0        0         0 |      0       167       0        0  same
ccc27-tests-s742.l4                            0       156       0        0         0 |      0       156       0        0  same
ccc27-tests-s743.l4                            0       138       0        0         0 |      0       138       0        0  same
ccc27-tests-s745-6.l4                          0       162       0        0         0 |      0       162       0        0  same
ccc27-tests-s745.l4                            0       120       0        0         0 |      0       120       0        0  same
ccc27-tests-s746.l4                            0        40       0        0         0 |      0        40       0        0  same
ccc27-tests-s748.l4                            0        62       0        0         0 |      0        62       0        0  same
ccc28-part24-s752.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc28-part24a-dangerous-offender.l4            0         0       0        0         0 |      0         0       0        0  same
ccc28-part24b-long-term.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc28-part24c-hearing-appeal.l4                0         0       0        0         0 |      0         0       0        0  same
ccc28-part25-forfeiture.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc28-part26-extraordinary-remedies.l4         0         0       0        0         0 |      0         0       0        0  same
ccc28-tests-part24-s752.l4                     0       227       0        0         0 |      0       227       0        0  same
ccc28-tests-part24a.l4                         0       127       0        0         0 |      0       127       0        0  same
ccc28-tests-part24b.l4                         0       137       0        0         0 |      0       137       0        0  same
ccc28-tests-part24c.l4                         0        58       0        0         0 |      0        58       0        0  same
ccc28-tests-part25.l4                          0       189       0        0         0 |      0       189       0        0  same
ccc28-tests-part26.l4                          0       124       0        0         0 |      0       124       0        0  same
ccc29-tests-xxvii-a.l4                         0        96       0        0         0 |      0        96       0        0  same
ccc29-tests-xxvii-b.l4                         0       158       0        0         0 |      0       158       0        0  same
ccc29-tests-xxviii-0-peace-810.l4              0       138       0        0         0 |      0       138       0        0  same
ccc29-tests-xxviii-1-peace-810-02.l4           0        87       0        0         0 |      0        87       0        0  same
ccc29-tests-xxviii-2-peace-810-1.l4            0       125       0        0         0 |      0       125       0        0  same
ccc29-tests-xxviii-3-peace-810-21.l4           0       126       0        0         0 |      0       126       0        0  same
ccc29-tests-xxviii-4-appeal-812.l4             0       203       0        0         0 |      0       203       0        0  same
ccc29-tests-xxviii-5-appeal-829.l4             0        96       0        0         0 |      0        96       0        0  same
ccc29-tests-xxviii-6-part-xxviii.l4            0        46       0        0         0 |      0        46       0        0  same
ccc29-tests-xxviii-7-schedules.l4              0       284       0        0         0 |      0       284       0        0  same
ccc29-xxvii-a-interpretation-penalty.l4        0         0       0        0         0 |      0         0       0        0  same
ccc29-xxvii-b-information-trial.l4             0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-0-peace-810.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-1-peace-810-02.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-2-peace-810-1.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-3-peace-810-21.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-4-appeal-812.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-5-appeal-829.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-6-part-xxviii.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-7-schedules.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc3-authorization.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc3-financing.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc3-forfeiture.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc3-freezing.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc3-interpretation.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc3-listing.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc3-participation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc3-proceedings.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc3-recognizance.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc3-tests-authorization.l4                    0       185       0        0         0 |      0       185       0        0  same
ccc3-tests-financing.l4                        0        60       0        0         0 |      0        60       0        0  same
ccc3-tests-forfeiture.l4                       0       142       0        0         0 |      0       142       0        0  same
ccc3-tests-freezing.l4                         0        68       0        0         0 |      0        68       0        0  same
ccc3-tests-interpretation.l4                   0        76       0        0         0 |      0        76       0        0  same
ccc3-tests-listing.l4                          0        67       0        0         0 |      0        67       0        0  same
ccc3-tests-participation.l4                    0       201       0        0         0 |      0       201       0        0  same
ccc3-tests-proceedings.l4                      0        45       0        0         0 |      0        45       0        0  same
ccc3-tests-recognizance.l4                     0       169       0        0         0 |      0       169       0        0  same
ccc30-forms-actors.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-appearance.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-dna.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-preservation.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-register.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-search.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc30-forms-warrants.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc30-tests-forms-appearance.l4                0       241       0        0         0 |      0       241       0        0  same
ccc30-tests-forms-dna.l4                       0        79       0        0         0 |      0        79       0        0  same
ccc30-tests-forms-preservation.l4              0       114       0        0         0 |      0       114       0        0  same
ccc30-tests-forms-register.l4                  0        85       0        0         0 |      0        85       0        0  same
ccc30-tests-forms-search.l4                    0        19       0        0         0 |      0        19       0        0  same
ccc30-tests-forms-warrants.l4                  0        81       0        0         0 |      0        81       0        0  same
ccc31-forms-custody.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-orders.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-periods.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-process.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-soira.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-statements.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc31-tests-custody.l4                         0        93       0        0         0 |      0        93       0        0  same
ccc31-tests-orders.l4                          0       113       0        0         0 |      0       113       0        0  same
ccc31-tests-periods.l4                         0        17       0        0         0 |      0        17       0        0  same
ccc31-tests-process.l4                         0       116       0        0         0 |      0       116       0        0  same
ccc31-tests-soira.l4                           0       136       0        0         0 |      0       136       0        0  same
ccc31-tests-statements.l4                      0        53       0        0         0 |      0        53       0        0  same
ccc32-nif-1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-c19.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-soirsa.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-xxi1-transition.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-xxi1.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc32-related-1.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-related-2.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-related-3.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-tests-nif-1.l4                           0        21       0        0         0 |      0        21       0        0  same
ccc32-tests-nif-c19.l4                         0        70       0        0         0 |      0        70       0        0  same
ccc32-tests-nif-soirsa.l4                      0        74       0        0         0 |      0        74       0        0  same
ccc32-tests-nif-xxi1-transition.l4             0        60       0        0         0 |      0        60       0        0  same
ccc32-tests-nif-xxi1.l4                        0       115       0        0         0 |      0       115       0        0  same
ccc32-tests-related-1.l4                       0        94       0        0         0 |      0        94       0        0  same
ccc32-tests-related-2.l4                       0       137       0        0         0 |      0       137       0        0  same
ccc32-tests-related-3.l4                       0       112       0        0         0 |      0       112       0        0  same
ccc4-cases-seat-expected-red.l4                6         0       6        0         6 |      6         0       6        0  same
ccc4-s109-110-3-prohibition-orders.l4          0         0       0        0         0 |      0         0       0        0  same
ccc4-s84-definitions.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc4-s85-98-use-possession.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc4-s99-108-trafficking-and-others.l4         0         0       0        0         0 |      0         0       0        0  same
ccc4-tests-s109-110-3.l4                       0       337       0        0         0 |      0       337       0        0  same
ccc4-tests-s84.l4                              0       374       0        0         0 |      0       374       0        0  same
ccc4-tests-s85-98.l4                           0       332       0        0         0 |      0       332       0        0  same
ccc4-tests-s99-108.l4                          0       333       0        0         0 |      0       333       0        0  same
ccc5-s110-4-to-117.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-01-to-117-012.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-02-to-117-06.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-07-to-117-15.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc5-s118-to-130-1.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc5-s131-to-143.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc5-s144-to-149.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc5-tests-s110-4-to-117.l4                    0       165       0        0         0 |      0       165       0        0  same
ccc5-tests-s117-01-to-117-012.l4               0       209       0        0         0 |      0       209       0        0  same
ccc5-tests-s117-02-to-117-06.l4                0       137       0        0         0 |      0       137       0        0  same
ccc5-tests-s117-07-to-117-15.l4                0       141       0        0         0 |      0       141       0        0  same
ccc5-tests-s118-to-130-1.l4                    0       387       0        0         0 |      0       387       0        0  same
ccc5-tests-s131-to-143.l4                      0       203       0        0         0 |      0       203       0        0  same
ccc5-tests-s144-to-149.l4                      0       235       0        0         0 |      0       235       0        0  same
ccc6-bestiality.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc6-builders.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-children.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-csaem.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc6-disorderly.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc6-morals.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc6-offence-table.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc6-prohibition-orders.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc6-repealed.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-s150-1-consent.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc6-s150-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc6-s153-1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc6-seizure.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc6-sexual-offences.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc6-tests-bestiality.l4                       0        63       0        0         0 |      0        63       0        0  same
ccc6-tests-children.l4                         0       161       0        0         0 |      0       161       0        0  same
ccc6-tests-csaem.l4                            0        70       0        0         0 |      0        70       0        0  same
ccc6-tests-disorderly.l4                       0       120       0        0         0 |      0       120       0        0  same
ccc6-tests-morals.l4                           0        60       0        0         0 |      0        60       0        0  same
ccc6-tests-offence-table.l4                    0        31       0        0         0 |      0        31       0        0  same
ccc6-tests-prohibition-orders.l4               0       112       0        0         0 |      0       112       0        0  same
ccc6-tests-repealed.l4                         0        19       0        0         0 |      0        19       0        0  same
ccc6-tests-s150-1-consent.l4                   0        94       0        0         0 |      0        94       0        0  same
ccc6-tests-s150-definitions.l4                 0        18       0        0         0 |      0        18       0        0  same
ccc6-tests-s153-1.l4                           0        38       0        0         0 |      0        38       0        0  same
ccc6-tests-seizure.l4                          0       154       0        0         0 |      0       154       0        0  same
ccc6-tests-sexual-offences.l4                  0        68       0        0         0 |      0        68       0        0  same
ccc6-tests-support.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc6-tests-voyeurism.l4                        0        85       0        0         0 |      0        85       0        0  same
ccc6-voyeurism.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc7-s183-base.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc7-s183-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc7-s183-offence.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc7-s184-applications.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc7-s184-interception.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc7-s185-applications.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc7-s186-authorizations.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc7-s187-packet.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc7-s191-offences.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc7-s195-notification.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc7-tests-s183-definitions.l4                 0        79       0        0         0 |      0        79       0        0  same
ccc7-tests-s183-offence.l4                     0       238       0        0         0 |      0       238       0        0  same
ccc7-tests-s184-applications.l4                0        94       0        0         0 |      0        94       0        0  same
ccc7-tests-s184-interception.l4                0       123       0        0         0 |      0       123       0        0  same
ccc7-tests-s185-applications.l4                0        71       0        0         0 |      0        71       0        0  same
ccc7-tests-s186-authorizations.l4              0       131       0        0         0 |      0       131       0        0  same
ccc7-tests-s187-packet.l4                      0        77       0        0         0 |      0        77       0        0  same
ccc7-tests-s191-offences.l4                    0       125       0        0         0 |      0       125       0        0  same
ccc7-tests-s195-notification.l4                0       116       0        0         0 |      0       116       0        0  same
ccc8-part7-houses.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc8-part7-lotteries.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc8-part7-pari-mutuel.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-assaults.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-duties.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-harm.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-homicide.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-maid.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-murder.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc8-part8-organs-suicide.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc8-repealed.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc8-tests-part7-houses.l4                     0       138       0        0         0 |      0       138       0        0  same
ccc8-tests-part7-lotteries.l4                  0       148       0        0         0 |      0       148       0        0  same
ccc8-tests-part7-pari-mutuel.l4                0        63       0        0         0 |      0        63       0        0  same
ccc8-tests-part8-assaults.l4                   0       136       0        0         0 |      0       136       0        0  same
ccc8-tests-part8-duties.l4                     0        66       0        0         0 |      0        66       0        0  same
ccc8-tests-part8-harm.l4                       0       190       0        0         0 |      0       190       0        0  same
ccc8-tests-part8-homicide.l4                   0        81       0        0         0 |      0        81       0        0  same
ccc8-tests-part8-maid.l4                       0       169       0        0         0 |      0       169       0        0  same
ccc8-tests-part8-murder.l4                     0       184       0        0         0 |      0       184       0        0  same
ccc8-tests-part8-organs-suicide.l4             0        60       0        0         0 |      0        60       0        0  same
ccc8-tests-repealed.l4                         0        42       0        0         0 |      0        42       0        0  same
ccc9-assault-officer.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc9-records.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc9-sexual-assault.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc9-sexual-evidence.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc9-support.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc9-tests-assault-officer.l4                  0        84       0        0         0 |      0        84       0        0  same
ccc9-tests-records.l4                          0       307       0        0         0 |      0       307       0        0  same
ccc9-tests-sexual-assault.l4                   0       243       0        0         0 |      0       243       0        0  same
ccc9-tests-sexual-evidence.l4                  0       247       0        0         0 |      0       247       0        0  same
tests-independent-g1.l4                        0       387       0        0         0 |      0       387       0        0  same
tests-independent-g2.l4                        0       411       0        0         0 |      0       411       0        0  same
tests-independent-g3.l4                        0       883       0        0         0 |      0       883       0        0  same
tests-independent-g4.l4                        0       287       0        0         0 |      0       287       0        0  same
tests-independent-g5.l4                        0       340       0        0         0 |      0       340       0        0  same
tests-independent-g6.l4                        0       385       0        0         0 |      0       385       0        0  same
TOTAL (555 modules)                            6     45541       6        0           |      6     45541       6        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 45,541 assertions satisfied over 555 modules, with 6 errors and 6 failed, all of them the 6 expectations of `ccc4-cases-seat-expected-red.l4` (meant to fail, listed in `check.sh` as expected, and in `encoding.json` as `expected_red`), 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each part read its own traces on both builds by hand (see its NOTES).

## The seat-question audits

A seat question is the question as the person in the seat would ask it; its name must ask what the layer-1 function it calls answers, in the same direction. A question titled as a permission over a function that answers the bar (or the reverse) makes `JUST TRUE` read as the opposite of what it means, so each part was audited for it.
- **Second pass, by each part's own agent, resumed with only that task:** all 32 parts read every seat question's name and `@export` text against the BODY of the layer-1 function it calls, not against its own title, by four tests (a different limb, route or scope than the body answers; a premise or consequence the function does not compute; a wrong polarity or modal; a different type of answer). 209 of 3,462 seat questions were retitled (6.0%). Per part the share runs from 1.0% (`ccc22`, 1 of 104) to 48% (`ccc19`, 10 of 21); `ccc26` retitled none of 213. The other 5 parts with more than 200 questions retitled between 1.0% and 7.5%, so `ccc26`'s none is below all of them; its notes say it read all 213, retitled none and list 13 it read and left, each with a reason. The counts are each part's own, read from its notes by the lead (table below). Some parts also ran a first, direction-only pass when they wrote the seat layer; their notes give it.

| part | seat questions read | retitled | share |
| --- | --- | --- | --- |
| ccc1 | 107 | 2 | 1.9% |
| ccc2 | 107 | 8 | 7.5% |
| ccc3 | 117 | 3 | 2.6% |
| ccc4 | 121 | 11 | 9.1% |
| ccc5 | 268 | 4 | 1.5% |
| ccc6 | 147 | 10 | 6.8% |
| ccc7 | 61 | 24 | 39.3% |
| ccc8 | 201 | 15 | 7.5% |
| ccc9 | 67 | 3 | 4.5% |
| ccc10 | 205 | 2 | 1.0% |
| ccc11 | 106 | 8 | 7.5% |
| ccc12 | 233 | 4 | 1.7% |
| ccc13 | 205 | 2 | 1.0% |
| ccc14 | 101 | 6 | 5.9% |
| ccc15 | 59 | 5 | 8.5% |
| ccc16 | 79 | 8 | 10.1% |
| ccc17 | 52 | 12 | 23.1% |
| ccc18 | 58 | 3 | 5.2% |
| ccc19 | 21 | 10 | 47.6% |
| ccc20 | 36 | 3 | 8.3% |
| ccc21 | 96 | 3 | 3.1% |
| ccc22 | 104 | 1 | 1.0% |
| ccc23 | 81 | 1 | 1.2% |
| ccc24 | 136 | 11 | 8.1% |
| ccc25 | 54 | 7 | 13.0% |
| ccc26 | 213 | 0 | 0.0% |
| ccc27 | 68 | 4 | 5.9% |
| ccc28 | 38 | 4 | 10.5% |
| ccc29 | 74 | 1 | 1.4% |
| ccc30 | 44 | 7 | 15.9% |
| ccc31 | 56 | 9 | 16.1% |
| ccc32 | 147 | 18 | 12.2% |
| **all 32 parts** | **3,462** | **209** | **6.0%** |

The audit read 3,462 questions; `ccc-seat.l4` holds 3,491. The difference is two parts: `ccc6` added 28 questions after its second audit began (its notes: written against their bodies, so counted as not read) and `ccc9` holds 68 where its audit read 67 (its notes give both figures; the lead did not trace which question is the later one).

- **Retitle, not negate.** The fix was to retitle the question so that it asks what the function answers; `ccc7`, `ccc31` and `ccc32` say in terms that no answer was negated, and each other part's notes give its own account. A bar's `NOTHING` and `JUST FALSE` are not a grant.
- **Assertions restated in place** carry `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>` (the date is the date of the instruction; 167 such comments in the part modules).
- **Precision of the second pass, measured by the lead on the Companies Act 2006 encoding (limit stated), not repeated here.** The same pass, run over seven parts of that Act and one Canadian part, flagged 177 of 665 seat questions (27%). Of 20 flagged questions drawn at random from four of the UK parts (5 each, from the 104 whose old title can be recovered from the part's `RECONCILED` comments), the lead judged each against the function body without reading the agent's reason: 7 were real mismatches, 7 were borderline (the old title restated the function's own name and differed only from an input the function tests) and 6 were cosmetic. So about 35% of the flags were clear mismatches (70% with the borderline ones). **Limit: four of the eight parts could not be sampled, because their old titles are not recoverable from their comments, and the measurement was not repeated for the Criminal Code.** The brief of the pass was tightened afterwards to the four kinds of real mismatch; the parts done before the tightening were not re-run (the coordinating session agreed), so their retitles are accurate but sometimes more than needed.

## The grant and power name test

A function **named for a grant or a power** ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The Guide (section 5, "In short") gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". The coordinating session ruled on 2026-11-12, with three limits:
1. **Flip to `NOTHING`**, with one fork line each, only a function named for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an `if` gate failed.
2. **Keep `JUST FALSE`** where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question.
3. **Do not flip, list instead**, in the part's fork register: "may" functions whose gate is "where", "when" or "upon" (and the equivalents the parts placed with them: "in the case of", "so long as", "while", "on payment", "after ..."; **assumed, not ruled**, part by part), because ruling (b) of the Guide's periods, where and scope-limits paragraph says `JUST FALSE` and the Guide's line on grants points the other way: a question for the maintainer or a lawyer; and "entitled"-named functions, because an entitlement is a claim, not a power, and the Guide does not settle it.
Functions named "it is lawful ..." are outside the sweep (their answers are kept; a scoped name is kept and an unscoped one is retitled to the scoped form, "s N makes it lawful ..."). The parts that give a count report none, except `ccc8`, which retitled eight (s 207) and also retitled `s 207(1)(e)` and `s 207(1)(f)` to the same form for consistency.

The counts below are read from each part's own NOTES (section "Name-test sweep of 2026-11-12"); a function can be counted in two columns when its `if` branch is flipped and its `where` branch is listed.

| part | flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- | --- |
| ccc1 | 4 | 4 | 5 | 1 |
| ccc2 | 1 | 0 | 1 | 0 |
| ccc3 | 19 | 6 | 15 | 3 |
| ccc4 | 5 | 9 | 2 | 0 |
| ccc5 | 12 | 3 | 20 | 0 |
| ccc6 | 0 | 1 | 9 | 0 |
| ccc7 | 0 | 5 | 8 | 0 |
| ccc8 | 3 | 8 | 2 | 0 |
| ccc9 | 0 | 8 | 0 | 0 |
| ccc10 | 0 | 5 | 4 | 0 |
| ccc11 | 18 | 4 | 3 | 1 |
| ccc12 | 0 | 2 | 1 | 0 |
| ccc13 | 0 | 3 | 3 | 0 |
| ccc14 | 1 | 5 | 20 | 0 |
| ccc15 | 0 | 4 | 12 | 1 |
| ccc16 | 0 | 27 | 28 | 0 |
| ccc17 | 0 | 13 | 12 | 0 |
| ccc18 | 0 | 16 | 10 | 0 |
| ccc19 | 0 | 0 | 0 | 0 |
| ccc20 | 0 | 4 | 22 | 0 |
| ccc21 | 0 | 7 | 39 | 1 |
| ccc22 | 37 | 22 | 46 | 8 |
| ccc23 | 1 | 14 | 33 | 3 |
| ccc24 | 91 | 10 | 33 | 6 |
| ccc25 | 7 | 2 | 3 | 0 |
| ccc26 | 1 | 0 | 43 | 0 |
| ccc27 | 0 | 7 | 28 | 1 |
| ccc28 | 8 | 8 | 17 | 1 |
| ccc29 | 47 | 6 | 31 | 4 |
| ccc30 | 9 | 21 | 1 | 0 |
| ccc31 | 7 | 6 | 1 | 0 |
| ccc32 | 5 | 6 | 3 | 0 |
| **all 32 parts** | **276** | **236** | **455** | **30** |

**Open for the maintainer or a lawyer: the 455 listed "may" functions with a where/when/upon-kind gate and the 30 "entitled" functions.** They answer as the Guide's own rulings give (for a failed `where`, `JUST FALSE`; the other reading is `NOTHING`), and each has a row in its part's fork register naming the other reading.
**The first column counts the functions each part put in that group, not the answers the sweep changed.** Some parts wrote their answers to the ruling from the start, so the functions already answered `NOTHING` (`ccc16`, `ccc28` and `ccc29` say so in their notes). `ccc16` splits its listed group in two columns (a literal "Where", and an "on application" or "when" kind); the table above adds them.
**A flip changes what every caller of the function sees.** A part checked the callers in its own range (its sweep section says where); no part module imports another part's module (checked at the merge), so a caller is always in the same part and what crosses parts is a seam, which is an input.

## The independent test pass

Six readers, one per group of consecutive parts (a whole Act is too long for one), each read only the text of its group's ranges and wrote its scenarios and expected answers (`ANSWERS.md`, not kept) **before** opening any `.l4` file, then wrote `tests-independent-gN.l4` against the group's modules and ran it. A failing assertion was left failing; each reader then wrote a triage with a verdict word per failure: `ENCODER` (the encoding is wrong), `SCENARIO` (the reader's own mistake), `AMBIGUOUS` (the text reads both ways) or `GAP` (no function can be asked the scenario). Readers were given the Guide's FALSE and NOTHING convention verbatim, so their disagreements are about the text and not about the convention.

| group | parts | words of text | scenarios | assertions (as returned) | failed as returned | ENCODER | SCENARIO | AMBIGUOUS | GAP | assertions now |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g1 | ccc1 to ccc6 | 74,340 | 388 (346 from the text, 42 seat questions) | 387 | 34 | 11 | 11 | 12 | 1 | 387 |
| g2 | ccc7 to ccc12 | 73,035 | 416 | 409 | 36 | 19 | 11 | 6 | 7 | 411 |
| g3 | ccc13 to ccc18 | 79,176 | 516 | 883 | 41 | 28 | 8 | 5 | 2 | 883 |
| g4 | ccc19 to ccc23 | 70,215 | 265 (255 asserted, 10 with no function to ask) | 287 | 40 | 22 | 5 | 13 | 10 | 287 |
| g5 | ccc24 to ccc29 | 71,865 | 237 (200 from the text, 37 seat questions) | 340 | 40 | 2 | 9 | 29 | 4 | 340 |
| g6 | ccc30 to ccc32 | 37,850 | 415, plus 36 in an appendix and 49 seat questions | 385 | 19 | 0 | 5 | 14 | 115 | 385 |
| **all six** | | 406,481 | | **2,691** | **210** | **82** | **49** | **79** | **139** | **2,693** |

In every group the `ENCODER`, `SCENARIO` and `AMBIGUOUS` verdicts add up to "failed as returned" (the merge checks it). A `GAP` verdict is a scenario for which no function can be asked, so it has no assertion. `g2` ends with 2 more assertions than it returned: the lead wrote two for `s 278.2(3)`, the bar `ccc9` added after the reader found no function for it, and marked them as the lead's.

After the parts' audits and sweeps, each group's file was brought up to the final modules: a seat question renamed by an audit was renamed in the reader's file; a failure that was the reader's own mistake (`SCENARIO`), or a reading the text leaves open (`AMBIGUOUS`), was restated in place to the encoding's answer with a `-- RECONCILED <date>: was EQUALS <old>; <reason>` comment that cites the Guide sentence or says that none decides it (the date is the day it was restated, 2026-11-12 to 2026-11-17); a failure that was an `ENCODER` verdict was settled as the next paragraph says. **An `AMBIGUOUS` restatement is the encoder's reading, not a ruling:** it is recorded for a lawyer in the part's fork register.
**How the 82 `ENCODER` verdicts were settled.** A reader's `ENCODER` verdict is as returned. In every group the lead read the owning part's fork rows, sweep rows or ruling and restated the line to the encoding's answer where one of them documents it; the shapes were (a) a "may" whose "if", "with" or "who" gate fails, answered `NOTHING` under the name-test ruling of 2026-11-12 (the large majority; the reader's guide gives `JUST FALSE` in its worked example 1, so under that guide they would stand as `ENCODER`), (b) an unmet element of an offence (cross-part split 1 below), (c) a period or scope limit (cross-part split 2 below), and (d) three bars of `ccc17` that answer `NOTHING` inside a stated period under a `NOTHING`-kind comment and no fork row. **None of the verdicts led to a change of an answer of an existing function, and each is also a call for a lawyer.** The group logs name the sites.
The as-returned copy of each file (with its failing assertions) is `notes/independent/gN-tests-independent-as-returned.l4.txt`, and each reader's triage is `notes/independent/gN-triage.md`. **Independence, as each reader disclosed it to the lead (the disclosures are not kept in this folder).** The brief required each reader to finish `ANSWERS.md` before opening any `.l4` file, and gave each the Guide's section on `FALSE` and `NOTHING` verbatim. `g1` opened `s 787(1)` (outside its range) to set a stand-in penalty. `g3` read some function bodies and fork comments after its answers were frozen. `g4` read a few function bodies (`s 493.01`, `494(2)`, `495(3)`, `496`, `501(3)`, `515(6)(b.2)`) after freezing its answers, corrected two argument constructions and added one assertion, and changed no expected value. `g5` read function bodies and the encoding's own header and fork comments, also after its run, to write its triage, and chose its seat questions after reading the seat modules' question lists; it says it opened no NOTES, PROGRESS or plan file. `g6` opened `jl4/examples/ok` in the L4 checkout and read the `prelude` and `daydate` library files to learn the assertion syntax. For `g2` the lead did not record a disclosure; the triage files are the record. **Limit:** the modules' header comments restate the encoder's reading rules, and a reader who opened a module saw them, so the readers were not blind to the encoder's conventions once they had written their answers.

## Findings the merge leaves open (for a lawyer)

Status: **reported by the part agents and the readers; the lead read each cited line in the parts' notes on 2026-11-17 and the merge checks that each cited label is still in the cited file. None is resolved here, and none is a ruling.**

### Cross-part split 1: an unmet element of an offence

"Every one who ... is guilty of ..." and "Every person commits an offence who ...": when one element is not met, the parts split between `JUST FALSE` (the section's own question: "this section does not make it an offence on these facts") and `NOTHING` (the section says who is guilty and is silent about everyone else). The coordinating session's ruling of 2026-11-05 decides such sites case by case at encoding time, so the split is not an error. **Each part's reading below is the part's own, and nothing here harmonises them** (the coordinating session's instruction, assumed, not ruled by the maintainer). A caller reading an answer must read `NOTHING` as "this section does not reach you on these facts", never as "no offence".

| part | reading taken | sites, as the part states them | where in the part's notes |
| --- | --- | --- | --- |
| ccc2 | `NOTHING` | 48 provision keys (its jural-relations table) | `notes/ccc2-NOTES.md`, F1 |
| ccc3 | `JUST FALSE` | every offence function: ss 83.02, 83.03, 83.04, 83.12(1), 83.18(1), 83.181, 83.19(1), 83.191, 83.2, 83.201, 83.202, 83.21(1), 83.22(1), 83.221(1), 83.23, 83.231; `NOTHING` only where an element is a term another section defines and the person did not settle it | `notes/ccc3-NOTES.md`, F-ccc3-1 |
| ccc4 | `JUST FALSE` | the 31 offence subsections ss 85(1) to 108(1) listed in its F-OF; a limb written "without lawful excuse", "without being the holder of" or "otherwise than under the authority of" answers `NOTHING` | `notes/ccc4-NOTES.md`, F-OF |
| ccc6 | `NOTHING` | 71 rows (its F1 lists them, from s 151) | `notes/ccc6-NOTES.md`, F1 |
| ccc7 | `JUST FALSE` | not counted by the part: s 184(1), s 184.5(1), s 191(1) and the other offence subsections of its range | `notes/ccc7-NOTES.md`, marginal reading (a) |
| ccc8 | `NOTHING` | every `... the person commits the offence ...` function of its range (not counted); the exception is s 233, where the definition of the category "infanticide" answers `JUST FALSE` for a person outside it, because ss 231 and 234 consume it as a yes or no | `notes/ccc8-NOTES.md`, M1, and M8 (= F15) for s 233 |
| ccc9 | `JUST FALSE` | 6 provisions: ss 270(1), 270.01(1), 270.02, 270.1(1), 272(1), 273(1); the other reading, `NOTHING`, is named | `notes/ccc9-NOTES.md`, F2 |
| ccc10 | `NOTHING` | every offence function of the part (not counted; listed in its coverage table) | `notes/ccc10-NOTES.md`, F1 |
| ccc11 | `JUST FALSE` | the offence functions of ss 320.13 to 320.18 | `notes/ccc11-NOTES.md`, F18 |
| ccc12 | `JUST FALSE` | the offence provisions of its range (not counted): the part read the 2026-11-05 ruling as deciding it, so it has no fork row | `notes/ccc12-NOTES.md`, (no fork: the ruling decides) |
| ccc13 | `JUST FALSE` | 95 functions named `the conduct is the offence of ...`, and the offence functions of ss 394(5), 394.1(3), 403(2), 415, 423.1(3), 425.1(2), 430(1) and 430(1.1) | `notes/ccc13-NOTES.md`, F1 |
| ccc18 | `NOTHING` | 4 provisions: ss 490.031(1), 490.0311, 490.0312, 490.8(9) | `notes/ccc18-NOTES.md`, F15 |
| ccc27 | `JUST FALSE` | 6 functions (its rows under F-7), among them s 743.21(2); the relative clause "An offender who fails to pay ... is in default" is read the same way | `notes/ccc27-NOTES.md`, F-7 |
| ccc32 | `NOTHING` | 1 provision: s 264.01(1) (not in force) | `notes/ccc32-NOTES.md`, F11 |

So 8 parts read it as `JUST FALSE` (ccc3, ccc4, ccc7, ccc9, ccc11, ccc12, ccc13, ccc27) and 6 as `NOTHING` (ccc2, ccc6, ccc8, ccc10, ccc18, ccc32). **Not surveyed:** ccc1, ccc5, ccc14 to ccc17, ccc19 to ccc26, ccc28 to ccc31. The lead did not look for an offence-element fork row in them; an absence from the table is not agreement. The fork lines above are one per fork, not one per site; the sites are in each part's coverage table, in the rows that name the fork.

### Cross-part split 2: a gate on a "may" worded "where", "when", "upon", "on application", "on", "after" or a period (assumed, not ruled)

The lead's own reading of the parts' sweep sections, not an instruction. The sweep ruling says not to flip these to `NOTHING` but to list them: ruling (b) of the periods ruling gives `JUST FALSE` for a failed "where", and the Guide's line on grants points the other way. The parts placed the equivalents differently, and the answers differ. What each of these parts says it did:

| part | what the part's own notes say |
| --- | --- |
| ccc1 | 5 listed, left as the Guide's rulings give it: `JUST FALSE` (its F12) |
| ccc6 | 3 listed, `JUST FALSE` when the gate fails, as ruling (b) of 2026-11-05 gives; the other reading is `NOTHING` (its F9) |
| ccc12 | 1 listed (s 342.01(2), its F-MAY-WHERE): a failed "Where" answers `JUST FALSE` |
| ccc13 | 3 listed, `JUST FALSE` when the gate fails; the other reading is `NOTHING` |
| ccc16 | 4 with a literal "Where" gate: `JUST FALSE`; 24 of the "on application" / "when" kind: `NOTHING` kept |
| ccc18 | two functions that answered `NOTHING` on a gate introduced by "once" now answer `JUST FALSE`: s 490.026(4) and s 490.02912(3.1) |
| ccc20 | 22 listed, `JUST FALSE`, as the Guide's ruling gives |
| ccc25 | 3 listed (s 715.39(2), s 715.3(2) for its "when" gate, s 715.52(1)(b) for its "where" gate): `JUST FALSE`, as in the first version of its modules (F10.1 to F10.3) |
| ccc26 | 43 listed, none changed; it also placed gates worded "with", "during" and "in" with the "on" and "after" gates (an assumption it flags: S1 s 720(2), S3 s 722(6)(a), S8 s 724(1), S13 s 729(6), S14 s 729.1(4)) |

The other parts' listed counts are in the sweep table above, and each part's sweep section says how its listed functions answer; the lead did not read them all for this table. **Within a part or across parts the same shape is answered both ways in at least these places:**

- `ccc24`'s module header (`ccc24-appeal-procedure.l4`) and `ccc29`'s s 810.01(1) (fork F-810.01-1) answer `NOTHING` when the "with" or "if" gate of a "may" fails, while `ccc26` answers `JUST FALSE` for s 720(2) (fork F27: "with the consent of the Attorney General and the offender"). The group-5 reader found this and flagged it.
- `ccc17` answers `NOTHING` for the bars of s 490(2) (180 days), s 490(3) (one year) and s 490(12) (thirty days) while the period is still running, under a `NOTHING`-kind comment and no fork row, and `JUST FALSE` for the like period at s 490.7. The group-3 reader found this; the reader reads ruling (a) of the periods ruling as `JUST FALSE`.
- A "prepositional gate" ("on application by", "with the consent of", "with leave of", "on proof of service", "after three days notice") is answered both ways by the encoders of groups `ccc19` to `ccc23`: `JUST FALSE` at s 511(2.1) and s 672.58; `NOTHING` at s 508(1)(b)(iii), s 519.1, s 644(3), s 667(3), s 605(1) and s 622. The group-4 reader found this.

### Other calls

- `ccc3`, s 83.08(2) ("shall not be liable ... if all reasonable steps"): the part answers `NOTHING` for a failed "if"; the group-1 reader reads the 2026-11-05 delegated ruling (b) on defences as `JUST FALSE`, "this section gives no defence on these facts".
- `ccc4` and the keel disagree on `s 2 weapon` and `s 3.01(1)`; six first seat expectations are kept in their own file (`ccc4-cases-seat-expected-red.l4`, listed in `check.sh` and `encoding.json` as expected to fail) and recorded as findings 12 and 13 of its notes. `s 110.2(1)` and `s 110.3(1)` are also open there.
- `ccc13`, its F13: the seat passes `JUST FALSE` where the keel would answer `NOTHING`, because the Code says "includes"; its `NEEDS-CORE.md` item 2 asks the keel to change.
- `ccc1`: a few seat questions are asked as the person who acts under a power or a duty (a peace officer charged for the force used, and similar), although the brief says there is never a seat for an official; the part says its audit rate is not independent, because the same agent wrote the functions, the names and the audit.
- Day counting: `ccc30` reads "N days after the day" as the days D+1 to D+N, while `ccc31`'s period helper "N years after this order is made" starts the count on the day of the order. Found by the group-6 reader.
- `ccc32`: the questions on s 490.04(2) and (4) are titled as permissions over functions that answer a bar, and the layer-1 names are misleading.
- `ccc8`'s s 207(1)(e) and (f) were retitled to the scoped form as well, although they are inside the name-test sweep and already answer `NOTHING`.
- Whether the readings flagged in each part's fork register and marginal readings are right is for a lawyer; the French version of the Code was not read (`ccc21` notes it), and nothing here has been read by a lawyer.

### Findings of the independent readers that no function answers (GAP)

| group | GAPs | sites |
| --- | --- | --- |
| g1 | 1 | the repealed s 38 and its neighbours (the encoding keeps only the text `[Repealed ...]` as a string, by design) |
| g2 | 7 as returned, 6 left | s 273.2, s 273.3(1)(a), s 320.12, s 320.38(b), s 355.3, s 320.24(2)(a); the seventh, s 278.2(3), was repaired by `ccc9`, which added a function for the bar (two assertions for it were written by the lead and are marked as such) |
| g3 | 2 | s 487.021, s 490(2)(a) |
| g4 | 10 | s 492.26(2) and s 492.31(2) (no function for a count of listed factors); s 506 (asked only as "may be in Form 2"); s 515(2.3) (asked only whether consent is required); s 533, s 533.1(2) and s 672.95 (regulation or committee provisions: inert or machinery); s 536.1(2) (the Nunavut election speech's options); s 545(2) (no function takes the adjournment length); s 672.35 (whether a body other than a court or parole board may take the verdict into account) |
| g5 | 4 | s 696.71(2) (composition of the Miscarriage of Justice Review Commission), s 696.75(2) (qualifications of commissioners), s 696.76(2) (acting Chief Commissioner), s 696.79(2) (quorum): `ccc24` leaves the Commission machinery inert on purpose |
| g6 | 115 | review, report and committee provisions of amending Acts, which are not encoded (2018 c. 21 s. 51, 2018 c. 29 ss. 79 to 80), and the recitals of Forms 5.01 to 5.05 |

None of these was repaired unless the row says so. The readers' own triage files, under `notes/independent/`, list them with the scenario each asked.

### Mechanical checks of the merge

- The mechanical consistency check between each part's coverage table and its fork register (coarse: an `F` identifier in a coverage row that is absent from the fork register) found: `ccc11` (F25b). The one hit is not a missing fork: the row for s 320.28(8) cites `F25b`, and `ccc11`'s fork F25 has limbs (a) and (b), so `F25b` is limb (b) of F25 (`notes/ccc11-NOTES.md`; read by the lead, 2026-11-17).
- The functions the sweep flipped are read by seat questions in the same part, whose `@export` text says what `NOTHING` now means; a reader of a seat answer should read that text.
- `ccc-cases-seat.l4` and `tests-independent-g1.l4` to `g6` import the merged seat module, not the parts' own seat modules.
- `check.sh` carries one expected failure, `ccc4-cases-seat-expected-red.l4` (6 assertions that are meant to fail: its notes, findings 12 and 13), and `encoding.json` lists it under `expected_red`.

## What each part's notes hold

**keel**
- `notes/keel-NOTES.md:6` What is encoded and what is not
- `notes/keel-NOTES.md:13` Seat
- `notes/keel-NOTES.md:18` How to read the answers
- `notes/keel-NOTES.md:30` Coverage table
- `notes/keel-NOTES.md:142` Fork register
- `notes/keel-NOTES.md:165` Marginal readings for a lawyer
- `notes/keel-NOTES.md:195` Rulings carried, word for word
- `notes/keel-NOTES.md:207` Jural relations
- `notes/keel-NOTES.md:227` Findings
- `notes/keel-NOTES.md:259` What `check.sh` printed
- `notes/keel-NOTES.md:279` Open questions for a domain expert
- `notes/keel-NOTES.md:288` Copied modules
- `notes/keel-NOTES.md:292` Files

**ccc1**
- `notes/ccc1-NOTES.md:7` What is encoded and what is not
- `notes/ccc1-NOTES.md:14` Seat
- `notes/ccc1-NOTES.md:29` Coverage (ccc1)
- `notes/ccc1-NOTES.md:456` Fork register (ccc1)
- `notes/ccc1-NOTES.md:510` Jural relations (ccc1)
- `notes/ccc1-NOTES.md:609` Marginal readings for a lawyer (ccc1)
- `notes/ccc1-NOTES.md:896` Seams (ccc1)
- `notes/ccc1-NOTES.md:918` Findings
- `notes/ccc1-NOTES.md:952` Seat questions (ccc1)
- `notes/ccc1-NOTES.md:1110` Name-test sweep of 2026-11-12
- `notes/ccc1-NOTES.md:1155` What check.sh printed, and the checks that go with it
- `notes/ccc1-NOTES.md:1208` Open questions for a domain expert
- `notes/ccc1-NOTES.md:1217` Limits of this work
- `notes/ccc1-NOTES.md:1225` Copied modules
- `notes/ccc1-NOTES.md:1229` Files

**ccc2**
- `notes/ccc2-NOTES.md:6` What is encoded and what is not
- `notes/ccc2-NOTES.md:13` Departures from the brief and from PLAN.md (stated, not hidden)
- `notes/ccc2-NOTES.md:19` Seat
- `notes/ccc2-NOTES.md:35` Coverage (ccc2)
- `notes/ccc2-NOTES.md:329` Fork register (ccc2)
- `notes/ccc2-NOTES.md:384` Jural relations (ccc2)
- `notes/ccc2-NOTES.md:494` Marginal readings for a lawyer (ccc2)
- `notes/ccc2-NOTES.md:646` Seams (ccc2)
- `notes/ccc2-NOTES.md:657` What the text turns out to say (findings)
- `notes/ccc2-NOTES.md:674` Seat questions
- `notes/ccc2-NOTES.md:815` What the stable binary does not accept, and what it does
- `notes/ccc2-NOTES.md:830` What check.sh prints
- `notes/ccc2-NOTES.md:867` Open questions for a lawyer
- `notes/ccc2-NOTES.md:873` Files

**ccc3**
- `notes/ccc3-NOTES.md:9` What is in this folder
- `notes/ccc3-NOTES.md:17` Where this brief and PLAN.md differ (the brief governs; said here as the brief asks)
- `notes/ccc3-NOTES.md:28` Coverage (ccc3)
- `notes/ccc3-NOTES.md:511` Fork register (ccc3)
- `notes/ccc3-NOTES.md:602` Jural relations (ccc3)
- `notes/ccc3-NOTES.md:689` Marginal readings for a lawyer (ccc3)
- `notes/ccc3-NOTES.md:1041` Seams (ccc3)
- `notes/ccc3-NOTES.md:1087` Findings: what the text turns out to say
- `notes/ccc3-NOTES.md:1110` What the stable binary does not accept
- `notes/ccc3-NOTES.md:1138` The seat layer (ccc3-seat.l4, ccc3-cases-seat.l4)
- `notes/ccc3-NOTES.md:1444` Rulings carried verbatim
- `notes/ccc3-NOTES.md:1458` What check.sh prints

**ccc4**
- `notes/ccc4-NOTES.md:24` Coverage (ccc4)
- `notes/ccc4-NOTES.md:370` Fork register (ccc4)
- `notes/ccc4-NOTES.md:518` Jural relations (ccc4)
- `notes/ccc4-NOTES.md:623` Marginal readings for a lawyer (ccc4)
- `notes/ccc4-NOTES.md:745` Seams (ccc4)
- `notes/ccc4-NOTES.md:764` Findings: what the text turns out to say (ccc4)
- `notes/ccc4-NOTES.md:793` What the stable binary does not accept (ccc4)
- `notes/ccc4-NOTES.md:804` Seat questions (ccc4)
- `notes/ccc4-NOTES.md:1019` What check.sh prints (ccc4)

**ccc5**
- `notes/ccc5-NOTES.md:6` What is encoded, and what is not
- `notes/ccc5-NOTES.md:13` Seat
- `notes/ccc5-NOTES.md:23` How the encoding was built, and where this brief departs from `inputs/PLAN.md`
- `notes/ccc5-NOTES.md:32` Answer table: the classes and the stated maxima in the range
- `notes/ccc5-NOTES.md:111` Coverage (ccc5)
- `notes/ccc5-NOTES.md:529` Fork register (ccc5)
- `notes/ccc5-NOTES.md:728` Jural relations (ccc5)
- `notes/ccc5-NOTES.md:799` Marginal readings for a lawyer (ccc5)
- `notes/ccc5-NOTES.md:925` Seams (ccc5)
- `notes/ccc5-NOTES.md:984` What the text turns out to say
- `notes/ccc5-NOTES.md:1000` What the stable binary does not accept, and what it does that surprises
- `notes/ccc5-NOTES.md:1008` Tests, and what check.sh prints
- `notes/ccc5-NOTES.md:1044` Seat questions (ccc5)
- `notes/ccc5-NOTES.md:1344` Peeked

**ccc6**
- `notes/ccc6-NOTES.md:9` Coverage (ccc6)
- `notes/ccc6-NOTES.md:375` Fork register (ccc6)
- `notes/ccc6-NOTES.md:561` Jural relations (ccc6)
- `notes/ccc6-NOTES.md:738` Marginal readings for a lawyer (ccc6)
- `notes/ccc6-NOTES.md:960` Seams (ccc6)
- `notes/ccc6-NOTES.md:970` Seat (ccc6)
- `notes/ccc6-NOTES.md:1269` Findings: what the text turns out to say
- `notes/ccc6-NOTES.md:1279` What the stable binary does not accept
- `notes/ccc6-NOTES.md:1290` Rulings (copied word for word from the brief)
- `notes/ccc6-NOTES.md:1308` What check.sh prints

**ccc7**
- `notes/ccc7-NOTES.md:6` What this is, and what it is not
- `notes/ccc7-NOTES.md:25` Coverage (ccc7)
- `notes/ccc7-NOTES.md:562` Fork register (ccc7)
- `notes/ccc7-NOTES.md:669` Jural relations (ccc7)
- `notes/ccc7-NOTES.md:710` Marginal readings for a lawyer (ccc7)
- `notes/ccc7-NOTES.md:760` Seams (ccc7)
- `notes/ccc7-NOTES.md:781` Seat layer (ccc7)
- `notes/ccc7-NOTES.md:898` Tests (ccc7)
- `notes/ccc7-NOTES.md:943` What the text turns out to say (numbered findings)
- `notes/ccc7-NOTES.md:969` What the stable binary does not accept (found while writing this part)
- `notes/ccc7-NOTES.md:986` What `check.sh` printed

**ccc8**
- `notes/ccc8-NOTES.md:10` What is encoded and what is not
- `notes/ccc8-NOTES.md:34` Seat
- `notes/ccc8-NOTES.md:138` Coverage (ccc8)
- `notes/ccc8-NOTES.md:1138` Fork register (ccc8)
- `notes/ccc8-NOTES.md:1170` Jural relations (ccc8)
- `notes/ccc8-NOTES.md:1235` Marginal readings for a lawyer (ccc8)
- `notes/ccc8-NOTES.md:1263` Seams (ccc8)
- `notes/ccc8-NOTES.md:1388` Findings: what the text turns out to say (ccc8)
- `notes/ccc8-NOTES.md:1403` What the stable binary does not accept
- `notes/ccc8-NOTES.md:1420` What the text does not answer
- `notes/ccc8-NOTES.md:1432` What check.sh prints

**ccc9**
- `notes/ccc9-NOTES.md:9` What is encoded and what is not
- `notes/ccc9-NOTES.md:31` Seat
- `notes/ccc9-NOTES.md:175` Coverage (ccc9)
- `notes/ccc9-NOTES.md:559` Fork register (ccc9)
- `notes/ccc9-NOTES.md:645` Jural relations (ccc9)
- `notes/ccc9-NOTES.md:731` Marginal readings for a lawyer (ccc9)
- `notes/ccc9-NOTES.md:933` Seams (ccc9)
- `notes/ccc9-NOTES.md:953` Rulings carried, word for word
- `notes/ccc9-NOTES.md:964` Findings
- `notes/ccc9-NOTES.md:1000` What `check.sh` printed
- `notes/ccc9-NOTES.md:1049` Files

**ccc10**
- `notes/ccc10-NOTES.md:50` Coverage (ccc10)
- `notes/ccc10-NOTES.md:493` Fork register (ccc10)
- `notes/ccc10-NOTES.md:594` Jural relations (ccc10)
- `notes/ccc10-NOTES.md:695` Marginal readings for a lawyer (ccc10)
- `notes/ccc10-NOTES.md:751` Seams (ccc10)
- `notes/ccc10-NOTES.md:779` Findings
- `notes/ccc10-NOTES.md:808` Rulings carried, word for word
- `notes/ccc10-NOTES.md:816` What the text does not answer
- `notes/ccc10-NOTES.md:827` Files
- `notes/ccc10-NOTES.md:834` What `check.sh` printed

**ccc11**
- `notes/ccc11-NOTES.md:7` What is encoded and what is not
- `notes/ccc11-NOTES.md:13` Seat (ccc11)
- `notes/ccc11-NOTES.md:24` Brief against PLAN.md
- `notes/ccc11-NOTES.md:28` How to read the answers
- `notes/ccc11-NOTES.md:72` Coverage (ccc11)
- `notes/ccc11-NOTES.md:311` Fork register (ccc11)
- `notes/ccc11-NOTES.md:422` Jural relations (ccc11)
- `notes/ccc11-NOTES.md:463` Marginal readings for a lawyer (ccc11)
- `notes/ccc11-NOTES.md:487` Rulings carried, word for word
- `notes/ccc11-NOTES.md:500` Seams (ccc11)
- `notes/ccc11-NOTES.md:515` Findings
- `notes/ccc11-NOTES.md:557` The seat questions
- `notes/ccc11-NOTES.md:670` What `check.sh` printed
- `notes/ccc11-NOTES.md:703` Open questions for a domain expert
- `notes/ccc11-NOTES.md:714` Limits of this work
- `notes/ccc11-NOTES.md:721` Copied modules
- `notes/ccc11-NOTES.md:725` Files

**ccc12**
- `notes/ccc12-NOTES.md:9` Where this part departs from the brief or the plan (stated, not hidden)
- `notes/ccc12-NOTES.md:18` The five rulings, copied word for word from the brief
- `notes/ccc12-NOTES.md:32` Coverage (ccc12)
- `notes/ccc12-NOTES.md:271` Fork register (ccc12)
- `notes/ccc12-NOTES.md:313` Jural relations (ccc12)
- `notes/ccc12-NOTES.md:543` Marginal readings for a lawyer (ccc12)
- `notes/ccc12-NOTES.md:630` Seams (ccc12)
- `notes/ccc12-NOTES.md:665` What the text turns out to say (numbered findings)
- `notes/ccc12-NOTES.md:680` What the stable binary does not accept (or reads in a way that surprises)
- `notes/ccc12-NOTES.md:689` Tests and the seat layer
- `notes/ccc12-NOTES.md:723` What `check.sh` prints
- `notes/ccc12-NOTES.md:764` Files

**ccc13**
- `notes/ccc13-NOTES.md:5` About this text and this note
- `notes/ccc13-NOTES.md:20` Rulings carried by the brief (word for word)
- `notes/ccc13-NOTES.md:42` Coverage (ccc13)
- `notes/ccc13-NOTES.md:547` Fork register (ccc13)
- `notes/ccc13-NOTES.md:756` Jural relations (ccc13)
- `notes/ccc13-NOTES.md:958` Marginal readings for a lawyer (ccc13)
- `notes/ccc13-NOTES.md:1260` Seams (ccc13)
- `notes/ccc13-NOTES.md:1275` Findings: what the text turns out to say (ccc13)
- `notes/ccc13-NOTES.md:1291` What the stable binary does not accept (ccc13)
- `notes/ccc13-NOTES.md:1302` Seat layer (ccc13)
- `notes/ccc13-NOTES.md:1544` What check.sh prints (ccc13)

**ccc14**
- `notes/ccc14-NOTES.md:9` What is encoded and what is not
- `notes/ccc14-NOTES.md:17` Seat
- `notes/ccc14-NOTES.md:24` How the answers are read
- `notes/ccc14-NOTES.md:35` Coverage (ccc14)
- `notes/ccc14-NOTES.md:511` Fork register (ccc14)
- `notes/ccc14-NOTES.md:616` Jural relations (ccc14)
- `notes/ccc14-NOTES.md:688` Marginal readings for a lawyer (ccc14)
- `notes/ccc14-NOTES.md:831` Seams (ccc14)
- `notes/ccc14-NOTES.md:852` What the text turns out to say (numbered findings)
- `notes/ccc14-NOTES.md:869` What the stable binary does not accept (found in this run)
- `notes/ccc14-NOTES.md:880` Seat questions: direction check, and the second audit pass (ccc14)
- `notes/ccc14-NOTES.md:940` Deviations from PLAN.md (the brief governs)
- `notes/ccc14-NOTES.md:946` Source and method
- `notes/ccc14-NOTES.md:955` Checks
- `notes/ccc14-NOTES.md:1003` Peeked

**ccc15**
- `notes/ccc15-NOTES.md:15` What is encoded and what is not
- `notes/ccc15-NOTES.md:39` Where this brief governs over PLAN.md, and where PLAN.md governs
- `notes/ccc15-NOTES.md:52` Seat
- `notes/ccc15-NOTES.md:259` Rulings applied (copied from the brief)
- `notes/ccc15-NOTES.md:276` Coverage (ccc15)
- `notes/ccc15-NOTES.md:427` Fork register (ccc15)
- `notes/ccc15-NOTES.md:630` Jural relations (ccc15)
- `notes/ccc15-NOTES.md:680` Marginal readings for a lawyer (ccc15)
- `notes/ccc15-NOTES.md:836` Seams (ccc15)
- `notes/ccc15-NOTES.md:877` Findings

**ccc16**
- `notes/ccc16-NOTES.md:6` About the text, the seat and the brief
- `notes/ccc16-NOTES.md:21` Rulings applied (copied word for word from the brief)
- `notes/ccc16-NOTES.md:33` Coverage (ccc16)
- `notes/ccc16-NOTES.md:664` Fork register (ccc16)
- `notes/ccc16-NOTES.md:968` Jural relations (ccc16)
- `notes/ccc16-NOTES.md:1074` Marginal readings for a lawyer (ccc16)
- `notes/ccc16-NOTES.md:1326` Seams (ccc16)
- `notes/ccc16-NOTES.md:1338` Findings: what the text turns out to say (ccc16)
- `notes/ccc16-NOTES.md:1347` What the stable binary does not accept (ccc16)
- `notes/ccc16-NOTES.md:1359` Seat layer (ccc16)
- `notes/ccc16-NOTES.md:1544` What check.sh prints (ccc16)

**ccc17**
- `notes/ccc17-NOTES.md:7` Status, and how each claim below was checked
- `notes/ccc17-NOTES.md:16` About this text, and what is not claimed
- `notes/ccc17-NOTES.md:23` Where this file departs from PLAN.md
- `notes/ccc17-NOTES.md:32` The seat
- `notes/ccc17-NOTES.md:38` Files
- `notes/ccc17-NOTES.md:46` Coverage (ccc17)
- `notes/ccc17-NOTES.md:902` Fork register (ccc17)
- `notes/ccc17-NOTES.md:1145` Jural relations (ccc17)
- `notes/ccc17-NOTES.md:1329` Marginal readings for a lawyer (ccc17)
- `notes/ccc17-NOTES.md:1583` Seams (ccc17)
- `notes/ccc17-NOTES.md:1613` What the text turns out to say (ccc17)
- `notes/ccc17-NOTES.md:1629` What the stable binary does not accept, and what it does differently (ccc17)
- `notes/ccc17-NOTES.md:1651` Seat questions (ccc17)
- `notes/ccc17-NOTES.md:1868` What `check.sh` prints

**ccc18**
- `notes/ccc18-NOTES.md:10` What is encoded and what is not
- `notes/ccc18-NOTES.md:18` Seat (ccc18)
- `notes/ccc18-NOTES.md:215` Coverage (ccc18)
- `notes/ccc18-NOTES.md:730` Fork register (ccc18)
- `notes/ccc18-NOTES.md:979` Jural relations (ccc18)
- `notes/ccc18-NOTES.md:1209` Marginal readings for a lawyer (ccc18)
- `notes/ccc18-NOTES.md:1431` Seams (ccc18)
- `notes/ccc18-NOTES.md:1496` Findings: what the text turns out to say (ccc18)
- `notes/ccc18-NOTES.md:1528` What the stable binary does not accept, and traps met (ccc18)
- `notes/ccc18-NOTES.md:1539` What check.sh prints (ccc18)

**ccc19**
- `notes/ccc19-NOTES.md:11` What is encoded and what is not
- `notes/ccc19-NOTES.md:32` Seat
- `notes/ccc19-NOTES.md:41` Coverage (ccc19)
- `notes/ccc19-NOTES.md:116` Fork register (ccc19)
- `notes/ccc19-NOTES.md:172` Jural relations (ccc19)
- `notes/ccc19-NOTES.md:197` Marginal readings for a lawyer (ccc19)
- `notes/ccc19-NOTES.md:320` Seams (ccc19)
- `notes/ccc19-NOTES.md:335` Seat questions: audit passes (first pass under the brief; second pass of 2026-11-12)
- `notes/ccc19-NOTES.md:412` Findings
- `notes/ccc19-NOTES.md:456` Open questions for a domain expert
- `notes/ccc19-NOTES.md:463` What `check.sh` prints
- `notes/ccc19-NOTES.md:503` Files

**ccc20**
- `notes/ccc20-NOTES.md:6` What this is
- `notes/ccc20-NOTES.md:30` Coverage (ccc20)
- `notes/ccc20-NOTES.md:583` Fork register (ccc20)
- `notes/ccc20-NOTES.md:872` Jural relations (ccc20)
- `notes/ccc20-NOTES.md:910` Marginal readings for a lawyer (ccc20)
- `notes/ccc20-NOTES.md:986` Seams (ccc20)
- `notes/ccc20-NOTES.md:1003` What the text turns out to say (numbered findings)
- `notes/ccc20-NOTES.md:1016` What the stable binary does not accept
- `notes/ccc20-NOTES.md:1032` Seat question audit of 2026-11-12 (second pass, written 2026-11-16)
- `notes/ccc20-NOTES.md:1136` What check.sh prints

**ccc21**
- `notes/ccc21-NOTES.md:11` Coverage (ccc21)
- `notes/ccc21-NOTES.md:613` Fork register (ccc21)
- `notes/ccc21-NOTES.md:831` Jural relations (ccc21)
- `notes/ccc21-NOTES.md:1191` Marginal readings for a lawyer (ccc21)
- `notes/ccc21-NOTES.md:1769` Seams (ccc21)
- `notes/ccc21-NOTES.md:1790` Seat questions (ccc21)
- `notes/ccc21-NOTES.md:1987` What the text turns out to say (numbered findings)
- `notes/ccc21-NOTES.md:1997` What the stable binary does not accept
- `notes/ccc21-NOTES.md:2013` Rulings applied, word for word (copied by script from the brief)
- `notes/ccc21-NOTES.md:2037` What check.sh prints

**ccc22**
- `notes/ccc22-NOTES.md:22` Coverage (ccc22)
- `notes/ccc22-NOTES.md:599` Fork register (ccc22)
- `notes/ccc22-NOTES.md:997` Jural relations (ccc22)
- `notes/ccc22-NOTES.md:1376` Marginal readings for a lawyer (ccc22)
- `notes/ccc22-NOTES.md:1641` Seams (ccc22)
- `notes/ccc22-NOTES.md:1660` Seat layer (ccc22)
- `notes/ccc22-NOTES.md:1806` Findings: what the text turns out to say (ccc22)
- `notes/ccc22-NOTES.md:1821` What the stable binary does not accept (ccc22)
- `notes/ccc22-NOTES.md:1834` check.sh (ccc22)

**ccc23**
- `notes/ccc23-NOTES.md:9` Coverage (ccc23)
- `notes/ccc23-NOTES.md:573` Fork register (ccc23)
- `notes/ccc23-NOTES.md:875` Jural relations (ccc23)
- `notes/ccc23-NOTES.md:1144` Marginal readings for a lawyer (ccc23)
- `notes/ccc23-NOTES.md:1385` Seams (ccc23)
- `notes/ccc23-NOTES.md:1432` Findings: what the text turns out to say (ccc23)
- `notes/ccc23-NOTES.md:1445` What the stable binary does not accept (ccc23)
- `notes/ccc23-NOTES.md:1456` Seat layer (ccc23)
- `notes/ccc23-NOTES.md:1766` What check.sh prints (ccc23)

**ccc24**
- `notes/ccc24-NOTES.md:8` Files
- `notes/ccc24-NOTES.md:25` Coverage (ccc24)
- `notes/ccc24-NOTES.md:587` Fork register (ccc24)
- `notes/ccc24-NOTES.md:756` Jural relations (ccc24)
- `notes/ccc24-NOTES.md:871` Marginal readings for a lawyer (ccc24)
- `notes/ccc24-NOTES.md:1004` Seams (ccc24)
- `notes/ccc24-NOTES.md:1018` Numbered findings: what the text turns out to say
- `notes/ccc24-NOTES.md:1032` What the stable binary does not accept
- `notes/ccc24-NOTES.md:1047` The seat layer
- `notes/ccc24-NOTES.md:1401` The check.sh output

**ccc25**
- `notes/ccc25-NOTES.md:22` Coverage (ccc25)
- `notes/ccc25-NOTES.md:323` Fork register (ccc25)
- `notes/ccc25-NOTES.md:605` Jural relations (ccc25)
- `notes/ccc25-NOTES.md:646` Marginal readings for a lawyer (ccc25)
- `notes/ccc25-NOTES.md:679` Seams (ccc25)
- `notes/ccc25-NOTES.md:696` What the text turns out to say (ccc25)
- `notes/ccc25-NOTES.md:715` What the stable binary does not accept (ccc25)
- `notes/ccc25-NOTES.md:723` The seat (ccc25)
- `notes/ccc25-NOTES.md:808` What check.sh prints (ccc25)
- `notes/ccc25-NOTES.md:839` PLAN against the brief; about the text (ccc25)

**ccc26**
- `notes/ccc26-NOTES.md:9` Status and scope (ccc26)
- `notes/ccc26-NOTES.md:17` Coverage (ccc26)
- `notes/ccc26-NOTES.md:422` Fork register (ccc26)
- `notes/ccc26-NOTES.md:681` Jural relations (ccc26)
- `notes/ccc26-NOTES.md:774` Marginal readings for a lawyer (ccc26)
- `notes/ccc26-NOTES.md:818` Seams (ccc26)
- `notes/ccc26-NOTES.md:839` Seat layer (ccc26)
- `notes/ccc26-NOTES.md:1075` What the text turns out to say (ccc26)
- `notes/ccc26-NOTES.md:1093` What the stable binary does not accept (ccc26)
- `notes/ccc26-NOTES.md:1105` What check.sh prints (ccc26)

**ccc27**
- `notes/ccc27-NOTES.md:15` Files
- `notes/ccc27-NOTES.md:45` Coverage (ccc27)
- `notes/ccc27-NOTES.md:413` Fork register (ccc27)
- `notes/ccc27-NOTES.md:707` Jural relations (ccc27)
- `notes/ccc27-NOTES.md:752` Marginal readings for a lawyer (ccc27)
- `notes/ccc27-NOTES.md:850` Seams (ccc27)
- `notes/ccc27-NOTES.md:873` Second seat-question audit (2026-11-12 instruction)
- `notes/ccc27-NOTES.md:907` What the text turns out to say (numbered findings)
- `notes/ccc27-NOTES.md:930` What the text does not answer
- `notes/ccc27-NOTES.md:941` What the stable binary does not accept
- `notes/ccc27-NOTES.md:963` check.sh

**ccc28**
- `notes/ccc28-NOTES.md:17` Coverage (ccc28)
- `notes/ccc28-NOTES.md:422` Fork register (ccc28)
- `notes/ccc28-NOTES.md:564` Jural relations (ccc28)
- `notes/ccc28-NOTES.md:689` Marginal readings for a lawyer (ccc28)
- `notes/ccc28-NOTES.md:860` Seams (ccc28)
- `notes/ccc28-NOTES.md:885` Seat layer (ccc28)
- `notes/ccc28-NOTES.md:1086` What the text turns out to say (ccc28)
- `notes/ccc28-NOTES.md:1097` What the stable binary does not accept (ccc28)
- `notes/ccc28-NOTES.md:1112` What check.sh prints (ccc28)

**ccc29**
- `notes/ccc29-NOTES.md:7` What this part is
- `notes/ccc29-NOTES.md:17` Seat
- `notes/ccc29-NOTES.md:25` Coverage (ccc29)
- `notes/ccc29-NOTES.md:577` Fork register (ccc29)
- `notes/ccc29-NOTES.md:796` Jural relations (ccc29)
- `notes/ccc29-NOTES.md:1025` Marginal readings for a lawyer (ccc29)
- `notes/ccc29-NOTES.md:1303` Seams (ccc29)
- `notes/ccc29-NOTES.md:1330` Findings (ccc29): what the text turns out to say
- `notes/ccc29-NOTES.md:1354` What the stable binary does not accept (ccc29)
- `notes/ccc29-NOTES.md:1371` Seat-question audit (ccc29)
- `notes/ccc29-NOTES.md:1499` What check.sh prints (ccc29)
- `notes/ccc29-NOTES.md:1550` Files (ccc29)

**ccc30**
- `notes/ccc30-NOTES.md:8` What is encoded and what is not
- `notes/ccc30-NOTES.md:29` Differences between PLAN.md and the brief (the brief governs)
- `notes/ccc30-NOTES.md:35` Seat
- `notes/ccc30-NOTES.md:177` Coverage (ccc30)
- `notes/ccc30-NOTES.md:500` Fork register (ccc30)
- `notes/ccc30-NOTES.md:548` Jural relations (ccc30)
- `notes/ccc30-NOTES.md:631` Marginal readings for a lawyer (ccc30)
- `notes/ccc30-NOTES.md:663` Seams (ccc30)
- `notes/ccc30-NOTES.md:678` Findings: what the text turns out to say
- `notes/ccc30-NOTES.md:694` What the stable binary does not accept
- `notes/ccc30-NOTES.md:705` Tests, and what `check.sh` prints
- `notes/ccc30-NOTES.md:742` Open questions for a lawyer or a domain expert

**ccc31**
- `notes/ccc31-NOTES.md:14` What is encoded and what is not
- `notes/ccc31-NOTES.md:27` Seat
- `notes/ccc31-NOTES.md:53` Method: what is a rule in a Form (assumed, not ruled)
- `notes/ccc31-NOTES.md:146` Coverage (ccc31)
- `notes/ccc31-NOTES.md:482` Fork register (ccc31)
- `notes/ccc31-NOTES.md:521` Jural relations (ccc31)
- `notes/ccc31-NOTES.md:561` Marginal readings for a lawyer (ccc31)
- `notes/ccc31-NOTES.md:624` Rulings carried, word for word
- `notes/ccc31-NOTES.md:640` Seams (ccc31)
- `notes/ccc31-NOTES.md:667` Findings
- `notes/ccc31-NOTES.md:704` Open questions for a domain expert
- `notes/ccc31-NOTES.md:713` What `check.sh` printed
- `notes/ccc31-NOTES.md:790` Files

**ccc32**
- `notes/ccc32-NOTES.md:11` What this range is
- `notes/ccc32-NOTES.md:23` Departures from PLAN.md and from the brief (stated, as the brief asks)
- `notes/ccc32-NOTES.md:32` Coverage (ccc32)
- `notes/ccc32-NOTES.md:386` Fork register (ccc32)
- `notes/ccc32-NOTES.md:637` Rulings carried word for word (ccc32)
- `notes/ccc32-NOTES.md:653` Jural relations (ccc32)
- `notes/ccc32-NOTES.md:782` Marginal readings for a lawyer (ccc32)
- `notes/ccc32-NOTES.md:1092` Seams (ccc32)
- `notes/ccc32-NOTES.md:1112` The seat layer (ccc32)
- `notes/ccc32-NOTES.md:1350` What the text turns out to say (ccc32)
- `notes/ccc32-NOTES.md:1363` What the stable binary does not accept (ccc32)
- `notes/ccc32-NOTES.md:1374` Limits, and what I peeked at (ccc32)
- `notes/ccc32-NOTES.md:1382` What check.sh printed (ccc32)

## What would need doing before the encoding is worth relying on

- A lawyer reads each part's coverage table, forks and marginal readings against the official text (this is a converter's rendering).
- The `FALSE` and `NOTHING` readings the parts flag for a lawyer, and the listed groups above, are decided.
- The seams are wired or kept as questions, and the requests in `NEEDS-CORE.md` are taken into the core or refused.
- The prescribed figures and rates that the text leaves to regulations or orders are supplied as inputs; this encoding does not hold them unless a part's notes say so.

## Source not official

The quoted text is a plain-text rendering of the Act as deposited in `../../registers/source-bundle/`; it is not the official text. See 'The source' above and `SOURCE-LICENSE.md`.
