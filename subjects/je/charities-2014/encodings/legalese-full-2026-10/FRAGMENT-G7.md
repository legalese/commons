# FRAGMENT-G7: the Charities (Jersey) Law 2014, Articles 21 to 25, Articles 37 to 43 and the endnotes (the temporal axis)

Encoder: G7.
Status: draft; no domain expert has read this against the Law.
Scope: Part 6 (Articles 21 to 25), Part 9 (Articles 37 to 43), the endnotes (Table of Legislation History, Table of Renumbered Provisions, Table of Endnote References); 129 coverage rows.
Source: `inputs/charities-jersey-law-2014-2026-10-02.txt` (RAW) checked against `inputs/charities-jersey-law-2014-official-pdf-text-layer.txt`, and the amending instruments in `inputs/amending/`.
Tool: the fleet binary `bin/l4` (sha256 18bd5a72...), `JL4_LIBRARY_PATH` unset.

## 0. What is in the deposit

| file | holds |
| --- | --- |
| g7-interpretation.l4 | the record `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` (fourteen fork fields), its enumerations, `the favoured interpretation`, one value per fork with the other reading, and `the favoured interpretation with the unit of a term of imprisonment` (IP35) |
| g7-vintages.l4 | the eight amending instruments of the Table as data, the nine texts, the resolver from a day or an instant to a `Vintage of the text` (IP2), what each text says (Minister, Comptroller, paragraph (ba), the Dormant Bank Accounts openings), the "7 days after it is made" rule, the amending instruments in force |
| g7-commencement.l4 | the staged commencement in the Table's own (original) numbers, the Table of Renumbered Provisions as data, the Articles each Part held (including the spent original Article 41, which stood in Part 9), the stage of each Part, Article and Schedule, whether a unit is in force on a day or at an instant (IP4) |
| g7-art21-23-expressions.l4 | Articles 21 to 23: the eight prohibitions as regulative rules and as booleans, the offences, the penalties as data, the excepted foreign charity (IP26), the powers of the States and the Minister; every prohibition binds or concerns an ENTITY only (a body whose `kinds of entity` is not empty) |
| g7-art24-25-powers.l4 | Articles 24 and 25: the powers, what a relevant term is, the cap on the penalty, the illustrative content of an Order carried as text |
| g7-art37-43-final.l4 | Articles 37 to 43: the officer's liability and penalty, the date of service, the ancillary powers, the savings and transitional powers, Articles 41 and 42 as powers, the citation |
| g7-tests-fixtures-expressions.l4 | fixtures only (entities, bodies that are not entities, awareness, intent, statements, 52 scenarios); no directive |
| g7-tests-vintages.l4, g7-tests-commencement.l4, g7-tests-expressions.l4, g7-tests-powers-final.l4 | the assertions |
| g7-tests-expression-traces.l4 (and the traces in g7-tests-powers-final.l4) | `#TRACE` of the regulative rules, each with an EXPECT comment, checked by `work/g7/check-traces.py` |
| g7-tests-red.l4 | 15 assertions that are MEANT to fail: the other reading of each fork asserted against the reading taken (14), and one claim of the brief that the instruments correct (1) |

Every module imports only `prelude`, `daydate`, `domain` and modules of group G7.
No module starts with `@lang en`.
No module contains an assertion except the `g7-tests-*` modules.
`DATETIME` values are ordered by `DATETIME_SERIAL`, because the comparison operators on `DATETIME` are in the `datetime` library, which a group module may not import (brief, ruling 1).

The test modules each define their own fixtures (`fav`, `other F7.n`, `an instant in Jersey`, `an instant in UTC`); `g7-tests-red.l4` and the traces module import `g7-tests-fixtures-expressions`; the test modules are not meant to be imported together.
The sentences of this file are one to a line, so that a grep returns a whole sentence.

## 1. Coverage

Rows are those of PLAN's `coverage.tsv` for group G7, in the Law's numbering; there are 129.
The module column names the module that carries the row; the next column names the rules, data or heading.
Summary: 110 `encoded`, 18 `inert`, 1 `refused`, 0 `out-of-scope`, 0 `deferred`.
Nine rows moved from PLAN's `out-of-scope` to `encoded`: 41, 41(1), 41(1)(a), 41(1)(b), 41(1)(c), 41(2), 42, 42(a), 42(b).
The reason is ruling 4 of the brief: Articles 41 and 42 are powers of the States to make Regulations and are encoded as `MAY` rules; the enactments they would amend are not in the sources and are not encoded.
No other disposition differs from PLAN's.

| id | provision | disposition | module | rules / data | note |
| --- | --- | --- | --- | --- | --- |
| Commencement note | Commencement note | inert | g7-commencement | `the commencement note of the Law points to the endnotes` | pointer only |
| 21 | Article 21 | encoded | g7-art21-23-expressions | `§§ Article 21` and the rules for its paragraphs |  |
| 21(1) | Article 21(1) | encoded | g7-art21-23-expressions | `Art 21(1) the prohibition binds the entity`; `Art 21(1) the statement contravenes paragraph (1)`; `Art 21(1) an unregistered entity must not say it is registered by the Commissioner` |  |
| 21(1)(a) | Article 21(1)(a) | encoded | g7-art21-23-expressions | `Art 21(1)(a) the entity contravenes sub-paragraph (a)`; `Art 21(1)(a) an unregistered entity must not refer to itself as being registered by the Commissioner` |  |
| 21(1)(b) | Article 21(1)(b) | encoded | g7-art21-23-expressions | `Art 21(1)(b) the entity contravenes sub-paragraph (b)`; `Art 21(1)(b) an unregistered entity must not cause or permit another person to refer to it as being registered by the Commissioner` |  |
| 21(2) | Article 21(2) | encoded | g7-art21-23-expressions | `Art 21(2) the prohibition binds the person`; `Art 21(2) the statement contravenes paragraph (2)`; `Art 21(2) a person must not say that an unregistered entity is registered, with knowledge and intent` | fork F7.4 with 21(1) |
| 21(2)(a) | Article 21(2)(a) | encoded | g7-art21-23-expressions | `the person knows, suspects or has reasonable grounds to suspect it` over field `that the entity is not a registered charity` of `Awareness of the person making a statement` |  |
| 21(2)(b) | Article 21(2)(b) | encoded | g7-art21-23-expressions | `the intent is within the advantage sub-paragraph` called with TRUE (other advantage reached) |  |
| 21(2)(b)(i) | Article 21(2)(b)(i) | encoded | g7-art21-23-expressions | field `to cause another person to be misled as to the nature of the entity` of `Intent of the person making a statement` |  |
| 21(2)(b)(ii) | Article 21(2)(b)(ii) | encoded | g7-art21-23-expressions | fields `to cause another person to give the entity any property`, `... a financial advantage`, `... some other advantage` of `Intent of the person making a statement` | fork F7.5: “or other advantage” is here and not in 21(4), 21(6), 23(2) |
| 21(3) | Article 21(3) | encoded | g7-art21-23-expressions | `Art 21(3) the prohibition binds the Jersey entity`; `Art 21(3) the statement contravenes paragraph (3)`; `Art 21(3) a Jersey entity that is not registered must not call itself a “charity”` |  |
| 21(3)(a) | Article 21(3)(a) | encoded | g7-art21-23-expressions | `Art 21(3)(a) the Jersey entity contravenes sub-paragraph (a)`; `Art 21(3)(a) a Jersey entity that is not registered must not refer to itself as a “charity”` |  |
| 21(3)(b) | Article 21(3)(b) | encoded | g7-art21-23-expressions | `Art 21(3)(b) the Jersey entity contravenes sub-paragraph (b)`; `Art 21(3)(b) a Jersey entity that is not registered must not cause or permit another person to refer to it as a “charity”` |  |
| 21(4) | Article 21(4) | encoded | g7-art21-23-expressions | `Art 21(4) the prohibition binds the person`; `Art 21(4) the statement contravenes paragraph (4)`; `Art 21(4) a person must not call an unregistered Jersey entity a “charity”, with knowledge and intent` | forks F7.4, F7.5 |
| 21(4)(a) | Article 21(4)(a) | encoded | g7-art21-23-expressions | `Art 21(4) the prohibition binds the person` (awareness of BOTH (i) and (ii)) |  |
| 21(4)(a)(i) | Article 21(4)(a)(i) | encoded | g7-art21-23-expressions | field `that the entity is a Jersey entity` of `Awareness of the person making a statement` |  |
| 21(4)(a)(ii) | Article 21(4)(a)(ii) | encoded | g7-art21-23-expressions | field `that the entity is not a registered charity` of `Awareness of the person making a statement` |  |
| 21(4)(b) | Article 21(4)(b) | encoded | g7-art21-23-expressions | `the intent is within the advantage sub-paragraph` called with `Articles 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii) reach other advantage under` |  |
| 21(4)(b)(i) | Article 21(4)(b)(i) | encoded | g7-art21-23-expressions | field `to cause another person to be misled as to the nature of the entity` |  |
| 21(4)(b)(ii) | Article 21(4)(b)(ii) | encoded | g7-art21-23-expressions | fields `... any property`, `... a financial advantage` (and `... some other advantage` on the other reading of F7.5) | fork F7.5 |
| 21(5) | Article 21(5) | encoded | g7-art21-23-expressions | `Art 21(5) the prohibition binds the foreign entity`; `Art 21(5) the statement contravenes paragraph (5)`; `Art 21(5) a foreign entity must not call itself a “charity” in connection with its Jersey activities` |  |
| 21(5)(a) | Article 21(5)(a) | encoded | g7-art21-23-expressions | `Art 21(5)(a) the foreign entity contravenes sub-paragraph (a)`; `Art 21(5)(a) a foreign entity must not refer to itself as a “charity” in connection with its activities in Jersey` |  |
| 21(5)(b) | Article 21(5)(b) | encoded | g7-art21-23-expressions | `Art 21(5)(b) the foreign entity contravenes sub-paragraph (b)`; `Art 21(5)(b) a foreign entity must not cause or permit another person to refer to it as a “charity” in connection with its activities in Jersey` |  |
| 21(6) | Article 21(6) | encoded | g7-art21-23-expressions | `Art 21(6) the prohibition binds the person`; `Art 21(6) the statement contravenes paragraph (6)`; `Art 21(6) a person must not call a foreign entity a “charity” in connection with its Jersey activities, with knowledge and intent` | forks F7.4, F7.5 |
| 21(6)(a) | Article 21(6)(a) | encoded | g7-art21-23-expressions | `Art 21(6) the prohibition binds the person` (awareness of BOTH (i) and (ii)) |  |
| 21(6)(a)(i) | Article 21(6)(a)(i) | encoded | g7-art21-23-expressions | field `that the entity is neither a Jersey entity nor an excepted foreign charity` of `Awareness of the person making a statement` |  |
| 21(6)(a)(ii) | Article 21(6)(a)(ii) | encoded | g7-art21-23-expressions | field `that the entity is not a registered charity` |  |
| 21(6)(b) | Article 21(6)(b) | encoded | g7-art21-23-expressions | `the intent is within the advantage sub-paragraph` called with `Articles 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii) reach other advantage under` |  |
| 21(6)(b)(i) | Article 21(6)(b)(i) | encoded | g7-art21-23-expressions | field `to cause another person to be misled as to the nature of the entity` |  |
| 21(6)(b)(ii) | Article 21(6)(b)(ii) | encoded | g7-art21-23-expressions | fields `... any property`, `... a financial advantage` (and `... some other advantage` on the other reading of F7.5) | fork F7.5 |
| 21(7) | Article 21(7) | encoded | g7-art21-23-expressions | `Art 21(7) paragraphs (2), (4) and (6) apply to the person making the reference`, consulted by the binding conditions of (2), (4), (6) | declaratory: TRUE for both values of its input |
| 21(8) | Article 21(8) | encoded | g7-art21-23-expressions | `Art 21(8) the States may prescribe exceptions`; input `an exception prescribed under Article 21(8) applies` | power of the States typed MAY; the Regulations are an input |
| 21(9) | Article 21(9) | encoded | g7-art21-23-expressions | `Art 21(9) the statement is an offence under paragraph (9)`; `Art 21 the penalty for the contravention`; `the penalty of imprisonment for a term of 2 years and a fine`; `Art 21(9) and 23(7) the day on which a term of imprisonment of 2 years beginning on a day ends` | penalty as data: 24 months, a fine with no maximum stated; forks F7.8, F7.4 |
| 21(10) | Article 21(10) | encoded | g7-art21-23-expressions | `Art 21(10) the statement is an offence under paragraph (10)`; `the penalty of a fine of level 3 on the standard scale` | penalty as data: no imprisonment, level 3; the amount of level 3 is not in the sources |
| 22 | Article 22 | encoded | g7-art21-23-expressions | `§§ Article 22` and the rules for its paragraphs |  |
| 22(1) | Article 22(1) | encoded | g7-art21-23-expressions | `Art 22 the entity is an excepted foreign charity`; `Art 22 the entity is an excepted foreign charity for the purpose of Article 2(10)(b)` | IP26; fork F7.12 (Article 2(10)(b)) |
| 22(2) | Article 22(2) | encoded | g7-art21-23-expressions | `Art 22(2) the entity meets the first condition` |  |
| 22(2)(a) | Article 22(2)(a) | encoded | g7-art21-23-expressions | `Art 22(2)(a) the entity is established under the law of the United Kingdom or of a prescribed jurisdiction` over `Law under which an entity is established` |  |
| 22(2)(a)(i) | Article 22(2)(a)(i) | encoded | g7-art21-23-expressions | constructor `the law of the United Kingdom or of a jurisdiction that is part of the United Kingdom` |  |
| 22(2)(a)(ii) | Article 22(2)(a)(ii) | encoded | g7-art21-23-expressions | constructor `the law of a jurisdiction, not Jersey or the United Kingdom or a part of it, that the Minister has prescribed by Order under Article 22(2)(a)(ii)`; `Art 22(2)(a)(ii) the Minister may prescribe a jurisdiction by Order` | power of the Minister typed MAY; the prescribed list is an input |
| 22(2)(b) | Article 22(2)(b) | encoded | g7-art21-23-expressions | field `entitled under that law to refer to itself there as a charity` of `Facts for the excepted foreign charity test` | an input |
| 22(3) | Article 22(3) | encoded | g7-art21-23-expressions | `Art 22(3) the entity meets the second condition` |  |
| 22(3)(a) | Article 22(3)(a) | encoded | g7-art21-23-expressions | field `managed wholly or mainly from that jurisdiction` |  |
| 22(3)(b) | Article 22(3)(b) | encoded | g7-art21-23-expressions | input `the entity is a registered charity` (IP6), negated | redundant against the opening words of 21(5) and (6) |
| 22(4) | Article 22(4) | encoded | g7-art21-23-expressions | `Art 22(4) the Minister may exempt a specified entity from the first condition`; field `specified in an Order under Article 22(4)` | power of the Minister typed MAY; the Order is an input |
| 22(5) | Article 22(5) | encoded | g7-art21-23-expressions | `Art 22(5) the States may amend the conditions` | power of the States typed MAY; the Regulations are not in the sources |
| 23 | Article 23 | encoded | g7-art21-23-expressions | `§§ Article 23` and the rules for its paragraphs |  |
| 23(1) | Article 23(1) | encoded | g7-art21-23-expressions | `Art 23(1) the prohibition binds the entity`; `Art 23(1) the statement contravenes paragraph (1)`; `Art 23(1) an entity must not call itself a “Jersey charity” unless it meets the conditions` |  |
| 23(1)(a) | Article 23(1)(a) | encoded | g7-art21-23-expressions | `Art 23(1)(a) the entity contravenes sub-paragraph (a)`; `Art 23(1)(a) an entity must not refer to itself as a “Jersey charity” unless it meets the conditions` |  |
| 23(1)(b) | Article 23(1)(b) | encoded | g7-art21-23-expressions | `Art 23(1)(b) the entity contravenes sub-paragraph (b)`; `Art 23(1)(b) an entity must not cause or permit another person to refer to it as a “Jersey charity” unless it meets the conditions` |  |
| 23(2) | Article 23(2) | encoded | g7-art21-23-expressions | `Art 23(2) the prohibition binds the person`; `Art 23(2) the statement contravenes paragraph (2)`; `Art 23(2) a person must not call an entity a “Jersey charity” unless it meets the conditions, with knowledge and intent` | forks F7.4, F7.5 |
| 23(2)(a) | Article 23(2)(a) | encoded | g7-art21-23-expressions | field `that the entity does not meet all of the conditions of Article 23(3)` of `Awareness of the person making a statement` |  |
| 23(2)(b) | Article 23(2)(b) | encoded | g7-art21-23-expressions | `the intent is within the advantage sub-paragraph` called with `Articles 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii) reach other advantage under` |  |
| 23(2)(b)(i) | Article 23(2)(b)(i) | encoded | g7-art21-23-expressions | field `to cause another person to be misled as to the nature of the entity` |  |
| 23(2)(b)(ii) | Article 23(2)(b)(ii) | encoded | g7-art21-23-expressions | fields `... any property`, `... a financial advantage` (and `... some other advantage` on the other reading of F7.5) | fork F7.5 |
| 23(3) | Article 23(3) | encoded | g7-art21-23-expressions | `Art 23(3) the entity meets all of the conditions` |  |
| 23(3)(a) | Article 23(3)(a) | encoded | g7-art21-23-expressions | input `the entity is a registered charity` (IP6) |  |
| 23(3)(b) | Article 23(3)(b) | encoded | g7-art21-23-expressions | field `is a Jersey entity` of `Entity` (IP5) |  |
| 23(3)(c) | Article 23(3)(c) | encoded | g7-art21-23-expressions | input `the entity is wholly or mainly managed or controlled in or from within Jersey` | an input (nouns request) |
| 23(4) | Article 23(4) | encoded | g7-art21-23-expressions | `Art 23(4) the States may prescribe exceptions`; input `an exception prescribed under Article 23(4) applies` | power of the States typed MAY; the Regulations are an input |
| 23(5) | Article 23(5) | encoded | g7-art21-23-expressions | `Art 23(5) paragraph (2) applies to the person making the reference` | declaratory: TRUE for both values of its input |
| 23(6) | Article 23(6) | encoded | g7-art21-23-expressions | `Art 23(6) the statement is an offence under paragraph (6)`; `Art 23 the penalty for the contravention`; `the penalty of a fine of level 3 on the standard scale` | penalty as data: no imprisonment, level 3 |
| 23(7) | Article 23(7) | encoded | g7-art21-23-expressions | `Art 23(7) the statement is an offence under paragraph (7)`; `Art 23 the penalty for the contravention`; `the penalty of imprisonment for a term of 2 years and a fine` | penalty as data: 24 months, a fine with no maximum stated; fork F7.8 |
| 24 | Article 24 | encoded | g7-art24-25-powers | `§§ Article 24` and the rules for its paragraphs |  |
| 24(1) | Article 24(1) | encoded | g7-art24-25-powers | `Art 24(1) the States may restrict the use of a relevant term in soliciting donations`; `Art 24(1) the use is one that the Regulations may restrict` | power of the States typed MAY; the Regulations are an input |
| 24(2) | Article 24(2) | encoded | g7-art24-25-powers | `Art 24(2) the term is a relevant term`; `the relevant terms named in Article 24(2)` | the related terms the Regulations specify are an input |
| 24(3) | Article 24(3) | encoded | g7-art24-25-powers | its three sub-paragraphs (each a permission of the States) |  |
| 24(3)(a) | Article 24(3)(a) | encoded | g7-art24-25-powers | `Art 24(3)(a) the Regulations may adapt provisions of Articles 21 to 23` | fork F7.13 |
| 24(3)(b) | Article 24(3)(b) | encoded | g7-art24-25-powers | `Art 24(3)(b) the Regulations may require permission to be sought from the Commissioner` | the Commissioner’s discretion to grant is an input of the Regulations |
| 24(3)(c) | Article 24(3)(c) | encoded | g7-art24-25-powers | `Art 24(3)(c) the Regulations may provide for the Commissioner to issue guidance` |  |
| 24(4) | Article 24(4) | encoded | g7-art24-25-powers | `Art 24(4) the Regulations may create an offence of contravening a restriction`; `Art 24(4) the penalty is no greater than a fine`; `Art 24 the Regulations may attach this penalty to the offence` | a cap on the content of the Regulations: no imprisonment; fork F7.13 |
| 25 | Article 25 | encoded | g7-art24-25-powers | `§§ Article 25` and the rules for its paragraphs |  |
| 25(1) | Article 25(1) | encoded | g7-art24-25-powers | `Art 25(1) the Minister may prescribe statements that a registered charity must make` | power of the Minister typed MAY; the Order is an input |
| 25(2) | Article 25(2) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a) | Article 25(2)(a) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(i) | Article 25(2)(a)(i) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(ii) | Article 25(2)(a)(ii) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(iii) | Article 25(2)(a)(iii) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(iv) | Article 25(2)(a)(iv) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(v) | Article 25(2)(a)(v) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(a)(vi) | Article 25(2)(a)(vi) | inert | g7-art24-25-powers | `the statements that an Order under Article 25(1) may require a charity to state (Article 25(2)(a))` | illustrates the content of an Order, “without prejudice to the generality of paragraph (1)”; carried as text that no rule reads |
| 25(2)(b) | Article 25(2)(b) | inert | g7-art24-25-powers | `the other provision that an Order under Article 25(1) may make (Article 25(2)(b) to (d))` | illustrative content of an Order; carried as text that no rule reads |
| 25(2)(c) | Article 25(2)(c) | inert | g7-art24-25-powers | `the other provision that an Order under Article 25(1) may make (Article 25(2)(b) to (d))` | illustrative content of an Order; carried as text that no rule reads |
| 25(2)(d) | Article 25(2)(d) | inert | g7-art24-25-powers | `the other provision that an Order under Article 25(1) may make (Article 25(2)(b) to (d))` | illustrative content of an Order; carried as text that no rule reads |
| 37 | Article 37 | encoded | g7-art37-43-final | `§§ Article 37` and the rules for its paragraphs |  |
| 37(1) | Article 37(1) | encoded | g7-art37-43-final | `Art 37(1) the person is also guilty of the offence`; `Art 37(1) the penalty of the person who is also guilty`; `the body is within Article 37(1)` | forks F7.6, F7.10 (trap T26); IP30 consumer |
| 37(1)(a) | Article 37(1)(a) | encoded | g7-art37-43-final | `the capacity fits the body` over `Capacity of a person in relation to a body under Article 37` (holds the capacity) | fork F7.10 |
| 37(1)(b) | Article 37(1)(b) | encoded | g7-art37-43-final | constructor `purports to act in the capacity` of `How a person comes within a capacity under Article 37` |  |
| 37(2) | Article 37(2) | encoded | g7-art37-43-final | `Art 37(2) the member is treated as a director of the body corporate` |  |
| 38 | Article 38 | encoded | g7-art37-43-final | `Art 38 the Minister may make further provision as to service`; `Art 38 the date on which the notice is served` | power of the Minister typed MAY; IP34; fork F7.7 |
| 39 | Article 39 | encoded | g7-art37-43-final | `§§ Article 39` and the rules for its paragraphs |  |
| 39(1) | Article 39(1) | encoded | g7-art37-43-final | `Art 39(1) the provision may be contained in the Order or Regulations`; `Art 39(1) the Minister may include ancillary provisions in an Order`; `Art 39(1) the States may include ancillary provisions in Regulations`; `Art 39 an Order under Article 2(2) may make a consequential amendment of another provision of the Law` | a limit on the content of Orders and Regulations; the opinion “necessary or expedient” is an input; fork F7.14 |
| 39(2) | Article 39(2) | encoded | g7-art37-43-final | `Art 39(2) the States may make consequential amendments of other provisions of the Law` | power of the States typed MAY; fork F7.14 |
| 40 | Article 40 | encoded | g7-art37-43-final | `§§ Article 40` and the rules for its paragraphs |  |
| 40(1) | Article 40(1) | inert | g7-art37-43-final | `Art 40(1) a rule of construction preserving the independent powers of the Attorney General, the Bailiff and the court` | rule of construction; no input or outcome of its own; carried as text |
| 40(2) | Article 40(2) | encoded | g7-art37-43-final | `Art 40(2) the States may make other saving provision` | power of the States typed MAY |
| 40(3) | Article 40(3) | encoded | g7-art37-43-final | `Art 40(3) the States may make transitional provision for the bringing into force of the Law` | power of the States typed MAY; whether it can still be exercised after 1 January 2019 is not answered |
| 41 | Article 41 | encoded | g7-art37-43-final | `§§ Article 41` and the rules for its paragraphs | changed by the brief’s ruling 4: an enabling power of the States |
| 41(1) | Article 41(1) | encoded | g7-art37-43-final | `Art 41(1) the enactment is a relevant enactment` over `Kind of enactment under Article 41` | the three kinds are named; the enactments themselves are not in the sources |
| 41(1)(a) | Article 41(1)(a) | encoded | g7-art37-43-final | constructor `the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008` of `Kind of enactment under Article 41` |  |
| 41(1)(b) | Article 41(1)(b) | encoded | g7-art37-43-final | constructor `an enactment under which the JFSC has functions` |  |
| 41(1)(c) | Article 41(1)(c) | encoded | g7-art37-43-final | constructor `an enactment relating to taxation` |  |
| 41(2) | Article 41(2) | encoded | g7-art37-43-final | `Art 41(2) the States may amend a relevant enactment to enable disclosure of information to the Commissioner` | power of the States typed MAY; the Regulations are an input |
| 42 | Article 42 | encoded | g7-art37-43-final | `§§ Article 42` and its two paragraphs |  |
| 42(a) | Article 42(a) | encoded | g7-art37-43-final | `Art 42(a) the States may amend the Trusts Law and the Foundations Law` | power of the States typed MAY; the official text reads “by reference the test itself” (no “to”) in both sources |
| 42(b) | Article 42(b) | encoded | g7-art37-43-final | `Art 42(b) the States may amend another enactment for consequential provision on references to charities` | power of the States typed MAY; not this Law |
| 43 | Article 43 | inert | g7-art37-43-final | `Art 43 the short title` | citation only; the original Article 44(1) |
| E1 | Endnotes, Table of Legislation History, row E1 | encoded | g7-commencement | `the Parts named in stage 1`; `the Articles named in stage 1, as numbered in the Table`; `the day that the Table names for` | forks F7.3, F7.11; trap T1 |
| E2 | Endnotes, Table of Legislation History, row E2 | encoded | g7-commencement | `the Parts named in stage 2`; `the Articles excepted from the Parts named in stage 2`; `the Articles named in stage 2, as numbered in the Table` | R&O.17/2018 Article 1; forks F7.1, F7.9, F7.11 |
| E3 | Endnotes, Table of Legislation History, row E3 | encoded | g7-commencement | `the stage that the Table gives to Article` (the remainder is what stages 1 and 2 leave) | R&O.17/2018 Article 2; trap T2 |
| E4 | Endnotes, Table of Legislation History, row E4 | encoded | g7-vintages | `R&O.40/2019`; `the text of the Law that took effect with R&O.40/2019` | 31 May 2019 |
| E5 | Endnotes, Table of Legislation History, row E5 | encoded | g7-vintages | `L.1/2017`; `the text of the Law that took effect with L.1/2017` | the day rests on the Table alone: the Act appointing it is not in the sources |
| E6 | Endnotes, Table of Legislation History, row E6 | encoded | g7-vintages | `L.13/2019`; `the text of the Law that took effect with L.13/2019` | R&O.136/2019 Article 1 is among the sources and confirms 1 January 2020 |
| E7 | Endnotes, Table of Legislation History, row E7 | encoded | g7-vintages | `R&O.29/2021`; `the text of the Law that took effect with R&O.29/2021` | CHANGED from the survey: the instrument is among the sources, so the text is shown, not inferred |
| E8 | Endnotes, Table of Legislation History, row E8 | encoded | g7-vintages | `R&O.28/2023`; `the text of the Law that took effect with R&O.28/2023` | made 5 April 2023, in force 7 days after; fork F7.2 |
| E9 | Endnotes, Table of Legislation History, row E9 | encoded | g7-vintages | `R&O.10/2024`; `the text of the Law that took effect with R&O.10/2024` | time of day; fork F7.1 |
| E10 | Endnotes, Table of Legislation History, row E10 | encoded | g7-vintages | `R&O.56/2025`; `the text of the Law that took effect with R&O.56/2025` | made 9 October 2025, in force 7 days after; fork F7.2 |
| E11 | Endnotes, Table of Legislation History, row E11 | encoded | g7-vintages | `R&O.102/2026`; `the text of the Law that took effect with R&O.102/2026` | made 25 September 2026, in force 7 days after; fork F7.2 |
| R1 | Endnotes, Table of Renumbered Provisions, row R1 | refused | g7-commencement | `what the original Article 41 provided is not in the sources`; `Commencement: what the original Article 41 provided` | the original Article 41 is in the remainder (in force 1 January 2019); its content is not in the sources; it stood in Part 9, whose stages now include it (`the spent original Articles that stood in Part`) |
| R2 | Endnotes, Table of Renumbered Provisions, row R2 | encoded | g7-commencement | `row R2: the original Article 42`; `Commencement: the Article as now numbered for the original Article` | fixes the stage of the present Article 41 (trap T1) |
| R3 | Endnotes, Table of Renumbered Provisions, row R3 | encoded | g7-commencement | `row R3: the original Article 43` |  |
| R4 | Endnotes, Table of Renumbered Provisions, row R4 | encoded | g7-commencement | `row R4: the original Article 44(1)` |  |
| R5 | Endnotes, Table of Renumbered Provisions, row R5 | inert | g7-commencement | `row R5: the original Article 44(2)` | spent; its effect (the stage 1 commencement) is E1; R&O.17/2018 Article 2 says that Article 44(2) brought stage 1 into force |
| R6 | Endnotes, Table of Renumbered Provisions, row R6 | inert | g7-commencement | `row R6: the original Article 44(3)` | spent; content not in the sources; nothing depends on it |
| N1 | Endnotes, Table of Endnote References, note 1 | encoded | g7-vintages | `the instruments that amend Article 1 (endnote [1])` |  |
| N2 | Endnotes, Table of Endnote References, note 2 | encoded | g7-vintages | `the instruments that amend Article 2(1) (endnote [2])` |  |
| N3 | Endnotes, Table of Endnote References, note 3 | inert | g7-vintages | `the editorial changes of endnotes [3] and [4]` | a typographical correction; no change of meaning |
| N4 | Endnotes, Table of Endnote References, note 4 | inert | g7-vintages | `the editorial changes of endnotes [3] and [4]` | a typographical correction; no change of meaning |
| N5 | Endnotes, Table of Endnote References, note 5 | encoded | g7-vintages | `the instruments that amend Schedule 1 (endnote [5])`; `Endnotes: the Dormant Bank Accounts openings of Schedule 1 are in the text of` | see E5 |

## 2. Fork register (the R4 shape)

There is one record, `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes`, declared in `g7-interpretation.l4`.
It has fourteen fields, one per fork, each `TYPICALLY` the reading taken.
A record has no update operator in L4, so the module also defines `the favoured interpretation` (the reading taken at every fork) and, for each fork, `the interpretation with the other reading of F7.n` (everything as taken except that fork).
Each public decision that depends on a fork takes the record as its LAST `GIVEN` and delegates by `CONSIDER` to one branch per reading.
The readings taken are assumed, not ruled.

Field names and constructors below are verbatim from `g7-interpretation.l4`.
"fav" is `the favoured interpretation`; "other F7.n" is `the interpretation with the other reading of F7.n`.
A test location is `file:line` of the assertion in the deposit that tells the two readings apart.

### F7.1

- **Provision.** Endnote row E9 (R&O.10/2024 Article 5: "comes into force at 9.30 a.m. on 27th February 2024"); every vintage date; trap T3.
- **Readings and the text that licenses each.** A (taken): the text of 27 February 2024 takes effect at 9.30 a.m.; a question about the day alone refuses unless both texts of the day give the same answer to the fact asked about; a question about an instant answers. B: the whole of 27 February 2024 is in the new text. License of A: the instrument states a time of day, and B would discard it. License of B: the Table names only the day.
- **Reading taken and why.** A: a refusal for the day is the honest answer where two texts are in force on one day, and every fact on which the two texts agree (Comptroller, paragraph (ba), the Dormant Bank Accounts openings) still answers.
- **Field and constructors.** `how a day on which a text takes effect at a stated time is treated` : `Treatment of a day on which a text takes effect at a stated time` = `a question about that day alone is refused` | `the whole day is in the new text`
- **Discriminating case.** The Minister on 27 February 2024: at 08:00 or 09:29:59 Jersey time it is the Chief Minister; at 09:30 or 10:00 it is the Minister for External Relations; asked of the day alone, A refuses and B answers the Minister for External Relations.
- **Tests.** g7-tests-vintages.l4:65; g7-tests-vintages.l4:105; g7-tests-vintages.l4:76; g7-tests-vintages.l4:77
- **Kind of period.** commencement (an instant within a day) — P47

### F7.2

- **Provision.** R&O.28/2023 Article 3, R&O.56/2025 Article 2, R&O.102/2026 Article 7(6): "comes into force 7 days after it is made"; endnote rows E8, E10, E11.
- **Readings and the text that licenses each.** A (taken): the day of making is left out and the seventh day after it is the first day in force. B: seven clear days are left, so the eighth day is the first day in force. License of A: made 5 April 2023, 9 October 2025 and 25 September 2026 give 12 April 2023, 16 October 2025 and 2 October 2026, which are exactly the dates the Table gives for the three Orders; B gives 13 April, 17 October and 3 October, which the Table contradicts.
- **Reading taken and why.** A: the three instruments in the sources are three independent confirmations; B stays callable because the Interpretation (Jersey) Law 1954 is not among the sources.
- **Field and constructors.** `how “7 days after it is made” is counted` : `Counting of “7 days after it is made”` = `the day of making is left out` | `seven clear days are left`
- **Discriminating case.** R&O.56/2025 made on 9 October 2025: in force on 16 October (A) or 17 October (B).
- **Tests.** g7-tests-vintages.l4:131; g7-tests-vintages.l4:135
- **Kind of period.** commencement by a number of days after making — P48

### F7.3

- **Provision.** Endnote row E1 ("Articles 32, 38, 39, 40, 42, 43 and 44") against the Table of Renumbered Provisions (rows R1 to R6); trap T1.
- **Readings and the text that licenses each.** A (taken): the numbers of the commencement Table are the ORIGINAL numbers, converted to present numbers through the renumbering. B: the numbers are read as present numbers. License of A: the Law now ends at Article 43, so the Table's "44" can only be an original number. License of B: the Table sits at the foot of the consolidated text.
- **Reading taken and why.** A: B names a non-existent Article 44 and leaves the present Article 41 (sharing of information, the original 42) to the remainder.
- **Field and constructors.** `the numbering the commencement table speaks in` : `Numbering that the commencement table speaks in` = `the table is in the original numbers` | `the table is in the present numbers`
- **Discriminating case.** Is the present Article 41 in force on 1 January 2018? Yes under A (it was the original 42, in stage 1, 21 November 2014); no under B (the remainder, 1 January 2019).
- **Tests.** g7-tests-commencement.l4:187; g7-tests-commencement.l4:188
- **Kind of period.** the numbering of the Table (not a period)

### F7.4

- **Provision.** Articles 21(1) with 21(2), 21(3) with 21(4), 21(5) with 21(6), 23(1) with 23(2), 21(7), 23(5), 21(9), 21(10), 23(6), 23(7); trap T13.
- **Readings and the text that licenses each.** A (taken): the strict offence and the knowing offence are both made out by one statement and each carries its own penalty. B: the knowing offence displaces the strict one. License of A: 21(7) and 23(5) say the knowing paragraphs apply to the entity itself, and nothing makes either offence exclusive of the other. License of B: one act, one wrong.
- **Reading taken and why.** A: the Law creates two offences with different elements and different penalties and says nothing about election between them.
- **Field and constructors.** `how the strict and the knowing offences combine for one act` : `How the strict and the knowing offences of Articles 21 and 23 combine for one act` = `both offences are made out` | `the knowing offence displaces the strict one`
- **Discriminating case.** An unregistered entity tells a donor, knowing it is untrue and meaning to induce a gift, that it is registered with the Commissioner (scenario 05): contraventions of 21(1) and 21(2) with the penalties of 21(10) and 21(9) (A); 21(2) only (B).
- **Tests.** g7-tests-expressions.l4:602; g7-tests-expressions.l4:605
- **Kind of period.** none

### F7.5

- **Provision.** Article 21(2)(b)(ii) ("any property or financial or other advantage") against 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii) ("any property or financial advantage").
- **Readings and the text that licenses each.** A (taken): the difference is kept as printed. B: "or other advantage" is carried to the other three. License of A: the words are in one paragraph and not in three that are otherwise parallel, and an encoding that harmonises them substitutes the encoder for the drafter. License of B: the four paragraphs are plainly parallel and the omission may be an accident.
- **Reading taken and why.** A: isomorphism; B is callable.
- **Field and constructors.** `the wording of the advantage limb of the knowing offences` : `Wording of the advantage limb of the knowing offences` = `the wording differs as printed` | `the wording is harmonised`
- **Discriminating case.** A person calls an unregistered Jersey entity a "charity" meaning to induce volunteers to give their time (scenario 11): not an offence under 21(4) as printed; an offence if harmonised. (The same intent against a claim of being "registered by the Commissioner" is an offence under 21(2) on either reading: scenario 12.)
- **Tests.** g7-tests-expressions.l4:110; g7-tests-expressions.l4:119
- **Kind of period.** none

### F7.6

- **Provision.** Article 37(1) ("a limited liability partnership, a separate limited partnership or a body corporate") against Article 2(1)(a) and (i) and 2(3) (trustees of a trust, unincorporated bodies are entities); trap T26.
- **Readings and the text that licenses each.** A (taken): only those three kinds of body. B: also an unincorporated association and the trustees of a trust. License of A: the text names three kinds. License of B: those are entities that can offend, for instance under 21(3).
- **Reading taken and why.** A: literal.
- **Field and constructors.** `the bodies within Article 37(1)` : `Bodies within Article 37(1)` = `only partnerships and bodies corporate` | `also unincorporated associations and trustees`
- **Discriminating case.** A committee member of an unincorporated association who connived in its 21(3) offence: not within 37(1) as written (A); within it (B).
- **Tests.** g7-tests-powers-final.l4:142; g7-tests-powers-final.l4:137
- **Kind of period.** none

### F7.7

- **Provision.** Article 38 (the Minister may by Order make further provision as to service); read in Articles 8(3)(k), 17(4), 26, 27, 33(3); integration point IP34.
- **Readings and the text that licenses each.** A (taken): the date of service is the date the notice is received by the person served. B: the date it is sent. A third source is an Order under Article 38, which the encoding takes as an input and lets govern. License of A: service is a notion of the notice reaching the person. License of B: the Law speaks of "giving" in 17(4).
- **Reading taken and why.** A: assumed, not ruled; an Order under Article 38 overrides both.
- **Field and constructors.** `the date on which a notice is served` : `Reading of the date on which a notice is served` = `the date of receipt` | `the date of sending`
- **Discriminating case.** Sent on 1 June 2026 and received on 3 June 2026: served on the 3rd (A) or the 1st (B); a notice not yet received is not served under A (refusal) and was served when sent under B.
- **Tests.** g7-tests-powers-final.l4:165; g7-tests-powers-final.l4:166
- **Kind of period.** none (the date of an event, not a period)

### F7.8

- **Provision.** Articles 21(9) and 23(7): "imprisonment for a term of 2 years"; the same fork is F6.16, F8.8 and F9.13 of the other groups (IP35).
- **Readings and the text that licenses each.** A (taken): calendar months; 2 years is 24 months, and a term beginning on a day ends on that day plus 24 months (clamped at the end of a month by `add months`). B: days; 2 years is 730 days. License of A: a year is a calendar year. License of B: the Law gives no calendar.
- **Reading taken and why.** A: the shared default of domain.l4. The `Penalty provided` of domain.l4 stores months (24), so B's 730 days cannot be carried in it; the unit changes the length of a term measured in days, not the stored number.
- **Field and constructors.** `the unit of a term of imprisonment` : `Unit of a term of imprisonment` (domain.l4) = `calendar months` | `days`
- **Discriminating case.** A sentence of 731 days beginning on 1 March 2027: within the maximum under A (2029-03-01 is 731 days later because 2028 has a 29 February); beyond it under B. A sentence of 730 days beginning on 29 February 2028: within it under A (the second anniversary is clamped to 28 February 2030, 730 days).
- **Tests.** g7-tests-expressions.l4:788; g7-tests-expressions.l4:802
- **Kind of period.** a sentence (a term of imprisonment) — P22; the month-end clamp is tested at 29 February 2028

### F7.9

- **Provision.** Endnote row E2 and R&O.17/2018 Article 1: "Part 8 (other than Article 32), Article 37" in stage 2 against the Parts 8 and 9 as units.
- **Readings and the text that licenses each.** A (taken): a Part brought into force in more than one stage (Part 8: Article 32 on 21 November 2014 and Articles 33 to 36 on 1 May 2018; Part 9: Articles 38 to 43 on 21 November 2014, Article 37 on 1 May 2018 and the spent original Article 41 on 1 January 2019) is in force when ALL the Articles it held are, the spent original Articles included. B: when ANY is. License of A: a Part is not in force while part of it is not. License of B: the first Article's commencement is the Part's first moment in force.
- **Reading taken and why.** A: the question "is Part 8 in force" is only a question about the whole. Both readings are callable, and the stage of each Article is exact on either.
- **Field and constructors.** `how a Part brought into force in two stages is treated` : `Treatment of a Part brought into force in two stages` = `in force when all its Articles are` | `in force when any of its Articles is`
- **Discriminating case.** Is Part 8 in force on 1 June 2015? No (A); yes (B), because Article 32 is. Is Part 9 in force on 1 June 2018? No (A: the original Article 41 is not in force until 1 January 2019); yes (B).
- **Tests.** g7-tests-commencement.l4:338; g7-tests-commencement.l4:339; g7-tests-commencement.l4:344; g7-tests-commencement.l4:347
- **Kind of period.** none (a question about a unit, not a period)

### F7.10

- **Provision.** Article 37(1)(a): "a person who is a partner of the partnership, or director, governor, secretary or other similar officer of the body corporate".
- **Readings and the text that licenses each.** A (taken): the capacities are paired with the bodies as the sentence pairs them (a partner with a partnership; a director, governor, secretary or similar officer, and by 37(2) a member of a member-managed body corporate, with a body corporate). B: any listed capacity for any body within 37(1). License of A: the sentence. License of B: a limited liability partnership may itself be a body corporate in Jersey law (not among the sources), in which case its directors would be officers of a body corporate.
- **Reading taken and why.** A: literal.
- **Field and constructors.** `how capacity is paired with the kind of body in Article 37(1)` : `Pairing of a capacity with the kind of body in Article 37(1)` = `capacity as printed for each kind of body` | `any listed capacity for any body`
- **Discriminating case.** A director of a limited liability partnership who connived: not within 37(1)(a) (A); within it (B).
- **Tests.** g7-tests-powers-final.l4:124; g7-tests-powers-final.l4:149
- **Kind of period.** none

### F7.11

- **Provision.** Every date of the Table of Legislation History; R&O.17/2018 Article 1 ("come into force on 1st May 2018") and Article 2.
- **Readings and the text that licenses each.** A (taken): the day named is the first day in force. B: the first day in force is the day after the named day. License of A: R&O.17/2018 says "come into force on"; and the three Orders that come into force "7 days after it is made" reach the Table's dates with the day named as the first day in force. License of B: none in the sources; kept because the brief asks for the counting convention of every period.
- **Reading taken and why.** A: the sources fix it. F7.11 moves only a day that is NAMED; the three Orders that compute their own day (F7.2) and the 9.30 a.m. of R&O.10/2024 are not moved.
- **Field and constructors.** `how the day named as the day of commencement is counted` : `Counting of the day named as the day of commencement` = `the named day is the first day in force` | `the day after the named day is the first day in force`
- **Discriminating case.** Is Part 1 in force on 21 November 2014? Yes (A); no (B).
- **Tests.** g7-tests-commencement.l4:442; g7-tests-commencement.l4:205
- **Kind of period.** commencement by a named day — P46, P47

### F7.12

- **Provision.** Article 22(1) ("For the purpose of Article 21, an entity is an excepted foreign charity if ...") against Article 2(10)(b) ("an excepted foreign charity (within the meaning of Article 22)").
- **Readings and the text that licenses each.** A (taken): Article 22 defines the term wherever the Law uses it. B: it defines it for Article 21 only, so Article 2(10)(b) has no definition to apply. License of A: 2(10)(b) cites Article 22 for its meaning. License of B: 22(1) says in terms "For the purpose of Article 21".
- **Reading taken and why.** A: the citation shows the drafter's intent; B refuses.
- **Field and constructors.** `whether Article 22 defines an excepted foreign charity outside Article 21` : `Reach of the definition of an excepted foreign charity in Article 22` = `Article 22 defines the term wherever the Law uses it` | `Article 22 defines the term for Article 21 only`
- **Discriminating case.** A conviction on 1 July 2018 of an offence in relation to a UK charity managed from the UK (misconduct under 2(10)(b)): answered under A (and Article 22 was not yet in force: trap T30); refused under B.
- **Tests.** g7-tests-expressions.l4:871; g7-tests-expressions.l4:874
- **Kind of period.** none

### F7.13

- **Provision.** Article 24(3)(a) ("may make the provision by adapting any provisions of Articles 21 to 23") against Article 24(4) ("an offence carrying a penalty no greater than a fine").
- **Readings and the text that licenses each.** A (taken): the cap of 24(4) applies to every offence of the Regulations, so an offence adapted from 21(9) cannot keep its imprisonment. B: an offence adapted from Articles 21 to 23 may keep the penalty of the provision adapted. License of A: 24(4) is a cap on "the Regulations" offence. License of B: 24(3)(a) allows adapting "any provisions", whose offences carry imprisonment.
- **Reading taken and why.** A: a specific cap beats a general permission.
- **Field and constructors.** `whether adapting Articles 21 to 23 under Article 24(3)(a) can carry their imprisonment` : `Reach of the cap of Article 24(4) on a penalty adapted from Articles 21 to 23` = `the cap of Article 24(4) applies to every offence of the Regulations` | `the cap of Article 24(4) does not apply to an offence adapted from Articles 21 to 23`
- **Discriminating case.** Regulations that adapt 21(9) wholesale for "charitable": imprisonment for 24 months is not allowed (A); allowed (B).
- **Tests.** g7-tests-powers-final.l4:80; g7-tests-powers-final.l4:85
- **Kind of period.** none

### F7.14

- **Provision.** Article 2(2) (the Minister may by Order add sub-paragraphs to Article 2(1)) against Article 39(1) ("other than an amendment of this Law") and Article 39(2) ("A power ... to amend, by Regulations").
- **Readings and the text that licenses each.** A (taken): an Order under 2(2) cannot make consequential amendments of other provisions of the Law; only Regulations can. B: the power to add sub-paragraphs carries the consequential amendments. License of A: 39(1) excludes an amendment of the Law from an Order's ancillary provisions and 39(2) speaks of Regulations; and R&O.56/2025 added paragraph (ba) and changed nothing else (Articles 2(3)(a), 2(5) and 8(3)(a)(ii) do not mention it: trap T5). License of B: a sub-paragraph that no other provision reaches is a trap for the Law.
- **Reading taken and why.** A: the one instrument in the sources made under 2(2) did exactly that.
- **Field and constructors.** `whether an Order under Article 2(2) can make consequential amendments of other provisions of the Law` : `Consequential amendments of this Law by an Order under Article 2(2)` = `only Regulations can make consequential amendments of this Law` | `an Order under Article 2(2) can make them too`
- **Discriminating case.** An Order under 2(2) adds a sub-paragraph and also amends 8(3)(a)(ii): not allowed (A); allowed (B).
- **Tests.** g7-tests-powers-final.l4:187; g7-tests-powers-final.l4:188
- **Kind of period.** none

### The kinds of period of the scope, one fork each

| period (PLAN) | words | kind | fork |
| --- | --- | --- | --- |
| P22 | "imprisonment for a term of 2 years" (21(9), 23(7)) | a sentence | F7.8 (unit; month-end clamp tested at 29 February 2028) |
| P46 | stage dates of row E1 to E3; "1st May 2018" and "1st January 2019" (R&O.17/2018) | commencement by a named day | F7.11 (is the named day inside), F7.3 (which numbering) |
| P47 | the eight dates of rows E4 to E11 and the nine texts | commencement (day against instant) | F7.1 (the 9.30 a.m.), F7.11 |
| P48 | "comes into force 7 days after it is made" (three Orders) | commencement by a number of days after making | F7.2 |

Counting backward ("preceding") does not occur in the scope.
A month or a year is added at the end of a month only in F7.8, through `add months`, which clamps (tested at 29 February 2028); no hand-rolled month arithmetic is used.
Days of rest and holidays are not modelled (brief).

### Readings considered and not forked

T25: a body that is both a Jersey entity and an excepted foreign charity is caught by 21(3) and (4) and not by (5) and (6); the text is clear and nothing discriminates (scenario 26, 27).
T2: the remainder of the staged commencement is Part 6 and the original Article 41 (R&O.17/2018 Article 2); the brief's wording is wrong, and the correction is the one finding of g7-tests-red.l4's second group.
The awareness of 21(4)(a) and 21(6)(a) is read as covering BOTH limbs (i) and (ii) together (a person aware of only one is outside the paragraph); the text ("the entity (i) ..., and (ii) ...") does not admit the other reading, and scenarios 37 to 43 test it.
The mental elements "knows, suspects or has reasonable grounds to suspect" are alternatives; any one suffices (scenarios 44 to 47).

## 3. Answer table (headline scenarios, with the Article cited)

Every row is an assertion in a `g7-tests-*` module; the readings are those taken unless a column says otherwise.

### Commencement and the text of the Law

| question | answer | cited |
| --- | --- | --- |
| Part 1 in force on 2014-11-20, 2014-11-21 | no, yes | Table of Legislation History, row L.41/2014, stage 1 |
| Part 4 in force on 2018-04-30, 2018-05-01 | no, yes | same, stage 2; R&O.17/2018 Article 1 |
| Part 6 (and Articles 21 to 25) in force on 2018-12-31, 2019-01-01 | no, yes | same, remainder; R&O.17/2018 Article 2 |
| Article 37 in force on 2018-04-30, 2018-05-01 | no, yes | stage 2: "Article 37" |
| Article 32 in force on 2014-11-20, 2014-11-21 | no, yes | stage 1: "Article 32"; excepted from stage 2 ("Part 8 (other than Article 32)") |
| present Article 41 on 2018-01-01 | in force (it was the original 42, stage 1) | Table of Renumbered Provisions R2; fork F7.3 |
| original Article 41 on 2018-12-31, 2019-01-01 | no, yes (the remainder) | R1; R&O.17/2018 Article 2; what it provided is not in the sources |
| present Article 44; original Article 45; Schedule 3 | a refusal: no such unit |  |
| Part 8 on 2015-06-01 | not in force (A: all its Articles); in force on the other reading (F7.9) | Article 32 is stage 1, Articles 33 to 36 stage 2 |
| the stages of Part 9 | stage 1, stage 2, stage 3 (Articles 38 to 43 in stage 1, Article 37 in stage 2, the spent original Article 41 in stage 3) | Table of Legislation History, row L.41/2014; Table of Renumbered Provisions R1; independent testing D1 |
| Part 9 on 2018-05-01, 2018-06-01, 2018-12-31, 2019-01-01 | not in force, not in force, not in force, in force (A: all the Articles it held); in force on all four days on the other reading (F7.9) | the original Article 41 is in the remainder, R&O.17/2018 Article 2 |
| the version of the text on 2018-12-31 | `before the first consolidated version` | the nine versions begin on 1 January 2019 |
| the version of the text on 2019-01-01, 2019-05-31, 2019-12-16, 2020-01-01, 2021-03-02, 2023-04-12, 2025-10-16, 2026-10-02 | the text of that date | Table of Legislation History |
| the version of the text on 2024-02-26, 2024-02-28 | the text of 12 April 2023, the text of 27 February 2024 | R&O.10/2024 |
| the version of the text on 2024-02-27 | a refusal (two texts); at 08:00 and 09:29:59 Jersey time the text of 12 April 2023, at 09:30 and 10:00 the text of 27 February 2024 | R&O.10/2024 Article 5; fork F7.1 |
| the Minister (Article 1) from 2019-01-01 to 2019-05-30 | the Chief Minister (INFERRED from R&O.40/2019 Schedule 2 paragraph 1(e)) | endnote [1] |
| the Minister from 2019-05-31 | the Minister for External Relations | R&O.40/2019 |
| the Minister from 2021-03-02 | the Minister for External Relations and Financial Services | R&O.29/2021 Article 6(1), Schedule 2 paragraph 1(e) |
| the Minister from 2023-04-12 | the Chief Minister | R&O.28/2023 Schedule 2 paragraph 1(4) |
| the Minister from 2024-02-27 09:30 | the Minister for External Relations | R&O.10/2024 Schedule 4 paragraph 1 |
| the Minister from 2026-10-02 | the Chief Minister | R&O.102/2026 Article 1, Article 7(6) |
| the Comptroller (Article 1) before 2020-01-01, from 2020-01-01 | the Income Tax (Jersey) Law 1961, the Revenue Administration (Jersey) Law 2019 | L.13/2019 Schedule 3 paragraph 1; R&O.136/2019 Article 1 |
| paragraph (ba) of Article 2(1) on 2025-10-15, 2025-10-16 | absent, present | R&O.56/2025; Article 2(2) |
| the two "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" openings of Schedule 1 on 2019-12-15, 2019-12-16 | absent, present | L.1/2017 Article 30(3); the day rests on the Table alone |
| an Order made on 5 April 2023, 9 October 2025, 25 September 2026 that comes into force 7 days after it is made | 12 April 2023, 16 October 2025, 2 October 2026 | R&O.28/2023 Article 3; R&O.56/2025 Article 2; R&O.102/2026 Article 7(6) |

### Articles 21 to 25

| statement | contraventions made out | penalty (data) | cited |
| --- | --- | --- | --- |
| an unregistered Jersey entity says of itself that it is registered by the Commissioner (no mental element) | 21(1) | a fine of level 3 on the standard scale | 21(1), 21(10) |
| the same, knowing it is untrue and meaning to induce a gift (scenario 05) | 21(1) and 21(2) (both) | level 3 fine; AND 24 months and a fine with no maximum stated | 21(1), 21(2), 21(7), 21(9), 21(10); fork F7.4 |
| a third person, suspecting, and meaning to mislead, says the entity is registered | 21(2) | 24 months and a fine with no maximum stated | 21(2), 21(9) |
| an unregistered Jersey entity calls itself a "charity" | 21(3) | level 3 | 21(3), 21(10) |
| a person aware that it is a Jersey entity and not registered calls it a "charity" meaning to obtain a financial advantage | 21(4) | 24 months and a fine | 21(4), 21(9) |
| a person calls an unregistered Jersey entity a "charity" to induce volunteers to give their time | none as printed (21(4) if harmonised) |  | 21(4)(b)(ii) against 21(2)(b)(ii); fork F7.5 |
| an unregistered foreign entity (not an excepted foreign charity) calls itself a "charity" in connection with its activities in Jersey | 21(5) | level 3 | 21(5), 21(10) |
| the same, outside Jersey activities | none |  | 21(5)(a) ("in connection with any of its activities in Jersey") |
| an excepted foreign charity calls itself a "charity" in Jersey | none |  | 21(5), 21(6), 22 |
| a Jersey entity that is also an excepted foreign charity calls itself a "charity" | 21(3) | level 3 | 21(3); trap T25 |
| an unregistered Jersey entity calls itself a "Jersey charity" | 23(1) | level 3 | 23(1), 23(6) |
| a registered Jersey entity managed from outside Jersey calls itself a "Jersey charity" | 23(1) | level 3 | 23(3)(c), 23(1) |
| a registered Jersey entity managed from Jersey calls itself a "Jersey charity" | none |  | 23(3) |
| an exception prescribed by Regulations under 21(8) (or 23(4)) applies | none |  | 21(8), 23(4); the Regulations are an input |
| a UK charity, entitled to call itself a charity there, managed from the UK and not registered | an excepted foreign charity (true) |  | 22(1) to (3) |
| a sentence of 731 days from 2027-03-01 | within the 2 years (24 calendar months); beyond it if the unit is days |  | 21(9), 23(7); fork F7.8 |
| a relevant term used by a registered charity | outside the power of 24(1) |  | 24(1), 24(2) |
| Regulations that attach imprisonment to an offence | not within 24(4) |  | 24(4); fork F7.13 |

### Article 37 and Article 38

| question | answer | cited |
| --- | --- | --- |
| a partner of a limited liability partnership or of a separate limited partnership whose consent or connivance is proved | also guilty, with the penalty provided for the offence | 37(1)(a) |
| a director, governor, secretary or similar officer of a body corporate, or one who purports to act as such, likewise | also guilty | 37(1)(a), (b) |
| a member of a body corporate managed by its members, acting in its management | treated as a director | 37(2) |
| a committee member of an unincorporated association; the trustees of a trust | not within 37(1) as written (F7.6) | 37(1); trap T26 |
| a notice sent 2026-06-01 and received 2026-06-03, no Order | served 2026-06-03 (received); 2026-06-01 if sent (F7.7) | 38 |
| an Order under Article 38 fixes a date | that date governs | 38 |

## 4. Nouns requests for the INTEGRATOR

1. `Legal actor` has no constructor for the entity that is the subject of a statement, or for a person who is not that entity; group G7 defines the local `Party to the prohibitions on expressions` (`the entity referred to`, `a person other than the entity`).
Request: add `an entity that is not a registered charity` or move the local type to domain.l4 if another group needs it.
The constructor is NOT named `the entity`, because that is the standard name of the `Entity` input (IP5) and a constructor of that name hides the input.
2. `Enactment that defines the Comptroller` (`the Income Tax (Jersey) Law 1961`, `the Revenue Administration (Jersey) Law 2019`) is local to `g7-vintages.l4`.
PLAN gave G1 a type `Law defining the Comptroller` for the same fact; the integrator should keep one.
3. `Stage of commencement`, `How an instrument comes into force`, `Amending instrument`, `Text of the Law` are local to `g7-commencement.l4` and `g7-vintages.l4` and need no move unless another group reads them.
4. A standard input for Article 23(3)(c) is missing from PLAN section (c): `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN.
G7 takes it as a plain `GIVEN` under that name.
5. The statement-level facts of Articles 21 and 23 (`Statement about an entity under Articles 21 to 23`, `Awareness of the person making a statement`, `Intent of the person making a statement`, `What is said of an entity`) are local to `g7-art21-23-expressions.l4`.
6. `Penalty provided` stores a term of imprisonment in months (24).
A term measured in days (F7.8 reading B) cannot be carried in it; G7 therefore carries the days in a function (`Art 21(9) and 23(7) the day on which a term of imprisonment of 2 years beginning on a day ends`) and keeps 24 months in the record on either reading.
If the integrator wants the record to follow the unit, `Penalty provided` needs a unit field.
7. `Contravention of Article 21 or Article 23` (the eight paragraphs) is local to `g7-art21-23-expressions.l4`; it is the argument of the unified penalty export (IP30) and is probably worth moving to domain.l4 for Article 37's wiring.

## 5. Standard inputs consumed and functions exported

### Inputs by their standard names

`the entity` : `Entity` (IP5), reading its fields `is a Jersey entity` and `kinds of entity` (an entity is a body whose `kinds of entity` is not empty: Articles 21 and 23 do not reach any other body).
`the entity is a registered charity` : BOOLEAN (IP6), produced by G1.
`the entity is an excepted foreign charity` : BOOLEAN (IP26), PRODUCED here by `Art 22 the entity is an excepted foreign charity`.
`the penalty provided for the offence` : `Penalty provided` (IP30), consumed by `Art 37(1) the penalty of the person who is also guilty`; produced here by `Art 21 and 23 the penalty for the contravention`.
`the day` (IP1), `the vintage of the text` (IP2) and `the unit of the Law` (IP4) are the GIVEN names of the temporal exports below.
`the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN is a new input (nouns request 4).

### How to call them

The record is passed as the LAST argument of every function that takes it (the pattern in `pattern-r4.l4` passes it first; group G7 passes it last, as PLAN section (b)'s export table lists it).
The value to pass for the readings taken is `the favoured interpretation` of `g7-interpretation.l4`.
For integration point IP35 (one `Unit of a term of imprisonment` for G6, G7, G8 and G9) call `the favoured interpretation with the unit of a term of imprisonment` with the shared unit.
Functions of an instant (`...at`) take a `DATETIME`; ordering of instants is by `DATETIME_SERIAL`.
The dates of the Law are Jersey local time, taken as the zone `Europe/Jersey` (assumed, not ruled).

Differences from PLAN's export table, all deliberate:
(a) Every temporal function takes the interpretation (F7.1, F7.2, F7.3, F7.9, F7.11 are readings).
(b) `Art 21(2) the statement contravenes paragraph (2)` takes no interpretation: F7.5 does not touch paragraph (2) (it is the paragraph that already says "or other advantage"), and F7.4 is carried only by the list functions `Art 21 and 23: the contraventions made out by the statement` and `Art 21 and 23: the penalties for the statement`.
(c) `Art 38 the date on which the notice is served` takes, besides the dates sent and received, `the date fixed by an Order under Article 38` (a `MAYBE DATE`; the Order's content is an input).
(d) `Endnotes: the vintage of the text on` answers `before the first consolidated version` for a day before 2019-01-01 and refuses on 2024-02-27 (reading taken).
(e) IP3: `Endnotes: the office that the definition of “Minister” names under the text of` duplicates G1's `Art 1 the Minister under the text of`; the integrator should assert that the two agree for all nine vintages and for `before the first consolidated version` (both refuse).
(f) The same holds for the Comptroller (G1), paragraph (ba) (G1) and the Dormant Bank Accounts openings (G9): G7 answers them from the amending instruments; G1 and G9 may answer from their own inputs; the integrator asserts agreement.

### Exports (exact names, in the order of their GIVEN)

Every export carries a sentence that says what question it answers, and every `GIVEN` of every export has a `@desc` (checked mechanically: 79 exports, 0 `GIVEN` without `@desc`).

| module | export (exact name) | inputs, in order | gives |
| --- | --- | --- | --- |
| g7-art21-23-expressions | `Art 21(1) the statement contravenes paragraph (1)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(1) an unregistered entity must not say it is registered by the Commissioner` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(2) the statement contravenes paragraph (2)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(2) a person must not say that an unregistered entity is registered, with knowledge and intent` | referrer : `Party to the prohibitions on expressions`; `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(3) the statement contravenes paragraph (3)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(3) a Jersey entity that is not registered must not call itself a “charity”` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(4) the statement contravenes paragraph (4)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(4) a person must not call an unregistered Jersey entity a “charity”, with knowledge and intent` | referrer : `Party to the prohibitions on expressions`; `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(5) the statement contravenes paragraph (5)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(5) a foreign entity must not call itself a “charity” in connection with its Jersey activities` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(6) the statement contravenes paragraph (6)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(6) a person must not call a foreign entity a “charity” in connection with its Jersey activities, with knowledge and intent` | referrer : `Party to the prohibitions on expressions`; `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 21(8) the States may prescribe exceptions` | none | DEONTIC `Legal actor` `Power exercised under Articles 21 to 23` |
| g7-art21-23-expressions | `Art 21 and 23 the penalty for the contravention` | contravention : `Contravention of Article 21 or Article 23` | `Penalty provided` |
| g7-art21-23-expressions | `Art 21 the penalty for the contravention` | contravention : `Contravention of Article 21 or Article 23` | `Penalty provided` |
| g7-art21-23-expressions | `Art 21(9) the statement is an offence under paragraph (9)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 21(10) the statement is an offence under paragraph (10)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 22(4) the Minister may exempt a specified entity from the first condition` | none | DEONTIC `Legal actor` `Power exercised under Articles 21 to 23` |
| g7-art21-23-expressions | `Art 22(5) the States may amend the conditions` | none | DEONTIC `Legal actor` `Power exercised under Articles 21 to 23` |
| g7-art21-23-expressions | `Art 22 the entity is an excepted foreign charity` | facts : `Facts for the excepted foreign charity test`; `the entity is a registered charity` : BOOLEAN | BOOLEAN |
| g7-art21-23-expressions | `Art 22 the entity is an excepted foreign charity for the purpose of Article 2(10)(b)` | facts : `Facts for the excepted foreign charity test`; `the entity is a registered charity` : BOOLEAN; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 23(3) the entity meets all of the conditions` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN | BOOLEAN |
| g7-art21-23-expressions | `Art 23(1) the statement contravenes paragraph (1)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 23(1) an entity must not call itself a “Jersey charity” unless it meets the conditions` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 23(2) the statement contravenes paragraph (2)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 23(2) a person must not call an entity a “Jersey charity” unless it meets the conditions, with knowledge and intent` | referrer : `Party to the prohibitions on expressions`; `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DEONTIC (party, act of referring to an entity) |
| g7-art21-23-expressions | `Art 23(4) the States may prescribe exceptions` | none | DEONTIC `Legal actor` `Power exercised under Articles 21 to 23` |
| g7-art21-23-expressions | `Art 23(6) the statement is an offence under paragraph (6)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | BOOLEAN |
| g7-art21-23-expressions | `Art 23(7) the statement is an offence under paragraph (7)` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art21-23-expressions | `Art 23 the penalty for the contravention` | contravention : `Contravention of Article 21 or Article 23` | `Penalty provided` |
| g7-art21-23-expressions | `Art 21 and 23: the contraventions made out by the statement` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Contravention of Article 21 or Article 23` |
| g7-art21-23-expressions | `Art 21 and 23: the penalties for the statement` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; `the entity is an excepted foreign charity` : BOOLEAN; `the entity is wholly or mainly managed or controlled in or from within Jersey` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Penalty provided` |
| g7-art21-23-expressions | `Art 21(9) and 23(7) the day on which a term of imprisonment of 2 years beginning on a day ends` | start : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DATE |
| g7-art21-23-expressions | `Art 21(9) and 23(7) a sentence of a number of days beginning on a day is within the maximum` | days : NUMBER; start : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art24-25-powers | `Art 24(1) the States may restrict the use of a relevant term in soliciting donations` | none | DEONTIC `Legal actor` `Power exercised under Articles 24 and 25` |
| g7-art24-25-powers | `Art 24(2) the term is a relevant term` | term : STRING; `terms specified as relevant terms in the Regulations` : LIST OF STRING | BOOLEAN |
| g7-art24-25-powers | `Art 24(1) the use is one that the Regulations may restrict` | use : `Use of a relevant term under Article 24`; `terms specified as relevant terms in the Regulations` : LIST OF STRING | BOOLEAN |
| g7-art24-25-powers | `Art 24(4) the penalty is no greater than a fine` | penalty : `Penalty provided` | BOOLEAN |
| g7-art24-25-powers | `Art 24 the Regulations may attach this penalty to the offence` | penalty : `Penalty provided`; `the offence is adapted from a provision of Articles 21 to 23` : BOOLEAN; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art24-25-powers | `Art 25(1) the Minister may prescribe statements that a registered charity must make` | none | DEONTIC `Legal actor` `Power exercised under Articles 24 and 25` |
| g7-art37-43-final | `Art 37(2) the member is treated as a director of the body corporate` | facts : `Facts for Article 37` | BOOLEAN |
| g7-art37-43-final | `Art 37(1) the person is also guilty of the offence` | facts : `Facts for Article 37`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art37-43-final | `Art 37(1) the penalty of the person who is also guilty` | facts : `Facts for Article 37`; `the penalty provided for the offence` : `Penalty provided`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | MAYBE `Penalty provided` |
| g7-art37-43-final | `Art 38 the Minister may make further provision as to service` | none | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 38 the date on which the notice is served` | `the date on which the notice was sent` : DATE; `the date on which the notice was received` : MAYBE DATE; `the date fixed by an Order under Article 38` : MAYBE DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DATE |
| g7-art37-43-final | `Art 39(1) the provision may be contained in the Order or Regulations` | kind : `Kind of ancillary provision under Article 39`; `it appears to be necessary or expedient for the purposes of the Order or Regulations` : BOOLEAN | BOOLEAN |
| g7-art37-43-final | `Art 39(2) the States may make consequential amendments of other provisions of the Law` | `it appears to the States to be necessary or expedient` : BOOLEAN | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 39 an Order under Article 2(2) may make a consequential amendment of another provision of the Law` | interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-art37-43-final | `Art 40(2) the States may make other saving provision` | `it appears to the States to be necessary or expedient` : BOOLEAN | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 40(3) the States may make transitional provision for the bringing into force of the Law` | `it appears to the States to be necessary or expedient` : BOOLEAN | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 41(1) the enactment is a relevant enactment` | enactment : `Kind of enactment under Article 41` | BOOLEAN |
| g7-art37-43-final | `Art 41(2) the States may amend a relevant enactment to enable disclosure of information to the Commissioner` | enactment : `Kind of enactment under Article 41`; `the States consider the provision necessary or expedient` : BOOLEAN | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 42(a) the States may amend the Trusts Law and the Foundations Law` | none | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-art37-43-final | `Art 42(b) the States may amend another enactment for consequential provision on references to charities` | `the enactment is the Charities (Jersey) Law 2014 itself` : BOOLEAN; `the States consider the provision necessary or expedient` : BOOLEAN | DEONTIC `Legal actor` `Power exercised under Articles 38 to 42` |
| g7-commencement | `Commencement: what the original Article 41 provided` | none | STRING |
| g7-commencement | `Commencement: the original provision as now numbered` | original : STRING | `What became of an original provision` |
| g7-commencement | `Commencement: the Article as now numbered for the original Article` | original : NUMBER | MAYBE NUMBER |
| g7-commencement | `Commencement: the stages in which the unit was brought into force` | `the unit of the Law` : `Unit of the Law`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Stage of commencement` |
| g7-commencement | `Commencement: the stage in which the unit was brought into force` | `the unit of the Law` : `Unit of the Law`; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Stage of commencement` |
| g7-commencement | `Commencement: the unit of the Law is in force on` | `the unit of the Law` : `Unit of the Law`; `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-commencement | `Commencement: the unit of the Law is in force at` | `the unit of the Law` : `Unit of the Law`; `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-vintages | `Endnotes: the day an instrument made on a day comes into force 7 days after` | made : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | DATE |
| g7-vintages | `Endnotes: the vintage of the text at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Vintage of the text` |
| g7-vintages | `Endnotes: the texts in force at some time on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Vintage of the text` |
| g7-vintages | `Endnotes: the vintage of the text on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Vintage of the text` |
| g7-vintages | `Endnotes: the office that the definition of “Minister” names under the text of` | `the vintage of the text` : `Vintage of the text` | `Office of the Minister` |
| g7-vintages | `Endnotes: the enactment that defines the Comptroller under the text of` | `the vintage of the text` : `Vintage of the text` | `Enactment that defines the Comptroller` |
| g7-vintages | `Endnotes: Article 2(1)(ba) is in the text of` | `the vintage of the text` : `Vintage of the text` | BOOLEAN |
| g7-vintages | `Endnotes: the Dormant Bank Accounts openings of Schedule 1 are in the text of` | `the vintage of the text` : `Vintage of the text` | BOOLEAN |
| g7-vintages | `Endnotes: the office of the Minister on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Office of the Minister` |
| g7-vintages | `Endnotes: the office of the Minister at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Office of the Minister` |
| g7-vintages | `Endnotes: the enactment that defines the Comptroller on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Enactment that defines the Comptroller` |
| g7-vintages | `Endnotes: the enactment that defines the Comptroller at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | `Enactment that defines the Comptroller` |
| g7-vintages | `Endnotes: Article 2(1)(ba) is in force on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-vintages | `Endnotes: Article 2(1)(ba) is in force at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-vintages | `Endnotes: the Dormant Bank Accounts openings of Schedule 1 are in force on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-vintages | `Endnotes: the Dormant Bank Accounts openings of Schedule 1 are in force at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | BOOLEAN |
| g7-vintages | `Endnotes: the amending instruments in force at` | `the moment` : DATETIME; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Amending instrument` |
| g7-vintages | `Endnotes: the amending instruments in force on` | `the day` : DATE; interp : `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` | LIST OF `Amending instrument` |

## 6. Contradictions, drift and slips in the source (a separate pass, made after encoding, against the modules)

Each item names both provisions, the case that discriminates, and where the other reading is callable.

| id | the provisions | the case that discriminates | where the other reading is callable or recorded |
| --- | --- | --- | --- |
| C1 (fork F7.12) | Article 22(1) defines an excepted foreign charity "For the purpose of Article 21"; Article 2(10)(b) says "an excepted foreign charity (within the meaning of Article 22)". | A conviction under 2(10)(b) in relation to an excepted foreign charity. | `Art 22 the entity is an excepted foreign charity for the purpose of Article 2(10)(b)` |
| C2 (fork F7.13) | Article 24(3)(a) lets the Regulations adapt "any provisions of Articles 21 to 23", whose offences carry imprisonment (21(9), 23(7)); Article 24(4) caps the penalty at "no greater than a fine". | Regulations adapting 21(9) wholesale. | `Art 24 the Regulations may attach this penalty to the offence` |
| C3 (fork F7.14) | Article 2(2) lets the Minister by Order add sub-paragraphs to Article 2(1); Article 39(1) bars "an amendment of this Law" from the ancillary provisions of an Order; Article 39(2) extends the power to amend "by Regulations" only. | An Order under 2(2) that also amends 8(3)(a)(ii). | `Art 39 an Order under Article 2(2) may make a consequential amendment of another provision of the Law` |
| C4 (fork F7.4) | Articles 21(1) and 21(2) (with 21(7)) both reach an entity that, knowing it is untrue, tells a donor it is registered; likewise (3)/(4), (5)/(6), 23(1)/(2). | scenario 05. | `Art 21 and 23: the contraventions made out by the statement` |
| C5 (fork F7.5) | "or other advantage" is in 21(2)(b)(ii) and not in 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii). | scenario 11. | `Articles 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii) reach other advantage under` |
| C6 (fork F7.3) | The Table of Legislation History names "Articles 32, 38, 39, 40, 42, 43 and 44"; the Law now ends at Article 43. | present Article 41 on 2018-01-01. | `Commencement: the unit of the Law is in force on` |
| C7 (trap T30) | Articles 2(10)(b) (src:111, stage 1) and 4(c) (src:127, stage 1) and 19(1)(g) (stage 2) cite Article 22 and Part 6, which come into force on 1 January 2019: for up to four years a rule that cites Article 22 is in force and the Article it cites is not. | a conviction on 1 July 2018 of an offence in relation to an excepted foreign charity. | assertions under `Trap T30` in `g7-tests-commencement.l4`; the integrator's wrapper answers the Article 22 limb with a refusal before 2019-01-01 |
| C8 (fork F7.9) | Part 8 is brought into force in two stages (Article 32 against Articles 33 to 36) and Part 9 in three (Articles 38 to 43, Article 37, and the spent original Article 41), so "Part 8 is in force" has no single day. | Part 8 on 2015-06-01; Part 9 on 2018-06-01. | `Commencement: the unit of the Law is in force on` |
| C9 (forks F7.6, F7.10) | Article 37(1) names three kinds of body; Article 2(1)(a) and (i) and 2(3) make trustees and unincorporated associations entities that can offend; "director" is paired with "body corporate" and "partner" with "partnership". | a committee member of an unincorporated association; a director of an LLP. | `Art 37(1) the person is also guilty of the offence` |
| C10 | Article 22(3)(b) ("is not a registered charity") repeats the opening words of Article 21(5) and (6) ("An entity that is not a registered charity and is ..."); it is redundant in effect, because wherever the Law uses the term a registered charity is dealt with separately (21(5), 21(6), 2(10)(b)). | an excepted foreign charity that is registered. | `Art 22(3) the entity meets the second condition` (kept as the Law has it) |
| C11 | Article 42(a) reads "by reference the test itself" (no "to"): a slip, present in the consolidated text (src:750) and in the official PDF text layer. | none (no outcome depends on it). | Article 42(a) is encoded as a power; the slip is not repaired. |
| C12 | R&O.40/2019 Schedule 2 paragraph 1(e) cites "Article 1(1) of the Charities (Jersey) Law 2014"; Article 1 has no paragraph (1) (it is an unnumbered list of definitions); R&O.29/2021 cites "Article 1", R&O.28/2023 "1 definition “Minister”", R&O.10/2024 "Article 1 definition “Minister”". | none (the substituted words are the same under every citation). | recorded in the row for R&O.40/2019 of `g7-vintages.l4` |
| C13 | "giving of the notice" (Article 17(4), and 36(2)(b) "giving of notice of decisions") against "served" (Articles 1, 8(3)(k), 26, 27) against "service" (Article 38): whether the date of "giving" is the date of "service" is not answered. | Article 17(4) protection of an act done on the day between sending and receipt. | `Art 38 the date on which the notice is served` (fork F7.7); the integrator decides whether 17(4) reads it |
| C14 | The brief says the 2019 remainder is "Part 6 and whatever the original Article 41 and 44(2)-(3) were"; R&O.17/2018 Article 2 gives the remainder as what "Article 44(2) of that Law or Article 1 of this Act" did not bring into force, so the original 44(2) and (3) are inside stage 1. | the stage of the original Article 44. | one assertion in `g7-tests-red.l4` (the brief's claim, failing) |
| C15 | The survey took the 2 March 2021 text of "Minister" to be inferred because R&O.29/2021 was not among the inputs; the instrument is now among them and shows it (Article 6(1), Schedule 2 paragraph 1(e)); likewise R&O.136/2019 shows that Schedule 3 of L.13/2019 is in force on 1 January 2020 (Article 1 excepts only Articles 17 to 19). | none. | `g7-vintages.l4`: `date in force shown by the sources` is TRUE for both |
| C16 | The survey took L.1/2017's date of 16 December 2019 to rest on the Table alone; that is still so: Article 31(2) of L.1/2017 leaves the day to an Act of the States ("such day or days"), and the Act is not among the sources, so whether Article 30(3) came into force with the rest of that Law or on another day is not shown. | none. | `date in force shown by the sources` is FALSE for L.1/2017 |
| C17 (checked and consistent) | The chain of substitutions of the definition of "Minister" is consistent: each instrument replaces the words the previous one left (Chief Minister, Minister for External Relations, Minister for External Relations and Financial Services, Chief Minister, Minister for External Relations, Chief Minister), and R&O.56/2025 was made on 9 October 2025 by "THE MINISTER FOR EXTERNAL RELATIONS", which is the office the definition names in October 2025. | none. | `g7-tests-vintages.l4` |

Text checks made in this pass.

Articles 21 to 25 and 37 to 43 of the consolidated text were compared word by word (case, punctuation and quotation marks folded) with the official PDF text layer: the only differences are the running page headers.
The three tables of the endnotes read the same in both.
The nine point-in-time dates in the brief equal the dates of the Table (31 May 2019, 16 December 2019, 1 January 2020, 2 March 2021, 12 April 2023, 27 February 2024 at 9.30 a.m., 16 October 2025, 2 October 2026) and 1 January 2019 for the first.

### Re-read of the numbers (the pass the assignment asks for)

Every date in the rule modules (`YMD` in `g7-vintages.l4` and `g7-commencement.l4`: 21 November 2014, 1 May 2018, 1 January 2019, 31 May 2019, 16 December 2019, 1 January 2020, 2 March 2021, 5 April 2023, 27 February 2024, 9 October 2025, 25 September 2026) was looked up as written text in RAW or in `inputs/amending/`: all eleven are found.
The time of day, 9.30 a.m., is in R&O.10/2024 (cover and Article 5).
"7 days" is in R&O.28/2023 Article 3, R&O.56/2025 Article 2, R&O.102/2026 Article 7(6).
"2 years" is in src:563 and src:593 (24 months), "level 3 on the standard scale" in src:564 and src:592, and no amount of a fine is stated anywhere in the scope.
The Part ranges used by `g7-commencement.l4` (1-2, 3-4, 5-7, 8-17, 18-20, 21-25, 26-31, 32-36, 37-43) were re-derived by a script from the `Part n` headings and the article headings of RAW: they agree.
The stage lists (Parts 1 to 3; Articles 32, 38, 39, 40, 42, 43, 44; Parts 4, 5, 7, 8 other than Article 32; Article 37) are those of src:876-880 and R&O.17/2018 Article 1(a) to (e).
One expectation of my own was wrong on first writing and was corrected after reading the instruments: the first draft of the F7.11 tests moved the two Orders that come into force "7 days after it is made"; those Orders compute their own day (F7.2), so F7.11 (which moves a NAMED day) does not move them.
The correction is in `gen_tests_vintages.py`'s comment and in `g7-tests-vintages.l4`; it is not a finding about the source.

## 7. Open questions for a domain expert

- Is the day named in the Table the first day on which a provision is in force? (R&O.17/2018 says "come into force on"; the Interpretation (Jersey) Law 1954 is not among the sources.)
- Does "7 days after it is made" leave the day of making out (the seventh day after is the first day in force)? The three Orders in the sources say so by their Table dates.
- Which Jersey time is meant by "9.30 a.m." (taken: the tz zone Europe/Jersey, which is GMT on 27 February)?
- Is a Part brought into force in more than one stage "in force" when any, or all, of the Articles it held are (Parts 8 and 9)?
- What did the original Article 41 provide (R&O.17/2018's headings suggest taxation), and what did the original 44(3) provide?
- Did the Act appointing 16 December 2019 for L.1/2017 bring Article 30(3) into force on that day, or only part of that Law?
- Can the States still make regulations under Article 40(3) "for the purposes of the bringing into force of this Law" after 1 January 2019?
- Is the date of service of a notice the date of sending or of receipt, and has an Order been made under Article 38?
- Is an unincorporated association or a trust within Article 37(1), and are the directors of a limited liability partnership officers of a body corporate?
- Does "in connection with any of its activities in Jersey" (21(5), 21(6)) cover a statement made outside Jersey about activities carried on in Jersey?
- Does the awareness of 21(4)(a) and 21(6)(a) have to cover both limbs together?
- Is the omission of "or other advantage" in 21(4), 21(6) and 23(2) intended?
- Does an offence of both kinds (strict and knowing) by one act give two convictions, and can the penalties be cumulated?
- Does Article 22(1) define an excepted foreign charity for Article 2(10)(b)?
- Can Regulations under Article 24 attach imprisonment to an offence adapted from Article 21(9)?
- Can an Order under Article 2(2) make consequential amendments of other provisions of the Law?
- What is a "supervisory body" in Article 41(2)? (the term is defined in the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008, which is not among the sources.)

## 8. What the sources do not answer

- The text of the Law before 1 January 2019: the nine versions begin there. The enacted text of 2014 and Article 44(2) of the Law as enacted are not among the sources; the days before 2019 answer `before the first consolidated version`.
- The definition of "Minister" in force from 1 January 2019 to 30 May 2019 is INFERRED, not shown: R&O.40/2019 Schedule 2 paragraph 1(e) shows the words it replaced ("Chief Minister"), and endnote [1] lists no earlier amendment of Article 1.
- The Act that appointed 16 December 2019 for L.1/2017 is not among the sources; that date rests on the Table alone (C16).
- What the original Article 41 and the original Article 44(3) provided.
- Every Order and every set of Regulations the scope empowers: 21(8), 22(2)(a)(ii), 22(4), 22(5), 23(4), 24(1) to (4), 25(1), 38, 39(1), 39(2), 40(2), 40(3), 41(2), 42. None is among the sources; each is an input.
- The amount of "level 3 on the standard scale" (the Criminal Justice (Standard Scale of Fines) (Jersey) Law is not among the sources); the Law states no maximum for "a fine".
- The Interpretation (Jersey) Law 1954, which would settle how a day and a period are counted; the counting conventions are forks.
- Whether the consolidated text is the enacted text outside the amended provisions (the licence note says "for information purposes only").
- Anything after 2 October 2026: `Endnotes: the vintage of the text on` answers the text of 2 October 2026 for every later day (the consolidation runs "to Current"); an amendment after that date is not known.
- Whether an Order under Article 38 exists, and what it says about the date of service.
- Whether Jersey time is the time of the 9.30 a.m. (assumed, not ruled).

## 9. Peeked

During the first assignment: nothing.
The session's global instructions carry an index of someone's notes that mentions this subject; it was not followed.
No file under `commons`, `commonswt`, `canon`, `paper` or `jl4/examples` was opened, listed or searched, and no filesystem was searched for the names of the Law.
For the repairs of section 10 the files the fleet lead named were opened: the two `-tests-disagree.l4` files of the independent authors ind-b and ind-c, and, to run their assertions against the repaired modules, copies of their snapshots (including `ind-b-tests-fixtures-g7.l4`, `ind-b-tests-art21-25.l4` and `ind-c-tests-art37-43.l4`).
After the compaction of this session the harness restored into the context, unasked, the text of the integrator's assignment (`phase1/ASSIGN-INT.md`) and of a note from someone's memory about this fleet (the headlines of the hunt and the survey's counts); neither was used for either repair, and no decision in this file rests on them.


## 10. Changes after independent testing

Two repairs were made on 2026-10-27 after independent test authors found two defects.
Each repair was checked against the author's failing assertion: D1 of ind-c (Part 9) and V-18 of ind-b (a body that is not an entity) now hold on the repaired modules.
No fork was added, removed or renamed.
The exported names are unchanged; four exports gained one input each (the table below).

### R1: Part 9 and the original Article 41

What was wrong: a Part's stages were computed from the Articles now standing in it, so the original Article 41 (spent and omitted, stage 3, the remainder) was left out and Part 9 showed two stages.
On reading A of F7.9 Part 9 was then wholly in force from 1 May 2018; the original Article 41 came into force on 1 January 2019 (R&O.17/2018 Article 2).
What changed: `the stages of the Articles of Part` now takes the stages of every Article the Part held: the Articles now standing in it, by the reading of F7.3, and the spent original Articles that stood in it, by their original number.
Three new rules in `g7-commencement.l4` carry this: `the whole original Article that a row says is spent`, `the original Articles that are spent and omitted` and `the spent original Articles that stood in Part`.
The original Article 41 is placed in Part 9 by its position between the original Articles 40 and 42 (assumed, not ruled: the sources do not show the Part of the original Article 41).
The rows for the original 44(2) and 44(3) are paragraphs of the original Article 44, which survives as Article 43; they are not Articles that stood in a Part by themselves and the new rules give them no number.
Every other Part was checked: the Table of Renumbered Provisions lists no original Article numbered 1 to 40, so no other Part held a spent Article, and `g7-tests-commencement.l4` asserts that the list of spent Articles of each of Parts 1 to 8 is empty.

The stages and the days from which each Part is in force, by the two readings of F7.9 (F7.11: the day named is the first day in force):

| Part | stages | in force from, A (taken: all the Articles it held) | in force from, B (any Article) |
| --- | --- | --- | --- |
| 1 | stage 1 | 2014-11-21 | 2014-11-21 |
| 2 | stage 1 | 2014-11-21 | 2014-11-21 |
| 3 | stage 1 | 2014-11-21 | 2014-11-21 |
| 4 | stage 2 | 2018-05-01 | 2018-05-01 |
| 5 | stage 2 | 2018-05-01 | 2018-05-01 |
| 6 | stage 3 | 2019-01-01 | 2019-01-01 |
| 7 | stage 2 | 2018-05-01 | 2018-05-01 |
| 8 | stage 1, stage 2 | 2018-05-01 | 2014-11-21 |
| 9 | stage 1, stage 2, stage 3 | 2019-01-01 | 2014-11-21 |

Every Part is asserted on each side of each stage date it could be in force on, on both readings (`g7-tests-commencement.l4`, section `The Parts`).
The reading B is unchanged: it answers from the first stage, so Part 9 is in force from 2014-11-21 on it, as before.
Under F7.3 B (the Table read in present numbers) Part 9 also has three stages: the present Article 41 is in the remainder, and the spent original Article 41 is in the remainder on either reading.
Fork touched: F7.9 (its reading A now reaches Part 9 from 1 January 2019; its text and its tests are updated).
F7.3 is touched only in that the spent original Articles are numbered by their ORIGINAL number whichever way the Table is read; its readings and its discriminating test are unchanged.

### R2: Articles 21 and 23 reach an entity only

What was wrong: the prohibitions of Articles 21 and 23 were applied to a body whose `kinds of entity` is empty (a partnership; an NPO body corporate on 15 October 2025, before paragraph (ba) was added on 16 October 2025), so such a body that called itself a "charity" in connection with its Jersey activities was reported as contravening 21(5), a level 3 offence.
What changed: a new rule `the body is an entity within Article 2(1)` (a body is an entity if its `kinds of entity` is not empty) is a condition of each binding predicate, and so of the contravention predicates, the regulative rules, the offences, the penalties and the F7.4 list functions that call it.
The guard is on the subject of 21(1), 21(3), 21(5), 23(1) and on the object of 21(2), 21(4), 21(6), 23(2), where the text of each paragraph names an entity ("An entity that is not a registered charity", "A Jersey entity", "An entity ... that is neither a Jersey entity nor an excepted foreign charity", "Unless an entity meets all of the conditions in paragraph (3), that entity"; "refer to an entity", "refer to a Jersey entity").
It is not on the person who refers in 21(2), 21(4), 21(6), 23(2), who need not be an entity (21(9): "An entity or other person").
Paragraphs 21(7) and 23(5) are unchanged.
The fork about "Jersey charity" (21(3) against 23(1), F7 A-10) is not touched.
Each paragraph is asserted on both sides (an entity, a partnership, a body flagged as a Jersey entity that is within no sub-paragraph of Article 2(1)) in `g7-tests-expressions.l4`, section `Articles 21 and 23 reach an ENTITY`, with the NPO body corporate of V-18 on 15 and 16 October 2025, the list functions, the offences and the traces (`g7-tests-expression-traces.l4`, section `A body that is not an entity`).

### Signature changes (every one)

Four exports gained one input, `the entity` : `Entity` (IP5), placed FIRST, as in the sibling rules of 21(3) to (6) and 23 which already took it.
Each carries a `@desc`.
No other export changed its name or its inputs.


| rule | old GIVEN list | new GIVEN list |
| --- | --- | --- |
| `Art 21(1) the statement contravenes paragraph (1)` | `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` |
| `Art 21(1) an unregistered entity must not say it is registered by the Commissioner` | `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` |
| `Art 21(2) the statement contravenes paragraph (2)` | `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` |
| `Art 21(2) a person must not say that an unregistered entity is registered, with knowledge and intent` | referrer : `Party to the prohibitions on expressions`; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` | referrer : `Party to the prohibitions on expressions`; `the entity` : Entity; `the entity is a registered charity` : BOOLEAN; statement : `Statement about an entity under Articles 21 to 23` |

The same input was added to six rules that are not exported and that the integrator may still call: `Art 21(1) the prohibition binds the entity`, `Art 21(1)(a) the entity contravenes sub-paragraph (a)`, `Art 21(1)(b) the entity contravenes sub-paragraph (b)`, `Art 21(2) the prohibition binds the person`, `Art 21(1)(a) an unregistered entity must not refer to itself as being registered by the Commissioner` and `Art 21(1)(b) an unregistered entity must not cause or permit another person to refer to it as being registered by the Commissioner`.
The rules of 21(3) to (6) and 23 already took `the entity`; their inputs are unchanged and only their bodies gained the guard, so a call that passed an entity whose `kinds of entity` is empty now answers as a non-entity (no contravention).
A new, non-exported rule `the body is an entity within Article 2(1)` (input `the entity` : Entity) holds the test.
What this means for a caller: pass the entity as G1 derives it for the day (IP5), with `kinds of entity` as Article 2(1) leaves it; an entity with `kinds of entity` empty gets no offence from Articles 21 and 23.

### Not done, and notes for the integrator

The wording of the type `Treatment of a Part brought into force in two stages` and its two values was not changed, because exported names must not change; Part 9 now has three stages, and the name says two.
Which Part the original Article 41 stood in is assumed from its position; if the Law as enacted placed it elsewhere the days for Part 9 would revert to those of the present Articles.
The old and new `Commencement: the stages in which the unit was brought into force` answers differ for Part 9 only.
Not run: the integrator's `int-` modules (they were being edited while this repair was made; `int-readings.l4` did not check, on a missing input of a G2 record, which is not a G7 input).
None of the `int-` modules calls the four rules that changed by name.

