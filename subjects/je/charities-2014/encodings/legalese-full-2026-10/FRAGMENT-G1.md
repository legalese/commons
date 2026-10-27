# FRAGMENT-G1: Articles 1 and 2 of the Charities (Jersey) Law 2014 (interpretation; definition of entity and related terms)

Written by ENCODER G1 on 2026-10-26.
Everything stated in the present tense below was checked on that day against the files named, with the fleet binary `l4` (sha256 `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`), by `work/g1/check.sh`.
The last run printed what section 0 shows.
Nothing here has been read by a domain expert (the review the pipeline calls HG1 has not happened).

## 0. What exists, and what check.sh printed

Files in DEPOSIT (all start with `g1-`, none starts with `@lang en`):

| file | holds |
| --- | --- |
| `g1-interpretation.l4` | the eight fork enumerations and the one record `Interpretation of Articles 1 and 2`, and the other reading of each fork as a value. Added to the PLAN's module list: the three rule modules share the record, and groups may import only their own modules, so the record needs a module of its own below them |
| `g1-art1-defined-terms.l4` | the title, the long title and Article 1: four computed definitions, three roles, the stubs for the rest |
| `g1-art2-entity.l4` | Article 2(1) to (6): the facts about a body, the kinds of entity, the power in 2(2), Jersey entity, constitution, constitutional Law, purpose |
| `g1-art2-governor-misconduct.l4` | Article 2(7) to (10): governor, relevant unincorporated entity, the two clarifications of (9), misconduct |
| `g1-tests-art1.l4`, `g1-tests-art2-entity.l4`, `g1-tests-art2-governor-misconduct.l4` | the tests; every expected value was decided from the source before the module was run |
| `FRAGMENT-G1.md` | this file |

There is no `g1-tests-red.l4`: nothing in Articles 1 and 2 is expected to fail, so the expected-failed count of group G1 is 0 in every module.
The only assertion that failed during the work was the first run of `Art 2(3) the body is a Jersey entity` for the day before the first consolidated text, which answered TRUE where the source says the text is unknown; the expected value (a refusal) was kept and the code was changed (laziness had let `any` answer before the refusal was reached; `Art 2(1) a text of the Law is among the sources for` now forces it first).

`work/g1/check.sh` (adapted from the skill's `assets/check.sh` and the template; it runs only `DEPOSIT/g1-*.l4`) printed:

```
l4 binary: FLEET_DIR/bin/l4 (sha256 matches the fleet's binary)

module                                    errors satisfied  failed  refused  warnings  expected
g1-art1-defined-terms.l4                       0         0       0        0         0         0
g1-art2-entity.l4                              0         0       0        0         0         0
g1-art2-governor-misconduct.l4                 0         0       0        0         0         0
g1-interpretation.l4                           0         0       0        0         0         0
g1-tests-art1.l4                               0        74       0        0         0         0
g1-tests-art2-entity.l4                        0       185       0        0         0         0
g1-tests-art2-governor-misconduct.l4           0       147       0        0         0         0
TOTAL (7 modules)                              0       406       0        0         0
(a failed assertion is also an error; a refused assertion is also a warning; any other error, any refusal, any warning and any failed count other than expected make the run red)

shape: every g1- module has a plain name, starts without @lang en, and imports only prelude, daydate, domain and g1- modules
srcrefs check: 134 src: lines, 81 runs, 144 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g1-tests-art2-entity.l4                            3         3         0      3     0          0
TOTAL                                              3         3         0      3     0          0
check-traces: all 3 guarded trace(s) behaved as expected
@ref notices (follows code on its line / end of the file): 0

check.sh (G1): GREEN
(a green run is the group's own: it says nothing about whether a domain expert agrees with any reading in FRAGMENT-G1.md)
```

`srcrefs.py check --refs` over every module (RAW is the Law's text file) is the `srcrefs check:` line above.

Mutation check (not part of check.sh; `work/g1/mutants.py`): 36 single-edit mutants of the three rule modules (a vintage mapped to the wrong office or Law, a limb dropped, a guard removed, a reading swapped) were each run against the three test modules on the final code; all 36 were caught by at least one assertion, none survived.
An earlier run during the work found one survivor, a conjunct in `Art 2(7)(e)` that could never matter (the relation to the control is a single constructor, so "has it" and "only exercises it for another" exclude each other); it was removed from the code and Article 2(9)(a) became a named rule that the tests assert.

Number re-read (a separate pass, after the tests were green): every digit-bearing token of the three test modules was listed and ticked against the source.
The nine dates of the texts agree with the Table of Legislation History (src:880, 885, 888, 892, 898, 902, 906, 909, 912); the five instrument citations of the "Minister" step table agree with the instrument files (R&O.40/2019 and R&O.29/2021 Schedule 2 paragraph 1(e), R&O.28/2023 Schedule 2 paragraph 1(4), R&O.10/2024 Schedule 4 paragraph (1), R&O.102/2026 Article 1); "7 days after it is made" agrees for R&O.56/2025 (9 to 16 October 2025), R&O.28/2023 (5 to 12 April 2023) and R&O.102/2026 (25 September to 2 October 2026); "9.30 a.m. on 27 February 2024" and "1 January 2020" agree with R&O.10/2024 Article 5 and the Table; the years of the other enactments in the expected strings agree with the lines of Articles 1 and 2 they come from.
Numbers that are not source numbers, by design: `YMD 2024 3 1` (the date served of a fixture notice, which no assertion reads), the clock values `AT 0` and `AT 7` of the three traces, and the invented names "Charity Example (Jersey) Law 1999", "Example Associations (Jersey) Law 1990" and "Example Act 1900" in the constitutional-Law tests.

## 1. Coverage

One row per provision of the group's scope, in the Law's numbering, with the ids of `phase1/coverage.tsv` (113 rows: 76 encoded, 25 inert, 12 out-of-scope, 0 deferred).
No disposition was changed from the PLAN.
Where the module column names a module for an out-of-scope row, the module holds a labelled stub that quotes the line and says what input it is; the other enactment itself is out of scope.

| id | provision | disposition | module | rules | note |
| --- | --- | --- | --- | --- | --- |
| Title | Title | inert | g1-art1-defined-terms | `Title of the Law` |  |
| Long title | Long title | inert | g1-art1-defined-terms | `Long title of the Law` |  |
| 1 | Article 1 | encoded | g1-art1-defined-terms | `Art 1 lead-in`; `Art 1 no text of the Law before 1 January 2019 is among the sources` | the lead-in 'unless the context otherwise requires': no place found where the context displaces a definition of Articles 1 and 2; Article 5(2)(a) 'a Minister' is the one place found in the Law (another group's) |
| 1[annual return] | Article 1 definition “annual return” | inert | g1-art1-defined-terms | `Art 1 annual return` |  |
| 1[charitable purpose] | Article 1 definition “charitable purpose” | inert | g1-art1-defined-terms | `Art 1 charitable purpose` |  |
| 1[Commissioner] | Article 1 definition “Commissioner” | inert | g1-art1-defined-terms | `Art 1 Commissioner` |  |
| 1[company] | Article 1 definition “company” | out-of-scope | g1-art1-defined-terms | `Art 1 company` |  |
| 1[Comptroller] | Article 1 definition “Comptroller” | encoded | g1-art1-defined-terms | `Art 1 Comptroller`; `Art 1 the Law that defines the Comptroller under the text of` | Income Tax (Jersey) Law 1961 to 31 December 2019, Revenue Administration (Jersey) Law 2019 from 1 January 2020: shown by L.13/2019 Sch 3 para 1 and R&O.136/2019 Art 1 (the survey said R&O.136/2019 was not among the inputs) |
| 1[constitution] | Article 1 definition “constitution” | inert | g1-art1-defined-terms | `Art 1 constitution` |  |
| 1[constitutional Law] | Article 1 definition “constitutional Law” | inert | g1-art1-defined-terms | `Art 1 constitutional Law` |  |
| 1[court] | Article 1 definition “court” | inert | g1-art1-defined-terms | `Art 1 court` |  |
| 1[court-approved fidéicommis] | Article 1 definition “court-approved fidéicommis” | out-of-scope | g1-art1-defined-terms | `Art 1 court-approved fidéicommis` |  |
| 1[donation] | Article 1 definition “donation” | inert | g1-art1-defined-terms | `Art 1 donation` |  |
| 1[entity] | Article 1 definition “entity” | inert | g1-art1-defined-terms | `Art 1 entity` |  |
| 1[foundation] | Article 1 definition “foundation” | out-of-scope | g1-art1-defined-terms | `Art 1 foundation` |  |
| 1[general section] | Article 1 definition “general section” | inert | g1-art1-defined-terms | `Art 1 general section` |  |
| 1[governor] | Article 1 definition “governor” | inert | g1-art1-defined-terms | `Art 1 governor` |  |
| 1[incorporated 1862 association] | Article 1 definition “incorporated 1862 association” | out-of-scope | g1-art1-defined-terms | `Art 1 incorporated 1862 association` |  |
| 1[JFSC] | Article 1 definition “JFSC” | out-of-scope | g1-art1-defined-terms | `Art 1 JFSC` | out of scope (the enactment); carried as the role `the Jersey Financial Services Commission` |
| 1[Jersey entity] | Article 1 definition “Jersey entity” | inert | g1-art1-defined-terms | `Art 1 Jersey entity` |  |
| 1[Loi of 1862] | Article 1 definition “Loi of 1862” | out-of-scope | g1-art1-defined-terms | `Art 1 Loi of 1862` |  |
| 1[Minister] | Article 1 definition “Minister” | encoded | g1-art1-defined-terms | `Art 1 the Minister under the text of`; `Art 1 no text of the Law before 1 January 2019 is among the sources` | ten vintages, five offices; the 2 March 2021 text is SHOWN by R&O.29/2021 Sch 2 para 1(e) (the survey said inferred); 1 January 2019 is derived from the words R&O.40/2019 replaced |
| 1[misconduct] | Article 1 definition “misconduct” | inert | g1-art1-defined-terms | `Art 1 misconduct` |  |
| 1[prescribed] | Article 1 definition “prescribed” | inert | g1-art1-defined-terms | `Art 1 prescribed and specified` |  |
| 1[property] | Article 1 definition “property” | out-of-scope | g1-art1-defined-terms | `Art 1 property` |  |
| 1[publish] | Article 1 definition “publish” | encoded | g1-art1-defined-terms | `Art 1 the information has been published`; `Art 1 published on the opinion of the person publishing`; `Art 1 published on the likelihood of the manner` | fork F1.5 |
| 1[purpose] | Article 1 definition “purpose” | inert | g1-art1-defined-terms | `Art 1 purpose` |  |
| 1[register] | Article 1 definition “register” | inert | g1-art1-defined-terms | `Art 1 register` |  |
| 1[registered charitable purposes] | Article 1 definition “registered charitable purposes” | inert | g1-art1-defined-terms | `Art 1 registered charitable purposes` |  |
| 1[registered charity] | Article 1 definition “registered charity” | encoded | g1-art1-defined-terms | `Art 1 the entity is a registered charity`; `Art 1 the standing is that of a registered charity` | the historic section is NOT included; a body that is not an entity (no kinds) is not one |
| 1[registered public benefit statement] | Article 1 definition “registered public benefit statement” | inert | g1-art1-defined-terms | `Art 1 registered public benefit statement` |  |
| 1[regulated financial services business] | Article 1 definition “regulated financial services business” | inert | g1-art1-defined-terms | `Art 1 regulated financial services business` |  |
| 1[regulated financial services business](a) | Article 1 definition “regulated financial services business”(a) | out-of-scope | g1-art1-defined-terms | `Art 1 regulated financial services business` |  |
| 1[regulated financial services business](b) | Article 1 definition “regulated financial services business”(b) | out-of-scope | g1-art1-defined-terms | `Art 1 regulated financial services business` |  |
| 1[regulated financial services business](c) | Article 1 definition “regulated financial services business”(c) | out-of-scope | g1-art1-defined-terms | `Art 1 regulated financial services business` |  |
| 1[regulated financial services business](d) | Article 1 definition “regulated financial services business”(d) | out-of-scope | g1-art1-defined-terms | `Art 1 regulated financial services business` |  |
| 1[reportable matter] | Article 1 definition “reportable matter” | inert | g1-art1-defined-terms | `Art 1 reportable matter` |  |
| 1[required steps notice] | Article 1 definition “required steps notice” | inert | g1-art1-defined-terms | `Art 1 required steps notice` |  |
| 1[restricted section] | Article 1 definition “restricted section” | inert | g1-art1-defined-terms | `Art 1 restricted section` |  |
| 1[solicit] | Article 1 definition “solicit” | inert | g1-art1-defined-terms | `Art 1 solicit` |  |
| 1[tribunal] | Article 1 definition “tribunal” | inert | g1-art1-defined-terms | `Art 1 tribunal` |  |
| 1[trust] | Article 1 definition “trust” | out-of-scope | g1-art1-defined-terms | `Art 1 trust` |  |
| 2 | Article 2 | encoded | g1-art2-entity | `Art 2(1) a text of the Law is among the sources for`; `Art 2 the body as an entity` |  |
| 2(1) | Article 2(1) | encoded | g1-art2-entity | `Art 2(1) the kinds of entity the body falls within`; `Art 2(1) the body is an entity` | the sub-paragraphs the body falls within, a LIST in the Law's order; REFUSES for a day before the first consolidated text |
| 2(1)(a) | Article 2(1)(a) | encoded | g1-art2-entity | `Art 2(1)(a) the body is the trustees of a trust` |  |
| 2(1)(b) | Article 2(1)(b) | encoded | g1-art2-entity | `Art 2(1)(b) the body is the fidéicommissaires of a court-approved fidéicommis` |  |
| 2(1)(ba) | Article 2(1)(ba) | encoded | g1-art2-entity | `Art 2(1)(ba) the body is a body corporate that is an NPO established under the law of Jersey`; `Art 2(1)(ba) is part of the text of` | in the texts of 16 October 2025 and 2 October 2026 only; R&O.56/2025 |
| 2(1)(ba)(i) | Article 2(1)(ba)(i) | encoded | g1-art2-entity | `Art 2(1)(ba) the body is a body corporate that is an NPO established under the law of Jersey` |  |
| 2(1)(ba)(ii) | Article 2(1)(ba)(ii) | encoded | g1-art2-entity | `Art 2(1)(ba) the body is a body corporate that is an NPO established under the law of Jersey` |  |
| 2(1)(ba)(iii) | Article 2(1)(ba)(iii) | encoded | g1-art2-entity | `Art 2(1)(ba)(iii) the body falls within one of sub-paragraphs (c) to (h)` |  |
| 2(1)(c) | Article 2(1)(c) | encoded | g1-art2-entity | `Art 2(1)(c) the body is an incorporated 1862 association` |  |
| 2(1)(d) | Article 2(1)(d) | encoded | g1-art2-entity | `Art 2(1)(d) the body is a foundation` |  |
| 2(1)(e) | Article 2(1)(e) | encoded | g1-art2-entity | `Art 2(1)(e) the body is a body corporate established by an enactment, an Act of the States or a Royal Charter`; `Art 2(1)(e) reading A: in relation to Jersey qualifies the Royal Charter only`; `Art 2(1)(e) reading B: in relation to Jersey qualifies each of (i), (ii) and (iii)` | fork F1.6 |
| 2(1)(e)(i) | Article 2(1)(e)(i) | encoded | g1-art2-entity | `Art 2(1)(e)(i) the body corporate is established by an enactment` |  |
| 2(1)(e)(ii) | Article 2(1)(e)(ii) | encoded | g1-art2-entity | `Art 2(1)(e)(ii) the body corporate is established by Act of the States` |  |
| 2(1)(e)(iii) | Article 2(1)(e)(iii) | encoded | g1-art2-entity | `Art 2(1)(e)(iii) the body corporate is established by Royal Charter` |  |
| 2(1)(f) | Article 2(1)(f) | encoded | g1-art2-entity | `Art 2(1)(f) the body is a company` |  |
| 2(1)(g) | Article 2(1)(g) | encoded | g1-art2-entity | `Art 2(1)(g) the body is incorporated under, but not by, an enactment other than the Companies Law` | fork F1.8 |
| 2(1)(h) | Article 2(1)(h) | encoded | g1-art2-entity | `Art 2(1)(h) the body is incorporated under, but not by, an Act of the United Kingdom Parliament or Order in Council` |  |
| 2(1)(i) | Article 2(1)(i) | encoded | g1-art2-entity | `Art 2(1)(i) the body is an unincorporated body or association of persons` |  |
| 2(1)(j) | Article 2(1)(j) | encoded | g1-art2-entity | `Art 2(1)(j) the body is substantially similar to an entity mentioned in (a) to (h) but established under the law of another jurisdiction`; `Art 2(1) the sub-paragraphs (a) to (h)` | fork F1.1 (the range 'sub-paragraphs (a) to (h)') |
| 2(2) | Article 2(2) | encoded | g1-art2-entity | `Art 2(2) the Minister may add a sub-paragraph to Article 2(1)` | MAY, no WITHIN (no period is stated); the content of an Order is an input |
| 2(3) | Article 2(3) | encoded | g1-art2-entity | `Art 2(3) the body is a Jersey entity` |  |
| 2(3)(a) | Article 2(3)(a) | encoded | g1-art2-entity | `Art 2(3)(a) the body falls within any of sub-paragraphs (a) to (h) of Article 2(1)` | fork F1.1 |
| 2(3)(b) | Article 2(3)(b) | encoded | g1-art2-entity | `Art 2(3)(b) the body is an unincorporated body within Article 2(1)(i) governed by the law of Jersey with a qualifying governor` |  |
| 2(3)(b)(i) | Article 2(3)(b)(i) | encoded | g1-art2-entity | `Art 2(3)(b)(i) the law governing the relationship between the persons constituting the body is the law of Jersey` |  |
| 2(3)(b)(ii) | Article 2(3)(b)(ii) | encoded | g1-art2-entity | `Art 2(3)(b)(ii) at least one governor is a natural person resident in Jersey or a Jersey entity by virtue of sub-paragraph (a)` |  |
| 2(4) | Article 2(4) | encoded | g1-art2-entity | `Art 2(4) the constitution of the entity consists of`; `Art 2(4) the constitution of the entity in all its kinds consists of` | fork F1.4 for a body in more than one kind |
| 2(4)(a) | Article 2(4)(a) | encoded | g1-art2-entity | `Art 2(4)(a) the constitution of a trust` |  |
| 2(4)(b) | Article 2(4)(b) | encoded | g1-art2-entity | `Art 2(4)(b) the constitution of a court-approved fidéicommis` |  |
| 2(4)(c) | Article 2(4)(c) | encoded | g1-art2-entity | `Art 2(4)(c) the constitution of an incorporated 1862 association` |  |
| 2(4)(d) | Article 2(4)(d) | encoded | g1-art2-entity | `Art 2(4)(d) the constitution of a foundation` |  |
| 2(4)(e) | Article 2(4)(e) | encoded | g1-art2-entity | `Art 2(4)(e) the constitution of a company` |  |
| 2(4)(f) | Article 2(4)(f) | encoded | g1-art2-entity | `Art 2(4)(f) the constitution of a body corporate falling within paragraph (1)(e)` |  |
| 2(4)(g) | Article 2(4)(g) | encoded | g1-art2-entity | `Art 2(4)(g) the constitution in any other case` |  |
| 2(5) | Article 2(5) | encoded | g1-art2-entity | `Art 2(5) the constitutional Laws of the entity are`; `Art 2(5) the constitutional Law of the entity is` | fork F1.3 ((g) and (h)) and fork F1.4; an empty list where the definition names no Law (trap T6) |
| 2(5)(a) | Article 2(5)(a) | encoded | g1-art2-entity | `Art 2(5)(a) the constitutional Law of a trust` |  |
| 2(5)(b) | Article 2(5)(b) | encoded | g1-art2-entity | `Art 2(5)(b) the constitutional Law of a court-approved fidéicommis or an incorporated 1862 association` |  |
| 2(5)(c) | Article 2(5)(c) | encoded | g1-art2-entity | `Art 2(5)(c) the constitutional Law of a foundation` |  |
| 2(5)(d) | Article 2(5)(d) | encoded | g1-art2-entity | `Art 2(5)(d) the constitutional Law of a company` |  |
| 2(5)(e) | Article 2(5)(e) | encoded | g1-art2-entity | `Art 2(5)(e) the constitutional Law of a body incorporated by (but not under) any other Law`; `Art 2(5) reading B of F1.3: the constitutional Law of a body incorporated under, but not by, an enactment` | reaches only a body established by a Law; the Law's name is an input |
| 2(6) | Article 2(6) | encoded | g1-art2-entity | `Art 2(6) the purpose of the entity means`; `Art 2(6) the purposes of the entity in all its kinds mean` | fork F1.4 |
| 2(6)(a) | Article 2(6)(a) | encoded | g1-art2-entity | `Art 2(6)(a) the purpose of a trust` |  |
| 2(6)(b) | Article 2(6)(b) | encoded | g1-art2-entity | `Art 2(6)(b) the purpose of a court-approved fidéicommis or an incorporated 1862 association` |  |
| 2(6)(c) | Article 2(6)(c) | encoded | g1-art2-entity | `Art 2(6)(c) the purpose of a foundation` |  |
| 2(6)(d) | Article 2(6)(d) | encoded | g1-art2-entity | `Art 2(6)(d) the purpose of any other entity` |  |
| 2(7) | Article 2(7) | encoded | g1-art2-governor-misconduct | `Art 2(7) the person is a governor of the entity`; `Art 2(7) the cases (a) to (d) for the entity and the person`; `Art 2(7) the governors among the people` | fork F1.4 (changed from the survey's reading) and, through 2(8)(b)(i), F1.5 |
| 2(7)(a) | Article 2(7)(a) | encoded | g1-art2-governor-misconduct | `Art 2(7)(a) in the case of a trust or fidéicommis, a trustee or fidéicommissaire of the trust or fidéicommis` |  |
| 2(7)(b) | Article 2(7)(b) | encoded | g1-art2-governor-misconduct | `Art 2(7)(b) in the case of a foundation, a member of the council of the foundation` |  |
| 2(7)(c) | Article 2(7)(c) | encoded | g1-art2-governor-misconduct | `Art 2(7)(c) in the case of a company, a director of the company` |  |
| 2(7)(d) | Article 2(7)(d) | encoded | g1-art2-governor-misconduct | `Art 2(7)(d) in the case of a relevant unincorporated entity, a member of its management committee` |  |
| 2(7)(e) | Article 2(7)(e) | encoded | g1-art2-governor-misconduct | `Art 2(7)(e) the person has the general control and management of the administration of the entity under its constitution` | 'in any other case' is read as the residue: it applies when none of (a) to (d) applies |
| 2(8) | Article 2(8) | encoded | g1-art2-governor-misconduct | `Art 2(8) the entity is a relevant unincorporated entity` |  |
| 2(8)(a) | Article 2(8)(a) | encoded | g1-art2-governor-misconduct | `Art 2(8)(a) the entity falls within Article 2(1)(i)` |  |
| 2(8)(b) | Article 2(8)(b) | encoded | g1-art2-governor-misconduct | `Art 2(8)(b) the constitution conforms to a model published by the Commissioner that provides for a management committee` |  |
| 2(8)(b)(i) | Article 2(8)(b)(i) | encoded | g1-art2-governor-misconduct | `Art 2(8)(b)(i) the model is published for the purpose by the Commissioner` |  |
| 2(8)(b)(ii) | Article 2(8)(b)(ii) | encoded | g1-art2-governor-misconduct | `Art 2(8)(b)(ii) the model provides for the entity to have a management committee` |  |
| 2(9) | Article 2(9) | encoded | g1-art2-governor-misconduct | `Art 2(9)(a) the person only exercises the general control and management on behalf of another who has it in own right`; `Art 2(9)(b) the person has the general control and management alone or as one of a number of governors` | both clarifications are named rules over the shared noun `Relation to the general control and management`; (9)(a) is declaratory and is asserted, not added to (7)(e) |
| 2(9)(a) | Article 2(9)(a) | encoded | g1-art2-governor-misconduct | `Art 2(9)(a) the person only exercises the general control and management on behalf of another who has it in own right` |  |
| 2(9)(b) | Article 2(9)(b) | encoded | g1-art2-governor-misconduct | `Art 2(9)(b) the person has the general control and management alone or as one of a number of governors` |  |
| 2(10) | Article 2(10) | encoded | g1-art2-governor-misconduct | `Art 2(10) the conduct is misconduct` | forks F1.2 and F1.7; inputs IP13, IP19, IP26 under their standard names |
| 2(10)(a) | Article 2(10)(a) | encoded | g1-art2-governor-misconduct | `Art 2(10)(a) a contravention by a registered charity or by any of its governors`; `Art 2(10) the entity is a registered charity at the time the standing is read` |  |
| 2(10)(a)(i) | Article 2(10)(a)(i) | encoded | g1-art2-governor-misconduct | `Art 2(10)(a)(i) a provision of this Law or of an enactment under it has been contravened` |  |
| 2(10)(a)(ii) | Article 2(10)(a)(ii) | encoded | g1-art2-governor-misconduct | `Art 2(10)(a)(ii) a provision of the constitution or of the constitutional Law of the charity has been contravened` |  |
| 2(10)(a)(iii) | Article 2(10)(a)(iii) | encoded | g1-art2-governor-misconduct | `Art 2(10)(a)(iii) a provision of a required steps notice has been contravened` | needs a notice served (IP19) |
| 2(10)(a)(iv) | Article 2(10)(a)(iv) | encoded | g1-art2-governor-misconduct | `Art 2(10)(a)(iv) a provision of an order of the court has been contravened` |  |
| 2(10)(b) | Article 2(10)(b) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b) the commission of an offence in relation to a charity`; `Art 2(10)(b) the offence is in relation to a registered charity, an excepted foreign charity or an equivalent foreign entity`; `Art 2(10)(b) the offence is under one of the Laws or of the kinds listed in (ii) to (vi)` | fork F1.2 |
| 2(10)(b)(i) | Article 2(10)(b)(i) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(i) an offence under the constitutional Law of that charity or other entity` | no offence under a constitutional Law the definition does not name |
| 2(10)(b)(ii) | Article 2(10)(b)(ii) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(ii) an offence under the financial services Laws` |  |
| 2(10)(b)(iii) | Article 2(10)(b)(iii) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(iii) an offence under the tax Laws` |  |
| 2(10)(b)(iv) | Article 2(10)(b)(iv) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(iv) an offence relating to money laundering or terrorist financing` |  |
| 2(10)(b)(v) | Article 2(10)(b)(v) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(v) an offence involving deception or dishonesty` |  |
| 2(10)(b)(vi) | Article 2(10)(b)(vi) | encoded | g1-art2-governor-misconduct | `Art 2(10)(b)(vi) an offence under the law of another jurisdiction similar to one in (i) to (v)` |  |

## 2. The fork register

All the fork points of the group are the eight fields of one record, `Interpretation of Articles 1 and 2`, in `g1-interpretation.l4`, each `TYPICALLY` the reading taken.
Every public decision that depends on a fork takes the record as an ordinary `GIVEN` and delegates by `CONSIDER` to one private implementation per reading; each reading has its own test.
The other reading of each fork, with every other fork left at the reading taken, is the value `the interpretation of Articles 1 and 2 with F1.n read the other way`; `the favoured interpretation of Articles 1 and 2` is the reading taken at every fork.
F1.1 to F1.5 are the survey's candidates; F1.6 to F1.8 are new.
F1.4 is changed from the survey (the reading taken is the survey's reading B) and is widened from governors to the four lists of cases, Article 2(4) to 2(7).

**Periods.** Articles 1 and 2 contain no period, no number of days, months or years, and no deadline: the words "for the time being" (Article 1 "Commissioner" and "registered charity", Article 2(1)(i)) name a standing at a moment, not a period, and are handled by fork F1.7.
So the group registers no fork on a counting convention.
The two day-edges that touch the group are the vintage resolver's: the text of 16 October 2025 begins "7 days after" the Order of 9 October 2025 was made (R&O.56/2025 Art 2; the Table of Legislation History gives 16 October 2025), and the text changes at 9.30 a.m. on 27 February 2024 (R&O.10/2024 Art 5).
Both are inputs here (`the vintage of the text`); fork F7.2 and F7.1 are the temporal group's.

### F1.1: does "(a) to (h)" reach the inserted sub-paragraph (ba)?

- **Provisions:** 2(1)(j), 2(3)(a); 2(1)(ba)(iii) says "(c) to (h)" and is not affected.
- **Field and constructors:** `ranges and sub-paragraph (ba)` of type `How the ranges (a) to (h) in Article 2 treat sub-paragraph (ba)`; `the ranges follow the letters of the amended list, so (ba) is inside (a) to (h)` (taken) and `the ranges are read as of the enactment of the Law, so (ba) is outside (a) to (h)`.
- **Reading A (taken):** by the letters, (ba) lies between (b) and (c), so it is inside "(a) to (h)" in every text that has it.
  Text that licenses it: R&O.56/2025 inserted (ba) "after paragraph (1)(b)" and the Minister chose the label (ba), not the next free letter (k); a sub-paragraph added at the end could never be a "Jersey entity" by 2(3)(a) (see contradiction C9), and the choice of label suggests that the new kind was meant to fall in the lettered range.
- **Reading B:** the ranges are read as the Law was enacted.
  Text that licenses it: R&O.56/2025 amended nothing but Article 2(1), and Article 8(3)(a)(i) and (ii) still say "(f) to (j)" and "(e), (g), (h) or (j)", which on A exclude (ba), so the Law as amended is not uniform.
- **Discriminating case:** a body corporate that is an NPO, established under the law of Jersey, within none of (c) to (h), on 2 October 2026.
  Reading A: it is a Jersey entity (2(3)(a)), so Article 21(3) bites on it if it calls itself a "charity" while unregistered; reading B: it is an entity but not a Jersey entity (2(3)(b) is for (1)(i) bodies only), so only Article 21(5) can bite, and only for its activities in Jersey.
  Also (j): a foreign analogue of such an NPO is within (j) on A and is not an entity on B.
- **Tests:** `g1-tests-art2-entity.l4`, sections "2(3) Jersey entity" (four assertions on `an NPO body corporate`) and "2(1)(j)" (`a foreign body similar to an NPO body corporate`, three texts, both readings, and the range itself).

### F1.2: do the words "in relation to ..." in 2(10)(b) govern every limb (i) to (vi)?

- **Provisions:** 2(10)(b); the same question arises in 18(4)(a) ("an offence mentioned in Article 2(10)") and 19(1)(g) ("an offence falling within Article 2(10)(b)"), which are other groups'.
- **Field and constructors:** `limbs of Article 2(10)(b)` of type `What the words in relation to a registered charity govern in Article 2(10)(b)`; `every limb (i) to (vi) needs the offence to be in relation to a charity or an equivalent entity` (taken) and `only limb (i) is tied to the charity, and limbs (ii) to (vi) apply to an offence by any person`.
- **Reading A (taken):** the sentence is "the commission by any person, in relation [to] a registered charity ..., of an offence – (i) ... (vi)"; the phrase modifies the commission, and the six limbs are only kinds of offence.
- **Reading B:** only limb (i) says "of that charity or other entity"; limbs (ii) to (v) name no charity, and 18(4)(a) and 19(1)(g) would be odd if a governor's tax offence on a personal return could never count.
- **Discriminating case:** a governor convicted of an offence under the Income Tax (Jersey) Law 1961 on a personal return unrelated to the charity.
  A: not misconduct; B: misconduct (and a reportable matter under 19(1)(g) in the other group).
- **Tests:** `g1-tests-art2-governor-misconduct.l4`, section "2(10): misconduct", `a personal tax offence by a governor`, and the six limbs on reading B.

### F1.3: what is the constitutional Law of a body incorporated "under, but not by," an enactment?

- **Provisions:** 2(5)(e) against 2(1)(g) and (h).
- **Field and constructors:** `constitutional Law of (g) and (h)` of type `The constitutional Law of a body incorporated under, but not by, an enactment`; `none, because Article 2(5) names no Law for sub-paragraphs (g) and (h)` (taken) and `the enactment under which the body is incorporated`.
- **Reading A (taken):** 2(5)(e) says "incorporated by (but not under) any other Law", the opposite of (g) and (h); the definition has no case for (ba), (g), (h), (i), (j), so it answers none.
- **Reading B:** "by (but not under)" is a slip for "under, but not by", and (g) and (h) have the enactment of incorporation as their constitutional Law.
- **Discriminating case:** a charity incorporated under, but not by, another Jersey enactment: Article 8(4)(a) asks whether its constitutional Law requires a registered office; A answers none (so 8(4)(b)), B may answer (a).
  Here: `Art 2(5) the constitutional Laws of the entity are` is empty on A and holds the enactment on B; and 2(10)(a)(ii) cannot be contravened on A.
- **Tests:** `g1-tests-art2-entity.l4`, section "2(5)", the F1.3 assertions; `g1-tests-art2-governor-misconduct.l4`, the constitutional-Law assertions of 2(10).

### F1.4: which cases of the lists in 2(4) to 2(7) apply to a body in more than one kind?

- **Provisions:** 2(4), 2(5), 2(6), 2(7); Article 8(3)(a)(i) ("whether it also falls within sub-paragraph (a)") shows that one entity can be in the case of a trust and the case of a company.
- **Field and constructors:** `cases for a body in more than one kind` of type `How the cases of Article 2(4) to (7) combine for a body in more than one kind`; `every case of Article 2(4) to (7) that applies` (taken) and `only the first case of Article 2(4) to (7) that applies, in the order the paragraph lists them`. "In any other case" ((4)(g), (6)(d), (7)(e)) is read as the residue: it applies when none of the specific cases applies to the body.
- **Reading A (taken; the survey's reading B):** each paragraph is a list of cases each of which applies where its case holds; nothing gives (a) precedence; so a company that is the sole trustee has both the trustee and its directors as governors, both sets of documents as constitution, and both Laws.
  Licensed by the lists' own form ("in the case of ..."), by Article 8(3)(a)(i), and by the purpose of the governor duties (the people who run the charity).
- **Reading B (the survey's reading A):** the first case in the paragraph's order.
  Licensed by "in any other case" read as the last item of a decision list.
- **Why changed from the survey:** the survey's reading needs "the entity" of 2(7) to mean one kind of the body, while 8(3)(a)(i) treats the body as one entity that is in several kinds; and on reading B a charity that is a company acting as sole trustee would have no human governor.
- **Discriminating case:** a director of a company that is the sole trustee of the charity's trust.
  A: a governor (Article 19(2) reporting duty, 18 duties); B: not.
  For 2(4): both documents or the trust's only; 2(5): both Laws or the Trusts Law only; 2(6): a foundation that is also the sole trustee has both sets of purposes (A) or the trust's purposes only (B).
- **Tests:** `g1-tests-art2-governor-misconduct.l4`, section "2(7): a body in more than one kind"; `g1-tests-art2-entity.l4`, the F1.4 assertions in sections 2(4), 2(5), 2(6).

### F1.5: is information "published" on the publisher's opinion or on the manner's likelihood?

- **Provisions:** Article 1 "publish" ("publish" or "published" appears in Articles 4(1)(d), 5(4), 5(6)(b), 5(7), 7(4), 9(4)(a), 10(2)(b), 11(2), 11(6)(a), 11(9) and Schedule 1 paragraphs 4(8) and 4(11), by a grep of the text on 2026-10-26, and Article 2(8)(b)(i) here).
- **Field and constructors:** `meaning of published` of type `What makes information published under Article 1`; `the opinion of the person publishing` (taken) and `the likelihood of the manner, judged objectively`.
- **Reading A (taken):** the text says "in the opinion of the person publishing". **Reading B:** the manner must in fact be likely to reach the public or those affected.
- **Discriminating case:** a notice posted only in a locked cabinet, which its publisher honestly believes adequate: published on A, not on B. Inside this group: a model constitution the Commissioner posted that way is "published for the purpose by the Commissioner" (2(8)(b)(i)) on A, so the unincorporated body is a relevant unincorporated entity and its committee members are governors; on B it is not, and the person with the general control and management is the governor under (7)(e).
- **Tests:** `g1-tests-art1.l4`, section "The definition of publish"; `g1-tests-art2-governor-misconduct.l4`, sections "2(8)" and "2(8) ... and (7)(d)".

### F1.6: does "in relation to Jersey" in 2(1)(e) qualify (iii) only, or each of (i) to (iii)?

- **Provisions:** 2(1)(e)(i) to (iii): "(i) by an enactment, (ii) by Act of the States, or (iii) by Royal Charter, in relation to Jersey;".
- **Field and constructors:** `reach of in relation to Jersey` of type `What the words in relation to Jersey qualify in Article 2(1)(e)`; `only the Royal Charter in sub-paragraph (iii)` (taken) and `each of sub-paragraphs (i), (ii) and (iii)`.
- **Reading A (taken):** the words follow a comma after "Royal Charter", and a Royal Charter is the one source that can be granted to bodies anywhere; an enactment and an Act of the States are of Jersey by their nature. **Reading B:** the words qualify the whole list: a body established by a United Kingdom Act that is not "in relation to Jersey" is not within (e) (it would be a foreign entity in (j)).
- **Discriminating case:** a body corporate established by an enactment that is not in relation to Jersey: within (e), hence a Jersey entity, on A; not within (e) on B. The Royal Charter case gives the same answer on both.
- **Tests:** `g1-tests-art2-entity.l4`, section "2(1) the kinds of entity", the (e) assertions.

### F1.7: is the standing of a "registered charity" read when the conduct occurred or when the question is asked?

- **Provisions:** Article 1 "registered charity ... entered for the time being", used in 2(10)(a) and (b); the same question arises in 14(1)(a), 17(9)(a) and 27(1)(a) in other groups.
- **Field and constructors:** `time of the standing of a charity` of type `When the standing of a registered charity is read for Article 2(10)`; `when the conduct in Article 2(10) occurred` (taken) and `when the question under Article 2(10) is asked`.
- **Reading A (taken):** Article 14(1)(a) speaks of misconduct that "is or has been", which would make no sense if deregistration erased the past; and a reading B lets an entity escape the consequences of its misconduct by being deregistered. **Reading B:** "for the time being" is present tense, and Article 17(9)(a) needs the counterfactual "would have been misconduct if the entity had not been deregistered", which reads naturally if misconduct is judged by today's standing.
  The text does not settle it.
- **Discriminating case:** a contravention while the charity was in the general section, asked about after the charity was deregistered: misconduct on A, not on B; and a contravention before registration, asked about after: not on A, misconduct on B.
- **Tests:** `g1-tests-art2-governor-misconduct.l4`, `a contravention by a charity since deregistered`, `a contravention before the charity was registered`, and the (b) case `an offence in relation to a charity since deregistered`.

### F1.8: does sub-paragraph (g) overlap (c), (d) and (f)?

- **Provisions:** 2(1)(g) against 2(1)(c), (d), (f); Article 8(3)(a)(i) and (ii).
- **Field and constructors:** `overlap of sub-paragraph (g)` of type `Whether sub-paragraph (g) overlaps sub-paragraphs (c), (d) and (f)`; `as written, so a foundation or an incorporated 1862 association is also within (g)` (taken) and `(g) is the residue, so a body within (c), (d) or (f) is not also within (g)`.
- **Reading A (taken):** (g) excludes only the Companies (Jersey) Law 1991; a foundation is incorporated under the Foundations (Jersey) Law 2009, an enactment other than the Companies Law, and an 1862 association under the Loi of 1862.
  The encoding follows the words.
- **Reading B:** Article 8(3)(a)(i) asks for "the sub-paragraph" (singular) within which the entity falls, which suggests the kinds were meant to be exclusive apart from (a); (g) is then the residue.
- **Discriminating case:** a foundation: kinds `a foundation` and `a body incorporated under, but not by, an enactment ...` (A) or `a foundation` alone (B); the register note of Article 8(3)(a) has one entry or two, and (ii) asks for details of the enactment for (g).
- **Tests:** `g1-tests-art2-entity.l4`, section "2(1)(g): does it overlap (c), (d) and (f)? (fork F1.8)".

## 3. The answer table

All expected values come from the source; the test that holds each is in the module named.
"Text" is the vintage of the text of the Law.

| scenario | answer | Article | test module |
| --- | --- | --- | --- |
| who is "the Minister" in the text of 1 January 2019 | the Chief Minister (derived from the words R&O.40/2019 replaced) | 1 "Minister" | tests-art1 |
| ... 31 May 2019, 16 December 2019, 1 January 2020 | the Minister for External Relations | 1 "Minister" | tests-art1 |
| ... 2 March 2021 | the Minister for External Relations and Financial Services (R&O.29/2021 Sch 2 para 1(e)) | 1 "Minister" | tests-art1 |
| ... 12 April 2023 | the Chief Minister (R&O.28/2023) | 1 "Minister" | tests-art1 |
| ... 27 February 2024, 16 October 2025 | the Minister for External Relations (R&O.10/2024) | 1 "Minister" | tests-art1 |
| ... 2 October 2026 | the Chief Minister (R&O.102/2026) | 1 "Minister" | tests-art1 |
| ... before 1 January 2019 | refuses: no text is among the sources | 1 "Minister" | tests-art1 |
| which Law defines "Comptroller" in the text of 1 January 2020 and later | the Revenue Administration (Jersey) Law 2019 | 1 "Comptroller" | tests-art1 |
| ... in the texts of 1 January, 31 May and 16 December 2019 | the Income Tax (Jersey) Law 1961 | 1 "Comptroller" | tests-art1 |
| an entity in the general or the restricted section | a registered charity | 1 "registered charity" | tests-art1 |
| an applicant, a body not on the register, a body in the historic section | not a registered charity | 1 "registered charity" | tests-art1 |
| a body in the general section that falls within no sub-paragraph of 2(1) | not a registered charity (not an entity) | 1 "registered charity" | tests-art1 |
| a notice in a locked cabinet that its publisher thinks adequate | published on A, not on B | 1 "publish" (F1.5) | tests-art1 |
| a trust; a fidéicommis; an 1862 association; a foundation; a company; a body under an enactment; a body under a UK Act | each is its own kind, and a Jersey entity | 2(1)(a) to (h), 2(3)(a) | tests-art2-entity |
| a company that is the sole trustee | kinds (a) and (f), in that order | 2(1), 8(3)(a)(i) | tests-art2-entity |
| an NPO body corporate established under Jersey law, in the text in force on 15 October 2025 (the text of 27 February 2024) | not an entity | 2(1)(ba) (R&O.56/2025) | tests-art2-entity |
| the same body in the text of 16 October 2025 and of 2 October 2026 | an entity of kind (ba), and (reading A) a Jersey entity | 2(1)(ba), 2(3)(a) | tests-art2-entity |
| the same body that is also a company | kind (f) only: (ba)(iii) excludes it | 2(1)(ba)(iii) | tests-art2-entity |
| a partnership; a body of unincorporated persons that is the trustees of a trust | not within (i) | 2(1)(i) | tests-art2-entity |
| a foreign body similar to a company | kind (j), not a Jersey entity | 2(1)(j), 2(3) | tests-art2-entity |
| an unincorporated body governed by Jersey law with a resident natural-person governor | a Jersey entity | 2(3)(b) | tests-art2-entity |
| ... whose only qualifying governor is itself a Jersey entity only by (b) | not a Jersey entity | 2(3)(b)(ii) | tests-art2-entity |
| the Minister makes an Order adding "(ba)" | the permission is taken up: FULFILLED; unused it is not a breach | 2(2) | tests-art2-entity (3 traces) |
| the constitution of a trust, of a foundation, of a company | the terms of the trust; the charter and regulations; the memorandum and articles | 2(4)(a), (d), (e) | tests-art2-entity |
| the constitutional Law of a trust, a foundation, a company | the Trusts (Jersey) Law 1984; the Foundations (Jersey) Law 2009; the Companies (Jersey) Law 1991 | 2(5)(a), (c), (d) | tests-art2-entity |
| the constitutional Law of an NPO body corporate, an unincorporated body, a foreign body | none | 2(5) (trap T6) | tests-art2-entity |
| a trustee of a trust; a council member; a director; a committee member of a relevant unincorporated entity | a governor | 2(7)(a) to (d) | tests-art2-governor-misconduct |
| the person with the general control and management, alone or as one of a number, of any other entity | a governor | 2(7)(e), 2(9)(b) | tests-art2-governor-misconduct |
| a person who only exercises the control for another who has it in own right | not a governor | 2(9)(a) | tests-art2-governor-misconduct |
| a director of a company that is the sole trustee | a governor on A, not on B | 2(7), F1.4 | tests-art2-governor-misconduct |
| a contravention of this Law by a registered charity | misconduct | 2(10)(a)(i) | tests-art2-governor-misconduct |
| a contravention of a required steps notice when none has been served | not misconduct | 2(10)(a)(iii) | tests-art2-governor-misconduct |
| an offence under the tax Laws in relation to a registered charity | misconduct | 2(10)(b)(iii) | tests-art2-governor-misconduct |
| the same offence, unrelated to any charity | not misconduct on A, misconduct on B | 2(10)(b), F1.2 | tests-art2-governor-misconduct |

## 4. Nouns requests for the INTEGRATOR

`domain.l4` was read and not edited.
The following nouns are defined in G1's own modules; the integrator may move them to `domain.l4` if another group needs to name them.

1. `Constitutional Law of an entity` (in `g1-art2-entity.l4`): the answer of Article 2(5).
   Consumers: 8(4)(a), 13(2) and (3), 17(7), 18(3), 31(d), and 2(10)(a)(ii) and (b)(i) here.
   Those groups read "the constitutional Law of the entity" as a fact; they can take the list `Art 2(5) the constitutional Laws of the entity are` as their input.
2. `Facts about a publication` (in `g1-art1-defined-terms.l4`): what a publisher did, thought and achieved.
   Every group that says "publish" (Articles 4, 5, 9, 11 and Schedule 1) can call `Art 1 the information has been published` with it, or keep a BOOLEAN of their own.
3. `Kind of entity` in `domain.l4` merges 2(1)(e)(i) to (iii) into one constructor.
   Article 8(3)(a)(ii) asks for "details of the enactment, Act of the States, Royal Charter, ... by virtue of which it falls within" (e), (g), (h) or (j), so G3 needs which of the three it was and, for (g), (h), (j), which enactment or foreign law.
   G1's `Facts about the body under Article 2` carries `established by an enactment`, `established by Act of the States`, `established by Royal Charter` and the two enactment-name fields; G3 can read them from there, or `Entity` could carry them.
4. `Entity` has no field for the register note "whether it also falls within sub-paragraph (a)" (8(3)(a)(i)); it is derivable from `kinds of entity` (membership of `the trustees of a trust`), so none is needed.
5. `Governor` in `domain.l4` has fields named `is a natural person`, `is resident in Jersey` and `is itself a Jersey entity by virtue of Article 2(3)(a)`, which begin with `is`; the house ruling on clitic verbs asks fields to start at the complement.
   Read-only to G1, so recorded here.
6. The roles `the Comptroller` and `the Jersey Financial Services Commission` are constructors of `Legal actor` already; no request.

## 5. Inputs consumed, functions exported

### Standard inputs consumed (PLAN section (c))

| id | exact `GIVEN` name and type | where |
| --- | --- | --- |
| IP2 | `the vintage of the text` : `Vintage of the text` | `Art 1 the Minister under the text of`, `Art 1 the Law that defines the Comptroller under the text of`, and every `Art 2(1)`, `Art 2(3)` and `Art 2` entity function. A vintage that does not decide a fact answers a refusal: `before the first consolidated version` refuses everywhere |
| IP5 | `the entity` : `Entity` | `Art 1 the entity is a registered charity` |
| IP13 | `the charity or governor has contravened a provision of this Law or an enactment under it` : BOOLEAN | `Art 2(10) the conduct is misconduct`, `Art 2(10)(a)(i) ...` |
| IP19 | `the required steps notices served` : LIST OF `Required steps notice` | `Art 2(10) the conduct is misconduct`, `Art 2(10)(a)(iii) ...` (a contravention of a notice needs a notice served) |
| IP26 | `the entity is an excepted foreign charity` : BOOLEAN | `Art 2(10) the conduct is misconduct`, `Art 2(10)(b) ...` |

IP1 (`the day`) is not used: Articles 1 and 2 have no date rule of their own; the text in force is the vintage.

### Facts that stay in G1 (raw facts about a body, a person and conduct)

`Facts about the body under Article 2` (23 fields: the status under the other enactments, how the body was established, its governors), `Facts about a person's role in an entity` (5 fields), `Facts about the model constitution of Article 2(8)`, `Facts about a publication`, `Facts about conduct under Article 2(10)` (19 fields).
Each field has a `@desc` that says which sub-paragraph it feeds.

### Functions exported (`@export`, with a sentence and a `@desc` on every `GIVEN`)

| exact name | takes | gives |
| --- | --- | --- |
| `Art 1 the Minister under the text of` | `the vintage of the text` | `Office of the Minister` (IP3 `the office of the Minister`); refuses before the first text |
| `Art 1 the Law that defines the Comptroller under the text of` | `the vintage of the text` | `Law defining the Comptroller` (a G1 type) |
| `Art 1 the entity is a registered charity` | `the entity` | BOOLEAN (IP6 `the entity is a registered charity`); false for an entity with no kind |
| `Art 1 the information has been published` | interp, `Facts about a publication` | BOOLEAN |
| `Art 2(1) the kinds of entity the body falls within` | interp, `the vintage of the text`, `Facts about the body under Article 2` | `LIST OF Kind of entity`, in the Law's order; empty if not an entity; refuses before the first text |
| `Art 2(1) the body is an entity` | the same | BOOLEAN |
| `Art 2(2) the Minister may add a sub-paragraph to Article 2(1)` | none | `DEONTIC Legal actor Act under Article 2` (MAY, no WITHIN) |
| `Art 2(3) the body is a Jersey entity` | interp, `the vintage of the text`, facts | BOOLEAN (IP5 field `is a Jersey entity`) |
| `Art 2 the body as an entity` | interp, `the vintage of the text`, name, standing, purposes, facts | `Entity` with `kinds of entity`, `is a Jersey entity` and `governors` derived (IP5) |
| `Art 2(4) the constitution of the entity consists of` | a `Kind of entity` | STRING |
| `Art 2(4) the constitution of the entity in all its kinds consists of` | interp, the kinds | `LIST OF STRING` |
| `Art 2(5) the constitutional Laws of the entity are` | interp, the kinds, facts | `LIST OF Constitutional Law of an entity` (empty: none) |
| `Art 2(5) the constitutional Law of the entity is` | interp, a kind, facts | `MAYBE Constitutional Law of an entity` (the PLAN's name; NOTHING: none) |
| `Art 2(6) the purpose of the entity means` | a `Kind of entity` | STRING |
| `Art 2(6) the purposes of the entity in all its kinds mean` | interp, the kinds | `LIST OF STRING` |
| `Art 2(7) the person is a governor of the entity` | interp, the kinds, the model facts, the person's role | BOOLEAN |
| `Art 2(7) the governors among the people` | interp, the kinds, the model facts, `LIST OF Person considered as a governor` | `LIST OF Governor` (IP5 field `governors`) |
| `Art 2(8) the entity is a relevant unincorporated entity` | interp, the kinds, the model facts | BOOLEAN |
| `Art 2(10) the conduct is misconduct` | interp, conduct facts, IP26, IP13, IP19 | BOOLEAN (IP12 `the conduct is misconduct within Article 2(10)`) |

**Where this differs from the PLAN's signatures (the integrator wires by this table).** The PLAN's `Art 2(1) ...` functions take "the raw facts"; here they take `the vintage of the text` as well, because sub-paragraph (ba) is in the text of the Law from 16 October 2025 and the PLAN's own export table already lists the vintage.
The assignment said to take (ba) as a `GIVEN` from the temporal group; the standard name for it is IP2, so (ba) is derived inside G1 from `the vintage of the text` and no separate (ba) input exists.
`Art 2(4)` and `Art 2(6)` have a second, list-valued function because of F1.4, and `Art 2(5)` answers a list or a `MAYBE` of a typed Law, not a `MAYBE STRING`, so a consumer matches on a constructor.
`Art 2(8)` takes the model facts as a record, not two BOOLEANs, because "published" is Article 1's defined term (F1.5).

**Wiring.** The integrator builds `the entity` for every consumer once: `Art 2 the body as an entity` gives `kinds of entity`, `is a Jersey entity` and `governors`; `standing on the register` and `purposes` are its inputs; `Art 1 the entity is a registered charity` on that record must equal the BOOLEAN `the entity is a registered charity` the consumers take (IP6).

## 6. Contradictions in the source, from a separate pass

Found by a pass made after the encoding was finished and green, reading Articles 1 and 2 against each other and against every use of their terms in the rest of the Law (grep of each defined term), and against the PDF text layer.
The consolidated text and the official PDF text layer agree word for word on Articles 1 and 2 (a token-level comparison of 1,950 tokens found six differences: four page headers and two footnote markers, no word).

- **C1: 2(10)(b), "in relation a registered charity".** A "to" is missing, in the consolidated text and in the PDF alike.
  The sense is clear; no case discriminates.
  Flagged in the module comment.
- **C2: 2(10)(b)(vi), "clauses (i) to (v)".** The Law says "sub-paragraphs" for the lettered level, (a), (b) and so on.
  It has no other name for the level of (i) to (v) (a search of the consolidated text for "paragraphs (i)", "sub-paragraphs (i)" and "clause (i)" finds nothing), so this use of "clauses" is not shown to be a slip.
  No case discriminates.
- **C3: 2(5) names a Law for five kinds of entity out of twelve (trap T6), and (e) says "by (but not under)".** Sub-paragraphs (g) and (h) are "under, but not by".
  No case for (ba), (g), (h), (i), (j).
  Also (e) reaches only a body established by a Law, not one established by Act of the States or by Royal Charter, though 2(1)(e) lists those.
  Discriminating case: a charity incorporated under, but not by, another Jersey enactment (F1.3).
- **C4: 2(1)(g) overlaps (c) and (d) as written, against Article 8(3)(a)(i)'s "the sub-paragraph".** (g) excludes only the Companies (Jersey) Law 1991, so a foundation and an 1862 association are also within (g).
  Discriminating case: a foundation (F1.8).
- **C5: 2(1)(j), "an entity that is substantially similar to an entity".** The definition of "entity" uses the word "entity" for the thing being defined; read as any body.
  No case discriminates.
- **C6: 2(1)(b) is "without prejudice to the generality of sub-paragraph (a)", and (i) excludes "the trustees of a trust" only.** A court-approved fidéicommis may be a trust within (a) as well as (b); whether its fidéicommissaires fall within (i) is not stated.
  Input; no fork.
  Discriminating case: a group of fidéicommissaires that is also an unincorporated body: (b), and (i) only if it is not "the trustees of a trust".
- **C7: R&O.56/2025 inserted (ba) and amended nothing else, so 8(3)(a)(i) ("sub-paragraphs (f) to (j)") and 8(3)(a)(ii) ("(e), (g), (h) or (j)") do not mention (ba).** A (ba) body gets no "also within (a)" note and no enactment details though it is "established under the law of Jersey".
  Another group's provisions; the survey's trap T5.
  Discriminating case: an NPO body corporate that is also the sole trustee of a trust.
- **C8: 2(10)(b) imports "excepted foreign charity (within the meaning of Article 22)", and 22(1) says "For the purpose of Article 21".** The express cross-reference brings the meaning in; the text of Article 22 is addressed to Article 21.
  No case discriminates.
- **C9: an Order under 2(2) can add a sub-paragraph to paragraph (1) but cannot reach 2(3).** A kind added at the end (say "(k)") is an entity but is never a "Jersey entity" (2(3)(a) names (a) to (h) and (b) is for (1)(i) only).
  The Order R&O.56/2025 avoided that by labelling its addition (ba), inside the lettered range; this is the strongest text for reading A of F1.1.
  Test: `a body within an added sub-paragraph` is not a Jersey entity.
- **C10: Article 1 defines "council member" for a foundation, and nothing uses the term.** 2(7)(b) says "a member of the council of the foundation".
  A defined term that is never used.
  No case discriminates.
- **C11: Article 1 defines "general section" and "restricted section" and not "historic section"**, which 8(2)(c), 8(5) and 10(3)(c) use (trap T7).
  It matters here: "registered charity" is the general or the restricted section only, so a formerly registered charity is not one.
- **C12: Article 1 "tribunal" is "the Charity Tribunal established by Article 32", and Schedule 2 is headed "Charity Commission tribunal".** The heading of Article 32 says "Charity Tribunal".
  No case discriminates.
- **C13: Article 1 "Minister means the Chief Minister" against "a Minister" in 5(2)(a).** Trap T4, fork F2.3 of another group.
  Here: noted in the comment at the definition.
- **C14: 17(9)(a) and 14(1)(a) against Article 1 "for the time being"** (fork F1.7): "is or has been misconduct" and "would have been misconduct if the entity had not been deregistered" point in opposite directions on whether the standing of the charity is read when the conduct occurred.
- **C15: an inconsistent citation in an amending instrument, not in the Law.** L.13/2019 Schedule 3 is headed "(Article 29(2))", and the Article that says "Schedule 3 has effect" is 28(2).
  It does not matter to the answer: neither Article is among 17 to 19, which R&O.136/2019 leaves out of the appointed day of 1 January 2020.
- **C16: 2(10)(b)'s offences as 18(4)(a) states them.** 18(4)(a) says "commits an offence, mentioned in Article 2(10)", which can be read without the connection to a charity; that supports reading B of F1.2 in the other group's provision.
  Recorded under F1.2.

## 7. Open questions for a domain expert

1. Is sub-paragraph (g) meant to overlap (c) and (d)? (C4, F1.8)
2. Does "in relation to Jersey" in 2(1)(e) qualify only the Royal Charter? Does "enactment" there include a United Kingdom Act that does not extend to Jersey? (F1.6)
3. Is the constitutional Law of a body incorporated "under, but not by," an enactment that enactment, and what is the constitutional Law of a (ba) body and of an unincorporated body? (C3, F1.3)
4. For a company that is the sole trustee of a charitable trust, are its directors governors of the charity? Do both the trust deed and the memorandum and articles make up its constitution? (F1.4)
5. Must an offence under 2(10)(b)(ii) to (vi) be in relation to a charity? Does 18(4)(a) read "an offence mentioned in Article 2(10)" with or without that connection? (F1.2)
6. Is a contravention by a charity that has since been deregistered "misconduct"? (F1.7)
7. Was the Order of 2025 meant to put (ba) inside "(a) to (h)", and should 8(3)(a)(i) and (ii) be read as covering it? (F1.1, C7)
8. Is "published" the publisher's honest opinion, or an objective test? (F1.5)
9. Is it intended that an Order adding a sub-paragraph at the end of 2(1) cannot create a Jersey entity? (C9)
10. Has the Commissioner published a model constitution under 2(8)(b)(i), and where? None is among the sources.

## 8. What the sources do not answer

Each is an input or a named refusal in the encoding, never a plausible value.

1. **The text of the Law before 1 January 2019.** The nine consolidated texts begin there.
   `Art 1 the Minister under the text of`, `Art 1 the Law that defines the Comptroller under the text of` and every function of `the vintage of the text` refuse for `before the first consolidated version`. R&O.40/2019 shows that the words of "Minister" before 31 May 2019 were "Chief Minister"; that is carried as the text of 1 January 2019, derived and not quoted.
2. **That sub-paragraphs (a) to (j) of Article 2(1) read the same in every text from 1 January 2019 to 15 October 2025.** The Table of Legislation History lists no amendment of Article 2(1) before R&O.56/2025 (endnote [2]); no consolidated text of those years is among the sources.
3. **The other enactments**: the Trusts (Jersey) Law 1984, the Companies (Jersey) Law 1991, the Foundations (Jersey) Law 2009, the Non-Profit Organizations (Jersey) Law 2008, the Loi (1862), the Revenue Administration (Jersey) Law 2019, the Income Tax (Jersey) Law 1961 and the financial-services Laws.
   Whether a body is a trust, a company, a foundation, an NPO or an 1862 association, who its trustees, directors and council members are, and whether an act is an offence under one of those Laws, are inputs.
4. **What "enactment" means in 2(1)(e)(i) and 2(1)(g)** (the Interpretation (Jersey) Law 1954 is not among the sources), and whether "partnership" includes the limited and separate limited partnerships.
5. **The judgements**: "substantially similar" (2(1)(j)), "conforms to a model" (2(8)(b)), "in the opinion of the person publishing" (Article 1), whether an offence "involves deception or dishonesty" or is "similar" (2(10)(b)(v), (vi)), "resident in Jersey" (2(3)(b)(ii)).
6. **Any Order under 2(2)** other than R&O.56/2025, and anything made after the text of 2 October 2026.
   The `the sub-paragraphs added by Order within which the body falls` field carries what an Order adds; its content is the caller's.
7. **Whether a contravention of this Law has occurred** (the standard input IP13): every duty of every group decides its own breach; this group takes the fact.
8. **The model constitutions the Commissioner has published**, and the Orders and Regulations of any other Article.
9. **The meaning of the register's "historic section" for the purposes of Article 1**: the term is not defined (C11); the definition of "registered charity" is read as excluding it.

## 9. What the instruments showed, against the survey

- R&O.29/2021 is among the inputs: it substitutes "Minister for External Relations and Financial Services" for "Minister for External Relations" in Article 1 of this Law (Sch 2 para 1(e), made and in force 2 March 2021).
  The survey said the 2 March 2021 text was inferred; it is shown.
- R&O.136/2019 is among the inputs: it brings the Revenue Administration (Jersey) Law 2019 into force on 1 January 2020 other than Articles 17 to 19, so L.13/2019 Sch 3 para 1 (the "Comptroller" amendment) took effect on 1 January 2020.
  The survey said the instrument was not among the inputs.
- The chain of the five "Minister" amendments closes: each instrument replaces the words the one before it put in, and the last puts back the words the first replaced (a test in `g1-tests-art1.l4` asserts it).
- The dates of the Table agree with the instruments: R&O.56/2025 made 9 October 2025 and in force "7 days after it is made" (16 October 2025); R&O.28/2023 made 5 April 2023 and in force 7 days after (12 April 2023); R&O.102/2026 made 25 September 2026 and the rest in force 7 days after (2 October 2026).
  The counting of "7 days after" is fork F7.2 of the temporal group; the encoding takes the Table's dates.

## 10. Peeked

Nothing under the forbidden directories was opened or listed.
I listed `FLEET_DIR/work` once, to see that my own directory could be created; it showed the names of other agents' directories and I opened none of them.
While probing the compiler I once copied the DEPOSIT directory into my own `work/g1/probe` (to give a probe file its `domain.l4`); the copy included other groups' modules as they stood at that moment, and a later `ls` of that probe directory and of DEPOSIT printed their file names.
I opened none of those files, and I deleted the copies from `work/g1/probe`; only the names of other groups' modules were seen.
My context carried the harness's memory index, which names notes on this subject; I did not follow it and read none of the notes.
