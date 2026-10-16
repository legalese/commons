# Independent expectations: Telecommunications Act 2001 (NZ), copper withdrawal, disputes, periods, levy interest

Written from BRIEF.md and the source text (as at 4 September 2026) before any `.l4` file was opened. Expected values in this file are not to be changed after the encoding is opened. Notes about which scenarios turned out not expressible against the encoding are added only in the section at the end.

## Working-day calendar used (s 5)

s 5: "working day means a day of the week other than— a Saturday, a Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Te Rā Aro ki a Matariki/Matariki Observance Day, and Labour Day; and the day observed in the appropriate area as the anniversary of the province ...; and a day in the period commencing with 25 December in any year and ending with 2 January in the following year; and if 1 January in any year falls on a Friday, the following Monday; ... if Waitangi Day or Anzac Day falls on a Saturday or a Sunday, the following Monday".

Non-working weekdays I used:
- 2026: Fri 6 Feb (Waitangi), Fri 3 Apr (Good Friday), Mon 6 Apr (Easter Monday), Mon 27 Apr (Anzac Day 25 Apr is a Saturday, so the following Monday), Mon 1 Jun (Sovereign's birthday, first Monday of June), Fri 10 Jul (Matariki, input), Mon 26 Oct (Labour Day, 4th Monday of October: Mondays are 5, 12, 19, 26), Fri 25 Dec to Sat 2 Jan 2027 inclusive.
- 2027: Mon 4 Jan (1 Jan 2027 is a Friday, so "the following Monday"), Mon 25 Jan (Wellington Anniversary, input), Mon 8 Feb (Waitangi Day 6 Feb is a Saturday), Fri 26 Mar (Good Friday; Easter Sunday 28 Mar 2027), Mon 29 Mar (Easter Monday), Mon 26 Apr (Anzac Day 25 Apr is a Sunday), Mon 7 Jun (Sovereign's birthday), Fri 25 Jun (Matariki 2027, input), Mon 25 Oct (Labour Day).

Reading taken for "N working days after date D": count starts on the day after D (D itself is not counted, whether or not it is a working day); the result is the Nth working day after D. I took the Sovereign's birthday as the first Monday in June (Holidays Act 2003 meaning); the brief makes only Matariki and the anniversary day inputs.

Unless stated, the anniversary day is Wellington (25 Jan 2027) and the Matariki days are 10 Jul 2026 and 25 Jun 2027.

## Goal 1: Copper withdrawal (ss 69AC-69AE, Schedule 2A)

Readings taken:
- s 69AC(2)/69AD(2): "Chorus may stop supplying the service ... only if— (a) a copper withdrawal code has been approved and Chorus complies with the requirements of the code in relation to stopping the supply of the service; or (b) the end-user chooses to have the service disconnected (other than a temporary disconnection)." The Act states only a necessary condition ("only if"). I take it, as the brief's goal does, as: may stop = (a) or (b), provided the section applies.
- Schedule 2A cl 1(3) protections are what the approved code must require "before Chorus is permitted to stop supplying a copper service under section 69AC or 69AD". I read limb (a) as satisfied only if each protection is met (an approved code must contain them, so Chorus cannot comply with the code without them). Limb (b) (the end-user's own choice) does not need them. Ambiguity: an encoding could instead treat "Chorus complies" as a single input and treat the protections separately as a test of the code's content.
- If the section does not apply (its (1) conditions fail), s 69AC/69AD says nothing; the right answer is not "FALSE" but a refusal or a "section does not apply" result.

| id | inputs | expected | provision |
|---|---|---|---|
| C01 | s 69AC applies; code approved; Chorus complies; all Sch 2A protections met; no end-user choice | may stop: TRUE | 69AC(2)(a) |
| C02 | s 69AC applies; code approved; Chorus does not comply; no choice | FALSE | 69AC(2) "only if" |
| C03 | s 69AC applies; no code approved; end-user chooses permanent disconnection | TRUE | 69AC(2)(b) |
| C04 | s 69AC applies; no code; end-user chooses temporary disconnection only | FALSE | 69AC(2)(b) "(other than a temporary disconnection)" |
| C05 | s 69AC applies; no code; no choice | FALSE | 69AC(2) |
| C06 | s 69AC applies; code NOT approved but Chorus "complies" (input true); no choice | FALSE | 69AC(2)(a) "a copper withdrawal code has been approved and" |
| C07 | s 69AC applies; code approved and complied with; end-user also chooses permanent disconnection | TRUE | 69AC(2) "or" |
| C08 | s 69AC applies; code approved, Chorus complies, but one Sch 2A protection unmet (notice not given); end-user chooses permanent disconnection | TRUE (limb (b)) | 69AC(2)(b) |
| C09 | s 69AD applies (relevant service: unbundled copper local loop network); code approved; complies; protections met | TRUE | 69AD(2)(a) |
| C10 | s 69AD applies (UCLL backhaul); no code; permanent disconnection chosen | TRUE | 69AD(2)(b), 69AD(4)(b) |
| C11 | s 69AD applies; no code; no choice | FALSE | 69AD(2) |
| C12 | s 69AD applies; temporary disconnection chosen; no code | FALSE | 69AD(2)(b) |
| C13 | 69AC(1)(b) fails: Chorus started supplying when the building was already in a specified fibre area | s 69AC does not apply: not TRUE/FALSE from s 69AC (expect refusal or "does not apply") | 69AC(1)(b) "started supplying the service at a time when the end-user's building ... was not located in a specified fibre area" |
| C14 | 69AC(1)(a) fails: no standard terms determination requires supply | s 69AC does not apply | 69AC(1)(a) |
| C15 | 69AC(1)(c) fails: building not (yet) in a specified fibre area by a s 69AB notice | s 69AC does not apply | 69AC(1)(c) |
| C16 | s 69AD: service is not a relevant service (e.g. bitstream) | s 69AD does not apply | 69AD(4) "relevant service means either of the following: ..." |
| C17 | s 69AD(1)(b) fails: service was not a designated access service when supply started | s 69AD does not apply | 69AD(1)(b) |

Schedule 2A cl 1(3) protections (each with s 69AC applying, code approved, Chorus otherwise complying, no end-user choice; baseline all protections met):

| id | change from baseline | expected (may stop / protections met) | provision (Sch 2A cl 1(3)) |
|---|---|---|---|
| P01 | none (all met) | TRUE | cl 1(3) |
| P02 | end-user cannot access a fibre service | FALSE | (a)(i) "access a fibre service" |
| P03 | connection not installable within a reasonable time frame | FALSE | (a)(ii)(A) "within a reasonable time frame" |
| P04 | standard connection, cost to end-user | FALSE | (a)(ii)(B) "at no cost to the end-user" |
| P05 | non-standard connection, cost to end-user | FALSE | (a)(ii)(B) "whether the connection is standard or non-standard, at no cost" |
| P06 | non-standard connection at no cost | TRUE | (a)(ii)(B) |
| P07 | reasonable notice given to end-user and access seeker but not the fibre service provider | FALSE | (b) "the end-user, the access seeker, and the relevant fibre service provider reasonable notice" |
| P08 | no reasonable notice to the end-user | FALSE | (b) |
| P09 | functionality available over fibre except a legacy service | TRUE | (c) "apart from legacy services" |
| P10 | non-legacy functionality not available over fibre | FALSE | (c) |
| P11 | no information about the withdrawal | FALSE | (d)(i) |
| P12 | no information about battery backup / alternative arrangements | FALSE | (d)(ii) "the need to make alternative arrangements, such as battery backup" |
| P13 | information about fibre services not given, and it was reasonably practicable | FALSE | (e) "if it is reasonably practicable to do so" |
| P14 | information about fibre services not given, not reasonably practicable | TRUE | (e) |
| P15 | anchor service declared, not available at premises (nor commercial equivalent) | FALSE | (f) |
| P16 | anchor service declared, only a commercial equivalent available | TRUE | (f) "(or a commercial equivalent)" |
| P17 | no anchor service declared, none available | TRUE | (f) "if an anchor service is declared under section 227" |
| P18 | no Commission 111 contact code in force | FALSE | (g) |
| P19 | prescribed matters not complied with | FALSE | (h) |
| P20 | protection unmet (no 111 contact code), but end-user chose permanent disconnection | may stop TRUE | 69AC(2)(b) |

s 69AE:

| id | inputs | expected | provision |
|---|---|---|---|
| T01 | area is a specified fibre area; LRTS Deed; matter not 111 call services | ceases to apply: TRUE | 69AE(a) |
| T02 | area is a specified fibre area; LRTS Deed; matter relates to 111 call services | ceases: FALSE (still applies) | 69AE(a) "(except to the extent that it relates to 111 call services)" |
| T03 | specified fibre area; TSO Network Service Deed | ceases: TRUE | 69AE(b) |
| T04 | specified fibre area; Network Service Deed; matter relates to 111 | ceases: TRUE (the 111 exception is only in para (a)) | 69AE(b) |
| T05 | area not a specified fibre area; LRTS Deed, non-111 | ceases: FALSE | 69AE "in relation to an area that becomes a specified fibre area" |

## Goal 2: Disputes and periods (ss 239, 241-246, Schedule 2A cl 2)

### Referral and binding effect (ss 241-242)

| id | inputs | expected | provision |
|---|---|---|---|
| D01 | consumer v telecommunications service provider, about rights under a Commission code; referred by consumer | may refer: TRUE | 241(1) "may be referred ... by any of the parties" |
| D02 | same, referred by the provider | TRUE | 241(1) |
| D03 | dispute not about a Commission code | FALSE (not s 241) | 241(1) "about their rights and obligations under a Commission code" |
| D04 | dispute between two providers (no consumer) | FALSE (not s 241) | 241(1) "between a consumer and a telecommunications service provider" |
| D05 | determination; party is scheme member | binding: TRUE | 242(2) |
| D06 | party not scheme member; no appeal lodged | binding: TRUE | 242(3) |
| D07 | non-member appeals; court reverses | binding: FALSE | 242(3) "except if ... lodges an appeal ... and the court modifies or reverses" |
| D08 | non-member appeals; court confirms | binding: TRUE | 242(3), 243(2) |
| D09 | non-member appeals; court modifies | the original determination not binding as made (FALSE) | 242(3) |

### Who may appeal (ss 242(2), 243(1))

| id | inputs | expected | provision |
|---|---|---|---|
| A01 | consumer, not a scheme member | may appeal: TRUE | 243(1) "A consumer or any other party ... who is not a scheme member may" |
| A02 | provider who is a scheme member | FALSE | 242(2) "the scheme member has no right of appeal" |
| A03 | provider party who is not a scheme member | TRUE | 243(1) "any other party to the dispute who is not a scheme member" |
| A04 | the industry dispute resolution scheme itself | not a party; cannot appeal (and 244(1)(b) bars representation) | 244(1)(b) |

Ambiguity: 243(1) could be read as "a consumer [always] or any other non-member". I take "who is not a scheme member" as qualifying both, which is consistent with 242(2).

### Appeal deadline (s 244(1)(a)): "within 5 working days after the determination appealed against is notified to the party ..., or any further time the court allows"

Reading: last day = 5th working day after the notification date; lodging on that day is in time; any further time the court allows extends the last day to the allowed date, whether the application was made before or after the period ended.

| id | notified | anniversary | last day for appeal | provision / working |
|---|---|---|---|---|
| W01 | Fri 16 Oct 2026 | Wellington | Fri 23 Oct 2026 | 19-23 Oct |
| W02 | Tue 20 Oct 2026 | Wellington | Wed 28 Oct 2026 | 21, 22, 23, (26 Labour Day), 27, 28 |
| W03 | Thu 22 Oct 2026 | Wellington | Fri 30 Oct 2026 | 23, 27, 28, 29, 30 |
| W04 | Fri 18 Dec 2026 | Wellington | Tue 5 Jan 2027 | 21-24 Dec (4), 25 Dec-2 Jan out, Mon 4 Jan out (1 Jan Friday), 5 Jan |
| W05 | Mon 21 Dec 2026 | Wellington | Wed 6 Jan 2027 | 22, 23, 24, 5 Jan, 6 Jan |
| W06 | Thu 24 Dec 2026 | Wellington | Mon 11 Jan 2027 | 5, 6, 7, 8, 11 Jan |
| W07 | Wed 20 Jan 2027 | Wellington (25 Jan) | Thu 28 Jan 2027 | 21, 22, (25), 26, 27, 28 |
| W08 | Wed 27 Jan 2027 | Wellington | Wed 3 Feb 2027 | 28, 29, 1, 2, 3 Feb |
| W09 | Wed 27 Jan 2027 | Auckland (Mon 1 Feb 2027) | Thu 4 Feb 2027 | 28, 29, (1 Feb), 2, 3, 4 |
| W10 | Wed 3 Feb 2027 | Wellington | Thu 11 Feb 2027 | 4, 5, (Mon 8 Feb Waitangi Mondayised), 9, 10, 11 |
| W11 | Tue 23 Mar 2027 | Wellington | Thu 1 Apr 2027 | 24, 25, (26 GF), (29 EM), 30, 31, 1 Apr |
| W12 | Tue 20 Apr 2027 | Wellington | Wed 28 Apr 2027 | 21, 22, 23, (26 Anzac Mondayised), 27, 28 |
| W13 | Mon 6 Jul 2026 | Wellington, Matariki 10 Jul 2026 | Tue 14 Jul 2026 | 7, 8, 9, (10), 13, 14 |
| W14 | Sat 17 Oct 2026 (notified on a non-working day) | Wellington | Fri 23 Oct 2026 | 19-23 |
| W15 | Wed 27 May 2026 | Wellington | Thu 4 Jun 2026 | 28, 29, (1 Jun Sovereign's birthday), 2, 3, 4 |
| W16 | Wed 1 Apr 2026 | Wellington | Fri 10 Apr 2026 | 2, (3 GF), (6 EM), 7, 8, 9, 10 |
| W17 | Wed 22 Apr 2026 | Wellington | Thu 30 Apr 2026 | 23, 24, (27 Anzac Mondayised), 28, 29, 30 |

In-time tests (non-member consumer):

| id | notified | lodged | court further time | expected in time | provision |
|---|---|---|---|---|---|
| AT1 | 16 Oct 2026 | 23 Oct 2026 | none | TRUE | 244(1)(a) |
| AT2 | 16 Oct 2026 | 26 Oct 2026 | none | FALSE | 244(1)(a) |
| AT3 | 16 Oct 2026 | 2 Nov 2026 | court allows until 6 Nov 2026 | TRUE | 244(1)(a) "any further time the court allows on an application made before or after that period ends" |
| AT4 | 16 Oct 2026 | 9 Nov 2026 | court allows until 6 Nov 2026 | FALSE | 244(1)(a) |
| AT5 | 18 Dec 2026 | 5 Jan 2027 | none | TRUE | 244(1)(a), s 5 |
| AT6 | 18 Dec 2026 | 6 Jan 2027 | none | FALSE | 244(1)(a) |
| AT7 | 20 Oct 2026 | 28 Oct 2026, by a scheme member provider | none | may not appeal: FALSE | 242(2) |
| AT8 | 16 Oct 2026 | 20 Oct 2026 (early) | none | TRUE | 244(1)(a) "within" |

### Submission periods

s 239(3): "not later than 30 working days after the date on which public notice of the draft code is given" — last day for submissions = 30th working day after; that day is in time.

Schedule 2A cl 2(2): "before the date that is 30 working days after the date on which public notice of the draft code is given (the due date)" — the due date is the 30th working day after; a submission must be made before it, so a submission on the due date is late. cl 2(3): the Commission must have regard to submissions "received before the due date". Difference: one day (the 30th working day itself).

| id | notice given | s 239 last day / Sch 2A due date (30 wd) | provision |
|---|---|---|---|
| S01 | Fri 16 Oct 2026 | Mon 30 Nov 2026 | 19-23 Oct (5), 27-30 (9), Nov 2-6 (14), 9-13 (19), 16-20 (24), 23-27 (29), 30 (30) |
| S02 | Thu 1 Oct 2026 | Fri 13 Nov 2026 | crosses Labour Day |
| S03 | Fri 20 Nov 2026 | Tue 12 Jan 2027 | crosses Christmas period and Mon 4 Jan |
| S04 | Tue 1 Dec 2026 | Thu 21 Jan 2027 | |
| S05 | Mon 11 Jan 2027 | Wed 24 Feb 2027 | crosses 25 Jan and 8 Feb |
| S06 | Mon 1 Mar 2027 | Wed 14 Apr 2027 | crosses Easter 2027 |
| S07 | Thu 24 Dec 2026 | Wed 17 Feb 2027 | notice inside the Christmas period |
| S08 | Tue 5 Jan 2027 | Thu 18 Feb 2027 | |

In-time tests:

| id | regime | notice | submitted | expected in time |
|---|---|---|---|---|
| S09 | s 239(3) Commission code | 16 Oct 2026 | 30 Nov 2026 | TRUE ("not later than") |
| S10 | s 239(3) | 16 Oct 2026 | 1 Dec 2026 | FALSE |
| S11 | Sch 2A cl 2(2) copper code | 16 Oct 2026 | 30 Nov 2026 | FALSE ("before the date") |
| S12 | Sch 2A cl 2(2) | 16 Oct 2026 | 27 Nov 2026 | TRUE |
| S13 | Sch 2A cl 2(2) | 16 Oct 2026 | Sun 29 Nov 2026 | TRUE (before the due date; nothing requires a working day) |
| S14 | s 239(3) | 20 Nov 2026 | 12 Jan 2027 | TRUE |
| S15 | Sch 2A cl 2(2) | 20 Nov 2026 | 12 Jan 2027 | FALSE |
| S16 | Sch 2A cl 2(2) | 20 Nov 2026 | 11 Jan 2027 | TRUE |

### s 246 reviews

s 246(1): "must review each industry dispute resolution scheme at least once every 3 years." Reading: the next review must take place no later than 3 calendar years after the previous review (same day and month); 29 Feb rolls to 28 Feb. Ambiguity: whether measured from start or completion of the last review; I take the date of the last review as the input. Also ambiguous whether a review exactly 3 years later is in time: "at least once every 3 years" — I take the anniversary day as the last permitted day (in time).

| id | last review | expected latest next review / test | provision |
|---|---|---|---|
| R01 | 15 Mar 2024 | 15 Mar 2027 | 246(1) |
| R02 | 15 Mar 2024, next review 15 Mar 2027 | in time: TRUE | 246(1) |
| R03 | 15 Mar 2024, next review 16 Mar 2027 | in time: FALSE (overdue) | 246(1) |
| R04 | 29 Feb 2024 | 28 Feb 2027 (ambiguous; 1 Mar 2027 is the other reading) | 246(1) |
| R05 | 1 Oct 2023, assessed on 16 Oct 2026 | overdue: TRUE (due by 1 Oct 2026) | 246(1) |

s 246(6): "must give the following persons 20 working days to make submissions on a draft report". Reading: the period runs from the day after the draft report is given; last day = 20th working day after.

| id | draft report given | last day for submissions | provision |
|---|---|---|---|
| R06 | Mon 2 Nov 2026 | Mon 30 Nov 2026 | 246(6) |
| R07 | Thu 10 Dec 2026 | Mon 18 Jan 2027 | 246(6), s 5 |
| R08 | Tue 13 Apr 2027 | Wed 12 May 2027 | 246(6) |
| R09 | Mon 31 May 2027 | Wed 30 Jun 2027 | crosses 7 Jun (Sovereign) and 25 Jun (Matariki 2027) |
| R10 | Fri 16 Oct 2026 | Mon 16 Nov 2026 | crosses Labour Day |

## Goal 3: Levy late-payment interest (s 14)

s 14(1): "If any service provider ... fails to pay the whole amount of that levy by the date specified ..., the service provider must pay interest on the unpaid amount at the rate of 1.5% per month calculated from the date payment is due." s 14(2): "Interest will be calculated in monthly instalments for each month, or part of each month, that the payment is due."

Readings taken: simple interest (no compounding: "on the unpaid amount"); payment on or before the due date attracts no interest ("by the date"); months counted from the due date: month k ends on the same day-of-month k months later (clamped to the last day of a shorter month); payment on that end day completes month k without starting month k+1. A payment one day after the due date is a part month, so one full instalment (1.5%). Ambiguity: an end-of-month due date could alternatively roll to month-ends; I take day-of-month clamping (28 Feb + 1 month = 28 Mar).

| id | levy / unpaid | due | paid | months | interest | provision |
|---|---|---|---|---|---|---|
| L01 | 10000 | 20 Jan 2027 | 20 Jan 2027 | 0 | 0 | 14(1) "by the date" |
| L02 | 10000 | 20 Jan 2027 | 15 Jan 2027 | 0 | 0 | 14(1) |
| L03 | 10000 | 20 Jan 2027 | 21 Jan 2027 | 1 | 150 | 14(2) "part of each month" |
| L04 | 10000 | 20 Jan 2027 | 20 Feb 2027 | 1 | 150 | 14(2) |
| L05 | 10000 | 20 Jan 2027 | 21 Feb 2027 | 2 | 300 | 14(2) |
| L06 | 10000 | 20 Jan 2027 | 19 Jul 2027 | 6 | 900 | 14(2) |
| L07 | 10000 | 31 Jan 2027 | 28 Feb 2027 | 1 | 150 | month-end clamping |
| L08 | 10000 | 31 Jan 2027 | 1 Mar 2027 | 2 | 300 | |
| L09 | 10000 | 31 Oct 2026 | 30 Nov 2026 | 1 | 150 | |
| L10 | 10000 | 31 Oct 2026 | 1 Dec 2026 | 2 | 300 | |
| L11 | 10000 | 30 Nov 2026 | 31 Dec 2026 | 2 | 300 | month 1 ends 30 Dec |
| L12 | 10000 | 28 Feb 2027 | 28 Mar 2027 | 1 | 150 | |
| L13 | 10000 | 28 Feb 2027 | 31 Mar 2027 | 2 | 300 | (other reading: 1) |
| L14 | 6000 unpaid (4000 of 10000 paid on time) | 20 Jan 2027 | 10 Feb 2027 | 1 | 90 | 14(1) "on the unpaid amount" |
| L15 | 10000 | 16 Oct 2026 | 16 Oct 2027 | 12 | 1800 | simple, not compounded |
| L16 | 10000 | 16 Oct 2026 | 17 Oct 2027 | 13 | 1950 | |
| L17 | 0 unpaid | 20 Jan 2027 | 20 Mar 2027 | n/a | 0 | nothing unpaid |
| L18 | 2000 | 25 Dec 2026 | 4 Jan 2027 | 1 | 30 | working days irrelevant to s 14 |

## Things that cannot be input/output tests

- s 245 compliance orders, s 246(2)-(5) content of reviews, and Sch 2A cl 1(1)-(2), (4), cl 3-5: discretionary or process duties without computable outputs.
- Whether a time frame is "reasonable" or notice "reasonable" (Sch 2A cl 1(3)(a)(ii)(A), (b)), or something "reasonably practicable" ((e)): judgments, taken as boolean inputs.
- 69AC(3)/69AD(3) (Chorus not required to supply a new end-user or resupply): a statement of no duty; testable only if the encoding has a function for it.
- s 243(3) (no appeal from the court's decision) and 244(1)(c): no input/output beyond a constant.

## Added after opening the encoding (expected values above unchanged)

Not expressible against the encoding (no function or input), so no test was written:
- C13-C17 (the section does not apply): the encoding has one boolean `section 69AC or 69AD applies`, and when it is FALSE `Chorus may stop supplying the copper service` returns TRUE. My expectation was a refusal or a "does not apply" result, not TRUE or FALSE. A boolean cannot carry that, so this is recorded as a difference and not as a test.
- P13, P14 (cl 1(3)(e), fibre-service information "if reasonably practicable") and P19 (cl 1(3)(h), prescribed matters): there is no input for either.
- T03, T04 (TSO Network Service Deed, s 69AE(b)): only the LRTS Deed has a function.
- D01-D09 (s 241 referral, s 242 binding effect): there is no function for either.
- A04 (the scheme as appellant): there is no input for it.
- Combined inputs: P03/P04/P05 share `fibre installed in reasonable time at no cost`; P07/P08 share the notice input; P11/P12 share the information input; P09, P16 and P17 reduce to an input being TRUE. These are tested only to that extent.
