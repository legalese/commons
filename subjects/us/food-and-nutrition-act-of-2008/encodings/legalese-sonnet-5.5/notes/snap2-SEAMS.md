# SEAMS (snap2)

Ranges: s 2015, s 2027, s 2029 (s 2030 is repealed in the text). Two lists, as PLAN.md rule 9 asks: ASKS (inputs this part takes from elsewhere) and ANSWERS (functions this part gives).
Generated 2026-11-04 from the layer-1 modules by `work/tools/seams.py`; names are exact.

## ASKS (input name, type, answering section)

An input is listed when its name begins with a section label (`s 2012(j) ...`). Type is the type of the input in the layer-1 function. "Answered in this part" means a function of the same part gives it, so no other part need answer.

| input name | type | answering section | answered in this part by | used by (first) |
| --- | --- | --- | --- | --- |
| `s 2014 the standards of eligibility are met` | MAYBE BOOLEAN | s 2014 | no (another part answers) | `s 2015(a) the household or individual is eligible to participate` |
| `s 2020(s) the household is receiving transitional benefits during the transitional benefits period` | BOOLEAN | s 2020 | no (another part answers) | `s 2015(c) the household is ineligible for refusing to provide necessary information` |
| `s 2012(l) all members of the household are homeless individuals` | MAYBE BOOLEAN | s 2012 | no (another part answers) | `s 2015(c)(1)(A) the State agency may require periodic reports for the period` |
| `s 2012(j) all adult members of the household are elderly or disabled members` | MAYBE BOOLEAN | s 2012 | no (another part answers) | `s 2015(c)(1)(A) the State agency may require periodic reports for the period` |
| `s 2012(n) the household resides on a reservation` | MAYBE BOOLEAN | s 2012 | no (another part answers) | `s 2015(c)(1)(C) the State agency may require monthly periodic reporting by households on a reservation` |
| `s 2014(c)(2) the income standard of eligibility in dollars` | NUMBER | s 2014 | no (another part answers) | `s 2015(c)(1)(D)(ii) the household must report in the manner the Secretary prescribes` |
| `s 2012(h) the program is a drug addiction or alcoholic treatment and rehabilitation program` | MAYBE BOOLEAN | s 2012 | no (another part answers) | `s 2015(d)(2)(D) the person is exempt because a regular participant in a treatment and rehabilitation program` |
| `s 2015(d)(2) the person is exempt from the requirements of paragraph (1)` | MAYBE BOOLEAN | s 2015 | yes: `s 2015(d)(2) the person is exempt from the requirements of paragraph (1)` | `s 2015(o)(3) paragraph (2) does not apply to the individual` |
| `s 2015(o)(7)(A) the State is a noncontiguous State` | MAYBE BOOLEAN | s 2015 | yes: `s 2015(o)(7)(A) the place is a noncontiguous State` | `s 2015(o)(7)(B) the Secretary may exempt individuals in the noncontiguous State from paragraph (2)` |
| `s 2015(k)(1) the individual is ineligible while fleeing or violating probation or parole` | MAYBE BOOLEAN | s 2015 | yes: `s 2015(k)(1) the individual is ineligible while fleeing or violating probation or parole` | `s 2015(r)(1) the individual is ineligible for benefits` |
| `s 2014 the household meets the allowable financial resources and income eligibility requirements under subsections (c), (d), (e), (f), (g), (i), (k), (l), (m), and (n)` | MAYBE BOOLEAN | s 2014 | no (another part answers) | `s 2015(s)(2) the household remains ineligible for participation` |
| `s 2014 the household met the allowable financial resources and income eligibility requirements under subsections (c), (d), (e), (f), (g), (i), (k), (l), (m), and (n) between the receipt and the date asked about` | MAYBE BOOLEAN | s 2014 | no (another part answers) | `s 2015(s) the household is ineligible on the date` |
| `s 2014(d) and (e) the household income, in dollars` | NUMBER | s 2014 | no (another part answers) | `s 2027(c) the ratio of household income to the income standard of eligibility` |
| `s 2014(c) the income standard of eligibility for households of equal size, in dollars` | NUMBER | s 2014 | no (another part answers) | `s 2027(c) the ratio of household income to the income standard of eligibility` |
| `s 2029(b) the household member is exempt from workfare requirements` | MAYBE BOOLEAN | s 2029 | yes: `s 2029(b) the household member is exempt from workfare requirements` | `s 2029(a)(1) the member is required to accept an offer from the subdivision to perform work` |
| `s 2015(d)(2)(B) to (F) the person is exempt from section 2015(d)(1) as the result of clause (B), (C), (D), (E), or (F)` | MAYBE BOOLEAN | s 2015 | yes: `s 2015(d)(2)(B) to (F) the person is exempt from section 2015(d)(1) as the result of clause (B), (C), (D), (E), or (F)` | `s 2029(b) the household member is exempt from workfare requirements` |

## ANSWERS (function name, type, section)

Every top-level function of the nine layer-1 modules, in module order. A function other sections of the Act cite (by a reference to its subsection) is marked with the citing sections; the citations were found by a regex scan of `usc07-ch51.txt` outside this part's ranges (2026-11-04).

Whole-section citations (no subsection named) from other sections: section 2015 cited from s 2014, s 2020, s 2026; section 2027 cited from s 2013, s 2016a, s 2026, s 2028; section 2029 cited from s 2025, s 2026.

| function name | type | section | cited from |
| --- | --- | --- | --- |
| `s 2015(a) the household or individual is eligible to participate` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(b)(1) the period of ineligibility the finding carries` | `s 2015(b)(1) outcome` | s 2015 | 2015(b) (s 2016, s 2025); 2015(b)(1) (s 2022, s 2024) |
| `s 2015(b)(1) the household may receive increased benefits as the result of the member's disqualification` | MAYBE BOOLEAN | s 2015 | 2015(b) (s 2016, s 2025); 2015(b)(1) (s 2022, s 2024) |
| `s 2015(b)(2) the State agency has proceeded against the individual in a way the paragraph provides` | MAYBE BOOLEAN | s 2015 | 2015(b)(2) (s 2016); 2015(b) (s 2016, s 2025) |
| `s 2015(b)(2) the State agency must proceed against the individual` | DEONTIC Party `s 2015(b)(2) action` | s 2015 | 2015(b)(2) (s 2016); 2015(b) (s 2016, s 2025) |
| `s 2015(b)(3) the period of ineligibility remains in effect` | MAYBE BOOLEAN | s 2015 | 2015(b) (s 2016, s 2025) |
| `s 2015(b)(3) the period of ineligibility can be stayed administratively or reviewed` | MAYBE BOOLEAN | s 2015 | 2015(b) (s 2016, s 2025) |
| `s 2015(b)(4) the State may withhold the information from the Secretary` | MAYBE BOOLEAN | s 2015 | 2015(b) (s 2016, s 2025) |
| `s 2015(c) the household is ineligible for refusing to provide necessary information` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(1)(A) the State agency may require periodic reports for the period` | MAYBE BOOLEAN | s 2015 | 2015(c)(1) (s 2014); 2015(c) (s 2020) |
| `s 2015(c)(1)(B) the household is required to report the change in income or household circumstances` | MAYBE BOOLEAN | s 2015 | 2015(c)(1) (s 2014); 2015(c) (s 2020) |
| `s 2015(c)(1)(C) the State agency may require monthly periodic reporting by households on a reservation` | MAYBE BOOLEAN | s 2015 | 2015(c)(1) (s 2014); 2015(c) (s 2020) |
| `s 2015(c)(1)(D)(i) the State agency may require reports at the interval` | MAYBE BOOLEAN | s 2015 | 2015(c)(1) (s 2014); 2015(c) (s 2020) |
| `s 2015(c)(1)(D)(ii) the household must report in the manner the Secretary prescribes` | MAYBE BOOLEAN | s 2015 | 2015(c)(1) (s 2014); 2015(c) (s 2020) |
| `s 2015(c)(2)(A) the date by which the allotment must be received` | MAYBE DATE | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(2)(A) the State agency must give the household its allotment within thirty days of the end of the month` | DEONTIC Party `s 2015(c)(2)(A) action` | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(2)(B) the household is to have special procedures available for filing` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(2)(D) the household is to be given prompt notice of the failure and a reasonable opportunity to cure` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(2)(C) and (E) the household is to have a reasonable period to file and a simple form with clear instructions each month` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(3) the report is considered complete` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(3) the form is to carry a description of the civil and criminal provisions and penalties in prominent bold face lettering` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(3) a further reporting requirement may be imposed for the subject matter` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(3) the household is to be given the opportunity to file reports at the same time under both Acts` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(4) the household shall not receive an allotment for the payment period to which the report applies` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(c)(5) the Secretary is authorized to waive the provision` | MAYBE BOOLEAN | s 2015 | 2015(c) (s 2020) |
| `s 2015(d)(1)(A) the individual is ineligible to participate in the program` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(B) the longest period of household ineligibility the State agency may determine, in days` | MAYBE NUMBER | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(B) the period the State agency determined is allowed` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(C) the individual remains ineligible until` | `s 2015(d)(1)(C) outcome` | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(i) and (ii) there is good cause, or the individual voluntarily quit or reduced work effort, as the Secretary determines` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(iii)(I) the State agency determines the meaning of a term, the procedure, or whether the individual is in compliance` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(iii)(II) the State agency may use the meaning, procedure or determination` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(iv) the individual is considered to have voluntarily quit without good cause` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(v)(I) the State agency must allow the household to select the person as head of the household` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(v)(II) the household is barred from changing the designation of the head` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(vi)(I) the household becomes eligible when the head leaves` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(1)(D)(vi)(II) the household the former head now heads is ineligible for the remaining period` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(2)(A) the person is exempt because subject to and complying with another work registration requirement` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(A) the failure is the same as failure to comply with paragraph (1)` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(B) the person is exempt because of responsibility for the care of a dependent child or an incapacitated person` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2) the State may lower the age of the dependent child` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(C) the person is exempt because a bona fide student enrolled at least half time` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(D) the person is exempt because a regular participant in a treatment and rehabilitation program` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(E) the person is exempt because employed or earning at the minimum rate for thirty hours` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(F) the person is exempt because a person between sixteen and eighteen` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2) the person is exempt from the requirements of paragraph (1)` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(2)(B) to (F) the person is exempt from section 2015(d)(1) as the result of clause (B), (C), (D), (E), or (F)` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026); 2015(d)(2) (s 2020) |
| `s 2015(d)(3) the household shall not participate while the member is on strike` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(3) the household may receive an increased allotment as the result of a decrease in the income of the striking member` | MAYBE BOOLEAN | s 2015 | 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(A)(i) the State agency is required to implement the program` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(A)(ii) the component must be delivered through the statewide workforce development system` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(B)(i) the component is one of those the definition lists` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(B)(i) the program is an employment and training program` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(B)(i) the State agency may apply employment requirements under the clause to the applicant` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(B)(ii) the program is a workforce partnership` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(C) the State agency may provide that participation supplements or supplants the other requirements` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(D) the State agency may exempt the category or the individual member from the requirement` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(D)(iii) the exemption is to be periodically evaluated to determine whether it continues to be valid` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(E) the State agency is required to establish requirements for participation by the individual` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(E)(iii) the individual is considered to be in compliance with the employment and training requirements` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(F)(i) the required hours of the household's members exceed the limit` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(F)(ii) the required hours of the member exceed one hundred and twenty hours per month` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(G) the State agency may operate the program component` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(H) the Federal funds may be used` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(i)(I) the State agency is required to pay or reimburse the cost` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(i)(II) the State agency is required to pay or reimburse the dependent care cost` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(i)(II) the most the State agency may pay or reimburse for the dependent care, in dollars` | NUMBER | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(i) the individual may be required to participate in the program` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(ii) the State agency may arrange dependent care instead of reimbursing it` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(iii)(I) the value or amount is treated as income for the other program` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(I)(iii)(II) the value or amount may be claimed as an employment-related expense for the credit under section 21 of title 26` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(J) the Secretary is required to promulgate the guideline` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(K) the funds the State agency uses exceed the limit` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(L) the Secretary is required to ensure that the State agencies comply with the requirement` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(M) the facilities may be used` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(i) the Secretary or the State agency is required to require the program to submit the information` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(ii) the State agency may use the workforce partnership` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(iii)(I) the State agency is required to provide the list of certified workforce partnerships to the household member` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(iii)(II) the State agency may require the member to participate in a workforce partnership` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(iv)(I) the workforce partnership may replace the employment or training of the individual` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(iv)(II) this subsection or subsection (o) affects the criteria or screening process for selecting participants` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(N)(v) the reporting requirement may be imposed on the workforce partnership` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(O)(i) the step is one the State agency is to take` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(d)(4)(O)(ii) the individual is found to have refused without good cause to participate in an employment and training program` | MAYBE BOOLEAN | s 2015 | 2015(d)(4) (s 2014, s 2020, s 2025, s 2031); 2015(d) (s 2014, s 2025, s 2026) |
| `s 2015(e) the individual is ineligible as a student` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(f) the individual is ineligible for want of residence or status` | MAYBE BOOLEAN | s 2015 | 2015(f) (s 2020) |
| `s 2015(f) the income of the ineligible individual counted for the household, in dollars` | MAYBE NUMBER | s 2015 | 2015(f) (s 2020) |
| `s 2015(f) the financial resources of the ineligible individual are considered for the household` | MAYBE BOOLEAN | s 2015 | 2015(f) (s 2020) |
| `s 2015(g) the individual is not considered a member of a household for the month` | MAYBE BOOLEAN | s 2015 | 2015(g) (s 2020) |
| `s 2015(h) the household is ineligible on the date` | `s 2015(h) outcome` | s 2015 |  |
| `s 2015(i)(1) the State agency may impose the same disqualification under the program` | MAYBE BOOLEAN | s 2015 | 2015(i) (s 2020) |
| `s 2015(i)(2) the State agency may use the rules and procedures of part A of title IV` | MAYBE BOOLEAN | s 2015 | 2015(i) (s 2020) |
| `s 2015(i)(3) a prior disqualification under subsection (d) is considered in determining the former member's eligibility` | MAYBE BOOLEAN | s 2015 | 2015(i) (s 2020) |
| `s 2015(i)(3) the member who applies is treated as a new applicant` | MAYBE BOOLEAN | s 2015 | 2015(i) (s 2020) |
| `s 2015(j) the period of ineligibility for receiving multiple benefits` | `s 2015(j) outcome` | s 2015 |  |
| `s 2015(k)(1) the individual is ineligible while fleeing or violating probation or parole` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(k)(2)(A) the individual is fleeing or actively sought, as the Secretary defines the terms` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(k)(2)(B) the State agency is to disqualify the individual under the Secretary's consistent procedures` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(l) the individual is ineligible for want of cooperation with the child support agency` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(l)(2) paragraph (1) does not apply to the individual` | MAYBE BOOLEAN | s 2015 | 2015(l)(2) (s 2026) |
| `s 2015(l)(3) the individual is required to pay a fee or other cost for the service` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(m)(1) the noncustodial parent is ineligible for refusing to cooperate with the child support agency` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(m)(2) the matter is a refusal to cooperate under the guidelines and procedures` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(m)(3) the individual is required to pay a fee or other cost for the service` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(m)(4) the State agency is required to provide safeguards restricting the use of the information to the purposes for which it was collected` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(n) the individual is ineligible for the month for child support arrears` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(o)(1) the program is a work program` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(2) the month is a benefit month in which the individual did none of the four things` | BOOLEAN | s 2015 | 2015(o)(2) (s 2016, s 2025); 2015(o) (s 2025) |
| `s 2015(o)(2) the individual is ineligible for failing the work requirement` | MAYBE BOOLEAN | s 2015 | 2015(o)(2) (s 2016, s 2025); 2015(o) (s 2025) |
| `s 2015(o)(3) paragraph (2) does not apply to the individual` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(3) (s 2025) |
| `s 2015(o)(4)(A) the Secretary may waive the applicability of paragraph (2) to the group of individuals` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(4) (s 2025) |
| `s 2015(o)(4)(B) the Secretary is required to report the basis for the waiver to the Committees` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(4) (s 2025) |
| `s 2015(o)(4)(C) the place is a noncontiguous State` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(4) (s 2025) |
| `s 2015(o)(5)(A) the individual regains eligibility` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(5)(B) the individual remains eligible` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(5)(C) the individual remains eligible on the date for the 3-month period` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(6)(A)(i) the caseload` | MAYBE NUMBER | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(A)(ii) the individual is a covered individual` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(B) the State agency may provide an exemption from paragraph (2)` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(C) to (F) the percentage of covered individuals for the fiscal year` | MAYBE NUMBER | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(C) to (F) the average monthly number of exemptions in effect is within the limit` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(G) the Secretary is required to adjust the number of individuals estimated for the State` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(H) the increase or decrease in the number of individuals who may be granted an exemption` | MAYBE NUMBER | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(I) the State agency is required to submit the report to the Secretary` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(6)(J) the State agency may accumulate unused exemptions to be provided beyond the subsequent fiscal year` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025); 2015(o)(6) (s 2025) |
| `s 2015(o)(7)(A) the place is a noncontiguous State` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(7)(B) the Secretary may exempt individuals in the noncontiguous State from paragraph (2)` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(7)(C) the Secretary is required to consider the matter in determining good faith effort` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(7)(D)(i) the exemption may run until the date` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(7)(D)(ii) the Secretary may terminate the exemption early` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(7)(E) the State agency is required to submit the quarterly progress reports and the information on risks and barriers` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(o)(8) this subsection makes the individual eligible for benefits` | MAYBE BOOLEAN | s 2015 | 2015(o) (s 2025) |
| `s 2015(p) the person is ineligible for benefits` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(p) the period of ineligibility` | MAYBE `Period of ineligibility` | s 2015 |  |
| `s 2015(q) the person is ineligible for benefits` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(q) the period of ineligibility` | MAYBE `Period of ineligibility` | s 2015 |  |
| `s 2015(r)(1)(A) the offense is one of those named in clauses (i) to (v)` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(r)(1) the individual is ineligible for benefits` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(r)(2) the individual is counted as a member of the household` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(r)(2) the number of members of the household counted in determining the amount of benefits` | MAYBE NUMBER | s 2015 |  |
| `s 2015(r)(2) the income and resources of the individual are counted as income and resources of the household` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(r)(3) the State is required to require the individual to attest to whether the individual or any member of the household has been convicted of a crime described in paragraph (1)` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(s)(1) the household loses eligibility for benefits upon receipt of the winnings` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(s)(2) the household remains ineligible for participation` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(s) the household is ineligible on the date` | MAYBE BOOLEAN | s 2015 |  |
| `s 2015(s)(3) the State agency is required to establish agreements with the entities responsible for the regulation or sponsorship of gaming in the State` | MAYBE BOOLEAN | s 2015 |  |
| `s 2027(a)(1) sums are authorized to be appropriated for the fiscal year` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028); 2027(a)(1) (s 2020, s 2025, s 2036a) |
| `s 2027(a)(1) the most that is authorized in the fiscal year to carry out section 2026` | MAYBE NUMBER | s 2027 | 2027(a) (s 2020, s 2026, s 2028); 2027(a)(1) (s 2020, s 2025, s 2036a) |
| `s 2027(a)(1) the amount for section 2026 is within what is authorized` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028); 2027(a)(1) (s 2020, s 2025, s 2036a) |
| `s 2027(a)(2) the limitation on the use of funds bars the use` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(2) the President is required to ensure that paragraph (2) is complied with` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(3)(A) the Secretary may use the amount for the grants` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(3)(B) the Secretary is required to make an award under paragraph (3) to the body` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(3)(B) the body is required to administer the grants in coordination with other State or local agencies serving low-income people` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(3)(C) the project is required to include an evaluation component and to develop an implementation plan for replication in other States` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(a)(3)(D) the Secretary is required to report on the results of the projects and to disseminate the results` | MAYBE BOOLEAN | s 2027 | 2027(a) (s 2020, s 2026, s 2028) |
| `s 2027(b) the value of the allotments issued is within the limit` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(b) the Secretary is required to direct State agencies to reduce the value of the allotments to be issued` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(b) the reduction in the value of the allotments to the extent necessary to comply with the subsection` | MAYBE NUMBER | s 2027 |  |
| `s 2027(c) the Secretary is required to ensure that the reductions reflect the ratio of household income to the income standards of eligibility` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(c) the ratio of household income to the income standard of eligibility` | MAYBE NUMBER | s 2027 |  |
| `s 2027(c)(1) the Secretary may establish special provisions applicable to the person in prescribing the manner of reducing allotments` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(c)(2) the Secretary may establish minimum allotments after any reductions are otherwise determined` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(d) the Secretary is required to take the requisite action to reduce allotments` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(d) the last day for the requisite action` | DATE | s 2027 |  |
| `s 2027(d) the action was taken in time` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(d) the Secretary must take the requisite action within sixty days of the report` | DEONTIC Party `s 2027(d) action` | s 2027 |  |
| `s 2027(d) the Secretary is required to furnish the Committees a statement` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(d) the last day for the statement` | DATE | s 2027 |  |
| `s 2027(d) the statement was furnished in time` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(d) the Secretary must furnish the Committees a statement within seven days of the action` | DEONTIC Party `s 2027(d) action` | s 2027 |  |
| `s 2027(d) the statement sets forth what the subsection requires` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(e) the claim is against a household or a State agency` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(e) the fiscal year of the supplemental nutrition assistance program appropriation account to which the funds collected on the claim are credited` | MAYBE NUMBER | s 2027 |  |
| `s 2027(e) the fiscal year of the appropriation account from which the funds provided to State agencies are paid` | MAYBE NUMBER | s 2027 |  |
| `s 2027(f) the funds may be transferred to the recipient` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(g) the ban bars the use of the funds for the activity` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(h) the Secretary is required to issue the regulations` | MAYBE BOOLEAN | s 2027 |  |
| `s 2027(h) the regulations are to prohibit the entity from compensating the person` | MAYBE BOOLEAN | s 2027 |  |
| `s 2029(a)(1) the Secretary is required to permit the political subdivision to operate a workfare program` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(a)(1) the member is required to accept an offer from the subdivision to perform work` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(a)(1) the portion of the allotment the household is entitled to for the hours of work` | MAYBE NUMBER | s 2029 |  |
| `s 2029(a)(2)(A) the Secretary is required to promulgate guidelines under paragraph (1)` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(a)(2)(B) the political subdivision may comply with the requirements of this section by operating the program` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(b) the household member is exempt from workfare requirements` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(c) the operating agency may require the work` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(c) the most hours of workfare work the agency may require of the member that week` | MAYBE NUMBER | s 2029 |  |
| `s 2029(d)(1) the operating agency may provide the work` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(d)(2) the operating agency is required to provide the same benefits and working conditions that are provided at the job site` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(d)(3) the amount the operating agency is required to reimburse for the month` | MAYBE NUMBER | s 2029 |  |
| `s 2029(e) the operating agency may allow a job search period of the length, prior to making workfare assignments` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(e) the last day of the longest job search period` | DATE | s 2029 |  |
| `s 2029(f) the individual or household may become ineligible under section 2015(d)(1) for failing to comply with this section` | MAYBE BOOLEAN | s 2029 |  |
| `s 2029(g)(1) the amount the Secretary is required to pay to the operating agency` | MAYBE NUMBER | s 2029 |  |
| `s 2029(g)(2)(B) the funds saved from employment related to a workfare program` | MAYBE NUMBER | s 2029 |  |
| `s 2029(g)(2)(A) the amount the Secretary is required to pay to the operating agency from the funds saved` | MAYBE NUMBER | s 2029 |  |
| `s 2029(g)(3) the Secretary may suspend or cancel some or all of the payments, or withdraw approval from the subdivision` | MAYBE BOOLEAN | s 2029 |  |

Cited from other sections but matching no function by label: 2015(f)(2) (s 2014). Each is encoded inside the function named for its parent provision (for example the list of statuses in 2015(f)(2) is inside `s 2015(f) the individual is ineligible for want of residence or status`).
