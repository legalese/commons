# NOTES: Companies Act 2006 (United Kingdom), 2006 c. 46, whole Act with an individual seat

Status: draft. No lawyer or other domain expert has read this encoding against the text, and it has not been checked against the official text.
Written 2026-11-12 and 2026-11-13 by Sonnet 5.5 agents (`claude-sonnet-5-5`) working in parallel, and merged by the lead agent of the session that ran them.
Built with the `l4` 1.6.110 (main, e51181d, 2026-11-11) and compared with 1.6.109 (main, 4c887e0, 2026-11-04); every module has the same four counts on both builds.

## How this folder was made

One **keel** agent first wrote the shared vocabulary (`coa-core.l4`, `coa-definitions.l4` and the definitions' tests) and a plan (`notes/keel-PLAN.md`) that gives each part a range of the text and says what it must take from the others.
30 **part** agents then encoded their ranges in parallel, each against the same core, none reading another's work: `coa1` (lines 56 to 563), `coa2` (lines 564 to 1413), `coa3` (lines 1414 to 2021), `coa4` (lines 2022 to 2696), `coa5` (lines 2697 to 3566), `coa6` (lines 3567 to 3716), `coa7` (lines 3717 to 4655), `coa8` (lines 4656 to 5417), `coa9` (lines 5418 to 5894), `coa10` (lines 5895 to 6542), `coa11` (lines 6543 to 6969), `coa12` (lines 6970 to 7555), `coa13` (lines 7556 to 8205), `coa14` (lines 8206 to 8744), `coa15` (lines 8745 to 9668), `coa16` (lines 9669 to 9961), `coa17` (lines 9962 to 10756), `coa18` (lines 10757 to 11596), `coa19` (lines 11597 to 12202), `coa20` (lines 12203 to 13131), `coa21` (lines 13132 to 13933), `coa22` (lines 13934 to 14665), `coa23` (lines 14666 to 15484), `coa24` (lines 15485 to 16189), `coa25` (lines 16190 to 16445, 16625 to 16995), `coa26` (lines 16996 to 17517), `coa27` (lines 17518 to 18348), `coa28` (lines 18349 to 19081), `coa29` (lines 19082 to 20016), `coa30` (lines 20017 to 20928).
The lead verified each part by itself (`check.sh` on both builds, `srcrefs.py check --refs` and `--strict`, the core identical to the keel's) and then merged them with a script; the part modules are copied unchanged, and the merge edited no rule.
After the parts returned, five further things were done, each by the part's own agent resumed with a short task, or by a separate reader; they are described in their own sections below:
1. a **seat-question audit** (section 'The seat-question audits');
2. a **name test for functions named for a grant or a power** (section 'The grant and power name test');
3. an **independent test pass** by six readers who saw only the text and the modules (section 'The independent test pass');
4. the **repairs** those readers' findings called for, made by the part agents;
5. the **merged gate**, below.

Every note a part wrote is kept, with names and local paths replaced by placeholders, as `notes/<part>-NOTES.md`, with its `PROGRESS.md`, `SEAMS.md` and `NEEDS-CORE.md` where it wrote them; the keel's are `notes/keel-*.md`, and the brief each agent was given is `notes/<agent>-BRIEF.md`.
**A part's NOTES.md is where its coverage table, fork register, marginal readings, jural relations and findings are.** They are not repeated or summed here, except as the sections below say.

## Merge decisions (assumed, not ruled)

- **One seat module for the Act.** Each part wrote its own seat questions and cases. The lead concatenated them, in part order, into `coa-seat.l4` and `coa-cases-seat.l4`, with one banner comment per part; the text under each banner is the part's, unchanged. The merged seat module imports every part module and checks clean.
- **Seams stay inputs.** Where a part needs an answer that belongs to another part, it takes it as an input named for the answering section (`notes/<part>-SEAMS.md` lists what each part asks and answers). The merge does not wire one part's output into another's input, so the seat asks the person each such fact.
- **NEEDS-CORE requests are not hoisted.** They are gathered in `NEEDS-CORE.md` (proposed, not landed); the core is the keel's, unchanged.
- **Part-local types and helper names stay where they are.** Every top-level name carries the label of its section or its part prefix; the merged seat module imports all part modules at once and compiles, so no two modules define the same name.
- **The merge lost nothing:** the merged folder was gated as it stands: 453 modules, 40,076 assertions satisfied (below).

## Where things are

| agent | text (lines of `ukpga-2006-46.txt`) | modules | assertions in its test modules | seat questions |
| --- | --- | --- | --- | --- |
| keel | 1 to 55, 16446 to 16624 | 2 | 346 | 0 |
| coa1 | 56 to 563 | 3 | 787 | 103 |
| coa2 | 564 to 1413 | 8 | 1180 | 159 |
| coa3 | 1414 to 2021 | 5 | 961 | 106 |
| coa4 | 2022 to 2696 | 8 | 1051 | 79 |
| coa5 | 2697 to 3566 | 10 | 1266 | 239 |
| coa6 | 3567 to 3716 | 6 | 362 | 59 |
| coa7 | 3717 to 4655 | 11 | 1317 | 170 |
| coa8 | 4656 to 5417 | 13 | 1173 | 171 |
| coa9 | 5418 to 5894 | 8 | 703 | 128 |
| coa10 | 5895 to 6542 | 10 | 902 | 101 |
| coa11 | 6543 to 6969 | 4 | 657 | 67 |
| coa12 | 6970 to 7555 | 8 | 1016 | 73 |
| coa13 | 7556 to 8205 | 7 | 987 | 59 |
| coa14 | 8206 to 8744 | 6 | 1052 | 124 |
| coa15 | 8745 to 9668 | 8 | 1349 | 162 |
| coa16 | 9669 to 9961 | 5 | 549 | 57 |
| coa17 | 9962 to 10756 | 10 | 834 | 80 |
| coa18 | 10757 to 11596 | 7 | 1032 | 65 |
| coa19 | 11597 to 12202 | 9 | 926 | 45 |
| coa20 | 12203 to 13131 | 5 | 1294 | 66 |
| coa21 | 13132 to 13933 | 7 | 1026 | 52 |
| coa22 | 13934 to 14665 | 6 | 1079 | 88 |
| coa23 | 14666 to 15484 | 5 | 977 | 52 |
| coa24 | 15485 to 16189 | 11 | 815 | 70 |
| coa25 | 16190 to 16445, 16625 to 16995 | 9 | 847 | 87 |
| coa26 | 16996 to 17517 | 8 | 805 | 38 |
| coa27 | 17518 to 18348 | 7 | 868 | 58 |
| coa28 | 18349 to 19081 | 8 | 904 | 74 |
| coa29 | 19082 to 20016 | 8 | 1203 | 40 |
| coa30 | 20017 to 20928 | 8 | 877 | 43 |
| seat cases, all parts | | 1 (`coa-cases-seat.l4`) | 7100 | |
| independent tests, six readers | | 6 (`tests-independent-g1.l4` to `g6`) | 3813 | |

The seat layer is `coa-seat.l4` (2,715 `@export` questions in all) and `coa-cases-seat.l4`; every other module is layer 1, with a tests module beside it.

## The source

The only source is `ukpga-2006-46.txt`, a plain-text rendering of the Act and its Schedules from legislation.gov.uk (Open Government Licence v3.0) made by a converter script; it is not the official text, and nothing here is "verified against the official text". It is the revised text of the version stated as 2026-07-16 in `../../registers/source-bundle/ukpga-2006-46.meta.json`, which "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish". Every `-- src:` quote line in `coa-core.l4` and `coa-definitions.l4` was generated by `srcrefs.py quote` from that file, and `python3 -I srcrefs.py check --refs ukpga-2006-46.txt coa-core.l4 coa-definitions.l4` reports 0 problems (the figures are in "What check.sh printed" below). The text file must sit beside the modules, or be named on the command line, for that gate to run; line numbers are of the file as it is.

## The seat

From the keel's notes:

The individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.) Officials and courts appear only as parties the text names (`Party` in the core), never as a seat. This module set has no seat layer: the seat layers belong to the part agents' modules and to the lead's merge; the keel's definitions are ordinary functions over plain facts that a seat layer can call.

## What check.sh prints

Run as `L4=<stable 1.6.110> L4_MAIN=<main 1.6.109> ./check.sh` on the merged folder, exit 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-cases-seat.l4                              0      7100       0        0         0 |      0      7100       0        0  same
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions-tests.l4                       0       346       0        0         0 |      0       346       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa1-part2-formation.l4                        0         0       0        0         0 |      0         0       0        0  same
coa1-part3-constitution.l4                     0         0       0        0         0 |      0         0       0        0  same
coa1-part4-capacity.l4                         0         0       0        0         0 |      0         0       0        0  same
coa1-tests-part2.l4                            0       273       0        0         0 |      0       273       0        0  same
coa1-tests-part3.l4                            0       283       0        0         0 |      0       283       0        0  same
coa1-tests-part4.l4                            0       231       0        0         0 |      0       231       0        0  same
coa10-default.l4                               0         0       0        0         0 |      0         0       0        0  same
coa10-disclosure.l4                            0         0       0        0         0 |      0         0       0        0  same
coa10-exemptions.l4                            0         0       0        0         0 |      0         0       0        0  same
coa10-filing.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-meaning.l4                               0         0       0        0         0 |      0         0       0        0  same
coa10-medium.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-period.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-revision.l4                              0         0       0        0         0 |      0         0       0        0  same
coa10-supplementary.l4                         0         0       0        0         0 |      0         0       0        0  same
coa10-tests-default.l4                         0        60       0        0         0 |      0        60       0        0  same
coa10-tests-disclosure.l4                      0       108       0        0         0 |      0       108       0        0  same
coa10-tests-exemptions.l4                      0       112       0        0         0 |      0       112       0        0  same
coa10-tests-filing.l4                          0       217       0        0         0 |      0       217       0        0  same
coa10-tests-meaning.l4                         0        98       0        0         0 |      0        98       0        0  same
coa10-tests-medium.l4                          0       106       0        0         0 |      0       106       0        0  same
coa10-tests-period.l4                          0        79       0        0         0 |      0        79       0        0  same
coa10-tests-revision.l4                        0        81       0        0         0 |      0        81       0        0  same
coa10-tests-supplementary.l4                   0        41       0        0         0 |      0        41       0        0  same
coa10-types.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-general.l4                    0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-private.l4                    0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-public.l4                     0         0       0        0         0 |      0         0       0        0  same
coa11-tests-ch1.l4                             0       239       0        0         0 |      0       239       0        0  same
coa11-tests-ch2-general.l4                     0        99       0        0         0 |      0        99       0        0  same
coa11-tests-ch2-private.l4                     0       180       0        0         0 |      0       180       0        0  same
coa11-tests-ch2-public.l4                      0       139       0        0         0 |      0       139       0        0  same
coa12-ch3a-report.l4                           0         0       0        0         0 |      0         0       0        0  same
coa12-ch3b-rights.l4                           0         0       0        0         0 |      0         0       0        0  same
coa12-ch4a-removal.l4                          0         0       0        0         0 |      0         0       0        0  same
coa12-ch4b-resignation.l4                      0         0       0        0         0 |      0         0       0        0  same
coa12-ch5-concerns.l4                          0         0       0        0         0 |      0         0       0        0  same
coa12-ch6-liability.l4                         0         0       0        0         0 |      0         0       0        0  same
coa12-ch7-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
coa12-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa12-tests-ch3a.l4                            0       163       0        0         0 |      0       163       0        0  same
coa12-tests-ch3b.l4                            0       187       0        0         0 |      0       187       0        0  same
coa12-tests-ch4a.l4                            0       157       0        0         0 |      0       157       0        0  same
coa12-tests-ch4b.l4                            0       333       0        0         0 |      0       333       0        0  same
coa12-tests-ch5.l4                             0        77       0        0         0 |      0        77       0        0  same
coa12-tests-ch6.l4                             0        99       0        0         0 |      0        99       0        0  same
coa13-ch1-shares.l4                            0         0       0        0         0 |      0         0       0        0  same
coa13-ch2-allotment.l4                         0         0       0        0         0 |      0         0       0        0  same
coa13-ch3-preemption.l4                        0         0       0        0         0 |      0         0       0        0  same
coa13-ch4-undersubscribed.l4                   0         0       0        0         0 |      0         0       0        0  same
coa13-ch5-payment.l4                           0         0       0        0         0 |      0         0       0        0  same
coa13-ch6-valuation.l4                         0         0       0        0         0 |      0         0       0        0  same
coa13-regulative.l4                            0         0       0        0         0 |      0         0       0        0  same
coa13-tests-ch1.l4                             0        73       0        0         0 |      0        73       0        0  same
coa13-tests-ch2.l4                             0       183       0        0         0 |      0       183       0        0  same
coa13-tests-ch3.l4                             0       247       0        0         0 |      0       247       0        0  same
coa13-tests-ch4.l4                             0        49       0        0         0 |      0        49       0        0  same
coa13-tests-ch5.l4                             0       156       0        0         0 |      0       156       0        0  same
coa13-tests-ch6.l4                             0       276       0        0         0 |      0       276       0        0  same
coa13-tests-regulative.l4                      0         3       0        0         0 |      0         3       0        0  same
coa14-ch07-premiums.l4                         0         0       0        0         0 |      0         0       0        0  same
coa14-ch08-alteration.l4                       0         0       0        0         0 |      0         0       0        0  same
coa14-ch09-classes.l4                          0         0       0        0         0 |      0         0       0        0  same
coa14-ch10-reduction.l4                        0         0       0        0         0 |      0         0       0        0  same
coa14-ch11-misc.l4                             0         0       0        0         0 |      0         0       0        0  same
coa14-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa14-tests-ch07.l4                            0       134       0        0         0 |      0       134       0        0  same
coa14-tests-ch08.l4                            0       310       0        0         0 |      0       310       0        0  same
coa14-tests-ch09.l4                            0       258       0        0         0 |      0       258       0        0  same
coa14-tests-ch10.l4                            0       311       0        0         0 |      0       311       0        0  same
coa14-tests-ch11.l4                            0        39       0        0         0 |      0        39       0        0  same
coa15-ch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch3.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch5.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch6.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch7.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa15-tests-ch1.l4                             0       285       0        0         0 |      0       285       0        0  same
coa15-tests-ch2.l4                             0       141       0        0         0 |      0       141       0        0  same
coa15-tests-ch3.l4                             0        84       0        0         0 |      0        84       0        0  same
coa15-tests-ch4.l4                             0       345       0        0         0 |      0       345       0        0  same
coa15-tests-ch5.l4                             0       297       0        0         0 |      0       297       0        0  same
coa15-tests-ch6.l4                             0       129       0        0         0 |      0       129       0        0  same
coa15-tests-ch7.l4                             0        68       0        0         0 |      0        68       0        0  same
coa16-part19-general.l4                        0         0       0        0         0 |      0         0       0        0  same
coa16-part19-register.l4                       0         0       0        0         0 |      0         0       0        0  same
coa16-part19-supplementary.l4                  0         0       0        0         0 |      0         0       0        0  same
coa16-part20-minimum-capital.l4                0         0       0        0         0 |      0         0       0        0  same
coa16-part20-public-offers.l4                  0         0       0        0         0 |      0         0       0        0  same
coa16-tests-part19-general.l4                  0        54       0        0         0 |      0        54       0        0  same
coa16-tests-part19-register.l4                 0       135       0        0         0 |      0       135       0        0  same
coa16-tests-part19-supplementary.l4            0        95       0        0         0 |      0        95       0        0  same
coa16-tests-part20-minimum-capital.l4          0       103       0        0         0 |      0       103       0        0  same
coa16-tests-part20-public-offers.l4            0       162       0        0         0 |      0       162       0        0  same
coa17-helpers.l4                               0         8       0        0         0 |      0         8       0        0  same
coa17-part21-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa17-part21-ch2.l4                            0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch1.l4                           0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch2-company.l4                   0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch2-others.l4                    0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch2a-id.l4                       0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch2a-notices.l4                  0         0       0        0         0 |      0         0       0        0  same
coa17-part21a-ch5.l4                           0         0       0        0         0 |      0         0       0        0  same
coa17-regulative.l4                            0         0       0        0         0 |      0         0       0        0  same
coa17-tests-part21-ch1.l4                      0       190       0        0         0 |      0       190       0        0  same
coa17-tests-part21-ch2.l4                      0        18       0        0         0 |      0        18       0        0  same
coa17-tests-part21a-ch1.l4                     0        71       0        0         0 |      0        71       0        0  same
coa17-tests-part21a-ch2-company.l4             0       155       0        0         0 |      0       155       0        0  same
coa17-tests-part21a-ch2-others.l4              0        83       0        0         0 |      0        83       0        0  same
coa17-tests-part21a-ch2a-id.l4                 0       147       0        0         0 |      0       147       0        0  same
coa17-tests-part21a-ch2a-notices.l4            0       148       0        0         0 |      0       148       0        0  same
coa17-tests-part21a-ch5.l4                     0        22       0        0         0 |      0        22       0        0  same
coa17-tests-regulative.l4                      0         0       0        0         0 |      0         0       0        0  same
coa18-part22-interest.l4                       0         0       0        0         0 |      0         0       0        0  same
coa18-part22-notice.l4                         0         0       0        0         0 |      0         0       0        0  same
coa18-part22-register.l4                       0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch2.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch3.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part24.l4                                0         0       0        0         0 |      0         0       0        0  same
coa18-tests-part22-interest.l4                 0       111       0        0         0 |      0       111       0        0  same
coa18-tests-part22-notice.l4                   0       234       0        0         0 |      0       234       0        0  same
coa18-tests-part22-register.l4                 0       165       0        0         0 |      0       165       0        0  same
coa18-tests-part23-ch1.l4                      0       110       0        0         0 |      0       110       0        0  same
coa18-tests-part23-ch2.l4                      0       103       0        0         0 |      0       103       0        0  same
coa18-tests-part23-ch3.l4                      0       140       0        0         0 |      0       140       0        0  same
coa18-tests-part24.l4                          0       169       0        0         0 |      0       169       0        0  same
coa19-a1-after.l4                              0         0       0        0         0 |      0         0       0        0  same
coa19-a1-delivery.l4                           0         0       0        0         0 |      0         0       0        0  same
coa19-a1-records.l4                            0         0       0        0         0 |      0         0       0        0  same
coa19-ch1-registrar.l4                         0         0       0        0         0 |      0         0       0        0  same
coa19-ch1-requirements.l4                      0         0       0        0         0 |      0         0       0        0  same
coa19-ch2-scotland.l4                          0         0       0        0         0 |      0         0       0        0  same
coa19-ch3-powers.l4                            0         0       0        0         0 |      0         0       0        0  same
coa19-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa19-regulative.l4                            0         0       0        0         0 |      0         0       0        0  same
coa19-tests-a1-after.l4                        0       184       0        0         0 |      0       184       0        0  same
coa19-tests-a1-delivery.l4                     0       177       0        0         0 |      0       177       0        0  same
coa19-tests-a1-records.l4                      0        43       0        0         0 |      0        43       0        0  same
coa19-tests-ch1-registrar.l4                   0       128       0        0         0 |      0       128       0        0  same
coa19-tests-ch1-requirements.l4                0       143       0        0         0 |      0       143       0        0  same
coa19-tests-ch2-scotland.l4                    0       229       0        0         0 |      0       229       0        0  same
coa19-tests-ch3-powers.l4                      0        22       0        0         0 |      0        22       0        0  same
coa19-tests-regulative.l4                      0         0       0        0         0 |      0         0       0        0  same
coa2-ch1-prohibited-names.l4                   0         0       0        0         0 |      0         0       0        0  same
coa2-ch2-company-type.l4                       0         0       0        0         0 |      0         0       0        0  same
coa2-ch3-similarity.l4                         0         0       0        0         0 |      0         0       0        0  same
coa2-ch4-other-powers.l4                       0         0       0        0         0 |      0         0       0        0  same
coa2-ch5-ch6-name-change-disclosure.l4         0         0       0        0         0 |      0         0       0        0  same
coa2-part6-registered-office.l4                0         0       0        0         0 |      0         0       0        0  same
coa2-part7-other-routes.l4                     0         0       0        0         0 |      0         0       0        0  same
coa2-part7-private-to-public.l4                0         0       0        0         0 |      0         0       0        0  same
coa2-tests-ch1.l4                              0        80       0        0         0 |      0        80       0        0  same
coa2-tests-ch2.l4                              0       144       0        0         0 |      0       144       0        0  same
coa2-tests-ch3.l4                              0       114       0        0         0 |      0       114       0        0  same
coa2-tests-ch4.l4                              0       184       0        0         0 |      0       184       0        0  same
coa2-tests-ch5-ch6.l4                          0        78       0        0         0 |      0        78       0        0  same
coa2-tests-part6.l4                            0        87       0        0         0 |      0        87       0        0  same
coa2-tests-part7a.l4                           0       196       0        0         0 |      0       196       0        0  same
coa2-tests-part7b.l4                           0       297       0        0         0 |      0       297       0        0  same
coa20-part26.l4                                0         0       0        0         0 |      0         0       0        0  same
coa20-part26a.l4                               0         0       0        0         0 |      0         0       0        0  same
coa20-part27-division.l4                       0         0       0        0         0 |      0         0       0        0  same
coa20-part27-merger.l4                         0         0       0        0         0 |      0         0       0        0  same
coa20-part27-supp.l4                           0         0       0        0         0 |      0         0       0        0  same
coa20-tests-part26.l4                          0       196       0        0         0 |      0       196       0        0  same
coa20-tests-part26a.l4                         0       249       0        0         0 |      0       249       0        0  same
coa20-tests-part27-division.l4                 0       329       0        0         0 |      0       329       0        0  same
coa20-tests-part27-merger.l4                   0       408       0        0         0 |      0       408       0        0  same
coa20-tests-part27-supp.l4                     0       112       0        0         0 |      0       112       0        0  same
coa21-ch1-panel.l4                             0         0       0        0         0 |      0         0       0        0  same
coa21-ch2-opting-in.l4                         0         0       0        0         0 |      0         0       0        0  same
coa21-ch3-offers.l4                            0         0       0        0         0 |      0         0       0        0  same
coa21-ch3-sell-out.l4                          0         0       0        0         0 |      0         0       0        0  same
coa21-ch3-squeeze-out.l4                       0         0       0        0         0 |      0         0       0        0  same
coa21-ch4-directors-report.l4                  0         0       0        0         0 |      0         0       0        0  same
coa21-part29-fraudulent-trading.l4             0         0       0        0         0 |      0         0       0        0  same
coa21-tests-ch1.l4                             0       294       0        0         0 |      0       294       0        0  same
coa21-tests-ch2.l4                             0       193       0        0         0 |      0       193       0        0  same
coa21-tests-ch3-offers.l4                      0       191       0        0         0 |      0       191       0        0  same
coa21-tests-ch3-sell-out.l4                    0       126       0        0         0 |      0       126       0        0  same
coa21-tests-ch3-squeeze-out.l4                 0       158       0        0         0 |      0       158       0        0  same
coa21-tests-ch4-part29.l4                      0        64       0        0         0 |      0        64       0        0  same
coa22-part30.l4                                0         0       0        0         0 |      0         0       0        0  same
coa22-part31-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa22-part31-ch2.l4                            0         0       0        0         0 |      0         0       0        0  same
coa22-part31-ch3.l4                            0         0       0        0         0 |      0         0       0        0  same
coa22-part32.l4                                0         0       0        0         0 |      0         0       0        0  same
coa22-part33.l4                                0         0       0        0         0 |      0         0       0        0  same
coa22-tests-part30.l4                          0       128       0        0         0 |      0       128       0        0  same
coa22-tests-part31-ch1.l4                      0       308       0        0         0 |      0       308       0        0  same
coa22-tests-part31-ch2.l4                      0       142       0        0         0 |      0       142       0        0  same
coa22-tests-part31-ch3.l4                      0       368       0        0         0 |      0       368       0        0  same
coa22-tests-part32.l4                          0        81       0        0         0 |      0        81       0        0  same
coa22-tests-part33.l4                          0        52       0        0         0 |      0        52       0        0  same
coa23-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa23-part34.l4                                0         0       0        0         0 |      0         0       0        0  same
coa23-part35-delivery.l4                       0         0       0        0         0 |      0         0       0        0  same
coa23-part35-register.l4                       0         0       0        0         0 |      0         0       0        0  same
coa23-part35-registrar.l4                      0         0       0        0         0 |      0         0       0        0  same
coa23-tests-part34.l4                          0       133       0        0         0 |      0       133       0        0  same
coa23-tests-part35-delivery.l4                 0       240       0        0         0 |      0       240       0        0  same
coa23-tests-part35-register.l4                 0       288       0        0         0 |      0       288       0        0  same
coa23-tests-part35-registrar.l4                0       316       0        0         0 |      0       316       0        0  same
coa24-acsp.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa24-delivery.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-disclosure.l4                            0         0       0        0         0 |      0         0       0        0  same
coa24-false-statements.l4                      0         0       0        0         0 |      0         0       0        0  same
coa24-identity.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-index.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa24-language.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-officers.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-penalty.l4                               0         0       0        0         0 |      0         0       0        0  same
coa24-prosecution.l4                           0         0       0        0         0 |      0         0       0        0  same
coa24-register.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-tests-acsp.l4                            0       119       0        0         0 |      0       119       0        0  same
coa24-tests-delivery.l4                        0        76       0        0         0 |      0        76       0        0  same
coa24-tests-disclosure.l4                      0        35       0        0         0 |      0        35       0        0  same
coa24-tests-false-statements.l4                0        47       0        0         0 |      0        47       0        0  same
coa24-tests-identity.l4                        0        63       0        0         0 |      0        63       0        0  same
coa24-tests-index.l4                           0        23       0        0         0 |      0        23       0        0  same
coa24-tests-language.l4                        0        88       0        0         0 |      0        88       0        0  same
coa24-tests-officers.l4                        0        50       0        0         0 |      0        50       0        0  same
coa24-tests-penalty.l4                         0        33       0        0         0 |      0        33       0        0  same
coa24-tests-prosecution.l4                     0       129       0        0         0 |      0       129       0        0  same
coa24-tests-register.l4                        0       152       0        0         0 |      0       152       0        0  same
coa25-communications.l4                        0         0       0        0         0 |      0         0       0        0  same
coa25-names-ch1.l4                             0         0       0        0         0 |      0         0       0        0  same
coa25-names-ch2.l4                             0         0       0        0         0 |      0         0       0        0  same
coa25-notices-courts.l4                        0         0       0        0         0 |      0         0       0        0  same
coa25-part39.l4                                0         0       0        0         0 |      0         0       0        0  same
coa25-part40.l4                                0         0       0        0         0 |      0         0       0        0  same
coa25-records.l4                               0         0       0        0         0 |      0         0       0        0  same
coa25-service.l4                               0         0       0        0         0 |      0         0       0        0  same
coa25-tests-communications.l4                  0       114       0        0         0 |      0       114       0        0  same
coa25-tests-names-ch1.l4                       0       244       0        0         0 |      0       244       0        0  same
coa25-tests-names-ch2.l4                       0       127       0        0         0 |      0       127       0        0  same
coa25-tests-notices-courts.l4                  0        62       0        0         0 |      0        62       0        0  same
coa25-tests-part39.l4                          0         6       0        0         0 |      0         6       0        0  same
coa25-tests-part40.l4                          0        63       0        0         0 |      0        63       0        0  same
coa25-tests-records.l4                         0        86       0        0         0 |      0        86       0        0  same
coa25-tests-service.l4                         0        70       0        0         0 |      0        70       0        0  same
coa25-tests-valuation.l4                       0        75       0        0         0 |      0        75       0        0  same
coa25-valuation.l4                             0         0       0        0         0 |      0         0       0        0  same
coa26-ch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa26-ch2a.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2b.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2c.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2d.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch3a.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch3b.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-support.l4                               0         0       0        0         0 |      0         0       0        0  same
coa26-tests-ch1.l4                             0        41       0        0         0 |      0        41       0        0  same
coa26-tests-ch2a.l4                            0       138       0        0         0 |      0       138       0        0  same
coa26-tests-ch2b.l4                            0       151       0        0         0 |      0       151       0        0  same
coa26-tests-ch2c.l4                            0       109       0        0         0 |      0       109       0        0  same
coa26-tests-ch2d.l4                            0       151       0        0         0 |      0       151       0        0  same
coa26-tests-ch3a.l4                            0        93       0        0         0 |      0        93       0        0  same
coa26-tests-ch3b.l4                            0        84       0        0         0 |      0        84       0        0  same
coa26-tests-support.l4                         0        38       0        0         0 |      0        38       0        0  same
coa27-ch4-register.l4                          0         0       0        0         0 |      0         0       0        0  same
coa27-ch5-third-country.l4                     0         0       0        0         0 |      0         0       0        0  same
coa27-ch6-administration.l4                    0         0       0        0         0 |      0         0       0        0  same
coa27-ch6-second-audit-offences.l4             0         0       0        0         0 |      0         0       0        0  same
coa27-definitions.l4                           0         0       0        0         0 |      0         0       0        0  same
coa27-part43.l4                                0         0       0        0         0 |      0         0       0        0  same
coa27-tests-ch4-register.l4                    0        47       0        0         0 |      0        47       0        0  same
coa27-tests-ch5-third-country.l4               0        60       0        0         0 |      0        60       0        0  same
coa27-tests-ch6-administration.l4              0        90       0        0         0 |      0        90       0        0  same
coa27-tests-ch6-second-audit-offences.l4       0       170       0        0         0 |      0       170       0        0  same
coa27-tests-definitions.l4                     0       155       0        0         0 |      0       155       0        0  same
coa27-tests-part43.l4                          0       237       0        0         0 |      0       237       0        0  same
coa27-tests-transfer.l4                        0       109       0        0         0 |      0       109       0        0  same
coa27-transfer.l4                              0         0       0        0         0 |      0         0       0        0  same
coa28-part44.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part45.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part46.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-part47.l4                                0         0       0        0         0 |      0         0       0        0  same
coa28-sch1.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa28-sch1a.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-sch1b.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-sch1c.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa28-tests-part44.l4                          0       104       0        0         0 |      0       104       0        0  same
coa28-tests-part45-47.l4                       0        37       0        0         0 |      0        37       0        0  same
coa28-tests-part46.l4                          0        97       0        0         0 |      0        97       0        0  same
coa28-tests-sch1.l4                            0        89       0        0         0 |      0        89       0        0  same
coa28-tests-sch1a.l4                           0       202       0        0         0 |      0       202       0        0  same
coa28-tests-sch1b.l4                           0       189       0        0         0 |      0       189       0        0  same
coa28-tests-sch1c.l4                           0       186       0        0         0 |      0       186       0        0  same
coa29-sch2-part1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa29-sch2-part2.l4                            0         0       0        0         0 |      0         0       0        0  same
coa29-sch2-part3.l4                            0         0       0        0         0 |      0         0       0        0  same
coa29-sch4.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa29-sch5.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa29-sch6.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa29-sch7.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa29-sch8.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa29-tests-sch2-part1.l4                      0        56       0        0         0 |      0        56       0        0  same
coa29-tests-sch2-part2.l4                      0       247       0        0         0 |      0       247       0        0  same
coa29-tests-sch2-part3.l4                      0        14       0        0         0 |      0        14       0        0  same
coa29-tests-sch4.l4                            0        83       0        0         0 |      0        83       0        0  same
coa29-tests-sch5.l4                            0       193       0        0         0 |      0       193       0        0  same
coa29-tests-sch6.l4                            0        81       0        0         0 |      0        81       0        0  same
coa29-tests-sch7.l4                            0        97       0        0         0 |      0        97       0        0  same
coa29-tests-sch8.l4                            0       432       0        0         0 |      0       432       0        0  same
coa3-part8-branch.l4                           0         0       0        0         0 |      0         0       0        0  same
coa3-part8-inspection.l4                       0         0       0        0         0 |      0         0       0        0  same
coa3-part8-members.l4                          0         0       0        0         0 |      0         0       0        0  same
coa3-part8-subsidiary.l4                       0         0       0        0         0 |      0         0       0        0  same
coa3-part9-rights.l4                           0         0       0        0         0 |      0         0       0        0  same
coa3-tests-branch.l4                           0       121       0        0         0 |      0       121       0        0  same
coa3-tests-inspection.l4                       0       237       0        0         0 |      0       237       0        0  same
coa3-tests-members.l4                          0       242       0        0         0 |      0       242       0        0  same
coa3-tests-rights.l4                           0       200       0        0         0 |      0       200       0        0  same
coa3-tests-subsidiary.l4                       0       161       0        0         0 |      0       161       0        0  same
coa30-regulative.l4                            0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part1.l4                           0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part2-a.l4                         0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part2-b.l4                         0         0       0        0         0 |      0         0       0        0  same
coa30-sch11.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-sch11a.l4                                0         0       0        0         0 |      0         0       0        0  same
coa30-sch12.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-sch13.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-tests-regulative.l4                      0         0       0        0         0 |      0         0       0        0  same
coa30-tests-sch10-part1.l4                     0        95       0        0         0 |      0        95       0        0  same
coa30-tests-sch10-part2-a.l4                   0       107       0        0         0 |      0       107       0        0  same
coa30-tests-sch10-part2-b.l4                   0       263       0        0         0 |      0       263       0        0  same
coa30-tests-sch11.l4                           0       146       0        0         0 |      0       146       0        0  same
coa30-tests-sch11a.l4                          0       131       0        0         0 |      0       131       0        0  same
coa30-tests-sch12.l4                           0        34       0        0         0 |      0        34       0        0  same
coa30-tests-sch13.l4                           0       101       0        0         0 |      0       101       0        0  same
coa4-appointment.l4                            0         0       0        0         0 |      0         0       0        0  same
coa4-approval-loans.l4                         0         0       0        0         0 |      0         0       0        0  same
coa4-approval-service-property.l4              0         0       0        0         0 |      0         0       0        0  same
coa4-declaration.l4                            0         0       0        0         0 |      0         0       0        0  same
coa4-general-duties.l4                         0         0       0        0         0 |      0         0       0        0  same
coa4-notification.l4                           0         0       0        0         0 |      0         0       0        0  same
coa4-removal.l4                                0         0       0        0         0 |      0         0       0        0  same
coa4-requirements.l4                           0         0       0        0         0 |      0         0       0        0  same
coa4-tests-appointment.l4                      0        88       0        0         0 |      0        88       0        0  same
coa4-tests-approval-loans.l4                   0       187       0        0         0 |      0       187       0        0  same
coa4-tests-approval-service-property.l4        0       146       0        0         0 |      0       146       0        0  same
coa4-tests-declaration.l4                      0       107       0        0         0 |      0       107       0        0  same
coa4-tests-general-duties.l4                   0       179       0        0         0 |      0       179       0        0  same
coa4-tests-notification.l4                     0       178       0        0         0 |      0       178       0        0  same
coa4-tests-removal.l4                          0        59       0        0         0 |      0        59       0        0  same
coa4-tests-requirements.l4                     0       107       0        0         0 |      0       107       0        0  same
coa5-ch4-supplementary.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-derivative-claims.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-director-definitions.l4                   0         0       0        0         0 |      0         0       0        0  same
coa5-director-liabilities.l4                   0         0       0        0         0 |      0         0       0        0  same
coa5-director-supplementary.l4                 0         0       0        0         0 |      0         0       0        0  same
coa5-loans-exceptions.l4                       0         0       0        0         0 |      0         0       0        0  same
coa5-loss-of-office.l4                         0         0       0        0         0 |      0         0       0        0  same
coa5-quoted-company-pay.l4                     0         0       0        0         0 |      0         0       0        0  same
coa5-residential-addresses.l4                  0         0       0        0         0 |      0         0       0        0  same
coa5-service-contracts.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-tests-ch4-supplementary.l4                0        26       0        0         0 |      0        26       0        0  same
coa5-tests-derivative-claims.l4                0       228       0        0         0 |      0       228       0        0  same
coa5-tests-director-definitions.l4             0       110       0        0         0 |      0       110       0        0  same
coa5-tests-director-liabilities.l4             0       169       0        0         0 |      0       169       0        0  same
coa5-tests-director-supplementary.l4           0        54       0        0         0 |      0        54       0        0  same
coa5-tests-loans-exceptions.l4                 0       182       0        0         0 |      0       182       0        0  same
coa5-tests-loss-of-office.l4                   0       189       0        0         0 |      0       189       0        0  same
coa5-tests-quoted-company-pay.l4               0       120       0        0         0 |      0       120       0        0  same
coa5-tests-residential-addresses.l4            0        97       0        0         0 |      0        97       0        0  same
coa5-tests-service-contracts.l4                0        91       0        0         0 |      0        91       0        0  same
coa6-dual-capacity.l4                          0         0       0        0         0 |      0         0       0        0  same
coa6-notification-of-changes.l4                0         0       0        0         0 |      0         0       0        0  same
coa6-offence-of-failure-to-notify.l4           0         0       0        0         0 |      0         0       0        0  same
coa6-private-and-public.l4                     0         0       0        0         0 |      0         0       0        0  same
coa6-required-information.l4                   0         0       0        0         0 |      0         0       0        0  same
coa6-tests-notification.l4                     0        78       0        0         0 |      0        78       0        0  same
coa6-tests-offence.l4                          0        40       0        0         0 |      0        40       0        0  same
coa6-tests-private-and-public.l4               0       168       0        0         0 |      0       168       0        0  same
coa6-tests-required-information.l4             0        56       0        0         0 |      0        56       0        0  same
coa6-tests-vacancy-and-dual-capacity.l4        0        20       0        0         0 |      0        20       0        0  same
coa6-vacancy.l4                                0         0       0        0         0 |      0         0       0        0  same
coa7-ch1.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-ch2.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-ch3a.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa7-ch3b.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa7-ch3c.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa7-ch3d.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa7-ch4.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-ch5.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-ch6.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-ch7.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa7-regulative.l4                             0        10       0        0         0 |      0        10       0        0  same
coa7-tests-ch1.l4                              0       109       0        0         0 |      0       109       0        0  same
coa7-tests-ch2.l4                              0       148       0        0         0 |      0       148       0        0  same
coa7-tests-ch3a.l4                             0        70       0        0         0 |      0        70       0        0  same
coa7-tests-ch3b.l4                             0       159       0        0         0 |      0       159       0        0  same
coa7-tests-ch3c.l4                             0       143       0        0         0 |      0       143       0        0  same
coa7-tests-ch3d.l4                             0       180       0        0         0 |      0       180       0        0  same
coa7-tests-ch4.l4                              0       136       0        0         0 |      0       136       0        0  same
coa7-tests-ch5.l4                              0       225       0        0         0 |      0       225       0        0  same
coa7-tests-ch6.l4                              0        80       0        0         0 |      0        80       0        0  same
coa7-tests-ch7.l4                              0        67       0        0         0 |      0        67       0        0  same
coa8-helpers.l4                                0         0       0        0         0 |      0         0       0        0  same
coa8-part14-authorisation.l4                   0         0       0        0         0 |      0         0       0        0  same
coa8-part14-exemptions.l4                      0         0       0        0         0 |      0         0       0        0  same
coa8-part14-meanings.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part14-remedies.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-accounts.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-approval.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-group.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-notes.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-records.l4                         0         0       0        0         0 |      0         0       0        0  same
coa8-part15-small.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-year.l4                            0         0       0        0         0 |      0         0       0        0  same
coa8-regulative.l4                             0         0       0        0         0 |      0         0       0        0  same
coa8-tests-helpers.l4                          0        29       0        0         0 |      0        29       0        0  same
coa8-tests-part14-authorisation.l4             0        84       0        0         0 |      0        84       0        0  same
coa8-tests-part14-exemptions.l4                0        85       0        0         0 |      0        85       0        0  same
coa8-tests-part14-meanings.l4                  0        68       0        0         0 |      0        68       0        0  same
coa8-tests-part14-remedies.l4                  0       105       0        0         0 |      0       105       0        0  same
coa8-tests-part15-accounts.l4                  0       134       0        0         0 |      0       134       0        0  same
coa8-tests-part15-approval.l4                  0        48       0        0         0 |      0        48       0        0  same
coa8-tests-part15-group.l4                     0       175       0        0         0 |      0       175       0        0  same
coa8-tests-part15-notes.l4                     0       100       0        0         0 |      0       100       0        0  same
coa8-tests-part15-records.l4                   0        76       0        0         0 |      0        76       0        0  same
coa8-tests-part15-small.l4                     0       180       0        0         0 |      0       180       0        0  same
coa8-tests-part15-year.l4                      0        89       0        0         0 |      0        89       0        0  same
coa9-approval.l4                               0         0       0        0         0 |      0         0       0        0  same
coa9-circulation.l4                            0         0       0        0         0 |      0         0       0        0  same
coa9-directors-report.l4                       0         0       0        0         0 |      0         0       0        0  same
coa9-laying.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa9-penalties.l4                              0         0       0        0         0 |      0         0       0        0  same
coa9-publication.l4                            0         0       0        0         0 |      0         0       0        0  same
coa9-remuneration.l4                           0         0       0        0         0 |      0         0       0        0  same
coa9-strategic.l4                              0         0       0        0         0 |      0         0       0        0  same
coa9-tests-approval.l4                         0        78       0        0         0 |      0        78       0        0  same
coa9-tests-circulation.l4                      0        75       0        0         0 |      0        75       0        0  same
coa9-tests-directors-report.l4                 0        79       0        0         0 |      0        79       0        0  same
coa9-tests-laying.l4                           0        24       0        0         0 |      0        24       0        0  same
coa9-tests-publication.l4                      0       194       0        0         0 |      0       194       0        0  same
coa9-tests-remuneration.l4                     0        55       0        0         0 |      0        55       0        0  same
coa9-tests-strategic.l4                        0       198       0        0         0 |      0       198       0        0  same
tests-independent-g1.l4                        0       734       0        0         0 |      0       734       0        0  same
tests-independent-g2.l4                        0       631       0        0         0 |      0       631       0        0  same
tests-independent-g3.l4                        0       440       0        0         0 |      0       440       0        0  same
tests-independent-g4.l4                        0       356       0        0         0 |      0       356       0        0  same
tests-independent-g5.l4                        0       963       0        0         0 |      0       963       0        0  same
tests-independent-g6.l4                        0       689       0        0         0 |      0       689       0        0  same
TOTAL (453 modules)                            0     40076       0        0           |      0     40076       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The total is 40,076 assertions satisfied over 453 modules, with 0 errors, 0 failed and 0 refused, identical on the main build.
`check.sh` does not see a `#TRACE` outcome, because a trace prints no assertion line; each part read its own traces on both builds by hand (see its NOTES).

## The seat-question audits

A seat question is the question as the person in the seat would ask it; its name must ask what the layer-1 function it calls answers, in the same direction. A question titled as a permission over a function that answers the bar (or the reverse) makes `JUST TRUE` read as the opposite of what it means, so each part was audited for it.
- **First audit, by the part's own agent, resumed with only that task:** 23 parts, 144 of 2,106 seat questions retitled (6.8%); per part from 0% to 18%. Direction mismatches (a permission title over a bar, or the reverse) and subject mismatches ("must" over "have", a premise or consequence carried in the name, a necessary condition titled as a grant).
- **Second pass, by the agent that had already audited itself under the brief's seat-direction paragraph:** 7 parts, 153 of 604 seat questions retitled (25.3%), found after the part's own check under the brief had found few (`coa9`: 2 of 128 at its own check, 17 more at the second pass). The own check reads a question against its own title, which always agrees with itself; the second pass reads it against the body of the function.
- **Nothing was negated.** The fix was always to retitle the question so that it asks what the function answers; a bar's `NOTHING` and `JUST FALSE` are not a grant.
- **Assertions restated in place** carry `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>`; facts and expected values did not change by a retitle.
- **Precision of the second pass, measured by the lead (limit stated).** The pass flagged 177 of 665 seat questions (27%) over the eight parts that had finished it when it was measured (seven UK parts and one Canadian part). Of 20 flagged questions drawn at random (5 from each of `coa10`, `coa11`, `coa12`, `coa14`, from the 104 whose old title can be recovered from the part's `RECONCILED` comments), the lead judged each against the function body without reading the agent's reason: 7 were real mismatches (the title asks a different limb, route or scope than the body answers, or carries a premise the function does not compute, or has a different answer type), 7 were borderline (the old title restated the function's own name and differed only from an input the function tests) and 6 were cosmetic (same value, different wording). So about 35% of the flags were clear mismatches (70% with the borderline ones): roughly 9% of questions, in line with the first audit's 7%. **Limit: four of the eight parts (`coa6`, `coa9`, `coa16` and one Canadian part) could not be sampled, because their old titles are not recoverable from their comments.** The brief of the pass was tightened afterwards to the four kinds of real mismatch; the parts done before the tightening were not re-run (the coordinating session agreed), so their retitles are accurate but sometimes more than needed.

## The grant and power name test

A function **named for a grant or a power** ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The Guide (section 5, "In short") gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". The coordinating session ruled on 2026-11-12, with three limits:
1. **Flip to `NOTHING`**, with one fork line each, only a function named for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an `if` gate failed.
2. **Keep `JUST FALSE`** where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question.
3. **Do not flip, list instead**, in the part's fork register: "may" functions whose gate is "where", "when" or "upon" (and the equivalents the parts placed with them: "in the case of", "so long as", "while", "on payment", "after ..."; **assumed, not ruled**, part by part), because ruling (b) of the Guide's periods, where and scope-limits paragraph says `JUST FALSE` and the Guide's line on grants points the other way: a question for the maintainer or a lawyer; and "entitled"-named functions, because an entitlement is a claim, not a power, and the Guide does not settle it.
Functions named "it is lawful ..." are outside the sweep (the parts' sweep subsections report none in this Act).

The counts below are read from each part's own NOTES (section "Name-test sweep of 2026-11-12"); a function can be counted in two columns when its `if` branch is flipped and its `where` branch is listed.

| part | flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- | --- |
| coa1 | 3 | 9 | 1 | 0 |
| coa2 | 12 | 18 | 10 | 0 |
| coa3 | 5 | 6 | 10 | 1 |
| coa4 | 3 | 5 | 3 | 1 |
| coa5 | 9 | 16 | 0 | 8 |
| coa6 | 2 | 0 | 4 | 0 |
| coa7 | 4 | 21 | 8 | 5 |
| coa8 | 1 | 11 | 8 | 4 |
| coa9 | 0 | 0 | 3 | 5 |
| coa10 | 9 | 4 | 4 | 0 |
| coa11 | 0 | 6 | 1 | 4 |
| coa12 | 11 | 11 | 7 | 6 |
| coa13 | 12 | 18 | 5 | 3 |
| coa14 | 2 | 13 | 8 | 1 |
| coa15 | 13 | 17 | 9 | 2 |
| coa16 | 0 | 3 | 7 | 1 |
| coa17 | 4 | 2 | 6 | 1 |
| coa18 | 7 | 11 | 14 | 7 |
| coa19 | 10 | 0 | 5 | 5 |
| coa20 | 8 | 6 | 3 | 2 |
| coa21 | 8 | 10 | 5 | 0 |
| coa22 | 11 | 15 | 8 | 0 |
| coa23 | 4 | 7 | 6 | 0 |
| coa24 | 4 | 18 | 0 | 0 |
| coa25 | 3 | 6 | 3 | 2 |
| coa26 | 2 | 10 | 10 | 0 |
| coa27 | 14 | 8 | 6 | 0 |
| coa28 | 2 | 2 | 1 | 2 |
| coa29 | 0 | 10 | 2 | 0 |
| coa30 | 7 | 12 | 7 | 0 |
| **all 30 parts** | **170** | **275** | **164** | **60** |

**Open for the maintainer or a lawyer: the 164 listed "may" functions with a where/when/upon-kind gate and the 60 "entitled" functions.** They answer as the Guide's own rulings give (for a failed `where`, `JUST FALSE`; the other reading is `NOTHING`), and each has a row in its part's fork register naming the other reading.
**A flip changes what every caller of the function sees.** Where a flipped function is read by another function of the same part, the part checked the caller (for example `s 552(1)` in `coa13`, `s 694(1)` in `coa15`, `s 966(1)` and `s 971(1)` in `coa21`, `s 1253D(1)` in `coa27`, and the caller adjustments of `coa8`); no part module imports another part's module (checked at the merge), so a caller is always in the same part and what crosses parts is a seam, which is an input.

## The independent test pass

Six readers, one per group of consecutive parts (a whole Act is too long for one), each read only the text of its group's ranges and wrote its scenarios and expected answers (`ANSWERS.md`, not kept) **before** opening any `.l4` file, then wrote `tests-independent-gN.l4` against the group's modules and ran it. A failing assertion was left failing; each reader then wrote a triage with a verdict word per failure: `ENCODER` (the encoding is wrong), `SCENARIO` (the reader's own mistake), `AMBIGUOUS` (the text reads both ways) or `GAP` (no function can be asked the scenario). Readers were given the Guide's FALSE and NOTHING convention verbatim, so their disagreements are about the text and not about the convention.

| group | parts | words of text | scenarios | assertions (as returned) | failed as returned | ENCODER | SCENARIO | AMBIGUOUS | GAP | assertions now |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g1 | coa1 to coa5 | 66,686 | 536 | 734 | 25 | 1 | 12 | 12 | 6 | 734 |
| g2 | coa6 to coa11 | 63,447 | 642 | 631 | 13 | 1 | 3 | 6 | 57 | 631 |
| g3 | coa12 to coa17 | 70,562 | 220 | 440 | 24 | 5 | 7 | 12 | 3 | 440 |
| g4 | coa18 to coa22 | 74,243 | 281 | 356 | 13 | 1 | 10 | 2 | 13 | 356 |
| g5 | coa23 to coa27 | 62,342 | 783 | 963 | 74 | 8 | 55 | 11 | 111 | 963 |
| g6 | coa28 to coa30 | 46,059 | 653 | 689 | 26 | 9 | 8 | 9 | 94 | 689 |

The verdict columns do not always sum to "failed as returned", because a `GAP` verdict can sit on a failed line as well as on a scenario with no assertion. In `g2`, 3 of the 13 failed lines carry `GAP` (scenarios 561b, 580b and 641, on `s 485(5)` and `s 489(5)`, for which the reader found no seat question asking the section's own rule); the other 10 are the 1 + 3 + 6 under `ENCODER`, `SCENARIO` and `AMBIGUOUS`. `coa11` later added seat questions for both sections.

After the parts' audits, sweeps and repairs, each group's file was brought up to the final modules: a seat question renamed by an audit was renamed in the reader's file; a failure that was the reader's own mistake (`SCENARIO`), or a reading the text leaves open (`AMBIGUOUS`), was restated in place to the encoding's answer with a `-- RECONCILED 2026-11-12: was EQUALS <old>; <reason>` comment that cites the Guide sentence or says that none decides it; a failure that was a real `ENCODER` finding was sent to the part agent, repaired, and the reader's own expectation then passes unchanged. **An `AMBIGUOUS` restatement is the encoder's reading, not a ruling:** it is recorded for a lawyer in the part's fork register.
**How the `ENCODER` verdicts were settled.** A reader's `ENCODER` verdict is as returned; it was settled in one of three ways, so the counts in the table are findings, not defects left open: (a) a real inconsistency, repaired in the part with the reader's expectation unchanged (for example `s 113(7)` in `coa3`, `s 421(3)` in `coa9`, `s 876(1)` in `coa19`, and the layer-1 gather behind the `s 645` seat question in `coa14`); (b) a seat question titled the opposite of what its function answers, retitled by the seat-question audit (most of the `ENCODER` verdicts of group 5); (c) a function named for a grant or a power that answers `NOTHING` for an unmet `if`, which the reader read against the Guide's worked example 1 but the grant and power name test settles as `NOTHING` (all five of group 3, and `s 1199A(1)` in group 5): those lines were restated as `AMBIGUOUS`, with the name-test ruling cited.
The as-returned copy of each file (with its failing assertions) is `notes/independent/gN-tests-independent-as-returned.l4.txt`, and each reader's triage is `notes/independent/gN-triage.md`. **Independence, as the readers reported it in their final messages (not kept in this folder).** The brief required each reader to finish `ANSWERS.md` before opening any `.l4` file; `g1`, `g3` and `g5` say in terms that they did, and none reports otherwise. All six report opening no NOTES, PROGRESS or plan file. **Limit:** the modules' header comments restate or cite the encoder's reading rules and its notes, and a reader who opened a module saw them; `g1` and `g2` say so, and `g2` also read the encoding's own comments on `s 279M` and `s 485(5)` in order to write its verdicts. The readers were therefore not blind to the encoder's conventions once they had written their answers (`g3` also read the encoder's fork labels in the comments, after an assertion had failed).

## Findings the merge leaves open (for a lawyer)

Status: **reported by the part agents and the readers, not re-checked by the merge.** None is resolved here.
- Lists that end with a catch-all limb: Schedule 10 paragraph 3(6) answers `JUST FALSE` (`coa30`), while `s 1275(3A)` and `s 1278(1)` answer `NOTHING` (`coa28`).
- Eight same-shape answers in `coa19` moved to `NOTHING` (its fork `F-Y1`); the least plain are `s 859J(2)` and `s 865(1)`.
- `s 992(6)` (`coa21`, its forks F11 and M10) and `s 887(2)` (three readings, `coa19`, fork F-M1).
- Parts 38 and 39 have no seat questions.
- `s 414A(5)` (`coa8`) answers `JUST FALSE` where `s 451(1)` (`coa10`) answers `NOTHING` on the same structure (found by the group-2 reader).
- The "without reasonable excuse" offences: `s 113(7)`, `s 113H(1)` and `s 113H(2)` (`coa3`) answer `JUST FALSE` for an excused default, like `s 86(3)` and `s 167L(1)`; `s 113G(1)` and `(2)` answer `NOTHING` because the excuse sits in a "who" clause, and `coa3`'s fork F35 says a one-line change aligns them.
- Fixed periods: `s 421(3)` (`coa9`) was aligned to `JUST FALSE` outside its five years, like `s 412(5)` (`coa8`); other functions with fixed-period wording may still answer `NOTHING` outside the period.
- Six seat inputs ask the person to carry another question's answer as a plain yes or no: "merger relief applies" in the `s 610(5)`, `s 612(2)` and `s 612(3)` questions, "supported by a solvency statement" in `s 641`, "in accordance with section 643" in `s 642`, and "section 646 applies" in `s 646` (`coa14`). The carried answer can be "not covered", and a person who answers "no" turns that `NOTHING` into a `JUST FALSE`; only the `s 646` input's description warns of it.
- The same shape treated oppositely: `s 501(3)`'s "unless it was not reasonably practicable" answers `JUST FALSE` once met, while `s 790F(1)`'s "without reasonable excuse" answers `NOTHING` (found by the group-3 reader; the 2026-11-05 case-by-case ruling leaves such sites to the encoder, with a fork line).
- `coa9` aligned `s 421(3)`, `s 416(1)(a)`, `s 439A(1)(a)` and `s 439A(3)` to `JUST FALSE` outside a period the text fixes (fork F35); the last three went beyond the site the reader found, on the same test, and `s 421(3)` and `s 416(1)(a)` now also answer `JUST FALSE` for a person who was never a director.
- The functions the sweep flipped are read by seat questions in the same part, whose `@export` text says what `NOTHING` now means; a reader of a seat answer should read that text.
- The mechanical consistency check between each part's coverage table and its fork register (coarse: an `F` identifier in a coverage row that is absent from the fork register) found: no part with an identifier absent from its fork register.

## What each part's notes hold

**keel**
- `notes/keel-NOTES.md:5` Source and what "verified" means here
- `notes/keel-NOTES.md:9` Seat
- `notes/keel-NOTES.md:13` What is encoded and what is not
- `notes/keel-NOTES.md:19` Coverage table
- `notes/keel-NOTES.md:125` Fork register
- `notes/keel-NOTES.md:165` Marginal readings for a lawyer
- `notes/keel-NOTES.md:186` Jural relations
- `notes/keel-NOTES.md:288` What the stable binary does not accept, and what it does
- `notes/keel-NOTES.md:298` What `check.sh` printed
- `notes/keel-NOTES.md:314` Open questions for a domain expert
- `notes/keel-NOTES.md:323` Copied modules

**coa1**
- `notes/coa1-NOTES.md:5` Source and what "verified" means here
- `notes/coa1-NOTES.md:9` Seat
- `notes/coa1-NOTES.md:13` What is encoded and what is not
- `notes/coa1-NOTES.md:23` Coverage (coa1)
- `notes/coa1-NOTES.md:550` Fork register (coa1)
- `notes/coa1-NOTES.md:810` Jural relations (coa1)
- `notes/coa1-NOTES.md:892` Marginal readings for a lawyer (coa1)
- `notes/coa1-NOTES.md:1038` Seams (coa1)
- `notes/coa1-NOTES.md:1076` What the text turns out to say (findings)
- `notes/coa1-NOTES.md:1089` What the stable binary does not accept, and what it does
- `notes/coa1-NOTES.md:1101` What `check.sh` printed
- `notes/coa1-NOTES.md:1126` Open questions for a domain expert
- `notes/coa1-NOTES.md:1136` Seat layer: the questions, in the text's order
- `notes/coa1-NOTES.md:1246` Copied modules

**coa2**
- `notes/coa2-NOTES.md:14` Files
- `notes/coa2-NOTES.md:34` Coverage (coa2)
- `notes/coa2-NOTES.md:875` Fork register (coa2)
- `notes/coa2-NOTES.md:986` Jural relations (coa2)
- `notes/coa2-NOTES.md:1159` Marginal readings for a lawyer (coa2)
- `notes/coa2-NOTES.md:1514` Seams (coa2)
- `notes/coa2-NOTES.md:1563` What the text turns out to say (numbered findings)
- `notes/coa2-NOTES.md:1575` What the stable binary does not accept (measured on 1.6.110; 1.6.109 gives the same assertion counts and the same 22 trace results)
- `notes/coa2-NOTES.md:1592` The seat layer (`coa2-seat.l4`, `coa2-cases-seat.l4`)
- `notes/coa2-NOTES.md:1621` What `check.sh` prints

**coa3**
- `notes/coa3-NOTES.md:6` What this is and what it rests on
- `notes/coa3-NOTES.md:13` Seat
- `notes/coa3-NOTES.md:23` Where this file and the brief differ from PLAN.md
- `notes/coa3-NOTES.md:29` Rulings applied (copied word for word from the brief)
- `notes/coa3-NOTES.md:46` Seat questions (coa3)
- `notes/coa3-NOTES.md:192` Coverage (coa3)
- `notes/coa3-NOTES.md:871` Fork register (coa3)
- `notes/coa3-NOTES.md:913` Jural relations (coa3)
- `notes/coa3-NOTES.md:1042` Marginal readings for a lawyer (coa3)
- `notes/coa3-NOTES.md:1406` Seams (coa3)
- `notes/coa3-NOTES.md:1438` What the text turns out to say (coa3)
- `notes/coa3-NOTES.md:1453` What the stable binary does not accept (coa3)
- `notes/coa3-NOTES.md:1462` What `check.sh` prints (coa3)

**coa4**
- `notes/coa4-NOTES.md:7` The files
- `notes/coa4-NOTES.md:33` The brief and PLAN.md
- `notes/coa4-NOTES.md:39` The seat layer, and what it leaves out
- `notes/coa4-NOTES.md:164` Coverage (coa4)
- `notes/coa4-NOTES.md:819` Fork register (coa4)
- `notes/coa4-NOTES.md:906` Jural relations (coa4)
- `notes/coa4-NOTES.md:1008` Marginal readings for a lawyer (coa4)
- `notes/coa4-NOTES.md:1102` Seams (coa4)
- `notes/coa4-NOTES.md:1163` What the text turns out to say
- `notes/coa4-NOTES.md:1176` What the stable binary does not accept (1.6.110; the same modules read the same on 1.6.109)
- `notes/coa4-NOTES.md:1190` Tests
- `notes/coa4-NOTES.md:1194` What check.sh prints

**coa5**
- `notes/coa5-NOTES.md:11` What is here
- `notes/coa5-NOTES.md:35` Seat (coa5)
- `notes/coa5-NOTES.md:104` Coverage (coa5)
- `notes/coa5-NOTES.md:936` Fork register (coa5)
- `notes/coa5-NOTES.md:1054` Jural relations (coa5)
- `notes/coa5-NOTES.md:1160` Marginal readings for a lawyer (coa5)
- `notes/coa5-NOTES.md:1244` Seams (coa5)
- `notes/coa5-NOTES.md:1267` Numbered findings: what the text turns out to say
- `notes/coa5-NOTES.md:1301` What the stable binary does not accept
- `notes/coa5-NOTES.md:1316` What check.sh prints

**coa6**
- `notes/coa6-NOTES.md:9` Source and what "verified" means here
- `notes/coa6-NOTES.md:17` Where this brief and PLAN.md differ
- `notes/coa6-NOTES.md:26` Seat
- `notes/coa6-NOTES.md:33` What is encoded and what is not
- `notes/coa6-NOTES.md:40` Coverage (coa6)
- `notes/coa6-NOTES.md:224` Fork register (coa6)
- `notes/coa6-NOTES.md:418` Jural relations (coa6)
- `notes/coa6-NOTES.md:462` Marginal readings for a lawyer (coa6)
- `notes/coa6-NOTES.md:508` Seams (coa6)
- `notes/coa6-NOTES.md:542` What the text turns out to say (coa6)
- `notes/coa6-NOTES.md:576` The seat layer
- `notes/coa6-NOTES.md:665` What the stable binary does not accept (and what it does)
- `notes/coa6-NOTES.md:686` What `check.sh` printed
- `notes/coa6-NOTES.md:720` Open questions for a domain expert
- `notes/coa6-NOTES.md:734` Files

**coa7**
- `notes/coa7-NOTES.md:5` Source and what "verified" means here
- `notes/coa7-NOTES.md:9` Seat
- `notes/coa7-NOTES.md:13` What is encoded and what is not
- `notes/coa7-NOTES.md:19` Coverage (coa7)
- `notes/coa7-NOTES.md:939` Fork register (coa7)
- `notes/coa7-NOTES.md:1357` Marginal readings for a lawyer (coa7)
- `notes/coa7-NOTES.md:1792` Jural relations (coa7)
- `notes/coa7-NOTES.md:2160` Seams (coa7)
- `notes/coa7-NOTES.md:2184` Findings (what the text turns out to say)
- `notes/coa7-NOTES.md:2205` What the stable binary does not accept, and what it does
- `notes/coa7-NOTES.md:2215` The regulative rules and their traces
- `notes/coa7-NOTES.md:2233` The seat layer
- `notes/coa7-NOTES.md:2436` What `check.sh` printed
- `notes/coa7-NOTES.md:2477` Open questions for a domain expert
- `notes/coa7-NOTES.md:2489` NEEDS-CORE, copied modules, peeked

**coa8**
- `notes/coa8-NOTES.md:30` Rulings applied (coa8)
- `notes/coa8-NOTES.md:48` Coverage (coa8)
- `notes/coa8-NOTES.md:816` Fork register (coa8)
- `notes/coa8-NOTES.md:898` Jural relations (coa8)
- `notes/coa8-NOTES.md:957` Marginal readings for a lawyer (coa8)
- `notes/coa8-NOTES.md:1007` Seams (coa8)
- `notes/coa8-NOTES.md:1078` Seat layer (coa8)
- `notes/coa8-NOTES.md:1299` Numbered findings: what the text turns out to say, and what the work turned up
- `notes/coa8-NOTES.md:1336` What the stable binary does not accept (and what it accepts without saying so)
- `notes/coa8-NOTES.md:1386` What check.sh prints
- `notes/coa8-NOTES.md:1432` Where PLAN.md and the brief differ (the brief governs)
- `notes/coa8-NOTES.md:1440` Honest limits

**coa9**
- `notes/coa9-NOTES.md:8` What this encoding is
- `notes/coa9-NOTES.md:46` Coverage (coa9)
- `notes/coa9-NOTES.md:544` Fork register (coa9)
- `notes/coa9-NOTES.md:607` Jural relations (coa9)
- `notes/coa9-NOTES.md:723` Marginal readings for a lawyer (coa9)
- `notes/coa9-NOTES.md:937` Seams (coa9)
- `notes/coa9-NOTES.md:985` What the text turns out to say (numbered findings)
- `notes/coa9-NOTES.md:1008` What the stable binary does not accept (and other traps met)
- `notes/coa9-NOTES.md:1021` Traces (the regulative rules)
- `notes/coa9-NOTES.md:1044` Direction audit of the seat layer
- `notes/coa9-NOTES.md:1205` What `check.sh` prints
- `notes/coa9-NOTES.md:1253` Rulings recorded word for word

**coa10**
- `notes/coa10-NOTES.md:9` What this part is
- `notes/coa10-NOTES.md:17` The text in this file
- `notes/coa10-NOTES.md:23` Rulings applied (coa10)
- `notes/coa10-NOTES.md:49` Coverage (coa10)
- `notes/coa10-NOTES.md:683` Fork register (coa10)
- `notes/coa10-NOTES.md:810` Jural relations (coa10)
- `notes/coa10-NOTES.md:929` Marginal readings for a lawyer (coa10)
- `notes/coa10-NOTES.md:1177` Seams (coa10)
- `notes/coa10-NOTES.md:1239` The seat layer (coa10)
- `notes/coa10-NOTES.md:1405` Findings: what the text turns out to say (coa10)
- `notes/coa10-NOTES.md:1424` What the stable binary does not accept (coa10)
- `notes/coa10-NOTES.md:1435` What check.sh printed (coa10)

**coa11**
- `notes/coa11-NOTES.md:7` Source and what "verified" means here
- `notes/coa11-NOTES.md:18` Seat
- `notes/coa11-NOTES.md:25` What is encoded and what is not
- `notes/coa11-NOTES.md:33` Coverage (coa11)
- `notes/coa11-NOTES.md:458` Fork register (coa11)
- `notes/coa11-NOTES.md:544` Marginal readings for a lawyer (coa11)
- `notes/coa11-NOTES.md:569` Jural relations (coa11)
- `notes/coa11-NOTES.md:625` Seams (coa11)
- `notes/coa11-NOTES.md:655` What the text turns out to say (findings)
- `notes/coa11-NOTES.md:670` What the stable binary does not accept, and what it does
- `notes/coa11-NOTES.md:680` What `check.sh` printed
- `notes/coa11-NOTES.md:706` Seat questions (the audit of direction required by the brief)
- `notes/coa11-NOTES.md:808` Open questions for a domain expert
- `notes/coa11-NOTES.md:817` Peeked
- `notes/coa11-NOTES.md:822` Index of the layer-1 names

**coa12**
- `notes/coa12-NOTES.md:5` About this text and this note
- `notes/coa12-NOTES.md:30` Files (coa12)
- `notes/coa12-NOTES.md:52` Coverage (coa12)
- `notes/coa12-NOTES.md:765` Fork register (coa12)
- `notes/coa12-NOTES.md:987` Jural relations (coa12)
- `notes/coa12-NOTES.md:1185` Marginal readings for a lawyer (coa12)
- `notes/coa12-NOTES.md:1549` Seams (coa12)
- `notes/coa12-NOTES.md:1618` What the text does not answer (coa12)
- `notes/coa12-NOTES.md:1686` What the text turns out to say (coa12)
- `notes/coa12-NOTES.md:1719` What the stable binary does not accept (coa12)
- `notes/coa12-NOTES.md:1749` The seat layer (coa12)
- `notes/coa12-NOTES.md:1866` Tests (coa12)
- `notes/coa12-NOTES.md:1874` What check.sh prints

**coa13**
- `notes/coa13-NOTES.md:5` Source and what "verified" means here
- `notes/coa13-NOTES.md:9` Seat
- `notes/coa13-NOTES.md:13` What is encoded and what is not
- `notes/coa13-NOTES.md:21` Coverage (coa13)
- `notes/coa13-NOTES.md:634` Fork register (coa13)
- `notes/coa13-NOTES.md:748` Jural relations (coa13)
- `notes/coa13-NOTES.md:1002` Marginal readings for a lawyer (coa13)
- `notes/coa13-NOTES.md:1229` Seams (coa13)
- `notes/coa13-NOTES.md:1271` Seat layer (coa13)
- `notes/coa13-NOTES.md:1319` Findings: what the text turns out to say (coa13)
- `notes/coa13-NOTES.md:1336` What the stable binary does not accept, and what it does (coa13)
- `notes/coa13-NOTES.md:1349` What `check.sh` printed (coa13)
- `notes/coa13-NOTES.md:1410` Open questions for a domain expert (coa13)
- `notes/coa13-NOTES.md:1422` peeked (coa13)

**coa14**
- `notes/coa14-NOTES.md:7` Source: a converter-made rendering, not the official text
- `notes/coa14-NOTES.md:16` Where PLAN.md and the brief differ
- `notes/coa14-NOTES.md:22` Seat
- `notes/coa14-NOTES.md:197` What is encoded
- `notes/coa14-NOTES.md:214` Coverage (coa14)
- `notes/coa14-NOTES.md:800` Fork register (coa14)
- `notes/coa14-NOTES.md:913` Jural relations (coa14)
- `notes/coa14-NOTES.md:1049` Marginal readings for a lawyer (coa14)
- `notes/coa14-NOTES.md:1250` Seams (coa14)
- `notes/coa14-NOTES.md:1284` Findings: what the text turns out to say
- `notes/coa14-NOTES.md:1307` What the stable binary does not accept (and what I measured)
- `notes/coa14-NOTES.md:1322` What check.sh prints

**coa15**
- `notes/coa15-NOTES.md:11` Status of the claims below, and how each was checked
- `notes/coa15-NOTES.md:23` What this folder holds
- `notes/coa15-NOTES.md:35` Coverage (coa15)
- `notes/coa15-NOTES.md:857` Audit of the coverage table
- `notes/coa15-NOTES.md:865` Fork register (coa15)
- `notes/coa15-NOTES.md:927` Jural relations (coa15)
- `notes/coa15-NOTES.md:1274` Marginal readings for a lawyer (coa15)
- `notes/coa15-NOTES.md:1783` Seams (coa15)
- `notes/coa15-NOTES.md:1821` What the text turns out to say (numbered findings)
- `notes/coa15-NOTES.md:1837` Seat audit of 2026-11-12
- `notes/coa15-NOTES.md:2012` Name-test sweep of 2026-11-12
- `notes/coa15-NOTES.md:2075` What the stable binary does not accept
- `notes/coa15-NOTES.md:2090` What check.sh printed

**coa16**
- `notes/coa16-NOTES.md:7` Source and what "verified" means here
- `notes/coa16-NOTES.md:14` Seat
- `notes/coa16-NOTES.md:21` What is encoded and what is not
- `notes/coa16-NOTES.md:41` Coverage (coa16)
- `notes/coa16-NOTES.md:357` Fork register (coa16)
- `notes/coa16-NOTES.md:448` Jural relations (coa16)
- `notes/coa16-NOTES.md:531` Marginal readings for a lawyer (coa16)
- `notes/coa16-NOTES.md:567` Seat questions: each name against the layer-1 function it calls
- `notes/coa16-NOTES.md:659` Regulative rules and the traces
- `notes/coa16-NOTES.md:665` Seams (coa16)
- `notes/coa16-NOTES.md:690` Findings: what the text turns out to say
- `notes/coa16-NOTES.md:707` What the stable binary does not accept, and what it does
- `notes/coa16-NOTES.md:716` What check.sh printed
- `notes/coa16-NOTES.md:752` Open questions for a domain expert
- `notes/coa16-NOTES.md:763` Copied modules

**coa17**
- `notes/coa17-NOTES.md:5` Edition, method and target
- `notes/coa17-NOTES.md:12` Seat
- `notes/coa17-NOTES.md:42` What is encoded and what is not
- `notes/coa17-NOTES.md:48` Coverage (coa17)
- `notes/coa17-NOTES.md:830` Fork register (coa17)
- `notes/coa17-NOTES.md:971` Jural relations (coa17)
- `notes/coa17-NOTES.md:1224` Marginal readings for a lawyer (coa17)
- `notes/coa17-NOTES.md:1364` Seams (coa17)
- `notes/coa17-NOTES.md:1385` What the text turns out to say (findings)
- `notes/coa17-NOTES.md:1400` What the stable binary does not accept
- `notes/coa17-NOTES.md:1412` Files
- `notes/coa17-NOTES.md:1537` What check.sh prints
- `notes/coa17-NOTES.md:1586` Peeked

**coa18**
- `notes/coa18-NOTES.md:15` Where PLAN.md and the brief differ (the brief governs)
- `notes/coa18-NOTES.md:25` Seat
- `notes/coa18-NOTES.md:203` What is encoded and what is not
- `notes/coa18-NOTES.md:211` Coverage (coa18)
- `notes/coa18-NOTES.md:1029` Fork register (coa18)
- `notes/coa18-NOTES.md:1204` Jural relations (coa18)
- `notes/coa18-NOTES.md:1288` Marginal readings for a lawyer (coa18)
- `notes/coa18-NOTES.md:1657` Seams (coa18)
- `notes/coa18-NOTES.md:1714` What the text turns out to say
- `notes/coa18-NOTES.md:1744` What the stable binary does not accept, and what it does
- `notes/coa18-NOTES.md:1766` What `check.sh` printed

**coa19**
- `notes/coa19-NOTES.md:7` Source and what "verified" means here
- `notes/coa19-NOTES.md:13` Seat
- `notes/coa19-NOTES.md:18` What is encoded and what is not
- `notes/coa19-NOTES.md:27` Coverage (coa19)
- `notes/coa19-NOTES.md:657` Fork register (coa19)
- `notes/coa19-NOTES.md:767` Marginal readings for a lawyer (coa19)
- `notes/coa19-NOTES.md:1014` Jural relations (coa19)
- `notes/coa19-NOTES.md:1144` Seams (coa19)
- `notes/coa19-NOTES.md:1163` What the text turns out to say (findings, numbered)
- `notes/coa19-NOTES.md:1179` What the stable binary does not accept, and what it does
- `notes/coa19-NOTES.md:1195` Regulative traces
- `notes/coa19-NOTES.md:1199` What `check.sh` printed
- `notes/coa19-NOTES.md:1234` Open questions for a domain expert
- `notes/coa19-NOTES.md:1245` Copied modules

**coa20**
- `notes/coa20-NOTES.md:7` Source and what "verified" means here
- `notes/coa20-NOTES.md:11` Method, and what was not done
- `notes/coa20-NOTES.md:15` Seat
- `notes/coa20-NOTES.md:19` What is encoded and what is not
- `notes/coa20-NOTES.md:25` Differences from PLAN.md
- `notes/coa20-NOTES.md:40` Findings: what the text turns out to say
- `notes/coa20-NOTES.md:56` What the stable binary does not accept, and what it does
- `notes/coa20-NOTES.md:65` Coverage (coa20)
- `notes/coa20-NOTES.md:904` Fork register (coa20)
- `notes/coa20-NOTES.md:1016` Jural relations (coa20)
- `notes/coa20-NOTES.md:1358` Marginal readings for a lawyer (coa20)
- `notes/coa20-NOTES.md:1611` Seams (coa20)
- `notes/coa20-NOTES.md:1757` Seat questions
- `notes/coa20-NOTES.md:1849` What `check.sh` printed
- `notes/coa20-NOTES.md:1879` Open questions for a domain expert
- `notes/coa20-NOTES.md:1888` Copied modules
- `notes/coa20-NOTES.md:1892` peeked

**coa21**
- `notes/coa21-NOTES.md:6` How this file was made, and what each part of it rests on
- `notes/coa21-NOTES.md:25` Coverage (coa21)
- `notes/coa21-NOTES.md:797` Fork register (coa21)
- `notes/coa21-NOTES.md:993` Jural relations (coa21)
- `notes/coa21-NOTES.md:1079` Marginal readings for a lawyer (coa21)
- `notes/coa21-NOTES.md:1155` Seams (coa21)
- `notes/coa21-NOTES.md:1304` The seat layer (coa21)
- `notes/coa21-NOTES.md:1375` What the text turns out to say (numbered findings)
- `notes/coa21-NOTES.md:1395` What the stable binary does not accept
- `notes/coa21-NOTES.md:1419` Regulative rules and their recorded traces (coa21)
- `notes/coa21-NOTES.md:1438` What check.sh prints

**coa22**
- `notes/coa22-NOTES.md:9` Where PLAN.md and the brief differ
- `notes/coa22-NOTES.md:17` Coverage (coa22)
- `notes/coa22-NOTES.md:743` Fork register (coa22)
- `notes/coa22-NOTES.md:940` Jural relations (coa22)
- `notes/coa22-NOTES.md:987` Marginal readings for a lawyer (coa22)
- `notes/coa22-NOTES.md:1011` Seams (coa22)
- `notes/coa22-NOTES.md:1028` Seat questions (coa22)
- `notes/coa22-NOTES.md:1139` Seat audit of 2026-11-12
- `notes/coa22-NOTES.md:1155` Name-test sweep of 2026-11-12
- `notes/coa22-NOTES.md:1173` Findings: what the text turns out to say
- `notes/coa22-NOTES.md:1190` What the stable binary does not accept
- `notes/coa22-NOTES.md:1199` What check.sh prints

**coa23**
- `notes/coa23-NOTES.md:5` Source and what "verified" means here
- `notes/coa23-NOTES.md:9` Seat (coa23)
- `notes/coa23-NOTES.md:21` What is encoded and what is not
- `notes/coa23-NOTES.md:25` Coverage (coa23)
- `notes/coa23-NOTES.md:838` Fork register (coa23)
- `notes/coa23-NOTES.md:907` Jural relations (coa23)
- `notes/coa23-NOTES.md:1247` Marginal readings for a lawyer (coa23)
- `notes/coa23-NOTES.md:1280` Seams (coa23)
- `notes/coa23-NOTES.md:1330` Findings: what the text turns out to say
- `notes/coa23-NOTES.md:1348` What the stable binary does not accept, and what it does (measured on 2026-11-13 with `L4_BIN`, 1.6.110 (main, e51181d, 2026-11-11), and with `L4_MAIN`, 1.6.109)
- `notes/coa23-NOTES.md:1405` What `check.sh` printed
- `notes/coa23-NOTES.md:1453` How the tests were written
- `notes/coa23-NOTES.md:1457` Open questions for a domain expert
- `notes/coa23-NOTES.md:1468` Files
- `notes/coa23-NOTES.md:1472` Copied modules
- `notes/coa23-NOTES.md:1476` Peeked

**coa24**
- `notes/coa24-NOTES.md:7` The source, and what this is not
- `notes/coa24-NOTES.md:13` Seat
- `notes/coa24-NOTES.md:18` Method
- `notes/coa24-NOTES.md:28` Where `PLAN.md` and the brief differ (the brief governs)
- `notes/coa24-NOTES.md:34` Files
- `notes/coa24-NOTES.md:38` Coverage (coa24)
- `notes/coa24-NOTES.md:764` Fork register (coa24)
- `notes/coa24-NOTES.md:797` Jural relations (coa24)
- `notes/coa24-NOTES.md:922` Marginal readings for a lawyer (coa24)
- `notes/coa24-NOTES.md:1182` Seat questions (coa24)
- `notes/coa24-NOTES.md:1281` Seams (coa24)
- `notes/coa24-NOTES.md:1315` Findings: what the text turns out to say
- `notes/coa24-NOTES.md:1334` What the stable binary does not accept (and what it accepts that the brief forbids)
- `notes/coa24-NOTES.md:1350` Rulings applied (coa24)
- `notes/coa24-NOTES.md:1381` What `check.sh` prints
- `notes/coa24-NOTES.md:1466` What the text does not answer, and what to do before relying on this

**coa25**
- `notes/coa25-NOTES.md:5` Source and what "verified" means here
- `notes/coa25-NOTES.md:9` Seat
- `notes/coa25-NOTES.md:19` What is encoded and what is not
- `notes/coa25-NOTES.md:37` Coverage (coa25)
- `notes/coa25-NOTES.md:319` Fork register (coa25)
- `notes/coa25-NOTES.md:377` Jural relations (coa25)
- `notes/coa25-NOTES.md:655` Marginal readings for a lawyer (coa25)
- `notes/coa25-NOTES.md:680` Seams (coa25)
- `notes/coa25-NOTES.md:701` Findings: what the text turns out to say
- `notes/coa25-NOTES.md:718` What the stable binary does not accept, and what it does (coa25)
- `notes/coa25-NOTES.md:728` What `check.sh` printed
- `notes/coa25-NOTES.md:765` Open questions for a domain expert
- `notes/coa25-NOTES.md:776` Copied modules

**coa26**
- `notes/coa26-NOTES.md:8` What is encoded, and what is not
- `notes/coa26-NOTES.md:14` Seat
- `notes/coa26-NOTES.md:23` Files
- `notes/coa26-NOTES.md:41` How the L4 was made (method)
- `notes/coa26-NOTES.md:49` Coverage (coa26)
- `notes/coa26-NOTES.md:564` Fork register (coa26)
- `notes/coa26-NOTES.md:621` Jural relations (coa26)
- `notes/coa26-NOTES.md:717` Marginal readings for a lawyer (coa26)
- `notes/coa26-NOTES.md:747` Seams (coa26)
- `notes/coa26-NOTES.md:769` What the text turns out to say (findings)
- `notes/coa26-NOTES.md:791` What the stable binary does not accept (or reads in a way that surprised)
- `notes/coa26-NOTES.md:806` What `check.sh` prints
- `notes/coa26-NOTES.md:840` Independence

**coa27**
- `notes/coa27-NOTES.md:5` What is encoded and what is not
- `notes/coa27-NOTES.md:15` Seat
- `notes/coa27-NOTES.md:86` Coverage (coa27)
- `notes/coa27-NOTES.md:882` Fork register (coa27)
- `notes/coa27-NOTES.md:967` Jural relations (coa27)
- `notes/coa27-NOTES.md:1136` Marginal readings for a lawyer (coa27)
- `notes/coa27-NOTES.md:1220` Seams (coa27)
- `notes/coa27-NOTES.md:1240` What the text turns out to say
- `notes/coa27-NOTES.md:1254` What the stable binary does not accept
- `notes/coa27-NOTES.md:1260` What check.sh prints
- `notes/coa27-NOTES.md:1293` Files

**coa28**
- `notes/coa28-NOTES.md:11` What is in this folder (coa28)
- `notes/coa28-NOTES.md:34` Coverage (coa28)
- `notes/coa28-NOTES.md:819` Fork register (coa28)
- `notes/coa28-NOTES.md:1005` Jural relations (coa28)
- `notes/coa28-NOTES.md:1081` Marginal readings for a lawyer (coa28)
- `notes/coa28-NOTES.md:1409` Seams (coa28)
- `notes/coa28-NOTES.md:1467` Findings: what the text turns out to say (coa28)
- `notes/coa28-NOTES.md:1523` What the stable binary does not accept (coa28)
- `notes/coa28-NOTES.md:1556` Decisions (coa28)
- `notes/coa28-NOTES.md:1587` Seat questions (coa28)
- `notes/coa28-NOTES.md:1690` What `check.sh` prints (coa28)

**coa29**
- `notes/coa29-NOTES.md:8` Source and what "verified" means here
- `notes/coa29-NOTES.md:21` Seat
- `notes/coa29-NOTES.md:31` What is encoded and what is not
- `notes/coa29-NOTES.md:39` Files
- `notes/coa29-NOTES.md:48` Coverage (coa29)
- `notes/coa29-NOTES.md:1108` Fork register (coa29)
- `notes/coa29-NOTES.md:1177` Marginal readings for a lawyer (coa29)
- `notes/coa29-NOTES.md:1222` Jural relations (coa29)
- `notes/coa29-NOTES.md:1285` Seams (coa29)
- `notes/coa29-NOTES.md:1318` What the text turns out to say (numbered findings)
- `notes/coa29-NOTES.md:1335` What the stable binary does not accept, and what it does
- `notes/coa29-NOTES.md:1355` What `check.sh` printed
- `notes/coa29-NOTES.md:1395` Open questions for a domain expert
- `notes/coa29-NOTES.md:1408` Copied modules

**coa30**
- `notes/coa30-NOTES.md:7` Source and what "verified" means here
- `notes/coa30-NOTES.md:11` Seat
- `notes/coa30-NOTES.md:91` What is encoded and what is not
- `notes/coa30-NOTES.md:97` Rulings applied (recorded word for word)
- `notes/coa30-NOTES.md:107` Tests (coa30): what each kind of assertion proves
- `notes/coa30-NOTES.md:111` Coverage (coa30)
- `notes/coa30-NOTES.md:949` Fork register (coa30)
- `notes/coa30-NOTES.md:1085` Jural relations (coa30)
- `notes/coa30-NOTES.md:1598` Marginal readings for a lawyer (coa30)
- `notes/coa30-NOTES.md:1708` Seams (coa30)
- `notes/coa30-NOTES.md:1735` What the text turns out to say (numbered findings)
- `notes/coa30-NOTES.md:1755` Regulative rules: traces (coa30-tests-regulative.l4)
- `notes/coa30-NOTES.md:1781` What the stable binary does not accept, and what it does
- `notes/coa30-NOTES.md:1791` What `check.sh` prints
- `notes/coa30-NOTES.md:1824` Open questions for a domain expert
- `notes/coa30-NOTES.md:1834` Copied modules
- `notes/coa30-NOTES.md:1838` Peeked

## What would need doing before the encoding is worth relying on

- A lawyer reads each part's coverage table, forks and marginal readings against the official text (this is a converter's rendering).
- The `FALSE` and `NOTHING` readings the parts flag for a lawyer, and the listed groups above, are decided.
- The seams are wired or kept as questions, and the requests in `NEEDS-CORE.md` are taken into the core or refused.
- The prescribed figures and rates that the text leaves to regulations or orders are supplied as inputs; this encoding does not hold them unless a part's notes say so.

## Source not official

The quoted text is a plain-text rendering of the Act as deposited in `../../registers/source-bundle/`; it is not the official text. See 'The source' above and `SOURCE-LICENSE.md`.
