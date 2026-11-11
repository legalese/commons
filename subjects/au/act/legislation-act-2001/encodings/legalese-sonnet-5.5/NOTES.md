# Legislation Act 2001 (Australian Capital Territory): encoding `legalese-sonnet-5.5`

Status: draft.
No domain expert has read this encoding against the authorised text.
It was written by a single Sonnet 5.5 agent working alone from `BRIEF.md`.
The target compiler is `main`, as the brief says.
The checks recorded below were run with the stable build 1.6.98 (main, 7689b0d, 2026-10-19) and compared with the main build 1.6.110 (main, e51181d, 2026-11-11).

## The text and the method

The text encoded is `registers/source-bundle/A2001-14.txt`: Republication No 126 of the Legislation Act 2001 (ACT), effective 2026-02-23.
It is a plain-text conversion, made by a script, of the DOCX file that the ACT publishes marked "Unauthorised version prepared by ACT Parliamentary Counsel's Office".
It is not the authorised republication, and nothing here has been compared with the authorised text.
The terms of the source are in `SOURCE-LICENSE.md` and, for the subject as a whole, in `../../SOURCE-LICENSE.md`.

The method, in the order the work was done:

1. A script splits the text into units: every chapter, part, division, section, subsection, paragraph, table row, definition, example and note, each with its line range.
2. The nouns of the Act (kinds of law, instrument, entity and period) are declared once in `act-nouns.l4`, and the rules for time (commencement, repeal, ages, periods, service) are in one module, `act-interpretation-time.l4`, that the chapter modules import and never restate.
3. Each chapter has one module; each rule is named for the provision it encodes, quotes the provision's words in `-- src:N | ...` comment lines, and carries an `@ref` locator.
   The quotation lines and the locators are written by a script that reads the text file, so none is typed by hand.
4. Each module has a test file whose assertions are written from the section named beside them.
5. `srcrefs.py` checks that every quoted line is a verbatim slice of the text line it names and that every `@ref` locator lies inside the quoted ranges; it does not check that a locator names the right provision.
6. A script lists every unit and gives it one disposition (the coverage table below), and reports any non-blank line of the in-scope text that falls outside a row and any encoded rule that has no test.
7. The seat layer (`act-seat.l4`, `act-cases-seat.l4`) calls the layer-1 rules and restates none.

Where the text says no, the rule answers `JUST FALSE`: a means or "is" definition, "if and only if", "unless", a flat negative, a fixed period.
Where the text only includes, lists without closing the list, or is silent, the rule answers `NOTHING`.
A "may be done" rule answers `JUST TRUE` when the facts match a listed way and `NOTHING` otherwise.
Where a `NOTHING` stands in for a reading the text does not choose between, the place is a fork below.

## Seat

The seat is a person who has a time limit to meet under an ACT Act or subordinate law (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, and who asks on which day their period ends and which of their days count.
The Legislation Act is the Act that says how those periods are counted, when a law begins and ends, how old a person is on a day, what a penalty unit is worth in dollars, and when a served document is taken to be served.
Those are the places where the Act decides something about a particular person's deadline or payment, so those are the questions.
The rest of the Act (how legislation is made, notified and republished, and what its parts mean) speaks to officials and drafters; it is encoded in layer 1 for what it decides and is not asked about from a seat.
There is no seat for an official.
`act-seat.l4` holds 24 questions in the order of the Act, each with `@export` and `@desc`.
`act-cases-seat.l4` holds the worked cases: at least one for every question, and a group of cases outside the encoding.

### What the seat questions leave out

A day is asked as a day.
The time of day within it is not asked, so a commencement the law fixes at a stated time is entered as the day it falls on and read as the start of that day.
The Holidays Act 1958 is named in the dictionary entries for public holiday (section 3) and bank holiday (section 4) and is not among the sources.
So public holidays, bank holidays and days an office is closed are asked as up to three days "that do not count", used for all three purposes at once.
For something done at an office a day is a working day when the office is open, so Saturdays and Sundays on which the office is closed must be among the three days given.
If more than three days in a row do not count, the answer may fall on a day that does not count.
Whether `s 151` and `s 151A` apply to a law enacted or made on or before 1 January 2006, and what a contrary intention does to them, is worked out from the date the law was enacted or made and three yes-or-no answers.
A provision inserted after that date into an older law is not asked.
The dollar figures in `s 133` ($160 for an individual, $810 for a corporation) are the text's own; a later amendment would change those answers.

## Jural relations

Most provisions of an interpretation Act define a term, count a period or say how words are read, and create no relation between two parties.
Those are grouped in the `none` rows at the end of the table.
The provisions that do create or change a relation are listed one by one.
Where the text names no holder or no bearer, the cell says so.

| Holder (right, privilege, power or immunity) | Bearer (duty, no-right, liability or disability) | Section | Module and rule |
|---|---|---|---|
| A person whom a prejudicial provision of a statutory instrument would disadvantage (immunity) | The maker of the instrument (disability, unless an Act displaces the rule) | s 76 (2) | `act-ch8-commencement.l4`: `s 76 (2): a statutory instrument can provide that the prejudicial provision commences retrospectively` |
| The maker of a statutory instrument (power to make a non-prejudicial provision commence retrospectively) | The text names none | s 76 (1) | `act-ch8-commencement.l4`: `s 76 (1): a statutory instrument may provide that the provision commences retrospectively` |
| The entity that holds a power under a law that is notified and not yet commenced (power to exercise it, and to do things to bring the law into operation) | The text names none | s 81 (3), (5) | `act-ch8-commencement.l4`: `s 81 (3): the power may be exercised at any time even though the authorising law is not in force`; `s 81 (5): anything else may be done under the power at any time for the purpose of bringing the authorising law into operation` |
| A person with a right, privilege or liability acquired, accrued or incurred under a law (immunity from its being affected by repeal or amendment) | The repeal or amendment (disability); the text names no person | s 84 (1), (3) | `act-ch9-repeal-and-amendment.l4`: `s 84 (1), (3): the repeal or amendment of a law affects the thing` |
| A person with an existing right, privilege or liability under a repealed or amended law (power to start, exercise, continue or complete a remedy and have the right enforced) | The text names none | s 84 (2) | `act-ch9-repeal-and-amendment.l4`: `s 84 (2): the investigation, proceeding or remedy may be started, exercised, continued or completed as if the repeal or amendment had not happened` |
| A person who did or omitted something before a law commences (immunity from its being an offence, or from an increase in the penalty) | The text names none; the rule limits the reach of the law itself | s 84A (1), (2) | `act-ch9-repeal-and-amendment.l4`: `s 84A (1): the act or omission is an offence`; `s 84A (2): the increase in the penalty applies to the offence` |
| The Territory (immunity from an Act's requirement to pay money that would form part of its public money); a government (immunity from prosecution); a government entity (the same immunity for an authorised act or omission) | The text names none | s 121 (2), (3), (4) | `act-ch12-scope.l4`: `s 121 (3): subsection (1) makes the subject liable to be prosecuted for an offence`; `s 121 (4): the same degree of immunity extends to the government entity` |
| A person who applies to a court or other entity for a time to be extended even though it has ended (power to apply) | The court or other entity (liability to be applied to) | s 151C (2) | `act-ch15-aids.l4`: `s 151C (2): a person may apply for the relevant time to be extended` |
| The court or other entity that has power to extend a time (power to extend it even though it has ended) | The person whose time has ended (liability to have it extended) | s 151C (3) | `act-ch15-aids.l4`: `s 151C (3): the court or other entity may extend the relevant time` |
| The text names none | The person required to do an act (duty, which continues until the act is done) | s 152 | `act-ch15-aids.l4`: `s 152: the obligation to do the act continues` |
| The text names none | A corporation (duty under a provision that creates an offence) | s 161 (1), (2) | `act-ch15-aids.l4`: `s 161 (1), (2): a provision of a law that creates an offence applies to the party` |
| A court (power to impose, on a corporation convicted where the penalty is imprisonment only, a maximum penalty in penalty units) | A corporation convicted of such an offence (liability) | s 161 (3) | `act-ch15-aids.l4`: `s 161 (3): the most the court may impose on the corporation, in penalty units` |
| The text names none | The Attorney-General (duty to review the amount of a penalty unit at least once every 4 years) | s 133 (3) | `act-ch13-structure.l4`: `s 133 (3): the last day by which the Attorney-General must have reviewed the amount of a penalty unit` |
| A person with the common law privileges against self-incrimination and exposure to a civil penalty, or the common law client legal privilege (privilege, preserved in the interpretation of an Act or instrument) | The text names none | s 170 (1), s 171 (1) | `act-ch15-aids.l4`: `s 170 (1): the thing must be interpreted to preserve the common law privileges against self-incrimination and exposure to the imposition of a civil penalty`; `s 171 (1): the thing must be interpreted to preserve the common law privilege in relation to client legal privilege` |
| An entity given a function by a law (power to do what is necessary and convenient to exercise it, and to exercise it from time to time) | The text names none | s 196 (1), s 197 | `act-ch19-functions-and-service.l4`: `s 196 (1): the provision also gives the entity the powers necessary and convenient to exercise the function`; `s 197: the function may be exercised from time to time` |
| A body given a function (power to exercise it by resolution, and as constituted for the time being); the occupant of a position (power to exercise the function given to the position) | The text names none | s 199 (1), (4), s 200 (1) | `act-ch19-functions-and-service.l4`: `s 199 (1): the body may exercise the function by resolution`; `s 199 (4): the function may be exercised by the body as constituted for the time being`; `s 200 (1): the function may be exercised by the person for the time being occupying the position` |
| The text names none | An individual, a corporation or an agency on whom a document is served (liability to be served in a listed way); the text says that a document "may be served" and does not say who serves it | s 247 (1), s 248 (1), s 249 | `act-ch19-functions-and-service.l4`: `s 247 (1): the document may be served on an individual in this way`; `s 248 (1): the document may be served on a corporation in this way`; `s 249: the document may be served on an agency in this way` |
| A law, or a regulation under an Act (power to fix the way, the address or the date of service of a document of a particular kind); a court or tribunal (power to authorise or require another way of service) | The text names none | s 251 (2), s 252 | `act-ch19-functions-and-service.l4`: `s 251 (2) (a): a law may provide that a document of a particular kind may or must be served only in a particular way or to a particular address or number`; `s 252: this part affects the power of a court or tribunal to authorise or require service of a document otherwise than as provided under this part` |
| none | none | Chapter 1 Preliminary (Parts 1.1, 1.2, 1.3): name, dictionary, determinative provisions, basic concepts, sources of law | `act-ch1-preliminary.l4`, `act-determinative.l4`, `act-nouns.l4` |
| none | none | Chapter 8 Commencement and exercise of powers before commencement, apart from the rows above: when a law commences, retrospective commencement, commencement notices, postponed laws | `act-ch8-commencement.l4`, `act-interpretation-time.l4` |
| none | none | Chapter 9 Repeal and amendment of laws, apart from the rows above: when a repeal takes effect, automatic repeal, the effect of amendment | `act-ch9-repeal-and-amendment.l4`, `act-interpretation-time.l4` |
| none | none | Chapter 10 Referring to laws | `act-ch10-referring-to-laws.l4` |
| none | none | Chapter 12 Scope of Acts and statutory instruments, apart from s 121 (2) to (4) | `act-ch12-scope.l4` |
| none | none | Chapter 13 Structure of Acts and statutory instruments, apart from s 133 (3): what is part of an Act, definitions, examples, penalty units and how penalties are read | `act-ch13-structure.l4` |
| none | none | Chapter 14 Interpretation of Acts and statutory instruments | `act-ch14-interpretation.l4` |
| none | none | Chapter 15 Aids to interpretation, apart from the rows above: how words are read, how periods of time are counted, definitions, references to entities and things | `act-ch15-aids.l4`, `act-interpretation-time.l4` |
| none | none | Parts 19.1, 19.2 and 19.5 apart from the rows above: the start of Chapter 19, the rest of the rules about functions, and when a served document is taken to be served | `act-ch19-functions-and-service.l4`, `act-interpretation-time.l4` |
| none | none | The in-section definitions and the dictionary entries | `act-section-definitions.l4`, `act-dictionary.l4` |

## What is encoded and what is not

Encoded in full: Chapter 1 (Parts 1.1 to 1.3), Chapter 8, Chapter 9 (Parts 9.1 to 9.3), Chapter 10, Chapter 12, Chapter 13 (Parts 13.1 and 13.2), Chapter 14 (Parts 14.1 and 14.2), Chapter 15 (Parts 15.1 to 15.4), Parts 19.1, 19.2 and 19.5, and the dictionary entries that an in-scope provision uses or that are about time, commencement, laws, instruments and the Territory.
Not encoded, one `out of scope` row each in the coverage table: Chapters 2 to 7, Chapter 11, Chapters 16 to 18, Parts 19.3, 19.4, 19.6 and 19.7, Chapter 20, Schedule 1, the endnotes, and the dictionary entries that no in-scope provision uses and that are not about those subjects.
The scope table is the brief's, and the brief calls it an assumed scope choice, not a ruling.

The layer-1 modules, in reading order:

- `act-ch1-preliminary.l4`
- `act-ch10-referring-to-laws.l4`
- `act-ch12-scope.l4`
- `act-ch13-structure.l4`
- `act-ch14-interpretation.l4`
- `act-ch15-aids.l4`
- `act-ch19-functions-and-service.l4`
- `act-ch8-commencement.l4`
- `act-ch9-repeal-and-amendment.l4`
- `act-determinative.l4`
- `act-dictionary.l4`
- `act-interpretation-time.l4`
- `act-nouns.l4`
- `act-provisions.l4`
- `act-section-definitions.l4`
- `act-xrefs.l4`

The test files:

- `act-tests-ch1.l4`
- `act-tests-ch10.l4`
- `act-tests-ch12.l4`
- `act-tests-ch13.l4`
- `act-tests-ch14.l4`
- `act-tests-ch15.l4`
- `act-tests-ch19.l4`
- `act-tests-ch8.l4`
- `act-tests-ch9.l4`
- `act-tests-determinative.l4`
- `act-tests-dictionary.l4`
- `act-tests-section-definitions.l4`
- `act-tests-time.l4`
- `act-tests-xrefs.l4`

The seat layer: `act-seat.l4` and `act-cases-seat.l4`.

Headings and notes are inert (reason 1 of the brief) because a heading and a note are not part of the Act (`s 127 (1)`, encoded in `act-ch13-structure.l4`).
Examples are encoded as cases in a test file, each with a comment naming the section and the example.

## Coverage table

Every non-blank line of the in-scope text falls in some row; a script checks this and finds no line outside a row.
The table has 1142 rows: 802 encoded, 270 inert, 52 fork, 18 out of scope.
Each `encoded` and `fork` row names the rule in its module and the test file that exercises it.
A rule counts as tested when a test file calls it by name, calls a rule of the same module that uses it, or (for the generated determinative constants) tests the status through `act-tests-determinative.l4`.
The in-section definitions are tested in `act-tests-section-definitions.l4` and the dictionary entries in `act-tests-dictionary.l4`.
No provision of the in-scope text is shown repealed or blank, so no row has the disposition `repealed or blank in this text`.

| Lines | Provision | Disposition | Rule, reason or fork | Test |
|---|---|---|---|---|
| 1-67 | Notice of the unofficial conversion, cover, title and long title | inert | reason 1: not operative; the notice is the converter's; the title and long title create no rule |  |
| 68 | Chapter 1 Preliminary | inert | reason 1: not operative; a heading |  |
| 70 | Part 1.1 General | inert | reason 1: not operative; a heading |  |
| 72 | s 1 Name of Act | inert | reason 1: not operative; a heading |  |
| 73 | s 1 text [opening words] | inert | reason 2: machinery; the short title of the Act |  |
| 75 | s 2 Dictionary | inert | reason 1: not operative; a heading |  |
| 76 | s 2 text [opening words] | encoded | `act-ch1-preliminary.l4`: s 2: whether the material is part of this Act, so far as s 2 says | `act-tests-ch1.l4` |
| 77 | s 2 Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 78 | s 2 Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 79 | s 2 Note 3 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 81 | s 2A Notes | inert | reason 1: not operative; a heading |  |
| 82 | s 2A text [opening words] | encoded | `act-ch1-preliminary.l4`: s 2A: whether the material is part of this Act, so far as s 2A says | `act-tests-ch1.l4` |
| 83 | s 2A Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 85 | s 3 Objects | inert | reason 1: not operative; a heading |  |
| 86 | s 3 (1) [subsection] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 87 | s 3 (2) [subsection] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 88 | s 3 (2) (a) [paragraph] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 89 | s 3 (2) (b) [paragraph] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 90-94 | s 3 (2) (c) [paragraph] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 95 | s 3 (3) [subsection] | inert | reason 1: not operative; objects clause: states the main object of the Act and creates no rule |  |
| 97 | s 4 Application of Act | inert | reason 1: not operative; a heading |  |
| 98 | s 4 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 4 (1): this Act applies to the thing | `act-tests-ch1.l4` |
| 99 | s 4 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 4 (2): the thing is taken to be made on the basis that it will operate in conjunction with this Act | `act-tests-ch1.l4` |
| 100-104 | s 4 (2) Examples [example] | encoded | as a case in `act-tests-ch1.l4` | `act-tests-ch1.l4` |
| 105 | s 4 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 106 | s 4 (3) [subsection] | encoded | `act-determinative.l4`: s 4 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 107 | s 4 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 109 | s 5 Determinative and non-determinative provisions | inert | reason 1: not operative; a heading |  |
| 110 | s 5 (1) [subsection] | encoded | `act-determinative.l4`: s 5 (2), (3): the determinative status of a section of this Act | `act-tests-determinative.l4` |
| 111 | s 5 (2) [subsection] | encoded | `act-determinative.l4`: s 5 (2), (3): the determinative status of a section of this Act | `act-tests-determinative.l4` |
| 112-113 | s 5 (2) Example [example] | encoded | as a case in `act-tests-determinative.l4` | `act-tests-determinative.l4` |
| 114 | s 5 (3) [subsection] | encoded | `act-determinative.l4`: s 5 (2), (3): the determinative status of a section of this Act | `act-tests-determinative.l4` |
| 115-116 | s 5 (3) Example [example] | encoded | as a case in `act-tests-determinative.l4` | `act-tests-determinative.l4` |
| 118 | s 6 Legislation Act provisions must be applied | inert | reason 1: not operative; a heading |  |
| 119 | s 6 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision; `act-ch1-preliminary.l4`: s 6 (1): the provision of this Act must be applied to the Act or statutory instrument | `act-tests-ch1.l4` |
| 120 | s 6 (2) [subsection] | fork | F1 (see the fork register); `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision | `act-tests-ch1.l4` |
| 121 | s 6 (3) [subsection] | fork | F1 (see the fork register); `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision | `act-tests-ch1.l4` |
| 122 | s 6 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 123 | s 6 (4) [subsection] | encoded | `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision; `act-ch1-preliminary.l4`: s 6 (4): how deliberate a displacement of the provision must be | `act-tests-ch1.l4` |
| 124 | s 6 (5) [subsection] | encoded | `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision; `act-ch1-preliminary.l4`: s 6 (5): this section applies despite any presumption or rule of interpretation | `act-tests-ch1.l4` |
| 125 | s 6 (6) [subsection] | encoded | `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision | `act-tests-ch1.l4` |
| 126 | s 6 (7) [subsection] | encoded | `act-ch1-preliminary.l4`: s 6: the provision of this Act is displaced by the other provision | `act-tests-ch1.l4` |
| 127 | s 6 (8) [subsection] | encoded | `act-determinative.l4`: s 6 (8): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 128-138 | s 6 (8) Examples—different [example] | encoded | as a case in `act-tests-ch1.l4` | `act-tests-ch1.l4` |
| 139-149 | s 6 (8) Example—concurrent [example] | encoded | as a case in `act-tests-ch1.l4` | `act-tests-ch1.l4` |
| 151 | Part 1.2 Basic concepts | inert | reason 1: not operative; a heading |  |
| 153 | s 7 Meaning of Act generally | inert | reason 1: not operative; a heading |  |
| 154 | s 7 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 7 (1), (2): the document is an Act | `act-tests-ch1.l4` |
| 155 | s 7 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 7 (1), (2): the document is an Act | `act-tests-ch1.l4` |
| 156 | s 7 (3) [subsection] | encoded | `act-ch1-preliminary.l4`: s 7 (3): a reference to an Act includes a reference to a provision of it | `act-tests-ch1.l4` |
| 157 | s 7 (3) Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 158 | s 7 (3) Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 160 | s 8 Meaning of subordinate law | inert | reason 1: not operative; a heading |  |
| 161 | s 8 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 8 (1): the document is a subordinate law | `act-tests-ch1.l4` |
| 162 | s 8 (1) (a) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 8 (1): the document is a subordinate law | `act-tests-ch1.l4` |
| 163 | s 8 (1) (b) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 8 (1): the document is a subordinate law | `act-tests-ch1.l4` |
| 164 | s 8 (1) (c) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 8 (1): the document is a subordinate law | `act-tests-ch1.l4` |
| 165 | s 8 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 8 (2): a reference to a subordinate law includes a reference to a provision of it | `act-tests-ch1.l4` |
| 167 | s 9 Meaning of disallowable instrument | inert | reason 1: not operative; a heading |  |
| 168 | s 9 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 9 (1): the document is a disallowable instrument | `act-tests-ch1.l4` |
| 169 | s 9 (1) (a) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 9 (1): the document is a disallowable instrument | `act-tests-ch1.l4` |
| 170 | s 9 (1) (b) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 9 (1): the document is a disallowable instrument | `act-tests-ch1.l4` |
| 171 | s 9 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 172 | s 9 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 9 (2): a reference to a disallowable instrument includes a reference to a provision of it | `act-tests-ch1.l4` |
| 174 | s 10 Meaning of notifiable instrument | inert | reason 1: not operative; a heading |  |
| 175 | s 10 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 10 (1): the document is a notifiable instrument | `act-tests-ch1.l4` |
| 176 | s 10 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 10 (2): a reference to a notifiable instrument includes a reference to a provision of it | `act-tests-ch1.l4` |
| 178 | s 11 Meaning of commencement notice | inert | reason 1: not operative; a heading |  |
| 179 | s 11 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 11 (1): the document is a commencement notice | `act-tests-ch1.l4` |
| 180 | s 11 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 11 (2): a reference to a commencement notice includes a reference to a provision of it | `act-tests-ch1.l4` |
| 182 | s 12 Meaning of legislative instrument | inert | reason 1: not operative; a heading |  |
| 183 | s 12 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 12 (1): the kind of document is a legislative instrument | `act-tests-ch1.l4` |
| 184 | s 12 (1) (a) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 12 (1): the kind of document is a legislative instrument | `act-tests-ch1.l4` |
| 185 | s 12 (1) (b) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 12 (1): the kind of document is a legislative instrument | `act-tests-ch1.l4` |
| 186 | s 12 (1) (c) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 12 (1): the kind of document is a legislative instrument | `act-tests-ch1.l4` |
| 187 | s 12 (1) (d) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 12 (1): the kind of document is a legislative instrument | `act-tests-ch1.l4` |
| 188 | s 12 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 12 (2): a reference to a legislative instrument includes a reference to a provision of it | `act-tests-ch1.l4` |
| 190 | s 13 Meaning of statutory instrument | inert | reason 1: not operative; a heading |  |
| 191 | s 13 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 13 (1): the document is a statutory instrument | `act-tests-ch1.l4` |
| 192 | s 13 (1) (a) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 13 (1): the document is a statutory instrument | `act-tests-ch1.l4` |
| 193 | s 13 (1) (b) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 13 (1): the document is a statutory instrument | `act-tests-ch1.l4` |
| 194 | s 13 (1) (c) [paragraph] | encoded | `act-ch1-preliminary.l4`: s 13 (1): the document is a statutory instrument | `act-tests-ch1.l4` |
| 195 | s 13 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 13 (2): the kind of document is included in the statutory instruments; `act-nouns.l4`: Kind of Act or instrument | `act-tests-ch1.l4` |
| 196 | s 13 (3) [subsection] | encoded | `act-ch1-preliminary.l4`: s 13 (3): a reference to a statutory instrument includes a reference to a provision of it | `act-tests-ch1.l4` |
| 198 | s 14 Meaning of instrument | inert | reason 1: not operative; a heading |  |
| 199 | s 14 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 14 (1): the document is an instrument | `act-tests-ch1.l4` |
| 200 | s 14 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 201 | s 14 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 14 (2): a reference to an instrument includes a reference to a provision of it | `act-tests-ch1.l4` |
| 203 | s 15 Meaning of authorised republication | inert | reason 1: not operative; a heading |  |
| 204 | s 15 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 15 (1): the republication is an authorised republication | `act-tests-ch1.l4` |
| 205 | s 15 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 15 (2): a reference to an authorised republication includes a reference to a provision of it | `act-tests-ch1.l4` |
| 206 | s 15 (3) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 207 | s 15 (3) law [definition] | encoded | `act-section-definitions.l4`: s 15 (3), definition of law | `act-tests-section-definitions.l4` |
| 209 | s 16 Meaning of provision | inert | reason 1: not operative; a heading |  |
| 210 | s 16 text [opening words] | encoded | `act-ch1-preliminary.l4`: s 16: the words or other thing are a provision of the Act or instrument | `act-tests-ch1.l4` |
| 211-212 | s 16 Examples—provisions [example] | encoded | as a case in `act-tests-ch1.l4` | `act-tests-ch1.l4` |
| 213-214 | s 16 Examples—provisions [example] | encoded | as a case in `act-tests-ch1.l4` | `act-tests-ch1.l4` |
| 215 | s 16 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 217 | Part 1.3 Sources of law in the ACT | inert | reason 1: not operative; a heading |  |
| 218-223 | note at line 218 | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 225 | s 17 References to Acts include references to former Cwlth enactments etc | inert | reason 1: not operative; a heading |  |
| 226 | s 17 (1) [subsection] | encoded | `act-ch1-preliminary.l4`: s 17 (1), (2): a reference to an Act includes a reference to the enactment | `act-tests-ch1.l4` |
| 227 | s 17 (2) [subsection] | encoded | `act-ch1-preliminary.l4`: s 17 (1), (2): a reference to an Act includes a reference to the enactment | `act-tests-ch1.l4` |
| 228 | s 17 (3) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 229-231 | s 17 (3) former Commonwealth enactment [definition] | encoded | `act-ch1-preliminary.l4`: s 17 (3): the enactment is a former Commonwealth enactment; `act-section-definitions.l4`: s 17 (3), definition of former Commonwealth enactment | `act-tests-ch1.l4`, `act-tests-section-definitions.l4` |
| 233-302 | Chapter 2 ACT legislation register and website | out of scope | assumed scope choice, not a ruling; The register and website kept by the Parliamentary Counsel |  |
| 303-373 | Chapter 3 Authorised versions and evidence of laws and legislative material | out of scope | assumed scope choice, not a ruling; Which versions are authorised, and proof of laws in court |  |
| 374-414 | Chapter 4 Numbering and notification of Acts | out of scope | assumed scope choice, not a ruling; How Acts are numbered and notified |  |
| 415-503 | Chapter 5 Regulatory impact statements (Parts 5.1, 5.2, 5.3) | out of scope | assumed scope choice, not a ruling; The statements required before certain subordinate laws and instruments are made |  |
| 504-842 | Chapter 6 Making, notification and numbering of statutory instruments (Parts 6.1 to 6.4) | out of scope | assumed scope choice, not a ruling; How statutory instruments are made, notified and numbered |  |
| 843-979 | Chapter 7 Presentation, amendment and disallowance of subordinate laws and disallowable instruments | out of scope | assumed scope choice, not a ruling; How subordinate laws are presented to the Assembly, amended and disallowed |  |
| 980 | Chapter 8 Commencement and exercise of powers before commencement | inert | reason 1: not operative; a heading |  |
| 982 | s 72 Meaning of law—ch 8 | inert | reason 1: not operative; a heading |  |
| 983 | s 72 text [opening words] | encoded | `act-ch8-commencement.l4`: s 72: the kind of document is a law for chapter 8 | `act-tests-ch8.l4` |
| 984 | s 72 law [definition] | encoded | `act-ch8-commencement.l4`: s 72: the kind of document is a law for chapter 8; `act-section-definitions.l4`: s 72, definition of law | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 985 | s 72 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 987 | s 73 General rules about commencement | inert | reason 1: not operative; a heading |  |
| 988 | s 73 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 73 (1) and s 74 (1): when an Act commences | `act-tests-time.l4` |
| 989 | s 73 (1) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (1) and s 74 (1): when an Act commences | `act-tests-time.l4` |
| 990 | s 73 (1) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (1) and s 74 (1): when an Act commences | `act-tests-time.l4` |
| 991 | s 73 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided; `act-interpretation-time.l4`: s 73 (2) and (3): when a legislative instrument commences | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 992 | s 73 (2) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided; `act-interpretation-time.l4`: s 73 (2) and (3): when a legislative instrument commences | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 993 | s 73 (2) (b) [paragraph] | fork | F2 (see the fork register); `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided; `act-interpretation-time.l4`: s 73 (2) and (3): when a legislative instrument commences | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 994 | s 73 (2) (c) [paragraph] | fork | F2 (see the fork register); `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided; `act-interpretation-time.l4`: s 73 (2) and (3): when a legislative instrument commences | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 995 | s 73 (2) (d) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided; `act-interpretation-time.l4`: s 73 (2) and (3): when a legislative instrument commences | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 996 | s 73 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 997 | s 73 (3) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 998 | s 73 (3) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 999 | s 73 (4) [subsection] | encoded | `act-interpretation-time.l4`: s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved; `act-interpretation-time.l4`: s 73 (4): when a statutory instrument that is not a legislative instrument commences | `act-tests-time.l4` |
| 1000 | s 73 (4) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved; `act-interpretation-time.l4`: s 73 (4): when a statutory instrument that is not a legislative instrument commences | `act-tests-time.l4` |
| 1001 | s 73 (4) (b) [paragraph] | fork | F2 (see the fork register); `act-interpretation-time.l4`: s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved; `act-interpretation-time.l4`: s 73 (4): when a statutory instrument that is not a legislative instrument commences | `act-tests-time.l4` |
| 1002 | s 73 (4) (c) [paragraph] | fork | F2 (see the fork register); `act-interpretation-time.l4`: s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved; `act-interpretation-time.l4`: s 73 (4): when a statutory instrument that is not a legislative instrument commences | `act-tests-time.l4` |
| 1003 | s 73 (4) (d) [paragraph] | encoded | `act-interpretation-time.l4`: s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved; `act-interpretation-time.l4`: s 73 (4): when a statutory instrument that is not a legislative instrument commences | `act-tests-time.l4` |
| 1004 | s 73 (5) [subsection] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1005 | s 73 (5) (a) [paragraph] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1006 | s 73 (5) (b) [paragraph] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1007 | s 73 (5) (c) [paragraph] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1008 | s 73 (5) (d) [paragraph] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1009 | s 73 (5) (e) [paragraph] | encoded | `act-ch8-commencement.l4`: s 73 (5): the sections that s 73 is subject to | `act-tests-ch8.l4` |
| 1010 | s 73 (6) [subsection] | encoded | `act-determinative.l4`: s 73 (6): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1011 | s 73 (6) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1013 | s 74 Time of commencement | inert | reason 1: not operative; a heading |  |
| 1014 | s 74 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 74 and dictionary, midnight: the number of minutes from the start of the day to a time of day; `act-interpretation-time.l4`: s 74: a single number that orders points in time; `act-interpretation-time.l4`: s 74: the first point is earlier than the second; and 4 more | `act-tests-time.l4`, `act-tests-ch8.l4` |
| 1015 | s 74 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 74 and dictionary, midnight: the number of minutes from the start of the day to a time of day; `act-interpretation-time.l4`: s 74: a single number that orders points in time; `act-interpretation-time.l4`: s 74: the first point is earlier than the second; and 3 more | `act-tests-time.l4`, `act-tests-ch8.l4` |
| 1017 | s 75 Commencement of naming and commencement provisions | inert | reason 1: not operative; a heading |  |
| 1018 | s 75 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 75 (1), (2): when the provisions providing for a law's name and commencement commence | `act-tests-time.l4` |
| 1019 | s 75 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 75 (1), (2): when the provisions providing for a law's name and commencement commence | `act-tests-time.l4` |
| 1020 | s 75 (2) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 75 (1), (2): when the provisions providing for a law's name and commencement commence | `act-tests-time.l4` |
| 1021 | s 75 (2) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 75 (1), (2): when the provisions providing for a law's name and commencement commence | `act-tests-time.l4` |
| 1022 | s 75 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 75 (3): the notification day of a statutory instrument that is not a legislative instrument | `act-tests-time.l4` |
| 1023 | s 75 (4) [subsection] | encoded | `act-determinative.l4`: s 75 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1024 | s 75 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1026 | s 75AA Commencement of provisions identifying amended laws | inert | reason 1: not operative; a heading |  |
| 1027 | s 75AA (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 75AA (1): s 75AA applies to the law | `act-tests-ch8.l4` |
| 1028 | s 75AA (2) [subsection] | encoded | `act-interpretation-time.l4`: s 75AA (2): when a provision identifying the amended law commences | `act-tests-time.l4` |
| 1029 | s 75AA (2) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 75AA (2): when a provision identifying the amended law commences | `act-tests-time.l4` |
| 1030 | s 75AA (2) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 75AA (2): when a provision identifying the amended law commences | `act-tests-time.l4` |
| 1031 | s 75AA (3) [subsection] | encoded | `act-determinative.l4`: s 75AA (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1032 | s 75AA (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1034 | s 75A Meaning of commences retrospectively | inert | reason 1: not operative; a heading |  |
| 1035 | s 75A (1) [subsection] | encoded | `act-interpretation-time.l4`: s 75A (1): an Act or legislative instrument commences retrospectively | `act-tests-ch8.l4`, `act-tests-time.l4` |
| 1036 | s 75A (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1037 | s 75A (2) [subsection] | encoded | `act-interpretation-time.l4`: s 75A (2): a statutory instrument that is not a legislative instrument commences retrospectively | `act-tests-time.l4` |
| 1039 | s 75B Retrospective commencement requires clear indication | inert | reason 1: not operative; a heading |  |
| 1040 | s 75B (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 75B (1): the law is taken to provide for the law (or another law) to commence retrospectively | `act-tests-ch8.l4` |
| 1041-1045 | s 75B (1) Example [example] | encoded | as a case in `act-tests-ch8.l4` | `act-tests-ch8.l4` |
| 1046 | s 75B (2) [subsection] | encoded | `act-determinative.l4`: s 75B (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1047 | s 75B (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1049 | s 76 Non–prejudicial provision may commence retrospectively | inert | reason 1: not operative; a heading |  |
| 1050 | s 76 (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 76 (1): a statutory instrument may provide that the provision commences retrospectively | `act-tests-ch8.l4` |
| 1051 | s 76 (2) [subsection] | encoded | `act-ch8-commencement.l4`: s 76 (2): a statutory instrument can provide that the prejudicial provision commences retrospectively | `act-tests-ch8.l4` |
| 1052-1054 | s 76 (2) Example [example] | encoded | as a case in `act-tests-ch8.l4` | `act-tests-ch8.l4` |
| 1055 | s 76 (3) [subsection] | encoded | `act-determinative.l4`: s 76 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1056 | s 76 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1057 | s 76 (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1058 | s 76 (4) non-prejudicial provision [definition] | encoded | `act-ch8-commencement.l4`: s 76 (4): the provision is a non-prejudicial provision; `act-section-definitions.l4`: s 76 (4), definition of non-prejudicial provision | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 1059-1061 | s 76 (4) prejudicial provision [definition] | encoded | `act-ch8-commencement.l4`: s 76 (4): the provision is a prejudicial provision; `act-section-definitions.l4`: s 76 (4), definition of prejudicial provision | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 1063 | s 77 Commencement by commencement notice | inert | reason 1: not operative; a heading |  |
| 1064 | s 77 (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 77 (1) (a): a single day, or a time on a single day, may be fixed or determined | `act-tests-ch8.l4` |
| 1065 | s 77 (1) (a) [paragraph] | encoded | `act-ch8-commencement.l4`: s 77 (1) (a): a single day, or a time on a single day, may be fixed or determined | `act-tests-ch8.l4` |
| 1066 | s 77 (1) (b) [paragraph] | encoded | `act-ch8-commencement.l4`: s 77 (1) (b): different days or times may be fixed or determined for different provisions | `act-tests-ch8.l4` |
| 1067 | s 77 (2) [subsection] | encoded | `act-ch8-commencement.l4`: s 77 (2): the commencement notice for the law is valid | `act-tests-ch8.l4` |
| 1068 | s 77 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 77 (3), (4): when a law commences under a commencement notice | `act-tests-time.l4` |
| 1069 | s 77 (4) [subsection] | fork | F3 (see the fork register); `act-interpretation-time.l4`: s 77 (3), (4): when a law commences under a commencement notice | `act-tests-time.l4` |
| 1070 | s 77 (4) (a) [paragraph] | fork | F3 (see the fork register); `act-interpretation-time.l4`: s 77 (3), (4): when a law commences under a commencement notice | `act-tests-time.l4` |
| 1071 | s 77 (4) (b) [paragraph] | fork | F3 (see the fork register); `act-interpretation-time.l4`: s 77 (3), (4): when a law commences under a commencement notice | `act-tests-time.l4` |
| 1072 | s 77 (5) [subsection] | encoded | `act-determinative.l4`: s 77 (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1073 | s 77 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1075 | s 78 Separate commencement of amendments | inert | reason 1: not operative; a heading |  |
| 1076 | s 78 (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 78 (1): the amendments may be given separate commencements | `act-tests-ch8.l4` |
| 1077-1079 | s 78 (1) Examples [example] | encoded | as a case in `act-tests-ch8.l4` | `act-tests-ch8.l4` |
| 1080 | s 78 (2) [subsection] | encoded | `act-determinative.l4`: s 78 (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1081 | s 78 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1083 | s 79 Automatic commencement of postponed law | inert | reason 1: not operative; a heading |  |
| 1084 | s 79 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 79 (1): when a postponed law automatically commences | `act-tests-time.l4` |
| 1085 | s 79 (2) [subsection] | encoded | `act-ch8-commencement.l4`: s 79 (2): s 79 applies to the law | `act-tests-ch8.l4` |
| 1086 | s 79 (3) [subsection] | encoded | `act-determinative.l4`: s 79 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1087 | s 79 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1088 | s 79 (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1089 | s 79 (4) enact [definition] | encoded | `act-section-definitions.l4`: s 79 (4), definition of enact | `act-tests-section-definitions.l4` |
| 1090 | s 79 (4) law [definition] | encoded | `act-ch8-commencement.l4`: s 79 (4): the kind of document is a law for s 79; `act-section-definitions.l4`: s 79 (4), definition of law | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 1091 | s 79 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1092-1094 | s 79 (4) notification day, for a postponed law [definition] | encoded | `act-ch8-commencement.l4`: s 79 (4): the notification day of the postponed law; `act-section-definitions.l4`: s 79 (4), definition of notification day, for a postponed law | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 1095 | s 79 (4) postponed law [definition] | encoded | `act-ch8-commencement.l4`: s 79 (4): the law is a postponed law; `act-section-definitions.l4`: s 79 (4), definition of postponed law | `act-tests-ch8.l4`, `act-tests-section-definitions.l4` |
| 1097 | s 79A Commencement of amendment of uncommenced law | inert | reason 1: not operative; a heading |  |
| 1098 | s 79A (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 79A (1): s 79A applies to the amending law | `act-tests-ch8.l4` |
| 1099 | s 79A (2) [subsection] | encoded | `act-ch8-commencement.l4`: s 79A (2): the amendment of the uncommenced law of itself commences that law | `act-tests-ch8.l4` |
| 1100 | s 79A (3) [subsection] | encoded | `act-ch8-commencement.l4`: s 79A (3): when the amendment made by the amending law commences | `act-tests-ch8.l4` |
| 1101 | s 79A (4) [subsection] | encoded | `act-determinative.l4`: s 79A (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1102 | s 79A (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1104 | s 80 References to commencement of law | inert | reason 1: not operative; a heading |  |
| 1105 | s 80 text [opening words] | encoded | `act-ch8-commencement.l4`: s 80: what a reference to the commencement of the law concerned is a reference to | `act-tests-ch8.l4` |
| 1106 | s 80 (a) [paragraph] | encoded | `act-ch8-commencement.l4`: s 80: what a reference to the commencement of the law concerned is a reference to | `act-tests-ch8.l4` |
| 1107 | s 80 (b) [paragraph] | encoded | `act-ch8-commencement.l4`: s 80: what a reference to the commencement of the law concerned is a reference to | `act-tests-ch8.l4` |
| 1108 | s 80 (c) [paragraph] | encoded | `act-ch8-commencement.l4`: s 80: what a reference to the commencement of the law concerned is a reference to | `act-tests-ch8.l4` |
| 1110 | s 81 Exercise of powers between notification and commencement | inert | reason 1: not operative; a heading |  |
| 1111 | s 81 (1) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (1): s 81 applies to the power | `act-tests-ch8.l4` |
| 1112 | s 81 (1) (a) [paragraph] | encoded | `act-ch8-commencement.l4`: s 81 (1): s 81 applies to the power | `act-tests-ch8.l4` |
| 1113 | s 81 (1) (b) [paragraph] | encoded | `act-ch8-commencement.l4`: s 81 (1): s 81 applies to the power | `act-tests-ch8.l4` |
| 1114-1118 | s 81 (1) Examples—powers [example] | encoded | as a case in `act-tests-ch8.l4` | `act-tests-ch8.l4` |
| 1119 | s 81 (2) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (2): s 81 applies to the power to make an appointment, make a statutory instrument or do anything else in relation to the entity | `act-tests-ch8.l4` |
| 1120 | s 81 (2) (a) [paragraph] | encoded | `act-ch8-commencement.l4`: s 81 (2): s 81 applies to the power to make an appointment, make a statutory instrument or do anything else in relation to the entity | `act-tests-ch8.l4` |
| 1121 | s 81 (2) (b) [paragraph] | encoded | `act-ch8-commencement.l4`: s 81 (2): s 81 applies to the power to make an appointment, make a statutory instrument or do anything else in relation to the entity | `act-tests-ch8.l4` |
| 1122 | s 81 (2) (c) [paragraph] | encoded | `act-ch8-commencement.l4`: s 81 (2): s 81 applies to the power to make an appointment, make a statutory instrument or do anything else in relation to the entity | `act-tests-ch8.l4` |
| 1123-1124 | s 81 (2) Example [example] | encoded | as a case in `act-tests-ch8.l4` | `act-tests-ch8.l4` |
| 1125 | s 81 (3) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (3): the power may be exercised at any time even though the authorising law is not in force | `act-tests-ch8.l4` |
| 1126 | s 81 (4) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (4): the authorising law is taken to be in force at the time of the exercise of the power | `act-tests-ch8.l4` |
| 1127 | s 81 (5) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (5): anything else may be done under the power at any time for the purpose of bringing the authorising law into operation | `act-tests-ch8.l4` |
| 1128 | s 81 (6) [subsection] | encoded | `act-interpretation-time.l4`: s 81 (6): when an appointment or instrument that declares subsection (6) applies commences | `act-tests-time.l4` |
| 1129 | s 81 (6) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 81 (6): when an appointment or instrument that declares subsection (6) applies commences | `act-tests-time.l4` |
| 1130 | s 81 (6) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 81 (6): when an appointment or instrument that declares subsection (6) applies commences | `act-tests-time.l4` |
| 1131 | s 81 (7) [subsection] | encoded | `act-interpretation-time.l4`: s 81 (7): when an appointment or instrument made under s 81 commences | `act-tests-time.l4` |
| 1132 | s 81 (7) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 81 (7): when an appointment or instrument made under s 81 commences | `act-tests-time.l4` |
| 1133 | s 81 (7) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 81 (7): when an appointment or instrument made under s 81 commences | `act-tests-time.l4` |
| 1134 | s 81 (8) [subsection] | encoded | `act-ch8-commencement.l4`: s 81 (8): the day a statutory instrument that is not a legislative instrument is taken to be notified | `act-tests-ch8.l4` |
| 1135 | s 81 (9) [subsection] | encoded | `act-determinative.l4`: s 81 (9): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1136 | s 81 (9) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1138 | Chapter 9 Repeal and amendment of laws | inert | reason 1: not operative; a heading |  |
| 1140 | Part 9.1 General | inert | reason 1: not operative; a heading |  |
| 1142 | s 82 Definitions—ch 9 | inert | reason 1: not operative; a heading |  |
| 1143 | s 82 text [opening words] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1144 | s 82 amend [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 82: the change is an amendment for chapter 9; `act-section-definitions.l4`: s 82, definition of amend | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1145 | s 82 law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 82: the kind of document is a law for chapter 9; `act-section-definitions.l4`: s 82, definition of law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1146 | s 82 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1147 | s 82 repeal [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 82: the change is a repeal for chapter 9; `act-section-definitions.l4`: s 82, definition of repeal | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1149 | s 83 Consequences of amendment of statutory instrument by Act | inert | reason 1: not operative; a heading |  |
| 1150 | s 83 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 83 (1): the instrument may be amended or repealed as if the amendment had been made by another statutory instrument of that kind | `act-tests-ch9.l4` |
| 1151 | s 83 (2) [subsection] | encoded | `act-determinative.l4`: s 83 (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1152 | s 83 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1154 | s 84 Saving of operation of repealed and amended laws | inert | reason 1: not operative; a heading |  |
| 1155 | s 84 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1156 | s 84 (1) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1157 | s 84 (1) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1158 | s 84 (1) (c) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1159 | s 84 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing; `act-ch9-repeal-and-amendment.l4`: s 84 (2): the investigation, proceeding or remedy may be started, exercised, continued or completed as if the repeal or amendment had not happened | `act-tests-ch9.l4` |
| 1160 | s 84 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1161 | s 84 (3) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1162 | s 84 (3) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (1), (3): the repeal or amendment of a law affects the thing | `act-tests-ch9.l4` |
| 1163 | s 84 (4) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84 (4): s 84 limits any other provision of this chapter | `act-tests-ch9.l4` |
| 1164 | s 84 (5) [subsection] | encoded | `act-determinative.l4`: s 84 (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1165 | s 84 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1166 | s 84 (6) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1167 | s 84 (6) liability [definition] | encoded | `act-section-definitions.l4`: s 84 (6), definition of liability | `act-tests-section-definitions.l4` |
| 1168 | s 84 (6) penalty [definition] | encoded | `act-section-definitions.l4`: s 84 (6), definition of penalty | `act-tests-section-definitions.l4` |
| 1169 | s 84 (6) privilege [definition] | encoded | `act-section-definitions.l4`: s 84 (6), definition of privilege | `act-tests-section-definitions.l4` |
| 1170 | s 84 (6) right [definition] | encoded | `act-section-definitions.l4`: s 84 (6), definition of right | `act-tests-section-definitions.l4` |
| 1172 | s 84A Creation of offences and changes in penalties | inert | reason 1: not operative; a heading |  |
| 1173 | s 84A (1) [subsection] | fork | F16 (see the fork register); `act-ch9-repeal-and-amendment.l4`: s 84A (1): the act or omission is an offence | `act-tests-ch9.l4` |
| 1174 | s 84A (2) [subsection] | fork | F16 (see the fork register); `act-ch9-repeal-and-amendment.l4`: s 84A (2): the increase in the penalty applies to the offence | `act-tests-ch9.l4` |
| 1175 | s 84A (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84A (3): the reduction in the penalty applies to the offence | `act-tests-ch9.l4` |
| 1176 | s 84A (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1177 | s 84A (4) law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 84A (4): the kind of document is a law for s 84A; `act-section-definitions.l4`: s 84A (4), definition of law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1178 | s 84A (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1179 | s 84A (5) [subsection] | encoded | `act-determinative.l4`: s 84A (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1180 | s 84A (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1182 | Part 9.2 Repeal | inert | reason 1: not operative; a heading |  |
| 1184 | s 85 When repeal takes effect | inert | reason 1: not operative; a heading |  |
| 1185 | s 85 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 85: when the repeal of a law takes effect | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1186 | s 85 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 85: when the repeal of a law takes effect | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1187 | s 85 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1188 | s 85 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 85: when the repeal of a law takes effect | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1190 | s 86 Repealed and amended laws not revived on repeal of repealing and amending laws | inert | reason 1: not operative; a heading |  |
| 1191 | s 86 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 86 (1): the first law is revived | `act-tests-ch9.l4` |
| 1192 | s 86 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 86 (2): the continuing operation of the amendments made by the other law is affected | `act-tests-ch9.l4` |
| 1193 | s 86 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 86 (3): s 86 limits any other provision of this chapter | `act-tests-ch9.l4` |
| 1194 | s 86 (4) [subsection] | encoded | `act-determinative.l4`: s 86 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1195 | s 86 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1196 | s 86 (5) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1197 | s 86 (5) amended does not include modified. [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 86 (5): the change is an amendment for s 86; `act-section-definitions.l4`: s 86 (5), definition of amended does not include modified. | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1198 | s 86 (5) law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 86 (5): the thing is a law for s 86; `act-section-definitions.l4`: s 86 (5), definition of law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1199-1202 | s 86 (5) Examples [example] | encoded | as a case in `act-tests-ch9.l4` | `act-tests-ch9.l4` |
| 1204 | s 87 Commencement not undone if repealed | inert | reason 1: not operative; a heading |  |
| 1205 | s 87 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 87 (1): the repeal of the provision providing for the commencement of the law affects the continuing operation of the law | `act-tests-ch9.l4` |
| 1206 | s 87 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 87 (2): the repeal of the commencement notice affects the continuing operation of the law | `act-tests-ch9.l4` |
| 1207 | s 87 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 87 (3): s 87 limits any other provision of this chapter | `act-tests-ch9.l4` |
| 1208 | s 87 (4) [subsection] | encoded | `act-determinative.l4`: s 87 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1209 | s 87 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1211 | s 88 Repeal does not end effect of transitional laws etc | inert | reason 1: not operative; a heading |  |
| 1212 | s 88 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (1), (2): the continuing operation of the law is affected | `act-tests-ch9.l4` |
| 1213 | s 88 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (1), (2): the continuing operation of the law is affected | `act-tests-ch9.l4` |
| 1214 | s 88 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (3): the effect of the declared law or the savings law ends | `act-tests-ch9.l4` |
| 1215 | s 88 (3) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (3): the effect of the declared law or the savings law ends | `act-tests-ch9.l4` |
| 1216 | s 88 (3) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (3): the effect of the declared law or the savings law ends | `act-tests-ch9.l4` |
| 1217 | s 88 (4) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (4): a declaration may be made for subsection (3) about the law | `act-tests-ch9.l4` |
| 1218 | s 88 (5) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (5): the declaration implies that, without a declaration about it, another law is not a law to which s 88 applies | `act-tests-ch9.l4` |
| 1219 | s 88 (6) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (6): s 88 limits any other provision of this chapter | `act-tests-ch9.l4` |
| 1220 | s 88 (7) [subsection] | encoded | `act-determinative.l4`: s 88 (7): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1221 | s 88 (7) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1222 | s 88 (8) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (8): the application of s 88 to the law is displaced | `act-tests-ch9.l4` |
| 1223 | s 88 (9) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1224-1226 | s 88 (9) transitional law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (9): the law is a transitional law; `act-section-definitions.l4`: s 88 (9), definition of transitional law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1227-1230 | s 88 (9) Examples [example] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (9): the law is a transitional law; `act-section-definitions.l4`: s 88 (9), definition of transitional law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1231 | s 88 (9) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1232-1234 | s 88 (9) validating law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (9): the law is a validating law; `act-section-definitions.l4`: s 88 (9), definition of validating law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1235-1237 | s 88 (9) Examples [example] | encoded | `act-ch9-repeal-and-amendment.l4`: s 88 (9): the law is a validating law; `act-section-definitions.l4`: s 88 (9), definition of validating law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1239 | s 89 Automatic repeal of certain laws and provisions | inert | reason 1: not operative; a heading |  |
| 1240 | s 89 (1) [subsection] | fork | F4 (see the fork register); `act-interpretation-time.l4`: s 89 (1): the day an amending law is automatically repealed | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1241 | s 89 (1) (a) [paragraph] | fork | F4 (see the fork register); `act-interpretation-time.l4`: s 89 (1): the day an amending law is automatically repealed | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1242 | s 89 (1) (b) [paragraph] | fork | F4 (see the fork register); `act-interpretation-time.l4`: s 89 (1): the day an amending law is automatically repealed | `act-tests-ch9.l4`, `act-tests-time.l4` |
| 1243-1244 | s 89 (1) Example—provision [example] | fork | F4 (see the fork register); as a case in `act-tests-ch9.l4` | `act-tests-ch9.l4` |
| 1245 | s 89 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (2): the day an appropriation Act is automatically repealed | `act-tests-time.l4` |
| 1246 | s 89 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (3), (4): the point in time immediately after which the provision is automatically repealed | `act-tests-time.l4` |
| 1247 | s 89 (4) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (3), (4): the point in time immediately after which the provision is automatically repealed | `act-tests-time.l4` |
| 1248 | s 89 (5) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (5), (6): the latest of some days; `act-interpretation-time.l4`: s 89 (5): the day a commencement notice is automatically repealed | `act-tests-time.l4` |
| 1249 | s 89 (6) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (5), (6): the latest of some days; `act-interpretation-time.l4`: s 89 (6): the day an instrument making or evidencing appointments is automatically repealed | `act-tests-time.l4` |
| 1250 | s 89 (6) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 89 (5), (6): the latest of some days; `act-interpretation-time.l4`: s 89 (6): the day an instrument making or evidencing appointments is automatically repealed | `act-tests-time.l4` |
| 1251 | s 89 (6) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 89 (5), (6): the latest of some days; `act-interpretation-time.l4`: s 89 (6): the day an instrument making or evidencing appointments is automatically repealed | `act-tests-time.l4` |
| 1252 | s 89 (7) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (7): a repeal under s 89 has effect for all purposes, including the provisions of this chapter about repeals | `act-tests-ch9.l4` |
| 1253 | s 89 (8) [subsection] | encoded | `act-interpretation-time.l4`: s 89 (8): the day a law is automatically repealed, if the day would be earlier than its notification day | `act-tests-time.l4` |
| 1254 | s 89 (9) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (9): the notification day of a statutory instrument that is not a legislative instrument, for s 89 (8) | `act-tests-ch9.l4` |
| 1255 | s 89 (10) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (10): s 89 limits any other provision of this chapter | `act-tests-ch9.l4` |
| 1256 | s 89 (11) [subsection] | encoded | `act-determinative.l4`: s 89 (11): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1257 | s 89 (11) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1258 | s 89 (12) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1259 | s 89 (12) amend does not include modify. [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (12): the change is an amendment for s 89; `act-section-definitions.l4`: s 89 (12), definition of amend does not include modify. | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1260-1266 | s 89 (12) amending law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (12): the law is an amending law; `act-section-definitions.l4`: s 89 (12), definition of amending law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1267-1271 | s 89 (12) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1272-1274 | s 89 (12) amending provision, of a law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (12): the provision is an amending provision; `act-section-definitions.l4`: s 89 (12), definition of amending provision, of a law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1275 | s 89 (12) appropriation Act [definition] | encoded | `act-section-definitions.l4`: s 89 (12), definition of appropriation Act | `act-tests-section-definitions.l4` |
| 1276 | s 89 (12) commencement provision, of a law [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 89 (12): the provision is a commencement provision; `act-section-definitions.l4`: s 89 (12), definition of commencement provision, of a law | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1278 | Part 9.3 Amendment | inert | reason 1: not operative; a heading |  |
| 1280 | s 90 Law and amending laws to be read as one | inert | reason 1: not operative; a heading |  |
| 1281 | s 90 text [opening words] | encoded | `act-ch9-repeal-and-amendment.l4`: s 90: the law and all laws amending it are to be read as one | `act-tests-ch9.l4` |
| 1283 | s 91 Insertion of provisions by amending law | inert | reason 1: not operative; a heading |  |
| 1284 | s 91 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1285 | s 91 (1) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1286 | s 91 (1) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1287 | s 91 (1) (c) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1288 | s 91 (1) (d) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1289 | s 91 (1) (e) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1290 | s 91 (1) (f) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (1): s 91 applies to the amendment | `act-tests-ch9.l4` |
| 1291 | s 91 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1292 | s 91 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1293 | s 91 (4) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1294 | s 91 (5) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1295 | s 91 (6) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1296 | s 91 (7) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (2) to (7): the position of the inserted provision in the amended law | `act-tests-ch9.l4` |
| 1297 | s 91 (8) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (8): a reference to a section or subsection is a reference to a corresponding provision of the law | `act-tests-ch9.l4` |
| 1298 | s 91 (9) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1299 | s 91 (9) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1300 | s 91 (9) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1301 | s 91 (9) (c) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1302 | s 91 (9) (d) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1303 | s 91 (9) (e) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (9): the matters to which regard may be had in working out the appropriate position | `act-tests-ch9.l4` |
| 1304 | s 91 (10) [subsection] | encoded | `act-determinative.l4`: s 91 (10): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1305 | s 91 (10) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1306 | s 91 (11) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1307 | s 91 (11) insert [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 91 (11): the thing is an insertion; `act-section-definitions.l4`: s 91 (11), definition of insert | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1309 | s 92 Amendment to be made wherever possible | inert | reason 1: not operative; a heading |  |
| 1310 | s 92 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 92 (1): the amendment is to be made wherever possible in the other law | `act-tests-ch9.l4` |
| 1311 | s 92 (1) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 92 (1): the amendment is to be made wherever possible in the other law | `act-tests-ch9.l4` |
| 1312 | s 92 (1) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 92 (1): the amendment is to be made wherever possible in the other law | `act-tests-ch9.l4` |
| 1313-1314 | s 92 (1) (c) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 92 (1): the amendment is to be made wherever possible in the other law | `act-tests-ch9.l4` |
| 1315 | s 92 (2) [subsection] | encoded | `act-determinative.l4`: s 92 (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1316 | s 92 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1318 | s 93 Provisions included in another provision for amendment purposes | inert | reason 1: not operative; a heading |  |
| 1319 | s 93 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1320 | s 93 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1321 | s 93 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1322 | s 93 (4) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1323 | s 93 (5) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law; `act-ch9-repeal-and-amendment.l4`: s 93 (5): a note in a law is, for any other purpose, part of the law | `act-tests-ch9.l4` |
| 1324 | s 93 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1325 | s 93 (6) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1326 | s 93 (6) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1327 | s 93 (6) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1328 | s 93 (7) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1329 | s 93 (8) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (2) to (8): what the material is part of, for the purpose of amending a law | `act-tests-ch9.l4` |
| 1330 | s 93 (9) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (9): the thing is disregarded in working out whether the material is at the end of the provision | `act-tests-ch9.l4` |
| 1331-1334 | s 93 (9) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1335 | s 93 (10) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 93 (10): a reference to a section or subsection is a reference to a corresponding provision of the law | `act-tests-ch9.l4` |
| 1336 | s 93 (11) [subsection] | encoded | `act-determinative.l4`: s 93 (11): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1337 | s 93 (11) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1339 | s 94 Continuance of appointments etc made under amended provisions | inert | reason 1: not operative; a heading |  |
| 1340 | s 94 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (1): s 94 applies to the appointment, instrument, delegation, licence, permit or other thing | `act-tests-ch9.l4` |
| 1341-1345 | s 94 (1) (a) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (1): s 94 applies to the appointment, instrument, delegation, licence, permit or other thing | `act-tests-ch9.l4` |
| 1346 | s 94 (1) (b) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (1): s 94 applies to the appointment, instrument, delegation, licence, permit or other thing | `act-tests-ch9.l4` |
| 1347-1352 | s 94 (1) (c) [paragraph] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (1): s 94 applies to the appointment, instrument, delegation, licence, permit or other thing | `act-tests-ch9.l4` |
| 1353-1355 | s 94 (1) Examples—par [example] | encoded | as a case in `act-tests-ch9.l4` | `act-tests-ch9.l4` |
| 1356 | s 94 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (2): the thing continues to have effect as if it had been made, issued or done under the amended law | `act-tests-ch9.l4` |
| 1357 | s 94 (3) [subsection] | encoded | `act-determinative.l4`: s 94 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1358 | s 94 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1359 | s 94 (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1360 | s 94 (4) amend [definition] | encoded | `act-ch9-repeal-and-amendment.l4`: s 94 (4): the change is an amendment for s 94; `act-section-definitions.l4`: s 94 (4), definition of amend | `act-tests-ch9.l4`, `act-tests-section-definitions.l4` |
| 1361 | s 94 (4) appointment [definition] | encoded | `act-section-definitions.l4`: s 94 (4), definition of appointment | `act-tests-section-definitions.l4` |
| 1363 | s 95 Status of modifications | inert | reason 1: not operative; a heading |  |
| 1364 | s 95 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 95 (1): the law operates as modified; `act-ch9-repeal-and-amendment.l4`: s 95 (1): the modification amends the text of the law | `act-tests-ch9.l4` |
| 1365 | s 95 (2) [subsection] | encoded | `act-determinative.l4`: s 95 (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1366 | s 95 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1368 | s 96 Relocated provisions | inert | reason 1: not operative; a heading |  |
| 1369 | s 96 (1) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 96 (1): s 96 applies to the provision | `act-tests-ch9.l4` |
| 1370 | s 96 (2) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 96 (2): the operation or meaning of the provision is affected | `act-tests-ch9.l4` |
| 1371 | s 96 (3) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 96 (3): the provision is to be interpreted in that way in its new location | `act-tests-ch9.l4` |
| 1372 | s 96 (4) [subsection] | encoded | `act-ch9-repeal-and-amendment.l4`: s 96 (4): the provision has effect subject to the changes | `act-tests-ch9.l4` |
| 1373 | s 96 (5) [subsection] | encoded | `act-determinative.l4`: s 96 (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1374 | s 96 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1376 | Chapter 10 Referring to laws | inert | reason 1: not operative; a heading |  |
| 1378 | s 97 Definitions—ch 10 | inert | reason 1: not operative; a heading |  |
| 1379 | s 97 (1) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1380 | s 97 (1) ACT law [definition] | encoded | `act-ch10-referring-to-laws.l4`: s 97 (1): the document is an ACT law; `act-section-definitions.l4`: s 97 (1), definition of ACT law | `act-tests-ch10.l4`, `act-tests-section-definitions.l4` |
| 1381 | s 97 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1382 | s 97 (1) law [definition] | encoded | `act-ch10-referring-to-laws.l4`: s 97 (1): the document is a law; `act-section-definitions.l4`: s 97 (1), definition of law | `act-tests-ch10.l4`, `act-tests-section-definitions.l4` |
| 1383 | s 97 (1) law of another jurisdiction [definition] | encoded | `act-ch10-referring-to-laws.l4`: s 97 (1): the document is a law of another jurisdiction; `act-section-definitions.l4`: s 97 (1), definition of law of another jurisdiction | `act-tests-ch10.l4`, `act-tests-section-definitions.l4` |
| 1384 | s 97 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1385 | s 97 (2) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1386 | s 97 (2) Act, in relation to another Territory [definition] | encoded | `act-ch10-referring-to-laws.l4`: s 97 (2): the document is an Act in relation to the other Territory; `act-section-definitions.l4`: s 97 (2), definition of Act, in relation to another Territory | `act-tests-ch10.l4`, `act-tests-section-definitions.l4` |
| 1387-1390 | s 97 (2) statutory instrument, of another jurisdiction [definition] | encoded | `act-ch10-referring-to-laws.l4`: s 97 (2): the instrument is a statutory instrument of another jurisdiction; `act-section-definitions.l4`: s 97 (2), definition of statutory instrument, of another jurisdiction | `act-tests-ch10.l4`, `act-tests-section-definitions.l4` |
| 1392 | s 98 References to ACT law include law containing reference | inert | reason 1: not operative; a heading |  |
| 1393 | s 98 text [opening words] | fork | F5 (see the fork register); `act-ch10-referring-to-laws.l4`: s 98: the reference includes a reference to the law itself | `act-tests-ch10.l4` |
| 1394-1395 | s 98 Example [example] | fork | F5 (see the fork register); as a case in `act-tests-ch10.l4` | `act-tests-ch10.l4` |
| 1397 | s 99 References in ACT statutory instruments to the Act | inert | reason 1: not operative; a heading |  |
| 1398 | s 99 text [opening words] | encoded | `act-ch10-referring-to-laws.l4`: s 99: the reference is a reference to the Act under which the instrument is made or in force | `act-tests-ch10.l4` |
| 1400 | s 100 Referring to particular ACT laws | inert | reason 1: not operative; a heading |  |
| 1401 | s 100 (1) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to an Act; `act-ch10-referring-to-laws.l4`: s 100 (1): an Act may be referred to in the way | `act-tests-ch10.l4` |
| 1402 | s 100 (1) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to an Act; `act-ch10-referring-to-laws.l4`: s 100 (1): an Act may be referred to in the way | `act-tests-ch10.l4` |
| 1403 | s 100 (1) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to an Act; `act-ch10-referring-to-laws.l4`: s 100 (1): an Act may be referred to in the way | `act-tests-ch10.l4` |
| 1404 | s 100 (2) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1405 | s 100 (2) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1406 | s 100 (2) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1407 | s 100 (2) (c) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1408 | s 100 (2) (d) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1409 | s 100 (2) (e) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a statutory instrument; `act-ch10-referring-to-laws.l4`: s 100 (2): a statutory instrument may be referred to in the way | `act-tests-ch10.l4` |
| 1411 | s 101 Referring to particular laws of other jurisdictions etc | inert | reason 1: not operative; a heading |  |
| 1412 | s 101 (1) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (1): a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1413 | s 101 (1) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (1): a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1414 | s 101 (1) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (1): a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1415-1416 | s 101 (1) (c) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (1): a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1417 | s 101 (2) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a provision of a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (2): a provision of a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1418 | s 101 (2) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a provision of a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (2): a provision of a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1419 | s 101 (2) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Way of referring to a provision of a law of another jurisdiction; `act-ch10-referring-to-laws.l4`: s 101 (2): a provision of a law of another jurisdiction may be referred to in the way | `act-tests-ch10.l4` |
| 1420 | s 101 (3) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 101 (3): subsection (2) limits any other provision of this chapter | `act-tests-ch10.l4` |
| 1422 | s 102 References to laws include references to laws as in force from time to time | inert | reason 1: not operative; a heading |  |
| 1423 | s 102 (1) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Version of a law that a reference to the law may include; `act-ch10-referring-to-laws.l4`: s 102 (1): a reference to a law includes a reference to the version | `act-tests-ch10.l4` |
| 1424 | s 102 (1) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Version of a law that a reference to the law may include; `act-ch10-referring-to-laws.l4`: s 102 (1): a reference to a law includes a reference to the version | `act-tests-ch10.l4` |
| 1425 | s 102 (1) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Version of a law that a reference to the law may include; `act-ch10-referring-to-laws.l4`: s 102 (1): a reference to a law includes a reference to the version | `act-tests-ch10.l4` |
| 1426 | s 102 (1) (c) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Version of a law that a reference to the law may include; `act-ch10-referring-to-laws.l4`: s 102 (1): a reference to a law includes a reference to the version | `act-tests-ch10.l4` |
| 1427 | s 102 (2) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: Version of a provision that a reference to the provision may include; `act-ch10-referring-to-laws.l4`: s 102 (2): a reference to a provision of a law includes a reference to the version | `act-tests-ch10.l4` |
| 1428 | s 102 (2) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Version of a provision that a reference to the provision may include; `act-ch10-referring-to-laws.l4`: s 102 (2): a reference to a provision of a law includes a reference to the version | `act-tests-ch10.l4` |
| 1429 | s 102 (2) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: Version of a provision that a reference to the provision may include; `act-ch10-referring-to-laws.l4`: s 102 (2): a reference to a provision of a law includes a reference to the version | `act-tests-ch10.l4` |
| 1430 | s 102 (3) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 102 (3): the reference includes a reference to the law by its name as amended | `act-tests-ch10.l4` |
| 1431 | s 102 (4) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 102 (4): the sections that s 102 is subject to | `act-tests-ch10.l4` |
| 1432 | s 102 (5) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1433 | s 102 (5) made [definition] | encoded | `act-section-definitions.l4`: s 102 (5), definition of made | `act-tests-section-definitions.l4` |
| 1435 | s 103 References to repealed laws | inert | reason 1: not operative; a heading |  |
| 1436 | s 103 text [opening words] | encoded | `act-ch10-referring-to-laws.l4`: s 103: the reference is a reference to the law as in force immediately before it was repealed | `act-tests-ch10.l4` |
| 1438 | s 104 References to laws include references to instruments under laws | inert | reason 1: not operative; a heading |  |
| 1439 | s 104 (1) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 104 (1): the reference includes a reference to the statutory instrument | `act-tests-ch10.l4` |
| 1440 | s 104 (2) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 104 (2): the reference to the statutory instruments made or in force under the law includes a reference to the law or instrument | `act-tests-ch10.l4` |
| 1441 | s 104 (3) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 104 (3): this chapter applies to the instrument as if it were a law, with any other necessary changes made | `act-tests-ch10.l4` |
| 1442 | s 104 (3) (a) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: s 104 (3): this chapter applies to the instrument as if it were a law, with any other necessary changes made | `act-tests-ch10.l4` |
| 1443 | s 104 (3) (b) [paragraph] | encoded | `act-ch10-referring-to-laws.l4`: s 104 (3): this chapter applies to the instrument as if it were a law, with any other necessary changes made | `act-tests-ch10.l4` |
| 1445 | s 105 Referring to provisions of laws | inert | reason 1: not operative; a heading |  |
| 1446 | s 105 text [opening words] | encoded | `act-ch10-referring-to-laws.l4`: s 105: the provision of the law may be referred to in the way | `act-tests-ch10.l4` |
| 1447-1448 | s 105 Example [example] | encoded | as a case in `act-tests-ch10.l4` | `act-tests-ch10.l4` |
| 1450 | s 106 References to provisions of laws are inclusive | inert | reason 1: not operative; a heading |  |
| 1451 | s 106 text [opening words] | fork | F6 (see the fork register); `act-ch10-referring-to-laws.l4`: s 106: the provision is within a reference to the part of the law | `act-tests-ch10.l4` |
| 1452 | s 106 (a) [paragraph] | fork | F6 (see the fork register); `act-ch10-referring-to-laws.l4`: s 106: the provision is within a reference to the part of the law | `act-tests-ch10.l4` |
| 1453 | s 106 (b) [paragraph] | fork | F6 (see the fork register); `act-ch10-referring-to-laws.l4`: s 106: the provision is within a reference to the part of the law | `act-tests-ch10.l4` |
| 1454 | s 106 (c) [paragraph] | fork | F6 (see the fork register); `act-ch10-referring-to-laws.l4`: s 106: the provision is within a reference to the part of the law | `act-tests-ch10.l4` |
| 1455-1458 | s 106 Examples [example] | fork | F6 (see the fork register); as a case in `act-tests-ch10.l4` | `act-tests-ch10.l4` |
| 1460 | s 106A References to paragraphs etc of laws | inert | reason 1: not operative; a heading |  |
| 1461 | s 106A (1) [subsection] | encoded | `act-ch10-referring-to-laws.l4`: s 106A (1): the reference includes the words | `act-tests-ch10.l4` |
| 1462 | s 106A (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1463 | s 106A (2) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1464 | s 106A (2) paragraph [definition] | encoded | `act-section-definitions.l4`: s 106A (2), definition of paragraph | `act-tests-section-definitions.l4` |
| 1466-1567 | Chapter 11 Republication of Acts and statutory instruments (Parts 11.1, 11.2, 11.3) | out of scope | assumed scope choice, not a ruling; Republication, and the editorial changes made on republication |  |
| 1568 | Chapter 12 Scope of Acts and statutory instruments | inert | reason 1: not operative; a heading |  |
| 1570 | s 120 Act to be interpreted not to exceed legislative powers of Assembly | inert | reason 1: not operative; a heading |  |
| 1571 | s 120 (1) [subsection] | encoded | `act-ch12-scope.l4`: s 120 (1): the interpretation of the Act is the one the section directs | `act-tests-ch12.l4` |
| 1572 | s 120 (2) [subsection] | encoded | `act-ch12-scope.l4`: s 120 (2) (a): the provision is effective as to the part; `act-ch12-scope.l4`: s 120 (2) (b): the remainder of the Act is affected | `act-tests-ch12.l4` |
| 1573 | s 120 (2) (a) [paragraph] | fork | F7 (see the fork register); `act-ch12-scope.l4`: s 120 (2) (a): the provision is effective as to the part | `act-tests-ch12.l4` |
| 1574 | s 120 (2) (b) [paragraph] | encoded | `act-ch12-scope.l4`: s 120 (2) (b): the remainder of the Act is affected | `act-tests-ch12.l4` |
| 1575 | s 120 (3) [subsection] | encoded | `act-ch12-scope.l4`: s 120 (3): the provision's application to other matters is affected | `act-tests-ch12.l4` |
| 1576 | s 120 (4) [subsection] | encoded | `act-ch12-scope.l4`: s 120 (4): this section is in addition to any provision of the Act itself | `act-tests-ch12.l4` |
| 1577 | s 120 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1578 | s 120 (5) [subsection] | encoded | `act-determinative.l4`: s 120 (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1579 | s 120 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1581 | s 121 Binding effect of Acts | inert | reason 1: not operative; a heading |  |
| 1582 | s 121 (1) [subsection] | encoded | `act-ch12-scope.l4`: Who or what an Act is applied to; `act-ch12-scope.l4`: s 121 (1), (2): the Act binds the subject | `act-tests-ch12.l4` |
| 1583 | s 121 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1584 | s 121 (2) [subsection] | encoded | `act-ch12-scope.l4`: s 121 (1), (2): the Act binds the subject | `act-tests-ch12.l4` |
| 1585 | s 121 (3) [subsection] | encoded | `act-ch12-scope.l4`: s 121 (3): subsection (1) makes the subject liable to be prosecuted for an offence | `act-tests-ch12.l4` |
| 1586 | s 121 (4) [subsection] | encoded | `act-ch12-scope.l4`: s 121 (4): the same degree of immunity extends to the government entity | `act-tests-ch12.l4` |
| 1587 | s 121 (5) [subsection] | encoded | `act-determinative.l4`: s 121 (5): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1588 | s 121 (5) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1589 | s 121 (6) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1590-1594 | s 121 (6) authorised [definition] | fork | F8 (see the fork register); `act-ch12-scope.l4`: Kind of entity of a government; `act-ch12-scope.l4`: s 121 (6): the act or omission of the government entity is authorised; `act-section-definitions.l4`: s 121 (6), definition of authorised | `act-tests-ch12.l4`, `act-tests-section-definitions.l4` |
| 1595 | s 121 (6) government [definition] | encoded | `act-ch12-scope.l4`: Who or what an Act is applied to; `act-ch12-scope.l4`: s 121 (6): the subject is a government; `act-section-definitions.l4`: s 121 (6), definition of government | `act-tests-ch12.l4`, `act-tests-section-definitions.l4` |
| 1596-1598 | s 121 (6) government entity [definition] | encoded | `act-ch12-scope.l4`: Kind of entity of a government; `act-ch12-scope.l4`: s 121 (6): the entity is a government entity; `act-section-definitions.l4`: s 121 (6), definition of government entity | `act-tests-ch12.l4`, `act-tests-section-definitions.l4` |
| 1600 | s 122 Application to Territory | inert | reason 1: not operative; a heading |  |
| 1601 | s 122 (1) [subsection] | encoded | `act-ch12-scope.l4`: s 122 (1) (a): the reference is a reference to the entity or position of that name or description in or for the Territory; `act-ch12-scope.l4`: s 122 (1) (b): the reference is a reference to the place, jurisdiction or thing of that name or description in or for the Territory | `act-tests-ch12.l4` |
| 1602 | s 122 (1) (a) [paragraph] | encoded | `act-ch12-scope.l4`: s 122 (1) (a): the reference is a reference to the entity or position of that name or description in or for the Territory | `act-tests-ch12.l4` |
| 1603 | s 122 (1) (b) [paragraph] | encoded | `act-ch12-scope.l4`: s 122 (1) (b): the reference is a reference to the place, jurisdiction or thing of that name or description in or for the Territory | `act-tests-ch12.l4` |
| 1604 | s 122 (2) [subsection] | encoded | `act-ch12-scope.l4`: s 122 (2): the reference must include the words | `act-tests-ch12.l4` |
| 1606 | Chapter 13 Structure of Acts and statutory instruments | inert | reason 1: not operative; a heading |  |
| 1608 | Part 13.1 General | inert | reason 1: not operative; a heading |  |
| 1610 | s 125 Meaning of law—ch 13 | inert | reason 1: not operative; a heading |  |
| 1611 | s 125 text [opening words] | encoded | `act-ch13-structure.l4`: s 125: the kind of document is a law for chapter 13 | `act-tests-ch13.l4` |
| 1612 | s 125 law [definition] | encoded | `act-ch13-structure.l4`: s 125: the kind of document is a law for chapter 13; `act-section-definitions.l4`: s 125, definition of law | `act-tests-ch13.l4`, `act-tests-section-definitions.l4` |
| 1613 | s 125 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1615 | s 126 Material that is part of Act or statutory instrument | inert | reason 1: not operative; a heading |  |
| 1616 | s 126 (1) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1617 | s 126 (2) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument; `act-interpretation-time.l4`: s 126 (2): the heading to a section or subsection is part of the Act or instrument | `act-tests-ch13.l4`, `act-tests-time.l4` |
| 1618 | s 126 (2) (a) [paragraph] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument; `act-interpretation-time.l4`: s 126 (2): the heading to a section or subsection is part of the Act or instrument | `act-tests-ch13.l4`, `act-tests-time.l4` |
| 1619 | s 126 (2) (b) [paragraph] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument; `act-interpretation-time.l4`: s 126 (2): the heading to a section or subsection is part of the Act or instrument | `act-tests-ch13.l4`, `act-tests-time.l4` |
| 1620 | s 126 (3) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1621 | s 126 (4) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1622 | s 126 (5) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1623 | s 126 (6) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1624 | s 126 (7) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1625 | s 126 (8) [subsection] | encoded | `act-ch13-structure.l4`: s 126 (8), s 127 (6): a reference to a section or subsection is a reference to a corresponding provision | `act-tests-ch13.l4` |
| 1626 | s 126 (8) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1627 | s 126 (9) [subsection] | encoded | `act-determinative.l4`: s 126 (9): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1628 | s 126 (9) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1630 | s 127 Material that is not part of Act or statutory instrument | inert | reason 1: not operative; a heading |  |
| 1631 | s 127 (1) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1632 | s 127 (2) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1633 | s 127 (3) [subsection] | encoded | `act-ch13-structure.l4`: Kind of material in or to an Act or instrument; `act-ch13-structure.l4`: s 126, s 127: the material is part of the Act or instrument | `act-tests-ch13.l4` |
| 1634 | s 127 (4) [subsection] | encoded | `act-ch13-structure.l4`: s 127 (4): this section prevents the amendment of a note, table, guide, index or heading | `act-tests-ch13.l4` |
| 1635 | s 127 (5) [subsection] | encoded | `act-ch13-structure.l4`: s 127 (5): the note, table, guide or index becomes part of the Act or instrument because it is amended or inserted | `act-tests-ch13.l4` |
| 1636 | s 127 (6) [subsection] | encoded | `act-ch13-structure.l4`: s 126 (8), s 127 (6): a reference to a section or subsection is a reference to a corresponding provision | `act-tests-ch13.l4` |
| 1637 | s 127 (6) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1638 | s 127 (7) [subsection] | encoded | `act-determinative.l4`: s 127 (7): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1639 | s 127 (7) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1641 | Part 13.2 Particular kinds of provisions | inert | reason 1: not operative; a heading |  |
| 1643 | s 130 What is a definition? | inert | reason 1: not operative; a heading |  |
| 1644 | s 130 text [opening words] | encoded | `act-ch13-structure.l4`: s 130: the provision is a definition; `act-nouns.l4`: How a term is defined | `act-tests-ch13.l4` |
| 1645 | s 130 (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 130: the provision is a definition; `act-nouns.l4`: How a term is defined | `act-tests-ch13.l4` |
| 1646 | s 130 (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 130: the provision is a definition; `act-nouns.l4`: How a term is defined | `act-tests-ch13.l4` |
| 1647-1657 | s 130 Examples—definitions [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1658 | s 130 Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1659 | s 130 Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1660 | s 130 Note 3 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1661 | s 130 Note 4 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1663 | s 131 Signpost definitions | inert | reason 1: not operative; a heading |  |
| 1664 | s 131 (1) [subsection] | encoded | `act-ch13-structure.l4`: Meaning a signpost definition gives a term; `act-ch13-structure.l4`: s 131 (1): the meaning a signpost definition gives the term | `act-tests-ch13.l4` |
| 1665-1668 | s 131 (1) Examples [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1669 | s 131 (2) [subsection] | encoded | `act-ch13-structure.l4`: s 131 (2): the sections that s 131 is subject to | `act-tests-ch13.l4` |
| 1670 | s 131 (3) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1671 | s 131 (3) instrument [definition] | encoded | `act-section-definitions.l4`: s 131 (3), definition of instrument | `act-tests-section-definitions.l4` |
| 1672 | s 131 (3) law [definition] | encoded | `act-section-definitions.l4`: s 131 (3), definition of law | `act-tests-section-definitions.l4` |
| 1673 | s 131 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1675 | s 132 Examples | inert | reason 1: not operative; a heading |  |
| 1676 | s 132 (1) [subsection] | encoded | `act-ch13-structure.l4`: s 132 (1) (a): an example is exhaustive; `act-ch13-structure.l4`: s 132 (1) (b): an example may extend the meaning of the Act or instrument, or of the provision to which it relates; `act-ch13-structure.l4`: s 132 (1) (b): an example limits the meaning of the Act or instrument, or of the provision to which it relates | `act-tests-ch13.l4` |
| 1677 | s 132 (1) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 132 (1) (a): an example is exhaustive | `act-tests-ch13.l4` |
| 1678 | s 132 (1) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 132 (1) (b): an example may extend the meaning of the Act or instrument, or of the provision to which it relates; `act-ch13-structure.l4`: s 132 (1) (b): an example limits the meaning of the Act or instrument, or of the provision to which it relates | `act-tests-ch13.l4` |
| 1679 | s 132 (2) [subsection] | encoded | `act-ch13-structure.l4`: s 132 (2): the statement has a form an example may take | `act-tests-ch13.l4` |
| 1680 | s 132 (2) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 132 (2): the statement has a form an example may take | `act-tests-ch13.l4` |
| 1681 | s 132 (2) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 132 (2): the statement has a form an example may take | `act-tests-ch13.l4` |
| 1682 | s 132 (3) [subsection] | encoded | `act-ch13-structure.l4`: s 132 (3): subsection (2) limits the form that an example may take | `act-tests-ch13.l4` |
| 1683 | s 132 (4) [subsection] | encoded | `act-determinative.l4`: s 132 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1684 | s 132 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1686 | s 133 Penalty units | inert | reason 1: not operative; a heading |  |
| 1687 | s 133 (1) [subsection] | encoded | `act-ch13-structure.l4`: s 133 (1): the fine, in penalty units; `act-ch13-structure.l4`: s 133 (1), (2): the fine, in dollars | `act-tests-ch13.l4` |
| 1688 | s 133 (2) [subsection] | encoded | `act-ch13-structure.l4`: s 133 (2): the amount of a penalty unit, in dollars; `act-ch13-structure.l4`: s 133 (1), (2): the fine, in dollars | `act-tests-ch13.l4` |
| 1689 | s 133 (2) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 133 (2): the amount of a penalty unit, in dollars; `act-ch13-structure.l4`: s 133 (1), (2): the fine, in dollars | `act-tests-ch13.l4` |
| 1690 | s 133 (2) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 133 (2): the amount of a penalty unit, in dollars; `act-ch13-structure.l4`: s 133 (1), (2): the fine, in dollars | `act-tests-ch13.l4` |
| 1691 | s 133 (3) [subsection] | fork | F11 (see the fork register); `act-ch13-structure.l4`: s 133 (3): the last day by which the Attorney-General must have reviewed the amount of a penalty unit | `act-tests-ch13.l4` |
| 1692 | s 133 (4) [subsection] | encoded | `act-determinative.l4`: s 133 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1693 | s 133 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1695 | s 134 Penalties at end of sections and subsections | inert | reason 1: not operative; a heading |  |
| 1696 | s 134 (1) [subsection] | encoded | `act-ch13-structure.l4`: Where a penalty is stated; `act-ch13-structure.l4`: s 134 (1), s 135 (1): the section that governs the stated penalty; `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to | `act-tests-ch13.l4` |
| 1697 | s 134 (1) (a) [paragraph] | encoded | `act-ch13-structure.l4`: Where a penalty is stated; `act-ch13-structure.l4`: s 134 (1), s 135 (1): the section that governs the stated penalty; `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to | `act-tests-ch13.l4` |
| 1698 | s 134 (1) (b) [paragraph] | encoded | `act-ch13-structure.l4`: Where a penalty is stated; `act-ch13-structure.l4`: s 134 (1), s 135 (1): the section that governs the stated penalty; `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to | `act-tests-ch13.l4` |
| 1699 | s 134 (1) (c) [paragraph] | encoded | `act-ch13-structure.l4`: Where a penalty is stated; `act-ch13-structure.l4`: s 134 (1), s 135 (1): the section that governs the stated penalty; `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to | `act-tests-ch13.l4` |
| 1700-1702 | s 134 (1) Example—par [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1703-1705 | s 134 (1) Example—par [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1706-1712 | s 134 (1) Examples—par [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1713 | s 134 (2) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to; `act-ch13-structure.l4`: s 134 (2), (3), s 135 (2), (3): what the stated penalty indicates | `act-tests-ch13.l4` |
| 1714-1716 | s 134 (2) Example—penalty [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1717-1721 | s 134 (2) Example—penalty [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1722 | s 134 (3) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to; `act-ch13-structure.l4`: s 134 (2), (3), s 135 (2), (3): what the stated penalty indicates | `act-tests-ch13.l4` |
| 1723-1725 | s 134 (3) Example—penalty [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1726-1730 | s 134 (3) Example—penalty [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1731 | s 134 (4) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1732 | s 134 (4) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1733 | s 134 (4) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1734 | s 134 (5) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (5): the first penalty is taken to be expressed as applying only to the last subsection | `act-tests-ch13.l4` |
| 1735 | s 134 (5) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (5): the first penalty is taken to be expressed as applying only to the last subsection | `act-tests-ch13.l4` |
| 1736 | s 134 (5) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (5): the first penalty is taken to be expressed as applying only to the last subsection | `act-tests-ch13.l4` |
| 1737-1738 | s 134 (5) (c) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (5): the first penalty is taken to be expressed as applying only to the last subsection | `act-tests-ch13.l4` |
| 1739-1745 | s 134 (5) Example [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1746 | s 134 (6) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (6), s 135 (5): the penalty is at the end of the section or subsection | `act-tests-ch13.l4` |
| 1747 | s 134 (7) [subsection] | encoded | `act-determinative.l4`: s 134 (7): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1748 | s 134 (7) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1750 | s 135 Penalties not at end of sections and subsections | inert | reason 1: not operative; a heading |  |
| 1751 | s 135 (1) [subsection] | encoded | `act-ch13-structure.l4`: Where a penalty is stated; `act-ch13-structure.l4`: s 134 (1), s 135 (1): the section that governs the stated penalty | `act-tests-ch13.l4` |
| 1752 | s 135 (2) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (2), (3), s 135 (2), (3): what the stated penalty indicates | `act-tests-ch13.l4` |
| 1753-1754 | s 135 (2) Example [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1755 | s 135 (3) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (1) to (3), s 135 (3): what the stated penalty applies to; `act-ch13-structure.l4`: s 134 (2), (3), s 135 (2), (3): what the stated penalty indicates | `act-tests-ch13.l4` |
| 1756-1757 | s 135 (3) Example [example] | encoded | as a case in `act-tests-ch13.l4` | `act-tests-ch13.l4` |
| 1758 | s 135 (4) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1759 | s 135 (4) (a) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1760 | s 135 (4) (b) [paragraph] | encoded | `act-ch13-structure.l4`: s 134 (4), s 135 (4): the penalty may be imposed | `act-tests-ch13.l4` |
| 1761 | s 135 (5) [subsection] | encoded | `act-ch13-structure.l4`: s 134 (6), s 135 (5): the penalty is at the end of the section or subsection | `act-tests-ch13.l4` |
| 1762 | s 135 (6) [subsection] | encoded | `act-determinative.l4`: s 135 (6): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1763 | s 135 (6) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1765 | Chapter 14 Interpretation of Acts and statutory instruments | inert | reason 1: not operative; a heading |  |
| 1767 | Part 14.1 Purpose and scope | inert | reason 1: not operative; a heading |  |
| 1769 | s 136 Meaning of Act—ch 14 | inert | reason 1: not operative; a heading |  |
| 1770 | s 136 text [opening words] | encoded | `act-ch14-interpretation.l4`: s 136: the kind of document is an Act for chapter 14 | `act-tests-ch14.l4` |
| 1771 | s 136 Act [definition] | encoded | `act-ch14-interpretation.l4`: s 136: the kind of document is an Act for chapter 14; `act-section-definitions.l4`: s 136, definition of Act | `act-tests-ch14.l4`, `act-tests-section-definitions.l4` |
| 1772 | s 136 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1774 | s 137 Purpose and scope—ch 14 | inert | reason 1: not operative; a heading |  |
| 1775 | s 137 (1) [subsection] | inert | reason 1: not operative; purpose and limit of chapter 14, stated; the rules the chapter gives are in `act-ch14-interpretation.l4` |  |
| 1776 | s 137 (2) [subsection] | inert | reason 1: not operative; purpose and limit of chapter 14, stated; the rules the chapter gives are in `act-ch14-interpretation.l4` |  |
| 1777 | s 137 (3) [subsection] | encoded | `act-ch14-interpretation.l4`: s 137 (3), (4): the common law presumption operates in conjunction with chapter 14 | `act-tests-ch14.l4` |
| 1778 | s 137 (4) [subsection] | encoded | `act-ch14-interpretation.l4`: s 137 (3), (4): the common law presumption operates in conjunction with chapter 14 | `act-tests-ch14.l4` |
| 1780 | Part 14.2 Key principles of interpretation | inert | reason 1: not operative; a heading |  |
| 1782 | s 138 Meaning of working out the meaning of an Act—pt 14.2 | inert | reason 1: not operative; a heading |  |
| 1783 | s 138 text [opening words] | encoded | `act-ch14-interpretation.l4`: s 138: the task is working out the meaning of an Act | `act-tests-ch14.l4` |
| 1784-1788 | s 138 working out the meaning of an Act [definition] | encoded | `act-ch14-interpretation.l4`: s 138: the task is working out the meaning of an Act; `act-section-definitions.l4`: s 138, definition of working out the meaning of an Act | `act-tests-ch14.l4`, `act-tests-section-definitions.l4` |
| 1790 | s 139 Interpretation best achieving Act’s purpose | inert | reason 1: not operative; a heading |  |
| 1791 | s 139 (1) [subsection] | encoded | `act-ch14-interpretation.l4`: s 139 (1): the interpretation is to be preferred to any other interpretation | `act-tests-ch14.l4` |
| 1792 | s 139 (2) [subsection] | encoded | `act-ch14-interpretation.l4`: s 139 (2): section 139 applies | `act-tests-ch14.l4` |
| 1793 | s 139 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1795 | s 140 Legislative context | inert | reason 1: not operative; a heading |  |
| 1796 | s 140 text [opening words] | encoded | `act-ch14-interpretation.l4`: s 140: the provisions of the Act must be read in the context of the Act as a whole | `act-tests-ch14.l4` |
| 1797-1802 | s 140 Examples [example] | encoded | as a case in `act-tests-ch14.l4` | `act-tests-ch14.l4` |
| 1803 | s 140 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1805 | s 141 Non-legislative context generally | inert | reason 1: not operative; a heading |  |
| 1806 | s 141 (1) [subsection] | encoded | `act-ch14-interpretation.l4`: s 141 (1): the material may be considered | `act-tests-ch14.l4` |
| 1807 | s 141 (1) Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1808 | s 141 (1) Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1809 | s 141 (1) Note 3 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1810 | s 141 (2) [subsection] | encoded | `act-ch14-interpretation.l4`: s 141 (2): the matters that must be taken into account | `act-tests-ch14.l4` |
| 1811 | s 141 (2) (a) [paragraph] | encoded | `act-ch14-interpretation.l4`: s 141 (2): the matters that must be taken into account | `act-tests-ch14.l4` |
| 1812 | s 141 (2) (b) [paragraph] | encoded | `act-ch14-interpretation.l4`: s 141 (2): the matters that must be taken into account | `act-tests-ch14.l4` |
| 1813 | s 141 (2) (c) [paragraph] | encoded | `act-ch14-interpretation.l4`: s 141 (2): the matters that must be taken into account | `act-tests-ch14.l4` |
| 1814 | s 141 (3) [subsection] | encoded | `act-ch14-interpretation.l4`: s 141 (3): subsection (2) limits the matters that may be taken into account | `act-tests-ch14.l4` |
| 1815 | s 141 (4) [subsection] | encoded | `act-ch14-interpretation.l4`: s 141 (4): the material is taken to be accessible to the public for subsection (2) (c) | `act-tests-ch14.l4` |
| 1816 | s 141 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1818 | s 142 Non-legislative context—material that may be considered | inert | reason 1: not operative; a heading |  |
| 1819 | s 142 (1) [subsection] | encoded | `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act | `act-tests-ch14.l4` |
| 1820 | s 142 (2) [subsection] | fork | F12 (see the fork register); `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1821 | s 142 (3) [subsection] | encoded | `act-ch14-interpretation.l4`: s 142 (3): this section limits the material that may be considered | `act-tests-ch14.l4` |
| 1822 | s 142 (3) Table 142 [tabletitle] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1824 | s 142 (3) column 1 item [tablehead] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1825 | s 142 (3) 1 [tablerow] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1826 | s 142 (3) 2 [tablerow] | fork | F12 (see the fork register); `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1827 | s 142 (3) 3 [tablerow] | fork | F12 (see the fork register); `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1828 | s 142 (3) 4 [tablerow] | fork | F12 (see the fork register); `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1829 | s 142 (3) 5 [tablerow] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1830 | s 142 (3) 6 [tablerow] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1831 | s 142 (3) 7 [tablerow] | encoded | `act-ch14-interpretation.l4`: Material in table 142; `act-ch14-interpretation.l4`: s 142 (1): the material may be considered in working out the meaning of an Act; `act-ch14-interpretation.l4`: s 142 (2): the material may be considered in working out the meaning of a statutory instrument | `act-tests-ch14.l4` |
| 1833 | s 143 Law stating material for consideration in working out meaning | inert | reason 1: not operative; a heading |  |
| 1834 | s 143 (1) [subsection] | encoded | `act-ch14-interpretation.l4`: s 143 (1): the provision prevents, by implication, other material of the same or similar kind being considered | `act-tests-ch14.l4` |
| 1835 | s 143 (2) [subsection] | encoded | `act-ch14-interpretation.l4`: What is being interpreted for s 143; `act-ch14-interpretation.l4`: Candidate for a relevant law | `act-tests-ch14.l4` |
| 1836-1839 | s 143 (2) relevant law [definition] | encoded | `act-ch14-interpretation.l4`: What is being interpreted for s 143; `act-ch14-interpretation.l4`: Candidate for a relevant law; `act-ch14-interpretation.l4`: s 143 (2): the candidate is a relevant law; and 1 more | `act-tests-ch14.l4`, `act-tests-section-definitions.l4` |
| 1841 | Chapter 15 Aids to interpretation | inert | reason 1: not operative; a heading |  |
| 1843 | Part 15.1 General | inert | reason 1: not operative; a heading |  |
| 1845 | s 144 Meaning of commonly-used terms | inert | reason 1: not operative; a heading |  |
| 1846 | s 144 text [opening words] | encoded | `act-ch15-aids.l4`: s 144: a definition in the dictionary, part 1 applies to the thing | `act-tests-ch15.l4` |
| 1847 | s 144 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1849 | s 145 Gender and number | inert | reason 1: not operative; a heading |  |
| 1850 | s 145 text [opening words] | encoded | `act-ch15-aids.l4`: s 145 (a): the word includes every other gender | `act-tests-ch15.l4` |
| 1851 | s 145 (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 145 (a): the word includes every other gender | `act-tests-ch15.l4` |
| 1852 | s 145 (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 145 (b): the numbers the word covers | `act-tests-ch15.l4` |
| 1854 | s 146 Meaning of may and must | inert | reason 1: not operative; a heading |  |
| 1855 | s 146 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 146 (1), (2): what the word indicates about the function | `act-tests-ch15.l4` |
| 1856 | s 146 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1857 | s 146 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 146 (1), (2): what the word indicates about the function | `act-tests-ch15.l4` |
| 1858 | s 146 (3) [subsection] | encoded | `act-determinative.l4`: s 146 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1859 | s 146 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1860 | s 146 (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1861 | s 146 (4) applicable law [definition] | encoded | `act-interpretation-time.l4`: s 146 (4): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 146 (4), definition of applicable law | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1862 | s 146 (4) applicable provision [definition] | encoded | `act-interpretation-time.l4`: s 146 (4): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 146 (4), definition of applicable provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1863-1865 | s 146 (4) application date [definition] | encoded | `act-interpretation-time.l4`: s 146 (4): the application date; `act-section-definitions.l4`: s 146 (4), definition of application date | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1866 | s 146 (4) inserted, for a provision [definition] | encoded | `act-section-definitions.l4`: s 146 (4), definition of inserted, for a provision | `act-tests-section-definitions.l4` |
| 1868 | s 147 Changes of drafting practice not to affect meaning | inert | reason 1: not operative; a heading |  |
| 1869 | s 147 (1) [subsection] | inert | reason 1: not operative; purpose of the section, stated; the rule it gives is encoded from its later subsections |  |
| 1870 | s 147 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1871 | s 147 (2) [subsection] | inert | reason 1: not operative; purpose of the section, stated; the rule it gives is encoded from its later subsections |  |
| 1872 | s 147 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 147 (3) to (5): the ideas in the two provisions are regarded as different | `act-tests-ch15.l4` |
| 1873 | s 147 (4) [subsection] | encoded | `act-ch15-aids.l4`: s 147 (3) to (5): the ideas in the two provisions are regarded as different | `act-tests-ch15.l4` |
| 1874 | s 147 (5) [subsection] | encoded | `act-ch15-aids.l4`: s 147 (3) to (5): the ideas in the two provisions are regarded as different | `act-tests-ch15.l4` |
| 1875 | s 147 (6) [subsection] | encoded | `act-ch15-aids.l4`: s 147 (6): regard must be had to the context and history of the 2 provisions | `act-tests-ch15.l4` |
| 1876 | s 147 (7) [subsection] | encoded | `act-ch15-aids.l4`: s 147 (7): subsection (6) limits the matters to which regard may be had | `act-tests-ch15.l4` |
| 1877 | s 147 (8) [subsection] | encoded | `act-determinative.l4`: s 147 (8): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1878 | s 147 (8) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1880 | s 148 Terms used in instruments have same meanings as in authorising laws | inert | reason 1: not operative; a heading |  |
| 1881 | s 148 text [opening words] | encoded | `act-ch15-aids.l4`: s 148: the meaning of a term used in a statutory instrument | `act-tests-ch15.l4` |
| 1883 | s 149 Age in years | inert | reason 1: not operative; a heading |  |
| 1884 | s 149 text [opening words] | fork | F13 (see the fork register); `act-interpretation-time.l4`: s 149: the birthday falls in the year; `act-interpretation-time.l4`: s 149: the age in years of a person on a day; `act-interpretation-time.l4`: s 149: the day a person attains an age in years | `act-tests-time.l4` |
| 1886 | s 150 Measurement of distance | inert | reason 1: not operative; a heading |  |
| 1887 | s 150 text [opening words] | encoded | `act-ch15-aids.l4`: s 150: the distance is measured as the Act requires | `act-tests-ch15.l4` |
| 1889 | s 151 Working out periods of time generally | inert | reason 1: not operative; a heading |  |
| 1890 | s 151 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 151 (1): s 151 applies in working out the period | `act-tests-ch15.l4` |
| 1891-1900 | s 151 (1) Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1901 | s 151 (1) Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1902 | s 151 (2) [subsection] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day | `act-tests-time.l4` |
| 1903 | s 151 (2) Table 151 Working out periods of time [tabletitle] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day | `act-tests-time.l4` |
| 1905 | s 151 (2) column 1 item [tablehead] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day | `act-tests-time.l4` |
| 1906 | s 151 (2) 1 [tablerow] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day; `act-interpretation-time.l4`: s 151 (2), table 151: the first day of a period that begins at, on, with or from a stated day; `act-interpretation-time.l4`: s 151: the last day of a period of days that begins on or from a stated day; and 2 more | `act-tests-time.l4` |
| 1907 | s 151 (2) 2 [tablerow] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day; `act-interpretation-time.l4`: s 151 (2), table 151: the first day of a period that begins at, on, with or from a stated day; `act-interpretation-time.l4`: s 151: the last day of a period of days that begins on or from a stated day; and 2 more | `act-tests-time.l4` |
| 1908 | s 151 (2) 3 [tablerow] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day; `act-interpretation-time.l4`: s 151: the first day of a period of days that ends at, by, on or with, or before, a stated day | `act-tests-time.l4` |
| 1909 | s 151 (2) 4 [tablerow] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day; `act-interpretation-time.l4`: s 151: the first day of a period of days that ends at, by, on or with, or before, a stated day | `act-tests-time.l4` |
| 1910 | s 151 (2) 5 [tablerow] | encoded | `act-interpretation-time.l4`: s 151 (2), table 151: the period includes the stated day; `act-interpretation-time.l4`: s 151 (2), table 151 item 5: the latest day for the earlier event, so that the given number of days lie between the 2 events; `act-interpretation-time.l4`: s 151 (2), table 151 item 5: the number of days between 2 events | `act-tests-time.l4` |
| 1911-1912 | s 151 (2) Example—item [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1913-1914 | s 151 (2) Example—item [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1915-1916 | s 151 (2) Example—item [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1917-1918 | s 151 (2) Example—item [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1919-1920 | s 151 (2) Example—item [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1921 | s 151 (3) [subsection] | encoded | `act-interpretation-time.l4`: s 151 (3): the thing may be done on the stated day | `act-tests-time.l4` |
| 1922 | s 151 (4) [subsection] | encoded | `act-determinative.l4`: s 151 (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1923 | s 151 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1924 | s 151 (5) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1925 | s 151 (5) applicable law [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151 (5), definition of applicable law | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1926 | s 151 (5) applicable provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151 (5), definition of applicable provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1927 | s 151 (5) inserted, for a provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151 (5), definition of inserted, for a provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1929 | s 151A Periods of time ending on non-working days | inert | reason 1: not operative; a heading |  |
| 1930 | s 151A (1) [subsection] | encoded | `act-interpretation-time.l4`: s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day | `act-tests-time.l4` |
| 1931 | s 151A (1) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day | `act-tests-time.l4` |
| 1932 | s 151A (1) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day | `act-tests-time.l4` |
| 1933 | s 151A (2) [subsection] | encoded | `act-interpretation-time.l4`: s 151A (2): the first working day on or after a day, searching a limited number of days; `act-interpretation-time.l4`: s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day; `act-interpretation-time.l4`: s 151 and s 151A: the last day on which the thing may be done within a period that begins on or from a stated day | `act-tests-time.l4` |
| 1934 | s 151A (3) [subsection] | encoded | `act-determinative.l4`: s 151A (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1935 | s 151A (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1936 | s 151A (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1937 | s 151A (4) applicable law [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151A (4), definition of applicable law | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1938 | s 151A (4) applicable provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151A (4), definition of applicable provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1939 | s 151A (4) inserted, for a provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151A (4), definition of inserted, for a provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1940-1944 | s 151A (4) public entity [definition] | encoded | `act-section-definitions.l4`: s 151A (4), definition of public entity | `act-tests-section-definitions.l4` |
| 1945-1950 | s 151A (4) working day [definition] | encoded | `act-interpretation-time.l4`: s 151A (4): the day is a working day for doing the thing; `act-section-definitions.l4`: s 151A (4), definition of working day | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1951-1952 | s 151A (4) Example—par [example] | encoded | as a case in `act-tests-time.l4` | `act-tests-time.l4` |
| 1954 | s 151B Doing things for which no time is fixed | inert | reason 1: not operative; a heading |  |
| 1955 | s 151B (1) [subsection] | encoded | `act-ch15-aids.l4`: s 151B (1): s 151B applies to the thing | `act-tests-ch15.l4` |
| 1956 | s 151B (1) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 151B (1): s 151B applies to the thing | `act-tests-ch15.l4` |
| 1957 | s 151B (1) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 151B (1): s 151B applies to the thing | `act-tests-ch15.l4` |
| 1958 | s 151B (2) [subsection] | encoded | `act-ch15-aids.l4`: s 151B (2): when the thing must or may be done | `act-tests-ch15.l4` |
| 1960 | s 151C Power to extend time | inert | reason 1: not operative; a heading |  |
| 1961 | s 151C (1) [subsection] | encoded | `act-ch15-aids.l4`: s 151C (1): s 151C applies to the thing | `act-tests-ch15.l4` |
| 1962 | s 151C (1) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 151C (1): s 151C applies to the thing | `act-tests-ch15.l4` |
| 1963 | s 151C (1) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 151C (1): s 151C applies to the thing | `act-tests-ch15.l4` |
| 1964 | s 151C (2) [subsection] | encoded | `act-ch15-aids.l4`: s 151C (2): a person may apply for the relevant time to be extended | `act-tests-ch15.l4` |
| 1965 | s 151C (3) [subsection] | encoded | `act-ch15-aids.l4`: s 151C (3): the court or other entity may extend the relevant time | `act-tests-ch15.l4` |
| 1966 | s 151C (4) [subsection] | encoded | `act-determinative.l4`: s 151C (4): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1967 | s 151C (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1968 | s 151C (5) [subsection] | encoded | `act-ch15-aids.l4`: s 151C (5): s 151C applies to the law or provision | `act-tests-ch15.l4` |
| 1969 | s 151C (6) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 1970 | s 151C (6) applicable law [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151C (6), definition of applicable law | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1971 | s 151C (6) applicable provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151C (6), definition of applicable provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1972 | s 151C (6) inserted, for a provision [definition] | encoded | `act-interpretation-time.l4`: s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision; `act-section-definitions.l4`: s 151C (6), definition of inserted, for a provision | `act-tests-time.l4`, `act-tests-section-definitions.l4` |
| 1974 | s 152 Continuing effect of obligations | inert | reason 1: not operative; a heading |  |
| 1975 | s 152 text [opening words] | encoded | `act-ch15-aids.l4`: s 152: the obligation to do the act continues | `act-tests-ch15.l4` |
| 1976 | s 152 (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 152: the obligation to do the act continues | `act-tests-ch15.l4` |
| 1977 | s 152 (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 152: the obligation to do the act continues | `act-tests-ch15.l4` |
| 1979 | Part 15.2 Definitions | inert | reason 1: not operative; a heading |  |
| 1980 | note at line 1980 | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1982 | s 155 Definitions apply subject to contrary intention | inert | reason 1: not operative; a heading |  |
| 1983 | s 155 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 155 (1): the definition applies | `act-tests-ch15.l4` |
| 1984 | s 155 (2) [subsection] | encoded | `act-determinative.l4`: s 155 (2): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 1985 | s 155 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1987 | s 156 Application of definitions in dictionaries and sections | inert | reason 1: not operative; a heading |  |
| 1988 | s 156 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 156 (1) to (3): how far the definition applies | `act-tests-ch15.l4` |
| 1989-1994 | s 156 (1) Examples [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 1995 | s 156 (1) Note 1 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1996 | s 156 (1) Note 2 [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 1997 | s 156 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 156 (1) to (3): how far the definition applies | `act-tests-ch15.l4` |
| 1998-2003 | s 156 (2) Examples [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2004 | s 156 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 156 (1) to (3): how far the definition applies | `act-tests-ch15.l4` |
| 2005-2006 | s 156 (3) Example [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2007 | s 156 (4) [subsection] | encoded | `act-ch15-aids.l4`: s 156 (4): what a reference to a section is a reference to | `act-tests-ch15.l4` |
| 2008 | s 156 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2010 | s 157 Defined terms—other parts of speech and grammatical forms | inert | reason 1: not operative; a heading |  |
| 2011 | s 157 text [opening words] | encoded | `act-ch15-aids.l4`: s 157: the other parts of speech and grammatical forms of the term have corresponding meanings | `act-tests-ch15.l4` |
| 2012-2013 | s 157 Example [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2015 | Part 15.3 References to various entities and things | inert | reason 1: not operative; a heading |  |
| 2016 | note at line 2016 | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2018 | s 160 References to people generally | inert | reason 1: not operative; a heading |  |
| 2019 | s 160 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 160 (1): a reference to a person generally includes the party | `act-tests-ch15.l4` |
| 2020 | s 160 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 160 (2): subsection (1) is displaced | `act-tests-ch15.l4` |
| 2021-2026 | s 160 (2) Examples—references [example] | encoded | `act-ch15-aids.l4`: s 160, examples: what the expression refers to | `act-tests-ch15.l4` |
| 2027-2029 | s 160 (2) Examples—express [example] | encoded | `act-ch15-aids.l4`: s 160, examples: what the expression refers to | `act-tests-ch15.l4` |
| 2030-2034 | s 160 (2) Examples—express [example] | encoded | `act-ch15-aids.l4`: s 160, examples: what the expression refers to | `act-tests-ch15.l4` |
| 2035 | s 160 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 160 (3): subsection (2) limits the operation of section 6 | `act-tests-ch15.l4` |
| 2036 | s 160 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2038 | s 161 Corporations liable to offences | inert | reason 1: not operative; a heading |  |
| 2039 | s 161 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 161 (1), (2): a provision of a law that creates an offence applies to the party | `act-tests-ch15.l4` |
| 2040 | s 161 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 161 (1), (2): a provision of a law that creates an offence applies to the party | `act-tests-ch15.l4` |
| 2041-2044 | s 161 (2) Example [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2045 | s 161 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2046 | s 161 (3) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2047 | s 161 (3) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2048 | s 161 (3) (c) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2049 | s 161 (3) (d) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2050 | s 161 (3) (e) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2051 | s 161 (3) (f) [paragraph] | encoded | `act-ch15-aids.l4`: s 161 (3): the most the court may impose on the corporation, in penalty units | `act-tests-ch15.l4` |
| 2052 | s 161 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2053 | s 161 (4) [subsection] | encoded | `act-ch15-aids.l4`: s 161 (4): the kind of document is a law for this section | `act-tests-ch15.l4` |
| 2054 | s 161 (4) law [definition] | encoded | `act-ch15-aids.l4`: s 161 (4): the kind of document is a law for this section; `act-section-definitions.l4`: s 161 (4), definition of law | `act-tests-ch15.l4`, `act-tests-section-definitions.l4` |
| 2056 | s 162 References to a Minister or the Minister | inert | reason 1: not operative; a heading |  |
| 2057 | s 162 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 162 (1): the person is a Minister | `act-tests-ch15.l4` |
| 2058 | s 162 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2059 | s 162 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 162 (2): who a reference to the Minister without a title is a reference to | `act-tests-ch15.l4` |
| 2060 | s 162 (2) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 162 (2): who a reference to the Minister without a title is a reference to | `act-tests-ch15.l4` |
| 2061-2063 | s 162 (2) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 162 (2): who a reference to the Minister without a title is a reference to | `act-tests-ch15.l4` |
| 2064 | s 162 (2) (c) [paragraph] | encoded | `act-ch15-aids.l4`: s 162 (2): who a reference to the Minister without a title is a reference to | `act-tests-ch15.l4` |
| 2065 | s 162 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 162 (3): the reference to the Minister in subsection (2) includes the person | `act-tests-ch15.l4` |
| 2066 | s 162 (3) Minister [definition] | encoded | `act-ch15-aids.l4`: s 162 (3): the reference to the Minister in subsection (2) includes the person; `act-section-definitions.l4`: s 162 (3), definition of Minister | `act-tests-ch15.l4`, `act-tests-section-definitions.l4` |
| 2067 | s 162 (4) [subsection] | encoded | `act-ch15-aids.l4`: s 162 (4): the provision whose administration decides which Minister the reference is to | `act-tests-ch15.l4` |
| 2068 | s 162 (4) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2070 | s 163 References to a director-general or the director-general | inert | reason 1: not operative; a heading |  |
| 2071 | s 163 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 163 (1): the person is a director-general | `act-tests-ch15.l4` |
| 2072 | s 163 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 163 (2): which administrative unit's director-general a reference to the director-general without a title is a reference to | `act-tests-ch15.l4` |
| 2073 | s 163 (2) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 163 (2): which administrative unit's director-general a reference to the director-general without a title is a reference to | `act-tests-ch15.l4` |
| 2074-2076 | s 163 (2) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 163 (2): which administrative unit's director-general a reference to the director-general without a title is a reference to | `act-tests-ch15.l4` |
| 2077 | s 163 (2) (c) [paragraph] | encoded | `act-ch15-aids.l4`: s 163 (2): which administrative unit's director-general a reference to the director-general without a title is a reference to | `act-tests-ch15.l4` |
| 2078 | s 163 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2079 | s 163 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 163 (3): the provision whose responsibility decides which director-general the reference is to | `act-tests-ch15.l4` |
| 2080 | s 163 (4) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 2081 | s 163 (4) director-general, of an administrative unit [definition] | encoded | `act-section-definitions.l4`: s 163 (4), definition of director-general, of an administrative unit | `act-tests-section-definitions.l4` |
| 2082 | s 163 (4) Public Sector Management Act [definition] | encoded | `act-section-definitions.l4`: s 163 (4), definition of Public Sector Management Act | `act-tests-section-definitions.l4` |
| 2083 | s 163 (4) responsible, for a provision [definition] | encoded | `act-section-definitions.l4`: s 163 (4), definition of responsible, for a provision | `act-tests-section-definitions.l4` |
| 2085 | s 164 References to Australian Standards etc | inert | reason 1: not operative; a heading |  |
| 2086 | s 164 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 164 (1), (2): the publisher of the standard a reference names | `act-tests-ch15.l4` |
| 2087 | s 164 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 164 (1), (2): the publisher of the standard a reference names | `act-tests-ch15.l4` |
| 2089 | s 165 References to Assembly committees that no longer exist | inert | reason 1: not operative; a heading |  |
| 2090 | s 165 text [opening words] | encoded | `act-ch15-aids.l4`: s 165: the committee a reference to a committee that no longer exists is a reference to | `act-tests-ch15.l4` |
| 2092 | s 168 References to person with interest in land include personal representative etc | inert | reason 1: not operative; a heading |  |
| 2093 | s 168 text [opening words] | encoded | `act-ch15-aids.l4`: s 168: a reference to a person with an interest in land or other property includes the person | `act-tests-ch15.l4` |
| 2094-2100 | s 168 Examples—references [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2102 | s 169 References to domestic partner and domestic partnership | inert | reason 1: not operative; a heading |  |
| 2103 | s 169 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 169 (1): a reference to a person's domestic partner includes the relationship | `act-tests-ch15.l4` |
| 2104 | s 169 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 169 (2): the relationship between the two people is a domestic partnership | `act-tests-ch15.l4` |
| 2105-2115 | s 169 (2) Example—indicators [example] | encoded | as a case in `act-tests-ch15.l4` | `act-tests-ch15.l4` |
| 2116 | s 169 (3) [subsection] | encoded | `act-ch15-aids.l4`: s 169 (3): a reference to a domestic partnership includes the relationship | `act-tests-ch15.l4` |
| 2118 | s 169A References to transgender people | inert | reason 1: not operative; a heading |  |
| 2119 | s 169A (1) [subsection] | encoded | `act-ch15-aids.l4`: s 169A (1): the person is a transgender person | `act-tests-ch15.l4` |
| 2120 | s 169A (1) (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 169A (1): the person is a transgender person | `act-tests-ch15.l4` |
| 2121-2122 | s 169A (1) (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 169A (1): the person is a transgender person | `act-tests-ch15.l4` |
| 2123 | s 169A (2) [subsection] | encoded | `act-ch15-aids.l4`: s 169A (2): a transgender person includes the person | `act-tests-ch15.l4` |
| 2124 | s 169A (3) [subsection] | encoded | `act-ch15-aids.l4`: s 169A (3): the person is a recognised transgender person | `act-tests-ch15.l4` |
| 2126 | s 169B References to intersex people | inert | reason 1: not operative; a heading |  |
| 2127 | s 169B text [opening words] | encoded | `act-ch15-aids.l4`: s 169B: the person is an intersex person | `act-tests-ch15.l4` |
| 2128 | s 169B (a) [paragraph] | encoded | `act-ch15-aids.l4`: s 169B: the person is an intersex person | `act-tests-ch15.l4` |
| 2129 | s 169B (b) [paragraph] | encoded | `act-ch15-aids.l4`: s 169B: the person is an intersex person | `act-tests-ch15.l4` |
| 2130 | s 169B (c) [paragraph] | encoded | `act-ch15-aids.l4`: s 169B: the person is an intersex person | `act-tests-ch15.l4` |
| 2132 | Part 15.4 Preservation of certain common law privileges | inert | reason 1: not operative; a heading |  |
| 2134 | s 170 Privileges against self-incrimination and exposure to civil penalty | inert | reason 1: not operative; a heading |  |
| 2135 | s 170 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 170 (1): the thing must be interpreted to preserve the common law privileges against self-incrimination and exposure to the imposition of a civil penalty | `act-tests-ch15.l4` |
| 2136 | s 170 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 170 (2): this section affects the operation of the Evidence Act 2011 | `act-tests-ch15.l4` |
| 2137 | s 170 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2138 | s 170 (3) [subsection] | encoded | `act-determinative.l4`: s 170 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 2139 | s 170 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2141 | s 171 Client legal privilege | inert | reason 1: not operative; a heading |  |
| 2142 | s 171 (1) [subsection] | encoded | `act-ch15-aids.l4`: s 171 (1): the thing must be interpreted to preserve the common law privilege in relation to client legal privilege | `act-tests-ch15.l4` |
| 2143 | s 171 (2) [subsection] | encoded | `act-ch15-aids.l4`: s 171 (2): this section affects the operation of the Evidence Act 2011 | `act-tests-ch15.l4` |
| 2144 | s 171 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2145 | s 171 (3) [subsection] | encoded | `act-determinative.l4`: s 171 (3): the section declares itself a determinative provision | `act-tests-determinative.l4` |
| 2146 | s 171 (3) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2148-2183 | Chapter 16 Courts, tribunals and other decision-makers | out of scope | assumed scope choice, not a ruling; Rules for references to courts and tribunals |  |
| 2184-2223 | Chapter 17 Entities and positions | out of scope | assumed scope choice, not a ruling; Rules for references to entities, offices and positions |  |
| 2224-2280 | Chapter 18 Offences | out of scope | assumed scope choice, not a ruling; Rules for offences, penalties and the way they are stated |  |
| 2283 | Part 19.1 Introductory | inert | reason 1: not operative; a heading |  |
| 2285 | s 195 Meaning of law—ch 19 | inert | reason 1: not operative; a heading |  |
| 2286 | s 195 text [opening words] | encoded | `act-ch19-functions-and-service.l4`: s 195: the kind of document is a law for chapter 19 | `act-tests-ch19.l4` |
| 2287 | s 195 law [definition] | encoded | `act-ch19-functions-and-service.l4`: s 195: the kind of document is a law for chapter 19; `act-section-definitions.l4`: s 195, definition of law | `act-tests-ch19.l4`, `act-tests-section-definitions.l4` |
| 2288 | s 195 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2290 | Part 19.2 Functions | inert | reason 1: not operative; a heading |  |
| 2291 | note at line 2291 | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2293 | s 196 Provision giving function gives power to exercise function | inert | reason 1: not operative; a heading |  |
| 2294 | s 196 (1) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 196 (1): the provision also gives the entity the powers necessary and convenient to exercise the function | `act-tests-ch19.l4` |
| 2295 | s 196 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2296 | s 196 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 196 (2): the powers given under subsection (1) are in addition to any other powers of the entity under the law | `act-tests-ch19.l4` |
| 2298 | s 197 Statutory functions may be exercised from time to time | inert | reason 1: not operative; a heading |  |
| 2299 | s 197 text [opening words] | encoded | `act-ch19-functions-and-service.l4`: s 197: the function may be exercised from time to time | `act-tests-ch19.l4` |
| 2300 | s 197 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2302 | s 199 Functions of bodies | inert | reason 1: not operative; a heading |  |
| 2303 | s 199 (1) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (1): the body may exercise the function by resolution | `act-tests-ch19.l4` |
| 2304 | s 199 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2305 | s 199 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (2): subsection (1) applies to the function | `act-tests-ch19.l4` |
| 2306 | s 199 (3) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (3): the signature of the person authorised by the body is taken to be the signature of the body | `act-tests-ch19.l4` |
| 2307 | s 199 (4) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (4): the function may be exercised by the body as constituted for the time being | `act-tests-ch19.l4` |
| 2308-2309 | s 199 (4) Example [example] | encoded | as a case in `act-tests-ch19.l4` | `act-tests-ch19.l4` |
| 2310 | s 199 (5) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (5): the exercise of the function is affected | `act-tests-ch19.l4` |
| 2311 | s 199 (6) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (6): subsections (4) and (5) affect any quorum requirement applying to the body | `act-tests-ch19.l4` |
| 2312-2313 | s 199 (6) Example [example] | encoded | as a case in `act-tests-ch19.l4` | `act-tests-ch19.l4` |
| 2314 | s 199 (7) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (7): the effect of the thing done by the body ends | `act-tests-ch19.l4` |
| 2315 | s 199 (7) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2316 | s 199 (8) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 199 (8): subsection (7) prevents the thing done by the body being ended or changed by the body as subsequently constituted | `act-tests-ch19.l4` |
| 2318 | s 200 Functions of occupants of positions | inert | reason 1: not operative; a heading |  |
| 2319 | s 200 (1) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 200 (1): the function may be exercised by the person for the time being occupying the position | `act-tests-ch19.l4` |
| 2320 | s 200 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2321 | s 200 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 200 (2): the thing done by the person ends | `act-tests-ch19.l4` |
| 2322 | s 200 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2323 | s 200 (3) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 200 (3): subsection (2) prevents the thing done by the person being ended or changed by any person subsequently occupying the position | `act-tests-ch19.l4` |
| 2325-2507 | Part 19.3 Appointments (Divisions 19.3.1 to 19.3.3) | out of scope | assumed scope choice, not a ruling; The making of appointments and acting appointments |  |
| 2508-2586 | Part 19.4 Delegations | out of scope | assumed scope choice, not a ruling; Delegation of functions |  |
| 2587 | Part 19.5 Service of documents | inert | reason 1: not operative; a heading |  |
| 2589 | s 245 Application—pt 19.5 | inert | reason 1: not operative; a heading |  |
| 2590 | s 245 text [opening words] | encoded | `act-ch19-functions-and-service.l4`: s 245: this part applies to the document | `act-tests-ch19.l4` |
| 2592 | s 246 Definitions—pt 19.5 | inert | reason 1: not operative; a heading |  |
| 2593 | s 246 text [opening words] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 2594 | s 246 administrator, of a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of administrator, of a law | `act-tests-section-definitions.l4` |
| 2595-2599 | s 246 agency [definition] | encoded | `act-ch19-functions-and-service.l4`: s 246: the entity is an agency; `act-section-definitions.l4`: s 246, definition of agency | `act-tests-ch19.l4`, `act-tests-section-definitions.l4` |
| 2600 | s 246 business address, of an individual, corporation or agency in relation to anything done or to be done under a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of business address, of an individual, corporation or agency in relation to anythin | `act-tests-section-definitions.l4` |
| 2601 | s 246 corporation does not include an agency. [definition] | encoded | `act-ch19-functions-and-service.l4`: s 246: the entity is a corporation for this part; `act-section-definitions.l4`: s 246, definition of corporation does not include an agency. | `act-tests-ch19.l4`, `act-tests-section-definitions.l4` |
| 2602 | s 246 document [definition] | encoded | `act-ch19-functions-and-service.l4`: s 246: the thing is a document; `act-section-definitions.l4`: s 246, definition of document | `act-tests-ch19.l4`, `act-tests-section-definitions.l4` |
| 2603 | s 246 email address, of an individual, corporation or agency in relation to anything done or to be done under a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of email address, of an individual, corporation or agency in relation to anything d | `act-tests-section-definitions.l4` |
| 2604-2610 | s 246 executive officer [definition] | encoded | `act-ch19-functions-and-service.l4`: s 246: the person is an executive officer of the entity; `act-section-definitions.l4`: s 246, definition of executive officer | `act-tests-ch19.l4`, `act-tests-section-definitions.l4` |
| 2611 | s 246 fax number, of an individual, corporation or agency in relation to anything done or to be done under a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of fax number, of an individual, corporation or agency in relation to anything done | `act-tests-section-definitions.l4` |
| 2612 | s 246 home address, of an individual in relation to anything done or to be done under a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of home address, of an individual in relation to anything done or to be done under  | `act-tests-section-definitions.l4` |
| 2613 | s 246 responsible, for a law [definition] | encoded | `act-section-definitions.l4`: s 246, definition of responsible, for a law | `act-tests-section-definitions.l4` |
| 2615 | s 247 Service of documents on individuals | inert | reason 1: not operative; a heading |  |
| 2616 | s 247 (1) [subsection] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2617 | s 247 (1) (a) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2618 | s 247 (1) (b) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2619 | s 247 (1) (c) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2620 | s 247 (1) (d) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2621 | s 247 (1) (e) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 247 (1): the document may be served on an individual in this way | `act-tests-ch19.l4` |
| 2622 | s 247 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2623 | s 247 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 247 (2): the section applies to the service in the same way as it applies to service in the ACT | `act-tests-ch19.l4` |
| 2625 | s 248 Service of documents on corporations | inert | reason 1: not operative; a heading |  |
| 2626 | s 248 (1) [subsection] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2627 | s 248 (1) (a) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2628 | s 248 (1) (b) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2629 | s 248 (1) (c) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2630 | s 248 (1) (d) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2631 | s 248 (1) (e) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 248 (1): the document may be served on a corporation in this way | `act-tests-ch19.l4` |
| 2632 | s 248 (1) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2633 | s 248 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 248 (2): the section applies to the service in the same way as it applies to service in the ACT | `act-tests-ch19.l4` |
| 2635 | s 249 Service of documents on agencies | inert | reason 1: not operative; a heading |  |
| 2636 | s 249 text [opening words] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2637 | s 249 (a) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2638 | s 249 (b) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2639 | s 249 (c) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2640 | s 249 (d) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2641 | s 249 (e) [paragraph] | fork | F14 (see the fork register); `act-ch19-functions-and-service.l4`: s 249: the document may be served on an agency in this way | `act-tests-ch19.l4` |
| 2642 | s 249 Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2644 | s 250 When document taken to be served | inert | reason 1: not operative; a heading |  |
| 2645 | s 250 (1) [subsection] | encoded | `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2646 | s 250 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 250 (2): subsection (1) affects the operation of the Evidence Act 2011, section 160 (Postal articles); `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-ch19.l4`, `act-tests-time.l4` |
| 2647 | s 250 (2) Note [note] | inert | reason 1: not operative; a note is not part of the Act (s 127 (1), encoded in act-ch13-structure.l4) |  |
| 2648 | s 250 (3) [subsection] | fork | F15 (see the fork register); `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2649 | s 250 (4) [subsection] | encoded | `act-interpretation-time.l4`: s 250 (4): the sender has reason to suspect the document was not received; `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2650 | s 250 (4) (a) [paragraph] | encoded | `act-interpretation-time.l4`: s 250 (4): the sender has reason to suspect the document was not received; `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2651 | s 250 (4) (b) [paragraph] | encoded | `act-interpretation-time.l4`: s 250 (4): the sender has reason to suspect the document was not received; `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2652 | s 250 (4) (c) [paragraph] | encoded | `act-interpretation-time.l4`: s 250 (4): the sender has reason to suspect the document was not received; `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2653 | s 250 (5) [subsection] | encoded | `act-interpretation-time.l4`: s 250: the day a document is taken to be served | `act-tests-time.l4` |
| 2654 | s 250 (6) [subsection] | encoded | the scope of each definition below is its `applies to` field, in `act-section-definitions.l4` | `act-tests-section-definitions.l4` |
| 2655 | s 250 (6) recipient, for a document [definition] | encoded | `act-section-definitions.l4`: s 250 (6), definition of recipient, for a document | `act-tests-section-definitions.l4` |
| 2656 | s 250 (6) sender, for a document served, or to be served, by fax or email [definition] | encoded | `act-section-definitions.l4`: s 250 (6), definition of sender, for a document served, or to be served, by fax or email | `act-tests-section-definitions.l4` |
| 2658 | s 251 Other laws not affected etc | inert | reason 1: not operative; a heading |  |
| 2659 | s 251 (1) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 251 (1): this part affects the operation of any other law that authorises or requires service of a document otherwise than as provided under this part | `act-tests-ch19.l4` |
| 2660 | s 251 (2) [subsection] | encoded | `act-ch19-functions-and-service.l4`: s 251 (2) (a): a law may provide that a document of a particular kind may or must be served only in a particular way or to a particular address or number | `act-tests-ch19.l4` |
| 2661 | s 251 (2) (a) [paragraph] | encoded | `act-ch19-functions-and-service.l4`: s 251 (2) (a): a law may provide that a document of a particular kind may or must be served only in a particular way or to a particular address or number | `act-tests-ch19.l4` |
| 2662 | s 251 (2) (b) [paragraph] | encoded | `act-ch19-functions-and-service.l4`: s 251 (2) (b): a law may provide for the date, or date and time, when service of a document is taken to have been made | `act-tests-ch19.l4` |
| 2664 | s 252 Powers of courts and tribunals not affected | inert | reason 1: not operative; a heading |  |
| 2665 | s 252 text [opening words] | encoded | `act-ch19-functions-and-service.l4`: s 252: this part affects the power of a court or tribunal to authorise or require service of a document otherwise than as provided under this part | `act-tests-ch19.l4` |
| 2667-2688 | Part 19.6 Functions of Executive and Ministers | out of scope | assumed scope choice, not a ruling; Functions of the Executive and of Ministers |  |
| 2689-2743 | Part 19.7 Other matters | out of scope | assumed scope choice, not a ruling; Miscellaneous administrative rules |  |
| 2744-2760 | Chapter 20 Miscellaneous | out of scope | assumed scope choice, not a ruling; Miscellaneous provisions |  |
| 2761-2800 | Schedule 1 Acts included in sources of law in the ACT (Parts 1.1, 1.2) | out of scope | assumed scope choice, not a ruling; A list of former New South Wales and United Kingdom Acts |  |
| 2801 | Dictionary Dictionary | inert | reason 1: not operative; a heading |  |
| 2801-3348 | Dictionary Parts 1 and 2: every entry that no in-scope provision uses and that is not about time, commencement, laws, instruments or the Territory (183 entries) | out of scope | assumed scope choice, not a ruling; no in-scope provision uses these terms |  |
| 2804 | Dictionary part 1 Meaning of commonly-used terms | inert | reason 1: not operative; a heading |  |
| 2808-2811 | dictionary pt 1: Act | encoded | `act-dictionary.l4`: dictionary pt 1: Act | `act-tests-dictionary.l4` |
| 2812 | dictionary pt 1: ACT | encoded | `act-dictionary.l4`: dictionary pt 1: ACT | `act-tests-dictionary.l4` |
| 2814 | dictionary pt 1: administrative unit | encoded | `act-dictionary.l4`: dictionary pt 1: administrative unit | `act-tests-dictionary.l4` |
| 2815 | dictionary pt 1: adult | encoded | `act-dictionary.l4`: dictionary pt 1: adult | `act-tests-dictionary.l4` |
| 2817-2821 | dictionary pt 1: amend | encoded | `act-dictionary.l4`: dictionary pt 1: amend | `act-tests-dictionary.l4` |
| 2823 | dictionary pt 1: AS | encoded | `act-dictionary.l4`: dictionary pt 1: AS | `act-tests-dictionary.l4` |
| 2824 | dictionary pt 1: AS/NZS | encoded | `act-dictionary.l4`: dictionary pt 1: AS/NZS | `act-tests-dictionary.l4` |
| 2826 | dictionary pt 1: Attorney-General | encoded | `act-dictionary.l4`: dictionary pt 1: Attorney-General | `act-tests-dictionary.l4` |
| 2828 | dictionary pt 1: Australia | encoded | `act-dictionary.l4`: dictionary pt 1: Australia | `act-tests-dictionary.l4` |
| 2829 | dictionary pt 1: Australian citizen | encoded | `act-dictionary.l4`: dictionary pt 1: Australian citizen | `act-tests-dictionary.l4` |
| 2835 | dictionary pt 1: Australian/New Zealand Standard | encoded | `act-dictionary.l4`: dictionary pt 1: Australian/New Zealand Standard | `act-tests-dictionary.l4` |
| 2836 | dictionary pt 1: Australian Standard | encoded | `act-dictionary.l4`: dictionary pt 1: Australian Standard | `act-tests-dictionary.l4` |
| 2838 | dictionary pt 1: authorised deposit-taking institution | encoded | `act-dictionary.l4`: dictionary pt 1: authorised deposit-taking institution | `act-tests-dictionary.l4` |
| 2839-2841 | dictionary pt 1: bank | encoded | `act-dictionary.l4`: dictionary pt 1: bank | `act-tests-dictionary.l4` |
| 2842 | dictionary pt 1: bank holiday | encoded | `act-dictionary.l4`: dictionary pt 1: bank holiday | `act-tests-dictionary.l4` |
| 2852-2859 | dictionary pt 1: body | encoded | `act-dictionary.l4`: dictionary pt 1: body | `act-tests-dictionary.l4` |
| 2866-2868 | dictionary pt 1: business day | encoded | `act-dictionary.l4`: dictionary pt 1: business day; `act-interpretation-time.l4`: dictionary, business day: the day is a business day | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 2869-2870 | dictionary pt 1: by regulation | encoded | `act-dictionary.l4`: dictionary pt 1: by regulation | `act-tests-dictionary.l4` |
| 2871 | dictionary pt 1: calendar month | encoded | `act-dictionary.l4`: dictionary pt 1: calendar month | `act-tests-dictionary.l4` |
| 2872 | dictionary pt 1: calendar year | fork | F10 (see the fork register); `act-dictionary.l4`: dictionary pt 1: calendar year; `act-interpretation-time.l4`: dictionary, calendar year and year: the last day of a run of calendar years beginning at the start of a day; `act-interpretation-time.l4`: dictionary, year, other reading: the last day of N years counted as 12 months each from any starting day | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 2874 | dictionary pt 1: change | encoded | `act-dictionary.l4`: dictionary pt 1: change | `act-tests-dictionary.l4` |
| 2878-2879 | dictionary pt 1: Chief Minister | encoded | `act-dictionary.l4`: dictionary pt 1: Chief Minister | `act-tests-dictionary.l4` |
| 2887 | dictionary pt 1: child, if age rather than descendancy is relevant | encoded | `act-dictionary.l4`: dictionary pt 1: child, if age rather than descendancy is relevant | `act-tests-dictionary.l4` |
| 2893 | dictionary pt 1: civil partner | encoded | `act-dictionary.l4`: dictionary pt 1: civil partner | `act-tests-dictionary.l4` |
| 2894 | dictionary pt 1: civil partnership | encoded | `act-dictionary.l4`: dictionary pt 1: civil partnership | `act-tests-dictionary.l4` |
| 2895 | dictionary pt 1: civil union | encoded | `act-dictionary.l4`: dictionary pt 1: civil union | `act-tests-dictionary.l4` |
| 2896 | dictionary pt 1: civil union partner | encoded | `act-dictionary.l4`: dictionary pt 1: civil union partner | `act-tests-dictionary.l4` |
| 2899 | dictionary pt 1: commencement, of an Act or statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: commencement, of an Act or statutory instrument | `act-tests-dictionary.l4` |
| 2900 | dictionary pt 1: commencement notice | encoded | `act-dictionary.l4`: dictionary pt 1: commencement notice | `act-tests-dictionary.l4` |
| 2908 | dictionary pt 1: Commonwealth | encoded | `act-dictionary.l4`: dictionary pt 1: Commonwealth | `act-tests-dictionary.l4` |
| 2909 | dictionary pt 1: Commonwealth country | encoded | `act-dictionary.l4`: dictionary pt 1: Commonwealth country | `act-tests-dictionary.l4` |
| 2912-2913 | dictionary pt 1: Commonwealth gazette | encoded | `act-dictionary.l4`: dictionary pt 1: Commonwealth gazette | `act-tests-dictionary.l4` |
| 2918 | dictionary pt 1: converted ordinance | encoded | `act-dictionary.l4`: dictionary pt 1: converted ordinance | `act-tests-dictionary.l4` |
| 2923 | dictionary pt 1: corporation | encoded | `act-dictionary.l4`: dictionary pt 1: corporation | `act-tests-dictionary.l4` |
| 2933 | dictionary pt 1: daylight | encoded | `act-dictionary.l4`: dictionary pt 1: daylight | `act-tests-dictionary.l4` |
| 2934 | dictionary pt 1: definition | encoded | `act-dictionary.l4`: dictionary pt 1: definition | `act-tests-dictionary.l4` |
| 2944 | dictionary pt 1: director-general | encoded | `act-dictionary.l4`: dictionary pt 1: director-general | `act-tests-dictionary.l4` |
| 2947 | dictionary pt 1: disallowable instrument | encoded | `act-dictionary.l4`: dictionary pt 1: disallowable instrument | `act-tests-dictionary.l4` |
| 2952-2956 | dictionary pt 1: document | encoded | `act-dictionary.l4`: dictionary pt 1: document | `act-tests-dictionary.l4` |
| 2957 | dictionary pt 1: domestic partner | encoded | `act-dictionary.l4`: dictionary pt 1: domestic partner | `act-tests-dictionary.l4` |
| 2958 | dictionary pt 1: domestic partnership | encoded | `act-dictionary.l4`: dictionary pt 1: domestic partnership | `act-tests-dictionary.l4` |
| 2966 | dictionary pt 1: enactment, of an Act | encoded | `act-dictionary.l4`: dictionary pt 1: enactment, of an Act | `act-tests-dictionary.l4` |
| 2972 | dictionary pt 1: entity | encoded | `act-dictionary.l4`: dictionary pt 1: entity | `act-tests-dictionary.l4` |
| 2976-2977 | dictionary pt 1: Executive | encoded | `act-dictionary.l4`: dictionary pt 1: Executive | `act-tests-dictionary.l4` |
| 2978 | dictionary pt 1: exercise a function | encoded | `act-dictionary.l4`: dictionary pt 1: exercise a function | `act-tests-dictionary.l4` |
| 2979 | dictionary pt 1: expire | encoded | `act-dictionary.l4`: dictionary pt 1: expire | `act-tests-dictionary.l4` |
| 2980 | dictionary pt 1: external territory | encoded | `act-dictionary.l4`: dictionary pt 1: external territory | `act-tests-dictionary.l4` |
| 2984 | dictionary pt 1: financial year | encoded | `act-dictionary.l4`: dictionary pt 1: financial year; `act-interpretation-time.l4`: s 89 (2): the day an appropriation Act is automatically repealed | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 2986-2987 | dictionary pt 1: for, in relation to an Act or statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: for, in relation to an Act or statutory instrument | `act-tests-dictionary.l4` |
| 2988 | dictionary pt 1: foreign country | encoded | `act-dictionary.l4`: dictionary pt 1: foreign country | `act-tests-dictionary.l4` |
| 2989-2991 | dictionary pt 1: former NSW Act | encoded | `act-dictionary.l4`: dictionary pt 1: former NSW Act | `act-tests-dictionary.l4` |
| 2992-2993 | dictionary pt 1: former UK Act | encoded | `act-dictionary.l4`: dictionary pt 1: former UK Act | `act-tests-dictionary.l4` |
| 2997 | dictionary pt 1: function | encoded | `act-dictionary.l4`: dictionary pt 1: function | `act-tests-dictionary.l4` |
| 2999-3001 | dictionary pt 1: gazette | encoded | `act-dictionary.l4`: dictionary pt 1: gazette | `act-tests-dictionary.l4` |
| 3002 | dictionary pt 1: give, in relation to a function | encoded | `act-dictionary.l4`: dictionary pt 1: give, in relation to a function | `act-tests-dictionary.l4` |
| 3005-3007 | dictionary pt 1: Governor | encoded | `act-dictionary.l4`: dictionary pt 1: Governor | `act-tests-dictionary.l4` |
| 3008 | dictionary pt 1: Governor-General | encoded | `act-dictionary.l4`: dictionary pt 1: Governor-General | `act-tests-dictionary.l4` |
| 3019 | dictionary pt 1: home address, for an individual | encoded | `act-dictionary.l4`: dictionary pt 1: home address, for an individual | `act-tests-dictionary.l4` |
| 3023 | dictionary pt 1: Imperial Act | encoded | `act-dictionary.l4`: dictionary pt 1: Imperial Act | `act-tests-dictionary.l4` |
| 3027 | dictionary pt 1: individual | encoded | `act-dictionary.l4`: dictionary pt 1: individual | `act-tests-dictionary.l4` |
| 3031-3038 | dictionary pt 1: in relation to | encoded | `act-dictionary.l4`: dictionary pt 1: in relation to | `act-tests-dictionary.l4` |
| 3039 | dictionary pt 1: instrument | encoded | `act-dictionary.l4`: dictionary pt 1: instrument | `act-tests-dictionary.l4` |
| 3040-3042 | dictionary pt 1: interest, in relation to land or other property | encoded | `act-dictionary.l4`: dictionary pt 1: interest, in relation to land or other property | `act-tests-dictionary.l4` |
| 3045 | dictionary pt 1: internal territory | encoded | `act-dictionary.l4`: dictionary pt 1: internal territory | `act-tests-dictionary.l4` |
| 3046 | dictionary pt 1: intersex person | encoded | `act-dictionary.l4`: dictionary pt 1: intersex person | `act-tests-dictionary.l4` |
| 3047-3048 | dictionary pt 1: Jervis Bay Territory | encoded | `act-dictionary.l4`: dictionary pt 1: Jervis Bay Territory | `act-tests-dictionary.l4` |
| 3051-3052 | dictionary pt 1: land | encoded | `act-dictionary.l4`: dictionary pt 1: land | `act-tests-dictionary.l4` |
| 3054-3058 | dictionary pt 1: law, of the Territory | encoded | `act-dictionary.l4`: dictionary pt 1: law, of the Territory | `act-tests-dictionary.l4` |
| 3062 | dictionary pt 1: Legislation Act | encoded | `act-dictionary.l4`: dictionary pt 1: Legislation Act | `act-tests-dictionary.l4` |
| 3063-3064 | dictionary pt 1: Legislative Assembly | encoded | `act-dictionary.l4`: dictionary pt 1: Legislative Assembly | `act-tests-dictionary.l4` |
| 3065 | dictionary pt 1: legislative instrument | encoded | `act-dictionary.l4`: dictionary pt 1: legislative instrument | `act-tests-dictionary.l4` |
| 3066 | dictionary pt 1: liability | encoded | `act-dictionary.l4`: dictionary pt 1: liability | `act-tests-dictionary.l4` |
| 3069 | dictionary pt 1: make an instrument | encoded | `act-dictionary.l4`: dictionary pt 1: make an instrument | `act-tests-dictionary.l4` |
| 3070 | dictionary pt 1: making, of a statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: making, of a statutory instrument | `act-tests-dictionary.l4` |
| 3071 | dictionary pt 1: may | encoded | `act-dictionary.l4`: dictionary pt 1: may | `act-tests-dictionary.l4` |
| 3073 | dictionary pt 1: midnight, in relation to a particular day | encoded | `act-dictionary.l4`: dictionary pt 1: midnight, in relation to a particular day; `act-interpretation-time.l4`: s 74 and dictionary, midnight: the number of minutes from the start of the day to a time of day | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 3077 | dictionary pt 1: Minister | encoded | `act-dictionary.l4`: dictionary pt 1: Minister | `act-tests-dictionary.l4` |
| 3078 | dictionary pt 1: modification | encoded | `act-dictionary.l4`: dictionary pt 1: modification | `act-tests-dictionary.l4` |
| 3079-3084 | dictionary pt 1: month | fork | F9 (see the fork register); `act-dictionary.l4`: dictionary pt 1: month; `act-interpretation-time.l4`: dictionary, month: the last day of the month that begins at the start of a day; `act-interpretation-time.l4`: dictionary, month: the last day of a run of successive months, the first beginning at the start of a day; and 5 more | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 3085 | dictionary pt 1: must | encoded | `act-dictionary.l4`: dictionary pt 1: must | `act-tests-dictionary.l4` |
| 3086-3089 | dictionary pt 1: name | encoded | `act-dictionary.l4`: dictionary pt 1: name | `act-tests-dictionary.l4` |
| 3101 | dictionary pt 1: night | encoded | `act-dictionary.l4`: dictionary pt 1: night | `act-tests-dictionary.l4` |
| 3102 | dictionary pt 1: Northern Territory | encoded | `act-dictionary.l4`: dictionary pt 1: Northern Territory | `act-tests-dictionary.l4` |
| 3103 | dictionary pt 1: notifiable instrument | encoded | `act-dictionary.l4`: dictionary pt 1: notifiable instrument | `act-tests-dictionary.l4` |
| 3104-3106 | dictionary pt 1: notification | encoded | `act-dictionary.l4`: dictionary pt 1: notification | `act-tests-dictionary.l4` |
| 3107 | dictionary pt 1: notification day, for an Act or statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: notification day, for an Act or statutory instrument | `act-tests-dictionary.l4` |
| 3108 | dictionary pt 1: NSW Act | encoded | `act-dictionary.l4`: dictionary pt 1: NSW Act | `act-tests-dictionary.l4` |
| 3110-3112 | dictionary pt 1: number | encoded | `act-dictionary.l4`: dictionary pt 1: number | `act-tests-dictionary.l4` |
| 3125 | dictionary pt 1: office | encoded | `act-dictionary.l4`: dictionary pt 1: office | `act-tests-dictionary.l4` |
| 3135 | dictionary pt 1: omit, in relation to a provision of an Act or statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: omit, in relation to a provision of an Act or statutory instrument | `act-tests-dictionary.l4` |
| 3139 | dictionary pt 1: ordinance | encoded | `act-dictionary.l4`: dictionary pt 1: ordinance | `act-tests-dictionary.l4` |
| 3145 | dictionary pt 1: parliamentary counsel | encoded | `act-dictionary.l4`: dictionary pt 1: parliamentary counsel | `act-tests-dictionary.l4` |
| 3146 | dictionary pt 1: passing, of an Act | encoded | `act-dictionary.l4`: dictionary pt 1: passing, of an Act | `act-tests-dictionary.l4` |
| 3147 | dictionary pt 1: penalty unit | encoded | `act-dictionary.l4`: dictionary pt 1: penalty unit | `act-tests-dictionary.l4` |
| 3148 | dictionary pt 1: person | encoded | `act-dictionary.l4`: dictionary pt 1: person | `act-tests-dictionary.l4` |
| 3153 | dictionary pt 1: position | encoded | `act-dictionary.l4`: dictionary pt 1: position | `act-tests-dictionary.l4` |
| 3154 | dictionary pt 1: power | encoded | `act-dictionary.l4`: dictionary pt 1: power | `act-tests-dictionary.l4` |
| 3155 | dictionary pt 1: prescribed, in an Act | encoded | `act-dictionary.l4`: dictionary pt 1: prescribed, in an Act | `act-tests-dictionary.l4` |
| 3157 | dictionary pt 1: proceeding | encoded | `act-dictionary.l4`: dictionary pt 1: proceeding | `act-tests-dictionary.l4` |
| 3158-3159 | dictionary pt 1: property | encoded | `act-dictionary.l4`: dictionary pt 1: property | `act-tests-dictionary.l4` |
| 3160 | dictionary pt 1: provision, of an Act or instrument | encoded | `act-dictionary.l4`: dictionary pt 1: provision, of an Act or instrument | `act-tests-dictionary.l4` |
| 3167 | dictionary pt 1: public holiday | encoded | `act-dictionary.l4`: dictionary pt 1: public holiday | `act-tests-dictionary.l4` |
| 3168 | dictionary pt 1: public money, of the Territory | encoded | `act-dictionary.l4`: dictionary pt 1: public money, of the Territory | `act-tests-dictionary.l4` |
| 3169-3171 | dictionary pt 1: public notice, if required by a Territory law | encoded | `act-dictionary.l4`: dictionary pt 1: public notice, if required by a Territory law | `act-tests-dictionary.l4` |
| 3181 | dictionary pt 1: quarter | encoded | `act-dictionary.l4`: dictionary pt 1: quarter | `act-tests-dictionary.l4` |
| 3183 | dictionary pt 1: recognised transgender person | encoded | `act-dictionary.l4`: dictionary pt 1: recognised transgender person | `act-tests-dictionary.l4` |
| 3191 | dictionary pt 1: regulation, in relation to an Act | encoded | `act-dictionary.l4`: dictionary pt 1: regulation, in relation to an Act | `act-tests-dictionary.l4` |
| 3193-3199 | dictionary pt 1: repeal | encoded | `act-dictionary.l4`: dictionary pt 1: repeal | `act-tests-dictionary.l4` |
| 3201 | dictionary pt 1: retrospectively, for the commencement of legislation | encoded | `act-dictionary.l4`: dictionary pt 1: retrospectively, for the commencement of legislation | `act-tests-dictionary.l4` |
| 3206-3208 | dictionary pt 1: rules | encoded | `act-dictionary.l4`: dictionary pt 1: rules | `act-tests-dictionary.l4` |
| 3210 | dictionary pt 1: Self-Government Act | encoded | `act-dictionary.l4`: dictionary pt 1: Self-Government Act | `act-tests-dictionary.l4` |
| 3211-3212 | dictionary pt 1: self-government day | encoded | `act-dictionary.l4`: dictionary pt 1: self-government day | `act-tests-dictionary.l4` |
| 3216 | dictionary pt 1: signpost definition | encoded | `act-dictionary.l4`: dictionary pt 1: signpost definition | `act-tests-dictionary.l4` |
| 3217-3218 | dictionary pt 1: sitting day, of the Legislative Assembly | encoded | `act-dictionary.l4`: dictionary pt 1: sitting day, of the Legislative Assembly | `act-tests-dictionary.l4` |
| 3221-3222 | dictionary pt 1: Speaker | encoded | `act-dictionary.l4`: dictionary pt 1: Speaker | `act-tests-dictionary.l4` |
| 3224 | dictionary pt 1: State | encoded | `act-dictionary.l4`: dictionary pt 1: State | `act-tests-dictionary.l4` |
| 3226 | dictionary pt 1: statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: statutory instrument | `act-tests-dictionary.l4` |
| 3227 | dictionary pt 1: statutory office-holder | encoded | `act-dictionary.l4`: dictionary pt 1: statutory office-holder | `act-tests-dictionary.l4` |
| 3228 | dictionary pt 1: subordinate law | encoded | `act-dictionary.l4`: dictionary pt 1: subordinate law | `act-tests-dictionary.l4` |
| 3236 | dictionary pt 1: territory authority | encoded | `act-dictionary.l4`: dictionary pt 1: territory authority | `act-tests-dictionary.l4` |
| 3237-3238 | dictionary pt 1: territory instrumentality | encoded | `act-dictionary.l4`: dictionary pt 1: territory instrumentality | `act-tests-dictionary.l4` |
| 3239-3240 | dictionary pt 1: territory land | encoded | `act-dictionary.l4`: dictionary pt 1: territory land | `act-tests-dictionary.l4` |
| 3241 | dictionary pt 1: territory law | encoded | `act-dictionary.l4`: dictionary pt 1: territory law | `act-tests-dictionary.l4` |
| 3242-3248 | dictionary pt 1: territory lease | encoded | `act-dictionary.l4`: dictionary pt 1: territory lease | `act-tests-dictionary.l4` |
| 3249 | dictionary pt 1: territory-owned corporation | encoded | `act-dictionary.l4`: dictionary pt 1: territory-owned corporation | `act-tests-dictionary.l4` |
| 3250 | dictionary pt 1: territory plan | encoded | `act-dictionary.l4`: dictionary pt 1: territory plan | `act-tests-dictionary.l4` |
| 3251 | dictionary pt 1: territory planning authority | encoded | `act-dictionary.l4`: dictionary pt 1: territory planning authority | `act-tests-dictionary.l4` |
| 3252-3254 | dictionary pt 1: the Territory | encoded | `act-dictionary.l4`: dictionary pt 1: the Territory | `act-tests-dictionary.l4` |
| 3255 | dictionary pt 1: transgender person | encoded | `act-dictionary.l4`: dictionary pt 1: transgender person | `act-tests-dictionary.l4` |
| 3256 | dictionary pt 1: transitional | encoded | `act-dictionary.l4`: dictionary pt 1: transitional | `act-tests-dictionary.l4` |
| 3257 | dictionary pt 1: Treasurer | encoded | `act-dictionary.l4`: dictionary pt 1: Treasurer | `act-tests-dictionary.l4` |
| 3258 | dictionary pt 1: tribunal | encoded | `act-dictionary.l4`: dictionary pt 1: tribunal | `act-tests-dictionary.l4` |
| 3259 | dictionary pt 1: UK Act | encoded | `act-dictionary.l4`: dictionary pt 1: UK Act | `act-tests-dictionary.l4` |
| 3260-3268 | dictionary pt 1: under, in relation to an Act or statutory instrument | encoded | `act-dictionary.l4`: dictionary pt 1: under, in relation to an Act or statutory instrument | `act-tests-dictionary.l4` |
| 3269 | dictionary pt 1: United Kingdom | encoded | `act-dictionary.l4`: dictionary pt 1: United Kingdom | `act-tests-dictionary.l4` |
| 3270-3274 | dictionary pt 1: United Kingdom Parliament | encoded | `act-dictionary.l4`: dictionary pt 1: United Kingdom Parliament | `act-tests-dictionary.l4` |
| 3278 | dictionary pt 1: word | encoded | `act-dictionary.l4`: dictionary pt 1: word | `act-tests-dictionary.l4` |
| 3280-3282 | dictionary pt 1: working day | encoded | `act-dictionary.l4`: dictionary pt 1: working day; `act-interpretation-time.l4`: dictionary, working day: the day is a working day; `act-interpretation-time.l4`: dictionary, working day: the first working day after a day, searching a limited number of days | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 3283-3285 | dictionary pt 1: writing | encoded | `act-dictionary.l4`: dictionary pt 1: writing | `act-tests-dictionary.l4` |
| 3286 | dictionary pt 1: year, without specifying the kind of year | fork | F10 (see the fork register); `act-dictionary.l4`: dictionary pt 1: year, without specifying the kind of year; `act-interpretation-time.l4`: dictionary, calendar year and year: the last day of a run of calendar years beginning at the start of a day | `act-tests-dictionary.l4`, `act-tests-time.l4` |
| 3288 | Dictionary part 2 Terms for Legislation Act 2001 only | inert | reason 1: not operative; a heading |  |
| 3290-3291 | dictionary pt 2: Act, for chapter 14 (Interpretation of Acts and statutory instruments) | encoded | `act-dictionary.l4`: dictionary pt 2: Act, for chapter 14 (Interpretation of Acts and statutory instruments) | `act-tests-dictionary.l4` |
| 3292-3294 | dictionary pt 2: ACT law | encoded | `act-dictionary.l4`: dictionary pt 2: ACT law | `act-tests-dictionary.l4` |
| 3295 | dictionary pt 2: administrator, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: administrator, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3296 | dictionary pt 2: agency, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: agency, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3297 | dictionary pt 2: amend, for chapter 9 (Repeal and amendment of laws) | encoded | `act-dictionary.l4`: dictionary pt 2: amend, for chapter 9 (Repeal and amendment of laws) | `act-tests-dictionary.l4` |
| 3298 | dictionary pt 2: another jurisdiction | encoded | `act-ch10-referring-to-laws.l4`: Jurisdiction of a document; `act-ch10-referring-to-laws.l4`: dictionary: the jurisdiction is another jurisdiction; `act-dictionary.l4`: dictionary pt 2: another jurisdiction | `act-tests-ch10.l4`, `act-tests-dictionary.l4` |
| 3307 | dictionary pt 2: authorised republication | encoded | `act-dictionary.l4`: dictionary pt 2: authorised republication | `act-tests-dictionary.l4` |
| 3310 | dictionary pt 2: business address, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: business address, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3311 | dictionary pt 2: corporation, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: corporation, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3313 | dictionary pt 2: current legislative drafting practice | encoded | `act-dictionary.l4`: dictionary pt 2: current legislative drafting practice | `act-tests-dictionary.l4` |
| 3315 | dictionary pt 2: determinative provision | encoded | `act-dictionary.l4`: dictionary pt 2: determinative provision | `act-tests-dictionary.l4` |
| 3316-3317 | dictionary pt 2: document, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: document, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3319 | dictionary pt 2: email address, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: email address, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3320 | dictionary pt 2: executive officer, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: executive officer, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3321 | dictionary pt 2: fax number, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: fax number, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3323 | dictionary pt 2: home address, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: home address, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3324-3333 | dictionary pt 2: law | encoded | `act-dictionary.l4`: dictionary pt 2: law | `act-tests-dictionary.l4` |
| 3334 | dictionary pt 2: law of another jurisdiction, for chapter 10 (Referring to laws) | encoded | `act-dictionary.l4`: dictionary pt 2: law of another jurisdiction, for chapter 10 (Referring to laws) | `act-tests-dictionary.l4` |
| 3336 | dictionary pt 2: non-determinative provision | encoded | `act-dictionary.l4`: dictionary pt 2: non-determinative provision | `act-tests-dictionary.l4` |
| 3338 | dictionary pt 2: register | encoded | `act-dictionary.l4`: dictionary pt 2: register | `act-tests-dictionary.l4` |
| 3339 | dictionary pt 2: repeal, for chapter 9 (Repeal and amendment of laws) | encoded | `act-dictionary.l4`: dictionary pt 2: repeal, for chapter 9 (Repeal and amendment of laws) | `act-tests-dictionary.l4` |
| 3340-3342 | dictionary pt 2: republication | encoded | `act-dictionary.l4`: dictionary pt 2: republication | `act-tests-dictionary.l4` |
| 3343 | dictionary pt 2: republication date, for an authorised republication | encoded | `act-dictionary.l4`: dictionary pt 2: republication date, for an authorised republication | `act-tests-dictionary.l4` |
| 3344 | dictionary pt 2: responsible, for part 19.5 (Service of documents) | encoded | `act-dictionary.l4`: dictionary pt 2: responsible, for part 19.5 (Service of documents) | `act-tests-dictionary.l4` |
| 3347 | dictionary pt 2: working out the meaning of an Act, for part 14.2 (Key principles of interpretation) | encoded | `act-dictionary.l4`: dictionary pt 2: working out the meaning of an Act, for part 14.2 (Key principles of interpretation) | `act-tests-dictionary.l4` |
| 3349-5536 | Endnotes | out of scope | assumed scope choice, not a ruling; The history of the Act, not rules |  |

## Fork register

A fork is a place where the text can be read two ways with different outcomes.
Each entry gives the rule that encodes the reading taken, the reading taken, the other reading, and the text that licenses each.
The rows of the coverage table that a fork touches say `fork` and name it.

### F1: A contrary intention that is not manifest, against a determinative provision

- Rule: `act-ch1-preliminary.l4`: `s 6: the provision of this Act is displaced by the other provision`
- Reading taken: For a determinative provision, an express displacement or a manifest contrary intention displaces it; a contrary intention that is not manifest answers NOTHING.
- Other reading: JUST FALSE: the provision is not displaced.
- Text: s 6 (2) "A determinative provision may be displaced expressly or by a manifest contrary intention" grants a way to displace and does not say that other ways fail; s 6 (4) asks for "a more deliberate displacement" of a determinative provision.

### F2: What a "later" or "earlier" date of commencement is later or earlier than

- Rule: `act-interpretation-time.l4`: `s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided`
- Reading taken: Compared, as points in time (the day and the time of day), with the commencement under paragraph (a): the start of the day after the notification day, or after the day the instrument is made or approved.
- Other reading: Compared with the notification day itself, or with the moment the instrument is notified or made.
- Text: s 73 (2) (b) "a later date or time of commencement" and (c) "an earlier date or time" name no comparator; paragraph (a) is the only commencement the subsection states before them.

### F3: When a law commences once s 77 (4) stops s 77 (3) applying

- Rule: `act-interpretation-time.l4`: `s 77 (3), (4): when a law commences under a commencement notice`
- Reading taken: The law commences at the point the notice fixes (the earlier date the notice clearly indicates, under authority given by an Act).
- Other reading: The text gives no commencement for that case, so the answer would be NOTHING.
- Text: s 77 (1) "a law ... expressed to commence on a day fixed or otherwise determined by a notice"; s 77 (2) the notice stands even if its day is before its notification day; s 77 (4) says only that subsection (3) does not apply.

### F4: Which of two events fixes the automatic repeal of an amending law when both have happened

- Rule: `act-interpretation-time.l4`: `s 89 (1): the day an amending law is automatically repealed`
- Reading taken: The day after the earlier of (a) all its provisions having commenced and (b) the last uncommenced provisions being omitted or unable to commence.
- Other reading: The day after the later of the two.
- Text: s 89 (1) "An amending law is automatically repealed on the day after (a) ...; or (b) ..." joins the two with "or" and gives no order.

### F5: What "of the same kind" means for an ACT law

- Rule: `act-ch10-referring-to-laws.l4`: `s 98: the reference includes a reference to the law itself`
- Reading taken: The same kind of Act or instrument as s 13 lists: an Act, a subordinate law, a disallowable instrument, a notifiable instrument, a commencement notice, or another statutory instrument.
- Other reading: A wider grouping, for example any statutory instrument for any statutory instrument.
- Text: s 98 "a reference in general terms to an ACT law of the same kind"; s 13 (2) lists the kinds of statutory instrument.

### F6: Whether a provision outside the part named is outside a reference to a part of a law

- Rule: `act-ch10-referring-to-laws.l4`: `s 106: the provision is within a reference to the part of the law`
- Reading taken: JUST FALSE for a provision before the beginning provision or after the ending provision: "is a reference to the following" is read as a "means" statement.
- Other reading: NOTHING: the list is not closed with "only".
- Text: s 106 "a reference to any part of a law is a reference to the following: (a) the provision of the law that begins the part; (b) ...; (c) any provision of the law between ...".

### F7: The part of a provision that exceeds the legislative power

- Rule: `act-ch12-scope.l4`: `s 120 (2) (a): the provision is effective as to the part`
- Reading taken: NOTHING for the part that exceeds the power.
- Other reading: JUST FALSE: the part has no effect.
- Text: s 120 (2) (a) gives the provision effect "to the extent to which it does not exceed power" and does not say what the rest has; s 120 (1) says the Act is not to be interpreted as exceeding the power.

### F8: Whether a definition printed as "term—an act is authorised if—" closes the case

- Rule: `act-ch12-scope.l4`: `s 121 (6): the act or omission of the government entity is authorised`
- Reading taken: A definition of the term: JUST FALSE when the paragraph for the entity's kind is not met.
- Other reading: A sufficient condition only: NOTHING when it is not met.
- Text: s 121 (6) "In this section: authorised—an act or omission of a government entity is authorised if— (a) for an instrumentality ... (d) for anyone else ...".

### F9: What N months are

- Rule: `act-interpretation-time.l4`: `dictionary, month: the last day of a run of successive months, the first beginning at the start of a day` (taken); `dictionary, month, other reading: the last day of N months counted to the corresponding day of the Nth following calendar month` (the other)
- Reading taken: N months are N successive months, each beginning at the start of the day after the previous one ended.
- Other reading: N months run to the corresponding day of the Nth following calendar month.
- Text: The dictionary defines one month ("a period beginning at the start of any day of one of the calendar months and ending immediately before the start of the corresponding day of the next calendar month ...") and has no entry for N months.
  The readings agree for starting days 1 to 28 and differ otherwise: from 31 January 2024, 2 months end on 31 March (taken) or 30 March (other).

### F10: What N years are, and from which day they can be counted

- Rule: `act-interpretation-time.l4`: `dictionary, calendar year and year: the last day of a run of calendar years beginning at the start of a day` (taken); `dictionary, year, other reading: the last day of N years counted as 12 months each from any starting day` and `s 151, other reading of years: the last day of a period of days, months or years that begins on or from a stated day` (the other)
- Reading taken: A year is a calendar year, "a period of 12 months beginning on 1 January"; a period of N years has an answer only when it starts on 1 January, and answers NOTHING from any other day.
- Other reading: N years are 12N months counted from any starting day.
- Text: The dictionary: "calendar year means a period of 12 months beginning on 1 January" and "year, without specifying the kind of year, means calendar year".
  It has no rule for a period of years that starts on another day.
  Three years from 16 July 2025 answers NOTHING (taken) or 16 July 2028 (other).

### F11: Which 4-year periods s 133 (3) counts

- Rule: `act-ch13-structure.l4`: `s 133 (3): the last day by which the Attorney-General must have reviewed the amount of a penalty unit`
- Reading taken: Successive periods of 4 years counted from the day the subsection commences; the first review is due by the last day of the first period.
- Other reading: 4 years from each review, so the next review is due 4 years after the last one; the same function gives this when the day of the last review is passed as the start and 1 as the period.
- Text: s 133 (3) "The Attorney-General must review the amount of a penalty unit at least once every 4 years after the day this subsection commences."

### F12: How "before the end of 6 sitting days after the day the instrument was presented" is counted

- Rule: `act-ch14-interpretation.l4`: `s 142 (2): the material may be considered in working out the meaning of a statutory instrument`
- Reading taken: Material presented or made on or before the 6th sitting day after the day of presentation (sitting days counted from 1 on the first sitting day after that day) is in time.
- Other reading: Material presented before the 6th sitting day begins (the 6th sitting day excluded), or counting the day of presentation as the first.
- Text: Table 142, column 3, items 2 to 4 "before the end of 6 sitting days after the day the instrument was presented to the Assembly"; the text does not define a sitting day or say how to count one.

### F13: The birthday of a person born on 29 February in a year without that day

- Rule: `act-interpretation-time.l4`: `s 149: the age in years of a person on a day` and `s 149: the day a person attains an age in years`
- Reading taken: NOTHING for 28 February in such a year, and NOTHING for the day an age is reached when the birth date is 29 February and the age falls in such a year.
- Other reading: The birthday is 28 February, or 1 March.
- Text: s 149 "a person is an age in years at the beginning of the person's birthday for the age"; the text does not say which day is the birthday when there is no 29 February.

### F14: Whether a document served in a way the sections do not list is served

- Rule: `act-ch19-functions-and-service.l4`: `s 247 (1): the document may be served on an individual in this way`, `s 248 (1): the document may be served on a corporation in this way`, `s 249: the document may be served on an agency in this way`
- Reading taken: JUST TRUE when the facts match a listed way; NOTHING otherwise.
- Other reading: JUST FALSE for a way the section does not list.
- Text: ss 247 to 249 say a document "may be served" in the listed ways; s 251 (1) says the part does not affect any other law that authorises or requires service otherwise.

### F15: A document sent by fax or email when the sender has reason to suspect it was not received, or doubt is raised

- Rule: `act-interpretation-time.l4`: `s 250: the day a document is taken to be served`
- Reading taken: NOTHING: s 250 (3) gives a presumption only when the sender has no reason to suspect, and the text does not say what happens otherwise.
- Other reading: JUST FALSE: the document is not served.
- Text: s 250 (3) "If the sender has no reason to suspect ... the document is presumed to be served when sent unless evidence sufficient to raise doubt about the presumption is given"; s 250 (4) defines the reason to suspect with "only if".

### F16: Whether an act on the day a law commences is "after the law commences"

- Rule: `act-ch9-repeal-and-amendment.l4`: `s 84A (1): the act or omission is an offence`, `s 84A (2): the increase in the penalty applies to the offence`
- Reading taken: An act or omission on the day the law commences is after the law commences, because a law commences at the beginning of its day (s 74 (1)).
- Other reading: Only acts on a later day are after.
- Text: s 84A (1) "only an offence if done or not done after the law commences"; s 74 (1) "if a law commences on a day, it commences at the beginning of the day unless otherwise provided" (the note under s 85 (2) says the same).

### Questions the brief raised that the text settles

- Whether a period "from" or "after" a day counts that day: It does not: s 151 (2), table 151, item 2 ("is described as beginning from or after ... does not include the stated day"); a period beginning "on" the day does (item 1). s 151 (3) lets a thing to be done within a period after a stated day be done on the stated day.
- Whether the last day of a period is inside it: Yes for a period ending "on" or "by" a day (table 151, item 3); a period of N days that begins on a day ends on day N, so the last day is the first day plus N minus 1 (`s 151: the last day of a period of days that begins on or from a stated day`).
- Whether the rule that moves a last day off a day that is not a working day applies to months and years: Yes: s 151A (1) applies to "a particular day or within a particular period of time" of any unit, and the module applies it to every unit (`s 151 and s 151A: the last day on which the thing may be done within a period that begins on or from a stated day`).

## What the Act turns out to say

1. An Act begins on the day after its notification day, or on the different date or time that it or another Act provides (s 73 (1)). Asserted.
2. A legislative instrument begins on the day after its notification day, unless an Act or the instrument provides a later date, an Act provides an earlier date, or the instrument provides an earlier date under authority given by an Act (s 73 (2)); an earlier date that the instrument provides without that authority does not apply, and the instrument begins on the day after its notification day (s 73 (3)). Asserted.
3. An instrument that is not a legislative instrument begins on the day after it is made, or after it is approved where approval is required, or on a later date that an Act or the instrument provides (s 73 (4) (a), (b)). Asserted.
4. An Act or legislative instrument commences retrospectively if it commences earlier than the day after its notification day (s 75A (1)). Asserted.
5. A commencement notice that fixes a day on or before its own notification day makes the law commence on the day after the notice's notification day, unless the notice clearly indicates the earlier date and provides for it under authority given by an Act (s 77 (3), (4)). Asserted.
6. A postponed law that has not commenced within 6 months beginning on its notification day commences on the first day after that period: notified on 10 March 2025, on 10 September 2025 (s 79 (1); dictionary: month). Asserted.
7. The text does not say what happens under s 79 (1) to a postponed law that has commenced within the 6 months. Asserted.
8. The repeal of a law that is not remade on the day it is repealed takes effect at midnight on that day; if the law is remade on that day, the repeal takes effect when the remade law commences (s 85 (2), (3)); the text does not say when, if the remade law's commencement is not stated. Asserted.
9. An amending law is repealed on the day after all its provisions have commenced or after the last uncommenced provisions are omitted or cannot commence, and where both have happened the encoding takes the earlier (s 89 (1); fork F4); where neither has happened the text does not say. Asserted.
10. An appropriation Act is repealed on the last day of the financial year, a period of 12 months beginning on 1 July: for the year beginning 1 July 2025, on 30 June 2026 (s 89 (2); dictionary: financial year). Asserted.
11. A person is an age in years at the beginning of the person's birthday for the age (s 149): born on 15 January 2000, a person is 24 on 14 January 2025 and 25 on 15 January 2025. Asserted.
12. The text does not say which day is the birthday of a person born on 29 February in a year that has no 29 February, so the Act does not answer that person's age on 28 February of such a year (s 149; fork F13). Asserted.
13. A period described as beginning from or after a day does not include that day, and one beginning at, on or with it does (s 151 (2), table 151, items 1 and 2): 30 days from 1 January 2026 end on 31 January 2026. Asserted.
14. Despite table 151 item 2, a thing that may be done within a period after a stated day may be done on the stated day (s 151 (3)). Asserted.
15. A month is a period beginning at the start of a day and ending immediately before the start of the corresponding day of the next calendar month, or at the end of the next calendar month if there is no such day (dictionary: month): 1 month from 31 January 2024 ends on 29 February 2024, and 2 months from 31 December 2025 end on 28 February 2026. Asserted.
16. A year is a calendar year, a period of 12 months beginning on 1 January, and the encoding gives an answer for a period of years only where the period begins on 1 January; three years from 16 July 2025, five years from 15 January 2025 or from 1 September 2025, and one year from 29 February 2024 are not answered (dictionary: calendar year, year; fork F10). Asserted.
17. A period of years that is counted from 31 December begins on 1 January (table 151, item 2) and so is a run of calendar years: 1 year from 31 December 2025 ends on 31 December 2026. Tested in `act-tests-time.l4`.
18. The text defines no period of weeks, so a period counted in weeks is not answered. Asserted.
19. Where the day, or the last day of the period, is not a working day, the thing must or may be done on the next day that is a working day (s 151A (2)): 3 days from Wednesday 8 April 2026 end on Saturday 11 April, so the thing may be done on Monday 13 April, or on Tuesday 14 April if Monday 13 April is a public holiday. Asserted.
20. A working day is, for something done at an office of a public entity, a day when the office is open; for anything else, a day that is not a Saturday, a Sunday or a public holiday, and for something done by or in relation to an authorised deposit-taking institution not a bank holiday it observes either (s 151A (4)). Asserted.
21. A period occurring between 2 events does not include the days when the events happen (s 151 (2), table 151, item 5): to serve a notice 2 days before a return date that is Friday 10 April 2026, serve on or before Tuesday 7 April 2026. Asserted.
22. A thing for which no time is provided must or may be done as soon as possible and as often as needed (s 151B). Asserted.
23. A person may apply to the court or other entity for a time to be extended even though it has ended, where the court or entity has power to extend it; this applies only to an applicable law or applicable provision, that is, an Act enacted or statutory instrument made after 1 January 2006, or a provision inserted after that date into an older one (s 151C (2), (5), (6)). Asserted.
24. The obligation to do an act continues until the act is done, even though the time for it has passed (s 152). Asserted.
25. A penalty expressed as a number of penalty units is a fine of that many units, and a penalty unit is $160 for an offence committed by an individual and $810 for one committed by a corporation, so 20 units are $3 200 and $16 200 (s 133 (1), (2)); the text gives no dollar amount for an offender that is neither. Asserted.
26. Where the penalty for an offence is a period of imprisonment only and a corporation is convicted, the court may impose a maximum of 50 penalty units for a period of up to 6 months, 100 for over 6 months to 1 year, 200 for over 1 to 2 years, 500 for over 2 to 5 years, 1 000 for over 5 to 10 years and 1 500 for longer (s 161 (3)). Asserted.
27. A document served by post is taken to be served when it would have been delivered in the ordinary course of post (s 250 (1)); one sent by fax or email is presumed served when sent if the sender has no reason to suspect it was not received and no doubt is raised (s 250 (3), (4)); one left at an address as ss 247 (e), 248 (e) and 249 (e) provide is taken to be served when it was left (s 250 (5)). Asserted.
28. Where a fax or email sender has reason to suspect that it was not received, or evidence raises doubt about the presumption, the text does not say when the document is taken to be served (s 250 (3); fork F15). Asserted.
29. Section 250 does not say when a document given to the person, or to an executive officer, is taken to be served. Asserted.
30. A determinative provision may be displaced expressly or by a manifest contrary intention, and a non-determinative provision expressly or by a contrary intention (s 6 (2), (3)); ss 151, 151A and 151C are determinative only so far as they apply to an applicable law or applicable provision, so for an older law a contrary intention that is not manifest displaces them (s 151 (4), s 151A (3)). Asserted.
31. A reference to any part of a law is a reference to the provision that begins the part, the provision that ends it and any provision between them (s 106; fork F6 for provisions outside). Tested in `act-tests-ch10.l4`.

## Worked cases: the periods the brief names

| Case | Answer | Where the text decides it |
|---|---|---|
| Three years from 2025-07-16 | Not answered (`NOTHING`). The other reading, 12 months to the year from any starting day, gives 2028-07-16. | Dictionary: calendar year, year; fork F10. Asserted in `act-cases-seat.l4` and `act-tests-time.l4`. |
| Five years from 2025-01-15 | Not answered (`NOTHING`). The other reading gives 2030-01-15. | The same. Asserted in `act-tests-time.l4`. |
| Five years from 2025-09-01 | Not answered (`NOTHING`). The other reading gives 2030-09-01. | The same. Asserted in `act-tests-time.l4`. |
| Thirty days from 2026-01-01 | 2026-01-31. | `s 151 (2)`, table 151, item 2: the stated day is not counted, so day 1 is 2 January. Asserted in `act-cases-seat.l4`. |
| Two months from 2025-12-31 | 2026-02-28. | Table 151, item 2 puts the start on 1 January 2026; the dictionary's month then runs 1 January to 31 January and 1 February to 28 February (the day before the corresponding day, 1 March); fork F9. Asserted in `act-cases-seat.l4`. |
| One month from 2024-01-31 | 2024-02-29. | Table 151, item 2 puts the start on 1 February 2024; the month ends immediately before 1 March, on 29 February (a leap year). Asserted in `act-cases-seat.l4`. |
| One year from 2024-02-29 | Not answered (`NOTHING`). The other reading gives 2025-02-28. | Dictionary: calendar year, year; fork F10. Asserted in `act-cases-seat.l4` and `act-tests-time.l4`. |

## Cross-references

`act-xrefs.l4` has 539 rows, one for each citation in the in-scope text that the script ties to a provision in the text, to a part of the dictionary or to another Act or instrument; `act-tests-xrefs.l4` has one assertion per row.
A row carries the line of the text, the citing provision, the words as printed, the kind of reference, the identifier and pinpoint cited, the heading printed with the citation, the heading of the cited provision, and where the target is.

By kind:

- 218 to a section
- 184 to another Act or instrument
- 62 to a provision of the section or definition it is in
- 21 to a part of the dictionary
- 21 to a chapter
- 15 to a part
- 9 to the dictionary
- 5 to a table
- 4 to a schedule

By where the target is:

- 314 in scope
- 184 not resolved here
- 41 out of scope

How the script finds them:

- It reads the text file and walks the in-scope lines.
- It finds a citation of a section (`s 12`, `section 12 (3)`, `ss 12 and 13`), a chapter, a part, a division, a schedule, a table (`table 151`) or the dictionary, and a citation of an Act or instrument other than this Act.
- It finds the paragraph, subsection and definition that a provision cites inside itself ("subsection (2)", "paragraph (b)").
- A reference inside an example is read as a reference to the example's own hypothetical law unless it follows "see" or "compare".
- A bare "pt 1" or "pt 2" in the Act's note on the dictionary and in the dictionary notes means the dictionary's own Part 1 or Part 2.
- A reference to another Act or instrument is a row of its own kind and is not resolved here.
- A reference to a provision outside the encoded scope is a row whose target is marked `out of scope`.
- A citation that the script could not tie to a target in the text is not given a row in `act-xrefs.l4`.

`act-provisions.l4` holds the provision index: 314 entries (chapters, parts, divisions, schedules, sections, the dictionary and its parts, and two tables) with identifier, heading and line range, of which 149 are in scope and 165 are not, and 365 sub-provision paths for 40 sections.

## What the stable binary does not accept

The stable build 1.6.98 is the writing binary.
These two points were met while writing this encoding and probed again on the stable build; the rest of the code uses only plain functions, records, enumerations, lists, `CONSIDER`, `IF` and recursion.

- A `CONSIDER` with several `WHEN` arms on one line is refused with a parse error; each arm is on its own line.
- The list function `length` is not defined: "I could not find a definition for the identifier length".
  Counting and membership are done by recursion on `first FOLLOWED BY rest`.

Every module gives the same four counts on the main build 1.6.110 as on the stable build.
No module uses `#TRACE`, `MUST` or `PARTY`, so the check's one blind spot (a different trace outcome) does not apply.

## Checks run

`check.sh`, with the stable build as `L4` and the main build as `L4_MAIN`, `JL4_LIBRARY_PATH` unset:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
act-cases-seat.l4                              0        90       0        0         0 |      0        90       0        0  same
act-ch1-preliminary.l4                         0         0       0        0         0 |      0         0       0        0  same
act-ch10-referring-to-laws.l4                  0         0       0        0         0 |      0         0       0        0  same
act-ch12-scope.l4                              0         0       0        0         0 |      0         0       0        0  same
act-ch13-structure.l4                          0         0       0        0         0 |      0         0       0        0  same
act-ch14-interpretation.l4                     0         0       0        0         0 |      0         0       0        0  same
act-ch15-aids.l4                               0         0       0        0         0 |      0         0       0        0  same
act-ch19-functions-and-service.l4              0         0       0        0         0 |      0         0       0        0  same
act-ch8-commencement.l4                        0         0       0        0         0 |      0         0       0        0  same
act-ch9-repeal-and-amendment.l4                0         0       0        0         0 |      0         0       0        0  same
act-determinative.l4                           0         0       0        0         0 |      0         0       0        0  same
act-dictionary.l4                              0         0       0        0         0 |      0         0       0        0  same
act-interpretation-time.l4                     0         0       0        0         0 |      0         0       0        0  same
act-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
act-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
act-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
act-section-definitions.l4                     0         0       0        0         0 |      0         0       0        0  same
act-tests-ch1.l4                               0       116       0        0         0 |      0       116       0        0  same
act-tests-ch10.l4                              0       107       0        0         0 |      0       107       0        0  same
act-tests-ch12.l4                              0        64       0        0         0 |      0        64       0        0  same
act-tests-ch13.l4                              0       101       0        0         0 |      0       101       0        0  same
act-tests-ch14.l4                              0        74       0        0         0 |      0        74       0        0  same
act-tests-ch15.l4                              0       176       0        0         0 |      0       176       0        0  same
act-tests-ch19.l4                              0        92       0        0         0 |      0        92       0        0  same
act-tests-ch8.l4                               0        79       0        0         0 |      0        79       0        0  same
act-tests-ch9.l4                               0       150       0        0         0 |      0       150       0        0  same
act-tests-determinative.l4                     0        50       0        0         0 |      0        50       0        0  same
act-tests-dictionary.l4                        0       512       0        0         0 |      0       512       0        0  same
act-tests-section-definitions.l4               0       236       0        0         0 |      0       236       0        0  same
act-tests-time.l4                              0       212       0        0         0 |      0       212       0        0  same
act-tests-xrefs.l4                             0       539       0        0         0 |      0       539       0        0  same
act-xrefs.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (32 modules)                             0      2598       0        0           |      0      2598       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `check --strict` over every `act-*.l4` file:

```
$ python3 -I srcrefs.py check --refs ../../registers/source-bundle/A2001-14.txt act-*.l4
srcrefs check: 1440 src: lines, 672 runs, 673 locators, 0 problems

$ python3 -I srcrefs.py check --strict ../../registers/source-bundle/A2001-14.txt act-*.l4
srcrefs check: 1440 src: lines, 672 runs, 673 locators, 0 problems
```

Every module runs with no error diagnostic and no refused assertion on both builds.
In each test file and in the case file the number of assertions satisfied equals the number of `#ASSERT` lines in the file.
No assertion is meant to fail.

## What would need doing before this encoding is worth relying on

- A domain expert reads it against the authorised republication; the deposited text is an unofficial conversion.
- The forks F1 to F16 are ruled one by one; each changes an answer for some facts.
- The Holidays Act 1958, sections 3 and 4, is added, so that "a day that does not count" is no longer an input.
- The time of day within a day is added to the seat questions, for laws that begin or end at a stated time.
- The chapters out of scope (Chapters 2 to 7, 11, 16 to 18, 20 and Parts 19.3, 19.4, 19.6, 19.7) are encoded, or a decision is recorded that they stay out.
- A provision inserted after 1 January 2006 into an older law is asked in the seat questions that depend on whether a section is determinative.
- The seat is deployed and its questions are read as a form by someone who did not write them.
