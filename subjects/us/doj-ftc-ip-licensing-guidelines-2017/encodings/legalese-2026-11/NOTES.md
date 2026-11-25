# DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property (2017): notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
These guidelines say when the Department of Justice and the Federal Trade Commission will, or will not, challenge a licensing arrangement.
They do not say what a court must hold, and nothing in this encoding does either.

## 1. Status and what was checked

Status: `draft`, version 0.1.0, written 2026-11-25 by one encoder working alone from the brief, then revised the same day on an independent test pass (section 11) and an adversarial review (section 12).
No domain expert has read it.
Some of the review's requests are held, because the independent test file spells the names they would change (section 13).

What was checked, and how:

- The source is `../../registers/source-bundle/2017-ip-licensing-guidelines.txt`, a `pdftotext` extraction of the 38-page PDF (text sha256 `6327fa46…`, PDF sha256 `74c75d29…`, both in the `.meta.json` beside it).
  It was read in full.
  Quotations were checked against that text, not against the PDF (the meta file warns that the extraction is not the authentic text): on 2026-11-25 a script took every double-quoted span in the modules' comments and in this file, split it at each `...`, and searched each piece in the flattened text, allowing a footnote number between words; every miss was read by hand, and was either one of this encoding's own result names or reading labels (not a quotation), a sentence broken by a page break or a footnote, or a misquotation, which was corrected.
- `check.sh` was run with both builds, and its output is in section 7.
- `check.sh` was shown able to fail: it exits 1 with a wrong expected count (a scratch copy expecting 156 for `ip-tests-boundaries.l4` before the review, and 163 after it) and with a main run that does not finish in `L4_MAIN_TIMEOUT`, and exits 2 with no main build, with an unstable build given as `L4_MAIN`, with a missing binary, and with a stub binary that prints nothing.
  `ip-tests-red.l4` holds four wrong assertions, and both builds fail all four.

**Whether the guideline is in force** (what was read at source, and what was only reported):

| fact | how it is known |
| --- | --- |
| The 2017 guidelines are listed among the DOJ's current guidelines. | Read at source by the parent session on 2026-11-25: `https://www.justice.gov/atr/guidelines-and-policy-statements-0`, page "Updated November 17, 2025" (the `in_force_check` field of the `.meta.json`). Not re-read by this encoder, who fetched nothing. |
| They replace the 1995 IP Licensing Guidelines of 6 April 1995. | Read at source: n.1 [pdf page 3]. |
| The 2000 Antitrust Guidelines for Collaborations Among Competitors were withdrawn on 11 December 2024. | **Reported only**: the parent session's search summary of an FTC press release it could not fetch. Not read at source. These guidelines lean on them in Example 3 (n.43 [pdf page 15]), so Example 3's citation points at a withdrawn document; the screen encoded from Example 3 is the Example's own words and does not depend on it. |
| The 2023 Merger Guidelines say that edition "consolidates, revises, and replaces" the earlier Merger Guidelines, so the 2010 Horizontal Merger Guidelines that n.31 and 5.7 cite are a document the 2023 text says it replaces. | Read at source, by grep on 2026-11-25, in the 2023 text deposited on branch `us/doj-ftc-guidelines` (`subjects/us/doj-ftc-merger-guidelines-2023/registers/source-bundle/2023-merger-guidelines.txt`, pdf page 5: "This edition of the Merger Guidelines consolidates, revises, and replaces the various versions of Merger Guidelines previously issued by the Agencies."). That text is not on this branch. Section 10. |

**"Create no independent rights or obligations."**
The coordinator's common brief for this batch of guidelines (`BRIEF-COMMON.md`, item 6) says the guideline creates "no independent rights or obligations"; this row's `BRIEF.md` does not hold the words.
They are **not in this text** (a search of the extraction finds neither "independent rights" nor "rights or obligations").
They are the 2023 Merger Guidelines' words ("the Merger Guidelines create no independent rights or obligations", pdf page 5 of the 2023 text named above), and the subject-level `SOURCE-LICENSE.md` now says so and that this document contains no such sentence.
This row has no copy of `SOURCE-LICENSE.md` beside its modules, although commons' `CLAUDE.md` asks for one in each row: the subject-level file (`../../SOURCE-LICENSE.md`) follows the layout of the euca-1970 subject (`subjects/us/federal-state-extended-unemployment-compensation-act-of-1970/`, whose only row has no copy; listed 2026-11-25), and the coordinator said no row copy is needed.
This guideline's own disclaimers are these, and the modules' header comments carry them:

- 1.0 [pdf page 3]: the guidelines "cannot remove judgment and discretion in antitrust law enforcement".
- n.2 [pdf page 3]: users should rely on qualified counsel; parties wanting to know the agencies' intentions should seek a business review letter or an advisory opinion.
- n.19 [pdf page 8]: the Examples are hypothetical.
- n.70 [pdf page 31]: "the factors listed are those that guide the Agencies' internal analysis in exercising their prosecutorial discretion".

So the result types are named for what the agencies say they do, with the text's own modal ("will", "may", "would be likely to", "generally"), and no type says "lawful", "unlawful" or "illegal" of the arrangement as a holding of this encoding.
**Five names do not meet that yet** (fork F25, held in section 13): the 3.3 results drop "ordinarily will treat"; 5.5's exclusion result drops "In general"; 5.5's pool wrapper returns 3.4's "will challenge" for the text's "subject to challenge"; and two turn a passive sentence into the agencies' own act: 5.2's "will be considered per se illegal" became "the agencies will consider the agreement per se illegal", and 5.5's "may be challenged as unlawful restraints of trade" became "the agencies may challenge the settlement as an unlawful restraint of trade".
Section 6's "it may violate section 2 of the Sherman Act" keeps the text's own words.

## Seat

A party to an intellectual property licensing arrangement, the licensor or a licensee (in practice, with its counsel), asking what the agencies say they will do with the arrangement: whether a restraint is in the safety zone, which mode of analysis applies, and what the guidelines say of the particular restraint.
The agencies are never the seat; their statements are encoded for what they mean to that party.
There is no seat layer with `@export` and `@desc` questions yet (deferred; the brief did not ask for one).

## 2. Target and builds

Target compiler: **`main`** (the stable `l4`), build `1.6.112 (main, e4f4bf3, 2026-11-18)`.
Written and tested with `unstable-20261125-a50cbd0 (unstable, a50cbd0, 2026-11-25)`.
`main` has no `REFUSE`, so a case the text does not answer is `NOTHING` from a `MAYBE`, never `FALSE`.
No module uses anything `main` lacks; the two builds give the same counts on every module (section 7).

## 3. Scope

In scope: the tests and definite statements of parts 1 to 6 and the ten Examples.

- 4.3, the safety zone: condition (1), not facially anticompetitive (n.59); condition (2), no more than twenty percent of each relevant market significantly affected, exactly twenty inside; the goods-markets-only rule and its exception; the four-or-more criteria for technology and research and development markets without usable share data; where the zone does not apply (n.58; transfers given a merger analysis, n.60, n.86; and n.85's in-substance transfers, read into n.86, F8); "absent extraordinary circumstances"; outside the zone is not a finding (4.3 [pdf page 27]).
- Parts 2 and 3: reach (2.1); market power never presumed from protection (2.2, 5.3); the concerns (3.1); whether a technology market (3.2.2, n.33) or a research and development market (3.2.3) is analysed; the equal-share rules ("will assign", 3.2.2 via Example 2; "may assign", 3.2.3); Example 3's four-entity screen; horizontal and vertical relationships (3.3, n.27); per se or rule of reason, and the depth of the rule-of-reason inquiry (3.4).
- Part 4: the risk considerations of 4.1.1 as a report; exclusivity in effect, and the two statements that a license "generally" raises no concern (4.1.2); what the agencies do on their findings, and the considerations for reasonable necessity (4.2).
- Parts 5 and 6: 5.1 to 5.7 and part 6, each to the extent the text states a test or a definite step; for 5.7, Example 10's own limb as well.

Not computed, by design:

- **No weighing.** Where the text lists considerations and gives no test (4.1.1, 4.2's duration, 5.4, 5.6), the caller supplies them and a function reports which are present, in the text's order. The text calls the balancing "necessarily a qualitative one" (4.2 [pdf page 25]).
- **Findings are inputs.** Market power, close substitutes, efficiency-enhancing integration, reasonable necessity, a significant reduction in incentives, a horizontal cartel, a "large fraction": all are the agencies' findings, supplied by the caller and never derived.
- **The Examples' bottom lines** in Examples 1, 7 and 9 ("would be unlikely to object", "unlikely to challenge") are reached from considerations, not from a test; the fixtures supply the agencies' finding and assert what the body rules do with it (section 6; fork F26).
- **Market definition and share measurement** (3.2.1, n.31, n.35): the caller supplies the markets and the shares.

## 4. Modules

| module | what it holds |
| --- | --- |
| `ip-nouns.l4` | Types only: the inputs, one record per provision's facts. |
| `ip-framework.l4` | 1.0, 2.1, 3.1, 3.2.2, 3.2.3 (with Example 3's screen and the shared count of entities), 3.3, 3.4. |
| `ip-rule-of-reason.l4` | 4.1.1, 4.1.2, 4.2. |
| `ip-restraints.l4` | 5.1 to 5.7, 6. |
| `ip-safety-zone.l4` | 4.3. It comes after the restraints because it reads 5.7. |
| `ip-tests.l4` | The ten Examples as fixtures. |
| `ip-tests-boundaries.l4` | Both sides of every threshold, every branch, and one discriminating fixture per fork that can have one (section 8). |
| `ip-tests-red.l4` | Four positive controls, each a misreading that must fail. |
| `tests-independent.l4` | 152 assertions written from the text by a reader who had not seen the encoding (section 11). |

Every rule carries an `@ref` with its section, footnote and `[pdf page N]`.

## 5. Coverage

Every numbered part, every Example, and every footnote, with its disposition.

| part | disposition | where, or why |
| --- | --- | --- |
| 1 / 1.0 Intellectual property and the antitrust laws | encoded | `1.0: whether the guidelines cover licensing of` (trademarks not covered, n.1; mask works covered, n.8). The account of each form of property is background: inert. |
| 2 / 2.0 General principles | inert | The three principles are framing; each is given effect where it bites (2.1, 2.2, 2.3). |
| 2.1 Standard antitrust analysis applies | encoded | `2.1: the reach of the principles`. |
| 2.2 Intellectual property and market power | encoded | No presumption of market power from protection: market power is always an input, and the field saying the tying item is protected is read by no rule (tested in 5.3). The definition of market power (n.15) is the caller's to apply. |
| 2.3 Procompetitive benefits of licensing | inert | States no test. Its notion of a blocked technology is used by the 3.2.2 competitor test. |
| 3 Antitrust concerns and modes of analysis | inert | A heading; part 3 begins with 3.1. |
| 3.1 Nature of the concerns | encoded | `3.1: when competition among actual or potential competitors may be adversely affected`. Its result's "sections 3.2 to 5" is this encoding's gloss on the text's "set forth below". |
| 3.2 Markets affected | inert | Framing for 3.2.1 to 3.2.3. |
| 3.2.1 Goods markets | inert | Delineation and share measurement follow the 2010 Horizontal Merger Guidelines (n.31); the shares are the caller's input. |
| 3.2.2 Technology markets | encoded | Whether one is analysed (n.33, F24); the equal share of Example 2's Discussion (n.37), none where no technology market is analysed; the competitor test, where blocked wins (F16). |
| 3.2.3 Research and development markets | encoded | The delineation rule; the "may assign" equal share. How R&D competition may be harmed is explanation: inert. |
| 3.3 Horizontal and vertical relationships | encoded | `3.3: the relationship of the parties in the market`, n.27. |
| 3.4 Framework for evaluating restraints | encoded | `3.4: the mode of analysis`, `3.4: what the agencies do with the restraint`. |
| 4 Rule-of-reason principles | inert | A heading. |
| 4.1 Analysis of anticompetitive effects | inert | One framing sentence. |
| 4.1.1 Market structure, coordination, foreclosure | encoded | A factor report, no weighing. |
| 4.1.2 Exclusivity | encoded | Exclusive licensing and exclusive dealing in effect; the two "generally" statements. |
| 4.2 Efficiencies and justifications | encoded | The definite steps; the considerations of reasonable necessity as a report. |
| 4.3 Antitrust "safety zone" | encoded | `4.3: the antitrust safety zone` and its parts. |
| 5 / 5.0 Application of general principles | inert | "not intended as an exhaustive list". |
| 5.1 Horizontal restraints | encoded | 3.4's test. |
| 5.2 Price maintenance | encoded | State law (n.65) out-of-scope: another body of law. |
| 5.3 Tying arrangements | encoded | Including package licensing. |
| 5.4 Exclusive dealing | encoded | Rule of reason, and a report of the matters taken into account. |
| 5.5 Cross-licensing and pooling | encoded | The per se mode; exclusion; terms on future technology; settlements. The account of the benefits of pooling is inert. |
| 5.6 Grantbacks | encoded | Rule of reason, and a report. |
| 5.7 Acquisition of rights | encoded | The sale and the exclusive license (5.7's definition word for word); n.85's "may also apply"; Example 10's "would apply"; n.86. |
| 6 Invalid or unenforceable rights | encoded | A list of the statements that apply. |

| Example | disposition | what the fixtures assert |
| --- | --- | --- |
| 1 ComputerCo | encoded | Vertical; 3.1 states nothing; the finding of no likely effect gives "will treat it as reasonable" and "will not challenge"; the barred-other-programs variant is exclusive dealing under the rule of reason; the form of property does not matter (n.22). The bottom line is supplied as the agencies' finding. |
| 2 Alpha and Beta | encoded | A technology market may be analysed. The fixture is partly constructed: that the processes are marketed apart from the drug is implied, not stated. The equal share is tested in the boundaries file, since the Example gives no count. |
| 3 Biodegradable plastic venture | encoded | The screen at four and at three, unassessed and with a significant risk, which wins at four as well (F22). n.43 (the 2000 Collaborations guidelines, **reported** withdrawn; the National Cooperative Research Act) and n.44 ("Cf. section 4.3") are out-of-scope and inert. The venture's effects in other markets (the Example's last paragraph) are not screened. |
| 4 AgCo and FarmCo | encoded | Vertical in emission control technology; horizontal in farm equipment. |
| 5 Cross-license of valves | encoded | Horizontal in part and vertical in part; licensing to others "not important". |
| 6 Gamma's sham process | encoded | Per se; with a real advance used by licensees, rule of reason. The body's "will" kept against the Example's "would be likely to". |
| 7 NewCo and BigCo | encoded | Exclusive licensing raises no concern absent a horizontal relationship; exclusive dealing under the rule of reason; the factor reports. The bottom line is supplied as the agencies' finding. |
| 8 Jointly assigned substitutes | encoded | Per se without integration (3.4 "will challenge", 5.1 "may merit per se treatment"); rule of reason with it; the quick look (fork F11). |
| 9 Jointly assigned blocking patents | encoded | Not horizontal in the patents; horizontal in the goods market. The bottom line is supplied. |
| 10 Omega and Delta | encoded | Horizontal (a potential competitor); the Example's own limb, "would apply a merger analysis" as an acquisition of a potential competitor, from the Situation's facts (nominally non-exclusive, every reasonable offer rejected); n.85's "may also apply" for the same license; the safety zone does not apply (n.86, F8). The license is not 5.7's exclusive license (section 6). |

No Example applies 4.3 with figures, so the safety-zone fixtures come from 4.3's own words (`ip-tests-boundaries.l4`).
The fixtures for Examples 4, 5 and 9 are **not independent**: the 3.2.2 competitor test and the blocking rule were read with those Examples in view.

| footnote | disposition | note |
| --- | --- | --- |
| n.1 | encoded | Trademarks not covered; the 1995 guidelines replaced (section 1). |
| n.2 | inert | Disclaimer (section 1). |
| n.8 | encoded | Mask works treated as copyright. |
| n.14, n.20 | out-of-scope | International enforcement: another guideline (n.14) and foreign law (n.20). |
| n.15 | inert | The dimensions of market power; market power is an input. |
| n.19 | inert | The Examples are hypothetical. |
| n.22 | encoded | Form-invariance of Example 1. |
| n.26 | inert | No duty to license; remedies. |
| n.27 | encoded | Potential competitor. |
| n.28 | inert | "Input" includes outlets; the caller applies it in listing the 3.1 concerns. |
| n.30 | inert | Goods include services. |
| n.31, n.35, n.52 | out-of-scope | Share measurement and market analysis under the 2010 Horizontal Merger Guidelines (open question 1). |
| n.33 | encoded | No separate technology-market analysis. |
| n.37 | encoded | "Comparably efficient" (a finding). |
| n.43 | out-of-scope | The 2000 Collaborations guidelines (reported withdrawn) and the National Cooperative Research Act. |
| n.44, n.61 | inert | Cross-reference; congressional intent. |
| n.58, n.59, n.60 | encoded | Where the zone does not apply; facially anticompetitive; the cross-reference to 5.7. |
| n.62 | inert | The time of the conduct. No rule reads a time or a date: the encoding does not model it, and the caller must supply the facts as they stood then. |
| n.64, n.69 | inert | Background (Leegin; patent misuse statute). |
| n.65 | out-of-scope | State law on resale price maintenance. |
| n.70 | inert | The prosecutorial-discretion disclaimer (section 1). |
| n.82 | inert | Pool mechanisms narrowing grantbacks. |
| n.85, n.86 | encoded | Merger analysis "in substance"; the zone does not apply to 5.7 transfers. |
| all others: n.3-7, 9-13, 16-18, 21, 23-25, 29, 32, 34, 36, 38-42, 45-51, 53-57, 63, 66-68, 71-81, 83, 84, 87-90 | inert | Citations, cross-references, or background that states no test (the first line of every footnote was read on 2026-11-25, and the full text where it was not a citation). |

Counts. Numbered parts (28 rows): 20 encoded, 8 inert, 0 out-of-scope, 0 deferred.
Examples: 10 encoded.
Footnotes (90): 31 footnotes are named in 23 rows, 11 of them encoded, 13 inert and 7 out-of-scope; the other 59 are inert.

## 6. The Examples where the text and the body differ

- **3.4 against Example 6.** 3.4 says the agencies "will challenge the restraint under the per se rule"; Example 6 says the agency "would be likely to challenge" it under the per se rule. The result keeps 3.4's words (fork F25).
- **5.7 and n.85 against Example 10.** 5.7's exclusive license "precludes all other persons, including the licensor"; n.85 says the agencies "may also apply" a merger analysis to a license outside that definition that in substance transfers the rights, and cites Example 10 for it.
  Example 10 finds the nominally nonexclusive license "exclusive in fact", and says the agency "would apply a merger analysis to this transaction, since it involves an acquisition of a potential competitor".
  The Situation never says Omega is precluded from using its own patent, so the license is not 5.7's exclusive license.
  The fixture gives the Situation's facts, and three answers follow: n.85's "may also apply", the Example's own limb ("would apply", as an acquisition of a potential competitor), and n.86's "does not apply" for the safety zone (fork F8).
  Until the review of 2026-11-25 the fixture set the exclusive-license field TRUE so that 5.7's "will apply" answered; that reading is withdrawn.
- **Examples 1, 7 and 9** reach "unlikely to object" or "unlikely to challenge" from considerations. No rule is minted from them: the fixtures supply the finding of no likely anticompetitive effect, and assert that 3.4 and 4.2 then give "will treat it as reasonable" and "will not challenge" (fork F26).
- **Example 8.** "May conclude that the joint marketing ... constitutes horizontal price-fixing" is the classification of the restraint, which the caller supplies; once it is classed so, 3.4 says "will" and 5.1 says it "may merit per se treatment". The Example's own "may" is in no result (fork F25). Its "sufficiently apparent" effects are read as 3.4's "facially appears" (fork F11).

## 7. Checks

`L4=<unstable l4> L4_MAIN=<main l4> ./check.sh`, run 2026-11-25:

```
your l4:    unstable-20261125-a50cbd0 (unstable, a50cbd0, 2026-11-25)
main build: 1.6.112 (main, e4f4bf3, 2026-11-18)
module                      err  sat fail  ref  expected |  err  sat fail  ref  main
ip-framework.l4               0    0    0    0       0/0 |    0    0    0    0  same
ip-nouns.l4                   0    0    0    0       0/0 |    0    0    0    0  same
ip-restraints.l4              0    0    0    0       0/0 |    0    0    0    0  same
ip-rule-of-reason.l4          0    0    0    0       0/0 |    0    0    0    0  same
ip-safety-zone.l4             0    0    0    0       0/0 |    0    0    0    0  same
ip-tests-boundaries.l4        0  164    0    0     164/0 |    0  164    0    0  same
ip-tests-red.l4               4    0    4    0       0/4 |    4    0    4    0  same
ip-tests.l4                   0   58    0    0      58/0 |    0   58    0    0  same
tests-independent.l4          0  152    0    0     152/0 |    0  152    0    0  same
TOTAL (9 modules): satisfied unstable 374, main 374; failed (positive controls) unstable 4, main 4
(a failed assertion is also an error; the expected column is satisfied/failed)
check.sh: all passed
```

The four errors in `ip-tests-red.l4` are its four failed assertions; no module has any other error.
The stable `l4 run` exits 0 on `ip-tests-red.l4` and the unstable one exits 1, which is why `check.sh` reads the diagnostics.
What it does not see: equal counts on the two builds can hide a different assertion failing on each side.

## 8. Fork register

Every reading below is **assumed, not ruled**.
Each has a fixture in `ip-tests-boundaries.l4` (or `ip-tests.l4` where named) on which the reading taken and its alternative give different answers, except four that no fixture can tell apart: F9 and F25, which are only results' names; F18, whose alternative would leave the equal-share rule unused (its fixtures test the rule's own edges); and F26, whose alternative is a rule nobody has written.
For F23 and F24 the alternative needs an input the record cannot hold, so their fixture is the case the alternative would answer differently, not a run of the alternative.
F8, F16 and F22 were revised on review on 2026-11-25, and the cell says what the earlier reading was.

| fork | the question | reading taken | the alternative | the text |
| --- | --- | --- | --- | --- |
| F1 | How is "collectively account for" computed? | The sum of each party's own share, each counted once. | Each party's share alone. | 4.3 "the licensor and its licensees collectively account for no more than twenty percent". Fixture: 15 + 10. |
| F2 | Must several affected markets each pass? | Each market considered must meet its own criterion; any one that fails puts the restraint outside, and the failing markets are named. | One market passing is enough, or the shares are pooled. | 4.3 "of each relevant market significantly affected". Fixture: goods markets at 15 and 21. |
| F3 | What is "independently controlled"? | Count distinct controllers, not technologies or entities. | Count items. | 4.3 "four or more independently controlled technologies". Fixture: four technologies, three controllers. |
| F4 | What is "facially anticompetitive"? | By the type of restraint (a type accorded per se treatment), or a restraint that would always or almost always reduce output or raise prices, whatever its integration. | Only a restraint that 3.4 would in fact treat per se (no integration). | n.59 "restraints that normally warrant per se treatment". Fixture: market division with integration is rule of reason under 3.4 yet outside the zone. |
| F5 | Is 3.4's per se list closed? | Open: the caller may class another type as accorded per se treatment. | Closed to the four named. | 3.4 "Among the restraints"; 5.1 "including". |
| F6 | With accurate share data, which criterion applies to a technology or research and development market? | The twenty percent test, as for goods markets. | The four-or-more count whenever enough others exist. | 4.3 [pdf page 26]: the counts apply "if market share data are unavailable or do not accurately represent competitive significance". Fixture: a technology market at 25 with five others. |
| F7 | A goods market with no usable share data? | NOTHING: the text names no criterion. | Inside, or outside. | 4.3 gives the substitute criteria only for technology and research and development markets. |
| F8 | n.85 transactions, n.86, and Example 10. | Three limbs: 5.7's exclusive license read word for word (the licensor precluded too), "will apply"; n.85's license that in substance transfers the rights and raises the same concern, "may also apply"; Example 10's own limb (nominally non-exclusive, every reasonable offer rejected, a potential competitor), "would apply". The zone does not apply to n.85's transfers either: n.86 speaks of transfers "such as those described in this section", and n.85 is in that section. | Example 10 as 5.7's exclusive license "in fact" (the reading before the review: but 5.7's definition needs the licensor precluded, which the Example never says, and the Example gives its own reason); and n.86 confined to the sale and the exclusive license, leaving an n.85 license's zone NOTHING (the reading before the review) or inside. | 5.7, n.85, n.86 [pdf page 36]; Example 10 [pdf pages 36-37]. Fixtures: the n.85 license and the zone in the boundaries file; Example 10 in `ip-tests.l4`. |
| F9 | "Absent extraordinary circumstances". | A qualifier kept in the result's name; not an input. | An input that defeats the zone. | 4.3; the text never says what they are (open question 2). |
| F10 | No market to consider. | NOTHING. | Inside (no market fails). | 4.3 assumes at least one relevant market is significantly affected. |
| F11 | Example 8's "sufficiently apparent" and "sufficiently weak or not reasonably related". | 3.4's "facially appears ... always or almost always", with efficiencies not reasonably related. | A separate standard. | Example 8 [pdf page 29]; 3.4 [pdf page 20]. Fixture in `ip-tests.l4`. |
| F12 | 5.6: when are the offsetting effects considered? | Only once the agencies determine a likely significant reduction in incentives; the "In addition" sentence is read as part of that consideration. | Always reported. | 5.6 [pdf page 35] "If the Agencies determine ...". |
| F13 | Example 3's "comparable capabilities and incentives" and 4.3's research and development criterion. | The same count: independently controlled, not a party's, with the required assets and the incentive. | Two different tests. | Example 3 [pdf page 15]; 4.3 [pdf page 27]. |
| F14 | A trademark license and the zone. | NOTHING: the guidelines do not cover trademarks. | "Does not apply". | n.1. |
| F15 | When goods-market analysis alone is inadequate, are goods markets still considered? | Yes, every listed market is considered. | Only the technology and research and development markets. | 4.3 "by reference only to goods markets unless ...". Fixture: goods analysis inadequate, a goods market at 25 and a technology market without share data with four independent technologies: outside, on the goods market (the alternative: inside). |
| F16 | Inputs the text treats as exclusive, both TRUE. | Where the text says which wins, it wins: blocked beats substitute (Example 9 [pdf page 34]: blocking patents "are not substitutable", and their owners are not horizontal in them), so the parties are not actual competitors in the technology (3.2.2); a clear, significantly less restrictive alternative beats reasonable necessity, "will not give weight" (4.2 [pdf page 25]: the sentence is unconditioned, and the alternative is "relevant to a determination of whether a restraint is reasonably necessary"). Where it does not, NOTHING: no likely effect and a facially harmful restraint with no related efficiency (3.4). | NOTHING for all three (the reading before the review); or the other side winning. | 3.2.2, 2.3, Example 9; 4.2; 3.4. Fixtures: one per pair. |
| F17 | 4.1.2: exclusive licensing with a horizontal relationship; a non-exclusive license with exclusive dealing. | NOTHING for both: "only if" states nothing on the other side, and exclusive dealing is a restraint on the licensee's conduct. | "may raise antitrust concerns" as a result; exclusive dealing not counted as a restraint. | 4.1.2 [pdf page 23]. |
| F18 | The equal share of Example 2's Discussion. | A general rule for technology markets ("will assign"), given only for a whole count of at least one. | Confined to Example 2. | Example 2 [pdf page 12], n.37. |
| F19 | Order of the zone's gates. | Coverage, then n.58, then the merger analysis, then condition (1), then condition (2). | Another order. A per se restraint outside any licensing arrangement then reads "does not apply", not "outside". | 4.3, n.58. Fixture: a per se restraint not in a licensing arrangement. |
| F20 | Section 6: the "other elements", and fraud without them. | One input stands for both sentences' other elements. Fraud without them: the fraud sentence states nothing; if inequitable conduct is also found, its sentence says it will not be the basis of a section 2 claim, because "unless" needs both fraud and the elements. | Two inputs; or "may violate" without the elements. | 6 [pdf page 37] "if all the elements otherwise necessary to establish a charge are proved"; "will not be the basis of a section 2 claim unless". |
| F21 | 3.1 when no concern appears; Example 3 with fewer than four and no significant risk. | NOTHING for both. So Example 1's "unlikely to object" is reached only through 4.1.2 (its result `generally, the exclusive licensing raises no antitrust concern: ...`, from the "only if" sentence) and the supplied finding (F26), never through 3.1. | That the agencies will not challenge; that the venture is unlikely to harm competition. | 3.1; Example 3. |
| F22 | Example 3 with four or more others and a significant risk found. | The risk wins: "would proceed to consider efficiency justifications". The risk sentence is not conditioned on the count, and "ordinarily" leaves room for the case where the agency finds the risk anyway. | The risk sentence belongs to the fewer-than-four branch, so four or more gives "ordinarily would be unlikely" whatever is found (the reading before the review). | Example 3 [pdf pages 15-16]. Fixture in `ip-tests.l4`: four others, `JUST TRUE`. |
| F23 | One input, "the agencies conclude that the restraint is unlikely to have an anticompetitive effect", for 3.4 and 4.2. | FALSE means both a conclusion that the restraint has, or is likely to have, such an effect and no conclusion yet. 3.4 reads it as "no conclusion of no effect", which fits both; 4.2 reads it as the contrary conclusion, which it needs before it balances, so a caller with no conclusion yet who says the restraint is reasonably necessary gets "will balance" early. | A three-valued input (no likely effect; a likely effect; not yet concluded), with 4.2 answering NOTHING until a conclusion is made. Held (section 13). | 4.2 [pdf page 25] "If the Agencies conclude that the restraint has, or is likely to have, an anticompetitive effect". Fixture: FALSE, FALSE, TRUE, FALSE gives "will balance". |
| F24 | 3.2.2 when the rights are not marketed separately. | FALSE is read as n.33's case, IP licensed "as an integral part of a marketed good": "no need for a separate analysis of technology markets", and no equal share. A caller who has not said how the rights are licensed gets the same answer, which over-reads n.33. | A three-way input (marketed separately; an integral part; not stated, NOTHING). Held (section 13). | 3.2.2, n.33 [pdf page 11]; Example 2 [pdf page 12]. Fixture: FALSE gives "no need". |
| F25 | Result names whose modal or attribution differs from the text. | Kept: 3.3's results without "ordinarily will treat" [pdf page 16]; 5.5's exclusion result without "In general" [pdf page 33]; 5.5's pool wrapper with 3.4's "will challenge" for "subject to challenge under the per se rule" [pdf page 32]; 5.2's "the agencies will consider the agreement per se illegal" for the passive "will be considered per se illegal" [pdf page 30]; 5.5's "the agencies may challenge the settlement" for the passive "may be challenged as unlawful restraints of trade" [pdf page 32]; and 3.4's "will challenge" where Example 6 says "would be likely to" and Example 8 "may". | The text's words in each name. Held for the first five (section 13); 5.1 has been given its own words ("may merit per se treatment"). | The sentences cited. A name only: no fixture tells them apart. |
| F26 | The bottom lines of Examples 1, 7 and 9. | Supplied as the agencies' finding of no likely anticompetitive effect; the fixtures assert what 3.4 and 4.2 do with it. Without the supplied finding no rule reaches "unlikely to challenge" or "unlikely to object". | Computing the bottom line from the facts (an empty 4.1.1 report, no horizontal relationship). | Examples 1, 7, 9. No fixture: the alternative is a rule the text does not state. |
| F27 | An impossible share the zone does not reach. | Passed over: condition (1) is checked before the shares, so a per se restraint beside a share of 150 is "outside"; and a market not considered is not checked, so a technology market at 500 is ignored when goods-market analysis is adequate. | NOTHING whenever any listed share is impossible. | 4.3; F19's order. Fixtures: both cases. |

## 9. Open questions for a domain expert

1. **Closed 2026-11-25.** Are the 2010 Horizontal Merger Guidelines, which 3.2.1 (n.31) and 5.7 rely on, still the agencies' merger guidelines? The 2023 Merger Guidelines say that edition "consolidates, revises, and replaces the various versions of Merger Guidelines previously issued by the Agencies" (pdf page 5 of the 2023 text; section 1's table says where it was read). So the IP text's two citations of the 2010 guidelines (n.31 and 5.7) point at a document the 2023 text says it replaces, and the IP Guidelines, which are the 2017 text, were not revised to match. In practice 5.7's "merger analysis" now points to the 2023 guidelines; that rests on that one sentence and on nothing else. How a 5.7 merger analysis is done is outside this encoding either way.
2. What are "extraordinary circumstances" (4.3)? The text does not say; the result carries the qualifier (F9).
3. Does n.86 take n.85's in-substance transfers out of the safety zone? The encoding now reads it so (F8); an expert should confirm.
4. With accurate share data in a technology or research and development market, do the agencies ever apply the four-or-more criteria instead (F6)?
5. What is a "large fraction of the potential research and development" (5.5)? No figure is given; it is an input.
6. How are shares in a research and development market measured when they are available (4.3 condition (2) applies to "each relevant market")? The text gives the twenty percent test but no measure.
7. The 2000 Collaborations guidelines were reported withdrawn on 11 December 2024. Does the withdrawal change how the agencies read Example 3, which cites them (n.43)?
8. Is the agencies' international guideline cited in n.14 (2017) still in force? Not checked.

## 10. Withdrawn and superseded guidelines

- **1995 IP Licensing Guidelines** (6 April 1995): replaced by these guidelines. Source: n.1 [pdf page 3], read at source.
- **2000 Antitrust Guidelines for Collaborations Among Competitors**: withdrawn 11 December 2024. Source: an FTC press release, **reported only** (the parent session's search summary; not fetched, not read). Cited by Example 3, n.43.
- **2010 Horizontal Merger Guidelines**: cited by n.31 and 5.7. The 2023 Merger Guidelines say they replace "the various versions of Merger Guidelines previously issued by the Agencies" (pdf page 5 of the 2023 text, read at source by grep on 2026-11-25; open question 1). No date of replacement is taken from anything else.

## 11. Independent test pass

`tests-independent.l4` was written on 2026-11-25 by a fresh agent that read the source text in full and wrote its expected answers before opening this folder; only then did it read the nouns and rule modules (not this encoding's tests) to phrase the facts, and it did not change its answers after that (its header says so, and says which kinds of assertion, about ten, have no pre-written answer).
It holds 152 assertions.

Before this round's fixes it gave 149 satisfied and 3 failed on both builds (unstable a50cbd0 and main 1.6.112), measured by this encoder at the start of the round; the failures were at lines 248, 469 and 488 of the file as delivered, now 252, 481 and 500 after the two comment blocks added below.

| assertion | what it expected | what it turned out to be |
| --- | --- | --- |
| A12, a license that in substance transfers the rights (n.85) | the safety zone does not apply (n.86) | **An encoding error.** The encoding answered NOTHING. Fixed: n.86 covers n.85's transfers (F8). |
| B6, 3.4 with a restraint that would always or almost always reduce output, reasonably related to efficiencies, with integration | NOTHING ("text silent on outcome") | **A test-author error.** With integration 3.4 sends the restraint to the rule of reason, and "Application of the rule of reason requires an inquiry into the likely competitive effects" (n.48: sections 4.1 to 4.3); the quick look needs a restraint not reasonably related to efficiencies. The encoding's answer, the inquiry, was right. This one expected value was corrected, on the coordinator's instruction, with a signed and dated comment at the assertion; a line in the file's header says so. |
| C4, a clear, significantly less restrictive alternative and a finding of reasonable necessity | "will not give weight" | **An encoding error.** The encoding answered NOTHING for contradictory findings. Fixed: the unconditioned sentence wins (F16). |

After the fixes: 152 satisfied, 0 failed, on both builds (section 7).
No other assertion in the file was edited.

Two passing assertions rest on a reading this encoding no longer takes: lines 736 and 737 give Example 10 the exclusive-license field TRUE, and expect 5.7's "an exclusive license" and the zone not applying. They pass because the function still maps that field to that answer; the encoding's own Example 10 fixture now sets the field FALSE (F8). They are left as the author wrote them.

## 12. Adversarial review

A fresh agent was asked to refute the encoding against the text, on 2026-11-25.
The coordinator relayed its findings 2 to 10 by number, and the Example 10 finding, which both reviewers made, as a separate item; this section counts that one as finding 1.
"Fixed" means the code now follows the text; "narrowed" means part was fixed and the rest is a fork held in section 13; none was disagreed with.

| finding | the text | what was done |
| --- | --- | --- |
| 1. Example 10's fixture says the licensor is precluded; n.85 and n.86 misread. | 5.7, n.85, n.86 [pdf page 36]; Example 10 [pdf pages 36-37]. | **Fixed**, except the field's name (held). Three limbs, the Situation's own facts, and the zone out for n.85 transfers (F8). |
| 2. F15 has no discriminating fixture. | 4.3 [pdf page 26]. | **Fixed.** Fixture added; section 8 corrected. |
| 3. Example 3 with four or more ignores a significant risk found. | Example 3 [pdf pages 15-16]. | **Fixed.** The risk wins; both readings in F22. |
| 4. One input stands for "no effect found" and "no finding yet". | 4.2 [pdf page 25]. | **Narrowed.** Fork F23 and a fixture; the three-valued input is held. |
| 5. F16's contradictions answer NOTHING where the text says which wins. | 4.2 [pdf page 25]; Example 9 [pdf page 34]. | **Fixed.** A clear alternative wins; blocked wins. 3.4's pair stays NOTHING (F16). |
| 6. 3.2.2's FALSE over-reads n.33; the equal share is given where no technology market is analysed. | 3.2.2, n.33 [pdf page 11]. | **Narrowed.** No equal share without a technology market; fork F24; the three-way input is held. |
| 7. Section 6's inequitable-conduct sentence is gated on enforcement. | 6 [pdf page 37]. | **Fixed.** It answers without enforcement; a fixture shows it. |
| 8. Result names drop the text's modals or make passive sentences the agencies' acts. | 3.3 [pdf page 16]; 5.1 [pdf page 28]; 5.2 [pdf page 30]; 5.5 [pdf pages 32-33]. | **Narrowed.** 5.1 now has its own words. The other five names are held (F25), and section 1 says which; Examples 6 and 8 are recorded in F25. |
| 9. Section 1 attributed the "no independent rights" words wrongly and was stale about `SOURCE-LICENSE.md`. | This text has no such sentence; the 2023 Merger Guidelines do. | **Fixed.** Section 1 rewritten. |
| 10. Nits. | As cited. | **Fixed**: F12's page (35); "reported" on the withdrawal in section 5; "blocks" in `ip-nouns.l4`; the boundaries header; the footnote count (31 footnotes in 23 rows); n.62 marked inert; "sections 3.2 to 5" labelled a gloss. |

The independent test author's observations are recorded as forks: Examples 1, 7 and 9's supplied findings (F26); Example 1 reachable only through 4.1.2 (F21); a share of 150 beside a per se restraint, and a technology share of 500 the zone does not consider (F27).

## 13. Held: changes the independent test file pins

The coordinator asked that no independent assertion be edited except B6.
`tests-independent.l4` builds every record with `WITH`, which must supply every field (a probe on both builds: a missing field is the error `check/missing-named-arguments`), and it names result constructors in its assertions.
So the changes below would make the whole file fail to type-check, and are held until the coordinator allows its spellings to be changed.
Each is a fork, and each place in the code says so.

| change asked | why it is held (lines of `tests-independent.l4` as committed) | fork |
| --- | --- | --- |
| Rename the field "the transferee obtains a license that in fact precludes all other persons, including the licensor, ..." to drop "in fact". | Line 62 constructs the record with that field. | F8 (the field already means 5.7's definition; its comment says so) |
| A three-valued finding for 4.2 (no likely effect; a likely effect; no conclusion yet). | Line 322 constructs `Findings under the rule of reason` with that field as a BOOLEAN. | F23 |
| A three-way input for 3.2.2 (marketed separately; an integral part of a marketed good; not stated). | Line 384 constructs the record with a BOOLEAN; line 549 expects "no need" for FALSE. | F24 |
| The text's modal in the 3.3 results ("ordinarily will treat"). | Lines 514, 518, 671, 672, 681. | F25 |
| 5.5's exclusion result with "In general". | Lines 582, 583. | F25 |
| 5.5's pool wrapper in its own words ("subject to challenge under the per se rule"). | Lines 576, 577, 715 expect 3.4's constructor. | F25 |
| 5.2's passive "will be considered per se illegal". | Line 558 (the cartel assertion). | F25 |
| 5.5's passive "may be challenged as unlawful restraints of trade". | Lines 592, 593. | F25 |
