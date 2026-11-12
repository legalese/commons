# Superannuation Guarantee (Administration) Act 1992 (Commonwealth), sections 1 to 80: a two-layer encoding

**Status: draft.**
Checked by running the gate on 23 modules (results below under "What `check.sh` prints"), on two builds of `l4`, and by `srcrefs.py` with and without `--strict`.
No domain expert has read it against the text.

**Target: `main`.**
The encoding is written for the stable `main` build of `l4` and `check.sh` runs every module on a second `main` build.
Writing build: 1.6.98 (main, 7689b0d, 2026-10-19).
Second build: 1.6.110 (main, e51181d, 2026-11-11).

**Edition.**
Federal Register compilation C2026C00272 (Compilation No. 78, in force from 1 July 2026), a plain-text conversion of the Word rendering, not the authorised text.
The in-scope text is lines 22 to 1353 of `C2004A04402.txt` (the contents list to the last line of section 80); the endnotes begin at line 1354 and are not encoded.
Formulas the text conversion lost are read from `C2004A04402.formulas.md` (ss 10A(5), 17A(2), 18A(3)(d)(iii), 18C(1), 18D(2), 19A(2), 64B(3)).

**The shared module `au-time-rules.l4` is NOT used.**
`sga-time.l4` is self-contained and imports only the prelude and `daydate`.

## Seat

The seat is an employer, or an adviser to one, asking whether superannuation guarantee charge is payable, how the individual and base shortfalls are worked out, what the choice of fund requirements need, when a statement or payment is due, and what penalty follows late payment.
The Act puts its duties and liabilities on the employer: the charge (s 16A), the choice loading (s 20A), the standard choice form (s 32N), general interest charge (s 49), the penalty (s 59C) and records (s 79).
So the questions are the ones an employer asks about its own payments.
The Commissioner's duties and powers are encoded in layer 1 for what they decide and appear in layer 2 only for what they mean to the employer (for example whether a notice to pay must be given, or whether an assessment can still be amended).
There is no seat for the Commissioner or any other official.

Layer 2 is `sga-seat.l4` and `sga-cases-seat.l4`.
Every question has `@export` and `@desc`, takes plain inputs (one for each fact the employer can state), and sits under a `§` heading in the order of the text.
Each question builds the records and lists the layer-1 rules expect inside its own `WHERE`, and then calls the same layer-1 rule.
No layer-1 module changes to suit layer 2 and layer 2 restates no rule.

## Files

All files are flat ASCII `sga-*.l4` beside this file, because the stable `l4` resolves `IMPORT` only within the importing file's folder.

| file | what it holds |
| --- | --- |
| `sga-provisions.l4` | generated: the provision index, 1,085 provisions (Parts, Divisions, Subdivisions, sections, subsections, paragraphs, subparagraphs, definitions, table items), and lookups by identifier |
| `sga-xrefs.l4` | generated: the cross-reference table, 438 rows, one assertion per row and two count assertions |
| `sga-defs.l4` | generated: the 103 defined terms of the text as records, with lookups |
| `sga-time.l4`, `sga-tests-time.l4` | every date, period and amount of time the text states or implies, and its tests |
| `sga-part1.l4`, `sga-tests-part1.l4` | Part 1 (ss 3 to 5C) |
| `sga-part2.l4`, `sga-tests-part2.l4` | Part 2 (ss 6 to 12A) |
| `sga-part3a.l4`, `sga-tests-part3a.l4` | Part 3, Division 1 and Subdivisions A to C up to s 18B (ss 15B to 18B) |
| `sga-part3b.l4`, `sga-tests-part3b.l4` | Part 3, ss 16B, 18C to 20D and 30 |
| `sga-choice-of-fund.l4`, `sga-tests-choice-of-fund.l4` | Part 3A (ss 32A to 32ZAB) |
| `sga-part4-6.l4`, `sga-tests-part4-6.l4` | Parts 4 to 6 (ss 33 to 58) |
| `sga-part7.l4`, `sga-tests-part7.l4` | Part 7 (ss 59 to 59E) |
| `sga-parts8-9.l4`, `sga-tests-parts8-9.l4` | Parts 8 and 9 (ss 63A to 80) |
| `sga-seat.l4`, `sga-cases-seat.l4` | layer 2: the seat's questions and worked cases |

`PROGRESS.md` records the method and the state of the work.
`encoding.json` and `SOURCE-LICENSE.md` follow the Commons deposit layout.
The module order for reading is the order of the table.

Every rule in layer 1 carries `-- src:N | text` lines that quote the text mechanically and an `@ref` locator naming the provision and the lines.
The quoting and the locators are produced by a script that reads the text file, so a quoted line cannot differ from the text; `srcrefs.py check` confirms this, and `--strict` confirms that each locator reaches exactly the lines its block quotes.

## What is encoded and what is not

**Encoded.**
Every operative provision of sections 3 to 80 that an employer, or an adviser, applies to its own facts:

- Who is an employee (s 12) and the terms the Act borrows for payments, funds and schemes (ss 6 to 11).
- Qualifying earnings, the maximum contributions base and its capping rule (s 10A), the charge percentage (12) and the individual superannuation guarantee amount (ss 15A to 17B), with exemption certificates (ss 17C, 17D).
- Eligible contributions (ss 18A, 18B), the individual base shortfall with the usual period, the 12-month period and the table of allowable longer periods (s 18C), the final shortfall over the late period (s 18D), notional earnings compounded daily (s 19A), the administrative uplift (s 19B), the choice loading and its limit (ss 20 to 20D), the employer's shortfall (s 16B) and the charge payable on an arrangement made to avoid it (s 30).
- The choice of fund requirements: each limb of s 32C with the override in s 32CA, eligible choice funds, chosen funds and when they take effect, standard choice forms and when they are due, stapled funds and the remaining Divisions.
- Voluntary disclosure statements, assessments and their amendment, refunds (ss 33 to 42), general interest charge on unpaid charge (s 49), public officers and service (ss 57 to 58).
- The notice to pay, the payment period, the 0, 25 and 50 per cent penalty, its assessment and amendment (ss 59A to 59E).
- The shortfall component for one or several employees, how the Commissioner deals with it, and recovery of overpayments (ss 63A to 69A).
- Partnerships and associations (ss 72, 73), the amnesty (s 74) and records (s 79).

**Computed in `sga-time.l4` and asserted.**
Every date, period and amount of time: business days, the usual and extended usual periods, quarters, the 12-month, 15-month and 24-month periods, the 20, 28, 50 and 60-day periods, 4 years, 5 years, the amnesty period, the late period and its length, and the day a chosen fund takes effect.

**Not encoded, and why** (the coverage table gives a disposition for every row of the text):

- Machinery: the short title, commencement and extent (ss 1, 2, 4), powers to make regulations (ss 10(6), 19B(3), 80) and the Commissioner's powers to determine by legislative instrument (ss 18C(3), 18C(4)). What a determination or a regulation provides is a plain input wherever a rule needs it.
- Outlines, purposes and overviews (ss 16, 17, 18, 19, 32A, 32B, 59 and 63B(2), (3)) state no rule beyond the rules they summarise.
- The notional employer contribution rate (s 10(2)) is stated by an actuary in a benefit certificate and is supplied as a percentage.
- Sections 72(6) and 73(7) extend "this Act" to Part III of the Taxation Administration Act 1953, which is not among the sources.
- Everything the Act borrows from another instrument is asked as a fact: the general interest charge rate (Part IIA of the Taxation Administration Act 1953), the concessional contributions cap, the value of a penalty unit, the date of the Royal Assent of the 2020 amending Act, and each term defined elsewhere.
- Judgments the Act hands to the Commissioner are conditional inputs, never guessed: opinions about avoidance, satisfaction under s 17C(2), the Commissioner's notifications about stapled funds (Division 7), and determinations under s 18C.

## Jural relations

One row per provision that creates a relation between two parties; every other provision creates none.
Each relation is stated once.

| provision | relation | first party | second party | what |
| --- | --- | --- | --- | --- |
| s 16A | duty / claim | the employer | the Commonwealth | to pay superannuation guarantee charge imposed on its superannuation guarantee shortfall for a QE day |
| s 17B | immunity | the employer | the Commonwealth | the individual superannuation guarantee amount is nil while an exemption certificate covers the employer and the employee |
| s 17C | power / liability | the Commissioner | the employer | to issue an exemption certificate for a period |
| s 30 | liability / power | the employer | the Commissioner | to pay for a QE day the amount the Commissioner thinks would have been payable had the arrangement not been made |
| s 32F | power / liability | the employee | the employer | to make a fund the chosen fund by notice |
| s 32FA | liberty / no-claim | the employer | the employee | to refuse a chosen fund when the statement or the evidence is missing, or another fund was chosen within 12 months |
| s 32N | duty / claim | the employer | the employee | to give a standard choice form in the times the section sets |
| s 33(1) | liberty / no-claim | the employer | the Commissioner | to lodge a voluntary disclosure statement for a shortfall |
| s 36 | power / liability | the Commissioner | the employer | to assess the shortfall and the charge payable on it |
| s 37 | power / liability | the Commissioner | the employer | to amend an assessment |
| s 38 | duty / claim | the Commissioner | the person who overpaid | to refund an overpaid amount |
| s 40 | duty / claim | the Commissioner | the person liable | to give written notice of an assessment or amendment as soon as practicable |
| s 42 | power / liability | the employer | the Commissioner | to object to an assessment under Part IVC of the Taxation Administration Act 1953 |
| s 49 | duty / claim | the employer | the Commonwealth | to pay general interest charge on unpaid charge for each day it remains unpaid |
| s 57(3), (4) | duty / claim | the public officer of a company | the Commissioner | to do what the Act requires of the company and to bear its penalties |
| s 58(3), (4) | duty / claim | the public officer of a trust estate | the Commissioner | to do what the Act requires of the trustee and to bear its penalties |
| s 59A | duty / claim | the Commissioner | the employer | to give a written notice to pay when the conditions of s 59A(1) and (2) are met |
| s 59C | duty / claim | the employer | the Commonwealth | to pay a penalty of 0, 25 or 50 per cent of the part of the specified amount unpaid at the end of the payment period |
| s 59D | duty / claim | the Commissioner | the employer | to make a penalty assessment and give written notice of it unless the penalty is nil |
| s 59E(1) | disability / immunity | the Commissioner | the employer | no power to remit the penalty in a penalty assessment |
| s 59E(2) | duty / claim | the Commissioner | the employer | to amend a penalty assessment when a relevant liability is reduced or ceases, or the penalty is reduced to nil |
| s 65 | duty / claim | the Commissioner | the employee | to pay or deal with the shortfall component in one of the ways the section lists |
| s 65A | duty / claim | the Commissioner | the employee aged 65 or more | to pay the shortfall component directly on request in the approved form |
| s 66 | duty / claim | the Commissioner | the retired former employee | to pay the shortfall component where the notice and the certificate of 2 registered medical practitioners are lodged |
| s 66A | duty / claim | the Commissioner | the employee with a terminal medical condition | to pay the shortfall component on request in the approved form |
| s 67 | duty / claim | the Commissioner | the employee's legal personal representative | to pay the shortfall component where the employee has died |
| s 69 | power / liability | the Commissioner | the debtor | to recover an excess paid under Part 8 as a debt due to the Commonwealth, on 28 days' written notice |
| s 72 | duty / claim | the partners | the Commonwealth | each partner bears the partnership's obligation, and the partners bear its liability to pay money jointly and severally |
| s 73 | duty / claim | the officers and members of an association | the Commonwealth | the officers bear the association's obligations and the members its liability to pay money jointly and severally |
| s 74(1) | immunity | the employer | the Commonwealth | an amnesty for the shortfall for a quarter when the conditions are met |
| s 74(5) | power / liability | the Commissioner | the employer | to notify that the employer has ceased to qualify for the amnesty |
| s 79 | duty / claim | the employer | the Commonwealth | to keep, and for 5 years to retain, the records the section describes |


## Fork register

Every ambiguity the encoding decides, the readings seen, the one taken, and the text that licenses each.
Each fork is a place where the text does not say, or says two things; where it is silent the answer is `NOTHING`, or both readings are computed and `NOTHING` is returned when they differ.
Forks are assumptions of the encoding, not rulings of anyone with authority over the Act.

| id | provision | function | answer taken | other reading | licensing text |
| --- | --- | --- | --- | --- | --- |
| F-1 | counts "within N days of", "N years from", "N business days after" an event (ss 6(1) "usual period", 10(3)(c), 32N, 37, 59D(3), 79(4)) | `the two readings agree`, `an act is within n days of an event` and the other counting functions in `sga-time.l4` | compute the last day with the day of the event not counted and with it counted as the first day; answer only where the two agree, otherwise `NOTHING` | take one reading as the only reading | the sources do not say whether the day of the event is counted |
| F-2 | a count in months or years that lands on a day the target month does not have (ss 32F(2), 74(3)(b), 6(1) "12-month period", 59C(2) item 2) | `the same day n months after`, `a day is on or after the day n months from`, `a day is on or before the day n months from` | `NOTHING` on the one day in doubt (the last day of the month or the first of the next); the days either side are answered | roll the day forward, or back to the month end | the text does not say which neighbouring day is meant |
| F-3 | s 18A(3), the notional contribution for a defined benefit member | `the notional contribution for a defined benefit member` | the qualifying earnings times the rate divided by 100, the rate being a percentage (s 10(1)) | multiply by the rate as stated | s 10(1) says the rate is expressed as a percentage; s 17A(2) divides its percentage by 100 |
| F-4 | s 19A(1)(b) | `the individual notional earnings component` | the individual final shortfall is one amount for the employee and the QE day (s 18D); when it is greater than nil every day of the late period counts; the daily rates are supplied by the caller and a list whose length differs from the number of days gives `NOTHING` | test each day separately | s 18D defines one amount for the employee and the QE day; s 19A(1) counts days of the late period |
| F-5 | s 18A(1) | `is an eligible contribution` | the paragraphs (a) to (d) are taken as the whole of what an eligible contribution is; a contribution outside them is `JUST FALSE` | `NOTHING` | s 18A(1) says an eligible contribution "is:" and lists (a) to (d) |
| F-6 | s 32C | `the contribution is made in compliance with the choice of fund requirements` | no limb of s 32C applying is `JUST FALSE`; the direct-cost override of s 32CA gives `JUST FALSE` even if a limb applies | `NOTHING` where no limb applies | s 32A says the Part sets out the circumstances in which contributions are made in compliance; s 32CA says "taken not to comply" |
| F-7 | s 16B(1) | `the superannuation guarantee shortfall of an employer for a QE day` | with no individual base shortfall and no choice loading greater than nil the section does not apply and the answer is `NOTHING` | `JUST 0` | s 16B(1) says the section "applies if" one of the two exists |
| F-8 | s 17A(1) | `the individual superannuation guarantee amount` | no payment of qualifying earnings on the QE day gives `NOTHING` | `JUST 0` | s 17A(1) says the Subdivision applies if the employer makes a payment on the QE day |
| F-9 | s 32FA(1) | `the employer may refuse to accept the fund chosen because the notice lacks the statement or the evidence` | the employer may refuse if either the statement or the evidence is missing | refusal only if both are missing | s 32FA(1) says "does not provide, together with the notice: (a) ... and (b) ..." |
| F-10 | s 12 | `is an employee for the purposes of the Act` | order of decision: s 12(11) (domestic work, `JUST FALSE`), s 12(10) (`JUST TRUE`), s 12(9A) (council member, `JUST FALSE`), then the expansions in ss 12(2) to (9) and the ordinary meaning (`JUST TRUE`); a person who is none of these gives `NOTHING` | a different order when the facts overlap | s 12(1) says employee and employer have their ordinary meaning and ss 12(2) to (11) expand or make particular provision; s 12(9A) is "subject to subsection (10)" |
| F-11 | s 32N | `the employer must give a standard choice form` | no trigger and no exception gives `NOTHING`; an exception in s 32NA gives `JUST FALSE` | `JUST FALSE` for no trigger | s 32N states the duty only for the events it lists |
| F-12 | s 6AA | `is a defined benefit member` | where the regulations prescribe circumstances under both paragraphs (a) and (b) for the same member the answer is `NOTHING` | paragraph (a) prevails | s 6AA says only that "the regulations may prescribe" each |
| F-13 | s 38(1)(b) | `the amount the Commissioner must refund` | where the person has a liability to the Commonwealth the refund is `NOTHING` and limb (ii) is computed separately as the lesser of the overpaid amount and the liability | the whole overpaid amount is refunded | s 38(1)(b) gives two limbs and does not say which applies |
| F-14 | s 59A(2)(c) | `the Commissioner must give the employer a written notice to pay as soon as practicable after the current notice trigger day` | the specified amount must exceed the greater of $30 and any higher prescribed amount | a prescribed amount replaces $30 even if it is lower | s 59A(2) says "exceeds $30 or a higher prescribed amount" |
| F-15 | s 59C(2) item 1 | `a determination covers the employer for some part of the period for item 1` | a determination with no end day covers every day from its first day; a determination that ended before the imposition day does not reach the period | the determination must cover the whole period | item 1 says "for any part of the period" |
| F-16 | s 66(b)(ii) | `the Commissioner must pay the shortfall component to an employee retired due to permanent incapacity or invalidity` | a certificate signed by at least 2 registered medical practitioners | exactly 2 | s 66(b)(ii) says "signed by 2 registered medical practitioners" |
| F-17 | s 79(6), (6A) | `the employer commits an offence against section 79` | no contravention gives `NOTHING`; a contravention with a reasonable excuse gives `JUST FALSE` | `JUST FALSE` for no contravention | s 79(6A) says subsection (6) "does not apply to the extent that" the person has a reasonable excuse |
| F-18 | s 20C(3) | `a QE day is in the notice period` | the notice period ends only on the day the Commissioner gives written notice; while none has been given it has not ended | the period ends at a day fixed by the facts | s 20C(3)(b) says it ends "on the day the Commissioner gives" the notice |
| F-19 | s 18C(1)(c), table items 2 to 4 | `a day of receipt is within the periods for the QE day` | items 2 to 4 say "before the end of" and have no first day, so any earlier day qualifies; the standard periods and item 1 have a first day | add a first day | the text as printed |
| F-20 | s 17D(3) | `the Commissioner is treated as having decided not to issue a certificate` | `JUST TRUE` only after the 60-day period starting on the day of the application with no notice of a decision; otherwise `NOTHING` | `JUST FALSE` before then | s 17D(3) deems a decision after the period |
| F-21 | rules stated with an "if" condition (for example ss 32C(10), 33(1), 37(2), 49(1), 57(1), 57(5), 59A(1), 59A(2), 59D(1), 63B(1), 65A, 66, 67, 32F(3)) | the matching functions in `sga-part4-6.l4`, `sga-part7.l4`, `sga-parts8-9.l4`, `sga-choice-of-fund.l4` and `sga-part2.l4` | where the condition fails: a duty stated with "must" or "is required to" gives `JUST FALSE` (ss 59A(2), 59D(1), 63B(1), 65A, 66, 66A, 67), and so does a liability stated with "is liable" and an "if" (s 49(1)); `NOTHING` for a power or deeming stated with "may" or "is taken to" (ss 32C(10), 33(1), 37(2), 57(5)), for a scope rule "applies if" with no "only" (s 59A(1)), for a limit on a grant (s 32F(3), "cannot become a chosen fund ... if"), and for a status whose test is taken from another Act (s 57(1), the public officer for s 252 of the Income Tax Assessment Act 1936) | `JUST FALSE` for all of them | the text's own words; the Commons ruling that a scope limit with no "only", a limit on a grant and a point outside the sources give `NOTHING`; the note to s 49(1) says only that the general interest charge is worked out under Part IIA of the Taxation Administration Act 1953, so it concerns the amount and not whether the liability arises, and the amount stays a plain input (fork F-23) |
| F-22 | notes that state a consequence (for example s 59A(2) Note 2, that a notice creates no separate liability) | the matching functions in `sga-part7.l4` | encoded as `JUST FALSE` where the note says no in its own words | not encoded | the note |
| F-23 | s 49(3) | `the general interest charge payable under section 49` | one daily amount per day from the day the charge was due to the last day any of it remains unpaid, both days included; the amounts are plain inputs; a list of a different length gives `NOTHING` | the end day is not included | s 49(3) says the period "started at the beginning of the day" and "finishes at the end of the last day" |
| F-24 | s 74(2) | `the shortfall for which the employer qualifies for the amnesty` | the extent of the increase is never below nil: where the shortfall taking the information into account is lower than, or the same as, the shortfall without it, the extent is 0 | the difference as computed, which can be negative | s 74(2) says the employer qualifies "only to the extent of the increase in the shortfall as a result of taking the information into account" |
| S-1 | seat | the questions of `sga-seat.l4` | each question is one step of the calculation; the answer to one question is an input to the next (the base shortfall to the final shortfall, the final shortfall to notional earnings, and so on) | one question that runs the whole calculation | each step is a section of the Act |
| S-2 | seat | the questions that take contributions | the amounts and the days the fund received them are two lists in the same order and are paired one for one | a list of records | the form asks plain facts |

## What the Act turns out to say

Each statement is what the encoding takes the text to provide; "Asserted." marks those a case asserts, with the file that holds it.

1. A person's status as an employee under the Act comes from the ordinary meaning of the word, extended by the particular provisions of s 12, and a person paid to do domestic work for not more than 30 hours a week is not regarded as an employee in relation to that work (`sga-cases-seat.l4`, `sga-tests-part2.l4`). Asserted.
2. The charge percentage is 12, and the maximum contributions base is the concessional contributions cap times 100 over 12, rounded down to the nearest $10: a cap of $30,000 gives $250,000 and a cap of $27,500 gives $229,160 (`sga-cases-seat.l4`, `sga-tests-part2.l4`). Asserted.
3. A payment of qualifying earnings counts only up to the maximum contributions base: with $248,000 already paid and a base of $250,000 a payment of $4,000 counts as $2,000, and a later payment counts as nil (`sga-cases-seat.l4`, `sga-tests-part3a.l4`). Asserted.
4. The individual superannuation guarantee amount is 12 per cent of the qualifying earnings counted on the QE day, so $5,000 gives $600, and it is nil while an exemption certificate covers the QE day (`sga-cases-seat.l4`, `sga-tests-part3a.l4`). Asserted.
5. The usual period for a QE day ends on the seventh business day after it and the extended usual period on the 20th; for a QE day of 1 July 2026 with no public holidays they end on 10 July and 29 July 2026 (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
6. The individual base shortfall is the individual superannuation guarantee amount less the eligible contributions relevant for the QE day, and is never below nil: $600 less $400 received in time is $200, and $700 received in time leaves nil (`sga-cases-seat.l4`). Asserted.
7. A contribution received on 11 July 2026 for a QE day of 1 July 2026 is out of time unless a table item applies, and under item 1 a contribution received on 14 July 2026 is in time (`sga-cases-seat.l4`). Asserted.
8. The late period starts on the day after the latest day a contribution could be applied and ends on the day before the assessment is made, so with a latest day of 10 July and an assessment on 20 July 2026 it is 9 days long (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
9. The individual final shortfall is the base shortfall less the eligible contributions received during the late period, and never below nil (`sga-cases-seat.l4`, `sga-tests-part3b.l4`). Asserted.
10. Notional earnings compound daily on the base shortfall: $200 over two days at 1 per cent a day is $2.00 and then $2.02, $4.02 in all, and no day counts if the final shortfall is nil (`sga-cases-seat.l4`, `sga-tests-part3b.l4`). Asserted.
11. The administrative uplift is 60 per cent of the total final shortfalls and notional earnings components, reduced under the regulations but not below nil: 60 per cent of $600 is $360 and a reduction of $60 leaves $300 (`sga-cases-seat.l4`, `sga-tests-part3b.l4`). Asserted.
12. The choice loading is 25 per cent of the contributions not made in compliance with the choice of fund requirements, limited to $1,200 less 25 per cent of the other such contributions in the notice period: $2,000 gives $500, $6,000 gives $1,200, and $6,000 with $1,000 of other contributions gives $950 (`sga-cases-seat.l4`, `sga-tests-part3b.l4`). Asserted.
13. The employer's shortfall for a QE day is the total of the final shortfalls, the notional earnings components, the administrative uplift and the choice loadings: $150 + $6 + $90 + $500 is $746 (`sga-cases-seat.l4`, `sga-tests-part3b.l4`). Asserted.
14. A contribution to a fund is made in compliance with the choice of fund requirements if a limb of s 32C is met, unless the employer imposes a direct cost or charge on the employee because of having to contribute to that fund (`sga-cases-seat.l4`, `sga-tests-choice-of-fund.l4`). Asserted.
15. For a temporary visa holder the fund need not be specified in the standard choice form (s 32C(2AA)) (`sga-cases-seat.l4`, `sga-tests-choice-of-fund.l4`). Asserted.
16. A standard choice form for an employee employed on 1 July 2005 had to be given before 29 July 2005, so 28 July 2005 is in time and 29 July 2005 is not (`sga-cases-seat.l4`, `sga-tests-choice-of-fund.l4`). Asserted.
17. A fund becomes a chosen fund 2 months after the notice, or at an earlier time the employer determines after the notice: a notice on 15 July 2026 makes 15 September 2026, or an earlier day the employer sets (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
18. A statement is a voluntary disclosure statement only if it is lodged before the day an assessment is made and is in the approved form (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
19. Where a statement gives only a payment day, the receipt day is taken to be the seventh business day after it: a payment day of Friday 3 July 2026 gives Tuesday 14 July 2026 (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
20. An assessment can be amended at any time where the Commissioner is of the opinion that an avoidance is due to fraud or evasion, and otherwise within 4 years from the day the assessment is made (`sga-cases-seat.l4`, `sga-tests-part4-6.l4`). Asserted.
21. General interest charge accrues for each day from the day the charge was due to the last day any of it remains unpaid at the end of the day, both days included: due on 29 July and unpaid at the end of 31 July is three days (`sga-cases-seat.l4`, `sga-tests-time.l4`, `sga-tests-part4-6.l4`). Asserted.
22. The current notice trigger day is the day after the 28-day period starting on the imposition day: 29 July 2026 for 1 July 2026 (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
23. A notice to pay must be given only if the specified amount exceeds $30 (or a higher prescribed amount), no earlier notice was given in the 50 days ending the day before the trigger day, and no part of the amount was in an earlier notice (`sga-cases-seat.l4`, `sga-tests-part7.l4`). Asserted.
24. The payment period in a notice ends on the 28th day after the day the notice specifies: 26 August 2026 for 29 July 2026 (`sga-cases-seat.l4`, `sga-tests-time.l4`). Asserted.
25. The penalty is 0 per cent if a determination under s 18C(4) covers the employer for any part of the period, otherwise 50 per cent if an earlier penalty greater than nil became payable in the 24 months ending the day after the payment period, otherwise 25 per cent, of the part of the specified amount unpaid at the end of the payment period (`sga-cases-seat.l4`, `sga-tests-part7.l4`). Asserted.
26. The penalty becomes due on the day the notice specifies, which must be at least 14 days after the day the notice is given (`sga-cases-seat.l4`, `sga-tests-part7.l4`). Asserted.
27. The shortfall component for one benefiting employee is the lesser of the payment and the employee entitlement, and the entitlement is reduced by earlier payments but not below zero (`sga-tests-parts8-9.l4`). Asserted.
28. The amnesty period started on 24 May 2018, and an employer qualifies only if the amnesty period started after the end of the 28 days after the end of the quarter (`sga-cases-seat.l4`, `sga-tests-parts8-9.l4`). Asserted.
29. Records must be retained until the end of 5 years after they were prepared or obtained, or after the transactions to which they relate were completed, whichever is later (`sga-cases-seat.l4`, `sga-tests-parts8-9.l4`). Asserted.
30. Under s 74(2), where the employer would have a shortfall even without the information, it qualifies only to the extent of the increase, and never for a negative amount: a shortfall of $500 with the information and $200 without gives $300, and a shortfall of $100 or $50 with the information against $200 or $50.50 without gives nil (`sga-cases-seat.l4`, `sga-tests-parts8-9.l4`). Asserted.
31. Where the text leaves a case unanswered the encoding returns `NOTHING` and asserts it: a person who fits no part of s 12, a count of days whose list of daily rates has the mismatched length, a counting day in doubt, and a standard choice form where no trigger has occurred (`sga-cases-seat.l4`, `sga-tests-part2.l4`, `sga-tests-time.l4`). Asserted.

## What the stable binary does not accept

Observed with the writing build 1.6.98; the second build 1.6.110 read every module the same way.

- With `daydate` imported, directly or through an imported module, a chain of eight `PLUS` terms did not finish type-checking in 40 seconds, because each `PLUS` may add a number to a date; two-term helper functions (`the sum of two amounts`, `the difference of two amounts`) type-check in about half a second.
- `NOT (a) AND b` parses as `NOT ((a) AND b)`; every `NOT` is written as `(NOT (a)) AND b`, and a whole `NOT` term inside an `AND` or `OR` chain is parenthesised.
- A chain of `ELSE IF` at one indentation gives an indentation error; `BRANCH IF ... OTHERWISE` is used instead.
- A function parameter named like an imported or top-level function is ambiguous ("multiple definitions"); parameters have names no function has.
- `length` is not found; `count` is used.
- A name bound in a `WHERE` cannot refer to a variable bound by a pattern in the function body.
- A positional record built with `Record OF a, b, c` across several lines needs every continuation line indented further than the start of the expression.
- `FOLLOWED BY` is cons, not append.
- `YMD` is not defined by `daydate`; dates are written `Date day month year`, and `Date` rolls an impossible day forward.
- An `#ASSERT` is one line; arithmetic that crosses a line break is bracketed.
- No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` is used; a case the text does not answer returns `NOTHING`.
- No section-level `GIVEN` is used: each rule carries its own `GIVEN`.
- No `TYPICALLY` on record fields, no `WAIT UNTIL`, no sets.
- `IMPORT` finds only modules in the same folder.
- Numbers such as 20.1 and 4.02 compare exactly in an `#ASSERT`.

## What `check.sh` prints

Run from this folder as `L4=<1.6.98 build> L4_MAIN=<1.6.110 build> ./check.sh`; the exit status is 0.
Target `main`.
Main build compared with: 1.6.110 (main, e51181d, 2026-11-11).
`srcrefs.py check --refs ../../registers/source-bundle/C2004A04402.txt sga-*.l4` reports 1505 `src:` lines, 488 runs, 488 locators, 0 problems, and the same with `--strict` reports 0 problems.
Every module also runs with no `DiagnosticSeverity_Error` and no `_Warning`.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sga-cases-seat.l4                              0       148       0        0         0 |      0       148       0        0  same
sga-choice-of-fund.l4                          0         0       0        0         0 |      0         0       0        0  same
sga-defs.l4                                    0       208       0        0         0 |      0       208       0        0  same
sga-part1.l4                                   0         0       0        0         0 |      0         0       0        0  same
sga-part2.l4                                   0         0       0        0         0 |      0         0       0        0  same
sga-part3a.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga-part3b.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga-part4-6.l4                                 0         0       0        0         0 |      0         0       0        0  same
sga-part7.l4                                   0         0       0        0         0 |      0         0       0        0  same
sga-parts8-9.l4                                0         0       0        0         0 |      0         0       0        0  same
sga-provisions.l4                              0         6       0        0         0 |      0         6       0        0  same
sga-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sga-tests-choice-of-fund.l4                    0       147       0        0         0 |      0       147       0        0  same
sga-tests-part1.l4                             0        45       0        0         0 |      0        45       0        0  same
sga-tests-part2.l4                             0       128       0        0         0 |      0       128       0        0  same
sga-tests-part3a.l4                            0        79       0        0         0 |      0        79       0        0  same
sga-tests-part3b.l4                            0        86       0        0         0 |      0        86       0        0  same
sga-tests-part4-6.l4                           0        64       0        0         0 |      0        64       0        0  same
sga-tests-part7.l4                             0        56       0        0         0 |      0        56       0        0  same
sga-tests-parts8-9.l4                          0       109       0        0         0 |      0       109       0        0  same
sga-tests-time.l4                              0       260       0        0         0 |      0       260       0        0  same
sga-time.l4                                    0         0       0        0         0 |      0         0       0        0  same
sga-xrefs.l4                                   0       440       0        0         0 |      0       440       0        0  same
TOTAL (23 modules)                             0      1776       0        0           |      0      1776       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Cross-references

`sga-xrefs.l4` holds every reference in the text to another provision, 438 rows: 317 to a provision of the same text and 121 to another Act or instrument.
Each row names the citing provision, the words as printed, the identifier cited and the heading of the cited provision as the text prints it, and has one assertion beneath the table.
The 317 internal rows by the word that introduces the reference: subsection 142, section 78, paragraph 71, subparagraph 13, Part 3, Subdivision 4, item 3, Division 2, and one "the definition of".
Five of the internal rows cite a defined term.
The 121 other rows cite 28 instruments; the largest groups are the Taxation Administration Act 1953 (26), the Superannuation Industry (Supervision) Act 1993 (18), the Income Tax Assessment Act 1997 (11), the Fair Work (Transitional Provisions and Consequential Amendments) Act 2009 (9), the Fair Work Act 2009 (7) and the Criminal Code (6).
A reference to another instrument is not resolved; its target is not among the sources.

The script finds them by reading the text file line by line.
It matches a keyword (section, subsection, paragraph, subparagraph, Part, Division, Subdivision, item, Schedule, or "the definition of") followed by an identifier or a list of identifiers joined by "and", "or" or "to".
It resolves a bare reference such as "subsection (2)" inside the citing section, and a full reference such as "section 32N" against the provision index.
A reference followed by "of that Act", "of the" and an Act's name, or "in Schedule 1 to" an Act, is a reference to another instrument.
A reference whose cited identifier is missing from the index is kept out of the deposit; there are none.

## What remains before the encoding is worth relying on

- A domain expert has to read it against the authorised text of the compilation, not the plain-text conversion it was written from.
- The forks need a ruling by someone with authority to rule on them, above all how a period is counted from an event (F-1, F-2), how the notional contribution formula is read (F-3), how the final shortfall is tested day by day (F-4) and what follows when the condition of a power or a deeming fails (F-21).
- The instruments the Act borrows have to be brought in or confirmed as inputs: the general interest charge rate under Part IIA of the Taxation Administration Act 1953, the concessional contributions cap for each year, the value of a penalty unit, the regulations the Act mentions (ss 6AA, 10(6), 19B(3), 59A(2), 80), the determinations under s 18C and the date of the Royal Assent of the 2020 amending Act.
- The formulas the text conversion lost (ss 10A(5), 17A(2), 18A(3)(d)(iii), 18C(1), 18D(2), 19A(2), 64B(3)) have to be checked against the authorised compilation; they are read here from the transcription in `C2004A04402.formulas.md`.
- Every expected value in the tests is worked by hand from the text; none has been compared with an outside calculator, a published example or the Commissioner's own figures.
- The seat questions need a trial in the Interact form with an employer or an adviser: they take lists (holidays, daily rates, contribution amounts and days) and one enumerated choice (the event that triggers a standard choice form), and the way a form presents them has not been seen.

## Coverage table

The table gives one row for every section, subsection, paragraph, table row and defined term of the in-scope text (lines 22 to 1353 of `C2004A04402.txt`): 930 rows.
A subparagraph or sub-subparagraph is owned by the paragraph or subsection row that contains it, and a Part, Division or Subdivision heading by the row that follows it.
Every one of the 1332 non-blank in-scope lines is owned by exactly one row, and every row has exactly one disposition; the script that builds the table checks both and is kept outside the deposit.
The provision index `sga-provisions.l4` lists every unit of the text, and the cross-reference table lists every reference, so the `where` column names only the module that carries the rule.

Dispositions:

- `encoded` (737 rows): every operative line of the row is quoted by a rule in the module named.
- `defined term` (86 rows): a definition kept as a record in `sga-defs.l4`; no rule applies it directly.
- `non-operative` (67 rows): headings, introductory words of definitions, and notes only.
- `outline` (17 rows): a simplified outline, purpose, structure or overview.
- `machinery` (20 rows): commencement, extent, powers to make regulations and to determine by instrument.
- `not encoded` (3 rows): the reason is in the row.

| row | kind | text lines | disposition | where or why |
| --- | --- | --- | --- | --- |
| 1 | section | 22-26 | machinery | short title, commencement and territorial extent; no rule for an employer to apply |
| 2 | section | 27-28 | machinery | short title, commencement and territorial extent; no rule for an employer to apply |
| 3 | section | 29 | non-operative | headings, introductory words of definitions, and notes only |
| 3(1) | subsection | 30 | encoded | `sga-part1.l4` |
| 3(2) | subsection | 31 | encoded | `sga-part1.l4` |
| 4 | section | 32-33 | machinery | short title, commencement and territorial extent; no rule for an employer to apply |
| 5 | section | 34 | non-operative | headings, introductory words of definitions, and notes only |
| 5(1) | subsection | 35 | encoded | `sga-part1.l4` |
| 5(2) | subsection | 36 | encoded | `sga-part1.l4` |
| 5(2)(a) | paragraph | 37 | encoded | `sga-part1.l4` |
| 5(2)(b) | paragraph | 38 | encoded | `sga-part1.l4` |
| 5(2)(c) | paragraph | 39 | encoded | `sga-part1.l4` |
| 5(2A) | subsection | 40 | encoded | `sga-part1.l4` |
| 5(2B) | subsection | 41 | encoded | `sga-part1.l4` |
| 5(2C) | subsection | 42 | encoded | `sga-part1.l4` |
| 5(3) | subsection | 43 | encoded | `sga-part1.l4` |
| 5(3)(a) | paragraph | 44 | encoded | `sga-part1.l4` |
| 5(3)(b) | paragraph | 45-46 | encoded | `sga-part1.l4` |
| 5(4) | subsection | 47 | encoded | `sga-part1.l4` |
| 5(5) | subsection | 48 | non-operative | headings, introductory words of definitions, and notes only |
| 5(5) definition: Commonwealth Department | definition | 49 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: Commonwealth Department(a) | paragraph | 50 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: Commonwealth Department(b) | paragraph | 51 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: Commonwealth Department(c) | paragraph | 52 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: Commonwealth entity | definition | 53 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: Finance Department | definition | 54 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 5(5) definition: Finance Minister | definition | 55 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 5(5) definition: responsible Department | definition | 56 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: responsible Department(a) | paragraph | 57 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: responsible Department(b) | paragraph | 58-60 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: responsible Department(c) | paragraph | 61 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5(5) definition: untaxable Commonwealth authority | definition | 62 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5A | section | 63 | non-operative | headings, introductory words of definitions, and notes only |
| 5A(1) | subsection | 64 | encoded | `sga-part1.l4` |
| 5A(1) definition: Commonwealth authority | definition | 65 | encoded | `sga-defs.l4`, `sga-part1.l4` |
| 5A(2) | subsection | 66 | encoded | `sga-part1.l4` |
| 5A(2)(a) | paragraph | 67-69 | encoded | `sga-part1.l4` |
| 5A(2)(b) | paragraph | 70-71 | encoded | `sga-part1.l4` |
| 5A(3) | subsection | 72 | encoded | `sga-part1.l4` |
| 5A(3)(a) | paragraph | 73-75 | encoded | `sga-part1.l4` |
| 5A(3)(b) | paragraph | 76-77 | encoded | `sga-part1.l4` |
| 5B | section | 78 | non-operative | headings, introductory words of definitions, and notes only |
| 5B(1) | subsection | 79 | encoded | `sga-part1.l4` |
| 5B(1)(a) | paragraph | 80 | encoded | `sga-part1.l4` |
| 5B(1)(b) | paragraph | 81 | encoded | `sga-part1.l4` |
| 5B(2) | subsection | 82 | encoded | `sga-part1.l4` |
| 5C | section | 83-85 | encoded | `sga-part1.l4` |
| 6 | section | 86-88 | non-operative | headings, introductory words of definitions, and notes only |
| 6(1) | subsection | 89 | non-operative | headings, introductory words of definitions, and notes only |
| 6(1) definition: actuary | definition | 90 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: administrative uplift amount | definition | 91 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: approved deposit fund | definition | 92 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: approved form | definition | 93 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: arrangement | definition | 94 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: arrangement(a) | paragraph | 95 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: arrangement(b) | paragraph | 96 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: assessment | definition | 97 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: associate | definition | 98 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Australia | definition | 99 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: benefit certificate | definition | 100 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: business day | definition | 101 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: business day(a) | paragraph | 102 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: business day(b) | paragraph | 103-106 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: choice loading | definition | 107 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: choice loading limit | definition | 108 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commissioner | definition | 109 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth employee | definition | 110 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth industrial award | definition | 111 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth industrial award(a) | paragraph | 112 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth industrial award(b) | paragraph | 113 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth industrial award(c) | paragraph | 114 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Commonwealth industrial award(d) | paragraph | 115 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying approved deposit fund | definition | 116 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying superannuation fund | definition | 117 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying superannuation fund or scheme | definition | 118 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying superannuation fund or scheme(a) | paragraph | 119 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying superannuation fund or scheme(b) | paragraph | 120 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: complying superannuation scheme | definition | 121 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: concessional contributions | definition | 122 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: conversion notice | definition | 123 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: CSS | definition | 124 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: data processing device | definition | 125 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: defined benefit member | definition | 126 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: defined benefit member(a) | paragraph | 127-129 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: defined benefit member(b) | paragraph | 130 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: defined benefit superannuation scheme | definition | 131 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Deputy Commissioner | definition | 132 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: eligible contribution | definition | 133 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: employee | definition | 134 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: employer | definition | 135 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: employer shortfall exemption certificate | definition | 136 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: enterprise agreement | definition | 137 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: excess concessional contributions | definition | 138 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: extended usual period | definition | 139 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: extended usual period(a) | paragraph | 140 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: extended usual period(b) | paragraph | 141 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: general interest charge | definition | 142 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: government body | definition | 143 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: government body(a) | paragraph | 144 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: government body(b) | paragraph | 145 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: individual base superannuation guarantee shortfall | definition | 146 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: individual final superannuation guarantee shortfall | definition | 147 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: individual notional earnings component | definition | 148 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: individual superannuation guarantee amount | definition | 149 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: industrial award | definition | 150 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: late period | definition | 151 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: late period(a) | paragraph | 152 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: late period(b) | paragraph | 153 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: liability to the Commonwealth | definition | 154 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: lodge | definition | 155 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: maximum contributions base | definition | 156 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: MySuper member | definition | 157 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: occupational superannuation arrangement | definition | 158 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: offence against this Act | definition | 159 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: offence against this Act(a) | paragraph | 160 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: offence against this Act(b) | paragraph | 161 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: ordinary time earnings | definition | 162 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: ordinary time earnings(a) | paragraph | 163 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: ordinary time earnings(b) | paragraph | 164-165 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: ordinary time earnings(c) | paragraph | 166 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: ordinary time earnings(d) | paragraph | 167 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: part-time employee | definition | 168 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: payment day | definition | 169 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: payment of qualifying earnings to or for an employee | definition | 170 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: penalty assessment | definition | 171 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: proceeding under this Act | definition | 172 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: proceeding under this Act(a) | paragraph | 173 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: proceeding under this Act(b) | paragraph | 174 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: PSS | definition | 175 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: PSSAP | definition | 176 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: public sector scheme | definition | 177 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: public sector scheme(a) | paragraph | 178 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: public sector scheme(b) | paragraph | 179-181 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: QE day | definition | 182 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: qualifying earnings | definition | 183 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: quarter | definition | 184 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: receipt day | definition | 185 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: resident of Australia | definition | 186 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: resident regulated superannuation fund | definition | 187 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: RSA | definition | 188 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: RSA provider | definition | 189 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: sacrificed contribution | definition | 190 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Second Commissioner | definition | 191 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: stapled fund | definition | 192 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: State industrial award | definition | 193 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: State industrial award(a) | paragraph | 194 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: State industrial award(b) | paragraph | 195 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: superannuation fund | definition | 196 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: superannuation guarantee charge | definition | 197 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: superannuation guarantee shortfall | definition | 198 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: superannuation provider | definition | 199 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation provider(a) | paragraph | 200 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation provider(b) | paragraph | 201 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation provider(c) | paragraph | 202 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation scheme | definition | 203 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation scheme(a) | paragraph | 204 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: superannuation scheme(b) | paragraph | 205 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: Territory industrial award | definition | 206 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Territory industrial award(a) | paragraph | 207 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: Territory industrial award(b) | paragraph | 208 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: trustee | definition | 209 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee(a) | paragraph | 210-213 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee(b) | paragraph | 214 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2] | definition | 215 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](a) | paragraph | 216-219 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](b) | paragraph | 220 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](c) | paragraph | 221 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](d) | paragraph | 222 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](e) | paragraph | 223 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: trustee [2](f) | paragraph | 224-227 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: unfunded public sector scheme | definition | 228 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: unfunded public sector scheme(a) | paragraph | 229 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: unfunded public sector scheme(b) | paragraph | 230 | encoded | `sga-defs.l4`, `sga-part2.l4` |
| 6(1) definition: usual period | definition | 231 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: usual period(a) | paragraph | 232 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: usual period(b) | paragraph | 233 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(1) definition: voluntary disclosure statement | definition | 234 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: workplace determination | definition | 235 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 6(1) definition: year | definition | 236 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 6(2) | subsection | 237 | encoded | `sga-part2.l4` |
| 6AA | section | 238-239 | encoded | `sga-part2.l4` |
| 6AA(a) | paragraph | 240 | encoded | `sga-part2.l4` |
| 6AA(b) | paragraph | 241 | encoded | `sga-part2.l4` |
| 6A | section | 242 | non-operative | headings, introductory words of definitions, and notes only |
| 6A(1) | subsection | 243 | encoded | `sga-part2.l4` |
| 6A(1)(a) | paragraph | 244-249 | encoded | `sga-part2.l4` |
| 6A(1)(b) | paragraph | 250 | encoded | `sga-part2.l4` |
| 6A(2) | subsection | 251 | encoded | `sga-part2.l4` |
| 6A(3) | subsection | 252 | encoded | `sga-part2.l4` |
| 6A(4) | subsection | 253 | encoded | `sga-part2.l4` |
| 6B | section | 254 | non-operative | headings, introductory words of definitions, and notes only |
| 6B(1) | subsection | 255 | encoded | `sga-part2.l4` |
| 6B(2) | subsection | 256 | encoded | `sga-part2.l4` |
| 6B(3) | subsection | 257 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(3)(a) | paragraph | 258 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(3)(b) | paragraph | 259 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(3)(c) | paragraph | 260 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(3)(d) | paragraph | 261 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(3)(e) | paragraph | 262 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 6B(4) | subsection | 263 | encoded | `sga-part2.l4` |
| 6B(4)(a) | paragraph | 264 | encoded | `sga-part2.l4` |
| 6B(4)(b) | paragraph | 265-266 | encoded | `sga-part2.l4` |
| 6B(5) | subsection | 267 | encoded | `sga-part2.l4` |
| 6B(5)(a) | paragraph | 268 | encoded | `sga-part2.l4` |
| 6B(5)(b) | paragraph | 269-270 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 7 | section | 271-272 | encoded | `sga-part2.l4` |
| 7A | section | 273-274 | encoded | `sga-part2.l4` |
| 8 | section | 275-276 | encoded | `sga-part2.l4` |
| 10 | section | 277 | non-operative | headings, introductory words of definitions, and notes only |
| 10(1) | subsection | 278 | encoded | `sga-part2.l4` |
| 10(2) | subsection | 279 | not encoded | the notional employer contribution rate is stated by an actuary in a benefit certificate; it is a plain input expressed as a percentage |
| 10(3) | subsection | 280 | encoded | `sga-part2.l4` |
| 10(3)(a) | paragraph | 281 | encoded | `sga-part2.l4` |
| 10(3)(b) | paragraph | 282 | encoded | `sga-part2.l4` |
| 10(3)(c) | paragraph | 283 | encoded | `sga-part2.l4`, `sga-time.l4` |
| 10(3)(d) | paragraph | 284-285 | encoded | `sga-part2.l4` |
| 10(4) | subsection | 286 | encoded | `sga-time.l4` |
| 10(4)(a) | paragraph | 287-292 | encoded | `sga-time.l4` |
| 10(4)(b) | paragraph | 293 | encoded | `sga-time.l4` |
| 10(6) | subsection | 294 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 10(6)(a) | paragraph | 295 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 10(6)(b) | paragraph | 296 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 10(6)(c) | paragraph | 297 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 10(6)(d) | paragraph | 298 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 10A | section | 299-300 | non-operative | headings, introductory words of definitions, and notes only |
| 10A(1) | subsection | 301 | encoded | `sga-part2.l4` |
| 10A(1)(a) | paragraph | 302 | encoded | `sga-part2.l4` |
| 10A(1)(b) | paragraph | 303 | encoded | `sga-part2.l4` |
| 10A(1)(c) | paragraph | 304 | encoded | `sga-part2.l4` |
| 10A(1)(d) | paragraph | 305 | encoded | `sga-part2.l4` |
| 10A(1)(e) | paragraph | 306 | encoded | `sga-part2.l4` |
| 10A(1)(f) | paragraph | 307 | encoded | `sga-part2.l4` |
| 10A(1)(g) | paragraph | 308 | encoded | `sga-part2.l4` |
| 10A(1)(h) | paragraph | 309-313 | encoded | `sga-part2.l4` |
| 10A(2) | subsection | 314-315 | encoded | `sga-part2.l4` |
| 10A(3) | subsection | 316 | encoded | `sga-part2.l4` |
| 10A(3)(a) | paragraph | 317 | encoded | `sga-part2.l4` |
| 10A(3)(b) | paragraph | 318-322 | encoded | `sga-part2.l4` |
| 10A(4) | subsection | 323 | encoded | `sga-part2.l4` |
| 10A(4)(a) | paragraph | 324 | encoded | `sga-part2.l4` |
| 10A(4)(b) | paragraph | 325-326 | encoded | `sga-part2.l4` |
| 10A(5) | subsection | 327-328 | encoded | `sga-part2.l4` |
| 10A(5) definition: charge percentage | definition | 329 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 10A(5) definition: concessional contributions cap | definition | 330 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 10A(6) | subsection | 331 | encoded | `sga-part2.l4` |
| 10A(6)(a) | paragraph | 332 | encoded | `sga-part2.l4` |
| 10A(6)(b) | paragraph | 333-334 | encoded | `sga-part2.l4` |
| 10A(6)(c) | paragraph | 335 | encoded | `sga-part2.l4` |
| 10A(6)(d) | paragraph | 336 | encoded | `sga-part2.l4` |
| 12 | section | 337 | non-operative | headings, introductory words of definitions, and notes only |
| 12(1) | subsection | 338 | encoded | `sga-part2.l4` |
| 12(1)(a) | paragraph | 339 | encoded | `sga-part2.l4` |
| 12(1)(b) | paragraph | 340 | encoded | `sga-part2.l4` |
| 12(2) | subsection | 341 | encoded | `sga-part2.l4` |
| 12(3) | subsection | 342 | encoded | `sga-part2.l4` |
| 12(4) | subsection | 343 | encoded | `sga-part2.l4` |
| 12(5) | subsection | 344 | encoded | `sga-part2.l4` |
| 12(6) | subsection | 345 | encoded | `sga-part2.l4` |
| 12(7) | subsection | 346 | encoded | `sga-part2.l4` |
| 12(8) | subsection | 347 | encoded | `sga-part2.l4` |
| 12(8)(a) | paragraph | 348 | encoded | `sga-part2.l4` |
| 12(8)(b) | paragraph | 349 | encoded | `sga-part2.l4` |
| 12(8)(c) | paragraph | 350 | encoded | `sga-part2.l4` |
| 12(9) | subsection | 351 | encoded | `sga-part2.l4` |
| 12(9)(a) | paragraph | 352 | encoded | `sga-part2.l4` |
| 12(9)(b) | paragraph | 353-354 | encoded | `sga-part2.l4` |
| 12(9A) | subsection | 355 | encoded | `sga-part2.l4` |
| 12(10) | subsection | 356 | encoded | `sga-part2.l4` |
| 12(11) | subsection | 357 | encoded | `sga-part2.l4` |
| 12A | section | 358 | non-operative | headings, introductory words of definitions, and notes only |
| 12A(1) | subsection | 359 | encoded | `sga-part2.l4` |
| 12A(1)(a) | paragraph | 360 | encoded | `sga-part2.l4` |
| 12A(1)(b) | paragraph | 361 | encoded | `sga-part2.l4` |
| 12A(1)(c) | paragraph | 362 | encoded | `sga-part2.l4` |
| 12A(1)(d) | paragraph | 363 | encoded | `sga-part2.l4` |
| 12A(1)(e) | paragraph | 364 | encoded | `sga-part2.l4` |
| 12A(1)(f) | paragraph | 365 | encoded | `sga-part2.l4` |
| 12A(1)(g) | paragraph | 366 | encoded | `sga-part2.l4` |
| 12A(1)(h) | paragraph | 367 | encoded | `sga-part2.l4` |
| 12A(1)(i) | paragraph | 368 | encoded | `sga-part2.l4` |
| 12A(1)(j) | paragraph | 369-370 | encoded | `sga-part2.l4` |
| 12A(2) | subsection | 371 | encoded | `sga-part2.l4` |
| 12A(3) | subsection | 372 | encoded | `sga-part2.l4` |
| 15B | section | 373-376 | encoded | `sga-part3a.l4` |
| 15C | section | 377 | non-operative | headings, introductory words of definitions, and notes only |
| 15C(1) | subsection | 378 | encoded | `sga-part3a.l4` |
| 15C(2) | subsection | 379 | encoded | `sga-part3a.l4` |
| 15C(3) | subsection | 380 | encoded | `sga-part3a.l4` |
| 15C(3)(a) | paragraph | 381 | encoded | `sga-part3a.l4` |
| 15C(3)(b) | paragraph | 382 | encoded | `sga-part3a.l4` |
| 15C(4) | subsection | 383 | encoded | `sga-part3a.l4` |
| 15C(5) | subsection | 384 | encoded | `sga-part3a.l4` |
| 15C(5)(a) | paragraph | 385 | encoded | `sga-part3a.l4` |
| 15C(5)(b) | paragraph | 386 | encoded | `sga-part3a.l4` |
| 15C(5)(c) | paragraph | 387 | encoded | `sga-part3a.l4` |
| 15C(6) | subsection | 388 | encoded | `sga-part3a.l4` |
| 15C(7) | subsection | 389 | encoded | `sga-part3a.l4` |
| 15C(8) | subsection | 390 | encoded | `sga-part3a.l4` |
| 16 | section | 391-396 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 16(a) | paragraph | 397 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 16(b) | paragraph | 398-401 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 16A | section | 402-403 | encoded | `sga-part3a.l4` |
| 16B | section | 404 | encoded | `sga-part3b.l4` |
| 16B(1) | subsection | 405 | encoded | `sga-part3b.l4` |
| 16B(1)(a) | paragraph | 406 | encoded | `sga-part3b.l4` |
| 16B(1)(b) | paragraph | 407 | encoded | `sga-part3b.l4` |
| 16B(2) | subsection | 408 | encoded | `sga-part3b.l4` |
| 16B(2)(a) | paragraph | 409 | encoded | `sga-part3b.l4` |
| 16B(2)(b) | paragraph | 410 | encoded | `sga-part3b.l4` |
| 16B(2)(c) | paragraph | 411 | encoded | `sga-part3b.l4` |
| 16B(2)(d) | paragraph | 412-413 | encoded | `sga-part3b.l4` |
| 17 | section | 414-416 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 17(a) | paragraph | 417 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 17(b) | paragraph | 418-420 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 17A | section | 421 | non-operative | headings, introductory words of definitions, and notes only |
| 17A(1) | subsection | 422-423 | encoded | `sga-part3a.l4` |
| 17A(2) | subsection | 424-425 | encoded | `sga-part3a.l4` |
| 17A(2) definition: amount of the qualifying earnings | definition | 426 | encoded | `sga-defs.l4`, `sga-part3a.l4` |
| 17A(2) definition: amount of the qualifying earnings(a) | paragraph | 427 | encoded | `sga-defs.l4`, `sga-part3a.l4` |
| 17A(2) definition: amount of the qualifying earnings(b) | paragraph | 428-429 | encoded | `sga-defs.l4`, `sga-part3a.l4` |
| 17A(2) definition: charge percentage | definition | 430 | encoded | `sga-defs.l4`, `sga-part3a.l4` |
| 17B | section | 431-432 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17B(a) | paragraph | 433 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17B(b) | paragraph | 434-436 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17B Note 1(a) | paragraph | 437 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17B Note 1(b) | paragraph | 438-439 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17C | section | 440-441 | non-operative | headings, introductory words of definitions, and notes only |
| 17C(1) | subsection | 442 | encoded | `sga-part3a.l4` |
| 17C(1)(a) | paragraph | 443 | encoded | `sga-part3a.l4` |
| 17C(1)(b) | paragraph | 444-445 | encoded | `sga-part3a.l4` |
| 17C(2) | subsection | 446 | encoded | `sga-part3a.l4` |
| 17C(2)(a) | paragraph | 447 | encoded | `sga-part3a.l4` |
| 17C(2)(b) | paragraph | 448-451 | encoded | `sga-part3a.l4` |
| 17C(2)(c) | paragraph | 452 | encoded | `sga-part3a.l4` |
| 17C(3) | subsection | 453 | encoded | `sga-part3a.l4` |
| 17C(3)(a) | paragraph | 454 | encoded | `sga-part3a.l4` |
| 17C(3)(b) | paragraph | 455-458 | encoded | `sga-part3a.l4` |
| 17C(4) | subsection | 459 | encoded | `sga-part3a.l4` |
| 17C(4)(a) | paragraph | 460 | encoded | `sga-part3a.l4` |
| 17C(4)(b) | paragraph | 461 | encoded | `sga-part3a.l4` |
| 17C(4)(c) | paragraph | 462-463 | encoded | `sga-part3a.l4`, `sga-time.l4` |
| 17C(5) | subsection | 464 | encoded | `sga-part3a.l4` |
| 17C(6) | subsection | 465 | encoded | `sga-part3a.l4` |
| 17C(7) | subsection | 466 | encoded | `sga-part3a.l4` |
| 17C(7)(a) | paragraph | 467 | encoded | `sga-part3a.l4` |
| 17C(7)(b) | paragraph | 468 | encoded | `sga-part3a.l4` |
| 17D | section | 469 | non-operative | headings, introductory words of definitions, and notes only |
| 17D(1) | subsection | 470 | encoded | `sga-part3a.l4` |
| 17D(1)(a) | paragraph | 471 | encoded | `sga-part3a.l4` |
| 17D(1)(b) | paragraph | 472 | encoded | `sga-part3a.l4` |
| 17D(2) | subsection | 473 | encoded | `sga-part3a.l4` |
| 17D(3) | subsection | 474 | encoded | `sga-time.l4` |
| 18 | section | 475-478 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 18(a) | paragraph | 479 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 18(b) | paragraph | 480-481 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 18(a) [2] | paragraph | 482 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 18(b) [2] | paragraph | 483 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 18A | section | 484 | non-operative | headings, introductory words of definitions, and notes only |
| 18A(1) | subsection | 485 | encoded | `sga-part3a.l4` |
| 18A(1)(a) | paragraph | 486-490 | encoded | `sga-part3a.l4` |
| 18A(1)(b) | paragraph | 491-493 | encoded | `sga-part3a.l4` |
| 18A(1)(c) | paragraph | 494-498 | encoded | `sga-part3a.l4` |
| 18A(1)(d) | paragraph | 499-501 | encoded | `sga-part3a.l4` |
| 18A(2) | subsection | 502 | encoded | `sga-part3a.l4` |
| 18A(2)(a) | paragraph | 503 | encoded | `sga-part3a.l4` |
| 18A(2)(b) | paragraph | 504-509 | encoded | `sga-part3a.l4` |
| 18A(3) | subsection | 510 | encoded | `sga-part3a.l4` |
| 18A(3)(a) | paragraph | 511 | encoded | `sga-part3a.l4` |
| 18A(3)(b) | paragraph | 512-514 | encoded | `sga-part3a.l4` |
| 18A(3)(c) | paragraph | 515-517 | encoded | `sga-part3a.l4` |
| 18A(3)(d) | paragraph | 518-523 | encoded | `sga-part3a.l4` |
| 18A(3) definition: amount of the qualifying earnings | definition | 524-525 | encoded | `sga-defs.l4`, `sga-part3a.l4` |
| 18B | section | 526 | non-operative | headings, introductory words of definitions, and notes only |
| 18B(1) | subsection | 527 | encoded | `sga-part3a.l4` |
| 18B(1)(a) | paragraph | 528 | encoded | `sga-part3a.l4` |
| 18B(1)(b) | paragraph | 529 | encoded | `sga-part3a.l4` |
| 18B(2) | subsection | 530 | encoded | `sga-part3a.l4` |
| 18B(2)(a) | paragraph | 531-534 | encoded | `sga-part3a.l4` |
| 18B(2)(b) | paragraph | 535-537 | encoded | `sga-part3a.l4` |
| 18B(3) | subsection | 538-539 | encoded | `sga-part3a.l4` |
| 18C | section | 540-541 | non-operative | headings, introductory words of definitions, and notes only |
| 18C(1) | subsection | 542-543 | encoded | `sga-part3b.l4` |
| 18C(1) definition: eligible contributions relevant for the QE day | definition | 544 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18C(1) definition: eligible contributions relevant for the QE day(a) | paragraph | 545 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18C(1) definition: eligible contributions relevant for the QE day(b) | paragraph | 546 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18C(1) definition: eligible contributions relevant for the QE day(c) | paragraph | 547-550 | encoded | `sga-defs.l4`, `sga-part3b.l4`, `sga-time.l4` |
| 18C(1) definition: eligible contributions relevant for the QE day(d) | paragraph | 551-553 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18C(2) | subsection | 554-558 | encoded | `sga-time.l4` |
| 18C(2) item 1 | item | 559-563 | encoded | `sga-time.l4` |
| 18C(2) item 2 | item | 564-567 | encoded | `sga-time.l4` |
| 18C(2) item 3 | item | 568-572 | encoded | `sga-time.l4` |
| 18C(2) item 4 | item | 573-580 | encoded | `sga-time.l4` |
| 18C(3) | subsection | 581 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18C(3)(a) | paragraph | 582 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18C(3)(b) | paragraph | 583-584 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18C(4) | subsection | 585 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18C(4)(a) | paragraph | 586 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18C(4)(b) | paragraph | 587-590 | machinery | power of the Commissioner to determine by legislative instrument; the effect of a determination is a plain input (table items 2 and 3, penalty item 1) |
| 18D | section | 591 | non-operative | headings, introductory words of definitions, and notes only |
| 18D(1) | subsection | 592 | encoded | `sga-part3b.l4` |
| 18D(1)(a) | paragraph | 593 | encoded | `sga-part3b.l4` |
| 18D(1)(b) | paragraph | 594 | encoded | `sga-part3b.l4` |
| 18D(2) | subsection | 595-596 | encoded | `sga-part3b.l4` |
| 18D(2) definition: eligible contributions relevant for the late period for the QE day | definition | 597 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18D(2) definition: eligible contributions relevant for the late period for the QE day(a) | paragraph | 598 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18D(2) definition: eligible contributions relevant for the late period for the QE day(b) | paragraph | 599 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18D(2) definition: eligible contributions relevant for the late period for the QE day(c) | paragraph | 600 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 18D(2) definition: eligible contributions relevant for the late period for the QE day(d) | paragraph | 601 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 19 | section | 602-604 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 19A | section | 605 | non-operative | headings, introductory words of definitions, and notes only |
| 19A(1) | subsection | 606 | encoded | `sga-part3b.l4` |
| 19A(1)(a) | paragraph | 607 | encoded | `sga-part3b.l4` |
| 19A(1)(b) | paragraph | 608-609 | encoded | `sga-part3b.l4` |
| 19A(2) | subsection | 610-611 | encoded | `sga-part3b.l4` |
| 19A(2) definition: general interest charge rate | definition | 612 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 19A(2) definition: notional sum | definition | 613 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 19A(2) definition: notional sum(a) | paragraph | 614 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 19A(2) definition: notional sum(b) | paragraph | 615 | encoded | `sga-defs.l4`, `sga-part3b.l4` |
| 19B | section | 616 | non-operative | headings, introductory words of definitions, and notes only |
| 19B(1) | subsection | 617 | encoded | `sga-part3b.l4` |
| 19B(1)(a) | paragraph | 618 | encoded | `sga-part3b.l4` |
| 19B(1)(b) | paragraph | 619-620 | encoded | `sga-part3b.l4` |
| 19B(2) | subsection | 621 | encoded | `sga-part3b.l4` |
| 19B(3) | subsection | 622 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 19B(3)(a) | paragraph | 623-626 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 19B(3)(b) | paragraph | 627 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 20 | section | 628-630 | encoded | `sga-part3b.l4` |
| 20(a) | paragraph | 631 | encoded | `sga-part3b.l4` |
| 20(b) | paragraph | 632-634 | encoded | `sga-part3b.l4` |
| 20A | section | 635 | non-operative | headings, introductory words of definitions, and notes only |
| 20A(1) | subsection | 636 | encoded | `sga-part3b.l4` |
| 20A(1)(a) | paragraph | 637-639 | encoded | `sga-part3b.l4` |
| 20A(1)(b) | paragraph | 640-641 | encoded | `sga-part3b.l4` |
| 20A(2) | subsection | 642 | encoded | `sga-part3b.l4` |
| 20A(2)(a) | paragraph | 643 | encoded | `sga-part3b.l4` |
| 20A(2)(b) | paragraph | 644-645 | encoded | `sga-part3b.l4` |
| 20A(3) | subsection | 646 | encoded | `sga-part3b.l4` |
| 20A(3)(a) | paragraph | 647-649 | encoded | `sga-part3b.l4` |
| 20A(3)(b) | paragraph | 650 | encoded | `sga-part3b.l4` |
| 20A(3)(c) | paragraph | 651-652 | encoded | `sga-part3b.l4` |
| 20B | section | 653 | non-operative | headings, introductory words of definitions, and notes only |
| 20B(1) | subsection | 654-655 | encoded | `sga-part3b.l4` |
| 20B(2) | subsection | 656 | encoded | `sga-part3b.l4` |
| 20B(2)(a) | paragraph | 657-659 | encoded | `sga-part3b.l4` |
| 20B(2)(b) | paragraph | 660 | encoded | `sga-part3b.l4` |
| 20B(2)(c) | paragraph | 661-663 | encoded | `sga-part3b.l4`, `sga-time.l4` |
| 20B(3) | subsection | 664 | encoded | `sga-part3b.l4` |
| 20B(3)(a) | paragraph | 665 | encoded | `sga-part3b.l4` |
| 20B(3)(b) | paragraph | 666 | encoded | `sga-part3b.l4` |
| 20B(3)(c) | paragraph | 667 | encoded | `sga-part3b.l4` |
| 20B(3)(d) | paragraph | 668-669 | encoded | `sga-part3b.l4` |
| 20B(4) | subsection | 670 | encoded | `sga-part3b.l4` |
| 20B(4)(a) | paragraph | 671 | encoded | `sga-part3b.l4` |
| 20B(4)(b) | paragraph | 672-674 | encoded | `sga-part3b.l4` |
| 20B(5) | subsection | 675 | non-operative | headings, introductory words of definitions, and notes only |
| 20B(5) definition: scheme’s accrued actuarial liabilities | definition | 676 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 20B(5) definition: scheme’s accrued actuarial liabilities(a) | paragraph | 677 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 20B(5) definition: scheme’s accrued actuarial liabilities(b) | paragraph | 678-679 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 20B(5) definition: scheme’s liabilities in respect of vested benefits | definition | 680 | defined term | `sga-defs.l4` a definition kept as a defined-term record; no rule applies it directly |
| 20C | section | 681 | non-operative | headings, introductory words of definitions, and notes only |
| 20C(1) | subsection | 682 | encoded | `sga-part3b.l4` |
| 20C(2) | subsection | 683 | encoded | `sga-part3b.l4` |
| 20C(2)(a) | paragraph | 684 | encoded | `sga-part3b.l4` |
| 20C(2)(b) | paragraph | 685 | encoded | `sga-part3b.l4` |
| 20C(3) | subsection | 686 | encoded | `sga-time.l4` |
| 20C(3) definition: notice period | definition | 687 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 20C(3) definition: notice period(a) | paragraph | 688-691 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 20C(3) definition: notice period(b) | paragraph | 692 | encoded | `sga-defs.l4`, `sga-time.l4` |
| 20D | section | 693-694 | encoded | `sga-part3b.l4` |
| 20D(a) | paragraph | 695 | encoded | `sga-part3b.l4` |
| 20D(b) | paragraph | 696 | encoded | `sga-part3b.l4` |
| 20D(c) | paragraph | 697-700 | encoded | `sga-part3b.l4` |
| 20D(d) | paragraph | 701 | encoded | `sga-part3b.l4` |
| 20D(e) | paragraph | 702 | encoded | `sga-part3b.l4` |
| 30 | section | 703-705 | encoded | `sga-part3b.l4` |
| 30(a) | paragraph | 706 | encoded | `sga-part3b.l4` |
| 30(b) | paragraph | 707 | encoded | `sga-part3b.l4` |
| 30(c) | paragraph | 708-709 | encoded | `sga-part3b.l4` |
| 32A | section | 710-713 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 32B | section | 714-718 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 32B item Division 1 | item | 719-720 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 2 | item | 721-722 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 3 | item | 723-724 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 4 | item | 725-726 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 6 | item | 727-728 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 7 | item | 729-730 | non-operative | headings, introductory words of definitions, and notes only |
| 32B item Division 8 | item | 731-732 | non-operative | headings, introductory words of definitions, and notes only |
| 32C | section | 733-735 | non-operative | headings, introductory words of definitions, and notes only |
| 32C(1) | subsection | 736 | encoded | `sga-choice-of-fund.l4` |
| 32C(1)(a) | paragraph | 737 | encoded | `sga-choice-of-fund.l4` |
| 32C(1)(b) | paragraph | 738-739 | encoded | `sga-choice-of-fund.l4` |
| 32C(1A) | subsection | 740 | encoded | `sga-choice-of-fund.l4` |
| 32C(1A)(a) | paragraph | 741 | encoded | `sga-choice-of-fund.l4` |
| 32C(1A)(b) | paragraph | 742-745 | encoded | `sga-choice-of-fund.l4` |
| 32C(1B) | subsection | 746 | encoded | `sga-choice-of-fund.l4` |
| 32C(1B)(a) | paragraph | 747 | encoded | `sga-choice-of-fund.l4` |
| 32C(1B)(b) | paragraph | 748-750 | encoded | `sga-choice-of-fund.l4` |
| 32C(2) | subsection | 751 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(a) | paragraph | 752 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(aa) | paragraph | 753-756 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(b) | paragraph | 757 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(ba) | paragraph | 758-760 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(c) | paragraph | 761 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(d) | paragraph | 762 | encoded | `sga-choice-of-fund.l4` |
| 32C(2)(e) | paragraph | 763 | encoded | `sga-choice-of-fund.l4` |
| 32C(2A) | subsection | 764 | encoded | `sga-choice-of-fund.l4` |
| 32C(2A)(a) | paragraph | 765 | encoded | `sga-choice-of-fund.l4` |
| 32C(2A)(b) | paragraph | 766-767 | encoded | `sga-choice-of-fund.l4` |
| 32C(2AA) | subsection | 768-769 | encoded | `sga-choice-of-fund.l4` |
| 32C(2AB) | subsection | 770 | encoded | `sga-choice-of-fund.l4` |
| 32C(2AB)(a) | paragraph | 771 | encoded | `sga-choice-of-fund.l4` |
| 32C(2AB)(b) | paragraph | 772-775 | encoded | `sga-choice-of-fund.l4` |
| 32C(2AB)(c) | paragraph | 776-777 | encoded | `sga-choice-of-fund.l4` |
| 32C(3) | subsection | 778-779 | encoded | `sga-choice-of-fund.l4` |
| 32C(4) | subsection | 780-781 | encoded | `sga-choice-of-fund.l4` |
| 32C(5) | subsection | 782-783 | encoded | `sga-choice-of-fund.l4` |
| 32C(6) | subsection | 784 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(a) | paragraph | 785 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(b) | paragraph | 786 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(c) | paragraph | 787 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(d) | paragraph | 788 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(e) | paragraph | 789 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(f) | paragraph | 790 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(g) | paragraph | 791 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32C(6)(h) | paragraph | 792 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32C(6)(i) | paragraph | 793 | encoded | `sga-choice-of-fund.l4` |
| 32C(6)(j) | paragraph | 794-795 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AAA) | subsection | 796 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AAA)(a) | paragraph | 797 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AAA)(b) | paragraph | 798-800 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AA) | subsection | 801 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AA)(a) | paragraph | 802 | encoded | `sga-choice-of-fund.l4` |
| 32C(6AA)(b) | paragraph | 803-804 | encoded | `sga-choice-of-fund.l4` |
| 32C(6A) | subsection | 805 | encoded | `sga-choice-of-fund.l4` |
| 32C(6A)(a) | paragraph | 806 | encoded | `sga-choice-of-fund.l4` |
| 32C(6A)(b) | paragraph | 807-809 | encoded | `sga-choice-of-fund.l4` |
| 32C(6B) | subsection | 810-812 | encoded | `sga-choice-of-fund.l4` |
| 32C(7) | subsection | 813-815 | encoded | `sga-choice-of-fund.l4` |
| 32C(8) | subsection | 816-817 | encoded | `sga-choice-of-fund.l4` |
| 32C(9) | subsection | 818-819 | encoded | `sga-choice-of-fund.l4` |
| 32C(10) | subsection | 820 | encoded | `sga-choice-of-fund.l4` |
| 32C(10)(a) | paragraph | 821 | encoded | `sga-choice-of-fund.l4` |
| 32C(10)(b) | paragraph | 822-823 | encoded | `sga-choice-of-fund.l4` |
| 32CA | section | 824-825 | encoded | `sga-choice-of-fund.l4` |
| 32D | section | 826-828 | encoded | `sga-choice-of-fund.l4` |
| 32D(a) | paragraph | 829 | encoded | `sga-choice-of-fund.l4` |
| 32D(b) | paragraph | 830 | encoded | `sga-choice-of-fund.l4` |
| 32D(c) | paragraph | 831 | encoded | `sga-choice-of-fund.l4` |
| 32D(ca) | paragraph | 832 | encoded | `sga-choice-of-fund.l4` |
| 32D(d) | paragraph | 833 | encoded | `sga-choice-of-fund.l4` |
| 32D(e) | paragraph | 834 | encoded | `sga-choice-of-fund.l4` |
| 32E | section | 835 | non-operative | headings, introductory words of definitions, and notes only |
| 32E(1) | subsection | 836 | encoded | `sga-choice-of-fund.l4` |
| 32E(1) definition: fund | definition | 837 | encoded | `sga-choice-of-fund.l4`, `sga-defs.l4` |
| 32E(1) definition: fund(a) | paragraph | 838 | encoded | `sga-choice-of-fund.l4`, `sga-defs.l4` |
| 32E(1) definition: fund(b) | paragraph | 839 | encoded | `sga-choice-of-fund.l4`, `sga-defs.l4` |
| 32E(1) definition: fund(c) | paragraph | 840-841 | encoded | `sga-choice-of-fund.l4`, `sga-defs.l4`, `sga-time.l4` |
| 32E(2) | subsection | 842 | encoded | `sga-choice-of-fund.l4` |
| 32F | section | 843-844 | non-operative | headings, introductory words of definitions, and notes only |
| 32F(1) | subsection | 845 | encoded | `sga-choice-of-fund.l4` |
| 32F(1)(a) | paragraph | 846 | encoded | `sga-choice-of-fund.l4` |
| 32F(1)(b) | paragraph | 847-848 | encoded | `sga-choice-of-fund.l4` |
| 32F(1A) | subsection | 849 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(1A)(a) | paragraph | 850 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(1A)(b) | paragraph | 851 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(1A)(c) | paragraph | 852-853 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(1A)(d) | paragraph | 854 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(1A)(e) | paragraph | 855-856 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32F(2) | subsection | 857 | encoded | `sga-time.l4` |
| 32F(3) | subsection | 858 | encoded | `sga-choice-of-fund.l4` |
| 32F(3)(a) | paragraph | 859 | encoded | `sga-choice-of-fund.l4` |
| 32F(3)(b) | paragraph | 860 | encoded | `sga-choice-of-fund.l4` |
| 32FA | section | 861 | non-operative | headings, introductory words of definitions, and notes only |
| 32FA(1) | subsection | 862 | encoded | `sga-choice-of-fund.l4` |
| 32FA(1)(a) | paragraph | 863-865 | encoded | `sga-choice-of-fund.l4` |
| 32FA(1)(b) | paragraph | 866 | encoded | `sga-choice-of-fund.l4` |
| 32FA(2) | subsection | 867 | encoded | `sga-choice-of-fund.l4` |
| 32G | section | 868 | non-operative | headings, introductory words of definitions, and notes only |
| 32G(1) | subsection | 869 | encoded | `sga-choice-of-fund.l4` |
| 32G(2) | subsection | 870 | encoded | `sga-choice-of-fund.l4` |
| 32H | section | 871 | non-operative | headings, introductory words of definitions, and notes only |
| 32H(1) | subsection | 872 | encoded | `sga-choice-of-fund.l4` |
| 32H(1)(a) | paragraph | 873 | encoded | `sga-choice-of-fund.l4` |
| 32H(1)(b) | paragraph | 874 | encoded | `sga-choice-of-fund.l4` |
| 32H(1A) | subsection | 875 | encoded | `sga-choice-of-fund.l4` |
| 32H(2) | subsection | 876 | encoded | `sga-choice-of-fund.l4` |
| 32H(3) | subsection | 877-878 | encoded | `sga-choice-of-fund.l4` |
| 32H(4) | subsection | 879 | encoded | `sga-choice-of-fund.l4` |
| 32J | section | 880-881 | encoded | `sga-choice-of-fund.l4` |
| 32J(a) | paragraph | 882 | encoded | `sga-choice-of-fund.l4` |
| 32J(b) | paragraph | 883 | encoded | `sga-choice-of-fund.l4` |
| 32J(c) | paragraph | 884 | encoded | `sga-choice-of-fund.l4` |
| 32J(d) | paragraph | 885-888 | encoded | `sga-choice-of-fund.l4` |
| 32N | section | 889-890 | non-operative | headings, introductory words of definitions, and notes only |
| 32N(1) | subsection | 891-892 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32N(2) | subsection | 893 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32N(3) | subsection | 894 | encoded | `sga-choice-of-fund.l4`, `sga-time.l4` |
| 32N(4) | subsection | 895 | encoded | `sga-choice-of-fund.l4` |
| 32N(4)(a) | paragraph | 896 | encoded | `sga-choice-of-fund.l4` |
| 32N(4)(b) | paragraph | 897 | encoded | `sga-choice-of-fund.l4` |
| 32N(5) | subsection | 898 | encoded | `sga-choice-of-fund.l4` |
| 32N(5)(a) | paragraph | 899 | encoded | `sga-choice-of-fund.l4` |
| 32N(5)(b) | paragraph | 900-901 | encoded | `sga-choice-of-fund.l4` |
| 32N(5A) | subsection | 902 | encoded | `sga-choice-of-fund.l4` |
| 32N(5A)(a) | paragraph | 903 | encoded | `sga-choice-of-fund.l4` |
| 32N(5A)(b) | paragraph | 904-905 | encoded | `sga-choice-of-fund.l4` |
| 32N(6) | subsection | 906 | encoded | `sga-choice-of-fund.l4` |
| 32NA | section | 907 | non-operative | headings, introductory words of definitions, and notes only |
| 32NA(1) | subsection | 908 | encoded | `sga-choice-of-fund.l4` |
| 32NA(2) | subsection | 909 | encoded | `sga-choice-of-fund.l4` |
| 32NA(2)(a) | paragraph | 910 | encoded | `sga-choice-of-fund.l4` |
| 32NA(2)(b) | paragraph | 911 | encoded | `sga-choice-of-fund.l4` |
| 32NA(3) | subsection | 912 | encoded | `sga-choice-of-fund.l4` |
| 32NA(3)(a) | paragraph | 913 | encoded | `sga-choice-of-fund.l4` |
| 32NA(3)(b) | paragraph | 914 | encoded | `sga-choice-of-fund.l4` |
| 32NA(4) | subsection | 915 | encoded | `sga-choice-of-fund.l4` |
| 32NA(4)(a) | paragraph | 916 | encoded | `sga-choice-of-fund.l4` |
| 32NA(4)(b) | paragraph | 917 | encoded | `sga-choice-of-fund.l4` |
| 32NA(5) | subsection | 918 | encoded | `sga-choice-of-fund.l4` |
| 32NA(6) | subsection | 919 | encoded | `sga-choice-of-fund.l4` |
| 32NA(6)(a) | paragraph | 920 | encoded | `sga-choice-of-fund.l4` |
| 32NA(6)(b) | paragraph | 921 | encoded | `sga-choice-of-fund.l4` |
| 32NA(7) | subsection | 922 | encoded | `sga-choice-of-fund.l4` |
| 32NA(7)(a) | paragraph | 923 | encoded | `sga-choice-of-fund.l4` |
| 32NA(7)(b) | paragraph | 924 | encoded | `sga-choice-of-fund.l4` |
| 32NA(8) | subsection | 925 | encoded | `sga-choice-of-fund.l4` |
| 32NA(8)(a) | paragraph | 926 | encoded | `sga-choice-of-fund.l4` |
| 32NA(8)(b) | paragraph | 927 | encoded | `sga-choice-of-fund.l4` |
| 32NA(9) | subsection | 928 | encoded | `sga-choice-of-fund.l4` |
| 32NA(9)(a) | paragraph | 929 | encoded | `sga-choice-of-fund.l4` |
| 32NA(9)(b) | paragraph | 930 | encoded | `sga-choice-of-fund.l4` |
| 32NA(10) | subsection | 931 | encoded | `sga-choice-of-fund.l4` |
| 32NA(10)(a) | paragraph | 932 | encoded | `sga-choice-of-fund.l4` |
| 32NA(10)(b) | paragraph | 933 | encoded | `sga-choice-of-fund.l4` |
| 32NA(10)(c) | paragraph | 934 | encoded | `sga-choice-of-fund.l4` |
| 32NA(11) | subsection | 935 | encoded | `sga-choice-of-fund.l4` |
| 32P | section | 936 | non-operative | headings, introductory words of definitions, and notes only |
| 32P(1) | subsection | 937 | encoded | `sga-choice-of-fund.l4` |
| 32P(1)(a) | paragraph | 938 | encoded | `sga-choice-of-fund.l4` |
| 32P(1)(c) | paragraph | 939 | encoded | `sga-choice-of-fund.l4` |
| 32P(1)(e) | paragraph | 940 | encoded | `sga-choice-of-fund.l4` |
| 32P(1)(g) | paragraph | 941 | encoded | `sga-choice-of-fund.l4` |
| 32P(2) | subsection | 942 | encoded | `sga-choice-of-fund.l4` |
| 32Q | section | 943-945 | encoded | `sga-choice-of-fund.l4` |
| 32R | section | 946-947 | non-operative | headings, introductory words of definitions, and notes only |
| 32R(1) | subsection | 948 | encoded | `sga-choice-of-fund.l4` |
| 32R(1)(a) | paragraph | 949 | encoded | `sga-choice-of-fund.l4` |
| 32R(1)(b) | paragraph | 950 | encoded | `sga-choice-of-fund.l4` |
| 32R(1A) | subsection | 951-952 | encoded | `sga-choice-of-fund.l4` |
| 32R(2) | subsection | 953 | encoded | `sga-choice-of-fund.l4` |
| 32R(2)(a) | paragraph | 954 | encoded | `sga-choice-of-fund.l4` |
| 32R(2)(b) | paragraph | 955-959 | encoded | `sga-choice-of-fund.l4` |
| 32R(3) | subsection | 960 | encoded | `sga-choice-of-fund.l4` |
| 32R(3)(a) | paragraph | 961 | encoded | `sga-choice-of-fund.l4` |
| 32R(3)(b) | paragraph | 962 | encoded | `sga-choice-of-fund.l4` |
| 32W | section | 963-965 | encoded | `sga-choice-of-fund.l4` |
| 32W(a) | paragraph | 966 | encoded | `sga-choice-of-fund.l4` |
| 32W(b) | paragraph | 967 | encoded | `sga-choice-of-fund.l4` |
| 32X | section | 968-969 | encoded | `sga-choice-of-fund.l4` |
| 32Z | section | 970-971 | encoded | `sga-choice-of-fund.l4` |
| 32Z(a) | paragraph | 972 | encoded | `sga-choice-of-fund.l4` |
| 32Z(b) | paragraph | 973 | encoded | `sga-choice-of-fund.l4` |
| 32Z(c) | paragraph | 974 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA | section | 975 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA(1) | subsection | 976 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA(2) | subsection | 977 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA(2)(a) | paragraph | 978 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA(2)(b) | paragraph | 979 | encoded | `sga-choice-of-fund.l4` |
| 32ZAA(2)(c) | paragraph | 980 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB | section | 981 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(1) | subsection | 982 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(1)(a) | paragraph | 983 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(1)(b) | paragraph | 984-987 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(2) | subsection | 988 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(2)(a) | paragraph | 989 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(2)(b) | paragraph | 990 | encoded | `sga-choice-of-fund.l4` |
| 32ZAB(2)(c) | paragraph | 991-993 | encoded | `sga-choice-of-fund.l4` |
| 32ZA | section | 994-995 | encoded | `sga-choice-of-fund.l4` |
| 33 | section | 996-997 | non-operative | headings, introductory words of definitions, and notes only |
| 33(1) | subsection | 998 | encoded | `sga-part4-6.l4` |
| 33(2) | subsection | 999 | encoded | `sga-part4-6.l4` |
| 33(2)(a) | paragraph | 1000 | encoded | `sga-part4-6.l4`, `sga-time.l4` |
| 33(2)(b) | paragraph | 1001-1002 | encoded | `sga-part4-6.l4` |
| 33(3) | subsection | 1003 | encoded | `sga-part4-6.l4` |
| 33(3)(a) | paragraph | 1004 | encoded | `sga-part4-6.l4` |
| 33(3)(b) | paragraph | 1005-1007 | encoded | `sga-part4-6.l4` |
| 33(4) | subsection | 1008 | encoded | `sga-part4-6.l4` |
| 33(4) definition: account | definition | 1009 | encoded | `sga-defs.l4`, `sga-part4-6.l4` |
| 36 | section | 1010-1011 | non-operative | headings, introductory words of definitions, and notes only |
| 36(1) | subsection | 1012 | encoded | `sga-part4-6.l4` |
| 36(1)(a) | paragraph | 1013 | encoded | `sga-part4-6.l4` |
| 36(1)(b) | paragraph | 1014 | encoded | `sga-part4-6.l4` |
| 36(2) | subsection | 1015 | encoded | `sga-part4-6.l4` |
| 36(2)(a) | paragraph | 1016 | encoded | `sga-part4-6.l4` |
| 36(2)(b) | paragraph | 1017-1018 | encoded | `sga-part4-6.l4` |
| 36(3) | subsection | 1019 | encoded | `sga-time.l4` |
| 36(3)(a) | paragraph | 1020-1022 | encoded | `sga-time.l4` |
| 36(3)(b) | paragraph | 1023-1026 | encoded | `sga-time.l4` |
| 36(4) | subsection | 1027 | encoded | `sga-part4-6.l4` |
| 37 | section | 1028 | non-operative | headings, introductory words of definitions, and notes only |
| 37(1) | subsection | 1029 | encoded | `sga-part4-6.l4` |
| 37(2) | subsection | 1030 | encoded | `sga-part4-6.l4` |
| 37(2)(a) | paragraph | 1031 | encoded | `sga-part4-6.l4` |
| 37(2)(b) | paragraph | 1032-1033 | encoded | `sga-part4-6.l4`, `sga-time.l4` |
| 37(3) | subsection | 1034 | encoded | `sga-part4-6.l4` |
| 37(4) | subsection | 1035 | encoded | `sga-part4-6.l4` |
| 37(5) | subsection | 1036 | encoded | `sga-part4-6.l4` |
| 37(5)(a) | paragraph | 1037 | encoded | `sga-part4-6.l4` |
| 37(5)(b) | paragraph | 1038-1039 | encoded | `sga-part4-6.l4` |
| 37(6) | subsection | 1040 | encoded | `sga-part4-6.l4` |
| 37(6)(a) | paragraph | 1041 | encoded | `sga-part4-6.l4` |
| 37(6)(b) | paragraph | 1042 | encoded | `sga-part4-6.l4` |
| 37(7) | subsection | 1043 | encoded | `sga-part4-6.l4` |
| 38 | section | 1044 | non-operative | headings, introductory words of definitions, and notes only |
| 38(1) | subsection | 1045 | encoded | `sga-part4-6.l4` |
| 38(1)(a) | paragraph | 1046 | encoded | `sga-part4-6.l4` |
| 38(1)(b) | paragraph | 1047-1049 | encoded | `sga-part4-6.l4` |
| 38(2) | subsection | 1050-1051 | encoded | `sga-part4-6.l4` |
| 38(2)(a) | paragraph | 1052 | encoded | `sga-part4-6.l4` |
| 38(2)(b) | paragraph | 1053 | encoded | `sga-part4-6.l4` |
| 38(2)(c) | paragraph | 1054 | encoded | `sga-part4-6.l4` |
| 39 | section | 1055-1056 | encoded | `sga-part4-6.l4` |
| 40 | section | 1057-1058 | encoded | `sga-part4-6.l4` |
| 41 | section | 1059-1060 | encoded | `sga-part4-6.l4` |
| 42 | section | 1061-1062 | encoded | `sga-part4-6.l4` |
| 43 | section | 1063-1066 | encoded | `sga-part4-6.l4` |
| 44 | section | 1067-1068 | encoded | `sga-part4-6.l4` |
| 49 | section | 1069-1070 | non-operative | headings, introductory words of definitions, and notes only |
| 49(1) | subsection | 1071-1072 | encoded | `sga-part4-6.l4` |
| 49(3) | subsection | 1073 | encoded | `sga-part4-6.l4`, `sga-time.l4` |
| 49(3)(a) | paragraph | 1074 | encoded | `sga-part4-6.l4`, `sga-time.l4` |
| 49(3)(b) | paragraph | 1075-1077 | encoded | `sga-part4-6.l4`, `sga-time.l4` |
| 49(4) | subsection | 1078 | encoded | `sga-part4-6.l4` |
| 57 | section | 1079 | non-operative | headings, introductory words of definitions, and notes only |
| 57(1) | subsection | 1080 | encoded | `sga-part4-6.l4` |
| 57(2) | subsection | 1081-1082 | encoded | `sga-part4-6.l4` |
| 57(3) | subsection | 1083 | encoded | `sga-part4-6.l4` |
| 57(4) | subsection | 1084 | encoded | `sga-part4-6.l4` |
| 57(5) | subsection | 1085 | encoded | `sga-part4-6.l4` |
| 57(6) | subsection | 1086 | encoded | `sga-part4-6.l4` |
| 57A | section | 1087-1088 | encoded | `sga-part4-6.l4` |
| 57A(a) | paragraph | 1089 | encoded | `sga-part4-6.l4` |
| 57A(b) | paragraph | 1090-1091 | encoded | `sga-part4-6.l4` |
| 58 | section | 1092 | non-operative | headings, introductory words of definitions, and notes only |
| 58(1) | subsection | 1093 | encoded | `sga-part4-6.l4` |
| 58(2) | subsection | 1094 | encoded | `sga-part4-6.l4` |
| 58(3) | subsection | 1095 | encoded | `sga-part4-6.l4` |
| 58(4) | subsection | 1096 | encoded | `sga-part4-6.l4` |
| 58(5) | subsection | 1097 | encoded | `sga-part4-6.l4` |
| 58(6) | subsection | 1098 | encoded | `sga-part4-6.l4` |
| 58(7) | subsection | 1099 | encoded | `sga-part4-6.l4` |
| 59 | section | 1100-1103 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 59A | section | 1104 | non-operative | headings, introductory words of definitions, and notes only |
| 59A(1) | subsection | 1105-1106 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59A(1) Note(a) | paragraph | 1107 | encoded | `sga-part7.l4` |
| 59A(1) Note(b) | paragraph | 1108 | encoded | `sga-part7.l4` |
| 59A(2) | subsection | 1109 | encoded | `sga-part7.l4` |
| 59A(2)(a) | paragraph | 1110 | encoded | `sga-part7.l4` |
| 59A(2)(b) | paragraph | 1111 | encoded | `sga-part7.l4` |
| 59A(2)(c) | paragraph | 1112 | encoded | `sga-part7.l4` |
| 59A(2)(d) | paragraph | 1113 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59A(2)(e) | paragraph | 1114-1115 | encoded | `sga-part7.l4` |
| 59A(2) Note 1(a) | paragraph | 1116 | encoded | `sga-part7.l4` |
| 59A(2) Note 1(b) | paragraph | 1117-1118 | encoded | `sga-part7.l4` |
| 59A(3) | subsection | 1119 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59A(3)(a) | paragraph | 1120 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59A(3)(b) | paragraph | 1121 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59B | section | 1122 | non-operative | headings, introductory words of definitions, and notes only |
| 59B(1) | subsection | 1123 | encoded | `sga-part7.l4` |
| 59B(1)(a) | paragraph | 1124 | encoded | `sga-part7.l4` |
| 59B(1)(b) | paragraph | 1125-1126 | encoded | `sga-part7.l4` |
| 59B(2) | subsection | 1127 | encoded | `sga-part7.l4` |
| 59B(2)(a) | paragraph | 1128 | encoded | `sga-part7.l4` |
| 59B(2)(b) | paragraph | 1129-1132 | encoded | `sga-part7.l4` |
| 59C | section | 1133 | non-operative | headings, introductory words of definitions, and notes only |
| 59C(1) | subsection | 1134 | encoded | `sga-part7.l4` |
| 59C(2) | subsection | 1135-1139 | encoded | `sga-part7.l4` |
| 59C(2) item 1 | item | 1140-1144 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59C(2) item 2 | item | 1145-1148 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59C(2) item 3 | item | 1149-1152 | encoded | `sga-part7.l4` |
| 59D | section | 1153 | non-operative | headings, introductory words of definitions, and notes only |
| 59D(1) | subsection | 1154 | encoded | `sga-part7.l4` |
| 59D(2) | subsection | 1155 | encoded | `sga-part7.l4` |
| 59D(3) | subsection | 1156-1158 | encoded | `sga-part7.l4`, `sga-time.l4` |
| 59D(4) | subsection | 1159 | encoded | `sga-part7.l4` |
| 59E | section | 1160 | non-operative | headings, introductory words of definitions, and notes only |
| 59E(1) | subsection | 1161 | encoded | `sga-part7.l4` |
| 59E(2) | subsection | 1162 | encoded | `sga-part7.l4` |
| 59E(2)(a) | paragraph | 1163 | encoded | `sga-part7.l4` |
| 59E(2)(b) | paragraph | 1164-1165 | encoded | `sga-part7.l4` |
| 59E(3) | subsection | 1166 | encoded | `sga-part7.l4` |
| 63A | section | 1167-1168 | non-operative | headings, introductory words of definitions, and notes only |
| 63A(1) | subsection | 1169 | encoded | `sga-parts8-9.l4` |
| 63A(1A) | subsection | 1170 | encoded | `sga-parts8-9.l4` |
| 63A(2) | subsection | 1171 | encoded | `sga-parts8-9.l4` |
| 63A(2) definition: charge payment | definition | 1172 | encoded | `sga-defs.l4`, `sga-parts8-9.l4` |
| 63A(2) definition: charge payment(a) | paragraph | 1173 | encoded | `sga-defs.l4`, `sga-parts8-9.l4` |
| 63A(2) definition: charge payment(b) | paragraph | 1174-1175 | encoded | `sga-defs.l4`, `sga-parts8-9.l4` |
| 63A(3) | subsection | 1176 | encoded | `sga-parts8-9.l4` |
| 63A(3)(a) | paragraph | 1177 | encoded | `sga-parts8-9.l4` |
| 63A(3)(b) | paragraph | 1178-1180 | encoded | `sga-parts8-9.l4` |
| 63A(4) | subsection | 1181 | encoded | `sga-parts8-9.l4` |
| 63B | section | 1182 | non-operative | headings, introductory words of definitions, and notes only |
| 63B(1) | subsection | 1183 | encoded | `sga-parts8-9.l4` |
| 63B(2) | subsection | 1184 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 63B(3) | subsection | 1185 | outline | simplified outline, purpose, structure or overview: states no rule of its own; the rules it summarises are encoded at their own sections |
| 64A | section | 1186 | non-operative | headings, introductory words of definitions, and notes only |
| 64A(1) | subsection | 1187 | encoded | `sga-parts8-9.l4` |
| 64A(2) | subsection | 1188 | encoded | `sga-parts8-9.l4` |
| 64A(2)(a) | paragraph | 1189 | encoded | `sga-parts8-9.l4` |
| 64A(2)(b) | paragraph | 1190 | encoded | `sga-parts8-9.l4` |
| 64A(3) | subsection | 1191 | encoded | `sga-parts8-9.l4` |
| 64A(3)(a) | paragraph | 1192 | encoded | `sga-parts8-9.l4` |
| 64A(3)(b) | paragraph | 1193 | encoded | `sga-parts8-9.l4` |
| 64A(3)(c) | paragraph | 1194 | encoded | `sga-parts8-9.l4` |
| 64A(3)(d) | paragraph | 1195-1199 | encoded | `sga-parts8-9.l4` |
| 64B | section | 1200 | non-operative | headings, introductory words of definitions, and notes only |
| 64B(1) | subsection | 1201 | encoded | `sga-parts8-9.l4` |
| 64B(2) | subsection | 1202 | encoded | `sga-parts8-9.l4` |
| 64B(2)(a) | paragraph | 1203 | encoded | `sga-parts8-9.l4` |
| 64B(2)(b) | paragraph | 1204 | encoded | `sga-parts8-9.l4` |
| 64B(3) | subsection | 1205 | encoded | `sga-parts8-9.l4` |
| 64B(3A) | subsection | 1206 | encoded | `sga-parts8-9.l4` |
| 64B(3A)(a) | paragraph | 1207 | encoded | `sga-parts8-9.l4` |
| 64B(3A)(b) | paragraph | 1208 | encoded | `sga-parts8-9.l4` |
| 64B(4) | subsection | 1209 | encoded | `sga-parts8-9.l4` |
| 64B(4)(a) | paragraph | 1210 | encoded | `sga-parts8-9.l4` |
| 64B(4)(b) | paragraph | 1211 | encoded | `sga-parts8-9.l4` |
| 64B(4)(c) | paragraph | 1212 | encoded | `sga-parts8-9.l4` |
| 64B(4)(d) | paragraph | 1213-1217 | encoded | `sga-parts8-9.l4` |
| 65 | section | 1218 | non-operative | headings, introductory words of definitions, and notes only |
| 65(1) | subsection | 1219 | encoded | `sga-parts8-9.l4` |
| 65(1)(a) | paragraph | 1220-1224 | encoded | `sga-parts8-9.l4` |
| 65(1)(b) | paragraph | 1225-1227 | encoded | `sga-parts8-9.l4` |
| 65(1)(c) | paragraph | 1228 | encoded | `sga-parts8-9.l4` |
| 65(2) | subsection | 1229 | encoded | `sga-parts8-9.l4` |
| 65(2)(a) | paragraph | 1230 | encoded | `sga-parts8-9.l4` |
| 65(2)(b) | paragraph | 1231 | encoded | `sga-parts8-9.l4` |
| 65(3) | subsection | 1232 | encoded | `sga-parts8-9.l4` |
| 65(4) | subsection | 1233 | encoded | `sga-parts8-9.l4` |
| 65(5) | subsection | 1234 | encoded | `sga-parts8-9.l4` |
| 65(6) | subsection | 1235 | encoded | `sga-parts8-9.l4` |
| 65AA | section | 1236 | encoded | `sga-parts8-9.l4` |
| 65AA(1) | subsection | 1237 | encoded | `sga-parts8-9.l4` |
| 65AA(2) | subsection | 1238 | encoded | `sga-parts8-9.l4` |
| 65A | section | 1239-1240 | encoded | `sga-parts8-9.l4` |
| 65A(a) | paragraph | 1241 | encoded | `sga-parts8-9.l4` |
| 65A(b) | paragraph | 1242 | encoded | `sga-parts8-9.l4` |
| 66 | section | 1243-1244 | encoded | `sga-parts8-9.l4` |
| 66(a) | paragraph | 1245 | encoded | `sga-parts8-9.l4` |
| 66(b) | paragraph | 1246-1249 | encoded | `sga-parts8-9.l4` |
| 66A | section | 1250-1251 | encoded | `sga-parts8-9.l4` |
| 66A(a) | paragraph | 1252 | encoded | `sga-parts8-9.l4` |
| 66A(b) | paragraph | 1253 | encoded | `sga-parts8-9.l4` |
| 67 | section | 1254-1255 | encoded | `sga-parts8-9.l4` |
| 69 | section | 1256 | non-operative | headings, introductory words of definitions, and notes only |
| 69(1) | subsection | 1257 | encoded | `sga-parts8-9.l4` |
| 69(2) | subsection | 1258 | encoded | `sga-parts8-9.l4` |
| 69(3) | subsection | 1259 | encoded | `sga-parts8-9.l4` |
| 69(3)(a) | paragraph | 1260 | encoded | `sga-parts8-9.l4` |
| 69(3)(b) | paragraph | 1261-1264 | encoded | `sga-parts8-9.l4` |
| 69(3)(c) | paragraph | 1265-1269 | encoded | `sga-parts8-9.l4` |
| 69(4) | subsection | 1270 | encoded | `sga-parts8-9.l4` |
| 69(4)(a) | paragraph | 1271 | encoded | `sga-parts8-9.l4` |
| 69(4)(b) | paragraph | 1272 | encoded | `sga-parts8-9.l4`, `sga-time.l4` |
| 69(4)(c) | paragraph | 1273 | encoded | `sga-parts8-9.l4` |
| 69(5) | subsection | 1274 | encoded | `sga-parts8-9.l4` |
| 69(5)(a) | paragraph | 1275 | encoded | `sga-parts8-9.l4` |
| 69(5)(b) | paragraph | 1276-1277 | encoded | `sga-parts8-9.l4` |
| 69(6) | subsection | 1278 | encoded | `sga-parts8-9.l4` |
| 69(7) | subsection | 1279 | encoded | `sga-parts8-9.l4` |
| 69(8) | subsection | 1280 | encoded | `sga-parts8-9.l4` |
| 69A | section | 1281 | non-operative | headings, introductory words of definitions, and notes only |
| 69A(1) | subsection | 1282 | encoded | `sga-parts8-9.l4` |
| 69A(1)(a) | paragraph | 1283 | encoded | `sga-parts8-9.l4` |
| 69A(1)(b) | paragraph | 1284 | encoded | `sga-parts8-9.l4` |
| 69A(2) | subsection | 1285 | encoded | `sga-parts8-9.l4` |
| 69A(3) | subsection | 1286 | encoded | `sga-parts8-9.l4` |
| 71 | section | 1287-1288 | encoded | `sga-parts8-9.l4` |
| 72 | section | 1289-1290 | non-operative | headings, introductory words of definitions, and notes only |
| 72(1) | subsection | 1291 | encoded | `sga-parts8-9.l4` |
| 72(2) | subsection | 1292 | encoded | `sga-parts8-9.l4` |
| 72(3) | subsection | 1293 | encoded | `sga-parts8-9.l4` |
| 72(4) | subsection | 1294 | encoded | `sga-parts8-9.l4` |
| 72(5) | subsection | 1295 | encoded | `sga-parts8-9.l4` |
| 72(5)(a) | paragraph | 1296 | encoded | `sga-parts8-9.l4` |
| 72(5)(b) | paragraph | 1297 | encoded | `sga-parts8-9.l4` |
| 72(6) | subsection | 1298 | not encoded | extends "this Act" to Part III of the Taxation Administration Act 1953, which is not among the sources |
| 73 | section | 1299 | non-operative | headings, introductory words of definitions, and notes only |
| 73(1) | subsection | 1300 | encoded | `sga-parts8-9.l4` |
| 73(2) | subsection | 1301 | encoded | `sga-parts8-9.l4` |
| 73(3) | subsection | 1302 | encoded | `sga-parts8-9.l4` |
| 73(4) | subsection | 1303 | encoded | `sga-parts8-9.l4` |
| 73(5) | subsection | 1304 | encoded | `sga-parts8-9.l4` |
| 73(6) | subsection | 1305 | encoded | `sga-parts8-9.l4` |
| 73(6)(a) | paragraph | 1306 | encoded | `sga-parts8-9.l4` |
| 73(6)(b) | paragraph | 1307 | encoded | `sga-parts8-9.l4` |
| 73(7) | subsection | 1308 | not encoded | extends "this Act" to Part III of the Taxation Administration Act 1953, which is not among the sources |
| 74 | section | 1309-1310 | non-operative | headings, introductory words of definitions, and notes only |
| 74(1) | subsection | 1311 | encoded | `sga-parts8-9.l4` |
| 74(1)(a) | paragraph | 1312-1314 | encoded | `sga-parts8-9.l4` |
| 74(1)(b) | paragraph | 1315 | encoded | `sga-parts8-9.l4`, `sga-time.l4` |
| 74(1)(c) | paragraph | 1316 | encoded | `sga-parts8-9.l4` |
| 74(2) | subsection | 1317 | encoded | `sga-parts8-9.l4` |
| 74(3) | subsection | 1318 | encoded | `sga-time.l4` |
| 74(3)(a) | paragraph | 1319 | encoded | `sga-time.l4` |
| 74(3)(b) | paragraph | 1320-1321 | encoded | `sga-time.l4` |
| 74(4) | subsection | 1322 | encoded | `sga-parts8-9.l4` |
| 74(5) | subsection | 1323 | encoded | `sga-parts8-9.l4` |
| 74(5)(a) | paragraph | 1324-1326 | encoded | `sga-parts8-9.l4` |
| 74(5)(b) | paragraph | 1327 | encoded | `sga-parts8-9.l4` |
| 74(6) | subsection | 1328 | encoded | `sga-parts8-9.l4` |
| 79 | section | 1329 | non-operative | headings, introductory words of definitions, and notes only |
| 79(1) | subsection | 1330-1331 | encoded | `sga-parts8-9.l4` |
| 79(2) | subsection | 1332 | encoded | `sga-parts8-9.l4` |
| 79(2)(a) | paragraph | 1333 | encoded | `sga-parts8-9.l4` |
| 79(2)(b) | paragraph | 1334 | encoded | `sga-parts8-9.l4` |
| 79(3) | subsection | 1335 | encoded | `sga-parts8-9.l4` |
| 79(3)(a) | paragraph | 1336 | encoded | `sga-parts8-9.l4` |
| 79(3)(b) | paragraph | 1337 | encoded | `sga-parts8-9.l4` |
| 79(4) | subsection | 1338 | encoded | `sga-parts8-9.l4`, `sga-time.l4` |
| 79(5) | subsection | 1339 | encoded | `sga-parts8-9.l4` |
| 79(5)(a) | paragraph | 1340 | encoded | `sga-parts8-9.l4` |
| 79(5)(b) | paragraph | 1341-1342 | encoded | `sga-parts8-9.l4` |
| 79(6) | subsection | 1343-1344 | encoded | `sga-parts8-9.l4` |
| 79(6A) | subsection | 1345-1346 | encoded | `sga-parts8-9.l4` |
| 79(7) | subsection | 1347-1348 | encoded | `sga-parts8-9.l4` |
| 80 | section | 1349-1350 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 80(a) | paragraph | 1351 | machinery | power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
| 80(b) | paragraph | 1352-1353 | machinery | `sga-parts8-9.l4` power to make regulations; what the regulations provide is a plain input where a rule needs it (the 19B reduction; the penalty-unit limit in s 80 is encoded in sga-parts8-9.l4) |
