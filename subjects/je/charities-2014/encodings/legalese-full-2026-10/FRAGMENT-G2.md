# FRAGMENT-G2: Articles 3 to 7 of the Charities (Jersey) Law 2014

Encoder G2. Scope: Part 2 (Articles 3 and 4: the Commissioner and its general functions) and Part 3 (Articles 5 to 7: the charity test, charitable purposes, public benefit). Module prefix `g2-`. Source: `inputs/charities-jersey-law-2014-2026-10-02.txt` (the text from 2 October 2026), checked word for word against the official PDF's text layer for Articles 3 to 7; the two agree (only layout differs). No endnote marker falls on Articles 3 to 7, and none of the instruments in `inputs/amending/` amends them (read for their amendments of this Law: Article 1 "Minister" and "Comptroller", Article 2(1)(ba), Schedule 1; R&O.17/2018 and R&O.136/2019 only appoint days). So the Articles read the same in the vintages the sources show. "The Minister" of Articles 4(3), 5(3) and 5(6) to 5(8) is the role `the Minister`; the office the role names in a given text is reached only through the input `the office of the Minister` (IP3), and only on the second reading of fork F2.3.

This file was revised after independent testing: three repairs (the object of improving the conditions of life in 6(1)(i); a body that is not an entity cannot meet the charity test; the Commissioner's staff exercising the Commissioner's function are bound as the Commissioner is, fork F2.13). Section 11, "Changes after independent testing", lists every change of signature and of behaviour, with the old and the new `GIVEN` lists, so that the integrator can rewire.

Everything below was checked with `work/g2/check-g2.sh` (the output is pasted in section 10). The statements in this file about the modules were checked against the modules at the time of writing; where a claim is only a proposal it says "proposed".

## 0. Files

All in `deposit/`, all starting `g2-`. Import graph (acyclic; each imports only prelude, daydate, domain and modules of group G2):

| module | holds | imports (G2) |
| --- | --- | --- |
| `g2-nouns` | the group's nouns: the act type, the records, the limb result, the thirteen fork enumerations and the record `Interpretation of Articles 3 to 7`. DECLAREs only | none |
| `g2-readings` | data: ready-made values of the record (the favoured interpretation, and 15 others that each differ from it at exactly one fork point) | `g2-nouns` |
| `g2-fixtures` | data: purposes, facts about purposes, entities, constitutions, determinations, for the tests and for any caller | `g2-nouns` |
| `g2-art3-4-commissioner` | Articles 3 and 4 | `g2-nouns` |
| `g2-art6-purposes` | Article 6 | `g2-nouns` |
| `g2-art7-public-benefit` | Article 7 | `g2-nouns` |
| `g2-art5-charity-test` | Article 5 | `g2-nouns`, `g2-art6-purposes`, `g2-art7-public-benefit` |
| `g2-tests-art3-4`, `g2-tests-art5`, `g2-tests-art6`, `g2-tests-art7` | green tests | the modules they test, `g2-readings`, `g2-fixtures` |
| `g2-tests-red` | assertions that are MEANT to fail, counted: 15 (14 forks answered as their other reading answers them, and one control) | all of the above |

Departures from PLAN section (b), with the reason. (1) A module `g2-nouns` was added because the one record of forks must be shared by four Article modules and `domain.l4` is read-only. (2) `g2-readings` and `g2-fixtures` were added so that the record, which has thirteen fields that L4 source must all supply (TYPICALLY does not let a source omit one; at the service boundary `l4 batch` fills an omitted field from its TYPICALLY, which I tested), and the case values need not be rewritten in every test or by every caller. (3) The rule names are PLAN's, kept exactly where PLAN gave one; PLAN gave no names for the extra rules, which follow the same `Art N(m) ...` style and are unique to this group by their Article number.

No module starts with `@lang en`. No section `GIVEN` is used in any g2 module: every input is an ordinary rule `GIVEN`, so that an `@export` reaching a rule in another module never reaches a section `GIVEN`.

Method. One session; the survey's slice and the skills read first; nouns, then Articles 3 and 4 with their tests, then the check script and the source-locator gate, then Article 6, Article 7, Article 5; each test's expected value was decided from the Law's text before the module was run. A mutation test of the finished modules is reported in section 10.

## 1. Coverage

One row per provision of the scope, in the Law's numbering: 90 rows. `encoded` is 81, `inert` is 9, `refused` and `out-of-scope` are 0, and `deferred` is 0. Four rows change disposition from the survey (4(3) and 4(3)(a), (b), (c): inert in PLAN, encoded here), and the reason is in the row. Article 4(1)'s paragraphs (a), (b), (c), (e), (f), (g) and Article 3 stay inert; the reason is given at each, and the modules carry the quotation and the reason as comments under the Article's `§§` heading.

Where a row says "calls", the rule named is where the provision's words are decided; where it says "field", the provision is a limb of a record the rule reads.

| id | provision | first words | disposition | module | rule or place | note |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | Article 3 | 3 Establishment of Jersey Charity Commissioner | inert | g2-art3-4-commissioner | (none) | The Article only establishes the office. Its whole effect here is that the role `the Commissioner` exists, which is a constructor of `Legal actor` in domain.l4; there is no condition to test and no outcome to compute, and no caller is ever asked whether a body "is established". Quoted under the Article 3 heading. |
| 3(1) | Article 3(1) | (1) There is established a corporation sole to be known … | inert | g2-art3-4-commissioner | (none) | Establishes a corporation sole; carried by the role `the Commissioner` of `Legal actor` (domain.l4). Who holds the office, and who acts for it, is Schedule 1 (G9). Quoted, with the reason, under the Article 3 heading. |
| 3(2) | Article 3(2) | (2) Schedule 1 makes further provision in respect of the … | inert | g2-art3-4-commissioner | (none) | Points at Schedule 1, which group G9 encodes. Nothing to compute. |
| 4 | Article 4 | 4 General functions of Commissioner | encoded | g2-art3-4-commissioner | the rules of 4(1)(d), 4(2), 4(3) and 4(4) below | heading row |
| 4(1) | Article 4(1) | (1) The general functions of the Commissioner are – | encoded | g2-art3-4-commissioner | `Art 4(1)(d) ...` (the only paragraph with an act) | lead-in; its paragraphs (a), (b), (c), (e), (f), (g) are inert |
| 4(1)(a) | Article 4(1)(a) | (a) to administer the charity test under Part 3, and … | inert | g2-art3-4-commissioner | (none) | A function: administering the charity test and operating the register. The rules that do it are Parts 3 and 4 (G2 to G4); this paragraph states no condition and no outcome. What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(1)(b) | Article 4(1)(b) | (b) to supervise the compliance of charity governors with their … | inert | g2-art3-4-commissioner | (none) | A function: supervising governors. The duties supervised are Part 5 (G6); no condition and no outcome here. What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(1)(c) | Article 4(1)(c) | (c) to seek to enforce the requirements of Part 6 … | inert | g2-art3-4-commissioner | (none) | A function: "seek to enforce" Part 6. It confers no power to prosecute and names no act that could be done or omitted; the prohibitions are encoded in G7. What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(1)(d) | Article 4(1)(d) | (d) to publish and maintain guidance on the operation of … | encoded | g2-art3-4-commissioner | `Art 4(1)(d) the Commissioner must publish and maintain guidance on the operation of the Law` | DEONTIC; MUST; no WITHIN because the Law states no period; "publish" is the Article 1 definition (the publisher's opinion), so publication is the event of a trace |
| 4(1)(e) | Article 4(1)(e) | (e) to assist other persons (including the Attorney General, the … | inert | g2-art3-4-commissioner | (none) | A function: assisting other persons, "particularly by giving information". It has no preconditions; the disclosure rules are Articles 29 to 31 (G8). What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(1)(f) | Article 4(1)(f) | (f) generally to encourage, facilitate and monitor compliance of registered … | inert | g2-art3-4-commissioner | (none) | A function: "generally to encourage, facilitate and monitor compliance". It names no act that could be done or omitted. What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(1)(g) | Article 4(1)(g) | (g) any other function conferred on the Commissioner by this … | inert | g2-art3-4-commissioner | (none) | Residual: any other function conferred elsewhere. Nothing to compute. What the list does control is the reach of 4(2), "any of his or her functions", which is the input `the thing is calculated to facilitate, or is conducive or incidental to, a function`. |
| 4(2) | Article 4(2) | (2) The Commissioner may do anything (other than acting as … | encoded | g2-art3-4-commissioner | `Art 4(2) the Commissioner has power to do the thing`; `Art 4(2) the Commissioner may do the thing` | BOOLEAN eligibility and the MAY rule; the exclusion (acting as a governor) is a conjunct |
| 4(3) | Article 4(3) | (3) The Commissioner may in particular, without prejudice to the … | encoded | g2-art3-4-commissioner | `Art 4(3) the Commissioner has power to do the listed example`; `Art 4(3) the Commissioner may do the listed example` | CHANGED FROM the survey's inert: three powers of a named actor are powers, and the text has a real ambiguity (F2.8) |
| 4(3)(a) | Article 4(3)(a) | (a) provide information to the public about the system of … | encoded | g2-art3-4-commissioner | constructor `providing information to the public about the system of registration of charities` of `Example listed in Article 4(3)`; `the act of the Commissioner that Article 4(3) lists as` | CHANGED FROM inert, see 4(3) |
| 4(3)(b) | Article 4(3)(b) | (b) advise the Minister as to the nature of charities … | encoded | g2-art3-4-commissioner | constructor `advising the Minister about charities in Jersey and further regulation of them` | CHANGED FROM inert, see 4(3) |
| 4(3)(c) | Article 4(3)(c) | (c) assist a body in any jurisdiction other than Jersey, … | encoded | g2-art3-4-commissioner | constructor `assisting an equivalent body outside Jersey in the performance of its functions` | CHANGED FROM inert, see 4(3); the discriminating case of F2.8 |
| 4(4) | Article 4(4) | (4) In performing his or her functions, the Commissioner must, … | encoded | g2-art3-4-commissioner | `Art 4(4) the Commissioner has sought to act as Article 4(4) requires`; `Art 4(4) the Commissioner must seek to act as Article 4(4) requires` | a standard of conduct: the Commissioner's opinion on practicability is an input (F2.9); the duty is a standing MUST without a period |
| 4(4)(a) | Article 4(4)(a) | (a) protects public trust and confidence in registered charities, and … | encoded | g2-art3-4-commissioner | field `protects public trust and confidence in registered charities` of `How the Commissioner acted in performing a function` | one limb of the record |
| 4(4)(a)(i) | Article 4(4)(a)(i) | (i) all forms of charitable giving, and | encoded | g2-art3-4-commissioner | field `is compatible with the encouragement of all forms of charitable giving` | one limb |
| 4(4)(a)(ii) | Article 4(4)(a)(ii) | (ii) voluntary participation in the work of registered charities; and | encoded | g2-art3-4-commissioner | field `is compatible with the encouragement of voluntary participation in the work of registered charities` | one limb |
| 4(4)(b) | Article 4(4)(b) | (b) is proportionate as to the burdens imposed on, and … | encoded | g2-art3-4-commissioner | fields `is proportionate as to the burdens imposed on registered charities` and `supports the development of registered charities` | two limbs of one paragraph |
| 5 | Article 5 | 5 The charity test | encoded | g2-art5-charity-test | `Art 5 the entity meets the charity test` | heading row; IP8 |
| 5(1) | Article 5(1) | (1) An entity meets the charity test if – | encoded | g2-art5-charity-test | `Art 5 the entity meets the charity test`; `Art 5 the limb that decides the charity test` | IP8; asks the non-entity guard first (a body within no kind of entity under Article 2(1) does not meet the test: FALSE), then the bar (see the module header) |
| 5(1)(a) | Article 5(1)(a) | (a) all of its purposes are – | encoded | g2-art5-charity-test | `Art 5(1)(a) all of the entity's purposes are charitable or purely ancillary`; `Art 5(1)(a) the purpose counts` | F2.1 |
| 5(1)(a)(i) | Article 5(1)(a)(i) | (i) charitable purposes, or | encoded | g2-art5-charity-test | `Art 5(1)(a)(i) the purpose is a charitable purpose` | calls `Art 6(1) the purpose with its facts is a charitable purpose` |
| 5(1)(a)(ii) | Article 5(1)(a)(ii) | (ii) purposes that are purely ancillary or incidental to any … | encoded | g2-art5-charity-test | `Art 5(1)(a)(ii) the purpose is purely ancillary or incidental to a charitable purpose`; `Art 5(1)(a)(ii) an ancillary purpose can count` | the flag is an input; Article 6(5) removes a political purpose from it; F2.1 |
| 5(1)(b) | Article 5(1)(b) | (b) in giving effect to those purposes, it provides (or, … | encoded | g2-art5-charity-test | `Art 5(1)(b) the entity provides public benefit to a reasonable degree` (calls `Art 7 the entity provides public benefit`) | "to a reasonable degree" is the determiner's finding; the applicant limb reads the standing on the register |
| 5(2) | Article 5(2) | (2) An entity that otherwise meets the charity test, nevertheless … | encoded | g2-art5-charity-test | `Art 5(2) the constitution defeats the charity test`; `Art 5(2) the bar applies to the entity` | F2.2, F2.3 |
| 5(2)(a) | Article 5(2)(a) | (a) a Minister; | encoded | g2-art5-charity-test | constructor `a Minister` of `Person named in Article 5(2)`; `Art 5(2) the person is one that Article 5(2) names` | F2.3 (T4) |
| 5(2)(b) | Article 5(2)(b) | (b) a member of the States Assembly; or | encoded | g2-art5-charity-test | constructor `a member of the States Assembly` | no reading to choose |
| 5(2)(c) | Article 5(2)(c) | (c) any equivalent of such a person in another jurisdiction, | encoded | g2-art5-charity-test | constructor `any equivalent of a Minister or of a member of the States Assembly in another jurisdiction` | "such a person" is read as both of (a) and (b); the equivalence is a fact the caller records |
| 5(3) | Article 5(3) | (3) The Minister may by Order disapply paragraph (2) in … | encoded | g2-art5-charity-test | `Art 5(3) the Minister may disapply Article 5(2)`; the input `an Order under Article 5(3) disapplies Article 5(2) for the entity`; `Art 5(3) the entity meets the charity test only by virtue of an Order` | IP10; the Order's content is an input; FALSE for a body that is not an entity |
| 5(4) | Article 5(4) | (4) The Commissioner must publish and maintain guidance on the … | encoded | g2-art5-charity-test | `Art 5(4) the Commissioner must publish and maintain guidance on the charity test` | standing MUST, no period |
| 5(5) | Article 5(5) | (5) Any person, in determining whether an entity meets the … | encoded | g2-art5-charity-test | `Art 5(5) the person must have regard to the guidance`; `Art 5(5) the duty to have regard to the guidance`; field `regard was had to the guidance published under Article 5(4)` of `Determination of public benefit` | "have regard" is a recorded fact; F2.13: a member of the Commissioner's staff exercising the Commissioner's function (Schedule 1 paragraph 4(3)) is bound as the Commissioner is, on the first reading |
| 5(6) | Article 5(6) | (6) Before issuing or amending guidance the Commissioner must – | encoded | g2-art5-charity-test | `Art 5(6) the Commissioner must consult and publish a report before issuing or amending guidance`; `Art 5(6) the consultation and the report preceded the guidance`; `Art 5(6) Articles 5(6) to 5(8) apply to the guidance` | F2.7 (period P3, "before"), F2.12 |
| 5(6)(a) | Article 5(6)(a) | (a) consult – | encoded | g2-art5-charity-test | `Art 5(6)(a) the consultation covered those whom Article 5(6)(a) names`; the act `consult` | one act with three objects |
| 5(6)(a)(i) | Article 5(6)(a)(i) | (i) any persons appearing to the Commissioner to be representative … | encoded | g2-art5-charity-test | field `persons appearing to the Commissioner to be representative of charities or bodies with charitable purposes` of the act `consult` | owed only if the Commissioner considers that any persons so appear (input) |
| 5(6)(a)(ii) | Article 5(6)(a)(ii) | (ii) the Minister, and | encoded | g2-art5-charity-test | field `the Minister` of the act `consult` | always owed |
| 5(6)(a)(iii) | Article 5(6)(a)(iii) | (iii) such other persons as the Commissioner considers appropriate; and | encoded | g2-art5-charity-test | field `such other persons as the Commissioner considers appropriate` of the act `consult` | owed only if the Commissioner considers that there are such persons (input) |
| 5(6)(b) | Article 5(6)(b) | (b) publish a report on the Commissioner’s views on the … | encoded | g2-art5-charity-test | the act `publish a report on the views on the consultation and the reasons for the decision on the guidance`, the HENCE of the chain in `Art 5(6) the Commissioner must consult and publish a report ...` | the report cannot precede the consultation it reports on |
| 5(7) | Article 5(7) | (7) Within a reasonable time after issuing or amending guidance … | encoded | g2-art5-charity-test | `Art 5(7) the Commissioner must provide the Minister with the guidance and the report`; `Art 5(7) the Commissioner provided the Minister with the guidance and the report in time` | period P1: F2.4, F2.6 |
| 5(8) | Article 5(8) | (8) The Minister must lay a copy of the guidance … | encoded | g2-art5-charity-test | `Art 5(8) the Minister must lay the guidance and the report before the States`; `Art 5(8) the Minister laid the guidance and the report before the States in time` | period P2: F2.4, F2.6 |
| 6 | Article 6 | 6 Charitable purposes | encoded | g2-art6-purposes | the rules of 6(1) to 6(5) below | heading row |
| 6(1) | Article 6(1) | (1) For the purposes of this Law, the charitable purposes … | encoded | g2-art6-purposes | `Art 6(1) the purpose is a charitable purpose`; `Art 6(1) the head admits the purpose`; `Art 6(1) the purpose falls within a paragraph of paragraph (1)` | the head recorded is the caller's determination; 6(2) and 6(5) are applied to it |
| 6(1)(a) | Article 6(1)(a) | (a) the prevention or relief of poverty; | encoded | g2-art6-purposes | arm `the prevention or relief of poverty` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(b) | Article 6(1)(b) | (b) the advancement of education; | encoded | g2-art6-purposes | arm `the advancement of education` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(c) | Article 6(1)(c) | (c) the advancement of religion; | encoded | g2-art6-purposes | arm `the advancement of religion` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | also IP11: `Art 6 the entity has a purpose within the advancement of religion` (F2.5) |
| 6(1)(d) | Article 6(1)(d) | (d) the advancement of health; | encoded | g2-art6-purposes | arm `the advancement of health` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | extended by 6(2)(a) |
| 6(1)(e) | Article 6(1)(e) | (e) the saving of lives; | encoded | g2-art6-purposes | arm `the saving of lives` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(f) | Article 6(1)(f) | (f) the advancement of citizenship or community development; | encoded | g2-art6-purposes | arm `the advancement of citizenship or community development` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | extended by 6(2)(b) |
| 6(1)(g) | Article 6(1)(g) | (g) the advancement of the arts, heritage, culture or science; | encoded | g2-art6-purposes | arm `the advancement of the arts, heritage, culture or science` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(h) | Article 6(1)(h) | (h) the advancement of public participation in sport; | encoded | g2-art6-purposes | arm `the advancement of public participation in sport` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | narrowed by 6(2)(c) |
| 6(1)(i) | Article 6(1)(i) | (i) the provision of recreational facilities, or the organisation of … | encoded | g2-art6-purposes | arm `the provision of recreational facilities or the organisation of recreational activities` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | needs the object of improving the conditions of life (src:176) AND the conditions of 6(2)(d): `Art 6(1)(i) paragraph (1)(i) is met` |
| 6(1)(j) | Article 6(1)(j) | (j) the advancement of human rights, conflict resolution or reconciliation; | encoded | g2-art6-purposes | arm `the advancement of human rights, conflict resolution or reconciliation` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(k) | Article 6(1)(k) | (k) the promotion of religious or racial harmony; | encoded | g2-art6-purposes | arm `the promotion of religious or racial harmony` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(l) | Article 6(1)(l) | (l) the promotion of equality and diversity; | encoded | g2-art6-purposes | arm `the promotion of equality and diversity` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | F2.11 |
| 6(1)(m) | Article 6(1)(m) | (m) the advancement of environmental protection or improvement; | encoded | g2-art6-purposes | arm `the advancement of environmental protection or improvement` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(n) | Article 6(1)(n) | (n) the relief of those in need by reason of … | encoded | g2-art6-purposes | arm `the relief of those in need by reason of age, ill-health, disability, financial hardship or other disadvantage` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | extended by 6(2)(e) |
| 6(1)(o) | Article 6(1)(o) | (o) the advancement of animal welfare; | encoded | g2-art6-purposes | arm `the advancement of animal welfare` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | a head admits a purpose recorded under it |
| 6(1)(p) | Article 6(1)(p) | (p) any other purpose that may reasonably be regarded as … | encoded | g2-art6-purposes | arm `any other purpose that may reasonably be regarded as analogous to one of the above` of `Art 6(1) the head admits the purpose` (constructor of `Head of charitable purpose`, domain.l4) | the caller records the judgement by recording this head; 6(2)(f) deems one analogy |
| 6(2) | Article 6(2) | (2) For the purposes of paragraph (1) – | encoded | g2-art6-purposes | `Art 6(2) a clarification brings the purpose within a head` | the extensions (a), (b), (e); the narrowings (c), (d) are applied through the heads (h) and (i) |
| 6(2)(a) | Article 6(2)(a) | (a) in paragraph (1)(d), “the advancement of health” includes the … | encoded | g2-art6-purposes | `Art 6(2)(a) the advancement of health includes the purpose` | extension of head (d) |
| 6(2)(b) | Article 6(2)(b) | (b) paragraph (1)(f) includes – | encoded | g2-art6-purposes | `Art 6(2)(b)(i) ...` and `Art 6(2)(b)(ii) ...` | extension of head (f) |
| 6(2)(b)(i) | Article 6(2)(b)(i) | (i) rural or urban regeneration, and | encoded | g2-art6-purposes | `Art 6(2)(b)(i) paragraph (1)(f) includes the purpose, as regeneration` |  |
| 6(2)(b)(ii) | Article 6(2)(b)(ii) | (ii) the promotion of civic responsibility, volunteering, the voluntary sector … | encoded | g2-art6-purposes | `Art 6(2)(b)(ii) paragraph (1)(f) includes the purpose, as promotion of civic responsibility` |  |
| 6(2)(c) | Article 6(2)(c) | (c) in paragraph (1)(h), “sport” means sport that involves physical … | encoded | g2-art6-purposes | `Art 6(2)(c) sport means sport that involves physical skill and exertion` | narrowing of head (h); refuses if the fact is not stated |
| 6(2)(d) | Article 6(2)(d) | (d) paragraph (1)(i) applies only in relation to recreational facilities … | encoded | g2-art6-purposes | `Art 6(2)(d) paragraph (1)(i) applies` | narrowing of head (i), the second condition of it; refuses if neither alternative is stated; head (i) calls it through `Art 6(1)(i) paragraph (1)(i) is met` |
| 6(2)(d)(i) | Article 6(2)(d)(i) | (i) primarily intended for persons who have need of them … | encoded | g2-art6-purposes | field `the facilities or activities are primarily intended for persons who have need of them ...` of `Facts about a purpose under Article 6` |  |
| 6(2)(d)(ii) | Article 6(2)(d)(ii) | (ii) available to members of the public at large or … | encoded | g2-art6-purposes | field `the facilities or activities are available to members of the public at large or to male or female members of the public at large` |  |
| 6(2)(e) | Article 6(2)(e) | (e) paragraph (1)(n) includes relief given by the provision of … | encoded | g2-art6-purposes | `Art 6(2)(e) paragraph (1)(n) includes the purpose, as relief given by accommodation or care` | extension of head (n) |
| 6(2)(f) | Article 6(2)(f) | (f) for the purposes of paragraph (1)(p), the advancement of … | encoded | g2-art6-purposes | `Art 6(2)(f) the purpose is analogous to the advancement of religion by the analogy of paragraph (1)(p)`; `Art 6 the purpose is within the advancement of religion` | F2.5; T27; IP11 |
| 6(3) | Article 6(3) | (3) The States may, on the recommendation of the Commissioner, … | encoded | g2-art6-purposes | `Art 6(3) the States may add a sub-paragraph to Article 6(1) or (2)`; `Art 6(3) the States may make the Regulations` | a MAY of the States, guarded by the Commissioner's recommendation; the Regulations' content is an input |
| 6(3)(a) | Article 6(3)(a) | (a) add sub-paragraphs to paragraph (1); | encoded | g2-art6-purposes | field `adds sub-paragraphs to paragraph (1)` of `Content of Regulations under Article 6(3)` |  |
| 6(3)(b) | Article 6(3)(b) | (b) add sub-paragraphs to paragraph (2) making explanatory provision in … | encoded | g2-art6-purposes | fields `adds sub-paragraphs to paragraph (2)` and `the sub-paragraphs added to paragraph (2) make explanatory provision in relation to sub-paragraphs added to paragraph (1)` |  |
| 6(4) | Article 6(4) | (4) The power under paragraph (3) does not include power … | encoded | g2-art6-purposes | `Art 6(4) the Regulations are within the power of Article 6(3)` | a limit on the content of the Regulations |
| 6(4)(a) | Article 6(4)(a) | (a) to amend or restrict the effect of any of … | encoded | g2-art6-purposes | field `amends or restricts the effect of any of paragraphs (1)(a) to (p) and (2)(a) to (f)` |  |
| 6(4)(b) | Article 6(4)(b) | (b) to alter the effect of paragraph (5). | encoded | g2-art6-purposes | field `alters the effect of paragraph (5)` |  |
| 6(5) | Article 6(5) | (5) The purpose of advancing a political party or promoting … | encoded | g2-art6-purposes | `Art 6(5) the purpose is neither charitable nor ancillary` | overrides 6(1) and 5(1)(a)(ii) by its own words |
| 7 | Article 7 | 7 Public benefit | encoded | g2-art7-public-benefit | the rules of 7(1) to 7(4) below | heading row |
| 7(1) | Article 7(1) | (1) Paragraphs (2) and (3) apply to the Commissioner, the … | encoded | g2-art7-public-benefit | `Art 7(1) Articles 7(2) and 7(3) apply to the person` | binds the Commissioner, the Charity Tribunal and the court; F2.13: and, on the first reading, a member of the Commissioner's staff exercising the Commissioner's function (Schedule 1 paragraph 4(3)) |
| 7(2) | Article 7(2) | (2) The person determining the question must have regard to … | encoded | g2-art7-public-benefit | `Art 7(2) the determiner had the regard that Article 7(2) requires` | "have regard" is a recorded fact |
| 7(2)(a) | Article 7(2)(a) | (a) how any – | encoded | g2-art7-public-benefit | `Art 7(2)(a) the person determining must have regard to the comparison of benefit and disbenefit`; field `regard was had to how benefit ... compare with the benefit gained or likely to be gained by the public` of `Determination of public benefit` |  |
| 7(2)(a)(i) | Article 7(2)(a)(i) | (i) benefit gained or likely to be gained by members … | encoded | g2-art7-public-benefit | the same field as 7(2)(a): (i) and (ii) are two objects of ONE comparison ("how any (i) ..., and (ii) ..., compares with ..."), recorded as one fact of regard | see the note on 7(2)(a) in section 7 (open questions) |
| 7(2)(a)(ii) | Article 7(2)(a)(ii) | (ii) disbenefit incurred or likely to be incurred by the … | encoded | g2-art7-public-benefit | the same field as 7(2)(a) | see 7(2)(a)(i) |
| 7(2)(b) | Article 7(2)(b) | (b) if benefit is, or is likely to be, provided … | encoded | g2-art7-public-benefit | `Art 7(2)(b) the person determining must have regard to whether a condition on obtaining the benefit is unduly restrictive`; fields `benefit is, or is likely to be, provided to a section of the public only` and `regard was had to whether any condition ... is unduly restrictive` | a gate: owed only where benefit goes to a section of the public only |
| 7(3) | Article 7(3) | (3) The person determining the question must not – | encoded | g2-art7-public-benefit | `Art 7(3) the determination is permitted` | vacuously satisfied by a determiner that 7(1) does not bind |
| 7(3)(a) | Article 7(3)(a) | (a) presume any particular charitable purpose to be for the … | encoded | g2-art7-public-benefit | `Art 7(3)(a) the determination did not presume a charitable purpose to be for the public benefit`; `Art 7(3)(a) the person determining must not presume a charitable purpose to be for the public benefit` | a SHANT with no period |
| 7(3)(b) | Article 7(3)(b) | (b) treat one particular natural person or a group of … | encoded | g2-art7-public-benefit | `Art 7(3)(b) the determination did not treat identified natural persons as a section of the public`; two SHANT rules (`... as a section of the public`, `... as providing public benefit`) | also makes one outcome a matter of law: `Art 7 the entity provides public benefit` |
| 7(4) | Article 7(4) | (4) The guidance published by the Commissioner under Article 5(4), … | encoded | g2-art7-public-benefit | `Art 7(4) the guidance published under Article 5(4) gives guidance on public benefit` | a limit on the content of the guidance |

Counts: 90 rows; encoded 81, inert 9; deferred 0.

## 2. Fork register (the R4 shape)

The record is `Interpretation of Articles 3 to 7` (module `g2-nouns`), with thirteen fields; each field is one fork point and one enumeration; each is `TYPICALLY` the reading taken. Every public decision that depends on a fork takes the record as an ordinary `GIVEN` named `interp` and delegates by `CONSIDER` to one private rule per reading (the rules are named `reading A of ...` and `reading B of ...`, so that each reading is callable and has a test). `g2-readings` has the favoured interpretation and one value per other reading, each differing from the favoured one at exactly one field. Register entries map 1:1 to the record's fields, in this order.

A note on the red tests. For every fork the discriminating case is asserted in a green test under each reading, and the answer the OTHER reading would give is asserted under the favoured reading in `g2-tests-red.l4`, where it fails on purpose. Those failures are the proof that the fork is real: the readings differ on that case.

### F2.1: "all of its purposes" with no purposes, and with ancillary purposes alone

- Provision: 5(1)(a), (a)(i), (a)(ii); `-- src:146-148`.
- Field: `how the purposes of an entity are tested` : `How the purposes of an entity are tested in Article 5(1)(a)`.
- Readings and their text.
  - A (taken), `at least one charitable purpose is required, and an ancillary purpose counts only beside one`: there is a charitable purpose among the purposes, and every purpose is charitable or purely ancillary. Licence: (ii) speaks of purposes "purely ancillary or incidental to any of its charitable purposes", which presupposes that the entity has one; the Law's own vocabulary treats having a charitable purpose as the mark of the class ("entities with charitable purposes", 4(1)(e), 4(2)); an entity with no purposes has not shown that it has any.
  - B, `an entity with no purposes satisfies the test vacuously`: the literal universal. "all of its purposes are ..." is true of no purposes. An ancillary purpose still needs a charitable one beside it, because of "any of its charitable purposes".
  - C, `purely ancillary purposes satisfy the test without any charitable purpose`: (ii) is read as a free-standing alternative joined by "or", so a purpose that is purely ancillary is acceptable on its own.
- Why A: B adds nothing the text states and gives the odd result that an entity with no purposes at all passes the charity test; C reads "any of its charitable purposes" as if it were not there.
- Political purposes are out on every reading: Article 6(5) says a political purpose is neither charitable nor ancillary, "irrespective of whether it would otherwise fall within paragraph (1) or Article 5(1)(a)(ii)".
- Discriminating cases. An entity with no purposes: A fails (a), B and C satisfy it. An entity whose only purpose is an ancillary one: A and B fail, C satisfies. Tests: `g2-tests-art5` section "FORK F2.1" (inventory, section 10). Red: 2 assertions.

### F2.2: "acting in that capacity"

- Provision: 5(2), flush text at `-- src:154`.
- Field: `how acting in that capacity qualifies the persons named in Article 5(2)`.
- The words stand at the paragraph's own indentation in the source (two spaces, the indentation of "(2)"), not at the list's (four), so they are tail text of the paragraph: they qualify (a), (b) and (c) together, not only (c).
- Readings.
  - A (taken), `the person must be permitted to act as a Minister, a member of the States Assembly or an equivalent`: the bar applies where the constitution expressly permits the person to control the entity, or be a governor, AS a Minister, member or equivalent (ex officio, or in that office).
  - B, `any such person is caught however the person is to act`: the bar applies whenever the constitution expressly permits a person who is a Minister, member or equivalent to control or be a governor, whatever the capacity.
- Why A: on B the words do no work; the mischief is political control of a charity, which is a matter of office and not of the individual.
- Representation: `Permission that a constitution expressly makes`, field `acting in that capacity`. The caller records one permission per express permission in the constitution's text.
- Discriminating case: a trust deed expressly permits a sitting member of the States Assembly to be a trustee in a personal capacity. A: not barred. B: barred. Tests: `g2-tests-art5` section "FORK F2.2". Red: 1.

### F2.3: "a Minister" or "the Minister"

- Provision: 5(2)(a) (`-- src:151`), against Article 1 "Minister" (`-- src:26`); trap T4.
- Field: `what a Minister means in Article 5(2)(a)`.
- Readings.
  - A (taken), `any Minister of the Government of Jersey`: the context displaces the definition (Article 1's lead-in is "unless the context otherwise requires"). Licence: 5(2)(a) says "a Minister", with the indefinite article, in a list with "a member of the States Assembly"; the same Article says "the Minister" where the defined office is meant (5(3), 5(6)(a)(ii), 5(7), 5(8)). The drafter used both, in one Article, for different things.
  - B, `only the Minister, as Article 1 defines the term in the text in force`: the defined term. Article 1 defines "Minister" as one office, which has changed with the text of the Law (the Chief Minister in the text of 2 October 2026; the Minister for External Relations in the text of 16 October 2025, since R&O.102/2026 Article 1 substitutes "Chief Minister" for "Minister for External Relations" in the definition from 2 October 2026; and so on; which text is in force is group G7's IP2).
- Why A: the contrast of "a Minister" and "the Minister" inside Article 5, and the purpose of the bar.
- Representation: `Person named in Article 5(2)`, constructor `a Minister`, which carries the office that Article 1 calls the Minister if the Minister holds it (`MAYBE Office of the Minister`; NOTHING for any other ministerial office, the Minister for Health, say, since domain.l4's enumeration lists only the three offices the definition has named). B compares it with the input `the office of the Minister` (IP3).
- Discriminating cases. (1) A constitution permits the Minister for Health to be a governor, acting as such: A barred; B not barred. (2) A constitution permits the Minister for External Relations: on B it is barred where that office is "the Minister" (the text of 16 October 2025) and not where it is not (the text of 2 October 2026). Tests: `g2-tests-art5` section "FORK F2.3". Red: 1.

### F2.4: "within a reasonable time" and "as soon as practicable" (periods P1 and P2)

- Provisions: 5(7) (`-- src:164`), 5(8) (`-- src:165`). Kind of period: a standard of promptness, with no number; forward from an event (issuing or amending the guidance; the Minister's receipt).
- Field: `how a standard of promptness is measured`.
- Readings.
  - A (taken), `by an input judgement that the time taken was reasonable or practicable`: the regulative rule has no `WITHIN`; the compliance Boolean reads an input (`the time taken was a reasonable time`, `it was laid as soon as practicable`) and the date on which the act was done.
  - B, `by a number of days counted from the event`: an extra input N (`the number of days that counts as a reasonable time`, `... as soon as practicable`); the rule is `WITHIN N OF` the date of the event; the Boolean tests the date of the act against it.
- Why A: the Law states no number, and the BRIEF forbids inventing one.
- Discriminating case: guidance issued 1 January 2026, copy provided 1 March 2026, N = 30. A: whatever the input says. B: late. Tests: `g2-tests-art5` sections "Article 5(7)" and "Article 5(8)". Red: 1.

### F2.5: a philosophical-belief purpose: (p) or (c)?

- Provisions: 6(2)(f) (`-- src:194`), 6(1)(c) (`-- src:170`), 6(1)(p) (`-- src:183`); trap T27; consumed by group G8 (28(1)(a), fork F8.3) through IP11.
- Field: `which head a philosophical belief falls within`.
- Readings.
  - A (taken), `paragraph (1)(p), by the analogy that Article 6(2)(f) states`: the text says "for the purposes of paragraph (1)(p), the advancement of any philosophical belief ... is analogous to the purpose set out in paragraph (1)(c)". The purpose is within (p); it is charitable; it is not within (c).
  - B, `paragraph (1)(c), as if the analogy made it a purpose of advancing religion`: analogy as identity.
- Why A: the clause is limited by its own words to (p), and an analogy to a thing is not the thing.
- What does not differ: the purpose is a charitable purpose on both readings. The fork changes `Art 6 the entity has a purpose within the advancement of religion` (IP11) only.
- Discriminating case: a humanist association's purpose. Tests: `g2-tests-art6` section "Article 6(2)(f)", which holds the IP11 assertions on both readings. Red: 1.

### F2.6: how the days of a period measured from an event are counted (periods P1 and P2 under F2.4's second reading)

- Provisions: 5(7), 5(8). Kind of period: forward, in days, from an event, inclusive at its far end (an act on the last day is in time).
- Field: `how the days of a measured period are counted`.
- Readings. A (taken), `the day of the event is not counted, so the day after it is the first day`: "within 30 days after" 1 January 2026 ends on 31 January. B, `the day of the event is the first day`: it ends on 30 January.
- Licence for A: the period runs "after" the event (5(7) "after issuing or amending", 5(8) "after the Minister receives"). The Interpretation (Jersey) Law 1954 would settle it and is not among the sources.
- Discriminating case: the copy provided on 31 January 2026 for guidance issued on 1 January and N = 30. A: in time. B: late. The fork is read only when days are counted: on F2.4's first reading it changes nothing (tested). Tests: the same sections, with a trace on each side of the edge for each reading. Red: 1.

### F2.7: "Before issuing or amending guidance" (period P3)

- Provision: 5(6) (`-- src:158`); the lead-in governs both (a) and (b). Kind of period: a backward boundary; the question is whether the boundary day is "before".
- Field: `how before issuing or amending guidance is read`.
- Readings. A (taken), `the consultation and the report must fall on an earlier day than the day the guidance is issued or amended`; B, `the consultation and the report may fall on the day the guidance is issued or amended`.
- Why A: "before" is strict, and a rule on dates alone cannot order two events within one day.
- Under both: the consultation may not come after the report, because the report is "on the Commissioner's views on the results of the consultation" (it may fall on the same day).
- Discriminating case: the report published on the day the guidance is issued. Tests: `g2-tests-art5` section "Article 5(6)". Red: 1.

### F2.8: do the examples in 4(3) add to 4(2)?

- Provision: 4(3), 4(3)(a) to (c) (`-- src:133-136`). The text: "may in particular, without prejudice to the generality of his or her powers".
- Field: `whether the examples in Article 4(3) add to Article 4(2)`.
- Readings. A (taken), `the examples illustrate Article 4(2) and are bound by its conditions`: "in particular" particularises the general power of 4(2); "without prejudice to the generality" says that the examples do not narrow it, not that they widen it. B, `each example is a power in its own right`: each paragraph is read as a grant.
- Discriminating case: assisting an equivalent body outside Jersey, where the assistance relates to no function of the Commissioner. A: no power. B: power. Tests: `g2-tests-art3-4` section "Article 4(3)". Red: 1.

### F2.9: "so far appears to him or her to be reasonably practicable"

- Provision: 4(4) (`-- src:137`; the source reads "so far appears", with no "as", in both texts: section 6).
- Field: `how so far as reasonably practicable qualifies Article 4(4)`.
- Readings. A (taken), `each limb binds so far as it appeared reasonably practicable`: "so far as" means "to the extent that", so the qualification works limb by limb. B, `the standard binds only if it appeared reasonably practicable to act in the whole way`: the qualifier governs the one sentence "seek to act in a way that (a) and (b)" and not its limbs.
- Why A: B releases the Commissioner from every limb when any one is impracticable.
- Discriminating case: the first limb was practicable and not sought, the last limb was not practicable. A: broken. B: the standard did not bind. Tests: `g2-tests-art3-4` section "Article 4(4)". Red: 1.

### F2.10: what follows from a determination of public benefit made in breach of the duties on its maker

- Provisions: 5(5) (`-- src:157`), 7(2), 7(3) (`-- src:204-212`). 5(5) binds any person determining to have regard to the guidance; 7(1) names the Commissioner, the tribunal and the court as bound by 7(2) and 7(3) (F2.13 adds the Commissioner's staff on its first reading). The Law does not say what follows from a breach.
- Field: `what follows from a determination made in breach of the duties on its maker`.
- Readings. A (taken), `the determination does not answer the question`: the encoding refuses, with the named refusal "a determination made in breach of the duties on its maker does not answer the question whether the entity provides public benefit". B, `the finding of the determination stands`: the duties bind conduct and do not change the result. C, `the entity is treated as not providing public benefit`.
- Why A: where the source does not answer, the BRIEF's rule is REFUSE; nothing in the text makes a defective determination either void or valid.
- Not subject to the fork: 7(3)(b) says "accordingly must not treat an entity that benefits only [identified natural persons] as providing public benefit". For the Commissioner, the tribunal and the court the answer is FALSE on all three readings (and, on the first reading of F2.13, for a member of the Commissioner's staff exercising the Commissioner's function).
- Discriminating case: the Commissioner presumed a charitable purpose to be for the public benefit and found that the entity provides it. Tests: `g2-tests-art7` section "Article 5(1)(b) with Article 7" and `g2-tests-art5` section "A barred entity, and a determination that does not answer". Red: 1.

### F2.11: "the promotion of equality and diversity"

- Provision: 6(1)(l) (`-- src:179`).
- Field: `how equality and diversity is read`.
- Readings. A (taken), `a purpose must promote both equality and diversity`: the drafter wrote "or" in (j) ("human rights, conflict resolution or reconciliation") and (k) ("religious or racial harmony") and "and" here. B, `a purpose that promotes either equality or diversity suffices`: a theme named by a compound.
- Representation: two `MAYBE BOOLEAN` facts of `Facts about a purpose under Article 6` (`the purpose promotes equality`, `the purpose promotes diversity`), read only when the head recorded is (l); if they are not stated and the reading cannot decide without them, the encoding refuses (named refusal).
- Discriminating case: a purpose that promotes diversity but not equality. Tests: `g2-tests-art6` section "Article 6(1)(l)". Red: 1.

### F2.12: which guidance do Articles 5(6) to 5(8) apply to?

- Provisions: 5(6), 5(7), 5(8) (`-- src:158-165`); Article 11(6)(b): "Articles 5(6) to (8) apply to that guidance as they apply to guidance under Article 5(4)" (`-- src:331`).
- Field: `which guidance Articles 5(6) to 5(8) apply to`.
- Readings. A (taken), `the guidance under Article 5(4), including the guidance on public benefit that Article 7(4) requires it to contain`: 5(4) and 5(5) say "the guidance"; 5(6) says "guidance"; and 11(6)(b) would be unnecessary if 5(6) to (8) already reached all guidance. B, `any guidance that the Commissioner issues or amends`: 5(6) says "guidance" without qualification, and 4(1)(d) obliges the Commissioner to publish guidance on the operation of the Law generally.
- Discriminating case: guidance on the duties of governors under 4(1)(d), covering no 5(4) subject. A: not in scope. B: in scope.
- Representation: only `Art 5(6) Articles 5(6) to 5(8) apply to the guidance` depends on the fork (it takes the list of subjects the guidance covers); the DEONTIC rules and the date Booleans of 5(6) to 5(8) assume the guidance is in scope, as they must for 11(6)(b)'s guidance, which group G4 wires in. Tests: `g2-tests-art5` section "Article 5(6)" (the F2.12 assertions). Red: 1.

### F2.13: is a member of the Commissioner's staff, exercising the Commissioner's function, bound as the Commissioner is?

- Provisions: 7(1) (`-- src:203`) names the Commissioner, the Charity Tribunal and the court, and no one else. 5(5) (`-- src:157`) names, for functions other than determining, the Commissioner, the Charity Tribunal, a registered charity and a governor of a registered charity. Schedule 1 paragraph 4(3) (`-- src:796`): "Any function of the Commissioner may, to the extent authorized by the Commissioner, be exercised on behalf of the Commissioner by any member of the Commissioner's staff", except three decisions of Articles 11, 15(3) and 16 (`-- src:797-799`); paragraph 4(2) (`-- src:795`) treats a States' employee made available under paragraph 4(1) as a member of the Commissioner's staff.
- Field: `whether the Commissioner's staff exercising the Commissioner's function are bound`.
- Readings. A (taken, the fleet default), `a member of staff exercising a function of the Commissioner under Schedule 1 paragraph 4(3) is bound as the Commissioner is`: a function exercised on the Commissioner's behalf is the Commissioner's function, so the duties that attach to the Commissioner's functions go with it; otherwise authorizing staff would take a determination out of Article 7(3)(b). (An example outside this group: the Commissioner's belief that a registered charity does not pass the charity test, Article 27(1)(b), `-- src:642`; Article 27 is not among the three decisions that paragraph 4(3) excepts, `-- src:797-799`.) B, `only the persons that Article 7(1) and Article 5(5) name are bound`: Article 7(1) names only the Commissioner, the tribunal and the court, a member of staff is none of the three, and a finding by anyone else stands (the point made by test author A-14).
- Representation: the constructor `a member of the Commissioner's staff` of `Legal actor` (domain.l4) stands for a member of staff exercising a function of the Commissioner under that authority; a member of staff acting otherwise is recorded by the caller as `any person`. The fork is decided in one rule, `Arts 7(1) and 5(5) the Commissioner's staff are bound as the Commissioner is` (module `g2-art7-public-benefit`), which delegates by `CONSIDER` to one private rule per reading (`reading A of F2.13: a function exercised on the Commissioner's behalf carries the Commissioner's duties` and `reading B of F2.13: only the persons the Articles name are bound`, both callable and both tested), and which `Art 7(1) Articles 7(2) and 7(3) apply to the person` and `the person is one of those whom Article 5(5) binds in other functions` call for that constructor and for no other. Every rule that read `Art 7(1) ...` now takes `interp` (section 11 lists them).
- What the fork does not decide: the three decisions that paragraph 4(3) excepts (Articles 11, 15(3), 16) are not Articles 3 to 7 and are not modelled here; whether a given act was in fact authorized is the caller's fact (the choice between the constructor `a member of the Commissioner's staff` and `any person`).
- Discriminating case: a member of staff, authorized under paragraph 4(3), finds that an entity that benefits only one named natural person provides public benefit. A: 7(3)(b) binds the finding, so the entity does not provide public benefit (FALSE). B: Article 7(1) does not name staff, so the finding stands and the entity provides public benefit (TRUE). Tests: `g2-tests-art7` sections "Article 7(1)" and "Article 5(1)(b) with Article 7", `g2-tests-art5` section "FORK F2.13". Red: 1.

### Ambiguities met that did not become forks

Each is a place where the text can be read two ways but where the Law has no case that the two readings answer differently, or where the point is a judgement the caller records. They are listed so that a reviewer can disagree with the decision cheaply.

- 5(1) "meets the charity test if": read as "if and only if". The Law has no other route to meeting the test, so no case discriminates; a caller who reads "if" as sufficient only would get no answer for an entity that fails (a) or (b), and the encoding gives FALSE.
- 5(2) "expressly permits": the permission recorded is a fact about the constitution's text. A constitution that requires a Minister to be a governor is recorded by the caller as expressly permitting it, since 8(3)(i) asks for "the text of the provision in the constitution that falls within paragraph (2)", which is the provision. If the caller records nothing, there is no permission.
- 5(2) "any of its governors": any one governor suffices; there is no reading by number or proportion.
- 5(6)(a)(i) "any persons appearing to the Commissioner to be representative": all such persons; whom the Commissioner thinks representative is the Commissioner's opinion (the input `any persons appear to ...`), and the consultation is one fact. The same for (iii).
- 7(2)(a): "how any (i) benefit ..., and (ii) disbenefit ..., in consequence of the entity exercising its functions, compares with the benefit gained ... by the public": (i) and (ii) are two objects of one comparison, and the flush text at `-- src:208` is at the level of (a). Recorded as one fact of regard.
- 7(3)(b) "natural person": only natural persons. An entity that benefits only a company is not caught by the override; whether it provides public benefit is the determiner's finding.
- 5(1)(b) "in Jersey or elsewhere": no Jersey nexus is required; the nexus is Article 11(4)(c).
- 4(2) "a charity or ... an entity with charitable purposes": an input fact; the Law defines only "registered charity".

## 3. Answer table

Each row is a scenario run by a green test; "FR" is the favoured interpretation (`g2-readings`). `Cases` are the fixtures of `g2-fixtures`; "proper determination" means one made with regard to the guidance, the comparison of 7(2)(a) and (where it applies) 7(2)(b), presuming nothing.

| scenario | answer | Article |
| --- | --- | --- |
| Purely educational entity, proper determination that it provides public benefit, no constitutional permission, no Order | meets the charity test (FR); `none: the entity meets the charity test` | 5(1)(a), 5(1)(b), 6(1)(b), 7 |
| Two charitable purposes and an ancillary one beside them | meets the test | 5(1)(a)(i), (ii) |
| A purpose under no head, beside an educational one | fails 5(1)(a); the limb names that purpose | 5(1)(a), 6(1) |
| Proper determination that the entity does not provide public benefit | fails 5(1)(b) | 5(1)(b) |
| Both (a) and (b) fail | the limb that decides is 5(1)(a) | 5(1) |
| Applicant that intends to provide public benefit | meets (b) | 5(1)(b) |
| Registered charity or unregistered entity that only intends to provide it | does not meet (b) | 5(1)(b) |
| A political purpose, alone or beside an educational one | fails 5(1)(a) | 6(5), 5(1)(a) |
| A political purpose flagged ancillary | does not count as ancillary; fails 5(1)(a) | 6(5), 5(1)(a)(ii) |
| Political purpose recorded under education | not a charitable purpose | 6(5), 6(1)(b) |
| Empty purposes (F2.1) | A fails, B and C satisfy | 5(1)(a) |
| An ancillary purpose alone (F2.1) | A and B fail, C satisfies | 5(1)(a)(ii) |
| Constitution expressly permits a governor to be the Chief Minister acting as such | barred; the limb that decides is 5(2) | 5(2)(a) |
| Constitution expressly permits control by a member of the States Assembly | barred | 5(2)(b) |
| Constitution expressly permits a governor to be an equivalent in another jurisdiction | barred | 5(2)(c) |
| Governor may be a member of the States Assembly in a personal capacity (F2.2) | A not barred, B barred | 5(2) |
| Governor may be the Minister for Health acting as such (F2.3) | A barred, B not barred | 5(2)(a), Article 1 "Minister" |
| Minister for External Relations permitted; office of "the Minister" is the Chief Minister (F2.3 B) | not barred; barred if the office is External Relations | 5(2)(a), Article 1 "Minister" |
| Order under 5(3) disapplies 5(2) for a barred entity | meets the test, and only by virtue of the Order | 5(3), 8(3)(i) |
| Order for an entity the constitution does not catch | meets the test, not by virtue of the Order | 5(3) |
| Order, but the entity fails (a) or (b) | does not meet the test; not by virtue of the Order | 5(3) |
| Barred entity, determination made in breach (F2.10 A) | test FALSE (bar asked first); the limb that decides REFUSES | 5(2), 7 |
| Not barred, passes (a), determination made in breach (F2.10) | A refuses; B meets; C does not | 5(1)(b), 7(3)(a) |
| Entity benefits only identified natural persons, found to provide public benefit by the Commissioner, tribunal or court | FALSE on every reading of F2.10 | 7(3)(b) |
| The same by a governor of a registered charity (with regard to the guidance) | the finding stands | 7(1), 5(5) |
| Sport without physical skill and exertion | not within head (h); not charitable | 6(2)(c), 6(1)(h) |
| Sport with physical skill and exertion | charitable | 6(1)(h) |
| Sport, exertion not stated | REFUSES | 6(2)(c) |
| Recreation for neither the needy nor the public at large | not within head (i) | 6(2)(d) |
| Recreation open to the public at large, or for the needy | within head (i) | 6(2)(d)(i), (ii) |
| Prevention or relief of sickness, regeneration, civic responsibility, relief by accommodation or care, with no head recorded | charitable (extensions) | 6(2)(a), (b), (e) |
| Philosophical belief (F2.5) | charitable on both; within (c) only on B | 6(2)(f), 6(1)(p), 6(1)(c) |
| Promotes diversity but not equality (F2.11) | A not charitable; B charitable | 6(1)(l) |
| Regulations add a sub-paragraph to 6(1) | within the power | 6(3)(a) |
| Regulations add explanatory sub-paragraphs to 6(2) | within the power only if explanatory of added 6(1) sub-paragraphs | 6(3)(b) |
| Regulations amend or restrict 6(1)(a) to (p) or 6(2)(a) to (f), or alter 6(5) | outside the power | 6(4) |
| States may make Regulations | only on the Commissioner's recommendation and within the limit | 6(3), 6(4) |
| 4(1)(d), 5(4): the Commissioner has published nothing, any length of time | the duty stands; never a breach | 4(1)(d), 5(4) |
| Guidance on the charity test only | does not discharge the 4(1)(d) duty | 4(1)(d) |
| Governor of a registered charity performing another function to which the guidance is relevant | must have regard to the guidance | 5(5) |
| The Minister, or the court, performing another function | no duty under the second limb of 5(5) (the court, as a determiner, is bound by the first) | 5(5) |
| Consultation omitting the Minister | does not discharge 5(6)(a) | 5(6)(a)(ii) |
| Report published on the day the guidance is issued (F2.7) | A not before; B before | 5(6) |
| Guidance issued 2026-01-01, copy 2026-01-31, N = 30 (F2.4 B) | in time with the day of issue not counted (F2.6 A); late with it counted (F2.6 B: the last day is 30 January) | 5(7) |
| The same, copy 2026-03-01 | A: whatever the input says; B: late | 5(7), 5(8) |
| Assistance to a foreign equivalent body that relates to no function of the Commissioner (F2.8) | A no power; B power | 4(3)(c) |
| First limb practicable and not sought, last not practicable (F2.9) | A broken; B no duty | 4(4) |
| Guidance on the duties of governors under 4(1)(d) only (F2.12) | A out of 5(6) to (8); B in | 5(6) |
| Recreational facilities open to the public at large, the object of improving the conditions of life stated NOT to hold (a public amusement arcade) | not within head (i); not charitable | 6(1)(i), 6(2)(d)(ii) |
| Recreational facilities with the object of improving the conditions of life, for people in need or open to the public at large | within head (i) | 6(1)(i), 6(2)(d) |
| Recreational facilities with the object, neither for people in need nor open to the public at large | not within head (i) | 6(2)(d) |
| Recreational facilities, the object not stated, 6(2)(d) holds | REFUSES (a named refusal) | 6(1)(i) |
| A partnership, or an NPO body corporate on 15 October 2025 (before paragraph (ba)), with a charitable purpose and a proper determination | does not meet the charity test (FALSE, not a refusal); the limb that decides is `Article 5(1) does not apply: the body is not an entity within Article 2(1)` | 5(1), 2(1) |
| The same body with an Order disapplying 5(2) | does not meet the test, and not by virtue of an Order | 5(1), 5(3) |
| A member of staff, authorized under Schedule 1 paragraph 4(3), finds that an entity that benefits only one named natural person provides public benefit (F2.13) | A: the entity does not provide public benefit; B: it does | 7(1), 7(3)(b), Sch 1 para 4(3) |
| A member of staff performing another function to which the guidance is relevant (F2.13) | A: must have regard to the guidance; B: not bound | 5(5), Sch 1 para 4(3) |

## 4. Nouns requests for the INTEGRATOR

`domain.l4` is read-only, so each noun below is declared in `g2-nouns` as a local stand-in.

- N1. `Facts about a purpose under Article 6` and `Purpose with the facts Article 6 reads`. Article 6(2) narrows head (h) and head (i), extends heads (d), (f) and (n), and head (l) joins two ideas; `Purpose` carries only the head and three flags. Request: add the ten fields of `Facts about a purpose under Article 6` (the tenth, the object of improving the conditions of life, was added after independent testing) to `Purpose` (the three-valued ones as `MAYBE BOOLEAN`), so that `Entity.purposes` carries them; G2's headline would then drop its parallel list `the purposes with their Article 6 facts`. Until then the charity test takes the entity and the list, and refuses if the list is not the entity's purposes.
- N2. `Facts about the constitution under Article 5(2)` (a list of `Permission that a constitution expressly makes`, with `Person named in Article 5(2)` and `What a constitution expressly permits`). It is a fact about the constitution (Article 2(4)), which G1 owns. Request: a field of `Entity` or of G1's constitution record. 8(3)(i) (G3) asks for "the text of the provision in the constitution that falls within paragraph (2)", so the permission's text should be recorded with it.
- N3. `Determination of public benefit`: who determined, what was found, and what the determiner did and did not do. It is not a fact about the entity but a record of a decision; the integrator needs one per time the test is applied (IP9: at the application and at the appeal). No change to `domain.l4` is requested; the integrator decides where it lives.
- N4. `Act under Articles 3 to 7` and `Subject of the Commissioner's guidance`: local to the group. If the integrator wants one act type across the fleet, the constructors are named for what is done and not for an Article, and each carries its performer as its first `Legal actor` field.
- N5. `Limb of the charity test that decides it`: local. It has a sixth constructor since the repair, `Article 5(1) does not apply: the body is not an entity within Article 2(1)`; a `CONSIDER` over it elsewhere must be extended.
- N6. `Interpretation of Articles 3 to 7` and its thirteen enumerations: local.
- N7. `Legal actor` (domain.l4) is matched exhaustively in `Art 7(1) Articles 7(2) and 7(3) apply to the person` and in `the person is one of those whom Article 5(5) binds in other functions`, and `Head of charitable purpose` in `Art 6(1) the head admits the purpose`. If a constructor is added, those matches must be extended; the compiler says where.

Standard inputs consumed. `the entity` : `Entity` (IP5: its `standing on the register`, for "applicant", and its `purposes`); `the office of the Minister` : `Office of the Minister` (IP3, read only on the second reading of F2.3). Also consumed since the repair: `the entity`'s `kinds of entity` (IP5, empty for a body that is not an entity). Not consumed: `the day` and `the vintage of the text` (IP1, IP2): this group decides nothing by the day of the question. Everything else is a group-local input, named in section 5.

## 5. Standard inputs consumed and functions exported

`@export` is on every function below, with a sentence that says what it answers and a `@desc` on every `GIVEN`. Names are exact (they are the `l4` identifiers, with backticks). A function that depends on a fork takes `interp`.

Additions to PLAN section (b)'s signatures, which the integrator must wire (they are not standard names): `Art 5 the entity meets the charity test` and its siblings (IP8, IP10, the limb function) take `the purposes with their Article 6 facts` (N1) and `the office of the Minister` (IP3) in addition to PLAN's inputs; `Art 5(2) the constitution defeats the charity test` takes `the office of the Minister`; `Art 5(6) the Commissioner must consult and publish a report ...` takes two opinions of the Commissioner; `Art 5(7)` and `Art 5(8)` take the date of the event and N; the Art 7 exports take the entity. Types are written with their backticks where a name has spaces. Since the repair, nine exports take `interp` as a last `GIVEN` and are listed in section 11.

IP8: `the entity meets the charity test` : BOOLEAN is produced by `Art 5 the entity meets the charity test`. IP9: the same export, evaluated twice by the integrator, once on the facts at the time of the application and once at the time of the appeal. IP10: `Art 5(3) the entity meets the charity test only by virtue of an Order`. IP11: `Art 6 the entity has a purpose within the advancement of religion`. The charity test's `Art 5(6)` to `Art 5(8)` rules are reusable for Article 11(6)(b); the scope question is `Art 5(6) Articles 5(6) to 5(8) apply to the guidance`.

40 exported functions.

**`Art 4(1)(d) the Commissioner must publish and maintain guidance on the operation of the Law`**

- module: `g2-art3-4-commissioner`
- answers: The Commissioner's standing duty under Article 4(1)(d) to publish and maintain guidance on the operation of the Law, including the duties of governors and the charity test; it has no deadline and stays standing until performed
- takes: nothing
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 4(2) the Commissioner has power to do the thing`**

- module: `g2-art3-4-commissioner`
- answers: Whether the Commissioner has power under Article 4(2) to do a thing: the thing must be calculated to facilitate, or be conducive or incidental to, the performance of a function, and must not be acting as a governor of a charity or of an entity with charitable purposes
- takes:
  - `the thing is calculated to facilitate, or is conducive or incidental to, a function` : BOOLEAN
  - `the thing is acting as a governor of a charity or of an entity with charitable purposes` : BOOLEAN
- gives: BOOLEAN

**`Art 4(2) the Commissioner may do the thing`**

- module: `g2-art3-4-commissioner`
- answers: The Commissioner's permission under Article 4(2) to do a thing; the permission exists only where Article 4(2) gives the Commissioner power to do it, and an unused permission is not a breach
- takes:
  - `the thing is calculated to facilitate, or is conducive or incidental to, a function` : BOOLEAN
  - `the thing is acting as a governor of a charity or of an entity with charitable purposes` : BOOLEAN
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 4(3) the Commissioner has power to do the listed example`**

- module: `g2-art3-4-commissioner`
- answers: Whether the Commissioner has power under Article 4(3) to do one of the three listed examples, on the reading of Article 4(3) chosen by the interpretation
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `example` : `Example listed in Article 4(3)`
  - `the thing is calculated to facilitate, or is conducive or incidental to, a function` : BOOLEAN
  - `the thing is acting as a governor of a charity or of an entity with charitable purposes` : BOOLEAN
- gives: BOOLEAN

**`Art 4(3) the Commissioner may do the listed example`**

- module: `g2-art3-4-commissioner`
- answers: The Commissioner's permission under Article 4(3) to do one of the three listed examples, on the reading of Article 4(3) chosen by the interpretation; an unused permission is not a breach
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `example` : `Example listed in Article 4(3)`
  - `the thing is calculated to facilitate, or is conducive or incidental to, a function` : BOOLEAN
  - `the thing is acting as a governor of a charity or of an entity with charitable purposes` : BOOLEAN
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 4(4) the Commissioner has sought to act as Article 4(4) requires`**

- module: `g2-art3-4-commissioner`
- answers: Whether the Commissioner has sought to act as Article 4(4) requires in performing a function, on the reading of the practicability qualification chosen by the interpretation
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `how` : `How the Commissioner acted in performing a function`
- gives: BOOLEAN

**`Art 4(4) the Commissioner must seek to act as Article 4(4) requires`**

- module: `g2-art3-4-commissioner`
- answers: The Commissioner's standing duty under Article 4(4) to seek to act, in performing a function, in a way that protects public trust and confidence in registered charities and is proportionate; it has no deadline
- takes: nothing
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 6(1) the purpose is a charitable purpose`**

- module: `g2-art6-purposes`
- answers: Whether a purpose is a charitable purpose under Article 6(1), as clarified by Article 6(2) and excluded by Article 6(5), on the readings chosen by the interpretation; the head recorded for the purpose is the caller's determination
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `purpose` : Purpose
  - `facts` : `Facts about a purpose under Article 6`
- gives: BOOLEAN

**`Art 6 the entity has a purpose within the advancement of religion`**

- module: `g2-art6-purposes`; IP11 (`the entity has a purpose within Article 6(1)(c)` : BOOLEAN)
- answers: Whether the entity has a purpose that falls within Article 6(1)(c), the advancement of religion; a purpose of advancing a philosophical belief counts only on the second reading of fork F2.5
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
- gives: BOOLEAN

**`Art 6(3) the States may add a sub-paragraph to Article 6(1) or (2)`**

- module: `g2-art6-purposes`
- answers: The States' permission under Article 6(3) to make Regulations adding sub-paragraphs to Article 6(1) and explanatory sub-paragraphs to Article 6(2); the power exists only on the recommendation of the Commissioner, and the content of the Regulations is not modelled here
- takes:
  - `the Commissioner has recommended the Regulations` : BOOLEAN
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 6(4) the Regulations are within the power of Article 6(3)`**

- module: `g2-art6-purposes`
- answers: Whether Regulations are within the power of Article 6(3) as limited by Article 6(4): they must add sub-paragraphs to paragraph (1), or explanatory sub-paragraphs to paragraph (2), and must not amend or restrict paragraphs (1)(a) to (p) and (2)(a) to (f) or alter paragraph (5)
- takes:
  - `content` : `Content of Regulations under Article 6(3)`
- gives: BOOLEAN

**`Art 6(3) the States may make the Regulations`**

- module: `g2-art6-purposes`
- answers: Whether the States may validly make the Regulations: the Commissioner has recommended them (Article 6(3)) and their content is within the power as limited by Article 6(4)
- takes:
  - `the Commissioner has recommended the Regulations` : BOOLEAN
  - `content` : `Content of Regulations under Article 6(3)`
- gives: BOOLEAN

**`Art 6(5) the purpose is neither charitable nor ancillary`**

- module: `g2-art6-purposes`
- answers: Whether a purpose is excluded by Article 6(5) as the purpose of advancing a political party or promoting a candidate for election, in Jersey or elsewhere; such a purpose is neither a charitable purpose nor a purpose ancillary or incidental to a charitable purpose
- takes:
  - `purpose` : Purpose
- gives: BOOLEAN

**`Art 7(1) Articles 7(2) and 7(3) apply to the person`**

- module: `g2-art7-public-benefit`
- answers: Whether Article 7(2) and (3) bind a person who determines whether an entity provides or intends to provide public benefit: they bind the Commissioner, the Charity Tribunal and the court, and (on the first reading of fork F2.13) a member of the Commissioner's staff exercising the Commissioner's function under Schedule 1 paragraph 4(3), and no one else
- takes:
  - `who` : `Legal actor`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: BOOLEAN

**`Art 7(2)(a) the person determining must have regard to the comparison of benefit and disbenefit`**

- module: `g2-art7-public-benefit`
- answers: The standing duty under Article 7(2)(a) of the Commissioner, the tribunal or the court (and, on the first reading of fork F2.13, of a member of the Commissioner's staff exercising the Commissioner's function), when determining public benefit, to have regard to how benefit to members or others and disbenefit to the public compare with benefit to the public; it binds no one else
- takes:
  - `who` : `Legal actor`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 7(2)(b) the person determining must have regard to whether a condition on obtaining the benefit is unduly restrictive`**

- module: `g2-art7-public-benefit`
- answers: The standing duty under Article 7(2)(b) of the Commissioner, the tribunal or the court (and, on the first reading of fork F2.13, of a member of the Commissioner's staff exercising the Commissioner's function), where benefit is or is likely to be provided to a section of the public only, to have regard to whether any condition on obtaining the benefit, including a charge or fee, is unduly restrictive
- takes:
  - `who` : `Legal actor`
  - `benefit is, or is likely to be, provided to a section of the public only` : BOOLEAN
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 7(3) the determination is permitted`**

- module: `g2-art7-public-benefit`
- answers: Whether a determination of public benefit is permitted by Article 7(3): it presumed no charitable purpose to be for the public benefit and did not treat identified natural persons as a section of the public; the paragraph binds the Commissioner, the tribunal and the court (and, on the first reading of fork F2.13, a member of the Commissioner's staff exercising the Commissioner's function), so it is satisfied vacuously by any other determiner
- takes:
  - `determination` : `Determination of public benefit`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: BOOLEAN

**`Art 7(3)(a) the person determining must not presume a charitable purpose to be for the public benefit`**

- module: `g2-art7-public-benefit`
- answers: The standing prohibition under Article 7(3)(a) on the Commissioner, the tribunal or the court (and, on the first reading of fork F2.13, on a member of the Commissioner's staff exercising the Commissioner's function) presuming any particular charitable purpose to be for the public benefit; it binds no one else
- takes:
  - `who` : `Legal actor`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 7(3)(b) the person determining must not treat identified natural persons as a section of the public`**

- module: `g2-art7-public-benefit`
- answers: The standing prohibition under Article 7(3)(b) on the Commissioner, the tribunal or the court (and, on the first reading of fork F2.13, on a member of the Commissioner's staff exercising the Commissioner's function) treating one natural person or a group of identified natural persons as a section of the public; it binds no one else
- takes:
  - `who` : `Legal actor`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 7(3)(b) the person determining must not treat an entity that benefits only identified natural persons as providing public benefit`**

- module: `g2-art7-public-benefit`
- answers: The standing prohibition under Article 7(3)(b) on the Commissioner, the tribunal or the court (and, on the first reading of fork F2.13, on a member of the Commissioner's staff exercising the Commissioner's function) treating an entity that benefits only one natural person or a group of identified natural persons as providing public benefit; it binds no one else
- takes:
  - `who` : `Legal actor`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 7 the determination complies with the duties on its maker`**

- module: `g2-art7-public-benefit`
- answers: Whether a determination of public benefit complies with the duties on its maker: regard to the guidance (Article 5(5)) for every maker, and for the Commissioner, the tribunal and the court (and, on the first reading of fork F2.13, a member of the Commissioner's staff exercising the Commissioner's function) also the regard Article 7(2) requires and the restraints of Article 7(3)
- takes:
  - `determination` : `Determination of public benefit`
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: BOOLEAN

**`Art 7 the entity provides public benefit`**

- module: `g2-art7-public-benefit`
- answers: Whether the entity provides public benefit (or, for an applicant, provides or intends to provide it) to a reasonable degree, on a determination by the Commissioner, the tribunal, the court or anyone else; a determination made in breach of the duties on its maker is treated as the interpretation says
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the public benefit determination` : `Determination of public benefit`
- gives: BOOLEAN

**`Art 7(4) the guidance published under Article 5(4) gives guidance on public benefit`**

- module: `g2-art7-public-benefit`
- answers: Whether the guidance published under Article 5(4) gives guidance on the determination of whether an entity provides or intends to provide public benefit, as Article 7(4) requires; the input is the list of subjects the guidance covers
- takes:
  - `subjects` : LIST OF `Subject of the Commissioner's guidance`
- gives: BOOLEAN

**`Art 5(1)(a) all of the entity's purposes are charitable or purely ancillary`**

- module: `g2-art5-charity-test`
- answers: Whether all of an entity's purposes are charitable purposes or purposes purely ancillary or incidental to its charitable purposes (Article 5(1)(a)), on the reading of "all of its purposes" chosen by the interpretation
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the purposes with their Article 6 facts` : LIST OF `Purpose with the facts Article 6 reads`
- gives: BOOLEAN

**`Art 5(1)(b) the entity provides public benefit to a reasonable degree`**

- module: `g2-art5-charity-test`
- answers: Whether the entity provides public benefit in Jersey or elsewhere to a reasonable degree (or, for an applicant, provides or intends to provide it), as Article 5(1)(b) asks, on a determination of the question
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the public benefit determination` : `Determination of public benefit`
- gives: BOOLEAN

**`Art 5(2) the constitution defeats the charity test`**

- module: `g2-art5-charity-test`
- answers: Whether the constitution of an entity expressly permits what Article 5(2) forbids: the activities of the entity to be directed or otherwise controlled by, or any of its governors to be, a Minister, a member of the States Assembly or an equivalent in another jurisdiction, acting in that capacity; the readings of "a Minister" and of "acting in that capacity" are chosen by the interpretation
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the office of the Minister` : `Office of the Minister`
  - `the constitution facts` : `Facts about the constitution under Article 5(2)`
- gives: BOOLEAN

**`Art 5(3) the Minister may disapply Article 5(2)`**

- module: `g2-art5-charity-test`
- answers: The Minister's permission under Article 5(3) to make an Order disapplying Article 5(2) in relation to an entity or a description of entity; the Order's content is not modelled here, and an unused permission is not a breach
- takes: nothing
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(2) the bar applies to the entity`**

- module: `g2-art5-charity-test`
- answers: Whether Article 5(2) bars the entity from meeting the charity test: its constitution expressly permits what Article 5(2) forbids, and no Order under Article 5(3) disapplies Article 5(2) for the entity
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the office of the Minister` : `Office of the Minister`
  - `the constitution facts` : `Facts about the constitution under Article 5(2)`
  - `an Order under Article 5(3) disapplies Article 5(2) for the entity` : BOOLEAN
- gives: BOOLEAN

**`Art 5 the entity meets the charity test`**

- module: `g2-art5-charity-test`; IP8 (`the entity meets the charity test` : BOOLEAN; IP9 is this function evaluated twice)
- answers: Whether an entity meets the charity test of Article 5: all of its purposes are charitable purposes or purely ancillary or incidental to them, it provides public benefit to a reasonable degree, and Article 5(2) does not bar it; a body that is not an entity (no kind of entity under Article 2(1)) does not meet it, and the answer for such a body is FALSE, not a refusal; the readings of the ambiguous provisions are chosen by the interpretation
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the purposes with their Article 6 facts` : LIST OF `Purpose with the facts Article 6 reads`
  - `the constitution facts` : `Facts about the constitution under Article 5(2)`
  - `the office of the Minister` : `Office of the Minister`
  - `the public benefit determination` : `Determination of public benefit`
  - `an Order under Article 5(3) disapplies Article 5(2) for the entity` : BOOLEAN
- gives: BOOLEAN

**`Art 5(3) the entity meets the charity test only by virtue of an Order`**

- module: `g2-art5-charity-test`; IP10 (`the entity meets the charity test only by virtue of an Order under Article 5(3)` : BOOLEAN)
- answers: Whether an entity meets the charity test only by virtue of an Order under Article 5(3): its constitution is within Article 5(2), an Order disapplies Article 5(2) for it, and it otherwise meets the test; FALSE for a body that is not an entity
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the purposes with their Article 6 facts` : LIST OF `Purpose with the facts Article 6 reads`
  - `the constitution facts` : `Facts about the constitution under Article 5(2)`
  - `the office of the Minister` : `Office of the Minister`
  - `the public benefit determination` : `Determination of public benefit`
  - `an Order under Article 5(3) disapplies Article 5(2) for the entity` : BOOLEAN
- gives: BOOLEAN

**`Art 5 the limb that decides the charity test`**

- module: `g2-art5-charity-test`
- answers: Which limb of the charity test of Article 5 decides it, taken in the order the text states them: Article 5(1)(a), Article 5(1)(b), then Article 5(2) for an entity that otherwise meets the test; or that the entity meets the test; or that the body is not an entity within Article 2(1), so that Article 5(1) does not apply to it and it does not meet the test
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the entity` : Entity
  - `the purposes with their Article 6 facts` : LIST OF `Purpose with the facts Article 6 reads`
  - `the constitution facts` : `Facts about the constitution under Article 5(2)`
  - `the office of the Minister` : `Office of the Minister`
  - `the public benefit determination` : `Determination of public benefit`
  - `an Order under Article 5(3) disapplies Article 5(2) for the entity` : BOOLEAN
- gives: `Limb of the charity test that decides it`

**`Art 5(4) the Commissioner must publish and maintain guidance on the charity test`**

- module: `g2-art5-charity-test`
- answers: The Commissioner's standing duty under Article 5(4) to publish and maintain guidance on the determination of whether an entity meets the charity test; it has no deadline and stays standing until performed
- takes: nothing
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(5) the duty to have regard to the guidance`**

- module: `g2-art5-charity-test`
- answers: The standing duty under Article 5(5) to have regard to the guidance: of any person determining whether an entity meets the charity test, and of the Commissioner, the Charity Tribunal, a registered charity and a governor of a registered charity (and, on the first reading of fork F2.13, a member of the Commissioner's staff exercising the Commissioner's function) when performing any other function under the Law to which the guidance is relevant; "have regard" is the event of a trace
- takes:
  - `who` : `Legal actor`
  - `the person is determining whether an entity meets the charity test` : BOOLEAN
  - `the person is performing another function under this Law to which the guidance is relevant` : BOOLEAN
  - `the person is a governor of a registered charity` : BOOLEAN
  - `interp` : `Interpretation of Articles 3 to 7`
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(6) Articles 5(6) to 5(8) apply to the guidance`**

- module: `g2-art5-charity-test`
- answers: Whether Articles 5(6) to 5(8) (consultation, report, copy to the Minister, laying before the States) apply to guidance on the given subjects: on the first reading only guidance under Article 5(4) and its public benefit content, on the second any guidance the Commissioner issues or amends
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the subjects of the guidance issued or amended` : LIST OF `Subject of the Commissioner's guidance`
- gives: BOOLEAN

**`Art 5(6) the Commissioner must consult and publish a report before issuing or amending guidance`**

- module: `g2-art5-charity-test`
- answers: The Commissioner's duty under Article 5(6), before issuing or amending guidance, to consult those whom Article 5(6)(a) names and then publish a report on the views on the consultation and the reasons for the decision; the consultation event must cover them, and the duty has no deadline of its own
- takes:
  - `any persons appear to the Commissioner to be representative of charities or bodies with charitable purposes` : BOOLEAN
  - `the Commissioner considers that there are other persons whom it is appropriate to consult` : BOOLEAN
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(6) the consultation and the report preceded the guidance`**

- module: `g2-art5-charity-test`
- answers: Whether the Commissioner consulted and published the report before issuing or amending the guidance, on the reading of "before" chosen by the interpretation; the consultation may not come after the report
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the date the guidance was issued or amended` : DATE
  - `the date the consultation was held` : MAYBE DATE
  - `the date the report was published` : MAYBE DATE
- gives: BOOLEAN

**`Art 5(7) the Commissioner must provide the Minister with the guidance and the report`**

- module: `g2-art5-charity-test`
- answers: The Commissioner's duty under Article 5(7), within a reasonable time after issuing or amending guidance, to provide the Minister with a copy of the guidance and the report published under Article 5(6)(b); on the first reading of the standard of promptness it has no deadline, on the second it falls due a number of days after the guidance is issued
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the date the guidance was issued or amended` : DATE
  - `the number of days that counts as a reasonable time` : NUMBER
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(7) the Commissioner provided the Minister with the guidance and the report in time`**

- module: `g2-art5-charity-test`
- answers: Whether the Commissioner provided the Minister with the guidance and the report within a reasonable time after issuing or amending the guidance: on the first reading of the standard of promptness, a copy was provided and the time taken was reasonable (an input); on the second, it was provided within the number of days given
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the date the guidance was issued or amended` : DATE
  - `the date the copy and the report were provided to the Minister` : MAYBE DATE
  - `the time taken was a reasonable time` : BOOLEAN
  - `the number of days that counts as a reasonable time` : NUMBER
- gives: BOOLEAN

**`Art 5(8) the Minister must lay the guidance and the report before the States`**

- module: `g2-art5-charity-test`
- answers: The Minister's duty under Article 5(8) to lay a copy of the guidance and the report before the States as soon as practicable after receiving them; on the first reading of the standard of promptness it has no deadline, on the second it falls due a number of days after receipt
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the date the Minister received the guidance and the report` : DATE
  - `the number of days that counts as as soon as practicable` : NUMBER
- gives: DEONTIC `Legal actor` `Act under Articles 3 to 7`

**`Art 5(8) the Minister laid the guidance and the report before the States in time`**

- module: `g2-art5-charity-test`
- answers: Whether the Minister laid the guidance and the report before the States as soon as practicable after receiving them: on the first reading of the standard of promptness, they were laid and it was as soon as practicable (an input); on the second, they were laid within the number of days given
- takes:
  - `interp` : `Interpretation of Articles 3 to 7`
  - `the date the Minister received the guidance and the report` : DATE
  - `the date the copy and the report were laid before the States` : MAYBE DATE
  - `it was laid as soon as practicable` : BOOLEAN
  - `the number of days that counts as as soon as practicable` : NUMBER
- gives: BOOLEAN

## 6. Contradictions, defects and tensions in the source (a separate pass, made after encoding)

Where I looked. I re-read Articles 3 to 7 against my modules once all were green, provision by provision, for: a cross-reference that points at nothing; two provisions that answer the same question differently; a definition and its use that disagree; a word or punctuation slip. I read the cross-references of other Articles to mine (lines 9, 10, 233, 320, 331, 437, 642, 654, 702, 739, 750 of the source) and the Table of Renumbered Provisions (it touches only original Articles 41 to 44, so no cross-reference of Articles 3 to 7 is affected). I found no pair of provisions in Articles 3 to 7 that gives different answers to the same question. What I found:

- C1. Missing word, 4(4) (`-- src:137`): "so far appears to him or her to be reasonably practicable", for "so far as appears". It is the same in the consolidated text and in the official PDF's text layer. The sense is clear and no reading turns on it (F2.9 is about what "so far as" does, not about the slip).
- C2. 5(1)(b) and 7(1) state the question differently. 5(1)(b): the entity "provides (or, in the case of an applicant, provides or intends to provide) public benefit". 7(1) (`-- src:203`): the Commissioner, the tribunal and the court determine "whether an entity provides or intends to provide public benefit, for the purpose of Article 5(1)(b)", with no limit to applicants. The encoding takes 5(1)(b) as the content of the question and 7(1) as saying to whom 7(2) and (3) apply; discriminating case: a registered charity that intends to provide public benefit but does not yet provide it: under 5(1)(b) it fails. (An operative conflict would arise only if 7(1) were read as widening 5(1)(b); it says it works "for the purpose of" 5(1)(b).)
- C3. 5(6) says "guidance" where 5(4) and 5(5) say "the guidance", and Article 11(6)(b) (`-- src:331`) extends 5(6) to (8) to other guidance "as they apply to guidance under Article 5(4)", which is superfluous if 5(6) already reaches all guidance. Registered as fork F2.12 and not resolved.
- C4. 6(2)(f) against 28(1)(a) (cross-group, trap T27, fork F8.3 of G8). 6(2)(f) makes a philosophical-belief purpose analogous to (c) "for the purposes of paragraph (1)(p)", so it is within (p). 28(1)(a) (`-- src:654`) lets the Minister categorize charities that "appear ... to meet the charity test by virtue of Article 6(1)(c)". On the first reading of F2.5 no humanist body can qualify. Whether the drafter meant that is not in the sources. Discriminating case: a humanist association.
- C5. 11(4)(a) (`-- src:320`, cross-group, G4): "the applicant meets the charity test, or will do so on registration". 5(1)(b) already accommodates an applicant by "intends to provide". The words "or will do so on registration" have no counterpart in 5(1)(a) or 5(2): which limbs may be prospective? Discriminating case: an applicant whose constitution now permits a Minister to be a governor but will be amended on registration. Not resolved here; the test in this group is asked at one time, on the facts given, and G4 decides how to ask it for an applicant.
- C6. 7(4) (`-- src:213`): a comma before the verb ("The guidance published by the Commissioner under Article 5(4), must in particular"). No effect.
- C7. Overlap, consistent: 4(1)(d), 5(4) and 7(4) are three provisions about the same guidance: 4(1)(d) the guidance on the operation of the Law "including guidance ... on the charity test under Article 5(4)"; 5(4) the guidance on the charity test; 7(4) its content on public benefit. They agree (checked); the encoding keeps three subjects of guidance and does not treat one publication as discharging the others (tested).
- C8. Mismatch of vocabulary: 4(2) speaks of "a charity" and "an entity with charitable purposes", the Law defines only "registered charity" and "charitable purpose". No operative effect; the input is a fact the caller records.
- C10. Schedule 1 paragraph 4(3) against 7(1) and 5(5) (cross-group, G9). Paragraph 4(3) lets staff exercise any function of the Commissioner on its behalf; Article 7(1) and the second limb of 5(5) name the Commissioner but not staff. Read literally, a staff determination escapes 7(3)(b). Registered as fork F2.13 (found by the independent test authors).
- C9. In the task description I was given, the copy to the Minister is "under 4(7)"; the Law has no Article 4(7): it is Article 5(7). (A slip in the assignment, not in the source.)

## 7. Open questions for a domain expert

1. Is a philosophical-belief purpose within 6(1)(p) only, or also within (c) for Article 28 (F2.5, C4)?
2. Does 5(6) to (8) bind the Commissioner's other guidance (F2.12)?
3. Does a determination of public benefit made in breach of 7(2) or 7(3) stand, fall or neither (F2.10)? Is a breach of 5(5) different?
4. Is "a Minister" in 5(2)(a) any Minister (F2.3)? Which offices have been "the Minister" in each text of the Law is G1's question.
5. Must the constitution say "permits", or does a provision that requires a Minister to be a governor count as expressly permitting it (the non-fork on "expressly permits")?
6. Does a purely ancillary purpose count alone, and does an entity with no purposes pass (F2.1)?
7. Is "the promotion of equality and diversity" one head that either idea satisfies, or two ideas that must be joined (F2.11)?
8. Is "so far as practicable" in 4(4) a limb-by-limb qualification (F2.9)?
9. Does 4(3) widen the Commissioner's powers (F2.8)?
10. What is a "reasonable time" in 5(7) and "as soon as practicable" in 5(8) in days, if the Commissioner or the States have fixed one; and how are the days counted (F2.4, F2.6)? Is the Interpretation (Jersey) Law 1954 the rule?
11. In 7(2)(a), are the benefit to members and the disbenefit to the public two comparisons or one?
12. What does "or will do so on registration" in 11(4)(a) add to 5(1)(b)'s applicant limb (C5)?
13. Does a function exercised by a member of the Commissioner's staff under Schedule 1 paragraph 4(3) carry the duties that Articles 7(1) and 5(5) attach to the Commissioner (F2.13, C10)?

## 8. What the sources do not answer

- The content of any Order under 5(3) or of any Regulations under 6(3): none is in the sources. The Order is the input `an Order under Article 5(3) disapplies Article 5(2) for the entity`; the Regulations' content is `Content of Regulations under Article 6(3)`. No Order or Regulations is assumed to exist.
- Which entities an Order "specifies", and which a "description of entity" covers: the Order's content.
- What follows from a determination made in breach of 5(5), 7(2) or 7(3) (F2.10): the Law is silent.
- How the days of 5(7) and 5(8) are counted, and whether any number of days has been fixed: the Interpretation (Jersey) Law 1954 is not among the sources (F2.4, F2.6).
- What "a reasonable degree" of public benefit is, what "unduly restrictive" is, what makes persons "identified", what "religion" and "philosophical belief" are, what "sport" involves beyond physical skill and exertion, what a purpose "may reasonably be regarded as analogous" to, what is "purely ancillary or incidental", what an "equivalent" office in another jurisdiction is: determinations, recorded as inputs; none is computed.
- Whether the Commissioner's "functions" in 4(1) include functions conferred by other enactments in a way that bears on 4(2): 4(1)(g) says they do; no list is in the sources.
- Whether the guidance of 5(4) exists, has been issued, or has been laid before the States: facts of the world, not in the sources.
- Who holds the office of Commissioner, and who acts when the holder cannot (Schedule 1, G9).
- The text of the other enactments named in these Articles: none is named in Articles 3 to 7 apart from the Law itself.
- Anything after 2 October 2026.

## 9. Notes for the integrator

1. Wiring (section 5). IP8: call `Art 5 the entity meets the charity test` with `interp` the integrator's choice, `the entity` and `the purposes with their Article 6 facts` (the same purposes, in the same order, with the facts N1), `the constitution facts` (N2), `the office of the Minister` (IP3), `the public benefit determination` (N3) and the Order Boolean. If the facts are not the entity's purposes the function refuses with the named refusal; assert in the integration tests that they are equal.
2. IP9: evaluate IP8 twice, with the facts and determination as they stood at each time.
3. IP10: `Art 5(3) the entity meets the charity test only by virtue of an Order` takes the same seven inputs and is TRUE only if the Order input is TRUE, the constitution is within 5(2) and (a) and (b) hold.
4. IP11: `Art 6 the entity has a purpose within the advancement of religion`; the first reading of F2.5 is the one consistent with 6(2)(f) read as written. G8's F8.3 should be set from the same reading of F2.5 (BRIEF "Forks that must be set together").
5. Commencement. No G2 function gates itself. Articles 3 to 7 are in the first stage (21 November 2014) per the Table of Legislation History; the integrator's wrapper (IP4) asks it.
6. A function that depends on a fork takes the whole record; the 16 values of `g2-readings` are the readings by name. The fork fields are 13; the register above has 13 entries.
7. Article 11(6)(b) (G4): "Articles 5(6) to (8) apply to that guidance as they apply to guidance under Article 5(4)". The G2 rules of 5(6) to (8) do not read the identity of the guidance, so G4 may call them for the guidance on "substantial"; they assume scope.
8. Article 28(1)(a) (G8) and Article 8(3)(i) (G3) consume IP11 and IP10.
9. A refused result is a named refusal and not an error. What can refuse, and why: (i) `Art 7 the entity provides public benefit`, and so `Art 5(1)(b) ...`, `Art 5 the entity meets the charity test`, `Art 5(3) the entity meets the charity test only by virtue of an Order` and `Art 5 the limb that decides the charity test`, when the determination was made in breach of the duties on its maker (first reading of F2.10) and nothing else decides the case first; (ii) `Art 6(1) the purpose is a charitable purpose` and so the functions of Article 5 that call it, when the head recorded is (h), (i) or (l) and a fact that 6(2)(c), 6(2)(d) or 6(1)(l) needs is NOTHING and no clarification or other alternative decides first; (iii) `Art 5(1)(a) ...`, `Art 5 ...`, IP10 and the limb function, when `the purposes with their Article 6 facts` are not the entity's purposes; (iv) `Art 5 the limb that decides the charity test`, additionally, for an entity that is barred by 5(2) and whose (b) cannot be answered (the test is FALSE; which limb is first is not known); (v) `Art 6(1) the purpose is a charitable purpose` and so Article 5's functions, when the head recorded is (i) and `the facilities or activities have the object of improving the conditions of life ...` is NOTHING, unless 6(2)(d) is stated not to hold on both alternatives (then FALSE). A body that is not an entity does not refuse: `Art 5 the entity meets the charity test` and IP10 answer FALSE for it before any other refusal can arise, and the limb function names the limb `Article 5(1) does not apply: the body is not an entity within Article 2(1)`.
10. Repair (section 11). IP5: the entity's `kinds of entity` must be filled (empty means "not an entity", and the charity test then answers FALSE). N1: the object of 6(1)(i) is a field of the facts (`MAYBE BOOLEAN`, TYPICALLY NOTHING); a caller that omits it in JSON gets NOTHING, and a head (i) purpose then refuses unless 6(2)(d) decides it as FALSE. F2.13: pass `a member of the Commissioner's staff` as `who` only for a function exercised under Schedule 1 paragraph 4(3); otherwise pass `any person`. Nine exports gained `interp`.

## 10. Checks, numbers re-read, peeked

Test inventory (assertions and traces by module and section, counted from the deposit):

| test module | section | #ASSERT | #TRACE |
| --- | --- | --- | --- |
| `g2-tests-art3-4` | Article 4(1)(d): the duty to publish and maintain guidance | 0 | 3 |
| `g2-tests-art3-4` | Article 4(2): anything calculated to facilitate a function, other than acting as a governor | 4 | 3 |
| `g2-tests-art3-4` | Article 4(3): the three examples | 10 | 3 |
| `g2-tests-art3-4` | Article 4(4): the standard of conduct | 16 | 2 |
| `g2-tests-art6` | Article 6(1): one test per head | 18 | 0 |
| `g2-tests-art6` | Article 6(2)(a): the advancement of health includes the prevention or relief of sickness, disease or human suffering | 3 | 0 |
| `g2-tests-art6` | Article 6(2)(b): paragraph (1)(f) includes regeneration and the promotion of civic responsibility etc. | 6 | 0 |
| `g2-tests-art6` | Article 6(2)(c): sport means sport that involves physical skill and exertion | 7 | 0 |
| `g2-tests-art6` | Article 6(2)(d): paragraph (1)(i) applies only to facilities for people in need or open to the public at large | 5 | 0 |
| `g2-tests-art6` | Article 6(1)(i): the object of improving the conditions of life, and 6(2)(d), each on both sides | 13 | 0 |
| `g2-tests-art6` | Article 6(2)(e): paragraph (1)(n) includes relief given by the provision of accommodation or care | 3 | 0 |
| `g2-tests-art6` | Article 6(2)(f): the advancement of any philosophical belief is analogous to the purpose in paragraph (1)(c), for the purposes of paragraph (1)(p) | 12 | 0 |
| `g2-tests-art6` | Article 6(1)(l): equality and diversity | 10 | 0 |
| `g2-tests-art6` | Article 6(5): political purposes | 7 | 0 |
| `g2-tests-art6` | Article 6(3) and (4): the States' power and its limit | 12 | 3 |
| `g2-tests-art7` | Article 7(1): to whom paragraphs (2) and (3) apply | 23 | 0 |
| `g2-tests-art7` | Article 7(2): regard to the comparison, and to undue restriction where benefit goes to a section of the public only | 4 | 10 |
| `g2-tests-art7` | Article 7(3): what the person determining must not do | 14 | 10 |
| `g2-tests-art7` | Article 7 with Article 5(5): whether the determination complies with the duties on its maker | 11 | 0 |
| `g2-tests-art7` | Article 5(1)(b) with Article 7: does the entity provide public benefit? | 26 | 0 |
| `g2-tests-art7` | Article 7(4): guidance on public benefit | 4 | 0 |
| `g2-tests-art5` | Article 5(1): the charity test | 10 | 0 |
| `g2-tests-art5` | Article 6(5) and Article 5(1)(a)(ii): a political purpose is neither charitable nor ancillary | 6 | 0 |
| `g2-tests-art5` | Article 6(2) reached through the charity test | 4 | 0 |
| `g2-tests-art5` | FORK F2.1: "all of its purposes" with no purposes, and with ancillary purposes alone | 14 | 0 |
| `g2-tests-art5` | The facts must be the entity's purposes | 3 | 0 |
| `g2-tests-art5` | Article 5(1): a body that is not an entity does not meet the charity test | 18 | 0 |
| `g2-tests-art5` | Article 5(2): the bar on control by a Minister or a member of the States Assembly | 8 | 0 |
| `g2-tests-art5` | FORK F2.2: "acting in that capacity" | 5 | 0 |
| `g2-tests-art5` | FORK F2.3: "a Minister" in 5(2)(a) against the defined term "Minister" | 9 | 0 |
| `g2-tests-art5` | Article 5(3): the Minister's Order disapplying paragraph (2) | 10 | 2 |
| `g2-tests-art5` | A barred entity, and a determination that does not answer | 7 | 0 |
| `g2-tests-art5` | Article 5(4): the Commissioner's guidance on the charity test | 0 | 3 |
| `g2-tests-art5` | Article 5(5): regard to the guidance | 12 | 3 |
| `g2-tests-art5` | FORK F2.13: a member of the Commissioner's staff exercising the Commissioner's function | 7 | 3 |
| `g2-tests-art5` | Article 5(6): consultation and a report before issuing or amending guidance | 28 | 5 |
| `g2-tests-art5` | Article 5(7): providing the Minister with the guidance and the report | 13 | 6 |
| `g2-tests-art5` | Article 5(8): laying the guidance and the report before the States | 8 | 6 |
| `g2-tests-red` | Control | 1 | 0 |
| `g2-tests-red` | Each fork, answered as its other reading answers it | 14 | 0 |
| total | | 385 | 62 |

What `work/g2/check-g2.sh` printed on the final run:

```
module                                    errors satisfied  failed  refused  warnings  expected
g2-art3-4-commissioner.l4                      0         0       0        0         0         0
g2-art5-charity-test.l4                        0         0       0        0         0         0
g2-art6-purposes.l4                            0         0       0        0         0         0
g2-art7-public-benefit.l4                      0         0       0        0         0         0
g2-fixtures.l4                                 0         0       0        0         0         0
g2-nouns.l4                                    0         0       0        0         0         0
g2-readings.l4                                 0         0       0        0         0         0
g2-tests-art3-4.l4                             0        30       0        0         0         0
g2-tests-art5.l4                               0       162       0        0         0         0
g2-tests-art6.l4                               0        96       0        0         0         0
g2-tests-art7.l4                               0        82       0        0         0         0
g2-tests-red.l4                               15         0      15        0         0        15
TOTAL (12 modules)                            15       370      15        0         0
(a failed assertion is also an error; any other error, any refused assertion, any warning, and any failed count other than the expected one make the run red)

srcrefs check: 212 src: lines, 71 runs, 133 locators, 0 problems

module                                        traces in-module   sidecar     ok   bad  unguarded
g2-tests-art3-4.l4                                11        11         0     11     0          0
g2-tests-art5.l4                                  28        28         0     28     0          0
g2-tests-art6.l4                                   3         3         0      3     0          0
g2-tests-art7.l4                                  20        20         0     20     0          0
TOTAL                                             62        62         0     62     0          0
check-traces: all 62 guarded trace(s) behaved as expected

check-g2.sh: GREEN
```

Other checks. `l4 verify` over the four Article modules, re-run on the final sources (`work/g2/frag/verify-*.txt`): every rule it analyses is without findings in `g2-art3-4-commissioner` (12 rules), `g2-art6-purposes` (30) and `g2-art5-charity-test` (28). In `g2-art7-public-benefit` it analyses 14 rules, 11 without findings and 3 with one finding each (the DEONTIC rules are reported `NOT ANALYSED`, as before: the tool visualises only a BOOLEAN-valued DECIDE). (1) `[vacuous-guard]` in `Art 7 the entity provides public benefit`, as before the repair, in the true-paths: the negated first arm of the BRANCH is entailed there, because a determination that complies with 7(3)(b) and finds public benefit cannot be one for an entity that benefits only identified natural persons; the first arm is not vacuous for the other outcomes, since it turns the REFUSE of a breach into the FALSE that 7(3)(b) requires (tested). (2) `[unsat]` in `reading B of F2.13: only the persons the Articles name are bound`, and (3) `[dead-branch]` at the second arm of `Arts 7(1) and 5(5) the Commissioner's staff are bound as the Commissioner is`, which calls it. Both come from the same thing: the second reading of F2.13 is the constant FALSE ("not bound"), which as a BOOLEAN is unsatisfiable by construction, and the tool reads the arm that calls it through to that constant. They are new with this repair, they are not defects in the Law's encoding, and I kept the one-rule-per-reading shape of the other forks rather than inline the constant to silence them. `l4 batch` run on `Art 4(2) the Commissioner has power to do the thing` and on `Art 5 the entity meets the charity test` with a JSON row: the exports load, an omitted record field takes its TYPICALLY default, and the answers agree. Re-run for the repair (`work/g2/batch/rows-repair-r1.json`, `rows-repair-r2.json`, with `interp` given as one field only, since an `interp` of `{}` is refused by the service with "the value is not known", before and after the repair alike): a company with an educational purpose gives true and the same inputs with `kinds of entity` empty give false (R2); a recreational head with the object field left out of the JSON is presumed NOTHING by the soft presumption and gives the named refusal of 6(1)(i), with the object true it gives true and with it false it gives false (R1); the thirteenth field of `interp`, left out, took its default. One limit found: a constructor with fields of an enumeration cannot be given as JSON input, so `Head of charitable purpose`'s `a purpose added by Regulations under Article 6(3)` (a constructor of domain.l4) cannot be supplied through the service; the other sixteen heads are given by name, and a `MAYBE` head as the plain name or null.

Mutation test of the modules (`work/g2/mutate.py`): 42 mutants, each a one-token change to one rule (a negation removed, a connective swapped, a branch flipped, a boundary changed, a reading's arm exchanged, a guard answered the other way), each run against the four green test modules and the trace check. Thirty are the original set. Twelve (M31 to M42) were added for the repair after independent testing: the non-entity guard (M31 the guard rule always true; M32 the guard answers TRUE in the rule for IP10; M33 the limb function names `none` for a non-entity; M34 the guard answers TRUE in the rule for IP8), the object of 6(1)(i) (M35 an object stated false admits the purpose; M36 an object stated true admits it without 6(2)(d); M37 6(2)(d) stated false on both alternatives admits it; M38 head (i) skips the object and asks 6(2)(d) alone), and the staff fork F2.13 (M39 the staff arm of 7(1) answers FALSE; M40 reading A of F2.13 answers FALSE; M41 the staff arm of 5(5) answers FALSE; M42 reading B answers TRUE).

Result, on the final sources: 42 of 42 killed, in one run of all 42 (`work/g2/mutants/report-final42.txt`). Before that run I checked by script that each of the 42 patterns occurs exactly once in the final sources; four of the original thirty (M06, M11, M15, M28) had patterns that no longer matched and I had corrected them, and M40 and M42 were re-aimed at the two per-reading rules of F2.13 when I split that fork into one rule per reading. Earlier partial runs on earlier states of the repaired sources (`report-repair-old.txt`, `report-repair-fixed.txt`, `report-repair-new.txt`, `report-repair-f213.txt`) agreed with it where they applied.

History. The first run of the thirty on the sources as first delivered: 29 killed, 1 survived (`M27`, the lower bound of `Art 5(7) and 5(8) the act falls within the days counted from the event`), because the assertion meant to put an act before the event used a date a year after it; I corrected the date and added the 5(8) counterpart, and `M27` is killed. That run's report listed M06, M11 and M15 as killed; section 11.4 says what that run did and did not establish.

Numbers re-read. Articles 3 to 7 state no figure. Their only numerals are paragraph and Article numbers, and "sixteen" in the count of the heads (a) to (p), which agrees with domain.l4's sixteen constructors plus the Regulation-added head. Every number in the tests is therefore a fixture, and each was re-read: the dates 2026-01-01 + 30 days = 2026-01-31 (January has 31 days), 2026-03-01 + 14 = 2026-03-15, the edge days of each period on both sides (30 and 31 days after; 29 and 30 days with the day of the event counted; the days before, on and after the issue of the guidance in F2.7), and `DATE_SERIAL` stamps for the traces. The numbers of limbs: Article 4(4) has five limbs ((a); (a)(i); (a)(ii); (b) twice), Article 5(6)(a) has three consultees, Article 4(3) three examples, Article 5(2) three persons, Article 6(2) six clarifications, Article 6(1) sixteen heads; each has a test per member.

Offences and penalties. Articles 3 to 7 create no offence and state no penalty; there is nothing to encode or test under that heading.

Expected values changed after a run (two, both mistakes in my own tests and not findings about the Law). (1) In `g2-tests-art6`, head (l) recorded with neither idea stated was expected to give FALSE; that contradicted the design I had already decided from the Law's text (REFUSE where the source gives the clause nothing to decide on). The run reported a refusal, and the expectation became `#ASSERT REFUSED` with the message, for both readings. (2) In `g2-tests-art5`, the assertion that an act "before the event" is out of time for 5(7) used 31 December 2026 against an event on 1 January 2026, which is a year after it and not a day before; the mutation test found the gap (mutant M27 survived), and the date is now 31 December 2025, with a 5(8) counterpart. No other expected value was changed after a run, and no assertion was edited to match what the code computed on a question the Law answers. In the repair after independent testing no expected value was changed after a run: every new assertion was decided from the Law's text (and from the evidence assertions named in section 11) before the module was run, and the runs that failed failed on a missing argument (the nine signatures of section 11) or on a parse error in my own fixture (a list not in brackets, which swallowed the next field), not on an expectation.

## 11. Changes after independent testing

Three defects were found by independent test authors and checked against the Law's text by the fleet lead: R1 (Article 6(1)(i), `-- src:176`: recreational facilities qualify only "with the object of improving the conditions of life for the persons for whom the facilities or activities are primarily intended"; evidence: assertion E6-2d4), R2 (Article 5(1), `-- src:145`: "An entity meets the charity test if"; a body that is not an entity cannot meet it; evidence: V-20), and R3 (Schedule 1 paragraph 4(3), `-- src:796`: staff exercising the Commissioner's function; evidence: the last assertions of the C test author's disagreements file, and A-14). The repairs are in the modules; the rest of this section is for the integrator, who must rewire.

### 11.1 Signatures that changed (rule, old `GIVEN` list, new `GIVEN` list)

Every change of a `GIVEN` list is the addition of `interp : Interpretation of Articles 3 to 7` as the LAST input; no existing input was renamed, retyped or reordered. The list was produced by comparing the `@export` rules of the sources before and after (`work/g2/exports.py`): nine exports changed, and the other 31 keep their names and their `GIVEN` lists. Two rules that are not exported but are callable changed in the same way.

| rule | old GIVEN list | new GIVEN list |
| --- | --- | --- |
| `Art 7(1) Articles 7(2) and 7(3) apply to the person` (export) | `who` | `who`, `interp` |
| `Art 7(2)(a) the person determining must have regard to the comparison of benefit and disbenefit` (export) | `who` | `who`, `interp` |
| `Art 7(2)(b) the person determining must have regard to whether a condition on obtaining the benefit is unduly restrictive` (export) | `who`, `benefit is, or is likely to be, provided to a section of the public only` | the same two, then `interp` |
| `Art 7(3) the determination is permitted` (export) | `determination` | `determination`, `interp` |
| `Art 7(3)(a) the person determining must not presume a charitable purpose to be for the public benefit` (export) | `who` | `who`, `interp` |
| `Art 7(3)(b) the person determining must not treat identified natural persons as a section of the public` (export) | `who` | `who`, `interp` |
| `Art 7(3)(b) the person determining must not treat an entity that benefits only identified natural persons as providing public benefit` (export) | `who` | `who`, `interp` |
| `Art 7 the determination complies with the duties on its maker` (export) | `determination` | `determination`, `interp` |
| `Art 5(5) the duty to have regard to the guidance` (export) | `who`, `the person is determining whether an entity meets the charity test`, `the person is performing another function under this Law to which the guidance is relevant`, `the person is a governor of a registered charity` | the same four, then `interp` |
| `Art 5(5) the person must have regard to the guidance` (not exported) | the same four | the same four, then `interp` |
| `the person is one of those whom Article 5(5) binds in other functions` (not exported) | `who`, `the person is a governor of a registered charity` | the same two, then `interp` |

Each new `interp` carries an `@desc` ("The readings of the ambiguous provisions of Articles 3 to 7; the field read here is whether the Commissioner's staff exercising the Commissioner's function are bound"). The favoured interpretation, `the favoured interpretation of Articles 3 to 7`, is the value to pass.

Why `interp` and not a Boolean: F2.13 is a fork, so it is a field of the one record of forks (the R4 shape), and the rules that read it take that record as every other rule that depends on a fork does.

Changes of type, with no change of any `GIVEN` list:

| type | before | after |
| --- | --- | --- |
| record `Facts about a purpose under Article 6` | 9 fields | 10: the last is `the facilities or activities have the object of improving the conditions of life for the persons for whom they are primarily intended` : `MAYBE BOOLEAN`, `TYPICALLY NOTHING` (R1). A positional `OF` takes 10 values; in JSON the field may be left out and is then NOTHING. It is part of the input `facts` of `Art 6(1) the purpose is a charitable purpose` and of `the purposes with their Article 6 facts` of the four exports of Article 5. |
| record `Interpretation of Articles 3 to 7` | 12 fields | 13: the last is `whether the Commissioner's staff exercising the Commissioner's function are bound`, `TYPICALLY` the first reading (R3). A positional `OF` takes 13 values (all 16 values of `g2-readings` were extended); in JSON the field may be left out and takes its default. |
| enumeration `Limb of the charity test that decides it` | 5 constructors | 6: the new one is `Article 5(1) does not apply: the body is not an entity within Article 2(1)` (R2). Any `CONSIDER` over this type elsewhere must be extended; the output of `Art 5 the limb that decides the charity test` can now be it. |

New, and so not a change: the enumeration `Whether a member of the Commissioner's staff exercising the Commissioner's function is bound as the Commissioner is` (constructors `a member of staff exercising a function of the Commissioner under Schedule 1 paragraph 4(3) is bound as the Commissioner is` and `only the persons that Article 7(1) and Article 5(5) name are bound`); the rules `Art 5(1) the body is an entity within Article 2(1)` (`the entity`), `Art 6(1)(i) paragraph (1)(i) is met` (`facts`), `Art 6(2)(d) both alternatives are stated as false` (`facts`), `Arts 7(1) and 5(5) the Commissioner's staff are bound as the Commissioner is` (`interp`), `reading A of F2.13: ...` and `reading B of F2.13: ...` (no inputs); the named refusal `Article 6(1)(i) was not given whether the facilities or activities have the object of improving the conditions of life`; the values `F2.13 A`, `F2.13 B` and `the interpretation of Articles 3 to 7 with F2.13 read as B` of `g2-readings`; the fixture `a G2 non-entity standing as ... holding these G2 purposes`.

### 11.2 Behaviour that changed with the same `GIVEN` list

- R1. `Art 6(1) the purpose is a charitable purpose` (and so every Article 5 export that calls it): a purpose recorded under head (i) now needs the object AND the conditions of 6(2)(d). Object stated false: not charitable, whatever 6(2)(d) says. Object stated true: 6(2)(d) decides, as before. Object not stated: FALSE if 6(2)(d) is stated not to hold on both alternatives, and otherwise the named refusal above. Before the repair a head (i) purpose with 6(2)(d) stated true was charitable; a caller that does not fill the new field now gets a refusal for that purpose, which is the intended signal. No other head is affected; `Art 6(2)(d) paragraph (1)(i) applies` itself is unchanged.
- R2. `Art 5 the entity meets the charity test` and `Art 5(3) the entity meets the charity test only by virtue of an Order` answer FALSE, and `Art 5 the limb that decides the charity test` answers `Article 5(1) does not apply: the body is not an entity within Article 2(1)`, when the `kinds of entity` of `the entity` is empty. The guard comes before everything else in these three rules, so it is FALSE (not a refusal) even when the list of purposes with their facts is not the entity's purposes and even when the determination was made in breach. Read and left unguarded, with the reason: `Art 5(1)(a) all of the entity's purposes ...` and `Art 5(1)(b) the entity provides public benefit ...` answer a question about the purposes or about a finding and claim nothing about the test; `Art 7 the entity provides public benefit` answers what a determination found; `Art 6 the entity has a purpose within the advancement of religion` (IP11) characterises purposes, and its consumer, Article 28, applies to a registered charity, which is an entity; `Art 5(2) the bar applies to the entity` does not start from the entity record (it takes the constitution facts). If the integrator wants these four to answer FALSE for a non-entity as well, the guard `Art 5(1) the body is an entity within Article 2(1)` is the rule to call.
- R3. Default of F2.13: `Art 7(1) Articles 7(2) and 7(3) apply to the person` is TRUE for the constructor `a member of the Commissioner's staff` (it was FALSE), and so 7(2) and 7(3) bind a staff determination; `Art 5(5) the person must have regard to the guidance` is TRUE for it when it performs another function to which the guidance is relevant (it was FALSE). `Art 7 the entity provides public benefit` is therefore FALSE for a staff finding that an entity benefiting only identified natural persons provides public benefit. The old behaviour is reading B (`the interpretation of Articles 3 to 7 with F2.13 read as B`), with a test for each reading in `g2-tests-art5` and `g2-tests-art7` and one red assertion in `g2-tests-red`.

### 11.3 For the integrator

- IP5: fill `kinds of entity` of `the entity` (G1 derives it from Article 2). Empty now means "not an entity" to this group, and the charity test answers FALSE.
- N1: supply the new field of `Facts about a purpose under Article 6` for every purpose recorded under head (i); it is a determination (the object of improving the conditions of life), like the other facts.
- F2.13: pass `a member of the Commissioner's staff` as `who` only for a function exercised under Schedule 1 paragraph 4(3); otherwise pass `any person`. G9 owns paragraph 4(3); its exceptions (the decisions of Articles 11, 15(3) and 16) are not modelled in Articles 3 to 7. The reading should be set from the same view of paragraph 4(3) in any other group that attaches a duty to the Commissioner (for example Article 27(1)(b), the Commissioner's belief that a registered charity does not pass the charity test).
- Nine exports gained `interp` as a last input (table above).

### 11.4 What I did not do, and what I found about my own earlier numbers

- I did not model which functions were in fact authorized under paragraph 4(3), or the three excepted decisions; the choice of the constructor is the caller's fact.
- I did not guard the four rules named in 11.2 against a non-entity; that is a judgement, stated there.
- My earlier statement that all 30 mutants were killed does not stand as it was made. Before the repair I counted, by script, how often each mutant's pattern occurs in the sources as delivered: the patterns of three mutants (M06, M11, M15) occurred 0 times, so those three could not have been applied to the delivered sources, although the report of the first run lists them as killed. The likely cause is that helper rules were renamed (to carry an Article number) after that run, but I did not establish that. Their kill status is established only by the re-run reported in section 10, on the repaired sources, with corrected patterns.

Peeked: nothing. I read only the files named in the assignment and the brief, the l4 documentation under `doc/reference` and `doc/concepts/legal-modeling`, and `phase1/slice-G2.md`. My context carried an index of someone's notes that mentions this subject; I did not follow it.
