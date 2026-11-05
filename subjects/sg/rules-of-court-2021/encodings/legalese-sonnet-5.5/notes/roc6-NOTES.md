# NOTES (roc6): Rules of Court 2021, Orders 23 to 27

Singapore, Rules of Court 2021 (G.N. No. S 914/2021), current version as at 5 November 2026.
Range: lines 3556 to 4193 of `SCJA1969-S914-2021.txt`: Order 23 (Contempt of court), Order 24 (Prerogative orders), Order 24A (Post-appeal applications in capital cases), Order 25 (Court fees), Order 26 (Registry and administration), Order 27 (Lodgment in Court, money in Registry and payment to Sheriff).
Target: the `main` dialect, built and checked on 1.6.109, cross-checked on 1.6.108 (the main column of `check.sh`).

**Status, and how each claim in this file was checked.**
The encoding of the range is complete as described below.
Checked by running: `check.sh` on both main builds (its output is at the end of this file), `srcrefs.py check --refs` and `--strict` over every `roc6-*.l4` file, `l4 check` on each file, and a comparison of the `#TRACE` outcomes of the five test files that hold traces between the two builds (identical).
The counts in the file, coverage, fork-row and marginal-reading tables were computed from the files by the script that wrote this file; the figures in the findings come from the commands named beside them.
This file describes the encoding after a second pass that followed an independent test pass; `### What the second pass changed` (under Findings) lists what moved, so that a later editor does not undo it.
The text is a converter rendering of the Rules (it carries 262 no-break spaces and 56 non-breaking hyphens on the 638 lines of this range, and writes lettered paragraphs as `( a )` on lines of their own), not the official PDF; nothing here was checked against the official text.
The layer-1 modules cite the text by `@ref LABEL (src:N-M)` over mechanically quoted `-- src:N | ...` lines; the quotes were produced from the raw file, not typed.

**Where `PLAN.md` and the brief differ, the brief governs.**
On periods the two now agree: a period the text fixes in its own words answers `JUST FALSE` outside it (Meng's ruling of 2026-11-05 (a); `PLAN.md` section 2 and its difficulty 10 say so).
I followed it: 38 branches carry a `ruling of 2026-11-05 (a)` comment, and 59 carry `(b)` for a "where ..." or "if" condition that fails.
No difference between the two documents changed an answer in this range.

## Files

| file | what it is | lines | assertions |
| --- | --- | --- | --- |
| `roc6-order-23.l4` | layer 1, Order 23 | 1245 |  |
| `roc6-order-24.l4` | layer 1, Order 24 | 665 |  |
| `roc6-order-24a.l4` | layer 1, Order 24A | 582 |  |
| `roc6-order-25.l4` | layer 1, Order 25 | 772 |  |
| `roc6-order-26.l4` | layer 1, Order 26 (imports `roc-definitions`) | 323 |  |
| `roc6-order-27.l4` | layer 1, Order 27 | 950 |  |
| `roc6-seat.l4` | layer 2, the seat (39 `@export` questions) | 408 |  |
| `roc6-cases-seat.l4` | cases for the seat | 130 | 103 |
| `roc6-tests-order-23.l4` | tests for Order 23 (7 `#TRACE`) | 424 | 302 |
| `roc6-tests-order-24.l4` | tests for Order 24 (5 `#TRACE`) | 277 | 166 |
| `roc6-tests-order-24a.l4` | tests for Order 24A (4 `#TRACE`) | 229 | 142 |
| `roc6-tests-order-25.l4` | tests for Order 25 (3 `#TRACE`) | 291 | 210 |
| `roc6-tests-order-26.l4` | tests for Order 26 (0 `#TRACE`) | 123 | 78 |
| `roc6-tests-order-27.l4` | tests for Order 27 (4 `#TRACE`) | 369 | 273 |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file; progress; two things the core lacks | | |

The seat is a party to a civil action in the Singapore courts (a claimant, a defendant, a third party or an appellant).
Every seat question is `@export`ed with an `@desc` on each input, named "Under Order N, rule M, ...", grouped under a `§` heading per Order in text order, and takes plain inputs: yes or no, a number, a date, a word, or a choice from a list.
A period is asked as "the last day for this", a DATE counted by Order 3, Rule 3 (another part's rule, taken as an input: see Seams).
There is no seat for an official; the rules that address only the Registrar, the Accountant-General, the Sheriff or the Chief Justice are in layer 1 and have no question.

## Coverage (roc6)

**Audit counts.**
The range has 638 lines, all non-blank.
`work/units.py` read the raw lines and counted **523 text units** (a unit is a heading, a rule, a paragraph, a lettered paragraph, a roman sub-paragraph, a capital-letter sub-sub-paragraph or a defined term): 69 headings (6 Orders and 63 rules), 22 rules with no numbered paragraph, 199 numbered paragraphs, 140 lettered paragraphs, 61 roman sub-paragraphs, 8 capital-letter sub-sub-paragraphs and 24 defined terms.
Rows in this table when first drafted from the units: **523**. Rows after checking every one of the 638 lines against the rows (each line falls inside at least one row; none is left over): **523**. No row was added or removed by the line check.

**Counts by disposition** (one disposition per row):

| disposition | rows |
| --- | --- |
| `encoded` | 361 |
| `fork` | 92 |
| `inert`, reason 1 (not operative: the Order headings and the rule headings) | 69 |
| `inert`, reason 2 (machinery: O 26 r 5(2)) | 1 |
| `inert`, reason 3 (text shown repealed or blank) | 0 |
| `repealed or blank in this text` | 0 |
| total | 523 |

The 92 `fork` rows are split among F-ASSUMED (13), F-MUST (24), F-O23-1 (5), F-O23-2 (6), F-O23-3 (1), F-O24-1 (4), F-O24-2 (5), F-O24A-1 (2), F-O24A-2 (1), F-O24A-3 (9), F-O25-1 (6), F-O25-2 (5), F-O25-3 (1), F-O26-1 (1), F-O27-1 (1), F-O27-2 (2), F-O27-3 (1), F-O27-4 (1), F-TIMED (7), F-UNSURE (8) (a row can carry more than one fork id, so these figures add to more than 92); each points at its entry in the fork register and at the function that carries the reading taken.

**What the columns mean.**
`lines` are the raw line numbers of the unit.
`where` is the layer-1 function, constant or type that carries the unit; a paragraph with sub-paragraphs shares its sub-paragraphs' functions, and a sub-paragraph with no function of its own points at its nearest parent's.
`asserts` counts the assertions in the tests and the seat cases whose first call is one of the functions named; a function used only by its callers (a helper, a type, a constant) is counted through them, so such a row can read 0. 3 `encoded` rows read 0 here (O 26 r 4(1)(a)(i), O 26 r 4(1)(a)(ii), O 26 r 4(1)(a)(iii)): they point at the type `o 26 r 4(1)(a) how the execution of the document is verified`, which is exercised through `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court`.
The `provision` column quotes the first 90 characters of the unit from the raw file, with the no-break spaces turned into spaces and `|` turned into `/`.

| lines | provision | disposition | where | asserts |
| --- | --- | --- | --- | --- |
| 3556 to 3557 | O 23 heading: ORDER 23 | inert, reason 1 | | |
| 3558 | O 23 r 1 heading: Definitions of this Order (O. 23, r. 1) | inert, reason 1 | | |
| 3559 | O 23 r 1: In this Order, unless the context otherwise requires — “Act” means the Administration of J... | encoded | `o 23 r 1 "Act" is the Administration of Justice (Protection)`; `o 23 r 1 "committal applicant" is the person applying for or`; `o 23 r 1 "committal respondent" is the person against whom a`; ... (7 names) | 17 |
| 3559 | O 23 r 1 “Act”: In this Order, unless the context otherwise requires — “Act” means the Administration of J... | encoded | `o 23 r 1 "Act" is the Administration of Justice (Protection) Act 2016`; `o 23 r 1 "contempt of court" is contempt under the Act, and includes contempt under the common law`; `o 23 r 1 "section" is a section of the Act` | 9 |
| 3560 | O 23 r 1 “committal applicant”: “committal applicant” means the person who is applying for or has obtained a committal ord... | encoded | `o 23 r 1 "committal applicant" is the person applying for or having obtained a committal order` | 3 |
| 3561 | O 23 r 1 “committal respondent”: “committal respondent” means the person against whom a committal order is sought or made; | encoded | `o 23 r 1 "committal respondent" is the person against whom a committal order is sought or made` | 3 |
| 3562 | O 23 r 1 “contempt of court”: “contempt of court” means contempt of court under the Act and includes, subject to section... | encoded | `o 23 r 1 "contempt of court" kind of contempt`; `o 23 r 1 "contempt of court" is contempt under the Act, and includes contempt under the common law` | 5 |
| 3563 | O 23 r 1 “non‑publication direction”: “non‑publication direction” means a direction under section 13; | encoded | `o 23 r 1 "non-publication direction" is a direction under section 13` | 2 |
| 3564 | O 23 r 1 “section”: “section” means a section of the Act. | encoded | `o 23 r 1 "non-publication direction" is a direction under section 13`; `o 23 r 1 "section" is a section of the Act` | 4 |
| 3565 | O 23 r 2 heading: Committal order for contempt of court (O. 23, r. 2) | inert, reason 1 | | |
| 3566 | O 23 r 2: The power of the Court to punish for contempt of court may be exercised by a committal ord... | encoded | `o 23 r 2 the power to punish for contempt of court may be exercised by a committal order` | 2 |
| 3567 | O 23 r 3 heading: Application for permission of Court (O. 23, r. 3) | inert, reason 1 | | |
| 3568 | O 23 r 3(1): A committal applicant must first apply to the Court for permission to make an application ... | fork (F-TIMED) | `o 23 r 3(1) the committal applicant has first applied to the Court for permission` | 3 |
| 3568 | O 23 r 3(2): A committal applicant must first apply to the Court for permission to make an application ... | fork (F-MUST) | `o 23 r 3(2) how the application for permission is made`; `o 23 r 3(2) the application for permission is made in the way required` | 6 |
| 3569 | O 23 r 3(3): The application must be supported by an affidavit setting out — ( a ) | fork (F-MUST) | `o 23 r 3(3) the affidavit supporting the application sets out what is required` | 5 |
| 3569 to 3570 | O 23 r 3(3)(a): the committal applicant’s name, description and address; | fork (F-MUST) | `o 23 r 3(3) the affidavit supporting the application sets out what is required` | 5 |
| 3571 to 3572 | O 23 r 3(3)(b): the committal respondent’s name, description and address; and | fork (F-MUST) | `o 23 r 3(3) the affidavit supporting the application sets out what is required` | 5 |
| 3573 to 3574 | O 23 r 3(3)(c): the grounds on which the committal order is sought. | fork (F-MUST) | `o 23 r 3(3) the affidavit supporting the application sets out what is required` | 5 |
| 3575 | O 23 r 4 heading: Application for committal order after permission of Court granted (O. 23, r. 4) | inert, reason 1 | | |
| 3576 | O 23 r 4(1): After permission is granted under Rule 3, the committal applicant must apply for the commi... | fork (F-O23-1, F-ASSUMED, F-MUST) | `o 23 r 4(1) the period for applying for the committal order`; `o 23 r 4(1) how the committal order is applied for`; `o 23 r 4(1) the application for the committal order is made `; ... (6 names) | 18 |
| 3576 to 3577 | O 23 r 4(1)(a): the originating application without notice or summons without notice for permission under ... | fork (F-O23-1, F-ASSUMED, F-MUST) | `o 23 r 4(1) the period for applying for the committal order`; `o 23 r 4(1) how the committal order is applied for`; `o 23 r 4(1) the application for the committal order is made `; ... (6 names) | 18 |
| 3578 to 3579 | O 23 r 4(1)(b): the supporting affidavit under Rule 3(3); | fork (F-O23-1, F-ASSUMED, F-MUST) | `o 23 r 4(1) the period for applying for the committal order`; `o 23 r 4(1) how the committal order is applied for`; `o 23 r 4(1) the application for the committal order is made `; ... (6 names) | 18 |
| 3580 to 3581 | O 23 r 4(1)(c): the order granting permission under Rule 3(1); | fork (F-O23-1, F-ASSUMED, F-MUST) | `o 23 r 4(1) the period for applying for the committal order`; `o 23 r 4(1) how the committal order is applied for`; `o 23 r 4(1) the application for the committal order is made `; ... (6 names) | 18 |
| 3582 to 3583 | O 23 r 4(1)(d): the summons for the committal order under this paragraph. | fork (F-O23-1, F-ASSUMED, F-MUST) | `o 23 r 4(1) the period for applying for the committal order`; `o 23 r 4(1) how the committal order is applied for`; `o 23 r 4(1) the application for the committal order is made `; ... (6 names) | 18 |
| 3584 | O 23 r 4(2): There must be at least 21 days between the service under paragraph (1) and the hearing dat... | fork (F-O23-3) | `o 23 r 4(2) the minimum gap between service and the hearing`; `o 23 r 4(2) there are at least 21 days between the service and the hearing date` | 5 |
| 3585 | O 23 r 5 heading: Power to commit without application (O. 23, r. 5) | inert, reason 1 | | |
| 3586 | O 23 r 5(1): Where by virtue of any written law, the General Division has power to punish or take steps... | encoded | `o 23 r 5(1) a committal order may be made by the General Division` | 4 |
| 3586 | O 23 r 5(2): Where by virtue of any written law, the General Division has power to punish or take steps... | encoded | `o 23 r 5(2) Rules 2, 3 and 4 affect the power to make a committal order on its own accord` | 7 |
| 3587 | O 23 r 6 heading: Transfer to General Division (O. 23, r. 6) | inert, reason 1 | | |
| 3588 | O 23 r 6(1): An application under section 10(4) to transfer a case in a State Court to the General Divi... | encoded | `o 23 r 6(1) the application to transfer a case is made in the way required` | 4 |
| 3588 | O 23 r 6(2): An application under section 10(4) to transfer a case in a State Court to the General Divi... | fork (F-UNSURE) | `o 23 r 6(2) the General Division may order the case and related proceedings stayed` | 3 |
| 3589 | O 23 r 6(3): Where the General Division orders a case in a State Court to be transferred to the General... | encoded | `o 23 r 6(3)(a) what the General Division may do on ordering `; `o 23 r 6(3)(a) the General Division may do this on ordering `; `o 23 r 6(3)(b) the Registrar of the State Courts has sent wh`; ... (6 names) | 16 |
| 3589 | O 23 r 6(3)(a): (3) Where the General Division orders a case in a State Court to be transferred to the Gen... | encoded | `o 23 r 6(3)(a) what the General Division may do on ordering a transfer`; `o 23 r 6(3)(a) the General Division may do this on ordering the transfer` | 5 |
| 3590 to 3591 | O 23 r 6(3)(a)(i): set aside or affirm any order made by the State Court; | encoded | `o 23 r 6(3)(a) what the General Division may do on ordering a transfer`; `o 23 r 6(3)(a) the General Division may do this on ordering the transfer` | 5 |
| 3592 to 3593 | O 23 r 6(3)(a)(ii): modify Rules 3 and 4 in their application to the case; and | encoded | `o 23 r 6(3)(a) what the General Division may do on ordering a transfer`; `o 23 r 6(3)(a) the General Division may do this on ordering the transfer` | 5 |
| 3594 to 3595 | O 23 r 6(3)(a)(iii): make any other order relating to the transfer; | encoded | `o 23 r 6(3)(a) what the General Division may do on ordering a transfer`; `o 23 r 6(3)(a) the General Division may do this on ordering the transfer` | 5 |
| 3596 to 3597 | O 23 r 6(3)(b): the Registrar of the State Courts must send to the Registrar of the Supreme Court the file... | encoded | `o 23 r 6(3)(b) the Registrar of the State Courts has sent what must be sent to the Registrar of the Supreme Court`; `o 23 r 6(3)(b) the person who must send the file, documents, exhibits and certified copy of the notes of evidence to the Registrar of the Supreme Court` | 7 |
| 3598 to 3599 | O 23 r 6(3)(c): the Registrar of the Supreme Court must give notice of the transfer to every party to the ... | encoded | `o 23 r 6(3)(c) every party to the case has been given notice of the transfer`; `o 23 r 6(3)(c) the person who must give notice of the transfer to every party to the case` | 4 |
| 3600 | O 23 r 7 heading: Provisions as to hearing (O. 23, r. 7) | inert, reason 1 | | |
| 3601 | O 23 r 7(1): The Court must hear in open court an application for a committal order or an application u... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3601 to 3602 | O 23 r 7(1)(a): where the application arises out of proceedings relating to the wardship or adoption of an... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3603 to 3604 | O 23 r 7(1)(b): where the application arises out of proceedings relating to a person who lacks capacity wi... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3605 to 3606 | O 23 r 7(1)(c): where the application is made in the General Division and arises out of proceedings in a S... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3607 to 3608 | O 23 r 7(1)(d): where the application arises out of proceedings in which a secret process, discovery or in... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3609 to 3610 | O 23 r 7(1)(e): where it appears to the Court that, in the interests of the administration of justice or f... | fork (F-O23-2) | `o 23 r 7(1) the Court may hear the application in private`; `o 23 r 7(1) the Court must hear the application in open court` | 11 |
| 3611 | O 23 r 7(2): If the Court hears the application in private under paragraph (1) and decides to make a co... | encoded | `o 23 r 7(2) the Court must state in open court what the paragraph lists`; `o 23 r 7(2) the Court has stated in open court what the paragraph lists` | 8 |
| 3611 to 3612 | O 23 r 7(2)(a): the name of the committal respondent; | encoded | `o 23 r 7(2) the Court must state in open court what the paragraph lists`; `o 23 r 7(2) the Court has stated in open court what the paragraph lists` | 8 |
| 3613 to 3614 | O 23 r 7(2)(b): in general terms the nature of the contempt of court in respect of which the committal ord... | encoded | `o 23 r 7(2) the Court must state in open court what the paragraph lists`; `o 23 r 7(2) the Court has stated in open court what the paragraph lists` | 8 |
| 3615 to 3616 | O 23 r 7(2)(c): if the committal respondent is being committed for a fixed period, the length of that peri... | fork (F-MUST) | `o 23 r 7(2) the Court must state in open court what the paragraph lists`; `o 23 r 7(2) the Court has stated in open court what the paragraph lists` | 8 |
| 3617 | O 23 r 7(3): The committal applicant must rely on only the grounds set out in the affidavit under Rule ... | encoded | `o 23 r 7(3) the committal applicant may rely on the ground`; `o 23 r 7(3) the committal applicant shall not rely on a ground not set out in the affidavit` | 2 |
| 3618 | O 23 r 7(4): At the hearing of the application for a committal order, the committal respondent — ( a ) | encoded | `o 23 r 7(4)(a) the committal respondent must rely on the matters stated in the affidavit`; `o 23 r 7(4)(b) the committal respondent may give oral evidence` | 5 |
| 3618 to 3619 | O 23 r 7(4)(a): must rely on the matters stated in his or her affidavit, if any; but | encoded | `o 23 r 7(4)(a) the committal respondent must rely on the matters stated in the affidavit` | 2 |
| 3620 to 3621 | O 23 r 7(4)(b): may, with the permission of the Court, give oral evidence on his or her own behalf. | fork (F-MUST) | `o 23 r 7(4)(b) the committal respondent may give oral evidence` | 3 |
| 3622 | O 23 r 7(5): For the purposes of section 26A(9), in making any order allowing a committal respondent to... | fork (F-UNSURE) | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3622 | O 23 r 7(5)(a): (5) For the purposes of section 26A(9), in making any order allowing a committal responden... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3623 to 3624 | O 23 r 7(5)(a)(i): the committal respondent; | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3625 to 3626 | O 23 r 7(5)(a)(ii): an advocate representing the committal respondent; | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3627 to 3628 | O 23 r 7(5)(b): whether the order would affect the ability of the committal applicant to effectively condu... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3629 to 3630 | O 23 r 7(5)(c): whether the order would affect the ability of the committal respondent to consult and inst... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3631 | O 23 r 7(5)(d): ( d ) | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3632 to 3633 | O 23 r 7(5)(d)(i): to verify the identities of persons giving evidence or appearing by means of the live vide... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3634 to 3635 | O 23 r 7(5)(d)(ii): to prevent the committal respondent from being coached or coerced while giving evidence or... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3636 to 3637 | O 23 r 7(5)(d)(iii): to prevent the proceedings from being recorded; and | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3638 to 3639 | O 23 r 7(5)(d)(iv): to control and restrict the persons who are able to access or observe the proceedings; | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3640 to 3641 | O 23 r 7(5)(e): the likelihood that the Court may require the committal respondent to handle any physical ... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3642 to 3643 | O 23 r 7(5)(f): whether a judgment or order requiring the committal respondent to be taken into custody ma... | encoded | `o 23 r 7(5) matter for a live link order for the committal respondent`; `o 23 r 7(5) the Court is to have regard to the matter` | 12 |
| 3644 | O 23 r 7(6): For the purposes of section 26A(9), in making any order allowing a witness (not being the ... | fork (F-UNSURE) | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3644 | O 23 r 7(6)(a): (6) For the purposes of section 26A(9), in making any order allowing a witness (not being ... | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3645 to 3646 | O 23 r 7(6)(a)(i): the committal respondent; | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3647 to 3648 | O 23 r 7(6)(a)(ii): an advocate representing the committal respondent; | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3649 to 3650 | O 23 r 7(6)(b): whether the order would affect the ability of the committal applicant to effectively condu... | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3651 | O 23 r 7(6)(c): ( c ) | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3652 to 3653 | O 23 r 7(6)(c)(i): to verify the identities of persons giving evidence by means of the live video or live tel... | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3654 to 3655 | O 23 r 7(6)(c)(ii): to prevent the witness from being coached or coerced while giving evidence by means of a l... | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3656 to 3657 | O 23 r 7(6)(c)(iii): to prevent the proceedings from being recorded; and | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3658 to 3659 | O 23 r 7(6)(c)(iv): to control and restrict the persons who are able to access or observe the proceedings; | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3660 to 3661 | O 23 r 7(6)(d): the likelihood that the Court may require the witness to handle any physical evidence; | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3662 to 3663 | O 23 r 7(6)(e): in the case of an order under section 26A(3) allowing an expert witness to give evidence f... | encoded | `o 23 r 7(6) matter for a live link order for a witness`; `o 23 r 7(6) the Court is to have regard to the matter` | 12 |
| 3664 | O 23 r 8 heading: Power to suspend execution of committal order (O. 23, r. 8) | inert, reason 1 | | |
| 3665 | O 23 r 8(1): The Court may order the execution of the committal order to be suspended for such period o... | encoded | `o 23 r 8(1) the Court may order the execution of the committal order to be suspended` | 2 |
| 3665 | O 23 r 8(2): The Court may order the execution of the committal order to be suspended for such period o... | encoded | `o 23 r 8(2) the committal applicant must serve a notice of the terms of the order`; `o 23 r 8(2) the committal applicant has served the notice required`; `o 23 r 8(2) the committal applicant must serve a notice of the terms of the suspension` | 5 |
| 3666 | O 23 r 8(3): The committal applicant may apply for the suspension to be lifted on the ground that any o... | fork (F-UNSURE) | `o 23 r 8(3) the committal applicant may apply for the suspension to be lifted` | 2 |
| 3667 | O 23 r 8(4): An application under paragraph (3) must be made by summons supported by an affidavit and m... | encoded | `o 23 r 8(4) the application to lift the suspension is made and served as required` | 4 |
| 3668 | O 23 r 9 heading: Discharge of committal respondent (O. 23, r. 9) | inert, reason 1 | | |
| 3669 | O 23 r 9(1): Where a committal respondent has been committed for contempt of court, the Court may disch... | encoded | `o 23 r 9(1) the Court may discharge the committal respondent` | 3 |
| 3669 | O 23 r 9(2): Where a committal respondent has been committed for contempt of court, the Court may disch... | encoded | `o 23 r 9(2) the Sheriff may take possession of the thing`; `o 23 r 9(2) the Court may discharge the committal respondent and give directions for dealing with the thing` | 6 |
| 3670 | O 23 r 10 heading: Saving for other powers (O. 23, r. 10) | inert, reason 1 | | |
| 3671 | O 23 r 10: Nothing in Rules 1 to 9 is to be taken as affecting the power of the Court to make an orde... | encoded | `o 23 r 10 an order the Court has power to make`; `o 23 r 10 Rules 1 to 9 affect the Court's power to make the order`; `o 23 r 10 Rules 1 to 9 apply to the application as they apply to an application for a committal order` | 6 |
| 3672 | O 23 r 11 heading: Form of committal order (O. 23, r. 11) | inert, reason 1 | | |
| 3673 | O 23 r 11(1): A committal order must be in Form 42. (2) The committal applicant must serve on the Sherif... | encoded | `o 23 r 11(1) the form of the committal order`; `o 23 r 11(1) the committal order is in the form required` | 3 |
| 3673 | O 23 r 11(2): A committal order must be in Form 42. (2) The committal applicant must serve on the Sherif... | encoded | `o 23 r 11(2) the committal applicant has served on the Sheriff's office what is required` | 8 |
| 3673 to 3674 | O 23 r 11(2)(a): the committal order; and | encoded | `o 23 r 11(2) the committal applicant has served on the Sheriff's office what is required` | 8 |
| 3675 | O 23 r 11(2)(b): ( b ) | encoded | `o 23 r 11(2) the committal applicant has served on the Sheriff's office what is required` | 8 |
| 3676 to 3677 | O 23 r 11(2)(b)(i): pay upon request all charges, expenses and fees incurred by or payable to the Sheriff and ... | encoded | `o 23 r 11(2) the committal applicant has served on the Sheriff's office what is required` | 8 |
| 3678 to 3679 | O 23 r 11(2)(b)(ii): indemnify the Sheriff and the Singapore Police Force against all claims, costs and expense... | encoded | `o 23 r 11(2) the committal applicant has served on the Sheriff's office what is required` | 8 |
| 3680 | O 23 r 11(3): The committal applicant must also deposit the amount of money requested by the Sheriff bef... | fork (F-TIMED) | `o 23 r 11(3) the committal applicant has deposited the money requested by the Sheriff`; `o 23 r 11(3) the committal applicant must deposit the money the Sheriff requested` | 3 |
| 3681 | O 23 r 12 heading: Committal proceedings before Employment Claims Tribunals (O. 23, r. 12) | inert, reason 1 | | |
| 3682 | O 23 r 12(1): Rules 1 to 11 (except Rule 7(1) and (2)) apply to committal proceedings before a tribunal.... | encoded | `o 23 r 12(1) Rules 1 to 11 apply to committal proceedings before a tribunal` | 8 |
| 3682 | O 23 r 12(2): Rules 1 to 11 (except Rule 7(1) and (2)) apply to committal proceedings before a tribunal.... | encoded | `o 23 r 12(2) a reference`; `o 23 r 12(2) how the reference is read`; `o 23 r 12(2) how a reference in Order 23 is read for a committal proceeding before an Employment Claims Tribunal` | 3 |
| 3682 to 3683 | O 23 r 12(2)(a): any reference to a Court is a reference to a tribunal or a tribunal magistrate; and | encoded | `o 23 r 12(2) a reference`; `o 23 r 12(2) how the reference is read`; `o 23 r 12(2) how a reference in Order 23 is read for a committal proceeding before an Employment Claims Tribunal` | 3 |
| 3684 to 3685 | O 23 r 12(2)(b): any reference to a Judge is a reference to a tribunal magistrate. | encoded | `o 23 r 12(2) a reference`; `o 23 r 12(2) how the reference is read`; `o 23 r 12(2) how a reference in Order 23 is read for a committal proceeding before an Employment Claims Tribunal` | 3 |
| 3686 | O 23 r 12(3): The court fees that apply to proceedings under this Order in a District Court apply to pro... | encoded | `o 23 r 12(3) the court fees that apply to proceedings under this Order in a tribunal are those in` | 2 |
| 3687 | O 23 r 12(4): The hearing fees prescribed in the Employment Claims Rules 2017 (G.N. No. S 104/2017) appl... | encoded | `o 23 r 12(4) the instrument that prescribes the hearing fees in a tribunal` | 1 |
| 3688 | O 23 r 12(5): In this Rule — “tribunal” means a State Court called an Employment Claims Tribunal constit... | encoded | `o 23 r 12(5) "tribunal" is a State Court called an Employment Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 12(5) "tribunal magistrate" has the meaning given by section 2(1) of the Employment Claims Act 2016` | 6 |
| 3688 | O 23 r 12(5) “tribunal”: (5) In this Rule — “tribunal” means a State Court called an Employment Claims Tribunal con... | encoded | `o 23 r 12(5) "tribunal" is a State Court called an Employment Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 12(5) "tribunal magistrate" has the meaning given by section 2(1) of the Employment Claims Act 2016` | 6 |
| 3689 | O 23 r 12(5) “tribunal magistrate”: “tribunal magistrate” has the meaning given by section 2(1) of the Employment Claims Act 2... | encoded | `o 23 r 12(5) "tribunal" is a State Court called an Employment Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 12(5) "tribunal magistrate" has the meaning given by section 2(1) of the Employment Claims Act 2016` | 6 |
| 3690 | O 23 r 13 heading: Committal proceedings before Small Claims Tribunals (O. 23, r. 13) | inert, reason 1 | | |
| 3691 | O 23 r 13(1): Rules 1 to 11 (except Rule 7(1) and (2)) apply to committal proceedings before a tribunal.... | encoded | `o 23 r 13(1) Rules 1 to 11 apply to committal proceedings before a Small Claims Tribunal` | 3 |
| 3691 | O 23 r 13(2): Rules 1 to 11 (except Rule 7(1) and (2)) apply to committal proceedings before a tribunal.... | encoded | `o 23 r 13(2) how a reference in Order 23 is read for a committal proceeding before a Small Claims Tribunal` | 2 |
| 3691 to 3692 | O 23 r 13(2)(a): any reference to a Court is a reference to a tribunal or a tribunal magistrate; and | encoded | `o 23 r 13(2) how a reference in Order 23 is read for a committal proceeding before a Small Claims Tribunal` | 2 |
| 3693 to 3694 | O 23 r 13(2)(b): any reference to a Judge is a reference to a tribunal magistrate. | encoded | `o 23 r 13(2) how a reference in Order 23 is read for a committal proceeding before a Small Claims Tribunal` | 2 |
| 3695 | O 23 r 13(3): The court fees that apply to proceedings under this Order in a Magistrate’s Court apply to... | encoded | `o 23 r 13(3) the court fees and hearing fees that apply to proceedings under this Order in a tribunal are those in` | 2 |
| 3696 | O 23 r 13(4): The hearing fees that apply to proceedings under this Order in a Magistrate’s Court apply ... | encoded | `o 23 r 13(3) the court fees and hearing fees that apply to proceedings under this Order in a tribunal are those in` | 2 |
| 3697 | O 23 r 13(5): In this Rule — “tribunal” means a Small Claims Tribunal constituted under section 4 of the... | encoded | `o 23 r 13(5) "tribunal" is a Small Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 13(5) "tribunal magistrate" has the meaning given by section 2(1) of the Small Claims Tribunals Act` | 5 |
| 3697 | O 23 r 13(5) “tribunal”: (5) In this Rule — “tribunal” means a Small Claims Tribunal constituted under section 4 of... | encoded | `o 23 r 13(5) "tribunal" is a Small Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 13(5) "tribunal magistrate" has the meaning given by section 2(1) of the Small Claims Tribunals Act` | 5 |
| 3698 | O 23 r 13(5) “tribunal magistrate”: “tribunal magistrate” has the meaning given by section 2(1) of the Small Claims Tribunals ... | encoded | `o 23 r 13(5) "tribunal" is a Small Claims Tribunal constituted under section 4 of the State Courts Act`; `o 23 r 13(5) "tribunal magistrate" has the meaning given by section 2(1) of the Small Claims Tribunals Act` | 5 |
| 3699 | O 23 r 14 heading: Committal proceedings before Community Disputes Resolution Tribunals (O. 23, r. 14) | inert, reason 1 | | |
| 3700 | O 23 r 14(1): To avoid doubt, Rules 1 to 11 (except Rule 7(1) and (2)) apply to a tribunal. (2) For the ... | encoded | `o 23 r 14(1) Rules 1 to 11 apply to a Community Disputes Resolution Tribunal` | 3 |
| 3700 | O 23 r 14(2): To avoid doubt, Rules 1 to 11 (except Rule 7(1) and (2)) apply to a tribunal. (2) For the ... | encoded | `o 23 r 14(2) a reference`; `o 23 r 14(2) how the reference is read`; `o 23 r 14(2) how a reference in Order 23 is read for a Community Disputes Resolution Tribunal` | 3 |
| 3700 to 3701 | O 23 r 14(2)(a): any reference to a Court is a reference to a tribunal or a tribunal judge; and | encoded | `o 23 r 14(2) a reference`; `o 23 r 14(2) how the reference is read`; `o 23 r 14(2) how a reference in Order 23 is read for a Community Disputes Resolution Tribunal` | 3 |
| 3702 to 3703 | O 23 r 14(2)(b): any reference to a Judge is a reference to a tribunal judge. | encoded | `o 23 r 14(2) a reference`; `o 23 r 14(2) how the reference is read`; `o 23 r 14(2) how a reference in Order 23 is read for a Community Disputes Resolution Tribunal` | 3 |
| 3704 | O 23 r 14(3): In this Rule — “tribunal” means a State Court designated as a Community Disputes Resolutio... | encoded | `o 23 r 14(3) "tribunal" is a State Court designated as a Community Disputes Resolution Tribunal`; `o 23 r 14(3) "tribunal judge" is a District Judge designated as a tribunal judge` | 4 |
| 3704 | O 23 r 14(3) “tribunal”: (3) In this Rule — “tribunal” means a State Court designated as a Community Disputes Resol... | encoded | `o 23 r 14(3) "tribunal" is a State Court designated as a Community Disputes Resolution Tribunal`; `o 23 r 14(3) "tribunal judge" is a District Judge designated as a tribunal judge` | 4 |
| 3705 | O 23 r 14(3) “tribunal judge”: “tribunal judge” means a District Judge designated as a tribunal judge under section 14(1)... | encoded | `o 23 r 14(3) "tribunal" is a State Court designated as a Community Disputes Resolution Tribunal`; `o 23 r 14(3) "tribunal judge" is a District Judge designated as a tribunal judge` | 4 |
| 3706 | O 23 r 15 heading: Application by Attorney‑General for permission to give non‑publication direction (O. 23, r... | inert, reason 1 | | |
| 3707 | O 23 r 15(1): An application by the Attorney‑General for permission to give a non‑publication direction ... | encoded | `o 23 r 15(1) the Attorney-General's application is made in the way required` | 5 |
| 3707 | O 23 r 15(2): An application by the Attorney‑General for permission to give a non‑publication direction ... | encoded | `o 23 r 15(1) the Attorney-General's application is made in the way required` | 5 |
| 3708 | O 23 r 15(3): The supporting affidavit must — ( a ) | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3708 to 3709 | O 23 r 15(3)(a): have annexed to it a copy of the proposed non‑publication direction; | fork (F-MUST) | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3710 | O 23 r 15(3)(b): ( b ) | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3711 to 3712 | O 23 r 15(3)(b)(i): the person to whom the proposed non‑publication direction will apply has published the mat... | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3713 to 3714 | O 23 r 15(3)(b)(ii): the publication of the matter that is the subject of the non‑publication direction would s... | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3715 to 3716 | O 23 r 15(3)(c): state the reasons for any exception or condition in the proposed non‑publication direction... | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3717 to 3718 | O 23 r 15(3)(d): state that the Attorney‑General is satisfied that it is in the public interest to give the... | encoded | `o 23 r 15(3) the supporting affidavit states what it must` | 6 |
| 3719 | O 23 r 15(4): The Court’s permission to give a non‑publication direction lapses if the direction is not ... | encoded | `o 23 r 15(4) the period for serving the non-publication direction`; `o 23 r 15(4) the Court's permission to give the non-publication direction lapses` | 6 |
| 3720 | O 23 r 15(5): After a non‑publication direction is served, a person authorised by the Attorney‑General m... | encoded | `o 23 r 15(5) the affidavit of service of the non-publication direction has been filed`; `o 23 r 15(5) the person who must file the affidavit of service of the non-publication direction` | 6 |
| 3721 | O 23 r 16 heading: Application to set aside or vary non‑publication direction (O. 23, r. 16) | inert, reason 1 | | |
| 3722 | O 23 r 16(1): This Rule applies to an application under section 13(9) to vary or set aside a non‑publica... | encoded | `o 23 r 16(2) the application is made within 14 days after the direction is served` | 4 |
| 3722 | O 23 r 16(2): This Rule applies to an application under section 13(9) to vary or set aside a non‑publica... | encoded | `o 23 r 16(2) the period for applying to vary or set aside the direction`; `o 23 r 16(2) the application is made within 14 days after the direction is served` | 5 |
| 3723 | O 23 r 16(3): To avoid doubt, paragraph (2) applies even if the application is made by the author of the... | encoded | `o 23 r 16(3) paragraph (2) applies to the application` | 2 |
| 3724 | O 23 r 16(4): An application must be made by summons in the originating application in which permission ... | encoded | `o 23 r 16(4) the application to vary or set aside is made as required` | 3 |
| 3725 | O 23 r 16(5): The applicant must serve the summons and the supporting affidavit on the Attorney‑General,... | encoded | `o 23 r 16(5) the applicant has served the summons and the supporting affidavit on those required` | 4 |
| 3726 | O 23 r 16(6): If the applicant is the author of the matter that is the subject of the non‑publication di... | encoded | `o 23 r 16(6) the supporting affidavit states that the applicant is the author` | 3 |
| 3727 | O 23 r 16(7): If the Court sets aside or varies a non‑publication direction, the applicant must serve th... | encoded | `o 23 r 16(7) the period for serving the order setting aside `; `o 23 r 16(7) the order is served within 14 days after the da`; `o 23 r 16(7) the order has been served on those required`; ... (4 names) | 10 |
| 3727 to 3728 | O 23 r 16(7)(a): on the person to whom the direction applies (unless the person is the applicant); and | encoded | `o 23 r 16(7) the period for serving the order setting aside `; `o 23 r 16(7) the order is served within 14 days after the da`; `o 23 r 16(7) the order has been served on those required`; ... (4 names) | 10 |
| 3729 to 3730 | O 23 r 16(7)(b): any other person whom the Court orders to be served. | encoded | `o 23 r 16(7) the period for serving the order setting aside `; `o 23 r 16(7) the order is served within 14 days after the da`; `o 23 r 16(7) the order has been served on those required`; ... (4 names) | 10 |
| 3731 | O 23 r 16(8): If an order of Court is required to be served in accordance with paragraph (7), the applic... | encoded | `o 23 r 16(8) the applicant has filed the affidavit of service of the order` | 4 |
| 3732 | O 23 r 16(9): An order of Court to set aside a non‑publication direction takes effect from the date of t... | encoded | `o 23 r 16(9) the date from which the order setting aside the direction takes effect` | 2 |
| 3733 | O 23 r 16(10): An order of Court to vary a non‑publication direction takes effect — ( a ) | encoded | `o 23 r 16(10)(a) the date from which the order varying the d`; `o 23 r 16(10)(b) the date from which the order varying the d`; `o 23 r 16(10)(b) the date the Court specified is a later dat`; ... (3 names) | 9 |
| 3733 to 3734 | O 23 r 16(10)(a): insofar as the direction and the variation apply to the applicant — from the date of the o... | encoded | `o 23 r 16(10)(a) the date from which the order varying the direction takes effect as to the applicant` | 2 |
| 3735 to 3736 | O 23 r 16(10)(b): insofar as the direction and the variation apply to a person other than the applicant — fr... | fork (F-ASSUMED) | `o 23 r 16(10)(b) the date from which the order varying the direction takes effect as to a person other than the applicant`; `o 23 r 16(10)(b) the date the Court specified is a later date than the date of service` | 7 |
| 3737 | O 23 r 17 heading: Order to arrest committal respondent (O. 23, r. 17) | inert, reason 1 | | |
| 3738 | O 23 r 17(1): The Court may order the Sheriff or any police officer to arrest and bring before the Court... | encoded | `o 23 r 17(1) the Court may order the Sheriff or a police officer to arrest and bring the committal respondent before the Court` | 3 |
| 3738 | O 23 r 17(2): The Court may order the Sheriff or any police officer to arrest and bring before the Court... | encoded | `o 23 r 17(2) the Court may include conditions about security or any other matter in the order to arrest` | 2 |
| 3739 | O 23 r 17(3): A letter from the Registrar stating the Court’s order made under paragraph (1) is sufficie... | encoded | `o 23 r 17(3) the letter is sufficient authority for the Sheriff or a police officer to effect the arrest` | 3 |
| 3740 | O 23 r 18 heading: Sheriff may engage auxiliary police officer or other security agency (O. 23, r. 18) | inert, reason 1 | | |
| 3741 | O 23 r 18(1): The Sheriff may engage, or direct the applicant to engage, any auxiliary police officer ap... | encoded | `o 23 r 18(1) the Sheriff may engage, or direct the applicant to engage, the person` | 3 |
| 3741 | O 23 r 18(2): The Sheriff may engage, or direct the applicant to engage, any auxiliary police officer ap... | encoded | `o 23 r 18(2) the amount is part of the charges, expenses and fees incurred in complying with a committal order` | 2 |
| 3742 to 3743 | O 24 heading: ORDER 24 | inert, reason 1 | | |
| 3744 | O 24 r 1 heading: Scope of this Order (O. 24, r. 1) | inert, reason 1 | | |
| 3745 | O 24 r 1: This Order applies to the Supreme Court only. | encoded | `o 24 r 1 this Order applies to the court` | 2 |
| 3746 | O 24 r 2 heading: Definition and general matters of this Order (O. 24, r. 2) | inert, reason 1 | | |
| 3747 | O 24 r 2(1): The following are prerogative orders: ( a ) | fork (F-O24-2) | `o 24 r 2(1) kind of order`; `o 24 r 2(1) the order is a prerogative order` | 5 |
| 3747 to 3748 | O 24 r 2(1)(a): an Order for Review of Detention; | fork (F-O24-2) | `o 24 r 2(1) kind of order`; `o 24 r 2(1) the order is a prerogative order` | 5 |
| 3749 to 3750 | O 24 r 2(1)(b): a Mandatory Order; | fork (F-O24-2) | `o 24 r 2(1) kind of order`; `o 24 r 2(1) the order is a prerogative order` | 5 |
| 3751 to 3752 | O 24 r 2(1)(c): a Prohibiting Order; | fork (F-O24-2) | `o 24 r 2(1) kind of order`; `o 24 r 2(1) the order is a prerogative order` | 5 |
| 3753 to 3754 | O 24 r 2(1)(d): a Quashing Order. | fork (F-O24-2) | `o 24 r 2(1) kind of order`; `o 24 r 2(1) the order is a prerogative order` | 5 |
| 3755 | O 24 r 2(2): An application for a prerogative order must not be made before the applicant has exhausted... | encoded | `o 24 r 2(2) the application for a prerogative order may be made`; `o 24 r 2(2) the applicant shall not apply for a prerogative order before exhausting every right of appeal or other remedy` | 2 |
| 3756 | O 24 r 3 heading: Application for Order for Review of Detention (O. 24, r. 3) | inert, reason 1 | | |
| 3757 | O 24 r 3(1): An application for an Order for Review of Detention must be made by originating applicatio... | encoded | `o 24 r 3(1) the application for an Order for Review of Detention is made by originating application without notice` | 2 |
| 3757 | O 24 r 3(2): An application for an Order for Review of Detention must be made by originating applicatio... | encoded | `o 24 r 3(2) the subject's affidavit supports the application as required` | 8 |
| 3758 | O 24 r 3(3): If the subject is unable to make the affidavit or if the application is urgent, some other... | encoded | `o 24 r 3(3) some other person may make the affidavit`; `o 24 r 3(3) the other person's affidavit states what it must` | 7 |
| 3759 | O 24 r 3(4): The application must be heard by a Judge sitting in the General Division. | encoded | `o 24 r 3(4) the application is heard by a Judge sitting in the General Division` | 4 |
| 3760 | O 24 r 3(5): The subject need not be brought before the Court hearing the originating application unles... | encoded | `o 24 r 3(5) the subject must be brought before the Court hearing the originating application` | 2 |
| 3761 | O 24 r 3(6): At the hearing of the application, the Court may — ( a ) | encoded | `o 24 r 3(6) what the Court may do at the hearing`; `o 24 r 3(6) the Court may do this at the hearing of the application` | 3 |
| 3761 to 3762 | O 24 r 3(6)(a): make an Order for Review of Detention in Form 43 forthwith and order that the subject is t... | encoded | `o 24 r 3(6)(a) the form of the Order for Review of Detention`; `o 24 r 3(6) what the Court may do at the hearing`; `o 24 r 3(6) the Court may do this at the hearing of the application` | 4 |
| 3763 to 3764 | O 24 r 3(6)(b): direct that a summons for the Order for Review of Detention be issued. | encoded | `o 24 r 3(6) what the Court may do at the hearing`; `o 24 r 3(6) the Court may do this at the hearing of the application` | 3 |
| 3765 | O 24 r 4 heading: Summons for Order for Review of Detention (O. 24, r. 4) | inert, reason 1 | | |
| 3766 | O 24 r 4(1): The summons for the Order for Review of Detention is to be a summons in the originating ap... | encoded | `o 24 r 4(1) the summons for the Order for Review of Detention is a summons in the originating application` | 2 |
| 3766 | O 24 r 4(2): The summons for the Order for Review of Detention is to be a summons in the originating ap... | fork (F-O24-1) | `o 24 r 4(2) two working days`; `o 24 r 4(2) the document is served as soon as practicable an`; `o 24 r 4(2) the four documents are served on the defendant a`; ... (4 names) | 11 |
| 3767 | O 24 r 4(3): Where the identity of the defendant is unknown or uncertain, the applicant may name the At... | encoded | `o 24 r 4(3) the applicant may name the Attorney-General as the defendant` | 2 |
| 3768 | O 24 r 4(4): The Attorney‑General may apply to the Court for an order that some other defendant be adde... | encoded | `o 24 r 4(4) the Attorney-General may apply to the Court for another defendant to be added or substituted` | 2 |
| 3769 | O 24 r 4(5): The defendant and the Attorney‑General may file and serve affidavits to contest the summon... | encoded | `o 24 r 4(5) who files an affidavit`; `o 24 r 4(5) how the affidavits are made`; `o 24 r 4(5) the person may file and serve an affidavit to contest the summons`; `o 24 r 4(5) the affidavits may be made in this way` | 6 |
| 3770 | O 24 r 4(6): Every party to the summons must serve a copy of each of the affidavits which he or she pro... | fork (F-O24-1) | `o 24 r 4(6) the copy of each affidavit is served on every other party in time` | 4 |
| 3771 | O 24 r 4(7): The summons for the Order for Review of Detention must be heard by a Judge sitting in the ... | encoded | `o 24 r 4(7) the summons is heard by a Judge sitting in the General Division` | 3 |
| 3772 | O 24 r 4(8): The subject need not be brought before the Court hearing the summons unless the Court othe... | encoded | `o 24 r 4(8) the subject must be brought before the Court hearing the summons` | 2 |
| 3773 | O 24 r 4(9): At the hearing of the summons, the Court may order that — ( a ) | encoded | `o 24 r 4(9) what the Court may order at the hearing`; `o 24 r 4(9) the Court may order this at the hearing of the summons` | 4 |
| 3773 to 3774 | O 24 r 4(9)(a): the summons be dismissed; | encoded | `o 24 r 4(9) what the Court may order at the hearing`; `o 24 r 4(9) the Court may order this at the hearing of the summons` | 4 |
| 3775 to 3776 | O 24 r 4(9)(b): further affidavits be filed and served by the parties; or | encoded | `o 24 r 4(9) what the Court may order at the hearing`; `o 24 r 4(9) the Court may order this at the hearing of the summons` | 4 |
| 3777 to 3778 | O 24 r 4(9)(c): an Order for Review of Detention be made in Form 43 and the defendant is to release the su... | encoded | `o 24 r 4(9) what the Court may order at the hearing`; `o 24 r 4(9) the Court may order this at the hearing of the summons` | 4 |
| 3779 | O 24 r 4(10): Where the Court makes an order under paragraph (9)( c ) or Rule 3(6)( a ), the solicitor a... | fork (F-TIMED) | `o 24 r 4(10) the defendant or the appropriate person or enti`; `o 24 r 4(10) the solicitor appearing for the defendant has i`; `o 24 r 4(10) the person who must inform the defendant or the`; ... (3 names) | 7 |
| 3780 | O 24 r 4(11): Where the Court makes an order under paragraph (9)( c ) in the presence of the defendant o... | encoded | `o 24 r 4(11) the defendant or the appropriate person or entity must comply with the Order for Review of Detention although it has not been served`; `o 24 r 4(11) the defendant must comply with the Order for Review of Detention` | 2 |
| 3781 | O 24 r 5 heading: No application for Mandatory Order, Prohibiting Order or Quashing Order without permission... | inert, reason 1 | | |
| 3782 | O 24 r 5(1): An application for a Mandatory Order, Prohibiting Order or Quashing Order — ( a ) | encoded | `o 24 r 5(1)(a) the application may include an application for a declaration`; `o 24 r 5(1)(b) the application for a Mandatory Order, Prohibiting Order or Quashing Order may be made` | 4 |
| 3782 to 3783 | O 24 r 5(1)(a): may include an application for a declaration which is ancillary to or consequential upon t... | encoded | `o 24 r 5(1)(a) the application may include an application for a declaration` | 2 |
| 3784 to 3785 | O 24 r 5(1)(b): must not be made, unless permission to make the application for the Order has been granted... | encoded | `o 24 r 5(1)(b) the application for a Mandatory Order, Prohibiting Order or Quashing Order may be made` | 2 |
| 3786 | O 24 r 5(2): Subject to any written law, an application for permission to apply for a Mandatory Order, ... | encoded | `o 24 r 5(2) three months`; `o 24 r 5(2) the application for permission is made within 3 months after the omission, judgment, order, conviction or proceedings` | 8 |
| 3787 | O 24 r 5(3): The application for permission must be made by originating application and must be support... | encoded | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3787 to 3788 | O 24 r 5(3)(a): a statement setting out the name and description of the applicant, the relief sought and t... | encoded | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3789 | O 24 r 5(3)(b): ( b ) | encoded | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3790 to 3791 | O 24 r 5(3)(b)(i): the applicant has the legal standing to make the application; | fork (F-MUST) | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3792 to 3793 | O 24 r 5(3)(b)(ii): the evidence discloses an arguable case of reasonable suspicion in favour of the Court mak... | encoded | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3794 to 3795 | O 24 r 5(3)(b)(iii): the defendant and the matters in issue are susceptible to the orders sought. | encoded | `o 24 r 5(3) the application for permission is made and supported as required` | 8 |
| 3796 | O 24 r 5(4): The applicant is bound by the grounds and relief set out in the statement and may not rely... | encoded | `o 24 r 5(4) the applicant may rely on the ground or seek the relief` | 3 |
| 3797 | O 24 r 5(5): The originating application, the statement and the affidavit must be served on the defenda... | fork (F-O24-1) | `o 24 r 5(5) the originating application, the statement and the affidavit are served on the defendant and the Attorney-General in time` | 4 |
| 3798 | O 24 r 5(6): The Attorney‑General may apply to the Court for an order that some other defendant be adde... | encoded | `o 24 r 5(6) the Attorney-General may apply to the Court for another defendant to be added or substituted` | 2 |
| 3799 | O 24 r 5(7): The defendant and the Attorney‑General may file and serve affidavits to contest the applic... | encoded | `o 24 r 5(7) the person may file and serve an affidavit to contest the application for permission` | 3 |
| 3800 | O 24 r 5(8): The application for permission must be heard by a Judge. | encoded | `o 24 r 5(8) the application for permission is heard by a Judge` | 3 |
| 3801 | O 24 r 5(9): At the hearing of the application for permission, the Court may order that — ( a ) | encoded | `o 24 r 5(9) what the Court may order at the hearing`; `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | 5 |
| 3801 to 3802 | O 24 r 5(9)(a): the application be allowed and where permission is granted to apply for a Prohibiting Orde... | encoded | `o 24 r 5(9)(a) the Court may also order a stay of the proceedings in question until the application for the Order is determined`; `o 24 r 5(9) what the Court may order at the hearing`; `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | 11 |
| 3803 to 3804 | O 24 r 5(9)(b): the application be dismissed; | encoded | `o 24 r 5(9) what the Court may order at the hearing`; `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | 5 |
| 3805 to 3806 | O 24 r 5(9)(c): the application be served on some other persons; or | encoded | `o 24 r 5(9) what the Court may order at the hearing`; `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | 5 |
| 3807 to 3808 | O 24 r 5(9)(d): further affidavits be filed and served by the parties. | encoded | `o 24 r 5(9) what the Court may order at the hearing`; `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | 5 |
| 3809 | O 24 r 6 heading: Application for Mandatory Order, Prohibiting Order or Quashing Order (O. 24, r. 6) | inert, reason 1 | | |
| 3810 | O 24 r 6(1): Where permission has been granted to apply for a Mandatory Order, Prohibiting Order or Qua... | encoded | `o 24 r 6(1) the application for the Order is made by summons in the originating application` | 4 |
| 3810 | O 24 r 6(2): Where permission has been granted to apply for a Mandatory Order, Prohibiting Order or Qua... | encoded | `o 24 r 6(2) fourteen days`; `o 24 r 6(2) the permission lapses` | 7 |
| 3811 | O 24 r 6(3): The order granting permission and the summons filed under paragraph (1) must be served on ... | fork (F-O24-1) | `o 24 r 6(3) the order granting permission and the summons are served on the defendant and the Attorney-General in time` | 4 |
| 3812 | O 24 r 6(4): The application mentioned in paragraph (1) must be heard by a Judge. | encoded | `o 24 r 6(4) the application is heard by a Judge` | 2 |
| 3813 | O 24 r 6(5): At the hearing, the Court may order that — ( a ) | encoded | `o 24 r 6(5) what the Court may order at the hearing`; `o 24 r 6(5) the Court may order this at the hearing` | 5 |
| 3813 to 3814 | O 24 r 6(5)(a): the application be dismissed; | encoded | `o 24 r 6(5) what the Court may order at the hearing`; `o 24 r 6(5) the Court may order this at the hearing` | 5 |
| 3815 to 3816 | O 24 r 6(5)(b): the application be served on some other persons; | encoded | `o 24 r 6(5) what the Court may order at the hearing`; `o 24 r 6(5) the Court may order this at the hearing` | 5 |
| 3817 to 3818 | O 24 r 6(5)(c): further affidavits be filed and served by the parties; or | encoded | `o 24 r 6(5) what the Court may order at the hearing`; `o 24 r 6(5) the Court may order this at the hearing` | 5 |
| 3819 to 3820 | O 24 r 6(5)(d): a Mandatory Order, Prohibiting Order or Quashing Order be made to take effect or to be com... | encoded | `o 24 r 6(5) what the Court may order at the hearing`; `o 24 r 6(5) the Court may order this at the hearing` | 5 |
| 3821 | O 24 r 6(6): Where the Court makes an order under paragraph (5)( d ), the solicitor appearing for the d... | fork (F-TIMED) | `o 24 r 6(6) the solicitor appearing for the defendant has informed the defendant or the appropriate person or entity`; `o 24 r 6(6) the defendant or the appropriate person or entity must comply with the relevant Order although it has not been served` | 5 |
| 3822 | O 24 r 6(7): Where the Court makes an order under paragraph (5)( d ) in the presence of the defendant o... | encoded | `o 24 r 6(7) the defendant or the appropriate person or entity must comply with the relevant Order although it has not been served` | 2 |
| 3823 | O 24 r 6(8): Subject to the Government Proceedings Act, where the Court makes an order under paragraph ... | encoded | `o 24 r 6(8)(a) the Court may also make a declaration`; `o 24 r 6(8)(b) the Court may also order that the applicant be awarded a liquidated amount, damages to be assessed or equitable relief` | 10 |
| 3823 to 3824 | O 24 r 6(8)(a): make a declaration which is ancillary to or consequential upon the Order; or | encoded | `o 24 r 6(8)(a) the Court may also make a declaration` | 5 |
| 3825 to 3826 | O 24 r 6(8)(b): order that the applicant be awarded a liquidated amount, damages to be assessed or equitab... | encoded | `o 24 r 6(8)(b) the Court may also order that the applicant be awarded a liquidated amount, damages to be assessed or equitable relief` | 5 |
| 3827 to 3829 | O 24A heading: ORDER 24A | inert, reason 1 | | |
| 3830 | O 24A r 1 heading: Interpretation and mode of application (O. 24A, r. 1) | inert, reason 1 | | |
| 3831 | O 24A r 1(1): In this Order, “Act” means the Supreme Court of Judicature Act 1969, and any reference to ... | encoded | `o 24A r 1(1) "Act" is the Supreme Court of Judicature Act 1969`; `o 24A r 1(1) a reference to a section is a reference to a section in the Act` | 6 |
| 3831 | O 24A r 1(1) “Act”: (1) In this Order, “Act” means the Supreme Court of Judicature Act 1969, and any reference... | encoded | `o 24A r 1(1) "Act" is the Supreme Court of Judicature Act 1969`; `o 24A r 1(1) a reference to a section is a reference to a section in the Act` | 6 |
| 3831 | O 24A r 1(2): In this Order, “Act” means the Supreme Court of Judicature Act 1969, and any reference to ... | encoded | `o 24A r 1(2) the expression has the meaning given by section 60F` | 3 |
| 3832 | O 24A r 1(3): An application to which this Order applies must be made — ( a ) | encoded | `o 24A r 1(3) the application`; `o 24A r 1(3) how the application is made`; `o 24A r 1(3) the application is made in the way required` | 7 |
| 3832 to 3833 | O 24A r 1(3)(a): in the case of an application for PACC permission, by originating application; and | encoded | `o 24A r 1(3) the application`; `o 24A r 1(3) how the application is made`; `o 24A r 1(3) the application is made in the way required` | 7 |
| 3834 to 3835 | O 24A r 1(3)(b): in the case of a PACC application, by summons in the originating application in which the ... | encoded | `o 24A r 1(3) the application`; `o 24A r 1(3) how the application is made`; `o 24A r 1(3) the application is made in the way required` | 7 |
| 3836 | O 24A r 2 heading: Application for PACC permission (O. 24A, r. 2) | inert, reason 1 | | |
| 3837 | O 24A r 2(1): For the purposes of section 60G(3), an application for PACC permission must be fixed for h... | fork (F-O24A-1) | `o 24A r 2(1) twenty-one days`; `o 24A r 2(1) the application for PACC permission is fixed for hearing within 21 days after it is filed` | 6 |
| 3837 | O 24A r 2(2): For the purposes of section 60G(3), an application for PACC permission must be fixed for h... | encoded | `o 24A r 2(2) the written submissions and the other documents are filed at the same time as the application` | 3 |
| 3838 | O 24A r 2(3): The written submissions mentioned in paragraph (2) are subject to a page limit of 35 pages... | encoded | `o 24A r 2(3) the page limit for the applicant's written submissions`; `o 24A r 2(3) the written submissions are within the page limit` | 5 |
| 3839 | O 24A r 2(4): For the purposes of section 60G(4), the other documents that the applicant in an applicati... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(a) the counsel's affidavit states all the matte`; ... (6 names) | 30 |
| 3839 | O 24A r 2(4)(a): (4) For the purposes of section 60G(4), the other documents that the applicant in an appli... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3840 to 3841 | O 24A r 2(4)(a)(i): the date on which each counsel was instructed, and who instructed each counsel; | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3842 to 3843 | O 24A r 2(4)(a)(ii): the material (being evidence or legal arguments) that will be relied on in the PACC applic... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3844 to 3845 | O 24A r 2(4)(a)(iii): the date on which the material mentioned in sub‑paragraph (ii) was first obtained, regardl... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3846 to 3847 | O 24A r 2(4)(a)(iv): the reason why the material mentioned in sub‑paragraph (ii) could not have been adduced in... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3848 to 3849 | O 24A r 2(4)(a)(v): the reason for the length of the interval of time between the date mentioned in sub‑paragr... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3850 to 3851 | O 24A r 2(4)(a)(vi): whether any argument similar to that in the PACC application to be made had been made prev... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3852 | O 24A r 2(4)(a)(vii): (vii) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3853 to 3854 | O 24A r 2(4)(a)(vii)(A): the details of — (A) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3855 to 3857 | O 24A r 2(4)(a)(vii)(B): (B) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3858 | O 24A r 2(4)(a)(viii): (viii) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3859 to 3860 | O 24A r 2(4)(a)(viii)(A): the details of — (A) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3861 to 3863 | O 24A r 2(4)(a)(viii)(B): (B) | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3864 to 3865 | O 24A r 2(4)(a)(ix): that each counsel genuinely believes the PACC application to be made to be of merit; | fork (F-MUST) | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3866 to 3867 | O 24A r 2(4)(a)(x): the reason why each counsel believes the PACC application to be made to be of merit, inclu... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3868 to 3869 | O 24A r 2(4)(a)(xi): that each counsel is aware of the consequences of making a false statement in the affidavi... | encoded | `o 24A r 2(4)(a) matter stated by counsel`; `o 24A r 2(4)(a) the counsel's affidavit states all the matters required`; `o 24A r 2(4)(a) all the matters` | 17 |
| 3870 | O 24A r 2(4)(b): ( b ) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3871 to 3872 | O 24A r 2(4)(b)(i): the material (being evidence or legal arguments) that will be relied on in the PACC applic... | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3873 to 3874 | O 24A r 2(4)(b)(ii): the date on which the applicant first obtained the material mentioned in sub-paragraph (i)... | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3875 to 3876 | O 24A r 2(4)(b)(iii): the reason why the material mentioned in sub‑paragraph (i) could not have been adduced in ... | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3877 to 3878 | O 24A r 2(4)(b)(iv): the reason for the length of the interval of time between the date mentioned in sub‑paragr... | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3879 | O 24A r 2(4)(b)(v): (v) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3880 to 3881 | O 24A r 2(4)(b)(v)(A): the details of — (A) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3882 to 3884 | O 24A r 2(4)(b)(v)(B): (B) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3885 | O 24A r 2(4)(b)(vi): (vi) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3886 to 3887 | O 24A r 2(4)(b)(vi)(A): the details of — (A) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3888 to 3890 | O 24A r 2(4)(b)(vi)(B): (B) | encoded | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3891 to 3892 | O 24A r 2(4)(b)(vii): whether the applicant is or was assisted by any person or organisation in the commencement... | fork (F-MUST) | `o 24A r 2(4)(b) matter stated by the applicant`; `o 24A r 2(4)(b) the applicant's affidavit states all the matters required`; `o 24A r 2(4)(b) all the matters` | 13 |
| 3893 | O 24A r 2(5): To avoid doubt, any affidavit mentioned in sub-paragraph ( a ) or ( b ) of paragraph (4) m... | fork (F-MUST) | `o 24A r 2(5) the affidavit must state the information even though it relates to an event before 28 June 2024` | 3 |
| 3894 | O 24A r 2(6): The applicant in an application for PACC permission must serve the application, the writte... | encoded | `o 24A r 2(6) the applicant has served the application, the submissions and the other documents on the respondent` | 4 |
| 3895 | O 24A r 2(7): Paragraphs (8) and (9) apply to an applicant in any of the following circumstances: ( a ) | fork (F-UNSURE) | `o 24A r 2(7) paragraphs (8) and (9) apply to the applicant` | 7 |
| 3895 to 3896 | O 24A r 2(7)(a): an applicant was represented by one or more counsel when the application for PACC permissi... | encoded | `o 24A r 2(7) paragraphs (8) and (9) apply to the applicant` | 7 |
| 3897 to 3898 | O 24A r 2(7)(b): an applicant was not represented by any counsel when the application for PACC permission w... | encoded | `o 24A r 2(7) paragraphs (8) and (9) apply to the applicant` | 7 |
| 3899 | O 24A r 2(8): For the purposes of section 60G(4), the applicant mentioned in paragraph (7) must, within ... | fork (F-O24A-3) | `o 24A r 2(8) three days`; `o 24A r 2(8) the affidavit of the newly appointed counsel is filed within 3 days after the appointment`; `o 24A r 2(8) the affidavit states all the matters in paragraph (4)(a)(i) to (xi)` | 9 |
| 3900 | O 24A r 2(9): The applicant must serve every affidavit filed in accordance with paragraph (8) on the res... | encoded | `o 24A r 2(9) the applicant has served every affidavit filed under paragraph (8) on the respondent` | 2 |
| 3901 | O 24A r 2(10): For the purposes of section 60G(5), the respondent in an application for PACC permission m... | fork (F-O24A-3) | `o 24A r 2(10)(a) the respondent's written submissions are fi`; `o 24A r 2(10)(b)(i) the respondent's written submissions are`; `o 24A r 2(10)(b)(ii) the respondent's written submissions ar`; ... (4 names) | 13 |
| 3901 to 3902 | O 24A r 2(10)(a): within 3 days after the date on which the application is filed and served on the responden... | fork (F-O24A-3) | `o 24A r 2(10)(a) the respondent's written submissions are filed within 3 days after the application is filed and served on the respondent`; `o 24A r 2(10) the respondent may file written submissions within 3 days after the application is filed and served` | 3 |
| 3903 | O 24A r 2(10)(b): ( b ) | fork (F-O24A-3) | `o 24A r 2(10)(b)(i) the respondent's written submissions are filed within 3 days after the affidavit or affidavits are filed and served`; `o 24A r 2(10)(b)(ii) the respondent's written submissions are filed within 3 days after each affidavit is filed and served` | 10 |
| 3904 to 3905 | O 24A r 2(10)(b)(i): if the affidavit of the counsel or the joint affidavit made by all of the counsel (as the ... | fork (F-O24A-3) | `o 24A r 2(10)(b)(i) the respondent's written submissions are filed within 3 days after the affidavit or affidavits are filed and served`; `o 24A r 2(10) the respondent may file written submissions within 3 days after the application is filed and served` | 5 |
| 3906 to 3907 | O 24A r 2(10)(b)(ii): if more than one affidavit of any kind mentioned in paragraph (8) is filed and served on t... | fork (F-O24A-3) | `o 24A r 2(10)(b)(ii) the respondent's written submissions are filed within 3 days after each affidavit is filed and served`; `o 24A r 2(10) the respondent may file written submissions within 3 days after the application is filed and served` | 5 |
| 3908 | O 24A r 2(11): The written submissions mentioned in paragraph (10) are subject to a page limit of 35 page... | encoded | `o 24A r 2(11) the page limit for the respondent's written submissions`; `o 24A r 2(11) the respondent's written submissions are within the page limit` | 4 |
| 3909 | O 24A r 2(12): The respondent in an application for PACC permission may also file an affidavit in support... | encoded | `o 24A r 2(12) the respondent may file an affidavit in support at the same time as the written submissions` | 2 |
| 3910 | O 24A r 2(13): The Court of Appeal may allow the page limit mentioned in paragraphs (3) and (11) to be ex... | fork (F-UNSURE) | `o 24A r 2(13) the Court of Appeal may allow the page limit to be exceeded` | 2 |
| 3911 | O 24A r 3 heading: Hearing of PACC application (O. 24A, r. 3) | inert, reason 1 | | |
| 3912 | O 24A r 3(1): For the purposes of section 60H(1), where the Court of Appeal grants the application for P... | fork (F-O24A-3) | `o 24A r 3(1) three days`; `o 24A r 3(1) the PACC application is made within 3 days after permission is granted`; `o 24A r 3(1) the applicant must make the PACC application within 3 days after permission is granted` | 6 |
| 3912 | O 24A r 3(2): For the purposes of section 60H(1), where the Court of Appeal grants the application for P... | fork (F-O24A-1) | `o 24A r 3(2) the PACC application is fixed for hearing within 21 days after it is made` | 3 |
| 3913 | O 24A r 3(3): For the purposes of section 60H(2), the applicant must — ( a ) | encoded | `o 24A r 3(3)(a) the affidavit in support is filed at the same time as the PACC application`; `o 24A r 3(3)(b) the applicant's written submissions are filed within 3 days after the PACC application is made` | 5 |
| 3913 to 3914 | O 24A r 3(3)(a): file any affidavit in support of the PACC application at the same time as the filing of th... | encoded | `o 24A r 3(3)(a) the affidavit in support is filed at the same time as the PACC application` | 2 |
| 3915 to 3916 | O 24A r 3(3)(b): file written submissions in support of the PACC application within 3 days after the date o... | fork (F-O24A-3) | `o 24A r 3(3)(b) the applicant's written submissions are filed within 3 days after the PACC application is made` | 3 |
| 3917 | O 24A r 3(4): The applicant in a PACC application must serve the application, and any affidavit in suppo... | encoded | `o 24A r 3(4) the PACC application and the affidavit are served on the respondent within the day on which it is made` | 2 |
| 3918 | O 24A r 3(5): For the purposes of section 60H(3), any written submissions in response to a PACC applicat... | fork (F-O24A-3) | `o 24A r 3(5) the respondent's written submissions in response are filed within 3 days after the application is made and served` | 3 |
| 3919 | O 24A r 3(6): The written submissions mentioned in paragraphs (3)( b ) and (5) are subject to a page lim... | fork (F-O24A-2) | `o 24A r 3(6) the page limit for written submissions on the PACC application`; `o 24A r 3(6) the written submissions are within the page limit` | 4 |
| 3920 | O 24A r 3(7): The Court of Appeal may allow the page limit mentioned in paragraph (6) to be exceeded in ... | fork (F-UNSURE) | `o 24A r 3(7) the Court of Appeal may allow the page limit to be exceeded` | 2 |
| 3921 | O 24A r 3(8): Each party to a PACC application must serve its written submissions (if any) on every othe... | encoded | `o 24A r 3(8) the party serves its written submissions on every other party within the day on which they are filed` | 2 |
| 3922 | O 24A r 4 heading: Appointment of solicitor in application for PACC permission or PACC application (O. 24A, r... | inert, reason 1 | | |
| 3923 | O 24A r 4: Where an applicant in an application for PACC permission or a PACC application who is repr... | encoded | `o 24A r 4 the form of the notice of appointment`; `o 24A r 4 the applicant must file and serve a notice of appointment`; `o 24A r 4 the notice of appointment is filed and served as required` | 9 |
| 3924 to 3925 | O 25 heading: ORDER 25 | inert, reason 1 | | |
| 3926 | O 25 r 1 heading: Definitions of this Order (O. 25, r. 1) | inert, reason 1 | | |
| 3927 | O 25 r 1: In this Order — “Court ADR service” means a service provided by the State Courts for resol... | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3927 | O 25 r 1 “Court ADR service”: In this Order — “Court ADR service” means a service provided by the State Courts for resol... | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process` | 4 |
| 3928 | O 25 r 1 “court fees”: “court fees” includes all charges, commissions and fees payable under these Rules, and the... | encoded | `o 25 r 1 the payment is within court fees` | 8 |
| 3928 to 3929 | O 25 r 1(a): document fees payable on the filing or sealing of specified documents; | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3930 to 3931 | O 25 r 1(b): hearing fees payable for specified hearings; | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3932 to 3933 | O 25 r 1(c): fees for provision of a Court ADR service by the State Courts; | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3934 to 3935 | O 25 r 1(d): service provision fees payable for services to be provided or rendered by, or which requir... | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3936 to 3937 | O 25 r 1(e): search fees payable for a search to be made of court records; | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3938 to 3939 | O 25 r 1(f): fees relating to admiralty matters; | encoded | `o 25 r 1 "Court ADR service" is a service provided by the State Courts for resolving a dispute by an alternative dispute resolution process`; `o 25 r 1 kind of payment`; `o 25 r 1 the payment is within court fees`; `o 25 r 1 kind of person`; `o 25 r 1 the person is a court officer` | 20 |
| 3940 | O 25 r 1 “court officer”: “court officer” includes the Sheriff, a commissioner for oaths, interpreter, clerk, proces... | encoded | `o 25 r 1 the person is a court officer` | 8 |
| 3941 | O 25 r 2 heading: Court fees (O. 25, r. 2) | inert, reason 1 | | |
| 3942 | O 25 r 2(1): Court fees must be paid in the circumstances and the manner set out in this Order and in t... | encoded | `o 25 r 2(1) court fees are paid in the circumstances and the manner set out` | 2 |
| 3942 | O 25 r 2(2): Court fees must be paid in the circumstances and the manner set out in this Order and in t... | encoded | `o 25 r 2(2) paragraph (2) applies to the court fees` | 2 |
| 3942 to 3943 | O 25 r 2(2)(a): if the claim is for a liquidated demand, the value of the claim is that specified in the o... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3944 to 3945 | O 25 r 2(2)(b): if the claim is for unliquidated damages, the value of the claim is that estimated by the ... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3946 to 3947 | O 25 r 2(2)(c): if the claim relates to proceedings under the Probate and Administration Act, the value of... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3948 to 3949 | O 25 r 2(2)(d): if the claim does not include any claim mentioned above, the claim is deemed to have a val... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3950 to 3951 | O 25 r 2(2)(e): in the case of a bill of costs, the value of the claim is the total amount claimed in the ... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3952 | O 25 r 2(3): If the claim is for both liquidated demand and unliquidated damages, the value of the clai... | fork (F-O25-1) | `o 25 r 2 the value of the claim` | 7 |
| 3953 | O 25 r 2(4): Where the claim includes or consists of a claim in foreign currency, the value of the clai... | encoded | `o 25 r 2(4) the amount of the claim in Singapore dollars` | 2 |
| 3954 | O 25 r 2(5): The Registrar may, after determining the value of the claim as awarded by the Court, requi... | fork (F-ASSUMED) | `o 25 r 2(5) the Registrar may require the parties to pay the difference in the court fees`; `o 25 r 2(5) the Registrar may refund to the parties the excess court fees paid` | 8 |
| 3955 | O 25 r 2(6): For the purpose of this Rule, the value of the claim excludes non‑contractual interest. | encoded | `o 25 r 2(6) the amount counted towards the value of the claim` | 2 |
| 3956 | O 25 r 3 heading: Court powers relating to court fees (O. 25, r. 3) | inert, reason 1 | | |
| 3957 | O 25 r 3(1): The Court may, in any case — ( a ) | encoded | `o 25 r 3(1) order about court fees`; `o 25 r 3(1) the Court may make this order about court fees` | 4 |
| 3957 to 3958 | O 25 r 3(1)(a): waive or defer the payment of the whole or any part of court fees; | encoded | `o 25 r 3(1) order about court fees`; `o 25 r 3(1) the Court may make this order about court fees` | 4 |
| 3959 to 3960 | O 25 r 3(1)(b): refund the whole or any part of court fees paid; or | encoded | `o 25 r 3(1) order about court fees`; `o 25 r 3(1) the Court may make this order about court fees` | 4 |
| 3961 to 3962 | O 25 r 3(1)(c): order, at any time, that the whole or any part of court fees be paid by any party or be ap... | encoded | `o 25 r 3(1) order about court fees`; `o 25 r 3(1) the Court may make this order about court fees` | 4 |
| 3963 | O 25 r 3(2): The Court may also exercise the powers in paragraph (1) in accordance with the provisions ... | encoded | `o 25 r 3(2) the Court may exercise the powers in paragraph (1) in accordance with a Civil Procedure Convention` | 2 |
| 3964 | O 25 r 3(3): A request for refund of court fees must be made in writing — ( a ) | fork (F-MUST) | `o 25 r 3(3) one month` | 3 |
| 3964 to 3965 | O 25 r 3(3)(a): where the application is for a refund of hearing fees — within one month after the date of... | fork (F-MUST) | `o 25 r 3(3)(a) the date the month runs from`; `o 25 r 3(3)(a) the request for refund of hearing fees is made in writing within one month`; `o 25 r 3(3) one month` | 12 |
| 3966 to 3967 | O 25 r 3(3)(b): where the application is for a refund of fees for unused documents — within the time in Ru... | fork (F-MUST) | `o 25 r 3(3)(b) the request for refund of fees for unused documents is made in writing within the time in Rule 4(2)`; `o 25 r 3(3) one month` | 8 |
| 3968 to 3969 | O 25 r 3(3)(c): where the application is for a refund of fees for Court ADR services — within the time in ... | fork (F-MUST) | `o 25 r 3(3)(c) the request for refund of fees for Court ADR services is made in writing within the time in Rule 8(4)`; `o 25 r 3(3) one month` | 8 |
| 3970 to 3971 | O 25 r 3(3)(d): in any other case — within one month after the date on which the reason for the refund aro... | fork (F-MUST) | `o 25 r 3(3)(d) the request for refund in any other case is made in writing within one month after the reason for the refund arose`; `o 25 r 3(3) one month` | 8 |
| 3972 | O 25 r 3(4): In the case of hearing fees, the Court must refund the whole of the hearing fees paid if t... | fork (F-O25-3) | `o 25 r 3(4) fourteen days before the first date fixed for hearing`; `o 25 r 3(4) the Court must refund the whole of the hearing fees paid` | 7 |
| 3973 | O 25 r 3(5): Any party who is dissatisfied with any decision of the Registrar made under this Rule may ... | encoded | `o 25 r 3(5) fourteen days`; `o 25 r 3(5) the party may apply by letter to a Judge to review the decision within 14 days`; `o 25 r 3(5) a dissatisfied party may apply by letter to a Judge within 14 days after the decision` | 7 |
| 3974 | O 25 r 3(6): The Court may make such order as the Court deems fit to secure compliance with any require... | encoded | `o 25 r 3(6) the Court may make the order it deems fit` | 2 |
| 3975 | O 25 r 4 heading: Refund of fees paid for unused documents (O. 25, r. 4) | inert, reason 1 | | |
| 3976 | O 25 r 4(1): The Registrar may, if he or she thinks fit, refund any fee or part of the fee which has be... | encoded | `o 25 r 4(1) the Registrar may refund the fee or part of the fee` | 2 |
| 3976 | O 25 r 4(2): The Registrar may, if he or she thinks fit, refund any fee or part of the fee which has be... | encoded | `o 25 r 4(2)(b) three months`; `o 25 r 4(2)(a) the application for refund is made by request signed by the applicant or the applicant's solicitor`; `o 25 r 4(2)(b) the application for refund is made within 3 months after the date of payment` | 9 |
| 3976 to 3977 | O 25 r 4(2)(a): by request signed by the applicant or his or her solicitor; and | encoded | `o 25 r 4(2)(a) the application for refund is made by request signed by the applicant or the applicant's solicitor` | 4 |
| 3978 to 3979 | O 25 r 4(2)(b): within 3 months after the date of the payment of the fee to be refunded. | encoded | `o 25 r 4(2)(b) three months`; `o 25 r 4(2)(b) the application for refund is made within 3 months after the date of payment` | 5 |
| 3980 | O 25 r 4(3): Where a refund of the fees paid for more than one unused document is being sought, a separ... | encoded | `o 25 r 4(3) a separate application is made for the refund of the fee paid for each unused document` | 4 |
| 3981 | O 25 r 4(4): Where an application under this Rule for the refund of any fee is not approved, the fee pa... | encoded | `o 25 r 4(4) the fee paid for the request is not refundable` | 2 |
| 3982 | O 25 r 5 heading: No hearing fee for some proceedings (O. 25, r. 5) | inert, reason 1 | | |
| 3983 | O 25 r 5: A hearing fee is not payable for a hearing in relation to — ( a ) | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3983 to 3984 | O 25 r 5(a): actions for damages for death or personal injuries; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3985 | O 25 r 5(b): ( b ) | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3986 to 3987 | O 25 r 5(b)(i): Adoption of Children Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3988 to 3989 | O 25 r 5(b)(ii): Guardianship of Infants Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3990 to 3991 | O 25 r 5(b)(iii): Inheritance (Family Provision) Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3992 to 3993 | O 25 r 5(b)(iv): Maintenance of Parents Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3994 to 3995 | O 25 r 5(b)(v): Mental Capacity Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3996 to 3997 | O 25 r 5(b)(vi): Mental Health (Care and Treatment) Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 3998 to 3999 | O 25 r 5(b)(vii): Women’s Charter; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4000 to 4001 | O 25 r 5(c): any application for an Order for Review of Detention and appeals relating to such applicat... | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4002 | O 25 r 5(d): ( d ) | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4003 to 4004 | O 25 r 5(d)(i): Accountants Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4005 to 4006 | O 25 r 5(d)(ii): Architects Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4007 to 4008 | O 25 r 5(d)(iii): Dental Registration Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4009 to 4010 | O 25 r 5(d)(iv): Land Surveyors Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4011 to 4012 | O 25 r 5(d)(v): Legal Profession Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4013 to 4014 | O 25 r 5(d)(vi): Medical Registration Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4015 to 4016 | O 25 r 5(d)(vii): Nurses and Midwives Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4017 to 4018 | O 25 r 5(d)(viii): Pharmacists Registration Act; | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4019 to 4020 | O 25 r 5(d)(ix): Professional Engineers Act. | encoded | `o 25 r 5 proceeding`; `o 25 r 5 no hearing fee is payable` | 19 |
| 4021 | O 25 r 6 heading: Hearing fee payable for winding up applications (O. 25, r. 6) | inert, reason 1 | | |
| 4022 | O 25 r 6: Hearing fees are payable in proceedings relating to the winding up of companies, limited l... | encoded | `o 25 r 6 entity wound up`; `o 25 r 6 hearing fees are payable` | 11 |
| 4023 | O 25 r 7 heading: Exemption where cause or matter relates to criminal proceedings (O. 25, r. 7) | inert, reason 1 | | |
| 4024 | O 25 r 7(1): Where the Registrar is satisfied that any cause or matter relates to or is predicated upon... | fork (F-ASSUMED) | `o 25 r 7(1) the Registrar may issue a certificate of exemption` | 4 |
| 4024 | O 25 r 7(2): Where the Registrar is satisfied that any cause or matter relates to or is predicated upon... | encoded | `o 25 r 7(2) the application for a certificate is made as required` | 5 |
| 4025 | O 25 r 7(3): Despite any other provision in these Rules — ( a ) | encoded | `o 25 r 7(3)(a) no fee is payable by any party in the cause or matter`; `o 25 r 7(3)(b) no security for costs is required to be provided by any party in the cause or matter` | 8 |
| 4025 to 4026 | O 25 r 7(3)(a): no fee is payable; and | encoded | `o 25 r 7(3)(a) no fee is payable by any party in the cause or matter` | 4 |
| 4027 to 4029 | O 25 r 7(3)(b): by any party in the cause or matter, including any appeal relating to such cause or matter... | encoded | `o 25 r 7(3)(b) no security for costs is required to be provided by any party in the cause or matter` | 4 |
| 4030 | O 25 r 7(4): The Registrar may, if he or she thinks fit, refund any fee or part of the fee which has be... | encoded | `o 25 r 7(4) the Registrar may refund the fee or part of the fee` | 4 |
| 4031 | O 25 r 7(5): Nothing in this Rule prevents an order for costs from being made by the Court in favour of... | encoded | `o 25 r 7(5) this Rule prevents the Court from making the order for costs` | 2 |
| 4032 | O 25 r 8 heading: Court ADR fees in District Court (O. 25, r. 8) | inert, reason 1 | | |
| 4033 | O 25 r 8(1): Subject to this Rule, a fee of $250 is payable by each party in a case in a District Court... | encoded | `o 25 r 8(1) the Court ADR fee payable by each party for all `; `o 25 r 8(1) the Court ADR fee is payable by the party`; `o 25 r 8(1) the total Court ADR fee payable by the parties i`; ... (4 names) | 20 |
| 4033 | O 25 r 8(2): Subject to this Rule, a fee of $250 is payable by each party in a case in a District Court... | encoded | `o 25 r 8(2) how the first Court ADR service came to be provided`; `o 25 r 8(2) the Court ADR fee is payable at the date asked about` | 7 |
| 4033 to 4034 | O 25 r 8(2)(a): a request made for the Court ADR service by any party in the case; | encoded | `o 25 r 8(2) how the first Court ADR service came to be provided`; `o 25 r 8(2) the Court ADR fee is payable at the date asked about` | 7 |
| 4035 to 4036 | O 25 r 8(2)(b): a referral by the Court or the Registrar. | encoded | `o 25 r 8(2) how the first Court ADR service came to be provided`; `o 25 r 8(2) the Court ADR fee is payable at the date asked about` | 7 |
| 4037 | O 25 r 8(3): No Court ADR fee is payable in any of the following actions: ( a ) | fork (F-O25-2) | `o 25 r 8(3) kind of action`; `o 25 r 8(3) no Court ADR fee is payable in the action` | 8 |
| 4037 to 4038 | O 25 r 8(3)(a): any non‑injury motor accident action (as defined in Order 21, Part 6 of Appendix 1); | fork (F-O25-2) | `o 25 r 8(3) kind of action`; `o 25 r 8(3) no Court ADR fee is payable in the action` | 8 |
| 4039 to 4040 | O 25 r 8(3)(b): any action for damages for death or personal injuries; | fork (F-O25-2) | `o 25 r 8(3) kind of action`; `o 25 r 8(3) no Court ADR fee is payable in the action` | 8 |
| 4041 to 4042 | O 25 r 8(3)(c): any action under the Protection from Harassment Act; | fork (F-O25-2) | `o 25 r 8(3) kind of action`; `o 25 r 8(3) no Court ADR fee is payable in the action` | 8 |
| 4043 to 4044 | O 25 r 8(3)(d): any action under the Community Disputes Resolution Act 2015. | fork (F-O25-2) | `o 25 r 8(3) kind of action`; `o 25 r 8(3) no Court ADR fee is payable in the action` | 8 |
| 4045 | O 25 r 8(4): Any party requesting a refund of the whole or any part of the Court ADR fee, pursuant to R... | encoded | `o 25 r 8(4) one month`; `o 25 r 8(4) the earlier of the two dates`; `o 25 r 8(4) the request for refund of the Court ADR fee is made in writing to the Registrar within one month` | 11 |
| 4045 to 4046 | O 25 r 8(4)(a): the date of a written withdrawal of consent by any party to proceed with any Court ADR ser... | encoded | `o 25 r 8(4) one month`; `o 25 r 8(4) the earlier of the two dates`; `o 25 r 8(4) the request for refund of the Court ADR fee is made in writing to the Registrar within one month` | 11 |
| 4047 to 4048 | O 25 r 8(4)(b): the date of settlement or discontinuance of the case. | encoded | `o 25 r 8(4) one month`; `o 25 r 8(4) the earlier of the two dates`; `o 25 r 8(4) the request for refund of the Court ADR fee is made in writing to the Registrar within one month` | 11 |
| 4049 | O 25 r 8(5): In this Rule, “Court ADR fee” means the fee payable under paragraph (1) for Court ADR serv... | encoded | `o 25 r 8(5) "Court ADR fee" is the fee payable under paragraph (1) for Court ADR services` | 2 |
| 4049 | O 25 r 8(5) “Court ADR fee”: (5) In this Rule, “Court ADR fee” means the fee payable under paragraph (1) for Court ADR ... | encoded | `o 25 r 8(5) "Court ADR fee" is the fee payable under paragraph (1) for Court ADR services` | 2 |
| 4050 to 4051 | O 26 heading: ORDER 26 | inert, reason 1 | | |
| 4052 | O 26 r 1 heading: Registry of Supreme Court and of State Courts (O. 26, r. 1) | inert, reason 1 | | |
| 4053 | O 26 r 1(1): There is a Registry with such departments and functions as the Chief Justice or the Presid... | encoded | `o 26 r 1(1) the office that directs the departments and functions of the Registry` | 2 |
| 4053 | O 26 r 1(2): There is a Registry with such departments and functions as the Chief Justice or the Presid... | encoded | `o 26 r 1(2) the office to whom the Registrar must report and be responsible for the proper administration and functions of the Registry` | 2 |
| 4054 | O 26 r 1(3): The Chief Justice or the Presiding Judge of the State Courts (as the case may be) may appo... | encoded | `o 26 r 1(3) the office may appoint a Chief Executive and one or more Assistant Chief Executives`; `o 26 r 1(3) the office to whom the Chief Executive and the Assistant Chief Executives must report and be responsible for the proper discharge of the functions they manage` | 7 |
| 4055 | O 26 r 2 heading: Practice directions (O. 26, r. 2) | inert, reason 1 | | |
| 4056 | O 26 r 2: The Registrar may issue practice directions from time to time with the approval of the Chi... | fork (F-O26-1) | `o 26 r 2 the directions are issued under Order 26, Rule 2` | 8 |
| 4057 | O 26 r 3 heading: Registry records (O. 26, r. 3) | inert, reason 1 | | |
| 4058 | O 26 r 3(1): The Registry must maintain such Court records and other documents that are required by any... | encoded | `o 26 r 3(1) the Registry maintains the Court records and other documents` | 3 |
| 4058 | O 26 r 3(2): The Registry must maintain such Court records and other documents that are required by any... | encoded | `o 26 r 3(2) the Registry may collect, use or disclose the data` | 2 |
| 4059 | O 26 r 3(3): The method of collection, the storage and the period of storage of Court records, document... | encoded | `o 26 r 3(3) matter`; `o 26 r 3(3) the matter is in the discretion of the Registrar` | 4 |
| 4060 | O 26 r 3(4): The Registrar may allow any person to search for, inspect and take a copy of any document ... | encoded | `o 26 r 3(4) the Registrar may allow the person to search for, inspect and take a copy of the document` | 4 |
| 4060 to 4061 | O 26 r 3(4)(a): shows a valid interest in the document in question; and | encoded | `o 26 r 3(4) the Registrar may allow the person to search for, inspect and take a copy of the document` | 4 |
| 4062 to 4063 | O 26 r 3(4)(b): pays the prescribed fee. | encoded | `o 26 r 3(4) the Registrar may allow the person to search for, inspect and take a copy of the document` | 4 |
| 4064 | O 26 r 3(5): The Registrar may redact any document in the interests of justice before a person searches... | fork (F-UNSURE) | `o 26 r 3(5) the Registrar may redact the document before a person searches for, inspects or takes a copy of it` | 2 |
| 4065 | O 26 r 3(6): Documents filed in Court in any action and the Registry’s records must not be taken out of... | encoded | `o 26 r 3(6) the document or record may be taken out of the Registry` | 2 |
| 4066 | O 26 r 3(7): Documents filed in Court must be typewritten and printed and must comply with practice dir... | fork (F-MUST) | `o 26 r 3(7) the document filed in Court is typewritten, printed and complies with the practice directions` | 3 |
| 4067 | O 26 r 3(8): The Registrar may authorise a person to provide a service that enables a subscriber of tha... | encoded | `o 26 r 3(8) the Registrar may authorise a person to provide the service` | 4 |
| 4067 to 4068 | O 26 r 3(8)(a): to search such information relating to Court records and other documents mentioned in para... | encoded | `o 26 r 3(8) the Registrar may authorise a person to provide the service` | 4 |
| 4069 to 4070 | O 26 r 3(8)(b): to search for, inspect and take a copy of any such documents filed in the Registry as the ... | encoded | `o 26 r 3(8) the Registrar may authorise a person to provide the service` | 4 |
| 4071 | O 26 r 3(9): The person authorised to provide the service mentioned in paragraph (8) must pay to the Re... | encoded | `o 26 r 3(9) the person authorised has paid the fees for access to the information and documents` | 2 |
| 4072 | O 26 r 3(10): Despite paragraph (4), a subscriber of the service mentioned in paragraph (8) is entitled,... | encoded | `o 26 r 3(10) what the subscriber does`; `o 26 r 3(10) the subscriber may do this without paying the prescribed fee and without the Registrar's permission` | 5 |
| 4072 to 4073 | O 26 r 3(10)(a): to search the information mentioned in paragraph (8)( a ), without paying the prescribed f... | encoded | `o 26 r 3(10) what the subscriber does`; `o 26 r 3(10) the subscriber may do this without paying the prescribed fee and without the Registrar's permission` | 5 |
| 4074 to 4075 | O 26 r 3(10)(b): to search for, inspect and take a copy of any document mentioned in paragraph (8)( b ), wi... | encoded | `o 26 r 3(10) what the subscriber does`; `o 26 r 3(10) the subscriber may do this without paying the prescribed fee and without the Registrar's permission` | 5 |
| 4076 | O 26 r 4 heading: Filing of powers of attorney (O. 26, r. 4) | inert, reason 1 | | |
| 4077 | O 26 r 4(1): A document or a certified copy of a document creating a power of attorney may be deposited... | encoded | `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court`; `o 26 r 4(1) the Registry in which the document creating a power of attorney may be deposited` | 8 |
| 4077 | O 26 r 4(1)(a): (1) A document or a certified copy of a document creating a power of attorney may be depos... | encoded | `o 26 r 4(1)(a) how the execution of the document is verified`; `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court`; `o 26 r 4(1) the Registry in which the document creating a power of attorney may be deposited` | 8 |
| 4078 to 4079 | O 26 r 4(1)(a)(i): an affidavit or a statutory declaration made by a witness to the execution or by an impart... | encoded | `o 26 r 4(1)(a) how the execution of the document is verified` | 0 |
| 4080 to 4081 | O 26 r 4(1)(a)(ii): the signature of a commissioner for oaths as a witness to the execution; or | encoded | `o 26 r 4(1)(a) how the execution of the document is verified` | 0 |
| 4082 to 4083 | O 26 r 4(1)(a)(iii): such other evidence which is satisfactory to the Registrar; | encoded | `o 26 r 4(1)(a) how the execution of the document is verified` | 0 |
| 4084 to 4085 | O 26 r 4(1)(b): the document is accompanied by the affidavit, statutory declaration, certificate or other ... | encoded | `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court`; `o 26 r 4(1) the Registry in which the document creating a power of attorney may be deposited` | 8 |
| 4086 to 4087 | O 26 r 4(1)(c): in the case of a certified copy of the document, the signature of the person who verified ... | encoded | `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court`; `o 26 r 4(1) the Registry in which the document creating a power of attorney may be deposited` | 8 |
| 4088 | O 26 r 4(2): The Registry of the Supreme Court must maintain an index of all documents or certified cop... | encoded | `o 26 r 4(2) the Registry of the Supreme Court maintains the index` | 3 |
| 4089 | O 26 r 4(3): Any person is, on payment of the prescribed fee, entitled — ( a ) | encoded | `o 26 r 4(3) what the person may do`; `o 26 r 4(3) the person is entitled to do this` | 7 |
| 4089 to 4090 | O 26 r 4(3)(a): to search the index mentioned in paragraph (2); | encoded | `o 26 r 4(3) what the person may do`; `o 26 r 4(3) the person is entitled to do this` | 7 |
| 4091 to 4092 | O 26 r 4(3)(b): to inspect any document filed or deposited in the Registry in accordance with paragraph (1... | encoded | `o 26 r 4(3) what the person may do`; `o 26 r 4(3) the person is entitled to do this` | 7 |
| 4093 to 4094 | O 26 r 4(3)(c): to be supplied with a copy or a certified copy of such document. | encoded | `o 26 r 4(3) what the person may do`; `o 26 r 4(3) the person is entitled to do this` | 7 |
| 4095 | O 26 r 5 heading: Registry hours (O. 26, r. 5) | inert, reason 1 | | |
| 4096 | O 26 r 5(1): The Registry must be open on every day of the year except non‑court days. (2) The Registry... | encoded | `o 26 r 5(1) the Registry must be open on the day` | 5 |
| 4096 | O 26 r 5(2): The Registry must be open on every day of the year except non‑court days. (2) The Registry... | inert, reason 2 (machinery: the opening hours are "as directed by the Chief Justice or the Presiding Judge"; the text gives none and there is no fact to ask; no function) | | |
| 4097 | O 26 r 6 heading: Court vacations (O. 26, r. 6) | inert, reason 1 | | |
| 4098 | O 26 r 6: There must be a Judge available during the Court vacations to hear such matters as the Reg... | fork (F-ASSUMED) | `o 26 r 6 a Judge is available during the Court vacations to hear the matter` | 5 |
| 4099 to 4100 | O 27 heading: ORDER 27 | inert, reason 1 | | |
| 4101 | O 27 r 1 heading: Definitions of this Order (O. 27, r. 1) | inert, reason 1 | | |
| 4102 | O 27 r 1: In this Order — “bank” means a bank approved by the Accountant‑General; | encoded | `o 27 r 1 "bank" is a bank approved by the Accountant-General`; `o 27 r 1 "carry over" is to transfer the fund or any part of`; `o 27 r 1 "funds" is money, securities or other investments s`; ... (8 names) | 28 |
| 4102 | O 27 r 1 “bank”: In this Order — “bank” means a bank approved by the Accountant‑General; | encoded | `o 27 r 1 "bank" is a bank approved by the Accountant-General` | 2 |
| 4103 | O 27 r 1 “carry over”: “carry over”, in relation to a fund in Court, means to transfer the fund or any part of th... | encoded | `o 27 r 1 "carry over" is to transfer the fund or any part of it from one account to another in the books of the Accountant-General` | 4 |
| 4104 | O 27 r 1 “funds”: “funds” or “funds in Court” means any money, securities, or other investments standing or ... | encoded | `o 27 r 1 "funds" is money, securities or other investments standing or to be placed to the account of the Accountant-General, and includes money placed on deposit`; `o 27 r 1 "interest" is the dividends and interest on funds` | 10 |
| 4105 | O 27 r 1 “interest”: “interest” means the dividends and interest on funds; | encoded | `o 27 r 1 "interest" is the dividends and interest on funds` | 4 |
| 4106 | O 27 r 1 “ledger credit”: “ledger credit” means the title of the cause or matter and the separate account opened or ... | encoded | `o 27 r 1 "ledger credit" is the title of the cause or matter and the separate account opened under an order or otherwise` | 4 |
| 4107 | O 27 r 1 “lodge in Court”: “lodge in Court” means pay or transfer into Court, or deposit in Court; | encoded | `o 27 r 1 "lodge in Court" act`; `o 27 r 1 "lodge in Court" is to pay or transfer into Court, or deposit in Court` | 4 |
| 4108 | O 27 r 1 “order”: “order” means an order or judgment of a Court, whether made in Court or in chambers, as th... | encoded | `o 27 r 1 "ledger credit" is the title of the cause or matter and the separate account opened under an order or otherwise`; `o 27 r 1 "order" is an order or judgment of a Court, whether made in Court or in chambers` | 8 |
| 4109 | O 27 r 2 heading: Payment into Court under Trustees Act (O. 27, r. 2) | inert, reason 1 | | |
| 4110 | O 27 r 2(1): Subject to paragraph (2), any trustee wishing to make a payment into Court under section 6... | encoded | `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required`; `o 27 r 2(1) the summons must be supported by an affidavit` | 13 |
| 4110 to 4111 | O 27 r 2(1)(a): a short description of the trust and of the instrument creating it or (as the case may be)... | encoded | `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required`; `o 27 r 2(1) the summons must be supported by an affidavit` | 13 |
| 4112 to 4113 | O 27 r 2(1)(b): the names of the persons interested in or entitled to the money or securities to be paid i... | encoded | `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required`; `o 27 r 2(1) the summons must be supported by an affidavit` | 13 |
| 4114 to 4115 | O 27 r 2(1)(c): the trustee’s submission to answer all such inquiries relating to the application of such ... | encoded | `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required`; `o 27 r 2(1) the summons must be supported by an affidavit` | 13 |
| 4116 to 4117 | O 27 r 2(1)(d): an address where the trustee may be served with any summons or order, or notice of any pro... | encoded | `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required`; `o 27 r 2(1) the summons must be supported by an affidavit` | 13 |
| 4118 | O 27 r 2(2): Where money or securities represents a legacy, or residue or any share of a legacy, to whi... | encoded | `o 27 r 2(2) paragraph (2) says no affidavit need be filed under paragraph (1)` | 4 |
| 4119 | O 27 r 3 heading: Notice of lodgment (O. 27, r. 3) | inert, reason 1 | | |
| 4120 | O 27 r 3: Any person who has lodged money or securities in Court must forthwith give notice of the l... | fork (F-TIMED) | `o 27 r 3 the person has given notice of the lodgment`; `o 27 r 3 the person who must give notice of the lodgment`; `o 27 r 3 the persons to whom the notice must be given`; `o 27 r 3 when the notice must be given`; `o 27 r 3 the person who lodged must give notice of the lodgment` | 6 |
| 4121 | O 27 r 4 heading: Funds how lodged (O. 27, r. 4) | inert, reason 1 | | |
| 4122 | O 27 r 4(1): Money to be lodged in Court must be lodged by means of a direction to the Accountant‑Gener... | encoded | `o 27 r 4(1) the form of the direction to the Accountant-General`; `o 27 r 4(1) the money is lodged in Court by means of a direction in the form required` | 3 |
| 4122 | O 27 r 4(2): Money to be lodged in Court must be lodged by means of a direction to the Accountant‑Gener... | encoded | `o 27 r 4(2) the securities may be transferred to the Accountant-General in his or her official name` | 4 |
| 4123 | O 27 r 4(3): The person lodging under paragraph (2) must execute a transfer of the securities, and send... | encoded | `o 27 r 4(3) the form of the authority`; `o 27 r 4(3) the person lodging has executed and sent the transfer with the authority` | 5 |
| 4124 | O 27 r 4(4): Such company or body corporate must, after registering such transfer, forward the authorit... | encoded | `o 27 r 4(4) the company or body corporate has forwarded the authority with the certificate` | 3 |
| 4125 | O 27 r 4(5): Securities, other than those described in paragraph (2), may be placed in a box or packet ... | encoded | `o 27 r 4(5) the securities may be placed in a box or packet and lodged with the Accountant-General` | 4 |
| 4126 | O 27 r 4(6): After inspecting the contents in the box or packet in the presence of the person lodging t... | encoded | `o 27 r 4(6) the Accountant-General has received the box or packet and given a receipt` | 4 |
| 4127 | O 27 r 4(7): The Accountant‑General must, after receiving the money or securities, send to the Registra... | encoded | `o 27 r 4(7) the Accountant-General has sent the Registrar a copy of the receipt` | 3 |
| 4128 | O 27 r 5 heading: Crediting lodgment and dividends (O. 27, r. 5) | inert, reason 1 | | |
| 4129 | O 27 r 5: Any principal money or dividends received by the Accountant‑General in respect of securiti... | encoded | `o 27 r 5 what was received`; `o 27 r 5 the credit to which the Accountant-General places the amount in his or her books` | 3 |
| 4129 to 4130 | O 27 r 5(a): in the case of principal money — to the credit to which the securities whereon such money ... | encoded | `o 27 r 5 what was received`; `o 27 r 5 the credit to which the Accountant-General places the amount in his or her books` | 3 |
| 4131 to 4132 | O 27 r 5(b): in the case of dividends — to the credit to which the securities whereon such dividends we... | encoded | `o 27 r 5 what was received`; `o 27 r 5 the credit to which the Accountant-General places the amount in his or her books` | 3 |
| 4133 | O 27 r 6 heading: Interest on money lodged in Court (O. 27, r. 6) | inert, reason 1 | | |
| 4134 | O 27 r 6(1): Money lodged in Court to the credit of any account is deemed to be placed on deposit, and ... | encoded | `o 27 r 6(1) the money lodged in Court is deemed to be placed on deposit and is credited with interest`; `o 27 r 6(1) the rate of interest credited is one the Rule allows` | 13 |
| 4134 to 4135 | O 27 r 6(1)(a): when money is paid into Court under Order 9, Rule 17, Order 14 or Order 33, or as security... | encoded | `o 27 r 6(1)(a) the money is paid into Court under Order 9, Rule 17, Order 14 or Order 33, or as security for costs`; `o 27 r 6(1) the money lodged in Court is deemed to be placed on deposit and is credited with interest`; `o 27 r 6(1) the rate of interest credited is one the Rule allows` | 23 |
| 4136 to 4137 | O 27 r 6(1)(b): when the amount is less than $30,000. | fork (F-O27-3) | `o 27 r 6(1) the money lodged in Court is deemed to be placed on deposit and is credited with interest`; `o 27 r 6(1) the rate of interest credited is one the Rule allows` | 13 |
| 4138 | O 27 r 6(2): Such money is deemed not to be placed on deposit when the amount is reduced below $30,000. | encoded | `o 27 r 6(2) the money is deemed not to be placed on deposit` | 3 |
| 4139 | O 27 r 7 heading: Computation of interest (O. 27, r. 7) | inert, reason 1 | | |
| 4140 | O 27 r 7(1): Interest upon money on deposit must not be computed on a fraction of $1. (2) Interest upon... | encoded | `o 27 r 7(1) interest on money on deposit may be computed on the amount` | 3 |
| 4140 | O 27 r 7(2): Interest upon money on deposit must not be computed on a fraction of $1. (2) Interest upon... | fork (F-TIMED) | `o 27 r 7(2) period`; `o 27 r 7(2) interest on money on deposit is computed by the period` | 3 |
| 4141 | O 27 r 7(3): Such interest begins on the first day of the calendar month next succeeding that in which ... | fork (F-O27-1) | `o 27 r 7(3) the first day on which interest begins`; `o 27 r 7(3) the day from which interest ceases` | 8 |
| 4142 | O 27 r 7(4): Interest which has accrued for or during the year ending on 31 December in every year, on ... | encoded | `o 27 r 7(4) fifteen days after the end of the year`; `o 27 r 7(4) the day the 15 days run from`; `o 27 r 7(4) the interest for the year is placed to the credi`; ... (4 names) | 5 |
| 4143 | O 27 r 7(5): When money on deposit is withdrawn from deposit, the interest on the money which has accru... | encoded | `o 27 r 7(5) the interest accrued and not credited is placed to the credit to which the money is then standing` | 3 |
| 4144 | O 27 r 7(6): When money on deposit consists of sums which have been placed on deposit at different time... | encoded | `o 27 r 7(6) the part is treated as withdrawn for the purpose of computing interest` | 5 |
| 4145 | O 27 r 7(7): Unless otherwise directed by an order, interest credited on money on deposit must, when or... | encoded | `o 27 r 7(7) the interest credited is placed on deposit`; `o 27 r 7(7) the day the interest is treated as placed on deposit` | 5 |
| 4146 | O 27 r 8 heading: Payment out of funds in Court (O. 27, r. 8) | inert, reason 1 | | |
| 4147 | O 27 r 8: Money paid into Court must be paid out on a direction to the Accountant‑General in Form 44... | encoded | `o 27 r 8 the form of the direction to the Accountant-General`; `o 27 r 8 the money is paid out on a direction in the form required` | 3 |
| 4148 | O 27 r 9 heading: Name of payee to be stated in order (O. 27, r. 9) | inert, reason 1 | | |
| 4149 | O 27 r 9(1): Every order which directs funds in Court to be paid, transferred, or delivered out must st... | encoded | `o 27 r 9(1) the order states the name of every payee` | 4 |
| 4149 | O 27 r 9(2): Every order which directs funds in Court to be paid, transferred, or delivered out must st... | fork (F-ASSUMED) | `o 27 r 9(2) it is sufficient for the order to state the business name of the firm` | 3 |
| 4150 | O 27 r 9(3): When money in Court is by an order directed to be paid to any persons described in the ord... | encoded | `o 27 r 9(3) to whom the money is paid`; `o 27 r 9(3) the money may be paid to the payee` | 4 |
| 4151 | O 27 r 10 heading: Payment out on death of payee (O. 27, r. 10) | inert, reason 1 | | |
| 4152 | O 27 r 10(1): When funds in Court are by an order directed to be paid, transferred, or delivered to any ... | fork (F-ASSUMED, F-TIMED) | `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | 6 |
| 4152 to 4153 | O 27 r 10(1)(a): on or after the date of such order; or | encoded | `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | 6 |
| 4154 to 4156 | O 27 r 10(1)(b): be paid, transferred or delivered to the legal personal representatives of the deceased pe... | encoded | `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | 6 |
| 4157 | O 27 r 10(2): Paragraph (1) does not apply to an order directing funds in Court to be paid, transferred ... | encoded | `o 27 r 10(2) paragraph (1) applies to the order` | 4 |
| 4157 to 4158 | O 27 r 10(2)(a): as trustee, executor or administrator; or | encoded | `o 27 r 10(2) paragraph (1) applies to the order` | 4 |
| 4159 to 4160 | O 27 r 10(2)(b): otherwise than in his or her own right, or for his or her own use. | encoded | `o 27 r 10(2) paragraph (1) applies to the order` | 4 |
| 4161 | O 27 r 10(3): If no administration has been taken out to the estate of such deceased person who has died... | fork (F-O27-4) | `o 27 r 10(3) relation to the deceased`; `o 27 r 10(3) the asset ceiling`; `o 27 r 10(3) the form of the declaration`; `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | 15 |
| 4162 | O 27 r 10(4): When funds in Court are by an order directed to be paid, transferred, or delivered to any ... | encoded | `o 27 r 10(4) the funds may be paid, transferred or delivered to the survivor or survivors` | 3 |
| 4163 | O 27 r 10(5): When any application for an order mentioned in paragraphs (1) and (4) is made, notice of t... | encoded | `o 27 r 10(5) notice of the application has been given to the Commissioner of Estate Duty` | 3 |
| 4164 | O 27 r 11 heading: Transfer of investment of funds in Court (O. 27, r. 11) | inert, reason 1 | | |
| 4165 | O 27 r 11(1): When funds in Court are by an order directed to be transferred or carried over, the party ... | encoded | `o 27 r 11(1) the party having the carriage of the order has lodged a copy with the Accountant-General`; `o 27 r 11(1) the party who must lodge a copy of the order with the Accountant-General` | 4 |
| 4165 | O 27 r 11(2): When funds in Court are by an order directed to be transferred or carried over, the party ... | encoded | `o 27 r 11(2) the party having the carriage of the order has lodged a copy with the Accountant-General` | 3 |
| 4166 | O 27 r 11(3): Subject to paragraph (4), the Court may direct that any money in Court, other than money u... | fork (F-MUST) | `o 27 r 11(3) the Court may direct that the money in Court be invested in trustee securities` | 7 |
| 4167 | O 27 r 11(4): The Court may direct that any money in Court under Order 33 may be placed on deposit with ... | encoded | `o 27 r 11(4) the amount the money must exceed`; `o 27 r 11(4) the Court may direct that the money in Court be placed on deposit` | 7 |
| 4168 | O 27 r 11(5): Any application for an order under paragraph (4) must be served on the Sheriff. | encoded | `o 27 r 11(5) the application was served on the Sheriff` | 3 |
| 4169 | O 27 r 12 heading: Accountant‑General to give certificate of funds in Court (O. 27, r. 12) | inert, reason 1 | | |
| 4170 | O 27 r 12: The Accountant‑General, upon a request signed by or on behalf of a person claiming to be i... | encoded | `o 27 r 12 the Accountant-General must issue a certificate of the amount and description of the funds` | 3 |
| 4171 | O 27 r 13 heading: Publication of list of funds in Court (O. 27, r. 13) | inert, reason 1 | | |
| 4172 | O 27 r 13: In the month of January in every year, the Accountant‑General must cause to be published i... | fork (F-O27-2) | `o 27 r 13 the list is published in the Gazette in the month of January`; `o 27 r 13 the number of years`; `o 27 r 13 the account is one the list must include`; `o 27 r 13 the list gives what the Rule requires` | 13 |
| 4173 | O 27 r 14 heading: Unclaimed funds in Court with Accountant‑General (O. 27, r. 14) | inert, reason 1 | | |
| 4174 | O 27 r 14(1): The funds in Court or in the Sheriff’s account appearing from the books and accounts to ha... | fork (F-O27-2) | `o 27 r 14(1) the number of years`; `o 27 r 14(1) the funds must be transferred and paid to the Government for the general purposes of the State` | 5 |
| 4174 | O 27 r 14(2): The funds in Court or in the Sheriff’s account appearing from the books and accounts to ha... | encoded | `o 27 r 14(2) the amount the Government must pay the claimant`; `o 27 r 14(2) the Government must pay the claimant` | 8 |
| 4175 | O 27 r 14(3): Nothing in this Rule authorises the transfer of any funds in Court or in the Sheriff’s acc... | encoded | `o 27 r 14(3) this Rule authorises the transfer of the funds`; `o 27 r 14(3) the transfer of the minor's funds under this Rule is barred` | 7 |
| 4176 | O 27 r 15 heading: Sheriff to keep account (O. 27, r. 15) | inert, reason 1 | | |
| 4177 | O 27 r 15(1): The Sheriff must keep an account of all sums of money paid to or deposited with him or her... | encoded | `o 27 r 15(1) the Sheriff keeps an account of all sums of money paid to, deposited with and paid out by him or her` | 3 |
| 4177 | O 27 r 15(2): The Sheriff must keep an account of all sums of money paid to or deposited with him or her... | encoded | `o 27 r 15(2) where the money is kept`; `o 27 r 15(2) the money paid to or deposited with the Sheriff is kept in the place` | 3 |
| 4178 | O 27 r 15(3): No interest is payable in respect of any money paid to or deposited with the Sheriff. | encoded | `o 27 r 15(3) interest is payable in respect of the money` | 2 |
| 4179 | O 27 r 16 heading: How money paid to Sheriff (O. 27, r. 16) | inert, reason 1 | | |
| 4180 | O 27 r 16: Money paid to or deposited with the Sheriff under these Rules or a judgment or order of a ... | encoded | `o 27 r 16 the Registry officer has acknowledged the money with a receipt` | 3 |
| 4181 | O 27 r 17 heading: Payment under judgment or order (O. 27, r. 17) | inert, reason 1 | | |
| 4182 | O 27 r 17: When any payment is made under a judgment or order, the person making the payment must — (... | encoded | `o 27 r 17 the person making the payment has produced a copy and given notice`; `o 27 r 17 the person making the payment must produce a copy and give notice` | 4 |
| 4182 to 4183 | O 27 r 17(a): produce a copy of the judgment or order; and | encoded | `o 27 r 17 the person making the payment has produced a copy and given notice`; `o 27 r 17 the person making the payment must produce a copy and give notice` | 4 |
| 4184 to 4185 | O 27 r 17(b): give notice to the person entitled to the money. | encoded | `o 27 r 17 the person making the payment has produced a copy and given notice`; `o 27 r 17 the person making the payment must produce a copy and give notice` | 4 |
| 4186 | O 27 r 18 heading: Proof before payment out (O. 27, r. 18) | inert, reason 1 | | |
| 4187 | O 27 r 18: Before any money is paid out to any person, the Sheriff must require proof to his or her s... | fork (F-ASSUMED) | `o 27 r 18 the Sheriff has required proof that the person applying is entitled or authorised to receive the money` | 3 |
| 4188 | O 27 r 19 heading: Where money due to Government under any law (O. 27, r. 19) | inert, reason 1 | | |
| 4189 | O 27 r 19: Before any money is paid out under any order directing the payment out of any money paid o... | fork (F-ASSUMED) | `o 27 r 19 the Sheriff has satisfied himself or herself that the money due to the Government has been paid or deducted` | 3 |
| 4190 | O 27 r 20 heading: Method of payments by Sheriff (O. 27, r. 20) | inert, reason 1 | | |
| 4191 | O 27 r 20: All payments by the Sheriff must be made by a method approved by the Registrar. | encoded | `o 27 r 20 the payment by the Sheriff is made by a method approved by the Registrar`; `o 27 r 20 the office that approves the method of payment by the Sheriff` | 4 |
| 4192 | O 27 r 21 heading: Instalments ledger (O. 27, r. 21) | inert, reason 1 | | |
| 4193 | O 27 r 21: Whenever a judgment or order has been made in the State Courts for payment of money by ins... | encoded | `o 27 r 21 the Registrar has caused the instalments ledger to be opened` | 4 |

## Fork register (roc6)

### The rulings that bind this row (E1 and N2 word for word from the brief; the two rulings of 2026-11-05 in my own words)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Where I applied them.**
E1: every section's answer is encoded on its own (option C); where the same legal effect is reached by several sections (the 35-page limit in O 24A r 2(3), r 2(11) and r 3(6); the three tribunal rules O 23 r 12, r 13 and r 14; the 14-day and 3-day periods) there is one function per section and no function that gathers them by name.
I wrote two functions by hand that gather routes to one effect, as option B allows: `o 25 r 2 the value of the claim` (the heads of paragraph (2) and the aggregate of paragraph (3), fork F-O25-1) and `o 27 r 6(1)(a) the money is paid into Court under Order 9, Rule 17, Order 14 or Order 33, or as security for costs` (the four routes the exception names).
N2: a flat negative ("shall not", "must not", "is not payable", "no ... is payable", "nothing in this Rule") answers `JUST FALSE`, and where the text names the bearer the prohibition is a `SHANT` rule (`o 23 r 7(3) the committal applicant shall not rely on a ground not set out in the affidavit`, `o 24 r 2(2) the applicant shall not apply for a prerogative order before exhausting every right of appeal or other remedy`); the Hohfeld kinds are in the table below and in no person-facing answer.
Periods, "where" and scope limits: (a) applied at 38 sites (an act after the last day of a period the text fixes answers `JUST FALSE`); (b) applied at 59 sites; (c) a scope limit with no "only" answers `NOTHING`: for example the District Court limit of O 25 r 8(1), the relatives of O 27 r 10(3), the orders of O 24 r 2(1), and the accounts of O 27 r 13 younger than the years stated.
Where I could not tell which of (a), (b) and (c) a clause was, or which words a period attaches to, or which of two readings a clause bears, there is a fork entry below: F-ASSUMED, F-MUST, F-O23-1, F-O23-2, F-O23-3, F-O24-1, F-O24-2, F-O24A-1, F-O24A-2, F-O24A-3, F-O25-1, F-O25-2, F-O25-3, F-O26-1, F-O27-1, F-O27-2, F-O27-3, F-O27-4, F-TIMED, F-UNSURE.
"Where", "if", "when", "upon" and the other opening words were applied at every site in the six layer-1 files, not only at the examples: each `NOTHING-kind (limited by its own wording)` branch was read for the word that opens it, and each `if` or `where` was classed as (a), (b) or scope (c); the sites where a word outside the rulings' own list (after, before, during, "on the application of", "in the case of", "on proof of") was read as "where" are listed in F-ASSUMED, and the sites that read as (b) but were kept at `NOTHING` are listed in F-UNSURE.

### Forks taken

**F-O23-1 (O 23 r 4(1)).**
Text: "the committal applicant must apply for the committal order within 14 days by summons ... and serve the following on the committal respondent by personal service".
Readings: (1) The 14 days attach to the application only, and the service has no time of its own except rule 4(2)'s 21 days before the hearing. (2) The 14 days run for the service too.
Taken: Reading (1). The phrase "within 14 days by summons in the originating application ... or by summons in the action" is one run of modifiers of "apply"; "and serve" opens a new verb with no time of its own. Under (2) a service on day 15 would answer `JUST FALSE` by ruling (a); under (1) the function `o 23 r 4(1) the four documents have been served on the committal respondent by personal service` answers `JUST TRUE` when all four were personally served and `NOTHING` otherwise.
The opening words "After permission is granted under Rule 3" are read as "where" (F-ASSUMED), so the period function answers `JUST FALSE` when no permission has been granted.
The personal-service sites of paragraph (1) are in F-MUST.
Carried by: `o 23 r 4(1) the period for applying for the committal order`, `o 23 r 4(1) the application for the committal order is made within 14 days after permission`, `o 23 r 4(1) the four documents have been served on the committal respondent by personal service`.

**F-O23-2 (O 23 r 7(1)).**
Text: "The Court must hear in open court an application for a committal order or an application under section 10(4) to transfer a case to the General Division, but may hear the application in private in the following cases", cases (a) to (e), each of which opens with "where" (L3601-3610).
Readings: (1) The five cases are the only ones in which the Court may hear in private: outside them, hearing in private is `JUST FALSE` and hearing in open court is `JUST TRUE`.
(2) The list does not say "only", so outside the five cases the text leaves the question open: `NOTHING` for both.
Taken: Reading (1).
Each case opens with "where", and ruling (b) of 2026-11-05 answers `JUST FALSE` when a "where" is not met.
The two functions agree on every row: outside the cases, private is `JUST FALSE` and open court is `JUST TRUE`; inside them, private is `JUST TRUE` and open court is `JUST FALSE`; for any other application both are `NOTHING`.
The open-court function takes the one fact the exception turns on, whether one of cases (a) to (e) applies.
Carried by: `o 23 r 7(1) the Court may hear the application in private`, `o 23 r 7(1) the Court must hear the application in open court`.

**F-O23-3 (O 23 r 4(2)).**
Text: "There must be at least 21 days between the service under paragraph (1) and the hearing date" (L3584).
Readings: (1) The days between are the difference of the two dates: service 21 days before the hearing date is enough.
(2) The days between are the intervening days, as with clear days in Order 3 Rule 3: service 21 days before the hearing date leaves only 20 days between and is not enough.
Taken: The function does not count.
It takes the last day for the service from Order 3 Rule 3 (`o 3 r 3 the last day for doing the act`), answers `JUST TRUE` for a service on or before it and `JUST FALSE` after it (ruling (a)).
The constant `o 23 r 4(2) the minimum gap between service and the hearing` says 21 `Days`, before the anchor, which is reading (1).
A caller who takes reading (2) passes the last day counted in clear days.
Carried by: `o 23 r 4(2) the minimum gap between service and the hearing`, `o 23 r 4(2) there are at least 21 days between the service and the hearing date`.
Reviewer: The independent reviewer took reading (2) for its scenario 20 and listed it as ambiguity A1.

**F-O24-1 (O 24 r 4(2), r 4(6), r 5(5), r 6(3)).**
Text: "as soon as it is practicable ... and in any case no later than 2 working days after it is filed".
Readings: (1) Two limbs, the second a backstop: late service is `JUST FALSE`; service on or before the last day is `JUST TRUE` when it was as soon as practicable and `NOTHING` when it was not, because "practicable" is a judgment the text leaves to the asker. (2) The 2 working days are enough: service within them is `JUST TRUE` whether or not it was as soon as practicable.
Taken: Reading (1). "and in any case" joins the limbs; reading (2) would make the first limb idle.
The "as soon as it is practicable" limb is a target and not a bar, so it stays `NOTHING` when the service was inside the 2 working days but not as soon as practicable.
The other reading for that limb alone is `JUST FALSE` (the limb read as a bar); the 2 working days are a bar and answer `JUST FALSE` after the last day (ruling (a)).
Carried by: `o 24 r 4(2) the document is served as soon as practicable and no later than 2 working days after it is filed`, shared by the four rules.

**F-O24-2 (O 24 r 2(1)).**
Text: "The following are prerogative orders", then four orders, under the heading "Definition and general matters of this Order" (L3747).
Readings: (1) A bare list: another kind of order is not covered by the paragraph, `NOTHING`.
(2) A definition that the list closes: another kind of order is not a prerogative order, `JUST FALSE`.
Taken: Reading (1).
The paragraph says "The following are" and does not say "means" or "only", and it does not hand a defined term to the list the way "has effect for determining what is" does, so the ruling on delegated definitions of 2026-11-05 does not reach it.
Carried by: `o 24 r 2(1) the order is a prerogative order`.
Reviewer: The independent reviewer asserted `NOTHING` (its scenario 98), noting that because of the heading a reader could argue `JUST FALSE`; open question.

**F-O24A-1 (O 24A r 2(1), r 3(2)).**
Text: "must be fixed for hearing within 21 days after the date on which the application is filed" (and "is made").
Readings: (1) The hearing DATE falls within 21 days. (2) The act of FIXING the date is done within 21 days.
Taken: Reading (1). The sentence is passive and names no actor, so reading (2) would have no bearer and no date input; reading (1) needs only the hearing date and the last day.
Carried by: `o 24A r 2(1) the application for PACC permission is fixed for hearing within 21 days after it is filed`, `o 24A r 3(2) the PACC application is fixed for hearing within 21 days after it is made`.

**F-O24A-2 (O 24A r 3(6)).**
Text: "The written submissions mentioned in paragraphs (3)(b) and (5) are subject to a page limit of 35 pages, unless the Court of Appeal otherwise allows" (L3919); rules 2(3) and 2(11) say "35 pages (including any cover page and contents page)" (L3838, L3908).
Readings: (1) The cover page and the contents page count in rule 3(6) as they do in rules 2(3) and 2(11).
(2) Rule 3(6) leaves them out of the count, or is silent on whether they count.
Taken: Neither is decided.
`o 24A r 3(6) the written submissions are within the page limit` takes `the number of pages` as the caller counts them and compares it with 35.
Rules 2(3) and 2(11) name the count in their input ("the number of pages, including any cover page and contents page").
Carried by: `o 24A r 3(6) the page limit for written submissions on the PACC application`, `o 24A r 3(6) the written submissions are within the page limit`.
Reviewer: The independent reviewer asked this as scenario 159 and listed it as ambiguity A7, expecting `NOTHING` for 35 body pages plus a cover page.

**F-O24A-3 (O 24A r 2(8), r 2(10), r 3(1), r 3(3)(b), r 3(5)).**
Text: Each gives a period of 3 days; Order 3 Rule 3(6) says "If the period in question is 6 days or less, any day that is a non-court day is to be excluded in the calculation of time" (raw L328).
Readings: (1) The 3-day periods exclude non-court days.
(2) They count every day.
Taken: Reading (1), but this range does not count.
Each of these functions takes the last day from Order 3 Rule 3 (`o 3 r 3 the last day for doing the act`), so whether non-court days were excluded is that rule's work, in another part.
The period constants say `Days`.
Carried by: `o 24A r 2(8) three days`, `o 24A r 3(1) three days`, and the functions `o 24A r 2(8)`, `o 24A r 2(10)(a)`, `o 24A r 2(10)(b)(i)`, `o 24A r 2(10)(b)(ii)`, `o 24A r 3(1)`, `o 24A r 3(3)(b)`, `o 24A r 3(5)` that take the last day.
Reviewer: The independent reviewer listed this as ambiguity A9 and relied on reading (1) in its scenarios 146-158.

**F-O25-1 (O 25 r 2(2)(a)-(e), r 2(3)).**
Text: The value of the claim for court fees in the Supreme Court: five heads in paragraph (2), the aggregate of (a) and (b) in paragraph (3), and "deemed to have a value of up to $1 million" in (2)(d).
Readings: (1) Add every head that applies. (2) Take the largest head. (3) Answer only for one head or for (a) plus (b), and refuse the rest. And for (d), a band "up to $1 million" is not a number: (i) answer 1000000, (ii) answer a refusal.
Taken: (1), and (d) as 1000000. Seam S-V1 asks for a NUMBER, and a NUMBER cannot answer `NOTHING`, so the "refuse" readings are not available in the type; the text gives an aggregate for two heads only, and I extend it to the others because no other combination rule exists. The 1000000 puts the claim in the Fourth Schedule's "up to $1 million" column and is **assumed, not ruled** (PLAN.md seam S-V1 says the same).
Carried by: `o 25 r 2 the value of the claim`, `o 25 r 2(2) paragraph (2) applies to the court fees`.

**F-O25-2 (O 25 r 8(1), r 8(3)).**
Text: "A fee of $250 is payable by each party in a case in a District Court for all Court ADR services that are provided in the case" (paragraph (1)); "No Court ADR fee is payable in any of the following actions" (paragraph (3)), four actions, no "only".
Readings: (1) Paragraph (3) carves exemptions out of paragraph (1): any action that is none of the four is not exempt, so the fee is payable.
(2) Paragraph (3) is a list with no "only", so for any other action the paragraph says nothing: `NOTHING`.
Taken: Reading (1), the other way round from the first version of this file.
Paragraph (1) states the general rule of payment and paragraph (3) lists exemptions from it; ruling (c) of 2026-11-05 is about a scope limit that restricts how far a rule reaches, and paragraph (3) does not restrict paragraph (1), it carves out of it.
So `o 25 r 8(3) no Court ADR fee is payable in the action` answers `JUST FALSE` for an action that is none of the four, and `o 25 r 8(1) the Court ADR fee is payable by the party` answers `JUST TRUE` for an ordinary contract claim in a District Court.
The first version took reading (2), and an independent test pass found that this left an ordinary contract claim in a District Court at `NOTHING` instead of "the fee of $250 is payable".
The total for the parties to a case is `o 25 r 8(1) the total Court ADR fee payable by the parties in a District Court case`: the number of parties times 250, so 750 for three parties, with no exemption applied (the yes/no question of exemption is `o 25 r 8(1) the Court ADR fee is payable by the party`).
The scope limit of "in a case in a District Court" is unchanged: any other court answers `NOTHING` (ruling (c)).
Carried by: `o 25 r 8(3) no Court ADR fee is payable in the action`, `o 25 r 8(1) the Court ADR fee is payable by the party`, `o 25 r 8(1) the total Court ADR fee payable by the parties in a District Court case`.

**F-O25-3 (O 25 r 3(4)).**
Text: "the Court must refund the whole of the hearing fees paid if the Court is notified in writing not later than 14 days before the first date fixed for hearing that the cause or matter has been settled or discontinued, or transferred to another Court" (L3972).
Readings: (1) A notice given on the day that is 14 days before the first date fixed for hearing is in time.
(2) The 14 days are clear days: the notice must come a day earlier.
Taken: The function does not count.
It takes the last day from Order 3 Rule 3, answers `JUST TRUE` for a notice on or before it and `JUST FALSE` after it; the constant `o 25 r 3(4) fourteen days before the first date fixed for hearing` says 14 `Days`, before the anchor, which is reading (1).
A caller who takes reading (2) passes the last day counted in clear days.
A late notice answers `JUST FALSE` only to this paragraph's duty to refund the whole: paragraph (3)(a) still allows a request for a refund of hearing fees within one month after settlement, and that is a different function.
Carried by: `o 25 r 3(4) fourteen days before the first date fixed for hearing`, `o 25 r 3(4) the Court must refund the whole of the hearing fees paid`.
Reviewer: The independent reviewer took reading (1) for its scenario 186 and listed it as ambiguity A2.

**F-O26-1 (O 26 r 2).**
Text: "The Registrar may issue practice directions from time to time with the approval of the Chief Justice or the Presiding Judge of the State Courts, as the case may be" (L4056).
Readings: (1) "With the approval of" is a condition of the power: without the approval the directions are not issued under the Rule, `JUST FALSE`.
(2) The words are not among those the rulings name ("if", "where", "when", "upon", "whenever"), so without the approval the text is silent: `NOTHING`.
Taken: Reading (2).
Carried by: `o 26 r 2 the directions are issued under Order 26, Rule 2`.
Reviewer: The independent reviewer asserted `NOTHING` (its scenario 228) and noted that a natural reading gives `JUST FALSE`; open question.

**F-O27-1 (O 27 r 7(3)).**
Text: "ceases from the last day of the calendar month next preceding the day of the withdrawal of the money from deposit".
Readings: (1) Interest is no longer earned for that last day, which is the day FROM which it ceases. (2) Interest runs through that last day and ceases the day after.
Taken: Reading (1): the function `o 27 r 7(3) the day from which interest ceases` answers that last day of the preceding month. "Begins on the first day of the calendar month next succeeding" has no such doubt and `o 27 r 7(3) the first day on which interest begins` answers that first day.
Carried by: `o 27 r 7(3) the day from which interest ceases`.

**F-O27-2 (O 27 r 13, r 14(1)).**
Text: Rule 13: "a list of accounts not dealt with for a period of 4 years or more". Rule 14(1): funds in custody "for a period of 6 years and upwards, without any claim having been made and allowed thereto during that period, must be transferred and paid to the Government".
Readings: (1) The threshold is a scope limit with no "only": below it the answer is `NOTHING` (ruling (c)). (2) It is a period the text fixes in its own words: below it the answer is `JUST FALSE` (ruling (a)).
Taken: Rule 13 as (1): it describes which accounts a list covers and does not say that a younger account must be left off. Rule 14(1) as (2): it says when a duty to transfer arises. Reading rule 14(1) as (1) would answer `NOTHING` below 6 years; reading rule 13 as (2) would answer `JUST FALSE` below 4 years.
Carried by: `o 27 r 13 the account is one the list must include`, `o 27 r 14(1) the funds must be transferred and paid to the Government for the general purposes of the State`.
Reviewer: The independent reviewer expected `JUST FALSE` for an account not dealt with for 3 years (its scenario 295).
Reviewer expected JUST FALSE; open question.

**F-O27-3 (O 27 r 6(1)(b), r 6(2)).**
Text: "... except — (a) when money is paid into Court under Order 9, Rule 17, Order 14 or Order 33, or as security for costs; or (b) when the amount is less than $30,000" (L4134-4137); "Such money is deemed not to be placed on deposit when the amount is reduced below $30,000" (L4138).
Readings: (1) "The amount" is the sum lodged on this occasion.
(2) "The amount" is the balance to the credit of the account, which rule 6(2) can "reduce".
Taken: Neither is decided.
`o 27 r 6(1) the money lodged in Court is deemed to be placed on deposit and is credited with interest` takes one number, `amount`, and the caller passes the figure it means; rule 6(2) "reduced below" is the only hint in the text, and it points to the balance.
The two exceptions are independent: below $30,000 the function answers `JUST FALSE` whatever exception (a) would answer, even when (a) is `NOTHING`; at exactly $30,000 the money is on deposit.
Carried by: `o 27 r 6(1) the money lodged in Court is deemed to be placed on deposit and is credited with interest`, `o 27 r 6(1)(a) the money is paid into Court under Order 9, Rule 17, Order 14 or Order 33, or as security for costs`.
Reviewer: The independent reviewer read "the amount" as the amount lodged to the credit of the account and listed it as ambiguity A8.

**F-O27-4 (O 27 r 10(3)).**
Text: "... such funds may be paid, transferred, or delivered to the person who, being widower, widow, child, father, mother, brother or sister of the deceased, would be entitled to take administration to his or her estate, upon a declaration by such person in accordance with Form 46" (L4161).
Readings: (1) The relatives are named in a relative clause that says who the person is, and the list does not say "only": a cousin is not covered, `NOTHING` (ruling (c)).
(2) The list is closed: a cousin is outside the paragraph, `JUST FALSE`.
Taken: Reading (1).
The same answer, `NOTHING`, is given when the person would not be entitled to take administration.
The other conditions answer as they read: administration already taken out, death not intestate, assets over $10,000, and no declaration in Form 46 are each `JUST FALSE` ("if", "upon").
Carried by: `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration`.
Reviewer: The independent reviewer asserted `NOTHING` for a cousin (its scenario 285) and noted that a reader could argue `JUST FALSE`; open question.

**F-MUST (sites where the text says "must" and I answer NOTHING).**
Text: in each row below the text says what a person must do, or what a document must contain, and says nothing of what follows from not doing it.
Readings: (1) The text is silent about the case where it is not done: `NOTHING`. (2) A duty that is not done is a no: `JUST FALSE`.
Taken: reading (1), at all 14 sites, and I changed none of them. "Must" is not among the words the rulings of 2026-11-05 name.
The answers were read from the encoding itself: I ran the 14 cases of the table, and the r 13 case of F-O27-2, in a scratch file asserting `NOTHING`, and every assertion was satisfied.
Reviewer expected JUST FALSE at every site; open question.

| reviewer scenario | provision | the case | answer here | reviewer expected |
| --- | --- | --- | --- | --- |
| 10 | O 23 r 3(2) (L3568) | the application for permission is made some other way than by originating application without notice or summons without notice (the reviewer's case: made with notice) | `NOTHING` | `JUST FALSE` |
| 12 | O 23 r 3(3)(b) (L3572) | the supporting affidavit omits the committal respondent's address | `NOTHING` | `JUST FALSE` |
| 16 | O 23 r 4(1) (L3576) | the documents are served by registered post only, not by personal service | `NOTHING` | `JUST FALSE` |
| 17 | O 23 r 4(1)(c) (L3581) | the other documents are personally served but the order granting permission is not | `NOTHING` | `JUST FALSE` |
| 38 | O 23 r 7(2)(c) (L3616) | the application is heard in private and the respondent is committed for a fixed period, and the Court does not state the length of the period in open court | `NOTHING` | `JUST FALSE` |
| 44 | O 23 r 7(4)(b) (L3619-3621) | the committal respondent gives oral evidence without the Court's permission | `NOTHING` | `JUST FALSE` |
| 75 | O 23 r 15(3)(a) (L3709) | the supporting affidavit has no copy of the proposed direction annexed | `NOTHING` | `JUST FALSE` |
| 119 | O 24 r 5(3)(b)(i) (L3791) | the affidavit does not show the applicant's legal standing | `NOTHING` | `JUST FALSE` |
| 142 | O 24A r 2(4)(a)(ix) (L3865) | the counsel's affidavit leaves out that counsel genuinely believes the PACC application to be of merit | `NOTHING` | `JUST FALSE` |
| 143 | O 24A r 2(4)(b)(vii) (L3892) | the unrepresented applicant's affidavit leaves out whether the applicant is assisted by any person or organisation | `NOTHING` | `JUST FALSE` |
| 145 | O 24A r 2(5) (L3893) | the affidavit leaves out information about an event before 28 June 2024 | `NOTHING` | `JUST FALSE` |
| 183 | O 25 r 3(3) (L3964) | the request for a refund is made orally, not in writing | `NOTHING` | `JUST FALSE` |
| 234 | O 26 r 3(7) (L4066) | the document filed is handwritten, not typewritten or printed | `NOTHING` | `JUST FALSE` |
| 289 | O 27 r 11(3) (L4166) | the money is paid into Court as security for costs, which the paragraph excepts ("other than") | `NOTHING` | `JUST FALSE` |

**F-ASSUMED (words outside the rulings' own lists, read as "where").**
Text: the rulings of 2026-11-05 name "if", "where", "when", "upon" and "whenever" for a condition that is not met, and "within", "not later than", "begins from ... until", "on the last day of" and "for a period not exceeding" for a period the text fixes.
Readings: (1) Only those words count, and any other opening word leaves `NOTHING`. (2) A word that does the same work counts too.
Taken: reading (2), at the sites below, **assumed, not ruled**.
"Once" and "in the event of" do not occur in lines 3556 to 4193 (a regular expression over the raw file found no line), so the assumption the brief makes for them was not needed.
A function that returns a number, a date or a record cannot carry `JUST FALSE`, so where its opening condition fails and the text says no, I added a yes/no twin and left the number as it was: `o 27 r 14(2) the Government must pay the claimant` beside `o 27 r 14(2) the amount the Government must pay the claimant`, and `o 23 r 16(10)(b) the date the Court specified is a later date than the date of service` beside `o 23 r 16(10)(b) the date from which the order varying the direction takes effect as to a person other than the applicant` ("such later date"), which keeps its `NOTHING` for a date that is not later; the total `o 25 r 8(1) the total Court ADR fee payable by the parties in a District Court case` is a number whose yes/no question is `o 25 r 8(1) the Court ADR fee is payable by the party`; I looked at the other number- and date-returning functions of the six files and none opens with a condition whose failure the text answers no to.

| function | the words | read as | answer |
| --- | --- | --- | --- |
| `o 23 r 4(1) the application for the committal order is made within 14 days after permission` | "After permission is granted under Rule 3" | "where" | `JUST FALSE` when no permission has been granted |
| `o 25 r 2(5) the Registrar may require the parties to pay the difference in the court fees` and `o 25 r 2(5) the Registrar may refund to the parties the excess court fees paid` | "after determining the value of the claim" | "where" | `JUST FALSE` when the Registrar has not determined the value |
| `o 25 r 7(1) the Registrar may issue a certificate of exemption` | "on the application of that party" | "upon" | `JUST FALSE` when the party has not applied |
| `o 26 r 6 a Judge is available during the Court vacations to hear the matter` | "during the Court vacations" | a period the text names, ruling (a) | `JUST FALSE` outside the vacations |
| `o 27 r 9(2) it is sufficient for the order to state the business name of the firm` | "In the case of payment to a firm" | "where" | `JUST FALSE` when the payment is not to a firm |
| `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | "on proof of the death of that person" | "upon" | `JUST FALSE` without proof of the death |
| `o 27 r 18 the Sheriff has required proof that the person applying is entitled or authorised to receive the money` and `o 27 r 19 the Sheriff has satisfied himself or herself that the money due to the Government has been paid or deducted` | "Before any money is paid out" | "when" | `JUST FALSE` when no money is to be paid out |

**F-UNSURE (opening phrases kept at NOTHING).**
Text: the phrases below open a power or a duty in a way that looks like a condition and is not one of the opening words the rulings name.
Readings: (1) A scope or judgment phrase: outside it the text says nothing, `NOTHING`. (2) A condition like "where": outside it `JUST FALSE`.
Taken: reading (1) at every site below, and I could not tell.

| provision | the words | why I kept NOTHING |
| --- | --- | --- |
| O 23 r 6(2) (L3588) | "In hearing such an application, the General Division may order ... stayed" | a scope phrase for one kind of order, not a "where" |
| O 23 r 7(5), r 7(6) (L3622, L3644) | "in making any order allowing ... a live video or live television link, the Court is to have regard to the following matters" | a scope phrase for one kind of order; the list of matters has no "only" |
| O 23 r 8(3) (L3666) | "may apply for the suspension to be lifted on the ground that any of the terms of the suspension has been breached" | a ground, not one of the opening words the rulings name |
| O 24A r 2(7) (L3895) | "Paragraphs (8) and (9) apply to an applicant in any of the following circumstances" | a list of circumstances with no "only" |
| O 24A r 2(13), r 3(7) (L3910, L3920) | "may allow the page limit ... to be exceeded in special circumstances" | a judgment phrase, not a condition the text states |
| O 26 r 3(5) (L4064) | "may redact any document in the interests of justice" | a judgment phrase, not a condition the text states |

**F-TIMED (time words that I did not turn into a bar).**
Text: the functions below carry a time word that is not a period the text fixes in its own words, and each stays at `NOTHING` where the time is not met.
Readings: (1) A target, a sequence, a bound on a prohibition, or a list of cases with no "only": outside it the text is silent, `NOTHING`.
(2) A period or deadline the text fixes: outside it `JUST FALSE` (ruling (a) of 2026-11-05).
Taken: reading (1) at every site below.
This table is the "stays NOTHING" part of the audit of period functions (see Seams); the functions that answer `JUST TRUE` inside and `JUST FALSE` outside a stated period are not repeated here.

| function | the words | why it stays NOTHING | other reading |
| --- | --- | --- | --- |
| `o 24 r 4(10) the solicitor appearing for the defendant has informed the defendant or the appropriate person or entity` and `o 24 r 6(6) the solicitor appearing for the defendant has informed the defendant or the appropriate person or entity` | "as soon as is practicable" | a target with no period; the input says whether it was done as soon as practicable, and false covers late and never | `JUST FALSE` |
| `o 27 r 3 the person has given notice of the lodgment` | "forthwith" | no period is stated; the input says whether notice was given forthwith, and false covers late and never | `JUST FALSE` |
| `o 23 r 11(3) the committal applicant has deposited the money requested by the Sheriff` | "before the Sheriff complies with the committal order and from time to time" | a deadline tied to an event, but the inputs are yes/no and cannot tell late from never; the paragraph names no consequence | `JUST FALSE` for a late deposit |
| `o 23 r 3(1) the committal applicant has first applied to the Court for permission` | "must first apply" | a sequence with no period; the input cannot tell late from never; the Rule names no consequence | `JUST FALSE` for an application made after the committal application |
| `o 27 r 7(2) interest on money on deposit is computed by the period`, the choice `a period longer than a calendar month` | "accrues by calendar months, and must not be computed by any less period" | the bar is on a shorter period (`JUST FALSE`); the paragraph does not speak of a longer one | `JUST FALSE`, if "accrues by calendar months" is read as fixing the period |
| `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | "whether (a) on or after the date of such order; or (b) in the case of payment directed to be made to a creditor as such, before the date of such order" | two cases with no "only", a scope list: a death before the order, for a payment that is not to a creditor, is in neither case | `JUST FALSE`, if the two cases are read as the whole of what the paragraph allows |
| `o 27 r 13 the account is one the list must include` | "a period of 4 years or more" | a scope limit with no "only" (fork F-O27-2) | `JUST FALSE` below 4 years |
| `o 27 r 14(3) this Rule authorises the transfer of the funds` | "until such minor comes of age or dies" | an "until" bar, ruled on 2026-11-05 (d): the bar is asked as its own question (`o 27 r 14(3) the transfer of the minor's funds under this Rule is barred`), and "does this Rule authorise the transfer" is never answered yes on the bar's strength | none: ruled |

### Smaller readings that are not forks

- O 27 r 6(1)(b) says "less than $30,000", r 6(2) "reduced below $30,000" and r 7(7) "amounts to or exceeds $30,000": at exactly $30,000 the money is on deposit. Tested at 29999 and 30000.
- O 27 r 13 says "4 years or more" and r 14(1) "6 years and upwards": both inclusive, compared with AT LEAST. The core has no years unit, so each is a NUMBER constant (NEEDS-CORE.md).
- O 25 r 8(1) "payable by each party in a case in a District Court" is a scope limit: any other court answers `NOTHING` (ruling (c)); within a District Court, an action outside the four of paragraph (3) answers `JUST TRUE` (F-O25-2).
- O 27 r 14(2) says what the Government "must pay": the principal only, which the function `o 27 r 14(2) the amount the Government must pay the claimant` takes as two inputs and returns the smaller of the two; the paragraph gives no interest and the function adds none.
- O 24A r 3(4) "within the day on which that application is made": taken as the same calendar day; tested one day later as `JUST FALSE`.
- Where a paragraph says "must" and the text names no time and no consequence (O 27 r 3 "forthwith give notice", O 27 r 17, O 23 r 4(1) service), the function answers `JUST TRUE` when it was done and `NOTHING` when it was not: the text says what to do and not what follows.

## Jural relations (roc6)

Hohfeld kinds are recorded here and are not typed into any person-facing answer (ruling N2).
Where the text does not name who holds the correlative right, the holder cell says "not named in the text" and I have not supplied one.
A reading made from the text's own words (for example from "lapses") and not from a word naming the relation is marked "read from".
The L4 column gives the label stem: every top-level name for that provision starts with it, so `grep` for the stem finds the functions; a regulative rule is named where there is one.
A provision that creates no relation is listed once as `none`.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| O 23 r 1 | none | none | none (definitions) | `o 23 r 1` |
| O 23 r 2 | the Court | the person in contempt | power / liability | `o 23 r 2` |
| O 23 r 3(1)-(3) | not named in the text (the Court's process) | the committal applicant: must first apply for permission, in the way and with the affidavit the rule describes | claim / duty | `o 23 r 3(1), (2), (3)` |
| O 23 r 4(1) | the committal respondent (as to service of the four documents); the Court (as to the application) | the committal applicant: must apply within 14 days and serve by personal service | claim / duty | `o 23 r 4(1)` (regulative rule `o 23 r 4(1) the committal applicant must apply for the committal order within 14 days`) |
| O 23 r 4(2) | the committal respondent | the committal applicant: at least 21 days between service and the hearing | claim / duty | `o 23 r 4(2)` |
| O 23 r 5(1) | the General Division | a person charged with having done anything in relation to a court, tribunal or person | power / liability | `o 23 r 5(1)` |
| O 23 r 5(2) | the General Division, the Appellate Division and the Court of Appeal (the saved power to commit on their own accord) | a person guilty of contempt of court | power / liability (saved) | `o 23 r 5(2)` |
| O 23 r 6(1)-(2) | the General Division (power to stay) | the parties to the case sought to be transferred | power / liability | `o 23 r 6(1), (2)` |
| O 23 r 6(3) | the General Division (power to order the transfer and make other orders); the Registrar of the Supreme Court (to be sent the file); every party (to be given notice) | the Registrar of the State Courts (must send); the Registrar of the Supreme Court (must give notice) | power / liability; claim / duty | `o 23 r 6(3)(a), (b), (c)` |
| O 23 r 7(1)-(2) | the public (open court) and the Court (private hearing in the listed cases) | the Court (must hear in open court; must state in open court what paragraph (2) lists) | claim / duty; liberty / no-right | `o 23 r 7(1), (2)` |
| O 23 r 7(3) | the committal respondent (not named; affected) | the committal applicant: shall not rely on a ground not set out in the affidavit | claim / duty (prohibition derived under N2) | `o 23 r 7(3)` (regulative rule `o 23 r 7(3) the committal applicant shall not rely on a ground not set out in the affidavit`) |
| O 23 r 7(4) | (a) not named in the text; (b) the committal respondent (may give oral evidence with the Court's permission) | (a) the committal respondent: must rely on the matters stated in the affidavit, if any; (b) the Court (gives or refuses permission) | (a) duty (no claimant named); (b) liberty / no-right, conditional on permission | `o 23 r 7(4)(a), (b)` |
| O 23 r 7(5)-(6) | not named in the text | the Court: to have regard to the listed matters before allowing a live link | duty (no claimant named) | `o 23 r 7(5), (6)` |
| O 23 r 8(1) | the Court | the committal respondent and the committal applicant | power / liability | `o 23 r 8(1)` |
| O 23 r 8(2) | the committal respondent | the committal applicant: must serve a notice of the terms of the suspension | claim / duty | `o 23 r 8(2)` (regulative rule `o 23 r 8(2) the committal applicant must serve a notice of the terms of the suspension`) |
| O 23 r 8(3)-(4) | the committal applicant (may apply for the suspension to be lifted if a term is breached) | the committal respondent (has no claim that the committal applicant refrain from applying); the committal applicant must make the application by summons with an affidavit and serve it on the respondent | liberty / no-right; claim / duty | `o 23 r 8(3), (4)` |
| O 23 r 9(1) | the Court (may discharge); the committal respondent (may apply) | the committal applicant | power / liability; liberty / no-right | `o 23 r 9(1)` |
| O 23 r 9(2) | the Court; the Sheriff (may take possession of the thing) | the committal respondent | power / liability | `o 23 r 9(2)` |
| O 23 r 10 | none | none | none (saving; applies Rules 1 to 9 to a fine or security order) | `o 23 r 10` |
| O 23 r 11(1) | not named in the text | whoever draws the committal order: it must be in Form 42 | duty (form) | `o 23 r 11(1)` |
| O 23 r 11(2)-(3) | the Sheriff's office; the Sheriff | the committal applicant: must serve a copy and an undertaking on the Sheriff's office, and deposit the money the Sheriff requests | claim / duty | `o 23 r 11(2), (3)` (regulative rule `o 23 r 11(3) the committal applicant must deposit the money the Sheriff requested`) |
| O 23 r 12-14 | none | none | none (applies Rules 1 to 11 to a tribunal; reads "Court" and "Judge" for a tribunal; says which fees apply; defines "tribunal") | `o 23 r 12(1)-(5), o 23 r 13(1)-(5), o 23 r 14(1)-(3)` |
| O 23 r 15(1)-(3) | not named in the text | the Attorney-General: must apply by originating application without notice with a supporting affidavit that states what paragraph (3) lists; may authorise a person to make it | duty; liberty / no-right (to authorise) | `o 23 r 15(1), (3)` |
| O 23 r 15(4) | the person to whom the direction would apply (the permission lapses if not served in 14 days) | the Attorney-General (loses the permission) | immunity / disability, read from "lapses" (a reading, not the text's word) | `o 23 r 15(4)` |
| O 23 r 15(5) | not named in the text | a person authorised by the Attorney-General: must file an affidavit of service | duty | `o 23 r 15(5)` |
| O 23 r 16(1)-(4) | a person to whom the direction applies (may apply within 14 days) | the Court and the Attorney-General (liable to the application) | liberty / no-right; power / liability | `o 23 r 16(2), (3), (4)` |
| O 23 r 16(5)-(8) | the Attorney-General, the persons to whom the direction applies and others the Court orders (to be served) | the applicant: must serve the summons and affidavit, state authorship, serve the order within 14 days and file an affidavit of service | claim / duty | `o 23 r 16(5), (6), (7), (8)` (regulative rule `o 23 r 16(7) the applicant must serve the order within 14 days after the date of the order`) |
| O 23 r 16(9)-(10) | none | none | none (says when an order takes effect) | `o 23 r 16(9), (10)(a), (10)(b)` |
| O 23 r 17(1)-(2) | the Court | the committal respondent; the Sheriff or a police officer (to carry out the order) | power / liability | `o 23 r 17(1), (2)` |
| O 23 r 17(3) | the Sheriff or a police officer (the Registrar's letter is sufficient authority) | the committal respondent (liable to arrest) | liberty / no-right | `o 23 r 17(3)` |
| O 23 r 18(1) | the Sheriff | the applicant (directed to engage an officer or agency) | power / liability | `o 23 r 18(1)` |
| O 23 r 18(2) | none | none | none (counts the amount as part of the charges, expenses and fees under rule 11(2)(b)(i)) | `o 23 r 18(2)` |
| O 24 r 1 | none | none | none (scope) | `o 24 r 1` |
| O 24 r 2(1) | none | none | none (definition) | `o 24 r 2(1)` |
| O 24 r 2(2) | the defendant to a prerogative-order application (until remedies are used) | the applicant: shall not apply before exhausting every right of appeal and other remedy | immunity / disability (prohibition derived under N2) | `o 24 r 2(2)` (regulative rule `o 24 r 2(2) the applicant shall not apply for a prerogative order before exhausting every right of appeal or other remedy`) |
| O 24 r 3(1)-(2) | not named in the text | the applicant (mode: originating application without notice); the subject (must make the supporting affidavit) | duty | `o 24 r 3(1), (2)` |
| O 24 r 3(3) | some other person (may make the affidavit if the subject is unable or the application is urgent) | none named | liberty / no-right, conditional | `o 24 r 3(3)` |
| O 24 r 3(4) | none | none | none (forum) | `o 24 r 3(4)` |
| O 24 r 3(5) | the subject (need not be brought) and the Court (may direct otherwise) | the Court | immunity / disability; power / liability | `o 24 r 3(5)` |
| O 24 r 3(6) | the Court | the person who detains the subject | power / liability | `o 24 r 3(6)` |
| O 24 r 4(1) | none | none | none (the summons is in the originating application) | `o 24 r 4(1)` |
| O 24 r 4(2) | the defendant and the Attorney-General (to be served) | the applicant: must serve as soon as practicable and no later than 2 working days after filing | claim / duty | `o 24 r 4(2)` (regulative rule `o 24 r 4(2) the applicant must serve the documents within 2 working days after filing`) |
| O 24 r 4(3)-(4) | the applicant (may name the Attorney-General as defendant); the Attorney-General (may apply for another defendant to be added or substituted) | the defendant; the other parties | liberty / no-right; power / liability | `o 24 r 4(3), (4)` |
| O 24 r 4(5) | the defendant and the Attorney-General (may file and serve affidavits) | the other parties | liberty / no-right | `o 24 r 4(5)` |
| O 24 r 4(6) | every other party | every party to the summons: must serve the affidavits to be used, as soon as practicable and no later than 2 working days after filing | claim / duty | `o 24 r 4(6)` |
| O 24 r 4(7) | none | none | none (forum) | `o 24 r 4(7)` |
| O 24 r 4(8) | the subject (need not be brought) and the Court (may direct otherwise) | the Court | immunity / disability; power / liability | `o 24 r 4(8)` |
| O 24 r 4(9) | the Court | the parties and the defendant | power / liability | `o 24 r 4(9)` |
| O 24 r 4(10)-(11) | the subject and the Court (the Order is to be complied with although not served) | the solicitor for the defendant (must inform); the defendant or the appropriate person or entity (must comply) | claim / duty | `o 24 r 4(10), (11)` (regulative rule `o 24 r 4(11) the defendant must comply with the Order for Review of Detention`) |
| O 24 r 5(1) | (a) the applicant (may include a declaration); (b) the defendant (until permission is granted) | (b) the applicant: must not apply unless permission has been granted | (a) liberty / no-right; (b) immunity / disability | `o 24 r 5(1)(a), (b)` |
| O 24 r 5(2) | the defendant (once the 3 months have run) | the applicant (loses the power to apply for permission) | power / liability, read from the time limit | `o 24 r 5(2)` |
| O 24 r 5(3) | not named in the text | the applicant: must apply by originating application with a statement and an affidavit that shows the three matters | duty | `o 24 r 5(3)` |
| O 24 r 5(4) | the defendant | the applicant: bound by the statement; may not rely on another ground or relief unless the Court allows | immunity / disability | `o 24 r 5(4)` |
| O 24 r 5(5) | the defendant and the Attorney-General | the applicant: must serve as soon as practicable and no later than 2 working days after filing | claim / duty | `o 24 r 5(5)` |
| O 24 r 5(6)-(7) | the Attorney-General (may apply); the defendant and the Attorney-General (may file and serve affidavits) | the other parties | power / liability; liberty / no-right | `o 24 r 5(6), (7)` |
| O 24 r 5(8) | none | none | none (forum) | `o 24 r 5(8)` |
| O 24 r 5(9) | the Court | the parties | power / liability | `o 24 r 5(9), 5(9)(a)` |
| O 24 r 6(1) | not named in the text | the applicant: must apply by summons in the originating application in which permission was obtained | duty | `o 24 r 6(1)` |
| O 24 r 6(2) | the defendant | the applicant (the permission lapses unless the summons is filed within 14 days) | immunity / disability, read from "lapses" | `o 24 r 6(2)` |
| O 24 r 6(3) | the defendant and the Attorney-General | the applicant: must serve the order and the summons, as soon as practicable and no later than 2 working days after filing | claim / duty | `o 24 r 6(3)` |
| O 24 r 6(4) | none | none | none (forum) | `o 24 r 6(4)` |
| O 24 r 6(5) | the Court | the parties | power / liability | `o 24 r 6(5)` |
| O 24 r 6(6)-(7) | the applicant (the Order is to be complied with although not served) | the solicitor for the defendant (must inform); the defendant or the appropriate person or entity (must comply) | claim / duty | `o 24 r 6(6), (7)` |
| O 24 r 6(8) | the Court (subject to the Government Proceedings Act) | the defendant | power / liability | `o 24 r 6(8)(a), (b)` |
| O 24A r 1(1)-(2) | none | none | none (definition and reading rule) | `o 24A r 1(1), (2)` |
| O 24A r 1(3) | not named in the text | the applicant: an application for PACC permission by originating application; a PACC application by summons in that application | duty (mode) | `o 24A r 1(3)` |
| O 24A r 2(1) | not named in the text | not named who must fix the hearing | duty (bearer not named) | `o 24A r 2(1)` |
| O 24A r 2(2)-(4) | not named in the text (section 60G(4) of the Act is cited) | the applicant for PACC permission: must file written submissions (35 pages unless the Court of Appeal allows) and the other documents with the application | duty (no claimant named) | `o 24A r 2(2), (3), (4)(a), (4)(b)` |
| O 24A r 2(5) | none | none | none (to avoid doubt) | `o 24A r 2(5)` |
| O 24A r 2(6) | the respondent | the applicant: must serve the application, submissions and documents | claim / duty | `o 24A r 2(6)` |
| O 24A r 2(7)-(9) | (9) the respondent (to be served); (8) not named in the text | the applicant: must file the new counsel's affidavit within 3 days and serve it on the respondent | claim / duty (for (9)); duty (for (8)) | `o 24A r 2(7), (8), (9)` |
| O 24A r 2(10) | the respondent (may file written submissions within 3 days) | the applicant | liberty / no-right | `o 24A r 2(10)(a), (b)(i), (b)(ii)` (regulative rule `o 24A r 2(10) the respondent may file written submissions within 3 days after the application is filed and served`) |
| O 24A r 2(11)-(12) | (11) not named in the text; (12) the respondent (may file a supporting affidavit with the submissions) | (11) the respondent: submissions subject to the 35-page limit unless the Court of Appeal allows; (12) the applicant (has no claim to prevent it) | (11) duty; (12) liberty / no-right | `o 24A r 2(11), (12)` |
| O 24A r 2(13) | the Court of Appeal | the applicant and the respondent | power / liability | `o 24A r 2(13)` |
| O 24A r 3(1) | not named in the text (section 60H(1) of the Act is cited) | the applicant: must make the PACC application within 3 days after permission is granted | duty (no claimant named) | `o 24A r 3(1)` (regulative rule `o 24A r 3(1) the applicant must make the PACC application within 3 days after permission is granted`) |
| O 24A r 3(2) | not named in the text | not named who must fix the hearing | duty (bearer not named) | `o 24A r 3(2)` |
| O 24A r 3(3) | not named in the text (section 60H(2) of the Act is cited) | the applicant: must file the affidavit with the PACC application and the written submissions within 3 days | duty (no claimant named) | `o 24A r 3(3)(a), (3)(b)` |
| O 24A r 3(4) | the respondent | the applicant in a PACC application: must serve within the day it is made | claim / duty | `o 24A r 3(4)` |
| O 24A r 3(5) | not named in the text (section 60H(3) of the Act is cited) | the respondent: must file written submissions in response within 3 days | duty (no claimant named) | `o 24A r 3(5)` |
| O 24A r 3(6)-(7) | the Court of Appeal (may allow the 35-page limit to be exceeded in special circumstances) | the parties | power / liability | `o 24A r 3(6), (7)` |
| O 24A r 3(8) | every other party to the PACC application | each party: must serve its written submissions within the day on which they are filed | claim / duty | `o 24A r 3(8)` |
| O 24A r 4 | not named in the text | the applicant who appoints additional counsel: must file and serve a notice of appointment in Form 3 | duty | `o 24A r 4` |
| O 25 r 1 | none | none | none (definitions) | `o 25 r 1` |
| O 25 r 2(1) | not named in the text | not named in the text ("Court fees must be paid") | duty (no claimant or bearer named) | `o 25 r 2(1)` |
| O 25 r 2(2)-(4), (6) | none | none | none (counting rules for the value of the claim) | `o 25 r 2(2), (4), (6), `o 25 r 2 the value of the claim`` |
| O 25 r 2(5) | the Registrar | the parties (to pay the difference; or to be refunded the excess) | power / liability | `o 25 r 2(5)` |
| O 25 r 3(1)-(2) | the Court | the parties | power / liability | `o 25 r 3(1), (2)` |
| O 25 r 3(3) | the person requesting a refund (may request, in writing and in time) | the Court | liberty / no-right, conditional on form and time | `o 25 r 3(3)(a)-(d)` |
| O 25 r 3(4) | the party who paid the hearing fees | the Court: must refund the whole if notified in writing at least 14 days before the first hearing date | claim / duty | `o 25 r 3(4)` |
| O 25 r 3(5) | any party dissatisfied with the Registrar's decision (may apply by letter to a Judge within 14 days) | the Registrar (liable to review) | power / liability | `o 25 r 3(5)` (regulative rule `o 25 r 3(5) a dissatisfied party may apply by letter to a Judge within 14 days after the decision`) |
| O 25 r 3(6) | the Court | the party who must pay the fees | power / liability | `o 25 r 3(6)` |
| O 25 r 4(1) | the Registrar (discretion: "if he or she thinks fit") | the person who paid for an unused document (has no claim) | liberty / no-right | `o 25 r 4(1)` |
| O 25 r 4(2)-(3) | not named in the text | the applicant: by signed request, within 3 months, one application for each document | duty (conditions of the request) | `o 25 r 4(2)(a), (2)(b), (3)` |
| O 25 r 4(4) | the Registrar | the applicant (the fee paid for the request is not refundable) | liberty / no-right (flat negative, N2) | `o 25 r 4(4)` |
| O 25 r 5 | a party in the listed proceedings (no hearing fee is payable) | the Court (no power to charge) | immunity / disability | `o 25 r 5` |
| O 25 r 6 | not named in the text | a party in winding up proceedings fixed on special hearing dates, and in appeals relating to them: hearing fees are payable | duty (no claimant named) | `o 25 r 6` |
| O 25 r 7(1)-(2) | the Registrar (may issue); a party to criminal proceedings affecting life or liberty (may apply by letter) | the Registrar (liable to the application) | power / liability; liberty / no-right | `o 25 r 7(1), (2)` |
| O 25 r 7(3) | any party in the cause or matter (and in an appeal) | the Court (no fee, no security for costs from the time the certificate is issued) | immunity / disability | `o 25 r 7(3)(a), (3)(b)` |
| O 25 r 7(4) | the Registrar | the party who paid before the certificate | power / liability | `o 25 r 7(4)` |
| O 25 r 7(5) | none | none | none (saving for costs orders) | `o 25 r 7(5)` |
| O 25 r 8(1) | not named in the text (the State Courts provide the service) | each party in a District Court case: must pay $250 for all Court ADR services provided | duty (no claimant named) | `o 25 r 8(1)` (regulative rule `o 25 r 8(1) each party in a District Court case must pay the Court ADR fee`) |
| O 25 r 8(2) | none | none | none (when the fee is payable) | `o 25 r 8(2)` |
| O 25 r 8(3) | a party to a non-injury motor accident action, a death or personal injuries action, a Protection from Harassment Act action or a Community Disputes Resolution Act action | the State Courts (no fee) | immunity / disability | `o 25 r 8(3)` |
| O 25 r 8(4) | the party requesting a refund (may make a written request to the Registrar within one month) | the Registrar | liberty / no-right, conditional on form and time | `o 25 r 8(4)` |
| O 25 r 8(5) | none | none | none (definition) | `o 25 r 8(5)` |
| O 26 r 1 | the Chief Justice or the Presiding Judge of the State Courts | the Registrar; the Chief Executive and Assistant Chief Executives | power / liability | `o 26 r 1(1), (2), (3)` |
| O 26 r 2 | the Registrar (with the approval of the Chief Justice or the Presiding Judge) | everyone bound by the practice directions | power / liability | `o 26 r 2` |
| O 26 r 3(1)-(3) | not named in the text (for (1) and (2)); none for (3) | the Registry: must maintain Court records (1); may collect, use or disclose data (2); the method and period of storage are in the Registrar's discretion (3) | duty; liberty / no-right; none (a discretion with no counterparty) | `o 26 r 3(1), (2), (3)` |
| O 26 r 3(4) | the Registrar (may allow a person who shows a valid interest and pays the prescribed fee) | the person who asks (has no claim) | power / liability | `o 26 r 3(4)` |
| O 26 r 3(5) | the Registrar | the person who asks to search, inspect or copy | power / liability | `o 26 r 3(5)` |
| O 26 r 3(6) | the Registrar (approves) | everyone: documents and records must not be taken out of the Registry without approval | claim / duty (prohibition, N2) | `o 26 r 3(6)` |
| O 26 r 3(7) | not named in the text | the person who files a document in Court: it must be typewritten, printed and comply with the practice directions | duty (no claimant named) | `o 26 r 3(7)` |
| O 26 r 3(8)-(9) | the Registrar | the person authorised to provide the service: must pay the agreed fees | power / liability; claim / duty | `o 26 r 3(8), (9)` |
| O 26 r 3(10) | a subscriber to the service | the Registrar (cannot charge the fee or require permission) | claim / duty | `o 26 r 3(10)` |
| O 26 r 4(1) | a person who deposits a power of attorney | the Registry of the Supreme Court | liberty / no-right, conditional on verification | `o 26 r 4(1)` |
| O 26 r 4(2) | not named in the text | the Registry of the Supreme Court: must maintain the index | duty | `o 26 r 4(2)` |
| O 26 r 4(3) | any person who pays the prescribed fee | the Registry of the Supreme Court | claim / duty | `o 26 r 4(3)` |
| O 26 r 5(1) | not named in the text (the public) | the Registry: must be open every day except non-court days | duty | `o 26 r 5(1)` |
| O 26 r 5(2) | the Chief Justice or the Presiding Judge | the Registry | power / liability (machinery: inert, reason 2; no function) | none |
| O 26 r 6 | not named in the text | the court: there must be a Judge available during the Court vacations to hear urgent matters | duty (no claimant named) | `o 26 r 6` |
| O 27 r 1 | none | none | none (definitions) | `o 27 r 1` |
| O 27 r 2(1) | not named in the text (the Court) | the trustee: must apply by summons supported by an affidavit that sets out the four matters | duty | `o 27 r 2(1)` |
| O 27 r 2(2) | the trustee | none named | immunity (no affidavit need be filed for such a legacy) | `o 27 r 2(2)` |
| O 27 r 3 | every person appearing to be entitled to, or to have an interest in, what was lodged | the person who lodged: must forthwith give notice | claim / duty | `o 27 r 3` (regulative rule `o 27 r 3 the person who lodged must give notice of the lodgment`) |
| O 27 r 4(1) | not named in the text (the Accountant-General) | the person lodging money: must use a direction in Form 44(a) | duty | `o 27 r 4(1)` |
| O 27 r 4(2) | the person lodging securities | the Accountant-General | liberty / no-right | `o 27 r 4(2)` |
| O 27 r 4(3)-(4) | the Accountant-General | the person lodging (must execute the transfer and send it with the authority in Form 45); the company or body corporate (must forward the authority with a certificate) | claim / duty | `o 27 r 4(3), (4)` |
| O 27 r 4(5) | the person lodging other securities | the Accountant-General | liberty / no-right | `o 27 r 4(5)` |
| O 27 r 4(6)-(7) | the person lodging (to be given a receipt); the Registrar (to be sent a copy) | the Accountant-General | claim / duty | `o 27 r 4(6), (7)` |
| O 27 r 5 | not named in the text (the holders of the credit) | the Accountant-General: must place principal money and dividends to the right credit | duty | `o 27 r 5` |
| O 27 r 6(1) | the person to whose credit money is lodged (interest at the Minister's rate, with exceptions) | the Accountant-General (implied: the text says the money "must be credited") | claim / duty | `o 27 r 6(1)` |
| O 27 r 6(2) | none | none | none (deeming) | `o 27 r 6(2)` |
| O 27 r 7(1)-(3) | none | none | none (how interest is computed) | `o 27 r 7(1), (2), (3)` |
| O 27 r 7(4)-(5) | not named in the text (the holders of the credit) | the Accountant-General: must place accrued interest to the credit within 15 days after the year ends, and on withdrawal | duty | `o 27 r 7(4), (5)` (regulative rule `o 27 r 7(4) the Accountant-General must place the interest for the year to the credit within 15 days`) |
| O 27 r 7(6)-(7) | none | none | none (which part is treated as withdrawn; when credited interest is placed on deposit) | `o 27 r 7(6), (7)` |
| O 27 r 8 | not named in the text (the payee) | the Accountant-General (implied): money must be paid out on a direction in Form 44(b) | duty | `o 27 r 8` |
| O 27 r 9(1)-(2) | none | none | none (what an order must state) | `o 27 r 9(1), (2)` |
| O 27 r 9(3) | any co-partner, or the survivor | none named | liberty / no-right | `o 27 r 9(3)` |
| O 27 r 10(1)-(4) | the Accountant-General (may pay, transfer or deliver the funds to the legal personal representatives, the person entitled to administration in the small-estate case, or the survivor) | those persons (have no claim to be paid unless an order directs) | liberty / no-right | `o 27 r 10(1), (2), (3), (4)` |
| O 27 r 10(5) | the Commissioner of Estate Duty (entitled to attend and be heard) | the applicant: must give notice of the application | claim / duty | `o 27 r 10(5)` |
| O 27 r 11(1)-(2) | not named in the text | the party having the carriage of the order: must lodge a copy with the Accountant-General; the Accountant-General: must act in accordance with the order | duty (no claimant named) | `o 27 r 11(1), (2)` |
| O 27 r 11(3)-(4) | the Court | the parties | power / liability | `o 27 r 11(3), (4)` |
| O 27 r 11(5) | the Sheriff | the applicant for an order under paragraph (4): must serve it on the Sheriff | claim / duty | `o 27 r 11(5)` |
| O 27 r 12 | a person claiming to be interested in funds in Court (on a signed request) | the Accountant-General: must issue a certificate unless there is good reason for refusing | claim / duty | `o 27 r 12` |
| O 27 r 13 | not named in the text (the public) | the Accountant-General: must publish the list in the Gazette in January | duty | `o 27 r 13` |
| O 27 r 14(1) | the Government | the Accountant-General and the Sheriff: funds 6 years or more without a claim must be transferred and paid | claim / duty | `o 27 r 14(1)` |
| O 27 r 14(2) | a claimant who establishes the claim to the Court's satisfaction | the Government: must pay the principal | claim / duty | `o 27 r 14(2)` |
| O 27 r 14(3) | the minor, or the minor's account | the Accountant-General and the Sheriff (no transfer until the minor comes of age or dies) | immunity / disability | `o 27 r 14(3)` |
| O 27 r 15(1)-(2) | not named in the text | the Sheriff: must keep an account; must keep money in a bank or with the Accountant-General | duty | `o 27 r 15(1), (2)` |
| O 27 r 15(3) | the Sheriff | the person who paid or deposited money (no interest is payable) | liberty / no-right (flat negative, N2) | `o 27 r 15(3)` |
| O 27 r 16 | the person who pays or deposits | the Registry officer receiving the money: must give a receipt | claim / duty | `o 27 r 16` |
| O 27 r 17 | the person entitled to the money | the person making a payment under a judgment or order: must produce a copy and give notice | claim / duty | `o 27 r 17` (regulative rule `o 27 r 17 the person making the payment must produce a copy and give notice`) |
| O 27 r 18 | not named in the text (the person entitled) | the Sheriff: must require proof before paying out | duty | `o 27 r 18` |
| O 27 r 19 | the Government | the Sheriff: must satisfy himself or herself that money due to the Government has been paid or deducted | claim / duty | `o 27 r 19` |
| O 27 r 20 | not named in the text (the Registrar approves the method) | the Sheriff: must make all payments by a method the Registrar approves | duty (no claimant named) | `o 27 r 20` |
| O 27 r 21 | not named in the text (the judgment creditor) | the Registrar: must cause the instalments ledger to be opened | duty | `o 27 r 21` |

The table has 156 rows: 132 create a relation and 24 are `none` (definitions, counting rules, saving clauses, forum, effect dates).
Every rule from Order 23 rule 1 to Order 27 rule 21 has a row; Order 26 rule 1 and rule 5(2) have a row and no function (machinery, inert reason 2).

## Marginal readings for a lawyer (roc6)

These are the branches that rest on one of the two readings the brief marks "for a lawyer, not for you to decide".
I took them as the status quo.
The lists were built by a script that reads the `FALSE-kind` and `NOTHING-kind` comments in the layer-1 files, so a branch whose comment does not use the words the script looks for is not on the list; the other branches are listed in the files with their comments.

### (a) A failed "if" counts as the text's no, clause by clause

The other reading: "if A then B" does not itself say "if not A then not B", so a failed condition is silent and answers `NOTHING`.
Each row below answers `JUST FALSE` where the other reading would answer `NOTHING`.
Not repeated here: the 38 branches tagged ruling (a) (an act outside a period the text fixes), which the ruling of 2026-11-05 decided; and the 59 tagged ruling (b) (a "where" or "if" condition that fails), which are branches of this very kind, now settled by the ruling, which treats a failed "where" like "if". The rows below are the failed-condition branches the ruling did not reach: they rest on this reading until a lawyer rules.
The audit of the period functions (ruling (a)) is under Seams, "Audit of period functions": which functions answer `JUST FALSE` outside a stated period, and which keep `NOTHING` with a fork line.
Quotes that say "unless", "except", "only if", "must not" or "need not" are the text's own no (the brief counts them so) and are not listed.

| function | the clause | other reading |
| --- | --- | --- |
| `o 23 r 7(2) the Court must state in open court what the paragraph lists` | "If the Court hears the application in private under paragraph (1) and decides to make a committal order ..., it must state in open court" | `NOTHING` |
| `o 23 r 7(4)(a) the committal respondent must rely on the matters stated in the affidavit` | "must rely on the matters stated in his or her affidavit, if any": with no affidavit there is nothing to rely on under this sub-paragraph" | `NOTHING` |
| `o 23 r 9(2) the Sheriff may take possession of the thing` | "Where a committal respondent has been committed ... under section 4 ..., then, if the thing is in the possession or control of the committal respondent, the Sheriff may take possession of it" | `NOTHING` |
| `o 23 r 9(2) the Court may discharge the committal respondent and give directions for dealing with the thing` | "Where ... then, if the thing is in the possession or control of the committal respondent, ... the Court may discharge the committal respondent and give directions" | `NOTHING` |
| `o 23 r 15(4) the Court's permission to give the non-publication direction lapses` | the permission lapses "if the direction is not served ... within 14 days", and the 14 days have not run | `NOTHING` |
| `o 23 r 16(6) the supporting affidavit states that the applicant is the author` | "If the applicant is the author of the matter ..., the supporting affidavit must state and give evidence of that fact" | `NOTHING` |
| `o 23 r 16(7) the order is served within 14 days after the date of the order` | "If the Court sets aside or varies a non‑publication direction, the applicant must serve the order" | `NOTHING` |
| `o 23 r 16(8) the applicant has filed the affidavit of service of the order` | "If an order of Court is required to be served in accordance with paragraph (7), the applicant must, after the order has been served, file an affidavit" | `NOTHING` |
| `o 24 r 3(3) some other person may make the affidavit` | "If the subject is unable to make the affidavit or if the application is urgent, some other person may make the affidavit" | `NOTHING` |
| `o 24 r 6(8)(b) the Court may also order that the applicant be awarded a liquidated amount, damages to be assessed or equitable relief` | "if it is satisfied that the applicant would have been entitled to such remedies in a separate action against the defendant" | `NOTHING` |
| `o 25 r 3(4) the Court must refund the whole of the hearing fees paid` | "if the Court is notified in writing not later than 14 days before the first date fixed for hearing" | `NOTHING` |
| `o 25 r 7(3)(a) no fee is payable by any party in the cause or matter` | "from the time that a certificate is issued under paragraph (1)"; none was issued | `NOTHING` |
| `o 25 r 7(3)(b) no security for costs is required to be provided by any party in the cause or matter` | "from the time that a certificate is issued under paragraph (1)"; none was issued | `NOTHING` |
| `o 26 r 3(4) the Registrar may allow the person to search for, inspect and take a copy of the document` | "if that person — (a) shows a valid interest in the document in question; and (b) pays the prescribed fee" | `NOTHING` |
| `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court` | "if — (a) the execution of the document is verified by — (i) ...; (ii) ...; or (iii) ..." | `NOTHING` |
| `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court` | "if ... (b) the document is accompanied by the affidavit, statutory declaration, certificate or other evidence by which the execution was verified" | `NOTHING` |
| `o 26 r 4(1) the document creating a power of attorney may be deposited in the Registry of the Supreme Court` | "if ... (c) in the case of a certified copy of the document, the signature of the person who verified the copy is sufficiently verified" | `NOTHING` |
| `o 26 r 4(3) the person is entitled to do this` | "on payment of the prescribed fee" | `NOTHING` |
| `o 27 r 4(4) the company or body corporate has forwarded the authority with the certificate` | "after registering such transfer" | `NOTHING` |
| `o 27 r 4(6) the Accountant-General has received the box or packet and given a receipt` | "After inspecting the contents in the box or packet in the presence of the person lodging the same" | `NOTHING` |
| `o 27 r 4(7) the Accountant-General has sent the Registrar a copy of the receipt` | "after receiving the money or securities" | `NOTHING` |
| `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | "If no administration has been taken out to the estate of such deceased person" | `NOTHING` |
| `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | "who has died intestate" | `NOTHING` |
| `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | "whose assets do not exceed the value of $10,000, including the amount of the funds" | `NOTHING` |
| `o 27 r 14(1) the funds must be transferred and paid to the Government for the general purposes of the State` | "without any claim having been made and allowed thereto during that period" | `NOTHING` |
| `o 27 r 14(2) the Government must pay the claimant` | "If any claim is made ..., and if such claim is established to the satisfaction of the Court, the Government must pay": the number function above cannot carry a no, so this is its yes/no twin (the Rule gives the principal only, and no interest) | `NOTHING` |

26 branches.

### (b) A prohibition or grant limited by its own wording does not

The other reading: the limit is the text's own no, so a case outside it answers `JUST FALSE`.
Each row below answers `NOTHING` where the other reading would answer `JUST FALSE`.

| function | what limits it | other reading |
| --- | --- | --- |
| `o 23 r 1 "contempt of court" is contempt under the Act, and includes contempt under the common law` | "subject to section 8" cuts the inclusion back, and what section 8 says is outside the sources | `JUST FALSE` |
| `o 23 r 2 the power to punish for contempt of court may be exercised by a committal order` | the Rule names a committal order as one way of exercising the power and does not say it is the only way | `JUST FALSE` |
| `o 23 r 3(1) the committal applicant has first applied to the Court for permission` | the duty is a committal applicant's | `JUST FALSE` |
| `o 23 r 5(2) Rules 2, 3 and 4 affect the power to make a committal order on its own accord` | the paragraph names three courts only | `JUST FALSE` |
| `o 23 r 6(1) the application to transfer a case is made in the way required` | the paragraph speaks only of an application under section 10(4) | `JUST FALSE` |
| `o 23 r 6(2) the General Division may order the case and related proceedings stayed` | "In hearing such an application, the General Division may order ..." names one kind of order | `JUST FALSE` |
| `o 23 r 6(3)(a) the General Division may do this on ordering the transfer` | "the General Division may —" lists three things | `JUST FALSE` |
| `o 23 r 7(1) the Court may hear the application in private` | the paragraph speaks of those two applications | `JUST FALSE` |
| `o 23 r 7(1) the Court must hear the application in open court` | the paragraph speaks of those two applications | `JUST FALSE` |
| `o 23 r 7(4)(b) the committal respondent may give oral evidence` | "may, with the permission of the Court, give oral evidence on his or her own behalf" | `JUST FALSE` |
| `o 23 r 7(5) the Court is to have regard to the matter` | the paragraph speaks of an order under section 26A(1) | `JUST FALSE` |
| `o 23 r 7(6) the Court is to have regard to the matter` | the paragraph speaks of an order under section 26A(2) or (3) | `JUST FALSE` |
| `o 23 r 7(6) the Court is to have regard to the matter` | (e) is for an order under section 26A(3) allowing an expert witness to give evidence from outside Singapore | `JUST FALSE` |
| `o 23 r 8(1) the Court may order the execution of the committal order to be suspended` | the power is over "the committal order" | `JUST FALSE` |
| `o 23 r 8(3) the committal applicant may apply for the suspension to be lifted` | "on the ground that any of the terms of the suspension has been breached" | `JUST FALSE` |
| `o 23 r 10 Rules 1 to 9 affect the Court's power to make the order` | the saving is for the two orders it names | `JUST FALSE` |
| `o 23 r 10 Rules 1 to 9 apply to the application as they apply to an application for a committal order` | the sentence speaks of "an application for such an order" | `JUST FALSE` |
| `o 23 r 10 Rules 1 to 9 apply to the application as they apply to an application for a committal order` | "so far as applicable and with the necessary modifications" | `JUST FALSE` |
| `o 23 r 12(1) Rules 1 to 11 apply to committal proceedings before a tribunal` | the paragraph speaks of "Rules 1 to 11" | `JUST FALSE` |
| `o 23 r 12(2) how a reference in Order 23 is read for a committal proceeding before an Employment Claims Tribunal` | paragraph (2) names references to a Court and to a Judge | `JUST FALSE` |
| `o 23 r 12(3) the court fees that apply to proceedings under this Order in a tribunal are those in` | the paragraph speaks of proceedings in a tribunal | `JUST FALSE` |
| `o 23 r 13(3) the court fees and hearing fees that apply to proceedings under this Order in a tribunal are those in` | the paragraphs speak of proceedings in a tribunal | `JUST FALSE` |
| `o 23 r 14(2) how a reference in Order 23 is read for a Community Disputes Resolution Tribunal` | paragraph (2) names references to a Court and to a Judge | `JUST FALSE` |
| `o 23 r 15(1) the Attorney-General's application is made in the way required` | the paragraph speaks of an application by the Attorney-General | `JUST FALSE` |
| `o 23 r 16(2) the application is made within 14 days after the direction is served` | "This Rule applies to an application under section 13(9)" | `JUST FALSE` |
| `o 23 r 17(1) the Court may order the Sheriff or a police officer to arrest and bring the committal respondent before the Court` | "who fails to attend any proceedings in Court or who disobeys any order of the Court" | `JUST FALSE` |
| `o 23 r 17(2) the Court may include conditions about security or any other matter in the order to arrest` | the power is over "the order to arrest under paragraph (1)" | `JUST FALSE` |
| `o 23 r 17(3) the letter is sufficient authority for the Sheriff or a police officer to effect the arrest` | "A letter from the Registrar stating the Court’s order made under paragraph (1)" | `JUST FALSE` |
| `o 23 r 18(1) the Sheriff may engage, or direct the applicant to engage, the person` | "any auxiliary police officer appointed under the Police Force Act or other security agency to assist him or her in the discharge of his or her duties under this Order" | `JUST FALSE` |
| `o 23 r 18(2) the amount is part of the charges, expenses and fees incurred in complying with a committal order` | the paragraph speaks of "Any amount of money incurred by the Sheriff under paragraph (1)" | `JUST FALSE` |
| `o 24 r 3(6) the Court may do this at the hearing of the application` | "the Court may —" names two things | `JUST FALSE` |
| `o 24 r 4(4) the Attorney-General may apply to the Court for another defendant to be added or substituted` | the order sought is that "he or she cease to be a defendant", which presupposes that the Attorney-General is one, and the paragraph does not say what follows if he or she is not | `JUST FALSE` |
| `o 24 r 4(5) the person may file and serve an affidavit to contest the summons` | "The defendant and the Attorney‑General may file and serve affidavits" | `JUST FALSE` |
| `o 24 r 4(5) the affidavits may be made in this way` | "may make their affidavits jointly or separately" | `JUST FALSE` |
| `o 24 r 4(9) the Court may order this at the hearing of the summons` | "the Court may order that —" names three things | `JUST FALSE` |
| `o 24 r 5(1)(a) the application may include an application for a declaration` | "a declaration which is ancillary to or consequential upon the Order" | `JUST FALSE` |
| `o 24 r 5(9) the Court may order this at the hearing of the application for permission` | "the Court may order that —" names four things | `JUST FALSE` |
| `o 24 r 6(5) the Court may order this at the hearing` | "the Court may order that —" names four things | `JUST FALSE` |
| `o 24 r 6(8)(a) the Court may also make a declaration` | "a declaration which is ancillary to or consequential upon the Order" | `JUST FALSE` |
| `o 24A r 1(1) a reference to a section is a reference to a section in the Act` | "unless it is otherwise expressly provided", and what is provided is not stated here | `JUST FALSE` |
| `o 24A r 1(3) the application is made in the way required` | "An application to which this Order applies" | `JUST FALSE` |
| `o 24A r 2(5) the affidavit must state the information even though it relates to an event before 28 June 2024` | "even if that information relates to any event that took place before 28 June 2024, where applicable": the paragraph makes the point for those events only | `JUST FALSE` |
| `o 24A r 2(7) paragraphs (8) and (9) apply to the applicant` | "in any of the following circumstances" names two | `JUST FALSE` |
| `o 24A r 2(8) the affidavit of the newly appointed counsel is filed within 3 days after the appointment` | "the applicant mentioned in paragraph (7)" | `JUST FALSE` |
| `o 24A r 2(13) the Court of Appeal may allow the page limit to be exceeded` | "in special circumstances" | `JUST FALSE` |
| `o 24A r 3(7) the Court of Appeal may allow the page limit to be exceeded` | "in special circumstances" | `JUST FALSE` |
| `o 25 r 2(2) paragraph (2) applies to the court fees` | "payable in the Supreme Court"; the paragraph does not say how the value is found in the State Courts | `JUST FALSE` |
| `o 25 r 2(5) the Registrar may require the parties to pay the difference in the court fees` | the power is to require "the difference"; with no difference there is nothing to require | `JUST FALSE` |
| `o 25 r 2(5) the Registrar may refund to the parties the excess court fees paid` | the power is to refund "the excess court fees paid"; with no excess there is nothing to refund | `JUST FALSE` |
| `o 25 r 3(1) the Court may make this order about court fees` | "the Court may —" names three things | `JUST FALSE` |
| `o 25 r 3(2) the Court may exercise the powers in paragraph (1) in accordance with a Civil Procedure Convention` | "also exercise ... in accordance with the provisions in any Civil Procedure Convention"; what the Convention provides is outside the sources | `JUST FALSE` |
| `o 25 r 3(5) the party may apply by letter to a Judge to review the decision within 14 days` | "Any party who is dissatisfied with any decision of the Registrar made under this Rule may apply by letter to a Judge" | `JUST FALSE` |
| `o 25 r 3(6) the Court may make the order it deems fit` | "to secure compliance with any requirement for the payment of any court fees, including the giving of judgment or the dismissal of any claim or counterclaim" | `JUST FALSE` |
| `o 25 r 4(1) the Registrar may refund the fee or part of the fee` | "paid for any unused document" | `JUST FALSE` |
| `o 25 r 6 hearing fees are payable` | the Rule is about "the winding up of companies, limited liability partnerships or variable capital companies and their sub-funds" | `JUST FALSE` |
| `o 25 r 7(4) the Registrar may refund the fee or part of the fee` | "in respect of a cause or matter for which a certificate under paragraph (1) is issued" is a scope limit with no "only" | `JUST FALSE` |
| `o 25 r 7(5) this Rule prevents the Court from making the order for costs` | the saving covers an order for costs in the cause or matter and its appeals | `JUST FALSE` |
| `o 25 r 8(1) the Court ADR fee is payable by the party` | "payable by each party in a case" | `JUST FALSE` |
| `o 25 r 8(1) the Court ADR fee is payable by the party` | "for all Court ADR services that are provided in the case" | `JUST FALSE` |
| `o 25 r 8(1) the Court ADR fee is payable by the party` | "in a case in a District Court" | `JUST FALSE` |
| `o 25 r 8(2) the Court ADR fee is payable at the date asked about` | "pursuant to either of the following" | `JUST FALSE` |
| `o 26 r 1(3) the office may appoint a Chief Executive and one or more Assistant Chief Executives` | "the Chief Justice or the Presiding Judge of the State Courts (as the case may be) may appoint": the power is the office's for its own Registry, and the paragraph does not say that another office may not | `JUST FALSE` |
| `o 26 r 2 the directions are issued under Order 26, Rule 2` | "The Registrar may issue practice directions" | `JUST FALSE` |
| `o 26 r 2 the directions are issued under Order 26, Rule 2` | "with the approval of the Chief Justice or the Presiding Judge of the State Courts, as the case may be" | `JUST FALSE` |
| `o 26 r 3(2) the Registry may collect, use or disclose the data` | "such data which the Registrar considers appropriate" | `JUST FALSE` |
| `o 26 r 3(3) the matter is in the discretion of the Registrar` | the paragraph names the method of collection, the storage and the period of storage of Court records, documents and data | `JUST FALSE` |
| `o 26 r 3(5) the Registrar may redact the document before a person searches for, inspects or takes a copy of it` | "in the interests of justice" | `JUST FALSE` |
| `o 26 r 3(8) the Registrar may authorise a person to provide the service` | "a service that enables a subscriber of that service — (a) ...; and (b) ..." | `JUST FALSE` |
| `o 26 r 3(10) the subscriber may do this without paying the prescribed fee and without the Registrar's permission` | the subscriber is entitled to the two things named | `JUST FALSE` |
| `o 26 r 4(3) the person is entitled to do this` | the entitlement is to the three things named | `JUST FALSE` |
| `o 26 r 6 a Judge is available during the Court vacations to hear the matter` | "to hear such matters as the Registrar considers urgent" is a scope limit with no "only" | `JUST FALSE` |
| `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required` | "any trustee wishing to make a payment into Court under section 62 of the Trustees Act" | `JUST FALSE` |
| `o 27 r 2(1) the summons must be supported by an affidavit` | "any trustee wishing to make a payment into Court under section 62 of the Trustees Act" is a scope limit with no "only" | `JUST FALSE` |
| `o 27 r 4(2) the securities may be transferred to the Accountant-General in his or her official name` | "Securities issued by a company or by any body corporate constituted under any written law, being fully paid up and free from liability" | `JUST FALSE` |
| `o 27 r 4(5) the securities may be placed in a box or packet and lodged with the Accountant-General` | "Securities, other than those described in paragraph (2), may be placed in a box or packet and lodged with a direction in Form 44(a)" | `JUST FALSE` |
| `o 27 r 5 the credit to which the Accountant-General places the amount in his or her books` | "Any principal money or dividends received by the Accountant‑General in respect of securities in Court" | `JUST FALSE` |
| `o 27 r 7(6) the part is treated as withdrawn for the purpose of computing interest` | the paragraph treats "the part or parts ... last placed and remaining on deposit" as withdrawn | `JUST FALSE` |
| `o 27 r 9(1) the order states the name of every payee` | "Every order which directs funds in Court to be paid, transferred, or delivered out" | `JUST FALSE` |
| `o 27 r 9(3) the money may be paid to the payee` | "to any persons described in the order, or in a certificate of the Registrar, as co‑partners" | `JUST FALSE` |
| `o 27 r 9(3) the money may be paid to the payee` | the money "may be paid to any one or more of such co‑partners, or to the survivor of them" | `JUST FALSE` |
| `o 27 r 10(1) the funds may be paid, transferred or delivered to the legal personal representatives of the deceased person or to the survivor or survivors of them` | "on proof of the death of that person, whether (a) on or after the date of such order; or (b) in the case of payment directed to be made to a creditor as such, before the date of such order" | `JUST FALSE` |
| `o 27 r 10(2) paragraph (1) applies to the order` | paragraph (2) takes out two kinds of order and says nothing of when paragraph (1) applies | `JUST FALSE` |
| `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | "the person who, being widower, widow, child, father, mother, brother or sister of the deceased, would be entitled to take administration" | `JUST FALSE` |
| `o 27 r 10(3) the funds may be paid, transferred or delivered to the person upon a declaration` | "the person who, being widower, ..., would be entitled to take administration to his or her estate" is a relative clause that names the person, with no "only" | `JUST FALSE` |
| `o 27 r 11(3) the Court may direct that the money in Court be invested in trustee securities` | the power is for "any money in Court, other than money under Order 9, Rule 17, Order 14 or Order 33, or as security for costs"; paragraph (4) deals with Order 33 money | `JUST FALSE` |
| `o 27 r 11(3) the Court may direct that the money in Court be invested in trustee securities` | "may be invested in any of the securities in which trustees are by law permitted to invest trust money in their hands" | `JUST FALSE` |
| `o 27 r 11(4) the Court may direct that the money in Court be placed on deposit` | the paragraph is about "money in Court under Order 33" | `JUST FALSE` |
| `o 27 r 11(4) the Court may direct that the money in Court be placed on deposit` | "placed on deposit with any bank or finance company in Singapore to earn interest" | `JUST FALSE` |
| `o 27 r 11(5) the application was served on the Sheriff` | "Any application for an order under paragraph (4)" | `JUST FALSE` |
| `o 27 r 13 the account is one the list must include` | "a list of accounts not dealt with for a period of 4 years or more" is a scope limit with no "only", so the Rule does not say that other accounts are left off | `JUST FALSE` |
| `o 27 r 14(3) this Rule authorises the transfer of the funds` | the paragraph bars a transfer of a minor's funds until the minor comes of age or dies and does not say what paragraph (1) does about other funds, or about a minor's funds after that | `JUST FALSE` |
| `o 27 r 14(3) the transfer of the minor's funds under this Rule is barred` | the bar is on "any funds ... standing to the separate credit of a minor, or held in a minor's account", and the paragraph does not speak of other funds | `JUST FALSE` |
| `o 27 r 15(3) interest is payable in respect of the money` | the paragraph is about "any money paid to or deposited with the Sheriff" | `JUST FALSE` |
| `o 27 r 16 the Registry officer has acknowledged the money with a receipt` | "Money paid to or deposited with the Sheriff under these Rules or a judgment or order of a Court" | `JUST FALSE` |
| `o 27 r 20 the payment by the Sheriff is made by a method approved by the Registrar` | "All payments by the Sheriff" | `JUST FALSE` |

95 branches.

### Reading a result: FALSE and NOTHING (roc6)

In this row a **no** (`JUST FALSE`) is the text saying no in its own words.
Examples from this range: a definition that "means" a closed thing and the case is not that thing ("committal applicant" means the person who is applying for or has obtained a committal order); a flat negative (Order 24 "applies to the Supreme Court only": a District Court case is not covered; "Interest ... must not be computed on a fraction of $1"; "No interest is payable in respect of any money paid to or deposited with the Sheriff"); a condition the text introduces with "if", "unless", "except" or "where" that is not met (the Registrar may allow a search "if" the person shows a valid interest and pays the fee); and, by the rulings of 2026-11-05, an act done after the last day of a period the text fixes in its own words ("within 14 days after ..."), a "where", "when" or "upon" condition that is not met (the Court may discharge a committal order "upon" the respondent's application), and a bar that runs "until" an event (O 27 r 14(3), "until such minor comes of age or dies"), which is asked as its own question "is the transfer barred": `JUST TRUE` before the event and `JUST FALSE` after it.
**Not covered** (`NOTHING`) is anything else: a list that "includes" ("court fees" includes ...; "funds" includes money placed on deposit); a list introduced without "only" (the matters the Court is "to have regard to"; the relatives of O 27 r 10(3); the orders of O 24 r 2(1)); a term the text uses and does not define ("practicable"); a case the text does not mention; a fact that lives outside these Orders (Order 9 rule 17, Order 14, Order 21 Part 6 of Appendix 1, Order 33, the Government Proceedings Act, the Employment Claims Rules 2017); and a duty or grant limited by its own wording when the case falls outside it ("the committal applicant must forthwith ..." says what to do and not what follows if it is not done).
A caller must never turn `NOTHING` into `FALSE`.
In the seat, a question answers `JUST TRUE`, `JUST FALSE` or `NOTHING`; the answer "I am not sure" to a yes/no/not-sure input (`roc6 My answer`) becomes `NOTHING` and a rule that cannot answer without it answers `NOTHING`.

How the 181 `FALSE-kind` and 219 `NOTHING-kind` branches in layer 1 are distributed: `FALSE-kind` is 83 plain, 38 by ruling (a), 59 by ruling (b) and 1 by the "until" ruling (d); `NOTHING-kind` is 105 limited by its own wording, 90 silent, 15 points outside the text, 4 includes, 3 list not closed, 2 undefined term.
Every one of these branches carries a comment of the form `-- FALSE-kind (the text says no in its own words): "<quote>"` or `-- NOTHING-kind (<why>)` on its own line.

**Every answer in the Rules carries a caveat that no function here threads as an input**: Order 3 rule 2(1) says every requirement in the Rules is subject to the Court's power to order otherwise in the interests of justice, "even if they are expressed using imperative words such as 'must'".
It is in another part's range; a reader of any `JUST TRUE` or `JUST FALSE` here should hold it in mind.

**When the text itself lifts a duty.**
Two paragraphs in this range say that an earlier paragraph does not apply or that no affidavit need be filed: O 27 r 2(2) (L4118) and O 27 r 10(2) (L4157).
Each has a function of its own, `o 27 r 2(2) paragraph (2) says no affidavit need be filed under paragraph (1)` and `o 27 r 10(2) paragraph (1) applies to the order`, which answer `JUST TRUE` and `JUST FALSE` respectively for the lifting case.
For O 27 r 2 the question "does the duty arise" is answered by a companion function and the compliance function agrees with it: `o 27 r 2(1) the summons must be supported by an affidavit` answers `JUST FALSE` for a legacy to a minor or a person resident outside Singapore and `JUST TRUE` otherwise, and `o 27 r 2(1) the trustee has applied by summons supported by an affidavit as required` answers `JUST TRUE` for such a legacy, whether or not an affidavit was filed, provided the trustee applied by summons.

**Gate and compliance are separate functions.**
Where a paragraph both gives a power or duty and lays down what must be done to use or meet it, the function that answers "may it be done" and the function that answers "was it done as required" are separate, so that a missing step answers `NOTHING` and not a refusal the text did not give.

## Seams (roc6)

Each seam input I took, as PLAN.md section 8 names it.

| seam | where used | input name | type | answered by |
| --- | --- | --- | --- | --- |
| S-T1 (counting a period) | every period in the range: O 23 r 4, r 15, r 16; O 24 r 4, r 5, r 6; O 24A r 2, r 3; O 25 r 3, r 4, r 8; O 27 r 7(4) | `o 3 r 3 the last day for doing the act` | DATE | roc1, Order 3 Rule 3 |
| other Order | O 25 r 8(3)(a) | `o 21 the action is a non-injury motor accident action as defined in Order 21, Part 6 of Appendix 1` | MAYBE BOOLEAN | roc5, Order 21 |
| S-L1 (an exception that names another Order) | O 27 r 6(1)(a), r 11(3) | `o 9 r 17 the money is paid into Court under Order 9, Rule 17` | MAYBE BOOLEAN | roc2, Order 9 Rule 17 |
| S-L1 | O 27 r 6(1)(a), r 11(3) | `o 14 the money is paid into Court under Order 14` | MAYBE BOOLEAN | roc2, Order 14 |
| S-L1 | O 27 r 6(1)(a), r 11(3), r 11(4) | `o 33 the money is paid into Court under Order 33` | MAYBE BOOLEAN | roc7, Order 33 |
| keel definition, imported | O 26 r 5(1) | `o 1 r 3(1) a day is a non-court day` | imported function | `roc-definitions.l4` |
| keel definition, imported | O 26 r 3(7) | `o 1 r 3(1) directions are practice directions` | imported function | `roc-definitions.l4` |
| keel definition, taken as input | O 25 r 3(2) | `the Court exercises the powers in accordance with the provisions in a Civil Procedure Convention` | BOOLEAN | a caller may pass the answer of the keel's `o 1 r 3(1) an instrument is a Civil Procedure Convention` |

**This part computes none of its deadlines.**
Every period in the range is checked by comparing a date the caller gives with the last day for doing the act, which the caller takes from Order 3 Rule 3 (seam S-T1): the exclusion of non-court days for a period of 6 days or less (O 3 r 3(6), raw L328), the roll-forward of a time that expires on a non-court day (O 3 r 3(7), raw L329) and the clear days of O 3 r 3(5) (raw L327) are all that rule's work, in another part.
The period constants of this range (`Period WITH ...`) say how long the period is and which way it runs; no function here adds them to a date.
**Audit of period functions (ruling (a) of 2026-11-05).**
I checked every function that tests a time against a period, deadline or window the text states, and checked that both sides of each are tested.
(a) 42 answer `JUST TRUE` inside the period and `JUST FALSE` outside it, so no answer changed: the 29 that take the last day, 5 that compare two dates for the same day (`o 24A r 2(2)`, `o 24A r 2(12)`, `o 24A r 3(3)(a)`, `o 24A r 3(4)`, `o 24A r 3(8)`), `o 25 r 7(3)(a)`, `o 25 r 7(3)(b)`, `o 25 r 8(2)`, `o 27 r 13` (the month of January), `o 27 r 14(1)`, `o 26 r 5(1)`, `o 26 r 6`, and the yes/no twin of `o 23 r 16(10)(b)`.
(b) None answered `NOTHING` outside a stated period, so none was changed; the one date-returning function with a window, `o 23 r 16(10)(b)` ("such later date"), cannot answer `JUST FALSE`, so it keeps its `NOTHING` and has a new yes/no twin.
Deliberate `NOTHING`: 8 functions keep it as a target, a sequence, a bound on a prohibition or a scope list, each with a fork line that gives `JUST FALSE` as the other reading (the table F-TIMED, of which `o 27 r 13` is fork F-O27-2), and `o 27 r 14(3)` keeps it by ruling (d).
Inside the 42, the four functions `o 24 r 4(2)`, `o 24 r 4(6)`, `o 24 r 5(5)` and `o 24 r 6(3)` keep a `NOTHING` limb for "as soon as it is practicable", with its other reading in fork F-O24-1.

The 29 functions that take `o 3 r 3 the last day for doing the act` as an input are:

- `o 23 r 4(1) the application for the committal order is made within 14 days after permission`
- `o 23 r 4(2) there are at least 21 days between the service and the hearing date`
- `o 23 r 15(4) the Court's permission to give the non-publication direction lapses`
- `o 23 r 16(2) the application is made within 14 days after the direction is served`
- `o 23 r 16(7) the order is served within 14 days after the date of the order`
- `o 24 r 4(2) the document is served as soon as practicable and no later than 2 working days after it is filed`
- `o 24 r 4(6) the copy of each affidavit is served on every other party in time`
- `o 24 r 5(2) the application for permission is made within 3 months after the omission, judgment, order, conviction or proceedings`
- `o 24 r 5(5) the originating application, the statement and the affidavit are served on the defendant and the Attorney-General in time`
- `o 24 r 6(2) the permission lapses`
- `o 24 r 6(3) the order granting permission and the summons are served on the defendant and the Attorney-General in time`
- `o 24A r 2(1) the application for PACC permission is fixed for hearing within 21 days after it is filed`
- `o 24A r 2(8) the affidavit of the newly appointed counsel is filed within 3 days after the appointment`
- `o 24A r 2(10)(a) the respondent's written submissions are filed within 3 days after the application is filed and served on the respondent`
- `o 24A r 2(10)(b)(i) the respondent's written submissions are filed within 3 days after the affidavit or affidavits are filed and served`
- `o 24A r 2(10)(b)(ii) the respondent's written submissions are filed within 3 days after each affidavit is filed and served`
- `o 24A r 3(1) the PACC application is made within 3 days after permission is granted`
- `o 24A r 3(2) the PACC application is fixed for hearing within 21 days after it is made`
- `o 24A r 3(3)(b) the applicant's written submissions are filed within 3 days after the PACC application is made`
- `o 24A r 3(5) the respondent's written submissions in response are filed within 3 days after the application is made and served`
- `o 25 r 3(3)(a) the request for refund of hearing fees is made in writing within one month`
- `o 25 r 3(3)(b) the request for refund of fees for unused documents is made in writing within the time in Rule 4(2)`
- `o 25 r 3(3)(c) the request for refund of fees for Court ADR services is made in writing within the time in Rule 8(4)`
- `o 25 r 3(3)(d) the request for refund in any other case is made in writing within one month after the reason for the refund arose`
- `o 25 r 3(4) the Court must refund the whole of the hearing fees paid`
- `o 25 r 3(5) the party may apply by letter to a Judge to review the decision within 14 days`
- `o 25 r 4(2)(b) the application for refund is made within 3 months after the date of payment`
- `o 25 r 8(4) the request for refund of the Court ADR fee is made in writing to the Registrar within one month`
- `o 27 r 7(4) the interest for the year is placed to the credit on or before 15 days after the year ends`

**What other parts ask of this range, and the function that answers.**

| asked by | asks | answered by | type |
| --- | --- | --- | --- |
| keel, O 1 r 3(1) "court fees" | whether a payment is within court fees | `o 25 r 1 the payment is within court fees` (takes `o 25 r 1 kind of payment`) | MAYBE BOOLEAN |
| keel, O 1 r 3(1) "practice directions" | whether directions are practice directions | `o 26 r 2 the directions are issued under Order 26, Rule 2` | MAYBE BOOLEAN |
| S-V1, Fourth Schedule fees (roc12) | the value of the claim for court fees | `o 25 r 2 the value of the claim` (answers 1000000 for "up to $1 million": assumed, not ruled) | NUMBER |
| S-V2, Fourth Schedule hearing fees (roc12) | no hearing fee; hearing fee payable in winding up; exemption | `o 25 r 5 no hearing fee is payable`, `o 25 r 6 hearing fees are payable`, `o 25 r 7(3)(a) no fee is payable by any party in the cause or matter` | MAYBE BOOLEAN |
| roc1, O 4 | O 24A whole, r 4 | `o 24A r 1(3) ...`, `o 24A r 4 the applicant must file and serve a notice of appointment` and the other `o 24A` functions | MAYBE BOOLEAN |
| roc7, roc9, roc10, roc12 | O 26 r 3 (records and search) | `o 26 r 3(4) the Registrar may allow the person to search for, inspect and take a copy of the document`, `o 26 r 3(7) the document filed in Court is typewritten, printed and complies with the practice directions` | MAYBE BOOLEAN |
| roc7, O 33 | O 27 r 15 | `o 27 r 15(1)`, `o 27 r 15(2)`, `o 27 r 15(3)` | MAYBE BOOLEAN |
| roc11, O 59 | O 23 whole | the `o 23 r ...` functions | MAYBE BOOLEAN |
| roc12, Fourth Schedule | O 23 r 11 | `o 23 r 11(1) the committal order is in the form required` | MAYBE BOOLEAN |

**S-L2 (an override that switches another provision off).**
PLAN.md section 8 lists O 59 r 11 (roc11) as an override of a provision in another part; none of the five overrides it names is a provision of this range as the overridden one, so this range threads no input for an override.
That sentence rests on the list in PLAN.md and not on a reading of Order 59, which is outside this range.

**Seams I found that the plan lacks.**

- O 23 r 12(4) takes the hearing fees "prescribed in the Employment Claims Rules 2017 (G.N. No. S 104/2017)", which is outside the sources: `o 23 r 12(4) the instrument that prescribes the hearing fees in a tribunal` names it and does not look it up.
- O 23 r 1, r 12(5), r 13(5) and r 14(3) define their terms by reference to the Administration of Justice (Protection) Act 2016, the State Courts Act, the Employment Claims Act 2016, the Small Claims Tribunals Act and the Community Disputes Resolution Act 2015, none of which is among the sources; each such definition answers `NOTHING` when the outside fact is absent.
- O 24 r 6(8) is "Subject to the Government Proceedings Act"; O 26 r 4(1) cites section 48 of the Conveyancing and Law of Property Act; O 24A r 1(2) takes its expressions from section 60F of the Supreme Court of Judicature Act 1969. All three are inputs or `NOTHING` branches, not looked up.

## Dependencies

I copied nothing from `inputs/DEPENDENCIES/` and took no Commons module.
The provisions of this range that count a period take the answer of Order 3 Rule 3 as an input (`o 3 r 3 the last day for doing the act`); Order 3 rule 3 displaces the Interpretation Act's counting for these Rules, as the brief says, so no Interpretation Act module is needed.
The only module imported besides the core is the keel's `roc-definitions.l4` (O 26), which is in the folder.
No dependency is listed for `encoding.json`; that file is not mine to write.

## Unstable dialect

I looked at time (the effect dates of O 23 r 16(9) and (10), the calendar-month interest of O 27 r 7, every period in the range), at rule versions (the amendment marks `[S 206/2022 wef 01/04/2022]` at O 23 r 7(5) and (6) and `[S 535/2024 wef 28/06/2024]` at O 24A, which are text annotations on provisions already in force at 5 November 2026) and at workarounds (no years unit, no reference to a rule: NEEDS-CORE.md), and found no shape that the unstable dialect would express better than the main files do: the dates are `Date` values with `Month` and `Day`, which main reads and which 1.6.108 and 1.6.109 agree on, so I wrote no second encoding.

## Findings

### What the text turns out to say

1. The text is a converter rendering. The range carries 262 lines with a no-break space, 56 lines with a non-breaking hyphen, and lettered paragraphs written as `( a )` on lines of their own. 7 lines carry an amendment mark inside the paragraph line (`[S 206/2022 wef 01/04/2022]` and `[S 535/2024 wef 28/06/2024]`, at lines 3643, 3663, 3829, 3835, 3910, 3921, 3923); the marks are not operative text and sit inside the rows of the paragraphs they follow. Any search of this file for "Order 25" or "non-court" with an ordinary space or hyphen misses lines (the keel found the same).
2. Order 23 rules 12, 13 and 14 are near copies of one another for three tribunals, and they differ in the fee paragraphs: rule 12(3) and (4) apply District Court court fees and the hearing fees "prescribed in the Employment Claims Rules 2017"; rule 13(3) and (4) apply the Magistrate's Court court fees and hearing fees; rule 14 has no fee paragraph. Rule 12's heading says Employment Claims Tribunals, rule 13's Small Claims Tribunals and rule 14's Community Disputes Resolution Tribunals, and each defines "tribunal" in terms of an Act outside the sources. Each is encoded on its own (E1, option C).
3. Order 24 rule 4(2) lists among the documents to be served "the order of the Court mentioned in Rule 3(6)(b)", but rule 3(6)(b) is the Court's direction that a summons be issued; the Form 43 order is in rule 3(6)(a). The function takes a plain "was served" input for the document and does not decide which of the two the text means.
4. Order 24A states the 35-page limit three times (r 2(3), r 2(11) and r 3(6)) with "unless the Court of Appeal otherwise allows", and states the Court's power to allow more twice more (r 2(13) and r 3(7)) "in special circumstances". The "otherwise allows" form has no special-circumstances condition, and the text does not say whether r 2(13) narrows r 2(3). Each is encoded on its own: the page-limit functions take a BOOLEAN "the Court of Appeal allows more", and `o 24A r 2(13)` and `o 24A r 3(7)` take "there are special circumstances".
5. Order 24A rule 2(8) refers to "paragraph (4)(a)(i) to (xi)", and paragraph (4)(a) has sub-paragraphs (i) to (xi), with (vii) and (viii) each split into (A) and (B): thirteen items, which `o 24A r 2(4)(a) all the matters` lists, and nine in (4)(b) (`o 24A r 2(4)(b) all the matters`). The cross-reference matches the rendering; I checked it because a cross-reference to a range that does not exist would have been a defect in the text.
6. Order 25 rule 2(2)(d) deems a claim of none of the listed kinds "to have a value of up to $1 million", which is a band and not a number. PLAN.md seam S-V1 asks for a number; the function answers 1000000 and says so (fork F-O25-1).
7. Order 25 rule 3(3) is a router: paragraph (a) fixes one month for hearing fees, (b) points to rule 4(2) (3 months), (c) points to rule 8(4) (one month after the earlier of two dates), and (d) is a catch-all of one month after the reason arose. Three different periods are reached through one request, and a caller must know which kind of refund is being asked for.
8. Order 25 rule 4(4) says "the fee paid for the request is not refundable". The Rules in this range set no fee for a request; the fee, if any, is in the Fourth Schedule (another part). The amount is not looked up: `o 25 r 4(4) the fee paid for the request is not refundable` answers `JUST TRUE` when the application was not approved and `JUST FALSE` when it was (a "where" condition that fails, ruling (b)).
9. Order 27 rule 7(4) reads oddly in the text: "must, on or before 15 days thereafter following, be placed by the Accountant-General to the credit to which such money is standing". It is read as: on or before the 15th day after 31 December, and the 15 days are counted by Order 3 rule 3 (input).
10. Order 27 rule 1 defines "order" as "an order or judgment of a Court, whether made in Court or in chambers" for that Order only; the PLAN lists it among the Orders that redefine a core word. Rule 1 "funds" "includes money placed on deposit", an open list.
11. Order 26 rule 1(1) to (3) say which office directs the departments and functions of the Registry, to whom the Registrar reports, and which office appoints a Chief Executive and Assistant Chief Executives and receives their reports: each has a function that answers the office (`o 26 r 1(1) the office that directs the departments and functions of the Registry`, `o 26 r 1(2) the office to whom the Registrar must report and be responsible for the proper administration and functions of the Registry`, `o 26 r 1(3) the office may appoint a Chief Executive and one or more Assistant Chief Executives`, `o 26 r 1(3) the office to whom the Chief Executive and the Assistant Chief Executives must report and be responsible for the proper discharge of the functions they manage`).
12. Silent in the text, no function: the fees for committal proceedings before a Community Disputes Resolution Tribunal (Order 23 rule 14 has paragraphs (1) to (3) only: the application of Rules 1 to 11, the references, the definitions; rules 12 and 13 have fee paragraphs and rule 14 has none), and the Registry's opening hours (Order 26 rule 5(2): "as directed by the Chief Justice or the Presiding Judge of the State Courts, as the case may be"; the text states no hours, so the paragraph is inert, reason 2).
13. Where the text names the bearer or the place of a duty, a function answers it, so that a caller can ask who or where: `o 23 r 6(3)(b) the person who must send the file, documents, exhibits and certified copy of the notes of evidence to the Registrar of the Supreme Court`, `o 23 r 6(3)(c) the person who must give notice of the transfer to every party to the case`, `o 23 r 15(5) the person who must file the affidavit of service of the non-publication direction`, `o 24 r 4(10) the person who must inform the defendant or the appropriate person or entity`, `o 26 r 4(1) the Registry in which the document creating a power of attorney may be deposited`, `o 27 r 3 the person who must give notice of the lodgment` (with `o 27 r 3 the persons to whom the notice must be given` and `o 27 r 3 when the notice must be given`), `o 27 r 11(1) the party who must lodge a copy of the order with the Accountant-General` and `o 27 r 20 the office that approves the method of payment by the Sheriff`.
14. Order 26 rule 3(8) joins (a) and (b) with "; and": `o 26 r 3(8) the Registrar may authorise a person to provide the service` answers `JUST TRUE` for a service that does both and `NOTHING` otherwise.
15. Order 23 rule 16(7)(a) is read in three parts: whether the order was served on the person to whom the direction applies, whether that person is the applicant ("unless the person is the applicant"), and whether it was served on every other person the Court ordered to be served: `o 23 r 16(7) the order has been served on those required` takes the three.
16. Order 24A rule 2(4)(a) and (b): the matters an affidavit states are a list of choices, and each list of choices ends in `o 24A r 2(4)(a) some other matter` or `o 24A r 2(4)(b) some other matter`, so that a caller can record that the affidavit also states something the paragraph does not list; that choice counts toward none of the required matters, and the function does not refuse the affidavit for stating it.
17. Names: every top-level name (function, type and constructor) in the six layer-1 files starts with `o 23` to `o 27` and the provision it implements (`o 23 r 3(1) ...`), checked by a script over the four kinds of top-level line; the types `o N party` and `o N act` that serve several regulative rules of one Order carry the Order's label only. The seat's own names start with `roc6`, and its questions are named "Under Order N, rule M, ...".
18. Where the text says a thing "must" be done and names no time and no consequence, the encoding does not invent one (Order 27 rules 3 and 17; Order 23 rule 4(1) service; Order 26 rule 3(7)). The seat asks whether it was done and answers `JUST TRUE` or `NOTHING`.

### What the main binary does not accept

Measured on 1.6.109 by a one-file probe each (probes in `work/probe`, not shipped); the 1.6.108 column of `check.sh` reads all the shipped files the same way.

- **`MIN` does not exist** (`check/unknown-identifier`). The smaller of two numbers is written with an `IF`.
- **`MODULO` rejects a fractional number** (`eval/not-an-integer`: "Expected an Integer but got the fractional number"). Amounts with cents are compared and subtracted and never reduced with `MODULO`.
- **`Month` and `Year` return DATEs, not numbers**: `Month (Date 15 3 2026)` equals `Date 1 3 2026` and `Year (Date 15 3 2026)` equals `Date 1 1 2026` (both assertions passed). Calendar-month arithmetic in O 27 r 7(3) is therefore written with `Date`, `Day` and `Month` (`Month (Date ((Day (Month d)) PLUS 32))` is the first of the next month).
- **Equality on a DEONTIC value is not supported** (`eval/unsupported-equality`: "Trying to check equality on types that do not support it"), so a regulative rule cannot be the subject of an `#ASSERT`. The 23 `#TRACE` directives in the tests print an outcome at information level and are not assertions: `check.sh` counts none of them. I compared the trace outcomes of the five test files that hold traces between 1.6.109 and 1.6.108 by running both and diffing the output: no line differs. That shows the two builds agree, not that either is right, so I also paired each of the 23 traces with the `-- expected:` comment written beside it before the run (by a script that matches each trace to its result block by source line): 21 print `FULFILLED` or `BREACH` as written, and the other 2 (`o 24 r 2(2)`, a prohibition nobody breaks, and `o 25 r 8(1)`, a duty with no day fixed, each followed by `(WAITUNTIL n)`) print the rule itself with no breach, as the comments say. Every regulative duty is also encoded as a decision function over the facts, and the function is what the assertions test.
- **A vertical `LIST` block of names without commas is read as an application** (`check/not-a-function`: "You are trying to apply `kind two` ... of type Kind"), whereas the same block of strings without commas is accepted. Every vertical list of names in these files has a comma at the end of each line but the last.
- **A `#TRACE` event list with several events on one line separated by commas is a parse error** (`parse/unexpected-comma`); one event per line is accepted (every trace in the tests is written that way).
- **`NOT x AND y` reads as `NOT (x AND y)`**: with x and y both `FALSE` it is `TRUE`, and `#ASSERT ... EQUALS FALSE` on it fails. Every `NOT` in these files is parenthesised, `((NOT x) AND y)`, as the brief requires.
- **No years unit**: `Time unit` in the core has none (NEEDS-CORE.md), and the core has no type for a reference to a rule.
- **No `REFUSE`, no `#ASSERT REFUSED`, no `BECAUSE` except `LEST BREACH BECAUSE`, no sets, no `YMD`, no `@lang`, no `TYPICALLY` on a field, no opaque `DECLARE`**: from the brief; the files use none (`grep` finds no `REFUSE` or `#CHECK` in any file of this row), and both main builds read every file the same way.

### What the second pass changed

An independent test pass wrote its own expected answers from the text alone and ran them against this encoding; the readings it disagreed with, and the rulings of 2026-11-05, produced the changes below.
They are listed so that a later editor does not undo one.

- **Stay on a Mandatory Order (O 24 r 5(9)(a)).** `o 24 r 5(9)(a) the Court may also order a stay of the proceedings in question until the application for the Order is determined` answers `JUST FALSE` for a Mandatory Order, both when permission is not granted and when it is, because paragraph (9)(a) speaks of a Prohibiting Order or a Quashing Order only.
- **Court ADR fee (O 25 r 8).** An ordinary contract claim in a District Court now answers `JUST TRUE` to `o 25 r 8(1) the Court ADR fee is payable by the party` (fork F-O25-2); `o 25 r 8(3) no Court ADR fee is payable in the action` answers `JUST FALSE` for an action outside the four; the new `o 25 r 8(1) the total Court ADR fee payable by the parties in a District Court case` gives 750 for three parties; the seat question for O 25 r 8(1) has cases for the three results.
- **Open court and private hearing (O 23 r 7(1)).** `o 23 r 7(1) the Court may hear the application in private` answers `JUST FALSE` outside cases (a) to (e), and `o 23 r 7(1) the Court must hear the application in open court` is rewritten to agree with it on every row (fork F-O23-2).
- **Account not dealt with for 4 years (O 27 r 13).** Left as it was, and recorded in fork F-O27-2 with the reviewer's expectation.
- **Affidavit under O 27 r 2.** The function that answered `paragraph (2) says no affidavit need be filed` is now named for what it answers (`o 27 r 2(2) paragraph (2) says no affidavit need be filed under paragraph (1)`), and a new function `o 27 r 2(1) the summons must be supported by an affidavit` asks the positive question of paragraph (1).
- **Seat labels for O 23 r 3(3).** The questions about the affidavit supporting the application for permission now say what lines 3569 to 3574 say: "Under Order 23, rule 3(3), does the affidavit supporting my application for permission set out what the Rule requires?"
- **Sweep of "if", "where", "when", "upon" and the periods.** Every site in the six layer-1 files was read for the rulings of 2026-11-05: 38 branches now carry ruling (a) (a period the text fixes), 59 carry ruling (b) (a "where", "when" or "upon" not met) and ruling (d) (an "until" bar) is carried by 1 branch. The sites that are left at `NOTHING` on purpose are the F-MUST table, the leave-as-is forks (F-O24-2, F-O26-1, F-O27-2 for rule 13, F-O27-4), and F-UNSURE.
- **Audit of period functions.** No answer changed; one yes/no twin added (`o 23 r 16(10)(b) the date the Court specified is a later date than the date of service`, three tests); fork F-TIMED added; fork F-O24-1 gained its other reading for the "as soon as practicable" limb. The counts are under Seams.
- **Gaps filled.** The bearer and place functions listed in the findings above; `o 27 r 14(2) the Government must pay the claimant` beside the number (no interest: the paragraph gives none); `o 27 r 14(3) the transfer of the minor's funds under this Rule is barred`; `o 23 r 16(7) the order has been served on those required` now takes three inputs; Order 26 rule 3(8) joins (a) and (b) with "and".

### What `check.sh` prints, and the baseline

Baseline: the keel's `KEEL-NOTES.md` records 3 modules and 278 assertions satisfied (`roc-core.l4`, `roc-definitions.l4` and `roc-definitions-tests.l4`); the folder I was given held `roc-core.l4` and `roc-definitions.l4` only, both at 0 assertions, so the figures before my files were 0 errors, 0 satisfied, 0 failed, 0 refused over 2 modules.
With my 14 files added: 16 modules, 0 errors, 1274 assertions satisfied, 0 failed, 0 refused, the same four counts on 1.6.108 for every module.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc6-cases-seat.l4                             0       103       0        0         0 |      0       103       0        0  same
roc6-order-23.l4                               0         0       0        0         0 |      0         0       0        0  same
roc6-order-24.l4                               0         0       0        0         0 |      0         0       0        0  same
roc6-order-24a.l4                              0         0       0        0         0 |      0         0       0        0  same
roc6-order-25.l4                               0         0       0        0         0 |      0         0       0        0  same
roc6-order-26.l4                               0         0       0        0         0 |      0         0       0        0  same
roc6-order-27.l4                               0         0       0        0         0 |      0         0       0        0  same
roc6-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc6-tests-order-23.l4                         0       302       0        0         0 |      0       302       0        0  same
roc6-tests-order-24.l4                         0       166       0        0         0 |      0       166       0        0  same
roc6-tests-order-24a.l4                        0       142       0        0         0 |      0       142       0        0  same
roc6-tests-order-25.l4                         0       210       0        0         0 |      0       210       0        0  same
roc6-tests-order-26.l4                         0        78       0        0         0 |      0        78       0        0  same
roc6-tests-order-27.l4                         0       273       0        0         0 |      0       273       0        0  same
TOTAL (16 modules)                             0      1274       0        0           |      0      1274       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

The command was `L4=<1.6.109> L4_MAIN=<1.6.108> ./check.sh` with `JL4_LIBRARY_PATH` unset.

Other checks, run in the encoding folder:

```
srcrefs.py check --refs   : srcrefs check: 600 src: lines, 233 runs, 324 locators, 0 problems
srcrefs.py check --strict : srcrefs check: 600 src: lines, 233 runs, 324 locators, 0 problems
```

`l4 check` on each of the 14 `roc6-*.l4` files prints `Check succeeded.`, and the output of each holds neither `is at the end of the file` nor `follows code on its line` (counted by `grep -c`: 0 for every file).

