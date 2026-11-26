# PLAN-K2.md -- K2 of Regulation (EU) 2016/679 (GDPR), and the keel as K2 completed it

Written by K2 (Sonnet 5.5) for P2 and the parts that follow.
Status of this file: every statement below was checked on 2026-11-26 against the files in this folder (the check is `check.sh`, whose output is in `notes/K2-NOTES.md`), except the lines marked "not checked".
Later parts read this file and do NOT read K2's code.
Target compiler: `main`, build 1.6.112 (`e4f4bf3`, 2026-11-18); leave `JL4_LIBRARY_PATH` unset.
The text is the Publications Office consolidated version of 4.5.2016 (a documentation tool with no legal effect; the Official Journal text is authentic).
No recital was read or encoded.

## 1 What K2 wrote, and who may edit it

K2 encodes Article 1, Article 2(3) and (4), Article 3, the lead-in and points (3), (4), (5), (9) to (26) of Article 4, and records Article 99 as `inert` machinery (lines 12-18, 27-35, 36-38, 41-43, 47-73, 1076-1080, and the footnote of point (25) at line 1081 of `eu-gdpr-2016-679-consolidated-20160504.txt`).
Points (1), (2), (6), (7), (8) of Article 4 are P1's (`gdpr-definitions.l4`).

| file | what it is | who may edit |
| --- | --- | --- |
| `gdpr-core-2.l4` | the keel's added nouns: DECLARE only (imports `gdpr-core`) | nobody after K2 |
| `gdpr-definitions-2.l4`, `gdpr-definitions-2-tests.l4` | Art 4 lead-in and points (3), (4), (5), (9) to (26) as functions, the categories of Art 9(1) that points (13) to (15) give, one regulative rule (Art 4(9)); and their tests | nobody after K2 |
| `K2-art-1.l4`, `K2-art-2b.l4`, `K2-art-3.l4`, `K2-tests-art-1.l4`, `K2-tests-art-2b.l4`, `K2-tests-art-3.l4` | layer 1 for Article 1(3), 2(3), 2(4), 3 and the combined answer "this Regulation applies" | K2 only |
| `K2-seat-subject.l4`, `K2-seat-controller.l4`, `K2-cases-seat-subject.l4`, `K2-cases-seat-controller.l4`, `K2-cases-mirror.l4` | the seat layer and its cases | K2 only |
| `PLAN-K2.md`, `notes/K2-NOTES.md`, `notes/gen-seats.py` | records, and the script that wrote the five seat files from the layer-1 signatures | K2 only; a lead merges the notes into `NOTES.md` and `PLAN.md` |

How to take a name from K2: IMPORT `gdpr-core`, `gdpr-core-2`, `gdpr-definitions` and `gdpr-definitions-2` (the keel; the two `-2` modules import `gdpr-core`, so import all four in one folder).
Do NOT import a `K2-` module: take its answer as an INPUT fact with the name given in section 5.
A module may import only modules in its own folder.

## 2 Naming rule (PLAN.md section 2, followed unchanged)

- Every top-level name K2 defines begins with the label of the provision it implements (`Art 4(11) ...`, `Art 3(2) ...`), types and constructors included.
- The seat names of K2 begin `K2 subject ...` and `K2 controller ...`; its questions begin `Under Article N, as a data subject, ...` and `Under Article N, as a controller, ...`.
- Nothing in K2's modules repeats a name of `gdpr-core.l4` or `gdpr-definitions.l4`: measured with a probe module (not kept) that imports `gdpr-core`, `gdpr-core-2`, `gdpr-definitions`, `gdpr-definitions-2`, `K2-art-1`, `K2-art-2b`, `K2-art-3`, `K2-seat-subject` and `K2-seat-controller` together and calls one function of each of the three definitions-and-keel modules: 3 assertions satisfied, no "multiple definitions" error.
  The `P1-` modules were not in the builder's folder when K2 was written, so a clash between a K2 name and a `P1-` name was not measured then. In this row they sit together, and `check.sh` runs each module on its own: no module imports a `P1-` module together with a K2 or P2 one, so a clash with a `P1-` name is not measured by any run. The two `tests-independent-2*.l4` modules import K2 and P2 modules together and read without a clash.
- A later part writes `P3 controller ...` and so on, and names its own functions with its own provision labels.

## 3 The keel's added modules (importable)

### 3.1 `gdpr-core-2.l4` (imports `prelude` and `gdpr-core`; no rule, no constant)

| type | members |
| --- | --- |
| `Art 4(4) personal aspect` | 10 |
| `Art 4(9) party` | 1 |
| `Art 4(9) action` | 1 |
| `Art 4(11) how the data subject signifies agreement` | 3 |
| `Art 4(12) consequence of a breach of security` | 9 |
| `Art 4(16) which establishment is the main establishment` | 4 |

Glosses.
`Art 4(4) personal aspect`: the nine aspects the profiling definition names ("in particular") and `Art 4(4) some other personal aspect`.
`Art 4(9) party` and `Art 4(9) action`: the party and the act of the one regulative rule of K2, one constructor each.
`Art 4(11) how the data subject signifies agreement`: the two ways the definition names and `in some other way, with no statement and no clear affirmative action` (silence, a pre-ticked box).
`Art 4(12) consequence of a breach of security`: the eight consequences the definition names and `some other consequence`.
`Art 4(16) which establishment is the main establishment`: the four answers of point (16)(a) and (b).

### 3.2 `gdpr-definitions-2.l4` (imports `prelude`, `gdpr-core`, `gdpr-core-2`)

One function per defined term; a point with sub-points that ask different questions has one function per sub-point ((16)(a), (16)(b)).
Every function answers `MAYBE` (of a `BOOLEAN`, of an enumeration or of a list), except the one regulative rule, which is a `DEONTIC`; `JUST FALSE` is the "means" no, and `NOTHING` is not covered (rule of 2026-10-29, assumed, not ruled).
Arguments are positional, in the order shown.

| function | inputs (name and type) | answer |
| --- | --- | --- |
| `Art 4 lead-in the definitions of Article 4 apply to the term` | `the term is used for the purposes of this Regulation` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(3) the act is a restriction of processing` | `the personal data are stored` (BOOLEAN); `the personal data are marked` (BOOLEAN); `the aim of the marking is to limit the processing of the personal data in the future` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(4) the processing is profiling` | `the processing is processing of personal data` (BOOLEAN); `the processing is automated` (BOOLEAN); `the personal aspects that the personal data are used to evaluate` (LIST OF Art 4(4) personal aspect); `the aspects relate to a natural person` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(5) the processing is pseudonymisation` | `the processing is processing of personal data` (BOOLEAN); `the personal data can no longer be attributed to a specific data subject without the use of additional information` (BOOLEAN); `the additional information is kept separately` (BOOLEAN); `the additional information is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(9) the body is a recipient` | `body` (Kind of person or body); `the personal data are disclosed to the body` (BOOLEAN); `the body is a third party` (BOOLEAN); `the personal data are received in the framework of a particular inquiry` (BOOLEAN); `the receipt is in accordance with Union or Member State law` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(9) the processing by the public authority of the data it receives in a particular inquiry is in compliance with the applicable data protection rules` | `body` (Kind of person or body); `the personal data are received in the framework of a particular inquiry` (BOOLEAN); `the receipt is in accordance with Union or Member State law` (BOOLEAN); `the processing complies with the applicable data protection rules according to the purposes of the processing` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(9) the public authority must process the data it receives in a particular inquiry in compliance with the applicable data protection rules` | none | DEONTIC Art 4(9) party Art 4(9) action |
| `Art 4(10) the body is a third party` | `body` (Kind of person or body); `the body is the data subject` (BOOLEAN); `the body is the controller` (BOOLEAN); `the body is the processor` (BOOLEAN); `the body is a person who, under the direct authority of the controller or processor, is authorised to process personal data` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(11) the indication is the consent of the data subject` | `the indication is freely given` (BOOLEAN); `the indication is specific` (BOOLEAN); `the indication is informed` (BOOLEAN); `the indication is unambiguous` (BOOLEAN); `the indication is of the data subject's wishes` (BOOLEAN); `how the data subject signifies agreement` (Art 4(11) how the data subject signifies agreement); `the agreement is to the processing of personal data relating to the data subject` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(12) the incident is a personal data breach` | `there is a breach of security` (BOOLEAN); `what the breach of security leads to` (LIST OF Art 4(12) consequence of a breach of security); `the personal data are transmitted, stored or otherwise processed` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(13) the data are genetic data` | `the data are personal data` (BOOLEAN); `the data relate to the inherited or acquired genetic characteristics of a natural person` (BOOLEAN); `the data give unique information about the physiology or the health of that natural person` (BOOLEAN); `the data result from an analysis of a biological sample from the natural person in question` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(14) the data are biometric data` | `the data are personal data` (BOOLEAN); `the data result from specific technical processing` (BOOLEAN); `the data relate to the physical, physiological or behavioural characteristics of a natural person` (BOOLEAN); `the data allow or confirm the unique identification of that natural person` (BOOLEAN); `the data are facial images or dactyloscopic data` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(15) the data are data concerning health` | `the data are personal data` (BOOLEAN); `the data relate to the physical or mental health of a natural person` (BOOLEAN); `the data relate to the provision of health care services to the natural person` (BOOLEAN); `the data reveal information about the health status of the natural person` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(13) to (15) the categories of Article 9(1) that the data fall in by these definitions` | `the data are genetic data` (MAYBE BOOLEAN); `the data are biometric data` (MAYBE BOOLEAN); `the biometric data are processed for the purpose of uniquely identifying a natural person` (BOOLEAN); `the data are data concerning health` (MAYBE BOOLEAN) | MAYBE (LIST OF Art 9(1) category of personal data) |
| `Art 4(13) to (15) the category of Article 9(1) that the data fall in by these definitions` | `the data are genetic data` (MAYBE BOOLEAN); `the data are biometric data` (MAYBE BOOLEAN); `the biometric data are processed for the purpose of uniquely identifying a natural person` (BOOLEAN); `the data are data concerning health` (MAYBE BOOLEAN) | MAYBE Art 9(1) category of personal data |
| `Art 4(16)(a) the main establishment of a controller` | `the controller has establishments in more than one Member State` (BOOLEAN); `the controller's central administration is in the Union` (BOOLEAN); `the decisions on the purposes and means of the processing are taken in another establishment of the controller in the Union` (BOOLEAN); `that other establishment has the power to have such decisions implemented` (BOOLEAN) | MAYBE Art 4(16) which establishment is the main establishment |
| `Art 4(16)(b) the main establishment of a processor` | `the processor has establishments in more than one Member State` (BOOLEAN); `the processor has a central administration in the Union` (BOOLEAN); `the processor has an establishment in the Union where the main processing activities in the context of the activities of an establishment of the processor take place` (BOOLEAN); `the processor is subject to specific obligations under this Regulation` (BOOLEAN) | MAYBE Art 4(16) which establishment is the main establishment |
| `Art 4(17) the person is a representative` | `person` (Kind of person or body); `the person is established in the Union` (BOOLEAN); `the person is designated by the controller or processor in writing pursuant to Article 27` (BOOLEAN); `the person represents the controller or processor with regard to their respective obligations under this Regulation` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(18) the body is an enterprise` | `body` (Kind of person or body); `the body is engaged in an economic activity` (BOOLEAN); `the body is a partnership or an association` (BOOLEAN); `the partnership or association is regularly engaged in an economic activity` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(19) the set of undertakings is a group of undertakings` | `an undertaking in the set is a controlling undertaking` (BOOLEAN); `every other undertaking in the set is controlled by that controlling undertaking` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(20) the policies are binding corporate rules` | `the rules are personal data protection policies` (BOOLEAN); `the policies are adhered to by a controller or processor established on the territory of a Member State` (BOOLEAN); `the policies are for transfers or a set of transfers of personal data` (BOOLEAN); `the transfers are to a controller or processor in one or more third countries` (BOOLEAN); `the transfers are within a group of undertakings` (BOOLEAN); `the transfers are within a group of enterprises engaged in a joint economic activity` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(21) the body is a supervisory authority` | `body` (Kind of person or body); `the body is independent` (BOOLEAN); `the body is established by a Member State` (BOOLEAN); `the body is established pursuant to Article 51` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(22) the supervisory authority is a supervisory authority concerned by the processing` | `the body is a supervisory authority` (BOOLEAN); `the controller or processor is established on the territory of the Member State of that supervisory authority` (BOOLEAN); `data subjects residing in the Member State of that supervisory authority are substantially affected by the processing` (BOOLEAN); `data subjects residing in the Member State of that supervisory authority are likely to be substantially affected by the processing` (BOOLEAN); `a complaint has been lodged with that supervisory authority` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(23) the processing is cross-border processing` | `the processing is processing of personal data` (BOOLEAN); `the processing takes place in the context of the activities of establishments in more than one Member State of a controller or processor in the Union` (BOOLEAN); `the controller or processor is established in more than one Member State` (BOOLEAN); `the processing takes place in the context of the activities of a single establishment of a controller or processor in the Union` (BOOLEAN); `the processing substantially affects data subjects in more than one Member State` (BOOLEAN); `the processing is likely to substantially affect data subjects in more than one Member State` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(24) the objection is a relevant and reasoned objection` | `the objection is to a draft decision` (BOOLEAN); `the objection is as to whether there is an infringement of this Regulation, or whether envisaged action in relation to the controller or processor complies with this Regulation` (BOOLEAN); `the objection clearly demonstrates the significance of the risks posed by the draft decision as regards the fundamental rights and freedoms of data subjects` (BOOLEAN); `the free flow of personal data within the Union is at issue` (BOOLEAN); `the objection clearly demonstrates the significance of the risks posed by the draft decision as regards the free flow of personal data within the Union` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(25) the service is an information society service` | `the service is a service as defined in point (b) of Article 1(1) of Directive (EU) 2015/1535` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(26) the body is an international organisation` | `the body is an organisation governed by public international law, or a subordinate body of such an organisation` (BOOLEAN); `the body is another body set up by, or on the basis of, an agreement between two or more countries` (BOOLEAN) | MAYBE BOOLEAN |

Notes on use.
`Art 4(22) ...` takes `the body is a supervisory authority` as a plain BOOLEAN: a caller derives it with `Art 4(21) the body is a supervisory authority ... EQUALS JUST TRUE`.
`Art 4(13) to (15) ...` take the three answers of points (13), (14), (15) as `MAYBE BOOLEAN` and the purpose of the biometric data as a BOOLEAN; the list function answers `NOTHING` whenever any of the three answers is `NOTHING` (the list is not decided, whatever the other two say: a definition that gives no answer may be met too), `JUST EMPTY` only when all three are `JUST FALSE`, and otherwise the full list of the definitions that are `JUST TRUE`.
`JUST EMPTY` is NOT "the data are not special": the other five categories of Art 9(1) are not defined in Art 4.
The single-choice function is unchanged in meaning: any definition that is `JUST TRUE` gives its category whatever the other two answer (the first of genetic, biometric, health when more than one holds, any one bringing Art 9(1)), and it answers `NOTHING` when none is `JUST TRUE`.
A caller that wants Art 9(1)'s yes or no from these definitions should ask the single-choice function; a caller that wants every category asks the list function and must have all three answers (fork FK4-6, changed after review R3).
The regulative rule `Art 4(9) the public authority must process ...` is a `DEONTIC` and cannot be compared in `#ASSERT`; trace it.

## 4 The layer-1 modules of K2 (read these names; do not import them)

| module | function | inputs (name and type) |
| --- | --- | --- |
| `K2-art-1.l4` | `Art 1(3) the restriction or prohibition of the free movement of personal data within the Union for reasons connected with data protection is barred` | `the personal data move within the Union` (BOOLEAN); `the measure restricts or prohibits that movement` (BOOLEAN); `the reason for the measure is connected with the protection of natural persons with regard to the processing of personal data` (BOOLEAN) |
| `K2-art-2b.l4` | `Art 2(3) Regulation (EC) No 45/2001 applies to the processing, where it is by the Union institutions, bodies, offices or agencies` | `the processing is by the Union institutions, bodies, offices or agencies` (BOOLEAN) |
| `K2-art-2b.l4` | `Art 2(3) this Regulation applies to the processing, where it is by the Union institutions, bodies, offices or agencies` | `the processing is by the Union institutions, bodies, offices or agencies` (BOOLEAN) |
| `K2-art-2b.l4` | `Art 2(3) the Union legal act applicable to such processing is adapted to the principles and rules of this Regulation in accordance with Article 98` | `the Union legal act is applicable to the processing of personal data by the Union institutions, bodies, offices and agencies` (BOOLEAN); `the act has been adapted to the principles and rules of this Regulation in accordance with Article 98` (BOOLEAN) |
| `K2-art-2b.l4` | `Art 2(4) this Regulation is without prejudice to the application of Directive 2000/31/EC` | `the matter is the application of Directive 2000/31/EC` (BOOLEAN); `the matter is the liability rules of intermediary service providers in Articles 12 to 15 of that Directive` (BOOLEAN) |
| `K2-art-3.l4` | `Art 3(1) the territorial limb: the processing is in the context of the activities of an establishment of a controller or a processor in the Union` | `the processing is in the context of the activities of an establishment of a controller or a processor in the Union` (BOOLEAN); `the processing takes place in the Union` (BOOLEAN) |
| `K2-art-3.l4` | `Art 3(2) the territorial limb: the processing is of data subjects in the Union by a controller or processor not established in the Union, and the activities are related to offering goods or services or to monitoring behaviour` | `the data subjects are in the Union` (BOOLEAN); `the controller or processor is not established in the Union` (BOOLEAN); `the processing activities are related to the offering of goods or services to those data subjects in the Union` (BOOLEAN); `a payment of the data subject is required` (BOOLEAN); `the processing activities are related to the monitoring of the behaviour of those data subjects` (BOOLEAN); `their behaviour takes place within the Union` (BOOLEAN) |
| `K2-art-3.l4` | `Art 3(3) the territorial limb: the processing is by a controller not established in the Union, in a place where Member State law applies by virtue of public international law` | `the controller is not established in the Union` (BOOLEAN); `the processing is in a place where Member State law applies by virtue of public international law` (BOOLEAN) |
| `K2-art-3.l4` | `Art 3 this Regulation applies to the processing of personal data` | `Art 2(1) and (2) the processing is within the material scope of this Regulation` (MAYBE BOOLEAN); `the processing is by the Union institutions, bodies, offices or agencies` (BOOLEAN); `the processing is in the context of the activities of an establishment of a controller or a processor in the Union` (BOOLEAN); `the processing takes place in the Union` (BOOLEAN); `the data subjects are in the Union` (BOOLEAN); `the controller or processor is not established in the Union` (BOOLEAN); `the processing activities are related to the offering of goods or services to those data subjects in the Union` (BOOLEAN); `a payment of the data subject is required` (BOOLEAN); `the processing activities are related to the monitoring of the behaviour of those data subjects` (BOOLEAN); `their behaviour takes place within the Union` (BOOLEAN); `the controller is not established in the Union` (BOOLEAN); `the processing is in a place where Member State law applies by virtue of public international law` (BOOLEAN) |

Each answers `MAYBE BOOLEAN`.
`K2-art-3.l4` imports `K2-art-2b.l4` and calls `Art 2(3) this Regulation applies to the processing, where it is by the Union institutions, bodies, offices or agencies`.

## 5 Seams

I read ONLY the range of K2 and Article 99 of the text, PLAN.md, NOTES.md, `inputs/HEADINGS.md` and `inputs/PARTS.md`.
I did NOT read Articles 5 to 98 (except for the two clauses of Art 99).
The "likely asker" column below comes from the headings in `inputs/HEADINGS.md` and from the cross-references in PLAN.md section 4, not from reading the asking provisions: each is a pointer for the part that owns it to check, not a claim about what that provision says.

### 5.1 Seams K2 PROVIDES (the answering side)

| answering provision | K2 function (full name in section 3 or 4) | how a later part uses it | likely asker (not checked) |
| --- | --- | --- | --- |
| Art 4(11) 'consent' | `Art 4(11) the indication is the consent of the data subject` | P1 takes the plain input `the data subject has given consent to the processing of his or her personal data` (BOOLEAN): it corresponds to the function `EQUALS JUST TRUE`. "Explicit" (P1's `the data subject has given explicit consent to the processing of those personal data`) is NOT defined in Art 4(11): it stays a plain BOOLEAN. | Art 6(1)(a), 7, 8, 9(2)(a) (P1); Art 13, 14, 17, 20 (P2) |
| Art 4(25) 'information society service' | `Art 4(25) the service is an information society service` | P1's plain input `the information society services are offered directly to a child` (BOOLEAN) is the function `EQUALS JUST TRUE` together with Art 8(1)'s own fact "offered directly to a child", which is not Art 4(25)'s. | Art 8(1) (P1); Art 17 (P2) |
| Art 4(13), (14), (15) | `Art 4(13) to (15) the category of Article 9(1) ...` and `... the categories of Article 9(1) ...` | answer P1's choice `Art 9(1) category of personal data` (and P1's plain input `the category of the personal data`) | Art 9(1), 9(4) (P1); Art 22(4), 35, 37 (P2, P4) |
| Art 4(3) 'restriction of processing' | `Art 4(3) the act is a restriction of processing` | call | Art 18, 19 (P2) |
| Art 4(4) 'profiling' | `Art 4(4) the processing is profiling` | call | Art 22 (P2) |
| Art 4(5) 'pseudonymisation' | `Art 4(5) the processing is pseudonymisation` | call; P1 reads none (Art 6(4)(e) names it as an example) | Art 25, 32 (P3) |
| Art 4(9) 'recipient', Art 4(10) 'third party' | `Art 4(9) the body is a recipient`, `Art 4(10) the body is a third party` | call | Art 13, 14, 15, 19 (P2) |
| Art 4(12) 'personal data breach' | `Art 4(12) the incident is a personal data breach` | call | Art 33, 34 (P3) |
| Art 4(16) 'main establishment' | `Art 4(16)(a) ...`, `Art 4(16)(b) ...` | call | Chapter VI and VII (P6, P7) |
| Art 4(17) 'representative' | `Art 4(17) the person is a representative` | call | Art 27 (P3) |
| Art 4(18) 'enterprise', Art 4(19) 'group of undertakings', Art 4(20) 'binding corporate rules' | the three functions | call | Art 47 (P5), Art 83 (P9) |
| Art 4(21) 'supervisory authority', Art 4(22) 'concerned' | the two functions | call | Chapter VI, VII (P6, P7) |
| Art 4(23) 'cross-border processing', Art 4(24) 'relevant and reasoned objection' | the two functions | call | Chapter VII (P7) |
| Art 4(26) 'international organisation' | `Art 4(26) the body is an international organisation` | call | Chapter V (P5) |
| Art 2(3), Art 2(4), Art 3 | `Art 3 this Regulation applies to the processing of personal data` (section 4) | a part that must say "this Regulation applies" takes `Art 3 this Regulation applies to the processing of personal data` as a plain input of type MAYBE BOOLEAN; a part that must say "where Article 3(2) applies" takes `Art 3(2) the territorial limb: ...` (MAYBE BOOLEAN) | Art 27 ("Where Article 3(2) applies"; P3, not checked) |
| Art 4 lead-in | `Art 4 lead-in the definitions of Article 4 apply to the term` | call; `NOTHING` for a use outside this Regulation | any |

### 5.2 Seams K2 TAKES (the asking side; each is a plain input)

| asking provision of K2 | answering provision | input (name, type) |
| --- | --- | --- |
| Art 3 combined | Art 2(1) and (2) (P1) | `Art 2(1) and (2) the processing is within the material scope of this Regulation`, MAYBE BOOLEAN: the name is the one PLAN.md sections 3.3 and 4.1 give; when K2 was written P1's module `P1-art-2.l4` was not in the builder's folder; in this row it is, and the name matches `P1-art-2.l4` exactly (checked 2026-11-26) |
| Art 4(17) | Art 27 (P3) | `the person is designated by the controller or processor in writing pursuant to Article 27` BOOLEAN |
| Art 4(21) | Art 51 (P6) | `the body is established pursuant to Article 51` BOOLEAN |
| Art 2(3) second sentence | Art 98 (P10) | `the act has been adapted to the principles and rules of this Regulation in accordance with Article 98` BOOLEAN |
| Art 4(25) | Directive (EU) 2015/1535, not among the sources | `the service is a service as defined in point (b) of Article 1(1) of Directive (EU) 2015/1535` BOOLEAN |
| Art 2(3) first sentence | Regulation (EC) No 45/2001, not among the sources | `the processing is by the Union institutions, bodies, offices or agencies` BOOLEAN (the instrument itself is not encoded) |
| Art 2(4) | Directive 2000/31/EC, not among the sources | `the matter is the application of Directive 2000/31/EC` BOOLEAN |
| Art 4(9), 4(22), 4(23) | "Union or Member State law", "inquiry", "complaint lodged", "Member State" | plain BOOLEANs named in section 3.2 |

## 6 Traps

Loud means the binary or the gate stops with an error; silent means the answer is wrong and nothing is reported.

- **Silent (re-measured on 1.6.112).** `#EVAL NOT FALSE OR TRUE` answers FALSE and `#EVAL NOT TRUE AND FALSE` answers TRUE: a one-line `NOT a OR b` reads as `NOT (a OR b)`.
  Every `NOT` in K2's files is parenthesised.
- **Silent.** `Art 2(3) this Regulation applies to the processing, where it is by the Union institutions, bodies, offices or agencies` answers `JUST FALSE` for processing by those bodies, and the combined `Art 3 ...` answers `JUST FALSE` for them.
  The text says only "Regulation (EC) No 45/2001 applies"; the `JUST FALSE` is reading A of fork FK2-1, listed for a lawyer.
- **Silent.** `Art 3 this Regulation applies ...` answers `NOTHING`, not `JUST FALSE`, for a processing that meets none of the three limbs (fork FK3-1): a caller must never turn that `NOTHING` into "the Regulation does not apply".
  The limb function `Art 3(2) ...` answers `JUST FALSE` when its own "where" gate fails; that is the limb's answer and does not make the combined answer false.
- **Silent.** Arguments the text declares irrelevant are kept so the clause has a test and are NOT read: `the body is a third party` (Art 4(9), "whether a third party or not"), `the data result from an analysis of a biological sample ...` (Art 4(13), "in particular"), `the data are facial images or dactyloscopic data` (Art 4(14), "such as"), `the processing takes place in the Union` (Art 3(1), "regardless"), `a payment of the data subject is required` (Art 3(2)(a), "irrespective").
  `the personal aspects that the personal data are used to evaluate` (Art 4(4)) is read only for whether it is empty.
- **Silent.** `Art 4(13) to (15) the categories ...` answers `JUST EMPTY` only when all three definitions are `JUST FALSE`, and that says nothing about the five categories of Art 9(1) that Art 4 does not define; it answers `NOTHING` whenever any of the three answers is `NOTHING`, so a caller that has not answered all three gets no list (the first build gave an incomplete list in that case; fixed after review R3).
- **Silent.** The `Kind of person or body` a caller states is taken as stated: a public authority that is also a legal person can be stated either way, and Art 4(17) (natural or legal person only) and Art 4(21) (public authority only) answer `JUST FALSE` for the kind not named.
- **Silent.** `#TRACE` results are not counted by `check.sh`; the one regulative rule of K2 (Art 4(9)) has no time limit and no consequence stated, so its traces end FULFILLED or standing, and none can breach.
- **Silent, environment.** `l4 run` prints `Warning | [Import Resolution] Multiple differing copies of module prelude (and daydate)` on this machine (an older copy is in the XDG data directory); `check.sh` does not count it.
- **Loud.** `MAYBE LIST OF X` is a parse error (`unexpected LIST`); write `MAYBE (LIST OF X)`.
- **Loud.** The main prelude has no `head`; use `at list 0` (0-based).
- **Loud, fixed by naming.** A name defined in two imported modules cannot be used; the labels of section 2 prevent it.
- **Loud (the gate).** `srcrefs.py` refuses a quote line that has no text (a line that is only `);`); quote the lines of point (25) as `src:70-71`.

## 7 The seat layer

Seats of K2: a data subject `[subject]` (24 questions) and a controller `[controller]` (33 questions), in the form of PLAN.md section 6.
A processor has no K2 question; there is NEVER a seat for a supervisory authority (Art 4(21), (22) and (24) are asked about, from the person's seat, as questions of identification: is this body a supervisory authority, is it concerned).
Shared inputs that K2 asks, with the same name and type as P1 where P1 asks them: none of P1's shared inputs is asked by K2 except the one it takes (`Art 2(1) and (2) the processing is within the material scope of this Regulation`, asked as `K2 subject answer` or `K2 controller answer`, yes, no or not sure).
Seat helper types: `K2 subject answer`, `K2 controller answer` (yes, no, not sure) with `K2 subject answer as a yes or no` and `K2 controller answer as a yes or no`.
A later part writes `P2 subject ...`, `P2 controller ...`.

## 8 What K2 did not see

Every provision outside lines 12-35, 36-73 and 1076-1081, and every recital.
The exact spelling of P1's functions (only PLAN.md and NOTES.md): the seam name in section 5.2 is PLAN.md's, not read from P1's code when K2 was written (in this row it matches `P1-art-2.l4`, checked 2026-11-26).
