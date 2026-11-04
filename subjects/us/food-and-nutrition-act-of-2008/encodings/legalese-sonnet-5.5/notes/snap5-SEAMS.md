# SEAMS (snap5)

Two lists, as PLAN.md rule 9 asks: ASKS (the inputs a caller must supply, with the section that answers each) and ANSWERS (what this part offers to the others).
Both lists are generated from the layer-1 modules by `work/tools/seams.py`, so they cannot drift from the code; the counts below are the counts of that run.

Where PLAN.md and the brief differ, the brief governs (see NOTES.md, "Where PLAN.md and the brief differ"): a borrowed term is asked as a plain fact, and only the seams the plan names (`s 2015(o)(2)`, `(3)`, `(4)`, `(6)`, `s 2027(a)`, `s 2012(u)(3)`) keep the plan's `s 20NN <what you ask>` name.

## ASKS

Every row is a `GIVEN` input of a layer-1 function whose answer lies outside snap5's three sections, or with an official, or in another Act. The same input name asked by several functions is listed once, with the functions that ask it. Inputs that are facts about the case in hand (a date, an amount, who did what) are not seams and are not listed; `PROGRESS.md` and the `@desc` of each seat question describe them.

Counts: plan-named seam: 8; another section or Act: 27; the Secretary's decision or another official's: 38 (73 inputs).

| kind | input name | type | answering section | asked by |
| --- | --- | --- | --- | --- |
| plan-named seam | `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between the two dates` | NUMBER | section 2012(u)(3), outside the ranges of this part (another part or the core) | `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year`; `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` |
| plan-named seam | `s 2015(o)(2) the individual is in the last month of the 3-month period` | MAYBE BOOLEAN | section 2015(o)(2), outside the ranges of this part (another part or the core) | `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant o...` |
| plan-named seam | `s 2015(o)(3) the individual is eligible for an exception` | MAYBE BOOLEAN | section 2015(o)(3), outside the ranges of this part (another part or the core) | `s 2025(h)(1)(E)(i) the costs of serving the member may be reimbursed from the...`; `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant o...` |
| plan-named seam | `s 2015(o)(4) the individual is eligible for a waiver` | MAYBE BOOLEAN | section 2015(o)(4), outside the ranges of this part (another part or the core) | `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant o...` |
| plan-named seam | `s 2015(o)(6) the individual is exempt` | MAYBE BOOLEAN | section 2015(o)(6), outside the ranges of this part (another part or the core) | `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant o...` |
| plan-named seam | `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` | MAYBE BOOLEAN | this part, section 2025(h)(1)(F)(vi)(II) | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the su...` |
| plan-named seam | `s 2027(a) appropriations are available` | MAYBE BOOLEAN | section 2027(a), outside the ranges of this part (another part or the core) | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` |
| plan-named seam | `s 2028(b)(1) the Commonwealth may receive payments` | MAYBE BOOLEAN | this part, section 2028(b)(1) | `s 2028(a)(3) the payment to the Commonwealth for the fiscal year` |
| another section or Act | `it arises directly out of their performance of duties under this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(f) the expense may be paid` |
| another section or Act | `it is the period used to determine the amount of the State family assistance grant for a State under section 403 of the Social Security Act` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(k)(1)(B) the period is the base period` |
| another section or Act | `it is the program of aid to families with dependent children established under part A of title IV of the Social Security Act` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(k)(1)(A) the program is the AFDC program` |
| another section or Act | `it is the program of medical assistance under a State plan under title XIX of the Social Security Act` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(k)(1)(C) the program is the medicaid program` |
| another section or Act | `it is the program of medical assistance under a waiver of the plan under title XIX of the Social Security Act` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(k)(1)(C) the program is the medicaid program` |
| another section or Act | `it takes into account the number of individuals who are not exempt from the work requirement under section 2015(o)` | BOOLEAN | section 2015(o), outside the ranges of this part | `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` |
| another section or Act | `it would assist in meeting the requirements of this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(g)(1)(A) the planning, design, development or installation of the syst...` |
| another section or Act | `payment made under section 2015(d)(4)(I)(i)(II), in dollars` | NUMBER | section 2015(d)(4)(I)(i)(II), outside the ranges of this part | `s 2025(h)(3) the most the reimbursement for dependent care expenses may be` |
| another section or Act | `payments are made under this chapter for the program` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2028(c)(1) the Secretary shall provide for the review of the program` |
| another section or Act | `recovered or collected pursuant to section 2015(b)` | BOOLEAN | section 2015(b), outside the ranges of this part | `s 2025(a) the amount of the claim the State may be permitted to retain, in do...`; `s 2025(a) the share of recovered or collected funds the Secretary may permit ...` |
| another section or Act | `recovered or collected pursuant to section 2022(c)` | BOOLEAN | section 2022(c), outside the ranges of this part | `s 2025(a) the amount of the claim the State may be permitted to retain, in do...`; `s 2025(a) the share of recovered or collected funds the Secretary may permit ...` |
| another section or Act | `the State agency administers the program in a Native village within the State of Alaska identified in section 1610(b) of title 43` | BOOLEAN | another title of the Code, outside the chapter | `s 2025(a) the additional amount the Secretary may pay a State agency for a re...` |
| another section or Act | `the State agency administers the program on all or part of an Indian reservation under section 2020(d)` | BOOLEAN | section 2020(d), outside the ranges of this part | `s 2025(a) the additional amount the Secretary may pay a State agency for a re...` |
| another section or Act | `the State agency has made a commitment to offer a position in a program described in subparagraph (B) or (C) of section 2015(o)(2) to each applicant or recipient described in subclauses (I) to (IV)` | BOOLEAN | section 2015(o)(2), outside the ranges of this part | `s 2025(h)(1)(E)(ii) the State agency is eligible for an additional allocation` |
| another section or Act | `the activity is an employment and training activity authorized under the program of block grants to States for temporary assistance for needy families established under part A of title IV of the So...` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(h)(1)(F)(iv) the program or service is allowable` |
| another section or Act | `the applicant or participant receives benefits under title XVI of the Social Security Act` | BOOLEAN | the Social Security Act, outside the chapter | `s 2025(e) the Secretary and State agencies shall have access to the information` |
| another section or Act | `the data are relevant data from a workforce partnership carried out under section 2015(d)(4)(N)` | BOOLEAN | section 2015(d)(4)(N), outside the ranges of this part | `s 2025(h)(5)(B)(v) the State agency may report the data to demonstrate the nu...` |
| another section or Act | `the error results from the application of new regulations promulgated under this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(3)(A) the error is excluded from the payment error rate` |
| another section or Act | `the member is placed in and complies with a program described in subparagraph (B) or (C) of section 2015(o)(2)` | BOOLEAN | section 2015(o)(2), outside the ranges of this part | `s 2025(h)(1)(E)(i) the costs of serving the member may be reimbursed from the...` |
| another section or Act | `the official is responsible for making determinations of ineligibility under this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(a) the official may receive or benefit from the revenues retained by t...` |
| another section or Act | `the pilot project is in accordance with the requirements of sections 2015(d) and 2029` | BOOLEAN | section 2015(d), outside the ranges of this part | `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` |
| another section or Act | `the program is a nutrition assistance program extended under section 1469d(c) of title 48` | BOOLEAN | another title of the Code, outside the chapter | `s 2028(a)(2)(C) the payment toward American Samoa's expenditures` |
| another section or Act | `the program or service is authorized under this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(iv) the program or service is allowable` |
| another section or Act | `the project limits the use of benefits provided under the Food and Nutrition Act of 2008` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2026a(c)(4) the funds made available under this section may be used for the...` |
| another section or Act | `the use is for pilot projects that comply with this chapter` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(ix)(I) the funds may be used for the use` |
| another section or Act | `the use is operating an employment and training program under section 2015(d)(4)` | BOOLEAN | section 2015(d)(4), outside the ranges of this part | `s 2025(h)(4) the funds may be used for the use` |
| another section or Act | `they include strategies that target individuals with low skills or limited work experience, individuals subject to the requirements under section 2015(o), and individuals who are working` | BOOLEAN | section 2015(o), outside the ranges of this part | `s 2025(h)(1)(F)(ii)(III)(ee) the Secretary has ensured that the group of pilo...` |
| the Secretary's decision or another official's | `date the Secretary determines final error rates, the national average payment error rate and the amounts claimed or liability amounts` | DATE | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(8)(C)(i) the final error rates are determined in time` |
| the Secretary's decision or another official's | `date the Secretary of Health and Human Services makes the determination with respect to the State` | DATE | the Secretary's (or another official's) decision, which the text does not make | `s 2025(k)(4)(A) the Secretary notifies the chief executive officer in time`; `s 2025(k)(4)(A) the last day for the Secretary to notify the chief executive ...` |
| the Secretary's decision or another official's | `gives the other information the Secretary requires` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2028(b)(2)(B) the statement has the required contents` |
| the Secretary's decision or another official's | `includes the other information the Secretary requires` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2028(b)(1)(A) the plan has the required contents` |
| the Secretary's decision or another official's | `it establishes performance criteria relating to other indicators of effective administration determined by the Secretary` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(d)(1)(A) the guidance has the content required` |
| the Secretary's decision or another official's | `it is a determination of the Secretary of Health and Human Services under paragraph (2)` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(k)(4)(D) the determination or decision is subject to judicial review` |
| the Secretary's decision or another official's | `it meets such conditions as the Secretary prescribes` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(g)(1)(A) the planning, design, development or installation of the syst...` |
| the Secretary's decision or another official's | `it would be accessible by the Secretary for inspection and audit under section 2020(a)(3)(B)` | BOOLEAN | section 2020(a)(3)(B), outside the ranges of this part | `s 2025(g)(1)(A) the planning, design, development or installation of the syst...` |
| the Secretary's decision or another official's | `the Commonwealth has a plan for the fiscal year approved by the Secretary` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2028(b)(1) the Commonwealth may receive payments` |
| the Secretary's decision or another official's | `the Secretary and the Commissioner of Social Security determine that access is necessary` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(e) the Secretary and State agencies shall have access to the information` |
| the Secretary's decision or another official's | `the Secretary considers the degree to which the pilot project would enhance existing employment and training programs in the State` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selectin...` |
| the Secretary's decision or another official's | `the Secretary considers the degree to which the pilot project would enhance the employment and earnings of program participants` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selectin...` |
| the Secretary's decision or another official's | `the Secretary considers the factor necessary` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(4) the Secretary may require the State agency to report the factor` |
| the Secretary's decision or another official's | `the Secretary considers whether the State agency has a demonstrated capacity to operate high quality employment and training programs` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selectin...` |
| the Secretary's decision or another official's | `the Secretary considers whether there is evidence that the pilot project could be replicated easily by other States or political subdivisions` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selectin...` |
| the Secretary's decision or another official's | `the Secretary determines that discontinuation of benefits in the form of cash is likely to have significant adverse effects` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2028(e)(3)(B) the Secretary may approve a plan that exempts participants or...` |
| the Secretary's decision or another official's | `the Secretary determines that the performance of the State agency with respect to employment and training outcomes is inadequate` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(5)(E) the Secretary may require the State agency to modify the plan` |
| the Secretary's decision or another official's | `the Secretary determines that the system has these qualities` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(g)(1)(A) the planning, design, development or installation of the syst...` |
| the Secretary's decision or another official's | `the Secretary determines that the system may continue to be operated in accordance with clauses (i) through (vii) of subparagraph (A)` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(g)(1)(B) the operation of the system qualifies for payment` |
| the Secretary's decision or another official's | `the Secretary determines that, for the second or subsequent consecutive fiscal year, a 95 percent statistical probability exists that the payment error rate of the State agency exceeds 105 percent ...` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the Stat...` |
| the Secretary's decision or another official's | `the Secretary determines the procedures would be cost effective` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(i)(2) the Secretary may require the State agency to carry out new or m...` |
| the Secretary's decision or another official's | `the Secretary determines the procedures would improve the integrity of the program` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(i)(2) the Secretary may require the State agency to carry out new or m...` |
| the Secretary's decision or another official's | `the Secretary determines the program is one under which that is so` | MAYBE BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(b)(1) the program is a work supplementation or support program` |
| the Secretary's decision or another official's | `the Secretary monitors the employment and training programs carried out by State agencies under section 2015(d)(4)` | BOOLEAN | section 2015(d)(4), outside the ranges of this part | `s 2025(h)(5)(A) the Secretary has monitored and assessed as required` |
| the Secretary's decision or another official's | `the Secretary of Health and Human Services makes the determinations with respect to the base period for each State` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(k)(2) the determinations are made as required` |
| the Secretary's decision or another official's | `the State agency fails to meet the reporting requirements established by the Secretary` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(4) the Secretary shall base the determination on all pertinent info...` |
| the Secretary's decision or another official's | `the action is an action by the Secretary under subparagraph (D) or (F)(iii) of paragraph (1)` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(7)(C) the action is subject to administrative or judicial review` |
| the Secretary's decision or another official's | `the amount the Secretary determines necessary for effective operation, in dollars` | MAYBE NUMBER | the Secretary's (or another official's) decision, which the text does not make | `s 2025(a) the additional amount the Secretary may pay a State agency for a re...` |
| the Secretary's decision or another official's | `the chief executive officer failed to make the payment within the reasonable period of time determined by the Secretary` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(1)(E)(ii)(II)(aa) the largest reduction the Secretary may make in a...` |
| the Secretary's decision or another official's | `the costs are allocated for reimbursement to the supplemental nutrition assistance program under a plan submitted by a State to the Secretary of Health and Human Services to allocate administrative...` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` |
| the Secretary's decision or another official's | `the data resulting from each pilot project is thoroughly evaluated before the Secretary approves the system for broader implementation` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(g)(1)(A)(v) the system would be tested adequately before and after imp...` |
| the Secretary's decision or another official's | `the determination is the Secretary's determination whether, and in what amount, to award a performance bonus payment` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(d)(4) the determination is subject to administrative or judicial review` |
| the Secretary's decision or another official's | `the entity has submitted an application containing the information the Secretary may require` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2026a(c)(2) the entity has met the application requirement` |
| the Secretary's decision or another official's | `the error results from actions based on policy information approved or disseminated, in writing, by the Secretary or the Secretary's designee` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(3)(B) the error is excluded from the payment error rate` |
| the Secretary's decision or another official's | `the formula is determined and adjusted by the Secretary` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` |
| the Secretary's decision or another official's | `the pilot project meets the terms and conditions the Secretary considers to be appropriate` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` |
| the Secretary's decision or another official's | `the time is within a period determined by the Secretary under item (aa)` | BOOLEAN | the Secretary's (or another official's) decision, which the text does not make | `s 2025(c)(1)(E)(ii)(II)(bb) interest accrues on the payment under section 202...` |
| the Secretary's decision or another official's | `threshold number of participants the Secretary determines, a year` | NUMBER | the Secretary's (or another official's) decision, which the text does not make | `s 2025(h)(5)(B)(iii) the State employment and training plan must identify rep...`; `s 2025(h)(5)(B)(iii) the threshold the Secretary determines is allowed` |

## ANSWERS

Every top-level function or rule of the layer-1 modules, with its type and the section it implements (its name begins with the section label). 269 in all.

| function | type | section | module |
| --- | --- | --- | --- |
| `s 2025(a) the share of administrative costs the Secretary is authorized to pay` | MAYBE NUMBER | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the amount the Secretary is authorized to pay before any reduction under subsection (k)` | MAYBE NUMBER | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the cost is an administrative cost the Secretary is authorized to pay a share of` | MAYBE BOOLEAN | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the additional amount the Secretary may pay a State agency for a reservation or a Native village` | MAYBE NUMBER | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the share of recovered or collected funds the Secretary may permit the State to retain` | `s 2025(a) retention` | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars` | NUMBER | s 2025(a) | snap5-s2025-ab |
| `s 2025(a) the official may receive or benefit from the revenues retained by the State` | MAYBE BOOLEAN | s 2025(a) | snap5-s2025-ab |
| `s 2025(b)(1) the program is a work supplementation or support program` | MAYBE BOOLEAN | s 2025(b)(1) | snap5-s2025-ab |
| `s 2025(b)(2) the State agency may elect to use an amount equal to the allotment to subsidize or support the job` | MAYBE BOOLEAN | s 2025(b)(2) | snap5-s2025-ab |
| `s 2025(b)(3) the procedure applies` | MAYBE BOOLEAN | s 2025(b)(3) | snap5-s2025-ab |
| `s 2025(b)(3)(A) the amount the Secretary shall pay the State agency` | MAYBE NUMBER | s 2025(b)(3)(A) | snap5-s2025-ab |
| `s 2025(b)(3)(B) the State agency has expended the amount as required` | MAYBE BOOLEAN | s 2025(b)(3)(B) | snap5-s2025-ab |
| `s 2025(b)(3)(C)(i) the amount received is excluded from household income and resources for sections 2014 and 2017(a)` | MAYBE BOOLEAN | s 2025(b)(3)(C)(i) | snap5-s2025-ab |
| `s 2025(b)(3)(C)(ii) the amount received is considered the value of an allotment provided to the household for section 2017(b)` | MAYBE BOOLEAN | s 2025(b)(3)(C)(ii) | snap5-s2025-ab |
| `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` | MAYBE BOOLEAN | s 2025(b)(3)(D) | snap5-s2025-ab |
| `s 2025(b)(4) the individual is excused from a work requirement under section 2015(d) by reason of the fact that the State has a work supp...` | MAYBE BOOLEAN | s 2025(b)(4) | snap5-s2025-ab |
| `s 2025(b)(5) the State agency has provided the description required` | MAYBE BOOLEAN | s 2025(b)(5) | snap5-s2025-ab |
| `s 2025(b)(6) the work supplementation or support program is permitted` | MAYBE BOOLEAN | s 2025(b)(6) | snap5-s2025-ab |
| `s 2025(c)(1)(A)(i) the Secretary's quality control system is the system required` | MAYBE BOOLEAN | s 2025(c)(1)(A)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(A)(ii)(I) the tolerance level set is within the limit` | MAYBE BOOLEAN | s 2025(c)(1)(A)(ii)(I) | snap5-s2025-c1 |
| `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year` | MAYBE NUMBER | s 2025(c)(1)(A)(ii)(II) | snap5-s2025-c1 |
| `s 2025(c)(1)(B)(i) the last day for the interim final regulations` | DATE | s 2025(c)(1)(B)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(B)(i) the interim final regulations are issued in time` | MAYBE BOOLEAN | s 2025(c)(1)(B)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(B)(i) the interim final regulations have the content required` | MAYBE BOOLEAN | s 2025(c)(1)(B)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(B)(ii) the Secretary shall debar the person` | MAYBE BOOLEAN | s 2025(c)(1)(B)(ii) | snap5-s2025-c1 |
| `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency` | MAYBE BOOLEAN | s 2025(c)(1)(C) | snap5-s2025-c1 |
| `s 2025(c)(1)(C) the liability amount` | MAYBE NUMBER | s 2025(c)(1)(C) | snap5-s2025-c1 |
| `s 2025(c)(1)(D)(i)(I) the portion required for new investment is within the limit` | MAYBE BOOLEAN | s 2025(c)(1)(D)(i)(I) | snap5-s2025-c1 |
| `s 2025(c)(1)(D)(i)(I) the new investment amount may be matched by Federal funds` | MAYBE BOOLEAN | s 2025(c)(1)(D)(i)(I) | snap5-s2025-c1 |
| `s 2025(c)(1)(D)(i)(II) the portion designated as the at-risk amount is within the limit` | MAYBE BOOLEAN | s 2025(c)(1)(D)(i)(II) | snap5-s2025-c1 |
| `s 2025(c)(1)(D)(i)(III) the combination of actions is allowed` | MAYBE BOOLEAN | s 2025(c)(1)(D)(i)(III) | snap5-s2025-c1 |
| `s 2025(c)(1)(D)(ii) the settlement with the State agency is permitted` | MAYBE BOOLEAN | s 2025(c)(1)(D)(ii) | snap5-s2025-c1 |
| `s 2025(c)(1)(E)(i) the State agency shall pay the at-risk amount to the Secretary` | MAYBE BOOLEAN | s 2025(c)(1)(E)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(E)(i) the at-risk amount payable to the Secretary` | MAYBE NUMBER | s 2025(c)(1)(E)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(E)(ii)(I) the chief executive officer of the State shall now remit the at-risk amount to the Secretary` | MAYBE BOOLEAN | s 2025(c)(1)(E)(ii)(I) | snap5-s2025-c1 |
| `s 2025(c)(1)(E)(ii)(II)(aa) the largest reduction the Secretary may make in amounts due to the State agency` | MAYBE NUMBER | s 2025(c)(1)(E)(ii)(II)(aa) | snap5-s2025-c1 |
| `s 2025(c)(1)(E)(ii)(II)(bb) interest accrues on the payment under section 2022(a)(2)` | MAYBE BOOLEAN | s 2025(c)(1)(E)(ii)(II)(bb) | snap5-s2025-c1 |
| `s 2025(c)(1)(F)(i) the largest reduction the Secretary may make in amounts due to the State agency` | MAYBE NUMBER | s 2025(c)(1)(F)(i) | snap5-s2025-c1 |
| `s 2025(c)(1)(F)(ii) the amount the Secretary shall pay the State agency` | MAYBE NUMBER | s 2025(c)(1)(F)(ii) | snap5-s2025-c1 |
| `s 2025(c)(1)(F)(iii) the Secretary shall require new investment or payment of the new investment amount` | MAYBE BOOLEAN | s 2025(c)(1)(F)(iii) | snap5-s2025-c1 |
| `s 2025(c)(1)(F)(iii) the new investment amount is divided as required` | MAYBE BOOLEAN | s 2025(c)(1)(F)(iii) | snap5-s2025-c1 |
| `s 2025(c)(1)(G) the State agency is required to develop and implement a corrective action plan` | MAYBE BOOLEAN | s 2025(c)(1)(G) | snap5-s2025-c1 |
| `s 2025(c)(2)(A) the payment error rate` | NUMBER | s 2025(c)(2)(A) | snap5-s2025-c2 |
| `s 2025(c)(2)(B) the overpayment error rate` | MAYBE NUMBER | s 2025(c)(2)(B) | snap5-s2025-c2 |
| `s 2025(c)(2)(C) the underpayment error rate` | MAYBE NUMBER | s 2025(c)(2)(C) | snap5-s2025-c2 |
| `s 2025(c)(3)(A) the error is excluded from the payment error rate` | MAYBE BOOLEAN | s 2025(c)(3)(A) | snap5-s2025-c2 |
| `s 2025(c)(3)(B) the error is excluded from the payment error rate` | MAYBE BOOLEAN | s 2025(c)(3)(B) | snap5-s2025-c2 |
| `s 2025(c)(4) the Secretary may require the State agency to report the factor` | MAYBE BOOLEAN | s 2025(c)(4) | snap5-s2025-c2 |
| `s 2025(c)(4) the Secretary shall base the determination on all pertinent information available` | MAYBE BOOLEAN | s 2025(c)(4) | snap5-s2025-c2 |
| `s 2025(c)(5) the State agency has submitted the data as required` | MAYBE BOOLEAN | s 2025(c)(5) | snap5-s2025-c2 |
| `s 2025(c)(5) the collection efforts are initiated in time` | MAYBE BOOLEAN | s 2025(c)(5) | snap5-s2025-c2 |
| `s 2025(c)(6)(A) the national performance measure` | MAYBE NUMBER | s 2025(c)(6)(A) | snap5-s2025-c2 |
| `s 2025(c)(6)(B) the Secretary may use another measure of the State's error` | MAYBE BOOLEAN | s 2025(c)(6)(B) | snap5-s2025-c2 |
| `s 2025(c)(6)(C) the announced national performance measure shall be used` | MAYBE BOOLEAN | s 2025(c)(6)(C) | snap5-s2025-c2 |
| `s 2025(c)(6)(D) the national performance measure is subject to administrative or judicial review` | MAYBE BOOLEAN | s 2025(c)(6)(D) | snap5-s2025-c2 |
| `s 2025(c)(7)(A) the State may seek administrative and judicial review of the action under section 2023` | MAYBE BOOLEAN | s 2025(c)(7)(A) | snap5-s2025-c2 |
| `s 2025(c)(7)(B) the determination is subject to administrative or judicial review` | MAYBE BOOLEAN | s 2025(c)(7)(B) | snap5-s2025-c2 |
| `s 2025(c)(7)(C) the action is subject to administrative or judicial review` | MAYBE BOOLEAN | s 2025(c)(7)(C) | snap5-s2025-c2 |
| `s 2025(c)(8)(A) this paragraph applies to the determination` | MAYBE BOOLEAN | s 2025(c)(8)(A) | snap5-s2025-c2 |
| `s 2025(c)(8)(B) the first May 31 after the end of the fiscal year` | DATE | s 2025(c)(8)(B) | snap5-s2025-c2 |
| `s 2025(c)(8)(B) the case review and arbitrations are completed in time` | MAYBE BOOLEAN | s 2025(c)(8)(B) | snap5-s2025-c2 |
| `s 2025(c)(8)(C) the first June 30 after the end of the fiscal year` | DATE | s 2025(c)(8)(C) | snap5-s2025-c2 |
| `s 2025(c)(8)(C)(i) the final error rates are determined in time` | MAYBE BOOLEAN | s 2025(c)(8)(C)(i) | snap5-s2025-c2 |
| `s 2025(c)(8)(C)(ii) the State agencies are notified in time` | MAYBE BOOLEAN | s 2025(c)(8)(C)(ii) | snap5-s2025-c2 |
| `s 2025(c)(8)(C)(iii) the copy is provided in time to the chief executive officer and the legislature` | MAYBE BOOLEAN | s 2025(c)(8)(C)(iii) | snap5-s2025-c2 |
| `s 2025(c)(8)(I) the deadline as extended for cause shown` | DATE | s 2025(c)(8)(I) | snap5-s2025-c2 |
| `s 2025(c)(8)(I) the administrative law judge shall extend the deadline` | MAYBE BOOLEAN | s 2025(c)(8)(I) | snap5-s2025-c2 |
| `s 2025(c)(8)(D)(i) the notice of appeal is submitted in time` | MAYBE BOOLEAN | s 2025(c)(8)(D)(i) | snap5-s2025-c2 |
| `s 2025(c)(8)(D)(ii) the evidence in support of the appeal is submitted in time` | MAYBE BOOLEAN | s 2025(c)(8)(D)(ii) | snap5-s2025-c2 |
| `s 2025(c)(8)(E) the responsive evidence is submitted in time` | MAYBE BOOLEAN | s 2025(c)(8)(E) | snap5-s2025-c2 |
| `s 2025(c)(8)(F) the rebuttal evidence is submitted in time` | MAYBE BOOLEAN | s 2025(c)(8)(F) | snap5-s2025-c2 |
| `s 2025(c)(8)(G) the last day for the administrative law judge's decision` | DATE | s 2025(c)(8)(G) | snap5-s2025-c2 |
| `s 2025(c)(8)(G) the appeal is decided in time` | MAYBE BOOLEAN | s 2025(c)(8)(G) | snap5-s2025-c2 |
| `s 2025(c)(8)(H) the administrative law judge has considered what the text requires` | MAYBE BOOLEAN | s 2025(c)(8)(H) | snap5-s2025-c2 |
| `s 2025(c)(9) the circumstance is good cause` | MAYBE BOOLEAN | s 2025(c)(9) | snap5-s2025-c2 |
| `s 2025(c)(9)(C) the growth in the caseload is a significant growth` | MAYBE BOOLEAN | s 2025(c)(9)(C) | snap5-s2025-c2 |
| `s 2025(d)(1)(A) the guidance is issued in time` | MAYBE BOOLEAN | s 2025(d)(1)(A) | snap5-s2025-dfij |
| `s 2025(d)(1)(A) the guidance has the content required` | MAYBE BOOLEAN | s 2025(d)(1)(A) | snap5-s2025-dfij |
| `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` | MAYBE BOOLEAN | s 2025(d)(1)(B)(i) | snap5-s2025-dfij |
| `s 2025(d)(1)(B)(ii) the total amount of performance bonus payments for the fiscal year` | MAYBE NUMBER | s 2025(d)(1)(B)(ii) | snap5-s2025-dfij |
| `s 2025(d)(1)(B)(ii) the State agency shall be awarded a performance bonus payment` | MAYBE BOOLEAN | s 2025(d)(1)(B)(ii) | snap5-s2025-dfij |
| `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` | MAYBE BOOLEAN | s 2025(d)(2)(B)(i) | snap5-s2025-dfij |
| `s 2025(d)(2)(B)(ii) the total amount of performance bonus payments for the fiscal year` | MAYBE NUMBER | s 2025(d)(2)(B)(ii) | snap5-s2025-dfij |
| `s 2025(d)(2)(B)(ii) the State agency shall be awarded a performance bonus payment` | MAYBE BOOLEAN | s 2025(d)(2)(B)(ii) | snap5-s2025-dfij |
| `s 2025(d)(3) the State agency is eligible for a performance bonus payment for the fiscal year` | MAYBE BOOLEAN | s 2025(d)(3) | snap5-s2025-dfij |
| `s 2025(d)(4) the determination is subject to administrative or judicial review` | MAYBE BOOLEAN | s 2025(d)(4) | snap5-s2025-dfij |
| `s 2025(d)(5) the State agency may use the performance bonus payment for the use` | MAYBE BOOLEAN | s 2025(d)(5) | snap5-s2025-dfij |
| `s 2025(d)(6)(B) the Secretary may award performance bonus payments` | MAYBE BOOLEAN | s 2025(d)(6)(B) | snap5-s2025-dfij |
| `s 2025(e)(1) the household member has met the condition of eligibility of furnishing a social security account number` | MAYBE BOOLEAN | s 2025(e)(1) | snap5-s2025-dfij |
| `s 2025(e)(2) the account numbers are used in the administration of the program` | MAYBE BOOLEAN | s 2025(e)(2) | snap5-s2025-dfij |
| `s 2025(e) the Secretary and State agencies shall have access to the information` | MAYBE BOOLEAN | s 2025(e) | snap5-s2025-dfij |
| `s 2025(f) the expense may be paid` | MAYBE BOOLEAN | s 2025(f) | snap5-s2025-dfij |
| `s 2025(i)(1) the Department of Agriculture may use the information to determine which project areas have payment error rates that impair ...` | MAYBE BOOLEAN | s 2025(i)(1) | snap5-s2025-dfij |
| `s 2025(i)(2) the Secretary may require the State agency to carry out new or modified certification procedures` | MAYBE BOOLEAN | s 2025(i)(2) | snap5-s2025-dfij |
| `s 2025(j) the date by which the instructional materials are due` | MAYBE DATE | s 2025(j) | snap5-s2025-dfij |
| `s 2025(j) the instructional materials are published as required` | MAYBE BOOLEAN | s 2025(j) | snap5-s2025-dfij |
| `s 2025(c)(8)(D) to (G) a State agency appeals a payment claim` | DEONTIC `s 2025(c)(8) actor` `s 2025(c)(8) act` | s 2025(c)(8)(D) | snap5-s2025-duties |
| `s 2025(c)(8)(G)(ii) the administrative law judge decides when no rebuttal evidence is submitted` | DEONTIC `s 2025(c)(8) actor` `s 2025(c)(8) act` | s 2025(c)(8)(G)(ii) | snap5-s2025-duties |
| `s 2025(k)(2) the Secretary of Health and Human Services makes the determinations` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(2) | snap5-s2025-duties |
| `s 2025(k)(4)(A) the Secretary notifies the chief executive officer of the State` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(4)(A) | snap5-s2025-duties |
| `s 2025(k)(4)(B)(i) the State appeals to an administrative law judge` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(4)(B)(i) | snap5-s2025-duties |
| `s 2025(k)(4)(B)(iv) the administrative law judge decides and notifies` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(4)(B)(iv) | snap5-s2025-duties |
| `s 2025(k)(4)(C)(i) the State appeals to the Departmental Appeals Board` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(4)(C)(i) | snap5-s2025-duties |
| `s 2025(k)(4)(C)(iii) the Board decides and notifies` | DEONTIC `s 2025(k) actor` `s 2025(k) act` | s 2025(k)(4)(C)(iii) | snap5-s2025-duties |
| `s 2028(b)(1)(A) the Commonwealth submits a plan` | DEONTIC `s 2028(b) actor` `s 2028(b) act` | s 2028(b)(1)(A) | snap5-s2025-duties |
| `s 2028(b)(1)(B)(i) the Secretary approves or disapproves the plan` | DEONTIC `s 2028(b) actor` `s 2028(b) act` | s 2028(b)(1)(B)(i) | snap5-s2025-duties |
| `s 2028(b)(2)(A) the Commonwealth reports the findings of the audit` | DEONTIC `s 2028(b) actor` `s 2028(b) act` | s 2028(b)(2)(A) | snap5-s2025-duties |
| `s 2028(b)(2)(B) the Commonwealth provides the Secretary with a statement` | DEONTIC `s 2028(b) actor` `s 2028(b) act` | s 2028(b)(2)(B) | snap5-s2025-duties |
| `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` | MAYBE BOOLEAN | s 2025(g)(1)(A) | snap5-s2025-gh |
| `s 2025(g)(1)(A)(v) the system would be tested adequately before and after implementation` | MAYBE BOOLEAN | s 2025(g)(1)(A)(v) | snap5-s2025-gh |
| `s 2025(g)(1)(A)(vi) the system would be operated in accordance with an adequate plan` | MAYBE BOOLEAN | s 2025(g)(1)(A)(vi) | snap5-s2025-gh |
| `s 2025(g)(1)(B) the operation of the system qualifies for payment` | MAYBE BOOLEAN | s 2025(g)(1)(B) | snap5-s2025-gh |
| `s 2025(g)(2) the costs on which the Secretary may make payments after the limitation` | NUMBER | s 2025(g)(2) | snap5-s2025-gh |
| `s 2025(g)(1) the amount the Secretary is authorized to pay for the costs` | MAYBE NUMBER | s 2025(g)(1) | snap5-s2025-gh |
| `s 2025(h)(1)(A) the amount the Secretary shall reserve for each fiscal year, in dollars` | NUMBER | s 2025(h)(1)(A) | snap5-s2025-gh |
| `s 2025(h)(1)(A) the last day the funds remain available` | DATE | s 2025(h)(1)(A) | snap5-s2025-gh |
| `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` | MAYBE BOOLEAN | s 2025(h)(1)(B) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(i) the unexpended funds the Secretary shall reallocate to other States` | MAYBE NUMBER | s 2025(h)(1)(C)(i) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(ii) the reallocation allows the State agency the time required` | MAYBE BOOLEAN | s 2025(h)(1)(C)(ii) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iii) every State agency has had an opportunity to obtain reallocated funds` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iii) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(I) the amount reallocated under subclause (I) meets the minimum` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(I) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(I)(bb) the determination is based on what the text requires` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(I)(bb) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to the evaluation of subparagraph (F)(vii)` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(I)(cc) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to monitoring under paragraph (5)` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(I)(cc) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(II) the amount reallocated under subclause (II) meets the minimum` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(II) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(II) the group is one the programs and activities are targeted to` | MAYBE BOOLEAN | s 2025(h)(1)(C)(iv)(II) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(iv)(III) the remaining funds to be reallocated` | NUMBER | s 2025(h)(1)(C)(iv)(III) | snap5-s2025-gh |
| `s 2025(h)(1)(C)(v) the State agency may also be considered for funding under clause (iv)(II)` | MAYBE BOOLEAN | s 2025(h)(1)(C)(v) | snap5-s2025-gh |
| `s 2025(h)(1)(D) the allocation meets the minimum` | MAYBE BOOLEAN | s 2025(h)(1)(D) | snap5-s2025-gh |
| `s 2025(h)(1)(E)(i) the additional allocation is within the limit` | MAYBE BOOLEAN | s 2025(h)(1)(E)(i) | snap5-s2025-gh |
| `s 2025(h)(1)(E)(i) the costs of serving the member may be reimbursed from the additional allocation` | MAYBE BOOLEAN | s 2025(h)(1)(E)(i) | snap5-s2025-gh |
| `s 2025(h)(1)(E)(ii) the State agency is eligible for an additional allocation` | MAYBE BOOLEAN | s 2025(h)(1)(E)(ii) | snap5-s2025-gh |
| `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant or recipient` | MAYBE BOOLEAN | s 2025(h)(1)(E)(ii) | snap5-s2025-gh |
| `s 2025(h)(2) the amount the Secretary shall pay for the additional costs` | MAYBE NUMBER | s 2025(h)(2) | snap5-s2025-gh |
| `s 2025(h)(3) the most the reimbursement for dependent care expenses may be` | NUMBER | s 2025(h)(3) | snap5-s2025-gh |
| `s 2025(h)(3) the amount the Secretary shall reimburse the State agency` | NUMBER | s 2025(h)(3) | snap5-s2025-gh |
| `s 2025(h)(3) the reimbursement may be made out of funds allocated under paragraph (1)` | MAYBE BOOLEAN | s 2025(h)(3) | snap5-s2025-gh |
| `s 2025(h)(4) the funds may be used for the use` | MAYBE BOOLEAN | s 2025(h)(4) | snap5-s2025-gh |
| `s 2025(h)(5)(A) the Secretary has monitored and assessed as required` | MAYBE BOOLEAN | s 2025(h)(5)(A) | snap5-s2025-gh |
| `s 2025(h)(5)(B) the State reporting measures are as required` | MAYBE BOOLEAN | s 2025(h)(5)(B) | snap5-s2025-gh |
| `s 2025(h)(5)(B)(iii) the threshold the Secretary determines is allowed` | MAYBE BOOLEAN | s 2025(h)(5)(B)(iii) | snap5-s2025-gh |
| `s 2025(h)(5)(B)(iii) the State employment and training plan must identify reporting measures for the component` | MAYBE BOOLEAN | s 2025(h)(5)(B)(iii) | snap5-s2025-gh |
| `s 2025(h)(5)(B)(iv) the reporting measure may be included` | MAYBE BOOLEAN | s 2025(h)(5)(B)(iv) | snap5-s2025-gh |
| `s 2025(h)(5)(B)(v) the State agency may report the data to demonstrate the number of participants served` | MAYBE BOOLEAN | s 2025(h)(5)(B)(v) | snap5-s2025-gh |
| `s 2025(h)(5)(C) the Secretary has assessed the State programs as required` | MAYBE BOOLEAN | s 2025(h)(5)(C) | snap5-s2025-gh |
| `s 2025(h)(5)(C)(iv) the Secretary may require the information` | MAYBE BOOLEAN | s 2025(h)(5)(C)(iv) | snap5-s2025-gh |
| `s 2025(h)(5)(D) the State agency has reported as required` | MAYBE BOOLEAN | s 2025(h)(5)(D) | snap5-s2025-gh |
| `s 2025(h)(5)(E) the Secretary may require the State agency to modify the plan` | MAYBE BOOLEAN | s 2025(h)(5)(E) | snap5-s2025-gh |
| `s 2025(h)(5)(F) the study is conducted in time` | MAYBE BOOLEAN | s 2025(h)(5)(F) | snap5-s2025-gh |
| `s 2025(h)(5)(F) the study covers what the text requires` | MAYBE BOOLEAN | s 2025(h)(5)(F) | snap5-s2025-gh |
| `s 2025(h)(1)(F)(i)(I) the Secretary has carried out the pilot projects as required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(i)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` | MAYBE BOOLEAN | s 2025(h)(1)(F)(i)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ii)(I) the Secretary has selected the pilot project as required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ii)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ii)(II) the State agency meets the qualifying criteria` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ii)(II)(cc) the commitment is at least the amount expended for fiscal year 2013` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ii)(II)(cc) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selecting the pilot project` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ii)(III) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ii)(III)(ee) the Secretary has ensured that the group of pilot projects tests the strategies` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ii)(III)(ee) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iii)(I) the Secretary has established and implemented the termination process` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iii)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iii)(II) the time period allowed to correct the noncompliance is as required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv) the program or service is allowable` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(I) the activity is employment in the public or private sector that is not subsidized` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(II) the activity is subsidized employment in the private sector` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(III) the activity is subsidized employment in the public sector` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(III) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(IV) the activity is a work activity of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(IV) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(V) the activity is training of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(V) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(VI) the activity is job search, obtaining employment, or preparation of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(VI) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(VII) the activity is a structured program or embedded activity of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(VII) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(VIII) the activity is a career and technical training program of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(VIII) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(IX) the activity is training or education for job skills of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(IX) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(X) the activity is education of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(X) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(XI) the activity is regular attendance of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(XI) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(iv)(XII) the activity is providing child care of the kind described` | MAYBE BOOLEAN | s 2025(h)(1)(F)(iv)(XII) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vi)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vi)(II) the Secretary has established the standards` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vi)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` | MAYBE BOOLEAN | s 2025(h)(1)(F)(v) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vi)(I) the activities are considered to be carried out under section 2015(d)` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vi)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vi)(III) the State agency complied before assigning the work registrant to mandatory activities` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vi)(III) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(I) the Secretary has conducted the independent evaluation as required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(I)(aa) the reporting of results is frequent enough` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(I)(aa) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(I)(cc) the evaluation uses the methodology required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(I)(cc) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(II) the report is submitted in time` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(II) the report is submitted and shared as required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(vii)(II) the report describes what is required` | MAYBE BOOLEAN | s 2025(h)(1)(F)(vii)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(viii)(I) the amount the Secretary shall use to carry out the subparagraph for the fiscal year` | MAYBE NUMBER | s 2025(h)(1)(F)(viii)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(viii)(II)(aa) the number of funded pilot projects is within the limit` | MAYBE BOOLEAN | s 2025(h)(1)(F)(viii)(II)(aa) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(viii)(II)(bb) the pilot project is in effect for no more than the limit` | MAYBE BOOLEAN | s 2025(h)(1)(F)(viii)(II)(bb) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(viii)(III) the funds remain available on the date` | MAYBE BOOLEAN | s 2025(h)(1)(F)(viii)(III) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ix)(I) the funds may be used for the use` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ix)(I) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ix)(II) the funds are used as the text allows` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ix)(II) | snap5-s2025-hf |
| `s 2025(h)(1)(F)(ix)(III) the State may contribute the additional funds` | MAYBE BOOLEAN | s 2025(h)(1)(F)(ix)(III) | snap5-s2025-hf |
| `s 2025(k)(1)(A) the program is the AFDC program` | MAYBE BOOLEAN | s 2025(k)(1)(A) | snap5-s2025-k |
| `s 2025(k)(1)(B) the period is the base period` | MAYBE BOOLEAN | s 2025(k)(1)(B) | snap5-s2025-k |
| `s 2025(k)(1)(C) the program is the medicaid program` | MAYBE BOOLEAN | s 2025(k)(1)(C) | snap5-s2025-k |
| `s 2025(k)(2) the date by which the Secretary of Health and Human Services must make the determinations` | DATE | s 2025(k)(2) | snap5-s2025-k |
| `s 2025(k)(2) the determinations are made as required` | MAYBE BOOLEAN | s 2025(k)(2) | snap5-s2025-k |
| `s 2025(k)(2)(B) the amount of common costs allocated to each program when allocated equally` | MAYBE NUMBER | s 2025(k)(2)(B) | snap5-s2025-k |
| `s 2025(k)(3)(A) the amount paid to the State after the reduction` | MAYBE NUMBER | s 2025(k)(3)(A) | snap5-s2025-k |
| `s 2025(k)(3)(A) the reductions are made on a quarterly basis as required` | MAYBE BOOLEAN | s 2025(k)(3)(A) | snap5-s2025-k |
| `s 2025(k)(3)(B) the determinations were not made by September 30, 1999` | MAYBE BOOLEAN | s 2025(k)(3)(B) | snap5-s2025-k |
| `s 2025(k)(3)(B)(i) the amount of the reduction in the fiscal year in which the determinations are made` | MAYBE NUMBER | s 2025(k)(3)(B)(i) | snap5-s2025-k |
| `s 2025(k)(3)(B)(ii) subparagraph (A) applies in the fiscal year` | MAYBE BOOLEAN | s 2025(k)(3)(B)(ii) | snap5-s2025-k |
| `s 2025(k)(4)(A) the last day for the Secretary to notify the chief executive officer of the State` | DATE | s 2025(k)(4)(A) | snap5-s2025-k |
| `s 2025(k)(4)(A) the Secretary notifies the chief executive officer in time` | MAYBE BOOLEAN | s 2025(k)(4)(A) | snap5-s2025-k |
| `s 2025(k)(4)(B)(i) the last day for the State to appeal to an administrative law judge` | DATE | s 2025(k)(4)(B)(i) | snap5-s2025-k |
| `s 2025(k)(4)(B)(i) the State may appeal the determination` | MAYBE BOOLEAN | s 2025(k)(4)(B)(i) | snap5-s2025-k |
| `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` | MAYBE BOOLEAN | s 2025(k)(4)(B) | snap5-s2025-k |
| `s 2025(k)(4)(B)(iv) the last day for the administrative law judge to decide and notify` | DATE | s 2025(k)(4)(B)(iv) | snap5-s2025-k |
| `s 2025(k)(4)(B)(iv) the administrative law judge decides and notifies in time` | MAYBE BOOLEAN | s 2025(k)(4)(B)(iv) | snap5-s2025-k |
| `s 2025(k)(4)(C)(i) the last day for the State to appeal to the Departmental Appeals Board` | DATE | s 2025(k)(4)(C)(i) | snap5-s2025-k |
| `s 2025(k)(4)(C)(i) the State may appeal the decision` | MAYBE BOOLEAN | s 2025(k)(4)(C)(i) | snap5-s2025-k |
| `s 2025(k)(4)(C)(ii) the Board has reviewed the decision as required` | MAYBE BOOLEAN | s 2025(k)(4)(C)(ii) | snap5-s2025-k |
| `s 2025(k)(4)(C)(iii) the last day for the Board to decide and notify` | DATE | s 2025(k)(4)(C)(iii) | snap5-s2025-k |
| `s 2025(k)(4)(C)(iii) the Board decides and notifies in time` | MAYBE BOOLEAN | s 2025(k)(4)(C)(iii) | snap5-s2025-k |
| `s 2025(k)(4)(D) the determination or decision is subject to judicial review` | MAYBE BOOLEAN | s 2025(k)(4)(D) | snap5-s2025-k |
| `s 2025(k)(4)(E) the pendency of the appeal affects the requirement that the Secretary reduce payments` | MAYBE BOOLEAN | s 2025(k)(4)(E) | snap5-s2025-k |
| `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` | MAYBE BOOLEAN | s 2025(k)(5) | snap5-s2025-k |
| `s 2026a(a) the product is fluid milk` | MAYBE BOOLEAN | s 2026a(a) | snap5-s2026a |
| `s 2026a(b) the project is a healthy fluid milk incentive project the Secretary is to carry out` | MAYBE BOOLEAN | s 2026a(b) | snap5-s2026a |
| `s 2026a(c)(1) the Secretary shall enter into the agreement with, or provide the grant to, the entity` | MAYBE BOOLEAN | s 2026a(c)(1) | snap5-s2026a |
| `s 2026a(c)(2) the entity has met the application requirement` | MAYBE BOOLEAN | s 2026a(c)(2) | snap5-s2026a |
| `s 2026a(c)(3) the projects are evaluated against the required criteria` | MAYBE BOOLEAN | s 2026a(c)(3) | snap5-s2026a |
| `s 2026a(c)(4) the funds made available under this section may be used for the project` | MAYBE BOOLEAN | s 2026a(c)(4) | snap5-s2026a |
| `s 2026a(d)(1)(A)(i) the evaluation is the independent evaluation required` | MAYBE BOOLEAN | s 2026a(d)(1)(A)(i) | snap5-s2026a |
| `s 2026a(d)(1)(A)(ii) the evaluation meets the requirement of rigorous methodologies` | MAYBE BOOLEAN | s 2026a(d)(1)(A)(ii) | snap5-s2026a |
| `s 2026a(d)(1)(B) the amount used for evaluation is within the limit` | MAYBE BOOLEAN | s 2026a(d)(1)(B) | snap5-s2026a |
| `s 2026a(d)(2) the date by which the report is due in the year` | MAYBE DATE | s 2026a(d)(2) | snap5-s2026a |
| `s 2026a(d)(2) the report is submitted in time` | MAYBE BOOLEAN | s 2026a(d)(2) | snap5-s2026a |
| `s 2026a(d)(2) the report describes the matters required` | MAYBE BOOLEAN | s 2026a(d)(2) | snap5-s2026a |
| `s 2026a(d)(3) the evaluation results are shared as required` | MAYBE BOOLEAN | s 2026a(d)(3) | snap5-s2026a |
| `s 2026a(e)(1) the amount authorized to be appropriated, in dollars` | NUMBER | s 2026a(e)(1) | snap5-s2026a |
| `s 2026a(e)(2) the funds are available to carry out this section` | MAYBE BOOLEAN | s 2026a(e)(2) | snap5-s2026a |
| `s 2028(a)(1) the place is a governmental entity` | MAYBE BOOLEAN | s 2028(a)(1) | snap5-s2028 |
| `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` | MAYBE NUMBER | s 2028(a)(2)(A) | snap5-s2028 |
| `s 2028(a)(2)(B)(i) the Commonwealth's share of the funds` | MAYBE NUMBER | s 2028(a)(2)(B)(i) | snap5-s2028 |
| `s 2028(a)(2)(B)(i) the payment toward the Commonwealth's expenditures and administrative expenses` | NUMBER | s 2028(a)(2)(B)(i) | snap5-s2028 |
| `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` | MAYBE BOOLEAN | s 2028(a)(2)(B)(ii) | snap5-s2028 |
| `s 2028(a)(2)(C) American Samoa's share of the funds` | MAYBE NUMBER | s 2028(a)(2)(C) | snap5-s2028 |
| `s 2028(a)(2)(C) the payment toward American Samoa's expenditures` | MAYBE NUMBER | s 2028(a)(2)(C) | snap5-s2028 |
| `s 2028(a)(2)(D) the carryover is within the limit` | MAYBE BOOLEAN | s 2028(a)(2)(D) | snap5-s2028 |
| `s 2028(a)(3) the payment to the Commonwealth for the fiscal year` | MAYBE NUMBER | s 2028(a)(3) | snap5-s2028 |
| `s 2028(b)(1) the Commonwealth may receive payments` | MAYBE BOOLEAN | s 2028(b)(1) | snap5-s2028 |
| `s 2028(b)(1)(A) the plan is submitted in time` | MAYBE BOOLEAN | s 2028(b)(1)(A) | snap5-s2028 |
| `s 2028(b)(1)(A) the plan has the required contents` | MAYBE BOOLEAN | s 2028(b)(1)(A) | snap5-s2028 |
| `s 2028(b)(1)(B)(i) the Secretary's decision on the plan is in time` | MAYBE BOOLEAN | s 2028(b)(1)(B)(i) | snap5-s2028 |
| `s 2028(b)(1)(B)(i) the Secretary shall approve the plan` | MAYBE BOOLEAN | s 2028(b)(1)(B)(i) | snap5-s2028 |
| `s 2028(b)(1)(B)(i) payments may be made for the fiscal year of the plan` | MAYBE BOOLEAN | s 2028(b)(1)(B)(i) | snap5-s2028 |
| `s 2028(b)(1)(B)(ii) the withheld payments are to be paid` | MAYBE BOOLEAN | s 2028(b)(1)(B)(ii) | snap5-s2028 |
| `s 2028(b)(2)(A) the last day for the report of the audit findings` | DATE | s 2028(b)(2)(A) | snap5-s2028 |
| `s 2028(b)(2)(A) the report of the audit findings is in time` | MAYBE BOOLEAN | s 2028(b)(2)(A) | snap5-s2028 |
| `s 2028(b)(2)(A) the audit is biennial` | MAYBE BOOLEAN | s 2028(b)(2)(A) | snap5-s2028 |
| `s 2028(b)(2)(B) the statement is provided in time` | MAYBE BOOLEAN | s 2028(b)(2)(B) | snap5-s2028 |
| `s 2028(b)(2)(B) the statement has the required contents` | MAYBE BOOLEAN | s 2028(b)(2)(B) | snap5-s2028 |
| `s 2028(b)(2)(C)(i) further payments may be made` | MAYBE BOOLEAN | s 2028(b)(2)(C)(i) | snap5-s2028 |
| `s 2028(b)(2)(C)(ii) the withheld payments are to be paid` | MAYBE BOOLEAN | s 2028(b)(2)(C)(ii) | snap5-s2028 |
| `s 2028(b)(2)(C)(iii) the Secretary may refer the matter to the Attorney General` | MAYBE BOOLEAN | s 2028(b)(2)(C)(iii) | snap5-s2028 |
| `s 2028(b)(2)(C)(iii) appropriate injunctive relief shall issue` | MAYBE BOOLEAN | s 2028(b)(2)(C)(iii) | snap5-s2028 |
| `s 2028(c)(1) the Secretary shall provide for the review of the program` | MAYBE BOOLEAN | s 2028(c)(1) | snap5-s2028 |
| `s 2028(c)(2) the Secretary may provide technical assistance` | MAYBE BOOLEAN | s 2028(c)(2) | snap5-s2028 |
| `s 2028(d) the conduct is within the offence` | MAYBE BOOLEAN | s 2028(d) | snap5-s2028 |
| `s 2028(d) the most the person may be fined, in dollars` | MAYBE NUMBER | s 2028(d) | snap5-s2028 |
| `s 2028(d) the longest term of imprisonment, in years` | MAYBE NUMBER | s 2028(d) | snap5-s2028 |
| `s 2028(e)(1) the review includes the required examinations` | MAYBE BOOLEAN | s 2028(e)(1) | snap5-s2028 |
| `s 2028(e)(2) the last day for the report` | DATE | s 2028(e)(2) | snap5-s2028 |
| `s 2028(e)(2) the report is in time` | MAYBE BOOLEAN | s 2028(e)(2) | snap5-s2028 |
| `s 2028(e)(3)(A) the largest share of a participant's benefit a plan may distribute in cash` | MAYBE NUMBER | s 2028(e)(3)(A) | snap5-s2028 |
| `s 2028(e)(3)(A) the Secretary shall disapprove the plan` | MAYBE BOOLEAN | s 2028(e)(3)(A) | snap5-s2028 |
| `s 2028(e)(3)(B) the Secretary may approve a plan that exempts participants or categories of participants` | MAYBE BOOLEAN | s 2028(e)(3)(B) | snap5-s2028 |
| `s 2028(e)(4) the amount to make available for the review and report` | MAYBE NUMBER | s 2028(e)(4) | snap5-s2028 |
