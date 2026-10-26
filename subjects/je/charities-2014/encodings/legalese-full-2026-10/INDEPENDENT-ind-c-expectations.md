# ind-c expectations, decided from the Law alone

Started 2026-10-26T16:06:43Z (UTC), before any module of the deposit, any FRAGMENT-G*.md, `domain.l4` or any file of `phase1/` other than `ASSIGN-IND-C.md` was opened or listed.
Sources read: `BRIEF.md`; `inputs/charities-jersey-law-2014-2026-10-02.txt` (whole); the PDF text layer for Arts 5-7 and 26 to the end of the endnotes (lines 440-600, 1515-2235); `inputs/amending/` R&O.17/2018, R&O.56/2025, R&O.136/2019, R&O.40/2019 (whole), and the Charities passages of R&O.29/2021, R&O.28/2023, R&O.10/2024, R&O.102/2026, L.1/2017 (Art 20, Art 30(3), Art 31) and L.13/2019 (Sch 3 para 1).
Path note: the assignment says `WORK/c/expectations.md`; the brief defines WORK as `FLEET_DIR/work/<role>/` and the assignment confines writes to `FLEET_DIR/work/ind-c/`, so this file is `work/ind-c/expectations.md`.

Every row is facts -> outcome. Status `certain` means the text decides it; `amb(A|B)` means the Law is silent or ambiguous, A is the reading I take as default, B the other; those rows are pre-committed now as ambiguous, before seeing the encoding.

## Counting conventions (cited by the period rows)

- **C-AFTER** ("not more than N days/weeks after E", "within N of E"): the day of E is excluded; the last compliant day is E + N days. Alternative **C-AFTER-INCL**: the day of E counts as day 1, last compliant day E + N - 1.
- **C-BEFORE** ("at least N before X"): compliant iff E + N <= X (A). Alternative **C-BEFORE-CLEAR**: N clear days between, i.e. E + N + 1 <= X (B).
- **C-MONTH** (adding months or years): same day-number in the target month; where it does not exist, CLAMP to the last day of that month (A). Alternative ROLLOVER into the following month (B: 31 Jan + 1 month = 3 Mar in a common year; 29 Feb + 1 year = 1 Mar).
- **C-NOTICE** ("not less than M months' notice"): effective date F is compliant iff F >= given + M months (C-MONTH) (A); alternative clear months, F > given + M months (B).
- **C-LONGER** ("absent for a period longer than N consecutive weeks"): count the consecutive days of absence, first and last day inclusive; the ground exists iff that count > 7N. Two separate spells never add.
- **C-YEAREND** ("no later than 4 months after the end of that year"): for calendar year Y, last compliant day is 30 April Y+1 (A: 31 Dec + 4 months, clamped; equivalently the end of the 4 months beginning 1 Jan). Alternative B: 1 May Y+1 (rollover of "31 April").
- **C-YEAR** (Art 26(5) "a period of one year" from retention on day R): A: the period runs to the end of R + 1 year (anniversary, R excluded, C-MONTH clamp at 29 Feb); B (inclusive): last day is R + 1 year - 1 day.
- **Instants.** Every instrument commences at the start of its day, except R&O.10/2024, which commences at 09:30 on 27 Feb 2024. A question asked of a DATE alone on 27 Feb 2024 that the 09:30 change decides REFUSES (fleet ruling 5, F7.1); asked of an instant it answers.

## Article 5: the charity test (20 + 11 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A5-01 | all purposes charitable (education); provides public benefit (PB) to a reasonable degree; constitution has no 5(2) clause | meets the test | 5(1) | certain |
| A5-02 | education + a cafe purely ancillary/incidental to it; PB reasonable | meets | 5(1)(a)(ii) | certain |
| A5-03 | education + a purpose that is neither charitable nor ancillary (profit for members) | fails | 5(1)(a) | certain |
| A5-04 | only purposes are "ancillary" ones (fund-raising) and there is no charitable purpose for them to serve | fails | 5(1)(a)(ii) "to any of its charitable purposes" | certain |
| A5-05 | all purposes charitable; not an applicant; does not provide PB | fails | 5(1)(b) | certain |
| A5-06 | APPLICANT; purposes charitable; does not yet provide PB but intends to, to a reasonable degree | meets | 5(1)(b) parenthesis | certain |
| A5-07 | REGISTERED charity (not applicant); does not provide PB but intends to | fails | 5(1)(b) | certain |
| A5-08 | PB provided only outside Jersey, reasonable degree | meets | 5(1)(b) "in Jersey or elsewhere" | certain |
| A5-09 | PB provided, but not to a reasonable degree | fails | 5(1)(b) | certain |
| A5-10 | A5-01 + constitution EXPRESSLY permits ACTIVITIES to be directed/controlled by a Minister (e.g. the Minister for Health) acting in that capacity | fails | 5(2)(a); "a Minister" is generic, not the defined "Minister" | certain |
| A5-11 | as A5-10, controller = a member of the States Assembly in that capacity | fails | 5(2)(b) | certain |
| A5-12 | as A5-10, controller = equivalent in another jurisdiction (a UK government minister) in that capacity | fails | 5(2)(c) | certain |
| A5-13 | A5-01 + constitution expressly permits any GOVERNOR to be a Minister acting in that capacity | fails | 5(2)(a) | certain |
| A5-14 | governor route, a States member in that capacity | fails | 5(2)(b) | certain |
| A5-15 | governor route, a foreign equivalent (a French deputy) in that capacity | fails | 5(2)(c) | certain |
| A5-16 | constitution permits a States member to be a governor in a personal capacity (not acting in that capacity) | meets | 5(2) "acting in that capacity" | certain |
| A5-17 | constitution silent; a States member happens to be a governor | meets | 5(2) "expressly permits" | certain |
| A5-18 | A5-10 facts + an Order under 5(3) disapplies 5(2) for this entity | meets | 5(3) | certain |
| A5-19 | A5-10 facts + an Order under 5(3) for a description that does not cover this entity | fails | 5(3) | certain |
| A5-20 | 5(1) fails (non-charitable purpose) + an Order disapplies 5(2) | fails (5(3) only lifts (2)) | 5(3) | certain |
| A5-21 | purposes: education + advancing a political party | fails | 6(5), 5(1)(a) | certain |
| A5-22 | promoting an election candidate as an "incidental" activity of an educational purpose | fails (not ancillary either) | 6(5) | certain |
| A5-23 | entity with no purposes at all | A: fails (nothing charitable, no PB "in giving effect"); B: vacuously meets 5(1)(a) | 5(1) | amb(A|B) |
| A5-30 | duty to publish and maintain guidance on the test | Commissioner MUST | 5(4) | certain |
| A5-31 | who must have regard to the guidance | any person determining the test; Commissioner, tribunal, a registered charity and its governors in their other relevant functions; NOT a governor of an unregistered entity for "other functions" | 5(5) | certain |
| A5-32 | guidance issued after consulting charity representatives, the Minister and others thought appropriate, report published | procedure compliant | 5(6) | certain |
| A5-33 | as A5-32 but the Minister not consulted | non-compliant | 5(6)(a)(ii) | certain |
| A5-34 | as A5-32 but charity representatives not consulted | non-compliant | 5(6)(a)(i) | certain |
| A5-35 | as A5-32 but no report published | non-compliant | 5(6)(b) | certain |
| A5-36 | no "other persons" consulted because the Commissioner thought none appropriate | compliant | 5(6)(a)(iii) | certain |
| A5-37 | within a reasonable time (input) the Commissioner gives the Minister the guidance but not the report | non-compliant (both are owed) | 5(7) | certain |
| A5-38 | laying before the States | the Minister MUST, as soon as practicable after receipt | 5(8) | certain |
| A5-39 | which "Minister" is consulted under 5(6)(a)(ii) | on 2026-10-27 the Chief Minister; on 2025-06-01 the Minister for External Relations (V rows) | 5(6), Art 1 | certain |
| A5-40 | who may disapply 5(2) | the Minister, by Order | 5(3) | certain |

## Article 6: charitable purposes (40 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A6-01..A6-15 | a purpose squarely within each of (a) poverty, (b) education, (c) religion, (d) health, (e) saving lives, (f) citizenship/community development, (g) arts/heritage/culture/science, (h) public participation in sport, (i) recreation (with 6(2)(d) met), (j) human rights/conflict resolution/reconciliation, (k) religious/racial harmony, (l) equality and diversity, (m) environment, (n) relief of need, (o) animal welfare | charitable (15 rows) | 6(1)(a)-(o) | certain |
| A6-16 | purpose not in (a)-(o); judged reasonably analogous (input TRUE) / not (input FALSE) | charitable / not | 6(1)(p) | certain |
| A6-17 | prevention of disease | charitable, (d) | 6(2)(a) | certain |
| A6-18 | urban regeneration | charitable, (f) | 6(2)(b)(i) | certain |
| A6-19 | promotion of volunteering | charitable, (f) | 6(2)(b)(ii) | certain |
| A6-20 | promoting participation in an activity without physical skill and exertion (a card game), no other head | not within (h); not charitable unless (p) judged | 6(2)(c) | certain |
| A6-21 | promoting public participation in football | charitable, (h) | 6(1)(h), 6(2)(c) | certain |
| A6-22 | recreational facilities, object of improving conditions of life, open to the public at large | charitable, (i) | 6(2)(d)(ii) | certain |
| A6-23 | same, open to female members of the public at large | charitable, (i) | 6(2)(d)(ii) | certain |
| A6-24 | same, primarily for persons in need by reason of age | charitable, (i) | 6(2)(d)(i) | certain |
| A6-25 | recreational facilities for a private members' club, no need limb | not within (i) | 6(2)(d) | certain |
| A6-26 | facilities open to the public at large, but no object of improving conditions of life | not within (i) | 6(1)(i) | certain |
| A6-27 | relief of the aged by providing accommodation | charitable, (n) | 6(2)(e) | certain |
| A6-28 | advancement of a non-theistic philosophical belief | charitable, (p) by deeming (no judgement needed) | 6(2)(f) | certain |
| A6-29 | advancing a political party (even if educational in form) | not charitable, not ancillary | 6(5) | certain |
| A6-30 | promoting a candidate for an office outside Jersey | not charitable | 6(5) "whether in Jersey or elsewhere" | certain |
| A6-31 | non-party campaigning for human-rights law reform | charitable, (j); 6(5) not engaged | 6(1)(j), 6(5) | certain |
| A6-32 | the States, on the Commissioner's recommendation, by Regulations add (1)(q) | within the power | 6(3)(a) | certain |
| A6-33 | same without the Commissioner's recommendation | outside the power | 6(3) | certain |
| A6-34 | the Minister by Order adds (1)(q) | outside (the States, by Regulations) | 6(3) | certain |
| A6-35 | Regulations restricting (1)(a) | outside | 6(4)(a) | certain |
| A6-36 | Regulations amending (2)(c) | outside | 6(4)(a) | certain |
| A6-37 | Regulations altering (5) | outside | 6(4)(b) | certain |
| A6-38 | Regulations add (2)(g) explaining an added (1)(q), with recommendation | within | 6(3)(b) | certain |
| A6-39 | Regulations add (2)(g) explaining the existing (1)(b) | outside (only sub-paragraphs "so added") | 6(3)(b) | certain |
| A6-40 | private profit for members | not charitable | 6(1) | certain |

## Article 7: public benefit (9 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A7-01 | benefits only one particular named natural person | no PB; test fails | 7(3)(b) | certain |
| A7-02 | benefits only a group of identified natural persons | no PB; test fails | 7(3)(b) | certain |
| A7-03 | benefits a section of the public (a parish), conditions not unduly restrictive | no hard bar; PB is the determiner's finding (input) | 7(2) | certain |
| A7-04 | section of the public, fee condition found unduly restrictive | A: a factor only, PB still the determiner's finding; B: automatically no PB | 7(2)(b) "have regard to" | amb(A|B) |
| A7-05 | determiner presumed PB from the purpose (religion) | determination non-compliant | 7(3)(a) | certain |
| A7-06 | who is bound by 7(2)-(3) | Commissioner, tribunal, court; NOT a governor or any other person | 7(1) | certain |
| A7-07 | determination made without regard to the private-benefit/disbenefit comparison | non-compliant | 7(2)(a) | certain |
| A7-08 | benefit to the public at large | 7(2)(b) not engaged | 7(2)(b) | certain |
| A7-09 | the charity-test guidance silent on PB | non-compliant | 7(4) | certain |

## Article 26: power to demand information (55 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A26-01 | target: a registered charity | within 26(2) | 26(2)(a) | certain |
| A26-02 | target: an entity formerly registered | within | 26(2)(a) | certain |
| A26-03 | target: a governor of a registered charity | within | 26(2)(b) | certain |
| A26-04 | target: a FORMER governor of a registered charity | within | 26(2)(b) | certain |
| A26-05 | target: a governor of a formerly registered entity | within | 26(2)(b) | certain |
| A26-06 | target: a former governor of a formerly registered entity | within | 26(2)(b) | certain |
| A26-07 | target: an applicant never registered | NOT within | 26(2) | certain |
| A26-08 | target: governor of a never-registered applicant | NOT within | 26(2) | certain |
| A26-09 | target: an employee (not governor) of a registered charity | NOT within (for 26(1)) | 26(2) | certain |
| A26-10 | target: an unrelated third party (a bank) | NOT within | 26(2) | certain |
| A26-11 | written notice served on a 26(2) person, for deciding whether to serve an RSN, reasonably required | the Commissioner MAY require (a) documents/information and (b) attendance to answer | 26(1) | certain |
| A26-12 | as A26-11 but for deciding a registration application | power not available | 26(1)(a) | certain |
| A26-13 | requirement made orally | power not exercised (notice in writing) | 26(1) | certain |
| A26-14 | not reasonably required | power not available | 26(1) | certain |
| A26-15 | on 2018-04-30 / 2018-05-01 | Art 26 not in force / in force | endnotes, R&O.17/2018 Art 1(c) | certain |
| A26-16 | provider claims a lien | requirement without prejudice to the lien | 26(3) | certain |
| A26-17 | document provided | MAY retain/copy, and require an explanation from the provider | 26(4)(a) | certain |
| A26-18 | document provided | MAY require an explanation from an employee of the charity who appears to hold relevant information | 26(4)(a) | certain |
| A26-19 | document provided | may NOT require an explanation from someone who is neither provider nor governor/employee (an outside accountant) | 26(4)(a) | certain |
| A26-20 | document not provided | MAY require the addressee to state where it is | 26(4)(b) | certain |
| A26-21 | document not provided | no retention, no 26(4)(a) explanation | 26(4) | certain |
| A26-22 | retained 2026-01-10, no proceedings; query 2026-12-31 | may retain | 26(5)(a), C-YEAR | certain |
| A26-23 | same; query 2027-01-09 | may retain | 26(5)(a) | certain |
| A26-24 | same; query 2027-01-10 | A: may retain; B: may not | 26(5)(a), C-YEAR | amb(A|B) |
| A26-25 | same; query 2027-01-11 | may not | 26(5)(a) | certain |
| A26-26 | proceedings (relevant) commenced 2026-06-01, concluded 2028-05-01; query 2027-06-01 / 2028-05-02 | may retain / may not | 26(5)(b) | certain |
| A26-26b | same; query 2028-05-01 (day of conclusion) | A: may retain; B: may not | 26(5)(b) "until the conclusion" | amb(A|B) |
| A26-27 | proceedings commenced 2027-02-01 (after the year); query 2027-03-01 | may not | 26(5)(b) "within that period" | certain |
| A26-28 | proceedings 2026-03-01..2026-04-01; query 2026-12-01 / 2027-01-11 | may retain / may not (the year is longer) | 26(5) "longer of" | certain |
| A26-29 | proceedings commenced in the year, not concluded; query 2029-01-01 | may retain | 26(5)(b) | certain |
| A26-30 | proceedings commenced exactly 2027-01-10 | A: within the period; B: not | 26(5)(b), C-YEAR | amb(A|B) |
| A26-31 | retained 2024-02-29, no proceedings | 2025-02-27 may retain (all readings); 2025-02-28 A may, B may not; 2025-03-01 A-clamp may not, A-rollover may; 2025-03-02 may not | 26(5)(a), C-YEAR, C-MONTH | amb(A|B) |
| A26-32 | proceedings commenced within the year, to which the document is NOT relevant | 26(5)(b) not engaged | 26(5)(b) | certain |
| A26-33 | person needs the retained document for business and requests it | MUST be supplied a copy as soon as practicable | 26(6) | certain |
| A26-34 | requests, no business need | no duty | 26(6) | certain |
| A26-35 | business need, no request | no duty | 26(6) | certain |
| A26-36 | addressee of a valid 26(1) requirement fails to comply, no reasonable excuse | offence; imprisonment 3 months AND a fine of level 3 on the standard scale | 26(7) | certain |
| A26-37 | same with reasonable excuse | no offence | 26(7) | certain |
| A26-38 | employee required under 26(4)(a) to explain, refuses, no excuse | offence, same penalty | 26(7) | certain |
| A26-39 | addressee required under 26(4)(b) to say where the document is, refuses, no excuse | offence, same penalty | 26(7) | certain |
| A26-40 | withholds a document covered by legal professional privilege | no requirement, no contravention, no offence | 26(8) | certain |
| A26-41 | compelled statement used by the prosecution against its maker in proceedings for an Art 21(9) offence | not admissible | 26(9) | certain |
| A26-42 | used in 26(7) proceedings | admissible | 26(9) | certain |
| A26-43 | used in 26(10) proceedings | admissible | 26(9) | certain |
| A26-44 | used by the prosecution against a different person | not barred by 26(9) | 26(9) "against the person" | certain |
| A26-45 | used in civil proceedings | not barred | 26(9) "criminal proceedings" | certain |
| A26-46 | statement volunteered, not in compliance with a requirement | 26(9) not engaged | 26(9) | certain |
| A26-47 | knowingly false in a material particular, intended for a registration application | offence; imprisonment 2 years and a fine (no maximum stated) | 26(10) | certain |
| A26-48 | same, intended for deciding whether to serve an RSN | offence | 26(10) | certain |
| A26-49 | false but not known to be false | no offence | 26(10) | certain |
| A26-50 | knowingly false, immaterial particular | no offence | 26(10) | certain |
| A26-51 | knowingly false, material, intended only for the annual return | no 26(10) offence | 26(10) purposes | certain |
| A26-52 | provided orally, not in a document | offence (irrelevant) | 26(11)(a) | certain |
| A26-53 | volunteered, not under Art 26 | offence (irrelevant) | 26(11)(b) | certain |
| A26-54 | provider is a third party, not a 26(2) person | offence | 26(10) "a person" | certain |
| A26-55 | penalty of 26(10) | imprisonment 2 years; fine present, maximum absent | 26(10) | certain |

## Article 27: required steps notices (18 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A27-01..05 | Commissioner believes (a) misconduct by the charity / (b) the charity fails the test / (c) a governor engaged in misconduct / (d) a governor unfit by reason of a reportable matter / (e) the charity ceased to meet 11(4)(c) or (d) | power to serve available (5 rows) | 27(1), (2) | certain |
| A27-06 | no such belief | no power | 27(1) | certain |
| A27-07 | addressee: the registered charity; a present governor of it | relevant persons | 27(3) | certain |
| A27-08 | addressee: a FORMER governor | NOT a relevant person (contrast 26(2)(b)) | 27(3)(b) | certain |
| A27-09 | addressee: an employee | not a relevant person | 27(3) | certain |
| A27-10 | addressee: a deregistered entity | not ("the registered charity") | 27(1), (3)(a) | certain |
| A27-11 | notice oral, or no time specified | not a valid RSN | 27(2) "written", "in a time specified" | certain |
| A27-12 | served under (1)(c), requires removal of THAT governor, charity not an ORC | permitted | 27(4) | certain |
| A27-13 | served under (1)(d), requires suspension of that governor | permitted | 27(4) | certain |
| A27-14 | served under (1)(c), requires replacement of a DIFFERENT governor | A: not authorised by (4); B: may be "appropriate" under (2) | 27(4) "the governor referred to" | amb(A|B) |
| A27-15 | served under (1)(a) only, requires removal of a governor | A: not authorised (removal is a (1)(c)/(d) step); B: authorised if appropriate | 27(2), (4) | amb(A|B) |
| A27-16 | served under (1)(c) on an ORC, requires removal | removal requirement invalid | 27(4) "subject to Article 28", 28(3) | certain |
| A27-17 | on 2018-04-30 | no power (Art 27 not in force) | endnotes | certain |
| A27-18 | further procedure | the Minister MAY by Order | 27(5) | certain |

## Article 28: organized religious charities (11 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A28-01 | ORC; RSN requires removal of a governor AND filing accounts | removal invalid; accounts requirement valid ("to the extent") | 28(3) | certain |
| A28-02 | ORC; RSN on a governor requiring that governor's suspension | invalid to that extent | 28(3) | certain |
| A28-03 | ORC; RSN with other steps only | valid | 28(3) | certain |
| A28-04 | religious charity not categorized by any Order; RSN requires removal | valid | 28(1), (3) | certain |
| A28-05 | test met by virtue of 6(1)(c) solely; supervision adequate | may be categorized | 28(1) | certain |
| A28-06 | religion combined with education; supervision adequate | may be | 28(1)(a) "solely or in combination" | certain |
| A28-07 | religion; supervision inadequate | may not | 28(1)(b) | certain |
| A28-08 | education only | may not | 28(1)(a) | certain |
| A28-09 | non-theistic philosophical belief (6(1)(p) via 6(2)(f)); supervision adequate | A: may not ("by virtue of Article 6(1)(c)"); B: may (deemed analogous to (c)) | 28(1)(a), 6(2)(f) | amb(A|B) |
| A28-10 | who categorizes | the Minister by Order; the Order may give the Commissioner discretion to grant/withdraw | 28(1), (2)(a) | certain |
| A28-11 | "appear to the Minister" | judgement, an input | 28(1) | certain |

## Article 29 to 31: restricted information, required and permitted disclosure (23 + 8 + 1 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A29-01 | received under the Law (route a), disclosed without the subject's consent, no exception | offence; imprisonment 2 years and a fine (no maximum stated) | 29(1)(a) | certain |
| A29-02 | route (a), subject consents | no offence | 29(1) | certain |
| A29-03 | route (b) (received indirectly), subject consents, source does not | offence | 29(1) "(where (b) applies) the person from whom it was received" | certain |
| A29-04 | route (b), both consent | no offence | 29(1) | certain |
| A29-05 | route (b), source consents, subject does not | offence | 29(1) | certain |
| A29-06 | information in the general section (a public part) | no offence | 29(2)(a), 10(3)(a) | certain |
| A29-07 | the registered NAME of a restricted-section charity | not excepted: offence (absent consent/31) | 29(2)(a), 9(1)(a) | certain |
| A29-08 | a matter designated under 10(5) as not public | not excepted: offence | 29(2)(a), 10(5) | certain |
| A29-09 | already public from other sources | no offence | 29(2)(b) | certain |
| A29-10 | anonymised aggregate | no offence | 29(2)(c) | certain |
| A29-11 | not received under the Law nor from such a recipient | outside 29(1) | 29(1) | certain |
| A29-12 | Commissioner discloses to the Comptroller as required under 30(1) | no offence | 29(1) "subject to ... Articles 30" | certain |
| A29-13 | by/on behalf of the Commissioner for the Commissioner's functions | no offence | 31(a) | certain |
| A29-14 | to the Comptroller for ANY of the Comptroller's functions | no offence | 31(b) | certain |
| A29-15 | to the JFSC for any of its functions | no offence | 31(c) | certain |
| A29-16 | to the AG, the Bailiff or the court for functions in relation to charities | no offence | 31(d) | certain |
| A29-17 | to the AG for a function not in relation to charities (and not an offence investigation), by a non-Commissioner | not excepted: offence | 31(d) | certain |
| A29-18 | to the police for investigating a Jersey offence | no offence | 31(e) | certain |
| A29-19 | to any person for deciding whether to take proceedings under this Law | no offence | 31(e) | certain |
| A29-20 | by a governor (not the Commissioner) to a foreign police force about a foreign offence | not excepted: offence | 31(e) "under any enactment or ... customary law of Jersey" | certain |
| A29-21 | circumstances prescribed by Regulations | no offence | 31(f) | certain |
| A29-22 | to a journalist, no consent | offence | 29(1) | certain |
| A29-23 | disclosure on 2018-04-30 | Art 29 not in force | endnotes | certain |
| A30-01 | Comptroller requires info for taxation of a registered charity | Commissioner MUST disclose | 30(1) | certain |
| A30-02 | for taxation of an unregistered entity with a charitable purpose | MUST disclose | 30(1) | certain |
| A30-03 | for taxation of an entity with no charitable purpose | no 30(1) duty (31(b) permits) | 30(1) | certain |
| A30-04 | Comptroller requires for a non-tax function | no 30(1) duty | 30(1) | certain |
| A30-05 | JFSC requires for its NPO Law functions | MUST disclose | 30(2) | certain |
| A30-06 | JFSC requires for banking supervision | no 30(2) duty (31(c) permits) | 30(2) | certain |
| A30-07 | no requirement made | no duty | 30 "if required by" | certain |
| A30-08 | meaning of "Comptroller" on 2019-12-31 / 2020-01-01 | by the Income Tax (Jersey) Law 1961 / by the Revenue Administration (Jersey) Law 2019 | Art 1, L.13/2019 Sch 3 para 1, R&O.136/2019 | certain |
| A31-01 | a governor (not the Commissioner) discloses to the Commissioner to help a registration | A: not within 31(a) (not "by or on behalf of the Commissioner"); B: within | 31(a) | amb(A|B) |

## Article 32: the tribunal (2 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A32-01 | 2015-01-01 | Art 32 in force (2014), Arts 33-36 not (2018): no appeal lies yet | endnotes | certain |
| A32-02 | function | to hear and determine appeals under Part 8 | 32(2) | certain |

## Article 33: who may appeal (29 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A33-01 | applicant refused registration | may appeal | 33(1)(a) | certain |
| A33-02 | applicant refused restricted-section entry | may appeal | 33(1)(b) | certain |
| A33-03 | applicant appeals the decision to register it | no right | 33(1) | certain |
| A33-04 | registered charity deregistered under 16(1) | may appeal | 33(2)(a) | certain |
| A33-05 | deregistered under 16(2) (no longer exists) | may appeal (literal) | 33(2)(a) | certain |
| A33-06 | deregistered on its own application, 15(3)(a) | A: may appeal (literal "to deregister"); B: no | 33(2)(a) | amb(A|B) |
| A33-07 | refused deregistration under 15(3)(b) | the charity has no right (not in 33(2)); only the AG | 33(2), (4) | certain |
| A33-08 | refused permission to change/add a name, 12(4) | may appeal | 33(2)(b) | certain |
| A33-09 | required under 12(6) to apply to change name | may appeal | 33(2)(c) | certain |
| A33-10 | refused approval of a purpose amendment, 13(3) | may appeal | 33(2)(d) | certain |
| A33-11 | refused approval of a PB-statement amendment, 13(4)(b) | may appeal | 33(2)(e) | certain |
| A33-12 | refused permission to amend a payments statement, 13(11)(b) | no right | 33(2) | certain |
| A33-13 | general-section charity refused restricted-section entry (9(2) request) | no right (not an applicant, not in 33(2)) | 33(1)(b), (2) | certain |
| A33-14 | addressee of an Art 26 notice, against a requirement in it | may appeal | 33(3) | certain |
| A33-15 | charity served with an RSN | may appeal | 33(3) | certain |
| A33-16 | governor served with an RSN | may appeal | 33(3) | certain |
| A33-17 | governor of a charity served with an RSN, governor not served | no right under 33(3) | 33(3) "a person on whom" | certain |
| A33-18 | the AG, against any decision (a registration, a refusal to deregister, a 10(5) designation) | may appeal | 33(4) | certain |
| A33-19 | third party with an interest in the name; applicant registered; name undesirable under 12(1) at application AND at appeal | may appeal | 33(5)(b) | certain |
| A33-20 | same, undesirable at application only | no | 33(5) "at both" | certain |
| A33-21 | same, undesirable at appeal only | no | 33(5) | certain |
| A33-22 | third party with no interest in the name, name ground | no | 33(5)(b) | certain |
| A33-23 | third party; applicant failed the test at both times | may appeal | 33(5)(a) | certain |
| A33-24 | failed at application, meets at appeal | no | 33(5) | certain |
| A33-25 | the third party is itself a registered charity (rival with a similar name), both-times name ground | A: excluded (literal "other than ... a registered charity"); B: may appeal | 33(5) | amb(A|B) |
| A33-26 | third party appeals a REFUSAL to register | no right under 33(5) | 33(5) | certain |
| A33-27 | governor of a deregistered charity appeals in own name | no right | 33 | certain |
| A33-28 | appeal rights on 2018-04-30 / 2018-05-01 | none / available | endnotes | certain |

## Articles 34 to 36: the tribunal's and court's powers (8 + 7 + 8 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A34-01 | ground: decision wrong on the facts | admissible ground (merits, facts or law; wrong or unreasonable) | 34(1) | certain |
| A34-02 | interim order; evidence not before the Commissioner | tribunal MAY | 34(2) | certain |
| A34-03 | outcomes | remit, substitute or dismiss | 34(3)(a) | certain |
| A34-04 | appeal vexatious | MAY award costs | 34(3)(b) | certain |
| A34-05 | appeal otherwise grossly unreasonable | MAY award costs | 34(3)(b) | certain |
| A34-06 | appeal failed, not vexatious or grossly unreasonable | may NOT award costs | 34(3)(b) | certain |
| A34-07 | successful appellant asks for costs against the Commissioner | no 34(3)(b) power (condition is on the appeal) | 34(3)(b) | certain |
| A34-08 | recommendations | MAY | 34(3)(c) | certain |
| A35-01 | a party appeals to the court on unreasonableness | may | 35(1) | certain |
| A35-02 | the AG, not a party | may | 35(1) | certain |
| A35-03 | a non-party, not the AG | may not | 35(1) | certain |
| A35-04 | the Commissioner (respondent below) | A: may (a party); B: not | 35(1) | amb(A|B) |
| A35-05 | ground: wrong on the facts but not unreasonable in all the circumstances | no ground | 35(1) | certain |
| A35-06 | court outcomes | remit to tribunal or Commissioner; substitute for the tribunal's or the Commissioner's decision; dismiss | 35(2) | certain |
| A35-07 | point of law reference; interim orders | tribunal MAY refer; court MAY make interim orders | 35(3), (4) | certain |
| A36-01 | reconsideration by the Commissioner | not limited by Part 8 | 36(1) | certain |
| A36-02 | time limit for an appeal | none in the Law; only if an Order under 36(2)(a) prescribes it (input), never an invented period | 36(2)(a) | certain |
| A36-03 | substituted decision's effective date | any date before, on or after the original or own decision | 36(3) | certain |
| A36-04 | order dated 2026-06-01, substituted decision effective 2025-01-01; act on 2025-06-01 | not an offence merely by the order | 36(4) | certain |
| A36-05 | same; act on 2026-06-02 | not protected by 36(4) | 36(4) "before the date of the order" | certain |
| A36-06 | same; act on 2026-06-01 (order's date) | not protected | 36(4) | certain |
| A36-07 | substituted effective date AFTER the order (2026-07-01) | 36(4) not engaged | 36(4) | certain |
| A36-08 | order 2026-06-01, effective 2025-01-01; act on 2024-06-01 | protected (before the order) | 36(4) | certain |

## Article 37: offences by bodies (15 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A37-01 | company commits a Law offence (26(7)) with a director's consent | director also guilty; same penalty (3 months + level 3) | 37(1)(a) | certain |
| A37-02 | with the company secretary's connivance | guilty | 37(1)(a) | certain |
| A37-03 | a person purporting to act as director consents | guilty | 37(1)(b) | certain |
| A37-04 | director neither consented nor connived (neglect only) | not guilty under 37 (no neglect limb) | 37(1) | certain |
| A37-05 | LLP, partner consents | guilty | 37(1) | certain |
| A37-06 | separate limited partnership, partner consents | guilty | 37(1) | certain |
| A37-07 | unincorporated association (2(1)(i)), committee member consents | 37 does not apply | 37(1) | certain |
| A37-08 | trustees of a trust | 37 does not apply | 37(1) | certain |
| A37-09 | foundation (body corporate), council member consents | guilty ("governor" of the body corporate) | 37(1)(a), 2(7)(b) | certain |
| A37-10 | member-managed body corporate, member consents in management | treated as director: guilty | 37(2) | certain |
| A37-11 | body corporate not member-managed; ordinary member consents | not guilty | 37 | certain |
| A37-12 | offence not proved against the body | no derived liability | 37(1) "is proved" | certain |
| A37-13 | ordinary limited partnership (not LLP, not separate) | 37 does not apply | 37(1) | certain |
| A37-14 | 2018-04-30 / 2018-05-01 | not in force / in force | endnotes, R&O.17/2018 Art 1(e) | certain |
| A37-15 | offence under another enactment | 37 does not apply ("an offence under this Law") | 37(1) | certain |

## Articles 38 to 43 (1 + 6 + 2 + 7 + 6 + 1 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| A38-01 | service of notices | the Minister MAY by Order; in force 2014-11-21 | 38 | certain |
| A39-01 | an Order with transitional provision | permitted | 39(1) | certain |
| A39-02 | an Order amending this Law as a "consequential" provision under 39(1) | not permitted | 39(1) "other than an amendment of this Law" | certain |
| A39-03 | Regulations under 22(5) amending 22(2), plus a consequential amendment of 21(5) | permitted | 39(2) | certain |
| A39-04 | an ORDER under 2(2) with a consequential amendment of 2(3) | not permitted (39(2) is for Regulations only) | 39(1), (2) | certain |
| A39-05 | 39(2) amendments | must appear to the States necessary or expedient | 39(2) | certain |
| A39-06 | Regulations under 6(3) adding (1)(q), with a consequential amendment of 6(5) | A: not permitted (6(4)(b) prevails); B: permitted by 39(2) | 6(4)(b) vs 39(2) | amb(A|B) |
| A40-01 | independent powers of AG, Bailiff, court | preserved | 40(1) | certain |
| A40-02 | saving and transitional Regulations | the States MAY; the Minister by Order may not under 40 | 40(2), (3) | certain |
| A41-01 | Regulations amending the Proceeds of Crime (Supervisory Bodies) Law 2008 to let supervisory bodies disclose to the Commissioner | within | 41(1)(a), (2) | certain |
| A41-02 | amending an enactment under which the JFSC has functions | within | 41(1)(b) | certain |
| A41-03 | amending a taxation enactment so the Comptroller may disclose | within | 41(1)(c) | certain |
| A41-04 | amending an enactment that is none of (a)-(c) | outside | 41(1) | certain |
| A41-05 | amending a relevant enactment for some other purpose | outside | 41(2) | certain |
| A41-06 | the Minister by Order | outside (the States, by Regulations) | 41(2) | certain |
| A41-07 | in force | 2014-11-21 (original Art 42) | endnotes | certain |
| A42-01 | Regulations amending the Trusts Law 1984 to apply the charity test | within | 42(a) | certain |
| A42-02 | amending the Foundations Law 2009 | within | 42(a) | certain |
| A42-03 | consequential amendment of another enactment's reference to charities | within | 42(b) | certain |
| A42-04 | amending THIS Law under 42(b) | outside | 42(b) "not including this Law" | certain |
| A42-05 | power holder | the States by Regulations | 42 | certain |
| A42-06 | in force | 2014-11-21 (original Art 43) | endnotes | certain |
| A43-01 | short title; in force | "Charities (Jersey) Law 2014"; 2014-11-21 (original 44(1)) | 43, endnotes | certain |

## Schedule 1: the Commissioner (51 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| S1.1-01 | who must appoint | the Minister: 2026-10-27 Chief Minister; 2025-01-01 Minister for External Relations | Sch1 1(1), Art 1 | certain |
| S1.1-02 | JAC views not sought | non-compliant | Sch1 1(2) | certain |
| S1.1-03 | notice 2026-01-01, appointment 2026-01-15 | A compliant; B (clear days) non-compliant | Sch1 1(3), C-BEFORE | amb(A|B) |
| S1.1-04 | notice 2026-01-01, appointment 2026-01-14 | non-compliant | Sch1 1(3) | certain |
| S1.1-05 | notice 2026-01-01, appointment 2026-01-16 | compliant | Sch1 1(3) | certain |
| S1.1-06 | notice on the day of appointment | non-compliant | Sch1 1(3) | certain |
| S1.1-07 | notice after appointment | non-compliant | Sch1 1(3) | certain |
| S1.1-08 | no notice | non-compliant | Sch1 1(3) | certain |
| S1.1-09 | leap February: notice 2028-02-20, appointment 2028-03-05 / 2028-03-04 | compliant (A) / non-compliant | Sch1 1(3) | certain (A row amb as S1.1-03) |
| S1.1-10 | term 6 years | valid | Sch1 1(5) | certain |
| S1.1-11 | term 6 years and 1 day, or 73 months | invalid | Sch1 1(5) | certain |
| S1.1-12 | term 1 year | valid | Sch1 1(5) | certain |
| S1.1-13 | start 2024-02-29; end 2030-02-28 / end 2030-03-01 | valid / A-clamp invalid, B-rollover valid | Sch1 1(5), C-MONTH | amb(A|B) |
| S1.1-14 | re-appointment | MAY; capped by 3(4)(c) | Sch1 1(6) | certain |
| S1.1-15 | part-time terms | permitted | Sch1 1(8) | certain |
| S1.2-01 | corporation sole powers | agreements; MOVABLE property; sue and be sued; be charged and defend; incidental | Sch1 2(1) | certain |
| S1.2-02 | independence | of the States and the Minister | Sch1 2(2) | certain |
| S1.2-03 | employment or agency contract | none to be construed | Sch1 2(3) | certain |
| S1.2-04 | remuneration out of the annual income of the States, subject to DBA Art 20(1)? 2019-12-15 / 2019-12-16 / 2026-10-27 | not subject / subject / subject | Sch1 2(4)(a), L.1/2017 Art 30(3)(a), endnote | certain |
| S1.2-04b | same question on 2018-06-01 | A: not subject (words inserted later); B: REFUSE (no vintage before 2019-01-01) | Sch1 2(4)(a) | amb(A|B) |
| S1.2-05 | fees received | paid to the income of the States; never DBA-qualified | Sch1 2(4)(b) | certain |
| S1.3-01 | 3 months' notice given 2026-01-15; effective 2026-04-15 / 04-14 / 04-16 | A valid, B invalid / invalid / valid | Sch1 3(1)(a), C-NOTICE | amb(A|B) for 04-15 |
| S1.3-02 | given 2025-11-30; effective 2026-02-28 / 2026-03-02 / 2026-02-27 | A-clamp valid, B-rollover invalid / valid / invalid | Sch1 3(1)(a), C-MONTH | amb(A|B) for 02-28 |
| S1.3-03 | given 2027-11-30; effective 2028-02-29 / 2028-02-28 | valid (clamp) / invalid | Sch1 3(1)(a) | certain under A |
| S1.3-04 | oral notice, or notice to someone other than the Minister | not a 3(1)(a) resignation | Sch1 3(1)(a) | certain |
| S1.3-05 | absent 28 consecutive days / 29 / two spells of 20 | no ground / ground / no ground | Sch1 3(2)(a), C-LONGER | certain |
| S1.3-06 | bankrupt / incapacitated by illness / otherwise unfit (judgement) | ground (Minister must be satisfied) | Sch1 3(2)(b)-(d) | certain |
| S1.3-07 | no ground | no power to terminate | Sch1 3(2) | certain |
| S1.3-08 | terminated 2026-03-01; notice to the States 2026-03-01 / 03-14 / 03-15 / 03-16 | compliant / compliant / A compliant, B non-compliant / non-compliant | Sch1 3(3), C-AFTER | amb(A|B) for 03-15 |
| S1.3-09 | period expires without re-appointment | appointment expires | Sch1 3(4)(a) | certain |
| S1.3-10 | becomes a member of the States | expires | Sch1 3(4)(b) | certain |
| S1.3-11 | aggregate service 6+6 years (with a gap) / 6+5 / 11y364d / exactly 12y | expires / not / not / expires | Sch1 3(4)(c) | certain |
| S1.3-12 | 10 years served, re-appointed for 6 | expires after 2 more years | Sch1 3(4)(c) | certain |
| S1.4-01 | staff makes the Art 11 registration decision (even if authorised) | not permitted | Sch1 4(3)(a) | certain |
| S1.4-02 | staff decides to REFUSE deregistration under 15(3)(b) | not permitted | Sch1 4(3)(b) | certain |
| S1.4-03 | staff decides TO deregister on application under 15(3)(a) | A: not permitted (it is the 15(3) decision); B: permitted | Sch1 4(3)(b) "whether to refuse" | amb(A|B) |
| S1.4-04 | staff decides an Art 16(1) or 16(2) deregistration | not permitted | Sch1 4(3)(c) | certain |
| S1.4-05 | authorised staff serves an Art 26 notice / unauthorised staff | permitted / not | Sch1 4(3) | certain |
| S1.4-06 | authorised staff serves an RSN | permitted | Sch1 4(3) | certain |
| S1.4-07 | authorised staff decides a restricted-section request (Art 9) | permitted | Sch1 4(3) | certain |
| S1.4-08 | designated relevant person; Commissioner incapacitated | treated as the Commissioner; may make the Art 11 decision | Sch1 4(5)(a) | certain |
| S1.4-09 | designated relevant person; Commissioner able to act | not treated as Commissioner | Sch1 4(5) | certain |
| S1.4-10 | vacancy + designation / vacancy, no designation | treated as Commissioner / nobody | Sch1 4(5)(b) | certain |
| S1.4-11 | States' employee made available, working under the Commissioner's direction | treated as the Commissioner's staff | Sch1 4(2) | certain |
| S1.4-12 | cost of staff, accommodation and equipment | out of the annual income of the States; DBA-qualified from 2019-12-16 (as S1.2-04) | Sch1 4(7) | certain |
| S1.4-13 | report for 2025 given to the Minister 2026-04-30 / 05-01 / 05-02 | compliant / A non-compliant, B compliant / non-compliant | Sch1 4(9), C-YEAREND | amb(A|B) for 05-01 |
| S1.4-14 | report prepared but not published | non-compliant (prepare AND publish) | Sch1 4(8) | certain |
| S1.4-15 | laying | the Minister MUST, as soon as practicable | Sch1 4(10) | certain |
| S1.4-16 | direction on form, by written notice, published | valid | Sch1 4(11) | certain |
| S1.4-17 | direction not published | not validly given | Sch1 4(11) | certain |
| S1.4-18 | direction requiring justification of a decision about an individual charity | invalid | Sch1 4(12) | certain |
| S1.4-19 | requiring justification about individual governors or applicants | invalid | Sch1 4(12) | certain |
| S1.4-20 | requiring aggregate counts of decisions | valid | Sch1 4(12) | certain |

## Schedule 2: the tribunal (24 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| S2.1-01 | members appointed 3 / 4 / 8 / 9 | non-compliant / compliant / compliant / non-compliant | Sch2 1(1) | certain |
| S2.1-02 | JAC views | must be sought | Sch2 1(2) | certain |
| S2.1-03 | 2 weeks' notice | as S1.1-03..09 | Sch2 1(3) | as Sch 1 |
| S2.1-04 | term | at most 6 years (as S1.1-10..13) | Sch2 1(5) | as Sch 1 |
| S2.1-05 | chair and vice-chair different persons / same person / chair only | compliant / non-compliant / non-compliant | Sch2 1(7) "one ... and another" | certain |
| S2.1-06 | no remuneration determination | all honorary | Sch2 1(8) | certain |
| S2.1-07 | determination: the chair | chair paid, others honorary | Sch2 1(8) | certain |
| S2.1-08 | determination: all members | all paid | Sch2 1(8) | certain |
| S2.1-09 | determination: the vice-chair only, or one ordinary member | not within 1(8): honorary | Sch2 1(8) | certain |
| S2.2-01 | 1 month's notice: given 2026-03-15, effective 04-15 / 04-14; given 2026-01-31, effective 02-28 / 03-03 | A valid, B invalid / invalid; A-clamp valid, B-rollover invalid / valid | Sch2 2(1)(a), C-NOTICE, C-MONTH | amb(A|B) |
| S2.2-02 | absent 56 consecutive days / 57 | no ground / ground | Sch2 2(2)(a), C-LONGER | certain |
| S2.2-03 | bankrupt / illness / unfit | ground | Sch2 2(2)(b)-(d) | certain |
| S2.2-04 | notice to the States after termination | as S1.3-08 | Sch2 2(3) | as Sch 1 |
| S2.2-05 | 12 years aggregate | expires | Sch2 2(4)(c) | certain |
| S2.2-06 | becomes a member of the States | expires | Sch2 2(4)(b) | certain |
| S2.3-01 | no responsible officer | non-compliant (at least one) | Sch2 3(2) | certain |
| S2.3-02 | responsible officer takes part in a determination | not permitted ("but not determinations") | Sch2 3(2) | certain |
| S2.3-03 | must the responsible officer PUBLISH the report? | no: prepare and provide only (contrast Sch1 4(8)) | Sch2 3(3) | certain |
| S2.3-04 | report deadline | as S1.4-13 | Sch2 3(4) | as Sch 1 |
| S2.4-01 | chair present (vice-chair present too) | chair presides | Sch2 4(1)(a) | certain |
| S2.4-02 | chair absent, vice-chair present | vice-chair presides | Sch2 4(1)(b) | certain |
| S2.4-03 | both absent | a member appointed by the members present | Sch2 4(1)(c) | certain |
| S2.4-04 | both absent, nobody appointed | nobody validly presides | Sch2 4(1) | certain |
| S2.4-05 | chair present but vice-chair presides | non-compliant | Sch2 4(1) | certain |
| S2.4-07 | Regulations create a tribunal offence: 2 years + fine / 3 years / fine only | within / outside / within | Sch2 4(3)(f) | certain |
| S2.4-08 | Regulations let the chair alone determine an appeal | within | Sch2 4(3)(e) | certain |
| S2.4-09 | who makes procedure Regulations | the States | Sch2 4(3) | certain |

## Commencement, in CURRENT numbering (13 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| C-01 | 2014-11-20 | nothing in force | endnotes | certain |
| C-02 | 2014-11-21 | Arts 1-7, 32, 38, 39, 40, 41, 42, 43; Schedules 1 and 2 in force | endnotes + renumbering table | certain |
| C-03 | 2014-11-21 | Arts 8-31, 33-37 not in force | endnotes | certain |
| C-04 | 2018-04-30 | Parts 4, 5, 7, Arts 33-37 not in force | R&O.17/2018 Art 1 | certain |
| C-05 | 2018-05-01 | Parts 4 (8-17), 5 (18-20), 7 (26-31), Arts 33-36, 37 in force; Part 6 (21-25) not | R&O.17/2018 Art 1 | certain |
| C-06 | 2018-12-31 | Part 6 not in force | R&O.17/2018 Art 2 | certain |
| C-07 | 2019-01-01 | Part 6 in force; the whole Law in force | R&O.17/2018 Art 2 | certain |
| C-08 | original Art 41 | in force 2019-01-01 as part of the remainder, now spent and omitted; content not in the sources | endnotes | certain |
| C-09 | original 44(2), 44(3) | in force 2014-11-21 (44(2) itself commenced the first stage); spent | R&O.17/2018 Art 2, renumbering table | certain |
| C-10 | renumbering | orig 42 -> 41, 43 -> 42, 44(1) -> 43; orig 41, 44(2), 44(3) spent; Arts 1-40 unchanged | renumbering table | certain |
| C-11 | current "Article 44" | does not exist (REFUSE) | renumbering table | certain |
| C-12 | 2015-01-01, Art 32 / Art 33 | in force / not | endnotes | certain |
| C-13 | 2015-01-01, Schedule 2 | in force (appeals only from 2018-05-01) | endnotes | certain |

## Vintages (17 rows)

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| V-01 | "Minister" on 2019-01-01 / 2019-05-30 | Chief Minister | 1 Jan 2019 vintage; R&O.40/2019 substitutes FOR "Chief Minister" | certain |
| V-02 | 2019-05-31 | Minister for External Relations | R&O.40/2019 Sch 2 para 1(e) | certain |
| V-03 | 2021-03-01 / 2021-03-02 | MER / Minister for External Relations and Financial Services | R&O.29/2021 Sch 2 para 1(e) | certain |
| V-04 | 2023-04-11 / 2023-04-12 | MERFS / Chief Minister | R&O.28/2023 Sch 2 para 1(4) (made 5 Apr, in force 7 days after) | certain |
| V-05 | 2024-02-26 / 2024-02-27 (date) / 2024-02-27T09:29 / 09:30 / 2024-02-28 | CM / REFUSE / CM / MER / MER | R&O.10/2024 Sch 4, Art 5 | certain |
| V-06 | 2025-10-09 | MER (consistent: R&O.56/2025 was made that day by the MER under Art 2(2)) | R&O.56/2025 | certain |
| V-07 | 2026-10-01 / 2026-10-02 / 2026-10-27 | MER / CM / CM | R&O.102/2026 Art 1, Art 7(6) (made 25 Sep 2026) | certain |
| V-08 | 2017-06-01 (after 2014-11-21, before any vintage) | A: Chief Minister (endnote [1] lists no earlier amender, R&O.40/2019 substitutes for "Chief Minister"); B: REFUSE (no vintage before 2019-01-01) | brief "Vintages are inputs" | amb(A|B) |
| V-09 | before 2014-11-21 | REFUSE (Part 1 not in force) | endnotes | certain |
| V-10 | "Comptroller" 2019-12-31 / 2020-01-01 | Income Tax (Jersey) Law 1961 / Revenue Administration (Jersey) Law 2019 | L.13/2019 Sch 3 para 1; R&O.136/2019 | certain |
| V-11 | Art 2(1)(ba) on 2025-10-15 / 2025-10-16 | absent / present | R&O.56/2025 Art 2 (made 9 Oct, 7 days after) | certain |
| V-12 | Sch1 2(4)(a), 4(7) DBA words 2019-12-15 / 2019-12-16 | absent / present | L.1/2017 Art 30(3); endnote | certain |
| V-13 | which text governs on 2026-10-27 | the vintage of 2 Oct 2026 | endnotes | certain |
| V-14 | vintage for day D | latest of the nine dates <= D (1 Jan 2019, 31 May 2019, 16 Dec 2019, 1 Jan 2020, 2 Mar 2021, 12 Apr 2023, 27 Feb 2024 09:30, 16 Oct 2025, 2 Oct 2026); none before 2019-01-01 | endnotes | certain |
| V-15 | editorial changes, endnotes [3] and [4] | no change of meaning; undated | endnotes | certain |
| V-16 | who makes a 5(3) / 28(1) / 36(2) Order on 2020-06-01 | Minister for External Relations | Art 1 vintage | certain |
| V-17 | who makes it on 2023-06-01 | Chief Minister | Art 1 vintage | certain |

## Source-text notes banked before opening the encoding

- 31(a) and 31(b) still read "for purpose of"; endnote [4] corrected only 31(c).
- 27(2) "in Commissioner's opinion"; 42(a) "by reference the test itself"; Sch 2 1(8) "as Minister sees fit" (missing articles).
- Schedule 2 is headed "Charity Commission tribunal"; Art 1 and Art 32 name it "the Charity Tribunal".
- Cross-scope contradiction: 19(9)(e)(i) obliges the Commissioner, on determining that a governor who reported a reportable matter is not fit, to serve an RSN requiring the charity to suspend or remove the governor; 28(3) makes that requirement invalid for an organized religious charity. Discriminating case: ORC, governor reports bankruptcy, the Commissioner (not the court) determines unfit.
- 6(4)(b) vs 39(2): see A39-06.
- 5(2)(b) "member of the States Assembly" vs Sch1 3(4)(b) and Sch2 2(4)(b) "member of the States": two spellings of one thing, probably.

## Rows added in the same sitting, still before opening anything

| id | facts | expected | provision | status |
| --- | --- | --- | --- | --- |
| S1.1-16 | office vacant, Minister takes no steps | non-compliant (all reasonable steps to keep it filled) | Sch1 1(7) | certain |
| S1.4-21 | staff, accommodation, equipment | the Minister MUST make available / provide, as the Minister considers required | Sch1 4(1), (6) | certain |
| S2.3-05 | staff and resources for the tribunal | the Minister MUST make available | Sch2 3(1) | certain |
| S2.4-06 | the tribunal's own procedure | MAY regulate it, subject to 4(1) and Regulations | Sch2 4(2) | certain |

Finished 2026-10-26T16:12:11Z (UTC). Nothing in DEPOSIT, `phase1/` (other than the assignment) or `domain.l4` was opened or listed before this line.

## Note appended after the encoding was opened (2026-10-26T16:46:23Z); nothing above it was changed

- The row counts in the section headings above were miscounted by hand.  Counted by row id (a range such as A6-01..A6-15 counts each row): Art 5: 34, Art 6: 40, Art 7: 9, Art 26: 56, Art 27: 18, Art 28: 11, Art 29: 23, Art 30: 8, Art 31: 1, Art 32: 2, Art 33: 28, Art 34: 8, Art 35: 7, Art 36: 8, Art 37: 15, Art 38: 1, Art 39: 6, Art 40: 2, Art 41: 7, Art 42: 6, Art 43: 1, Sch 1 para 1: 16, para 2: 6, para 3: 12, para 4: 21, Sch 2 para 1: 9, para 2: 6, para 3: 5, para 4: 9, commencement: 13, vintages: 17; total 405 rows, of which 24 are amb(A|B).
- Rows added later are tagged POST-HOC or POST-HOC-CERTAIN in the test modules, never here.
