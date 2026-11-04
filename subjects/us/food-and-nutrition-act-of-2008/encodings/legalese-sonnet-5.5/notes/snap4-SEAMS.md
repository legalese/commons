# SEAMS (snap4)

A seam is a provision in one place whose answer another provision needs (PLAN.md rule 9).
Inputs are named for the answering section and typed `MAYBE BOOLEAN` unless they are a number, a date, or a plain `BOOLEAN` where PLAN.md says so.
Two lists follow: **ASKS** (the inputs snap4 takes from other sections) and **ANSWERS** (the functions snap4 offers to other sections).
Generated from the `GIVEN` lists of the modules by `work/tools/seams.py` on 2026-11-04, then read.

## ASKS

### Inputs named for the answering section

| input name | type | answering section | used by | file |
| --- | --- | --- | --- | --- |
| `s 2012(s) the body is a State agency` | MAYBE BOOLEAN | s 2012(s) | `s 2020(a)(2) the responsibility of the State agency is affected by the basis of operation` | snap4-s2020-a-d.l4 |
| `s 2012(s) the body is a State agency` | MAYBE BOOLEAN | s 2012(s) | `s 2020(d) the State agency must submit a plan of operation for approval` | snap4-s2020-a-d.l4 |
| `s 2012(l) the individual is a homeless individual` | MAYBE BOOLEAN | s 2012(l) | `s 2020(e)(2)(B)(vi) the State agency must provide a method of certifying and issuing benefits to the individual` | snap4-s2020-e-1.l4 |
| `s 2012(s) the body is a State agency` | MAYBE BOOLEAN | s 2012(s) | `s 2020(e)(17) the State agency may request and exchange information for income and eligibility verification` | snap4-s2020-e-2.l4 |
| `s 2012(s) the body is a State agency` | MAYBE BOOLEAN | s 2012(s) | `s 2020(e)(17) the State agency may request and use additional information from the agency administering State unemployment compensation laws` | snap4-s2020-e-2.l4 |
| `s 2012(k) the establishment is one described in paragraphs (3), (4) and (9) of section 2012(k)` | BOOLEAN | s 2012(k) | `s 2020(e)(25)(A) the State plan of operation must include the item` | snap4-s2020-e-2.l4 |
| `s 2012(j) the answers, member by member, to whether each member is an elderly or disabled member` | LIST OF MAYBE BOOLEAN | s 2012(j) | `s 2020(w) the State agency must advise the member regarding available employment and training services` | snap4-s2020-o-x.l4 |
| `s 2015(d)(2) the member is exempt` | MAYBE BOOLEAN | s 2015(d)(2) | `s 2020(w) the State agency must advise the member regarding available employment and training services` | snap4-s2020-o-x.l4 |
| `s 2018 the seller is an approved retail food store or wholesale food concern` | MAYBE BOOLEAN | s 2018 | `s 2021(a)(1) the seller may be subjected to the sanction` | snap4-s2021.l4 |
| `s 2036d(b)(1)(D) the Secretary has determined that the private entity is an eligible entity` | MAYBE BOOLEAN | none (the Act hands it to the Secretary) | `s 2036d(b)(1) the entity is an eligible entity` | snap4-s2036b-d.l4 |


Notes on the rows:
- `s 2012(s) the body is a State agency`, `s 2012(k) ... paragraphs (3), (4) and (9) of section 2012(k)`, `s 2012(l) ...` are the names PLAN.md section 6 group A gives for snap4, and the types it gives.
- **Deviation:** `s 2012(j) the answers, member by member, ...` is a `LIST OF MAYBE BOOLEAN` and PLAN.md names `s 2012(j) the member is an elderly or disabled member` (`MAYBE BOOLEAN`, one member).
  `s 2020(w)` asks about every member of a household at once, so the input is the list of the per-member answers; the lead wires it by mapping the keel function over the household's members.
- `s 2015(d)(2) the member is exempt` is a group C seam (snap4 asks snap2); PLAN.md does not name it.
  It is typed `MAYBE BOOLEAN`, one value for the member the rule is about.
- `s 2018 the seller is an approved retail food store or wholesale food concern` is a group C seam (snap4 asks snap1, two mentions in PLAN.md).
  "Wholesale food concern" has no definition in section 2012 (PLAN.md difficulty 2): the caller states whether the seller is one, and whether it is approved.
- `s 2036d(b)(1)(D) the Secretary has determined ...` has no answering section: "a private entity, as determined by the Secretary" hands the determination to the Secretary, so the caller supplies it, and `NOTHING` means no determination was supplied (PLAN.md group B, last row).
- Every seam input passes `NOTHING` through as `NOTHING` (points outside the text); none is turned into `FALSE`.

### Borrowed terms and facts taken as plain `BOOLEAN` inputs

Where the text borrows a fact from another section ("eligible to receive benefits under section 2015(f)", "a program carried out under the statutes specified in section 2014(a)") the module asks it as a plain yes/no input worded as the fact (Guide section 4: borrowed terms are asked as facts), not as a function of the other section.
They are listed so the lead can wire any of them to an answering function at the merge.

| input name (a plain fact) | type | the section it points at | used by | file |
| --- | --- | --- | --- | --- |
| `the certification says that all members of the household are citizens or are aliens eligible to receive benefits under section 2015(f)` | BOOLEAN | 2015(f) | `s 2020(e)(2)(B)(v) the certification required of the applicant household is complete` | snap4-s2020-e-1.l4 |
| `the requirement is additional to those in sections 2014 and 2015` | BOOLEAN | 2014 | `s 2020(e)(5) the State agency may impose the requirement in determining eligibility` | snap4-s2020-e-1.l4 |
| `the matter is one of the plans of the State agency for carrying out employment and training programs under section 2015(d)(4)` | BOOLEAN | 2015(d)(4) | `s 2020(e)(19) the State plan of operation must provide for the matter` | snap4-s2020-e-2.l4 |
| `the matter is a guideline the State agency uses in carrying out section 2015(i)` | BOOLEAN | 2015(i) | `s 2020(e)(22) the State plan of operation must provide for the guideline` | snap4-s2020-e-2.l4 |
| `the State elects to carry out a simplified supplemental nutrition assistance program under section 2035` | BOOLEAN | 2035 | `s 2020(e)(23) the State plan of operation must include the item` | snap4-s2020-e-2.l4 |
| `the information, if accurate, would have been required to be reported by the household based on the reporting requirements assigned under section 2015(c)` | BOOLEAN | 2015(c) | `s 2020(e)(26) the State agency may pursue clarification and verification of the information` | snap4-s2020-e-2.l4 |
| `the Secretary determines that in the administration of the supplemental nutrition assistance program there is a failure by a State agency without good cause to comply with the chapter, its regulations, the State plan of operation, the State plan for automated data processing, or the requirements under section 2032` | MAYBE BOOLEAN | 2032 | `s 2020(g) the Secretary must immediately inform the State agency of the failure and allow a specified period for its correction` | snap4-s2020-f-n.l4 |
| `the denial or termination is solely on the basis that the application was denied or the benefits were terminated under a program carried out under the statutes specified in the second sentence of section 2014(a)` | BOOLEAN | 2014(a) | `s 2020(i)(2) the State agency may deny the application or terminate the benefits` | snap4-s2020-f-n.l4 |
| `the verification is to assure that an individual does not receive both benefits and benefits or payments referred to in section 2015(g), or both benefits and assistance provided in lieu of benefits under section 2026(b)(1)` | BOOLEAN | 2015(g), 2026(b)(1) | `s 2020(n) the Secretary must require the State agency to conduct the verification` | snap4-s2020-f-n.l4 |
| `the household loses eligibility under section 2015` | BOOLEAN | 2015 | `s 2020(s)(5) the household is eligible for transitional benefits` | snap4-s2020-o-x.l4 |
| `the civil penalty imposed under paragraph (1) has become final under section 2023(a)` | BOOLEAN | 2023(a) | `s 2021(e)(2) the Secretary may request the Attorney General to institute a civil action to collect the penalty` | snap4-s2021.l4 |
| `the use is to administer the supplemental nutrition assistance program and enforce regulations promulgated under section 2013(c)` | BOOLEAN | 2013(c) | `s 2036b(b)(2) the Secretary must use an appropriate amount of the funds` | snap4-s2036b-d.l4 |

### Pointed at, no input taken

Section 2021 points at section 2023 (review, hearing: 2021(c)(2), (d)(5), (e)(2), (g)(2)(C)) and at section 2024(g) (forfeiture, 2021(h)(2)(B)(i)).
snap4 states only what its own sentence says (that review or a hearing is available, that benefits may be forfeited); what review or forfeiture decides is snap3's, and no input is taken.
Section 2036b(b)(2) points at section 2013(c); 2032(a)(1) at section 2025(a) and (g); 2020 at sections 2014, 2015, 2022, 2023, 2025, 2026, 2027 and 2035 in many places, each asked as a plain fact where a rule turns on it (the table above) and otherwise left as a citation.

## ANSWERS

### Group B: fields the keel left waiting for snap4

| function | type | section | feeds |
| --- | --- | --- | --- |
| `s 2020(s)(2) the day falls within the transitional benefits period` (takes the day cash assistance is terminated and the day) | `BOOLEAN` | s 2020(s)(2), line 1610 | the keel's field "the period or the contact falls within a transitional benefit period under section 2020(s)" in `s 2012(f)`; the last day is counted (fork F-1) |
| `s 2020(d) the Secretary has determined that the tribal organization is capable of conducting the program` (takes the Secretary's determination, a `MAYBE BOOLEAN`, and the four factors) | `MAYBE BOOLEAN` | s 2020(d), line 1462 | the keel's field in `s 2012(s)` agency ("the Secretary determines that the tribal organization is capable ... section 2013(b) ... section 2020(d)"); the determination is the caller's, `NOTHING` means none was supplied |

### Definitions the Act gives inside snap4's ranges

| function | type | section |
| --- | --- | --- |
| `s 2020(m) the person is a fee agent` | `MAYBE BOOLEAN` | s 2020(m), line 1583 |
| `s 2020(x)(1) the indication is an indication of multiple issuance` | `MAYBE BOOLEAN` | s 2020(x)(1) |
| `s 2036d(b)(1) the entity is an eligible entity` | `MAYBE BOOLEAN` | s 2036d(b)(1), lines 3300-3305 |
| `s 2036d(b)(2) the body is a public agency` | `MAYBE BOOLEAN` | s 2036d(b)(2), line 3306 |

### Group C: functions other parts are likely to ask

PLAN.md section 6 group C says which sections mention snap4's sections (counted from its table, 2026-11-04): section 2020 is mentioned by sections 2014, 2015, 2016a, 2017, 2018, 2025, 2026, 2027, 2031, 2035 and 2036a; section 2021 by sections 2018 and 2023; sections 2032, 2036b, 2036c and 2036d by none.
As PLAN.md advises for a section many parts ask, every subsection of section 2020 and section 2021 has its own small function, named `s 2020(x) ...` or `s 2021(x) ...` for the subsection it implements; the Coverage table in NOTES.md lists each by name.
The ones most likely wanted:

| function | type | section |
| --- | --- | --- |
| `s 2020(e)(3) the household is entitled to certification and a retroactive allotment within thirty days of filing` | `MAYBE BOOLEAN` | s 2020(e)(3) |
| `s 2020(e)(9)(A)` and `(B)` `... entitled to benefits no later than 7 days after the date of application` | `MAYBE BOOLEAN` | s 2020(e)(9) |
| `s 2020(e)(10) the household is entitled to a fair hearing and a prompt determination thereafter` | `MAYBE BOOLEAN` | s 2020(e)(10) |
| `s 2020(e)(11) the period must be restored to the household in the form of benefits` | `MAYBE BOOLEAN` | s 2020(e)(11) |
| `s 2020(s)(3) the amount of transitional benefits` | `NUMBER` | s 2020(s)(3) |
| `s 2021(a)(1) the seller may be subjected to the sanction` | `MAYBE BOOLEAN` | s 2021(a)(1) |
| `s 2021(b) the period imposed is allowed` | `MAYBE BOOLEAN` | s 2021(b) |
| `s 2021(b)(3)(B)`, `(C)` `the Secretary may impose a civil penalty in lieu of permanent disqualification` | `MAYBE BOOLEAN` | s 2021(b)(3) |
| `s 2021(c)(2) the action is subject to review as provided in section 2023` | `MAYBE BOOLEAN` | s 2021(c)(2) |
| `s 2021(d)(1)`, `(d)(2)` `the Secretary may require a collateral bond or irrevocable letter of credit ...` | `MAYBE BOOLEAN` | s 2021(d) |
| `s 2032(a)(1)(A)` `the review was completed by the deadline` | `BOOLEAN` | s 2032(a)(1)(A) |
