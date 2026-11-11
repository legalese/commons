# Acts Interpretation Act 1954 (Queensland), encoded in L4

Status: draft.
No domain expert has read this encoding against the text.
The counts and results below were produced by running the files named, on the date given at the foot of this file (2026-11-11).
The jural-relations table, the readings in the fork register and the list of what must be done before the encoding is relied on are the encoder’s judgments; they were not produced by a run, and nothing in this file was checked against the official text.
The text encoded is a plain-text rendering of the Queensland Legislation website’s HTML view, made by a converter script; it is not the official text, and no claim here is that anything was verified against the official text.
The encoding is a single Sonnet 5.5 agent working alone from the brief in `BRIEF.md`.

Target compiler: `main`.
The writing binary is the stable build, 1.6.98 (main, 7689b0d, 2026-10-19), and `check.sh` compared every module with the main build 1.6.110 (main, e51181d, 2026-11-11).

## Seat

The seat is a person who has a time limit to meet under a Queensland Act or statutory instrument (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.
The Act is a set of rules for reading other Acts, and the questions that reach a person most often are the time questions of Part 9 and Schedule 1, so the seat layer puts those first and lets a person state the facts they know: a day, a number of days, months or years, whether the thing to be done is filing or registering a document, and the holidays and closed days of the place.
The seat layer is `qld-seat.l4` (26 questions, each with `@export` and `@desc`) and `qld-cases-seat.l4` (96 assertions).
It imports the layer-1 modules and calls their rules; it builds only the records those rules ask for (a length of a period, the facts about the days of a place) from the answers.
Provisions that address only an official are encoded in layer 1 for what they decide, and appear in the seat layer only where they mean something to the person (for example, when a proclamation brings an Act into force, or when a posted letter is taken to have been served).

## What is encoded, and what is not

Layer 1 is one module per Part, or per natural group of a Part, written in the text’s own order: `qld-part01-preliminary` to `qld-part14-transitional` (Part 8 is in three groups, 8a to 8c; Part 12 is followed by Parts 12A and 12B in `qld-part12a-forms` and `qld-part12b-fee-units`).
Schedule 1 is a table of every defined term, `qld-schedule1-table`, and a module of the terms that turn on a fact, a number or a date, `qld-schedule1-terms`.
The time rules are collected in one self-contained module, `qld-interpretation-time`, which imports only `prelude` and `daydate`, with its own tests in `qld-tests-time`.
The provision index `qld-provisions` (1310 entries) and the cross-reference module `qld-xrefs` are data written by a script that reads the text.
Every module has a test file beside it named `qld-tests-<stem>.l4` (the provision index is tested in `qld-tests-xrefs`); the examples printed in the Act are quoted with `@ref`, in the rule they illustrate or in the test file that exercises them.
A definition is a function or a table entry; a rule of reading is a function over a small typed description of what it operates on, with tests on both sides of each limb.

Not encoded, and why:
- Titles, headings and introductory words are not operative (inert, reason 1).
- The Act’s short title and the regulation-making power are machinery (inert, reason 2).
- Sections shown as repealed or expired, and Schedule 1 entries shown as a term followed by ‘...’, are shown repealed or blank in this text.
- Facts the Act leaves to other instruments are inputs, not encoded: the public holidays, special holidays and bank holidays of a place (Schedule 1, "public holiday" and "business day"), the days an office is closed (s 38(5)(a)), the time at which a letter would be delivered in the ordinary course of post (s 39A(1)(b)), the value of a fee unit (s 48B), and the content of every other Act or instrument the Act cites.
- A period of weeks is not answered: the Act does not define "week" or "day".
- References to other Acts and instruments are rows of their own kind in `qld-xrefs` and are not resolved.

## Jural relations

Hohfeld’s correlatives are used as the brief states them: a right (claim) is matched by a duty, a privilege by a no-right, a power by a liability, an immunity by a disability.
Each relation is stated once, from the side of the holder.
Most of an interpretation Act creates no relation; the single row `none` lists every section of the in-scope text that is not in a row above it.

| Provision | Holder | Other party | L4 rule |
| --- | --- | --- | --- |
| s 5 | any person relying on a rule of this Act (claim) | the Crown (duty to observe this Act) | `this Act binds the person (s 5)` in qld-part01-preliminary |
| s 12(1) | the Crown, or another person (immunity from a “private Act” prejudicing pre-existing rights or imposing liabilities) | a “private Act” (disability) | `a private Act does the thing (s 12)` in qld-part03-general-provisions |
| s 13 | the Crown (immunity from being bound by a later Act, or from derogation from a prerogative right, without express words) | a later Act and whoever would apply it against the Crown (disability) | `the Act binds the Crown or derogates from a prerogative right of the Crown (s 13)` in qld-part03-general-provisions |
| s 13A(1) | holders of native title rights and interests (immunity from a later Act that does not expressly affect them) | a later Act (disability) | `an Act affects native title (s 13A(1))` in qld-part03-general-provisions |
| s 13B(1) | the Legislative Assembly, its members and committees (immunity of their powers, rights and immunities from a later Act that does not expressly affect them) | a later Act (disability) | `an Act affects the powers, rights or immunities of the Legislative Assembly or of its members or committees (s 13B(1))` in qld-part03-general-provisions |
| s 17(1)(c) | the person or body who may exercise a power before the enabling provision commences (power) | the persons the power will bind once the enabling provision commences (liability) | `the power may be exercised (s 17(1)(c))` in qld-part05-commencement |
| s 17(5) | a person on whom a thing done under s 17(1) would otherwise confer a duty before the empowering provision commences (immunity) | the instrument or appointment made under s 17(1) (disability) | `anything done under s 17(1) confers a right or imposes a liability on a person on the day (s 17(5))` in qld-part05-commencement |
| s 20(2)(c) and (d), (4)(b) | a person who acquired a right or privilege, or incurred a liability or penalty, under a repealed or amended Act (immunity) | the repeal or amendment (disability) | `the repeal or amendment of an Act revives or affects the thing (s 20(2) and (4))` in qld-part06-amendment-and-repeal |
| s 20(3) | whoever may start, continue or complete the proceeding, enforce the right or liability, or impose the penalty (privilege) | the person against whom it is done (no-right) | `the step may be taken as if the repeal or amendment had not happened (s 20(3))` in qld-part06-amendment-and-repeal |
| s 20A(2) and (3) | whoever relies on a “saving, transitional or validating effect”, or on a law declared to be one to which s 20A applies (immunity) | the repeal of the Act (disability) | `the declaratory or validating effect of the Act ends merely because of the repeal of the Act (s 20A(2))` in qld-part06-amendment-and-repeal |
| s 20B(2) | a person appointed, or to whom a function or power was delegated, under a provision that is then amended (immunity of the appointment or delegation) | the amendment (disability) | `the appointment, delegation or other thing continues to have effect after the commencement as if it had been done under the amended provision (s 20B(2))` in qld-part06-amendment-and-repeal |
| s 20C(2) and (3) | a person who acted or omitted before the Act commences (immunity from the new offence, or from the increased penalty) | the prosecuting authority (disability) | `the act or omission is an offence under the Act (s 20C(2))` in qld-part06-amendment-and-repeal |
| s 23(1) and (2) | the person or body on whom an Act confers a function or power, or the holder of the specified office (power) | the persons subject to its exercise (liability) | `the function may be performed, or the power may be exercised, as occasion requires (s 23(1))` in qld-part07-functions-and-powers |
| s 23A(1) | the other entity on whom the second power is taken to be conferred (power) | the persons subject to its exercise (liability) | `the provision is taken to confer the second power on the other entity (s 23A(1))` in qld-part07-functions-and-powers |
| s 24AA | whoever may make an instrument or decision (power to amend or repeal it) | the persons the instrument or decision binds (liability) | `the power includes power to amend or repeal the instrument or decision (s 24AA(a))` in qld-part07-functions-and-powers |
| s 24A(1) | the person or body that appoints (power to appoint by name or by the title of an office) | the person appointed (liability) | `the person or body may make the appointment in the way (s 24A(1))` in qld-part07-functions-and-powers |
| s 24B(1) and (3) | the appointer (power to appoint a person to act in an office, and to end or revoke the appointment) | the person appointed to act (liability) | `the person or body may, in accordance with the Act, appoint to act in the office in the way (s 24B(1))` in qld-part07-functions-and-powers |
| s 24B(8) | the person appointed to act (power: all the functions and powers of the holder of the office) | the persons subject to the office’s powers (liability) | `the appointee has all the functions and powers of the holder of the office, and laws apply as if the appointee were the holder (s 24B(8))` in qld-part07-functions-and-powers |
| s 24C(2) | the nominated person while acting (power: all the functions and powers of the office) | the persons subject to the office’s powers (liability) | `the nominated person has all the functions and powers, and laws apply as if the nominated person were the officer or holder of the office (s 24C(2))` in qld-part07-functions-and-powers |
| s 25(1) | the person or body that appoints to an office (power to remove, suspend, appoint to act, reinstate and reappoint) | the person appointed (liability) | `the power of appointment may be exercised as occasion requires (s 25(1)(a))` in qld-part07-functions-and-powers |
| s 26 | a person appointed to an office, to act, to exercise a power or to do anything else (immunity from an appointment’s being treated as ineffective for a “defect or irregularity”) | anyone who would challenge the appointment on that ground (disability) | `the appointment is invalid merely because of a defect or irregularity in relation to the appointment (s 26)` in qld-part07-functions-and-powers |
| s 27 | a person or body authorised to conduct a hearing (power to receive evidence, “to examine witnesses” and to administer oaths) | witnesses lawfully called (liability) | `the person or body has authority (s 27)` in qld-part07-functions-and-powers |
| s 27A(1) and (2) | the person or body that may delegate (power to delegate generally or in a limited way, from time to time, and to revoke) | the delegate (liability) | `the person or body may, in accordance with the Act and any other applicable law, delegate the function or power in the way (s 27A(1))` in qld-part07-functions-and-powers |
| s 27A(10) | the delegator (privilege to perform or exercise the function or power despite the delegation) | the delegate (no-right) | `the delegator may, despite the delegation, perform the function or exercise the power (s 27A(10))` in qld-part07-functions-and-powers |
| s 27A(10A) | whoever the obligation to ensure proper performance is owed to (claim) | the delegator (duty) | `the delegation relieves the delegator of the delegator's obligation to ensure that the function or power is properly performed or exercised (s 27A(10A))` in qld-part07-functions-and-powers |
| s 27B | the person entitled to the written reasons (claim) | the tribunal, authority, body or person making the decision (duty to set out findings on material questions of fact and refer to the evidence) | `the instrument giving the reasons has the content s 27B requires (s 27B)` in qld-part07-functions-and-powers |
| s 32E | the court, tribunal or person to whom the record is to be produced or made available (claim to a document that reproduces the information in a form capable of being understood) | the person who keeps the record by a mechanical, electronic or other device (duty) | `the requirement obliges the person to produce or make available a document reproducing the information in a form capable of being understood (s 32E(c))` in qld-part08a-defined-terms |
| s 39(1) | the person serving a document that an Act requires or permits to be served (privilege to serve in the ways listed) | the person served (no-right to insist on another way) | `the document may be served in the way (s 39(1))` in qld-part10-service-of-documents |
| s 39A(1) | the person serving by post (privilege to serve by posting, with service taken to be effected when the letter would be delivered in the ordinary course of post) | the person served (liability to be treated as served at that time) | `service by post may be effected (s 39A(1)(a))` in qld-part10-service-of-documents |
| s 41 and s 41A | the court (power to punish on conviction up to the specified penalty) | the offender (liability) | `the offence is punishable by the penalty imposed (s 41)` in qld-part11-offences |
| s 42 | any person (privilege and power to take a proceeding for a penalty or forfeiture order) | the offender (no-right, liability) | `any person may take the proceeding (s 42)` in qld-part11-offences |
| s 43(1) and (2) | the party prosecuting, as far as the court orders (claim to part of the amount recovered), and the consolidated fund (claim to the rest) | whoever holds the amount recovered (duty to pay it over) | `the part of the amount paid to the consolidated fund (s 43(1)(b))` in qld-part11-offences |
| s 45(1), first limb | the prosecuting authority (power to prosecute and punish under any of the laws) | the offender (liability) | `the offender may be prosecuted and punished under any of the laws (s 45(1))` in qld-part11-offences |
| s 45(1), second limb | the offender (immunity from being punished more than once for the same offence) | the prosecuting authority (disability) | `the offender may be prosecuted and punished under any of the laws (s 45(1))` in qld-part11-offences |
| s 46 | the prosecuting authority (power to prosecute offences punishable on indictment or summary conviction) | a body corporate (liability) | `the provision applies to the person (s 46)` in qld-part11-offences |
| s 47C(2) | the courts of the State (power: jurisdiction in matters arising under the laws of the State applied to coastal waters) | the persons subject to those proceedings (liability) | `all courts of the State are invested with jurisdiction in the matter (s 47C(2))` in qld-part12-coastal-waters |
| s 48A(1) | the person using a prescribed or approved form (privilege: substantial compliance is enough) | the entity receiving the form (no-right to insist on strict compliance) | `strict compliance with the form is necessary (s 48A(1))` in qld-part12a-forms |
| s 48A(2) | the entity receiving a form that has a requirement about how it is completed (claim) | the person completing the form (duty to comply with the requirement) | `the form is properly completed (s 48A(2))` in qld-part12a-forms |
| s 49 | the entity that requires verification (claim) | the person lodging the document (duty to verify it in the specified way) | `the purpose is fulfilled (s 49)` in qld-part13-miscellaneous |
| s 49A | the court or tribunal in which a provision authorises a proceeding to be instituted (power: jurisdiction) | the parties to the proceeding (liability) | `the provision is taken to confer jurisdiction in the matter on the court or tribunal (s 49A)` in qld-part13-miscellaneous |
| s 50(1) | the empowered entity, and any other entity that approves or disapproves (immunity of their powers from the making or amendment of the subordinate legislation by an Act) | the Act that makes or amends the subordinate legislation (disability) | `the making or amendment affects the power of the empowered entity to amend or further amend the subordinate legislation or to repeal it (s 50(1)(a))` in qld-part13-miscellaneous |
| s 52A(2) | an approving entity (power to authorise a person to issue certificates) | the person authorised (liability) | `an approving entity may authorise a person to issue certificates under subsection (1) for the entity (s 52A(2))` in qld-part13-miscellaneous |
| s 58(2) | the entity that approved a form or made it available (privilege to notify the approval or availability after the commencement) | any person affected by the form (no-right) | `the entity may notify the approval or availability of the form under amended section 48 (s 58(2))` in qld-part14-transitional |
| none | none | none: s 1, s 2, s 4, s 6, s 7, s 9, s 9A, s 10, s 11, s 12A, s 14, s 14A, s 14B, s 14C, s 14CA, s 14D, s 14E, s 14F, s 14G, s 14H, s 14I, s 14J, s 15, s 15A, s 15B, s 15C, s 15D, s 15DA, s 15E, s 17A, s 18, s 19, s 19A, s 21, s 22, s 22A, s 22B, s 22C, s 29, s 29B, s 32, s 32A, s 32AA, s 32AB, s 32B, s 32C, s 32CA, s 32CB, s 32D, s 32DA, s 32F, s 33, s 33AA, s 33AB, s 33AC, s 33A, s 34, s 34A, s 34B, s 35, s 35A, s 35B, s 35C, s 35CA, s 35D, s 35E, s 36, s 37, s 38, s 38A, s 44, s 47, s 47A, s 47B, s 47D, s 47E, s 48, s 48B, s 48C, s 51A, s 52, s 52B, s 53, s 54, s 55, s 56, s 57; the sections shown repealed or expired (s 3, s 8, s 15DB, s 15DC, s 16, s 24, s 28, s 28AA, s 28AB, s 28AC, s 28A, s 29A, s 30, s 32CC, s 35BA, s 35BB, s 40, s 47F, s 47G, s 51); and Schedule 1 | none (these provisions are definitions, counting rules, rules of reading or machinery; their rules are in the modules listed in the coverage table) |

## Coverage table

The coverage table has one row for every title, long title, Part, Division, Schedule heading, section, subsection, paragraph, subparagraph, sub-subparagraph, defined term and example of the in-scope text (lines 10 to 1490 of `act-1954-003.txt`), 1283 rows in all.
Each row has exactly one disposition: `encoded`, `inert`, `fork` or `repealed or blank in this text`.
The rows were written by a script that reads the text file (kept outside the deposit); the `Where` column gives the module and the line of the `@ref` that covers the row’s first line.
The tests of each module are in the test file beside it (`qld-tests-<stem>.l4`); the table does not link a row to a single assertion.
A row marked `encoded` for an example says in which test file the example is quoted.

The script check: of 1481 non-blank lines in lines 10 to 1490, 0 fall in no row and 0 fall in more than one row.
Dispositions: encoded 1047, fork 56, inert 94, repealed or blank in this text 86.
Rows by kind: def 52, division 3, example 43, longtitle 1, paragraph 391, part 16, sched_def 308, schedule 1, section 144, subparagraph 39, subsection 279, subsubparagraph 5, title 1.

| Row | Lines | Disposition | Where |
| --- | --- | --- | --- |
| title | 10 | inert | not operative: the title |
| long title | 11 | inert | not operative: the long title |
| Part 1 heading | 12 | inert | not operative: Part heading |
| s 1 | 13-14 | inert | machinery: short title: the Act’s citation |
| s 2 | 15-16 | encoded | qld-part01-preliminary:14 |
| s 2, example | 17-18 | encoded | qld-part01-preliminary:24 |
| s 3 | 19 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 4 | 20-21 | encoded | qld-part01-preliminary:39 |
| s 5 | 22-23 | encoded | qld-part01-preliminary:54 |
| Part 2 heading | 24 | inert | not operative: Part heading |
| s 6 heading | 25 | inert | not operative: section heading (the rules are in its subsections) |
| s 6(1) | 26-27 | encoded | qld-part02-meaning-of-act:16 |
| s 6(1)(a) | 28 | encoded | qld-part02-meaning-of-act:16 |
| s 6(1)(b) | 29 | encoded | qld-part02-meaning-of-act:16 |
| s 6(2) | 30 | encoded | qld-part02-meaning-of-act:28 |
| s 7 heading | 31 | inert | not operative: section heading (the rules are in its subsections) |
| s 7(1) | 32 | encoded | qld-part02-meaning-of-act:38 |
| s 7(2) | 33-34 | encoded | qld-part02-meaning-of-act:47 |
| s 8 | 35 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| Part 3 heading | 36 | inert | not operative: Part heading |
| s 9 heading | 37 | inert | not operative: section heading (the rules are in its subsections) |
| s 9(1) | 38 | encoded | qld-part03-general-provisions:15 |
| s 9(1)(a) | 39 | encoded | qld-part03-general-provisions:15 |
| s 9(1)(b) | 40 | encoded | qld-part03-general-provisions:15 |
| s 9(1A) | 41 | encoded | qld-part03-general-provisions:33 |
| s 9(1B) | 42 | encoded | qld-part03-general-provisions:40 |
| s 9(2) | 43 | encoded | qld-part03-general-provisions:50 |
| s 9(2)(a) | 44 | encoded | qld-part03-general-provisions:50 |
| s 9(2)(b) | 45 | encoded | qld-part03-general-provisions:50 |
| s 9(3) | 46 | encoded | qld-part03-general-provisions:67 |
| s 9(4) | 47 | encoded | qld-part03-general-provisions:74 |
| s 9A | 48-49 | encoded | qld-part03-general-provisions:83 |
| s 10 | 50-51 | encoded | qld-part03-general-provisions:90 |
| s 11 | 52-53 | fork | F1; qld-part03-general-provisions:100 |
| s 12 heading | 54 | inert | not operative: section heading (the rules are in its subsections) |
| s 12(1) | 55 | fork | F2; qld-part03-general-provisions:125 |
| s 12(1)(a) | 56 | fork | F2; qld-part03-general-provisions:125 |
| s 12(1)(b) | 57-58 | fork | F2; qld-part03-general-provisions:125 |
| s 12(2) | 59 | fork | F2; qld-part03-general-provisions:129 |
| s 12(2)(a) | 60 | fork | F2; qld-part03-general-provisions:129 |
| s 12(2)(b) | 61 | fork | F2; qld-part03-general-provisions:129 |
| s 12A | 62-63 | encoded | qld-part03-general-provisions:147 |
| s 13 | 64-65 | encoded | qld-part03-general-provisions:158 |
| s 13A heading | 66 | inert | not operative: section heading (the rules are in its subsections) |
| s 13A(1) | 67 | encoded | qld-part03-general-provisions:169 |
| s 13A(2) | 68 | encoded | qld-part03-general-provisions:178 |
| s 13B heading | 69 | inert | not operative: section heading (the rules are in its subsections) |
| s 13B(1) | 70 | encoded | qld-part03-general-provisions:187 |
| s 13B(2) | 71 | encoded | qld-part03-general-provisions:195 |
| s 13B(3) | 72 | encoded | qld-part03-general-provisions:204 |
| s 13B(3), definition rights | 73 | encoded | qld-part03-general-provisions:204 |
| s 14 heading | 74 | inert | not operative: section heading (the rules are in its subsections) |
| s 14(1) | 75 | encoded | qld-part03-general-provisions:223 |
| s 14(2) | 76 | encoded | qld-part03-general-provisions:227 |
| s 14(2)(a) | 77 | encoded | qld-part03-general-provisions:227 |
| s 14(2)(b) | 78 | encoded | qld-part03-general-provisions:227 |
| s 14(3) | 79 | encoded | qld-part03-general-provisions:229 |
| s 14(4) | 80 | encoded | qld-part03-general-provisions:235 |
| s 14(4), example | 81-82 | encoded | qld-part03-general-provisions:235 |
| s 14(4), example 2 | 83-84 | encoded | qld-part03-general-provisions:235 |
| s 14(5) | 85 | encoded | qld-part03-general-provisions:237 |
| s 14(6) | 86 | encoded | qld-part03-general-provisions:239 |
| s 14(7) | 87 | encoded | qld-part03-general-provisions:241 |
| s 14A heading | 88 | inert | not operative: section heading (the rules are in its subsections) |
| s 14A(1) | 89 | encoded | qld-part03-general-provisions:261 |
| s 14A(2) | 90 | encoded | qld-part03-general-provisions:268 |
| s 14A(3) | 91 | encoded | qld-part03-general-provisions:281 |
| s 14A(3), example | 92-93 | encoded | qld-part03-general-provisions:281 |
| s 14B heading | 94 | inert | not operative: section heading (the rules are in its subsections) |
| s 14B(1) | 95 | fork | F3; qld-part03-general-provisions:302 |
| s 14B(1)(a) | 96 | fork | F3; qld-part03-general-provisions:302 |
| s 14B(1)(b) | 97 | fork | F3; qld-part03-general-provisions:302 |
| s 14B(1)(c) | 98 | fork | F3; qld-part03-general-provisions:302 |
| s 14B(2) | 99 | encoded | qld-part03-general-provisions:327 |
| s 14B(2)(a) | 100 | encoded | qld-part03-general-provisions:327 |
| s 14B(2)(b) | 101 | encoded | qld-part03-general-provisions:327 |
| s 14B(2)(c) | 102 | encoded | qld-part03-general-provisions:327 |
| s 14B(3) | 103 | fork | F4; qld-part03-general-provisions:351 |
| s 14B(3), definition extrinsic material | 104 | fork | F4; qld-part03-general-provisions:351 |
| s 14B(3)(a) | 105 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(b) | 106 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(c) | 107 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(d) | 108 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(e) | 109 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(f) | 110 | encoded | qld-part03-general-provisions:368 |
| s 14B(3), definition extrinsic material, example | 111-112 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(g) | 113 | encoded | qld-part03-general-provisions:368 |
| s 14B(3)(h) | 114 | encoded | qld-part03-general-provisions:368 |
| s 14B(3), definition ordinary meaning | 115 | encoded | qld-part03-general-provisions:377 |
| s 14C | 116-117 | encoded | qld-part03-general-provisions:392 |
| s 14C(a) | 118 | encoded | qld-part03-general-provisions:392 |
| s 14C(b) | 119 | encoded | qld-part03-general-provisions:392 |
| s 14C(b)(i) | 120 | encoded | qld-part03-general-provisions:392 |
| s 14C(b)(ii) | 121-122 | encoded | qld-part03-general-provisions:392 |
| s 14CA heading | 123 | inert | not operative: section heading (the rules are in its subsections) |
| s 14CA(1) | 124 | encoded | qld-part03-general-provisions:406 |
| s 14CA(1)(a) | 125 | encoded | qld-part03-general-provisions:406 |
| s 14CA(1)(b) | 126-127 | encoded | qld-part03-general-provisions:406 |
| s 14CA(2) | 128 | encoded | qld-part03-general-provisions:420 |
| s 14CA(2)(a) | 129 | encoded | qld-part03-general-provisions:420 |
| s 14CA(2)(b) | 130-131 | encoded | qld-part03-general-provisions:420 |
| s 14CA(3) | 132 | fork | F5; qld-part03-general-provisions:436 |
| s 14CA(3)(a) | 133 | fork | F5; qld-part03-general-provisions:436 |
| s 14CA(3)(b) | 134 | fork | F5; qld-part03-general-provisions:436 |
| s 14CA(3)(c) | 135 | fork | F5; qld-part03-general-provisions:436 |
| s 14CA(4) | 136 | encoded | qld-part03-general-provisions:450 |
| s 14CA(4), definition corresponding provision | 137 | encoded | qld-part03-general-provisions:450 |
| s 14D | 138-139 | encoded | qld-part03-general-provisions:465 |
| s 14D(a) | 140 | encoded | qld-part03-general-provisions:465 |
| s 14D(b) | 141 | encoded | qld-part03-general-provisions:465 |
| s 14D(c) | 142 | encoded | qld-part03-general-provisions:465 |
| Part 4 heading | 143 | inert | not operative: Part heading |
| s 14E | 144-145 | encoded | qld-part04-references:11 |
| s 14F heading | 146 | inert | not operative: section heading (the rules are in its subsections) |
| s 14F(1) | 147 | fork | F6; qld-part04-references:29 |
| s 14F(1)(a) | 148 | fork | F6; qld-part04-references:29 |
| s 14F(1)(b) | 149 | fork | F6; qld-part04-references:29 |
| s 14F(1), example | 150-154 | fork | F7; qld-tests-part04:26 |
| s 14F(2) | 155 | encoded | qld-part04-references:42 |
| s 14F(2)(a) | 156 | encoded | qld-part04-references:42 |
| s 14F(2)(b) | 157-158 | encoded | qld-part04-references:42 |
| s 14F(3) | 159 | encoded | qld-part04-references:55 |
| s 14F(3)(a) | 160 | encoded | qld-part04-references:55 |
| s 14F(3)(b) | 161-162 | encoded | qld-part04-references:55 |
| s 14F(4) | 163 | encoded | qld-part04-references:75 |
| s 14F(4)(a) | 164 | encoded | qld-part04-references:75 |
| s 14F(4)(b) | 165-166 | encoded | qld-part04-references:75 |
| s 14G heading | 167 | inert | not operative: section heading (the rules are in its subsections) |
| s 14G(1) | 168 | encoded | qld-part04-references:87 |
| s 14G(2) | 169 | fork | F8; qld-part04-references:102 |
| s 14G(2)(a) | 170 | fork | F8; qld-part04-references:102 |
| s 14G(2)(b) | 171 | fork | F8; qld-part04-references:102 |
| s 14G(3) | 172 | encoded | qld-part04-references:121 |
| s 14G(3), definition Act | 173 | encoded | qld-part04-references:121 |
| s 14G(3), definition enactment | 174 | encoded | qld-part04-references:130 |
| s 14G(3), definition official copy | 175 | encoded | qld-part04-references:139 |
| s 14G(3)(a) | 176 | encoded | qld-part04-references:139 |
| s 14G(3)(b) | 177 | encoded | qld-part04-references:146 |
| s 14H heading | 178 | inert | not operative: section heading (the rules are in its subsections) |
| s 14H(1) | 179 | encoded | qld-part04-references:169 |
| s 14H(1)(a) | 180 | encoded | qld-part04-references:169 |
| s 14H(1)(b) | 181 | encoded | qld-part04-references:169 |
| s 14H(1)(c) | 182 | encoded | qld-part04-references:169 |
| s 14H(2) | 183 | encoded | qld-part04-references:189 |
| s 14H(2)(a) | 184 | encoded | qld-part04-references:189 |
| s 14H(2)(b) | 185 | encoded | qld-part04-references:189 |
| s 14H(3) | 186 | encoded | qld-part04-references:203 |
| s 14H(3), definition law | 187 | encoded | qld-part04-references:203 |
| s 14H(3), definition make | 188 | encoded | qld-part04-references:214 |
| s 14I heading | 189 | inert | not operative: section heading (the rules are in its subsections) |
| s 14I(1) | 190 | encoded | qld-part04-references:223 |
| s 14I(2) | 191 | encoded | qld-part04-references:231 |
| s 14I(2), definition law | 192 | encoded | qld-part04-references:231 |
| s 14J heading | 193 | inert | not operative: section heading (the rules are in its subsections) |
| s 14J(1) | 194 | encoded | qld-part04-references:249 |
| s 14J(1), example | 195-196 | encoded | qld-part04-references:249 |
| s 14J(2) | 197 | encoded | qld-part04-references:259 |
| s 14J(2), definition law | 198 | encoded | qld-part04-references:259 |
| Part 5 heading | 199 | inert | not operative: Part heading |
| s 15 | 200-201 | encoded | qld-part05-commencement:15 |
| s 15A | 202-203 | encoded | qld-interpretation-time:72 |
| s 15B | 204-205 | encoded | qld-interpretation-time:83 |
| s 15C heading | 206 | inert | not operative: section heading (the rules are in its subsections) |
| s 15C(1) | 207 | encoded | qld-interpretation-time:90 |
| s 15C(2) | 208 | encoded | qld-part05-commencement:34 |
| s 15C(2)(a) | 209 | encoded | qld-part05-commencement:34 |
| s 15C(2)(b) | 210 | encoded | qld-part05-commencement:34 |
| s 15C(2)(c) | 211 | encoded | qld-part05-commencement:34 |
| s 15C(3) | 212 | fork | F9; qld-part05-commencement:48 |
| s 15C(4) | 213 | encoded | qld-part05-commencement:55 |
| s 15D heading | 214 | inert | not operative: section heading (the rules are in its subsections) |
| s 15D(1) | 215 | encoded | qld-part05-commencement:71 |
| s 15D(1)(a) | 216 | encoded | qld-part05-commencement:71 |
| s 15D(1)(b) | 217 | encoded | qld-part05-commencement:71 |
| s 15D(2) | 218 | encoded | qld-part05-commencement:84 |
| s 15D(2)(a) | 219 | encoded | qld-part05-commencement:84 |
| s 15D(2)(b) | 220 | encoded | qld-interpretation-time:103 |
| s 15DA heading | 221 | inert | not operative: section heading (the rules are in its subsections) |
| s 15DA(1) | 222 | encoded | qld-interpretation-time:160 |
| s 15DA(1), definition assent day | 223 | encoded | qld-part05-commencement:96 |
| s 15DA(1)(a) | 224 | encoded | qld-part05-commencement:96 |
| s 15DA(1)(b) | 225 | encoded | qld-part05-commencement:96 |
| s 15DA(1), definition postponed law | 226 | encoded | qld-part05-commencement:105 |
| s 15DA(2) | 227 | encoded | qld-interpretation-time:160 |
| s 15DA(3) | 228 | encoded | qld-interpretation-time:160 |
| s 15DA(4) | 229 | encoded | qld-part05-commencement:124 |
| s 15DA(4)(a) | 230 | encoded | qld-part05-commencement:124 |
| s 15DA(4)(b) | 231 | encoded | qld-part05-commencement:124 |
| s 15DA(4)(c) | 232-233 | encoded | qld-part05-commencement:124 |
| s 15DA(5) | 234 | encoded | qld-interpretation-time:160 |
| s 15DA(5)(a) | 235 | encoded | qld-interpretation-time:160 |
| s 15DA(5)(b) | 236 | encoded | qld-interpretation-time:160 |
| s 15DA(5), example | 237-238 | encoded | qld-interpretation-time:160 |
| s 15DB | 239 | repealed or blank in this text | the text shows the heading ‘[Expired]’ and no text |
| s 15DC | 240 | repealed or blank in this text | the text shows the heading ‘[Expired]’ and no text |
| s 15E | 241-242 | encoded | qld-part05-commencement:138 |
| s 15E(a) | 243 | encoded | qld-part05-commencement:138 |
| s 15E(b) | 244-245 | encoded | qld-part05-commencement:138 |
| s 16 | 246 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 17 heading | 247 | inert | not operative: section heading (the rules are in its subsections) |
| s 17(1) | 248 | encoded | qld-part05-commencement:164 |
| s 17(1)(a) | 249 | encoded | qld-part05-commencement:164 |
| s 17(1)(a)(i) | 250 | encoded | qld-part05-commencement:164 |
| s 17(1)(a)(ii) | 251 | encoded | qld-part05-commencement:164 |
| s 17(1)(a)(iii) | 252 | encoded | qld-part05-commencement:164 |
| s 17(1)(b) | 253-254 | encoded | qld-part05-commencement:164 |
| s 17(1)(c) | 255 | encoded | qld-part05-commencement:164 |
| s 17(1)(d) | 256 | encoded | qld-part05-commencement:164 |
| s 17(1)(d)(i) | 257 | encoded | qld-part05-commencement:164 |
| s 17(1)(d)(ii) | 258-259 | encoded | qld-part05-commencement:164 |
| s 17(2) | 260 | encoded | qld-part05-commencement:213 |
| s 17(2)(a) | 261 | encoded | qld-part05-commencement:213 |
| s 17(2)(b) | 262-263 | encoded | qld-part05-commencement:213 |
| s 17(2)(c) | 264 | encoded | qld-part05-commencement:213 |
| s 17(2)(d) | 265 | encoded | qld-part05-commencement:213 |
| s 17(3) | 266 | fork | F10; qld-part05-commencement:253 |
| s 17(3)(a) | 267 | fork | F10; qld-part05-commencement:253 |
| s 17(3)(b) | 268-269 | fork | F10; qld-part05-commencement:253 |
| s 17(3)(c) | 270 | fork | F10; qld-part05-commencement:253 |
| s 17(3)(d) | 271 | fork | F10; qld-part05-commencement:253 |
| s 17(4) | 272 | encoded | qld-part05-commencement:268 |
| s 17(4)(a) | 273 | encoded | qld-part05-commencement:268 |
| s 17(4)(b) | 274-275 | encoded | qld-part05-commencement:268 |
| s 17(4)(c) | 276 | encoded | qld-part05-commencement:268 |
| s 17(4)(d) | 277 | encoded | qld-part05-commencement:268 |
| s 17(5) | 278 | encoded | qld-part05-commencement:278 |
| s 17(6) | 279 | encoded | qld-part05-commencement:293 |
| Part 6 heading | 280 | inert | not operative: Part heading |
| s 17A | 281-282 | encoded | qld-part06-amendment-and-repeal:12 |
| s 18 | 283-284 | encoded | qld-interpretation-time:117 |
| s 18(a) | 285 | encoded | qld-interpretation-time:117 |
| s 18(b) | 286-287 | encoded | qld-interpretation-time:117 |
| s 19 heading | 288 | inert | not operative: section heading (the rules are in its subsections) |
| s 19(1) | 289 | encoded | qld-part06-amendment-and-repeal:22 |
| s 19(1), definition Act | 290 | encoded | qld-part06-amendment-and-repeal:22 |
| s 19(1), definition repeal | 291 | encoded | qld-part06-amendment-and-repeal:29 |
| s 19(2) | 292 | encoded | qld-part06-amendment-and-repeal:37 |
| s 19(2), example | 293-295 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:28 |
| s 19(3) | 296 | encoded | qld-part06-amendment-and-repeal:47 |
| s 19(3), example | 297-299 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:41 |
| s 19(4) | 300 | encoded | qld-part06-amendment-and-repeal:63 |
| s 19A | 301-302 | encoded | qld-part06-amendment-and-repeal:70 |
| s 20 heading | 303 | inert | not operative: section heading (the rules are in its subsections) |
| s 20(1) | 304 | encoded | qld-part06-amendment-and-repeal:82 |
| s 20(1), definition Act | 305 | encoded | qld-part06-amendment-and-repeal:82 |
| s 20(1), definition repeal | 306 | encoded | qld-part06-amendment-and-repeal:89 |
| s 20(2) | 307 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(2)(a) | 308 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(2)(b) | 309 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(2)(c) | 310 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(2)(d) | 311 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(2)(e) | 312 | encoded | qld-part06-amendment-and-repeal:115 |
| s 20(3) | 313 | encoded | qld-part06-amendment-and-repeal:138 |
| s 20(4) | 314 | encoded | qld-part06-amendment-and-repeal:121 |
| s 20(4)(a) | 315 | encoded | qld-part06-amendment-and-repeal:121 |
| s 20(4)(b) | 316 | encoded | qld-part06-amendment-and-repeal:121 |
| s 20(4)(c) | 317 | encoded | qld-part06-amendment-and-repeal:121 |
| s 20(4)(d) | 318 | encoded | qld-part06-amendment-and-repeal:121 |
| s 20(5) | 319 | encoded | qld-part06-amendment-and-repeal:150 |
| s 20A heading | 320 | inert | not operative: section heading (the rules are in its subsections) |
| s 20A(1) | 321 | encoded | qld-part06-amendment-and-repeal:158 |
| s 20A(1), definition Act | 322 | encoded | qld-part06-amendment-and-repeal:158 |
| s 20A(1), definition repeal | 323 | encoded | qld-part06-amendment-and-repeal:165 |
| s 20A(2) | 324 | encoded | qld-part06-amendment-and-repeal:182 |
| s 20A(2)(a) | 325 | encoded | qld-part06-amendment-and-repeal:182 |
| s 20A(2)(b) | 326 | encoded | qld-part06-amendment-and-repeal:182 |
| s 20A(2)(c) | 327-328 | encoded | qld-part06-amendment-and-repeal:182 |
| s 20A(2), example | 329-330 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:92 |
| s 20A(2), example 2 | 331-332 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:92 |
| s 20A(2), example 3 | 333-335 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:92 |
| s 20A(3) | 336 | encoded | qld-part06-amendment-and-repeal:197 |
| s 20A(3)(a) | 337 | encoded | qld-part06-amendment-and-repeal:197 |
| s 20A(3)(b) | 338 | encoded | qld-part06-amendment-and-repeal:197 |
| s 20A(4) | 339 | encoded | qld-part06-amendment-and-repeal:205 |
| s 20A(5) | 340 | encoded | qld-part06-amendment-and-repeal:211 |
| s 20A(6) | 341 | encoded | qld-part06-amendment-and-repeal:218 |
| s 20B heading | 342 | inert | not operative: section heading (the rules are in its subsections) |
| s 20B(1) | 343 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(a) | 344 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(a)(i) | 345 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(a)(ii) | 346 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(a)(iii) | 347 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(b) | 348 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(c) | 349 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(c)(i) | 350 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(c)(ii) | 351 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(1)(c)(iii) | 352 | encoded | qld-part06-amendment-and-repeal:236 |
| s 20B(2) | 353 | encoded | qld-part06-amendment-and-repeal:249 |
| s 20B(3) | 354 | encoded | qld-part06-amendment-and-repeal:265 |
| s 20B(3), definition amend | 355 | encoded | qld-part06-amendment-and-repeal:265 |
| s 20C heading | 356 | inert | not operative: section heading (the rules are in its subsections) |
| s 20C(1) | 357 | encoded | qld-part06-amendment-and-repeal:279 |
| s 20C(1), definition Act | 358 | encoded | qld-part06-amendment-and-repeal:279 |
| s 20C(2) | 359 | encoded | qld-part06-amendment-and-repeal:287 |
| s 20C(3) | 360 | encoded | qld-part06-amendment-and-repeal:297 |
| s 21 | 361-362 | encoded | qld-part06-amendment-and-repeal:310 |
| s 22 | 363-364 | encoded | qld-part06-amendment-and-repeal:320 |
| s 22A heading | 365 | inert | not operative: section heading (the rules are in its subsections) |
| s 22A(1) | 366 | encoded | qld-part06-amendment-and-repeal:347 |
| s 22A(2) | 367 | encoded | qld-part06-amendment-and-repeal:349 |
| s 22A(3) | 368 | encoded | qld-part06-amendment-and-repeal:351 |
| s 22A(4) | 369 | encoded | qld-part06-amendment-and-repeal:353 |
| s 22A(5) | 370 | encoded | qld-part06-amendment-and-repeal:355 |
| s 22A(6) | 371 | encoded | qld-part06-amendment-and-repeal:357 |
| s 22A(7) | 372 | encoded | qld-part06-amendment-and-repeal:359 |
| s 22A(8) | 373 | encoded | qld-part06-amendment-and-repeal:377 |
| s 22B | 374-375 | encoded | qld-part06-amendment-and-repeal:394 |
| s 22B(a) | 376 | encoded | qld-part06-amendment-and-repeal:394 |
| s 22B(b) | 377 | encoded | qld-part06-amendment-and-repeal:394 |
| s 22B(c) | 378-379 | encoded | qld-part06-amendment-and-repeal:394 |
| s 22C heading | 380 | inert | not operative: section heading (the rules are in its subsections) |
| s 22C(1) | 381 | encoded | qld-interpretation-time:126 |
| s 22C(2) | 382 | encoded | qld-part06-amendment-and-repeal:406 |
| s 22C(3) | 383 | encoded | qld-part06-amendment-and-repeal:413 |
| s 22C(4) | 384 | inert | not operative: introductory words or a caption (the rules are in the rows that follow) |
| s 22C(4), definition amending Act | 385 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(a) | 386 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(b) | 387 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(c) | 388 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(d) | 389 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(e) | 390 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(f) | 391 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4)(g) | 392 | encoded | qld-part06-amendment-and-repeal:436 |
| s 22C(4), definition amending Act, example | 393-401 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:171 |
| s 22C(4), definition amending Act, example 2 | 402-403 | encoded | example, quoted in qld-tests-part06; qld-tests-part06:176 |
| s 22C(4), definition assent day | 404 | encoded | qld-part06-amendment-and-repeal:445 |
| s 22C(4)(a) | 405 | encoded | qld-part06-amendment-and-repeal:445 |
| s 22C(4)(b) | 406 | encoded | qld-part06-amendment-and-repeal:445 |
| Part 7 heading | 407 | inert | not operative: Part heading |
| s 23 heading | 408 | inert | not operative: section heading (the rules are in its subsections) |
| s 23(1) | 409 | encoded | qld-part07-functions-and-powers:14 |
| s 23(2) | 410 | encoded | qld-part07-functions-and-powers:21 |
| s 23(3) | 411 | encoded | qld-part07-functions-and-powers:31 |
| s 23A heading | 412 | inert | not operative: section heading (the rules are in its subsections) |
| s 23A(1) | 413 | encoded | qld-part07-functions-and-powers:39 |
| s 23A(2) | 414 | encoded | qld-part07-functions-and-powers:50 |
| s 23A(2), definition power | 415 | encoded | qld-part07-functions-and-powers:50 |
| s 24 | 416 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 24AA | 417-418 | encoded | qld-part07-functions-and-powers:60 |
| s 24AA(a) | 419 | encoded | qld-part07-functions-and-powers:60 |
| s 24AA(b) | 420 | encoded | qld-part07-functions-and-powers:67 |
| s 24A heading | 421 | inert | not operative: section heading (the rules are in its subsections) |
| s 24A(1) | 422 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(1)(a) | 423 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(1)(b) | 424 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(1)(c) | 425-426 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(1)(d) | 427 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(1)(e) | 428 | encoded | qld-part07-functions-and-powers:85 |
| s 24A(2) | 429 | encoded | qld-part07-functions-and-powers:97 |
| s 24B heading | 430 | inert | not operative: section heading (the rules are in its subsections) |
| s 24B(1) | 431 | encoded | qld-part07-functions-and-powers:109 |
| s 24B(1)(a) | 432 | encoded | qld-part07-functions-and-powers:109 |
| s 24B(1)(b) | 433-434 | encoded | qld-part07-functions-and-powers:109 |
| s 24B(2) | 435 | encoded | qld-part07-functions-and-powers:121 |
| s 24B(3) | 436 | encoded | qld-part07-functions-and-powers:135 |
| s 24B(3)(a) | 437 | encoded | qld-part07-functions-and-powers:135 |
| s 24B(3)(b) | 438 | encoded | qld-part07-functions-and-powers:135 |
| s 24B(3A) | 439 | encoded | qld-part07-functions-and-powers:144 |
| s 24B(4) | 440 | encoded | qld-part07-functions-and-powers:153 |
| s 24B(5) | 441 | encoded | qld-interpretation-time:471 |
| s 24B(5)(a) | 442 | encoded | qld-interpretation-time:471 |
| s 24B(5)(b) | 443 | encoded | qld-interpretation-time:471 |
| s 24B(6) | 444 | encoded | qld-interpretation-time:483 |
| s 24B(6)(a) | 445 | encoded | qld-interpretation-time:483 |
| s 24B(6)(b) | 446 | encoded | qld-interpretation-time:483 |
| s 24B(6)(c) | 447-448 | encoded | qld-interpretation-time:483 |
| s 24B(6A) | 449 | encoded | qld-part07-functions-and-powers:182 |
| s 24B(7) | 450 | encoded | qld-part07-functions-and-powers:187 |
| s 24B(7A) | 451 | encoded | qld-part07-functions-and-powers:195 |
| s 24B(7B) | 452 | encoded | qld-part07-functions-and-powers:203 |
| s 24B(7C) | 453 | encoded | qld-part07-functions-and-powers:211 |
| s 24B(7D) | 454 | encoded | qld-part07-functions-and-powers:217 |
| s 24B(7E) | 455 | encoded | qld-part07-functions-and-powers:224 |
| s 24B(8) | 456 | encoded | qld-part07-functions-and-powers:231 |
| s 24B(8)(a) | 457 | encoded | qld-part07-functions-and-powers:231 |
| s 24B(8)(b) | 458 | encoded | qld-part07-functions-and-powers:231 |
| s 24B(9) | 459 | encoded | qld-part07-functions-and-powers:247 |
| s 24B(9)(a) | 460 | encoded | qld-part07-functions-and-powers:247 |
| s 24B(9)(b) | 461 | encoded | qld-part07-functions-and-powers:247 |
| s 24B(9)(c) | 462 | encoded | qld-part07-functions-and-powers:247 |
| s 24B(10) | 463 | encoded | qld-part07-functions-and-powers:259 |
| s 24B(11) | 464 | encoded | qld-part07-functions-and-powers:272 |
| s 24B(11)(a) | 465 | encoded | qld-part07-functions-and-powers:272 |
| s 24B(11)(b) | 466-467 | encoded | qld-part07-functions-and-powers:272 |
| s 24B(11)(c) | 468 | encoded | qld-part07-functions-and-powers:272 |
| s 24B(11)(d) | 469 | encoded | qld-part07-functions-and-powers:272 |
| s 24B(12) | 470 | encoded | qld-part07-functions-and-powers:287 |
| s 24B(12)(a) | 471 | encoded | qld-part07-functions-and-powers:287 |
| s 24B(12)(b) | 472-473 | encoded | qld-part07-functions-and-powers:287 |
| s 24B(12)(c) | 474 | encoded | qld-part07-functions-and-powers:287 |
| s 24B(12)(d) | 475 | encoded | qld-part07-functions-and-powers:287 |
| s 24B(13) | 476 | encoded | qld-part07-functions-and-powers:295 |
| s 24B(14) | 477 | encoded | qld-part07-functions-and-powers:302 |
| s 24B(15) | 478 | fork | F11; qld-part07-functions-and-powers:314 |
| s 24C heading | 479 | inert | not operative: section heading (the rules are in its subsections) |
| s 24C(1) | 480 | encoded | qld-part07-functions-and-powers:324 |
| s 24C(2) | 481 | encoded | qld-part07-functions-and-powers:333 |
| s 24C(2)(a) | 482 | encoded | qld-part07-functions-and-powers:333 |
| s 24C(2)(b) | 483 | encoded | qld-part07-functions-and-powers:333 |
| s 24C(3) | 484 | encoded | qld-part07-functions-and-powers:341 |
| s 25 heading | 485 | inert | not operative: section heading (the rules are in its subsections) |
| s 25(1) | 486 | encoded | qld-part07-functions-and-powers:382 |
| s 25(1)(a) | 487 | encoded | qld-part07-functions-and-powers:382 |
| s 25(1)(b) | 488 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(b)(i) | 489 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(b)(ii) | 490 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(b)(iii) | 491 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(b)(iv) | 492 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(b)(v) | 493 | encoded | qld-part07-functions-and-powers:369 |
| s 25(1)(c) | 494 | encoded | qld-part07-functions-and-powers:389 |
| s 25(2) | 495 | encoded | qld-part07-functions-and-powers:397 |
| s 25(3) | 496 | encoded | qld-part07-functions-and-powers:403 |
| s 25(4) | 497 | encoded | qld-part07-functions-and-powers:408 |
| s 26 | 498-499 | encoded | qld-part07-functions-and-powers:421 |
| s 27 | 500-501 | encoded | qld-part07-functions-and-powers:436 |
| s 27(a) | 502 | encoded | qld-part07-functions-and-powers:436 |
| s 27(b) | 503 | encoded | qld-part07-functions-and-powers:436 |
| s 27A heading | 504 | inert | not operative: section heading (the rules are in its subsections) |
| s 27A(1) | 505 | encoded | qld-part07-functions-and-powers:457 |
| s 27A(1)(a) | 506 | encoded | qld-part07-functions-and-powers:457 |
| s 27A(1)(b) | 507 | encoded | qld-part07-functions-and-powers:457 |
| s 27A(2) | 508 | encoded | qld-part07-functions-and-powers:479 |
| s 27A(2)(a) | 509 | encoded | qld-part07-functions-and-powers:479 |
| s 27A(2)(b) | 510 | encoded | qld-part07-functions-and-powers:479 |
| s 27A(2)(c) | 511 | encoded | qld-part07-functions-and-powers:479 |
| s 27A(3) | 512 | encoded | qld-part07-functions-and-powers:488 |
| s 27A(3A) | 513 | encoded | qld-part07-functions-and-powers:499 |
| s 27A(3B) | 514 | fork | F12; qld-part07-functions-and-powers:508 |
| s 27A(3C) | 515 | encoded | qld-part07-functions-and-powers:515 |
| s 27A(3D) | 516 | encoded | qld-part07-functions-and-powers:522 |
| s 27A(3D), example | 517-518 | encoded | example, quoted in qld-tests-part07; qld-tests-part07:156 |
| s 27A(4) | 519 | encoded | qld-part07-functions-and-powers:529 |
| s 27A(5) | 520 | encoded | qld-part07-functions-and-powers:536 |
| s 27A(6) | 521 | encoded | qld-part07-functions-and-powers:543 |
| s 27A(7) | 522 | encoded | qld-part07-functions-and-powers:551 |
| s 27A(8) | 523 | encoded | qld-part07-functions-and-powers:558 |
| s 27A(8A) | 524 | encoded | qld-part07-functions-and-powers:573 |
| s 27A(8A)(a) | 525 | encoded | qld-part07-functions-and-powers:573 |
| s 27A(8A)(b) | 526-527 | encoded | qld-part07-functions-and-powers:573 |
| s 27A(8A)(c) | 528 | encoded | qld-part07-functions-and-powers:573 |
| s 27A(8A)(d) | 529 | encoded | qld-part07-functions-and-powers:573 |
| s 27A(8B) | 530 | encoded | qld-part07-functions-and-powers:588 |
| s 27A(8B)(a) | 531 | encoded | qld-part07-functions-and-powers:588 |
| s 27A(8B)(b) | 532-533 | encoded | qld-part07-functions-and-powers:588 |
| s 27A(8B)(c) | 534 | encoded | qld-part07-functions-and-powers:588 |
| s 27A(8B)(d) | 535 | encoded | qld-part07-functions-and-powers:588 |
| s 27A(9) | 536 | encoded | qld-part07-functions-and-powers:598 |
| s 27A(9)(a) | 537 | encoded | qld-part07-functions-and-powers:598 |
| s 27A(9)(b) | 538 | encoded | qld-part07-functions-and-powers:608 |
| s 27A(10) | 539 | encoded | qld-part07-functions-and-powers:618 |
| s 27A(10A) | 540 | encoded | qld-part07-functions-and-powers:625 |
| s 27A(11) | 541 | encoded | qld-part07-functions-and-powers:632 |
| s 27A(12) | 542 | encoded | qld-part07-functions-and-powers:639 |
| s 27A(13) | 543 | encoded | qld-part07-functions-and-powers:649 |
| s 27A(14) | 544 | encoded | qld-part07-functions-and-powers:656 |
| s 27A(15) | 545 | encoded | qld-part07-functions-and-powers:666 |
| s 27A(15A) | 546 | encoded | qld-part07-functions-and-powers:674 |
| s 27A(16) | 547 | encoded | qld-part07-functions-and-powers:682 |
| s 27A(16), definition power | 548 | encoded | qld-part07-functions-and-powers:682 |
| s 27B | 549-550 | encoded | qld-part07-functions-and-powers:693 |
| s 27B(a) | 551 | encoded | qld-part07-functions-and-powers:693 |
| s 27B(b) | 552 | encoded | qld-part07-functions-and-powers:693 |
| s 28 | 553 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 28AA | 554 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 28AB | 555 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 28AC | 556 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 28A | 557 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 29 heading | 558 | inert | not operative: section heading (the rules are in its subsections) |
| s 29(1) | 559 | encoded | qld-part07-functions-and-powers:709 |
| s 29(1)(a) | 560 | encoded | qld-part07-functions-and-powers:709 |
| s 29(1)(b) | 561 | encoded | qld-part07-functions-and-powers:709 |
| s 29(1)(c) | 562 | encoded | qld-part07-functions-and-powers:709 |
| s 29(2) | 563 | encoded | qld-part07-functions-and-powers:718 |
| s 29(2)(a) | 564 | encoded | qld-part07-functions-and-powers:718 |
| s 29(2)(b) | 565 | encoded | qld-part07-functions-and-powers:718 |
| s 29(3) | 566 | encoded | qld-part07-functions-and-powers:734 |
| s 29(4) | 567 | encoded | qld-part07-functions-and-powers:741 |
| s 29A | 568 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 29B | 569-570 | encoded | qld-part07-functions-and-powers:754 |
| s 30 | 571 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| Part 8 heading | 572 | inert | not operative: Part heading |
| s 32 | 573-574 | encoded | qld-part08a-defined-terms:13 |
| s 32A | 575-576 | fork | F13; qld-part08a-defined-terms:23 |
| s 32AA | 577-578 | encoded | qld-part08a-defined-terms:33 |
| s 32AB | 579-580 | encoded | qld-part08a-defined-terms:46 |
| s 32AB(a) | 581 | encoded | qld-part08a-defined-terms:46 |
| s 32AB(b) | 582-583 | encoded | qld-part08a-defined-terms:46 |
| s 32AB(c) | 584 | encoded | qld-part08a-defined-terms:46 |
| s 32AB(d) | 585 | encoded | qld-part08a-defined-terms:66 |
| s 32B | 586-587 | encoded | qld-part08a-defined-terms:79 |
| s 32C | 588-589 | encoded | qld-part08a-defined-terms:92 |
| s 32C(a) | 590 | encoded | qld-part08a-defined-terms:92 |
| s 32C(b) | 591 | encoded | qld-part08a-defined-terms:92 |
| s 32CA heading | 592 | inert | not operative: section heading (the rules are in its subsections) |
| s 32CA(1) | 593 | encoded | qld-part08a-defined-terms:113 |
| s 32CA(2) | 594 | encoded | qld-part08a-defined-terms:115 |
| s 32CA(3) | 595 | encoded | qld-part08a-defined-terms:125 |
| s 32CB heading | 596 | inert | not operative: section heading (the rules are in its subsections) |
| s 32CB(1) | 597 | encoded | qld-part08a-defined-terms:134 |
| s 32CB(2) | 598 | encoded | qld-part08a-defined-terms:141 |
| s 32CC | 599 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 32D heading | 600 | inert | not operative: section heading (the rules are in its subsections) |
| s 32D(1) | 601 | encoded | qld-part08a-defined-terms:153 |
| s 32D(2) | 602 | encoded | qld-part08a-defined-terms:165 |
| s 32D(2), example | 603-611 | encoded | qld-part08a-defined-terms:195 |
| s 32D(2), example 2 | 612-615 | encoded | qld-part08a-defined-terms:200 |
| s 32D(2), example 3 | 616-619 | encoded | qld-part08a-defined-terms:205 |
| s 32DA heading | 620 | inert | not operative: section heading (the rules are in its subsections) |
| s 32DA(1) | 621 | encoded | qld-part08a-defined-terms:221 |
| s 32DA(2) | 622 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(a) | 623 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(b) | 624 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(c) | 625 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(d) | 626 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(e) | 627 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(f) | 628 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(g) | 629 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(h) | 630 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(2)(i) | 631 | encoded | qld-part08a-defined-terms:252 |
| s 32DA(3) | 632 | encoded | qld-part08a-defined-terms:261 |
| s 32DA(4) | 633 | encoded | qld-part08a-defined-terms:267 |
| s 32DA(5) | 634 | encoded | qld-part08a-defined-terms:275 |
| s 32DA(5)(a) | 635 | encoded | qld-part08a-defined-terms:275 |
| s 32DA(5)(b) | 636 | encoded | qld-part08a-defined-terms:281 |
| s 32DA(6) | 637 | fork | F14; qld-part08a-defined-terms:290 |
| s 32E | 638-639 | fork | F15; qld-part08a-defined-terms:306 |
| s 32E(a) | 640 | fork | F15; qld-part08a-defined-terms:306 |
| s 32E(b) | 641-642 | fork | F15; qld-part08a-defined-terms:306 |
| s 32E(c) | 643 | fork | F15; qld-part08a-defined-terms:306 |
| s 32E(d) | 644 | encoded | qld-part08a-defined-terms:316 |
| s 32F heading | 645 | inert | not operative: section heading (the rules are in its subsections) |
| s 32F(1) | 646 | encoded | qld-part08a-defined-terms:329 |
| s 32F(2) | 647 | encoded | qld-part08a-defined-terms:342 |
| s 32F(2), example | 648-649 | encoded | qld-part08a-defined-terms:342 |
| s 33 heading | 650 | inert | not operative: section heading (the rules are in its subsections) |
| s 33(1) | 651 | encoded | qld-part08b-ministers-and-offices:14 |
| s 33(1)(a) | 652 | encoded | qld-part08b-ministers-and-offices:14 |
| s 33(1)(b) | 653 | encoded | qld-part08b-ministers-and-offices:21 |
| s 33(2) | 654 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(2)(a) | 655 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(2)(b) | 656 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(2)(b)(i) | 657 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(2)(b)(ii) | 658 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(2)(c) | 659 | encoded | qld-part08b-ministers-and-offices:44 |
| s 33(3) | 660 | encoded | qld-part08b-ministers-and-offices:63 |
| s 33(4) | 661 | encoded | qld-part08b-ministers-and-offices:70 |
| s 33(5) | 662 | encoded | qld-part08b-ministers-and-offices:78 |
| s 33(5)(a) | 663 | encoded | qld-part08b-ministers-and-offices:78 |
| s 33(5)(b) | 664 | encoded | qld-part08b-ministers-and-offices:85 |
| s 33AA heading | 665 | inert | not operative: section heading (the rules are in its subsections) |
| s 33AA(1) | 666 | encoded | qld-part08b-ministers-and-offices:95 |
| s 33AA(2) | 667 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(a) | 668 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(a)(i) | 669 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(a)(ii) | 670 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(b) | 671 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(b)(i) | 672 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(2)(b)(ii) | 673 | encoded | qld-part08b-ministers-and-offices:112 |
| s 33AA(3) | 674 | encoded | qld-part08b-ministers-and-offices:124 |
| s 33AA(4) | 675 | encoded | qld-part08b-ministers-and-offices:131 |
| s 33AB heading | 676 | inert | not operative: section heading (the rules are in its subsections) |
| s 33AB(1) | 677 | encoded | qld-part08b-ministers-and-offices:138 |
| s 33AB(2) | 678 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(a) | 679 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(a)(i) | 680 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(a)(ii) | 681 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(b) | 682 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(b)(i) | 683 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(2)(b)(ii) | 684 | encoded | qld-part08b-ministers-and-offices:155 |
| s 33AB(3) | 685 | encoded | qld-part08b-ministers-and-offices:167 |
| s 33AC | 686-687 | encoded | qld-part08b-ministers-and-offices:177 |
| s 33AC(a) | 688 | encoded | qld-part08b-ministers-and-offices:177 |
| s 33AC(b) | 689-690 | encoded | qld-part08b-ministers-and-offices:177 |
| s 33A heading | 691 | inert | not operative: section heading (the rules are in its subsections) |
| s 33A(1) | 692 | encoded | qld-part08b-ministers-and-offices:195 |
| s 33A(1), example | 693-695 | encoded | example, quoted in qld-tests-part08b; qld-tests-part08b:64 |
| s 33A(2) | 696 | encoded | qld-part08b-ministers-and-offices:208 |
| s 33A(3) | 697 | encoded | qld-part08b-ministers-and-offices:216 |
| s 34 | 698-699 | encoded | qld-part08b-ministers-and-offices:229 |
| s 34A heading | 700 | inert | not operative: section heading (the rules are in its subsections) |
| s 34A(1) | 701 | encoded | qld-part08b-ministers-and-offices:236 |
| s 34A(2) | 702 | encoded | qld-part08b-ministers-and-offices:244 |
| s 34A(3) | 703 | encoded | qld-part08b-ministers-and-offices:254 |
| s 34A(3), definition chair title | 704 | encoded | qld-part08b-ministers-and-offices:254 |
| s 34B heading | 705 | inert | not operative: section heading (the rules are in its subsections) |
| s 34B(1) | 706 | encoded | qld-part08b-ministers-and-offices:262 |
| s 34B(2) | 707 | encoded | qld-part08b-ministers-and-offices:270 |
| s 34B(3) | 708 | encoded | qld-part08b-ministers-and-offices:280 |
| s 34B(3), definition deputy chair title | 709 | encoded | qld-part08b-ministers-and-offices:280 |
| s 35 heading | 710 | inert | not operative: section heading (the rules are in its subsections) |
| s 35(1) | 711 | encoded | qld-part08b-ministers-and-offices:291 |
| s 35(1)(a) | 712 | encoded | qld-part08b-ministers-and-offices:291 |
| s 35(1)(b) | 713 | encoded | qld-part08b-ministers-and-offices:298 |
| s 35(2) | 714 | encoded | qld-part08b-ministers-and-offices:305 |
| s 35A | 715-716 | encoded | qld-part08b-ministers-and-offices:331 |
| s 35B heading | 717 | inert | not operative: section heading (the rules are in its subsections) |
| s 35B(1) | 718-719 | encoded | qld-part08c-provision-references:20 |
| s 35B(1), definition body of the Act | 720 | encoded | qld-part08c-provision-references:20 |
| s 35B(1), definition provision unit | 721 | encoded | qld-part08c-provision-references:54 |
| s 35B(1)(a) | 722 | encoded | qld-part08c-provision-references:54 |
| s 35B(1)(b) | 723 | encoded | qld-part08c-provision-references:54 |
| s 35B(1)(c) | 724 | encoded | qld-part08c-provision-references:54 |
| s 35B(1)(d) | 725 | encoded | qld-part08c-provision-references:54 |
| s 35B(2) | 726-727 | encoded | qld-part08c-provision-references:63 |
| s 35B(2), example | 728-732 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:38 |
| s 35B(3) | 733-734 | encoded | qld-part08c-provision-references:88 |
| s 35B(3), example | 735-738 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:48 |
| s 35B(4) | 739 | encoded | qld-part08c-provision-references:90 |
| s 35B(4), example | 740-741 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:57 |
| s 35B(5) | 742-743 | encoded | qld-part08c-provision-references:95 |
| s 35B(5)(a) | 744 | encoded | qld-part08c-provision-references:95 |
| s 35B(5)(b) | 745-746 | encoded | qld-part08c-provision-references:95 |
| s 35B(5), example | 747-759 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:77 |
| s 35B(6) | 760-761 | encoded | qld-part08c-provision-references:101 |
| s 35B(6)(a) | 762 | encoded | qld-part08c-provision-references:101 |
| s 35B(6)(b) | 763 | encoded | qld-part08c-provision-references:101 |
| s 35B(6)(c) | 764-765 | encoded | qld-part08c-provision-references:101 |
| s 35B(6), example | 766-768 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:95 |
| s 35B(7) | 769 | encoded | qld-part08c-provision-references:107 |
| s 35B(7)(a) | 770 | encoded | qld-part08c-provision-references:107 |
| s 35B(7)(b) | 771 | encoded | qld-part08c-provision-references:107 |
| s 35B(7)(c) | 772-773 | encoded | qld-part08c-provision-references:107 |
| s 35B(7), example | 774-780 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:108 |
| s 35BA | 781 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 35BB | 782 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 35C heading | 783 | inert | not operative: section heading (the rules are in its subsections) |
| s 35C(1) | 784 | encoded | qld-part08c-provision-references:135 |
| s 35C(2) | 785 | fork | F16; qld-part08c-provision-references:146 |
| s 35C(2), example | 786-787 | fork | F16; qld-part08c-provision-references:146 |
| s 35C(3) | 788 | encoded | qld-part08c-provision-references:154 |
| s 35C(4) | 789 | encoded | qld-part08c-provision-references:168 |
| s 35C(4)(a) | 790 | encoded | qld-part08c-provision-references:168 |
| s 35C(4)(b) | 791 | encoded | qld-part08c-provision-references:168 |
| s 35C(5) | 792 | encoded | qld-part08c-provision-references:178 |
| s 35C(6) | 793 | encoded | qld-part08c-provision-references:194 |
| s 35C(7) | 794 | encoded | qld-part08c-provision-references:196 |
| s 35C(8) | 795 | encoded | qld-part08c-provision-references:209 |
| s 35C(8), example | 796-797 | encoded | qld-part08c-provision-references:217 |
| s 35CA | 798-799 | encoded | qld-part08c-provision-references:225 |
| s 35D | 800-801 | encoded | qld-part08c-provision-references:240 |
| s 35D(a) | 802 | encoded | qld-part08c-provision-references:240 |
| s 35D(b) | 803 | encoded | qld-part08c-provision-references:240 |
| s 35D(c) | 804 | encoded | qld-part08c-provision-references:240 |
| s 35D, example | 805-806 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:152 |
| s 35D, example 2 | 807-808 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:161 |
| s 35E | 809-810 | encoded | qld-part08c-provision-references:250 |
| s 35E, example | 811-812 | encoded | example, quoted in qld-tests-part08c; qld-tests-part08c:167 |
| s 36 heading | 813 | inert | not operative: section heading (the rules are in its subsections) |
| s 36(1) | 814 | encoded | qld-part08c-provision-references:258 |
| s 36(2) | 815 | encoded | qld-part08c-provision-references:265 |
| Part 9 heading | 816 | inert | not operative: Part heading |
| s 37 heading | 817 | inert | not operative: section heading (the rules are in its subsections) |
| s 37(1) | 818 | encoded | qld-part09-distance-time-age:43 |
| s 37(2) | 819 | encoded | qld-part09-distance-time-age:45 |
| s 37(3) | 820 | fork | F17; qld-part09-distance-time-age:16 |
| s 37(3), definition post-2023 provision | 821 | fork | F17; qld-part09-distance-time-age:16 |
| s 37(3), definition pre-2023 provision | 822 | encoded | qld-part09-distance-time-age:25 |
| s 37(3), definition provision | 823 | encoded | qld-part09-distance-time-age:25 |
| s 38 heading | 824 | inert | not operative: section heading (the rules are in its subsections) |
| s 38(1) | 825 | fork | F18, F19; qld-interpretation-time:291 |
| s 38(1)(a) | 826 | fork | F20; qld-interpretation-time:269 |
| s 38(1)(b) | 827 | encoded | qld-interpretation-time:280 |
| s 38(2) | 828 | fork | F20, F21; qld-interpretation-time:354 |
| s 38(3) | 829 | fork | F19; qld-interpretation-time:366 |
| s 38(4) | 830 | encoded | qld-interpretation-time:414 |
| s 38(5) | 831 | encoded | qld-interpretation-time:341 |
| s 38(5), definition excluded day | 832 | encoded | qld-interpretation-time:341 |
| s 38(5)(a) | 833 | encoded | qld-interpretation-time:341 |
| s 38(5)(b) | 834 | encoded | qld-interpretation-time:341 |
| s 38A | 835-836 | fork | F22; qld-interpretation-time:430 |
| Part 10 heading | 837 | inert | not operative: Part heading |
| s 39 heading | 838 | inert | not operative: section heading (the rules are in its subsections) |
| s 39(1) | 839 | encoded | qld-part10-service-of-documents:28 |
| s 39(1)(a) | 840 | encoded | qld-part10-service-of-documents:28 |
| s 39(1)(a)(i) | 841 | encoded | qld-part10-service-of-documents:28 |
| s 39(1)(a)(ii) | 842 | encoded | qld-part10-service-of-documents:28 |
| s 39(1)(b) | 843 | encoded | qld-part10-service-of-documents:28 |
| s 39(2) | 844 | encoded | qld-part10-service-of-documents:58 |
| s 39(3) | 845 | encoded | qld-part10-service-of-documents:65 |
| s 39(3)(a) | 846 | encoded | qld-part10-service-of-documents:65 |
| s 39(3)(b) | 847 | encoded | qld-part10-service-of-documents:70 |
| s 39A heading | 848 | inert | not operative: section heading (the rules are in its subsections) |
| s 39A(1) | 849 | encoded | qld-part10-service-of-documents:78 |
| s 39A(1)(a) | 850 | encoded | qld-part10-service-of-documents:78 |
| s 39A(1)(b) | 851 | encoded | qld-interpretation-time:455 |
| s 39A(2) | 852 | encoded | qld-part10-service-of-documents:87 |
| s 39A(3) | 853 | encoded | qld-part10-service-of-documents:98 |
| s 40 | 854 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| Part 11 heading | 855 | inert | not operative: Part heading |
| s 41 | 856-857 | encoded | qld-part11-offences:20 |
| s 41(a) | 858 | encoded | qld-part11-offences:20 |
| s 41(b) | 859 | encoded | qld-part11-offences:20 |
| s 41(c) | 860-861 | encoded | qld-part11-offences:20 |
| s 41(d) | 862 | encoded | qld-part11-offences:20 |
| s 41(e) | 863 | encoded | qld-part11-offences:20 |
| s 41A heading | 864 | inert | not operative: section heading (the rules are in its subsections) |
| s 41A(1) | 865 | encoded | qld-part11-offences:36 |
| s 41A(1)(a) | 866 | encoded | qld-part11-offences:36 |
| s 41A(1)(b) | 867 | encoded | qld-part11-offences:36 |
| s 41A(2) | 868 | encoded | qld-part11-offences:38 |
| s 42 | 869-870 | encoded | qld-part11-offences:55 |
| s 43 heading | 871 | inert | not operative: section heading (the rules are in its subsections) |
| s 43(1) | 872 | encoded | qld-part11-offences:84 |
| s 43(1)(a) | 873 | encoded | qld-part11-offences:84 |
| s 43(1)(b) | 874 | encoded | qld-part11-offences:84 |
| s 43(2) | 875 | encoded | qld-part11-offences:70 |
| s 43(3) | 876 | encoded | qld-part11-offences:62 |
| s 44 heading | 877 | inert | not operative: section heading (the rules are in its subsections) |
| s 44(1) | 878 | encoded | qld-part11-offences:101 |
| s 44(2) | 879 | encoded | qld-part11-offences:107 |
| s 44(2)(a) | 880 | encoded | qld-part11-offences:107 |
| s 44(2)(b) | 881 | encoded | qld-part11-offences:107 |
| s 44(2)(c) | 882 | encoded | qld-part11-offences:107 |
| s 44(2)(d) | 883 | encoded | qld-part11-offences:107 |
| s 44(3) | 884 | encoded | qld-part11-offences:116 |
| s 44(4) | 885 | encoded | qld-part11-offences:123 |
| s 45 heading | 886 | inert | not operative: section heading (the rules are in its subsections) |
| s 45(1) | 887 | fork | F23; qld-part11-offences:137 |
| s 45(2) | 888 | fork | F23; qld-part11-offences:139 |
| s 45(3) | 889 | encoded | qld-part11-offences:158 |
| s 45(3), definition law | 890 | encoded | qld-part11-offences:158 |
| s 46 | 891-892 | encoded | qld-part11-offences:170 |
| Part 12 heading | 893 | inert | not operative: Part heading |
| s 47 heading | 894-895 | inert | not operative: section heading and introductory words to definitions that are rows of their own |
| s 47, definition cooperative scheme | 896 | encoded | qld-part12-coastal-waters:12 |
| s 47, definition criminal laws | 897 | encoded | qld-part12-coastal-waters:19 |
| s 47, definition laws of the State | 898 | encoded | qld-part12-coastal-waters:29 |
| s 47(a) | 899 | encoded | qld-part12-coastal-waters:29 |
| s 47(b) | 900 | encoded | qld-part12-coastal-waters:29 |
| s 47A | 901-902 | encoded | qld-part12-coastal-waters:49 |
| s 47A(a) | 903 | encoded | qld-part12-coastal-waters:49 |
| s 47A(b) | 904-905 | encoded | qld-part12-coastal-waters:49 |
| s 47B heading | 906 | inert | not operative: section heading (the rules are in its subsections) |
| s 47B(1) | 907 | encoded | qld-part12-coastal-waters:65 |
| s 47B(1)(a) | 908 | encoded | qld-part12-coastal-waters:65 |
| s 47B(1)(b) | 909 | encoded | qld-part12-coastal-waters:65 |
| s 47B(1)(c) | 910 | encoded | qld-part12-coastal-waters:65 |
| s 47B(2) | 911 | encoded | qld-part12-coastal-waters:78 |
| s 47C heading | 912 | inert | not operative: section heading (the rules are in its subsections) |
| s 47C(1) | 913 | encoded | qld-part12-coastal-waters:85 |
| s 47C(2) | 914 | encoded | qld-part12-coastal-waters:92 |
| s 47D | 915-916 | encoded | qld-part12-coastal-waters:99 |
| s 47E | 917-918 | encoded | qld-part12-coastal-waters:106 |
| s 47E, example | 919-924 | encoded | qld-part12-coastal-waters:122 |
| s 47F | 925 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 47G | 926 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| Part 12A heading | 927 | inert | not operative: Part heading |
| s 48 heading | 928 | inert | not operative: section heading (the rules are in its subsections) |
| s 48(1) | 929 | encoded | qld-part12a-forms:11 |
| s 48(2) | 930 | encoded | qld-part12a-forms:20 |
| s 48(3) | 931 | encoded | qld-part12a-forms:46 |
| s 48(3), example | 932-934 | encoded | example, quoted in qld-tests-part12a; qld-tests-part12a:19 |
| s 48(4) | 935 | encoded | qld-part12a-forms:54 |
| s 48(5) | 936 | encoded | qld-part12a-forms:62 |
| s 48(6) | 937 | encoded | qld-part12a-forms:80 |
| s 48(6)(a) | 938 | encoded | qld-part12a-forms:80 |
| s 48(6)(a)(i) | 939 | encoded | qld-part12a-forms:80 |
| s 48(6)(a)(ii) | 940 | encoded | qld-part12a-forms:80 |
| s 48(6)(a)(?)(A) | 941 | encoded | qld-part12a-forms:80 |
| s 48(6)(a)(?)(B) | 942 | encoded | qld-part12a-forms:80 |
| s 48(6)(a)(?)(C) | 943 | encoded | qld-part12a-forms:80 |
| s 48(6)(b) | 944 | encoded | qld-part12a-forms:80 |
| s 48(7) | 945 | encoded | qld-part12a-forms:95 |
| s 48(8) | 946 | encoded | qld-part12a-forms:103 |
| s 48(9) | 947 | encoded | qld-part12a-forms:111 |
| s 48(9), definition relevant department | 948 | encoded | qld-part12a-forms:111 |
| s 48(9), definition relevant website | 949 | encoded | qld-part12a-forms:135 |
| s 48(9)(a) | 950 | encoded | qld-part12a-forms:135 |
| s 48(9)(b) | 951 | encoded | qld-part12a-forms:135 |
| s 48(9)(b)(i) | 952 | encoded | qld-part12a-forms:135 |
| s 48(9)(b)(ii) | 953 | encoded | qld-part12a-forms:135 |
| s 48(9)(b)(iii) | 954 | encoded | qld-part12a-forms:135 |
| s 48(9)(b)(?)(A) | 955 | encoded | qld-part12a-forms:135 |
| s 48(9)(b)(?)(B) | 956 | encoded | qld-part12a-forms:135 |
| s 48(9), definition whole-of-government website | 957 | encoded | qld-part12a-forms:154 |
| s 48(9)(a) | 958 | encoded | qld-part12a-forms:154 |
| s 48(9)(b) | 959 | encoded | qld-part12a-forms:154 |
| s 48A heading | 960 | inert | not operative: section heading (the rules are in its subsections) |
| s 48A(1) | 961 | encoded | qld-part12a-forms:164 |
| s 48A(2) | 962 | encoded | qld-part12a-forms:183 |
| s 48A(2)(a) | 963 | encoded | qld-part12a-forms:183 |
| s 48A(2)(b) | 964 | encoded | qld-part12a-forms:183 |
| s 48A(2)(c) | 965-966 | encoded | qld-part12a-forms:183 |
| s 48A(3) | 967 | encoded | qld-part12a-forms:196 |
| s 48A(3)(a) | 968 | encoded | qld-part12a-forms:196 |
| s 48A(3)(b) | 969-970 | encoded | qld-part12a-forms:196 |
| s 48A(4) | 971 | encoded | qld-part12a-forms:208 |
| s 48A(4), example | 972-973 | encoded | example, quoted in qld-tests-part12a; qld-tests-part12a:80 |
| s 48A(4), example 2 | 974-975 | encoded | example, quoted in qld-tests-part12a; qld-tests-part12a:80 |
| Part 12B heading | 976 | inert | not operative: Part heading |
| s 48B heading | 977 | inert | not operative: section heading (the rules are in its subsections) |
| s 48B(1) | 978 | encoded | qld-part12b-fee-units:11 |
| s 48B(2) | 979 | encoded | qld-part12b-fee-units:18 |
| s 48B(2), example | 980-981 | encoded | example, quoted in qld-tests-part12b; qld-tests-part12b:14 |
| s 48B(3) | 982 | encoded | qld-part12b-fee-units:24 |
| s 48B(4) | 983 | encoded | qld-part12b-fee-units:34 |
| s 48B(4)(a) | 984 | encoded | qld-part12b-fee-units:34 |
| s 48B(4)(b) | 985 | encoded | qld-part12b-fee-units:34 |
| s 48C heading | 986 | inert | not operative: section heading (the rules are in its subsections) |
| s 48C(1) | 987 | encoded | qld-part12b-fee-units:45 |
| s 48C(2) | 988 | encoded | qld-part12b-fee-units:51 |
| s 48C(3) | 989 | encoded | qld-part12b-fee-units:67 |
| s 48C(3)(a) | 990 | encoded | qld-part12b-fee-units:67 |
| s 48C(3)(b) | 991 | encoded | qld-part12b-fee-units:67 |
| s 48C(3)(b)(i) | 992 | encoded | qld-part12b-fee-units:67 |
| s 48C(3)(b)(ii) | 993 | encoded | qld-part12b-fee-units:67 |
| s 48C(3), example | 994-995 | encoded | example, quoted in qld-tests-part12b; qld-tests-part12b:27 |
| Part 13 heading | 996 | inert | not operative: Part heading |
| s 49 | 997-998 | encoded | qld-part13-miscellaneous:13 |
| s 49, example | 999-1000 | encoded | example, quoted in qld-tests-part13; qld-tests-part13:12 |
| s 49A | 1001-1002 | encoded | qld-part13-miscellaneous:23 |
| s 50 heading | 1003 | inert | not operative: section heading (the rules are in its subsections) |
| s 50(1) | 1004 | encoded | qld-part13-miscellaneous:33 |
| s 50(1)(a) | 1005 | encoded | qld-part13-miscellaneous:33 |
| s 50(1)(b) | 1006 | encoded | qld-part13-miscellaneous:40 |
| s 50(2) | 1007 | encoded | qld-part13-miscellaneous:57 |
| s 50(2), definition approve | 1008 | encoded | qld-part13-miscellaneous:57 |
| s 50(2), definition disapprove | 1009 | encoded | qld-part13-miscellaneous:68 |
| s 50(2), definition empowered entity | 1010 | encoded | qld-part13-miscellaneous:78 |
| s 51 | 1011 | repealed or blank in this text | the text shows the heading ‘[Repealed]’ and no text |
| s 51A | 1012-1013 | encoded | qld-part13-miscellaneous:87 |
| s 52 | 1014-1015 | encoded | qld-part13-miscellaneous:105 |
| s 52(a) | 1016 | encoded | qld-part13-miscellaneous:114 |
| s 52(b) | 1017 | encoded | qld-part13-miscellaneous:121 |
| s 52A heading | 1018 | inert | not operative: section heading (the rules are in its subsections) |
| s 52A(1) | 1019 | encoded | qld-part13-miscellaneous:134 |
| s 52A(1)(a) | 1020 | encoded | qld-part13-miscellaneous:134 |
| s 52A(1)(a)(i) | 1021 | encoded | qld-part13-miscellaneous:134 |
| s 52A(1)(a)(ii) | 1022 | encoded | qld-part13-miscellaneous:134 |
| s 52A(1)(b) | 1023 | encoded | qld-part13-miscellaneous:134 |
| s 52A(2) | 1024 | encoded | qld-part13-miscellaneous:142 |
| s 52A(3) | 1025 | encoded | qld-part13-miscellaneous:150 |
| s 52A(3), definition approving entity | 1026 | encoded | qld-part13-miscellaneous:150 |
| s 52A(3), definition authorising law | 1027 | encoded | qld-part13-miscellaneous:157 |
| s 52A(3), definition form | 1028 | encoded | qld-part13-miscellaneous:164 |
| s 52B | 1029-1030 | inert | machinery: regulation-making power |
| Part 14 heading | 1031 | inert | not operative: Part heading |
| Division 1 of Part 14 heading | 1032 | inert | not operative: Division heading |
| s 53 heading | 1033 | inert | not operative: section heading (the rules are in its subsections) |
| s 53(1) | 1034 | encoded | qld-part14-transitional:12 |
| s 53(2) | 1035 | encoded | qld-part14-transitional:23 |
| Division 2 of Part 14 heading | 1036 | inert | not operative: Division heading |
| s 54 | 1037-1038 | encoded | qld-part14-transitional:35 |
| s 54, definition commencement | 1039 | encoded | qld-part14-transitional:35 |
| s 54, definition subordinate legislation | 1040 | encoded | qld-part14-transitional:42 |
| s 55 heading | 1041 | inert | not operative: section heading (the rules are in its subsections) |
| s 55(1) | 1042 | encoded | qld-part14-transitional:62 |
| s 55(2) | 1043 | encoded | qld-part14-transitional:67 |
| s 55(2)(a) | 1044 | encoded | qld-part14-transitional:67 |
| s 55(2)(b) | 1045 | encoded | qld-part14-transitional:67 |
| s 55(2)(c) | 1046 | encoded | qld-part14-transitional:67 |
| s 56 | 1047-1048 | encoded | qld-part14-transitional:91 |
| s 56(a) | 1049 | encoded | qld-part14-transitional:91 |
| s 56(b) | 1050 | encoded | qld-part14-transitional:91 |
| s 57 | 1051-1052 | encoded | qld-part14-transitional:102 |
| s 57(a) | 1053 | encoded | qld-part14-transitional:102 |
| s 57(b) | 1054 | encoded | qld-part14-transitional:102 |
| Division 3 of Part 14 heading | 1055 | inert | not operative: Division heading |
| s 58 heading | 1056 | inert | not operative: section heading (the rules are in its subsections) |
| s 58(1) | 1057 | encoded | qld-part14-transitional:115 |
| s 58(1)(a) | 1058 | encoded | qld-part14-transitional:115 |
| s 58(1)(b) | 1059 | encoded | qld-part14-transitional:115 |
| s 58(2) | 1060 | encoded | qld-part14-transitional:123 |
| s 58(3) | 1061 | encoded | qld-part14-transitional:133 |
| s 58(3), definition amended section 48 | 1062 | encoded | qld-part14-transitional:133 |
| s 58(3), definition authorising law | 1063 | encoded | qld-part14-transitional:140 |
| s 58(3), definition form | 1064 | encoded | qld-part14-transitional:147 |
| s 58(3), definition previous section 48(5) | 1065 | encoded | qld-part14-transitional:154 |
| Schedule 1 heading | 1066-1067 | inert | not operative: Schedule heading and the provision reference printed under it |
| schedule 1, definition Aboriginal local government | 1068 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Aboriginal people | 1069 | encoded | qld-schedule1-table:33 |
| schedule 1, definition Aboriginal tradition | 1070 | encoded | qld-schedule1-table:37 |
| schedule 1, definition Aborigine | 1071 | encoded | qld-schedule1-table:41 |
| schedule 1, definition Act | 1072 | encoded | qld-schedule1-table:45 |
| schedule 1, definition Acting Governor | 1073 | encoded | qld-schedule1-table:49 |
| schedule 1, definition additional territorial unit | 1074 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition adjacent area in respect of the State | 1075 | encoded | qld-schedule1-table:57 |
| schedule 1, definition Administrative Arrangements | 1076 | encoded | qld-schedule1-table:61 |
| schedule 1, definition Administrator | 1077 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition adult | 1078 | encoded | qld-schedule1-table:69 |
| schedule 1, definition affidavit | 1079 | encoded | qld-schedule1-table:73 |
| schedule 1, definition AFIC (Queensland) Code | 1080 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition AFIC (Queensland) Regulations | 1081 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Alien | 1082 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition amend | 1083 | encoded | qld-schedule1-table:92 |
| schedule 1, definition amend, paragraph (a) | 1084 | encoded | qld-schedule1-table:92 |
| schedule 1, definition amend, paragraph (b) | 1085 | encoded | qld-schedule1-table:92 |
| schedule 1, definition amend, paragraph (c) | 1086 | encoded | qld-schedule1-table:92 |
| schedule 1, definition appoint | 1087 | encoded | qld-schedule1-table:96 |
| schedule 1, definition appropriately qualified | 1088 | encoded | qld-schedule1-table:104 |
| schedule 1, definition appropriately qualified, paragraph (a) | 1089 | encoded | qld-schedule1-table:104 |
| schedule 1, definition appropriately qualified, paragraph (b) | 1090 | encoded | qld-schedule1-table:104 |
| schedule 1, definition appropriately qualified, example | 1091-1092 | encoded | qld-schedule1-table:104 |
| schedule 1, definition area | 1093 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition AS | 1094 | encoded | qld-schedule1-table:112 |
| schedule 1, definition ASC Law | 1095 | encoded | qld-schedule1-table:116 |
| schedule 1, definition ASC Law and ASC Regulations | 1096 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition ASC Regulations | 1097 | encoded | qld-schedule1-table:124 |
| schedule 1, definition ASIC | 1098 | encoded | qld-schedule1-table:128 |
| schedule 1, definition ASIC Act | 1099 | encoded | qld-schedule1-table:132 |
| schedule 1, definition ASIC Law | 1100 | encoded | qld-schedule1-table:136 |
| schedule 1, definition ASIC Regulations | 1101 | encoded | qld-schedule1-table:142 |
| schedule 1, definition ASIC Regulations, paragraph (a) | 1102 | encoded | qld-schedule1-table:142 |
| schedule 1, definition ASIC Regulations, paragraph (b) | 1103 | encoded | qld-schedule1-table:142 |
| schedule 1, definition asset | 1104 | encoded | qld-schedule1-table:146 |
| schedule 1, definition Attorney-General | 1105 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Australia | 1106 | encoded | qld-schedule1-table:154 |
| schedule 1, definition Australia Acts | 1107 | encoded | qld-schedule1-table:158 |
| schedule 1, definition Australian citizen | 1108 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Australian Standard | 1109 | encoded | qld-schedule1-table:166 |
| schedule 1, definition bank | 1110 | encoded | qld-schedule1-table:172 |
| schedule 1, definition bank, paragraph (a) | 1111 | encoded | qld-schedule1-table:172 |
| schedule 1, definition bank, paragraph (b) | 1112 | encoded | qld-schedule1-table:172 |
| schedule 1, definition basic territorial unit | 1113 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition breach | 1114 | encoded | qld-schedule1-table:180 |
| schedule 1, definition British Act | 1115 | encoded | qld-schedule1-table:184 |
| schedule 1, definition British Parliament | 1116 | encoded | qld-schedule1-table:193 |
| schedule 1, definition British Parliament, paragraph (a) | 1117 | encoded | qld-schedule1-table:193 |
| schedule 1, definition British Parliament, paragraph (b) | 1118 | encoded | qld-schedule1-table:193 |
| schedule 1, definition British Parliament, paragraph (c) | 1119 | encoded | qld-schedule1-table:193 |
| schedule 1, definition British Parliament, paragraph (d) | 1120-1121 | encoded | qld-schedule1-table:193 |
| schedule 1, definition British possession | 1122 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition British subject | 1123 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition building society | 1124 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition burial | 1125 | encoded | qld-schedule1-table:209 |
| schedule 1, definition business day | 1126 | encoded | qld-interpretation-time:328 |
| schedule 1, definition business day, paragraph (a) | 1127 | encoded | qld-interpretation-time:328 |
| schedule 1, definition business day, paragraph (b) | 1128 | encoded | qld-interpretation-time:328 |
| schedule 1, definition by-law | 1129 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition by-laws | 1130 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition calendar month | 1131 | fork | F18, F24; qld-interpretation-time:185 |
| schedule 1, definition calendar month, paragraph (a) | 1132 | fork | F18, F24; qld-interpretation-time:185 |
| schedule 1, definition calendar month, paragraph (b) | 1133 | fork | F18, F24; qld-interpretation-time:185 |
| schedule 1, definition calendar year | 1134 | fork | F25; qld-interpretation-time:211 |
| schedule 1, definition change | 1135 | encoded | qld-schedule1-table:237 |
| schedule 1, definition charge, of an offence | 1136 | encoded | qld-schedule1-table:245 |
| schedule 1, definition charge, of an offence, paragraph (a) | 1137 | encoded | qld-schedule1-table:245 |
| schedule 1, definition charge, of an offence, paragraph (b) | 1138 | encoded | qld-schedule1-table:245 |
| schedule 1, definition charge, of an offence, paragraph (c) | 1139 | encoded | qld-schedule1-table:245 |
| schedule 1, definition charge, of an offence, paragraph (d) | 1140 | encoded | qld-schedule1-table:245 |
| schedule 1, definition cheque | 1141 | encoded | qld-schedule1-table:249 |
| schedule 1, definition chief executive | 1142 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive, paragraph (a) | 1143 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive, paragraph (b) | 1144 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive, paragraph (c) | 1145 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive, paragraph (d) | 1146 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive, paragraph (e) | 1147 | encoded | qld-schedule1-table:258 |
| schedule 1, definition chief executive (corrective services) | 1148 | encoded | qld-schedule1-table:262 |
| schedule 1, definition chief executive officer of a local government | 1149 | encoded | qld-schedule1-table:266 |
| schedule 1, definition child | 1150 | encoded | qld-schedule1-table:270 |
| schedule 1, definition Childrens Court judge | 1151 | encoded | qld-schedule1-table:276 |
| schedule 1, definition Childrens Court judge, paragraph (a) | 1152 | encoded | qld-schedule1-table:276 |
| schedule 1, definition Childrens Court judge, paragraph (b) | 1153 | encoded | qld-schedule1-table:276 |
| schedule 1, definition Childrens Court magistrate | 1154 | encoded | qld-schedule1-table:282 |
| schedule 1, definition Childrens Court magistrate, paragraph (a) | 1155 | encoded | qld-schedule1-table:282 |
| schedule 1, definition Childrens Court magistrate, paragraph (b) | 1156 | encoded | qld-schedule1-table:282 |
| schedule 1, definition citation of an Act | 1157 | encoded | qld-schedule1-table:286 |
| schedule 1, definition civil partner | 1158 | encoded | qld-schedule1-table:290 |
| schedule 1, definition civil partnership | 1159 | encoded | qld-schedule1-table:294 |
| schedule 1, definition coastal waters of the State | 1160 | encoded | qld-schedule1-table:300 |
| schedule 1, definition coastal waters of the State, paragraph (a) | 1161 | encoded | qld-schedule1-table:300 |
| schedule 1, definition coastal waters of the State, paragraph (b) | 1162 | encoded | qld-schedule1-table:300 |
| schedule 1, definition commencement | 1163 | encoded | qld-schedule1-table:304 |
| schedule 1, definition committal proceeding | 1164 | encoded | qld-schedule1-table:308 |
| schedule 1, definition Commonwealth | 1165 | encoded | qld-schedule1-table:312 |
| schedule 1, definition Commonwealth Constitution | 1166 | encoded | qld-schedule1-table:316 |
| schedule 1, definition Commonwealth Minister | 1167 | encoded | qld-schedule1-table:320 |
| schedule 1, definition Commonwealth Parliament | 1168 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition community or group of Aboriginal people | 1169 | encoded | qld-schedule1-table:330 |
| schedule 1, definition community or group of Aboriginal people, paragraph (a) | 1170 | encoded | qld-schedule1-table:330 |
| schedule 1, definition community or group of Aboriginal people, paragraph (b) | 1171 | encoded | qld-schedule1-table:330 |
| schedule 1, definition community or group of Torres Strait Islanders | 1172 | encoded | qld-schedule1-table:336 |
| schedule 1, definition community or group of Torres Strait Islanders, paragraph (a) | 1173 | encoded | qld-schedule1-table:336 |
| schedule 1, definition community or group of Torres Strait Islanders, paragraph (b) | 1174 | encoded | qld-schedule1-table:336 |
| schedule 1, definition company GOC | 1175 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition complaint and summons | 1176 | encoded | qld-schedule1-table:346 |
| schedule 1, definition complaint and summons, example | 1177-1178 | encoded | qld-schedule1-table:346 |
| schedule 1, definition confer | 1179 | encoded | qld-schedule1-table:350 |
| schedule 1, definition consolidated fund | 1180 | encoded | qld-schedule1-table:354 |
| schedule 1, definition Consolidated Revenue | 1181 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Consolidated Revenue Fund | 1182 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Constitution of Queensland | 1183 | encoded | qld-schedule1-table:369 |
| schedule 1, definition Constitution of Queensland, paragraph (a) | 1184 | encoded | qld-schedule1-table:369 |
| schedule 1, definition Constitution of Queensland, paragraph (b) | 1185 | encoded | qld-schedule1-table:369 |
| schedule 1, definition Constitution of Queensland, paragraph (c) | 1186 | encoded | qld-schedule1-table:369 |
| schedule 1, definition contravene | 1187 | encoded | qld-schedule1-table:373 |
| schedule 1, definition corporation | 1188 | encoded | qld-schedule1-table:377 |
| schedule 1, definition Corporations Act | 1189 | encoded | qld-schedule1-table:381 |
| schedule 1, definition Corporations Law | 1190 | encoded | qld-schedule1-table:385 |
| schedule 1, definition Corporations Law and Corporations Regulations | 1191 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Corporations legislation | 1192 | encoded | qld-schedule1-table:393 |
| schedule 1, definition Corporations Regulations | 1193 | encoded | qld-schedule1-table:399 |
| schedule 1, definition Corporations Regulations, paragraph (a) | 1194 | encoded | qld-schedule1-table:399 |
| schedule 1, definition Corporations Regulations, paragraph (b) | 1195 | encoded | qld-schedule1-table:399 |
| schedule 1, definition Court of Criminal Appeal | 1196 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition COVID-19 legislation expiry day | 1197 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition COVID-19 public health legislation expiry day | 1198 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition credit union | 1199 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Crime and Corruption Commission | 1200 | encoded | qld-schedule1-table:419 |
| schedule 1, definition CSIRO | 1201 | encoded | qld-schedule1-table:423 |
| schedule 1, definition date of assent | 1202 | encoded | qld-schedule1-table:427 |
| schedule 1, definition de facto partner | 1203 | encoded | qld-schedule1-table:431 |
| schedule 1, definition de facto relationship | 1204 | encoded | qld-schedule1-table:435 |
| schedule 1, definition definition | 1205 | encoded | qld-schedule1-table:447 |
| schedule 1, definition definition, paragraph (a) | 1206 | encoded | qld-schedule1-table:447 |
| schedule 1, definition definition, paragraph (b) | 1207 | encoded | qld-schedule1-table:447 |
| schedule 1, definition definition, example | 1208-1213 | encoded | qld-schedule1-table:447 |
| schedule 1, definition department | 1214 | encoded | qld-schedule1-table:451 |
| schedule 1, definition Deputy Governor | 1215 | encoded | qld-schedule1-table:455 |
| schedule 1, definition descendant | 1216 | encoded | qld-schedule1-table:461 |
| schedule 1, definition descendant, paragraph (a) | 1217 | encoded | qld-schedule1-table:461 |
| schedule 1, definition descendant, paragraph (b) | 1218 | encoded | qld-schedule1-table:461 |
| schedule 1, definition District Court | 1219 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition District Court judge | 1220 | encoded | qld-schedule1-table:469 |
| schedule 1, definition doctor | 1221 | encoded | qld-schedule1-table:473 |
| schedule 1, definition document | 1222 | encoded | qld-schedule1-table:482 |
| schedule 1, definition document, paragraph (a) | 1223 | encoded | qld-schedule1-table:482 |
| schedule 1, definition document, paragraph (b) | 1224 | encoded | qld-schedule1-table:482 |
| schedule 1, definition document, paragraph (i) | 1225 | encoded | qld-schedule1-table:482 |
| schedule 1, definition document, paragraph (ii) | 1226 | encoded | qld-schedule1-table:482 |
| schedule 1, definition document, paragraph (iii) | 1227 | encoded | qld-schedule1-table:482 |
| schedule 1, definition electronic document | 1228 | encoded | qld-schedule1-table:489 |
| schedule 1, definition electronic document, paragraph (a) | 1229 | encoded | qld-schedule1-table:489 |
| schedule 1, definition electronic document, paragraph (b) | 1230 | encoded | qld-schedule1-table:489 |
| schedule 1, definition electronic document, paragraph (c) | 1231 | encoded | qld-schedule1-table:489 |
| schedule 1, definition enactment | 1232 | encoded | qld-schedule1-table:493 |
| schedule 1, definition entity | 1233 | encoded | qld-schedule1-table:497 |
| schedule 1, definition establish | 1234 | encoded | qld-schedule1-table:501 |
| schedule 1, definition estate | 1235 | encoded | qld-schedule1-table:505 |
| schedule 1, definition Executive Council | 1236 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition exempt subordinate legislation | 1237 | encoded | qld-schedule1-table:513 |
| schedule 1, definition expire | 1238 | encoded | qld-schedule1-table:517 |
| schedule 1, definition external Territory | 1239 | encoded | qld-schedule1-table:521 |
| schedule 1, definition fail | 1240 | encoded | qld-schedule1-table:525 |
| schedule 1, definition Federal Court | 1241 | encoded | qld-schedule1-table:529 |
| schedule 1, definition federal industrial instrument | 1242 | encoded | qld-schedule1-table:533 |
| schedule 1, definition fee unit | 1243 | encoded | qld-schedule1-table:537 |
| schedule 1, definition file | 1244 | encoded | qld-schedule1-table:541 |
| schedule 1, definition financial institution | 1245 | encoded | qld-schedule1-table:545 |
| schedule 1, definition Financial Institutions (Queensland) Code | 1246 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Financial Institutions (Queensland) Regulations | 1247 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition financial year | 1248 | fork | F25; qld-interpretation-time:225 |
| schedule 1, definition finding | 1249 | encoded | qld-schedule1-table:561 |
| schedule 1, definition fix | 1250 | encoded | qld-schedule1-table:565 |
| schedule 1, definition foreign country | 1251 | encoded | qld-schedule1-table:569 |
| schedule 1, definition freehold land register | 1252 | encoded | qld-schedule1-table:573 |
| schedule 1, definition Friendly Societies (Queensland) Code | 1253 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Friendly Societies (Queensland) Regulations | 1254 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition function | 1255 | encoded | qld-schedule1-table:585 |
| schedule 1, definition fundamental legislative principles | 1256 | encoded | qld-schedule1-table:589 |
| schedule 1, definition Gas Pipelines Access (Queensland) Law | 1257 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Gas Pipelines Access (Queensland) Regulations | 1258 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition gazette | 1259 | encoded | qld-schedule1-table:601 |
| schedule 1, definition gazetted | 1260 | encoded | qld-schedule1-table:605 |
| schedule 1, definition gazette notice | 1261 | encoded | qld-schedule1-table:609 |
| schedule 1, definition GOC (or government owned corporation) | 1262 | encoded | qld-schedule1-table:613 |
| schedule 1, definition Government | 1263 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Government Gazette | 1264 | encoded | qld-schedule1-table:621 |
| schedule 1, definition government printer | 1265 | encoded | qld-schedule1-table:625 |
| schedule 1, definition Governor | 1266 | encoded | qld-schedule1-table:632 |
| schedule 1, definition Governor, paragraph (a) | 1267 | encoded | qld-schedule1-table:632 |
| schedule 1, definition Governor, paragraph (b) | 1268 | encoded | qld-schedule1-table:632 |
| schedule 1, definition Governor, paragraph (c) | 1269 | encoded | qld-schedule1-table:632 |
| schedule 1, definition Governor-General | 1270 | encoded | qld-schedule1-table:636 |
| schedule 1, definition Governor in Council | 1271 | encoded | qld-schedule1-table:642 |
| schedule 1, definition Governor in Council, paragraph (a) | 1272 | encoded | qld-schedule1-table:642 |
| schedule 1, definition Governor in Council, paragraph (b) | 1273 | encoded | qld-schedule1-table:642 |
| schedule 1, definition grant of representation | 1274 | encoded | qld-schedule1-table:646 |
| schedule 1, definition GST | 1275 | encoded | qld-schedule1-table:650 |
| schedule 1, definition Health Practitioner Regulation National Law | 1276 | encoded | qld-schedule1-table:658 |
| schedule 1, definition Health Practitioner Regulation National Law, paragraph (a) | 1277 | encoded | qld-schedule1-table:658 |
| schedule 1, definition Health Practitioner Regulation National Law, paragraph (i) | 1278 | encoded | qld-schedule1-table:658 |
| schedule 1, definition Health Practitioner Regulation National Law, paragraph (ii) | 1279 | encoded | qld-schedule1-table:658 |
| schedule 1, definition Health Practitioner Regulation National Law, paragraph (b) | 1280 | encoded | qld-schedule1-table:658 |
| schedule 1, definition High Court | 1281 | encoded | qld-schedule1-table:662 |
| schedule 1, definition Imperial Act | 1282 | encoded | qld-schedule1-table:666 |
| schedule 1, definition Imperial Parliament | 1283 | encoded | qld-schedule1-table:670 |
| schedule 1, definition indictable offence | 1284 | encoded | qld-schedule1-table:674 |
| schedule 1, definition indictment | 1285 | encoded | qld-schedule1-table:678 |
| schedule 1, definition individual | 1286 | encoded | qld-schedule1-table:682 |
| schedule 1, definition industrial commission | 1287 | encoded | qld-schedule1-table:686 |
| schedule 1, definition Industrial Commission or Industrial Relations Commission | 1288 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition industrial commissioner | 1289 | encoded | qld-schedule1-table:694 |
| schedule 1, definition industrial court | 1290 | encoded | qld-schedule1-table:698 |
| schedule 1, definition industrial gazette | 1291 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition industrial gazette notice | 1292 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition industrial magistrate | 1293 | encoded | qld-schedule1-table:710 |
| schedule 1, definition Industrial Magistrates Court | 1294 | encoded | qld-schedule1-table:714 |
| schedule 1, definition industrial relations commission | 1295 | encoded | qld-schedule1-table:718 |
| schedule 1, definition insert | 1296 | encoded | qld-schedule1-table:722 |
| schedule 1, definition insolvent under administration | 1297 | encoded | qld-schedule1-table:726 |
| schedule 1, definition instrument | 1298 | encoded | qld-schedule1-table:730 |
| schedule 1, definition interest | 1299 | encoded | qld-schedule1-table:736 |
| schedule 1, definition interest, paragraph (a) | 1300 | encoded | qld-schedule1-table:736 |
| schedule 1, definition interest, paragraph (b) | 1301 | encoded | qld-schedule1-table:736 |
| schedule 1, definition internal Territory | 1302 | encoded | qld-schedule1-table:740 |
| schedule 1, definition Island custom, known in the Torres Strait as Ailan Kastom | 1303 | encoded | qld-schedule1-table:744 |
| schedule 1, definition Jervis Bay Territory | 1304 | encoded | qld-schedule1-table:748 |
| schedule 1, definition joint local government | 1305 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Judge | 1306 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition justice | 1307 | encoded | qld-schedule1-table:760 |
| schedule 1, definition land | 1308 | encoded | qld-schedule1-table:764 |
| schedule 1, definition Land and Resources Tribunal | 1309 | encoded | qld-schedule1-table:768 |
| schedule 1, definition Land Appeal Court | 1310 | encoded | qld-schedule1-table:772 |
| schedule 1, definition Land Court | 1311 | encoded | qld-schedule1-table:776 |
| schedule 1, definition land registry | 1312 | encoded | qld-schedule1-table:780 |
| schedule 1, definition law of a State | 1313 | encoded | qld-schedule1-table:786 |
| schedule 1, definition law of a State, paragraph (a) | 1314 | encoded | qld-schedule1-table:786 |
| schedule 1, definition law of a State, paragraph (b) | 1315 | encoded | qld-schedule1-table:786 |
| schedule 1, definition lawyer | 1316 | encoded | qld-schedule1-table:790 |
| schedule 1, definition lease | 1317 | encoded | qld-schedule1-table:794 |
| schedule 1, definition Legislative Assembly | 1318 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Legislature | 1319 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition lessee | 1320 | encoded | qld-schedule1-table:806 |
| schedule 1, definition lessor | 1321 | encoded | qld-schedule1-table:810 |
| schedule 1, definition liability | 1322 | encoded | qld-schedule1-table:814 |
| schedule 1, definition Lieutenant Governor | 1323 | encoded | qld-schedule1-table:818 |
| schedule 1, definition local authority | 1324 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition local government | 1325 | encoded | qld-schedule1-table:828 |
| schedule 1, definition local government, paragraph (a) | 1326 | encoded | qld-schedule1-table:828 |
| schedule 1, definition local government, paragraph (b) | 1327 | encoded | qld-schedule1-table:828 |
| schedule 1, definition local government area | 1328 | encoded | qld-schedule1-table:832 |
| schedule 1, definition local law | 1329 | encoded | qld-schedule1-table:836 |
| schedule 1, definition local law policy | 1330 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition magistrate | 1331 | encoded | qld-schedule1-table:844 |
| schedule 1, definition Magistrates Court | 1332 | encoded | qld-schedule1-table:848 |
| schedule 1, definition make | 1333 | encoded | qld-schedule1-table:852 |
| schedule 1, definition medical practitioner | 1334 | encoded | qld-schedule1-table:856 |
| schedule 1, definition midnight | 1335 | encoded | qld-interpretation-time:40 |
| schedule 1, definition Minister | 1336 | encoded | qld-schedule1-table:864 |
| schedule 1, definition minor | 1337 | encoded | qld-schedule1-table:868 |
| schedule 1, definition modification | 1338 | encoded | qld-schedule1-table:872 |
| schedule 1, definition month | 1339 | fork | F18, F24; qld-interpretation-time:200 |
| schedule 1, definition mortgage | 1340 | encoded | qld-schedule1-table:880 |
| schedule 1, definition mortgagee | 1341 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition mortgagee in possession | 1342 | encoded | qld-schedule1-table:888 |
| schedule 1, definition mortgagor | 1343 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition named month | 1344 | encoded | qld-schedule1-table:896 |
| schedule 1, definition National Gas (Queensland) Law | 1345 | encoded | qld-schedule1-table:900 |
| schedule 1, definition National Gas (Queensland) Regulations | 1346 | encoded | qld-schedule1-table:904 |
| schedule 1, definition native title | 1347 | encoded | qld-schedule1-table:913 |
| schedule 1, definition native title, paragraph (a) | 1348 | encoded | qld-schedule1-table:913 |
| schedule 1, definition native title, paragraph (b) | 1349 | encoded | qld-schedule1-table:913 |
| schedule 1, definition native title, paragraph (c) | 1350 | encoded | qld-schedule1-table:913 |
| schedule 1, definition native title, example | 1351-1352 | encoded | qld-schedule1-table:913 |
| schedule 1, definition Northern Territory | 1353 | encoded | qld-schedule1-table:917 |
| schedule 1, definition notice to appear | 1354 | encoded | qld-schedule1-table:921 |
| schedule 1, definition notified | 1355 | encoded | qld-schedule1-table:925 |
| schedule 1, definition number | 1356 | encoded | qld-schedule1-table:932 |
| schedule 1, definition number, paragraph (a) | 1357 | encoded | qld-schedule1-table:932 |
| schedule 1, definition number, paragraph (b) | 1358 | encoded | qld-schedule1-table:932 |
| schedule 1, definition number, paragraph (c) | 1359 | encoded | qld-schedule1-table:932 |
| schedule 1, definition oath | 1360 | encoded | qld-schedule1-table:936 |
| schedule 1, definition oath and affidavit | 1361 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition office | 1362 | encoded | qld-schedule1-table:944 |
| schedule 1, definition officer | 1363 | encoded | qld-schedule1-table:948 |
| schedule 1, definition officer of the public service | 1364 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition official copy | 1365 | encoded | qld-schedule1-table:958 |
| schedule 1, definition official copy, paragraph (a) | 1366 | encoded | qld-schedule1-table:958 |
| schedule 1, definition official copy, paragraph (b) | 1367 | encoded | qld-schedule1-table:958 |
| schedule 1, definition of this Act | 1368 | encoded | qld-schedule1-table:962 |
| schedule 1, definition ombudsman | 1369 | encoded | qld-schedule1-table:966 |
| schedule 1, definition omit | 1370 | encoded | qld-schedule1-table:970 |
| schedule 1, definition order in council | 1371 | encoded | qld-schedule1-table:974 |
| schedule 1, definition ordinance | 1372 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Parliament | 1373 | encoded | qld-schedule1-table:984 |
| schedule 1, definition Parliament, paragraph (a) | 1374 | encoded | qld-schedule1-table:984 |
| schedule 1, definition Parliament, paragraph (b) | 1375 | encoded | qld-schedule1-table:984 |
| schedule 1, definition parliamentary counsel | 1376 | encoded | qld-schedule1-table:988 |
| schedule 1, definition party | 1377 | encoded | qld-schedule1-table:992 |
| schedule 1, definition passing | 1378 | encoded | qld-schedule1-table:996 |
| schedule 1, definition payable | 1379 | encoded | qld-schedule1-table:1000 |
| schedule 1, definition penalty | 1380 | encoded | qld-schedule1-table:1004 |
| schedule 1, definition penalty unit | 1381 | encoded | qld-schedule1-table:1008 |
| schedule 1, definition person | 1382 | encoded | qld-schedule1-table:1012 |
| schedule 1, definition person or party | 1383 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition personal representative of a deceased individual | 1384 | encoded | qld-schedule1-table:1020 |
| schedule 1, definition Petty sessions | 1385 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Planning and Environment Court | 1386 | encoded | qld-schedule1-table:1028 |
| schedule 1, definition police commissioner | 1387 | encoded | qld-schedule1-table:1032 |
| schedule 1, definition police officer | 1388 | encoded | qld-schedule1-table:1036 |
| schedule 1, definition possession of land | 1389 | encoded | qld-schedule1-table:1040 |
| schedule 1, definition power | 1390 | encoded | qld-schedule1-table:1044 |
| schedule 1, definition prescribed | 1391 | encoded | qld-schedule1-table:1048 |
| schedule 1, definition printed | 1392 | encoded | qld-schedule1-table:1052 |
| schedule 1, definition proceeding | 1393 | encoded | qld-schedule1-table:1056 |
| schedule 1, definition proceedings in the Legislative Assembly | 1394 | encoded | qld-schedule1-table:1060 |
| schedule 1, definition proclamation | 1395 | encoded | qld-schedule1-table:1064 |
| schedule 1, definition property | 1396 | encoded | qld-schedule1-table:1068 |
| schedule 1, definition provision | 1397 | encoded | qld-schedule1-table:1075 |
| schedule 1, definition provision, paragraph (a) | 1398 | encoded | qld-schedule1-table:1075 |
| schedule 1, definition provision, paragraph (b) | 1399 | encoded | qld-schedule1-table:1075 |
| schedule 1, definition provision, paragraph (c) | 1400 | encoded | qld-schedule1-table:1075 |
| schedule 1, definition public holiday | 1401 | encoded | qld-schedule1-table:1079 |
| schedule 1, definition public sector unit | 1402 | encoded | qld-schedule1-table:1085 |
| schedule 1, definition public sector unit, paragraph (a) | 1403 | encoded | qld-schedule1-table:1085 |
| schedule 1, definition public sector unit, paragraph (b) | 1404 | encoded | qld-schedule1-table:1085 |
| schedule 1, definition public service | 1405 | encoded | qld-schedule1-table:1089 |
| schedule 1, definition public service employee | 1406 | encoded | qld-schedule1-table:1093 |
| schedule 1, definition public service office | 1407 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition public service officer | 1408 | encoded | qld-schedule1-table:1101 |
| schedule 1, definition published | 1409 | encoded | qld-schedule1-table:1105 |
| schedule 1, definition purpose | 1410 | encoded | qld-schedule1-table:1109 |
| schedule 1, definition QCAT | 1411 | encoded | qld-schedule1-table:1113 |
| schedule 1, definition QCAT Act | 1412 | encoded | qld-schedule1-table:1117 |
| schedule 1, definition QIRC website | 1413 | encoded | qld-schedule1-table:1121 |
| schedule 1, definition Queensland Government Gazette | 1414 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Queensland lawyer | 1415 | encoded | qld-schedule1-table:1129 |
| schedule 1, definition Queensland legislation | 1416 | encoded | qld-schedule1-table:1137 |
| schedule 1, definition Queensland legislation, paragraph (a) | 1417 | encoded | qld-schedule1-table:1137 |
| schedule 1, definition Queensland legislation, paragraph (b) | 1418 | encoded | qld-schedule1-table:1137 |
| schedule 1, definition Queensland legislation, paragraph (c) | 1419 | encoded | qld-schedule1-table:1137 |
| schedule 1, definition Queensland legislation, paragraph (d) | 1420 | encoded | qld-schedule1-table:1137 |
| schedule 1, definition Queensland legislation website | 1421 | encoded | qld-schedule1-table:1141 |
| schedule 1, definition Queensland waters | 1422 | encoded | qld-schedule1-table:1147 |
| schedule 1, definition Queensland waters, paragraph (a) | 1423 | encoded | qld-schedule1-table:1147 |
| schedule 1, definition Queensland waters, paragraph (b) | 1424 | encoded | qld-schedule1-table:1147 |
| schedule 1, definition record | 1425 | encoded | qld-schedule1-table:1151 |
| schedule 1, definition regulation | 1426 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition regulations | 1427 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition repeal | 1428 | encoded | qld-schedule1-table:1166 |
| schedule 1, definition repeal, paragraph (a) | 1429 | encoded | qld-schedule1-table:1166 |
| schedule 1, definition repeal, paragraph (b) | 1430 | encoded | qld-schedule1-table:1166 |
| schedule 1, definition repeal, paragraph (c) | 1431 | encoded | qld-schedule1-table:1166 |
| schedule 1, definition reprint | 1432 | encoded | qld-schedule1-table:1172 |
| schedule 1, definition reprint, paragraph (a) | 1433 | encoded | qld-schedule1-table:1172 |
| schedule 1, definition reprint, paragraph (b) | 1434 | encoded | qld-schedule1-table:1172 |
| schedule 1, definition rule | 1435 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition rules | 1436 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition rules of court | 1437 | encoded | qld-schedule1-table:1184 |
| schedule 1, definition see, followed by a reference to, or to a provision of, any Act, law or document | 1438 | encoded | qld-schedule1-table:1188 |
| schedule 1, definition senior executive | 1439 | encoded | qld-schedule1-table:1192 |
| schedule 1, definition serve | 1440 | encoded | qld-schedule1-table:1196 |
| schedule 1, definition serve by post | 1441 | encoded | qld-schedule1-table:1200 |
| schedule 1, definition sign | 1442 | encoded | qld-schedule1-table:1204 |
| schedule 1, definition sitting day | 1443 | encoded | qld-schedule1-table:1208 |
| schedule 1, definition sitting days | 1444 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Speaker | 1445 | encoded | qld-schedule1-table:1216 |
| schedule 1, definition spent conviction | 1446 | encoded | qld-schedule1-table:1222 |
| schedule 1, definition spent conviction, paragraph (a) | 1447 | encoded | qld-schedule1-table:1222 |
| schedule 1, definition spent conviction, paragraph (b) | 1448 | encoded | qld-schedule1-table:1222 |
| schedule 1, definition spouse | 1449 | encoded | qld-schedule1-table:1226 |
| schedule 1, definition Standards Association of Australia | 1450 | encoded | qld-schedule1-table:1230 |
| schedule 1, definition Standards Australia | 1451 | encoded | qld-schedule1-table:1234 |
| schedule 1, definition State | 1452 | encoded | qld-schedule1-table:1238 |
| schedule 1, definition statutory declaration | 1453 | encoded | qld-schedule1-table:1244 |
| schedule 1, definition statutory declaration, paragraph (a) | 1454 | encoded | qld-schedule1-table:1244 |
| schedule 1, definition statutory declaration, paragraph (b) | 1455 | encoded | qld-schedule1-table:1244 |
| schedule 1, definition statutory declaration or solemn declaration | 1456 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition statutory GOC | 1457 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition statutory instrument | 1458 | encoded | qld-schedule1-table:1256 |
| schedule 1, definition statutory rule | 1459 | encoded | qld-schedule1-table:1260 |
| schedule 1, definition stipendiary magistrate | 1460 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition subordinate legislation | 1461 | encoded | qld-schedule1-table:1268 |
| schedule 1, definition subordinate local law | 1462 | encoded | qld-schedule1-table:1272 |
| schedule 1, definition summary | 1463 | encoded | qld-schedule1-table:1276 |
| schedule 1, definition supply | 1464 | encoded | qld-schedule1-table:1280 |
| schedule 1, definition Supreme Court | 1465 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Supreme Court judge or judge | 1466 | encoded | qld-schedule1-table:1288 |
| schedule 1, definition swear | 1467 | encoded | qld-schedule1-table:1292 |
| schedule 1, definition table in the Legislative Assembly | 1468 | encoded | qld-schedule1-table:1296 |
| schedule 1, definition territorial sea of Australia | 1469 | encoded | qld-schedule1-table:1300 |
| schedule 1, definition territorial unit | 1470 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Territory | 1471 | encoded | qld-schedule1-table:1308 |
| schedule 1, definition the Act | 1472 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition the State | 1473 | encoded | qld-schedule1-table:1316 |
| schedule 1, definition this Act | 1474 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition Torres Strait Islander | 1475 | encoded | qld-schedule1-table:1324 |
| schedule 1, definition Torres Strait Islander local government | 1476 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition transfer of an interest in land | 1477 | encoded | qld-schedule1-table:1332 |
| schedule 1, definition transmission of an interest in land | 1478 | encoded | qld-schedule1-table:1336 |
| schedule 1, definition under | 1479 | encoded | qld-schedule1-table:1344 |
| schedule 1, definition under, paragraph (a) | 1480 | encoded | qld-schedule1-table:1344 |
| schedule 1, definition under, paragraph (b) | 1481 | encoded | qld-schedule1-table:1344 |
| schedule 1, definition under, paragraph (c) | 1482 | encoded | qld-schedule1-table:1344 |
| schedule 1, definition under, paragraph (d) | 1483 | encoded | qld-schedule1-table:1344 |
| schedule 1, definition United Kingdom | 1484 | encoded | qld-schedule1-table:1348 |
| schedule 1, definition unit of the public sector | 1485 | repealed or blank in this text | the text shows the defined term followed by ‘...’ and no definition |
| schedule 1, definition valuer-general | 1486 | encoded | qld-schedule1-table:1356 |
| schedule 1, definition will | 1487 | encoded | qld-schedule1-table:1360 |
| schedule 1, definition word | 1488 | encoded | qld-schedule1-table:1364 |
| schedule 1, definition writing | 1489 | encoded | qld-schedule1-table:1368 |
| schedule 1, definition year | 1490 | fork | F25; qld-schedule1-table:1372 |

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the provision, the rule that encodes the reading taken, the reading taken, the other reading, and the text that licenses both.
Where an "unless" or an "except" is met, or a grant or definition limited by a bare "if" is not satisfied, the question has no convention; it is decided at each site on the text’s own words, with one entry here, and the answer taken is NOTHING (the section does not answer) unless the entry says otherwise.
The standing reading for a bare "if" with no "only" is the same: outside the stated cases the section is silent, so the answer is NOTHING.

### F1: s 11

- Rule: `an Act is a public Act (s 11)` in qld-part03-general-provisions.
- Question: what the section answers once its own condition is not met.
- Reading taken: once the Act otherwise expressly provides, s 11 answers NOTHING (the Act's own provision governs).
- Other reading: JUST FALSE (the Act is then not a public Act).
- Text:
  - line 53: “Every Act passed after 26 July 1852 is a public Act unless the Act otherwise expressly provides.”

### F2: s 12(1) and s 12(2)

- Rule: `a private Act does the thing (s 12)` in qld-part03-general-provisions.
- Question: "except so far as it otherwise expressly provides" and the (2) carve-out once met
- Reading taken: NOTHING (the section no longer answers).
- Other reading: JUST TRUE (the Act does the thing).
- Text:
  - line 55: “(1) A private Act does not—”
  - line 56: “(a) affect pre-existing rights in a way prejudicial to the Crown or another person; or”
  - line 57: “(b) impose liabilities on the Crown or another person in relation to previous acts or omissions;”
  - line 58: “except so far as the Act otherwise expressly provides.”
  - line 59: “(2) Subsection (1) does not affect rights conferred, or liabilities imposed, on—”
  - line 60: “(a) a person at whose instance, or for whose special benefit, the Act is passed; or”
  - line 61: “(b) another person claiming by, through or under such a person.”

### F3: s 14B(1)

- Rule: `consideration may be given to extrinsic material for the purpose (s 14B(1))` in qld-part03-general-provisions.
- Question: what the section answers once its own condition is not met.
- Reading taken: each limb of s 14B(1) answers NOTHING when its condition is not met (a grant limited in its own wording).
- Other reading: JUST FALSE (the "if" condition fails).
- Text:
  - line 95: “(1) Subject to subsection (2), in the interpretation of a provision of an Act, consideration may be given to extrinsic material capable of assisting in the interpretation—”
  - line 96: “(a) if the provision is ambiguous or obscure—to provide an interpretation of it; or”
  - line 97: “(b) if the ordinary meaning of the provision leads to a result that is manifestly absurd or is unreasonable—to provide an interpretation that avoids such a result; or”
  - line 98: “(c) in any other case—to confirm the interpretation conveyed by the ordinary meaning of the provision.”

### F4: s 14B(3)

- Rule: `the material is extrinsic material (s 14B(3))` in qld-part03-general-provisions.
- Question: a listed example that forms part of the Act concerned
- Reading taken: JUST FALSE (the "means" limb governs).
- Other reading: JUST TRUE (the example list governs).
- Text:
  - line 103: “(3) In this section—”
  - line 104: “extrinsic material means relevant material not forming part of the Act concerned, including, for example—”

### F5: s 14CA(3)

- Rule: `a former provision is replaced by a corresponding provision (s 14CA(3))` in qld-part03-general-provisions.
- Question: what the section answers once its own condition is not met.
- Reading taken: s 14CA(3) answers NOTHING when none of (a) to (c) holds (no "only").
- Other reading: JUST FALSE.
- Text:
  - line 132: “(3) For this section, a provision of an Act (a former provision) is replaced by a corresponding provision if—”
  - line 133: “(a) an amendment of the Act omits the former provision and inserts a corresponding provision, whether in the same or a different location; or”
  - line 134: “(b) the former provision is amended and the amended provision is a corresponding provision; or”
  - line 135: “(c) the Act is repealed by an Act that includes a corresponding provision to the former provision.”

### F6: s 14F(1)

- Rule: `an Act may be cited in the way (s 14F(1))` in qld-part04-references.
- Question: a way of citing that is neither (a) nor (b)
- Reading taken: NOTHING (the grant names two ways and does not say another is refused).
- Other reading: JUST FALSE.
- Text:
  - line 147: “(1) An Act may be cited—”
  - line 148: “(a) by its short title; or”
  - line 149: “(b) by reference to the year in which it was passed and its number.”

### F7: s 14F(1), examples 1 to 4

- Rule: `an Act may be cited in the way (s 14F(1))` in qld-part04-references.
- Question: example 2 (short title and number together)
- Reading taken: read as a citation by short title, limb (a).
- Other reading: read as a citation by year and number, limb (b).
- Text:
  - line 150: “Examples of citations—”
  - line 151: “1 Statutory Instruments Act 1992”
  - line 152: “2 Statutory Instruments Act 1992, No. 22”
  - line 153: “3 Act No. 22 of 1992”
  - line 154: “4 1992 Act No. 22”

### F8: s 14G(2)

- Rule: `the reference is made according to a copy the section names (s 14G(2))` in qld-part04-references.
- Question: a reference made according to a copy that is not an official copy
- Reading taken: NOTHING (s 14G(2) names the copies and does not say what follows otherwise).
- Other reading: JUST FALSE.
- Text:
  - line 169: “(2) The reference is to be made according to an official copy of—”
  - line 170: “(a) the Act; or”
  - line 171: “(b) the Act as amended.”

### F9: s 15C(3)

- Rule: `s 15C(1) applies to the Act despite anything in the Act (s 15C(3))` in qld-part05-commencement.
- Question: once the Act expressly provides that s 15C(1) does not apply
- Reading taken: NOTHING (this subsection no longer answers; the Act's own provision governs).
- Other reading: JUST FALSE.
- Text:
  - line 212: “(3) Subsection (1) applies to an Act despite anything in the Act unless the Act expressly provides that it does not apply.”

### F10: s 17(3)

- Rule: `the day an instrument or provision necessary under s 17(3) takes effect (s 17(3))` in qld-part05-commencement.
- Question: a day expressed in the instrument that is not later than the day under (c)
- Reading taken: the (c) day applies (the word "later").
- Other reading: the expressed day applies.
- Text:
  - line 266: “(3) If an instrument, or a provision of an instrument, is made under subsection (1) that is necessary for the purpose of—”
  - line 267: “(a) enabling the exercise of a power mentioned in subsection (1)(a); or”
  - line 268: “(b) bringing an appointment, instrument or other thing made or done under such a power into effect;”
  - line 269: “the instrument or provision takes effect—”
  - line 270: “(c) on the making of the instrument; or”
  - line 271: “(d) if the instrument or provision is expressed to take effect at a later time—the later time.”

### F11: s 24B(15)

- Rule: `the document is taken to be the certificate, and to have been properly given (s 24B(15))` in qld-part07-functions-and-powers.
- Question: once the contrary is established
- Reading taken: NOTHING (the presumption is displaced and the subsection no longer answers).
- Other reading: JUST FALSE (the document is not the certificate).
- Text:
  - line 478: “(15) A document purporting to be a certificate mentioned in subsection (14) is taken to be the certificate, and to have been properly given, unless the contrary is established.”

### F12: s 27A(3B)

- Rule: `all conditions and preliminary steps required for the exercise of a delegation are presumed to have been satisfied and performed (s 27A(3B))` in qld-part07-functions-and-powers.
- Question: once the contrary is established
- Reading taken: NOTHING (the presumption is displaced).
- Other reading: JUST FALSE.
- Text:
  - line 514: “(3B) All conditions and preliminary steps required for the exercise of a delegation are presumed to have been satisfied and performed unless the contrary is established.”

### F13: s 32A

- Rule: `the definition applies (s 32A)` in qld-part08a-defined-terms.
- Question: once the context or subject matter otherwise indicates or requires
- Reading taken: NOTHING (the definition's application is then not settled by s 32A).
- Other reading: JUST FALSE.
- Text:
  - line 576: “Definitions in or applicable to an Act apply except so far as the context or subject matter otherwise indicates or requires.”

### F14: s 32DA(6)

- Rule: `a reference to a spouse includes a reference to a de facto partner as defined in s 32DA (s 32DA(6))` in qld-part08a-defined-terms.
- Question: once the Act expressly provides to the contrary
- Reading taken: NOTHING (this subsection no longer answers).
- Other reading: JUST FALSE.
- Text:
  - line 637: “(6) In an Act enacted before the commencement of this section, a reference to a spouse includes a reference to a de facto partner as defined in this section unless the Act expressly provides to the contrary.”

### F15: s 32E

- Rule: `the requirement obliges the person to produce or make available a document reproducing the information in a form capable of being understood (s 32E(c))` in qld-part08a-defined-terms.
- Question: once the court, tribunal or person otherwise directs
- Reading taken: NOTHING (the requirement is then as directed and s 32E(c) and (d) do not answer).
- Other reading: JUST FALSE.
- Text:
  - line 639: “If a person who keeps a record of information by way of a mechanical, electronic or other device is required by or under an Act—”
  - line 640: “(a) to produce the information or a document containing the information to a court, tribunal or person; or”
  - line 641: “(b) to make a document containing the information available for inspection by a court, tribunal or person;”
  - line 642: “then, unless the court, tribunal or person otherwise directs—”
  - line 643: “(c) the requirement obliges the person to produce or make available for inspection, as the case may be, a document that reproduces the information in a form capable of being understood by the court, tribunal or person; and”

### F16: s 35C(2)

- Rule: `the example is part of the provision (s 35C(2))` in qld-part08c-provision-references.
- Question: once the example relates to a different provision
- Reading taken: NOTHING (s 35C(2) no longer answers).
- Other reading: JUST FALSE.
- Text:
  - line 785: “(2) An example of the operation of a provision of an Act at the end of the provision is part of the provision unless the example relates to a different provision.”
  - line 786: “Example of subsection (2)—”
  - line 787: “This example forms part of subsection (2) and an amendment omitting subsection (2) would omit this example.”

### F17: s 37(3), definition post-2023 provision

- Rule: `the provision is a post-2023 provision (s 37(3))` in qld-part09-distance-time-age.
- Question: a provision enacted on the day s 9 commenced
- Reading taken: after (s 9 commences at the beginning of its day, s 15B, so an enactment later in that day is after it).
- Other reading: not after (same day).
- Text:
  - line 820: “(3) In this section—”
  - line 821: “post-2023 provision means a provision enacted after the commencement of the Justice and Other Legislation Amendment Act 2023, section 9.”

### F18: s 38(1); Schedule 1, calendar month and month

- Rule: `the last day of a period beginning on a given day (s 38(1))` in qld-interpretation-time.
- Question: Does a period beginning on a given day exclude that day whatever the unit of the period is?
- Reading taken: Yes, for days, months and years alike.
  A period of calendar months begins at the beginning of the day after the given day.
- Other reading: The exclusion applies to a period of days only; a period of months or years begins at the beginning of the given day itself, so one month from 15 January 2025 would run from 15 January and end on 14 February 2025 (the reading taken gives 15 February 2025).
- Text: Section 38(1) says "If a period beginning on a given day, act or event is provided or allowed for a purpose by an Act, the period is to be calculated by excluding the day" and names no unit (lines 825 to 827).
  Schedule 1 says a calendar month is "a period starting at the beginning of any day of 1 of the 12 named months" (line 1131), which allows a month to start on a given day.

### F19: s 38(1) and (3)

- Rule: `the earliest day of a period of days calculated backwards from a given day (s 38(1) and (3))` in qld-interpretation-time.
- Question: When a period is calculated backwards from a given day, is the given day excluded as it is forwards?
- Reading taken: Yes: the earliest day is n days before the given day, and the given day is not counted.
- Other reading: The given day is counted, so the earliest day is n minus 1 days before it.
- Text: Section 38(1) excludes "the day, or the day of the act or event" for a period "beginning on" it (line 825); section 38(3) speaks of the "earliest day of a period, calculated backwards" (line 829) and does not say how such a period is counted.

### F20: s 38(1)(a) and (2)

- Rule: `the earliest day on which the purpose can be fulfilled after clear days (s 38(1)(a))` in qld-interpretation-time.
- Question: After a number of clear days, is the earliest day on which the thing can be done moved forward off an excluded day?
- Reading taken: No.
  Section 38(2) speaks of the "time, or last day of a period"; the day after the clear days is neither, so it is not moved.
- Other reading: Yes: the earliest day is "the time" calculated forwards for doing a thing, and is moved to the next later day that is not an excluded day.
- Text: Section 38(1)(a) makes the day on which the purpose is to be fulfilled fall outside the period (line 826); section 38(2) moves "the time, or last day of a period, calculated forwards" (line 828).

### F21: s 38(2)

- Rule: `the day a period beginning on a given day ends once moved off an excluded day (s 38(1) and (2))` in qld-interpretation-time.
- Question: Does the move off an excluded day apply to the last day of a period of months or years, or to a period of days only?
- Reading taken: It applies to the last day of a period however the period was counted.
- Other reading: It applies to a period of days only.
- Text: Section 38(2) speaks of "the time, or last day of a period, calculated forwards that is provided or allowed by an Act for doing anything" and names no unit (line 828).

### F22: s 38A

- Rule: `the age in years of a person on a day (s 38A)` in qld-interpretation-time.
- Question: In a year without a 29 February, is the birthday of a person born on 29 February 28 February or 1 March?
- Reading taken: The Act does not choose: for 28 February of such a year the answer is NOTHING, and from 1 March the age has been reached on either reading.
- Other reading: 28 February is the birthday (the age is reached on 28 February), or 1 March is the birthday (the age is not reached until 1 March).
- Text: Section 38A says "a person is an age in years at the beginning of the person’s birthday for the age" (line 836) and the Act does not say which day is the birthday of a person born on 29 February in a year without that day.

### F23: s 45(1) and s 45(2)

- Rule: `the offender may be prosecuted and punished under any of the laws (s 45(1))` in qld-part11-offences.
- Question: once an Act otherwise expressly provides
- Reading taken: NOTHING (s 45(1) then does not answer).
- Other reading: JUST FALSE for the "may not be punished more than once" limb and JUST TRUE for the "may be prosecuted and punished under any" limb.
- Text:
  - line 887: “(1) If an act or omission is an offence under each of 2 or more laws, the offender may be prosecuted and punished under any of the laws, but the offender may not be punished more than once for the same offence.”
  - line 888: “(2) Subsection (1) applies to a law unless an Act otherwise expressly provides.”

### F24: Schedule 1, calendar month and month

- Rule: `the last day of calendar months in succession` in qld-interpretation-time.
- Question: Is a period of N months N calendar months in succession, or one span ending at the day corresponding to the given day N months later?
- Reading taken: N calendar months in succession: each starts at the beginning of the day after the previous one ended.
  Two months from 30 January 2025 end on 31 March 2025.
- Other reading: One span from the first day to the day before the corresponding day N months later.
  Two months from 30 January 2025 would end on 30 March 2025.
- Text: Schedule 1 says "month means a calendar month" (line 1339) and defines a calendar month as a period starting at the beginning of a day and ending immediately before the beginning of the corresponding day of the next named month, or, if there is no such day, at the end of the next named month (lines 1131 to 1133).
  The text defines one month only and says nothing about several.

### F25: Schedule 1, calendar year, financial year and year

- Rule: `the last day of a period beginning on a given day (s 38(1))` in qld-interpretation-time.
- Question: Is a period of N years counted as 12 calendar months for each year from the day after the given day, or as whole calendar years from 1 January?
- Reading taken: 12 calendar months for each year, in succession from the day after the given day.
  Three years from 16 July 2025 end on 16 July 2028.
- Other reading: Whole calendar years: a period of years ends on a 31 December.
- Text: Schedule 1 says "calendar year means a period of 12 months beginning on 1 January" (line 1134), that a financial year is "a period of 1 year beginning on 1 July" (line 1248), and that "year", without specifying the type of year, means calendar year (line 1490).
  The section 15DA example counts 1 year from the assent day of 5 April 1995 to 5 April 1996, which fits twelve months from the day after.

## What the Act turns out to say

Each statement is drawn from the text and ends "Asserted." where a case in the test file named asserts it.
Statements that the Act is silent say so; each of those is asserted as NOTHING.

1. [qld-tests-part03] A provision of an Act that would apart from s 9 be interpreted as exceeding power has effect to the extent to which it does not exceed power, and the remainder of the Act is not affected (s 9(2)). Asserted.
2. [qld-tests-part03] An Act passed on 26 July 1852 itself is not within the words "after 26 July 1852", so s 11 does not answer for it (s 11). Asserted.
3. [qld-tests-part03] An Act passed after the commencement of this Act does not bind the Crown or derogate from a prerogative right of the Crown unless express words are included (s 13). Asserted.
4. [qld-tests-part03] A heading to a section is part of an Act enacted on or before 30 June 1991 only if the heading was amended or inserted after 30 June 1991; a footnote, editor's note or endnote is never part of the Act (s 14(2), (4)). Asserted.
5. [qld-tests-part03] Consideration may be given to extrinsic material to confirm the ordinary meaning only in a case that is neither ambiguous or obscure nor leads to a manifestly absurd or unreasonable result (s 14B(1)(c)). Asserted.
6. [qld-tests-part03] Extrinsic material means relevant material not forming part of the Act concerned (s 14B(3)). Asserted.
7. [qld-tests-part03] If an example and the provision, read in context, are inconsistent, the provision prevails over the example (s 14D(c)). Asserted.
8. [qld-tests-part04] In s 14G, Act includes a Commonwealth Act, an Act of another State, a Territory Act and a British Act; the list is open, so the text does not say that any other kind is not an Act (s 14G(3)). Asserted.
9. [qld-tests-part04] A reference to a law includes the law as originally made and as amended; the remade version is included only if the law has been repealed and remade since the reference was made (s 14H(1)). Asserted.
10. [qld-tests-part04] A reference to a law as repealed or expired is a reference to the law as in force immediately before it was repealed or expired, so the 'repealed ABC Act 1950' is the ABC Act 1950 as then in force (s 14J(1) and its example). Asserted.
11. [qld-tests-part05] A reference to the enactment or passing of an Act is a reference to the fact of the Act's having received the royal assent, so an Act that has not received the royal assent is not enacted or passed in that sense (s 15). Asserted.
12. [qld-tests-part05] An instrument made under s 17(1) that is necessary to enable the power to be exercised takes effect on its making, or on the later time at which it is expressed to take effect (s 17(3)). Asserted.
13. [qld-tests-part05] Anything done under s 17(1) does not confer a right or impose a liability on a person before the relevant empowering provision commences (s 17(5)). Asserted.
14. [qld-tests-part06] If an Act is repealed by another Act, the first Act is not revived merely because the other Act is repealed (s 19(2)). Asserted.
15. [qld-tests-part06] If an Act is amended by another Act, the amendments continue to operate, and the first Act is not revived in its form before the amendments, merely because the other Act is repealed (s 19(3)). Asserted.
16. [qld-tests-part06] The repeal or amendment of an Act does not revive anything not in force or existing at the time, nor affect its previous operation, accrued rights, penalties, investigations, the proof of anything, savings, repeals or transitional effects (s 20(2), (4)). Asserted.
17. [qld-tests-part06] The "declaratory or validating effect" of an Act that declares a thing for a saving or transitional purpose, "validates" a thing, or declares a thing consequentially does not end merely because the Act is repealed (s 20A(2)). Asserted.
18. [qld-tests-part06] An act or omission that an Act makes an offence is only an offence if committed after the Act commences (s 20C(2)). Asserted.
19. [qld-tests-part06] Repealed provisions that an Act replaces by new provisions continue in force until the new provisions commence (s 21). Asserted.
20. [qld-tests-part06] An amending Act is an Act that consists only of the listed types of provision, so one extra provision of another type takes it outside the definition (s 22C(4)). Asserted.
21. [qld-tests-part07] The performance of a function, or the exercise of a power, by a body is not affected merely because of vacancies in its membership (s 23(3)). Asserted.
22. [qld-tests-part07] Anything done by or in relation to a person purporting to act in an office is not invalid merely because the occasion for the appointment had not arisen, the appointment had ended, or the occasion to act had not arisen or had ended (s 24B(9)). Asserted.
23. [qld-tests-part07] The appointment of a person to an office, to act, to exercise a power or to do anything else is not "invalid" merely because of a "defect or irregularity" in relation to the appointment (s 26). Asserted.
24. [qld-tests-part07] A delegated function or power may be exercised only in accordance with the conditions of the delegation (s 27A(4)). Asserted.
25. [qld-tests-part07] A function or power may be subdelegated only if the Act expressly authorises it to be subdelegated (s 27A(12)). Asserted.
26. [qld-tests-part07] Where an Act requires a decision-maker to give written reasons, the instrument giving them must also set out the findings on material questions of fact and refer to the evidence on which the findings were based (s 27B). Asserted.
27. [qld-tests-part08a] Definitions in or applicable to an Act apply except so far as the context or subject matter otherwise indicates or requires; once it does, s 32A does not settle the application (s 32A). Asserted.
28. [qld-tests-part08a] A non-exhaustive definition for another Act does not exclude or limit, but may extend, the meaning given by this Act's definition (s 32AB(c)). Asserted.
29. [qld-tests-part08a] If the two definitions, read in context, are inconsistent, the Interpretation Act definition is displaced (s 32AB(d)). Asserted.
30. [qld-tests-part08a] Two persons are de facto partners if they live together as a couple on a genuine domestic basis and are neither married to each other nor related by family (s 32DA(1)). Asserted.
31. [qld-tests-part08a] Two persons are not to be regarded as living together as a couple on a genuine domestic basis only because they have a common residence (s 32DA(4)). Asserted.
32. [qld-tests-part08b] Where a provision is administered by 2 or more Ministers and authorises anything to be done by or in relation to any 1 of them, it does not authorise or require it to be done in a particular case by or in relation to more than 1 of them (s 33AC). Asserted.
33. [qld-tests-part09] In applying a pre-2023 provision, distance is measured along the shortest road ordinarily used for travelling unless there is a contrary intention (s 37(1)); in applying a post-2023 provision, in a straight line on a horizontal plane (s 37(2)). Asserted.
34. [qld-tests-part10] A document may be served on an individual by delivering it personally, by leaving it at, or by sending it by post, telex, facsimile or similar facility to, the last known address of residence or business (s 39(1)(a)). Asserted.
35. [qld-tests-part11] Where a minimum as well as a maximum penalty is specified at the end of a section, the offence is punishable by a penalty not less than the minimum and not more than the maximum (s 41(d)). Asserted.
36. [qld-tests-part11] The part of an amount recovered that is ordered to be paid to the party prosecuting is paid first, and the remaining part is paid to the consolidated fund (s 43(1)). Asserted.
37. [qld-tests-part11] If an act or omission is an offence under each of 2 or more laws, the offender may be prosecuted and punished under any of the laws, but may not be punished more than once for the same offence (s 45(1)). Asserted.
38. [qld-tests-part12] The laws of the State are the laws in force in the State, written or unwritten, substantive or procedural, other than laws of the Commonwealth and criminal laws (s 47). Asserted.
39. [qld-tests-part12a] Forms under an authorising law must be numbered so that each form has a unique number, so two forms with the same number do not meet s 48(3). Asserted.
40. [qld-tests-part12a] A form that requires a specified way of completion, specified information or documents, or verification in a specified way is not properly completed unless the requirement is complied with (s 48A(2)). Asserted.
41. [qld-tests-part12b] The value of a fee unit for an Act is the amount prescribed, or $1 if no amount is prescribed (s 48B(4)). Asserted.
42. [qld-tests-part13] Where an Act requires verification in a specified way, the purpose is not fulfilled unless the requirement is satisfied; that it is satisfied does not by itself say the purpose is fulfilled (s 49). Asserted.
43. [qld-tests-part14] For a Bill introduced before the commencement of s 53, the speech in s 14B(3)(f) is taken to be the speech made in moving that the Bill be read a second time (s 53(2)). Asserted.
44. [qld-tests-schedule1-terms] An adult is an individual who is 18 or more; a minor, and a child where age rather than descendancy is relevant, is an individual who is under 18 (Schedule 1). Asserted.
45. [qld-tests-schedule1-terms] State means a State of the Commonwealth and includes the Australian Capital Territory and the Northern Territory; a Territory such as the Jervis Bay Territory is not a State (Schedule 1). Asserted.
46. [qld-tests-time] The midnight of a day is the point of time at which the day ends, which is the same point of time as the beginning of the next day (Schedule 1, midnight). Asserted.
47. [qld-tests-time] If the day fixed by a proclamation for the commencement of an Act or provision comes before the day on which the proclamation is notified, the Act or provision commences on the notification day (s 15D(2)). Asserted.
48. [qld-tests-time] An amending Act enacted after 30 June 1994 is automatically repealed at the beginning of the day after all of its provisions have commenced (s 22C(1)). Asserted.
49. [qld-tests-time] A postponed law enacted after 31 December 1994 that has not commenced within 1 year of the assent day automatically commences on the next day, and a regulation made within that year may extend the period to not more than 2 years of the assent day (s 15DA(2), (3) and (5)). Asserted.
50. [qld-tests-time] A calendar month starting at the beginning of a day ends immediately before the beginning of the corresponding day of the next named month, or, if there is no such day, at the end of the next named month (Schedule 1, calendar month). Asserted.
51. [qld-tests-time] A calendar year is a period of 12 months beginning on 1 January, and a financial year is a period of 1 year beginning on 1 July (Schedule 1, calendar year and financial year). Asserted.
52. [qld-tests-time] A period beginning on a given day, act or event is calculated by excluding that day, or the day of the act or event (s 38(1)). Asserted.
53. [qld-tests-time] The Act does not define "week", so it does not say how long a period of weeks is, and a period of weeks is not answered (silent). Asserted.
54. [qld-tests-time] For a period expressed as a specified number of clear days or at least a specified number of days the day on which the purpose is to be fulfilled is excluded as well; in any other case it is included (s 38(1)(a) and (b)). Asserted.
55. [qld-tests-time] A business day is a day that is not a Saturday or Sunday and not a public holiday, special holiday or bank holiday in the place in which any relevant act is to be or may be done (Schedule 1, business day). Asserted.
56. [qld-tests-time] For filing or registering a document an excluded day is a day on which the office is closed where the filing or registration must or may be done; otherwise it is a day that is not a business day in the place in which the thing must or may be done (s 38(5)). Asserted.
57. [qld-tests-time] If the time, or last day of a period, calculated forwards for doing anything falls on an excluded day, it is taken to fall on the next later day that is not an excluded day (s 38(2)). Asserted.
58. [qld-tests-time] If the time, or earliest day of a period, calculated backwards for doing anything falls on an excluded day, it is taken to fall on the next earlier day that is not an excluded day (s 38(3)). Asserted.
59. [qld-tests-time] If no time is provided or allowed for doing anything, the thing is to be done as soon as possible, and as often as the relevant occasion happens (s 38(4)). Asserted.
60. [qld-tests-time] A person is an age in years at the beginning of the person's birthday for the age (s 38A). Asserted.
61. [qld-tests-time] Service by post is taken to have been effected at the time at which the letter would be delivered in the ordinary course of post, unless the contrary is proved; once the contrary is proved the Act gives no time (s 39A(1)(b)). Asserted.
62. [qld-tests-time] The term of an acting appointment made because of a vacancy may not be more than 1 year (s 24B(5)(a)). Asserted.
63. [qld-cases-seat] An Act that does not expressly provide otherwise commences on the date of assent; if it does expressly provide otherwise, s 15A does not say when it commences (s 15A). Asserted.
64. [qld-cases-seat] An instrument made before its enabling law commences takes effect on the day it is made, or on the later day at which it is expressed to take effect, if it is necessary to enable the power to be exercised or brought into effect (s 17(3)). Asserted.
65. [qld-cases-seat] A provision that commences on a day is in force from the beginning of that day, not from its end (s 15B). Asserted.
66. [qld-cases-seat] A provision that expires on a day, or that remains in force until a day, has effect until the end of that day (s 18). Asserted.
67. [qld-cases-seat] A period of days beginning on a given day excludes that day and includes the last day, so thirty days from 1 January 2026 end on 31 January 2026 (s 38(1)). Asserted.
68. [qld-cases-seat] Two months from 31 December 2025 end on 28 February 2026, the last day of the second calendar month, which begins on the day after the given day (Schedule 1 "calendar month", s 38(1)). Asserted.
69. [qld-cases-seat] For a thing other than filing or registering a document, an excluded day is a day that is not a business day, that is a Saturday, a Sunday or a public holiday, special holiday or bank holiday in the place (s 38(5)(b), Schedule 1 "business day"). Asserted.
70. [qld-cases-seat] A document that an Act requires or permits to be served on an individual may be served by delivering it personally, by leaving it at, or by sending it by post to, the last known address of residence or business (s 39(1)). Asserted.

## The six worked time cases

Each case is asserted in `qld-cases-seat.l4` through the questions "On which day does my period of days, months or years end", and in `qld-tests-time.l4` through the module functions.
The last day counted is the last day of the period under s 38(1) with Schedule 1 (a calendar month ends immediately before the beginning of the corresponding day of the next named month, or at the end of the next named month if there is none; a year is read as twelve calendar months).
The next column applies s 38(2) to a thing other than filing or registering a document, with no public, special or bank holiday and no closed office: Saturday, Sunday and holidays are excluded days (s 38(5)(b), Schedule 1 "business day").
For filing or registering a document an excluded day is a day the office is closed (s 38(5)(a)); with no closed day listed the last day does not move.
The weekday of each date was read from a calendar.

| Case | Section | Last day counted | Weekday | Taken to fall on (s 38(2), not filing) | Filing, no closed day | Fork |
| --- | --- | --- | --- | --- | --- | --- |
| three years from 2025-07-16 | s 38(1), Schedule 1 calendar year | 2028-07-16 | Sunday | 2028-07-17 | 2028-07-16 | F18, F24, F25, F21 |
| five years from 2025-01-15 | s 38(1), Schedule 1 calendar year | 2030-01-15 | Tuesday | 2030-01-15 | 2030-01-15 | F18, F24, F25 |
| five years from 2025-09-01 | s 38(1), Schedule 1 calendar year | 2030-09-01 | Sunday | 2030-09-02 | 2030-09-01 | F18, F24, F25, F21 |
| thirty days from 2026-01-01 | s 38(1) | 2026-01-31 | Saturday | 2026-02-02 | 2026-01-31 | none |
| two months from 2025-12-31 | s 38(1), Schedule 1 calendar month | 2026-02-28 | Saturday | 2026-03-02 | 2026-02-28 | F18, F24, F21 |
| one month from 2024-01-31 | s 38(1), Schedule 1 calendar month | 2024-02-29 | Thursday | 2024-02-29 | 2024-02-29 | F18, F24 |
| one year from 2024-02-29 | s 38(1), Schedule 1 calendar year | 2025-02-28 | Friday | 2025-02-28 | 2025-02-28 | F18, F24, F25 |

The Act is silent on the length of a period of weeks, so a period of weeks is answered NOTHING (asserted).
The Act is silent on the time of day at which a letter would be delivered in the ordinary course of post, so that time is an input to the s 39A(1)(b) question.
The "Fork" column refers to the entries of the fork register above that bear on the case.

## Cross-references

The cross-reference module `qld-xrefs` holds 227 references from one provision of the Act to another provision of the same text, and 112 references to another Act or instrument.
Of the 227 references within the Act, by the words printed: subsection 83, this section 53, section 51, paragraph 24, this part 8, schedule 5, this subsection 2, this division 1.
The references to other instruments are rows of their own kind, carrying the instrument and provision as printed; they are not resolved here.
The script that found them reads the text file one row at a time and looks, by regular expression, for the words section, subsection, paragraph, subparagraph, part, division and schedule followed by a number or letter (including lists such as "sections 19 to 20A"), for "this section", "this subsection", "this part" and "this division", and for ", definition <term>" after a cited section or schedule.
It does not read words between single quotation marks, nor the made-up citations in the illustrations of ss 32F, 35B and 35D and in the illustrations of a definition in Schedule 1.
A reference such as "subsection (1)" or "paragraph (a)" is resolved as s 35B(5) says, to the subsection or section where it occurs.
A reference to another instrument is found by the pattern of a title ending in Act, Code or Law followed by a year, and by the Constitution of Queensland 2001, and is recorded with the provision printed after it.
Each row has a test asserting that the cited identifier is in the index under the heading the row gives (`qld-tests-xrefs`).
A scan by regular expression can miss a reference that is phrased in an unusual way; the count is the count of what the script found.

## What the stable binary does not accept

The binary governs where the skills describe something it rejects.
Loud failures (an error is printed) and silent ones (a changed meaning with a clean run) are separated, because the silent ones are the ones to watch.

Silent:
- `NOT a AND NOT b` parses as `NOT (a AND NOT b)`, so a negated condition joined by AND changes meaning without a message; every `NOT` that shares a condition with `AND` or `OR` is parenthesised in this encoding, and a `NOT` that is the whole condition (`IF NOT x THEN`, `#ASSERT NOT f x`) is left bare.

Loud:
- Chained `ELSE IF` needs the `THEN` and `ELSE` indented under the `IF`; otherwise the error is "incorrect indentation (got 10, should be greater than 10)".
- `length` is not defined; `count` is.
- `count OF (...) EQUALS 3` mis-parses with a type error; the call is parenthesised: `(count (...)) EQUALS 3`.
- `JUST e’s field` mis-parses with a type error ("trying to apply e... to 1 argument"); it is written `JUST (e’s field)`.
- An inline `(Type OF ...)` as an element of a `LIST` gives a parse error; the elements are named fixtures with `MEANS`.
- A continuation line of an `#ASSERT` is rejected, so every assertion is on one line.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used.

Both builds agree on every module (see below); there is no construct here that one accepts and the other reads differently.

## What check.sh prints

Run from the encoding folder with `L4=<the 1.6.98 build> L4_MAIN=<the 1.6.110 build> ./check.sh` (each build is identified by its version line, and the writing build by its sha256, in `encoding.json`).
The columns are errors, assertions satisfied, failed and refused, then the expected failed count, then the same four counts for the main build; a module whose counts differ would be marked, and none is.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
qld-cases-seat.l4                              0        96       0        0         0 |      0        96       0        0  same
qld-interpretation-time.l4                     0         0       0        0         0 |      0         0       0        0  same
qld-part01-preliminary.l4                      0         0       0        0         0 |      0         0       0        0  same
qld-part02-meaning-of-act.l4                   0         0       0        0         0 |      0         0       0        0  same
qld-part03-general-provisions.l4               0         0       0        0         0 |      0         0       0        0  same
qld-part04-references.l4                       0         0       0        0         0 |      0         0       0        0  same
qld-part05-commencement.l4                     0         0       0        0         0 |      0         0       0        0  same
qld-part06-amendment-and-repeal.l4             0         0       0        0         0 |      0         0       0        0  same
qld-part07-functions-and-powers.l4             0         0       0        0         0 |      0         0       0        0  same
qld-part08a-defined-terms.l4                   0         0       0        0         0 |      0         0       0        0  same
qld-part08b-ministers-and-offices.l4           0         0       0        0         0 |      0         0       0        0  same
qld-part08c-provision-references.l4            0         0       0        0         0 |      0         0       0        0  same
qld-part09-distance-time-age.l4                0         0       0        0         0 |      0         0       0        0  same
qld-part10-service-of-documents.l4             0         0       0        0         0 |      0         0       0        0  same
qld-part11-offences.l4                         0         0       0        0         0 |      0         0       0        0  same
qld-part12-coastal-waters.l4                   0         0       0        0         0 |      0         0       0        0  same
qld-part12a-forms.l4                           0         0       0        0         0 |      0         0       0        0  same
qld-part12b-fee-units.l4                       0         0       0        0         0 |      0         0       0        0  same
qld-part13-miscellaneous.l4                    0         0       0        0         0 |      0         0       0        0  same
qld-part14-transitional.l4                     0         0       0        0         0 |      0         0       0        0  same
qld-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
qld-schedule1-table.l4                         0         0       0        0         0 |      0         0       0        0  same
qld-schedule1-terms.l4                         0         0       0        0         0 |      0         0       0        0  same
qld-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
qld-tests-part01.l4                            0        10       0        0         0 |      0        10       0        0  same
qld-tests-part02.l4                            0        10       0        0         0 |      0        10       0        0  same
qld-tests-part03.l4                            0       100       0        0         0 |      0       100       0        0  same
qld-tests-part04.l4                            0        57       0        0         0 |      0        57       0        0  same
qld-tests-part05.l4                            0        53       0        0         0 |      0        53       0        0  same
qld-tests-part06.l4                            0       104       0        0         0 |      0       104       0        0  same
qld-tests-part07.l4                            0       170       0        0         0 |      0       170       0        0  same
qld-tests-part08a.l4                           0        79       0        0         0 |      0        79       0        0  same
qld-tests-part08b.l4                           0        82       0        0         0 |      0        82       0        0  same
qld-tests-part08c.l4                           0        81       0        0         0 |      0        81       0        0  same
qld-tests-part09.l4                            0        11       0        0         0 |      0        11       0        0  same
qld-tests-part10.l4                            0        25       0        0         0 |      0        25       0        0  same
qld-tests-part11.l4                            0        45       0        0         0 |      0        45       0        0  same
qld-tests-part12.l4                            0        32       0        0         0 |      0        32       0        0  same
qld-tests-part12a.l4                           0        52       0        0         0 |      0        52       0        0  same
qld-tests-part12b.l4                           0        15       0        0         0 |      0        15       0        0  same
qld-tests-part13.l4                            0        42       0        0         0 |      0        42       0        0  same
qld-tests-part14.l4                            0        32       0        0         0 |      0        32       0        0  same
qld-tests-schedule1-table.l4                   0       927       0        0         0 |      0       927       0        0  same
qld-tests-schedule1-terms.l4                   0        86       0        0         0 |      0        86       0        0  same
qld-tests-time.l4                              0       117       0        0         0 |      0       117       0        0  same
qld-tests-xrefs.l4                             0       359       0        0         0 |      0       359       0        0  same
qld-xrefs.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (47 modules)                             0      2585       0        0           |      0      2585       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Before this encoding is relied on

1. A lawyer who knows Queensland drafting should read the fork register against the text and overrule any reading they dislike; the entries are listed above with the other reading beside each.
2. Every module should be compared with the authorised version of the Act, because the text encoded is a plain-text rendering and not the official text.
3. The version encoded is the one in force from 2024-02-01; later amendments, and the commencement dates of provisions that the sources do not state, are not reflected.
4. The holidays, special holidays, bank holidays and closed days of the place are inputs; a person using the seat layer must supply them from the instrument that appoints them.
5. The seat questions take lists of dates; the website form has not been tried with them, and a form that cannot take a list would need one question per date or a fixed number of date inputs.
6. The references to other Acts and instruments are recorded, not resolved; the value of a fee unit, the time of ordinary post and every date that the Act borrows from another instrument are inputs.
7. The coverage dispositions were assigned by a script from the places where each row’s lines are quoted; a reviewer should spot-check rows marked `encoded` against the rule named in the `Where` column.

## The text, and its licence

The text is the plain-text rendering `act-1954-003.txt` (version 2024-02-01 of the Acts Interpretation Act 1954, retrieved 2026-11-11); it is not the official text, and the converter dropped amendment-history notes, links and bold marking.
Quoted lines are marked `-- src:N |` and checked against the file by `srcrefs.py`.
The terms the quoted text carries are in `SOURCE-LICENSE.md`, which points at the subject-level note.


The numbers in this file were produced on 2026-11-11 with the builds named at the top.
