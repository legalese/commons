# NOTES.md (scja1): Supreme Court of Judicature Act 1969 (Singapore), lines 46 to 2309 of the plain-text rendering

Status (2026-11-05), and how each claim below was checked.
Every `.l4` file named here was written and run on main build 1.6.109; `check.sh` also ran every file on main build 1.6.108 and the counts agree (section "What check.sh prints").
`python3 -I srcrefs.py check --refs` and `check --strict` over the 22 `scja1-*.l4` files both print 0 problems (section "What check.sh prints" gives the numbers).
A script checked that every non-blank line of lines 46 to 2309 falls in some coverage row (section "Coverage (scja1)").
Nothing here was read by a lawyer, and nothing here was verified against the official text.

**The text is a plain-text rendering made by a converter script; it is not the official text.**
Edition: Supreme Court of Judicature Act 1969, 2020 Revised Edition, informal consolidation, "version in force from 1/7/2024" (`SCJA1969.txt` line 16).
Every `-- src:N` line in these files is a verbatim slice of line N of that rendering, copied by a script that reads the file.
**Where `PLAN.md` and the brief differ, the brief governs.**
The differences I met: `PLAN.md` says every module "begins with `scja-`", and the brief says `scja1-`, so the files are `scja1-*.l4`; the brief's file list names a keel file `scja-definitions.l4`, and `PLAN.md` says none was written (and none is in the folder), so section 2 is encoded here, in `scja1-part1-preliminary.l4`.

This file covers my ranges only: lines 46 to 2309 (the Arrangement of Sections, Part 1 ss 1-2, Part 2 ss 3-8A, Part 3 Divisions 1-9 ss 9-29E).
`scja2` has lines 2310 to 4320 and `scja3` lines 4321 to 7314; the lead merges the three files.
I did not write `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` or `README.md`.

## Files (scja1)

| file | what it holds |
| --- | --- |
| `scja1-part1-preliminary.l4`, `scja1-tests-part1-preliminary.l4` | s 2 (the definitions and their "unless the context otherwise requires" gate); s 1 is inert |
| `scja1-part2-court.l4`, `scja1-tests-part2-court.l4` | ss 3, 4, 5, 5A, 7; s 6 is inert |
| `scja1-part2-hearings.l4`, `scja1-tests-part2-hearings.l4` | ss 8 and 8A, with the regulative rule for s 8A(3) |
| `scja1-part3-div1.l4`, `scja1-tests-part3-div1.l4` | Division 1: ss 10 to 14 (ss 9 and 12 repealed) |
| `scja1-part3-div2-jurisdiction.l4`, `scja1-tests-part3-div2-jurisdiction.l4` | ss 15, 16, 17, 17A, and the hand-gathered `ss 16, 17 and 17A ...` function; regulative rule for s 17A(3) |
| `scja1-part3-div2-procedure.l4`, `scja1-tests-part3-div2-procedure.l4` | ss 17B, 17C, 18; regulative rules for s 17B(4) and s 17C(2) |
| `scja1-part3-div3-sicc.l4`, `scja1-tests-part3-div3-sicc.l4` | Division 3: ss 18A to 18M (s 18E repealed) |
| `scja1-part3-div4.l4`, `scja1-tests-part3-div4.l4` | Division 4: ss 19 to 22B; regulative rules for s 22A(4) and s 22B(2) |
| `scja1-part3-div5-6.l4`, `scja1-tests-part3-div5-6.l4` | Divisions 5 and 6: ss 23 to 28A (s 28B repealed); regulative rule for s 27(4) |
| `scja1-part3-div7-9.l4`, `scja1-tests-part3-div7-9.l4` | Divisions 7 to 9: ss 29 to 29E; regulative rules for s 29D(3) and s 29E(3) |
| `scja1-seat.l4`, `scja1-cases-seat.l4` | the seat layer (58 questions) and its cases |
| `sgia-interpretation-time.l4` | the Interpretation Act module, copied unchanged (section "Dependencies") |
| `scja-core.l4`, `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` | supplied; not mine, not edited |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file; my working log; the one thing I would hoist into the core |

The seat is a person who wishes to start, defend or appeal a civil case in the Singapore High Court or Court of Appeal.
There is no seat for officials.
Each of the 58 seat questions has `@export` and `@desc`, its name begins "Under section N,", and the questions are grouped under `§§` headings in the order of the text: s 8; s 8A; ss 10 to 14; ss 16, 17 and 17A; ss 17B and 17C; ss 18D to 18M; ss 20 to 22B; ss 24 to 28; ss 29 to 29E.
Every seat helper begins `scja1 seat`.
The seat answers are the layer-1 rule's own value: `MAYBE BOOLEAN` for 55 questions, `MAYBE Court` for s 29C, `MAYBE DATE` for s 29B(4)(b), and a `NUMBER` for s 10(1).
The helper `scja1 seat answer` (Yes, No, I am not sure) is how a person states a fact they are unsure of; an "I am not sure" reaches the rule as `NOTHING`; section "Seams (scja1)" says how the rules that depend on a Schedule treat it.

## Coverage (scja1)

One row per unit of lines 46 to 2309: the Arrangement of Sections, the long title, the date of enactment, every Part and Division heading, every section, subsection, paragraph and sub-paragraph, and every defined term.
Each row has exactly one disposition: `encoded`, `fork` (with the fork label; the register is the next section), `inert, reason 1` (not operative), `inert, reason 2` (machinery), or `repealed or blank in this text` (what the text shows is in the row).
There is no `out-of-scope` row and no `deferred` row.

How the table was built and audited (the two scripts are in my scratch work folder and are not shipped; the table is the record):
- `units.py` read the text and cut lines 46 to 2309 into 343 structural units (sections, subsections, paragraphs, sub-paragraphs, defined terms, headings) by their printed labels.
- `gen-coverage.py` joined each unit to the L4 names in the deposit (by the section label that begins every name), refused any unit with no name or reason, and wrote the table.
- The audit read the text for what the labels miss: terms defined inline in a paragraph (`third party proceedings`, `third party`, `subsequent party proceedings` and `subsequent party` in `s 18D(3)(c)` and `(d)`) got 4 further rows.
  Rows before the audit: 343; rows after: 347.
- A script then checked that all 1532 non-blank lines of lines 46 to 2309 fall inside some row, and 0 do not.

Counts by disposition (347 rows):

| disposition | rows |
| --- | --- |
| encoded | 200 |
| fork | 123 |
| inert, reason 1 | 15 |
| inert, reason 2 | 2 |
| repealed or blank in this text | 7 |
| total | 347 |

A paragraph or sub-paragraph row carries the name of the rule that holds it, written `within` that name; the rule's `-- src:` lines and `@ref` quote the text.
The last column names the seat question (`Under section N`) that asks the rule of a person, where there is one; the table does not say why a row has none.
Rows with reason 1 or 2 and the repealed rows are listed again in the final report.

| unit | lines | disposition | L4 name | module | seat question |
| --- | --- | --- | --- | --- | --- |
| arrangement of sections | 46-364 | inert, reason 1 | none | the Arrangement of Sections lists headings and creates no rule | |
| long title | 365-369 | inert, reason 1 | none | the long title states the Act's purpose and creates no rule | |
| date of enactment | 370-371 | inert, reason 1 | none | the date of enactment | |
| Part 1 heading | 372-373 | inert, reason 1 | none | a Part heading | |
| s 1 | 374-376 | inert, reason 2 | none | the short title: the Act's own name, which affects no one now | |
| s 2 | 377-378 | fork F1 | `s 2 the definitions of this section govern the word here` | scja1-part1-preliminary.l4 | |
| s 2 “Appellate Division” | 379-380 | encoded | `s 2 Appellate Division: the court is the Appellate Division of the High Court` | scja1-part1-preliminary.l4 | |
| s 2 “court” | 381-382 | fork K1 | `s 2 court: the court is the General Division, the Appellate Division or the Court of Appeal` | scja1-part1-preliminary.l4 | |
| s 2 “Family Division of the High Court” | 383-391 | encoded | `s 2 Family Division of the High Court: the court is the Family Division of the High Court` | scja1-part1-preliminary.l4 | |
| s 2 “Family Justice Rules” | 392-396 | encoded | `s 2 Family Justice Rules: the instrument is the Family Justice Rules` | scja1-part1-preliminary.l4 | |
| s 2 “General Division” | 397-399 | fork K1 | `s 2 General Division: the court is the General Division of the High Court` | scja1-part1-preliminary.l4 | |
| s 2 “Judge” | 400-403 | fork F2 | `s 2 Judge: the person is a Supreme Court Judge, a Judicial Commissioner, a Senior Judge or an International Judge` | scja1-part1-preliminary.l4 | |
| s 2 “Judge”(a) | 404-407 | fork F2 | `s 2 Judge (a): in relation to the General Division, the person is a Judge sitting in that Division` | scja1-part1-preliminary.l4 | |
| s 2 “Judge”(b) | 408-411 | fork F2 | `s 2 Judge (b): in relation to the Appellate Division, the person is a Judge sitting in that Division` | scja1-part1-preliminary.l4 | |
| s 2 “Judge”(c) | 412-415 | fork F2 | `s 2 Judge (c): in relation to the Court of Appeal, the person is a Judge sitting in that Court` | scja1-part1-preliminary.l4 | |
| s 2 “Registrar” | 416-418 | fork F3 | `s 2 Registrar: the officer is the Registrar, the Deputy Registrar or an Assistant Registrar` | scja1-part1-preliminary.l4 | |
| s 2 “Rules of Court” | 419-421 | fork F3 | `s 2 Rules of Court: the instrument is Rules of Court made under this Act or a form` | scja1-part1-preliminary.l4 | |
| s 2 “seal” | 422-423 | fork F3 | `s 2 seal: the thing is a seal or a stamp` | scja1-part1-preliminary.l4 | |
| s 2 “subordinate court” | 424-430 | fork F4 | `s 2 subordinate court: the court is a subordinate court` | scja1-part1-preliminary.l4 | |
| s 2 “Supreme Court Judge” | 431-441 | fork F2 | `s 2 Supreme Court Judge: the person is a Supreme Court Judge` | scja1-part1-preliminary.l4 | |
| Part 2 heading | 442-445 | inert, reason 1 | none | a Part heading | |
| s 3 | 446-453 | encoded | `s 3 superior court of record: the court is declared a superior court of record` | scja1-part2-court.l4 | |
| s 4 | 454-457 | fork K3 | `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(a) | 458-459 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(b) | 460-462 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(c) | 463-466 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(d) | 467-469 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(e) | 470-473 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 4(f) | 474-478 | fork K3 | within `s 4 the class of rank of the Judge, or 0 if s 4 does not rank the Judge`; `s 4 the first Judge ranks before the second`; `s 4 the most senior Supreme Court Judge among those sitting` | scja1-part2-court.l4 | |
| s 5(1) | 479-487 | encoded | `s 5(1) the powers and duties of the Chief Justice pass to the next Judge in precedence`; `s 5(1) the Judge who exercises the powers and duties of the Chief Justice` | scja1-part2-court.l4 | |
| s 5(2) | 488-495 | encoded | `s 5(2) the absence counts as absence from Singapore for s 5` | scja1-part2-court.l4 | |
| s 5A | 496-503 | encoded | `s 5A an International Judge may sit in this sitting` ; type `s 5A sitting` | scja1-part2-court.l4 | |
| s 6 | 504-511 | inert, reason 2 | none | the Court's seal, of a nature and pattern the Chief Justice prescribes by notification in the Gazette: office machinery | |
| s 7 | 512-518 | encoded | `s 7 the vacations specified for the year are within the limit` | scja1-part2-court.l4 | |
| s 8(1) | 519-524 | encoded | `s 8(1) the place is deemed an open and public court to which the public generally may have access` | scja1-part2-hearings.l4 | |
| s 8(2) | 525-534 | encoded | `s 8(2) the court has power to hear the matter or proceeding in private` ; type `s 8(2) ground` | scja1-part2-hearings.l4 | Under section 8(2) |
| s 8(2AA) | 535-540 | fork F5 | `s 8(2AA) the application is to be heard in private` | scja1-part2-hearings.l4 | |
| s 8(2AB) | 541-549 | fork F5 | `s 8(2AB) the court has power to hear the application otherwise than in private` | scja1-part2-hearings.l4 | |
| s 8(2AB)(a) | 550-553 | fork F5 | within `s 8(2AB) the court has power to hear the application otherwise than in private` | scja1-part2-hearings.l4 | |
| s 8(2AB)(b) | 554-559 | fork F5 | within `s 8(2AB) the court has power to hear the application otherwise than in private` | scja1-part2-hearings.l4 | |
| s 8(2A) | 560-565 | encoded | `s 8(2A) the court has power to order the thing removed or sufficiently redacted` ; type `s 8(2A) thing in a court document` | scja1-part2-hearings.l4 | |
| s 8(2A)(a) | 566-569 | encoded | within `s 8(2A) the court has power to order the thing removed or sufficiently redacted` ; type `s 8(2A) thing in a court document` | scja1-part2-hearings.l4 | |
| s 8(2A)(b) | 570-575 | encoded | within `s 8(2A) the court has power to order the thing removed or sufficiently redacted` ; type `s 8(2A) thing in a court document` | scja1-part2-hearings.l4 | |
| s 8(2A)(c) | 576-585 | encoded | within `s 8(2A) the court has power to order the thing removed or sufficiently redacted` ; type `s 8(2A) thing in a court document` | scja1-part2-hearings.l4 | |
| s 8(3) | 586-587 | encoded | `s 8(3) the court may order that no person is to do the act` ; type `s 8(3) act the order may forbid` | scja1-part2-hearings.l4 | |
| s 8(3)(a) | 588-595 | encoded | within `s 8(3) the court may order that no person is to do the act` ; type `s 8(3) act the order may forbid` | scja1-part2-hearings.l4 | |
| s 8(3)(b) | 596-607 | encoded | within `s 8(3) the court may order that no person is to do the act` ; type `s 8(3) act the order may forbid` | scja1-part2-hearings.l4 | |
| s 8(3)(c) | 608-614 | encoded | within `s 8(3) the court may order that no person is to do the act` ; type `s 8(3) act the order may forbid` | scja1-part2-hearings.l4 | |
| s 8(4) | 615-621 | fork F13, F19 | `s 8(4) the highest fine`; `s 8(4) the longest imprisonment, in years`; `s 8(4) the person is guilty of an offence`; `s 8(4) the sentence is within what the person is liable to on conviction` | scja1-part2-hearings.l4 | |
| s 8(5) | 622-626 | encoded | `s 8(5) the court may permit the individual to be present in the courtroom` ; type `s 8(5) individual` | scja1-part2-hearings.l4 | Under section 8(5) |
| s 8(5)(a) | 627-629 | encoded | `s 8(5)(a) the individual is a journalist who reports news for a newspaper or a broadcasting service` | scja1-part2-hearings.l4 | |
| s 8(5)(b) | 630-632 | encoded | within `s 8(5) the court may permit the individual to be present in the courtroom` ; type `s 8(5) individual` | scja1-part2-hearings.l4 | Under section 8(5) |
| s 8(5)(c) | 633-639 | encoded | within `s 8(5) the court may permit the individual to be present in the courtroom` ; type `s 8(5) individual` | scja1-part2-hearings.l4 | Under section 8(5) |
| s 8(6) | 640-646 | encoded | `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(6)(a) | 647-650 | encoded | within `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(6)(b) | 651-659 | encoded | within `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(6)(c) | 660-663 | encoded | within `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(6)(d) | 664-668 | encoded | within `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(6)(e) | 669-676 | encoded | within `s 8(6) the court may consider the matter in deciding whether to hear in private` ; type `s 8(6) matter` | scja1-part2-hearings.l4 | |
| s 8(7) | 677-678 | encoded | `s 8(7) broadcasting service: it has the meaning given by section 2(1) of the Broadcasting Act 1994`; `s 8(7) newspaper: it has the meaning given by section 2(1) of the Newspaper and Printing Presses Act 1974` | scja1-part2-hearings.l4 | |
| s 8(7) “broadcasting service” | 679-681 | encoded | `s 8(7) broadcasting service: it has the meaning given by section 2(1) of the Broadcasting Act 1994` | scja1-part2-hearings.l4 | |
| s 8(7) “newspaper” | 682-687 | encoded | `s 8(7) newspaper: it has the meaning given by section 2(1) of the Newspaper and Printing Presses Act 1974` | scja1-part2-hearings.l4 | |
| s 8A(1) | 688-699 | fork F6 | `s 8A(1) the court may conduct the hearing of the matter through the means` | scja1-part2-hearings.l4 | Under section 8A(1) |
| s 8A(2) | 700-713 | encoded | `s 8A(2) section 8A(1) affects the operation of the provision` | scja1-part2-hearings.l4 | |
| s 8A(3) | 714-717 | fork F15 | `s 8A(3) the court must not conduct this part of the hearing through a live audio link only`; `s 8A(3) the court shall not conduct the part through a live audio link only` | scja1-part2-hearings.l4 | Under section 8A(3) |
| s 8A(3)(a) | 718-720 | fork F15 | `s 8A(3)(a) a criminal proceeding where oral evidence is given` | scja1-part2-hearings.l4 | |
| s 8A(3)(b) | 721-724 | fork F15 | `s 8A(3)(b) a civil proceeding where oral evidence is given and the parties do not all consent` | scja1-part2-hearings.l4 | |
| s 8A(3)(c) | 725-729 | fork F15 | within `s 8A(3) the court must not conduct this part of the hearing through a live audio link only`; `s 8A(3) the court shall not conduct the part through a live audio link only` | scja1-part2-hearings.l4 | Under section 8A(3) |
| s 8A(4) | 730-739 | encoded | `s 8A(4) the court is considered to have conducted the part through a live audio link only` | scja1-part2-hearings.l4 | |
| s 8A(5) | 740-746 | encoded | `s 8A(5) the court must not conduct the hearing in the manner provided under section 8A(1)` | scja1-part2-hearings.l4 | Under section 8A(5) |
| s 8A(6) | 747-754 | encoded | `s 8A(6) the court is deemed to be sitting at the appointed place` | scja1-part2-hearings.l4 | |
| Part 3 heading | 755-764 | inert, reason 1 | none | a Part heading | |
| Division 1 heading | 765-766 | inert, reason 1 | none | a Division heading | |
| s 9 | 767-768 | repealed or blank in this text | none | the text shows: "9. [Repealed by Act 40 of 2019]" | |
| s 10(1) | 769-778 | encoded | `s 10(1) the number of Judges before whom the proceeding is heard and disposed of` | scja1-part3-div1.l4 | Under section 10(1) |
| s 10(1A) | 779-786 | fork F17 | `s 10(1A) the Chief Justice may direct that the proceeding be heard before this number of Judges` | scja1-part3-div1.l4 | Under section 10(1A) |
| s 10(1B) | 787-792 | encoded | `s 10(1B) how a proceeding before 3 or more Judges is decided` ; type `s 10(1B) decision` | scja1-part3-div1.l4 | |
| s 10(2) | 793-803 | encoded | `s 10(2) a Judge may exercise the jurisdiction of the General Division in the cause, matter or proceeding` | scja1-part3-div1.l4 | Under section 10(2) |
| s 10(3) | 804-805 | repealed or blank in this text | none | the text shows: "(3) [Deleted by Act 42 of 2014]" | |
| s 10(4) | 806-816 | encoded | `s 10(4) the Judge has power to deliver judgment despite the expiry or termination of the appointment` | scja1-part3-div1.l4 | |
| s 10(5) | 817-820 | fork F15 | `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10(5)(a) | 821-824 | fork F15 | within `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10(5)(b) | 825-829 | fork F15 | within `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10(5)(c) | 830-834 | fork F15 | within `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10(5)(d) | 835-840 | fork F15 | within `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10(5)(e) | 841-849 | fork F15 | within `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding`; `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` ; type `s 10(5) proceeding` | scja1-part3-div1.l4 | |
| s 10A(1) | 850-860 | fork K1 | within `s 10A the court may summon assessors` | scja1-part3-div1.l4 | Under section 10A |
| s 10A(2) | 861-873 | fork K1 | `s 10A(2) the remuneration of the assessors is costs in the proceedings` | scja1-part3-div1.l4 | |
| s 10A(3) | 874-878 | encoded | `s 10A(3) the remuneration of the assessors is payable out of moneys provided by Parliament` | scja1-part3-div1.l4 | |
| s 10A(4) | 879-882 | encoded | `s 10A(4) a party may take objection to the proposed assessor` | scja1-part3-div1.l4 | Under section 10A(4) |
| s 10B(1) | 883-890 | fork F18 | `s 10B(1) the General Division is to sit on the day` | scja1-part3-div1.l4 | Under section 10B(1) |
| s 10B(2) | 891-894 | fork F18 | `s 10B(2) the Judge may lawfully sit on the day` | scja1-part3-div1.l4 | Under section 10B(2) |
| s 10B(2)(a) | 895-897 | fork F18 | within `s 10B(2) the Judge may lawfully sit on the day` | scja1-part3-div1.l4 | Under section 10B(2) |
| s 10B(2)(b) | 898-902 | fork F18 | within `s 10B(2) the Judge may lawfully sit on the day` | scja1-part3-div1.l4 | Under section 10B(2) |
| s 11(1) | 903-909 | encoded | `s 11(1) the General Division sits at the time and place` | scja1-part3-div1.l4 | |
| s 11(2) | 910-913 | fork F7 | `s 11(2) the distribution of business among the Judges is as the Act requires` | scja1-part3-div1.l4 | |
| s 12 | 914-920 | repealed or blank in this text | none | the text shows: "12. [Repealed by Act 40 of 2019]" | |
| s 13 | 921-927 | encoded | `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 13(a) | 928-933 | encoded | within `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 13(b) | 934-939 | encoded | within `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 13(c) | 940-941 | encoded | within `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 13(d) | 942-944 | encoded | within `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 13(e) | 945-953 | encoded | within `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` ; type `s 13 property` | scja1-part3-div1.l4 | Under section 13 |
| s 14(1) | 954-957 | encoded | `s 14(1) the interested party may prepare the instrument and tender it to the court for execution`; `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4 | Under section 14(1) |
| s 14(1)(a) | 958-961 | encoded | within `s 14(1) the interested party may prepare the instrument and tender it to the court for execution`; `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4 | Under section 14(1) |
| s 14(1)(b) | 962-972 | encoded | within `s 14(1) the interested party may prepare the instrument and tender it to the court for execution`; `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4 | Under section 14(1) |
| s 14(1)(c) | 973-976 | encoded | within `s 14(1) the interested party may prepare the instrument and tender it to the court for execution`; `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4 | Under section 14(1) |
| s 14(1)(d) | 977-983 | encoded | within `s 14(1) the interested party may prepare the instrument and tender it to the court for execution`; `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4 | Under section 14(1) |
| s 14(2) | 984-987 | encoded | `s 14(2) section 14 abridges the court's power to proceed by attachment against the person` | scja1-part3-div1.l4 | |
| Division 2 heading | 988-991 | inert, reason 1 | none | a Division heading | |
| s 15(1) | 992-996 | encoded | `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(a) | 997-998 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(b) | 999-1000 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(c) | 1001-1003 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(d) | 1004-1006 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(e) | 1007-1012 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(1)(f) | 1013-1017 | encoded | within `s 15(1) the General Division has jurisdiction to try the offence` ; type `s 15(1) offence` | scja1-part3-div2-jurisdiction.l4 | |
| s 15(2) | 1018-1026 | encoded | `s 15(2) the General Division may pass the sentence` | scja1-part3-div2-jurisdiction.l4 | |
| s 16(1) | 1027-1031 | fork F9 | `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4 | Under section 16(1) |
| s 16(1)(a) | 1032-1034 | fork F9 | within `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4 | Under section 16(1) |
| s 16(1)(a)(i) | 1035-1037 | fork F9 | within `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4 | Under section 16(1) |
| s 16(1)(a)(ii) | 1038-1043 | fork F9 | within `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4 | Under section 16(1) |
| s 16(1)(b) | 1044-1048 | fork F9 | within `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4 | Under section 16(1) |
| s 16(2) | 1049-1053 | fork F9 | `s 16(2) the General Division has the jurisdiction vested in it by another written law` | scja1-part3-div2-jurisdiction.l4 | |
| s 17(1) | 1054-1058 | fork F9 | `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(a) | 1059-1061 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(b) | 1062-1064 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(c) | 1065-1067 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(d) | 1068-1070 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(e) | 1071-1079 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(f) | 1080-1083 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(g) | 1084-1088 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(1)(h) | 1089-1094 | fork F9 | within `s 17(1) the civil jurisdiction of the General Division includes the subject` | scja1-part3-div2-jurisdiction.l4 | Under section 17(1) |
| s 17(2) | 1095-1096 | encoded | `s 17(2) international settlement agreement: it has the meaning given by section 2(1) of the Singapore Convention on Mediation Act 2020`; `s 17(2) mediated settlement agreement: it has the meaning given by the Mediation Act 2017`; `s 17(2) mediation: it has the meaning given by the Mediation Act 2017` | scja1-part3-div2-jurisdiction.l4 | |
| s 17(2) “international settlement agreement” | 1097-1105 | encoded | `s 17(2) international settlement agreement: it has the meaning given by section 2(1) of the Singapore Convention on Mediation Act 2020` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(1) | 1106-1117 | fork F15 | `s 17A(1) the General Division has no jurisdiction to hear and try the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | Under section 17A(1) |
| s 17A(2) | 1118-1123 | fork F9 | `s 17A(2) the General Division has the jurisdiction vested in it by written law over the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(2)(a) | 1124-1125 | fork F9 | within `s 17A(2) the General Division has the jurisdiction vested in it by written law over the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(2)(b) | 1126-1132 | fork F9 | within `s 17A(2) the General Division has the jurisdiction vested in it by written law over the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(2)(c) | 1133-1136 | fork F9 | within `s 17A(2) the General Division has the jurisdiction vested in it by written law over the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(3) | 1137-1142 | fork F8 | `s 17A(3) the General Division is to stay the civil proceedings`; `s 17A(3) the General Division must stay the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | Under section 17A(3) |
| s 17A(3)(a) | 1143-1152 | fork F8 | `s 17A(3)(a) a Syariah Court divorce event precedes or coincides with the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(3)(b) | 1153-1164 | fork F8 | `s 17A(3)(b) a Syariah Court divorce event follows the commencement of the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(3A) | 1165-1172 | encoded | `s 17A(3A) the registration of the divorce counts for section 17A(3)` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(4) | 1173-1186 | encoded | `s 17A(4) the Syariah Court proceedings are deemed to have been commenced before the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(5) | 1187-1195 | fork F8 | `s 17A(3) the General Division is to stay the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | Under section 17A(3) |
| s 17A(6) | 1196-1203 | fork F8 | `s 17A(3) the General Division is to stay the civil proceedings` | scja1-part3-div2-jurisdiction.l4 | Under section 17A(3) |
| s 17A(7) | 1204-1208 | encoded | `s 17A(7) the General Division applies the civil law` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(8) | 1209-1214 | encoded | `s 17A(8) section 112 of the Women's Charter 1961 applies to the General Division in the proceeding` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(9) | 1215-1216 | encoded | `s 17A(9) Syariah Court: the court is the Syariah Court constituted under the Administration of Muslim Law Act 1966`; `s 17A(9) Syariah Court commencement certificate: it is a commencement certificate issued by the Syariah Court under section 35A(4)`; `s 17A(9) Syariah Court continuation certificate: it is a continuation certificate issued by the Syariah Court under section 35A(4)` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(9) “Syariah Court” | 1217-1219 | encoded | `s 17A(9) Syariah Court: the court is the Syariah Court constituted under the Administration of Muslim Law Act 1966` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(9) “Syariah Court commencement certificate” | 1220-1224 | encoded | `s 17A(9) Syariah Court commencement certificate: it is a commencement certificate issued by the Syariah Court under section 35A(4)` | scja1-part3-div2-jurisdiction.l4 | |
| s 17A(9) “Syariah Court continuation certificate” | 1225-1233 | encoded | `s 17A(9) Syariah Court continuation certificate: it is a continuation certificate issued by the Syariah Court under section 35A(4)` | scja1-part3-div2-jurisdiction.l4 | |
| s 17B(1) | 1234-1240 | fork F6 | `s 17B(1) the General Division may decide the matter without hearing oral arguments` | scja1-part3-div2-procedure.l4 | Under section 17B(1) |
| s 17B(2) | 1241-1244 | fork F16 | `s 17B(2) section 17B(1) allows this part of the proceeding to be conducted without an oral hearing` | scja1-part3-div2-procedure.l4 | Under section 17B(2) |
| s 17B(3) | 1245-1250 | encoded | `s 17B(3) the General Division may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` | scja1-part3-div2-procedure.l4 | Under section 17B(3) |
| s 17B(4) | 1251-1254 | encoded | `s 17B(4) the General Division must not hear the matter in an asynchronous manner`; `s 17B(4) the General Division shall not hear the matter in an asynchronous manner` | scja1-part3-div2-procedure.l4 | Under section 17B(4) |
| s 17B(5) | 1255-1260 | encoded | `s 17B(5) section 17B affects the General Division's power to hear oral arguments before deciding the matter` | scja1-part3-div2-procedure.l4 | |
| s 17C(1) | 1261-1267 | encoded | `s 17C(1) a Judge sitting in the General Division may on his or her own motion summarily dismiss the appeal` | scja1-part3-div2-procedure.l4 | Under section 17C(1) |
| s 17C(1)(a) | 1268-1272 | encoded | within `s 17C(1) a Judge sitting in the General Division may on his or her own motion summarily dismiss the appeal` | scja1-part3-div2-procedure.l4 | Under section 17C(1) |
| s 17C(1)(b) | 1273-1275 | encoded | within `s 17C(1) a Judge sitting in the General Division may on his or her own motion summarily dismiss the appeal` | scja1-part3-div2-procedure.l4 | Under section 17C(1) |
| s 17C(2) | 1276-1283 | fork F7 | `s 17C(2) the Judge may summarily dismiss the appeal under section 17C(1) now, as the section requires`; `s 17C(2) the Judge must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div2-procedure.l4 | Under section 17C(2) |
| s 17C(2)(a) | 1284-1286 | fork F7 | within `s 17C(2) the Judge may summarily dismiss the appeal under section 17C(1) now, as the section requires`; `s 17C(2) the Judge must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div2-procedure.l4 | Under section 17C(2) |
| s 17C(2)(b) | 1287-1288 | fork F7 | within `s 17C(2) the Judge may summarily dismiss the appeal under section 17C(1) now, as the section requires`; `s 17C(2) the Judge must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div2-procedure.l4 | Under section 17C(2) |
| s 17C(3) | 1289-1292 | fork F3 | `s 17C(3) the thing is an appeal for the purposes of section 17C` | scja1-part3-div2-procedure.l4 | |
| s 18(1) | 1293-1299 | encoded | `s 18(1) the General Division has the power vested in it by a written law` | scja1-part3-div2-procedure.l4 | |
| s 18(2) | 1300-1304 | encoded | `s 18(2) the General Division has the power set out in the First Schedule` | scja1-part3-div2-procedure.l4 | |
| s 18(3) | 1305-1310 | encoded | `s 18(3) the power is to be exercised in accordance with the written law, Rules of Court or Family Justice Rules relating to it` | scja1-part3-div2-procedure.l4 | |
| Division 3 heading | 1311-1314 | inert, reason 1 | none | a Division heading | |
| s 18A | 1315-1321 | encoded | `s 18A the court is the division of the General Division known as the Singapore International Commercial Court` | scja1-part3-div3-sicc.l4 | |
| s 18B(1) | 1322-1330 | fork F17 | `s 18B(1) the Chief Justice may appoint the Judge to be the President of the Singapore International Commercial Court` | scja1-part3-div3-sicc.l4 | |
| s 18B(2) | 1331-1341 | encoded | `s 18B(2) the Chief Justice is the President of the Singapore International Commercial Court` | scja1-part3-div3-sicc.l4 | |
| s 18C | 1342-1350 | encoded | `s 18C the provision of the Act applies to proceedings in the Singapore International Commercial Court as to the General Division in its original civil jurisdiction` | scja1-part3-div3-sicc.l4 | |
| s 18D(1) | 1351-1356 | encoded | `s 18D(1) the Singapore International Commercial Court has jurisdiction to hear and try the action` | scja1-part3-div3-sicc.l4 | Under section 18D(1) |
| s 18D(1)(a) | 1357-1358 | encoded | within `s 18D(1) the Singapore International Commercial Court has jurisdiction to hear and try the action` | scja1-part3-div3-sicc.l4 | Under section 18D(1) |
| s 18D(1)(b) | 1359-1361 | encoded | within `s 18D(1) the Singapore International Commercial Court has jurisdiction to hear and try the action` | scja1-part3-div3-sicc.l4 | Under section 18D(1) |
| s 18D(1)(c) | 1362-1366 | encoded | within `s 18D(1) the Singapore International Commercial Court has jurisdiction to hear and try the action` | scja1-part3-div3-sicc.l4 | Under section 18D(1) |
| s 18D(2) | 1367-1370 | encoded | within `s 18D(2)(a) the Singapore International Commercial Court has jurisdiction to hear the proceedings relating to international commercial arbitration`; `s 18D(2)(b) the Singapore International Commercial Court has jurisdiction to hear the application`; `s 18D(2)(c) the Singapore International Commercial Court has jurisdiction to hear the corporate insolvency, restructuring or dissolution proceedings`; `s 18D(2)(c) the version of the Companies Act 1967 is one in force before 30 July 2020` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(a) | 1371-1377 | encoded | `s 18D(2)(a) the Singapore International Commercial Court has jurisdiction to hear the proceedings relating to international commercial arbitration` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(b) | 1378-1379 | encoded | `s 18D(2)(b) the Singapore International Commercial Court has jurisdiction to hear the application` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(b)(i) | 1380-1382 | encoded | within `s 18D(2)(b) the Singapore International Commercial Court has jurisdiction to hear the application` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(b)(ii) | 1383-1390 | encoded | within `s 18D(2)(b) the Singapore International Commercial Court has jurisdiction to hear the application` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(c) | 1391-1403 | encoded | `s 18D(2)(c) the Singapore International Commercial Court has jurisdiction to hear the corporate insolvency, restructuring or dissolution proceedings`; `s 18D(2)(c) the version of the Companies Act 1967 is one in force before 30 July 2020` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(c)(i) | 1404-1405 | encoded | within `s 18D(2)(c) the Singapore International Commercial Court has jurisdiction to hear the corporate insolvency, restructuring or dissolution proceedings`; `s 18D(2)(c) the version of the Companies Act 1967 is one in force before 30 July 2020` | scja1-part3-div3-sicc.l4 | |
| s 18D(2)(c)(ii) | 1406-1414 | encoded | within `s 18D(2)(c) the Singapore International Commercial Court has jurisdiction to hear the corporate insolvency, restructuring or dissolution proceedings`; `s 18D(2)(c) the version of the Companies Act 1967 is one in force before 30 July 2020` | scja1-part3-div3-sicc.l4 | |
| s 18D(3) | 1415-1418 | encoded | `s 18D(3) the jurisdiction under section 18D(1) includes the further jurisdiction in this subsection` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(a) | 1419-1424 | encoded | `s 18D(3)(a) the jurisdiction includes hearing and trying the action upon the joinder of an additional party` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(b) | 1425-1430 | encoded | `s 18D(3)(b) the jurisdiction includes hearing and trying the counterclaim` | scja1-part3-div3-sicc.l4 | Under section 18D(3)(b) |
| s 18D(3)(c) | 1431-1436 | encoded | `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(c)(i) | 1437-1440 | encoded | within `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(c)(ii) | 1441-1450 | encoded | within `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(d) | 1451-1457 | encoded | `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(d)(i) | 1458-1461 | encoded | within `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(d)(ii) | 1462-1470 | encoded | within `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` | scja1-part3-div3-sicc.l4 | |
| s 18D(4) | 1471-1478 | encoded | `s 18D(4) the jurisdiction includes hearing and trying the proceedings brought by a subsequent party` | scja1-part3-div3-sicc.l4 | |
| s 18E | 1479-1480 | repealed or blank in this text | none | the text shows: "18E. [Repealed by Act 1 of 2018]" | |
| s 18F(1) | 1481-1486 | encoded | `s 18F(1) the parties are considered to have agreed to the term` ; type `s 18F(1) agreed term` | scja1-part3-div3-sicc.l4 | Under section 18F(1) |
| s 18F(1)(a) | 1487-1489 | encoded | within `s 18F(1) the parties are considered to have agreed to the term` ; type `s 18F(1) agreed term` | scja1-part3-div3-sicc.l4 | Under section 18F(1) |
| s 18F(1)(b) | 1490-1492 | encoded | within `s 18F(1) the parties are considered to have agreed to the term` ; type `s 18F(1) agreed term` | scja1-part3-div3-sicc.l4 | Under section 18F(1) |
| s 18F(1)(c) | 1493-1506 | encoded | within `s 18F(1) the parties are considered to have agreed to the term` ; type `s 18F(1) agreed term` | scja1-part3-div3-sicc.l4 | Under section 18F(1) |
| s 18F(2) | 1507-1511 | encoded | `s 18F(1) the parties are considered to have agreed to the term` | scja1-part3-div3-sicc.l4 | Under section 18F(1) |
| s 18G | 1512-1518 | fork F7, F17 | `s 18G the proceeding is to be heard and disposed of before this number of Judges, as the section requires` | scja1-part3-div3-sicc.l4 | |
| s 18H(1) | 1519-1526 | encoded | `s 18H(1) section 18H applies to the case` | scja1-part3-div3-sicc.l4 | |
| s 18H(2) | 1527-1530 | fork F7 | `s 18H(2) the presiding Judge was appointed by the Chief Justice, as the section requires` | scja1-part3-div3-sicc.l4 | |
| s 18H(3) | 1531-1535 | encoded | `s 18H(3) how the case is decided` ; type `s 18H(3) decision` | scja1-part3-div3-sicc.l4 | |
| s 18H(4) | 1536-1540 | encoded | `s 18H(4) the case is to be reheard` | scja1-part3-div3-sicc.l4 | |
| s 18H(5) | 1541-1546 | encoded | `s 18H(5) the remaining 2 Judges may continue to hear and determine the case` | scja1-part3-div3-sicc.l4 | |
| s 18H(6) | 1547-1548 | encoded | `s 18H(6) this subsection applies to the case`; `s 18H(6) how the case heard by 2 Judges is determined` ; type `s 18H(6) outcome` | scja1-part3-div3-sicc.l4 | |
| s 18H(6)(a) | 1549-1551 | encoded | within `s 18H(6) this subsection applies to the case`; `s 18H(6) how the case heard by 2 Judges is determined` ; type `s 18H(6) outcome` | scja1-part3-div3-sicc.l4 | |
| s 18H(6)(b) | 1552-1563 | encoded | within `s 18H(6) this subsection applies to the case`; `s 18H(6) how the case heard by 2 Judges is determined` ; type `s 18H(6) outcome` | scja1-part3-div3-sicc.l4 | |
| s 18I(1) | 1564-1569 | encoded | `s 18I(1) the Singapore International Commercial Court may exercise the power` | scja1-part3-div3-sicc.l4 | |
| s 18I(1)(a) | 1570-1571 | encoded | within `s 18I(1) the Singapore International Commercial Court may exercise the power` | scja1-part3-div3-sicc.l4 | |
| s 18I(1)(b) | 1572-1576 | encoded | within `s 18I(1) the Singapore International Commercial Court may exercise the power` | scja1-part3-div3-sicc.l4 | |
| s 18I(2) | 1577-1582 | fork F7 | `s 18I(2) the Singapore International Commercial Court exercises the power as the Act requires` | scja1-part3-div3-sicc.l4 | |
| s 18J(1) | 1583-1590 | encoded | `s 18J(1) the Singapore International Commercial Court may transfer the case to the General Division` | scja1-part3-div3-sicc.l4 | Under section 18J(1) |
| s 18J(2) | 1591-1596 | encoded | `s 18J(2) the General Division may transfer the case to the Singapore International Commercial Court` | scja1-part3-div3-sicc.l4 | Under section 18J(2) |
| s 18J(3) | 1597-1598 | encoded | within `s 18J(3)(a) the court to which the case is transferred may permit a matter that has been adduced to remain in evidence`; `s 18J(3)(b) the courts may make the consequential order` | scja1-part3-div3-sicc.l4 | |
| s 18J(3)(a) | 1599-1603 | encoded | `s 18J(3)(a) the court to which the case is transferred may permit a matter that has been adduced to remain in evidence` | scja1-part3-div3-sicc.l4 | |
| s 18J(3)(b) | 1604-1609 | encoded | `s 18J(3)(b) the courts may make the consequential order` | scja1-part3-div3-sicc.l4 | |
| s 18J(4) | 1610-1619 | fork K1 | `s 18J(4) the court is the General Division for the purposes of section 18J` | scja1-part3-div3-sicc.l4 | |
| s 18K(1) | 1620-1623 | encoded | within `s 18K(1)(a) the Singapore International Commercial Court is not bound to apply the rule of evidence under Singapore law`; `s 18K(1)(b) the Singapore International Commercial Court may apply other rules of evidence` | scja1-part3-div3-sicc.l4 | |
| s 18K(1)(a) | 1624-1627 | encoded | `s 18K(1)(a) the Singapore International Commercial Court is not bound to apply the rule of evidence under Singapore law` | scja1-part3-div3-sicc.l4 | |
| s 18K(1)(b) | 1628-1633 | encoded | `s 18K(1)(b) the Singapore International Commercial Court may apply other rules of evidence` | scja1-part3-div3-sicc.l4 | |
| s 18K(2) | 1634-1638 | fork F3 | `s 18K(2) the rule is a rule of evidence for the purposes of section 18K(1)` | scja1-part3-div3-sicc.l4 | |
| s 18L(1) | 1639-1647 | encoded | `s 18L(1) the Singapore International Commercial Court may order the question of foreign law determined on the basis of submissions instead of proof` | scja1-part3-div3-sicc.l4 | |
| s 18L(2) | 1648-1653 | encoded | `s 18L(2) the Singapore International Commercial Court may have regard to the matter in determining foreign law on submissions` | scja1-part3-div3-sicc.l4 | |
| s 18M | 1654-1663 | fork F17 | `s 18M the party may be represented by the foreign lawyer or law expert` | scja1-part3-div3-sicc.l4 | Under section 18M |
| Division 4 heading | 1664-1672 | inert, reason 1 | none | a Division heading | |
| s 19 | 1673-1677 | fork F10 | `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 19(a) | 1678-1682 | fork F10 | within `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 19(b) | 1683-1687 | fork F10 | within `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 19(ba) | 1688-1692 | fork F10 | within `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 19(c) | 1693-1695 | fork F10 | within `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 19(d) | 1696-1699 | fork F10 | within `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` ; type `s 19 matter` | scja1-part3-div4.l4 | |
| s 20 | 1700-1704 | fork F10 | `s 20 the appellate civil jurisdiction of the General Division consists of hearing the appeal` | scja1-part3-div4.l4 | Under section 20 |
| s 20(a) | 1705-1707 | fork F10 | within `s 20 the appellate civil jurisdiction of the General Division consists of hearing the appeal` | scja1-part3-div4.l4 | Under section 20 |
| s 20(b) | 1708-1711 | fork F10 | within `s 20 the appellate civil jurisdiction of the General Division consists of hearing the appeal` | scja1-part3-div4.l4 | Under section 20 |
| s 20(c) | 1712-1716 | fork F10 | within `s 20 the appellate civil jurisdiction of the General Division consists of hearing the appeal` | scja1-part3-div4.l4 | Under section 20 |
| s 21(1) | 1717-1730 | fork K2, F14 | `s 21(1) an appeal lies to the General Division from the decision`; `s 21(1) permission is needed to appeal from the decision` | scja1-part3-div4.l4 | Under section 21(1) |
| s 21(1)(a) | 1731-1736 | fork K2, F14 | `s 21(1)(a) the amount in dispute or the value of the subject matter does not exceed the sum` | scja1-part3-div4.l4 | |
| s 21(1)(b) | 1737-1742 | fork K2, F14 | within `s 21(1) an appeal lies to the General Division from the decision`; `s 21(1) permission is needed to appeal from the decision` | scja1-part3-div4.l4 | Under section 21(1) |
| s 21(2) | 1743-1744 | repealed or blank in this text | none | the text shows: "(2) [Deleted by Act 25 of 2021 wef 01/04/2022]" | |
| s 21(2A) | 1745-1751 | encoded | `s 21(2A) the order is final` | scja1-part3-div4.l4 | Under section 21(2A) |
| s 21(2B) | 1752-1753 | repealed or blank in this text | none | the text shows: "(2B) [Deleted by Act 40 of 2019]" | |
| s 21(3) | 1754-1756 | encoded | `s 21(3) the President may vary the amount mentioned in section 21(1)` | scja1-part3-div4.l4 | |
| s 22(1) | 1757-1763 | encoded | `s 22(1) the appeal is by way of rehearing` | scja1-part3-div4.l4 | Under section 22(1) |
| s 22(2) | 1764-1769 | encoded | `s 22(2) the General Division has the power or duty` | scja1-part3-div4.l4 | |
| s 22(3) | 1770-1772 | encoded | `s 22(3) the General Division may receive further evidence in this manner` ; type `s 22(3) manner of receiving further evidence` | scja1-part3-div4.l4 | |
| s 22(3)(a) | 1773-1774 | encoded | within `s 22(3) the General Division may receive further evidence in this manner` ; type `s 22(3) manner of receiving further evidence` | scja1-part3-div4.l4 | |
| s 22(3)(b) | 1775-1776 | encoded | within `s 22(3) the General Division may receive further evidence in this manner` ; type `s 22(3) manner of receiving further evidence` | scja1-part3-div4.l4 | |
| s 22(3)(c) | 1777-1784 | encoded | within `s 22(3) the General Division may receive further evidence in this manner` ; type `s 22(3) manner of receiving further evidence` | scja1-part3-div4.l4 | |
| s 22(3)(d) | 1785-1788 | encoded | within `s 22(3) the General Division may receive further evidence in this manner` ; type `s 22(3) manner of receiving further evidence` | scja1-part3-div4.l4 | |
| s 22(4) | 1789-1794 | fork F11 | `s 22(4) the further evidence may be given to the General Division` | scja1-part3-div4.l4 | Under section 22(4) |
| s 22(5) | 1795-1800 | fork F11 | `s 22(5) the further evidence may be given to the General Division without permission` | scja1-part3-div4.l4 | |
| s 22(6) | 1801-1805 | encoded | `s 22(6) the General Division may draw the inference, give the judgment or make the order` | scja1-part3-div4.l4 | |
| s 22(7) | 1806-1807 | encoded | within `s 22(7)(a) the power may be exercised in relation to any part of the decision appealed against`; `s 22(7)(b) the power may be exercised in favour of any party to the decision appealed against` | scja1-part3-div4.l4 | |
| s 22(7)(a) | 1808-1811 | encoded | `s 22(7)(a) the power may be exercised in relation to any part of the decision appealed against` | scja1-part3-div4.l4 | |
| s 22(7)(b) | 1812-1818 | encoded | `s 22(7)(b) the power may be exercised in favour of any party to the decision appealed against` | scja1-part3-div4.l4 | |
| s 22A(1) | 1819-1825 | fork F6 | `s 22A(1) the General Division may decide the matter without hearing oral arguments` | scja1-part3-div4.l4 | Under section 22A(1) |
| s 22A(2) | 1826-1829 | fork F16 | `s 22A(2) section 22A(1) allows this part of the proceeding to be conducted without an oral hearing` | scja1-part3-div4.l4 | |
| s 22A(3) | 1830-1840 | encoded | `s 22A(3) the General Division may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` | scja1-part3-div4.l4 | |
| s 22A(4) | 1841-1844 | encoded | `s 22A(4) the General Division must not hear the matter in an asynchronous manner`; `s 22A(4) the General Division shall not hear the matter in an asynchronous manner` | scja1-part3-div4.l4 | Under section 22A(4) |
| s 22A(5) | 1845-1850 | encoded | `s 22A(5) section 22A affects the General Division's power to hear oral arguments before deciding the matter` | scja1-part3-div4.l4 | |
| s 22B(1) | 1851-1857 | encoded | `s 22B(1) the General Division may on its own motion summarily dismiss the appeal` | scja1-part3-div4.l4 | Under section 22B(1) |
| s 22B(1)(a) | 1858-1860 | encoded | within `s 22B(1) the General Division may on its own motion summarily dismiss the appeal` | scja1-part3-div4.l4 | Under section 22B(1) |
| s 22B(1)(b) | 1861-1865 | encoded | within `s 22B(1) the General Division may on its own motion summarily dismiss the appeal` | scja1-part3-div4.l4 | Under section 22B(1) |
| s 22B(1)(c) | 1866-1868 | encoded | within `s 22B(1) the General Division may on its own motion summarily dismiss the appeal` | scja1-part3-div4.l4 | Under section 22B(1) |
| s 22B(2) | 1869-1871 | fork F7 | `s 22B(2) the General Division may summarily dismiss the appeal under section 22B(1) now, as the section requires`; `s 22B(2) the General Division must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div4.l4 | Under section 22B(2) |
| s 22B(2)(a) | 1872-1874 | fork F7 | within `s 22B(2) the General Division may summarily dismiss the appeal under section 22B(1) now, as the section requires`; `s 22B(2) the General Division must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div4.l4 | Under section 22B(2) |
| s 22B(2)(b) | 1875-1876 | fork F7 | within `s 22B(2) the General Division may summarily dismiss the appeal under section 22B(1) now, as the section requires`; `s 22B(2) the General Division must give the appellant an opportunity to show cause and consider the representations` | scja1-part3-div4.l4 | Under section 22B(2) |
| s 22B(3) | 1877-1880 | fork F3 | `s 22B(3) the thing is an appeal for the purposes of section 22B` | scja1-part3-div4.l4 | |
| Division 5 heading | 1881-1884 | inert, reason 1 | none | a Division heading | |
| s 23 | 1885-1899 | encoded | `s 23 the General Division may exercise powers of revision in the criminal proceedings` | scja1-part3-div5-6.l4 | |
| s 24 | 1900-1910 | encoded | `s 24 the General Division may call for and examine the record of the civil proceedings` | scja1-part3-div5-6.l4 | Under section 24 |
| s 25 | 1911-1920 | encoded | `s 25 the General Division may give such orders on the civil proceedings, including directing a new trial` | scja1-part3-div5-6.l4 | |
| s 26 | 1921-1926 | encoded | `s 26 the section applies to the civil matter`; `s 26 a proceeding by way of revision may be entertained at the instance of the party` | scja1-part3-div5-6.l4 | Under section 26 |
| s 27(1) | 1927-1936 | encoded | `s 27(1) the General Division has general supervisory and revisionary jurisdiction over the court` | scja1-part3-div5-6.l4 | |
| s 27(2) | 1937-1953 | encoded | `s 27(2) the General Division may take the step in the matter or proceeding` ; type `s 27(2) step` | scja1-part3-div5-6.l4 | Under section 27(2) |
| s 27(3) | 1954-1960 | encoded | `s 27(3) the proceedings in the subordinate court are stayed` | scja1-part3-div5-6.l4 | Under section 27(3) |
| s 27(4) | 1961-1970 | encoded | `s 27(4) the General Division is to have regard to whether the matter was or could reasonably have been raised in the appeal`; `s 27(4) the General Division must have regard to whether the matter was or could reasonably have been raised in the appeal` | scja1-part3-div5-6.l4 | |
| s 28(1) | 1971-1978 | encoded | `s 28(1) the party has a right to be heard before the General Division` | scja1-part3-div5-6.l4 | Under section 28(1) |
| s 28(2) | 1979-1981 | fork F16 | `s 28(2) the final order may be made to the prejudice of the person`; `s 28(2) the bar on a final order made to the prejudice of the person applies` | scja1-part3-div5-6.l4 | Under section 28(2) |
| Division 6 heading | 1982-1985 | inert, reason 1 | none | a Division heading | |
| s 28A(1) | 1986-2001 | fork F17 | `s 28A(1) the Chief Justice may by order direct the class of proceedings to be heard and determined by the District Court or Family Court` | scja1-part3-div5-6.l4 | |
| s 28A(2) | 2002-2003 | encoded | `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(a) | 2004-2006 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(a)(i) | 2007-2012 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(a)(ii) | 2013-2015 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(aa) | 2016-2020 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(b) | 2021-2025 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28A(2)(c) | 2026-2032 | encoded | within `s 28A(2) an order under section 28A(1) may make the provision` ; type `s 28A(2) provision` | scja1-part3-div5-6.l4 | |
| s 28B | 2033-2034 | repealed or blank in this text | none | the text shows: "28B. [Repealed by Act 40 of 2019]" | |
| Division 7 heading | 2035-2039 | inert, reason 1 | none | a Division heading | |
| s 29 | 2040-2045 | fork K1, F15 | `s 29 an appeal cannot be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29 |
| s 29(a) | 2046-2056 | fork K1, F15 | within `s 29 an appeal cannot be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29 |
| s 29(b) | 2057-2061 | fork K1, F15 | within `s 29 an appeal cannot be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29 |
| s 29A(1) | 2062-2067 | fork K1, K2, F14 | `s 29A(1) permission is required before an appeal may be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29A(1) |
| s 29A(1)(a) | 2068-2073 | fork K1, K2, F14 | within `s 29A(1) permission is required before an appeal may be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29A(1) |
| s 29A(1)(b) | 2074-2080 | fork K1, K2, F14 | `s 29A(1)(b) the amount in dispute or value of the subject matter does not exceed the sum` | scja1-part3-div7-9.l4 | |
| s 29A(1)(c) | 2081-2088 | fork K1, K2, F14 | within `s 29A(1) permission is required before an appeal may be brought against the decision` | scja1-part3-div7-9.l4 | Under section 29A(1) |
| s 29A(2) | 2089-2091 | fork K1 | `s 29A(2) the court from which permission must be obtained`; `s 29A(2) permission must be obtained from this court` | scja1-part3-div7-9.l4 | Under section 29A(2) |
| s 29A(2)(a) | 2092-2097 | fork K1 | within `s 29A(2) the court from which permission must be obtained`; `s 29A(2) permission must be obtained from this court` | scja1-part3-div7-9.l4 | Under section 29A(2) |
| s 29A(2)(b) | 2098-2109 | fork K1 | within `s 29A(2) the court from which permission must be obtained`; `s 29A(2) permission must be obtained from this court` | scja1-part3-div7-9.l4 | Under section 29A(2) |
| s 29A(3) | 2110-2117 | encoded | `s 29A(3) the President may specify another sum in substitution of the sum mentioned in section 29A(1)(b)` | scja1-part3-div7-9.l4 | |
| Division 8 heading | 2118-2119 | inert, reason 1 | none | a Division heading | |
| s 29B(1) | 2120-2127 | encoded | `s 29B(1) this section applies to the decision` | scja1-part3-div7-9.l4 | |
| s 29B(2) | 2128-2133 | fork F12, K1 | `s 29B(2) the 15th day after the date on which the decision is made`; `s 29B(2) the day before which the request for further arguments must be made`; `s 29B(2) the request for further arguments is made before the earlier of the following`; `s 29B(2) other reading: the request is made on or before the 15th day after the date on which the decision is made`; `s 29B(2) the Judge who made the decision may hear further arguments in respect of the decision` | scja1-part3-div7-9.l4 | Under section 29B(2) |
| s 29B(2)(a) | 2134-2138 | fork F12, K1 | within `s 29B(2) the 15th day after the date on which the decision is made`; `s 29B(2) the day before which the request for further arguments must be made`; `s 29B(2) the request for further arguments is made before the earlier of the following`; `s 29B(2) other reading: the request is made on or before the 15th day after the date on which the decision is made`; `s 29B(2) the Judge who made the decision may hear further arguments in respect of the decision` | scja1-part3-div7-9.l4 | Under section 29B(2) |
| s 29B(2)(b) | 2139-2142 | fork F12, K1 | within `s 29B(2) the 15th day after the date on which the decision is made`; `s 29B(2) the day before which the request for further arguments must be made`; `s 29B(2) the request for further arguments is made before the earlier of the following`; `s 29B(2) other reading: the request is made on or before the 15th day after the date on which the decision is made`; `s 29B(2) the Judge who made the decision may hear further arguments in respect of the decision` | scja1-part3-div7-9.l4 | Under section 29B(2) |
| s 29B(3) | 2143-2147 | encoded | `s 29B(3) the Judge may take the step` ; type `s 29B(3) step` | scja1-part3-div7-9.l4 | |
| s 29B(4) | 2148-2150 | encoded | `s 29B(4) this subsection applies` | scja1-part3-div7-9.l4 | |
| s 29B(4)(a) | 2151-2153 | encoded | `s 29B(4)(a) a notice of appeal may not be filed against the decision yet` | scja1-part3-div7-9.l4 | Under section 29B(4)(a) |
| s 29B(4)(a)(i) | 2154-2156 | encoded | within `s 29B(4)(a) a notice of appeal may not be filed against the decision yet` | scja1-part3-div7-9.l4 | Under section 29B(4)(a) |
| s 29B(4)(a)(ii) | 2157-2159 | encoded | within `s 29B(4)(a) a notice of appeal may not be filed against the decision yet` | scja1-part3-div7-9.l4 | Under section 29B(4)(a) |
| s 29B(4)(b) | 2160-2167 | encoded | `s 29B(4)(b) the date on which the time for filing a notice of appeal begins` | scja1-part3-div7-9.l4 | Under section 29B(4)(b) |
| s 29B(4)(b)(i) | 2168-2170 | encoded | within `s 29B(4)(b) the date on which the time for filing a notice of appeal begins` | scja1-part3-div7-9.l4 | Under section 29B(4)(b) |
| s 29B(4)(b)(ii) | 2171-2175 | encoded | within `s 29B(4)(b) the date on which the time for filing a notice of appeal begins` | scja1-part3-div7-9.l4 | Under section 29B(4)(b) |
| s 29B(5) | 2176-2181 | encoded | `s 29B(5) a party to the hearing may request further arguments before filing a notice of appeal`; `s 29B(5) a party to the hearing is required to request further arguments before filing a notice of appeal` | scja1-part3-div7-9.l4 | |
| Division 9 heading | 2182-2183 | inert, reason 1 | none | a Division heading | |
| s 29C(1) | 2184-2192 | fork K1 | `s 29C(1) the appeal is to be made to the Appellate Division` | scja1-part3-div7-9.l4 | |
| s 29C(2) | 2193-2198 | fork K1 | `s 29C(2) the appeal is to be made to the Court of Appeal` | scja1-part3-div7-9.l4 | |
| s 29C(3) | 2199-2203 | fork K1 | `s 29C(3) section 29C creates a right of appeal against the decision` | scja1-part3-div7-9.l4 | |
| s 29D(1) | 2204-2208 | encoded | `s 29D(1) the Court of Appeal may transfer the appeal to itself` ; type `s 29D(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29D(1)(a) | 2209-2211 | encoded | within `s 29D(1) the Court of Appeal may transfer the appeal to itself` ; type `s 29D(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29D(1)(b) | 2212-2223 | encoded | within `s 29D(1) the Court of Appeal may transfer the appeal to itself` ; type `s 29D(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29D(2) | 2224-2226 | encoded | `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(2)(a) | 2227-2228 | encoded | within `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(2)(b) | 2229-2230 | encoded | within `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(2)(c) | 2231-2233 | encoded | within `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(2)(c)(i) | 2234-2237 | encoded | within `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(2)(c)(ii) | 2238-2241 | encoded | within `s 29D(2) the power in section 29D(1) may be exercised in this way` ; type `s 29D(2) way` | scja1-part3-div7-9.l4 | |
| s 29D(3) | 2242-2247 | encoded | `s 29D(3) the Court of Appeal is to have regard to the matter`; `s 29D(3) the Court of Appeal must have regard to the matter prescribed by the Rules of Court` | scja1-part3-div7-9.l4 | |
| s 29D(4) | 2248-2253 | encoded | `s 29D(4) the Rules of Court may prescribe different matters for the circumstance` | scja1-part3-div7-9.l4 | |
| s 29D(5) | 2254-2259 | encoded | `s 29D(5) the appeal may be transferred under section 29D(1) even though it was made in accordance with section 29C(1)` | scja1-part3-div7-9.l4 | |
| s 29E(1) | 2260-2264 | encoded | `s 29E(1) the Court of Appeal may transfer the appeal to the Appellate Division` ; type `s 29E(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29E(1)(a) | 2265-2269 | encoded | within `s 29E(1) the Court of Appeal may transfer the appeal to the Appellate Division` ; type `s 29E(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29E(1)(b) | 2270-2279 | encoded | within `s 29E(1) the Court of Appeal may transfer the appeal to the Appellate Division` ; type `s 29E(1) appeal` | scja1-part3-div7-9.l4 | |
| s 29E(2) | 2280-2282 | fork F17 | `s 29E(2) the power in section 29E(1) may be exercised in this way` ; type `s 29E(2) way` | scja1-part3-div7-9.l4 | |
| s 29E(2)(a) | 2283-2284 | fork F17 | within `s 29E(2) the power in section 29E(1) may be exercised in this way` ; type `s 29E(2) way` | scja1-part3-div7-9.l4 | |
| s 29E(2)(b) | 2285-2291 | fork F17 | within `s 29E(2) the power in section 29E(1) may be exercised in this way` ; type `s 29E(2) way` | scja1-part3-div7-9.l4 | |
| s 29E(3) | 2292-2297 | encoded | `s 29E(3) the Court of Appeal is to have regard to the matter`; `s 29E(3) the Court of Appeal must have regard to the matter prescribed by the Rules of Court` | scja1-part3-div7-9.l4 | |
| s 29E(4) | 2298-2303 | encoded | `s 29E(4) the Rules of Court may prescribe different matters for the circumstance` | scja1-part3-div7-9.l4 | |
| s 29E(5) | 2304-2309 | encoded | `s 29E(5) the appeal may be transferred under section 29E(1) even though it was made in accordance with section 29C(2)` | scja1-part3-div7-9.l4 | |
| s 18D(3)(c) “third party proceedings” | 1431-1432 | encoded | `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` (the term is defined by its input) | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(c) “third party” | 1433-1434 | encoded | `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` (the term is defined by its input) | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(d) “subsequent party proceedings” | 1451-1453 | encoded | `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` (the term is defined by its input) | scja1-part3-div3-sicc.l4 | |
| s 18D(3)(d) “subsequent party” | 1453-1455 | encoded | `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` (the term is defined by its input) | scja1-part3-div3-sicc.l4 | |

## Fork register (scja1)

### The rulings that bind this row (word for word, as the brief prints them)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

Where a row rests on a ruling, its source comment says so (for example `ruling of 2026-11-05`).
Where I could not tell which of (a), (b) and (c) of the periods ruling a clause is, it has a fork below and says which I took.

### Forks taken, one entry each

Format: label, provision, the readings I saw, the one taken, the text that licenses each, and where the choice sits (function and `file:line`).
"Assumed, not ruled" means no ruling covers it and the call is mine; it is a small, separate commit-sized choice in the source.

**F1. "unless the context otherwise requires" (s 2 lead-in).**
Reading 1 (taken): the definitions govern unless the context requires otherwise, so when it does the gate answers `JUST FALSE` ("these definitions do not govern the word here"); the gate is its own yes/no question and the definition functions do not take it as an input.
Reading 2: the gate answers `NOTHING` when the context requires otherwise, because the Act does not say what the word means then.
Licence: "2. In this Act, unless the context otherwise requires —" (line 378).
Taken as reading 1 because "unless" is on the brief's list of words that make the text say no.
The "otherwise" is a judgment the person states as a plain input.
Sits in `scja1-part1-preliminary.l4:22` (judgment-call site QA).

**F2. Vice-President and President read as Justice and Judge (s 2 "Supreme Court Judge" and "Judge", s 4).**
Reading 1 (taken): a Vice-President of the Court of Appeal is a Justice of the Court of Appeal, and the President of the Appellate Division is a Judge of the Appellate Division, because s 4(c) ranks "the Justices of the Court of Appeal (other than the Vice-Presidents of the Court of Appeal)" and s 4(e) "the Judges of the Appellate Division (other than the President of the Appellate Division)", which only makes sense if the excepted office is otherwise inside the class.
Reading 2: the offices are separate and outside "Justice" and "Judge" unless a list names them.
Sits in `scja1-part1-preliminary.l4:225`.

**F3. A definition that says "means X and includes Y".**
Rows: s 2 "Registrar", "Rules of Court", "seal"; s 17C(3) and s 22B(3) ("appeal includes part of an appeal"); s 18K(2) ("rule of evidence includes ...").
Reading 1 (taken): the members the text names answer `JUST TRUE`, and anything else answers `NOTHING` (NOTHING-kind: includes).
Reading 2: "means" closes the definition and anything else answers `JUST FALSE`.
Licence: "means the Registrar of the Supreme Court and includes the Deputy Registrar and the Assistant Registrars"; "means Rules of Court made under this Act and includes forms"; "“seal” includes stamp".
A Sheriff is not named in the "Registrar" definition (lines 416-417), so a Sheriff asked about as a Registrar answers `NOTHING` (includes), where a reader who takes "means ... and includes" as closing the list would answer `JUST FALSE`.
Assumed, not ruled; this is marginal reading M1 below.
Sits in `scja1-part1-preliminary.l4:157`, `scja1-part1-preliminary.l4:171`, `scja1-part1-preliminary.l4:183`, `scja1-part3-div2-procedure.l4:169`, `scja1-part3-div4.l4:392`, `scja1-part3-div3-sicc.l4:580`.

**F4. "subordinate court" and the divisions of the Supreme Court (s 2).**
The definition lists courts under the State Courts Act 1970, the Family and Youth Courts, and "any other court, tribunal or judicial or quasi-judicial body from whose decisions a written law gives a right of appeal to the Supreme Court".
Reading 1 (taken): whether a division of the Supreme Court itself falls in the last limb is not said, so the answer is `NOTHING` (NOTHING-kind: undefined term).
Reading 2: "Supreme Court" in the last limb includes its own divisions, so they are subordinate courts.
Reading 3: it does not, so they are not.
Sits in `scja1-part1-preliminary.l4:202`.

**F5. ss 8(2AA) and 8(2AB) read together (gathered by hand; ruling E1, option B as guidance).**
Reading 1 (taken): an application on national interest or security grounds is heard in private ("is to be heard in private"); where the court has the power in s 8(2AB) to hear it otherwise, the Act does not say whether it will, so the combined answer is `NOTHING`.
Reading 2: the combined answer is `JUST FALSE` once the 8(2AB) power exists.
Licence: lines 535-537 and 541-556 (quoted in the source above the gathering function).
The gathering function is one extra function that calls the two single-section rules; it does not replace them.
Sits in `scja1-part2-hearings.l4:102`.

**F6. "(other than X)" in a grant (s 8A(1), s 17B(1), s 22A(1)) (question QE).**
Reading 1 (taken): a matter the parenthesis takes out answers `JUST FALSE`.
Reading 2: it answers `NOTHING`, because the parenthesis limits the grant and the section is silent about the excluded matter.
Licence: "the court may conduct the hearing of any matter or proceeding (other than a matter or proceeding prescribed by the Rules of Court, the Family Justice Rules or the Criminal Procedure Rules)" (lines 691-696).
Taken as reading 1 because an exclusion is the text's own no for that matter; marginal reading M4.
Sits in `scja1-part2-hearings.l4:314`, `scja1-part3-div2-procedure.l4:26`, `scja1-part3-div4.l4:322`.

**F7. A bare "must" or "is to be" with no stated consequence (question QB).**
Rows: s 11(2), s 17C(2) (the twin), s 18G, s 18H(2), s 18I(2), s 22B(2) (the twin).
Reading 1 (taken, assumed, not ruled): a case outside what the sentence requires answers `NOTHING`, because the text states a duty and does not say what follows when it is not done.
Reading 2: it answers `JUST FALSE`, because a bare "is to be" is the text's own statement of what must happen and anything else is therefore not what the Act requires.
Licence: "The distribution of business among the several Judges is to be made in accordance with such directions"; "Every proceeding in the Singapore International Commercial Court is to be heard and disposed of before a single Judge or 3 Judges"; "The Chief Justice is to appoint one of the Judges to preside"; "Before summarily dismissing any appeal under subsection (1), a Judge sitting in the General Division must (a) ... and (b) ...".
Ruling N2 counts a flat negative as the text's no; a bare "must" or "is to be" is not a negative, so it is not the text's no, and the function says NOTHING.
The names of these functions end "... as the section requires" (or "as the Act requires"), so a reader sees that the function asks whether a requirement is met and does not state a fact.
Sits in the six functions listed under QB in the judgment-call table.

**F8. s 17A(3), (5), (6): "where", "if" and "unless" on a stay of civil proceedings.**
Reading 1 (taken): a "where" or "if" that is not met, and an "unless" or "does not apply" that is met, are each the text's no (the stay is not ordered), `JUST FALSE`.
Reading 2: they answer `NOTHING`.
Licence: ruling of 2026-11-05 (b) and (c) for "where"; "if" and "unless" are on the brief's list.
The rule is also written as a regulative rule (`PARTY ... MUST ... LEST`) with a decision twin.
Marginal readings M2 (a "where" or "if" not met) and M3 (an "unless" met, or "does not apply" met).
Both limbs of the opening "Where civil proceedings involving any matter referred to in subsection (2)(b) or (c) ... involving parties who are Muslims or were married under the provisions of the Muslim law" answer alike: the parties limb not met is `JUST FALSE`, and the matter limb not met (maintenance for a wife or child, which is (2)(a), is not a matter in (2)(b) or (c)) is `JUST FALSE`, because both belong to one "Where".
Sits in `scja1-part3-div2-jurisdiction.l4:274` and `scja1-part3-div2-jurisdiction.l4:332`.

**F9. ss 16, 17 and 17A gathered by hand (ruling E1, option B as guidance).**
The sections give routes to one legal effect, "the General Division has civil jurisdiction": s 16(1), s 16(2), s 17(1) and s 17A(2) are routes, and s 17A(1) takes jurisdiction away "despite" ss 16 and 17.
Reading 1 (taken): each section is encoded on its own (option C), and one extra function calls them: `JUST FALSE` if s 17A(1) says there is no jurisdiction, `JUST TRUE` if any route is `JUST TRUE`, otherwise `NOTHING` (list not closed: the routes have no "only").
Reading 2: no gathering function (option C alone).
Sits in `scja1-part3-div2-jurisdiction.l4:436`.

**F10. "consists of" in ss 19 and 20 is not a closing word.**
Reading 1 (taken): a matter outside paragraphs (a) to (d) of s 19, or (a) to (c) of s 20, answers `NOTHING` (list not closed: no "only").
Reading 2: "consists of" closes the list and a matter outside answers `JUST FALSE`.
Licence: "The appellate civil jurisdiction of the General Division consists of —" (s 20, lines 1702-1703).
Marginal reading M6 in kind (a grant limited by its own wording is not a no).
Sits in `scja1-part3-div4.l4:46` and `scja1-part3-div4.l4:77`.

**F11. s 22(4): "Except as provided in subsection (5)".**
Reading 1 (taken): when (5) is met (the evidence relates to matters after the date of the decision appealed against) the whole bar goes, so neither permission nor special grounds is needed.
Reading 2: (5) lifts only the permission limb, and the "special grounds" limb of (4) still applies.
Licence: "Except as provided in subsection (5), further evidence may be given to the General Division only with the permission of the General Division and on special grounds".
Sits in `scja1-part3-div4.l4:241`.

**F12. s 29B(2): a request "before the earlier of" the extraction of the order and "the 15th day after the date on which the decision is made".**
Reading 1 (taken, assumed, not ruled): "before the 15th day" excludes the 15th day itself, so a request made on the 15th day is too late (`JUST FALSE`); a request made on the day the order is extracted answers `NOTHING`, because the core holds the date of extraction and the Act speaks of its time.
The 15th day is counted with the Interpretation Act module, including its shift when the last day of a period of days is a Sunday or public holiday.
Reading 2 (kept as an alternative function and tested): the request may be made on or before the 15th day.
Licence: "requests for further arguments before the earlier of the following: (a) the time at which the judgment or order relating to the decision is extracted; (b) the 15th day after the date on which the decision is made" (lines 2127-2139).
Sits in `scja1-part3-div7-9.l4:196`, `scja1-part3-div7-9.l4:220` and `scja1-part3-div7-9.l4:240`.

**F13. A ceiling: "a fine not exceeding $5,000 or ... imprisonment for a term not exceeding 3 years" (s 8(4)).**
Reading 1 (taken): a sentence above the ceiling answers `JUST FALSE`, by ruling (a) of the periods line ("not later than" is its example): the text fixes the limit in its own words.
Reading 2: it answers `NOTHING`, as a scope limit with no "only".
Assumed, not ruled.
Sits in `scja1-part2-hearings.l4:193`.

**K1 (from the keel). Does "General Division" include the Singapore International Commercial Court?**
Taken as the keel's note says: neither; the SICC is its own `Court`.
In ss 29, 29A and 29B(2) a decision of the SICC answers `NOTHING` (NOTHING-kind: undefined term), because s 18A makes the SICC "a division of the General Division" while s 18J(4) says "General Division" does not include it for that section.
In s 29C(2) the answer depends on the Sixth Schedule input: when `sch 6 the appeal is to be made to the Court of Appeal` is `JUST TRUE` the answer is `JUST TRUE` for a decision of the General Division or of the SICC, because the Schedule's own answer (which is understood to name decisions of the SICC in its paragraph 1(f)) decides it and the question whether the SICC is "the General Division" does not arise; when that input is not `JUST TRUE`, a decision of the SICC stays `NOTHING`, because then the answer does depend on that question.
A decision of any other court, such as a District Court, is outside s 29C and stays `NOTHING` whatever the Schedule input says.
The Sixth Schedule is scja3's and I did not read it for this encoding, so the paragraph 1(f) point is as I was told it, not checked against the Schedule.
In s 10A the same, and in s 2 "court" and "General Division" the SICC is not named.
s 18J(4) is encoded as written.
Sits in the functions named in the coverage rows marked `fork K1`.

**K2 (from the keel). A case with no amount or value (ss 21(1)(a), 29A(1)(b)).**
Taken: `NOTHING` (the Act does not say what an unvalued case counts as).
Other readings: it does not "exceed" the sum, so the money limb is met; or its value is 0.
Sits in `scja1-part3-div4.l4:97` and `scja1-part3-div7-9.l4:70`.

**K3 (from the keel). Order of appointments (s 4).**
Taken: the date of appointment is the order, and a tie, or two holders of a single office, is a case the Act does not settle (`NOTHING`).
Other reading: an explicit order number.
Sits in `scja1-part2-court.l4:67`.

**F14. "In the following cases" and a case in no limb (ss 21(1), 29A(1); questions QC and the seat's "do I need permission?").**
Rows: `s 21(1) an appeal lies ...`, `s 21(1) permission is needed ...`, `s 29A(1) permission is required ...`, and the money limbs `s 21(1)(a)` and `s 29A(1)(b)`.
Reading 1 (taken, assumed, not ruled): "in the following cases" is a scope limit with no "only" on the list, so a case in no limb answers `NOTHING`: for example a District Court claim of $75,000 against the $60,000 limit in s 21(1)(a), or a claim of $300,000 against the $250,000 limit in s 29A(1)(b) with every other head false.
Ruling (c) of the periods line: a scope limit with no "only" is not a no.
Reading 2: it answers `JUST FALSE` ("no permission needed"), because the cases listed are the only ones in which the section says permission is needed.
Licence: s 21(1), lines 1719-1737: "an appeal lies to the General Division from a decision of a District Court or Magistrate's Court only with the permission of that District Court or Magistrate's Court or the General Division in the following cases"; s 29A(1): "In the following cases, permission is required before an appeal may be brought".
The "only" in s 21(1) attaches to the permission ("only with the permission"), so where permission is needed and has not been given the answer to "does an appeal lie?" is `JUST FALSE`; it does not close the list of cases.
The seat questions "do I need permission?" (ss 21(1) and 29A(1)) say in their `@desc` what a not-covered answer means for the person: that the section does not say that permission is needed in their case, and that they should look at the Schedules and any other provision.
Sits in `scja1-part3-div4.l4:130`, `scja1-part3-div4.l4:145` and `scja1-part3-div7-9.l4:107`.

**F15. A bar asked "is it barred by this section?" for a case outside the bar's own description (ss 10(5), 17A(1), 29; and s 8A(3) outside its limbs).**
Reading 1 (taken): for a case outside the description of what the bar covers, ss 10(5), 17A(1) and 29 answer `NOTHING` (ruling (c): a scope limit with no "only"), while s 8A(3) outside its limbs (a), (b) and (c) answers `JUST FALSE` (ruling (b): an unmet "where").
Reading 2: all four answer `JUST FALSE`, or all four answer `NOTHING`.
The textual reason they differ:
s 8A(3) lists its three limbs each with its own "where" ("(a) where oral evidence is given ...; (b) where oral evidence is given ... unless all the parties consent; or (c) where the matter is prescribed by the Rules of Court ..."), lines 714-724, so a case in none of them is a case in which no "where" is met.
s 10(5) (lines 817-844) and s 29 (lines 2042-2058) name what they cover by a list with no "where" and no "only": "in proceedings incidental or preliminary to — (a) ... (e)", "In the following cases, an appeal cannot be brought ... (a) ... (b)".
s 17A(1) (lines 1109-1114) describes the proceedings by relative clauses ("matters which come within the jurisdiction of the Syariah Court ... in which all the parties are Muslims or where the parties were married under the provisions of the Muslim law"), where the "where" is a relative adverb inside the description of the matters and does not open a limb of the rule.
The twin for the grant of s 10(5), `s 10(5) the Judge may sit ...`, answers `JUST FALSE` when the Judge is the one the bar names and `NOTHING` otherwise, for the same reason.
Sits in `scja1-part3-div1.l4:144`, `scja1-part3-div1.l4:155`, `scja1-part3-div2-jurisdiction.l4:205`, `scja1-part3-div7-9.l4:48` and `scja1-part2-hearings.l4:352`.

**F16. A met "unless", asked as the grant or as the bar (ss 17B(2), 22A(2), 28(2)).**
Reading 1 (taken): the answer follows what the function's name asks.
`s 17B(2) section 17B(1) allows this part ...` and `s 22A(2) section 22A(1) allows this part ...` ask what the earlier subsection allows, so a met "unless all the parties consent" answers `JUST TRUE` (the subsection no longer denies what (1) allows), oral evidence without consent answers `JUST FALSE`, and a part with no oral evidence answers `NOTHING`.
`s 28(2) the final order may be made to the prejudice of the person` asks the grant, so a met "unless that person has had an opportunity of being so heard" answers `NOTHING` (the subsection grants nothing itself), and not heard answers `JUST FALSE`; its twin `s 28(2) the bar on a final order made to the prejudice of the person applies` asks the bar, so it answers `JUST TRUE` when the person has not been heard and `JUST FALSE` once the "unless" is met.
Reading 2: a met "unless" answers `JUST TRUE` when asked as a grant, or `NOTHING` when asked about what (1) allows.
Licence: "Section 17B(1) does not allow any part of a proceeding where oral evidence is given to be conducted without an oral hearing, unless all the parties consent"; "No final order may be made to the prejudice of any person unless that person has had an opportunity of being so heard".
Sits in `scja1-part3-div2-procedure.l4:39`, `scja1-part3-div4.l4:306`, `scja1-part3-div5-6.l4:232` and `scja1-part3-div5-6.l4:243`.

**F17. A list or a description with no "only" in a grant (ss 10(1A), 18B(1), 18G, 18M, 28A(1)).**
Reading 1 (taken): a case outside the list answers `NOTHING`.
s 10(1A): "any uneven number of Judges greater than the number provided under subsection (1)"; s 18B(1): "a Supreme Court Judge, a Senior Judge or an International Judge"; s 18G: "a single Judge or 3 Judges"; s 18M: a party, a registered foreign lawyer or law expert, and "in accordance with the Rules of Court"; s 28A(1): "the District Court or Family Court", which the function now takes as an input, so a direction to another court, such as a Magistrate's Court, answers `NOTHING`.
Reading 2: it answers `JUST FALSE`.
s 29E(2) is different: its paragraph (b) says an application "may only be made on the ground" that the appeal was not made to the Court of Appeal in accordance with section 29C, so an application on another ground answers `JUST FALSE`; the `way` type has two members (own motion, application by a party), so a reference by the Appellate Division cannot be entered (a gap; see "What the text does not answer").
Sits in `scja1-part3-div1.l4:44`, `scja1-part3-div3-sicc.l4:40`, `scja1-part3-div3-sicc.l4:335`, `scja1-part3-div3-sicc.l4:625`, `scja1-part3-div5-6.l4:268` and `scja1-part3-div7-9.l4:601`.

**F18. A weekday in a vacation (s 10B(1) and (2)).**
s 10B(1) says the General Division "is to sit on every day of the year except on Saturdays, Sundays and public holidays", so a weekday that is none of those answers `JUST TRUE` in `s 10B(1) the General Division is to sit on the day`, which takes only the day and the public holidays.
s 10B(2) says "Despite subsection (1)" a Judge may lawfully sit "on a Saturday, Sunday or public holiday or during a vacation prescribed under section 7" if the Chief Justice has directed it or the business is extremely urgent, which suggests that a vacation weekday is outside what (1) requires.
The Act does not say how the two fit.
Reading 1 (taken): each subsection is encoded as written: (1) has no vacation input, so a vacation weekday answers `JUST TRUE` under (1); (2) takes one boolean for "a Saturday, Sunday, public holiday or a day in a vacation".
Reading 2: (1) answers `NOTHING` or `JUST FALSE` for a vacation weekday.
Sits in `scja1-part3-div1.l4:244` and `scja1-part3-div1.l4:265`.

**F19. An offence clause with a relative clause ("Any person who ...", s 8(4)).**
`s 8(4) the person is guilty of an offence`: "Any person who acts in contravention of any order under subsection (2A) or (3) shall be guilty of an offence" (line 615).
Reading 1 (taken): a person who has not acted in contravention of such an order answers `NOTHING`, because the relative clause describes the person to whom the offence applies, with no "if", "only" or "unless", so it is a scope limit (ruling (c)); the sentence is separate (F13).
Reading 2: it answers `JUST FALSE`, reading "who ..." like an "if".
This is the only offence clause in the lines this part covers, so there is no other "who" offence clause to align with.
Sits in `scja1-part2-hearings.l4:184`.

### Judgment calls (QA to QE), one hand-written line per function

Format: question, provision, function, `file:line` of the function, answer taken, other reading.
QA is a bar with "unless"; QB a bare "must" or "is to be"; QC a question about a Schedule; QD a duty with an unmet "if" or "where"; QE "(other than X)".
QF (the state ledger) does not arise: this encoding writes no events to a ledger.
There are 37 lines: QA 7, QB 6, QC 12, QD 9, QE 3, QF 0.
Each line is one function; a function with an "unless" in two of its branches is still one line.
The file:line is the line of the function's name in the deposited module, filled in by the notes script from the file itself.

| question | provision | function | file:line | answer taken | other reading |
| --- | --- | --- | --- | --- | --- |
| QA | s 2 | `s 2 the definitions of this section govern the word here` | `scja1-part1-preliminary.l4:22` | "unless the context otherwise requires": when the person says the context does require otherwise, `JUST FALSE`; otherwise `JUST TRUE` (F1) | `NOTHING`, because the Act does not say what the word means then |
| QA | s 10A(2) | `s 10A(2) the remuneration of the assessors is costs in the proceedings` | `scja1-part3-div1.l4:199` | assessors not summoned on a party's application: `NOTHING` ("Subject to subsection (3)"); the General Division has otherwise ordered: `JUST FALSE`; else `JUST TRUE` (M3) | `NOTHING` once an order is made |
| QA | s 17A(3) | `s 17A(3) the General Division is to stay the civil proceedings` | `scja1-part3-div2-jurisdiction.l4:274` | an "unless" certificate filed, or "does not apply" met, is `JUST FALSE` (the stay is not due); matter limb not met is `JUST FALSE` too (F8, M2, M3) | `NOTHING` |
| QA | s 17B(2) | `s 17B(2) section 17B(1) allows this part of the proceeding to be conducted without an oral hearing` | `scja1-part3-div2-procedure.l4:39` | the name asks what s 17B(1) allows, so "unless all the parties consent" met is `JUST TRUE`; oral evidence and no consent `JUST FALSE`; no oral evidence `NOTHING` (F16) | `NOTHING` for the met "unless", on the reading that (2) grants nothing itself |
| QA | s 22A(2) | `s 22A(2) section 22A(1) allows this part of the proceeding to be conducted without an oral hearing` | `scja1-part3-div4.l4:306` | as s 17B(2) (F16) | as s 17B(2) |
| QA | s 28(2) | `s 28(2) the final order may be made to the prejudice of the person` | `scja1-part3-div5-6.l4:232` | the name asks the grant, so "unless that person has had an opportunity of being so heard" met is `NOTHING` (the subsection grants nothing itself); not heard `JUST FALSE`; not a final order to the person's prejudice `NOTHING` (F16) | `JUST TRUE` once the person has been heard |
| QA | s 28(2) | `s 28(2) the bar on a final order made to the prejudice of the person applies` | `scja1-part3-div5-6.l4:243` | the twin asks the bar: `JUST TRUE` if the person has not been heard, `JUST FALSE` once the "unless" is met, `NOTHING` if it is not a final order to their prejudice (F16) | `NOTHING` when the "unless" is met |
| QB | s 11(2) | `s 11(2) the distribution of business among the Judges is as the Act requires` | `scja1-part3-div1.l4:292` | made on the Chief Justice's directions `JUST TRUE`; made otherwise `NOTHING`: "is to be made in accordance with such directions" states a duty and no consequence (F7) | `JUST FALSE` |
| QB | s 17C(2) | `s 17C(2) the Judge may summarily dismiss the appeal under section 17C(1) now, as the section requires` | `scja1-part3-div2-procedure.l4:138` | opportunity to show cause given and representations considered `JUST TRUE`; otherwise `NOTHING` (F7) | `JUST FALSE` |
| QB | s 18G | `s 18G the proceeding is to be heard and disposed of before this number of Judges, as the section requires` | `scja1-part3-div3-sicc.l4:335` | 1 or 3 Judges `JUST TRUE`; any other number `NOTHING`: two numbers named, no "only", no consequence stated (F7, F17) | `JUST FALSE` |
| QB | s 18H(2) | `s 18H(2) the presiding Judge was appointed by the Chief Justice, as the section requires` | `scja1-part3-div3-sicc.l4:358` | case heard before 3 Judges and the Judge who presides appointed by the Chief Justice `JUST TRUE`; a case not before 3 Judges `JUST FALSE` ("This section applies where ..."); otherwise `NOTHING`: "is to appoint" states a duty and no consequence (F7) | `JUST FALSE` |
| QB | s 18I(2) | `s 18I(2) the Singapore International Commercial Court exercises the power as the Act requires` | `scja1-part3-div3-sicc.l4:471` | exercised under the Rules of Court and the written law `JUST TRUE`; otherwise `NOTHING` (F7) | `JUST FALSE` |
| QB | s 22B(2) | `s 22B(2) the General Division may summarily dismiss the appeal under section 22B(1) now, as the section requires` | `scja1-part3-div4.l4:437` | opportunity to show cause given and representations considered `JUST TRUE`; otherwise `NOTHING`, as s 17C(2) (F7) | `JUST FALSE` |
| QC | s 18(2) | `s 18(2) the General Division has the power set out in the First Schedule` | `scja1-part3-div2-procedure.l4:195` | seam 1: Schedule `JUST TRUE` is `JUST TRUE`; Schedule `JUST FALSE` or `NOTHING` is `NOTHING` ("Without limiting subsection (1)": a power outside the Schedule may still be vested by a written law) | `JUST FALSE` when the Schedule says no |
| QC | s 18(3) | `s 18(3) the power is to be exercised in accordance with the written law, Rules of Court or Family Justice Rules relating to it` | `scja1-part3-div2-procedure.l4:208` | seam 1, answered as s 18(2) | as s 18(2) |
| QC | s 18I(1) | `s 18I(1) the Singapore International Commercial Court may exercise the power` | `scja1-part3-div3-sicc.l4:456` | seam 2: the paragraph 1 power is an express exception, so `JUST FALSE`; a Schedule that does not answer is `NOTHING` | none: the exception is the text's own |
| QC | s 21(1) | `s 21(1) an appeal lies to the General Division from the decision` | `scja1-part3-div4.l4:130` | seam 3: where permission is needed and not given, `JUST FALSE` ("only with the permission"); a case in neither limb `NOTHING` ("in the following cases") (F14) | `JUST FALSE` for a case in neither limb |
| QC | s 21(1) | `s 21(1) permission is needed to appeal from the decision` | `scja1-part3-div4.l4:145` | seam 3: money limb or Third Schedule `JUST TRUE`; neither `NOTHING` (F14) | `JUST FALSE` when neither limb holds |
| QC | s 29 | `s 29 an appeal cannot be brought against the decision` | `scja1-part3-div7-9.l4:48` | seam 4: (a) or a `JUST TRUE` Fourth Schedule is `JUST TRUE`; otherwise `NOTHING` (F15) | `JUST FALSE` |
| QC | s 29A(1) | `s 29A(1) permission is required before an appeal may be brought against the decision` | `scja1-part3-div7-9.l4:107` | seams 5 and 6: a Schedule's `NOTHING` is passed through, never turned into `JUST FALSE`; a case in no limb is `NOTHING` (F14, K2) | `JUST FALSE` for a case in no limb |
| QC | s 29A(2) | `s 29A(2) the court from which permission must be obtained` | `scja1-part3-div7-9.l4:130` | seam 7: a court a written law specifies wins; otherwise the Fifth Schedule's court; `NOTHING` if neither answers | none |
| QC | s 29A(2) | `s 29A(2) permission must be obtained from this court` | `scja1-part3-div7-9.l4:141` | seam 7 twin: the court named `JUST TRUE`, another court `JUST FALSE`, no answer `NOTHING` | none |
| QC | s 29C(1) | `s 29C(1) the appeal is to be made to the Appellate Division` | `scja1-part3-div7-9.l4:381` | seam 8: `JUST FALSE` when (2) is `JUST TRUE`; a Schedule that does not answer `NOTHING`; an SICC decision `NOTHING` (K1) | none |
| QC | s 29C(2) | `s 29C(2) the appeal is to be made to the Court of Appeal` | `scja1-part3-div7-9.l4:401` | seam 8: a `JUST TRUE` Schedule answer is `JUST TRUE` for a decision of the General Division or of the SICC (which the Sixth Schedule is understood to name), and a decision of any other court stays `NOTHING`; an SICC decision with a Schedule answer that is not `JUST TRUE` stays `NOTHING` (K1) | `NOTHING` for every SICC decision |
| QC | s 29C | `s 29C the court to which the appeal is to be made` | `scja1-part3-div7-9.l4:416` | seam 8 and its twins: `JUST` a court, or `NOTHING` | none |
| QD | s 8A(3) | `s 8A(3) the court shall not conduct the part through a live audio link only` | `scja1-part2-hearings.l4:382` | IF the decision twin is `JUST TRUE` THEN PARTY SHANT ... ELSE FULFILLED: an unmet "where" is FULFILLED at once | the rule silent when the "where" is not met |
| QD | s 17A(3) | `s 17A(3) the General Division must stay the civil proceedings` | `scja1-part3-div2-jurisdiction.l4:332` | no stay due is FULFILLED at once; the section sets no time, so there is no WITHIN | as s 8A(3) |
| QD | s 17B(4) | `s 17B(4) the General Division shall not hear the matter in an asynchronous manner` | `scja1-part3-div2-procedure.l4:80` | where hearing it asynchronously is not inconsistent with the court's duty of fairness, FULFILLED at once | as s 8A(3) |
| QD | s 17C(2) | `s 17C(2) the Judge must give the appellant an opportunity to show cause and consider the representations` | `scja1-part3-div2-procedure.l4:152` | a Judge who is not about to summarily dismiss is FULFILLED at once | as s 8A(3) |
| QD | s 22A(4) | `s 22A(4) the General Division shall not hear the matter in an asynchronous manner` | `scja1-part3-div4.l4:363` | as s 17B(4) | as s 8A(3) |
| QD | s 22B(2) | `s 22B(2) the General Division must give the appellant an opportunity to show cause and consider the representations` | `scja1-part3-div4.l4:451` | as s 17C(2) | as s 8A(3) |
| QD | s 27(4) | `s 27(4) the General Division must have regard to whether the matter was or could reasonably have been raised in the appeal` | `scja1-part3-div5-6.l4:200` | the gate not `JUST TRUE` is FULFILLED at once | as s 8A(3) |
| QD | s 29D(3) | `s 29D(3) the Court of Appeal must have regard to the matter prescribed by the Rules of Court` | `scja1-part3-div7-9.l4:523` | the gate not `JUST TRUE` is FULFILLED at once | as s 8A(3) |
| QD | s 29E(3) | `s 29E(3) the Court of Appeal must have regard to the matter prescribed by the Rules of Court` | `scja1-part3-div7-9.l4:632` | the gate not `JUST TRUE` is FULFILLED at once | as s 8A(3) |
| QE | s 8A(1) | `s 8A(1) the court may conduct the hearing of the matter through the means` | `scja1-part2-hearings.l4:314` | a matter the Rules prescribe, taken out by "(other than ...)", is `JUST FALSE` (F6) | `NOTHING` |
| QE | s 17B(1) | `s 17B(1) the General Division may decide the matter without hearing oral arguments` | `scja1-part3-div2-procedure.l4:26` | as s 8A(1) (F6) | `NOTHING` |
| QE | s 22A(1) | `s 22A(1) the General Division may decide the matter without hearing oral arguments` | `scja1-part3-div4.l4:322` | as s 8A(1) (F6) | `NOTHING` |

## Jural relations (scja1)

Hohfeld's correlatives: a claim (right) pairs with a duty; a privilege (liberty) with a no-right; a power with a liability; an immunity with a disability.
One row per provision or group that creates a relation; a provision that creates none (a definition, a counting or deeming rule) is listed as `none`.
"Not named" means the text does not say who holds the right or bears the duty, and I did not guess.
In the last column `s 8(2) …` stands for the whole rule name, which starts with that label and is found by searching for it; section "Coverage (scja1)" prints the full names.
The kinds are recorded here and are not typed into any person-facing answer (ruling N2).

| provision | holder: what they hold | bearer of the correlative | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 1 | none (short title) | none | none | inert |
| s 2 | none (definitions; the "unless the context otherwise requires" gate) | none | none | `s 2 …` |
| s 3 | none (declares three courts superior courts of record: a status) | none | none | `s 3 …` |
| s 4 | none (the rank order of Judges: a counting rule) | none | none | `s 4 …` |
| s 5(1) | the Judge next in precedence, present in Singapore and able to act: power to exercise the Chief Justice's powers and perform the duties | anyone subject to those powers (not named) | power / liability | `s 5(1) …` |
| s 5(2) | none (deeming: temporary absence in Malaysia is not absence from Singapore) | none | none | `s 5(2) …` |
| s 5A | an International Judge may sit only in the Singapore International Commercial Court, in an appeal from it and in an application relating to such an appeal | the International Judge is under a disability to sit elsewhere; parties elsewhere hold the correlative immunity (not named) | immunity / disability | `s 5A …` |
| s 6 | none (the seal: machinery) | none | none | inert |
| s 7 | the Chief Justice: power to specify vacations, limited to 2 months in any year | court users (not named) | power / liability | `s 7 …` |
| s 8(1) | the public: privilege to attend a court held to try a cause or matter | the court and the parties: no-right to keep the public out, except under s 8 | privilege / no-right | `s 8(1) …` |
| s 8(2) | the court: power to hear a matter, or a part, in private if satisfied it is expedient on a stated ground | the parties and the public: liability | power / liability | `s 8(2) …` |
| s 8(2AA) | the applicant (not named): claim that a national-interest application be heard in private | the court: duty | claim / duty | `s 8(2AA) …` |
| s 8(2AB) | the court: power to hear such an application otherwise than in private if satisfied of (a) and (b) | the applicant: liability | power / liability | `s 8(2AB) …`, `ss 8(2AA) and 8(2AB) …` |
| s 8(2A) | the court: power to order a thing in a court document removed or redacted | the person who produces the document: liability | power / liability | `s 8(2A) …` |
| s 8(3) | the court: power to order that no person do an act of the three kinds named | any person: liability | power / liability | `s 8(3) …` |
| s 8(4) | the State (not named): claim that a contravening person be liable to a fine up to $5,000, imprisonment up to 3 years, or both | the person who contravenes an order under s 8(2A) or (3): duty not to, and liability to the ceiling | claim / duty | `s 8(4) …` |
| s 8(5) | the court: power to permit an individual (a journalist, a person with a sufficient interest, or another it specifies) to be present | the individual: no-right to be present | power / liability; privilege / no-right for the individual | `s 8(5) …` |
| s 8(6), (7) | none (matters the court may consider; borrowed definitions) | none | none | `s 8(6) …`, `s 8(7) …` |
| s 8A(1) | the court: power to conduct a hearing by video, television, audio or other approved electronic means, except a matter the Rules prescribe | the parties: liability | power / liability | `s 8A(1) …` |
| s 8A(2), (4), (6) | none (a saving of other Acts; an interpretive rule; a deeming rule). In (4) the court holds an immunity from breach of (3) for a temporary, insignificant disruption | a party: disability to treat that as a breach | immunity / disability (in (4) only) | `s 8A(2) …`, `s 8A(4) …`, `s 8A(6) …` |
| s 8A(3) | a party to the proceeding (not named): claim that no part of a hearing be conducted through a live audio link only in the cases (a) to (c) | the court: duty (SHANT) | claim / duty | `s 8A(3) …` and the regulative rule `s 8A(3) the court shall not …` |
| s 8A(5) | a party (not named): claim that the court not conduct the hearing under s 8A(1) if that is inconsistent with its duty of fairness | the court: duty | claim / duty | `s 8A(5) …` |
| s 9 | none (repealed) | none | none | repealed |
| s 10(1), (1A) | the Chief Justice: power to direct that a proceeding be heard before a greater uneven number of Judges | the parties: liability | power / liability | `s 10(1) …`, `s 10(1A) …` |
| s 10(1B) | none (a rule that 3 or more Judges decide by majority) | none | none | `s 10(1B) …` |
| s 10(2) | a Judge: power to exercise the General Division's jurisdiction in court or in chambers | the parties: liability | power / liability | `s 10(2) …` |
| s 10(3) | none (deleted) | none | none | repealed |
| s 10(4) | a Judge who reserved judgment: power to deliver it after the appointment expires or ends | the parties: liability | power / liability | `s 10(4) …` |
| s 10(5) | a party (not named): claim that a Judge not sit on the matters (a) to (e) | the Judge: duty | claim / duty | `s 10(5) …` |
| s 10A(1) | the court: power to summon assessors | the parties and the persons summoned: liability | power / liability | `s 10A …` |
| s 10A(2), (3) | the assessors (by implication; not named): claim to remuneration, which is costs in the proceedings unless the General Division otherwise orders, or is payable out of moneys provided by Parliament where they were summoned otherwise than on a party's application | the parties (as costs); Parliament's moneys | claim / duty | `s 10A(2) …`, `s 10A(3) …` |
| s 10A(4) | any party: power to object to a proposed assessor, personally or as to qualification, in the prescribed manner | the court: liability (what follows an objection is not said) | power / liability | `s 10A(4) …` |
| s 10B(1) | none (the General Division sits every day but Saturdays, Sundays and public holidays: a rule on sittings) | none | none | `s 10B(1) …` |
| s 10B(2) | a Judge: privilege to sit on a Saturday, Sunday, public holiday or in vacation in the cases (a) and (b) | the parties: no-right | privilege / no-right | `s 10B(2) …` |
| s 11(1) | the Chief Justice: power to appoint the times and places of sitting | Judges and court users: liability | power / liability | `s 11(1) …` |
| s 11(2) | the Chief Justice: power to direct the distribution of business | the Judges: duty to follow the directions (a bare "is to be") | power / liability; claim / duty | `s 11(2) …` |
| s 12 | none (repealed) | none | none | repealed |
| s 13 | the judgment creditor: power to enforce a money judgment against the debtor's property by seizure and sale; the judgment debtor: immunity for the property in (a) to (e) | the debtor: liability; the creditor: disability for the excepted property | power / liability; immunity / disability | `s 13 …` |
| s 14(1) | an interested party: power to prepare the instrument and tender it; the court (by the Registrar's signature): power to give the signature the effect of execution | the party ordered who is absent, neglects or refuses: liability | power / liability | `s 14(1) …` |
| s 14(2) | the court: power to proceed by attachment against a person neglecting or refusing to execute, sign or indorse | that person: liability | power / liability | `s 14(2) …` |
| s 15(1), (2) | the General Division: jurisdiction over offences (a) to (f), and power to pass any sentence allowed by law (criminal: no seat) | the accused: liability | power / liability | `s 15(1) …`, `s 15(2) …` |
| s 16(1), (2) | the plaintiff: power to start an action in personam; the General Division: jurisdiction | the defendant served in Singapore or as the Rules authorise: liability | power / liability | `s 16(1) …`, `s 16(2) …` |
| s 17(1), (2) | the General Division: civil jurisdiction over the subjects named | the defendant: liability | power / liability | `s 17(1) …`, `s 17(2) …` |
| s 17A(1) | a party to proceedings on a Syariah Court matter: immunity from the General Division's jurisdiction | the General Division: disability | immunity / disability | `s 17A(1) …` |
| s 17A(2) | the General Division: jurisdiction vested by written law over the other Syariah-adjacent matters | the defendant: liability | power / liability | `s 17A(2) …` |
| s 17A(3), (5), (6) | a party to the civil proceedings (not named): claim that the General Division stay them in the cases stated | the General Division: duty | claim / duty | `s 17A(3) …` and the regulative rule `s 17A(3) the General Division must stay …` |
| s 17A(3A), (4), (7), (8), (9) | none (a date cut, a deeming rule, a direction to apply the civil law, a Women's Charter application, definitions). In (7) the General Division is under a duty to apply the civil law; the claimant is not named | none | none | `s 17A(3A) …` to `s 17A(9) …` |
| ss 16, 17, 17A together | none (a gathering function, not a new rule) | none | none | `ss 16, 17 and 17A …` |
| s 17B(1) | the General Division: power to decide a matter without oral arguments, except a matter the Rules prescribe | the parties: liability | power / liability | `s 17B(1) …` |
| s 17B(2) | a party to a proceeding where oral evidence is given: immunity from decision without an oral hearing unless all the parties consent | the General Division: disability | immunity / disability | `s 17B(2) …` |
| s 17B(3) | the General Division: power to direct a hearing by exchange of written correspondence | the parties: liability | power / liability | `s 17B(3) …` |
| s 17B(4) | the parties (not named): claim that the General Division not hear a matter asynchronously if that would be inconsistent with its duty of fairness | the General Division: duty (SHANT) | claim / duty | `s 17B(4) …` and the regulative rule `s 17B(4) the General Division shall not …` |
| s 17B(5), 17C(3) | none (to avoid doubt; a definition) | none | none | `s 17B(5) …`, `s 17C(3) …` |
| s 17C(1) | a Judge: power to dismiss an appeal against the Registrar's decision summarily on the Judge's own motion, on the grounds (a) to (c) | the appellant: liability | power / liability | `s 17C(1) …` |
| s 17C(2) | the appellant: claim to a reasonable opportunity to show cause and to have the representations considered | the Judge: duty (MUST) | claim / duty | `s 17C(2) …` and the regulative rule `s 17C(2) the Judge must give …` |
| s 18(1), (2), (3) | the General Division: powers under written law and the First Schedule; (3) the powers are exercised under the written law and Rules | persons subject to the powers: liability; (3) the claimant is not named | power / liability | `s 18(1) …` to `s 18(3) …` |
| s 18A, 18C | none (constitutes the Singapore International Commercial Court as a division; applies the Act to it) | none | none | `s 18A …`, `s 18C …` |
| s 18B(1), (2) | the Chief Justice: power to appoint a Judge as President of the Court | the Judge: liability | power / liability | `s 18B(1) …`, `s 18B(2) …` |
| s 18D(1) to (4) | the Singapore International Commercial Court: jurisdiction over the actions in (1), the proceedings in (2), and, in (3) and (4), over additional parties, counterclaims, third party and subsequent party proceedings | the parties, third parties and subsequent parties: liability | power / liability | `s 18D(1) …` to `s 18D(4) …` |
| s 18E | none (repealed) | none | none | repealed |
| s 18F | each party to an agreement to submit to the Court: claim to the three deemed terms (submit to the exclusive jurisdiction of the Court; carry out any judgment or order without undue delay; waive recourse outside Singapore insofar as validly waivable), unless the agreement says otherwise | every other party: duty | claim / duty | `s 18F(1) …` |
| s 18G, 18H | none (the number of Judges; how a 3-Judge or 2-Judge case is decided) | none | none | `s 18G …`, `s 18H(1) …` to `s 18H(6) …` |
| s 18I(1), (2) | the Singapore International Commercial Court: the General Division's original civil powers except the stated exceptions; (2) the duty to exercise them under the Rules | persons subject: liability; (2) the claimant is not named | power / liability | `s 18I(1) …`, `s 18I(2) …` |
| s 18J(1), (2), (3) | the Court and the General Division: power to transfer a case in accordance with the Rules; the receiving court: privilege to keep evidence already adduced; both: power to make consequential orders | the parties: liability | power / liability | `s 18J(1) …` to `s 18J(4) …` |
| s 18K | the Court: privilege not to be bound by Singapore rules of evidence in the cases and to the extent the Rules provide, and to apply others | the parties: no-right to the Singapore rule in those cases | privilege / no-right | `s 18K(1)(a) …`, `s 18K(1)(b) …`, `s 18K(2) …` |
| s 18L | the Court: power to order foreign law determined on submissions instead of proof, and to have regard to matters the Rules prescribe | the parties: liability | power / liability | `s 18L(1) …`, `s 18L(2) …` |
| s 18M | a party to a case in the Court or an appeal from it: privilege to be represented, in accordance with the Rules, by a registered foreign lawyer or law expert | the other parties and the Court: no-right to object | privilege / no-right | `s 18M …` |
| s 19 | the General Division: appellate criminal jurisdiction (criminal: no seat) | the appellant: liability | power / liability | `s 19 …` |
| s 20 | the General Division: appellate civil jurisdiction | the parties to an appeal: liability | power / liability | `s 20 …` |
| s 21(1) | a party wishing to appeal a District Court or Magistrate's Court decision: power to appeal to the General Division, only with permission in the cases (a) and (b); the lower court or the General Division: power to give permission | the respondent: liability | power / liability | `s 21(1) …` |
| s 21(2), (2B) | none (deleted) | none | none | repealed |
| s 21(2A) | the party who obtained or resisted permission: immunity from challenge to the General Division's order on permission | any court: disability to disturb it | immunity / disability | `s 21(2A) …` |
| s 21(3) | the President: power to vary the amount in s 21(1) | persons affected: liability | power / liability | `s 21(3) …` |
| s 22(1), (2) | the appellant (by implication): claim to a rehearing; the General Division: all the powers and duties of the court appealed from | the General Division: duty | claim / duty | `s 22(1) …`, `s 22(2) …` |
| s 22(3) | the General Division: power to receive further evidence in the manners (a) to (d), including by affidavit and by deposition before an examiner or commissioner | the parties: liability | power / liability | `s 22(3) …` |
| s 22(4), (5) | the General Division: power to permit further evidence on special grounds; a party: privilege to give evidence of matters after the decision without permission | the party: no-right to give further evidence otherwise; the General Division: no-right to refuse in the (5) case | power / liability; privilege / no-right | `s 22(4) …`, `s 22(5) …` |
| s 22(6), (7) | the General Division: power to draw inferences of fact, give judgment and make orders, over any part of the decision and in favour of any party | the parties: liability | power / liability | `s 22(6) …`, `s 22(7)(a) …`, `s 22(7)(b) …` |
| s 22A(1) to (5) | as s 17B: the General Division's power to decide without oral arguments (1) and (3); a party's immunity (2); the parties' claim and the General Division's duty (4); none (5) | as s 17B | power / liability; immunity / disability; claim / duty | `s 22A(1) …` to `s 22A(5) …`; regulative rule `s 22A(4) …` |
| s 22B(1) to (3) | as s 17C: the General Division's power to dismiss an appeal summarily on its own motion (1); the appellant's claim to show cause and the General Division's duty (2); a definition (3) | as s 17C | power / liability; claim / duty | `s 22B(1) …` to `s 22B(3) …`; regulative rule `s 22B(2) …` |
| s 23 | the General Division: power of revision in criminal proceedings in subordinate courts (criminal: no seat) | subordinate courts: liability | power / liability | `s 23 …` |
| s 24 | the General Division: power to call for and examine the record of civil proceedings in a subordinate court | the subordinate court: liability | power / liability | `s 24 …` |
| s 25 | the General Division: power to give orders, including a new trial, to secure substantial justice | the parties: liability | power / liability | `s 25 …` |
| s 26 | a party who could have appealed and did not: no-right to revision; the General Division: disability to entertain it | the party | disability / no-right | `s 26 …` |
| s 27(1) to (3) | the General Division: general supervisory and revisionary jurisdiction over subordinate courts, power to take the steps in (2), and to stay the lower proceedings on calling for a record | subordinate courts and the parties to the lower matter: liability | power / liability | `s 27(1) …` to `s 27(3) …` |
| s 27(4) | the General Division: duty to have regard to whether the matter was or could reasonably have been raised in the appeal; the claimant is not named | the General Division | duty | `s 27(4) …` and the regulative rule `s 27(4) …` |
| s 28(1) | the General Division: privilege to hear no party as of right when it exercises these powers, subject to written law | the parties: no-right to be heard | privilege / no-right | `s 28(1) …` |
| s 28(2) | a person: immunity from a final order made to their prejudice unless they have had an opportunity to be heard | the General Division: disability | immunity / disability | `s 28(2) …` |
| s 28A(1), (2) | the Chief Justice: power to order a class of proceedings to be heard and determined by the District Court or Family Court, and the provisions in (2) | the parties to those proceedings: liability | power / liability | `s 28A(1) …`, `s 28A(2) …` |
| s 28B | none (repealed) | none | none | repealed |
| s 29 | the party in whose favour a decision stands: immunity from appeal in the cases (a) and (b) | the other party: disability to appeal | immunity / disability | `s 29 …` |
| s 29A(1), (3) | the appellant: power to appeal only with permission in the cases (a) to (c); the President: power to specify another sum | the respondent: liability | power / liability | `s 29A(1) …`, `s 29A(3) …` |
| s 29A(2) | none (which court gives permission) | none | none | `s 29A(2) …` |
| s 29B(1) to (5) | a party, or the Judge: power to request further arguments before the earlier of the two events; the Judge: power to hear them and affirm, vary or set aside; in (4)(a) the appellant is under a disability to file a notice of appeal until the Judge decides, and the respondent holds the correlative immunity; in (5) a party has a privilege to request or not | the other parties: liability; in (5) no-right to require a request | power / liability; immunity / disability; privilege / no-right | `s 29B(1) …` to `s 29B(5) …` |
| s 29C(1), (2), (3) | the appellant: power to appeal to the Appellate Division, or to the Court of Appeal if the Sixth Schedule or another written law so provides; (3) creates no right of appeal | the respondent: liability | power / liability | `s 29C(1) …` to `s 29C(3) …`, `s 29C the court …` |
| s 29D(1) to (5) | the Court of Appeal: power to transfer an appeal to itself, on its own motion, on a reference by the Appellate Division, or on a party's application on stated grounds; a party: power to apply on those grounds; (3) the Court's duty to have regard to the matters the Rules prescribe | the parties: liability; the Court: liability to the application | power / liability; claim / duty | `s 29D(1) …` to `s 29D(5) …`; regulative rule `s 29D(3) …` |
| s 29E(1) to (5) | the Court of Appeal: power to transfer an appeal to the Appellate Division, on its own motion or on a party's application on the stated ground; (3) as s 29D(3) | as s 29D | power / liability; claim / duty | `s 29E(1) …` to `s 29E(5) …`; regulative rule `s 29E(3) …` |

## Marginal readings for a lawyer (scja1)

These are the readings the brief marks "for a lawyer, not for you to decide".
I took them as the status quo and list every branch that rests on one.
Each reading is stated with the other reading beside it.

| label | the reading taken | the other reading |
| --- | --- | --- |
| M1 | a "means ... and includes" definition: the members it names are `JUST TRUE`, anything else is `NOTHING` (fork F3) | "means" closes the set, so anything else is `JUST FALSE` |
| M2 | s 17A(3), (5), (6): a "where" or "if" that is not met answers `JUST FALSE` (fork F8) | `NOTHING`: "if A then B" does not itself say "if not A then not B" |
| M3 | s 17A(3), (5), (6): an "unless" that is met, or a "does not apply" that is met, answers `JUST FALSE` (fork F8) | `NOTHING` |
| M4 | everywhere else, a failed "if", "where", "when", "upon", "unless", "until", "while", "except", "provided" or "only" is the text's no, clause by clause, within the provision that holds it (this includes "(other than X)", fork F6, and a stated ceiling, fork F13) | `NOTHING` |
| M5 | a flat negative ("shall not", "must not", "may not", "does not", "no appeal") is the text's no (ruling N2) | `NOTHING` |
| M6 | a grant or prohibition limited by its own wording does not answer no outside the limit: it answers `NOTHING` (for example a "consists of" list without "only", fork F10) | `JUST FALSE` |

The table below is built by a script from the source comments: it takes every branch carrying `FALSE-kind` (reading M2 to M5, or a "means" definition, which is the text's own no and not marginal) and every branch carrying `NOTHING-kind (limited by its own wording)` (reading M6).
The class shown for a `JUST FALSE` branch is read from its quoted words by keyword, so it is a guide: a branch can rest on more than one reading, and a reader should go to the quoted words.

The table lists every branch that rests on reading (a) or (b): 132 branches that answer JUST FALSE and 113 that answer NOTHING because the text limits its own grant or prohibition, in 156 functions.
The class of a JUST FALSE branch is read from its quoted words by keyword (M4 a failed condition, M5 a flat negative, `definition` a "means" definition, which is the text's own no and is not marginal); a branch can rest on more than one.

| function | JUST FALSE branches (file:line, the words relied on, class) | NOTHING branches limited by the text's own wording (file:line, the words) |
| --- | --- | --- |
| `s 2 the definitions of this section govern the word here` | scja1-part1-preliminary.l4:24 "unless the context otherwise requires" [M4 failed condition] | none |
| `s 2 Appellate Division: the court is the Appellate Division of the High Court` | scja1-part1-preliminary.l4:36 "means" [definition] | none |
| `s 2 court: the court is the General Division, the Appellate Division or the Court of Appeal` | scja1-part1-preliminary.l4:51 "means" [definition] | none |
| `s 2 Family Division of the High Court: the court is the Family Division of the High Court` | scja1-part1-preliminary.l4:63 "means" [definition] | none |
| `s 2 Family Justice Rules: the instrument is the Family Justice Rules` | scja1-part1-preliminary.l4:78 "means" [definition] | none |
| `s 2 General Division: the court is the General Division of the High Court` | scja1-part1-preliminary.l4:90 "means" [definition] | none |
| `s 2 Judge: the person is a Supreme Court Judge, a Judicial Commissioner, a Senior Judge or an International Judge` | scja1-part1-preliminary.l4:105 "means" [definition] | none |
| `s 2 Judge (a): in relation to the General Division, the person is a Judge sitting in that Division` | scja1-part1-preliminary.l4:120 "means a Judge sitting in that Division in accordance with the Constitution and this Act" [definition] | none |
| `s 2 Judge (b): in relation to the Appellate Division, the person is a Judge sitting in that Division` | scja1-part1-preliminary.l4:134 "means a Judge sitting in that Division in accordance with the Constitution and this Act" [definition] | none |
| `s 2 Judge (c): in relation to the Court of Appeal, the person is a Judge sitting in that Court` | scja1-part1-preliminary.l4:148 "means a Judge sitting in that Court in accordance with the Constitution and this Act" [definition] | none |
| `s 2 subordinate court: the court is a subordinate court` | scja1-part1-preliminary.l4:210 "means" ... "any other court, tribunal or judicial or quasi-judicial body from the decisions of [definition]<br>scja1-part1-preliminary.l4:213 "means" ... "any other court, tribunal or judicial or quasi-judicial body from the decisions of [definition] | none |
| `s 2 Supreme Court Judge: the person is a Supreme Court Judge` | scja1-part1-preliminary.l4:233 "means" [definition] | none |
| `s 4 the first Judge ranks before the second` | scja1-part2-court.l4:72 "rank in the following order" [M4 failed condition]<br>scja1-part2-court.l4:76 "according to the order of their appointments" [M4 failed condition] | none |
| `s 5(1) the powers and duties of the Chief Justice pass to the next Judge in precedence` | scja1-part2-court.l4:114 "Whenever during any period, owing to illness or absence from Singapore or any other cause, the [M4 failed condition] | none |
| `s 5(2) the absence counts as absence from Singapore for s 5` | scja1-part2-court.l4:135 "temporary absence in any part of Malaysia is not to be deemed to be absence from Singapore" [M5 flat negative] | none |
| `s 5A an International Judge may sit in this sitting` | scja1-part2-court.l4:160 "may only sit in the Singapore International Commercial Court, in an appeal from a decision of  [M4 failed condition] | scja1-part2-court.l4:156 "An International Judge may only sit" speaks of International Judges |
| `s 7 the vacations specified for the year are within the limit` | scja1-part2-court.l4:173 "which must not exceed 2 months in any year" [M5 flat negative] | none |
| `s 8(1) the place is deemed an open and public court to which the public generally may have access` | none | scja1-part2-hearings.l4:25 the deeming speaks of "the place in which any court is held for the purpose of trying any cause |
| `s 8(2) the court has power to hear the matter or proceeding in private` | scja1-part2-hearings.l4:49 "if the court is satisfied that it is expedient" [M4 failed condition] | none |
| `s 8(2AA) the application is to be heard in private` | none | scja1-part2-hearings.l4:61 "Any application ... on the grounds that it is expedient in the national interest or national s |
| `s 8(2AB) the court has power to hear the application otherwise than in private` | scja1-part2-hearings.l4:81 "if the court is satisfied that (a) ... and (b)" [M4 failed condition] | none |
| `ss 8(2AA) and 8(2AB) the application will be heard in private` | none | scja1-part2-hearings.l4:104 s 8(2AA) speaks of applications on the ground of national interest or national security |
| `s 8(2A) the court has power to order the thing removed or sufficiently redacted` | scja1-part2-hearings.l4:137 "if satisfied that it is expedient" [M4 failed condition] | scja1-part2-hearings.l4:138 the order is for "(a) ... (b) ... or (c)"<br>scja1-part2-hearings.l4:140 "which is contained in any court document intended to be produced before the court" |
| `s 8(4) the person is guilty of an offence` | none | scja1-part2-hearings.l4:187 "Any person who acts in contravention of any order under subsection (2A) or (3)" |
| `s 8(4) the sentence is within what the person is liable to on conviction` | scja1-part2-hearings.l4:196 "a fine not exceeding $5,000 or to imprisonment for a term not exceeding 3 years or to both" [M4 failed condition] | none |
| `s 8(5) the court may permit the individual to be present in the courtroom` | none | scja1-part2-hearings.l4:222 "A court that hears the whole or any part of any matter or proceeding in private may" |
| `s 8(5)(a) the individual is a journalist who reports news for a newspaper or a broadcasting service` | none | scja1-part2-hearings.l4:297 a person who is not such a journalist may still be within (b) or (c) |
| `s 8A(1) the court may conduct the hearing of the matter through the means` | scja1-part2-hearings.l4:316 "(other than a matter or proceeding prescribed by the Rules of Court, the Family Justice Rules  [M4 failed condition] | none |
| `s 8A(2) section 8A(1) affects the operation of the provision` | scja1-part2-hearings.l4:333 "does not affect the operation of" [M5 flat negative] | scja1-part2-hearings.l4:334 s 8A(2) names three provisions |
| `s 8A(3) the court must not conduct this part of the hearing through a live audio link only` | scja1-part2-hearings.l4:358 "where" (a), (b) or (c) is not met [M4 failed condition/M5 flat negative] | scja1-part2-hearings.l4:354 "through a live audio link only, without an accompanying live video link or live television lin |
| `s 8A(4) the court is considered to have conducted the part through a live audio link only` | scja1-part2-hearings.l4:409 "is not considered to have conducted a part of a hearing of a matter through a live audio link  [M4 failed condition/M5 flat negative] | scja1-part2-hearings.l4:410 "by reason only of a temporary disruption ... that was insignificant and which did not affect t |
| `s 8A(5) the court must not conduct the hearing in the manner provided under section 8A(1)` | scja1-part2-hearings.l4:423 "if to do so would be inconsistent with the court's duty" [M4 failed condition] | none |
| `s 8A(6) the court is deemed to be sitting at the appointed place` | scja1-part2-hearings.l4:440 "when the court conducts a hearing of a matter or proceeding in the manner provided under subse [M4 failed condition] | scja1-part2-hearings.l4:444 s 8A(6) names the places appointed under ss 11(1), 34(1)(a) and 52(1)(a), for the courts they g |
| `s 10(1A) the Chief Justice may direct that the proceeding be heard before this number of Judges` | none | scja1-part3-div1.l4:47 "any uneven number of Judges greater than the number provided under subsection (1)" |
| `s 10(1B) how a proceeding before 3 or more Judges is decided` | none | scja1-part3-div1.l4:64 "A proceeding in the General Division before 3 or more Judges" |
| `s 10(2) a Judge may exercise the jurisdiction of the General Division in the cause, matter or proceeding` | none | scja1-part3-div1.l4:87 "in all such causes and matters ... as might immediately before 9 January 1970 have been heard  |
| `s 10(4) the Judge has power to deliver judgment despite the expiry or termination of the appointment` | scja1-part3-div1.l4:104 "If a Judge reserves judgment in any proceedings and his or her appointment as a Judge expires  [M4 failed condition] | none |
| `s 10(5) the Judge must not sit in the General Division on the hearing or determine an application in the proceeding` | none | scja1-part3-div1.l4:146 "proceedings incidental or preliminary to" (a) to (e)<br>scja1-part3-div1.l4:148 (a) to (e) each speak of what "the Judge" did "as the Presiding Judge" |
| `s 10(5) the Judge may sit in the General Division on the hearing or determine an application in the proceeding` | scja1-part3-div1.l4:158 "No Judge is to sit in the General Division on the hearing of, or determine any application in  [M4 failed condition] | scja1-part3-div1.l4:157 "proceedings incidental or preliminary to" (a) to (e)<br>scja1-part3-div1.l4:159 (a) to (e) each speak of what "the Judge" did "as the Presiding Judge" |
| `s 10A the court may summon assessors` | scja1-part3-div1.l4:178 "if it thinks fit" [M4 failed condition]<br>scja1-part3-div1.l4:180 "if it thinks fit" (reached through s 32(3)) [M4 failed condition]<br>scja1-part3-div1.l4:182 "if it thinks fit" (reached through s 50(3)) [M4 failed condition] | scja1-part3-div1.l4:183 "In any proceedings before the General Division"; the Singapore International Commercial Court  |
| `s 10A(2) the remuneration of the assessors is costs in the proceedings` | scja1-part3-div1.l4:202 "unless otherwise ordered by the General Division" [M4 failed condition] | scja1-part3-div1.l4:201 "Subject to subsection (3)": where the assessors are not summoned on a party's application, sub |
| `s 10A(3) the remuneration of the assessors is payable out of moneys provided by Parliament` | scja1-part3-div1.l4:211 "Where one or more assessors are summoned for the purposes of this section otherwise than on th [M4 failed condition] | none |
| `s 10A(4) a party may take objection to the proposed assessor` | scja1-part3-div1.l4:224 "Where any person is proposed to be summoned as an assessor" [M4 failed condition] | scja1-part3-div1.l4:226 "either personally or in respect of the person's qualification ... in the prescribed manner" |
| `s 10B(1) the General Division is to sit on the day` | scja1-part3-div1.l4:246 "except on Saturdays, Sundays and public holidays" [M4 failed condition]<br>scja1-part3-div1.l4:247 "except on Saturdays, Sundays and public holidays" [M4 failed condition]<br>scja1-part3-div1.l4:248 "except on Saturdays, Sundays and public holidays" [M4 failed condition] | none |
| `s 10B(2) the Judge may lawfully sit on the day` | scja1-part3-div1.l4:270 "if (a) ... or (b)" [M4 failed condition] | scja1-part3-div1.l4:267 "a Saturday, Sunday or public holiday or during a vacation prescribed under section 7" |
| `s 11(1) the General Division sits at the time and place` | none | scja1-part3-div1.l4:283 "at such times and at such places as the Chief Justice may from time to time appoint" |
| `s 13 the property of the judgment debtor may be seized under an enforcement order for seizure and sale` | scja1-part3-div1.l4:344 "except (a) ... when the value of such apparel, bedding, tools and implements does not exceed $ [M4 failed condition/M5 flat negative]<br>scja1-part3-div1.l4:345 "except ... (b) tools of artisans" [M4 failed condition]<br>scja1-part3-div1.l4:347 "except ... (b) ... such animals and seed-grain or produce as may in the opinion of the court b [M4 failed condition]<br>scja1-part3-div1.l4:348 "except ... (c) the wages or salary of the judgment debtor" [M4 failed condition]<br>scja1-part3-div1.l4:349 "except ... (d) any pension, gratuity or allowance granted by the Government" [M4 failed condition]<br>scja1-part3-div1.l4:351 "except ... (e) the share of the judgment debtor in a partnership, as to which the judgment cre [M4 failed condition] | scja1-part3-div1.l4:342 "A judgment for the payment of money to any person or into court may be enforced" |
| `s 14(1) the interested party may prepare the instrument and tender it to the court for execution` | scja1-part3-div1.l4:373 "If (a) ... and (b) ..." [M4 failed condition] | none |
| `s 14(1) the Registrar's signature has the same effect as execution by the party ordered` | scja1-part3-div1.l4:397 "If (a) ... and (b) ..." with steps (c) and (d) and "the signature thereof by the Registrar, by [M4 failed condition] | none |
| `s 14(2) section 14 abridges the court's power to proceed by attachment against the person` | scja1-part3-div1.l4:408 "Nothing in this section is to be held to abridge the powers of the court to proceed by attachm [M4 failed condition] | scja1-part3-div1.l4:409 "against any person neglecting or refusing to execute, sign or indorse any such instrument" |
| `s 15(2) the General Division may pass the sentence` | none | scja1-part3-div2-jurisdiction.l4:63 "any sentence allowed by law" |
| `s 16(1) the General Division has jurisdiction to hear and try the action in personam` | scja1-part3-div2-jurisdiction.l4:92 "where (a) the defendant is served ... or (b) the defendant submits to the jurisdiction" [M4 failed condition] | scja1-part3-div2-jurisdiction.l4:88 "any action in personam" |
| `s 17(1) the civil jurisdiction of the General Division includes the subject` | none | scja1-part3-div2-jurisdiction.l4:147 "in relation to a dispute for which no proceedings have been commenced in a court" |
| `s 17A(1) the General Division has no jurisdiction to hear and try the civil proceedings` | none | scja1-part3-div2-jurisdiction.l4:209 "matters which come within the jurisdiction of the Syariah Court under section 35(2)(a), (b) or |
| `s 17A(2) the General Division has the jurisdiction vested in it by written law over the civil proceedings` | none | scja1-part3-div2-jurisdiction.l4:228 "(a) maintenance for any wife or child; (b) custody of any child; and (c) disposition or divisi<br>scja1-part3-div2-jurisdiction.l4:229 "such matters" come within the Syariah Court's jurisdiction under section 35(2)(d) or (e), 51 o |
| `s 17A(3) the General Division is to stay the civil proceedings` | scja1-part3-div2-jurisdiction.l4:276 "Where civil proceedings ... involving parties who are Muslims or were married under the provis [M4 failed condition]<br>scja1-part3-div2-jurisdiction.l4:289 "Where civil proceedings involving any matter referred to in subsection (2)(b) or (c)"; mainten [M4 failed condition/M5 flat negative]<br>scja1-part3-div2-jurisdiction.l4:290 "if" no divorce event in the Syariah Court (a) precedes the civil proceedings, or (b) follows t [M4 failed condition/M5 flat negative] | none |
| `s 17A(3A) the registration of the divorce counts for section 17A(3)` | scja1-part3-div2-jurisdiction.l4:352 "registration of a divorce ... under that section before 1 March 2009" [M4 failed condition] | none |
| `s 17A(4) the Syariah Court proceedings are deemed to have been commenced before the civil proceedings` | scja1-part3-div2-jurisdiction.l4:368 "where the proceedings in the Syariah Court are commenced on the same day" [M4 failed condition] | none |
| `s 17A(7) the General Division applies the civil law` | none | scja1-part3-div2-jurisdiction.l4:379 "in exercising its jurisdiction or powers under subsection (2)" |
| `s 17A(8) section 112 of the Women's Charter 1961 applies to the General Division in the proceeding` | none | scja1-part3-div2-jurisdiction.l4:391 "in the exercise of its jurisdiction or powers under subsection (2)(c)" |
| `s 17A(9) Syariah Court: the court is the Syariah Court constituted under the Administration of Muslim Law Act 1966` | scja1-part3-div2-jurisdiction.l4:410 "“Syariah Court” means the Syariah Court constituted under the Administration of Muslim Law Act [definition] | none |
| `ss 16, 17 and 17A the General Division has civil jurisdiction by one of these sections` | scja1-part3-div2-jurisdiction.l4:438 "Despite sections 16 and 17, the General Division has no jurisdiction" [M4 failed condition] | none |
| `s 17B(1) the General Division may decide the matter without hearing oral arguments` | scja1-part3-div2-procedure.l4:29 "other than a matter prescribed by the Rules of Court or the Family Justice Rules" [M4 failed condition] | scja1-part3-div2-procedure.l4:28 "any matter in its original civil jurisdiction" |
| `s 17B(2) section 17B(1) allows this part of the proceeding to be conducted without an oral hearing` | scja1-part3-div2-procedure.l4:43 "does not allow any part of a proceeding where oral evidence is given ... to be conducted witho [M4 failed condition/M5 flat negative] | scja1-part3-div2-procedure.l4:41 "any part of a proceeding where oral evidence is given" |
| `s 17B(3) the General Division may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` | none | scja1-part3-div2-procedure.l4:57 "in any matter that the General Division may decide without hearing oral arguments" |
| `s 17B(4) the General Division must not hear the matter in an asynchronous manner` | scja1-part3-div2-procedure.l4:69 "if to do so would be inconsistent with the court's duty" [M4 failed condition] | none |
| `s 17B(5) section 17B affects the General Division's power to hear oral arguments before deciding the matter` | scja1-part3-div2-procedure.l4:98 "this section does not affect the power of the General Division to hear oral arguments" [M5 flat negative] | scja1-part3-div2-procedure.l4:99 "any matter that may be decided without hearing oral arguments" |
| `s 17C(1) a Judge sitting in the General Division may on his or her own motion summarily dismiss the appeal` | scja1-part3-div2-procedure.l4:125 "if the Judge is satisfied of any of the following" [M4 failed condition] | scja1-part3-div2-procedure.l4:122 "any appeal made against a decision of the Registrar relating to civil proceedings" |
| `s 18(2) the General Division has the power set out in the First Schedule` | none | scja1-part3-div2-procedure.l4:198 "Without limiting subsection (1)": a power outside the First Schedule may still be vested by a  |
| `s 18(3) the power is to be exercised in accordance with the written law, Rules of Court or Family Justice Rules relating to it` | none | scja1-part3-div2-procedure.l4:211 "The powers mentioned in subsection (2)" |
| `s 18B(1) the Chief Justice may appoint the Judge to be the President of the Singapore International Commercial Court` | none | scja1-part3-div3-sicc.l4:45 "a Supreme Court Judge, a Senior Judge or an International Judge" |
| `s 18B(2) the Chief Justice is the President of the Singapore International Commercial Court` | scja1-part3-div3-sicc.l4:56 "If no appointment is made under subsection (1)" [M4 failed condition] | none |
| `s 18C the provision of the Act applies to proceedings in the Singapore International Commercial Court as to the General Division in its original civil jurisdiction` | none | scja1-part3-div3-sicc.l4:72 "Subject to sections 18D to 18M and 80(2A)" |
| `s 18D(1) the Singapore International Commercial Court has jurisdiction to hear and try the action` | scja1-part3-div3-sicc.l4:97 "any action that satisfies all of the following conditions" [M4 failed condition] | none |
| `s 18D(2)(a) the Singapore International Commercial Court has jurisdiction to hear the proceedings relating to international commercial arbitration` | none | scja1-part3-div3-sicc.l4:115 "Without limiting subsection (1)": other routes remain; this paragraph names proceedings "that  |
| `s 18D(2)(b) the Singapore International Commercial Court has jurisdiction to hear the application` | none | scja1-part3-div3-sicc.l4:135 "Without limiting subsection (1)": other routes remain |
| `s 18D(2)(c) the Singapore International Commercial Court has jurisdiction to hear the corporate insolvency, restructuring or dissolution proceedings` | none | scja1-part3-div3-sicc.l4:157 "Without limiting subsection (1)": other routes remain |
| `s 18D(2)(c) the version of the Companies Act 1967 is one in force before 30 July 2020` | scja1-part3-div3-sicc.l4:166 "the Companies Act 1967 as in force immediately before 30 July 2020" [M4 failed condition] | none |
| `s 18D(3) the jurisdiction under section 18D(1) includes the further jurisdiction in this subsection` | scja1-part3-div3-sicc.l4:179 "Where the Singapore International Commercial Court has and exercises jurisdiction under subsec [M4 failed condition] | none |
| `s 18D(3)(a) the jurisdiction includes hearing and trying the action upon the joinder of an additional party` | scja1-part3-div3-sicc.l4:192 "Where the Singapore International Commercial Court has and exercises jurisdiction under subsec [M4 failed condition]<br>scja1-part3-div3-sicc.l4:194 "if the action continues to maintain an international and commercial character" [M4 failed condition] | none |
| `s 18D(3)(b) the jurisdiction includes hearing and trying the counterclaim` | scja1-part3-div3-sicc.l4:208 "Where the Singapore International Commercial Court has and exercises jurisdiction under subsec [M4 failed condition]<br>scja1-part3-div3-sicc.l4:210 "if the action and counterclaim taken as a whole maintain an international and commercial chara [M4 failed condition] | none |
| `s 18D(3)(c) the jurisdiction includes hearing and trying the third party proceedings` | scja1-part3-div3-sicc.l4:234 "Where the Singapore International Commercial Court has and exercises jurisdiction under subsec [M4 failed condition]<br>scja1-part3-div3-sicc.l4:237 "if (i) the requirements ... are satisfied; and (ii) the main action and the third party procee [M4 failed condition] | scja1-part3-div3-sicc.l4:235 "proceedings (called ... third party proceedings) brought by a defendant or respondent against  |
| `s 18D(3)(d) the jurisdiction includes hearing and trying the subsequent party proceedings` | scja1-part3-div3-sicc.l4:264 "Where the Singapore International Commercial Court has and exercises jurisdiction under subsec [M4 failed condition]<br>scja1-part3-div3-sicc.l4:267 "if (i) the requirements ... are satisfied; and (ii) the main action, the third party proceedin [M4 failed condition] | scja1-part3-div3-sicc.l4:265 "proceedings (called ... subsequent party proceedings) brought by a third party against any par |
| `s 18F(1) the parties are considered to have agreed to the term` | scja1-part3-div3-sicc.l4:322 "applies only if there is no express provision to the contrary in the agreement" [M4 failed condition] | scja1-part3-div3-sicc.l4:321 "the parties to an agreement to submit to the jurisdiction of the Singapore International Comme<br>scja1-part3-div3-sicc.l4:324 "insofar as the recourse can be validly waived" |
| `s 18H(1) section 18H applies to the case` | scja1-part3-div3-sicc.l4:350 "This section applies where a case in the Singapore International Commercial Court is heard bef [M4 failed condition] | none |
| `s 18H(2) the presiding Judge was appointed by the Chief Justice, as the section requires` | scja1-part3-div3-sicc.l4:360 "This section applies where a case ... is heard before 3 Judges" [M4 failed condition] | none |
| `s 18H(4) the case is to be reheard` | scja1-part3-div3-sicc.l4:395 "if one or more of the Judges are unable to continue hearing the case" [M4 failed condition] | scja1-part3-div3-sicc.l4:396 "Subject to subsection (5)": the remaining 2 "may continue"; the Act does not say whether they  |
| `s 18H(5) the remaining 2 Judges may continue to hear and determine the case` | scja1-part3-div3-sicc.l4:405 "Where one Judge is unable to continue hearing a case for any reason" [M4 failed condition]<br>scja1-part3-div3-sicc.l4:407 "if the parties consent" [M4 failed condition] | none |
| `s 18H(6) this subsection applies to the case` | scja1-part3-div3-sicc.l4:423 "Where a case is heard by 2 Judges under subsection (5)" [M4 failed condition] | none |
| `s 18H(6) how the case heard by 2 Judges is determined` | none | scja1-part3-div3-sicc.l4:437 "Where a case is heard by 2 Judges under subsection (5)" |
| `s 18I(1) the Singapore International Commercial Court may exercise the power` | scja1-part3-div3-sicc.l4:458 "except (a) the power under paragraph 1 of the First Schedule" [M4 failed condition]<br>scja1-part3-div3-sicc.l4:459 "except ... (b) any power that must be exercised through the Family Division of the High Court" [M4 failed condition] | scja1-part3-div3-sicc.l4:460 "such powers as the General Division may exercise in its original civil jurisdiction" |
| `s 18J(4) the court is the General Division for the purposes of section 18J` | scja1-part3-div3-sicc.l4:486 "In this section, “General Division” does not include the Singapore International Commercial Co [M5 flat negative] | none |
| `s 18J(1) the Singapore International Commercial Court may transfer the case to the General Division` | none | scja1-part3-div3-sicc.l4:500 "a case commenced in that Court"<br>scja1-part3-div3-sicc.l4:502 "in accordance with the Rules of Court" |
| `s 18J(2) the General Division may transfer the case to the Singapore International Commercial Court` | none | scja1-part3-div3-sicc.l4:514 "a case commenced in the General Division"<br>scja1-part3-div3-sicc.l4:516 "in accordance with the Rules of Court" |
| `s 18J(3)(a) the court to which the case is transferred may permit a matter that has been adduced to remain in evidence` | scja1-part3-div3-sicc.l4:534 "Where a case is transferred under subsection (1) or (2)" [M4 failed condition] | none |
| `s 18J(3)(b) the courts may make the consequential order` | scja1-part3-div3-sicc.l4:542 "Where a case is transferred under subsection (1) or (2)" [M4 failed condition] | scja1-part3-div3-sicc.l4:544 "in accordance with the Rules of Court" |
| `s 18M the party may be represented by the foreign lawyer or law expert` | none | scja1-part3-div3-sicc.l4:627 "A party to a case in the Singapore International Commercial Court, or to an appeal from that C<br>scja1-part3-div3-sicc.l4:628 "a foreign lawyer or law expert who is registered in accordance with Part 4B of the Legal Profe<br>scja1-part3-div3-sicc.l4:630 "may in accordance with the Rules of Court be represented" |
| `s 19 the appellate criminal jurisdiction of the General Division consists of hearing the matter` | none | scja1-part3-div4.l4:50 "before one or more Judges according to the provisions of the law for the time being in force r<br>scja1-part3-div4.l4:53 "before one or more Judges according to the provisions of the law for the time being in force r |
| `s 21(1)(a) the amount in dispute or the value of the subject matter does not exceed the sum` | scja1-part3-div4.l4:104 "does not exceed $60,000 or such other amount as may be specified by an order made under subsec [M5 flat negative]<br>scja1-part3-div4.l4:107 "does not exceed $60,000" [M5 flat negative] | none |
| `s 21(1) an appeal lies to the General Division from the decision` | scja1-part3-div4.l4:135 "an appeal lies to the General Division from a decision of a District Court or Magistrate's Cou [M4 failed condition] | scja1-part3-div4.l4:132 "a decision of a District Court or Magistrate's Court"<br>scja1-part3-div4.l4:136 "in the following cases"; outside (a) and (b) the subsection does not say whether an appeal lie |
| `s 21(1) permission is needed to appeal from the decision` | none | scja1-part3-div4.l4:149 "in the following cases" |
| `s 21(2A) the order is final` | none | scja1-part3-div4.l4:160 "An order of the General Division giving or refusing permission under subsection (1)" |
| `s 21(3) the President may vary the amount mentioned in section 21(1)` | none | scja1-part3-div4.l4:173 "The President may, after consulting the Chief Justice, by order in the Gazette, vary the amoun |
| `s 22(1) the appeal is by way of rehearing` | none | scja1-part3-div4.l4:186 "All appeals to the General Division in the exercise of its appellate civil jurisdiction" |
| `s 22(2) the General Division has the power or duty` | none | scja1-part3-div4.l4:199 "In hearing and deciding an appeal, the General Division has all the powers and duties ... of t |
| `s 22(3) the General Division may receive further evidence in this manner` | none | scja1-part3-div4.l4:228 "in any other manner as the court may allow" |
| `s 22(4) the further evidence may be given to the General Division` | scja1-part3-div4.l4:245 "only with the permission of the General Division and on special grounds" [M4 failed condition] | none |
| `s 22(5) the further evidence may be given to the General Division without permission` | scja1-part3-div4.l4:258 "if the evidence relates to matters occurring after the date of the decision appealed against" [M4 failed condition] | none |
| `s 22(7)(a) the power may be exercised in relation to any part of the decision appealed against` | none | scja1-part3-div4.l4:287 "The powers in this section" |
| `s 22(7)(b) the power may be exercised in favour of any party to the decision appealed against` | none | scja1-part3-div4.l4:295 "The powers in this section" |
| `s 22A(2) section 22A(1) allows this part of the proceeding to be conducted without an oral hearing` | scja1-part3-div4.l4:310 "does not allow any part of a proceeding where oral evidence is given ... to be conducted witho [M4 failed condition/M5 flat negative] | scja1-part3-div4.l4:308 "any part of a proceeding where oral evidence is given" |
| `s 22A(1) the General Division may decide the matter without hearing oral arguments` | scja1-part3-div4.l4:325 "other than a matter prescribed by the Rules of Court or the Family Justice Rules" [M4 failed condition] | scja1-part3-div4.l4:324 "any matter in its appellate civil jurisdiction" |
| `s 22A(3) the General Division may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` | none | scja1-part3-div4.l4:340 "in any matter that the General Division may decide without hearing oral arguments" |
| `s 22A(4) the General Division must not hear the matter in an asynchronous manner` | scja1-part3-div4.l4:352 "if to do so would be inconsistent with the court's duty" [M4 failed condition] | none |
| `s 22A(5) section 22A affects the General Division's power to hear oral arguments before deciding the matter` | scja1-part3-div4.l4:381 "this section does not affect the power of the General Division to hear oral arguments" [M5 flat negative] | scja1-part3-div4.l4:382 "any matter that may be decided without hearing oral arguments" |
| `s 22B(1) the General Division may on its own motion summarily dismiss the appeal` | scja1-part3-div4.l4:424 "if it is satisfied of any of the following" [M4 failed condition] | scja1-part3-div4.l4:420 "any appeal to the General Division in the exercise of its appellate civil jurisdiction" |
| `s 23 the General Division may exercise powers of revision in the criminal proceedings` | none | scja1-part3-div5-6.l4:30 "criminal proceedings and matters in subordinate courts"<br>scja1-part3-div5-6.l4:32 "criminal proceedings and matters"<br>scja1-part3-div5-6.l4:34 "in accordance with the provisions of any written law for the time being in force relating to c |
| `s 24 the General Division may call for and examine the record of the civil proceedings` | none | scja1-part3-div5-6.l4:53 "any civil proceedings before any subordinate court"<br>scja1-part3-div5-6.l4:55 "any civil proceedings"<br>scja1-part3-div5-6.l4:57 "for the purpose of satisfying itself as to the correctness, legality or propriety of any decis |
| `s 25 the General Division may give such orders on the civil proceedings, including directing a new trial` | none | scja1-part3-div5-6.l4:77 "any civil proceedings in a subordinate court"<br>scja1-part3-div5-6.l4:79 "any civil proceedings"<br>scja1-part3-div5-6.l4:80 "the record of which has been called for, or which otherwise comes to its knowledge"<br>scja1-part3-div5-6.l4:82 "such orders ... as seem necessary to secure that substantial justice is done" |
| `s 26 the section applies to the civil matter` | scja1-part3-div5-6.l4:98 "Where an appeal lies from any decision in any civil matter, and no appeal is brought" [M4 failed condition/M5 flat negative] | none |
| `s 26 a proceeding by way of revision may be entertained at the instance of the party` | scja1-part3-div5-6.l4:108 "no proceeding by way of revision is to be entertained at the instance of a party who could hav [M4 failed condition] | scja1-part3-div5-6.l4:109 "at the instance of a party who could have appealed"; the section grants nothing |
| `s 27(1) the General Division has general supervisory and revisionary jurisdiction over the court` | none | scja1-part3-div5-6.l4:126 "over all subordinate courts" |
| `s 27(2) the General Division may take the step in the matter or proceeding` | scja1-part3-div5-6.l4:154 "if it appears desirable in the interests of justice" [M4 failed condition] | scja1-part3-div5-6.l4:152 "in any subordinate court" |
| `s 27(3) the proceedings in the subordinate court are stayed` | scja1-part3-div5-6.l4:168 "Upon the General Division calling for any record under subsection (2)" [M4 failed condition]<br>scja1-part3-div5-6.l4:169 "pending further order of the General Division" [M4 failed condition] | none |
| `s 27(4) the General Division is to have regard to whether the matter was or could reasonably have been raised in the appeal` | scja1-part3-div5-6.l4:188 "when exercising (or deciding whether to exercise) ... in relation to any matter which concerns [M4 failed condition] | none |
| `s 28(1) the party has a right to be heard before the General Division` | scja1-part3-div5-6.l4:223 "no party has any right to be heard before the General Division" [M5 flat negative] | scja1-part3-div5-6.l4:221 "when exercising its powers of supervision and revision" |
| `s 28(2) the final order may be made to the prejudice of the person` | scja1-part3-div5-6.l4:236 "No final order may be made to the prejudice of any person unless that person has had an opport [M4 failed condition] | scja1-part3-div5-6.l4:234 "No final order may be made to the prejudice of any person"<br>scja1-part3-div5-6.l4:235 "unless that person has had an opportunity of being so heard" lifts the bar; the subsection gra |
| `s 28(2) the bar on a final order made to the prejudice of the person applies` | scja1-part3-div5-6.l4:246 "unless that person has had an opportunity of being so heard" [M4 failed condition] | scja1-part3-div5-6.l4:245 "No final order may be made to the prejudice of any person" |
| `s 28A(1) the Chief Justice may by order direct the class of proceedings to be heard and determined by the District Court or Family Court` | scja1-part3-div5-6.l4:272 "where he or she considers it necessary or expedient to improve efficiency" [M4 failed condition] | none |
| `s 28A(2) an order under section 28A(1) may make the provision` | none | scja1-part3-div5-6.l4:314 "any order under subsection (1)"<br>scja1-part3-div5-6.l4:322 paragraph (a) is for the proceedings it names; the paragraphs have no "only" |
| `s 29 an appeal cannot be brought against the decision` | none | scja1-part3-div7-9.l4:51 "a decision of the General Division made in the exercise of its original or appellate civil jur |
| `s 29A(1)(b) the amount in dispute or value of the subject matter does not exceed the sum` | scja1-part3-div7-9.l4:77 "does not exceed $250,000 or such other sum as may be specified by an order made under subsecti [M5 flat negative]<br>scja1-part3-div7-9.l4:80 "does not exceed $250,000" [M5 flat negative] | none |
| `s 29A(1) permission is required before an appeal may be brought against the decision` | none | scja1-part3-div7-9.l4:110 "a decision of the General Division made in the exercise of its original or appellate civil jur |
| `s 29A(2) permission must be obtained from this court` | scja1-part3-div7-9.l4:145 "permission must be obtained ... from the specified court" / "from the court specified in the F [M4 failed condition] | none |
| `s 29A(3) the President may specify another sum in substitution of the sum mentioned in section 29A(1)(b)` | none | scja1-part3-div7-9.l4:160 "The President may, after consulting with the Chief Justice, by order in the Gazette, specify a |
| `s 29B(1) this section applies to the decision` | scja1-part3-div7-9.l4:178 "after any hearing other than a trial of an action" [M4 failed condition] | scja1-part3-div7-9.l4:176 "a decision made ... in the exercise of the original or appellate civil jurisdiction of the Gen<br>scja1-part3-div7-9.l4:177 "a decision made by a Judge" |
| `s 29B(2) the request for further arguments is made before the earlier of the following` | scja1-part3-div7-9.l4:224 "before the earlier of the following: ... (b) the 15th day after the date on which the decision [M4 failed condition]<br>scja1-part3-div7-9.l4:232 "before the earlier of the following: (a) the time at which the judgment or order relating to t [M4 failed condition] | none |
| `s 29B(2) other reading: the request is made on or before the 15th day after the date on which the decision is made` | scja1-part3-div7-9.l4:244 "(b) the 15th day after the date on which the decision is made" [M4 failed condition]<br>scja1-part3-div7-9.l4:252 "(a) the time at which the judgment or order relating to the decision is extracted" [M4 failed condition] | none |
| `s 29B(2) the Judge who made the decision may hear further arguments in respect of the decision` | scja1-part3-div7-9.l4:266 "after any hearing other than a trial of an action" [M4 failed condition]<br>scja1-part3-div7-9.l4:268 "Before any notice of appeal is filed against a decision to which this section applies" [M4 failed condition]<br>scja1-part3-div7-9.l4:269 "if any party to the hearing, or the Judge, requests for further arguments" [M4 failed condition] | scja1-part3-div7-9.l4:267 "a decision to which this section applies" |
| `s 29B(3) the Judge may take the step` | scja1-part3-div7-9.l4:288 "After hearing further arguments, the Judge may affirm, vary or set aside the decision" [M4 failed condition] | none |
| `s 29B(4) this subsection applies` | scja1-part3-div7-9.l4:315 "If a request for further arguments has been made under subsection (2)" [M4 failed condition] | none |
| `s 29B(4)(a) a notice of appeal may not be filed against the decision yet` | scja1-part3-div7-9.l4:326 "If a request for further arguments has been made under subsection (2)" [M4 failed condition]<br>scja1-part3-div7-9.l4:327 "until the Judge (i) affirms, varies or sets aside the decision after hearing further arguments [M4 failed condition]<br>scja1-part3-div7-9.l4:328 "until the Judge ... (ii) certifies, or is deemed to have certified, that no further arguments  [M4 failed condition] | none |
| `s 29B(4)(b) the date on which the time for filing a notice of appeal begins` | none | scja1-part3-div7-9.l4:340 "If a request for further arguments has been made under subsection (2)" |
| `s 29B(5) a party to the hearing may request further arguments before filing a notice of appeal` | none | scja1-part3-div7-9.l4:359 "a party to the hearing" |
| `s 29B(5) a party to the hearing is required to request further arguments before filing a notice of appeal` | scja1-part3-div7-9.l4:366 "may, but is not required to, request for further arguments" [M5 flat negative] | scja1-part3-div7-9.l4:367 "a party to the hearing" |
| `s 29C(1) the appeal is to be made to the Appellate Division` | scja1-part3-div7-9.l4:383 "Subject to subsection (2)" [M4 failed condition] | scja1-part3-div7-9.l4:388 "an appeal against a decision of the General Division in the exercise of its original or appell |
| `s 29C(2) the appeal is to be made to the Court of Appeal` | scja1-part3-div7-9.l4:407 "if the Sixth Schedule or any other written law so provides" [M4 failed condition] | scja1-part3-div7-9.l4:405 "an appeal against a decision of the General Division" |
| `s 29C the court to which the appeal is to be made` | none | scja1-part3-div7-9.l4:422 s 29C(1) names the Appellate Division only for an appeal against a decision of the General Divi |
| `s 29C(3) section 29C creates a right of appeal against the decision` | scja1-part3-div7-9.l4:433 "this section does not create any right of appeal against a decision of the General Division" [M5 flat negative] | scja1-part3-div7-9.l4:434 "a decision of the General Division" |
| `s 29D(1) the Court of Appeal may transfer the appeal to itself` | scja1-part3-div7-9.l4:469 "where an order under section 39A of the Land Acquisition Act 1966 is in force, any appeal made [M4 failed condition] | none |
| `s 29D(2) the power in section 29D(1) may be exercised in this way` | scja1-part3-div7-9.l4:497 "such an application may only be made (i) on the ground that the appeal was not made to the App [M4 failed condition] | none |
| `s 29D(3) the Court of Appeal is to have regard to the matter` | scja1-part3-div7-9.l4:509 "In deciding whether to exercise the power in subsection (1)" [M4 failed condition] | none |
| `s 29D(5) the appeal may be transferred under section 29D(1) even though it was made in accordance with section 29C(1)` | none | scja1-part3-div7-9.l4:554 "even if it was made to the Appellate Division in accordance with section 29C(1)" |
| `s 29E(2) the power in section 29E(1) may be exercised in this way` | scja1-part3-div7-9.l4:606 "such an application may only be made on the ground that the appeal was not made to the Court o [M4 failed condition] | none |
| `s 29E(3) the Court of Appeal is to have regard to the matter` | scja1-part3-div7-9.l4:618 "In deciding whether to exercise the power in subsection (1)" [M4 failed condition] | none |
| `s 29E(5) the appeal may be transferred under section 29E(1) even though it was made in accordance with section 29C(2)` | none | scja1-part3-div7-9.l4:662 "even if it was made to the Court of Appeal in accordance with section 29C(2)" |

### Reading a result: FALSE and NOTHING (scja1)

Every rule here answers `JUST TRUE`, `JUST FALSE` or `NOTHING` (a `MAYBE BOOLEAN`), or a `MAYBE` number, date, court or Judge.
`JUST TRUE` and `JUST FALSE` are answers the Act gives in its own words; `NOTHING` means the Act does not answer on these facts and is **never** to be read as "No".

What a "no" is in this row: the text says no in its own words.
That is a definition that says "means" (the thing is not what the definition describes), a condition the text introduces with "if", "only if", "unless", "where", "when", "until" or "except" that is not met, a list the text closes with "only", or a flat negative ("shall not", "may not", "is not", "no appeal").
Examples: s 17A(1) ("the General Division has no jurisdiction") is `JUST TRUE` for a Syariah Court matter, and the question in the seat is worded so that `JUST TRUE` means "my case is outside the General Division's jurisdiction"; s 29 ("an appeal cannot be brought") is `JUST TRUE` for a case the section names, and `JUST TRUE` there means "an appeal cannot be brought".
Read the name of each rule: it says what `JUST TRUE` means.

What "not covered" is in this row: the Act is silent, names a list without closing it, uses a term it does not define, points to a Schedule, a rule, a regulation or another Act that is not among the sources, or limits a grant in its own wording and the case falls outside the limit.
Examples: a matter that is not one of the paragraphs of s 19 or s 20 (no "only"); a decision of the Singapore International Commercial Court in ss 29 to 29C (fork K1); a case with no amount or value in ss 21(1)(a) and 29A(1)(b) (fork K2); two Judges appointed on the same day in s 4 (fork K3); a Schedule question the person does not know (seams 1 to 8).
A caller must never turn `NOTHING` into `FALSE`.

Where a result is a number, a date, a court or a Judge and so cannot carry `JUST FALSE`, there is a yes/no twin that does:
- the court for an appeal: `s 29C the court to which the appeal is to be made` (a court or `NOTHING`), with twins `s 29C(1) the appeal is to be made to the Appellate Division` and `s 29C(2) the appeal is to be made to the Court of Appeal`;
- the day before which a request for further arguments must be made: `s 29B(2) the day before which ...` (a date), with the twin `s 29B(2) the request for further arguments is made before the earlier of the following`;
- the date the time for a notice of appeal begins: `s 29B(4)(b) ...` (a date), with the twin `s 29B(4)(a) a notice of appeal may not be filed against the decision yet`;
- the Judge who exercises the Chief Justice's powers (`s 5(1) the Judge who exercises ...`), with the twin `s 5(1) the powers and duties of the Chief Justice pass to the next Judge in precedence`;
- the number of Judges in s 10(1) is a plain `NUMBER` (one Judge unless the person states a number that a written law provides), so it carries neither `JUST FALSE` nor `NOTHING`; the yes/no question about a number is `s 18G the proceeding is to be heard and disposed of before this number of Judges, as the section requires`, which answers `NOTHING` for a number other than 1 or 3 (fork F7).

A bar ("until", "pending further order") is encoded as the bar and never as the thing having happened.
`s 29B(4)(a) a notice of appeal may not be filed against the decision yet` is `JUST TRUE` while the bar is in force (a request for further arguments has been made and the Judge has not yet affirmed, varied or set aside the decision, or certified that no further arguments are required) and `JUST FALSE` after the Judge acts, or where no request was made.
`s 27(3) the proceedings in the subordinate court are stayed` is `JUST TRUE` from the General Division's calling for the record until it makes a further order, and `JUST FALSE` before the call and after the further order.
No function says that the Judge or the court has done the act: the act is a fact the person states.

## Seams (scja1)

A seam is an input named for the section that answers it; the lead connects the input to the answering function at the merge.
The names below are the exact `GIVEN` names, as `PLAN.md` section "Seams" prints them.
Every seam whose answering section can say `NOTHING` is typed `MAYBE ...`, and the asking function passes `NOTHING` through: it never turns it into `JUST FALSE`.
Each asking function has at least one test whose expected value is `NOTHING` (counted by `grep` over the tests: s 18(2) 2, s 18I(1) 2, s 21(1) 3 and 3, s 29 5, s 29A(1) 7, s 29A(2) 1, s 29C 4, s 29C(2) 4).

### Seams I consume (PLAN.md rows 1 to 8), all typed as the plan types them

| # | asking section | input name (exact) | type | asked at |
| --- | --- | --- | --- | --- |
| 1 | s 18(2), (3) | `sch 1 the power is one set out in the First Schedule` | MAYBE BOOLEAN | `scja1-part3-div2-procedure.l4:193`, `scja1-part3-div2-procedure.l4:206` |
| 2 | s 18I(1)(a) | `sch 1 para 1 the power is the power under paragraph 1` | MAYBE BOOLEAN | `scja1-part3-div3-sicc.l4:453` |
| 3 | s 21(1)(b) | `sch 3 the decision is a case specified in the Third Schedule` | MAYBE BOOLEAN | `scja1-part3-div4.l4:126`, `scja1-part3-div4.l4:143` |
| 4 | s 29(b) | `sch 4 the Fourth Schedule says no appeal can be brought` | MAYBE BOOLEAN | `scja1-part3-div7-9.l4:46` |
| 5 | s 29A(1)(b) | `sch 5 an exception in the Fifth Schedule takes the case out of s 29A(1)(b)` | MAYBE BOOLEAN | `scja1-part3-div7-9.l4:104` |
| 6 | s 29A(1)(c) | `sch 5 the case is one specified in paragraph 3, 4(1) or 5(1) of the Fifth Schedule and no exception applies` | MAYBE BOOLEAN | `scja1-part3-div7-9.l4:105` |
| 7 | s 29A(2)(b) | `sch 5 the court from which permission must be obtained` | MAYBE Court | `scja1-part3-div7-9.l4:128`, `scja1-part3-div7-9.l4:139` |
| 8 | s 29C(2) | `sch 6 the appeal is to be made to the Court of Appeal` | MAYBE BOOLEAN | `scja1-part3-div7-9.l4:378`, `scja1-part3-div7-9.l4:398`, `scja1-part3-div7-9.l4:413` |

In the seat layer a Schedule question is asked of the person as "Yes / No / I am not sure"; "I am not sure" reaches the seam input as `NOTHING`.
The seat does not answer any Schedule.

### Seams I answer (PLAN.md rows 9, 10, 12, 13)

| # | answering function (exact name) | type | defined at |
| --- | --- | --- | --- |
| 9 | `s 29C the court to which the appeal is to be made` | MAYBE Court | `scja1-part3-div7-9.l4:416` |
| 10 | `s 29A(1)(b) the amount in dispute or value of the subject matter does not exceed the sum` | MAYBE BOOLEAN | `scja1-part3-div7-9.l4:70` |
| 12 | `s 4 the most senior Supreme Court Judge among those sitting` | MAYBE Judge | `scja1-part2-court.l4:84` |
| 13 | `s 10A the court may summon assessors`, with `the court` as an input of type `Court`, so the lead can call it with `Appellate Division` and `Court of Appeal` | MAYBE BOOLEAN | `scja1-part3-div1.l4:175` |

### Seam 11 (s 8A(6)), and seams the plan lacks

- **Seam 11.** `s 8A(6)` asks `s 34(1)(a) or s 52(1)(a) the place is one the Chief Justice appointed` (MAYBE BOOLEAN) for the Appellate Division and the Court of Appeal, as the plan says (asked at `scja1-part2-hearings.l4:436`).
  For the General Division it asks a second input, `s 11(1) the place is one the Chief Justice appointed for the General Division` (MAYBE BOOLEAN), which the plan does not name; the lead can connect it to `s 11(1) the General Division sits at the time and place`, which is in this range, defined at `scja1-part3-div1.l4:280`.
- **Rows 19 and 20** (the facts `s 29E(1) the appeal was transferred to the Appellate Division`, `s 29D(1) the Court of Appeal declined to transfer the appeal to itself` and `s 29D(1) the appeal was transferred to the Court of Appeal`) are facts that scja2 takes as `BOOLEAN` inputs.
  scja1 defines no function with those names: they are facts a party can state, and a function named that way would claim to decide whether the transfer happened, which ss 29D and 29E do not say.
  What ss 29D and 29E do answer is `s 29D(1) the Court of Appeal may transfer the appeal to itself` and `s 29E(1) the Court of Appeal may transfer the appeal to the Appellate Division`.
- **Seam the plan lacks: public holidays.** `s 10B(1)` and `s 29B(2)(b)` need to know which dates are public holidays; the Act does not list them, so they are a plain input (`the public holidays`, a list of dates, asked of the person), passed to the Interpretation Act module.
- **Seam the plan lacks: "every issue already decided".** The ground in `s 17C(1)(a)` and `s 22B(1)(b)` is a plain `BOOLEAN` input with the label of its own section, as `PLAN.md` difficulty 7 directs; `NEEDS-CORE.md` suggests hoisting it.
- **Other Acts not staged.** The Administration of Muslim Law Act 1966 and the Women's Charter 1961 (s 17A), the Broadcasting Act 1994 and the Newspaper and Printing Presses Act 1974 (s 8(7)), the Mediation Act 2017 and the Singapore Convention on Mediation Act 2020 (s 17(2)), the Companies Act 1967 and the Insolvency, Restructuring and Dissolution Act 2018 (s 18D(2)(c)) and the Criminal Procedure Rules are asked as plain borrowed facts, named for the section that borrows them.

## Dependencies

| module | Commons path | blob | what I used |
| --- | --- | --- | --- |
| `sgia-interpretation-time.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4` (Commons main d468311a6) | fe60ab2c1f2326a5b061e163761bd63e4f47e12a | Interpretation Act 1965 s 50: `the last day of a period of days from the event` counts the 15th day in `s 29B(2)` (the day of the event is not counted, and a last day that is a Sunday or public holiday moves to the next day that is not one); `is a Sunday` finds the Sundays (and, by the day before, the Saturdays) in `s 10B(1)` |

The copy in this folder is byte-identical to the staged copy (checked with `cmp`), and keeps its three-line header naming the Commons path and blob; I did not edit it.
The staged copy carries that header, so `git hash-object` on it gives a different value from the blob above (the staged-modules note says the same).
I passed `FALSE` for the module's "contrary intention" argument everywhere: the Act gives no sign of one.
No rule of the Supreme Court of Judicature Act overrides the Interpretation Act's counting for the period I use; the Rules of Court, which count their own periods, are outside the sources.
`sgia-p1-definitions.l4` was staged and I did not need it; I took no other Act as a module and asked each borrowed fact as a plain input (section "Seams (scja1)").
The key `"dependencies"` of `encoding.json` is the lead's to write; the row above is what it should list.

## Unstable dialect

I looked at time (the 15th-day count in `s 29B(2)`, the date cuts `s 17A(3A)` and `s 18D(2)(c)`, the sittings of `s 10B`), versions (the Act is one consolidation in force from 1 July 2024, with no two vintages to merge) and workarounds (`s 8A(3)` and the eight other regulative rules, which `#TRACE` can run but not assert, and for which each has a decision twin) in `scja1-part3-div7-9.l4`, `scja1-part3-div2-jurisdiction.l4`, `scja1-part3-div1.l4` and the regulative rules; I found no shape that earns a second encoding.

## What the text turns out to say (numbered findings)

1. **The Act sets almost no time limit a party can count.**
   In my range the periods are the 15th day in `s 29B(2)(b)`, the 2 months a year in `s 7` (a limit on the Chief Justice's power to specify vacations), and two date cuts (`s 17A(3A)`: registered before 1 March 2009; `s 18D(2)(c)`: the Companies Act 1967 as in force before 30 July 2020).
   The time for filing a notice of appeal is not in the Act: `s 29B(4)(b)` says only when that time "begins".
2. **Two sections are written as negatives, so `JUST TRUE` means no.**
   `s 17A(1)` ("the General Division has no jurisdiction") and `s 29` ("an appeal cannot be brought") are `JUST TRUE` when the case is inside them, and the function names and the seat questions say so.
   `s 10(5)` is written the same way: `s 10(5) the Judge must not sit ...` is `JUST TRUE` when the bar applies, and its twin `s 10(5) the Judge may sit ...` asks the grant (fork F15).
3. **The money tests say "does not exceed", so permission is needed in the smaller cases.**
   `s 21(1)(a)` ($60,000) and `s 29A(1)(b)` ($250,000) require permission where the amount "does not exceed" the figure.
   A larger case under that limb is not a "no permission needed" in the text: `s 21(1)` says an appeal lies "only with the permission ... in the following cases", and outside (a) and (b) it says nothing, so the answer is `NOTHING` (fork F14); the seat's "do I need permission?" questions say what that means for the person.
4. **Further evidence on appeal needs no permission if it concerns matters after the decision.**
   `s 22(5)`; otherwise `s 22(4)` requires both permission and special grounds, and I read "Except as provided in subsection (5)" as lifting both (fork F11).
5. **An oral hearing is protected only where oral evidence is given.**
   `s 17B(2)` and `s 22A(2)` say the power to decide without oral arguments does not allow any part of a proceeding where oral evidence is given to be conducted without an oral hearing, unless all the parties consent; they say nothing where no oral evidence is given.
   Asked what section 17B(1) or 22A(1) allows, a met "unless all the parties consent" is `JUST TRUE`; asked as a grant, as `s 28(2)` is, a met "unless" is `NOTHING` and a twin asks the bar (fork F16).
6. **The civil limb of the audio-link ban has a consent exception and the criminal limb does not.**
   `s 8A(3)(b)` ("unless all the parties consent") against `s 8A(3)(a)`.
7. **A request for further arguments has two clocks.**
   `s 29B(2)` runs to "the earlier of" the extraction of the order and the 15th day; the core records the extraction as a date, and the Act speaks of its time, so a request on the day of extraction is `NOTHING`.
8. **The Appellate Division is the default court for an appeal from a civil decision of the General Division.**
   `s 29C(1)`; the Court of Appeal only "if the Sixth Schedule or any other written law so provides" (`s 29C(2)`); and `ss 29D` and `29E` let the Court of Appeal transfer an appeal either way.
   A Sixth Schedule answer of `JUST TRUE` decides `s 29C(2)` for a decision of the Singapore International Commercial Court too; without it, such a decision stays `NOTHING` (fork K1).
9. **A two-Judge Singapore International Commercial Court bench that divides dismisses the contested claim.**
   `s 18H(6)(b)`: different opinions on any claim, counterclaim or application mean that claim, counterclaim or application is dismissed.
10. **The deemed terms of a jurisdiction agreement apply only if the agreement is silent.**
    `s 18F(2)`: subsection (1)(a), (b) and (c) apply "only if there is no express provision to the contrary in the agreement".
11. **The General Division loses jurisdiction over some Syariah Court matters and stays others.**
    `s 17A(1)` removes the civil proceedings on matters within the Syariah Court's jurisdiction under `s 35(2)(a)`, (b) or (c) of the Administration of Muslim Law Act 1966 where all the parties are Muslims or were married under the Muslim law.
    `s 17A(2)` keeps the jurisdiction any written law vests in the General Division over maintenance, custody and property on divorce where the matter falls under `s 35(2)(d)` or (e), 51 or 52(3)(c) or (d).
    `s 17A(3)` stays custody and property-on-divorce proceedings after a Syariah Court divorce event, unless a certificate has been filed.
12. **No revision at the instance of a party who could have appealed and did not.**
    `s 26`.
13. **An International Judge "may only sit" in the Singapore International Commercial Court, in an appeal from it, and in an application relating to such an appeal.**
    `s 5A`: outside those, the answer is `JUST FALSE`.
14. **Three subsections are shown deleted and four sections repealed.**
    `s 10(3)`, `s 21(2)` and `s 21(2B)` are shown "[Deleted by Act ...]"; ss 9, 12, 18E and 28B are shown "[Repealed by Act ...]"; each is a coverage row with that disposition.
15. **`s 22(6)` is stated with no limit.**
    "The General Division may draw any inference of fact, give any judgment and make any order" names no limit and sits in a section on appeals.
16. **The Act says nothing on four small points a litigant would ask.**
    A bare "must", "is to be" or "is to appoint" (ss 11(2), 17C(2), 18G, 18H(2), 18I(2), 22B(2)) names no consequence for non-compliance (fork F7); `s 10(1B)` does not say how fewer than 3 Judges, or an even split, decide; `s 18H(3)` does not say what happens without a majority; and the Act does not list the public holidays.

### What the text does not answer (for the final report)

- how long a party has to file a notice of appeal (the Rules of Court, outside the sources; `s 29B(4)(b)` says only when that time "begins");
- the filing fee for a case in the Singapore International Commercial Court (silent in this part);
- the short title (`s 1`) and the Court's seal (`s 6`): inert machinery (coverage reason 2), no question a litigant can ask of them;
- whether a person who is not a Judge, such as a District Judge, is a "Judge" under `s 2`: the core's `Kind of Judge` (`scja-core.l4`) has no member for such a person, so the `JUST FALSE` branch of `s 2 Judge` cannot be reached from a `Judge` record (see `NEEDS-CORE.md`);
- whether a transfer to the Appellate Division can be made on a reference by the Appellate Division (`s 29E(2)`: the `way` type has two members, own motion and an application by a party; `s 29D(2)(b)` has the reference for the opposite transfer);
- how a weekday in a vacation fits `s 10B(1)` and `(2)` (fork F18);
- whether a case in no limb of "in the following cases" (`ss 21(1)`, `29A(1)`) needs permission (fork F14);
- whether a division of the Supreme Court is a "subordinate court" (fork F4);
- whether "General Division" in ss 29 to 29C includes the Singapore International Commercial Court (fork K1);
- what a case with no amount or value counts as (fork K2);
- the order of two Judges appointed on the same day, or of two holders of a single office (fork K3);
- whether the court will use the power in `s 8(2AB)` (fork F5);
- what follows non-compliance with a bare "must" (fork F7);
- how fewer than 3 Judges, or an even split, decide (`s 10(1B)`), and what `s 18H(3)` does without a majority;
- whether a request for further arguments made on the day of extraction is in time (`s 29B(2)`);
- every Schedule question (seams 1 to 8, scja3) and which dates are public holidays.

## What the main binary does not accept

The binary governs where a skill describes a construct main rejects.
These are what I met on main 1.6.109, each loud (an error) unless marked silent:

- **`NOT EQUALS` is not an operator.** Write `NOT (a EQUALS b)`; also `NOT ((a PLUS b) EQUALS 2)`. Loud.
- **`means` is a keyword**, so a `GIVEN` cannot be named `means`. Loud. In a test fixture a `GIVEN` named `court` clashed with the core's `Bench` field of that name, and I renamed it `lower court`. Loud.
- **`Rec OF a, b` is greedy.** `Decision OF ... Order OF a, b` took the wrong arity until the nested constructor and each `(Date ...)` argument were bracketed. Loud.
- **A compared call must be bracketed:** `#ASSERT (f x) EQUALS JUST TRUE`. Without the brackets the type-checker reports a `MAYBE` where a `BOOLEAN` was expected. Loud.
- **A bare `CONSIDER` inside a `BRANCH` arm is invalid.** Write `IF ... ELSE` with the `CONSIDER` nested in the `ELSE`. Loud.
- **`#TRACE` needs a `WITH` clause.** Loud.
- **A regulative rule cannot be asserted.** `#TRACE` prints `BREACH`, `FULFILLED` or a residual obligation, but no assertion line, so `check.sh` does not count it and an `#ASSERT` cannot state it. Silent for `check.sh`. Each regulative rule (ss 8A(3), 17A(3), 17B(4), 17C(2), 22A(4), 22B(2), 27(4), 29D(3), 29E(3)) has a decision twin that is asserted, and the trace outcomes were read from the output of both builds: 27 traces, and the `FULFILLED` / `BREACH` / residual lines are the same on 1.6.109 and 1.6.108 (compared by hashing those lines per file).
- **`REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used** (except `LEST BREACH ... BECAUSE`, which is accepted); "not covered" is `NOTHING`.
- **`YMD` is not defined here**; dates are `Date day month year`.

Accepted on main and not a problem: forward references between top-level rules; parentheses inside a backtick name; a vertical `LIST`.

## What check.sh prints

The baseline it replaced, from the supplied folder before my files: 1 module (`scja-core.l4`), 0 errors, 0 satisfied, 0 failed, 0 refused.
With my files it prints this (run in the folder with `L4=<main 1.6.109> L4_MAIN=<main 1.6.108> ./check.sh`; the 24 modules are the core, the 22 `scja1-*.l4` files and the Interpretation Act copy):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
scja-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
scja1-cases-seat.l4                            0       172       0        0         0 |      0       172       0        0  same
scja1-part1-preliminary.l4                     0         0       0        0         0 |      0         0       0        0  same
scja1-part2-court.l4                           0         0       0        0         0 |      0         0       0        0  same
scja1-part2-hearings.l4                        0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div1.l4                            0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div2-jurisdiction.l4               0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div2-procedure.l4                  0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div3-sicc.l4                       0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div4.l4                            0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div5-6.l4                          0         0       0        0         0 |      0         0       0        0  same
scja1-part3-div7-9.l4                          0         0       0        0         0 |      0         0       0        0  same
scja1-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
scja1-tests-part1-preliminary.l4               0        61       0        0         0 |      0        61       0        0  same
scja1-tests-part2-court.l4                     0        57       0        0         0 |      0        57       0        0  same
scja1-tests-part2-hearings.l4                  0        87       0        0         0 |      0        87       0        0  same
scja1-tests-part3-div1.l4                      0        88       0        0         0 |      0        88       0        0  same
scja1-tests-part3-div2-jurisdiction.l4         0        94       0        0         0 |      0        94       0        0  same
scja1-tests-part3-div2-procedure.l4            0        30       0        0         0 |      0        30       0        0  same
scja1-tests-part3-div3-sicc.l4                 0       123       0        0         0 |      0       123       0        0  same
scja1-tests-part3-div4.l4                      0        91       0        0         0 |      0        91       0        0  same
scja1-tests-part3-div5-6.l4                    0        69       0        0         0 |      0        69       0        0  same
scja1-tests-part3-div7-9.l4                    0       162       0        0         0 |      0       162       0        0  same
sgia-interpretation-time.l4                    0         0       0        0         0 |      0         0       0        0  same
TOTAL (24 modules)                             0      1034       0        0           |      0      1034       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit status: 0
```

The 1034 assertions are 862 in the ten layer-1 test files and 172 in `scja1-cases-seat.l4`; in every file the number written equals the number satisfied, and no assertion fails or is refused.

`srcrefs.py`, run over the 22 `scja1-*.l4` files:

```
$ python3 -I srcrefs.py check --refs SCJA1969.txt scja1-*.l4
srcrefs check: 979 src: lines, 172 runs, 213 locators, 0 problems
$ python3 -I srcrefs.py check --strict SCJA1969.txt scja1-*.l4
srcrefs check: 979 src: lines, 172 runs, 213 locators, 0 problems
```

Nothing here claims more than those counts.
`check.sh` does not see a different `#TRACE` outcome; I compared those by hand as described above.
