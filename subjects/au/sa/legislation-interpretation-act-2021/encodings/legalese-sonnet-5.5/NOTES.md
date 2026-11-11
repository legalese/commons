# Legislation Interpretation Act 2021 (South Australia): encoding notes

Encoding name: `legalese-sonnet-5.5`.
Status: draft, version 0.1.0.
Method: a single Sonnet 5.5 agent working alone from the brief.
Edition encoded: version 20.11.2025, in the unofficial plain-text rendering deposited at `registers/source-bundle/legislation-interpretation-act-2021.txt`.
The text is not the authorised text of the Act and may be out of date; it is licensed CC BY 4.0 (see `SOURCE-LICENSE.md`).
No domain expert has read this encoding against the text.
Target compiler: `main`.
Written with `l4` 1.6.98 (main, 7689b0d, 2026-10-19); compared with the main build 1.6.110 (main, e51181d, 2026-11-11).

## Seat

The seat is a person who has a time limit to meet under a South Australian Act or statutory instrument (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.
The Act is a set of general rules of reading and, for this seat, a set of rules for counting time, so the seat asks the questions a person asks when a deadline is running or a date is in doubt.
`sa-seat.l4` holds 20 questions in the text's order, grouped under `§` headings: when an Act or provision takes effect or ends, counting a period, having a document served, and penalties and fees.
Every question has `@export` and a `@desc` worded for the person, and takes plain inputs: yes or no, a number, a date, or a choice from a list the modules define.
A time within a day is asked as a number of hours since the day began.
Public holidays are asked as one run of consecutive days, because the Public Holidays Act 2023 is not among the sources.
The seat builds the modules' records inside each question and calls the module rule; it restates no rule.
There is no seat for an official.
The performance of functions, powers of appointment and delegation, gender balance in nominations, and the rules of reading that bind a court are encoded in the layer-1 modules for what they decide, and have no question in the seat layer.
`sa-cases-seat.l4` holds 77 assertions: at least one case for every question, the facts a person in the seat would give, and a case outside the encoding that returns NOTHING.

## What is encoded and what is not

Every section, subsection, paragraph, schedule clause, table row and defined term of the text has a row in the coverage table below.
Layer 1 follows the Act's structure.
Each rule carries `@ref` and the quoted source lines, and each module carries tests with expected values written by hand from the text.

| File | What it holds | Assertions |
| --- | --- | --- |
| `sa-interpretation-time.l4` | The self-contained time module (imports `prelude` and `daydate` only): days and moments (s 4 "day", ss 28, 30), business days and public holidays (s 4, s 46), counting a period (s 4 "month" and "year", s 44(1) and (2) and (3)), commencement by assent and proclamation (s 27), attaining an age (s 49), service by post (s 51(5)). Every function name begins with the section it implements, for example `s 44(1): the last day of a period`. | 0 here; tested in `sa-tests-time.l4` |
| `sa-tests-time.l4` | The tests of the time module, including the worked cases below. | 151 |
| `sa-nouns.l4` | Nouns shared by more than one module. | 0 |
| `sa-provisions.l4` | An index of the 351 parts, sections, subsections, paragraphs, subparagraphs, schedules and clauses of the text, with their headings and lines. | 16 |
| `sa-xrefs.l4` | 54 rows for references from one provision to another provision of this Act, and 35 rows for references to other Acts or instruments, each with a test. | 91 |
| `sa-part1-application.l4` | s 3. | 13 |
| `sa-part2-standard-definitions.l4` | The 91 defined terms of s 4, each as an entry with its limbs, and two tests for each. | 232 |
| `sa-part2-health-table.l4` | The table in s 5(1) (16 rows), and s 5(2). | 33 |
| `sa-part2-reading-words.l4` | ss 6 to 13. | 52 |
| `sa-part3-general.l4` | ss 14 to 26, with s 19A. | 76 |
| `sa-part4-repeal-and-amendment.l4` | ss 27(4), 29 and 31 to 34. | 46 |
| `sa-part5-citation.l4` | ss 35 and 36. | 25 |
| `sa-part6-functions-and-powers.l4` | ss 37 to 43. | 115 |
| `sa-part7-references-distance-amounts.l4` | ss 45, 47, 48 and 50. | 17 |
| `sa-part8-documents.l4` | ss 51(1) to (4) and 52. | 33 |
| `sa-part9-standard-scales.l4` | The table in s 54 (27 rows). | 67 |
| `sa-part9-penalties-and-proceedings.l4` | ss 53 and 55 to 59. | 37 |
| `sa-part10-and-schedule1.l4` | Schedule 1 clauses 24 and 25. | 9 |
| `sa-seat.l4` | The seat layer: 20 questions. | 0 |
| `sa-cases-seat.l4` | Worked cases for the seat layer. | 77 |

Not encoded, and why (each is an `inert` row below): the title block, contents and enacting words; part and section headings; the short title (s 1); the regulation-making powers (s 5(3), s 60); and the notes that point to other Acts.
The Public Holidays Act 2023, the Health Practitioner Regulation National Law, the Criminal Procedure Act 1921, the Electronic Communications Act 2000, the Expiation of Offences Act 1996 and the Legislative Instruments Act 1978 are not among the sources.
Where a rule depends on one of them, the borrowed fact is an input (the list of public holidays, whether a person is registered in a profession).

## Jural relations

Most provisions create no Hohfeldian relation: they define a term, state a rule of reading, or count time.
The table lists those that do.
"Not stated" means the text names no one on the other side.

| Provision | Relation | Holder | Counterparty | Where encoded |
| --- | --- | --- | --- | --- |
| s 8(3) | duty and claim-right | the person who keeps information in digital form | the body or person it must be produced or made available to | `the requirement obliges producing a document the body or person can understand` |
| s 32(2)(d), (e) | right preserved; duty and liability preserved | the holder of a right accrued under the repealed Act; the person subject to a duty or penalty incurred | not stated | `the repeal, amendment or expiry affects` |
| s 32(3) | power and liability | whoever may commence, continue or enforce the proceeding or impose the penalty | the person liable | `it may be commenced, continued, enforced or imposed as if the Act had not been repealed, amended or expired` |
| s 37(1), (2) | power | the person or body on whom the function is conferred; the person holding or performing the duties of the office | not stated | `a function conferred on a person or body may be performed from time to time as occasion requires` |
| s 39(1) | liberty | the persons who are to meet or transact | not stated | `the requirement is taken to be satisfied by meeting or transacting remotely` |
| s 40 | power and liability | the holder of a power to make an instrument | not stated | `a power to make an instrument includes a power to amend or repeal it` |
| s 41(2) | power and liability | the appointer | the person appointed or whose appointment is ended | `the appointer may do this in the appointer's discretion` |
| s 42(3)(a), (c) | duty | the non-government entity (to nominate a panel); the Governor or Minister (to select from it) | not stated | `the Act is taken to provide that the non-government entity must nominate a panel` |
| s 43(2), (6) | power and liability | the delegator | the delegate | `a delegation may be revoked at any time by the delegator` |
| s 51(2), (3) | power and liability | the person serving a document | the person served | `the document may be served on an individual in this way` |
| s 53(1), (2) | liability | the person who commits an offence | not stated | `a penalty may be imposed on a finding of guilt` |
| s 55 | duty | whoever recovers the fine, penalty or forfeiture | the Treasurer of the State | `section 55 requires the recovered fine, penalty or forfeiture to be paid to the Treasurer of the State and to form part of the Consolidated Account` |
| s 57 | power | any person | the person liable to the fine, penalty or forfeiture | `the person may take proceedings to recover a fine, penalty or forfeiture` |
| s 59 | liability | the offender | not stated | `the offender is liable to be prosecuted and punished under either or any of those laws` |

## Coverage table

The table is generated by a script, kept outside the folder, from the text file.
It has one row for each of the 509 units the script finds (parts, sections, subsections, paragraphs, subparagraphs, table rows, defined terms, notes, the schedule and its clauses), and one more row for the file's own notice block (lines 1 to 8).
The script checked that every non-blank line of the text from line 9 to the end falls in some row.
A row is `encoded` when a declaration in a module quotes at least one of its lines; the last column names the module and, for each, up to two of the functions or entries that quote it.
Dispositions: encoded 399, fork 51, inert 59, and the notice block row (inert).
An `inert` row says which of the three permitted reasons applies: not operative (a title, heading, contents list, enacting words or note), machinery (the short title, regulation-making powers), or text shown repealed or blank.
There is no row marked out of scope or deferred.
A `fork` row names the fork-register entry (F1 to F29) that covers it.

| Unit | Lines | Disposition | Where |
| --- | --- | --- | --- |
| File notice block | 1-8 | inert | not operative: the notice block of the text file |
| Title block | 10-12 | inert | not operative: the title block |
| Contents | 13-88 | inert | not operative: the contents list |
| Enacting words | 89 | inert | not operative: the enacting words |
| Part 1 | 90 | inert | not operative: a part heading |
| section 1 | 91-92 | inert | machinery: the short title |
| section 3 | 93 | inert | not operative: the heading; the text is in the rows below |
| section 3(1) | 94 | encoded | sa-part1-application: `the provisions of this Act apply to` |
| section 3(1)(a) | 95 | encoded | sa-part1-application: `the provisions of this Act apply to` |
| section 3(1)(b) | 96 | encoded | sa-part1-application: `the provisions of this Act apply to` |
| section 3(1)(c) | 97 | encoded | sa-part1-application: `the provisions of this Act apply to` |
| section 3(2) | 98 | encoded | sa-part1-application: `this Act applies to an Act or legislative instrument made at a time` |
| section 3(3) | 99 | encoded | sa-part1-application: `the application of this Act is displaced by a contrary intention` |
| Part 2 | 100 | inert | not operative: a part heading |
| section 4 | 101-102 | encoded | sa-interpretation-time: `s 4: the number of days in a week the Act states` / sa-part2-standard-definitions: `a thing falls within the Act's definition` |
| section 4 "Act" | 103 | encoded | sa-part2-standard-definitions: `s 4 definition 1` |
| section 4 "Act"(a) | 104 | encoded | sa-part2-standard-definitions: `s 4 definition 1` |
| section 4 "Act"(b) | 105 | encoded | sa-part2-standard-definitions: `s 4 definition 1` |
| section 4 "ADI" | 106 | encoded | sa-part2-standard-definitions: `s 4 definition 2` |
| section 4 "administrative unit" | 107 | encoded | sa-part2-standard-definitions: `s 4 definition 3` |
| section 4 "affidavit" | 108 | encoded | sa-part2-standard-definitions: `s 4 definition 4` |
| section 4 "amend" | 109 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "amend"(a) | 110 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "amend"(b) | 111 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "amend"(c) | 112 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "amend"(d) | 113 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "amend"(e) | 114 | encoded | sa-part2-standard-definitions: `s 4 definition 5` |
| section 4 "appoint" | 115 | encoded | sa-part2-standard-definitions: `s 4 definition 6` |
| section 4 "AS or Australian Standard or AS/NZS or Australian/New Zealand Standard" | 116 | encoded | sa-part2-standard-definitions: `s 4 definition 7` |
| section 4 "Australia" | 117 | encoded | sa-part2-standard-definitions: `s 4 definition 8`; `a place is within Australia or the Commonwealth` |
| section 4 "Australia Acts" | 118 | encoded | sa-part2-standard-definitions: `s 4 definition 9` |
| section 4 "Australia Acts"(a) | 119 | encoded | sa-part2-standard-definitions: `s 4 definition 9` |
| section 4 "Australia Acts"(b) | 120 | encoded | sa-part2-standard-definitions: `s 4 definition 9` |
| section 4 "Australian citizen" | 121 | encoded | sa-part2-standard-definitions: `s 4 definition 10` |
| section 4 "bank" | 122 | encoded | sa-part2-standard-definitions: `s 4 definition 11` |
| section 4 "bank"(a) | 123 | encoded | sa-part2-standard-definitions: `s 4 definition 11` |
| section 4 "bank"(b) | 124 | encoded | sa-part2-standard-definitions: `s 4 definition 11` |
| section 4 "bank cheque or banker's cheque" | 125 | encoded | sa-part2-standard-definitions: `s 4 definition 12` |
| section 4 "bank holiday" | 126 | encoded | sa-part2-standard-definitions: `s 4 definition 13` |
| section 4 "Banking Act of the Commonwealth or Banking Act (Cwth)" | 127 | encoded | sa-part2-standard-definitions: `s 4 definition 14` |
| section 4 "building society" | 128 | encoded | sa-part2-standard-definitions: `s 4 definition 15` |
| section 4 "building society"(a) | 129 | encoded | sa-part2-standard-definitions: `s 4 definition 15` |
| section 4 "building society"(b) | 130 | encoded | sa-part2-standard-definitions: `s 4 definition 15` |
| section 4 "business day" | 131 | encoded | sa-interpretation-time: `s 4: is a business day` / sa-part2-standard-definitions: `s 4 definition 16` |
| section 4 "business day"(a) | 132 | encoded | sa-interpretation-time: `s 4: is a business day` / sa-part2-standard-definitions: `s 4 definition 16` |
| section 4 "business day"(b) | 133 | encoded | sa-interpretation-time: `s 4: is a business day` / sa-part2-standard-definitions: `s 4 definition 16` |
| section 4 "calendar month" | 134 | encoded | sa-interpretation-time: `s 4: is one of the 12 months of the calendar year` / sa-part2-standard-definitions: `s 4 definition 17` |
| section 4 "calendar year" | 135 | encoded | sa-interpretation-time: `s 4: the last day of the calendar year` / sa-part2-standard-definitions: `s 4 definition 18` |
| section 4 "certified mail" | 136 | encoded | sa-part2-standard-definitions: `s 4 definition 19` |
| section 4 "commencement" | 137 | encoded | sa-part2-standard-definitions: `s 4 definition 20` |
| section 4 "Commonwealth" | 138 | encoded | sa-part2-standard-definitions: `s 4 definition 21`; `a place is within Australia or the Commonwealth` |
| section 4 "confer" | 139 | encoded | sa-part2-standard-definitions: `s 4 definition 22` |
| section 4 "contravene" | 140 | encoded | sa-part2-standard-definitions: `s 4 definition 23` |
| section 4 "council or local council" | 141 | encoded | sa-part2-standard-definitions: `s 4 definition 24` |
| section 4 "Court of Appeal" | 142 | encoded | sa-part2-standard-definitions: `s 4 definition 25` |
| section 4 "credit union" | 143 | encoded | sa-part2-standard-definitions: `s 4 definition 26` |
| section 4 "credit union"(a) | 144 | encoded | sa-part2-standard-definitions: `s 4 definition 26` |
| section 4 "credit union"(b) | 145 | encoded | sa-part2-standard-definitions: `s 4 definition 26` |
| section 4 "Crown" | 146 | encoded | sa-part2-standard-definitions: `s 4 definition 27` |
| section 4 "data storage device" | 147 | encoded | sa-part2-standard-definitions: `s 4 definition 28` |
| section 4 "day" | 148 | encoded | sa-interpretation-time: `s 4: seconds in a day`; `s 4: the beginning of a day` (+3 more) / sa-part2-standard-definitions: `s 4 definition 29` |
| section 4 "Department or department of a Minister or of the Public Service, government department or public department" | 149 | encoded | sa-part2-standard-definitions: `s 4 definition 30` |
| section 4 "District Court" | 150 | encoded | sa-part2-standard-definitions: `s 4 definition 31` |
| section 4 "document" | 151 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "document"(a) | 152 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "document"(b) | 153 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "document"(c) | 154 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "document"(d) | 155 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "document"(e) | 156 | encoded | sa-part2-standard-definitions: `s 4 definition 32` |
| section 4 "DPP" | 157 | encoded | sa-part2-standard-definitions: `s 4 definition 33` |
| section 4 "entity" | 158 | encoded | sa-part2-standard-definitions: `s 4 definition 34` |
| section 4 "estate" | 159 | encoded | sa-part2-standard-definitions: `s 4 definition 35` |
| section 4 "external Territory" | 160 | encoded | sa-part2-standard-definitions: `s 4 definition 36` |
| section 4 "financial year" | 161 | encoded | sa-interpretation-time: `s 4: the last day of the financial year starting on 1 July` / sa-part2-standard-definitions: `s 4 definition 37` |
| section 4 "friendly society" | 162 | encoded | sa-part2-standard-definitions: `s 4 definition 38` |
| section 4 "foreign country" | 163 | encoded | sa-part2-standard-definitions: `s 4 definition 39` |
| section 4 "function" | 164 | encoded | sa-part2-standard-definitions: `s 4 definition 40` |
| section 4 "Gazette, Government Gazette or South Australian Government Gazette" | 165 | encoded | sa-part2-standard-definitions: `s 4 definition 41` |
| section 4 "gender identity" | 166 | encoded | sa-part2-standard-definitions: `s 4 definition 42` |
| section 4 "Governor-in-Chief, Governor or Lieutenant-Governor" | 167 | encoded | sa-part2-standard-definitions: `s 4 definition 43` |
| section 4 "Health Practitioner Regulation National Law" | 168 | encoded | sa-part2-standard-definitions: `s 4 definition 44` |
| section 4 "Health Practitioner Regulation National Law"(a) | 169 | encoded | sa-part2-standard-definitions: `s 4 definition 44` |
| section 4 "Health Practitioner Regulation National Law"(a)(i) | 170 | encoded | sa-part2-standard-definitions: `s 4 definition 44` |
| section 4 "Health Practitioner Regulation National Law"(a)(ii) | 171 | encoded | sa-part2-standard-definitions: `s 4 definition 44` |
| section 4 "Health Practitioner Regulation National Law"(b) | 172 | encoded | sa-part2-standard-definitions: `s 4 definition 44` |
| section 4 "His Majesty or Her Majesty, the King or the Queen" | 173 | encoded | sa-part2-standard-definitions: `s 4 definition 45` |
| section 4 "individual" | 174 | encoded | sa-part2-standard-definitions: `s 4 definition 46` |
| section 4 "internal Territory" | 175 | encoded | sa-part2-standard-definitions: `s 4 definition 47` |
| section 4 "intersex status" | 176 | encoded | sa-part2-standard-definitions: `s 4 definition 48` |
| section 4 "intersex status"(a) | 177 | encoded | sa-part2-standard-definitions: `s 4 definition 48` |
| section 4 "intersex status"(b) | 178 | encoded | sa-part2-standard-definitions: `s 4 definition 48` |
| section 4 "intersex status"(c) | 179 | encoded | sa-part2-standard-definitions: `s 4 definition 48` |
| section 4 "Jervis Bay Territory" | 180 | encoded | sa-part2-standard-definitions: `s 4 definition 49` |
| section 4 "justice" | 181 | encoded | sa-part2-standard-definitions: `s 4 definition 50` |
| section 4 "land" | 182 | encoded | sa-part2-standard-definitions: `s 4 definition 51` |
| section 4 "land"(a) | 183 | encoded | sa-part2-standard-definitions: `s 4 definition 51` |
| section 4 "land"(b) | 184 | encoded | sa-part2-standard-definitions: `s 4 definition 51` |
| section 4 "land"(c) | 185 | encoded | sa-part2-standard-definitions: `s 4 definition 51` |
| section 4 "land"(d) | 186 | encoded | sa-part2-standard-definitions: `s 4 definition 51` |
| section 4 "legislative instrument" | 187 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "legislative instrument"(a) | 188 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "legislative instrument"(b) | 189 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "legislative instrument"(c) | 190 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "legislative instrument"(d) | 191 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "legislative instrument"(e) | 192 | encoded | sa-part2-standard-definitions: `s 4 definition 52` |
| section 4 "Magistrates Court" | 193 | encoded | sa-part2-standard-definitions: `s 4 definition 53` |
| section 4 "major indictable offence" | 194 | encoded | sa-part2-standard-definitions: `s 4 definition 54` |
| section 4 "make" | 195 | encoded | sa-part2-standard-definitions: `s 4 definition 55` |
| section 4 "Minister" | 196 | encoded | sa-part2-standard-definitions: `s 4 definition 56` |
| section 4 "Minister"(a) | 197 | encoded | sa-part2-standard-definitions: `s 4 definition 56` |
| section 4 "Minister"(b) | 198-199 | encoded | sa-part2-standard-definitions: `s 4 definition 56` |
| section 4 "minor indictable offence" | 200 | encoded | sa-part2-standard-definitions: `s 4 definition 57` |
| section 4 "month" | 201 | fork | sa-interpretation-time: `s 4: the first day of the month a number of months after the month of a day`; `s 4 and s 44(1) item 8: the last day of a period of months beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 58` -- F2 |
| section 4 "month"(a) | 202 | encoded | sa-interpretation-time: `s 4: the first day of the month a number of months after the month of a day`; `s 4 and s 44(1) item 8: the last day of a period of months beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 58` |
| section 4 "month"(b) | 203 | encoded | sa-interpretation-time: `s 4: the first day of the month a number of months after the month of a day`; `s 4 and s 44(1) item 8: the last day of a period of months beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 58` |
| section 4 "motor vehicle" | 204 | encoded | sa-part2-standard-definitions: `s 4 definition 59` |
| section 4 "Northern Territory" | 205 | encoded | sa-part2-standard-definitions: `s 4 definition 60` |
| section 4 "oath" | 206 | encoded | sa-part2-standard-definitions: `s 4 definition 61` |
| section 4 "office" | 207 | encoded | sa-part2-standard-definitions: `s 4 definition 62` |
| section 4 "Parliament" | 208 | encoded | sa-part2-standard-definitions: `s 4 definition 63` |
| section 4 "part‑day public holiday" | 209 | encoded | sa-part2-standard-definitions: `s 4 definition 64` |
| section 4 "person" | 210 | encoded | sa-part2-standard-definitions: `s 4 definition 65` |
| section 4 "police force" | 211 | encoded | sa-part2-standard-definitions: `s 4 definition 66` |
| section 4 "police officer" | 212 | encoded | sa-part2-standard-definitions: `s 4 definition 67` |
| section 4 "prescribed" | 213 | encoded | sa-part2-standard-definitions: `s 4 definition 68` |
| section 4 "prescribed"(a) | 214 | encoded | sa-part2-standard-definitions: `s 4 definition 68` |
| section 4 "prescribed"(b) | 215 | encoded | sa-part2-standard-definitions: `s 4 definition 68` |
| section 4 "proclamation" | 216 | encoded | sa-part2-standard-definitions: `s 4 definition 69` |
| section 4 "public holiday" | 217 | encoded | sa-interpretation-time: `Public holiday` / sa-part2-standard-definitions: `s 4 definition 70` |
| section 4 "public holiday"(a) | 218 | encoded | sa-interpretation-time: `Public holiday` / sa-part2-standard-definitions: `s 4 definition 70` |
| section 4 "public holiday"(b) | 219 | encoded | sa-interpretation-time: `Public holiday` / sa-part2-standard-definitions: `s 4 definition 70` |
| section 4 "Public Service or public service" | 220 | encoded | sa-part2-standard-definitions: `s 4 definition 71` |
| section 4 "regulation, rule or by-law" | 221 | encoded | sa-part2-standard-definitions: `s 4 definition 72` |
| section 4 "regulation, rule or by-law"(a) | 222 | encoded | sa-part2-standard-definitions: `s 4 definition 72` |
| section 4 "regulation, rule or by-law"(b) | 223 | encoded | sa-part2-standard-definitions: `s 4 definition 72` |
| section 4 "repeal" | 224 | encoded | sa-part2-standard-definitions: `s 4 definition 73` |
| section 4 "SAPOL" | 225 | encoded | sa-part2-standard-definitions: `s 4 definition 74` |
| section 4 "sitting day" | 226 | encoded | sa-part2-standard-definitions: `s 4 definition 75`; `a day is a sitting day of a House` |
| section 4 "South Australian Civil and Administrative Tribunal or SACAT" | 227 | encoded | sa-part2-standard-definitions: `s 4 definition 76` |
| section 4 "South Australian Employment Tribunal or SAET" | 228 | encoded | sa-part2-standard-definitions: `s 4 definition 77` |
| section 4 "special justice" | 229 | encoded | sa-part2-standard-definitions: `s 4 definition 78` |
| section 4 "Standards Association of Australia" | 230 | encoded | sa-part2-standard-definitions: `s 4 definition 79` |
| section 4 "Standards Australia" | 231 | encoded | sa-part2-standard-definitions: `s 4 definition 80` |
| section 4 "statutory declaration" | 232 | encoded | sa-part2-standard-definitions: `s 4 definition 81` |
| section 4 "statutory declaration"(a) | 233 | encoded | sa-part2-standard-definitions: `s 4 definition 81` |
| section 4 "statutory declaration"(b) | 234 | encoded | sa-part2-standard-definitions: `s 4 definition 81` |
| section 4 "statutory declaration"(b)(i) | 235 | encoded | sa-part2-standard-definitions: `s 4 definition 81` |
| section 4 "statutory declaration"(b)(ii) | 236 | encoded | sa-part2-standard-definitions: `s 4 definition 81` |
| section 4 "statutory instrument" | 237 | encoded | sa-part2-standard-definitions: `s 4 definition 82` |
| section 4 "summary offence" | 238 | encoded | sa-part2-standard-definitions: `s 4 definition 83` |
| section 4 "Supreme Court" | 239 | encoded | sa-part2-standard-definitions: `s 4 definition 84` |
| section 4 "swear" | 240 | encoded | sa-part2-standard-definitions: `s 4 definition 85` |
| section 4 "the State or this State" | 241 | encoded | sa-part2-standard-definitions: `s 4 definition 86` |
| section 4 "this Act" | 242 | encoded | sa-part2-standard-definitions: `s 4 definition 87` |
| section 4 "United Kingdom" | 243 | encoded | sa-part2-standard-definitions: `s 4 definition 88` |
| section 4 "writing" | 244 | encoded | sa-part2-standard-definitions: `s 4 definition 89` |
| section 4 "year" | 245 | fork | sa-interpretation-time: `s 4: the last day of a year beginning on a day`; `s 4: the last day of a period of years beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 90` -- F3 |
| section 4 "year"(a) | 246 | encoded | sa-interpretation-time: `s 4: the last day of a year beginning on a day`; `s 4: the last day of a period of years beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 90` |
| section 4 "year"(b) | 247 | encoded | sa-interpretation-time: `s 4: the last day of a year beginning on a day`; `s 4: the last day of a period of years beginning on a day` (+2 more) / sa-part2-standard-definitions: `s 4 definition 90` |
| section 4 "Youth Court" | 248 | encoded | sa-part2-standard-definitions: `s 4 definition 91` |
| section 5 | 249 | inert | not operative: the heading; the text is in the rows below |
| section 5(1) | 250-251 | encoded | sa-part2-health-table: `a person is within a reference in column 1 of the table` |
| section 5(1) table row: Column 1 | 252 | inert | not operative: the heading row of the table |
| section 5(1) table row: chiropractor | 253 | encoded | sa-part2-health-table: `s 5(1) row 1` |
| section 5(1) table row: dental practitioner | 254 | encoded | sa-part2-health-table: `s 5(1) row 2` |
| section 5(1) table row: dentist | 255 | encoded | sa-part2-health-table: `s 5(1) row 3` |
| section 5(1) table row: enrolled nurse | 256 | encoded | sa-part2-health-table: `s 5(1) row 4` |
| section 5(1) table row: legally qualified medical practitioner | 257 | encoded | sa-part2-health-table: `s 5(1) row 5` |
| section 5(1) table row: medical practitioner | 258 | encoded | sa-part2-health-table: `s 5(1) row 6` |
| section 5(1) table row: midwife | 259 | encoded | sa-part2-health-table: `s 5(1) row 7` |
| section 5(1) table row: nurse | 260 | encoded | sa-part2-health-table: `s 5(1) row 8` |
| section 5(1) table row: occupational therapist | 261 | encoded | sa-part2-health-table: `s 5(1) row 9` |
| section 5(1) table row: optometrist | 262 | encoded | sa-part2-health-table: `s 5(1) row 10` |
| section 5(1) table row: osteopath | 263 | encoded | sa-part2-health-table: `s 5(1) row 11` |
| section 5(1) table row: pharmacist | 264 | encoded | sa-part2-health-table: `s 5(1) row 12` |
| section 5(1) table row: physiotherapist | 265 | encoded | sa-part2-health-table: `s 5(1) row 13` |
| section 5(1) table row: podiatrist | 266 | encoded | sa-part2-health-table: `s 5(1) row 14` |
| section 5(1) table row: psychologist | 267 | encoded | sa-part2-health-table: `s 5(1) row 15` |
| section 5(1) table row: registered nurse | 268 | encoded | sa-part2-health-table: `s 5(1) row 16` |
| section 5(2) | 269 | encoded | sa-part2-health-table: `a person is within a reference to a registered health practitioner` |
| section 5(3) | 270 | inert | machinery: a regulation-making power to amend the table |
| section 6 | 271-272 | encoded | sa-part2-reading-words: `a definition in an Act or legislative instrument applies to its construction` |
| section 7 | 273-274 | encoded | sa-part2-reading-words: `another form of a defined word or phrase has a corresponding meaning` |
| section 8 | 275 | inert | not operative: the heading; the text is in the rows below |
| section 8(1) | 276 | encoded | sa-part2-reading-words: `a word describing the physical form includes the digital form` |
| section 8(2) | 277 | encoded | sa-part2-reading-words: `a reference includes its digital counterpart under section 8(2)` |
| section 8(2)(a) | 278 | encoded | sa-part2-reading-words: `a reference includes its digital counterpart under section 8(2)` |
| section 8(2)(b) | 279 | encoded | sa-part2-reading-words: `a reference includes its digital counterpart under section 8(2)` |
| section 8(2)(c) | 280 | encoded | sa-part2-reading-words: `a reference includes its digital counterpart under section 8(2)` |
| section 8(2)(d) | 281 | encoded | sa-part2-reading-words: `a reference includes its digital counterpart under section 8(2)` |
| section 8(3) | 282 | encoded | sa-part2-reading-words: `the requirement obliges producing a document the body or person can understand`; `producing that document complies with the requirement` |
| section 8(3)(a) | 283 | encoded | sa-part2-reading-words: `the requirement obliges producing a document the body or person can understand`; `producing that document complies with the requirement` |
| section 8(3)(b) | 284-285 | encoded | sa-part2-reading-words: `the requirement obliges producing a document the body or person can understand`; `producing that document complies with the requirement` |
| section 8(3)(c) | 286 | encoded | sa-part2-reading-words: `the requirement obliges producing a document the body or person can understand` |
| section 8(3)(d) | 287 | encoded | sa-part2-reading-words: `producing that document complies with the requirement` |
| section 9 | 288 | inert | not operative: the heading; the text is in the rows below |
| section 9(1) | 289 | encoded | sa-part2-reading-words: `a word implying a particular gender is construed as applicable to` |
| section 9(2) | 290 | encoded | sa-part2-reading-words: `a word implying a particular gender includes a body corporate as well as an individual` |
| section 9(3) | 291 | encoded | sa-part2-reading-words: `a phrase of a masculine and a feminine pronoun joined by "or" is applicable to` |
| section 10 | 292 | inert | not operative: the heading; the text is in the rows below |
| section 10(1) | 293 | encoded | sa-part2-reading-words: `a word in the singular is construed as including the plural` |
| section 10(2) | 294 | encoded | sa-part2-reading-words: `a word in the plural is construed as including the singular` |
| section 10(3) | 295 | encoded | sa-part2-reading-words: `a word in the plural or singular is construed as including a body corporate as well as an individual` |
| section 11 | 296 | inert | not operative: the heading; the text is in the rows below |
| section 11(1) | 297 | encoded | sa-part2-reading-words: `what the entity on which a function is conferred has` |
| section 11(2) | 298 | encoded | sa-part2-reading-words: `what the entity on which a function is conferred has` |
| section 11(3) | 299 | encoded | sa-part2-reading-words: `what the entity on which a function is conferred has` |
| section 11(4) | 300 | encoded | sa-part2-reading-words: `section 11 applies to an Act or legislative instrument passed on` |
| section 12 | 301-302 | encoded | sa-part2-reading-words: `the meaning of an expression used in an instrument made under an Act` |
| section 13 | 303-304 | encoded | sa-part2-reading-words: `an Act or legislative instrument is taken to authorise a body corporate to sign or execute in this manner` |
| section 13(a) | 305 | encoded | sa-part2-reading-words: `an Act or legislative instrument is taken to authorise a body corporate to sign or execute in this manner` |
| section 13(b) | 306 | encoded | sa-part2-reading-words: `an Act or legislative instrument is taken to authorise a body corporate to sign or execute in this manner` |
| section 13 note | 307-308 | inert | not operative: a note pointing to other provisions |
| Part 3 | 309 | inert | not operative: a part heading |
| section 14 | 310 | inert | not operative: the heading; the text is in the rows below |
| section 14(1) | 311 | encoded | sa-part3-general: `an interpretation is to be preferred to any other` |
| section 14(2) | 312 | encoded | sa-part3-general: `section 14 operates to create or extend criminal liability` |
| section 15 | 313 | inert | not operative: the heading; the text is in the rows below |
| section 15(1) | 314 | encoded | sa-part3-general: `an Act or legislative instrument operates as to this part of its reach under section 15(1)` |
| section 15(2) | 315 | encoded | sa-part3-general: `a legislative instrument operates as to this part of its reach under section 15(2)` |
| section 15(3) | 316 | encoded | sa-part3-general: `a provision has effect as to this part of its reach under section 15(3)` |
| section 16 | 317 | inert | not operative: the heading; the text is in the rows below |
| section 16(1) | 318 | encoded | sa-part3-general: `consideration may be given to the material` |
| section 16(1)(a) | 319 | encoded | sa-part3-general: `consideration may be given to the material` |
| section 16(1)(b) | 320 | encoded | sa-part3-general: `consideration may be given to the material` |
| section 16(1)(b)(i) | 321 | encoded | sa-part3-general: `consideration may be given to the material` |
| section 16(1)(b)(ii) | 322 | encoded | sa-part3-general: `consideration may be given to the material` |
| section 16(2) | 323 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(a) | 324 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(b) | 325 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(c) | 326 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(d) | 327 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(e) | 328 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(f) | 329 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(g) | 330 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(2)(h) | 331 | encoded | sa-part3-general: `the material is included among the material that may be considered` |
| section 16(3) | 332 | encoded | sa-part3-general: `regard must be had to the matter in deciding whether to consider material` |
| section 16(3)(a) | 333 | encoded | sa-part3-general: `regard must be had to the matter in deciding whether to consider material` |
| section 16(3)(b) | 334 | encoded | sa-part3-general: `regard must be had to the matter in deciding whether to consider material` |
| section 17 | 335-336 | encoded | sa-part3-general: `a provision is applied to the circumstances as they arise` |
| section 18 | 337-338 | encoded | sa-part3-general: `re-enactment of a provision that has been construed creates a presumption that Parliament sanctioned the construction` |
| section 19 | 339 | inert | not operative: the heading; the text is in the rows below |
| section 19(1) | 340 | encoded | sa-part3-general: `a thing appearing in an Act or legislative instrument is part of it` |
| section 19(2) | 341 | encoded | sa-part3-general: `a thing appearing in an Act or legislative instrument is part of it` |
| section 19(2)(a) | 342 | encoded | sa-part3-general: `a thing appearing in an Act or legislative instrument is part of it` |
| section 19(2)(b) | 343 | encoded | sa-part3-general: `a thing appearing in an Act or legislative instrument is part of it` |
| section 19(2)(c) | 344 | encoded | sa-part3-general: `a thing appearing in an Act or legislative instrument is part of it` |
| section 19A | 345-346 | encoded | sa-part3-general: `an amending Act or instrument must be construed as part of the amended Act or instrument` |
| section 20 | 347-348 | encoded | sa-part3-general: `an example included in an Act or legislative instrument is exhaustive` |
| section 20(a) | 349 | encoded | sa-part3-general: `an example included in an Act or legislative instrument is exhaustive` |
| section 20(b) | 350 | encoded | sa-part3-general: `an example included in an Act or legislative instrument is exhaustive`; `an example may do this to the meaning of the provision it relates to` |
| section 21 | 351-352 | encoded | sa-part3-general: `the Governor's act is taken to be done with the advice and consent of the Executive Council` |
| section 22 | 353 | inert | not operative: the heading; the text is in the rows below |
| section 22(1) | 354 | encoded | sa-part3-general: `an Act passed or instrument made after 20 June 1990 is taken to bind the Crown`; `binding the Crown under section 22(1) imposes criminal liability on the Crown` |
| section 22(2) | 355 | encoded | sa-part3-general: `whether the amendment binds the Crown is decided by section 22(3)` |
| section 22(3) | 356 | encoded | sa-part3-general: `an Act passed or instrument made on or before 20 June 1990 is taken to bind the Crown` |
| section 22(4) | 357 | encoded | sa-part3-general: `the Crown's immunity extends to an agent where the Act binds the Crown` |
| section 22(5) | 358 | encoded | sa-part3-general: `the Crown's immunity extends to an agent where the Act does not bind the Crown` |
| section 22(6) | 359 | encoded | sa-part3-general: `a reference to the Crown extends to the Crown in this capacity` |
| section 22(6)(a) | 360 | encoded | sa-part3-general: `a reference to the Crown extends to the Crown in this capacity` |
| section 22(6)(b) | 361 | encoded | sa-part3-general: `a reference to an agent of the Crown extends to` |
| section 22(6)(c) | 362 | encoded | sa-part3-general: `an agent acts within the scope of the agent's obligations` |
| section 23 | 363-364 | encoded | sa-part3-general: `the day the State is taken to have been established` |
| section 24 | 365-366 | encoded | sa-part3-general: `a provision has the effect it would have had if the Australia Acts had been in operation` |
| section 25 | 367-368 | encoded | sa-part3-general: `an Act is taken to be a public Act` |
| section 26 | 369-370 | encoded | sa-part3-general: `a provision or portion of an Act needs separate enacting words to have effect as a substantive enactment` |
| Part 4 | 371 | inert | not operative: a part heading |
| section 27 | 372 | inert | not operative: the heading; the text is in the rows below |
| section 27(1) | 373 | encoded | sa-interpretation-time: `s 27(1): the day an Act with no commencement provision comes into operation` |
| section 27(2) | 374 | encoded | sa-interpretation-time: `s 27(2): the day a Bill is taken to have been assented to` |
| section 27(3) | 375 | encoded | sa-interpretation-time: `s 27(3) and (5): the day fixed by the proclamations made so far` |
| section 27(3)(a) | 376 | encoded | sa-interpretation-time: `s 27(3) and (5): the day fixed by the proclamations made so far` |
| section 27(3)(b) | 377 | encoded | sa-interpretation-time: `s 27(3) and (5): the day fixed by the proclamations made so far` |
| section 27(3)(c) | 378 | encoded | sa-interpretation-time: `s 27(3) and (5): the day fixed by the proclamations made so far` |
| section 27(4) | 379 | encoded | sa-part4-repeal-and-amendment: `a reference to a provision of an Act extends to this for the purposes of section 27(3)` |
| section 27(4)(a) | 380 | encoded | sa-part4-repeal-and-amendment: `a reference to a provision of an Act extends to this for the purposes of section 27(3)` |
| section 27(4)(b) | 381 | encoded | sa-part4-repeal-and-amendment: `a reference to a provision of an Act extends to this for the purposes of section 27(3)` |
| section 27(5) | 382 | encoded | sa-interpretation-time: `s 27(3) and (5): the day fixed by the proclamations made so far` |
| section 27(6) | 383 | fork | sa-interpretation-time: `s 27(6) and (7): the day an Act or provision to be brought into operation by proclamation comes into operation` -- F6 |
| section 27(6)(a) | 384 | fork | sa-interpretation-time: `s 27(6) and (7): the day an Act or provision to be brought into operation by proclamation comes into operation` -- F6 |
| section 27(6)(b) | 385-386 | fork | sa-interpretation-time: `s 27(6): the anniversary of a day in a later year`; `s 27(6) and (7): the day an Act or provision to be brought into operation by proclamation comes into operation` -- F6 |
| section 27(7) | 387 | encoded | sa-interpretation-time: `s 27(6) and (7): the day an Act or provision to be brought into operation by proclamation comes into operation` |
| section 27 note | 388-389 | inert | not operative: a note pointing to the Legislative Instruments Act 1978 |
| section 28 | 390-391 | encoded | sa-interpretation-time: `s 28: the moment an Act or provision comes into operation on a particular day`; `ss 28 and 30: a provision is in operation at a moment` |
| section 29 | 392-393 | encoded | sa-part4-repeal-and-amendment: `an Act or legislative instrument may include a provision specifying a day on which it expires` |
| section 30 | 394-395 | fork | sa-interpretation-time: `s 30: the moment up to which an expiring provision continues to have effect`; `ss 28 and 30: a provision is in operation at a moment` -- F4 |
| section 31 | 396 | inert | not operative: the heading; the text is in the rows below |
| section 31(1) | 397 | fork | sa-part4-repeal-and-amendment: `a provision under a heading amends what the heading specifies` -- F7 |
| section 31(2) | 398 | fork | sa-part4-repeal-and-amendment: `a provision under a heading amends what the heading specifies` -- F7 |
| section 32 | 399 | inert | not operative: the heading; the text is in the rows below |
| section 32(1) | 400 | fork | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` -- F8 |
| section 32(1)(a) | 401 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(1)(b) | 402 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2) | 403 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(a) | 404 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(b) | 405 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(c) | 406 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(d) | 407 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(e) | 408 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(2)(f) | 409 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry affects` |
| section 32(3) | 410 | encoded | sa-part4-repeal-and-amendment: `it may be commenced, continued, enforced or imposed as if the Act had not been repealed, amended or expired` |
| section 32(4) | 411 | encoded | sa-part4-repeal-and-amendment: `the office, court, tribunal or body continues in existence` |
| section 32(5) | 412 | encoded | sa-part4-repeal-and-amendment: `the repealed, amended or expired provision continues in force for completing the act, matter or thing` |
| section 32(6) | 413 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry ends` |
| section 32(6)(a) | 414 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry ends` |
| section 32(6)(b) | 415 | encoded | sa-part4-repeal-and-amendment: `the repeal, amendment or expiry ends` |
| section 32(7) | 416 | encoded | sa-part4-repeal-and-amendment: `a proceeding is a legal proceeding` |
| section 32 "legal proceeding" | 417 | encoded | sa-part4-repeal-and-amendment: `a proceeding is a legal proceeding` |
| section 33 | 418 | inert | not operative: the heading; the text is in the rows below |
| section 33(1) | 419 | fork | sa-part4-repeal-and-amendment: `an administrative act done under a replaced provision is regarded as done for the purposes of the replacement` -- F9 |
| section 33(2) | 420 | encoded | sa-part4-repeal-and-amendment: `the instrument remains in force as if made under the subsequent Act or provision` |
| section 33(2)(a) | 421 | encoded | sa-part4-repeal-and-amendment: `the instrument remains in force as if made under the subsequent Act or provision` |
| section 33(2)(b) | 422-423 | encoded | sa-part4-repeal-and-amendment: `the instrument remains in force as if made under the subsequent Act or provision` |
| section 33(3) | 424 | encoded | sa-part4-repeal-and-amendment: `an Act, instrument or provision is taken to have been replaced` |
| section 34 | 425-426 | encoded | sa-part4-repeal-and-amendment: `an Act may be amended or repealed in the session of Parliament in which it was passed` |
| Part 5 | 427 | inert | not operative: a part heading |
| section 35 | 428 | inert | not operative: the heading; the text is in the rows below |
| section 35(1) | 429 | encoded | sa-part5-citation: `an Act or legislative instrument of this jurisdiction may be cited in this way` |
| section 35(1)(a) | 430 | encoded | sa-part5-citation: `an Act or legislative instrument of this jurisdiction may be cited in this way` |
| section 35(1)(b) | 431 | encoded | sa-part5-citation: `an Act or legislative instrument of this jurisdiction may be cited in this way` |
| section 35(2) | 432 | encoded | sa-part5-citation: `an Act or legislative instrument of another jurisdiction may be cited in this way` |
| section 35(3) | 433 | encoded | sa-part5-citation: `a reference to an Act includes a reference to the legislative instrument` |
| section 35(4) | 434 | encoded | sa-part5-citation: `a reference to a portion or provision of an Act includes a reference to the legislative instrument` |
| section 35(4)(a) | 435 | encoded | sa-part5-citation: `a reference to a portion or provision of an Act includes a reference to the legislative instrument` |
| section 35(4)(b) | 436 | encoded | sa-part5-citation: `a reference to a portion or provision of an Act includes a reference to the legislative instrument` |
| section 35(5) | 437 | encoded | sa-part5-citation: `section 35 renders unlawful or ineffective a citation or reference not made in a manner it authorises` |
| section 36 | 438 | inert | not operative: the heading; the text is in the rows below |
| section 36(1) | 439 | encoded | sa-part5-citation: `section 36 applies to a reference to` |
| section 36(1)(a) | 440 | encoded | sa-part5-citation: `section 36 applies to a reference to` |
| section 36(1)(b) | 441 | encoded | sa-part5-citation: `section 36 applies to a reference to` |
| section 36(2) | 442 | encoded | sa-part5-citation: `the reference is a reference to the enactment as replaced and amended from time to time`; `the reference is a reference to the enactment as amended from time to time` |
| Part 6 | 443 | inert | not operative: a part heading |
| section 37 | 444 | inert | not operative: the heading; the text is in the rows below |
| section 37(1) | 445 | encoded | sa-part6-functions-and-powers: `a function conferred on a person or body may be performed from time to time as occasion requires` |
| section 37(2) | 446 | encoded | sa-part6-functions-and-powers: `a function conferred on the holder of an office may be performed by the person` |
| section 37(3) | 447 | encoded | sa-part6-functions-and-powers: `the performance of a function conferred on a body is affected` |
| section 38 | 448 | inert | not operative: the heading; the text is in the rows below |
| section 38(1) | 449 | fork | sa-part6-functions-and-powers: `a function conferred by a provision not yet in operation may be performed before it comes into operation` -- F10 |
| section 38(1)(a) | 450 | fork | sa-part6-functions-and-powers: `a function conferred by a provision not yet in operation may be performed before it comes into operation` -- F10 |
| section 38(1)(b) | 451-452 | fork | sa-part6-functions-and-powers: `a function conferred by a provision not yet in operation may be performed before it comes into operation` -- F10 |
| section 38(2) | 453 | encoded | sa-part6-functions-and-powers: `a thing done by virtue of section 38(1) has taken effect` |
| section 38(3) | 454 | encoded | sa-part6-functions-and-powers: `the appointed person may act in the office or the established body may meet and perform its functions before the provision comes into operation`; `the appointed person or the established body has the same entitlement to remuneration or allowances as if the provision were in operation` |
| section 38(3)(a) | 455 | encoded | sa-part6-functions-and-powers: `the appointed person may act in the office or the established body may meet and perform its functions before the provision comes into operation`; `the appointed person or the established body has the same entitlement to remuneration or allowances as if the provision were in operation` |
| section 38(3)(b) | 456 | encoded | sa-part6-functions-and-powers: `the appointed person may act in the office or the established body may meet and perform its functions before the provision comes into operation`; `the appointed person or the established body has the same entitlement to remuneration or allowances as if the provision were in operation` |
| section 39 | 457 | inert | not operative: the heading; the text is in the rows below |
| section 39(1) | 458 | fork | sa-part6-functions-and-powers: `the requirement is taken to be satisfied by meeting or transacting remotely` -- F11 |
| section 39(1)(a) | 459 | fork | sa-part6-functions-and-powers: `the requirement is taken to be satisfied by meeting or transacting remotely` -- F11 |
| section 39(1)(b) | 460 | fork | sa-part6-functions-and-powers: `the requirement is taken to be satisfied by meeting or transacting remotely` -- F11 |
| section 39(2) | 461 | encoded | sa-part6-functions-and-powers: `the requirement is taken to be satisfied by meeting or transacting remotely` |
| section 39(3) | 462 | encoded | sa-part6-functions-and-powers: `the requirement is taken to be satisfied by meeting or transacting remotely` |
| section 39(4) | 463 | encoded | sa-part6-functions-and-powers: `the person is taken to be present at the meeting and to form part of any quorum` |
| section 40 | 464-465 | encoded | sa-part6-functions-and-powers: `a power to make an instrument includes a power to amend or repeal it`; `the same conditions apply to the amendment or repeal as applied to the making` |
| section 41 | 466 | inert | not operative: the heading; the text is in the rows below |
| section 41(1) | 467 | encoded | sa-part6-functions-and-powers: `section 41 applies` |
| section 41(1)(a) | 468 | encoded | sa-part6-functions-and-powers: `section 41 applies` |
| section 41(1)(b) | 469-470 | encoded | sa-part6-functions-and-powers: `section 41 applies` |
| section 41(2) | 471 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion` |
| section 41(2)(a) | 472 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion` |
| section 41(2)(b) | 473 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion` |
| section 41(2)(c) | 474 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion` |
| section 41(2)(d) | 475 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion` |
| section 41(2)(e) | 476 | encoded | sa-part6-functions-and-powers: `the appointer may do this in the appointer's discretion`; `the appointer may appoint another person temporarily or permanently` |
| section 41(2)(e)(i) | 477 | encoded | sa-part6-functions-and-powers: `the appointer may appoint another person temporarily or permanently` |
| section 41(2)(e)(ii) | 478 | encoded | sa-part6-functions-and-powers: `the appointer may appoint another person temporarily or permanently` |
| section 41(3) | 479 | encoded | sa-part6-functions-and-powers: `it is taken to include an authorisation to appoint a person to act in the office` |
| section 41(4) | 480 | fork | sa-part6-functions-and-powers: `a person may be appointed to act in the office` -- F12 |
| section 41(5) | 481 | encoded | sa-part6-functions-and-powers: `the person is taken to be appointed to do the thing` |
| section 41(6) | 482 | encoded | sa-part6-functions-and-powers: `the person has all the functions of the holder of the office` |
| section 41(7) | 483 | encoded | sa-part6-functions-and-powers: `an appointment made by the holder of a particular office ceases to have effect` |
| section 41(8) | 484 | encoded | sa-part6-functions-and-powers: `what was done by a person purporting to act in an office is invalid merely because` |
| section 41(8)(a) | 485 | encoded | sa-part6-functions-and-powers: `what was done by a person purporting to act in an office is invalid merely because` |
| section 41(8)(b) | 486 | encoded | sa-part6-functions-and-powers: `what was done by a person purporting to act in an office is invalid merely because` |
| section 41(8)(c) | 487 | encoded | sa-part6-functions-and-powers: `what was done by a person purporting to act in an office is invalid merely because` |
| section 41(8)(d) | 488 | encoded | sa-part6-functions-and-powers: `what was done by a person purporting to act in an office is invalid merely because` |
| section 42 | 489 | inert | not operative: the heading; the text is in the rows below |
| section 42(1) | 490 | encoded | sa-part6-functions-and-powers: `section 42 applies` |
| section 42(2) | 491 | encoded | sa-part6-functions-and-powers: `the panel includes at least 1 woman and 1 man` |
| section 42(2)(a) | 492 | encoded | sa-part6-functions-and-powers: `the panel includes at least 1 woman and 1 man` |
| section 42(2)(b) | 493 | fork | sa-part6-functions-and-powers: `the panel is comprised of equal numbers of women and men as far as practicable` -- F13 |
| section 42(3) | 494 | encoded | sa-part6-functions-and-powers: `the fewest persons the panel may comprise` |
| section 42(3)(a) | 495 | fork | sa-part6-functions-and-powers: `the fewest persons the panel may comprise`; `the fewest persons the panel may comprise on the reading that doubles the number plus 1` (+1 more) -- F14 |
| section 42(3)(b) | 496 | encoded | sa-part6-functions-and-powers: `the panel includes at least 1 woman and 1 man` |
| section 42(3)(b)(i) | 497 | encoded | sa-part6-functions-and-powers: `the panel includes at least 1 woman and 1 man` |
| section 42(3)(b)(ii) | 498 | fork | sa-part6-functions-and-powers: `the panel is comprised of equal numbers of women and men as far as practicable` -- F13 |
| section 42(3)(c) | 499 | encoded | sa-part6-functions-and-powers: `the Act is taken to provide that the Governor or Minister must select the person from the panel` |
| section 42(4) | 500 | encoded | sa-part6-functions-and-powers: `section 42 derogates from the need to properly assess merit in selecting persons for appointment` |
| section 42(5) | 501 | encoded | sa-part6-functions-and-powers: `the person or body is a non-government entity` |
| section 42 "man" | 502 | encoded | sa-part6-functions-and-powers: `the person is a man for section 42 regardless of the person's designated sex at birth` |
| section 42 "non-government entity" | 503 | encoded | sa-part6-functions-and-powers: `the person or body is a non-government entity` |
| section 42 "woman" | 504 | encoded | sa-part6-functions-and-powers: `the person is a woman for section 42 regardless of the person's designated sex at birth` |
| section 43 | 505 | inert | not operative: the heading; the text is in the rows below |
| section 43(1) | 506 | encoded | sa-part6-functions-and-powers: `section 43 applies` |
| section 43(2) | 507 | encoded | sa-part6-functions-and-powers: `a delegation may be made subject to conditions or limitations specified by the delegator`; `a delegation may be revoked at any time by the delegator` |
| section 43(3) | 508 | fork | sa-part6-functions-and-powers: `a delegation of the power of delegation can be made`; `a purported delegation of all of the functions of the delegator is read as excluding the power of delegation` -- F15 |
| section 43(4) | 509 | fork | sa-part6-functions-and-powers: `section 43(4) makes the function depend on the delegate's opinion, belief or state of mind in relation to that matter` -- F16 |
| section 43(5) | 510 | encoded | sa-part6-functions-and-powers: `the function is taken to have been exercised by the delegator` |
| section 43(6) | 511 | encoded | sa-part6-functions-and-powers: `the delegator may exercise the function despite the delegation` |
| section 43(7) | 512 | encoded | sa-part6-functions-and-powers: `the delegator may delegate the function to a person or body in this way` |
| section 43(8) | 513 | encoded | sa-part6-functions-and-powers: `the delegation to the holder of a particular office is taken to be made to the person` |
| section 43(9) | 514 | encoded | sa-part6-functions-and-powers: `the delegation includes the additional function` |
| section 43(10) | 515 | fork | sa-part6-functions-and-powers: `the delegation is of the function as so altered` -- F16 |
| section 43(11) | 516 | encoded | sa-part6-functions-and-powers: `a delegation made by, or to, the holder of a particular office ceases to have effect` |
| section 43(12) | 517 | encoded | sa-part6-functions-and-powers: `the validity of a delegation is affected by the error` |
| section 43(13) | 518 | encoded | sa-part6-functions-and-powers: `the person or body is a delegate within section 43` |
| section 43 "delegate" | 519 | encoded | sa-part6-functions-and-powers: `the person or body is a delegate within section 43` |
| Part 7 | 520 | inert | not operative: a part heading |
| section 44 | 521 | inert | not operative: the heading; the text is in the rows below |
| section 44(1) | 522 | fork | sa-interpretation-time: `How a period is expressed to begin` -- F1 |
| section 44(1) table row: Column 1 Item | 523 | inert | not operative: the heading row of the table |
| section 44(1) table row: 1 | 524 | encoded | sa-interpretation-time: `s 44(1): the last day of a period`; `s 44(1) and (2): the last day on which a thing may be done within a period` (+3 more) |
| section 44(1) table row: 2 | 525 | fork | sa-interpretation-time: `How a period is expressed to begin`; `s 44(1): the first day counted in a period` (+2 more) -- F1 |
| section 44(1) table row: 3 | 526 | fork | sa-interpretation-time: `How a period is expressed to begin`; `s 44(1): the first day counted in a period` (+2 more) -- F1 |
| section 44(1) table row: 4 | 527 | encoded | sa-interpretation-time: `s 44(1): the last day of a period`; `s 44(1) and (2): the last day on which a thing may be done within a period` (+2 more) |
| section 44(1) table row: 5 | 528 | encoded | sa-interpretation-time: `s 44(1): the last day of a period`; `s 44(1) and (2): the last day on which a thing may be done within a period` (+2 more) |
| section 44(1) table row: 6 | 529 | fork | sa-interpretation-time: `How a period is expressed to begin`; `s 44(1): the first day counted in a period` (+2 more) -- F1 |
| section 44(1) table row: 7 | 530 | encoded | sa-interpretation-time: `s 44(1): the last day of a period`; `s 44(1) and (2): the last day on which a thing may be done within a period` (+2 more) |
| section 44(1) table row: 8 | 531 | fork | sa-interpretation-time: `s 4 and s 44(1) item 8: the last day of a period of months beginning on a day`; `s 44(1): the last day of a period` (+2 more) -- F2 |
| section 44(2) | 532 | fork | sa-interpretation-time: `s 44(2): the next day that is a business day`; `s 44(2): the last day on which a thing may be done` (+1 more) -- F5 |
| section 44(3) | 533 | encoded | sa-interpretation-time: `s 44(3): the thing must be done as soon as is reasonably practicable` |
| section 45 | 534-535 | fork | sa-part7-references-distance-amounts: `the reference is a reference to the legal time in the jurisdiction` -- F17 |
| section 46 | 536-537 | encoded | sa-interpretation-time: `s 46: an exclusion of public holidays extends to a holiday` |
| section 47 | 538-539 | fork | sa-part7-references-distance-amounts: `the number of sitting days in a span` -- F18 |
| section 48 | 540-541 | encoded | sa-part7-references-distance-amounts: `the distance measured in a straight line on a horizontal plane` |
| section 49 | 542 | inert | not operative: the heading; the text is in the rows below |
| section 49(1) | 543 | encoded | sa-interpretation-time: `s 49: the moment a person attains an age in years` |
| section 49(2) | 544 | encoded | sa-interpretation-time: `s 49: the moment a person attains an age in years` |
| section 50 | 545-546 | fork | sa-part7-references-distance-amounts: `the amount payable after rounding down to a multiple of 5 cents` -- F19 |
| Part 8 | 547 | inert | not operative: a part heading |
| section 51 | 548 | inert | not operative: the heading; the text is in the rows below |
| section 51(1) | 549 | encoded | sa-part8-documents: `section 51 applies` |
| section 51(2) | 550 | encoded | sa-part8-documents: `the document may be served on an individual in this way` |
| section 51(2)(a) | 551 | encoded | sa-part8-documents: `the document may be served on an individual in this way` |
| section 51(2)(b) | 552 | fork | sa-part8-documents: `the document may be served on an individual in this way` -- F20 |
| section 51(2)(b)(i) | 553 | fork | sa-part8-documents: `the document may be served on an individual in this way` -- F20 |
| section 51(2)(b)(ii) | 554 | fork | sa-part8-documents: `the document may be served on an individual in this way` -- F20 |
| section 51(2)(c) | 555 | encoded | sa-part8-documents: `the document may be served on an individual in this way` |
| section 51(3) | 556 | encoded | sa-part8-documents: `the document may be served on a body corporate in this way` |
| section 51(3)(a) | 557 | fork | sa-part8-documents: `the document may be served on a body corporate in this way` -- F20 |
| section 51(3)(a)(i) | 558 | fork | sa-part8-documents: `the document may be served on a body corporate in this way` -- F20 |
| section 51(3)(a)(ii) | 559 | fork | sa-part8-documents: `the document may be served on a body corporate in this way` -- F20 |
| section 51(3)(a)(iii) | 560 | fork | sa-part8-documents: `the document may be served on a body corporate in this way` -- F20 |
| section 51(3)(b) | 561 | encoded | sa-part8-documents: `the document may be served on a body corporate in this way` |
| section 51(4) | 562 | encoded | sa-part8-documents: `a document is posted to an address` |
| section 51(5) | 563 | encoded | sa-interpretation-time: `s 51(5): the moment service by post is taken to be effected` |
| section 51 note | 564-565 | inert | not operative: a note pointing to the Electronic Communications Act 2000 |
| section 52 | 566-567 | fork | sa-part8-documents: `the form used is sufficient` -- F21 |
| Part 9 | 568 | inert | not operative: a part heading |
| section 53 | 569 | inert | not operative: the heading; the text is in the rows below |
| section 53(1) | 570 | encoded | sa-part9-penalties-and-proceedings: `a penalty may be imposed on a finding of guilt` |
| section 53(1)(a) | 571 | encoded | sa-part9-penalties-and-proceedings: `a penalty may be imposed on a finding of guilt` |
| section 53(1)(b) | 572 | fork | sa-part9-penalties-and-proceedings: `a penalty may be imposed on a finding of guilt`; `section 53(1)(b) makes a contravention of the provision an offence` -- F22 |
| section 53(2) | 573 | fork | sa-part9-penalties-and-proceedings: `the changed penalty applies to the offence` -- F23 |
| section 53(2)(a) | 574 | fork | sa-part9-penalties-and-proceedings: `the changed penalty applies to the offence` -- F23 |
| section 53(2)(b) | 575 | fork | sa-part9-penalties-and-proceedings: `the changed penalty applies to the offence` -- F23 |
| section 53(3) | 576 | encoded | sa-part9-penalties-and-proceedings: `it is a penalty for section 53` |
| section 53 "penalty" | 577 | encoded | sa-part9-penalties-and-proceedings: `it is a penalty for section 53` |
| section 53 note | 578-579 | inert | not operative: a note pointing to the Expiation of Offences Act 1996 |
| section 54 | 580-581 | fork | sa-part9-standard-scales: `a proposed penalty is within the standard scale` -- F24 |
| section 54 table row: Division 1 imprisonment | 582 | encoded | sa-part9-standard-scales: `s 54 row 1` |
| section 54 table row: Division 1 fine | 583 | encoded | sa-part9-standard-scales: `s 54 row 2` |
| section 54 table row: Division 2 imprisonment | 584 | encoded | sa-part9-standard-scales: `s 54 row 3` |
| section 54 table row: Division 2 fine | 585 | encoded | sa-part9-standard-scales: `s 54 row 4` |
| section 54 table row: Division 3 imprisonment | 586 | encoded | sa-part9-standard-scales: `s 54 row 5` |
| section 54 table row: Division 3 fine | 587 | encoded | sa-part9-standard-scales: `s 54 row 6` |
| section 54 table row: Division 4 imprisonment | 588 | encoded | sa-part9-standard-scales: `s 54 row 7` |
| section 54 table row: Division 4 fine | 589 | encoded | sa-part9-standard-scales: `s 54 row 8` |
| section 54 table row: Division 5 imprisonment | 590 | encoded | sa-part9-standard-scales: `s 54 row 9` |
| section 54 table row: Division 5 fine | 591 | encoded | sa-part9-standard-scales: `s 54 row 10` |
| section 54 table row: Division 6 imprisonment | 592 | encoded | sa-part9-standard-scales: `s 54 row 11` |
| section 54 table row: Division 6 fine | 593 | encoded | sa-part9-standard-scales: `s 54 row 12` |
| section 54 table row: Division 6 fee | 594 | encoded | sa-part9-standard-scales: `s 54 row 13` |
| section 54 table row: Division 7 imprisonment | 595 | encoded | sa-part9-standard-scales: `s 54 row 14` |
| section 54 table row: Division 7 fine | 596 | encoded | sa-part9-standard-scales: `s 54 row 15` |
| section 54 table row: Division 7 fee | 597 | encoded | sa-part9-standard-scales: `s 54 row 16` |
| section 54 table row: Division 8 imprisonment | 598 | encoded | sa-part9-standard-scales: `s 54 row 17` |
| section 54 table row: Division 8 fine | 599 | encoded | sa-part9-standard-scales: `s 54 row 18` |
| section 54 table row: Division 8 fee | 600 | encoded | sa-part9-standard-scales: `s 54 row 19` |
| section 54 table row: Division 9 fine | 601 | encoded | sa-part9-standard-scales: `s 54 row 20` |
| section 54 table row: Division 9 fee | 602 | encoded | sa-part9-standard-scales: `s 54 row 21` |
| section 54 table row: Division 10 fine | 603 | encoded | sa-part9-standard-scales: `s 54 row 22` |
| section 54 table row: Division 10 fee | 604 | encoded | sa-part9-standard-scales: `s 54 row 23` |
| section 54 table row: Division 11 fine | 605 | encoded | sa-part9-standard-scales: `s 54 row 24` |
| section 54 table row: Division 11 fee | 606 | encoded | sa-part9-standard-scales: `s 54 row 25` |
| section 54 table row: Division 12 fine | 607 | encoded | sa-part9-standard-scales: `s 54 row 26` |
| section 54 table row: Division 12 fee | 608 | encoded | sa-part9-standard-scales: `s 54 row 27` |
| section 55 | 609-610 | encoded | sa-part9-penalties-and-proceedings: `section 55 requires the recovered fine, penalty or forfeiture to be paid to the Treasurer of the State and to form part of the Consolidated Account` |
| section 56 | 611-612 | encoded | sa-part9-penalties-and-proceedings: `a reference to an offence punishable by imprisonment for a specified term or more includes the offence` |
| section 57 | 613-614 | fork | sa-part9-penalties-and-proceedings: `the person may take proceedings to recover a fine, penalty or forfeiture` -- F25 |
| section 58 | 615 | inert | not operative: the heading; the text is in the rows below |
| section 58(1) | 616 | fork | sa-part9-penalties-and-proceedings: `section 58(1) makes those offences be dealt with under the Criminal Procedure Act 1921 as summary offences` -- F26 |
| section 58(2) | 617 | fork | sa-part9-penalties-and-proceedings: `section 58(2) makes the sum recoverable on information in proceedings under the Criminal Procedure Act 1921`; `section 58(2) makes an order for payment enforceable as if it were a fine` -- F26 |
| section 58(3) | 618 | encoded | sa-part9-penalties-and-proceedings: `the expression in an Act or legislative instrument is taken to be a reference to` |
| section 58(4) | 619 | encoded | sa-part9-penalties-and-proceedings: `the expression in an Act or legislative instrument is taken to be a reference to` |
| section 58(5) | 620 | encoded | sa-part9-penalties-and-proceedings: `the reference is to be construed so as to recognise that all offences are to be charged on information` |
| section 59 | 621-622 | fork | sa-part9-penalties-and-proceedings: `the offender is liable to be prosecuted and punished under either or any of those laws`; `the offender is liable to be punished twice for the same offence` -- F27 |
| Part 10 | 623 | inert | not operative: a part heading |
| section 60 | 624 | inert | machinery: the regulation-making power |
| section 60(1) | 625 | inert | machinery: the regulation-making power and what regulations may do |
| section 60(2) | 626 | inert | machinery: the regulation-making power and what regulations may do |
| section 60(2)(a) | 627 | inert | machinery: the regulation-making power and what regulations may do |
| section 60(2)(b) | 628 | inert | machinery: the regulation-making power and what regulations may do |
| section 60(2)(c) | 629 | inert | machinery: the regulation-making power and what regulations may do |
| section 60(2)(d) | 630 | inert | machinery: the regulation-making power and what regulations may do |
| Schedule 1 | 631 | inert | not operative: the schedule heading |
| Schedule 1 Part 7 | 632 | inert | not operative: the heading of the part of the schedule |
| clause 24 of Schedule 1 | 633 | inert | not operative: the heading; the text is in the rows below |
| clause 24 of Schedule 1(1) | 634 | fork | sa-part10-and-schedule1: `a section heading to an amending provision forms part of the Act` -- F28 |
| clause 24 of Schedule 1(2) | 635 | encoded | sa-part10-and-schedule1: `a provision of an Act is an amending provision` |
| clause 24 of Schedule 1 "amending provision of an Act" | 636 | encoded | sa-part10-and-schedule1: `a provision of an Act is an amending provision` |
| clause 25 of Schedule 1 | 637-638 | fork | sa-part10-and-schedule1: `section 44 operates to alter the period of time provided or allowed for the doing of the thing` -- F29 |

## Fork register

Each entry gives the provision, the function, the answer taken, the other reading, and the text that licenses the answer.
Where the rulings on `JUST FALSE` and `NOTHING` do not settle a case, the answer is decided at the site on the text's own words.

| # | Provision | Function | Answer taken | Other reading | Text that licenses it |
| --- | --- | --- | --- | --- | --- |
| F1 | s 44(1) items 2, 3 and 6 | `s 44(1): the first day counted in a period` | Item 2 counts the specified day itself. Items 3 and 6 begin the day after the act, event or specified day. For a period expressed to begin "from a specified day" the text does not say how it is counted, so the answer is NOTHING. | Count "from a specified day" like item 3 (the table uses "from" only with an act or event) or like item 2. | Item 2 "begin at, on or with a specified day ... includes that specified day"; item 3 "begin on, from or after the happening of an act or event ... does not include the day"; item 6 "begin after a specified day ... does not include that specified day". |
| F2 | s 4 "month"; s 44(1) item 8 | `s 4 and s 44(1) item 8: the last day of a period of months beginning on a day` | A period of 1 or more months, from its first day counted, ends immediately before the corresponding day of the month that many months on, or at the end of that month if it has no such day. A period that begins the day after an event is counted the same way from that day. | Repeat the single month of s 4 "month" one month at a time (kept as `s 4 and s 44(1) item 8, alternative reading: the last day of a period of months counted one month at a time`; 31 January 2025 and 2 months give 31 March 2025 on it). | Item 8 "a period of 2 or more months expressed to begin at, on or with a specified day ... ends immediately before the corresponding day of the calendar month ... or, if there is no corresponding day, at the end of the ending month"; s 4 "month" says the same for one month. |
| F3 | s 4 "year" | `s 4: the last day of a period of years beginning on a day` | A period of N years is N successive years, each beginning the day after the one before ends. | One step to the corresponding day N years on (kept as `s 4, alternative reading: the last day of a period of years counted in one step`; 29 February 2024 and 4 years give 28 February 2028 on it). | Section 4 "year" defines a single year only; nothing says how several years combine. |
| F4 | s 30 | `ss 28 and 30: a provision is in operation at a moment` | A provision expressed to expire on a day is in operation up to, but not at, the stroke of midnight that ends the day. | The instant of that midnight is still within the operation. | Section 30 "continues to have effect until the end of the specified day"; s 4 "day" "a period of 24 hours ending at the stroke of midnight". |
| F5 | s 44(2) | `s 44(2): the last day on which a thing may be done` | The rule moves the last day of a period counted in days, months or years alike to the next business day. | Apply it to a period counted in days only. | Section 44(2) speaks of "the last day for doing it", whatever the unit of the period. |
| F6 | s 27(6) | `s 27(6): the anniversary of a day in a later year` | The text does not say what the second anniversary of 29 February is where the second year is not a leap year, so the answer is NOTHING. | Take 28 February or 1 March, as s 49(2) does for an age. | Section 49(2) gives the 29 February rule for attaining an age only; section 27(6) speaks of "the second anniversary of the date". |
| F7 | s 31 | `a provision under a heading amends what the heading specifies` | In an Act, a heading naming a legislative instrument made by another authority is within subsection (1). In a legislative instrument, a heading naming an Act or another authority's instrument gives NOTHING. | JUST FALSE for those two cases in a legislative instrument. | Subsection (2) names only the same authority and has no "only"; subsection (1) says "a legislative instrument" without limit. |
| F8 | s 32(1) | `the repeal, amendment or expiry affects` | NOTHING when no repeal, amendment or expiry has happened. | JUST FALSE under the brief's rule for "applies if". | The function's JUST FALSE reads "is not affected"; the text does not say that of something never repealed. |
| F9 | s 33(1) | `an administrative act done under a replaced provision is regarded as done for the purposes of the replacement` | Not replaced: JUST FALSE ("If ... is replaced"). Not done in accordance with the old provision, or its effect exhausted: NOTHING. Inconsistent with the provision as it stands after the replacement: JUST FALSE ("if it is not inconsistent"). | NOTHING for the not-replaced case. | "If ... is replaced, an administrative act done in accordance with it (... not being an administrative act the effect of which was exhausted) will be regarded as ... if it is not inconsistent". |
| F10 | s 38(1) | `a function conferred by a provision not yet in operation may be performed before it comes into operation` | An unmet condition of (a) or (b) gives JUST FALSE. | NOTHING. | The opening words are "If". |
| F11 | s 39(1) | `the requirement is taken to be satisfied by meeting or transacting remotely` | A requirement of the first kind met by any means other than audio visual, audio or both gives JUST FALSE. | NOTHING. | "will be taken to be satisfied if the persons meet ... remotely using 1 or both ... of the following". |
| F12 | s 41(4) | `a person may be appointed to act in the office` | The input "no appointment has ever been made" does not change the answer. | Ask the input and answer differently when an appointment has been made. | "even if no appointment has ever been made to the office". |
| F13 | s 42(2)(b) and (3)(b)(ii) | `the panel is comprised of equal numbers of women and men as far as practicable` | When equal numbers are practicable, JUST TRUE exactly when the counts are equal. When they are not practicable, NOTHING, because the text does not say how far from equal a panel may be. | JUST FALSE for any unequal panel. | "must, as far as practicable, be comprised of equal numbers of women and men". |
| F14 | s 42(3)(a) | `the fewest persons the panel may comprise` | "twice the number of members ... plus 1" is read as the number doubled and then 1 added: (2 x n) + 1. | 2 x (n + 1), kept as `the fewest persons the panel may comprise on the reading that doubles the number plus 1`. | "not less than twice the number of members of the body to be appointed on the nomination of the entity plus 1". |
| F15 | s 43(3) | `a delegation of the power of delegation can be made` | No express contrary provision: JUST FALSE. A contrary provision exists: NOTHING, because the bar lifts and section 43 itself grants nothing. | JUST TRUE where the contrary provision exists. | "Unless the Act or the legislative instrument expressly provides to the contrary, a delegation of the power of delegation cannot be made". |
| F16 | s 43(4) and (10) | `section 43(4) makes the function depend on the delegate's opinion, belief or state of mind in relation to that matter` and `the delegation is of the function as so altered` | An unmet "If" gives JUST FALSE, read as "this section gives no such effect". | NOTHING. | Both subsections begin "If". |
| F17 | s 45 | `the reference is a reference to the legal time in the jurisdiction` | The function answers only that the reference is to the legal time; it does not compute a time, because the text does not say what the legal time is. | Compute a time zone offset. | "a reference ... to time ... is a reference to the legal time in the jurisdiction". |
| F18 | s 47 | `the number of sitting days in a span` | A contrary intention gives NOTHING (the text does not say how the days then count); the span is closed at both ends. | A half-open span. | "unless the contrary intention appears, a reference to the number of those days regardless of whether the days ... occur in different sessions ... or in different Parliaments". |
| F19 | s 50 | `the amount payable after rounding down to a multiple of 5 cents` | The calculated amount is in cents and may carry a fraction of a cent; an exact multiple is left as it is. | Round a fraction of a cent up. | "if not an exact multiple of 5 cents, is to be rounded down to the highest multiple of 5 cents that is less than that amount". |
| F20 | s 51(2)(b)(ii) and (3)(a)(iii) | `the document may be served on an individual in this way` and `... on a body corporate in this way` | Leaving or posting to the last known place is JUST FALSE when the person did designate a physical address ("if such an address is not so designated"). Leaving or posting to the designated address when none was designated is NOTHING. | JUST FALSE for the designated-address ways too. | "if such an address is not so designated, the place of residence or a place of business ... last known to the server". |
| F21 | s 52 | `the form used is sufficient` | "provided that deviations ... are not calculated to mislead" is a condition: calculated to mislead gives JUST FALSE. A form not to the same effect, or no prescribed form, gives NOTHING. | JUST FALSE for a form not to the same effect. | "a form to the same effect is sufficient provided that deviations from the prescribed or approved form are not calculated to mislead". |
| F22 | s 53(1)(b) | `section 53(1)(b) makes a contravention of the provision an offence` | When an offence is mentioned in the provision the function answers JUST FALSE ("if an offence is not mentioned"); paragraph (a) covers that case. | NOTHING. | "(b) if an offence is not mentioned in the provision, a contravention of the provision is an offence". |
| F23 | s 53(2) | `the changed penalty applies to the offence` | An offence committed after a reduction takes effect gives NOTHING (the paragraph speaks only of earlier offences). "After" is strictly later on the scale of seconds. An increase applies only to offences committed after it takes effect. | JUST TRUE for a reduction and a later offence. | "(a) is increased, the increased penalty applies only to offences committed after the increase takes effect; or (b) is reduced, the reduced penalty extends to offences committed before the reduction takes effect (if the penalty is being imposed after ...)". |
| F24 | s 54 | `the amount the table in section 54 gives` | Imprisonment is held in months (a year is 12 months), a fine or fee in dollars. A fee is a fixed sum; a fine or term is a ceiling. | Hold terms in years. | "a term of imprisonment not exceeding 15 years"; "a fine not exceeding $75 000"; "an expiation fee of $315". |
| F25 | s 57 | `the person may take proceedings to recover a fine, penalty or forfeiture` | The right is vested in a particular officer or person and the person is that officer: NOTHING (the Act that vests the right decides). Someone else: JUST FALSE. | JUST TRUE for the officer. | "Any person may take proceedings ... unless the right to take proceedings is vested by the Act ... in a particular officer or person". |
| F26 | s 58(1) and (2) | `section 58(1) makes ...` and `section 58(2) makes ...` | An unmet "If" gives JUST FALSE, read as "this section makes no such provision". | NOTHING. | Both subsections begin "If an Act or a legislative instrument provides ...". |
| F27 | s 59 | `the offender is liable to be prosecuted and punished under either or any of those laws` | Fewer than 2 laws, or a contrary intention: JUST FALSE. | NOTHING. | "If an act or omission constitutes an offence under 2 or more Acts ... the offender will, unless the contrary intention appears, be liable". |
| F28 | Schedule 1 cl 24(1) | `a section heading to an amending provision forms part of the Act` | A Bill introduced on the day section 19 commenced is introduced after commencement (section 28: operation begins with the day), so only an earlier day is "before". | The Bill introduced on that day is "before". | "if the Bill for that Act was introduced in either House of Parliament before the commencement of section 19"; s 28. |
| F29 | Schedule 1 cl 25 | `section 44 operates to alter the period of time provided or allowed for the doing of the thing` | A period that commenced before the Act: JUST FALSE ("does not operate ... if"). Otherwise NOTHING (the clause does not say that section 44 does operate). | JUST TRUE otherwise. | "Section 44 does not operate to alter the period of time ... if the period commenced before the commencement of this Act". |

## Worked cases for counting a period

The brief asks for seven cases.
Each is counted three ways, because s 44(1) has three forms: A, a period expressed to begin at, on or with a specified day (item 2, which includes that day); E, a period expressed to begin from the happening of an act or event on that day (item 3, which does not include the day); P, a period expressed to begin after a specified day (item 6, which does not include the day).
E and P count alike.
The last column applies s 44(2): if the last day is not a business day, the thing may be done on the next day that is.
Every answer is asserted in `sa-tests-time.l4`.

| Case | Form | First day counted | Last day of the period | Last day on which the thing may be done (no public holidays) | Text |
| --- | --- | --- | --- | --- | --- |
| three years from 2025-07-16 | A | 16 July 2025 | 15 July 2028 (a Saturday) | Monday 17 July 2028 | s 4 "year"; s 44(1) item 2; s 44(2) |
| three years from 2025-07-16 | E, P | 17 July 2025 | 16 July 2028 (a Sunday) | Monday 17 July 2028 | s 4 "year"; s 44(1) items 3, 6; s 44(2) |
| five years from 2025-01-15 | A | 15 January 2025 | 14 January 2030 (a Monday) | 14 January 2030 | s 44(1) item 2 |
| five years from 2025-01-15 | E, P | 16 January 2025 | 15 January 2030 (a Tuesday) | 15 January 2030 | s 44(1) items 3, 6 |
| five years from 2025-09-01 | A | 1 September 2025 | 31 August 2030 (a Saturday) | Monday 2 September 2030 | s 44(1) item 2; s 44(2) |
| five years from 2025-09-01 | E, P | 2 September 2025 | 1 September 2030 (a Sunday) | Monday 2 September 2030 | s 44(1) items 3, 6; s 44(2) |
| thirty days from 2026-01-01 | A | 1 January 2026 | 30 January 2026 (a Friday) | 30 January 2026 | s 44(1) item 2 |
| thirty days from 2026-01-01 | E, P | 2 January 2026 | 31 January 2026 (a Saturday) | Monday 2 February 2026 | s 44(1) items 3, 6; s 44(2) |
| two months from 2025-12-31 | A | 31 December 2025 | 28 February 2026 (a Saturday) | Monday 2 March 2026 | s 4 "month"; s 44(1) items 2, 8; s 44(2) |
| two months from 2025-12-31 | E, P | 1 January 2026 | 28 February 2026 (a Saturday) | Monday 2 March 2026 | s 44(1) items 3, 6, 8; s 44(2) |
| one month from 2024-01-31 | A | 31 January 2024 | 29 February 2024 (a Thursday) | 29 February 2024 | s 4 "month" |
| one month from 2024-01-31 | E, P | 1 February 2024 | 29 February 2024 (a Thursday) | 29 February 2024 | s 4 "month"; s 44(1) items 3, 6 |
| one year from 2024-02-29 | A | 29 February 2024 | 28 February 2025 (a Friday) | 28 February 2025 | s 4 "year" |
| one year from 2024-02-29 | E, P | 1 March 2024 | 28 February 2025 (a Friday) | 28 February 2025 | s 4 "year"; s 44(1) items 3, 6 |

A period of weeks, and a period expressed to begin "from a specified day", are answered NOTHING: the text does not say.

## What the Act turns out to say

Each statement ends "Asserted." where a case asserts it, and the sentence before names the file that holds the case.

1. A provision that comes into operation on a day does so at the beginning of that day, so it is in operation at the stroke of midnight that ends the day before. Cases in `sa-cases-seat.l4`, ss 28 and 30 cases; `sa-tests-time.l4`. Asserted.
2. A provision expressed to expire on a day continues to have effect until the end of that day, read here as excluding the instant of the midnight that ends it (F4). Cases in `sa-cases-seat.l4`. Asserted.
3. An Act with no commencement provision comes into operation on the day of assent, and a Bill reserved for Her Majesty's assent is taken to be assented to on the day the assent is notified by proclamation in the State. Cases in `sa-cases-seat.l4`. Asserted.
4. A later proclamation made before the day an earlier one fixed amends that day; one made on or after that day does not. Cases in `sa-cases-seat.l4`. Asserted.
5. A provision to be brought in by proclamation and not brought in sooner comes into operation on the second anniversary of assent, unless the provision says that s 27(6) does not apply; the text does not say what the second anniversary of 29 February is where the second year is not a leap year. Cases in `sa-cases-seat.l4`, `sa-tests-time.l4`. Asserted.
6. A period beginning at, on or with a specified day includes that day; a period beginning from the happening of an event, or after a specified day, does not. Cases in `sa-tests-time.l4`, cases 1 to 7. Asserted.
7. A calendar month that starts on a day with no corresponding day in the ending month ends at the end of the ending month. Cases in `sa-tests-time.l4`, cases 5 and 6. Asserted.
8. A year starting on 29 February ends at the end of 28 February in the next calendar year. Cases in `sa-tests-time.l4`, case 7. Asserted.
9. If the last day for doing a thing is not a business day, the thing may be done on the next business day, whether the period is counted in days, months or years. Cases in `sa-tests-time.l4`, cases 1 and 3 to 5. Asserted.
10. A part-day public holiday does not take the day out of the business days, and an exclusion of public holidays does not extend to one unless the Act or instrument expressly says so. Cases in `sa-tests-time.l4`, s 46 cases. Asserted.
11. A thing required to be done with no period provided or allowed must be done as soon as is reasonably practicable. Cases in `sa-tests-time.l4`, `sa-cases-seat.l4`. Asserted.
12. A person attains an age at the beginning of the anniversary of the date of birth; a person born on 29 February attains it at the beginning of 1 March in a year that is not a leap year. Cases in `sa-cases-seat.l4`, `sa-tests-time.l4`. Asserted.
13. An amount that is not an exact multiple of 5 cents is rounded down to the highest multiple of 5 cents below it. Cases in `sa-part7-references-distance-amounts.l4`, `sa-cases-seat.l4`. Asserted.
14. Service of a document by post is taken to be effected when it would be delivered in the ordinary course of post, unless the contrary is proved. Cases in `sa-cases-seat.l4`, `sa-tests-time.l4`. Asserted.
15. A document is posted to an address by properly addressing, prepaying and posting it as a letter. Cases in `sa-part8-documents.l4`, `sa-cases-seat.l4`. Asserted.
16. The repeal, amendment or expiry of an Act does not revive what was not in force, or affect rights, duties and penalties created or incurred under it. Cases in `sa-part4-repeal-and-amendment.l4`, `sa-cases-seat.l4`. Asserted.
17. An increased penalty applies only to offences committed after the increase takes effect, and a reduced penalty extends to earlier offences if the penalty is imposed after the reduction takes effect. Cases in `sa-part9-penalties-and-proceedings.l4`, `sa-cases-seat.l4`. Asserted.
18. Division 6 of the standard scale is a fine not exceeding $5 000, a term of imprisonment not exceeding 1 year, and an expiation fee of $315; the table has no Division 9 imprisonment. Cases in `sa-part9-standard-scales.l4`, `sa-cases-seat.l4`. Asserted.
19. An Act passed or instrument made after 20 June 1990 is taken to bind the Crown unless the contrary intention appears, but not so as to impose criminal liability. Cases in `sa-part3-general.l4`. Asserted.
20. The Governor's acts after 1 January 1873 are taken to be done with the advice and consent of the Executive Council. Cases in `sa-part3-general.l4`. Asserted.
21. Editorial notes and material under the heading "Legislative History" are not part of an Act or instrument. Cases in `sa-part3-general.l4`. Asserted.
22. A document may be served on an individual by delivery, by leaving or posting at the address the individual designated, at the last known residence or place of business if none was designated, or electronically in a manner designated or agreed. Cases in `sa-part8-documents.l4`, `sa-cases-seat.l4`. Asserted.
23. Persons required to be physically present for a meeting may satisfy the requirement remotely by audio visual means, audio, or both, unless the requirement is to witness a signing or take an oath, or the regulations prescribe the meeting. Cases in `sa-part6-functions-and-powers.l4`. Asserted.
24. A panel nominated for appointment must include at least 1 woman and 1 man; where the Act provides no panel, the entity must nominate not less than twice the number of members plus 1. Cases in `sa-part6-functions-and-powers.l4`. Asserted.
25. Each of the 91 terms of s 4 is an entry carrying the limbs the Act prints, with two tests for each. Cases in `sa-part2-standard-definitions.l4`. Asserted.

## What the text does not answer

- The meaning of "week", and so the last day of a period of weeks: NOTHING.
- How a period expressed to begin "from a specified day" is counted: NOTHING.
- The second anniversary of 29 February where the second year is not a leap year: NOTHING.
- The day on which s 27(6), s 19 or the Act itself commenced: the day is an input to the functions that need it.
- The legal time in the jurisdiction (s 45): the function answers only that the reference is to it.
- The public holidays of any year: always an input.
- How far from equal numbers a panel may be where equal numbers are not practicable: NOTHING.
- Whether a provision of the Health Practitioner Regulation National Law, the Criminal Procedure Act 1921 or another Act outside the sources applies: the borrowed fact is an input.

## Provision index and cross-references

`sa-provisions.l4` indexes 351 provisions.
`sa-xrefs.l4` holds 54 rows for references from one provision of this Act to another, and 35 rows for references to other Acts or instruments.
A script outside the folder finds them: it reads the text and picks out every printed reference such as "section N", "section N(n)", "subsection (n)", "subsection (n)(x)", "paragraph (x)", "this section", "this subsection", "that subsection", "this clause" and "the table" where a table is meant, resolves the provision each points at by rule, and writes one row per reference.
A reference to another Act is a row of its own kind carrying the instrument and provision as printed.
Each internal row has a test that the cited identifier is in the index and that the row's heading is the one the index gives.

## What the stable binary does not accept

- A constructor pattern with `WITH` (`WHEN `a number of days` WITH `how many days` THEN`) is a parse error; write the field name directly after the constructor.
- `IF NOT x OR y` parses as `NOT (x OR y)`; write `(NOT x) OR y`.
- A record literal written inside `LIST ... WITH ...` is not accepted; write `(Proclamation OF (Date d m y), (JUST (Date d m y)))`, each part in brackets.
- A type or function name with a hyphen, such as `Cross-reference`, parses as a subtraction unless it is in backticks.
- `length` is not defined; the count of a list is `count`.
- A one-line `CONSIDER` inside an `#ASSERT` is not accepted; a helper function is called instead.
- One question written as `DECIDE ... IF` with a body that began on the next line with a bracketed expression followed by `AT LEAST` was reported as a parse error at `AT LEAST`; its cause was not isolated, and the comparison now sits in a function of the time module.
- `Day` is overloaded in `daydate`, so `Day x` is ambiguous when the type of `x` is not yet known; a function with typed `GIVEN` is used for the comparison.
- `Date 29 2 2025` is 1 March 2025 (an impossible date rolls forward), and `Days in month` normalises a month beyond 12.
- This encoding does not use `REFUSE`, `YMD`, a section `GIVEN`, sets, `TYPICALLY` or an opaque `DECLARE`, which the brief says the stable binary rejects; it did not test each one.

## What check.sh prints

Command, run from the encoding folder: `L4=<the 1.6.98 binary> L4_MAIN=<the 1.6.110 binary> ./check.sh`.
Exit status 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sa-cases-seat.l4                               0        77       0        0         0 |      0        77       0        0  same
sa-interpretation-time.l4                      0         0       0        0         0 |      0         0       0        0  same
sa-nouns.l4                                    0         0       0        0         0 |      0         0       0        0  same
sa-part1-application.l4                        0        13       0        0         0 |      0        13       0        0  same
sa-part10-and-schedule1.l4                     0         9       0        0         0 |      0         9       0        0  same
sa-part2-health-table.l4                       0        33       0        0         0 |      0        33       0        0  same
sa-part2-reading-words.l4                      0        52       0        0         0 |      0        52       0        0  same
sa-part2-standard-definitions.l4               0       232       0        0         0 |      0       232       0        0  same
sa-part3-general.l4                            0        76       0        0         0 |      0        76       0        0  same
sa-part4-repeal-and-amendment.l4               0        46       0        0         0 |      0        46       0        0  same
sa-part5-citation.l4                           0        25       0        0         0 |      0        25       0        0  same
sa-part6-functions-and-powers.l4               0       115       0        0         0 |      0       115       0        0  same
sa-part7-references-distance-amounts.l4        0        17       0        0         0 |      0        17       0        0  same
sa-part8-documents.l4                          0        33       0        0         0 |      0        33       0        0  same
sa-part9-penalties-and-proceedings.l4          0        37       0        0         0 |      0        37       0        0  same
sa-part9-standard-scales.l4                    0        67       0        0         0 |      0        67       0        0  same
sa-provisions.l4                               0        16       0        0         0 |      0        16       0        0  same
sa-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
sa-tests-time.l4                               0       151       0        0         0 |      0       151       0        0  same
sa-xrefs.l4                                    0        91       0        0         0 |      0        91       0        0  same
TOTAL (20 modules)                             0      1090       0        0           |      0      1090       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `srcrefs.py check --strict` over all `sa-*.l4` files, against the text file, each printed:

```
srcrefs check: 550 src: lines, 319 runs, 319 locators, 0 problems
```

Every `.l4` file in the folder was also run on its own with `l4 run` on 1.6.98: no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` in any of them.
`l4 check` on each file printed none of the two messages that mark a misplaced `@ref` ("is at the end of the file", "follows code on its line").
No `@ref` sits before a `§` heading or an `#ASSERT`.
No name is defined in two files.

## What would need doing before this encoding is relied on

- A domain expert reads it against the authorised text of the Act. The deposited text is an unofficial rendering, and it omits the amendment history printed at the back of the published Act.
- The 29 forks above are ruled on, in particular F1 to F6 (counting a period and commencement), which decide the day a time limit ends.
- A list of public holidays is supplied for any date question that depends on a business day.
- The commencement days that s 27(6), s 19 and the Act refer to are supplied.
- The seat layer is deployed and its questions are read by a person in the seat.
- Provisions of other Acts that a rule borrows are encoded or supplied as facts.
