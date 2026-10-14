# PLAN: the Charities (Jersey) Law 2014, the whole Law, in L4

Status: **proposed**, written by the SURVEYOR on 2026-10-14 from the sources named in the BRIEF only, before any encoder has started.
Where the fleet lead's rulings added to `BRIEF.md` after this survey differ from this plan, they govern; an encoder may change a disposition or a reading by registering a fork.
Nothing here is verified against any encoding: the claims about the Law are verified against the consolidated text, its PDF text layer and the amending instruments in `inputs/`, and each is marked "shown" (the sources say it) or "inferred" (the sources imply it).

## 0. How to read this plan

**What this is.** One document that tells nine encoders what to encode and how their groups fit.
Section (a) is the coverage skeleton for the whole Law, one row for every node of the source text, with its disposition; the same table is `FLEET_DIR/phase1/coverage.tsv`.
Section (b) is the group map: modules, exports with exact names, inputs.
Section (c) is the integration table; its names are standard and exact.
Sections (d) to (g) are the periods register, the terminology, the traps found on first reading, and the candidate forks.
Section 8 explains `FLEET_DIR/deposit/domain.l4`; 9 lists what the sources do not answer; 10 is for the integrator.

**Ids.**

| kind | spelling | example |
| --- | --- | --- |
| Article, paragraph, sub-paragraph | as the Law writes them | `8(3)(a)(i)`, `2(1)(ba)(iii)` |
| definition in Article 1 (unnumbered) | `1[term]`, and `(a)` etc. for its limbs | `1[Minister]`, `1[regulated financial services business](a)` |
| Schedule | `Sch 1`, `Sch1 4(3)(b)` (Schedule 1 paragraph 4(3)(b)) | `Sch2 4(3)(f)` |
| endnote rows | `E1` to `E11` (Table of Legislation History: three stages of L.41/2014, then the eight amending instruments in order), `R1` to `R6` (Table of Renumbered Provisions), `N1` to `N5` (Table of Endnote References) | `E3`, `R2` |
| front matter | `Title`, `Long title`, `Commencement note` | |
| integration point | `IP1` ... | section (c) |
| period | `P1` ... | section (d) |
| trap | `T1` ... | section (f) |
| fork | `F<group>.<n>` | `F6.10` |

**Dispositions.** `encoded`: becomes L4 (a rule, a record, a lookup, a typed regulative rule, or a named refusal inside one). `inert`: quoted in the module as labelled inert text with no operative L4. `refused`: its content is not in the sources and the module carries a named `REFUSE`. `out-of-scope`: the text of another enactment, or an amendment of one.
The column `reason` has a real reason for every row that is not `encoded`; for an `encoded` row it holds a note (prefixed `note:`) on what the encoder should watch.

**Notation for standard inputs.** A standard input is written as a name and a type separated by a colon: `the day` : DATE stands for the declaration ``GIVEN `the day` IS A DATE``, and `the entity` : Entity for ``GIVEN `the entity` IS AN Entity``. A phrase in backticks that begins `Art`, `Sch`, `Commencement:` or `Endnotes:` is an export. An action type `Act under ...` is a group's own enumeration of what is done.

**Method, so the figures can be trusted.** The text of Articles 1 to 43, Schedules 1 and 2 was compared word by word with the official PDF's text layer: no difference except line-end hyphenation, the case of headings and the position of footnote markers. The Table of Legislation History was checked against the PDF layout (the text file reassembles its columns). `first_words` in the coverage table is the output of `srcrefs.py quote` on the row's first source line, cut at ten words. The parse of the text into rows was scripted; every node has exactly one row (0 missing, 0 unknown, 0 duplicate).
Dates in the examples are chosen to separate readings, and the arithmetic in sections (d) and (g) was evaluated with `L4_BIN` and `daydate`: `add months` of 2026-11-30 by 3 is 2027-02-28 (the rolled `Date 30 2 2027` is 2 March 2027); `add years` of 2028-02-29 by 15 is 2043-02-28; `add months` of 2026-12-31 by 4 is 2027-04-30 (the rolled `Date 31 4 2027` is 1 May 2027); 12 calendar years from 2026-03-01 are 4,383 days; 2027-03-01 to 2028-03-01 is 366 days; 9 October 2025, 5 April 2023 and 25 September 2026 plus 7 days are 16 October 2025, 12 April 2023 and 2 October 2026.

**What is proposed, not decided.** The depth ("every duty, power, prohibition, offence, number and time limit as a typed rule, every definition that decides an outcome as a noun and a rule") is the BRIEF's assumption, "not ruled". The default reading of each fork is a proposal. Dispositions in section (a) are a proposal; the judgement calls are listed after the table.

## (a) Coverage skeleton

One row for every Article and for every lettered or numbered paragraph, in the Law's own numbering, for the whole Law: the 43 Articles, the 35 definitions of Article 1 (cited `1[term]`), every paragraph, sub-paragraph and sub-sub-paragraph, the two Schedules and their eight paragraphs, the endnote tables, and three front-matter lines. The same table is `FLEET_DIR/phase1/coverage.tsv` (tab-separated, header `id	provision	first_words	gloss	disposition	module	group	reason`).

**Totals.** 851 rows: 745 `encoded`, 82 `inert`, 1 `refused`, 23 `out-of-scope`. Nothing is `deferred`.

| group | rows | encoded | inert | refused | out-of-scope |
| --- | --- | --- | --- | --- | --- |
| G1 | 113 | 76 | 25 | 0 | 12 |
| G2 | 90 | 77 | 13 | 0 | 0 |
| G3 | 82 | 82 | 0 | 0 | 0 |
| G4 | 73 | 73 | 0 | 0 | 0 |
| G5 | 58 | 58 | 0 | 0 | 0 |
| G6 | 99 | 99 | 0 | 0 | 0 |
| G7 | 129 | 101 | 18 | 1 | 9 |
| G8 | 104 | 96 | 6 | 0 | 2 |
| G9 | 103 | 83 | 20 | 0 | 0 |

The group is the group whose scope contains the provision; the module is where the row is carried (an inert pointer in Article 1 is carried by G1's module even when it points at another group's Article).

| id | provision | first words | gloss | disposition proposed | module proposed | group | reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Title | Title | Charities (Jersey) Law 2014 | the Law's short title, Charities (Jersey) Law 2014 | inert | g1-art1-defined-terms | G1 | heading only; no rule |
| Long title | Long title | A LAW to establish a commissioner and register of charities, … | long title: commissioner, register, governors' duties, regulating "charity", related purposes | inert | g1-art1-defined-terms | G1 | statement of purposes of the Law; gates nothing; no outcome to compute |
| Commencement note | Commencement note | Commencement [see endnotes] | "Commencement [see endnotes]": pointer to the staged commencement | inert | g7-commencement | G7 | pointer only; the commencement rules are encoded from the endnote rows (E1 to E3, R1 to R6) |
| 1 | Article 1 | 1 Interpretation[1] | Article 1: the definitions of the whole Law, "unless the context otherwise requires" | encoded | g1-art1-defined-terms | G1 | note: the lead-in "unless the context otherwise requires" is the general override; encoders record each place where context displaces a definition (5(2)(a) "a Minister") |
| 1[annual return] | Article 1 definition “annual return” | “annual return” means a return sent under Article 13(7); | "annual return" is a return sent under Article 13(7) | inert | g1-art1-defined-terms | G1 | pure pointer; the duty to send it is encoded at 13(7) (G5) |
| 1[charitable purpose] | Article 1 definition “charitable purpose” | “charitable purpose” has the meaning given by Article 6; | "charitable purpose" has the meaning in Article 6 | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at Article 6 (G2) |
| 1[Commissioner] | Article 1 definition “Commissioner” | “Commissioner” means the person for the time being appointed to … | the Commissioner is whoever is for the time being appointed to the office created by Article 3 | inert | g1-art1-defined-terms | G1 | role definition: carried by the actor constructor `the Commissioner`; who holds the office on a day is Schedule 1 (G9) |
| 1[company] | Article 1 definition “company” | “company” means a company registered under the Companies (Jersey) Law … | "company" is a company under the Companies (Jersey) Law 1991, with its directors, memorandum, articles | out-of-scope | (none) | G1 | text of the Companies (Jersey) Law 1991 not in sources; whether a body is such a company is an input fact to Article 2(1)(f) |
| 1[Comptroller] | Article 1 definition “Comptroller” | “Comptroller” has the meaning given by the Revenue Administration (Jersey) … | "Comptroller" has the meaning in the Revenue Administration (Jersey) Law 2019 (before 1 January 2020: the Income Tax (Jersey) Law 1961) | encoded | g1-art1-defined-terms | G1 | note: vintage-dependent text (L.13/2019); the encoded part is which Law defines the term in which vintage; the substance of those Laws is out of scope |
| 1[constitution] | Article 1 definition “constitution” | “constitution” has the meaning given by Article 2(4); | "constitution" has the meaning in Article 2(4) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(4) |
| 1[constitutional Law] | Article 1 definition “constitutional Law” | “constitutional Law” has the meaning given by Article 2(5); | "constitutional Law" has the meaning in Article 2(5) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(5) |
| 1[court] | Article 1 definition “court” | “court”, in the expression “the court”, means the Royal Court; | "the court" means the Royal Court | inert | g1-art1-defined-terms | G1 | role definition: carried by the actor constructor `the court` |
| 1[court-approved fidéicommis] | Article 1 definition “court-approved fidéicommis” | “court-approved fidéicommis” means a fidéicommis created under Article 3 of … | a fidéicommis created under Article 3 of the Loi of 1862 or extended the Loi's benefits under its Article 17 | out-of-scope | (none) | G1 | text of the Loi (1862) not in sources; whether a body is one is an input fact to Article 2(1)(b) |
| 1[donation] | Article 1 definition “donation” | “donation” is to be construed in accordance with the Order … | "donation" is construed per the Order under Article 9(3)(b)(ii) | inert | g1-art1-defined-terms | G1 | pointer to the content of an Order not in the sources; encoded as an input at 9(3)(b)(ii) |
| 1[entity] | Article 1 definition “entity” | “entity” has the meaning given by Article 2(1); | "entity" has the meaning in Article 2(1) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(1) |
| 1[foundation] | Article 1 definition “foundation” | “foundation” means a foundation incorporated under the Foundations (Jersey) Law … | "foundation" is a foundation under the Foundations (Jersey) Law 2009, with its charter, regulations, council member | out-of-scope | (none) | G1 | text of the Foundations (Jersey) Law 2009 not in sources; an input fact to Article 2(1)(d) |
| 1[general section] | Article 1 definition “general section” | “general section” means the section of the register that is … | the section of the register distinguished from the restricted and historic sections under Article 8(2) | inert | g1-art1-defined-terms | G1 | pointer; encoded at 8(2) |
| 1[governor] | Article 1 definition “governor” | “governor” in relation to an entity (including a registered charity) … | "governor" in relation to an entity has the meaning in Article 2(7) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(7) to (9) |
| 1[incorporated 1862 association] | Article 1 definition “incorporated 1862 association” | “incorporated 1862 association” means an association incorporated under Article 4 … | an association incorporated under Article 4 of the Loi of 1862 | out-of-scope | (none) | G1 | text of the Loi (1862) not in sources; an input fact to Article 2(1)(c) |
| 1[JFSC] | Article 1 definition “JFSC” | “JFSC” means the Jersey Financial Services Commission established by the … | the Jersey Financial Services Commission under the Financial Services Commission (Jersey) Law 1998 | out-of-scope | (none) | G1 | that Law not in sources; carried as the actor constructor `the Jersey Financial Services Commission` |
| 1[Jersey entity] | Article 1 definition “Jersey entity” | “Jersey entity” has the meaning given by Article 2(3); | "Jersey entity" has the meaning in Article 2(3) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(3) |
| 1[Loi of 1862] | Article 1 definition “Loi of 1862” | “Loi of 1862” means the Loi (1862) sur les teneures … | the Loi (1862) sur les teneures en fidéicommis et l'incorporation d'associations | out-of-scope | (none) | G1 | title of another enactment, not in sources |
| 1[Minister] | Article 1 definition “Minister” | “Minister” means the Chief Minister; | "Minister" means the Chief Minister (as the text of 2 October 2026 reads; earlier texts name other offices) | encoded | g1-art1-defined-terms | G1 | note: vintage-dependent: five texts in the nine versions (R&O.40/2019, R&O.29/2021, R&O.28/2023, R&O.10/2024, R&O.102/2026); a vintage the sources do not show answers REFUSE |
| 1[misconduct] | Article 1 definition “misconduct” | “misconduct” has the meaning given by Article 2(10), and a … | "misconduct" has the meaning in Article 2(10); a governor's misconduct is read under Article 18(4) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(10) (G1) and 18(4) (G6) |
| 1[prescribed] | Article 1 definition “prescribed” | “prescribed” and “specified” mean prescribed or specified in an Order … | "prescribed" and "specified" mean prescribed or specified in an Order or Regulations as the case may be | inert | g1-art1-defined-terms | G1 | rule of construction; implemented by the fleet convention that the content of an Order or Regulations is an input (BRIEF, scope) |
| 1[property] | Article 1 definition “property” | “property” has the meaning given by the Trusts (Jersey) Law … | "property" has the meaning in the Trusts (Jersey) Law 1984 | out-of-scope | (none) | G1 | that Law not in sources; "property" is an input noun wherever used |
| 1[publish] | Article 1 definition “publish” | “publish”, in respect of any information, means publish in a … | "publish" means publish in a manner that, in the opinion of the person publishing, is likely to bring the information to the attention of the public or those affected | encoded | g1-art1-defined-terms | G1 | note: subjective test: the opinion of the publisher is an input (fork F1.5); used by 4(1)(d), 5(4), 5(6)(b), 9(4)(a), 11(2), 11(6)(a), 11(9), Sch 1 4(8), 4(11) |
| 1[purpose] | Article 1 definition “purpose” | “purpose”, in relation to an entity, has the meaning given … | "purpose" in relation to an entity has the meaning in Article 2(6) | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 2(6) |
| 1[register] | Article 1 definition “register” | “register” means the register kept by the Commissioner under Article … | "register" is the register kept under Article 8, or (verb) to enter an entity on it | inert | g1-art1-defined-terms | G1 | pointer; encoded at Article 8 |
| 1[registered charitable purposes] | Article 1 definition “registered charitable purposes” | “registered charitable purposes” has the meaning assigned by Article 8(3)(e); | has the meaning in Article 8(3)(e) | inert | g1-art1-defined-terms | G1 | pointer; encoded at 8(3)(e) |
| 1[registered charity] | Article 1 definition “registered charity” | “registered charity” means an entity entered for the time being … | "registered charity" is an entity entered for the time being in the general or the restricted section of the register | encoded | g1-art1-defined-terms | G1 | note: decides outcomes throughout: the historic section is NOT included; the standing on the register is the input |
| 1[registered public benefit statement] | Article 1 definition “registered public benefit statement” | “registered public benefit statement” has the meaning assigned by Article … | has the meaning in Article 8(3)(f) | inert | g1-art1-defined-terms | G1 | pointer; encoded at 8(3)(f) |
| 1[regulated financial services business] | Article 1 definition “regulated financial services business” | “regulated financial services business” means business for which a person … | business for which a person is registered, permitted or authorized under four financial-services Laws | inert | g1-art1-defined-terms | G1 | used only in 11(7)(a) (content of Regulations) and 14(3)(e) (content of an order); the four limbs are registrations under other Laws (out of scope) |
| 1[regulated financial services business](a) | Article 1 definition “regulated financial services business”(a) | (a) is registered under the Banking Business (Jersey) Law 1991; | registered under the Banking Business (Jersey) Law 1991 | out-of-scope | (none) | G1 | another enactment, not in sources |
| 1[regulated financial services business](b) | Article 1 definition “regulated financial services business”(b) | (b) holds a permit or certificate under the Collective Investment … | holds a permit or certificate under the Collective Investment Funds (Jersey) Law 1988 | out-of-scope | (none) | G1 | another enactment, not in sources |
| 1[regulated financial services business](c) | Article 1 definition “regulated financial services business”(c) | (c) is registered under the Financial Services (Jersey) Law 1998; … | registered under the Financial Services (Jersey) Law 1998 | out-of-scope | (none) | G1 | another enactment, not in sources |
| 1[regulated financial services business](d) | Article 1 definition “regulated financial services business”(d) | (d) is authorized by a permit under the Insurance Business … | authorized by a permit under the Insurance Business (Jersey) Law 1996 | out-of-scope | (none) | G1 | another enactment, not in sources |
| 1[reportable matter] | Article 1 definition “reportable matter” | “reportable matter” has the meaning given by Article 19; | "reportable matter" has the meaning in Article 19 | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at 19(1) |
| 1[required steps notice] | Article 1 definition “required steps notice” | “required steps notice” means a notice served under Article 27; | a notice served under Article 27 | inert | g1-art1-defined-terms | G1 | pure pointer; encoded at Article 27 |
| 1[restricted section] | Article 1 definition “restricted section” | “restricted section” means the section of the register that is … | the section of the register distinguished from the general and historic sections under Article 8(2) | inert | g1-art1-defined-terms | G1 | pointer; encoded at 8(2) |
| 1[solicit] | Article 1 definition “solicit” | “solicit” is to be construed in accordance with the Order … | "solicit" is construed per the Order under Article 9(3)(b)(i) | inert | g1-art1-defined-terms | G1 | pointer to the content of an Order not in the sources; encoded as an input at 9(3)(b)(i) |
| 1[tribunal] | Article 1 definition “tribunal” | “tribunal” means the Charity Tribunal established by Article 32; | "tribunal" means the Charity Tribunal established by Article 32 | inert | g1-art1-defined-terms | G1 | role definition: carried by the actor constructor `the Charity Tribunal` |
| 1[trust] | Article 1 definition “trust” | “trust” means a trust over which the court has jurisdiction … | a trust over which the court has jurisdiction under Article 5 of the Trusts (Jersey) Law 1984 | out-of-scope | (none) | G1 | that Law not in sources; whether a body is one is an input fact to Article 2(1)(a) |
| 2 | Article 2 | 2 Definition of entity and related terms | Article 2: entity, Jersey entity, constitution, constitutional Law, purpose | encoded | g1-art2-entity | G1 |  |
| 2(1) | Article 2(1) | (1) In this Law, unless the context otherwise requires, “entity” … | "entity" means any of ten (eleven from 16 October 2025) kinds of person or body | encoded | g1-art2-entity | G1 |  |
| 2(1)(a) | Article 2(1)(a) | (a) the person or persons, taken together, who are the … | the persons, taken together, who are the trustees of a trust | encoded | g1-art2-entity | G1 |  |
| 2(1)(b) | Article 2(1)(b) | (b) without prejudice to the generality of sub-paragraph (a), the … | without prejudice to (a), the fidéicommissaires of a court-approved fidéicommis, taken together | encoded | g1-art2-entity | G1 |  |
| 2(1)(ba) | Article 2(1)(ba) | (ba) a body corporate that – | a body corporate that is an NPO, established under Jersey law, and in none of (c) to (h) (inserted by R&O.56/2025) | encoded | g1-art2-entity | G1 | note: exists only in the text of 16 October 2025 and later |
| 2(1)(ba)(i) | Article 2(1)(ba)(i) | (i) is an NPO, as defined by the Non-Profit Organizations … | is an NPO as defined by the Non-Profit Organizations (Jersey) Law 2008 | encoded | g1-art2-entity | G1 | note: whether a body is an NPO is an input |
| 2(1)(ba)(ii) | Article 2(1)(ba)(ii) | (ii) is established under the law of Jersey; and | is established under the law of Jersey | encoded | g1-art2-entity | G1 |  |
| 2(1)(ba)(iii) | Article 2(1)(ba)(iii) | (iii) does not fall within any of sub-paragraphs (c) to … | does not fall within any of (c) to (h) | encoded | g1-art2-entity | G1 |  |
| 2(1)(c) | Article 2(1)(c) | (c) an incorporated 1862 association; | an incorporated 1862 association | encoded | g1-art2-entity | G1 |  |
| 2(1)(d) | Article 2(1)(d) | (d) a foundation; | a foundation | encoded | g1-art2-entity | G1 |  |
| 2(1)(e) | Article 2(1)(e) | (e) a body corporate established – | a body corporate established by an enactment, an Act of the States or a Royal Charter in relation to Jersey | encoded | g1-art2-entity | G1 |  |
| 2(1)(e)(i) | Article 2(1)(e)(i) | (i) by an enactment, | established by an enactment | encoded | g1-art2-entity | G1 |  |
| 2(1)(e)(ii) | Article 2(1)(e)(ii) | (ii) by Act of the States, or | established by Act of the States | encoded | g1-art2-entity | G1 |  |
| 2(1)(e)(iii) | Article 2(1)(e)(iii) | (iii) by Royal Charter, in relation to Jersey; | established by Royal Charter, in relation to Jersey | encoded | g1-art2-entity | G1 |  |
| 2(1)(f) | Article 2(1)(f) | (f) a company; | a company | encoded | g1-art2-entity | G1 |  |
| 2(1)(g) | Article 2(1)(g) | (g) a body incorporated under, but not by, any enactment … | a body incorporated under, but not by, an enactment other than the Companies (Jersey) Law 1991 | encoded | g1-art2-entity | G1 |  |
| 2(1)(h) | Article 2(1)(h) | (h) a body incorporated under, but not by, an Act … | a body incorporated under, but not by, a UK Act or Order in Council extended or applicable in Jersey | encoded | g1-art2-entity | G1 |  |
| 2(1)(i) | Article 2(1)(i) | (i) the persons, taken together, who constitute for the time … | the persons, taken together, who constitute an unincorporated body or association, not a partnership and not trustees of a trust | encoded | g1-art2-entity | G1 |  |
| 2(1)(j) | Article 2(1)(j) | (j) an entity that is substantially similar to an entity … | an entity substantially similar to one in (a) to (h) but established under the law of a jurisdiction other than Jersey | encoded | g1-art2-entity | G1 | note: whether "(a) to (h)" includes the later-inserted (ba): see fork F1.1 |
| 2(2) | Article 2(2) | (2) The Minister may by Order add sub-paragraphs to paragraph … | the Minister may by Order add sub-paragraphs to paragraph (1) | encoded | g1-art2-entity | G1 | note: power typed MAY (the Minister); the content of the Order is an input; R&O.56/2025 is the one exercise in the sources |
| 2(3) | Article 2(3) | (3) For the purposes of this Law, an entity is … | a "Jersey entity": within (a) to (h), or an unincorporated body governed by Jersey law with a qualifying governor | encoded | g1-art2-entity | G1 |  |
| 2(3)(a) | Article 2(3)(a) | (a) it falls within any of sub-paragraphs (a) to (h) … | falls within any of 2(1)(a) to (h) | encoded | g1-art2-entity | G1 | note: range question F1.1 |
| 2(3)(b) | Article 2(3)(b) | (b) it is an unincorporated body or association of persons … | an unincorporated body in 2(1)(i) meeting (i) and (ii) | encoded | g1-art2-entity | G1 |  |
| 2(3)(b)(i) | Article 2(3)(b)(i) | (i) the law governing the relationship between the persons constituting … | the law governing the relationship between the persons constituting it is the law of Jersey | encoded | g1-art2-entity | G1 |  |
| 2(3)(b)(ii) | Article 2(3)(b)(ii) | (ii) at least one governor is a natural person resident … | at least one governor is a natural person resident in Jersey, or is itself a Jersey entity by virtue of 2(3)(a) | encoded | g1-art2-entity | G1 | note: one level of look-through only: via (a), not (b) |
| 2(4) | Article 2(4) | (4) In this Law, unless the context otherwise requires, “constitution” … | "constitution": the document or documents that establish the entity, by kind | encoded | g1-art2-entity | G1 | note: lookup from kind of entity; the document is an input everywhere the Law reads it |
| 2(4)(a) | Article 2(4)(a) | (a) in the case of a trust the terms of … | trust: the terms of the trust | encoded | g1-art2-entity | G1 |  |
| 2(4)(b) | Article 2(4)(b) | (b) in the case of a court-approved fidéicommis, the minute … | court-approved fidéicommis: the minute annexed to the application, other annexed documents, any authorisation under Article 10 of the Loi | encoded | g1-art2-entity | G1 |  |
| 2(4)(c) | Article 2(4)(c) | (c) in the case of an incorporated 1862 association, the … | incorporated 1862 association: the Act of court incorporating it and the object and rules approved or modified | encoded | g1-art2-entity | G1 |  |
| 2(4)(d) | Article 2(4)(d) | (d) in the case of a foundation, the charter and … | foundation: the charter and regulations | encoded | g1-art2-entity | G1 |  |
| 2(4)(e) | Article 2(4)(e) | (e) in the case of a company, the memorandum and … | company: the memorandum and articles of association | encoded | g1-art2-entity | G1 |  |
| 2(4)(f) | Article 2(4)(f) | (f) in the case of a body corporate falling within … | body corporate under 2(1)(e): the enactment, Act of the States or Royal Charter that established it | encoded | g1-art2-entity | G1 |  |
| 2(4)(g) | Article 2(4)(g) | (g) in any other case, any instrument or instruments (in … | any other case: any instrument or instruments, in whatever form, that establish the entity or give it powers | encoded | g1-art2-entity | G1 | note: "in whatever form" sits beside 11(4)(b) "a written document" |
| 2(5) | Article 2(5) | (5) In this Law, unless the context otherwise requires, “constitutional … | "constitutional Law": the governing Law, by kind of entity | encoded | g1-art2-entity | G1 | note: no case for kinds (ba), (g), (h), (i), (j): trap T6, fork F1.3; answers MAYBE (NOTHING) |
| 2(5)(a) | Article 2(5)(a) | (a) in relation to an entity that is a trust, … | trust: the Trusts (Jersey) Law 1984 | encoded | g1-art2-entity | G1 |  |
| 2(5)(b) | Article 2(5)(b) | (b) in relation to an entity that is a court-approved … | court-approved fidéicommis or incorporated 1862 association: the Loi of 1862 | encoded | g1-art2-entity | G1 |  |
| 2(5)(c) | Article 2(5)(c) | (c) in relation to an entity that is a foundation, … | foundation: the Foundations (Jersey) Law 2009 | encoded | g1-art2-entity | G1 |  |
| 2(5)(d) | Article 2(5)(d) | (d) in relation to an entity that is a company, … | company: the Companies (Jersey) Law 1991 | encoded | g1-art2-entity | G1 |  |
| 2(5)(e) | Article 2(5)(e) | (e) in relation to an entity that is a body … | a body incorporated by (but not under) any other Law: that Law | encoded | g1-art2-entity | G1 | note: says "by (but not under)"; the (g) and (h) kinds are incorporated "under, but not by" |
| 2(6) | Article 2(6) | (6) In this Law, unless the context otherwise requires, “purpose” … | "purpose": what the entity's purposes are, by kind | encoded | g1-art2-entity | G1 |  |
| 2(6)(a) | Article 2(6)(a) | (a) in the case of a trust, the benefit of … | trust: benefit of beneficiaries or another purpose in Article 2(b) of the Trusts Law, as in its constitution | encoded | g1-art2-entity | G1 |  |
| 2(6)(b) | Article 2(6)(b) | (b) in the case of a court-approved fidéicommis, or of … | fidéicommis or 1862 association: the objects for which created or incorporated, or later authorized under Article 10 of the Loi | encoded | g1-art2-entity | G1 |  |
| 2(6)(c) | Article 2(6)(c) | (c) in the case of a foundation, the objects specified … | foundation: the objects in its charter or regulations | encoded | g1-art2-entity | G1 |  |
| 2(6)(d) | Article 2(6)(d) | (d) in the case of any other entity, a purpose … | any other entity: a purpose to which its property may lawfully be applied, other than by court order, per its constitution, including on winding up | encoded | g1-art2-entity | G1 |  |
| 2(7) | Article 2(7) | (7) In this Law, unless the context otherwise requires, “governor” … | "governor": trustee, council member, director, committee member, or person with general control and management | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(7)(a) | Article 2(7)(a) | (a) in the case of a trust or fidéicommis, a … | trust or fidéicommis: a trustee or fidéicommissaire | encoded | g1-art2-governor-misconduct | G1 | note: a corporate trustee is the governor; look-through to its directors is fork F1.4 |
| 2(7)(b) | Article 2(7)(b) | (b) in the case of a foundation, a member of … | foundation: a member of the council | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(7)(c) | Article 2(7)(c) | (c) in the case of a company, a director of … | company: a director | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(7)(d) | Article 2(7)(d) | (d) in the case of a relevant unincorporated entity, a … | relevant unincorporated entity: a member of its management committee | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(7)(e) | Article 2(7)(e) | (e) in any other case, a person who, under the … | any other case: a person who under the constitution has the general control and management of the administration | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(8) | Article 2(8) | (8) For the purpose of paragraph (7)(d) a relevant unincorporated … | a "relevant unincorporated entity" for 2(7)(d) | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(8)(a) | Article 2(8)(a) | (a) falls within paragraph (1)(i); and | falls within 2(1)(i) | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(8)(b) | Article 2(8)(b) | (b) has a constitution that conforms to a model that … | has a constitution conforming to a model published by the Commissioner that provides for a management committee | encoded | g1-art2-governor-misconduct | G1 | note: "conforms to a model" is an input judgement |
| 2(8)(b)(i) | Article 2(8)(b)(i) | (i) is published for the purpose by the Commissioner, and | the model is published for the purpose by the Commissioner | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(8)(b)(ii) | Article 2(8)(b)(ii) | (ii) provides for the entity to have a management committee. | the model provides for the entity to have a management committee | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(9) | Article 2(9) | (9) For the purpose of paragraph (7)(e) – | two clarifications of governor under 2(7)(e) | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(9)(a) | Article 2(9)(a) | (a) a person is not a governor merely by virtue … | a person exercising control on behalf of another who has it in own right is not a governor merely for that | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(9)(b) | Article 2(9)(b) | (b) a person is a governor whether that person has … | a person is a governor whether having control and management alone or as one of a number | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(10) | Article 2(10) | (10) In this Law, unless the context otherwise requires, “misconduct” … | "misconduct": contravention by a registered charity or governor, or an offence by any person in relation to a charity | encoded | g1-art2-governor-misconduct | G1 | note: needs the input "has contravened a provision of this Law" (IP13) |
| 2(10)(a) | Article 2(10)(a) | (a) a contravention, by a registered charity or by any … | a contravention by a registered charity or any of its governors of one of four kinds of provision | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(10)(a)(i) | Article 2(10)(a)(i) | (i) of this Law, or of any enactment under this … | a provision of this Law or of any enactment under it | encoded | g1-art2-governor-misconduct | G1 | note: contravention is an input fact (breach is computed by the group that owns each duty) |
| 2(10)(a)(ii) | Article 2(10)(a)(ii) | (ii) of the constitution of the registered charity, or of … | a provision of the charity's constitution or constitutional Law | encoded | g1-art2-governor-misconduct | G1 | note: constitutional Law is MAYBE (T6) |
| 2(10)(a)(iii) | Article 2(10)(a)(iii) | (iii) of a required steps notice, or | a provision of a required steps notice | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(10)(a)(iv) | Article 2(10)(a)(iv) | (iv) of an order of the court under this Law … | an order of the court under this Law or the constitutional Law or an enactment under such a Law | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(10)(b) | Article 2(10)(b) | (b) the commission by any person, in relation a registered … | commission by any person, in relation to a registered charity, excepted foreign charity or foreign equivalent, of an offence of six kinds | encoded | g1-art2-governor-misconduct | G1 | note: "in relation to": fork F1.2 |
| 2(10)(b)(i) | Article 2(10)(b)(i) | (i) under the constitutional Law of that charity or other … | an offence under the constitutional Law of that charity or other entity | encoded | g1-art2-governor-misconduct | G1 |  |
| 2(10)(b)(ii) | Article 2(10)(b)(ii) | (ii) under the Financial Services (Jersey) Law 1998, the Banking … | an offence under the financial services Laws (named), Regulations or Orders under them, or the Alternative Investment Funds (Jersey) Regulations 2012 | encoded | g1-art2-governor-misconduct | G1 | note: the named Laws are out of scope; whether an offence falls here is an input |
| 2(10)(b)(iii) | Article 2(10)(b)(iii) | (iii) under the Income Tax (Jersey) Law 1961, the Goods … | an offence under the Income Tax (Jersey) Law 1961, the Goods and Services Tax (Jersey) Law 2007 or the Taxation (Land Transactions) (Jersey) Law 2009 | encoded | g1-art2-governor-misconduct | G1 | note: the named Laws are out of scope; an input |
| 2(10)(b)(iv) | Article 2(10)(b)(iv) | (iv) under any other enactment, being an offence relating to … | an offence under any other enactment relating to money laundering or terrorist financing | encoded | g1-art2-governor-misconduct | G1 | note: an input |
| 2(10)(b)(v) | Article 2(10)(b)(v) | (v) under any other enactment or under customary law, being … | an offence under any other enactment or customary law involving deception or dishonesty | encoded | g1-art2-governor-misconduct | G1 | note: an input |
| 2(10)(b)(vi) | Article 2(10)(b)(vi) | (vi) under the law of a jurisdiction other than Jersey, … | an offence under the law of another jurisdiction similar to those in "clauses (i) to (v)" | encoded | g1-art2-governor-misconduct | G1 | note: says "clauses", elsewhere "sub-paragraphs"; an input judgement of similarity |
| 3 | Article 3 | 3 Establishment of Jersey Charity Commissioner | Article 3: the Jersey Charity Commissioner is established | inert | g2-art3-4-commissioner | G2 | constitutive; no rule to compute; the office is an input fact |
| 3(1) | Article 3(1) | (1) There is established a corporation sole to be known … | there is established a corporation sole, the Jersey Charity Commissioner | inert | g2-art3-4-commissioner | G2 | establishes the office; carried by the actor constructor `the Commissioner` |
| 3(2) | Article 3(2) | (2) Schedule 1 makes further provision in respect of the … | Schedule 1 makes further provision | inert | g2-art3-4-commissioner | G2 | pointer to Schedule 1 (G9) |
| 4 | Article 4 | 4 General functions of Commissioner | Article 4: general functions of the Commissioner | encoded | g2-art3-4-commissioner | G2 |  |
| 4(1) | Article 4(1) | (1) The general functions of the Commissioner are – | the general functions of the Commissioner | encoded | g2-art3-4-commissioner | G2 | note: list of functions; the duty at (d) is encoded, the others are statements of function |
| 4(1)(a) | Article 4(1)(a) | (a) to administer the charity test under Part 3, and … | administer the charity test (Part 3) and operate the register (Part 4) | inert | g2-art3-4-commissioner | G2 | statement of function; the powers and duties are encoded in Parts 3 and 4 |
| 4(1)(b) | Article 4(1)(b) | (b) to supervise the compliance of charity governors with their … | supervise governors' compliance with Part 5 duties | inert | g2-art3-4-commissioner | G2 | statement of function; encoded in Part 5 |
| 4(1)(c) | Article 4(1)(c) | (c) to seek to enforce the requirements of Part 6 … | seek to enforce the Part 6 restrictions on terms | inert | g2-art3-4-commissioner | G2 | statement of function; no preconditions or outcomes; prosecution is not conferred by the Law |
| 4(1)(d) | Article 4(1)(d) | (d) to publish and maintain guidance on the operation of … | publish and maintain guidance on the operation of the Law, including governors' duties and the charity test | encoded | g2-art3-4-commissioner | G2 | note: a duty with no deadline: MUST publish and maintain; "publish" is the Article 1 definition |
| 4(1)(e) | Article 4(1)(e) | (e) to assist other persons (including the Attorney General, the … | assist other persons (Attorney General, court, Bailiff, Comptroller, JFSC) in their functions, particularly by giving information under Part 7 | inert | g2-art3-4-commissioner | G2 | open-textured function with no preconditions; the disclosure rules are encoded at 29 to 31 |
| 4(1)(f) | Article 4(1)(f) | (f) generally to encourage, facilitate and monitor compliance of registered … | encourage, facilitate and monitor compliance of registered charities | inert | g2-art3-4-commissioner | G2 | open-textured function; no outcome to compute |
| 4(1)(g) | Article 4(1)(g) | (g) any other function conferred on the Commissioner by this … | any other function conferred by this Law or another enactment | inert | g2-art3-4-commissioner | G2 | residual; no rule |
| 4(2) | Article 4(2) | (2) The Commissioner may do anything (other than acting as … | the Commissioner may do anything calculated to facilitate or conducive to the functions, other than act as a governor of a charity or of an entity with charitable purposes | encoded | g2-art3-4-commissioner | G2 | note: a permission with one exclusion |
| 4(3) | Article 4(3) | (3) The Commissioner may in particular, without prejudice to the … | in particular, without prejudice to generality, three kinds of thing | inert | g2-art3-4-commissioner | G2 | illustrations of 4(2); add nothing to it |
| 4(3)(a) | Article 4(3)(a) | (a) provide information to the public about the system of … | provide information to the public about registration, including model constitutions | inert | g2-art3-4-commissioner | G2 | illustration of 4(2) |
| 4(3)(b) | Article 4(3)(b) | (b) advise the Minister as to the nature of charities … | advise the Minister about charities and further regulation | inert | g2-art3-4-commissioner | G2 | illustration of 4(2) |
| 4(3)(c) | Article 4(3)(c) | (c) assist a body in any jurisdiction other than Jersey, … | assist an equivalent foreign body or the Attorney General, court, Comptroller or JFSC elsewhere | inert | g2-art3-4-commissioner | G2 | illustration of 4(2) |
| 4(4) | Article 4(4) | (4) In performing his or her functions, the Commissioner must, … | in performing functions the Commissioner must, so far as reasonably practicable, seek to act in a way that protects trust and is proportionate | encoded | g2-art3-4-commissioner | G2 | note: a standard of conduct: the Commissioner's judgement is an input |
| 4(4)(a) | Article 4(4)(a) | (a) protects public trust and confidence in registered charities, and … | protects public trust and confidence in registered charities and is compatible with encouraging charitable giving and voluntary participation | encoded | g2-art3-4-commissioner | G2 | note: limb of the recorded determination |
| 4(4)(a)(i) | Article 4(4)(a)(i) | (i) all forms of charitable giving, and | compatible with encouragement of all forms of charitable giving | encoded | g2-art3-4-commissioner | G2 |  |
| 4(4)(a)(ii) | Article 4(4)(a)(ii) | (ii) voluntary participation in the work of registered charities; and | compatible with encouragement of voluntary participation in the work of registered charities | encoded | g2-art3-4-commissioner | G2 |  |
| 4(4)(b) | Article 4(4)(b) | (b) is proportionate as to the burdens imposed on, and … | is proportionate as to burdens imposed on, and supports the development of, registered charities | encoded | g2-art3-4-commissioner | G2 | note: limb of the recorded determination |
| 5 | Article 5 | 5 The charity test | Article 5: the charity test | encoded | g2-art5-charity-test | G2 |  |
| 5(1) | Article 5(1) | (1) An entity meets the charity test if – | an entity meets the charity test if all its purposes are charitable or purely ancillary, and it provides public benefit to a reasonable degree | encoded | g2-art5-charity-test | G2 |  |
| 5(1)(a) | Article 5(1)(a) | (a) all of its purposes are – | all of its purposes are charitable purposes or purely ancillary or incidental to any of them | encoded | g2-art5-charity-test | G2 | note: "all": fork F2.1 |
| 5(1)(a)(i) | Article 5(1)(a)(i) | (i) charitable purposes, or | charitable purposes | encoded | g2-art5-charity-test | G2 |  |
| 5(1)(a)(ii) | Article 5(1)(a)(ii) | (ii) purposes that are purely ancillary or incidental to any … | purposes purely ancillary or incidental to any of its charitable purposes | encoded | g2-art5-charity-test | G2 |  |
| 5(1)(b) | Article 5(1)(b) | (b) in giving effect to those purposes, it provides (or, … | in giving effect to its purposes it provides (an applicant: provides or intends to provide) public benefit in Jersey or elsewhere to a reasonable degree | encoded | g2-art5-charity-test | G2 | note: "to a reasonable degree" is an input judgement |
| 5(2) | Article 5(2) | (2) An entity that otherwise meets the charity test, nevertheless … | an entity that otherwise meets the test does not if its constitution expressly permits control by, or a governor to be, a Minister, a member of the States Assembly or an equivalent, acting in that capacity | encoded | g2-art5-charity-test | G2 | note: forks F2.2, F2.3 |
| 5(2)(a) | Article 5(2)(a) | (a) a Minister; | a Minister | encoded | g2-art5-charity-test | G2 | note: generic office or the defined term "Minister": fork F2.3 |
| 5(2)(b) | Article 5(2)(b) | (b) a member of the States Assembly; or | a member of the States Assembly | encoded | g2-art5-charity-test | G2 |  |
| 5(2)(c) | Article 5(2)(c) | (c) any equivalent of such a person in another jurisdiction, | any equivalent of such a person in another jurisdiction | encoded | g2-art5-charity-test | G2 |  |
| 5(3) | Article 5(3) | (3) The Minister may by Order disapply paragraph (2) in … | the Minister may by Order disapply 5(2) for an entity or description of entity | encoded | g2-art5-charity-test | G2 | note: power typed MAY (the Minister); the Order's content is an input; feeds 8(3)(i) |
| 5(4) | Article 5(4) | (4) The Commissioner must publish and maintain guidance on the … | the Commissioner must publish and maintain guidance on whether an entity meets the charity test | encoded | g2-art5-charity-test | G2 | note: a duty with no deadline |
| 5(5) | Article 5(5) | (5) Any person, in determining whether an entity meets the … | any person determining the test must have regard to the guidance; the Commissioner, tribunal, registered charity and governor must have regard when performing other functions | encoded | g2-art5-charity-test | G2 | note: "have regard" is a recorded fact (input) |
| 5(6) | Article 5(6) | (6) Before issuing or amending guidance the Commissioner must – | before issuing or amending guidance the Commissioner must consult and publish a report | encoded | g2-art5-charity-test | G2 |  |
| 5(6)(a) | Article 5(6)(a) | (a) consult – | consult representatives of charities, the Minister, and others the Commissioner considers appropriate | encoded | g2-art5-charity-test | G2 |  |
| 5(6)(a)(i) | Article 5(6)(a)(i) | (i) any persons appearing to the Commissioner to be representative … | persons appearing to the Commissioner to be representative of charities or bodies with charitable purposes | encoded | g2-art5-charity-test | G2 |  |
| 5(6)(a)(ii) | Article 5(6)(a)(ii) | (ii) the Minister, and | the Minister | encoded | g2-art5-charity-test | G2 |  |
| 5(6)(a)(iii) | Article 5(6)(a)(iii) | (iii) such other persons as the Commissioner considers appropriate; and | such other persons as the Commissioner considers appropriate | encoded | g2-art5-charity-test | G2 |  |
| 5(6)(b) | Article 5(6)(b) | (b) publish a report on the Commissioner’s views on the … | publish a report on the views on the consultation and the reasons for the decision | encoded | g2-art5-charity-test | G2 |  |
| 5(7) | Article 5(7) | (7) Within a reasonable time after issuing or amending guidance … | within a reasonable time after issuing or amending guidance, give the Minister the guidance and the report | encoded | g2-art5-charity-test | G2 | note: period "a reasonable time": fork F2.4 |
| 5(8) | Article 5(8) | (8) The Minister must lay a copy of the guidance … | the Minister must lay the guidance and report before the States as soon as practicable | encoded | g2-art5-charity-test | G2 | note: period "as soon as practicable": fork F2.4 |
| 6 | Article 6 | 6 Charitable purposes | Article 6: charitable purposes | encoded | g2-art6-purposes | G2 |  |
| 6(1) | Article 6(1) | (1) For the purposes of this Law, the charitable purposes … | the charitable purposes are sixteen heads | encoded | g2-art6-purposes | G2 |  |
| 6(1)(a) | Article 6(1)(a) | (a) the prevention or relief of poverty; | the prevention or relief of poverty | encoded | g2-art6-purposes | G2 |  |
| 6(1)(b) | Article 6(1)(b) | (b) the advancement of education; | the advancement of education | encoded | g2-art6-purposes | G2 |  |
| 6(1)(c) | Article 6(1)(c) | (c) the advancement of religion; | the advancement of religion | encoded | g2-art6-purposes | G2 | note: feeds Article 28(1)(a) (IP11) |
| 6(1)(d) | Article 6(1)(d) | (d) the advancement of health; | the advancement of health | encoded | g2-art6-purposes | G2 | note: extended by 6(2)(a) |
| 6(1)(e) | Article 6(1)(e) | (e) the saving of lives; | the saving of lives | encoded | g2-art6-purposes | G2 |  |
| 6(1)(f) | Article 6(1)(f) | (f) the advancement of citizenship or community development; | the advancement of citizenship or community development | encoded | g2-art6-purposes | G2 | note: extended by 6(2)(b) |
| 6(1)(g) | Article 6(1)(g) | (g) the advancement of the arts, heritage, culture or science; | the advancement of the arts, heritage, culture or science | encoded | g2-art6-purposes | G2 |  |
| 6(1)(h) | Article 6(1)(h) | (h) the advancement of public participation in sport; | the advancement of public participation in sport | encoded | g2-art6-purposes | G2 | note: narrowed by 6(2)(c) |
| 6(1)(i) | Article 6(1)(i) | (i) the provision of recreational facilities, or the organisation of … | recreational facilities or activities to improve conditions of life for those they are intended for | encoded | g2-art6-purposes | G2 | note: limited by 6(2)(d) |
| 6(1)(j) | Article 6(1)(j) | (j) the advancement of human rights, conflict resolution or reconciliation; | the advancement of human rights, conflict resolution or reconciliation | encoded | g2-art6-purposes | G2 |  |
| 6(1)(k) | Article 6(1)(k) | (k) the promotion of religious or racial harmony; | the promotion of religious or racial harmony | encoded | g2-art6-purposes | G2 |  |
| 6(1)(l) | Article 6(1)(l) | (l) the promotion of equality and diversity; | the promotion of equality and diversity | encoded | g2-art6-purposes | G2 |  |
| 6(1)(m) | Article 6(1)(m) | (m) the advancement of environmental protection or improvement; | the advancement of environmental protection or improvement | encoded | g2-art6-purposes | G2 |  |
| 6(1)(n) | Article 6(1)(n) | (n) the relief of those in need by reason of … | the relief of those in need by reason of age, ill-health, disability, financial hardship or other disadvantage | encoded | g2-art6-purposes | G2 | note: extended by 6(2)(e) |
| 6(1)(o) | Article 6(1)(o) | (o) the advancement of animal welfare; | the advancement of animal welfare | encoded | g2-art6-purposes | G2 |  |
| 6(1)(p) | Article 6(1)(p) | (p) any other purpose that may reasonably be regarded as … | any other purpose that may reasonably be regarded as analogous to (a) to (o) | encoded | g2-art6-purposes | G2 | note: "may reasonably be regarded" is an input judgement; 6(2)(f) deems one analogy |
| 6(2) | Article 6(2) | (2) For the purposes of paragraph (1) – | clarifications of the heads in (1) | encoded | g2-art6-purposes | G2 |  |
| 6(2)(a) | Article 6(2)(a) | (a) in paragraph (1)(d), “the advancement of health” includes the … | "the advancement of health" includes the prevention or relief of sickness, disease or human suffering | encoded | g2-art6-purposes | G2 |  |
| 6(2)(b) | Article 6(2)(b) | (b) paragraph (1)(f) includes – | (1)(f) includes regeneration and promotion of civic responsibility, volunteering, the voluntary sector, effectiveness of registered charities | encoded | g2-art6-purposes | G2 |  |
| 6(2)(b)(i) | Article 6(2)(b)(i) | (i) rural or urban regeneration, and | rural or urban regeneration | encoded | g2-art6-purposes | G2 |  |
| 6(2)(b)(ii) | Article 6(2)(b)(ii) | (ii) the promotion of civic responsibility, volunteering, the voluntary sector … | promotion of civic responsibility, volunteering, the voluntary sector or the effectiveness or efficiency of registered charities | encoded | g2-art6-purposes | G2 |  |
| 6(2)(c) | Article 6(2)(c) | (c) in paragraph (1)(h), “sport” means sport that involves physical … | "sport" means sport that involves physical skill and exertion | encoded | g2-art6-purposes | G2 |  |
| 6(2)(d) | Article 6(2)(d) | (d) paragraph (1)(i) applies only in relation to recreational facilities … | (1)(i) applies only to facilities or activities for people in need by reason of disadvantage, or open to the public at large or to male or female members of it | encoded | g2-art6-purposes | G2 |  |
| 6(2)(d)(i) | Article 6(2)(d)(i) | (i) primarily intended for persons who have need of them … | primarily intended for persons who need them by reason of age, ill-health, disability, financial hardship or other disadvantage | encoded | g2-art6-purposes | G2 |  |
| 6(2)(d)(ii) | Article 6(2)(d)(ii) | (ii) available to members of the public at large or … | available to members of the public at large or to male or female members of the public at large | encoded | g2-art6-purposes | G2 |  |
| 6(2)(e) | Article 6(2)(e) | (e) paragraph (1)(n) includes relief given by the provision of … | (1)(n) includes relief given by provision of accommodation or care | encoded | g2-art6-purposes | G2 |  |
| 6(2)(f) | Article 6(2)(f) | (f) for the purposes of paragraph (1)(p), the advancement of … | for (1)(p), the advancement of any philosophical belief is analogous to the purpose in (1)(c) | encoded | g2-art6-purposes | G2 | note: a philosophical-belief purpose is within (p), not (c): fork F2.5, feeds fork F8.3 |
| 6(3) | Article 6(3) | (3) The States may, on the recommendation of the Commissioner, … | the States, on the Commissioner's recommendation, may by Regulations add sub-paragraphs to (1) and explanatory ones to (2) | encoded | g2-art6-purposes | G2 | note: power typed MAY (the States); the Regulations are not in the sources |
| 6(3)(a) | Article 6(3)(a) | (a) add sub-paragraphs to paragraph (1); | add sub-paragraphs to paragraph (1) | encoded | g2-art6-purposes | G2 |  |
| 6(3)(b) | Article 6(3)(b) | (b) add sub-paragraphs to paragraph (2) making explanatory provision in … | add sub-paragraphs to paragraph (2) explaining the added ones | encoded | g2-art6-purposes | G2 |  |
| 6(4) | Article 6(4) | (4) The power under paragraph (3) does not include power … | the power in (3) cannot amend or restrict (1)(a) to (p) or (2)(a) to (f), or alter (5) | encoded | g2-art6-purposes | G2 | note: a limit on the content of the Regulations |
| 6(4)(a) | Article 6(4)(a) | (a) to amend or restrict the effect of any of … | to amend or restrict the effect of 6(1)(a) to (p) and 6(2)(a) to (f) | encoded | g2-art6-purposes | G2 |  |
| 6(4)(b) | Article 6(4)(b) | (b) to alter the effect of paragraph (5). | to alter the effect of paragraph (5) | encoded | g2-art6-purposes | G2 |  |
| 6(5) | Article 6(5) | (5) The purpose of advancing a political party or promoting … | advancing a political party or promoting a candidate is neither a charitable purpose nor an ancillary one | encoded | g2-art6-purposes | G2 | note: overrides 5(1)(a)(ii) as well as 6(1) |
| 7 | Article 7 | 7 Public benefit | Article 7: public benefit | encoded | g2-art7-public-benefit | G2 |  |
| 7(1) | Article 7(1) | (1) Paragraphs (2) and (3) apply to the Commissioner, the … | (2) and (3) bind the Commissioner, the tribunal and the court when deciding public benefit for 5(1)(b) | encoded | g2-art7-public-benefit | G2 | note: does not bind "any person" under 5(5), only guided by guidance |
| 7(2) | Article 7(2) | (2) The person determining the question must have regard to … | the decision-maker must have regard to the comparison of private benefit and public disbenefit with public benefit, and to restrictive conditions | encoded | g2-art7-public-benefit | G2 | note: "have regard" is a recorded fact |
| 7(2)(a) | Article 7(2)(a) | (a) how any – | how benefit to members or others (other than as the public) and disbenefit to the public compares with benefit to the public | encoded | g2-art7-public-benefit | G2 |  |
| 7(2)(a)(i) | Article 7(2)(a)(i) | (i) benefit gained or likely to be gained by members … | benefit gained or likely to be gained by members or other persons other than as members of the public | encoded | g2-art7-public-benefit | G2 |  |
| 7(2)(a)(ii) | Article 7(2)(a)(ii) | (ii) disbenefit incurred or likely to be incurred by the … | disbenefit incurred or likely to be incurred by the public | encoded | g2-art7-public-benefit | G2 |  |
| 7(2)(b) | Article 7(2)(b) | (b) if benefit is, or is likely to be, provided … | if benefit goes to a section of the public only, whether any condition, including a charge or fee, is unduly restrictive | encoded | g2-art7-public-benefit | G2 |  |
| 7(3) | Article 7(3) | (3) The person determining the question must not – | the decision-maker must not presume public benefit or treat identified persons as a section of the public | encoded | g2-art7-public-benefit | G2 |  |
| 7(3)(a) | Article 7(3)(a) | (a) presume any particular charitable purpose to be for the … | presume any particular charitable purpose to be for the public benefit | encoded | g2-art7-public-benefit | G2 |  |
| 7(3)(b) | Article 7(3)(b) | (b) treat one particular natural person or a group of … | treat one natural person or a group of identified natural persons as a section of the public, and so not treat an entity benefiting only them as providing public benefit | encoded | g2-art7-public-benefit | G2 |  |
| 7(4) | Article 7(4) | (4) The guidance published by the Commissioner under Article 5(4), … | the guidance under 5(4) must give guidance on public benefit | encoded | g2-art7-public-benefit | G2 | note: a limit on the content of the guidance |
| 8 | Article 8 | 8 Charity register | Article 8: the charity register | encoded | g3-art8-register | G3 |  |
| 8(1) | Article 8(1) | (1) The Commissioner must establish and maintain a register of … | the Commissioner must establish and maintain a register of charities | encoded | g3-art8-register | G3 |  |
| 8(2) | Article 8(2) | (2) The register must be kept in such a way … | the register must distinguish the general, restricted and historic sections | encoded | g3-art8-register | G3 | note: the historic section is not defined in Article 1: trap T7 |
| 8(2)(a) | Article 8(2)(a) | (a) the general section; | the general section | encoded | g3-art8-register | G3 |  |
| 8(2)(b) | Article 8(2)(b) | (b) the restricted section; and | the restricted section | encoded | g3-art8-register | G3 |  |
| 8(2)(c) | Article 8(2)(c) | (c) the historic section. | the historic section | encoded | g3-art8-register | G3 |  |
| 8(3) | Article 8(3) | (3) The Commissioner must enter in the register, in respect … | the Commissioner must enter, for each registered charity, fourteen items in addition to name and number | encoded | g3-art8-register | G3 |  |
| 8(3)(a) | Article 8(3)(a) | (a) a note of the status of the entity that … | a note of the status of the entity | encoded | g3-art8-register | G3 |  |
| 8(3)(a)(i) | Article 8(3)(a)(i) | (i) the sub-paragraph of the definition “entity” in Article 2(1) … | the sub-paragraph(s) of 2(1) within which it falls, and for (f) to (j) whether it also falls within (a) | encoded | g3-art8-register | G3 | note: (ba) is not listed in the range of this sub-paragraph's second limb |
| 8(3)(a)(ii) | Article 8(3)(a)(ii) | (ii) in the case of an entity falling within one … | for (e), (g), (h) or (j), details of the enactment, Act, Charter, Order in Council or foreign law by virtue of which it falls there | encoded | g3-art8-register | G3 | note: (ba) is not listed |
| 8(3)(b) | Article 8(3)(b) | (b) the names of each of the governors of the … | the names of each of the governors | encoded | g3-art8-register | G3 |  |
| 8(3)(c) | Article 8(3)(c) | (c) the principal address of the registered charity with the … | the principal address, as defined in 8(4) | encoded | g3-art8-register | G3 |  |
| 8(3)(d) | Article 8(3)(d) | (d) the address of any other premises in Jersey, other … | the address of any other premises in Jersey, other than a private dwelling house, from which it undertakes any activity | encoded | g3-art8-register | G3 |  |
| 8(3)(e) | Article 8(3)(e) | (e) a statement of the purposes of the registered charity … | a statement of the charity's purposes drawn from its constitution and approved by the Commissioner as accurate | encoded | g3-art8-register | G3 | note: defines "registered charitable purposes" |
| 8(3)(f) | Article 8(3)(f) | (f) a statement (the charity’s “registered public benefit statement”), approved … | a statement of the public benefit provided and how, approved by the Commissioner | encoded | g3-art8-register | G3 | note: defines "registered public benefit statement" |
| 8(3)(g) | Article 8(3)(g) | (g) the date on which the charity was registered; | the date on which the charity was registered | encoded | g3-art8-register | G3 |  |
| 8(3)(h) | Article 8(3)(h) | (h) if the registered charity is an organized religious charity, … | if an organized religious charity, a note of that fact and of the provision of the Order by which it is one | encoded | g3-art8-register | G3 | note: IP20 |
| 8(3)(i) | Article 8(3)(i) | (i) if the registered charity meets the charity test by … | if it meets the charity test by virtue of an Order under 5(3), the text of the constitution provision in 5(2) | encoded | g3-art8-register | G3 | note: IP10 |
| 8(3)(j) | Article 8(3)(j) | (j) whether the registered charity has or has not sent … | whether it has or has not sent its annual return for the most recent year | encoded | g3-art8-register | G3 | note: "the most recent year": fork F3.2 |
| 8(3)(k) | Article 8(3)(k) | (k) if a required steps notice has been served on … | if a required steps notice has been served on the charity or a governor, a note or copy of it and the date of service | encoded | g3-art8-register | G3 |  |
| 8(3)(l) | Article 8(3)(l) | (l) if the registered name has been changed, the previous … | if the registered name has changed, the previous names | encoded | g3-art8-register | G3 |  |
| 8(3)(m) | Article 8(3)(m) | (m) if an Order under Article 13(9)(c) applies to the … | if an Order under 13(9)(c) applies, the details or statement the Order requires | encoded | g3-art8-register | G3 | note: IP29 |
| 8(3)(n) | Article 8(3)(n) | (n) any other information prescribed by the Minister by Order. | any other information the Minister prescribes by Order | encoded | g3-art8-register | G3 | note: power typed MAY (the Minister) |
| 8(4) | Article 8(4) | (4) The principal address for the purpose of paragraph (3)(c) … | the "principal address" for 8(3)(c) | encoded | g3-art8-register | G3 |  |
| 8(4)(a) | Article 8(4)(a) | (a) if the registered charity is a company, foundation, or … | a company, foundation or other entity required by its constitutional Law to have a registered office or business address in Jersey: that address | encoded | g3-art8-register | G3 |  |
| 8(4)(b) | Article 8(4)(b) | (b) if the charity is not such an entity, the … | otherwise: the address of the main premises in Jersey from which its Jersey activities are managed, unless a private dwelling house | encoded | g3-art8-register | G3 |  |
| 8(4)(c) | Article 8(4)(c) | (c) if neither sub-paragraph (a) nor (b) applies, the address … | otherwise: the address in Jersey of one of the governors | encoded | g3-art8-register | G3 |  |
| 8(5) | Article 8(5) | (5) The Commissioner must enter in the historic section, in … | the Commissioner must enter in the historic section, for a deregistered charity, five items | encoded | g3-art8-register | G3 |  |
| 8(5)(a) | Article 8(5)(a) | (a) the entity’s former registered number; | the former registered number | encoded | g3-art8-register | G3 |  |
| 8(5)(b) | Article 8(5)(b) | (b) if the entity was registered in the general section, … | if registered in the general section, the name immediately before deregistration and earlier names | encoded | g3-art8-register | G3 | note: restricted-section charities' names are not entered |
| 8(5)(c) | Article 8(5)(c) | (c) a summary of the reason why the entity was … | a summary of the reason for deregistration, including the reason for a contravened required steps notice | encoded | g3-art8-register | G3 |  |
| 8(5)(d) | Article 8(5)(d) | (d) the dates on which the entity was registered and … | the dates of registration and deregistration | encoded | g3-art8-register | G3 |  |
| 8(5)(e) | Article 8(5)(e) | (e) such other matters as the Minister may prescribe by … | other matters the Minister prescribes by Order | encoded | g3-art8-register | G3 | note: power typed MAY (the Minister) |
| 8(6) | Article 8(6) | (6) The Commissioner must retain for 10 years, in respect … | the Commissioner must retain for 10 years, for each registered charity, a copy of four kinds of document | encoded | g3-art8-register | G3 | note: period "10 years": fork F3.1; no start date stated |
| 8(6)(a) | Article 8(6)(a) | (a) the constitution of the charity, and any amendments to … | the constitution and any amendments | encoded | g3-art8-register | G3 |  |
| 8(6)(b) | Article 8(6)(b) | (b) the annual returns of the charity; | the annual returns | encoded | g3-art8-register | G3 |  |
| 8(6)(c) | Article 8(6)(c) | (c) any notice served on the charity under this Law; … | any notice served on the charity under this Law | encoded | g3-art8-register | G3 |  |
| 8(6)(d) | Article 8(6)(d) | (d) any other document prescribed by the Minister by Order. | any other document the Minister prescribes by Order | encoded | g3-art8-register | G3 | note: power typed MAY (the Minister) |
| 9 | Article 9 | 9 Restricted section | Article 9: the restricted section | encoded | g3-art9-restricted-section | G3 |  |
| 9(1) | Article 9(1) | (1) For the purpose of Article 10 the public elements … | the public elements of the restricted section, for Article 10 | encoded | g3-art9-restricted-section | G3 |  |
| 9(1)(a) | Article 9(1)(a) | (a) the registration number (but not the registered name) of … | the registration number, but not the registered name | encoded | g3-art9-restricted-section | G3 |  |
| 9(1)(b) | Article 9(1)(b) | (b) the matters registered under sub-paragraphs (a), (e), (f), (j) … | the matters registered under 8(3)(a), (e), (f), (j) and (k) | encoded | g3-art9-restricted-section | G3 | note: includes the required steps notice note, 8(3)(k) |
| 9(1)(c) | Article 9(1)(c) | (c) a summary, produced by the charity, to the satisfaction … | a summary, produced by the charity to the Commissioner's satisfaction, of the reasons for restricted registration | encoded | g3-art9-restricted-section | G3 |  |
| 9(1)(d) | Article 9(1)(d) | (d) any other element that may be prescribed by the … | any other element the Minister prescribes by Order | encoded | g3-art9-restricted-section | G3 | note: power typed MAY (the Minister) |
| 9(2) | Article 9(2) | (2) An applicant for registration, or a charity registered in … | an applicant or a general-section charity may request entry in the restricted section if it meets a prescribed condition | encoded | g3-art9-restricted-section | G3 |  |
| 9(2)(a) | Article 9(2)(a) | (a) the applicant meets the funding condition, prescribed by the … | the funding condition prescribed by Order: refraining from soliciting donations from the general public or a prescribed description of persons | encoded | g3-art9-restricted-section | G3 | note: the condition is an input; power typed MAY (the Minister) |
| 9(2)(b) | Article 9(2)(b) | (b) the applicant meets any other condition that may be … | any other condition the Minister prescribes by Order | encoded | g3-art9-restricted-section | G3 | note: an input |
| 9(3) | Article 9(3) | (3) The Order – | what the Order must and may contain | encoded | g3-art9-restricted-section | G3 | note: a limit on the content of the Order |
| 9(3)(a) | Article 9(3)(a) | (a) must prescribe grounds, that may include the exercise of … | must prescribe grounds, which may include the Commissioner's discretion, on which a request may be accepted or refused | encoded | g3-art9-restricted-section | G3 |  |
| 9(3)(b) | Article 9(3)(b) | (b) must specify, for the purpose of paragraph (2)(a) – | must specify, for 9(2)(a), what is soliciting, what is a donation, and what is the general public | encoded | g3-art9-restricted-section | G3 |  |
| 9(3)(b)(i) | Article 9(3)(b)(i) | (i) what constitutes soliciting, | what constitutes soliciting | encoded | g3-art9-restricted-section | G3 | note: defines "solicit" (Article 1) |
| 9(3)(b)(ii) | Article 9(3)(b)(ii) | (ii) what constitutes a donation, and | what constitutes a donation | encoded | g3-art9-restricted-section | G3 | note: defines "donation" (Article 1) |
| 9(3)(b)(iii) | Article 9(3)(b)(iii) | (iii) if the Order does not prescribe a description of … | if no description of persons is prescribed, what constitutes the general public | encoded | g3-art9-restricted-section | G3 |  |
| 9(3)(c) | Article 9(3)(c) | (c) may make provision under sub-paragraph (b) by reference to … | may make that provision by reference to the Commissioner's discretion or otherwise | encoded | g3-art9-restricted-section | G3 |  |
| 9(4) | Article 9(4) | (4) A request under paragraph (2) must be – | a request must be in the published form and supported by information and evidence to the Commissioner's satisfaction | encoded | g3-art9-restricted-section | G3 |  |
| 9(4)(a) | Article 9(4)(a) | (a) made in the form published by the Commissioner; and | made in the form published by the Commissioner | encoded | g3-art9-restricted-section | G3 |  |
| 9(4)(b) | Article 9(4)(b) | (b) supported by information and evidence to the satisfaction of … | supported by information and evidence to the Commissioner's satisfaction | encoded | g3-art9-restricted-section | G3 |  |
| 9(5) | Article 9(5) | (5) A request under paragraph (2) must be accompanied by … | a request must state what the applicant intends if it is refused | encoded | g3-art9-restricted-section | G3 |  |
| 9(5)(a) | Article 9(5)(a) | (a) in the case of an application for registration – | an application: treated as withdrawn, or treated as an application for the general section | encoded | g3-art9-restricted-section | G3 |  |
| 9(5)(a)(i) | Article 9(5)(a)(i) | (i) that that application should be treated as withdrawn, or | the application should be treated as withdrawn | encoded | g3-art9-restricted-section | G3 |  |
| 9(5)(a)(ii) | Article 9(5)(a)(ii) | (ii) that it should be treated as an application for … | it should be treated as an application for the general section, on any further information required | encoded | g3-art9-restricted-section | G3 |  |
| 9(5)(b) | Article 9(5)(b) | (b) in the case of a charity registered in the … | a general-section charity: remain registered, or be treated as applying to deregister | encoded | g3-art9-restricted-section | G3 | note: ties to Article 15 |
| 9(5)(b)(i) | Article 9(5)(b)(i) | (i) that the charity should remain so registered, or | the charity should remain so registered | encoded | g3-art9-restricted-section | G3 |  |
| 9(5)(b)(ii) | Article 9(5)(b)(ii) | (ii) that the charity should be treated as applying to … | the charity should be treated as applying to be deregistered, on any further information required | encoded | g3-art9-restricted-section | G3 |  |
| 9(6) | Article 9(6) | (6) The Commissioner must not enter a charity in the … | the Commissioner must not enter a charity in the restricted section unless satisfied of three things | encoded | g3-art9-restricted-section | G3 | note: the Commissioner's satisfaction is an input |
| 9(6)(a) | Article 9(6)(a) | (a) that the request complied with paragraphs (4) and (5); | the request complied with 9(4) and (5) | encoded | g3-art9-restricted-section | G3 |  |
| 9(6)(b) | Article 9(6)(b) | (b) that one of the conditions prescribed under paragraph (2) … | one of the conditions prescribed under 9(2) is met | encoded | g3-art9-restricted-section | G3 | note: feeds 13(5)(a) |
| 9(6)(c) | Article 9(6)(c) | (c) that there is no ground, prescribed under paragraph (3), … | no prescribed ground requires refusal and, for a discretionary ground, the Commissioner does not consider refusal should be made | encoded | g3-art9-restricted-section | G3 |  |
| 9(7) | Article 9(7) | (7) If the Commissioner refuses a request, he or she … | if the Commissioner refuses a request | encoded | g3-art9-restricted-section | G3 |  |
| 9(7)(a) | Article 9(7)(a) | (a) must give written notice of the refusal to the … | must give written notice of the refusal to the applicant or charity | encoded | g3-art9-restricted-section | G3 | note: no time limit stated |
| 9(7)(b) | Article 9(7)(b) | (b) may proceed on the basis of the intention stated … | may proceed on the basis of the intention stated under 9(5) | encoded | g3-art9-restricted-section | G3 |  |
| 10 | Article 10 | 10 Public access | Article 10: public access to the register | encoded | g3-art10-public-access | G3 |  |
| 10(1) | Article 10(1) | (1) The Commissioner must make the public parts of the … | the Commissioner must make the public parts available on a website for inspection without charge | encoded | g3-art10-public-access | G3 |  |
| 10(2) | Article 10(2) | (2) The Minister may by Order provide for the Commissioner … | the Minister may by Order provide for other specified manners of access, on payment | encoded | g3-art10-public-access | G3 | note: power typed MAY (the Minister); charges are an input |
| 10(2)(a) | Article 10(2)(a) | (a) a specified charge; or | payment of a specified charge | encoded | g3-art10-public-access | G3 |  |
| 10(2)(b) | Article 10(2)(b) | (b) a charge determined and published by the Commissioner. | payment of a charge determined and published by the Commissioner | encoded | g3-art10-public-access | G3 |  |
| 10(3) | Article 10(3) | (3) For the purpose of paragraphs (1) and (2), the … | the public parts: the general section, the public elements of the restricted section, the historic section, subject to (5) | encoded | g3-art10-public-access | G3 |  |
| 10(3)(a) | Article 10(3)(a) | (a) the general section; | the general section | encoded | g3-art10-public-access | G3 |  |
| 10(3)(b) | Article 10(3)(b) | (b) the public elements of the restricted section, within the … | the public elements of the restricted section within Article 9(1) | encoded | g3-art10-public-access | G3 |  |
| 10(3)(c) | Article 10(3)(c) | (c) the historic section. | the historic section | encoded | g3-art10-public-access | G3 |  |
| 10(4) | Article 10(4) | (4) Paragraph (5) applies if the Commissioner considers, in relation … | (5) applies if the Commissioner considers public access to a matter would significantly endanger safety or security | encoded | g3-art10-public-access | G3 | note: the Commissioner's consideration is an input; "registered charity": fork F3.3 |
| 10(5) | Article 10(5) | (5) The Commissioner may designate that matter as not being … | the Commissioner may designate that matter as not a public part of the register | encoded | g3-art10-public-access | G3 | note: a permission (MAY) |
| 11 | Article 11 | 11 Application to register | Article 11: application to register | encoded | g4-art11-application | G4 |  |
| 11(1) | Article 11(1) | (1) An entity (“the applicant”), that wishes to have available … | an entity that wishes to have the advantages of registration may apply to be registered | encoded | g4-art11-application | G4 | note: a permission of the entity (MAY) |
| 11(2) | Article 11(2) | (2) The applicant must provide to the Commissioner, in such … | what the applicant must give the Commissioner, in the published form | encoded | g4-art11-application | G4 |  |
| 11(2)(a) | Article 11(2)(a) | (a) information and evidence, as at the time of the … | information and evidence, as at the application and as proposed once registered, on three matters | encoded | g4-art11-application | G4 |  |
| 11(2)(a)(i) | Article 11(2)(a)(i) | (i) how the entity meets the requirements of paragraphs (4)(c) … | how the entity meets 11(4)(c) and (d) | encoded | g4-art11-application | G4 |  |
| 11(2)(a)(ii) | Article 11(2)(a)(ii) | (ii) the matters that are required to be registered under … | the matters to be registered under 8(3)(a), (b) and (d) | encoded | g4-art11-application | G4 |  |
| 11(2)(a)(iii) | Article 11(2)(a)(iii) | (iii) if applicable, the matters that are required to be … | if applicable, the matters under 8(3)(h), (i), (m) and (n) | encoded | g4-art11-application | G4 |  |
| 11(2)(b) | Article 11(2)(b) | (b) a copy of the applicant’s constitution; | a copy of the applicant's constitution | encoded | g4-art11-application | G4 |  |
| 11(2)(c) | Article 11(2)(c) | (c) a draft of the proposed statement of the entity’s … | a draft of the proposed statement of registered charitable purposes | encoded | g4-art11-application | G4 |  |
| 11(2)(d) | Article 11(2)(d) | (d) a draft of the entity’s registered public benefit statement; | a draft of the registered public benefit statement | encoded | g4-art11-application | G4 |  |
| 11(2)(e) | Article 11(2)(e) | (e) details of – | details of four financial matters | encoded | g4-art11-application | G4 |  |
| 11(2)(e)(i) | Article 11(2)(e)(i) | (i) the applicant’s most recent, if any, financial accounts, | the applicant's most recent financial accounts, if any | encoded | g4-art11-application | G4 |  |
| 11(2)(e)(ii) | Article 11(2)(e)(ii) | (ii) any payment made to any governor of the entity … | any payment to a governor in the 12 months preceding the application, and, if a 13(9)(b) Order applies, a draft of the proposed statement | encoded | g4-art11-application | G4 | note: period "12 months preceding": forks F4.1, F4.2; two requirements in one item: trap T28 |
| 11(2)(e)(iii) | Article 11(2)(e)(iii) | (iii) any other financial information that would be required if … | any other financial information required for registration under the Non-Profit Organizations (Jersey) Law 2008 | encoded | g4-art11-application | G4 | note: the content of that Law is out of scope; an input |
| 11(2)(e)(iv) | Article 11(2)(e)(iv) | (iv) if the applicant is not requesting entry in the … | if not requesting the restricted section, further financial information the Minister prescribes by Order | encoded | g4-art11-application | G4 | note: an input |
| 11(2)(f) | Article 11(2)(f) | (f) such other information, documents and evidence as may be … | such other information as Regulations require or the Commissioner requests to decide the application | encoded | g4-art11-application | G4 |  |
| 11(2)(f)(i) | Article 11(2)(f)(i) | (i) required by Regulations under paragraph (3), or | required by Regulations under 11(3) | encoded | g4-art11-application | G4 |  |
| 11(2)(f)(ii) | Article 11(2)(f)(ii) | (ii) otherwise requested by the Commissioner in order to determine … | otherwise requested by the Commissioner in order to determine the application | encoded | g4-art11-application | G4 |  |
| 11(3) | Article 11(3) | (3) The States may by Regulations – | the States may by Regulations prescribe further information and the procedure | encoded | g4-art11-application | G4 | note: power typed MAY (the States); the Regulations are not in the sources |
| 11(3)(a) | Article 11(3)(a) | (a) prescribe other information, documents or evidence that must be … | prescribe other information, documents or evidence | encoded | g4-art11-application | G4 |  |
| 11(3)(b) | Article 11(3)(b) | (b) make further provision as to the procedure for making … | make further provision on the procedure for applying | encoded | g4-art11-application | G4 |  |
| 11(4) | Article 11(4) | (4) If the applicant complies with paragraph (2), with any … | if the applicant complies with 11(2), the Regulations and Article 19(5), the Commissioner must register if satisfied of six matters | encoded | g4-art11-application | G4 | note: a MUST that collides with 19(9)(c) and with a court order under 20(1)(c): trap T10, fork F4.4 |
| 11(4)(a) | Article 11(4)(a) | (a) the applicant meets the charity test, or will do … | the applicant meets the charity test, or will on registration | encoded | g4-art11-application | G4 | note: IP8 |
| 11(4)(b) | Article 11(4)(b) | (b) the constitution of the applicant is a written document; | its constitution is a written document | encoded | g4-art11-application | G4 | note: beside 2(4)(g) "in whatever form" |
| 11(4)(c) | Article 11(4)(c) | (c) the applicant – | the applicant is a Jersey entity or carries on a substantial activity in or from Jersey | encoded | g4-art11-application | G4 | note: IP15 |
| 11(4)(c)(i) | Article 11(4)(c)(i) | (i) is a Jersey entity, or | is a Jersey entity | encoded | g4-art11-application | G4 | note: IP5 |
| 11(4)(c)(ii) | Article 11(4)(c)(ii) | (ii) carries out, or intends to carry out, in or … | carries out, or intends to carry out, in or from within Jersey, an activity that is, in the Commissioner's opinion, substantial | encoded | g4-art11-application | G4 | note: the opinion is an input |
| 11(4)(d) | Article 11(4)(d) | (d) the applicant has a principal address in Jersey, within … | the applicant has a principal address in Jersey within 8(4) | encoded | g4-art11-application | G4 | note: IP16 |
| 11(4)(e) | Article 11(4)(e) | (e) the name of the applicant is not undesirable under … | the name is not undesirable under Article 12 | encoded | g4-art11-application | G4 | note: IP18 |
| 11(4)(f) | Article 11(4)(f) | (f) no other ground for refusal, prescribed under paragraph (7), … | no other ground prescribed under 11(7) applies or should be applied | encoded | g4-art11-application | G4 | note: the prescribed grounds are inputs |
| 11(5) | Article 11(5) | (5) If not so satisfied, the Commissioner must refuse to … | if not so satisfied, the Commissioner must refuse to register the applicant | encoded | g4-art11-application | G4 | note: does not cover a non-compliant application: trap T10, fork F4.3 |
| 11(6) | Article 11(6) | (6) For the purpose of paragraph (4)(c)(ii) – | guidance on whether an activity is substantial | encoded | g4-art11-application | G4 |  |
| 11(6)(a) | Article 11(6)(a) | (a) the Commissioner must publish and maintain guidance as to … | the Commissioner must publish and maintain guidance on determining whether an activity is substantial | encoded | g4-art11-application | G4 |  |
| 11(6)(b) | Article 11(6)(b) | (b) Articles 5(6) to (8) apply to that guidance as … | Articles 5(6) to (8) apply to that guidance | encoded | g4-art11-application | G4 |  |
| 11(6)(c) | Article 11(6)(c) | (c) the Commissioner must have regard to that guidance, in … | the Commissioner must have regard to that guidance | encoded | g4-art11-application | G4 |  |
| 11(6)(d) | Article 11(6)(d) | (d) a registered charity, a governor of a registered charity, … | a registered charity, a governor, the tribunal and the court must have regard to it in their functions | encoded | g4-art11-application | G4 |  |
| 11(7) | Article 11(7) | (7) The States may by Regulations prescribe further grounds on … | the States may by Regulations prescribe further grounds on which an application must or may be refused | encoded | g4-art11-application | G4 | note: power typed MAY (the States); grounds are inputs |
| 11(7)(a) | Article 11(7)(a) | (a) that the entity has only one governor, not being … | the entity has only one governor who is not carrying on a prescribed description of business as governor | encoded | g4-art11-application | G4 | note: an example the Regulations may include |
| 11(7)(b) | Article 11(7)(b) | (b) that a number or proportion of its governors are … | a number or proportion of governors are related to each other in prescribed ways | encoded | g4-art11-application | G4 | note: an example the Regulations may include |
| 11(8) | Article 11(8) | (8) The Minister may by Order – | the Minister may by Order make provision on decisions and relieve small applicants | encoded | g4-art11-application | G4 | note: power typed MAY (the Minister) |
| 11(8)(a) | Article 11(8)(a) | (a) make provision as to – | provide for the decision period and notification | encoded | g4-art11-application | G4 |  |
| 11(8)(a)(i) | Article 11(8)(a)(i) | (i) the period within which the Commissioner must make a … | the period within which the Commissioner must decide an application | encoded | g4-art11-application | G4 | note: no Order in the sources: a named refusal for any "late" query; anchor F4.2 |
| 11(8)(a)(ii) | Article 11(8)(a)(ii) | (ii) the notification to applicants of decisions and of reasons … | the notification of decisions and reasons for refusal | encoded | g4-art11-application | G4 |  |
| 11(8)(b) | Article 11(8)(b) | (b) after consulting the Commissioner and any body appearing to … | after consultation, disapply or modify 11(2) for a prescribed description of small applicant | encoded | g4-art11-application | G4 |  |
| 11(8)(b)(i) | Article 11(8)(b)(i) | (i) does not apply to a prescribed description of applicant … | that a provision of 11(2) does not apply to a prescribed description of applicant | encoded | g4-art11-application | G4 |  |
| 11(8)(b)(ii) | Article 11(8)(b)(ii) | (ii) applies to a prescribed description of applicant only subject … | that a provision applies only subject to a modification | encoded | g4-art11-application | G4 |  |
| 11(9) | Article 11(9) | (9) The Commissioner must – | the Commissioner must issue certificates of registration and of name change | encoded | g4-art11-application | G4 | note: no time limit stated |
| 11(9)(a) | Article 11(9)(a) | (a) on registering an entity as a charity, issue to … | on registering, a certificate confirming the registered name, number and date | encoded | g4-art11-application | G4 |  |
| 11(9)(b) | Article 11(9)(b) | (b) on entering on the register a new or alternative … | on entering a new or alternative name under 12(5), a further certificate | encoded | g4-art11-application | G4 |  |
| 11(10) | Article 11(10) | (10) An applicant for registration, if it is an entity … | an applicant required to be registered under the Non-Profit Organizations Law but not registered must provide extra information and request registration there | encoded | g4-art11-application | G4 | note: whether it is "required" is an input |
| 11(10)(a) | Article 11(10)(a) | (a) provide with the application any additional information that must … | provide any additional information that must be provided to the JFSC for registration under that Law | encoded | g4-art11-application | G4 |  |
| 11(10)(b) | Article 11(10)(b) | (b) request to be registered under that Law (by virtue … | request to be registered under that Law (by virtue of 11(11)) | encoded | g4-art11-application | G4 |  |
| 11(11) | Article 11(11) | (11) If the Commissioner receives information and a request under … | on receiving the information and request | encoded | g4-art11-application | G4 | note: a duty on the Commissioner and on the JFSC |
| 11(11)(a) | Article 11(11)(a) | (a) the Commissioner must pass to the JFSC that request, … | the Commissioner must pass the request, information and documents to the JFSC | encoded | g4-art11-application | G4 |  |
| 11(11)(b) | Article 11(11)(b) | (b) the JFSC must treat that request, with the information … | the JFSC must treat the request as an application for registration under that Law | encoded | g4-art11-application | G4 | note: a duty on another body; the Law of that body is out of scope |
| 12 | Article 12 | 12 Name of charity | Article 12: name of charity | encoded | g4-art12-name | G4 |  |
| 12(1) | Article 12(1) | (1) For the purpose of Article 11(4)(e), the name of … | a name is undesirable for 11(4)(e) if, in the Commissioner's opinion, one of four grounds | encoded | g4-art12-name | G4 | note: the opinion is an input; reused by 12(4), 12(7) and 33(5)(b) |
| 12(1)(a) | Article 12(1)(a) | (a) is the same as, or too similar to, the … | the same as, or too similar to, the name of any other registered charity | encoded | g4-art12-name | G4 | note: "registered charity" excludes a deregistered one: fork F4.5 |
| 12(1)(b) | Article 12(1)(b) | (b) is likely to mislead the public as to the … | likely to mislead the public as to purpose, activities or identity | encoded | g4-art12-name | G4 |  |
| 12(1)(c) | Article 12(1)(c) | (c) gives the impression that the entity is connected to … | gives the impression of a connection with a person to whom it is not connected | encoded | g4-art12-name | G4 |  |
| 12(1)(d) | Article 12(1)(d) | (d) is offensive. | is offensive | encoded | g4-art12-name | G4 |  |
| 12(2) | Article 12(2) | (2) If the Commissioner registers the entity, the Commissioner must … | if the Commissioner registers the entity, enter the name and allocate and enter a number | encoded | g4-art12-name | G4 |  |
| 12(2)(a) | Article 12(2)(a) | (a) enter the name of the entity in the register … | enter the name of the entity as the registered name | encoded | g4-art12-name | G4 |  |
| 12(2)(b) | Article 12(2)(b) | (b) allocate a number in respect of the registration, and … | allocate a registration number and enter it | encoded | g4-art12-name | G4 |  |
| 12(3) | Article 12(3) | (3) A registered charity may apply to the Commissioner for … | a registered charity may apply for permission to change its registered name or add an alternative | encoded | g4-art12-name | G4 | note: a permission of the charity (MAY) |
| 12(4) | Article 12(4) | (4) The Commissioner must refuse permission if, in his or … | the Commissioner must refuse permission if, in his or her opinion, a ground in 12(1)(a) to (d) applies to the proposed name | encoded | g4-art12-name | G4 | note: the opinion is an input; the refusal is appealable (33(2)(b)) |
| 12(5) | Article 12(5) | (5) If the Commissioner grants permission, and the registered charity … | if permission is granted and the charity notifies that it has changed or added the name, the Commissioner must enter it | encoded | g4-art12-name | G4 |  |
| 12(6) | Article 12(6) | (6) If a registered charity reports a matter relating to … | if a charity reports a name matter under 13(6)(b), the Commissioner may require it to apply to change its name | encoded | g4-art12-name | G4 | note: power typed MAY (the Commissioner); appealable (33(2)(c)) |
| 12(7) | Article 12(7) | (7) A registered charity must not use any name other … | a registered charity must not use any name other than registered, or related and not undesirable | encoded | g4-art12-name | G4 | note: a prohibition with no stated penalty: its only consequence is through "misconduct" (IP13) |
| 12(7)(a) | Article 12(7)(a) | (a) its registered name or one of its registered names; … | its registered name or one of its registered names | encoded | g4-art12-name | G4 |  |
| 12(7)(b) | Article 12(7)(b) | (b) another name that – | another name that is related to such a name and not, in the Commissioner's opinion, undesirable in the context | encoded | g4-art12-name | G4 |  |
| 12(7)(b)(i) | Article 12(7)(b)(i) | (i) is related to such a name, and | is related to such a name | encoded | g4-art12-name | G4 |  |
| 12(7)(b)(ii) | Article 12(7)(b)(ii) | (ii) is not, in the opinion of the Commissioner, undesirable … | is not, in the Commissioner's opinion, undesirable within 12(1) in the context in which it is used | encoded | g4-art12-name | G4 |  |
| 13 | Article 13 | 13 Effects of registration | Article 13: effects of registration | encoded | g5-art13-effects | G5 |  |
| 13(1) | Article 13(1) | (1) Paragraphs (2) to (4) apply while an entity is … | (2) to (4) apply while an entity is registered and cease only on deregistration | encoded | g5-art13-effects | G5 | note: see T15 for deregistration with retrospective effect |
| 13(2) | Article 13(2) | (2) Any provision of the entity’s constitution or constitutional Law … | a constitution provision permitting an amendment adding a non-charitable purpose is of no effect to that extent | encoded | g5-art13-effects | G5 |  |
| 13(3) | Article 13(3) | (3) Any provision of the entity’s constitution or constitutional Law … | a provision permitting an amendment adding or substituting a charitable purpose is subject to evidence and the Commissioner's prior approval | encoded | g5-art13-effects | G5 | note: approval decision appealable (33(2)(d)) |
| 13(3)(a) | Article 13(3)(a) | (a) providing evidence, to the satisfaction of the Commissioner, of … | providing evidence, to the Commissioner's satisfaction, of a reason justifying the amendment | encoded | g5-art13-effects | G5 |  |
| 13(3)(b) | Article 13(3)(b) | (b) obtaining the Commissioner’s prior approval of the proposed amendment. | obtaining the Commissioner's prior approval | encoded | g5-art13-effects | G5 |  |
| 13(4) | Article 13(4) | (4) The entity must – | the entity must provide public benefit per its registered statement and evidence a request to amend it | encoded | g5-art13-effects | G5 |  |
| 13(4)(a) | Article 13(4)(a) | (a) provide public benefit in accordance with its registered public … | provide public benefit in accordance with its registered public benefit statement | encoded | g5-art13-effects | G5 |  |
| 13(4)(b) | Article 13(4)(b) | (b) if it requests the Commissioner’s approval of a proposed … | if requesting approval of an amendment to that statement, provide evidence of a reason justifying it | encoded | g5-art13-effects | G5 | note: approval decision appealable (33(2)(e)) |
| 13(5) | Article 13(5) | (5) A registered charity must, while it is entered in … | a charity in the restricted section must ensure it meets the prescribed condition | encoded | g5-art13-effects | G5 |  |
| 13(5)(a) | Article 13(5)(a) | (a) that it meets the condition, prescribed under Article 9(2), … | meets the condition prescribed under 9(2) on which the Commissioner was satisfied under 9(6)(b) | encoded | g5-art13-effects | G5 |  |
| 13(5)(b) | Article 13(5)(b) | (b) if, before it ceased to meet that condition, the … | or, with the Commissioner's prior permission, a different prescribed condition | encoded | g5-art13-effects | G5 |  |
| 13(6) | Article 13(6) | (6) A registered charity must promptly report to the Commissioner … | a registered charity must promptly report eight kinds of matter to the Commissioner | encoded | g5-art13-effects | G5 | note: period "promptly": fork F5.1 |
| 13(6)(a) | Article 13(6)(a) | (a) a change in a matter about which information is … | a change in a matter entered on the register | encoded | g5-art13-effects | G5 |  |
| 13(6)(b) | Article 13(6)(b) | (b) any other matter, coming to light after registration or … | any other matter that could have led to refusal of registration, of the name, or entry in a different section | encoded | g5-art13-effects | G5 | note: feeds 12(6) |
| 13(6)(c) | Article 13(6)(c) | (c) a proposal to change the charity’s constitution; | a proposal to change the charity's constitution | encoded | g5-art13-effects | G5 |  |
| 13(6)(d) | Article 13(6)(d) | (d) a proposal that could result, or an event that … | a proposal or event that could result in, or has resulted in, ceasing to meet 11(4)(c) or (d) | encoded | g5-art13-effects | G5 | note: IP15, IP16 |
| 13(6)(e) | Article 13(6)(e) | (e) a reportable matter, in relation to a governor of … | a reportable matter about a governor, if the charity knows the governor has not promptly reported it under 19(2) | encoded | g5-art13-effects | G5 |  |
| 13(6)(f) | Article 13(6)(f) | (f) a matter likely to lead to the charity becoming … | a matter likely to lead to bankruptcy, winding up or ceasing to exist | encoded | g5-art13-effects | G5 |  |
| 13(6)(g) | Article 13(6)(g) | (g) if the charity is entered in the restricted section, … | if in the restricted section, a proposal to change how or whether it meets the condition | encoded | g5-art13-effects | G5 |  |
| 13(6)(h) | Article 13(6)(h) | (h) any other matter prescribed by the Minister by Order … | any other matter the Minister prescribes by Order | encoded | g5-art13-effects | G5 | note: power typed MAY (the Minister) |
| 13(7) | Article 13(7) | (7) A registered charity must send an annual return to … | a registered charity must send an annual return on 13(6) matters arising during the year and prescribed matters | encoded | g5-art13-effects | G5 | note: "the year to which the return relates": fork F5.2; the date it is due is by Order (13(8)) |
| 13(8) | Article 13(8) | (8) An Order under paragraph (7) may also make provision … | an Order under (7) may provide the format, timing, consequences of lateness and register entries | encoded | g5-art13-effects | G5 | note: no Order in the sources: "late" is a named refusal; whether the due date itself is timely: fork F5.5 |
| 13(9) | Article 13(9) | (9) The Minister may by Order – | the Minister may by Order add annual-return and payment-intention requirements | encoded | g5-art13-effects | G5 | note: power typed MAY (the Minister) |
| 13(9)(a) | Article 13(9)(a) | (a) require a registered charity to include in its annual … | require details of prescribed payments to a governor or a person connected to a governor in the annual return | encoded | g5-art13-effects | G5 |  |
| 13(9)(b) | Article 13(9)(b) | (b) require a registered charity to provide to the Commissioner … | require a statement of the charity's intentions on such payments | encoded | g5-art13-effects | G5 | note: feeds 11(2)(e)(ii) |
| 13(9)(c) | Article 13(9)(c) | (c) provide for the entry on the register by the … | provide for entry on the register of those details and that statement | encoded | g5-art13-effects | G5 | note: feeds 8(3)(m) |
| 13(10) | Article 13(10) | (10) The Minister may by Order, after consulting the Commissioner … | the Minister may by Order relieve small charities from (6), (7) and Orders under (7), (8), (9) | encoded | g5-art13-effects | G5 | note: "Order under paragraph (8)": trap T18, fork F5.3 |
| 13(10)(a) | Article 13(10)(a) | (a) does not apply to a prescribed description of charity … | a provision does not apply to a prescribed description of charity | encoded | g5-art13-effects | G5 |  |
| 13(10)(b) | Article 13(10)(b) | (b) applies to a prescribed description of charity only subject … | a provision applies only subject to a prescribed modification | encoded | g5-art13-effects | G5 |  |
| 13(11) | Article 13(11) | (11) A registered charity – | a registered charity must not make a payment inconsistent with its statement, and may apply to amend it | encoded | g5-art13-effects | G5 | note: the prohibition has no stated penalty: only "misconduct" (IP13) |
| 13(11)(a) | Article 13(11)(a) | (a) must not make any payment that is inconsistent with … | must not make any payment inconsistent with a statement provided under 13(9)(b) | encoded | g5-art13-effects | G5 |  |
| 13(11)(b) | Article 13(11)(b) | (b) may apply to the Commissioner, with reasons, for permission … | may apply to the Commissioner, with reasons, for permission to amend the statement | encoded | g5-art13-effects | G5 | note: no decision rule and no appeal right stated (T12) |
| 13(12) | Article 13(12) | (12) If the States make Regulations under Article 11(7), those … | Regulations under 11(7) may require a charity to avoid or report and remedy later grounds for refusal | encoded | g5-art13-effects | G5 | note: power typed MAY (the States); an input |
| 13(13) | Article 13(13) | (13) If a court-approved fidéicommis or an incorporated 1862 association … | for a fidéicommis or 1862 association, (2) and (3) yield to any court order under the Loi of 1862 | encoded | g5-art13-effects | G5 |  |
| 14 | Article 14 | 14 Powers of court over registered charity | Article 14: powers of the court over a registered charity | encoded | g5-art14-court-powers | G5 |  |
| 14(1) | Article 14(1) | (1) The court may exercise any of the powers set … | on application by the Commissioner or the Attorney General, the court may exercise the (2) powers if misconduct or protection of property | encoded | g5-art14-court-powers | G5 | note: power typed MAY (the court) |
| 14(1)(a) | Article 14(1)(a) | (a) that there is or has been misconduct in the … | there is or has been misconduct in the administration of the charity | encoded | g5-art14-court-powers | G5 | note: "misconduct in the administration": fork F5.4 |
| 14(1)(b) | Article 14(1)(b) | (b) that it is necessary or desirable to exercise the … | necessary or desirable to protect the charity's property or secure its proper application per its registered purposes and statement | encoded | g5-art14-court-powers | G5 |  |
| 14(2) | Article 14(2) | (2) The court may make any order that the court … | the court may make any order it sees fit to remedy the misconduct, protect the property, secure its proper application | encoded | g5-art14-court-powers | G5 | note: the content of the order is an input |
| 14(3) | Article 14(3) | (3) Without prejudice to the generality of paragraph (2), the … | without prejudice to (2), the orders include nine kinds | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(a) | Article 14(3)(a) | (a) prohibiting (whether for a specified or indefinite period) the … | prohibiting the charity or a governor, for a specified or indefinite period, from three things | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(a)(i) | Article 14(3)(a)(i) | (i) referring to or holding out the entity as a … | referring to or holding out the entity as a charity or Jersey charity, charitable, having charitable purposes or providing public benefit | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(a)(ii) | Article 14(3)(a)(ii) | (ii) soliciting donations from the public, as specified in the … | soliciting donations from the public, as specified | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(a)(iii) | Article 14(3)(a)(iii) | (iii) taking any other action specified in the order; | taking any other action specified in the order | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(b) | Article 14(3)(b) | (b) appointing a person (whether a specified or indefinite period) … | appointing a person to manage the affairs in place of the governors | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(c) | Article 14(3)(c) | (c) appointing a person to be a governor of the … | appointing a person to be a governor | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(d) | Article 14(3)(d) | (d) suspending or removing a governor of the charity, or … | suspending or removing a governor or another person concerned in management or control | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(e) | Article 14(3)(e) | (e) requiring a person (including without prejudice a person carrying … | requiring a holder of property for the charity or a governor not to part with it without consent | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(f) | Article 14(3)(f) | (f) restricting the transactions that may be entered into, or … | restricting transactions or payments without the court's consent | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(g) | Article 14(3)(g) | (g) making the administration of the charity subject to such … | making the administration subject to supervision, restraint or conditions | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(h) | Article 14(3)(h) | (h) requiring a governor who appears to the court to … | requiring a governor or other person responsible for misconduct to take steps to remedy it | encoded | g5-art14-court-powers | G5 |  |
| 14(3)(i) | Article 14(3)(i) | (i) making such ancillary provision as the court thinks desirable. | making ancillary provision | encoded | g5-art14-court-powers | G5 |  |
| 14(4) | Article 14(4) | (4) The court may, on the application of the Commissioner, … | the court may amend or revoke an order on application by the Commissioner, the Attorney General, the charity or a person to whom it was directed | encoded | g5-art14-court-powers | G5 |  |
| 14(5) | Article 14(5) | (5) The powers of the court under this Article apply … | the court's powers apply in addition to other powers, and despite the constitution | encoded | g5-art14-court-powers | G5 |  |
| 14(5)(a) | Article 14(5)(a) | (a) in addition to and not in derogation from any … | in addition to and not in derogation from powers under other enactments or customary law | encoded | g5-art14-court-powers | G5 |  |
| 14(5)(b) | Article 14(5)(b) | (b) despite anything in the constitution of the charity. | despite anything in the constitution of the charity | encoded | g5-art14-court-powers | G5 |  |
| 14(6) | Article 14(6) | (6) The powers of the court under this Article are … | the court's powers are without prejudice to the Commissioner's own powers on misconduct | encoded | g5-art14-court-powers | G5 |  |
| 15 | Article 15 | 15 Deregistration on application by entity | Article 15: deregistration on application by the entity | encoded | g6-art15-16-deregistration | G6 |  |
| 15(1) | Article 15(1) | (1) An entity that is a registered charity may apply … | a registered charity may apply to the Commissioner to terminate its registration | encoded | g6-art15-16-deregistration | G6 | note: a permission of the charity (MAY) |
| 15(2) | Article 15(2) | (2) An entity applying for deregistration must provide the Commissioner … | an entity applying must provide any information or document the Commissioner requests on continuation, winding up and application of property | encoded | g6-art15-16-deregistration | G6 |  |
| 15(3) | Article 15(3) | (3) If the entity complies with paragraph (2) the Commissioner … | if the entity complies with (2), the Commissioner must deregister or refuse on grounds relating to the proposals | encoded | g6-art15-16-deregistration | G6 | note: no rule if (2) is not complied with: fork F6.1; reserved from staff (Sch 1 4(3)(b)); refusal not appealable (T12) |
| 15(3)(a) | Article 15(3)(a) | (a) deregister the entity; or | deregister the entity | encoded | g6-art15-16-deregistration | G6 |  |
| 15(3)(b) | Article 15(3)(b) | (b) refuse to deregister the entity on grounds relating to … | refuse to deregister on grounds relating to the proposals mentioned in 15(2) | encoded | g6-art15-16-deregistration | G6 |  |
| 16 | Article 16 | 16 Deregistration in other cases | Article 16: deregistration in other cases | encoded | g6-art15-16-deregistration | G6 |  |
| 16(1) | Article 16(1) | (1) The Commissioner may, by written notice to an entity … | the Commissioner may, by written notice, deregister if satisfied, after a notice inviting objections, that it is proportionate on one of four grounds | encoded | g6-art15-16-deregistration | G6 | note: two notices: trap T15; "reasonable time" for objections: fork F6.13 |
| 16(1)(a) | Article 16(1)(a) | (a) the entity no longer meets the charity test; | the entity no longer meets the charity test | encoded | g6-art15-16-deregistration | G6 | note: IP8 |
| 16(1)(b) | Article 16(1)(b) | (b) the Commissioner was misled into registering the entity, whether … | the Commissioner was misled into registering it, by the entity or anyone, intentionally or not | encoded | g6-art15-16-deregistration | G6 |  |
| 16(1)(c) | Article 16(1)(c) | (c) the entity has failed to comply with a required … | the entity failed to comply with a required steps notice | encoded | g6-art15-16-deregistration | G6 | note: IP19 |
| 16(1)(d) | Article 16(1)(d) | (d) any other circumstance prescribed by the Minister by Order … | any other circumstance prescribed by the Minister by Order | encoded | g6-art15-16-deregistration | G6 | note: power typed MAY (the Minister); an input |
| 16(2) | Article 16(2) | (2) If the Commissioner is satisfied that an entity that … | if satisfied that a registered charity no longer exists, the Commissioner must give written notice to deregister it | encoded | g6-art15-16-deregistration | G6 | note: a MUST beside the MAY of 16(1): fork F6.2 |
| 17 | Article 17 | 17 Effects of deregistration | Article 17: effects of deregistration | encoded | g6-art17-after-deregistration | G6 |  |
| 17(1) | Article 17(1) | (1) After deregistering an entity, the Commissioner – | after deregistering, the Commissioner has two duties | encoded | g6-art17-after-deregistration | G6 |  |
| 17(1)(a) | Article 17(1)(a) | (a) must retain the information registered in respect of that … | must retain the information registered for 10 years | encoded | g6-art17-after-deregistration | G6 | note: period "10 years", start unstated: fork F6.5; beside 8(6) |
| 17(1)(b) | Article 17(1)(b) | (b) must not assign the registered number of that entity … | must not assign the entity's registered number to any other registered charity | encoded | g6-art17-after-deregistration | G6 | note: no time limit stated: fork F6.6 |
| 17(2) | Article 17(2) | (2) Paragraph (3) applies if the Commissioner – | (3) applies if the Commissioner deregisters under Article 16, is satisfied the grounds existed since a past date, specifies it in the notice and decides on retrospective effect | encoded | g6-art17-after-deregistration | G6 | note: only Article 16, not Article 15; "the notice": fork F6.3 |
| 17(2)(a) | Article 17(2)(a) | (a) deregisters a charity under Article 16; | deregisters a charity under Article 16 | encoded | g6-art17-after-deregistration | G6 |  |
| 17(2)(b) | Article 17(2)(b) | (b) is satisfied that the grounds for deregistration have existed … | is satisfied the grounds have existed since a past date | encoded | g6-art17-after-deregistration | G6 |  |
| 17(2)(c) | Article 17(2)(c) | (c) specifies that date in the notice under Article 16(1) … | specifies that date in the notice under 16(1) or (2) | encoded | g6-art17-after-deregistration | G6 |  |
| 17(2)(d) | Article 17(2)(d) | (d) determines that the deregistration should take effect retrospectively. | determines that the deregistration should take effect retrospectively | encoded | g6-art17-after-deregistration | G6 |  |
| 17(3) | Article 17(3) | (3) The termination takes effect from the past date specified … | the termination takes effect from the past date for all purposes, including taxation, subject to (4) | encoded | g6-art17-after-deregistration | G6 | note: effect of "for all purposes" on 13 and Part 5 duties: trap T15 |
| 17(4) | Article 17(4) | (4) An act, that occurred before the date of the … | an act before the date of giving the notice is not made an offence merely by (3) | encoded | g6-art17-after-deregistration | G6 |  |
| 17(5) | Article 17(5) | (5) Paragraphs (6) to (11) apply, after a charity is … | (6) to (11) apply after deregistration so long as property acquired before deregistration remains | encoded | g6-art17-after-deregistration | G6 | note: "acquired before it was deregistered" under retrospective effect: fork F6.4 |
| 17(6) | Article 17(6) | (6) The entity must continue to apply the remaining property … | the entity must keep applying the remaining property for the preserved purposes and per the preserved public benefit statement | encoded | g6-art17-after-deregistration | G6 | note: defines "preserved charitable purposes" and "preserved public benefit statement" |
| 17(7) | Article 17(7) | (7) Despite any provision of the entity’s constitution, or of … | despite its constitution the entity has no power to amend the preserved purposes or statement | encoded | g6-art17-after-deregistration | G6 |  |
| 17(8) | Article 17(8) | (8) The entity may apply to the court for an … | the entity may apply to the court to amend them, and the court may make an amending order and ancillary orders | encoded | g6-art17-after-deregistration | G6 | note: the order's content is an input |
| 17(9) | Article 17(9) | (9) The court may exercise any of the powers set … | the court may exercise its Article 14 powers as if still registered, on application by the Attorney General or a governor | encoded | g6-art17-after-deregistration | G6 | note: the Article 14 order kinds are in domain.l4 |
| 17(9)(a) | Article 17(9)(a) | (a) that there is or has been any conduct in … | there is or has been conduct about the remaining property that would have been misconduct if not deregistered | encoded | g6-art17-after-deregistration | G6 |  |
| 17(9)(b) | Article 17(9)(b) | (b) that it is necessary or desirable to exercise the … | necessary or desirable to protect the remaining property or secure its application for the preserved purposes | encoded | g6-art17-after-deregistration | G6 |  |
| 17(10) | Article 17(10) | (10) A governor may not apply under paragraph (9) unless … | a governor may not apply under (9) without first giving the Attorney General notice of intention and reasons | encoded | g6-art17-after-deregistration | G6 | note: no period stated |
| 17(11) | Article 17(11) | (11) The Attorney General may at any time, by giving … | the Attorney General may at any time take over a governor's application, then withdraw or proceed | encoded | g6-art17-after-deregistration | G6 |  |
| 18 | Article 18 | 18 General duties of governors of registered charities | Article 18: general duties of governors of registered charities | encoded | g6-art18-governor-duties | G6 |  |
| 18(1) | Article 18(1) | (1) A governor of a registered charity must seek, in … | a governor must seek, in good faith, to ensure the charity acts consistently and complies | encoded | g6-art18-governor-duties | G6 |  |
| 18(1)(a) | Article 18(1)(a) | (a) acts in a manner that is consistent with its … | acts consistently with its registered charitable purposes and registered public benefit statement | encoded | g6-art18-governor-duties | G6 |  |
| 18(1)(b) | Article 18(1)(b) | (b) complies with any direction, requirement, notice or duty imposed … | complies with any direction, requirement, notice or duty imposed on it by or under the Law | encoded | g6-art18-governor-duties | G6 |  |
| 18(2) | Article 18(2) | (2) A governor of a registered charity, that is an … | a governor of a charity that is an unincorporated body within 2(1)(i) must meet three standards of care and observe the utmost good faith | encoded | g6-art18-governor-duties | G6 | note: applies only to 2(1)(i) bodies: trap T19, fork F6.7 |
| 18(2)(a) | Article 18(2)(a) | (a) act – | act with due diligence, as would a prudent person, to the best of the governor's ability and skill | encoded | g6-art18-governor-duties | G6 |  |
| 18(2)(a)(i) | Article 18(2)(a)(i) | (i) with due diligence, | with due diligence | encoded | g6-art18-governor-duties | G6 |  |
| 18(2)(a)(ii) | Article 18(2)(a)(ii) | (ii) as would a prudent person, | as would a prudent person | encoded | g6-art18-governor-duties | G6 |  |
| 18(2)(a)(iii) | Article 18(2)(a)(iii) | (iii) to the best of the governor’s ability and skill; … | to the best of the governor's ability and skill | encoded | g6-art18-governor-duties | G6 |  |
| 18(2)(b) | Article 18(2)(b) | (b) observe the utmost good faith. | observe the utmost good faith | encoded | g6-art18-governor-duties | G6 |  |
| 18(3) | Article 18(3) | (3) The duties imposed by this Article apply despite any … | these duties apply despite a contrary constitution or constitutional Law, except to the extent a provision imposes a more onerous duty | encoded | g6-art18-governor-duties | G6 |  |
| 18(4) | Article 18(4) | (4) For the purposes of this Law a governor engages … | a governor engages in misconduct in four cases | encoded | g6-art18-governor-duties | G6 | note: recurses into 2(10): trap T8 |
| 18(4)(a) | Article 18(4)(a) | (a) the governor contravenes a provision, or commits an offence, … | contravenes a provision, or commits an offence, mentioned in 2(10) | encoded | g6-art18-governor-duties | G6 |  |
| 18(4)(b) | Article 18(4)(b) | (b) the governor concurs in misconduct by the charity; | concurs in misconduct by the charity | encoded | g6-art18-governor-duties | G6 |  |
| 18(4)(c) | Article 18(4)(c) | (c) the governor assists or encourages another governor to engage … | assists or encourages another governor to engage in misconduct | encoded | g6-art18-governor-duties | G6 | note: recursive over the other governor's misconduct |
| 18(4)(d) | Article 18(4)(d) | (d) the governor – | becomes aware or ought to have, and conceals or fails within a reasonable time to protect the property or prevent misconduct | encoded | g6-art18-governor-duties | G6 | note: fork F6.8 |
| 18(4)(d)(i) | Article 18(4)(d)(i) | (i) becomes aware or ought to have become aware of … | becomes aware or ought to have become aware of misconduct, or of another governor's intention to engage in it | encoded | g6-art18-governor-duties | G6 |  |
| 18(4)(d)(ii) | Article 18(4)(d)(ii) | (ii) the governor actively conceals that misconduct or that intention, … | actively conceals it, or fails within a reasonable time to take proper steps to protect or restore property or prevent the misconduct | encoded | g6-art18-governor-duties | G6 |  |
| 19 | Article 19 | 19 Reportable matters and acting as a governor | Article 19: reportable matters and acting as a governor | encoded | g6-art19-20-fitness | G6 |  |
| 19(1) | Article 19(1) | (1) A reportable matter in relation to a person is … | a reportable matter in relation to a person is the fact that the person falls within one of eight descriptions | encoded | g6-art19-20-fitness | G6 |  |
| 19(1)(a) | Article 19(1)(a) | (a) has engaged in misconduct as a governor of a … | has engaged in misconduct as a governor that led to a required steps notice on that governor, the charity or another governor | encoded | g6-art19-20-fitness | G6 |  |
| 19(1)(b) | Article 19(1)(b) | (b) is the subject of a disqualification order, or of … | is the subject of a disqualification order or other restriction on acting as a governor under this Law | encoded | g6-art19-20-fitness | G6 |  |
| 19(1)(c) | Article 19(1)(c) | (c) has been disqualified from or for being a charity … | has been disqualified as a charity trustee in the United Kingdom or from an equivalent position elsewhere | encoded | g6-art19-20-fitness | G6 | note: "has been": fork F6.9 |
| 19(1)(d) | Article 19(1)(d) | (d) has been disqualified from being a company director, or … | has been disqualified as a company director, or equivalently outside Jersey | encoded | g6-art19-20-fitness | G6 | note: "has been": fork F6.9 |
| 19(1)(e) | Article 19(1)(e) | (e) is bankrupt or otherwise insolvent, whether under the law … | is bankrupt or otherwise insolvent, in Jersey or elsewhere | encoded | g6-art19-20-fitness | G6 | note: endnote [3]: editorial change "law of Jersey" |
| 19(1)(f) | Article 19(1)(f) | (f) has a conviction (whether or not spent) for an … | has a conviction, spent or not, for an offence under this Law | encoded | g6-art19-20-fitness | G6 |  |
| 19(1)(g) | Article 19(1)(g) | (g) has an unspent conviction for an offence falling within … | has an unspent conviction for an offence within 2(10)(b) | encoded | g6-art19-20-fitness | G6 | note: whether a conviction is spent is an input (not decided by this Law) |
| 19(1)(h) | Article 19(1)(h) | (h) falls within any other description that may be prescribed … | falls within any other description the Minister prescribes by Order | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the Minister) |
| 19(2) | Article 19(2) | (2) A governor of an entity applying for registration, or … | a governor of an applicant or of a registered charity must report any reportable matter promptly to the entity or charity and to the Commissioner | encoded | g6-art19-20-fitness | G6 | note: period "promptly": fork F6.12; the start of the 19(10) ban: fork F6.10 |
| 19(3) | Article 19(3) | (3) A governor of an entity applying for registration must, … | a governor of an applicant with no reportable matter must give the entity a declaration before the application is made | encoded | g6-art19-20-fitness | G6 |  |
| 19(4) | Article 19(4) | (4) A governor of a registered charity must, if there … | a governor of a registered charity with no reportable matter must give a declaration when notified the annual return is being prepared | encoded | g6-art19-20-fitness | G6 |  |
| 19(5) | Article 19(5) | (5) The entity must state in its application, and the … | the applicant must state in its application, and the charity in its annual return, that it has declarations from all governors who have not reported | encoded | g6-art19-20-fitness | G6 | note: feeds 11(4) |
| 19(6) | Article 19(6) | (6) An application for registration is not complete if the … | an application is not complete if (5) is not complied with | encoded | g6-art19-20-fitness | G6 | note: feeds the gap in 11(4) and (5) |
| 19(7) | Article 19(7) | (7) A registered charity that contravenes paragraph (5) must explain … | a registered charity that contravenes (5) must explain the reason to the Commissioner | encoded | g6-art19-20-fitness | G6 |  |
| 19(8) | Article 19(8) | (8) A person must not act as a governor of … | a person must not act as a governor while in breach of (2) or (4) | encoded | g6-art19-20-fitness | G6 | note: no offence attached: trap T9, fork F6.11 |
| 19(9) | Article 19(9) | (9) If a governor reports a reportable matter to the … | if a governor reports a reportable matter to the Commissioner, the Commissioner has five duties and powers | encoded | g6-art19-20-fitness | G6 |  |
| 19(9)(a) | Article 19(9)(a) | (a) must make inquiries to determine whether the governor is … | must make inquiries to decide whether the governor is a fit and proper person | encoded | g6-art19-20-fitness | G6 | note: no deadline stated |
| 19(9)(b) | Article 19(9)(b) | (b) may apply to the court to determine that issue … | may apply to the court to determine that issue under Article 20 | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the Commissioner) |
| 19(9)(c) | Article 19(9)(c) | (c) must not, in the case of an application for … | must not, on an application for registration, grant it until the issue is decided and any resulting order or notice complied with | encoded | g6-art19-20-fitness | G6 | note: collides with 11(4): trap T10 |
| 19(9)(d) | Article 19(9)(d) | (d) may, in the case of a registered charity, by … | for a registered charity, may by written notice permit the governor to act, with conditions, until the issue is decided | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the Commissioner) |
| 19(9)(e) | Article 19(9)(e) | (e) must, if the issue is not to be determined … | if the court is not to decide, must on deciding the issue do one of two things | encoded | g6-art19-20-fitness | G6 |  |
| 19(9)(e)(i) | Article 19(9)(e)(i) | (i) notify the entity that the application will be refused … | notify the entity that the application will be refused unless the governor is removed, or serve a required steps notice to suspend or remove the governor | encoded | g6-art19-20-fitness | G6 | note: against Article 28(3) for organized religious charities: trap T11, fork F6.15 |
| 19(9)(e)(ii) | Article 19(9)(e)(ii) | (ii) by notice in writing, entered in the register, give … | give permission by notice entered in the register, unconditionally or with conditions or a time limit | encoded | g6-art19-20-fitness | G6 |  |
| 19(10) | Article 19(10) | (10) A person must not act as a governor of … | a person must not act as a governor of a registered charity after reporting a reportable matter unless permitted and within any condition | encoded | g6-art19-20-fitness | G6 | note: fork F6.10 |
| 19(10)(a) | Article 19(10)(a) | (a) is permitted to do so by the Commissioner under … | permitted by the Commissioner under 19(9)(d) or (e)(ii), or by the court under Article 20 | encoded | g6-art19-20-fitness | G6 |  |
| 19(10)(b) | Article 19(10)(b) | (b) does so in either case in accordance with any … | acts in accordance with any condition on that permission | encoded | g6-art19-20-fitness | G6 |  |
| 19(11) | Article 19(11) | (11) A person who without reasonable excuse contravenes paragraph (10) … | a person who without reasonable excuse contravenes (10) commits an offence: imprisonment for one year and a fine | encoded | g6-art19-20-fitness | G6 | note: penalty data: 12 months, a fine with no maximum stated; "reasonable excuse" is an input; unit: fork F6.16 |
| 19(12) | Article 19(12) | (12) Paragraphs (10) and (11) are not to be construed … | (10) and (11) do not make an act void or invalid merely for contravening (10) | encoded | g6-art19-20-fitness | G6 |  |
| 19(13) | Article 19(13) | (13) If at any time the Commissioner suspects that a … | if the Commissioner suspects a governor breached (2), the Commissioner may apply to the court to decide fitness | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the Commissioner) |
| 20 | Article 20 | 20 Court orders as to fitness of governor | Article 20: court orders as to fitness of governor | encoded | g6-art19-20-fitness | G6 |  |
| 20(1) | Article 20(1) | (1) On an application under Article 19(9)(b) or (13), the … | on an application under 19(9)(b) or (13), the court may make any order it sees fit, including six kinds | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the court); the content of an order is an input |
| 20(1)(a) | Article 20(1)(a) | (a) an order dismissing the application; | an order dismissing the application | encoded | g6-art19-20-fitness | G6 |  |
| 20(1)(b) | Article 20(1)(b) | (b) an order giving permission for the governor to act … | an order permitting the governor to act despite a reportable matter | encoded | g6-art19-20-fitness | G6 | note: feeds 19(10)(a) |
| 20(1)(c) | Article 20(1)(c) | (c) an order that the entity must not be registered … | an order that the entity must not be registered as a charity | encoded | g6-art19-20-fitness | G6 | note: collides with 11(4): trap T10 |
| 20(1)(d) | Article 20(1)(d) | (d) an order requiring a registered charity to suspend or … | an order requiring a registered charity to suspend or remove the governor | encoded | g6-art19-20-fitness | G6 |  |
| 20(1)(e) | Article 20(1)(e) | (e) an order making any provision that could be made … | an order making any provision that a required steps notice could make | encoded | g6-art19-20-fitness | G6 |  |
| 20(1)(f) | Article 20(1)(f) | (f) any order ancillary to any such order. | any order ancillary to those | encoded | g6-art19-20-fitness | G6 |  |
| 20(2) | Article 20(2) | (2) An order under paragraph (1) may, without limitation – | an order under (1) may apply to a particular, a described or all charities, and carry conditions or time limits | encoded | g6-art19-20-fitness | G6 |  |
| 20(2)(a) | Article 20(2)(a) | (a) apply to a governor in respect of a particular … | apply to a governor in respect of a particular registered charity, a description of charities, or all registered charities | encoded | g6-art19-20-fitness | G6 |  |
| 20(2)(b) | Article 20(2)(b) | (b) be made subject to any condition or time limit … | be made subject to any condition or time limit that appears necessary or equitable to the court | encoded | g6-art19-20-fitness | G6 | note: time limit: the court's choice, an input |
| 20(3) | Article 20(3) | (3) If it appears to the Commissioner or the Attorney … | if it appears expedient in the public interest, the Commissioner or the Attorney General may apply for a disqualification order | encoded | g6-art19-20-fitness | G6 | note: defines "disqualification order"; power typed MAY (the Commissioner, the Attorney General) |
| 20(4) | Article 20(4) | (4) The court may, on such an application or on … | the court may make a disqualification order if satisfied the person is unfit by conduct or by the seriousness of a reportable matter | encoded | g6-art19-20-fitness | G6 | note: power typed MAY (the court) |
| 20(4)(a) | Article 20(4)(a) | (a) the person’s conduct in relation to a registered charity, … | the person's conduct in relation to a registered charity or an entity applying for registration | encoded | g6-art19-20-fitness | G6 |  |
| 20(4)(b) | Article 20(4)(b) | (b) the seriousness of a reportable matter in relation to … | the seriousness of a reportable matter in relation to the person | encoded | g6-art19-20-fitness | G6 |  |
| 20(5) | Article 20(5) | (5) A disqualification order is to be for such period, … | a disqualification order is for the period the court directs, not exceeding 15 years | encoded | g6-art19-20-fitness | G6 | note: period "not exceeding 15 years": fork F6.14 |
| 20(6) | Article 20(6) | (6) A person who contravenes a disqualification order commits an … | a person who contravenes a disqualification order commits an offence: imprisonment for 2 years and a fine | encoded | g6-art19-20-fitness | G6 | note: penalty data: 24 months, a fine with no maximum stated; unit: fork F6.16 |
| 21 | Article 21 | 21 Prohibition of unauthorized use of expression “charity” and related … | Article 21: prohibition of unauthorized use of "charity" and related terms | encoded | g7-art21-23-expressions | G7 |  |
| 21(1) | Article 21(1) | (1) An entity that is not a registered charity – | an entity that is not a registered charity must not say, or cause or permit another to say, that it is registered by the Commissioner | encoded | g7-art21-23-expressions | G7 | note: strict (no mental element); penalty 21(10) |
| 21(1)(a) | Article 21(1)(a) | (a) must not refer to itself as being registered by … | must not refer to itself as being registered by the Commissioner | encoded | g7-art21-23-expressions | G7 |  |
| 21(1)(b) | Article 21(1)(b) | (b) must not cause or permit another person to refer … | must not cause or permit another person to refer to it as being registered by the Commissioner | encoded | g7-art21-23-expressions | G7 |  |
| 21(2) | Article 21(2) | (2) A person must not refer to an entity, that … | a person must not refer to an unregistered entity as registered by the Commissioner if they know or suspect it is not registered and intend to mislead or to obtain an advantage | encoded | g7-art21-23-expressions | G7 | note: mental elements; penalty 21(9); overlaps 21(1) when the person is the entity: fork F7.4 |
| 21(2)(a) | Article 21(2)(a) | (a) knows, suspects or has reasonable grounds to suspect that … | knows, suspects or has reasonable grounds to suspect that the entity is not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(2)(b) | Article 21(2)(b) | (b) intends, by so referring to the entity, to cause … | intends to cause another person to be misled as to the nature of the entity, or to give it property or a financial or other advantage | encoded | g7-art21-23-expressions | G7 | note: "or other advantage" is missing from 21(4), 21(6), 23(2): fork F7.5 |
| 21(2)(b)(i) | Article 21(2)(b)(i) | (i) to be misled as to the nature of the … | to be misled as to the nature of the entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(2)(b)(ii) | Article 21(2)(b)(ii) | (ii) to give to the entity any property or financial … | to give the entity any property or financial or other advantage | encoded | g7-art21-23-expressions | G7 |  |
| 21(3) | Article 21(3) | (3) A Jersey entity that is not a registered charity … | a Jersey entity that is not a registered charity must not call itself, or cause or permit others to call it, a "charity" | encoded | g7-art21-23-expressions | G7 | note: strict; penalty 21(10) |
| 21(3)(a) | Article 21(3)(a) | (a) must not refer to itself as a “charity”; and | must not refer to itself as a "charity" | encoded | g7-art21-23-expressions | G7 |  |
| 21(3)(b) | Article 21(3)(b) | (b) must not cause or permit another person to refer … | must not cause or permit another person to refer to it as a "charity" | encoded | g7-art21-23-expressions | G7 |  |
| 21(4) | Article 21(4) | (4) A person must not refer to a Jersey entity, … | a person must not call an unregistered Jersey entity a "charity" if they know or suspect and intend to mislead or to obtain a financial advantage | encoded | g7-art21-23-expressions | G7 | note: penalty 21(9) |
| 21(4)(a) | Article 21(4)(a) | (a) knows, suspects or has reasonable grounds to suspect that … | knows, suspects or has reasonable grounds to suspect that the entity is a Jersey entity and not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(4)(a)(i) | Article 21(4)(a)(i) | (i) is a Jersey entity, and | is a Jersey entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(4)(a)(ii) | Article 21(4)(a)(ii) | (ii) is not a registered charity; and | is not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(4)(b) | Article 21(4)(b) | (b) intends, by so referring to the entity, to cause … | intends to cause another person to be misled as to the nature of the entity, or to give it any property or financial advantage | encoded | g7-art21-23-expressions | G7 |  |
| 21(4)(b)(i) | Article 21(4)(b)(i) | (i) to be misled as to the nature of the … | to be misled as to the nature of the entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(4)(b)(ii) | Article 21(4)(b)(ii) | (ii) to give any property or financial advantage to the … | to give any property or financial advantage to the entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(5) | Article 21(5) | (5) An entity that is not a registered charity and … | an unregistered entity that is neither a Jersey entity nor an excepted foreign charity must not call itself a "charity" in connection with its Jersey activities | encoded | g7-art21-23-expressions | G7 | note: strict; penalty 21(10) |
| 21(5)(a) | Article 21(5)(a) | (a) must not refer to itself as a “charity” in … | must not refer to itself as a "charity" in connection with any of its activities in Jersey | encoded | g7-art21-23-expressions | G7 |  |
| 21(5)(b) | Article 21(5)(b) | (b) must not cause or permit another person to refer … | must not cause or permit another to refer to it as a "charity" in connection with any of its Jersey activities | encoded | g7-art21-23-expressions | G7 |  |
| 21(6) | Article 21(6) | (6) A person must not refer to an entity, that … | a person must not call such an entity a "charity" in connection with its Jersey activities if they know or suspect and intend to mislead or to obtain a financial advantage | encoded | g7-art21-23-expressions | G7 | note: penalty 21(9) |
| 21(6)(a) | Article 21(6)(a) | (a) knows, suspects or has reasonable grounds to suspect that … | knows, suspects or has reasonable grounds to suspect the entity is neither a Jersey entity nor an excepted foreign charity and is not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(6)(a)(i) | Article 21(6)(a)(i) | (i) is neither a Jersey entity nor an excepted foreign … | is neither a Jersey entity nor an excepted foreign charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(6)(a)(ii) | Article 21(6)(a)(ii) | (ii) is not a registered charity; and | is not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 21(6)(b) | Article 21(6)(b) | (b) intends, by so referring to the entity, to cause … | intends to cause another person to be misled as to the nature of the entity, or to give it any property or financial advantage | encoded | g7-art21-23-expressions | G7 |  |
| 21(6)(b)(i) | Article 21(6)(b)(i) | (i) to be misled as to the nature of the … | to be misled as to the nature of the entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(6)(b)(ii) | Article 21(6)(b)(ii) | (ii) to give any property or financial advantage to the … | to give any property or financial advantage to the entity | encoded | g7-art21-23-expressions | G7 |  |
| 21(7) | Article 21(7) | (7) Paragraphs (2), (4) and (6) apply whether or not … | (2), (4) and (6) apply whether or not the person making the reference is also the entity referring to itself | encoded | g7-art21-23-expressions | G7 |  |
| 21(8) | Article 21(8) | (8) The States may by Regulations prescribe exceptions to the … | the States may by Regulations prescribe exceptions to the prohibitions in (1) to (6) | encoded | g7-art21-23-expressions | G7 | note: power typed MAY (the States); the Regulations are not in the sources |
| 21(9) | Article 21(9) | (9) An entity or other person, that contravenes paragraph (2), … | an entity or other person who contravenes (2), (4) or (6) commits an offence: imprisonment for 2 years and a fine | encoded | g7-art21-23-expressions | G7 | note: penalty data: 24 months, a fine with no maximum stated; unit: fork F7.8 |
| 21(10) | Article 21(10) | (10) An entity, that contravenes paragraph (1), (3) or (5), … | an entity that contravenes (1), (3) or (5) commits an offence: a fine of level 3 on the standard scale | encoded | g7-art21-23-expressions | G7 | note: penalty data: no imprisonment, level 3; the amount of level 3 is outside the sources |
| 22 | Article 22 | 22 Excepted foreign charities | Article 22: excepted foreign charities | encoded | g7-art21-23-expressions | G7 |  |
| 22(1) | Article 22(1) | (1) For the purpose of Article 21, an entity is … | an entity is an excepted foreign charity if it meets both the first and second conditions, for Article 21 | encoded | g7-art21-23-expressions | G7 | note: also used by 2(10)(b) |
| 22(2) | Article 22(2) | (2) The first condition is that the entity is – | the first condition | encoded | g7-art21-23-expressions | G7 |  |
| 22(2)(a) | Article 22(2)(a) | (a) established under the law – | established under the law of the United Kingdom or part of it, or of a jurisdiction prescribed by the Minister by Order | encoded | g7-art21-23-expressions | G7 |  |
| 22(2)(a)(i) | Article 22(2)(a)(i) | (i) of the United Kingdom, or of any jurisdiction that … | established under the law of the United Kingdom or any part of it | encoded | g7-art21-23-expressions | G7 |  |
| 22(2)(a)(ii) | Article 22(2)(a)(ii) | (ii) of a jurisdiction (not being Jersey, the United Kingdom … | established under the law of a jurisdiction (not Jersey or the UK) prescribed by Order | encoded | g7-art21-23-expressions | G7 | note: power typed MAY (the Minister); the prescribed list is an input |
| 22(2)(b) | Article 22(2)(b) | (b) entitled, under the law of that jurisdiction, to refer … | entitled under that law to call itself a "charity" there (or an equivalent term in another language) | encoded | g7-art21-23-expressions | G7 | note: an input |
| 22(3) | Article 22(3) | (3) The second condition is that the entity – | the second condition | encoded | g7-art21-23-expressions | G7 |  |
| 22(3)(a) | Article 22(3)(a) | (a) is managed wholly or mainly from the jurisdiction under … | managed wholly or mainly from the jurisdiction under whose law it is established | encoded | g7-art21-23-expressions | G7 |  |
| 22(3)(b) | Article 22(3)(b) | (b) is not a registered charity. | is not a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 22(4) | Article 22(4) | (4) The Minister may by Order prescribe that a specified … | the Minister may by Order say that a specified entity need not meet the first condition | encoded | g7-art21-23-expressions | G7 | note: power typed MAY (the Minister) |
| 22(5) | Article 22(5) | (5) The States may by Regulations amend paragraph (1), (2) … | the States may by Regulations amend 22(1), (2) or (3) to change the conditions | encoded | g7-art21-23-expressions | G7 | note: power typed MAY (the States); can change the answer; Regulations are not in the sources |
| 23 | Article 23 | 23 Prohibition of unauthorized use of expression “Jersey charity” | Article 23: prohibition of unauthorized use of "Jersey charity" | encoded | g7-art21-23-expressions | G7 |  |
| 23(1) | Article 23(1) | (1) Unless an entity meets all of the conditions in … | unless an entity meets all three conditions it must not call itself, or cause or permit another to call it, a "Jersey charity" | encoded | g7-art21-23-expressions | G7 | note: strict; penalty 23(6) |
| 23(1)(a) | Article 23(1)(a) | (a) must not refer to itself as a “Jersey charity”; … | must not refer to itself as a "Jersey charity" | encoded | g7-art21-23-expressions | G7 |  |
| 23(1)(b) | Article 23(1)(b) | (b) must not cause or permit another person to refer … | must not cause or permit another to refer to it as a "Jersey charity" | encoded | g7-art21-23-expressions | G7 |  |
| 23(2) | Article 23(2) | (2) Unless an entity meets all of the conditions in … | a person must not call an entity not meeting the conditions a "Jersey charity" if they know or suspect and intend to mislead or to obtain a financial advantage | encoded | g7-art21-23-expressions | G7 | note: penalty 23(7) |
| 23(2)(a) | Article 23(2)(a) | (a) knows, suspects or has reasonable grounds to suspect that … | knows, suspects or has reasonable grounds to suspect that the entity does not meet all of the conditions | encoded | g7-art21-23-expressions | G7 |  |
| 23(2)(b) | Article 23(2)(b) | (b) intends, by so referring to the entity, to cause … | intends to cause another person to be misled as to the nature of the entity or to give it any property or financial advantage | encoded | g7-art21-23-expressions | G7 |  |
| 23(2)(b)(i) | Article 23(2)(b)(i) | (i) to be misled as to the nature of the … | to be misled as to the nature of the entity | encoded | g7-art21-23-expressions | G7 |  |
| 23(2)(b)(ii) | Article 23(2)(b)(ii) | (ii) to give any property or financial advantage to the … | to give any property or financial advantage to the entity | encoded | g7-art21-23-expressions | G7 |  |
| 23(3) | Article 23(3) | (3) The conditions are that the entity – | the conditions: a registered charity, a Jersey entity, wholly or mainly managed or controlled in or from Jersey | encoded | g7-art21-23-expressions | G7 |  |
| 23(3)(a) | Article 23(3)(a) | (a) is a registered charity; | is a registered charity | encoded | g7-art21-23-expressions | G7 |  |
| 23(3)(b) | Article 23(3)(b) | (b) is a Jersey entity; and | is a Jersey entity | encoded | g7-art21-23-expressions | G7 |  |
| 23(3)(c) | Article 23(3)(c) | (c) is wholly or mainly managed or controlled in or … | is wholly or mainly managed or controlled in or from within Jersey | encoded | g7-art21-23-expressions | G7 |  |
| 23(4) | Article 23(4) | (4) Paragraphs (1) and (2) are subject to any exception … | (1) and (2) are subject to any exception the States prescribe by Regulations | encoded | g7-art21-23-expressions | G7 |  |
| 23(5) | Article 23(5) | (5) Paragraph (2) applies whether or not the person making … | (2) applies whether or not the person making the reference is also the entity | encoded | g7-art21-23-expressions | G7 |  |
| 23(6) | Article 23(6) | (6) An entity that contravenes paragraph (1) commits an offence … | an entity that contravenes (1) commits an offence: a fine of level 3 on the standard scale | encoded | g7-art21-23-expressions | G7 | note: penalty data: no imprisonment, level 3 |
| 23(7) | Article 23(7) | (7) An entity or other person, that contravenes paragraph (2), … | an entity or other person who contravenes (2) commits an offence: imprisonment for 2 years and a fine | encoded | g7-art21-23-expressions | G7 | note: penalty data: 24 months, a fine with no maximum stated; unit: fork F7.8 |
| 24 | Article 24 | 24 Power to restrict use of term “charitable” in soliciting … | Article 24: power to restrict the term "charitable" in soliciting funds | encoded | g7-art24-25-powers | G7 |  |
| 24(1) | Article 24(1) | (1) The States may by Regulations make provision restricting the … | the States may by Regulations restrict the use, other than by a registered charity, of a relevant term in soliciting donations from the public or a prescribed description of persons | encoded | g7-art24-25-powers | G7 | note: power typed MAY (the States); the Regulations are not in the sources |
| 24(2) | Article 24(2) | (2) The relevant terms are “charitable”, “public benefit” and any … | the relevant terms are "charitable", "public benefit" and any related term other than "charity" specified in the Regulations | encoded | g7-art24-25-powers | G7 |  |
| 24(3) | Article 24(3) | (3) Without prejudice to the generality of paragraph (1) any … | the Regulations may adapt Articles 21 to 23, require permission with Commissioner discretion, and provide for Commissioner guidance | encoded | g7-art24-25-powers | G7 | note: a limit on the content of the Regulations |
| 24(3)(a) | Article 24(3)(a) | (a) may make the provision by adapting any provisions of … | make the provision by adapting any provisions of Articles 21 to 23 | encoded | g7-art24-25-powers | G7 |  |
| 24(3)(b) | Article 24(3)(b) | (b) may impose the restriction by any means, including by … | impose the restriction by any means, including a permission the Commissioner may be given discretion to grant | encoded | g7-art24-25-powers | G7 |  |
| 24(3)(c) | Article 24(3)(c) | (c) may provide for the Commissioner to issue guidance as … | provide for the Commissioner to issue guidance on the operation of the Regulations | encoded | g7-art24-25-powers | G7 |  |
| 24(4) | Article 24(4) | (4) The Regulations may make it an offence to contravene … | the Regulations may create an offence carrying a penalty no greater than a fine | encoded | g7-art24-25-powers | G7 | note: a cap on the content of the Regulations: no imprisonment |
| 25 | Article 25 | 25 Power to require registered charities to identify themselves as … | Article 25: power to require registered charities to identify themselves | encoded | g7-art24-25-powers | G7 |  |
| 25(1) | Article 25(1) | (1) The Minister may by Order prescribe statements that must … | the Minister may by Order prescribe statements a registered charity must make about its registration in prescribed documents or publicity | encoded | g7-art24-25-powers | G7 | note: power typed MAY (the Minister); the Order is not in the sources |
| 25(2) | Article 25(2) | (2) Without prejudice to the generality of paragraph (1), the … | the provision may include six statements and three kinds of provision | inert | g7-art24-25-powers | G7 | illustrates the content of an Order, without prejudice to 25(1); the content of an Order is an input |
| 25(2)(a) | Article 25(2)(a) | (a) provision requiring the charity to state any or all … | require the charity to state that it is a charity, its number, that it is registered, how documents may be inspected, its purposes, or its governors' contact details | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(i) | Article 25(2)(a)(i) | (i) that it is a charity, | that it is a charity | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(ii) | Article 25(2)(a)(ii) | (ii) its charity registration number, | its charity registration number | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(iii) | Article 25(2)(a)(iii) | (iii) that it is registered with the Commissioner, | that it is registered with the Commissioner | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(iv) | Article 25(2)(a)(iv) | (iv) how documents relating to its registration may be inspected, | how documents relating to its registration may be inspected | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(v) | Article 25(2)(a)(v) | (v) the nature of its purposes, | the nature of its purposes | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(a)(vi) | Article 25(2)(a)(vi) | (vi) the identity or contact details of one or more … | the identity or contact details of one or more of its charity governors | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(b) | Article 25(2)(b) | (b) provision as to the legibility of the statement, and … | provision on legibility and the language of the statement | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(c) | Article 25(2)(c) | (c) provision as to whether the requirement only applies to … | provision on whether the requirement applies only to documents issued or signed for the charity | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 25(2)(d) | Article 25(2)(d) | (d) provision as to whether and how the requirement applies … | provision on whether and how it applies to web pages and sites and the charity's responsibility for them | inert | g7-art24-25-powers | G7 | illustrative content of an Order |
| 26 | Article 26 | 26 Power to demand information | Article 26: power to demand information | encoded | g8-art26-demand | G8 |  |
| 26(1) | Article 26(1) | (1) The Commissioner may, by notice in writing served on … | the Commissioner may by written notice require a person in 26(2) to provide information or documents or to attend and answer questions, for deciding whether to serve a required steps notice | encoded | g8-art26-demand | G8 | note: power typed MAY (the Commissioner); "reasonably requires" is an input; purpose narrower than 26(10): trap T23; the time specified in the notice: fork F8.7 |
| 26(1)(a) | Article 26(1)(a) | (a) to provide to the Commissioner, at such time and … | provide information or a document of a specified description at a specified time and place | encoded | g8-art26-demand | G8 |  |
| 26(1)(b) | Article 26(1)(b) | (b) to attend at such place and time as may … | attend at a specified time and place and answer questions | encoded | g8-art26-demand | G8 |  |
| 26(2) | Article 26(2) | (2) The persons falling within this paragraph are – | the persons: a registered or former registered charity, and governors or former governors | encoded | g8-art26-demand | G8 | note: applicants are not within it |
| 26(2)(a) | Article 26(2)(a) | (a) a registered charity or an entity that was formerly … | a registered charity or an entity that was formerly a registered charity | encoded | g8-art26-demand | G8 |  |
| 26(2)(b) | Article 26(2)(b) | (b) a governor or former governor of a registered charity … | a governor or former governor of a registered charity or of a formerly registered entity | encoded | g8-art26-demand | G8 |  |
| 26(3) | Article 26(3) | (3) If a person from whom provision of a document … | if a person claims a lien on a document, providing it is without prejudice to the lien | encoded | g8-art26-demand | G8 |  |
| 26(4) | Article 26(4) | (4) If the Commissioner exercises a power under paragraph (1) … | if a document is required, the Commissioner may retain or copy it and require an explanation, or require a statement of where it is | encoded | g8-art26-demand | G8 |  |
| 26(4)(a) | Article 26(4)(a) | (a) if the document is provided, retain or take copies … | if provided, retain or copy it and require an explanation from the provider or from a governor or employee | encoded | g8-art26-demand | G8 |  |
| 26(4)(b) | Article 26(4)(b) | (b) if the document is not provided, require the person … | if not provided, require a statement of where it is, to the best of knowledge and belief | encoded | g8-art26-demand | G8 |  |
| 26(5) | Article 26(5) | (5) A document, copy or extract retained or taken under … | a retained document may be kept for the longer of one year and, if proceedings begin within that year, until they conclude | encoded | g8-art26-demand | G8 | note: period "one year", start unstated: fork F8.1 |
| 26(5)(a) | Article 26(5)(a) | (a) a period of one year; and | a period of one year | encoded | g8-art26-demand | G8 |  |
| 26(5)(b) | Article 26(5)(b) | (b) if within that period proceedings to which the document … | if proceedings to which the document is relevant are commenced against any person within that period, until they conclude | encoded | g8-art26-demand | G8 |  |
| 26(6) | Article 26(6) | (6) A person who requires a document retained under paragraph … | a person who needs a retained document for business and requests it must be supplied a copy as soon as practicable | encoded | g8-art26-demand | G8 | note: period "as soon as practicable": fork F8.2 |
| 26(7) | Article 26(7) | (7) A person who without reasonable excuse contravenes a requirement … | a person who without reasonable excuse contravenes a requirement under (1) or (4) commits an offence: 3 months and a fine of level 3 | encoded | g8-art26-demand | G8 | note: penalty data: 3 months, level 3; "reasonable excuse" is an input; unit: fork F8.8 |
| 26(8) | Article 26(8) | (8) Nothing in this Article is to be construed as … | nothing requires disclosure of what a person could refuse to disclose on grounds of legal professional privilege | encoded | g8-art26-demand | G8 | note: a limit on the duty |
| 26(9) | Article 26(9) | (9) A statement made by a person in compliance with … | a statement made in compliance may not be used by the prosecution in criminal proceedings except under (7) or (10) | encoded | g8-art26-demand | G8 | note: an evidential rule: computable as a predicate |
| 26(10) | Article 26(10) | (10) A person commits an offence, and is liable to … | a person who gives information to the Commissioner, knowing it false in a material particular and intending it to be used for an application or for deciding on a notice, commits an offence: 2 years and a fine | encoded | g8-art26-demand | G8 | note: penalty data: 24 months, a fine with no maximum stated; unit: fork F8.8 |
| 26(11) | Article 26(11) | (11) For the purpose of paragraph (10) it is irrelevant … | for (10) it is irrelevant whether the information | encoded | g8-art26-demand | G8 |  |
| 26(11)(a) | Article 26(11)(a) | (a) is contained in a document or not; or | is contained in a document or not | encoded | g8-art26-demand | G8 |  |
| 26(11)(b) | Article 26(11)(b) | (b) is provided under this Article or not. | is provided under this Article or not | encoded | g8-art26-demand | G8 |  |
| 27 | Article 27 | 27 Required steps notices | Article 27: required steps notices | encoded | g8-art27-28-required-steps | G8 |  |
| 27(1) | Article 27(1) | (1) Paragraph (2) applies if the Commissioner believes that – | (2) applies if the Commissioner believes one of five things | encoded | g8-art27-28-required-steps | G8 | note: the Commissioner's belief is an input |
| 27(1)(a) | Article 27(1)(a) | (a) there has been misconduct by a registered charity; | there has been misconduct by a registered charity | encoded | g8-art27-28-required-steps | G8 | note: IP12 |
| 27(1)(b) | Article 27(1)(b) | (b) a registered charity does not pass the charity test; | a registered charity does not pass the charity test | encoded | g8-art27-28-required-steps | G8 | note: IP8 |
| 27(1)(c) | Article 27(1)(c) | (c) a governor of a registered charity has engaged in … | a governor of a registered charity has engaged in misconduct | encoded | g8-art27-28-required-steps | G8 | note: IP14 (Article 18(4)) |
| 27(1)(d) | Article 27(1)(d) | (d) a governor of a registered charity is, by reason … | a governor is, by reason of a reportable matter, unfit to be a governor | encoded | g8-art27-28-required-steps | G8 | note: IP21 |
| 27(1)(e) | Article 27(1)(e) | (e) a registered charity has ceased to meet the requirements … | a registered charity has ceased to meet the requirements of 11(4)(c) or (d) | encoded | g8-art27-28-required-steps | G8 | note: IP15, IP16 |
| 27(2) | Article 27(2) | (2) The Commissioner may serve written notice on any one … | the Commissioner may serve written notice on one or more relevant persons requiring steps in a specified time that are, in the Commissioner's opinion, appropriate to remedy the matter | encoded | g8-art27-28-required-steps | G8 | note: power typed MAY (the Commissioner); the time and the steps are inputs; how a specified time is counted: fork F8.7 |
| 27(3) | Article 27(3) | (3) The relevant persons for the purpose of paragraph (2) … | the relevant persons: the registered charity and its governors | encoded | g8-art27-28-required-steps | G8 |  |
| 27(3)(a) | Article 27(3)(a) | (a) the registered charity; and | the registered charity | encoded | g8-art27-28-required-steps | G8 |  |
| 27(3)(b) | Article 27(3)(b) | (b) the governors of the registered charity. | the governors of the registered charity | encoded | g8-art27-28-required-steps | G8 |  |
| 27(4) | Article 27(4) | (4) If the notice is served by virtue of paragraph … | if served under (1)(c) or (d), the steps may include suspension, removal or replacement of the governor, subject to Article 28 | encoded | g8-art27-28-required-steps | G8 |  |
| 27(5) | Article 27(5) | (5) The Minister may by Order make further provision as … | the Minister may by Order make further provision on procedure and restrictions for serving the notice | encoded | g8-art27-28-required-steps | G8 | note: power typed MAY (the Minister) |
| 28 | Article 28 | 28 Required steps notices restricted in relation to governors of … | Article 28: required steps notices restricted for organized religious charities | encoded | g8-art27-28-required-steps | G8 |  |
| 28(1) | Article 28(1) | (1) The Minister may by Order provide for registered charities … | the Minister may by Order categorize registered charities as organized religious charities, for (3) | encoded | g8-art27-28-required-steps | G8 | note: power typed MAY (the Minister); who is categorized is an input from the Order |
| 28(1)(a) | Article 28(1)(a) | (a) to meet the charity test by virtue of Article … | charities that appear to the Minister to meet the charity test by virtue of Article 6(1)(c), alone or with other purposes | encoded | g8-art27-28-required-steps | G8 | note: "by virtue of 6(1)(c)": fork F8.3 on a philosophical-belief purpose (F2.5) |
| 28(1)(b) | Article 28(1)(b) | (b) to be organized in such a way that the … | charities organized so that supervision and discipline of governors in respect of Jersey activities is adequate | encoded | g8-art27-28-required-steps | G8 | note: the Minister's appearance is an input |
| 28(2) | Article 28(2) | (2) The provision that may be made under paragraph (1) … | the provision may include discretion for the Commissioner and distinctions by status | encoded | g8-art27-28-required-steps | G8 | note: a limit on the content of the Order |
| 28(2)(a) | Article 28(2)(a) | (a) provision granting discretion to the Commissioner to grant or … | discretion for the Commissioner to grant or withdraw the status | encoded | g8-art27-28-required-steps | G8 | note: power typed MAY (the Commissioner) where the Order gives it |
| 28(2)(b) | Article 28(2)(b) | (b) provision that distinguishes between charities on the basis of … | distinctions by status under three headings | inert | g8-art27-28-required-steps | G8 | illustrative content of an Order |
| 28(2)(b)(i) | Article 28(2)(b)(i) | (i) a designated religious charity within the meaning of the … | a designated religious charity under the Charities and Trustee Investment (Scotland) Act 2005 | out-of-scope | (none) | G8 | the text of the Scottish Act is not in sources; an input |
| 28(2)(b)(ii) | Article 28(2)(b)(ii) | (ii) an institution falling within section 10(2) of the Charities … | an institution within section 10(2) of the Charities Act 2011 of the United Kingdom | out-of-scope | (none) | G8 | the text of the UK Act is not in sources; an input |
| 28(2)(b)(iii) | Article 28(2)(b)(iii) | (iii) an entity in Jersey that is similar to such … | an entity in Jersey similar to those | inert | g8-art27-28-required-steps | G8 | illustrative content of an Order |
| 28(3) | Article 28(3) | (3) A required steps notice served on an organized religious … | a required steps notice on an organized religious charity or its governor is invalid to the extent it requires a governor to be suspended, removed or replaced | encoded | g8-art27-28-required-steps | G8 | note: partial invalidity; collides with 19(9)(e)(i): trap T11 |
| 29 | Article 29 | 29 Restricted information | Article 29: restricted information | encoded | g8-art29-31-information | G8 |  |
| 29(1) | Article 29(1) | (1) Subject to paragraph (2) and to Articles 30 and … | a person who receives information about another's affairs under the Law, or from someone who did, commits an offence by disclosing it without consent: 2 years and a fine | encoded | g8-art29-31-information | G8 | note: "subject to (2) and Articles 30 and 31"; penalty data: 24 months, a fine with no maximum stated; unit: fork F8.8 |
| 29(1)(a) | Article 29(1)(a) | (a) under or for the purposes of this Law; or | under or for the purposes of this Law | encoded | g8-art29-31-information | G8 |  |
| 29(1)(b) | Article 29(1)(b) | (b) directly or indirectly from a person who has so … | directly or indirectly from a person who has so received it | encoded | g8-art29-31-information | G8 | note: consent of the person from whom it was received as well, where (b) applies |
| 29(2) | Article 29(2) | (2) This Article does not apply to information – | the Article does not apply to three kinds of information | encoded | g8-art29-31-information | G8 |  |
| 29(2)(a) | Article 29(2)(a) | (a) that is registered in the public parts of the … | information registered in the public parts of the register, within 10(3) to (5) | encoded | g8-art29-31-information | G8 | note: IP25 |
| 29(2)(b) | Article 29(2)(b) | (b) that at the time of the disclosure is or … | information already made available to the public from other sources | encoded | g8-art29-31-information | G8 |  |
| 29(2)(c) | Article 29(2)(c) | (c) in the form of a summary or collection of … | a summary or collection so framed that no particular person can be identified | encoded | g8-art29-31-information | G8 |  |
| 30 | Article 30 | 30 Required disclosure of information | Article 30: required disclosure of information | encoded | g8-art29-31-information | G8 |  |
| 30(1) | Article 30(1) | (1) The Commissioner must disclose information to the Comptroller, if … | the Commissioner must disclose information to the Comptroller if required for the Comptroller's functions in the taxation of charities | encoded | g8-art29-31-information | G8 | note: the Comptroller's requirement is an input |
| 30(2) | Article 30(2) | (2) The Commissioner must disclose information to the JFSC, if … | the Commissioner must disclose information to the JFSC if required for its functions under the Non-Profit Organizations (Jersey) Law 2008 | encoded | g8-art29-31-information | G8 | note: the JFSC's requirement is an input |
| 31 | Article 31 | 31 Permitted disclosure of information | Article 31: permitted disclosure of information | encoded | g8-art29-31-information | G8 |  |
| 31(a) | Article 31(a) | (a) by or on behalf of the Commissioner, for purpose … | by or for the Commissioner, to enable the Commissioner to discharge any function | encoded | g8-art29-31-information | G8 |  |
| 31(b) | Article 31(b) | (b) to the Comptroller for purpose of enabling the Comptroller … | to the Comptroller, to enable the Comptroller to discharge any function | encoded | g8-art29-31-information | G8 | note: wider than the duty in 30(1) |
| 31(c) | Article 31(c) | (c) to the JFSC for the purpose of enabling the … | to the JFSC, to enable it to discharge any function | encoded | g8-art29-31-information | G8 | note: endnote [4]: editorial change "for the purpose of" |
| 31(d) | Article 31(d) | (d) to the Attorney General, the Bailiff or the court … | to the Attorney General, the Bailiff or the court, for their functions in relation to charities | encoded | g8-art29-31-information | G8 |  |
| 31(e) | Article 31(e) | (e) to any person for the purpose of the investigation … | to any person, for the investigation or prosecution of an offence or for taking proceedings under this Law | encoded | g8-art29-31-information | G8 |  |
| 31(f) | Article 31(f) | (f) in any other circumstances prescribed by the States by … | in other circumstances prescribed by the States by Regulations | encoded | g8-art29-31-information | G8 | note: power typed MAY (the States) |
| 32 | Article 32 | 32 Establishment of Charity Tribunal | Article 32: establishment of the Charity Tribunal | inert | g8-art32-36-appeals | G8 | constitutive; the Tribunal as an actor is `the Charity Tribunal` |
| 32(1) | Article 32(1) | (1) There is established a tribunal to be known as … | there is established a tribunal known as the Charity Tribunal | inert | g8-art32-36-appeals | G8 | establishes a body; no rule to compute |
| 32(2) | Article 32(2) | (2) The function of the tribunal is to hear and … | the tribunal's function is to hear and determine appeals under Part 8 | inert | g8-art32-36-appeals | G8 | declares the Tribunal's jurisdiction; the appeal rights are encoded at 33 to 35 |
| 32(3) | Article 32(3) | (3) Schedule 2 makes further provision in respect of the … | Schedule 2 makes further provision | inert | g8-art32-36-appeals | G8 | pointer to Schedule 2 (G9) |
| 33 | Article 33 | 33 Persons who may appeal and decisions that may be … | Article 33: persons who may appeal and decisions that may be appealed | encoded | g8-art32-36-appeals | G8 |  |
| 33(1) | Article 33(1) | (1) An applicant for registration may appeal against a decision … | an applicant for registration may appeal two decisions | encoded | g8-art32-36-appeals | G8 |  |
| 33(1)(a) | Article 33(1)(a) | (a) to refuse to register the applicant; or | a decision to refuse to register the applicant | encoded | g8-art32-36-appeals | G8 |  |
| 33(1)(b) | Article 33(1)(b) | (b) to refuse to register the applicant in the restricted … | a decision to refuse to register the applicant in the restricted section | encoded | g8-art32-36-appeals | G8 |  |
| 33(2) | Article 33(2) | (2) A registered charity may appeal against a decision of … | a registered charity may appeal five decisions | encoded | g8-art32-36-appeals | G8 | note: a closed list: trap T12, fork F8.4 |
| 33(2)(a) | Article 33(2)(a) | (a) to deregister the charity; | a decision to deregister the charity | encoded | g8-art32-36-appeals | G8 | note: not a refusal to deregister (15(3)(b)) |
| 33(2)(b) | Article 33(2)(b) | (b) to refuse permission, under Article 12(4), for the charity … | a decision to refuse permission under 12(4) to change or add a registered name | encoded | g8-art32-36-appeals | G8 |  |
| 33(2)(c) | Article 33(2)(c) | (c) to require the charity, under Article 12(6), to apply … | a decision under 12(6) to require the charity to apply to change its registered name | encoded | g8-art32-36-appeals | G8 |  |
| 33(2)(d) | Article 33(2)(d) | (d) to refuse approval, under Article 13(3), of a proposed … | a decision to refuse approval under 13(3) of a purposes amendment | encoded | g8-art32-36-appeals | G8 |  |
| 33(2)(e) | Article 33(2)(e) | (e) to refuse to approve an amendment, proposed under Article … | a decision to refuse to approve under 13(4)(b) an amendment of the registered public benefit statement | encoded | g8-art32-36-appeals | G8 |  |
| 33(3) | Article 33(3) | (3) A person on whom the Commissioner serves a notice … | a person served with a notice under Article 26 or a required steps notice may appeal the decision to impose a requirement in it | encoded | g8-art32-36-appeals | G8 |  |
| 33(4) | Article 33(4) | (4) The Attorney General may appeal against any decision of … | the Attorney General may appeal any decision of the Commissioner | encoded | g8-art32-36-appeals | G8 |  |
| 33(5) | Article 33(5) | (5) A person, other than an applicant for registration, a … | a person other than the applicant, a registered charity or the Attorney General may appeal a decision to register an applicant on two grounds, at both the time of application and the time of appeal | encoded | g8-art32-36-appeals | G8 | note: the "both times" structure: trap T12 |
| 33(5)(a) | Article 33(5)(a) | (a) the applicant did not meet the charity test; or | the applicant did not meet the charity test | encoded | g8-art32-36-appeals | G8 | note: IP8 at two times |
| 33(5)(b) | Article 33(5)(b) | (b) if the appellant has an interest in the registered … | if the appellant has an interest in the registered name, that name was undesirable under 12(1) | encoded | g8-art32-36-appeals | G8 | note: IP18 at two times |
| 34 | Article 34 | 34 Grounds of appeal and powers of tribunal in determining … | Article 34: grounds of appeal and powers of the tribunal | encoded | g8-art32-36-appeals | G8 |  |
| 34(1) | Article 34(1) | (1) An appeal may be made to the tribunal on … | an appeal may be made on the ground that the Commissioner's decision was wrong or unreasonable on its merits, the facts or the law | encoded | g8-art32-36-appeals | G8 | note: wider than the ground in 35(1): fork F8.5 |
| 34(2) | Article 34(2) | (2) The tribunal may – | the tribunal may make interim orders and consider evidence | encoded | g8-art32-36-appeals | G8 |  |
| 34(2)(a) | Article 34(2)(a) | (a) make such interim order on an appeal as it … | make such interim order on an appeal as it thinks fit | encoded | g8-art32-36-appeals | G8 |  |
| 34(2)(b) | Article 34(2)(b) | (b) consider evidence that was put to the Commissioner or … | consider evidence that was put to the Commissioner or accept other evidence | encoded | g8-art32-36-appeals | G8 |  |
| 34(3) | Article 34(3) | (3) On determining an appeal the tribunal may – | on determining an appeal the tribunal may do three things | encoded | g8-art32-36-appeals | G8 |  |
| 34(3)(a) | Article 34(3)(a) | (a) remit the decision to the Commissioner, substitute the tribunal’s … | remit the decision to the Commissioner, substitute its own decision, or dismiss the appeal | encoded | g8-art32-36-appeals | G8 |  |
| 34(3)(b) | Article 34(3)(b) | (b) award costs if satisfied that the appeal was vexatious … | award costs if satisfied the appeal was vexatious or otherwise grossly unreasonable | encoded | g8-art32-36-appeals | G8 | note: against whom is unstated: the appellant is the natural reading (fork not registered, no case) |
| 34(3)(c) | Article 34(3)(c) | (c) make any recommendation to the Commissioner, as to the … | make any recommendation to the Commissioner about the performance of functions in the subject matter | encoded | g8-art32-36-appeals | G8 |  |
| 35 | Article 35 | 35 Appeal and reference to court | Article 35: appeal and reference to the court | encoded | g8-art32-36-appeals | G8 |  |
| 35(1) | Article 35(1) | (1) A party to an appeal to the tribunal, or … | a party to a tribunal appeal, or the Attorney General, may appeal to the court on the ground that the decision was unreasonable having regard to all the circumstances | encoded | g8-art32-36-appeals | G8 | note: fork F8.5 |
| 35(2) | Article 35(2) | (2) The court, on determining the appeal, may remit the … | the court may remit to the tribunal or Commissioner, substitute its decision for either, or dismiss | encoded | g8-art32-36-appeals | G8 |  |
| 35(3) | Article 35(3) | (3) The tribunal may refer any point of law to … | the tribunal may refer any point of law to the court for a ruling | encoded | g8-art32-36-appeals | G8 | note: power typed MAY (the Charity Tribunal) |
| 35(4) | Article 35(4) | (4) The court may make such interim order on an … | the court may make such interim order on an appeal or reference as it thinks fit | encoded | g8-art32-36-appeals | G8 |  |
| 36 | Article 36 | 36 Further provision as to appeals to tribunal or court | Article 36: further provision as to appeals | encoded | g8-art32-36-appeals | G8 |  |
| 36(1) | Article 36(1) | (1) Nothing in this Part is to be read as … | nothing in Part 8 limits the Commissioner's power to reconsider the decisions of the Commissioner or staff | encoded | g8-art32-36-appeals | G8 |  |
| 36(2) | Article 36(2) | (2) The Minister may by Order – | the Minister may by Order set time limits for appeals and provide for notice of decisions | encoded | g8-art32-36-appeals | G8 | note: power typed MAY (the Minister); no Order in the sources: "in time" is a named refusal |
| 36(2)(a) | Article 36(2)(a) | (a) prescribe time limits within which appeals to the tribunal … | prescribe time limits within which appeals to the tribunal or court are brought | encoded | g8-art32-36-appeals | G8 | note: anchor of the time limit: fork F8.6 |
| 36(2)(b) | Article 36(2)(b) | (b) make such provision as to the giving of notice … | make provision on the giving of notice of decisions and reasons so appeals can be brought in time | encoded | g8-art32-36-appeals | G8 |  |
| 36(3) | Article 36(3) | (3) If the court or tribunal substitutes its decision for … | a court or tribunal that substitutes its decision may order it to take effect from any date it thinks appropriate, before, on or after either decision | encoded | g8-art32-36-appeals | G8 |  |
| 36(4) | Article 36(4) | (4) If the court or tribunal makes an order under … | if the order takes effect from a date before the order, an act before the date of the order is not made an offence merely by that | encoded | g8-art32-36-appeals | G8 | note: parallel of 17(4) |
| 37 | Article 37 | 37 Offences by corporate and other bodies | Article 37: offences by corporate and other bodies | encoded | g7-art37-43-final | G7 |  |
| 37(1) | Article 37(1) | (1) If an offence under this Law, committed by a … | if an offence by an LLP, separate limited partnership or body corporate is proved to have been committed with the consent or connivance of an officer, the officer is also guilty and liable in the same manner | encoded | g7-art37-43-final | G7 | note: scope is narrow: trap T26, fork F7.6 |
| 37(1)(a) | Article 37(1)(a) | (a) a person who is a partner of the partnership, … | a partner of the partnership, or a director, governor, secretary or similar officer of the body corporate | encoded | g7-art37-43-final | G7 |  |
| 37(1)(b) | Article 37(1)(b) | (b) any person purporting to act in any such capacity, | any person purporting to act in any such capacity | encoded | g7-art37-43-final | G7 |  |
| 37(2) | Article 37(2) | (2) Where the affairs of a body corporate are managed … | where a body corporate is managed by its members, (1) applies to a member's management acts as if the member were a director | encoded | g7-art37-43-final | G7 |  |
| 38 | Article 38 | 38 Service of notices | Article 38: service of notices | encoded | g7-art37-43-final | G7 | note: the Law does not say how service is fixed: fork F7.7 |
| 39 | Article 39 | 39 Regulations and Orders | Article 39: Regulations and Orders | encoded | g7-art37-43-final | G7 |  |
| 39(1) | Article 39(1) | (1) An Order or Regulations under this Law may contain … | an Order or Regulations may contain transitional, consequential, incidental, supplementary or savings provisions, other than an amendment of this Law | encoded | g7-art37-43-final | G7 | note: a limit on the content of Orders and Regulations; 2(2) is the one power to amend by Order |
| 39(2) | Article 39(2) | (2) A power under this Law to amend, by Regulations, … | a power to amend this Law by Regulations includes consequential amendments of other provisions of it | encoded | g7-art37-43-final | G7 |  |
| 40 | Article 40 | 40 Savings and transitional provisions | Article 40: savings and transitional provisions | encoded | g7-art37-43-final | G7 |  |
| 40(1) | Article 40(1) | (1) Nothing in this Law is to be read as … | nothing in the Law derogates from the independent powers or functions of the Attorney General, the Bailiff or the court | inert | g7-art37-43-final | G7 | rule of construction; no input or outcome of its own |
| 40(2) | Article 40(2) | (2) The States may by Regulations make such other saving … | the States may by Regulations make other saving provision | encoded | g7-art37-43-final | G7 | note: power typed MAY (the States) |
| 40(3) | Article 40(3) | (3) The States may by Regulations make such transitional provision … | the States may by Regulations make transitional provision for bringing the Law into force | encoded | g7-art37-43-final | G7 | note: power typed MAY (the States); spent after commencement |
| 41 | Article 41 | 41 Amendments of Laws relating to sharing of information | Article 41: amendments of Laws relating to sharing of information | out-of-scope | (none) | G7 | empowers Regulations amending other enactments (the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008, any other enactment giving the JFSC functions, any taxation enactment); neither those enactments nor any Regulations are in the sources; original Article 42 |
| 41(1) | Article 41(1) | (1) For the purpose of paragraph (2) a relevant enactment … | a "relevant enactment" is one of three kinds | out-of-scope | (none) | G7 | names the enactments the Regulations may amend; not in sources |
| 41(1)(a) | Article 41(1)(a) | (a) the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008; | the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008 | out-of-scope | (none) | G7 | another enactment, not in sources |
| 41(1)(b) | Article 41(1)(b) | (b) any other enactment under which the JFSC has functions; | any other enactment under which the JFSC has functions | out-of-scope | (none) | G7 | other enactments, not in sources |
| 41(1)(c) | Article 41(1)(c) | (c) any enactment relating to taxation. | any enactment relating to taxation | out-of-scope | (none) | G7 | other enactments, not in sources |
| 41(2) | Article 41(2) | (2) The States may by Regulations amend any relevant enactment, … | the States may by Regulations amend a relevant enactment so supervisory bodies, the JFSC and the Comptroller may disclose information to the Commissioner | out-of-scope | (none) | G7 | a power to amend other enactments; the Regulations are not in the sources |
| 42 | Article 42 | 42 Consequential amendments of other enactments | Article 42: consequential amendments of other enactments | out-of-scope | (none) | G7 | empowers Regulations amending the Trusts (Jersey) Law 1984, the Foundations (Jersey) Law 2009 and any enactment referring to charities; those enactments and the Regulations are not in the sources; original Article 43 |
| 42(a) | Article 42(a) | (a) amend the Trusts (Jersey) Law 1984 and the Foundations … | the States may by Regulations amend the Trusts (Jersey) Law 1984 and the Foundations (Jersey) Law 2009 to apply the charity test or charitable purposes | out-of-scope | (none) | G7 | those enactments and the Regulations are not in the sources |
| 42(b) | Article 42(b) | (b) amend any other enactment (not including this Law) to … | the States may by Regulations amend any other enactment (not this Law) for consequential provision on charities | out-of-scope | (none) | G7 | other enactments are not in the sources |
| 43 | Article 43 | 43 Citation | Article 43: citation | inert | g7-art37-43-final | G7 | citation only; original Article 44(1) |
| Sch 1 | Schedule  paragraph 1 | Schedule 1[5] | Schedule 1: the Jersey Charity Commissioner (Article 3) | encoded | g9-sched1-commissioner | G9 | note: amended by L.1/2017 (two "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" additions, from 16 December 2019) |
| Sch1 1 | Schedule 1 paragraph 1 | 1 Appointment of Commissioner | paragraph 1: appointment of the Commissioner | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 1(1) | Schedule 1 paragraph 1(1) | (1) The Minister must appoint a person appearing to the … | the Minister must appoint a person appearing to the Minister to be suitable | encoded | g9-sched1-commissioner | G9 | note: a duty on the Minister with no trigger or deadline stated beyond 1(7); suitability is an input |
| Sch1 1(2) | Schedule 1 paragraph 1(2) | (2) Before appointing a person as the Commissioner, the Minister … | before appointing, the Minister must seek the views of the Jersey Appointments Commission | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 1(3) | Schedule 1 paragraph 1(3) | (3) The Minister must, at least 2 weeks before appointing … | the Minister must, at least 2 weeks before appointing, present to the States a notice of intention | encoded | g9-sched1-commissioner | G9 | note: period "at least 2 weeks before": fork F9.1 |
| Sch1 1(4) | Schedule 1 paragraph 1(4) | (4) A person appointed as the Commissioner holds and vacates … | the Commissioner holds and vacates office per the terms of appointment, subject to the Law | inert | g9-sched1-commissioner | G9 | restates the terms of appointment; no rule of its own |
| Sch1 1(5) | Schedule 1 paragraph 1(5) | (5) When appointing a person as the Commissioner the Minister … | the Minister must fix the period of appointment, not more than 6 years | encoded | g9-sched1-commissioner | G9 | note: period "not more than 6 years": fork F9.2 |
| Sch1 1(6) | Schedule 1 paragraph 1(6) | (6) The Minister may re-appoint a person serving as the … | the Minister may re-appoint, and "appointment" in this paragraph includes re-appointment | encoded | g9-sched1-commissioner | G9 | note: power typed MAY (the Minister); extends 1(2), (3), (5) to re-appointment |
| Sch1 1(7) | Schedule 1 paragraph 1(7) | (7) The Minister must take all reasonable steps to ensure … | the Minister must take all reasonable steps to ensure the office is filled at all times | encoded | g9-sched1-commissioner | G9 | note: a continuous duty; "all reasonable steps" is an input |
| Sch1 1(8) | Schedule 1 paragraph 1(8) | (8) Nothing in sub-paragraph (7) is to be construed as … | 1(7) does not prevent an appointment requiring limited days or hours | inert | g9-sched1-commissioner | G9 | clarification of 1(7); no rule of its own |
| Sch1 2 | Schedule 1 paragraph 2 | 2 Status of Commissioner | paragraph 2: status of the Commissioner | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 2(1) | Schedule 1 paragraph 2(1) | (1) The Commissioner may, as a corporation sole, in the … | the Commissioner, as a corporation sole, may do five things in the name of the office | inert | g9-sched1-commissioner | G9 | capacities of a corporation sole; no precondition or outcome |
| Sch1 2(1)(a) | Schedule 1 paragraph 2(1)(a) | (a) enter into an agreement for any purpose of his … | enter into an agreement for any purpose of the office | inert | g9-sched1-commissioner | G9 | a legal capacity of a corporation sole, with no precondition and no outcome to compute; nothing in the Law turns on it |
| Sch1 2(1)(b) | Schedule 1 paragraph 2(1)(b) | (b) acquire, hold and dispose of movable property; | acquire, hold and dispose of movable property | inert | g9-sched1-commissioner | G9 | a legal capacity of a corporation sole, with no precondition and no outcome to compute; nothing in the Law turns on it |
| Sch1 2(1)(c) | Schedule 1 paragraph 2(1)(c) | (c) sue and be sued in any civil proceedings; | sue and be sued in any civil proceedings | inert | g9-sched1-commissioner | G9 | a legal capacity of a corporation sole, with no precondition and no outcome to compute; nothing in the Law turns on it |
| Sch1 2(1)(d) | Schedule 1 paragraph 2(1)(d) | (d) be charged with an offence and defend criminal proceedings; … | be charged with an offence and defend criminal proceedings | inert | g9-sched1-commissioner | G9 | a legal capacity of a corporation sole, with no precondition and no outcome to compute; the Law creates no offence the Commissioner could commit |
| Sch1 2(1)(e) | Schedule 1 paragraph 2(1)(e) | (e) do anything reasonably necessary or expedient for or incidental … | do anything reasonably necessary or expedient for or incidental to the Commissioner's functions | inert | g9-sched1-commissioner | G9 | capacity; overlaps Article 4(2) |
| Sch1 2(2) | Schedule 1 paragraph 2(2) | (2) The Commissioner is independent of the States and the … | the Commissioner is independent of the States and the Minister | inert | g9-sched1-commissioner | G9 | status; limits only Sch 1 4(11) and (12) |
| Sch1 2(3) | Schedule 1 paragraph 2(3) | (3) The terms and conditions of the appointment of the … | appointment terms do not create a contract of employment or agency with the States or the Minister | inert | g9-sched1-commissioner | G9 | a statement of legal status with no input, condition or outcome in this Law; employment law is outside the sources |
| Sch1 2(4) | Schedule 1 paragraph 2(4) | (4) Despite sub-paragraphs (2) and (3) – | despite (2) and (3), remuneration and fees are dealt with in two ways | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 2(4)(a) | Schedule 1 paragraph 2(4)(a) | (a) subject to Article 20(1) of the Dormant Bank Accounts … | subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017, remuneration must be paid out of the annual income of the States | encoded | g9-sched1-commissioner | G9 | note: vintage-dependent: the words "subject to Article 20(1) of the DBAL" exist from 16 December 2019 (L.1/2017); fork F9.9 |
| Sch1 2(4)(b) | Schedule 1 paragraph 2(4)(b) | (b) all fees and other sums received by the Commissioner … | all fees and sums received by the Commissioner must be paid to the income of the States | encoded | g9-sched1-commissioner | G9 | note: not made subject to the DBAL |
| Sch1 3 | Schedule 1 paragraph 3 | 3 Termination of office as Commissioner | paragraph 3: termination of office as Commissioner | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(1) | Schedule 1 paragraph 3(1) | (1) A person ceases to be appointed as the Commissioner … | a person ceases to be Commissioner in three cases | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(1)(a) | Schedule 1 paragraph 3(1)(a) | (a) he or she resigns from office by giving not … | resigns by giving not less than 3 months' notice in writing to the Minister | encoded | g9-sched1-commissioner | G9 | note: period "not less than 3 months": fork F9.3; the Schedule 2 equivalent is one month (trap T20) |
| Sch1 3(1)(b) | Schedule 1 paragraph 3(1)(b) | (b) the Minister terminates his or her appointment under sub-paragraph … | the Minister terminates the appointment under 3(2) | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(1)(c) | Schedule 1 paragraph 3(1)(c) | (c) his or her appointment expires under sub-paragraph (4). | the appointment expires under 3(4) | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(2) | Schedule 1 paragraph 3(2) | (2) The Minister may terminate the appointment of a person … | the Minister may terminate after satisfying himself or herself on one of four grounds | encoded | g9-sched1-commissioner | G9 | note: power typed MAY (the Minister) |
| Sch1 3(2)(a) | Schedule 1 paragraph 3(2)(a) | (a) has been absent from his or her duties for … | absent from duties for a period longer than 4 consecutive weeks | encoded | g9-sched1-commissioner | G9 | note: period "longer than 4 consecutive weeks": fork F9.4; the Schedule 2 equivalent is 8 weeks (trap T20) |
| Sch1 3(2)(b) | Schedule 1 paragraph 3(2)(b) | (b) has become bankrupt; | has become bankrupt | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(2)(c) | Schedule 1 paragraph 3(2)(c) | (c) is incapacitated by illness; or | is incapacitated by illness | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(2)(d) | Schedule 1 paragraph 3(2)(d) | (d) is otherwise unable or unfit to discharge the functions … | is otherwise unable or unfit to discharge the functions | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(3) | Schedule 1 paragraph 3(3) | (3) The Minister must, not more than 2 weeks after … | the Minister must, not more than 2 weeks after terminating, present a notice of the termination to the States | encoded | g9-sched1-commissioner | G9 | note: period "not more than 2 weeks after": fork F9.5 |
| Sch1 3(4) | Schedule 1 paragraph 3(4) | (4) A person’s appointment as the Commissioner expires if – | the appointment expires in three cases | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(4)(a) | Schedule 1 paragraph 3(4)(a) | (a) the period for which the person was appointed expires … | the period of appointment expires without re-appointment | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(4)(b) | Schedule 1 paragraph 3(4)(b) | (b) the person becomes a member of the States; or | the person becomes a member of the States | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 3(4)(c) | Schedule 1 paragraph 3(4)(c) | (c) the person completes 12 years (whether consecutive or in … | the person completes 12 years of service as Commissioner, consecutive or in aggregate | encoded | g9-sched1-commissioner | G9 | note: period "12 years": fork F9.6; mid-term cut-off beside 1(5) and 1(6): trap T21 |
| Sch1 4 | Schedule 1 paragraph 4 | 4 Staff, resources and reporting | paragraph 4: staff, resources and reporting | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(1) | Schedule 1 paragraph 4(1) | (1) The Minister must make available to the Commissioner such … | the Minister must make available such staff as the Minister considers required | encoded | g9-sched1-commissioner | G9 | note: the Minister's consideration is an input |
| Sch1 4(2) | Schedule 1 paragraph 4(2) | (2) To the extent that any States’ employee (within the … | a States employee made available and directed by the Commissioner is treated as the Commissioner's staff | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(3) | Schedule 1 paragraph 4(3) | (3) Any function of the Commissioner may, to the extent … | a function of the Commissioner may be exercised by staff to the extent authorized, except three decisions | encoded | g9-sched1-commissioner | G9 | note: fork F9.8; trap T17 |
| Sch1 4(3)(a) | Schedule 1 paragraph 4(3)(a) | (a) the decision under Article 11 on whether to register … | the decision under Article 11 whether to register a charity | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(3)(b) | Schedule 1 paragraph 4(3)(b) | (b) the decision under Article 15(3) on whether to refuse … | the decision under Article 15(3) whether to refuse to deregister a charity | encoded | g9-sched1-commissioner | G9 | note: reserves the refusal, not the grant under 15(3)(a): trap T17 |
| Sch1 4(3)(c) | Schedule 1 paragraph 4(3)(c) | (c) the decision under Article 16 on whether to deregister … | the decision under Article 16 whether to deregister a charity | encoded | g9-sched1-commissioner | G9 | note: includes the mandatory 16(2) |
| Sch1 4(4) | Schedule 1 paragraph 4(4) | (4) The Minister may designate a person as the relevant … | the Minister may designate a person as the relevant person for 4(5) | encoded | g9-sched1-commissioner | G9 | note: power typed MAY (the Minister) |
| Sch1 4(5) | Schedule 1 paragraph 4(5) | (5) A relevant person designated under sub-paragraph (4) is to … | a designated relevant person is treated as the Commissioner while the Commissioner is unable to act or the office is vacant, temporarily | encoded | g9-sched1-commissioner | G9 | note: who acts as the Commissioner on a day (IP28) |
| Sch1 4(5)(a) | Schedule 1 paragraph 4(5)(a) | (a) the person appointed as the Commissioner is unable to … | the person appointed is unable to act through incapacity or absence | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(5)(b) | Schedule 1 paragraph 4(5)(b) | (b) there is a vacancy in the office of Commissioner, | there is a vacancy in the office of Commissioner | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(6) | Schedule 1 paragraph 4(6) | (6) The Minister must provide such accommodation and equipment as … | the Minister must provide accommodation and equipment as the Minister considers required | encoded | g9-sched1-commissioner | G9 |  |
| Sch1 4(7) | Schedule 1 paragraph 4(7) | (7) Subject to Article 20(1) of the Dormant Bank Accounts … | subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017, the cost of staff, accommodation and equipment must be met out of the annual income of the States | encoded | g9-sched1-commissioner | G9 | note: vintage-dependent: the "subject to" words exist from 16 December 2019 (L.1/2017); fork F9.9 |
| Sch1 4(8) | Schedule 1 paragraph 4(8) | (8) The Commissioner must prepare and publish a report on … | the Commissioner must prepare and publish a report on activities in each calendar year | encoded | g9-sched1-commissioner | G9 | note: "calendar year" stated, unlike Article 13(7): trap T24; a part-year of office: fork F9.12 |
| Sch1 4(9) | Schedule 1 paragraph 4(9) | (9) The Commissioner must provide the Minister with the report … | the Commissioner must give the Minister the report as soon as practicable and in no case later than 4 months after the end of the year | encoded | g9-sched1-commissioner | G9 | note: period "4 months after the end of that year": fork F9.7; "as soon as practicable": fork F9.10 |
| Sch1 4(10) | Schedule 1 paragraph 4(10) | (10) The Minister must lay a copy of the report … | the Minister must lay a copy before the States as soon as practicable | encoded | g9-sched1-commissioner | G9 | note: period "as soon as practicable": fork F9.10 |
| Sch1 4(11) | Schedule 1 paragraph 4(11) | (11) The Minister may, by giving written notice to the … | the Minister may, by written notice to the Commissioner that is published, give directions on the content and form of the report | encoded | g9-sched1-commissioner | G9 | note: power typed MAY (the Minister) |
| Sch1 4(12) | Schedule 1 paragraph 4(12) | (12) Directions under paragraph (11) must respect the independence of … | directions must respect independence and may not require the report to justify decisions about individual charities, governors or applicants | encoded | g9-sched1-commissioner | G9 | note: a limit on the content of the directions |
| Sch 2 | Schedule  paragraph 2 | Schedule 2 | Schedule 2: the Charity Tribunal (Article 32), headed "Charity Commission tribunal" | encoded | g9-sched2-tribunal | G9 | note: the heading differs from Article 32's "Charity Tribunal": trap T20 |
| Sch2 1 | Schedule 2 paragraph 1 | 1 Appointment | paragraph 1: appointment of tribunal members | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 1(1) | Schedule 2 paragraph 1(1) | (1) The Minister must appoint as members of the tribunal … | the Minister must appoint at least 4 and no more than 8 suitable and experienced members | encoded | g9-sched2-tribunal | G9 | note: a numeric limit on the membership |
| Sch2 1(2) | Schedule 2 paragraph 1(2) | (2) Before appointing a person as a tribunal member, the … | before appointing a member, the Minister must seek the views of the Jersey Appointments Commission | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 1(3) | Schedule 2 paragraph 1(3) | (3) The Minister must, at least 2 weeks before appointing … | the Minister must, at least 2 weeks before appointing, present to the States a notice of intention | encoded | g9-sched2-tribunal | G9 | note: period "at least 2 weeks before": fork F9.1 |
| Sch2 1(4) | Schedule 2 paragraph 1(4) | (4) A person appointed as a tribunal member holds and … | a member holds and vacates the position per the terms of appointment, subject to the Law | inert | g9-sched2-tribunal | G9 | restates the terms of appointment |
| Sch2 1(5) | Schedule 2 paragraph 1(5) | (5) When appointing a person as a tribunal member the … | the Minister must fix the period of appointment, not more than 6 years | encoded | g9-sched2-tribunal | G9 | note: period "not more than 6 years": fork F9.2 |
| Sch2 1(6) | Schedule 2 paragraph 1(6) | (6) The Minister may re-appoint a person serving as a … | the Minister may re-appoint, and "appointment" in this paragraph includes re-appointment | encoded | g9-sched2-tribunal | G9 | note: power typed MAY (the Minister) |
| Sch2 1(7) | Schedule 2 paragraph 1(7) | (7) The Minister must, among the members of the tribunal, … | the Minister must designate one member as chair and another as vice-chair | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 1(8) | Schedule 2 paragraph 1(8) | (8) Service as a tribunal member is honorary, unless the … | service is honorary unless the Minister determines that the chair, or all members, are to be remunerated | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2 | Schedule 2 paragraph 2 | 2 Termination of appointment | paragraph 2: termination of appointment | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(1) | Schedule 2 paragraph 2(1) | (1) A person ceases to be a member of the … | a person ceases to be a member in three cases | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(1)(a) | Schedule 2 paragraph 2(1)(a) | (a) he or she resigns from office by giving not … | resigns by giving not less than one month's notice in writing to the Minister | encoded | g9-sched2-tribunal | G9 | note: period "not less than one month": fork F9.3; the Schedule 1 equivalent is 3 months (trap T20) |
| Sch2 2(1)(b) | Schedule 2 paragraph 2(1)(b) | (b) the Minister terminates his or her appointment under sub-paragraph … | the Minister terminates the appointment under 2(2) | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(1)(c) | Schedule 2 paragraph 2(1)(c) | (c) his or her appointment expires under sub-paragraph (4). | the appointment expires under 2(4) | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(2) | Schedule 2 paragraph 2(2) | (2) The Minister may terminate the appointment of a person … | the Minister may terminate after satisfying himself or herself on one of four grounds | encoded | g9-sched2-tribunal | G9 | note: power typed MAY (the Minister) |
| Sch2 2(2)(a) | Schedule 2 paragraph 2(2)(a) | (a) has been absent from his or her duties for … | absent from duties for a period longer than 8 consecutive weeks | encoded | g9-sched2-tribunal | G9 | note: period "longer than 8 consecutive weeks": fork F9.4; the Schedule 1 equivalent is 4 weeks (trap T20) |
| Sch2 2(2)(b) | Schedule 2 paragraph 2(2)(b) | (b) has become bankrupt; | has become bankrupt | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(2)(c) | Schedule 2 paragraph 2(2)(c) | (c) is incapacitated by illness; or | is incapacitated by illness | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(2)(d) | Schedule 2 paragraph 2(2)(d) | (d) is otherwise unable or unfit to discharge the functions … | is otherwise unable or unfit to discharge the functions of a member | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(3) | Schedule 2 paragraph 2(3) | (3) The Minister must, not more than 2 weeks after … | the Minister must, not more than 2 weeks after terminating, present a notice of the termination to the States | encoded | g9-sched2-tribunal | G9 | note: period "not more than 2 weeks after": fork F9.5 |
| Sch2 2(4) | Schedule 2 paragraph 2(4) | (4) A person’s appointment as a member of the tribunal … | the appointment expires in three cases | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(4)(a) | Schedule 2 paragraph 2(4)(a) | (a) the period for which the person was appointed expires … | the period of appointment expires without re-appointment | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(4)(b) | Schedule 2 paragraph 2(4)(b) | (b) the person becomes a member of the States; or | the person becomes a member of the States | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 2(4)(c) | Schedule 2 paragraph 2(4)(c) | (c) the person completes 12 years (whether consecutive or in … | the person completes 12 years of service as a member, consecutive or in aggregate | encoded | g9-sched2-tribunal | G9 | note: period "12 years": fork F9.6; trap T21 |
| Sch2 3 | Schedule 2 paragraph 3 | 3 Staff, resources and reporting | paragraph 3: staff, resources and reporting | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 3(1) | Schedule 2 paragraph 3(1) | (1) The Minister must make available to the tribunal such … | the Minister must make available staff and resources as the Minister considers required | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 3(2) | Schedule 2 paragraph 3(2) | (2) The Minister must secure that there is available to … | the Minister must secure at least one member of staff as the responsible officer to assist with administration but not determinations | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 3(3) | Schedule 2 paragraph 3(3) | (3) The responsible officer must prepare a report on the … | the responsible officer must prepare a report on the tribunal's activities in each calendar year | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 3(4) | Schedule 2 paragraph 3(4) | (4) The responsible officer must provide the Minister with the … | the responsible officer must give the Minister the report as soon as practicable and in no case later than 4 months after the end of the year | encoded | g9-sched2-tribunal | G9 | note: period "4 months after the end of that year": fork F9.7; "as soon as practicable": fork F9.10 |
| Sch2 3(5) | Schedule 2 paragraph 3(5) | (5) The Minister must lay a copy of the report … | the Minister must lay a copy before the States as soon as practicable | encoded | g9-sched2-tribunal | G9 | note: period "as soon as practicable": fork F9.10 |
| Sch2 4 | Schedule 2 paragraph 4 | 4 Procedure of tribunal | paragraph 4: procedure of the tribunal | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(1) | Schedule 2 paragraph 4(1) | (1) A sitting of the tribunal is to be presided … | a sitting is presided over by the chair, the vice-chair if the chair is absent, or a member chosen by those present | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(1)(a) | Schedule 2 paragraph 4(1)(a) | (a) the chair; | the chair | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(1)(b) | Schedule 2 paragraph 4(1)(b) | (b) the vice-chair, if the chair is absent; or | the vice-chair, if the chair is absent | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(1)(c) | Schedule 2 paragraph 4(1)(c) | (c) if both the chair and vice-chair are absent, a … | if both are absent, a tribunal member appointed for the purpose by the members present at the sitting | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(2) | Schedule 2 paragraph 4(2) | (2) Subject to sub-paragraph (1), and to any Regulations under … | subject to 4(1) and any Regulations under 4(3), the tribunal may regulate its own procedure | encoded | g9-sched2-tribunal | G9 |  |
| Sch2 4(3) | Schedule 2 paragraph 4(3) | (3) The States may by Regulations make further provision as … | the States may by Regulations make further provision on the procedure of the tribunal on ten matters | encoded | g9-sched2-tribunal | G9 | note: power typed MAY (the States); the Regulations are not in the sources |
| Sch2 4(3)(a) | Schedule 2 paragraph 4(3)(a) | (a) the burden of proof on an appeal; | the burden of proof on an appeal | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover; the Regulations are not in the sources |
| Sch2 4(3)(b) | Schedule 2 paragraph 4(3)(b) | (b) the summoning of witnesses and the administration of oaths; | the summoning of witnesses and the administration of oaths | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(c) | Schedule 2 paragraph 4(3)(c) | (c) securing the production of documents and evidence; | securing the production of documents and evidence | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(d) | Schedule 2 paragraph 4(3)(d) | (d) the conduct of hearings, the determination of appeals with … | the conduct of hearings, decisions without hearings, and hearings in public or private or in a party's absence | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(e) | Schedule 2 paragraph 4(3)(e) | (e) enabling an appeal to be determined, or any matter … | determination or directions by the chair or vice-chair, and quorum and voting rules | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(f) | Schedule 2 paragraph 4(3)(f) | (f) the award of costs, and the creation of offences … | costs, and offences in relation to the tribunal carrying a penalty not exceeding 2 years' imprisonment and a fine | encoded | g9-sched2-tribunal | G9 | note: a cap on the content of the Regulations: penalty data of at most 24 months and a fine; unit: fork F9.13 |
| Sch2 4(3)(g) | Schedule 2 paragraph 4(3)(g) | (g) the publication of reports of the tribunal’s decisions; | the publication of reports of the tribunal's decisions | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(h) | Schedule 2 paragraph 4(3)(h) | (h) duties of the Commissioner in relation to an appeal; | duties of the Commissioner in relation to an appeal | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(i) | Schedule 2 paragraph 4(3)(i) | (i) striking out, withdrawal and amendment of appeals or replies; | striking out, withdrawal and amendment of appeals or replies | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| Sch2 4(3)(j) | Schedule 2 paragraph 4(3)(j) | (j) such ancillary powers of the tribunal as the States … | such ancillary powers of the tribunal as the States think necessary | inert | g9-sched2-tribunal | G9 | subject matter the Regulations may cover |
| E1 | Endnotes, Table of Legislation History, row E1 | Parts 1 to 3, Articles 32, 38, 39, 40, 42, … | Table of Legislation History, L.41/2014 stage 1: Parts 1 to 3, Articles 32, 38, 39, 40, 42, 43 and 44 and the Schedules, in force 21 November 2014 | encoded | g7-commencement | G7 | note: numbers are the ORIGINAL numbers: trap T1; fork F7.3 |
| E2 | Endnotes, Table of Legislation History, row E2 | Parts 4, 5, 7, 8 (other than Article 32), Article … | stage 2: Parts 4, 5, 7, 8 (other than Article 32) and Article 37 in force 1 May 2018 (R&O.17/2018) | encoded | g7-commencement | G7 | note: R&O.17/2018 Article 1 confirms; "in force on" the stated day: fork F7.1 |
| E3 | Endnotes, Table of Legislation History, row E3 | Remainder in force 1 January 2019 (R&O.17/2018). | stage 3: the remainder in force 1 January 2019 (R&O.17/2018) | encoded | g7-commencement | G7 | note: the remainder is Part 6 and the original Article 41: trap T2 (R&O.17/2018 Article 2) |
| E4 | Endnotes, Table of Legislation History, row E4 | States of Jersey (Transfer of Responsibilities and | R&O.40/2019, 31 May 2019: Chief Minister to External Relations (Article 1 "Minister") | encoded | g7-vintages | G7 | note: first change of the defined office; effective date from the Table; the text before is "Chief Minister" per Schedule 2 paragraph 1(e) of the Order |
| E5 | Endnotes, Table of Legislation History, row E5 | Dormant Bank Accounts (Jersey) Law 2017 | L.1/2017 (Dormant Bank Accounts (Jersey) Law 2017), 16 December 2019: Schedule 1 amended | encoded | g7-vintages | G7 | note: the two "subject to Article 20(1)" additions; the Act appointing 16 December 2019 is not in the sources |
| E6 | Endnotes, Table of Legislation History, row E6 | Revenue Administration (Jersey) Law 2019 | L.13/2019 (Revenue Administration (Jersey) Law 2019), 1 January 2020 (R&O.136/2019): Article 1 "Comptroller" | encoded | g7-vintages | G7 | note: substitutes "Revenue Administration (Jersey) Law 2019" for "Income Tax (Jersey) Law 1961"; R&O.136/2019 is not in the sources |
| E7 | Endnotes, Table of Legislation History, row E7 | States of Jersey (Minister for Children and Education, | R&O.29/2021, 2 March 2021: Article 1 amended | encoded | g7-vintages | G7 | note: the instrument is NOT in the sources; the text it produced is inferred from R&O.28/2023 (the words replaced there): trap T29 |
| E8 | Endnotes, Table of Legislation History, row E8 | States of Jersey (Transfer of Financial Services Functions | R&O.28/2023, 12 April 2023: "Minister for External Relations and Financial Services" replaced by "Chief Minister" | encoded | g7-vintages | G7 | note: made 5 April 2023, in force 7 days after: fork F7.2 |
| E9 | Endnotes, Table of Legislation History, row E9 | Changes to Ministerial Offices (Jersey) Amendment Order | R&O.10/2024, 9.30 a.m. on 27 February 2024: "Chief Minister" replaced by "Minister for External Relations" | encoded | g7-vintages | G7 | note: time-of-day boundary: trap T3, fork F7.1 |
| E10 | Endnotes, Table of Legislation History, row E10 | Charities (Entities) Law (Jersey) Amendment Order 2025 | R&O.56/2025, 16 October 2025: paragraph (ba) inserted in Article 2(1), made under Article 2(2) | encoded | g7-vintages | G7 | note: made 9 October 2025, in force 7 days after: fork F7.2 |
| E11 | Endnotes, Table of Legislation History, row E11 | States of Jersey (Transfer of Functions) Order 2026 | R&O.102/2026, 2 October 2026: "Minister for External Relations" replaced by "Chief Minister" | encoded | g7-vintages | G7 | note: made 25 September 2026, in force 7 days after: fork F7.2 |
| R1 | Endnotes, Table of Renumbered Provisions, row R1 | 41 | Table of Renumbered Provisions: original 41, spent, omitted | refused | g7-commencement | G7 | what the original Article 41 provided is not in the sources (R&O.17/2018 headings suggest taxation); it was in the stage 3 remainder, so a named refusal for its content |
| R2 | Endnotes, Table of Renumbered Provisions, row R2 | 42 | original 42 is now Article 41 | encoded | g7-commencement | G7 | note: fixes which stage the present Article 41 is in: trap T1 |
| R3 | Endnotes, Table of Renumbered Provisions, row R3 | 43 | original 43 is now Article 42 | encoded | g7-commencement | G7 |  |
| R4 | Endnotes, Table of Renumbered Provisions, row R4 | 44(1) | original 44(1) is now Article 43 | encoded | g7-commencement | G7 |  |
| R5 | Endnotes, Table of Renumbered Provisions, row R5 | 44(2) | original 44(2), spent, omitted | inert | g7-commencement | G7 | spent; its effect (the stage 1 commencement) is in E1; R&O.17/2018 Article 2 says 44(2) brought the stage 1 provisions into force |
| R6 | Endnotes, Table of Renumbered Provisions, row R6 | 44(3) | original 44(3), spent, omitted | inert | g7-commencement | G7 | spent; content not in the sources and nothing depends on it |
| N1 | Endnotes, Table of Endnote References, note 1 | [1] Article 1 amended | endnote [1]: Article 1 amended by R&O.40/2019, L.13/2019, R&O.29/2021, R&O.28/2023, R&O.10/2024, R&O.102/2026 | encoded | g7-vintages | G7 | note: the list of instruments that changed Article 1; the vintage table is built from it |
| N2 | Endnotes, Table of Endnote References, note 2 | [2] Article 2(1) amended | endnote [2]: Article 2(1) amended by R&O.56/2025 | encoded | g7-vintages | G7 |  |
| N3 | Endnotes, Table of Endnote References, note 3 | [3] Article 19(1) editorial change, in sub-paragraph (e), “law or | endnote [3]: Article 19(1) editorial change in (e), "law or Jersey" to "law of Jersey" | inert | g7-vintages | G7 | a typographical correction; no change of meaning |
| N4 | Endnotes, Table of Endnote References, note 4 | [4] Article 31 editorial | endnote [4]: Article 31 editorial change in (c), "for purpose of" to "for the purpose of" | inert | g7-vintages | G7 | a typographical correction; no change of meaning |
| N5 | Endnotes, Table of Endnote References, note 5 | [5] Schedule 1 amended | endnote [5]: Schedule 1 amended by L.1/2017 | encoded | g7-vintages | G7 | note: see E5 |


### Reasons for every inert, refused and out-of-scope row

Each such row also carries its own reason in the table. Here they are grouped; every non-`encoded` row appears in exactly one group below (106 rows).

- **inert: 3 rows.** The short title, the long title and the "Commencement [see endnotes]" line state purpose or point elsewhere; they gate nothing and compute nothing. The commencement itself is encoded from the endnote rows.
  Rows: Title, Long title, Commencement note.
- **inert: 23 rows.** Article 1 definitions that only name the Article in which the term is defined or the role it denotes ("annual return" is a return sent under 13(7); "entity" has the meaning in 2(1); "Commissioner", "court", "tribunal" are roles carried by the `Legal actor` constructors; "prescribed" is a rule of construction that the fleet implements by treating the content of an Order as an input; "regulated financial services business" is used only in the content of Regulations and of a court order). The operative rule is encoded where the term is defined, and the stub quotes the Article 1 line so the module can be read beside the source.
  Rows: 1[annual return], 1[charitable purpose], 1[Commissioner], 1[constitution], 1[constitutional Law], 1[court], 1[donation], 1[entity], 1[general section], 1[governor], 1[Jersey entity], 1[misconduct], 1[prescribed], 1[purpose], 1[register], 1[registered charitable purposes], 1[registered public benefit statement], 1[regulated financial services business], 1[reportable matter], 1[required steps notice], 1[restricted section], 1[solicit], 1[tribunal].
- **out-of-scope: 12 rows.** Article 1 definitions that restate another enactment ("company", "foundation", "trust", "property", "JFSC", "Loi of 1862", "incorporated 1862 association", "court-approved fidéicommis", and the four limbs of "regulated financial services business"). The text of those enactments is not in the sources; whether a body is one is an input fact to Article 2.
  Rows: 1[company], 1[court-approved fidéicommis], 1[foundation], 1[incorporated 1862 association], 1[JFSC], 1[Loi of 1862], 1[property], 1[regulated financial services business](a), 1[regulated financial services business](b), 1[regulated financial services business](c), 1[regulated financial services business](d), 1[trust].
- **inert: 8 rows.** Establishment, status and citation: Article 3 (the Commissioner is established; Schedule 1 makes further provision), Article 32 (the Tribunal is established, with its function; Schedule 2 makes further provision), Article 43 (citation). They create or name a body or point at a Schedule; nothing is computed from them. The actors are `the Commissioner` and `the Charity Tribunal`; the appeal rights are encoded at 33 to 35.
  Rows: 3, 3(1), 3(2), 32, 32(1), 32(2), 32(3), 43.
- **inert: 10 rows.** Statements of function and illustrations that carry no precondition or outcome: 4(1)(a), (b), (c), (e), (f), (g) (the powers and duties are encoded where conferred, Parts 3 to 8; 4(1)(d), the one duty with no other home, is encoded) and 4(3) with (a) to (c), which are "without prejudice to the generality" of the permission in 4(2).
  Rows: 4(1)(a), 4(1)(b), 4(1)(c), 4(1)(e), 4(1)(f), 4(1)(g), 4(3), 4(3)(a), 4(3)(b), 4(3)(c).
- **inert: 22 rows.** Illustrative or subject-matter lists for the content of an Order or Regulations whose content is an input and whose text is not in the sources: 25(2) and its limbs (what statements an Order may require), 28(2)(b) and (b)(iii) (how an Order may distinguish charities), and Schedule 2 paragraph 4(3)(a) to (e), (g) to (j) (what the tribunal Regulations may cover). The powers themselves are encoded (25(1), 28(1), Sch 2 4(3)); Sch 2 4(3)(f) is encoded because it caps a penalty.
  Rows: 25(2), 25(2)(a), 25(2)(a)(i), 25(2)(a)(ii), 25(2)(a)(iii), 25(2)(a)(iv), 25(2)(a)(v), 25(2)(a)(vi), 25(2)(b), 25(2)(c), 25(2)(d), 28(2)(b), 28(2)(b)(iii), Sch2 4(3)(a), Sch2 4(3)(b), Sch2 4(3)(c), Sch2 4(3)(d), Sch2 4(3)(e), Sch2 4(3)(g), Sch2 4(3)(h), Sch2 4(3)(i), Sch2 4(3)(j).
- **out-of-scope: 2 rows.** The Scottish and United Kingdom statutes named in 28(2)(b)(i) and (ii) (the Charities and Trustee Investment (Scotland) Act 2005; section 10(2) of the Charities Act 2011); their text is not in the sources and what they decide is an input to the content of an Order.
  Rows: 28(2)(b)(i), 28(2)(b)(ii).
- **inert: 1 rows.** Article 40(1) is a rule of construction (nothing in the Law derogates from the independent powers of the Attorney General, the Bailiff or the court); it gates no decision and computes nothing. Compare 14(5)(a), which is encoded as a statement beside the court's power.
  Rows: 40(1).
- **out-of-scope: 9 rows.** Articles 41 and 42 (original 42 and 43) are enabling powers of the States to make Regulations amending OTHER enactments: 41 the Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008, any other enactment under which the JFSC has functions, any enactment relating to taxation, so that supervisory bodies, the JFSC and the Comptroller may disclose information to the Commissioner; 42 the Trusts (Jersey) Law 1984, the Foundations (Jersey) Law 2009 and any enactment referring to charities. Neither those enactments nor any Regulations are in the sources, and nothing else in the Law reads the result.
  Rows: 41, 41(1), 41(1)(a), 41(1)(b), 41(1)(c), 41(2), 42, 42(a), 42(b).
- **inert: 11 rows.** Statements of legal status and capacity with no precondition, input or outcome in this Law: Schedule 1 paragraph 2(1) (the capacities of a corporation sole), 2(2) (independence), 2(3) (no contract of employment), and restatements of the terms of appointment (Sch 1 1(4), 1(8); Sch 2 1(4)). Employment law is outside the sources. The rules that bind (who pays, the directions that may be given) are encoded at Sch 1 2(4), 4(11), 4(12).
  Rows: Sch1 1(4), Sch1 1(8), Sch1 2(1), Sch1 2(1)(a), Sch1 2(1)(b), Sch1 2(1)(c), Sch1 2(1)(d), Sch1 2(1)(e), Sch1 2(2), Sch1 2(3), Sch2 1(4).
- **refused: 1 rows.** R1, the original Article 41, "spent, omitted": it was in the stage 3 remainder (so it came into force on 1 January 2019) and R&O.17/2018's headings suggest it concerned taxation, but what it provided is not in the sources. A question about its content answers with a named `REFUSE`; a question about its commencement is answered from E3.
  Rows: R1.
- **inert: 4 rows.** R5 and R6 (original 44(2) and 44(3), spent, omitted; their effect, the stage 1 commencement, is in E1) and the two editorial endnotes N3 and N4, which correct typography ("law or Jersey" to "law of Jersey"; "for purpose of" to "for the purpose of") and change no meaning.
  Rows: R5, R6, N3, N4.

### Judgement calls in the dispositions

These are the rows where a different disposition was defensible.
Each is stated with what an encoder gains or loses by changing it; an encoder may change a disposition by registering the change in the `FRAGMENT`.

- **J1: Article 4(1) is mostly inert, with one encoded limb.** The six statements of function (a), (b), (c), (e), (f), (g) have no precondition or outcome and the powers they point at are encoded where conferred; (d) ("publish and maintain guidance") is a duty with no other home, so it is encoded. The cost of treating (a) to (c) as encoded would be rules that restate Parts 3 to 6.
- **J2: Article 4(2) is encoded, the illustrations in 4(3) are inert.** 4(2) is a permission with one exclusion (acting as a governor), and the exclusion is checkable; 4(3) is "without prejudice to the generality" of it.
- **J3: Article 4(4) is encoded as a recorded determination, not as a computation.** "So far as appears reasonably practicable" and the two limbs are the Commissioner's judgement; the rule only records whether the Commissioner sought to act that way.
- **J4: Article 2(4), (5), (6) are encoded as total lookups from the kind of entity**, although every use of "constitution", "constitutional Law" and "purpose" reads an input document. Reason: the lookup is the only place the gap in 2(5) (T6) becomes testable, and 2(4)(g) "in whatever form" beside 11(4)(b) "a written document" is checked there. If an encoder prefers, these three may become inert with the gap carried by T6 in NOTES.
- **J5: the Article 1 pointers are inert, and their stubs live in G1's module** (`g1-art1-defined-terms`) even where the target is another group's Article (donation, solicit, general section, restricted section, register): G1 cannot write into another group's module.
- **J6: "Commissioner", "court" and "tribunal" in Article 1 are inert as definitions** and carried as the `Legal actor` constructors; who holds the office on a day is Schedule 1 paragraph 4(5) (G9, IP28).
- **J7: "regulated financial services business" is inert** although it names a class; only 11(7)(a) and 14(3)(e) use it and both are the content of Regulations or an order. Its four limbs are registrations under other Laws and are `out-of-scope`.
- **J8: Articles 41 and 42 are `out-of-scope`, not powers.** The BRIEF pins them so. Each is an enabling power of the States to make Regulations amending other enactments; the powers are not encoded as `MAY` rules (the Regulations and the enactments they would amend are not in the sources). The alternative, a typed `MAY` for each, costs two rules and changes no answer.
- **J9: Article 40(1) is inert; 40(2) and (3) are encoded as powers.** 40(1) is a rule of construction (nothing in the Law derogates from independent powers). 40(3) (transitional provision for bringing the Law into force) is spent in practice after commencement; it is encoded for completeness.
- **J10: Article 32 is inert, the appeal rights are encoded at 33 to 35.** 32(2) declares the Tribunal's only function, which 33 to 35 implement.
- **J11: Article 25(2) and 28(2)(b), and Schedule 2 paragraph 4(3)(a) to (e), (g) to (j), are inert**: they illustrate or list the possible content of an Order or Regulations whose content is an input (Schedule 2 paragraph 4(3)(f) is encoded because it caps the penalty the Regulations may create).
- **J12: Schedule 1 paragraph 2(1) (the corporation sole's capacities) and 2(2), 2(3) are inert**; 2(4) is encoded because it says who pays; 1(4), 1(8) and Schedule 2 1(4) restate the terms of appointment.
- **J13: the "have regard" duties (5(5), 7(2), 11(6)(c) and (d)) are encoded as recorded facts**: the rule asks whether regard was had; it does not compute what the regard concludes.
- **J14: each power to prescribe by Order or Regulations is encoded as a typed `MAY` with the content as an input**, including where no Order exists in the sources. Where the Order would set a period or a due date (11(8)(a)(i), 13(8), 36(2)(a)), the question "is it late" is a named refusal until the period is supplied.
- **J15: 9(3) is encoded as a constraint on the content of the Order** (what it "must" prescribe), because a missing element would make the Order not comply; the alternative is to treat the Order as an opaque input.
- **J16: the stage rows E1 to E3 and the nine instrument rows E4 to E11 are `encoded`** (the in-force function and the vintage resolver); R1 (the original Article 41) is `refused` because what it said is not in the sources, and R5, R6 are inert because they are spent and their effect is in E1.
- **J17: the editorial endnotes [3] and [4] are inert**: they correct typography ("law or Jersey", "for purpose of"); they do not change a meaning. Whether the enacted text had the error is unknown (T29).
- **J18: coverage granularity.** Every node of the parsed text is a row, down to sub-sub-paragraphs, so that a test author can ask for "every row of Article 21" and a missed limb shows. Where a sub-paragraph is only an item of a list whose parent row carries the rule (6(1)(a) to (p), 8(3)(a) to (n), 26(11)(a) and (b)), the row is still `encoded` and its note says it is carried by the parent's rule.

## (b) Group map

The map of the fleet lead is kept: nine groups, the numbering and the prefixes as given.
**No change to the group map is proposed.**
G7 is the lightest in volume and the heaviest in judgement (the offences of Part 6, the temporal axis); if it runs long, `g7-vintages` is the module the integrator can hand to another encoder, because it depends on nothing but `domain.l4`.
G9 is housekeeping in kind but carries ten periods; its counting forks (F9.1 to F9.7) are the larger part of its work.

**Conventions for every group.**

- **Names.** A row of the tables below that compresses several rules (for example `Art 19(3)`, `Art 19(4)` or `Sch 2 para 1(1)` to `(8)`) stands for one export per paragraph, each named by the same pattern (`Art 19(3) ...`, `Art 19(4) ...`); it is not licence to invent names outside the pattern. Rule names start `Art N(p) ...` or `Sch N para P(s) ...` (Commencement and endnote rules start `Commencement:` and `Endnotes:`), so they are unique across the fleet. The names below are the exports and they are the names the integrator and the test authors will call; helpers are free.
- **Shape.** A duty, power or prohibition is a regulative rule typed `DEONTIC \`Legal actor\` \`Act under <scope>\``, where the action enumeration is the group's own, and the precondition is a computable condition; the CONTENT of an Order, notice or court order is an input. A definition that decides an outcome is a `BOOLEAN` (or enumeration) rule. An evaluative standard is a `GIVEN` fact named for what it decides.
- **Forks.** One record `Interpretation of <scope>` per group (named below), one field per fork, each field `TYPICALLY` reading A of section (g); every public decision that depends on a fork takes the record as an ordinary `GIVEN` and delegates by `CONSIDER` to one private implementation per reading.
- **Inputs.** The standard names of section (c), exactly; a fact decided by another group is a `GIVEN` and a "nouns request" or a FRAGMENT line, never a call.
- **Headline exports** carry `@export` with a sentence saying what question they answer; every `GIVEN` carries `@desc`.
- **Tests.** In modules of their own, `gK-tests-<module>`; expected values from the source (the worked cases of section (g) are source-derived); a refusal is asserted with `#ASSERT REFUSED`.
- **Imports.** `prelude`, `daydate`, `domain` and the group's own modules only.

### G1: Articles 1 and 2 (interpretation; definition of entity and related terms)

Source: Article 1 (35 definitions), Article 2(1) to (10); about 1,950 words; coverage rows 113 (76 encoded, 25 inert, 12 out-of-scope).
Interpretation record: `Interpretation of Articles 1 and 2` (forks F1.1 to F1.5).

| module | holds |
| --- | --- |
| `g1-art1-defined-terms` | the Article 1 definitions that decide something: "Minister" by vintage, "Comptroller" by vintage, "registered charity", "publish"; every other definition as a labelled inert stub quoting the source line (pointers and other-statute terms), so the module can be read beside Article 1 |
| `g1-art2-entity` | Article 2(1) to (6): the raw facts about a body, the kinds of entity (with (ba) by vintage), "Jersey entity", the power in 2(2), and the lookups for "constitution", "constitutional Law" (MAYBE) and "purpose" |
| `g1-art2-governor-misconduct` | Article 2(7) to (10): "governor", "relevant unincorporated entity", "misconduct" |
| `g1-tests-art1`, `g1-tests-art2-entity`, `g1-tests-art2-governor-misconduct` | tests from the source |

Types needed from `domain.l4`: `Vintage of the text`, `Office of the Minister`, `Kind of entity`, `Standing on the register`, `Legal actor`, `Entity`, `Governor`, `Kind of reportable matter` (for the governor list), `Required steps notice`.
Group-local types: `Law defining the Comptroller` (`the Income Tax (Jersey) Law 1961`, `the Revenue Administration (Jersey) Law 2019`); `Facts about the body under Article 2` (one `BOOLEAN` per sub-paragraph of 2(1) as a witness would state it, `established under the law of Jersey`, `the law governing the relationship between the persons constituting the body is the law of Jersey`, `sub-paragraphs added by Order`, `governors`); `Facts about a person's role in an entity` (trustee or fidéicommissaire, council member, director, management-committee member, has general control and management under the constitution, exercises it on behalf of another who has it in own right, alone or with others); `Facts about conduct under Article 2(10)` (one `BOOLEAN` per limb (a)(i) to (iv) and (b)(i) to (vi), plus `the offence is in relation to a registered charity, an excepted foreign charity or an equivalent`).

| export | takes | gives |
| --- | --- | --- |
| `Art 1 the Minister under the text of` | `the vintage of the text` (IP2) | `Office of the Minister`; REFUSE for `before the first consolidated version`; comment "inferred" on the 2021 row |
| `Art 1 the Law that defines the Comptroller under the text of` | `the vintage of the text` | `Law defining the Comptroller`; the Income Tax Law until 31 December 2019 |
| `Art 1 the entity is a registered charity` | `the entity` (IP5) | BOOLEAN: standing is the general or the restricted section (IP6) |
| `Art 1 the information has been published` | `the publisher's opinion is that the manner of publication is likely to bring the information to the attention of the public or of those affected` : BOOLEAN | BOOLEAN (F1.5) |
| `Art 2(1) the kinds of entity the body falls within` | the interpretation, `the vintage of the text`, the raw facts | `LIST OF Kind of entity` (empty if none); (ba) only from the text of 16 October 2025 |
| `Art 2(1) the body is an entity` | as above | BOOLEAN |
| `Art 2(2) the Minister may add a sub-paragraph to Article 2(1)` | none | DEONTIC `Legal actor` `Act under Article 2`; the added label is an input |
| `Art 2(3) the body is a Jersey entity` | the interpretation, the vintage, the raw facts | BOOLEAN (IP5 field `is a Jersey entity`) |
| `Art 2(4) the constitution of the entity consists of` | a `Kind of entity` | `STRING` |
| `Art 2(5) the constitutional Law of the entity is` | a `Kind of entity`, the interpretation | `MAYBE STRING` (T6, F1.3) |
| `Art 2(6) the purpose of the entity means` | a `Kind of entity` | `STRING` |
| `Art 2(7) the person is a governor of the entity` | the interpretation, the kinds, the role facts | BOOLEAN (F1.4) |
| `Art 2(8) the entity is a relevant unincorporated entity` | the kinds, `the Commissioner has published a model constitution that provides for a management committee` : BOOLEAN, `the constitution conforms to that model` : BOOLEAN | BOOLEAN |
| `Art 2(10) the conduct is misconduct` | the interpretation, the conduct facts, `the entity is an excepted foreign charity` (IP26), `the charity or governor has contravened a provision of this Law or an enactment under it` (IP13), `the required steps notices served` (IP19) | BOOLEAN (IP12; F1.2) |

Look at: T3 (the five texts of "Minister", the 9.30 a.m. change, which G1 does not resolve: it takes the vintage), T5, T6, T8, T25, T30; `a Minister` in 5(2)(a) is G2's. The definitions "Commissioner", "court" and "tribunal" are roles, not rules. Keep the quotation of each source line above its stub (`srcrefs.py quote`) and run `check --refs`.
Tests from the source: each of the 11 kinds, one body per sub-paragraph; a body in two kinds (a company that is a sole trustee: (a) and (f)); a (ba) body in the text of 15 October and 16 October 2025; a Jersey entity by 2(3)(b) with a resident governor and with a governor that is itself a Jersey entity by (a) (and one that is a Jersey entity only by (b): not enough); a governor for each of 2(7)(a) to (e); 2(9)(a) (an agent is not a governor) and (b); misconduct for each limb of 2(10), including 2(10)(b)(iii) with and without the connection to a charity; `Art 1 the Minister` for each of the nine vintages.

### G2: Articles 3 to 7 (the Commissioner and its functions; the charity test, charitable purposes, public benefit)

Source: Articles 3 to 7; about 1,550 words; coverage rows 90 (77 encoded, 13 inert).
Interpretation record: `Interpretation of Articles 3 to 7` (forks F2.1 to F2.5).

| module | holds |
| --- | --- |
| `g2-art3-4-commissioner` | Article 3 as an inert stub; Article 4: the duty to publish and maintain guidance, the permission with its one exclusion, the standard of conduct as a recorded determination |
| `g2-art5-charity-test` | Article 5: the test and its bar, the Minister's power to disapply, the guidance duties |
| `g2-art6-purposes` | Article 6: the heads, their clarifications, the States' power, its limit, the political-purpose exclusion |
| `g2-art7-public-benefit` | Article 7: what the decision-maker must have regard to and must not do |
| `g2-tests-*` | tests per module |

Types needed from `domain.l4`: `Entity`, `Purpose`, `Head of charitable purpose`, `Legal actor`, `Office of the Minister` (for F2.3 B).
Group-local types: `Facts about the constitution under Article 5(2)` (`the constitution expressly permits activities to be directed or controlled by`, `... a governor to be`, each over `a Minister`, `a member of the States Assembly`, `an equivalent in another jurisdiction`, and `acting in that capacity`); `Determination of public benefit` (the decision-maker, whether regard was had to each limb of 7(2), whether the entity benefits only identified natural persons, whether a presumption was applied); `Act of the Commissioner under Article 4 or 5`.

| export | takes | gives |
| --- | --- | --- |
| `Art 4(1)(d) the Commissioner must publish and maintain guidance on the operation of the Law` | none | DEONTIC `Legal actor` act; no deadline |
| `Art 4(2) the Commissioner may do the thing` | `the thing is calculated to facilitate, or is conducive or incidental to, a function` : BOOLEAN; `the thing is acting as a governor of a charity or of an entity with charitable purposes` : BOOLEAN | BOOLEAN or a MAY rule |
| `Art 4(4) the Commissioner has sought to act as Article 4(4) requires` | the recorded determination (both limbs, and the "so far as reasonably practicable" input) | BOOLEAN |
| `Art 5 the entity meets the charity test` | the interpretation, `the entity`, the constitution facts, the public benefit determination, `an Order under Article 5(3) disapplies Article 5(2) for the entity` : BOOLEAN | BOOLEAN, `@export` (IP8) |
| `Art 5(1)(a) all of the entity's purposes are charitable or purely ancillary` | the interpretation, `the entity` | BOOLEAN (F2.1) |
| `Art 5(2) the constitution defeats the charity test` | the interpretation, the constitution facts | BOOLEAN (F2.2, F2.3, IP3) |
| `Art 5(3) the Minister may disapply Article 5(2)` | none | DEONTIC; the entity or description is an input |
| `Art 5(3) the entity meets the charity test only by virtue of an Order` | as `Art 5` | BOOLEAN (IP10) |
| `Art 5(4) the Commissioner must publish and maintain guidance on the charity test` | none | DEONTIC |
| `Art 5(6) the Commissioner must consult and publish a report before issuing or amending guidance` | none | DEONTIC chain: consult, then publish the report |
| `Art 5(7) the Commissioner must give the Minister the guidance and the report` | the interpretation | DEONTIC (F2.4) |
| `Art 5(8) the Minister must lay the guidance and the report before the States` | the interpretation | DEONTIC (F2.4) |
| `Art 6(1) the purpose is a charitable purpose` | the interpretation, a `Purpose` | BOOLEAN: a head, not excluded by 6(5) |
| `Art 6(3) the States may add a sub-paragraph to Article 6(1) or (2)` | none | DEONTIC `Legal actor` `the States`; "on the recommendation of the Commissioner" is a guard |
| `Art 6(4) the Regulations are within the power of Article 6(3)` | whether they amend or restrict 6(1)(a) to (p), 6(2)(a) to (f), or alter 6(5) | BOOLEAN |
| `Art 6(5) the purpose is neither charitable nor ancillary` | a `Purpose` | BOOLEAN |
| `Art 6 the entity has a purpose within the advancement of religion` | the interpretation, `the entity` | BOOLEAN (IP11; F2.5) |
| `Art 7 the entity provides public benefit` | the determination | BOOLEAN; the decision-maker is the Commissioner, the tribunal or the court |
| `Art 7(3) the determination is permitted` | the determination | BOOLEAN: no presumption; identified persons are not a section of the public |

Look at: T4, T27, F2.1 to F2.5. The guidance duties are standing duties with no deadline: assert them with `#TRACE`, not `#ASSERT`. 5(5) and 7(2) "have regard" are recorded facts. The Order or Regulations under 5(3) and 6(3) are inputs; no Order is in the sources.
Tests from the source: a purely educational entity meets the test; an entity with a political-party purpose does not (6(5)) even as an ancillary purpose; the 5(2) bar for a Minister, a member of the States Assembly, an equivalent; the Order that disapplies it (8(3)(i) sees it); one test per head (a) to (o) and a (p) analogue; the 6(2) clarifications (health includes relief of suffering; sport needs physical skill and exertion; 6(1)(i) only for the needy or the public at large or all-male/all-female public).

### G3: Articles 8 to 10 (the register, the restricted section, public access)

Source: Articles 8 to 10; about 1,530 words; coverage rows 82 (all encoded).
Interpretation record: `Interpretation of Articles 8 to 10` (forks F3.1 to F3.3).

| module | holds |
| --- | --- |
| `g3-art8-register` | the register's sections, the fourteen entries, the principal address, the historic-section entries, the retention duty |
| `g3-art9-restricted-section` | the public elements, the request, the Order's required content, the Commissioner's conditions and the refusal |
| `g3-art10-public-access` | the duty to publish, the Order for other access, the public parts, the safety designation |

Types needed from `domain.l4`: `Registered charity`, `Entity`, `Standing on the register`, `Kind of entity`, `Governor`, `Required steps notice`, `Basis of deregistration`, `Meaning of the year of an annual return`, `Legal actor`.
Group-local types: `Entry required by Article 8(3)` (14 constructors (a) to (n)), `Entry required by Article 8(5)` (5), `Element of the restricted section` (the 9(1) elements), `Full register entry` (wraps `Registered charity`; adds addresses, other premises, annual-return flag, notes).

| export | takes | gives |
| --- | --- | --- |
| `Art 8(1) the Commissioner must establish and maintain the register` | none | DEONTIC |
| `Art 8(3) the entries required for the registered charity` | `the registered charity`, the facts that condition (h), (i), (k), (l), (m) | `LIST OF Entry required by Article 8(3)` |
| `Art 8(3)(a) the status note of the entity` | `the entity` | the sub-paragraphs and the enactment details for (e), (g), (h), (j) |
| `Art 8(4) the principal address of the registered charity` | the interpretation of the entity's constitutional Law, the premises, the governors' addresses | `MAYBE STRING` |
| `Art 8(4) the entity has a principal address in Jersey` | the same | BOOLEAN (IP17) |
| `Art 8(5) the entries required in the historic section` | `the registered charity`, `the basis of deregistration` (IP32) | `LIST OF Entry required by Article 8(5)` |
| `Art 8(6) the Commissioner must retain the copy for 10 years` | none | DEONTIC (F3.1) |
| `Art 8(6) the Commissioner may discard the copy on` | the interpretation, the copy's receipt date, the deregistration date | `DATE` (F3.1) |
| `Art 9(1) the public elements of the restricted section` | `the registered charity` | `LIST OF Element of the restricted section` |
| `Art 9(2) the request for entry in the restricted section may be made` | `the entity`, the funding condition met, any other prescribed condition met | BOOLEAN |
| `Art 9(3) the Order contains what Article 9(3) requires` | the Order's content flags | BOOLEAN |
| `Art 9(6) the Commissioner may enter the charity in the restricted section` | the three satisfactions as inputs | BOOLEAN |
| `Art 9(7) the Commissioner must give written notice of the refusal` | none | DEONTIC |
| `Art 9(7) the Commissioner may proceed on the stated intention` | the stated intention | DEONTIC MAY |
| `Art 10(1) the Commissioner must make the public parts of the register available on a website` | none | DEONTIC |
| `Art 10(2) the Minister may by Order provide for other access` | none | DEONTIC MAY |
| `Art 10(3) the matter is in a public part of the register` | the section, the designation | BOOLEAN (IP25) |
| `Art 10(5) the Commissioner may designate the matter as not a public part` | the Commissioner's consideration (safety), the standing (F3.3) | DEONTIC MAY |

Look at: T7, T14, T16, T24; the entry list 8(3) is conditional (a charity not in the restricted section has no 9(1) elements; (h) only if an organized religious charity). 8(3)(a)(ii) does not list (ba). The register note is a rule over the kinds list.
Tests from the source: each of the fourteen entries present or absent; the principal address cascade (registered office; main premises, not a private dwelling house; governor's address) with a case for each; the restricted-section public elements exclude the name but include the number and the 8(3)(k) note; a historic-section entry for a general-section and a restricted-section charity (8(5)(b)); the 9(6) refusal and the 9(7) notice.

### G4: Articles 11 and 12 (application to register; name of charity)

Source: Articles 11 and 12; about 1,350 words; coverage rows 73 (all encoded).
Interpretation record: `Interpretation of Articles 11 and 12` (forks F4.1 to F4.5).

| module | holds |
| --- | --- |
| `g4-art11-application` | the application, its content, the Commissioner's duty to register or refuse, the powers, the certificate, the Non-Profit Organizations pass-through |
| `g4-art12-name` | undesirable names, the registered name and number, changes, the prohibition on other names |

Types needed from `domain.l4`: `Entity`, `Registered charity`, `Standing on the register`, `Legal actor`, `Decision of the Commissioner`.
Group-local types: `Application for registration` (the dates lodged and complete, the 11(2) items present as BOOLEANs, the payments to governors as dated amounts, the Commissioner's opinion that the activity is substantial), `Act under Article 11`, `Act under Article 12`.

| export | takes | gives |
| --- | --- | --- |
| `Art 11(1) the entity may apply` | none | DEONTIC MAY |
| `Art 11(2) the application includes what Article 11(2) requires` | the application | BOOLEAN |
| `Art 11(2)(e)(ii) the payment to a governor is within the period` | the interpretation, the application, the payment date | BOOLEAN (F4.1, F4.2) |
| `Art 11(4)(c) the requirement is met` | `the entity`, the opinion that the activity is substantial | BOOLEAN (IP15) |
| `Art 11(4)(d) the requirement is met` | `the entity has a principal address in Jersey within Article 8(4)` (IP17) | BOOLEAN (IP16) |
| `Art 11(4) the Commissioner must register the applicant` | `the entity meets the charity test` (IP8), `the applicant has complied with Article 19(5)` (IP22), `Article 19(9)(c) bars granting the application` (IP23), `the court has ordered that the entity must not be registered as a charity` (IP24), `the name is undesirable under Article 12(1)` (IP18), the constitution is a written document, the prescribed grounds | DEONTIC (F4.3, F4.4) |
| `Art 11(5) the Commissioner must refuse to register the applicant` | as above | DEONTIC |
| `Art 11 what the Commissioner must do on the application` | the above | `MAYBE Decision of the Commissioner`; NOTHING for an incomplete application (F4.3); `@export` |
| `Art 11(3) the States may prescribe further information`, `Art 11(7) ... further grounds`, `Art 11(8) the Minister may make provision on the decision period and relieve small applicants` | none | DEONTIC MAY, three rules |
| `Art 11(6) the Commissioner must publish and maintain guidance on substantial activity` | none | DEONTIC |
| `Art 11(9) the Commissioner must issue the certificate` | the registered name, number, date | DEONTIC |
| `Art 11(10) the applicant must provide additional information and request registration under the Non-Profit Organizations (Jersey) Law 2008` | `the entity is required to be registered under that Law and is not` : BOOLEAN | DEONTIC |
| `Art 11(11) the Commissioner must pass the request on; the JFSC must treat it as an application` | none | two DEONTIC rules |
| `Art 12(1) the name is undesirable` | the proposed name, the Commissioner's opinion on each of (a) to (d) | BOOLEAN (IP18; F4.5) |
| `Art 12(2) the Commissioner must enter the registered name and allocate and enter a number` | none | DEONTIC |
| `Art 12(4) the Commissioner must refuse permission to change or add a name` | `the name is undesirable under Article 12(1)` | DEONTIC |
| `Art 12(5) the Commissioner must enter the new or alternative registered name` | the grant, the notification | DEONTIC |
| `Art 12(6) the Commissioner may require the charity to apply to change its name` | `the charity reported a name matter under Article 13(6)(b)` : BOOLEAN | DEONTIC MAY |
| `Art 12(7) a registered charity must not use a name other than a registered or related name` | the name used, the Commissioner's opinion | DEONTIC SHANT |

Look at: T10, T28; the decision period of 11(8)(a)(i) is an input and "late" a named refusal. The six matters of 11(4) come from other groups as inputs (IP8, IP17, IP18); G4 does not call them.
Tests from the source: each of the six grounds failing singly; a satisfied application; the 12-month window with the four payment dates of F4.1; the (ba) NPO applicant (11(4)(c)(i) via Jersey entity); a foreign entity with a substantial Jersey activity ((c)(ii)); the Order 13(9)(b) draft statement present and absent.

### G5: Articles 13 and 14 (effects of registration; powers of the court over a registered charity)

Source: Articles 13 and 14; about 1,490 words; coverage rows 58 (all encoded).
Interpretation record: `Interpretation of Articles 13 and 14` (forks F5.1 to F5.5).

| module | holds |
| --- | --- |
| `g5-art13-effects` | the effects while registered: constitution provisions, public benefit, the restricted-section condition, the eight reports, the annual return, the Minister's Orders, the payment prohibition |
| `g5-art14-court-powers` | the court's power, its nine kinds of order, amendment and revocation, and the two savings |

Types needed from `domain.l4`: `Registered charity`, `Entity`, `Governor`, `Legal actor`, `Order of the court over a charity`, `Meaning of the year of an annual return`.
Group-local types: `Matter to report under Article 13(6)` (8 constructors (a) to (h)), `Act under Article 13`, `Act under Article 14`.

| export | takes | gives |
| --- | --- | --- |
| `Art 13(2) the provision of the constitution is of no effect` | `the registered charity`, whether the provision permits an amendment adding a non-charitable purpose | BOOLEAN; while registered only (13(1)) |
| `Art 13(3) the amendment of purposes is subject to evidence and approval` | evidence given, prior approval obtained | BOOLEAN |
| `Art 13(4) the registered charity must provide public benefit in accordance with its statement` | none | DEONTIC |
| `Art 13(5) the registered charity in the restricted section must ensure it meets its condition` | the condition met, the Commissioner's prior permission | DEONTIC |
| `Art 13(6) the registered charity must promptly report the matter` | the interpretation, the matter, `the requirement of Article 11(4)(c) is met` (IP15), `the requirement of Article 11(4)(d) is met` (IP16), `the name is undesirable under Article 12(1)` (IP18), the governor's reportable matters (IP21) | DEONTIC (F5.1) |
| `Art 13(7) the registered charity must send an annual return` | the interpretation, the due date (an input) | DEONTIC (F5.2, F5.5) |
| `Art 13(8) the Minister may by Order provide for the format and timing of the annual return` | none | DEONTIC MAY |
| `Art 13(9) the Minister may by Order require payment details, a statement of intentions, and entry on the register` | none | DEONTIC MAY (three rules) |
| `Art 13(10) the Minister may by Order relieve small charities` | the interpretation | DEONTIC MAY (F5.3) |
| `Art 13(11)(a) the registered charity must not make a payment inconsistent with its statement` | `an Order under Article 13(9) applies to the registered charity` (IP29), the statement | DEONTIC SHANT |
| `Art 13(11)(b) the registered charity may apply for permission to amend the statement` | none | DEONTIC MAY |
| `Art 13(12) the States may require a charity to avoid or report and remedy a later ground for refusal` | none | DEONTIC MAY |
| `Art 13(13) paragraphs (2) and (3) yield to an order under the Loi of 1862` | the kinds of entity, whether an order exists and is inconsistent | BOOLEAN |
| `Art 14(1) the court may exercise the powers on the application` | the interpretation, the applicant (Commissioner or Attorney General), `the conduct is misconduct within Article 2(10)` (IP12) | DEONTIC MAY, `@export` (F5.4) |
| `Art 14(3) the court may make the order` | an `Order of the court over a charity` | DEONTIC MAY (IP31) |
| `Art 14(4) the court may amend or revoke an order` | the applicant, who is an allowed applicant | DEONTIC MAY |
| `Art 14(5) the powers apply in addition to other powers and despite the constitution` | none | BOOLEAN statements, or comments |

Look at: T18, T15 (13(1) and the end of the regime), T24; 13(6) is eight reports under one lead-in, not eight separate deadlines; the reports (c) and (d) are about proposals and events; the prohibition 13(11)(a) has no penalty (IP13). Orders under 13(8) to (10) are not in the sources.
Tests from the source: each of the 13(6) reports; the annual return of a charity in a year; 13(2) on a clause that would add a political purpose; 13(3) with and without approval; the 14(1) applications by the Commissioner, the Attorney General and by someone else (not allowed); 14(4) by each of the four applicants and by a fifth.

### G6: Articles 15 to 20 (deregistration; effects of deregistration; governors' duties, reportable matters, fitness orders)

Source: Articles 15 to 20; about 2,250 words; coverage rows 99 (all encoded).
Interpretation record: `Interpretation of Articles 15 to 20` (forks F6.1 to F6.16).

| module | holds |
| --- | --- |
| `g6-art15-16-deregistration` | deregistration on application and in other cases |
| `g6-art17-after-deregistration` | retrospective effect, retention, the number, the remaining property, the court's powers over a deregistered entity |
| `g6-art18-governor-duties` | the governors' duties and "misconduct" for a governor |
| `g6-art19-20-fitness` | reportable matters, the reports and declarations, the bar on acting, the Commissioner's steps, the court's orders, disqualification and its offence |

Types needed from `domain.l4`: `Registered charity`, `Entity`, `Governor`, `Kind of reportable matter`, `Required steps notice`, `Basis of deregistration`, `Order of the court over a charity`, `Penalty provided`, `Fine provided`, `Legal actor`, `Decision of the Commissioner`.
Group-local types: `Act under Article 15 or 16`, `Act under Article 17`, `Act under Article 18`, `Act under Article 19 or 20`, `Disqualification order` (the person, the start date, the period, any leave), `Facts about a reported matter` (the issue determined or not, the order or notice complied with).

| export | takes | gives |
| --- | --- | --- |
| `Art 15(1) the registered charity may apply to be deregistered` | none | DEONTIC MAY |
| `Art 15(2) the entity must provide the information requested` | none | DEONTIC |
| `Art 15(3) the Commissioner must deregister or refuse` | the interpretation, `the entity has complied with Article 15(2)`, the proposals acceptable (an input) | DEONTIC (F6.1) |
| `Art 16(1) the Commissioner may deregister the entity` | the interpretation, `the entity meets the charity test` (IP8), `the required steps notices served` (IP19), the Commissioner was misled, a prescribed circumstance, satisfied that it is proportionate, objections invited for the reasonable time | DEONTIC MAY (F6.2, F6.13) |
| `Art 16(2) the Commissioner must deregister the entity that no longer exists` | the Commissioner is satisfied that it no longer exists | DEONTIC |
| `Art 16 the basis of deregistration` | the above | `Basis of deregistration` (IP32) |
| `Art 17(1)(a) the Commissioner must retain the information for 10 years` and `... may discard the information on` | the interpretation, the dates | DEONTIC; DATE (F6.5) |
| `Art 17(1)(b) the Commissioner must not assign the registered number` | the interpretation | DEONTIC SHANT (F6.6) |
| `Art 17(2) the deregistration takes effect retrospectively` | the four conditions | BOOLEAN |
| `Art 17(3) the date from which the termination takes effect` | the above | `MAYBE DATE` |
| `Art 17(4) the act is not rendered an offence by the retrospective effect` | the act date, the notice date (F6.3) | BOOLEAN |
| `Art 17(5) the property is remaining property` | the interpretation, the acquisition date | BOOLEAN (F6.4) |
| `Art 17(6) the entity must apply the remaining property for the preserved purposes` | `the registered charity` | DEONTIC |
| `Art 17(9) the court may exercise its Article 14 powers over the deregistered entity` | an `Order of the court over a charity`, the applicant, the conduct | DEONTIC MAY (IP31) |
| `Art 17(10) a governor may not apply without first notifying the Attorney General` | the notice given | BOOLEAN or SHANT |
| `Art 18(1) the governor must seek in good faith to ensure the charity acts consistently` | none | DEONTIC |
| `Art 18(2) the governor must act with due diligence and in utmost good faith` | the interpretation, the kinds of entity | DEONTIC (F6.7) |
| `Art 18(4) the governor engages in misconduct` | `the conduct is misconduct within Article 2(10)` (IP12), the other governors' conduct, concurrence, assistance, awareness, concealment | BOOLEAN (IP14; F6.8; T8) |
| `Art 19(1) the reportable matters of the person` | the person's facts | `LIST OF Kind of reportable matter` (IP21; F6.9) |
| `Art 19(2) the governor must report the reportable matter` | the interpretation | DEONTIC (F6.12) |
| `Art 19(3)`, `Art 19(4)` the declarations | none | two DEONTIC rules |
| `Art 19(5) the applicant has stated that it holds declarations` | the application, the declarations | BOOLEAN (IP22) |
| `Art 19(8) the person must not act as a governor while in breach of Article 19(2) or (4)` | none | DEONTIC SHANT, no penalty (F6.11, T9) |
| `Art 19(9)(a)` to `(e)` the Commissioner's steps | the interpretation, the reported matter | five DEONTIC rules; `(e)(i)` meets IP20 (F6.15) |
| `Art 19(9)(c) the Commissioner must not grant the application` | the fitness facts | DEONTIC SHANT and BOOLEAN (IP23) |
| `Art 19(10) the person must not act as a governor after reporting` | the interpretation, the permission and its conditions | DEONTIC SHANT (F6.10), penalty (IP30) |
| `Art 19(11) the penalty for contravening Article 19(10)` | none | `Penalty provided` (12 months, a fine with no maximum stated) |
| `Art 19(13) the Commissioner may apply to the court` | the suspicion | DEONTIC MAY |
| `Art 20(1) the court may make the order` | the application, the kind | DEONTIC MAY (IP24 for (c)) |
| `Art 20(3) the Commissioner or the Attorney General may apply for a disqualification order` | expedient in the public interest | DEONTIC MAY |
| `Art 20(4) the court may make a disqualification order` | unfit by conduct or by the seriousness of a reportable matter | DEONTIC MAY |
| `Art 20(5) the order's period is within the limit` | the interpretation, the start date, the end date | BOOLEAN (F6.14) |
| `Art 20(6) a person must not contravene a disqualification order` | the order | DEONTIC SHANT; penalty `Penalty provided` (24 months, a fine) |

Look at: T8, T9, T10, T11, T14, T15, T19; every F6.x. G6 is the largest group: the encoder should write modules in the order 18, 19-20, 15-16, 17 (18's misconduct is used by 19(1)(a)). The three offences, the standing duties and the powers each get their own `#TRACE`.
Tests from the source: each of the eight reportable matters; a governor who reports and acts without permission, one who does not report and acts, one with the Commissioner's permission under (9)(d) and one under (9)(e)(ii) with a condition breached; 16(1) on each of four grounds; 16(2); a retrospective deregistration (the four conditions) with the 17(4) edge; a disqualification order with a 15-year period and one of 16 years; the contravention offence.

### G7: Articles 21 to 25, 37 to 43, and the endnotes (the temporal axis)

Source: Articles 21 to 25 (Part 6), Articles 37 to 43 (Part 9), the endnotes; about 2,300 words; coverage rows 129 (101 encoded, 18 inert, 1 refused, 9 out-of-scope).
Interpretation record: `Interpretation of Articles 21 to 25, 37 to 43 and the endnotes` (forks F7.1 to F7.8).

| module | holds |
| --- | --- |
| `g7-art21-23-expressions` | the prohibitions on "charity", "registered by the Commissioner" and "Jersey charity"; the excepted foreign charity; the penalties |
| `g7-art24-25-powers` | the States' power to restrict "charitable"; the Minister's power on statements |
| `g7-art37-43-final` | officers' liability, service of notices, Regulations and Orders, savings; Articles 41 and 42 and 43 as stubs |
| `g7-commencement` | the staged commencement in original numbers, the renumbering map, the in-force function over both numberings |
| `g7-vintages` | the amendment history as data (instrument, made, in force, change) and the resolver from a day or an instant to a `Vintage of the text` |

Types needed from `domain.l4`: `Entity`, `Vintage of the text`, `Unit of the Law`, `Penalty provided`, `Fine provided`, `Legal actor`, `Required steps notice`.
Group-local types: `Act under Article 21 to 23`, `Statement made by an entity or person` (what was said, to whom, intent), `Stage of commencement` (`stage 1: 21 November 2014`, `stage 2: 1 May 2018`, `stage 3: 1 January 2019`, `not stated in the sources`), `Amending instrument` (identifier, date made, date in force or `9.30 a.m.`, effect, `in the sources` flag).

| export | takes | gives |
| --- | --- | --- |
| `Art 21(1) an unregistered entity must not say it is registered by the Commissioner` | `the entity is a registered charity` (IP6), the statement | DEONTIC SHANT; penalty level 3 |
| `Art 21(2) a person must not say that an unregistered entity is registered, with knowledge and intent` | the interpretation, the statement | DEONTIC SHANT; penalty 24 months and a fine (F7.4, F7.5) |
| `Art 21(3)`, `(4)` for a Jersey entity; `Art 21(5)`, `(6)` for one that is neither Jersey nor excepted | `the entity`, `the entity is an excepted foreign charity` (IP26), the statement | four DEONTIC SHANT rules (T25) |
| `Art 21(7) the prohibition applies to a person who is also the entity` | none | BOOLEAN |
| `Art 21(8) the States may prescribe exceptions` | none | DEONTIC MAY |
| `Art 21 the penalty for the contravention` | the paragraph contravened | `Penalty provided` (IP30) |
| `Art 22 the entity is an excepted foreign charity` | the established-under facts, the prescribed jurisdictions, the entity's own law's entitlement, management, `the entity is a registered charity` | BOOLEAN (IP26) |
| `Art 22(4) the Minister may exempt a specified entity from the first condition`, `Art 22(5) the States may amend the conditions` | none | DEONTIC MAY |
| `Art 23(1)`, `(2)` the "Jersey charity" prohibitions; `Art 23(3) the entity meets the conditions` | `the entity`, `the entity is a registered charity`, managed or controlled in or from Jersey | DEONTIC SHANT; BOOLEAN |
| `Art 24(1)`, `Art 24(3)`, `Art 24(4)` the States' Regulations on "charitable"; their limits | none | DEONTIC MAY; BOOLEAN limit (no imprisonment) |
| `Art 25(1) the Minister may by Order prescribe statements` | none | DEONTIC MAY |
| `Art 37(1) the officer is also guilty` | the interpretation, the body's kind, the officer's capacity, `the penalty provided for the offence` (IP30) | BOOLEAN and the penalty (F7.6) |
| `Art 37(2) a member of a body managed by its members is treated as a director` | none | BOOLEAN |
| `Art 38 the Minister may by Order make provision as to service` | none | DEONTIC MAY |
| `Art 38 the date on which the notice is served` | the interpretation, the dates sent and received | `DATE` (F7.7; IP34) |
| `Art 39(1)`, `Art 39(2)`, `Art 40(2)`, `Art 40(3)` the Minister's and the States' incidental powers | none | DEONTIC MAY |
| `Commencement: the unit of the Law is in force on` | `the unit of the Law`, `the day` (IP1), the interpretation | BOOLEAN, `@export` (IP4; F7.1, F7.3) |
| `Commencement: the stage in which the unit was brought into force` | `the unit of the Law` | `Stage of commencement` |
| `Commencement: the Article as now numbered for the original Article` | the original number | `MAYBE NUMBER` (T1, F7.3) |
| `Endnotes: the vintage of the text on` | `the day` | `Vintage of the text`: the constructor `before the first consolidated version` for a day before 2019-01-01 (so that a consumer can name the case; G1's `Art 1 the Minister under the text of` REFUSES on it), REFUSE for 2024-02-27 (IP2; F7.1), `@export` |
| `Endnotes: the vintage of the text at` | an instant (`DATETIME`) | `Vintage of the text` (F7.1) |
| `Endnotes: the day an instrument made on a day comes into force 7 days after` | the day made | `DATE` (F7.2) |
| `Endnotes: the amending instruments in force on` | `the day` | `LIST OF Amending instrument` |

Look at: T1, T2, T3, T13, T25, T26, T29, T30; every F7.x. The nine vintages are listed in domain.l4; encode the nine as data rows and test the resolver at both sides of each date (the day before, the day, and for 27 February 2024 the instants 08:00 and 10:00). Cross-group vintage tests (Minister, Comptroller, (ba), the Schedule 1 words) are the integrator's, because G7 may not import G1 or G9.
Tests from the source: the stage of each Part and Article on the days 2014-11-20, 2014-11-21, 2018-04-30, 2018-05-01, 2018-12-31, 2019-01-01; present Article 41 on 2018-01-01; "7 days after it is made" for the three Orders; each prohibition of Part 6, strict and with knowledge and intent, for each of a registered charity, a Jersey entity, a foreign entity, an excepted foreign charity; the 37(1) officer in an LLP and a body corporate and, per F7.6, not an unincorporated association.

### G8: Articles 26 to 36 (information and enforcement; the Charity Tribunal and appeals)

Source: Articles 26 to 36; about 2,330 words; coverage rows 104 (96 encoded, 6 inert, 2 out-of-scope).
Interpretation record: `Interpretation of Articles 26 to 36` (forks F8.1 to F8.8).

| module | holds |
| --- | --- |
| `g8-art26-demand` | the power to demand information, retention, the offences |
| `g8-art27-28-required-steps` | the grounds for a required steps notice, its content, the Order on procedure, organized religious charities and the invalidity |
| `g8-art29-31-information` | the restricted-information offence, its exceptions, required and permitted disclosure |
| `g8-art32-36-appeals` | the Tribunal's jurisdiction, who may appeal what, grounds and powers, appeal to the court, time limits and retrospective decisions |

Types needed from `domain.l4`: `Registered charity`, `Entity`, `Governor`, `Required steps notice`, `Belief that prompts a required steps notice`, `Recipient of a required steps notice`, `Decision of the Commissioner`, `Penalty provided`, `Legal actor`.
Group-local types: `Appellant` (applicant for registration, registered charity, person served, the Attorney General, any other person), `Appeal` (the appellant, the decision, the date of decision and of notice, the date lodged), `Requirement in a required steps notice`, `Act under Article 26 to 31`, `Act under Article 32 to 36`.

| export | takes | gives |
| --- | --- | --- |
| `Art 26(1) the Commissioner may require the person to provide information or attend` | `the person falls within Article 26(2)`, the Commissioner reasonably requires it to decide on a notice | DEONTIC MAY (T23) |
| `Art 26(2) the person falls within Article 26(2)` | the person's relation to a registered or formerly registered charity | BOOLEAN |
| `Art 26(5) the Commissioner may keep the document until` | the interpretation, the dates, the proceedings | `DATE` (F8.1) |
| `Art 26(6) the Commissioner must supply a copy of the retained document` | the interpretation | DEONTIC (F8.2) |
| `Art 26(7) the person must comply with the requirement` | the reasonable excuse | DEONTIC; penalty 3 months, level 3 |
| `Art 26(9) the statement may be used by the prosecution` | the proceedings | BOOLEAN |
| `Art 26(10) the person must not give false information` | none | DEONTIC SHANT; penalty 24 months and a fine |
| `Art 27(1) the Commissioner has a ground to serve a required steps notice` | `the conduct is misconduct within Article 2(10)` (IP12), `the entity meets the charity test` (IP8), `the governor has engaged in misconduct within Article 18(4)` (IP14), `the reportable matters` (IP21), `the requirement of Article 11(4)(c) is met` (IP15), `... (d) is met` (IP16) | `Belief that prompts a required steps notice`, a `LIST` |
| `Art 27(2) the Commissioner may serve a required steps notice` | the belief, the time specified, the steps | DEONTIC MAY (IP19) |
| `Art 27(4) the steps may include suspension, removal or replacement` | the belief, `the entity is an organized religious charity` (IP20) | BOOLEAN |
| `Art 27(5)`, `Art 28(1)` the Minister's Orders | none | DEONTIC MAY |
| `Art 28(2)(a) the Commissioner may grant or withdraw the status` | the Order gives the discretion | DEONTIC MAY |
| `Art 28(3) the required steps notice is invalid to the extent` | the notice, `the entity is an organized religious charity` (IP20) | BOOLEAN per requirement |
| `Art 28 the entity is an organized religious charity` | `the entity has a purpose within Article 6(1)(c)` (IP11), the Order's categorization | BOOLEAN (IP20; F8.3) |
| `Art 29(1) the person must not disclose the information` | `the information is registered in a public part of the register` (IP25), the exceptions of 29(2) and 31, consent | DEONTIC SHANT; penalty 24 months and a fine |
| `Art 30(1)`, `(2)` the Commissioner must disclose to the Comptroller and to the JFSC | the requirement | two DEONTIC rules |
| `Art 31 the disclosure is permitted` | the recipient, the purpose | BOOLEAN |
| `Art 33 the person may appeal the decision` | the appellant, `the decision of the Commissioner` (IP27), `the entity met the charity test at the time of the application` and `... meets ... at the time of the appeal` (IP9), the IP18 pair | BOOLEAN, `@export` (F8.4, T12) |
| `Art 34(1) the appeal has a ground`, `Art 34(2) the tribunal may make interim orders and consider evidence`, `Art 34(3) the tribunal may determine the appeal` | the appeal | BOOLEAN; DEONTIC MAY |
| `Art 35(1) the party may appeal to the court`, `Art 35(2)`, `Art 35(3) the tribunal may refer a point of law`, `Art 35(4)` | the appeal | BOOLEAN; DEONTIC MAY (F8.5) |
| `Art 36(1)`, `Art 36(2) the Minister may by Order set time limits` | none | DEONTIC MAY |
| `Art 36(2) the appeal is in time` | the interpretation, the dates, the limit (an input) | BOOLEAN; REFUSE when no limit is supplied (F8.6) |
| `Art 36(3)`, `Art 36(4)` a substituted decision takes effect from any date; acts before the order are not offences | the dates | `DATE`; BOOLEAN |

Look at: T11, T12, T23; every F8.x. The Order under 28 and the time limits under 36 are not in the sources: the Order's categorization is a `GIVEN` list. The decisions in 33 are the `Decision of the Commissioner` record of `domain.l4` (subject and outcome).
Tests from the source: each of the five 33(2) decisions by a registered charity and by a stranger; an applicant's two decisions; a general-section charity's refused restricted-section request (not appealable); the 33(5) appeal with the charity test failing at both times and at one; the Attorney General on any decision; the 35(1) ground; 28(3) partial invalidity: a notice that requires removal and also a report, only the first void.

### G9: Schedules 1 and 2 (the Commissioner; the Tribunal)

Source: Schedules 1 and 2; about 2,015 words; coverage rows 103 (83 encoded, 20 inert).
Interpretation record: `Interpretation of Schedules 1 and 2` (forks F9.1 to F9.13).

| module | holds |
| --- | --- |
| `g9-sched1-commissioner` | appointment, status, termination, staff, acting Commissioner, resources and reporting |
| `g9-sched2-tribunal` | appointment, termination, staff, the responsible officer, reporting, procedure |

Types needed from `domain.l4`: `Vintage of the text` (the two Dormant Bank Accounts additions), `Decision of the Commissioner`, `Legal actor`, `Penalty provided` (the cap of Sch 2 4(3)(f)).
Group-local types: `Appointment` (the person, the start date, the fixed end date, the dates of the notices), `Service` (periods of service, with a flag for service as a designated relevant person), `Report` (the calendar year, the dates given and laid), `Act under Schedule 1`, `Act under Schedule 2`.

| export | takes | gives |
| --- | --- | --- |
| `Sch 1 para 1(1) the Minister must appoint a suitable person` | the vacancy | DEONTIC |
| `Sch 1 para 1(2)` the views of the Jersey Appointments Commission; `Sch 1 para 1(3) the notice was presented in time` | the interpretation, the dates | DEONTIC; BOOLEAN (F9.1) |
| `Sch 1 para 1(5) the period of appointment is within the limit` | the interpretation, the dates | BOOLEAN (F9.2) |
| `Sch 1 para 1(6) the Minister may re-appoint` | none | DEONTIC MAY |
| `Sch 1 para 1(7) the Minister must take all reasonable steps to keep the office filled` | the office filled | DEONTIC |
| `Sch 1 para 2(4)(a) the remuneration is paid out of the annual income of the States` and `(b)` fees | the interpretation, `the vintage of the text` (IP2), `an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs the cost to the Fund` : BOOLEAN | BOOLEAN (T22, F9.9) |
| `Sch 1 para 3(1) the person ceases to be the Commissioner` | the interpretation, the three events | BOOLEAN (F9.3) |
| `Sch 1 para 3(2) the Minister may terminate the appointment` | the four grounds | DEONTIC MAY (F9.4) |
| `Sch 1 para 3(3) the Minister must present a notice of the termination` | the interpretation, the dates | DEONTIC (F9.5) |
| `Sch 1 para 3(4) the appointment expires` | the interpretation, the service | BOOLEAN (F9.6, F9.11) |
| `Sch 1 para 4(1)`, `4(6)` the Minister must make available staff, accommodation | none | two DEONTIC rules |
| `Sch 1 para 4(3) the Commissioner's function may be exercised by a member of staff` | `the decision of the Commissioner` (IP27), the interpretation | BOOLEAN (IP27; F9.8, T17) |
| `Sch 1 para 4(4) the Minister may designate a relevant person` | none | DEONTIC MAY |
| `Sch 1 para 4(5) someone is treated as the Commissioner` | the appointee's ability, the vacancy, the designation | BOOLEAN (IP28), `@export` |
| `Sch 1 para 4(7) the cost of staff, accommodation and equipment is met out of the annual income of the States` | as para 2(4)(a) | BOOLEAN |
| `Sch 1 para 4(8)`, `(9)`, `(10)` the report | the interpretation, the report | DEONTIC chain (F9.7, F9.10) |
| `Sch 1 para 4(11)`, `(12)` directions on the report | none | DEONTIC MAY; BOOLEAN limit |
| `Sch 2 para 1(1)` to `(8)` and `2(1)` to `(4)` | as Schedule 1 paragraphs 1 and 3 | the same shapes; membership of 4 to 8; chair and vice-chair (F9.1 to F9.6) |
| `Sch 2 para 3(1)` to `(5)` | as Schedule 1 paragraph 4 | the staff and the responsible officer's report (F9.7, F9.10) |
| `Sch 2 para 4(1)` the person presiding | which of chair, vice-chair, a member chosen | `STRING` or enumeration |
| `Sch 2 para 4(3)(f) the Regulations' penalty is within the cap` | a `Penalty provided` | BOOLEAN (24 months and a fine at most) |

Look at: T17, T20, T21, T22; every F9.x. The two Schedules are parallel but their figures differ: one record per Schedule, never a shared function with a parameter that hides the difference (T20). 3(1)(a), 3(2)(a), 2(1)(a) and 2(2)(a) are the places where the figures differ.
Tests from the source: each period at the boundary on both sides; the 12-year cut-off mid-term (T21); the DBAL words absent in the 2019-05-31 vintage and present in the 2019-12-16 vintage; the staff reservation for each of the three decisions and for another function; the acting Commissioner for each of (a) and (b); the report with a deadline of 30 April (F9.7).

## (c) Integration points

Every fact that one group decides and another consumes is one row, with ONE standard `GIVEN` name and ONE type.
Encoders use the names exactly as written here, with the backticks, so that the integrator can wire a consumer to its producer by name.
Two conventions make the table short.

- **Facts about the entity travel in two records of `domain.l4`.**
  `the entity` (type `Entity`) carries what Article 2 leaves: standing on the register, kinds of entity, Jersey-entity status, governors, purposes.
  `the registered charity` (type `Registered charity`) carries what the register holds about an entity that is or was registered.
  A fact that is a field of one of them is carried by that field; it is not a second `GIVEN`.
  The integrator sets the derived fields (kinds, Jersey entity, governors) from G1's exports and checks that every group that reads them was given the same record.
- **A discretion is an input named for what it decides**, never a computation: "satisfied", "in the opinion of", "believes", "considers", "reasonable excuse".
  Where a discretion is read by one group only it stays in that group's module and is not a row here.
  The rows below are the discretions and determinations that cross a group boundary.

`⇒ x` means "the integrator wires the producer's export to this `GIVEN` of the consumer".
Group-local names (an export of one group) are given with the `Art`/`Sch` prefix of PLAN section (b).

| id | what is shared | decided by | consumed by | carried by |
| --- | --- | --- | --- | --- |
| IP1 | the day on which the question is asked | the caller (input) | G1, G7, G9, the integrator | `the day` : DATE. Not a `TODAY`: every group takes the day as an argument (BRIEF "Vintages are inputs") |
| IP2 | which of the nine point-in-time texts (or none) is in force | G7, `Endnotes: the vintage of the text on` the day (REFUSES on 27 February 2024, where the text changes at 9.30 a.m.) and `Endnotes: the vintage of the text at` an instant | G1 (Minister, Comptroller, paragraph (ba)), G9 (the two Dormant Bank Accounts additions to Schedule 1), G2 (the Minister, for fork F2.3) | `the vintage of the text` : `Vintage of the text`. A vintage that does not decide a fact answers REFUSE, never a value borrowed from a neighbour |
| IP3 | which office "the Minister" names in the vintage | G1, `Art 1 the Minister under the text of` the vintage | G2 (5(2)(a), reading B of F2.3); any test that needs to say which office acts | `the office of the Minister` : `Office of the Minister`. Every MAY/MUST rule of the Minister is typed by the ROLE `the Minister` of `Legal actor`; the office is only the answer to "who is that on this day" |
| IP4 | whether a Part, an Article (present or original number) or a Schedule is in force on a day | G7, `Commencement: the unit of the Law is in force on` unit day (table in original numbers; renumbering map; stages 21 November 2014, 1 May 2018, 1 January 2019) | the integrator only, as a wrapper around each headline `@export` of G2 to G9; no group gates itself on commencement | `the unit of the Law` : `Unit of the Law`, `the day` : DATE, answer BOOLEAN. See section 10 |
| IP5 | the entity as Article 2 leaves it: `name`, `standing on the register`, `kinds of entity`, `is a Jersey entity`, `governors`, `purposes` | G1 derives `kinds of entity` (Art 2(1)), `is a Jersey entity` (Art 2(3)) and the members of `governors` (Art 2(7) to (9)) from raw facts that stay in G1; `standing` and `purposes` are inputs | G2 (purposes), G3, G4, G5, G6, G7, G8 | `the entity` : Entity |
| IP6 | whether the entity is a registered charity (general or restricted section, not the historic section) | G1, `Art 1 the entity is a registered charity` | G3, G4, G5, G6, G7, G8 (every rule that says "a registered charity") | `the entity is a registered charity` : BOOLEAN; it must equal the result of G1's export on `the entity` (integrator check) |
| IP7 | what the register holds about a registered or formerly registered entity: registration number, registered name(s), dates, the approved statements, organized-religious flag | G3 (Art 8(3), 8(5), 12(2)); `date deregistered` is set by G6 | G4, G5, G6, G7, G8 | `the registered charity` : `Registered charity`. Fields `registered charitable purposes` and `registered public benefit statement` are what 13(4)(a), 14(1)(b), 17(6) and 18(1)(a) refer to |
| IP8 | whether the entity meets the charity test | G2, `Art 5 the entity meets the charity test` | G4 (11(4)(a)), G6 (16(1)(a)), G8 (27(1)(b)) | `the entity meets the charity test` : BOOLEAN |
| IP9 | the same fact at two times, for the third-party appeal | G2 (the same export, evaluated twice) | G8 (33(5)(a): "at both the time of the application and the time of the appeal") | `the entity met the charity test at the time of the application` : BOOLEAN and `the entity meets the charity test at the time of the appeal` : BOOLEAN |
| IP10 | whether the entity meets the charity test only by virtue of an Order under Article 5(3) (and the constitution provision that 5(2) would have caught) | G2, `Art 5(3) the entity meets the charity test only by virtue of an Order` | G3 (8(3)(i)) | `the entity meets the charity test only by virtue of an Order under Article 5(3)` : BOOLEAN |
| IP11 | whether the entity has a purpose that falls within Article 6(1)(c) itself (not merely analogous under 6(2)(f)) | G2, `Art 6 the entity has a purpose within the advancement of religion` | G8 (28(1)(a), fork F8.3) | `the entity has a purpose within Article 6(1)(c)` : BOOLEAN |
| IP12 | whether conduct is "misconduct" under Article 2(10) | G1, `Art 2(10) the conduct is misconduct` | G5 (14(1)(a)), G6 (18(4)(a), 19(1)(a)), G8 (27(1)(a)) | `the conduct is misconduct within Article 2(10)` : BOOLEAN |
| IP13 | whether the charity or a governor has contravened a provision of this Law or of an enactment under it | no single group: every duty or prohibition of every group decides its own breach (the LEST arm of its regulative rule). The integrator maps a trace's BREACH to this fact | G1 (2(10)(a)(i)) | `the charity or governor has contravened a provision of this Law or an enactment under it` : BOOLEAN. Every prohibition without a penalty (12(7), 13(11)(a), 19(8)) routes its only consequence through this fact and then through "misconduct": 14(1)(a), 16, 27 |
| IP14 | whether a governor has engaged in misconduct under Article 18(4) | G6, `Art 18(4) the governor engages in misconduct` | G8 (27(1)(c)); G1 (the Article 1 pointer only) | `the governor has engaged in misconduct within Article 18(4)` : BOOLEAN |
| IP15 | whether the requirement of Article 11(4)(c) (Jersey entity or substantial Jersey activity) is met | G4, `Art 11(4)(c) the requirement is met` | G5 (13(6)(d)), G8 (27(1)(e)) | `the requirement of Article 11(4)(c) is met` : BOOLEAN |
| IP16 | whether the requirement of Article 11(4)(d) (principal address in Jersey) is met | G4, `Art 11(4)(d) the requirement is met` | G5 (13(6)(d)), G8 (27(1)(e)) | `the requirement of Article 11(4)(d) is met` : BOOLEAN |
| IP17 | whether the entity has a principal address in Jersey within Article 8(4) | G3, `Art 8(4) the entity has a principal address in Jersey` | G4 (11(4)(d)) | `the entity has a principal address in Jersey within Article 8(4)` : BOOLEAN |
| IP18 | whether a name is undesirable under Article 12(1) | G4, `Art 12(1) the name is undesirable` (the Commissioner's opinion is the input of that export) | G4 (11(4)(e), 12(4)), G5 (13(6)(b)), G8 (33(5)(b), at the two times as in IP9) | `the name is undesirable under Article 12(1)` : BOOLEAN; for 33(5)(b) the two forms `... at the time of the application` and `... at the time of the appeal` |
| IP19 | the required steps notices served on the charity or on its governors | G8, `Art 27(2) the Commissioner may serve a required steps notice` (each service is a record) | G1 (2(10)(a)(iii)), G3 (8(3)(k)), G6 (16(1)(c), 19(1)(a)) | `the required steps notices served` : LIST OF `Required steps notice`. The date of service is fixed by Art 38 (IP34) |
| IP20 | whether the charity is an organized religious charity | G8 (Art 28: the Order's categorization, the Commissioner's grant or withdrawal) | G3 (8(3)(h)), G6 (19(9)(e)(i)), G8 (28(3)) | field `is an organized religious charity` of `the registered charity` (IP7) |
| IP21 | the kinds of reportable matter that describe a person | G6, `Art 19(1) the reportable matters of the person` | G5 (13(6)(e)), G8 (27(1)(d)), G4 (through 19(9)(c)) | field `reportable matters` of each `Governor` in `the entity`'s `governors` |
| IP22 | whether the applicant has complied with Article 19(5) (and so whether the application is complete under 19(6)) | G6, `Art 19(5) the applicant has stated that it holds declarations from all its governors who have not reported` | G4 (11(4), the chapeau) | `the applicant has complied with Article 19(5)` : BOOLEAN |
| IP23 | whether Article 19(9)(c) bars granting an application (a reported fitness issue is undetermined, or its resulting order or notice is not complied with) | G6, `Art 19(9)(c) the Commissioner must not grant the application` | G4 (11(4); trap T10, fork F4.4) | `Article 19(9)(c) bars granting the application` : BOOLEAN |
| IP24 | whether the court has ordered that the entity must not be registered | G6, `Art 20(1)(c) the court orders that the entity must not be registered` | G4 (11(4); trap T10, fork F4.4) | `the court has ordered that the entity must not be registered as a charity` : BOOLEAN |
| IP25 | whether information is in a public part of the register (the general section, the public elements of the restricted section, the historic section, less what the Commissioner has designated non-public) | G3, `Art 10(3) the matter is in a public part of the register` | G8 (29(2)(a)) | `the information is registered in a public part of the register` : BOOLEAN |
| IP26 | whether the entity is an excepted foreign charity | G7, `Art 22 the entity is an excepted foreign charity` | G1 (2(10)(b)), G7 (21(5), 21(6)) | `the entity is an excepted foreign charity` : BOOLEAN |
| IP27 | the Commissioner's decisions that other provisions name: the subject (which Article) and the outcome | the deciding groups G3 (9(6)-(7)), G4 (11, 12), G5 (13), G6 (15, 16), G8 (26, 27) | G8 (Article 33: which are appealable and by whom), G9 (Sch 1 4(3): which are reserved from staff) | `the decision of the Commissioner` : `Decision of the Commissioner` (subject and outcome, `domain.l4`) |
| IP28 | whether someone is acting as the Commissioner (the person appointed, or a designated relevant person while the appointee is unable to act or the office is vacant) | G9, `Sch 1 para 4(5) someone is treated as the Commissioner` | every group whose rule has the Commissioner as PARTY; the integrator | `someone is acting as the Commissioner` : BOOLEAN. The role is the constructor `the Commissioner` of `Legal actor`; the Commissioner's function may be exercised by staff except the reserved decisions (IP27) |
| IP29 | whether an Order under Article 13(9) (payment details, statement of intentions) applies to the registered charity | G5 (the Order is an input; Art 13(9) is the power) | G3 (8(3)(m)), G4 (11(2)(e)(ii)) | `an Order under Article 13(9) applies to the registered charity` : BOOLEAN |
| IP30 | the penalty an offence carries (term in months, fine) | each offence's owner: G6 (19(11), 20(6)), G7 (21(9), 21(10), 23(6), 23(7)), G8 (26(7), 26(10), 29(1)) | G7 (37(1): "the penalty provided for that offence"), Sch 2 4(3)(f) (a cap) | `the penalty provided for the offence` : `Penalty provided`. The amount of level 3 is not in the sources |
| IP31 | the kinds of order the court may make over a charity (Article 14(3)), which Article 17(9) lends to a deregistered entity | G5, `Art 14(3) the court may make the order` | G6 (17(9)) | type `Order of the court over a charity` (`domain.l4`); G6 types the action of 17(9) with it |
| IP32 | why an entity was deregistered | G6 (Articles 15, 16) | G3 (8(5)(c)), G8 (33(2)(a): the appeal lies against a deregistration, not a refusal to deregister) | `the basis of deregistration` : `Basis of deregistration` |
| IP33 | the meaning of "year" for the annual return | G5 (fork F5.2) and G3 (fork F3.2), which must take the same reading | G3 (8(3)(j)), G5 (13(7), 13(9)(a)) | each group's `Interpretation` record has a field typed `Meaning of the year of an annual return`; the integrator sets both from one value |
| IP34 | how the date on which a notice was served is fixed | G7, `Art 38 the date on which the notice is served` (fork F7.7) | G3 (8(3)(k)), G6 (17(4)), G8 (26, 27, 33(3)) | field `date served` of `Required steps notice`; for a notice under Article 26 or 16(1), `the date on which the notice was served` : DATE |
| IP35 | the unit in which a term of imprisonment is measured (calendar months or days) | each owning group's fork: G6 (F6.16), G7 (F7.8), G8 (F8.8), G9 (F9.13), which must take the same reading | the offence rules of those groups; G7 (37(1) carries the penalty to an officer); G9 (the cap in Sch 2 4(3)(f)) | each group's `Interpretation` record has a field typed `Unit of a term of imprisonment`; the integrator sets all four from one value |

Rows that look like candidates for this table but are not:

- **The charity test inside Article 5(2).** The constitution provision that bars the test is G2's own input; only its outcome (IP8, IP10) crosses.
- **"Prescribed" content of Orders and Regulations.** Each is an input in the group whose Article confers the power (section 10 lists them); only IP29, IP20 and IP26 are read by another group.
- **The Commissioner's staff.** The reservation in Schedule 1 paragraph 4(3) is IP27/IP28; the groups do not model delegation.

## (d) Periods register

Every period, term, limit and time-bound in the Law and in the three commencement-bearing instruments.
`kind` names what sort of time-bound it is: a deadline, a retention period, a term of office, a minimum notice, a backward-looking period, a look-back, a sentence, a commencement, or a standard of promptness (a time bound the Law states without a number); a few rows have their own kind (a cap on service, a duration threshold, the start of a prohibition).
Each row names the fork (section (g)) that carries its counting question.
The `daydate` library's `add months` and `add years` clamp to the last day of the target month; the fork readings below use that as the clamped reading and `Date`'s roll-forward as the rolled one.
Days of rest and holidays are not mentioned by the Law and are not modelled.

| id | provision | the words | kind | the counting question | owner | fork |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 5(7) | "Within a reasonable time after issuing or amending guidance" | standard of promptness | no number; start = the day the guidance is issued or amended; the standard of reasonableness is an input | G2 | F2.4 |
| P2 | 5(8) | "as soon as practicable after the Minister receives the guidance and report" | standard of promptness | no number; start = receipt by the Minister | G2 | F2.4 |
| P3 | 8(3)(j) | "whether the registered charity has or has not sent its annual return for the most recent year" | look-back | which year is "the most recent": the calendar year just ended, the charity's financial year, or the year from the anniversary of registration | G3 | F3.2 (with F5.2; IP33) |
| P4 | 8(6) | "retain for 10 years, in respect of each registered charity, a copy of" four kinds of document | retention period | start unstated: receipt of each copy, deregistration, or a rolling look-back; whether the last day of the tenth year is inside | G3 | F3.1 |
| P5 | 11(2)(e)(ii) | "any payment made to any governor of the entity in the 12 months preceding the application" | backward-looking period | is the day of the application inside; does the period start on the anniversary day or the day after; a 12-month window ending on 29 February | G4 | F4.1 |
| P6 | 11(2)(e)(ii), 11(8)(a)(i) | "the application" as the anchor of P5 and of the decision period an Order may set | commencement of a period | the date the application is made, or the date it is complete under 19(6) | G4 | F4.2 |
| P7 | 11(8)(a)(i) | "the period within which the Commissioner must make a decision on an application" (by Order; no Order in the sources) | deadline | the length is an input; inclusive of the last day; anchor per P6; a "late" decision is a named refusal until the Order is supplied | G4 | F4.2 |
| P8 | 13(6) | "must promptly report" (eight kinds of matter) | standard of promptness | no number; start = the event or the charity's awareness of it; for 13(6)(c) and (d) the matter is a proposal, so the report precedes the event | G5 | F5.1 |
| P9 | 13(7), 13(9)(a) | "the year to which the return relates" | reporting period | calendar year, financial year, or anniversary year; Schedule 1 paragraph 4(8) says "calendar year" when it means one | G5 | F5.2 (IP33) |
| P10 | 13(8) | "the format and timing of the annual return, the consequences of lateness" (by Order; none in the sources) | deadline | the due date is an input; is a return sent on the due date timely | G5 | F5.5 |
| P11 | 16(1) | "inviting objections within a reasonable time specified in the notice" | deadline (set by the Commissioner) | the time is in the notice (an input); whether an unreasonably short time invalidates the deregistration | G6 | F6.13 |
| P12 | 17(1)(a) | "must retain the information registered in respect of that entity for 10 years" after deregistering | retention period | start = the date of the deregistration notice or the effective (possibly retrospective) date; inclusive of the last day | G6 | F6.5 |
| P13 | 17(1)(b) | "must not assign the registered number of that entity to any other registered charity" | no period stated | whether the bar is permanent or lasts only for the 10 years of 17(1)(a) | G6 | F6.6 |
| P14 | 17(2) to (5) | "since a past date"; "acquired before it was deregistered" | backward effect | which notice fixes the date (16(1) has two); which date is "deregistered" for property acquired between the past date and the notice | G6 | F6.3, F6.4 |
| P15 | 18(4)(d)(ii) | "fails within a reasonable time to take proper steps" | standard of promptness | no number; whether "within a reasonable time" also qualifies "actively conceals" | G6 | F6.8 |
| P16 | 19(1)(c), (d) | "has been disqualified" | look-back | no limit stated (contrast "whether or not spent" in (f) and "unspent" in (g)): does an expired disqualification count | G6 | F6.9 |
| P17 | 19(2) | "must report any reportable matter promptly" | standard of promptness | no number; start = the matter arising or the governor's awareness | G6 | F6.12 |
| P18 | 19(10) | "at any time after reporting a reportable matter" | start of a prohibition | to whom the report must be made for the ban to start (the charity, the Commissioner, or both) | G6 | F6.10 |
| P19 | 19(11) | "imprisonment for one year" | sentence | a maximum term; stored as 12 months; one year as 12 calendar months or 365 days | G6 | F6.16 |
| P20 | 20(5) | "for such period, not exceeding 15 years, as the court directs" | maximum term of a disqualification | start = the date of the order; end = start + 15 years, clamped or rolled on 29 February; inclusive of the last day | G6 | F6.14 |
| P21 | 20(6) | "imprisonment for 2 years" | sentence | as P19; 24 months | G6 | F6.16 |
| P22 | 21(9), 23(7) | "imprisonment for a term of 2 years" | sentence | as P19 | G7 | F7.8 |
| P23 | 26(5) | "whichever is the longer of (a) a period of one year; and (b) if within that period proceedings ... are commenced ..., until the conclusion of those proceedings" | retention period | start unstated: the date the document is provided or retained, or the date of the notice; one year from 29 February; whether proceedings begun on the last day extend it | G8 | F8.1 |
| P24 | 26(6) | "must be supplied with a copy as soon as practicable" | standard of promptness | no number; start = the request | G8 | F8.2 |
| P25 | 26(7) | "imprisonment for a term of 3 months" | sentence | as P19; 3 months | G8 | F8.8 |
| P26 | 26(10), 29(1) | "imprisonment for a term of 2 years" | sentence | as P19 | G8 | F8.8 |
| P27 | 36(2)(a) | "time limits within which appeals to the tribunal or court are to be brought" (by Order; none in the sources) | deadline | the limit is an input; runs from the decision or from the notice of the decision (36(2)(b)); inclusive of the last day | G8 | F8.6 |
| P28 | 27(2), 26(1) | "in a time specified in the notice"; "at such time and place as may be specified" | deadline (set by the Commissioner) | the time is in the notice (an input); no counting convention is the Law's to fix | G8 | F8.7 |
| P29 | Sch 1 1(3) | "at least 2 weeks before appointing a person as the Commissioner, present to the States a notice" | minimum notice | 14 days; are the day of the notice and the day of the appointment both counted | G9 | F9.1 |
| P30 | Sch 1 1(5) | "the period of the appointment, being not more than 6 years" | term of office | start + 6 years, clamped, and whether the last day is the day before the anniversary | G9 | F9.2 |
| P31 | Sch 1 3(1)(a) | "resigns ... by giving not less than 3 months' notice in writing to the Minister" | minimum notice | month arithmetic from a notice given on the 30th or 31st; whether the office ends when the notice is given or when it runs out | G9 | F9.3 |
| P32 | Sch 1 3(2)(a) | "absent from his or her duties for a period longer than 4 consecutive weeks" | duration threshold | 28 days; "longer than" is strict; whether the first and last days of absence are counted | G9 | F9.4 |
| P33 | Sch 1 3(3) | "not more than 2 weeks after terminating the appointment, present to the States a notice" | deadline | 14 days after the termination; is the 14th day timely | G9 | F9.5 |
| P34 | Sch 1 3(4)(c) | "completes 12 years (whether consecutive or in aggregate) of service as Commissioner" | cap on service | aggregation of gaps by years, months and days; whether service as a designated relevant person counts; the cut-off falls mid-term | G9 | F9.6 |
| P35 | Sch 1 4(8) | "a report ... in each calendar year" | reporting period | "calendar year" is stated (contrast Article 13(7)); no fork | G9 | F9.12 (and T24) |
| P36 | Sch 1 4(9) | "as soon as practicable after the end of the year ..., but in no case later than 4 months after the end of that year" | deadline | 31 December plus 4 months: 30 April (clamped) or 1 May (rolled); is the last day timely | G9 | F9.7 (and F9.10 for "as soon as practicable") |
| P37 | Sch 1 4(10) | "as soon as practicable after the Minister receives the report" | standard of promptness | no number | G9 | F9.10 |
| P38 | Sch 2 1(3) | "at least 2 weeks before appointing a person as a tribunal member" | minimum notice | as P29 | G9 | F9.1 |
| P39 | Sch 2 1(5) | "not more than 6 years" | term of office | as P30 | G9 | F9.2 |
| P40 | Sch 2 2(1)(a) | "not less than one month's notice in writing to the Minister" | minimum notice | as P31, with one month | G9 | F9.3 |
| P41 | Sch 2 2(2)(a) | "longer than 8 consecutive weeks" | duration threshold | as P32, 56 days | G9 | F9.4 |
| P42 | Sch 2 2(3) | "not more than 2 weeks after terminating" | deadline | as P33 | G9 | F9.5 |
| P43 | Sch 2 2(4)(c) | "completes 12 years (whether consecutive or in aggregate) of service as a member of the tribunal" | cap on service | as P34 | G9 | F9.6 |
| P44 | Sch 2 3(3) to (5) | "a report ... in each calendar year"; "in no case later than 4 months after the end of that year"; "as soon as practicable" | reporting period; deadline; standard of promptness | as P35, P36, P37; the duty is the responsible officer's | G9 | F9.7, F9.10 |
| P45 | Sch 2 4(3)(f) | "carrying a penalty not exceeding imprisonment for a term of 2 years and a fine" | sentence (a cap on Regulations) | as P19 | G9 | F9.13 |
| P46 | endnote E1 | "in force 21 November 2014" (stage 1), "1 May 2018" (stage 2, R&O.17/2018 Article 1), "1 January 2019" (stage 3, Article 2) | commencement | the named day is the first day in force; the table speaks in original Article numbers | G7 | F7.1, F7.3 |
| P47 | endnotes E4 to E11 | R&O.40/2019 "31 May 2019"; L.1/2017 "16 December 2019"; L.13/2019 "1 January 2020 (R&O.136/2019)"; R&O.29/2021 "2 March 2021"; R&O.28/2023 "12 April 2023"; R&O.10/2024 "9.30 a.m. on 27 February 2024"; R&O.56/2025 "16 October 2025"; R&O.102/2026 "2 October 2026" | commencement (nine texts) | day against instant: only R&O.10/2024 has a time of day | G7 | F7.1 |
| P48 | R&O.28/2023 Article 3; R&O.56/2025 Article 2; R&O.102/2026 Article 7(6) | "comes into force 7 days after it is made" (made 5 April, 9 October 2025, 25 September 2026) | commencement | the day of making excluded; the seventh day after is the first day in force. The three instruments settle it: 5 April + 7 = 12 April; 9 October + 7 = 16 October; 25 September + 7 = 2 October | G7 | F7.2 |

Time-bounds in the Law that are NOT periods and so have no row: "before the application is made" (19(3)), "when notified by the charity that it is preparing its annual return" (19(4)), "at both the time of the application and the time of the appeal" (33(5)), "before it ceased to meet that condition" (13(5)(b)), "for a specified or indefinite period" (14(3)(a), (b): the content of a court order), "any condition or time limit" (19(9)(e)(ii), 20(2)(b): the content of a permission or order), "has been disqualified" with no limit (P16), "whether or not spent" and "unspent" (19(1)(f), (g): the rehabilitation of offenders rules are another Law and an input).

## (e) Terminology

Four tables: the defined terms of Articles 1 and 2; the terms defined in place; the terms from other statutes and from Jersey French and customary law, which are inputs; and the operative words the Law uses without defining them.
"Rule" below means an export named in section (b); "input" means a `GIVEN` fact the caller supplies; "pointer" means the Article 1 definition only names the Article that defines the term (coverage row: inert).
The lead-in of Article 1 and of Article 2 is "unless the context otherwise requires": each encoder records, as a comment at the definition, every place where the context displaces it (the one found is `a Minister`, 5(2)(a), F2.3).

### Defined terms, Articles 1 and 2

| term | where | meaning (short) | what the encoding does |
| --- | --- | --- | --- |
| annual return | 1; 13(7) | a return sent under 13(7) | pointer; the duty is G5's; "year": F5.2 |
| charitable purpose | 1; 6(1) | the purposes in Article 6 | pointer; `Head of charitable purpose` in `domain.l4`; G2 rules |
| Commissioner | 1; 3; Sch 1 | the person for the time being appointed to the office | role: `Legal actor` constructor `the Commissioner`; who acts is IP28 (G9) |
| company | 1 | a company under the Companies (Jersey) Law 1991 | other statute; an input fact in the raw facts of 2(1)(f) |
| Comptroller | 1 | as in the Revenue Administration (Jersey) Law 2019; before 1 January 2020, the Income Tax (Jersey) Law 1961 | rule `Art 1 the Law that defines the Comptroller under the text of` the vintage (inferred from L.13/2019 Schedule 3); role constructor `the Comptroller` |
| constitution | 1; 2(4) | the document that establishes the entity, by kind | rule `Art 2(4)`; the document itself is an input |
| constitutional Law | 1; 2(5) | the governing Law, by kind of entity; none stated for (ba), (g), (h), (i), (j) | rule `Art 2(5)` answers MAYBE; trap T6; fork F1.3 |
| court | 1 | the Royal Court | role: `the court` |
| court-approved fidéicommis | 1 | a fidéicommis created under Article 3 of the Loi of 1862 or extended under its Article 17 | other statute; an input in the raw facts of 2(1)(b) |
| donation | 1; 9(3)(b)(ii) | as the Order under 9(3)(b)(ii) construes it | pointer; the Order's content is an input to G3 |
| entity | 1; 2(1) | any of the kinds in 2(1)(a) to (j), including (ba) from 16 October 2025 | rule `Art 2(1) the kinds of entity the body falls within`; `Kind of entity` in `domain.l4` |
| foundation | 1 | a foundation under the Foundations (Jersey) Law 2009; charter, regulations, council member | other statute; an input fact |
| general section | 1; 8(2) | the section distinguished from the restricted and historic sections | `Standing on the register` constructor; pointer |
| governor | 1; 2(7) to (9) | trustee or fidéicommissaire; council member; director; management-committee member of a relevant unincorporated entity; or a person with general control and management under the constitution | rule `Art 2(7)`; record `Governor` in `domain.l4`; a corporate trustee is a governor (F1.4) |
| incorporated 1862 association | 1 | an association incorporated under Article 4 of the Loi of 1862 | other statute; an input fact |
| JFSC | 1 | the Jersey Financial Services Commission under the Financial Services Commission (Jersey) Law 1998 | other statute; role constructor |
| Jersey entity | 1; 2(3) | an entity in 2(1)(a) to (h), or an unincorporated body governed by Jersey law with a governor resident in Jersey or itself a Jersey entity by (a) | rule `Art 2(3)`; field of `Entity`; F1.1 on whether "(a) to (h)" reaches (ba) |
| Loi of 1862 | 1 | the Loi (1862) sur les teneures en fidéicommis et l'incorporation d'associations | other statute and Jersey French; named only |
| Minister | 1 | the Chief Minister (text of 2 October 2026) | rule `Art 1 the Minister under the text of` the vintage; five texts; trap T3; role constructor `the Minister` |
| misconduct | 1; 2(10); 18(4) | contravention by a registered charity or governor; or an offence by any person in relation to a charity; a governor's misconduct per 18(4) | rule `Art 2(10)` (G1) and `Art 18(4)` (G6); IP12, IP13, IP14 |
| prescribed, specified | 1 | prescribed or specified in an Order or Regulations as the case may be | the content of an Order or Regulations is an input (BRIEF); coverage row inert |
| property | 1 | as in the Trusts (Jersey) Law 1984 | other statute; an input noun |
| publish | 1 | publish in a manner that, in the opinion of the person publishing, is likely to bring the information to the attention of the public or those affected | rule `Art 1 the information has been published` on the publisher's opinion (input); F1.5 |
| purpose | 1; 2(6) | by kind of entity | rule `Art 2(6)`; record `Purpose` |
| register | 1; 8 | the register kept under Article 8; as a verb, to enter an entity on it | pointer; `Standing on the register` |
| registered charitable purposes | 1; 8(3)(e) | the statement of purposes approved by the Commissioner | field of `Registered charity` |
| registered charity | 1 | an entity entered for the time being in the general or the restricted section | rule `Art 1 the entity is a registered charity` (IP6); the historic section is excluded (T7, T16) |
| registered public benefit statement | 1; 8(3)(f) | the statement of public benefit approved by the Commissioner | field of `Registered charity` |
| regulated financial services business | 1 | business for which a person is registered or authorized under four financial-services Laws | coverage row inert; only 11(7)(a) and 14(3)(e) use it and both are input content |
| reportable matter | 1; 19(1) | the eight descriptions of a person | `Kind of reportable matter`; rule `Art 19(1)`; IP21 |
| required steps notice | 1; 27 | a notice served under Article 27 | record `Required steps notice`; IP19 |
| restricted section | 1; 8(2) | the section distinguished from the general and historic sections | `Standing on the register` constructor; pointer |
| solicit | 1; 9(3)(b)(i) | as the Order under 9(3)(b)(i) construes it | pointer; an input to G3 |
| tribunal | 1; 32 | the Charity Tribunal | role: `the Charity Tribunal` |
| trust | 1 | a trust over which the court has jurisdiction under Article 5 of the Trusts (Jersey) Law 1984 | other statute; an input in the raw facts of 2(1)(a) |
| relevant unincorporated entity | 2(8) | an unincorporated body in 2(1)(i) whose constitution conforms to a model the Commissioner has published providing for a management committee | rule `Art 2(8)`; "conforms" is an input |
| NPO | 2(1)(ba)(i) | as defined by the Non-Profit Organizations (Jersey) Law 2008 | other statute; an input fact |
| body incorporated by (but not under) another Law | 2(5)(e) | the (e) kind | `Art 2(5)`; the matching gap for "under, but not by" (g), (h) is T6 |

### Terms defined in place

| term | where | meaning (short) | what the encoding does |
| --- | --- | --- | --- |
| the applicant | 11(1) | the entity that applies to be registered | actor constructor `an applicant for registration`; standing `an applicant for registration` |
| charity test | 5(1) | all purposes charitable or ancillary and public benefit to a reasonable degree, subject to 5(2) | rule `Art 5 the entity meets the charity test` (IP8) |
| the advancement of health | 6(2)(a) | includes the prevention or relief of sickness, disease or human suffering | G2 rule on the head (d) |
| sport | 6(2)(c) | sport that involves physical skill and exertion | G2 rule on the head (h) |
| principal address | 8(4) | registered office or business address in Jersey; else main premises in Jersey (not a private dwelling house); else a governor's address in Jersey | rule `Art 8(4)`; IP17 |
| public elements of the restricted section | 9(1) | the number (not the name), five 8(3) matters, a summary of reasons, anything prescribed | rule `Art 9(1)`; IP25 |
| funding condition | 9(2)(a) | the condition prescribed by Order about refraining from soliciting donations | an input |
| public parts of the register | 10(3) | the general section, the public elements of the restricted section, the historic section, subject to (5) | rule `Art 10(3)`; IP25 |
| historic section | 8(2)(c), 8(5), 10(3)(c) | not defined in Article 1 (T7): the section for formerly registered charities | `Standing on the register` constructor; defined by 8(5) |
| registered name; the registration number | 12(2) | the name and number entered when the Commissioner registers the entity | fields of `Registered charity` |
| alternative registered name | 12(3), 12(5) | a further name entered with permission | field `alternative registered names` |
| certificate of registration | 11(9)(a) | the Commissioner's certificate of name, number and date | G4 duty; no record needed |
| deregister | 15(1) | to terminate the registration | `Standing on the register` change; `date deregistered` |
| remaining property | 17(5) | property of the charity acquired before it was deregistered | an input list in G6; F6.4 on "before it was deregistered" |
| preserved charitable purposes; preserved public benefit statement | 17(6) | the registered purposes and statement immediately before deregistration | derived from `Registered charity` in G6 |
| disqualification order | 20(3) | an order that a person not, without leave, be a governor or concerned in the management of a registered charity | G6 record; field `reportable matters` includes it (19(1)(b)) |
| excepted foreign charity | 22(1) | a foreign entity meeting both conditions of 22 | rule `Art 22 the entity is an excepted foreign charity` (IP26) |
| relevant terms | 24(2) | "charitable", "public benefit" and related terms specified in Regulations | an input list in G7 |
| relevant persons | 27(3) | the registered charity and its governors | `Recipient of a required steps notice` |
| organized religious charity | 28(1) | a charity the Order categorizes as one | field of `Registered charity` (IP20) |
| relevant enactment | 41(1) | three kinds of enactment | out of scope (Article 41 is an enabling power over other enactments) |
| relevant person (Schedule 1) | Sch 1 4(4) | the person the Minister designates to act as the Commissioner | rule `Sch 1 para 4(5)`; IP28 |
| responsible officer | Sch 2 3(2) | the member of staff who assists the tribunal's administration | G9 role record |
| chair; vice-chair | Sch 2 1(7) | the members the Minister designates | G9 |

### Other statutes, Jersey French, customary law and other jurisdictions: all inputs

| term | where | what the encoding does |
| --- | --- | --- |
| fidéicommis; fidéicommissaire(s) | 1, 2(1)(b), 2(4)(b), 2(6)(b), 2(7)(a) | Jersey French (a form of trust-like arrangement under the Loi of 1862); the facts that a body is one, and who its fidéicommissaires are, are inputs; the term is kept in the constructor names of `domain.l4` |
| Loi (1862) sur les teneures en fidéicommis et l'incorporation d'associations | 1, 2(4)(b)-(c), 2(5)(b), 2(6)(b), 13(13) | text not in the sources; inputs |
| Act of the court incorporating an association; minute of the contract annexed to the application | 2(4)(b), (c) | documents; an input that the constitution is made up of them |
| Royal Court; Bailiff; Attorney General | 1, 14, 17, 31, 40 | roles; `Legal actor` constructors |
| customary law | 14(5)(a), 29, 31(e), 40(1) | the independent powers of the court preserved by 14(5)(a) and 40(1); an input; no rule |
| States; States Assembly; Act of the States; Royal Charter; Order in Council | 2(1)(e), (h), 5(2)(b) | inputs for the kind of body; the States as maker of Regulations is `Legal actor` `the States` |
| Trusts (Jersey) Law 1984; Companies (Jersey) Law 1991; Foundations (Jersey) Law 2009; Non-Profit Organizations (Jersey) Law 2008 | 1, 2 | out of scope; the status of a body under them is an input fact |
| Banking Business (Jersey) Law 1991 and the other financial-services Laws and Regulations named in 1 and 2(10)(b)(ii); Income Tax (Jersey) Law 1961, Goods and Services Tax (Jersey) Law 2007, Taxation (Land Transactions) (Jersey) Law 2009 | 1, 2(10)(b) | out of scope; whether an offence is under one of them is an input |
| Charities and Trustee Investment (Scotland) Act 2005; Charities Act 2011 section 10(2) | 28(2)(b) | out of scope; an input to the content of an Order |
| Employment of States of Jersey Employees (Jersey) Law 2005, Jersey Appointments Commission | Sch 1 1(2), Sch 2 1(2) | out of scope; the views being sought is an input fact |
| Dormant Bank Accounts (Jersey) Law 2017, Article 20(1) | Sch 1 2(4)(a), 4(7) | out of scope; an Order under it is an input (T22) |
| Revenue Administration (Jersey) Law 2019; Income Tax (Jersey) Law 1961 (Comptroller) | 1 | out of scope; which Law defines "Comptroller" in which text is encoded |
| Proceeds of Crime (Supervisory Bodies) (Jersey) Law 2008 | 41(1)(a) | out of scope |
| standard scale of fines, level 3 | 21(10), 23(6), 26(7) | the amount is not in the sources; data `a fine of a level on the standard scale` with level 3 |
| spent conviction | 19(1)(f), (g) | the rehabilitation of offenders rules are another Law; an input per conviction |
| natural person; resident in Jersey; partnership; limited liability partnership; separate limited partnership; body corporate; bankrupt or otherwise insolvent; lien; legal professional privilege | 2(1)(i), 2(3), 19(1)(e), 26(3), 26(8), 37 | ordinary legal terms or terms of other Laws; inputs |
| equivalent offices or entities in another jurisdiction | 5(2)(c), 19(1)(c), (d), 2(10)(b) | inputs; no list of jurisdictions in the Law except by Order (22(2)(a)(ii)) |

### Operative words the Law uses without defining

| word | where | what the encoding does |
| --- | --- | --- |
| promptly; a reasonable time; as soon as practicable; within a reasonable time | 5(7), 5(8), 13(6), 16(1), 18(4)(d), 19(2), 26(6), Sch 1 4(9), (10), Sch 2 3(4), (5) | standard of promptness; an input Boolean by default, and a fork for the anchor (section (d)) |
| year; the most recent year; the year to which the return relates | 8(3)(j), 13(7), 13(9)(a) | `Meaning of the year of an annual return` (F3.2, F5.2); calendar year taken |
| substantial (activity) | 11(4)(c)(ii), 11(6) | the Commissioner's opinion, with published guidance: an input |
| satisfied; in the opinion of; believes; considers; appears to the Commissioner, the Minister or the court | passim | the discretion is an input named for what it decides (BRIEF "Rules that matter") |
| fit and proper person | 19(9)(a), 19(13) | the Commissioner's or the court's determination: an input |
| reasonable excuse | 19(11), 26(7) | an input Boolean |
| reasonable degree (of public benefit); unduly restrictive; section of the public | 5(1)(b), 7(2)(b), 7(3)(b) | determinations: inputs, recorded; 7(3)(b) is a rule that identified persons are not a section |
| too similar; likely to mislead; offensive; connected | 12(1) | the Commissioner's opinion: input |
| significantly put at risk | 10(4) | the Commissioner's consideration: input |
| proportionate | 16(1) | the Commissioner's satisfaction: input |
| expressly permits | 5(2) | a fact about the constitution's text: an input Boolean |
| analogous; ancillary or incidental | 5(1)(a)(ii), 6(1)(p) | determinations: inputs recorded in `Purpose` |
| acting in that capacity | 5(2) | F2.2 |
| in relation to (a charity) | 2(10)(b) | F1.2 |
| written document | 11(4)(b) | an input Boolean about the constitution |
| unfit | 20(4), 27(1)(d) | the court's or Commissioner's determination: an input |
| expedient in the public interest | 20(3) | the Commissioner's or Attorney General's view: an input |

## (f) First-read contradictions and traps

Each trap names the provisions, the groups affected, a discriminating case (a set of facts on which the readings give different answers) and a suggested handling.
A trap that is also an ambiguity points at its fork in section (g); a trap that is only a gap or an inconsistency has no fork and is handled as stated.
Quotations are the output of `srcrefs.py quote` on the consolidated text (`src:N` is line N of that file).

### T1: the commencement table speaks in the original Article numbers

- **Provisions:** endnotes E1 to E3 and R1 to R6 (the Table of Legislation History and the Table of Renumbered Provisions); Articles 41, 42, 43; R&O.17/2018 Articles 1 and 2.
- **Groups affected:** G7 (owner), and the integrator's in-force wrappers.
- **The trap:** stage 1 reads `-- src:876 | Parts 1 to 3, Articles 32, 38, 39, 40, 42, 43 and 44 and` / `-- src:877 | the Schedules, in force 21 November 2014;`. The Law now ends at Article 43. The Table of Renumbered Provisions (`src:917` to `src:928`) says original 41 is "spent, omitted", original 42 is now 41, 43 is now 42, 44(1) is now 43, and 44(2) and 44(3) are "spent, omitted".
  Read in the present numbering, "42, 43 and 44" names present Articles 42 and 43 and a non-existent Article 44, and does not name present Article 41, which would then fall to the stage 3 "remainder".
- **Discriminating case:** is present Article 41 (sharing of information) in force on 1 January 2018? Present-numbering reading: no (remainder, 1 January 2019). Original-numbering reading: yes (it was original 42, named in stage 1, in force from 21 November 2014).
- **Suggested handling:** encode the table in ORIGINAL numbers, with the renumbering map as data; `Commencement: the unit of the Law is in force on` accepts `an Article of the Law as now numbered` and `an Article of the Law as originally numbered` and converts. Fork F7.3 carries the other reading as a callable. Tests: present 41 on 2018-01-01 TRUE; original 41 on 2018-01-01 FALSE and on 2019-01-01 TRUE; "an Article 44 as now numbered" REFUSES (there is none).

### T2: the "remainder" is Part 6 and the original Article 41, not original 44(2) and (3)

- **Provisions:** E3, R1, R5, R6; R&O.17/2018 Article 2.
- **Groups affected:** G7.
- **The trap:** the BRIEF describes the 2019 remainder as "Part 6 and whatever the original Article 41 and 44(2)-(3) were". Stage 1 names "44" without limiting it to paragraph (1), so original 44(2) and 44(3) are inside stage 1 (21 November 2014). R&O.17/2018 Article 2 says the remainder is what was "not brought into force by Article 44(2) of that Law or Article 1 of this Act" — so Article 44(2) was itself in force before 1 May 2018 and was what brought stage 1 into force.
- **Discriminating case:** none for a present Article (44(2), 44(3) and 41 are all spent); the difference is in the rows R5 and R6 (stage 1, not stage 3).
- **Suggested handling:** the remainder is Part 6 (Articles 21 to 25) plus original Article 41; R5 and R6 are stage 1 and spent. Not a fork (no discriminating case). The BRIEF's wording should be corrected by the fleet lead.

### T3: "Minister" has five texts, one of which changes at 9.30 a.m.

- **Provisions:** Article 1 "Minister" (`src:26` reads `“Minister” means the Chief Minister;`); every Order-making and MAY/MUST rule of the Minister; E4, E7, E8, E9, E11.
- **Groups affected:** G1 (owner of the definition), G7 (the vintage resolver), G9, and every group whose rules have the Minister as PARTY.
- **The texts** (the text of 2 October 2026 is the one in the consolidated file; the others are rebuilt from the amending instruments):
  - until 30 May 2019: "Chief Minister" (shown only by R&O.40/2019 Schedule 2 paragraph 1(e), which substitutes for "Chief Minister");
  - 31 May 2019 to 1 March 2021: "Minister for External Relations" (R&O.40/2019, made and in force 31 May 2019);
  - 2 March 2021 to 11 April 2023: "Minister for External Relations and Financial Services" (R&O.29/2021 is NOT in the sources; the words are the ones R&O.28/2023 Schedule 2 paragraph 1(4) replaces, so the text is inferred, not shown);
  - 12 April 2023 to the morning of 27 February 2024: "Chief Minister" (R&O.28/2023, made 5 April, in force 7 days after);
  - from 9.30 a.m. on 27 February 2024 to 1 October 2026: "Minister for External Relations" (R&O.10/2024 Schedule 4, in force at 9.30 a.m. that day);
  - from 2 October 2026: "Chief Minister" (R&O.102/2026 Article 1, made 25 September 2026, rest of the Order in force 7 days after).
- **Discriminating cases:** (i) an act at 08:00 on 27 February 2024: the Minister is the Chief Minister; at 10:00 it is the Minister for External Relations; a vintage keyed by DATE alone cannot answer for that day. (ii) R&O.56/2025 was made on 9 October 2025 by "THE MINISTER FOR EXTERNAL RELATIONS" under Article 2(2): consistent with the 2024-2026 text and with no other, which is evidence for the reading of the vintage table.
- **Suggested handling:** `Office of the Minister` as a function of `Vintage of the text`; the vintage resolver in G7 answers REFUSE for a DATE on 27 February 2024 and answers for an instant (F7.1); `the Minister` stays a role (`Legal actor`) everywhere else. The 2021 row is marked "inferred from R&O.28/2023" in a comment and in NOTES.

### T4: "a Minister" in Article 5(2)(a) against the defined term "Minister"

- **Provisions:** 5(2)(a), 5(3), Article 1 "Minister".
- **Groups affected:** G2 (owner), G1.
- **The trap:** `-- src:151 | (a) a Minister;` uses the capitalised word with the indefinite article. The definition makes "Minister" mean one office, and the office changes by vintage (T3); the lead-in "unless the context otherwise requires" lets the context displace it.
- **Discriminating case:** a constitution permits one governor to be the Minister for Health acting in that capacity. Generic reading: the entity does not meet the charity test. Defined-term reading: it does (the Minister for Health is not "the Minister"). Under the defined-term reading the answer also changes with the vintage: in the text of 16 October 2025 the barred Minister is the Minister for External Relations.
- **Suggested handling:** fork F2.3, generic reading taken (a person who is any Minister of the Government of Jersey); the defined-term reading takes `the office of the Minister` (IP3) as an input.

### T5: entity categories overlap, and the new paragraph (ba) is carried through by exclusion only

- **Provisions:** 2(1)(a) to (j) and (ba), 2(3)(a), 8(3)(a)(i) and (ii).
- **Groups affected:** G1 (owner), G3, G7.
- **The trap:** the kinds are not exclusive: 8(3)(a)(i) asks, for an entity in (f) to (j), "whether it also falls within sub-paragraph (a)" (a company that is the sole trustee). Paragraph (ba) was written to avoid overlap with (c) to (h) only (`-- src:54 | (iii) does not fall within any of sub-paragraphs (c) to (h);`). R&O.56/2025 inserted (ba) and amended nothing else, so 8(3)(a)(ii) (details of the enactment for (e), (g), (h), (j)) never mentions (ba), and 2(5) (T6) and 2(3)(a) (F1.1) read around it.
- **Discriminating case:** a Jersey-established NPO body corporate that is a company: (f) applies and (ba) does not ((iii)). A Jersey-established NPO body corporate that is none of (c) to (h): (ba) applies. A company that is the sole trustee of a trust: (a) and (f).
- **Suggested handling:** the kinds of an entity are a LIST; (ba) only in the text of 16 October 2025 and later; the register note (G3) takes the list; no (ba) enactment note is invented (G3 records "none required by 8(3)(a)(ii)" and flags the gap).

### T6: "constitutional Law" is defined for five kinds out of twelve

- **Provisions:** 2(5)(a) to (e); the uses at 2(10)(a)(ii), 2(10)(a)(iv), 2(10)(b)(i), 8(4)(a), 13(2), 13(3), 17(7), 18(3), 31(d).
- **Groups affected:** G1 (owner), G3, G5, G6, G8.
- **The trap:** 2(5) names a Law for trusts, fidéicommis and 1862 associations, foundations, companies, and (e) `-- src:85 | (e) in relation to an entity that is a body incorporated by (but not under) any other Law, that Law.` It has no case for (ba), (g) and (h) ("incorporated under, but not by"), (i) (unincorporated bodies) or (j) (foreign entities).
- **Discriminating case:** a registered charity that is a body incorporated under, but not by, another Jersey enactment: 13(2) ("any provision of the entity's constitution or constitutional Law is of no effect to the extent...") has only the constitution to bite on; 8(4)(a) ("required by its constitutional Law to have a registered office") cannot apply, so the principal address falls to 8(4)(b).
- **Suggested handling:** `Art 2(5)` answers a MAYBE (`NOTHING` for the five kinds); every consumer handles NOTHING by reading the constitution only. Fork F1.3 carries the reading that (g) and (h) have the enactment of incorporation as their constitutional Law.

### T7: "historic section" is used but never defined; "registered charity" excludes it

- **Provisions:** 1 ("general section", "restricted section" defined; "historic section" not), 8(2)(c), 8(5), 10(3)(c), 1 "registered charity".
- **Groups affected:** G3, G1.
- **The trap:** `-- src:34 | “registered charity” means an entity entered for the time being in the general section or the restricted section of the register;` The historic section holds formerly registered charities, which are therefore not "registered charities" (see T16).
- **Suggested handling:** `Standing on the register` has the constructor `formerly registered and entered in the historic section`; `Art 1 the entity is a registered charity` is FALSE for it; the historic section is defined by 8(5) in a comment.

### T8: "misconduct" is defined twice and refers to itself

- **Provisions:** 1 "misconduct", 2(10), 18(4), 14(1)(a), 17(9)(a), 19(1)(a), 27(1)(a), (c).
- **Groups affected:** G1, G6 (owners), G5, G8.
- **The trap:** 2(10)(a) is about a contravention by "a registered charity or by any of its governors"; 2(10)(b) is "the commission by any person, in relation a registered charity or to an excepted foreign charity" and so on "of an offence" (the source has no "to" after "in relation"). 18(4) then defines when "a governor engages in misconduct" (a: a 2(10) contravention or offence; b: concurring in misconduct by the charity; c: assisting or encouraging "another governor to engage in misconduct"; d: concealing). 18(4)(c) refers to the same notion (another governor's misconduct) and 2(10) says a reference to a governor engaging in misconduct "is to be read in accordance with Article 18(4)". 14(1)(a) uses the different phrase "misconduct in the administration of the charity".
- **Discriminating case:** governor A concurs in the charity's contravention (18(4)(b)); governor B assists A (18(4)(c)): B's misconduct needs A's. Governor C assists B: depth three. Governor D is convicted of tax evasion on a personal return unrelated to the charity (2(10)(b)(iii) requires the offence to be "in relation to" a charity, F1.2).
- **Suggested handling:** a least fixed point over the list of governors, depth bounded by the length of the list; the base case is 2(10) plus 18(4)(a), (b), (d). Forks F1.2 and F5.4.

### T9: reporting a reportable matter starts the ban on acting, and not reporting is not an offence

- **Provisions:** 19(2), 19(8), 19(9)(d), 19(10), 19(11), 19(12); 13(6)(e); 27(1)(d).
- **Groups affected:** G6 (owner), G5, G8.
- **The trap:** `-- src:492 | (2) A governor of an entity applying for registration, or of a registered charity, must report any reportable matter promptly to that entity or charity and to the Commissioner.`; `-- src:498 | (8) A person must not act as a governor of a registered charity at any time when the person is in breach of paragraph (2) or (4).`; `-- src:507 | (10) A person must not act as a governor of a registered charity at any time after reporting a reportable matter, unless the governor –` (a) is permitted ... and (b) acts within the condition; `-- src:510 | (11) A person who without reasonable excuse contravenes paragraph (10) commits an offence and is liable to imprisonment for one year and to a fine.` Only (10) is a criminal prohibition.
- **Discriminating cases:** (A) a governor with a reportable matter reports at once and acts the next day, before any permission: offence under (11). (B) The same governor does not report and acts: in breach of (2), barred by (8), and no offence under (11), because (8) is not mentioned. (C) A governor with no reportable matter who ignores the 19(4) request for a declaration: barred by (8); no offence.
- **Suggested handling:** encode (8) and (10) as two SHANT rules; only (10) carries the penalty (IP30); register F6.11 for the reading that (8) is also within (11), and F6.10 for when the ban starts. Breach of (2), (4) or (8) is a "contravention of a provision of this Law" and so misconduct (IP13).

### T10: the duty to register meets the bar on granting, a court order not to register, and a gap for an incomplete application

- **Provisions:** 11(4), 11(5), 19(5), 19(6), 19(9)(c), 20(1)(c), 11(8)(a)(i).
- **Groups affected:** G4 (owner), G6.
- **The trap:** `-- src:319 | (4) If the applicant complies with paragraph (2), with any Regulations under paragraph (3), and with Article 19(5), the Commissioner must register the applicant as a charity if satisfied that –` (six matters); `-- src:328 | (5) If not so satisfied, the Commissioner must refuse to register the applicant.` and `-- src:502 | (c) must not, in the case of an application for registration, grant that application until the issue has been determined and any resulting order or notice complied with;`. 11(4)'s grounds do not include 19(9)(c) or a court order under 20(1)(c) (`order that the entity must not be registered`).
- **Discriminating cases:** (A) every one of 11(4)(a) to (f) is satisfied and a reported fitness issue about a governor is undetermined: MUST register (11(4)) and MUST NOT grant (19(9)(c)). (B) An applicant satisfies (a) to (f) but omits the copy of its constitution (11(2)(b)): 11(4) does not apply (it needs compliance), 11(5) does not apply ("not so satisfied" is about the six matters), and 19(6) says only that a 19(5) failure makes the application "not complete". Neither duty arises.
- **Suggested handling:** forks F4.4 (reading taken: 19(9)(c) and a court order override 11(4); both are inputs IP23, IP24) and F4.3 (reading taken: an incomplete application raises no duty either way; the decision period of 11(8)(a)(i) is an input that does not run until it is complete, F4.2).

### T11: the Commissioner must serve a required steps notice that Article 28 says is invalid

- **Provisions:** 19(9)(e)(i), 27(4), 28(3), 20(1)(d).
- **Groups affected:** G6, G8.
- **The trap:** `-- src:505 | (i) notify the entity that the application will be refused unless the governor is removed, or in the case of a registered charity serve a required steps notice requiring the charity to suspend or remove the governor, or` against `-- src:662 | (3) A required steps notice served on an organized religious charity, or on a governor of such a charity, is invalid to the extent that it purports to impose a requirement to suspend, remove or replace a governor of that charity.`
- **Discriminating case:** the governor of an organized religious charity has a reportable matter that the Commissioner finds disqualifying on determining the issue. Limb (i) would have the Commissioner serve a notice whose only requirement is void; the only valid alternative left in (e) is (ii) (permission). The court route (19(9)(b), 20(1)(d)) is not caught by 28(3).
- **Suggested handling:** fork F6.15 (reading taken: 28(3) prevails; the duty in (e)(i) does not extend to the removal limb for an organized religious charity). IP20.

### T12: Article 33 is a closed list that omits several decisions, and its third-party appeal needs two dates

- **Provisions:** 33(1) to (5); 9(7), 13(5)(b), 13(11)(b), 15(3)(b), 16(2), 19(9), 10(5).
- **Groups affected:** G8 (owner), G3, G5, G6.
- **The trap:** an applicant may appeal a refusal to register and a refusal of the restricted section (33(1)); a registered charity may appeal five named decisions (33(2)); a person served with an Article 26 or required steps notice may appeal the requirement (33(3)); the Attorney General may appeal any decision (33(4)); anyone else may appeal a decision to register on two grounds, each "at both the time of the application and the time of the appeal" (33(5), `src:701`). Not listed: a general-section charity's refused request for the restricted section (9(7), which the Law treats as the same kind of request as an applicant's); a refusal to deregister on application (15(3)(b), though 33(2)(a) lists a decision "to deregister"); refusal of permission under 13(5)(b) or 13(11)(b); the Commissioner's decisions under 19(9); a safety designation under 10(5).
- **Discriminating case:** a charity in the general section asks for the restricted section and is refused (9(7)): has it a right of appeal under Part 8? A charity applies to deregister and is refused on grounds relating to its proposals (15(3)(b)): same question.
- **Suggested handling:** the list is closed (reading taken), the Attorney General is the catch-all (33(4)), and `may appeal under Article 33` answers FALSE for an unlisted decision, with the reason "no appeal is given by Part 8" (not a statement that no other remedy exists; 40(1) preserves independent powers). Fork F8.4 carries the analogy reading. 33(5) takes IP9 and the IP18 pair.

### T13: Article 21 creates two offences for one act, and its parallel limbs differ by one phrase

- **Provisions:** 21(1), (2), (7), (9), (10); 21(3) to (6); 23(1), (2), (5) to (7).
- **Groups affected:** G7 (owner), G6 (37).
- **The trap:** (1) is strict and carries a fine of level 3 (21(10)); (2) needs knowledge and intent and carries 2 years and a fine (21(9)); (7) says (2) applies "whether or not the person making the reference is also the entity, and is referring to itself". An unregistered entity that tells a donor it is registered with the Commissioner, knowing it is not, intending to induce a gift, contravenes both. Separately, `-- src:540 | (ii) to give to the entity any property or financial or other advantage.` in 21(2)(b)(ii), against `-- src:550`, `-- src:560` and `-- src:585`: `(ii) to give any property or financial advantage to the entity.` in 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii).
- **Discriminating cases:** (A) the two-offence act above: penalties cumulative or only the aggravated offence. (B) A person calls an unregistered Jersey entity a "charity" intending to induce volunteers to give their time (an "other advantage"): an offence under 21(2) if the claim was "registered by the Commissioner", not under 21(4).
- **Suggested handling:** forks F7.4 (cumulative taken) and F7.5 (literal difference taken). Penalty data carried, no fine amount invented (IP30).

### T14: two 10-year retention duties, and a number bar with no stated end

- **Provisions:** 8(6), 17(1)(a), 17(1)(b).
- **Groups affected:** G3, G6.
- **The trap:** `-- src:249 | (6) The Commissioner must retain for 10 years, in respect of each registered charity, a copy of –` (constitution and amendments, annual returns, notices served, prescribed documents) and `-- src:444 | (a) must retain the information registered in respect of that entity for 10 years; and` / `-- src:445 | (b) must not assign the registered number of that entity to any other registered charity.` Neither says when the ten years start; 17(1)(b) is joined to (a) by "and" but has no period.
- **Discriminating cases:** a constitution received in 2019 by a charity still registered in 2030: may the 2019 copy be discarded (the period runs from receipt) or not (it runs from deregistration)? A number released in year 11 after deregistration: may it be assigned?
- **Suggested handling:** forks F3.1, F6.5, F6.6.

### T15: deregistration has two notices, a mandatory twin, and retrospective effect "for all purposes"

- **Provisions:** 16(1), 16(2), 17(2) to (5), 13(1), 18, 17(6).
- **Groups affected:** G6 (owner), G5.
- **The trap:** 16(1) is a power ("may, by written notice ... deregister ... if satisfied, after giving the entity written notice specifying reasons and inviting objections within a reasonable time"): two notices. 16(2) is a duty ("must, by written notice ... deregister") when the entity no longer exists. 17(2)(c) and 17(4) speak of "the notice under Article 16(1) or (2)" without saying which of 16(1)'s two. 17(3) makes the termination effective from the past date "for all purposes, including the purposes of any enactment relating to taxation", and 17(4) protects only an act that "is not rendered an offence"; 17(5) applies the preserved-purposes regime to property "acquired before it was deregistered".
- **Discriminating cases:** (A) an entity that has ceased to exist and also no longer meets the charity test: 16(1) may, 16(2) must. (B) a donation received between the past date and the notice: acquired "before it was deregistered" (notice date) or after (effective date)? (C) an amendment of the purposes to a non-charitable one made in that interval: 13(2) bites only while registered. (D) an act between the preliminary notice and the deregistration notice but after the past date: protected by 17(4) or not.
- **Suggested handling:** forks F6.2, F6.3, F6.4; 17(2) holds only for Article 16, not for Article 15 (a voluntary deregistration has no retrospective effect).

### T16: Article 10(4) lets the Commissioner protect a "registered charity" but the historic section is public

- **Provisions:** 10(3)(c), 10(4), 10(5), 1 "registered charity", 8(5).
- **Groups affected:** G3.
- **The trap:** `-- src:296 | (4) Paragraph (5) applies if the Commissioner considers, in relation to a particular registered charity, that the safety or security of any person, property or premises would be significantly put at risk by public access to a matter entered on any section of the register in respect of that charity.` A deregistered entity is not a "registered charity" (T7), yet its historic-section entry (former number and name, summary of the reason, dates) is public under 10(3)(c).
- **Discriminating case:** a deregistered entity whose historic-section summary of reasons would put a person at risk: 10(4) literally does not reach it.
- **Suggested handling:** fork F3.3 (reading taken: literal, FALSE).

### T17: Schedule 1 paragraph 4(3) reserves "whether to refuse" under Article 15(3) but not the grant

- **Provisions:** Sch 1 4(3)(a) to (c); 15(3)(a), (b); 16(1), (2); 11.
- **Groups affected:** G9 (owner), G4, G6.
- **The trap:** `-- src:797 | (a) the decision under Article 11 on whether to register a charity;` / `-- src:798 | (b) the decision under Article 15(3) on whether to refuse to deregister a charity; and` / `-- src:799 | (c) the decision under Article 16 on whether to deregister a charity.` The reserved Article 15(3) decision is the refusal, while for Articles 11 and 16 it is the decision "whether", which covers both outcomes.
- **Discriminating case:** a member of staff, under an authorization, deregisters an entity on its own application (15(3)(a)). Reserved if "whether to refuse" means the one decision whether-or-not-to-refuse; not reserved if only the refusal is.
- **Suggested handling:** fork F9.8 (reading taken: the decision "whether to refuse" is the single decision under 15(3), either outcome reserved). `Decision of the Commissioner` carries subject and outcome (IP27).

### T18: "any Order under paragraph (7), (8) or (9)" names a paragraph that confers no Order

- **Provisions:** 13(7), 13(8), 13(9), 13(10).
- **Groups affected:** G5.
- **The trap:** `-- src:398 | (10) The Minister may by Order, after consulting the Commissioner and any body appearing to the Minister to be representative of interested registered charities, provide that any provision of paragraph (6) or (7), or of any Order under paragraph (7), (8) or (9) –`. Paragraph (8) says "An Order under paragraph (7) may also make provision as to the format and timing ..."; it creates no separate Order.
- **Discriminating case:** the Minister relieves small charities from the consequences of lateness set by an Order that 13(8) allows.
- **Suggested handling:** fork F5.3 (reading taken: the references to an Order under paragraph (8) mean the Order under (7) as extended by (8)).

### T19: the standard of care in Article 18(2) applies only to governors of unincorporated associations

- **Provisions:** 18(2), 18(3), 2(1)(i), 2(8).
- **Groups affected:** G6.
- **The trap:** `-- src:468 | (2) A governor of a registered charity, that is an unincorporated body or association of persons falling within Article 2(1)(i), must in the execution of his or her duties and in the exercise of his or her powers and discretions –` due diligence, prudent person, ability and skill, utmost good faith. All other governors are bound by 18(1) and 18(3) only.
- **Discriminating case:** a director of a registered company charity breaches the prudent-person standard: 18(2) does not apply.
- **Suggested handling:** fork F6.7 (literal taken). Note that "relevant unincorporated entity" (2(8)) is a narrower class used for the governor definition only; 18(2) applies to every 2(1)(i) body.

### T20: Schedules 1 and 2 are parallel, with different numbers, and Schedule 2 carries another name for the Tribunal

- **Provisions:** Sch 1 3(1)(a) (3 months), Sch 2 2(1)(a) (one month); Sch 1 3(2)(a) (4 consecutive weeks), Sch 2 2(2)(a) (8 consecutive weeks); the heading of Schedule 2 against Article 32.
- **Groups affected:** G9.
- **The trap:** `-- src:780` and `-- src:826` read "not less than 3 months’ notice" and "not less than one month’s notice"; `-- src:784` and `-- src:830` read "longer than 4 consecutive weeks" and "longer than 8 consecutive weeks". The other periods (2 weeks before appointing, 6 years, 2 weeks after terminating, 12 years, 4 months for the report) are identical. `-- src:814 | Charity Commission tribunal` heads Schedule 2, while `-- src:686` establishes "the Charity Tribunal" and Article 1 defines "tribunal" as that body.
- **Checked:** the PDF text layer agrees word for word on all four figures and on the heading, so these are the Law's own figures and not transcription errors.
- **Suggested handling:** encode both sets of figures as written; do not unify. The heading is not operative.

### T21: re-appointment and the 12-year cap

- **Provisions:** Sch 1 1(5), 1(6), 3(4)(a), (c); Sch 2 1(5), 1(6), 2(4)(a), (c).
- **Groups affected:** G9.
- **The trap:** the Minister fixes a period "not more than 6 years" and may re-appoint, and "references in this paragraph to appointment include re-appointment" (so 1(2) views, 1(3) notice, 1(5) cap all apply to a re-appointment); 3(4)(c) ends the appointment when the person "completes 12 years (whether consecutive or in aggregate) of service", whatever period was fixed.
- **Discriminating case:** a person who has served 10 years is re-appointed for 5: the appointment ends at 12 years, two years in.
- **Suggested handling:** the appointment's effective end is the earlier of the period's end, the 12-year mark, and the other expiry events.

### T22: "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" exists only from 16 December 2019

- **Provisions:** Sch 1 2(4)(a), 4(7); endnote [5], E5; Dormant Bank Accounts Law Articles 20(1), 20(2)(a), 30(3), 31(2).
- **Groups affected:** G9, G7 (vintages).
- **The trap:** L.1/2017 Article 30(3) inserted the words at the beginning of 2(4)(a) and substituted "Subject to Article 20(1) ..., the" at the start of 4(7). Its Article 31(2) brings it into force on days the States appoint by Act; the Table gives 16 December 2019 and the Act is not in the sources. 2(4)(b) (fees to the States) and 4(1), 4(6) (the Minister's duty to make staff and accommodation available) are not made subject to it, only who pays. Article 20(2)(a) of that Law allows its Fund to "defray the cost of the remuneration ... and the cost of providing staff, accommodation or equipment".
- **Discriminating cases:** before 16 December 2019 the funding rule has no carve-out; from that date it does, but only if the Order under Article 20(1) of that Law directs a distribution (an input).
- **Suggested handling:** fork F9.9; the carve-out is a vintage-gated input.

### T23: the power to demand information serves one purpose; the offence of false information serves two

- **Provisions:** 26(1), 26(2), 26(10), 11(2)(f)(ii).
- **Groups affected:** G8, G4.
- **The trap:** `-- src:619` ties the demand to "the purpose of determining whether to serve a required steps notice"; `-- src:635` makes it an offence to give false information "intending it to be used by the Commissioner for the purpose of an application for registration or for the purpose of determining whether to serve a required steps notice". Applicants and their governors are not within 26(2). Information for an application is requested under 11(2)(f)(ii), which has no sanction of its own.
- **Suggested handling:** encode 26(1) for the notice purpose only; 26(10) for both; a demand to an applicant under 26 REFUSES (not a power the Law gives).

### T24: "year" in Part 4 is unqualified; the Schedules say "calendar year"

- **Provisions:** 8(3)(j), 13(7), 13(9)(a); Sch 1 4(8); Sch 2 3(3).
- **Groups affected:** G3, G5, G9.
- **The trap:** `-- src:392` says "the year to which the return relates", `-- src:234` "the most recent year"; `-- src:807` says "in each calendar year". The drafter wrote "calendar" when meant.
- **Suggested handling:** forks F3.2 and F5.2, both typed `Meaning of the year of an annual return` (IP33); calendar year taken.

### T25: a UK-extended body is both a Jersey entity and possibly an excepted foreign charity

- **Provisions:** 2(1)(h), 2(3)(a), 21(3) to (6), 22(2)(a)(i).
- **Groups affected:** G1, G7.
- **The trap:** a body incorporated under, but not by, a UK Act extended to Jersey is within 2(1)(h), hence a Jersey entity (2(3)(a)); it is also established under the law of the United Kingdom (22(2)(a)(i)). 21(3) and (4) restrict Jersey entities with no exemption for excepted foreign charities; 21(5) and (6) restrict those that are neither.
- **Discriminating case:** such a body, not registered, calls itself a "charity" in Jersey: 21(3) applies to it (as a Jersey entity); its status as an excepted foreign charity gives it nothing.
- **Suggested handling:** G7 evaluates 21(3), (4) on the Jersey-entity fact first; no fork (the text is clear, if odd). 22(3)(b) ("is not a registered charity") is redundant against 21's own opening words.

### T26: Article 37 reaches partnerships and bodies corporate, not unincorporated associations or trustees

- **Provisions:** 37(1), 37(2), 2(1)(a), 2(1)(i), 2(3).
- **Groups affected:** G7.
- **The trap:** `-- src:728 | (1) If an offence under this Law, committed by a limited liability partnership, a separate limited partnership or a body corporate is proved to have been committed with the consent or connivance of –` An unincorporated association (2(1)(i)) and "the trustees of a trust" are entities (so can offend under 21(3)) but are neither.
- **Discriminating case:** a committee member of an unincorporated association who connived in its 21(3) offence: not within 37(1) as written.
- **Suggested handling:** fork F7.6 (literal taken); the penalty is the entity's (IP30).

### T27: a philosophical-belief purpose is analogous to religion, but Article 28 asks about "Article 6(1)(c)"

- **Provisions:** 6(1)(c), 6(1)(p), 6(2)(f), 28(1)(a), 8(3)(h).
- **Groups affected:** G2, G8.
- **The trap:** `-- src:194 | (f) for the purposes of paragraph (1)(p), the advancement of any philosophical belief (whether or not involving belief in a god) is analogous to the purpose set out in paragraph (1)(c).` makes such a purpose fall within (p), not (c). 28(1)(a) allows categorization of charities that "meet the charity test by virtue of Article 6(1)(c)".
- **Discriminating case:** a humanist association: charitable under (p) via 6(2)(f); eligible to be categorized as an organized religious charity?
- **Suggested handling:** forks F2.5 (G2 classifies; (p), not (c), taken) and F8.3 (G8 reads 28(1)(a)); IP11.

### T28: 11(2)(e)(ii) joins two requirements, and 13(9)(b) is written for a registered charity

- **Provisions:** 11(2)(e)(ii), 13(9)(b), 8(3)(m).
- **Groups affected:** G4, G5.
- **The trap:** `-- src:310` joins "any payment made to any governor ... in the 12 months preceding the application" and "if an Order under Article 13(9)(b) applies to the registered charity, a draft of the proposed statement under that Order" in one item; an applicant is not yet "the registered charity".
- **Suggested handling:** two requirements in one rule body; IP29 reads "applies to the registered charity" as applying to the applicant as if registered.

### T29: three vintages are only partly shown by the sources

- **Provisions:** E5, E6, E7, Article 1 "Minister", "Comptroller", Schedule 1.
- **Groups affected:** G7 (owner), G1, G9.
- **The trap:** (i) R&O.29/2021 (2 March 2021) is in the Table but not among the inputs: the text it produced is known only from the words R&O.28/2023 replaced. (ii) The pre-1 January 2020 meaning of "Comptroller" is the Income Tax (Jersey) Law 1961 only because L.13/2019 Schedule 3 paragraph 1 says it substituted the Revenue Administration (Jersey) Law 2019 for those words; R&O.136/2019, which appointed 1 January 2020, is not in the sources. (iii) The Act appointing 16 December 2019 for L.1/2017 is not in the sources. (iv) No text before 1 January 2019 is among the nine versions.
- **Suggested handling:** each such row says in a comment whether it is shown or inferred; a vintage question about a day the sources do not decide REFUSES.

### T30: Part 5 and Article 2(10) come into force a year and a half before the Article they cite

- **Provisions:** 2(10)(b), 19(1)(g) (in force 21 November 2014 and 1 May 2018 respectively) against Article 22 (Part 6, in force 1 January 2019); Articles 21 and 23 offences from 1 January 2019.
- **Groups affected:** G7, G1, G6, the integrator.
- **The trap:** `-- src:111` says "an excepted foreign charity (within the meaning of Article 22)" from 21 November 2014, but Article 22 is in the 1 January 2019 remainder; between 1 May 2018 and 31 December 2018 Part 5 applies with Article 2(10)(b) citing an Article not yet in force. The text before 1 January 2019 is not among the sources (T29).
- **Discriminating case:** a conviction on 1 July 2018 of an offence in relation to an excepted foreign charity.
- **Suggested handling:** the integrator's wrapper answers REFUSE for the Article 22 limb on a day before 1 January 2019; G1 takes IP26 as an input and never assumes it.

## (g) Forks

Candidate forks in the R4 shape of the BRIEF, grouped by owner group: id, provision, readings, discriminating case.
In each, reading **A is the reading proposed** for the default (`TYPICALLY`) and the other readings are to be made callable with a test; an encoder may change the reading taken by registering the change in the `FRAGMENT`.
The record of each group is named `Interpretation of <scope>` as in section (b); each fork id is also the name of its row in the group's `FRAGMENT`.
A fork whose alternative needs a number the Law does not give (a "promptness" threshold, a period set by Order) takes that number as an extra `GIVEN` of the alternative reading only, so the default reading never invents it.
Dates in the cases are chosen to differ under the readings; `add months` and `add years` of the `daydate` library clamp to the last day of the target month.

### G1: Articles 1 and 2

- **F1.1: does "(a) to (h)" reach the inserted (ba)?** Provisions 2(1)(j), 2(3)(a), 2(1)(ba)(iii).
  - A (taken): ranges are by letter order, so (ba) lies inside "(a) to (h)": an NPO body corporate established under Jersey law and in none of (c) to (h) is a Jersey entity, and a foreign analogue can be "substantially similar" to it under (j).
  - B: the ranges are read as of the Law's enactment and exclude (ba); an NPO body corporate is then not a Jersey entity under 2(3)(a) (and 2(3)(b) is only for 2(1)(i) bodies).
  - Discriminating case: a Jersey NPO body corporate that is not in (c) to (h), unregistered, calls itself a "charity" in Jersey: 21(3) applies to it under A; under B only 21(5) can (it is not a Jersey entity), limited to "activities in Jersey". Also 11(4)(c)(i) versus (ii) as its route in. Text of 16 October 2025 and later only.
- **F1.2: must the offence in 2(10)(b) be "in relation to" a charity?** Provisions 2(10)(b), 18(4)(a), 19(1)(g).
  - A (taken): the words `-- src:111 | (b) the commission by any person, in relation a registered charity or to an excepted foreign charity (within the meaning of Article 22) or to an entity equivalent to a registered charity under the law of a jurisdiction other than Jersey, of an offence –` govern every limb (i) to (vi): the offence must be connected to a registered charity, an excepted foreign charity or a foreign equivalent.
  - B: only limb (i) (an offence under that charity's constitutional Law) is tied to a charity; limbs (ii) to (v) are offences by any person who is a governor of the charity.
  - Discriminating case: a governor convicted of an Income Tax (Jersey) Law 1961 offence on a personal return unrelated to the charity: misconduct and a reportable matter under B, neither under A.
- **F1.3: what is the constitutional Law of a body "incorporated under, but not by"?** Provisions 2(5)(e), 2(1)(g), (h).
  - A (taken): nothing; 2(5) has no case for (ba), (g), (h), (i), (j) (T6), so `Art 2(5)` answers NOTHING.
  - B: for (g) and (h) it is the enactment under which the body is incorporated (2(5)(e)'s "by (but not under)" read as a slip for either preposition).
  - Discriminating case: a charity incorporated under, but not by, another Jersey enactment; 8(4)(a) asks whether its constitutional Law requires a registered office in Jersey: A answers (b) main premises, B may answer (a).
- **F1.4: is the governor of a trust whose trustee is a company the company only, or also its directors?** Provisions 2(7)(a), (c), 2(1)(a), 8(3)(a)(i).
  - A (taken): the trustee (the company) is the governor of the trust; its directors are governors of the company-entity only.
  - B: where the company is both "the trustees" (2(1)(a)) and a company (2(1)(f)), 8(3)(a)(i) shows the same body in both kinds, so both 2(7)(a) and 2(7)(c) apply and its directors are governors.
  - Discriminating case: a director of a sole corporate trustee is bankrupt: a reportable matter in relation to a governor (19(1)(e)) under B; under A the director has no reporting duty under 19(2).
- **F1.5: is "published" the publisher's opinion or the manner's likelihood?** Provisions 1 "publish".
  - A (taken): the publisher's own opinion that the manner is likely to bring the information to attention (the text says "in the opinion of the person publishing").
  - B: an objective likelihood.
  - Discriminating case: a notice posted only in a locked cabinet, which its publisher honestly believes adequate.

### G2: Articles 3 to 7

- **F2.1: "all of its purposes" with no purposes, or only ancillary ones.** Provisions 5(1)(a).
  - A (taken): at least one charitable purpose is required; ancillary purposes count only if ancillary to one of the entity's own charitable purposes (5(1)(a)(ii)); an entity with no purposes does not meet the test.
  - B: vacuous truth: no purposes at all satisfies (a).
  - C: purely ancillary purposes satisfy (a) without any charitable purpose.
  - Discriminating cases: an entity with an empty purposes list; an entity whose only purpose is an incidental one.
- **F2.2: "acting in that capacity" in Article 5(2).** Provisions 5(2), `-- src:154 | acting in that capacity.`
  - A (taken): the words qualify the Minister, member or equivalent: the bar applies where the constitution permits a person to control the entity or be a governor *as* a Minister/member (ex officio or in that office).
  - B: the bar applies whenever the constitution permits any person who is a Minister (etc.) to be a governor, however they act.
  - Discriminating case: a trust deed permits a sitting member of the States Assembly to be a trustee in a personal capacity.
- **F2.3: "a Minister": the generic office or the defined term?** Provisions 5(2)(a), Article 1 "Minister", T3, T4.
  - A (taken): any Minister of the Government of Jersey (the context displaces the definition).
  - B: the defined term: the office `the office of the Minister` (IP3), which depends on the vintage.
  - Discriminating cases: the Minister for Health as a permitted governor; the same constitution evaluated in the text of 16 October 2025 (the barred office is the Minister for External Relations) and 2 October 2026 (the Chief Minister).
- **F2.4: "within a reasonable time" and "as soon as practicable" (5(7), 5(8)).** Provisions 5(7), 5(8).
  - A (taken): an input Boolean (`the Commissioner did so within a reasonable time`, `the Minister did so as soon as practicable`); no number is invented.
  - B: measured from the day the guidance is issued or amended (5(7)) or received (5(8)) against a threshold of N days supplied as an extra input.
  - Discriminating case: guidance issued 2026-01-01, copy given 2026-03-01, N = 30: late under B; under A whatever the input says.
- **F2.5: a philosophical-belief purpose: (p) or (c)?** Provisions 6(2)(f), 6(1)(c), 6(1)(p), T27.
  - A (taken): the purpose falls within (p) (the text says "for the purposes of paragraph (1)(p)"); the head recorded is (p) and `Art 6 the entity has a purpose within the advancement of religion` is FALSE for it.
  - B: it is treated as within (c) for every purpose of the Law (analogy as identity).
  - Discriminating case: the purpose of a humanist association; consumed by F8.3.

### G3: Articles 8 to 10

- **F3.1: from when do the 10 years of 8(6) run?** Provisions 8(6), 17(1)(a), T14.
  - A (taken): from the day the Commissioner receives or makes each copy (document by document).
  - B: from the charity's deregistration (so a charity's records are kept for as long as it is registered and 10 years after).
  - C: a rolling window: at any time the Commissioner must hold the copies of the preceding 10 years.
  - Discriminating case: a constitution copy received 2019-03-01 by a charity still registered; asked on 2029-03-02: may it be discarded? A yes, B no, C yes (the copy is outside the window, but the later amendments are not).
- **F3.2: "the most recent year" (8(3)(j)).** Provisions 8(3)(j), 13(7), IP33.
  - A (taken): the calendar year that has most recently ended (`the calendar year`); typed `Meaning of the year of an annual return`.
  - B: the charity's own financial year.
  - C: the twelve months from the latest anniversary of registration.
  - Discriminating case: asked on 2027-02-01 for a charity with a 30 June year-end that has filed for the year to 30 June 2026: sent for "the most recent year" under B, not under A (the year 2026 is the most recent calendar year, ended on 2026-12-31).
- **F3.3: does "a particular registered charity" in 10(4) include a deregistered entity?** Provisions 10(4), 10(3)(c), T16.
  - A (taken): no, by Article 1; the Commissioner cannot designate a historic-section matter non-public.
  - B: yes; "registered charity" in 10(4) includes a formerly registered one.
  - Discriminating case: a historic-section summary of reasons that would significantly endanger a person.

### G4: Articles 11 and 12

- **F4.1: "the 12 months preceding the application" (11(2)(e)(ii)).** Provisions 11(2)(e)(ii).
  - A (taken): the 12 months ending on the day before the day of application: from the same calendar day one year earlier (clamped on 29 February) to the day before the application day, both inclusive.
  - B: the 12 months ending on the day of application.
  - C: the 12 whole calendar months before the month of application.
  - Discriminating cases (application 2026-03-15): a payment on 2025-03-15 (in A, out B, in C); on 2026-03-15 (out A, in B, out C); on 2026-03-01 (in A and B, out C). For an application on 2028-02-29: the start is 2027-02-28 (clamped, A) or 2027-03-01 (rolled).
- **F4.2: what is the date of "the application"?** Provisions 11(2)(e)(ii), 11(8)(a)(i), 19(6).
  - A (taken): the date it is lodged.
  - B: the date it becomes complete (19(6): it is "not complete" until 19(5) is complied with).
  - Discriminating case: lodged 2026-03-01, completed 2026-03-20: a payment on 2026-03-10 is outside the window under A and inside under B; the same anchor sets the start of any decision period an Order prescribes under 11(8)(a)(i).
- **F4.3: an application that does not comply with 11(2), the Regulations or 19(5).** Provisions 11(4), 11(5), 19(6), T10.
  - A (taken): no duty to register or to refuse arises (the application remains pending); `Art 11 what the Commissioner must do on the application` answers NOTHING with the reason "application not complete".
  - B: the Commissioner must refuse (non-compliance means "not so satisfied").
  - Discriminating case: everything in 11(4)(a) to (f) is satisfied but the constitution copy of 11(2)(b) is missing.
- **F4.4: 11(4) against 19(9)(c) and 20(1)(c).** Provisions 11(4), 19(9)(c), 20(1)(c), T10.
  - A (taken): 19(9)(c) (IP23) and a court order not to register (IP24) displace the duty to register: the Commissioner must not register, and the decision period is not a ground.
  - B: 11(4) prevails once (a) to (f) hold.
  - C: genuine conflict: REFUSE.
  - Discriminating case: a reported fitness issue is undetermined; the applicant otherwise satisfies 11(4)(a) to (f); also a court order that the entity must not be registered.
- **F4.5: does "any other registered charity" in 12(1)(a) include a formerly registered one?** Provisions 12(1)(a), 12(4), 33(5)(b).
  - A (taken): no (Article 1); an identical name in the historic section is not a ground.
  - B: yes.
  - Discriminating case: a proposed name identical to that of a deregistered charity.

### G5: Articles 13 and 14

- **F5.1: "promptly" (13(6)).** Provisions 13(6).
  - A (taken): an input Boolean `the report was made promptly`.
  - B: measured from the event against N days (extra input).
  - C: measured from the charity's awareness against N days.
  - Discriminating case: event 2026-03-01, awareness 2026-03-20, report 2026-03-25, N = 14: late under B, timely under C.
- **F5.2: "the year to which the return relates" (13(7), 13(9)(a)).** Provisions 13(7), 13(9)(a), IP33, T24.
  - A (taken): the calendar year (`Meaning of the year of an annual return`).
  - B: the charity's financial year.
  - C: the twelve months from each anniversary of registration.
  - Discriminating case: a payment to a governor on 2026-02-10 by a charity with a 30 June year-end falls in the return for the year 2026 under A and 2025/26 under B.
- **F5.3: "any Order under paragraph (7), (8) or (9)" in 13(10).** Provisions 13(10), 13(8), T18.
  - A (taken): the words "any Order under paragraph (7), (8) or (9)" are read so that an Order under paragraph (8) means the Order under (7) as extended by (8) (format, timing, lateness).
  - B: literal: there is no Order under (8), so a relief Order cannot reach the timing and lateness provisions.
  - Discriminating case: a relief Order dispensing small charities from the lateness consequences.
- **F5.4: "misconduct in the administration of the charity" (14(1)(a)).** Provisions 14(1)(a), 2(10), 14(1)(b).
  - A (taken): misconduct as defined in 2(10) (IP12) that bears on the administration of the charity.
  - B: any misconduct as defined.
  - C: the ordinary meaning (not the defined term).
  - Discriminating case: a governor's related-offence conviction (2(10)(b)(iii)) with no effect on the charity's administration.
- **F5.5: is a return sent on the due date timely?** Provisions 13(8), 13(7), P10.
  - A (taken): yes: sent on or before the due date the Order sets (an input).
  - B: no: it must be sent before the due date.
  - Discriminating case: due 2027-03-31, sent 2027-03-31.

### G6: Articles 15 to 20

- **F6.1: an application to deregister without the information 15(2) requires.** Provisions 15(2), 15(3).
  - A (taken): no duty arises; the Commissioner neither must deregister nor must refuse, and the application stays pending.
  - B: the Commissioner may refuse.
  - C: the Commissioner must refuse.
  - Discriminating case: the entity supplies none of the information requested.
- **F6.2: 16(1) (may, with prior notice) against 16(2) (must, entity no longer exists).** Provisions 16(1), 16(2), T15.
  - A (taken): 16(2) governs where the entity no longer exists: mandatory, no prior notice.
  - B: 16(1)'s procedure also applies; 16(2) adds a duty to deregister after it.
  - Discriminating case: an entity that has ceased to exist and also fails the charity test.
- **F6.3: which notice does "the notice under Article 16(1) or (2)" mean?** Provisions 17(2)(c), 17(4), 16(1).
  - A (taken): the notice by which the Commissioner deregisters.
  - B: the preliminary notice specifying reasons and inviting objections.
  - Discriminating case: preliminary notice 2026-03-01, deregistration notice 2026-04-01, past date 2025-01-01; an act on 2026-03-15.
- **F6.4: "property of the charity that was acquired before it was deregistered" under retrospective effect.** Provisions 17(5), 17(3), T15.
  - A (taken): "deregistered" means the effective (past) date under 17(3), "for all purposes": property acquired after that date is not "remaining property".
  - B: the date of the notice.
  - Discriminating case: a donation received between the past date and the notice.
- **F6.5: from when do the 10 years of 17(1)(a) run?** Provisions 17(1)(a), 8(6).
  - A (taken): from the date of the deregistration notice ("after deregistering").
  - B: from the effective (possibly retrospective) date.
  - Discriminating case: notice 2026-06-01, effective date 2021-06-01; asked on 2033-01-01.
- **F6.6: does the bar on reassigning the number end?** Provisions 17(1)(b).
  - A (taken): never.
  - B: after the 10 years of (a).
  - Discriminating case: a reassignment attempt in year 11.
- **F6.7: scope of the standard of care in 18(2).** Provisions 18(2), T19.
  - A (taken): only governors of charities that are unincorporated bodies within 2(1)(i).
  - B: every governor of a registered charity.
  - Discriminating case: a director of a registered company breaches the prudent-person standard.
- **F6.8: what does "within a reasonable time" qualify in 18(4)(d)(ii)?** Provisions 18(4)(d)(ii).
  - A (taken): only "fails ... to take proper steps"; concealment is misconduct at once.
  - B: both limbs.
  - Discriminating case: a governor conceals the misconduct for a month, then discloses it within what would have been a reasonable time.
- **F6.9: does "has been disqualified" include an expired disqualification?** Provisions 19(1)(c), (d); contrast (f) "whether or not spent" and (g) "unspent".
  - A (taken): yes: any disqualification ever imposed.
  - B: only one in force.
  - Discriminating case: a company-director disqualification imposed in 2010 for 5 years.
- **F6.10: when does the 19(10) ban start?** Provisions 19(2), 19(10).
  - A (taken): on reporting to the Commissioner.
  - B: on reporting to the charity.
  - C: only when both reports are made.
  - Discriminating case: a governor reports to the charity but not to the Commissioner, then acts.
- **F6.11: is acting while in breach of 19(2) or (4) an offence?** Provisions 19(8), 19(11), T9.
  - A (taken): no: 19(11) mentions only (10).
  - B: yes: (8) is read into (11) purposively.
  - Discriminating case: an unreported bankruptcy and the governor acts.
- **F6.12: "promptly" in 19(2).** Provisions 19(2).
  - A (taken): an input Boolean; B: from the matter arising; C: from awareness; same pattern and case as F5.1.
- **F6.13: the "reasonable time" for objections in 16(1).** Provisions 16(1).
  - A (taken): the time the notice specifies governs; whether it is reasonable is an input Boolean, and an unreasonable time invalidates the deregistration.
  - B: any specified time suffices.
  - Discriminating case: a notice that gives one day.
- **F6.14: the 15-year limit of 20(5).** Provisions 20(5).
  - A (taken): the period may not exceed 15 years from the date of the order: the last day may be the anniversary date, `add years` start 15, clamped on 29 February.
  - B: rolled on 29 February (start 2028-02-29: bound 2043-03-01).
  - C: the last day is the day before the anniversary (inclusive counting).
  - Discriminating cases: an order starting 2028-02-29 and ending 2043-03-01 (valid under B only), ending 2043-02-28 (valid under A and B, not C).
- **F6.15: the duty in 19(9)(e)(i) against Article 28(3).** Provisions 19(9)(e)(i), 28(3), T11.
  - A (taken): 28(3) prevails: for an organized religious charity the duty to serve a notice requiring removal does not arise; (ii) remains.
  - B: the duty stands and the notice is partly void.
  - C: conflict: REFUSE.
  - Discriminating case: a governor of an organized religious charity with a reportable matter.
- **F6.16: the unit of the terms of imprisonment in 19(11) and 20(6).** Provisions 19(11) (one year), 20(6) (2 years).
  - A (taken): calendar months, 12 and 24, as F7.8; typed `Unit of a term of imprisonment` (IP35).
  - B: days, 365 and 730.
  - Discriminating case: a sentence of 366 days from 2027-03-01 under 19(11): within the maximum under A, over it under B.

### G7: Articles 21 to 25, 37 to 43 and the endnotes

- **F7.1: the day, or the instant, at which a text takes effect.** Provisions E2, E3, E9 and every vintage date; T3.
  - A (taken): the named day is the first day in force; the text of 27 February 2024 takes effect at 9.30 a.m.; a DATE-only query for 27 February 2024 answers REFUSE and an instant query answers.
  - B: the whole of 27 February 2024 is in the new text.
  - Discriminating case: an act at 08:00 on 27 February 2024 (the Minister is the Chief Minister under A).
- **F7.2: "comes into force 7 days after it is made".** Provisions R&O.28/2023 Article 3, R&O.56/2025 Article 2, R&O.102/2026 Article 7(6).
  - A (taken): the day of making is excluded; the 7th day after is the first day in force. The three instruments in the sources fix it: 5 April + 7 = 12 April 2023; 9 October + 7 = 16 October 2025; 25 September + 7 = 2 October 2026, each the date the Table gives.
  - B: the eighth day (the day of making counted as day 1).
  - Discriminating case: made 9 October 2025: 16 October (A) or 17 October (B).
- **F7.3: the commencement table in original or present numbers.** Provisions E1 to E3, R1 to R4, T1.
  - A (taken): original numbers, converted through the renumbering map.
  - B: present numbers read literally.
  - Discriminating case: present Article 41 on 2018-01-01 (in force under A; not under B).
- **F7.4: the same act under 21(1) and 21(2).** Provisions 21(1), (2), (7), (9), (10), T13.
  - A (taken): cumulative: both offences are made out; each carries its own penalty (IP30).
  - B: alternative: where 21(2) is made out the strict offence of (1) is displaced.
  - Discriminating case: an unregistered entity states to a donor, knowing it is untrue, that it is registered with the Commissioner.
- **F7.5: "or other advantage" in 21(2)(b)(ii) but not in 21(4)(b)(ii), 21(6)(b)(ii) and 23(2)(b)(ii).** Provisions 21(2), 21(4), 21(6), 23(2).
  - A (taken): the difference is preserved.
  - B: harmonised: "property or financial or other advantage" throughout.
  - Discriminating case: a person calls an unregistered Jersey entity a "charity" intending to induce volunteers to give their time.
- **F7.6: who is within Article 37(1).** Provisions 37(1), 37(2), T26.
  - A (taken): a limited liability partnership, a separate limited partnership or a body corporate, and their partners and officers.
  - B: also an unincorporated association (2(1)(i)) and the trustees of a trust, and their governors.
  - Discriminating case: a committee member of an unincorporated association who connived in its 21(3) offence.
- **F7.7: how is the date of service of a notice fixed?** Provisions 38, 8(3)(k), 17(4), 26, 27.
  - A (taken): the date the notice is received by the person served.
  - B: the date it is sent.
  - Discriminating case: sent by post 2026-06-01, received 2026-06-03; an act on 2026-06-02 (17(4) protection applies under A).
- **F7.8: the unit of a term of imprisonment ("2 years") in 21(9) and 23(7).** Provisions 21(9), 23(7); the same fork is F6.16, F8.8 and F9.13 for the other groups' terms, all typed `Unit of a term of imprisonment` (IP35).
  - A (taken): calendar months (12, 24, 3), added by `add months`; the amount is a maximum; stored as months.
  - B: days (365, 730, 90).
  - Discriminating case: a sentence of 366 days from 2027-03-01 is within "one year" under A (the calendar year to 2028-03-01 is 366 days) and not under B. A weak fork: kept because the assignment lists a sentence as a kind of period; the encoder may drop it if no test of a sentence in days exists.

### G8: Articles 26 to 36

- **F8.1: when does the one year of 26(5) start, and when do proceedings extend it?** Provisions 26(5), 26(4)(a).
  - A (taken): from the date the document is provided (or retained) under 26(4)(a).
  - B: from the date of the notice under 26(1).
  - Discriminating case: notice 2026-02-01, document provided 2026-02-20, proceedings commenced 2027-02-10: the document may be kept to the conclusion of the proceedings under A; under B the year had ended on 2027-02-01.
- **F8.2: "as soon as practicable" in 26(6).** Provisions 26(6).
  - A (taken): an input Boolean; B: measured from the request against N days (extra input).
  - Discriminating case: request 2026-05-01, copy supplied 2026-05-20, N = 7.
- **F8.3: does Article 28(1)(a) "by virtue of Article 6(1)(c)" include a philosophical-belief purpose?** Provisions 28(1)(a), 6(2)(f), T27.
  - A (taken): no (F2.5 A): only a purpose within (c).
  - B: yes.
  - Discriminating case: a humanist association the Minister is asked to categorize.
- **F8.4: is the list in Article 33 closed?** Provisions 33(1) to (5), T12.
  - A (taken): closed; the Attorney General alone may appeal any decision (33(4)).
  - B: unlisted decisions of the same kind (a refused restricted-section request by a general-section charity, a refusal to deregister) are appealable by analogy.
  - Discriminating case: a general-section charity's refused request under 9(7).
- **F8.5: the ground of an appeal from the Tribunal to the court.** Provisions 34(1), 35(1).
  - A (taken): only that the decision "was unreasonable having regard to all the circumstances" (35(1)); an error of law is reached only by the Tribunal's own reference (35(3)).
  - B: the ground is as wide as 34(1): wrong or unreasonable on the merits, facts or law.
  - Discriminating case: a Tribunal decision that is wrong in law but not unreasonable.
- **F8.6: from when does an appeal time limit run?** Provisions 36(2)(a), (b).
  - A (taken): from the giving of notice of the decision (36(2)(b) provides for notice of decisions and reasons "for the purpose of enabling appeals to be brought within any time limits").
  - B: from the decision.
  - Discriminating case: decision 2026-01-01, notice of it 2026-01-10, limit 30 days (extra input), appeal lodged 2026-02-05: timely under A (ends 2026-02-09), late under B (ends 2026-01-31).

- **F8.7: how is "a time specified in the notice" counted?** Provisions 26(1)(a), (b), 27(2).
  - A (taken): the notice specifies a date and time, which is the deadline; the Law fixes no counting convention.
  - B: the notice specifies a duration ("within 14 days"), which runs from the date of service (F7.7).
  - Discriminating case: a notice served by post on 2026-06-01, received 2026-06-03, requiring steps "within 14 days": 2026-06-15 or 2026-06-17.
- **F8.8: the unit of the terms of imprisonment in 26(7), 26(10) and 29(1).** Provisions 26(7) (3 months), 26(10) and 29(1) (2 years).
  - A (taken): calendar months, 3 and 24, as F7.8; typed `Unit of a term of imprisonment` (IP35).
  - B: days, 90 and 730.
  - Discriminating case: a sentence of 91 days from 2027-11-30 under 26(7) is within three calendar months (to 2028-02-29, clamped) under A and over 90 days under B.

### G9: Schedules 1 and 2

- **F9.1: "at least 2 weeks before appointing" (Sch 1 1(3); Sch 2 1(3)).**
  - A (taken): the appointment day is at least 14 days after the day the notice is presented.
  - B: 14 clear days between them (the appointment day at least 15 days after).
  - Discriminating case: notice 2026-03-01, appointment 2026-03-15.
- **F9.2: "not more than 6 years" (Sch 1 1(5); Sch 2 1(5)).**
  - A (taken): the end date may be as late as the anniversary, `add years` start 6 (clamped).
  - B: the end date is at most the day before the anniversary (the start day counted).
  - Discriminating case: an appointment from 2026-03-01 to 2032-03-01.
- **F9.3: "not less than 3 months'" (Sch 1 3(1)(a)) and "not less than one month's" (Sch 2 2(1)(a)) notice.**
  - A (taken): the office ends when the notice runs out; the earliest end is `add months` the notice date (clamped).
  - B: the office ends when the notice is given.
  - C: month addition rolled (30 February becomes 2 March).
  - Discriminating cases: notice given 2026-11-30, resignation effective 2027-02-28: valid under A, not under C; the office has already ended on 2026-11-30 under B.
- **F9.4: "absent ... for a period longer than 4 consecutive weeks" (Sch 1 3(2)(a)); 8 weeks (Sch 2 2(2)(a)).**
  - A (taken): count the days absent, both ends included; longer than 28 (56) days.
  - B: elapsed days, end minus start.
  - Discriminating case: absent from 2026-03-01 to 2026-03-29 inclusive: 29 days, longer than 28 under A; elapsed 28 under B, so not longer.
- **F9.5: "not more than 2 weeks after terminating" (Sch 1 3(3); Sch 2 2(3)).**
  - A (taken): the notice may be presented up to 14 days after the termination day.
  - B: the termination day is day 1, so the 14th day is 13 days after.
  - Discriminating case: terminated 2026-03-01, notice presented 2026-03-15.
- **F9.6: "completes 12 years (whether consecutive or in aggregate) of service" (Sch 1 3(4)(c); Sch 2 2(4)(c)).**
  - A (taken): calendar arithmetic: service periods are added in order, each added by years, months and days, with `add months` clamping.
  - B: 12 years as 4,380 days (365-day years).
  - Discriminating case: aggregate service of 4,380 days across two periods: complete under B; under A not complete (12 calendar years from 2026-03-01 are 4,383 days, three leap days included).
- **F9.7: "in no case later than 4 months after the end of that year" (Sch 1 4(9); Sch 2 3(4)).**
  - A (taken): the end of the year is 31 December; plus 4 months, clamped: 30 April.
  - B: rolled: 1 May.
  - Discriminating case: the report supplied on 2027-05-01 (for the year 2026): late under A, timely under B.
- **F9.8: the reservation in Sch 1 4(3)(b).** Provisions Sch 1 4(3), 15(3), T17.
  - A (taken): "the decision under Article 15(3) on whether to refuse to deregister" is the single decision under 15(3), whichever outcome: staff may not decide either.
  - B: literal: only the refusal is reserved; a member of staff may deregister on application.
  - Discriminating case: a member of staff deregisters an entity on its own application.
- **F9.9: "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" (Sch 1 2(4)(a), 4(7)).** Provisions Sch 1 2(4)(a), 4(7), T22.
  - A (taken): to the extent an Order under that Article directs a distribution to the cost, the cost is met from that Fund instead of the annual income of the States.
  - B: the States remain liable; the Fund only reimburses.
  - Discriminating case: such an Order is in force (an input) and the Fund is empty: who must pay. The words exist only in the text of 16 December 2019 and later.
- **F9.10: "as soon as practicable" in Sch 1 4(9), 4(10) and Sch 2 3(4), 3(5).**
  - A (taken): an input Boolean; B: measured from receipt against N days (extra input).
  - Discriminating case: report received 2027-02-01, laid 2027-03-15, N = 28.
- **F9.11: does service as a designated relevant person count toward the 12 years?** Provisions Sch 1 3(4)(c), 4(4), 4(5).
  - A (taken): no: service as Commissioner is service under an appointment; a designated person is "treated as the Commissioner" only temporarily.
  - B: yes.
  - Discriminating case: a person designated for 14 months, later appointed.
- **F9.12: is a report required for a calendar year in which the office was held only part of the year?** Provisions Sch 1 4(8), Sch 2 3(3).
  - A (taken): yes: "in each calendar year" includes the year in which the Commissioner (or the responsible officer) takes up or leaves the office, for the part held.
  - B: only for a whole calendar year.
  - Discriminating case: an appointment from 2026-11-01: a report for 2026, due by 2027-04-30 (F9.7), under A; none under B.
- **F9.13: the unit of the 2-year cap in Sch 2 4(3)(f).** Provisions Sch 2 4(3)(f).
  - A (taken): calendar months, 24, as F7.8; typed `Unit of a term of imprisonment` (IP35).
  - B: days, 730.
  - Discriminating case: Regulations create an offence with a maximum of 24 months; applied from 2027-03-01 that is 731 days, within the cap under A and over it under B.

## 8. The domain nouns

`FLEET_DIR/deposit/domain.l4` holds the nouns that two or more groups use, written once; it imports `prelude` and nothing else, starts with no `@lang` line, and `L4_BIN check` on it returns `Check succeeded.` with no diagnostics (exit 0; `check --json` returns an empty diagnostics list).
It has no rules and no directives.
Every field carries a `@desc`.

| noun | why it is here (who decides it, who reads it) |
| --- | --- |
| `Vintage of the text` | the nine point-in-time versions plus "before the first consolidated version"; resolved by G7, read by G1 (Minister, Comptroller, (ba)) and G9 (the Dormant Bank Accounts words); IP2 |
| `Office of the Minister` | the three offices the definition "Minister" names across the texts; decided by G1, read by G2 (F2.3 B); IP3 |
| `Unit of the Law` | a Part, an Article (present or original number), a Schedule; the argument of the in-force function; IP4. Four constructors because the commencement table is in the original numbers (T1) |
| `Kind of entity` | the eleven kinds of Article 2(1) plus "added by Order" (twelve constructors; the Order may add sub-paragraphs); an entity has a LIST of them |
| `Standing on the register` | not on, applicant, general, restricted, historic; an input; read by every group; IP5, IP6 |
| `Legal actor` | the PARTY of every regulative rule, in one place so that the integrator composes rules of different groups; the roles only, not identities |
| `Kind of reportable matter` | the eight descriptions of Article 19(1), a field of `Governor`; decided by G6, read by G5, G8 (IP21) |
| `Governor` | a record: name, natural person, resident in Jersey, Jersey entity by 2(3)(a), reportable matters; derived by G1, read by G1, G3, G5, G6, G7, G8 |
| `Head of charitable purpose` | the sixteen heads of Article 6(1) plus heads added under 6(3); decided by G2, read by G2 and G8 (IP11) |
| `Purpose` | description, head (MAYBE), ancillary, political, philosophical belief; a field of `Entity` because Article 5(1)(a) quantifies over all purposes |
| `Entity` | the entity as Article 2 leaves it (name, standing, kinds, Jersey entity, governors, purposes); the one record the Parts after Article 2 take (IP5). The raw facts G1 reads to derive three of its fields stay in a G1 record |
| `Registered charity` | the register's record: the entity, number, name(s), dates, the approved statements, organized-religious flag (IP7); fields only G3 reads stay in G3's record |
| `Meaning of the year of an annual return` | the shared enumeration of F3.2 and F5.2 (IP33) |
| `Belief that prompts a required steps notice` and `Recipient of a required steps notice` and `Required steps notice` | decided by G8, read by G1 (2(10)(a)(iii)), G3 (8(3)(k)), G6 (16(1)(c), 19(1)(a)); IP19 |
| `Basis of deregistration` | decided by G6, read by G3 (8(5)(c)), G8 (33(2)(a)); IP32 |
| `Subject of a decision of the Commissioner`, `Outcome of a decision of the Commissioner`, `Decision of the Commissioner` | decided by G3 to G6 and G8, read by G8 (which decisions are appealable, 33) and G9 (which are reserved from staff, Sch 1 4(3)): subject and outcome because 33 attaches to a refusal and 4(3) reserves the decision "whether"; IP27 |
| `Order of the court over a charity` | the nine kinds of Article 14(3); decided by G5, read by G6 (17(9)); IP31 |
| `Unit of a term of imprisonment` | the shared enumeration of F6.16, F7.8, F8.8 and F9.13 (IP35) |
| `Fine provided`, `Penalty provided` | the penalty data of the offences; decided by each offence's owner, read by G7 (37(1)) and G9 (Sch 2 4(3)(f)); IP30 |

Not in `domain.l4`, with the reason:

- **Raw facts for Article 2(1) and 2(7), 2(10)**: used by G1 only.
- **The facts about an application** (G4), **the facts about the constitution under 5(2)** (G2), **the register entry's extra fields** (G3), **appointments and reports** (G9), **statements and the stage of commencement** (G7): used by one group.
- **A three-valued "satisfied / not satisfied / undecided" type**: the language has `MAYBE` and `REFUSE` (BRIEF "Where the source does not answer").
- **A money type for fines**: the Law states no amounts; level 3 is a number only.
- **A date or instant of an act** as a shared noun: each rule that needs a day takes `DATE` (or `DATETIME` for the one instant, F7.1).
- **The identity of a Minister, Commissioner or judge**: roles only; `Office of the Minister` is the one identity the Law's own text changes.
- **Interpretation records**: one per group (section (g)); only the one type shared between groups by decision, `Meaning of the year of an annual return`, is here.

If a group needs a noun that is missing, the "nouns request" goes in its `FRAGMENT`; the integrator adds it to a separate file, never into `domain.l4`, unless two groups ask.

## 9. What the sources do not answer

Each item here is a place where an encoder must produce a named refusal or an input, never a plausible value.

1. **The text of the Law before 1 January 2019.** The nine versions begin there. The enacted text of 2014 and the three-stage commencement in between are known only from the Table of Legislation History and R&O.17/2018; whatever the Law said on a given day before 2019 is not in the sources (it is inferred only for "Minister", from R&O.40/2019).
2. **R&O.29/2021.** It is in the Table (2 March 2021) but not among the inputs. The text of "Minister" it produced is inferred from R&O.28/2023 (T3, T29). What else, if anything, it changed in the Law is unknown.
3. **R&O.136/2019, and the Act appointing 16 December 2019 for L.1/2017.** The commencement of the Revenue Administration (Jersey) Law 2019 amendment ("1 January 2020") and of the Dormant Bank Accounts additions to Schedule 1 are the Table's dates, not read from the appointing instruments (T29, T22).
4. **The original Articles 41 and 44(2), 44(3).** "Spent, omitted". R&O.17/2018's headings suggest the original Article 41 concerned taxation; nothing more is in the sources (R1, R5, R6).
5. **Every Order and every set of Regulations the Law empowers.** None is in the sources except R&O.56/2025 (the one Order under Article 2(2)). The powers and the places the content is read: 2(2), 5(3), 6(3) (G1, G2); 8(3)(n), 8(5)(e), 8(6)(d), 9(1)(d), 9(2), 9(3), 10(2) (G3); 11(3), 11(7), 11(8) (G4); 13(6)(h), 13(7), 13(8), 13(9), 13(10), 13(12) (G5); 16(1)(d), 19(1)(h) (G6); 21(8), 22(2)(a)(ii), 22(4), 22(5), 23(4), 24, 25, 38, 39, 40, 41, 42 (G7); 27(5), 28, 31(f), 36(2) (G8); Schedule 2 4(3) (G9). In particular unknown: the funding condition and the grounds for the restricted section, the decision period for an application, the annual return's due date and the consequences of lateness, the appeal time limits, the categories of organized religious charity, the exceptions to Part 6, the prescribed jurisdictions for excepted foreign charities, the statements a charity must make, how a notice is served.
6. **The amount of "level 3 on the standard scale"** (21(10), 23(6), 26(7)); it is in the Criminal Justice (Standard Scale of Fines) (Jersey) Law, not in the sources. The Law states no maximum for any other fine ("a fine").
7. **The text of the other enactments named**: the Trusts (Jersey) Law 1984, Companies (Jersey) Law 1991, Foundations (Jersey) Law 2009, Non-Profit Organizations (Jersey) Law 2008, Loi (1862), Revenue Administration (Jersey) Law 2019, the financial-services Laws, the tax Laws, the Rehabilitation of Offenders rules (what is a "spent" conviction), the Employment of States of Jersey Employees (Jersey) Law 2005, the Scottish and UK charity statutes of Article 28, and the Dormant Bank Accounts (Jersey) Law 2017 beyond Articles 20(1), 20(2)(a), 30(3) and 31(2) as quoted in L.1/2017. Whether a body is a company, an NPO, a trust is an input.
8. **The Interpretation (Jersey) Law 1954**, which would settle how a period is counted ("clear days", a month): not among the inputs. The counting conventions are therefore forks (section (g)) and the only evidence is the three "7 days after it is made" instruments (F7.2).
9. **Whether an appeal suspends the decision appealed** (34(2)(a) lets the Tribunal make an interim order; nothing makes a decision suspended automatically), **who prosecutes** the offences, and any procedure beyond the penalties stated; **what a court or tribunal "sees fit"** to order; **the Commissioner's, the Minister's and the court's judgement** wherever the text says "opinion", "satisfied", "considers", "believes", "reasonably requires".
10. **Anything after 2 October 2026.** The text is "from 2 October 2026 to Current"; later amendments, if any, are not in the sources.
11. **Whether the consolidated text is exactly the enacted text** outside the amended provisions. The licence note says the site's contents are "for information purposes only"; the text was cross-checked word for word against the official PDF text layer (no difference except hyphenation, heading case and footnote markers), not against the enacted Law.

## 10. Notes for the integrator

1. **Wiring.** Section (c) names every standard `GIVEN` and its producer; the integrator wires by name. Where a producer is a field of `Entity` or `Registered charity`, the integrator derives the field from the producer's export once and passes the same record to every consumer. Check that the field equals the export (IP5 to IP7) with an assertion in the integration tests.
2. **Commencement is the integrator's wrapper, not a group's gate.** Each headline `@export` of G2 to G9 is wrapped by a function that first asks `Commencement: the unit of the Law is in force on` for the unit that contains the provision, and REFUSES (or answers `NOTHING`) if it is not. The units: Articles 1 and 2 and Part 2 and Part 3 (Articles 3 to 7) and the Schedules and Articles 32, 38 to 43: stage 1 (21 November 2014); Part 4 (8 to 17), Part 5 (18 to 20), Part 7 (26 to 31), Part 8 other than Article 32 (33 to 36), Article 37: stage 2 (1 May 2018); Part 6 (21 to 25): stage 3 (1 January 2019). Note T30: Article 2(10)(b) cites Article 22.
3. **The vintage matrix is the integrator's test.** For each of the nine vintages and the day before each change, assert: `Art 1 the Minister` (G1), `Art 1 the Law that defines the Comptroller` (G1), whether (ba) is among the kinds of a Jersey NPO body corporate (G1), and whether the DBAL words are in force (G9). G7's own tests cover only the resolver. On 27 February 2024 the DATE form REFUSES and the instant form answers (F7.1).
4. **Forks that must be set together.** F3.2 and F5.2 (one `Meaning of the year of an annual return`); F3.1 and F6.5 (both 10-year retention periods; the readings may differ but the integrator should state the pair); F2.5 and F8.3 (a philosophical-belief purpose); F4.2 and F7.7 (when "the application", "the notice" is dated); F6.16, F7.8, F8.8 and F9.13 for every term of imprisonment (one `Unit of a term of imprisonment`, IP35). The fork registers of the groups map 1:1 to their record fields; the integrator's `NOTES.md` merges them.
5. **Breach is a fact the integrator must supply (IP13).** Each group's prohibitions and duties yield BREACH in a `#TRACE`; "misconduct" (2(10)(a)(i)) asks only for a Boolean. The integrator maps one to the other in the integration tests and says so in NOTES; no group calls another's trace.
6. **Orders and Regulations are inputs, by Article.** Section 9, item 5, lists them. A caller of an `@export` that depends on one (the decision period, the due date of the annual return, the appeal time limit, the restricted-section grounds) supplies it, or receives a named refusal.
7. **Corrections to the BRIEF found by the survey.** (i) The remainder of the staged commencement is Part 6 and the original Article 41 only (T2); original 44(2) and (3) are in stage 1. (ii) Articles 41 and 42 are enabling powers to make Regulations that amend other enactments, not amendments (J8). (iii) The two Schedule 1 additions are the only amendments of this Law by L.1/2017 (its Article 30(3)). (iv) The brief names R&O.29/2021 among the amendments of "Minister"; the instrument itself is not among the inputs.
8. **Counts to expect.** 851 coverage rows (one per node of the source: 43 Articles, 35 definitions with 4 sub-paragraphs, every paragraph and lettered or numbered item, 8 Schedule paragraphs, the two Schedules, 22 endnote rows, 3 front-matter rows); 35 integration points; 48 periods; 96 terminology rows; 30 traps; 68 candidate forks. Each encoder's FRAGMENT coverage must reproduce the rows of its group, and the integrator should diff the union against `coverage.tsv`.
9. **Do not merge vintages.** A function that takes `the vintage of the text` answers for that vintage only. No vintage-independent "Minister" exists.
10. **The cleanroom.** This plan was written from the sources named in the BRIEF only. Nothing under the forbidden directories was opened.
