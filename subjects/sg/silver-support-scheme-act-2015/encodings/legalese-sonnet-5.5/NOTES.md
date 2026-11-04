# Silver Support Scheme Act 2015 (Singapore): encoding `legalese-sonnet-5.5`

**Status: draft, not reviewed.**
How it was checked: mechanically only, by the gates listed under "What `check.sh` prints" and by the author's own reading of the deposited text.
No lawyer or other domain expert has read it against the text.
It has not been checked against the official text of the Act, and nothing in it is "verified against the official text".

The text it encodes is a plain-text rendering made by a converter script (`inputs/SSSA2015.txt`, 955 lines, sha256 `3e8b8392d4cb4cf078486b91439d47ca37d78e3210c6d7d723cbc9e9314cfee6`) of the informal consolidation on Singapore Statutes Online, "2020 Revised Edition, version in force from 1/12/2025".
That is a rendering of an unofficial consolidation, not the official text of the Act.
The converter's page furniture and its mis-aligned arrangement of sections are recorded below (findings 22 and 23).
The terms on which the text may be quoted are in `SOURCE-LICENSE.md`.

Target compiler: `main` (the brief's target).
Written with the stable `l4` 1.6.98 (`l4-stable-98`) and compared with the main build 1.6.108 (`2ae7c9b`, 2026-11-02): every module has the same four counts on both.

## What this is

A fresh, whole encoding of the Act in two layers.

- **Layer 1: the law, objectively.**
  Five modules in reading order: `sssa-nouns.l4` (the nouns), `sssa-part1-preliminary.l4` (s 2), `sssa-part2-scheme.l4` (ss 5 to 7), `sssa-part3-administration.l4` (ss 8 to 10), `sssa-part4-miscellaneous.l4` (ss 11 to 20).
  Each rule carries an `@ref` with `src:` locators into the deposited text, and the quotation it relies on, copied mechanically with `srcrefs.py quote`.
  Four test modules, `sssa-tests-part1.l4` to `sssa-tests-part4.l4`, test them.
- **Layer 2: the seat.**
  `sssa-seat.l4` asks 33 questions as the person asks them, over layer 1, and `sssa-cases-seat.l4` has 148 worked cases.

## Seat

The seat is a person who is, or may become, entitled to Silver Support payments: a citizen of Singapore aged 65 or over, or about to be.
They ask whether they are eligible; how and when payment is made; when it stops or is withdrawn; what they must tell the authorities; and what they can be made to repay.
The individual comes first and is the only seat.
There is never a seat for an official, so the Minister, the Board, the Commissioner, an administrator, an investigator, the court and a department appear only as what they mean to the person.
Provisions that address only an official (ss 5, 8(1), 8(2), 8(5), 9(1), 9(3), 9(4), 9(6), 18, and the immunities of ss 8(4)(b) and (c)) are in layer 1 for what they decide and have no question of their own, because the facts they turn on are ones the person cannot state.

What the seat cannot answer:

- **A system built on this encoding alone cannot answer "am I eligible?"** without the regulations.
  Section 6(1)(c) makes a person an eligible individual only if they "satisfy all other eligibility criteria that may be prescribed".
  Section 7(1) leaves "such benefits in such manner and of such amounts as may be prescribed" to the same regulations, and s 20(2) lists what the regulations may cover.
  The regulations are not among the sources, so each criterion, amount and manner is an input (the person states whether they meet the criteria; the amount is a number they give), and the answer is `NOTHING` when it is not known.
  The seat question on how and when payment is made answers `NOTHING` for everyone.
- When payment stops or is withdrawn: the deposited text has no provision that ends or suspends a benefit, so the seat question `Does my benefit stop because of the change` answers `NOTHING` whatever has changed.
  The words `cease`, `withdraw`, `suspend`, `cancel`, `terminate`, `die` and `death` do not occur in the body of the Act (lines 77 to 898; checked with a whole-word search).
  Terms and conditions for each benefit are left to regulations by s 20(2)(c).
  The only provisions that take money back are s 10 (recovery) and s 12 (the court's order on conviction).
- What the person must tell the authorities: the deposited body contains no provision requiring a recipient to report a change of circumstances, so the seat question `Must I tell the authorities about the change` answers `NOTHING` whatever has changed.
  The word `report` occurs only in s 9(3)(b) and s 9(5), where it is a report the authorities make about the person (lines 482 to 506).
  The person's duties to give information are the compulsory powers of s 14, and the consequences of false statements are ss 10(2) and 11.

The figures the Act itself states (the ceilings of its penalties, the $1,000 cap on a compounded sum, the 65th year) are taken from the modules.
Nothing in the seat substitutes a figure, and the Act lets no minister substitute any of its own figures (the 65 years, the ceilings, the $1,000), so there is no substitution whose effect on the answers needs recording; what the regulations prescribe is an input.

## What is encoded and what is not

Everything in the body of the Act is disposed of in the coverage table below; none of it is silently skipped.
In short:

- **Encoded.**
  The definitions in s 2 (one function per defined term).
  The Scheme's name and purpose (s 5(1)).
  Who is an eligible individual and when a person attains 65, with the 29 February, unknown-day and unknown-month rules (s 6).
  The grant of benefits (s 7), with benefits, amounts and manner as inputs.
  The Minister's directions to departments and the duty to comply (s 8(1), (2)), the opt-out bar (s 8(3), s 9(5)), the immunities (s 8(4)), terms and conditions (s 8(5), s 9(4)), the definitions of s 8(7), the offence and its ceiling (s 8(6), s 9(7)).
  To whom s 9 applies, the purpose test for use or disclosure (s 9(2)), reports for a prescribed public scheme (s 9(3)), the Board's use of its CPF Act information (s 9(6)).
  Recovery of overpaid and fraudulently obtained sums, and the sources it may be taken from (s 10).
  The offences of ss 11, 14(4) and 15 and their ceilings, the court's order and the administrator's certificate (ss 12, 13), the compulsory powers (s 14(1) to (3)), bodies corporate, partnerships and associations (s 16), composition (s 17), prosecutions (s 18), personal liability (s 19), and the regulation-making matters and the ceiling for offences in regulations (s 20(1) to (3)).
- **Regulative rules** (a duty or a bar, run with `#TRACE`): ss 8(1)(b), 8(2)(b), 8(3)(a), 8(3)(b), 9(5), 14(4), 17(3).
  A `#TRACE` prints FULFILLED, a breach or a residual obligation and never an assertion line, so no assertion can be made on one on the stable binary; `traces.py` (not shipped) reads each printed result and compares it with the `-- EXPECT` comment above the trace, and each duty is also encoded as a decision function over plain facts that carries the assertions.
  No time limit is invented: ss 8(1)(b), 8(2)(b) and 17(3) have none in the text; s 14(4) takes the requirer's days as a parameter.
- **Inputs, not encoded, because they are not among the sources:** the criteria, benefits, amounts and manner prescribed under ss 6(1)(c), 7 and 20; which public schemes are prescribed for s 9(3); which offences are prescribed as compoundable for s 17(1); the Central Provident Fund Act 1953 (the Board), the Financial Procedure Act 1966 (s 20), the Immigration Act 1959 (permanent resident), the Limited Liability Partnerships Act 2005 (s 2(1)); what a "public officer", a "public Act", a "public function" or "written law" is; whether a person is a citizen of Singapore.
- **Not encoded as rules (inert):** the short title (s 1), the purpose (s 3), the machinery for appointing the Commissioner (s 4) and for the Board, administrators and investigators (s 5(2) to (8)), the lead-ins to definitions, the presentation of regulations to Parliament (s 20(4)), and the front matter, headings, arrangement, long title, commencement note, legislative history, abbreviations table and page furniture.
  The effect of an appointment under s 4 or s 5 enters as a fact in the definitions in s 2.

## Jural relations

One row per provision that creates a relation.
"None" means a definition, a counting rule, a statement of purpose, evidence law or a lead-in.
Hohfeldian pairs are named as the text gives them; where the text does not say who bears the correlative, the cell says so.

| provision | holder | relation | counter-party | correlative | L4 rule |
|---|---|---|---|---|---|
| s 2 definitions | none | none | none | none | the `s 2 ...` functions |
| s 3 purpose | none | none | none | none | not encoded (inert, reason 1) |
| s 4 appointments | the Minister | power to appoint the Commissioner and deputies | the appointee | liability to be appointed | not encoded (inert, reason 2); enters as `Appointment under section 4` |
| s 5(1) | none | none (establishes the Scheme) | none | none | `s 5(1) ...` (the name and purpose) |
| s 5(2) to (3) | the Board | power and duty to administer the Scheme and enforce the Act, subject to the Commissioner's directions | the Government | not stated | not encoded (inert, reason 2) |
| s 5(4), (5), (6) | the Minister | power to appoint administrators; duty to gazette | the appointee | liability | not encoded (inert, reason 2); enters in `s 2 the body is an administrator` |
| s 5(7), (8) | the Board; the Minister | power to authorise or appoint investigators | the officer, employee or appointee | liability | not encoded (inert, reason 2); enters in `s 2 the person is an investigator` |
| s 6(1), (2) | none | none (the status "eligible individual" and how age is counted) | none | none | `s 6(1)`, `s 6(1)(b)`, `s 6(2)(a)` and the others in `sssa-part2-scheme.l4` |
| s 7(1) | an eligible individual | claim to be eligible to receive the benefits prescribed | not stated in the Act; the administrator disburses (s 5(4)) | not stated | `s 7(1) ...` |
| s 7(2) | the Minister | power (by regulations) to prescribe different benefits, methods and amounts by class | classes of eligible individual | liability | `s 7(2) the amount prescribed for the class ...` |
| s 8(1)(a), (2)(a) | the Minister responsible for the department or authority | power to direct it to provide the information | the department or authority | liability to the direction | `s 8(1)(a) ...`, `s 8(2)(a) ...` |
| s 8(1)(b), (2)(b) | the authorised person; the information recipient | claim that the direction be complied with | the department or authority | duty to comply, despite other law | `s 8(1)(b) ...`, `s 8(2)(b) ...`, the two `duty` rules |
| s 8(3) | the individual | power to opt out; power to consent | the authorised person | duty not to access, use or disclose after notice, unless the individual consents | `s 8(3) the authorised person is barred from the act`, `s 8(3)(a)`, `s 8(3)(b)` |
| s 8(4)(a) | the department, authority or person disclosing | immunity from criminal, confidence and civil liability merely for disclosing as directed | whoever would sue or prosecute | disability | `s 8(4)(a) ...` |
| s 8(4)(b), (c) | the authorised person; the officer | immunity (good faith, reasonable care) | whoever would sue or prosecute | disability | `s 8(4)(b) ...`, `s 8(4)(c) ...` |
| s 8(5) | the Minister | power to attach terms and conditions to a direction | the department or authority | liability | `s 8(5) ...` |
| s 8(6) | the State (prosecution and court) | power to convict and punish | a person who contravenes s 8(3) | liability to a fine up to $5,000 or imprisonment up to 12 months or both | `s 8(6) ...` |
| s 8(7) | none | none (definitions) | none | none | `s 8(7) ...` |
| s 9(1) | none | none (scope) | none | none | `s 9(1) ...` |
| s 9(2) | the individual | claim that their information is not used or disclosed without consent except for the stated purposes | the persons in s 9(1) | duty not to use or disclose otherwise | `s 9(2) ...` |
| s 9(3) | the Commissioner, the Board, an administrator | privilege (liberty) to give a report for a prescribed public scheme, on request and with the Minister's approval | the individual | no-right | `s 9(3) ...` |
| s 9(4) | the Minister | power to attach terms to the approval | the Commissioner, the Board, an administrator | liability | `s 9(4) ...` |
| s 9(5) | the individual | power to opt out of a report; power to consent | the Commissioner, the Board or the administrator | duty not to provide the report after notice, unless the individual consents | `s 9(5) ...`, the `bar` rule |
| s 9(6) | the Board | privilege to use its CPF Act information to administer the Scheme as the Minister approves | the individual | no-right | `s 9(6) ...` |
| s 9(7) | the State | power to convict and punish | a person who contravenes s 9(2), (3) or (5) | liability to a fine up to $5,000 or imprisonment up to 12 months or both | `s 9(7) ...` |
| s 10(1), (2) | the Government | claim to the amount as a debt | the recipient; the individual who obtained by falsehood | duty to repay | `s 10(1) ...`, `s 10(2) ...` |
| s 10(3) | an administrator | power to recover by set-off or otherwise | the recipient or individual | liability | `s 10(3) ...` |
| s 11(1) | the State | power to convict and punish | a person who dishonestly obtains a benefit by a false statement or document | liability to a fine up to $5,000 or imprisonment up to 12 months or both | `s 11(1) ...` |
| s 11(2) | none | none (savings: the right of recovery under s 10 is unaffected) | none | none | `s 11(2) ...` |
| s 12 | the court | power to order the person to pay the certified amount to an administrator | a convicted person | liability | `s 12 ...` |
| s 13 | none | none (evidence: the certificate is prima facie evidence) | none | none | `s 13 ...` |
| s 14(1), (2) | the Commissioner; an investigator | power to require attendance, information, production, retention and copies | any person | liability to the requirement | `s 14(1) ...`, `s 14(2)(a)`, `s 14(2)(b)` |
| s 14(3) | none | none (evidence: certified copies are admissible) | none | none | `s 14(3) ...` |
| s 14(4) | the Commissioner; an investigator | claim to the information or document within the time allowed | the person required | duty to provide it in time; liability to a fine up to $10,000 or imprisonment up to 6 months or both | `s 14(4) ...`, the `duty` rule |
| s 15 | the Commissioner; an investigator | claim not to be obstructed | any person | duty not to obstruct without reasonable excuse; liability to a fine up to $20,000 or imprisonment up to 12 months or both | `s 15 ...` |
| s 16(1) to (4) | the State | power to convict the officer, partner or member as well as the body | the officer, partner or member | liability | `s 16(1)`, `s 16(2)`, `s 16(3)`, `s 16(4)` |
| s 16(5) | none | none (definitions) | none | none | `s 16(5) ...` |
| s 17(1) | the Board and its authorised officers and employees | power to compound a prescribed offence for a sum up to the lower of half the maximum fine and $1,000 | a person reasonably suspected | liability | `s 17(1) ...` |
| s 17(2) | the person who paid | immunity from further proceedings for the offence | the State | disability | `s 17(2) ...` |
| s 17(3) | the Consolidated Fund | claim to all sums collected | the collector | duty to pay them in | `s 17(3) ...`, the `duty` rule |
| s 18 | the Board's authorised officer or employee | power to conduct proceedings with the Public Prosecutor's authorisation | the proceedings | none stated | `s 18 ...` |
| s 19(1) to (3) | the individuals listed | immunity from personal liability for acts in good faith with reasonable care | anyone who would sue them personally | disability | `s 19 ...` |
| s 19(4) | none | none (to avoid doubt: liabilities under FPA s 20, s 8(6), s 9(7) remain) | none | none | `s 19(4) ...` |
| s 20(1), (2) | the Minister | power to make regulations for the purposes and provisions of the Act and the matters listed | those regulated | liability | `s 20(1) ...`, `s 20(2) ...` |
| s 20(3) | the Minister | power to make a contravention of the regulations an offence | those regulated | liability to a fine up to $2,000 or imprisonment up to 12 months or both | `s 20(3) ...` |
| s 20(4) | the Minister | duty to present regulations to Parliament | Parliament | not stated | not encoded (inert, reason 2) |

## Coverage table

Audit: text lines counted: 684 non-blank, 684 assigned; units: 199; dispositions: encoded=141, fork=11, inert=47; problems: 0.
Rows in the table before this work: 0 (a fresh encoding); after: 199.
Dispositions: encoded 141, fork 11, inert reason 1 (not operative) 26, inert reason 2 (machinery) 21, inert reason 3 (repealed or blank) 0, repealed or blank 0.
No row was moved out of `inert` (the encoding is fresh); 47 rows are left `inert`, each with its reason in the table.


Every section, subsection, paragraph, table row and defined term of the deposited text has one row, found by `coverage.py` (not shipped) from the text itself and checked against `coverage-map.txt` (not shipped).
The checker assigns every non-blank line of the text to one unit, requires every `encoded` or `fork` row to cite rules that are defined, have a locator-covered `@ref`, and are used in an `#ASSERT`, `#EVAL` or `#TRACE`, and requires every `inert` row to give a reason.
Reason 1 is "not operative", reason 2 is "machinery", reason 3 is "repealed or blank"; no unit is repealed or blank in this text.

| unit | kind | lines | opens with | disposition | where / why |
| --- | --- | --- | --- | --- | --- |
| front | front matter | 1-2, 4, 6-7, 9-10, 12-13, 16, 18 | THE STATUTES OF THE REPUBLIC OF SINGAPORE | inert (reason 1) | `/` - title block and edition banner |
| furniture | furniture | 15, 63, 65-66, 113-114, 161-162, 208-209, 252-253, 302-303, 348-349, 394-395, 443-444, 490-491, 537-538, 585-586, 632-633, 678-679, 724-725, 774-775, 822-823, 869-870, 900, 935-936, 954 | Informal Consolidation – version in force from 1... | inert (reason 1) | `/` - running headers, footers and page numbers |
| arrangement | arrangement of sections | 20, 22, 24, 26-31, 33, 35, 37-39, 41, 43, 45-47, 49, 51, 53-61, 68-69 | ARRANGEMENT OF SECTIONS | inert (reason 1) | `/` - arrangement of sections (a list of headings; the converter pairs numbers 1-4 with the wrong titles, see NOTES finding) |
| long-title | long title | 71-72 | An Act to provide for a social security scheme c... | inert (reason 1) | `/` - long title |
| commencement-note | commencement note | 74-75 | [18 January 2016: Except sections 6 and 7 ; | inert (reason 2) | `/` - the Act's own commencement dates (18 Jan 2016; 22 Jul 2016 for ss 6 and 7) |
| legislative-history | legislative history | 901-902, 904-905, 907, 909, 911, 913, 915-917, 919, 921, 923-924, 926, 928, 930, 932-933 | LEGISLATIVE HISTORY | inert (reason 1) | `/` - "not part of the Act" (its own words) |
| abbreviations | abbreviations table | 937-952 | Abbreviations | inert (reason 1) | `/` - table of abbreviations, not operative |
| part1 | part heading | 77, 79 | PART 1 | inert (reason 1) | `/` - part heading |
| s1 | section | 81, 83 | Short title | inert (reason 2) | `/` - short title |
| s2 | section | 85, 87 | Interpretation | encoded | `s 2 the definitions apply to the term as used` - chapeau: the definitions hold unless the context otherwise requires |
| s2:administrator | defined term | 89-91 | “administrator” means the Board, or any public o... | encoded | `s 2 the body is an administrator` |
| s2:Board | defined term | 93-94 | “Board” means the Central Provident Fund Board c... | encoded | `s 2 the body is the Board` - a fact: the CPF Board constituted under the CPF Act 1953, outside the sources |
| s2:cash grant | defined term | 96-97 | “cash grant” means any cash grant made by the Go... | encoded | `s 2 the payment is a cash grant` |
| s2:Commissioner | defined term | 99-102 | “Commissioner” means the Commissioner for Silver... | encoded | `s 2 the person is the Commissioner` |
| s2:eligible individual | defined term | 104-105 | “eligible individual” means an individual who is... | fork | `s 2 the person is an eligible individual` - FORK F-1: the s 2 statement, read with s 6(1) and s 7(1) as one status [fork F-1] |
| s2:investigator | defined term | 107-111 | “investigator” means an officer or employee of t... | encoded | `s 2 the person is an investigator` |
| s2:means information | defined term | 116-119 | “means information” means any information relati... | encoded | `s 2 the information is means information` |
| s2:permanent resident of Singapore | defined term | 121-122, 124 | “permanent resident of Singapore” has the meanin... | encoded | `s 2 the person is a permanent resident of Singapore` - borrowed from s 2 of the Immigration Act 1959 (outside the sources): the stated fact answers |
| s2:public authority | defined term | 126-127 | “public authority” means a body established or c... | encoded | `s 2 the body is a public authority` |
| s2:public scheme | defined term | 129 | “public scheme” means any scheme that — | encoded | `s 2 the scheme is a public scheme` |
| s2:public scheme(a) | paragraph | 131-133 | (a) is or will be established by or under any wr... | encoded | `s 2 the scheme is a public scheme` |
| s2:public scheme(b) | paragraph | 135-137, 139 | (b) is to provide financial relief, assistance o... | encoded | `s 2 the scheme is a public scheme` |
| s2:Scheme | defined term | 141-142 | “Scheme” means the Silver Support Scheme establi... | encoded | `s 2 the scheme is the Scheme` |
| s3 | section | 144, 146-148 | Purpose of Act | inert (reason 1) | statement of purpose: it creates no right, duty, power or immunity of its own |
| s4 | section | 150 | Administration of Act | inert (reason 1) | section heading |
| s4(1) | subsection | 152-153 | 4.—(1) The Minister may in writing appoint a pub... | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| s4(2) | subsection | 155 | (2) The Minister may in writing — | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| s4(2)(a) | paragraph | 157-159 | (a) appoint any public officer, or any employee ... | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| s4(2)(b) | paragraph | 164-166 | (b) appoint any public officer, or any employee ... | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| s4(3) | subsection | 168-169 | (3) The Commissioner for Silver Support is respo... | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| s4(4) | subsection | 171-175 | (4) Subject to the directions of the Commissione... | inert (reason 2) | machinery: appointing the Commissioner and his deputies and directing him; the appointment enters as a fact (`Appointment under section 4`) in s 2 "Commissioner" |
| part2 | part heading | 177, 179 | PART 2 | inert (reason 1) | `/` - part heading |
| s5 | section | 181 | Establishment of Silver Support Scheme | inert (reason 1) | section heading |
| s5(1) | subsection | 183-185 | 5.—(1) There is established a social security sc... | encoded | `s 5(1) the name by which the established scheme is known`; `s 5(1) the purpose for which the Scheme is established` - the Scheme's name and purpose carried as two constants |
| s5(2) | subsection | 187-189 | (2) Subject to the directions of the Commissione... | inert (reason 2) | machinery: the Board administers the Scheme and enforces the Act on behalf of the Government, subject to the Commissioner's directions |
| s5(3) | subsection | 191-193 | (3) Subject to the provisions of this Act, where... | inert (reason 2) | machinery: the Board's status under the CPF Act 1953 and the Financial Procedure Act 1966 when administering the Scheme |
| s5(3)(a) | paragraph | 195-199 | (a) the Board is to be regarded as fulfilling th... | inert (reason 2) | machinery: the Board is regarded as fulfilling the purposes of the CPF Act 1953 |
| s5(3)(b) | paragraph | 201-206, 211-212 | (b) the members, officers and employees of the B... | inert (reason 2) | machinery: the Board's members, officers and employees are deemed public officers for the Financial Procedure Act 1966 |
| s5(4) | subsection | 214-217 | (4) The Minister may appoint any public officer,... | inert (reason 2) | machinery: the Minister appoints administrators; the appointment enters as a fact in s 2 "administrator" |
| s5(5) | subsection | 219-221 | (5) The Minister must, as soon as practicable, c... | inert (reason 2) | machinery: Gazette notice of an appointment |
| s5(6) | subsection | 223-225 | (6) Subject to the provisions of this Act, where... | inert (reason 2) | machinery: the effect of appointing a public authority as an administrator |
| s5(6)(a) | paragraph | 227-229 | (a) the functions and duties of the public autho... | inert (reason 2) | machinery: the authority's functions include administering the Scheme |
| s5(6)(b) | paragraph | 231-235 | (b) the public authority is to be regarded as fu... | inert (reason 2) | machinery: the authority is regarded as fulfilling the purposes of its constituting Act |
| s5(6)(c) | paragraph | 237-244 | (c) the members, officers and employees of the p... | inert (reason 2) | machinery: the authority's members, officers and employees are deemed public officers for the Financial Procedure Act 1966 |
| s5(7) | subsection | 246-247 | (7) The Board may authorise any officer or emplo... | inert (reason 2) | machinery: the Board authorises an officer or employee to investigate; the authorisation enters as a fact in s 2 "investigator" |
| s5(8) | subsection | 249-250 | (8) The Minister may in writing appoint any pers... | inert (reason 2) | machinery: the Minister appoints a person to assist an investigation; the appointment enters as a fact in s 2 "investigator" |
| s6 | section | 255 | Who is an eligible individual? | inert (reason 1) | section heading |
| s6(1) | subsection | 257 | 6.—(1) In this Act, an eligible individual is an... | encoded | `s 6(1) the individual is an eligible individual` - the three limbs read as a definition; limb (c) is an input |
| s6(1)(a) | paragraph | 259 | (a) is a citizen of Singapore; | encoded | `s 6(1) the individual is an eligible individual` - citizenship is a fact (borrowed status) |
| s6(1)(b) | paragraph | 261 | (b) has attained 65 years of age; and | fork | `s 6(1)(b) the individual has attained 65 years of age` - FORK F-5: the date the question is asked about is supplied by the caller [fork F-5] |
| s6(1)(c) | paragraph | 263 | (c) satisfies all other eligibility criteria tha... | encoded | `s 6(1) the individual is an eligible individual` - the criteria that may be prescribed are in regulations outside the sources: an input |
| s6(2) | subsection | 265 | (2) For the purposes of subsection (1)(b) — | encoded | `s 6(2)(a) the date on which the individual attains 65 years of age` |
| s6(2)(a) | paragraph | 267-268 | (a) an individual attains 65 years of age on the | encoded | `s 6(2)(a) and (b) the 65th anniversary of the date of birth`; `s 6(2)(a) the date on which the individual attains 65 years of age`; `s 6(1)(b) the individual has attained 65 years of age` |
| s6(2)(b) | paragraph | 270-272 | (b) where an individual was born on 29 February,... | encoded | `s 6(2)(a) and (b) the 65th anniversary of the date of birth`; `s 6(2)(a) the date on which the individual attains 65 years of age`; `s 6(1)(b) the individual has attained 65 years of age` - 1 March, built from components, not by adding years |
| s6(2)(c) | paragraph | 274-276 | (c) where the day of the month in which an indiv... | encoded | `s 6(2)(c) the day of the month of birth taken for s 6(1)(b)`; `s 6(2)(a) the date on which the individual attains 65 years of age` |
| s6(2)(d) | paragraph | 278-280 | (d) where the month in which an individual was b... | fork | `s 6(2)(d) the month of birth taken for s 6(1)(b)`; `s 6(2)(a) the date on which the individual attains 65 years of age` - FORK F-2: where the month cannot be ascertained but the day can, the day is kept [fork F-2] |
| s7 | section | 282 | Benefits | inert (reason 1) | section heading |
| s7(1) | subsection | 284-285 | 7.—(1) An eligible individual is eligible to rec... | encoded | `s 7(1) the individual is eligible to receive the benefits that may be prescribed`; `s 7(1) the amount of benefit an eligible individual is eligible to receive`; `s 7(1) the manner in which an eligible individual is to receive the benefit` - the grant to an eligible individual; benefits, manner and amounts are inputs (regulations outside the sources) |
| s7(2) | subsection | 287-290 | (2) For the purposes of subsection (1), differen... | encoded | `s 7(2) the amount prescribed for the class of eligible individual` - classes and amounts are in regulations outside the sources: the table is an input |
| part3 | part heading | 292, 294 | PART 3 | inert (reason 1) | `/` - part heading |
| s8 | section | 296 | Provision of information for administration of A... | inert (reason 1) | section heading |
| s8(1) | subsection | 298-300, 305-306 | 8.—(1) Where the Minister certifies in writing t... | encoded | `s 8(1)(a) the Minister may direct the department or authority to provide the information`; `s 8(1)(b) the department or authority must comply with the direction`; `s 8(1)(b) duty of the department or authority` |
| s8(1)(a) | paragraph | 308-313 | (a) the Minister charged with the responsibility... | encoded | `s 8(1)(a) the Minister may direct the department or authority to provide the information` |
| s8(1)(b) | paragraph | 315-319 | (b) that Government department or public authori... | encoded | `s 8(1)(b) the department or authority must comply with the direction`; `s 8(1)(b) duty of the department or authority` - a duty with no time limit in the text |
| s8(2) | subsection | 321-326 | (2) Where the Minister certifies in writing that... | encoded | `s 8(2)(a) the Minister may direct the department or authority to provide the information`; `s 8(2)(b) the department or authority must comply with the direction`; `s 8(2)(b) duty of the department or authority` |
| s8(2)(a) | paragraph | 328-334 | (a) the Minister charged with the responsibility... | encoded | `s 8(2)(a) the Minister may direct the department or authority to provide the information` |
| s8(2)(b) | paragraph | 336-340 | (b) that Government department or other public a... | encoded | `s 8(2)(b) the department or authority must comply with the direction`; `s 8(2)(b) duty of the department or authority` - a duty with no time limit in the text |
| s8(3) | subsection | 342-346 | (3) If an individual opts out, in the manner det... | encoded | `s 8(3) the authorised person is barred from the act`; `s 8(3)(a) bar on the authorised person`; `s 8(3)(b) bar on the authorised person` |
| s8(3)(a) | paragraph | 351-352 | (a) access any means information about the indiv... | encoded | `s 8(3) the authorised person is barred from the act`; `s 8(3)(a) bar on the authorised person` |
| s8(3)(b) | paragraph | 354-355 | (b) use or disclose under section 9 any such mea... | encoded | `s 8(3) the authorised person is barred from the act`; `s 8(3)(b) bar on the authorised person` |
| s8(3)-tail | subsection tail | 357 | except with the consent of that individual. | encoded | `s 8(3) the authorised person is barred from the act` - the consent exception |
| s8(4) | subsection | 359-360 | (4) Despite the provisions of this Act or any ot... | encoded | `s 8(4)(a) the person is not guilty or liable merely by disclosing in accordance with the direction`; `s 8(4)(b) the authorised person is not guilty or liable merely by accessing or disclosing the means information`; `s 8(4)(c) the officer is not guilty or liable merely by accessing or disclosing the confidential information` - lead-in: subject to s 8(3) |
| s8(4)(a) | paragraph | 362-366 | (a) a person is not guilty of an offence under a... | encoded | `s 8(4)(a) the person is not guilty or liable merely by disclosing in accordance with the direction` |
| s8(4)(b) | paragraph | 368-378 | (b) an authorised person (being an officer of an... | encoded | `s 8(4)(b) the authorised person is not guilty or liable merely by accessing or disclosing the means information` |
| s8(4)(c) | paragraph | 380-389 | (c) an officer of an information recipient is no... | encoded | `s 8(4)(c) the officer is not guilty or liable merely by accessing or disclosing the confidential information` |
| s8(5) | subsection | 391-392, 397-398 | (5) A direction under subsection (1)(a) or (2)(a... | encoded | `s 8(5) the Minister giving the direction may impose terms and conditions regarding access` |
| s8(6) | subsection | 400-403 | (6) Any person who does any act in contravention... | encoded | `s 8(6) the greatest penalty`; `s 8(6) the person is guilty of an offence`; `s 8(6) the sentence is within the greatest penalty` |
| s8(7) | subsection | 405 | (7) In this section — | inert (reason 1) | lead-in to the definitions that follow ("In this section —") |
| s8(7):authorised person | defined term | 407 | “authorised person” means — | encoded | `s 8(7) the person is an authorised person` |
| s8(7):authorised person(a) | paragraph | 409 | (a) the Commissioner; or | encoded | `s 8(7) the person is an authorised person` |
| s8(7):authorised person(b) | paragraph | 411-413 | (b) any other officer of an information recipien... | encoded | `s 8(7) the person is an authorised person` |
| s8(7):information recipient | defined term | 415-416 | “information recipient” means the Commissioner, ... | encoded | `s 8(7) the person is an information recipient` |
| s8(7):officer | defined term | 418 | “officer”, in relation to an information recipie... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s8(7):officer(a) | paragraph | 420-423 | (a) in any case where the information recipient ... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s8(7):officer(b) | paragraph | 425-429 | (b) in any case where the information recipient ... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s8(7):officer(c) | paragraph | 431-433 | (c) in any case where the information recipient ... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s8(7):officer(d) | paragraph | 435-438 | (d) in any case where the information recipient ... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s8(7):officer(e) | paragraph | 440-441, 446-447 | (e) in any case where the information recipient ... | encoded | `s 8(7) the person is an officer in relation to the information recipient` |
| s9 | section | 449 | Use of information | inert (reason 1) | section heading |
| s9(1) | subsection | 451-456 | 9.—(1) This section applies to the Commissioner,... | fork | `s 9(1) section 9 applies to the person` - FORK F-9: the list of persons is not closed with "only" [fork F-9] |
| s9(2) | subsection | 458-463 | (2) The use or disclosure of means information o... | encoded | `s 9(2) the use or disclosure is authorised`; `s 9(2) the purpose is one the subsection names` |
| s9(2)(a) | paragraph | 465 | (a) the administration or enforcement of this Ac... | encoded | `s 9(2) the use or disclosure is authorised`; `s 9(2) the purpose is one the subsection names` |
| s9(2)(b) | paragraph | 467 | (b) the administration of the Scheme. | encoded | `s 9(2) the use or disclosure is authorised`; `s 9(2) the purpose is one the subsection names` |
| s9(3) | subsection | 469-476 | (3) Despite subsection (2), the Commissioner, th... | encoded | `s 9(3) the Commissioner, the Board or an administrator may provide the information` |
| s9(3)(a) | paragraph | 478-480 | (a) only at the request of the public officer, p... | encoded | `s 9(3) the Commissioner, the Board or an administrator may provide the information` |
| s9(3)(b) | paragraph | 482 | (b) only in the form of a report stating — | encoded | `s 9(3) the Commissioner, the Board or an administrator may provide the information` |
| s9(3)(b)(i) | sub-paragraph | 484-485 | (i) whether an individual satisfies the eligibil... | encoded | `s 9(3) the Commissioner, the Board or an administrator may provide the information` |
| s9(3)(b)(ii) | sub-paragraph | 487-488, 493-494 | (ii) the description and amount of each benefit ... | encoded | `s 9(3) the Commissioner, the Board or an administrator may provide the information` |
| s9(4) | subsection | 496-498 | (4) An approval under subsection (3)(a) may be g... | encoded | `s 9(4) the Minister may give the approval on terms and conditions regarding access` |
| s9(5) | subsection | 500-506 | (5) If an individual opts out, in the manner det... | encoded | `s 9(5) the provider is barred from providing the report`; `s 9(5) bar on the Commissioner, the Board or the administrator` |
| s9(6) | subsection | 508-512 | (6) The Board may use to administer the Scheme s... | encoded | `s 9(6) the Board may use the information to administer the Scheme` - the date on which the Board obtained the information is made irrelevant by the text, so it is not an input |
| s9(7) | subsection | 514-517 | (7) Any person who does any act in contravention... | encoded | `s 9(7) the greatest penalty`; `s 9(7) the person is guilty of an offence`; `s 9(7) the sentence is within the greatest penalty` |
| s10 | section | 519 | Recovery of sums overpaid, etc. | inert (reason 1) | section heading |
| s10(1) | subsection | 521-522 | 10.—(1) If any benefit under the Scheme is disbu... | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(1)(a) | paragraph | 524 | (a) the recipient — | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(1)(a)(i) | sub-paragraph | 526 | (i) is not an eligible individual; or | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(1)(a)(ii) | sub-paragraph | 528-529 | (ii) is an eligible individual, but is not eligi... | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(1)(b) | paragraph | 531-532 | (b) the amount paid is in excess of the amount t... | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(1)-tail | subsection tail | 534-535 | the amount paid or paid in excess (as the case m... | encoded | `s 10(1) the amount made recoverable as a debt due to the Government` |
| s10(2) | subsection | 540-541 | (2) If any individual (whether or not an eligibl... | encoded | `s 10(2) the amount made recoverable as a debt due to the Government` |
| s10(2)(a) | paragraph | 543-544 | (a) by knowingly or recklessly making any false ... | encoded | `s 10(2) the amount made recoverable as a debt due to the Government` |
| s10(2)(b) | paragraph | 546-548 | (b) by producing or providing, or causing to be ... | encoded | `s 10(2) the amount made recoverable as a debt due to the Government` |
| s10(2)-tail | subsection tail | 550-551 | the amount of the cash grant or other benefit so... | encoded | `s 10(2) the amount made recoverable as a debt due to the Government` |
| s10(3) | subsection | 553-555 | (3) An administrator may recover on behalf of th... | encoded | `s 10(3) the administrator may recover the amount from the source` |
| s10(3)(a) | paragraph | 557-559 | (a) any cash grant or other benefit which the re... | encoded | `s 10(3) the administrator may recover the amount from the source` |
| s10(3)(b) | paragraph | 561-562 | (b) any other sum that is payable to that recipi... | encoded | `s 10(3) the administrator may recover the amount from the source` |
| part4 | part heading | 564, 566 | PART 4 | inert (reason 1) | `/` - part heading |
| s11 | section | 568 | Obtaining benefit through false or misleading st... | inert (reason 1) | section heading |
| s11(1) | subsection | 570 | 11.—(1) A person — | encoded | `s 11(1) the person is guilty of an offence` |
| s11(1)(a) | paragraph | 572 | (a) who — | encoded | `s 11(1) the person is guilty of an offence` |
| s11(1)(a)(i) | sub-paragraph | 574-575 | (i) knowingly or recklessly makes any false or | encoded | `s 11(1) the person is guilty of an offence` |
| s11(1)(a)(ii) | sub-paragraph | 577-580 | (ii) produces or provides, or causes to be produ... | encoded | `s 11(1) the person is guilty of an offence` |
| s11(1)(b) | paragraph | 582-583 | (b) who, with the intention of dishonestly induc... | fork | `s 11(1) the person is guilty of an offence` - FORK F-6: (a) and (b) are conjunctive; the intention in (b) refers to the statement or document of (a) [fork F-6] |
| s11(1)-tail | subsection tail | 588-589, 591-593 | dishonestly obtains any cash grant or other bene... | encoded | `s 11(1) the person is guilty of an offence`; `s 11(1) the greatest penalty`; `s 11(1) the sentence is within the greatest penalty` |
| s11(2) | subsection | 595-596 | (2) Subsection (1) does not affect any right of ... | encoded | `s 11(2) the right of recovery under section 10 is unaffected by section 11(1)` |
| s12 | section | 598, 600 | Recovery of cash grant, etc., upon conviction | encoded | `s 12 the court may order the person to pay the certified amount to an administrator`; `s 12 the amount the court may order the person to pay` - lead-in: "Where —" |
| s12(a) | paragraph | 602-603 | (a) a person has received any cash grant or othe... | encoded | `s 12 the court may order the person to pay the certified amount to an administrator`; `s 12 the amount the court may order the person to pay` |
| s12(b) | paragraph | 605-606 | (b) the person is convicted of an offence under ... | encoded | `s 12 the court may order the person to pay the certified amount to an administrator`; `s 12 the amount the court may order the person to pay` |
| s12-tail | subsection tail | 608-612 | the court before which the conviction is had may... | encoded | `s 12 the court may order the person to pay the certified amount to an administrator`; `s 12 the amount the court may order the person to pay` |
| s13 | section | 614, 616-619 | Certificate on amount of cash grant, etc. | encoded | `s 13 the certificate is prima facie evidence of the amount stated` |
| s13(a) | paragraph | 621-622 | (a) the amount of any cash grant or other benefi... | encoded | `s 13 the certificate is prima facie evidence of the amount stated` |
| s13(b) | paragraph | 624-626 | (b) the amount recoverable from any person as at... | encoded | `s 13 the certificate is prima facie evidence of the amount stated` |
| s13-tail | subsection tail | 628-630 | is prima facie evidence that the amount so state... | encoded | `s 13 the certificate is prima facie evidence of the amount stated` |
| s14 | section | 635 | Power to obtain information | inert (reason 1) | section heading |
| s14(1) | subsection | 637-640 | 14.—(1) The Commissioner may, for the purpose of... | encoded | `s 14(1) the requirer may make the requirement` |
| s14(1)(a) | paragraph | 642-647 | (a) by written notice require any person to atte... | encoded | `s 14(1) the requirer may make the requirement` |
| s14(1)(b) | paragraph | 649 | (b) require any person — | encoded | `s 14(1) the requirer may make the requirement` |
| s14(1)(b)(i) | sub-paragraph | 651-652 | (i) to provide any information within the person... | encoded | `s 14(1) the requirer may make the requirement` |
| s14(1)(b)(ii) | sub-paragraph | 654-655 | (ii) to produce for inspection any document or r... | encoded | `s 14(1) the requirer may make the requirement` |
| s14(1)(b)-tail | paragraph tail | 657-660 | (b) that the Commissioner or investigator (as th... | fork | `s 14(1) the requirer may make the requirement` - FORK F-3: the closing words are read as qualifying both (b)(i) and (b)(ii) [fork F-3] |
| s14(1)(c) | paragraph | 662-667 | (c) retain the original of any document or recor... | encoded | `s 14(1) the requirer may make the requirement` |
| s14(2) | subsection | 669-670 | (2) Where any document or record required by the... | encoded | `s 14(2)(a) the power to require production includes the power to require it in legible form`; `s 14(2)(b) section 14(1)(c) applies to the copy` |
| s14(2)(a) | paragraph | 672-676 | (a) the power of the Commissioner or investigato... | encoded | `s 14(2)(a) the power to require production includes the power to require it in legible form` |
| s14(2)(b) | paragraph | 681-682 | (b) subsection (1)(c) applies to any copy of tha... | encoded | `s 14(2)(b) section 14(1)(c) applies to the copy` |
| s14(3) | subsection | 684-687 | (3) Any copy of or extract from any document or ... | encoded | `s 14(3) the copy or extract is admissible as evidence` |
| s14(4) | subsection | 689-695 | (4) Any person who, when required by the Commiss... | fork | `s 14(4) the person is within the time allowed`; `s 14(4) the person is guilty of an offence`; `s 14(4) the greatest penalty`; `s 14(4) the sentence is within the greatest penalty`; `s 14(4) duty of the person required` - FORK F-4: "within the time allowed" includes the last day allowed (and see F-7: a refusal counts at any time) [fork F-4] |
| s15 | section | 697-698, 700-706 | Obstructing Commissioner or investigator in exec... | encoded | `s 15 the person is guilty of an offence`; `s 15 the greatest penalty`; `s 15 the sentence is within the greatest penalty`; `ss 8(6), 9(7), 11(1), 14(4) and 15 the greatest penalty for the offence` |
| s16 | section | 708 | Offences by bodies corporate, etc. | inert (reason 1) | `/` - section heading |
| s16(1) | subsection | 710-711 | 16.—(1) Where an offence under this Act committe... | encoded | `s 16(1) the officer is guilty of the offence as well as the body corporate` |
| s16(1)(a) | paragraph | 713-714 | (a) to have been committed with the consent or c... | encoded | `s 16(1) the officer is guilty of the offence as well as the body corporate` |
| s16(1)(b) | paragraph | 716 | (b) to be attributable to any neglect on the off... | encoded | `s 16(1) the officer is guilty of the offence as well as the body corporate` |
| s16(1)-tail | subsection tail | 718-719 | the officer as well as the body corporate shall ... | encoded | `s 16(1) the officer is guilty of the offence as well as the body corporate` |
| s16(2) | subsection | 721-722, 727-728 | (2) Where the affairs of a body corporate are ma... | encoded | `s 16(2) section 16(1) applies to the member as if the member were a director` |
| s16(3) | subsection | 730-731 | (3) Where an offence under this Act committed by... | encoded | `s 16(3) the partner is guilty of the offence as well as the partnership` |
| s16(3)(a) | paragraph | 733-734 | (a) to have been committed with the consent or c... | encoded | `s 16(3) the partner is guilty of the offence as well as the partnership` |
| s16(3)(b) | paragraph | 736 | (b) to be attributable to any neglect on the par... | encoded | `s 16(3) the partner is guilty of the offence as well as the partnership` |
| s16(3)-tail | subsection tail | 738-739 | the partner as well as the partnership shall be ... | encoded | `s 16(3) the partner is guilty of the offence as well as the partnership` |
| s16(4) | subsection | 741-742 | (4) Where an offence under this Act committed by... | encoded | `s 16(4) the officer or member is guilty of the offence as well as the unincorporated association` |
| s16(4)(a) | paragraph | 744-746 | (a) to have been committed with the consent or c... | encoded | `s 16(4) the officer or member is guilty of the offence as well as the unincorporated association` |
| s16(4)(b) | paragraph | 748-749 | (b) to be attributable to any neglect on the par... | encoded | `s 16(4) the officer or member is guilty of the offence as well as the unincorporated association` |
| s16(4)-tail | subsection tail | 751-753 | the officer or member as well as the unincorpora... | encoded | `s 16(4) the officer or member is guilty of the offence as well as the unincorporated association` |
| s16(5) | subsection | 755 | (5) In this section — | inert (reason 1) | lead-in to the definitions that follow ("In this section —") |
| s16(5):body corporate | defined term | 757-759 | “body corporate” includes a limited liability pa... | encoded | `s 16(5) the entity is a body corporate` - "includes": another kind of entity is not answered |
| s16(5):officer | defined term | 761 | “officer” — | fork | `s 16(5)(a) the person is an officer of a body corporate`; `s 16(5)(b) the person is an officer of an unincorporated association` - FORK F-8: "means ... and includes" [fork F-8] |
| s16(5):officer(a) | paragraph | 763-767 | (a) in relation to a body corporate, means any d... | fork | `s 16(5)(a) the person is an officer of a body corporate` - FORK F-8 [fork F-8] |
| s16(5):officer(b) | paragraph | 769-772, 777-779 | (b) in relation to an unincorporated association... | fork | `s 16(5)(b) the person is an officer of an unincorporated association` - FORK F-8 [fork F-8] |
| s16(5):partner | defined term | 781 | “partner” includes a person purporting to act as... | encoded | `s 16(5) the person is a partner` |
| s17 | section | 783 | Composition of offences | inert (reason 1) | section heading |
| s17(1) | subsection | 785-789 | 17.—(1) The Board, or an officer or employee of ... | encoded | `s 17(1) the Board or its authorised officer or employee may compound the offence`; `s 17(1) the greatest sum that may be collected`; `s 17(1) the sum collected is within the greatest sum` - Which offences are compoundable is in regulations outside the sources: an input |
| s17(1)(a) | paragraph | 791-792 | (a) one half of the amount of the maximum fine t... | encoded | `s 17(1) the greatest sum that may be collected`; `s 17(1) the sum collected is within the greatest sum` |
| s17(1)(b) | paragraph | 794 | (b) $1,000. | encoded | `s 17(1) the greatest sum that may be collected`; `s 17(1) the sum collected is within the greatest sum` |
| s17(2) | subsection | 796-797 | (2) On payment of the sum of money, no further p... | encoded | `s 17(2) no further proceedings are to be taken against the person in respect of the offence` |
| s17(3) | subsection | 799-800 | (3) All sums collected under this section must b... | encoded | `s 17(3) the sum collected must be paid into the Consolidated Fund`; `s 17(3) duty of the collector` |
| s18 | section | 802, 804-807 | Conduct of prosecutions | encoded | `s 18 the officer or employee may conduct the proceedings` |
| s19 | section | 809 | Protection from personal liability | inert (reason 1) | section heading |
| s19(1) | subsection | 811-814 | 19.—(1) No liability is to lie personally agains... | fork | `s 19 no liability lies personally against the individual` - FORK F-10: the Board and an administrator that is a public authority are not individuals and are not listed [fork F-10] |
| s19(1)(a) | paragraph | 816 | (a) the Commissioner for Silver Support; | encoded | `s 19 no liability lies personally against the individual` |
| s19(1)(b) | paragraph | 818 | (b) any Deputy Commissioner for Silver Support; | encoded | `s 19 no liability lies personally against the individual` |
| s19(1)(c) | paragraph | 820 | (c) any Assistant Commissioner for Silver Suppor... | encoded | `s 19 no liability lies personally against the individual` |
| s19(1)(d) | paragraph | 825-826 | (d) any public officer (or employee of a public ... | encoded | `s 19 no liability lies personally against the individual` |
| s19(1)(e) | paragraph | 828 | (e) any member, officer or employee of the Board... | encoded | `s 19 no liability lies personally against the individual` |
| s19(1)(f) | paragraph | 830 | (f) any investigator. | encoded | `s 19 no liability lies personally against the individual` |
| s19(2) | subsection | 832-836 | (2) Where an administrator is a public officer, ... | encoded | `s 19 no liability lies personally against the individual` |
| s19(3) | subsection | 838-842 | (3) Where an administrator is a public authority... | encoded | `s 19 no liability lies personally against the individual` |
| s19(4) | subsection | 844-846 | (4) To avoid doubt, this section does not exclud... | encoded | `s 19(4) section 19 leaves the liability in place` |
| s20 | section | 848 | Regulations | inert (reason 1) | section heading |
| s20(1) | subsection | 850-851 | 20.—(1) The Minister may make regulations for ca... | encoded | `s 20(1) the Minister may make the regulations` |
| s20(2) | subsection | 853-854 | (2) Without limiting subsection (1), the Ministe... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(a) | paragraph | 856-857 | (a) the benefits under the Scheme, including dif... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(b) | paragraph | 859-860 | (b) the method and manner of disbursing or confe... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(c) | paragraph | 862-863 | (c) the terms and conditions for each benefit un... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(d) | paragraph | 865-867 | (d) the assessment by an administrator of an ind... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(e) | paragraph | 872-874 | (e) the review by the Commissioner of any assess... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(f) | paragraph | 876-879 | (f) how any administrator appointed under sectio... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(g) | paragraph | 881-883 | (g) how any investigator appointed under section... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(h) | paragraph | 885-887 | (h) the fees to be paid for any thing or matter ... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(2)(i) | paragraph | 889-890 | (i) anything that is required or permitted to be... | encoded | `s 20(2) the Minister may make regulations for or with respect to the matter` |
| s20(3) | subsection | 892-895 | (3) The regulations made under this section may ... | encoded | `s 20(3) the greatest penalty a regulation may provide`; `s 20(3) the sentence is within the greatest penalty a regulation may provide` |
| s20(4) | subsection | 897-898 | (4) All regulations made under this section must... | inert (reason 2) | machinery: regulations are presented to Parliament; no right, duty or power of a person in the seat |


## Fork register

**Bench rulings of 2026-11-04** (full text in `docs/ENCODING-GUIDE.md` section 5; they apply to every entry below).
These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23


Every ambiguity the author saw, the readings, the one taken, and the text that licenses it.
A "fork" row in the coverage table points here.
F-1 to F-10 are the rows that carry a fork id; F-11 to F-13 are readings that recur across many rules and are also listed under "Marginal readings for a lawyer"; F-14 is a reading that no input of the encoding carries, so nothing is encoded for it and no coverage row carries its id (the row for s 9(3)(b)(ii) stays `encoded`).

### F-1 What an "eligible individual" is (ss 2, 6(1), 7(1))

- Readings.
  (i) Section 2 says an eligible individual "means an individual who is eligible to receive any benefit under the Scheme", and s 7(1) says "An eligible individual is eligible to receive such benefits", so each defines the other.
  (ii) Section 6(1) is the operative definition ("In this Act, an eligible individual is an individual who"), s 7(1) grants benefits to that status, and the s 2 sentence is the same status in other words.
  (iii) The s 2 definition governs and s 6(1) only supplies conditions for being "eligible to receive".
- Taken: (ii).
  `s 2 the person is an eligible individual` takes the s 7(1) answer as an input and does not decide it a second time; the seat asks s 6(1), then s 7(1).
- Text: lines 104 to 105, 257 to 263, 284 to 285.
- Asserted: `sssa-tests-part1.l4` (the five `s 2 the person is an eligible individual` cases).

### F-2 A month that cannot be ascertained, with the day known (s 6(2)(c), (d))

- Readings.
  The person is born on the 15th of an unknown month.
  (i) The month is deemed January and the ascertained day is kept: 15 January.
  (ii) Both are deemed: 1 January.
- Taken: (i).
  Paragraph (d) deems only the month; paragraph (c) deems the first day only where the day "cannot be ascertained".
- Text: lines 274 to 280.
- Asserted: `sssa-tests-part2.l4` (born 1960, month unknown, day 15: attains on 15 January 2025, and the day before, the day of and the day after).

### F-3 What the closing words of s 14(1)(b) qualify

- Readings.
  The deposited rendering has a second line lettered "(b)" at line 657: "that the Commissioner or investigator (as the case may be) believes on reasonable grounds to be connected with the disbursement or conferment of any benefit under the Scheme; and".
  (i) It is the closing words of paragraph (b), qualifying both (i) "any information within the person's knowledge" and (ii) "any document or record in the person's possession".
  (ii) It qualifies only (ii).
- Taken: (i).
  The reading taken treats line 657 as a continuation of (b): paragraph (b) opens at line 649, no other paragraph (b) follows (a), and (c) follows at line 662.
  The belief is therefore required for information as well as for documents.
- Text: lines 649 to 660.
- Asserted: `sssa-tests-part4.l4` (information and documents without the belief answer `NOTHING`).

### F-4 "Within the time allowed" and the last day (s 14(4))

- Readings.
  A person gives the information on the last day allowed.
  (i) That is within the time.
  (ii) The time is the days before the last day.
- Taken: (i), so 7 days allowed and 7 days counted is in time, and 8 is out of time.
- Text: lines 689 to 695.
- Asserted: day before, day of and day after, in `sssa-tests-part4.l4`, in `sssa-cases-seat.l4`, and in the `#TRACE`s (the stable and main binaries agree that a duty with `WITHIN 7` is fulfilled on day 7 and breached on day 8).

### F-5 As at when a person "has attained 65 years of age" (s 6(1)(b))

- Readings.
  The text does not say as at when the question is asked.
  (i) At the date the question is asked about.
  (ii) At the date a benefit is claimed, or first paid.
- Taken: (i); the caller gives the date asked about.
  No rule of the Act chooses between them, and the seat asks "For which date are you asking?".
- Text: line 261 ("has attained 65 years of age") and the absence of any date.
- Asserted: day before, day of and day after (`sssa-tests-part2.l4`, `sssa-cases-seat.l4`).

### F-6 The two limbs of s 11(1)

- Readings.
  (i) Limbs (a) and (b) are both required, and the intention in (b) is to induce another person to accept "the statement or document" of (a) as genuine.
  (ii) Limb (b) can be met without the false statement or document having been the instrument.
- Taken: (i); the third input of `s 11(1) the person is guilty of an offence` is worded to carry the link.
- Text: lines 570 to 589.
- Asserted: all combinations of the three inputs (`sssa-tests-part4.l4`).

### F-7 A refusal under s 14(4)

- Readings.
  "Refuses or fails, without reasonable excuse, to do so within the time allowed."
  (i) A refusal is an offence at any time, even before the time allowed has run out.
  (ii) Both verbs are governed by "within the time allowed", so nothing is an offence until the time has run out.
- Taken: (i).
  A person who refused is treated as not having complied.
- Text: lines 689 to 693.
- Asserted: refused with 1 of 7 days counted answers `JUST TRUE` (`sssa-tests-part4.l4`, `sssa-cases-seat.l4`).

### F-8 "Officer": "means ... and includes" (s 16(5))

- Readings.
  The definition of "officer" says it "means" a list "and includes any person purporting to act in any such capacity".
  (i) The list is closed by "means", so a person in none of the positions is not an officer (`JUST FALSE`).
  (ii) "Includes" shows the definition is not exhaustive, so the case is not answered (`NOTHING`).
- Taken: (ii); the listed positions and a person purporting to act are `JUST TRUE`, anyone else is `NOTHING`.
- Text: lines 761 to 779.
- Asserted: `sssa-tests-part4.l4`.

### F-9 Whom s 9 applies to (s 9(1))

- Readings.
  "This section applies to" a list of persons.
  (i) The list is closed, so s 9 applies to no one else.
  (ii) The list is not closed with "only", so no answer is given for anyone else.
- Taken: (ii).
- Text: lines 451 to 456.
- Asserted: `sssa-tests-part3.l4` (an investigator and someone else answer `NOTHING`).

### F-10 Who is protected from personal liability (s 19)

- Readings.
  Section 19(1) protects listed "individuals".
  The Board, and an administrator that is a public authority, are bodies and are not listed; their members, officers and employees are (s 19(1)(e), (3)).
  (i) The bodies are outside s 19.
  (ii) They are protected because their people are.
- Taken: (i), answered `NOTHING` (the section is silent about the bodies themselves).
- Text: lines 811 to 842.
- Asserted: `sssa-tests-part4.l4`, `sssa-cases-seat.l4`.

### F-11 "Where" as a condition

- Readings.
  Several provisions begin "Where" (ss 8(1), 8(2), 12, 14(2), 16(1), 16(2), 16(3), 16(4), 19(2), 19(3); checked with a whole-word search of lines 77 to 898).
  (i) "Where" is a condition like "if", and a case outside it is `JUST FALSE`.
  (ii) "Where" introduces the grant, and a case outside it is not answered (`NOTHING`).
- Taken: (ii).
  The brief's list of words that make a failed condition a "no" ("if", "only if", "as long as", "unless", "so long as", "while", "until", "except", "save", "provided that") does not include "where".

### F-12 "Subject to subsection (3)" (s 8(4))

- Readings.
  (i) Where s 8(3) bars the act, the immunity is gone (`JUST FALSE`).
  (ii) Where s 8(3) bars the act, or that is not known, the immunity is not answered (`NOTHING`).
- Taken: (ii); "subject to" limits a grant in its own wording.
- Asserted: `sssa-tests-part3.l4`.

### F-13 "Authorised only if" (s 9(2))

- Readings.
  (i) The purpose test is also sufficient: a use or disclosure for a named purpose is authorised.
  (ii) "Only if" states a necessary condition and nothing more.
- Taken: (ii).
  `s 9(2) the use or disclosure is authorised` answers `JUST FALSE` when no named purpose is present and `NOTHING` otherwise; it never answers `JUST TRUE`.
  `s 9(2) the purpose is one the subsection names` is a plain `BOOLEAN` for the condition alone.
- Asserted: `sssa-tests-part3.l4`, `sssa-cases-seat.l4`.

### F-14 Whether "up to the date on which the report is made" includes that date (s 9(3)(b)(ii))

- Readings.
  The report must state "the description and amount of each benefit that the individual is eligible to receive or has received under the Scheme up to the date on which the report is made".
  (i) "Up to" includes the date on which the report is made: the benefits of that day are in the report.
  (ii) "Up to" stops before it: the benefits of that day are not in the report.
- Taken: neither.
  Nothing is encoded for it: no input is a report date, and nothing is compared with one.
  `s 9(3) the Commissioner, the Board or an administrator may provide the information` takes a single fact, that the report states the description and amount of each benefit up to the date of the report, and the caller settles the reading when answering it.
- Text: lines 487 to 488 and 493 to 494 (page furniture at lines 490 to 491 splits the sentence).
- Asserted: not asserted; no case exercises the date.

## Marginal readings for a lawyer

The brief's rule of 2026-10-29 (assumed, not ruled by a lawyer) is that a `JUST FALSE` is given only where the text itself says no in its own words, and everything else is `NOTHING`.
Two readings are marginal, and each branch that rests on one is listed below with the other reading stated.

- **Reading (a):** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"); flat negatives count as the text saying no.
  A branch resting on it answers `JUST FALSE` (or nil, 0).
  The other reading would answer `NOTHING`.
- **Reading (b):** a prohibition or grant limited by its own wording does not count as the text's no.
  A branch resting on it answers `NOTHING`.
  The other reading would answer `JUST FALSE`.

Not listed, because they are not marginal: definitions that say "means" (a thing outside the definition is `JUST FALSE`), flat ceilings ("a fine not exceeding $5,000": a sentence above it is `JUST FALSE`), and the `NOTHING` kinds that are silent, list not closed, includes, undefined term and points outside the text.
The list below is generated by `marginal.py` (not shipped) from the comments in the code, so it cannot drift from it.

| function | where | reading | words relied on | answer given | the other reading gives |
|---|---|---|---|---|---|
| `s 2 the definitions apply to the term as used` | sssa-part1-preliminary.l4:38 | (a) | unless the context otherwise requires | JUST FALSE | NOTHING |
| `s 6(1)(b) the individual has attained 65 years of age` | sssa-part2-scheme.l4:122 | (a) | an individual attains 65 years of age on the 65th anniversary of the date of that individual’s birth | JUST FALSE | NOTHING |
| `s 6(1) the individual is an eligible individual` | sssa-part2-scheme.l4:145 | (a) | an eligible individual is an individual who — (a) is a citizen of Singapore | JUST FALSE | NOTHING |
| `s 6(1) the individual is an eligible individual` | sssa-part2-scheme.l4:147 | (a) | (b) has attained 65 years of age | JUST FALSE | NOTHING |
| `s 6(1) the individual is an eligible individual` | sssa-part2-scheme.l4:149 | (a) | (c) satisfies all other eligibility criteria that may be prescribed | JUST FALSE | NOTHING |
| `s 7(1) the individual is eligible to receive the benefits that may be prescribed` | sssa-part2-scheme.l4:174 | (b) | An eligible individual | NOTHING | JUST FALSE |
| `s 7(1) the amount of benefit an eligible individual is eligible to receive` | sssa-part2-scheme.l4:191 | (b) | only an eligible individual is given the amounts prescribed | NOTHING | JUST FALSE |
| `s 7(1) the manner in which an eligible individual is to receive the benefit` | sssa-part2-scheme.l4:205 | (b) | only an eligible individual is given the manner prescribed | NOTHING | JUST FALSE |
| `s 8(1)(a) the Minister may direct the department or authority to provide the information` | sssa-part3-administration.l4:68 | (b) | Where the Minister certifies in writing ... so much of the means information as is necessary for that purpose | NOTHING | JUST FALSE |
| `s 8(1)(b) the department or authority must comply with the direction` | sssa-part3-administration.l4:85 | (b) | to comply with the direction under paragraph (a) | NOTHING | JUST FALSE |
| `s 8(2)(a) the Minister may direct the department or authority to provide the information` | sssa-part3-administration.l4:134 | (b) | Where the Minister certifies in writing ... so much of the confidential information as is necessary for that purpose | NOTHING | JUST FALSE |
| `s 8(2)(b) the department or authority must comply with the direction` | sssa-part3-administration.l4:148 | (b) | to comply with the direction under paragraph (a) | NOTHING | JUST FALSE |
| `s 8(3) the authorised person is barred from the act` | sssa-part3-administration.l4:193 | (b) | must not ... (a) access ... (b) use or disclose under section 9 | NOTHING | JUST FALSE |
| `s 8(3) the authorised person is barred from the act` | sssa-part3-administration.l4:195 | (a) | If an individual opts out, in the manner determined by the Commissioner, from the application of subsection (1) | JUST FALSE | NOTHING |
| `s 8(3) the authorised person is barred from the act` | sssa-part3-administration.l4:197 | (a) | except with the consent of that individual | JUST FALSE | NOTHING |
| `s 8(3) the authorised person is barred from the act` | sssa-part3-administration.l4:199 | (b) | from the time an authorised person is notified that the individual has opted out | NOTHING | JUST FALSE |
| `s 8(4)(a) the person is not guilty or liable merely by disclosing in accordance with the direction` | sssa-part3-administration.l4:265 | (b) | by virtue merely of the person disclosing any information in accordance with any direction ... subject to subsection (3) | NOTHING | JUST FALSE |
| `s 8(4)(b) the authorised person is not guilty or liable merely by accessing or disclosing the means information` | sssa-part3-administration.l4:300 | (b) | by virtue merely of ... acting in good faith and with reasonable care ... subject to subsection (3) | NOTHING | JUST FALSE |
| `s 8(4)(c) the officer is not guilty or liable merely by accessing or disclosing the confidential information` | sssa-part3-administration.l4:329 | (b) | by virtue merely of ... acting in good faith and with reasonable care ... subject to subsection (3) | NOTHING | JUST FALSE |
| `s 8(5) the Minister giving the direction may impose terms and conditions regarding access` | sssa-part3-administration.l4:343 | (b) | A direction under subsection (1)(a) or (2)(a) | NOTHING | JUST FALSE |
| `s 8(6) the person is guilty of an offence` | sssa-part3-administration.l4:366 | (b) | any act in contravention of subsection (3) | NOTHING | JUST FALSE |
| `s 9(2) the use or disclosure is authorised` | sssa-part3-administration.l4:525 | (b) | means information obtained under section 8(1) ... confidential information (other than means information) obtained under section 8(2) | NOTHING | JUST FALSE |
| `s 9(2) the use or disclosure is authorised` | sssa-part3-administration.l4:528 | (b) | without the consent of the individual to whom the information relates | NOTHING | JUST FALSE |
| `s 9(2) the use or disclosure is authorised` | sssa-part3-administration.l4:530 | (a) | is authorised only if the purpose of the use or disclosure is to communicate or manage the information as part of | JUST FALSE | NOTHING |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:572 | (b) | the Commissioner, the Board or an administrator | NOTHING | JUST FALSE |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:575 | (b) | information derived from means information obtained under section 8(1), or from confidential information | NOTHING | JUST FALSE |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:578 | (b) | for the development or implementation of any public scheme that may be prescribed for the purposes of this subsection | NOTHING | JUST FALSE |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:580 | (a) | only at the request of the public officer, public authority, person or organisation (as the case may be) | JUST FALSE | NOTHING |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:582 | (a) | with the approval of the Minister | JUST FALSE | NOTHING |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:584 | (a) | only in the form of a report stating | JUST FALSE | NOTHING |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:586 | (a) | whether an individual satisfies the eligibility criteria for receiving any benefit under the Scheme | JUST FALSE | NOTHING |
| `s 9(3) the Commissioner, the Board or an administrator may provide the information` | sssa-part3-administration.l4:588 | (a) | the description and amount of each benefit that the individual is eligible to receive or has received under | JUST FALSE | NOTHING |
| `s 9(4) the Minister may give the approval on terms and conditions regarding access` | sssa-part3-administration.l4:604 | (b) | An approval under subsection (3)(a) | NOTHING | JUST FALSE |
| `s 9(5) the provider is barred from providing the report` | sssa-part3-administration.l4:627 | (b) | the Commissioner, the Board or the administrator (as the case may be) | NOTHING | JUST FALSE |
| `s 9(5) the provider is barred from providing the report` | sssa-part3-administration.l4:630 | (b) | any such report about the individual | NOTHING | JUST FALSE |
| `s 9(5) the provider is barred from providing the report` | sssa-part3-administration.l4:632 | (a) | If an individual opts out, in the manner determined by the Commissioner, from the provision of a report | JUST FALSE | NOTHING |
| `s 9(5) the provider is barred from providing the report` | sssa-part3-administration.l4:634 | (a) | except with the consent of the individual | JUST FALSE | NOTHING |
| `s 9(5) the provider is barred from providing the report` | sssa-part3-administration.l4:636 | (b) | from the time the Commissioner, the Board or an administrator is notified that the individual has opted out | NOTHING | JUST FALSE |
| `s 9(6) the Board may use the information to administer the Scheme` | sssa-part3-administration.l4:682 | (b) | so much of ... as the Minister approves to be used for such purpose | NOTHING | JUST FALSE |
| `s 9(7) the person is guilty of an offence` | sssa-part3-administration.l4:711 | (b) | any act in contravention of subsection (2), (3) or (5) | NOTHING | JUST FALSE |
| `s 10(1) the amount made recoverable as a debt due to the Government` | sssa-part3-administration.l4:757 | (a) | If any benefit under the Scheme is disbursed as a cash grant | JUST FALSE | NOTHING |
| `s 10(1) the amount made recoverable as a debt due to the Government` | sssa-part3-administration.l4:776 | (a) | the amount paid is in excess of the amount the recipient is eligible to receive | JUST FALSE | NOTHING |
| `s 10(2) the amount made recoverable as a debt due to the Government` | sssa-part3-administration.l4:802 | (a) | If any individual (whether or not an eligible individual) obtains any cash grant or other benefit under the Scheme | JUST FALSE | NOTHING |
| `s 10(3) the administrator may recover the amount from the source` | sssa-part3-administration.l4:825 | (b) | An administrator | NOTHING | JUST FALSE |
| `s 10(3) the administrator may recover the amount from the source` | sssa-part3-administration.l4:828 | (b) | the amount due to the Government under subsection (1) or (2) | NOTHING | JUST FALSE |
| `s 11(1) the person is guilty of an offence` | sssa-part4-miscellaneous.l4:51 | (b) | A person | NOTHING | JUST FALSE |
| `s 11(2) the right of recovery under section 10 is unaffected by section 11(1)` | sssa-part4-miscellaneous.l4:89 | (b) | Subsection (1) ... any right of recovery under section 10 | NOTHING | JUST FALSE |
| `s 12 the court may order the person to pay the certified amount to an administrator` | sssa-part4-miscellaneous.l4:117 | (b) | has received ... is convicted of an offence under this Act in connection with | NOTHING | JUST FALSE |
| `s 12 the amount the court may order the person to pay` | sssa-part4-miscellaneous.l4:140 | (b) | the amount certified by the administrator to be recoverable from the person, as at the date of the conviction | NOTHING | JUST FALSE |
| `s 13 the certificate is prima facie evidence of the amount stated` | sssa-part4-miscellaneous.l4:172 | (b) | a certificate purporting to be issued by an administrator certifying | NOTHING | JUST FALSE |
| `s 14(1) the requirer may make the requirement` | sssa-part4-miscellaneous.l4:234 | (b) | for the purpose of reviewing the administration of the Scheme or the disbursement or conferment of any benefit ... for the purpose of conducting any investigation under this Act ... by written notice  | NOTHING | JUST FALSE |
| `s 14(2)(a) the power to require production includes the power to require it in legible form` | sssa-part4-miscellaneous.l4:261 | (b) | required by the Commissioner or an investigator ... is kept in electronic form ... produced for inspection | NOTHING | JUST FALSE |
| `s 14(2)(b) section 14(1)(c) applies to the copy` | sssa-part4-miscellaneous.l4:274 | (b) | any copy of that document or record so made available | NOTHING | JUST FALSE |
| `s 14(3) the copy or extract is admissible as evidence` | sssa-part4-miscellaneous.l4:294 | (b) | made under subsection (1)(c) and certified as such by the Commissioner or an investigator ... in any proceedings under this Act | NOTHING | JUST FALSE |
| `s 14(4) the person is within the time allowed` | sssa-part4-miscellaneous.l4:315 | (a) | within the time allowed by the Commissioner or investigator | JUST FALSE | NOTHING |
| `s 14(4) the person is guilty of an offence` | sssa-part4-miscellaneous.l4:340 | (b) | required by the Commissioner or an investigator under subsection (1)(b) ... refuses or fails, without reasonable excuse, to do so within the time allowed | NOTHING | JUST FALSE |
| `s 15 the person is guilty of an offence` | sssa-part4-miscellaneous.l4:429 | (b) | the Commissioner or an investigator ... without reasonable excuse | NOTHING | JUST FALSE |
| `s 16(1) the officer is guilty of the offence as well as the body corporate` | sssa-part4-miscellaneous.l4:641 | (b) | is proved ... the consent or connivance of an officer ... neglect | NOTHING | JUST FALSE |
| `s 16(2) section 16(1) applies to the member as if the member were a director` | sssa-part4-miscellaneous.l4:659 | (b) | affairs ... are managed by its members ... in connection with the member’s functions of management | NOTHING | JUST FALSE |
| `s 16(3) the partner is guilty of the offence as well as the partnership` | sssa-part4-miscellaneous.l4:683 | (b) | is proved ... the consent or connivance of a partner ... neglect | NOTHING | JUST FALSE |
| `s 16(4) the officer or member is guilty of the offence as well as the unincorporated association` | sssa-part4-miscellaneous.l4:712 | (b) | is proved ... the consent or connivance of an officer of the unincorporated association or a member of its governing body ... neglect | NOTHING | JUST FALSE |
| `s 17(1) the Board or its authorised officer or employee may compound the offence` | sssa-part4-miscellaneous.l4:739 | (b) | The Board, or an officer or employee of the Board who is authorised by the Board in writing | NOTHING | JUST FALSE |
| `s 17(1) the Board or its authorised officer or employee may compound the offence` | sssa-part4-miscellaneous.l4:742 | (b) | from a person reasonably suspected of having committed the offence | NOTHING | JUST FALSE |
| `s 17(2) no further proceedings are to be taken against the person in respect of the offence` | sssa-part4-miscellaneous.l4:791 | (b) | On payment of the sum of money | NOTHING | JUST FALSE |
| `s 17(3) the sum collected must be paid into the Consolidated Fund` | sssa-part4-miscellaneous.l4:803 | (b) | All sums collected under this section | NOTHING | JUST FALSE |
| `s 18 the officer or employee may conduct the proceedings` | sssa-part4-miscellaneous.l4:838 | (b) | may, with the authorisation of the Public Prosecutor, be conducted by an officer or employee of the Board who is authorised by the Board in writing | NOTHING | JUST FALSE |
| `s 19 no liability lies personally against the individual` | sssa-part4-miscellaneous.l4:881 | (b) | who, acting in good faith and with reasonable care, does or omits to do anything in the execution or purported execution of this Act | NOTHING | JUST FALSE |
| `s 20(1) the Minister may make the regulations` | sssa-part4-miscellaneous.l4:923 | (b) | for carrying out the purposes and provisions of this Act | NOTHING | JUST FALSE |

19 branches rest on reading (a), 49 on reading (b).


### Reading a result: FALSE and NOTHING

- `JUST TRUE` and `JUST FALSE` are answers the Act itself gives.
- `NOTHING` means the text does not answer on these facts.
  It is never "no".
  A caller must never turn `NOTHING` into `FALSE`.
- Every function name carries the section it encodes and claims no more than the section says.
  Examples: `s 7(1) the individual is eligible to receive the benefits that may be prescribed` answers `NOTHING` for a person who is not an eligible individual, because the grant is to "An eligible individual" and the section does not say others receive nothing.
  `s 9(2) the use or disclosure is authorised` never answers `JUST TRUE`, because "authorised only if" does not say the use is authorised once the purpose test is met.
  `s 14(4) the person is guilty of an offence` answers `JUST TRUE` or `NOTHING`: an unmet element says nothing about any other offence.
- Offences (ss 8(6), 9(7), 11(1), 14(4), 15, 16) answer `JUST TRUE` or `NOTHING`, never "not guilty".
- A money result is a number or `MAYBE NUMBER`.
  A nil (0) is given only where the text says no in its own words ("If any benefit ... is disbursed as a cash grant") and is listed above as reading (a).
- Every `JUST FALSE` that is an answer of the law has a comment `-- FALSE-kind (the text says no in its own words): "..."` and every `NOTHING` that is an answer of the law has `-- NOTHING-kind (<why>)`, where the reason is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
  `kinds.py` (not shipped) checks that each comment is present, that each quoted phrase (including those in `NOTHING-kind` comments) is a verbatim substring of the deposited text, and that the reason is one of the six.
  The seat's wiring lines that map a person's "I am not sure" or 0 onto a `MAYBE` input of a rule are marked `-- input mapping`; `kinds.py` skips them, because they are not answers of the law.
- In the seat, "I am not sure" and a 0 for an unknown date or amount become `NOTHING`, and a rule that cannot answer without it answers `NOTHING`.
- An unknown answers `NOTHING` only when the answer turns on it: an arm that returns `NOTHING` for an unknown input must come after every arm that decides the answer without that input.
  Swept 2026-11-04 over the 24 functions in the four rule modules that take a `MAYBE` input (directly, or as a field of `Birth facts`), and over the seat.
  Twelve arms answer `NOTHING` because an input is unknown (6 written `EQUALS NOTHING THEN NOTHING`, 6 written `WHEN NOTHING THEN NOTHING`; 9 functions).
  One function had the defect and is fixed: `s 10(1)`, whose arm for an unknown status stood ahead of the arm for a recipient known not to be eligible for the cash grant.
  Clean: `s 2 the person is an eligible individual`, `s 6(1)` and `s 9(3)`, which have an unknown-input `NOTHING` arm and also decide `JUST FALSE` from other facts, and in each the `NOTHING` arm follows every arm that decides without it (asserted for `s 6(1)` and `s 9(3)`: an unknown with another limb failing answers `JUST FALSE`); `s 2` Board, `s 2` permanent resident, `s 6(2)(a)`, `s 6(1)(b)` and `s 7(1)` (three functions), where the unknown is the only thing the answer turns on, or is passed on.
  Not subject to it: `s 6(2)(c)` and `(d)`, which absorb the unknown as the text deems; and 11 functions (`s 8(1)(a)`, `s 8(4)(a)`, `(b)`, `(c)`, `s 8(6)`, `s 9(7)`, `s 10(3)`, `s 12`, `s 16(3)`, `s 16(4)`, `s 17(1)`) that answer `JUST TRUE` or a number from a `MAYBE` input, or else `NOTHING`, so no determinate answer stands behind the unknown.
  The seat's wiring turns "I am not sure" and 0 into `NOTHING` and passes it to layer 1, and no seat question has an arm of its own that tests an unknown ahead of another.
  The one residue is stated under finding 12: a nil eligible amount makes an unknown status or entitlement irrelevant in `s 10(1)` by arithmetic, and the function does not see it.

## What the text turns out to say

Findings from encoding and testing.
Each ends "Asserted." where a case or test asserts it, and says so where it does not.

1. **A 29 February birth reaches 65 on 1 March.**
   Section 6(2)(b) deems the 65th anniversary to occur on 1 March.
   Adding 65 years to the date with the `l4` library function `add years` clamps 29 February to 28 February, a day early, which would make a person born on 29 February 1960 eligible on 28 February 2025.
   The encoding builds the anniversary from its components instead.
   Asserted (`sssa-tests-part2.l4`, `sssa-cases-seat.l4`: 28 February 2025 is `JUST FALSE`, 1 March 2025 is `JUST TRUE`).
2. **Sixty-five years after a leap year is never a leap year,** so a 29 February birth always falls under s 6(2)(b): born 29 February 1996, the date is 1 March 2061; born 29 February 2000 (a century leap year), 1 March 2065.
   Asserted.
3. **An unknown day is the 1st; an unknown month is January.**
   Both unknown is 1 January.
   Asserted.
4. **A year of birth that cannot be ascertained is not covered.**
   Section 6(2) deems a month and a day and says nothing of a year, so the date of attaining 65 is `NOTHING`, and so is eligibility unless another limb already answers `JUST FALSE`.
   Asserted.
5. **The Act alone cannot answer "am I eligible?"**
   Limb (c) of s 6(1) and the benefits, amounts and manner of s 7 are in regulations.
   With every limb the Act states met and the prescribed criteria not known, the answer is `NOTHING`.
   Asserted (`sssa-cases-seat.l4`).
6. **Sections 2, 6(1) and 7(1) define eligibility in a circle** (fork F-1).
   Asserted (`sssa-tests-part1.l4`).
7. **Section 7(1) does not say a person who is not an eligible individual gets nothing.**
   The question "am I eligible to receive benefits?" answers `NOTHING` for such a person, not `JUST FALSE`.
   Asserted.
8. **The Act does not say when payment is made, or when it stops or is withdrawn.**
   Manner and terms are left to regulations (s 7(1), s 20(2)(b), (c)).
   The question on how and when payment is made answers `NOTHING` for everyone, the two questions on a change of circumstances (whether the benefit stops; whether the person must tell the authorities) answer `NOTHING` whatever has changed, and the question whether regulations may deal with the terms answers `JUST TRUE` (the Minister may; the Act does not say what they provide).
   Asserted.
9. **The opt-out bar runs from notice.**
   Under s 8(3) and s 9(5) the bar starts "from the time" the authorised person (or the Commissioner, the Board or the administrator) is notified.
   Before notice, the text is silent, so the answer is `NOTHING`; an individual who did not opt out, or who consents, gets `JUST FALSE` (the bar does not apply).
   Asserted.
10. **Section 9(2) is a necessary condition only** (fork F-13), so a use for a named purpose is `NOTHING`, not authorised, and a use for no named purpose is `JUST FALSE`.
    Asserted.
11. **Section 9(3) has three kinds of limit.**
    A provider who is not the Commissioner, the Board or an administrator, or information that is not derived from s 8 information, or a scheme that is not prescribed, is outside the grant (`NOTHING`); a missing request, approval or report form is a failed "only" limb (`JUST FALSE`), and that answer holds even where the scheme is not known.
    Asserted.
12. **Section 10(1) makes the whole amount recoverable when (a) applies and only the excess when (b) alone applies.**
    The result is the amount made recoverable by the subsection; nil means the subsection makes nothing recoverable, not that nothing is owed.
    Asserted.
    **An unknown status does not block an answer that does not need it** (changed 2026-11-04 after the independent test pass, which found the defect).
    A recipient known not to be eligible for that cash grant owes the whole amount paid whether or not the recipient is an eligible individual: if not, limb (a)(i) ("is not an eligible individual") applies, and if so, limb (a)(ii) ("is an eligible individual, but is not eligible for that cash grant") does, and the text makes "the amount paid" recoverable under either.
    So `s 10(1) ...` answers `JUST` the amount paid when the entitlement is `JUST FALSE`, whatever the status (status unknown, entitlement known false, 1000 paid: `JUST 1000`).
    It answers `NOTHING` when the status is unknown and the entitlement is known true or unknown too: limb (a) would give the whole amount paid and limb (b) only the excess (1000 paid and 800 eligible gives 1000 or 200), and the text says only "the amount paid or paid in excess (as the case may be)", so the text does not say which.
    Asserted (`sssa-tests-part3.l4`, `sssa-cases-seat.l4`); no earlier expected value changed.
    **Not handled, and not changed:** where the amount the recipient is eligible to receive is known to be nil (`JUST 0`) every route gives the whole amount paid, so an unknown status or entitlement is irrelevant there too; the function still answers `NOTHING` for such an unknown, because that is an arithmetic coincidence and not an arm of the text.
    The seat cannot reach it, which turns a stated 0 into "not known".
13. **Section 10(2) is wider than s 10(1):** it reaches any "cash grant or other benefit", and an individual "whether or not an eligible individual".
    The encoding takes the amount obtained as an input and does not distinguish cash from other benefits.
    Asserted for the amount; the cash/other distinction is not separately asserted.
14. **The deposited text has no limitation period and no interest for the recovery in s 10.**
    The words `limitation` and `interest` do not occur in the body of the Act (a whole-word search of lines 77 to 898).
    Not asserted: the absence of a provision is not a case.
15. **An offence is never answered "not guilty".**
    Offences answer `JUST TRUE` when every element is met and `NOTHING` otherwise.
    Asserted.
16. **Obstruction (s 15) carries the heaviest fine ceiling, $20,000 (with imprisonment up to 12 months),** four times that of s 8(6), s 9(7) and s 11(1) ($5,000 or 12 months) and twice that of s 14(4) ($10,000 or 6 months).
    Asserted.
17. **A compounded sum is capped at $1,000 for every offence of this Act.**
    The cap is the lower of half the maximum fine and $1,000; every offence in the Act has a maximum fine of $5,000 or more, so half is $2,500 or more and the lower is $1,000.
    The half-fine limb bites only below a maximum fine of $2,000 (for example $1,500 gives $750).
    Which offences may be compounded is for regulations.
    Asserted (layer 1 for the arithmetic, the seat for the offences).
18. **After payment of a compounded sum, no further proceedings** (s 17(2)); the sum must be paid into the Consolidated Fund (s 17(3)) with no time limit in the text.
    Asserted for the decision function; the duty is traced.
19. **The certificate in s 13 is only prima facie evidence:** it can be rebutted.
    Asserted.
20. **Section 19 protects individuals, and not the bodies** (fork F-10); s 19(4) preserves liability under s 8(6), s 9(7) and s 20 of the Financial Procedure Act 1966.
    Asserted.
21. **The seat has no question on s 9(3), s 9(4), s 9(6) or s 8(4)(b) and (c).**
    The facts they turn on (a Minister's approval, an officer's good faith and care) are not ones the person can state.
    They are encoded and tested in layer 1.
    Not asserted at the seat.
22. **The deposited rendering carries page furniture,** a running header and footer on each page (for example "Informal Consolidation – version in force from 1/12/2025" and "2020 Ed. Silver Support Scheme Act 2015 N"), which the coverage table lists as the `furniture` unit and which splits some sentences across pages (for example s 8(1) at lines 298 to 306).
    Not asserted.
23. **The arrangement of sections is mis-aligned by the converter:** lines 26 to 31 pair the numbers 1 to 4 with the wrong titles.
    The section headings in the body are taken as authoritative.
    Not asserted.
24. **No function checks the date asked about against a commencement date, so an answer for a date before commencement is not meaningful.**
    The commencement note reads "[18 January 2016: Except sections 6 and 7 ; 22 July 2016: Sections 6 and 7 ]" (lines 74 to 75), and Part 1 of the encoding treats it as machinery (coverage row `commencement-note`, inert).
    The only functions that take a date are `s 6(1)(b) the individual has attained 65 years of age` and `s 6(1) the individual is an eligible individual` (the date asked about, fork F-5), and the five seat questions that ask for it; every other function takes no date at all, so cannot be asked a question about a date.
    They compare the date only with the 65th anniversary of the birth.
    Measured 2026-11-04 on the stable build: `s 6(1)` answers `JUST TRUE` for a citizen born 15 March 1940 who meets the other criteria, asked about 21 July 2016, a day before s 6 and s 7 commenced on 22 July 2016, and for the same person asked about 17 January 2016, before the rest of the Act commenced on 18 January 2016.
    An answer for a date before 22 July 2016 (ss 6 and 7) or before 18 January 2016 (every other section) is not meaningful: the provision was not in force.
    A caller must not ask about such a date.
    No commencement model is added.
    Not asserted: an expected value for a date before commencement would bless a meaningless answer.

## What the stable binary does not accept

Observed with `l4-stable-98` (1.6.98) while writing this encoding:

- A vertical `LIST` of records written as `` `Class amount` OF "a", 1 `` on one line, with the next entry introduced by a leading comma, is a parse error: "incorrect indentation (got 9, should be greater than 9)".
  Each record must be wrapped in parentheses: `(`Class amount` OF "a", 1)`, with the comma at the left of the second entry.
- ``JUST (f x)'s field`` (a possessive after a parenthesised application, inside `JUST`, with backticked names) was a parse error: `unexpected (`, pointing at the opening bracket after `JUST`.
  Binding the application in a `WHERE` and taking the field from the bound name parses (`sssa-seat.l4`, the s 17(1) question).
- `add years` on a `DATE` clamps 29 February to 28 February (see finding 1).
  It is accepted and gives a wrong answer for s 6(2)(b); the anniversary is built from components instead.
- A `DEONTIC` result cannot be compared: `#ASSERT rule EQUALS FULFILLED` fails with "Trying to check equality on types that do not support it", so no assertion can be written on a rule's result.
  A `#TRACE` prints FULFILLED, `DEONTIC BREACHED` or a residual `PARTY ... MUST` and no assertion line, so `check.sh` counts nothing for it.
  `traces.py` reads the printed result and compares it with the `-- EXPECT` comment; each duty is also encoded as a decision function that carries assertions.

Taken from the brief, not re-probed here: section-level `GIVEN` is rejected on main; `YMD` and `YearMonthDay` are not defined (use `Date day month year`); `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (except `LEST BREACH ... BECAUSE`) are not available; `WAIT UNTIL` is `WAITUNTIL`; `TYPICALLY` on a record field is not accepted; a bullet in a list is a parse error.

## What `check.sh` prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sssa-cases-seat.l4                             0       148       0        0         0 |      0       148       0        0  same
sssa-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
sssa-part1-preliminary.l4                      0         0       0        0         0 |      0         0       0        0  same
sssa-part2-scheme.l4                           0         0       0        0         0 |      0         0       0        0  same
sssa-part3-administration.l4                   0         0       0        0         0 |      0         0       0        0  same
sssa-part4-miscellaneous.l4                    0         0       0        0         0 |      0         0       0        0  same
sssa-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sssa-tests-part1.l4                            0        49       0        0         0 |      0        49       0        0  same
sssa-tests-part2.l4                            0        79       0        0         0 |      0        79       0        0  same
sssa-tests-part3.l4                            0       225       0        0         0 |      0       225       0        0  same
sssa-tests-part4.l4                            0       246       0        0         0 |      0       246       0        0  same
TOTAL (11 modules)                             0       747       0        0           |      0       747       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Exit status of `check.sh`: 0.


The other gates, run from this folder (all exit 0):

```
$ python3 -I srcrefs.py check --refs ../../../inputs/SSSA2015.txt <all sssa-*.l4>
srcrefs check: 700 src: lines, 99 runs, 103 locators, 0 problems
(exit 0)

$ python3 -I srcrefs.py check --strict ../../../inputs/SSSA2015.txt <all sssa-*.l4>
srcrefs check: 700 src: lines, 99 runs, 103 locators, 0 problems
(exit 0)

$ python3 -I kinds.py ../../../inputs/SSSA2015.txt <layer-1 modules, seat>
kinds check: 37 FALSE-kind answers, 82 NOTHING-kind answers, 138 quoted phrases verified, 0 problems
(exit 0)

$ python3 -I coverage.py check ../../../inputs/SSSA2015.txt coverage-map.txt <all .l4>
lines: 684 non-blank, 684 assigned; units: 199; dispositions: encoded=141, fork=11, inert=47; problems: 0
(exit 0)

$ python3 -I traces.py l4-stable-98 <modules with #TRACE>
traces check: 17 traces, 17 matched, 0 problems
(exit 0)

$ python3 -I traces.py l4-main-108 <modules with #TRACE>
traces check: 17 traces, 17 matched, 0 problems
(exit 0)

$ python3 -I seatcheck.py sssa-seat.l4 sssa-cases-seat.l4
seat check: 33 questions, 0 problems
(exit 0)
```

What `check.sh` does not see, and what covers it here: a `#TRACE` outcome (read by `traces.py` on both builds), a citation that points at the wrong provision (not checked by anything: `srcrefs.py` checks that a locator lies inside the quoted lines, not that it names the right provision), and any difference no assertion exercises.


The baseline numbers this replaced: none (a fresh encoding).

## Before this encoding is relied on

- A lawyer must read it against the official text of the Act.
  Nothing here has been compared with the official text.
- Read the fork register (F-1 to F-14) and the list of marginal readings, and rule on them; the readings taken are the author's, and the FALSE/NOTHING rule is itself assumed, not ruled.
- Obtain the regulations made under the Act (the criteria, benefits, amounts and manner under ss 6(1)(c), 7 and 20; the public schemes prescribed for s 9(3); the offences prescribed as compoundable for s 17(1)), put them in as sources, and replace the inputs with rules.
  Until then no answer to "am I eligible?" or "how much?" can come from this encoding alone.
- Check the borrowed terms against their own instruments: the Central Provident Fund Act 1953, the Financial Procedure Act 1966 (s 20), the Immigration Act 1959 (permanent resident), the Limited Liability Partnerships Act 2005 (s 2(1)).
- Compare the deposited text with the current Singapore Statutes Online version; the deposited rendering is of the version in force from 1 December 2025, and the metadata says "Current version as at 01 Oct 2026".
- Decide, with a lawyer, whether the seat's `Yes / No / I am not sure` inputs should be asked as they are.
- Deploy the seat only after a person with Legalese Cloud access has read the `@desc` wording; changing a question's inputs is a breaking change.
- If the encoding is to be read by `unstable` as well, run `check.sh` with `L4_TARGET=unstable` and compare `#TRACE` outcomes by hand (this has not been done).

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage-map.txt`, `coverage.py`, `expand-quotes.py`, `kinds.py`, `marginal.py`, `seatcheck.py`, `traces.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated or checked a module, the module in this folder is the file to edit.
The commands in this file that run one of them (`python3 -I coverage.py ...` and the like) cannot be run from this folder; `check.sh` and `srcrefs.py` can.
The lead keeps the scripts outside this repository.

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, brief or tests wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 478 numbered scenarios (items 1 to 461 before it opened any module; items 462 to 478 are a second addendum written afterwards, with expected values taken from the text) and 90 seat scenarios (S1 to S90).
It then wrote `tests-independent.l4`: 457 assertions, covering 305 of the 478 numbered scenarios and all 90 seat scenarios, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the numbers in the comments of `tests-independent.l4` refer to it.
The author's rules for "no" and "not covered" are in its `ANSWERS.md` (R1 to R6); its R3 counts a failed condition introduced by `if`, `where`, `only if`, `unless` or a stated manner as a plain no, which is wider than the family's rule (see "Reading a result: FALSE and NOTHING" above).

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as first deposited | 457 | 382 | 75 | 0 |
| after the encoder's repair of s 10(1), before the reconciliation below | 457 | 383 | 74 | 0 |
| after the reconciliation below | 456 | 456 | 0 | 0 |

**What the 75 first-run failures turned out to be.**

- **One was an encoder defect, repaired; the author's assertion stands unchanged (scenario 478, s 10(1)).**
  With the recipient's status as an eligible individual unknown, the recipient known not to be eligible for that cash grant, and 1000 paid, limbs (a)(i) and (a)(ii) each make the whole 1000 recoverable, so the answer is `JUST 1000`; the encoding tested "status unknown" before "known not eligible" and answered `NOTHING`.
  The encoder moved one arm and swept the 24 functions that take a `MAYBE` input for the same shape: one defect and no other (finding 12 lists one residue, left unchanged).
- **One is a limit, kept as a `-- GAP` line and not asserted (scenario 117, s 6(1)).**
  A citizen aged 76 asked about 21 July 2016, before s 6 commenced on 22 July 2016, gets `JUST TRUE`, and the author expected `JUST FALSE`.
  No module models commencement (finding 24); no assertion blesses the answer.
- **Three were a genuine fork, reconciled to the encoding's answer (226, 227 and seat S31, s 9(2)).**
  "Is authorised only if the purpose … is to communicate or manage the information as part of the administration or enforcement of this Act or of the Scheme" is read by the encoding as a necessary condition only (fork F-13), so a lawful purpose answers `NOTHING` and `s 9(2) the use or disclosure is authorised` never answers `JUST TRUE`; the author read the subsection as the grant as well and expected `JUST TRUE`.
  The negative limb agrees (225, 228 and S30 all answer `JUST FALSE` for a purpose outside the Act and the Scheme).
  **Which reading is right is for a lawyer.**
- **Three were the author's own scenarios, reconciled with the reason in the file (171, 173 and 375).**
  171 and 173 (s 8(1)(a) and s 8(2)(a) asked about the kind of information the paragraph does not address) were marked weakly held by the author, whose rule R4 gives "not covered".
  375 (s 16(5), "'body corporate' includes a limited liability partnership") was conceded by the author: "includes" extends the ordinary meaning, so an ordinary body corporate is a body corporate.
- **Sixty-seven were one convention disagreement, reconciled to the encoding's `NOTHING` (the author's finding 2A).**
  On a condition phrased "where", "who", "acting in good faith", "that is prescribed", "subject to", "from the time" or a stated manner ("in writing", "reasonable time"), the author wrote `JUST FALSE` when the condition fails; the encoding writes `NOTHING`, because those words are not in the family's list of words that make a failed condition the text's no.
  They are the failures at s 8(1), 8(3) and 8(4), s 9, ss 11 and 12, s 14 (and the offence element at 14(4)), s 15, s 16, s 17, s 18, s 19 and 256 of the author's list, with their seat counterparts, and each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote.
  The author did not think the encoding wrong under the family's rule; its view was that these are conditionals in plain English, so a failed one makes the provision not apply.
  **These are the first thing for a lawyer to look at, together with the three s 9(2) assertions above:** if those words do close a case, the encoding says "the Act does not say" in 70 places where a reader would say "no".
  This is the second of the two readings that the 2026-10-29 rule leaves for a lawyer (a prohibition or grant limited by its own wording is not counted as the text's no); no ruling has been made.

**The gaps.**
173 of the 478 numbered scenarios have no assertion, each kept as a `-- GAP` line at the end of the file in the author's words (about 17 of them repeat a call the author had already asserted).
By the author's grouping: commencement and revision (1 to 30 and 87); s 4 (71 to 86); s 5(2) to (8) (89 to 111); period counting and time of day (125, 136, 147 to 152, 349), where the Act has no rule and the right answer is "not covered" but no function can be asked; repeal, re-enactment, cross-references and silence (444 to 459, with s 20(3) and (4)); and questions for which a function exists but has no input for the distinguishing fact (who acts, a moment in time, whether a person gave consent, an intent, a minimum penalty, a retention period, and so on).
Every one of the 90 seat questions has at least one assertion.

**What the author could not decide from the text** (for comparison with the fork register above): the positive limb of s 9(2); whether the date in s 9(3)(b)(ii) is included (the encoder had not registered this; F-14 now does, with nothing encoded); what "wef 31/12/2024" and "wef 01/12/2025" say about the days before; whether the Board is a "public authority" (the encoding asks it as a fact); whether each body in s 9(5) is barred only from when that body is notified; and whether a Deputy Commissioner is "responsible for administration" under s 4(3) and (4).

**Independence, as far as it went.**
The author did not open `NOTES.md` or `PROGRESS.md`.
After it had written `ANSWERS.md` it read all six `.l4` modules in full, including their header comments, which name forks F-1 to F-4 and the "marginal readings (a) and (b)", and the two skill files for the `#ASSERT` syntax and the diagnostic shapes; it created and deleted two scratch files in its copy.
A process listing it ran at the end printed another run's command line, naming a different run's directory; it did not open that directory.
Scenarios 462 to 478 were written after it had read the modules.
The encoder was given the author's findings 478, 117 and the missed s 9(3)(b)(ii) fork after the author's report (and not the 67 or the s 9(2) disagreement), repaired or recorded them, and reran everything.
