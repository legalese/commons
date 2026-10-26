# FRAGMENT-G4: Articles 11 and 12 of the Charities (Jersey) Law 2014 (group G4)

Written by ENCODER G4 on 2026-10-26 for the integrator.
Status: draft; no domain expert has read it against the Law (`not_reviewed`).
Verified on the fleet's binary (sha256 `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`) by the check script reproduced in section 11; its last line, when this file was generated, was `check.sh (G4): GREEN`.
Nothing in this file was committed, pushed or sent.

## 0. What is here

The modules, all in `DEPOSIT`, all with the prefix `g4-`:

| module | holds | lines |
| --- | --- | --- |
| `g4-interpretation` | the twelve forks as enumerations and the one record `Interpretation of Articles 11 and 12` (DECLAREs only) | 174 |
| `g4-nouns` | the group-local nouns: the application and its sub-records, the findings, the duty enumeration, the acts of Articles 11 and 12, the records of names and opinions (DECLAREs only) | 278 |
| `g4-art11-application` | Article 11(1) to (3), (8), (10), (11): the right to apply, what the application must include, the periods, the powers of the States and the Minister, the pass-through to the JFSC | 562 |
| `g4-art11-decision` | Article 11(4) to (7) and (9): the six matters, the duty to register and to refuse against the bars, the guidance, the further grounds, the certificates | 637 |
| `g4-art12-name` | Article 12: undesirable names, the registered name and number, changes and alternatives, the prohibition on other names | 359 |
| `g4-tests-fixtures` | named cases shared by the tests (no assertion) | 921 |
| `g4-tests-art11-application` | tests of Article 11(1) to (3), (8), (10), (11) | 350 |
| `g4-tests-art11-decision` | tests of Article 11(4) to (7) and (9) | 345 |
| `g4-tests-art12-name` | tests of Article 12 | 267 |
| `g4-tests-forks` | the discriminating case of each fork on every reading | 351 |
| `g4-tests-red` | assertions meant to fail, counted (14) | 59 |

`PLAN.md` section (b) proposed two modules, `g4-art11-application` and `g4-art12-name`.
Three things made me change that, and each is recorded in the coverage table's module column.
First, Article 11 is 55 lines of the Law's text with 55 coverage rows (Article 12: 18), and one file of its rules was too long to review against the source section by section, so the decision (paragraphs (4) to (7) and (9)) is in `g4-art11-decision`.
Second, the record `Interpretation of Articles 11 and 12` is read by all three rule modules, and modules may import only their own group, so it lives in a module of its own, `g4-interpretation`.
Third, the nouns are written first and once, as the skill asks (`g4-nouns`).
The names of rules that PLAN section (b) proposed are kept as given wherever the text allowed.

How the modules were written.
Every quotation of the Law in the modules is produced by `srcrefs.py quote` from a template, so none was retyped.
Every rule carries an `@ref` with `src:` locators where it rests on particular lines, and `srcrefs.py check --refs` over every module reports 0 problems (section 11).
The tests' expected values were written from the text of the Law and from the words of each reading before the modules were run, and no expected value was ever edited to match the code.
When each test module first compiled and ran, every assertion written from the text agreed with the encoding.
One later run was red: after Article 12(7) was gated on Article 1's definition of a registered charity, `g4-tests-art12-name.l4` showed 1 failed assertion and 4 traces that changed, because a test fixture (a `Registered charity` record) had an entity with the standing of an applicant; the fixture was corrected to an entity in the general section, and no expectation was changed.
A positive control was run as well: 28 single-point mutations of the rule modules (a boundary moved, a connective swapped, a modality changed, a case dropped) were applied one at a time, and every one made some assertion or trace fail (section 12).

What is NOT here.
There is no `encoding.json`, no `NOTES.md` and no `check.sh` of the deposit: those are the integrator's.
No module imports another group's module; every fact another group decides is a `GIVEN` under the standard name of PLAN section (c) (section 6).

## 1. Coverage

One row per provision of the scope, in the Law's numbering, 73 rows.
Disposition counts: encoded 73, inert 0, refused 0, out-of-scope 0, deferred 0.
No disposition was changed from the PLAN.
A row that is `encoded` and carries a named refusal says so in the notes: the refusal is returned in the position of the answer (never stored), is named for what is not covered, and is tested with `#ASSERT REFUSED ... BECAUSE`.
Where the PLAN named a module, the module column here is the module that holds the rule; the PLAN's single Article 11 module is split as section 0 says.

| id | provision | disposition | module | rule | notes |
| --- | --- | --- | --- | --- | --- |
| 11 | Article 11 | encoded | `g4-art11-application`, `g4-art11-decision` | `Art 11(1) the entity may apply`; `Art 11 what the Commissioner must do on the application` |  |
| 11(1) | Article 11(1) | encoded | `g4-art11-application` | `Art 11(1) the entity may apply`; `the entity applies` |  |
| 11(2) | Article 11(2) | encoded | `g4-art11-application`, `g4-nouns` | `Art 11(2) the applicant must provide what Article 11(2) requires`; `Art 11(2) the application includes what Article 11(2) requires`; `Art 11(2) the provision applies to the applicant`; `Application for registration` |  |
| 11(2)(a) | Article 11(2)(a) | encoded | `g4-art11-application`, `g4-nouns` | `Art 11(2)(a) the information on a matter is provided`; `Information on a matter under Article 11(2)(a)`; `Particulars under Article 11(2)(a)` |  |
| 11(2)(a)(i) | Article 11(2)(a)(i) | encoded | `g4-art11-application` | `Art 11(2)(a)(i) the requirement is met` |  |
| 11(2)(a)(ii) | Article 11(2)(a)(ii) | encoded | `g4-art11-application` | `Art 11(2)(a)(ii) the requirement is met` |  |
| 11(2)(a)(iii) | Article 11(2)(a)(iii) | encoded | `g4-art11-application` | `Art 11(2)(a)(iii) the requirement is met` |  |
| 11(2)(b) | Article 11(2)(b) | encoded | `g4-art11-application`, `g4-nouns` | `Art 11(2)(b) the requirement is met`; `Documents under Article 11(2)(b) to (d)` |  |
| 11(2)(c) | Article 11(2)(c) | encoded | `g4-art11-application` | `Art 11(2)(c) the requirement is met` |  |
| 11(2)(d) | Article 11(2)(d) | encoded | `g4-art11-application` | `Art 11(2)(d) the requirement is met` |  |
| 11(2)(e) | Article 11(2)(e) | encoded | `g4-nouns`, `g4-art11-application` | `Financial details under Article 11(2)(e)`; `Art 11(2)(e)(i) the requirement is met` |  |
| 11(2)(e)(i) | Article 11(2)(e)(i) | encoded | `g4-art11-application` | `Art 11(2)(e)(i) the requirement is met` |  |
| 11(2)(e)(ii) | Article 11(2)(e)(ii) | encoded | `g4-art11-application` | `Art 11(2)(e)(ii) the requirement to disclose payments is met`; `Art 11(2)(e)(ii) the requirement of a draft statement is met`; `Art 11(2)(e)(ii) the twelve months preceding the application`; `Art 11(2)(e)(ii) the payment to a governor is within the period`; `Art 11(2)(e)(ii) the payment is one the paragraph reaches`; `Art 11(2)(e)(ii) the payment is among the details disclosed` | periods P5 and P6, forks F4.1, F4.2, F4.6, F4.11; trap T28 (two requirements in one item); IP29 is read of the applicant as the registered charity it would become |
| 11(2)(e)(iii) | Article 11(2)(e)(iii) | encoded | `g4-art11-application` | `Art 11(2)(e)(iii) the requirement is met` | the content of the Non-Profit Organizations (Jersey) Law 2008 is not in the sources: whether it requires more is an input |
| 11(2)(e)(iv) | Article 11(2)(e)(iv) | encoded | `g4-art11-application` | `Art 11(2)(e)(iv) the requirement is met` | an Order's content is an input; no Order is among the sources |
| 11(2)(f) | Article 11(2)(f) | encoded | `g4-nouns`, `g4-art11-application` | `Other requirements under Article 11(2)(f)`; `Art 11(2)(f)(i) the requirement is met` |  |
| 11(2)(f)(i) | Article 11(2)(f)(i) | encoded | `g4-art11-application` | `Art 11(2)(f)(i) the requirement is met` | Regulations under 11(3) are not among the sources: whether they require more is an input |
| 11(2)(f)(ii) | Article 11(2)(f)(ii) | encoded | `g4-art11-application` | `Art 11(2)(f)(ii) the requirement is met` |  |
| 11(3) | Article 11(3) | encoded | `g4-art11-application` | `Art 11(3)(a) the States may prescribe other information, documents or evidence`; `Art 11(3)(b) the States may make further provision as to the procedure` | powers of the States; the Regulations are not in the sources |
| 11(3)(a) | Article 11(3)(a) | encoded | `g4-art11-application` | `Art 11(3)(a) the States may prescribe other information, documents or evidence` |  |
| 11(3)(b) | Article 11(3)(b) | encoded | `g4-art11-application` | `Art 11(3)(b) the States may make further provision as to the procedure` |  |
| 11(4) | Article 11(4) | encoded | `g4-art11-decision` | `Art 11(4) the Commissioner must register the applicant`; `Art 11 the duty of the Commissioner on the application`; `Art 11(4) the applicant has complied with Article 11(2), the Regulations and Article 19(5)`; `Art 11(4) the six matters are found`; `Art 11 what the Commissioner must do on the application` | trap T10; forks F4.3, F4.4; the six matters are the Commissioner's findings (section 10, modelling decision 1) |
| 11(4)(a) | Article 11(4)(a) | encoded | `g4-art11-decision` | `Art 11(4)(a) the applicant meets the charity test, or will do so on registration` |  |
| 11(4)(b) | Article 11(4)(b) | encoded | `g4-art11-decision` | `Art 11(4)(b) the constitution of the applicant is a written document` |  |
| 11(4)(c) | Article 11(4)(c) | encoded | `g4-art11-decision` | `Art 11(4)(c) the requirement is met` | standard fact IP15, exported |
| 11(4)(c)(i) | Article 11(4)(c)(i) | encoded | `g4-art11-decision` | `Art 11(4)(c)(i) the applicant is a Jersey entity` |  |
| 11(4)(c)(ii) | Article 11(4)(c)(ii) | encoded | `g4-art11-decision` | `Art 11(4)(c)(ii) the applicant carries out an activity that is substantial` |  |
| 11(4)(d) | Article 11(4)(d) | encoded | `g4-art11-decision` | `Art 11(4)(d) the requirement is met` | standard fact IP16, exported |
| 11(4)(e) | Article 11(4)(e) | encoded | `g4-art11-decision` | `Art 11(4)(e) the name of the applicant is not undesirable under Article 12` | consumes IP18, does not call Art 12(1) (PLAN: G4 does not call the six matters) |
| 11(4)(f) | Article 11(4)(f) | encoded | `g4-art11-decision` | `Art 11(4)(f) no other ground for refusal prescribed under Article 11(7) applies or should be applied` | the prescribed grounds are inputs; fork F4.12 reads 'applies' of a ground of mandatory refusal and 'should be applied' of a ground of discretionary refusal |
| 11(5) | Article 11(5) | encoded | `g4-art11-decision` | `Art 11(5) the Commissioner must refuse to register the applicant` | fork F4.3 (reading C is Article 11(5) on its own words) |
| 11(6) | Article 11(6) | encoded | `g4-art11-decision` | `Art 11(6) the guidance from consultation to the States` |  |
| 11(6)(a) | Article 11(6)(a) | encoded | `g4-art11-decision` | `Art 11(6)(a) the Commissioner must publish and maintain guidance on whether an activity is substantial` |  |
| 11(6)(b) | Article 11(6)(b) | encoded | `g4-art11-decision` | `Art 11(6)(b) before issuing or amending the guidance the Commissioner must consult and publish a report`; `Art 11(6)(b) the consultation and the report are as Article 5(6) requires`; `Art 11(6)(b) the Commissioner must provide the Minister with a copy of the guidance and the report`; `Art 11(6)(b) the copy was provided to the Minister within a reasonable time`; `Art 11(6)(b) the Minister must lay a copy of the guidance and the report before the States`; `Art 11(6)(b) the Minister laid the copy before the States as soon as practicable` | Articles 5(6) to (8) restated for this guidance because a group module may not call G2's; fork F4.10, set together with F2.4 |
| 11(6)(c) | Article 11(6)(c) | encoded | `g4-art11-decision` | `Art 11(6)(c) the Commissioner must have regard to the guidance in determining whether an activity is substantial` |  |
| 11(6)(d) | Article 11(6)(d) | encoded | `g4-art11-decision` | `Art 11(6)(d) the party must have regard to the guidance`; `Art 11(6)(d) the paragraph binds the party` |  |
| 11(7) | Article 11(7) | encoded | `g4-art11-decision` | `Art 11(7) the States may prescribe further grounds on which an application must or may be refused` | power of the States; grounds are inputs |
| 11(7)(a) | Article 11(7)(a) | encoded | `g4-art11-decision` | `Art 11(7)(a) the entity has only one governor who does not carry on a prescribed description of business as a governor` | an example the Regulations may include, encoded as the test they would apply |
| 11(7)(b) | Article 11(7)(b) | encoded | `g4-art11-decision` | `Art 11(7)(b) a number or proportion of the governors are related to each other in prescribed ways` | an example the Regulations may include; the number, proportion and ways are in the Regulations, so the test is an input |
| 11(8) | Article 11(8) | encoded | `g4-art11-application` | `Art 11(8)(a)(i) the Minister may provide for the period within which the Commissioner must decide an application`; `Art 11(8)(b)(i) the Minister may provide that a provision of Article 11(2) does not apply to a prescribed description of applicant` |  |
| 11(8)(a) | Article 11(8)(a) | encoded | `g4-art11-application` | `Art 11(8)(a)(i) the Minister may provide for the period within which the Commissioner must decide an application`; `Art 11(8)(a)(ii) the Minister may provide for the notification of decisions and of reasons for refusal` |  |
| 11(8)(a)(i) | Article 11(8)(a)(i) | encoded | `g4-art11-application` | `Art 11(8)(a)(i) the Minister may provide for the period within which the Commissioner must decide an application`; `Art 11(8)(a)(i) the last day for the Commissioner's decision`; `Art 11(8)(a)(i) the Commissioner's decision is within the period`; `Art 11 the date of the application` | periods P6 and P7, forks F4.2, F4.9; the length is a MAYBE NUMBER and NOTHING returns a named refusal; no consequence of lateness is encoded because the Law states none |
| 11(8)(a)(ii) | Article 11(8)(a)(ii) | encoded | `g4-art11-application` | `Art 11(8)(a)(ii) the Minister may provide for the notification of decisions and of reasons for refusal` |  |
| 11(8)(b) | Article 11(8)(b) | encoded | `g4-art11-application` | `Art 11(8)(b) the Minister has consulted as the paragraph requires`; `Art 11(2) the provision applies to the applicant` | the consultation is a computable precondition; the effect (a provision disapplied for this applicant) is read by every limb of 11(2) |
| 11(8)(b)(i) | Article 11(8)(b)(i) | encoded | `g4-art11-application` | `Art 11(8)(b)(i) the Minister may provide that a provision of Article 11(2) does not apply to a prescribed description of applicant` |  |
| 11(8)(b)(ii) | Article 11(8)(b)(ii) | encoded | `g4-art11-application` | `Art 11(8)(b)(ii) the Minister may provide that a provision of Article 11(2) applies to a prescribed description of applicant subject to a modification` |  |
| 11(9) | Article 11(9) | encoded | `g4-art11-decision` | `Art 11(9)(a) the Commissioner must issue a certificate of registration`; `Art 11(9)(b) the Commissioner must issue a further certificate for a new or alternative registered name` | no time limit is stated, so no WITHIN |
| 11(9)(a) | Article 11(9)(a) | encoded | `g4-art11-decision` | `Art 11(9)(a) the Commissioner must issue a certificate of registration` |  |
| 11(9)(b) | Article 11(9)(b) | encoded | `g4-art11-decision` | `Art 11(9)(b) the Commissioner must issue a further certificate for a new or alternative registered name` |  |
| 11(10) | Article 11(10) | encoded | `g4-art11-application` | `Art 11(10) the applicant must provide the additional information and request to be registered under that Law` | whether the applicant is 'required' under that Law is an input |
| 11(10)(a) | Article 11(10)(a) | encoded | `g4-art11-application` | `Art 11(10)(a) the applicant must provide the additional information with the application` |  |
| 11(10)(b) | Article 11(10)(b) | encoded | `g4-art11-application` | `Art 11(10)(b) the applicant must request to be registered under that Law` |  |
| 11(11) | Article 11(11) | encoded | `g4-art11-application` | `Art 11(11)(a) the Commissioner must pass the request to the JFSC`; `Art 11(11)(b) the JFSC must treat the request as an application for registration under that Law` |  |
| 11(11)(a) | Article 11(11)(a) | encoded | `g4-art11-application` | `Art 11(11)(a) the Commissioner must pass the request to the JFSC` |  |
| 11(11)(b) | Article 11(11)(b) | encoded | `g4-art11-application` | `Art 11(11)(b) the JFSC must treat the request as an application for registration under that Law` | a duty of another body (the JFSC) under a Law that is not in the sources: only the duty is encoded |
| 12 | Article 12 | encoded | `g4-art12-name` | `Art 12(1) the name is undesirable`; `Art 12(7) a registered charity must not use a name other than a registered or related name` |  |
| 12(1) | Article 12(1) | encoded | `g4-art12-name` | `Art 12(1) the name is undesirable` | standard fact IP18, exported |
| 12(1)(a) | Article 12(1)(a) | encoded | `g4-art12-name` | `Art 12(1)(a) the name is the same as, or too similar to, the name of any other registered charity`; `Art 12(1)(a) the entry is the name of another registered charity` | forks F4.5, F4.7; the Commissioner's opinion is given as the entries of the register that he or she thinks the same or too similar |
| 12(1)(b) | Article 12(1)(b) | encoded | `g4-art12-name` | `Art 12(1)(b) the name is likely to mislead the public as to the purpose, activities or identity of the entity` |  |
| 12(1)(c) | Article 12(1)(c) | encoded | `g4-art12-name` | `Art 12(1)(c) the name gives the impression that the entity is connected to a person to which it is not connected` |  |
| 12(1)(d) | Article 12(1)(d) | encoded | `g4-art12-name` | `Art 12(1)(d) the name is offensive` |  |
| 12(2) | Article 12(2) | encoded | `g4-art12-name` | `Art 12(2) the Commissioner must enter the registered name and allocate and enter a number` | no time limit is stated; the number is whatever the Commissioner allocates |
| 12(2)(a) | Article 12(2)(a) | encoded | `g4-art12-name` | `Art 12(2)(a) the Commissioner must enter the name of the entity in the register as the registered name` |  |
| 12(2)(b) | Article 12(2)(b) | encoded | `g4-art12-name` | `Art 12(2)(b) the Commissioner must allocate a registration number and enter it in the register` |  |
| 12(3) | Article 12(3) | encoded | `g4-art12-name` | `Art 12(3) a registered charity may apply for permission to change its registered name or to add an alternative registered name` |  |
| 12(4) | Article 12(4) | encoded | `g4-art12-name` | `Art 12(4) the Commissioner must refuse permission to change or add a name`; `Art 12(4) what the Commissioner must do on the application for permission` | the Law states no duty to grant when no ground applies, so that case answers NOTHING in the decision function |
| 12(5) | Article 12(5) | encoded | `g4-art12-name` | `Art 12(5) the Commissioner must enter the new or alternative registered name` |  |
| 12(6) | Article 12(6) | encoded | `g4-art12-name` | `Art 12(6) the Commissioner may require the charity to apply to change its registered name`; `Art 12(6) the decision of the Commissioner on whether to require the charity to apply` | appealable (33(2)(c)); the decision function maps 'requires' to 'does what was proposed' |
| 12(7) | Article 12(7) | encoded | `g4-art12-name` | `Art 12(7) a registered charity must not use a name other than a registered or related name`; `Art 12(7) the name used is permitted`; `Art 12(7) the entity is a registered charity` | a prohibition with no penalty; its only consequence is through misconduct (IP13); fork F4.8; binds a registered charity only (Article 1) |
| 12(7)(a) | Article 12(7)(a) | encoded | `g4-art12-name` | `Art 12(7)(a) the name used is its registered name or one of its registered names` |  |
| 12(7)(b) | Article 12(7)(b) | encoded | `g4-art12-name` | `Art 12(7)(b) the name used is related to a registered name and is not undesirable in its context` |  |
| 12(7)(b)(i) | Article 12(7)(b)(i) | encoded | `g4-art12-name` | `Art 12(7)(b) the name used is related to a registered name and is not undesirable in its context` | 'related' is not defined by the Law: an input |
| 12(7)(b)(ii) | Article 12(7)(b)(ii) | encoded | `g4-art12-name` | `Art 12(7)(b) the name used is related to a registered name and is not undesirable in its context` | the opinion is of the name in the context in which it is used; see section 7, finding C3 |

## 2. The fork register

The record is `Interpretation of Articles 11 and 12` (module `g4-interpretation`).
It has twelve fields, one per fork point, each an enumeration with one constructor per reading and each `TYPICALLY` the reading taken.
Register entries map 1:1 to the fields: the field name is the entry's second line.
Every public decision that depends on a fork takes the record as an ordinary `GIVEN` named `interp` and dispatches by `CONSIDER` to one function per reading; those functions are named `F4.n reading X: ...` and are the ones the fork tests call directly.
F4.1 to F4.5 are the survey's forks (F4.3 gained a third reading); F4.6 to F4.12 are new, found while encoding.

A note on the record at the boundary.
`TYPICALLY` fills in only what a caller leaves out of a record that the caller supplies; it does not make the whole record optional.
Measured with `l4 batch` on this binary: a row that omits `interp` altogether is an error (`Missing required field 'interp'`), a row with `"interp": {}` is an error (`the value is not known: supply a value`), and a row with one field of `interp` set takes the defaults of the other eleven and lists the ones it used under `presumed`.
So a caller who wants every default must send one field of `interp` explicitly.
The headline decision was also run end to end at that boundary on a base case (a Jersey company that complies, the six matters found, no bar): `l4 batch ... -e "Art 11 the duty of the Commissioner on the application"` answered `the Commissioner must register the applicant` and listed under `presumed` exactly the two forks that the answer used, `interp.how the duty to register meets the bars on granting the application` and `interp.what an application that does not comply leads to`.
An exported name that contains an apostrophe (`Art 11(8)(a)(i) the last day for the Commissioner's decision`) works as an entry point, and a `null` length answers the named refusal.
An exported DEONTIC rule answers `<obligation>` or `FULFILLED` at that boundary.

### Text quoted for the forks

The provisions the readings turn on, quoted mechanically:

> -- src:310 | (ii) any payment made to any governor of the entity in the 12 months preceding the application, and if an Order under Article 13(9)(b) applies to the registered charity, a draft of the proposed statement under that Order,
> -- src:319 | (4) If the applicant complies with paragraph (2), with any Regulations under paragraph (3), and with Article 19(5), the Commissioner must register the applicant as a charity if satisfied that –
> -- src:327 | (f) no other ground for refusal, prescribed under paragraph (7), applies or should be applied.
> -- src:328 | (5) If not so satisfied, the Commissioner must refuse to register the applicant.
> -- src:334 | (7) The States may by Regulations prescribe further grounds on which an application must or may be refused, and those grounds may, without limitation, include –
> -- src:339 | (i) the period within which the Commissioner must make a decision on an application,
> -- src:355 | (a) is the same as, or too similar to, the name of any other registered charity;
> -- src:367 | (a) its registered name or one of its registered names; or
> -- src:496 | (6) An application for registration is not complete if the entity has not complied with paragraph (5).
> -- src:502 | (c) must not, in the case of an application for registration, grant that application until the issue has been determined and any resulting order or notice complied with;
> -- src:517 | (c) an order that the entity must not be registered as a charity;

> -- src:164 | (7) Within a reasonable time after issuing or amending guidance the Commissioner must provide to the Minister a copy of the issued or amended guidance and the report published under paragraph (6)(b).
> -- src:165 | (8) The Minister must lay a copy of the guidance and report so provided before the States as soon as practicable after the Minister receives the guidance and report.
> -- src:331 | (b) Articles 5(6) to (8) apply to that guidance as they apply to guidance under Article 5(4);
> -- src:34 | “registered charity” means an entity entered for the time being in the general section or the restricted section of the register;

### F4.1: the 12 months preceding the application

- **Provision:** Article 11(2)(e)(ii) (src:310); period P5, a backward-looking period.
- **Field:** `how the twelve months preceding the application are counted` of type `How the twelve months preceding an application are counted`.
- **Reading A (taken):** `the twelve months ending on the day before the application`. "Preceding" excludes the day of the application itself; a year back from the date of the application, ending the day before it. Window for an application on 15 March 2026: 15 March 2025 to 14 March 2026, both inclusive.
- **Reading B:** `the twelve months ending on the day of the application`. A payment made earlier on the day of the application precedes the application; the window ends on that day and so starts the day after the anniversary. Window: 16 March 2025 to 15 March 2026.
- **Reading C:** `the twelve whole calendar months before the month of the application`. "12 months" as calendar months. Window: 1 March 2025 to 28 February 2026.
- **Why A:** it is the plainest sense of "preceding": nothing on the day of the application is before the application, and the window is the year that ends as the application begins.
- **Discriminating case:** application lodged and complete on 15 March 2026: a payment on 15 March 2025 is in A, out of B, in C; on 15 March 2026 out of A, in B, out of C; on 1 March 2026 in A and B, out of C; on 14 March 2025 out of A and B, in C.
- **Tests:** `g4-tests-forks.l4` section F4.1 (the ten dates against the three windows, 30 assertions, and the windows themselves); `g4-tests-art11-application.l4` (the default window and the duty to disclose); `g4-tests-red.l4` (two assertions of the other readings' answers under the default).

### F4.2: the date of "the application"

- **Provision:** Articles 11(2)(e)(ii), 11(8)(a)(i), 19(6) (src:310, src:339, src:496); period P6, the commencement of a period; also the "time of the application" of 11(2)(a).
- **Field:** `which day is the date of the application` of type `Which day is the date of an application`.
- **Reading A (taken):** `the day the application is lodged`. Article 19(6) says that "An application for registration is not complete if the entity has not complied with paragraph (5)", which presupposes that there is an application before it is complete.
- **Reading B:** `the day the application becomes complete`. "Complete" in the sense of Article 19(6). That sense is narrower than "includes everything Article 11(2) requires": an application can be complete under 19(6) and still lack the copy of the constitution.
- **Why A:** the Law speaks of "the application" as existing while it is not yet complete; a date that does not exist until completion would leave the first stretch of the life of an application without a date.
- **Discriminating case:** lodged 1 March 2026, complete 20 March 2026, a payment on 10 March 2026 not disclosed: under A the window is 1 March 2025 to 28 February 2026 and the payment is outside it (requirement met); under B the window is 20 March 2025 to 19 March 2026 and the payment is inside (requirement not met); an Order's 30 days end on 31 March (A) or 19 April 2026 (B); an application not yet complete has the lodging date under A and no date under B (a named refusal).
- **Tests:** `g4-tests-forks.l4` section F4.2; `g4-tests-red.l4` (one assertion).
- **One anchor for two periods.** PLAN period P6 makes this one fork serve the twelve months (P5) and the period an Order may set for the Commissioner's decision (P7). The survey's handling note for trap T10 said that the decision period "does not run until it is complete", which is reading B, while the survey takes reading A. I kept ONE anchor fork, as P6 says, and dropped that claim: under F4.2 reading A together with F4.3 reading A, an Order's period would already be running from the day of lodging while the Commissioner has no duty to decide a non-complying application. The tension is asserted in `g4-tests-forks.l4` (the last day is computed, and the duty is `no duty to register or to refuse arises`). The integrator should set F4.2 and F4.3 together.

### F4.3: an application that does not comply

- **Provision:** Articles 11(4), 11(5), 19(6) (src:319, src:328, src:496); trap T10.
- **Field:** `what an application that does not comply leads to` of type `What an application that does not comply leads to`.
- **Reading A (taken):** `no duty to register or to refuse arises while the application does not comply`. Article 11(4) begins "If the applicant complies with paragraph (2), with any Regulations under paragraph (3), and with Article 19(5)", and Article 11(5) is "If not so satisfied", the satisfaction being that of Article 11(4); a non-complying application is outside both, and Article 19(6) says only that it is "not complete".
- **Reading B:** `the Commissioner must refuse an application that does not comply`. Non-compliance is itself a failure to be satisfied, so Article 11(5) applies.
- **Reading C:** `the duty to refuse depends on the six matters alone`. Article 11(5) read on its own words: "If not so satisfied, the Commissioner must refuse" does not repeat the condition of compliance, so the duty to refuse arises whenever the six matters are not found, complying or not; the duty to register still needs compliance.
- **Why A:** it is the survey's reading and the most natural: the Commissioner determines an application that is complete, and the Commissioner may ask for what is missing (Article 11(2)(f)(ii)); the application remains pending.
- **Discriminating case:** everything in Article 11(4)(a) to (f) is found but the copy of the constitution (Article 11(2)(b)) is missing: A no duty, B refuse, C no duty. Where a matter is also not found (the name is undesirable): A no duty, B refuse, C refuse. Reading C is new: it separates from A only in the second case.
- **Tests:** `g4-tests-forks.l4` section F4.3 (the two cases on every reading, and the four combinations of (complies, found) on each reading function); `g4-tests-art11-decision.l4` (each way of not complying, on the default); `g4-tests-red.l4` (one assertion).

### F4.4: the duty to register against the bars on granting

- **Provision:** Articles 11(4), 19(9)(c), 20(1)(c) (src:319, src:502, src:517); trap T10.
- **Field:** `how the duty to register meets the bars on granting the application` of type `How the duty to register meets the bars on granting the application`.
- **Reading A (taken):** `a bar on granting the application displaces the duty to register`. Article 19(9)(c): the Commissioner "must not, in the case of an application for registration, grant that application until the issue has been determined and any resulting order or notice complied with"; Article 20(1)(c): the court may order "that the entity must not be registered as a charity". Neither is among the six matters, and each is addressed to the very act of granting, or registering, this applicant. A court order is not temporary, so it comes first when both apply.
- **Reading B:** `the duty to register prevails once its six matters hold`. Article 11(4) says the Commissioner "must register" if satisfied of six matters, and lists no bar.
- **Reading C:** `the duty to register and the bars conflict and the model refuses`. The provisions conflict (a MUST register and a MUST NOT grant) and the Law does not say which prevails.
- **Why A:** a prohibition addressed to the very act (granting this application) is more specific than the general duty, and a reading that binds the Commissioner at once to register and not to grant is the worst available; this is my reasoning, no text decides it.
- **Discriminating case:** a reported fitness issue is undetermined and the applicant otherwise complies and satisfies (a) to (f): A `must not yet grant`, B `must register`, C a named refusal; a court order that the entity must not be registered: A `must not register`, B `must register`, C a named refusal; both bars: A `must not register`.
- **Tests:** `g4-tests-forks.l4` section F4.4 (the cases on every reading, and each reading function over its inputs); `g4-tests-art11-decision.l4`; `g4-tests-red.l4` (one assertion).

### F4.5: is a formerly registered charity "another registered charity"

- **Provision:** Articles 12(1)(a), 12(4), 33(5)(b) (src:355); Article 1 "registered charity" (src:34).
- **Field:** `whether a formerly registered charity is another registered charity` of type `Whether a formerly registered charity is another registered charity`.
- **Reading A (taken):** `a formerly registered charity is not another registered charity`. Article 1 defines "registered charity" as "an entity entered for the time being in the general section or the restricted section", which excludes an entity in the historic section.
- **Reading B:** `a formerly registered charity is another registered charity`. The historic section is part of the public register (Article 10(3)(c)) and a name still entered there can mislead.
- **Why A:** the defined term governs unless the context otherwise requires, and nothing in Article 12(1)(a) requires otherwise.
- **Discriminating case:** a proposed name the Commissioner thinks the same as the registered name of a charity that has since been deregistered: A not undesirable, B undesirable.
- **Tests:** `g4-tests-forks.l4` section F4.5; `g4-tests-red.l4` (one assertion).

### F4.6: a year before 29 February

- **Provision:** Article 11(2)(e)(ii) (src:310); the month-end convention for a backward period.
- **Field:** `how a year is taken back from 29 February` of type `How a year is taken back from 29 February`.
- **Reading A (taken):** `a year before 29 February is 28 February`. The daydate library's `add years`, which falls back to the last day of the month as a spreadsheet's EDATE does.
- **Reading B:** `a year before 29 February is 1 March`. The lenient `Date` constructor, which rolls the day that does not exist forward.
- **Why A:** the Law gives no rule; clamping keeps the window within the twelve months, and it is what the library's documentation recommends for an anniversary.
- **Discriminating case:** application lodged and complete on 29 February 2028: the window (F4.1 reading A) starts on 28 February 2027 under A and on 1 March 2027 under B; a payment on 28 February 2027 is inside under A and outside under B. Under F4.1 reading B the start is 1 March 2027 (A) or 2 March 2027 (B). Reading C of F4.1 does not take a year back from a day, so it is unaffected.
- **Tests:** `g4-tests-forks.l4` section F4.6; `g4-tests-red.l4` (one assertion).

### F4.7: which names of another charity Article 12(1)(a) compares

- **Provision:** Article 12(1)(a) (src:355), with Articles 12(2)(a), 12(3), 12(5), 12(7)(a), 8(3)(l).
- **Field:** `which names of another registered charity Article 12(1)(a) compares` of type `Which names of another registered charity Article 12(1)(a) compares`.
- **Reading A (taken):** `its registered name and its alternative registered names`. Article 12(7)(a) speaks of "its registered name or one of its registered names", and Article 12(3) and (5) call the added name an "alternative registered name".
- **Reading B:** `its registered name only`. Article 12(2)(a) defines "the registered name" as the one name entered when the Commissioner registers the entity.
- **Reading C:** `every name entered for it in the register, previous names included`. Article 8(3)(l) keeps the previous registered names on the register.
- **Why A:** the name of a registered charity is any name it is entitled to use as its registered name; a previous name it has given up is not its name.
- **Discriminating case:** a proposed name the same as another charity's alternative registered name: undesirable under A and C, not under B; the same as one of its previous names: undesirable under C only.
- **Tests:** `g4-tests-forks.l4` section F4.7; `g4-tests-red.l4` (one assertion).

### F4.8: a previous registered name of the charity itself

- **Provision:** Article 12(7)(a) (src:367), with Article 8(3)(l).
- **Field:** `whether a previous registered name is still one of its registered names` of type `Whether a previous registered name is still one of the charity's registered names`.
- **Reading A (taken):** `a previous registered name is not one of its registered names`. "its registered name or one of its registered names" are the names registered now; a name given up is on the register only as a previous name (Article 8(3)(l)) and must pass sub-paragraph (b).
- **Reading B:** `a previous registered name is still one of its registered names`. It was a registered name and is still entered in the register.
- **Why A:** it is the reading under which a change of name has an effect: otherwise the old name stays usable for ever and Article 12(6) (requiring a charity to change a name) would achieve nothing.
- **Discriminating case:** a charity that changed its registered name from Hope Foundation to Hope Foundation Limited uses Hope Foundation, which is not related to a registered name in the sense of (b): A not permitted (using it breaches the prohibition), B permitted.
- **Tests:** `g4-tests-forks.l4` section F4.8 (including both traces); `g4-tests-red.l4` (one assertion).
- The previous registered names are an input of the record `Name used by a registered charity` because `Registered charity` in `domain.l4` has no field for them (nouns request 2).

### F4.9: counting the period for the Commissioner's decision

- **Provision:** Article 11(8)(a)(i) (src:339); period P7, a deadline set by Order.
- **Field:** `how the period for the Commissioner's decision is counted` of type `How the period for the Commissioner's decision is counted`.
- **Reading A (taken):** `the period starts the day after the date of the application`. The usual way of counting a period "from" an event: the day of the event is not in it (my reasoning, no text decides it). The last day is the date plus the length.
- **Reading B:** `the date of the application is the first day of the period`. A period "within" which a decision must be made includes the day of the application as its first day (my reasoning, no text decides it). The last day is one earlier.
- **Why A:** it is the counting the library's date arithmetic gives (`date PLUS n`), and the amending instruments count "7 days after it is made" the same way: made 5 April 2023, in force 12 April 2023 (R&O.28/2023); made 9 October 2025, in force 16 October 2025 (R&O.56/2025); made 25 September 2026, in force 2 October 2026 (R&O.102/2026), so the day of making is not counted.
- **Discriminating case:** an Order allows 30 days from 1 March 2026: the last day is 31 March (A) or 30 March (B); a decision on 31 March is in time under A and late under B.
- **Tests:** `g4-tests-forks.l4` section F4.9 (the last day, the boundary on both sides, a period of one day, a period across a leap February); `g4-tests-red.l4` (one assertion).
- The length is an input, `MAYBE NUMBER`: no Order is among the sources, and NOTHING returns the named refusal `no Order under Article 11(8)(a)(i) fixing the period for the Commissioner's decision is encoded in this model`, tested with `#ASSERT REFUSED ... BECAUSE`. The Law attaches no consequence to a late decision, so none is encoded.

### F4.10: reasonable time and as soon as practicable, for the guidance

- **Provision:** Article 11(6)(b) applying Articles 5(7) and 5(8) (src:331, src:164, src:165); periods of the kind "standard of promptness". Set together with F2.4 of group G2, which reads the same words in Articles 5(7) and 5(8).
- **Field:** `how reasonable time and as soon as practicable are read for the guidance` of type `How reasonable time and as soon as practicable are read for the guidance`.
- **Reading A (taken):** `as a determination the caller supplies`. "Within a reasonable time" and "as soon as practicable" are standards of judgement; no number is in the Law.
- **Reading B:** `as a number of days from the event`. A caller who wants a threshold supplies the number of days; the days between the event and the act are compared with it.
- **Why A:** a number would be invented; the extra input of reading B (a `MAYBE NUMBER`) exists on that reading only, and NOTHING there returns a named refusal.
- **Discriminating case:** guidance issued 1 January 2026, copy provided to the Minister on 1 March 2026 (59 days): under A the answer is whatever the caller says; under B with 30 days it is late, with 59 it is in time, with 58 late; the same for the Minister's laying (14 days: 14 in time, 13 late).
- **Tests:** `g4-tests-forks.l4` section F4.10; `g4-tests-art11-decision.l4`; `g4-tests-red.l4` (one assertion).
- The duties themselves carry no `WITHIN`, because the Law gives no number; the promptness is a separate predicate (`Art 11(6)(b) the copy was provided to the Minister within a reasonable time`, `Art 11(6)(b) the Minister laid the copy before the States as soon as practicable`).

### F4.11: the payee who is a governor

- **Provision:** Article 11(2)(e)(ii) (src:310): "any payment made to any governor of the entity".
- **Field:** `which payees Article 11(2)(e)(ii) reaches` of type `Which payees Article 11(2)(e)(ii) reaches`.
- **Reading A (taken):** `a payee who was a governor when the payment was made`. The payment is the event; the question is whether it was a payment to a governor.
- **Reading B:** `a payee who is a governor on the date of the application`. "any governor of the entity" is read at the date of the application, the entity being the applicant as it stands.
- **Why A:** no text decides it; my reasoning is that a payment to a person who has since left is as relevant to the applicant's governance as one to a person who has stayed.
- **Discriminating case:** a payment to a person who was a governor when paid and has since ceased to be one: reached under A, not under B; a payment to a person who became a governor after being paid: not reached under A, reached under B.
- **Tests:** `g4-tests-forks.l4` section F4.11; `g4-tests-red.l4` (one assertion).

### F4.12: "applies or should be applied" in Article 11(4)(f)

- **Provision:** Article 11(4)(f) (src:327), with Article 11(7) (src:334) and Article 9(6)(c).
- **Field:** `how applies or should be applied is read in Article 11(4)(f)` of type `How applies or should be applied is read in Article 11(4)(f)`.
- **Reading A (taken):** `a ground of mandatory refusal applies, or a ground of discretionary refusal should be applied`. Article 11(7) lets the Regulations prescribe grounds on which an application "must or may be refused". A ground on which it MUST be refused "applies"; one on which it MAY be refused "should be applied" if the Commissioner so considers. Article 9(6)(c) says the same in more words: "no ground ... on which the request must be refused or, in the case of a discretionary ground, on which the Commissioner considers the request should be refused".
- **Reading B:** `any prescribed ground whose circumstances are present defeats the matter`. "applies" is not qualified, so a ground of discretionary refusal whose circumstances are present "applies" whether or not the Commissioner would apply it.
- **Why A:** under B the words "or should be applied" would add nothing for a ground of discretionary refusal, since a ground whose circumstances are present would already "apply"; under A each word does work, and Article 9(6)(c) is the same provision spelled out.
- **Discriminating case:** a ground of discretionary refusal whose circumstances are present but which the Commissioner considers should not be applied, the rest of the six matters found: A the matter (f) holds and the Commissioner must register; B it fails and the Commissioner must refuse.
- **Tests:** `g4-tests-forks.l4` section F4.12; `g4-tests-art11-decision.l4`; `g4-tests-red.l4` (one assertion).

### Something looked at and not made a fork

The Commissioner's "satisfied" in Article 11(4).
The assignment says the Commissioner's opinions and satisfaction are inputs, and each of the six matters is already an input: the charity test (IP8), the principal address (IP17), the name (IP18), the written constitution, the substantial activity (the Commissioner's opinion), and the prescribed grounds.
So the six inputs ARE the satisfaction, and a Commissioner who is not satisfied of a matter is represented by a FALSE for it.
A further input "the Commissioner is satisfied" would have to be derived from those six or contradict them; the text gives no basis for a separate reading, so there is no fork.

## 3. Periods

| id | provision | the words | kind | where it is encoded | fork |
| --- | --- | --- | --- | --- | --- |
| P5 | 11(2)(e)(ii) | "in the 12 months preceding the application" | backward-looking period | `Art 11(2)(e)(ii) the twelve months preceding the application` | F4.1, F4.6 |
| P6 | 11(2)(e)(ii), 11(8)(a)(i) | "the application" as the anchor | commencement of a period | `Art 11 the date of the application` | F4.2 |
| P7 | 11(8)(a)(i) | "the period within which the Commissioner must make a decision on an application" | deadline set by Order | `Art 11(8)(a)(i) the last day for the Commissioner's decision` | F4.9 (and F4.2) |
| P1, P2 of G2, as applied | 11(6)(b) applying 5(7), 5(8) | "Within a reasonable time", "as soon as practicable" | standard of promptness | `Art 11(6)(b) the copy was provided to the Minister within a reasonable time`, `Art 11(6)(b) the Minister laid the copy before the States as soon as practicable` | F4.10 |

Periods looked for and not found as periods: "on registering" (Article 11(9)(a)) and "on entering" (11(9)(b)) fix a trigger and state no time; Articles 12(2) and 12(5) state no time either.
None of the rules for them has a `WITHIN`, and section 9 says so.
The kinds of period met are therefore a backward-looking period, the commencement of a period, a deadline set by Order, and a standard of promptness; each has its fork.

## 4. Answer table

The headline scenarios on the default reading, each tested; the Article that decides the answer is cited.

| scenario | answer | decided by |
| --- | --- | --- |
| A Jersey company complies with Article 11(2), the Regulations and Article 19(5), the six matters are found, no bar applies | The Commissioner must register it; the decision under Article 11 is that the Commissioner does what was sought | Art 11(4) |
| The same, but the name is undesirable under Article 12(1) | The Commissioner must refuse; the decision is a refusal | Art 11(4)(e), 11(5) |
| The same, but the charity test is not met and will not be met on registration | Must refuse | Art 11(4)(a), 11(5) |
| The same, but the charity test is not met now and will be met on registration | Must register | Art 11(4)(a) |
| A foreign entity with no activity in Jersey | Must refuse (it is not a Jersey entity and has no activity) | Art 11(4)(c), 11(5) |
| A foreign entity that carries on, or intends to carry on, in or from within Jersey an activity the Commissioner thinks substantial, with a principal address in Jersey | Must register | Art 11(4)(c)(ii), (d) |
| The same foreign entity, the activity not substantial in the Commissioner's opinion | Must refuse | Art 11(4)(c)(ii) |
| A Jersey NPO body corporate (Article 2(1)(ba)) with no activity in Jersey | Satisfies (c)(i) through its Jersey-entity status (G1's output); must register if the rest is found | Art 11(4)(c)(i) |
| Six matters found, copy of the constitution missing | No duty to register or to refuse arises (reading A of F4.3) | Art 11(2)(b), 11(4), 19(6) |
| Six matters found, a reported fitness issue undetermined | The Commissioner must not yet grant the application (reading A of F4.4) | Art 19(9)(c) displacing 11(4) |
| Six matters found, the court has ordered that the entity must not be registered | The Commissioner must not register it (reading A of F4.4) | Art 20(1)(c) displacing 11(4) |
| Application lodged and complete on 15 March 2026: the twelve months preceding it | 15 March 2025 to 14 March 2026, both inclusive | Art 11(2)(e)(ii), F4.1 A |
| A payment to a governor on 14 March 2025 / 15 March 2026 | Neither is in the period | Art 11(2)(e)(ii) |
| A payment in the period that the application does not disclose | The application does not include what Article 11(2) requires | Art 11(2)(e)(ii) |
| Application lodged 1 March 2026, complete 20 March 2026, a payment on 10 March 2026 not disclosed | Outside the period on reading A (disclosure not required); inside on reading B | Art 11(2)(e)(ii), F4.2 |
| Application lodged on 29 February 2028 | The period starts on 28 February 2027 (reading A of F4.6) | Art 11(2)(e)(ii), F4.6 |
| An Order allows 30 days from 1 March 2026 | The Commissioner may decide up to and including 31 March 2026 | Art 11(8)(a)(i), F4.9 A |
| No Order's length supplied | A named refusal: no Order is encoded | Art 11(8)(a)(i) |
| A proposed name the Commissioner thinks the same as, or too similar to, another registered charity's registered name | Undesirable | Art 12(1)(a) |
| The same, the other name being the charity's own | Not undesirable on ground (a) | Art 12(1)(a) 'other' |
| A name the Commissioner thinks likely to mislead, to give the impression of a connection that does not exist, or offensive | Undesirable | Art 12(1)(b), (c), (d) |
| A ground of Article 12(1) applies to the proposed name on an application for permission | The Commissioner must refuse permission | Art 12(4) |
| Permission granted and the charity notifies the same change, or addition, of the same name | The Commissioner must enter it | Art 12(5) |
| A registered charity uses a name that is neither a registered name nor a related name acceptable in its context | The prohibition is breached | Art 12(7) |
| A registered charity uses its alternative registered name | Permitted | Art 12(7)(a) |
| A deregistered entity uses an unrelated name | Not bound: it is not a registered charity | Art 12(7), Art 1 |
| The Commissioner has registered an entity | The Commissioner must issue a certificate of the registered name, number and date of registration, and enter the name and a number | Art 11(9)(a), 12(2) |

## 5. Nouns requests for the integrator

`domain.l4` was not edited. These are requests; each has a local stand-in in `g4-nouns.l4` until the integrator moves it.

1. **`Application for registration`** and its sub-records (`Dates of an application`, `Particulars under Article 11(2)(a)`, `Documents under Article 11(2)(b) to (d)`, `Financial details under Article 11(2)(e)`, `Other requirements under Article 11(2)(f)`). G6 decides Article 19(5) and (6) and G8 Article 33; the dates the application was lodged and became complete are shared facts. If the integrator wants one record of an application for the Law, this is it.
2. **Previous registered names.** `Registered charity` has no field for the previous names that Article 8(3)(l) keeps on the register. G4 carries them in the record `Name used by a registered charity` (field `previous registered names of the charity`). A field `previous registered names` : LIST OF STRING on `Registered charity`, set by G3, would let G4 read them from `the registered charity`.
3. **Names in the register.** Article 12(1)(a) compares a name with the names of other charities. G4 takes that as the list `entries in the register that are the same as, or too similar to, the name` of the record `Opinion of the Commissioner on a name`, each entry a `Name entered in the register` (name, kind of entry, standing of its holder, whether the entity itself holds it). G3, who keeps the register, can produce those entries; the Commissioner's opinion selects among them.
4. **IP29 should be two facts.** Standard fact IP29 is `an Order under Article 13(9) applies to the registered charity`. Article 11(2)(e)(ii) reads "an Order under Article 13(9)(b)" (the statement of intentions) and Article 8(3)(m) reads "an Order under Article 13(9)(c)" (the entry on the register). G4 consumes the standard name, as the brief requires, and reads it as the (b) fact; the integrator should wire it from a (b) fact, and G3 from a (c) fact, which may differ (an Order can be made under (a) alone).
5. **`Decision of the Commissioner` for Article 12(6).** The domain has two outcomes, `the Commissioner does what was sought or proposed` and `the Commissioner refuses`. For the decision "whether to require a charity to apply to change its registered name" G4 maps "requires" to the first and "decides not to require" to the second. The appeal of Article 33(2)(c) is against the requirement, so G8 should test for the first outcome there.
6. **"Will do so on registration" (Article 11(4)(a)).** IP8 is `the entity meets the charity test`; Article 11(4)(a) has a second limb, "or will do so on registration", for which there is no standard fact. G4 takes it as a finding (`applicant will meet the charity test on registration`). If G2 can evaluate `Art 5 the entity meets the charity test` for the entity as it will be on registration (Article 5(1)(b) already speaks of an applicant that "provides or intends to provide" public benefit), the integrator can wire the finding from there.
7. **The kind of an act.** G4's acts are records `Act under Article 11` and `Act under Article 12` (an `actor` of type `Legal actor` and a thing done). If the integrator wants a single act type for the Law, these two are the model for it; nothing else in G4 depends on their being separate.
8. **Names that could collide.** Every rule name of G4 begins `Art 11`, `Art 12` or `F4.`, except four short constants (`the entity applies`, `the applicant provides what Article 11(2) requires`, `the Commissioner registers the applicant`, `the Commissioner refuses to register the applicant`) and the five named refusals, whose names are their messages (they begin `no date of the application`, `no number of days` twice, `no Order under Article 11(8)(a)(i)` and `Articles 11(4), 19(9)(c) and 20(1)(c) conflict`). The nouns of `g4-nouns` are not prefixed; three are generic enough to collide with a noun of the same name in another group if two groups' modules are used in one file: `Period of days`, `Payment to a governor` and `Name entered in the register`. If the integrator meets "multiple definitions" on one of them, the G4 noun can be renamed (all uses are in the group's own files) or moved to `domain.l4`. I did not look at other groups' modules, so I do not know whether any collides.

## 6. Standard inputs consumed, and functions exported

### Consumed (exact `GIVEN` names)

| id | `GIVEN` name | type | read by |
| --- | --- | --- | --- |
| IP5 | `the entity` | `Entity` | `Art 11(1)`, `Art 11(4)(c)`, `Art 11(4)` (the decision), `Art 11(7)(a)`, `Art 12(2)` |
| IP6 | `the entity is a registered charity` | BOOLEAN | `Art 12(3)` |
| IP7 | `the registered charity` | `Registered charity` | `Art 11(9)(a)`, `Art 12(7)` (its entity's standing is read for Article 1's definition) |
| IP8 | `the entity meets the charity test` | BOOLEAN | `Art 11(4)(a)` and the decision |
| IP17 | `the entity has a principal address in Jersey within Article 8(4)` | BOOLEAN | `Art 11(4)(d)` and the decision |
| IP18 | `the name is undesirable under Article 12(1)` | BOOLEAN | `Art 11(4)(e)`, `Art 12(4)` and the decision (G4 consumes its own export through the integrator's wiring) |
| IP22 | `the applicant has complied with Article 19(5)` | BOOLEAN | `Art 11(4)` chapeau and the decision |
| IP23 | `Article 19(9)(c) bars granting the application` | BOOLEAN | the decision |
| IP24 | `the court has ordered that the entity must not be registered as a charity` | BOOLEAN | the decision |
| IP29 | `an Order under Article 13(9) applies to the registered charity` | BOOLEAN | `Art 11(2)(e)(ii)` second requirement and every function above it (see nouns request 4) |

Inputs that no standard name covers are `GIVEN`s with their own `@desc`: the Commissioner's finding on each matter of Article 11(4) not decided elsewhere (the record `Findings of the Commissioner for Article 11(4)`), the consultation of the Minister (`Art 11(8)(b)`), the Minister's appearance, the length of the period an Order fixes, and the like.

### Produced for other groups

| id | export | gives |
| --- | --- | --- |
| IP15 | `Art 11(4)(c) the requirement is met` | BOOLEAN; wire to `the requirement of Article 11(4)(c) is met` |
| IP16 | `Art 11(4)(d) the requirement is met` | BOOLEAN; wire to `the requirement of Article 11(4)(d) is met` |
| IP18 | `Art 12(1) the name is undesirable` | BOOLEAN; wire to `the name is undesirable under Article 12(1)`; the Commissioner's opinion is the input of the export; for 33(5)(b) evaluate it twice, with the opinion at the time of the application and at the time of the appeal |
| IP27 | `Art 11 what the Commissioner must do on the application`, `Art 12(4) what the Commissioner must do on the application for permission`, `Art 12(6) the decision of the Commissioner on whether to require the charity to apply` | `MAYBE Decision of the Commissioner` |

### Every `@export`

Each has a sentence that says what question it answers and a `@desc` on every `GIVEN` (checked by script).

| module | export | `GIVEN` parameters, in order | gives |
| --- | --- | --- | --- |
| `g4-art11-application` | `Art 11(1) the entity may apply` | `the entity`; `the entity wishes to have available to it the advantages of registration as a charity` | `DEONTIC Legal actor Act under Article 11` |
| `g4-art11-application` | `Art 11(2) the application includes what Article 11(2) requires` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity` | `BOOLEAN` |
| `g4-art11-application` | `Art 11 the date of the application` | `interp`; `the application` | `DATE` |
| `g4-art11-application` | `Art 11(2)(e)(ii) the twelve months preceding the application` | `interp`; `the application` | `Period of days` |
| `g4-art11-application` | `Art 11(2)(e)(ii) the payment to a governor is within the period` | `interp`; `the application`; `the payment date` | `BOOLEAN` |
| `g4-art11-application` | `Art 11(2)(e)(ii) the payment is one the paragraph reaches` | `interp`; `the application`; `payment` | `BOOLEAN` |
| `g4-art11-application` | `Art 11(8)(a)(i) the last day for the Commissioner's decision` | `interp`; `the application`; `the length in days of the period that an Order under Article 11(8)(a)(i) fixes` | `DATE` |
| `g4-art11-application` | `Art 11(8)(a)(i) the Commissioner's decision is within the period` | `interp`; `the application`; `the length in days of the period that an Order under Article 11(8)(a)(i) fixes`; `the day of the Commissioner's decision` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11(4)(c) the requirement is met` | `the entity`; `the applicant carries out, or intends to carry out, an activity in or from within Jersey`; `the activity is, in the opinion of the Commissioner, substantial` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11(4)(d) the requirement is met` | `the entity has a principal address in Jersey within Article 8(4)` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11(4) the applicant has complied with Article 11(2), the Regulations and Article 19(5)` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity`; `the applicant has complied with Article 19(5)` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11 the duty of the Commissioner on the application` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity`; `the applicant has complied with Article 19(5)`; `the entity`; `the entity meets the charity test`; `the findings`; `the entity has a principal address in Jersey within Article 8(4)`; `the name is undesirable under Article 12(1)`; `Article 19(9)(c) bars granting the application`; `the court has ordered that the entity must not be registered as a charity` | `Duty of the Commissioner on an application for registration` |
| `g4-art11-decision` | `Art 11 what the Commissioner must do on the application` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity`; `the applicant has complied with Article 19(5)`; `the entity`; `the entity meets the charity test`; `the findings`; `the entity has a principal address in Jersey within Article 8(4)`; `the name is undesirable under Article 12(1)`; `Article 19(9)(c) bars granting the application`; `the court has ordered that the entity must not be registered as a charity` | `MAYBE Decision of the Commissioner` |
| `g4-art11-decision` | `Art 11(4) the Commissioner must register the applicant` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity`; `the applicant has complied with Article 19(5)`; `the entity`; `the entity meets the charity test`; `the findings`; `the entity has a principal address in Jersey within Article 8(4)`; `the name is undesirable under Article 12(1)`; `Article 19(9)(c) bars granting the application`; `the court has ordered that the entity must not be registered as a charity` | `DEONTIC Legal actor Act under Article 11` |
| `g4-art11-decision` | `Art 11(5) the Commissioner must refuse to register the applicant` | `interp`; `the application`; `an Order under Article 13(9) applies to the registered charity`; `the applicant has complied with Article 19(5)`; `the entity`; `the entity meets the charity test`; `the findings`; `the entity has a principal address in Jersey within Article 8(4)`; `the name is undesirable under Article 12(1)`; `Article 19(9)(c) bars granting the application`; `the court has ordered that the entity must not be registered as a charity` | `DEONTIC Legal actor Act under Article 11` |
| `g4-art11-decision` | `Art 11(6)(b) the copy was provided to the Minister within a reasonable time` | `interp`; `the Commissioner provided the copy within a reasonable time`; `the day the guidance was issued or amended`; `the day the Commissioner provided the copy`; `the number of days that counts as a reasonable time` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11(6)(b) the Minister laid the copy before the States as soon as practicable` | `interp`; `the Minister laid the copy as soon as practicable`; `the day the Minister received the guidance and the report`; `the day the Minister laid the copy before the States`; `the number of days that counts as as soon as practicable` | `BOOLEAN` |
| `g4-art11-decision` | `Art 11(9)(a) the Commissioner must issue a certificate of registration` | `the Commissioner has registered the entity as a charity`; `the registered charity` | `DEONTIC Legal actor Act under Article 11` |
| `g4-art11-decision` | `Art 11(9)(b) the Commissioner must issue a further certificate for a new or alternative registered name` | `the Commissioner has entered a new or alternative registered name under Article 12(5)`; `the new or alternative registered name`; `the day on which that name was entered on the register` | `DEONTIC Legal actor Act under Article 11` |
| `g4-art12-name` | `Art 12(1) the name is undesirable` | `interp`; `opinion` | `BOOLEAN` |
| `g4-art12-name` | `Art 12(2) the Commissioner must enter the registered name and allocate and enter a number` | `the entity`; `the Commissioner has registered the entity` | `DEONTIC Legal actor Act under Article 12` |
| `g4-art12-name` | `Art 12(4) the Commissioner must refuse permission to change or add a name` | `the name is undesirable under Article 12(1)` | `DEONTIC Legal actor Act under Article 12` |
| `g4-art12-name` | `Art 12(4) what the Commissioner must do on the application for permission` | `the name is undesirable under Article 12(1)` | `MAYBE Decision of the Commissioner` |
| `g4-art12-name` | `Art 12(5) the Commissioner must enter the new or alternative registered name` | `permission was granted`; `the name for which permission was granted`; `the change for which permission was granted`; `the charity notified the Commissioner that it has changed or added the name`; `the name notified`; `the change notified` | `DEONTIC Legal actor Act under Article 12` |
| `g4-art12-name` | `Art 12(6) the Commissioner may require the charity to apply to change its registered name` | `the charity reported a matter relating to its registered name under Article 13(6)(b)` | `DEONTIC Legal actor Act under Article 12` |
| `g4-art12-name` | `Art 12(7) the name used is permitted` | `interp`; `the registered charity`; `used` | `BOOLEAN` |
| `g4-art12-name` | `Art 12(7) a registered charity must not use a name other than a registered or related name` | `interp`; `the registered charity`; `used` | `DEONTIC Legal actor Act under Article 12` |

A function that depends on a fork takes the record as its first `GIVEN`, named `interp`, so that a caller can choose the reading.

## 7. Contradictions and other findings in the source

Found by a deliberate pass after the modules were written, reading Articles 11 and 12 against my own rules, and checking every cross-reference in the scope.
Every cross-reference in the scope resolves: 11(2)(a)(i) to 11(4)(c) and (d); 11(2)(a)(ii) and (iii) to 8(3)(a), (b), (d), (h), (i), (m), (n); 11(2)(e)(ii) to 13(9)(b); 11(4) to 11(2), 11(3), 19(5), 8(4), 12, 11(7); 11(6) to 11(4)(c)(ii), 5(4) and 5(6) to (8); 11(9)(b) to 12(5); 11(10) and (11) to each other; 12(1) to 11(4)(e); 12(4) to 12(1)(a) to (d); 12(6) to 13(6)(b).
The text of Articles 11 and 12 in the consolidated file and in the official PDF's text layer was compared mechanically after removing page furniture, quotation-mark style and hyphenation: 1,354 words in each, no difference (and I also read every number, list and connective in both). No endnote marker is on a provision of either Article, and no entry in the Table of Endnote References amends them.

### Contradictions and conflicts

**C1. The duty to register meets two bars (trap T10).** Article 11(4): the Commissioner "must register the applicant as a charity if satisfied" of six matters. Article 19(9)(c): the Commissioner "must not, in the case of an application for registration, grant that application until the issue has been determined". Article 20(1)(c): the court may order "that the entity must not be registered as a charity". Neither bar is among the six matters. Discriminating case: the applicant satisfies (a) to (f) and a reported fitness issue about a governor is undetermined, MUST register and MUST NOT grant at once. Fork F4.4; every reading is callable; test in `g4-tests-forks.l4` section F4.4.

**C2. Article 11(5) does not repeat the condition of Article 11(4).** "If not so satisfied" is the whole condition of the duty to refuse, while the duty to register is conditioned on the applicant's compliance as well as on satisfaction. Read literally, an application that does not comply and whose six matters are not found must be refused, while one that does not comply and whose six matters are found need not be. Discriminating case: the copy of the constitution is missing and the name is undesirable. Fork F4.3, reading C (new).

**C3. A defined term used outside its definition's stated purpose (12(1) and 12(7)(b)(ii)).** Article 12(1) defines "undesirable" "for the purpose of Article 11(4)(e)" and "as the registered name of a charity". Article 12(4) re-states the four grounds instead of using the term, but Article 12(7)(b)(ii) uses "undesirable within the meaning of paragraph (1), in the context in which it is used" of a name that is not a registered name and not an application for registration, and Article 33(5)(b) uses "undesirable under Article 12(1)". Read strictly, the definition does not reach a name used in a context. Discriminating case: a name used for a trading activity and offensive to the Commissioner in that context: undesirable "within the meaning of paragraph (1)" only if the definition's stated purpose is read loosely. There is no fork because the Law answers the strict reading in its own words: Article 12(7)(b)(ii) says "undesirable within the meaning of paragraph (1), in the context in which it is used", an express import of paragraph (1) into the context of use. What can still vary is the Commissioner's opinion, and the encoding takes that, on the four grounds and in the context of use, as the input (`undesirable within Article 12(1) in the context in which it is used, in the opinion of the Commissioner`); the strict reading is therefore a different input and not a different function.

**C4. "Complete" (19(6)) is not "includes what Article 11(2) requires".** Article 19(6) makes an application "not complete" only if Article 19(5) has not been complied with. Article 11(4) conditions the duty on compliance with paragraph (2) and with Article 19(5), separately. So an application can be complete in the sense of 19(6) and yet short of 11(2). The two notions are kept apart (the field `date on which it became complete` is the 19(6) one); the survey's trap T10 case B and fork F4.2 both depend on the distinction.

**C5. Two Articles name different sub-paragraphs of Article 13(9) for one Order.** Article 11(2)(e)(ii) reads "an Order under Article 13(9)(b)" and Article 8(3)(m) reads "an Order under Article 13(9)(c)". They are consistent in subject (the statement of intentions, and its entry on the register) but an Order may be made under one without the other, and the survey's standard fact IP29 names Article 13(9) as a whole. Nouns request 4.

**C6. A constitution "in whatever form" against a constitution that is "a written document".** Article 2(4)(g): for any other case the constitution is "any instrument or instruments (in whatever form) that establish the entity or give it any powers". Article 11(4)(b): the Commissioner must be satisfied that "the constitution of the applicant is a written document". Article 11(2)(b) asks for "a copy of the applicant's constitution". An entity whose constitution is an instrument that is not a written document (an oral understanding, a recording) is an entity under Article 2 and cannot be registered under Article 11(4)(b). This is a tension and not a conflict (11(4)(b) is a ground of refusal), but the Law does not say that it is meant. The written-document finding is an input, so the encoding is unaffected.

**C7. A referent that does not exist yet.** Article 11(2): the applicant must provide information "in such form as the Commissioner may publish in relation to an entity of a description into which that charity falls". "That charity" is the applicant, which is not a charity until registered. Article 11(2)(e)(ii) has the same shape with "the registered charity" (trap T28). Both are read of the applicant.

### Gaps and asymmetries (not contradictions)

**D1.** Article 11(6)(c) obliges only the Commissioner to have regard to the guidance in determining whether an activity is substantial, and 11(6)(d) adds a registered charity, a governor, the tribunal and the court, while Article 5(5) for the charity test obliges "any person" in determining whether an entity meets the test and omits the court. The two guidance regimes are parallel but not identical; 11(6)(b) imports 5(6) to (8) and not 5(5), which 11(6)(c) and (d) replace.

**D2.** Article 11(2)(e)(iv) refers to financial information "prescribed by the Minister by Order" and no Article of the Law says that the Minister may make that Order. This is the drafting style of the Law, which says "prescribed by the Minister by Order", or words close to it, in the same way at 8(3)(n), 8(5)(e), 8(6)(d), 9(1)(d), 13(6)(h), 16(1)(d) and 19(1)(h), and I do not report it as a conflict. What can be said is that Article 11(3)(a) lets the States prescribe "other information, documents or evidence" by Regulations, so two bodies and two instruments can add to the same list; the Law does not say which prevails if they differ.

**D3.** Article 12(1)(a) compares a name with that of "any other registered charity", which includes a charity in the restricted section whose registered name is not public (Article 9(1)(a)). The applicant cannot know it. The Commissioner can. Nothing in the Law says how an applicant is told.

**D4.** Nothing says that an applicant must be told of a refusal under Article 11. Article 9(7)(a) requires written notice of a refusal of a request for the restricted section; Article 11(8)(a)(ii) lets an Order provide for the notification of decisions and of reasons for refusal. Article 33(1)(a) gives an appeal against a decision "to refuse to register the applicant".

**D5.** Article 12(2)(b) says the Commissioner "allocate[s] a number in respect of the registration" and Article 17(1)(b) says the Commissioner "must not assign the registered number of that entity to any other registered charity" after deregistration. Whether an entity that is registered again (nothing bars it) receives a new number or its old one is not said; nothing says numbers must be unique or what form they take.

**D6.** An entity may apply (11(1)) even if it is already a registered charity or has been deregistered; the Law neither permits nor forbids it, and the encoding permits any entity that wishes to.

**D7.** Article 13(6)(b) (G5's) speaks of a matter that could have led the Commissioner to "refus[e] to accept the name of the charity". Articles 11 and 12 give the Commissioner no decision called by those words: the decisions are to refuse to register on the ground of Article 11(4)(e) and to refuse permission under Article 12(4). Article 12(6) cross-refers to 13(6)(b) and is encoded as written; the phrase is read as covering both.

## 8. Open questions for a domain expert

- On Article 11(5): does the duty to refuse arise for an application that does not comply with Article 11(2), the Regulations or Article 19(5) when the six matters are not found (F4.3 reading C), or does the Commissioner wait for a complete application (reading A)?
- On Articles 11(4), 19(9)(c) and 20(1)(c): which prevails (F4.4)? Is the refusal of Article 11(5) available while a fitness issue is undetermined, or must the application stay pending?
- On Article 11(2)(e)(ii): which twelve months (F4.1), counted from which date (F4.2), and does "any governor of the entity" mean a governor when the payment was made or on the date of the application (F4.11)?
- On Article 12(1)(a): are the alternative and previous registered names of another charity "the name" of that charity (F4.7), and is a deregistered charity "another registered charity" (F4.5)?
- On Article 12(7)(a): after a charity changes its registered name, may it still use its previous name as "one of its registered names" (F4.8)?
- On Article 12(7)(b)(ii): does the definition of "undesirable" in Article 12(1), which is "for the purpose of Article 11(4)(e)", apply to a name used in some context (finding C3)?
- On Article 11(2)(e)(ii): are payments by a third party to a governor (for example a salary from the governor's own employer) within "any payment made to any governor of the entity", or only payments by the entity or on its behalf?
- What is "related" in Article 12(7)(b)(i)?
- Is there any consequence of breaching Article 12(7) other than as misconduct under Article 2(10)(a)(i)?
- On Article 11(8)(a)(i): what does the Order, if one is made, say happens to a decision made after the period? The Law says nothing.
- Do Regulations under Article 11(3)(a) and an Order that prescribes financial information under Article 11(2)(e)(iv) overlap, and which prevails?

## 9. What the sources do not answer

- The content of any Order or Regulations under Article 11(3), 11(7), 11(8) and the Order of Article 11(2)(e)(iv): none is among the sources. Each is an input, and the one that fixes a length (Article 11(8)(a)(i)) answers a named refusal while it is not supplied.
- The form the Commissioner publishes under Article 11(2) ("in such form as the Commissioner may publish"). Whether an item was provided in that form is absorbed in the BOOLEAN that says it was provided.
- The content of the Non-Profit Organizations (Jersey) Law 2008: whether an applicant must register under it, what additional information it requires, and what financial information it would require, are inputs.
- Who makes the payments that Article 11(2)(e)(ii) asks about: "any payment made to any governor of the entity" does not say by whom (contrast Article 13(9)(a), "by or on behalf of the registered charity to a governor, or to a person having a prescribed connection with a governor"). The list of payments is an input, so the caller decides; the question is registered as an open question and not as a fork because it changes an input and not a computation.
- What "substantial" means in Article 11(4)(c)(ii): the Commissioner's opinion, with guidance the Commissioner publishes under Article 11(6); the guidance is not among the sources.
- What "related" means in Article 12(7)(b)(i), and what "too similar", "likely to mislead", "gives the impression" and "offensive" mean in Article 12(1): the Commissioner's opinion.
- A time limit for any duty of the Commissioner in Articles 11 and 12 (to register, to refuse, to issue the certificate on registering, to enter the name or the number, to enter a changed or added name) unless an Order under Article 11(8)(a)(i) fixes one for the decision. The rules for them have no `WITHIN`.
- Whether the Commissioner must, or may, grant permission under Article 12(3) when no ground of Article 12(1) applies. Article 12(4) says when permission must be refused and Article 12(5) says what follows a grant; the power to grant is implied. The decision function answers NOTHING for that case.
- Whether a failure to comply with a requirement under Article 12(6) has a consequence, and what it is.
- Whether an applicant is told of a refusal, and how (finding D4).
- Whether numbers entered under Article 12(2)(b) are unique, and what becomes of an entity's number when it is registered again (finding D5).
- Whether the approval of a decision by a member of the Commissioner's staff is possible: Schedule 1 paragraph 4(3)(a) reserves "the decision under Article 11 on whether to register a charity" to the Commissioner. The decision function's subject is `whether to register an applicant, Article 11`; G9 reads it.
- The commencement of Part 4 is 1 May 2018 (R&O.17/2018), from the Table of Legislation History, and is not gated here (PLAN section 10). Anything the Law said before 1 January 2019 is not in the sources.

## 10. Modelling decisions (assumed, not ruled)

Each is a choice made while encoding that no ruling covers; each can be reversed alone.

1. **The Commissioner's satisfaction is the six inputs.** No further "satisfied" input (section 2, last subsection).
2. **A guarded rule answers FULFILLED when its guard fails.** A duty or power with a precondition (`IF guard THEN PARTY ... ELSE FULFILLED`) means "nothing is owed or permitted here" when the guard is FALSE. The guard is also a predicate that a test can assert.
3. **Duties and powers are typed by role and act.** The party is a constructor of `Legal actor`; the act is a record of the performer and a thing done, named for what is done and never for the Article. The performer rule of the language therefore checks that each act is done by the role that may do it.
4. **No `WITHIN` where the Law states no time.** A duty without a deadline stands until performed; its trace ends as a standing obligation, never as a breach.
5. **Powers of the Minister with a precondition.** The precondition (the consultation) is a predicate; the power is `IF predicate THEN MAY ... ELSE FULFILLED`. The Law does not forbid the Minister to make the Order without consulting, but the power is conferred only "after consulting", so no permission arises without it.
6. **Article 5(6) to (8), applied by Article 11(6)(b), are restated here** for the guidance on a substantial activity, as three duties and two promptness predicates, because a group module may not call another group's. If the integrator prefers one set of rules parameterised by the guidance, G2's and these can be merged.
7. **Disclosure of a payment compares who, when and how much.** A payment is disclosed when the application gives those three details; the two facts about the payee that fork F4.11 reads are not details of the payment.
8. **A relief by Order is a list of the provisions of Article 11(2) disapplied for this applicant**, supplied by the caller. A modification under Article 11(8)(b)(ii) is absorbed in what the applicant is recorded as having provided.
9. **The decision period's length is a `MAYBE NUMBER`.** NOTHING is a named refusal, not zero.
10. **Article 12(7) binds a registered charity only**, in the sense of Article 1 (an entity in the general or the restricted section), read from the standing of the entity of the `Registered charity` record.
11. **"Accordingly" in Article 12(5)** is read as: the name the charity notified is exactly the name for which permission was granted, and the change notified is the kind of change permitted (string equality on the name). A looser reading would be a judgement of the Commissioner and is not offered.
12. **"If applicable" in Article 11(2)(a)(iii)** is one flag for the four matters of Article 8(3)(h), (i), (m) and (n): TRUE when at least one applies, the information then being what is required about those that do.
13. **Test numbers that are not in the Law.** The 30 days of an Order, the 59 and 14 days of the promptness tests, the amounts and names of payments and charities are illustrations chosen to put the cases on both sides of a boundary; the Law gives none of them. The only numbers the Law gives in this scope are 12 (months), 1 (one governor, 11(7)(a)) and the Article and paragraph numbers.

## 11. What the check prints

These are the result lines of the output of the check script for this group (`work/g4/check.sh`, the skill's `assets/check.sh` adapted to run only `DEPOSIT/g4-*.l4`, with a warnings column, the import-graph check, `srcrefs.py check --refs` and `check-traces.py`), as it was when this file was generated.
Nothing is printed here from memory.

```text
l4 binary: /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4 (sha256 matches the fleet's binary)
module                                    errors satisfied  failed  refused  warnings  exp.fail
g4-art11-application.l4                        0         0       0        0         0         0
g4-art11-decision.l4                           0         0       0        0         0         0
g4-art12-name.l4                               0         0       0        0         0         0
g4-interpretation.l4                           0         0       0        0         0         0
g4-nouns.l4                                    0         0       0        0         0         0
g4-tests-art11-application.l4                  0        83       0        0         0         0
g4-tests-art11-decision.l4                     0        82       0        0         0         0
g4-tests-art12-name.l4                         0        34       0        0         0         0
g4-tests-fixtures.l4                           0         0       0        0         0         0
g4-tests-forks.l4                              0       210       0        0         0         0
g4-tests-red.l4                               14         0      14        0         0        14
TOTAL (11 modules)                            14       409      14        0         0        14
shape: every module has a plain name, none starts with @lang en, and each imports only prelude, daydate, domain and g4- modules
srcrefs check: 256 src: lines, 131 runs, 185 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g4-tests-art11-application.l4                     40        40         0     40     0          0
g4-tests-art11-decision.l4                        39        39         0     39     0          0
g4-tests-art12-name.l4                            34        34         0     34     0          0
g4-tests-forks.l4                                  4         4         0      4     0          0
TOTAL                                            117       117         0    117     0          0
check-traces: all 117 guarded trace(s) behaved as expected
check.sh (G4): GREEN
```

`g4-tests-red.l4` is MEANT to fail 14 assertions (13 expectations of another reading's answer under the default reading, one `#ASSERT REFUSED` on an expression that answers); the script lists the count, so any other number is red.
There are no failing or refused assertions apart from those 14, and no warning anywhere.

The positive control: `work/g4/mutate.py` applies 28 single mutations to a copy of the rule modules and runs the four test modules and the trace checker against each; the result is recorded in section 12.

## 12. Positive control (mutations)

```text
M01 F4.1 A: last day is the day of the application                       KILLED (errors 11, traces ok)
M02 payment within period: first day exclusive                           KILLED (errors 9, traces ok)
M03 F4.6 A rolls instead of clamping                                     KILLED (errors 5, traces ok)
M04 11(4)(a) needs both                                                  KILLED (errors 25, traces changed)
M05 11(4)(e) forgets the NOT                                             KILLED (errors 32, traces changed)
M06 F4.3 A: non-complying is refused                                     KILLED (errors 12, traces changed)
M07 F4.4 A: the 19(9)(c) bar before the court order                      KILLED (errors 2, traces ok)
M08 11(4)(c)(ii) either suffices                                         KILLED (errors 6, traces ok)
M09 12(1)(a) counts the charity's own name                               KILLED (errors 1, traces ok)
M10 12(7) obliges instead of prohibiting                                 KILLED (errors 0, traces changed)
M11 12(4) refuses when the name is not undesirable                       KILLED (errors 0, traces changed)
M12 F4.5 A counts the historic section                                   KILLED (errors 2, traces ok)
M13 11(2)(e)(iv) applies even when the restricted section is requested   KILLED (errors 1, traces ok)
M14 11(2)(a): the proposal is never required                             KILLED (errors 1, traces ok)
M15 disclosure: any instead of all                                       KILLED (errors 41, traces changed)
M16 12(5) ignores the kind of change                                     KILLED (errors 0, traces changed)
M17 11(4) duty is to refuse                                              KILLED (errors 0, traces changed)
M18 11(1) permits a non-entity                                           KILLED (errors 0, traces changed)
M19 F4.2 A uses the day it becomes complete                              KILLED (errors 29, traces ok)
M20 F4.9 A counts the anchor as day one                                  KILLED (errors 10, traces ok)
M21 11(6)(d) binds the Commissioner too                                  KILLED (errors 3, traces changed)
M22 11(9)(a) certificate carries the wrong date field                    KILLED (errors 0, traces changed)
M23 12(7)(b) ignores undesirability in context                           KILLED (errors 2, traces changed)
M24 F4.7 A excludes alternative names                                    KILLED (errors 2, traces ok)
M25 12(7) binds a deregistered entity too                                KILLED (errors 0, traces changed)
M26 disclosure compares whole records again                              KILLED (errors 1, traces ok)
M27 disclosure ignores the amount                                        KILLED (errors 1, traces ok)
M28 F4.12 A also counts circumstances present                            KILLED (errors 3, traces ok)
survivors: none
```

## 13. A second check of the twelve months

The window of Article 11(2)(e)(ii) was also checked against a model written independently in Python (`work/g4/diff_window.py`, which shares no code with the encoding).
It drove the exported `Art 11(2)(e)(ii) the payment to a governor is within the period` through `l4 batch` on 549 cases: 16 application dates (the days around 1 March 2027, 27 February to 1 March 2028, month ends, 1 January 2026, 29 February 2032), every reading of F4.1 and F4.6, and for each the payment dates on and beside both ends of the window and the day of the application.
Result: 549 cases, 549 answers, 0 differences.

