# The 2023 Merger Guidelines (U.S. DOJ and FTC): notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
The Guidelines say of themselves that, "as a statement of the Agencies' law enforcement procedures and practices", they "create no independent rights or obligations" and "do not limit the discretion of the Agencies" (`[pdf page 5 of 51]`).
Every result in this encoding says what the Agencies presume, infer, examine, credit or accept.
No result says that a merger is lawful or unlawful, and none should be read as what a court must hold.

**Seat:** the merging firms, and anyone advising them or affected by the merger, asking what the Agencies will presume, examine or credit. The Agencies are never the seat; their positions appear only as what they mean for the merger.

## 1. Status and what was checked

Status: `draft`, version 0.1.0, written 2026-11-25 by a single builder session from the deposited text alone.
No domain expert has read it.
An independent test pass has been run (section 10), and an adversarial review (section 11). Every finding of the review has been dealt with after the parent session's rulings of 2026-11-25, and `tests-independent.l4` carries a signature-only patch made at its ruling (section 10).
Every expected value in the test modules was written from the text, or from a fixture built from the text's own definitions and stated as such in its comment.
One expected value was wrong when first written, and the fault was mine, not the encoding's: a hand sum of a pre-merger HHI (2,850 for 2,950), corrected before commit.
No assertion has been changed to match the code.
The type changes of section 11, finding 5 wrapped some of my expected values in `JUST`; none changed value.
Two of my expectations changed on review because the reading changed, and each was re-derived from the text (section 11, findings 1 and 2): the rejected offers of 150 and 90 in `mg-tests-boundaries.l4` were `NOTHING` and are now not accepted (fork FF-2); the rejected offer of 120 that would take a division's assets out of the market in `mg-tests.l4` barred the claim and now does not (fork FD-1).
A review before the first hand-back found one test too weak to catch its rule: the failing division test for a rejected offer asserted only that the answer was not `NOTHING`. It now asserts the whole finding.
Measured 2026-11-25 on scratch copies: with "keeps the assets in the market" removed from the division's bar, `mg-tests.l4` fails one assertion (the one after "Footnote 62's bar applied to a division only for an offer keeping the assets"); with the failing firm reading made to answer `NOTHING` whenever any offer at or below liquidation value is received, `mg-tests.l4` and `mg-tests-boundaries.l4` fail two each; with failed attempts at coordination drawing Guideline 3's inference, `mg-tests.l4` fails one.

The source is `registers/source-bundle/2023-merger-guidelines.txt`, a `pdftotext` extraction of the justice.gov PDF (sha256 in the `.meta.json` beside it).
Page markers `[pdf page N of 51]` are the PDF's page index, not the printed page numbers.
One cross-reference has been checked against the PDF itself (finding 1); no other quotation has.

## 2. Target and checks

Target compiler: `main`, the stable 1.6.112.
The modules use only syntax that build reads; there is no `REFUSE`, so an answer the text does not give is `NOTHING` from a `MAYBE`.

`L4=<unstable l4> L4_MAIN=<main l4, 1.6.112> ./check.sh`, run 2026-11-25, exit 0:

```
unstable: unstable-20261125-a50cbd0 (unstable, a50cbd0, 2026-11-25)
main:     1.6.112 (main, e4f4bf3, 2026-11-18)
module                     unstable err/sat/fail/ref  main err/sat/fail/ref      expected sat/fail
mg-concentration.l4        0/0/0/0                    0/0/0/0                    0/0
mg-frameworks.l4           0/0/0/0                    0/0/0/0                    0/0
mg-nouns.l4                0/0/0/0                    0/0/0/0                    0/0
mg-rebuttal.l4             0/0/0/0                    0/0/0/0                    0/0
mg-test-fixtures.l4        0/0/0/0                    0/0/0/0                    0/0
mg-tests-boundaries.l4     0/155/0/0                  0/155/0/0                  155/0
mg-tests-red.l4            19/0/19/0                  19/0/19/0                  0/19
mg-tests.l4                0/159/0/0                  0/159/0/0                  159/0
mg-tools.l4                0/0/0/0                    0/0/0/0                    0/0
tests-independent.l4       0/291/0/0                  0/291/0/0                  291/0
assertions satisfied: unstable 605, main 605
check.sh: all passed
```

The stable `l4 run` exits 0 even when an assertion fails, so `check.sh` counts diagnostics, not exit codes.
It requires, per module, the expected number of satisfied and failed assertions on both builds, and for the red module that every error is one of its failures.

The unstable build caught two precedence traps that the stable build accepts silently: `NOT (a) OR b` written on one line reads as `NOT (a OR b)`.
Measured 2026-11-25 with a three-line probe: the stable 1.6.112 fails `#ASSERT NOT (FALSE) OR TRUE` and passes `#ASSERT (NOT (FALSE)) OR TRUE`, and the unstable build rejects the first with `check/not-reaches-connective`.
Both were bracketed before commit (`mg-rebuttal.l4`, the monopoly clause of 3.3; `mg-tools.l4`, the critical loss guard).
A stable-only check would not have found them.

## 3. Scope

Encoded: the structural presumption of Guideline 1 and its arithmetic; the tests and factor lists of Guidelines 2 to 11; the rebuttal frameworks of section 3 (failing firm, failing division, entry and repositioning, efficiencies, and footnote 31's double marginalization); and the computations of section 4 (diversion and its ratios, the HMT and the SSNIP, recapture, critical loss, targeting, geographic shares, participants, and shares as Guideline 1's input).

Where the text lists indicators or considerations and gives no rule for combining them ("for example", "the Agencies consider"), the encoding takes the list the caller says the evidence shows and reports it back unchanged.
Nothing here weighs indicators against each other, and a reader should not take the presence of a list in a result as a conclusion.
A BOOLEAN input named for an evidential finding ("the evidence demonstrates substantial competition between the merging parties") is the caller's finding, not something the encoding decides.

Not encoded: the discussion of evidence in section 4 (sources, the generally applicable considerations, bargaining, capacity, innovation, and the specific market settings other than targeting and geography); remedies, which footnote 8 puts outside the Guidelines' scope; and the statutes themselves.

Which results refuse an impossible input with `NOTHING`, as the code stands at this commit:

- `the Agencies' reading under Guideline 1 of`, and `Guideline 1 applied to the whole series`: shares that are negative, over 100, or do not sum to exactly 100, an empty market, or no party (fork G1-2).
- `the Agencies' reading under Guideline 3 of` and `the HHI limb of the presumption is met by`: a post-merger HHI outside 0 to 10,000, a negative change, or a change above the post-merger HHI (which would make the pre-merger HHI negative).
- `the share limb of the presumption is met by`: a merged share outside 0 to 100, or a change below 0 or over 10,000; `the Guideline 1 presumption on the metrics`: any impossible HHI, change or share, as for the limbs; `the concentration band of an HHI of`: an HHI outside 0 to 10,000.
- `the Agencies' reading under Guideline 4 of`: an HHI of the market entered outside 0 to 10,000.
- `the Agencies' reading under Guideline 5 of`: a foreclosure share outside 0 to 100.
- `the offer is a reasonable alternative offer, by footnote 62`, and the failing firm and failing division readings: a negative price or liquidation value.
- `the Agencies' reading of the entry claim`: a negative time.
- `the diversion ratio of` and `the aggregate diversion ratio of`: no units lost, negative units diverted, or more units diverted than lost.
- `the upward pricing pressure indicator of`: no revenues lost, negative units, more units diverted than lost, or a negative price or incremental cost.
- `the SSNIP on a price of`: a negative price, or a SSNIP of zero or less.
- `the critical loss, in units, of`: negative units or cost, a price or increase of zero or less, or a cost above the price.
- `the HMT answer for`: an empty candidate market.
- `the seller's share of the geographic market, in percent` and `the market shares on the measure`: a negative amount, or a total of zero.

The limbs, the presumption on the metrics and the Guideline 3 reading check each number's own range, not that the numbers could come from one market together.
A merged share of 10 cannot give a change of 101 (the change is less than the square of the merged share), yet `the Guideline 1 presumption on the metrics` presumes on 1,801, 101 and 10, which `tests-independent.l4` line 202 asserts as a test of the HHI limb on its own numbers.
`the Agencies' reading under Guideline 1 of` computes the metrics from the shares, so there they always agree.
The number helpers and predicates compute on whatever they are given, impossible numbers included, and only the results above guard: `the HHI of the shares`, `the change in HHI from merging firms with shares` (2ab), the pre-merger, post-merger and merged-share helpers, `the value of diverted sales of`, `the margin on incremental units of`, `the implicit price of the pipeline's service`, `the SSNIP percentage of`, `what footnote 30 says of a foreclosure share of`, the threshold predicates of Guidelines 1, 3 and 4 (`highly concentrated, by an HHI of`, `the market is presumptively susceptible to coordination, under 2.3.A`, `the market entered is concentrated, for Guideline 4` and the like), and the comparisons of recapture and critical loss.
`mg-tests-boundaries.l4` pins two of them on impossible input (a value of diverted sales on -30 units; a margin on an incremental revenue of -10) so that this paragraph stays true.

Number conventions: shares and percentages are NUMBER in percent points (30 means 30 percent); HHI is on the 0 to 10,000 scale; the diversion ratio and the price increase of a critical loss are fractions (0.3, 0.05), because the text defines them as fractions.
Arithmetic is exact: L4 keeps rationals, so 10,000/6 is not 1,666.67.

## 4. Modules

| module | what it holds | assertions (both builds) |
| --- | --- | --- |
| `mg-nouns.l4` | types only, in the Guidelines' order | 0 |
| `mg-concentration.l4` | 2.1, Guideline 1: HHI, change, merged share, the two limbs, the presumption, footnote 15's bands | 0 |
| `mg-frameworks.l4` | 2.2 to 2.11, Guidelines 2 to 11 | 0 |
| `mg-rebuttal.l4` | 3.1 to 3.3, footnotes 31, 62, 64, 65, 70, 71 | 0 |
| `mg-tools.l4` | 4.2.B, 4.3, 4.3.A to 4.3.D.2, 4.4.A, 4.4.B, footnotes 72, 84, 85 | 0 |
| `mg-test-fixtures.l4` | builders for test inputs, and readers of a Guideline 3 finding; not rules of the Guidelines | 0 |
| `mg-tests.l4` | tests from the text | 159 satisfied |
| `mg-tests-boundaries.l4` | both sides of every threshold, impossible inputs, properties | 155 satisfied |
| `mg-tests-red.l4` | positive controls, each written wrong | 19 failed, as required |
| `tests-independent.l4` | the independent test pass (section 10); its signatures patched by this builder, no expected value | 291 satisfied |

The positive controls each state a plausible wrong reading and must fail: the rounded 1,667 as the exact HHI; 1,800 as highly concentrated; a change of 100 as significant; a share of 30 as over thirty percent; (a + b)² as the change; shares summing to 99 as readable; 1,000 as concentrated; footnote 30's inference at exactly 50; footnote 37's routing reversed; an offer at liquidation value as reasonable; a rejected reasonable offer not barring the claim; entry at the moment of the effect as timely; entry depending on lessening elsewhere as sufficient; efficiencies with a contractual alternative as cognizable; the diversion ratio as a percentage; the HMT met with no SSNIPT; the SSNIP on 200 as 5; recapture gains equal to the losses as profitable; idle capacity alone as a rapid entrant.

## 5. Coverage table

Every section, subsection, lettered and numbered item, and every footnote of the text.
The text has no numbered Examples.
Dispositions: `encoded`; `encoded (list)`, a typed list the caller supplies and the result reports, with no weighing; `inert`, framing or explanation that states no test; `out-of-scope`; `deferred`.

| part | `[pdf page]` | disposition | where, or why |
| --- | --- | --- | --- |
| 1 Overview: purpose, Clayton Act s 7, how the Guidelines are used | 2-3 | inert | framing |
| 1 Overview: the summary of Guideline 3 ("will infer" / "investigate") | 4 | encoded | `the Agencies' reading under Guideline 3 of`; fork G3-1 |
| 1 Overview: the other ten summaries | 3-4 | inert | each restated and encoded under its own section |
| unnumbered, after the summaries: "consolidates, revises, and replaces" | 5 | inert | recorded in section 8 |
| unnumbered: "create no independent rights or obligations" | 5 | inert | reflected in every result type and in this file's label |
| 2 Applying the Merger Guidelines (introduction) | 6 | inert | framing |
| 2.1 Guideline 1: HHI, more than 100, over 30 percent, the table | 6-7 | encoded | `mg-concentration.l4`; forks G1-1 to G1-4, G1-6 |
| 2.1: rebuttable; "the higher ... the stronger the evidence needed" | 7 | encoded | the finding reports the metrics; no weighing |
| 2.2 Guideline 2 | 7-8 | encoded | `the Agencies' reading under Guideline 2 of` |
| 2.2 indicators (strategic deliberations, prior events, customer substitution, impact on rivals, and the rest) | 8-9 | encoded (list) | `Guideline 2 indicator` |
| 2.3 Guideline 3 | 9 | encoded | `mg-frameworks.l4` |
| 2.3.A Primary Factors (three) | 9-10 | encoded | `the Guideline 3 primary factors in`; fork G3-4 |
| 2.3.B Secondary Factors | 10-11 | encoded (list) | `Guideline 3 secondary factor` |
| 2.3.B competitive responses, items (1) to (5) | 10 | encoded (list) | `Factor increasing strong or rapid responses` |
| 2.4 Guideline 4 | 11-12 | encoded | `the Agencies' reading under Guideline 4 of` |
| 2.4.A Actual Potential Competition, elements (1) and (2) | 12 | encoded | fork G4-2 for the high-concentration suggestion |
| 2.4.A evidence of a reasonable probability of entry | 12 | encoded (list) | `Evidence of a reasonable probability of entry` |
| 2.4.B Perceived Potential Competition | 13 | encoded | `perceived potential competition: the elements of 2.4.B are met` |
| 2.4.B evidence of a likely influence | 13 | encoded (list) | `Evidence of a likely influence` |
| 2.4.C Distinguishing Potential Entry from Entry as Rebuttal | 13-14 | inert | explains that the 3.2 standard differs from Guideline 4's; states no test of its own |
| 2.5 Guideline 5 | 14 | encoded | `the Agencies' reading under Guideline 5 of` |
| 2.5.A The Risk that the Merged Firm May Limit Access (ability and incentive) | 14-15 | encoded | concern (A) |
| 2.5.A.1 considerations 1 to 4, and those that follow | 15-16 | encoded (list) | `Guideline 5 consideration` |
| 2.5.A.2 Structure of the Related Market | 16-17 | encoded | `market structure shows the merged firm's ability ...`; forks G5-1, G5-2 |
| 2.5.A.2 nature and purpose; trend toward vertical integration | 17 | encoded (list) | `Guideline 5 consideration` |
| 2.5.B Visibility into Rivals' Competitively Sensitive Information | 18 | encoded | concern (B) |
| 2.5.C Limiting Rivals' Access and Creating Barriers to Entry | 18-19 | encoded | concern (C); fork G5-3 |
| 2.6 Guideline 6 | 19-20 | encoded | `the Agencies' reading under Guideline 6 of`; fork G6-1 |
| 2.6.A Entrenching a Dominant Position | 20-22 | encoded (list) | `Way of entrenching a dominant position` |
| 2.6.B Extending a Dominant Position into Another Market | 22 | encoded (list) | `Way of extending a dominant position` |
| 2.7 Guideline 7: the four trends | 23-24 | encoded | `what Guideline 7 says the trend does` |
| 2.8 Guideline 8 | 24 | encoded | `how Guideline 8 examines the series`; `Guideline 1 applied to the whole series`, fork G8-1 |
| 2.9 Guideline 9: three kinds of platform competition | 24-27 | encoded | `the platform competition Guideline 9 examines`; fork G9-1 |
| 2.9 scenarios A to D | 26 | encoded | `Platform merger` |
| 2.9 a market around one side; both sides only for a transaction platform | 25 | encoded | `the Agencies' reading under Guideline 9 of` |
| 2.10 Guideline 10: effects on workers; benefits in another market not saving harm | 27-28 | encoded | fork G10-1 |
| 2.10: concentration concerns "may be lower in labor markets" | 28 | inert | no figure given; open question 7 |
| 2.11 Guideline 11: partial ownership, the three effects | 29-30 | encoded (list) | `the Agencies' reading under Guideline 11 of`: the kinds and effects are reported; Guideline 11 has no test of its own and sends the analysis to Guidelines 1 to 6 |
| after 2.11: mechanisms A, B and C "not covered above" | 30 | inert | examples of past cases, no test |
| after 2.11: rebuttal evidence is examined under section 3 | 30 | inert | the rebuttal is section 3 |
| 3 Rebuttal Evidence (introduction) | 31 | inert | framing |
| 3.1 Failing Firms, requirements A, B and C | 31-32 | encoded | `the Agencies' reading of the failing firm claim`; forks FF-1 to FF-3 |
| 3.2 Entry and Repositioning: timeliness, likelihood, sufficiency | 32-33 | encoded | `the Agencies' reading of the entry claim`; forks EN-1, EN-2 |
| 3.3 Procompetitive Efficiencies: the four criteria | 33-34 | encoded | `the Agencies' reading of the efficiencies claim`; fork EF-1 |
| 3.3: nature, magnitude and likelihood; the monopoly clause; vague claims; benefits outside the market | 33-34 | encoded | as above |
| 4 Analytical, Economic, and Evidentiary Tools (introduction) | 35 | inert | framing |
| 4.1 Sources of Evidence | 35-36 | inert | describes evidence; no test |
| 4.2 Evaluating Competition Among Firms (introduction) | 36 | inert | framing |
| 4.2.A Generally Applicable Considerations | 36-37 | inert | describes evidence and models; no test |
| 4.2.B Considerations When Terms Are Set by Firms | 38 | encoded | diversion ratio, aggregate diversion ratio, value of diverted sales, upward pricing pressure indicator |
| 4.2.C Bargaining or Auctions | 38-39 | inert | describes evidence; no test |
| 4.2.D Capacity and Output | 39 | inert | describes evidence; no test |
| 4.2.E Innovation and Product Variety | 40 | inert | describes evidence; no test |
| 4.3 Market Definition (introduction) | 40-41 | inert | framing |
| 4.3 tools A to D | 41-42 | encoded | `a relevant antitrust market is identified, by the tools of 4.3` |
| 4.3 C practical indicia | 42 | inert | typed as `Practical indicium` for a caller, but no rule reads it ("Various practical indicia may identify a relevant market in different settings") |
| 4.3.A The Hypothetical Monopolist Test | 42-43 | encoded | `the HMT answer for` |
| 4.3.B Implementing the HMT: dimensions, input and labor, geography, negotiations, benchmark | 43 | inert | describes how the test is framed; no further test |
| 4.3.B Magnitude of the SSNIPT; the pipeline's implicit price | 44 | encoded | `the SSNIP on a price of`; `the implicit price of the pipeline's service` |
| 4.3.C recapture | 44 | encoded | `the price increase is profitable, by recapture` |
| 4.3.C critical loss | 44-45 | encoded | `the critical loss, in units, of`; fork TL-1 |
| 4.3.C consistency of the predicted loss with margins | 45 | encoded, in part | the margin property is tested; the consistency requirement is inert |
| 4.3.D Market Definition in Certain Specific Settings (introduction) | 45 | inert | framing |
| 4.3.D.1 Targeted Trading Partners | 45-46 | encoded | `targeting is feasible, so a market around the targeted customers may be identified` |
| 4.3.D.2 Geographic Markets (introduction) | 46 | inert | factors limiting geography; no test |
| 4.3.D.2.a based on the locations of suppliers | 46 | encoded | `the seller's share of the geographic market, in percent` |
| 4.3.D.2.b based on targeting of customers by location | 47 | encoded | as above |
| 4.3.D.3 Supplier Responses | 47 | inert | says where supplier responses go; no test |
| 4.3.D.4 Cluster Markets | 47-48 | inert | permits aggregation; no test |
| 4.3.D.5 Bundled Product Markets | 48 | inert | no test |
| 4.3.D.6 One-Stop Shop Markets | 48 | inert | no test |
| 4.3.D.7 Market Definition When There is Harm to Innovation | 49 | inert | no test |
| 4.3.D.8 Input Markets and Labor Markets | 49 | inert | applies the same tools; no further test |
| 4.4 Calculating Market Shares and Concentration (introduction, three considerations) | 49-50 | inert | when structural measures are probative; no test |
| 4.4.A Market Participants | 50-51 | encoded | `the firm's participation in the relevant market` |
| 4.4.B Market Shares | 51 | encoded | `the market shares on the measure`, whose result is Guideline 1's input |
| 4.4.B the listed metrics | 51 | inert | typed as `Measure of market shares` for a caller, but no rule reads it: the choice of metric is the caller's, and the arithmetic is the same for each |
| fn 13 (five and six equal firms) | 6 | encoded | tested; fork G1-4 |
| fn 14 (2ab) | 7 | encoded | tested |
| fn 15 (history of the thresholds; the 1982 bands) | 7 | encoded | `the concentration band of an HHI of`; fork G1-5; history in section 8 |
| fn 21 (concentrated means HHI over 1,000) | 11 | encoded | Guideline 4 |
| fn 23 (a market not yet commercialized) | 12 | encoded | `a future market not yet commercialized` |
| fn 30 (over 50 percent of the related market) | 17 | encoded | `what footnote 30 says of a foreclosure share of` |
| fn 31 (double marginalization) | 17 | encoded | `the Agencies' reading of the double marginalization claim`; fork EDM-1 |
| fn 37 (nascent threats acquired by non-dominant firms) | 21 | encoded | `Where a nascent threat is assessed` |
| fn 47 (transaction platforms) | 25 | encoded | Guideline 9 |
| fn 62 (reasonable alternative offers; liquidation value; the bar on a rejected offer) | 31-32 | encoded | forks FF-1, FF-2 |
| fn 64 (failing divisions) | 32 | encoded | `the Agencies' reading of the failing division claim`; fork FD-1 |
| fn 65 (repositioning) | 32 | encoded | `the supply response is a cognizable rebuttal` |
| fn 70 (contracts and merger specificity) | 33 | encoded | `the efficiencies are merger-specific` |
| fn 71 (decrease in competition in a separate market) | 34 | encoded | `the efficiencies are not anticompetitive` |
| fn 72 (margin on incremental units) | 37 | encoded | `the margin on incremental units of` |
| fn 84 (five percent is not a threshold of harm) | 44 | encoded | the HMT answer names itself "not a finding of harm"; nothing else reads the SSNIP |
| fn 85 (recapture rate is the aggregate diversion ratio) | 45 | encoded | tested with `the aggregate diversion ratio of` |
| fn 88 (only customer locations inside the region) | 47 | encoded | each `Sale` carries its own customer location |
| fn 12 (number of significant competitors) | 6 | inert | an alternative measure with no threshold |
| fn 16 (Philadelphia National Bank, 30 percent) | 7 | inert | the citation for the share limb, which is encoded from the text |
| fn 51 (wages relative to the counterfactual) | 28 | inert | explains the effects; the caller's finding |
| fn 55 (a 20 percent investment) | 29 | inert | a case parenthetical, not a threshold; nothing uses 20 |
| fn 82 (hypothetical cartel) | 43 | inert | an alternative framing of the HMT with no test of its own |
| fn 87, fn 90 (hypothetical cartel across geographies) | 46, 47 | inert | each cites "Section 4.3.A, n.81", which the PDF shows is the Guidelines' own error for n.82 (finding 1) |
| fns 2, 8, 10, 11, 17, 27, 36, 42, 45, 46, 48, 52, 69, 73, 83, 86, 89, 92 | various | inert | explanation, definitions or scope (fn 8: remedies are outside the Guidelines); each read, none states a test |
| fns 1, 3-7, 9, 18-20, 22, 24-26, 28, 29, 32-35, 38-41, 43, 44, 49, 50, 53, 54, 56-61, 63, 66-68, 74-81, 91 | various | inert | citations of statutes, cases and reports |

Counts: 103 rows; `encoded` 54, `encoded, in part` 1, `encoded (list)` 10, `inert` 38, `out-of-scope` 0, `deferred` 0.
Of the 103 rows, 26 are footnotes: 18 encoded, and 8 inert, of which the last two rows group 18 and 49 footnotes, so all 92 footnotes appear.
Counted from this file with `awk` over the table's disposition column, 2026-11-25.

## 6. Fork register

Every reading below was taken by this builder, assumed and not ruled, except where a row says the parent session ruled it on 2026-11-25. No domain expert has ruled any of them.

| fork | text | readings | taken |
| --- | --- | --- | --- |
| G1-1 | 2.1 "a merger that creates a firm with a share over thirty percent"; fn 14 "shares a and b" | (a) the merged share is the sum of the parties' pre-merger shares; (b) a predicted post-merger share | (a); it is what makes fn 14's 2ab the change. For three or more parties the change is post minus pre, which is 2(ab + bc + ca) |
| G1-2 | 2.1 "the sum of the squares of the market shares" | shares that do not sum to 100 are (a) impossible, (b) completed by an unlisted fringe, (c) normalised, (d) allowed a rounding tolerance | (a): every firm listed, each 0 to 100, summing to exactly 100, at least one party, else `NOTHING`. Fn 13's own 16.67 x 6 = 100.02 is therefore `NOTHING` |
| G1-3 | 2.1 "creates or further consolidates a highly concentrated market" | (a) post-merger HHI over 1,800; (b) pre-merger over 1,800 for "further consolidates" | (a), as the table states it |
| G1-4 | fn 13 "six equal firms is 1,667" | (a) the exact 10,000/6; (b) 1,667 | (a); 1,667 is the text's rounding. Nothing turns on it at 1,800 |
| G1-5 | fn 15 "between 1,000 and 1,800 as 'moderately concentrated'"; fn 21 "greater than 1,000" | the band edges | over 1,000 and at most 1,800, so that it meets "greater than 1,800" and fn 21 |
| G1-6 | 1 "a merger between competitors" (`[pdf page 3 of 51]`) | a market in which only one firm is a party (an acquirer from outside it): (a) read, with the change 0; (b) `NOTHING`, Guideline 1 being stated for competitors | (a): the merged share is that party's share, the change is 0, and no presumption arises; tested at shares 50 and 50. The text is silent; the independent test author noted it |
| G3-1 | 1 "A market that is highly concentrated ... the Agencies will infer"; 2.3.A "highly concentrated after a merger that significantly increases concentration" | (a) post over 1,800 alone; (b) post over 1,800 and change over 100 | (b). At post 2,000 and change 50, (a) infers harm and (b) does not; tested |
| G3-2 | 1 names concentration and prior coordination; 2.3.A names three primary factors for "may conclude" | which factors found the inference | concentration (G3-1) or prior coordination found the inference; any of the three founds "may conclude", so the elimination of a maverick alone gives "may conclude" and not the inference |
| G3-3 | 1 "In a market that is not highly concentrated, the Agencies investigate" | not highly concentrated by (a) post HHI alone; (b) G3-1's reading | (a). So at post 2,000 and change 50 the encoding neither infers nor flags an investigation; open question 1 |
| G3-4 | 1 "has seen prior anticompetitive coordination" (`[pdf page 4 of 51]`); 2.3.A "Prior Actual or Attempted Attempts to Coordinate", and failed attempts "suggest that successful coordination was not so difficult as to deter attempts" (`[pdf page 10 of 51]`) | (a) one input for actual or attempted coordination, grounding both the primary factor and the inference; (b) two inputs: actual coordination grounds the inference and the primary factor, attempted coordination the primary factor only | (b), since the 2026-11-25 review (until then (a), which let failed attempts alone draw the inference). Only actual prior coordination grounds section 1's inference; failed attempts alone count only as 2.3.A's primary factor, so they allow "may conclude" and not the inference. Tested both ways, and both together give the factor once |
| G4-1 | fn 21, fn 23 | concentrated | HHI over 1,000, or a future market with few equivalent potential entrants |
| G4-2 | 2.4.A "a reasonable probability of entering a highly concentrated relevant market ... suggests ... unless ... de minimis", and "To supplement the suggestion ... the Agencies will consider projections" (`[pdf page 12 of 51]`) | (a) the suggestion satisfies element (2), unless there is substantial direct evidence of a de minimis effect; (b) the adversarial review's reading: "suggests" and "supplement" make it evidence only, so it is reported as its own field and element (2) stays the caller's finding even when the caller says FALSE | (a), kept by the parent session's ruling of 2026-11-25. The suggestion carries its own stated exception, which the de minimis input is, and the projections "supplement" the suggestion rather than replace it. The two reviewers split: the independent test author reads (a) (`tests-independent.l4` line 411), the refuter (b). That the de minimis input defeats the suggestion is tested in `mg-tests.l4` line 220 and `tests-independent.l4` lines 409 and 412. The suggestion is also reported as its own field. "Highly concentrated" is over 1,800 (Guideline 1); a future market has no HHI, so the suggestion never arises there |
| G5-1 | fn 30 "a share greater than 50% of the related product market"; 2.5.A.2 defines the "foreclosure share" | which share | the foreclosure share, which 2.5.A.2 defines just before the sentence fn 30 annotates |
| G5-2 | fn 30: greater than 50 infers; "less than 50%" may still lessen competition | exactly 50 | neither sentence covers it; a named result says so |
| G5-3 | 2.5.C "may occur irrespective of the merged firm's incentive" | concern (C) needs (a) ability or visibility; (b) ability and incentive | (a) |
| G6-1 | 2.6 "direct evidence or market shares showing durable market power" | a share threshold for dominance | none is given; dominance is the caller's finding |
| G8-1 | 2.8 "collectively under Guidelines 1-6" | how Guideline 1 applies to a series | the firms of the series as the parties to one merger, on the shares before the first acquisition |
| G9-1 | 2.9 scenarios A to D and the paragraphs after | which kinds of platform competition each scenario engages | the mapping in `the platform competition Guideline 9 examines`; scenario B also engages competition on a platform |
| G10-1 | 2.10 "not saved by benefits to competition among sellers"; 3.3 "benefits outside the relevant market" | identity of markets | whether a claimed benefit is in the market where competition may be lessened (`the claimed benefit is in the market where competition may be lessened`), compared by the caller's market name. Nothing is weighed: 3.3 says "possible economies [from a merger] cannot be used as a defense to illegality" (`[pdf page 33 of 51]`). Until the 2026-11-25 review the result was named `the benefit may be weighed against the harm` |
| FF-1 | fn 62 "If a reasonable alternative offer was rejected, the parties cannot claim that the business is failing"; requirement C "offers that pose a less severe danger" | the bar applies to (a) any rejected reasonable offer; (b) only one less dangerous than the merger | (a), as fn 62 is written, so a rejected offer more dangerous than the merger still bars. On fork FF-2's reading (b) a rejected offer at or below liquidation value bars too, and where that changes the answer it is `NOTHING` |
| FF-2 | fn 62 "above the liquidation value ... will be regarded as a reasonable alternative offer"; "Liquidation value is the highest value the assets could command outside the market" | an offer at or below liquidation value is (a) not reasonable; (b) reasonable | both are computed in full. When they give the same accept (or credit) answer, that is the answer; when they differ, `NOTHING`. Counting more offers can only defeat requirement C or condition 2, or add a bar, so two readings cover every way of classifying several such offers. The requirement and bar fields count only offers above liquidation value, and a field says when one at or below it was received. The liquidation value is the caller's figure |
| FF-3 | 3.1 "The Agencies typically look for evidence ..." under requirements A, B and C (`[pdf page 31 of 51]`) | each input is (a) the requirement itself; (b) the caller's finding on the evidence the Agencies look for | (b), and since the 2026-11-25 review the `Failing firm claim` fields are named for it ("the evidence shows that the firm would be unable to meet its financial obligations ...", "the evidence suggests that the firm would be unable to reorganize ...", "the evidence shows good-faith efforts ..."); the requirements are the encoding's conclusions from them |
| FD-1 | fn 64 "reasonable alternative offers that would keep its assets in the relevant market and pose a less severe danger" | fn 62's bar on a rejected reasonable offer applies to a division (a) for any such offer; (b) only for one that would keep the assets in the relevant market | (b), since 2026-11-25's review. Fn 64 asks only for offers that keep the assets in the market, and an offer that would take them out is no alternative to the exit the claim asserts. Fn 62's definition of a reasonable offer (above liquidation value) still applies, and the bar, as in FF-1, does not ask that the offer be less dangerous. Until then (a) was taken |
| EN-1 | 3.2 "replicate the scale, strength, and durability of one of the merging parties" | (a) one party on all three; (b) each dimension against any party | (a); tested with A's scale and strength and B's durability, which is not sufficient |
| EN-2 | 3.2 "before any effect ... may occur" | strict or not; units | strictly before; the two times in one unit the caller chooses |
| EF-1 | 3.3 the four criteria, then "To successfully rebut ..." | which conditions are criteria of cognizability and which of crediting | the four criteria make efficiencies cognizable; vagueness, benefits outside the market, nature-magnitude-likelihood and the monopoly clause are conditions on crediting |
| EDM-1 | fn 31 (a), (b), (c) | which examination decides what | (b) decides merger specificity; (a) and (c) have no stated outcome and are reported together |
| TL-1 | 4.3.C "the number of lost unit sales that would leave profits unchanged" | the formula | breakeven with a constant incremental cost per unit; the text gives none. A negative pre-merger margin is `NOTHING` |
| TL-2 | 4.3.C "exceed"; "less than" | strict or not | strict in both |
| TL-3 | 4.3.B "larger or smaller than five percent" | a SSNIP of zero or less | `NOTHING`: a SSNIP is an increase |

## 7. Findings

1. Footnotes 87 and 90 (`[pdf pages 46 and 47 of 51]`) send the reader to "Section 4.3.A, n.81" for the hypothetical cartel, but n.81 is the Penn State Hershey citation and the hypothetical cartel is n.82 (`[pdf page 43 of 51]`).
   Closed 2026-11-25: checked against the PDF itself (sha256 equal to the bundle's `pdf_sha256`) with `pdftotext -layout`, by the parent session on pdf pages 42 to 44 and by this builder on pages 42 to 47: n.81 is on page 42 and n.82 on page 43, and the "n.81" stands in fns 87 and 90.
   The cross-reference is the Guidelines' own error, not an artefact of the extraction.
2. Footnote 13's own figures for six equal firms (16.67 each) sum to 100.02, so under fork G1-2 the text's illustration is not a market Guideline 1 reads; the exact shares (100/6) give 10,000/6, which rounds to the text's 1,667.
3. Footnote 30 says what a share over 50 percent and a share under 50 percent mean, and nothing of exactly 50.
4. The text has no numbered Examples; its worked figures are in fns 13 and 14 only.
5. The "consolidates, revises, and replaces" sentence is on `[pdf page 5 of 51]`, printed page 4, not page 4 of the PDF.
6. Under forks G3-1 and G3-3, a market already highly concentrated where the merger adds 100 points or fewer gets neither the inference nor the instruction to investigate: the two sentences of section 1 do not between them cover it.

## 8. Withdrawn and superseded guidelines

Not encoded; recorded so that a reader knows what this text displaced and what stands beside it.
Each line says whether it was read at source in this row or only reported to this builder.

- The 2023 text "consolidates, revises, and replaces the various versions of Merger Guidelines previously issued by the Agencies" (`[pdf page 5 of 51]`, printed page 4). Read at source. It does not list them.
- Fn 15 gives the threshold history: the 1982 guidelines first used HHI thresholds (concentrated above 1,000, "moderately concentrated" between 1,000 and 1,800, "highly concentrated" above 1,800, an increase of 100 "significant"); the 1992 and 1997 Horizontal Merger Guidelines (s 1.51) kept them; the 2010 guidelines raised them; the 2023 Guidelines return to the originals. Read at source. The 2010 figures are not in this text and are not stated here.
- 2020 Vertical Merger Guidelines: the FTC withdrew its approval on 15 September 2021. Reported to this builder, not read at source. A DOJ notice of December 2023 on their status was reported as ambiguous; not read.
- 2000 Antitrust Guidelines for Collaborations Among Competitors: withdrawn on 11 December 2024. Reported to this builder from a search summary of an FTC press release that could not be fetched; not read at source. A public inquiry in early 2026 was reported; no replacement was found. Whether the "replaces" sentence above reaches them is open question 11.
- The 2023 Guidelines remain in force: memoranda of the FTC Chair and of the DOJ of 18 February 2025 were reported to this builder, not read. The DOJ index page `https://www.justice.gov/atr/guidelines-and-policy-statements-0` listed them on 2026-11-25 (read by the parent session; `2023-merger-guidelines.meta.json` records the page as "Updated November 17, 2025").

## 9. Open questions for a domain expert

1. Section 1 says the Agencies "will infer" harm in a highly concentrated market, and 2.3.A ties presumptive susceptibility to a merger that "significantly increases concentration". In a market over 1,800 where the merger adds 100 points or fewer, do the Agencies infer harm under Guideline 3? (forks G3-1, G3-3; finding 6)
2. Is footnote 30's "share ... of the related product market" the foreclosure share of 2.5.A.2, and what do the Agencies infer at exactly 50 percent? (G5-1, G5-2)
3. Footnote 62: is an offer at or below liquidation value ever a reasonable alternative offer, and does a rejected reasonable offer bar the claim when it posed no less severe a danger than the merger? (FF-1, FF-2)
4. Do footnote 62's definition and bar apply to a failing division under footnote 64, and does a rejected offer that would take the division's assets out of the market bar the claim? (FD-1)
5. Must sufficient entry replicate one merging party on all three of scale, strength and durability? (EN-1)
6. How do the Agencies apply Guideline 1 "collectively" to a series of acquisitions? (G8-1)
7. Guideline 10 says concentration concerns may arise at a lower level in labor markets. Is there a figure the Agencies use?
8. What evidence or share do the Agencies take as showing a dominant position under Guideline 6? (G6-1)
9. Critical loss: is the constant-cost breakeven the computation the Agencies intend, or one of several? (TL-1)
10. Should Guideline 1 accept shares that sum to 100 only after rounding, as fn 13's do? (G1-2)
11. Which prior guidelines does the 2023 text's "consolidates, revises, and replaces the various versions of Merger Guidelines" reach? It names none, and the status of the 2020 Vertical Merger Guidelines and the 2000 Collaboration Guidelines was only reported to this builder (section 8).
12. Does a reasonable probability of entering a highly concentrated market satisfy element (2) of 2.4.A by itself, unless there is substantial direct evidence of a de minimis effect, or is it a suggestion the Agencies "supplement" with projections, leaving element (2) to the evidence? The encoding keeps the first, by the parent session's ruling; the refuter read the second, and the independent test author the first. (G4-2)
13. Does evidence of failed attempts at coordination ground section 1's inference, which names a market that "has seen prior anticompetitive coordination", or only 2.3.A's primary factor? The encoding takes the second. (G3-4)

## 10. Independent test pass

`tests-independent.l4` was written on 2026-11-25 by a fresh agent, not this builder.
It read the source text first and wrote its expected answers down before opening the encoding; it then took only the encoding's exported names and signatures, and read none of its tests or fixtures (the file's header says so).
It has 291 assertions, in groups each citing the provision and the `[pdf page]` its answers come from; where the text is silent it asserts `NOTHING` or "not JUST TRUE", never a bare FALSE.

On the encoding as first handed back (commit 7ee34b5cf), 290 were satisfied and 1 failed, on both builds (re-measured by this builder on a scratch copy).
The failure, at what is now line 1085 (line 1040 before the signature patch below): footnote 62's test answered `JUST TRUE` for an offer of 10 against a liquidation value of -5, while the failing firm reading answered `NOTHING` for the same input, so the encoding disagreed with itself.
`the offer is a reasonable alternative offer, by footnote 62` now answers `NOTHING` for a negative price or liquidation value (section 11, finding 5).
Now 291 satisfied, 0 failed, on both builds (section 2).

The author retracted one assertion of its own after its first run, and left a comment saying so at lines 849-851: the input at line 852 says both that a contract could achieve the efficiencies and that a contract would not be practical, which contradict each other; it first expected merger-specific, and corrected that to not merger-specific, footnote 70's first sentence answering the input as written.

The author noted five cases where the text is silent and the encoding takes a reading; each is a fork: at a post-merger HHI of 2,000 with a change of 50, neither the inference nor the investigation (G3-1, G3-3, finding 6); the elimination of a maverick alone gives "may conclude" but not the inference (G3-2); a rejected offer more dangerous than the merger still bars (FF-1); concern (C) on the ability to limit access alone (G5-3); a "merger" with one party in the market gives a change of 0 (G1-6).

### 10.1 The signature-only patch (2026-11-25)

This builder patched the file once, in a commit of its own whose subject ends "signature-only: constructors, field names, CONSIDER wrappers; no expected value touched", at the parent session's ruling of 2026-11-25 (option (a)), so that findings 4 to 7 of section 11 could land.
Measured on the patch itself: 19 of the 291 `#ASSERT` lines changed, and for each of them the text after `EQUALS` (where there is one) and every number and `TRUE`/`FALSE` outside backquotes are identical before and after (a script over both versions); the assertion count is still 291.
After it, 291 satisfied and 0 failed on both builds.
The unstable build prints 7 `lint/non-exhaustive-match` warnings for the file, one per wrapper below; they are deliberate.
To see it word by word: `git show --word-diff=plain <that commit> -- tests-independent.l4`.

What was mapped, and why: the file's `ind G3 facts` takes one `prior` coordination input, and the encoding now has two (fork G3-4).
`prior` maps to actual prior coordination, and failed attempts are given as FALSE.
The author's own words read as actual coordination: its comment at line 354 quotes section 1's "has seen prior anticompetitive coordination", its answers note S8 reads that clause as the ground of the inference, and line 358 expects the inference from `prior` alone, which only actual coordination draws.
Its note E2 lists "prior actual or attempted coordination" as one primary factor, and line 352 asserts that factor from `prior`; that holds under either mapping.

Each changed line, by its line number after the patch:

- 119-150 (added): a comment and four wrappers, `ind band of`, `ind presumption on the metrics`, `ind HHI limb`, `ind share limb`, each a `CONSIDER` with only a `WHEN JUST` branch, so a `NOTHING` raises `eval/non-exhaustive-patterns` and cannot satisfy an assertion (measured on both builds before this round, `NOT (...)` included).
- 181-185: `the concentration band of an HHI of` became `ind band of`; HHI and expected band unchanged.
- 202-204 and 206-208: `the Guideline 1 presumption on the metrics` became `ind presumption on the metrics`; the three numbers and the expected `ind PRESUME` or `ind NO PRESUMPTION` unchanged.
- 209-210: `the share limb of the presumption is met by` became `ind share limb`; numbers and `NOT` unchanged.
- 211-212: `the HHI limb of the presumption is met by` became `ind HHI limb`; numbers and `NOT` unchanged.
- 304-306 (added): a comment stating the mapping above.
- 315: the field `firms with a substantial share appear to have coordinated, or attempted to, before` renamed to `... previously engaged in express or tacit coordination to lessen competition`; still `IS prior`.
- 316 (added): `there is evidence of failed attempts at coordination in the relevant market IS FALSE`, the new field.
- 321, 328, 335 (added): a comment on each Guideline 3 reader.
- 322, 329, 336: each reader's parameter changed from `f IS A Guideline 3 finding` to `m IS A MAYBE Guideline 3 finding`.
- 324-326, 331-333, 338-340: each reader's body changed from `f's <field>` to `CONSIDER m WHEN JUST f THEN f's <field>`, the same field, no `NOTHING` branch.
- 553: `magnified concerns under Guideline 5` renamed to `concerns under Guideline 5 that the trend could magnify`; same trend, same `elem`.
- 554: `exacerbated problems under Guidelines 1 to 6` renamed to `problems under Guidelines 1 to 6 that the trend can exacerbate`; same trend, same `elem`.
- 596-597: `the benefit may be weighed against the harm` renamed to `the claimed benefit is in the market where competition may be lessened`; the market names and `NOT` unchanged.
- 635: field `the firm would be unable to meet its financial obligations in the near future` renamed to `the evidence shows that the firm would be unable to ...`; still `IS unable`.
- 637: field `the firm would be unable to reorganize successfully under Chapter 11` renamed to `the evidence suggests that the firm would be unable to ...`; still `IS noreorg`.
- 638: field `good-faith efforts were made to elicit reasonable alternative offers, before the claim` renamed to `the evidence shows good-faith efforts, before the claim, to elicit reasonable alternative offers`; still `IS efforts`.

Nothing else in the file changed.

## 11. Adversarial review

A second fresh agent tried to refute the encoding against the text; the parent session confirmed each of its eight findings against the source and relayed them.
This section relies on the parent session's statement of the refuter's findings: this builder has not read the refuter's own report.
What was done with each, after the parent session's rulings of 2026-11-25:

1. **The failing firm and division readings answered `NOTHING` where the text answers** (a claim failing requirement A or B, or a division whose negative cash flow is justified, is not accepted on either reading of an offer at or below liquidation value). Fixed: both readings of fork FF-2 are computed, and `NOTHING` is returned only when they differ. `mg-tests-boundaries.l4`'s rejected offers of 150 and 90, which asserted `NOTHING`, are now not accepted: the 150 bars the claim on both readings. New tests cover requirement A failing and a justified cash flow.
2. **FD-1: footnote 64 counts only offers that would keep the assets in the market.** Fixed: the bar applies to a division only for a rejected offer above liquidation value that would keep the assets in the relevant market. `mg-tests.l4`'s rejected offer of 120 taking the assets out of the market now leaves the claim credited, and a new test shows the same offer keeping the assets bars it. Fork FD-1 records both readings.
3. **G4-2: the high-concentration suggestion overrode the caller's own FALSE on element (2).** Kept, with reason, by the parent session's ruling; behaviour unchanged. Two reviewers split: the independent test author reads the text as the encoding does (`tests-independent.l4` line 411), the refuter does not. Reading (a) is kept because the suggestion carries its own stated exception, substantial direct evidence of a de minimis effect, which is an input here, and because the projections "supplement" the suggestion rather than replace it (`[pdf page 12 of 51]`). Fork G4-2 and open question 12 record the refuter's reading as the alternative.
4. **Prior coordination conflates actual and attempted coordination.** Fixed: `Guideline 3 facts` has two inputs (fork G3-4). Only actual prior coordination grounds section 1's inference; failed attempts alone count only as 2.3.A's primary factor, so they allow "may conclude" and not the inference. `tests-independent.l4` was patched to the new fields (section 10.1).
5. **Guards: several results answered impossible input.** Fixed, narrowed in one respect. Footnote 62's test and the upward pricing pressure indicator were guarded first; the Guideline 3 reading, the band, the presumption on the metrics and its two limbs now return a `MAYBE` and answer `NOTHING` out of range. They check each number's range, not that the numbers could come from one market (section 3). The number helpers and predicates are left unguarded by design, documented in section 3, two of them pinned by tests.
6. **"Typically look for": the inputs are named as the requirements, not as the evidence findings.** Fixed: the `Failing firm claim` fields are named as findings on the evidence (fork FF-3).
7. **Cosmetics and citations.** Fixed: `mg-frameworks.l4`'s header quotes "could magnify"; the table is cited as "Indicator Threshold for Structural Presumption", with no slash; "creates or further consolidates a highly concentrated market" is cited to `[pdf page 6 of 51]` and the overview at `[pdf page 3 of 51]`; the two Guideline 7 values are renamed with their modals ("could magnify", "can exacerbate"); and Guideline 10's result is renamed `the claimed benefit is in the market where competition may be lessened`, which asserts no weighing, its `@desc` kept (fork G10-1).
8. **Fns 87 and 90 cite "n.81"** (finding 1, then open question 11). Fixed: closed after the PDF check described in finding 1.

None was disagreed with; finding 3 is the one where the encoding keeps its reading against the refuter's.
