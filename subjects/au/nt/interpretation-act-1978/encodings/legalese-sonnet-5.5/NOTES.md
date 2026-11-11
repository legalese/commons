# Interpretation Act 1978 (Northern Territory): encoding notes

Status: draft.
Not reviewed: no domain expert has read this encoding against the text.
Source: `11865.txt`, an unofficial plain-text rendering of the reprint of the Act in force at 21 April 2023.
It is not the official text, and nothing here is verified against the official text.
Method: a single Sonnet 5.5 agent working alone from the brief in `BRIEF.md`.
Target: main.
Written with the stable build 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`, and compared with the main build 1.6.110 (main, e51181d, 2026-11-11).

## Seat

The seat is a person who has a time limit to meet under a Northern Territory Act or subordinate legislation (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.
It was chosen because the website turns the seat layer into a question form, and the questions this Act answers for an individual are about counting time: on which day a period ends, whether a rest day moves it, when a law or a document takes effect, and when a document is taken to be served.
There is no seat for an official.
Provisions that address only an official (the Gazette and publication duties of the Administrator, ministers and the Government Printer in sections 34 to 38A, 63A, 66A and 72A to 72D) are encoded in layer 1 for what they decide, and appear in the seat layer only as what they mean to the person: the day something begins, or the last day on which the person may act.
The seat layer is `nt-seat.l4` (36 questions in 9 groups) and its cases are `nt-cases-seat.l4`.

Three departures from the rule that every input is a plain yes-or-no, number, date or short typed answer:

1. Public holidays are a fact of the place where the thing must be done, and the Act that lists them is not among the sources.
   The person names up to two public holidays covering a whole day (a flag and a date for each) near the end of the period.
   A public holiday that is part of a day does not move a last day (section 28(2)), so the seat does not offer it (fork F19).
2. The days on which the Legislative Assembly meets are a calendar, so the questions that count sitting days (sections 63(b), 63A(2)(b), 63C(3)) take that calendar as a list of dates.
3. The unit of a period (days, months or years) is a short typed answer; any other unit returns the not-covered value.

## What is encoded and what is not

The in-scope text is the Act and its Schedule: lines 149 to 962 of the text file.
Lines 1 to 148 (the deposit notice, the cover, the table of provisions, the title and the long title) and lines 963 to 1531 (the endnotes) are listed at the foot of the coverage table.
All 814 non-blank lines of the in-scope text fall in exactly one row of the coverage table; a script checks that.
For each section, definition and Schedule row marked encoded the script also finds the `@ref` locators that overlap its lines.
Every operative provision of the Act is encoded; the rows marked inert are headings, the introductions to lists of definitions, the notes and examples (not operative), and the short title (machinery).
Facts that the text borrows or leaves open are inputs: which days are public holidays in the place where a thing is to be done (the Act that lists them is not among the sources), which days the Assembly sits, and the open-textured judgments the Act hands to a reader.

### Modules

| module | provisions | tests | assertions satisfied |
| --- | --- | --- | --- |
| `nt-interpretation-time.l4` | sections 5, 6, 6A, 6B, 11 to 16, 17 ("calendar month", "month", "year", "business day", "calendar year", "financial year", "sitting day"), 25(2) to (4), 28, 29, 30, 63B | `nt-tests-time.l4` | 195 |
| `nt-provisions.l4` | the provision index (one entry per Part, Division, section, subsection, paragraph, subparagraph, the Schedule and each Part of it) | `nt-tests-xrefs.l4` | 148 |
| `nt-xrefs.l4` | the cross-reference rows | `nt-tests-xrefs.l4` | 148 |
| `nt-part1-application.l4` | sections 2(3), 2(4), 3, 4 | `nt-tests-part1.l4` | 29 |
| `nt-part2-commencement.l4` | sections 7, 8, 9 | `nt-tests-part2.l4` | 23 |
| `nt-part4-reading.l4` | sections 18 to 38A (except those in the time module) | `nt-tests-part4-reading.l4` | 177 |
| `nt-part4-definitions.l4` | section 17, definitions (a generated table of 133 and hand-written functions) | `nt-tests-part4-definitions.l4` | 341 |
| `nt-part4a-penalties.l4` | sections 38B to 38G | `nt-tests-part4a.l4` | 43 |
| `nt-part5-powers.l4` | sections 39 to 48B | `nt-tests-part5.l4` | 96 |
| `nt-part6-mechanics.l4` | sections 49 to 57B | `nt-tests-part6.l4` | 97 |
| `nt-part7-construction.l4` | sections 58 to 62E | `nt-tests-part7-construction.l4` | 59 |
| `nt-part7-instruments.l4` | sections 63 to 66 | `nt-tests-part7-instruments.l4` | 94 |
| `nt-part7-general.l4` | sections 66A to 72 | `nt-tests-part7-general.l4` | 45 |
| `nt-part7a-reprints.l4` | sections 72A to 72D | `nt-tests-part7a.l4` | 21 |
| `nt-part8-transitional.l4` | sections 73 to 78 | `nt-tests-part8.l4` | 26 |
| `nt-schedule.l4` | the Schedule and section 2(1), (2) | `nt-tests-schedule.l4` | 41 |
| `nt-seat.l4` | layer 2: the seat's questions | `nt-cases-seat.l4` | 165 |

### The time module

`nt-interpretation-time.l4` imports only `prelude` and `daydate`, names each function for what it computes and the section it implements, and has its own tests in `nt-tests-time.l4`.
It can be copied alone into other work.

## Jural relations

Most provisions of an interpretation Act create no relation between parties: they define, count, say how to read, state a rule of evidence or procedure, or say what a power or duty covers.
Each section is listed once below: the sections that create a relation first, with the party holding the right, privilege, power or immunity, the party bearing the correlative, the provision and the rule; then every other section, as `none`.

| provision | holder | bearer of the correlative | rule |
| --- | --- | --- | --- |
| s 25(1) | a person serving a document: power to serve it on the recipient by the listed methods | the recipient (individual or body): liability to be served | `s 25(1): a person may serve the document on the recipient in that way` in `nt-part4-reading.l4` |
| s 28(2) | the person who must do a thing within a period: privilege to do it on the first following day that is not a Saturday, a Sunday or a public holiday | anyone who would treat the thing as done late: no-right | `s 28(2): the last day on which the thing may be done, for a period whose last day is` in `nt-interpretation-time.l4` |
| s 35(1) | the Administrator: power to make an Administrative Arrangements Order | the ministers and Agencies whose administration of Acts the order allocates: liability | `s 35(1): the person may make an Administrative Arrangements Order` in `nt-part4-reading.l4` |
| s 40(1) | the person acting in an office: privilege to continue to act until the earlier of the two events | anyone who would deny that the person may act: no-right | `s 40(1): the last day on which the person acting may continue to act` in `nt-part5-powers.l4` |
| s 44(1) | the person or authority with power to make appointments to an office or position: power to terminate, remove or suspend a person appointed | the person appointed: liability | `s 44(1): the power to make appointments includes the power to do the thing to the person appointed` in `nt-part5-powers.l4` |
| s 44A | the appointer: power to appoint a person, or 2 or more people, to act in the office or position | the person appointed to act: liability | `s 44A: the appointer may appoint a person, or 2 or more people, to act` in `nt-part5-powers.l4` |
| s 46(1) | the minister, or the person on whom a function or power is conferred: power to give another person authority to perform or exercise it | the person given the authority: liability | `s 46(1), (2): the person may perform the function or exercise the power by authority` in `nt-part5-powers.l4` |
| s 46A(1) | the person with a power to delegate a power or function: power to delegate it to a person by name, by office or by designation | the delegate: liability | `s 46A(1): the power to delegate may be exercised by delegating to a person in that way` in `nt-part5-powers.l4` |
| s 48A(2) | a body established by an Act: power to permit its members to take part in meetings by telephone, email or other means | its members: liability | `s 48A(2): the body may permit its members to participate in a meeting by any means of communication` in `nt-part5-powers.l4` |
| s 48B(1) | the decision maker: power to correct the decision | the parties to the proceeding: liability | `s 48B(1): the decision maker may correct the decision` in `nt-part5-powers.l4` |
| s 63A(1) | the person making a rule or by-law: duty to sign it and give it to the minister (the text names no holder of the correlative claim) | none named | `s 63A(1)(b): the signed rule or by-law must be given to the minister administering the provision containing the power` in `nt-part7-instruments.l4` |
| s 63A(2) | the minister: duty to cause the rule or by-law to be published, notified and tabled (the text names no holder of the correlative claim) | none named | `s 63A(2)(a): the minister has caused the rule or by-law to be published and notified as required` in `nt-part7-instruments.l4` |
| s 63C(2) | the Legislative Assembly: power to pass a resolution disallowing subordinate legislation | the subordinate legislation, and so those who rely on it: liability to be disallowed | `s 63C(2): the Legislative Assembly may pass a resolution disallowing the subordinate legislation or specified provisions of it` in `nt-part7-instruments.l4` |
| s 68 | a person who complies with a prescribed form: privilege that substantial compliance, or such compliance as the circumstances allow, is sufficient | the person or body receiving the form: no-right to insist on strict compliance | `s 68: the compliance with the form is sufficient` in `nt-part7-general.l4` |
| s 69 | the person to whom money is due under an Act: claim to recover it in a court or tribunal | the person who owes it: duty to pay | `s 69: the money is recoverable in the court or tribunal` in `nt-part7-general.l4` |

| section | heading | relation |
| --- | --- | --- |
| s 1 | Short title | none |
| s 2 | Repeal and savings | none |
| s 3 | Application of this Act | none |
| s 4 | Application to statutory instruments | none |
| s 5 | Date of commencement | none |
| s 6 | Proposed laws reserved for Governor-General | none |
| s 6A | Time of commencement | none |
| s 6B | References to commencement | none |
| s 7 | Evidence of assent etc. | none |
| s 8 | Exercise of powers before commencement | none |
| s 9 | Amendment before commencement | none |
| s 11 | Repeal does not revive previous Act | none |
| s 12 | Effect of repeal | none |
| s 13 | Effect of State laws ceasing to apply | none |
| s 14 | Continuance of repealed provisions | none |
| s 15 | References to repealed provisions | none |
| s 16 | Expiration of Acts | none |
| s 17 | Definitions | none |
| s 18 | Definitions to be read in context | none |
| s 18A | References relating to an Agency | none |
| s 19 | Ministerial references | none |
| s 19A | Definitions of certain domestic relationships | none |
| s 20 | Construction of statutory instruments | none |
| s 21 | By, under or pursuant to Act | none |
| s 22 | Construction of amending Acts | none |
| s 23 | Parts of speech and grammatical forms | none |
| s 23A | Defined words in Acts and references in other legislation | none |
| s 24 | Gender and number | none |
| s 24A | Range of numbers, words or other things | none |
| s 24AA | References to persons generally | none |
| s 26 | References to writing | none |
| s 27 | Measurement of distance | none |
| s 29 | 24 hour clock | none |
| s 30 | Reckoning of age | none |
| s 31 | References to the Sovereign | none |
| s 34 | References to Administrator | none |
| s 34A | References to Administrator in Council | none |
| s 36 | Publication and commencement of Administrative Arrangements Order | none |
| s 37 | References in agreements | none |
| s 38 | References to offices etc. | none |
| s 38A | Reference to Commonwealth ministers etc. | none |
| s 38B | Penal provisions include bodies corporate | none |
| s 38C | Penalties at foot of sections and subsections | none |
| s 38DC | Body corporate fines under provision authorising subordinate legislation | none |
| s 38F | Penalties for breach of subordinate legislation | none |
| s 38G | Civil penalties | none |
| s 39 | Confirmation of appointments not required | none |
| s 41 | Occasions for exercise of powers etc. | none |
| s 42 | How power may be exercised | none |
| s 43 | Power to take action or make statutory instrument includes power to revoke, amend etc. | none |
| s 48 | Discretions | none |
| s 49 | Citation | none |
| s 50 | References to other legislation | none |
| s 51 | Reference to Act includes reference to statutory instruments under Act | none |
| s 52 | References to Imperial, Commonwealth and State Acts | none |
| s 53 | References in an Act to provisions of that Act | none |
| s 54 | Every section a substantive enactment | none |
| s 55 | Material that is, and is not, part of an Act | none |
| s 56 | Numbering of Acts | none |
| s 57 | Numbering of subordinate legislation | none |
| s 57A | Amendment of instruments by Act | none |
| s 57B | Definitions automatically inserted in alphabetical order | none |
| s 58 | Amending act to be construed with amended Act | none |
| s 59 | Act to be construed subject to power | none |
| s 59A | Public places etc. on Aboriginal land | none |
| s 61 | Construction of statutory instruments | none |
| s 62 | Construction of resolutions of Legislative Assembly | none |
| s 62A | Regard to be had to purpose or object of Act | none |
| s 62B | Use of extrinsic material in interpreting Act | none |
| s 62C | Changes in drafting practice do not affect meaning | none |
| s 62D | Examples | none |
| s 62E | Notes | none |
| s 63 | Procedure for making regulations | none |
| s 63B | Commencement of subordinate legislation | none |
| s 64 | Subordinate legislation not to be made in terms of disallowed subordinate legislation | none |
| s 65 | Power to make subordinate legislation | none |
| s 65A | Subordinate legislation may prohibit | none |
| s 65B | Subordinate legislation may provide for review or appeal | none |
| s 65C | Subordinate legislation may provide for exemption, waiver or refund of fees | none |
| s 65D | Subordinate legislation may provide for infringement notice offences | none |
| s 65E | Statutory instrument may require making of statutory declaration | none |
| s 65F | Simultaneous actions | none |
| s 66 | Prescribing matters by reference to other instruments | none |
| s 66A | Gazette publication requirements | none |
| s 67 | Tabling documents in Legislative Assembly | none |
| s 70 | Powers of persons authorised to adjudicate | none |
| s 71 | Amendment in same session | none |
| s 72 | Sunday observance | none |
| s 72A | Meaning of reprint | none |
| s 72B | Reprint of legislation in force at stated date | none |
| s 72C | Omission of making words in reprint | none |
| s 72D | Inclusion of tables of amendments in reprints | none |
| s 73 | Subordinate legislation | none |
| s 74 | Numbering of subordinate legislation | none |
| s 75 | Short titles and cross references taken to include year of enactment or making | none |
| s 76 | Disapplication of section 50(1) in certain circumstances | none |
| s 77 | Administrative Arrangements Orders | none |
| s 78 | Tabling requirements for subordinate legislation | none |

## What the Act turns out to say

1. A period of time dating from a given day, act or event is reckoned without that day (section 28(1)).
   Cases: `nt-tests-time.l4:93`.
   Asserted.
2. A period that ends at, with or on a given day, act or event is reckoned to include that day (section 28(1A)).
   Cases: `nt-tests-time.l4:94`.
   Asserted.
3. A calendar month commencing at the beginning of a day ends at the end of the day before the corresponding day of the next named month, or at the end of the next named month if it has no such day (section 17 "calendar month").
   Cases: `nt-tests-time.l4:27`, `nt-tests-time.l4:32`.
   Asserted.
4. A month is a calendar month and a year is a period of 12 months, so three years from 16 July 2025 end on 16 July 2028 (section 17 "month", "year").
   Cases: `nt-tests-time.l4:71`.
   Asserted.
5. When the last day of a period falls on a Saturday, a Sunday or a public holiday in the place where the thing is to be done, the thing may be done on the first following day that is none of these; a public holiday that is part of a day does not count; the rule applies to periods in days, months and years (section 28(2)).
   Cases: `nt-tests-time.l4:124`, `nt-tests-time.l4:116`, `nt-cases-seat.l4:24`.
   Asserted.
6. A business day is a day other than a Saturday or Sunday and other than a public holiday, not being a public holiday that is part of a day, in the place where the act is to be done (section 17 "business day").
   Cases: `nt-tests-time.l4:144`, `nt-cases-seat.l4:78`.
   Asserted.
7. The Act says nothing about a period of weeks, and does not define "week" or "day": the answer is not covered (sections 17 and 28).
   Cases: `nt-tests-time.l4:86`, `nt-cases-seat.l4:41`.
   Asserted.
8. A time of day written as four digits is the number of hours given by the first two digits and the number of minutes given by the last two, after midnight (section 29).
   Cases: `nt-tests-time.l4:185`, `nt-tests-time.l4:191`.
   Asserted.
9. A person attains an age on the anniversary of the birth; for a birth on 29 February the anniversary in a year that is not a leap year is 28 February (section 30).
   Cases: `nt-tests-time.l4:175`, `nt-tests-time.l4:176`.
   Asserted.
10. An Act that does not specify or provide for its commencement commences on the day after the day on which assent is declared; an Act commences at the beginning of the day on which it commences unless it provides otherwise (sections 5(4), 6A).
   Cases: `nt-tests-time.l4:237`, `nt-tests-time.l4:250`.
   Asserted.
11. Where parts of the provisions concerned commence on different days, a reference to their commencement is a reference to the last of those days or times (section 6B).
   Cases: `nt-tests-time.l4:262`.
   Asserted.
12. A proposed law reserved for the Governor-General does not have effect before the day on which notification of the assent is published in the Gazette (section 6).
   Cases: `nt-tests-time.l4:243`, `nt-cases-seat.l4:141`.
   Asserted.
13. Subordinate legislation that specifies no commencement commences on the day after the day it is made, except that a rule or by-law not published or to be published on the legislation website commences on the day it is notified in the Gazette (section 63B(5), (6)).
   Cases: `nt-tests-time.l4:277`, `nt-tests-time.l4:280`.
   Asserted.
14. A provision of subordinate legislation specified to commence or take effect before the day it is made, where the Act under which it is made does not expressly provide for that, is of no effect (section 63B(3), (4)).
   Cases: `nt-tests-time.l4:286`, `nt-cases-seat.l4:163`.
   Asserted.
15. A document served by prepaid post is taken to be served when it would have been delivered in the ordinary course of post; by fax, when it was sent to a current fax number of the recipient, subject to evidence to the contrary; by leaving it at the address, when it was left with the person (section 25(2) to (4)).
   Cases: `nt-tests-time.l4:293`, `nt-tests-time.l4:295`, `nt-tests-time.l4:298`.
   Asserted.
16. A regulation must be tabled in the Legislative Assembly within 6 sitting days after it is made, and a rule or by-law within 6 sitting days after it is notified in the Gazette (sections 63(b), 63A(2)(b)).
   Cases: `nt-tests-part7-instruments.l4:28`, `nt-tests-part7-instruments.l4:58`.
   Asserted.
17. Notice of a resolution disallowing subordinate legislation must be given within 12 sitting days after it is tabled, or, if it was not tabled as required, 12 sitting days after the last sitting day on which it was required to be tabled (section 63C(3)).
   Cases: `nt-tests-part7-instruments.l4:79`, `nt-tests-part7-instruments.l4:81`.
   Asserted.
18. Subordinate legislation the same in substance as disallowed legislation must not be made within 6 months after the disallowance unless the Legislative Assembly rescinds the resolution (section 64(2)).
   Cases: `nt-tests-part7-instruments.l4:94`, `nt-tests-part7-instruments.l4:95`.
   Asserted.
19. The repeal of an Act does not revive an earlier Act repealed by it without express words, and does not affect a right, privilege, obligation or liability acquired, accrued or incurred under the repealed Act, or a penalty, forfeiture or punishment incurred for an offence against it (sections 11, 12).
   Cases: `nt-tests-time.l4:322`, `nt-tests-time.l4:339`, `nt-cases-seat.l4:236`.
   Asserted.
20. Where an Act repeals a former Act and substitutes provisions, the repealed provisions continue in force until the substituted provisions commence (section 14).
   Cases: `nt-tests-time.l4:357`, `nt-tests-time.l4:358`.
   Asserted.
21. The maximum fine for a body corporate that may be imposed under subordinate legislation is 5 times the maximum for an individual where the authorising Act gives no other maximum, and a fine prescribed by subordinate legislation must not exceed 100 penalty units, subject to the Act under which the legislation is made (sections 38DC(3), 38F(2), (3)).
   Cases: `nt-tests-part4a.l4:59`, `nt-tests-part4a.l4:66`.
   Asserted.
22. A reference in an Act to a civil penalty being imposed or required to be paid for a contravention indicates that the contravention may result in a penalty not exceeding the penalty specified in, or prescribed for the purposes of, the provision (section 38G).
   Cases: `nt-tests-part4a.l4:74`.
   Asserted.
23. Substantial compliance with a prescribed form, or such compliance as the circumstances of the case allow, is sufficient; the text does not say that less is insufficient (section 68).
   Cases: `nt-tests-part7-general.l4:45`, `nt-tests-part7-general.l4:46`.
   Asserted.
24. Money due under an Act is recoverable in a court or tribunal having civil jurisdiction in the Territory to the extent of the amount due (section 69).
   Cases: `nt-tests-part7-general.l4:51`, `nt-tests-part7-general.l4:49`.
   Asserted.
25. A reprint shows the legislation as in force at the stated date; an amendment that commences after that date is left out unless the reprint identifies it as uncommenced (section 72B).
   Cases: `nt-tests-part7a.l4:24`, `nt-tests-part7a.l4:25`.
   Asserted.
26. A heading to a Part or Division is part of the Act; a heading to a section is part of the Act if the Act was enacted after 1 July 2006 or the heading was amended or inserted after that date (section 55).
   Cases: `nt-tests-part6.l4:93`, `nt-tests-part6.l4:96`.
   Asserted.
27. An example or note does not limit or extend the meaning of the provision, is not exhaustive, and yields to the provision if inconsistent (sections 62D, 62E).
   Cases: `nt-tests-part7-construction.l4:67`, `nt-tests-part7-construction.l4:74`.
   Asserted.
28. The Schedule names 33 instruments: those in Parts 1, 2 and 3 are repealed, and the laws of the State of South Australia in Part 4 cease to have effect in the Northern Territory as laws of the Northern Territory (section 2(1), (2)).
   Cases: `nt-tests-schedule.l4:57`, `nt-tests-schedule.l4:10`, `nt-tests-schedule.l4:42`.
   Asserted.
29. Section 17 defines 133 terms, each of which has an entry in the table of definitions.
   Cases: `nt-tests-part4-definitions.l4:166`.
   Asserted.

## Answers to the worked time cases

Each answer is the last day on which the thing may be done, counting the period under sections 17 and 28(1) and then applying section 28(2).
The Act that lists public holidays is not among the sources, so the final day assumes no public holiday falls on the day shown; if one does, section 28(2) moves it to the first following day that is none of a Saturday, a Sunday or a public holiday.
The weekdays are computed from the calendar, not read from the encoding.

| case | last day of the period | section 28(2) | final day | sections | assertions |
| --- | --- | --- | --- | --- | --- |
| three years from 2025-07-16 | 2028-07-16 (Sunday) | moves from Sunday to Monday | 2028-07-17 (Monday) | 17 "month", 17 "year", 28(1), 28(2) | `nt-tests-time.l4:71`, `nt-tests-time.l4:132`, `nt-cases-seat.l4:14` |
| five years from 2025-01-15 | 2030-01-15 (Tuesday) | none: the last day is a Tuesday | 2030-01-15 (Tuesday) | 17 "month", 17 "year", 28(1), 28(2) | `nt-tests-time.l4:73`, `nt-tests-time.l4:134`, `nt-cases-seat.l4:18` |
| five years from 2025-09-01 | 2030-09-01 (Sunday) | moves from Sunday to Monday | 2030-09-02 (Monday) | 17 "month", 17 "year", 28(1), 28(2) | `nt-tests-time.l4:74`, `nt-tests-time.l4:136`, `nt-cases-seat.l4:20` |
| thirty days from 2026-01-01 | 2026-01-31 (Saturday) | moves from Saturday to Monday | 2026-02-02 (Monday) | 28(1), 28(2) | `nt-tests-time.l4:44`, `nt-tests-time.l4:124`, `nt-cases-seat.l4:22` |
| two months from 2025-12-31 | 2026-02-28 (Saturday) | moves from Saturday to Monday | 2026-03-02 (Monday) | 17 "calendar month", 17 "month", 28(1), 28(2) | `nt-tests-time.l4:56`, `nt-tests-time.l4:126`, `nt-cases-seat.l4:26` |
| one month from 2024-01-31 | 2024-02-29 (Thursday) | none: the last day is a Thursday | 2024-02-29 (Thursday) | 17 "calendar month", 17 "month", 28(1), 28(2) | `nt-tests-time.l4:54`, `nt-tests-time.l4:128`, `nt-cases-seat.l4:28` |
| one year from 2024-02-29 | 2025-02-28 (Friday) | none: the last day is a Friday | 2025-02-28 (Friday) | 17 "month", 17 "year", 28(1), 28(2) | `nt-tests-time.l4:76`, `nt-tests-time.l4:130`, `nt-cases-seat.l4:30` |

The text is silent on one thing each case may need: whether a public holiday falls on the final day.
It is also silent on periods in weeks and on the meaning of "day"; those return the not-covered value.

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the provision, the reading taken, the other reading, the text that licenses them (copied from the text file), the rule that encodes the reading taken, and the assertions.

### F1: Which day starts the count of a period

Coverage rows: s 28(1), s 28(1A).

Text:

> line 507: (1) If in an Act a period of time dating from a given day, act or event is prescribed, allowed or limited for any purpose, the time must be reckoned exclusive of such day or of the day of such act or event.
> line 508: (1A) If an Act provides that a period of time ends at, with or on a given day, act or event, the time is reckoned to include that day or the day of that act or event.

Reading taken:

A period dating from a given day leaves that day out and starts on the next day (subsection (1)).
A period that ends at, with or on a given day includes that day (subsection (1A)).
A period said to run after a day is counted as one dating from it: its first day is the next day.
For a period expressed in any other way, whether the day counts is not covered.
Counting back from an end day is covered for days only; for months and years it is not covered.

Other reading:

(i) A period from a day includes that day: the text says in terms that it does not.
(ii) A period after a day is not one dating from it, so no provision of the Act says which day starts it.

Rules: `s 28(1): the first day counted in a period dating from` in `nt-interpretation-time.l4`; `s 28(1), (1A): the given day, act or event is counted in the period` in `nt-interpretation-time.l4`; `s 28(1A): the first day of a period ending on` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:93`, `nt-tests-time.l4:94`, `nt-tests-time.l4:95`, `nt-tests-time.l4:97`, `nt-tests-time.l4:99`.

### F2: Months and years are counted one calendar month at a time

Coverage rows: s 28(1), s 17 "calendar month", s 17 "month", s 17 "year".

Text:

> line 263: calendar month means a period commencing at the beginning of any day of a named month and ending:
> line 264: (a) at the end of the day before the corresponding day of the next named month; or
> line 265: (b) if there is no such corresponding day – at the end of the next named month.
> line 354: month means a calendar month.
> line 415: year means a period of 12 months.
> line 507: (1) If in an Act a period of time dating from a given day, act or event is prescribed, allowed or limited for any purpose, the time must be reckoned exclusive of such day or of the day of such act or event.

Reading taken:

A month is a calendar month and a year is a period of 12 months.
N months from a day are N calendar months one after another, the first commencing at the beginning of the day after the given day and each later one commencing at the beginning of the day after the previous one ends.
A year is 12 of these months.

Other reading:

N months are counted once from the first counted day, the last day being the day before the corresponding day N months on.
For two months from 29 January 2025 the first counted day is 30 January and that gives 29 March 2025 (the day before 30 March); the reading taken gives 31 March 2025, because the first month has no corresponding 30 February and ends at the end of February, so the second commences on 1 March and ends at the end of March.
A year as 365 days is not licensed: the text says 12 months.

Rules: `s 17 "calendar month": the last day of the calendar month commencing at the beginning of` in `nt-interpretation-time.l4`; `s 17 "month": the last day of consecutive calendar months, the first commencing at the beginning of` in `nt-interpretation-time.l4`; `s 17 "year": the last day of consecutive years, the first commencing at the beginning of` in `nt-interpretation-time.l4`; `s 28(1): the last day of a period dating from` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:63`, `nt-tests-time.l4:81`, `nt-tests-time.l4:71`, `nt-tests-time.l4:34`.

### F3: Section 28(2) applies to periods of days, months and years

Coverage rows: s 28(2).

Text:

> line 509: (2) If the last day of any period prescribed, allowed or limited by an Act for the doing of any thing falls on a Saturday, on a Sunday or on a public holiday in the place in which the thing is to or may be done (other than a public holiday that is part of a day), the thing may be done on the first day following which is not a Saturday, a Sunday or a public holiday in that place.

Reading taken:

Subsection (2) speaks of the last day of any period prescribed, allowed or limited by an Act for the doing of any thing, so it applies whatever the unit of the period.

Other reading:

Subsection (2) applies only to periods in days.
The words "any period" do not support it.

Rules: `s 28(2): the first day, on or after the day, that is not a Saturday, a Sunday or a public holiday` in `nt-interpretation-time.l4`; `s 28(2): the last day on which the thing may be done, for a period whose last day is` in `nt-interpretation-time.l4`; `s 28(1), (2): the last day on which a thing may be done within a period dating from` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:132`, `nt-tests-time.l4:126`, `nt-tests-time.l4:124`.

### F4: Periods in subordinate legislation

Coverage rows: s 4, s 4(a), s 28(1).

Text:

> line 162: This Act applies, so far as it is applicable:
> line 163: (a) to and in respect of statutory instruments made under laws to which this Act applies, and to and in respect of the interpretation, application and effect of such instruments, as if those instruments were Acts; and
> line 507: (1) If in an Act a period of time dating from a given day, act or event is prescribed, allowed or limited for any purpose, the time must be reckoned exclusive of such day or of the day of such act or event.

Reading taken:

Section 28 speaks of periods in an Act.
Section 4(a) applies the Act "so far as it is applicable" to statutory instruments as if they were Acts.
The seat questions count a period under subordinate legislation in the same way and do not ask whether the counting rules are "applicable".

Other reading:

Whether a counting rule is applicable to a given instrument is left to the reader, as a fact to be asked.
The seat layer does not ask it.

Rules: `s 4: the way in which this Act applies to the thing` in `nt-part1-application.l4`.

Assertions: `nt-tests-part1.l4:51`.

### F5: Weeks, and lengths that are not whole positive numbers

Coverage rows: s 28(1), s 28(2).

Text:

> line 507: (1) If in an Act a period of time dating from a given day, act or event is prescribed, allowed or limited for any purpose, the time must be reckoned exclusive of such day or of the day of such act or event.
> line 509: (2) If the last day of any period prescribed, allowed or limited by an Act for the doing of any thing falls on a Saturday, on a Sunday or on a public holiday in the place in which the thing is to or may be done (other than a public holiday that is part of a day), the thing may be done on the first day following which is not a Saturday, a Sunday or a public holiday in that place.

Reading taken:

Section 17 defines month and year and does not define week or day, and section 28 says nothing about a period of weeks, so a period of weeks is not covered.
A length of nought, a negative length or a part of a unit is likewise not covered.

Other reading:

A week is 7 days.
The text does not say so.

Rules: `s 28(1): the last day of a period dating from` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:86`, `nt-tests-time.l4:87`, `nt-tests-time.l4:89`.

### F6: Day of service of a document given to a person

Coverage rows: s 25(2), s 25(3), s 25(4).

Text:

> line 491: (2) A document served under subsection (1)(b) is taken to be served when it would have been delivered in the ordinary course of post.
> line 492: (3) Subject to evidence to the contrary, a document served under subsection (1)(c) is taken to be served when it was sent to a current fax number of the recipient.
> line 493: (4) A document served under subsection (1)(d) is taken to be served when it was left with the person mentioned in the subsection.

Reading taken:

Subsections (2), (3) and (4) say when a document is taken to be served under (1)(b), (c) and (d) (post, fax, leaving it at the address).
They say nothing about a document served under (1)(a) by giving it to a person, so the day is not covered.

Other reading:

A document given to a person is served on the day it is given.
The text does not say so.

Rules: `s 25(2), (3), (4): the day on which a document is taken to be served` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:300`.

### F7: Service by fax: the current number and evidence to the contrary

Coverage rows: s 25(3).

Text:

> line 492: (3) Subject to evidence to the contrary, a document served under subsection (1)(c) is taken to be served when it was sent to a current fax number of the recipient.

Reading taken:

A fax is taken to be served when it was sent to a current fax number of the recipient, subject to evidence to the contrary.
If it was not sent to a current number, or there is evidence to the contrary, the text gives no day and the answer is not covered.

Other reading:

With evidence to the contrary the document is taken to be served on the day the evidence shows.
The text does not provide for that day.

Rules: `s 25(2), (3), (4): the day on which a document is taken to be served` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:297`, `nt-tests-time.l4:296`.

### F8: Subordinate legislation that commences on a day fixed by Gazette notice

Coverage rows: s 63B(2), s 63B(2)(a), s 63B(2)(b).

Text:

> line 794: (2) Subordinate legislation may be specified to commence:
> line 795: (a) subject to subsection (3), on a particular day or on a number of different days; or
> line 796: (b) on the happening of a particular event or events.
> line 172: (b) on a day to be fixed by Gazette notice; or

Reading taken:

Section 63B(2) says subordinate legislation may be specified to commence on a particular day or on the happening of an event.
It does not mention a day fixed by Gazette notice (which section 5(2)(b) mentions for Acts) and does not say "only", so for that way of specifying the day the answer is not covered.

Other reading:

Subordinate legislation may be specified to commence on a day fixed by Gazette notice, as an Act may.
The list in subsection (2) does not include it and section 5 is about Acts.

Rules: `s 63B: the day on which subordinate legislation commences` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:272`.

### F9: "Subject to section 2" in section 3(1)

Coverage rows: s 3(1).

Text:

> line 158: (1) Subject to section 2, this Act applies to each Act, and to each Ordinance and Act of the State of South Australia in its application to the Northern Territory, and to each Ordinance of the Northern Territory, whether made before or after the making of this Act, including this Act, as though that law were an Act.

Reading taken:

Section 3(1) applies the Act to each Act and Ordinance "subject to section 2".
Where section 2 provides otherwise for the law, the Act does not apply to it: the answer is JUST FALSE.

Other reading:

Where section 2 applies the text says nothing: the answer is not covered.
The words "subject to" make the application conditional, which the ruling on conditions treats as a text that says no.

Rules: `s 3(1): this Act applies to the law as though the law were an Act` in `nt-part1-application.l4`.

Assertions: `nt-tests-part1.l4:30`.

### F10: Section 8(2)(b): taking effect before the commencement

Coverage rows: s 8(2), s 8(2)(a), s 8(2)(b).

Text:

> line 203: (2) The statutory instrument or other thing may take effect either:
> line 204: (a) on the commencement of the provision under which the power was exercised; or
> line 205: (b) before the commencement of the provision under which the power was exercised, to the extent necessary for the effective operation of the Act.

Reading taken:

Section 8(2) says the instrument or thing may take effect (a) on the commencement or (b) before it, to the extent necessary for the effective operation of the Act.
A day before the commencement that is not necessary is outside the permission, but the text does not say it is forbidden: the answer is not covered.

Other reading:

A day before the commencement that is not necessary is not allowed, so JUST FALSE.
The text limits a permission in its own words and does not say "only".

Rules: `s 8(2): the instrument or thing may take effect on that day` in `nt-part2-commencement.l4`.

Assertions: `nt-tests-part2.l4:33`.

### F11: Section 9: the period in which a proposed law may be cited and amended

Coverage rows: s 9, s 9(a), s 9(b).

Text:

> line 208: At any time after a proposed law has been passed by the Legislative Assembly and before it has commenced:
> line 209: (a) it may be cited by its proposed short title; and
> line 210: (b) it may be the subject of a further proposed law to amend or repeal it,

Reading taken:

Section 9 fixes the period in its own words: at any time after the proposed law has been passed and before it has commenced.
Outside it, the answer is JUST FALSE.

Other reading:

Outside the period the text says nothing: the answer is not covered.

Rules: `s 9(a), (b): the proposed law may be cited by its proposed short title and be the subject of a further proposed law to amend or repeal it` in `nt-part2-commencement.l4`.

Assertions: `nt-tests-part2.l4:46`, `nt-tests-part2.l4:47`.

### F12: A reference to a paragraph inside a subsection (section 53(3) and (4))

Coverage rows: s 53(3), s 53(4).

Text:

> line 691: (3) A reference in a section of an Act to a subsection or paragraph shall be read as a reference to a subsection or paragraph of that section.
> line 692: (4) A reference in a subsection of a section of an Act to a paragraph shall be read as a reference to a paragraph of that subsection.

Reading taken:

A reference in a subsection of a section to a paragraph falls under both (3) (a paragraph of that section) and (4) (a paragraph of that subsection).
The narrower provision, (4), governs: the paragraph is one of that subsection.

Other reading:

Subsection (3) governs and the paragraph is read as one of the section.

Rules: `s 53(3), (4), (5): the identifier of the unit named` in `nt-part6-mechanics.l4`.

Assertions: `nt-tests-part6.l4:74`.

### F13: Section 40(1)(b): "1 year after the office-holder ceased to hold office"

Coverage rows: s 40(1), s 40(1)(b).

Text:

> line 602: (1) If a person is acting in an office (including a Ministerial office) during the absence or inability of the office-holder and, for any reason, the office-holder ceases to hold the office, the person acting may continue to act in the office until the earlier of the following:
> line 604: (b) 1 year after the office-holder ceased to hold office.

Reading taken:

The year is a period dating from the day the office-holder ceased (section 28(1)), so it is 12 calendar months from the next day and the person may act on its last day.

Other reading:

The person may act until, and not including, the day one year after the day the office-holder ceased.

Rules: `s 40(1): the last day on which the person acting may continue to act` in `nt-part5-powers.l4`.

Assertions: `nt-tests-part5.l4:17`, `nt-tests-part5.l4:25`.

### F14: Individuals under "person" and "party"

Coverage rows: s 17 "person", s 17 "party", s 24AA(1).

Text:

> line 369: person includes a body politic and a body corporate.
> line 367: party includes a body politic and a body corporate.
> line 475: (1) In an Act, a reference to a person generally includes a reference to a body politic and body corporate as well as an individual.

Reading taken:

Section 17 says "person includes a body politic and a body corporate" and "party includes ...".
The definitions list those two and say "includes", so for a natural person the answer under section 17 is not covered.
Section 24AA(1) separately says a reference to a person generally includes a body politic and body corporate "as well as an individual", and the answer there is JUST TRUE for an individual.

Other reading:

Section 17 "person" excludes an individual, since only bodies are listed.
The word "includes" leaves the list open.

Rules: `s 17 "person": the entity is within a person` in `nt-part4-definitions.l4`; `s 17 "party": the entity is within a party` in `nt-part4-definitions.l4`; `s 24AA(1): the reference to a person generally includes the kind of person` in `nt-part4-reading.l4`.

Assertions: `nt-tests-part4-definitions.l4:274`, `nt-tests-part4-reading.l4:127`.

### F15: "Sufficient" in sections 66A(1) and 68

Coverage rows: s 66A(1), s 68.

Text:

> line 854: (1) If an Act requires a statutory instrument to be published in the Gazette, it is sufficient compliance with the requirement if:
> line 868: Strict compliance with the forms prescribed by or under an Act is not necessary and substantial compliance, or such compliance as the circumstances of a particular case allow, is sufficient.

Reading taken:

Section 66A(1) says it is "sufficient compliance with the requirement if" the two conditions hold, and section 68 says substantial compliance "is sufficient".
These state what is enough, not what is required: when the conditions fail, the text does not say the requirement is unmet, and the answer is not covered.

Other reading:

The "if" in section 66A(1) is an ordinary condition, so a failed condition gives JUST FALSE, as for the conditions the ruling covers.
The words "sufficient compliance" make it a statement of sufficiency.

Rules: `s 66A(1): the requirement that the instrument be published in the Gazette is satisfied` in `nt-part7-general.l4`; `s 68: the compliance with the form is sufficient` in `nt-part7-general.l4`.

Assertions: `nt-tests-part7-general.l4:11`, `nt-tests-part7-general.l4:46`.

### F16: "Alphabetical order" in section 57B

Coverage rows: s 57B.

Text:

> line 721: If an Act amends a provision of another Act that contains definitions by inserting another definition in that provision but does not specify where in that provision the definition is to be inserted, it is taken to be inserted in alphabetical order.
> line 235: Act means an Act passed by the Legislative Assembly and assented to under the Northern Territory (Self-Government) Act 1978 (Cth), and includes:
> line 239: Acting Administrator means a person appointed under the Northern Territory (Self-Government) Act 1978 (Cth) to act in the office of Administrator.
> line 240: ADI means an authorised deposit-taking institution as defined in section 5(1) of the Banking Act 1959 (Cth).
> line 241: Administrative Arrangements Order means an Administrative Arrangements Order made under section 35 and notified under section 36.

Reading taken:

The text does not say how capital letters or punctuation rank.
Section 17 prints "Act", "Acting Administrator", "ADI" and "Administrative Arrangements Order" in that order, which is the order of the letters without regard to capitals.
Terms are therefore compared with capitals made small and otherwise as given.

Other reading:

Terms are compared as given, capitals before small letters, which puts "ADI" before "Act".
The order section 17 prints does not support it.

Rules: `s 57B: the terms in the order they stand after the insertion` in `nt-part6-mechanics.l4`.

Assertions: `nt-tests-part6.l4:144`, `nt-tests-part6.l4:146`.

### F17: Items numbered "in the order" when two have the same day

Coverage rows: s 56(1), s 57(2).

Text:

> line 708: (1) The Acts which receive assent in each calendar year shall be numbered in regular arithmetical series, beginning with the number one, in the order in which they receive assent.
> line 715: (2) Subordinate legislation made in each calendar year must be numbered in regular arithmetical series, beginning with the number one, as close as possible to the order in which it is made.

Reading taken:

Sections 56(1) and 57(2) number Acts and subordinate legislation in the order in which they are assented to or made.
Where two items have the same day, the text does not say which comes first, so the number is not covered.

Other reading:

Items on the same day take the numbers in the order they happen to be listed.
The text gives no rule for it.

Rules: `s 56(2): the day on which the Act is deemed to receive assent` in `nt-part6-mechanics.l4`; `s 57(2): the number of the subordinate legislation` in `nt-part6-mechanics.l4`.

Assertions: `nt-tests-part6.l4:128`.

### F18: Periods counted in sitting days and months after a day (sections 63, 63A, 63C, 64)

Coverage rows: s 63(b), s 63A(2)(b), s 63C(3), s 63C(3)(a), s 63C(3)(b), s 64(2).

Text:

> line 774: (b) within 6 sitting days after it is made, be tabled in the Legislative Assembly.
> line 808: (a) in the case of subordinate legislation that is tabled in accordance with section 63(b) or 63A(2)(b) – 12 sitting days after the subordinate legislation is tabled; or
> line 809: (b) in the case of subordinate legislation that has not been tabled in accordance with section 63(b) or 63A(2)(b) – 12 sitting days after the last sitting day the subordinate legislation was required to be tabled.
> line 814: (2) Subordinate legislation or provisions of subordinate legislation that is the same in substance or has the same effect as the disallowed legislation must not be made within 6 months after the disallowance unless the Legislative Assembly rescinds the resolution for disallowance.

Reading taken:

"Within 6 sitting days after it is made" is up to and including the 6th sitting day after the day, the day itself being left out; "12 sitting days after" likewise.
"Within 6 months after the disallowance" is the 6 calendar months counted from the day after the disallowance.
The days on which the Legislative Assembly meets are not in the Act, so they are an input list; if the list names fewer sitting days than the count needs, the answer is not covered.

Other reading:

The day on which the instrument is made, or tabled, counts as the first of the sitting days when the Assembly sits that day.
Section 28(1) and the word "after" leave it out.

Rules: `s 17 "sitting day": the nth sitting day after` in `nt-interpretation-time.l4`; `s 63(b): the last day on which the regulation must be tabled` in `nt-part7-instruments.l4`; `s 63C(3): the last day on which notice of the resolution must be given` in `nt-part7-instruments.l4`; `s 64(2): the last day of the 6 months after the disallowance` in `nt-part7-instruments.l4`.

Assertions: `nt-tests-part7-instruments.l4:28`, `nt-tests-part7-instruments.l4:30`, `nt-tests-part7-instruments.l4:32`, `nt-tests-part7-instruments.l4:81`.

### F19: Part-day public holidays in section 28(2)

Coverage rows: s 28(2).

Text:

> line 509: (2) If the last day of any period prescribed, allowed or limited by an Act for the doing of any thing falls on a Saturday, on a Sunday or on a public holiday in the place in which the thing is to or may be done (other than a public holiday that is part of a day), the thing may be done on the first day following which is not a Saturday, a Sunday or a public holiday in that place.
> line 375: public holiday means a day or part of a day specified in, or appointed under, the Public Holidays Act 1981 to be observed as a public holiday.
> line 260: business day means a day other than:
> line 261: (a) a Saturday or Sunday; or
> line 262: (b) a day that is a public holiday in the place in which any relevant act is to be done or may be done (other than a public holiday that is part of a day).

Reading taken:

The words "(other than a public holiday that is part of a day)" follow the first mention of a public holiday.
They are read as qualifying "public holiday" wherever section 28(2) uses it: a public holiday that is part of a day neither moves a last day nor stops a day from being the day it moves to.
Section 17 "business day" states the same exclusion in terms.

Other reading:

The parenthesis qualifies only the first mention.
Section 17 defines a public holiday as "a day or part of a day", so for the day it moves to, a part-day holiday makes the day unavailable: a last day of Saturday 31 January 2026, with Monday 2 February 2026 a part-day holiday, moves to Tuesday 3 February 2026 and not to Monday 2 February 2026.
The seat offers whole-day public holidays only, which follows the reading taken.

Rules: `s 28(2): the day is a Saturday, a Sunday or a public holiday` in `nt-interpretation-time.l4`; `s 28(2): the first day, on or after the day, that is not a Saturday, a Sunday or a public holiday` in `nt-interpretation-time.l4`.

Assertions: `nt-tests-time.l4:116`, `nt-tests-time.l4:112`.

### F20: Section 19A(1)(b): both persons Aboriginal or Torres Strait Islander

Coverage rows: s 19A(1), s 19A(1)(b).

Text:

> line 439: (b) if the person is an Aboriginal or Torres Strait Islander – an Aboriginal or Torres Strait Islander to whom the person is married according to the customs and traditions of the particular community of Aboriginals or Torres Strait Islanders with which either person identifies.

Reading taken:

Paragraph (b) reads "if the person is an Aboriginal or Torres Strait Islander – an Aboriginal or Torres Strait Islander to whom the person is married according to the customs and traditions of the particular community ... with which either person identifies".
The other person must also be an Aboriginal or Torres Strait Islander, and the two must be married according to the customs of the community with which either identifies.
A marriage under the Marriage Act 1961 of the Commonwealth is paragraph (a) and needs neither.

Other reading:

Only the person need be an Aboriginal or Torres Strait Islander, and the other person is described by the marriage alone.
The words "an Aboriginal or Torres Strait Islander to whom" describe the other person.

Rules: `s 19A(1): the other person is a spouse of the person` in `nt-part4-reading.l4`.

Assertions: `nt-tests-part4-reading.l4:58`, `nt-tests-part4-reading.l4:56`.

### Rulings applied without a fork

Section 55(2) says a heading to a section "is part of the Act if" the Act was enacted after 1 July 2006 or the heading was amended or inserted after it; under the ruling on conditions the text introduces with "if", a heading for which neither holds is not part of the Act (JUST FALSE).
Assertions: `nt-tests-part6.l4:96`, `nt-tests-part6.l4:95`.

### Time questions on which the Act is silent

The Act is silent on each of these.
The encoding returns the not-covered value, and an assertion shows it, except where the row says there is nothing to assert.

| question | what the Act says | the encoding returns | assertion |
| --- | --- | --- | --- |
| a period counted in weeks | section 28 speaks of a period of time and section 17 defines no unit shorter than a month | NOTHING | `nt-tests-time.l4:86` |
| the meaning of "day" | section 17 has no entry for it | NOTHING from the table of definitions | `nt-tests-part4-definitions.l4:170` |
| the meaning of "week" | section 17 has no entry for it | NOTHING from the table of definitions | `nt-tests-part4-definitions.l4:171` |
| the meaning of "hour", and a period counted in hours | section 17 has no entry for it, and section 28 does not mention hours | NOTHING for the definition, and NOTHING for a period in hours in the seat | `nt-cases-seat.l4:43` |
| a period of no days, a negative number of days or a part of a day | section 28 does not speak of them | NOTHING | `nt-tests-time.l4:89` |
| a day on which an office is closed, other than a Saturday, a Sunday or a public holiday | section 28(2) and section 17 "business day" name those three kinds of day and no others, and the Act does not mention a closed office | only the three kinds of day are rest days; there is no input for any other (nothing further to assert) | `nt-tests-time.l4:144` |

## What the text does not answer

These return the not-covered value (`NOTHING`) in layer 1, and a test asserts each:

- a period expressed in weeks, a length of nought, a negative length or a part of a unit (section 28): `nt-tests-time.l4:86`.
- whether the day counts for a period expressed in some way other than "dating from" or "ending at, with or on" a day (section 28(1), (1A)): `nt-tests-time.l4:95`.
- counting back months or years from a day on which a period ends (section 28(1A)): `nt-tests-time.l4:99`.
- the day on which a document given to a person is taken to be served (section 25): `nt-tests-time.l4:300`.
- the day of service by fax when the number was not current or there is evidence to the contrary (section 25(3)): `nt-tests-time.l4:297`.
- the day of service by post when the day of delivery in the ordinary course of post is not known (section 25(2)): `nt-tests-time.l4:294`.
- the commencement of subordinate legislation on a day fixed by Gazette notice (section 63B(2)): `nt-tests-time.l4:272`.
- whether an individual is a "person" within section 17 (as distinct from section 24AA): `nt-tests-part4-definitions.l4:274`.
- the sitting day that is the nth after a day when the calendar names fewer than n (sections 63, 63A, 63C): `nt-tests-part7-instruments.l4:32`.
- how two items on the same day are ordered for numbering (sections 56, 57): `nt-tests-part6.l4:128`.

## Cross-references and the provision index

`nt-provisions.l4` has 535 entries and `nt-xrefs.l4` has 126 rows of references from one provision of this text to another, and 90 rows of references to another Act or instrument.
A script reads the text file and builds both modules.
The table of provisions (lines 13 to 141) gives the section numbers and headings in order, and the body (lines 149 to 962) is matched against it, so that the numbered items of examples are not taken for headings.
The header of `nt-xrefs.l4` says what the script scans for and what it leaves out.
A test per row asserts that the cited identifier is in the index and that the row's heading is the index's heading for it.
References to another Act or instrument are not resolved here; the borrowed fact is asked as an input where a rule needs it.

## Coverage

Dispositions: `encoded` (a rule, definition or table in layer 1 with a locator and tests), `fork` (the fork register entry named, and the rule that encodes the reading taken), `inert` (only for the three reasons the brief allows: not operative, machinery, or shown repealed or blank), `repealed or blank in this text` (the six section numbers listed below the table; no line of the in-scope text is shown repealed or blank).
Six section numbers are not printed in the table of provisions or in the body: 10, 32, 33, 45, 47 and 60.
The endnotes show each as repealed, so each has a row after the table below with the disposition `repealed or blank in this text`; it has no line in the in-scope text to cover.
The text prints subsections (1), (2) and (4) of section 42, (1) and (3) of section 44, and (1), (2), (3), (5), (6) and (7) of section 46; a test asserts that the provision index has no entry for the other numbers.

Rows with lines: 661, covering 814 non-blank lines; and 6 rows for section numbers that are not printed.
By disposition:

| disposition | rows | lines |
| --- | --- | --- |
| encoded | 515 | 633 |
| fork | 41 | 49 |
| inert | 105 | 132 |
| repealed or blank in this text | 6 | 0 |

By kind of row:

| kind | rows |
| --- | --- |
| definition | 144 |
| division | 6 |
| example | 9 |
| note | 7 |
| para | 143 |
| part | 10 |
| schedule | 1 |
| schedule note | 1 |
| schedule part | 4 |
| schedule row | 33 |
| section | 112 |
| sub | 191 |

| provision | heading or term | lines | disposition | where, or reason | assertions naming the rules |
| --- | --- | --- | --- | --- | --- |
| Part I | Preliminary | 149 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 1 | Short title | 150-151 | inert | reason 2: machinery (short title). The text is "This Act may be cited as the Interpretation Act 1978." Its heading is an entry in nt-provisions.l4. |  |
| s 2 | Repeal and savings | 152 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 2(1) | The Ordinances set out in Parts 1, 2 and 3 of the Schedule are repeale... | 153 | encoded | nt-schedule.l4: s 2(1), (2): what this Act does to the instrument named | 40 |
| s 2(2) | The laws of the State of South Australia set out in Part 4 of the Sche... | 154 | encoded | nt-schedule.l4: s 2(1), (2): what this Act does to the instrument named | 40 |
| s 2(3) | Where there is, in an Act, or a law of the State of South Australia in... | 155 | encoded | nt-part1-application.l4: s 2(3): the provision of the earlier law continues to apply to the word, expression or provision | 4 |
| s 2(4) | Notwithstanding the repeal effected by this section, in the interpreta... | 156 | encoded | nt-part1-application.l4: s 2(4): reference is made to the law in force when the thing was done or suffered, and not to this Act | 3 |
| s 3 | Application of this Act | 157 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 3(1) | Subject to section 2, this Act applies to each Act, and to each Ordina... | 158 | fork F9 | nt-part1-application.l4: s 3(1): this Act applies to the law as though the law were an Act | 8 |
| s 3(2) | This Act binds the Crown not only in right of the Territory but, so fa... | 159 | encoded | nt-part1-application.l4: s 3(2): this Act binds the Crown in the capacity | 4 |
| s 3(3) | In the application of a provision of this Act to a provision, whether ... | 160 | encoded | nt-part1-application.l4: s 3(3): the provision of this Act yields to the other provision | 2 |
| s 4 | Application to statutory instruments | 161-162 | fork F4 | nt-part1-application.l4: s 4: the way in which this Act applies to the thing | 8 |
| s 4(a) | to and in respect of statutory instruments made under laws to which th... | 163 | fork F4 | nt-part1-application.l4: s 4: the way in which this Act applies to the thing | 8 |
| s 4(b) | without limiting its general application: | 164-166 | encoded | nt-part1-application.l4: s 4: the way in which this Act applies to the thing | 8 |
| Part II | Commencement of Acts | 167 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 5 | Date of commencement | 168 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 5(1) | An Act commences on the day specified or provided for in the Act. | 169 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(2) | An Act may be specified to commence: | 170 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(2)(a) | on a particular day or on a number of different days; or | 171 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(2)(b) | on a day to be fixed by Gazette notice; or | 172 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(2)(c) | on the happening of a particular event or events. | 173 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(2) Example for subsection (2)(c) | Example for subsection (2)(c) | 174-175 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 5(3) | If an Act is specified to commence as specified in subsection (2)(b): | 176 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(3)(a) | a single day or time may be fixed; or | 177 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(3)(b) | different days or times may be fixed for different provisions of the A... | 178 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 5(4) | If an Act does not specify or provide for its commencement, or the com... | 179 | encoded | nt-interpretation-time.l4: s 5: the day on which an Act or a provision commences | 9 |
| s 6 | Proposed laws reserved for Governor-General | 180-181 | encoded | nt-interpretation-time.l4: s 6: the first day on which a proposed law reserved for the Governor-General has effect | 4 |
| s 6 Note for section 6 | Note for section 6 | 182-183 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 6A | Time of commencement | 184-185 | encoded | nt-interpretation-time.l4 (3 rules) | 8 |
| s 6B | References to commencement | 186-187 | encoded | nt-interpretation-time.l4: s 6B: the commencement of the provisions concerned | 6 |
| s 6B(a) | if the provisions concerned commence on a single day or at a particula... | 188 | encoded | nt-interpretation-time.l4: s 6B: the commencement of the provisions concerned | 6 |
| s 6B(b) | if different parts of the provisions concerned commence on different d... | 189 | encoded | nt-interpretation-time.l4: s 6B: the commencement of the provisions concerned | 6 |
| s 7 | Evidence of assent etc. | 190 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 7(1) | The date appearing on a copy of an Act printed by the Government Print... | 191 | encoded | nt-part2-commencement.l4: s 7: the day of which the date appearing on the printed copy is evidence | 7 |
| s 7(2) | The date appearing on a copy of an Act printed by the Government Print... | 192 | encoded | nt-part2-commencement.l4: s 7: the day of which the date appearing on the printed copy is evidence | 7 |
| s 7(3) | The dates appearing on a copy of subordinate legislation printed by th... | 193, 196 | encoded | nt-part2-commencement.l4: s 7: the day of which the date appearing on the printed copy is evidence | 7 |
| s 7(3)(a) | the date on which the subordinate legislation was made; and | 194 | encoded | nt-part2-commencement.l4: s 7: the day of which the date appearing on the printed copy is evidence | 7 |
| s 7(3)(b) | the date on which the subordinate legislation was notified in the Gaze... | 195 | encoded | nt-part2-commencement.l4: s 7: the day of which the date appearing on the printed copy is evidence | 7 |
| s 8 | Exercise of powers before commencement | 197 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 8(1) | A power to make a statutory instrument, or to do any other thing, unde... | 198 | encoded | nt-part2-commencement.l4: s 8(1): the power may be exercised before the provision commences | 2 |
| s 8(1) Examples of powers under subsection (1) | Examples of powers under subsection (1) | 199-202 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 8(2) | The statutory instrument or other thing may take effect either: | 203 | fork F10 | nt-part2-commencement.l4: s 8(2): the instrument or thing may take effect on that day | 5 |
| s 8(2)(a) | on the commencement of the provision under which the power was exercis... | 204 | fork F10 | nt-part2-commencement.l4: s 8(2): the instrument or thing may take effect on that day | 5 |
| s 8(2)(b) | before the commencement of the provision under which the power was exe... | 205 | fork F10 | nt-part2-commencement.l4: s 8(2): the instrument or thing may take effect on that day | 5 |
| s 8(3) | Subsection (1) applies whether the provision is in the Act as enacted ... | 206 | encoded | nt-part2-commencement.l4: s 8(3): subsection (1) applies to the provision | 3 |
| s 9 | Amendment before commencement | 207-208, 211 | fork F11 | nt-part2-commencement.l4 (2 rules) | 6 |
| s 9(a) | it may be cited by its proposed short title; and | 209 | fork F11 | nt-part2-commencement.l4: s 9(a), (b): the proposed law may be cited by its proposed short title and be the subject of a further proposed law to amend or repeal it | 3 |
| s 9(b) | it may be the subject of a further proposed law to amend or repeal it, | 210 | fork F11 | nt-part2-commencement.l4: s 9(a), (b): the proposed law may be cited by its proposed short title and be the subject of a further proposed law to amend or repeal it | 3 |
| Part III | Repeal and expiration of Acts | 212 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 11 | Repeal does not revive previous Act | 213-214 | encoded | nt-interpretation-time.l4: s 11: the repeal has the effect of reviving the previous Act or part | 4 |
| s 12 | Effect of repeal | 215-216, 221 | encoded | nt-interpretation-time.l4: s 12(a): the repeal revives the thing; s 12: the thing may be instituted, continued, enforced or imposed as if the repealing Act had not been made | 6 |
| s 12(a) | revive anything not in force or existing at the time at which the repe... | 217 | encoded | nt-interpretation-time.l4: s 12(a): the repeal revives the thing; s 12(a): the thing was in force or existing at the time at which the repeal takes effect | 7 |
| s 12(b) | affect the previous operation of the Act or the part of the Act so rep... | 218 | encoded | nt-interpretation-time.l4: s 12(b), (c), (d): the repeal affects the thing | 7 |
| s 12(c) | affect a right, privilege, obligation or liability acquired, accrued o... | 219 | encoded | nt-interpretation-time.l4: s 12(b), (c), (d): the repeal affects the thing | 7 |
| s 12(d) | affect a penalty, forfeiture or punishment incurred in respect of an o... | 220 | encoded | nt-interpretation-time.l4: s 12(b), (c), (d): the repeal affects the thing | 7 |
| s 13 | Effect of State laws ceasing to apply | 222-223 | encoded | nt-interpretation-time.l4: s 13: the sections that apply as if the law of the State were an Act or part repealed | 2 |
| s 14 | Continuance of repealed provisions | 224-225 | encoded | nt-interpretation-time.l4: s 14: the repealed provisions continue in force on | 4 |
| s 15 | References to repealed provisions | 226 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 15(1) | If an Act repeals and re-enacts, with or without modification, any pro... | 227 | encoded | nt-interpretation-time.l4: s 15: a reference to the provision repealed is taken to be a reference to the provision re-enacted | 7 |
| s 15(2) | If a Commonwealth Act or legislative instrument repeals and re‑enacts,... | 228 | encoded | nt-interpretation-time.l4: s 15: a reference to the provision repealed is taken to be a reference to the provision re-enacted | 7 |
| s 15(3) | If a State, Territory or New Zealand Act or subordinate legislation re... | 229 | encoded | nt-interpretation-time.l4: s 15: a reference to the provision repealed is taken to be a reference to the provision re-enacted | 7 |
| s 16 | Expiration of Acts | 230-231 | encoded | nt-interpretation-time.l4: s 16: the sections that apply as though the Act or part had been repealed | 2 |
| Part IV | Words and references in Acts | 232 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 17 | Definitions | 233-234 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). The introduction "In an Act:" only introduces the definitions that follow, each its own row. The heading is carried as data in nt-provisions.l4. |  |
| s 17 "Act" | Act | 235-238 | encoded | nt-part4-definitions.l4 (1 rule) | 6 |
| s 17 "Acting Administrator" | Acting Administrator | 239 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "ADI" | ADI | 240 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "Administrative Arrangements Order" | Administrative Arrangements Order | 241 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Administrator" | Administrator | 242 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "adult" | adult | 243 | encoded | nt-part4-definitions.l4 (2 rules) | 5 |
| s 17 "affidavit" | affidavit | 244 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Agency" | Agency | 245 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "appropriation" | appropriation | 246 | encoded | nt-part4-definitions.l4 (1 rule) | 4 |
| s 17 "ASIC" | ASIC | 247 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "ASIC Act" | ASIC Act | 248 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Associate Judge" | Associate Judge | 249 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Attorney-General" | Attorney-General | 250 | encoded | nt-part4-definitions.l4 (1 rule) | 4 |
| s 17 "Auditor-General" | Auditor-General | 251 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "Australian Crime Commission" | Australian Crime Commission | 252 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "bank" | bank | 253-255 | encoded | nt-part4-definitions.l4 (2 rules) | 4 |
| s 17 "bank cheque or banker's cheque" | bank cheque or banker's cheque | 256 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "building society" | building society | 257-259 | encoded | nt-part4-definitions.l4 (2 rules) | 4 |
| s 17 "business day" | business day | 260-262 | encoded | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 5 |
| s 17 "calendar month" | calendar month | 263-265 | fork F2 | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 10 |
| s 17 "calendar year" | calendar year | 266 | encoded | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Central Holding Authority" | Central Holding Authority | 267 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Chief Health Officer" | Chief Health Officer | 268 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Chief Judge" | Chief Judge | 269 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Chief Justice" | Chief Justice | 270 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Civil and Administrative Tribunal" | Civil and Administrative Tribunal | 271 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Commissioner of Correctional Services" | Commissioner of Correctional Services | 272 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Commissioner of Police" | Commissioner of Police | 273 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "commissioner for oaths" | commissioner for oaths | 274 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "committed for trial" | committed for trial | 275-277 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "Commonwealth" | Commonwealth | 278 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Commonwealth Act" | Commonwealth Act | 279 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Consolidated Revenue Account" | Consolidated Revenue Account | 280 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "contravene" | contravene | 281 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Corporations Act 2001" | Corporations Act 2001 | 282 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "court of competent jurisdiction" | court of competent jurisdiction | 283 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "credit union" | credit union | 284 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "Criminal Code" | Criminal Code | 285 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "de facto partner" | de facto partner | 286 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "de facto relationship" | de facto relationship | 287 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "department" | department | 288 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "document" | document | 289-297 | encoded | nt-part4-definitions.l4 (2 rules) | 8 |
| s 17 "Electoral Commission" | Electoral Commission | 298 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Electoral Commissioner" | Electoral Commissioner | 299 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "estate" | estate | 300 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "Executive Council" | Executive Council | 301 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "external territory" | external territory | 302 | encoded | nt-part4-definitions.l4 (2 rules) | 5 |
| s 17 "Family Court" | Family Court | 303 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Federal Circuit Court" | Federal Circuit Court | 304 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Federal Circuit Court and Family Court of Australia" | Federal Circuit Court and Family Court of Australia | 305 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Federal Court" | Federal Court | 306 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "financial year" | financial year | 307 | encoded | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "friendly society" | friendly society | 308 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "function" | function | 309 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Gazette, Government Gazette, Northern Territory Government Gazette or Gazette of the Northern Territory" | Gazette, Government Gazette, Northern Territory Government Gazette or Gazette of the Northern Territory | 310 | encoded | nt-part4-definitions.l4 (2 rules) | 5 |
| s 17 "Gazette notice" | Gazette notice | 311 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "Government Printer" | Government Printer | 312 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Health Practitioner Regulation National Law" | Health Practitioner Regulation National Law | 313-317 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Health Practitioner Regulation National Law" Note for definition Health Practitioner Regulation National Law | Note for definition Health Practitioner Regulation National Law | 318-319 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 17 "husband" | husband | 320 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "ICAC" | ICAC | 321 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Imperial Act" | Imperial Act | 322 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "indictable offence" | indictable offence | 323-325 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "indictment" | indictment | 326 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "individual" | individual | 327 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "infant" | infant | 328 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "insert" | insert | 329 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "instrument of a legislative or administrative character" | instrument of a legislative or administrative character | 330 | encoded | nt-part4-definitions.l4 (2 rules) | 4 |
| s 17 "justice of the peace" | justice of the peace | 331 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "land" | land | 332 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "law of the Territory" | law of the Territory | 333-337 | encoded | nt-part4-definitions.l4 (2 rules) | 5 |
| s 17 "lawyer" | lawyer | 338 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "legal practitioner" | legal practitioner | 339 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "legislation website" | legislation website | 340-342 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "Legislative Assembly" | Legislative Assembly | 343 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Local Court" | Local Court | 344 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Local Court Judge" | Local Court Judge | 345 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "local government area" | local government area | 346 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "local government council" | local government council | 347 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "marriage" | marriage | 348 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "medical practitioner" | medical practitioner | 349 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "member of the Police Force" | member of the Police Force | 350 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "minister" | minister | 351 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Ministerial office" | Ministerial office | 352 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "monetary unit" | monetary unit | 353 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "month" | month | 354 | fork F2 | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 4 |
| s 17 "Northern Territory Government Account" | Northern Territory Government Account | 355 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "notified in the Gazette" | notified in the Gazette | 356-360 | encoded | nt-part4-definitions.l4 (2 rules) | 6 |
| s 17 "NTCAT" | NTCAT | 361 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "oath" | oath | 362 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Ordinance" | Ordinance | 363-365 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Parliament" | Parliament | 366 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "party" | party | 367 | fork F14 | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "penalty unit" | penalty unit | 368 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "person" | person | 369 | fork F14 | nt-part4-definitions.l4 (2 rules) | 4 |
| s 17 "person" Note for definition of person | Note for definition of person | 370-371 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 17 "police officer" | police officer | 372 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "prescribed" | prescribed | 373 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "proclamation" | proclamation | 374 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "public holiday" | public holiday | 375 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "public place" | public place | 376-379 | encoded | nt-part4-definitions.l4 (2 rules) | 4 |
| s 17 "public sector employee" | public sector employee | 380 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "real property" | real property | 381 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Registrar-General" | Registrar-General | 382 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "regulatory offence" | regulatory offence | 383 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "revenue unit" | revenue unit | 384 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "see" | see | 385 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "sitting day" | sitting day | 386 | encoded | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 9 |
| s 17 "Speaker" | Speaker | 387 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "spouse" | spouse | 388 | encoded | nt-part4-definitions.l4 (1 rule) | 4 |
| s 17 "State" | State | 389 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "statutory corporation" | statutory corporation | 390 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "statutory declaration" | statutory declaration | 391 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "statutory instrument" | statutory instrument | 392 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "stepchild" | stepchild | 393 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "step-relative" | step-relative | 394 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "subordinate legislation" | subordinate legislation | 395-397 | encoded | nt-part4-definitions.l4 (2 rules) | 3 |
| s 17 "summary offence" | summary offence | 398 | encoded | nt-part4-definitions.l4 (1 rule) | 2 |
| s 17 "Supreme Court" | Supreme Court | 399 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Supreme Court Judge" | Supreme Court Judge | 400 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "table" | table | 401 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Territory" | Territory | 402 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "the Agency" | the Agency | 403 | encoded | nt-part4-definitions.l4 (1 rule) | 4 |
| s 17 "the Chief Executive Officer" | the Chief Executive Officer | 404 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "the Minister" | the Minister | 405 | encoded | nt-part4-definitions.l4 (1 rule) | 5 |
| s 17 "the Regulations" | the Regulations | 406 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "the Territory" | the Territory | 407 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "this Act" | this Act | 408 | encoded | nt-part4-definitions.l4 (2 rules) | 2 |
| s 17 "Treasurer" | Treasurer | 409 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Under Treasurer" | Under Treasurer | 410 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "Valuer-General" | Valuer-General | 411 | encoded | nt-part4-definitions.l4 (1 rule) | 1 |
| s 17 "widow" | widow | 412 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "widower" | widower | 413 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "wife" | wife | 414 | encoded | nt-part4-definitions.l4 (1 rule) | 3 |
| s 17 "year" | year | 415 | fork F2 | nt-interpretation-time.l4 (1 rule); nt-part4-definitions.l4 (1 rule) | 1 |
| s 18 | Definitions to be read in context | 416-417 | encoded | nt-part4-reading.l4: s 18: a definition in or applicable to an Act applies | 2 |
| s 18A | References relating to an Agency | 418 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 18A(1) | An Agency is a department or unit of a department, or other authority ... | 419 | encoded | nt-part4-reading.l4: s 18A(1): the body is an Agency | 5 |
| s 18A(1)(a) | nominated as an Agency in an Administrative Arrangements Order; or | 420 | encoded | nt-part4-reading.l4: s 18A(1): the body is an Agency | 5 |
| s 18A(1)(b) | declared by an Act to be an Agency for the Public Sector Employment an... | 421 | encoded | nt-part4-reading.l4: s 18A(1): the body is an Agency | 5 |
| s 18A(2) | A reference to the Agency in a provision of an Act is a reference to t... | 422 | encoded | nt-part4-reading.l4: s 18A(2): the Agency that "the Agency" refers to in a provision | 2 |
| s 18A(3) | A reference to the Agency administering a provision of an Act or havin... | 423 | encoded | nt-part4-reading.l4: s 18A(3): the Agencies that the reference is a reference to | 4 |
| s 18A(4) | A reference to a specified Agency (including a reference to an Agency ... | 424 | encoded | nt-part4-reading.l4: s 18A(4): what a reference to the specified Agency includes | 2 |
| s 19 | Ministerial references | 425 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 19(1) | A minister is a person holding a Ministerial office. | 426 | encoded | nt-part4-reading.l4: s 19(1): the person is a minister | 2 |
| s 19(2) | A reference in an Act to the Minister: | 427 | encoded | nt-part4-reading.l4: s 19(2): the person is referred to by "the Minister" in the Act | 3 |
| s 19(2)(a) | is a reference to: | 428-430 | encoded | nt-part4-reading.l4: s 19(2): the person is referred to by "the Minister" in the Act | 3 |
| s 19(2)(b) | includes a minister acting for the Minister. | 431 | encoded | nt-part4-reading.l4: s 19(2): the person is referred to by "the Minister" in the Act | 3 |
| s 19(3) | A reference to the minister administering a provision of an Act or hav... | 432 | encoded | nt-part4-reading.l4: s 19(3): the ministers that the reference is a reference to | 4 |
| s 19(4) | A reference in a provision of an Act to the Minister or a specified mi... | 433 | encoded | nt-part4-reading.l4: s 19(4): what a reference to the specified minister includes | 2 |
| s 19(5) | If a reference is made in a provision of an Act to the Minister and th... | 434 | encoded | nt-part4-reading.l4: s 19(5): the reference is a reference to any minister | 3 |
| s 19A | Definitions of certain domestic relationships | 435 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 19A(1) | In any Act: | 436-437 | fork F20 | nt-part4-reading.l4: s 19A(1): the other person is a spouse of the person | 6 |
| s 19A(1)(a) | a person to whom the person is validly married under the Marriage Act ... | 438 | encoded | nt-part4-reading.l4: s 19A(1): the other person is a spouse of the person | 6 |
| s 19A(1)(b) | if the person is an Aboriginal or Torres Strait Islander – an Aborigin... | 439 | fork F20 | nt-part4-reading.l4: s 19A(1): the other person is a spouse of the person | 6 |
| s 19A(2) | In any Act, marriage, husband, wife, widow and widower have the meanin... | 440 | encoded | nt-part4-reading.l4: s 19A(2): the term has the meaning that corresponds with the meaning of spouse | 6 |
| s 19A(3) | In any Act, de facto partner and de facto relationship have the meanin... | 441 | encoded | nt-part4-reading.l4: s 19A(3): where the meaning of the term is to be found | 3 |
| s 19A(4) | In any Act: | 442-443 | encoded | nt-part4-reading.l4: s 19A(4): the child is a stepchild of the person | 5 |
| s 19A(4)(a) | if the person is married – a child of the person's spouse but not a ch... | 444 | encoded | nt-part4-reading.l4: s 19A(4): the child is a stepchild of the person | 5 |
| s 19A(4)(b) | if the person is in a de facto relationship – a child of the person's ... | 445 | encoded | nt-part4-reading.l4: s 19A(4): the child is a stepchild of the person | 5 |
| s 19A(5) | In any Act, a reference to a step-relative of a person is read as havi... | 446 | encoded | nt-part4-reading.l4: s 19A(5): the term has the meaning that corresponds with the meaning of stepchild | 2 |
| s 20 | Construction of statutory instruments | 447 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 20(1) | Words, expressions and provisions in a statutory instrument have the s... | 448 | encoded | nt-part4-reading.l4: s 20(1): the meaning that a word, expression or provision has in a statutory instrument | 2 |
| s 20(2) | A reference in a statutory instrument to the Act is a reference to the... | 449 | encoded | nt-part4-reading.l4: s 20(2): the Act that "the Act" refers to in a statutory instrument | 1 |
| s 21 | By, under or pursuant to Act | 450-451 | encoded | nt-part4-reading.l4: s 21: the thing is by, under, pursuant to or in pursuance of the Act | 3 |
| s 22 | Construction of amending Acts | 452-453 | encoded | nt-part4-reading.l4: s 22: the meaning that a word, expression or provision has in an amending Act | 2 |
| s 23 | Parts of speech and grammatical forms | 454-455 | encoded | nt-part4-reading.l4: s 23: the form has a corresponding meaning | 3 |
| s 23A | Defined words in Acts and references in other legislation | 456 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 23A(1) | This section applies to a word or term defined in a particular way in ... | 457 | encoded | nt-part4-reading.l4: s 23A: the idea is taken to be different because of the spelling | 5 |
| s 23A(2) | In subordinate legislation made under that Act or in other Acts or sub... | 458 | encoded | nt-part4-reading.l4: s 23A: the idea is taken to be different because of the spelling | 5 |
| s 23A Note for section 23A | Note for section 23A | 459-460 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 24 | Gender and number | 461 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 24(1) | In an Act, any language that indicates or could be taken to indicate a... | 462 | encoded | nt-part4-reading.l4: s 24(1): the language includes the individual, regardless of gender or sex | 3 |
| s 24(2) | In an Act: | 463 | encoded | nt-part4-reading.l4: s 24(2): the word as used includes the word in the other number | 3 |
| s 24(2)(a) | words in the singular include the plural; and | 464 | encoded | nt-part4-reading.l4: s 24(2): the word as used includes the word in the other number | 3 |
| s 24(2)(b) | words in the plural include the singular. | 465 | encoded | nt-part4-reading.l4: s 24(2): the word as used includes the word in the other number | 3 |
| s 24 Examples for section 24(2) | Examples for section 24(2) | 466-468 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 24A | Range of numbers, words or other things | 469-470 | encoded | nt-part4-reading.l4: s 24A: the number is included in the range of numbers; s 24A: the word is included in the range of words | 10 |
| s 24A Examples for section 24A | Examples for section 24A | 471-473 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 24AA | References to persons generally | 474 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 24AA(1) | In an Act, a reference to a person generally includes a reference to a... | 475 | fork F14 | nt-part4-reading.l4: s 24AA(1): the reference to a person generally includes the kind of person | 5 |
| s 24AA(1) Examples of references to persons generally in subsection (1) | Examples of references to persons generally in subsection (1) | 476-480 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 24AA(2) | Subsection (1) is not displaced merely because there is an express ref... | 481 | encoded | nt-part4-reading.l4: s 24AA(2): subsection (1) is displaced | 2 |
| s 25 | Service of documents | 482 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 25(1) | A person may serve a document on an individual or body (the recipient)... | 483 | encoded | nt-part4-reading.l4: s 25(1): a person may serve the document on the recipient in that way | 12 |
| s 25(1)(a) | by giving it to: | 484-487 | encoded | nt-part4-reading.l4: s 25(1): a person may serve the document on the recipient in that way | 12 |
| s 25(1)(b) | by sending it by prepaid post addressed to the recipient at the recipi... | 488 | encoded | nt-part4-reading.l4: s 25(1): a person may serve the document on the recipient in that way | 12 |
| s 25(1)(c) | by sending it to the recipient by fax; or | 489 | encoded | nt-part4-reading.l4: s 25(1): a person may serve the document on the recipient in that way | 12 |
| s 25(1)(d) | by leaving it, addressed to the recipient, at the recipient's address ... | 490 | encoded | nt-part4-reading.l4: s 25(1): a person may serve the document on the recipient in that way | 12 |
| s 25(2) | A document served under subsection (1)(b) is taken to be served when i... | 491 | fork F6 | nt-interpretation-time.l4: s 25(2), (3), (4): the day on which a document is taken to be served | 7 |
| s 25(3) | Subject to evidence to the contrary, a document served under subsectio... | 492 | fork F6, F7 | nt-interpretation-time.l4: s 25(2), (3), (4): the day on which a document is taken to be served | 7 |
| s 25(4) | A document served under subsection (1)(d) is taken to be served when i... | 493 | fork F6 | nt-interpretation-time.l4: s 25(2), (3), (4): the day on which a document is taken to be served | 7 |
| s 25(5) | This section has effect for the service of a document whether or not t... | 494 | encoded | nt-part4-reading.l4: s 25(5): section 25 has effect for the service of the document | 3 |
| s 25(6) | In this section: | 495 | inert | reason 1: not operative. "(6) In this section:" only introduces the definitions that follow, each its own row. |  |
| s 25 "address" | address | 496 | encoded | nt-part4-reading.l4 (1 rule) | 2 |
| s 25 "body" | body | 497 | encoded | nt-part4-reading.l4 (1 rule) | 2 |
| s 25 "document" | document | 498 | encoded | nt-part4-reading.l4 (1 rule) | 2 |
| s 25 "executive officer" | executive officer | 499-501 | encoded | nt-part4-reading.l4 (1 rule) | 4 |
| s 26 | References to writing | 502-503 | encoded | nt-part4-reading.l4: s 26: the mode of representing or reproducing is within a reference to writing | 3 |
| s 27 | Measurement of distance | 504-505 | encoded | nt-part4-reading.l4: s 27: the distance in metres between the two points measured in a straight line in a horizontal plane | 3 |
| s 28 | Reckoning of time | 506 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 28(1) | If in an Act a period of time dating from a given day, act or event is... | 507 | fork F1, F2, F4, F5 | nt-interpretation-time.l4 (4 rules) | 36 |
| s 28(1A) | If an Act provides that a period of time ends at, with or on a given d... | 508 | fork F1 | nt-interpretation-time.l4 (3 rules) | 16 |
| s 28(2) | If the last day of any period prescribed, allowed or limited by an Act... | 509 | fork F3, F5, F19 | nt-interpretation-time.l4 (4 rules) | 19 |
| s 28(3) | In an Act, a reference to time must be read as a reference to standard... | 510 | encoded | nt-interpretation-time.l4: s 28(3): a reference to time is read as a reference to | 1 |
| s 28(4) | A reference in an Act to a thing existing or having effect from time t... | 511 | encoded | nt-interpretation-time.l4: s 28(4), (5): a time expression is read as | 3 |
| s 28(5) | A reference in an Act to a thing existing or having effect for the tim... | 512 | encoded | nt-interpretation-time.l4: s 28(4), (5): a time expression is read as | 3 |
| s 29 | 24 hour clock | 513 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 29(1) | A reference in an Act to a time of day expressed as 4 digits in hours ... | 514 | encoded | nt-interpretation-time.l4: s 29: the time after midnight for four digits | 9 |
| s 29(2) | For the purposes of subsection (1), where the first of 2 digits consti... | 515 | encoded | nt-interpretation-time.l4: s 29: the time after midnight for four digits | 9 |
| s 30 | Reckoning of age | 516 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 30(1) | In the reckoning of age of a person for the purposes of any Act, the p... | 517 | encoded | nt-interpretation-time.l4: s 30(1): the day on which a person attains the age; s 30(1): the person has attained the age on | 7 |
| s 30(2) | Subject to subsection (3), if an Act refers to the anniversary of the ... | 518 | encoded | nt-interpretation-time.l4: s 30(2), (3): the day on which the anniversary of the birth occurs in | 6 |
| s 30(3) | If a person was born on 29 February in any year, then, in any subseque... | 519 | encoded | nt-interpretation-time.l4: s 30(2), (3): the day on which the anniversary of the birth occurs in | 6 |
| s 31 | References to the Sovereign | 520-521 | encoded | nt-part4-reading.l4: s 31: the Sovereign to whom the reference is a reference | 2 |
| s 34 | References to Administrator | 522 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 34(1) | Subject to this section, a provision of an Act that confers upon the A... | 523 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(2) | The Administrator may, without reference to the Executive Council: | 524 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(2)(a) | exercise a power to fix a date for the bringing into operation of an A... | 525 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(2)(b) | exercise any other power or perform any function that the Administrato... | 526 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(3) | The Administrator may, without reference to the Executive Council: | 527, 530 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(3)(a) | exercise any power where the exercise of that power relates only to; o... | 528 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34(3)(b) | perform any function where the performance of that function relates on... | 529 | encoded | nt-part4-reading.l4: s 34: the Administrator may exercise the power or perform the function without the advice of the Executive Council | 4 |
| s 34A | References to Administrator in Council | 531-532 | encoded | nt-part4-reading.l4: s 34A: the reference is read as a reference to the Administrator, with section 34 applying | 2 |
| s 35 | Administrative Arrangements Order | 533 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 35(1) | The Administrator may make an Administrative Arrangements Order. | 534 | encoded | nt-part4-reading.l4: s 35(1): the person may make an Administrative Arrangements Order | 2 |
| s 35(2) | An Administrative Arrangements Order may do any of the following: | 535 | encoded | nt-part4-reading.l4: s 35(2): an Administrative Arrangements Order may do the thing | 7 |
| s 35(2)(a) | nominate a department or other authority or body as an Agency; | 536 | encoded | nt-part4-reading.l4: s 35(2): an Administrative Arrangements Order may do the thing | 7 |
| s 35(2)(b) | allocate to a specified minister or the minister holding a specified M... | 537-540 | encoded | nt-part4-reading.l4: s 35(2): an Administrative Arrangements Order may do the thing | 7 |
| s 35(2)(c) | allocate to an Agency nominated under paragraph (a): | 541-543 | encoded | nt-part4-reading.l4: s 35(2): an Administrative Arrangements Order may do the thing | 7 |
| s 35(2) Note for subsection (2)(a) | Note for subsection (2)(a) | 544-545 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 35(3) | For subsection (2)(b)(i): | 546 | encoded | nt-part4-reading.l4: s 35(3): the arrangement is available for the administration of an Act or a provision | 4 |
| s 35(3)(a) | different provisions of an Act may be administered by different minist... | 547 | encoded | nt-part4-reading.l4: s 35(3): the arrangement is available for the administration of an Act or a provision | 4 |
| s 35(3)(b) | different ministers may administer an Act in different respects; and | 548 | encoded | nt-part4-reading.l4: s 35(3): the arrangement is available for the administration of an Act or a provision | 4 |
| s 35(3)(c) | 2 or more ministers may jointly administer the same Act or the same pr... | 549 | encoded | nt-part4-reading.l4: s 35(3): the arrangement is available for the administration of an Act or a provision | 4 |
| s 35(4) | For subsection (3)(c), the joint administration of an Act or provision... | 550 | encoded | nt-part4-reading.l4: s 35(4): the joint administration requires the ministerial function to be exercised jointly | 2 |
| s 35(5) | The administration of any Act not allocated to a minister or an Agency... | 551 | encoded | nt-part4-reading.l4: s 35(5): the minister and Agency to which the administration of the Act is allocated | 2 |
| s 36 | Publication and commencement of Administrative Arrangements Order | 552 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 36(1) | Notice of the making of an Administrative Arrangements Order must be p... | 553 | encoded | nt-part4-reading.l4: s 36(1), (2): the notice meets the requirements for an Administrative Arrangements Order | 3 |
| s 36(2) | The notice must specify where a copy of the Administrative Arrangement... | 554 | encoded | nt-part4-reading.l4: s 36(1), (2): the notice meets the requirements for an Administrative Arrangements Order | 3 |
| s 36(3) | An Administrative Arrangements Order takes effect: | 555 | encoded | nt-part4-reading.l4: s 36(3): the day on which an Administrative Arrangements Order takes effect | 4 |
| s 36(3)(a) | when notice of its making is published under subsection (1); or | 556 | encoded | nt-part4-reading.l4: s 36(3): the day on which an Administrative Arrangements Order takes effect | 4 |
| s 36(3)(b) | at a later time specified in the Administrative Arrangements Order. | 557 | encoded | nt-part4-reading.l4: s 36(3): the day on which an Administrative Arrangements Order takes effect | 4 |
| s 37 | References in agreements | 558-559 | encoded | nt-part4-reading.l4: s 37: what the reference in the agreement is read as | 4 |
| s 37(a) | a reference in the agreement to the Minister administering the first-m... | 560 | encoded | nt-part4-reading.l4: s 37: what the reference in the agreement is read as | 4 |
| s 37(b) | a reference in the agreement to the first-mentioned Agency shall be re... | 561 | encoded | nt-part4-reading.l4: s 37: what the reference in the agreement is read as | 4 |
| s 38 | References to offices etc. | 562 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38(1) | In an Act: | 563 | encoded | nt-part4-reading.l4: s 38(1): the reference is construed as a reference to the thing for, or in and of, the Territory | 3 |
| s 38(1)(a) | a reference to an officer or office shall be construed as a reference ... | 564 | encoded | nt-part4-reading.l4: s 38(1): the reference is construed as a reference to the thing for, or in and of, the Territory | 3 |
| s 38(1)(b) | references to localities, jurisdictions and other matters and things s... | 565 | encoded | nt-part4-reading.l4: s 38(1): the reference is construed as a reference to the thing for, or in and of, the Territory | 3 |
| s 38(2) | Where, in relation to a power or function, there is, in a provision of... | 566 | encoded | nt-part4-reading.l4: s 38(2): the reference is read as including the candidate | 7 |
| s 38(2)(a) | a reference to a person, officer, office or body for the time being ha... | 567 | encoded | nt-part4-reading.l4: s 38(2): the reference is read as including the candidate | 7 |
| s 38(2)(b) | if there is no person, officer, office or body for the time being havi... | 568 | encoded | nt-part4-reading.l4: s 38(2): the reference is read as including the candidate | 7 |
| s 38(2)(c) | if there is no person, officer, office or body for the time being havi... | 569 | encoded | nt-part4-reading.l4: s 38(2): the reference is read as including the candidate | 7 |
| s 38(3) | Where in an Act or in an order made under subsection (2), a person hol... | 570 | encoded | nt-part4-reading.l4: s 38(3): the mention includes the person | 3 |
| s 38A | Reference to Commonwealth ministers etc. | 571 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38A(1) | Notwithstanding section 38, where in a provision of an Act reference i... | 572 | encoded | nt-part4-reading.l4: s 38A(1): what the reference to the Commonwealth minister, department or body is read as | 3 |
| s 38A(2) | Where in a provision of an Act reference is made to a Commonwealth min... | 573 | encoded | nt-part4-reading.l4 (1 rule) | 4 |
| Part IVA | Penalties | 574 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38B | Penal provisions include bodies corporate | 575-576 | encoded | nt-part4a-penalties.l4: s 38B: the provision is read as referring to the offender | 4 |
| s 38C | Penalties at foot of sections and subsections | 577 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38C(1) | The penalty, pecuniary or otherwise, set out: | 578, 581 | encoded | nt-part4a-penalties.l4 (3 rules) | 11 |
| s 38C(1)(a) | at the foot of a section; or | 579 | encoded | nt-part4a-penalties.l4 (3 rules) | 11 |
| s 38C(1)(b) | at the foot of a subsection, | 580 | encoded | nt-part4a-penalties.l4 (3 rules) | 11 |
| s 38C(1AA) | Subsection (1) applies regardless of whether the penalty is expressed ... | 582 | encoded | nt-part4a-penalties.l4: s 38C(1AA): subsection (1) applies to the penalty | 2 |
| s 38C(1A) | For subsection (1), a penalty is taken to be at the foot of a section ... | 583 | encoded | nt-part4a-penalties.l4: s 38C(1A): the penalty is taken to be at the foot of the section or subsection | 2 |
| s 38C(2) | A penalty set out as provided in subsection (1) which is expressed to ... | 584 | encoded | nt-part4a-penalties.l4: s 38C(2): the penalty applies according to the tenor of the provision | 2 |
| s 38C(3) | In this section section includes a rule, regulation or by-law and subs... | 585 | encoded | nt-part4a-penalties.l4: s 38C(3): the thing is a section for the purposes of section 38C | 5 |
| s 38DC | Body corporate fines under provision authorising subordinate legislation | 586 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38DC(1) | This section applies to a provision of an Act authorising a maximum fi... | 587 | encoded | nt-part4a-penalties.l4: s 38DC(1): section 38DC applies to the provision | 3 |
| s 38DC(2) | The maximum fine is taken only to be the maximum fine for an individua... | 588 | encoded | nt-part4a-penalties.l4: s 38DC(2): the maximum fine for an individual that may be imposed under the subordinate legislation | 2 |
| s 38DC(3) | The maximum fine for a body corporate that may be imposed under the su... | 589 | encoded | nt-part4a-penalties.l4: s 38DC(3): the maximum fine for a body corporate that may be imposed under the subordinate legislation | 3 |
| s 38F | Penalties for breach of subordinate legislation | 590 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 38F(1) | Subordinate legislation may prescribe a fine for an offence against th... | 591 | encoded | nt-part4a-penalties.l4: s 38F(1): the subordinate legislation may prescribe a fine for the offence | 2 |
| s 38F(2) | The fine prescribed must not exceed 100 penalty units. | 592 | encoded | nt-part4a-penalties.l4: s 38F(2): the fine prescribed is within the limit | 4 |
| s 38F(2) Note for subsection (2) | Note for subsection (2) | 593-594 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 38F(3) | This section has effect subject to the Act under which the legislation... | 595 | encoded | nt-part4a-penalties.l4: s 38F(2): the fine prescribed is within the limit | 4 |
| s 38G | Civil penalties | 596-597 | encoded | nt-part4a-penalties.l4: s 38G: the civil penalty is within the penalty specified or prescribed | 3 |
| Part V | Powers, functions and authorities | 598 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 39 | Confirmation of appointments not required | 599-600 | encoded | nt-part5-powers.l4: s 39: the appointment or exercise of the power ceases to have effect or needs to be confirmed | 2 |
| s 40 | Continuing to act during vacancy in office | 601 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 40(1) | If a person is acting in an office (including a Ministerial office) du... | 602 | fork F13 | nt-part5-powers.l4: s 40(1): the last day on which the person acting may continue to act | 5 |
| s 40(1)(a) | the lawful revocation of the person's authority to act; | 603 | encoded | nt-part5-powers.l4: s 40(1): the last day on which the person acting may continue to act | 5 |
| s 40(1)(b) | 1 year after the office-holder ceased to hold office. | 604 | fork F13 | nt-part5-powers.l4: s 40(1): the last day on which the person acting may continue to act | 5 |
| s 40(2) | In this section: | 605 | inert | reason 1: not operative. "(2) In this section:" only introduces the definitions that follow, each its own row. |  |
| s 40 "acting in an office" | acting in an office | 606 | encoded | nt-part5-powers.l4 (1 rule) | 2 |
| s 40 "office" | office | 607 | encoded | nt-part5-powers.l4 (1 rule) | 2 |
| s 41 | Occasions for exercise of powers etc. | 608 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 41(1) | Where an Act confers a power or imposes a duty, the power may be exerc... | 609 | encoded | nt-part5-powers.l4: s 41(1): the power may be exercised and the duty performed on the occasion | 2 |
| s 41(2) | Where an Act confers a power or imposes a duty on the holder of an off... | 610 | encoded | nt-part5-powers.l4: s 41(2): the person may exercise the power and must perform the duty | 3 |
| s 42 | How power may be exercised | 611 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 42(1) | A power under an Act to make, grant or issue a statutory instrument ma... | 612 | encoded | nt-part5-powers.l4: s 42(1): the power to make, grant or issue a statutory instrument may be exercised in that manner | 5 |
| s 42(1)(a) | in whole or in part; | 613 | encoded | nt-part5-powers.l4: s 42(1): the power to make, grant or issue a statutory instrument may be exercised in that manner | 5 |
| s 42(1)(b) | so that it is subject to any conditions, limitations or qualifications... | 614 | encoded | nt-part5-powers.l4: s 42(1): the power to make, grant or issue a statutory instrument may be exercised in that manner | 5 |
| s 42(1)(c) | to make different provision in relation to different matters or classe... | 615 | encoded | nt-part5-powers.l4: s 42(1): the power to make, grant or issue a statutory instrument may be exercised in that manner | 5 |
| s 42(1)(d) | to apply differently by reference to exceptions or factors specified i... | 616 | encoded | nt-part5-powers.l4: s 42(1): the power to make, grant or issue a statutory instrument may be exercised in that manner | 5 |
| s 42(2) | The power is not limited to making provision in relation to a particul... | 617 | encoded | nt-part5-powers.l4: s 42(2): the power is limited to a particular matter or aspect of a matter | 2 |
| s 42(4) | This section applies in relation to a power whether exercised before o... | 618 | encoded | nt-part5-powers.l4: s 42(4): section 42 applies in relation to the power | 2 |
| s 43 | Power to take action or make statutory instrument includes power to revoke, amend etc. | 619-620 | encoded | nt-part5-powers.l4: s 43: the power includes the power to do the thing to the action or instrument, in the same manner and subject to the same conditions | 6 |
| s 44 | Power to appoint includes power to remove | 621 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 44(1) | Subject to subsection (3), where an Act confers on any person or autho... | 622 | encoded | nt-part5-powers.l4: s 44(1): the power to make appointments includes the power to do the thing to the person appointed | 4 |
| s 44(3) | Where a power to make appointments to an office or position is exercis... | 623 | encoded | nt-part5-powers.l4: s 44(3): the power of termination or removal may be exercised | 3 |
| s 44A | Acting appointment | 624-625 | encoded | nt-part5-powers.l4: s 44A: the appointer may appoint a person, or 2 or more people, to act | 4 |
| s 44A(a) | during a vacancy, or all vacancies, in the office or position whether ... | 626 | encoded | nt-part5-powers.l4: s 44A: the appointer may appoint a person, or 2 or more people, to act | 4 |
| s 44A(b) | during any period, or all periods, when the holder of the office or po... | 627 | encoded | nt-part5-powers.l4: s 44A: the appointer may appoint a person, or 2 or more people, to act | 4 |
| s 46 | Power to authorise another person to exercise power or perform function | 628 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 46(1) | If an Act or a statutory instrument confers a function or power on a m... | 629 | encoded | nt-part5-powers.l4: s 46(1), (2): the person may perform the function or exercise the power by authority | 8 |
| s 46(1)(a) | for a minister – by a person who has the authority of the minister; or | 630 | encoded | nt-part5-powers.l4: s 46(1), (2): the person may perform the function or exercise the power by authority | 8 |
| s 46(1)(b) | otherwise – by a person who, with the approval of the minister adminis... | 631 | encoded | nt-part5-powers.l4: s 46(1), (2): the person may perform the function or exercise the power by authority | 8 |
| s 46(1) Note for subsection (1) | Note for subsection (1) | 632-633 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 46(2) | Subsection (1) does not empower the exercise of a power or the perform... | 634 | encoded | nt-part5-powers.l4: s 46(1), (2): the person may perform the function or exercise the power by authority | 8 |
| s 46(3) | Authority may be conferred pursuant to subsection (1) on: | 635 | encoded | nt-part5-powers.l4: s 46(3): authority may be conferred on a person in that way | 4 |
| s 46(3)(a) | a person by name; | 636 | encoded | nt-part5-powers.l4: s 46(3): authority may be conferred on a person in that way | 4 |
| s 46(3)(b) | a person by reference to the office, position or designation held or o... | 637 | encoded | nt-part5-powers.l4: s 46(3): authority may be conferred on a person in that way | 4 |
| s 46(3)(c) | a person from time to time holding, acting in or performing the duties... | 638 | encoded | nt-part5-powers.l4: s 46(3): authority may be conferred on a person in that way | 4 |
| s 46(5) | The conferring of authority by an instrument under this section does n... | 639 | encoded | nt-part5-powers.l4: s 46(5): the conferring of authority prevents the person from exercising the power | 3 |
| s 46(6) | The performance of a function or exercise of a power by the authority ... | 640 | encoded | nt-part5-powers.l4: s 46(6): the performance or exercise is within the authority conferred | 3 |
| s 46(7) | This section does not apply to: | 641 | encoded | nt-part5-powers.l4: s 46(7): section 46 applies to the function or power | 4 |
| s 46(7)(a) | a function or power of a legislative or judicial nature; or | 642 | encoded | nt-part5-powers.l4: s 46(7): section 46 applies to the function or power | 4 |
| s 46(7)(b) | a function or power relating to: | 643-645 | encoded | nt-part5-powers.l4: s 46(7): section 46 applies to the function or power | 4 |
| s 46A | Power of delegation | 646 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 46A(1) | A provision of an Act that confers a power to delegate a power or func... | 647 | encoded | nt-part5-powers.l4: s 46A(1): the power to delegate may be exercised by delegating to a person in that way | 3 |
| s 46A(1)(a) | a person by name; | 648 | encoded | nt-part5-powers.l4: s 46A(1): the power to delegate may be exercised by delegating to a person in that way | 3 |
| s 46A(1)(b) | a person by reference to the office, position or designation held or o... | 649 | encoded | nt-part5-powers.l4: s 46A(1): the power to delegate may be exercised by delegating to a person in that way | 3 |
| s 46A(1)(c) | a person from time to time holding, acting in or performing the duties... | 650 | encoded | nt-part5-powers.l4: s 46A(1): the power to delegate may be exercised by delegating to a person in that way | 3 |
| s 46A(2) | A provision of an Act that confers a power to delegate a power or func... | 651 | encoded | nt-part5-powers.l4: s 46A(2): the power to delegate includes the power to delegate that power of delegation | 2 |
| s 46A(3) | If a power or function is delegated under an Act, the power or functio... | 652 | encoded | nt-part5-powers.l4: s 46A(3): the person by whom the power or function is taken to be exercised or performed | 2 |
| s 46A(4) | The delegation of the power or function under an Act does not prevent ... | 653 | encoded | nt-part5-powers.l4: s 46A(4): the delegation prevents the person who delegated from exercising the power or performing the function | 2 |
| s 48 | Discretions | 654-655 | encoded | nt-part5-powers.l4: s 48: the power may be exercised upon the opinion, belief or state of mind of the delegate or authorised person | 3 |
| s 48A | Participation in meetings by telephone etc. | 656 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 48A(1) | This section applies to a body (whether or not incorporated) establish... | 657 | encoded | nt-part5-powers.l4: s 48A(1): section 48A applies to the body | 3 |
| s 48A(2) | The body may permit its members to participate in a meeting or all mee... | 658 | encoded | nt-part5-powers.l4: s 48A(2): the body may permit its members to participate in a meeting by any means of communication | 2 |
| s 48A(2)(a) | telephone; or | 659 | encoded | nt-part5-powers.l4: s 48A(2): the body may permit its members to participate in a meeting by any means of communication | 2 |
| s 48A(2)(b) | exchange of emails; or | 660 | encoded | nt-part5-powers.l4: s 48A(2): the body may permit its members to participate in a meeting by any means of communication | 2 |
| s 48A(2)(c) | online facilities; or | 661 | encoded | nt-part5-powers.l4: s 48A(2): the body may permit its members to participate in a meeting by any means of communication | 2 |
| s 48A(2)(d) | any other means of communication. | 662 | encoded | nt-part5-powers.l4: s 48A(2): the body may permit its members to participate in a meeting by any means of communication | 2 |
| s 48A(3) | A member who participates in a meeting under a permission under subsec... | 663 | encoded | nt-part5-powers.l4: s 48A(3): the member is taken to be present at the meeting | 3 |
| s 48B | Power to correct minor errors | 664 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 48B(1) | Where a decision made in proceedings before a person or body authorise... | 665, 670 | encoded | nt-part5-powers.l4: s 48B(1): the decision maker may correct the decision | 7 |
| s 48B(1)(a) | a clerical mistake; | 666 | encoded | nt-part5-powers.l4: s 48B(1): the decision maker may correct the decision | 7 |
| s 48B(1)(b) | an error arising from an accidental slip or omission; | 667 | encoded | nt-part5-powers.l4: s 48B(1): the decision maker may correct the decision | 7 |
| s 48B(1)(c) | a material miscalculation of figures or a material mistake in the desc... | 668 | encoded | nt-part5-powers.l4: s 48B(1): the decision maker may correct the decision | 7 |
| s 48B(1)(d) | a defect of form, | 669 | encoded | nt-part5-powers.l4: s 48B(1): the decision maker may correct the decision | 7 |
| s 48B(2) | In this section decision includes a judgment, order and determination,... | 671 | encoded | nt-part5-powers.l4: s 48B(2): the thing is a decision | 5 |
| Part VI | Mechanics of legislation | 672 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 49 | Citation | 673 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 49(1) | An Act may be cited in any of the following ways: | 674 | encoded | nt-part6-mechanics.l4: s 49(1): the Act may be cited in that way | 3 |
| s 49(1)(a) | by its short title including the year of enactment; | 675 | encoded | nt-part6-mechanics.l4: s 49(1): the Act may be cited in that way | 3 |
| s 49(1)(b) | by reference to its number and the calendar year in which it received ... | 676 | encoded | nt-part6-mechanics.l4: s 49(1): the Act may be cited in that way | 3 |
| s 49(2) | A provision of an Act may be cited by reference to the part, section, ... | 677 | encoded | nt-part6-mechanics.l4: s 49(2): the provision may be cited by reference to the division | 5 |
| s 49(3) | A reference mentioned in subsection (2) must be made according to the ... | 678 | encoded | nt-part6-mechanics.l4: s 49(3): the reference meets the requirement of subsection (3) | 2 |
| s 50 | References to other legislation | 679 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 50(1) | A reference in an Act to other legislation is a reference to the other... | 680 | encoded | nt-part6-mechanics.l4: s 50(1): the version of the other legislation that a reference to it is a reference to on the day | 6 |
| s 50(2) | If a provision of an Act amends another Act, a reference in the provis... | 681 | encoded | nt-part6-mechanics.l4: s 50(2): the version of the other Act that the reference in the amending provision is a reference to | 3 |
| s 51 | Reference to Act includes reference to statutory instruments under Act | 682 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 51(1) | In an Act, a reference (either generally or specifically) to a law or ... | 683 | encoded | nt-part6-mechanics.l4: s 51(1): the reference includes the statutory instrument | 2 |
| s 51(2) | In this section: | 684 | inert | reason 1: not operative. "(2) In this section:" only introduces the definitions that follow, each its own row. |  |
| s 51 "law" | law | 685 | encoded | nt-part6-mechanics.l4 (1 rule) | 4 |
| s 52 | References to Imperial, Commonwealth and State Acts | 686-687 | encoded | nt-part6-mechanics.l4 (2 rules) | 9 |
| s 53 | References in an Act to provisions of that Act | 688 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 53(1) | A reference in an Act to a Part, section or Schedule shall be read as ... | 689 | encoded | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part; s 53(3), (4), (5): the identifier of the unit named | 19 |
| s 53(2) | A reference in a Part of an Act to a Division shall be read as a refer... | 690 | encoded | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part; s 53(3), (4), (5): the identifier of the unit named | 19 |
| s 53(3) | A reference in a section of an Act to a subsection or paragraph shall ... | 691 | fork F12 | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part; s 53(3), (4), (5): the identifier of the unit named | 19 |
| s 53(4) | A reference in a subsection of a section of an Act to a paragraph shal... | 692 | fork F12 | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part; s 53(3), (4), (5): the identifier of the unit named | 19 |
| s 53(5) | A reference in a paragraph of a section, or of a subsection of a secti... | 693 | encoded | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part; s 53(3), (4), (5): the identifier of the unit named | 19 |
| s 53(6) | A reference in a Schedule, or part of a Schedule, to an Act to a form,... | 694 | encoded | nt-part6-mechanics.l4: s 53(1) to (6): the thing of which the unit that the reference names is a part | 13 |
| s 53(7) | A reference to a form in an Act the Schedule to which or only one of t... | 695 | encoded | nt-part6-mechanics.l4: s 53(7): the reference to a form is read as a reference to a form in that Schedule | 2 |
| s 54 | Every section a substantive enactment | 696-697 | encoded | nt-part6-mechanics.l4: s 54: the section has effect as a substantive enactment | 2 |
| s 55 | Material that is, and is not, part of an Act | 698 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 55(1) | A heading to a Chapter, Part, Division or Subdivision of an Act is par... | 699 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(2) | A heading to a section of an Act is part of the Act if: | 700 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(2)(a) | the Act is enacted after 1 July 2006; or | 701 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(2)(b) | the heading is amended or inserted after 1 July 2006. | 702 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(3) | Subsection (2) does not prevent the amendment of a heading to a sectio... | 703 | encoded | nt-part6-mechanics.l4: s 55(3): subsection (2) prevents the amendment of the heading by an Act; s 55: the material is part of the Act | 12 |
| s 55(4) | An example or note in the text of an Act is part of the provision of t... | 704 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(5) | A Schedule to an Act is part of the Act. | 705 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 55(6) | A marginal note, footnote, endnote or any other note that is not part ... | 706 | encoded | nt-part6-mechanics.l4: s 55: the material is part of the Act | 10 |
| s 56 | Numbering of Acts | 707 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 56(1) | The Acts which receive assent in each calendar year shall be numbered ... | 708 | fork F17 | nt-part6-mechanics.l4: s 56(1): the number of the Act | 5 |
| s 56(2) | For the purposes of subsection (1), an Act which receives the Governor... | 709 | encoded | nt-part6-mechanics.l4: s 56(2): the day on which the Act is deemed to receive assent | 2 |
| s 57 | Numbering of subordinate legislation | 710 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 57(1) | This section applies to subordinate legislation other than: | 711 | encoded | nt-part6-mechanics.l4: s 57(1): section 57 applies to the subordinate legislation | 4 |
| s 57(1)(a) | rules of court that relate only to dates of sittings of a court; or | 712 | encoded | nt-part6-mechanics.l4: s 57(1): section 57 applies to the subordinate legislation | 4 |
| s 57(1)(b) | by-laws made by the Commissioner for Public Employment under the Publi... | 713 | encoded | nt-part6-mechanics.l4: s 57(1): section 57 applies to the subordinate legislation | 4 |
| s 57(1)(c) | subordinate legislation that expressly provides this section does not ... | 714 | encoded | nt-part6-mechanics.l4: s 57(1): section 57 applies to the subordinate legislation | 4 |
| s 57(2) | Subordinate legislation made in each calendar year must be numbered in... | 715 | fork F17 | nt-part6-mechanics.l4: s 57(2): the number of the subordinate legislation | 3 |
| s 57(3) | Subordinate legislation may, without prejudice to any other method of ... | 716 | encoded | nt-part6-mechanics.l4: s 57(3): the subordinate legislation may be cited by its number and the calendar year in which it is made | 2 |
| s 57A | Amendment of instruments by Act | 717 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 57A(1) | If a statutory instrument under an Act (the parent Act) has been amend... | 718 | encoded | nt-part6-mechanics.l4: s 57A(1): the statutory instrument may be amended, varied, repealed, rescinded or revoked by a statutory instrument under the parent Act | 2 |
| s 57A(2) | Subsection (1) applies in relation to amendments effected before or af... | 719 | encoded | nt-part6-mechanics.l4: s 57A(2): subsection (1) applies in relation to the amendment | 2 |
| s 57B | Definitions automatically inserted in alphabetical order | 720-721 | fork F16 | nt-part6-mechanics.l4: s 57B: the terms in the order they stand after the insertion | 8 |
| Part VII | General | 722 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Part VII, Division 1 | Construction | 723 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 58 | Amending act to be construed with amended Act | 724-725 | encoded | nt-part7-construction.l4: s 58: the amending Act is construed with the other Act or law and as part of it | 2 |
| s 59 | Act to be construed subject to power | 726-727 | encoded | nt-part7-construction.l4: s 59: the part of the Act stands | 3 |
| s 59A | Public places etc. on Aboriginal land | 728 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 59A(1) | Where by or under a law of the Territory a right, privilege, obligatio... | 729 | encoded | nt-part7-construction.l4: s 59A(1): the reference includes the place | 5 |
| s 59A(2) | For the purposes of a law of the Territory referred to in subsection (... | 730 | encoded | nt-part7-construction.l4: s 59A(2): the persons are capable of constituting a section of the public in relation to the land | 3 |
| s 61 | Construction of statutory instruments | 731 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 61(1) | If an Act confers upon any authority power to make, grant or issue a s... | 732 | encoded | nt-part7-construction.l4: s 61(1): the part of the instrument stands | 3 |
| s 61(2) | It is presumed, unless the contrary is proved, that all conditions and... | 733 | encoded | nt-part7-construction.l4: s 61(2): the conditions and steps required for the making of the instrument are presumed to have been satisfied and carried out | 2 |
| s 62 | Construction of resolutions of Legislative Assembly | 734-735 | encoded | nt-part7-construction.l4: s 62: the part of the resolution stands | 3 |
| s 62A | Regard to be had to purpose or object of Act | 736-737 | encoded | nt-part7-construction.l4: s 62A: the first construction is to be preferred to the second | 4 |
| s 62B | Use of extrinsic material in interpreting Act | 738 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 62B(1) | In interpreting a provision of an Act, if material not forming part of... | 739 | encoded | nt-part7-construction.l4: s 62B(1): the material may be considered | 6 |
| s 62B(1)(a) | to confirm that the meaning of the provision is the ordinary meaning c... | 740 | encoded | nt-part7-construction.l4: s 62B(1): the material may be considered | 6 |
| s 62B(1)(b) | to determine the meaning of the provision when: | 741-743 | encoded | nt-part7-construction.l4: s 62B(1): the material may be considered | 6 |
| s 62B(2) | Without limiting subsection (1), the material that may be considered i... | 744 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(a) | all matters not forming part of the Act that are set out in the docume... | 745 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(b) | any relevant report of a Royal Commission, Law Reform Commission, comm... | 746 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(c) | any relevant report of a committee of the Legislative Assembly that wa... | 747 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(d) | any treaty or other international agreement that is referred to in the... | 748 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(e) | any explanatory memorandum relating to the Bill containing the provisi... | 749 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(f) | any explanatory speech or statement given by a Minister or other Membe... | 750 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(g) | any document (whether or not a document to which a preceding paragraph... | 751 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62B(2)(h) | any relevant material in any official record of debates in the Legisla... | 752 | encoded | nt-part7-construction.l4: s 62B(2): the material is within the material that may be considered | 12 |
| s 62C | Changes in drafting practice do not affect meaning | 753 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 62C(1) | Subsection (2) applies if: | 754 | encoded | nt-part7-construction.l4: s 62C: the ideas are taken to be different | 4 |
| s 62C(1)(a) | a provision of an Act expresses an idea in particular words; and | 755 | encoded | nt-part7-construction.l4: s 62C: the ideas are taken to be different | 4 |
| s 62C(1)(b) | a provision of the Act enacted later appears to express the same idea ... | 756 | encoded | nt-part7-construction.l4: s 62C: the ideas are taken to be different | 4 |
| s 62C(2) | The ideas must not be taken to be different merely because different w... | 757 | encoded | nt-part7-construction.l4: s 62C: the ideas are taken to be different | 4 |
| s 62D | Examples | 758-759 | encoded | nt-part7-construction.l4 (3 rules) | 7 |
| s 62D(a) | the example is not exhaustive; | 760 | encoded | nt-part7-construction.l4 (3 rules) | 7 |
| s 62D(b) | the example does not limit or extend the meaning of the provision; and | 761 | encoded | nt-part7-construction.l4 (2 rules) | 5 |
| s 62D(c) | if the example is inconsistent with the provision, the provision preva... | 762 | encoded | nt-part7-construction.l4: s 62D(c): the provision prevails over the example to the extent of the inconsistency | 3 |
| s 62E | Notes | 763 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 62E(1) | A note at the foot of a provision: | 764 | encoded | nt-part7-construction.l4: s 62E(1): the note is exhaustive or limits or extends the meaning of the provision | 2 |
| s 62E(1)(a) | is not exhaustive; and | 765 | encoded | nt-part7-construction.l4: s 62E(1): the note is exhaustive or limits or extends the meaning of the provision | 2 |
| s 62E(1)(b) | does not limit or extend the meaning of the provision. | 766 | encoded | nt-part7-construction.l4: s 62E(1): the note is exhaustive or limits or extends the meaning of the provision | 2 |
| s 62E(2) | If a note at the foot of a provision is inconsistent with the provisio... | 767 | encoded | nt-part7-construction.l4: s 62E(2): the provision prevails over the note to the extent of the inconsistency | 3 |
| Part VII, Division 2 | Statutory instruments | 768 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 63 | Procedure for making regulations | 769-770 | encoded | nt-part7-instruments.l4: s 63(a): the regulation has been published and notified as required | 4 |
| s 63(a) | as soon as practicable after it is made: | 771-773 | encoded | nt-part7-instruments.l4: s 63(a): the regulation has been published and notified as required | 4 |
| s 63(b) | within 6 sitting days after it is made, be tabled in the Legislative A... | 774 | fork F18 | nt-part7-instruments.l4: s 63(b): the last day on which the regulation must be tabled; s 63(b): the regulation is tabled within 6 sitting days after it is made | 8 |
| s 63A | Procedure for making rules or by-laws | 775 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 63A(1) | If an Act contains a power to make rules or by-laws, a rule or by‑law ... | 776 | encoded | nt-part7-instruments.l4: s 63A(1)(a): the rule or by-law is signed as required | 4 |
| s 63A(1)(a) | signed by: | 777-779 | encoded | nt-part7-instruments.l4: s 63A(1)(a): the rule or by-law is signed as required | 4 |
| s 63A(1)(b) | once signed, given to the minister administering the provision contain... | 780 | encoded | nt-part7-instruments.l4: s 63A(1)(b): the signed rule or by-law must be given to the minister administering the provision containing the power | 2 |
| s 63A(2) | Subject to this section, if a signed rule or by-law is given to a mini... | 781 | encoded | nt-part7-instruments.l4: s 63A(2)(a): the minister has caused the rule or by-law to be published and notified as required | 5 |
| s 63A(2)(a) | as soon as practicable after it is made, cause it to be: | 782-784 | encoded | nt-part7-instruments.l4: s 63A(2)(a): the minister has caused the rule or by-law to be published and notified as required | 5 |
| s 63A(2)(b) | within 6 sitting days after it is notified in the Gazette, cause it to... | 785 | fork F18 | nt-part7-instruments.l4 (2 rules) | 6 |
| s 63A(3) | If a rule or by-law is given to a minister under subsection (1)(b), th... | 786 | encoded | nt-part7-instruments.l4: s 63A(3): the minister may return the rule or by-law with a request for amendment | 3 |
| s 63A(4) | If a minister returns a rule or by-law under subsection (3), the perso... | 787 | encoded | nt-part7-instruments.l4: s 63A(4): the person making the rule or by-law has done what the subsection requires | 4 |
| s 63A(4)(a) | consider the amendment; and | 788 | encoded | nt-part7-instruments.l4: s 63A(4): the person making the rule or by-law has done what the subsection requires | 4 |
| s 63A(4)(b) | give the rule or by-law, signed in accordance with subsection (1)(a), ... | 789 | encoded | nt-part7-instruments.l4: s 63A(4): the person making the rule or by-law has done what the subsection requires | 4 |
| s 63A(5) | Subsection (2) applies to a rule or by-law given to the minister under... | 790 | encoded | nt-part7-instruments.l4: s 63A(5): subsection (2) applies to the rule or by-law | 2 |
| s 63A(6) | Subsection (1)(b) does not apply to a by-law made under the Unit Title... | 791 | encoded | nt-part7-instruments.l4: s 63A(6): subsection (1)(b) applies to the by-law | 2 |
| s 63B | Commencement of subordinate legislation | 792 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 63B(1) | Subordinate legislation commences on the day specified or provided for... | 793 | encoded | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63B(2) | Subordinate legislation may be specified to commence: | 794 | fork F8 | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63B(2)(a) | subject to subsection (3), on a particular day or on a number of diffe... | 795 | fork F8 | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63B(2)(b) | on the happening of a particular event or events. | 796 | fork F8 | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63B(2) Examples for subsection (2)(b) | Examples for subsection (2)(b) | 797-799 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 63B(3) | Subordinate legislation must not be specified to commence or to take e... | 800 | encoded | nt-interpretation-time.l4: s 63B(3), (4): the provision of subordinate legislation is of no effect; s 63B: the day on which subordinate legislation commences | 14 |
| s 63B(4) | A provision of subordinate legislation made in contravention of subsec... | 801 | encoded | nt-interpretation-time.l4: s 63B(3), (4): the provision of subordinate legislation is of no effect; s 63B: the day on which subordinate legislation commences | 14 |
| s 63B(5) | If subordinate legislation does not specify or provide for its commenc... | 802 | encoded | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63B(6) | Despite subsection (5), a rule or by-law that does not specify or prov... | 803 | encoded | nt-interpretation-time.l4: s 63B: the day on which subordinate legislation commences | 10 |
| s 63C | Tabling and disallowance requirements | 804 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 63C(1) | A failure to table subordinate legislation in the Legislative Assembly... | 805 | encoded | nt-part7-instruments.l4: s 63C(1): the failure to table affects whether the subordinate legislation has effect | 2 |
| s 63C(2) | The Legislative Assembly may pass a resolution disallowing subordinate... | 806 | encoded | nt-part7-instruments.l4: s 63C(2): the Legislative Assembly may pass a resolution disallowing the subordinate legislation or specified provisions of it | 3 |
| s 63C(3) | Notice of a resolution referred to in subsection (2) must be given wit... | 807 | fork F18 | nt-part7-instruments.l4: s 63C(3): the last day on which notice of the resolution must be given | 3 |
| s 63C(3)(a) | in the case of subordinate legislation that is tabled in accordance wi... | 808 | fork F18 | nt-part7-instruments.l4: s 63C(3): the last day on which notice of the resolution must be given | 3 |
| s 63C(3)(b) | in the case of subordinate legislation that has not been tabled in acc... | 809 | fork F18 | nt-part7-instruments.l4: s 63C(3): the last day on which notice of the resolution must be given | 3 |
| s 63C(4) | Subject to subsection (5), disallowance under this section has the sam... | 810 | encoded | nt-part7-instruments.l4: s 63C(4): the disallowance has the same effect as a repeal | 2 |
| s 63C(5) | If a provision of disallowed subordinate legislation (the disallowed p... | 811 | encoded | nt-part7-instruments.l4: s 63C(5): the date from which the disallowance revives the other provision | 2 |
| s 64 | Subordinate legislation not to be made in terms of disallowed subordinate legislation | 812 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 64(1) | This section applies if, under section 63C, the Legislative Assembly p... | 813 | encoded | nt-part7-instruments.l4: s 64(2): the last day of the 6 months after the disallowance; s 64(2): the subordinate legislation may be made on the day | 7 |
| s 64(2) | Subordinate legislation or provisions of subordinate legislation that ... | 814 | fork F18 | nt-part7-instruments.l4: s 64(2): the last day of the 6 months after the disallowance; s 64(2): the subordinate legislation may be made on the day | 7 |
| s 64(3) | Subordinate legislation or provisions of subordinate legislation made ... | 815 | encoded | nt-part7-instruments.l4: s 64(3): the subordinate legislation is of no effect | 2 |
| s 65 | Power to make subordinate legislation | 816 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 65(1) | If an Act authorises or requires the making of subordinate legislation... | 817 | encoded | nt-part7-instruments.l4: s 65(1): the power enables subordinate legislation to be made with respect to the matter | 3 |
| s 65(1)(a) | is required or permitted to be prescribed by the Act; or | 818 | encoded | nt-part7-instruments.l4: s 65(1): the power enables subordinate legislation to be made with respect to the matter | 3 |
| s 65(1)(b) | is necessary or convenient to be prescribed for carrying out or giving... | 819 | encoded | nt-part7-instruments.l4: s 65(1): the power enables subordinate legislation to be made with respect to the matter | 3 |
| s 65(2) | Subsection (1) applies even though the Act also authorises the making ... | 820 | encoded | nt-part7-instruments.l4: s 65(2): subsection (1) applies | 2 |
| s 65(3) | Power conferred by the Act to make subordinate legislation for a parti... | 821 | encoded | nt-part7-instruments.l4: s 65(3): the power for a particular purpose limits the effect of the general power | 2 |
| s 65A | Subordinate legislation may prohibit | 822-823 | encoded | nt-part7-instruments.l4: s 65A: the power may be exercised by prohibiting the matter or an aspect of it | 2 |
| s 65B | Subordinate legislation may provide for review or appeal | 824 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 65B(1) | Subordinate legislation may provide for the review of, or a right of a... | 825 | encoded | nt-part7-instruments.l4: s 65B(1): the subordinate legislation may provide for review of, or a right of appeal against, the decision | 2 |
| s 65B(2) | For subsection (1), the subordinate legislation may confer jurisdictio... | 826 | encoded | nt-part7-instruments.l4: s 65B(2): the subordinate legislation may confer jurisdiction on the holder | 5 |
| s 65C | Subordinate legislation may provide for exemption, waiver or refund of fees | 827-828 | encoded | nt-part7-instruments.l4: s 65C: the power to prescribe a fee includes power to provide for the thing | 4 |
| s 65C(a) | the exemption from payment of the fee; | 829 | encoded | nt-part7-instruments.l4: s 65C: the power to prescribe a fee includes power to provide for the thing | 4 |
| s 65C(b) | the waiver (wholly or partly) of the fee; | 830 | encoded | nt-part7-instruments.l4: s 65C: the power to prescribe a fee includes power to provide for the thing | 4 |
| s 65C(c) | the refund (wholly or partly) of the fee. | 831 | encoded | nt-part7-instruments.l4: s 65C: the power to prescribe a fee includes power to provide for the thing | 4 |
| s 65D | Subordinate legislation may provide for infringement notice offences | 832-833 | encoded | nt-part7-instruments.l4: s 65D: the power enables subordinate legislation providing for the thing | 4 |
| s 65D(a) | the payment of a prescribed amount instead of a penalty that may other... | 834 | encoded | nt-part7-instruments.l4: s 65D: the power enables subordinate legislation providing for the thing | 4 |
| s 65D(b) | the service of a notice relating to payment of the amount on a person ... | 835 | encoded | nt-part7-instruments.l4: s 65D: the power enables subordinate legislation providing for the thing | 4 |
| s 65D(c) | the particulars to be included in the notice. | 836 | encoded | nt-part7-instruments.l4: s 65D: the power enables subordinate legislation providing for the thing | 4 |
| s 65E | Statutory instrument may require making of statutory declaration | 837 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 65E(1) | If an Act gives power to make, grant or issue a statutory instrument, ... | 838 | encoded | nt-part7-instruments.l4: s 65E(1): the statutory instrument may require the making of a statutory declaration | 2 |
| s 65E(2) | Subsection (1) applies: | 839 | encoded | nt-part7-instruments.l4: s 65E(2): subsection (1) applies | 3 |
| s 65E(2)(a) | whether or not the Act authorises or requires penalties to be prescrib... | 840 | encoded | nt-part7-instruments.l4: s 65E(2): subsection (1) applies | 3 |
| s 65E(2)(b) | if the Act authorises or requires penalties to be prescribed by instru... | 841 | encoded | nt-part7-instruments.l4: s 65E(2): subsection (1) applies | 3 |
| s 65F | Simultaneous actions | 842 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 65F(1) | If the effect of a statutory instrument is to substitute an action (ac... | 843 | encoded | nt-part7-instruments.l4: s 65F(1): action A is taken to have occurred after the revocation of action B | 2 |
| s 65F(2) | If a series of actions has effect simultaneously, the actions are take... | 844 | encoded | nt-part7-instruments.l4: s 65F(2): the sequence in which the actions are taken to have effect | 2 |
| s 65F Example for section 65F | Example for section 65F | 845-846 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| s 66 | Prescribing matters by reference to other instruments | 847-848, 851 | encoded | nt-part7-instruments.l4: s 66: the statutory instrument may apply, adopt or incorporate the matter | 5 |
| s 66(a) | the provisions of any Territory or Commonwealth Act, or of a statutory... | 849 | encoded | nt-part7-instruments.l4: s 66: the statutory instrument may apply, adopt or incorporate the matter | 5 |
| s 66(b) | any matter contained in any other instrument or writing as in force or... | 850 | encoded | nt-part7-instruments.l4: s 66: the statutory instrument may apply, adopt or incorporate the matter | 5 |
| Part VII, Division 3 | General | 852 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 66A | Gazette publication requirements | 853 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 66A(1) | If an Act requires a statutory instrument to be published in the Gazet... | 854 | fork F15 | nt-part7-general.l4: s 66A(1): the requirement that the instrument be published in the Gazette is satisfied | 3 |
| s 66A(1)(a) | the instrument is notified in the Gazette; and | 855 | encoded | nt-part7-general.l4: s 66A(1): the requirement that the instrument be published in the Gazette is satisfied | 3 |
| s 66A(1)(b) | the notification under paragraph (a) states the place where copies of ... | 856 | encoded | nt-part7-general.l4: s 66A(1): the requirement that the instrument be published in the Gazette is satisfied | 3 |
| s 66A(2) | The place under subsection (1)(b) may be a website or another publicly... | 857 | encoded | nt-part7-general.l4: s 66A(2): the place may be the kind of place | 4 |
| s 67 | Tabling documents in Legislative Assembly | 858 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 67(1) | A document is tabled in the Legislative Assembly under an Act if the d... | 859 | encoded | nt-part7-general.l4: s 67(1): the document is tabled in the Legislative Assembly under the Act | 5 |
| s 67(1)(a) | tabled in the Assembly under the Standing Orders of the Assembly; or | 860 | encoded | nt-part7-general.l4: s 67(1): the document is tabled in the Legislative Assembly under the Act | 5 |
| s 67(1)(b) | delivered to the Clerk of the Assembly and recorded in the Minutes of ... | 861 | encoded | nt-part7-general.l4: s 67(1): the document is tabled in the Legislative Assembly under the Act | 5 |
| s 67(2) | The document must be tabled under subsection (1) within the period spe... | 862 | encoded | nt-part7-general.l4: s 67(2): the document is tabled within the period specified in the Act | 4 |
| s 67(3) | If the Act provides for a specified person to table the document, the ... | 863 | encoded | nt-part7-general.l4: s 67(3): the document may be tabled by the person | 3 |
| s 67(4) | In this section: | 864 | inert | reason 1: not operative. "(4) In this section:" only introduces the definitions that follow, each its own row. |  |
| s 67 "Act" | Act | 865 | encoded | nt-part7-general.l4 (1 rule) | 2 |
| s 67 "document" | document | 866 | encoded | nt-part7-general.l4 (1 rule) | 2 |
| s 68 | Compliance with forms | 867-868 | fork F15 | nt-part7-general.l4: s 68: strict compliance with the form is necessary; s 68: the compliance with the form is sufficient | 6 |
| s 69 | Civil proceedings | 869-870 | encoded | nt-part7-general.l4: s 69: the money is recoverable in the court or tribunal | 5 |
| s 70 | Powers of persons authorised to adjudicate | 871-872 | encoded | nt-part7-general.l4: s 70: the person or body has authority to receive evidence and examine on oath any witness appearing before it | 2 |
| s 71 | Amendment in same session | 873-874 | encoded | nt-part7-general.l4: s 71: the Act may be amended or repealed | 2 |
| s 72 | Sunday observance | 875 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 72(1) | It is hereby declared that all laws and statutes of England, to the ex... | 876 | encoded | nt-part7-general.l4: s 72(1): the law or statute of England has force or effect in the Territory to that extent | 3 |
| s 72(2) | Except as provided by or under a law of the Territory or of the Common... | 877 | encoded | nt-part7-general.l4: s 72(2): it is lawful to do the act on that day | 4 |
| Part VIIA | Incorporation of amendments | 878 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 72A | Meaning of reprint | 879-880 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). The introduction "In this Part:" only introduces the definitions that follow, each its own row. The heading is carried as data in nt-provisions.l4. |  |
| s 72A "legislation" | legislation | 881 | encoded | nt-part7a-reprints.l4 (1 rule) | 3 |
| s 72A "reprint" | reprint | 882 | encoded | nt-part7a-reprints.l4 (1 rule) | 3 |
| s 72B | Reprint of legislation in force at stated date | 883 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 72B(1) | A reprint of legislation must show the legislation as in force at the ... | 884 | encoded | nt-part7a-reprints.l4: s 72B(1): the reprint must show the amendment as in force | 3 |
| s 72B(2) | For the avoidance of doubt, an amendment of legislation that commences... | 885 | encoded | nt-part7a-reprints.l4: s 72B(2), (3): the reprint may include the amendment | 3 |
| s 72B(3) | Subsection (2) does not prevent the inclusion of uncommenced amendment... | 886 | encoded | nt-part7a-reprints.l4: s 72B(2), (3): the reprint may include the amendment | 3 |
| s 72C | Omission of making words in reprint | 887-888 | encoded | nt-part7a-reprints.l4: s 72C: the reprint may include the item | 4 |
| s 72C(a) | the words of making the legislation; or | 889 | encoded | nt-part7a-reprints.l4: s 72C: the reprint may include the item | 4 |
| s 72C(b) | the date of the making of the legislation; or | 890 | encoded | nt-part7a-reprints.l4: s 72C: the reprint may include the item | 4 |
| s 72C(c) | the signature of the person making the legislation. | 891 | encoded | nt-part7a-reprints.l4: s 72C: the reprint may include the item | 4 |
| s 72D | Inclusion of tables of amendments in reprints | 892-893 | encoded | nt-part7a-reprints.l4: s 72D(a): the table of amendments lists each amending Act or instrument; s 72D(b): the table of amendments lists each provision that has been amended | 5 |
| s 72D(a) | each amending Act or other instrument that has amended that legislatio... | 894 | encoded | nt-part7a-reprints.l4: s 72D(a): the table of amendments lists each amending Act or instrument; s 72D(b): the table of amendments lists each provision that has been amended | 5 |
| s 72D(b) | each provision of that legislation that has been amended and a referen... | 895 | encoded | nt-part7a-reprints.l4: s 72D(b): the table of amendments lists each provision that has been amended | 2 |
| Part VIII | Transitional matters | 896 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Part VIII, Division 1 | Justice Legislation Amendment Act 2006 | 897 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 73 | Subordinate legislation | 898 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 73(1) | This section applies if, immediately before the commencement of this s... | 899 | encoded | nt-part8-transitional.l4: s 73: the reference to regulations is taken to include a reference to rules or by-laws | 3 |
| s 73(2) | Despite the repeal of the definition, the reference is taken to includ... | 900 | encoded | nt-part8-transitional.l4: s 73: the reference to regulations is taken to include a reference to rules or by-laws | 3 |
| s 74 | Numbering of subordinate legislation | 901-902 | encoded | nt-part8-transitional.l4: s 74: the citation of the subordinate legislation by its number and year | 3 |
| s 74 Example for section 74 | Example for section 74 | 903-904 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| Part VIII, Division 2 | Interpretation Legislation Amendment Act 2018 | 905 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 75 | Short titles and cross references taken to include year of enactment or making | 906 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 75(1) | On and after the repeal of the Amendments Incorporation Act 1938: | 907 | encoded | nt-part8-transitional.l4: s 75(1)(a), (b), (c): the short title or reference is taken to include the year of enactment or making | 5 |
| s 75(1)(a) | the short title of an Act that, but for the operation of section 4(1) ... | 908 | encoded | nt-part8-transitional.l4: s 75(1)(a), (b), (c): the short title or reference is taken to include the year of enactment or making | 5 |
| s 75(1)(b) | the short title of subordinate legislation is taken to include the yea... | 909 | encoded | nt-part8-transitional.l4: s 75(1)(a), (b), (c): the short title or reference is taken to include the year of enactment or making | 5 |
| s 75(1)(c) | a reference in an Act or subordinate legislation to another Act or sub... | 910 | encoded | nt-part8-transitional.l4: s 75(1)(a), (b), (c): the short title or reference is taken to include the year of enactment or making | 5 |
| s 75(1)(d) | the short title of an Act or subordinate legislation including its yea... | 911 | encoded | nt-part8-transitional.l4 (2 rules) | 7 |
| s 75(2) | For the avoidance of doubt, a reference in any other document of any k... | 912 | encoded | nt-part8-transitional.l4: s 75(2): the reference in the other document fails | 2 |
| s 76 | Disapplication of section 50(1) in certain circumstances | 913-914 | encoded | nt-part8-transitional.l4: s 76: section 50(1) applies to the reference | 2 |
| s 76 Example for section 76 | Example for section 76 | 915-916 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| Part VIII, Division 3 | Interpretation Amendment Act 2021 | 917 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| s 77 | Administrative Arrangements Orders | 918-919 | encoded | nt-part8-transitional.l4: s 77: the order is taken to have been made under section 35 as in force after the commencement | 2 |
| s 78 | Tabling requirements for subordinate legislation | 920-921 | encoded | nt-part8-transitional.l4: s 78: section 63 as formerly in force continues to apply to the subordinate legislation on the day | 5 |
| s 78(a) | regulations made before the commencement; | 922 | encoded | nt-part8-transitional.l4: s 78: section 63 as formerly in force continues to apply to the subordinate legislation on the day | 5 |
| s 78(b) | rules or by-laws signed under section 63(2)(a) before the commencement... | 923 | encoded | nt-part8-transitional.l4: s 78: section 63 as formerly in force continues to apply to the subordinate legislation on the day | 5 |
| Schedule | Ordinances repealed | 924 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Schedule: operative reference | section 2(1) | 925 | inert | reason 1: not operative. Section 55(4) makes it part of the provision it belongs to; sections 62D and 62E say it does not limit or extend that provision. Its header is a row in nt-xrefs.l4. |  |
| Schedule Part 1 | Repeal of Interpretation Ordinances | 926 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Schedule Part 1 item 1 | Interpretation Ordinance 1931 | 927 | encoded | nt-schedule.l4: instrument at line 927 | 2 |
| Schedule Part 1 item 2 | Interpretation Ordinance 1932 | 928 | encoded | nt-schedule.l4: instrument at line 928 | 1 |
| Schedule Part 1 item 3 | Interpretation Ordinance 1933 | 929 | encoded | nt-schedule.l4: instrument at line 929 | 1 |
| Schedule Part 1 item 4 | Interpretation Ordinance 1934 | 930 | encoded | nt-schedule.l4: instrument at line 930 | 1 |
| Schedule Part 1 item 5 | Interpretation Ordinance 1938 | 931 | encoded | nt-schedule.l4: instrument at line 931 | 1 |
| Schedule Part 1 item 6 | Interpretation Ordinance 1940 | 932 | encoded | nt-schedule.l4: instrument at line 932 | 1 |
| Schedule Part 1 item 7 | Interpretation Ordinance 1948 | 933 | encoded | nt-schedule.l4: instrument at line 933 | 1 |
| Schedule Part 1 item 8 | Interpretation Ordinance 1949 | 934 | encoded | nt-schedule.l4: instrument at line 934 | 1 |
| Schedule Part 1 item 9 | Interpretation Ordinance 1952 | 935 | encoded | nt-schedule.l4: instrument at line 935 | 1 |
| Schedule Part 1 item 10 | Interpretation Ordinance (No. 2) 1952 | 936 | encoded | nt-schedule.l4: instrument at line 936 | 1 |
| Schedule Part 1 item 11 | Interpretation Ordinance 1954 | 937 | encoded | nt-schedule.l4: instrument at line 937 | 1 |
| Schedule Part 1 item 12 | Interpretation Ordinance 1956 | 938 | encoded | nt-schedule.l4: instrument at line 938 | 1 |
| Schedule Part 1 item 13 | Interpretation Ordinance 1957 | 939 | encoded | nt-schedule.l4: instrument at line 939 | 1 |
| Schedule Part 1 item 14 | Interpretation Ordinance 1959 | 940 | encoded | nt-schedule.l4: instrument at line 940 | 1 |
| Schedule Part 1 item 15 | Interpretation Ordinance 1962 | 941 | encoded | nt-schedule.l4: instrument at line 941 | 1 |
| Schedule Part 1 item 16 | Interpretation Ordinance 1968 | 942 | encoded | nt-schedule.l4: instrument at line 942 | 1 |
| Schedule Part 1 item 17 | Interpretation Ordinance (No. 2) 1968 | 943 | encoded | nt-schedule.l4: instrument at line 943 | 1 |
| Schedule Part 1 item 18 | Interpretation Ordinance 1969 | 944 | encoded | nt-schedule.l4: instrument at line 944 | 1 |
| Schedule Part 1 item 19 | Interpretation Ordinance 1972 | 945 | encoded | nt-schedule.l4: instrument at line 945 | 1 |
| Schedule Part 1 item 20 | Interpretation Ordinance 1973 | 946 | encoded | nt-schedule.l4: instrument at line 946 | 1 |
| Schedule Part 1 item 21 | Interpretation Ordinance (No. 2) 1973 | 947 | encoded | nt-schedule.l4: instrument at line 947 | 1 |
| Schedule Part 1 item 22 | Interpretation Ordinance 1976 | 948 | encoded | nt-schedule.l4: instrument at line 948 | 1 |
| Schedule Part 1 item 23 | Interpretation Ordinance (No. 3) 1976 | 949 | encoded | nt-schedule.l4: instrument at line 949 | 1 |
| Schedule Part 1 item 24 | Interpretation Ordinance 1977 | 950 | encoded | nt-schedule.l4: instrument at line 950 | 1 |
| Schedule Part 1 item 25 | Interpretation Ordinance (No. 2) 1977 | 951 | encoded | nt-schedule.l4: instrument at line 951 | 1 |
| Schedule Part 1 item 26 | Interpretation (Amendment) Ordinance 1978 | 952 | encoded | nt-schedule.l4: instrument at line 952 | 2 |
| Schedule Part 2 | Repeal of Regulations Publication Ordinance | 953 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Schedule Part 2 item 1 | Regulations Publication Ordinance 1940 | 954 | encoded | nt-schedule.l4: instrument at line 954 | 1 |
| Schedule Part 2 item 2 | Regulations Publication Ordinance 1952 | 955 | encoded | nt-schedule.l4: instrument at line 955 | 2 |
| Schedule Part 3 | Repeal of Administrator's Council Ordinance | 956 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Schedule Part 3 item 1 | Administrator's Council Ordinance 1959 | 957 | encoded | nt-schedule.l4: instrument at line 957 | 1 |
| Schedule Part 3 item 2 | Administrator's Council Ordinance 1963 | 958 | encoded | nt-schedule.l4: instrument at line 958 | 1 |
| Schedule Part 3 item 3 | Administrator's Council Ordinance 1976 | 959 | encoded | nt-schedule.l4: instrument at line 959 | 2 |
| Schedule Part 4 | Repeal of State Acts | 960 | inert | reason 1: not operative. A heading creates no rule (section 55(1), (2) make headings part of the Act). It is carried as data in nt-provisions.l4. |  |
| Schedule Part 4 item 1 | The Act entitled "An Act for shortening and explaining the Language us... | 961 | encoded | nt-schedule.l4: instrument at line 961 | 1 |
| Schedule Part 4 item 2 | The Language of Acts Amendment Act, 1900. | 962 | encoded | nt-schedule.l4: instrument at line 962 | 2 |

Section numbers not printed (disposition `repealed or blank in this text`):

| provision | what the text shows | endnote line |
| --- | --- | --- |
| s 10 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 10 rep No. 13, 2006, s 22 | 1378 |
| s 32 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 32 rep No. 73, 1993, s 8 | 1410 |
| s 33 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 33 amd No. 35, 2006, s 21 / rep No. 40, 2010, s 49 | 1412 |
| s 45 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 45 amd No. 13, 2006, s 44 / rep No. 28, 2021, s 13 | 1458 |
| s 47 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 47 rep No. 13, 2006, s 35 | 1461 |
| s 60 | not printed in the table of provisions (lines 13 to 141) or the body; the endnotes show: s 60 rep No. 44, 1985, s 2 | 1481 |

Outside the in-scope text:

| lines | what | disposition | reason |
| --- | --- | --- | --- |
| 1-7 | deposit notice | inert | reason 1: not operative |
| 8-11 | cover and title | inert | reason 1: not operative |
| 12-142 | table of provisions | inert | reason 1: not operative; the provision index is built from it |
| 143-148 | title and long title | inert | reason 1: not operative |
| 963-1531 | endnotes | inert | reason 1: section 55(6) says an endnote that is not part of the text of the Act is not part of the Act |

## What the stable binary does not accept

Observed on the stable build 1.6.98 while writing; the second build, 1.6.110, reads every module the same way (the main-build column below).

- Loud: `WHERE` cannot be followed by another `DECIDE` in the same declaration; helpers are top-level functions.
- Loud: `sort` takes numbers only, so strings and dates are ordered with `filter` and a comparison, and the latest date with `maximum`.
- Loud: a constructor or type name defined in two modules that a file imports cannot be used; every module here has distinct names.
- Loud: a constructor pattern binds its fields by position (`WHEN `c` a b THEN`); reading a field of the scrutinee by name fails.
- Loud: comparing dates with `LESS THAN` or `EQUALS` without `IMPORT daydate` is an ambiguous operator; with it, dates are compared through `Day x`.
- Silent: `NOT a OR b` parses as `NOT (a OR b)`, so an answer changes with no error; every `NOT` in the encoding is parenthesised.
- Not listed on the skill pages: `TOLOWER` exists in the stable build's prelude; it is used for section 57B.
- Not used, as the brief says: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, a `YMD` type of our own.

## What check.sh prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
nt-cases-seat.l4                               0       165       0        0         0 |      0       165       0        0  same
nt-interpretation-time.l4                      0         0       0        0         0 |      0         0       0        0  same
nt-part1-application.l4                        0         0       0        0         0 |      0         0       0        0  same
nt-part2-commencement.l4                       0         0       0        0         0 |      0         0       0        0  same
nt-part4-definitions.l4                        0         0       0        0         0 |      0         0       0        0  same
nt-part4-reading.l4                            0         0       0        0         0 |      0         0       0        0  same
nt-part4a-penalties.l4                         0         0       0        0         0 |      0         0       0        0  same
nt-part5-powers.l4                             0         0       0        0         0 |      0         0       0        0  same
nt-part6-mechanics.l4                          0         0       0        0         0 |      0         0       0        0  same
nt-part7-construction.l4                       0         0       0        0         0 |      0         0       0        0  same
nt-part7-general.l4                            0         0       0        0         0 |      0         0       0        0  same
nt-part7-instruments.l4                        0         0       0        0         0 |      0         0       0        0  same
nt-part7a-reprints.l4                          0         0       0        0         0 |      0         0       0        0  same
nt-part8-transitional.l4                       0         0       0        0         0 |      0         0       0        0  same
nt-provisions.l4                               0         0       0        0         0 |      0         0       0        0  same
nt-schedule.l4                                 0         0       0        0         0 |      0         0       0        0  same
nt-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
nt-tests-part1.l4                              0        29       0        0         0 |      0        29       0        0  same
nt-tests-part2.l4                              0        23       0        0         0 |      0        23       0        0  same
nt-tests-part4-definitions.l4                  0       341       0        0         0 |      0       341       0        0  same
nt-tests-part4-reading.l4                      0       177       0        0         0 |      0       177       0        0  same
nt-tests-part4a.l4                             0        43       0        0         0 |      0        43       0        0  same
nt-tests-part5.l4                              0        96       0        0         0 |      0        96       0        0  same
nt-tests-part6.l4                              0        97       0        0         0 |      0        97       0        0  same
nt-tests-part7-construction.l4                 0        59       0        0         0 |      0        59       0        0  same
nt-tests-part7-general.l4                      0        45       0        0         0 |      0        45       0        0  same
nt-tests-part7-instruments.l4                  0        94       0        0         0 |      0        94       0        0  same
nt-tests-part7a.l4                             0        21       0        0         0 |      0        21       0        0  same
nt-tests-part8.l4                              0        26       0        0         0 |      0        26       0        0  same
nt-tests-schedule.l4                           0        41       0        0         0 |      0        41       0        0  same
nt-tests-time.l4                               0       195       0        0         0 |      0       195       0        0  same
nt-tests-xrefs.l4                              0       148       0        0         0 |      0       148       0        0  same
nt-xrefs.l4                                    0         0       0        0         0 |      0         0       0        0  same
TOTAL (33 modules)                             0      1600       0        0           |      0      1600       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The source checks, run from the encoding folder:

```
$ python3 -I srcrefs.py check --refs ../../registers/source-bundle/11865.txt *.l4
srcrefs check: 741 src: lines, 432 runs, 450 locators, 0 problems
$ python3 -I srcrefs.py check --strict --refs ../../registers/source-bundle/11865.txt *.l4
srcrefs check: 741 src: lines, 432 runs, 450 locators, 0 problems
```

## What would need doing before the encoding is worth relying on

- A person who knows Northern Territory law reads each rule against the official text, not this rendering.
- The fork register is read by the same person, in particular F1 (the first day of a period "after" a day), F2 (months counted one at a time), F6 (service by giving a document to a person), F14 (individuals and "person") and F16 (alphabetical order).
- The seat layer is run through the website's question form, and a person with a real time limit answers it; that has not been done.
- The public holidays of the place where the thing is to be done are supplied by the user; a table from the Act that lists them would let the questions drop that input, but that Act is not among the sources.
- The days on which the Legislative Assembly meets are supplied by the user in the same way.
- The 90 rows of references to other Acts and instruments are not resolved; a rule that needs a fact from one asks it as an input.
