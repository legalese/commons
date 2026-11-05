#!/usr/bin/env python3
"""The coverage table and the jural-relations table of this encoding, built from the text and from the .l4 files.

The ROWS block below is the one place where the provisions of the Retirement and Re-employment Act 1993 are listed, with
the lines of RRA1993.txt each one occupies, its disposition, and (for rows that create a Hohfeld relation) who holds the
right, privilege, power or immunity and who bears the correlative duty, no-right, liability or disability.  The rules
that encode a row are NOT typed here: they are found in the .l4 files, as the definitions whose backtick name begins with
the row's citation (`s 4(2) ...`), so the table cannot claim a rule that does not exist.

  python3 -I coverage.py audit  RAW           every non-blank line of RAW falls in some row; counts per disposition;
                                              every `encoded` or `fork` row has a rule; every `s ...` rule has a row
  python3 -I coverage.py write  RAW NOTES.md  rewrite the two generated blocks of NOTES.md (between the BEGIN/END markers)

Row syntax, one row per line, fields separated by ` ; `:
    cite ; lines ; disposition ; jural ; label
  lines        N-M, or several such separated by commas
  disposition  E           encoded: the rules whose names begin with the cite
               E>other     encoded by the rules whose names begin with `other` (a paragraph row inside a subsection rule)
               F:F3,F7     fork: encoded, and the reading chosen is in the fork register under these ids
               I1 I2       inert, reason 1 (not operative) or 2 (machinery), with a short why after a colon: I2:short title
               X           repealed or blank in this text: what the text shows follows the colon: X:[Repealed by Act 5 of 2017]
  jural        `Holder: kind > Bearer: kind`, or `-` for a provision that creates no such relation
"""
import os, re, sys

ROWS = r"""
front: title ; 1-17 ; I1:title, edition banner and publication notes ; - ; Title, edition banner and publication notes
front: arrangement ; 19-91 ; I1:the Arrangement of Sections is a table of contents ; - ; Arrangement of Sections
front: long title ; 93-95 ; I1:long title creates no rule ; - ; Long title
front: commencement ; 97 ; I2:the Act's own commencement date ; - ; [1 July 1993]
Part 1: headings ; 99-101,104,238 ; I1:part title and section headings ; - ; Part 1 title and the headings Short title, Interpretation, Officers
s 1 ; 102 ; I2:short title ; - ; Short title
s 2(1) ; 105 ; E ; - ; Interpretation: "unless the context otherwise requires"
s 2(1) "agreed date" ; 106-108 ; E ; - ; "agreed date" means a date specified for the purposes of section 7C(2)(a) in a consent form
s 2(1) "approved mediator" ; 115-117 ; E ; - ; "approved mediator" has the meaning given by the Employment Claims Act 2016
s 2(1) "claim referral certificate" ; 115-117 ; E ; - ; "claim referral certificate" has the meaning given by the Employment Claims Act 2016
s 2(1) "collective agreement" ; 119-120 ; E ; - ; "collective agreement" has the meaning given by the Industrial Relations Act 1960
s 2(1) "Commissioner" ; 122-123 ; E ; - ; "Commissioner" means the Commissioner for Labour
s 2(1) "contract of service" ; 125-128 ; E ; - ; "contract of service" means any agreement, written or oral, express or implied, to employ and serve as an employee
s 2(1) "eligible employee" ; 130-131 ; E ; - ; "eligible employee" means an employee who satisfies the criteria in section 7(1)
s 2(1) "employee" ; 133-134 ; E ; - ; "employee" means a person who has entered into or works under a contract of service
s 2(1) "employer" ; 136-138 ; F:F4 ; - ; "employer" means a person who employs another under a contract of service and includes
s 2(1) "employer" (a) ; 139 ; E>s 2(1) "employer" ; - ; "employer" includes (a) the Government
s 2(1) "employer" (b) ; 141 ; E>s 2(1) "employer" ; - ; "employer" includes (b) any statutory authority
s 2(1) "employer" (c) ; 143-144 ; E>s 2(1) "employer" ; - ; "employer" includes (c) any duly authorised agent or manager of any employer
s 2(1) "employer" (d) ; 146-149 ; E>s 2(1) "employer" ; - ; "employer" includes (d) any person who owns, carries on or is responsible for managing or controlling a profession, business, trade or work
s 2(1) "employment assistance payment" ; 151-153 ; E ; - ; "employment assistance payment" means a sum payable by an employer to an eligible employee under section 7C(1)
s 2(1) "Employment Claims Tribunal" ; 155-157 ; E ; - ; "Employment Claims Tribunal" means a Tribunal constituted under section 4 of the State Courts Act 1970
s 2(1) "investigating officer" ; 159-160 ; E ; - ; "investigating officer" means a person appointed under section 3
s 2(1) "mediation request" ; 167-168 ; E ; - ; "mediation request" has the meaning given by the Employment Claims Act 2016
s 2(1) "prescribed minimum retirement age" ; 170-173 ; E ; - ; "prescribed minimum retirement age" means the age specified under section 4(1) applicable to the employee
s 2(1) "prescribed re-employment age" ; 177-179 ; E ; - ; "prescribed re-employment age" means the age specified under section 7A(11) applicable to the employee
s 2(1) "re-employment" ; 183-185 ; E ; - ; "re-employment" means employment by the same employer on or after the date the employee attains the specified age
s 2(1) "re-employment contract" ; 189-192 ; E ; - ; "re-employment contract" means a contract of service entered into with an eligible employee for section 7A(1) or (3)(a)(i)
s 2(1) "re-employment obligations" ; 194-198 ; E ; - ; "re-employment obligations" means an employer's obligations to re-employ under section 7A, failing which to offer an employment assistance payment
s 2(1) "salary" ; 200-201 ; E ; - ; "salary" has the meaning given by the Employment Act 1968
s 2(1) "specified age" ; 203-204 ; E ; - ; "specified age" means the higher of the following ages
s 2(1) "specified age" (a) ; 206 ; E>s 2(1) "specified age" ; - ; "specified age" (a) the employee's prescribed minimum retirement age
s 2(1) "specified age" (b) ; 208-209 ; E>s 2(1) "specified age" ; - ; "specified age" (b) the retirement age stipulated in the employee's contract of service
s 2(1) "tripartite guidelines" ; 218-219 ; E ; - ; "tripartite guidelines" means the guidelines relating to re-employment issued by the Minister under section 11B
s 2(2) ; 223-224 ; F:F16 ; Employee: immunity > Employer: disability ; Treated as dismissed
s 2(2)(a) ; 226-228 ; E>s 2(2) ; - ; treated as dismissed if the contract is terminated by the employer, by notice or without notice
s 2(2)(b) ; 230-231 ; E>s 2(2) ; - ; treated as dismissed if the employer retires the employee, or requires or causes the employee to retire or resign on the ground of age
s 2(3) ; 233-236 ; F:F1,F2 ; - ; A person is regarded as attaining an age on or after the Nth anniversary of birth
s 3(1) ; 240-241 ; I2:the officer in charge of the general administration of the Act ; - ; The Commissioner for Labour is the officer in charge
s 3(2) ; 243-250 ; E ; Deputy and assistant commissioners: power > Persons affected: liability ; Deputy and Assistant Commissioners may perform the Commissioner's duties
s 3(3) ; 252-254 ; I2:the Minister's power to appoint investigating officers is staffing ; - ; The Minister may appoint investigating officers and other officers
s 3(4) ; 258-259 ; I2:rule-making power ; - ; The Minister may make rules for the conduct of officers' duties
Part 2: headings ; 266-270,272,297 ; I1:part title, amendment note and section headings ; - ; Part 2 title, and the headings Prescribed minimum retirement age and Invalidity of term of contract of service
s 4(1) ; 274-277 ; E ; - ; The Minister may specify the prescribed minimum retirement age, at least 62 but not more than 65
s 4(2) ; 281-284 ; E ; Employee: claim > Employer: duty ; Despite any other written law, an employer must not dismiss an employee on the ground of age before the prescribed minimum retirement age
s 4(3) ; 288-291 ; E ; State: claim > Employer: duty ; Offence: fine up to $5,000, or imprisonment up to 6 months, or both
s 5 ; 295 ; X:[Repealed by Act 5 of 2017] ; - ; [Repealed by Act 5 of 2017]
s 6 ; 299-302 ; E ; Employee: immunity > Employer: disability ; A term providing a retirement age below the prescribed minimum retirement age is void to that extent
Part 3: headings ; 306-308,339,458-459,501 ; I1:part title and section headings ; - ; Part 3 title, and the headings of ss 7, 7A, 7B and 7C
s 7(1) ; 309-310 ; E ; Employee: claim > Employer: duty ; An employee is eligible for re-employment in accordance with section 7A if
s 7(1)(a) ; 311 ; E ; - ; (a) the employee is born on or after 1 July 1952
s 7(1)(b) ; 318 ; E>s 7(1) ; - ; (b) the employer assesses the employee as
s 7(1)(b)(i) ; 320 ; E>s 7(1) ; - ; (i) having at least satisfactory work performance
s 7(1)(b)(ii) ; 322 ; F:F5 ; Employee: immunity > Employer: disability ; (ii) being medically fit to continue working
s 7(2) ; 326-329 ; F:F5 ; Employee: immunity > Employer: liability ; Presumption of medical fitness unless the employer proves otherwise on a balance of probabilities
s 7(3) ; 331-335 ; E ; Employee: claim > Employer: duty ; Written notice of an intention not to re-employ
s 7A(1) ; 341-346 ; F:F6,F7,F19 ; Employee: claim > Employer: duty ; Subject to section 7C, offer re-employment before the specified age; obligation to re-employ until the prescribed re-employment age
s 7A(2) ; 352-352 ; E ; - ; Where
s 7A(2)(a) ; 354-356 ; E>s 7A(2) ; - ; (a) an employee mentioned in section 7(1)(a) continues, after attaining the specified age, to work
s 7A(2)(b) ; 358-363 ; E>s 7A(2) ; - ; (b) the employer neither re-employs nor terminates the employment
s 7A(2) effect ; 365-366,373-374 ; E>s 7A(2) ; Employee: immunity > Employer: disability ; then rights acquired, accrued or incurred before the specified age are not affected
s 7A(3) ; 378-379 ; E ; Employer: privilege > Employee: no-right ; Where subsection (2) applies, the employer
s 7A(3)(a) ; 381-382 ; E>s 7A(3) ; - ; (a) may at any time after the specified age
s 7A(3)(a)(i) ; 384 ; E>s 7A(3) ; Employer: privilege > Employee: no-right ; (i) re-employ the employee
s 7A(3)(a)(ii) ; 386-388 ; F:F20>s 7A(3) ; Employer: power > Employee: liability ; (ii) terminate the employment if the employee does not satisfy section 7(1)(b)
s 7A(3)(b) ; 390-397 ; F:F17>s 7A(3) ; Employer: immunity > Employee: disability ; (b) is deemed to have complied with subsection (1) for the period until it re-employs or terminates
s 7A(4) ; 401-405 ; E ; Employer: power > Employee: liability ; A re-employment contract must be entered into; job scope and terms may vary
s 7A(5) ; 409-412 ; E ; Employee: claim > Employer: duty ; A variation must be based on reasonable factors
s 7A(6) ; 414-416 ; F:F8,F18 ; Employee: claim > Employer: duty ; Unless otherwise agreed, the period stipulated must not be less than one year at any one time
s 7A(7) ; 420-423,430-431,433-434 ; E ; Employer: privilege > Employee: no-right ; Despite subsection (6), a shorter period where less than one year remains to the prescribed re-employment age
s 7A(8) ; 440 ; X:[Deleted by Act 5 of 2017] ; - ; [Deleted by Act 5 of 2017]
s 7A(9) ; 442-445 ; E ; Eligible employee and employer: privilege > Each: no-right ; Despite the Act, an eligible employee may retire or be retired if he or she does not wish to be employed
s 7A(10) ; 447-450 ; E ; Employer: claim > Eligible employee: duty ; An eligible employee who intends to retire must, insofar as reasonably practicable, give written notice
s 7A(11) ; 452-454 ; E ; - ; The Minister may specify the prescribed re-employment age, at least 67 but not more than 70
s 7B(1) ; 461-470 ; F:F8 ; Employer: immunity > Employee: disability ; Previous service is disregarded, unless otherwise agreed and subject to subsections (2) and (3)
s 7B(2) ; 474-483 ; E ; Employee: claim > Employer: duty ; Previous service is reckoned for the purposes of
s 7B(2)(a) ; 485-487 ; E>s 7B(2) ; - ; (a) computing the minimum period of 3 months for entitlement to annual leave
s 7B(2)(b) ; 489-491 ; E>s 7B(2) ; - ; (b) determining the period of service for entitlement to paid sick leave
s 7B(3) ; 495-497 ; E ; Employee: immunity > Employer: disability ; Continuity of employment is not broken on re-employment or renewal
s 7C(1) ; 503-508 ; F:F9 ; Employer: immunity > Employee: disability ; Section 7A does not apply if E1 cannot find a suitable vacancy despite reasonable attempts, and
s 7C(1)(a) ; 510-511 ; E>s 7C(1) ; - ; (a) E1 offers an employment assistance payment
s 7C(1)(b) ; 513 ; E>s 7C(1) ; - ; (b) during the employee's employment with E1
s 7C(1)(b)(i) ; 515-516 ; E>s 7C(1) ; - ; (i) another employer E2 offers to employ the eligible employee in lieu of E1
s 7C(1)(b)(ii) ; 518 ; E>s 7C(1) ; - ; (ii) the eligible employee accepts the offer
s 7C(2) ; 522-523 ; E ; - ; Subject to prescribed modifications, where subsection (1)(b) applies
s 7C(2)(a) ; 525-526 ; F:F10>s 7C(2) ; Employee: immunity > Employer E1: disability ; (a) E1's re-employment obligations are discharged immediately before the agreed date
s 7C(2)(b) ; 528-530 ; E>s 7C(2) ; Employee: claim > Employer E2: duty ; (b) a reference to an employer includes E2 from the agreed date
s 7C(2)(c) ; 537-540 ; E>s 7C(2) ; Employee: claim > Employer E1: duty ; (c) E1's re-employment obligations survive an unlawful dismissal by E1 before the agreed date, to the extent of (a) and (b)
s 7C(3) ; 544-548 ; E ; Employer: immunity > Employee: disability ; Despite subsection (1)(a), no employment assistance payment is required for an employee who decides not to continue
s 7C(4) ; 552-553 ; F:F11 ; Employee: claim > Employer: duty ; Subject to subsection (5), the employment assistance payment is
s 7C(4)(a) ; 555-556 ; F:F11>s 7C(4) ; Employee: claim > Employer: duty ; (a) a single lump sum payment paid by the last day of employment
s 7C(4)(b) ; 558 ; E>s 7C(4) ; - ; (b) other mutually agreed arrangements
s 7C(5) ; 560-562 ; E ; Employee: claim > Employer: duty ; In determining the amount, the employer must take the tripartite guidelines into account
s 7C(6) ; 564-568 ; E ; Employee: claim > Employer E2: duty ; Without affecting section 7B, service under E1 is reckoned only for the purposes of
s 7C(6)(a) ; 570-572 ; E>s 7C(6) ; - ; (a) computing the minimum period of 3 months for annual leave
s 7C(6)(b) ; 574-576 ; E>s 7C(6) ; - ; (b) determining the period of service for paid sick leave
s 7C(7) ; 580-582 ; E ; Employee, E1 and E2: privilege > Others: no-right ; A signed consent form is prima facie proof of the matters in subsection (1)(b)
s 7C(8) ; 591-592 ; E ; Employee: claim > Employer E2: duty ; To avoid doubt, references to the employer in Parts 4 and 5 include E2
Part 4: headings ; 596-598,600,688,753-754,910-911 ; I1:part title and section headings ; - ; Part 4 title, and the headings of ss 8, 8A, 8B and 8C
s 8(1) ; 602-606 ; F:F12,F3 ; Employee: power > Minister: liability ; Representations in writing to the Minister, within one month of the dismissal, to be reinstated (gap: the form, "in writing", is not an input; see "What the text does not answer")
s 8(2) ; 608-611 ; E ; Minister: power > Commissioner: liability ; The Minister may direct the Commissioner to inquire and report (the text says "may", not "must"; the form, "in writing", is not an input; see "What the text does not answer")
s 8(3) ; 613-617 ; E ; Minister: power > Employer: liability ; The Minister may direct reinstatement and back pay, or compensation, and the employer must comply
s 8(3)(a) ; 619-623 ; E>s 8(3) ; - ; (a) reinstate the employee and pay an amount equivalent to the salary the employee would have earned
s 8(3)(b) ; 625-628 ; E>s 8(3) ; - ; (b) pay such amount of salary as compensation as the Minister considers just and equitable
s 8(3) closing ; 630 ; E>s 8(3) ; Minister: claim > Employer: duty ; and the employer must comply with the direction of the Minister
s 8(4) ; 632-634 ; E ; Employee: claim > Minister: duty ; In determining compensation the Minister must in particular have regard to
s 8(4)(a) ; 641-642 ; E>s 8(4) ; - ; (a) the loss sustained by the employee
s 8(4)(b) ; 644-645 ; E>s 8(4) ; - ; (b) the employee's prospects in obtaining alternative employment
s 8(4)(c) ; 647 ; E>s 8(4) ; - ; (c) the steps taken by the employee to mitigate the loss
s 8(4)(d) ; 649 ; E>s 8(4) ; - ; (d) the period the employee has served with the employer
s 8(4)(e) ; 650 ; E>s 8(4) ; - ; (e) the employee's age
s 8(5) ; 652-653 ; E ; Minister: immunity > Employee: disability ; The decision of the Minister is final
s 8(6) ; 655-657 ; E ; Employer: immunity > Employee: disability ; A direction under subsection (3) bars an action for damages
s 8(7) ; 659-662 ; E ; State: claim > Employer: duty ; Offence of failing to comply with the direction: fine up to $10,000, or imprisonment up to 12 months, or both
s 8(8) ; 664-670 ; E ; Employee: claim > Employer: duty ; An unpaid amount is recoverable by the court as if it were a fine, and paid to the employee
s 8(9) ; 672-674 ; E ; - ; The Minister may delegate the Minister's powers under this section (except the power of delegation) to a public officer
s 8(10) ; 676-677 ; E ; - ; A delegation is revocable at will and does not prevent the Minister exercising the power
s 8(11) ; 679-681 ; E ; Employee: claim > Employer: duty ; A delegated power, when exercised by the delegate, is deemed exercised by the Minister
s 8A(1) ; 690-695 ; F:F3 ; Commissioner: claim > Employee: duty ; The employee must first notify the Commissioner in writing no later than one month after the last day of employment
s 8A(2) ; 699-706 ; F:F3 ; Commissioner: claim > Employee: duty ; The same for an employee dismissed without just cause or excuse on or after attaining the specified age, who attained it on or after 1 January 2012
s 8A(3) ; 708-715 ; F:F3 ; Commissioner: claim > Employee: duty ; The employee must submit a mediation request not later than 6 months after the last day of employment
s 8A(4) ; 719-720 ; E ; - ; A re-employment dispute means a dispute over any of the following matters
s 8A(4)(a) ; 722-724 ; E>s 8A(4) ; - ; (a) the denial of re-employment because the employee does not satisfy the criteria in section 7(1)
s 8A(4)(b) ; 726-729 ; E>s 8A(4) ; - ; (b) the denial of re-employment because the employer cannot find a suitable vacancy
s 8A(4)(c) ; 736-738 ; E>s 8A(4) ; - ; (c) the reasonableness of the terms and conditions of a re-employment offer
s 8A(4)(d) ; 740-742 ; E>s 8A(4) ; - ; (d) the reasonableness of the amount of an employment assistance payment offered
s 8A(5) ; 746-749 ; E ; Commissioner: power > Employee and employer: liability ; The Commissioner may consult, or direct an approved mediator to consult, the employer and employee
s 8B(1) ; 756-764 ; F:F13 ; Employee: power > Minister: liability ; Representations in writing to the Minister to be re-employed
s 8B(2) ; 766-768 ; F:F3 ; Minister: claim > Employee: duty ; Representations must be made no later than one month after the conclusion of conciliation
s 8B(3) ; 770-773 ; E ; Employer: immunity > Employee: disability ; Representations under subsection (1) bar
s 8B(3)(a) ; 775-777 ; E>s 8B(3) ; - ; (a) the lodging of a claim under section 8C(1) in relation to section 8A(4)(d)
s 8B(3)(b) ; 784-786 ; E>s 8B(3) ; - ; (b) representations to the Minister under section 35(3) of the Industrial Relations Act 1960
s 8B(4) ; 790-793 ; E ; Employer: immunity > Employee: disability ; Representations under section 35(3) of the Industrial Relations Act 1960 bar
s 8B(4)(a) ; 795-797 ; E>s 8B(4) ; - ; (a) the lodging of a claim under section 8C(1) in relation to section 8A(4)(d)
s 8B(4)(b) ; 799-800 ; E>s 8B(4) ; - ; (b) representations under subsection (1)
s 8B(5) ; 804-809 ; E ; Minister: power > Commissioner: liability ; The Minister may direct the Commissioner to inquire and report
s 8B(6) ; 811-816 ; E ; Minister: power > Employer: liability ; The Minister may direct re-employment or compensation, and the employer must comply
s 8B(6)(a) ; 818 ; E>s 8B(6) ; - ; (a) direct the employer to re-employ the employee
s 8B(6)(b) ; 820-822 ; E>s 8B(6) ; - ; (b) direct the employer to pay such amount of compensation as the Minister considers just and equitable
s 8B(6) closing ; 824 ; E>s 8B(6) ; Minister: claim > Employer: duty ; and the employer must comply with the direction of the Minister
s 8B(7) ; 826-829,836-838 ; E ; Employee: power > Minister: liability ; Despite this section, the Minister may allow a mediation request and a claim for employment assistance payment where
s 8B(7)(a) ; 840-841 ; E>s 8B(7) ; - ; (a) the Minister has considered the Commissioner's report
s 8B(7)(b) ; 843-847 ; E>s 8B(7) ; - ; (b) the Minister is satisfied, for a dispute over section 8A(4)(b), that the employer made reasonable attempts
s 8B(8) ; 851-853 ; E ; Minister: claim > Employee: duty ; The employee must submit the mediation request within the time the Minister determines
s 8B(9) ; 857-858 ; E ; - ; Section 8C(3) applies to a claim lodged under subsection (7)
s 8B(10) ; 862-864 ; E ; Employee: claim > Minister: duty ; In determining compensation the Minister may in particular have regard to
s 8B(10)(a) ; 866 ; E>s 8B(10) ; - ; (a) the tripartite guidelines
s 8B(10)(b) ; 868-869 ; E>s 8B(10) ; - ; (b) the steps taken by the employer to re-employ the employee
s 8B(11) ; 871-872 ; E ; Minister: immunity > Employee: disability ; The decision of the Minister is final
s 8B(12) ; 874-877 ; E ; Employer: immunity > Employee: disability ; A direction under subsection (6) bars an action for damages
s 8B(13) ; 879-882 ; E ; State: claim > Employer: duty ; Offence of failing to comply with the direction: fine up to $10,000, or imprisonment up to 12 months, or both
s 8B(14) ; 889-895 ; E ; Employee: claim > Employer: duty ; An unpaid amount is recoverable by the court as if it were a fine, and paid to the employee
s 8B(15) ; 897-900 ; E ; - ; The Minister may delegate the Minister's powers under this section (except the power of delegation) to a public officer
s 8B(16) ; 902-904 ; E ; - ; A delegation is revocable at will and does not prevent the Minister exercising the power
s 8B(17) ; 906-908 ; E ; Employee: claim > Employer: duty ; A delegated power, when exercised by the delegate, is deemed exercised by the Minister
s 8C(1) ; 913-918 ; F:F21 ; Employee: power > Tribunal: liability ; A claim for employment assistance payment with an Employment Claims Tribunal, if a claim referral certificate is issued
s 8C(2) ; 922-925 ; E ; Employer: immunity > Employee: disability ; A claim to a Tribunal over section 8A(4)(d) bars
s 8C(2)(a) ; 927-928 ; E>s 8C(2) ; - ; (a) representations under section 8B(1) in respect of that dismissal
s 8C(2)(b) ; 935-937 ; E>s 8C(2) ; - ; (b) representations to the Minister under section 35(3) of the Industrial Relations Act 1960
s 8C(3) ; 941-942 ; E ; Employee: claim > Tribunal: duty ; In deciding a claim for employment assistance payment, the Tribunal
s 8C(3)(a) ; 944-946 ; E>s 8C(3) ; - ; (a) may take into account the tripartite guidelines and steps taken by the employer to re-employ
s 8C(3)(b) ; 948-952 ; E>s 8C(3) ; Employee: claim > Tribunal: duty ; (b) may, despite paragraph (a), order any amount it considers just and equitable
s 8D ; 956 ; X:[Repealed by Act 21 of 2016] ; - ; [Repealed by Act 21 of 2016]
s 8E ; 958 ; X:[Repealed by Act 21 of 2016] ; - ; [Repealed by Act 21 of 2016]
s 8F ; 960 ; X:[Repealed by Act 21 of 2016] ; - ; [Repealed by Act 21 of 2016]
Part 5: headings ; 962-964,966,1022,1064,1076,1091,1110,1119,1135,1147,1184 ; I1:part title and section headings ; - ; Part 5 title, and the headings of ss 9 to 13
s 9(1) ; 967-969 ; F:F14 ; Commissioner and investigating officers: power > Employer and others: liability ; The Commissioner or an investigating officer has power to do all or any of the following
s 9(1)(a) ; 971-976 ; E>s 9(1) ; - ; (a) enter without notice any place of employment, or make inquiry into terms and conditions of employment
s 9(1)(b) ; 978-991 ; E ; Commissioner and investigating officers: claim > Person examined: duty ; (b) examine orally any person supposed to be acquainted with the facts
s 9(1)(c) ; 993-996 ; E ; Commissioner and investigating officers: claim > Employer: duty ; (c) require the employer to produce any other employee and any contract of service or document
s 9(1)(d) ; 998-999 ; E>s 9(1) ; - ; (d) make copies of any document required to be produced
s 9(1)(e) ; 1001-1002 ; E>s 9(1) ; - ; (e) take or remove any document for purposes of investigations
s 9(1)(f) ; 1004-1008 ; E>s 9(1) ; - ; (f) take photographs or audio or video recordings
s 9(1)(g) ; 1010-1012 ; E ; Commissioner and investigating officers: claim > Person required: duty ; (g) require any person to produce any article, and if necessary take it into custody
s 9(2) ; 1014-1020 ; E ; State: claim > Any person: duty ; Offence of hindering or obstructing an investigating officer, or a materially false statement
s 9A(1) ; 1024 ; E ; Minister, Commissioner and investigating officers: power > Person summoned: liability ; Whenever
s 9A(1)(a) ; 1026-1028 ; E>s 9A(1) ; - ; (a) reasonable grounds for believing that an offence has been committed
s 9A(1)(b) ; 1030-1039 ; E>s 9A(1) ; - ; (b) wishes to inquire into any matter for which provision is made by this Act
s 9A(1)(c) ; 1041-1042 ; E>s 9A(1) ; - ; (c) any person complains of any breach
s 9A(1) summons ; 1044-1052 ; E>s 9A(1) ; Minister, Commissioner and investigating officers: claim > Person summoned: duty ; the person summoned is legally bound to attend and furnish information and answer truthfully
s 9A(2) ; 1054-1056 ; E ; State: claim > Any person: duty ; Offence of wilfully obstructing a summons, or neglecting to attend
s 9A(3) ; 1058-1062 ; E ; Commissioner and investigating officers: power > Person summoned: liability ; Report of a failure to attend to a Magistrate, who may issue a warrant
s 9B(1) ; 1066-1070 ; E ; State: claim > Employer or other person: duty ; Offence of obstructing an employee in appearing before the Commissioner
s 9B(2) ; 1072-1074 ; E ; State: claim > Any person: duty ; Offence of wilfully obstructing or impeding any entry, inquiry or investigation
s 9C ; 1078-1089 ; E ; State: claim > Offender: duty ; Penalty where none is otherwise provided; a heavier penalty for a subsequent offence
s 10(1) ; 1093-1097 ; E ; Investigating officer: power > Suspected offender: liability ; An investigating officer may compound a prescribed offence for a sum not exceeding the lower of
s 10(1)(a) ; 1099-1100 ; E>s 10(1) ; - ; (a) one half of the maximum fine prescribed for the offence
s 10(1)(b) ; 1102 ; E>s 10(1) ; - ; (b) $1,000
s 10(2) ; 1104-1105 ; E ; Suspected offender: immunity > State: disability ; On payment no further proceedings are to be taken against that person
s 10(3) ; 1107-1108 ; I2:regulation-making power ; - ; The Minister may make regulations to prescribe the offences that may be compounded
s 11(1) ; 1112-1114 ; E ; Exempted person: immunity > Employee and others: disability ; The Minister may by notification in the Gazette exempt any person or class from any provision
s 11(2) ; 1116-1117 ; E ; Minister: power > Exempted person: liability ; The Minister may at any time revoke an exemption, vary or revoke its conditions or impose new conditions
s 11A ; 1121-1122 ; E ; Employee: immunity > Employer: disability ; Any term of a contract of service or collective agreement is void insofar as it purports
s 11A(a) ; 1124-1125 ; E>s 11A ; - ; (a) to exclude or limit the operation of any provision of this Act
s 11A(b) ; 1127-1128 ; E>s 11A ; - ; (b) to preclude any person from making a representation, a claim or an application under this Act
s 11B ; 1137-1143 ; F:F15 ; Employee and employer: privilege > Tribunal and Minister: no-right ; Guidelines in the Gazette: regard may be had to them for Part 3 and sections 8A, 8B and 8C
s 12(1) ; 1149-1152 ; I2:regulation-making power ; - ; The Minister may make regulations
s 12(2) ; 1154-1156 ; I2:regulation-making power ; - ; Without limiting subsection (1), regulations may be made with respect to
s 12(2)(a) ; 1158-1159 ; I2:regulation-making power ; - ; (a) the procedure in respect of any proceedings under this Act
s 12(2)(b) ; 1161-1163 ; I2:regulation-making power ; - ; (b) incidental matters
s 12(2)(c) ; 1165-1166 ; I2:regulation-making power ; - ; (c) the form of the orders to be made under this Act
s 12(2)(d) ; 1168-1170 ; I2:regulation-making power ; - ; (d) application of provisions on re-employment, with modifications, to
s 12(2)(d)(i) ; 1172 ; I2:regulation-making power ; - ; (i) the renewal of a re-employment contract
s 12(2)(d)(ii) ; 1174-1175 ; I2:regulation-making power ; - ; (ii) the employment of an eligible employee by another employer as mentioned in section 7C(1)(b)
s 13 ; 1186-1188 ; E ; Employee and others: immunity > Employer: disability ; Nothing in this Act relieves any employer of any duty or liability under any other written law
back: legislative history ; 1191-1309 ; I1:the Legislative History says it is not part of the Act ; - ; Legislative History
back: abbreviations ; 1311-1338 ; I1:a list of abbreviations ; - ; Abbreviations
back: comparative table ; 1341-1389 ; I1:a table matching 2020 sections to the 2012 edition ; - ; Comparative Table
"""

# Running page headers and footers, and the marginal amendment notes, are inert (reason 1) and are found by pattern,
# not listed row by row: a page header is the line "Informal Consolidation - version in force from 1/7/2022" and the
# lines that follow it up to and including the line carrying the page number.
AMEND = re.compile(r"^\s*\[(Act \d+ of \d{4} wef [0-9/]+|[0-9/;\s]+)\]\s*$")

def parse_rows():
    rows = []
    for ln in ROWS.strip().split("\n"):
        f = [x.strip() for x in ln.split(" ; ")]
        if len(f) != 5:
            sys.exit(f"bad row (need 5 fields): {ln!r}")
        cite, lines, disp, jural, label = f
        rngs = []
        for part in lines.split(","):
            a, _, b = part.partition("-")
            rngs.append((int(a), int(b or a)))
        rows.append(dict(cite=cite, ranges=rngs, disp=disp, jural=jural, label=label))
    return rows

def read_lines(raw):
    return open(raw, encoding="utf-8").read().split("\n")

def auto_lines(lines):
    """line numbers (1-based) that are running headers/footers, and marginal amendment notes."""
    ph, am = set(), set()
    n = len(lines)
    for i, l in enumerate(lines, 1):
        if "Informal Consolidation" in l and "version in force" in l:
            ph.add(i)
            j = i + 1
            while j <= n and j <= i + 4:
                t = lines[j - 1].strip()
                if t == "" or re.fullmatch(r"(Retirement and Re-employment|Act 1993|2020 Ed\.|\d+|ii|iii)(\s+(Act 1993|2020 Ed\.|\d+))*", t) or re.fullmatch(r"2020 Ed\.\s+Act 1993\s+\d+", t) or re.fullmatch(r"\d+\s+Act 1993\s+2020 Ed\.", t) or re.fullmatch(r"2020 Ed\.\s+Act 1993\s+\d+", t):
                    ph.add(j)
                    if re.search(r"\d+\s*$", t) and t != "":
                        break
                    j += 1
                else:
                    break
        if AMEND.match(l):
            am.add(i)
    return ph, am

L4_DEF = re.compile(r"^(?:DECIDE\s+)?`([^`]+)`\s+(?:MEANS|IS|IF)\b")

def rules_in(folder):
    names = {}
    for fn in sorted(os.listdir(folder)):
        if fn.startswith("rra-") and fn.endswith(".l4") and not fn.startswith(("rra-tests", "rra-cases")):
            for i, l in enumerate(open(os.path.join(folder, fn), encoding="utf-8"), 1):
                m = L4_DEF.match(l)
                if m and m.group(1).startswith("s "):
                    names.setdefault(m.group(1), (fn, i))
    return names

def rules_for(cite, names):
    pre = cite + " "
    out = [n for n in names if n.startswith(pre)]
    if cite == "s 2(1)":  # the lead-in row owns only its own rule; each defined term has a row of its own
        out = [n for n in out if not n[len(pre):].startswith('"')]
    return out

def disp_kind(d):
    return d.split(":")[0].split(">")[0]

def main():
    cmd, raw = sys.argv[1], sys.argv[2]
    here = os.path.dirname(os.path.abspath(__file__))
    rows = parse_rows()
    lines = read_lines(raw)
    ph, am = auto_lines(lines)
    names = rules_in(here)
    nonblank = [i for i, l in enumerate(lines, 1) if l.strip()]
    covered = {}
    for r in rows:
        for a, b in r["ranges"]:
            for i in range(a, b + 1):
                covered.setdefault(i, []).append(r["cite"])
    uncovered = [i for i in nonblank if i not in covered and i not in ph and i not in am]
    over = [i for i in nonblank if len(covered.get(i, [])) > 1]
    bad_range = [(r["cite"], a, b) for r in rows for a, b in r["ranges"] if b > len(lines) or a < 1]
    # blank-only rows would be a mistake
    empty = [r["cite"] for r in rows if not any(lines[i - 1].strip() for a, b in r["ranges"] for i in range(a, b + 1))]
    # rules
    missing = []
    for r in rows:
        k = disp_kind(r["disp"])
        if k in ("E", "F"):
            cite = r["disp"].split(">", 1)[1].strip() if ">" in r["disp"] else r["cite"]
            r["via"] = cite
            r["rules"] = rules_for(cite, names)
            if not r["rules"]:
                missing.append(r["cite"])
    used = set()
    for r in rows:
        used.update(r.get("rules", []))
    unrowed = [n for n in names if n not in used]
    if cmd == "audit":
        kinds = {}
        for r in rows:
            kinds[disp_kind(r["disp"]) if disp_kind(r["disp"]) not in ("E", "F", "X") else disp_kind(r["disp"])] = kinds.get(disp_kind(r["disp"]), 0) + 1
        print(f"text lines: {len(lines)}; non-blank lines: {len(nonblank)}")
        print(f"  running page headers/footers (auto, inert reason 1): {len([i for i in ph if lines[i-1].strip()])} non-blank lines")
        print(f"  marginal amendment notes (auto, inert reason 1): {len(am)} lines")
        print(f"rows: {len(rows)}   by disposition: " + ", ".join(f"{k}={v}" for k, v in sorted(kinds.items())))
        print(f"non-blank lines in no row and not auto: {len(uncovered)} {uncovered[:40]}")
        print(f"non-blank lines in more than one row (information only; a sentence that defines two terms is in two rows): {len(over)} {over[:20]}")
        print(f"rows whose lines are all blank: {empty}")
        print(f"bad ranges: {bad_range}")
        print(f"encoded/fork rows with no rule: {len(missing)}")
        for m in missing: print("   MISSING", m)
        print(f"rules (`s ...` names in layer 1): {len(names)}; rules in no row: {len(unrowed)}")
        for u in unrowed: print("   UNROWED", u)
        ok = not (uncovered or empty or bad_range or missing or unrowed)
        print("AUDIT", "OK" if ok else "PROBLEMS")
        sys.exit(0 if ok else 1)
    if cmd == "write":
        notes = sys.argv[3]
        # coverage table
        def lrange(r):
            return ",".join(f"{a}-{b}" if a != b else str(a) for a, b in r["ranges"])
        out = ["| Row | Lines | Disposition | Encoded by / why |", "| --- | --- | --- | --- |"]
        for r in rows:
            k = disp_kind(r["disp"])
            if k == "E":
                d, w = "encoded", "; ".join(f"`{x}`" for x in r["rules"]) if r["via"] == r["cite"] else "within " + "; ".join(f"`{x}`" for x in r["rules"])
            elif k == "F":
                d = "fork " + r["disp"].split(":")[1].split(">")[0]
                w = "; ".join(f"`{x}`" for x in r["rules"]) if r["via"] == r["cite"] else "within " + "; ".join(f"`{x}`" for x in r["rules"])
            elif k in ("I1", "I2"):
                d = "inert, reason " + k[1]
                w = r["disp"].split(":", 1)[1]
            else:
                d = "repealed or blank in this text"
                w = "the text shows " + r["disp"].split(":", 1)[1]
            out.append(f"| {r['cite']} | {lrange(r)} | {d} | {w} |")
        out.append(f"| (auto) running page headers and footers | {len([i for i in ph if lines[i-1].strip()])} non-blank lines | inert, reason 1 | page headers, footers and page numbers repeat on every page |")
        out.append(f"| (auto) marginal amendment notes | {len(am)} lines | inert, reason 1 | `[Act 38 of 2021 wef 01/07/2022]`, `[5/2017]` and the like record which Act made an amendment; they state no rule |")
        cov = "\n".join(out)
        # jural table
        jt = ["| Provision | Holder of the right, privilege, power or immunity | Bearer of the duty, no-right, liability or disability | L4 rule |", "| --- | --- | --- | --- |"]
        nones = []
        for r in rows:
            if disp_kind(r["disp"]) in ("I1", "I2", "X"):
                continue
            if r["jural"] == "-":
                nones.append(r["cite"]); continue
            h, _, b = r["jural"].partition(" > ")
            rs = "; ".join(f"`{x}`" for x in r["rules"]) if r.get("rules") else ""
            jt.append(f"| {r['cite']} | {h} | {b} | {rs} |")
        jt.append("")
        jt.append("Provisions that create no such relation (a definition, a counting rule, a list of what a power may take into account, a gate on another section), listed once as `none`: " + "; ".join(nones) + ".")
        jur = "\n".join(jt)
        txt = open(notes, encoding="utf-8").read()
        for tag, body in (("coverage", cov), ("jural", jur)):
            pat = re.compile(rf"(<!-- BEGIN {tag} -->\n).*?(\n<!-- END {tag} -->)", re.S)
            if not pat.search(txt):
                sys.exit(f"NOTES.md has no {tag} markers")
            txt = pat.sub(lambda m: m.group(1) + body + m.group(2), txt)
        open(notes, "w", encoding="utf-8").write(txt)
        print(f"wrote {len(rows)} coverage rows and the jural table into {notes}")

main()
