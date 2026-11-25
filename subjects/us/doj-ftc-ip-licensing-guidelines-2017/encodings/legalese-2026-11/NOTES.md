# DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property (2017): notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
These guidelines say when the Department of Justice and the Federal Trade Commission will, or will not, challenge a licensing arrangement.
They do not say what a court must hold, and nothing in this encoding does either.

## 1. Status and what was checked

Status: `draft`, version 0.1.0, written 2026-11-25 by one encoder working alone from the brief.
No domain expert has read it, and no independent test pass has been made yet (a later session is to write one).

What was checked, and how:

- The source is `../../registers/source-bundle/2017-ip-licensing-guidelines.txt`, a `pdftotext` extraction of the 38-page PDF (text sha256 `6327fa46…`, PDF sha256 `74c75d29…`, both in the `.meta.json` beside it).
  It was read in full; every quotation in the modules' comments was checked against that text by a phrase search on 2026-11-25, not against the PDF (the meta file warns that the extraction is not the authentic text).
- `check.sh` was run with both builds, and its output is in section 7.
- `check.sh` was shown able to fail: it exits 1 with a wrong expected count (a scratch copy with 156 for `ip-tests-boundaries.l4`) and with a main run that does not finish in `L4_MAIN_TIMEOUT`, and exits 2 with no main build, with an unstable build given as `L4_MAIN`, with a missing binary, and with a stub binary that prints nothing.
  `ip-tests-red.l4` holds four wrong assertions, and both builds fail all four.

**Whether the guideline is in force** (what was read at source, and what was only reported):

| fact | how it is known |
| --- | --- |
| The 2017 guidelines are listed among the DOJ's current guidelines. | Read at source by the parent session on 2026-11-25: `https://www.justice.gov/atr/guidelines-and-policy-statements-0`, page "Updated November 17, 2025" (the `in_force_check` field of the `.meta.json`). Not re-read by this encoder, who fetched nothing. |
| They replace the 1995 IP Licensing Guidelines of 6 April 1995. | Read at source: n.1 [pdf page 3]. |
| The 2000 Antitrust Guidelines for Collaborations Among Competitors were withdrawn on 11 December 2024. | **Reported only**: the parent session's search summary of an FTC press release it could not fetch. Not read at source. These guidelines lean on them in Example 3 (n.43 [pdf page 15]), so Example 3's citation points at a withdrawn document; the screen encoded from Example 3 is the Example's own words and does not depend on it. |
| The 2010 Horizontal Merger Guidelines, which 3.2.1 (n.31) and 5.7 rely on. | **Not checked.** Open question 1. |

**"Creates no independent rights or obligations."**
The brief attributes these words to the guideline; they are **not in this text** (a search of the extraction finds neither "independent rights" nor "rights or obligations").
`SOURCE-LICENSE.md` at the subject level attributes them to "the merger guidelines' own words", which may be where they come from.
This guideline's own disclaimers are these, and the modules' header comments carry them:

- 1.0 [pdf page 3]: the guidelines "cannot remove judgment and discretion in antitrust law enforcement".
- n.2 [pdf page 3]: users should rely on qualified counsel; parties wanting to know the agencies' intentions should seek a business review letter or an advisory opinion.
- n.19 [pdf page 8]: the Examples are hypothetical.
- n.70 [pdf page 31]: "the factors listed are those that guide the Agencies' internal analysis in exercising their prosecutorial discretion".

So every result type is named for what the agencies say they do, with the text's own modal ("will", "may", "would be likely to", "generally"), and no type says "lawful", "unlawful" or "illegal" of the arrangement itself.
Where the text quotes a legal characterisation, the result keeps it as the agencies' ("the agencies will consider the agreement per se illegal: it constitutes a horizontal cartel", 5.2; "it may violate section 2 of the Sherman Act", 6).

## 2. Target and builds

Target compiler: **`main`** (the stable `l4`), build `1.6.112 (main, e4f4bf3, 2026-11-18)`.
Written and tested with `unstable-20261125-a50cbd0 (unstable, a50cbd0, 2026-11-25)`.
`main` has no `REFUSE`, so a case the text does not answer is `NOTHING` from a `MAYBE`, never `FALSE`.
No module uses anything `main` lacks; the two builds give the same counts on every module (section 7).

## 3. Scope

In scope: the tests and definite statements of parts 1 to 6 and the ten Examples.

- 4.3, the safety zone: condition (1), not facially anticompetitive (n.59); condition (2), no more than twenty percent of each relevant market significantly affected, exactly twenty inside; the goods-markets-only rule and its exception; the four-or-more criteria for technology and research and development markets without usable share data; where the zone does not apply (n.58; transfers given a merger analysis, n.60, n.86); "absent extraordinary circumstances"; outside the zone is not a finding (4.3 [pdf page 27]).
- Parts 2 and 3: reach (2.1); market power never presumed from protection (2.2, 5.3); the concerns (3.1); whether a technology market (3.2.2, n.33) or a research and development market (3.2.3) is analysed; the equal-share rules ("will assign", 3.2.2 via Example 2; "may assign", 3.2.3); Example 3's four-entity screen; horizontal and vertical relationships (3.3, n.27); per se or rule of reason, and the depth of the rule-of-reason inquiry (3.4).
- Part 4: the risk considerations of 4.1.1 as a report; exclusivity in effect, and the two "generally no concern" statements (4.1.2); what the agencies do on their findings, and the considerations for reasonable necessity (4.2).
- Parts 5 and 6: 5.1 to 5.7 and part 6, each to the extent the text states a test or a definite step.

Not computed, by design:

- **No weighing.** Where the text lists considerations and gives no test (4.1.1, 4.2's duration, 5.4, 5.6), the caller supplies them and a function reports which are present, in the text's order. The text calls the balancing "necessarily a qualitative one" (4.2 [pdf page 25]).
- **Findings are inputs.** Market power, close substitutes, efficiency-enhancing integration, reasonable necessity, a significant reduction in incentives, a horizontal cartel, a "large fraction": all are the agencies' findings, supplied by the caller and never derived.
- **The Examples' bottom lines** in Examples 1, 7 and 9 ("would be unlikely to object", "unlikely to challenge") are reached from considerations, not from a test; the fixtures supply the agencies' finding and assert what the body rules do with it (section 6).
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
| `ip-tests-boundaries.l4` | Both sides of every threshold, every branch, and one discriminating fixture per fork. |
| `ip-tests-red.l4` | Four positive controls, each a misreading that must fail. |

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
| 3.1 Nature of the concerns | encoded | `3.1: when competition among actual or potential competitors may be adversely affected`. |
| 3.2 Markets affected | inert | Framing for 3.2.1 to 3.2.3. |
| 3.2.1 Goods markets | inert | Delineation and share measurement follow the 2010 Horizontal Merger Guidelines (n.31); the shares are the caller's input. |
| 3.2.2 Technology markets | encoded | Whether one is analysed (n.33); the equal share of Example 2's Discussion (n.37); the competitor test. |
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
| 5.7 Acquisition of rights | encoded | n.85, n.86. |
| 6 Invalid or unenforceable rights | encoded | A list of the statements that apply. |

| Example | disposition | what the fixtures assert |
| --- | --- | --- |
| 1 ComputerCo | encoded | Vertical; 3.1 states nothing; the finding of no likely effect gives "treat as reasonable" and "will not challenge"; the barred-other-programs variant is exclusive dealing under the rule of reason; the form of property does not matter (n.22). The bottom line is supplied as the agencies' finding. |
| 2 Alpha and Beta | encoded | A technology market may be analysed; the equal share is tested in the boundaries file, since the Example gives no count. |
| 3 Biodegradable plastic venture | encoded | The screen at four and at three, unassessed and with a significant risk. n.43 (the withdrawn 2000 Collaborations guidelines; the National Cooperative Research Act) and n.44 ("Cf. section 4.3") are out-of-scope and inert. The venture's effects in other markets (the Example's last paragraph) are not screened. |
| 4 AgCo and FarmCo | encoded | Vertical in emission control technology; horizontal in farm equipment. |
| 5 Cross-license of valves | encoded | Horizontal in part and vertical in part; licensing to others "not important". |
| 6 Gamma's sham process | encoded | Per se; with a real advance used by licensees, rule of reason. The body's "will" kept against the Example's "would be likely to". |
| 7 NewCo and BigCo | encoded | Exclusive licensing raises no concern absent a horizontal relationship; exclusive dealing under the rule of reason; the factor reports. The bottom line is supplied as the agencies' finding. |
| 8 Jointly assigned substitutes | encoded | Per se without integration; rule of reason with it; the quick look (fork F11). |
| 9 Jointly assigned blocking patents | encoded | Not horizontal in the patents; horizontal in the goods market. The bottom line is supplied. |
| 10 Omega and Delta | encoded | Exclusive in fact: a merger analysis, and the safety zone does not apply (fork F8). |

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
| n.62 | encoded | The time of the conduct: the inputs are the facts then. |
| n.64, n.69 | inert | Background (Leegin; patent misuse statute). |
| n.65 | out-of-scope | State law on resale price maintenance. |
| n.70 | inert | The prosecutorial-discretion disclaimer (section 1). |
| n.82 | inert | Pool mechanisms narrowing grantbacks. |
| n.85, n.86 | encoded | Merger analysis "in substance"; the zone does not apply to 5.7 transfers. |
| all others: n.3-7, 9-13, 16-18, 21, 23-25, 29, 32, 34, 36, 38-42, 45-51, 53-57, 63, 66-68, 71-81, 83, 84, 87-90 | inert | Citations, cross-references, or background that states no test (the first line of every footnote was read on 2026-11-25, and the full text where it was not a citation). |

Counts. Numbered parts (28 rows): 20 encoded, 8 inert, 0 out-of-scope, 0 deferred.
Examples: 10 encoded.
Footnotes (90): 31 have their own row, 12 encoded, 12 inert and 7 out-of-scope; the other 59 are inert.

## 6. The Examples where the text and the body differ

- **3.4 against Example 6.** 3.4 says the agencies "will challenge the restraint under the per se rule"; Example 6 says the agency "would be likely to challenge" it under the per se rule. The result keeps 3.4's words.
- **n.85 against Example 10.** n.85 says the agencies "may also apply" a merger analysis to a license that in substance transfers the rights, and cites Example 10; Example 10 says the agency "would apply" one because the license is "exclusive in fact". The fixture reads Example 10 as 5.7's main rule, an exclusive license in fact (fork F8).
- **Examples 1, 7 and 9** reach "unlikely to object" or "unlikely to challenge" from considerations. No rule is minted from them: the fixtures supply the finding of no likely anticompetitive effect, and assert that 3.4 and 4.2 then give "treat as reasonable" and "will not challenge".
- **Example 8.** "May conclude that the joint marketing ... constitutes horizontal price-fixing" is the classification of the restraint, which the caller supplies; once it is classed so, 3.4 says "will". Its "sufficiently apparent" effects are read as 3.4's "facially appears" (fork F11).

## 7. Checks

`L4=<unstable l4> L4_MAIN=/Users/mengwong/.cache/l4-main/112/l4 ./check.sh`, run 2026-11-25:

```
your l4:    unstable-20261125-a50cbd0 (unstable, a50cbd0, 2026-11-25)
main build: 1.6.112 (main, e4f4bf3, 2026-11-18)
module                      err  sat fail  ref  expected |  err  sat fail  ref  main
ip-framework.l4               0    0    0    0       0/0 |    0    0    0    0  same
ip-nouns.l4                   0    0    0    0       0/0 |    0    0    0    0  same
ip-restraints.l4              0    0    0    0       0/0 |    0    0    0    0  same
ip-rule-of-reason.l4          0    0    0    0       0/0 |    0    0    0    0  same
ip-safety-zone.l4             0    0    0    0       0/0 |    0    0    0    0  same
ip-tests-boundaries.l4        0  157    0    0     157/0 |    0  157    0    0  same
ip-tests-red.l4               4    0    4    0       0/4 |    4    0    4    0  same
ip-tests.l4                   0   54    0    0      54/0 |    0   54    0    0  same
TOTAL (8 modules): satisfied unstable 211, main 211; failed (positive controls) unstable 4, main 4
(a failed assertion is also an error; the expected column is satisfied/failed)
check.sh: all passed
```

The four errors in `ip-tests-red.l4` are its four failed assertions; no module has any other error.
The stable `l4 run` exits 0 on `ip-tests-red.l4` and the unstable one exits 1, which is why `check.sh` reads the diagnostics.
What it does not see: equal counts on the two builds can hide a different assertion failing on each side.

## 8. Fork register

Every reading below is **assumed, not ruled**.
Each has a fixture in `ip-tests-boundaries.l4` (or `ip-tests.l4` where named) on which the reading taken and its alternative give different answers.

| fork | the question | reading taken | the alternative | the text |
| --- | --- | --- | --- | --- |
| F1 | How is "collectively account for" computed? | The sum of each party's own share, each counted once. | Each party's share alone. | 4.3 "the licensor and its licensees collectively account for no more than twenty percent". Fixture: 15 + 10. |
| F2 | Must several affected markets each pass? | Each market considered must meet its own criterion; any one that fails puts the restraint outside, and the failing markets are named. | One market passing is enough, or the shares are pooled. | 4.3 "of each relevant market significantly affected". Fixture: goods markets at 15 and 21. |
| F3 | What is "independently controlled"? | Count distinct controllers, not technologies or entities. | Count items. | 4.3 "four or more independently controlled technologies". Fixture: four technologies, three controllers. |
| F4 | What is "facially anticompetitive"? | By the type of restraint (a type accorded per se treatment), or a restraint that would always or almost always reduce output or raise prices, whatever its integration. | Only a restraint that 3.4 would in fact treat per se (no integration). | n.59 "restraints that normally warrant per se treatment". Fixture: market division with integration is rule of reason under 3.4 yet outside the zone. |
| F5 | Is 3.4's per se list closed? | Open: the caller may class another type as accorded per se treatment. | Closed to the four named. | 3.4 "Among the restraints"; 5.1 "including". |
| F6 | With accurate share data, which criterion applies to a technology or research and development market? | The twenty percent test, as for goods markets. | The four-or-more count whenever enough others exist. | 4.3 [pdf page 26]: the counts apply "if market share data are unavailable or do not accurately represent competitive significance". Fixture: a technology market at 25 with five others. |
| F7 | A goods market with no usable share data? | NOTHING: the text names no criterion. | Inside, or outside. | 4.3 gives the substitute criteria only for technology and research and development markets. |
| F8 | n.85 transactions, and Example 10. | A license that only in substance transfers the rights: 5.7 "may also apply" a merger analysis, and whether the zone applies is NOTHING. Example 10 is read as an exclusive license in fact under 5.7's main rule. | n.86 ("such as those described in this section") takes the n.85 transactions out of the zone too. | 5.7, n.85, n.86, Example 10. |
| F9 | "Absent extraordinary circumstances". | A qualifier kept in the result's name; not an input. | An input that defeats the zone. | 4.3; the text never says what they are (open question 2). |
| F10 | No market to consider. | NOTHING. | Inside (no market fails). | 4.3 assumes at least one relevant market is significantly affected. |
| F11 | Example 8's "sufficiently apparent" and "sufficiently weak or not reasonably related". | 3.4's "facially appears ... always or almost always", with efficiencies not reasonably related. | A separate standard. | Example 8 [pdf page 29]; 3.4 [pdf page 20]. Fixture in `ip-tests.l4`. |
| F12 | 5.6: when are the offsetting effects considered? | Only once the agencies determine a likely significant reduction in incentives; the "In addition" sentence is read as part of that consideration. | Always reported. | 5.6 [pdf page 36] "If the Agencies determine ...". |
| F13 | Example 3's "comparable capabilities and incentives" and 4.3's research and development criterion. | The same count: independently controlled, not a party's, with the required assets and the incentive. | Two different tests. | Example 3 [pdf page 15]; 4.3 [pdf page 27]. |
| F14 | A trademark license and the zone. | NOTHING: the guidelines do not cover trademarks. | "Does not apply". | n.1. |
| F15 | When goods-market analysis alone is inadequate, are goods markets still considered? | Yes, every listed market is considered. | Only the technology and research and development markets. | 4.3 "by reference only to goods markets unless ...". Fixture: the goods-only rule in both directions. |
| F16 | Contradictory findings. | NOTHING, wherever two inputs the text treats as exclusive are both TRUE: a substitute that is also blocked (3.2.2); no likely effect and a facially harmful restraint with no related efficiency (3.4); reasonably necessary with a clear less restrictive alternative (4.2). | Let one win by the order of the sentences. | 3.2.2, 2.3; 3.4; 4.2. |
| F17 | 4.1.2: exclusive licensing with a horizontal relationship; a non-exclusive license with exclusive dealing. | NOTHING for both: "only if" states nothing on the other side, and exclusive dealing is a restraint on the licensee's conduct. | "May raise concerns" as a result; exclusive dealing not counted as a restraint. | 4.1.2 [pdf page 23]. |
| F18 | The equal share of Example 2's Discussion. | A general rule for technology markets ("will assign"), given only for a whole count of at least one. | Confined to Example 2. | Example 2 [pdf page 12], n.37. |
| F19 | Order of the zone's gates. | Coverage, then n.58, then the merger analysis, then condition (1), then condition (2). | Another order. A per se restraint outside any licensing arrangement then reads "does not apply", not "outside". | 4.3, n.58. Fixture: a per se restraint not in a licensing arrangement. |
| F20 | Section 6: fraud without the other elements proved. | Section 6 states nothing on it. | "May violate". | 6 [pdf page 37] "if all the elements otherwise necessary to establish a charge are proved". |
| F21 | 3.1 when no concern appears; Example 3 with fewer than four and no significant risk. | NOTHING for both. | "Will not challenge"; "unlikely to affect competition". | 3.1; Example 3. |

## 9. Open questions for a domain expert

1. Are the 2010 Horizontal Merger Guidelines, which 3.2.1 (n.31) and 5.7 rely on, still the agencies' merger guidelines? This was not checked (no fetching). The encoder's recollection, unverified and not relied on, is that the agencies issued new merger guidelines in December 2023; whether that changes how 5.7's "merger analysis" is done is outside this encoding either way.
2. What are "extraordinary circumstances" (4.3)? The text does not say; the result carries the qualifier (F9).
3. Does n.86 take n.85's in-substance transfers out of the safety zone (F8)?
4. With accurate share data in a technology or research and development market, do the agencies ever apply the four-or-more criteria instead (F6)?
5. What is a "large fraction of the potential research and development" (5.5)? No figure is given; it is an input.
6. How are shares in a research and development market measured when they are available (4.3 condition (2) applies to "each relevant market")? The text gives the twenty percent test but no measure.
7. The 2000 Collaborations guidelines were reported withdrawn on 11 December 2024. Does the withdrawal change how the agencies read Example 3, which cites them (n.43)?
8. Is the agencies' international guideline cited in n.14 (2017) still in force? Not checked.

## 10. Withdrawn and superseded guidelines

- **1995 IP Licensing Guidelines** (6 April 1995): replaced by these guidelines. Source: n.1 [pdf page 3], read at source.
- **2000 Antitrust Guidelines for Collaborations Among Competitors**: withdrawn 11 December 2024. Source: an FTC press release, **reported only** (the parent session's search summary; not fetched, not read). Cited by Example 3, n.43.
- **2010 Horizontal Merger Guidelines**: cited by n.31 and 5.7; status not checked (open question 1).
