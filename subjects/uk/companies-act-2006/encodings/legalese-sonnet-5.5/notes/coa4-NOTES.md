# NOTES: coa4, Companies Act 2006 (United Kingdom), Part 10 Chapters 1 to 4 (to s 204(2)), lines 2022-2696 of `ukpga-2006-46.txt`

Status (how each claim below was verified): every count and every statement about what the code answers was read from the files in this folder on 2026-11-13 (the `check.sh` output at the end is the run that produced the numbers quoted here: `L4=l4-main-110 L4_MAIN=l4-main-109 ./check.sh`, target `main`, exit 0). Nothing here is "proposed, not landed" except what a heading says is a fork, a marginal reading or a gap.

Range: `2022-2696` (12,421 words), s 154 to s 204(2): Part 10 (a company's directors), Chapter 1 (appointment and removal of directors, including the Chapter 1 sections 156A to 156C, 159A, 167G to 167N and 169A), Chapter 2 (general duties, ss 170 to 181), Chapter 3 (declaration of interest in an existing transaction, ss 182 to 187), and the first half of Chapter 4 (service contracts, substantial property transactions, loans, quasi-loans and credit transactions, and s 204(1) and (2)). The range ends at the last line of s 204(2) (line 2696, "exceeds £50,000."); s 205 begins at line 2697 and is coa5's.

## The files

| file | what it is | assertions or cases |
| --- | --- | --- |
| `coa4-appointment.l4` | ss 157 to 161: minimum age, the disqualification table of s 159A(2), single-resolution appointments, validity of acts (layer 1) (20 rules and functions) | - |
| `coa4-approval-loans.l4` | ss 197 to 204(2): loans, quasi-loans, credit transactions, related arrangements, the business-expenditure exception (layer 1) (38 rules and functions) | - |
| `coa4-approval-service-property.l4` | ss 188 to 196: long-term service contracts and substantial property transactions (layer 1) (32 rules and functions) | - |
| `coa4-cases-seat.l4` | cases for every seat question, with a "not covered" case (NOTHING) where the text leaves one | 321 |
| `coa4-declaration.l4` | ss 182 to 187: declaring an interest in an existing transaction (layer 1) (31 rules and functions) | - |
| `coa4-general-duties.l4` | ss 170 to 181: the seven general duties, authorisation, charities (layer 1) (52 rules and functions) | - |
| `coa4-notification.l4` | ss 167G to 167N: notices to the registrar, offences, ID verification, acting before notice (layer 1) (46 rules and functions) | - |
| `coa4-removal.l4` | ss 168 to 169A: removal by ordinary resolution, special notice, representations, ceasing on disqualification (layer 1) (19 rules and functions) | - |
| `coa4-requirements.l4` | ss 154 to 156C: the number of directors, a natural person, the Secretary of State's direction, the penalty, the age-and-person rules of s 156A (layer 1) (28 rules and functions) | - |
| `coa4-seat.l4` | the seat layer: 79 questions "Under section N, ...", each with @export and @desc, grouped under § headings in the text's order (layer 2) | - |
| `coa4-tests-appointment.l4` | tests of `coa4-appointment.l4`: expected values written from the text beside each assertion | 88 assertions satisfied |
| `coa4-tests-approval-loans.l4` | tests of `coa4-approval-loans.l4`: expected values written from the text beside each assertion | 187 assertions satisfied |
| `coa4-tests-approval-service-property.l4` | tests of `coa4-approval-service-property.l4`: expected values written from the text beside each assertion | 146 assertions satisfied |
| `coa4-tests-declaration.l4` | tests of `coa4-declaration.l4`: expected values written from the text beside each assertion | 107 assertions satisfied |
| `coa4-tests-general-duties.l4` | tests of `coa4-general-duties.l4`: expected values written from the text beside each assertion | 179 assertions satisfied |
| `coa4-tests-notification.l4` | tests of `coa4-notification.l4`: expected values written from the text beside each assertion | 178 assertions satisfied |
| `coa4-tests-removal.l4` | tests of `coa4-removal.l4`: expected values written from the text beside each assertion | 59 assertions satisfied |
| `coa4-tests-requirements.l4` | tests of `coa4-requirements.l4`: expected values written from the text beside each assertion | 107 assertions satisfied |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file; the work log; what the core lacks | - |

The keel's files `coa-core.l4`, `coa-definitions.l4`, `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are untouched. Every top-level name in the coa4 files (functions, types, constructors) begins with the label of its provision (`s 156(7) ...`), except the two seat helpers, `coa4 seat all of these answers hold` and `coa4 seat the individual born on`, which serve many sections and so cannot carry one section's label; the prefix `coa4` is this part's own, so they cannot collide with another part's names. The seat questions begin "Under section N,".

## The brief and PLAN.md

Where PLAN.md and the brief differ, the brief governs. I found no rule on which they conflict. They differ in emphasis in one place, which I resolved by the brief, and agree on the one other point I checked:
- PLAN.md section 4 makes `MAYBE BOOLEAN` the default type of a seam input. In layer 1 I did that. In the seat layer (the brief: "plain inputs, one per fact the person can state") each such input is a yes or no question, and the seat wraps the answer in `JUST` before passing it on; the form cannot ask "I do not know", so a fact another part decides (connected with a director, a shadow director, an officer in default, identity verified) reaches layer 1 as `JUST TRUE` or `JUST FALSE`. Where NOTHING has to travel through the seat (the answer of another section is unknown), the question cannot be asked at the seat, which is the limit of the plain-input form, not a rule of the Act.
- (Agreement, not a difference.) PLAN.md section 5 forbids `REFUSE`, `#ASSERT REFUSED` and `YMD`; so does the brief. No coa4 file uses them (checked by search, 2026-11-13).

## The seat layer, and what it leaves out

Seat: an individual who is, or is about to become, a director, a company secretary or a member of a company registered under the Act, or who deals with one. The seat file asks what such a person asks: is the company required to have enough directors, may I be appointed, have I ceased to be a director, must I notify, have I declared my interest, does the section bar the company from this transaction without the members' approval, what is the most I can be fined. 79 questions, 394 cases, every question has at least one case, and 63 of the cases are "not covered" cases asserted as NOTHING. Two seat answers deserve a word. The s 204 question answers NOTHING over the 50,000-pound limit: s 204(2) says only that the section "does not authorise" the transaction, not that approval is needed (ss 197 to 201 say that, and the seat asks those questions). The s 156(7) pound figures are asked of the person, because the Act does not state what a level on the standard scale is.


Left out of the seat: the layer-1 rules and functions the seat never calls. This list is generated by scanning the seat file for every layer-1 name, so it is complete (as of the run in this file); a caller can add a seat question for any of them without writing new law. The groups, in order of how much a person in the seat would feel their absence: the company's own liability (`s 156(6)(a)`, `s 156A(6)(a)` and (b), `s 167L(1)(a)`, `s 167M(4)(a)`); the penalty functions of the notification offences and of `s 183(2)` (each the same shape as the `s 156(7)` question the seat does ask); the memorandum rules of ss 197(3), 198(4), 200(4), 201(4) and 203(3) (the same shape as the s 188(5) question the seat does ask); and definitions, savings and signposts. The holding-company second-approval limbs of ss 188(2)(b), 190(2), 197(2), 198(3), 200(3), 201(3) and 203(2) are all asked (s 188 inside its main question, the others as their own questions).

- `coa4-appointment` (9): `s 157(2)`, `s 157(3)`, `s 157(5)`, `s 158(3)`, `s 158(3A)`, `s 159A(2)`, `s 159A(3)`, `s 159A(4)`, `s 160(2)`
- `coa4-approval-loans` (15): `s 197(4)`, `s 197(3)`, `s 198(5)`, `s 198(4)`, `s 199(2)`, `s 199(3)`, `s 200(5)`, `s 200(4)`, `s 201(5)`, `s 201(4)`, `s 202(2)`, `s 202(3)`, `s 203(4)`, `s 203(3)`, `s 203(6)`
- `coa4-approval-service-property` (11): `s 188(3)`, `s 188(4)`, `s 188(7)`, `s 191(4)`, `s 191(5)`, `s 190(5)`, `s 190(6)`, `s 190(3)`, `s 194(2)`, `s 195(3)(b)`, `s 195(8)`
- `coa4-declaration` (14): `s 182(3)`, `s 182(4)`, `s 182`, `s 183(2)`, `s 184(1)`, `s 184(5)(a)`, `s 184(5)(b)`, `s 185(1)`, `s 186(1)(b)`, `s 186(1)(c)`, `s 186(2)`, `s 187(2)`, `s 187(3)`, `s 187(4)`
- `coa4-general-duties` (34): `s 170(1)`, `s 170(3)`, `s 170(4)`, `s 170(5)`, `s 171`, `s 172(2)`, `s 172(3)`, `s 172(1)`, `s 173(2)`, `s 173(1)`, `s 174(1)`, `s 175(7)`, `s 175(2)`, `s 175(3)`, `s 175(4)`, `s 175(1)`, `s 176(4)`, `s 176(5)`, `s 176(1)`, `s 177(2)`, `s 177(3)`, `s 177(1)`, `s 178(1)`, `s 179`, `s 180(1)`, `s 180(2)`, `s 180(3)`, `s 180(4)(a)`, `s 180(4)(b)`, `s 180(5)`, `s 181(1)`, `s 181(2)(a)`, `s 181(3)`, `s 181(5)`
- `coa4-notification` (32): `s 167G(2)`, `s 167G(3)(a)`, `s 167G(3)(b)`, `s 167G(3)(c)`, `s 167G(3)(d)`, `s 167G(3)(e)`, `s 167G(3)(f)`, `s 167G(4)`, `s 167G(1)`, `s 167H(1)`, `s 167H(2)`, `s 167H(4)`, `s 167I(1)`, `s 167I(2)`, `s 167I(3)`, `s 167I(4)`, `s 167I(5)`, `s 167J(1)`, `s 167J(2)`, `s 167J(3)`, `s 167J(4)`, `s 167K(1)`, `s 167L(1)(a)`, `s 167L(3)`, `s 167M(2)`, `s 167M(4)(a)`, `s 167M(4)(b)`, `s 167M(5)`, `s 167M(6)`, `s 167N(4)`, `s 167N(6)`, `s 167N(7)`
- `coa4-removal` (12): `s 168(3)`, `s 168(4)`, `s 168(5)(a)`, `s 168(5)(b)`, `s 169(1)`, `s 169(3)`, `s 169(3)(a)`, `s 169(3)(b)`, `s 169(5)`, `s 169(6)`, `s 169A(2)`, `s 169A(3)`
- `coa4-requirements` (11): `s 156(4)`, `s 156(5A)`, `s 156(6)(a)`, `s 156A(4)`, `s 156A(6)(a)`, `s 156A(6)(b)`, `s 156A(6)(c)`, `s 156A(7)`, `s 156C(1)`, `s 156C(2A)`, `s 156C(3)`

### The seat questions, and what JUST TRUE answers in each

A question about a bar asks "does the section bar ...": JUST TRUE = the section bars it, JUST FALSE = it does not, NOTHING = the Act does not say on these facts. A question about a requirement asks whether it is met, and one about an effect asks whether the effect follows. The right-hand column is the layer-1 function the question returns (the first one it calls; a few questions combine several, see the seat file), whose own words are what JUST TRUE says.

| # | question | JUST TRUE says (the layer-1 function returned) |
| --- | --- | --- |
| 1 | Under section 154, does my company have enough directors | s 154(2) the public company meets the requirement to have at least two directors |
| 2 | Under section 155, does my company have a director who is a natural person | s 155(2) the requirement is met by the office of director being held by a natural person as a corporation sole or by virtue of an office |
| 3 | Under section 156, may the Secretary of State direct my company to appoint a director | s 156(1) the Secretary of State may give the company a direction under section 156 |
| 4 | Under section 156, is the direction my company has been given valid in form | s 156(2) the direction specifies what the section requires it to specify |
| 5 | Under section 156, has my company complied with the direction | s 156(5) the company has complied with the direction by giving notice of the appointments already made |
| 6 | Under section 156, am I guilty of an offence because my company did not comply with the direction | s 156(6)(b) the officer in default commits the offence |
| 7 | Under section 156, what is the most I can be fined for failing to comply with the direction | a maybe number: s 156(7) the penalty for the offence, under the wording ending one-tenth of level 5 on the standard scale |
| 8 | Under section 156, what is the most the daily default fine can be for continued failure | a maybe number: s 156(7) the daily default fine limit in pounds under the wording one-tenth of the greater of 5000 pounds or level 4 on the standard scale |
| 9 | Under section 156A, am I barred from being appointed a director because I am not a natural person | s 156A(1) section 156A(1) bars the appointment of the person as a director |
| 10 | Under section 156A, is an appointment of a person who is not a natural person void | s 156A(3) the appointment made is void |
| 11 | Under section 156C, have I ceased to be a director because I am not a natural person | s 156C(2) the person has ceased to hold office by virtue of that appointment |
| 12 | Under section 157, does section 157(1) bar the appointment of a person of my age as a director | s 157(1) section 157(1) bars the appointment of the person as a director |
| 13 | Under section 157, is the appointment of a person under 16 void | s 157(4) the appointment made is void |
| 14 | Under section 159A, am I barred from being appointed a director of a company registered in England and Wales or Scotland | s 159A(1) section 159A(1) bars the appointment of the person as a director |
| 15 | Under section 159A, am I barred from being appointed a director of a company registered in Northern Ireland | s 159A(1) section 159A(1) bars the appointment of the person as a director |
| 16 | Under section 160, does section 160(1) bar a motion to appoint two or more directors of a public company by a single resolution from being made | s 160(1) section 160(1) bars the motion being made |
| 17 | Under section 161, are the acts of a person acting as a director valid despite a defect | s 161(1) the acts of the person acting as a director are valid |
| 18 | Under section 167G, by what day must my company notify the registrar of a change in directors | a date: s 167G(6) the last day of the period of 14 days beginning with the day the person becomes or ceases to be a director |
| 19 | Under section 167G, did my company give notice of the change in directors in time | s 167G(6) the notice is given within the period of 14 days |
| 20 | Under section 167G, is my company obliged to notify the registrar of a change in directors | s 167G(1) the company is obliged to give notice to the registrar of the change |
| 21 | Under section 167G, does the notice of a new director contain what it must | s 167G(3) the notice contains what the subsection requires |
| 22 | Under section 167H, did my company give notice of a change in a director's details in time | s 167H(3) the notice is given within the period of 14 days beginning with the day the change occurs |
| 23 | Under section 167I, did my company give notice of a change before incorporation in time | s 167I(5) the notice is given within the period of 14 days beginning with the day the company was incorporated |
| 24 | Under section 167L, am I guilty of an offence because my company did not notify the registrar | s 167L(1)(b) the officer in default commits the offence |
| 25 | Under section 167M, am I committing an offence by acting as a director without my identity being verified | s 167M(3) the person who contravenes subsection (1) commits an offence |
| 26 | Under section 167N, am I committing an offence by acting as a director before the registrar has been told | s 167N(3) the person who contravenes subsection (2) commits an offence |
| 27 | Under section 167N, do I have a defence to the charge of acting before the registrar was told | s 167N(5) this section gives the person a defence on these facts |
| 28 | Under section 168, can the company remove a director by resolution | s 168(1) the company may by that resolution remove the director before the expiration of the director's period of office |
| 29 | Under section 168, is special notice required of a resolution to remove a director | s 168(2) special notice is required of the resolution |
| 30 | Under section 169, has my company done what it must when it received notice of a resolution to remove a director | s 169(1) the company has complied with the duty to send a copy of the notice to the director concerned |
| 31 | Under section 169, is a director entitled to be heard on the resolution to remove him | s 169(2) the director is entitled to be heard on the resolution at the meeting |
| 32 | Under section 169, can I require my written representations to be read out at the meeting | s 169(4) the director may require that the representations be read out at the meeting |
| 33 | Under section 169A, have I ceased to be a director because I became disqualified | s 169A(1) the person has ceased to hold office by virtue of the appointment |
| 34 | Under section 170, do the general duties still bind me after I cease to be a director | s 170(2) the former director continues to be subject to the duty |
| 35 | Under section 171, have I complied with the duty to act within my powers | s 171 the director has complied with the duty to act within powers |
| 36 | Under section 172, have I complied with the duty to promote the success of the company | s 172(1) the director has complied with the duty to promote the success of the company |
| 37 | Under section 173, have I complied with the duty to exercise independent judgment | s 173(1) the director has complied with the duty to exercise independent judgment |
| 38 | Under section 174, have I exercised reasonable care, skill and diligence | s 174(1) the director has exercised reasonable care, skill and diligence |
| 39 | Under section 175, have I complied with the duty to avoid conflicts of interest | s 175(1) the director has complied with the duty to avoid conflicts of interest |
| 40 | Under section 175, have the directors validly authorised the conflict | s 175(5) authorisation has been given by the directors |
| 41 | Under section 176, have I complied with the duty not to accept benefits from third parties | s 176(1) the director has complied with the duty not to accept benefits from third parties |
| 42 | Under section 177, must I declare my interest in a proposed transaction | s 177(1) the director is obliged to declare the nature and extent of the interest to the other directors |
| 43 | Under section 177, have I made the declaration of interest the section requires | s 177(4) the director has made the declaration the section requires |
| 44 | Under section 178, can the company enforce a general duty against me like any other fiduciary duty | s 178(2) the duty is enforceable in the same way as any other fiduciary duty owed to a company by its directors |
| 45 | Under section 180, is a transaction safe from being set aside for want of members' consent if section 175 or 177 was complied with | s 180(1) the transaction or arrangement is not liable to be set aside by virtue of a common law rule or equitable principle requiring the consent or approval of the members |
| 46 | Under section 181, have the directors validly authorised the conflict in a charitable company | s 181(2)(b) authorisation has been given by the directors, for a charity |
| 47 | Under section 182, must I declare my interest in a transaction the company has already entered into | s 182(1) the director is obliged to declare the nature and extent of the interest to the other directors |
| 48 | Under section 182, have I made the declaration in the way and at the time the section requires | s 182 the director has complied with the requirements of section 182 |
| 49 | Under section 183, am I guilty of an offence for failing to declare my interest | s 183(1) the director commits an offence |
| 50 | Under section 184, is my notice in writing of my interest in accordance with the section | s 184 the notice in writing is in accordance with section 184 |
| 51 | Under section 185, is my general notice of my interests in accordance with the section | s 185 the general notice is in accordance with section 185 |
| 52 | Under section 186, have I recorded my declaration of interest in writing as a sole director must | s 186(1)(a) the declaration has been recorded in writing as the section requires |
| 53 | Under section 187, does the duty to declare an interest in an existing transaction bind a shadow director | s 187(1) the provisions of Chapter 3 relating to the duty under section 182 apply to the person |
| 54 | Under section 188, does section 188(2) bar my company from agreeing a long-term service contract without its members' approval | s 188(3) the day on which the guaranteed term of the director's employment ends |
| 55 | Under section 188, has the memorandum been made available to members as required | s 188(5) the memorandum has been made available to members as the subsection requires |
| 56 | Under section 189, is a long-term service provision void if the company agreed to it without approval | s 189(a) the provision is void to the extent of the contravention |
| 57 | Under section 189, is a long-term service contract deemed to contain a term entitling my company to end it at any time on reasonable notice if the company agreed to it without approval | s 189(b) the contract is deemed to contain a term entitling the company to terminate it at any time by the giving of reasonable notice |
| 58 | Under section 190, does section 190(1) bar my company from entering into an arrangement for a substantial non-cash asset with a director without members' approval | s 190(1) section 190(1) bars the company from entering into the arrangement |
| 59 | Under section 190, must the members of my company's holding company also approve an arrangement for a substantial non-cash asset | s 190(2) section 190(2) requires the approval of the members of the holding company |
| 60 | Under section 191, is an asset substantial for the purposes of section 190 | s 191(2) the asset is a substantial asset in relation to the company |
| 61 | Under section 192, is approval under section 190 needed for a transaction with a member or between group companies | s 192 approval is required under section 190 for the transaction |
| 62 | Under section 193, is approval under section 190 needed while my company is being wound up or is in administration | s 193(2) approval is required under section 190 |
| 63 | Under section 194, is approval under section 190 needed for a transaction on a recognised investment exchange | s 194(1) approval is required under section 190 for the transaction |
| 64 | Under section 195, is an arrangement made without the approval section 190 requires voidable by the company | s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company |
| 65 | Under section 195, am I liable to account to the company and indemnify it for an arrangement made in contravention of section 190 | s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage |
| 66 | Under section 196, may an arrangement made without approval no longer be avoided because the members have affirmed it | s 196 the transaction or arrangement may no longer be avoided under section 195 |
| 67 | Under section 197, does section 197(1) bar my company from making a loan to a director without its members' approval | s 197(1) section 197(1) bars the company from the transaction |
| 68 | Under section 197, must the members of my company's holding company also approve a loan to a director of the holding company | s 197(2) the section requires the approval of the members of the holding company |
| 69 | Under section 198, does section 198(2) bar my company from making a quasi-loan to a director without its members' approval | s 198(2) the section bars the company from the transaction |
| 70 | Under section 198, must the members of my company's holding company also approve a quasi-loan to a director of the holding company | s 198(3) the section requires the approval of the members of the holding company |
| 71 | Under section 199, is the transaction a quasi-loan | s 199(1) the transaction is a quasi-loan |
| 72 | Under section 200, does section 200(2) bar my company from lending to a person connected with a director without its members' approval | s 200(2) the section bars the company from the transaction |
| 73 | Under section 200, must the members of my company's holding company also approve a loan to a person connected with a director of the holding company | s 200(3) the section requires the approval of the members of the holding company |
| 74 | Under section 201, does section 201(2) bar my company from entering into a credit transaction for a director without its members' approval | s 201(2) the section bars the company from the transaction |
| 75 | Under section 201, must the members of my company's holding company also approve a credit transaction for a director of the holding company or a person connected with one | s 201(3) the section requires the approval of the members of the holding company |
| 76 | Under section 202, is the transaction a credit transaction | s 202(1) the transaction is a credit transaction |
| 77 | Under section 203, does section 203(1) bar my company from taking part in a related arrangement without its members' approval | s 203(1) section 203(1) bars the company from the arrangement |
| 78 | Under section 203, must the members of my company's holding company also approve a related arrangement | s 203(2) the section requires the approval of the members of the holding company |
| 79 | Under section 204, does my company need members' approval for funds for expenditure on company business | s 204(2) section 204 authorises the company to enter into the transaction |

### Direction audit of the seat (repair of 2026-11-12)

A screen over every part's seat file found eight questions titled as a permission ("can ... be appointed", "may my company ...") whose layer-1 function says the section BARS the thing. I audited all 79 seat questions for the same defect, in direction (the name asks the opposite of what the function returns) and in subject (the name asks one thing and the function returns another: "must I" against "have I"). Fourteen questions were found in all: ten of direction (the eight flagged, `s 188`, and `s 196`, whose title asked "can it still be avoided" while the function answers "may no longer be avoided") and four of subject (`s 181`, `s 185`, `s 186`, `s 189(b)`). None was fixed by negating an answer: a bar's NOTHING and JUST FALSE are not a grant. Each was retitled, in its @export text and its DECIDE name, to ask what the function answers; no layer-1 function and no expected value changed. The other 65 questions were read against their functions and agree. The seat inputs' @desc lines ask facts, not permissions, and are unchanged; the seat has no separate question-level @desc.

| was | now |
| --- | --- |
| Under section 157, can a person of my age be appointed a director | Under section 157, does section 157(1) bar the appointment of a person of my age as a director |
| Under section 160, may a motion to appoint two or more directors of a public company by a single resolution be made | Under section 160, does section 160(1) bar a motion to appoint two or more directors of a public company by a single resolution from being made |
| Under section 188, may my company agree a long-term service contract without its members' approval | Under section 188, does section 188(2) bar my company from agreeing a long-term service contract without its members' approval |
| Under section 190, may my company enter into an arrangement for a substantial non-cash asset with a director without members' approval | Under section 190, does section 190(1) bar my company from entering into an arrangement for a substantial non-cash asset with a director without members' approval |
| Under section 197, may my company make a loan to a director without its members' approval | Under section 197, does section 197(1) bar my company from making a loan to a director without its members' approval |
| Under section 198, may my company make a quasi-loan to a director without its members' approval | Under section 198, does section 198(2) bar my company from making a quasi-loan to a director without its members' approval |
| Under section 200, may my company lend to a person connected with a director without its members' approval | Under section 200, does section 200(2) bar my company from lending to a person connected with a director without its members' approval |
| Under section 201, may my company enter into a credit transaction for a director without its members' approval | Under section 201, does section 201(2) bar my company from entering into a credit transaction for a director without its members' approval |
| Under section 203, may my company take part in a related arrangement without its members' approval | Under section 203, does section 203(1) bar my company from taking part in a related arrangement without its members' approval |
| Under section 196, can an arrangement made without approval still be avoided after the members affirm it | Under section 196, may an arrangement made without approval no longer be avoided because the members have affirmed it |
| Under section 181, can the directors authorise a conflict in a charitable company | Under section 181, have the directors validly authorised the conflict in a charitable company |
| Under section 186, must a sole director record a declaration of interest in writing | Under section 186, have I recorded my declaration of interest in writing as a sole director must |
| Under section 189, may my company end a long-term service contract at any time on reasonable notice if it agreed to it without approval | Under section 189, is a long-term service contract deemed to contain a term entitling my company to end it at any time on reasonable notice if the company agreed to it without approval |
| Under section 185, is my general notice of my interests effective | Under section 185, is my general notice of my interests in accordance with the section |



## Coverage (coa4)

One row per section, subsection, paragraph, sub-paragraph, table, table row, dotted line and defined term in lines 2022-2696, each with exactly one disposition. The table is generated from the text by `work/enumerate.py` (which asserts that every non-blank line of 2022-2696 falls in exactly one row) and `work/mkcoverage.py`; it is not typed by hand. Dispositions: `encoded` (a rule with a test and an `@ref`), `fork` (the row's reading is a fork, with its number in the note), `inert` (reason 1: not operative, a heading or a signpost; reason 2: machinery, regulation-making powers; reason 3: text shown repealed or blank, which in this range is the disposition `repealed or blank in this text`), and `repealed or blank in this text`. There is no `deferred` and no `out-of-scope` row.


Summary: 640 rows in all (the 618 text units and 22 defined terms): encoded 340, fork 183, inert 87, repealed or blank in this text 30.
The `fork` rule, so that the split between `fork` and `encoded` is not arbitrary: a row is `fork` when its note cites a fork where the text itself can be read two ways with different outcomes (forks F2, F3, F4, F11, F14, F16, F22, F23, F28, F29, F34, F35, F36, F37, F38, F39, F40, F41, F43, F44, F45, F47, F48, F49, F52, F53, F54, F56, F57, F59, F60, F66, F67, F69, F70, F71); a row whose note cites only a convention fork (forks F1, F5, F6, F7, F8, F9, F10, F12, F13, F15, F17, F18, F19, F20, F21, F24, F25, F26, F27, F30, F31, F32, F33, F42, F46, F50, F51, F55, F58, F61, F62, F63, F64, F65, F68: the site is decided by the 2026-11-05 ruling or a house convention, so the text alone does not offer two readings with different outcomes) stays `encoded`. The reading is in the fork register either way.

Audit: the enumerator counted 618 text units (238 subsections, 223 paragraphs, 71 sections, 39 sub-paragraphs, 18 headings, 15 table rows or tables, 14 dotted lines) covering all 675 non-blank lines of 2022-2696 with no line uncovered and no line in two rows; 22 defined-term rows were added to the 618 units, so the table has 640 rows. The table was regenerated after each module: at the last regeneration before the loans module it had 636 rows, 111 of them still `deferred` (ss 197 to 204 not yet written); the final table has 640 rows (four more defined terms: quasi-loan, credit transaction, conditional sale agreement, services) and 0 `deferred`.

Inert rows (87): reason 1 is 71 rows (the Part and Chapter headings, the section heading lines and the sub-headings of ss 154 to 204, and `s 191(1)`, a signpost sentence); reason 2 is 16 rows (`s 156B(1)`, (2), (3), (4), (6), (7); `s 158(1)`, (2), (4), (5); `s 167J(5)` with its (a) and (b), `s 167J(6)`; `s 167K(2)`, (3): regulation-making powers). Reason 3 (the text shown repealed or blank) is carried by the 30 rows whose disposition is `repealed or blank in this text`: the sections 161A to 167F shown as a heading and a row of dots, `s 156B(5)`, `s 159`, `s 181(4)` and the other dotted rows.

| provision | text lines | disposition | L4 name(s) | tests | note |
| --- | --- | --- | --- | --- | --- |
| Part 10 | 2022 | inert | - | - | reason 1: heading (not operative) |
| Chapter 1 | 2023 | inert | - | - | reason 1: heading (not operative) |
| heading: Requirement to have directors | 2024 | inert | - | - | reason 1: heading (not operative) |
| s 154 | 2025 | inert | - | - | reason 1: heading (not operative) |
| s 154(1) | 2026 | encoded | `s 154(1) the private company meets the requirement to have at least one director` | 5 | F1 (a bare "must" not done answers JUST FALSE) |
| s 154(2) | 2027 | encoded | `s 154(2) the public company meets the requirement to have at least two directors` | 5 | F1 |
| s 155 | 2028 | inert | - | - | reason 1: heading (not operative) |
| s 155(1) | 2029 | encoded | `s 155(1) the company meets the requirement to have at least one director who is a natural person` | 3 | F1 |
| s 155(2) | 2030 | encoded | `s 155(2) the requirement is met by the office of director being held by a natural person as a corporation sole or by virtue of an office` | 4 | marginal reading (a): a failed "if" answers JUST FALSE |
| s 156 | 2031 | inert | - | - | reason 1: heading (not operative) |
| s 156(1) | 2032-2035 | fork | `s 156(1) the Secretary of State may give the company a direction under section 156` | 4 | F4 (a grant behind an "If it appears" gate: NOTHING when it does not appear) |
| s 156(2) | 2036 | encoded | `s 156(2) the direction specifies what the section requires it to specify` | 4 | F1 |
| s 156(2)(a) | 2037 | encoded | `s 156(2) the direction specifies what the section requires it to specify` | 4 | F1 (row carried by 156(2)) |
| s 156(2)(b) | 2038 | encoded | `s 156(2) the direction specifies what the section requires it to specify` | 4 | F1 (row carried by 156(2)) |
| s 156(2)(c) | 2039-2040 | fork | `s 156(2) the direction specifies what the section requires it to specify`; `s 156(2) the period the direction specifies is not less than one month or more than three months after the day the direction is given` | 12 | the last sentence is the period rule; F3 (one month after a day that does not exist) |
| s 156(3) | 2041 | encoded | `s 156(3) the direction informs the company of the consequences of failing to comply as the section requires` | 2 | F1 |
| s 156(4) | 2042 | encoded | `s 156(4) the company has complied with the direction by making the appointments and giving notice of them`; `s 156(4) the company's duty to comply with the direction` | 8 | F5 (NOTHING when the "where" is unmet); regulative rule traced, decision function asserted |
| s 156(4)(a) | 2043 | encoded | `s 156(4) the company has complied with the direction by making the appointments and giving notice of them`; `s 156(4) the company's duty to comply with the direction` | 8 | F5 (NOTHING when the "where" is unmet); regulative rule traced, decision function asserted (row carried by 156(4)) |
| s 156(4)(b) | 2044-2045 | encoded | `s 156(4) the company has complied with the direction by making the appointments and giving notice of them`; `s 156(4) the company's duty to comply with the direction` | 8 | F5 (NOTHING when the "where" is unmet); regulative rule traced, decision function asserted (row carried by 156(4)) |
| s 156(5) | 2046 | encoded | `s 156(5) the company has complied with the direction by giving notice of the appointments already made` | 3 | F5 |
| s 156(5A) | 2047 | encoded | `s 156(5A) complying with the direction discharges the duty under section 167G to give notice within the period in section 167G(6)` | 1 | F10 (a constant: a flat negative) |
| s 156(6) | 2048 | encoded | `s 156(6)(a) the company commits an offence`; `s 156(6)(b) the officer in default commits the offence` | 11 | F6 |
| s 156(6)(a) | 2049 | encoded | `s 156(6)(a) the company commits an offence` | 2 | F6 |
| s 156(6)(b) | 2050-2051 | encoded | `s 156(6)(b) the officer in default commits the offence` | 9 | F6; the shadow-director sentence is carried by the s 251 input |
| s 156(7) | 2052 | fork | `s 156(7) the penalty for the offence, under the wording ending one-tenth of level 5 on the standard scale`; `s 156(7) the daily default fine limit in pounds under the wording one-tenth of the greater of 5000 pounds or level 4 on the standard scale`; `s 156(7) the fine limit in pounds` | 13 | F2. the text shows two wordings of the daily default fine; both are encoded |
| heading: Appointment | 2053 | inert | - | - | reason 1: heading (not operative) |
| s 156A | 2054 | inert | - | - | reason 1: heading (not operative) |
| s 156A(1) | 2055 | encoded | `s 156A(1) section 156A(1) bars the appointment of the person as a director` | 4 | F7 (polarity: JUST TRUE = barred); (2) and (5) are carried by the same function |
| s 156A(2) | 2056 | encoded | `s 156A(1) section 156A(1) bars the appointment of the person as a director` | 4 | F7: the corporation-sole branch |
| s 156A(3) | 2057 | encoded | `s 156A(3) the appointment made is void` | 3 | takes the answer under s 156A(1) |
| s 156A(4) | 2058 | encoded | `s 156A(4) section 156A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 156A(4)(a) | 2059 | encoded | `s 156A(4) section 156A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 156A(4)) |
| s 156A(4)(b) | 2060-2061 | encoded | `s 156A(4) section 156A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 156A(4)) |
| s 156A(5) | 2062 | encoded | `s 156A(1) section 156A(1) bars the appointment of the person as a director` | 4 | F7: the s 156B exception is the third input; regulations are outside the sources |
| s 156A(6) | 2063 | encoded | `s 156A(6)(a) the company purporting to make the appointment commits an offence`; `s 156A(6)(b) the body corporate or firm purportedly appointed commits an offence`; `s 156A(6)(c) the officer in default commits the offence` | 9 | F6 |
| s 156A(6)(a) | 2064 | encoded | `s 156A(6)(a) the company purporting to make the appointment commits an offence` | 2 | F6 |
| s 156A(6)(b) | 2065 | encoded | `s 156A(6)(b) the body corporate or firm purportedly appointed commits an offence` | 3 | F6 |
| s 156A(6)(c) | 2066-2067 | encoded | `s 156A(6)(c) the officer in default commits the offence` | 4 | F6; the shadow-director sentence is carried by the s 251 input |
| s 156A(7) | 2068 | fork | `s 156A(7) the penalty for the offence` | 5 | F2 does not apply here; the place of conviction selects the limb |
| s 156A(7)(a) | 2069 | fork | `s 156A(7) the penalty for the offence` | 5 | F2 does not apply here; the place of conviction selects the limb (row carried by 156A(7)) |
| s 156A(7)(b) | 2070 | fork | `s 156A(7) the penalty for the offence` | 5 | F2 does not apply here; the place of conviction selects the limb (row carried by 156A(7)) |
| s 156B | 2071 | inert | - | - | reason 1: heading (not operative) |
| s 156B(1) | 2072 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156B(2) | 2073 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156B(3) | 2074 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156B(4) | 2075 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156B(5) | 2076 | repealed or blank in this text | - | - | the text shows a row of dots |
| s 156B(6) | 2077-2078 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156B(7) | 2079 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain; the regulations are outside the sources (the effect of an exception is the third input of the s 156A(1) function) |
| s 156C | 2080 | inert | - | - | reason 1: heading (not operative) |
| s 156C(1) | 2081 | encoded | `s 156C(1) the relevant day` | 2 | F9; the day s 156A comes into force is an input |
| s 156C(2) | 2082 | encoded | `s 156C(2) the person has ceased to hold office by virtue of that appointment` | 6 | F8 |
| s 156C(2)(a) | 2083 | encoded | `s 156C(2) the person has ceased to hold office by virtue of that appointment` | 6 | F8 (row carried by 156C(2)) |
| s 156C(2)(b) | 2084-2085 | encoded | `s 156C(2) the person has ceased to hold office by virtue of that appointment` | 6 | F8 (row carried by 156C(2)) |
| s 156C(2A) | 2086 | encoded | `s 156C(2A) section 156C leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 156C(2A)(a) | 2087 | encoded | `s 156C(2A) section 156C leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 156C(2A)) |
| s 156C(2A)(b) | 2088 | encoded | `s 156C(2A) section 156C leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 156C(2A)) |
| s 156C(3) | 2089 | encoded | `s 156C(3) the registrar must include a note in the register recording that the company failed to give notice` | 3 | addresses the registrar; encoded for what it means to the company and its directors |
| s 157 | 2090 | inert | - | - | reason 1: heading (not operative) |
| s 157(1) | 2091 | fork | `s 157(1) section 157(1) bars the appointment of the person as a director` | 7 | F7 (polarity), F11 (a 29 February birthday) |
| s 157(2) | 2092 | encoded | `s 157(2) section 157 does not affect the validity of the appointment made before the person attains the age of 16 years` | 3 | F18 |
| s 157(3) | 2093 | encoded | `s 157(3) the appointment to the other office cannot yet make the person a director of the company` | 3 | F12 ("until" bar, ruling of 2026-11-05) |
| s 157(4) | 2094 | encoded | `s 157(4) the appointment made is void` | 3 | takes the answer under s 157(1) |
| s 157(5) | 2095 | encoded | `s 157(5) section 157 leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 157(5)(a) | 2096 | encoded | `s 157(5) section 157 leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 157(5)) |
| s 157(5)(b) | 2097-2098 | encoded | `s 157(5) section 157 leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 157(5)) |
| s 157(6) | 2099 | encoded | `s 157(1) section 157(1) bars the appointment of the person as a director` | 7 | the subject-to-s-158 limit is the third input of the s 157(1) function |
| s 158 | 2100 | inert | - | - | reason 1: heading (not operative) |
| s 158(1) | 2101 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain (the exception is the third input of the s 157(1) function) |
| s 158(2) | 2102 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain (the exception is the third input of the s 157(1) function) |
| s 158(3) | 2103 | encoded | `s 158(3) the person has ceased to hold office by virtue of that appointment` | 4 | F13 |
| s 158(3A) | 2104 | encoded | `s 158(3A) section 158(3) leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 158(3A)(a) | 2105 | encoded | `s 158(3A) section 158(3) leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 158(3A)) |
| s 158(3A)(b) | 2106 | encoded | `s 158(3A) section 158(3) leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 158(3A)) |
| s 158(4) | 2107-2108 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain (the exception is the third input of the s 157(1) function) |
| s 158(5) | 2109 | inert | - | - | reason 2: regulation-making power and what the regulations must or may contain (the exception is the third input of the s 157(1) function) |
| s 159 | 2110 | inert | - | - | reason 1: heading (not operative) |
| s 159 (blank text) | 2111 | repealed or blank in this text | - | - | the text shows a row of dots |
| s 159A | 2112 | inert | - | - | reason 1: heading (not operative) |
| s 159A(1) | 2113 | encoded | `s 159A(1) section 159A(1) bars the appointment of the person as a director` | 3 | F7, F15 |
| s 159A(2) | 2114 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it |
| s 159A(2)(a) | 2115 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(2)(a)(i) | 2116 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(2)(a)(ii) | 2117 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(2)(b) | 2118 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(2)(b)(i) | 2119 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(2)(b)(ii) | 2120 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table header | 2121 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 heading | 2122 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 1 | 2123 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 2 | 2124 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 3 | 2125 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 4 | 2126 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 5 | 2127 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 1 row 6 | 2128 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 heading | 2129 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 1 | 2130 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 2 | 2131 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 3 | 2132 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 4 | 2133 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 5 | 2134 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| 159A(2) table Part 2 row 6 | 2135 | fork | `s 159A(2) the person is disqualified under the directors disqualification legislation`; `s 159A(2) the Part of the table that applies for the place`; `s 159A(2) the Part of the table in which the row appears`; `s 159A(2) the circumstance in column 1 of the row`; `s 159A(2) the provision in column 2 of the row` | 30 | F14; the table is data (12 rows) and the decision function reads it (row carried by 159A(2)) |
| s 159A(3) | 2136 | encoded | `s 159A(3) the appointment made is void` | 3 | takes the answer under s 159A(1) |
| s 159A(4) | 2137 | encoded | `s 159A(4) section 159A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 159A(4)(a) | 2138 | encoded | `s 159A(4) section 159A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 159A(4)) |
| s 159A(4)(b) | 2139-2140 | encoded | `s 159A(4) section 159A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 159A(4)) |
| s 160 | 2141 | inert | - | - | reason 1: heading (not operative) |
| s 160(1) | 2142 | fork | `s 160(1) section 160(1) bars the motion being made` | 5 | F16 |
| s 160(2) | 2143-2144 | encoded | `s 160(2) the resolution moved is void`; `s 160(2) a provision for the automatic reappointment of retiring directors in default of another appointment applies` | 5 | the first sentence and the second sentence |
| s 160(3) | 2145 | encoded | `s 160(3) the motion is treated as a motion for the person's appointment` | 3 | list not closed (NOTHING for any other motion) |
| s 160(4) | 2146 | fork | `s 160(1) section 160(1) bars the motion being made` | 5 | F16: "Nothing in this section applies to a resolution amending the company's articles" is the first branch of the s 160(1) function |
| s 161 | 2147 | inert | - | - | reason 1: heading (not operative) |
| s 161(1) | 2148 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17 |
| s 161(1)(a) | 2149 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17 (row carried by 161(1)) |
| s 161(1)(b) | 2150 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17 (row carried by 161(1)) |
| s 161(1)(c) | 2151 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17 (row carried by 161(1)) |
| s 161(1)(d) | 2152 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17 (row carried by 161(1)) |
| s 161(2) | 2153 | encoded | `s 161(1) the acts of the person acting as a director are valid` | 7 | F17: the void resolution of section 160 is the fifth listed defect |
| heading: ... | 2154 | repealed or blank in this text | - | - | a heading shown as three dots |
| s 161A | 2155 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 161A (blank text) | 2156 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 161A) |
| s 162 | 2157 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 162 (blank text) | 2158 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 162) |
| s 163 | 2159 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 163 (blank text) | 2160 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 163) |
| s 164 | 2161 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 164 (blank text) | 2162 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 164) |
| s 165 | 2163 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 165 (blank text) | 2164 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 165) |
| s 166 | 2165 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 166 (blank text) | 2166 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 166) |
| s 167 | 2167 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167 (blank text) | 2168 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167) |
| heading: Option to keep information on the central register | 2169 | inert | - | - | reason 1: heading (not operative) |
| s 167A | 2170 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167A (blank text) | 2171 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167A) |
| s 167B | 2172 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167B (blank text) | 2173 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167B) |
| s 167C | 2174 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167C (blank text) | 2175 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167C) |
| s 167D | 2176 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167D (blank text) | 2177 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167D) |
| s 167E | 2178 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167E (blank text) | 2179 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167E) |
| s 167F | 2180 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank |
| s 167F (blank text) | 2181 | repealed or blank in this text | - | - | the section is shown as a heading followed by a row of dots: the text is repealed or blank (row carried by 167F) |
| heading: Notification of information about directors | 2182 | inert | - | - | reason 1: heading (not operative) |
| s 167G | 2183 | inert | - | - | reason 1: heading (not operative) |
| s 167G(1) | 2184 | encoded | `s 167G(1) the company is obliged to give notice to the registrar of the change`; `s 167G(1) the company's duty to give notice to the registrar of the change in directors` | 7 | regulative rule traced (clock 0 = the day of the change; the 14th day is clock 13), decision function asserted |
| s 167G(1)(a) | 2185 | encoded | `s 167G(1) the company is obliged to give notice to the registrar of the change`; `s 167G(1) the company's duty to give notice to the registrar of the change in directors` | 7 | regulative rule traced (clock 0 = the day of the change; the 14th day is clock 13), decision function asserted (row carried by 167G(1)) |
| s 167G(1)(b) | 2186 | encoded | `s 167G(1) the company is obliged to give notice to the registrar of the change`; `s 167G(1) the company's duty to give notice to the registrar of the change in directors` | 7 | regulative rule traced (clock 0 = the day of the change; the 14th day is clock 13), decision function asserted (row carried by 167G(1)) |
| s 167G(2) | 2187 | encoded | `s 167G(2) the notice specifies the date as the subsection requires` | 2 | F1 |
| s 167G(3) | 2188 | encoded | `s 167G(3) the notice contains what the subsection requires` | 9 | F5: a paragraph whose "if" is unmet answers NOTHING and is skipped by the whole |
| s 167G(3)(a) | 2189 | encoded | `s 167G(3)(a) the notice contains a statement of the required information about the new director` | 2 | F1 |
| s 167G(3)(b) | 2190 | encoded | `s 167G(3)(b) the notice contains a statement by the company that the person has consented to act in that capacity` | 2 | F1 |
| s 167G(3)(c) | 2191 | encoded | `s 167G(3)(c) the notice contains a statement that the individual's identity is verified` | 4 | F5 |
| s 167G(3)(d) | 2192 | encoded | `s 167G(3)(d) the notice contains a statement that the person is neither disqualified nor otherwise ineligible` | 3 | F1; both limbs (i) and (ii) are required |
| s 167G(3)(d)(i) | 2193 | encoded | `s 167G(3)(d) the notice contains a statement that the person is neither disqualified nor otherwise ineligible` | 3 | F1; both limbs (i) and (ii) are required (row carried by 167G(3)(d)) |
| s 167G(3)(d)(ii) | 2194 | encoded | `s 167G(3)(d) the notice contains a statement that the person is neither disqualified nor otherwise ineligible` | 3 | F1; both limbs (i) and (ii) are required (row carried by 167G(3)(d)) |
| s 167G(3)(e) | 2195 | encoded | `s 167G(3)(e) the notice contains a statement of the court and the date of the permission` | 5 | F5 |
| s 167G(3)(e)(i) | 2196 | encoded | `s 167G(3)(e) the notice contains a statement of the court and the date of the permission` | 5 | F5 (row carried by 167G(3)(e)) |
| s 167G(3)(e)(ii) | 2197 | encoded | `s 167G(3)(e) the notice contains a statement of the court and the date of the permission` | 5 | F5 (row carried by 167G(3)(e)) |
| s 167G(3)(f) | 2198 | encoded | `s 167G(3)(f) the notice contains a statement of the date and issuer of the licence` | 4 | F5 |
| s 167G(3)(f)(i) | 2199 | encoded | `s 167G(3)(f) the notice contains a statement of the date and issuer of the licence` | 4 | F5 (row carried by 167G(3)(f)) |
| s 167G(3)(f)(ii) | 2200 | encoded | `s 167G(3)(f) the notice contains a statement of the date and issuer of the licence` | 4 | F5 (row carried by 167G(3)(f)) |
| s 167G(4) | 2201 | encoded | `s 167G(4) the permission is permission of a court to act` | 3 | a "means" definition |
| s 167G(5) | 2202 | encoded | `s 167G(1) the company is obliged to give notice to the registrar of the change` | 5 | the incorporation exception is the third input of the s 167G(1) function (a flat negative) |
| s 167G(6) | 2203 | encoded | `s 167G(6) the last day of the period of 14 days beginning with the day the person becomes or ceases to be a director`; `s 167G(6) the notice is given within the period of 14 days`; `s 167G(1) the company's duty to give notice to the registrar of the change in directors` | 12 | F19 (14 days beginning with the day: the last day is the day plus 13) |
| s 167H | 2204 | inert | - | - | reason 1: heading (not operative) |
| s 167H(1) | 2205 | encoded | `s 167H(1) the company is obliged to give notice to the registrar of the change in the required information`; `s 167H(1) the company's duty to give notice to the registrar of the change in the required information` | 4 | regulative rule traced, decision function asserted |
| s 167H(2) | 2206 | encoded | `s 167H(2) the notice specifies the date of the change as the subsection requires` | 2 | F1 |
| s 167H(3) | 2207 | encoded | `s 167H(3) the notice is given within the period of 14 days beginning with the day the change occurs`; `s 167H(1) the company's duty to give notice to the registrar of the change in the required information` | 6 | F19 |
| s 167H(4) | 2208 | encoded | `s 167H(4) the notice contains the statement that the residential address is unchanged as the subsection requires` | 4 | F5 |
| s 167I | 2209 | inert | - | - | reason 1: heading (not operative) |
| s 167I(1) | 2210 | encoded | `s 167I(1) the company is obliged to give notice to the registrar that the proposed director did not become a director`; `s 167I(5) the company's duty to give notice to the registrar of the matters before incorporation` | 4 | the seam s 12 (coa1) is a plain fact |
| s 167I(2) | 2211 | encoded | `s 167I(2) the company is obliged to give notice to the registrar of the change in the required information about the proposed director`; `s 167I(5) the company's duty to give notice to the registrar of the matters before incorporation` | 5 | the seam s 9 (coa1) is a plain fact |
| s 167I(2)(a) | 2212 | encoded | `s 167I(2) the company is obliged to give notice to the registrar of the change in the required information about the proposed director`; `s 167I(5) the company's duty to give notice to the registrar of the matters before incorporation` | 5 | the seam s 9 (coa1) is a plain fact (row carried by 167I(2)) |
| s 167I(2)(b) | 2213 | encoded | `s 167I(2) the company is obliged to give notice to the registrar of the change in the required information about the proposed director`; `s 167I(5) the company's duty to give notice to the registrar of the matters before incorporation` | 5 | the seam s 9 (coa1) is a plain fact (row carried by 167I(2)) |
| s 167I(3) | 2214 | encoded | `s 167I(3) the company is required to give notice under subsection (2) in respect of the person` | 2 | flat negative: JUST FALSE; otherwise NOTHING (limited by its own wording) |
| s 167I(4) | 2215 | encoded | `s 167I(4) the notice specifies the date of the change as the subsection requires` | 2 | F1 |
| s 167I(5) | 2216 | encoded | `s 167I(5) the notice is given within the period of 14 days beginning with the day the company was incorporated`; `s 167I(5) the company's duty to give notice to the registrar of the matters before incorporation` | 5 | F19 |
| s 167J | 2217 | inert | - | - | reason 1: heading (not operative) |
| s 167J(1) | 2218 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) |
| s 167J(1)(a) | 2219 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) (row carried by 167J(1)) |
| s 167J(1)(b) | 2220 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) (row carried by 167J(1)) |
| s 167J(1)(c) | 2221 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) (row carried by 167J(1)) |
| s 167J(1)(d) | 2222 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) (row carried by 167J(1)) |
| s 167J(1)(e) | 2223 | encoded | `s 167J(1) the item is required information about a director who is an individual` | 6 | a definition by "is": closed (marginal reading (a)) (row carried by 167J(1)) |
| s 167J(2) | 2224 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 |
| s 167J(2)(a) | 2225 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 (row carried by 167J(2)) |
| s 167J(2)(b) | 2226 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 (row carried by 167J(2)) |
| s 167J(2)(b)(i) | 2227 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 (row carried by 167J(2)) |
| s 167J(2)(b)(ii) | 2228 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 (row carried by 167J(2)) |
| s 167J(2)(b)(iii) | 2229 | fork | `s 167J(2) the name is a relevant former name` | 7 | F22 (row carried by 167J(2)) |
| s 167J(3) | 2230-2232 | encoded | `s 167J(3) the name is a former name`; `s 167J(3) the item is the individual's name` | 4 | two "means" definitions |
| s 167J(4) | 2233 | encoded | `s 167J(4) the requirement to provide the individual's name is satisfied by providing the title` | 3 | limited by its own wording: NOTHING outside the limit |
| s 167J(5) | 2234 | inert | - | - | reason 2: regulations amending the section: machinery |
| s 167J(5)(a) | 2235 | inert | - | - | reason 2: regulations amending the section: machinery |
| s 167J(5)(b) | 2236 | inert | - | - | reason 2: regulations amending the section: machinery |
| s 167J(6) | 2237 | inert | - | - | reason 2: regulations are subject to affirmative resolution procedure: machinery |
| s 167K | 2238 | inert | - | - | reason 1: heading (not operative) |
| s 167K(1) | 2239 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 |
| s 167K(1)(a) | 2240 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(b) | 2241 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(c) | 2242 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(d) | 2243 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(e) | 2244 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(e)(i) | 2245 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(1)(e)(ii) | 2246 | fork | `s 167K(1) the item is required information about a body corporate or a firm that is a legal person` | 16 | F23 (row carried by 167K(1)) |
| s 167K(2) | 2247 | inert | - | - | reason 2: regulations amending the section: machinery |
| s 167K(3) | 2248 | inert | - | - | reason 2: regulations are subject to affirmative resolution procedure: machinery |
| s 167L | 2249 | inert | - | - | reason 1: heading (not operative) |
| s 167L(1) | 2250 | encoded | `s 167L(1)(a) the company commits an offence`; `s 167L(1)(b) the officer in default commits the offence` | 8 | F6, F24 |
| s 167L(1)(a) | 2251 | encoded | `s 167L(1)(a) the company commits an offence` | 2 | F6, F24 |
| s 167L(1)(b) | 2252 | encoded | `s 167L(1)(b) the officer in default commits the offence` | 6 | F6; the shadow-director sentence of (2) is carried by the s 251 input |
| s 167L(2) | 2253 | encoded | `s 167L(1)(b) the officer in default commits the offence` | 6 | F6 |
| s 167L(3) | 2254 | encoded | `s 167L(3) the penalty for the offence` | 5 | the place of conviction selects the limb |
| s 167L(3)(a) | 2255 | encoded | `s 167L(3) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167L(3)) |
| s 167L(3)(b) | 2256 | encoded | `s 167L(3) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167L(3)) |
| heading: Directors: duties relating to ID verification and  | 2257 | inert | - | - | reason 1: heading (not operative) |
| s 167M | 2258 | inert | - | - | reason 1: heading (not operative) |
| s 167M(1) | 2259 | encoded | `s 167M(1) the individual contravenes subsection (1) by acting as a director` | 5 | prohibition: JUST TRUE = contravenes |
| s 167M(2) | 2260 | encoded | `s 167M(2) the company contravenes subsection (2)` | 4 | F20 |
| s 167M(3) | 2261 | encoded | `s 167M(3) the person who contravenes subsection (1) commits an offence` | 3 | takes the answer under s 167M(1) |
| s 167M(4) | 2262 | encoded | `s 167M(4)(a) the company commits an offence`; `s 167M(4)(b) the officer in default commits the offence` | 10 | F6 |
| s 167M(4)(a) | 2263 | encoded | `s 167M(4)(a) the company commits an offence` | 3 | F6 |
| s 167M(4)(b) | 2264-2265 | encoded | `s 167M(4)(b) the officer in default commits the offence` | 7 | F6; the shadow-director sentence is carried by the s 251 input |
| s 167M(5) | 2266 | encoded | `s 167M(5) the penalty for the offence` | 5 | the place of conviction selects the limb |
| s 167M(5)(a) | 2267 | encoded | `s 167M(5) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167M(5)) |
| s 167M(5)(b) | 2268 | encoded | `s 167M(5) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167M(5)) |
| s 167M(6) | 2269 | encoded | `s 167M(6) the consequence follows from contravening subsection (1) or (2)` | 3 | F27 |
| s 167N | 2270 | inert | - | - | reason 1: heading (not operative) |
| s 167N(1) | 2271 | encoded | `s 167N(2) the person contravenes subsection (2) by acting as a director` | 5 | the two conditions of (1) are the first two inputs of the s 167N(2) function |
| s 167N(1)(a) | 2272 | encoded | `s 167N(2) the person contravenes subsection (2) by acting as a director` | 5 | the two conditions of (1) are the first two inputs of the s 167N(2) function (row carried by 167N(1)) |
| s 167N(1)(b) | 2273 | encoded | `s 167N(2) the person contravenes subsection (2) by acting as a director` | 5 | the two conditions of (1) are the first two inputs of the s 167N(2) function (row carried by 167N(1)) |
| s 167N(2) | 2274 | encoded | `s 167N(2) the person contravenes subsection (2) by acting as a director` | 5 | an "until" bar (ruling of 2026-11-05, see F12): JUST TRUE before notice is given, JUST FALSE once it is |
| s 167N(3) | 2275 | encoded | `s 167N(3) the person who contravenes subsection (2) commits an offence` | 3 | takes the answer under s 167N(2) |
| s 167N(4) | 2276 | encoded | `s 167N(4) the officer in default commits the offence` | 6 | F26 (no shadow-director sentence in this subsection) |
| s 167N(5) | 2277 | encoded | `s 167N(5) this section gives the person a defence on these facts` | 4 | F25 (ruling of 2026-11-05 (b)) |
| s 167N(6) | 2278 | encoded | `s 167N(6) the penalty for the offence` | 5 | the place of conviction selects the limb |
| s 167N(6)(a) | 2279 | encoded | `s 167N(6) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167N(6)) |
| s 167N(6)(b) | 2280 | encoded | `s 167N(6) the penalty for the offence` | 5 | the place of conviction selects the limb (row carried by 167N(6)) |
| s 167N(7) | 2281 | encoded | `s 167N(7) the consequence follows from contravening subsection (2)` | 3 | F27 |
| heading: Removal | 2282 | inert | - | - | reason 1: heading (not operative) |
| s 168 | 2283 | inert | - | - | reason 1: heading (not operative) |
| s 168(1) | 2284 | fork | `s 168(1) the company may by that resolution remove the director before the expiration of the director's period of office` | 6 | F28; the ordinary resolution is the s 282 seam |
| s 168(2) | 2285 | encoded | `s 168(2) special notice is required of the resolution` | 4 | limited by its own wording: NOTHING for another resolution |
| s 168(3) | 2286 | fork | `s 168(3) the vacancy may be filled as a casual vacancy` | 3 | F70 (a grant behind an "if not filled" gate: NOTHING when it was filled) |
| s 168(4) | 2287 | encoded | `s 168(4) the day on which the person appointed in place is treated as having become director, for the time at which a director is to retire` | 2 | F33 |
| s 168(5) | 2288 | encoded | `s 168(5)(a) section 168 deprives the person removed of the compensation or damages`; `s 168(5)(b) section 168 derogates from the power to remove the director that exists apart from the section` | 4 | two flat negatives |
| s 168(5)(a) | 2289 | encoded | `s 168(5)(a) section 168 deprives the person removed of the compensation or damages` | 2 | a flat negative: JUST FALSE where compensation is payable |
| s 168(5)(b) | 2290 | encoded | `s 168(5)(b) section 168 derogates from the power to remove the director that exists apart from the section` | 2 | a flat negative: JUST FALSE where such a power exists |
| s 169 | 2291 | inert | - | - | reason 1: heading (not operative) |
| s 169(1) | 2292 | fork | `s 169(1) the company has complied with the duty to send a copy of the notice to the director concerned`; `s 169(1) the company's duty to send a copy of the notice to the director concerned` | 6 | F29 ("forthwith"); regulative rule traced (a MUST with no WITHIN), decision function asserted |
| s 169(2) | 2293 | encoded | `s 169(2) the director is entitled to be heard on the resolution at the meeting` | 3 | membership does not change the answer |
| s 169(3) | 2294 | encoded | `s 169(3) the company is obliged to state the fact of the representations and send a copy of them to the members`; `s 169(3) the company's duty to state the representations and send a copy of them` | 7 | F30; regulative rule traced |
| s 169(3)(a) | 2295 | encoded | `s 169(3)(a) the company has stated the fact of the representations in the notice of the resolution` | 4 | F5 (NOTHING where the obligation does not arise) |
| s 169(3)(b) | 2296 | encoded | `s 169(3)(b) the company has sent a copy of the representations to every member to whom notice of the meeting is sent` | 4 | F5 |
| s 169(4) | 2297 | fork | `s 169(4) the director may require that the representations be read out at the meeting` | 3 | F71 (a grant behind an "If" gate: NOTHING when the gate fails) |
| s 169(5) | 2298 | encoded | `s 169(5) copies need not be sent out and the representations need not be read out` | 2 | F31: the court's satisfaction is a plain input |
| s 169(6) | 2299 | encoded | `s 169(6) the court may order the company's costs to be paid in whole or in part by the director` | 3 | being a party does not change the answer |
| s 169A | 2300 | inert | - | - | reason 1: heading (not operative) |
| s 169A(1) | 2301 | encoded | `s 169A(1) the person has ceased to hold office by virtue of the appointment` | 4 | takes the s 159A(2) answer as a MAYBE BOOLEAN |
| s 169A(2) | 2302 | encoded | `s 169A(2) section 169A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources |
| s 169A(2)(a) | 2303 | encoded | `s 169A(2) section 169A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 169A(2)) |
| s 169A(2)(b) | 2304 | encoded | `s 169A(2) section 169A leaves the person's liability unaffected` | 4 | the liability itself is outside the sources (row carried by 169A(2)) |
| s 169A(3) | 2305 | encoded | `s 169A(3) the person is treated as a person who becomes disqualified` | 3 | F32 ("includes") |
| Chapter 2 | 2306 | inert | - | - | reason 1: heading (not operative) |
| heading: Introductory | 2307 | inert | - | - | reason 1: heading (not operative) |
| s 170 | 2308 | inert | - | - | reason 1: heading (not operative) |
| s 170(1) | 2309 | encoded | `s 170(1) the general duty is owed by the person to the company` | 9 | the duties are the enum of ss 171 to 177; any other duty answers NOTHING |
| s 170(2) | 2310 | fork | `s 170(2) the former director continues to be subject to the duty` | 7 | F34 |
| s 170(2)(a) | 2311 | fork | `s 170(2) the former director continues to be subject to the duty` | 7 | F34 (row carried by 170(2)) |
| s 170(2)(b) | 2312-2313 | fork | `s 170(2) the former director continues to be subject to the duty` | 7 | F34 (row carried by 170(2)) |
| s 170(3) | 2314 | encoded | `s 170(3) the general duties have effect in place of the common law rules and equitable principles` | 2 | a rule of effect; the common law itself is outside the sources |
| s 170(4) | 2315 | encoded | `s 170(4) regard shall be had to the corresponding common law rules and equitable principles` | 2 | a rule of reading, encoded as a function over whether the duties are being interpreted or applied |
| s 170(5) | 2316 | encoded | `s 170(5) the general duty applies to the shadow director` | 4 | the shadow director is the s 251 seam; "capable of so applying" is a plain input |
| heading: The general duties | 2317 | inert | - | - | reason 1: heading (not operative) |
| s 171 | 2318-2321 | encoded | `s 171 the director has complied with the duty to act within powers`; `s 171 the director's duty to act within powers` | 6 | F1; regulative rule with no deadline (the text gives none), traced |
| s 172 | 2322 | inert | - | - | reason 1: heading (not operative) |
| s 172(1) | 2323 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) |
| s 172(1)(a) | 2324 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(1)(b) | 2325 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(1)(c) | 2326 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(1)(d) | 2327 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(1)(e) | 2328 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(1)(f) | 2329 | fork | `s 172(1) the director has complied with the duty to promote the success of the company`; `s 172(1) the director's duty to promote the success of the company` | 10 | F35 (open-textured: "considers, in good faith" is a plain input; "amongst other matters" does not close the list) (row carried by 172(1)) |
| s 172(2) | 2330 | encoded | `s 172(2) the object of the duty in section 172(1)` | 2 | the object the duty is read as having |
| s 172(3) | 2331 | encoded | `s 172(3) the duty has effect subject to the enactment or rule of law requiring directors to consider or act in the interests of creditors` | 2 | the enactment or rule of law is outside the sources |
| s 173 | 2332 | inert | - | - | reason 1: heading (not operative) |
| s 173(1) | 2333 | encoded | `s 173(1) the director has complied with the duty to exercise independent judgment`; `s 173(1) the director's duty to exercise independent judgment` | 6 | F1; regulative rule traced |
| s 173(2) | 2334 | encoded | `s 173(2) the duty to exercise independent judgment is not infringed by the director's acting` | 3 | NOTHING for any other conduct |
| s 173(2)(a) | 2335 | encoded | `s 173(2) the duty to exercise independent judgment is not infringed by the director's acting` | 3 | NOTHING for any other conduct (row carried by 173(2)) |
| s 173(2)(b) | 2336 | encoded | `s 173(2) the duty to exercise independent judgment is not infringed by the director's acting` | 3 | NOTHING for any other conduct (row carried by 173(2)) |
| s 174 | 2337 | inert | - | - | reason 1: heading (not operative) |
| s 174(1) | 2338 | fork | `s 174(1) the director has exercised reasonable care, skill and diligence`; `s 174(1) the director's duty to exercise reasonable care, skill and diligence` | 6 | F35; the two standards of (2) are the two inputs; regulative rule traced |
| s 174(2) | 2339 | encoded | `s 174(1) the director has exercised reasonable care, skill and diligence` | 4 | "This means": a closed definition, carried by the s 174(1) function |
| s 174(2)(a) | 2340 | encoded | `s 174(1) the director has exercised reasonable care, skill and diligence` | 4 | "This means": a closed definition, carried by the s 174(1) function (row carried by 174(2)) |
| s 174(2)(b) | 2341 | encoded | `s 174(1) the director has exercised reasonable care, skill and diligence` | 4 | "This means": a closed definition, carried by the s 174(1) function (row carried by 174(2)) |
| s 175 | 2342 | inert | - | - | reason 1: heading (not operative) |
| s 175(1) | 2343 | fork | `s 175(1) the director has complied with the duty to avoid conflicts of interest`; `s 175(1) the director's duty to avoid conflicts of interest` | 7 | F37; regulative rule traced; the function calls (3) and (4) |
| s 175(2) | 2344 | encoded | `s 175(2) the situation is within the duty to avoid conflicts of interest as the exploitation of property, information or opportunity` | 3 | "in particular": NOTHING for another situation |
| s 175(3) | 2345 | encoded | `s 175(3) the duty to avoid conflicts of interest applies to the conflict` | 2 | a flat negative: JUST FALSE for a conflict arising in relation to a transaction or arrangement with the company |
| s 175(4) | 2346 | fork | `s 175(4) the duty to avoid conflicts of interest is not infringed` | 3 | F37 |
| s 175(4)(a) | 2347 | fork | `s 175(4) the duty to avoid conflicts of interest is not infringed` | 3 | F37 (row carried by 175(4)) |
| s 175(4)(b) | 2348 | fork | `s 175(4) the duty to avoid conflicts of interest is not infringed` | 3 | F37 (row carried by 175(4)) |
| s 175(5) | 2349 | encoded | `s 175(5) authorisation has been given by the directors` | 7 | public or private by the s 4(2) seam; for a charity see s 181(2)(b) |
| s 175(5)(a) | 2350 | encoded | `s 175(5) authorisation has been given by the directors` | 7 | public or private by the s 4(2) seam; for a charity see s 181(2)(b) (row carried by 175(5)) |
| s 175(5)(b) | 2351 | encoded | `s 175(5) authorisation has been given by the directors` | 7 | public or private by the s 4(2) seam; for a charity see s 181(2)(b) (row carried by 175(5)) |
| s 175(6) | 2352 | encoded | `s 175(6) the authorisation is effective` | 5 | "effective only if": a closed condition, JUST FALSE otherwise |
| s 175(6)(a) | 2353 | encoded | `s 175(6) the authorisation is effective` | 5 | "effective only if": a closed condition, JUST FALSE otherwise (row carried by 175(6)) |
| s 175(6)(b) | 2354 | encoded | `s 175(6) the authorisation is effective` | 5 | "effective only if": a closed condition, JUST FALSE otherwise (row carried by 175(6)) |
| s 175(7) | 2355 | encoded | `s 175(7) the conflict is a conflict of interest for the purposes of the section` | 2 | "includes": JUST TRUE for the named cases, NOTHING otherwise |
| s 176 | 2356 | inert | - | - | reason 1: heading (not operative) |
| s 176(1) | 2357 | fork | `s 176(1) the director has complied with the duty not to accept benefits from third parties`; `s 176(1) the director's duty not to accept benefits from third parties` | 8 | F37-style; regulative rule is a SHANT with no deadline, traced |
| s 176(1)(a) | 2358 | fork | `s 176(1) the director has complied with the duty not to accept benefits from third parties`; `s 176(1) the director's duty not to accept benefits from third parties` | 8 | F37-style; regulative rule is a SHANT with no deadline, traced (row carried by 176(1)) |
| s 176(1)(b) | 2359 | fork | `s 176(1) the director has complied with the duty not to accept benefits from third parties`; `s 176(1) the director's duty not to accept benefits from third parties` | 8 | F37-style; regulative rule is a SHANT with no deadline, traced (row carried by 176(1)) |
| s 176(2) | 2360 | encoded | `s 176(2) the person is a third party` | 4 | a "means" definition |
| s 176(3) | 2361 | encoded | `s 176(3) the benefit is regarded as conferred by a third party` | 2 | a flat negative |
| s 176(4) | 2362 | encoded | `s 176(4) the duty not to accept benefits from third parties is not infringed` | 2 | NOTHING for any other case |
| s 176(5) | 2363 | encoded | `s 176(5) the conflict is a conflict of interest for the purposes of the section` | 2 | "includes" |
| s 177 | 2364 | inert | - | - | reason 1: heading (not operative) |
| s 177(1) | 2365 | fork | `s 177(1) the director is obliged to declare the nature and extent of the interest to the other directors`; `s 177(1) the director's duty to declare the interest to the other directors` | 8 | F38; the answers of (5) and (6) are inputs; regulative rule traced |
| s 177(2) | 2366 | fork | `s 177(2) the declaration is made in a way the subsection allows` | 5 | F39; the ss 184 and 185 answers are MAYBE BOOLEAN inputs wired to this part's own functions |
| s 177(2)(a) | 2367 | fork | `s 177(2) the declaration is made in a way the subsection allows` | 5 | F39; the ss 184 and 185 answers are MAYBE BOOLEAN inputs wired to this part's own functions (row carried by 177(2)) |
| s 177(2)(b) | 2368 | fork | `s 177(2) the declaration is made in a way the subsection allows` | 5 | F39; the ss 184 and 185 answers are MAYBE BOOLEAN inputs wired to this part's own functions (row carried by 177(2)) |
| s 177(2)(b)(i) | 2369 | fork | `s 177(2) the declaration is made in a way the subsection allows` | 5 | F39; the ss 184 and 185 answers are MAYBE BOOLEAN inputs wired to this part's own functions (row carried by 177(2)) |
| s 177(2)(b)(ii) | 2370 | fork | `s 177(2) the declaration is made in a way the subsection allows` | 5 | F39; the ss 184 and 185 answers are MAYBE BOOLEAN inputs wired to this part's own functions (row carried by 177(2)) |
| s 177(3) | 2371 | encoded | `s 177(3) a further declaration must be made` | 2 | an "if" condition |
| s 177(4) | 2372 | fork | `s 177(4) the director has made the declaration the section requires`; `s 177(1) the director's duty to declare the interest to the other directors` | 7 | F38; "before the company enters into" is a fixed point, not a number of days |
| s 177(5) | 2373-2374 | encoded | `s 177(5) the section requires a declaration so far as the director's awareness goes` | 5 | the "ought reasonably to be aware" sentence is carried by the inputs |
| s 177(6) | 2375 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") |
| s 177(6)(a) | 2376 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") (row carried by 177(6)) |
| s 177(6)(b) | 2377 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") (row carried by 177(6)) |
| s 177(6)(c) | 2378 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") (row carried by 177(6)) |
| s 177(6)(c)(i) | 2379 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") (row carried by 177(6)) |
| s 177(6)(c)(ii) | 2380 | fork | `s 177(6) the director need not declare the interest` | 6 | F36 ("to the extent") (row carried by 177(6)) |
| heading: Supplementary provisions | 2381 | inert | - | - | reason 1: heading (not operative) |
| s 178 | 2382 | inert | - | - | reason 1: heading (not operative) |
| s 178(1) | 2383 | encoded | `s 178(1) the consequences of breach are the same as would apply if the corresponding common law rule or equitable principle applied` | 8 | the consequences themselves are outside the sources |
| s 178(2) | 2384 | encoded | `s 178(2) the duty is enforceable in the same way as any other fiduciary duty owed to a company by its directors` | 8 | the exception for s 174 is JUST FALSE |
| s 179 | 2385-2386 | encoded | `s 179 more than one of the general duties may apply in the case` | 2 | "Except as otherwise provided": NOTHING |
| s 180 | 2387 | inert | - | - | reason 1: heading (not operative) |
| s 180(1) | 2388 | encoded | `s 180(1) the transaction or arrangement is not liable to be set aside by virtue of a common law rule or equitable principle requiring the consent or approval of the members`; `s 180(1) subsection (1) prejudices an enactment or provision of the company's constitution requiring consent or approval` | 5 | the first sentence and the "without prejudice" sentence |
| s 180(1)(a) | 2389 | encoded | `s 180(1) the transaction or arrangement is not liable to be set aside by virtue of a common law rule or equitable principle requiring the consent or approval of the members`; `s 180(1) subsection (1) prejudices an enactment or provision of the company's constitution requiring consent or approval` | 5 | the first sentence and the "without prejudice" sentence (row carried by 180(1)) |
| s 180(1)(b) | 2390-2392 | encoded | `s 180(1) the transaction or arrangement is not liable to be set aside by virtue of a common law rule or equitable principle requiring the consent or approval of the members`; `s 180(1) subsection (1) prejudices an enactment or provision of the company's constitution requiring consent or approval` | 5 | the first sentence and the "without prejudice" sentence (row carried by 180(1)) |
| s 180(2) | 2393 | fork | `s 180(2) the general duty applies although the case also falls within Chapter 4 or 4A` | 6 | F40 |
| s 180(2)(a) | 2394 | fork | `s 180(2) the general duty applies although the case also falls within Chapter 4 or 4A` | 6 | F40 (row carried by 180(2)) |
| s 180(2)(b) | 2395-2396 | fork | `s 180(2) the general duty applies although the case also falls within Chapter 4 or 4A` | 6 | F40 (row carried by 180(2)) |
| s 180(3) | 2397 | encoded | `s 180(3) compliance with the general duties removes the need for approval under Chapter 4 or 4A` | 2 | a flat negative |
| s 180(4) | 2398 | encoded | `s 180(4)(a) the act or omission is not a breach of the general duties because the company gave authority`; `s 180(4)(b) the general duties are not infringed by the thing done in accordance with the articles` | 6 | the lead-in of (4) |
| s 180(4)(a) | 2399 | encoded | `s 180(4)(a) the act or omission is not a breach of the general duties because the company gave authority` | 3 | limited by its own wording |
| s 180(4)(b) | 2400 | encoded | `s 180(4)(b) the general duties are not infringed by the thing done in accordance with the articles` | 3 | limited by its own wording |
| s 180(5) | 2401 | encoded | `s 180(5) the general duties have effect notwithstanding any enactment or rule of law` | 3 | "except as otherwise provided or the context otherwise requires": NOTHING |
| s 181 | 2402 | inert | - | - | reason 1: heading (not operative) |
| s 181(1) | 2403 | encoded | `s 181(1) the provisions of Chapter 2 have effect subject to section 181` | 2 | a charity |
| s 181(2) | 2404 | fork | `s 181(2)(a) the duty to avoid conflicts of interest applies to the conflict, for a charity`; `s 181(2)(b) authorisation has been given by the directors, for a charity` | 8 | F41; the substituted subsections (3) and (5) are the quoted text inside (a) and (b) |
| s 181(2)(a) | 2405-2406 | fork | `s 181(2)(a) the duty to avoid conflicts of interest applies to the conflict, for a charity` | 5 | F41 |
| s 181(2)(b) | 2407-2408 | fork | `s 181(2)(b) authorisation has been given by the directors, for a charity` | 3 | F41 |
| s 181(3) | 2409 | encoded | `s 181(3) section 180(2)(b) disapplies the duties, for a charity` | 3 | "applies only if": a closed condition |
| s 181(4) | 2410 | repealed or blank in this text | - | - | the text shows a row of dots |
| s 181(5) | 2411 | encoded | `s 181(5) the section extends to the company` | 3 | a flat negative: JUST FALSE for Scotland; NOTHING elsewhere (silent) |
| Chapter 3 | 2412 | inert | - | - | reason 1: heading (not operative) |
| s 182 | 2413 | inert | - | - | reason 1: heading (not operative) |
| s 182(1) | 2414-2415 | fork | `s 182(1) the director is obliged to declare the nature and extent of the interest to the other directors` | 7 | F38-style; the second sentence (a flat negative where s 177 applies) is the second branch |
| s 182(2) | 2416 | fork | `s 182(2) the declaration is made in a way the subsection requires` | 8 | F44 |
| s 182(2)(a) | 2417 | fork | `s 182(2) the declaration is made in a way the subsection requires` | 8 | F44 (row carried by 182(2)) |
| s 182(2)(b) | 2418 | fork | `s 182(2) the declaration is made in a way the subsection requires` | 8 | F44 (row carried by 182(2)) |
| s 182(2)(c) | 2419 | fork | `s 182(2) the declaration is made in a way the subsection requires` | 8 | F44 (row carried by 182(2)) |
| s 182(3) | 2420 | encoded | `s 182(3) a further declaration must be made` | 2 | an "if" condition |
| s 182(4) | 2421-2422 | fork | `s 182(4) the declaration was made as soon as is reasonably practicable`; `s 182(4) the failure affects the underlying duty to make the declaration`; `s 182 the director has complied with the requirements of section 182`; `s 182 the director's duty to declare the interest to the other directors` | 13 | F49; "as soon as is reasonably practicable" is a plain input (no number of days); regulative rule traced |
| s 182(5) | 2423-2424 | encoded | `s 182(5) the section requires a declaration so far as the director's awareness goes` | 5 | the "ought reasonably to be aware" sentence is carried by the inputs |
| s 182(6) | 2425 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 |
| s 182(6)(a) | 2426 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 (row carried by 182(6)) |
| s 182(6)(b) | 2427 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 (row carried by 182(6)) |
| s 182(6)(c) | 2428 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 (row carried by 182(6)) |
| s 182(6)(c)(i) | 2429 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 (row carried by 182(6)) |
| s 182(6)(c)(ii) | 2430 | fork | `s 182(6) the director need not declare the interest under section 182` | 6 | F36 (row carried by 182(6)) |
| s 183 | 2431 | inert | - | - | reason 1: heading (not operative) |
| s 183(1) | 2432 | fork | `s 183(1) the director commits an offence` | 3 | F48; takes the answer under s 182 |
| s 183(2) | 2433 | encoded | `s 183(2) the penalty for the offence` | 3 | conviction on indictment: a fine; summary conviction: the statutory maximum (a fraction of 1) |
| s 183(2)(a) | 2434 | encoded | `s 183(2) the penalty for the offence` | 3 | conviction on indictment: a fine; summary conviction: the statutory maximum (a fraction of 1) (row carried by 183(2)) |
| s 183(2)(b) | 2435 | encoded | `s 183(2) the penalty for the offence` | 3 | conviction on indictment: a fine; summary conviction: the statutory maximum (a fraction of 1) (row carried by 183(2)) |
| s 184 | 2436 | inert | - | - | reason 1: heading (not operative) |
| s 184(1) | 2437 | encoded | `s 184(1) the section applies to the declaration` | 2 | limited by its own wording |
| s 184(2) | 2438 | encoded | `s 184(2) the director has sent the notice to the other directors` | 2 | F1 |
| s 184(3) | 2439 | fork | `s 184(3) the notice is sent in a form the subsection allows` | 4 | F45; the form is the core `Form of document` |
| s 184(4) | 2440 | fork | `s 184(4) the notice is sent by a means the subsection allows` | 5 | F45 |
| s 184(4)(a) | 2441 | fork | `s 184(4) the notice is sent by a means the subsection allows` | 5 | F45 (row carried by 184(4)) |
| s 184(4)(b) | 2442 | fork | `s 184(4) the notice is sent by a means the subsection allows` | 5 | F45 (row carried by 184(4)) |
| s 184(5) | 2443 | encoded | `s 184(5)(a) the making of the declaration is deemed to form part of the proceedings at the next meeting of the directors after the notice is given`; `s 184(5)(b) the provisions of section 248 apply as if the declaration had been made at that meeting` | 4 | the effect of s 248 is coa5's |
| s 184(5)(a) | 2444 | encoded | `s 184(5)(a) the making of the declaration is deemed to form part of the proceedings at the next meeting of the directors after the notice is given` | 2 | a deeming rule |
| s 184(5)(b) | 2445 | encoded | `s 184(5)(b) the provisions of section 248 apply as if the declaration had been made at that meeting` | 2 | a deeming rule; s 248 is coa5's |
| s 185 | 2446 | inert | - | - | reason 1: heading (not operative) |
| s 185(1) | 2447 | encoded | `s 185(1) the general notice is a sufficient declaration of interest in relation to the matters to which it relates`; `s 185 the general notice is in accordance with section 185` | 8 | the second function composes (2), (3) and (4) under the seam name that ss 177(2) and 182(2) ask for |
| s 185(2) | 2448 | fork | `s 185(2) the notice is general notice` | 5 | F47 |
| s 185(2)(a) | 2449 | fork | `s 185(2) the notice is general notice` | 5 | F47 (row carried by 185(2)) |
| s 185(2)(b) | 2450 | fork | `s 185(2) the notice is general notice` | 5 | F47 (row carried by 185(2)) |
| s 185(3) | 2451 | encoded | `s 185(3) the notice states what the subsection requires` | 2 | F1 |
| s 185(4) | 2452 | encoded | `s 185(4) section 185(4) makes the general notice ineffective` | 4 | F46 (an "unless" bar: JUST TRUE = ineffective) |
| s 185(4)(a) | 2453 | encoded | `s 185(4) section 185(4) makes the general notice ineffective` | 4 | F46 (an "unless" bar: JUST TRUE = ineffective) (row carried by 185(4)) |
| s 185(4)(b) | 2454 | encoded | `s 185(4) section 185(4) makes the general notice ineffective` | 4 | F46 (an "unless" bar: JUST TRUE = ineffective) (row carried by 185(4)) |
| s 186 | 2455 | inert | - | - | reason 1: heading (not operative) |
| s 186(1) | 2456 | encoded | `s 186(1)(a) the declaration has been recorded in writing as the section requires`; `s 186(1)(b) the making of the declaration is deemed to form part of the proceedings at the next meeting of the directors after the notice is given`; `s 186(1)(c) the provisions of section 248 apply as if the declaration had been made at that meeting` | 7 | F50 |
| s 186(1)(a) | 2457 | encoded | `s 186(1)(a) the declaration has been recorded in writing as the section requires` | 3 | F50 (F5: NOTHING where the "where" is unmet) |
| s 186(1)(b) | 2458 | encoded | `s 186(1)(b) the making of the declaration is deemed to form part of the proceedings at the next meeting of the directors after the notice is given` | 2 | a deeming rule |
| s 186(1)(c) | 2459 | encoded | `s 186(1)(c) the provisions of section 248 apply as if the declaration had been made at that meeting` | 2 | a deeming rule; s 248 is coa5's |
| s 186(2) | 2460 | encoded | `s 186(2) section 186 affects the operation of section 231` | 1 | a flat negative: the constant JUST FALSE; s 231 is coa5's |
| s 187 | 2461 | inert | - | - | reason 1: heading (not operative) |
| s 187(1) | 2462 | encoded | `s 187(1) the provisions of Chapter 3 relating to the duty under section 182 apply to the person` | 3 | F51 |
| s 187(2) | 2463 | encoded | `s 187(2) section 182(2)(a) applies to the person` | 3 | F51: a flat negative for a shadow director |
| s 187(3) | 2464 | encoded | `s 187(3) section 185(4) applies to the person's general notice` | 3 | F51: a flat negative for a shadow director |
| s 187(4) | 2465 | encoded | `s 187(4) the shadow director's general notice is made ineffective by subsection (4)` | 4 | F46, F51 (an "unless" bar) |
| Chapter 4 | 2466 | inert | - | - | reason 1: heading (not operative) |
| heading: Service contracts | 2467 | inert | - | - | reason 1: heading (not operative) |
| s 188 | 2468 | inert | - | - | reason 1: heading (not operative) |
| s 188(1) | 2469 | fork | `s 188(1) section 188 applies to the provision` | 4 | F53 (a scope limit: NOTHING outside it) |
| s 188(1)(a) | 2470 | fork | `s 188(1) section 188 applies to the provision` | 4 | F53 (a scope limit: NOTHING outside it) (row carried by 188(1)) |
| s 188(1)(b) | 2471-2472 | fork | `s 188(1) section 188 applies to the provision` | 4 | F53 (a scope limit: NOTHING outside it) (row carried by 188(1)) |
| s 188(2) | 2473 | encoded | `s 188(2) section 188(2) bars the company from agreeing to the provision` | 9 | F55 (JUST TRUE = barred); the (6) exceptions are inputs |
| s 188(2)(a) | 2474 | encoded | `s 188(2) section 188(2) bars the company from agreeing to the provision` | 9 | F55 (JUST TRUE = barred); the (6) exceptions are inputs (row carried by 188(2)) |
| s 188(2)(b) | 2475 | encoded | `s 188(2) section 188(2) bars the company from agreeing to the provision` | 9 | F55 (JUST TRUE = barred); the (6) exceptions are inputs (row carried by 188(2)) |
| s 188(3) | 2476 | fork | `s 188(3) the day on which a period beginning on the start day ends`; `s 188(3) the day on which the guaranteed term of the director's employment ends` | 10 | F52; the guaranteed term is returned as the day it ends |
| s 188(3)(a) | 2477 | fork | `s 188(3) the day on which a period beginning on the start day ends`; `s 188(3) the day on which the guaranteed term of the director's employment ends` | 10 | F52; the guaranteed term is returned as the day it ends (row carried by 188(3)) |
| s 188(3)(a)(i) | 2478 | fork | `s 188(3) the day on which a period beginning on the start day ends`; `s 188(3) the day on which the guaranteed term of the director's employment ends` | 10 | F52; the guaranteed term is returned as the day it ends (row carried by 188(3)) |
| s 188(3)(a)(ii) | 2479 | fork | `s 188(3) the day on which a period beginning on the start day ends`; `s 188(3) the day on which the guaranteed term of the director's employment ends` | 10 | F52; the guaranteed term is returned as the day it ends (row carried by 188(3)) |
| s 188(3)(b) | 2480-2481 | fork | `s 188(3) the day on which a period beginning on the start day ends`; `s 188(3) the day on which the guaranteed term of the director's employment ends` | 10 | F52; the guaranteed term is returned as the day it ends (row carried by 188(3)) |
| s 188(4) | 2482 | fork | `s 188(4) the unexpired period of the original guaranteed term is added to the guaranteed term of the new contract`; `s 188(4) the day on which the guaranteed term of the new contract is treated as ending` | 5 | F54 |
| s 188(5) | 2483 | encoded | `s 188(5) the memorandum has been made available to members as the subsection requires` | 7 | F1: a memorandum with the required contents, sent to every eligible member (a written resolution) or open to inspection for 15 days ending with the meeting and at the meeting |
| s 188(5)(a) | 2484 | encoded | `s 188(5) the memorandum has been made available to members as the subsection requires` | 7 | F1: a memorandum with the required contents, sent to every eligible member (a written resolution) or open to inspection for 15 days ending with the meeting and at the meeting (row carried by 188(5)) |
| s 188(5)(b) | 2485 | encoded | `s 188(5) the memorandum has been made available to members as the subsection requires` | 7 | F1: a memorandum with the required contents, sent to every eligible member (a written resolution) or open to inspection for 15 days ending with the meeting and at the meeting (row carried by 188(5)) |
| s 188(5)(b)(i) | 2486 | encoded | `s 188(5) the memorandum has been made available to members as the subsection requires` | 7 | F1: a memorandum with the required contents, sent to every eligible member (a written resolution) or open to inspection for 15 days ending with the meeting and at the meeting (row carried by 188(5)) |
| s 188(5)(b)(ii) | 2487 | encoded | `s 188(5) the memorandum has been made available to members as the subsection requires` | 7 | F1: a memorandum with the required contents, sent to every eligible member (a written resolution) or open to inspection for 15 days ending with the meeting and at the meeting (row carried by 188(5)) |
| s 188(6) | 2488 | encoded | `s 188(6) approval is required on the part of the members of the body corporate` | 4 | F55: JUST FALSE where the body corporate is not UK-registered or is a wholly-owned subsidiary; NOTHING otherwise |
| s 188(6)(a) | 2489 | encoded | `s 188(6) approval is required on the part of the members of the body corporate` | 4 | F55: JUST FALSE where the body corporate is not UK-registered or is a wholly-owned subsidiary; NOTHING otherwise (row carried by 188(6)) |
| s 188(6)(b) | 2490 | encoded | `s 188(6) approval is required on the part of the members of the body corporate` | 4 | F55: JUST FALSE where the body corporate is not UK-registered or is a wholly-owned subsidiary; NOTHING otherwise (row carried by 188(6)) |
| s 188(7) | 2491 | encoded | `s 188(7) the employment is employment for the purposes of section 188` | 2 | a "means" definition |
| s 189 | 2492-2495 | encoded | `s 189(a) the provision is void to the extent of the contravention`; `s 189(b) the contract is deemed to contain a term entitling the company to terminate it at any time by the giving of reasonable notice` | 8 | F62; both take the answer under s 188(2) |
| heading: Substantial property transactions | 2496 | inert | - | - | reason 1: heading (not operative) |
| s 190 | 2497 | inert | - | - | reason 1: heading (not operative) |
| s 190(1) | 2498 | fork | `s 190(1) section 190(1) bars the company from entering into the arrangement` | 11 | F55, F56 |
| s 190(1)(a) | 2499 | fork | `s 190(1) section 190(1) bars the company from entering into the arrangement` | 11 | F55, F56 (row carried by 190(1)) |
| s 190(1)(b) | 2500-2502 | fork | `s 190(1) section 190(1) bars the company from entering into the arrangement` | 11 | F55, F56 (row carried by 190(1)) |
| s 190(2) | 2503 | encoded | `s 190(2) section 190(2) requires the approval of the members of the holding company` | 5 | F55: an unmet "If" answers JUST FALSE |
| s 190(3) | 2504 | encoded | `s 190(3) the company is subject to liability by reason of the failure to obtain approval` | 2 | a flat negative |
| s 190(4) | 2505 | encoded | `s 190(4) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 190(4)(a) | 2506 | encoded | `s 190(4) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 190(4)) |
| s 190(4)(b) | 2507 | encoded | `s 190(4) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 190(4)) |
| s 190(5) | 2508 | encoded | `s 190(5) the value of the non-cash asset the arrangement is treated as involving` | 3 | the aggregate of the values of the assets in the arrangement or series |
| s 190(5)(a) | 2509 | encoded | `s 190(5) the value of the non-cash asset the arrangement is treated as involving` | 3 | the aggregate of the values of the assets in the arrangement or series (row carried by 190(5)) |
| s 190(5)(b) | 2510-2511 | encoded | `s 190(5) the value of the non-cash asset the arrangement is treated as involving` | 3 | the aggregate of the values of the assets in the arrangement or series (row carried by 190(5)) |
| s 190(6) | 2512 | fork | `s 190(6) section 190 applies to the transaction` | 3 | F56: JUST FALSE where it relates to the service-contract entitlement or payment for loss of office (s 215 is coa5's); "so far as" is taken whole |
| s 190(6)(a) | 2513 | fork | `s 190(6) section 190 applies to the transaction` | 3 | F56: JUST FALSE where it relates to the service-contract entitlement or payment for loss of office (s 215 is coa5's); "so far as" is taken whole (row carried by 190(6)) |
| s 190(6)(b) | 2514 | fork | `s 190(6) section 190 applies to the transaction` | 3 | F56: JUST FALSE where it relates to the service-contract entitlement or payment for loss of office (s 215 is coa5's); "so far as" is taken whole (row carried by 190(6)) |
| s 191 | 2515 | inert | - | - | reason 1: heading (not operative) |
| s 191(1) | 2516 | inert | - | - | reason 1: a signpost sentence: "This section explains what is meant in section 190 ..." creates no rule of its own |
| s 191(2) | 2517 | fork | `s 191(2) the asset is a substantial asset in relation to the company` | 8 | F57; the pounds are the text's own |
| s 191(2)(a) | 2518 | fork | `s 191(2) the asset is a substantial asset in relation to the company` | 8 | F57; the pounds are the text's own (row carried by 191(2)) |
| s 191(2)(b) | 2519 | fork | `s 191(2) the asset is a substantial asset in relation to the company` | 8 | F57; the pounds are the text's own (row carried by 191(2)) |
| s 191(3) | 2520 | fork | `s 191(3) the company's asset value` | 3 | F57 |
| s 191(3)(a) | 2521 | fork | `s 191(3) the company's asset value` | 3 | F57 (row carried by 191(3)) |
| s 191(3)(b) | 2522 | fork | `s 191(3) the company's asset value` | 3 | F57 (row carried by 191(3)) |
| s 191(4) | 2523 | fork | `s 191(4) the most recent statutory accounts` | 4 | F57; "statutory accounts" is the record type (annual accounts prepared in accordance with Part 15) |
| s 191(5) | 2524 | encoded | `s 191(5) the determination is as at the time the arrangement is entered into` | 2 | a rule of reading: the facts are taken at the time |
| s 192 | 2525-2530 | encoded | `s 192 approval is required under section 190 for the transaction` | 4 | F58 |
| s 193 | 2531 | inert | - | - | reason 1: heading (not operative) |
| s 193(1) | 2532 | encoded | `s 193(1) section 193 applies to the company` | 5 | F58 ("unless" a members' voluntary winding up: JUST FALSE) |
| s 193(1)(a) | 2533 | encoded | `s 193(1) section 193 applies to the company` | 5 | F58 ("unless" a members' voluntary winding up: JUST FALSE) (row carried by 193(1)) |
| s 193(1)(b) | 2534 | encoded | `s 193(1) section 193 applies to the company` | 5 | F58 ("unless" a members' voluntary winding up: JUST FALSE) (row carried by 193(1)) |
| s 193(2) | 2535 | encoded | `s 193(2) approval is required under section 190` | 3 | F58 |
| s 193(2)(a) | 2536 | encoded | `s 193(2) approval is required under section 190` | 3 | F58 (row carried by 193(2)) |
| s 193(2)(b) | 2537 | encoded | `s 193(2) approval is required under section 190` | 3 | F58 (row carried by 193(2)) |
| s 194 | 2538 | inert | - | - | reason 1: heading (not operative) |
| s 194(1) | 2539 | encoded | `s 194(1) approval is required under section 190 for the transaction` | 5 | F58; the recognised investment exchange is a borrowed term |
| s 194(2) | 2540 | encoded | `s 194(2) the person is an independent broker`; `s 194(2) the exchange is a recognised investment exchange` | 6 | a "means" definition and a borrowed definition (Part 18 of the Financial Services and Markets Act 2000) |
| s 194(2)(a) | 2541 | encoded | `s 194(2) the person is an independent broker`; `s 194(2) the exchange is a recognised investment exchange` | 6 | a "means" definition and a borrowed definition (Part 18 of the Financial Services and Markets Act 2000) (row carried by 194(2)) |
| s 194(2)(b) | 2542 | encoded | `s 194(2) the person is an independent broker`; `s 194(2) the exchange is a recognised investment exchange` | 6 | a "means" definition and a borrowed definition (Part 18 of the Financial Services and Markets Act 2000) (row carried by 194(2)) |
| s 195 | 2543 | inert | - | - | reason 1: heading (not operative) |
| s 195(1) | 2544 | encoded | `s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company` | 7 | the scope sentence: carried by the first branches of the s 195(2) function |
| s 195(2) | 2545 | fork | `s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company` | 7 | F60 |
| s 195(2)(a) | 2546 | fork | `s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company` | 7 | F60 (row carried by 195(2)) |
| s 195(2)(b) | 2547 | fork | `s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company` | 7 | F60 (row carried by 195(2)) |
| s 195(2)(c) | 2548 | fork | `s 195(2) the arrangement and any transaction entered into in pursuance of it is voidable at the instance of the company` | 7 | F60 (row carried by 195(2)) |
| s 195(3) | 2549 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage`; `s 195(3)(b) the liability to indemnify the company is joint and several with that of the other person` | 15 | F59 |
| s 195(3)(a) | 2550 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage`; `s 195(3)(b) the liability to indemnify the company is joint and several with that of the other person` | 15 | F59 (row carried by 195(3)) |
| s 195(3)(b) | 2551 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage`; `s 195(3)(b) the liability to indemnify the company is joint and several with that of the other person` | 15 | F59 (row carried by 195(3)) |
| s 195(4) | 2552 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the four persons are the enum of the function |
| s 195(4)(a) | 2553 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the four persons are the enum of the function (row carried by 195(4)) |
| s 195(4)(b) | 2554 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the four persons are the enum of the function (row carried by 195(4)) |
| s 195(4)(c) | 2555 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the four persons are the enum of the function (row carried by 195(4)) |
| s 195(4)(d) | 2556 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the four persons are the enum of the function (row carried by 195(4)) |
| s 195(5) | 2557 | encoded | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | a signpost: (3) and (4) are subject to (6) and (7), which are the two defences of the same function |
| s 195(6) | 2558 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the defence of the director with whom a connected person is connected |
| s 195(7) | 2559 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the defence of ignorance of the relevant circumstances |
| s 195(7)(a) | 2560 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the defence of ignorance of the relevant circumstances (row carried by 195(7)) |
| s 195(7)(b) | 2561-2562 | fork | `s 195(3) the person is liable to account to the company for any gain and to indemnify the company for any loss or damage` | 13 | F59: the defence of ignorance of the relevant circumstances (row carried by 195(7)) |
| s 195(8) | 2563 | encoded | `s 195(8) section 195 excludes the operation of any other enactment or rule of law by virtue of which the arrangement or transaction may be called in question or any liability to the company may arise` | 1 | a flat negative: the constant JUST FALSE |
| s 196 | 2564-2568 | encoded | `s 196 the transaction or arrangement may no longer be avoided under section 195` | 6 | F61 |
| heading: Loans, quasi-loans and credit transactions | 2569 | inert | - | - | reason 1: heading (not operative) |
| s 197 | 2570 | inert | - | - | reason 1: heading (not operative) |
| s 197(1) | 2571 | encoded | `s 197(1) section 197(1) bars the company from the transaction` | 7 | F55, F64 (JUST TRUE = barred) |
| s 197(1)(a) | 2572 | encoded | `s 197(1) section 197(1) bars the company from the transaction` | 7 | F55, F64 (JUST TRUE = barred) (row carried by 197(1)) |
| s 197(1)(b) | 2573-2574 | encoded | `s 197(1) section 197(1) bars the company from the transaction` | 7 | F55, F64 (JUST TRUE = barred) (row carried by 197(1)) |
| s 197(2) | 2575 | encoded | `s 197(2) the section requires the approval of the members of the holding company` | 4 | F55: an unmet "If" answers JUST FALSE |
| s 197(3) | 2576 | fork | `s 197(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 |
| s 197(3)(a) | 2577 | fork | `s 197(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 197(3)) |
| s 197(3)(b) | 2578 | fork | `s 197(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 197(3)) |
| s 197(3)(b)(i) | 2579 | fork | `s 197(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 197(3)) |
| s 197(3)(b)(ii) | 2580 | fork | `s 197(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 197(3)) |
| s 197(4) | 2581 | encoded | `s 197(4) the memorandum sets out the matters to be disclosed` | 4 | F68 |
| s 197(4)(a) | 2582 | encoded | `s 197(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 197(4)) |
| s 197(4)(b) | 2583 | encoded | `s 197(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 197(4)) |
| s 197(4)(c) | 2584 | encoded | `s 197(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 197(4)) |
| s 197(5) | 2585 | encoded | `s 197(5) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 197(5)(a) | 2586 | encoded | `s 197(5) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 197(5)) |
| s 197(5)(b) | 2587 | encoded | `s 197(5) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 197(5)) |
| s 198 | 2588 | inert | - | - | reason 1: heading (not operative) |
| s 198(1) | 2589 | encoded | `s 198(1) the section applies to the company` | 4 | F63 |
| s 198(1)(a) | 2590 | encoded | `s 198(1) the section applies to the company` | 4 | F63 (row carried by 198(1)) |
| s 198(1)(b) | 2591 | encoded | `s 198(1) the section applies to the company` | 4 | F63 (row carried by 198(1)) |
| s 198(2) | 2592 | encoded | `s 198(2) the section bars the company from the transaction` | 9 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) |
| s 198(2)(a) | 2593 | encoded | `s 198(2) the section bars the company from the transaction` | 9 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 198(2)) |
| s 198(2)(b) | 2594-2595 | encoded | `s 198(2) the section bars the company from the transaction` | 9 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 198(2)) |
| s 198(3) | 2596 | encoded | `s 198(3) the section requires the approval of the members of the holding company` | 4 | F55: an unmet "If" answers JUST FALSE |
| s 198(4) | 2597 | fork | `s 198(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 |
| s 198(4)(a) | 2598 | fork | `s 198(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 198(4)) |
| s 198(4)(b) | 2599 | fork | `s 198(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 198(4)) |
| s 198(4)(b)(i) | 2600 | fork | `s 198(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 198(4)) |
| s 198(4)(b)(ii) | 2601 | fork | `s 198(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 198(4)) |
| s 198(5) | 2602 | encoded | `s 198(5) the memorandum sets out the matters to be disclosed` | 4 | F68 |
| s 198(5)(a) | 2603 | encoded | `s 198(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 198(5)) |
| s 198(5)(b) | 2604 | encoded | `s 198(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 198(5)) |
| s 198(5)(c) | 2605 | encoded | `s 198(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 198(5)) |
| s 198(6) | 2606 | encoded | `s 198(6) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 198(6)(a) | 2607 | encoded | `s 198(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 198(6)) |
| s 198(6)(b) | 2608 | encoded | `s 198(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 198(6)) |
| s 199 | 2609 | inert | - | - | reason 1: heading (not operative) |
| s 199(1) | 2610 | encoded | `s 199(1) the transaction is a quasi-loan` | 5 | F65 (a "means"-style definition, closed) |
| s 199(1)(a) | 2611 | encoded | `s 199(1) the transaction is a quasi-loan` | 5 | F65 (a "means"-style definition, closed) (row carried by 199(1)) |
| s 199(1)(b) | 2612 | encoded | `s 199(1) the transaction is a quasi-loan` | 5 | F65 (a "means"-style definition, closed) (row carried by 199(1)) |
| s 199(2) | 2613 | encoded | `s 199(2) the person is the person to whom the quasi-loan is made` | 2 | a reading rule: the reference is to the borrower |
| s 199(3) | 2614 | encoded | `s 199(3) the liability is a liability of the borrower under the quasi-loan` | 3 | "include": JUST TRUE for the named case, NOTHING otherwise |
| s 200 | 2615 | inert | - | - | reason 1: heading (not operative) |
| s 200(1) | 2616 | encoded | `s 200(1) the section applies to the company` | 4 | F63 |
| s 200(1)(a) | 2617 | encoded | `s 200(1) the section applies to the company` | 4 | F63 (row carried by 200(1)) |
| s 200(1)(b) | 2618 | encoded | `s 200(1) the section applies to the company` | 4 | F63 (row carried by 200(1)) |
| s 200(2) | 2619 | encoded | `s 200(2) the section bars the company from the transaction` | 10 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) |
| s 200(2)(a) | 2620 | encoded | `s 200(2) the section bars the company from the transaction` | 10 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 200(2)) |
| s 200(2)(b) | 2621-2622 | encoded | `s 200(2) the section bars the company from the transaction` | 10 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 200(2)) |
| s 200(3) | 2623 | encoded | `s 200(3) the section requires the approval of the members of the holding company` | 4 | F55: an unmet "If" answers JUST FALSE |
| s 200(4) | 2624 | fork | `s 200(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 |
| s 200(4)(a) | 2625 | fork | `s 200(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 200(4)) |
| s 200(4)(b) | 2626 | fork | `s 200(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 200(4)) |
| s 200(4)(b)(i) | 2627 | fork | `s 200(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 200(4)) |
| s 200(4)(b)(ii) | 2628 | fork | `s 200(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 200(4)) |
| s 200(5) | 2629 | encoded | `s 200(5) the memorandum sets out the matters to be disclosed` | 4 | F68 |
| s 200(5)(a) | 2630 | encoded | `s 200(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 200(5)) |
| s 200(5)(b) | 2631 | encoded | `s 200(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 200(5)) |
| s 200(5)(c) | 2632 | encoded | `s 200(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 200(5)) |
| s 200(6) | 2633 | encoded | `s 200(6) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 200(6)(a) | 2634 | encoded | `s 200(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 200(6)) |
| s 200(6)(b) | 2635 | encoded | `s 200(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 200(6)) |
| s 201 | 2636 | inert | - | - | reason 1: heading (not operative) |
| s 201(1) | 2637 | encoded | `s 201(1) the section applies to the company` | 4 | F63 |
| s 201(1)(a) | 2638 | encoded | `s 201(1) the section applies to the company` | 4 | F63 (row carried by 201(1)) |
| s 201(1)(b) | 2639 | encoded | `s 201(1) the section applies to the company` | 4 | F63 (row carried by 201(1)) |
| s 201(2) | 2640 | encoded | `s 201(2) the section bars the company from the transaction` | 12 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) |
| s 201(2)(a) | 2641 | encoded | `s 201(2) the section bars the company from the transaction` | 12 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 201(2)) |
| s 201(2)(b) | 2642-2643 | encoded | `s 201(2) the section bars the company from the transaction` | 12 | F55, F64 (JUST TRUE = barred; scope JUST FALSE gives JUST FALSE) (row carried by 201(2)) |
| s 201(3) | 2644 | encoded | `s 201(3) the section requires the approval of the members of the holding company` | 4 | F55: an unmet "If" answers JUST FALSE |
| s 201(4) | 2645 | fork | `s 201(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 |
| s 201(4)(a) | 2646 | fork | `s 201(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 201(4)) |
| s 201(4)(b) | 2647 | fork | `s 201(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 201(4)) |
| s 201(4)(b)(i) | 2648 | fork | `s 201(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 201(4)) |
| s 201(4)(b)(ii) | 2649 | fork | `s 201(4) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 201(4)) |
| s 201(5) | 2650 | encoded | `s 201(5) the memorandum sets out the matters to be disclosed` | 4 | F68 |
| s 201(5)(a) | 2651 | encoded | `s 201(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 201(5)) |
| s 201(5)(b) | 2652 | encoded | `s 201(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 201(5)) |
| s 201(5)(c) | 2653 | encoded | `s 201(5) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 201(5)) |
| s 201(6) | 2654 | encoded | `s 201(6) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 201(6)(a) | 2655 | encoded | `s 201(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 201(6)) |
| s 201(6)(b) | 2656 | encoded | `s 201(6) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 201(6)) |
| s 202 | 2657 | inert | - | - | reason 1: heading (not operative) |
| s 202(1) | 2658 | encoded | `s 202(1) the transaction is a credit transaction` | 4 | F65 |
| s 202(1)(a) | 2659 | encoded | `s 202(1) the transaction is a credit transaction` | 4 | F65 (row carried by 202(1)) |
| s 202(1)(b) | 2660 | encoded | `s 202(1) the transaction is a credit transaction` | 4 | F65 (row carried by 202(1)) |
| s 202(1)(c) | 2661 | encoded | `s 202(1) the transaction is a credit transaction` | 4 | F65 (row carried by 202(1)) |
| s 202(2) | 2662 | encoded | `s 202(2) the person is the person for whose benefit the credit transaction is entered into` | 2 | a reading rule |
| s 202(3) | 2663-2665 | encoded | `s 202(3) the agreement is a conditional sale agreement`; `s 202(3) the thing is services` | 6 | a borrowed definition (the Consumer Credit Act 1974) and a "means" definition |
| s 203 | 2666 | inert | - | - | reason 1: heading (not operative) |
| s 203(1) | 2667 | fork | `s 203(1) section 203(1) bars the company from the arrangement` | 7 | F55, F66 |
| s 203(1)(a) | 2668 | fork | `s 203(1) section 203(1) bars the company from the arrangement` | 7 | F55, F66 (row carried by 203(1)) |
| s 203(1)(a)(i) | 2669 | fork | `s 203(1) section 203(1) bars the company from the arrangement` | 7 | F55, F66 (row carried by 203(1)) |
| s 203(1)(a)(ii) | 2670 | fork | `s 203(1) section 203(1) bars the company from the arrangement` | 7 | F55, F66 (row carried by 203(1)) |
| s 203(1)(b) | 2671-2672 | fork | `s 203(1) section 203(1) bars the company from the arrangement` | 7 | F55, F66 (row carried by 203(1)) |
| s 203(2) | 2673 | encoded | `s 203(2) the section requires the approval of the members of the holding company` | 4 | F55 |
| s 203(3) | 2674 | fork | `s 203(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 |
| s 203(3)(a) | 2675 | fork | `s 203(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 203(3)) |
| s 203(3)(b) | 2676 | fork | `s 203(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 203(3)) |
| s 203(3)(b)(i) | 2677 | fork | `s 203(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 203(3)) |
| s 203(3)(b)(ii) | 2678 | fork | `s 203(3) the memorandum has been made available to members as the subsection requires` | 7 | F68, F69 (row carried by 203(3)) |
| s 203(4) | 2679 | encoded | `s 203(4) the memorandum sets out the matters to be disclosed` | 4 | F68 |
| s 203(4)(a) | 2680 | encoded | `s 203(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 203(4)) |
| s 203(4)(b) | 2681 | encoded | `s 203(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 203(4)) |
| s 203(4)(c) | 2682 | encoded | `s 203(4) the memorandum sets out the matters to be disclosed` | 4 | F68 (row carried by 203(4)) |
| s 203(5) | 2683 | encoded | `s 203(5) approval is required on the part of the members of the body corporate` | 4 | F55 |
| s 203(5)(a) | 2684 | encoded | `s 203(5) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 203(5)) |
| s 203(5)(b) | 2685 | encoded | `s 203(5) approval is required on the part of the members of the body corporate` | 4 | F55 (row carried by 203(5)) |
| s 203(6) | 2686 | fork | `s 203(6) the date on which the transaction is treated as having been entered into` | 2 | F66 (a rule of reading: the date of the arrangement) |
| s 204 | 2687 | inert | - | - | reason 1: heading (not operative) |
| s 204(1) | 2688 | fork | `s 204(1) approval is required under section 197, 198, 200 or 201 for the thing done` | 4 | F67 |
| s 204(1)(a) | 2689 | fork | `s 204(1) approval is required under section 197, 198, 200 or 201 for the thing done` | 4 | F67 (row carried by 204(1)) |
| s 204(1)(a)(i) | 2690 | fork | `s 204(1) approval is required under section 197, 198, 200 or 201 for the thing done` | 4 | F67 (row carried by 204(1)) |
| s 204(1)(a)(ii) | 2691 | fork | `s 204(1) approval is required under section 197, 198, 200 or 201 for the thing done` | 4 | F67 (row carried by 204(1)) |
| s 204(1)(b) | 2692 | fork | `s 204(1) approval is required under section 197, 198, 200 or 201 for the thing done` | 4 | F67 (row carried by 204(1)) |
| s 204(2) | 2693 | fork | `s 204(2) section 204 authorises the company to enter into the transaction` | 7 | F67: the 50,000 pounds is the text's own; the aggregate must exceed it to remove the authority |
| s 204(2)(a) | 2694 | fork | `s 204(2) section 204 authorises the company to enter into the transaction` | 7 | F67: the 50,000 pounds is the text's own; the aggregate must exceed it to remove the authority (row carried by 204(2)) |
| s 204(2)(b) | 2695-2696 | fork | `s 204(2) section 204 authorises the company to enter into the transaction` | 7 | F67: the 50,000 pounds is the text's own; the aggregate must exceed it to remove the authority (row carried by 204(2)) |
| s 156C(1) "the relevant day" | 2081 | encoded | `s 156C(1) the relevant day` | 2 | F9 |
| s 159A(2) "disqualified under the directors disqualification legislation" (Part 1) | 2115 | encoded | `s 159A(2) the person is disqualified under the directors disqualification legislation` | 9 | F14 |
| s 159A(2) "disqualified under the directors disqualification legislation" (Part 2) | 2118 | encoded | `s 159A(2) the person is disqualified under the directors disqualification legislation` | 9 | F14 |
| s 167G(4) "permission of a court to act" | 2201 | encoded | `s 167G(4) the permission is permission of a court to act` | 3 | a "means" definition |
| s 167J(2) "relevant former name" | 2224 | encoded | `s 167J(2) the name is a relevant former name` | 7 | F22 |
| s 167J(3) "former name" | 2231 | encoded | `s 167J(3) the name is a former name` | 2 | a "means" definition |
| s 167J(3) "name" | 2232 | encoded | `s 167J(3) the item is the individual's name` | 2 | a "means" definition |
| s 175(7) "conflict of interest" (includes) | 2355 | encoded | `s 175(7) the conflict is a conflict of interest for the purposes of the section` | 2 | "includes" |
| s 176(2) "third party" | 2360 | encoded | `s 176(2) the person is a third party` | 4 | a "means" definition |
| s 185(2) "general notice" | 2448 | encoded | `s 185(2) the notice is general notice` | 5 | F47 |
| s 188(3) "the guaranteed term" of a director's employment | 2476 | encoded | `s 188(3) the day on which the guaranteed term of the director's employment ends` | 5 | F52 (the term is defined in the text without quotation marks) |
| s 188(7) "employment" | 2491 | encoded | `s 188(7) the employment is employment for the purposes of section 188` | 2 | a "means" definition |
| s 190(1) "substantial non-cash asset" (see s 191) | 2502 | encoded | `s 191(2) the asset is a substantial asset in relation to the company` | 8 | a pointer to s 191 |
| s 191 "substantial" | 2516 | encoded | `s 191(2) the asset is a substantial asset in relation to the company` | 8 | F57 |
| s 191(3) "asset value" | 2520 | encoded | `s 191(3) the company's asset value` | 3 | F57 |
| s 191(4) "statutory accounts" and "most recent" | 2523 | encoded | `s 191(4) the most recent statutory accounts` | 4 | F57 |
| s 194(2) "independent broker" | 2541 | encoded | `s 194(2) the person is an independent broker` | 3 | a "means" definition |
| s 194(2) "recognised investment exchange" | 2542 | encoded | `s 194(2) the exchange is a recognised investment exchange` | 3 | a borrowed definition |
| s 199(1) "quasi-loan" (and "the creditor", "the borrower") | 2610 | encoded | `s 199(1) the transaction is a quasi-loan`; `s 199(2) the person is the person to whom the quasi-loan is made` | 7 | F65; the creditor and the borrower are the two parties the definition names |
| s 202(1) "credit transaction" (and "the creditor") | 2658 | encoded | `s 202(1) the transaction is a credit transaction`; `s 202(2) the person is the person for whose benefit the credit transaction is entered into` | 6 | F65 |
| s 202(3) "conditional sale agreement" | 2664 | encoded | `s 202(3) the agreement is a conditional sale agreement` | 3 | a borrowed definition |
| s 202(3) "services" | 2665 | encoded | `s 202(3) the thing is services` | 3 | a "means" definition |

## Fork register (coa4)

Every ambiguity, the readings seen, the one taken, and the text that licenses each. "The 2026-11-05 ruling" is the ruling set out in the brief on negatives and legal effects: (a) a failed "if" or "unless" condition is a no, (b) a wording-limited grant is not, (c) a scope sentence with no "only" answers NOTHING outside its wording, (d) an "until" bar is the bar itself.

- **F1** (every bare "must" requirement not met: s 154(1), s 154(2), s 155(1), s 156(2) (content), s 156(2) (period), s 156(3), s 156(4), s 156(5); and the same site in later modules): the 2026-11-05 ruling leaves "a bare must not done" to the encoder. Taken: the function is named "the requirement is met" (or "the company has complied"), and when the fact is not met it answers JUST FALSE with the comment `FALSE-kind ... "must have ..."`; when the section's own scope does not hold (a public company asked under s 154(1)) it answers NOTHING (limited by its own wording, the 2026-11-05 scope ruling (c)). Licence: "must", read as the statement of what the requirement is. Other reading: NOTHING for an unmet bare "must", since "must" states the duty and not that its breach is a "no" the text pronounces.
- **F2** (s 156(7), the penalty): the text file runs two wordings together: "a daily default fine not exceeding one-tenth of level 5 on the standard scale" and, with no space, "one-tenth of the greater of £5,000 or level 4 on the standard scale". The rendering "may carry more than one extent version of a provision, and prospective provisions" (inputs/SOURCES.md), and the text does not say which is in force. Taken: both are encoded as separate functions (the first as the core `Penalty`, the second as a pounds function over an input record of the scale in pounds, because the core has no "greater of" constructor: NEEDS-CORE.md), and the seat asks which wording applies. Other reading: one wording only; neither can be chosen from the sources.
- **F3** (s 156(2), "not less than one month or more than three months after the date on which the direction is given"): `add months` clamps to the last day of a shorter month, so one month after 31 January is 28 (or 29) February. Taken: the period may end on any day from one calendar month to three calendar months after the day of the direction, both ends included (tests use days that exist in every month). Other reading: one month after 31 January is 3 March (the day count rolls forward). The text does not decide.
- **F4** (s 156(1), "If it appears to the Secretary of State that a company is in breach ... the Secretary of State may give the company a direction"): Taken: a grant ("may give") behind an "If it appears" gate, so when it does not appear the answer is NOTHING (a grant limited by its own wording and the case outside the limit, Guide section 5 "In short"). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F5** (compliance questions with a condition: s 156(4) "Where the company is in breach of section 154 or 155, it must comply", s 156(5) "If the company has already made the necessary appointment or appointments", and the same site in s 167G(3)(c), (e), (f), s 167H(4), s 169(3), s 182 and others): the 2026-11-05 ruling leaves "a duty whose 'if' or 'where' is unmet" to the encoder. Taken: for the question "has the company complied / does the notice contain what the paragraph requires", an unmet "where" or "if" answers NOTHING (limited by its own wording: the paragraph says nothing of a company or notice outside its condition); for an effect or an "is obliged" question (does the person cease to hold office; is the company obliged to give notice) an unmet "where" or "if" answers JUST FALSE, as rulings (a) and (b) of 2026-11-05 and marginal reading (a) say. Other reading: JUST FALSE for the compliance questions too.
- **F6** (the offence sections: s 156(6), s 156A(6); and the same pattern in ss 167L, 167M(4), 167N(4), 183): the text names the company and "every officer of the company who is in default", and says "a shadow director is treated as an officer". Taken: the company's limb is JUST TRUE when it failed and JUST FALSE when it did not ("If a company fails ..."); the officer's limb is JUST TRUE for an officer (or a shadow director) in default, and NOTHING for an officer not in default (the case falls outside the limit "who is in default") and NOTHING for a person who is not an officer (the list is not closed with "only"). Whether the person is an officer (s 1173(1)), a shadow director (s 251) and in default (s 1121) are inputs from other parts (MAYBE BOOLEAN; a NOTHING input gives NOTHING). Other reading: JUST FALSE for an officer not in default, since only officers in default commit the offence.
- **F7** (s 156A(1), s 157(1), s 159A(1): "may not be appointed"): Taken: each is a function "section X bars the appointment", JUST TRUE meaning barred, so the consequence rules ((3) or (4): "void") take that answer as an input. The "unless" or "if" in the text decides the polarity: JUST FALSE for the person the "unless" lets through. Other reading: a function "the appointment is allowed", the mirror image.
- **F8** (s 156C(2), "Where (a) a person appointed ... before section 156A comes into force is not a natural person, and (b) the case is not one excepted from that section by regulations under section 156B"): Taken: the day section 156A comes into force and the exception are inputs; a failed "where" answers JUST FALSE (ruling (b) of 2026-11-05); before the relevant day the answer is JUST FALSE ("on the relevant day"), on or after it JUST TRUE. Other reading: NOTHING for a failed "where".
- **F9** (s 156C(1), "the day after the end of the period of 12 months beginning with the day on which section 156A comes into force"): Taken: a period of 12 months beginning with day C ends the day before C's anniversary, so the relevant day is C plus twelve months (`add months`, which clamps a 29 February to 28 February). Other reading: none seen apart from the clamp.
- **F10** (s 156(5A), "Nothing in subsection (4) or (5) affects the duty imposed by section 167G"): Taken: a flat negative, encoded as the constant `JUST FALSE` ("complying with the direction discharges the 167G duty": no). Other reading: inert (a saving that decides nothing).
- **F11** (s 157(1), s 157(3), s 158(3), "has attained the age of 16 years"): Taken: the person attains 16 on the sixteenth anniversary of the date of birth, so the test is "the day is not before `add years` (date of birth) 16". The text does not say how a 29 February birthday is counted (`add years` clamps to 28 February in a non-leap year; at 16 years from 2000 or any year divisible by 4 the date exists, so the tests are unaffected). Other reading: a person born on 29 February attains the age on 1 March.
- **F12** (s 157(3), "is not effective also to make him a director of the company until he attains the age of 16 years"): Taken, by the ruling of 2026-11-05 (d) on "until" bars: the function is the bar, "the appointment to the other office cannot yet make the person a director": JUST TRUE before the sixteenth birthday, JUST FALSE from it (the text does not say the appointment has taken effect, only that the bar lifts); where the office is not held by a corporation sole or by virtue of another office, JUST FALSE (the "where" ruling (b)). Other reading: a function "the appointment is effective", NOTHING before the date.
- **F13** (s 158(3), "a person who was appointed by virtue of the regulations and who has not since attained the age of 16 years ceases to hold office"): Taken: JUST FALSE when the person has since attained 16 (the person is not in the class the subsection names) and when the appointment or the ceasing of the circumstances is not shown ("If ..."). Other reading: NOTHING for the person who has since attained 16 (a limit in the text's own wording).
- **F14** (s 159A(2), the table): Taken: (i) the table is data, twelve rows (six per Part), and the Part comes from the place of registration (England and Wales and Scotland: Part 1; Northern Ireland: Part 2); (ii) a row disqualifies when its circumstance (column 1) holds and no permission of a court, authority of a licence or exception by virtue of that row's column 2 applies to what the person is doing ("Except in the application of the provision in relation to P acting in a capacity, or doing anything, for which P has the permission ... or in respect of which an exception applies, by virtue of"); (iii) when no row of the Part holds, JUST FALSE ("a person (P) is disqualified ... if:" read as closed, marginal reading (a)); (iv) the facts of each row (for example "P is disqualified as mentioned in section 1184(2)(a) or (b)", which turns on s 1184, coa25) are plain inputs. Other reading: NOTHING for a person in no row, because the table is a list of "if" rows not closed with "only".
- **F15** (s 159A(1), "A person may not be appointed a director of a company if the person is disqualified"): Taken: the bar function takes the answer to s 159A(2) as a MAYBE BOOLEAN input; not disqualified answers JUST FALSE (marginal reading (a)); NOTHING passes through. Other reading: NOTHING when the person is not disqualified (the text does not say the person may be appointed).
- **F16** (s 160(1) and (4)): Taken: the motion is barred (JUST TRUE) when the company is public, the motion is for two or more persons by a single resolution, and no preliminary resolution was first agreed "without any vote being given against it"; JUST FALSE when that resolution was so agreed ("unless"); JUST FALSE for a resolution amending the articles ("Nothing in this section applies": a flat negative); NOTHING for a private company or a motion for one person (a scope limit with no "only", ruling (c) of 2026-11-05). Other reading: JUST FALSE for the out-of-scope cases.
- **F17** (s 161(1) and (2)): Taken: the four listed defects and the void resolution of section 160 give JUST TRUE; any other defect gives NOTHING (the list is introduced with "notwithstanding that it is afterwards discovered" and not closed with "only"); a person who was not "acting as a director" gives NOTHING. Other reading: JUST TRUE for any defect ("notwithstanding").
- **F18** (s 157(2)): Taken: the subsection fixes one case, an appointment made before the person is 16 but not to take effect until the person is 16, and says the appointment's validity is unaffected: JUST TRUE; any other case NOTHING. Other reading: none seen.
- **F19** (s 167G(6), s 167H(3), s 167I(5), "within the period of 14 days beginning with the day on which ..."): Taken: the first day is the day of the event, so the period is the event day and the 13 days after it; the last day is the event day plus 13; a notice given before the event day is outside the period (JUST FALSE, ruling (a) of 2026-11-05 on a period the text fixes in its own words). As a regulative rule the clock is 0 on the event day and the duty is `WITHIN 13`. Other reading: 14 days counted from the day after, so the last day is the event day plus 14.
- **F20** (s 167M(2), "A company must ensure that an individual does not act as a director unless the individual's identity is verified"): Taken: the text states the duty without a defence, so the company contravenes whenever the individual acts without verification (the same inputs as s 167M(1)). Other reading: a company that took all reasonable steps does not contravene.
- **F21** (s 167G(3)(d), "a statement that the person is not (i) disqualified under the directors disqualification legislation, or (ii) otherwise ineligible by virtue of any enactment for appointment as a director"): Taken: the statement must cover both limbs (the person is neither disqualified nor otherwise ineligible), so the function needs both statements and answers JUST FALSE if either is missing. Other reading: "or" makes either statement enough.
- **F22** (s 167J(2), "relevant former name"): Taken: a former name is a relevant one unless it falls in one of the exceptions, each a flat negative ("other than"); the 16-year exception compares the day the name was changed or disused with the person's sixteenth birthday (before it: excepted); the 20-year exception is met when the day in question is on or after the twentieth anniversary of the day the name was changed or disused ("has been changed or disused for 20 years or more"). The day a name was "changed or disused" is a plain input. Other reading: none seen apart from the leap-day clamp of fork F11.
- **F23** (s 167K(1), the corporate director's required information): Taken: items (a) to (c) are always required; (d) the registered number only for a limited company that is a UK-registered company (JUST FALSE otherwise: "in the case of"); (e) "in any other case": the legal form and governing law, and the register entry "if applicable" (JUST FALSE where the body is not entered in a register); the inputs are the keel's `s 3(1)` and `s 1158` answers (BOOLEAN suffices). Other reading: NOTHING for the items outside the case each paragraph names.
- **F24** (s 167L(1), "fails, without reasonable excuse, to comply with section 167G, 167H or 167I"): Taken: the failure and the absence of a reasonable excuse are one plain fact in the text's own words; the court's judgment of "reasonable excuse" is the person's to state. A company that has an excuse answers JUST FALSE for the offence. Other reading: the excuse is a defence to be proved (not a limb of the offence).
- **F25** (s 167N(5), "It is a defence for a person charged with an offence under this section to prove that they reasonably believed that notice had been given"): Taken, by the ruling of 2026-11-05 (b): when the belief is not proved the answer is JUST FALSE for this provision's defence, worded "this section gives the person a defence on these facts" and never "no defence at all"; a person not charged with an offence under the section is outside the limit and answers NOTHING. Other reading: NOTHING when not proved.
- **F26** (s 167N(4), "Where the offence is committed by a firm, every officer of the firm who is in default also commits the offence"): the subsection has no sentence treating a shadow director as an officer (ss 156, 156A, 167L and 167M have one), so the function takes no shadow-director input; an officer in default is JUST TRUE, anyone else NOTHING. Other reading: a shadow director of the firm is treated as an officer here too.
- **F27** (s 167M(6), s 167N(7), "The only consequences ... are the offences provided for by this section"): Taken: a closed list ("only"): the offence is JUST TRUE; the invalidity of the person's acts and any other consequence are JUST FALSE ("a contravention does not in any way affect the validity"). Other reading: none seen.
- **F28** (s 168(1), "A company may by ordinary resolution at a meeting remove a director ... notwithstanding anything in any agreement between it and him"): Taken: the power is exercised by an ordinary resolution (s 282, the seam) passed at a meeting (on a show of hands or a poll); a resolution that is not an ordinary resolution, and a written resolution, are outside the grant and answer NOTHING (limited by its own wording); an agreement saying the director may not be removed does not change the answer. Other reading: JUST FALSE for a written resolution (s 288 of coa7 excludes it).
- **F29** (s 169(1) and (3), "forthwith"): Taken: "forthwith" gives no number of days, so it is not a deadline the encoding can state: the question is a plain fact (the company has forthwith sent the copy), and the regulative rules are a `MUST` with no `WITHIN` (accepted on the stable binary: a trace with the event is FULFILLED and with no event leaves the obligation standing). No consequence is stated by the text, so no `LEST` is invented. Other reading: a short fixed number of days.
- **F30** (s 169(3), "the company shall, unless the representations are received by it too late for it to do so"): Taken: the obligation to state the fact of the representations and to send a copy arises when notice is given, the director makes written representations of reasonable length and requests their notification, and they are not received too late; otherwise JUST FALSE ("unless"). The two duties (a) and (b) are separate functions that take the obligation's answer as an input and answer NOTHING where it does not arise (fork F5). Other reading: NOTHING for a late receipt (the text gives (4) as the remedy).
- **F31** (s 169(5), (6)): Taken: (5) the court's being "satisfied that the rights ... are being abused" is the court's judgment and a plain input, and "need not be sent ... if" unmet is JUST FALSE (marginal reading (a)); (6) "may order ... notwithstanding that he is not a party": JUST TRUE for an application under (5) whether or not the director is a party, NOTHING for any other application. Other reading: NOTHING for an unmet "if" in (5). (Subsection (4) is F71.)
- **F32** (s 169A(3), "the reference in subsection (1) to a person who becomes disqualified includes a reference to a person who, at that time, is already disqualified"): Taken: "includes" lists without closing: the case named is JUST TRUE and any other NOTHING. Other reading: none seen.
- **F33** (s 168(4), the retirement of a person appointed in place of a person removed): Taken: the function answers the date the person is "treated ... as if he had become director" (the day the person replaced was last appointed), a MAYBE DATE; NOTHING when the person was not appointed in place of a person removed. Other reading: none seen.
- **F34** (s 170(2), "A person who ceases to be a director continues to be subject (a) to the duty in section 175 ... as regards the exploitation of any property, information or opportunity of which he became aware at a time when he was a director, and (b) to the duty in section 176 ... as regards things done or omitted by him before he ceased"): Taken: JUST TRUE for the former director in the two named matters; NOTHING for the same duties outside those matters, for the other five duties (the list is not closed with "only"), and for a person who has not ceased to be a director. Other reading: JUST FALSE for the other duties ("continues to be subject to" these two only).
- **F35** (ss 171 to 177, the open-textured duties): the text asks for "good faith", "considers", "reasonably diligent", "cannot reasonably be regarded as likely to give rise to a conflict of interest" and the like. Taken: each judgment is a plain input the person (or the court) supplies; nothing is guessed. s 172(1) is JUST TRUE only if the director acts as he considers, in good faith, would be most likely to promote the object of the duty (s 172(2) says what the object is) AND has regard to each of the six matters (a) to (f) ("have regard (amongst other matters) to"); JUST FALSE otherwise (F1). s 174(1) is JUST TRUE only if the director's care, skill and diligence reaches both standards of (2) (the objective one and the one for the director's own knowledge), since "This means" the care that a reasonably diligent person with (a) and (b) would exercise. Other reading: s 172's list is illustrative ("amongst other matters"), so a director who did not have regard to one matter answers NOTHING.
- **F36** (s 177(6) and s 182(6), "if, or to the extent that"): Taken: each limb is a yes or no for the part of the interest in question, supplied by the person; the encoding does not split an interest into parts. Other reading: a fraction of the interest.
- **F37** (s 175(1), (3), (4), (5), (6)): Taken: (3) is a flat negative (the duty "does not apply" to a conflict arising in relation to a transaction or arrangement with the company): JUST FALSE for "the duty applies"; (4) names two cases in which the duty "is not infringed" and says nothing of any other: JUST TRUE for them, NOTHING otherwise; (1) combines them, answering JUST TRUE where there is no conflict situation, where (3) removes the duty or where (4) applies, and JUST FALSE otherwise (a bare "must" not done, F1); (5) distinguishes a public company from a private one by the s 4(2) seam ("where" unmet answers JUST FALSE); (6) says the authorisation is "effective only if" and is closed. Other reading: the infringement outside (4) is not stated by the text and answers NOTHING.
- **F38** (s 177(1) and (4)): Taken: the duty is split into "is the director obliged to declare" (the text's conditions: interested, aware by (5), not excused by (6); an unmet "if" or a flat negative answers JUST FALSE) and "has the director made the declaration the section requires" (declared, and before the company entered into the transaction; a fixed point in time and not a number of days, so the regulative rule has no `WITHIN`). The latter answers NOTHING where no declaration is required (F5). Other reading: one function.
- **F39** (s 177(2), "The declaration may (but need not) be made (a) at a meeting of the directors, or (b) by notice ... in accordance with section 184 or 185"): Taken: JUST TRUE for the listed ways; any other way answers NOTHING (the subsection permits and does not forbid another way); the s 184 and s 185 answers are MAYBE BOOLEAN inputs (this part's own functions answer them). Other reading: JUST FALSE for any other way ("may be made ..." read as closed).
- **F40** (s 180(2), "The application of the general duties is not affected by the fact that the case also falls within Chapter 4 ... or 4A, except that ... it is not necessary also to comply with section 175 ... or section 176"): Taken: for a case within Chapter 4 or 4A the answer to "does the general duty still apply" is JUST TRUE ("not affected"), except that for ss 175 and 176, where approval is given or the matter is one for which approval is not needed, it is JUST FALSE (the "except" is met); a case outside Chapters 4 and 4A answers NOTHING (a scope limit). Chapter 4A is coa5's (ss 226A to 226F). Other reading: NOTHING where the "except" is met.
- **F41** (s 181(2)(a), the substituted s 175(3) for a charity, "This duty does not apply ... if or to the extent that the company's articles allow that duty to be so disapplied, which they may do only in relation to descriptions of transaction or arrangement specified in the company's articles"): Taken: the duty does not apply (JUST FALSE for "applies") when the articles allow it for a description of transaction they specify; it applies (JUST TRUE) when the articles do not so allow (the "only" closes the permission); a conflict not arising in relation to a transaction or arrangement with the company answers NOTHING (the substituted subsection says nothing of it). Other reading: NOTHING where the articles do not allow it.
- **F42** (the regulative rules of ss 171 to 177): the text gives no deadline and no consequence for the general duties (the civil consequences are s 178, which points to the common law outside the sources), so each rule is a bare `MUST` (or `SHANT` for s 176(1)) with no `WITHIN`; `LEST` is not written for a `MUST` with no deadline, and for `SHANT` the default applies. A `#TRACE` with the act shows a `FULFILLED` for a `MUST`, and, for the `SHANT`, a breach; with no act the duty stays standing. Other reading: none.
- **F43** (s 178(2), "(with the exception of section 174 ...)"): the 2026-11-05 ruling leaves an "except" once met to the encoder. Taken: JUST FALSE for the s 174 duty ("is enforceable in the same way as any other fiduciary duty": no, by the exception) and JUST TRUE for the other six. Other reading: NOTHING for s 174 (the text says only that s 174 is not enforced as a fiduciary duty, not that it is not enforceable at all).
- **F44** (s 182(2), "The declaration must be made (a) at a meeting of the directors, or (b) by notice in writing (see section 184), or (c) by general notice (see section 185)"): Taken: a closed list of ways ("must"): JUST TRUE for any one, JUST FALSE for none; a shadow director cannot use (a) (s 187(2): an input); the answers of s 184 and s 185 are MAYBE BOOLEAN inputs and a NOTHING gives NOTHING unless another way is already JUST TRUE. Other reading: NOTHING for any other way.
- **F45** (s 184(3) and (4), "The notice may be sent in hard copy form or, if the recipient has agreed to receive it in electronic form, in an agreed electronic form"; "(a) by hand or by post, or (b) if the recipient has agreed to receive it by electronic means, by agreed electronic means"): Taken: hard copy, hand and post are JUST TRUE; electronic form or means without the recipient's agreement is JUST FALSE (an "if" unmet); any other means answers NOTHING (the subsection permits and does not forbid another). Other reading: JUST FALSE for another means.
- **F46** (s 185(4) and s 187(4), "General notice is not effective unless ..."): Taken: the function says whether the subsection makes the general notice ineffective (JUST TRUE = it does not yet satisfy (a) or (b); JUST FALSE once it does, and for a shadow director, whom s 187(3) takes out of subsection (4)); s 187(4) is the same kind of bar for a shadow director's general notice and the notice in writing. The `s 185 the general notice is in accordance with section 185` function composes (2), (3) and (4). Other reading: a function "the general notice is effective" (the mirror image).
- **F47** (s 185(2)(b), "is connected with a specified person (other than a body corporate or firm)"): Taken: this is the "(other than X)" site of the 2026-11-05 ruling: a specified person who is a body corporate or firm falls under (a) (the director's interest in it), so the input of limb (b) is true only for a specified person who is not a body corporate or firm; "connected with" is s 252 (coa5), a MAYBE BOOLEAN input (NOTHING passes through); where neither limb is given the answer is JUST FALSE ("General notice is notice given ... to the effect that"). Other reading: NOTHING for a person who is a body corporate or firm.
- **F48** (s 183(1), "A director who fails to comply with the requirements of section 182 commits an offence"): Taken: the offence takes the answer to the `s 182 the director has complied` function: JUST FALSE (not complied) gives the offence (JUST TRUE); JUST TRUE gives JUST FALSE; NOTHING gives NOTHING. The text names no "reasonable excuse" defence here. Other reading: none seen.
- **F49** (s 182(4), "must be made as soon as is reasonably practicable. Failure to comply with this requirement does not affect the underlying duty to make the declaration"): Taken: the timing is a plain input (the text gives no number of days); the second sentence is a flat negative: JUST FALSE for "the failure affects the underlying duty" where there was a failure, NOTHING otherwise; the regulative rule has a bare `MUST` and no `WITHIN`. Other reading: none seen.
- **F50** (s 186(1), "Where a declaration of interest under section 182 is required of a sole director of a company that is required to have more than one director"): Taken: the compliance question (a) answers NOTHING where the "where" is unmet (F5); (b) and (c) are deeming rules, JUST TRUE where the "where" is met and NOTHING otherwise. That the company "is required to have more than one director" is a plain fact (s 154(2) makes a public company one). Other reading: JUST FALSE where unmet.
- **F51** (s 187, "The provisions of this Chapter relating to the duty under section 182 apply to a shadow director as to a director, but with the following adaptations"): Taken: (1) JUST TRUE for a shadow director (s 251 is a MAYBE BOOLEAN input), NOTHING otherwise; (2) and (3) are flat negatives for a shadow director: JUST FALSE for "section 182(2)(a) applies" and "section 185(4) applies"; (4) is the bar of F46. Other reading: NOTHING for the flat negatives.
- **F52** (s 188(3), the guaranteed term): Taken: the term is returned as the day it ends, counting from the first day of the employment: the fixed period of paragraph (a), then the notice period of paragraph (b), chained ("the aggregate of those periods"); a period in months or years is counted by the calendar (`add months`, `add years`, which clamp), in weeks and days by the day count, and a period in working days answers NOTHING (the working-day calendar is the keel's s 1173(1) and is not taken here); where neither paragraph applies the aggregate of the periods is none and the term is nil. Other reading: a contract with neither has no guaranteed term (NOTHING).
- **F53** (s 188(1), "is, or may be, longer than two years"): Taken: the longest the provision allows is the day its guaranteed term ends; it is "longer than two years" when that day is after the second anniversary of the first day (exactly two years is not longer); the employment must be with the company or, for a director of a holding company, within the group; outside that (a scope sentence with no "only") the answer is NOTHING (ruling (c) of 2026-11-05). Other reading: JUST FALSE for a term not longer than two years.
- **F54** (s 188(4), "If more than six months before the end of the guaranteed term ... the company enters into a further service contract (otherwise than in pursuance of a right conferred, by or under the original contract, on the other party to it)"): Taken: "more than six months before the end" is `add months` (entry day) 6 earlier than the end day (adding to the earlier date avoids the month-subtraction trap); entry exactly six months before the end is not "more than"; the parenthetical is an "(other than X)" site (ruling of 2026-11-05): when the further contract is in pursuance of such a right the answer is JUST FALSE; the unexpired period is the number of days from the entry day to the end of the original term and is added to the new term's end day. Other reading: NOTHING for the parenthetical met.
- **F55** (the bar functions of ss 188(2), 190(1), 190(2) and, in coa4-approval-loans.l4, 197 to 203): Taken: a "may not ... unless approved" subsection is a function "section X bars the company", JUST TRUE meaning the company is barred (the approval is missing); JUST FALSE where approved, conditional on approval (s 190 only), or excused ("No approval is required ... on the part of the members of a body corporate that is not a UK-registered company or is a wholly-owned subsidiary": the (6)-type function answers JUST FALSE for the excused body corporate and NOTHING for any other, because the subsection says only when approval is not required); NOTHING where the arrangement is outside the subsection's own wording or a borrowed answer (`s 252` connected, `s 256` associated, `s 1158`, `s 1159(2)`) is not known. The "unless the arrangement has been approved" is a flat condition ("unless"), so the approved case is JUST FALSE. Other reading: JUST FALSE for the outside-the-wording cases.
- **F56** (s 190(1), (6) and the exceptions): Taken: the other party must be a director of the company or its holding company or a person connected with such a director (s 252: MAYBE BOOLEAN); the asset must be substantial (s 191: MAYBE BOOLEAN); the exceptions of ss 190(6), 192, 193 and 194 are one BOOLEAN input to the s 190(1) function, each exception being its own function answering JUST FALSE (approval not required) or NOTHING; s 190(6) "so far as it relates" is taken whole or not at all (the person states whether the transaction relates to the service-contract entitlement or the payment for loss of office; s 215 is coa5's). Other reading: a transaction that partly relates is partly outside the section.
- **F57** (s 191): Taken: the thresholds are the text's own (more than 10% of the asset value and more than 5,000 pounds, or more than 100,000 pounds: all "exceeds" and "more than", so equality is not enough); the asset value is the net assets by the most recent statutory accounts (the accounts whose time for sending out to members, s 424, is the most recent), or, if none have been prepared, the called-up share capital; the accounts are a list of records (the day the time falls, the net assets); the time of determination is the time the arrangement is entered into (a rule of reading: the facts are those at that time). Other reading: none seen.
- **F58** (ss 192 to 194, "Approval is not required under section 190 ..."): Taken: each exception is a function "approval is required under section 190 for the transaction": JUST FALSE where the exception's wording is met, NOTHING otherwise (the section says only when approval is not required); s 193(1) "applies to a company (a) that is being wound up (unless the winding up is a members' voluntary winding up), or (b) that is in administration": administration or a winding up that is not a members' voluntary one gives JUST TRUE; a members' voluntary winding up gives JUST FALSE (the "unless" is met) and a company in neither gives NOTHING. "recognised investment exchange" is a borrowed definition (Part 18 of the Financial Services and Markets Act 2000: a MAYBE BOOLEAN input). Other reading: JUST FALSE for "approval is required" where no exception is met.
- **F59** (s 195(3), (4), (6), (7)): Taken: the persons liable are the four classes of (4) (the director with whom the company dealt; a connected person with whom it dealt; the director with whom that person is connected; any other director who authorised it) and are JUST TRUE unless the defence of (6) (the director with whom a connected person is connected shows all reasonable steps) or (7) (a connected person or an authorising director shows he did not know the relevant circumstances) is shown, when JUST FALSE; any other person answers NOTHING (the list is not closed: (8) leaves other enactments and rules of law untouched). Other reading: JUST FALSE for any other person ("The persons so liable are").
- **F60** (s 195(2), "voidable at the instance of the company, unless (a), (b) or (c)"): Taken: voidable (JUST TRUE) where the company entered into the arrangement in contravention of s 190(1) and none of the three exceptions holds; JUST FALSE where one does (an "unless" met); NOTHING where there is no contravention or the arrangement was not entered into. Other reading: NOTHING where an exception holds.
- **F61** (s 196, "Where ... it is affirmed ... within a reasonable period"): Taken: JUST TRUE where the contravention of subsection (1) is affirmed by the members of the company, or of subsection (2) by the members of the holding company, within a reasonable period (a plain input); otherwise JUST FALSE (a "where" unmet: ruling (b) of 2026-11-05). Other reading: NOTHING.
- **F62** (s 189(a) and (b)): Taken: JUST TRUE where the company agreed to the provision and section 188(2) bars it (the contravention); NOTHING where there is no contravention or no agreement. Other reading: JUST FALSE.
- **F63** (ss 198(1), 200(1), 201(1), "This section applies to a company if it is (a) a public company, or (b) a company associated with a public company"): Taken: an explicit "applies ... if" is a condition: JUST TRUE for a public company or one associated with a public company (s 256, coa5: MAYBE BOOLEAN), JUST FALSE for a company that is neither (marginal reading (a)); the bar function takes the scope answer and gives JUST FALSE where it is JUST FALSE. Other reading: NOTHING (a scope limit with no "only", ruling (c) of 2026-11-05).
- **F64** (ss 197(1), 198(2), 200(2), 201(2), 203(1), each "may not ... unless ... approved by a resolution of the members of the company"): see F55. Taken for these sections: the other exceptions (ss 205 to 209, coa5's; s 204 this part's) are one BOOLEAN input, `an exception in section 204, 205, 206, 207, 208 or 209 disapplies the requirement of approval`, that the seat computes (from `s 204(1)`, `s 204(2)` and the coa5 answers); the subsection's own transaction (a loan, a quasi-loan, a credit transaction, a guarantee or security in connection with one, for a director, or for a person connected with one: s 252) is in the inputs, and a transaction outside it answers NOTHING. Other reading: JUST FALSE for a transaction outside the subsection.
- **F65** (ss 199(1) and 202(1), "A 'quasi-loan' is a transaction under which ..."; "A 'credit transaction' is a transaction under which ..."): Taken: closed definitions ("is a transaction under which"): JUST TRUE where the limbs are met, JUST FALSE otherwise (marginal reading (a)); "conditional sale agreement" is a borrowed definition (the Consumer Credit Act 1974: a MAYBE BOOLEAN input); "services" means anything other than goods or land (JUST FALSE for goods or land). Other reading: NOTHING for a transaction not within the limbs.
- **F66** (s 203(1) and (6)): Taken: the arrangement is barred (JUST TRUE) where the company takes part in an arrangement under which another person enters into a transaction that would have required approval under s 197, 198, 200 or 201 and obtains a benefit from the company or an associated body corporate, or arranges for the assignment or assumption of rights, obligations or liabilities under such a transaction, and the arrangement has not been approved; whether the transaction "would have required approval" is the answer of those sections' bar functions (MAYBE BOOLEAN inputs: a NOTHING gives NOTHING); (6) says the transaction is treated as entered into on the date of the arrangement (a function returning that date). Other reading: JUST FALSE where the arrangement is not within (a) or (b).
- **F67** (s 204(1) and (2), "Approval is not required under section 197, 198, 200 or 201 for anything done by a company (a) to provide a director ... with funds to meet expenditure ... (b) to enable any such person to avoid incurring such expenditure"; "This section does not authorise a company to enter into a transaction if the aggregate of the value of the transaction and of any other relevant transactions or arrangements exceeds £50,000"): Taken: (1) JUST FALSE ("approval is required": no) for the three listed things, NOTHING for anything else; (2) JUST FALSE ("section 204 authorises": no) where the aggregate exceeds 50,000 pounds (not at exactly 50,000), NOTHING otherwise; "relevant transactions or arrangements" are a plain number (the sum of their values); the seat combines the two, so that the exception applies when (1) says approval is not required and (2) does not say the section fails to authorise. Other reading: (2) overrides (1) without a separate function.
- **F68** (ss 197(4), 198(5), 200(5), 201(5), 203(4), "The matters to be disclosed are"): Taken: each of the three matters is required, so the function is JUST TRUE only if all are set out and JUST FALSE if any is missing; the memorandum-availability functions (ss 188(5), 197(3), 198(4), 200(4), 201(4), 203(3)) take "the memorandum has the required contents" as one BOOLEAN input. Other reading: NOTHING for a missing matter.
- **F69** (the 15 days of ss 188(5), 197(3), 198(4), 200(4), 201(4), 203(3), "at the company's registered office for not less than 15 days ending with the date of the meeting"): Taken: the days are counted inclusively from the first day of availability to the day of the meeting, so 15 days or more is a first day 14 days or more before the meeting day; and the memorandum must also be available at the meeting itself; for a written resolution it must be "sent or submitted to every eligible member at or before the time at which the proposed resolution is sent or submitted to him". Other reading: 15 clear days.
- **F70** (s 168(3), "A vacancy created by the removal of a director under this section, if not filled at the meeting at which he is removed, may be filled as a casual vacancy"): Taken: a grant ("may be filled") behind an "if not filled" gate, so when the vacancy was filled at the meeting the answer is NOTHING (the case falls outside the grant and the text does not say it may not be filled as a casual vacancy). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F71** (s 169(4), "If a copy of the representations is not sent as required by subsection (3) because received too late or because of the company's default, the director may ... require that the representations shall be read out at the meeting"): Taken: a grant ("may require") behind an "If" gate, so when the gate fails the answer is NOTHING (the text does not say the director may not otherwise require it). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).

### Listed by the name-test sweep of 2026-11-12, not flipped

Two groups the sweep does not settle, one row per function. Both are questions for the maintainer or a lawyer. The answer in force is the one in the third column; the other reading is in the fourth.

| function | the text and its gate | answer in force | the other reading |
| --- | --- | --- | --- |
| `s 175(5) authorisation has been given by the directors` | "(5) Authorisation may be given by the directors— (a) where the company is a private company and nothing in the company's constitution invalidates such authorisation, ...; or (b) where the company is a public company and its constitution includes provision enabling the directors to authorise the matter, ..." A "may" provision behind a "where" gate; the function is named for the fact that authorisation has been given, not for the power (F37) | JUST FALSE when the "where" gate fails (ruling (b) of the Guide's "Periods, where and scope limits" paragraph) | NOTHING (a grant limited by its own wording, Guide section 5 "In short") |
| `s 181(2)(b) authorisation has been given by the directors, for a charity` | "(5) Authorisation may be given by the directors where the company's constitution includes provision enabling them to authorise the matter, ..." A "may" provision behind a "where" gate; named for the fact of authorisation | JUST FALSE when the "where" gate fails | NOTHING |
| `s 196 the transaction or arrangement may no longer be avoided under section 195` | "Where a transaction or arrangement is entered into by a company in contravention of section 190 ... but, within a reasonable period, it is affirmed ..., it may no longer be avoided" A "where" gate; the "may" is a disability on the power to avoid, not a grant (F61) | JUST FALSE when it was not affirmed | NOTHING |
| `s 169(2) the director is entitled to be heard on the resolution at the meeting` | "(2) The director (whether or not a member of the company) is entitled to be heard on the resolution at the meeting." An entitlement (a claim), listed by its name; it has no JUST FALSE branch | JUST TRUE for a resolution to remove the director, NOTHING otherwise: nothing is at stake today | the Guide does not settle an "entitled" function that fails its gate |

## Jural relations (coa4)

Hohfeld relations in the Act's own words (the text seldom names the claim-holder; where it does not, the cell says so). Typing marked "assumed" is mine, not the text's.

| provision | whose claim, power, privilege or immunity | whose duty, liability, no-right or disability | relation | names |
| --- | --- | --- | --- | --- |
| s 154(1), (2) | not named in the text (s 156 gives the Secretary of State a power when the company is in breach) | the company (duty to have the directors) | claim / duty | `s 154(1)`, `s 154(2)` |
| s 155(1) | not named in the text (as s 154) | the company (duty) | claim / duty | `s 155(1)` |
| s 155(2) | none (a rule saying when the requirement is met) | none | none | `s 155(2)` |
| s 156(1) | the Secretary of State (power to give a direction) | the company (liability to be directed) | power / liability | `s 156(1)` |
| s 156(2), (3) | the company (claim that the direction has the content the section requires) | the Secretary of State (duty to specify and inform) | claim / duty | `s 156(2)` (both), `s 156(3)` |
| s 156(4), (5) | the Secretary of State (claim to compliance with the direction) | the company (duty to make the appointments and give notice before the end of the period) | claim / duty | `s 156(4)` (rule and function), `s 156(5)` |
| s 156(5A) | none (a saving of the s 167G duty) | none | none | `s 156(5A)` |
| s 156(6), (7) | not named in the text (the Crown prosecutes) | the company, and every officer in default (a shadow director treated as an officer): liability to conviction | power / liability | `s 156(6)(a)`, `s 156(6)(b)`, `s 156(7)` |
| s 156A(1), (2), (5) | the person who is not a natural person (immunity from appointment) | the company (disability: it cannot appoint) | immunity / disability (typing assumed, for a lawyer) | `s 156A(1)` |
| s 156A(3) | none (a rule of effect: the appointment is void) | none | none | `s 156A(3)` |
| s 156A(4) | none (a saving of liability) | none | none | `s 156A(4)` |
| s 156A(6), (7) | not named (the Crown) | the company, the body corporate or firm purportedly appointed, and every officer in default: liability to conviction | power / liability | `s 156A(6)(a)`-`(c)`, `s 156A(7)` |
| s 156B | the Secretary of State (power to make regulations) | companies and persons within the regulations (liability to be bound) | power / liability | none: machinery (inert, reason 2) |
| s 156C(1), (2) | none for (1); (2): the company (the person's office ends) | the person appointed: ceases to hold office (an effect) | none | `s 156C(1)`, `s 156C(2)` |
| s 156C(2A) | none (a saving) | none | none | `s 156C(2A)` |
| s 156C(3) | not named in the text | the registrar (duty to note) | claim / duty (holder not named) | `s 156C(3)` |
| s 157(1), (6) | the person under 16 years (immunity from appointment) | the company (disability: it cannot appoint) | immunity / disability (typing assumed, for a lawyer) | `s 157(1)` |
| s 157(2), (3) | none (rules of effect: the appointment is not affected; the other office does not yet make a director) | none | none | `s 157(2)`, `s 157(3)` |
| s 157(4), (5) | none (void; a saving of liability) | none | none | `s 157(4)`, `s 157(5)` |
| s 158(1), (2), (4), (5) | the Secretary of State (power to make regulations) | persons and companies within the regulations (liability) | power / liability | none: machinery (inert, reason 2) |
| s 158(3), (3A) | none (an effect: the person ceases to hold office; a saving of liability) | none | none | `s 158(3)`, `s 158(3A)` |
| s 159 | none (repealed or blank in the text) | none | none | - |
| s 159A(1), (3), (4) | the person who is disqualified (immunity from appointment) | the company (disability: it cannot appoint; (3): the appointment is void; (4): a saving of liability) | immunity / disability (typing assumed) | `s 159A(1)`, `s 159A(3)`, `s 159A(4)` |
| s 159A(2) | none (a definition by table) | none | none | `s 159A(2)` |
| s 160(1), (2) | the members at the meeting (claim that appointments are voted on individually): the holder is not named in the text | whoever moves the motion (duty not to move it): the bearer is not named in the text | claim / duty | `s 160(1)`, `s 160(2)` |
| s 160(3), (4) | none (a deeming rule; a disapplication) | none | none | `s 160(3)`, `s 160(1)` |
| s 161 | persons dealing with the company (immunity from the invalidity of the acts of a person acting as a director) | the company and its members (disability: they cannot challenge the acts on these grounds) | immunity / disability (typing assumed) | `s 161(1)` |
| s 161A to s 167F | none (repealed or blank in the text) | none | none | - |
| s 167G(1), (2), (3), (6) | the registrar (recipient of the notice; the text names no one who may enforce) | the company (duty to give notice of the change, with its date and contents, within 14 days) | claim / duty | `s 167G(1)` (rule and function), `s 167G(2)`, `s 167G(3)` (a)-(f), `s 167G(6)` |
| s 167G(4), (5) | none (a definition; an exception to the duty) | none | none | `s 167G(4)`, `s 167G(1)` |
| s 167H(1) to (4) | the registrar (recipient) | the company (duty to give notice of a change of information within 14 days, with its date and, for a service address change, the statement) | claim / duty | `s 167H(1)` (rule and function) to `s 167H(4)` |
| s 167I(1) to (5) | the registrar (recipient) | the company (duty to give notice of the matters before incorporation within 14 days of incorporation); (3) none: an exception | claim / duty | `s 167I(1)` to `s 167I(5)` |
| s 167J, s 167K | none (definitions of the required information; (5), (6), (2), (3): powers of the Secretary of State to amend by regulations, machinery) | none | none | `s 167J(1)` to `s 167J(4)`, `s 167K(1)` |
| s 167L | not named (the Crown prosecutes) | the company and every officer in default (a shadow director treated as an officer): liability to conviction | power / liability | `s 167L(1)(a)`, `s 167L(1)(b)`, `s 167L(3)` |
| s 167M(1), (2) | not named (the registrar and the public interest) | an individual acting as a director (duty not to act unverified); the company (duty to ensure it) | claim / duty | `s 167M(1)`, `s 167M(2)` |
| s 167M(3) to (5) | not named (the Crown) | the individual, the company and every officer in default: liability to conviction | power / liability | `s 167M(3)`, `s 167M(4)`, `s 167M(5)` |
| s 167M(6), s 167N(7) | the individual or person whose acts are in question (immunity: the acts remain valid) | those who might challenge the acts (disability) | immunity / disability (typing assumed) | `s 167M(6)`, `s 167N(7)` |
| s 167N(2) | not named (the registrar and the public interest) | the person who has become a director and has not been notified in time (duty not to act until notice is given) | claim / duty | `s 167N(2)` |
| s 167N(3), (4), (6) | not named (the Crown) | the person, and every officer of a firm in default: liability to conviction | power / liability | `s 167N(3)`, `s 167N(4)`, `s 167N(6)` |
| s 167N(5) | the person charged (immunity from conviction on proof of the belief) | the prosecution (disability to obtain a conviction) | immunity / disability (a defence; typing assumed) | `s 167N(5)` |
| s 168(1) | the company (power to remove the director by ordinary resolution at a meeting) | the director (liability to be removed, notwithstanding any agreement) | power / liability | `s 168(1)` |
| s 168(2) | the members (claim to special notice of the resolution; the holder is not named) | the company and those proposing the resolution (duty to give special notice) | claim / duty | `s 168(2)` |
| s 168(3), (4) | none (the vacancy may be filled; a deeming rule for retirement) | none | none | `s 168(3)`, `s 168(4)` |
| s 168(5) | the person removed (immunity: compensation or damages and other powers to remove are not affected) | the company (disability) | immunity / disability (typing assumed) | `s 168(5)(a)`, `s 168(5)(b)` |
| s 169(1) | the director concerned (claim to a copy of the notice) | the company (duty to send it forthwith) | claim / duty | `s 169(1)` (rule and function) |
| s 169(2) | the director (claim to be heard on the resolution at the meeting, member or not) | the company and the meeting (duty to hear him) | claim / duty | `s 169(2)` |
| s 169(3) | the director (claim to have his representations notified to the members) | the company (duty to state the fact and send a copy) | claim / duty | `s 169(3)` (rule and functions) |
| s 169(4) | the director (power to require the representations to be read out) | the company and the meeting (liability) | power / liability | `s 169(4)` |
| s 169(5) | the company and any person aggrieved (power to apply to the court; the court's satisfaction) | the director (liability to lose the rights in (3) and (4)) | power / liability | `s 169(5)` |
| s 169(6) | the court (power to order costs) | the director (liability to pay the company's costs) | power / liability | `s 169(6)` |
| s 169A | none (an effect: the person ceases to hold office; a saving; an inclusion) | none | none | `s 169A(1)`, `s 169A(2)`, `s 169A(3)` |
| s 170(1), (2), (5) | the company (claim that the director observe the general duties; for (2) also against a former director; for (5) against a shadow director) | the director (duty); the former director (continuing duty under ss 175, 176); the shadow director | claim / duty | `s 170(1)`, `s 170(2)`, `s 170(5)` |
| s 170(3), (4) | none (the duties replace the common law; a rule of interpretation) | none | none | `s 170(3)`, `s 170(4)` |
| s 171 to s 174 | the company (claim) | the director (duty to act within powers; to promote the success of the company; to exercise independent judgment; to exercise reasonable care, skill and diligence) | claim / duty | `s 171` to `s 174(1)` (functions and rules) |
| s 172(2), (3) | none (the object of the duty; a subjection to other law) | none | none | `s 172(2)`, `s 172(3)` |
| s 173(2) | the director (privilege to act under an agreement or as the constitution authorises) | the company (no-right to complain) | privilege / no-right | `s 173(2)` |
| s 175(1), (2) | the company (claim) | the director (duty to avoid conflicts of interest) | claim / duty | `s 175(1)`, `s 175(2)` |
| s 175(3), (4), (7) | the director (privilege: the duty does not apply or is not infringed) | the company (no-right) | privilege / no-right | `s 175(3)`, `s 175(4)` |
| s 175(5), (6) | the directors (power to authorise the matter) | the director with the conflict (liability to have the matter authorised or not) | power / liability | `s 175(5)`, `s 175(6)` |
| s 176(1) | the company (claim) | the director (duty not to accept benefits from third parties) | claim / duty | `s 176(1)` (rule and function) |
| s 176(2), (3), (5) | none (definitions) | none | none | `s 176(2)`, `s 176(3)`, `s 176(5)` |
| s 176(4) | the director (privilege) | the company (no-right) | privilege / no-right | `s 176(4)` |
| s 177(1), (3), (4) | the other directors (recipients) and the company (claim) | the director (duty to declare the nature and extent of the interest before the company enters into the transaction; to make a further declaration) | claim / duty | `s 177(1)` (rule and function), `s 177(3)`, `s 177(4)` |
| s 177(2), (5), (6) | the director (privilege to declare in these ways; not to declare an interest of which he is unaware, or those listed) | the other directors (no-right) | privilege / no-right | `s 177(2)`, `s 177(5)`, `s 177(6)` |
| s 178 | the company (claim to the consequences of breach as at common law; enforcement as a fiduciary duty, except s 174) | the director (liability) | claim / duty | `s 178(1)`, `s 178(2)` |
| s 179 | none (a rule of reading) | none | none | `s 179` |
| s 180(1) | the other party to the transaction or arrangement (immunity from its being set aside on that ground) | the company (disability) | immunity / disability (typing assumed) | `s 180(1)` |
| s 180(2), (3), (5) | none (rules of effect) | none | none | `s 180(2)`, `s 180(3)`, `s 180(5)` |
| s 180(4) | the directors (immunity from breach where authority is given or the articles are followed) | the company (disability) | immunity / disability (typing assumed) | `s 180(4)(a)`, `s 180(4)(b)` |
| s 181 | none (modifications for a charity; (4) blank; (5) extent) | none | none | `s 181(1)` to `s 181(5)` |
| s 182(1), (2), (3), (4) | the other directors (recipients) and the company (claim) | the director interested in a transaction already entered into (duty to declare its nature and extent, in the ways allowed, as soon as reasonably practicable; to make a further declaration) | claim / duty | `s 182(1)`, `s 182(2)`, `s 182(3)`, `s 182(4)` (rule and functions) |
| s 182(5), (6) | the director (privilege: no declaration of an interest he is unaware of, or listed in (6)) | the other directors (no-right) | privilege / no-right | `s 182(5)`, `s 182(6)` |
| s 183 | not named (the Crown) | the director who fails to comply with s 182 (liability to conviction) | power / liability | `s 183(1)`, `s 183(2)` |
| s 184(1) to (4) | the other directors (claim to receive the notice); the director (privilege to send it in these forms and by these means) | the director (duty to send it); the recipients (no-right as to form and means) | claim / duty; privilege / no-right | `s 184(2)`, `s 184(3)`, `s 184(4)` |
| s 184(5), s 186(1)(b), (c) | none (deeming rules) | none | none | `s 184(5)`, `s 186(1)(b)`, `s 186(1)(c)` |
| s 185 | the director (power to make a sufficient declaration by general notice) | the other directors and the company (liability to treat it as sufficient) | power / liability | `s 185(1)`, `s 185(2)`, `s 185(3)`, `s 185(4)` |
| s 186(1)(a), (2) | the company and the other directors (claim that a sole director's declaration be recorded in writing) | the sole director (duty); (2) none | claim / duty | `s 186(1)(a)`, `s 186(2)` |
| s 187 | none (the Chapter applies to a shadow director, with adaptations) | none | none | `s 187(1)` to `s 187(4)` |
| s 188(1), (2), (5), (6) | the members of the company (and of the holding company) (claim that a long-term provision is not agreed without their approval, on a memorandum made available to them) | the company (duty not to agree it without approval; to make the memorandum available); (6): none | claim / duty | `s 188(1)`, `s 188(2)`, `s 188(5)`, `s 188(6)` |
| s 188(3), (4), (7) | none (definitions and a rule of addition) | none | none | `s 188(3)`, `s 188(4)`, `s 188(7)` |
| s 189 | the company (power to terminate at any time on reasonable notice; the provision void) | the director (liability to termination on reasonable notice) | power / liability | `s 189(a)`, `s 189(b)` |
| s 190(1), (2) | the members of the company (and of the holding company) (claim to approve) | the company (duty not to enter into the arrangement without approval or a condition of approval) | claim / duty | `s 190(1)`, `s 190(2)` |
| s 190(3) | the company (immunity from liability for the failure to obtain approval) | whoever might claim against it (disability) | immunity / disability (typing assumed) | `s 190(3)` |
| s 190(4), (5), (6), s 191 | none (exceptions and definitions: (4) and (6): the company's privilege not to seek approval, with the members' no-right) | none | none (privilege / no-right for the exceptions) | `s 190(4)` to `s 190(6)`, `s 191(2)` to `s 191(5)` |
| s 192, s 193, s 194 | the company (privilege: approval is not required) | the members (no-right) | privilege / no-right | `s 192`, `s 193(2)`, `s 194(1)` |
| s 195(2) | the company (power to avoid the arrangement and any transaction in pursuance) | the other parties (liability to the avoidance), except where (a), (b) or (c) | power / liability | `s 195(2)` |
| s 195(3), (4) | the company (claim to an account of any gain and an indemnity, jointly and severally) | the directors and connected persons listed in (4) (duty) | claim / duty | `s 195(3)`, `s 195(3)(b)` |
| s 195(6), (7) | the director or person who shows the matter (immunity from liability) | the company (disability) | immunity / disability (typing assumed) | `s 195(3)` (the defences) |
| s 195(8) | none (a saving of other law) | none | none | `s 195(8)` |
| s 196 | the parties to the transaction (immunity from avoidance after affirmation) | the company (disability: it can no longer avoid) | immunity / disability (typing assumed) | `s 196` |
| s 197 to s 198 | the members of the company (and of the holding company) (claim that a loan, quasi-loan, guarantee or security for a director is not made without their approval, on a memorandum made available to them) | the company (duty not to make it without approval; to make the memorandum available) | claim / duty | `s 197(1)` to `s 197(5)`, `s 198(1)` to `s 198(6)` |
| s 199, s 202 | none (definitions) | none | none | `s 199(1)` to `s 199(3)`, `s 202(1)` to `s 202(3)` |
| s 200, s 201 | the members of the company (and of the holding company) (claim: as ss 197, 198, for a loan or quasi-loan to a connected person, or a credit transaction for a director or connected person) | the company (duty as above) | claim / duty | `s 200(1)` to `s 200(6)`, `s 201(1)` to `s 201(6)` |
| s 203 | the members of the company (and of the holding company) (claim that no related arrangement is entered into without their approval) | the company (duty) | claim / duty | `s 203(1)` to `s 203(6)` |
| s 204 | the company (privilege: approval is not required for expenditure on company business up to 50,000 pounds in aggregate) | the members (no-right) | privilege / no-right | `s 204(1)`, `s 204(2)` |

## Marginal readings for a lawyer (coa4)

Each row is a branch where the answer rests on a reading, not on the text in its own words: (a) a failed "if", "unless" or bare "must" counted as the text's no, or (b) a wording-limited grant counted as not the text's no. A lawyer who disagrees with a row flips that branch from JUST FALSE to NOTHING (or the reverse); no other rule moves.

| function | branch | rests on | the other reading |
| --- | --- | --- | --- |
| `s 154(1)`, `s 154(2)`, `s 155(1)`, `s 156(2)` (both), `s 156(3)`, `s 156(4)`, `s 156(5)` | JUST FALSE for the unmet requirement (when the condition of the subsection holds) | a bare "must" not done counted as the text's no (fork F1) | NOTHING |
| `s 155(2)` | JUST FALSE when the office is not so held | (a): "This requirement is met if ..." | NOTHING ("if" does not say "only if") |
| `s 156(1)` | NOTHING when it does not appear to the Secretary of State | (b): a grant ("may give") behind an "If it appears" gate; Guide section 5 "In short" (F4) | JUST FALSE (a failed "if" read as the text's own no) |
| `s 156(6)(a)`, `s 156A(6)(a)`, `s 156A(6)(b)`, `s 156A(6)(c)` | JUST FALSE when the company did not fail or the appointment did not contravene | (a): "If a company fails ... an offence is committed by" | NOTHING |
| `s 156(6)(b)`, `s 156A(6)(c)` | NOTHING for an officer not in default, and for a person who is not an officer | (b): a prohibition limited by its own wording | JUST FALSE |
| `s 156A(1)` | JUST FALSE for a natural person and for the office held as a corporation sole | (a): "unless" and the flat negative in (2) | NOTHING |
| `s 156C(2)` | JUST FALSE when (a) or (b) of the "where" fails, and before the relevant day | the 2026-11-05 rulings (a) and (b) | NOTHING |
| `s 156C(3)` | JUST FALSE when the registrar has no such appearance | (a): "If it appears to the registrar" | NOTHING |
| `s 158(3)` | JUST FALSE when the appointment or the ceasing of the circumstances is not shown, and for a person who has since attained 16 | (a): "If the specified circumstances cease to obtain ..." and a class limited by "who has not since attained" (fork F13) | NOTHING |
| `s 159A(2)`, `s 159A(1)` | JUST FALSE when no row holds, and when the person is not disqualified | (a): "a person (P) is disqualified ... if:" and "if the person is disqualified" (forks F14, F15) | NOTHING |
| `s 160(1)` | JUST FALSE for a resolution amending the articles | flat negative counted as the text's no (N2 ruling): "Nothing in this section applies" | NOTHING |
| `s 160(1)`, `s 161(1)`, `s 160(3)`, `s 157(2)` | NOTHING outside the limit each states (a public company and two or more persons; the listed defects; the listed motions; an appointment not taking effect until 16) | (b): a rule limited by its own wording (forks F16, F17, F18) | JUST FALSE outside the limit |
| `s 157(3)` | JUST FALSE where the office is not held by a corporation sole or by virtue of another office | the 2026-11-05 ruling (b) on "where" (fork F12) | NOTHING |
| `s 167G(1)`, `s 167H(1)`, `s 167I(1)`, `s 167I(2)` | JUST FALSE when the event or the condition did not occur | (a): "A company must give notice ... if ..." | NOTHING |
| `s 167G(2)`, `s 167G(3)(a)`, `(b)`, `(d)`, `s 167G(3)`, `s 167G(6)`, `s 167H(2)`, `s 167H(3)`, `s 167I(4)`, `s 167I(5)` | JUST FALSE for the unmet requirement or a day outside the period | a bare "must" not done (F1) and a period the text fixes (ruling (a) of 2026-11-05) | NOTHING |
| `s 167G(3)(c)`, `(e)`, `(f)`, `s 167H(4)` | NOTHING where the paragraph's own "if" or "where" is unmet | F5 | JUST FALSE |
| `s 167G(4)`, `s 167J(1)`, `s 167J(2)`, `s 167J(3)`, `s 167K(1)` | JUST FALSE where a definition's limb fails | definitions by "means" or "is" read as closed (F2-style; marginal reading (a)) | NOTHING |
| `s 167I(3)` | JUST FALSE where notice is given under (1) | a flat negative counted as the text's no (N2 ruling) | NOTHING |
| `s 167L(1)(a)`, `s 167M(3)`, `s 167M(4)(a)`, `s 167N(3)` | JUST FALSE when the failure or contravention did not occur | (a): "If a company fails ... an offence is committed by", "A person who contravenes ... commits an offence" | NOTHING |
| `s 167L(1)(b)`, `s 167M(4)(b)`, `s 167N(4)` | NOTHING for an officer not in default and for a person who is not an officer | (b): a prohibition limited by its own wording | JUST FALSE |
| `s 167M(1)`, `s 167M(2)`, `s 167N(2)` | JUST FALSE where the person does not act, where the identity is verified, or where notice has been given | flat negatives and "unless" / "until" (rulings (d) of 2026-11-05) | NOTHING |
| `s 167N(5)` | JUST FALSE where the belief is not proved | the 2026-11-05 ruling (b) on defences | NOTHING |
| `s 167M(6)`, `s 167N(7)` | JUST FALSE for any consequence other than the offence | a list closed with "only" (not marginal: stated for completeness) | - |
| `s 167J(4)` | NOTHING outside the limit | (b): a grant limited by its own wording | JUST FALSE |
| `s 168(3)` | NOTHING where the vacancy was filled at the meeting | (b): a grant ("may be filled") behind an "if not filled" gate; Guide section 5 "In short" (F70) | JUST FALSE (a failed "if" read as the text's own no) |
| `s 169(4)` | NOTHING where a copy was sent as required, or was not sent for another reason | (b): a grant ("may require") behind an "If a copy ... is not sent" gate (F71) | JUST FALSE (a failed "if" read as the text's own no) |
| `s 169(5)` | JUST FALSE where the court is not satisfied | (a): "need not be sent ... if ... the court is satisfied" (F31) | NOTHING |
| `s 169(3)` | JUST FALSE for a late receipt and where a limb is missing | (a): "unless the representations are received by it too late" (F30) | NOTHING |
| `s 169(1)`, `s 169(3)(a)`, `(b)` | JUST FALSE when the duty arises and is not met; NOTHING where it does not arise | a bare "must" not done (F1); F5 | NOTHING; JUST FALSE |
| `s 168(1)`, `s 168(2)`, `s 169A(3)`, `s 169(2)`, `s 169(6)` | NOTHING outside the limit each states | (b): a grant limited by its own wording, and "includes" (F28, F32) | JUST FALSE outside the limit |
| `s 168(5)(a)`, `s 168(5)(b)` | JUST FALSE where compensation is payable or the power exists | a flat negative counted as the text's no (N2 ruling) | NOTHING |
| `s 169A(1)` | JUST FALSE where the person has not become disqualified or was not appointed | (a): "if the person becomes disqualified" | NOTHING |
| `s 171`, `s 172(1)`, `s 173(1)`, `s 174(1)`, `s 175(1)`, `s 176(1)`, `s 177(4)`, `s 177(3)` | JUST FALSE for the unmet duty | a bare "must" or "must not" not done (F1; F37) | NOTHING |
| `s 177(5)`, `s 177(1)`, `s 175(3)` | JUST FALSE for "does not require a declaration" and "does not apply" | flat negatives counted as the text's no (N2 ruling) | NOTHING |
| `s 177(6)` | JUST FALSE where none of the limbs holds | (a): "A director need not declare an interest (a) if ..." | NOTHING |
| `s 175(5)`, `s 181(2)(b)` | JUST FALSE where the "where" or the constitution provision is not met | the 2026-11-05 ruling (b) on "where" | NOTHING |
| `s 178(2)` | JUST FALSE for s 174 | the "except" site of the 2026-11-05 case-by-case ruling (F43) | NOTHING |
| `s 180(2)` | JUST FALSE where the "except" is met; NOTHING outside Chapters 4 and 4A | F40 | NOTHING; JUST FALSE |
| `s 181(2)(a)`, `s 181(3)` | JUST TRUE (the duty applies) / JUST FALSE where the articles do not allow | "which they may do only in relation to" (a closed permission; F41) | NOTHING |
| `s 170(2)`, `s 170(1)`, `s 170(3)`, `s 170(4)`, `s 173(2)`, `s 175(4)`, `s 176(4)`, `s 179`, `s 180(1)`, `s 180(4)`, `s 180(5)` | NOTHING outside the limit each states | (b): a rule limited by its own wording | JUST FALSE outside the limit |
| `s 170(5)` | JUST FALSE where the duty is not capable of applying to a shadow director | the 2026-11-05 ruling (b) on "where" | NOTHING |
| `s 182(1)`, `s 182(5)`, `s 182(6)`, `s 182(3)`, `s 182(4)`, `s 184(2)`, `s 185(3)`, `s 186(1)(a)` | JUST FALSE for the unmet requirement or the unmet "if" | a bare "must" not done (F1), (a): "Where ... interested", "If a declaration ... proves to be inaccurate" | NOTHING |
| `s 182(2)`, `s 184(3)`, `s 184(4)` | JUST FALSE for a way or form the text does not list or does not allow | "must be made" as a closed list (F44); an "if" unmet (F45) | NOTHING |
| `s 182(4)` (second sentence), `s 186(2)`, `s 187(2)`, `s 187(3)` | JUST FALSE | flat negatives counted as the text's no (N2 ruling) | NOTHING |
| `s 183(1)` | JUST FALSE where the director complied | (a): a relative clause "who fails to comply" | NOTHING |
| `s 185(2)`, `s 185(4)`, `s 187(4)` | JUST FALSE where neither limb holds, and for the "unless" met | (a) and the ruling on "unless" bars | NOTHING |
| `s 184(1)`, `s 184(5)`, `s 186(1)(b)`, `(c)`, `s 187(1)` | NOTHING outside the limit each states | (b): limited by its own wording | JUST FALSE |
| `s 188(2)`, `s 190(1)`, `s 190(2)` | JUST FALSE where the "unless" approval condition is met, and for an unmet "If" | (a): "unless it has been approved", "If the director ..." (F55) | NOTHING |
| `s 188(4)`, `s 193(1)` | JUST FALSE for "If more than six months" unmet, for the parenthetical met, and for a members' voluntary winding up | (a): "If ..."; the "(other than X)" and "unless" sites (F54, F58) | NOTHING |
| `s 188(5)`, `s 188(7)`, `s 191(2)`, `s 191(5)`, `s 194(2)`, `s 195(2)`, `s 196` | JUST FALSE where a "means" or "if" or "must not ... unless" limb fails | (a) and the 2026-11-05 ruling (b) (F57, F60, F61) | NOTHING |
| `s 188(6)`, `s 190(4)`, `s 190(6)`, `s 192`, `s 193(2)`, `s 194(1)` | JUST FALSE where the exception's wording is met, NOTHING otherwise | a flat negative ("No approval is required", "Approval is not required") counted as the text's no; (b) for the rest | NOTHING; JUST FALSE |
| `s 188(1)`, `s 188(2)` | NOTHING outside the section's own wording (a provision not longer than two years; an arrangement not within the subsection) | (b) and ruling (c) of 2026-11-05 | JUST FALSE |
| `s 190(3)`, `s 195(8)` | JUST FALSE | flat negatives counted as the text's no (N2 ruling) | NOTHING |
| `s 195(3)` | JUST FALSE where the (6) or (7) defence is shown; NOTHING for any other person | defences "if he shows"; a list not closed (F59) | NOTHING; JUST FALSE |
| `s 197(1)`, `s 197(2)`, `s 198(2)`, `s 198(3)`, `s 200(2)`, `s 200(3)`, `s 201(2)`, `s 201(3)`, `s 203(1)`, `s 203(2)` | JUST FALSE where the approval condition is met, an exception applies, or an "If" is unmet | (a): "unless the transaction has been approved", "If the director is a director of the company's holding company" (F55, F64) | NOTHING |
| `s 198(1)`, `s 200(1)`, `s 201(1)` | JUST FALSE where the company is neither public nor associated with a public company | (a): "applies to a company if it is" (F63) | NOTHING |
| `s 197(3)`, `s 198(4)`, `s 200(4)`, `s 201(4)`, `s 203(3)`, `s 197(4)`, `s 198(5)`, `s 200(5)`, `s 201(5)`, `s 203(4)` | JUST FALSE where the memorandum or a matter is missing | "must not be passed unless ...", "The matters to be disclosed are" (F68) | NOTHING |
| `s 199(1)`, `s 199(2)`, `s 202(1)`, `s 202(2)`, `s 202(3)` | JUST FALSE where a definition's limb fails | definitions read as closed (F65) | NOTHING |
| `s 204(1)`, `s 204(2)`, `s 192`, `s 193(2)`, `s 194(1)` | JUST FALSE where the exception's wording is met | a flat negative ("Approval is not required", "does not authorise") counted as the text's no | NOTHING |
| `s 197(1)`, `s 198(2)`, `s 200(2)`, `s 201(2)`, `s 203(1)`, `s 199(3)` | NOTHING for a transaction outside the subsection's wording; "include" | (b) and "include" (F64, F66) | JUST FALSE |

### Name-test sweep of 2026-11-12

Scope: every top-level layer-1 name containing "may", "permitted", "power", "entitled" or "authorised/authorized" (including "powers", "authorises", "authorisation"): 18 names, found by scanning every layer-1 module. Sixteen are functions; one is a type (`s 195(4) person who may be liable`) and one a regulative rule (`s 171 the director's duty to act within powers`), neither of which answers JUST FALSE.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 3 | 5 | 3 | 1 |

- Flipped to NOTHING (a grant behind an "If" gate that answered JUST FALSE; each has one fork line and a marginal-readings row naming the other reading): `s 156(1) the Secretary of State may give the company a direction under section 156` (F4), `s 168(3) the vacancy may be filled as a casual vacancy` (F70), `s 169(4) the director may require that the representations be read out at the meeting` (F71).
- Kept JUST FALSE: `s 171 the director has complied with the duty to act within powers` (a duty), `s 175(6) the authorisation is effective` ("effective only if": the text closes the gate), `s 195(8) section 195 excludes the operation of any other enactment or rule of law ...` (a flat negative), `s 168(5)(b) section 168 derogates from the power to remove the director that exists apart from the section` (a flat negative), `s 204(2) section 204 authorises the company to enter into the transaction` (a flat negative: "This section does not authorise a company to enter into a transaction if ...").
- Listed, "may" with "where": `s 175(5) authorisation has been given by the directors`, `s 181(2)(b) authorisation has been given by the directors, for a charity`, `s 196 the transaction or arrangement may no longer be avoided under section 195`.
- Listed, "entitled": `s 169(2) the director is entitled to be heard on the resolution at the meeting`.
- Read and unchanged because they have no JUST FALSE branch (so nothing is decided): `s 168(1)` (a written resolution or another resolution is already NOTHING), `s 169(6)` (already NOTHING outside an application under (5)), `s 179`, `s 189(b)` ("entitling", not "entitled"; JUST TRUE or NOTHING).

### Reading a result: FALSE and NOTHING (coa4)

A function answers `JUST TRUE`, `JUST FALSE` or `NOTHING`. What each means depends on the kind of function, and a caller must never turn NOTHING into FALSE.
- **Requirement and compliance functions** (`s 154(1)`, `s 156(4)`, `s 167G(3)`, `s 171` to `s 177`, `s 182`): JUST TRUE = the requirement is met; JUST FALSE = it is not met (the text says "must" and it was not done); NOTHING = the subsection's own condition does not hold (for example the company is not in breach, so a direction question does not arise) or an answer from another part is not known.
- **Bar functions** (`s 188(2)`, `s 190(1)`, `s 190(2)`, `s 197(1)`, `s 198(2)`, `s 200(2)`, `s 201(2)`, `s 203(1)`, `s 156A(1)`, `s 157(1)`, `s 159A(1)`, `s 160(1)`): JUST TRUE = the section bars the company (or the appointment, or the motion); JUST FALSE = it does not, because the approval was given, was made a condition, is excused, or the section does not apply to this company; NOTHING = the case is outside the subsection's own wording (for example the borrower is not a director) or a borrowed answer (connected with a director, `s 256` associated) is not known.
- **Effect and offence functions** (`s 156A(3)`, `s 157(4)`, `s 161(1)`, `s 189`, `s 195(2)`, `s 195(3)`, `s 156(6)(b)`, `s 167L(1)(b)`, `s 167M(3)`, `s 167N(3)`): JUST TRUE = the effect follows or the offence is committed; JUST FALSE = the text says no (the company did not fail, the defence is shown); NOTHING = the text does not say (an officer who is not in default is outside the offence as the text words it).
- **Exception functions** (`s 192`, `s 193(2)`, `s 194(1)`, `s 204(1)`): JUST FALSE = approval is not required (the text says so); NOTHING = the exception does not apply, which does not mean approval is required: the section says only when it is not.
- **Amounts and days**: a function that returns a day returns a `DATE` (`s 167G(6)`, `s 188(3)` returns `MAYBE DATE`, NOTHING when a period counts in working days); a function that returns pounds returns `MAYBE NUMBER`, NOTHING where the text states no limit for the mode of conviction asked about.
- **Regulative rules** (`PARTY ... MUST/SHANT`) are tested with `#TRACE` (a DEONTIC value cannot be compared in an `#ASSERT`): FULFILLED, BREACH, or the residual obligation.
- **In the seat**: the same, with plain yes/no inputs; the answer NOTHING in a seat case is printed in the cases file as a "NOT COVERED" comment beside the expected value.

The loudest silent failure in this part was mine, not the text's: `NOT (x) OR y` is read as `NOT ((x) OR y)` on 1.6.110 (see "What the stable binary does not accept"), which made the `s 188(6)` and `s 190(4)` functions answer NOTHING for a wholly-owned subsidiary, where the text says no approval is required, and gave the same wrong answer in the holding-company limb of `s 188(2)`. Six assertions caught it; it was fixed by bracketing each NOT, and a scan of every template for a NOT followed by AND or OR now finds only a line that is already bracketed (`s 182(2)`).

## Seams (coa4)

Each seam input as PLAN.md section 4 names it; "answered by" says which part or the keel computes it. Seams the plan lacks, which I found by reading the text: the exceptions of ss 205 to 209 (the input `an exception in section 204, 205, 206, 207, 208 or 209 disapplies the requirement of approval`, found from s 204(1)'s own wording and the heading of s 205 at line 2697, not in the plan's list), and `s 191`'s statutory accounts (a plain record of the day the time for sending them out falls and the net assets, because Part 15 and s 424 are other parts').

| function | seam input (as PLAN.md section 4 names it) | type | answered by |
| --- | --- | --- | --- |
| `s 154(1)` | `s 4(1) the company is a private company` | BOOLEAN | keel (coa-definitions.l4: `s 4(1)`; "BOOLEAN suffices") |
| `s 154(2)` | `s 4(2) the company is a public company` | BOOLEAN | keel (`s 4(2)`) |
| `s 156(4)` | notice "under section 167G" is a fact (the notice was given before the end of the period); my own module coa4-notification answers what the notice is | BOOLEAN | this part (s 167G) |
| `s 156(6)(b)`, `s 156A(6)(c)` | `s 1173(1) the holder of the position is an officer of the body corporate` | MAYBE BOOLEAN | keel |
| `s 156(6)(b)`, `s 156A(6)(c)` | `s 251 the person is a shadow director` | MAYBE BOOLEAN | coa5 |
| `s 156(6)(b)`, `s 156A(6)(c)` | `s 1121 the officer is in default` | MAYBE BOOLEAN | coa24 |
| `s 156A(3)` | `the answer under section 156A(1)` | MAYBE BOOLEAN | this part (my own `s 156A(1)`) |
| `s 157(1)`, `s 157(2)`, `s 157(3)`, `s 158(3)` | the person's date of birth (core `Individual`, a fact the person states) | `Individual` | the seat |
| `s 157(4)`, `s 159A(3)`, `s 160(2)` | `the answer under section 157(1)` and its siblings (this part's own bar function) | MAYBE BOOLEAN | this part |
| `s 159A(1)` | `s 159A(2) the person is disqualified under the directors disqualification legislation` | MAYBE BOOLEAN | this part (own function); other parts take the same name |
| `s 159A(2)` | the facts of each row (for example s 1184, "P is disqualified as mentioned in section 1184(2)(a) or (b)"): plain BOOLEAN inputs | BOOLEAN | the person; s 1184 is coa25's (the seam found by reading the table: PLAN.md lists `s 1184 [coa25]` for s 159A) |
| `s 160(1)` | `s 4(2) the company is a public company` | BOOLEAN | keel |
| `s 167G(1)` | whether the person is "named as a proposed director in the statement under section 12" | BOOLEAN (a fact the company can state) | coa1 (s 12) |
| `s 167G(3)` | the statements in the notice, and `s 1110A` is a statement the notice must make (a fact about the notice, not the s 1110A answer) | BOOLEAN | the person |
| `s 167G(4)` | "a provision mentioned in column 2 of the table in section 159A(2)" | BOOLEAN | this part (s 159A(2)) |
| `s 167I(1)`, `s 167I(2)` | being named in the statement under s 12; the application "delivered ... under section 9" | BOOLEAN | coa1 (s 12, s 9) |
| `s 167J(2)` | "the registrar is required to refrain ... by virtue of regulations under section 1088(1)(a) or (b)" | BOOLEAN | coa23 (s 1088) |
| `s 167K(1)` | `s 3(1) the company is a limited company`, `s 1158 the company is a UK-registered company` | BOOLEAN | keel |
| `s 167L(1)(b)`, `s 167M(4)(b)`, `s 167N(4)` | `s 1173(1)` officer, `s 251` shadow director (not `s 167N(4)`), `s 1121` in default | MAYBE BOOLEAN | keel, coa5, coa24 |
| `s 167M(1)`, `s 167M(2)` | `s 1110A the individual's identity is verified` | MAYBE BOOLEAN | coa24 |
| `s 167M(3)`, `s 167M(4)(a)`, `s 167M(4)(b)`, `s 167N(3)` | `the answer under section 167M(1)`, `167M(2)`, `167N(2)` (this part's own functions) | MAYBE BOOLEAN | this part |
| `s 168(1)` | `s 282 the resolution is an ordinary resolution` | MAYBE BOOLEAN | coa7 |
| `s 168(1)` | the way the resolution is passed: the core `Way a resolution is passed` (`s 288 the resolution is a written resolution` is its written case) | core type | the seat |
| `s 169A(1)` | `s 159A(2) the person becomes disqualified under the directors disqualification legislation` | MAYBE BOOLEAN | this part (`s 159A(2)` in coa4-appointment.l4) |
| `s 170(5)` | `s 251 the person is a shadow director` | MAYBE BOOLEAN | coa5 |
| `s 175(5)` | `s 4(2) the company is a public company` | BOOLEAN | keel |
| `s 177(2)` | `s 184 the notice in writing is in accordance with section 184`, `s 185 the general notice is in accordance with section 185` | MAYBE BOOLEAN | this part (coa4-declaration.l4) |
| `s 177(1)` | `the answer under section 177(5)` and `177(6)` (this part's own functions) | MAYBE BOOLEAN | this part |
| `s 180(2)` | whether the case falls within Chapter 4 or Chapter 4A: Chapter 4 is this part's; Chapter 4A is coa5's (ss 226A to 226F, not in PLAN.md's seam list for coa4; found by reading s 180(2) and (3)) | BOOLEAN | the person (the facts), coa5 |
| `s 181(1)` | whether the company "is a charity" (the text does not define it in these ranges) | BOOLEAN | the person (a borrowed term asked as a fact) |
| `s 182(1)` | `the interest has been declared under section 177` (a fact; this part's `s 177(1)` and `s 177(4)` give it) | BOOLEAN | this part |
| `s 182(2)`, `s 177(2)` | `s 184 the notice in writing is in accordance with section 184`, `s 185 the general notice is in accordance with section 185` | MAYBE BOOLEAN | this part (own functions in coa4-declaration.l4) |
| `s 183(1)` | `the answer under section 182` (the compliance function) | MAYBE BOOLEAN | this part |
| `s 185(2)` | `s 252 the specified person is connected with the director` | MAYBE BOOLEAN | coa5 (ss 252 to 254), as PLAN.md's seam table says for coa4 and coa5 |
| `s 184(5)`, `s 186(1)(c)` | "the provisions of section 248 apply" (the effect of s 248 on minutes of meetings is coa5's: PLAN.md's seam `s 184: s 248 [coa5]`); no input is needed: the encoding says the provisions apply | - | coa5 |
| `s 186(2)` | section 231 (coa5): no input; a flat negative | - | coa5 |
| `s 187(1)` to `(3)` | `s 251 the person is a shadow director` | MAYBE BOOLEAN | coa5 |
| `s 186(1)` | the company "is required to have more than one director" (a fact; s 154(2) makes a public company one) | BOOLEAN | this part |
| `s 188(6)`, `s 190(4)` | `s 1158 the body corporate is a UK-registered company`, `s 1159(2) the body corporate is a wholly-owned subsidiary of another body corporate` | BOOLEAN | keel |
| `s 188(5)`, `s 190(1)` | the company's registered office (s 86, coa2): a fact (the memorandum is available for inspection there) | BOOLEAN / DATE | the person |
| `s 190(1)` | `s 252 the other party is connected with a director of the company or of its holding company` | MAYBE BOOLEAN | coa5 |
| `s 190(1)` | `s 191 the non-cash asset is a substantial non-cash asset` | MAYBE BOOLEAN | this part (`s 191(2)`); the non-cash asset itself is the keel's `s 1163(1)` (BOOLEAN suffices: a fact about the asset the caller states) |
| `s 191(4)` | the time for sending out accounts to members (s 424, coa9) and statutory accounts "prepared in accordance with Part 15" (coa8): the day and the net assets are plain facts | DATE / NUMBER | the person |
| `s 190(6)` | payment for loss of office "as defined in section 215" (coa5) | BOOLEAN | coa5 |
| `s 194(2)` | "recognised investment exchange" in Part 18 of the Financial Services and Markets Act 2000: a borrowed definition | MAYBE BOOLEAN | outside the sources |
| `s 188(1)`, `s 190(1)` | "holding company" and "subsidiary" (s 1159, keel): the facts are stated as BOOLEANs (the director of a holding company; the group) | BOOLEAN | keel |
| `s 189`, `s 195(2)` | `the answer under section 188(2)`, `the answer under section 190(1)` (this part's own bar functions) | MAYBE BOOLEAN | this part |
| `s 197(1)` to `s 203(1)` | `an exception in section 204, 205, 206, 207, 208 or 209 disapplies the requirement of approval`: s 204 is this part's (`s 204(1)`, `s 204(2)`); ss 205 to 209 are coa5's (found by reading s 204(1)'s own cross-reference and the heading of s 205 at line 2697) | BOOLEAN | this part and coa5 |
| `s 198(1)`, `s 200(1)`, `s 201(1)` | `s 256 the company is associated with a public company` | MAYBE BOOLEAN | coa5 (s 256) |
| `s 200(2)`, `s 200(3)`, `s 201(2)` | `s 252 ...` connected with a director | MAYBE BOOLEAN | coa5 (ss 252 to 254) |
| `s 201(2)` | `s 202(1) the transaction is a credit transaction` | MAYBE BOOLEAN | this part |
| `s 203(1)` | whether a transaction "would have required approval under section 197, 198, 200 or 201": the answers of those bar functions | MAYBE BOOLEAN | this part |
| `s 197(5)`, `s 198(6)`, `s 200(6)`, `s 201(6)`, `s 203(5)` | `s 1158` and `s 1159(2)` for the company and for the holding company | BOOLEAN | keel |
| `s 202(3)` | "conditional sale agreement" in the Consumer Credit Act 1974 | MAYBE BOOLEAN | outside the sources |

## What the text turns out to say

1. **Two wordings of one penalty are run together in the text file.** `s 156(7)` (src:2052) reads "...a daily default fine not exceeding one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale." with no space: two versions of one provision. The encoding gives both (two functions) and the seat asks which is in force (fork F2). The sources do not say which applies.
2. **England and Wales has no stated limit.** `s 156A(7)` (lines 2069 and 2070), `s 167L(3)` (2255, 2256), `s 167M(5)` (2267, 2268) and `s 167N(6)` (2279, 2280) each say (a) "in England and Wales, to a fine" and (b) "in Scotland or Northern Ireland, to a fine not exceeding level 5 on the standard scale"; ss 167L, 167M and 167N add "and, for continued contravention, a daily default fine not exceeding one-tenth of level 5 on the standard scale" to (b), and s 156A(7) does not. The first is encoded as `a fine without a stated limit`; the second as a level on the standard scale. The pounds a level stands for are not in the Act, so the seat asks for them.
3. **Section 197 has no scope sentence; ss 198, 200 and 201 do.** s 197(1) ("A company may not make a loan to a director ...") applies to every company; s 198(1), s 200(1) and s 201(1) each begin "This section applies to a company if it is (a) a public company, or (b) a company associated with a public company" (lines 2588, 2615, 2636). So a company that is neither public nor associated with a public company is barred by s 197 from lending to a director without approval, and by none of ss 198, 200 and 201 from a quasi-loan, a loan to a connected person or a credit transaction. The seat questions for ss 198, 200 and 201 therefore ask the two scope questions.
4. **One sentence is repeated seven times.** "No approval is required under this section on the part of the members of a body corporate that (a) is not a UK-registered company, or (b) is a wholly-owned subsidiary of another body corporate" occurs at lines 2488, 2505, 2585, 2606, 2633, 2654 and 2683 (ss 188(6), 190(4), 197(5), 198(6), 200(6), 201(6), 203(5)). It is one macro in the build and seven functions, each tested at four fact patterns.
5. **Sections 189 and 192 have no subsection numbers.** The sections run (a), (b) straight from the opening words (lines 2492 to 2495 and 2525 to 2530), so their rows carry the section label alone and their source locators span the whole section.
6. **The range ends inside s 204.** Subsections (1) and (2) are in the range; s 205 (exception for expenditure on defending proceedings) begins at line 2697 and is coa5's, as are ss 206 to 209. The five bar functions of ss 197 to 203 take the effect of all of ss 204 to 209 as one yes/no input, and the seat asks it as one question ("does an exception apply").
7. **A paragraph the text leaves open: "most recent" with equal dates.** `s 191(4)` defines the most recent statutory accounts as those whose time for sending out to members (s 424) is most recent; if two sets of accounts share that day the text does not choose. The function keeps the earlier in the list; no test depends on it.
8. **s 188(3) has no case for a contract with neither a fixed term nor a notice period.** The "aggregate of those periods" of nothing is taken as nil (fork F52), so such a contract has no guaranteed term longer than two years and the section does not apply.
9. **The seat case I wrote wrongly, and the rule that corrected me.** My first seat case for `s 176` (a benefit from the company itself) expected JUST TRUE; the layer-1 function answered NOTHING, and so does the text: s 176(1) speaks only of a benefit from a third party, so a benefit from the company is outside the duty and the text says neither that the duty was met nor that it was breached (the wording-limited NOTHING of the 2026-10-29 rule). The expected value in `coa4-cases-seat.l4` was corrected by that reading of the text, and the comment beside it says why; it was not changed to match output without a reason.
10. **Where my own work was wrong during the run.** Seven assertions were red at one point in the last stretch of work: the six `NOT (x) OR y` assertions (my code: see the next section) and the seat case of finding 9 (my expectation). None was a disagreement with the text that survived reading it; no assertion in this folder is meant to fail.

## What the stable binary does not accept (1.6.110; the same modules read the same on 1.6.109)

Sorted by how the failure shows. **Loud** (the binary errors, you will find it):
- A constructor pattern with named fields, `WHEN Con WITH field IS f THEN`, is a parse error; bind positionally, `WHEN \`Con\` n f THEN`.
- A type whose name has spaces must be backticked in a `GIVEN` or a field type: `IS A Mode of conviction` gives "I could not find a definition for the identifier Mode / of / conviction" (three errors); write `IS A \`Mode of conviction\``.
- A constructor is not a type: typing a `GIVEN` with a constructor's name is an error.
- A list of records needs each record in brackets: `LIST (R OF a, b), (R OF c, d)`; without the brackets the two records read as one record with four arguments.
- `WAIT UNTIL` is spelled `WAITUNTIL`; an `#ASSERT` must be on one line; `TYPICALLY` on a record field is not accepted; `REFUSE`, `#ASSERT REFUSED` and `YMD` are in the supplied builds but are not used here (the brief and PLAN.md say so).
- A section `GIVEN` read by a second rule is "I could not find a definition" (measured by the keel, PLAN.md section 5): each function declares its own `GIVEN`.

**Silent** (exit 0, a wrong answer; these are the ones worth the attention):
- `NOT (x) OR y` and `NOT (x) AND y` read as `NOT ((x) OR y)`: the `NOT` takes everything to its right when it leads a condition. Measured on 1.6.110 on the `s 188(6)` and `s 190(4)` functions and the `s 188(2)` holding-company limb: six assertions went red, and every other test passed, so a fixture-only check would not have found it. Bracket the whole `NOT` too: `(NOT (x)) OR y`.
- A `#TRACE` outcome is not an assertion line, so `check.sh` does not compare it across builds. There are 29 traces (requirements 4, notification 6, removal 3, declaration 2, general duties 14). Each was read by hand when written, and on 2026-11-13 the whole output of the five trace-bearing test files was compared between 1.6.110 and 1.6.109 (paths normalised): no difference in any line.

## Tests

Expected values are written beside each assertion from the section named, before the code was run. The tests were written branch by branch from the comments beside each branch (I did not measure branch coverage mechanically); the thresholds have a test on each side (for example: a term of exactly two years is not longer than two years, 100,000 pounds is not more than 100,000, 5,000 pounds is not more than 5,000, a memorandum available for 14 days is short of 15, a notice on the 14th day is in time and on the 15th is late, a person is not under 16 on the sixteenth birthday); every seat question has a case; and most rules and seat questions that can answer NOTHING have an asserted "not covered" case. No assertion is meant to fail; `expected_failed` is empty.

## What check.sh prints

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` in this folder (target `main`: every module is also run with the 1.6.109 build and the counts compared). The keel's baseline was 3 modules and 346 assertions (`coa-definitions-tests.l4`, which is not in this deposit folder); this folder prints 20 modules and 1,372 assertions: 978 in the eight test modules and 394 in the seat cases.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa4-appointment.l4                            0         0       0        0         0 |      0         0       0        0  same
coa4-approval-loans.l4                         0         0       0        0         0 |      0         0       0        0  same
coa4-approval-service-property.l4              0         0       0        0         0 |      0         0       0        0  same
coa4-cases-seat.l4                             0       321       0        0         0 |      0       321       0        0  same
coa4-declaration.l4                            0         0       0        0         0 |      0         0       0        0  same
coa4-general-duties.l4                         0         0       0        0         0 |      0         0       0        0  same
coa4-notification.l4                           0         0       0        0         0 |      0         0       0        0  same
coa4-removal.l4                                0         0       0        0         0 |      0         0       0        0  same
coa4-requirements.l4                           0         0       0        0         0 |      0         0       0        0  same
coa4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa4-tests-appointment.l4                      0        88       0        0         0 |      0        88       0        0  same
coa4-tests-approval-loans.l4                   0       187       0        0         0 |      0       187       0        0  same
coa4-tests-approval-service-property.l4        0       146       0        0         0 |      0       146       0        0  same
coa4-tests-declaration.l4                      0       107       0        0         0 |      0       107       0        0  same
coa4-tests-general-duties.l4                   0       179       0        0         0 |      0       179       0        0  same
coa4-tests-notification.l4                     0       178       0        0         0 |      0       178       0        0  same
coa4-tests-removal.l4                          0        59       0        0         0 |      0        59       0        0  same
coa4-tests-requirements.l4                     0       107       0        0         0 |      0       107       0        0  same
TOTAL (20 modules)                             0      1372       0        0           |      0      1372       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

