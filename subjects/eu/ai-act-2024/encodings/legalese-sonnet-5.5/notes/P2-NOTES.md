# NOTES (P2): Article 4a, Articles 8 to 15 and Annex IV of the EU Artificial Intelligence Act

Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (the Omnibus).
Part P2 of the parallel encoding: lines 156-169, 262-373 and 1755-1782 of `eu-ai-act-2024-1689-consolidated-20260727.txt`, that is Article 4a, Articles 8 to 15 (Chapter III Section 2) and Annex IV.
Run `dst-aia-P2`; encoded in L4 (stable) with `l4` 1.6.110, compared on 1.6.109; `JL4_LIBRARY_PATH` unset throughout.

## Status header

- **The consolidated text is a rendering with no legal effect.** The Publications Office's consolidated version of 27.7.2026 is a documentation tool; only the acts published in the Official Journal are authentic.
  Every claim below is about the rendering the brief supplied.
- **Commencement is IN, assumed, not ruled.** The dates of application (Article 113 as enacted and as amended, Article 111(2)) are the keel's; I call its functions and restate no date.
  Whether the Commission's duties in Articles 11 and 15 follow any date at all is my reading (fork F-commission-no-gate), not a ruling.
- **Where the brief and `inputs/PLAN.md` differ, the brief governs, and I followed it.** The differences I acted on: the brief states the ruling of 2026-11-12 (a function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails) and asks for the count (iii) of functions that answer `NOTHING` because Article 111(2) saves a system, which PLAN.md's section 9 does not; the brief's wording of the breach-path rule ("Do not invent a deadline or a consequence the text does not state") decides which duties get a regulative rule (only where the text names the party and the act).
- **How each kind of claim was verified.**
  - Quotations and `@ref` locators: `python3 -I srcrefs.py check --strict` over the ten layer-1 modules, and `--refs` over every `P2-*.l4`, 0 problems each (re-run at the end of the run).
  - Assertions: `check.sh` with `L4` = 1.6.110 and `L4_MAIN` = 1.6.109: 39 modules, 1946 assertions satisfied, 0 errors, 0 failed, 0 refused, and the same four counts on 1.6.109 for every module (the full output is at the end of this file).
  - Traces: `check.sh` does not see a trace outcome.
    Every one of the 24 `#TRACE`s was run on both builds and its outcome compared with the `-- EXPECT` comment above it by `work/traces.py` (not shipped): 24 of 24 agree on both builds.
  - Coverage: `work/coverage.py` reads the quote lines of the layer-1 modules and the text of my ranges: counts: {'inert': 29, 'fork': 42, 'encoded': 81, 'repealed or blank in this text': 2} total: 154.
  - Expected values: each was written by hand from the quoted text before the run; no expected value was changed to match output.
    Three fixtures of my own were wrong in the run (a testing date later than a fixture's placement date in Article 9(8), a drawing-up date later than a fixture's placement date in Article 11(1), and a default for the Article 4a(1) flag of Article 10(6)): each was test data, not code or an expected value, and was fixed in the generator.
- **The seat layer** is six pairs of files (person, provider, deployer, notified, gpai, manufacturer; none for importer, distributor or authorised representative: see Seats).
  Each question has `@export` and `@desc`, is named `Under Article N, as <role phrase>, ...` (for the Annex, `Under Annex IV point M, as ...`), takes plain inputs and builds the core's records in a `WHERE`; none restates a rule.

## Files (P2)

| file | what it holds | definitions | assertions satisfied |
| --- | --- | --- | --- |
| `P2-section-2-gate.l4` | the gate of Chapter III Section 2 and the combinator (seam S8), hand-written | 2 | 0 |
| `P2-art-4a.l4` | Article 4a and Article 10(5) as enacted (the hand-over) | 5 | 0 |
| `P2-art-8.l4` | Article 8 | 5 | 0 |
| `P2-art-9.l4` | Article 9 | 15 | 0 |
| `P2-art-10.l4` | Article 10 | 11 | 0 |
| `P2-art-11.l4` | Article 11 | 15 | 0 |
| `P2-art-12.l4` | Article 12 | 3 | 0 |
| `P2-art-13.l4` | Article 13 | 4 | 0 |
| `P2-art-14.l4` | Article 14 | 8 | 0 |
| `P2-art-15.l4` | Article 15 | 11 | 0 |
| `P2-annex-iv.l4` | Annex IV | 10 | 0 |
| `P2-tests-art-4a.l4` | tests of `P2-art-4a.l4` (and its regulative rules, as traces) | 0 | 73 |
| `P2-tests-art-8.l4` | tests of `P2-art-8.l4` (and its regulative rules, as traces) | 0 | 53 |
| `P2-tests-art-9.l4` | tests of `P2-art-9.l4` (and its regulative rules, as traces) | 0 | 191 |
| `P2-tests-art-10.l4` | tests of `P2-art-10.l4` (and its regulative rules, as traces) | 0 | 132 |
| `P2-tests-art-11.l4` | tests of `P2-art-11.l4` (and its regulative rules, as traces) | 0 | 111 |
| `P2-tests-art-12.l4` | tests of `P2-art-12.l4` (and its regulative rules, as traces) | 0 | 47 |
| `P2-tests-art-13.l4` | tests of `P2-art-13.l4` (and its regulative rules, as traces) | 0 | 67 |
| `P2-tests-art-14.l4` | tests of `P2-art-14.l4` (and its regulative rules, as traces) | 0 | 105 |
| `P2-tests-art-15.l4` | tests of `P2-art-15.l4` (and its regulative rules, as traces) | 0 | 126 |
| `P2-tests-annex-iv.l4` | tests of `P2-annex-iv.l4` (and its regulative rules, as traces) | 0 | 156 |
| `P2-tests-versions.l4` | the version pairs of Articles 10 and 11 side by side (hand-written) | 0 | 31 |
| `P2-seat-person.l4`, `P2-cases-seat-person.l4` | the person seat: 6 questions; cases | 6 | 53 |
| `P2-seat-provider.l4`, `P2-cases-seat-provider.l4` | the provider seat: 69 questions; cases | 69 | 483 |
| `P2-seat-deployer.l4`, `P2-cases-seat-deployer.l4` | the deployer seat: 24 questions; cases | 24 | 167 |
| `P2-seat-notified.l4`, `P2-cases-seat-notified.l4` | the notified seat: 13 questions; cases | 13 | 100 |
| `P2-seat-gpai.l4`, `P2-cases-seat-gpai.l4` | the gpai seat: 4 questions; cases | 4 | 21 |
| `P2-seat-manufacturer.l4`, `P2-cases-seat-manufacturer.l4` | the manufacturer seat: 5 questions; cases | 5 | 30 |

`P2-section-2-gate.l4` has no tests file of its own: the gate is exercised by the date, Article 111(2), Article 2(2) and Article 2(13) cases of every requirement function (each module's first function carries the full set), and the combinator by the list cases of `Art 8(1) first sentence ...` and the Annex IV wrapper.

Layer 1: 89 definitions (functions and rules; counted by `MEANS`) in 11 modules; layer 2: 121 seat questions in six seat modules.
`PROGRESS.md` is the working log.
The generator that wrote most of these files is in `runs/dst-aia-P2/work/` and is not shipped; the files here are what it wrote.

## Coverage (P2)

One row per non-blank line of my ranges (the unit is the line: every paragraph, point, annex item and heading is one line of the text; a long line holds several sentences and each sentence's function is listed on its row).
Dispositions: `encoded` (a rule with a test, citing the line with `@ref`), `fork` (the row names the fork-register entry and the rule that encodes the reading taken), `inert` (reason 1 only: a heading or an amendment marker of the rendering), `repealed or blank in this text`.
Audit: text units counted by script in the three ranges: 154 (14 + 112 + 28 non-blank lines); rows in the table: 154 (before this table was built: 0, because it is built from the text by `coverage.py`, which fails on any line no layer-1 quote covers). counts: {'inert': 29, 'fork': 42, 'encoded': 81, 'repealed or blank in this text': 2} total: 154.

| line | text | disposition | L4 name or reason |
| --- | --- | --- | --- |
| 156 | ▼M1 INSERTED | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 157 | Article 4a | inert | reason 1: a heading |
| 158 | Processing of special categories of personal data for bias detection a... | inert | reason 1: a heading |
| 159 | 1. To the extent strictly necessary to ensure bias detection and corre... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-necessary, F-4a-1-gdpr, F-4a-handover) |
| 160 | (a) the bias detection and correction cannot be effectively fulfilled ... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 161 | (b) the special categories of personal data are subject to technical l... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 162 | (c) the special categories of personal data are subject to measures to... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 163 | (d) the special categories of personal data are not transmitted, trans... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 164 | (e) the special categories of personal data are deleted once the bias ... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 165 | (f) the records of processing activities pursuant to Regulations (EU) ... | fork | `Art 4a(1) as amended the provider may exceptionally process special categories of personal data` (P2-art-4a.l4); `Art 4a(1) the provider may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-1-conditions) |
| 166 | 2. Providers and deployers of other AI systems and models and deployer... | fork | `Art 4a(2) the provider or deployer may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-2-parties, F-4a-2-extent) |
| 167 | (a) such processing is strictly necessary to ensure bias detection and... | fork | `Art 4a(2) the provider or deployer may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-2-extent) |
| 168 | (b) all of the conditions and safeguards set out in paragraph 1 are ap... | fork | `Art 4a(2) the provider or deployer may exceptionally process special categories of personal data` (P2-art-4a.l4) (fork F-4a-2-extent) |
| 169 | This paragraph does not create any obligation to conduct such bias det... | encoded | `Art 4a(2) last sentence the paragraph creates an obligation to conduct bias detection and correction` (P2-art-4a.l4) |
| 262 | SECTION 2 | inert | reason 1: a heading |
| 263 | Requirements for high-risk AI systems | inert | reason 1: a heading |
| 264 | Article 8 | inert | reason 1: a heading |
| 265 | Compliance with the requirements | inert | reason 1: a heading |
| 266 | 1. High-risk AI systems shall comply with the requirements laid down i... | encoded | `Art 8(1) first sentence the high-risk AI system complies with the requirements laid down in this Section` (P2-art-8.l4); `Art 8(1) second sentence the risk management system has been taken into account when ensuring compliance with the requirements` (P2-art-8.l4) |
| 267 | 2. Where a product contains an AI system, to which the requirements of... | fork | `Art 8(2) first sentence the provider is responsible for ensuring that the product is fully compliant with all applicable requirements under Union harmonisation legislation` (P2-art-8.l4); `Art 8(2) the provider's duty to ensure that the product is fully compliant` (P2-art-8.l4); `Art 8(2) second sentence the provider has the choice of integrating the necessary testing and reporting processes, information and documentation into existing documentation and procedures` (P2-art-8.l4) (fork F-duty-where, F-ii-grants) |
| 268 | Article 9 | inert | reason 1: a heading |
| 269 | Risk management system | inert | reason 1: a heading |
| 270 | 1. A risk management system shall be established, implemented, documen... | encoded | `Art 9(1) a risk management system has been established, implemented, documented and maintained in relation to the high-risk AI system` (P2-art-9.l4) |
| 271 | 2. The risk management system shall be understood as a continuous iter... | encoded | `Art 9(2) the risk management system is a continuous iterative process comprising the following steps` (P2-art-9.l4) |
| 272 | (a) the identification and analysis of the known and the reasonably fo... | encoded | `Art 9(2) the risk management system is a continuous iterative process comprising the following steps` (P2-art-9.l4) |
| 273 | (b) the estimation and evaluation of the risks that may emerge when th... | encoded | `Art 9(2) the risk management system is a continuous iterative process comprising the following steps` (P2-art-9.l4) |
| 274 | (c) the evaluation of other risks possibly arising, based on the analy... | encoded | `Art 9(2) the risk management system is a continuous iterative process comprising the following steps` (P2-art-9.l4) |
| 275 | (d) the adoption of appropriate and targeted risk management measures ... | encoded | `Art 9(2) the risk management system is a continuous iterative process comprising the following steps` (P2-art-9.l4) |
| 276 | 3. The risks referred to in this Article shall concern only those whic... | encoded | `Art 9(3) the risks referred to in Article 9 concern only those which may be reasonably mitigated or eliminated` (P2-art-9.l4) |
| 277 | 4. The risk management measures referred to in paragraph 2, point (d),... | encoded | `Art 9(4) the risk management measures give due consideration to the combined application of the requirements` (P2-art-9.l4) |
| 278 | 5. The risk management measures referred to in paragraph 2, point (d),... | encoded | `Art 9(5) first subparagraph the residual risk is judged to be acceptable` (P2-art-9.l4) |
| 279 | In identifying the most appropriate risk management measures, the foll... | encoded | `Art 9(5) second subparagraph in identifying the most appropriate risk management measures the following are ensured` (P2-art-9.l4) |
| 280 | (a) elimination or reduction of risks identified and evaluated pursuan... | encoded | `Art 9(5) second subparagraph in identifying the most appropriate risk management measures the following are ensured` (P2-art-9.l4) |
| 281 | (b) where appropriate, implementation of adequate mitigation and contr... | encoded | `Art 9(5) second subparagraph in identifying the most appropriate risk management measures the following are ensured` (P2-art-9.l4) |
| 282 | (c) provision of information required pursuant to Article 13 and, wher... | encoded | `Art 9(5) second subparagraph in identifying the most appropriate risk management measures the following are ensured` (P2-art-9.l4) |
| 283 | With a view to eliminating or reducing risks related to the use of the... | encoded | `Art 9(5) third subparagraph due consideration is given to the deployer's knowledge and the context of use` (P2-art-9.l4) |
| 284 | 6. High-risk AI systems shall be tested for the purpose of identifying... | encoded | `Art 9(6) first sentence the high-risk AI system has been tested to identify the most appropriate and targeted risk management measures` (P2-art-9.l4); `Art 9(6) second sentence the testing ensures consistent performance and compliance with the requirements of this Section` (P2-art-9.l4) |
| 285 | 7. Testing procedures may include testing in real-world conditions in ... | fork | `Art 9(7) testing procedures may include testing in real-world conditions in accordance with Article 60` (P2-art-9.l4) (fork F-ii-grants) |
| 286 | 8. The testing of high-risk AI systems shall be performed, as appropri... | encoded | `Art 9(8) first sentence the testing of the high-risk AI system is performed throughout development and in any event before placing on the market` (P2-art-9.l4); `Art 9(8) second sentence the testing is carried out against prior defined metrics and probabilistic thresholds` (P2-art-9.l4) |
| 287 | 9. When implementing the risk management system as provided for in par... | fork | `Art 9(9) the provider has given consideration to the adverse impact on persons under the age of 18 and other vulnerable groups` (P2-art-9.l4); `Art 9(9) the provider's duty to give consideration to the adverse impact on persons under the age of 18 and other vulnerable groups` (P2-art-9.l4) (fork F-duty-where) |
| 288 | 10. For providers of high-risk AI systems that are subject to requirem... | fork | `Art 9(10) the aspects provided in paragraphs 1 to 9 may be part of, or combined with, the risk management procedures established pursuant to other Union law` (P2-art-9.l4) (fork F-ii-grants) |
| 289 | Article 10 | inert | reason 1: a heading |
| 290 | Data and data governance | inert | reason 1: a heading |
| 291 | ▼M1 REPLACED | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 292 | 1. High-risk AI systems which make use of techniques involving the tra... | fork | `Art 10(1) as amended the high-risk AI system is developed on the basis of data sets that meet the quality criteria` (P2-art-10.l4); `Art 10(1) the high-risk AI system is developed on the basis of data sets that meet the quality criteria` (P2-art-10.l4) (fork F-duty-scope) |
| 293 | ▼B | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 294 | 2. Training, validation and testing data sets shall be subject to data... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 295 | (a) the relevant design choices; | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 296 | (b) data collection processes and the origin of data, and in the case ... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 297 | (c) relevant data-preparation processing operations, such as annotatio... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 298 | (d) the formulation of assumptions, in particular with respect to the ... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 299 | (e) an assessment of the availability, quantity and suitability of the... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 300 | (f) examination in view of possible biases that are likely to affect t... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 301 | (g) appropriate measures to detect, prevent and mitigate possible bias... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 302 | (h) the identification of relevant data gaps or shortcomings that prev... | encoded | `Art 10(2) the data sets are subject to data governance and management practices appropriate for the intended purpose, which concern the following` (P2-art-10.l4) |
| 303 | 3. Training, validation and testing data sets shall be relevant, suffi... | encoded | `Art 10(3) first sentence the data sets are relevant, sufficiently representative, and to the best extent possible, free of errors and complete` (P2-art-10.l4); `Art 10(3) second sentence the data sets have the appropriate statistical properties` (P2-art-10.l4); `Art 10(3) third sentence the characteristics of the data sets may be met at the level of individual data sets or of a combination thereof` (P2-art-10.l4) |
| 304 | 4. Data sets shall take into account, to the extent required by the in... | encoded | `Art 10(4) the data sets take into account the characteristics or elements particular to the setting of use` (P2-art-10.l4) |
| 305 | ▼M1 DELETED | repealed or blank in this text | the Omnibus deleted Article 10(5): its as-enacted text is encoded as `Art 10(5) as enacted the provider may exceptionally process special categories of personal data` (P2-art-4a.l4), next to Article 4a(1) which took it over |
| 306 | ————— | repealed or blank in this text | the blank left by the deleted paragraph 5 (see the row above) |
| 307 | ▼M1 REPLACED | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 308 | 6. For the development of high-risk AI systems not using techniques in... | fork | `Art 10(6) as amended the paragraph applies to the data set` (P2-art-10.l4); `Art 10(6) the paragraph applies to the data set` (P2-art-10.l4) (fork F-duty-scope) |
| 309 | ▼B | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 310 | Article 11 | inert | reason 1: a heading |
| 311 | Technical documentation | inert | reason 1: a heading |
| 312 | 1. The technical documentation of a high-risk AI system shall be drawn... | fork | `Art 11(1) first subparagraph the technical documentation is drawn up before the placing on the market and kept up to date` (P2-art-11.l4) (fork F-party-less) |
| 313 | ▼M1 REPLACED | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 314 | That technical documentation shall be drawn up in such a way as to dem... | fork | `Art 11(1) second subparagraph first sentence the technical documentation is drawn up in such a way as to demonstrate compliance and to inform` (P2-art-11.l4); `Art 11(1) second subparagraph second sentence the technical documentation contains at a minimum the elements set out in Annex IV` (P2-art-11.l4); `Art 11(1) as amended the provider may provide the elements of the technical documentation in a simplified manner` (P2-art-11.l4); `Art 11(1) the provider may provide the elements of the technical documentation in a simplified manner` (P2-art-11.l4); `Art 11(1) as amended the Commission has established a simplified technical documentation form targeted at the needs of SMEs and SMCs` (P2-art-11.l4); `Art 11(1) the provider that opts for the simplified manner has used the simplified technical documentation form` (P2-art-11.l4); `Art 11(1) the notified body has accepted the simplified technical documentation form for the purposes of the conformity assessment` (P2-art-11.l4); `Art 11(1) the SME's or SMC's duty to use the form` (P2-art-11.l4); `Art 11(1) the notified body's duty to accept the form` (P2-art-11.l4); `Art 11(1) the Commission's duty to establish the simplified technical documentation form` (P2-art-11.l4) (fork F-11-1-versions, F-duty-where, F-ii-grants) |
| 315 | ▼B | inert | reason 1: an amendment marker of the consolidated rendering, not operative text |
| 316 | 2. Where a high-risk AI system related to a product covered by the Uni... | fork | `Art 11(2) a single set of technical documentation has been drawn up containing all the information` (P2-art-11.l4) (fork F-duty-where) |
| 317 | 3. The Commission is empowered to adopt delegated acts in accordance w... | fork | `Art 11(3) the Commission may adopt delegated acts to amend Annex IV` (P2-art-11.l4) (fork F-11-3-necessary, F-ii-grants) |
| 318 | Article 12 | inert | reason 1: a heading |
| 319 | Record-keeping | inert | reason 1: a heading |
| 320 | 1. High-risk AI systems shall technically allow for the automatic reco... | encoded | `Art 12(1) the high-risk AI system technically allows for the automatic recording of events over the lifetime of the system` (P2-art-12.l4) |
| 321 | 2. In order to ensure a level of traceability of the functioning of a ... | encoded | `Art 12(2) the logging capabilities enable the recording of events relevant for the purposes listed` (P2-art-12.l4) |
| 322 | (a) identifying situations that may result in the high-risk AI system ... | encoded | `Art 12(2) the logging capabilities enable the recording of events relevant for the purposes listed` (P2-art-12.l4) |
| 323 | (b) facilitating the post-market monitoring referred to in Article 72;... | encoded | `Art 12(2) the logging capabilities enable the recording of events relevant for the purposes listed` (P2-art-12.l4) |
| 324 | (c) monitoring the operation of high-risk AI systems referred to in Ar... | encoded | `Art 12(2) the logging capabilities enable the recording of events relevant for the purposes listed` (P2-art-12.l4) |
| 325 | 3. For high-risk AI systems referred to in point 1 (a), of Annex III, ... | fork | `Art 12(3) the logging capabilities provide, at a minimum, the recording listed for systems referred to in point 1 (a) of Annex III` (P2-art-12.l4) (fork F-A1A-seam, F-duty-scope) |
| 326 | (a) recording of the period of each use of the system (start date and ... | encoded | `Art 12(3) the logging capabilities provide, at a minimum, the recording listed for systems referred to in point 1 (a) of Annex III` (P2-art-12.l4) |
| 327 | (b) the reference database against which input data has been checked b... | encoded | `Art 12(3) the logging capabilities provide, at a minimum, the recording listed for systems referred to in point 1 (a) of Annex III` (P2-art-12.l4) |
| 328 | (c) the input data for which the search has led to a match; | encoded | `Art 12(3) the logging capabilities provide, at a minimum, the recording listed for systems referred to in point 1 (a) of Annex III` (P2-art-12.l4) |
| 329 | (d) the identification of the natural persons involved in the verifica... | encoded | `Art 12(3) the logging capabilities provide, at a minimum, the recording listed for systems referred to in point 1 (a) of Annex III` (P2-art-12.l4) |
| 330 | Article 13 | inert | reason 1: a heading |
| 331 | Transparency and provision of information to deployers | inert | reason 1: a heading |
| 332 | 1. High-risk AI systems shall be designed and developed in such a way ... | encoded | `Art 13(1) first sentence the high-risk AI system is designed and developed so that its operation is sufficiently transparent` (P2-art-13.l4); `Art 13(1) second sentence an appropriate type and degree of transparency is ensured with a view to compliance with the obligations of the provider and deployer` (P2-art-13.l4) |
| 333 | 2. High-risk AI systems shall be accompanied by instructions for use i... | encoded | `Art 13(2) the high-risk AI system is accompanied by instructions for use that include concise, complete, correct and clear information` (P2-art-13.l4) |
| 334 | 3. The instructions for use shall contain at least the following infor... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 335 | (a) the identity and the contact details of the provider and, where ap... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 336 | (b) the characteristics, capabilities and limitations of performance o... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 337 | (i) its intended purpose; | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 338 | (ii) the level of accuracy, including its metrics, robustness and cybe... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 339 | (iii) any known or foreseeable circumstance, related to the use of the... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 340 | (iv) where applicable, the technical capabilities and characteristics ... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 341 | (v) when appropriate, its performance regarding specific persons or gr... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 342 | (vi) when appropriate, specifications for the input data, or any other... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 343 | (vii) where applicable, information to enable deployers to interpret t... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 344 | (c) the changes to the high-risk AI system and its performance which h... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 345 | (d) the human oversight measures referred to in Article 14, including ... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 346 | (e) the computational and hardware resources needed, the expected life... | encoded | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) |
| 347 | (f) where relevant, a description of the mechanisms included within th... | fork | `Art 13(3) the instructions for use contain at least the following information` (P2-art-13.l4) (fork F-qualifier-fold) |
| 348 | Article 14 | inert | reason 1: a heading |
| 349 | Human oversight | inert | reason 1: a heading |
| 350 | 1. High-risk AI systems shall be designed and developed in such a way,... | encoded | `Art 14(1) the high-risk AI system is designed and developed so that it can be effectively overseen by natural persons` (P2-art-14.l4) |
| 351 | 2. Human oversight shall aim to prevent or minimise the risks to healt... | encoded | `Art 14(2) human oversight aims to prevent or minimise the risks to health, safety or fundamental rights` (P2-art-14.l4) |
| 352 | 3. The oversight measures shall be commensurate with the risks, level ... | encoded | `Art 14(3) the oversight measures are commensurate with the risks and ensured through one or both types of measures` (P2-art-14.l4) |
| 353 | (a) measures identified and built, when technically feasible, into the... | encoded | `Art 14(3) the oversight measures are commensurate with the risks and ensured through one or both types of measures` (P2-art-14.l4) |
| 354 | (b) measures identified by the provider before placing the high-risk A... | encoded | `Art 14(3) the oversight measures are commensurate with the risks and ensured through one or both types of measures` (P2-art-14.l4) |
| 355 | 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-ris... | fork | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) (fork F-qualifier-fold) |
| 356 | (a) to properly understand the relevant capacities and limitations of ... | encoded | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) |
| 357 | (b) to remain aware of the possible tendency of automatically relying ... | encoded | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) |
| 358 | (c) to correctly interpret the high-risk AI system’s output, taking in... | encoded | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) |
| 359 | (d) to decide, in any particular situation, not to use the high-risk A... | encoded | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) |
| 360 | (e) to intervene in the operation of the high-risk AI system or interr... | encoded | `Art 14(4) the high-risk AI system is provided to the deployer so that the natural persons to whom human oversight is assigned are enabled to do the following` (P2-art-14.l4) |
| 361 | 5. For high-risk AI systems referred to in point 1(a) of Annex III, th... | fork | `Art 14(5) first subparagraph the measures ensure that no action or decision is taken unless the identification is separately verified and confirmed by at least two natural persons` (P2-art-14.l4); `Art 14(5) the deployer is barred from taking an action or decision on the basis of the identification` (P2-art-14.l4); `Art 14(5) the deployer's prohibition on acting on an identification that is not separately verified` (P2-art-14.l4) (fork F-A1A-seam, F-14-5-shape, F-duty-scope) |
| 362 | The requirement for a separate verification by at least two natural pe... | fork | `Art 14(5) second subparagraph the requirement for a separate verification by at least two natural persons applies` (P2-art-14.l4); `Art 14(5) the deployer is barred from taking an action or decision on the basis of the identification` (P2-art-14.l4); `Art 14(5) the deployer's prohibition on acting on an identification that is not separately verified` (P2-art-14.l4) (fork F-14-5-shape) |
| 363 | Article 15 | inert | reason 1: a heading |
| 364 | Accuracy, robustness and cybersecurity | inert | reason 1: a heading |
| 365 | 1. High-risk AI systems shall be designed and developed in such a way ... | encoded | `Art 15(1) the high-risk AI system achieves an appropriate level of accuracy, robustness and cybersecurity and performs consistently` (P2-art-15.l4) |
| 366 | 2. To address the technical aspects of how to measure the appropriate ... | encoded | `Art 15(2) the Commission has encouraged the development of benchmarks and measurement methodologies` (P2-art-15.l4); `Art 15(2) the Commission's duty to encourage the development of benchmarks and measurement methodologies` (P2-art-15.l4) |
| 367 | 3. The levels of accuracy and the relevant accuracy metrics of high-ri... | encoded | `Art 15(3) the levels of accuracy and the relevant accuracy metrics are declared in the accompanying instructions of use` (P2-art-15.l4) |
| 368 | 4. High-risk AI systems shall be as resilient as possible regarding er... | encoded | `Art 15(4) first subparagraph first sentence the high-risk AI system is as resilient as possible regarding errors, faults or inconsistencies` (P2-art-15.l4); `Art 15(4) first subparagraph second sentence technical and organisational measures have been taken in this regard` (P2-art-15.l4) |
| 369 | The robustness of high-risk AI systems may be achieved through technic... | encoded | `Art 15(4) second subparagraph the robustness may be achieved through technical redundancy solutions` (P2-art-15.l4) |
| 370 | High-risk AI systems that continue to learn after being placed on the ... | fork | `Art 15(4) third subparagraph the high-risk AI system that continues to learn is developed to eliminate or reduce the risk of feedback loops` (P2-art-15.l4) (fork F-duty-scope) |
| 371 | 5. High-risk AI systems shall be resilient against attempts by unautho... | encoded | `Art 15(5) first subparagraph the high-risk AI system is resilient against attempts by unauthorised third parties to alter its use, outputs or performance` (P2-art-15.l4) |
| 372 | The technical solutions aiming to ensure the cybersecurity of high-ris... | encoded | `Art 15(5) second subparagraph the technical solutions aiming to ensure cybersecurity are appropriate to the relevant circumstances and the risks` (P2-art-15.l4) |
| 373 | The technical solutions to address AI specific vulnerabilities shall i... | fork | `Art 15(5) third subparagraph the technical solutions to address AI specific vulnerabilities include measures against the listed attacks` (P2-art-15.l4) (fork F-15-5-list, F-qualifier-fold) |
| 1755 | ANNEX IV | inert | reason 1: a heading |
| 1756 | Technical documentation referred to in Article 11(1) | inert | reason 1: a heading |
| 1757 | The technical documentation referred to in Article 11(1) shall contain... | fork | `Annex IV the technical documentation contains at least the following information` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1758 | 1. A general description of the AI system including: | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1759 | (a) its intended purpose, the name of the provider and the version of ... | fork | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1760 | (b) how the AI system interacts with, or can be used to interact with,... | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1761 | (c) the versions of relevant software or firmware, and any requirement... | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1762 | (d) the description of all the forms in which the AI system is placed ... | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1763 | (e) the description of the hardware on which the AI system is intended... | fork | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1764 | (f) where the AI system is a component of products, photographs or ill... | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1765 | (g) a basic description of the user-interface provided to the deployer... | fork | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1766 | (h) instructions for use for the deployer, and a basic description of ... | encoded | `Annex IV point 1 the technical documentation contains a general description of the AI system` (P2-annex-iv.l4) |
| 1767 | 2. A detailed description of the elements of the AI system and of the ... | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1768 | (a) the methods and steps performed for the development of the AI syst... | fork | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1769 | (b) the design specifications of the system, namely the general logic ... | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1770 | (c) the description of the system architecture explaining how software... | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1771 | (d) where relevant, the data requirements in terms of datasheets descr... | fork | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1772 | (e) assessment of the human oversight measures needed in accordance wi... | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1773 | (f) where applicable, a detailed description of pre-determined changes... | fork | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1774 | (g) the validation and testing procedures used, including information ... | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1775 | (h) cybersecurity measures put in place; | encoded | `Annex IV point 2 the technical documentation contains a detailed description of the elements of the AI system and of the process for its development` (P2-annex-iv.l4) |
| 1776 | 3. Detailed information about the monitoring, functioning and control ... | fork | `Annex IV point 3 the technical documentation contains detailed information about the monitoring, functioning and control of the AI system` (P2-annex-iv.l4) (fork F-qualifier-fold) |
| 1777 | 4. A description of the appropriateness of the performance metrics for... | encoded | `Annex IV point 4 the technical documentation contains a description of the appropriateness of the performance metrics` (P2-annex-iv.l4) |
| 1778 | 5. A detailed description of the risk management system in accordance ... | encoded | `Annex IV point 5 the technical documentation contains a detailed description of the risk management system` (P2-annex-iv.l4) |
| 1779 | 6. A description of relevant changes made by the provider to the syste... | encoded | `Annex IV point 6 the technical documentation contains a description of relevant changes made by the provider to the system` (P2-annex-iv.l4) |
| 1780 | 7. A list of the harmonised standards applied in full or in part the r... | fork | `Annex IV point 7 the technical documentation contains a list of the harmonised standards applied or a description of the solutions adopted` (P2-annex-iv.l4) (fork F-IV-7-disjunction) |
| 1781 | 8. A copy of the EU declaration of conformity referred to in Article 4... | encoded | `Annex IV point 8 the technical documentation contains a copy of the EU declaration of conformity` (P2-annex-iv.l4) |
| 1782 | 9. A detailed description of the system in place to evaluate the AI sy... | encoded | `Annex IV point 9 the technical documentation contains a detailed description of the post-market evaluation system and the monitoring plan` (P2-annex-iv.l4) |

`inert` rows: 29, all reason 1 (22 headings: Section 2 and its title, the Article numbers and titles of 4a, 8 to 15 and Annex IV, and the Annex title; 7 amendment markers `▼M1 INSERTED`, `▼M1 REPLACED`, `▼B`).
There is no reason 2 and no reason 3 row.
The two `repealed or blank in this text` rows (305, 306) are Article 10(5), deleted by the Omnibus: the text shows `▼M1 DELETED` and a dash line.
Its as-enacted text is encoded, from the base file, in `P2-art-4a.l4` as `Art 10(5) as enacted ...`; see Versions.

## Fork register (P2)

One entry per site where the text reads two or more ways with different outcomes; the row of the coverage table names the entry.
Each entry gives the provision, the function, the answer taken, the other reading, and the text that licenses each.
At the split sites the licence names the Guide line or ruling it relies on and quotes its words: "Guide line N" is line N of `inputs/ENCODING-GUIDE.md` and "Brief line N" is line N of `BRIEF.md`, both this run's copies.
The ruling of 2026-11-12 is in the brief (Brief line 34), not in the Guide copy; its three limits are cited as limit (1), (2) and (3).
Every quotation is the file's own text, looked up by script when this file is generated.

| id | provision | function | answer taken | other reading | licence |
| --- | --- | --- | --- | --- | --- |
| F-bare-shall | every flat "shall" requirement of Articles 8 to 15 and of Annex IV (for example 9(1), 12(1), 13(1), 15(1)) | each requirement function | an unmet flat "shall" answers `JUST FALSE`, with the quoted words in a FALSE-kind comment | `NOTHING`: a requirement stated without "if" or "only" does not say no to the case | the brief's list of what the text says no to in its own words includes "a flat negative" and the "shall" is its positive form; reading (a) of the brief (a failed element counts as the text's no). Not on a coverage row: it is the default of the whole of Chapter III Section 2. |
| F-duty-where | 8(2) first sentence ("Where a product contains an AI system ..."), 9(9) ("When implementing the risk management system ..."), 10(1) ("whenever such data sets are used", both versions), 11(1) use of the form ("Where an SME ... opts ..."), 11(2) ("Where a high-risk AI system related to a product ... is placed on the market"), 11(1) notified bodies ("Notified bodies shall accept the form", which has no "where" of its own) | `Art 8(2) first sentence ...`, `Art 9(9) ...`, `Art 10(1) ...` (both versions), `Art 11(1) the provider that opts ...`, `Art 11(2) ...`, `Art 11(1) the notified body has accepted ...` | a duty whose "where", "when" or "whenever" is unmet answers `NOTHING` (the duty does not arise, so the compliance question is not answered), and `JUST FALSE` where the duty arose and is not met; six sites. At the acceptance site the gate (the documentation was provided on the form) is not in the sentence's words: the sentence is silent on that case, and the answer is `NOTHING` | `JUST FALSE`: the Guide's rule for a "where", "when" or "whenever" condition that fails, applied to a duty; the function named "the provider has ensured ..." would then say the provider has not ensured something it was never asked to | Relies on Guide line 95 alone, which leaves the decision to the encoder: "Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment" (Guide line 95); it lists "a duty whose "if" or "where" is unmet" (Guide line 95) among them and asks for one fork line each. It gives no answer. What does NOT support `NOTHING` here: the grant line ("limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87)) is about a grant or a prohibition, not a duty. What points the other way: "a "where ..." condition: when it fails the answer is `JUST FALSE`" (Guide line 93); ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" (Guide line 94); and limit (2) of the ruling of 2026-11-12 (not in the Guide copy), "Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question." (Brief line 34) which can be read as keeping `JUST FALSE` for a duty. I kept the first pass's answer because line 95 supports a decision either way and I was not to change an answer a Guide line supports. A reviewer who reads limit (2) strictly would change six functions and the seat questions and cases that call them (provider: 8(2) first sentence, 9(9), 10(1), 11(1) use, 11(2); manufacturer: 8(2) first sentence, 11(2); notified body: 11(1) acceptance). At the acceptance site the Guide's words are "leaves a term undefined, is silent, points outside the sources" (Guide line 87) (silent). Listed under Marginal readings and flagged in the final report. |
| F-duty-scope | 10(1) ("which make use of techniques involving the training of AI models with data"), 10(6) ("not using techniques ..."), 12(3) ("For high-risk AI systems referred to in point 1(a) of Annex III"), 14(5) (the same), 15(4) third subparagraph ("that continue to learn after being placed on the market") | `Art 10(1)`, `Art 10(6)`, `Art 12(3)`, `Art 14(5)` (three functions), `Art 15(4) third subparagraph` | a duty the text limits to a class of system answers `NOTHING` for a system outside the class | `JUST FALSE` (the text says what the system "shall" do only for the class: outside it the requirement is not met) | Relies on the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" (Guide line 93). Each site limits the duty to a class of system with no "only", so outside the class the answer is `NOTHING`. The bar of 14(5) (split site (i), an unmet element of a prohibition) is also a prohibition limited in its own wording, so the grant line applies too: the text "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87). One exception inside these sites: 10(6) also says "apply only to the testing data sets", so a data set that is not a testing data set answers `JUST FALSE`, which I read as "a list the text closes with "only"" (Guide line 86); that is a stretch ("apply only to" is not literally a list) and is listed under Marginal readings. Six sites (10(1) and 10(6) count once each across their two versions). |
| F-party-less | 9(8), 11(1) first subparagraph, 11(2), 12 to 15 and Annex IV: every provision in the passive or with a system as its subject ("High-risk AI systems shall ...", "The technical documentation ... shall be drawn up") | the decision functions only | no regulative rule where the text names no party and no act; the duty is encoded as a decision function over the facts | a regulative rule with `Provider` as the party (Article 16(a) puts the Section's requirements on providers, but Article 16 is outside my ranges; the keel's Article 111(1) took the keel's `Operator` for the same reason) | the brief: a regulative rule "where the text names the party and the act"; "Do not invent an actor, a deadline, a remedy or a consequence the text does not state". |
| F-4a-1-necessary | 4a(1) "To the extent strictly necessary to ensure bias detection and correction ..."; 10(5) as enacted ("To the extent that it is strictly necessary ...") | `Art 4a(1) ...`, `Art 10(5) as enacted ...` | a grant limited by "to the extent": when the processing is not strictly necessary the function answers `NOTHING` (split site (ii)) | `JUST FALSE` (reading the "to the extent" gate as the periods ruling's "where" condition, item (b)) | Relies on the grant line, which gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87). The extent limit is also, as I read it, a scope limit: "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" (Guide line 93). The gate words are "to the extent", not "where", "when" or "upon", so the brief's limit (3) does not hold this site back, and limit (1) of the ruling of 2026-11-12 (not in the Guide copy) applies: "Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading." (Brief line 34) |
| F-4a-1-conditions | 4a(1) points (a) to (f), and the safeguards ("subject to appropriate safeguards ...") | `Art 4a(1) ...` | an unmet condition or safeguard answers `JUST FALSE`: "all the following conditions shall be met in order for such processing to occur" closes the gate | `NOTHING` (the grant is silent on processing that meets some conditions) | Relies on limit (2) of the ruling of 2026-11-12 (not in the Guide copy): "Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question." (Brief line 34) "In order for" is not one of the words that limit names; I read it as "only if" (the processing occurs only if the conditions are met), which is my reading and is listed under Marginal readings. The nearest Guide line is "a condition the text introduces with "if", "only if", "as long as" or "unless"" (Guide line 86). |
| F-4a-1-gdpr | 4a(1) "In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable, all the following conditions ..." | `Art 4a(1) ...` | compliance with those provisions is a further condition (a plain yes/no input; unmet answers `JUST FALSE`) | a reminder that the other instruments also apply, adding no condition of this Article | "In addition to ... all the following conditions shall be met in order for such processing to occur": the sentence puts the other provisions alongside the conditions that close the gate. Relies on the same limit (2) as F-4a-1-conditions. |
| F-4a-2-parties | 4a(2) "Providers and deployers of other AI systems and models and deployers of high-risk AI systems" | `Art 4a(2) ...` | three kinds of party: a provider or a deployer of an AI system or model that is not a high-risk AI system, and a deployer of a high-risk AI system; a provider of a high-risk AI system is under paragraph 1 and answers `NOTHING` here | "other" qualifies only the first two (providers and deployers of other systems and models) and the provider of a high-risk system is outside paragraph 2 because it is not named | the list as written; paragraph 1 names the providers of high-risk AI systems. |
| F-4a-2-extent | 4a(2) "may exceptionally process ... to the extent that: (a) such processing is strictly necessary ...; and (b) all of the conditions and safeguards set out in paragraph 1 are applied" | `Art 4a(2) ...` | (a) a grant limited by "to the extent": not strictly necessary answers `NOTHING` (split site (ii)); (b) paragraph 1's conditions and safeguards imported with their closure: not applied answers `JUST FALSE` | both limbs are the grant's own limit and answer `NOTHING` | For (a), relies on the grant line, which gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87), and on "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" (Guide line 93); limit (1) of the ruling of 2026-11-12 (not in the Guide copy) applies: "Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading." (Brief line 34) For (b), relies on paragraph 1's closure read through limit (2), as at F-4a-1-conditions; clause (b) is introduced by "to the extent that", not by "if", "only if", "as long as" or "unless", so no Guide line fits it exactly, and it is listed under Marginal readings. |
| F-4a-handover | the hand-over from Article 10(5) as enacted to Article 4a(1) as amended | `Art 4a(1) the provider may exceptionally process special categories of personal data` (the dispatcher) | one dispatcher on the version in force: as enacted, Article 10(5) in Chapter III (its date from Article 113 as enacted by route); as amended, Article 4a(1) in Chapter I (from 2 February 2025) | dispatch both versions through the Chapter I group | Article 10(5) as enacted sat in Chapter III Section 2, whose date was Article 113(c)'s; Article 4a is in Chapter I (Art 113(a)). |
| F-10-5-dead | every dispatcher of Chapter III Sections 1 to 3 (10(1), 10(6), 11(1) SME liberty) and the amended-only sentences of 11(1) | the dispatchers | the as-enacted branch is written and each as-enacted text is tested through its own function; no date reaches the branch through the gate | omit the as-enacted branch as dead | as enacted Chapter III Section 2 applied from 2 August 2026 (Annex III) or 2 August 2027 (Annex I); the Omnibus took effect on 27 July 2026, so no date at which the Section applied was governed by the old text; the brief says to encode both texts. |
| F-11-1-versions | 11(1) second subparagraph (REPLACED) | `Art 11(1) the provider may provide ...` and its as-enacted / as-amended functions; the Commission's form | the two sentences unchanged in substance are one function ("The" became "That"); the three changed or new ones are each in both versions | one dispatcher for the whole subparagraph | the base file (lines 781-782) against the consolidated line 314. |
| F-11-3-necessary | 11(3) "is empowered to adopt delegated acts ... where necessary, to ensure" | `Art 11(3) the Commission may adopt delegated acts to amend Annex IV` | a power gated by the word "where" ("where necessary"): when it is not necessary the function answers `JUST FALSE` (split site (ii); the "where" group of the brief's limit (3), count 1; CHANGED in the second pass from `NOTHING`) | `NOTHING` (the grant line, and limit (1) of the ruling of 2026-11-12) | Relies on the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" (Guide line 93). Limit (3) of the ruling of 2026-11-12 (not in the Guide copy) says not to decide this group myself and to "leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer)" (Brief line 34). The first pass answered `NOTHING` under limit (1); limit (3) leaves a "may" gated by "where" to the Guide's rulings, so the answer is now `JUST FALSE`, and the assertion is restated in `P2-tests-art-11.l4` with `-- RECONCILED 2026-11-17`. The other reading is the grant line, which gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87): a question for a lawyer (Marginal readings). |
| F-ii-grants | 8(2) second sentence ("shall have a choice of integrating ... into documentation and procedures that already exist and are required under" the Section A legislation), 9(7) ("may include testing in real-world conditions in accordance with Article 60"), 9(10) ("For providers ... that are subject to requirements ... under other relevant provisions of Union law, ... may be part of, or combined with"), 11(1) SME liberty ("SMEs, including start-ups, and SMCs, may provide") | the corresponding liberty functions | each answers `NOTHING` when its gate fails (the case falls outside the limit the text puts on the liberty) | `JUST FALSE` | Relies on the grant line, which gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87). The gates, in the text's own words: 8(2), a relative clause ("that already exist and are required under"); 9(7), a reference outside my ranges ("in accordance with Article 60"; also within "leaves a term undefined, is silent, points outside the sources" (Guide line 87)); 9(10) and 11(1), limits on who, which I read as scope limits: "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" (Guide line 93). None of the four is introduced by "where", "when" or "upon", so limit (3) of the ruling of 2026-11-12 does not hold them back, and its limit (1) (not in the Guide copy) applies: "Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading." (Brief line 34) Count for limit (3): "may" functions gated by "where", "when" or "upon": 1 (11(3), F-11-3-necessary); "entitled"-named functions: 0. See Split sites. |
| F-A1A-seam | 12(3) and 14(5) "high-risk AI systems referred to in point 1(a) of Annex III" | `Art 12(3)`, `Art 14(5)` (three functions) and the rule | a plain yes/no input: Annex III is outside my ranges and the plan has no seam for it | take the keel's route and ask which point of Annex III (not available as an input of the core) | a seam found, not in the plan; see Seams. |
| F-qualifier-fold | 13(3) items (a), (b)(iv) to (vii), (c), (f); 14(4) "as appropriate and proportionate"; 15(5) third subparagraph "where appropriate"; Annex IV chapeau and items 1(b), 1(f), 1(h), 2(a), 2(d), 2(f), 3 | the functions of those provisions | a qualifier inside a limb ("where applicable", "when appropriate", "if any") is folded into that limb's one yes/no: answer yes where the qualifier makes the limb inapplicable | one more input per qualifier (is the limb applicable?), `JUST TRUE` where it is not and `NOTHING` or `JUST FALSE` otherwise | the text qualifies each limb in its own words; folding keeps each function a one-line conjunction of the text's limbs; the `@desc` of each question says to answer yes where not applicable. |
| F-14-5-shape | 14(5) both subparagraphs | `Art 14(5) first subparagraph ...`, `Art 14(5) second subparagraph ...`, `Art 14(5) the deployer is barred ...`, and the rule | the "where Union or national law considers the application of this requirement to be disproportionate" qualifies the whole list (law enforcement, migration, border control or asylum): both limbs are needed to lift the requirement; the bar on the deployer is derived from the requirement and "unless" verification | "where ..." qualifies only the last item | the sentence has one "where" after the whole list. |
| F-15-5-list | 15(5) third subparagraph ("measures to prevent, detect, respond to, resolve and control for attacks ... or ..., confidentiality attacks or model flaws") | `Art 15(5) third subparagraph ...` | five matters the measures cover, each where appropriate (the "or" list is read as the minimum content of "shall include") | the measures need cover only one of the listed attacks | "shall include" gives the minimum; the list is of the matters the technical solutions address. |
| F-IV-7-disjunction | Annex IV point 7 | `Annex IV point 7 ...` | by cases: where harmonised standards were applied, the list; where none was, the description (the keel's `Art 3(27)` says what a harmonised standard is) | the list and the description are both always required | "where no such harmonised standards have been applied, a detailed description ...". |
| F-commission-no-gate | 11(1) the Commission's form, 11(3) delegated acts, 15(2) benchmarks | `Art 11(1) ... Commission ...`, `Art 11(3)`, `Art 15(2)` | the Commission's duties and powers take no AI system and no date gate (they are not about one system, so no route-based date can be computed) | gate them with the earliest date of the Section (2 December 2027), or with the route of a system | Article 113 dates a provision group by the route of a system; the text gives these provisions no system. |

20 forks.
The brief says to list them with a count; the sites that carry a count of their own are in Split sites.

## Jural relations (P2)

Each relation is stated once, neutrally.
The text names few holders: where it names none, the table says so and no holder is invented.

| provision | relation | holder | bearer (correlative) | L4 |
| --- | --- | --- | --- | --- |
| 4a(1), 4a(2) | privilege (liberty) to process special categories of personal data to detect and correct bias, on conditions | provider of a high-risk AI system (para 1); provider or deployer of another AI system or model, deployer of a high-risk AI system (para 2) | no-right: the data subject has no claim against the processing while the conditions are met | `Art 4a(1) ...`, `Art 4a(2) ...` |
| 4a(2) last sentence | none created (the text says it creates no obligation) | - | - | `Art 4a(2) last sentence ...` (`JUST FALSE`) |
| 8(1) | duty that a high-risk AI system comply with Section 2; no holder named | not named | provider (by Article 16, outside my ranges) | `Art 8(1) ...` |
| 8(2) | duty of the provider to ensure the product is compliant with Union harmonisation legislation; privilege to integrate documentation and procedures | not named; the provider holds the privilege | provider (duty); no-right of whoever would require separate documentation (privilege) | rule `Art 8(2) the provider's duty ...`; `Art 8(2) second sentence ...` |
| 9 to 15 (requirements) | duties that the system, its documentation and its instructions meet each requirement; no holder named | not named | provider (by Article 16, outside my ranges) | the decision functions of Articles 9 to 15 |
| 9(9) | duty of the provider to give consideration to adverse impact on persons under 18 | not named | provider | rule `Art 9(9) the provider's duty ...` |
| 11(1) simplified manner | privilege of an SME (and, as amended, an SMC) to provide the Annex IV elements in a simplified manner | the SME or SMC | no-right of the notified body or authority to insist on the full form | `Art 11(1) the provider may provide ...` |
| 11(1) the form | duty of the Commission to establish the simplified form; duty of the SME or SMC that opts to use it (as amended); duty of notified bodies to accept it (as amended) | SMEs and SMCs (claim to the form and its acceptance) | Commission; the SME or SMC; notified bodies | rules `Art 11(1) the Commission's duty ...`, `... the SME's or SMC's duty ...`, `... the notified body's duty ...` |
| 11(3) | power of the Commission to amend Annex IV by delegated act | Commission | liability of providers (their documentation requirement may change) | `Art 11(3) ...` |
| 13(2), 13(3), 15(3) | claim to instructions for use with the listed content | deployer | provider | `Art 13(2)`, `Art 13(3)`, `Art 15(3)` |
| 14(4) | claim that the system be provided so that the natural persons assigned oversight are enabled | deployer (and the natural persons assigned oversight) | provider | `Art 14(4)` |
| 14(5) | prohibition on the deployer's acting on an identification not separately verified by at least two natural persons; protection of the person identified; exemption in the second subparagraph | the person identified (the text names no holder) | deployer | rule `Art 14(5) the deployer's prohibition ...`; `Art 14(5) the deployer is barred ...` |
| 15(2) | duty of the Commission to encourage the development of benchmarks; no holder named | not named | Commission | rule `Art 15(2) the Commission's duty ...` |
| Annex IV | the content of the technical documentation of Article 11(1); no holder named | national competent authorities and notified bodies (Article 11(1) says the documentation is to give them the information) | provider | `Annex IV point 1` to `point 9`, the chapeau function |
| 10(1) to 10(4), 10(6), 12 | duties on the data sets and the logging capabilities; no holder named | not named | provider | the decision functions |

## Marginal readings for a lawyer (P2)

Every branch that rests on reading (a) (a failed "if" is the text's no, clause by clause, within the provision; a flat negative is the text's no) or on reading (b) (a grant or prohibition limited by its own wording does not say no), with the other reading.

| branch | rests on | answer taken | other reading |
| --- | --- | --- | --- |
| every flat "shall" requirement (F-bare-shall) | (a) | `JUST FALSE` when unmet | `NOTHING` |
| 4a(1) conditions (a) to (f), safeguards and the other instruments (F-4a-1-conditions, F-4a-1-gdpr); 4a(2)(b) | (a) | `JUST FALSE` when unmet: the gate is closed by "in order for" | `NOTHING` |
| 4a(1) "to the extent strictly necessary"; 4a(2)(a) "to the extent that"; 8(2) second sentence; 9(7); 9(10); 11(1) SME liberty (F-4a-1-necessary, F-4a-2-extent, F-ii-grants): the gate is not "where", "when" or "upon" | (b) | `NOTHING` when the gate fails | `JUST FALSE` (the periods ruling's rule (b), if the gate is read as a "where") |
| 11(3) "where necessary" (F-11-3-necessary): a "may" gated by the word "where" | (a) | `JUST FALSE` when it is not necessary (the periods ruling's item (b), as the brief's limit (3) leaves it) | `NOTHING` (the grant line): a question for a lawyer, per limit (3) |
| duties with an unmet "where", "when" or "whenever": 8(2) first sentence, 9(9), 10(1), 11(1) use, 11(2); and 11(1) acceptance, whose gate is not in the sentence's words (F-duty-where) | (a) declined; Guide line 95 (a duty whose "if" or "where" is unmet: the encoder decides) | `NOTHING` (the duty does not arise) | `JUST FALSE` (reading (a): a failed "if" is the text's no; the periods ruling's item (b); the brief's limit (2) "a duty") |
| duties limited to a class of system: 10(1), 10(6), 12(3), 14(5), 15(4) third subparagraph (F-duty-scope); and 10(6)'s "apply only to the testing data sets" | (b); 10(6) "only": (a) | `NOTHING` outside the class; `JUST FALSE` for a data set that is not a testing data set | `JUST FALSE` outside the class; `NOTHING` for a data set that is not a testing data set |
| 14(5) exemption: the requirement does not apply (second subparagraph) | (a) | `JUST FALSE` for "the requirement applies" when both limbs hold ("shall not apply"); `JUST TRUE` otherwise | the requirement is lifted for the listed uses whatever the law says |
| 14(5) "unless": the deployer is barred | (a) | `JUST FALSE` (not barred) where the identification was verified and confirmed by two natural persons | `NOTHING` |
| Article 2(2) cutting off Section 2 (the keel's answer, seam S14) | (a) | `JUST FALSE` (keel) | - |
| a system saved by Article 111(2), or not yet in the Section's date: `NOTHING` (the keel's reading) | keel | `NOTHING` | `JUST FALSE` (the keel's F-111-2-nothing) |

### Reading a result: FALSE and NOTHING (P2)

In this row a `JUST TRUE` is that the text's requirement is met on the facts given (or, for a "may" function, that the liberty or power is open on them), and a `JUST FALSE` is the text's own no to the case: a flat "shall" not done, a condition the text closes ("in order for", "unless") not met, or a "shall not apply" or "does not create any obligation".
A `NOTHING` is "not covered": the Section does not yet apply to the system on the date asked (Article 113), the system is saved by Article 111(2), Article 2(13) says the requirement may be limited and the delegated acts are outside the sources, the case falls outside a grant or a class the text limits in its own wording, or the text is silent.
A caller must never turn a `NOTHING` into a `FALSE`; the seat questions pass the answer through unchanged.

## Seams (P2)

| seam | what I took | where |
| --- | --- | --- |
| S1 route | `the route by which the AI system is high-risk` (the keel's enumeration) asked in the seat; the gate takes the core's `AI system` record | `P2-section-2-gate.l4`, every seat question |
| S7 all conditions of Article 57 or 60 fulfilled | a plain yes/no ("all the conditions laid down in Article 60 for testing in real-world conditions are fulfilled") | `Art 9(7)` |
| S8 provided: the high-risk AI system complies with the requirements of Chapter III Section 2 | `Arts 8 to 15 all the requirements are met given the answers` (a list of `MAYBE BOOLEAN`: any `JUST FALSE` gives `JUST FALSE`; all `JUST TRUE` and non-empty gives `JUST TRUE`; else `NOTHING`); `Art 8(1) first sentence ...` uses it over the seven Articles' answers | `P2-section-2-gate.l4`, `P2-art-8.l4` |
| S9 harmonised standard | the keel's `Art 3(27) the standard is a harmonised standard`, called | `Annex IV point 7` |
| S14 Article 2(2) | taken through the gate (the keel's function) | `Arts 8 to 15 the gate for the requirement` |
| S15 Article 2(13) | taken through the gate (the keel's function); Article 2(13) names Articles 9 to 15 and 17 to 25, so Article 8 is never limited by it | `Arts 8 to 15 the gate for the requirement` |
| found, not in the plan: Annex III point 1(a) | a plain yes/no `the high-risk AI system is referred to in point 1(a) of Annex III` (fork F-A1A-seam); another part that encodes Annex III may answer it | `Art 12(3)`, `Art 14(5)` |
| found, not in the plan: the Annex IV answer in Article 11(1) | a plain yes/no ("the technical documentation contains, at a minimum, the elements set out in Annex IV"); the Annex IV functions of this part answer it and a seat can compute it | `Art 11(1) second subparagraph second sentence ...` |
| named inside plain inputs (no function of another part called) | Article 3(3) and (4), (22), (63) and Article 2(1)(e) and (g) in the role questions (the keel's); Article 15, 14, 9(2), 12, 13(3), 72, 79(1), 26(5), 60, 47 inside the text of facts only | - |

## Split sites (P2)

(i) An unmet element of an infringement: **1 site**, answer `NOTHING`: `Art 14(5) the deployer is barred ...` when the system is not one referred to in point 1(a) of Annex III (the element that makes the prohibition reach it).
The Section has no prohibited practice and no other infringement; fork F-duty-scope.
Guide lines the answer relies on: the prohibition is limited in its own wording, "limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87); and the limit is a scope limit with no "only", "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" (Guide line 93).

(ii) A "may" gated by "where", "when", "to the extent" or the like, or a grant limited in its own wording: **7 sites**. Six answer `NOTHING` when the gate fails, on the grant line ("limits a grant or prohibition in its own wording and the case falls outside the limit" (Guide line 87)) as the brief's limit (1) applies it; none of the six gates is introduced by "where", "when" or "upon".
One, 11(3), is gated by the literal word "where" ("where necessary") and answers `JUST FALSE`, on the periods ruling's item (b) ("a "where ..." condition: when it fails the answer is `JUST FALSE`" (Guide line 93)) as the brief's limit (3) leaves it to the Guide's rulings.
The other reading at each site is the other answer.
Count for the brief's limit (3): "may" functions gated by "where", "when" or "upon": 1 (11(3)); "entitled"-named functions: 0.

| site | gate | answer taken | Guide line or ruling it relies on | fork line |
| --- | --- | --- | --- | --- |
| 4a(1) `Art 4a(1) ... may exceptionally process` | "To the extent strictly necessary" | `NOTHING` | Guide line 87 (grant limited in its own wording); line 93 item (c) (scope limit with no "only") | F-4a-1-necessary |
| 4a(2) `Art 4a(2) ... may exceptionally process` | "to the extent that (a) such processing is strictly necessary" | `NOTHING` for (a); `JUST FALSE` for (b) | (a) Guide line 87 and line 93 item (c); (b) limit (2) of the brief (Brief line 34); no Guide line fits exactly | F-4a-2-extent |
| 8(2) second sentence `Art 8(2) second sentence ... has the choice` | "into documentation and procedures that already exist" | `NOTHING` | Guide line 87 (grant limited in its own wording) | F-ii-grants |
| 9(7) `Art 9(7) ... may include testing in real-world conditions` | "in accordance with Article 60" (the conditions of Article 60 fulfilled, seam S7) | `NOTHING` | Guide line 87 (grant limited in its own wording; points outside the sources) | F-ii-grants |
| 9(10) `Art 9(10) ... may be part of, or combined with` | "For providers ... subject to requirements regarding internal risk management processes under other relevant provisions of Union law" | `NOTHING` | Guide line 93 item (c) (scope limit with no "only"); line 87 | F-ii-grants |
| 11(1) SME liberty `Art 11(1) the provider may provide ...` | "SMEs, including start-ups, [and SMCs,] may provide" (a gate on who) | `NOTHING` | Guide line 93 item (c); Guide line 87 | F-ii-grants |
| 11(3) `Art 11(3) ... may adopt delegated acts` | "where necessary, to ensure" | `JUST FALSE` | Guide line 93 item (b) (a "where" condition); limit (3) of the brief (Brief line 34) | F-11-3-necessary |

Two further liberties answer `NOTHING` as silent and have no gate: `Art 10(3) third sentence ...` and `Art 15(4) second subparagraph ...` (not counted).
`Art 4a(1)` also has a gate the text closes ("in order for such processing to occur") that answers `JUST FALSE`: F-4a-1-conditions; it is not a split site.

A grant or power limited by its own wording (the sites above) is one kind of split site; a duty whose "where", "when" or "if" is unmet is the other, and its six sites are in F-duty-where (the Guide's line 95 names that class and leaves the decision to the encoder; see the entry for what that line does and does not support).
A site that fits no Guide line says so in its fork entry and is in Marginal readings: 4a(2)(b), 4a(1) conditions, the acceptance site of 11(1), and 10(6)'s "only".

(iii) Functions whose answer can be `NOTHING` because a system is saved by Article 111(2) (those that pass the core's placement date to the keel's applicability function, through the gate): **65 decision functions** (all the functions of Articles 8 to 15 and Annex IV that take the AI system: 8(1) 4, 9 14, 10 7, 11 7, 12 3, 13 4, 14 7, 15 9, Annex IV 10, counting the dispatchers once), and the five regulative rules that call the gate answer `FULFILLED` for such a system (nothing is owed).
The keel's fork line is F-111-2-nothing in the keel's `NOTES.md`; I did not decide it again.

## Rules with no breach path (P2)

Seven regulative rules.
Six are a `MUST` with no time limit and no consequence the text states, so no trace can show them breached (a late act reads `FULFILLED`); each has a trace that fulfils it and a trace that leaves it `RESIDUAL`, and those with a "where" or the Section's date also have a trace where it is unmet (`FULFILLED`):

| provision | rule | party |
| --- | --- | --- |
| 8(2) first sentence | `Art 8(2) the provider's duty to ensure that the product is fully compliant` | Provider |
| 9(9) | `Art 9(9) the provider's duty to give consideration ...` | Provider |
| 11(1) second subparagraph (use of the form, as amended) | `Art 11(1) the SME's or SMC's duty to use the form` | Provider |
| 11(1) second subparagraph (acceptance, as amended) | `Art 11(1) the notified body's duty to accept the form` | Notified body |
| 11(1) second subparagraph (the form) | `Art 11(1) the Commission's duty to establish the simplified technical documentation form` | Commission (the keel's `Art 2(13) body`) |
| 15(2) | `Art 15(2) the Commission's duty to encourage the development of benchmarks and measurement methodologies` | Commission |

The seventh, `Art 14(5) the deployer's prohibition on acting on an identification that is not separately verified`, is a `SHANT` and has a breach path: the trace where the deployer acts on an identification not so verified reaches `BREACH` on both builds.
The duties in the passive (9(8), 11(1) first subparagraph, 11(2) and the design duties of Articles 10, 12, 13, 14(1) to (4) and 15, Annex IV) name no party, so there is no regulative rule for them (fork F-party-less); the time limit of 9(8) and 11(1) ("prior to", "before") is tested in the decision functions (a testing or drawing-up date on each side of the placement date).

## Versions (P2)

| consolidated lines | provision | what the Omnibus changed | encoded |
| --- | --- | --- | --- |
| 156-169 (INSERTED) | Article 4a | inserted: the permission of Article 10(5) as enacted, restated for providers of high-risk AI systems (para 1) and extended to providers and deployers of other AI systems and models and deployers of high-risk AI systems (para 2), with the last sentence that para 2 creates no obligation | both: `Art 10(5) as enacted ...` (base file lines 765-777) and `Art 4a(1) as amended ...` side by side; `Art 4a(1) the provider may exceptionally process ...` dispatches on the version and applies Chapter III's date as enacted or Chapter I's date as amended (F-4a-handover); 4a(2) as amended only, answering `NOTHING` before 27 July 2026 (silent) |
| 292 (REPLACED) | Article 10(1) | the cross-reference "paragraphs 2 to 5" became "paragraphs 2, 3 and 4 of this Article and in Article 4a(1)" | both: `Art 10(1) as enacted ...`, `Art 10(1) as amended ...`, dispatcher `Art 10(1) ...`; `P2-tests-versions.l4` tests the pair |
| 305-306 (DELETED) | Article 10(5) | deleted (its text went to Article 4a(1)) | the as-enacted text is encoded (`Art 10(5) as enacted ...`); the as-amended text has no paragraph 5: `Art 10(6) as amended` answers `NOTHING` for paragraph 5 |
| 308 (REPLACED) | Article 10(6) | "paragraphs 2 to 5" became "paragraphs 2, 3 and 4 of this Article and Article 4a(1)" | both: `Art 10(6) as enacted ...`, `Art 10(6) as amended ...`, dispatcher `Art 10(6) ...` |
| 314 (REPLACED) | Article 11(1), second subparagraph | SMCs added to the simplified manner and the form; the SME or SMC that opts must use the form; notified bodies must accept it | both for the SME liberty and the Commission's form (functions as enacted and as amended, a dispatcher for the liberty); the unchanged first two sentences once; the use and acceptance sentences, which are new, in the amended text only with an as-enacted branch answering `NOTHING` (silent) and the rules with an as-enacted branch `FULFILLED` |

Every as-enacted branch of a dispatcher of Chapter III Sections 1 to 3 is unreachable through the gate (fork F-10-5-dead): as enacted the Section applied from 2 August 2026 or 2 August 2027, after the Omnibus took effect on 27 July 2026.
Each as-enacted text is therefore tested through its own function, with no date and no gate.

## Seats (P2)

| seat | questions | files | note |
| --- | --- | --- | --- |
| provider | 69 | `P2-seat-provider.l4`, `P2-cases-seat-provider.l4` | the main seat: the requirements of Articles 8 to 15 and Annex IV, Article 4a, the role and applicability questions; mirrors of the deployer's and the notified body's |
| deployer | 24 | `P2-seat-deployer.l4`, `P2-cases-seat-deployer.l4` | Article 4a(2), and the mirror of each provider requirement the deployer receives or relies on (12, 13, 14, 15), and the bar of 14(5) |
| person | 6 | `P2-seat-person.l4`, `P2-cases-seat-person.l4` | Article 4a (may a provider or deployer process my special categories of data), the bar of Article 14(5) (is the deployer barred from acting on an identification of me), the role and applicability questions |
| notified | 13 | `P2-seat-notified.l4`, `P2-cases-seat-notified.l4` | the simplified form (11(1)) and the nine points of Annex IV and the chapeau |
| gpai | 4 | `P2-seat-gpai.l4`, `P2-cases-seat-gpai.l4` | Article 4a(2) only: a provider of a general-purpose AI model is a provider of an "other AI model" (the text of Chapter III Section 2 addresses systems, not models) |
| manufacturer | 5 | `P2-seat-manufacturer.l4`, `P2-cases-seat-manufacturer.l4` | Article 8(2) and Article 11(2): a product manufacturer that places a system with its product |
| importer | 0 | - | none: the text of my ranges does not address importers |
| distributor | 0 | - | none: the text of my ranges does not address distributors |
| rep | 0 | - | none: Article 13(3)(a) only requires the instructions for use to give the authorised representative's identity and contact details; that is a provider's duty, and the representative has no duty or right in my ranges |

Seat audit (second pass): 121 questions read, 3 retitled (direction 0, subject 3)

Method: every `@export` name and text, in all six seat files, was read against the layer-1 function its body calls and against the facts that function takes (the `@desc` of each asked fact).
Direction: the pairs with "may" call a function named "may" (the permission); "am I barred" and "is the deployer barred" call the bar (`Art 14(5) the deployer is barred ...`); "does paragraph 2 create an obligation on me" calls the function that answers that same question (`JUST FALSE`: the text says it does not); "does ... apply" calls the applicability function; "am I a ..." calls the keel's role definition (the general-purpose AI model question calls the keel's `Art 3(3)` and `Art 3(63)` together, as its title says); every other question is a compliance question over a function named for the same fact.
No direction mismatch was found.
Subject: three deployer questions asked about a property of the system itself (whether its operation is sufficiently transparent, whether it can be effectively overseen, whether it achieves an appropriate level of accuracy) while the function they call, and the facts it takes, ask whether the system is designed and developed in such a way, which is the Article's own wording.
They are retitled to ask what the function answers.
The provider's questions for the same provisions already used the Article's wording and are unchanged.
The function names and every fact, `@desc` and expected value are unchanged; each assertion the new titles break is restated in place in `P2-cases-seat-deployer.l4` with `-- RECONCILED 2026-11-17: was ...`.

| was | now |
| --- | --- |
| `Under Article 13(1), as a deployer of an AI system, in the first sentence, is the operation of the high-risk AI system I use sufficiently transparent to enable me to interpret its output and use it appropriately` | `Under Article 13(1), as a deployer of an AI system, in the first sentence, is the high-risk AI system I use designed and developed in such a way as to ensure that its operation is sufficiently transparent to enable me to interpret its output and use it appropriately` |
| `Under Article 14(1), as a deployer of an AI system, can the high-risk AI system I use be effectively overseen by natural persons during the period in which it is in use, with appropriate human-machine interface tools` | `Under Article 14(1), as a deployer of an AI system, is the high-risk AI system I use designed and developed in such a way, including with appropriate human-machine interface tools, that it can be effectively overseen by natural persons during the period in which it is in use` |
| `Under Article 15(1), as a deployer of an AI system, does the high-risk AI system I use achieve an appropriate level of accuracy, robustness and cybersecurity and perform consistently in those respects throughout its lifecycle` | `Under Article 15(1), as a deployer of an AI system, is the high-risk AI system I use designed and developed in such a way that it achieves an appropriate level of accuracy, robustness and cybersecurity and performs consistently in those respects throughout its lifecycle` |

Mirror cases: the same facts asked from two seats with answers that agree are marked `-- MIRROR` in the case files (provider, deployer and notified body; provider and person for Article 4a and 14(5)).

## What the text turns out to say (P2)

1. Article 4a(1) is Article 10(5) as enacted moved to Chapter I and reworded in small ways: "To the extent that it is strictly necessary for the purpose of ensuring ... paragraph (2), points (f) and (g) of this Article" became "To the extent strictly necessary to ensure ... Article 10(2), points (f) and (g), of this Regulation"; "as applicable" was added after the three instruments; "must" became "shall".
   The six conditions are the same.
2. Article 4a is in Chapter I, which applies from 2 February 2025 (Article 113(a)), while Article 10(5) as enacted sat in Chapter III Section 2.
   A reader asking on a date between 2 February 2025 and 26 July 2026 about processing special categories of personal data finds the text as enacted, whose paragraph is in a Section that did not yet apply: the answer is `NOTHING`, not a permission.
3. Because the Omnibus took effect on 27 July 2026, before any date on which Chapter III Section 2 applied as enacted (2 August 2026 and 2 August 2027), no date at which Article 10 applied was ever governed by its old text.
   The old text matters only for the question "what did it say".
4. Article 4a(2)'s last sentence ("This paragraph does not create any obligation to conduct such bias detection and correction") answers `JUST FALSE` whatever the facts, once Chapter I applies and the Omnibus text is in force: it is a flat negative.
5. Paragraph 5 of Article 14 puts a requirement on the measures (the provider's) and a prohibition on the deployer's acting in one sentence, and the second subparagraph lifts "the requirement" for law enforcement, migration, border control and asylum only where Union or national law considers it disproportionate; both limbs are needed.
6. Article 12(3)(d) points at Article 14(5)'s verifying persons and Article 13(3)(b)(ii) at Article 15's metrics; no function of mine calls another Article's function except through the inputs' texts.
7. Article 8(1)'s second sentence (the risk management system "shall be taken into account") is a requirement of its own, not part of Article 9.
8. Article 11(2) requires "a single set of technical documentation" only where the system is related to a product covered by Section A of Annex I; for any other system it does not speak.
9. Annex IV's chapeau ("as applicable to the relevant AI system") qualifies every point; items carry their own "where applicable" besides.
10. Article 15(2) is a duty of the Commission with no time limit and no consequence; Article 15(3) and 15(4) are in the passive.

## What the text does not answer (P2)

- Who holds the claim for the duties of Articles 8 to 15: the text names the system, not a party; Article 16(a) puts them on providers and is outside my ranges.
- When the Commission's duties in Articles 11(1) and 15(2) must be met: neither carries a date, and Article 113 dates a provision group by the route of a system.
- Whether "as applicable to the relevant AI system" (Annex IV chapeau) lets the provider leave out a whole point: the text qualifies the list without saying which points.
- What "appropriate", "as far as technically feasible", "sufficiently", "relevant" and the like mean: taken as plain yes/no inputs.
- How far the application of a requirement "may be limited" under Article 2(13): outside the sources (delegated acts); the gate answers `NOTHING` there.
- Whether the deployer's prohibition in Article 14(5) has a time limit or a consequence: the text gives neither, so the rule has no `WITHIN` and no `LEST`; the breach is the act.

## What the stable binary does not accept (P2)

Nothing I wrote was refused on the stable binary; the constructs I avoided because the brief and the plan say they fail are `REFUSE`, `#ASSERT REFUSED`, and `BECAUSE` (other than `LEST BREACH ... BECAUSE`).
- A `#TRACE`'s outcome cannot be asserted with `#ASSERT` on the stable binary, and `check.sh` does not see it (its own header says so).
  The seven regulative rules are therefore run with `#TRACE` (24 traces) and each outcome is compared with the `-- EXPECT` comment above it, on both builds, by `work/traces.py`; the same duties are also encoded as decision functions that are asserted (the layer-1 requirement functions, and for Article 14(5) `Art 14(5) the deployer is barred ...`).
- `NOT` is parenthesised; a genitive argument is parenthesised (`(`the AI system`'s `date placed ...`)`); an `#ASSERT` is on one line; dates are `Date d m y`; `IMPORT` finds only modules in the same folder.

## What `check.sh` prints (P2)

Baseline it replaced: the keel as handed over, five modules in the deposit (`aia-annex-x`, `aia-core`, `aia-definitions`, `aia-scope`, `aia-timeline`), 0 assertions satisfied, 0 failed, 0 refused, 0 errors (the keel's own run, with its tests and patterns, was 14 modules and 666 assertions, per PLAN.md).
After this run (`L4` 1.6.110, `L4_MAIN` 1.6.109, `JL4_LIBRARY_PATH` unset):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
aia-annex-x.l4                                 0         0       0        0         0 |      0         0       0        0  same
aia-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
aia-scope.l4                                   0         0       0        0         0 |      0         0       0        0  same
aia-timeline.l4                                0         0       0        0         0 |      0         0       0        0  same
P2-annex-iv.l4                                 0         0       0        0         0 |      0         0       0        0  same
P2-art-10.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-11.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-12.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-13.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-14.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-15.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-4a.l4                                   0         0       0        0         0 |      0         0       0        0  same
P2-art-8.l4                                    0         0       0        0         0 |      0         0       0        0  same
P2-art-9.l4                                    0         0       0        0         0 |      0         0       0        0  same
P2-cases-seat-deployer.l4                      0       167       0        0         0 |      0       167       0        0  same
P2-cases-seat-gpai.l4                          0        21       0        0         0 |      0        21       0        0  same
P2-cases-seat-manufacturer.l4                  0        30       0        0         0 |      0        30       0        0  same
P2-cases-seat-notified.l4                      0       100       0        0         0 |      0       100       0        0  same
P2-cases-seat-person.l4                        0        53       0        0         0 |      0        53       0        0  same
P2-cases-seat-provider.l4                      0       483       0        0         0 |      0       483       0        0  same
P2-seat-deployer.l4                            0         0       0        0         0 |      0         0       0        0  same
P2-seat-gpai.l4                                0         0       0        0         0 |      0         0       0        0  same
P2-seat-manufacturer.l4                        0         0       0        0         0 |      0         0       0        0  same
P2-seat-notified.l4                            0         0       0        0         0 |      0         0       0        0  same
P2-seat-person.l4                              0         0       0        0         0 |      0         0       0        0  same
P2-seat-provider.l4                            0         0       0        0         0 |      0         0       0        0  same
P2-section-2-gate.l4                           0         0       0        0         0 |      0         0       0        0  same
P2-tests-annex-iv.l4                           0       156       0        0         0 |      0       156       0        0  same
P2-tests-art-10.l4                             0       132       0        0         0 |      0       132       0        0  same
P2-tests-art-11.l4                             0       111       0        0         0 |      0       111       0        0  same
P2-tests-art-12.l4                             0        47       0        0         0 |      0        47       0        0  same
P2-tests-art-13.l4                             0        67       0        0         0 |      0        67       0        0  same
P2-tests-art-14.l4                             0       105       0        0         0 |      0       105       0        0  same
P2-tests-art-15.l4                             0       126       0        0         0 |      0       126       0        0  same
P2-tests-art-4a.l4                             0        73       0        0         0 |      0        73       0        0  same
P2-tests-art-8.l4                              0        53       0        0         0 |      0        53       0        0  same
P2-tests-art-9.l4                              0       191       0        0         0 |      0       191       0        0  same
P2-tests-versions.l4                           0        31       0        0         0 |      0        31       0        0  same
TOTAL (39 modules)                             0      1946       0        0           |      0      1946       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```
