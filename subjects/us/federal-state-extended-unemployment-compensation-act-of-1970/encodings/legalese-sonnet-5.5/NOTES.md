# Federal-State Extended Unemployment Compensation Act of 1970: an L4 encoding (legalese-sonnet-5.5)

**What this is.** An encoding in L4 of the Federal-State Extended Unemployment Compensation Act of 1970 (Pub. L. 91-373, title II, 84 Stat. 708; sections 201 to 208), as the Office of the Law Revision Counsel (OLRC) sets it out in the note under 26 U.S.C. 3304.
Layer 1 is the law, objectively: `euca-nouns.l4` (types), `euca-shared.l4` (dates the Act states, small arithmetic), and the section modules `euca-s202-work-test.l4`, `euca-s202-conditions.l4`, `euca-s202-account.l4`, `euca-s202-payable.l4`, `euca-s203-period.l4`, `euca-s203-indicators.l4`, `euca-s204-payments.l4`, `euca-s205-definitions.l4`, `euca-s207-dates.l4`, `euca-s208-sea.l4`.
Layer 2 is one thin seat layer: `euca-seat.l4` (38 questions) and `euca-cases-seat.l4` (111 asserted cases).
Layer-1 tests: `euca-tests-period.l4`, `euca-tests-indicators.l4`, `euca-tests-eligibility.l4`, `euca-tests-account.l4`, `euca-tests-payments.l4`.
Written by one session (Claude Sonnet 5.5) from `euca-1970-note-26usc3304.txt` alone, with the stable `l4` 1.6.98 (sha256 `82ea44ad...263e`).
Every layer-1 rule has a quoted source line (`-- src:N | text`, taken mechanically from the text) and an `@ref` naming the section and lines.

**The source is a plain-text rendering, not the official text.**
`euca-1970-note-26usc3304.txt` is a plain-text rendering made by a converter script from the OLRC's USLM XML (release point Public Law 119-121, current through 2026-10-09).
It is not the official text and it is not marked up.
The Act is not classified to any Code section; the Statutes at Large text, as amended, is the law, and the OLRC note is an editorial reproduction of it.
Nothing here has been checked against the official text.

**Square brackets are OLRC editorial matter, not law.**
Catch-lines such as `[Payment of Extended Compensation]`, `[formerly I.R.C. 1954]`, `[probably means subpar. (C)]`, `[see Short Title of 1970 Amendment note ...]`, the dates in square brackets after "the date of enactment" (`[Aug. 10, 1970]`, `[Dec. 17, 2010]`, `[Feb. 22, 2012]`), and the whole of lines 164 to 215 (the OLRC's notes on the effective dates of the amending laws) are neither encoded as provisions nor treated as law.
Where the Act's own words say "the date of enactment" and the figure lives only in a bracket, the figure is carried as a value with the bracket cited (fork register F-9, F-26, F-33).
Two of the bracketed "[probably means ...]" corrections are followed in the encoding (F-15, F-17), and so are "[now 233(c)]" and "state [State]" (F-38); each is a fork-register row.
The converter also dropped the text of several of the bracketed notes (lines 170 to 173, 177 to 192, 198 to 201, 206 to 215 print only fragments).

**Target and binary.** The target dialect is `main`, build 1.6.98 (the stable binary).
Weeks are carried as the `DATE` on which the week begins; rates of unemployment are plain percentage points (5.5 means 5.5 per cent); money is in dollars.

## Seat

**The individual to whom the Act is applied**: an unemployed worker in the United States who has used up regular unemployment compensation (regular compensation, "exhausted") in a period of high unemployment, and asks whether extended compensation is payable for a week, for how many weeks, and what must be done (look for work, accept suitable work, avoid a disqualification) to keep getting it.
Why this seat: the Act speaks mostly to State laws ("a State law shall provide ..."), but every one of its operative rules ends in what happens to this person: whether they are paid for a week (s 202(a)), how much their account holds (s 202(b)), whether an interstate claim is cut off (s 202(c)), which weeks are theirs (s 203(c)), and when the State's period starts and stops (s 203, which decides whether the person has any eligibility period at all).
Decisions are phrased as that person would ask them ("Must I ...?", "Am I ...?", "Will I be denied ...?", "How much ...?"), and the facts are ones the person can state.
Where a provision addresses only an official or another government, nothing is invented for the person: section 204 (the Federal share of the cost, paid by the Secretary of the Treasury to the State), section 203(b)(2) and (e)(2) and (f)(3) (the Secretary's and the State agency's functions) are encoded in layer 1 only, and the seat asks only the questions the person can ask about them (whether notice must be published; the rate; whether the State is "on").
The seat is one person in one State for one week at a time; the weekly question is the master question `Is extended compensation payable to me for this week`.
The employer is not a party to the Act; there is no second seat.
The seat questions group under `§` headings in the order of the text: ss 202(a)(1) and (2); 202(a)(3); 202(a)(4), (5), (7); 202(b); 202(c); 202 together; 203; 205; 207; 208.
Section 208 (self-employment assistance) arises only if the person's State has such a program; its heading says so.
Inputs are plain facts; the Act's own figures are used as the Act states them; the federal minimum wage, the State's rates and elections, and the State agency's judgments are inputs (F-36).

## Jural relations

The Act is addressed to State laws, so most relations are between the individual and the State (which bears the duty to pay under its State law), or between the State and the United States.
Hohfeld's terms: right/duty, privilege/no-right, power/liability, immunity/disability.

| provision | holder | bearer of the correlative | relation | L4 rule |
|---|---|---|---|---|
| s 202(a)(1) | the individual: right to extended compensation for a week in the eligibility period who has exhausted regular compensation and has no other rights to compensation | the State: duty to pay (its law must provide it) | right / duty | `the State law must provide payment of extended compensation for the week`; `extended compensation is payable for the week` |
| s 202(a)(2) | the State: power to apply its regular-claim terms to extended claims | the individual: liability to those terms (unless inconsistent with the title) | power / liability | `a State rule for regular compensation claims applies to extended compensation claims` |
| s 202(a)(3)(A), (B) | the State: privilege not to pay (no duty) for a week in which the individual fails to accept or apply for suitable work or to seek work, and for later weeks until 4 weeks' work with pay of 4 times the weekly benefit amount | the individual: no-right to the payment | privilege / no-right | `extended compensation is denied under clause (i) for the offer or referral`; `extended compensation is denied under clause (ii) for failing to seek work`; `the week begins during the period of ineligibility after an earlier failure`; `the work test bars extended compensation for the week` |
| s 202(a)(3)(D) | the individual: privilege to turn down the four kinds of job in subparagraph D without a denial | the State: no-right to deny | privilege / no-right | `an exception in subparagraph D applies` |
| s 202(a)(3)(E), (C) | none (definitions of "actively engaged in seeking work" and "suitable work") | | none | `the individual is treated as actively engaged in seeking work`; `the work is suitable work` |
| s 202(a)(3)(F) | the individual: right to be referred to suitable work to which none of D(i) to (iv) applies | the State: duty to provide for the referral | right / duty | `the State law must provide for referring applicants to the work` |
| s 202(a)(4) | the State: privilege to keep a disqualification in force unless its termination rests on later employment | the individual: no-right to extended compensation while it stands | privilege / no-right | `the disqualification still bars extended compensation` |
| s 202(a)(5) | the State: privilege not to pay without 20 weeks' employment or its wage equivalent (as the State law chooses) | the individual: no-right | privilege / no-right | `the result of the employment requirement` |
| s 202(a)(6) | the United States: privilege not to pay the State its share for a week the rules of (3), (4), (5) would not have allowed | the State: no-right to that payment | privilege / no-right | `no payment is made to the State for the week under section 202(a)(6)`; `the State may not be paid its share of extended compensation paid for the week` |
| s 202(a)(7) | the individual: immunity from paragraphs (3) and (4) for weeks after 6 March 1993 and before 1 January 1995 | the State: disability to apply them | immunity / disability | `paragraphs (3) and (4) of section 202(a) apply to the week` |
| s 202(b)(1) | the individual: right to an account of at least the least of three amounts | the State: duty to establish it | right / duty | `the amount the extended compensation account must hold` |
| s 202(b)(2), (3) | none (the weekly benefit amount; the high unemployment figures and the period) | | none | `the weekly benefit amount for a week`; `the week begins in a high unemployment period` |
| s 202(c)(1) | the State: privilege not to pay extended compensation on an interstate claim filed in a State with no extended benefit period, after the first two weeks | the individual: no-right to payment on that claim | privilege / no-right | `payment of extended compensation is not made for the week under section 202(c)(1)` |
| s 202(c)(2) | the individual: immunity from (c)(1) for the first 2 weeks | the State: disability | immunity / disability | `the week is one of the first 2 weeks payable pursuant to the interstate claim` |
| s 202(c)(3) | the State: immunity from section 3304(a)(9)(A) of the Internal Revenue Code for a denial (c) requires | the individual and the Secretary: disability to rely on that provision | immunity / disability | `section 3304(a)(9)(A) of the Internal Revenue Code does not apply to the denial` |
| s 203(a), (b)(1) | none (counting rules for when a period begins and ends) | | none | `the week with which an extended benefit period begins`; `the week with which an extended benefit period ends` |
| s 203(b)(2) | (no holder is named): the Secretary of Labor bears a duty to have notice published in the Federal Register | the Secretary: duty | duty owed generally | `the Secretary must cause notice to be published in the Federal Register` |
| s 203(c) | none (the eligibility period is a counting rule) | | none | `the week is in the individual's eligibility period` |
| s 203(d), (e)(2) | the State agency: power to determine the "on" and "off" indicators in accordance with the Secretary's regulations | the individual: liability to the determination | power / liability | `the party who makes the determinations under subsection (d)` |
| s 203(d), (f)(1) | the State: power to adopt, by law, the 6 per cent option, the three-year option and the alternative trigger | the individual: liability to the State's choice | power / liability | `the State law's 6 per cent option applies to the week`; `the alternative trigger applies to the week` |
| s 203(f)(3) | the Secretary of Labor: power to determine the rate of total unemployment and its seasonal adjustment | the State: liability | power / liability | `the party who determines the rate of total unemployment and any seasonal adjustment` |
| s 203(d), (e), (f) (the tests) | none (the indicator tests themselves are conditions) | | none | `there is a State on indicator for the week` and its parts |
| s 204(a)(1) | the State: right to one-half of the sharable compensation | the United States (the Secretary of the Treasury pays): duty | right / duty | `the amount payable to the State for the week` |
| s 204(a)(2), (3) | the United States: privilege not to pay for the excluded compensation, and to reduce the sum | the State: no-right | privilege / no-right | `no payment is made to the State in respect of the compensation under section 204(a)(2)(A), (B) or (C)`; `the compensation counted for the week after section 204(a)(2)`; `the amount payable after the reduction in section 204(a)(3)` |
| s 204(b), (c) | none (they define "sharable" extended and regular compensation) | | none | `the sharable extended compensation for the week`; `the sharable regular compensation for the week` |
| s 204(d) | the State: right to monthly payments in advance or by reimbursement; the Secretary: power to estimate and to correct | the Secretary: duty to pay the estimated sum; the State: liability to the correction | right / duty; power / liability | `the sum to be paid to the State for the calendar month` |
| s 204(e) | the State: right to the certified sums; the Secretary of Labor: duty to certify | the Secretary of the Treasury: duty to pay on the certification | right / duty | `the party who certifies the sums payable to each State`; `the party who pays each State the certified sums`; `the sum the Secretary of the Treasury must pay the State` |
| s 205 | none (definitions) | | none | `euca-s205-definitions.l4` |
| s 206 | none (amendment of another instrument; not encoded) | | none | |
| s 207(a), (b), (c) | none (date gates: when a period may begin, when section 204 applies, when section 3304(a)(11) binds a State law) | | none | `an extended benefit period may begin with the week`; `section 204 applies to the week of unemployment`; `section 3304(a)(11) of the Internal Revenue Code is a requirement for the State law for the week` |
| s 208(a)(1) | the State: power to establish a self-employment assistance program for weeks after 22 February 2012 | the individual: liability to take part in or be paid under it | power / liability | `extended compensation may be paid as a self-employment assistance allowance for the week` |
| s 208(a)(2) | the individual: right to the allowance, paid out of the extended compensation account | the State agency: duty to pay; the account is reduced | right / duty | `the amount in the extended compensation account after the allowance is paid` |
| s 208(a)(3) | the individual: right to up to 26 weeks of allowances together with section 4001(j) of the 2008 Act | the State: duty; disability of the individual beyond 26 weeks | right / duty | `self-employment assistance allowances may be provided for a further week`; `the individual is eligible for allowances under section 4001(j) of the Supplemental Appropriations Act, 2008 until the combined eligibility limit is reached` |
| s 208(c) | the State agency: privilege to withhold allowances unless it reasonably expects at least 13 times the weekly benefit amount | the individual: no-right | privilege / no-right | `the individual may receive self-employment assistance allowances under section 208(c)` |
| s 208(d)(1) | the individual: power to discontinue at any time | the State: liability | power / liability | `the individual may elect to discontinue participation at any time` |
| s 208(d)(2) | the individual: right to extended compensation for later weeks to the extent amounts remain | the State: duty | right / duty | `the individual receives extended compensation payments for subsequent weeks`; `the most extended compensation that may be paid for subsequent weeks` |
| s 208(b) | none (what a self-employment assistance program is: modifications to section 3306(t) as data) | | none | `the program is a self-employment assistance program for this section` and the constants beside it |

## Coverage table

Dispositions: `encoded`, `inert` (with the reason), `repealed or blank in this text`, `fork`.
A `fork` row is encoded: the reading taken is in the fork register under the F-number given.
The text has 8 sections (ss 201 to 208) and 22 catch-lined headings in square brackets (8 section headings such as `[Short Title]` and 14 subsection headings such as `[State Law Requirements]` and `[Amount Payable]`); the table has 99 rows; no row is `deferred`.
`Where` names a module and, in quotes, the rule; a rule name that is the same as the provision's title is written in short.

| provision | source lines | disposition | where | note |
|---|---|---|---|---|
| title and credit line | src:18-19 | inert | euca-shared `the date this title was enacted` carries the date | pure citation or title: it names the Act and lists the amending laws and their dates; nothing in it creates a right, duty or condition. The enactment date, 10 August 1970, is carried from here (F-26). |
| s 201 | src:21-22 | inert | none | pure citation or title: "This title may be cited as the Federal-State Extended Unemployment Compensation Act of 1970"; a short title decides nothing for the individual. |
| s 202(a)(1), first sentence | src:26 | encoded | euca-s202-conditions `the individual has no other rights to compensation for the week`, `the State law must provide payment of extended compensation for the week`; euca-s202-payable `extended compensation is payable for the week` | F-13, F-14. |
| s 202(a)(1), second sentence (exhaustion) | src:26 | fork | euca-s202-conditions `the individual has exhausted all rights to regular compensation` | (A) all regular compensation received, (B) benefit year expired; F-13. |
| s 202(a)(2) | src:27 | encoded | euca-s202-conditions `a State rule for regular compensation claims applies to extended compensation claims` | whether a State rule is "inconsistent with the provisions of this title" is an input (F-36). |
| s 202(a)(3)(A)(i) | src:28-30 | fork | euca-s202-work-test `the individual fails to accept an offer of suitable work or to apply for suitable work to which referred`, `extended compensation is denied under clause (i) for the offer or referral`, `... for any offer or referral` | accept an offer, apply for a referral; "[probably means subpar. (C)]" followed; F-15. |
| s 202(a)(3)(A)(ii) with (I), (II) and the closing proviso | src:31-34 | fork | euca-s202-work-test `the jury duty exemption applies`, `the hospitalization exemption applies`, `extended compensation is denied under clause (ii) for failing to seek work` | each exemption needs its own two conditions; F-16. |
| s 202(a)(3)(B) | src:35-37 | fork | euca-s202-work-test `the period of ineligibility after an earlier failure has ended`, `the week begins during the period of ineligibility after an earlier failure`, `weeks of employment still needed to end the period of ineligibility`, `remuneration still needed to end the period of ineligibility` | F-17. |
| s 202(a)(3)(C) | src:38 | encoded | euca-s202-work-test `the work is suitable work` | |
| s 202(a)(3)(D)(i) | src:39-42 | encoded | euca-s202-work-test `the pay for the position does not exceed the benefit amount plus supplemental benefits` | "does not exceed": at most; F-18. |
| s 202(a)(3)(D)(ii) | src:43 | encoded | euca-s202-work-test `the position was neither offered in writing nor listed with the State employment service` | F-18. |
| s 202(a)(3)(D)(iii) | src:44 | encoded | euca-s202-work-test `the failure would not result in a denial under the State law` | the State law's denial is an input (F-36). |
| s 202(a)(3)(D)(iv) | src:45-47 | encoded | euca-s202-work-test `the position pays less than the higher of the minimum wages` | strictly less; F-18. |
| s 202(a)(3)(E) | src:48-50 | encoded | euca-s202-work-test `the individual is treated as actively engaged in seeking work` | both effort and evidence. |
| s 202(a)(3)(F) | src:51 | encoded | euca-s202-work-test `the State law must provide for referring applicants to the work` | same set as the denied offers (asserted). |
| s 202(a)(4) | src:52 | encoded | euca-s202-conditions `the termination of the disqualification applies to eligibility for extended compensation`, `the disqualification still bars extended compensation`, `a disqualification still bars extended compensation` | |
| s 202(a)(5), first and second sentences | src:53 | fork | euca-s202-conditions `the individual had 20 weeks of full-time insured employment`, `the earnings exceed 40 times the most recent weekly benefit amount`, `the earnings exceed one and a half times the highest quarter` | "exceed" governs both wage methods; F-19. |
| s 202(a)(5), third sentence (the State chooses the method) | src:53 | fork | euca-s202-conditions `the State law has chosen at least one method`, `the result of the employment requirement` | no method chosen returns a named not-covered constructor; F-19. |
| s 202(a)(6) | src:54 | encoded | euca-s202-conditions `no payment is made to the State for the week under section 202(a)(6)`; euca-s202-payable `the State may not be paid its share of extended compensation paid for the week` | F-20. |
| s 202(a)(7) | src:55 | encoded | euca-s202-conditions `paragraphs (3) and (4) of section 202(a) apply to the week`; euca-s202-payable `the work test bars extended compensation for the week unless section 202(a)(7) suspends it`, `a disqualification bars extended compensation for the week unless section 202(a)(7) suspends it` | F-21, F-25. |
| s 202(b)(1), chapeau and (A), (B), (C) | src:56-59 | encoded | euca-s202-account `the amount under section 202(b)(1)(A)`, `(B)`, `(C)`, `the least of the amounts in section 202(b)(1)(A), (B) and (C)` | F-22. |
| s 202(b)(1), closing "except that" reduction | src:60 | encoded | euca-s202-account `the amount the extended compensation account must hold`, `the number of whole weeks the extended compensation account covers` | the State's choice to reduce is an input; F-22. |
| s 202(b)(2) | src:61 | encoded | euca-s202-account `the weekly benefit amount for a week` | |
| s 202(b)(3)(A) | src:62-66 | encoded | euca-s202-account the 0.8 / 20 / 46 figures inside `the amount under section 202(b)(1)(A)`, `(B)`, `(C)` | |
| s 202(b)(3)(B) | src:62,67 | fork | euca-s202-account `the percentage substituted in section 202(b)(3)(B)`, `the reading for the high unemployment period`, `the week begins in a high unemployment period` | F-23. |
| s 202(c)(1) | src:68-70 | fork | euca-s202-account `payment of extended compensation is not made for the week under section 202(c)(1)` | F-24. |
| s 202(c)(2) | src:71 | fork | euca-s202-account `the week is one of the first 2 weeks payable pursuant to the interstate claim` | F-24. |
| s 202(c)(3) | src:72 | encoded | euca-s202-account `section 3304(a)(9)(A) of the Internal Revenue Code does not apply to the denial` | IRC 3304(a)(9)(A) is outside the text (dependencies). |
| s 203(a)(1) | src:76-77 | fork | euca-s203-period `the third week after the first week with a State on indicator`, `the week with which an extended benefit period begins`, `the first week with a State on indicator`, `the extended benefit period that follows the readings` | F-2. |
| s 203(a)(2) | src:76,78 | fork | euca-s203-period `the third week after the first week with a State off indicator`, `the week with which an extended benefit period ends`, `the first week with a State off indicator from the week` | F-2, F-5. |
| s 203(b)(1)(A) | src:79-80 | fork | euca-s203-period `the earliest last week of an extended benefit period of thirteen consecutive weeks` | F-3. |
| s 203(b)(1)(B) | src:79,81 | fork | euca-s203-period `the earliest week with which a new extended benefit period may begin` | F-4. |
| s 203(b)(2) | src:82 | encoded | euca-s203-period `the Secretary must cause notice to be published in the Federal Register`, `the party who must cause notice of a determination to be published` | a duty on an official; it decides for the person only whether notice must appear. |
| s 203(c) | src:83 | fork | euca-s203-period `the week begins in the extended benefit period`, `the week is in the benefit year`, `the benefit year ends within the extended benefit period`, `the week is in the individual's eligibility period` | F-6. |
| s 203(d)(1) | src:84-87 | encoded | euca-s203-indicators `the rate equals or exceeds 120 per centum of the average of the corresponding rates`, `the rate equals or exceeds 5 per centum`, `there is a State on indicator under paragraph (1) of section 203(d)` | F-11. |
| s 203(d)(2) | src:88 | encoded | euca-s203-indicators `there is a State off indicator under section 203(d)` | |
| s 203(d), closing paragraph, first sentence (1977 option) | src:89 | fork | euca-s203-indicators `the State law's 6 per cent option applies to the week`, `there is a State on indicator under section 203(d)` | F-8. |
| s 203(d), closing paragraph, second sentence (2010 option) | src:89 | fork | euca-s203-indicators `the State law's three-year comparison option of section 203(d) applies to the week`, `the average of such rates for the corresponding thirteen-week period in each of the preceding calendar years` | the date 17 December 2010 is an OLRC bracket; F-9. |
| s 203(d), closing paragraph, third sentence (covered employment) | src:89 | fork | euca-s203-indicators `the average monthly covered employment for a thirteen-week period` | F-10. |
| s 203(e)(1) | src:90-92 | fork | euca-s203-indicators `the rate of insured unemployment` | zero covered employment returns NOTHING; F-10. |
| s 203(e)(2) | src:93 | encoded | euca-s203-indicators `the party who makes the determinations under subsection (d)` | the Secretary's regulations are outside the text (dependencies). |
| s 203(f)(1) | src:94-99 | fork | euca-s203-indicators `the alternative trigger applies to the week`, `the average rate of total unemployment equals or exceeds the percentage`, `the average rate equals or exceeds 110 percent of the rate for a corresponding period in a preceding year`, `the alternative trigger test is met at the percentage`, `there is a State on indicator under section 203(f)`, `there is a State off indicator under section 203(f)`, `there is a State on indicator for the week`, `there is a State off indicator for the week` | F-7, F-12. |
| s 203(f)(2) | src:100 | fork | euca-s203-indicators `the State law's three-year comparison option of section 203(f) applies to the week` | F-9, F-12. |
| s 203(f)(3) | src:101 | encoded | euca-s203-indicators `the party who determines the rate of total unemployment and any seasonal adjustment` | |
| s 204(a)(1) | src:105-108 | encoded | euca-s204-payments `the amount payable to the State for the week but for section 204(a)(3)`, `the amount payable to the State for the week` | F-27. |
| s 204(a)(2)(A) | src:109 | encoded | euca-s204-payments `no payment is made to the State in respect of the compensation under section 204(a)(2)(A), (B) or (C)` | the Federal reimbursement is an input (dependencies). |
| s 204(a)(2)(B) | src:109 | encoded | euca-s204-payments (same rule) | the "first week" is an input flag (F-27). |
| s 204(a)(2)(C) | src:109 | encoded | euca-s204-payments (same rule) | section 233 of the Trade Act of 1974 is outside the text (dependencies). |
| s 204(a)(2)(D) | src:109 | encoded | euca-s204-payments `the compensation counted for the week after section 204(a)(2)` | rounding down trims only an excess. |
| s 204(a)(3) | src:110 | fork | euca-s204-payments `the amount payable after the reduction in section 204(a)(3)` | total base period wages of 0: no reduction; F-28. |
| s 204(b) | src:111 | fork | euca-s204-payments `the sharable extended compensation for the week` | F-29. |
| s 204(c)(1) | src:112-113 | encoded | euca-s204-payments `the sharable regular compensation for the week` | the week must be in the eligibility period (input flag). |
| s 204(c)(2) | src:112,114 | fork | euca-s204-payments `the upper limit of the sharable regular compensation band`, `the sharable regular compensation for the week` | the sentence is garbled in the text; F-30. |
| s 204(d) | src:115 | fork | euca-s204-payments `the sum to be paid to the State for the calendar month` | encoded minimally (F-31). |
| s 204(e) | src:116 | fork | euca-s204-payments `the party who certifies the sums payable to each State`, `the party who pays each State the certified sums`, `the sum the Secretary of the Treasury must pay the State` | encoded minimally (F-31). |
| s 205(1) "compensation" | src:120 | encoded | euca-s205-definitions `the payment is compensation` | |
| s 205(2) "regular compensation" | src:121 | encoded | euca-s205-definitions `the payment is regular compensation` | |
| s 205(3) "extended compensation" | src:122 | encoded | euca-s205-definitions `the payment is extended compensation` | |
| s 205(4) "additional compensation" | src:123 | encoded | euca-s205-definitions `the payment is additional compensation` | |
| s 205(5) "benefit year" | src:124 | encoded | euca-s205-definitions `the benefit year under section 205(5)` | the applicable State law supplies the dates (input). |
| s 205(6) "base period" | src:125 | encoded | euca-s205-definitions `the base period under section 205(6)` | the applicable State law supplies the dates (input). |
| s 205(7) "Secretary" | src:126 | encoded | euca-s205-definitions `the Secretary under section 205(7)` | |
| s 205(8) "State" | src:127 | fork | euca-s205-definitions `the status of the place under the definition of State` | "includes": a place not named is neither included nor excluded; F-32. |
| s 205(9) "State agency" | src:128 | encoded | euca-s205-definitions `the agency is the State agency` | |
| s 205(10) "State law" | src:129 | encoded | euca-s205-definitions `the law is the State law` | the Secretary's approval under IRC 3304 is an input (dependencies). |
| s 205(11) "week" | src:130 | encoded | euca-s205-definitions `the week under section 205(11)` | the State law supplies the day the week begins (F-1). |
| s 206 | src:132-133 | inert | none | an amendment of another instrument: it added paragraph (11) to section 3304(a) of the Internal Revenue Code, and the text itself says so in brackets. Its content is the requirement that a State law provide extended compensation, which this Act's sections 202, 203 and 207 spell out and which appears here as the premise "for purposes of section 3304(a)(11)". |
| s 207(a)(1) | src:136-137 | encoded | euca-s207-dates `an extended benefit period may begin with the week` | F-25, F-26. |
| s 207(a)(2) | src:136,138 | encoded | euca-s207-dates `section 204 applies to the week of unemployment` | |
| s 207(b)(1) | src:139-140 | fork | euca-s207-dates `an extended benefit period may begin with the week`; euca-shared `60 days after the date this title was enacted` | the enactment date 10 August 1970 is from the OLRC bracket and title block; F-26. |
| s 207(b)(2) | src:139,141 | fork | euca-s207-dates `the extended benefit period is determined solely by the State on and off indicators`; used by euca-s203-period | F-26. |
| s 207(b)(3) | src:139,142 | encoded | euca-s207-dates `section 204 applies to the week of unemployment` (second argument) | |
| s 207(c)(1) | src:143-144 | encoded | euca-s207-dates `section 3304(a)(11) of the Internal Revenue Code is a requirement for the State law for the week` | the converse of "shall not be a requirement"; F-25. |
| s 207(c)(2) | src:143,145 | encoded | euca-s207-dates (same rule) | |
| s 208(a)(1) | src:148 | fork | euca-s208-sea `extended compensation may be paid as a self-employment assistance allowance for the week` | the enactment date 22 February 2012 is from the OLRC bracket; F-33. |
| s 208(a)(2) | src:149 | encoded | euca-s208-sea `the amount in the extended compensation account after the allowance is paid` | |
| s 208(a)(3)(A) | src:150-151 | encoded | euca-s208-sea `the combined eligibility limit in weeks`, `self-employment assistance allowances may be provided for a further week`, `weeks of allowances still available under the combined eligibility limit` | F-33. |
| s 208(a)(3)(B) | src:150,152 | encoded | euca-s208-sea `the individual is eligible for allowances under section 4001(j) of the Supplemental Appropriations Act, 2008 until the combined eligibility limit is reached` | section 4001(j) and title IV of Pub. L. 110-252 are outside the text (dependencies). |
| s 208(b), chapeau | src:153 | encoded | euca-s208-sea `the program is a self-employment assistance program for this section` | IRC 3306(t) is outside the text (dependencies); F-34. |
| s 208(b)(1) | src:154 | encoded | euca-s208-sea `the words read in place of regular unemployment compensation under the State law` | data: the replacement words. |
| s 208(b)(2) | src:155 | encoded | euca-s208-sea `the paragraphs of the section 3306(t) definition that do not apply to a program under this section` | data. |
| s 208(b)(3) | src:156-157 | encoded | euca-s208-sea `the words that clause (i) of paragraph (3)(C) is deemed to state` | data: the training clause, copied from the text. |
| s 208(b)(4) | src:158 | encoded | euca-s208-sea `the percentage read in place of 5 percent in paragraph (4) of the section 3306(t) definition` | data: 1. |
| s 208(b)(5) | src:159 | encoded | euca-s208-sea (the same list as (b)(2)) | data. |
| s 208(c) | src:160 | fork | euca-s208-sea `the individual may receive self-employment assistance allowances under section 208(c)` | "reasonable expectation" is the State agency's judgment, taken as an input; F-33. |
| s 208(d)(1) | src:161-162 | encoded | euca-s208-sea `the individual may elect to discontinue participation at any time` | |
| s 208(d)(2) | src:161,163 | encoded | euca-s208-sea `the individual receives extended compensation payments for subsequent weeks`, `the most extended compensation that may be paid for subsequent weeks` | F-33. |
| OLRC note: three "Amendment by section ... effective as if included" notes (Pub. L. 112-240, 112-96, 112-78) | src:164-166 | inert | none | machinery (commencement): each says that an amendment to section 203 takes effect as if included in an earlier Act; it fixes when amendments to this Act took effect, and the encoded text is the Act as amended. F-35. |
| OLRC note: Pub. L. 102-318, title II, s 202(a)(2) | src:167-169 | inert | none | machinery (commencement of an amendment to section 202(a)(5)): applies from 3 July 1992 and waives certain overpayments under another Act; the waiver concerns the Emergency Unemployment Compensation Act of 1991, another instrument. F-35. |
| OLRC note: Pub. L. 98-21, title V, s 522(b) | src:170-173 | inert | none | machinery (commencement): the converter kept only fragments (section 202(a)(3)(A)(ii), 20 April 1983); the text printed does not make a rule. F-35. |
| OLRC note: Pub. L. 97-248, title I, s 191(b) | src:174-176 | inert | none | machinery (commencement of an amendment to section 204(a)(2) for eligibility periods from 1 October 1983, with a State-legislation exception). F-35. |
| OLRC notes: Pub. L. 97-35, title XXIV, ss 2401(c), 2402(b), 2403(b), 2404(c), and the 2408(b) cross-reference | src:177-193 | inert | none | machinery (commencement): the converter kept only fragments (dates 13 August 1981, 25 September 1982; sections 203(d), 203(e)(1)(A)); the 2408(b) cross-reference says the amendments were required in State laws for certification purposes. F-35. |
| OLRC note: Pub. L. 97-35, s 2505(b), effective date | src:194 | inert | none | an amendment of another instrument's application: the amendment to section 204(a)(2)(C) applies to allowances payable for weeks beginning after 30 September 1981, and the transitional provisions are in the Trade Act note it cites. F-35. |
| OLRC note: Pub. L. 96-499, title X, s 1022(b) | src:195-197 | inert | none | machinery (commencement of an amendment to section 204(a)(2) for eligibility periods from 5 December 1980, with a State-legislation exception). F-35. |
| OLRC note: Pub. L. 96-499, title X, s 1024(b) | src:198-201 | inert | none | machinery (commencement): the converter kept only fragments (section 202(a), 31 March 1981). F-35. |
| OLRC note: Pub. L. 96-364, title IV, s 416(b) | src:202-204 | inert | none | machinery (commencement of an amendment to section 202(c): weeks after 1 October 1980, not a requirement of a State law under IRC 3304(a)(11) for a week before 1 June 1981, or 1 June 1982 for certain States). F-35. |
| OLRC note: Pub. L. 94-566, s 116(f)(1) (Virgin Islands) | src:205 | inert | none | machinery (commencement): the deletion of "the Virgin Islands or" from section 202(a)(1) and the insertion in section 205(8) take effect on a date tied to the Secretary's approval; the text printed is "in part". F-35. |
| OLRC note: Pub. L. 94-566, title II, s 212(b) | src:206-209 | inert | none | machinery (commencement): the converter kept only fragments (section 204(a)(4), 1 January 1979); paragraph (4) of section 204(a) does not appear in this text at all. F-35. |
| OLRC note: Pub. L. 94-566, title III, s 311(c) | src:210-215 | inert | none | machinery (commencement): the converter kept only fragments (section 203(d), 31 December 1976; section 203(e), 30 March 1977). F-35. |

Counts: 99 rows; encoded 54 (including the five rows of section 208(b)); fork 30; inert 15; repealed or blank 0.
The 99 rows cover the 8 sections and all 22 catch-lined headings: one row per section where a section is one rule (ss 201, 206), one row per subsection or paragraph elsewhere, and twelve rows for the OLRC's effective-date notes at the end (lines 164 to 215).
Every `inert` row names what the provision does and why the reason applies.

## Fork register

Each entry gives the readings I saw, the one taken, and the text that licenses it.
`src:N` is a line of `euca-1970-note-26usc3304.txt`.

| id | where | readings seen | taken | licensing text |
|---|---|---|---|---|
| F-1 | s 205(11), s 203 | a week is a calendar week; a week is whatever the State law says | a week is the DATE on which it begins; weeks are 7 days apart; "the third week after" is 21 days on | src:130 "a week as defined in the applicable State law" |
| F-2 | s 203(a) | the period begins in the third week after (inclusive) or the week after that | the third week after the first "on" week is the period's first week; the third week after the first "off" week is its last | src:77 "shall begin with the third week after", src:78 "shall end with the third week after" |
| F-3 | s 203(b)(1)(A) | "not less than thirteen consecutive weeks" counts the first week or not | the last week is at least the first week plus 12 weeks (13 weeks inclusive) | src:79-80 |
| F-4 | s 203(b)(1)(B) | a period that would begin too soon is cancelled, or is delayed | delayed: it begins at the later of the third week after the first "on" week and the fourteenth week after the close | src:81 "may begin before the fourteenth week after the close" |
| F-5 | s 203(a)(2) | any "off" reading, or the first "off" reading at or after the "on" week | the first "off" reading at or after the first "on" week | src:78 "the first week for which there is a State 'off' indicator" |
| F-6 | s 203(c) | "his benefit year ends within such extended benefit period": the last day of the benefit year falls in the period | the last day is from the period's first week to 6 days after its last week; weeks "thereafter which begin in such period" count | src:83 |
| F-7 | s 203(d), (f) | the alternative trigger replaces subsection (d); or either suffices | "on" if (d) says on OR (f) says on; "off" if neither | src:99 "any week for which there would otherwise be a State 'on' indicator shall continue to be such a week" |
| F-8 | s 203(d), closing | the 6 per cent option replaces paragraph (1) or adds to it | "on" if paragraph (1) is met OR (the option applies AND the rate is at least 6); the option applies to weeks beginning after the later of 30 March 1977 and the date the State law establishes | src:89 |
| F-9 | s 203(d), (f)(2) | the 2010 option's window and bracketed date | the option applies if the week begins after the later of 17 December 2010 (OLRC bracket) and the State date, and the week's last day (begin + 6) is not after 31 December 2013; "two" becomes "three" in (d); "either" becomes "any", "2" becomes "3" in (f) | src:89, src:100 |
| F-10 | s 203(d) last sentence, (e)(1) | a rate with zero covered employment; the "first four of the most recent six" quarters | zero covered employment returns NOTHING (the text is silent); the first four are the chronologically earliest four of exactly six, otherwise NOTHING | src:89, src:90-92 |
| F-11 | s 203(d)(1)(A) | the average of the preceding rates | the arithmetic mean of the rates for the preceding two (or, under the option, three) years | src:86 |
| F-12 | s 203(f)(1)(A)(ii) | "either (or both)" | the 3-month rate must equal or exceed 110 per cent of the figure for at least one of the corresponding periods (one of three under the 2010 option) | src:97, src:100 |
| F-13 | s 202(a)(1) | "exhausted" at the start of the week, or during it | (A) all regular compensation received, or (B) the last day of the benefit year is before the week begins | src:26 |
| F-14 | s 202(a)(1), (b)(1) | "payable" is what the State pays, or what the Act requires its law to provide | the floor the Act requires; a State law may give more, which is not modelled | src:26 "a State law shall provide"; src:56 "not less than" |
| F-15 | s 202(a)(3)(A)(i) | an offer is accepted, a referral is applied for; "(c) [probably means subpar. (C)]" | accept the offer, apply for the referral (the field `how the work reached the individual` chooses); "subparagraph (c)" is subparagraph (C) | src:29 |
| F-16 | s 202(a)(3)(A)(ii) | the closing "if such exemptions in clauses (I) and (II) apply to recipients of regular benefits, and the State chooses to apply such exemptions for recipients of extended benefits" covers both together or each | each exemption applies when its own two conditions hold | src:34 "such exemptions", "clauses (I) and (II)" |
| F-17 | s 202(a)(3)(B) | which weeks of employment count; the "average weekly benefit amount (as determined for purposes of subsection (b)(1)(c)) [probably means subsec. (b)(1)(C)]" | weeks that began after the failure and before the week claimed; remuneration at least 4 times the benefit-year average weekly benefit amount; at least 4 weeks AND the pay; the ineligibility starts the week after the failure | src:36-37 |
| F-18 | s 202(a)(3)(D) | the four clauses are cumulative or alternative; "not offered in writing and was not listed"; "does not exceed"; "less than" | alternative (any one); neither written nor listed; (i) at most the sum; (iv) strictly below the higher | src:39-47 |
| F-19 | s 202(a)(5) | "exceed" for both wage methods; "one or more of the foregoing methods"; no method chosen | "exceed" strictly for both; the individual passes if they meet any method the State chose; no method chosen returns `the State law has chosen no method, which section 202(a)(5) requires it to do` (not covered); the master rule `extended compensation is payable for the week` treats that result as not payable (it asks for `the individual has the required employment`), so only the separate employment question (the rule `the result of the employment requirement`, and the seat question on employment) carries the not-covered value | src:53 |
| F-20 | s 202(a)(6) | "under the rules of paragraphs (3), (4), and (5)" includes the suspension by paragraph (7) | the same rules, with paragraphs (3) and (4) suspended in their weeks and paragraph (5) never suspended | src:54-55 |
| F-21 | s 202(a)(7) | "weeks of unemployment beginning after March 6, 1993, and before January 1, 1995" | the week's begin date is after 6 March 1993 and before 1 January 1995; outside that, paragraphs (3) and (4) apply | src:55 |
| F-22 | s 202(b)(1) | "not less than ... the least"; negative (C); "reduced ... if the State law so provides" | the least of the three; if negative the account holds nothing and no weeks are covered; the reduction applies only if an input says the State law provides it; whole weeks are FLOOR(account / weekly amount) and NOTHING if the weekly amount is not above 0 | src:56-60 |
| F-23 | s 202(b)(3)(B) | "an extended benefit period would be in effect if section 203(f)(1)(A)(i) were applied by substituting '8 percent' for '6.5 percent'": clause (i) alone, or the whole alternative trigger (clause (ii) too); whether the State adopted it | the whole alternative trigger of 203(f)(1)(A) at 8 per cent (clause (ii)'s 110 per cent comparison kept), whether or not the State law adopted it, then the extended benefit period engine of 203(a)(b) applied to those readings | src:67 |
| F-24 | s 202(c)(1), (2) | "the first 2 weeks for which extended compensation is payable (determined without regard to this subsection)" | counted by the earlier weeks for which extended compensation was payable on the claim from the account: fewer than 2 means exempt; "such State" is the State where the interstate claim was filed | src:68-71 |
| F-25 | ss 202(a)(7), 203(d), 207, 208(a)(1) | the day an effective date is tested | at the date on which the week begins | src:55, 89, 137-145, 148 |
| F-26 | s 207(a), (b) | the enactment date; a period before 1 January 1972 | 10 August 1970 (OLRC title block and bracket); with an approved State law a period may begin from 60 days after that, 9 October 1970; for such weeks the period is fixed "solely by reference to the State 'on' and 'off' indicators", so the 14-week gap and 13-week minimum are left out | src:19, 140-141 |
| F-27 | s 204(a) | the order the exclusions and caps apply in; the "first week" | exclusions (A) to (C) remove the whole week's compensation; (D) trims an excess over the rounded-down amount; the caps of (b) and (c) then apply; one-half of the sum; then the reduction of (a)(3); the "first week" and the State's first-week rule are input flags | src:105-110 |
| F-28 | s 204(a)(3) | total base period wages of 0 | no reduction | src:110 |
| F-29 | s 204(b) | "the smallest of the amounts referred to in subparagraphs (A), (B), and (C) of section 202(b)(1)" before or after the "except that" reduction | before: the three amounts, not reduced by additional compensation | src:111 |
| F-30 | s 204(c)(2) | "exceeds twenty-six times (and does not exceed thirty-nine, forty-six in any case where section 202(b)(3)(A) applies[,] times)": the sentence is garbled | the sharable part is the amount above 26 times and not above 39 times the weekly benefit amount (46 times where section 202(b)(3)(A) applies); the bracketed "[,]" is editorial | src:114 |
| F-31 | s 204(d), (e) | how much of the monthly payment and certification to encode | the sum (estimate less the correction), the two officials and the Treasury's payment of the certified sum; the sampling method and the Government Accountability Office clause are not encoded | src:115-116 |
| F-32 | s 205(8) | "State includes the District of Columbia, Puerto Rico and the Virgin Islands": whether any other place is excluded | the three are included; any other place is returned as "not named by the definition" (neither in nor out) | src:127 |
| F-33 | s 208 | "date of enactment of this section [Feb. 22, 2012]"; the combined limit; "reasonable expectation"; (d)(2) | weeks beginning after 22 February 2012; the 26 weeks are counted from a number the caller supplies; strictly fewer than 26 permits another week; "reasonable expectation" is the State agency's judgment, taken as the amount it expects, tested at least 13 times the weekly benefit amount; (d)(2) resumes up to what remains in the account, never negative | src:148-152, 160, 163 |
| F-34 | s 208(b) | what to do with the modifications to IRC 3306(t), which is not in the text | the modifications are data (the replacement words, the paragraphs that do not apply, the training clause, the 1 percent figure); the definition itself is an input flag | src:153-159 |
| F-35 | lines 164-215 | the OLRC effective-date notes apply to old weeks; they are law of the amending Acts | not applied: the encoded text is the Act as amended and is applied to every week; the transitional dates for the 1976 to 1983 amendments (for example weeks before 1 October 1983 for the rounding exclusion) are not encoded; the converter dropped much of their text | src:164-215 |
| F-36 | the seat | judgments handed to others: whether the State agency is satisfied that prospects are good; whether the State law treats work as suitable or would deny; whether a State rule is inconsistent; whether the State chose an exemption; the State agency's expectation | plain inputs the person can state or has been told; the answer is conditional on them | src:27, 38, 44, 34, 160 |
| F-37 | s 202(a)(1) and others | "an individual" has no defined term | the seat's person; one individual, one benefit year, one week at a time | src:26 |
| F-38 | s 204(a)(2)(C), s 203(d), (f)(2) | "section 233(d) [now 233(c)]"; "a state [State]" | followed: both are OLRC corrections of the same reference; no rule turns on them | src:109, 89, 100 |

## Dependencies on instruments outside the text

Each dependency is a plain input in the layer-1 records declared in `euca-nouns.l4`, named for the fact, with a `-- out of text:` comment in the module that uses it.

| your provision | the provision it depends on | the input you made |
|---|---|---|
| s 202(a)(1), s 207(b)(1) | IRC 3304(a)(11) (the requirement that a State law provide extended compensation, added by s 206) | `a State law approved under section 3304(a)(11) provides that an extended benefit period may begin with the week` (BOOLEAN, euca-s207-dates) |
| s 202(a)(1), s 205(5), (6), (11) | the applicable State law: benefit year, base period, week, regular compensation, rights | `Benefit year` and `Base period` records; `Regular compensation position` (euca-nouns) |
| s 202(a)(1) | another State's unemployment compensation law | `rights to regular compensation for the week under another State's unemployment compensation law` |
| s 202(a)(1) | other Federal law (any other Federal compensation) | `compensation for the week under another Federal law` |
| s 202(a)(1) | the unemployment compensation law of Canada | `receiving compensation for the week under the unemployment compensation law of Canada` |
| s 202(a)(3)(C) | the State agency's satisfaction; the applicable State law's treatment of suitability | `the individual furnished evidence satisfactory to the State agency ...`, `the applicable State law treats the work as suitable` |
| s 202(a)(3)(D)(iii) | the applicable State law's denial of compensation for the failure | `State law, so far as consistent with C and E, would deny compensation for the failure` |
| s 202(a)(3)(D)(i) | IRC 501(c)(17)(D) (supplemental unemployment compensation benefits) | `supplemental unemployment compensation benefits payable to the individual for the week` |
| s 202(a)(3)(D)(iv) | Fair Labor Standards Act s 6(a)(1) (29 U.S.C. 206(a)(1)); State or local minimum wage law | `Fair Labor Standards Act section 6(a)(1) minimum wage per hour ...`, `highest applicable State or local minimum wage per hour ...` |
| s 202(a)(3)(A)(ii) | the Secretary's definitions of "jury duty" and of "an emergency or a life-threatening condition" ("as such term may be defined by the Secretary"); State law's determination | `before a court ... jury duty`, `hospitalized ...`, the four exemption flags (euca-nouns `Search for work`) |
| s 202(a)(4) | the State law's disqualifications and their termination | `Disqualification` record |
| s 202(a)(5) | the State law's insured employment, covered earnings, weekly benefit amount, highest quarter, and its choice of method | `Employment in the base period` record |
| s 202(b) | the State law's regular compensation payable and paid, dependents' allowances, option to reduce, additional compensation | `Account facts` record |
| s 202(c) | the interstate benefit payment plan (an agreement outside the text) | `Interstate claim` record |
| s 202(c)(3) | IRC 3304(a)(9)(A) | the BOOLEAN parameter of `section 3304(a)(9)(A) of the Internal Revenue Code does not apply to the denial` |
| s 203(d), (e)(1) | reports of the State agency to the Secretary; the Secretary's regulations (s 203(e)(2)) | `Insured unemployment reading`; the claimant and employment numbers |
| s 203(f) | the published seasonally adjusted rates of total unemployment, determined by the Secretary | `Total unemployment reading` |
| s 203(d), (f) options | the State law's adoption of the options and the dates it establishes | `date from which the State law adopts the 6 per cent option`, `date from which the State law adopts the three-year comparison option`, `the State law adopts the alternative trigger` |
| s 204(a)(2)(A) | any Federal law that reimburses the State | `the State is entitled to reimbursement under a Federal law other than this title` |
| s 204(a)(2)(B), (D) | the State law's first-week rule and benefit structure | `the State law provides for payment of regular compensation for a first week ...`, `amount that would be paid for the week if the State rounded down ...` |
| s 204(a)(2)(C) | Trade Act of 1974 s 233 (19 U.S.C. 2293) | `benefits are not payable for the week by reason of section 233 of the Trade Act of 1974` |
| s 204(a)(3) | IRC 3306(c)(7) | `base period wages attributable to services to which section 3306(c)(7) of the Internal Revenue Code applies`, `total base period wages` |
| s 204(e) | the Unemployment Trust Fund and the Government Accountability Office's audit | none (the parties only; the clause is not encoded) |
| s 205(2), (3) | 5 U.S.C. chapter 85 (unemployment compensation for Federal employees) | `payable pursuant to 5 U.S.C. chapter 85` |
| s 205(10) | IRC 3304 (the Secretary's approval of a State law) | the BOOLEAN parameter of `the law is the State law` |
| s 207(c) | the State legislature's regular sessions in 1971 | `the legislature of the State does not meet in a regular session which closes during the calendar year 1971` |
| s 208(a)(3), (b) | Supplemental Appropriations Act, 2008 (Pub. L. 110-252) s 4001(j) and title IV; IRC 3306(t) | the weeks already received; the eligibility flag; the modifications are data |
| s 208(c) | "emergency unemployment compensation" (not defined in the text) | `the amount of extended compensation and emergency unemployment compensation the State agency has a reasonable expectation the individual will be entitled to` |

That is 28 rows.
The ones that matter most: the State law (everything about the individual's own record: benefit year, base period, weekly benefit amount, method of measuring employment, disqualifications, choices of option), the Secretary's published unemployment figures (the indicators), IRC 3304(a)(11) and (a)(9)(A), and section 3306(t) of the Internal Revenue Code with the 2008 Act for section 208.

## What the text turns out to say

Each finding ends "Asserted." where a case in a test file or in `euca-cases-seat.l4` checks it.

1. An individual whose benefit year ended before the extended benefit period began has an empty eligibility period; one whose benefit year ends inside the period also gets the weeks after it that begin in the period (the last day of the period's last week is 6 days after the week begins). Asserted.
2. An extended benefit period lasts at least 13 weeks even if the "off" indicator comes sooner (begin 3 February 2013, "off" 10 February: the last week is 28 April, not 3 March). Asserted.
3. The 14-week gap delays the start of a new period; a prior close of 4 November 2012 moves a 3 February 2013 start to 10 February. Asserted.
4. The insured unemployment test is met at equality ("equaled or exceeded") on both limbs: a rate of 6 against two years of 5 is on; 5.9 is off; 4.9 is off although above 120 per cent of 4. Asserted.
5. The 6 per cent option removes the 120 per cent limb, but cannot make a standard "on" week "off"; it starts only after the later of 30 March 1977 and the State's date, and the date itself is not "after" it. Asserted.
6. The 2010 three-year option covers a week beginning 25 December 2013 (ends 31 December) and not a week beginning 26 December. Asserted.
7. Under the alternative trigger "either (or both)" means one comparison year is enough; a State that has not adopted the trigger is neither "on" nor "off" under it; a week "on" under subsection (d) stays on. Asserted.
8. The work test is two different steps: an offer is accepted, a referral is applied for; accepting a referral or applying for an offer does not satisfy the other. Asserted.
9. Subparagraph D's four exceptions are alternatives; pay equal to the weekly benefit amount (plus supplemental benefits) may be refused; pay one dollar above may not; the wage test uses the higher of the federal and State or local minimum, and equal is not "less". Asserted.
10. The jury-duty and hospitalisation exemptions each need three things: the circumstance, the exemption for regular benefits, and the State's choice for extended benefits; the State's choice for one does not carry to the other. Asserted.
11. After a failure to accept work or to seek work, the ineligibility starts the week after and ends only when both 4 weeks of employment and 4 times the weekly benefit amount have been met. Asserted.
12. Earnings must "exceed" 40 times the weekly benefit amount or 1.5 times the highest quarter: equal is not enough. Asserted.
13. If a State law has chosen no method of measuring employment, the Act itself decides nothing about the individual's employment test (the encoding returns an explicit not-covered value). Asserted.
14. Paragraphs (3) and (4) of section 202(a) (the work test and the disqualifications) are suspended for weeks beginning after 6 March 1993 and before 1 January 1995; paragraph (5) is not. Asserted.
15. The account is the least of three amounts; when regular compensation paid exceeds 39 (46) times the weekly benefit amount the least is negative and nothing is owed; in a high unemployment period the figures are 80 per cent, twenty and forty-six. Asserted.
16. A high unemployment period needs the whole alternative trigger at 8 per cent (the 110 per cent limb too), starts three weeks after the first week in which it is met, and lasts at least 13 weeks; the State's adoption of the trigger does not matter (fork F-23). Asserted.
17. On an interstate claim the first two weeks are exempt from the cessation rule and the third is cut off when the claim State has no extended benefit period. Asserted.
18. Section 204: one-half of the sharable amounts, after dropping the excluded compensation; sharable regular compensation is only the part of the running total above 26 times and up to 39 (46) times the weekly benefit amount; rounding trims only an excess; the reduction for section 3306(c)(7) services is proportional. Asserted.
19. Section 207: an extended benefit period cannot begin before 1 January 1972 unless an approved State law so provides, and then not before 9 October 1970; section 204 applies only to weeks after 31 December 1971 or in such periods; section 3304(a)(11) binds a State law from 1 January 1972, or 1 July 1972 where the legislature held no regular session closing in 1971. Asserted.
20. Section 208: allowances only for weeks beginning after 22 February 2012; at most 26 weeks together with the 2008 Act's program; the State agency must reasonably expect at least 13 times the weekly benefit amount; the individual may leave at any time and resume extended compensation to what remains in the account. Asserted.
21. "State" in section 205(8) "includes" three places and says nothing of any other: a place it does not name is not decided (the encoding returns an explicit not-covered value). Asserted.
22. Subparagraph F's jobs (those a State law must refer applicants to) are the suitable jobs to which none of D(i) to (iv) applies, which are the jobs whose refusal A(i) denies. Asserted.
23. The text carries three editorial corrections ("[probably means subpar. (C)]", "[probably means subsec. (b)(1)(C)]", "[now 233(c)]") and a garbled sentence in s 204(c)(2); the encoding follows the corrections and reads the sentence as the 26-to-39 (46) band. Not asserted as a fact about the law (F-15, F-17, F-30, F-38).
24. Section 202(a)(1) makes no mention of being able and available for work: those conditions come only through (a)(2), the State law's own terms for regular claims. Not asserted.
25. The Act never says what happens to the individual if the State has not adopted the options of section 203(d) and (f): the standard test of subsection (d) applies alone (asserted with no option adopted). Asserted.

## What the stable binary does not accept

Observed in this session with `l4` 1.6.98 (`main`):

- A function argument that is a field of a record must be parenthesised: `f (r's x) (r's y)`; the unparenthesised `f r's x` is read as `(f r)'s x` and the error that follows (at the next operator) misdescribes the problem.
- A comparison operator (`AT MOST`, `LESS THAN`) must end the first operand's line with the right operand on the next, more deeply indented line; an operator line that begins with `AND` or `OR` at a lesser indent than the first operand is accepted.
- A `CONSIDER ... WHEN ... WHEN ...` cannot be written on one line inside an `#ASSERT`; give it a name in a rule and assert on the name.
- A multi-line argument list inside a `THEN` branch broke the parser; use a `WHERE` local.
- A `LIST` of record constructions needs each element in parentheses (`LIST (R WITH ...), (R WITH ...)`) or named first; the unparenthesised inline form did not parse.
- An empty list passed as an argument is `(EMPTY)`.
- A `MAYBE` field in a record is written `NOTHING` or `JUST x`; a bare field name for a `MAYBE` input to a question is turned into one with `IF ... THEN JUST x ELSE NOTHING`.
- `l4 run` prints `Checking succeeded.` only when nothing else is reported; assertion outcomes are `Information` diagnostics, so a count is the way to see them (check.sh does that).

From the guide and the skill's dialect notes (stated there, not re-tested here): no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`; no section-level `GIVEN`; no `TYPICALLY` on a record field; no `YMD` (use `Date day month year`); no sets; no `@lang`.
Decimal arithmetic gave no rounding trouble at the boundaries tested: with the rates 10 and 11, `11 AT LEAST (1.1 TIMES 10)` held and `10.9 AT LEAST (1.1 TIMES 10)` did not (euca-tests-indicators.l4); no `EQUALS` on a decimal product was asserted, so the rule that decimals are exact is not claimed.

## What check.sh prints

Run as `L4=<the stable l4> L4_TARGET=unstable ./check.sh` from the encoding folder (the deposit has no `fetch-main-l4.sh`, so the main check was skipped; the binary used is the stable `main` build 1.6.98).

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
euca-cases-seat.l4                             0       111       0        0         0
euca-nouns.l4                                  0         0       0        0         0
euca-s202-account.l4                           0         0       0        0         0
euca-s202-conditions.l4                        0         0       0        0         0
euca-s202-payable.l4                           0         0       0        0         0
euca-s202-work-test.l4                         0         0       0        0         0
euca-s203-indicators.l4                        0         0       0        0         0
euca-s203-period.l4                            0         0       0        0         0
euca-s204-payments.l4                          0         0       0        0         0
euca-s205-definitions.l4                       0         0       0        0         0
euca-s207-dates.l4                             0         0       0        0         0
euca-s208-sea.l4                               0         0       0        0         0
euca-seat.l4                                   0         0       0        0         0
euca-shared.l4                                 0         0       0        0         0
euca-tests-account.l4                          0        37       0        0         0
euca-tests-eligibility.l4                      0       113       0        0         0
euca-tests-indicators.l4                       0        46       0        0         0
euca-tests-payments.l4                         0        99       0        0         0
euca-tests-period.l4                           0        50       0        0         0
TOTAL (19 modules)                             0       456       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Assertions written equal assertions satisfied in every file that has any (`grep -c '^#ASSERT'`: 111, 37, 113, 46, 99, 50; total 456).
`python3 -I srcrefs.py check --refs <the text> euca-*.l4` reports 0 problems (208 quoted lines, 141 runs, 159 locators), and so does `--strict`.
A mutation check was run and undone: changing one figure in each of six modules (the one-half in section 204, the 120 per cent, the 4-week count, the 50 per cent, the 14-week gap, the exhaustion comparison) made the corresponding tests and cases fail, then the originals were restored byte for byte.

## Before this is worth relying on

- The source is a converter's plain-text rendering of the OLRC note, not the official text; read the rules against the Statutes at Large (or the OLRC's own page) before relying on them. Nothing here has been checked against an official text.
- Three dates (10 August 1970, 17 December 2010, 22 February 2012) exist in the text only in OLRC square brackets; they are carried as values with the bracket cited (F-9, F-26, F-33).
- The OLRC's effective-date notes (lines 164 to 215) are not applied and the converter dropped much of their text; the encoded text is applied to every week. Weeks before the dates in those notes (for example the rounding exclusion before 1 October 1983, or the 1981 trade-act reference) may have been governed by earlier wording.
- "Payable" means what the Act requires a State law to provide; every State's own law, which may give more, is an input, and no State's law is encoded.
- Everything about an individual's own record comes from a State law that is not in the text (benefit year, base period, weekly benefit amount, disqualifications, the measure of employment, the choices of option); the answers are conditional on those inputs.
- Weeks are dates and seven-day steps (F-1); a State whose weeks are defined otherwise would differ.
- The Secretary of Labor's regulations (s 203(e)(2)) and definitions (jury duty, emergency, life-threatening condition) and the interstate benefit payment plan are not in the text.
- Fork register entries F-2, F-3, F-4, F-6, F-16, F-19, F-23, F-24 and F-30 change answers: each deserves a second reading by someone who knows the Act. F-23 (the high unemployment period) and F-30 (the garbled sentence in s 204(c)(2)) most.
- The expected values in every test were written by hand by the same agent that wrote the rules, after reading the text but not independently; there was no separate test pass by another reader. A mutation check shows the tests can fail; it does not show that the hand calculation matches the intended law.
- Section 204 is encoded as written, week by week; the Federal share depends on State practice (rounding, first-week rules, the unresolved "first week" flag) that the caller must supply truthfully.
- The seat layer asks 38 questions and the master question takes 58 inputs; a deployment may want to split it.
- No lawyer has reviewed this encoding.

## Checked after the run

This section was added by the session that ran the agent, after the run; the sections above are the agent's.

- `L4=<L4_BIN> L4_MAIN=<L4_BIN> ./check.sh` in this folder, with `JL4_LIBRARY_PATH` unset, on the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19): `TOTAL (19 modules) 0 456 0 0 | 0 456 0 0`; exit status 0; every main column reads `same`.
  The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
  The agent ran `check.sh` with `L4_TARGET=unstable`, as its brief said, so the output printed above under "What check.sh prints" is from that run.
- `srcrefs.py check --refs` against `../../registers/source-bundle/euca-1970-note-26usc3304.txt`: `srcrefs check: 208 src: lines, 141 runs, 159 locators, 0 problems`.
- `srcrefs.py check --strict`: `srcrefs check: 208 src: lines, 141 runs, 159 locators, 0 problems`. These findings are counted here and have not been reviewed one by one.
- 38 `@export` seat questions; 99 coverage rows (54 encoded, 30 fork, 15 inert, 0 repealed or blank).
- Paths in the agent's files that named its run folder (`inputs/...`) were rewritten on copying to name the deposited text in `../../registers/source-bundle/`; the agent's brief is kept verbatim as `BRIEF.md`, and the paths in it are the run's own.
