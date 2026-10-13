# ind-b: expectations decided from the sources alone

Written 2026-10-13, BEFORE opening any `gN-*.l4`, any `FRAGMENT-G*.md`, or any file in `phase1/` other than `ASSIGN-IND-B.md`.
Scope: ss. 19 to 40 (Chapters 4 and 5), ss. 58 to 63 (Chapter 7), and the Fourth Schedule.

Sources read: `inputs/law.wiki` (lines 157-338, 434-464, 728-1016); the gazette page images of `sefer-hachukim-3349-pp182-209.pdf` (PDF pages 6-13 = printed pp. 186-193, 16-18 = pp. 196-198, 26-28 = pp. 206-208; PDF page 1 is the unnumbered cover, so the file actually holds the cover plus pp. 182-208); `kovetz-hatakanot-11951-p2116.txt`; `regulations-fees.wiki`; `interpretation-NOTES.md` ss. 0.1, 3, 4; the export list of `il-interpretation-time.l4`.

Conventions:

- "IL s.10(b)" is the Interpretation Law's rule: N months or years after an event ends on the same-numbered day of the month (or that month's last day if it lacks the day); that last day is inside the period (interpretation-NOTES F1, F25).
- A commencement "N months from day D" is taken to fall ON the last day of the IL s.10 period (the convention the Fees Regulations' own editorial note uses: published 9.7.2025, "7 days from publication", commencement 16.7.2025).
- Fleet default (BRIEF ruling 4): IL s.10(c) not applied to a period of validity (V) or a commencement (C). I agree with that default for the cases below and test it.
- "MAY" = the act is authorised on these facts; "MUST" = a duty arises; "FALSE" for a MAY means the act is not authorised on these facts.
- Discretions and judgements (unfit "by its nature, gravity or circumstances", "satisfaction of the Minister") are inputs, stated in the scenario.

Gazette check of every number in scope (read from the page images, not the wiki): s.20 "בת 11 חברים" and eleven numbered seats (1)-(11); s.22 "ארבע שנים"; s.23(c) "משלוש ישיבות רצופות", "מיותר ממחצית הישיבות", "במהלך שנה אחת"; s.24 and s.25(a) "רוב חבריה ובהם יושב ראש המועצה"; s.29(e) "סעיף 20(7) עד (11)"; s.63(a)(1) "שלושה חודשים", (a)(2) "18 חודשים", (b) "18 חודשים"; Fourth Schedule items (1)-(95).
All agree with the wiki except **Fourth Schedule item (66): the gazette prints `E170` (text layer `E170`, image `E170`); the wiki has `170E`.** `E170` is the ASHRAE designation of dimethyl ether (R-E170); `170E` is not a designation. The gazette governs.

Dates: the Law was published in Sefer HaChukim 3349 on **2025-01-14** (cover and every page footer). The s.59 Fees Regulations were published 2025-07-09 (Kovetz HaTakanot 11951) and commence "7 days from publication" (reg. 5) = **2025-07-16** (IL s.10(a)).

## s.19 the Registrar (9 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| R19-1 | Minister appoints a Ministry (Labour) employee as Registrar | eligible: TRUE | 19(a) |
| R19-2 | appointee is not a Ministry employee | eligible: FALSE | 19(a) |
| R19-3 | appointment made, notice not published in Reshumot | publication duty unmet (a duty exists to publish) | 19(a) |
| R19-4 | a study programme (incl. supplementary studies) leading to a completion certificate, Registrar has not consented | programme may not serve for s.6(a)(4): FALSE | 19(b) |
| R19-5 | same, Registrar consented | TRUE | 19(b) |
| R19-6 | foreign certificate; Registrar consulted the Council; scope and content match s.6(a)(4) | Registrar MAY recognise: TRUE | 19(c)(1) |
| R19-7 | same, Council not consulted | FALSE | 19(c)(1) |
| R19-8 | Council consulted, scope/content do not match | FALSE | 19(c)(1) |
| R19-9 | recognition conditioned on a professional exam / on training studies / on both | each permitted: TRUE (three cases) | 19(c)(2) |

## s.20 Council composition (5 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C20-1 | size of the Council | 11 | 20 |
| C20-2 | number of seats listed | 11 (matches the stated size) | 20(1)-(11) |
| C20-3 | who chairs | the seat (1) member, representative of the Ministry's senior division for occupational regulation | 20(1) |
| C20-4 | the Registrar | is a member, seat (2) | 20(2) |
| C20-5 | seat (4) member appointed without the Energy Minister's proposal | appointment not per s.20: FALSE (same for seat 5 / Env. Protection Minister, seat 6 / Fire Commissioner) | 20(4)-(6) |

## s.21 bar to appointment (7 scenarios)

The unfitness judgement ("מפאת מהותה, חומרתה או נסיבותיה אין הוא ראוי") is an input.

| id | facts | expected (barred?) | provision |
| --- | --- | --- | --- |
| C21-1 | convicted of a criminal offence, judged unfitting | TRUE | 21 |
| C21-2 | convicted, judged NOT unfitting | FALSE | 21 |
| C21-3 | indictment pending for an unfitting offence, no final judgment | TRUE | 21 |
| C21-4 | indicted, final judgment given (acquitted) | FALSE | 21 |
| C21-5 | disciplinary complaint (קובלנה) pending, unfitting, no final judgment | TRUE | 21 |
| C21-6 | convicted of a disciplinary offence, unfitting | TRUE | 21 |
| C21-7 | clean record | FALSE | 21 |

## s.22 term of office (7 scenarios)

Kind V (validity): IL s.10(c) not applied (fleet default; I agree).

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C22-1 | member (not Registrar) appointed 2025-03-01 | last day of term 2029-03-01; serving on 2029-03-01 TRUE; on 2029-03-02 FALSE | 22, IL s.10(b) |
| C22-2 | appointed 2024-02-29 | last day 2028-02-29 | 22, IL s.10(b) |
| C22-3 | appointed 2096-02-29 | last day 2100-02-28 (2100 is not a leap year) | 22, IL s.10(b) |
| C22-4 | the Registrar | no four-year term (excepted) | 22 |
| C22-5 | appointed 2025-03-01, 2029-03-01 is a rest day | last day still 2029-03-01 | 22, fleet default |
| C22-6 | Minister extends | MAY: TRUE, no precondition; repeatable ("לתקופות כהונה נוספות") | 22 |
| C22-7 | one extension of a term that ended 2029-03-01 | AMBIGUOUS: extension length. Reading A: a further term of four years, last day 2033-03-01. Reading B: whatever the Minister fixes | 22 |

## s.23 ending a term early (22 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C23-1 | resignation letter delivered to the Minister | ceases: TRUE | 23(a)(1) |
| C23-2 | resignation letter delivered only to the Chair | does not cease under (a)(1): FALSE | 23(a)(1) |
| C23-3 | seat (4) ministry employee leaves that ministry | ceases: TRUE | 23(a)(2) |
| C23-4 | seat (8) representative ceases to be a member of the employers' organisation | ceases: TRUE | 23(a)(2) |
| C23-5 | seat (11) public representative appointed a state employee | ceases: TRUE | 23(a)(2) |
| C23-6 | public representative, nothing happened | continues: (ceases) FALSE | 23(a) |
| C23-7 | convicted of an unfitting offence; written hearing given | Minister MUST remove: TRUE | 23(b)(1), (d) |
| C23-8 | indictment filed for an unfitting offence; hearing given | MUST remove: TRUE | 23(b)(1), (d) |
| C23-9 | permanently incapacitated; hearing given | MUST remove: TRUE | 23(b)(2), (d) |
| C23-10 | temporarily incapacitated only | no (b) ground: FALSE | 23(b)(2) |
| C23-11 | ceased to satisfy a condition of appointment (e.g. now frequently in conflict, s.29(b)); hearing given | MUST remove: TRUE | 23(b)(3), (d) |
| C23-12 | (b) ground present but no written hearing yet | may not terminate yet: FALSE | 23(d) |
| C23-13 | 3 consecutive unjustified absences; Chair consulted; hearing given | MAY remove: TRUE | 23(c), (d) |
| C23-14 | 2 consecutive unjustified absences, 2 of 10 meetings that year | FALSE | 23(c) |
| C23-15 | absent unjustified from 6 of 10 meetings in one year, never 3 in a row | TRUE (more than half) | 23(c) |
| C23-16 | absent unjustified from 5 of 10 | FALSE (exactly half is not more than half) | 23(c) |
| C23-17 | absent unjustified from 5 of 9 | TRUE | 23(c) |
| C23-18 | 3 consecutive absences, all with justified reason | FALSE | 23(c) |
| C23-19 | 3 consecutive unjustified; Chair NOT consulted | FALSE | 23(c) |
| C23-20 | 3 consecutive unjustified; Chair consulted; no hearing | FALSE | 23(d) |
| C23-21 | absent from 6 of 10, of which 2 justified (4 unjustified), no 3 unjustified in a row | FALSE on my reading ("בלא סיבה מוצדקת" governs both limbs); AMBIGUOUS, other reading TRUE | 23(c) |
| C23-22 | a member ceased under s.23 | Minister MUST appoint a replacement under s.20 as soon as possible: TRUE | 23(e) |

## s.24 validity of acts (5 scenarios)

"רוב חבריה" = a majority of the eleven seats, i.e. at least 6. s.24's own wording ("provided a majority of its members are serving") only makes sense with the full complement as the base.

| id | facts | expected (acts unaffected?) | provision |
| --- | --- | --- | --- |
| C24-1 | 6 of 11 serving incl. the Chair | TRUE | 24 |
| C24-2 | 5 serving incl. the Chair | FALSE | 24 |
| C24-3 | 6 serving, Chair's seat vacant | FALSE | 24 |
| C24-4 | 11 serving, one appointment defective | TRUE | 24 |
| C24-5 | 7 serving incl. Chair | TRUE | 24 |

## s.25 procedure (16 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C25-1 | 6 present incl. Chair | quorum TRUE | 25(a) |
| C25-2 | 5 present incl. Chair | quorum FALSE | 25(a) |
| C25-3 | 6 present, Chair absent | quorum FALSE | 25(a) |
| C25-4 | 11 present | quorum TRUE | 25(a) |
| C25-5 | only 9 seats filled, 5 present incl. Chair | quorum FALSE on my reading (base is 11); AMBIGUOUS, a "serving members" base gives TRUE | 25(a) |
| C25-6 | 4 for, 3 against | adopted | 25(b) |
| C25-7 | 3 for (Chair among them), 3 against | adopted (Chair decides the tie) | 25(b) |
| C25-8 | 3 for, 3 against (Chair among the against) | rejected | 25(b) |
| C25-9 | 3 for, 4 against | rejected | 25(b) |
| C25-10 | 3 for, 2 against, 2 abstain | adopted (majority of those voting) | 25(b) |
| C25-11 | 2 for, 2 against, Chair present and abstains | AMBIGUOUS: source does not say; REFUSE is the honest answer | 25(b) |
| C25-12 | 3 present incl. Chair, all 11 duly summoned | may discuss in partial composition: TRUE | 25(c) |
| C25-13 | 3 present incl. Chair, not all summoned | FALSE | 25(c) |
| C25-14 | 8 present, all summoned, Chair absent | FALSE | 25(a), (c) |
| C25-15 | 3 present incl. Chair, all summoned: may it DECIDE? | AMBIGUOUS (tension (a) v (c)): (a) gives no quorum, (c) allows discussion with only the Chair present | 25(a), (c) |
| C25-16 | engage advisers and experts | MAY: TRUE | 25(d) |

## s.26 functions and sub-committees (5 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C26-1 | delegate its powers on individual applications ((a)(3)) to a sub-committee | MAY: TRUE | 26(b) |
| C26-2 | delegate its policy-advice powers ((a)(2)) | FALSE (sub-committees may only advise it) | 26(b) |
| C26-3 | delegate advice to the Minister on exemptions ((a)(1)) | FALSE | 26(b) |
| C26-4 | appoint a non-member to a sub-committee | MAY: TRUE | 26(b) |
| C26-5 | advising the Registrar on an individual extension of validity (s.17(c)) | is a Council function: TRUE | 26(a)(3) |

## s.27 remuneration and expenses (6 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C27-1 | seat 11 public representative, self-employed | payment for meetings: not entitled; travel reimbursement: entitled | 27(a) |
| C27-2 | state employee (seat 4) | reimbursement: not entitled | 27(b) |
| C27-3 | employee of a budgeted body | reimbursement: not entitled | 27(b) |
| C27-4 | employee of a supported body (גוף נתמך) representing another organisation | reimbursement: not entitled (outside (a)'s class; (b) does not name supported bodies but (a) is the only grant) | 27(a) |
| C27-5 | seat 8 representative employed by the employers' organisation he represents (not a state/budgeted/supported body) | reimbursement: not entitled ((b) carves him out of (a)) | 27(b) |
| C27-6 | seat 7 representative, employed by an unrelated private firm | reimbursement: entitled | 27(a) |

## s.28 laws applied to Council members (2 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C28-1 | non-state-employee member, for each of: Gifts Law, Penal Law (public servants), Post-Retirement Restrictions Law, Party Activity Law, Evidence Ordinance (public servant certificate), Knesset Elections Law | treated as a state employee: TRUE (six laws) | 28(1)-(6) |
| C28-2 | same member, another law (e.g. State Service (Discipline) Law) | FALSE | 28 |

## s.29 conflict of interest (31 scenarios)

"Family member" ((a)): TRUE for spouse, parent, grandparent, child, child's spouse, sibling, sibling's child, brother- or sister-in-law, uncle/aunt, cousin (uncle's or aunt's child), each parent-in-law form (חותן, חותנת, חם, חמות), grandchild, a step-relative of any of these.
FALSE for great-grandparent, grandchild's spouse, sibling's child's spouse, cousin's child, great-uncle, spouse's grandparent. (19 scenarios: 13 TRUE, 6 FALSE.)

"Relative" ((a)): TRUE for (2) a person in whose economic situation the member has an interest; (3) a corporation in which the member, a family member or a (2)-person is an interested party; (4) a body in which any of them is a manager or responsible employee. FALSE for a corporation in which a mere friend (no economic interest) is an interested party. (4 scenarios.)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| C29-1 | candidate whose office will frequently put him in a conflict preventing the core of his role | may not be appointed nor serve: TRUE | 29(b) |
| C29-2 | member must not handle (incl. attend a discussion of) a matter that puts him in conflict | prohibition: TRUE | 29(c) |
| C29-3 | member (not Chair) learns he may be in conflict | MUST notify the Chair as soon as possible | 29(d) |
| C29-4 | the Chair learns it | MUST notify the Minister | 29(d) |
| C29-5 | seat 8 representative weighs the employers' interests, related to Council functions | not in conflict for that alone: TRUE | 29(e) |
| C29-6 | seat 3 (Economy Ministry) member weighs a public's interests | (e) does not apply | 29(e) |
| C29-7 | seat 8 representative weighs an interest unrelated to Council functions | (e) does not protect | 29(e) |
| C29-8 | seat 8 representative whose brother's company would benefit | conflict (a relative's interest, not the represented public's) | 29(a), (c), (e) |

## s.30 inspectors (8 scenarios)

| id | facts | expected (may be authorised?) | provision |
| --- | --- | --- | --- |
| I30-1 | Ministry employee, no unfitting conviction, trained as directed, meets additional conditions | TRUE | 30(a), (b) |
| I30-2 | not a Ministry employee | FALSE | 30(a) |
| I30-3 | convicted, Minister judges unfitting | FALSE | 30(b)(1) |
| I30-4 | criminal proceedings PENDING, no conviction, all else met | TRUE: (b)(1) speaks only of conviction (contrast ss. 35(2), 36(b)(1)) | 30(b)(1) |
| I30-5 | training missing | FALSE | 30(b)(2) |
| I30-6 | additional conditions missing | FALSE | 30(b)(3) |
| I30-7 | notice of authorisation | must be published in Reshumot | 30(c) |
| I30-8 | inspector authorised for only some powers | may use only those | 30(a) |

## s.31 inspection powers (10 scenarios)

All with s.32 met and on duty.

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I31-1 | demand name, address, ID from any person (a bystander) | MAY | 31(1) |
| I31-2 | demand documents from a person concerned | MAY | 31(2) |
| I31-3 | demand documents from a person not concerned | FALSE | 31(2) |
| I31-4 | enter a non-residential place with grounds to suspect unlicensed work | MAY | 31(3) |
| I31-5 | same, grounds that an operator employs someone unlicensed | MAY | 31(3) |
| I31-6 | same, grounds that a licensee works outside his licence conditions | MAY | 31(3) |
| I31-7 | enter without grounds | FALSE | 31(3) |
| I31-8 | residence, grounds, no court order, no occupier consent | FALSE | 31(3) |
| I31-9 | residence, grounds, court order | MAY | 31(3) |
| I31-10 | residence, grounds, occupier consents | MAY | 31(3) |

## s.32 identification (5 scenarios)

| id | facts | expected (may use powers?) | provision |
| --- | --- | --- | --- |
| I32-1 | on duty, visible badge, certificate signed by the Minister | TRUE | 32 |
| I32-2 | badge not visible | FALSE | 32(1) |
| I32-3 | certificate signed by someone other than the Minister | FALSE | 32(2) |
| I32-4 | not in the course of his duties | FALSE | 32 |
| I32-5 | certificate held but refused when demanded | FALSE (must show on demand) | 32(2) |

## ss.33-34 senior inspector, testing bodies and experts (7 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I34-1 | senior inspector chosen from among the inspectors | eligible TRUE | 34(a) |
| I34-2 | a Ministry employee who is not an inspector | FALSE | 34(a) |
| I34-3 | senior inspector relies on findings of a tester's auxiliary test / an expert's findings and opinion | MAY | 34(b) |
| I34-4 | an ordinary inspector relies on them | FALSE (Sign B powers are the senior inspector's) | 34(a), (b) |
| I34-5 | contract with a testing body or expert | must follow the Mandatory Tenders Law | 34(c) |
| I34-6 | testing body's report signed by its manager / only by the tester | compliant / not compliant | 34(d) |
| I34-7 | expert's report and opinion signed by the expert | compliant; an expert employed by a testing body is allowed | 34(c), (e) |

## s.35 testing body (9 scenarios)

| id | facts | expected (may serve?) | provision |
| --- | --- | --- | --- |
| I35-1 | Israeli-incorporated and registered company, clean, staffing proved to the Minister's satisfaction, no conflict, tender conditions met | TRUE | 35 |
| I35-2 | incorporated abroad | FALSE | 35(1) |
| I35-3 | an officer has pending criminal proceedings on suspicion of an unfitting offence | FALSE | 35(2) |
| I35-4 | a controlling holder convicted of an unfitting offence | FALSE | 35(2) |
| I35-5 | an officer convicted of an offence judged NOT unfitting | TRUE | 35(2) |
| I35-6 | staffing not proved | FALSE | 35(3) |
| I35-7 | an officer may be in an indirect conflict | FALSE | 35(4) |
| I35-8 | tender set an extra condition, not met | FALSE | 35(5) |
| I35-9 | no extra condition was set | (5) satisfied: TRUE | 35(5) |

## s.36 authorising testers and experts (9 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I36-1 | meets the s.60(1)(c) conditions, no conviction, nothing pending, no conflict | Minister shall authorise (subject to (c)): TRUE | 36(a), (b) |
| I36-2 | pending criminal proceeding, no conviction | barred: may not authorise | 36(b)(1) |
| I36-3 | convicted, Minister judges unfitting | barred | 36(b)(1) |
| I36-4 | may be in an indirect conflict | barred | 36(b)(2) |
| I36-5 | does not meet the regulation conditions | may not authorise | 36(a) |
| I36-6 | refusal despite conditions met, with reasons, after written hearing, on a finding of unfitness | refusal permitted: TRUE | 36(c) |
| I36-7 | refusal without hearing, or without reasons | not permitted: FALSE | 36(c) |
| I36-8 | change of working conditions after hearing / without | permitted / not | 36(d) |
| I36-9 | authorisation stated for 2 years from 2025-11-01 | in force 2027-11-01 TRUE, 2027-11-02 FALSE (V, no IL s.10(c)) | 36(e), IL s.10(b) |

## s.37 testers' and experts' actions (13 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I37-1 | non-residence; SENIOR INSPECTOR has grounds; authorisation shown; written consent; prior explanation of purpose and of the right to refuse and withdraw | may enter: TRUE | 37(a)(1), (b)(1)-(3) |
| I37-2 | only the tester has grounds, senior inspector has none | FALSE | 37(a)(1) |
| I37-3 | consent only oral | FALSE | 37(b)(2) |
| I37-4 | no explanation before consent | FALSE | 37(b)(3) |
| I37-5 | authorisation not shown | FALSE | 37(b)(1) |
| I37-6 | residence; (1)-(3) met; occupier requested; prior coordination | TRUE | 37(b)(4) |
| I37-7 | residence; (1)-(3) met; not at occupier's request | FALSE | 37(b)(4) |
| I37-8 | residence; requested; no prior coordination | FALSE | 37(b)(4) |
| I37-9 | court order instead of consent | FALSE (no warrant route for testers) | 37(b) |
| I37-10 | demand ID from the person performing HVAC work / from a bystander | MAY / FALSE | 37(a)(2) |
| I37-11 | receive documents listed in the checklist / not listed | MAY / FALSE | 37(a)(4) |
| I37-12 | conduct tests on the system | MAY | 37(a)(5) |
| I37-13 | checklist incl. list of official documents | must be published in Reshumot and on the Ministry website | 37(a)(3) |

## s.38 information security (5 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I38-1 | contracted testing body / expert | MUST secure the information | 38(a) |
| I38-2 | contract ended | MUST transfer information to the senior inspector | 38(b) |
| I38-3 | information remaining after transfer | MUST destroy it and notify the senior inspector | 38(b) |
| I38-4 | use or disclose information for performing the contracted action | permitted | 38(c) |
| I38-5 | tester discloses to a third party for another purpose | prohibited | 38(c) |

## s.39 cancelling or suspending an authorisation (13 scenarios)

| id | facts | expected (may cancel/suspend?) | provision |
| --- | --- | --- | --- |
| I39-1 | granted on false information; hearing given | TRUE | 39(a)(1) |
| I39-2 | granted on erroneous information; hearing | TRUE | 39(a)(1) |
| I39-3 | granted on PARTIAL (incomplete) information only; hearing | FALSE (s.39(a)(1) says only "כוזב או שגוי"; contrast s.10(a)(1)) | 39(a)(1) |
| I39-4 | any ground, no hearing | FALSE | 39(a) |
| I39-5 | s.36 condition ceased; hearing; no prior demand to comply | FALSE | 39(b) |
| I39-6 | same; demand made; not complied within the time set | TRUE | 39(b) |
| I39-7 | same; demand made; complied | FALSE | 39(b) |
| I39-8 | condition ceased, impossible to fulfil; hearing; no demand | TRUE | 39(b) |
| I39-9 | breach of a condition of authorisation; hearing; no demand | FALSE | 39(a)(3), (b) |
| I39-10 | breach; hearing; demand unmet | TRUE | 39(a)(3), (b) |
| I39-11 | special circumstances of unfitness; hearing; no demand | TRUE (no demand needed) | 39(a)(4) |
| I39-12 | work not at an adequate professional level; hearing; no demand | TRUE | 39(a)(5) |
| I39-13 | suspension for 5 years | permitted (period set by the Minister, no cap; contrast s.10(a)'s three years) | 39(a) |

## s.40 laws applied to testers and experts (2 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| I40-1 | Gifts Law, Penal Law (public servants), Post-Retirement Restrictions Law | treated as state employees: TRUE | 40(1)-(3) |
| I40-2 | Knesset Elections Law, Party Activity Law, Evidence Ordinance | FALSE (those are s.28 only) | 40 |

## s.58 electrical work (4 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| M58-1 | holder of an HVAC licence (any grade) | deemed an electrician-service licence holder for HVAC systems: TRUE | 58 |
| M58-2 | same, for electrical work not on an HVAC system | FALSE | 58 |
| M58-3 | no HVAC licence | FALSE | 58 |
| M58-4 | temporary grade 3 licence of a foreign expert (s.9) | TRUE (it is a licence under this Law) | 58, 9 |

## s.59 fees power (7 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| M59-1 | fee for submitting a licence application, with Labour and Welfare Committee approval | MAY | 59 |
| M59-2 | same, without committee approval | FALSE | 59 |
| M59-3 | fee for granting or renewing a licence (approved) | MAY | 59 |
| M59-4 | fee for exams for a completion certificate, incl. objection (approved) | MAY | 59 |
| M59-5 | fee for s.17 training (approved) | MAY | 59 |
| M59-6 | different rates for a foreign expert's temporary licence application, renewal, grant (approved) | MAY | 59 |
| M59-7 | fee for a registry search (s.11(b)) or an exemption request (s.7) | not authorised by s.59: FALSE | 59 |

## s.60 implementation and regulations (7 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| M60-1 | regulations on training requirements (1)(a), with committee approval | MAY | 60(1)(a) |
| M60-2 | same, without approval | FALSE | 60(1) |
| M60-3 | exam rules (1)(b), approved | MAY | 60(1)(b) |
| M60-4 | tester/expert conditions (1)(c), approved, relevant Minister consulted | MAY | 60(1)(c) |
| M60-5 | (1)(c) approved, relevant Minister NOT consulted | FALSE | 60(1)(c) |
| M60-6 | manner of applying for a licence or renewal, incl. renewal deadline (2)(a), no committee approval | MAY | 60(2)(a) |
| M60-7 | manner of applying for a foreign expert's temporary licence (2)(b), no approval | MAY | 60(2)(b) |

## ss.61-62

Amendments to the Electricity Law (adds s.6(e)) and to the Administrative Courts Law (adds item (31) to First Schedule item 21). Out of scope per the brief; nothing to compute in this Law. 0 scenarios.

## s.63 commencement (24 scenarios)

**Reading A (taken): "שלושה חודשים מיום פרסומו או מועד כניסתן לתוקף של תקנות לפי סעיף 59, לפי המאוחר" = three months from the LATER of (publication day, s.59 regulations' commencement).**
The one preposition "מ" governs both nouns; s.63(b) shows how the drafter writes the other reading ("18 חודשים מיום התחילה **או במועד** כניסתן לתוקף", with "ב").
**Reading B (ambiguous alternative): the later of (three months from publication) and (the regulations' commencement day).**

With the actual dates (publication 2025-01-14, regulations 2025-07-16):

| id | facts | Reading A | Reading B | provision |
| --- | --- | --- | --- | --- |
| K63-1 | the commencement day ("יום התחילה") | 2025-10-16 | 2025-07-16 | 63(a)(1) |
| K63-2 | work on a system using a listed flammable refrigerant (290) whose use is lawful, on 2025-10-16 | commenced TRUE | TRUE | 63(a)(1) |
| K63-3 | same, on 2025-10-15 | FALSE | TRUE | 63(a)(1) |
| K63-4 | same, on 2025-07-16 | FALSE | TRUE | 63(a)(1) |
| K63-5 | same, on 2025-07-15 | FALSE | FALSE | 63(a)(1) |
| K63-6 | the date for other refrigerants (e.g. 410A) | 2027-04-16 | 2027-01-16 | 63(a)(2) |
| K63-7 | 410A system on 2027-04-16 / 2027-04-15 | TRUE / FALSE | TRUE / TRUE | 63(a)(2) |
| K63-8 | 410A system on 2025-10-16 | FALSE | FALSE | 63(a)(2) |
| K63-9 | listed refrigerant whose use is NOT permitted by law (e.g. 1270 assumed unlawful): which date | (a)(2): 2027-04-16 ("קרר שאינו כאמור בפסקה (1)") | 2027-01-16 | 63(a)(1)-(2) |
| K63-10 | rest day supplied on 2025-10-16 and on 2027-04-16 | dates unmoved (C, no IL s.10(c)) | - | fleet default |
| K63-11 | Chapter 6, s.46 regulations never made (NOTHING), on 2030-01-01 | not commenced: FALSE | FALSE | 63(b) |
| K63-12 | Chapter 6, s.46 regulations in force 2026-01-01: on 2027-04-16 / 2027-04-15 | TRUE / FALSE | (2027-01-16) | 63(b) |
| K63-13 | Chapter 6, s.46 regulations 2028-01-01: on 2028-01-01 / 2027-12-31 / 2027-06-01 | TRUE / FALSE / FALSE | same | 63(b) |
| K63-14 | Chapter 6, s.46 regulations 2027-04-16 | commences 2027-04-16 | 2027-04-16 | 63(b) |
| K63-15 | Chapter 6 does not depend on the refrigerant | same answer for 290 and 410A | | 63(a) "למעט פרק ו׳", (b) |
| K63-16 | Chapter 6 on 2027-04-16 with a rest day there | unmoved | | fleet default |

Hypothetical regulation dates (publication fixed at 2025-01-14), each side of the "later of":

| id | regulations in force | Reading A day | Reading B day | (a)(2) day under A |
| --- | --- | --- | --- | --- |
| K63-17 | 2025-01-01 (before publication) | 2025-04-14 | 2025-04-14 | 2026-10-14 |
| K63-18 | 2025-03-01 (between publication and +3 months) | 2025-06-01 | 2025-04-14 | 2026-12-01 |
| K63-19 | 2025-04-14 (exactly +3 months) | 2025-07-14 | 2025-04-14 | 2027-01-14 |
| K63-20 | 2025-11-30 | 2026-02-28 (February lacks the 30th) | 2025-11-30 | 2027-08-28 |
| K63-21 | 2025-01-14 (same day as publication) | 2025-04-14 | 2025-04-14 | 2026-10-14 |

| id | facts | expected | provision |
| --- | --- | --- | --- |
| K63-22 | Minister amends the Fourth Schedule by order after consulting the Minister of Environmental Protection | MAY: TRUE | 63(a)(1) |
| K63-23 | same, without that consultation | FALSE | 63(a)(1) |
| K63-24 | same, consulted, no Knesset committee approval | MAY: TRUE (none required, unlike ss. 3(c), 6(b), 41(b)) | 63(a)(1) |

Unanswered by the source: when Chapters 4 and 5 (the Registrar, the Council, inspection) commence. s.63(a) commences the Law "for the purposes of work on a system operating with" a given refrigerant, and those chapters are not about any one refrigerant. Expected: AMBIGUOUS (probably "יום התחילה", the earlier date).

## Fourth Schedule (99 scenarios)

| id | facts | expected | provision |
| --- | --- | --- | --- |
| S4-1..95 | each of the 95 designations as printed in the gazette: 440A, 1132a, 142b, 152a, 403A, 406A, 411A, 411B, 412A, 413A, 415A, 415B, 418A, 419A, 419B, 439A, 462A, 465A, 512A, 32, 1234yf, 1234ze(E), 143a, 444A, 444B, 445A, 446A, 447A, 447B, 451A, 451B, 452B, 454A, 454B, 454C, 455A, 457A, 459A, 459B, 516A, 50, 170, 290, 600, 601, 702, 1150, 1270, 429A, 430A, 431A, 432A, 433A, 433B, 433C, 435A, 436A, 436B, 436C, 441A, 443A, 510A, 511A, 600a, 601a, **E170**, 40, 611, 1130(E), 717, 1132(E), 454D, 455B, 455C, 457B, 457C, 457D, 467A, 468A, 468B, 468C, 474A, 474B, 475B, 477A, 477B, 478A, 479A, 483A, 484A, 487A, 488A, 489A, 490A, 491A | listed: TRUE | Sch. 4 (1)-(95) |
| S4-96 | count | 95 distinct designations | Sch. 4 |
| S4-97 | `170E` (the wiki's spelling of item 66) | not a gazette designation; the gazette's `E170` is listed | Sch. 4 (66) |
| S4-98 | non-listed: 134a, 410A, 744, 22, 404A, 407C, 1234ze(Z), 152 | not listed: FALSE | Sch. 4 |
| S4-99 | 600a and 600 both listed; 601a and 601 both listed | TRUE, distinct items (44)/(64), (45)/(65) | Sch. 4 |

## Totals decided before opening the encoding

| section / schedule | scenarios |
| --- | --- |
| s.19 | 9 |
| s.20 | 5 |
| s.21 | 7 |
| s.22 | 7 |
| s.23 | 22 |
| s.24 | 5 |
| s.25 | 16 |
| s.26 | 5 |
| s.27 | 6 |
| s.28 | 2 |
| s.29 | 31 |
| s.30 | 8 |
| s.31 | 10 |
| s.32 | 5 |
| ss.33-34 | 7 |
| s.35 | 9 |
| s.36 | 9 |
| s.37 | 13 |
| s.38 | 5 |
| s.39 | 13 |
| s.40 | 2 |
| s.58 | 4 |
| s.59 | 7 |
| s.60 | 7 |
| ss.61-62 | 0 |
| s.63 | 24 |
| Fourth Schedule | 99 |
| **total** | **347** |

## Ambiguities (both answers written; these go to `ind-b-tests-ambiguous.l4` where testable)

1. s.63(a)(1): three months from the later of the two dates (A) v. the later of three months from publication and the regulations' date (B). Discriminating: actual dates, 2025-10-16 v 2025-07-16.
2. s.63(a)(1) proviso: a listed flammable refrigerant whose use is not lawful falls under (a)(2) (literal), or is outside the commencement scheme.
3. s.63: the commencement of Chapters 4 and 5 is not stated.
4. s.63(b) with s.46 regulations never made: not commenced (my answer), or a refusal.
5. s.22: the length of an extension.
6. s.23(c): whether justified absences count toward "more than half".
7. s.23(b)(1) v s.21: indictment then acquittal. s.21 no longer bars; s.23(b)(1)'s literal "הוגשו נגדו כתב אישום" still names a ground.
8. s.25(a) v (c): (a) requires a quorum of 6 incl. the Chair; (c) lets the Council "discuss" with only the Chair present if all were summoned. Whether a decision can be taken at such a sitting.
9. s.25(a)/s.24: majority of 11 seats v of members serving.
10. s.25(b): a tie when the Chair abstains.
