# Interpretation Act 1987 (New South Wales): L4 encoding, notes

- **Status:** draft.
  No domain expert has read this encoding against the text.
- **Target:** `main`.
  Written with the stable build 1.6.98; `check.sh` also runs every module on the main build 1.6.110 and compares the four counts.
- **Text encoded:** `act-1987-015.txt`, the Open Australian Legal Corpus rendering of Interpretation Act 1987 No 15 (NSW), version dated 2024-11-21.
  It is an unofficial plain-text rendering (see "The text is an unofficial rendering" below).
- **Method:** a single Sonnet 5.5 agent working alone from the brief; no other agent read or tested the work.
- **Where the files are:** every `.l4` file sits in this folder; layer 1 is the `nsw-*.l4` modules and their tests, layer 2 is `nsw-seat.l4` and `nsw-cases-seat.l4`.

## Seat

The seat is: **a person who has a time limit to meet under a New South Wales Act or statutory rule (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.**

Why this seat.
The Act is addressed to the reader of every other New South Wales Act and instrument.
The individual who uses it most directly is the person holding a deadline set somewhere else: the Act says how the days are counted (section 36 and the Dictionary), when an Act or rule begins and stops (sections 23, 24, 39, 71, 30D), what a repeal leaves in force (sections 29, 30C), when a posted document is taken to be served (section 76), whether a form followed in substance is enough (section 80), and when a person attains an age (section 37).
Those rules are the questions of layer 2.

Layer 2 asks 21 questions, each with `@export` and `@desc`, under `§` headings in the order of the text:

| Question (as the person asks it) | Section |
|---|---|
| On which day does my period end? | 36(1), Schedule 4 |
| By which day must I act, allowing for weekends and holidays? | 36(1), 36(2) |
| Is the day I am asking about inside my period of days? | 36(1) |
| Can I still apply for an extension after my period has run out? | 36(3) |
| Is the day I am asking about a working day? | 76(2) |
| Is the day I am asking about a business day? | Schedule 4 |
| On which day does the Act commence? | 23 |
| On which day does the statutory rule commence? | 39 |
| Has the Act or statutory rule commenced at the moment I am asking about? | 24 |
| Is the Act or instrument still operating at the moment I am asking about? | 71 |
| Has the repeal taken effect at the moment I am asking about? | 30D |
| Are the repealed provisions still in force on the day I am asking about? | 29 |
| On which day is the amending Act repealed? | 30C |
| Does the statutory rule I rely on stop working if the written notice was not laid before Parliament in time? | 40(4) |
| Until which day can notice of a motion to disallow the statutory rule I rely on still be given? | 41(1) |
| Can the statutory rule I rely on still be disallowed by a resolution of a House? | 41(1) |
| On which day is the document I posted taken to have been served? | 76(1) |
| Is it enough that I substantially followed the form? | 80(1) |
| On which day does the person attain the age? | 37 |
| Is the person a minor at the moment I am asking about? | 37, Schedule 4 |
| How is the distance measured? | 38 |

The layer calls layer-1 rules and restates none.
There is never a seat for an official: provisions addressed only to the Governor, a Minister, the Parliamentary Counsel, a delegator or a statutory body are encoded in layer 1 for what they decide and have no question in layer 2.
Facts the Act borrows from outside its text are asked as inputs and never guessed: which days are public holidays or bank holidays in the place, the days a House of Parliament sat, whether an Act or instrument authorises service by post, and the judgments the Act hands to the reader ("the context or subject-matter otherwise indicates or requires").
A question the Act does not answer returns `NOTHING`, which the website shows as "the Act does not say".

## What is encoded and what is not

Everything in the text has a row in the coverage table below.
Layer 1 follows the structure of the text:

| Module | What it holds | Assertions |
|---|---|---|
| `nsw-interpretation-time.l4` | the time rules: sections 18, 23(1), 23(5), 24, 30C(2)-(3), 30D, 36, 37, 39(1)(b), 71, 76, and the Dictionary entries midnight, month, calendar month, calendar year, business day, minor; imports only `prelude` and `daydate` | in `nsw-tests-time.l4` |
| `nsw-tests-time.l4` | tests of the time module | 127 |
| `nsw-nouns.l4` | shared nouns (declarations only) | none |
| `nsw-p1-preliminary.l4` | sections 3 to 5 | 36 |
| `nsw-p2-words.l4`, `nsw-p2-crown-offices.l4`, `nsw-p2-references.l4` | Part 2, sections 6 to 21D | 33, 66, 53 |
| `nsw-p3-commencement.l4` | Part 3, sections 22 to 26 | 41 |
| `nsw-p4-repeals.l4` | Part 4, sections 27 to 30D | 81 |
| `nsw-p5-construction.l4` | Part 5, sections 31 to 38 | 68 |
| `nsw-p6-statutory-rules.l4` | Part 6 and Part 6A, sections 39 to 45E | 131 |
| `nsw-p7-functions.l4` | Part 7, sections 46 to 49 | 60 |
| `nsw-p8-bodies.l4` | Part 8, sections 50 to 53A | 62 |
| `nsw-p10-coastal.l4` | Part 10, sections 58 to 63 | 30 |
| `nsw-p11-misc.l4` | Part 11, sections 64 to 83 | 136 |
| `nsw-definitions.l4` | the Dictionary entries whose words can be run | 96 |
| `nsw-dictionary.l4`, `nsw-tests-dictionary.l4` | the Dictionary as a table (137 entries, as printed) and its tests | none, 287 |
| `nsw-schedules.l4` | Schedules 1 to 3 | 75 |
| `nsw-provisions.l4` | the index of provisions (identifier and heading as printed), generated from the text | none; used by the cross-reference tests |
| `nsw-xrefs.l4` | the cross-references as data, with a test per row | 296 |
| `nsw-seat.l4`, `nsw-cases-seat.l4` | layer 2 | none, 92 |

Parts 9 and 12 are printed with nothing but "(Repealed)" and have no module.
Rules of reading (sections 6 to 12) are functions over a small typed description of what the rule operates on, with tests.
Judgments the Act hands to the reader, and facts it borrows from other Acts, are plain inputs.
Where a rule depends on another Act or instrument that is not among the sources (the Public Holidays Act 2010, the Coastal Waters (State Powers) Act 1980 of the Commonwealth and others), the encoding states the provision as the Act states it and asks the borrowed fact as an input.
The Act's own commencement (sections 1 and 2), the regulation-making power in Schedule 1 clause 2, and the twelve repeals in Schedule 2 are machinery and have rows marked `inert`.

## Jural relations

Hohfeld's correlatives: a right (claim) is the other party's duty; a privilege (liberty) is the other party's no-right; a power is the other party's liability, that is, being subject to the power; an immunity is the other party's disability.
Each relation is stated once, as a relation between two parties, in the rule that encodes it.
The first table has a row for each provision that creates a relation; the second lists, once, the provisions that create none (a definition, a counting rule, a rule of reading), by Part or Schedule, so that the whole text is covered.
In an interpretation Act most provisions create none.

| Holder (right, privilege, power or immunity) | Bearer (correlative duty, no-right, liability or disability) | Provision | Rule in L4 |
|---|---|---|---|
| the Governor (power: appoint the day for commencement of an Act within 28 days of assent) | persons to whom the Act will apply (liability) | s 23(2), s 23(4), s 23(4A) | interpretation-time: s 23(2); p3-commencement: s 23(2); p3-commencement: s 23(4) (+1) |
| persons to whom the Act will apply (immunity: no appointed day before the proclamation is published) | the Governor (disability) | s 23(3) | p3-commencement: s 23(3) |
| a person or body with a power under an Act (power: make an instrument and do things before the Act commences) | persons affected by the instrument (liability) | s 26(1), s 26(2), s 26(3), s 26(4) | p3-commencement: s 26(1); p3-commencement: s 26(2); p3-commencement: s 26(3) (+1) |
| the Governor (power: revoke the repeal of an Act or instrument) | persons subject to the revoked repeal (liability) | s 29A(1), s 29A(2) | p4-repeals: s 29A(1) revocation by proclamation; p4-repeals: s 29A(1) effect of revocation; p4-repeals: s 29A(2) |
| a person other than the State or an authority of the State (immunity: rights existing before the revocation are not prejudiced, no liability imposed for earlier acts) | the Governor (disability) | s 29A(3) | p4-repeals: s 29A(3)(a); p4-repeals: s 29A(3)(b) |
| a person holding a right, privilege, obligation or liability acquired, accrued or incurred under the amended or repealed Act or rule (immunity) | the amending or repealing instrument (disability) | s 30(1), s 30(2), s 30(3) | p4-repeals: s 30(1) and (2); p4-repeals: s 30(1) closing words; p4-repeals: s 30(3) |
| a person with a deadline falling on a Saturday, a Sunday or a public or bank holiday (privilege: do the thing on the next day that is not one) | the person or authority that would otherwise treat the thing as late (no-right) | s 36(2) | interpretation-time: s 36(2); interpretation-time: s 36; Schedule 4, month and calendar month and calendar year; interpretation-time: s 36(1) and (2) |
| a person or body with power to extend a period of time (power: exercise it, and receive an application for extension, after the period has expired) | the person who had the period (liability) | s 36(3) | p5-construction: s 36(3)(a); p5-construction: s 36(3)(b) |
| the Governor (power: by order, exclude a class of statutory rules from s 39 or from s 42(1) or (2)) | the makers of the excluded classes of statutory rules (liability) | s 39(4), s 42(4) | p6-statutory-rules: s 39(4); p6-statutory-rules: s 42(4) |
| each House of Parliament (claim: written notice of the making of a statutory rule laid within 14 sitting days) | the person who lays the notice (duty; the text says "must be laid" without naming who bears it, and s 40(3A) says a Minister or the Clerk may lay it) | s 40(1), s 40(3A), s 40(4) | p6-statutory-rules: s 40(1); p6-statutory-rules: s 40(3A); p6-statutory-rules: s 40(4) effect on the rule (+1) |
| either House of Parliament (power: pass a resolution disallowing a statutory rule, within the time s 41(1) allows) | the statutory rule and those subject to it (liability) | s 41(1), s 41(2), s 41(3), s 41(9) | p6-statutory-rules: s 41(1); p6-statutory-rules: s 41(2) the rule ceases to have effect; p6-statutory-rules: s 41(2) the day (+2) |
| the person or body that may make a statutory rule or order (power: amend or repeal it) | those subject to the rule or order (liability) | s 43(1), s 43(2), s 43(3) | p6-statutory-rules: s 43(1); p6-statutory-rules: s 43(2); p6-statutory-rules: s 43(3) |
| the Parliamentary Counsel (power: publish on the NSW legislation website and determine technical requirements) | persons dealing with the published matter (liability) | s 45C(1), s 45C(6) | p6-statutory-rules: s 45C(1); p6-statutory-rules: s 45C(6) |
| a person or body with a power of appointment (power: appoint by name or by office, and the incidental powers s 47 lists) | the person appointed (liability) | s 46(1), s 46(2), s 47(1), s 47(2), s 47(3) | p7-functions: s 46(1); p7-functions: s 46(2); p7-functions: s 47(1)(a) (+3) |
| a delegator (power: delegate a function, revoke the delegation, and exercise the function despite it) | the delegate (liability) | s 49(1), s 49(2), s 49(9) | p7-functions: s 49(1); p7-functions: s 49(2)(a); p7-functions: s 49(2)(b) (+2) |
| a delegate (power: exercise a function incidental to the delegated function) | persons affected by the delegated function (liability) | s 49(4) | p7-functions: s 49(4) |
| a statutory body (immunity: its acts and proceedings are not called into question for the reasons s 52(1) lists) | a person who would call them into question (disability) | s 52(1) | p8-bodies: s 52(1) |
| the Governor (power: extend the age limit for a part-time member, not beyond age 72) | the member concerned (liability) | s 53A(1) | p8-bodies: s 53A(1) |
| persons with functions for the purposes of a law of the State (power: exercise them in the coastal waters) | persons in the coastal waters (liability) | s 61(1) | p10-coastal: s 61(1) |
| the courts of the State (power: jurisdiction in matters arising under the laws of the State as applying to the coastal waters) | parties to those matters (liability) | s 61(2) | p10-coastal: s 61(2) |
| a person serving a document by post (power: effect service by properly addressing, prepaying and posting; service taken effected on the day s 76(1) fixes) | the person served (liability) | s 76(1) | interpretation-time: s 76(1)(b); p11-misc: s 76(1)(a); p11-misc: s 76(1)(b) (+1) |
| the Governor (power: by order published in the Gazette, declare that s 77(1) does not apply to a specified Act, rule or provision) | persons served under the Act or rule specified (liability) | s 77(3) | p11-misc: s 77; p11-misc: s 77(3) |
| a person who posted a document before an order under s 77(3) was made (immunity) | the Governor (disability) | s 77(4) | p11-misc: s 77 |
| a person or body that makes rules of court (power: make rules for the purposes of any Act or statutory rule, and for a court or tribunal whose jurisdiction an Act or rule confers or varies) | the courts and persons before them (liability) | s 78(1), s 78(2) | p11-misc: s 78(1); p11-misc: s 78(2) |
| a person or body conducting a hearing (power: receive evidence and administer oaths to witnesses lawfully called) | a witness lawfully called (liability) | s 79 | p11-misc: s 79 |
| a person completing a form prescribed or approved under an Act or statutory rule (privilege: substantial compliance is sufficient) | the person or body that would insist on strict compliance (no-right) | s 80(1) | p11-misc: s 80(1) strict compliance; p11-misc: s 80(1) substantial compliance |
| the Crown and any other person (immunity: an Act of the kind the Act calls a "Private Act", passed after commencement, is not construed to prejudice their rights or impose liabilities) | Parliament, in such an Act (disability) | s 73(1) | p11-misc: s 73(1)(a); p11-misc: s 73(1)(b) |
| a person who contravenes a temporary Act after it expires and before the continuing Act is assented to (immunity: no liability to penalty) | the enforcing authority (disability) | s 72(2) | p11-misc: s 72(2) |

| Part or Schedule | Provisions that create no such relation (`none`) |
|---|---|
| Part 1 | s 1, s 2, s 3, s 4, s 5 |
| Part 2 | s 6, s 7, s 8, s 9, s 10, s 11, s 12, s 13, s 13A, s 14, s 15, s 16, s 17, s 18, s 18A, s 19, s 20, s 21, s 21C, s 21D |
| Part 3 | s 22, s 23 (subsections not cited above), s 24, s 25, s 26 (subsections not cited above) |
| Part 4 | s 27, s 28, s 29, s 29A (subsections not cited above), s 30 (subsections not cited above), s 30A, s 30B, s 30C, s 30D |
| Part 5 | s 31, s 32, s 33, s 34, s 34A, s 35, s 36 (subsections not cited above), s 37, s 38 |
| Part 6 | s 39 (subsections not cited above), s 40 (subsections not cited above), s 41 (subsections not cited above), s 42 (subsections not cited above), s 43 (subsections not cited above), s 45, s 45A |
| Part 6A | s 45B, s 45C (subsections not cited above), s 45E |
| Part 7 | s 46 (subsections not cited above), s 47 (subsections not cited above), s 48, s 49 (subsections not cited above) |
| Part 8 | s 50, s 52 (subsections not cited above), s 53, s 53A (subsections not cited above) |
| Part 10 | s 58, s 59, s 60, s 61 (subsections not cited above), s 62, s 63 |
| Part 11 | s 64, s 64A, s 65, s 66, s 67, s 68, s 69, s 69A, s 70, s 71, s 72 (subsections not cited above), s 73 (subsections not cited above), s 74, s 75, s 76 (subsections not cited above), s 77 (subsections not cited above), s 78 (subsections not cited above), s 79 (subsections not cited above), s 80 (subsections not cited above), s 80A, s 82, s 83 |
| Schedule 1 | Schedule 1 clause 1, Schedule 1 clause 2 |
| Schedule 3 | Schedule 3 clause 1, Schedule 3 clause 2, Schedule 3 clause 3, Schedule 3 clause 4, Schedule 3 clause 5, Schedule 3 clause 6, Schedule 3 clause 7, Schedule 3 clause 8, Schedule 3 clause 9, Schedule 3 clause 11, Schedule 3 clause 12 |
| Schedule 4 (the Dictionary) | every defined term, with the paragraphs of each entry: `none` (a definition creates no relation) |
| Terms defined in the text of a section (for example in 3(1), 21(2), 23(8), 30C(1), 76(2)) | `none` |
| Title, long title, headings, notes, Schedule 2 | `none` |
| Repealed provisions: Schedule 3 clause 10, s 21A, s 21B, s 44, s 45D, s 51, s 54, s 55, s 56, s 57, s 69B, s 81, s 84, s 85, s 86, s 87, s 88, s 89, s 90, s 91 | `none` (printed repealed) |

## Coverage table

The table is built by a script outside the deposit that reads the text file: it parses the text into 893 rows (every Part, section, subsection, paragraph, Schedule, Schedule clause, defined term, defined term in the text, Schedule table row and note), and it checks that every one of the 977 non-blank lines of the 1110-line text falls in at least one row (none falls outside).
Each row has exactly one disposition:

| Disposition | Rows |
|---|---|
| encoded | 785 |
| fork | 41 |
| inert (1: not operative) | 23 |
| inert (2: machinery) | 23 |
| repealed or blank in this text | 21 |
| total | 893 |

How to read a row.
`encoded` means that a rule in the module named cites, with `@ref`, a range of lines that overlaps the lines the row owns, and that rule is reached by an assertion.
A row that owns only a heading or opening words (such as "In this Act—" before paragraphs) takes the disposition of its sub-rows and says so in the "Where / why" column; there are 68 such rows.
`fork` means that a function encodes the reading the fork register chooses; the last column gives the fork.
`inert (1)` is the deposit notice, the title, the long title, the 13 Part headings, the 4 Schedule headings and the 3 printed notes; each Part and Schedule heading is also held as data in the index.
`inert (2)` is machinery: sections 1 and 2 (short title and the Act's own commencement, with the sub-rows of section 2), Schedule 1 clause 2 (a power to amend clause 1 by regulation, with its two paragraphs) and the 12 rows of Schedule 2 (the repeals of other Acts that section 82 applies).
`repealed or blank in this text` is a row the text prints as "(Repealed)", or as "(Renumbered as Schedule 4)" for section 21(1), whose definitions are in Schedule 4.
Questions on which the Act is silent have no row of their own, because they are not a row of the text.
Each is answered by an explicit "the Act does not say" value (`NOTHING`) and a test asserts it:

| Question | What the Act is silent on | Returned | Asserted in |
|---|---|---|---|
| How is a period of weeks counted? | the Dictionary has no entry for "week" | `NOTHING` | `nsw-tests-time.l4`, `nsw-cases-seat.l4` |
| How is a period of years counted, other than a number of calendar years from 1 January? | the Dictionary has no entry for "year" | `NOTHING` | `nsw-tests-time.l4`, `nsw-cases-seat.l4` |
| What is a "day"? | the Dictionary has no entry for "day"; periods in days are counted as successive days from the day after the given day | `NOTHING` for the term | `nsw-tests-dictionary.l4` |
| Which days are bank holidays in the place? | the Dictionary has no entry for "bank holiday" | `NOTHING` for the term; the days are asked as an input list | `nsw-tests-dictionary.l4`, `nsw-tests-time.l4`, `nsw-cases-seat.l4` |
| Which day is the birthday of a person born on 29 February in a year that is not a leap year? | section 37 | `NOTHING` | `nsw-tests-time.l4`, `nsw-cases-seat.l4` |
| What is a period that is not a positive whole number of units? | section 36 | `NOTHING` | `nsw-tests-time.l4`, `nsw-cases-seat.l4` |
| What if the last day is a day on which an office is closed and is none of the four kinds of day that 36(2) names? | 36(2) names a Saturday, a Sunday, a public holiday and a bank holiday and mentions no other closed day | the day is not moved; no not-covered value is returned, and a person who treats such a day as a holiday adds it to the input list | `nsw-tests-time.l4` (a Friday that is not a holiday is itself the last day) |
| At what moment does an instrument other than an Act or a statutory rule commence on a particular day? | section 24 speaks of an Act or a statutory rule | `NOTHING` | `nsw-tests-time.l4`, `nsw-cases-seat.l4` |

The rows, in the order of the text:

| Row | Lines | Text as printed | Disposition | Where / why | Fork |
|---|---|---|---|---|---|
| Deposit notice | 1-8 | Interpretation Act 1987 | inert (1: not operative) | deposit notice |  |
| Title | 9 | Interpretation Act 1987 No 15 | inert (1: not operative) | title |  |
| Long title | 11 | An Act relating to the interpretation, construction, application and o | inert (1: not operative) | long title |  |
| Part 1 | 13 | Part 1 Preliminary | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 1 | 15-16 | s 1 Name of Act | inert (2: machinery) | short title |  |
| s 2 | 18-25 | 2 Commencement | inert (2: machinery) | commencement of this Act |  |
| s 2(1) | 19 | (1) Sections 1 and 2 shall commence on the date of assent to this Act. | inert (2: machinery) | commencement of this Act |  |
| s 2(2) | 20 | (2) Subject to this section, this Act shall commence on such day as ma | inert (2: machinery) | commencement of this Act |  |
| s 2(3) | 21 | (3) Section 23 shall commence on such day, being a day occurring after | inert (2: machinery) | commencement of this Act |  |
| s 2(4) | 22-25 | (4) Section 81 and Schedule 1 shall commence— | inert (2: machinery) | commencement of this Act |  |
| s 2(4)(a) | 23 | (a) on the day appointed and notified under subsection (2), or | inert (2: machinery) | commencement of this Act |  |
| s 2(4)(b) | 24 | (b) on the day fixed by proclamation for the purposes of section 2 (2) | inert (2: machinery) | commencement of this Act |  |
| s 3 | 27-33 | 3 Definitions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 3(1) | 28-29 | (1) In this Act— | encoded | p1-preliminary: s 3(1) instrument |  |
| s 3(2) | 30-32 | (2) In this Act— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 3(2)(a) | 31 | (a) a reference to a function includes a reference to a power, authori | encoded | p1-preliminary: s 3(2)(a) |  |
| s 3(2)(b) | 32 | (b) a reference to the exercise of a function includes, in relation to | encoded | p1-preliminary: s 3(2)(b) |  |
| s 3(3) | 33 | (3) The Dictionary in Schedule 4 defines certain terms used in Acts an | encoded | p1-preliminary: s 3(3) |  |
| s 4 | 35-36 | s 4 Act binds Crown | encoded | p1-preliminary: s 4 |  |
| s 5 | 38-44 | 5 Application of Act | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 5(1) | 39 | (1) This Act applies to all Acts and instruments (including this Act)  | encoded | p1-preliminary: s 5(1) |  |
| s 5(2) | 40 | (2) This Act applies to an Act or instrument except in so far as the c | encoded | p1-preliminary: s 5(2) |  |
| s 5(3) | 41 | (3) Wherever appropriate, this Act applies to a portion of an Act or i | encoded | p1-preliminary: s 5(3) |  |
| s 5(4) | 42 | (4) Nothing in this Act excludes the application to an Act or instrume | encoded | p1-preliminary: s 5(4) |  |
| s 5(5) | 43 | (5) This section does not authorise a statutory rule to exclude or mod | encoded | p1-preliminary: s 5(5) |  |
| s 5(6) | 44 | (6) The provisions of sections 24, 28, 29, 30, 30B, 33, 42, 43, 69A, 7 | encoded | p1-preliminary: s 5(6) |  |
| Part 2 | 46 | Part 2 Words and expressions | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 6 | 48-49 | s 6 Definitions to be read in context | encoded | p2-words: s 6 |  |
| s 7 | 51-52 | s 7 Cognate words | encoded | p2-words: s 7 |  |
| s 8 | 54-60 | s 8 Gender and number | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 8(a) | 56 | (a) a word or expression that indicates one or more particular genders | encoded | p2-words: s 8(a) |  |
| s 8(b) | 57 | (b) a reference to a word or expression in the singular form includes  | encoded | p2-words: s 8(b) and (c) |  |
| s 8(c) | 58 | (c) a reference to a word or expression in the plural form includes a  | encoded | p2-words: s 8(b) and (c) |  |
| s 8(d) | 59 | (d) a reference to a person does not exclude a reference to a corporat | encoded | p2-words: s 8(d) |  |
| s 8(e) | 60 | (e) a reference to a person does not exclude a reference to an individ | encoded | p2-words: s 8(e) |  |
| s 9 | 62-64 | 9 Meaning of may and shall | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 9(1) | 63 | (1) In any Act or instrument, the word "may", if used to confer a powe | encoded | p2-words: s 9(1) |  |
| s 9(2) | 64 | (2) In any Act or instrument, the word "shall", if used to impose a du | encoded | p2-words: s 9(2) |  |
| s 10 | 66-67 | s 10 Construction of amending Acts and instruments | encoded | p2-words: s 10 |  |
| s 11 | 69-70 | s 11 Words etc in instruments under an Act have same meanings as in th | encoded | p2-words: s 11 |  |
| s 12 | 72-76 | 12 References to New South Wales to be implied | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 12(1) | 73-75 | (1) In any Act or instrument— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 12(1)(a) | 74 | (a) a reference to an officer, office or statutory body is a reference | encoded | p2-words: s 12(1) |  |
| s 12(1)(b) | 75 | (b) a reference to a locality, jurisdiction or other matter or thing i | encoded | p2-words: s 12(1) |  |
| s 12(2) | 76 | (2) In any Act or instrument, a reference to a body constituted by or  | encoded | p2-words: s 12(2) |  |
| s 13 | 78-81 | s 13 Sovereign and Crown | encoded | p2-crown-offices: s 13(a) and (b) |  |
| s 13(a) | 80 | (a) a reference to the Sovereign (whether the words "Her Majesty" or " | encoded | p2-crown-offices: s 13(a) and (b) |  |
| s 13(b) | 81 | (b) a reference to the Crown is a reference to the Crown in right of N | encoded | p2-crown-offices: s 13(a) and (b) |  |
| s 13A | 83-98 | 13A NSW Government agencies and statutory bodies representing the Crow | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 13A(1) | 84-87 | (1) If an Act provides that a body is— | encoded | p2-crown-offices: s 13A(1) |  |
| s 13A(1)(a) | 85 | (a) a NSW Government agency, or | encoded | p2-crown-offices: s 13A(1) |  |
| s 13A(1)(b) | 86 | (b) a statutory body representing the Crown, | encoded | p2-crown-offices: s 13A(1) |  |
| s 13A(2) | 88-91 | (2) If an Act provides that a body— | encoded | p2-crown-offices: s 13A(2) |  |
| s 13A(2)(a) | 89 | (a) is not or does not represent the Crown, or | encoded | p2-crown-offices: s 13A(2) |  |
| s 13A(2)(b) | 90 | (b) is not a NSW Government agency or a statutory body representing th | encoded | p2-crown-offices: s 13A(2) |  |
| s 13A(3) | 92-94 | (3) This section extends (without limiting its operation)— | encoded | p2-crown-offices: s 13A(3) |  |
| s 13A(3)(a) | 93 | (a) to a provision that is expressed to be made for the purposes of an | encoded | p2-crown-offices: s 13A(3) |  |
| s 13A(3)(b) | 94 | (b) to privileges and immunities conferred by law expressly or as a ma | encoded | p2-crown-offices: s 13A(3) |  |
| s 13A(4) | 95-97 | (4) In any Act or instrument— | encoded | p2-crown-offices: s 13A(4) |  |
| s 13A(4)(a) | 96 | (a) a reference to a NSW Government agency includes a reference to a b | encoded | p2-crown-offices: s 13A(4) |  |
| s 13A(4)(b) | 97 | (b) a reference to a statutory body representing the Crown includes a  | encoded | p2-crown-offices: s 13A(4) |  |
| s 13A(5) | 98 |  | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 14 | 100-101 | s 14 Governor | encoded | p2-crown-offices: s 14 |  |
| s 15 | 103-121 | 15 Minister | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 15(1) | 104-106 | (1) In any Act or instrument— | encoded | p2-crown-offices: s 15(1)(a) |  |
| s 15(1)(a) | 105 | (a) a reference to a Minister is a reference to a Minister of the Crow | encoded | p2-crown-offices: s 15(1)(a) |  |
| s 15(1)(b) | 106 | (b) a reference to a particular Minister includes a reference to any o | encoded | p2-crown-offices: s 15(1)(a); s 15(1)(b) |  |
| s 15(2) | 107-111 | (2) In any Act, a reference to "the Minister" is a reference to— | fork | p2-crown-offices: s 15(2); s 15(2) to (4), paragraphs (a) to (d) | F5 |
| s 15(2)(a) | 108 | (a) the Minister administering the Act, | encoded | p2-crown-offices: s 15(2); s 15(2) to (4), paragraphs (a) to (d) |  |
| s 15(2)(b) | 109 | (b) if different Ministers are administering the Act in different resp | fork | p2-crown-offices: s 15(2); s 15(2) to (4), paragraphs (a) to (d) | F5 |
| s 15(2)(c) | 110 | (c) if different Ministers are administering different portions of the | fork | p2-crown-offices: s 15(2); s 15(2) to (4), paragraphs (a) to (d) | F5 |
| s 15(2)(d) | 111 | (d) if paragraphs (b) and (c) do not apply and 2 or more Ministers are | fork | p2-crown-offices: s 15(2); s 15(2) to (4), paragraphs (a) to (d) | F5 |
| s 15(3) | 112-116 | (3) In any instrument, a reference to "the Minister" is a reference to | fork | p2-crown-offices: s 15(3) | F5 |
| s 15(3)(a) | 113 | (a) the Minister administering the Act under which the instrument is m | encoded | p2-crown-offices: s 15(3) |  |
| s 15(3)(b) | 114 | (b) if different Ministers are administering that Act in different res | fork | p2-crown-offices: s 15(3) | F5 |
| s 15(3)(c) | 115 | (c) if different Ministers are administering different portions of tha | fork | p2-crown-offices: s 15(3) | F5 |
| s 15(3)(d) | 116 | (d) if paragraphs (b) and (c) do not apply and 2 or more Ministers are | fork | p2-crown-offices: s 15(3) | F5 |
| s 15(4) | 117-121 | (4) In an Act or instrument, a reference to the Minister administering | fork | p2-crown-offices: s 15(4) | F5 |
| s 15(4)(a) | 118 | (a) the Minister administering the other Act, or | encoded | p2-crown-offices: s 15(4) |  |
| s 15(4)(b) | 119 | (b) if different Ministers are administering the other Act in differen | fork | p2-crown-offices: s 15(4) | F5 |
| s 15(4)(c) | 120 | (c) if different Ministers are administering different portions of the | fork | p2-crown-offices: s 15(4) | F5 |
| s 15(4)(d) | 121 | (d) if paragraphs (b) and (c) do not apply and 2 or more Ministers are | fork | p2-crown-offices: s 15(4) | F5 |
| s 16 | 123-136 | 16 British subjects and aliens | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 16(1) | 124-128 | (1) In any Act or instrument— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 16(1)(a) | 125-127 | (a) a reference to a British subject, or to a natural-born or naturali | encoded | p2-crown-offices: s 16(1)(a) |  |
| s 16(1)(a)(i) | 126 | (i) an Australian citizen, or | encoded | p2-crown-offices: s 16(1)(a) |  |
| s 16(1)(a)(ii) | 127 | (ii) any other person who would, had the relevant Commonwealth law con | encoded | p2-crown-offices: s 16(1)(a) |  |
| s 16(1)(b) | 128 | (b) a reference to an alien is a reference to a person who would, had  | encoded | p2-crown-offices: s 16(1)(b) |  |
| s 16(2) | 129-132 | (2) If a rule of law applies to or in relation to, or has effect with  | encoded | p2-crown-offices: s 16(2) |  |
| s 16(2)(a) | 130 | (a) an Australian citizen, and | encoded | p2-crown-offices: s 16(2) |  |
| s 16(2)(b) | 131 | (b) any other person who would, had the relevant Commonwealth law cont | encoded | p2-crown-offices: s 16(2) |  |
| s 16(3) | 133 | (3) If a rule of law applies to or in relation to, or has effect with  | encoded | p2-crown-offices: s 16(3) |  |
| s 16(4) | 134-136 | (4) In this section, a reference to the relevant Commonwealth law is a | encoded | p2-crown-offices: s 16(4) |  |
| s 16(4)(a) | 135 | (a) the Australian Citizenship Act 1948 of the Commonwealth, as in for | encoded | p2-crown-offices: s 16(4) |  |
| s 16(4)(b) | 136 | (b) the regulations in force immediately before the commencement of th | encoded | p2-crown-offices: s 16(4) |  |
| s 17 | 138-142 | s 17 Public Seal of the State | encoded | p2-crown-offices: s 17 |  |
| s 17(a) | 140 | (a) the Great Seal of the State, or | encoded | p2-crown-offices: s 17 |  |
| s 17(b) | 141 | (b) the Seal of the State, | encoded | p2-crown-offices: s 17 |  |
| s 18 | 144-147 | s 18 Sitting days | encoded | interpretation-time: s 18; s 40(1); s 41(1)(b) / p2-crown-offices: s 18(a) |  |
| s 18(a) | 146 | (a) a reference to a sitting day, in relation to a House of Parliament | encoded | interpretation-time: s 18; s 40(1); s 41(1)(b) / p2-crown-offices: s 18(a) |  |
| s 18(b) | 147 | (b) a reference to a number of sitting days, in relation to a House of | encoded | interpretation-time: s 18; s 40(1); s 41(1)(b) / p2-crown-offices: s 18(b) |  |
| s 18A | 149-151 | 18A Tabling of documents | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 18A(1) | 150 | (1) In an Act or statutory rule, a reference to tabling a document in  | encoded | p2-crown-offices: s 18A(1) |  |
| s 18A(2) | 151 | (2) This section applies in relation to the tabling of a document befo | encoded | p2-crown-offices: s 18A(2) |  |
| s 19 | 153-155 | 19 Holders of offices | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 19(1) | 154 | (1) In any Act or instrument, a reference to a particular officer or t | encoded | p2-crown-offices: s 19(1) |  |
| s 19(2) | 155 | (2) The office of chairperson, chairman or chairwoman may be referred  | encoded | p2-crown-offices: s 19(2) |  |
| s 20 | 157-163 | s 20 References to statutory rules etc | encoded | p2-references: s 20 |  |
| s 21 | 165-172 | 21 References to Colony and punishments for offences | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 21(1) | 166 | (1) (Renumbered as Schedule 4) | repealed or blank in this text | printed "(Renumbered as Schedule 4)"; the text of the definitions is in Schedule 4 |  |
| s 21(2) | 167-169 | (2) In any Act passed before the commencement of this Act, and in any  | encoded | p2-references: s 21(2) Colony; s 21(2) the Colony |  |
| s 21(3) | 170-172 | (3) In any Act or instrument— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 21(3)(a) | 171 | (a) a reference to an offence that is punishable by imprisonment for a | encoded | p2-references: s 21(3)(a) |  |
| s 21(3)(b) | 172 | (b) a reference to an offence that is punishable by imprisonment for a | encoded | p2-references: s 21(3)(b) |  |
| s 21A | 174 | 21A, 21B (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 21B | 174 | 21A, 21B (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 21C | 176-202 | 21C References to de facto partners and de facto relationships | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 21C(1) | 177-179 | (1) Meaning of "de facto partner" For the purposes of any Act or instr | encoded | p2-references: s 21C(1) |  |
| s 21C(1)(a) | 178 | (a) the person is in a registered relationship or interstate registere | encoded | p2-references: s 21C(1) |  |
| s 21C(1)(b) | 179 | (b) the person is in a de facto relationship with the other person. | encoded | p2-references: s 21C(1) |  |
| s 21C(2) | 180-183 | (2) Meaning of "de facto relationship" For the purposes of any Act or  | encoded | p2-references: s 21C(2); s 21C(2) closing sentence |  |
| s 21C(2)(a) | 181 | (a) they have a relationship as a couple living together, and | encoded | p2-references: s 21C(2) |  |
| s 21C(2)(b) | 182 | (b) they are not married to one another or related by family. | encoded | p2-references: s 21C(2) |  |
| s 21C(3) | 184-194 | (3) Determination of "relationship as a couple" In determining whether | encoded | p2-references: s 21C(3); s 21C(3) closing sentence |  |
| s 21C(3)(a) | 185 | (a) the duration of the relationship, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(b) | 186 | (b) the nature and extent of their common residence, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(c) | 187 | (c) whether a sexual relationship exists, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(d) | 188 | (d) the degree of financial dependence or interdependence, and any arr | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(e) | 189 | (e) the ownership, use and acquisition of property, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(f) | 190 | (f) the degree of mutual commitment to a shared life, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(g) | 191 | (g) the care and support of children, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(h) | 192 | (h) the performance of household duties, | encoded | p2-references: s 21C(3) |  |
| s 21C(3)(i) | 193 | (i) the reputation and public aspects of the relationship. | encoded | p2-references: s 21C(3) |  |
| s 21C(4) | 195-198 | (4) Meaning of "related by family" For the purposes of subsection (2), | encoded | p2-references: s 21C(4) |  |
| s 21C(4)(a) | 196 | (a) one is the child (including an adopted child) of the other, or | encoded | p2-references: s 21C(4) |  |
| s 21C(4)(b) | 197 | (b) one is another descendant of the other (even if the relationship b | encoded | p2-references: s 21C(4) |  |
| s 21C(4)(c) | 198 | (c) they have a parent in common (including an adoptive parent of eith | encoded | p2-references: s 21C(4) |  |
| s 21C(5) | 199-201 | (5) Subsection (4) applies— | encoded | p2-references: s 21C(5) |  |
| s 21C(5)(a) | 200 | (a) even if an adoption has been declared void or is of no effect, and | encoded | p2-references: s 21C(5) |  |
| s 21C(5)(b) | 201 | (b) to adoptions under the law of any place (whether in or out of Aust | encoded | p2-references: s 21C(5) |  |
| s 21C(6) | 202 | (6) Subsection (4) applies in relation to a child whose parentage is t | encoded | p2-references: s 21C(6) |  |
| s 21D | 204-206 | 21D References to health practitioners | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 21D(1) | 205 | (1) In any Act or instrument, a reference to a named class of health p | encoded | p2-references: s 21D(1) |  |
| s 21D(2) | 206 | (2) However, if the reference is to a registered nurse this is taken n | encoded | p2-references: s 21D(2) |  |
| Part 3 | 208 | Part 3 Commencement of Acts and instruments | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 22 | 210-212 | 22 References to enactment etc of Acts | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 22(1) | 211 | (1) In any Act or instrument, a reference to the enactment of an Act o | encoded | p3-commencement: s 22(1) |  |
| s 22(2) | 212 | (2) The date purporting to be the date of assent to an Act, as appeari | encoded | p3-commencement: s 22(2) |  |
| s 23 | 214-236 | 23 Commencement of Acts | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 23(1) | 215-218 | (1) An Act shall commence, or shall be deemed to have commenced— | encoded | interpretation-time: s 23(1)(a) |  |
| s 23(1)(a) | 216 | (a) except as provided by paragraphs (b) and (c)—on the day occurring  | encoded | interpretation-time: s 23(1)(a) |  |
| s 23(1)(b) | 217 | (b) if the Act provides for its commencement, whether by proclamation  | encoded | interpretation-time: s 23(1)(a) |  |
| s 23(1)(c) | 218 | (c) if a day is appointed for its commencement by a proclamation under | encoded | interpretation-time: s 23(1)(a) |  |
| s 23(2) | 219-221 | (2) The Governor may, by proclamation, appoint a day for the commencem | encoded | interpretation-time: s 23(2) / p3-commencement: s 23(2) |  |
| s 23(2)(a) | 220 | (a) no earlier than the date of assent to the Act, and | encoded | interpretation-time: s 23(2) / p3-commencement: s 23(2) |  |
| s 23(2)(b) | 221 | (b) no later than the day occurring 28 days after the date of assent t | encoded | interpretation-time: s 23(2) / p3-commencement: s 23(2) |  |
| s 23(3) | 222 | (3) A power to appoint by proclamation a day on which an Act shall com | fork | p3-commencement: s 23(3) | F7 |
| s 23(4) | 223 | (4) A power to appoint by proclamation a day on which an Act shall com | encoded | p3-commencement: s 23(4) |  |
| s 23(4A) | 224 | (4A) A power to appoint by proclamation different days for the commenc | encoded | p3-commencement: s 23(4A) |  |
| s 23(5) | 225-230 | (5) A proclamation appointing a day on which an Act shall commence doe | fork | interpretation-time: s 23(5) / p3-commencement: s 23(5) chapeau | F7 |
| s 23(5)(a) | 226 | (a) except as provided by paragraph (b)—on the day on which the procla | fork | interpretation-time: s 23(5) | F7 |
| s 23(5)(b) | 227-230 | (b) in the case of a proclamation under subsection (2)— | fork | interpretation-time: s 23(5) | F7 |
| s 23(5)(b)(i) | 228 | (i) on the day on which the proclamation is published, or | fork | interpretation-time: s 23(5) | F7 |
| s 23(5)(b)(ii) | 229 | (ii) on the day on which the Act would have commenced had the proclama | fork | interpretation-time: s 23(5) | F7 |
| s 23(6) | 231 | (6) An Act may be referred to by its short title (or name) even though | encoded | p3-commencement: s 23(6) |  |
| s 23(7) | 232-235 | (7) If an Act provides for its commencement, whether by proclamation u | encoded | p3-commencement: s 23(7) |  |
| s 23(7)(a) | 233 | (a) that provision has effect for the purposes of subsection (1) (b),  | encoded | p3-commencement: s 23(7) |  |
| s 23(7)(b) | 234 | (b) in the case of an Act that provides for its commencement by procla | encoded | p3-commencement: s 23(7) |  |
| s 23(8) | 236 |  | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 24 | 238-239 | s 24 Time of commencement of Acts and statutory rules | fork | interpretation-time: s 24 | F11 |
| s 25 | 241-242 | s 25 References to commencement of Acts and instruments | encoded | p3-commencement: s 25 |  |
| s 26 | 244-260 | 26 Exercise of certain powers between enactment and commencement of Ac | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 26(1) | 245-251 | (1) If an Act (in this section referred to as the Act concerned) that  | encoded | p3-commencement: s 26(1) |  |
| s 26(1)(a) | 246 | (a) confer a power, or | encoded | p3-commencement: s 26(1) |  |
| s 26(1)(b) | 247 | (b) amend some other Act in such a manner that the other Act, as amend | encoded | p3-commencement: s 26(1) |  |
| s 26(1)(c) | 249 | (c) such an instrument may be made, and | encoded | p3-commencement: s 26(1) |  |
| s 26(1)(d) | 250 | (d) any thing may be done for the purpose of enabling such an instrume | encoded | p3-commencement: s 26(1) |  |
| s 26(2) | 252-255 | (2) A provision of an instrument made by virtue of subsection (1) shal | encoded | p3-commencement: s 26(2) |  |
| s 26(2)(a) | 253 | (a) on the day on which the Act concerned commences, or | encoded | p3-commencement: s 26(2) |  |
| s 26(2)(b) | 254 | (b) on the day on which the provision would have taken effect had the  | encoded | p3-commencement: s 26(2) |  |
| s 26(3) | 256-259 | (3) If— | encoded | p3-commencement: s 26(3) |  |
| s 26(3)(a) | 257 | (a) this section applies to an Act that would, had it commenced, amend | encoded | p3-commencement: s 26(3) |  |
| s 26(3)(b) | 258 | (b) the other Act has not commenced, | encoded | p3-commencement: s 26(3) |  |
| s 26(4) | 260 | (4) This section applies to an instrument that does not commence on it | encoded | p3-commencement: s 26(4) |  |
| Part 4 | 262 | Part 4 Amendments and repeals | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 27 | 264-265 | s 27 Acts may be amended etc in the same session of Parliament | encoded | p4-repeals: s 27 |  |
| s 28 | 267-268 | s 28 Repealed Acts and statutory rules not revived | encoded | p4-repeals: s 28 |  |
| s 29 | 270-271 | s 29 Repealed Acts and statutory rules continue in force | fork | p4-repeals: s 29 | F6 |
| s 29A | 273-280 | 29A Revocation of repeal of Acts and instruments | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 29A(1) | 274 | (1) The Governor may, by proclamation published on the NSW legislation | encoded | p4-repeals: s 29A(1) revocation by proclamation; s 29A(1) effect of revocation |  |
| s 29A(2) | 275-277 | (2) The revocation of the repeal of an Act or instrument is authorised | encoded | p4-repeals: s 29A(2) |  |
| s 29A(2)(a) | 276 | (a) stated that this section applied to the repeal or otherwise author | encoded | p4-repeals: s 29A(2) |  |
| s 29A(2)(b) | 277 | (b) described the repeal (in a heading or otherwise) as the repeal of  | encoded | p4-repeals: s 29A(2) |  |
| s 29A(3) | 278-280 | (3) The revocation of the repeal of an Act or instrument under this se | encoded | p4-repeals: s 29A(3)(a); s 29A(3)(b) |  |
| s 29A(3)(a) | 279 | (a) to affect in a manner prejudicial to any person (other than the St | encoded | p4-repeals: s 29A(3)(a); s 29A(3)(b) |  |
| s 29A(3)(b) | 280 | (b) to impose liabilities on any person (other than the State or an au | encoded | p4-repeals: s 29A(3)(b) |  |
| s 30 | 282-303 | 30 Effect of amendment or repeal of Acts and statutory rules | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 30(1) | 283-289 | (1) The amendment or repeal of an Act or statutory rule does not— | encoded | p4-repeals: s 30(1) and (2); s 30(1) closing words |  |
| s 30(1)(a) | 284 | (a) revive anything not in force or existing at the time at which the  | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(1)(b) | 285 | (b) affect the previous operation of the Act or statutory rule or anyt | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(1)(c) | 286 | (c) affect any right, privilege, obligation or liability acquired, acc | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(1)(d) | 287 | (d) affect any penalty incurred in respect of any offence arising unde | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(1)(e) | 288 | (e) affect any investigation, legal proceeding or remedy in respect of | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(2) | 290-294 | (2) Without limiting the effect of subsection (1), the amendment or re | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(2)(a) | 291 | (a) the proof of any past act or thing, or | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(2)(b) | 292 | (b) any right, privilege, obligation or liability saved by the operati | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(2)(c) | 293 | (c) any amendment or validation made by the Act or statutory rule, or | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(2)(d) | 294 | (d) the operation of any savings or transitional provision contained i | encoded | p4-repeals: s 30(1) and (2) |  |
| s 30(3) | 295 | (3) This section applies to the amendment or repeal of an Act or statu | encoded | p4-repeals: s 30(3) |  |
| s 30(4) | 296-303 | (4) In this section, a reference to the amendment or repeal of an Act  | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(a) | 297 | (a) a reference to the expiration of the Act or statutory rule, | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(b) | 298 | (b) a reference to an amendment or repeal of the Act or statutory rule | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(c) | 299 | (c) a reference to the abrogation, limitation or extension of the effe | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(d) | 300-303 | (d) a reference to— | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(d)(i) | 301 | (i) the exclusion from the application of the Act or statutory rule, o | encoded | p4-repeals: s 30(4) |  |
| s 30(4)(d)(ii) | 302 | (ii) the inclusion within the application of the Act or statutory rule | encoded | p4-repeals: s 30(4) |  |
| s 30A | 305-308 | 30A Transferred provisions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 30A(1) | 306 | (1) This section applies where a provision is transferred from an Act  | encoded | p4-repeals: s 30A(1) |  |
| s 30A(2) | 307 | (2) The transfer does not affect the operation (if any) or meaning of  | encoded | p4-repeals: s 30A(2) |  |
| s 30A(3) | 308 | (3) This section applies whether or not the provision is modified, but | encoded | p4-repeals: s 30A(3) |  |
| s 30B | 310-311 | s 30B Effect of amendment of instrument by an Act | encoded | p4-repeals: s 30B |  |
| s 30C | 313-323 | 30C Automatic repeal of amending Acts that have commenced | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 30C(1) | 314-318 | (1) In this section— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 30C(1)(a) | 316 | (a) a whole Act that directly amends or repeals other Acts or instrume | encoded | p4-repeals: s 30C(1) amending Act |  |
| s 30C(1)(b) | 317 | (b) a section or subsection of an Act, a schedule or subschedule to an | encoded | p4-repeals: s 30C(1) amending Act |  |
| s 30C(2) | 319 | (2) An amending Act is repealed on the day after all of its provisions | encoded | interpretation-time: s 30C(2) and (3) / p4-repeals: s 30C(2) and (3) the day of the repeal |  |
| s 30C(3) | 320 | (3) If an amending Act commences before the date of assent, the amendi | encoded | interpretation-time: s 30C(2) and (3) / p4-repeals: s 30C(2) and (3) the day of the repeal |  |
| s 30C(4) | 321 | (4) The repeal by this section of an amending Act does not, because of | encoded | p4-repeals: s 30C(4) |  |
| s 30C(5) | 322 | (5) This section does not apply to an amending Act that makes provisio | encoded | p4-repeals: s 30C(5) and (6) |  |
| s 30C(6) | 323 | (6) This section applies only to an amending Act enacted after 1 Janua | encoded | interpretation-time: s 30C(6) / p4-repeals: s 30C(5) and (6) |  |
| s 30D | 325-326 | s 30D Time of repeal of Acts and instruments | fork | interpretation-time: s 30D | F11 |
| Part 5 | 328 | Part 5 Construction of Acts and instruments | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 31 | 330-335 | 31 Acts and instruments to be construed so as not to exceed the legisl | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 31(1) | 331 | (1) An Act or instrument shall be construed as operating to the full e | encoded | p5-construction: s 31(1) |  |
| s 31(2) | 332-334 | (2) If any provision of an Act or instrument, or the application of an | encoded | p5-construction: s 31(2)(a); s 31(2)(b) |  |
| s 31(2)(a) | 333 | (a) it shall be a valid provision to the extent to which it is not in  | encoded | p5-construction: s 31(2)(a); s 31(2)(b) |  |
| s 31(2)(b) | 334 | (b) the remainder of the Act or instrument, and the application of the | encoded | p5-construction: s 31(2)(b) |  |
| s 31(3) | 335 | (3) This section applies to an Act or instrument in addition to, and w | encoded | p5-construction: s 31(3) |  |
| s 32 | 337-342 | 32 Instruments to be construed so as not to exceed the powers conferre | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 32(1) | 338 | (1) An instrument shall be construed as operating to the full extent o | encoded | p5-construction: s 32(1) |  |
| s 32(2) | 339-341 | (2) If any provision of an instrument, or the application of any such  | encoded | p5-construction: s 32(2)(a); s 32(2)(b) |  |
| s 32(2)(a) | 340 | (a) it shall be a valid provision to the extent to which it is not in  | encoded | p5-construction: s 32(2)(a); s 32(2)(b) |  |
| s 32(2)(b) | 341 | (b) the remainder of the instrument, and the application of the provis | encoded | p5-construction: s 32(2)(b) |  |
| s 32(3) | 342 | (3) This section applies to an instrument in addition to, and without  | encoded | p5-construction: s 32(3) |  |
| s 33 | 344-345 | s 33 Regard to be had to purposes or objects of Acts and statutory rul | encoded | p5-construction: s 33 |  |
| s 34 | 347-364 | 34 Use of extrinsic material in the interpretation of Acts and statuto | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 34(1) | 348-352 | (1) In the interpretation of a provision of an Act or statutory rule,  | encoded | p5-construction: s 34(1) |  |
| s 34(1)(a) | 349 | (a) to confirm that the meaning of the provision is the ordinary meani | encoded | p5-construction: s 34(1) |  |
| s 34(1)(b) | 350-352 | (b) to determine the meaning of the provision— | encoded | p5-construction: s 34(1) |  |
| s 34(1)(b)(i) | 351 | (i) if the provision is ambiguous or obscure, or | encoded | p5-construction: s 34(1) |  |
| s 34(1)(b)(ii) | 352 | (ii) if the ordinary meaning conveyed by the text of the provision (ta | encoded | p5-construction: s 34(1) |  |
| s 34(2) | 353-361 | (2) Without limiting the effect of subsection (1), the material that m | encoded | p5-construction: s 34(2) |  |
| s 34(2)(a) | 354 | (a) all matters not forming part of the Act that are set out in the do | encoded | p5-construction: s 34(2) |  |
| s 34(2)(b) | 355 | (b) any relevant report of a Royal Commission, Law Reform Commission,  | encoded | p5-construction: s 34(2) |  |
| s 34(2)(c) | 356 | (c) any relevant report of a committee of Parliament or of either Hous | encoded | p5-construction: s 34(2) |  |
| s 34(2)(d) | 357 | (d) any treaty or other international agreement that is referred to in | encoded | p5-construction: s 34(2) |  |
| s 34(2)(e) | 358 | (e) any explanatory note or memorandum relating to the Bill for the Ac | encoded | p5-construction: s 34(2) |  |
| s 34(2)(f) | 359 | (f) the speech made to a House of Parliament by a Minister or other me | encoded | p5-construction: s 34(2) |  |
| s 34(2)(g) | 360 | (g) any document (whether or not a document to which a preceding parag | encoded | p5-construction: s 34(2) |  |
| s 34(2)(h) | 361 | (h) any relevant material in the Minutes of Proceedings or the Votes a | encoded | p5-construction: s 34(2) |  |
| s 34(3) | 362-364 | (3) In determining whether consideration should be given to any materi | encoded | p5-construction: s 34(3) |  |
| s 34(3)(a) | 363 | (a) the desirability of persons being able to rely on the ordinary mea | encoded | p5-construction: s 34(3) |  |
| s 34(3)(b) | 364 | (b) the need to avoid prolonging legal or other proceedings without co | encoded | p5-construction: s 34(3) |  |
| s 34A | 366-370 | s 34A Declaration of validity of certain laws | encoded | p5-construction: s 34A |  |
| s 34A(a) | 368 | (a) has the same effect as it would have had, and | encoded | p5-construction: s 34A |  |
| s 34A(b) | 369 | (b) is as valid as it would have been, | encoded | p5-construction: s 34A |  |
| s 35 | 372-387 | 35 Headings etc | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 35(1) | 373-376 | (1) Headings to provisions of an Act or instrument, being headings to— | encoded | p5-construction: s 35 |  |
| s 35(1)(a) | 374 | (a) Chapters, Parts, Divisions or Subdivisions into which the Act or i | encoded | p5-construction: s 35 |  |
| s 35(1)(b) | 375 | (b) Schedules to the Act or instrument, | encoded | p5-construction: s 35 |  |
| s 35(2) | 377-381 | (2) Except as provided by subsections (3) and (4)— | encoded | p5-construction: s 35 |  |
| s 35(2)(a) | 378 | (a) a heading to a provision of an Act or instrument (not being a head | encoded | p5-construction: s 35 |  |
| s 35(2)(b) | 379 | (b) matter within a provision of an Act or instrument (being matter in | encoded | p5-construction: s 35 |  |
| s 35(2)(c) | 380 | (c) a marginal note, footnote or endnote in an Act or instrument, | encoded | p5-construction: s 35 |  |
| s 35(3) | 382 | (3) A heading to a provision of an Act or instrument (not being a head | encoded | p5-construction: s 35 |  |
| s 35(4) | 383-385 | (4) A heading to a provision of an Act or instrument (not being a head | encoded | p5-construction: s 35 |  |
| s 35(4)(a) | 384 | (a) it is referred to expressly, otherwise than by means of matter wit | encoded | p5-construction: s 35 |  |
| s 35(4)(b) | 385 | (b) not being so referred to, it is a heading, marginal note, footnote | encoded | p5-construction: s 35 |  |
| s 35(4A) | 386 | (4A) The number of a section, subsection, clause or subclause of an Ac | encoded | p5-construction: s 35 |  |
| s 35(5) | 387 | (5) This section does not limit the application of section 34 in relat | encoded | p5-construction: s 35(5) |  |
| s 36 | 389-398 | 36 Reckoning of time | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 36(1) | 390 | (1) If in any Act or instrument a period of time, dating from a given  | fork | interpretation-time: s 36(1); s 36; Schedule 4, month and calendar month and calendar year (+1) | F1,F2,F3 |
| s 36(2) | 391-394 | (2) If the last day of a period of time prescribed or allowed by an Ac | fork | interpretation-time: s 36(2); s 36; Schedule 4, month and calendar month and calendar year (+1) | F2,F4 |
| s 36(2)(a) | 392 | (a) on a Saturday or Sunday, or | fork | interpretation-time: s 36(2); s 36; Schedule 4, month and calendar month and calendar year (+1) | F4 |
| s 36(2)(b) | 393 | (b) on a day that is a public holiday or bank holiday in the place in  | fork | interpretation-time: s 36(2); s 36; Schedule 4, month and calendar month and calendar year (+1) | F4 |
| s 36(3) | 395-398 | (3) If in any Act or instrument a period of time is prescribed or allo | encoded | p5-construction: s 36(3)(a); s 36(3)(b) |  |
| s 36(3)(a) | 396 | (a) that power may be exercised, and | encoded | p5-construction: s 36(3)(a); s 36(3)(b) |  |
| s 36(3)(b) | 397 | (b) if the exercise of that power depends on the making of an applicat | encoded | p5-construction: s 36(3)(a); s 36(3)(b) |  |
| s 37 | 400-401 | s 37 Age | fork | interpretation-time: s 37; s 37; Schedule 4, minor | F8,F11 |
| s 38 | 403-406 | s 38 Measurement of distance | encoded | p5-construction: s 38 |  |
| s 38(a) | 405 | (a) for the purposes of any Act passed before the commencement of this | encoded | p5-construction: s 38 |  |
| s 38(b) | 406 | (b) for the purposes of any Act passed after the commencement of this  | encoded | p5-construction: s 38 |  |
| Part 6 | 408 | Part 6 Statutory rules and certain other instruments | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 39 | 410-420 | 39 The making of statutory rules | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 39(1) | 411-413 | (1) A statutory rule— | encoded | interpretation-time: s 39(1)(b) and (2A) |  |
| s 39(1)(a) | 412 | (a) shall be published on the NSW legislation website, and | encoded | interpretation-time: s 39(1)(b) and (2A) / p6-statutory-rules: s 39(1)(a) |  |
| s 39(1)(b) | 413 | (b) commences on the day on which it is so published or, if a later da | encoded | interpretation-time: s 39(1)(b) and (2A) |  |
| s 39(2) | 414 | (2) Subsection (1) does not prevent a statutory rule from specifying d | encoded | interpretation-time: s 39(1)(b) and (2A) / p6-statutory-rules: s 39(2) |  |
| s 39(2A) | 415 | (2A) Neither the whole nor any part of a statutory rule is invalid mer | encoded | interpretation-time: s 39(1)(b) and (2A) / p6-statutory-rules: s 39(2A) |  |
| s 39(3) | 416 | (3) If an Act provides for the making of a statutory rule by a person  | fork | p6-statutory-rules: s 39(3) | F9 |
| s 39(4) | 417-419 | (4) The Governor may, by order published on the NSW legislation websit | encoded | p6-statutory-rules: s 39(4) |  |
| s 39(4)(a) | 418 | (a) in respect of statutory rules made under Acts passed before the co | encoded | p6-statutory-rules: s 39(4) |  |
| s 39(4)(b) | 419 | (b) if, immediately before the commencement of this Act, section 41 of | encoded | p6-statutory-rules: s 39(4) |  |
| s 39(5) | 420 | (5) This section does not apply to the Standing Rules and Orders of th | encoded | p6-statutory-rules: s 39(5) |  |
| s 40 | 422-432 | 40 Notice of statutory rules to be tabled | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 40(1) | 423 | (1) Written notice of the making of a statutory rule must be laid befo | encoded | p6-statutory-rules: s 40(1) |  |
| s 40(2) | 424 | (2) A written notice is to identify the statutory rule to which it rel | encoded | p6-statutory-rules: s 40(2) |  |
| s 40(3) | 425-428 | (3) A written notice shall identify a statutory rule by reference to— | encoded | p6-statutory-rules: s 40(3); s 40(3) closing words |  |
| s 40(3)(a) | 426 | (a) the Act under which it is made, and | encoded | p6-statutory-rules: s 40(3) |  |
| s 40(3)(b) | 427 | (b) its citation (if any), | encoded | p6-statutory-rules: s 40(3) |  |
| s 40(3A) | 429 | (3A) A written notice may be laid before a House of Parliament by a Mi | encoded | p6-statutory-rules: s 40(3A) |  |
| s 40(4) | 430 | (4) Failure to lay a written notice before each House of Parliament in | encoded | p6-statutory-rules: s 40(4) effect on the rule; s 40(4) the notice must still be laid |  |
| s 40(5) | 431 | (5) Any provision of an Act that relates to the laying before each Hou | encoded | p6-statutory-rules: s 40(5) |  |
| s 40(6) | 432 | (6) This section does not apply to the Standing Rules and Orders of th | encoded | p6-statutory-rules: s 40(6) |  |
| s 41 | 434-448 | 41 Disallowance of statutory rules | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 41(1) | 435-437 | (1) Either House of Parliament may pass a resolution disallowing a sta | fork | p6-statutory-rules: s 41(1) | F10 |
| s 41(1)(a) | 436 | (a) at any time before the relevant written notice is laid before the  | encoded | p6-statutory-rules: s 41(1) |  |
| s 41(1)(b) | 437 | (b) at any time after the relevant written notice is laid before the H | fork | p6-statutory-rules: s 41(1) | F10 |
| s 41(2) | 438 | (2) On the passing of a resolution disallowing a statutory rule, the r | encoded | p6-statutory-rules: s 41(2) the rule ceases to have effect; s 41(2) the day |  |
| s 41(3) | 439 | (3) The disallowance of a statutory rule has the same effect as a repe | encoded | p6-statutory-rules: s 41(3) |  |
| s 41(4) | 440-443 | (4) If— | encoded | p6-statutory-rules: s 41(4) |  |
| s 41(4)(a) | 441 | (a) a statutory rule ceases to have effect by virtue of its disallowan | encoded | p6-statutory-rules: s 41(4) |  |
| s 41(4)(b) | 442 | (b) the rule amended or repealed some other Act or statutory rule that | encoded | p6-statutory-rules: s 41(4) |  |
| s 41(5) | 444 | (5) The restoration or revival of an Act or statutory rule pursuant to | encoded | p6-statutory-rules: s 41(5) |  |
| s 41(6) | 445 | (6) This section applies to a portion of a statutory rule in the same  | encoded | p6-statutory-rules: s 41(6) |  |
| s 41(7) | 446 | (7) Any provision of an Act that relates to the disallowance of statut | encoded | p6-statutory-rules: s 41(7) |  |
| s 41(8) | 447 | (8) This section does not apply to the Standing Rules and Orders of th | encoded | p6-statutory-rules: s 41(8) |  |
| s 41(9) | 448 | (9) This section does not limit any provision of an Act (for example,  | encoded | p6-statutory-rules: s 41(9) |  |
| s 42 | 450-458 | 42 Matters for which statutory rules may make provision | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 42(1) | 451 | (1) If an Act authorises or requires provision to be made for or with  | encoded | p6-statutory-rules: s 42(1) |  |
| s 42(2) | 452-456 | (2) A statutory rule may— | encoded | p6-statutory-rules: s 42(2) |  |
| s 42(2)(a) | 453 | (a) apply generally or be limited in its application by reference to s | encoded | p6-statutory-rules: s 42(2) |  |
| s 42(2)(b) | 454 | (b) apply differently according to different factors of a specified ki | encoded | p6-statutory-rules: s 42(2) |  |
| s 42(2)(c) | 455 | (c) authorise any matter or thing to be from time to time determined,  | encoded | p6-statutory-rules: s 42(2) |  |
| s 42(3) | 457 | (3) This section applies to a statutory rule in addition to, and witho | encoded | p6-statutory-rules: s 42(3) |  |
| s 42(4) | 458 | (4) The Governor may, by order published in the Gazette, exclude any s | encoded | p6-statutory-rules: s 42(4) |  |
| s 43 | 460-463 | 43 Implied power to amend or repeal statutory rules and orders | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 43(1) | 461 | (1) If an Act confers a power on any person or body to make a statutor | encoded | p6-statutory-rules: s 43(1) |  |
| s 43(2) | 462 | (2) If an Act or statutory rule confers a power on any person or body  | encoded | p6-statutory-rules: s 43(2) |  |
| s 43(3) | 463 | (3) If the power of a person or body to make a statutory rule or order | fork | p6-statutory-rules: s 43(3) | F9 |
| s 44 | 465 | 44 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 45 | 467-476 | 45 Presumption of validity of certain instruments | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 45(1) | 468 | (1) It shall be presumed, in the absence of evidence to the contrary,  | encoded | p6-statutory-rules: s 45(1) |  |
| s 45(2) | 469-476 | (2) In this section— | encoded | p6-statutory-rules: s 45(2) |  |
| s 45(2)(a) | 471-473 | (a) an instrument— | encoded | p6-statutory-rules: s 45(2) |  |
| s 45(2)(a)(i) | 472 | (i) that is made by the Governor, or | encoded | p6-statutory-rules: s 45(2) |  |
| s 45(2)(a)(ii) | 473 | (ii) that is made by a person or body other than the Governor, but is  | encoded | p6-statutory-rules: s 45(2) |  |
| s 45(2)(b) | 474 | (b) a rule of court, or | encoded | p6-statutory-rules: s 45(2) |  |
| s 45(2)(c) | 475 | (c) an environmental planning instrument, | encoded | p6-statutory-rules: s 45(2) |  |
| s 45A | 478-479 | s 45A Tabling of instruments | encoded | p6-statutory-rules: s 45A |  |
| Part 6A | 481 | Part 6A Publication of legislation | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 45B | 483-489 | s 45B Definitions | encoded | p6-statutory-rules: s 45B legislation |  |
| s 45B(a) | 486 | (a) an Act or instrument of this jurisdiction, or | encoded | p6-statutory-rules: s 45B legislation |  |
| s 45B(b) | 487 | (b) a law of another jurisdiction that, under such an Act or instrumen | encoded | p6-statutory-rules: s 45B legislation |  |
| s 45B(c) | 488 | (c) a publication applied, adopted or incorporated by such an Act or i | encoded | p6-statutory-rules: s 45B legislation |  |
| s 45C | 491-504 | 45C Publication on NSW legislation website | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 45C(1) | 492-495 | (1) The Parliamentary Counsel may publish on the NSW legislation websi | encoded | p6-statutory-rules: s 45C(1) |  |
| s 45C(1)(a) | 493-494 | (a) legislation (as originally made or as amended), and | encoded | p6-statutory-rules: s 45C(1) |  |
| s 45C(1)(b) | 495 | (b) other matter (including information relating to legislation and an | encoded | p6-statutory-rules: s 45C(1) |  |
| s 45C(2) | 496-498 | (2) Legislation, the Gazette or other matter is published on the NSW l | encoded | p6-statutory-rules: s 45C(2) |  |
| s 45C(2)(a) | 497 | (a) if it is made accessible in full on that website, or | encoded | p6-statutory-rules: s 45C(2) |  |
| s 45C(2)(b) | 498 | (b) if notice of its making, issue or other production is made accessi | encoded | p6-statutory-rules: s 45C(2) |  |
| s 45C(3) | 499 | (3) The date on which legislation, the Gazette or other matter is publ | encoded | p6-statutory-rules: s 45C(3) |  |
| s 45C(4) | 500 | (4) If legislation, the Gazette or other matter cannot for technical o | encoded | p6-statutory-rules: s 45C(4) |  |
| s 45C(5) | 501 | (5) The Parliamentary Counsel is to compile and maintain a database of | encoded | p6-statutory-rules: s 45C(5) |  |
| s 45C(6) | 502-504 | (6) For the purpose of facilitating public access to instruments on th | encoded | p6-statutory-rules: s 45C(6) |  |
| s 45C(6)(a) | 503 | (a) the requirements for lodging instruments required to be published  | encoded | p6-statutory-rules: s 45C(6) |  |
| s 45C(6)(b) | 504 | (b) standard technical requirements with respect to the drafting or fo | encoded | p6-statutory-rules: s 45C(6) |  |
| s 45D | 506 | 45D (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 45E | 508-517 | 45E Style changes, roman numerals, colons and dashes | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 45E(1) | 510-514 | (1) Legislation may be published under this Part— | encoded | p6-statutory-rules: s 45E(1) |  |
| s 45E(1)(a) | 511 | (a) with the omission of the enacting formula, and | encoded | p6-statutory-rules: s 45E(1) |  |
| s 45E(1)(b) | 512 | (b) with the omission of any comma before or after the year in the sho | encoded | p6-statutory-rules: s 45E(1) |  |
| s 45E(1)(c) | 513 | (c) with the omission of inverted commas around the short title or cit | encoded | p6-statutory-rules: s 45E(1) |  |
| s 45E(1)(d) | 514 | (d) with other changes to the format (but not to the text) of legislat | encoded | p6-statutory-rules: s 45E(1) |  |
| s 45E(2) | 515-517 | (2) For the purposes of publication under this Part and for all other  | encoded | p6-statutory-rules: s 45E(2) |  |
| s 45E(2)(a) | 516 | (a) roman numerals in legislation may be regarded as being interchange | encoded | p6-statutory-rules: s 45E(2) |  |
| s 45E(2)(b) | 517 | (b) colons in legislation may be regarded as being interchangeable wit | encoded | p6-statutory-rules: s 45E(2) |  |
| Part 7 | 519 | Part 7 Exercise of statutory functions | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 46 | 521-527 | 46 Appointments may be made by name or by office | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 46(1) | 522-526 | (1) If an Act or instrument confers a power on any person or body— | encoded | p7-functions: s 46(1) |  |
| s 46(1)(a) | 523 | (a) to appoint a person to an office, | encoded | p7-functions: s 46(1) |  |
| s 46(1)(b) | 524 | (b) to appoint a person or body to exercise a function, or | encoded | p7-functions: s 46(1) |  |
| s 46(1)(c) | 525 | (c) to appoint a person or body to do any other thing, | encoded | p7-functions: s 46(1) |  |
| s 46(2) | 527 | (2) Any appointment of a particular officer or the holder of a particu | encoded | p7-functions: s 46(2) |  |
| s 47 | 529-541 | 47 Powers of appointment imply certain incidental powers | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 47(1) | 530-536 | (1) If an Act or instrument confers a power on any person or body to a | encoded | p7-functions: s 47(1)(a); s 47(1)(b) |  |
| s 47(1)(a) | 531 | (a) the power may be exercised from time to time, as occasion requires | encoded | p7-functions: s 47(1)(a); s 47(1)(b) |  |
| s 47(1)(b) | 532-536 | (b) the power includes— | encoded | p7-functions: s 47(1)(b) |  |
| s 47(1)(b)(i) | 533 | (i) power to remove or suspend, at any time, a person so appointed, | encoded | p7-functions: s 47(1)(b) |  |
| s 47(1)(b)(ii) | 534 | (ii) power to appoint some other person to act in the office of a pers | encoded | p7-functions: s 47(1)(b) |  |
| s 47(1)(b)(iii) | 535 | (iii) power to appoint a person to act in a vacant office, whether or  | encoded | p7-functions: s 47(1)(b) |  |
| s 47(1)(b)(iv) | 536 | (iv) power to appoint a person to act in the office of a person who is | encoded | p7-functions: s 47(1)(b) |  |
| s 47(2) | 537 | (2) The power to remove or suspend a person under subsection (1) (b) m | encoded | p7-functions: s 47(2) |  |
| s 47(3) | 538-541 | (3) The power to make an appointment under subsection (1) (b) may be e | encoded | p7-functions: s 47(3) |  |
| s 47(3)(a) | 539 | (a) as occasion requires, | encoded | p7-functions: s 47(3) |  |
| s 47(3)(b) | 540 | (b) in anticipation of a particular event, so as to provide that the a | encoded | p7-functions: s 47(3) |  |
| s 47(3)(c) | 541 | (c) in anticipation of a particular state of affairs, so as to provide | encoded | p7-functions: s 47(3) |  |
| s 48 | 543-545 | 48 Exercise of statutory functions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 48(1) | 544 | (1) If an Act or instrument confers or imposes a function on any perso | encoded | p7-functions: s 48(1) |  |
| s 48(2) | 545 | (2) If an Act or instrument confers or imposes a function on a particu | encoded | p7-functions: s 48(2) |  |
| s 49 | 547-565 | 49 Delegation of functions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 49(1) | 548 | (1) If an Act or instrument confers a power on any person or body to d | encoded | p7-functions: s 49(1) |  |
| s 49(2) | 549-552 | (2) A delegation— | encoded | p7-functions: s 49(2)(a); s 49(2)(b) (+1) |  |
| s 49(2)(a) | 550 | (a) may be general or limited, | encoded | p7-functions: s 49(2)(a); s 49(2)(b) (+1) |  |
| s 49(2)(b) | 551 | (b) shall be in, or be evidenced by, writing signed by the delegator o | encoded | p7-functions: s 49(2)(b); s 49(2)(c) |  |
| s 49(2)(c) | 552 | (c) may be revoked, wholly or partly, by the delegator. | encoded | p7-functions: s 49(2)(c) |  |
| s 49(3) | 553 | (3) A delegated function may be exercised only in accordance with any  | fork | p7-functions: s 49(3) | F9 |
| s 49(4) | 554 | (4) A delegate may, in the exercise of a delegated function, exercise  | encoded | p7-functions: s 49(4) |  |
| s 49(5) | 555 | (5) A delegated function that purports to have been exercised by a del | encoded | p7-functions: s 49(5) |  |
| s 49(6) | 556 | (6) A delegated function that is duly exercised by a delegate shall be | encoded | p7-functions: s 49(6) |  |
| s 49(7) | 557-560 | (7) If— | encoded | p7-functions: s 49(7) |  |
| s 49(7)(a) | 558 | (a) the exercise of a function by a person or body is, by virtue of an | encoded | p7-functions: s 49(7) |  |
| s 49(7)(b) | 559 | (b) the person or body has delegated the function to some other person | encoded | p7-functions: s 49(7) |  |
| s 49(8) | 561-563 | (8) If a function is delegated by or to a particular officer or the ho | encoded | p7-functions: s 49(8)(a); s 49(8)(b) |  |
| s 49(8)(a) | 562 | (a) the delegation does not cease to have effect merely because the pe | encoded | p7-functions: s 49(8)(a); s 49(8)(b) |  |
| s 49(8)(b) | 563 | (b) the person for the time being occupying or acting in the office co | encoded | p7-functions: s 49(8)(b) |  |
| s 49(9) | 564 | (9) A function that has been delegated may, notwithstanding the delega | encoded | p7-functions: s 49(9) |  |
| s 49(10) | 565 | (10) This section applies to a sub-delegation of a function in the sam | encoded | p7-functions: s 49(10) |  |
| Part 8 | 567 | Part 8 Statutory bodies | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 50 | 569-583 | 50 Statutory corporations | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 50(1) | 570-575 | (1) A statutory corporation— | encoded | p8-bodies: s 50(1) |  |
| s 50(1)(a) | 571 | (a) has perpetual succession, | encoded | p8-bodies: s 50(1) |  |
| s 50(1)(b) | 572 | (b) shall have a seal, | encoded | p8-bodies: s 50(1) |  |
| s 50(1)(c) | 573 | (c) may take proceedings and be proceeded against in its corporate nam | encoded | p8-bodies: s 50(1) |  |
| s 50(1)(d) | 574 | (d) may, for the purpose of enabling it to exercise its functions, pur | encoded | p8-bodies: s 50(1) |  |
| s 50(1)(e) | 575 | (e) may do and suffer all other things that bodies corporate may, by l | encoded | p8-bodies: s 50(1) |  |
| s 50(2) | 576-578 | (2) The seal of a statutory corporation (being a corporation that has  | fork | p8-bodies: s 50(2) custody; s 50(2) affixing | F9 |
| s 50(2)(a) | 577 | (a) in the presence of at least 2 members of the corporation, and | fork | p8-bodies: s 50(2) affixing | F9 |
| s 50(2)(b) | 578 | (b) with an attestation by the signatures of those members of the fact | fork | p8-bodies: s 50(2) affixing | F9 |
| s 50(3) | 579-582 | (3) Every document requiring authentication by a statutory corporation | encoded | p8-bodies: s 50(3) |  |
| s 50(3)(a) | 580 | (a) in the case of a corporation that has 2 or more members—if it is s | encoded | p8-bodies: s 50(3) |  |
| s 50(3)(b) | 581 | (b) in the case of a corporation sole—if it is signed by the person by | encoded | p8-bodies: s 50(3) |  |
| s 50(3)(c) | 582 | (c) in the case of a corporation that has no members—if it is signed b | encoded | p8-bodies: s 50(3) |  |
| s 50(4) | 583 | (4) This section applies to a statutory corporation in addition to, an | encoded | p8-bodies: s 50(4) |  |
| s 51 | 585 | 51 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 52 | 587-594 | 52 Proceedings of statutory bodies | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 52(1) | 588-593 | (1) Any act or proceeding of a statutory body shall not be called into | encoded | p8-bodies: s 52(1) |  |
| s 52(1)(a) | 589 | (a) any vacancies in the membership of the body, | encoded | p8-bodies: s 52(1) |  |
| s 52(1)(b) | 590 | (b) any defects in the appointment of any members of the body, | encoded | p8-bodies: s 52(1) |  |
| s 52(1)(c) | 591 | (c) any disqualifications of any members of the body, | encoded | p8-bodies: s 52(1) |  |
| s 52(1)(d) | 592 | (d) any minor irregularities in the manner in which any meetings of th | encoded | p8-bodies: s 52(1) |  |
| s 52(1)(e) | 593 | (e) the presence or participation at any meetings of the body of any p | encoded | p8-bodies: s 52(1) |  |
| s 52(2) | 594 | (2) This section applies to a statutory body in addition to, and witho | encoded | p8-bodies: s 52(2) |  |
| s 53 | 596-604 | 53 Alterations of names and constitutions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 53(1) | 597-599 | (1) If an Act or statutory rule alters the name of a body or office— | encoded | p8-bodies: s 53(1)(a); s 53(1)(b) |  |
| s 53(1)(a) | 598 | (a) the body or office continues in existence under its new name so th | encoded | p8-bodies: s 53(1)(a); s 53(1)(b) |  |
| s 53(1)(b) | 599 | (b) a reference in any Act or instrument, or in any other document, to | encoded | p8-bodies: s 53(1)(b) |  |
| s 53(2) | 600-604 | (2) If an Act or statutory rule alters the constitution of a body— | encoded | p8-bodies: s 53(2) |  |
| s 53(2)(a) | 601 | (a) the body continues in existence as newly constituted so that its i | encoded | p8-bodies: s 53(2) |  |
| s 53(2)(b) | 602 | (b) the alteration does not affect any functions of the body, | encoded | p8-bodies: s 53(2) |  |
| s 53(2)(c) | 603 | (c) the alteration does not affect any legal or other proceedings inst | encoded | p8-bodies: s 53(2); s 53(2)(c) continuation |  |
| s 53(2)(d) | 604 | (d) the alteration does not affect any investigation or inquiry being  | encoded | p8-bodies: s 53(2); s 53(2)(d) continuation |  |
| s 53A | 606-620 | 53A Extension of age limit for part-time members of statutory bodies | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 53A(1) | 607-612 | (1) If— | encoded | p8-bodies: s 53A(1) |  |
| s 53A(1)(a) | 608 | (a) a person is or has, within the last 3 months, been the holder of a | encoded | p8-bodies: s 53A(1) |  |
| s 53A(1)(b) | 609 | (b) the person cannot be re-appointed to the office because a provisio | encoded | p8-bodies: s 53A(1) |  |
| s 53A(1)(c) | 610 | (c) a Minister certifies to the Governor that that Minister is of the  | encoded | p8-bodies: s 53A(1) |  |
| s 53A(1)(d) | 611 | (d) the person has reached the age limit or is within 3 months of reac | encoded | p8-bodies: s 53A(1) |  |
| s 53A(2) | 613 | (2) While under the extended age limit, the person (if otherwise quali | encoded | p8-bodies: s 53A(2) |  |
| s 53A(3) | 614 | (3) An office held by a person re-appointed under this section becomes | encoded | p8-bodies: s 53A(3) |  |
| s 53A(4) | 615 | (4) This section prevails over any Act or statutory rule relating to t | encoded | p8-bodies: s 53A(4) |  |
| s 53A(5) | 616 | (5) A notification in the Gazette by a Minister to the effect that the | encoded | p8-bodies: s 53A(5) |  |
| s 53A(6) | 617 | (6) The age limit for a person may be extended under this section on m | encoded | p8-bodies: s 53A(6) |  |
| s 53A(7) | 618-620 |  | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 53A(7)(a) | 619 | (a) an office required to be held on a full-time basis, or | encoded | p8-bodies: s 53A(7) |  |
| s 53A(7)(b) | 620 | (b) an office specified in any of the Schedules to the Statutory and O | encoded | p8-bodies: s 53A(7) |  |
| Part 9 | 622 | Part 9 | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 54 | 623 | 54–57 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 55 | 623 | 54–57 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 56 | 623 | 54–57 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 57 | 623 | 54–57 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| Part 10 | 625 | Part 10 Application of State laws to coastal waters | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 58 | 627-634 | s 58 Definitions | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 58(a) | 631 | (a) the part or parts of the territorial sea of Australia that is or a | encoded | p10-coastal: s 58 coastal waters of the State |  |
| s 58(b) | 632 | (b) any sea that is on the landward side of any part of the territoria | encoded | p10-coastal: s 58 coastal waters of the State |  |
| s 59 | 636-640 | s 59 Application of laws of the State to coastal waters | encoded | p10-coastal: s 59 |  |
| s 59(a) | 638 | (a) the coastal waters of the State, and | encoded | p10-coastal: s 59 |  |
| s 59(b) | 639 | (b) the sea-bed and subsoil beneath, and the airspace above, the coast | encoded | p10-coastal: s 59 |  |
| s 60 | 642-647 | 60 Laws with specific application not to apply | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 60(1) | 643-646 | (1) Nothing in this Part renders a provision of the laws of the State  | encoded | p10-coastal: s 60(1) |  |
| s 60(1)(a) | 644 | (a) in so far as the provision is incapable of applying in or in relat | encoded | p10-coastal: s 60(1) |  |
| s 60(1)(b) | 645 | (b) if those laws expressly provide that the provision does not extend | encoded | p10-coastal: s 60(1) |  |
| s 60(1)(c) | 646 | (c) if those laws expressly provide that the provision applies only in | encoded | p10-coastal: s 60(1) |  |
| s 60(2) | 647 | (2) A provision of the laws of the State shall not be taken to be a pr | encoded | p10-coastal: s 60(2) |  |
| s 61 | 649-651 | 61 Extent of jurisdiction in relation to coastal waters | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 61(1) | 650 | (1) All persons who have functions conferred or imposed on them by law | encoded | p10-coastal: s 61(1) |  |
| s 61(2) | 651 | (2) The several courts of the State are invested with jurisdiction in  | encoded | p10-coastal: s 61(2) |  |
| s 62 | 653-654 | s 62 Constitutional basis | encoded | p10-coastal: s 62 |  |
| s 63 | 656-657 | s 63 Saving | encoded | p10-coastal: s 63 |  |
| Part 11 | 659 | Part 11 Miscellaneous | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 64 | 661-662 | s 64 Every section of an Act a substantive enactment | encoded | p11-misc: s 64 |  |
| s 64A | 664-665 | s 64A Schedules | encoded | p11-misc: s 64A |  |
| s 65 | 667-668 | s 65 References to Acts generally | encoded | p11-misc: s 65 |  |
| s 66 | 670-687 | 66 Citation of particular Acts | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 66(1) | 671-675 | (1) An Act may be cited— | encoded | p11-misc: s 66(1) |  |
| s 66(1)(a) | 672 | (a) by its short title (or name), or | encoded | p11-misc: s 66(1) |  |
| s 66(1)(b) | 673-675 | (b) by reference to— | encoded | p11-misc: s 66(1) |  |
| s 66(1)(b)(i) | 674 | (i) the year in which it was passed or, in the case of an Act passed b | encoded | p11-misc: s 66(1) |  |
| s 66(1)(b)(ii) | 675 | (ii) its number. | encoded | p11-misc: s 66(1) |  |
| s 66(2) | 676-679 | (2) A Commonwealth Act may be cited— | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(2)(a) | 677 | (a) by its short title (or name), or | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(2)(b) | 678 | (b) in such other manner as is sufficient in a Commonwealth Act, | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(3) | 680-683 | (3) An Act or Ordinance of some other State or Territory may be cited— | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(3)(a) | 681 | (a) by its short title (or name), or | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(3)(b) | 682 | (b) in such other manner as is sufficient in an Act or Ordinance of th | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(4) | 684-687 | (4) A British Act may be cited— | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(4)(a) | 685 | (a) by its short title (or name), or | encoded | p11-misc: s 66(2) to (4) |  |
| s 66(4)(b) | 686 | (b) in such other manner as is sufficient in a British Act, | encoded | p11-misc: s 66(2) to (4) |  |
| s 67 | 689-708 | 67 Citation of instruments etc | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 67(1) | 690-696 | (1) An instrument may be referred to— | encoded | p11-misc: s 67(1) |  |
| s 67(1)(a) | 691 | (a) by its citation (or name), or | encoded | p11-misc: s 67(1) |  |
| s 67(1)(b) | 692-696 | (b) by reference to— | encoded | p11-misc: s 67(1) |  |
| s 67(1)(b)(i) | 693 | (i) in the case of an instrument that has been published in a printed  | encoded | p11-misc: s 67(1) |  |
| s 67(1)(b)(ia) | 694 | (ia) in the case of an instrument that has been published on the NSW l | encoded | p11-misc: s 67(1) |  |
| s 67(1)(b)(ii) | 695 | (ii) in any other case—the date on which it was made, | encoded | p11-misc: s 67(1) |  |
| s 67(2) | 697-700 | (2) An instrument made under a Commonwealth Act may be referred to— | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(2)(a) | 698 | (a) by its citation (or name), or | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(2)(b) | 699 | (b) in such other manner as is sufficient in a Commonwealth Act, | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(3) | 701-704 | (3) An instrument made under an Act or Ordinance of some other State o | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(3)(a) | 702 | (a) by its citation (or name), or | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(3)(b) | 703 | (b) in such other manner as is sufficient in an Act or Ordinance of th | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(4) | 705-708 | (4) An instrument made under a British Act may be referred to— | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(4)(a) | 706 | (a) by its citation (or name), or | encoded | p11-misc: s 67(2) to (4) |  |
| s 67(4)(b) | 707 | (b) in such other manner as is sufficient in a British Act, | encoded | p11-misc: s 67(2) to (4) |  |
| s 68 | 710-733 | 68 References to amended or repealed Acts and instruments | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 68(1) | 711 | (1) In any Act or instrument, a reference to some other Act or instrum | encoded | p11-misc: s 68(1) |  |
| s 68(2) | 712-714 | (2) Subsection (1) applies to a reference to an Act or instrument— | encoded | p11-misc: s 68(2) |  |
| s 68(2)(a) | 713 | (a) whether or not the reference includes a reference to subsequent am | encoded | p11-misc: s 68(2) |  |
| s 68(2)(b) | 714 | (b) whether or not the reference is to a mode of citation that include | encoded | p11-misc: s 68(2) |  |
| s 68(3) | 715-718 | (3) Notwithstanding subsection (1), in any Act or instrument— | encoded | p11-misc: s 68(3) |  |
| s 68(3)(a) | 716 | (a) a reference to an Act that has been repealed and re-enacted, with  | encoded | p11-misc: s 68(3) |  |
| s 68(3)(b) | 717 | (b) a reference to an instrument that has been repealed and re-made, w | encoded | p11-misc: s 68(3) |  |
| s 68(3A) | 719 | (3A) Nothing in this section affects the operation of sections 11 and  | encoded | p11-misc: s 68(3A) |  |
| s 68(4) | 720-732 | (4) In this section— | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a) | 721-731 | (a) a reference to an Act includes a reference to— | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(i) | 722 | (i) a Commonwealth Act, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(ii) | 723 | (ii) an Act or Ordinance of some other State or Territory, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(iii) | 724 | (iii) a British Act, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(iv) | 725 | (iv) the Companies (New South Wales) Code, the Companies (Acquisition  | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(v) | 726 | (v) the ASIC Law of New South Wales, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(vi) | 727 | (vi) the Corporations Law of New South Wales, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(vii) | 728 | (vii) the AFIC (NSW) Code and the Financial Institutions (NSW) Code, a | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(viia) | 729 | (viia) the National Electricity (NSW) Law, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(viii) | 730 | (viii) the Friendly Societies (NSW) Code, and | encoded | p11-misc: s 68(4) |  |
| s 68(4)(a)(ix) | 731 | (ix) the National Gas (NSW) Law, | encoded | p11-misc: s 68(4) |  |
| s 68(4)(b) | 732 | (b) a reference to an instrument includes a reference to an instrument | encoded | p11-misc: s 68(4); s 68(4)(b) |  |
| s 68(5) | 733 | (5) This section extends to a reference to a repealed Act or instrumen | encoded | p11-misc: s 68(5) |  |
| s 69 | 735-741 | 69 References to publications other than Acts or instruments | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 69(1) | 736-738 | (1) In any Act or instrument, a reference to a publication other than  | encoded | p11-misc: s 69(1) |  |
| s 69(1)(a) | 737 | (a) if a particular day is specified for that purpose in the Act or in | encoded | p11-misc: s 69(1) |  |
| s 69(1)(b) | 738 | (b) in any other case—as in force or current on the day on which the p | encoded | p11-misc: s 69(1) |  |
| s 69(2) | 739-741 | (2) Notwithstanding subsection (1), a reference in any Act or instrume | encoded | p11-misc: s 69(2) |  |
| s 69(2)(a) | 740 | (a) if that intention appears in the Act or instrument, and | encoded | p11-misc: s 69(2) |  |
| s 69(2)(b) | 741 | (b) where that intention appears in the instrument—if the Act under wh | encoded | p11-misc: s 69(2) |  |
| s 69A | 743-746 | s 69A Evidence of publication of Australian standards or other publica | encoded | p11-misc: s 69A |  |
| s 69A(a) | 745 | (a) by the production of a document purporting to be a copy of it and  | encoded | p11-misc: s 69A |  |
| s 69A(b) | 746 | (b) by the production of a document purporting to be a copy of it and  | encoded | p11-misc: s 69A |  |
| s 69B | 748 | 69B (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 70 | 750-751 | s 70 References to changed short titles, names and citations | encoded | p11-misc: s 70 |  |
| s 71 | 753-754 | s 71 Time of expiry of temporary Acts and instruments | fork | interpretation-time: s 71 | F11 |
| s 72 | 756-758 | 72 Retrospective commencement of continuing Acts | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 72(1) | 757 | (1) If a Bill for an Act to continue a temporary Act has been introduc | encoded | p11-misc: s 72(1) |  |
| s 72(2) | 758 | (2) This section does not make any person liable to any penalty for or | encoded | p11-misc: s 72(2) |  |
| s 73 | 760-767 | 73 Private Acts not to affect rights of the Crown etc | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 73(1) | 761-763 | (1) A Private Act that is passed after the commencement of this Act sh | encoded | p11-misc: s 73(1)(a); s 73(1)(b) |  |
| s 73(1)(a) | 762 | (a) to affect, in a manner prejudicial to the Crown or any other perso | encoded | p11-misc: s 73(1)(a); s 73(1)(b) |  |
| s 73(1)(b) | 763 | (b) to impose liabilities on the Crown or any other person (other than | encoded | p11-misc: s 73(1)(b) |  |
| s 73(2) | 764-767 | (2) Without limiting the effect of section 30— | encoded | p11-misc: s 73(2) |  |
| s 73(2)(a) | 765 | (a) the provisions of section 17 of the Act 16 Victoria No 1 (the Acts | encoded | p11-misc: s 73(2) |  |
| s 73(2)(b) | 766 | (b) the provisions of section 14 of the Interpretation Act 1897 contin | encoded | p11-misc: s 73(2) |  |
| s 74 | 769-770 | s 74 Private Acts amended by Public Acts do not thereby become Public  | encoded | p11-misc: s 74 |  |
| s 75 | 772-778 | s 75 Publication of statutory notices | encoded | p11-misc: s 75 |  |
| s 75(a) | 774 | (a) the notice or advertisement is published in the Gazette, and | encoded | p11-misc: s 75 |  |
| s 75(b) | 775-778 | (b) there is published in each newspaper or other location— | encoded | p11-misc: s 75 |  |
| s 75(b)(i) | 776 | (i) a summary of the notice or advertisement, or | encoded | p11-misc: s 75 |  |
| s 75(b)(ii) | 777 | (ii) a statement to the effect that the notice or advertisement has be | encoded | p11-misc: s 75 |  |
| s 76 | 780-788 | 76 Service by post | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 76(1) | 781-784 | (1) If an Act or instrument authorises or requires any document to be  | encoded | p11-misc: s 76(1)(a); s 76(1)(b) (+1) |  |
| s 76(1)(a) | 782 | (a) may be effected by properly addressing, prepaying and posting a le | encoded | p11-misc: s 76(1)(a); s 76(1)(b) (+1) |  |
| s 76(1)(b) | 783 | (b) in Australia or in an external Territory—is, unless evidence suffi | encoded | interpretation-time: s 76(1)(b) / p11-misc: s 76(1)(b); s 76(1)(c) |  |
| s 76(1)(c) | 784 | (c) in another place—is, unless evidence sufficient to raise doubt is  | encoded | p11-misc: s 76(1)(c) |  |
| s 76(2) | 785-788 | (2) In this section— | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 76(2)(a) | 787 | (a) a Saturday or Sunday, or | encoded | interpretation-time: s 76(2) |  |
| s 76(2)(b) | 788 | (b) a public holiday or a bank holiday in the place to which the lette | encoded | interpretation-time: s 76(2) |  |
| s 77 | 790-796 | 77 Registered post etc not necessary in the case of Acts and statutory | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 77(1) | 791 | (1) Any Act or statutory rule under which a document (other than a sum | encoded | p11-misc: s 77 |  |
| s 77(2) | 792-794 | (2) Subsection (1)— | encoded | p11-misc: s 77 |  |
| s 77(2)(a) | 793 | (a) applies only to Acts and statutory rules enacted or made before 24 | encoded | p11-misc: s 77 |  |
| s 77(2)(b) | 794 | (b) so applies notwithstanding any provision of any such Act or statut | encoded | p11-misc: s 77 |  |
| s 77(3) | 795 | (3) The Governor may, by order published in the Gazette, declare that  | encoded | p11-misc: s 77; s 77(3) |  |
| s 77(4) | 796 | (4) An order in force under subsection (3) does not affect the operati | encoded | p11-misc: s 77 |  |
| s 78 | 798-803 | 78 Rules of court | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 78(1) | 799 | (1) The power of a person or body to make rules of court includes powe | encoded | p11-misc: s 78(1) |  |
| s 78(2) | 800-803 | (2) If an Act or statutory rule— | encoded | p11-misc: s 78(2) |  |
| s 78(2)(a) | 801 | (a) confers any jurisdiction on a court or tribunal, or | encoded | p11-misc: s 78(2) |  |
| s 78(2)(b) | 802 | (b) extends or varies the jurisdiction of a court or tribunal, | encoded | p11-misc: s 78(2) |  |
| s 79 | 805-808 | s 79 Authority to administer oaths | encoded | p11-misc: s 79 |  |
| s 79(a) | 807 | (a) to receive evidence, and | encoded | p11-misc: s 79 |  |
| s 79(b) | 808 | (b) to examine witnesses, and to administer oaths to witnesses, who ha | encoded | p11-misc: s 79 |  |
| s 80 | 810-814 | 80 Compliance with forms | encoded | heading or opening words only; the text is in the sub-rows |  |
| s 80(1) | 811 | (1) If a form is prescribed by, or approved under, an Act or statutory | encoded | p11-misc: s 80(1) strict compliance; s 80(1) substantial compliance |  |
| s 80(2) | 812 | (2) If a form prescribed by, or approved under, an Act or instrument r | fork | p11-misc: s 80(2) | F9 |
| s 80(3) | 813 | (3) Without limiting the generality of subsections (1) and (2), in any | encoded | p11-misc: s 80(3) |  |
| s 80(4) | 814 | (4) If an Act or statutory rule requires anything to be in a form pres | encoded | p11-misc: s 80(4) |  |
| s 80A | 816-820 | s 80A Maximum monetary penalty Local Court may impose in certain circu | encoded | p11-misc: s 80A |  |
| s 80A(a) | 818 | (a) provides that an offence under the Act may be dealt with summarily | encoded | p11-misc: s 80A |  |
| s 80A(b) | 819 | (b) imposes a limit by reference solely to an amount of money (however | encoded | p11-misc: s 80A |  |
| s 81 | 822 | 81 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 82 | 824-825 | s 82 Repeals | encoded | p11-misc: s 82 |  |
| s 83 | 827-828 | s 83 Savings and transitional provisions | encoded | p11-misc: s 83 |  |
| Part 12 | 830 | Part 12 | inert (1: not operative) | Part heading, held as data in provisions |  |
| s 84 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 85 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 86 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 87 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 88 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 89 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 90 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| s 91 | 831 | 84–91 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| Schedule 1 | 833 | Schedule 1 Greater Sydney Region | inert (1: not operative) | Schedule heading, held as data in provisions |  |
| Schedule 1 clause 1 | 835-869 | Schedule 1 clause 1 Composition of Greater Sydney Region | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(a) | 837 | (a) Bayside, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(b) | 838 | (b) City of Blacktown, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(c) | 839 | (c) City of Blue Mountains, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(d) | 840 | (d) Burwood, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(e) | 841 | (e) Canada Bay, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(f) | 842 | (f) Canterbury-Bankstown, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(g) | 843 | (g) Camden, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(h) | 844 | (h) City of Campbelltown, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(i) | 845 | (i) Cumberland, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(j) | 846 | (j) City of Fairfield, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(k) | 847 | (k) Georges River, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(l) | 848 | (l) City of Hawkesbury, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(m) | 849 | (m) Hornsby, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(n) | 850 | (n) Hunter's Hill, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(o) | 851 | (o) Inner West, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(p) | 852 | (p) Ku-ring-gai, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(q) | 853 | (q) Lane Cove, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(r) | 854 | (r) City of Liverpool, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(s) | 855 | (s) Mosman, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(t) | 856 | (t) North Sydney, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(u) | 857 | (u) Northern Beaches, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(v) | 858 | (v) City of Parramatta, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(w) | 859 | (w) City of Penrith, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(x) | 860 | (x) City of Randwick, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(y) | 861 | (y) City of Ryde, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(z) | 862 | (z) Strathfield, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(za) | 863 | (za) City of Sydney, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(zb) | 864 | (zb) Sutherland Shire, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(zc) | 865 | (zc) The Hills Shire, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(zd) | 866 | (zd) Waverley, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(ze) | 867 | (ze) City of Willoughby, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(zf) | 868 | (zf) Wollondilly, | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 1(zg) | 869 | (zg) Woollahra. | encoded | schedules: Schedule 1 clause 1 |  |
| Schedule 1 clause 2 | 871-874 | Schedule 1 clause 2 Amendment of area comprising Greater Sydney Region | inert (2: machinery) | regulation-making power to amend clause 1 |  |
| Schedule 1 clause 2(a) | 873 | (a) to extend or reduce the Greater Sydney Region, or | inert (2: machinery) | regulation-making power to amend clause 1 |  |
| Schedule 1 clause 2(b) | 874 | (b) to rename a local government area. | inert (2: machinery) | regulation-making power to amend clause 1 |  |
| Schedule 2 | 876 | Schedule 2 Repeals | inert (1: not operative) | Schedule heading, held as data in provisions |  |
| Schedule 3 | 891 | Schedule 3 Savings and transitional provisions | inert (1: not operative) | Schedule heading, held as data in provisions |  |
| Schedule 3 clause 1 | 894-897 | 1 Commencement of certain Acts | encoded | heading or opening words only; the text is in the sub-rows |  |
| Schedule 3 clause 1(1) | 895 | (1) Section 3 (II) of the Interpretation Act 1897 continues to apply t | encoded | schedules: Schedule 3 clause 1 |  |
| Schedule 3 clause 1(2) | 896-897 | (2) In this clause— | encoded | schedules: Schedule 3 clause 1 |  |
| Schedule 3 clause 2 | 899-900 | Schedule 3 clause 2 Orders under sec 27 (III) of the Interpretation Ac | encoded | schedules: Schedule 3 clause 2 |  |
| Schedule 3 clause 3 | 902-903 | Schedule 3 clause 3 Instruments under sec 37 of the Interpretation Act | encoded | schedules: Schedule 3 clause 3 |  |
| Schedule 3 clause 4 | 905-906 | Schedule 3 clause 4 Regulations under sec 41 of the Interpretation Act | encoded | schedules: Schedule 3 clause 4 |  |
| Schedule 3 clause 5 | 908-909 | Schedule 3 clause 5 References to the tabling of statutory rules | encoded | schedules: Schedule 3 clause 5 |  |
| Schedule 3 clause 6 | 911-912 | Schedule 3 clause 6 Ordinances under sec 577 of the Local Government A | encoded | schedules: Schedule 3 clause 6 |  |
| Schedule 3 clause 7 | 914-917 | 7 Statutory bodies representing the Crown | encoded | heading or opening words only; the text is in the sub-rows |  |
| Schedule 3 clause 7(1) | 915 | (1) Section 13A, as inserted by the Interpretation Amendment Act 2006, | encoded | schedules: Schedule 3 clause 7(1) |  |
| Schedule 3 clause 7(2) | 916 | (2) Nothing in subclause (1) affects any judgment or other order of a  | encoded | schedules: Schedule 3 clause 7(2) |  |
| Schedule 3 clause 7(3) | 917 | (3) In particular, the Roads and Traffic Authority is bound by the Lan | encoded | schedules: Schedule 3 clause 7(3) |  |
| Schedule 3 clause 8 | 919-920 | Schedule 3 clause 8 Repeal of Reprints Act 1972—saving of certificates | encoded | schedules: Schedule 3 clause 8 |  |
| Schedule 3 clause 9 | 922-924 | 9 Construction of references to publication in Gazette where instrumen | encoded | heading or opening words only; the text is in the sub-rows |  |
| Schedule 3 clause 9(1) | 923 | (1) This clause applies to statutory rules and other instruments that  | encoded | schedules: Schedule 3 clause 9 |  |
| Schedule 3 clause 9(2) | 924 | (2) In any Act or instrument, a reference to the publication in the Ga | encoded | schedules: Schedule 3 clause 9 |  |
| Schedule 3 clause 10 | 926 | 10 (Repealed) | repealed or blank in this text | printed "(Repealed)" |  |
| Schedule 3 clause 11 | 928-930 | 11 References to offences—section 21 (3) | encoded | heading or opening words only; the text is in the sub-rows |  |
| Schedule 3 clause 11(1) | 929 | (1) Section 21 (3), as inserted by the Crimes Legislation Amendment Ac | encoded | schedules: Schedule 3 clause 11(1) |  |
| Schedule 3 clause 11(2) | 930 | (2) Nothing in subclause (1) affects any judgment or other order of a  | encoded | schedules: Schedule 3 clause 11(2) |  |
| Schedule 3 clause 12 | 932-937 | 12 Acts Printed by the NSW Government Printer | encoded | heading or opening words only; the text is in the sub-rows |  |
| Schedule 3 clause 12(1) | 933 | (1) This clause applies to Acts printed by the Government Printer befo | encoded | schedules: Schedule 3 clause 12(2); Schedule 3 clause 12(3) |  |
| Schedule 3 clause 12(2) | 934 | (2) The date purporting to be the date of assent, as appearing on the  | encoded | schedules: Schedule 3 clause 12(2); Schedule 3 clause 12(3) |  |
| Schedule 3 clause 12(3) | 935 | (3) All matters not forming part of the Act that are set out in the do | encoded | schedules: Schedule 3 clause 12(3) |  |
| Schedule 3 clause 12(4) | 936-937 | (4) In this clause— | encoded | schedules: Schedule 3 clause 12(4) |  |
| Schedule 4 | 939 | Schedule 4 Dictionary | inert (1: not operative) | Schedule heading, held as data in provisions |  |
| Schedule 2 row 1 | 878 | Acts Shortening Act of 1852 16 Vic No 1—the unrepealed portion | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 2 | 879 | Acts Shortening Act of 1858 22 Vic No 12—the unrepealed portion | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 3 | 880 | Interpretation Act 1897 No 4—the whole Act | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 4 | 881 | Crimes Act 1900 No 40—so much of the First Schedule as amends Act 16 V | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 5 | 882 | Fines and Penalties Act 1901 No 16—so much of the Schedule as amends A | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 6 | 883 | Justices Act 1902 No 27—so much of the First Schedule as amends Act 16 | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 7 | 884 | Local Government Act 1919 No 41—sections 577 and 579 and the words "by | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 8 | 885 | Publication of Statutory Advertisements and Notices Act 1920 No 32—the | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 9 | 886 | Minors (Property and Contracts) Act 1970 No 60—so much of the First Sc | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 10 | 887 | Miscellaneous Acts (Local Courts) Amendment Act 1982 No 168—so much of | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 11 | 888 | Statute Law (Miscellaneous Amendments) Act 1984 No 153—Schedule 7 | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 2 row 12 | 889 | Statute Law (Miscellaneous Provisions) Act 1985 No 231—Schedule 11 | inert (2: machinery) | repeal of another Act (Schedule 2, applied by s 82) |  |
| Schedule 4 'affidavit' | 940 | affidavit, in the case of persons for the time being allowed by law to | encoded | definitions: Schedule 4 includes: affidavit / dictionary: Schedule 4, affidavit, in the case of persons for the time being allowed by law to affirm, declare or promise |  |
| Schedule 4 'Ageing and Disability Commissioner' | 941 | Ageing and Disability Commissioner means the Ageing and Disability Com | encoded | dictionary: Schedule 4, Ageing and Disability Commissioner |  |
| Schedule 4 'Ambulance Service of NSW' | 942 | Ambulance Service of NSW means the Ambulance Service of NSW under the  | encoded | dictionary: Schedule 4, Ambulance Service of NSW |  |
| Schedule 4 'amend' | 943 | amend, in relation to an Act or instrument, includes alter and vary. | encoded | definitions: Schedule 4 includes: amend / dictionary: Schedule 4, amend, in relation to an Act or instrument |  |
| Schedule 4 'Anti-Discrimination Board' | 944 | Anti-Discrimination Board means the Anti-Discrimination Board under th | encoded | dictionary: Schedule 4, Anti-Discrimination Board |  |
| Schedule 4 'Auditor-General' | 945 | Auditor-General means the Auditor-General under the Government Sector  | encoded | dictionary: Schedule 4, Auditor-General |  |
| Schedule 4 'ASC Law' | 946 | ASC Law has the same meaning as ASIC Law. | encoded | dictionary: Schedule 4, ASC Law |  |
| Schedule 4 'ASC Regulations' | 947 | ASC Regulations has the same meaning as ASIC Regulations when used in  | encoded | dictionary: Schedule 4, ASC Regulations |  |
| Schedule 4 'ASIC Law' | 948 | ASIC Law has the meaning provided for by Part 11 of the Corporations ( | encoded | dictionary: Schedule 4, ASIC Law |  |
| Schedule 4 'ASIC Regulations' | 949-951 | ASIC Regulations— | encoded | dictionary: Schedule 4, ASIC Regulations |  |
| Schedule 4 'ASIC Regulations'(a) | 950 | (a) when used in relation to the ASIC Law, has the meaning provided fo | encoded | dictionary: Schedule 4, ASIC Regulations |  |
| Schedule 4 'ASIC Regulations'(b) | 951 | (b) when used in relation to the Australian Securities and Investments | encoded | dictionary: Schedule 4, ASIC Regulations |  |
| Schedule 4 'Australia' | 952 | Australia means the Commonwealth of Australia but, when used in a geog | encoded | definitions: Schedule 4 Australia in a geographical sense / dictionary: Schedule 4, Australia |  |
| Schedule 4 'Australia Acts' | 953 | Australia Acts means the Australia Act 1986 of the Commonwealth and th | encoded | dictionary: Schedule 4, Australia Acts |  |
| Schedule 4 'Australian lawyer' | 954 | Australian lawyer means a person admitted to the Australian legal prof | encoded | dictionary: Schedule 4, Australian lawyer |  |
| Schedule 4 'Australian legal practitioner' | 955 | Australian legal practitioner means an Australian lawyer who holds a c | encoded | dictionary: Schedule 4, Australian legal practitioner |  |
| Schedule 4 'authorised deposit-taking institution or ADI' | 956 | authorised deposit-taking institution or ADI means an authorised depos | encoded | dictionary: Schedule 4, authorised deposit-taking institution or ADI |  |
| Schedule 4 'bank' | 957-959 | bank means— | encoded | dictionary: Schedule 4, bank |  |
| Schedule 4 'bank'(a) | 958 | (a) a bank as defined by section 5 of the Banking Act 1959 of the Comm | encoded | dictionary: Schedule 4, bank |  |
| Schedule 4 'bank'(b) | 959 | (b) a bank constituted under a law of a State or Territory. | encoded | dictionary: Schedule 4, bank |  |
| Schedule 4 'British Act or Imperial Act' | 960 | British Act or Imperial Act means an Act of the British Parliament. | encoded | dictionary: Schedule 4, British Act or Imperial Act |  |
| Schedule 4 'British Parliament or Imperial Parliament' | 961-966 | British Parliament or Imperial Parliament means— | encoded | definitions: Schedule 4 British Parliament / dictionary: Schedule 4, British Parliament or Imperial Parliament |  |
| Schedule 4 'British Parliament or Imperial Parliament'(a) | 962 | (a) the Parliament of England, | encoded | definitions: Schedule 4 British Parliament / dictionary: Schedule 4, British Parliament or Imperial Parliament |  |
| Schedule 4 'British Parliament or Imperial Parliament'(b) | 963 | (b) the Parliament of Great Britain, | encoded | definitions: Schedule 4 British Parliament / dictionary: Schedule 4, British Parliament or Imperial Parliament |  |
| Schedule 4 'British Parliament or Imperial Parliament'(c) | 964 | (c) the Parliament of the United Kingdom of Great Britain and Ireland, | encoded | definitions: Schedule 4 British Parliament / dictionary: Schedule 4, British Parliament or Imperial Parliament |  |
| Schedule 4 'British Parliament or Imperial Parliament'(d) | 965 | (d) the Parliament of the United Kingdom of Great Britain and Northern | encoded | definitions: Schedule 4 British Parliament / dictionary: Schedule 4, British Parliament or Imperial Parliament |  |
| Schedule 4 'business day' | 967-969 | business day means a day that is not— | encoded | dictionary: Schedule 4, business day / interpretation-time: Schedule 4, business day |  |
| Schedule 4 'business day'(a) | 968 | (a) a Saturday or Sunday, or | encoded | dictionary: Schedule 4, business day / interpretation-time: Schedule 4, business day |  |
| Schedule 4 'business day'(b) | 969 | (b) a public holiday or bank holiday throughout the State. | encoded | dictionary: Schedule 4, business day / interpretation-time: Schedule 4, business day |  |
| Schedule 4 'calendar month' | 970-972 | calendar month means a period commencing at the beginning of a day of  | fork | dictionary: Schedule 4, calendar month / interpretation-time: Schedule 4, calendar month; Schedule 4, calendar month and calendar year; s 36(1) | F1 |
| Schedule 4 'calendar month'(a) | 971 | (a) immediately before the beginning of the corresponding day of the n | fork | dictionary: Schedule 4, calendar month / interpretation-time: Schedule 4, calendar month; Schedule 4, calendar month and calendar year; s 36(1) | F1 |
| Schedule 4 'calendar month'(b) | 972 | (b) if there is no such corresponding day, at the end of the next name | fork | dictionary: Schedule 4, calendar month / interpretation-time: Schedule 4, calendar month; Schedule 4, calendar month and calendar year; s 36(1) | F1 |
| Schedule 4 'calendar year' | 973 | calendar year means a period of 12 months commencing on 1 January. | fork | dictionary: Schedule 4, calendar year / interpretation-time: Schedule 4, calendar month and calendar year; s 36(1); Schedule 4, calendar year; s 36(1) | F3 |
| Schedule 4 'Chief Commissioner of State Revenue' | 974 | Chief Commissioner of State Revenue means the Chief Commissioner of St | encoded | dictionary: Schedule 4, Chief Commissioner of State Revenue |  |
| Schedule 4 'Children's Court' | 975 | Children's Court means the Children's Court of New South Wales under t | encoded | dictionary: Schedule 4, Children's Court |  |
| Schedule 4 'Children's Guardian' | 976 | Children's Guardian means the Children's Guardian under the Children's | encoded | dictionary: Schedule 4, Children's Guardian |  |
| Schedule 4 'Civil and Administrative Tribunal' | 977 | Civil and Administrative Tribunal means the Civil and Administrative T | encoded | dictionary: Schedule 4, Civil and Administrative Tribunal |  |
| Schedule 4 'Commissioner of Fire and Rescue NSW' | 978 | Commissioner of Fire and Rescue NSW means the Commissioner under the F | encoded | dictionary: Schedule 4, Commissioner of Fire and Rescue NSW |  |
| Schedule 4 'Commissioner of Police' | 979 | Commissioner of Police means the Commissioner of Police under the Poli | encoded | dictionary: Schedule 4, Commissioner of Police |  |
| Schedule 4 'committal proceedings' | 980 | committal proceedings means proceedings before a Magistrate for the pu | encoded | dictionary: Schedule 4, committal proceedings |  |
| Schedule 4 'Commonwealth' | 981 | Commonwealth means the Commonwealth of Australia but, when used in a g | encoded | definitions: Schedule 4 Commonwealth in a geographical sense / dictionary: Schedule 4, Commonwealth |  |
| Schedule 4 'Commonwealth Constitution' | 982 | Commonwealth Constitution means the Constitution of the Commonwealth. | encoded | dictionary: Schedule 4, Commonwealth Constitution |  |
| Schedule 4 'Consolidated Fund' | 983 | Consolidated Fund means the fund formed as referred to in section 39 o | encoded | dictionary: Schedule 4, Consolidated Fund |  |
| Schedule 4 'contravene' | 984 | contravene includes fail to comply with. | encoded | definitions: Schedule 4 includes: contravene / dictionary: Schedule 4, contravene |  |
| Schedule 4 'Corporations Law' | 985 | Corporations Law has the meaning provided for by Part 3 of the Corpora | encoded | dictionary: Schedule 4, Corporations Law |  |
| Schedule 4 'Corporations legislation' | 986 | Corporations legislation means the Corporations legislation to which P | encoded | dictionary: Schedule 4, Corporations legislation |  |
| Schedule 4 'Corporations Regulations' | 987-989 | Corporations Regulations— | encoded | dictionary: Schedule 4, Corporations Regulations |  |
| Schedule 4 'Corporations Regulations'(a) | 988 | (a) when used in relation to the Corporations Law, has the meaning pro | encoded | dictionary: Schedule 4, Corporations Regulations |  |
| Schedule 4 'Corporations Regulations'(b) | 989 | (b) when used in relation to the Corporations Act 2001 of the Commonwe | encoded | dictionary: Schedule 4, Corporations Regulations |  |
| Schedule 4 'Court of Appeal' | 990 | Court of Appeal means the Court of Appeal under the Supreme Court Act  | encoded | dictionary: Schedule 4, Court of Appeal |  |
| Schedule 4 'Court of Criminal Appeal' | 991 | Court of Criminal Appeal means the Court of Criminal Appeal under the  | encoded | dictionary: Schedule 4, Court of Criminal Appeal |  |
| Schedule 4 'Crown Prosecutor' | 992 | Crown Prosecutor means a Crown Prosecutor under the Crown Prosecutors  | encoded | dictionary: Schedule 4, Crown Prosecutor |  |
| Schedule 4 'date of assent' | 993 | date of assent, in relation to an Act, means the day on which the Act  | encoded | dictionary: Schedule 4, date of assent, in relation to an Act |  |
| Schedule 4 'definition' | 994-996 | definition means a provision of an Act or instrument (however expresse | encoded | dictionary: Schedule 4, definition |  |
| Schedule 4 'definition'(a) | 995 | (a) gives a meaning to a word or expression, or | encoded | dictionary: Schedule 4, definition |  |
| Schedule 4 'definition'(b) | 996 | (b) limits or extends the meaning of a word or expression. | encoded | dictionary: Schedule 4, definition |  |
| Schedule 4 'Director of Public Prosecutions' | 997 | Director of Public Prosecutions means the Director of Public Prosecuti | encoded | dictionary: Schedule 4, Director of Public Prosecutions |  |
| Schedule 4 'District Court' | 998 | District Court means the District Court of New South Wales under the D | encoded | dictionary: Schedule 4, District Court |  |
| Schedule 4 'document' | 999-1003 | document means any record of information, and includes— | encoded | definitions: Schedule 4 document / dictionary: Schedule 4, document |  |
| Schedule 4 'document'(a) | 1000 | (a) anything on which there is writing, or | encoded | definitions: Schedule 4 document / dictionary: Schedule 4, document |  |
| Schedule 4 'document'(b) | 1001 | (b) anything on which there are marks, figures, symbols or perforation | encoded | definitions: Schedule 4 document / dictionary: Schedule 4, document |  |
| Schedule 4 'document'(c) | 1002 | (c) anything from which sounds, images or writings can be reproduced w | encoded | definitions: Schedule 4 document / dictionary: Schedule 4, document |  |
| Schedule 4 'document'(d) | 1003 | (d) a map, plan, drawing or photograph. | encoded | definitions: Schedule 4 document / dictionary: Schedule 4, document |  |
| Schedule 4 'Drug Court' | 1004 | Drug Court means the Drug Court of New South Wales under the Drug Cour | encoded | dictionary: Schedule 4, Drug Court |  |
| Schedule 4 'Dust Diseases Tribunal' | 1005 | Dust Diseases Tribunal means the Dust Diseases Tribunal of New South W | encoded | dictionary: Schedule 4, Dust Diseases Tribunal |  |
| Schedule 4 'Electoral Commissioner' | 1006 | Electoral Commissioner means the Electoral Commissioner under the Elec | encoded | dictionary: Schedule 4, Electoral Commissioner |  |
| Schedule 4 'environmental planning instrument' | 1007 | environmental planning instrument means an environmental planning inst | encoded | dictionary: Schedule 4, environmental planning instrument |  |
| Schedule 4 'estate' | 1008 | estate includes interest, charge, right, title, claim, demand, lien an | encoded | definitions: Schedule 4 includes: estate / dictionary: Schedule 4, estate |  |
| Schedule 4 'Executive Council' | 1009 | Executive Council means the Executive Council of New South Wales. | encoded | dictionary: Schedule 4, Executive Council |  |
| Schedule 4 'external Territory' | 1010 | external Territory means a Territory, not being an internal Territory, | encoded | definitions: Schedule 4 external Territory / dictionary: Schedule 4, external Territory |  |
| Schedule 4 'Federal Circuit and Family Court of Australia' | 1011 | Federal Circuit and Family Court of Australia has the same meaning as  | encoded | dictionary: Schedule 4, Federal Circuit and Family Court of Australia |  |
| Schedule 4 'foreign country' | 1012 | foreign country means any country (whether or not an independent sover | encoded | definitions: Schedule 4 foreign country / dictionary: Schedule 4, foreign country |  |
| Schedule 4 'Gazette, or Government Gazette' | 1013-1015 | Gazette, or Government Gazette, means the New South Wales Government G | encoded | definitions: Schedule 4 Gazette / dictionary: Schedule 4, Gazette, or Government Gazette |  |
| Schedule 4 'Gazette, or Government Gazette'(a) | 1014 | (a) in print, or | encoded | definitions: Schedule 4 Gazette / dictionary: Schedule 4, Gazette, or Government Gazette |  |
| Schedule 4 'Gazette, or Government Gazette'(b) | 1015 | (b) on a website authorised by the Parliamentary Counsel to provide pu | encoded | definitions: Schedule 4 Gazette / dictionary: Schedule 4, Gazette, or Government Gazette |  |
| Schedule 4 'Government' | 1016 | Government means the Government of New South Wales. | encoded | dictionary: Schedule 4, Government |  |
| Schedule 4 'Greater Sydney Region' | 1017 | Greater Sydney Region—see Schedule 1. | encoded | dictionary: Schedule 4, Greater Sydney Region |  |
| Schedule 4 'Health Care Complaints Commission' | 1018 | Health Care Complaints Commission means the Health Care Complaints Com | encoded | dictionary: Schedule 4, Health Care Complaints Commission |  |
| Schedule 4 'High Court' | 1019 | High Court means the High Court of Australia. | encoded | dictionary: Schedule 4, High Court |  |
| Schedule 4 'ICAC or Independent Commission Against Corruption' | 1020 | ICAC or Independent Commission Against Corruption means the Independen | encoded | dictionary: Schedule 4, ICAC or Independent Commission Against Corruption |  |
| Schedule 4 'indictable offence' | 1021 | indictable offence means an offence for which proceedings may be taken | encoded | definitions: Schedule 4 indictable offence / dictionary: Schedule 4, indictable offence |  |
| Schedule 4 'individual' | 1022 | individual means a natural person. | encoded | definitions: Schedule 4 individual / dictionary: Schedule 4, individual |  |
| Schedule 4 'Industrial Court or Industrial Relations Commission in Court Session' | 1023 | Industrial Court or Industrial Relations Commission in Court Session m | encoded | dictionary: Schedule 4, Industrial Court or Industrial Relations Commission in Court Session |  |
| Schedule 4 'Industrial Relations Commission' | 1024 | Industrial Relations Commission means the Industrial Relations Commiss | encoded | dictionary: Schedule 4, Industrial Relations Commission |  |
| Schedule 4 'Information Commissioner' | 1025 | Information Commissioner means the Information Commissioner under the  | encoded | dictionary: Schedule 4, Information Commissioner |  |
| Schedule 4 'Inspector of Custodial Services' | 1026 | Inspector of Custodial Services means the Inspector of Custodial Servi | encoded | dictionary: Schedule 4, Inspector of Custodial Services |  |
| Schedule 4 'Inspector of the Independent Commission Against Corruption' | 1027 | Inspector of the Independent Commission Against Corruption means the I | encoded | dictionary: Schedule 4, Inspector of the Independent Commission Against Corruption |  |
| Schedule 4 'internal Territory' | 1028 | internal Territory means the Australian Capital Territory, the Jervis  | encoded | definitions: Schedule 4 internal Territory / dictionary: Schedule 4, internal Territory |  |
| Schedule 4 'IPART or Independent Pricing and Regulatory Tribunal' | 1029 | IPART or Independent Pricing and Regulatory Tribunal means the Indepen | encoded | dictionary: Schedule 4, IPART or Independent Pricing and Regulatory Tribunal |  |
| Schedule 4 'Jervis Bay Territory' | 1030 | Jervis Bay Territory means the Territory referred to in the Jervis Bay | encoded | dictionary: Schedule 4, Jervis Bay Territory |  |
| Schedule 4 'land' | 1031 | land includes messuages, tenements and hereditaments, corporeal and in | encoded | definitions: Schedule 4 includes: land / dictionary: Schedule 4, land |  |
| Schedule 4 'Land and Environment Court' | 1032 | Land and Environment Court means the Land and Environment Court under  | encoded | dictionary: Schedule 4, Land and Environment Court |  |
| Schedule 4 'Law Enforcement Conduct Commission' | 1033 | Law Enforcement Conduct Commission means the Law Enforcement Conduct C | encoded | dictionary: Schedule 4, Law Enforcement Conduct Commission |  |
| Schedule 4 'Legislative Assembly' | 1034 | Legislative Assembly means the Legislative Assembly of New South Wales | encoded | dictionary: Schedule 4, Legislative Assembly |  |
| Schedule 4 'Legislative Council' | 1035 | Legislative Council means the Legislative Council of New South Wales. | encoded | dictionary: Schedule 4, Legislative Council |  |
| Schedule 4 'local council' | 1036 | local council means a council within the meaning of the Local Governme | encoded | dictionary: Schedule 4, local council |  |
| Schedule 4 'Local Court' | 1037 | Local Court means the Local Court established under the Local Court Ac | encoded | dictionary: Schedule 4, Local Court |  |
| Schedule 4 'Magistrate' | 1038 | Magistrate means a Magistrate appointed under the Local Court Act 2007 | encoded | dictionary: Schedule 4, Magistrate |  |
| Schedule 4 'make' | 1039 | make, in relation to an instrument, includes issue and grant. | encoded | definitions: Schedule 4 includes: make / dictionary: Schedule 4, make, in relation to an instrument |  |
| Schedule 4 'Mental Health Review Tribunal' | 1040 | Mental Health Review Tribunal means the Mental Health Review Tribunal  | encoded | dictionary: Schedule 4, Mental Health Review Tribunal |  |
| Schedule 4 'mentally incapacitated person' | 1041 | mentally incapacitated person means a person who is an involuntary pat | encoded | definitions: Schedule 4 mentally incapacitated person / dictionary: Schedule 4, mentally incapacitated person |  |
| Schedule 4 'midnight' | 1042 | midnight, in relation to a particular day, means the point of time at  | fork | dictionary: Schedule 4, midnight, in relation to a particular day / interpretation-time: Schedule 4, midnight; Schedule 4, midnight; s 24; s 30D; s 71 | F11 |
| Schedule 4 'minor' | 1043 | minor means an individual who is under the age of 18 years. | encoded | definitions: Schedule 4 minor / dictionary: Schedule 4, minor |  |
| Schedule 4 'minor indictable offence' | 1044 | minor indictable offence means an indictable offence that is not a ser | encoded | definitions: Schedule 4 minor indictable offence / dictionary: Schedule 4, minor indictable offence |  |
| Schedule 4 'month' | 1045 | month means a calendar month. | encoded | dictionary: Schedule 4, month |  |
| Schedule 4 'named month' | 1046 | named month means January, February, March, April, May, June, July, Au | encoded | definitions: Schedule 4 named month; Schedule 4 named month number / dictionary: Schedule 4, named month |  |
| Schedule 4 'National Electricity (NSW) Law' | 1047 | National Electricity (NSW) Law means the provisions applying because o | encoded | dictionary: Schedule 4, National Electricity (NSW) Law |  |
| Schedule 4 'National Electricity (NSW) Regulations' | 1048 | National Electricity (NSW) Regulations means the provisions applying b | encoded | dictionary: Schedule 4, National Electricity (NSW) Regulations |  |
| Schedule 4 'National Gas (NSW) Law' | 1049 | National Gas (NSW) Law means the provisions applying because of sectio | encoded | dictionary: Schedule 4, National Gas (NSW) Law |  |
| Schedule 4 'National Gas (NSW) Regulations' | 1050 | National Gas (NSW) Regulations means the provisions applying because o | encoded | dictionary: Schedule 4, National Gas (NSW) Regulations |  |
| Schedule 4 'New South Wales Crime Commission' | 1051 | New South Wales Crime Commission means the New South Wales Crime Commi | encoded | dictionary: Schedule 4, New South Wales Crime Commission |  |
| Schedule 4 'NICC or NSW Independent Casino Commission' | 1052 | NICC or NSW Independent Casino Commission means the NSW Independent Ca | encoded | dictionary: Schedule 4, NICC or NSW Independent Casino Commission |  |
| Schedule 4 'Northern Territory' | 1053 | Northern Territory means the Northern Territory of Australia. | encoded | dictionary: Schedule 4, Northern Territory |  |
| Schedule 4 'NSW Health Service' | 1054 | NSW Health Service means the NSW Health Service referred to in the Hea | encoded | dictionary: Schedule 4, NSW Health Service |  |
| Schedule 4 'NSW legislation website' | 1055 | NSW legislation website means the website with the URL of www.legislat | encoded | dictionary: Schedule 4, NSW legislation website |  |
| Schedule 4 'NSW Police Force' | 1056 | NSW Police Force means the NSW Police Force established by the Police  | encoded | dictionary: Schedule 4, NSW Police Force |  |
| Schedule 4 'NSW Rural Fire Service' | 1057 | NSW Rural Fire Service means the NSW Rural Fire Service under the Rura | encoded | dictionary: Schedule 4, NSW Rural Fire Service |  |
| Schedule 4 'NSW Trustee and Guardian' | 1058 | NSW Trustee and Guardian means the NSW Trustee and Guardian under the  | encoded | dictionary: Schedule 4, NSW Trustee and Guardian |  |
| Schedule 4 'oath' | 1059 | oath, in the case of persons for the time being allowed by law to affi | encoded | definitions: Schedule 4 includes: oath / dictionary: Schedule 4, oath, in the case of persons for the time being allowed by law to affirm, declare or promise |  |
| Schedule 4 'office' | 1060 | office includes position. | encoded | definitions: Schedule 4 includes: office / dictionary: Schedule 4, office |  |
| Schedule 4 'Ombudsman' | 1061 | Ombudsman means the Ombudsman under the Ombudsman Act 1974. | encoded | dictionary: Schedule 4, Ombudsman |  |
| Schedule 4 'Parliament' | 1062 | Parliament means the Parliament of New South Wales. | encoded | dictionary: Schedule 4, Parliament |  |
| Schedule 4 'party' | 1063 | party includes an individual, a corporation and a body corporate or po | encoded | definitions: Schedule 4 includes: party / dictionary: Schedule 4, party |  |
| Schedule 4 'penalty' | 1064 | penalty includes forfeiture and punishment. | encoded | definitions: Schedule 4 includes: penalty / dictionary: Schedule 4, penalty |  |
| Schedule 4 'penalty unit' | 1065 | penalty unit is defined in section 17 of the Crimes (Sentencing Proced | encoded | dictionary: Schedule 4, penalty unit |  |
| Schedule 4 'person' | 1066 | person includes an individual, a corporation and a body corporate or p | encoded | definitions: Schedule 4 includes: person / dictionary: Schedule 4, person |  |
| Schedule 4 'personally insolvent' | 1067-1074 | personally insolvent, for an individual, means the individual— | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(a) | 1068-1072 | (a) under the Bankruptcy Act 1966 of the Commonwealth— | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(a)(i) | 1069 | (i) is bankrupt, or | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(a)(ii) | 1070 | (ii) is a party to a debt agreement as a debtor, or | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(a)(iii) | 1071 | (iii) is a party to a personal insolvency agreement as a debtor and th | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(a)(iv) | 1072 | (iv) authorises a controlling trustee to control the individual's prop | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(b) | 1073 | (b) has a status under a law of a foreign country substantially simila | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'personally insolvent'(c) | 1074 | (c) otherwise applies to take the benefit of a law for the relief of b | encoded | definitions: Schedule 4 personally insolvent / dictionary: Schedule 4, personally insolvent, for an individual |  |
| Schedule 4 'police officer' | 1075 | police officer means a member of the NSW Police Force who is a police  | encoded | dictionary: Schedule 4, police officer |  |
| Schedule 4 'Privacy Commissioner' | 1076 | Privacy Commissioner means the Privacy Commissioner under the Privacy  | encoded | dictionary: Schedule 4, Privacy Commissioner |  |
| Schedule 4 'proclamation' | 1077 | proclamation means a proclamation of the Governor published in the Gaz | encoded | definitions: Schedule 4 proclamation / dictionary: Schedule 4, proclamation |  |
| Schedule 4 'property' | 1078 | property means any legal or equitable estate or interest (whether pres | encoded | definitions: Schedule 4 includes: property / dictionary: Schedule 4, property |  |
| Schedule 4 'public holiday' | 1079 | public holiday means a day appointed under the Public Holidays Act 201 | encoded | dictionary: Schedule 4, public holiday |  |
| Schedule 4 'Public Service or NSW Public Service' | 1080 | Public Service or NSW Public Service means the Public Service referred | encoded | dictionary: Schedule 4, Public Service or NSW Public Service |  |
| Schedule 4 'Registrar-General' | 1081 | Registrar-General means the person employed in the Public Service as t | encoded | dictionary: Schedule 4, Registrar-General |  |
| Schedule 4 'Registrar of Births, Deaths and Marriages' | 1082 | Registrar of Births, Deaths and Marriages means the Registrar under th | encoded | dictionary: Schedule 4, Registrar of Births, Deaths and Marriages |  |
| Schedule 4 'repeal' | 1083 | repeal, in relation to an instrument, includes revoke and rescind. | encoded | definitions: Schedule 4 includes: repeal / dictionary: Schedule 4, repeal, in relation to an instrument |  |
| Schedule 4 'rules of court' | 1084 | rules of court, in relation to a court or tribunal, means rules made b | encoded | dictionary: Schedule 4, rules of court, in relation to a court or tribunal |  |
| Schedule 4 'serious indictable offence' | 1085 | serious indictable offence means an indictable offence that is punisha | encoded | definitions: Schedule 4 serious indictable offence / dictionary: Schedule 4, serious indictable offence |  |
| Schedule 4 'Service NSW' | 1086 | Service NSW means Service NSW under the Service NSW (One-stop Access t | encoded | dictionary: Schedule 4, Service NSW |  |
| Schedule 4 'Sheriff' | 1087 | Sheriff means the Sheriff under the Sheriff Act 2005. | encoded | dictionary: Schedule 4, Sheriff |  |
| Schedule 4 'sign' | 1088 | sign includes the affixing of a seal and the making of a mark. | encoded | definitions: Schedule 4 includes: sign / dictionary: Schedule 4, sign |  |
| Schedule 4 'Standards Australia' | 1089 | Standards Australia means Standards Australia International Limited (A | encoded | dictionary: Schedule 4, Standards Australia |  |
| Schedule 4 'State' | 1090 | State means a State of the Commonwealth. | encoded | dictionary: Schedule 4, State |  |
| Schedule 4 'State Emergency Service' | 1091 | State Emergency Service means the NSW State Emergency Service under th | encoded | dictionary: Schedule 4, State Emergency Service |  |
| Schedule 4 'State industrial instrument' | 1092 | State industrial instrument means an industrial instrument within the  | encoded | dictionary: Schedule 4, State industrial instrument |  |
| Schedule 4 'State owned corporation' | 1093 | State owned corporation means a State owned corporation within the mea | encoded | dictionary: Schedule 4, State owned corporation |  |
| Schedule 4 'statutory declaration' | 1094 | statutory declaration means a declaration made by virtue of any Act au | encoded | dictionary: Schedule 4, statutory declaration |  |
| Schedule 4 'statutory rule' | 1095-1099 | statutory rule means— | encoded | definitions: Schedule 4 statutory rule / dictionary: Schedule 4, statutory rule |  |
| Schedule 4 'statutory rule'(a) | 1096-1098 | (a) a regulation, by-law, rule or ordinance— | encoded | definitions: Schedule 4 statutory rule / dictionary: Schedule 4, statutory rule |  |
| Schedule 4 'statutory rule'(a)(i) | 1097 | (i) that is made by the Governor, or | encoded | definitions: Schedule 4 statutory rule / dictionary: Schedule 4, statutory rule |  |
| Schedule 4 'statutory rule'(a)(ii) | 1098 | (ii) that is made by a person or body other than the Governor, but is  | encoded | definitions: Schedule 4 statutory rule / dictionary: Schedule 4, statutory rule |  |
| Schedule 4 'statutory rule'(b) | 1099 | (b) a rule of court. | encoded | definitions: Schedule 4 statutory rule / dictionary: Schedule 4, statutory rule |  |
| Schedule 4 'summary offence' | 1100 | summary offence means an offence that is not an indictable offence. | encoded | definitions: Schedule 4 summary offence / dictionary: Schedule 4, summary offence |  |
| Schedule 4 'Supreme Court' | 1101 | Supreme Court means the Supreme Court of New South Wales under the Sup | encoded | dictionary: Schedule 4, Supreme Court |  |
| Schedule 4 'Surveyor-General' | 1102 | Surveyor-General means the Surveyor-General under the Surveying and Sp | encoded | dictionary: Schedule 4, Surveyor-General |  |
| Schedule 4 'swear' | 1103 | swear, in the case of persons for the time being allowed by law to aff | encoded | definitions: Schedule 4 includes: swear / dictionary: Schedule 4, swear, in the case of persons for the time being allowed by law to affirm, declare or promise |  |
| Schedule 4 'Teaching Service' | 1104 | Teaching Service means the Teaching Service of New South Wales referre | encoded | dictionary: Schedule 4, Teaching Service |  |
| Schedule 4 'Territory' | 1105 | Territory means a Territory of the Commonwealth. | encoded | dictionary: Schedule 4, Territory |  |
| Schedule 4 'the State' | 1106 | the State means the State of New South Wales. | encoded | dictionary: Schedule 4, the State |  |
| Schedule 4 'Transport Service' | 1107 | Transport Service means the Transport Service of New South Wales refer | encoded | dictionary: Schedule 4, Transport Service |  |
| Schedule 4 'United Kingdom' | 1108 | United Kingdom means the United Kingdom of Great Britain and Northern  | encoded | dictionary: Schedule 4, United Kingdom |  |
| Schedule 4 'Valuer-General' | 1109 | Valuer-General means the Valuer-General under the Valuation of Land Ac | encoded | dictionary: Schedule 4, Valuer-General |  |
| Schedule 4 'writing' | 1110 | writing includes printing, photography, photocopying, lithography, typ | encoded | definitions: Schedule 4 includes: writing / dictionary: Schedule 4, writing |  |
| s 45E note | 509 | (cf former ss 9D and 9F of Reprints Act 1972) | inert (1: not operative) | printed note |  |
| Schedule 3 note | 892 | (Section 83) | inert (1: not operative) | printed note |  |
| Schedule 2 note | 877 | (Section 82) | inert (1: not operative) | printed note |  |
| s 3(1) 'instrument' | 29 | instrument means an instrument (including a statutory rule or an envir | encoded | p1-preliminary: s 3(1) instrument |  |
| s 20 'by-law' | 159 | by-law means a by-law made under the Act in which that word occurs. | encoded | p2-references: s 20 |  |
| s 20 'ordinance' | 160 | ordinance means an ordinance made under the Act in which that word occ | encoded | p2-references: s 20 |  |
| s 20 'prescribed' | 161 | prescribed means prescribed by, or by a statutory rule made under, the | encoded | p2-references: s 20 |  |
| s 20 'regulation' | 162 | regulation means a regulation made under the Act in which that word oc | encoded | p2-references: s 20 |  |
| s 20 'rule' | 163 | rule means a rule made under the Act in which that word occurs. | encoded | p2-references: s 20 |  |
| s 21(2) 'Colony' | 168 | Colony, in relation to any part of Australia, means the State or Terri | encoded | p2-references: s 21(2) Colony; s 21(2) the Colony |  |
| s 21(2) 'the Colony' | 169 | the Colony means the State of New South Wales. | encoded | p2-references: s 21(2) the Colony |  |
| s 30C(1) 'amending Act' | 315-317 | amending Act means— | encoded | p4-repeals: s 30C(1) amending Act |  |
| s 30C(1) 'ancillary provision' | 318 | ancillary provision of an amending Act means the long title of the Act | encoded | p4-repeals: s 30C(1) ancillary provision |  |
| s 45(2) 'instrument' | 470-476 | instrument means— | encoded | p6-statutory-rules: s 45(2) |  |
| s 45B 'legislation' | 485-489 | legislation means— | encoded | p6-statutory-rules: s 45B legislation |  |
| s 58 'adjacent area' | 629 | adjacent area in respect of the State means the area the boundary of w | encoded | p10-coastal: s 58 adjacent area |  |
| s 58 'coastal waters of the State' | 630-632 | coastal waters of the State means— | encoded | p10-coastal: s 58 coastal waters of the State |  |
| s 58 'laws of the State' | 633 | laws of the State means the laws (whether written or unwritten and whe | encoded | p10-coastal: s 58 laws of the State |  |
| s 58 'territorial sea of Australia' | 634 | territorial sea of Australia means the territorial sea of Australia wi | encoded | p10-coastal: s 58 territorial sea of Australia |  |
| s 76(2) 'working day' | 786-788 | working day means a day that is not— | encoded | interpretation-time: s 76(2) |  |
| s 53A(7) 'part-time office' | 618-620 | (7) In this section, part-time office means an office other than— | encoded | p8-bodies: s 53A(7) |  |
| s 23(8) 'published' | 236 | (8) In this section, published means published on the NSW legislation  | encoded | p3-commencement: s 23(8) |  |
| s 13A(5) 'the Crown' | 98 | (5) In this section, the Crown includes the State and the Government o | encoded | p2-crown-offices: s 13A(5) |  |
| Schedule 3 clause 1(2) 'the appointed day' | 897 | the appointed day means the day appointed and notified under section 2 | encoded | schedules: Schedule 3 clause 1 |  |
| Schedule 3 clause 12(4) 'Government Printer' | 937 | Government Printer means the Government Printer of New South Wales, an | encoded | schedules: Schedule 3 clause 12(4) |  |


## Fork register

This register has three parts.
The first lists the shapes of answer that the Guide's rulings on `JUST FALSE` and `NOTHING` fix, so that a reader knows what each answer means without opening every rule.
The second lists the forks: places where the text can be read two or more ways with different outcomes and the rulings do not choose.
The third lists four sites that the rulings leave open and that were decided on the text's own words.
A fork row in the coverage table carries the fork's identifier in its last column.

### The shapes the rulings fix

Measured over the `@ref` blocks of the layer-1 modules by a script outside the deposit: 474 blocks, of which 103 contain `JUST FALSE`.
Of those 103, 39 answer `JUST FALSE` where the printed condition fails (`ELSE JUST FALSE`) and 64 answer it where a printed negative is engaged and `NOTHING` otherwise.
214 blocks contain `NOTHING`.

| Shape | What the function answers | Examples (the function's `@ref` label) |
|---|---|---|
| A condition the text introduces with "if", "where", "only if", "as long as" or "unless", and a rule that gives an effect or a result when it holds | `JUST FALSE` when the condition fails | 13A(1), 16(2), 16(3), 23(7), 25, 26(1), 29, 30A(1), 36(3), 41(2), 41(4), 45C(2), 45C(4), 46(1), 47(1)(a), 48, 49(1), 53A(1) to (3), 69A, 70, 72(1), 75, 76(1)(a), 78(2), 80(1), 80(4) |
| A flat negative ("does not ...", "is not ...", "shall not ...") | `JUST FALSE` when the case engages it, `NOTHING` when it does not | 23(3), 29A(3), 30(1), 40(4), 41(7) to (9), 60(1), 60(2), 63, 72(2), 73(1), 74, 77 |
| A list the text opens ("includes", "without limiting", a list with no "only") | `NOTHING` for a member outside the list | 30(2), 47(1)(b), 47(3), 45C(6), the 16 "includes" entries of Schedule 4 |
| A scope limit with no "only" ("other than a summons", "being a corporation that has 2 or more members") | `NOTHING` outside the limit | 77(1), 50(2) |
| A period the text fixes in its own words | `JUST FALSE` outside it | 23(2) (the 28 days), 41(1)(b) (the 15 sitting days), 77(2)(a) (before 24 April 1969) |
| An answer that is a date or a moment (the type cannot carry `FALSE`) | `NOTHING` when the case is not engaged or the text does not say | 36 (periods in weeks or years), 37 (29 February), 45C(3), 76(1)(b) and (c) when evidence raises doubt, 41(1) when too few sitting days are known |
| Silence, a borrowed term, or a case the text does not decide | `NOTHING` | 33 (both constructions or neither promote the purpose), a term that has no Dictionary entry |

### The forks

| Id | Provision | Function (module) | Answer taken | Other reading | Text that licenses each |
|---|---|---|---|---|---|
| F1 | 36(1); Schedule 4 "calendar month" and "month" | `s 36(1) and Schedule 4 the last day of a period of n calendar months dating from a given day` (`nsw-interpretation-time`) | n months dating from a day run as n successive calendar months, the first commencing at the beginning of the day after the given day. One month from 15 January 2025 ends on 15 February 2025. | The month commences on the given day itself and one month from 15 January ends on 14 February. | 36(1): "the time shall be reckoned exclusive of that day". Schedule 4: a calendar month is "a period commencing at the beginning of a day of one of the 12 named months and ending— (a) immediately before the beginning of the corresponding day of the next named month, or (b) if there is no such corresponding day, at the end of the next named month". Both fit the printed words. |
| F2 | 36(2) | `s 36(2) the latest day on which the thing may be done when the period ends on a day` (`nsw-interpretation-time`) | The last day counted is inside the period: the thing may be done on it. | The period ends the day before the last day counted. | 36(2): "the last day of a period of time prescribed or allowed ... for the doing of any thing". The text does not say whether that last day is inside or outside. |
| F3 | 36(1); Schedule 4 "calendar year" | `s 36 the last day of a period of n units dating from a given day` and `s 36(1) and Schedule 4 the last day of a period of n calendar years dating from a given day` (`nsw-interpretation-time`) | "day" counts as successive days. "Week" and "year" have no Dictionary entry, so a period in weeks or in years returns `NOTHING`. A calendar year is a period of 12 months commencing on 1 January, so a number of calendar years is counted only from a period that begins on 1 January. | A week is 7 days. A year is 12 months from any day. | Schedule 4 defines "calendar year" and "month" and has no entry for "day", "week" or "year". 36(1) speaks only of "a period of time". |
| F4 | 36(2) | the same function | The rule that moves a last day off a Saturday, a Sunday or a holiday applies to the last day of a period in months as in days. | It applies to periods in days only. | 36(2) says "a period of time" and does not limit itself to days. |
| F5 | 15(2), 15(3), 15(4), paragraphs (b) to (d) | `which Minister is meant when paragraphs (b) and (c) are tested first` (`nsw-p2-crown-offices`) | When both (b) different Ministers administering in different respects and (c) different Ministers administering different portions apply, the answer is `NOTHING`. | (b) prevails, or (c) prevails. | (d) begins "if paragraphs (b) and (c) do not apply", which presumes an order between neither and the rest; no text ranks (b) against (c). |
| F6 | 29 | `s 29 the repealed provisions are in force on the day` (`nsw-p4-repeals`) | The repealed provisions are in force on every day before the day the new provisions commence, and not on that day. | They are in force on the commencement day as well. | 29: "continue in force until the new provisions commence"; 24: a provision commencing on a particular day commences "at the beginning of that day"; 30D: a repeal on a day takes effect at the beginning of the day. |
| F7 | 23(3) and 23(5) | `s 23(3) the power to appoint a day extends to a day prior to the day on which the proclamation appointing it is published` and `s 23(5) the proclamation appointing the day fails merely because it is published after that day` (`nsw-p3-commencement`); `s 23(1) and (5) the day an Act commences` (`nsw-interpretation-time`) | Each subsection is encoded as it is printed and they are not combined into one rule: (3) is a bar on appointing a day before the publication day; (5) says what happens when the proclamation is published after the appointed day. | (5) displaces (3), or (3) governs and (5) never arises. | 23(3): "does not include power to appoint a day prior to the day on which the proclamation ... is published". 23(5): "does not fail merely because the proclamation is not published until after that day". |
| F8 | 37 | `s 37 the moment a person attains an age in years` (`nsw-interpretation-time`) | A person born on 29 February has no birthday in a year that is not a leap year, so the moment of attaining an age in such a year is `NOTHING`. | 28 February, or 1 March. | 37: "at the beginning of the person's birthday for that age". The text does not say which day is the birthday in that year. |
| F9 | 39(3), 43(3), 49(3), 50(2), 80(2) | `s 39(3) section 39(1) and (2A) apply to the statutory rule`, `s 43(3) the power to amend or repeal the statutory rule or order is exercisable`, `s 49(3) the delegated function may be exercised`, `s 50(2) the seal is affixed to the document`, `s 80(2) the form is duly completed` | A necessary condition ("unless", "only", "only in accordance with"): `JUST FALSE` when the condition is not met, `NOTHING` when it is met. | `JUST TRUE` when it is met. | The text says no when the condition is unmet. It does not say yes when it is met, because other requirements may remain. |
| F10 | 41(1)(b) | `s 41(1) either House may pass a resolution disallowing the statutory rule` and `s 18 the nth sitting day of a House after a day` (`nsw-p6-statutory-rules`, `nsw-interpretation-time`) | The 15 sitting days run from the first sitting day after the day the notice was laid, so a notice of motion given on the day of laying is outside them (`JUST FALSE`). | The sitting day on which the notice was laid counts as the first. | 41(1)(b): "within 15 sitting days of the House after the relevant written notice was so laid"; 18: a sitting day is a day on which the House actually sits; 36(1): time is reckoned exclusive of the day of the act or event. |
| F11 | 24, 30D, 37, 71; Schedule 4 "midnight" | `the instant a day point denotes, counted in half days` and the day-point functions (`nsw-interpretation-time`) | The end of a day and the beginning of the next day are the same instant. A person who attains an age at the beginning of a birthday is no longer under that age at the end of the day before. | The end of a day and the beginning of the next are two instants with nothing between them, so a moment can be both after the one and before the other. | Schedule 4: midnight, in relation to a particular day, "means the point of time at which that day ends"; 24 and 30D: "at the beginning of" a day; 71: "until the end of that day"; 37: "at the beginning of the person's birthday". |

### Sites decided on the text's own words

These four are decided at the site and have one line each: the provision, the function, the answer taken and the other reading.
Their coverage rows carry no fork identifier, because the answer follows the shape that the printed words fit.

| Id | Provision | Function (module) | Answer taken | Other reading |
|---|---|---|---|---|
| D1 | 47(1)(a), against 47(1)(b), 43(1) and 43(2) | `s 47(1)(a) the power may be exercised from time to time, as occasion requires` (`nsw-p7-functions`); `s 47(1)(b) the power to appoint a person to an office includes the power` (`nsw-p7-functions`); `s 43(1) the power to make a statutory rule includes power to amend or repeal the statutory rule` and `s 43(2) the power to make an order includes power to amend or repeal the order` (`nsw-p6-statutory-rules`) | 47(1)(a) says what the power may do and not that it includes something, so it answers `JUST FALSE` when the "if" fails. 47(1)(b), 43(1) and 43(2) say "includes", so they answer `NOTHING` when their "if" fails or the power is outside the list. | 47(1)(a) answers `NOTHING` when its "if" fails, as the other three do. |
| D2 | 33 | `s 33 the first construction is preferred to the second construction` (`nsw-p5-construction`) | When both constructions would promote the purpose or object, or neither would, the answer is `NOTHING`. | `JUST FALSE`: neither is preferred. |
| D3 | 45C(3), 76(1)(b), 76(1)(c) | `s 45C(3) the date on which the legislation, the Gazette or other matter is published on the NSW legislation website`, `s 76(1)(b) the day service is taken to have been effected`, `s 76(1)(c) the day service in another place is taken to have been effected` (`nsw-p6-statutory-rules`, `nsw-p11-misc`) | The answer is a date, which cannot carry `FALSE`, so a case the rule does not engage (a notified date earlier than the first access, evidence sufficient to raise doubt, a letter posted in another place for 76(1)(b)) answers `NOTHING`. | The rule answers a boolean that the date satisfies the section, and `JUST FALSE` where it fails. |
| D4 | 36(1) | `s 36(1) the first day counted in a period dating from a given day` (`nsw-interpretation-time`) | A period "dating from a given day, act or event" is reckoned exclusive of that day or of the day of the act or event, so it makes no difference whether the period runs "from" a day or "after" an event: the first day counted is the next day. | A period after an event counts the day of the event. |

## What the Act turns out to say

Each statement is what the text provides, read as the fork register says.
A statement ending "Asserted." has a case in `nsw-cases-seat.l4` or a test in the module named; the expected value was written from the text before the run.

1. The first day of a period dating from a given day, act or event is the day after it (36(1)).
   Thirty days from 1 January 2026 end on 31 January 2026.
   Asserted (`nsw-cases-seat.l4`, `nsw-tests-time.l4`).
2. A period of n days has n counted days; the n-th is the last day and is inside the period, and the given day is outside it (36(1), fork F2).
   For thirty days from 1 January 2026, 2 January and 31 January are inside; 1 January and 1 February are not.
   Asserted (`nsw-cases-seat.l4`, "Is the day I am asking about inside my period of days").
3. A period in months is a run of calendar months, the first commencing at the beginning of the day after the given day (36(1), Schedule 4 "calendar month", fork F1).
   One month from 15 January 2025 ends on 15 February 2025.
   One month from 31 January 2024 ends on 29 February 2024.
   One month from 28 February 2025 ends on 31 March 2025.
   Two months from 31 December 2025 end on 28 February 2026.
   Asserted (`nsw-cases-seat.l4`, `nsw-tests-time.l4`).
4. When the last day falls on a Saturday, a Sunday, or a public holiday or bank holiday in the place where the thing is to be done, the thing may be done on the first following day that is none of those (36(2)).
   Thirty days from 1 January 2026 end on Saturday 31 January, so the day is Monday 2 February 2026; with 2 February a holiday, Tuesday 3 February.
   Ten days from 2 March 2026 end on Thursday 12 March; with that day a holiday, Friday 13 March.
   Asserted (`nsw-cases-seat.l4`, "By which day must I act"; `nsw-tests-time.l4`).
5. The rule in statement 4 applies to a period in months as to a period in days (36(2), fork F4).
   Two months from 31 December 2025 end on Saturday 28 February 2026, so the day is Monday 2 March 2026.
   One month from 31 January 2024 ends on Thursday 29 February 2024, which is not moved.
   Asserted (`nsw-cases-seat.l4`).
6. The Dictionary has no entry for "day", "week" or "year", and defines "calendar year" as a period of 12 months commencing on 1 January.
   A period in weeks or in years returns "the Act does not say"; a number of calendar years is counted only from a period that begins on 1 January (fork F3).
   One calendar year from 31 December 2024 ends on 31 December 2025; from 10 March 2025 the Act does not say.
   Asserted (`nsw-cases-seat.l4`, `nsw-tests-time.l4`, `nsw-tests-dictionary.l4`).
7. A power to extend a period of time may be exercised after the period has expired, and an application for an extension may be made after it has expired (36(3)).
   Asserted (`nsw-cases-seat.l4`, "Can I still apply for an extension after my period has run out").
8. A person attains an age in years at the beginning of the person's birthday for that age (37).
   A person born on 15 March 2008 attains 18 on 15 March 2026.
   A person born on 29 February 2008 attains 16 on 29 February 2024; for 18 the Act does not say (fork F8).
   Asserted (`nsw-cases-seat.l4`).
9. A minor is an individual who is under the age of 18 years (Schedule 4), and the end of 14 March 2026 is the same instant as the beginning of 15 March 2026 (Schedule 4 "midnight", fork F11).
   A person born on 15 March 2008 is a minor at the end of 13 March 2026 and is not a minor at the end of 14 March 2026.
   Asserted (`nsw-cases-seat.l4`, "Is the person a minor at the moment I am asking about").
10. An Act commences, if nothing else provides, on the day 28 days after assent; or on the day its own provision specifies; or on the day appointed by proclamation (23(1)).
    With assent on 10 June 2026 and nothing else provided, the day is 8 July 2026.
    Asserted (`nsw-cases-seat.l4`, "On which day does the Act commence").
11. A proclamation published after the day it appoints does not fail; the Act commences on the day the proclamation is published, or, for a proclamation under 23(2), on the earlier of that day and the day the Act would have commenced without the proclamation (23(5)).
    Appointed 1 August 2026 and published 5 August: commences 5 August.
    Appointed 20 June 2026 under 23(2): published 25 June commences 25 June; published 20 July commences 8 July.
    Asserted (`nsw-cases-seat.l4`).
12. A day appointed under 23(2) that is outside the 28 days after assent is not a day the section provides for.
    Assent 10 June 2026 and a proclamation under 23(2) appointing 15 August 2026: the Act does not say.
    Asserted (`nsw-cases-seat.l4`).
13. An Act or statutory rule that commences on a particular day commences at the beginning of that day; an instrument of another kind is not covered (24).
    Asserted (`nsw-cases-seat.l4`, `nsw-tests-time.l4`).
14. A statutory rule commences on the day it is published or, if a later day is specified in the rule for that purpose, on the later day (39(1)(b)).
    Published 5 March 2026: no day specified, 5 March; 1 April specified, 1 April; 1 March specified, which is not later than the publication day, 5 March.
    Asserted (`nsw-cases-seat.l4`).
15. An Act or instrument expressed to expire on a day continues in operation until the end of that day (71).
    Asserted (`nsw-cases-seat.l4`).
16. A repeal on a day takes effect at the beginning of that day (30D).
    Asserted (`nsw-cases-seat.l4`).
17. Repealed provisions continue in force until the new provisions commence (29, fork F6).
    New provisions commencing on 1 July 2026: in force on 30 June, not in force on 1 July.
    Asserted (`nsw-cases-seat.l4`).
18. An amending Act is repealed on the day after all its provisions have commenced, or on the day after assent if it commenced before assent (30C(2), (3)).
    The section does not apply to an amending Act that provides for its own repeal, and applies only to an amending Act enacted after 1 January 2009 (30C(5), (6)).
    Asserted (`nsw-cases-seat.l4`, `nsw-p4-repeals.l4`).
19. Failure to lay a written notice of a statutory rule before each House does not affect the rule (40(4)).
    Asserted (`nsw-cases-seat.l4`).
20. A House may pass a resolution disallowing a statutory rule at any time before the written notice is laid, and after it is laid only if notice of the resolution was given within 15 sitting days of the House after the laying (41(1), fork F10).
    With the notice laid on 3 March 2026 and the sample sitting days of the cases, the last day for notice is 18 March 2026; notice on 19 March is too late.
    Asserted (`nsw-cases-seat.l4`).
21. The Act says that a sitting day is a day on which the House actually sits, and that a number of sitting days counts days across sessions (18).
    Asserted (`nsw-tests-time.l4`).
22. Service of a document by post, where an Act authorises it, is taken to be effected in Australia or in an external Territory on the seventh working day after posting, unless evidence sufficient to raise doubt is adduced; a working day is a day that is not a Saturday, a Sunday, or a public holiday or bank holiday in the place to which the letter was addressed (76).
    Posted Thursday 1 January 2026: Monday 12 January 2026; with 6 January a holiday in the place, 13 January.
    Where evidence sufficient to raise doubt is adduced, 76(1)(b) gives no day.
    A letter posted in another place is taken to be served when it would have been delivered in the ordinary course of post (76(1)(c)), and the Act does not say when that is.
    Asserted (`nsw-cases-seat.l4`).
23. A business day is a day that is not a Saturday, a Sunday, or a public holiday or bank holiday throughout the State (Schedule 4); a working day in 76(2) tests the place the letter was addressed to.
    Asserted (`nsw-cases-seat.l4`).
24. Where a form is prescribed, strict compliance is not necessary and substantial compliance is sufficient (80(1)).
    Asserted (`nsw-cases-seat.l4`).
25. Distance is measured along the nearest route ordinarily used in travelling for an Act passed before the Act's commencement and instruments under it, and in a straight line on a horizontal plane for an Act passed after and instruments under it (38).
    Asserted (`nsw-cases-seat.l4`).
26. The rules of reading in sections 6 to 12 (a definition applies unless the context or subject-matter otherwise indicates or requires; other grammatical forms of a defined word; the singular and the plural; "may" and "shall") are functions over a small description of what is read.
    Asserted (`nsw-p2-words.l4`).
27. The Dictionary is a list that does not say it is closed: a term it does not define is not covered, and each of its 16 "includes" entries names members without closing the list.
    Asserted (`nsw-tests-dictionary.l4`, `nsw-definitions.l4`).
28. The 295 rows of `nsw-xrefs.l4` are each borne out by the index of provisions: the cited identifier is in the index and the heading in the row is the heading the index prints.
    Asserted (`nsw-xrefs.l4`).
29. A power to appoint, delegate or make rules, and the incidental powers that go with it, are stated in sections 46 to 49, 78 and 79 and have rules and tests in layer 1; they have no question in layer 2 because they are addressed to officials.
    Asserted (`nsw-p7-functions.l4`, `nsw-p11-misc.l4`).

## Worked cases: the answer table

Each case was decided from the text, then run.
"Last day" is the last day of the period under 36(1) and Schedule 4; "day to act by" is that day moved by 36(2) when it falls on a Saturday, a Sunday, or a public holiday or bank holiday, with no holidays given.
The section lines are lines of `act-1987-015.txt`.

| Case | Last day | Day to act by | What decides it |
|---|---|---|---|
| Three years from 2025-07-16 | the Act does not say | the Act does not say | 36(1) (line 390) speaks of "a period of time". The Dictionary in Schedule 4 (from line 939) has no entry for "year", and defines only "calendar year", "a period of 12 months commencing on 1 January" (line 973). Fork F3. |
| Five years from 2025-01-15 | the Act does not say | the Act does not say | The same. 15 January is not 1 January. |
| Five years from 2025-09-01 | the Act does not say | the Act does not say | The same. 1 September is not 1 January. |
| Thirty days from 2026-01-01 | Saturday 2026-01-31 | Monday 2026-02-02 | 36(1): the time is reckoned exclusive of 1 January, so 2 January is the first day and 31 January the thirtieth. 36(2) (lines 391 to 394): a last day that falls on a Saturday moves to the first following day that is not a Saturday, a Sunday or a holiday. |
| Two months from 2025-12-31 | Saturday 2026-02-28 | Monday 2026-03-02 | 36(1) and Schedule 4 "calendar month" (lines 970 to 972): the first month commences on 1 January and ends on 31 January; the second commences on 1 February and ends on 28 February. 36(2) moves a Saturday. Forks F1 and F4. |
| One month from 2024-01-31 | Thursday 2024-02-29 | Thursday 2024-02-29 | The month commences on 1 February 2024 and ends immediately before the beginning of the corresponding day of the next named month, 1 March, so at the end of 29 February 2024, a leap year (Schedule 4 "calendar month" (a)). A Thursday is not moved. Fork F1. |
| One year from 2024-02-29 | the Act does not say | the Act does not say | As for three years from 2025-07-16. |

Cases the table does not list but the tests assert, because the same rules decide them: one month from 15 January 2025 ends on 15 February 2025 and its day to act by is Monday 17 February 2025; one month from 28 February 2025 ends on 31 March 2025; one calendar year from 31 December 2024 ends on 31 December 2025.

## Cross-references

`nsw-provisions.l4` indexes the text: one entry for each Part, section, subsection, paragraph, Schedule, Schedule clause, defined term and Schedule table row, with the identifier and the heading as the text prints them.
`nsw-xrefs.l4` holds one row for each reference, with the citing provision, the words of the citation as printed, the identifier it cites, and the heading of the cited provision as printed.
`nsw-xrefs.l4` has **295** rows:

| Kind | Rows | What it is |
|---|---|---|
| to a provision of this text (`ToAProvisionOfThisText`) | 87 | "section 23", "subsection (2)", "Schedule 4", "paragraphs (b) and (c)" |
| to the same unit or the whole Act (`ToTheSameUnitOrTheWholeAct`) | 69 | "this section", "this Part", "this Act", "this subsection" |
| to another Act or instrument (`ToAnotherInstrument`) | 139 | 42 with a provision cited, as in "section 4 (1) of the Coastal Waters (State Powers) Act 1980 of the Commonwealth"; 97 naming the Act or instrument only |

A test for each row asserts that the cited identifier is in the index and that the heading in the row is the index's heading for it; a rows-count test asserts the 295.
A row to another Act or instrument carries the instrument and the provision as printed and is not resolved here; where a rule needs the borrowed fact, the rule asks it as an input.

How the script finds them (the script reads only the text file and is kept outside the deposit):

1. It parses the text into units by its layout: the indentation and printed numbers of Parts, sections, subsections, paragraphs, Schedule clauses, Dictionary terms and table rows.
2. It scans every line for the words "section", "sections", "Part", "Schedule", "clause", "subsection", "paragraph" and "subclause" followed by one or more identifiers (joined by commas, "and" or "or", with bracketed sub-identifiers), and for "this section", "this Part", "this Act", "this subsection", "this clause" and "this Schedule".
3. It scans for a name followed by "Act" and a year, with the optional "No" and "of the Commonwealth" or "of the United Kingdom" tails, and for a short list of codes and laws printed without a year.
4. It attributes each match to the smallest unit that contains the line.
5. A provision followed by "of" and an instrument name is a row of the other-instrument kind with the provision cited; a bare instrument name is a row of that kind with no provision cited.
6. The script writes a row for each reference to a provision of this text that it accepts against the index, and 295 rows result.
7. The rows are written into `nsw-xrefs.l4` in the order of the text.

## What the stable binary does not accept

The writing binary is the stable build 1.6.98; where a skill describes a construct it rejects, the binary governs.
Met while writing, with the form that works:

- **A constructor with fields in a pattern needs parentheses.** `WHEN JUST BeginningOfDay d` is rejected; `WHEN JUST (BeginningOfDay d)` is accepted.
- **Arguments of a record literal need commas, and a list that is not the last argument needs its own parentheses.** `DictionaryEntry OF "amend", Includes, ...` swallowed the arguments after a bare `LIST`; `(LIST "amend", ...)` is accepted.
- **A function application inside a membership test needs parentheses.** `elem term e's names` is a parse error; `elem term (e's names)` is accepted.
- **A chain of `ELSE IF` over twelve month names** hit an indentation error; a table of records filtered by name replaces it (`nsw-definitions.l4`, `Schedule 4 the twelve named months in order`).
- **`length` does not exist**; `count` does.
- **A name defined in two imported modules cannot be used.** One constructor was defined in two modules and was renamed; `dupnames.py` (outside the deposit) now finds every name defined in more than one module, and finds none among 850 names.
- **`IMPORT` finds only modules in the importing file's own folder**, so all `.l4` files sit in one folder, and a module name with a hyphen is written in backticks.
- **`Date d m y` rolls an impossible date forward** (`Date 29 2 2023` is 1 March 2023), so section 37 tests for a 29 February birthday in a year that is not a leap year itself and returns `NOTHING`; no rule builds a date that does not exist.

Used as the brief directs, not tried against the binary here: no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`; every `NOT` parenthesised; every `#ASSERT` on one line.

## What `check.sh` prints

Run from this folder with the stable build as `L4` and the main build as `L4_MAIN`:

```
L4=<stable build 1.6.98> L4_MAIN=<main build 1.6.110> ./check.sh
```

The output, unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
nsw-cases-seat.l4                              0        92       0        0         0 |      0        92       0        0  same
nsw-definitions.l4                             0        96       0        0         0 |      0        96       0        0  same
nsw-dictionary.l4                              0         0       0        0         0 |      0         0       0        0  same
nsw-interpretation-time.l4                     0         0       0        0         0 |      0         0       0        0  same
nsw-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
nsw-p1-preliminary.l4                          0        36       0        0         0 |      0        36       0        0  same
nsw-p10-coastal.l4                             0        30       0        0         0 |      0        30       0        0  same
nsw-p11-misc.l4                                0       136       0        0         0 |      0       136       0        0  same
nsw-p2-crown-offices.l4                        0        66       0        0         0 |      0        66       0        0  same
nsw-p2-references.l4                           0        53       0        0         0 |      0        53       0        0  same
nsw-p2-words.l4                                0        33       0        0         0 |      0        33       0        0  same
nsw-p3-commencement.l4                         0        41       0        0         0 |      0        41       0        0  same
nsw-p4-repeals.l4                              0        81       0        0         0 |      0        81       0        0  same
nsw-p5-construction.l4                         0        68       0        0         0 |      0        68       0        0  same
nsw-p6-statutory-rules.l4                      0       131       0        0         0 |      0       131       0        0  same
nsw-p7-functions.l4                            0        60       0        0         0 |      0        60       0        0  same
nsw-p8-bodies.l4                               0        62       0        0         0 |      0        62       0        0  same
nsw-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
nsw-schedules.l4                               0        75       0        0         0 |      0        75       0        0  same
nsw-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
nsw-tests-dictionary.l4                        0       287       0        0         0 |      0       287       0        0  same
nsw-tests-time.l4                              0       127       0        0         0 |      0       127       0        0  same
nsw-xrefs.l4                                   0       296       0        0         0 |      0       296       0        0  same
TOTAL (23 modules)                             0      1770       0        0           |      0      1770       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Every module has the same four counts on both builds, no module has an error, and `TOTAL` shows 1770 assertions satisfied, none failed, none refused.

Source locators, run from this folder over every `.l4` file:

```
$ python3 -I srcrefs.py check --refs ../../registers/source-bundle/act-1987-015.txt *.l4
srcrefs check: 976 src: lines, 474 runs, 474 locators, 0 problems
$ python3 -I srcrefs.py check --refs ../../registers/source-bundle/act-1987-015.txt --strict *.l4
srcrefs check: 976 src: lines, 474 runs, 474 locators, 0 problems
```

The build used to write the encoding is 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`; the build it was compared with is the one `check.sh` names on its second line.

## The text is an unofficial rendering

The text encoded is `act-1987-015.txt`, a plain-text rendering taken from the Open Australian Legal Corpus (version 7.1.0), document version `nsw_legislation:2024-11-21/act-1987-015`, collected on 2025-03-10.
Its own notice (lines 2 to 3) says it is "not the current official text and may be out of date" and "not the authorised text of the legislation".
Nothing in this encoding has been verified against the official text, and no claim here is "verified against the official text".
The line numbers in every `@ref` are lines of the rendering, so they move if the text is replaced.
The terms the text carries are in `SOURCE-LICENSE.md`, which points at the subject-level note.

## What would need doing before this encoding is worth relying on

1. A New South Wales lawyer reads the layer-1 modules against the official text of the Act as in force on the day of use, and reads the forks F1 to F11 and the shapes in the fork register.
2. The rendering is replaced with the official text, the `@ref` line numbers are regenerated, and `srcrefs.py` is run again.
3. The forks are settled by an authority: the Act does not choose between the readings, and a court decision or the drafting practice of the Parliamentary Counsel would.
4. The borrowed facts are supplied from their sources: the public holidays and bank holidays of the place, the days each House of Parliament sat, and the Acts and instruments that the Act cites and the sources do not include.
5. An independent person writes the tests again from the text, because the expected values here were written by the same agent that wrote the rules.
6. The seat's questions are put in front of people who hold deadlines, to see whether the wording of the `@desc` lines is the wording they would use.
7. The Act is amended over time; the encoding is of the version dated 2024-11-21 and should be re-run against any later version before it is relied on.
