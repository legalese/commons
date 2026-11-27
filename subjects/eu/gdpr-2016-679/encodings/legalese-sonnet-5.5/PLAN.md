# PLAN.md -- P1 of Regulation (EU) 2016/679 (GDPR), and the keel as P1 wrote it

Written by P1 (Sonnet 5.5) for the parts that follow.
Status of this file: every statement below was checked against the files in this folder on the day P1 stopped (the check is `check.sh`, whose output is in NOTES.md).
Later parts read this file and do NOT read P1's code.
Target compiler: `main`, build 1.6.112 (`e4f4bf3`, 2026-11-18); leave `JL4_LIBRARY_PATH` unset.

## 1 Purpose and how to read this plan

P1 encodes Article 2(1) and (2), Article 4 points (1), (2), (6), (7), (8), Chapter II (Articles 5 to 11) and Article 24 of the consolidated text (lines 19-26, 39-40, 44-46, 76-141, 308-312), and, because no keel existed, writes the shared nouns and the Article 4 definitions it needs.
What each file is:

| file | what it is | who may edit |
| --- | --- | --- |
| `gdpr-core.l4` | the keel's nouns: DECLARE only (165 lines) | nobody after P1; K2 may extend it |
| `gdpr-definitions.l4`, `gdpr-definitions-tests.l4` | Art 4 points (1), (2), (6), (7), (8) as functions, and their tests | K2 adds points 3-5, 9-26 (in this file or in its own `gdpr-` module) |
| `P1-art-2.l4` ... `P1-art-24.l4`, `P1-tests-art-N.l4` | layer 1 for P1's provisions, one module per article (Article 6 is two: `P1-art-6.l4` for (1) and (2), `P1-art-6b.l4` for (3) and (4)) | P1 only |
| `P1-seat-subject.l4`, `P1-seat-controller.l4`, `P1-cases-seat-*.l4`, `P1-cases-mirror.l4` | the seat layer and its cases | P1 only |
| `NOTES.md`, `PROGRESS.md`, `PLAN.md`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` | records and tools | P1 only |

How to take a name from P1: IMPORT `gdpr-core` and `gdpr-definitions` (the keel).
Do NOT import a `P1-` module: parts live in separate sandboxes, so a later part takes a P1 answer as an INPUT fact (section 4).
A module may import only modules in its own folder.

Reading a result.
Every decision function answers `MAYBE BOOLEAN` or `MAYBE` an enum (`MAYBE `Duty outcome``, or `MAYBE` of `Art 4(7) how a controller determines the purposes and means`), with these exceptions: `Art 9(1) the categories processed include one that paragraph 1 names` answers a plain `BOOLEAN` (a helper other rules use as a gate, not a decision of the text); three functions answer a `NUMBER` (the two constants of Art 8(1), 16 and 13, and `Art 8(1) the age from which the child may consent in this Member State`); and the regulative forms answer a `DEONTIC`.
The two Art 8(1) seat questions "is the consent of the holder of parental responsibility needed" answer `MAYBE BOOLEAN` (they were a plain `BOOLEAN` before the fix round).
`JUST TRUE` and `JUST FALSE` are answers the text gives in its own words; `NOTHING` means the text does not answer on these facts, and a caller must never turn `NOTHING` into `FALSE`.
Every `NOTHING` branch is tagged `-- NOTHING-kind (...)` and every `JUST FALSE` branch `-- FALSE-kind (...)` in the code; the six kinds of NOTHING are silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.

## 2 Naming rule (every part follows it)

- A name defined in two modules imported together cannot be used at all (main reports "multiple definitions"), so no two parts may define the same name.
- Every top-level name (function, constant, type, constructor) a part defines begins with the label of the provision it implements, in the Regulation's own numbering and in the form `Art 5(1)(a) ...`, `Art 6(4)(a) ...`, `Art 9(2)(h) ...`.
  Parentheses inside a backtick name parse on main.
  This covers every type and every constructor, not only functions: `` DECLARE `Art 6(1) lawful basis` IS ONE OF `Art 6(1)(a) consent`, ... `` and never a bare `Consent`.
- Types and constructors shared across parts live only in the core and the keel's modules (`gdpr-core.l4`, `gdpr-definitions.l4`, and what K2 adds).
  The role nouns and the two shared result types in the core have plain names (`controller`, `data subject`, `Duty outcome`): no later part may reuse them.
- Later parts may not edit the keel's modules.
  A part that needs a type or constructor the keel lacks defines it in its own module under its own label and records it in `NEEDS-CORE.md`.
- File names: every module of part `Pn` begins with `Pn-` (`P1-art-5.l4`, `P1-tests-art-5.l4`, `P1-seat-subject.l4`, `P1-cases-seat-subject.l4`); every module of the keel begins with `gdpr-`.
- A name that is not a provision's: a seat helper begins with its part and seat (`P1 controller answer`, `P1 subject principles shown`), and so does each constructor of a seat's answer type (`P1 controller answer: yes`, `P1 subject answer: not sure`).
  A later part writes `P2 controller ...`, `P2 subject ...`.
- Name a function for what the provision says, never `is the processing lawful` and never `may I ...`: `Art 6(1)(f) point (f) applies: the processing is necessary for legitimate interests that are not overridden`.

## 3 The core and the keel's modules

### 3.1 `gdpr-core.l4` (imports `prelude` and `daydate` only; no rule, no constant)

No money and no date is declared: nothing in P1's range is a sum or a date.
The constants a part needs (the ages 16 and 13 of Art 8(1)) are in `P1-art-8.l4`, under the Article's label.


| type | members | gloss |
| --- | --- | --- |
| `Role in the Regulation` | 9: `data subject`, `controller`, `joint controller`, `processor`, `recipient`, `third party`, `representative`, `supervisory authority`, `child` | a party the Regulation speaks of; the shared PARTY type for any regulative rule (P1 uses `controller` and `data subject`) |
| `Kind of person or body` | 6: `natural person`, `legal person`, `public authority`, `agency`, `other body`, `not a person or body` | "natural or legal person, public authority, agency or other body" (Art 4(7), (8), and for K2 (9), (10), (17)); the last member is the case just outside the list, such as a software tool |
| `Duty outcome` | 3: `the duty does not arise`, `the duty arises and is met`, `the duty arises and is not met` | the answer of every gated duty ("where", "if", "when", "where necessary"), always wrapped in `MAYBE`; the first member is the text's own no to a failed gate (periods ruling (b)); NOTHING means not covered |
| `Art 4(1) means of identification` | 12 | name, identification number, location data, online identifier, seven factor-specific identities (physical, physiological, genetic, mental, economic, cultural, social), some other means |
| `Art 4(2) operation on personal data` | 19 | the 18 operations Art 4(2) names ("such as") and `some other operation` |
| `Art 4(6) arrangement of a set of personal data` | 5 | centralised, decentralised, dispersed on a functional basis, dispersed on a geographical basis, some other arrangement |
| `Art 4(7) how a controller determines the purposes and means` | 2 | `Art 4(7) alone`, `Art 4(7) jointly with others` |
| `Art 5 principle` | 7 | the principles of Art 5(1)(a) to (f) and Art 5(2) accountability |
| `Art 5(1)(b) purpose of archiving, research or statistics` | 5 | the four purposes of Art 5(1)(b), Art 5(1)(e), Art 9(2)(j) and (for P9) Art 89, and `Art 5(1)(b) some other purpose` |
| `Art 6(1) lawful basis` | 6 | `Art 6(1)(a) consent` to `Art 6(1)(f) legitimate interests` |
| `Art 9(1) category of personal data` | 10 | the eight categories Art 9(1) names, `Art 9(1) biometric data not for the purpose of uniquely identifying a natural person` (just outside), `Art 9(1) other personal data` |
| `Art 9(2) ground` | 10 | `Art 9(2)(a) explicit consent` to `Art 9(2)(j) archiving, research or statistical purposes`; no P1 function reads it (the ten grounds are functions in P1-art-9.l4); it is there for later parts that must name a ground |

### 3.2 `gdpr-definitions.l4` (imports `prelude` and `gdpr-core`)

One function per defined term, typed arguments that are facts a person could state.
Every function answers `MAYBE`; `JUST FALSE` is the "means" no.

| function | inputs (name and type) | answer |
| --- | --- | --- |
| `Art 4(1) the natural person is an identifiable natural person` | `the ways the natural person can be identified` (LIST OF `Art 4(1) means of identification) | MAYBE BOOLEAN |
| `Art 4(1) the information is personal data` | `the information relates to a natural person` (BOOLEAN); `the natural person is identified` (BOOLEAN); `the ways the natural person can be identified` (LIST OF `Art 4(1) means of identification) | MAYBE BOOLEAN |
| `Art 4(1) the person is a data subject` | `the person is a natural person` (BOOLEAN); `the information relates to the person` (BOOLEAN); `the person is identified` (BOOLEAN); `the ways the person can be identified` (LIST OF `Art 4(1) means of identification) | MAYBE BOOLEAN |
| `Art 4(2) the operations are processing` | `the operations performed` (LIST OF `Art 4(2) operation on personal data); `on personal data` (BOOLEAN); `on sets of personal data` (BOOLEAN) (these two replaced one input, `the operations are performed on personal data or on sets of personal data`, on 2026-11-27: see NOTES.md, "Art 4(2): the OR is two inputs"); `the operations are performed by automated means` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(6) the set is a filing system` | `the set is structured` (BOOLEAN); `the set consists of personal data` (BOOLEAN); `the data are accessible according to specific criteria` (BOOLEAN); `how the set is arranged` (Art 4(6) arrangement of a set of personal data) | MAYBE BOOLEAN |
| `Art 4(7) the body is a controller` | `body` (Kind of person or body); `the body decides the purposes of the processing` (BOOLEAN); `the body decides the means of the processing` (BOOLEAN); `Union or Member State law determines the purposes and means of the processing` (BOOLEAN); `that law provides for the body as the controller, or sets criteria for nominating the controller that the body meets` (BOOLEAN) | MAYBE BOOLEAN |
| `Art 4(7) how the body determines the purposes and means` | `the body decides the purposes of the processing` (BOOLEAN); `the body decides the means of the processing` (BOOLEAN); `the body decides them jointly with another body` (BOOLEAN) | MAYBE Art 4(7) how a controller determines the purposes and means |
| `Art 4(8) the body is a processor` | `body` (Kind of person or body); `the body processes personal data` (BOOLEAN); `the body processes it on behalf of the controller` (BOOLEAN) | MAYBE BOOLEAN |

`Art 4(1) the person is a data subject` calls `Art 4(1) the information is personal data`; `Art 4(1) the information is personal data` calls `Art 4(1) the natural person is an identifiable natural person`.
Points (3) to (5), (9) to (26) are K2's.
The terms of P1's range that are not points (1), (2), (6), (7), (8) are plain input facts: see section 4.

### 3.3 The layer-1 modules of P1 (read these names; do not import them)

Each function below answers `MAYBE BOOLEAN` unless the last column says otherwise.
A later part that needs one of these answers takes it as an input with the name of the answering function (section 4).

| module | functions a later part may need (full names begin as shown) | result |
| --- | --- | --- |
| `P1-art-2.l4` | `Art 2(1) and (2) the processing is within the material scope of this Regulation` (combines `Art 2(1) this Regulation applies to the processing of personal data` and `Art 2(2) this Regulation applies ... given points (a) to (d)`; points (a) to (d) are `Art 2(2)(a)`...`(d)`) | MAYBE BOOLEAN |
| `P1-art-5.l4` | `Art 5(1)(a)` ... `Art 5(1)(f)` (one principle each; (b) and (e) have a second function for the deeming sentence and the longer storage; (d) has a second function, the "reasonable step" duty, answering `Duty outcome`), `Art 5(2) the body is responsible ...`, `Art 5(2) the controller is able to demonstrate ...` | MAYBE BOOLEAN |
| `P1-art-6.l4` | `Art 6(1)(a)` ... `Art 6(1)(f)`, `Art 6(1) the condition is met that at least one of points (a) to (f) applies` (takes six MAYBE BOOLEAN answers), `Art 6(2) a Member State may ...` | MAYBE BOOLEAN |
| `P1-art-6b.l4` | `Art 6(3) the basis ...`, `Art 6(3) the purpose ...`, `Art 6(3) the legal basis may contain ...`, `Art 6(3) the Union or Member State law meets ...`, `Art 6(4) the controller takes into account ...` | MAYBE BOOLEAN; the 6(4) one MAYBE `Duty outcome` |
| `P1-art-7.l4` | `Art 7(1) the controller is able to demonstrate ...`, `Art 7(2) the request for consent is presented clearly ...` (both `Duty outcome`), `Art 7(2) the part of the declaration is binding`, `Art 7(3) ...` (four), `Art 7(4) ...` | mixed |
| `P1-art-8.l4` | constants `Art 8(1) the age from which a child may consent unless a Member State has provided otherwise` (16) and `Art 8(1) the lowest age a Member State may provide by law` (13); `Art 8(1) a Member State may provide by law for the lower age`, `Art 8(1) the age from which the child may consent in this Member State`, `Art 8(1) the case is one in which the consent of the holder of parental responsibility is needed` (MAYBE BOOLEAN, with the same arms as the decision function; Art 8(2) tests it `EQUALS JUST TRUE`), `Art 8(1) the processing of a child's personal data meets the condition of Art 8(1)`, `Art 8(2) ...` (its first input is that MAYBE BOOLEAN), `Art 8(3) ...` | mixed |
| `P1-art-9.l4` | `Art 9(1) the categories processed include one that paragraph 1 names` (a plain BOOLEAN), `Art 9(2)(a)` ... `(j)`, `Art 9(2) one of points (a) to (j) applies` (ten MAYBE BOOLEAN), `Art 9(1) the processing of personal data of a category named in paragraph 1 is prohibited`, `Art 9(3)`, `Art 9(4)` | MAYBE BOOLEAN, except the first |
| `P1-art-10.l4` | `Art 10 the processing ... meets the condition of Art 10`, `Art 10 the comprehensive register ...` | MAYBE BOOLEAN |
| `P1-art-11.l4` | `Art 11(1) ...`, `Art 11(2) the controller informs the data subject ...` (`Duty outcome`), `Art 11(2) Articles 15 to 20 are disapplied` | MAYBE BOOLEAN |
| `P1-art-24.l4` | `Art 24(1) ...` (two), `Art 24(2) ...` (`Duty outcome`), `Art 24(3) ...` | mixed |

Regulative rules (functions with no input or a gate input, result `DEONTIC `Role in the Regulation` `Art N action``): `Art 5(2) the controller must be able to demonstrate compliance with Art 5(1)`, `Art 6(4) the controller must take into account the matters (a) to (e)`, `Art 7(1) ...`, `Art 7(3) the data subject may withdraw consent`, `Art 8(2) ...`, `Art 9(1) the controller shall not process ...` (a SHANT with a breach path), `Art 11(2) ...`, `Art 24(1) ...`, `Art 24(2) ...`.
A later part that wants one shared actor type for its own regulative rules may use `Role in the Regulation`; its action type is its own.

## 4 Seams

**What I read outside my range, and what I saw only from headings.**
I read Articles 1, 2(3) and (4), 3 and the whole of Article 4 (lines 14-73, about 1,800 words) and the first lines of Article 25 (lines 313-315, which a line-range read of Article 24 brought with it): about 1,900 words in all, under the 8,000 allowed.
I saw ONLY from headings: Articles 12 to 23 (so Article 23(1)'s objectives, Article 15 to 20's content), Article 40, Article 42, Article 89 and Chapter IX, Articles 25 to 99.
Every seam to those provisions below is therefore a plain input named for the fact the asking provision needs; none was checked against the answering provision's text.

A part cannot import another part, so the dependent part takes the answer as an INPUT fact named for the answering provision, with the type shown.
Where the answering provision is already in the keel (Art 4 (1), (2), (6), (7), (8)), call it.

### 4.1 Seams P1's own range has (P1 takes each as a plain input)

| asking provision | answering provision | input (name, type) |
| --- | --- | --- |
| Art 6(1)(a), 7(1), 8(1), 9(2)(a) | Art 4(11) 'consent' (K2) | `the data subject has given consent to the processing of his or her personal data` BOOLEAN; Art 9(2)(a) asks `the data subject has given explicit consent to the processing of those personal data` BOOLEAN ("explicit" is a judgment the text leaves to the case) |
| Art 6(1)(f), 8(1) | none: the Regulation does not define 'child' | `the data subject is a child` BOOLEAN; `the information society services are offered directly to a child` BOOLEAN; `the age of the child in complete years` NUMBER |
| Art 8(1) | Art 4(25) 'information society service' (K2) | `the information society services are offered directly to a child` BOOLEAN |
| Art 6(4)(e) | Art 4(5) 'pseudonymisation' (K2) | none: "encryption or pseudonymisation" is an example inside matter (e) and is not read |
| Art 9(1) | Art 4(13) 'genetic data', (14) 'biometric data', (15) 'data concerning health' (K2) | the choice `Art 9(1) category of personal data` (core); K2 may add a function that answers it |
| Art 4(7), 6(1)(c), 6(1)(e), 6(3), 8(1), 9(2)(a), (b), (g), (h), (i), (j), 10 | Union law and Member State law (outside the sources) | plain BOOLEANs named for the attribute of the law, for example `Union or Member State law determines the purposes and means of the processing`, `the basis is laid down by Union law`, `it is on the basis of Union or Member State law`, `that law is proportionate to the aim pursued` |
| Art 2(2)(d) | 'competent authorities' (recital 19 of the uncorrected text names Directive (EU) 2016/680; not among the sources) | `the processing is by a competent authority` BOOLEAN |
| Art 6(4) | Art 23(1) (P2) | `the processing is based on a Union or Member State law which constitutes a necessary and proportionate measure in a democratic society to safeguard the objectives referred to in Article 23(1)` BOOLEAN |
| Art 5(1)(b), 5(1)(e), 9(2)(j) | Art 89(1) (P9) | `the processing is in accordance with Article 89(1)` BOOLEAN |
| Art 24(3) | Art 40 and Art 42 (P4) | `the controller adheres to an approved code of conduct as referred to in Article 40` BOOLEAN; `the controller adheres to an approved certification mechanism as referred to in Article 42` BOOLEAN |
| Art 2(1) and (2) | Art 2(3), Art 2(4), Art 3 (K2) | P1 answers the MATERIAL scope only; K2's "this Regulation applies" takes `Art 2(1) and (2) the processing is within the material scope of this Regulation` (MAYBE BOOLEAN) as an input |
| Art 5(1)(a), 5(1)(c), 5(1)(d), 5(1)(f), 6(1), 9(2) | "lawfully", "fairly", "transparent", "adequate", "relevant", "appropriate", "necessary", "proportionate", "suitable", "reasonable" | plain BOOLEAN facts; the text leaves each to the case (open-textured judgments) |

### 4.2 Seams other parts will have with P1's range (answer to take as an input, with the name to use)

I checked each asking provision below by grepping the consolidated text for the cross-reference (lines given), not by reading the provision whole.

| asking provision (part) | answering provision | input (name, type) |
| --- | --- | --- |
| Art 12(2), Arts 15 to 20 (P2) (lines 149, 206-259) | Art 11(2) | `Art 11(2) Articles 15 to 20 are disapplied` MAYBE BOOLEAN (Art 12(2) says "In the cases referred to in Article 11(2), the controller shall not refuse to act on the request"; P2 decides how to use the answer) |
| Art 13(2)(c), Art 14(2)(d), Art 17(1)(b), Art 20(1)(a) (P2) (lines 173, 192, 229, 256): "based on point (a) of Article 6(1) or point (a) of Article 9(2)" | Art 6(1)(a), Art 9(2)(a) | `the processing is based on point (a) of Article 6(1) or point (a) of Article 9(2)` BOOLEAN; Art 20(1)(a) adds "or on a contract pursuant to point (b) of Article 6(1)": `Art 6(1)(b) point (b) applies: ...` MAYBE BOOLEAN |
| Art 13(1)(d), Art 14(2)(b), Art 21(1) (P2) (lines 167, 190, 265): "based on point (f)" and "(e) or (f) of Article 6(1)" | Art 6(1)(e), (f) | `Art 6(1)(e) point (e) applies: the processing is necessary for a task in the public interest or in the exercise of official authority vested in the controller` MAYBE BOOLEAN; `Art 6(1)(f) point (f) applies: the processing is necessary for legitimate interests that are not overridden` MAYBE BOOLEAN |
| Art 17(1)(f) (P2) (line 233) | Art 8(1), Art 4(25) | `the personal data have been collected in relation to the offer of information society services referred to in Article 8(1)` BOOLEAN |
| Art 17(3)(c) (P2) (line 238): "points (h) and (i) of Article 9(2) as well as Article 9(3)" | Art 9(2)(h), (i), 9(3) | `Art 9(2)(h) point (h) applies: ...`, `Art 9(2)(i) point (i) applies: ...`, `Art 9(3) personal data referred to in paragraph 1 may be processed for the purposes referred to in point (h) of paragraph 2` (each MAYBE BOOLEAN) |
| Art 22(4) (P2) (line 279): "special categories of personal data referred to in Article 9(1), unless point (a) or (g) of Article 9(2) applies" | Art 9(1), 9(2)(a), (g) | `Art 9(1) the categories processed include one that paragraph 1 names` BOOLEAN; `Art 9(2)(a) point (a) applies: ...` and `Art 9(2)(g) point (g) applies: ...` MAYBE BOOLEAN |
| Art 14, 15, 17 and any provision that says "personal data" (P2 and later) | Art 4(1) | call `Art 4(1) the information is personal data` (keel) |
| Art 27(2)(a), Art 35(3)(b), Art 37(1)(c) (P3, P4) (lines 327, 417, 452): special categories and criminal convictions | Art 9(1), Art 10 | `Art 9(1) the categories processed include one that paragraph 1 names` BOOLEAN; for Art 10 data a plain BOOLEAN `the personal data relate to criminal convictions and offences or related security measures` |
| Art 35(10) (P4) (line 429): "processing pursuant to point (c) or (e) of Article 6(1) has a legal basis in Union law or in the law of the Member State"; Art 55(2) (P6) (line 681): "acting on the basis of point (c) or (e) of Article 6(1)" | Art 6(1)(c), (e), Art 6(3) | `Art 6(1)(c) point (c) applies: ...` and `Art 6(1)(e) point (e) applies: ...` MAYBE BOOLEAN; `Art 6(3) the basis for the processing is laid down by Union law or by Member State law to which the controller is subject` MAYBE BOOLEAN |
| any provision that speaks of a controller, a joint controller or a processor (P3 and later) | Art 4(7), 4(8) | call `Art 4(7) the body is a controller`, `Art 4(7) how the body determines the purposes and means`, `Art 4(8) the body is a processor` (keel) |
| Art 83(4)(a) (Articles 8, 11, 25 to 39, 42, 43) and Art 83(5)(a) (Articles 5, 6, 7 and 9) (P9) (lines 989, 993) | each named Article's function | the MAYBE BOOLEAN or `Duty outcome` of the function of Articles 5, 6, 7, 8, 9, 11; an unmet principle is `JUST FALSE` or `the duty arises and is not met`. Article 83 does not name Article 10 or Article 24 (as read at those two lines), so P9 has no input for them |
| any provision about measures or demonstration (P3 and later) | Art 24(1) | `Art 24(1) the controller implements appropriate technical and organisational measures ...` MAYBE BOOLEAN (listed for convenience: no cross-reference to Article 24 was found in the lines grepped) |

## 5 Traps on the stable binary that I met

Loud means the binary stops with an error; silent means it answers wrongly with no error.

- **Silent (met, caught by a test).** On main a one-line `NOT a OR b` reads as `NOT (a OR b)`, with no error: for `a` = FALSE and `b` = TRUE it answers FALSE, where `(NOT a) OR b` answers TRUE (measured on 1.6.112 with a probe).
  My test of Art 9(2)(d) failed because of it, which is how I found it.
  Write `(NOT (a)) OR b`; all `NOT`s in P1's files are parenthesised.
- **Not a trap (measured).** `NOT x EQUALS y` parses with no error and reads as `NOT (x EQUALS y)`: on its own, after a multi-line `AND`, in `IF NOT x EQUALS y THEN ...` on one line, and with enum constructors.
  P1 writes `NOT (x EQUALS y)` anyway.
- **Loud.** A nested `IF ... THEN ... ELSE IF ... THEN ...` fails with `incorrect indentation (got 10, should be greater than 10)` when the inner `THEN` is on its own line at the column of the outer `THEN` and `ELSE IF`.
  It is accepted when the inner `THEN` is indented under the inner `IF`, when `ELSE IF ... THEN ... ELSE ...` is on one line, and with `BRANCH`; P1 uses `BRANCH` with `OTHERWISE`.
- **Silent.** A `#TRACE` result is not an assertion and `check.sh` does not count it: read every trace by eye (P1's traces were read; see NOTES.md).
  A `MUST` with no `WITHIN` never breaches and a trace of it with `(WAITUNTIL 1000)` answers the standing obligation, not `BREACH`; a `SHANT` with no deadline is breached by the act itself.
- **Silent, environment.** `l4 run` prints `Warning | [Import Resolution] Multiple differing copies of module prelude (and daydate)` on this machine because an older copy sits in the XDG data directory; it is not a diagnostic of the module and is not counted by `check.sh`.
- **Loud, fixed by naming.** A name defined in two imported modules cannot be used; P1 avoids it by the labels of section 2.
- **Loud.** A `DEONTIC` value cannot be compared in `#ASSERT` (`eval/unsupported-equality`); assert the gate and trace the rule.
- `IS A` and `IS AN` are interchangeable; `@export` and `@desc` accept a question mark and a colon; a `DECLARE` between two rules is accepted.
- `elem x list` works on enum constructors and gives the list membership P1 uses for the principles and the matters of Art 6(4) and Art 24(1).

## 6 The seat layer

Seats of P1: a data subject `[subject]` (required) and a controller `[controller]`; a joint controller is the same seat as the controller, with the plain input `the body decides them jointly with another body`.
A processor `[processor]` has no P1 question: Art 4(8) is the only provision of the range that addresses it, and it is asked from the controller's seat ("is the body that processes personal data for me a processor") and the data subject's.
There is NEVER a seat for a supervisory authority, the Board, the Commission or a court.
Later parts add `[dpo]`, `[rep]` and `[certbody]`.

Files: `P1-seat-subject.l4` with `P1-cases-seat-subject.l4`; `P1-seat-controller.l4` with `P1-cases-seat-controller.l4`; `P1-cases-mirror.l4` (asserts that the two seats answer the same facts alike).
A later part writes `P2-seat-subject.l4`, `P2-cases-seat-subject.l4` and so on.

Question name and role phrase: every `@export` question and its `DECIDE` name begin `Under Article N, as <role phrase>, ...` (a paragraph: `Under Article 6(1), as ...`), with the role phrases `as a data subject,` `as a controller,` `as a processor,` `as a data protection officer,` `as a representative of a controller or processor not established in the Union,` `as a certification or monitoring body,`.
Questions are grouped under `§§` headings in the text's order.
The name asks the question its body answers, in the same direction: `JUST TRUE` is "yes".

Plain inputs.
An input's name is the layer-1 fact's name, so two questions that ask the same fact share a name and a type.
The `@desc` of each kind of input is:

| kind | `@desc` |
| --- | --- |
| BOOLEAN, controller | `Is it the case, for your processing, that <fact>? Answer true or false.` |
| BOOLEAN, data subject | `As far as you can tell, is it the case that <fact>? Answer true or false.` |
| NUMBER | `What is <fact>? Give a number.` |
| DATE | `On what date: <fact>?` |
| a choice of a core or layer-1 enumeration | `<Fact>: choose exactly one of: <member>; <member>; ...` |
| a yes, no or not sure that a combining rule takes | `<label> Answer P1 controller answer: yes, P1 controller answer: no or P1 controller answer: not sure (not sure is treated as not covered).` (data subject: `P1 subject answer: yes` ...) |

A seat takes a seam input (section 4.1) as such a plain input, with the name the table gives; where a layer-1 rule needs a `MAYBE` or a `LIST`, the seat builds it from plain answers with its helpers (`P1 controller answer as a yes or no`, `P1 controller ways of identification`, `P1 controller age a Member State has provided`, `P1 controller principles shown`, `P1 controller matters of Art 6(4) shown`, `P1 controller matters of Art 24(1) shown`; the same names with `P1 subject`).
The shared inputs that other parts' seats should ask with the same name and type:

| input name | type | seam |
| --- | --- | --- |
| `the data subject has given consent to the processing of his or her personal data` | BOOLEAN | Art 4(11) |
| `the data subject has given explicit consent to the processing of those personal data` | BOOLEAN | Art 4(11), Art 9(2)(a) |
| `the processing is based on consent` | BOOLEAN | Art 6(1)(a) / 9(2)(a) |
| `the data subject is a child` | BOOLEAN | child |
| `the age of the child in complete years` | NUMBER | child |
| `the information society services are offered directly to a child` | BOOLEAN | Art 4(25) |
| `a Member State has provided by law for a lower age` and `the lower age a Member State has provided by law` | BOOLEAN and NUMBER | Art 8(1) |
| `the processing is in accordance with Article 89(1)` | BOOLEAN | Art 89(1) |
| `the processing is by a competent authority` | BOOLEAN | Art 2(2)(d) |
| `the category of the personal data` | choice `Art 9(1) category of personal data` | Art 4(13)-(15) |

## 7 The NOTES sections every part must write

`NOTES.md` has, in this order and with these headings:
`## What is encoded` (scope as provisions; edition; target; binary; the status of the text);
`### Reading a result: FALSE and NOTHING` (in the subject's terms, with the rulings of 2026-11-04 and 2026-11-05 and where this brief and the Guide differ);
`## Seats`;
`## Coverage table` (every provision of the range, one disposition each: encoded / inert / fork / repealed or blank; no `out-of-scope` and no `deferred` row);
`## Fork register` (every reading, the text that licenses it, the one taken);
`## Jural relations` (one row per provision that creates a relation; `none` for a definition or counting rule);
`## Marginal readings for a lawyer` (every branch that rests on a failed "if" as a no, or on a grant or prohibition limited by its own wording as a not-covered);
`## Split sites (your part)` (the count and the answer at each site of the two questions the Guide leaves open);
`## Rules with no breach path (your part)`;
`## What the stable binary does not accept`;
`## What check.sh prints`; `## Findings`; `## Open questions`.
