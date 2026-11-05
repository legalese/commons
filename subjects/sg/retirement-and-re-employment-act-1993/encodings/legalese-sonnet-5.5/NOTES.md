# Retirement and Re-employment Act 1993 (Singapore), 2020 Revised Edition -- encoding `legalese-sonnet-5.5`

Status: draft.
Target compiler: `main` (l4 1.6.109, main, 4c887e0, 2026-11-04), compared by `check.sh` with 1.6.108 (main, 2ae7c9b, 2026-11-02).
`not_reviewed`: no domain expert has read this encoding against the text.
The text is `RRA1993.txt`, a plain-text rendering made by a converter script from the informal consolidation "version in force from 1/7/2022"; it is not the official text, and nothing here is "verified against the official text".
Method: one Sonnet 5.5 agent working alone from the brief.

## Seat

The seat is an employee who is approaching the retirement age, or a worker who has reached it, asking on facts they can state whether they may be dismissed on the ground of age, whether an offer of re-employment is due, on what terms and by when, and what they can do if they think they were dismissed or denied re-employment unlawfully.
The Act is written to that person: sections 4 and 6 protect the employee's retirement age, Part 3 gives the eligible employee a right to be offered re-employment and says on what terms, and Part 4 is the employee's remedies.
Parts of the Act that address only an official (the Minister's delegation, the Commissioner's inquiries, an investigating officer's powers) are encoded in layer 1 for what they decide, and reach the seat only through what they mean to the person.
There is no seat for an official.

Layer 1 is the law, taking nobody's point of view: seven modules, each rule citing its provision with `@ref` and quoting it with `-- src:` lines produced by `srcrefs.py`.
Layer 2 is `rra-seat.l4`, 77 questions with `@export` and `@desc`, and `rra-cases-seat.l4`, 228 assertions, at least one for every question.
The seat calls the layer-1 rules and restates none of them.

## Files

| File | What it holds |
| --- | --- |
| `rra-logic.l4` | no law: the three-valued helpers (`every one of these answers is yes`, `at least one of these answers is yes`, `the opposite of this answer`) and the arithmetic of a penalty's ceilings |
| `rra-nouns.l4` | the parties, the acts the regulative rules name, the `Employment` record, the `Penalty` record and the enumerations the rules take |
| `rra-part1-preliminary.l4` | s 2 (interpretation: every defined term, treated as dismissed, attaining an age) and s 3 |
| `rra-part2-minimum-retirement-age.l4` | s 4 (the prescribed minimum retirement age and the bar on dismissal before it) and s 6 |
| `rra-part3-re-employment.l4` | ss 7 to 7C (eligibility, the offer, the contract, earlier service, the employment assistance payment) |
| `rra-part4-remedies.l4` | ss 8 to 8C (representations to the Minister, notice and mediation, the Tribunal) |
| `rra-part5-general.l4` | ss 9 to 13 (powers, summonses, offences, penalties, composition, exemption, contracting out, guidelines, saving) |
| `rra-tests-part1.l4` to `rra-tests-part5.l4` | the tests of layer 1: branches, both sides of every threshold, and not-covered cases; `rra-tests-part2.l4` also holds the s 2(3) tests |
| `rra-seat.l4`, `rra-cases-seat.l4` | layer 2 |
| `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` | given with the task and unchanged |
| `coverage.py` | the single source of the coverage table and the jural-relations table below (`audit` and `write`) |
| `marginal.py` | writes the list of marginal readings below from the tags in the code |
| `trace-check.py` | holds every `#TRACE` to the outcome written above it (see "What the main binary does not accept") |
| `fillquotes.py` | expands `-- @@QUOTE N-M` placeholders into `-- src:` quote lines by calling `srcrefs.py quote`; every placeholder has been expanded |
| `PROGRESS.md`, `BRIEF.md` | the working notes and a copy of the brief |

## What is encoded and what is not

Every non-blank line of the text falls in a row of the coverage table below, and each row has exactly one disposition.
Encoded: sections 2, 3(2), 4(1) to (3), 6, 7, 7A, 7B, 7C, 8, 8A, 8B, 8C, 9, 9A, 9B, 9C, 10(1) and (2), 11, 11A, 11B and 13, and every defined term of section 2(1).
Inert, reason 1 (not operative): the title and headings, and the running page headers, page numbers and marginal amendment notes of the rendering.
Inert, reason 2 (machinery): section 1 (short title), section 3(1), (3) and (4) (the administration and the Minister's appointments and rules), section 10(3) (regulations prescribing compoundable offences) and section 12 (regulations).
Repealed or blank in this text (reason 3): section 5, section 7A(8), and sections 8D, 8E and 8F.
The legislative history and the comparative table that follow section 13 in the rendering are not part of the Act and are rows of reason 1.
Not encoded because it is not among the sources: the Gazette notifications that fix the ages, the regulations (prescribed forms and manner, limitations, compoundable offences, modifications), the tripartite guidelines, and the Employment Claims Act 2016, the Industrial Relations Act 1960, the Employment Act 1968 and the State Courts Act 1970, which the Act borrows from.
A term borrowed from one of those Acts ("approved mediator", "claim referral certificate", "collective agreement", "mediation request", "salary", "Employment Claims Tribunal") is asked as a fact.
The ages 63 and 68 used in the cases are illustrative inputs; the Act fixes only the ranges 62 to 65 (s 4(1)) and 67 to 70 (s 7A(11)).
The staged Interpretation Act time module (`inputs/DEPENDENCIES.md`) was read and not imported; see fork F3.

## Dependencies

Each entry says what the text borrows or what was staged, where it came from, what the encoding used or took as an input, and why.
Nothing is imported from outside this folder: `IMPORT` finds only modules beside the importing file (and the libraries).

### `sgia-interpretation-time.l4` (Interpretation Act 1965, Singapore): read, not imported

- Where from: staged in `inputs/DEPENDENCIES/sg-interpretation-act/` for this run; Commons path `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4`; blob `fe60ab2c1f2326a5b061e163761bd63e4f47e12a` as stated in `inputs/DEPENDENCIES.md`. The staged copy is that Commons file with a three-line header added at the top (it says where the file came from); `git hash-object` on the staged copy gives `120b41762ec5ed8646817639a43d5d99c57b3c1e`, and on the staged copy with its first three lines removed it gives `fe60ab2c1f2326a5b061e163761bd63e4f47e12a`, the Commons blob (checked by the lead, 2026-11-05).
- What was used: nothing in code. I read the module to see whether it counts the periods this Act sets.
- Why not imported: its header says the Interpretation Act "has NO rule for counting a period of weeks, months or years from a day" and that those cases return `NOTHING`, so importing it would answer `NOTHING` for every month-counted or year-counted period in this Act. It would also need copying into this folder.
- Provisions of this Act that depend on it: the periods counted in months, which are ss 8(1), 8A(1), 8A(2), 8A(3) (six months) and 8B(2), and the periods counted in years, which are ss 7A(6) and 7A(7). They are counted with daydate `add months` and `add years` instead (fork F3, fork F18).

### The Employment Claims Act 2016: taken as named inputs; to fill later

- Where from: not staged. Commons encodes some Acts, but this one is not among the staged files, so this entry is to fill later.
- Borrowing provisions and what the encoding does:
  - s 2(1) "approved mediator", "claim referral certificate" and "mediation request" (lines 115-117, 167-168) "have the meanings given by section 2(1)" of that Act: each is asked as a fact, for example `the person is an approved mediator within the meaning given by section 2(1) of the Employment Claims Act 2016`.
  - s 8A(3) (lines 708-715): a mediation request under section 3(1) for mediation under Part 2, before a claim under section 13; the request and its time are inputs and the six months are counted here.
  - s 8B(7) (lines 826-838): the same request, and a claim for employment assistance payment under section 13, which the Minister may allow; the Minister's allowance is an input.
  - s 8C(1) (lines 913-918): a claim under section 13 once a claim referral certificate is issued; that the certificate was issued is an input.
- Why: the Act's own text is the only source; a term or step defined elsewhere is asked, never reconstructed from memory.

### The Industrial Relations Act 1960: taken as named inputs; to fill later

- Where from: not staged; to fill later.
- Borrowing provisions: s 2(1) "collective agreement" "has the meaning given by" that Act (lines 119-120), asked as a fact; ss 8B(3)(b), 8B(4) and 8C(2)(b) (lines 784-786, 790-793, 935-937) refer to representations to the Minister under its section 35(3), and the fact that they were made is an input to the bars; s 11B (lines 1141-1143) lets regard be had to the guidelines for the purposes of its section 34, and that the purpose is one the section names is an input.
- Why: as above.

### The Employment Act 1968: taken as named inputs; to fill later

- Where from: not staged; to fill later.
- Borrowing provisions: s 2(1) "Commissioner" is the Commissioner for Labour appointed under its section 3(1) (line 123), and s 2(1) "salary" has the meaning given by its section 2(1) (lines 200-201), both asked as facts; s 3(2) (lines 243-250) names the Deputy, Principal Assistant and Assistant Commissioners appointed under it; ss 7B(2) and 7C(6) (lines 485-491, 570-576) reckon earlier service for annual leave under its section 88A(1) and paid sick leave under its section 89(1) and (2), and those two purposes are named in the enumeration `Purpose of reckoning service` without computing either entitlement.
- Why: as above.

### The State Courts Act 1970: taken as a named input; to fill later

- Where from: not staged; to fill later.
- Borrowing provision: s 2(1) "Employment Claims Tribunal" means a Tribunal constituted under its section 4 (lines 155-157), asked as a fact.
- Why: as above.

## Jural relations

One row per provision that creates a relation, from the table in `coverage.py`.
The correlatives are Hohfeld's: a claim is correlative to a duty, a privilege to a no-right, a power to a liability, an immunity to a disability.
The kind is recorded here only; the person-facing answers do not carry it (ruling N2).

<!-- BEGIN jural -->
| Provision | Holder of the right, privilege, power or immunity | Bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2(2) | Employee: immunity | Employer: disability | `s 2(2) the employee is treated as dismissed by the employer` |
| s 3(2) | Deputy and assistant commissioners: power | Persons affected: liability | `s 3(2) the act is deemed to have been duly performed or exercised by the Commissioner` |
| s 4(2) | Employee: claim | Employer: duty | `s 4(2) the employer may dismiss the employee on the ground of age before the prescribed minimum retirement age`; `s 4(2) the employer shall not dismiss the employee on the ground of age before the prescribed minimum retirement age` |
| s 4(3) | State: claim | Employer: duty | `s 4(3) the employer is guilty of an offence`; `s 4(3) the penalty on conviction`; `s 4(3) the sentence is within the penalty` |
| s 6 | Employee: immunity | Employer: disability | `s 6 the term is void`; `s 6 the retirement age that the term leaves standing` |
| s 7(1) | Employee: claim | Employer: duty | `s 7(1) the employee is eligible for re-employment in accordance with section 7A` |
| s 7(1)(b)(ii) | Employee: immunity | Employer: disability | `s 7(1)(b)(ii) the employee counts as assessed by the employer as medically fit to continue working` |
| s 7(2) | Employee: immunity | Employer: liability | `s 7(2) the employee is presumed to be medically fit to continue working` |
| s 7(3) | Employee: claim | Employer: duty | `s 7(3) the employer has complied with the duty to give written notice of the intention not to re-employ`; `s 7(3) the employer must give the employee written notice of the intention not to re-employ` |
| s 7A(1) | Employee: claim | Employer: duty | `s 7A(1) the employer owes the employee an offer of re-employment before the specified age`; `s 7A(1) the last day on which the employer can offer re-employment`; `s 7A(1) the offer of re-employment was made before the employee attained the specified age`; `s 7A(1) the employer's obligation to re-employ the employee is on foot on the date`; `s 7A(1) the employer must offer re-employment before the employee attains the specified age` |
| s 7A(2) effect | Employee: immunity | Employer: disability | `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` |
| s 7A(3) | Employer: privilege | Employee: no-right | `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(a)(i) | Employer: privilege | Employee: no-right | `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(a)(ii) | Employer: power | Employee: liability | `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(b) | Employer: immunity | Employee: disability | `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(4) | Employer: power | Employee: liability | `s 7A(4) the employer has complied with the requirement to enter into a re-employment contract`; `s 7A(4) the job scope and the terms and conditions may vary from the previous contract` |
| s 7A(5) | Employee: claim | Employer: duty | `s 7A(5) the variation is based on a reasonable factor` |
| s 7A(6) | Employee: claim | Employer: duty | `s 7A(6) the period of employment stipulated is not less than one year` |
| s 7A(7) | Employer: privilege | Employee: no-right | `s 7A(7) the period of employment may be for the shorter period` |
| s 7A(9) | Eligible employee and employer: privilege | Each: no-right | `s 7A(9) the eligible employee may retire or be retired` |
| s 7A(10) | Employer: claim | Eligible employee: duty | `s 7A(10) the employee has complied with the duty to give written notice of the intention to retire`; `s 7A(10) the eligible employee must give the employer written notice of the intention to retire` |
| s 7B(1) | Employer: immunity | Employee: disability | `s 7B(1) the previous service is disregarded for the purpose` |
| s 7B(2) | Employee: claim | Employer: duty | `s 7B(2) the previous service is reckoned for the purpose` |
| s 7B(3) | Employee: immunity | Employer: disability | `s 7B(3) the employee's continuity of employment under re-employment is not broken` |
| s 7C(1) | Employer: immunity | Employee: disability | `s 7C(1) section 7A does not apply to the employer` |
| s 7C(2)(a) | Employee: immunity | Employer E1: disability | `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(2)(b) | Employee: claim | Employer E2: duty | `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(2)(c) | Employee: claim | Employer E1: duty | `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(3) | Employer: immunity | Employee: disability | `s 7C(3) the employer is not required to offer an employment assistance payment` |
| s 7C(4) | Employee: claim | Employer: duty | `s 7C(4) the employment assistance payment is made in a form the section names`; `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` |
| s 7C(4)(a) | Employee: claim | Employer: duty | `s 7C(4) the employment assistance payment is made in a form the section names`; `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` |
| s 7C(5) | Employee: claim | Employer: duty | `s 7C(5) the employer has complied with the duty to take the tripartite guidelines into account` |
| s 7C(6) | Employee: claim | Employer E2: duty | `s 7C(6) the service under E1 is reckoned for the purpose` |
| s 7C(7) | Employee, E1 and E2: privilege | Others: no-right | `s 7C(7) the consent form is prima facie proof of the matters mentioned in subsection (1)(b)` |
| s 7C(8) | Employee: claim | Employer E2: duty | `s 7C(8) a reference to the employer in Part 4 or 5 includes E2` |
| s 8(1) | Employee: power | Minister: liability | `s 8(1) the last day on which the employee can make representations to the Minister`; `s 8(1) the employee may make representations in writing to the Minister to be reinstated` |
| s 8(2) | Minister: power | Commissioner: liability | `s 8(2) the Minister may direct the Commissioner in writing to inquire and report` |
| s 8(3) | Minister: power | Employer: liability | `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(3) closing | Minister: claim | Employer: duty | `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(4) | Employee: claim | Minister: duty | `s 8(4) the Minister must have regard to the consideration` |
| s 8(5) | Minister: immunity | Employee: disability | `s 8(5) the decision of the Minister on the representation is final` |
| s 8(6) | Employer: immunity | Employee: disability | `s 8(6) the employee may bring an action for damages in a court in respect of the unlawful dismissal` |
| s 8(7) | State: claim | Employer: duty | `s 8(7) the employer is guilty of an offence`; `s 8(7) the penalty on conviction`; `s 8(7) the sentence is within the penalty` |
| s 8(8) | Employee: claim | Employer: duty | `s 8(8) the amount recoverable by the court as if it were a fine`; `s 8(8) the court may recover the unpaid amount as if it were a fine` |
| s 8(11) | Employee: claim | Employer: duty | `s 8(11) the power exercised by the delegate is deemed to have been exercised by the Minister` |
| s 8A(1) | Commissioner: claim | Employee: duty | `s 8A(1) the last day on which the employee can notify the Commissioner of the re-employment dispute`; `s 8A(1) the employee notified the Commissioner in time`; `s 8A(1) the employee must notify the Commissioner in writing of the re-employment dispute` |
| s 8A(2) | Commissioner: claim | Employee: duty | `s 8A(2) the last day on which the employee can notify the Commissioner of the dismissal`; `s 8A(2) the employee notified the Commissioner in time`; `s 8A(2) the employee must notify the Commissioner in writing of the dismissal` |
| s 8A(3) | Commissioner: claim | Employee: duty | `s 8A(3) the last day on which the employee can submit a mediation request`; `s 8A(3) the employee submitted the mediation request in time`; `s 8A(3) the employee must submit a mediation request to the Commissioner` |
| s 8A(5) | Commissioner: power | Employee and employer: liability | `s 8A(5) the Commissioner may consult, or direct an approved mediator to consult, the employer and employee` |
| s 8B(1) | Employee: power | Minister: liability | `s 8B(1) the employee may make representations in writing to the Minister to be re-employed` |
| s 8B(2) | Minister: claim | Employee: duty | `s 8B(2) the last day on which the employee can make representations to the Minister`; `s 8B(2) the representations were made in time`; `s 8B(2) the employee must make written representations to the Minister within one month after the conclusion of the conciliation` |
| s 8B(3) | Employer: immunity | Employee: disability | `s 8B(3) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(3) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8B(4) | Employer: immunity | Employee: disability | `s 8B(4) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(4) the employee may make representations to the Minister under subsection (1)` |
| s 8B(5) | Minister: power | Commissioner: liability | `s 8B(5) the Minister may direct the Commissioner to inquire and report` |
| s 8B(6) | Minister: power | Employer: liability | `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(6) closing | Minister: claim | Employer: duty | `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(7) | Employee: power | Minister: liability | `s 8B(7) the Minister may allow the employee to submit a mediation request and to lodge a claim for employment assistance payment` |
| s 8B(8) | Minister: claim | Employee: duty | `s 8B(8) the employee submitted the mediation request within the time the Minister determined`; `s 8B(8) the employee must submit the mediation request within the time the Minister determined` |
| s 8B(10) | Employee: claim | Minister: duty | `s 8B(10) the Minister may have regard to the consideration` |
| s 8B(11) | Minister: immunity | Employee: disability | `s 8B(11) the decision of the Minister on the representation is final` |
| s 8B(12) | Employer: immunity | Employee: disability | `s 8B(12) the employee may bring an action for damages in a court in respect of the denial of re-employment or the dismissal` |
| s 8B(13) | State: claim | Employer: duty | `s 8B(13) the employer is guilty of an offence`; `s 8B(13) the penalty on conviction`; `s 8B(13) the sentence is within the penalty` |
| s 8B(14) | Employee: claim | Employer: duty | `s 8B(14) the amount recoverable by the court as if it were a fine`; `s 8B(14) the court may recover the unpaid amount as if it were a fine` |
| s 8B(17) | Employee: claim | Employer: duty | `s 8B(17) the power exercised by the delegate is deemed to have been exercised by the Minister` |
| s 8C(1) | Employee: power | Tribunal: liability | `s 8C(1) the employee may lodge a claim for employment assistance payment with an Employment Claims Tribunal` |
| s 8C(2) | Employer: immunity | Employee: disability | `s 8C(2) the employee may make representations under section 8B(1) in respect of that dismissal`; `s 8C(2) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8C(3) | Employee: claim | Tribunal: duty | `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account`; `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` |
| s 8C(3)(b) | Employee: claim | Tribunal: duty | `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account`; `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` |
| s 9(1) | Commissioner and investigating officers: power | Employer and others: liability | `s 9(1) the person has the power` |
| s 9(1)(b) | Commissioner and investigating officers: claim | Person examined: duty | `s 9(1)(b) the person examined is bound to state truly the facts and circumstances` |
| s 9(1)(c) | Commissioner and investigating officers: claim | Employer: duty | `s 9(1)(c) the Commissioner or investigating officer may require the employer to produce the employee and the documents` |
| s 9(1)(g) | Commissioner and investigating officers: claim | Person required: duty | `s 9(1)(g) the Commissioner or investigating officer may require a person to produce the article` |
| s 9(2) | State: claim | Any person: duty | `s 9(2) the person is guilty of an offence`; `s 9(2) the penalty on conviction`; `s 9(2) the sentence is within the penalty` |
| s 9A(1) | Minister, Commissioner and investigating officers: power | Person summoned: liability | `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(1) summons | Minister, Commissioner and investigating officers: claim | Person summoned: duty | `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(2) | State: claim | Any person: duty | `s 9A(2) the person is guilty of an offence` |
| s 9A(3) | Commissioner and investigating officers: power | Person summoned: liability | `s 9A(3) the Commissioner or investigating officer may report the failure to a Magistrate, who may issue a warrant to secure the attendance` |
| s 9B(1) | State: claim | Employer or other person: duty | `s 9B(1) the person is guilty of an offence`; `s 9B(1) the penalty on conviction`; `s 9B(1) the sentence is within the penalty` |
| s 9B(2) | State: claim | Any person: duty | `s 9B(2) the person is guilty of an offence` |
| s 9C | State: claim | Offender: duty | `s 9C the penalty on conviction`; `s 9C the sentence is within the penalty` |
| s 10(1) | Investigating officer: power | Suspected offender: liability | `s 10(1) the investigating officer may compound the offence`; `s 10(1) the largest sum that may be collected` |
| s 10(2) | Suspected offender: immunity | State: disability | `s 10(2) further proceedings may be taken against the person in respect of the offence` |
| s 11(1) | Exempted person: immunity | Employee and others: disability | `s 11(1) the person is exempt from the provision` |
| s 11(2) | Minister: power | Exempted person: liability | `s 11(2) the Minister may revoke the exemption, vary or revoke its conditions, or impose new conditions` |
| s 11A | Employee: immunity | Employer: disability | `s 11A the term is void insofar as it so purports` |
| s 11B | Employee and employer: privilege | Tribunal and Minister: no-right | `s 11B regard may be had to the guidelines for the purpose` |
| s 13 | Employee and others: immunity | Employer: disability | `s 13 this Act relieves the employer of the duty or liability` |

Provisions that create no such relation (a definition, a counting rule, a list of what a power may take into account, a gate on another section), listed once as `none`: s 2(1); s 2(1) "agreed date"; s 2(1) "approved mediator"; s 2(1) "claim referral certificate"; s 2(1) "collective agreement"; s 2(1) "Commissioner"; s 2(1) "contract of service"; s 2(1) "eligible employee"; s 2(1) "employee"; s 2(1) "employer"; s 2(1) "employer" (a); s 2(1) "employer" (b); s 2(1) "employer" (c); s 2(1) "employer" (d); s 2(1) "employment assistance payment"; s 2(1) "Employment Claims Tribunal"; s 2(1) "investigating officer"; s 2(1) "mediation request"; s 2(1) "prescribed minimum retirement age"; s 2(1) "prescribed re-employment age"; s 2(1) "re-employment"; s 2(1) "re-employment contract"; s 2(1) "re-employment obligations"; s 2(1) "salary"; s 2(1) "specified age"; s 2(1) "specified age" (a); s 2(1) "specified age" (b); s 2(1) "tripartite guidelines"; s 2(2)(a); s 2(2)(b); s 2(3); s 4(1); s 7(1)(a); s 7(1)(b); s 7(1)(b)(i); s 7A(2); s 7A(2)(a); s 7A(2)(b); s 7A(3)(a); s 7A(11); s 7B(2)(a); s 7B(2)(b); s 7C(1)(a); s 7C(1)(b); s 7C(1)(b)(i); s 7C(1)(b)(ii); s 7C(2); s 7C(4)(b); s 7C(6)(a); s 7C(6)(b); s 8(3)(a); s 8(3)(b); s 8(4)(a); s 8(4)(b); s 8(4)(c); s 8(4)(d); s 8(4)(e); s 8(9); s 8(10); s 8A(4); s 8A(4)(a); s 8A(4)(b); s 8A(4)(c); s 8A(4)(d); s 8B(3)(a); s 8B(3)(b); s 8B(4)(a); s 8B(4)(b); s 8B(6)(a); s 8B(6)(b); s 8B(7)(a); s 8B(7)(b); s 8B(9); s 8B(10)(a); s 8B(10)(b); s 8B(15); s 8B(16); s 8C(2)(a); s 8C(2)(b); s 8C(3)(a); s 9(1)(a); s 9(1)(d); s 9(1)(e); s 9(1)(f); s 9A(1)(a); s 9A(1)(b); s 9A(1)(c); s 10(1)(a); s 10(1)(b); s 11A(a); s 11A(b).
<!-- END jural -->

## Coverage table

The coverage table was built fresh, so there were no rows before; there are 208 after.
`python3 -I coverage.py audit` counts 966 non-blank lines in the 1,390-line text and finds every one in some row: 80 are running page headers and footers and 45 are marginal amendment notes (both counted automatically, inert reason 1), and the rest are in the 208 rows.
The rows by disposition: encoded 156, fork 22, inert reason 1 (not operative) 11, inert reason 2 (machinery) 14, repealed or blank in this text 5.
Lines 115 to 117 are in two rows, because one sentence defines two terms ("approved mediator" and "claim referral certificate").
All 159 rules in layer 1 (every function whose name begins `s ...`) are in a row, and every encoded or fork row has a rule: the audit ends `AUDIT OK`.
Nothing is a row of "out of scope" or "deferred", and no row was moved out of inert, because the table was built fresh.

<!-- BEGIN coverage -->
| Row | Lines | Disposition | Encoded by / why |
| --- | --- | --- | --- |
| front: title | 1-17 | inert, reason 1 | title, edition banner and publication notes |
| front: arrangement | 19-91 | inert, reason 1 | the Arrangement of Sections is a table of contents |
| front: long title | 93-95 | inert, reason 1 | long title creates no rule |
| front: commencement | 97 | inert, reason 2 | the Act's own commencement date |
| Part 1: headings | 99-101,104,238 | inert, reason 1 | part title and section headings |
| s 1 | 102 | inert, reason 2 | short title |
| s 2(1) | 105 | encoded | `s 2(1) the Act's definitions apply` |
| s 2(1) "agreed date" | 106-108 | encoded | `s 2(1) "agreed date" the date is the agreed date` |
| s 2(1) "approved mediator" | 115-117 | encoded | `s 2(1) "approved mediator" the person is an approved mediator` |
| s 2(1) "claim referral certificate" | 115-117 | encoded | `s 2(1) "claim referral certificate" the document is a claim referral certificate` |
| s 2(1) "collective agreement" | 119-120 | encoded | `s 2(1) "collective agreement" the agreement is a collective agreement` |
| s 2(1) "Commissioner" | 122-123 | encoded | `s 2(1) "Commissioner" the person is the Commissioner` |
| s 2(1) "contract of service" | 125-128 | encoded | `s 2(1) "contract of service" the agreement is a contract of service` |
| s 2(1) "eligible employee" | 130-131 | encoded | `s 2(1) "eligible employee" the person is an eligible employee` |
| s 2(1) "employee" | 133-134 | encoded | `s 2(1) "employee" the person is an employee` |
| s 2(1) "employer" | 136-138 | fork F4,F22 | `s 2(1) "employer" the person is an employer` |
| s 2(1) "employer" (a) | 139 | encoded | within `s 2(1) "employer" the person is an employer` |
| s 2(1) "employer" (b) | 141 | encoded | within `s 2(1) "employer" the person is an employer` |
| s 2(1) "employer" (c) | 143-144 | encoded | within `s 2(1) "employer" the person is an employer` |
| s 2(1) "employer" (d) | 146-149 | encoded | within `s 2(1) "employer" the person is an employer` |
| s 2(1) "employment assistance payment" | 151-153 | encoded | `s 2(1) "employment assistance payment" the sum is an employment assistance payment` |
| s 2(1) "Employment Claims Tribunal" | 155-157 | encoded | `s 2(1) "Employment Claims Tribunal" the body is an Employment Claims Tribunal` |
| s 2(1) "investigating officer" | 159-160 | encoded | `s 2(1) "investigating officer" the person is an investigating officer` |
| s 2(1) "mediation request" | 167-168 | encoded | `s 2(1) "mediation request" the request is a mediation request` |
| s 2(1) "prescribed minimum retirement age" | 170-173 | encoded | `s 2(1) "prescribed minimum retirement age" the employee's prescribed minimum retirement age` |
| s 2(1) "prescribed re-employment age" | 177-179 | encoded | `s 2(1) "prescribed re-employment age" the employee's prescribed re-employment age` |
| s 2(1) "re-employment" | 183-185 | encoded | `s 2(1) "re-employment" the employment is re-employment` |
| s 2(1) "re-employment contract" | 189-192 | encoded | `s 2(1) "re-employment contract" the contract is a re-employment contract` |
| s 2(1) "re-employment obligations" | 194-198 | encoded | `s 2(1) "re-employment obligations" the obligations are the re-employment obligations` |
| s 2(1) "salary" | 200-201 | encoded | `s 2(1) "salary" the sum is salary` |
| s 2(1) "specified age" | 203-204 | encoded | `s 2(1) "specified age" the employee's specified age` |
| s 2(1) "specified age" (a) | 206 | encoded | within `s 2(1) "specified age" the employee's specified age` |
| s 2(1) "specified age" (b) | 208-209 | encoded | within `s 2(1) "specified age" the employee's specified age` |
| s 2(1) "tripartite guidelines" | 218-219 | encoded | `s 2(1) "tripartite guidelines" the guidelines are the tripartite guidelines` |
| s 2(2) | 223-224 | fork F16 | `s 2(2) the employee is treated as dismissed by the employer` |
| s 2(2)(a) | 226-228 | encoded | within `s 2(2) the employee is treated as dismissed by the employer` |
| s 2(2)(b) | 230-231 | encoded | within `s 2(2) the employee is treated as dismissed by the employer` |
| s 2(3) | 233-236 | fork F1,F2 | `s 2(3) the date of the anniversary on which the person attains the age`; `s 2(3) the person has attained the age on the date` |
| s 3(1) | 240-241 | inert, reason 2 | the officer in charge of the general administration of the Act |
| s 3(2) | 243-250 | encoded | `s 3(2) the act is deemed to have been duly performed or exercised by the Commissioner` |
| s 3(3) | 252-254 | inert, reason 2 | the Minister's power to appoint investigating officers is staffing |
| s 3(4) | 258-259 | inert, reason 2 | rule-making power |
| Part 2: headings | 266-270,272,297 | inert, reason 1 | part title, amendment note and section headings |
| s 4(1) | 274-277 | encoded | `s 4(1) the age specified may be the prescribed minimum retirement age` |
| s 4(2) | 281-284 | fork F23 | `s 4(2) the employer may dismiss the employee on the ground of age before the prescribed minimum retirement age`; `s 4(2) the employer shall not dismiss the employee on the ground of age before the prescribed minimum retirement age` |
| s 4(3) | 288-291 | encoded | `s 4(3) the employer is guilty of an offence`; `s 4(3) the penalty on conviction`; `s 4(3) the sentence is within the penalty` |
| s 5 | 295 | repealed or blank in this text | the text shows [Repealed by Act 5 of 2017] |
| s 6 | 299-302 | fork F22 | `s 6 the term is void`; `s 6 the retirement age that the term leaves standing` |
| Part 3: headings | 306-308,339,458-459,501 | inert, reason 1 | part title and section headings |
| s 7(1) | 309-310 | encoded | `s 7(1) the employee is eligible for re-employment in accordance with section 7A` |
| s 7(1)(a) | 311 | encoded | `s 7(1)(a) the employee is born on or after 1 July 1952` |
| s 7(1)(b) | 318 | encoded | within `s 7(1) the employee is eligible for re-employment in accordance with section 7A` |
| s 7(1)(b)(i) | 320 | encoded | within `s 7(1) the employee is eligible for re-employment in accordance with section 7A` |
| s 7(1)(b)(ii) | 322 | fork F5 | `s 7(1)(b)(ii) the employee counts as assessed by the employer as medically fit to continue working` |
| s 7(2) | 326-329 | fork F5 | `s 7(2) the employee is presumed to be medically fit to continue working` |
| s 7(3) | 331-335 | fork F23 | `s 7(3) the employer has complied with the duty to give written notice of the intention not to re-employ`; `s 7(3) the employer must give the employee written notice of the intention not to re-employ` |
| s 7A(1) | 341-346 | fork F6,F7,F19 | `s 7A(1) the employer owes the employee an offer of re-employment before the specified age`; `s 7A(1) the last day on which the employer can offer re-employment`; `s 7A(1) the offer of re-employment was made before the employee attained the specified age`; `s 7A(1) the employer's obligation to re-employ the employee is on foot on the date`; `s 7A(1) the employer must offer re-employment before the employee attains the specified age` |
| s 7A(2) | 352 | fork F23 | `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` |
| s 7A(2)(a) | 354-356 | encoded | within `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` |
| s 7A(2)(b) | 358-363 | encoded | within `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` |
| s 7A(2) effect | 365-366,373-374 | encoded | within `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` |
| s 7A(3) | 378-379 | fork F23 | `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(a) | 381-382 | encoded | within `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(a)(i) | 384 | encoded | within `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(a)(ii) | 386-388 | fork F20 | within `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(3)(b) | 390-397 | fork F17 | within `s 7A(3) the employer may re-employ the employee`; `s 7A(3) the employer may terminate the employment of the employee`; `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` |
| s 7A(4) | 401-405 | encoded | `s 7A(4) the employer has complied with the requirement to enter into a re-employment contract`; `s 7A(4) the job scope and the terms and conditions may vary from the previous contract` |
| s 7A(5) | 409-412 | encoded | `s 7A(5) the variation is based on a reasonable factor` |
| s 7A(6) | 414-416 | fork F8,F18 | `s 7A(6) the period of employment stipulated is not less than one year` |
| s 7A(7) | 420-423,430-431,433-434 | fork F23 | `s 7A(7) the period of employment may be for the shorter period` |
| s 7A(8) | 440 | repealed or blank in this text | the text shows [Deleted by Act 5 of 2017] |
| s 7A(9) | 442-445 | encoded | `s 7A(9) the eligible employee may retire or be retired` |
| s 7A(10) | 447-450 | encoded | `s 7A(10) the employee has complied with the duty to give written notice of the intention to retire`; `s 7A(10) the eligible employee must give the employer written notice of the intention to retire` |
| s 7A(11) | 452-454 | encoded | `s 7A(11) the age specified may be the prescribed re-employment age` |
| s 7B(1) | 461-470 | fork F8,F23 | `s 7B(1) the previous service is disregarded for the purpose` |
| s 7B(2) | 474-483 | encoded | `s 7B(2) the previous service is reckoned for the purpose` |
| s 7B(2)(a) | 485-487 | encoded | within `s 7B(2) the previous service is reckoned for the purpose` |
| s 7B(2)(b) | 489-491 | encoded | within `s 7B(2) the previous service is reckoned for the purpose` |
| s 7B(3) | 495-497 | encoded | `s 7B(3) the employee's continuity of employment under re-employment is not broken` |
| s 7C(1) | 503-508 | fork F9 | `s 7C(1) section 7A does not apply to the employer` |
| s 7C(1)(a) | 510-511 | encoded | within `s 7C(1) section 7A does not apply to the employer` |
| s 7C(1)(b) | 513 | encoded | within `s 7C(1) section 7A does not apply to the employer` |
| s 7C(1)(b)(i) | 515-516 | encoded | within `s 7C(1) section 7A does not apply to the employer` |
| s 7C(1)(b)(ii) | 518 | encoded | within `s 7C(1) section 7A does not apply to the employer` |
| s 7C(2) | 522-523 | encoded | `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(2)(a) | 525-526 | fork F10 | within `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(2)(b) | 528-530 | encoded | within `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(2)(c) | 537-540 | encoded | within `s 7C(2) E1's re-employment obligations are discharged on the date`; `s 7C(2) the reference to the employer includes E2 on the date`; `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` |
| s 7C(3) | 544-548 | encoded | `s 7C(3) the employer is not required to offer an employment assistance payment` |
| s 7C(4) | 552-553 | fork F11 | `s 7C(4) the employment assistance payment is made in a form the section names`; `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` |
| s 7C(4)(a) | 555-556 | fork F11 | within `s 7C(4) the employment assistance payment is made in a form the section names`; `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` |
| s 7C(4)(b) | 558 | encoded | within `s 7C(4) the employment assistance payment is made in a form the section names`; `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` |
| s 7C(5) | 560-562 | encoded | `s 7C(5) the employer has complied with the duty to take the tripartite guidelines into account` |
| s 7C(6) | 564-568 | encoded | `s 7C(6) the service under E1 is reckoned for the purpose` |
| s 7C(6)(a) | 570-572 | encoded | within `s 7C(6) the service under E1 is reckoned for the purpose` |
| s 7C(6)(b) | 574-576 | encoded | within `s 7C(6) the service under E1 is reckoned for the purpose` |
| s 7C(7) | 580-582 | encoded | `s 7C(7) the consent form is prima facie proof of the matters mentioned in subsection (1)(b)` |
| s 7C(8) | 591-592 | fork F23 | `s 7C(8) a reference to the employer in Part 4 or 5 includes E2` |
| Part 4: headings | 596-598,600,688,753-754,910-911 | inert, reason 1 | part title and section headings |
| s 8(1) | 602-606 | fork F12,F3,F22 | `s 8(1) the last day on which the employee can make representations to the Minister`; `s 8(1) the employee may make representations in writing to the Minister to be reinstated` |
| s 8(2) | 608-611 | fork F23 | `s 8(2) the Minister may direct the Commissioner in writing to inquire and report` |
| s 8(3) | 613-617 | encoded | `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(3)(a) | 619-623 | encoded | within `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(3)(b) | 625-628 | encoded | within `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(3) closing | 630 | encoded | within `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation`; `s 8(3) the employer has complied with the direction of the Minister`; `s 8(3) the employer must comply with the direction of the Minister` |
| s 8(4) | 632-634 | encoded | `s 8(4) the Minister must have regard to the consideration` |
| s 8(4)(a) | 641-642 | encoded | within `s 8(4) the Minister must have regard to the consideration` |
| s 8(4)(b) | 644-645 | encoded | within `s 8(4) the Minister must have regard to the consideration` |
| s 8(4)(c) | 647 | encoded | within `s 8(4) the Minister must have regard to the consideration` |
| s 8(4)(d) | 649 | encoded | within `s 8(4) the Minister must have regard to the consideration` |
| s 8(4)(e) | 650 | encoded | within `s 8(4) the Minister must have regard to the consideration` |
| s 8(5) | 652-653 | encoded | `s 8(5) the decision of the Minister on the representation is final` |
| s 8(6) | 655-657 | fork F23 | `s 8(6) the employee may bring an action for damages in a court in respect of the unlawful dismissal` |
| s 8(7) | 659-662 | encoded | `s 8(7) the employer is guilty of an offence`; `s 8(7) the penalty on conviction`; `s 8(7) the sentence is within the penalty` |
| s 8(8) | 664-670 | fork F23 | `s 8(8) the amount recoverable by the court as if it were a fine`; `s 8(8) the court may recover the unpaid amount as if it were a fine` |
| s 8(9) | 672-674 | encoded | `s 8(9) the Minister may delegate the power` |
| s 8(10) | 676-677 | encoded | `s 8(10) the delegation is revocable at will`; `s 8(10) the delegation prevents the Minister from exercising the power` |
| s 8(11) | 679-681 | encoded | `s 8(11) the power exercised by the delegate is deemed to have been exercised by the Minister` |
| s 8A(1) | 690-695 | fork F3 | `s 8A(1) the last day on which the employee can notify the Commissioner of the re-employment dispute`; `s 8A(1) the employee notified the Commissioner in time`; `s 8A(1) the employee must notify the Commissioner in writing of the re-employment dispute` |
| s 8A(2) | 699-706 | fork F3 | `s 8A(2) the last day on which the employee can notify the Commissioner of the dismissal`; `s 8A(2) the employee notified the Commissioner in time`; `s 8A(2) the employee must notify the Commissioner in writing of the dismissal` |
| s 8A(3) | 708-715 | fork F3 | `s 8A(3) the last day on which the employee can submit a mediation request`; `s 8A(3) the employee submitted the mediation request in time`; `s 8A(3) the employee must submit a mediation request to the Commissioner` |
| s 8A(4) | 719-720 | encoded | `s 8A(4) the dispute is a re-employment dispute` |
| s 8A(4)(a) | 722-724 | encoded | within `s 8A(4) the dispute is a re-employment dispute` |
| s 8A(4)(b) | 726-729 | encoded | within `s 8A(4) the dispute is a re-employment dispute` |
| s 8A(4)(c) | 736-738 | encoded | within `s 8A(4) the dispute is a re-employment dispute` |
| s 8A(4)(d) | 740-742 | encoded | within `s 8A(4) the dispute is a re-employment dispute` |
| s 8A(5) | 746-749 | fork F23 | `s 8A(5) the Commissioner may consult, or direct an approved mediator to consult, the employer and employee` |
| s 8B(1) | 756-764 | fork F13 | `s 8B(1) the employee may make representations in writing to the Minister to be re-employed` |
| s 8B(2) | 766-768 | fork F3 | `s 8B(2) the last day on which the employee can make representations to the Minister`; `s 8B(2) the representations were made in time`; `s 8B(2) the employee must make written representations to the Minister within one month after the conclusion of the conciliation` |
| s 8B(3) | 770-773 | fork F23 | `s 8B(3) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(3) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8B(3)(a) | 775-777 | encoded | within `s 8B(3) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(3) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8B(3)(b) | 784-786 | encoded | within `s 8B(3) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(3) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8B(4) | 790-793 | fork F23 | `s 8B(4) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(4) the employee may make representations to the Minister under subsection (1)` |
| s 8B(4)(a) | 795-797 | encoded | within `s 8B(4) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(4) the employee may make representations to the Minister under subsection (1)` |
| s 8B(4)(b) | 799-800 | encoded | within `s 8B(4) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)`; `s 8B(4) the employee may make representations to the Minister under subsection (1)` |
| s 8B(5) | 804-809 | fork F23 | `s 8B(5) the Minister may direct the Commissioner to inquire and report` |
| s 8B(6) | 811-816 | encoded | `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(6)(a) | 818 | encoded | within `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(6)(b) | 820-822 | encoded | within `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(6) closing | 824 | encoded | within `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation`; `s 8B(6) the employer has complied with the direction of the Minister` |
| s 8B(7) | 826-829,836-838 | encoded | `s 8B(7) the Minister may allow the employee to submit a mediation request and to lodge a claim for employment assistance payment` |
| s 8B(7)(a) | 840-841 | encoded | within `s 8B(7) the Minister may allow the employee to submit a mediation request and to lodge a claim for employment assistance payment` |
| s 8B(7)(b) | 843-847 | encoded | within `s 8B(7) the Minister may allow the employee to submit a mediation request and to lodge a claim for employment assistance payment` |
| s 8B(8) | 851-853 | fork F23 | `s 8B(8) the employee submitted the mediation request within the time the Minister determined`; `s 8B(8) the employee must submit the mediation request within the time the Minister determined` |
| s 8B(9) | 857-858 | encoded | `s 8B(9) section 8C(3) applies in relation to the claim` |
| s 8B(10) | 862-864 | encoded | `s 8B(10) the Minister may have regard to the consideration` |
| s 8B(10)(a) | 866 | encoded | within `s 8B(10) the Minister may have regard to the consideration` |
| s 8B(10)(b) | 868-869 | encoded | within `s 8B(10) the Minister may have regard to the consideration` |
| s 8B(11) | 871-872 | encoded | `s 8B(11) the decision of the Minister on the representation is final` |
| s 8B(12) | 874-877 | fork F23 | `s 8B(12) the employee may bring an action for damages in a court in respect of the denial of re-employment or the dismissal` |
| s 8B(13) | 879-882 | encoded | `s 8B(13) the employer is guilty of an offence`; `s 8B(13) the penalty on conviction`; `s 8B(13) the sentence is within the penalty` |
| s 8B(14) | 889-895 | fork F23 | `s 8B(14) the amount recoverable by the court as if it were a fine`; `s 8B(14) the court may recover the unpaid amount as if it were a fine` |
| s 8B(15) | 897-900 | encoded | `s 8B(15) the Minister may delegate the power` |
| s 8B(16) | 902-904 | encoded | `s 8B(16) the delegation is revocable at will`; `s 8B(16) the delegation prevents the Minister from exercising the power` |
| s 8B(17) | 906-908 | encoded | `s 8B(17) the power exercised by the delegate is deemed to have been exercised by the Minister` |
| s 8C(1) | 913-918 | fork F21,F22 | `s 8C(1) the employee may lodge a claim for employment assistance payment with an Employment Claims Tribunal` |
| s 8C(2) | 922-925 | fork F23 | `s 8C(2) the employee may make representations under section 8B(1) in respect of that dismissal`; `s 8C(2) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8C(2)(a) | 927-928 | encoded | within `s 8C(2) the employee may make representations under section 8B(1) in respect of that dismissal`; `s 8C(2) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8C(2)(b) | 935-937 | encoded | within `s 8C(2) the employee may make representations under section 8B(1) in respect of that dismissal`; `s 8C(2) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` |
| s 8C(3) | 941-942 | encoded | `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account`; `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` |
| s 8C(3)(a) | 944-946 | encoded | within `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account`; `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` |
| s 8C(3)(b) | 948-952 | encoded | within `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account`; `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` |
| s 8D | 956 | repealed or blank in this text | the text shows [Repealed by Act 21 of 2016] |
| s 8E | 958 | repealed or blank in this text | the text shows [Repealed by Act 21 of 2016] |
| s 8F | 960 | repealed or blank in this text | the text shows [Repealed by Act 21 of 2016] |
| Part 5: headings | 962-964,966,1022,1064,1076,1091,1110,1119,1135,1147,1184 | inert, reason 1 | part title and section headings |
| s 9(1) | 967-969 | fork F14,F23 | `s 9(1) the person has the power` |
| s 9(1)(a) | 971-976 | encoded | within `s 9(1) the person has the power` |
| s 9(1)(b) | 978-991 | encoded | `s 9(1)(b) the person examined is bound to state truly the facts and circumstances` |
| s 9(1)(c) | 993-996 | encoded | `s 9(1)(c) the Commissioner or investigating officer may require the employer to produce the employee and the documents` |
| s 9(1)(d) | 998-999 | encoded | within `s 9(1) the person has the power` |
| s 9(1)(e) | 1001-1002 | encoded | within `s 9(1) the person has the power` |
| s 9(1)(f) | 1004-1008 | encoded | within `s 9(1) the person has the power` |
| s 9(1)(g) | 1010-1012 | encoded | `s 9(1)(g) the Commissioner or investigating officer may require a person to produce the article` |
| s 9(2) | 1014-1020 | encoded | `s 9(2) the person is guilty of an offence`; `s 9(2) the penalty on conviction`; `s 9(2) the sentence is within the penalty` |
| s 9A(1) | 1024 | fork F23 | `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(1)(a) | 1026-1028 | encoded | within `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(1)(b) | 1030-1039 | encoded | within `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(1)(c) | 1041-1042 | encoded | within `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(1) summons | 1044-1052 | encoded | within `s 9A(1) the person acting may summon the person`; `s 9A(1) the person summoned is legally bound to attend and to answer truthfully`; `s 9A(1) the person summoned must attend at the time and place specified in the summons` |
| s 9A(2) | 1054-1056 | encoded | `s 9A(2) the person is guilty of an offence` |
| s 9A(3) | 1058-1062 | encoded | `s 9A(3) the Commissioner or investigating officer may report the failure to a Magistrate, who may issue a warrant to secure the attendance` |
| s 9B(1) | 1066-1070 | encoded | `s 9B(1) the person is guilty of an offence`; `s 9B(1) the penalty on conviction`; `s 9B(1) the sentence is within the penalty` |
| s 9B(2) | 1072-1074 | encoded | `s 9B(2) the person is guilty of an offence` |
| s 9C | 1078-1089 | encoded | `s 9C the penalty on conviction`; `s 9C the sentence is within the penalty` |
| s 10(1) | 1093-1097 | fork F22 | `s 10(1) the investigating officer may compound the offence`; `s 10(1) the largest sum that may be collected` |
| s 10(1)(a) | 1099-1100 | encoded | within `s 10(1) the investigating officer may compound the offence`; `s 10(1) the largest sum that may be collected` |
| s 10(1)(b) | 1102 | encoded | within `s 10(1) the investigating officer may compound the offence`; `s 10(1) the largest sum that may be collected` |
| s 10(2) | 1104-1105 | fork F23 | `s 10(2) further proceedings may be taken against the person in respect of the offence` |
| s 10(3) | 1107-1108 | inert, reason 2 | regulation-making power |
| s 11(1) | 1112-1114 | encoded | `s 11(1) the person is exempt from the provision` |
| s 11(2) | 1116-1117 | encoded | `s 11(2) the Minister may revoke the exemption, vary or revoke its conditions, or impose new conditions` |
| s 11A | 1121-1122 | fork F22 | `s 11A the term is void insofar as it so purports` |
| s 11A(a) | 1124-1125 | encoded | within `s 11A the term is void insofar as it so purports` |
| s 11A(b) | 1127-1128 | encoded | within `s 11A the term is void insofar as it so purports` |
| s 11B | 1137-1143 | fork F15,F23 | `s 11B regard may be had to the guidelines for the purpose` |
| s 12(1) | 1149-1152 | inert, reason 2 | regulation-making power |
| s 12(2) | 1154-1156 | inert, reason 2 | regulation-making power |
| s 12(2)(a) | 1158-1159 | inert, reason 2 | regulation-making power |
| s 12(2)(b) | 1161-1163 | inert, reason 2 | regulation-making power |
| s 12(2)(c) | 1165-1166 | inert, reason 2 | regulation-making power |
| s 12(2)(d) | 1168-1170 | inert, reason 2 | regulation-making power |
| s 12(2)(d)(i) | 1172 | inert, reason 2 | regulation-making power |
| s 12(2)(d)(ii) | 1174-1175 | inert, reason 2 | regulation-making power |
| s 13 | 1186-1188 | encoded | `s 13 this Act relieves the employer of the duty or liability` |
| back: legislative history | 1191-1309 | inert, reason 1 | the Legislative History says it is not part of the Act |
| back: abbreviations | 1311-1338 | inert, reason 1 | a list of abbreviations |
| back: comparative table | 1341-1389 | inert, reason 1 | a table matching 2020 sections to the 2012 edition |
| (auto) running page headers and footers | 80 non-blank lines | inert, reason 1 | page headers, footers and page numbers repeat on every page |
| (auto) marginal amendment notes | 45 lines | inert, reason 1 | `[Act 38 of 2021 wef 01/07/2022]`, `[5/2017]` and the like record which Act made an amendment; they state no rule |
<!-- END coverage -->

## Fork register

Every ambiguity, the readings seen, the one taken, and the text that licenses each.
Line numbers are those of `RRA1993.txt`.
The two rulings of 2026-11-04 come first, word for word as printed in the brief.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (ruled 2026-11-05): (a) a period the text fixes in its own words: outside it `JUST FALSE`; (b) a "where" condition not met: `JUST FALSE`; (c) a scope limit with no "only": `NOTHING` outside the scope. Meng's words, verbatim apart from the trigger word: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z.

How E1 applies here: each section's answer is encoded on its own (option C), and the seat asks them one at a time.
Where I gathered by hand, in plain L4, it is in two places only: `s 7(1)(b)(ii)` calls `s 7(2)` because the Act supplies the employer's assessment of medical fitness by presumption (F5), and `s 2(1) "eligible employee"` calls `s 7(1)` because the definition points at it.
Nothing proposes or uses a construct that gathers a legal effect by name.
How N2 applies here: a flat negative ("must not", "shall not", "does not apply", "operates as a bar", "no further proceedings") answers `JUST FALSE`, and the only prohibition the text names a bearer for, section 4(2), is also written as a `SHANT` rule whose breach follows from that answer.
The Hohfeld kinds are in the table above.
How the ruling of 2026-11-05 applies here: every period the text fixes in its own words, and every "where", "when", "upon" or "whenever" condition, answers `JUST FALSE` outside the period or when the condition fails, for the function that asks the proposition the clause governs; a scope limit with no "only" answers `NOTHING` outside the scope.
Where it was not plain which of (a), (b) and (c) a clause is, or what "outside" means for the question the function asks, the reading taken is in F23.

### F1. Section 2(3): a person born on 29 February (lines 233-236)

Readings: (i) the anniversary in a year that has no 29 February is 28 February; (ii) it is 1 March; (iii) the Act does not say.
Taken: (iii).
The rule answers `NOTHING` (silent) for the date, and so for everything counted from it, when the anniversary year has no 29 February.
Licence: the Act says "anniversary of the date of his or her birth" and gives no rule for a date that does not recur.

### F2. Section 2(3): "regarded as attaining ... on or after the Nth anniversary" (lines 233-236)

Readings: (i) the person attains the age on the anniversary and not before, so a date before it answers no to "has attained"; (ii) the sentence says when a person is regarded as having attained and is silent before.
Taken: (i), answering `JUST FALSE`, flagged as reading (c) below.

### F3. Counting months (ss 8(1), 8A(1), 8A(2), 8A(3), 8B(2); lines 602-606, 690-715, 766-768)

Readings: (i) the same day of the following month, with the last day of a shorter month standing in, so one month after 31 January is 28 February (29 in a leap year); (ii) the day before that day; (iii) thirty days.
Taken: (i), through daydate `add months`, with the last day inclusive ("no later than", "within").
The staged time module of the Interpretation Act 1965 was read: its own header says the Act "has NO rule for counting a period of weeks, months or years from a day" and it returns `NOTHING` for them.
Importing it would therefore answer `NOTHING` for every month-counted period in this Act, and would need copying into this folder because `IMPORT` finds only modules beside the importing file, so I did not use it.
The Act itself is silent on how a period in months is counted, and the staged Interpretation Act module does not fill that gap, so counting with daydate `add months` is my own choice, not an answer given by the Act or by that module.
Whether the last day, when it is a Sunday or a public holiday, is moved on is not answered by the Act or by the module's months rule, and is not encoded.
Tested: 31 January 2023 plus one month is 28 February 2023, and 31 August 2023 plus six months is 29 February 2024.

### F4. Section 2(1) "employer": "means ... and includes" (lines 136-149)

Readings: (i) the definition is closed by its limbs; (ii) "includes" leaves the class open.
Taken: (ii).
A person who employs another under a contract of service, the Government, a statutory authority, a duly authorised agent or manager, and an owner or manager of a business in which an employee is engaged, all answer `JUST TRUE`; anyone else answers `NOTHING` (includes).
Ruled 2026-11-05 (c): NOTHING outside the scope.

### F5. Sections 7(1)(b)(ii) and 7(2): the employer's assessment of medical fitness (lines 322, 326-329)

Readings: (i) the employer's assessment of fitness is an input like the assessment of performance; (ii) section 7(2) supplies it: the employee is presumed medically fit unless the employer proves otherwise on a balance of probabilities.
Taken: (ii).
The performance assessment of section 7(1)(b)(i) is the employer's judgment and remains an input (`JUST TRUE`, `JUST FALSE` or `NOTHING`).

### F6. Section 7A(1): "until" the prescribed re-employment age (lines 341-346)

Readings: (i) the obligation lasts until, and not including, the day the employee attains the prescribed re-employment age; (ii) it includes that day.
Taken: (i).
Before the specified age is attained, and on or after the day the prescribed re-employment age is attained, the obligation is not on foot: `JUST FALSE`, for the rule and for the seat question "Is my employer's obligation to re-employ me on foot".
Ruled 2026-11-05 (a): JUST FALSE outside the period.

### F7. Section 7A(1): "Subject to section 7C" (lines 341-346, 503-508)

Readings: (i) section 7C(1) is a gate: where it applies, section 7A(1) imposes no duty; (ii) it adds an alternative way of meeting the duty.
Taken: (i), because section 7C(1) says "Section 7A does not apply".

### F8. "Unless otherwise agreed" and "subject to" (ss 7A(6), 7B(1); lines 414-416, 461-470)

Readings: (i) where the parties agreed otherwise the section says nothing more, so `NOTHING`; (ii) the exception simply lifts the rule, so the opposite answer.
Taken for section 7B(1): (ii), `JUST FALSE`, marginal reading (a): where the parties agreed otherwise, "the previous service is disregarded" is not so, because the text introduces the rule with "Unless otherwise agreed", and an "unless" says when the rule does not hold.
Reading (i) is the one rejected for section 7B(1): it left the agreed-otherwise case unanswered on the ground that the section says nothing of what the parties agreed in its place; but the question asked is only whether the earlier service is disregarded, and that the text answers.
What the parties agreed in the earlier service's place is theirs and is not asked.
Taken for section 7A(6): (i), `NOTHING`: the function asks whether the period meets the requirement "must not be less than one year", and where the parties agreed otherwise the requirement is lifted; a shorter period is then not a breach, but the section does not say whether such a period is "not less than one year", so the answer is not given.
Section 7B(1) is also "subject to subsections (2) and (3)": taken as a gate, so for annual leave and paid sick leave "the previous service is disregarded" answers `JUST FALSE` (reading (c) below).

### F9. Section 7C(1): a failed "if" (lines 503-518)

Readings: (i) where the conditions for disapplying section 7A are not all met, section 7A applies, so `JUST FALSE`; (ii) the section says only when section 7A does not apply, so `NOTHING`.
Taken: (i), reading (a) below.

### F10. Section 7C(2)(a): "immediately before the agreed date" (lines 525-526)

Readings: (i) at the end of the day before the agreed date, so discharged on the agreed date and after; (ii) on the day before.
Taken: (i).
Before the agreed date the obligations are not discharged: `JUST FALSE`; the same holds for the reference to E2 in section 7C(2)(b), which runs "from that agreed date".
Ruled 2026-11-05 (a): JUST FALSE outside the period.

### F11. Section 7C(4): "is (a) a single lump sum ... by the last day of employment; or (b) other mutually agreed arrangements" (lines 552-558)

Readings: (i) the two forms are the only ones, so a lump sum paid late, with no other arrangement agreed, is neither and the answer is `JUST FALSE`; (ii) the two are the forms the section names, and a payment of neither form is neither said to be one nor said not to be (`NOTHING`, list not closed).
Taken: (i), marginal reading (a).
Reading (ii) is the one rejected: subsection (4) says the employment assistance payment "is" (a) or (b), and does not say "includes".
The decision function and the duty rule `s 7C(4) the employer must pay the employment assistance payment as a single lump sum by the last day of employment` now agree: a payment after the last day is a breach of the duty and is not a form the section names.
The seat question "Is the way my payment is made one the Act names" answers `JUST FALSE` for a lump sum paid after the last day with no other arrangement.
Where no lump sum has been paid and no other arrangement was agreed, there is as yet no payment to say which form it takes: `NOTHING` (silent).
"By the last day" is inclusive.

### F12. Section 8(1): the age "below the specified age" (lines 602-606)

Readings: (i) the age of the employee at the dismissal; (ii) at the time the representations are made.
Taken: (i).
"Specified age" is the higher of the prescribed minimum retirement age and the contract's age, so the class of section 8(1) is wider than the prohibition of section 4(2); see finding 4.
For an employee who had already attained the specified age at the dismissal ("any employee below the specified age", line 602) the function answers `NOTHING`.
Ruled 2026-11-05 (c): NOTHING outside the scope.

### F13. Sections 8B(1) and 8B(2): "any conciliation conducted pursuant to section 8A(5)" (lines 756-768)

Readings: (i) where the Commissioner conducted none, the Act does not say when representations may be made or by when (`NOTHING`); (ii) the time runs from the notice under section 8A(1) or (2); (iii) there is no deadline.
Taken: (i).
"At any time after" a conciliation is read as from the day it concluded, that day included; the one month of section 8B(2) runs from that day.
Representations made before the conciliation concluded answer `JUST FALSE`.
Ruled 2026-11-05 (a): JUST FALSE outside the period.

### F14. Section 9(1): "power to do all or any of the following" (lines 967-969)

Readings: (i) each of the seven powers is a separate grant; (ii) the powers are granted only together.
Taken: (i).
A power not in the list answers `NOTHING` (list not closed).

### F15. Section 11B: "regard may be had" (lines 1137-1143)

Readings: (i) a permission; (ii) a duty.
Taken: (i): the rule answers `JUST TRUE` when the guidelines are published for one of the named purposes and never `JUST FALSE`.
Contrast section 7C(5), which says the employer must take the guidelines into account.

### F16. Section 2(2)(b): the comma before "or requires or causes" (lines 223-231)

Readings: (i) "on the ground of age" qualifies only requiring or causing the employee to retire or resign, so an employer's retiring the employee on any ground is a dismissal; (ii) it qualifies the retiring as well.
Taken: (i).

### F17. Section 7A(3)(b): "for the period between" (lines 390-397)

Readings: (i) both ends are inside the period; (ii) neither is.
Taken: (i).
The period has no end until the employer re-employs or terminates.
Before the specified age is attained, and after the employer re-employs or terminates, the deeming does not apply: `JUST FALSE`.
Ruled 2026-11-05 (a): JUST FALSE outside the period.
Where subsection (2) does not apply at all, the deeming does not apply either.
Ruled 2026-11-05 (b): JUST FALSE when the condition fails.

### F18. Section 7A(6): "not be less than one year" (lines 414-416, 420-434)

Readings: (i) a period of one year that begins on a day ends on the day before the next anniversary of that day; (ii) it is 365 days; (iii) it ends on the anniversary.
Taken: (i), through `add years`, and the same count for the "less than one year" of section 7A(7).
A period that begins on 29 February answers `NOTHING` (silent).

### F19. Section 7A(1): an employee who is not an eligible employee (lines 309-311, 341-343)

Readings: (i) section 7(1) has already said no ("an employee is eligible for re-employment in accordance with section 7A if" its limbs are met), and the duty of section 7A(1) is owed to "an employee of the employer (being an eligible employee)", so where eligibility is `JUST FALSE` no offer is owed and the obligation is not on foot: `JUST FALSE`; (ii) the duty is stated for an eligible employee and the section says nothing of anyone else: `NOTHING`.
Taken: (i), for `s 7A(1) the employer owes the employee an offer of re-employment before the specified age` and for `s 7A(1) the employer's obligation to re-employ the employee is on foot on the date`, whatever is known of section 7C(1); marginal reading (a).
An eligibility answer of `NOTHING` (not known) still gives `NOTHING`.
The seat questions "Does my employer owe me an offer of re-employment" and "Is my employer's obligation to re-employ me on foot" answer `JUST FALSE` for a person who says they are not an eligible employee.
Every input of type `MAYBE BOOLEAN` in layer 1 was checked for a `JUST FALSE` that is dropped into `NOTHING` (`grep -n 'IS A MAYBE BOOLEAN' rra-part*.l4`).
The two work-performance inputs go to the `every one of these answers is yes` helper, which already treats a `JUST FALSE` as the answer; the section 7C(1) input in the two rules above is read both ways; `s 7A(5)` hands its input back as it is; section 7A(3)(a)(ii) is F20.
The last, `s 7A(9)`, still answers `NOTHING` for an employee who is not eligible: it is a permission "Despite any of the provisions of this Act" for an eligible employee to retire, and it says nothing of whether others may retire, so there is no no to carry.

### F20. Section 7A(3)(a)(ii): "terminate the employment of the employee if the employee does not satisfy ..." (lines 378-388)

Readings: (i) the permission is given "if" the employee does not satisfy section 7(1)(b); where the employee does satisfy it, the "if" is not met and the permission does not arise: `JUST FALSE`; (ii) the text gives a permission in one case and does not say that the employer may not terminate in the other: `NOTHING`.
Taken: (i), marginal reading (a), within the case that subsection (3) speaks to (subsection (2) applies and the specified age has been attained).
Outside that case (subsection (2) not applying, or the specified age not yet attained) the permission does not arise either: `JUST FALSE`.
Ruled 2026-11-05 (a) and (b): JUST FALSE outside the period and when the condition fails.
Where it is not known whether the employee satisfies section 7(1)(b), the answer is `NOTHING`.
The answer concerns the permission this paragraph gives; it does not say whether the employer may terminate on some other lawful ground.

### F21. Section 8C(1): "may, if a claim referral certificate is issued" (lines 913-918)

Readings, for the certificate: (i) the employee "may, if a claim referral certificate is issued ... lodge a claim"; with no certificate the "if" is not met and the permission does not arise: `JUST FALSE`; (ii) `NOTHING`.
Taken: (i), for a dispute over a matter in section 8A(4)(c) or (d), marginal reading (a).
Readings, for the matter: the clause "which relates to any matter referred to in section 8A(4)(c) or (d)" narrows who may lodge a claim and has no "if", "only" or "unless".
Taken: `NOTHING` for a dispute over any other matter (including the denials of re-employment in section 8A(4)(a) and (b)), certificate or no certificate.
Ruled 2026-11-05 (c): NOTHING outside the scope.

### F22. Scope limits with no "only" (lines as listed)

Where a sentence names the case it speaks to and the narrowing words are none of "if", "only" or "unless", and are not a period or a "where" (for example "any employee below the specified age", "which relates to any matter referred to in ...", "any offence ... that is prescribed as a compoundable offence"), the text says what the rule covers and does not say that nothing else is covered.
Ruled 2026-11-05 (c): NOTHING outside the scope.
The clauses, and what each answers outside its scope:

- s 2(1) "employer" ("means ... and includes"): F4; a person who is none of the listed kinds answers `NOTHING`.
- s 6 (lines 299-302): a term that provides for a retirement age equal to or above the prescribed minimum retirement age; the function answers `NOTHING` to "the term is void".
- s 8(1) (line 602): an employee who had attained the specified age at the dismissal: F12.
- s 8C(1) (lines 913-915): a dispute over a matter outside section 8A(4)(c) and (d): F21.
- s 10(1) (lines 1093-1095): an offence that is not prescribed as compoundable, and a compounding without the Commissioner's approval; the power answers `NOTHING`.
- s 11A (lines 1121-1128): a term that neither excludes or limits a provision nor precludes a claim, such as a more favourable term; the function answers `NOTHING` to "the term is void insofar as it so purports".

The other scope limits of the same shape (a relative clause naming the person, the thing or the occasion a rule is about) answer `NOTHING` in the same way; they are the branches tagged `limited by its own wording` in the code, and are counted under "Marginal readings for a lawyer".

### F23. Applying the ruling of 2026-11-05 where a clause is not plain

The ruling is applied to the proposition the text states.
A function that asks that proposition answers `JUST FALSE` outside the period or when the "where" fails.
A function that asks the opposite of what the clause says keeps `NOTHING` outside, as every flat negative always did: "A shall not do X if C" gives no for C and gives no yes for not-C.
A function that asks whether a duty was complied with, and not whether the duty exists, keeps `NOTHING` when the duty's trigger fails: there is nothing to comply with, and a no would read as a breach.

Ruled 2026-11-05 (a): JUST FALSE outside the period, for these functions: `s 7A(1)` on foot (and the seat question); `s 7A(3)` "at any time after" the specified age and the deeming period; `s 7A(7)` "that shorter period"; `s 7C(2)(a)` "immediately before the agreed date" and `s 7C(2)(b)` "from that agreed date"; `s 8(1)` "within one month"; `s 8B(1)` "at any time after" the conciliation; `s 8(2)` and `s 8B(5)` "before making a decision".
The month and year periods that already answered `JUST FALSE` when late (ss 7A(1) the offer, 7A(6), 7C(4), 8A(1) to (3), 8B(2), 8B(8)) are unchanged.
Ruled 2026-11-05 (b): JUST FALSE when the condition fails, for these functions: `s 7A(3)` "Where subsection (2) applies"; `s 7A(7)` "where the period between ... is less than one year"; `s 7B(1)` "when a re-employment contract is entered into"; `s 7C(2)(a)`, `(b)` and `(c)` "where subsection (1)(b) applies"; `s 7C(6)` "where E2 enters into a contract of service"; `s 7C(8)` "where applicable"; `s 8(8)` and `s 8B(14)` "Where any amount ... is not paid ... and the employer has been convicted"; `s 8A(5)` "Upon receipt"; `s 8B(7)` "where the Minister (a) has considered ... and (b) is satisfied"; `s 9A(1)` "Whenever"; `s 11B` "upon the publication".

Readings taken where it was not plain which of (a), (b) and (c) a clause is:

- "When", "upon" and "whenever" are read as "where" (ss 7B(1), 8A(5), 9A(1), 11B), and "where applicable" in section 7C(8) as "where section 7C(1)(b) applies".
  If they are scope limits, those answers would be `NOTHING`.
- "Before making a decision" (ss 8(2), 8B(5)) is read as a period the text fixes: once the decision is made the power has gone.
  With no representations at all the answer stays `NOTHING`, because there is nothing to decide on.
- "At any reasonable time" (s 9(1)) is a standard and not a period the text fixes, so an unreasonable time answers `NOTHING` (a scope limit), as "a reasonable period" is an input throughout.
- "A power so delegated, when exercised by the delegate" (ss 8(11), 8B(17)) puts the "when" inside the subject of the deeming, so it is a scope limit and the answer stays `NOTHING`.
- A function that returns a number (`s 8(8)` and `s 8B(14)`, the amount recoverable) has no `JUST FALSE`.
  Each keeps its `NOTHING` and has a yes-or-no twin, `s 8(8) the court may recover the unpaid amount as if it were a fine` and `s 8B(14) the court may recover the unpaid amount as if it were a fine`, which answers the "where".
- Section 7A(7) has two limbs: the "where" (the period between the start of re-employment and the prescribed re-employment age is less than one year) and the length ("may be for that shorter period", read as no longer than that period); either failing answers `JUST FALSE`.

Kept at `NOTHING` outside, because the function asks the opposite of what the clause says:

- A bar asked as "may": ss 8B(3), 8B(4), 8C(2) (the bars on the second step), 8(6) and 8B(12) (the direction bars an action for damages), 10(2) ("On payment of the sum of money, no further proceedings").
  Inside the "where" (or the occasion the bar is of) the answer is `JUST FALSE`; outside it the Act does not say the step may be taken.
- A prohibition asked as "may": `s 4(2)` asks whether the employer may dismiss on the ground of age before the prescribed minimum retirement age; the period is the period of the prohibition, and on or after the day the age is attained the Act does not say the employer may (finding 2).
- A saving asked as "is affected": `s 7A(2)` ("Where ... then any right ... is not affected"); the "where" failing gives no yes to "affected".

Kept at `NOTHING` when the duty's trigger fails, because the function asks about compliance: `s 7(3)` "Where an employer does not intend to re-employ ..."; `s 7A(4)`; `s 7A(6)` ("Unless otherwise agreed", F8); `s 8B(8)` "Where subsection (7) applies".
The duties of sections 7(3) and 7A(10) are also qualified by "as far as it is reasonably practicable" and "insofar as is reasonably practicable"; where giving notice was not reasonably practicable the Act does not say what is owed, and the answer is `NOTHING` (a scope limit, (c)).

Four "if" conditions on a permission or a continuity were found in the same sweep and answer `JUST FALSE` when not met, on reading (a) of the rule of 2026-10-29: `s 7A(9)` ("may retire or be retired, if he or she does not wish ..."), `s 7B(3)` ("is not broken if ..."), `s 8(3)` and `s 8B(6)` ("If, after considering any report ..., the Minister is satisfied ...").

### Section 8(1) and sections 8A and 8B(2): one month

Section 8(1) says "he or she may, within one month of the dismissal, make representations": a period the text fixes in its own words, so a late representation answers `JUST FALSE`.
Ruled 2026-11-05 (a): JUST FALSE outside the period.
Sections 8A(1) to (3) and 8B(2) say the employee "must" notify or act "no later than" a stated time, and sections 8B(8) and 7A(10) say "must": a requirement, so a late act answers `JUST FALSE` (reading (a) of the rule of 2026-10-29).
Both shapes now give the same answer for a late act, and each is listed under its own heading below.

### Choices that are not forks (assumed, not ruled)

- Judgments the Act hands to someone are inputs and never guessed: "satisfactory work performance", "reasonably practicable", "reasonable period", "reasonable factors", "unlawfully dismissed", what the Minister is "satisfied" of, and what the Minister or the Tribunal considers "just and equitable".
- Amounts and times the Act leaves to the Minister (the ages, the time under s 8B(8), the amount of a compensation or payment) are inputs.
- A deadline measured in days from an event is written `WITHIN (Day <last day> MINUS Day <the day the clock starts>)`, the clock starting at an input date; the last day is inclusive because `MUST ... WITHIN n` accepts an act at n.
- A regulative rule with no stated time (ss 7(3), 7A(10), 8(3)) has no `WITHIN`.

## What the text turns out to say

Findings, each ending "Asserted." where a case asserts it.

1. The Act fixes no retirement age. It fixes the ranges within which the Minister must specify them: at least 62 and not more than 65 for the prescribed minimum retirement age (s 4(1)), and at least 67 and not more than 70 for the prescribed re-employment age (s 7A(11)). Every date in the cases uses an illustrative 63 and 68. Asserted (`rra-tests-part2.l4`, `rra-tests-part3.l4`, `rra-cases-seat.l4`).
2. Section 4(2) forbids dismissal on the ground of age before the employee attains the prescribed minimum retirement age and says nothing about the day itself or after. The Act nowhere says the employer may dismiss from that day, so the answer on and after it is `NOTHING`. The "despite any written law, contract of service or collective agreement" input is read by no limb: it cannot change the answer. Asserted.
3. The specified age is the higher of the prescribed minimum retirement age and the retirement age stipulated in the contract; a lower contract age is ignored (and section 6 voids it to that extent). Asserted.
4. The class of section 8(1) ("any employee below the specified age") is wider than the prohibition of section 4(2): with a contract age of 65 and a prescribed minimum of 63, a dismissal on the ground of age at 64 is not prohibited by section 4(2) (`NOTHING`), yet the employee may ask the Minister for reinstatement under section 8(1). "Unlawfully dismissed" is not defined, so whether such a dismissal is unlawful is the employee's belief, an input. Asserted (`rra-tests-part4.l4`).
5. The last day for the offer of re-employment is the day before the specified age is attained; an offer on the day itself is late. Asserted.
6. The employer's obligation to re-employ runs from the day the specified age is attained up to, not including, the day the prescribed re-employment age is attained; before the specified age is attained, and on or after the day the prescribed re-employment age is attained, it is not on foot (F6). Asserted.
7. Section 7A(3)(b) deems the employer to have complied with the duty to offer from the day the employee attains the specified age until the employer re-employs or terminates, and sets no limit: an employee may work on indefinitely with the deeming in force. Asserted.
8. A re-employment period of exactly one year remaining is not "less than one year": a contract beginning on 1 January 2027 for an employee who attains the prescribed re-employment age on 1 January 2028 is outside section 7A(7), and one beginning on 2 January 2027 is inside it. Asserted.
9. Section 7B(1) disregards earlier service but section 7B(2) reckons it for annual leave and paid sick leave, so for those two purposes "disregarded" is false; for any other purpose section 7B(2) says nothing; where the parties agreed otherwise it is not disregarded for any purpose (F8). Section 7C(6), by contrast, reckons the service under the first employer "only" for those two purposes, so any other purpose is false there. Asserted.
10. Section 7A stops applying only if the employer cannot find a suitable vacancy despite reasonable attempts and either offers an employment assistance payment or another employer offers and the employee accepts. Without the payment or the alternative, section 7A still applies. Asserted.
11. A lump sum paid after the last day of employment is neither the single lump sum of section 7C(4)(a) nor an agreed arrangement under (b), and the section does not say what else it could be: "the employment assistance payment is" (a) or (b), so the answer is no (F11). Asserted.
12. The periods of one month (ss 8(1), 8A(1), 8A(2), 8B(2)) and six months (s 8A(3)) are not defined; counted with calendar months, a dispute notice for an employment that ended on 31 January 2023 is due on 28 February 2023, and a mediation request for one that ended on 31 August 2023 is due on 29 February 2024 (F3). Asserted.
13. If the Commissioner conducts no conciliation, sections 8B(1) and 8B(2) do not say when representations may be made or by when (F13). Asserted.
14. Three steps bar each other: representations to be re-employed (s 8B(1)), representations under section 35(3) of the Industrial Relations Act 1960, and a claim in the Employment Claims Tribunal (s 8C(1)). After any one of them the other two are barred (ss 8B(3), 8B(4), 8C(2)); doing the same step twice is not addressed. Asserted (`rra-cases-seat.l4`).
15. A Minister's direction bars an action for damages (ss 8(6), 8B(12)); making representations does not. Unpaid amounts are recoverable "as if it were a fine" only after the employer is convicted of failing to comply (ss 8(8), 8B(14)). Asserted.
16. Whether the Minister's decision is "final" (ss 8(5), 8B(11)) says nothing about review by a court; the encoding answers only that the decision is final. Asserted for the answer; the wider question is not covered.
17. Composition (s 10(1)): the lower of one half of the maximum fine and $1,000 is $1,000 for every offence in the Act, since the maximum fines are $5,000 and $10,000 (ss 4(3), 8(7), 8B(13), 9(2), 9B(1), 9C). Asserted.
18. Section 9B(2) creates an offence only "for which no penalty is expressly provided"; the penalty then comes from section 9C, whose ceilings double for "a subsequent offence under the same section". What makes an offence a subsequent one is not said, and is an input. Asserted.
19. The text shows section 5, section 7A(8) and sections 8D to 8F as repealed or deleted.

## What the text does not answer

- The employer's or Commissioner's conduct when no conciliation is held (F13).
- Whether the Minister's final decision can be reviewed by a court, and whether a deadline that ends on a non-working day is moved on.
- Section 8: the time within which the Minister must decide on representations (nothing in the text sets one); no function.
- Section 8(1): the form of the representations ("make representations in writing", lines 604-605) is not an input; the function answers for representations made as the subsection describes, and the seat question says "written representations".
- Section 8(2): the Minister "may" (line 608) direct the Commissioner "in writing" to inquire and report: the text gives a power and no duty, so there is no duty to encode, and the form of the direction ("in writing") is not an input.
- The amount of any compensation or employment assistance payment: the Minister and the Tribunal fix it (ss 8(3), 8B(6), 8C(3)), guided by the tripartite guidelines, which are not among the sources.
- What a "subsequent offence under the same section" is (s 9C), what "unlawfully dismissed" is (s 8(1)), and what "reasonable" attempts, factors or periods are.
- Anything the regulations prescribe: forms, manner, limitations (s 3(2)), compoundable offences (s 10(3)), modifications (s 7C(2), s 12(2)(d)).
- What an employer may do on the day an employee attains the prescribed minimum retirement age (finding 2).

## Marginal readings for a lawyer

The rule of 2026-10-29 names two readings and asks that every branch resting on one be listed with the other reading stated: (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
I took both as the status quo.
Reading (c) is not in that rule: it is a flag I added for a third shape I met, so that a lawyer sees it once rather than finding it.
Fork F2 and fork F8 describe the two places it arises.
The ruling of 2026-11-05 (fork register, beside E1 and N2) then settled three shapes: a period the text fixes in its own words and a "where" condition answer `JUST FALSE` outside, and a scope limit with no "only" answers `NOTHING` outside.
The branches that rest on it are listed first below, and the branches that rest on the older readings after them.

<!-- BEGIN marginal -->
These counts are produced by `marginal.py` from the tags in the code, so they cannot drift from it.

**Ruled 2026-11-05: a period the text fixes in its own words, and a "where" condition, answer `JUST FALSE` outside the period or when the condition fails (25 branches).** These are not marginal: the ruling is in the fork register beside rulings E1 and N2. They are listed so that a lawyer sees every place it is used; (a) is a period, (b) is a "where" (which includes "when", "upon" and "whenever", fork F23).

| Rule | File | Lines | Ruling |
| --- | --- | --- | --- |
| `s 7A(1) the employer's obligation to re-employ the employee is on foot on the date` | rra-part3-re-employment.l4 | 217 | (a) |
| `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` | rra-part3-re-employment.l4 | 334, 343 | (a) |
| `s 7C(2) E1's re-employment obligations are discharged on the date` | rra-part3-re-employment.l4 | 656 | (a) |
| `s 7C(2) the reference to the employer includes E2 on the date` | rra-part3-re-employment.l4 | 680 | (a) |
| `s 8(1) the employee may make representations in writing to the Minister to be reinstated` | rra-part4-remedies.l4 | 48 | (a) |
| `s 8(2) the Minister may direct the Commissioner in writing to inquire and report` | rra-part4-remedies.l4 | 67 | (a) |
| `s 8B(1) the employee may make representations in writing to the Minister to be re-employed` | rra-part4-remedies.l4 | 541 | (a) |
| `s 8B(5) the Minister may direct the Commissioner to inquire and report` | rra-part4-remedies.l4 | 671 | (a) |
| `s 7A(3) the employer is deemed to have complied with section 7A(1) on the date` | rra-part3-re-employment.l4 | 330 | (b) |
| `s 7B(1) the previous service is disregarded for the purpose` | rra-part3-re-employment.l4 | 542 | (b) |
| `s 7C(2) E1's re-employment obligations are discharged on the date` | rra-part3-re-employment.l4 | 645 | (b) |
| `s 7C(2) the reference to the employer includes E2 on the date` | rra-part3-re-employment.l4 | 670 | (b) |
| `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` | rra-part3-re-employment.l4 | 696 | (b) |
| `s 7C(6) the service under E1 is reckoned for the purpose` | rra-part3-re-employment.l4 | 795 | (b) |
| `s 7C(8) a reference to the employer in Part 4 or 5 includes E2` | rra-part3-re-employment.l4 | 829 | (b) |
| `s 8(8) the court may recover the unpaid amount as if it were a fine` | rra-part4-remedies.l4 | 241 | (b) |
| `s 8A(5) the Commissioner may consult, or direct an approved mediator to consult, the employer and employee` | rra-part4-remedies.l4 | 505 | (b) |
| `s 8B(7) the Minister may allow the employee to submit a mediation request and to lodge a claim for employment assistance payment` | rra-part4-remedies.l4 | 740 | (b) |
| `s 8B(14) the court may recover the unpaid amount as if it were a fine` | rra-part4-remedies.l4 | 903 | (b) |
| `s 9A(1) the person acting may summon the person` | rra-part5-general.l4 | 180 | (b) |
| `s 11B regard may be had to the guidelines for the purpose` | rra-part5-general.l4 | 463 | (b) |
| `s 7A(3) the employer may re-employ the employee` | rra-part3-re-employment.l4 | 277 | (a) and (b) |
| `s 7A(3) the employer may terminate the employment of the employee` | rra-part3-re-employment.l4 | 301 | (a) and (b) |
| `s 7A(7) the period of employment may be for the shorter period` | rra-part3-re-employment.l4 | 441 | (a) and (b) |

**Reading (a): a failed "if", an "unless" that applies, or a "must" that is not met, is the text's no (29 branches).** It covers, among others, section 7B(1) ("Unless otherwise agreed", fork F8), section 7C(4) ("the payment is (a) ... or (b)", read as naming the only two forms, fork F11), sections 7A(3)(a)(ii) and 8C(1) (a permission "if" its condition holds, forks F20 and F21), and the carry of section 7(1)'s no into section 7A(1) (fork F19). The other reading: "if A then B" does not itself say "if not A then not B", and "must" says what is required, not that its absence is a no, so each of these would answer `NOTHING`.

| Rule | File | Lines |
| --- | --- | --- |
| `s 2(2) the employee is treated as dismissed by the employer` | rra-part1-preliminary.l4 | 342 |
| `s 4(1) the age specified may be the prescribed minimum retirement age` | rra-part2-minimum-retirement-age.l4 | 74 |
| `s 7(1)(a) the employee is born on or after 1 July 1952` | rra-part3-re-employment.l4 | 28 |
| `s 7(1) the employee is eligible for re-employment in accordance with section 7A` | rra-part3-re-employment.l4 | 51 |
| `s 7(3) the employer has complied with the duty to give written notice of the intention not to re-employ` | rra-part3-re-employment.l4 | 116 |
| `s 7A(1) the employer owes the employee an offer of re-employment before the specified age` | rra-part3-re-employment.l4 | 150 |
| `s 7A(1) the offer of re-employment was made before the employee attained the specified age` | rra-part3-re-employment.l4 | 180 |
| `s 7A(1) the employer's obligation to re-employ the employee is on foot on the date` | rra-part3-re-employment.l4 | 199 |
| `s 7A(3) the employer may terminate the employment of the employee` | rra-part3-re-employment.l4 | 305 |
| `s 7A(4) the employer has complied with the requirement to enter into a re-employment contract` | rra-part3-re-employment.l4 | 365 |
| `s 7A(5) the variation is based on a reasonable factor` | rra-part3-re-employment.l4 | 396 |
| `s 7A(9) the eligible employee may retire or be retired` | rra-part3-re-employment.l4 | 459 |
| `s 7A(10) the employee has complied with the duty to give written notice of the intention to retire` | rra-part3-re-employment.l4 | 488 |
| `s 7A(11) the age specified may be the prescribed re-employment age` | rra-part3-re-employment.l4 | 510 |
| `s 7B(1) the previous service is disregarded for the purpose` | rra-part3-re-employment.l4 | 546 |
| `s 7B(3) the employee's continuity of employment under re-employment is not broken` | rra-part3-re-employment.l4 | 598 |
| `s 7C(1) section 7A does not apply to the employer` | rra-part3-re-employment.l4 | 627 |
| `s 7C(4) the employment assistance payment is made in a form the section names` | rra-part3-re-employment.l4 | 743 |
| `s 7C(5) the employer has complied with the duty to take the tripartite guidelines into account` | rra-part3-re-employment.l4 | 771 |
| `s 8(3) the Minister may direct the employer to reinstate and pay, or to pay compensation` | rra-part4-remedies.l4 | 97 |
| `s 8(3) the employer has complied with the direction of the Minister` | rra-part4-remedies.l4 | 113 |
| `s 8A(1) the employee notified the Commissioner in time` | rra-part4-remedies.l4 | 383 |
| `s 8A(2) the employee notified the Commissioner in time` | rra-part4-remedies.l4 | 436 |
| `s 8A(3) the employee submitted the mediation request in time` | rra-part4-remedies.l4 | 481 |
| `s 8B(2) the representations were made in time` | rra-part4-remedies.l4 | 567 |
| `s 8B(6) the Minister may direct the employer to re-employ the employee or to pay compensation` | rra-part4-remedies.l4 | 695 |
| `s 8B(6) the employer has complied with the direction of the Minister` | rra-part4-remedies.l4 | 711 |
| `s 8B(8) the employee submitted the mediation request within the time the Minister determined` | rra-part4-remedies.l4 | 765 |
| `s 8C(1) the employee may lodge a claim for employment assistance payment with an Employment Claims Tribunal` | rra-part4-remedies.l4 | 983 |

**Reading (c): the text's own contrary affirmative is read as its no (3 branches).** Section 7B(1) disregards earlier service, "subject to" section 7B(2), which reckons it for annual leave and paid sick leave, so "disregarded for annual leave" is answered `JUST FALSE`; and section 2(3) says a person is regarded as attaining an age on or after the anniversary, so a date before it answers `JUST FALSE` to "has attained" (fork F2). The other reading answers `NOTHING`: the text says what is reckoned, or when a person is regarded as attaining, and does not say what is not.

| Rule | File | Lines |
| --- | --- | --- |
| `s 2(3) the person has attained the age on the date` | rra-part1-preliminary.l4 | 383 |
| `s 7B(1) the previous service is disregarded for the purpose` | rra-part3-re-employment.l4 | 551, 554 |

**Reading (b): a grant or prohibition limited by its own wording does not answer no outside the limit (83 branches, over 78 rules).** Every one answers `NOTHING`. Ruled 2026-11-05 (c): a scope limit with no "only" answers `NOTHING` outside the scope; the limits that are a period or a "where" are in the ruled table above and are not counted here. The other reading, now ruled out for a scope limit: outside the limit the text means no, so each would answer `JUST FALSE` (for a grant, "may ... if the conditions hold" would mean "may not otherwise"; for a duty or bar, "applies to X" would mean "does not apply to anyone else").

| Rule | File | Lines |
| --- | --- | --- |
| `s 3(2) the act is deemed to have been duly performed or exercised by the Commissioner` | rra-part1-preliminary.l4 | 411 |
| `s 4(2) the employer may dismiss the employee on the ground of age before the prescribed minimum retirement age` | rra-part2-minimum-retirement-age.l4 | 36 |
| `s 4(1) the age specified may be the prescribed minimum retirement age` | rra-part2-minimum-retirement-age.l4 | 79 |
| `s 4(3) the employer is guilty of an offence` | rra-part2-minimum-retirement-age.l4 | 95 |
| `s 4(3) the sentence is within the penalty` | rra-part2-minimum-retirement-age.l4 | 110 |
| `s 6 the term is void` | rra-part2-minimum-retirement-age.l4 | 134 |
| `s 7(3) the employer has complied with the duty to give written notice of the intention not to re-employ` | rra-part3-re-employment.l4 | 107, 111 |
| `s 7A(2) a right, privilege, obligation or liability accrued before the specified age is affected` | rra-part3-re-employment.l4 | 257 |
| `s 7A(4) the employer has complied with the requirement to enter into a re-employment contract` | rra-part3-re-employment.l4 | 360 |
| `s 7A(4) the job scope and the terms and conditions may vary from the previous contract` | rra-part3-re-employment.l4 | 375 |
| `s 7A(6) the period of employment stipulated is not less than one year` | rra-part3-re-employment.l4 | 413 |
| `s 7A(9) the eligible employee may retire or be retired` | rra-part3-re-employment.l4 | 462 |
| `s 7A(10) the employee has complied with the duty to give written notice of the intention to retire` | rra-part3-re-employment.l4 | 479, 483 |
| `s 7A(11) the age specified may be the prescribed re-employment age` | rra-part3-re-employment.l4 | 515 |
| `s 7B(2) the previous service is reckoned for the purpose` | rra-part3-re-employment.l4 | 578 |
| `s 7C(2) E1's re-employment obligations survive an unlawful dismissal by E1` | rra-part3-re-employment.l4 | 699 |
| `s 7C(3) the employer is not required to offer an employment assistance payment` | rra-part3-re-employment.l4 | 717 |
| `s 7C(7) the consent form is prima facie proof of the matters mentioned in subsection (1)(b)` | rra-part3-re-employment.l4 | 817 |
| `s 8(1) the employee may make representations in writing to the Minister to be reinstated` | rra-part4-remedies.l4 | 51 |
| `s 8(2) the Minister may direct the Commissioner in writing to inquire and report` | rra-part4-remedies.l4 | 70 |
| `s 8(3) the employer has complied with the direction of the Minister` | rra-part4-remedies.l4 | 108 |
| `s 8(5) the decision of the Minister on the representation is final` | rra-part4-remedies.l4 | 160 |
| `s 8(6) the employee may bring an action for damages in a court in respect of the unlawful dismissal` | rra-part4-remedies.l4 | 175 |
| `s 8(7) the employer is guilty of an offence` | rra-part4-remedies.l4 | 189 |
| `s 8(7) the sentence is within the penalty` | rra-part4-remedies.l4 | 204 |
| `s 8(8) the amount recoverable by the court as if it were a fine` | rra-part4-remedies.l4 | 229 |
| `s 8(9) the Minister may delegate the power` | rra-part4-remedies.l4 | 261 |
| `s 8(10) the delegation is revocable at will` | rra-part4-remedies.l4 | 273 |
| `s 8(10) the delegation prevents the Minister from exercising the power` | rra-part4-remedies.l4 | 285 |
| `s 8(11) the power exercised by the delegate is deemed to have been exercised by the Minister` | rra-part4-remedies.l4 | 299 |
| `s 8A(1) the last day on which the employee can notify the Commissioner of the re-employment dispute` | rra-part4-remedies.l4 | 367 |
| `s 8A(1) the employee notified the Commissioner in time` | rra-part4-remedies.l4 | 377 |
| `s 8A(2) the last day on which the employee can notify the Commissioner of the dismissal` | rra-part4-remedies.l4 | 420 |
| `s 8A(3) the last day on which the employee can submit a mediation request` | rra-part4-remedies.l4 | 466 |
| `s 8B(1) the employee may make representations in writing to the Minister to be re-employed` | rra-part4-remedies.l4 | 531 |
| `s 8B(3) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)` | rra-part4-remedies.l4 | 597 |
| `s 8B(3) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` | rra-part4-remedies.l4 | 616 |
| `s 8B(4) the employee may lodge a claim under section 8C(1) in relation to the matter referred to in section 8A(4)(d)` | rra-part4-remedies.l4 | 635 |
| `s 8B(4) the employee may make representations to the Minister under subsection (1)` | rra-part4-remedies.l4 | 653 |
| `s 8B(5) the Minister may direct the Commissioner to inquire and report` | rra-part4-remedies.l4 | 674 |
| `s 8B(6) the employer has complied with the direction of the Minister` | rra-part4-remedies.l4 | 706 |
| `s 8B(8) the employee submitted the mediation request within the time the Minister determined` | rra-part4-remedies.l4 | 755 |
| `s 8B(9) section 8C(3) applies in relation to the claim` | rra-part4-remedies.l4 | 788 |
| `s 8B(11) the decision of the Minister on the representation is final` | rra-part4-remedies.l4 | 822 |
| `s 8B(12) the employee may bring an action for damages in a court in respect of the denial of re-employment or the dismissal` | rra-part4-remedies.l4 | 838 |
| `s 8B(13) the employer is guilty of an offence` | rra-part4-remedies.l4 | 852 |
| `s 8B(13) the sentence is within the penalty` | rra-part4-remedies.l4 | 867 |
| `s 8B(14) the amount recoverable by the court as if it were a fine` | rra-part4-remedies.l4 | 891 |
| `s 8B(15) the Minister may delegate the power` | rra-part4-remedies.l4 | 924 |
| `s 8B(16) the delegation is revocable at will` | rra-part4-remedies.l4 | 937 |
| `s 8B(16) the delegation prevents the Minister from exercising the power` | rra-part4-remedies.l4 | 949 |
| `s 8B(17) the power exercised by the delegate is deemed to have been exercised by the Minister` | rra-part4-remedies.l4 | 963 |
| `s 8C(1) the employee may lodge a claim for employment assistance payment with an Employment Claims Tribunal` | rra-part4-remedies.l4 | 986 |
| `s 8C(2) the employee may make representations under section 8B(1) in respect of that dismissal` | rra-part4-remedies.l4 | 1004 |
| `s 8C(2) the employee may make representations to the Minister under section 35(3) of the Industrial Relations Act 1960` | rra-part4-remedies.l4 | 1023 |
| `s 8C(3) the Tribunal may take the tripartite guidelines and the employer's steps to re-employ into account` | rra-part4-remedies.l4 | 1038 |
| `s 8C(3) the Tribunal may order any amount of employment assistance payment that it considers just and equitable` | rra-part4-remedies.l4 | 1055 |
| `s 9(1) the person has the power` | rra-part5-general.l4 | 39, 47 |
| `s 9(1)(b) the person examined is bound to state truly the facts and circumstances` | rra-part5-general.l4 | 74 |
| `s 9(1)(c) the Commissioner or investigating officer may require the employer to produce the employee and the documents` | rra-part5-general.l4 | 89 |
| `s 9(1)(g) the Commissioner or investigating officer may require a person to produce the article` | rra-part5-general.l4 | 103 |
| `s 9(2) the person is guilty of an offence` | rra-part5-general.l4 | 121 |
| `s 9(2) the sentence is within the penalty` | rra-part5-general.l4 | 136 |
| `s 9A(1) the person acting may summon the person` | rra-part5-general.l4 | 176, 183 |
| `s 9A(1) the person summoned is legally bound to attend and to answer truthfully` | rra-part5-general.l4 | 202 |
| `s 9A(2) the person is guilty of an offence` | rra-part5-general.l4 | 227 |
| `s 9A(3) the Commissioner or investigating officer may report the failure to a Magistrate, who may issue a warrant to secure the attendance` | rra-part5-general.l4 | 242 |
| `s 9B(1) the person is guilty of an offence` | rra-part5-general.l4 | 259 |
| `s 9B(1) the sentence is within the penalty` | rra-part5-general.l4 | 274 |
| `s 9B(2) the person is guilty of an offence` | rra-part5-general.l4 | 293 |
| `s 9C the sentence is within the penalty` | rra-part5-general.l4 | 327 |
| `s 10(1) the investigating officer may compound the offence` | rra-part5-general.l4 | 354 |
| `s 10(2) further proceedings may be taken against the person in respect of the offence` | rra-part5-general.l4 | 385 |
| `s 11(1) the person is exempt from the provision` | rra-part5-general.l4 | 402 |
| `s 11(2) the Minister may revoke the exemption, vary or revoke its conditions, or impose new conditions` | rra-part5-general.l4 | 414 |
| `s 11A the term is void insofar as it so purports` | rra-part5-general.l4 | 435 |
| `s 11B regard may be had to the guidelines for the purpose` | rra-part5-general.l4 | 459, 466 |
| `s 13 this Act relieves the employer of the duty or liability` | rra-part5-general.l4 | 483 |
<!-- END marginal -->

### Reading a result: FALSE and NOTHING

In this row a `JUST FALSE` is a no that the Act gives in its own words: a definition that says "means" or "has the meaning given by"; "must not", "does not", "shall not" and "operates as a bar"; a list the Act closes with "only" or "means ... any of the following"; a ceiling ("not exceeding"); on reading (a), a "must" or a condition ("if", "no later than") that the facts do not meet; and, by the ruling of 2026-11-05, a period the Act fixes in its own words (outside it) and a "where" condition (when it fails).
A `NOTHING` is "not covered": the Act is silent, lists without closing the list ("such as", "in particular", "includes", "all or any"), leaves a term undefined, points to a Gazette notification, regulation or guideline that is not among the sources, or narrows a grant or prohibition by a scope limit that has no "only" (ruled 2026-11-05 (c)) and the case falls outside the scope.
Each branch says which, in a comment: `-- FALSE-kind (the text says no in its own words): "..."` or `-- NOTHING-kind (<why>)`, where `<why>` is silent, list not closed, includes, undefined term, points outside the text, or limited by its own wording.
A caller must never turn `NOTHING` into `FALSE`: "the Act does not say the employer may" is not "the employer may not", and "the Act does not say" is not "no".
In the seat, "I am not sure" becomes `NOTHING`, and a rule that cannot answer without that fact answers `NOTHING`; if another fact already decides the answer, it answers that.

## What the main binary does not accept

Each item below was measured on 1.6.109 on 5 November 2026, and is marked loud (the binary says so) or silent (it answers, wrongly, with no diagnostic).

- **Loud: a DEONTIC value cannot be the operand of `#ASSERT`.** `#ASSERT <rule> EQUALS FULFILLED` gives `eval/unsupported-equality`, "Trying to check equality on types that do not support it". So each regulative rule here is written twice: as the `PARTY ... MUST/SHANT ... WITHIN ... LEST BREACH BY` rule, run with `#TRACE`, and as a decision function over the same facts, which is asserted. The compensating control is `trace-check.py`: the line before every `#TRACE` reads `-- TRACE-EXPECT: FULFILLED|BREACH|RESIDUAL (why)`, written from the text before the trace was run, and the script runs the file with both main builds and compares each outcome. It reports 2 builds, 54 trace outcomes checked (27 traces), 0 problems. `check.sh` cannot see a trace, because a trace prints no assertion line.
- **Loud: `GIVEN` at section level before a `§` is a parse error** (`parse/unexpected-section-sign`). Every rule carries its own `GIVEN`.
- **Silent: `NOT` binds to everything after it.** `a AND NOT b AND NOT c` reads as `a AND NOT (b AND NOT c)`: with a, b and c true, false and true it answers `TRUE`, where left to right it is `FALSE`. It produced a wrong answer in section 7A(2) here and was caught only by a test. Every `NOT` in the modules is either the whole condition or applied to a parenthesised operand.
- **Loud: a genitive after a parenthesised call is a parse error** (`parse/unexpected-genitive`: `(f x)'s field`). The seat names the value in a `WHERE` and takes the field from the name.
- **Silent: `Date 29 2 2023` rolls forward to 1 March**, and daydate's `add months` clamps 31 January to 28 February. Both are used on purpose and tested (F1, F3).
- **Loud: `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (outside `LEST BREACH ... BECAUSE`)** are not used; "not covered" is `NOTHING`, asserted.
- The skills' `EVERY`, `TYPICALLY`, sets and `AFTER ... WITHIN` are not used; deadlines are day counts (see "Unstable dialect").

## What `check.sh` prints

Run as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh`.
There are no earlier numbers for it to replace: this is a fresh row.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
rra-cases-seat.l4                              0       228       0        0         0 |      0       228       0        0  same
rra-logic.l4                                   0         0       0        0         0 |      0         0       0        0  same
rra-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
rra-part1-preliminary.l4                       0         0       0        0         0 |      0         0       0        0  same
rra-part2-minimum-retirement-age.l4            0         0       0        0         0 |      0         0       0        0  same
rra-part3-re-employment.l4                     0         0       0        0         0 |      0         0       0        0  same
rra-part4-remedies.l4                          0         0       0        0         0 |      0         0       0        0  same
rra-part5-general.l4                           0         0       0        0         0 |      0         0       0        0  same
rra-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
rra-tests-part1.l4                             0        82       0        0         0 |      0        82       0        0  same
rra-tests-part2.l4                             0        33       0        0         0 |      0        33       0        0  same
rra-tests-part3.l4                             0       147       0        0         0 |      0       147       0        0  same
rra-tests-part4.l4                             0       168       0        0         0 |      0       168       0        0  same
rra-tests-part5.l4                             0        84       0        0         0 |      0        84       0        0  same
TOTAL (14 modules)                             0       742       0        0           |      0       742       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Unstable dialect

Looked at: time (deadlines counted from events), versions, and workarounds.
These shapes are present.
Every deadline in the Act that runs from an event is written on main as a day count, `WITHIN (Day <last day> MINUS Day <the day the clock starts>)`, with the clock-start date as an input and the last day worked out with daydate `add months` or `add years`: ss 7A(1) (the offer before the specified age), 7C(4)(a) (the lump sum by the last day of employment), 8A(1) to (3) and 8B(2) (one and six months from an event), 8B(8) (a time the Minister fixes) and 9A(1) (attendance at the time in a summons).
Main rejects the `AFTER ... WITHIN` window (the dialect guide, `dialects.md`, row `AFTER 3 WITHIN 30`), so the one earliest edge in the Act, the "at any time after" a conciliation of section 8B(1), is a decision function and not a window on a rule.
The Act's version history (the text is the version in force from 1 July 2022) is not modelled as rule versions.
No second, unstable encoding was written.
I did not test whether the unstable dialect would express these deadlines better than the workaround.

## Before this encoding is worth relying on

- A lawyer who knows Singapore employment law should read the marginal readings above and rule on readings (a) and (c) and on forks F3, F11, F13 and F23, which decide the dates and the places where a clause could be a period, a "where" or a scope limit.
- The Gazette notifications that fix the ages, the regulations, the tripartite guidelines and the borrowed Acts should be added, so the ages and the borrowed terms stop being inputs.
- The text is a converter rendering; it should be checked against the official text on Singapore Statutes Online, which this encoding does not do.
- No domain expert has reviewed the seat's wording against what an employee would ask.
