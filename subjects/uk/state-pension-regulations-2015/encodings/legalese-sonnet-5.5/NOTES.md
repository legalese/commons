# NOTES: the State Pension Regulations 2015 (S.I. 2015/173), encoding `legalese-sonnet-5.5`

Status: **draft** (`encoding.json` says the same): both layers are complete as a first pass and every check in "What check.sh prints" is green; nobody has reviewed it (see "What would need doing").
Method: a single Sonnet 5.5 agent working alone from BRIEF.md, with no ontology agent, fleet, integrator or independent test author.
Binary: the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
The source is `uksi-2015-173.txt`, **a plain-text rendering made by a converter script from legislation.gov.uk, version 2026-04-06; it is not the official text and it is not marked up.**
Nothing here is "verified against the official text".

## Seat

The seat is **a person who is, or will become, entitled to the State Pension, asking what these Regulations mean for when and how their State Pension is claimed, paid and affected by their choices** (BRIEF.md).
Why this seat: the Regulations are made under the Pensions Act 2014 and nearly every rule in them is something the pensioner does, is owed or is exposed to: choosing between a lump sum and a pension (regulations 4 to 6), suspending or deferring (7 to 12A), inheriting from a late spouse or civil partner (15 to 20), living abroad (21 to 23), and being credited for weeks of caring and the like (24 to 39).
The Secretary of State and HM Revenue and Customs are the other party of every one of those relations.
They have no seat; their side appears only as facts the person states (a notice has been issued, a direction to use writing has been given, a late choice is thought reasonable, a release date is certified, Regulations apply regulation 21).
The layer is `spr-seat.l4` (59 questions, each with `@export` and a plain-English `@desc` on every input) and `spr-cases-seat.l4` (one or more worked cases for every question; the count is in the check.sh table below).
It imports all ten layer-1 modules, builds the records they expect from plain answers inside each question's `WHERE`, and calls the module's own rule; no rule is restated and no layer-1 module changed for it.
The questions sit under ten `§` headings in the text's order; a heading whose group only arises in a situation the person may not be in (custody, an inherited deferred pension, suspending or deferring, a death, living abroad, a particular week) says so in its title, so a form can ask "has this happened to you?" before showing it.

| heading | questions |
| --- | --- |
| Do these Regulations apply to me, and how are people counted (Parts 1, 1A) | 3 |
| Prison and other custody (Part 2) | 1 |
| Choosing a lump sum or a state pension (regulations 4 to 6) | 6 |
| Suspending or deferring my State Pension (regulations 7 to 12A) | 8 |
| How many qualifying years I need (Part 4) | 2 |
| Sharing State Pension rights on divorce or dissolution (Part 5, Schedule) | 3 |
| A survivor's state pension from a late spouse's or civil partner's graduated retirement benefit (Part 6) | 13 |
| Living abroad (Part 7) | 6 |
| National Insurance credits that count towards my State Pension (Part 8) | 17 |

**Pairing.** Wherever the text gives the person a power (to choose, to alter, to suspend, to cancel, to elect) or a claim (to a credit, to information), the questions take the facts on the other side as plain inputs: the Secretary of State's notice and its date, a direction to use writing, whether a late choice or a longer period is thought reasonable, a certified release date, whether Regulations apply regulation 21, whether a declaration was requested, the day an application was received.
Where the text also puts a duty or a liability on the person, there is a paired question: what they owe in the way of giving a choice or a notice (regulations 5 and 7), applying in the right form and in time (28, 33 to 37, 39), repaying a lump sum (4(4), 6(2)(e)), and what can be done to them (withholding the pension while they are a prisoner, regulations 2 and 3).
Regulation 6(2)(a) asks whether the person who made the choice has since died, so the seat asks that too ("If you made the choice yourself and are asking for yourself, no").

**Placeholders.** A record field that the rule called never reads is given a fixed value with a comment saying so (59 of them).
They were checked mechanically, not by eye: for each placeholder the check was whether the field's name appears in the text of the called rule or of any rule it calls.
It does not, except one: in the question on credit for caring for a child under 12 the field `the person who decides considers it reasonable to allow further time` is read by the rule for regulation 39 only for applications under regulations 34, 36 and 37; for an application under regulation 35 (the only kind that question asks about) regulation 39(b) gives no further time and the branch that reads it is not taken.
The placeholder there is `FALSE`, with a comment.

**What the form cannot ask.** A list of dates is asked as one or two dates: the most recent notice that confirms the choice (regulation 4(2)), the first and second change in the weekly rate other than by up-rating (12A), the first and second person cared for (37).
The longer encoding in layer 1 takes any number.
The weekly rate of the deceased's graduated retirement benefit (regulation 16(5), questions on regulations 15 and 16), the lump sum under the 2005 Regulations (regulation 19), the lump sum and the pension paid so far (regulation 6), the weekly rates the person would have had if not deferred (regulations 10 and 22) and the lower earnings limit (regulations 30 to 32) are figures the text takes from other legislation or from the person's own record, so the seat asks for each as a number the person states (see Stated inputs below).
Two questions (the lump sum under regulation 19, and whether a state pension is payable under regulation 20) take as an input the answer to the question "What am I paid after my choice?", so that the seat does not rebuild the regulation 18 record twice.

**Figures taken as the text states them.** The full rate of the State Pension (241.30 pounds a week, regulation 1A, in the version of 6 April 2026), the one-ninth of 1 per cent of regulation 10, 6 April 2016 and the other dates and periods the text names.
The person cannot state these; if an amending instrument changes one, these answers change with it.

## Jural relations

One row per provision that creates a relation; a provision that creates none (a definition, a counting rule, a value) is listed once as `none`.
Layer 1 states each relation once, neutrally; the person in the seat is on one side of it and an official (the Secretary of State, or HM Revenue and Customs) on the other.
Hohfeld's correlatives: a claim (right) and a duty; a privilege (liberty) and a no-right; a power and a liability; an immunity and a disability.

| Provision | Holder of the right, privilege, power or immunity | Bearer of the correlative duty, no-right, liability or disability | Relation | L4 rule |
| --- | --- | --- | --- | --- |
| reg 1(2)-(4), 1A, 10-13, 24, 25(1), 26-27 (counting, values and definitions) | none | none | none | values and counting rules (see Part rows) |
| reg 1(3) | none (a gate: the Regulations other than Part 5 do not apply) | none | none | `whether Parts 1 to 4 and 6 to 8 apply to a person who reaches pensionable age on` |
| reg 1(5) | none (deeming: how a marriage is counted) | none | none | `the two people are treated as married to each other` |
| reg 2(1), 3(1) | Secretary of State: privilege not to pay for a day on which the person is a prisoner | the person: no-right to payment for that day | privilege / no-right (and, for a remand with no later sentence, the person's claim to payment stands and the Secretary of State's duty to pay with it) | `a state pension is not to be paid for the day`, `regulation 2(1) does not apply to the day because of regulation 3` |
| reg 2(2)-(4), 3(2)-(3) | none | none | none (definitions of who is a prisoner and what sentence counts) | `the person is a prisoner within regulation 2(2) on the day`, `the sentence is one described in regulation 3(2)` |
| reg 4(2)-(3) | the person: power to choose, within the period, a lump sum or a survivor's pension | Secretary of State: liability to pay what is chosen | power / liability | `where the choice falls against its period` |
| reg 4(4) | the person: power to make a late choice (but only where the Secretary of State considers it reasonable and any lump sum has been repaid) | Secretary of State: liability to accept it | power / liability, conditioned on the Secretary of State's judgment | `a late choice may be made` |
| reg 4(5) | Secretary of State: privilege not to pay the lump sum once a late choice for a state pension is made | the person: no-right to the lump sum | privilege / no-right | `the lump sum to be paid after a choice, the amount being` |
| reg 5(2) | the person: privilege to choose in writing or by telephone, to a place the Secretary of State has specified | Secretary of State: no-right that it be done another way | privilege / no-right | `it was given in a manner the Regulations allow` |
| reg 5(3), 7(3), 6(2)(d)(i) | Secretary of State: power to direct that the written manner be used | the person: liability to use writing | power / liability | `it was given in a manner the Regulations allow` |
| reg 6(1)-(2) | the person: power to alter a choice, once, in the circumstances (a) to (h) | Secretary of State: liability to the altered choice | power / liability | `the choice may be altered` |
| reg 6(3) | the person: claim to have the pension already paid counted against the lump sum | Secretary of State: duty to treat it as paid on account | claim / duty | `the part of the lump sum still to be paid, the lump sum being` |
| reg 7(1)-(3) | the person: power to suspend entitlement by notice | Secretary of State: liability to the suspension | power / liability | `entitlement is suspended by a notice` |
| reg 8 | the person: power to name the date, within 28 days starting with the day of the option | Secretary of State: liability to the date named | power / liability | `the date from which the suspension takes effect` |
| reg 9 | the person: power to cancel a suspension for a past period of up to 12 months, by claiming | Secretary of State: liability to the cancellation | power / liability | `the suspension is cancelled for the past period` |
| reg 13 | none | none | none | `the person has the minimum number of qualifying years for the reduced rate`, `... for the transitional rate` |
| Sch 1 > inserted reg 6(1), (2)-(6) | the person with shareable new state scheme rights (and, for the explanation, their spouse or civil partner): claim to the information on request | Secretary of State: duty to furnish it | claim / duty | `the information the person with shareable new state scheme rights is owed on request` |
| Sch 1 > inserted reg 6(7), (8) | the person (or spouse, or the court): claim that the information arrive by the day | Secretary of State: duty to furnish it by then | claim / duty | `the last day by which the Secretary of State must furnish the information` |
| reg 15 | the survivor: claim to the state pension under regulation 15 | Secretary of State: duty to pay it at the inherited rate | claim / duty | `a state pension is payable under regulation 15`, `the weekly rate of a state pension under regulation 15` |
| reg 16 | none | none | none (it fixes the amount and who qualifies for it) | `the paragraph of regulation 16 the survivor falls within`, `the inherited amount`, `the date for the inherited amount` |
| reg 17 | the survivor: claim to the up-rated pension | Secretary of State: duty to pay the increase at the time of the full-rate rise or uprating order | claim / duty | `the increase in the rate of the person's state pension` |
| reg 18(1)-(2) | the survivor: power to choose a lump sum or a state pension | Secretary of State: liability to pay what is chosen | power / liability | `the person is entitled to a choice under regulation 18`, `what is paid when the payment chosen is` |
| reg 18(3)-(5), (11) | Secretary of State: privilege to pay a lump sum where no valid choice was made within the period | the survivor: no-right to a state pension in that case | privilege / no-right | `what is paid under regulation 18` |
| reg 18(7) | the survivor: power to alter a choice once (regulation 6) | Secretary of State: liability to the altered choice | power / liability | `a choice under regulation 18 may be altered` |
| reg 19 | the survivor: claim to a lump sum calculated under the 2005 Regulations | Secretary of State: duty to pay it | claim / duty | `the lump sum payable under regulation 19` |
| reg 20 | the survivor: claim to a state pension under regulation 20 at half the deceased's increase, up-rated | Secretary of State: duty to pay it | claim / duty | `a state pension is payable under regulation 20`, `the weekly rate of a state pension under regulation 20` |
| reg 21 | Secretary of State: privilege not to pay an up-rating increase to an overseas resident (where Regulations apply regulation 21) | the person: no-right to the up-rating increase | privilege / no-right | `what regulation 21 does to an up-rating increase` |
| reg 22, 23 | none | none | none (they fix the amount of an increment) | `the increment under regulation 22, the weekly rate being`, `the increment under regulation 23, the weekly rate regulation 22 refers to being` |
| reg 24, 25(1), 25(3), 26-27, 29, 38(2) | none | none | none (definitions, gates and counting rules) | `a credit under Chapter 3 may be given for the week`, `the tax year a week falls in`, `the week falls in a year before 6 April 2016` |
| reg 25(2) | Secretary of State: privilege not to credit more than is needed to make the year a qualifying year | the person: no-right to more | privilege / no-right | `the amount the person is credited with` |
| reg 28, 30-38 (Class 3 contributions and earnings credited) | the person: claim to a credit for the week | Secretary of State, or HMRC: duty to give the credit | claim / duty | `a Class 3 contribution is credited under regulation 28`, `...regulation 30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38` |
| reg 28(5)-(6), 33(5)-(6), 34(2)(e), 35(3)(c), 35(5), 36(3), 37(5)-(6), 39 | Secretary of State, or HMRC: privilege to give no credit until an application in order and in time is received | the person: liability to apply in the form, with the content and by the time | privilege / liability | `the conditions for a forces spouse's credit are met`, `the application meets regulation 35(5)`, `the application meets regulation 37(6)`, `the application is received in time` |
| reg 35(4) | the persons who could be credited: power to elect, with the agreement of the other person, which of them is credited | the other persons who could be credited: liability to go without; Secretary of State: power (and so liability on the persons) to decide in default of agreement | power / liability | `who is credited where more than one person could be` |

## What is encoded and what is not

**Encoded (162 of the 200 provisions in the coverage table).**
Part 1 and 1A: the date the Regulations were made (9 February 2015) and the date they come into force (6 April 2016) as values with `@ref`; regulation 1(3) (who the Regulations reach), 1(5) (a person married to a third person is treated as not married), and the full rate (241.30 pounds a week).
Part 2: who is a prisoner for regulation 2 (kinds of custody, the section 47 release date, the outside-Great-Britain exception) and how remand changes it (regulation 3).
Part 3: the period for a choice and a late choice (regulation 4), the manner of making it (5), changing it (6), suspending (7), the date a suspension takes effect (8), cancelling it (9), the percentage (10), the days that do not count (11), part weeks (12) and modification periods (12A).
Part 4: the minimum number of qualifying years (13).
Part 5 and the Schedule: what the inserted regulation 6 of the 2000 Regulations makes the Secretary of State furnish, to whom, and by when.
Part 6: the survivor's pension (15, 16), its up-rating (17), the choice and what is paid (18), the lump sum (19) and the pension (20).
Part 7: which up-rating increases an overseas resident loses (21), the specified territory (21(6)), and the two modifications of an increment (22, 23).
Part 8: interpretation and general rules (24, 25), the Chapter 2 credits (26 to 28), the Chapter 3 credits (29 to 38) and the time limit (39).
The layers above that are the seat (59 questions) and their cases.

**Not encoded, and why (37 provisions `inert`, 1 `repealed or blank in this text`, 0 `not applicable`).**
The title, the recitals and the citation (no rule); the definitions of other instruments' names (the 1965 Act, the 2014 Act, the 1975 Regulations, the 1992 Act, the 2012 Act) and the borrowed terms (qualifying year, working tax credit, couple, graduated retirement benefit, uprating order), which are facts the person or a stated input supplies; and the amending machinery of the Schedule (paragraphs 1(1) to 1(9) and 2), which changes wording or numbering in two other sets of Regulations that are not among the inputs, so there is nothing in this text for them to decide.
Regulation 1(4) is shown with `{repealed: ...}` marks (fork F1); the live definitions beneath it are the four rows next to it.

**Not in this text at all, so not encoded.**
The Pensions Act 2014 (sections 2, 4, 7, 8, 9, 12, 17, 18, 20), the Administration Act (the text's own short name for it; its title is not given), the Social Security Contributions and Benefits Act 1992, the National Insurance Act 1965, the 1975 Regulations and the Sharing of State Scheme Rights Regulations 2000 are not among the inputs; every place a rule needs one of them is a stated input (below), never a guess.
Nothing in `jl4-core` or any other encoding was read or used.
No commencement order is needed: the text fixes its own commencement (6 April 2016), carried as a value.

## Coverage table

One row per paragraph of the text (a regulation with no paragraphs is one row; each definition is a row).
Headings are not provisions and have no row of their own.
Dispositions: `encoded`, `inert` (reason of real length), `repealed or blank in this text`, `not applicable`.
Every row carries one of the four dispositions; no row is `deferred` (counts: 162 `encoded`, 37 `inert`, 1 `repealed or blank in this text`, 0 `not applicable`, 200 rows).

| Provision | Source lines | What it is | Disposition | Where (module: rules) | Note |
| --- | --- | --- | --- | --- | --- |
| Title | 1-3 | 2015 No. 173, Social Security, The State Pension Regulations 2015 | inert | none | A title and a number: no rule. |
| Made / in force | 4-5 | Made 9th February 2015; Coming into force 6th April 2016 | encoded | spr-part1-general: `the date the Regulations were made`, `the date the Regulations come into force` | Dates are data, carried as values with an @ref. |
| Recitals | 6-10 | powers recital; Social Security Advisory Committee; consultation; draft approved | inert | none | Lines 6-10 recite the powers under which the Regulations are made (sections of the 1992 Act, the 1999 Act and the 2014 Act), the Social Security Advisory Committee's non-referral, the consultation on Part 5, and the approval of the draft by each House. They decide nothing for a person who is, or will become, entitled to the State Pension; they are the regulation-making machinery the Commons defaults put out of scope. |
| reg 1(1) | 13 | These Regulations may be cited as the State Pension Regulations 2015. | inert | none | The citation of the Regulations; no rule. |
| reg 1(2) | 14 | These Regulations come into force on 6th April 2016. | encoded | spr-part1-general: `the date the Regulations come into force` | Commencement date carried as a value (6 April 2016); the text fixes it, so it is not a stated input. |
| reg 1(3) | 15 | These Regulations (except Part 5) do not apply to a person who reaches | encoded | spr-part1-general: `whether Parts 1 to 4 and 6 to 8 apply to a person who reaches pensionable age on` | The text names the outcome 'do not apply', so it is a member of the result (total enum), not NOTHING. Date of reaching pensionable age is a fact (borrowed term). |
| reg 1(4) | 16 | {repealed: In these Regulations, “}{repealed: the 2014 Act}{repealed: | repealed or blank in this text | none | The text shows the single old definition ('the 2014 Act' means the Pensions Act 2014) with {repealed: ...} marks; the live definitions are the list that follows it (lines 17-21), which includes the same definition. See fork F1. |
| reg 1(4) lead-in | 17 | In these Regulations— | inert | none | 'In these Regulations—' introduces the four definitions below it, each its own row. |
| reg 1 def the 1965 Act | 18 | “the 1965 Act” means the National Insurance Act 1965; | inert | none | Names the National Insurance Act 1965, which is not among the inputs; used only inside the borrowed term 'graduated retirement benefit'. |
| reg 1 def the 2014 Act | 19 | “the 2014 Act” means the Pensions Act 2014; | inert | none | Names the Pensions Act 2014, which is not among the inputs. Every reference to it in the encoding is a stated input (the Act's effect), listed under 'Stated inputs'. |
| reg 1 def deferral period | 20 | “deferral period” means the period during which a person’s entitlement | encoded | spr-nouns: `Deferral period` (first day, last day); used by spr-part3-deferral and spr-part7-overseas | The definition is a noun: the stretch of time during which entitlement is deferred. |
| reg 1 def graduated retirement benefit | 21 | “graduated retirement benefit” means any benefit under section 36 (gra | inert | none | A borrowed term (benefits under ss 36-37 of the 1965 Act). Part 6 takes the weekly rate of the deceased's graduated retirement benefit as a stated input, so no rule is needed to define it. |
| reg 1(5) | 22 | For the purposes of these Regulations (except this paragraph), two peo | encoded | spr-part1-general: `the two people are treated as married to each other`, `the two people are treated as spouses or civil partners of each other` | Called by Part 3 (reg 11), Part 6 (regs 15, 18, 20) and Part 8 (regs 28, 33). Civil partners are not affected: the text says 'married'. See fork F2. |
| reg 1A | 24-25 | Full rate of state pension | encoded | spr-part1-general: `the full rate of the state pension, in pounds per week` | The figure is the one in the 2026-04-06 version of the text. See fork F3. |
| reg 2(1) | 28 | Subject to regulation 3, a person is not to be paid a state pension un | encoded | spr-part2-prisoners: `a state pension is not to be paid for the day` | Unit is one day of custody ('any period during which'). |
| reg 2(2) | 29-35 | Except where paragraph (3) applies, a person is a prisoner for the pur | encoded | spr-part2-prisoners: `the person is a prisoner within regulation 2(2) on the day`, `the day is on or before the certified release date, if there is one` | Paragraph (2)(c)(ii) hands the release date to the Secretary of State's certification: a MAYBE DATE input. Fork F4. |
| reg 2(3) | 36 | Where a person outside Great Britain is a prisoner within paragraph (2 | encoded | spr-part2-prisoners: `paragraph (3) of regulation 2 applies on the day` | Reaches (2)(a) and (b) only. |
| reg 2(4) | 37 | In determining a person’s rights to relevant benefits for the purposes | encoded | spr-part2-prisoners: `regulation 13 has effect when determining rights to relevant benefits for regulation 2` | A single negative statement (FALSE). Fork F5. |
| reg 3(1) | 39 | Where a person is remanded in custody for an offence, regulation 2(1) | encoded | spr-part2-prisoners: `regulation 2(1) does not apply to the day because of regulation 3` |  |
| reg 3(2) | 40-43 | Subject to paragraph (3), the described sentences for the purposes of | encoded | spr-part2-prisoners: `the sentence is one described in regulation 3(2)` | A suspended sentence counts (3(2)(c)). Fork F6. |
| reg 3(3) | 44 | A sentence described in paragraph (2)(a) which is imposed outside Grea | encoded | spr-part2-prisoners: `the sentence is one described in regulation 3(2)` | Reaches kind (2)(a) only. |
| reg 4(1) | 47-49 | Where a person falls within section 8(1) of the 2014 Act (choice of lu | encoded | spr-part3-deferral: `where the choice falls against its period` (lead-in) | Whether the person 'falls within section 8(1) of the 2014 Act' is a stated input (the parent Act's effect): the question is only asked of a person who does. |
| reg 4(2) | 50 | Where the Secretary of State has issued a notice which confirms that t | encoded | spr-part3-deferral: `the last day of the period of three months starting on`, `the date in the most recent notice`, `where the choice falls against its period` | Forks F7, F9. |
| reg 4(3) | 51-55 | Where the person makes the choice before the Secretary of State has is | encoded | spr-part3-deferral: `where the choice falls against its period` | A choice dated before the period starts is not provided for: a named 'not covered' member (fork F10), asserted. |
| reg 4(4) | 56-60 | A person may make a late choice after the period set out in this regul | encoded | spr-part3-deferral: `a late choice may be made` | The Secretary of State's view that it is reasonable is a conditional input, never guessed. |
| reg 4(5) | 61 | The amount of any lump sum to be paid to the person under section 8(4) | encoded | spr-part3-deferral: `the lump sum to be paid after a choice, the amount being` |  |
| reg 5(1) | 63-65 | Where a person falls within section 8(1) of the 2014 Act, this regulat | encoded | spr-part3-deferral: `it was given in a manner the Regulations allow` (lead-in) |  |
| reg 5(2) | 66-68 | The manner is— | encoded | spr-part3-deferral: `it was given in a manner the Regulations allow` | One rule serves regulations 5, 6(2)(d), 7(2)-(3) and (for Part 6) 18(3): they say the same thing. Whether an office or number 'is specified to the person in writing' is a fact about the Secretary of State's side (input). |
| reg 5(3) | 69 | The person must use the manner set out in paragraph (2)(a) where the S | encoded | spr-part3-deferral: `it was given in a manner the Regulations allow` |  |
| reg 6(1) | 71-74 | Any choice under section 8(2) of the 2014 Act to be paid— | encoded | spr-part3-deferral: `the choice may be altered` (lead-in) |  |
| reg 6(2) | 75-90 | The circumstances referred to in paragraph (1) are— | encoded | spr-part3-deferral: `the choice may be altered`, `the application is made within the time allowed`, `the repayment condition for a change to a state pension is met`, `the amount condition for a change to a lump sum is met` | All of (a) to (h) together ('and' before (h)); (e) and (f) bite only on the direction of the change they name. Fork F9b. |
| reg 6(3) | 91 | Where the circumstance in paragraph (2)(f) applies, any amount paid by | encoded | spr-part3-deferral: `the part of the lump sum still to be paid, the lump sum being` |  |
| reg 7(1) | 93 | A person who has become entitled to a state pension under Part 1 of th | encoded | spr-part3-deferral: `entitlement is suspended by a notice` |  |
| reg 7(2) | 94-96 | The manner in which the notice must be given is— | encoded | spr-part3-deferral: `it was given in a manner the Regulations allow` | Same rule as regulation 5(2). |
| reg 7(3) | 97 | But the person must use the manner set out in paragraph (2)(a) where t | encoded | spr-part3-deferral: `it was given in a manner the Regulations allow` | Same rule as regulation 5(3). |
| reg 8(1) | 99 | Where a person exercises their option to suspend their entitlement to | encoded | spr-part3-deferral: `the date from which the suspension takes effect` |  |
| reg 8(2) | 100-102 | The date is any date which the person specifies that is— | encoded | spr-part3-deferral: `the last date the person may specify, the option being exercised on`, `the date from which the suspension takes effect` | Fork F8. |
| reg 8(3) | 103 | Where the person does not specify a date in accordance with paragraph | encoded | spr-part3-deferral: `the date from which the suspension takes effect` | A date the person names outside paragraph (2) is not one 'in accordance with paragraph (2)', so the day of the option applies. |
| reg 9(1) | 105 | Where a person has opted to suspend their entitlement to a state pensi | encoded | spr-part3-deferral: `the suspension is cancelled for the past period` |  |
| reg 9(2) | 106 | The person cancels the suspension by making a claim for their state pe | encoded | spr-part3-deferral: `the suspension is cancelled for the past period` |  |
| reg 9(3) | 107 | The past period mentioned in paragraph (1) is any period of up to 12 m | encoded | spr-part3-deferral: `the suspension is cancelled for the past period` | Fork F9. |
| reg 10 | 108-109 | Percentage for the weekly rate of increases resulting from deferral of state pension | encoded | spr-part3-deferral: `the specified percentage for the increase in the weekly rate` | One-ninth of 1%, exactly (a rational). |
| reg 11(1) | 111 | In the circumstances set out in paragraph (2), a day does not count in | encoded | spr-part3-deferral: `the number of the listed days that do not count` |  |
| reg 11(2) | 112-129 | The circumstances mentioned in paragraph (1) are where the day is— | encoded | spr-part3-deferral: `the day does not count in determining a number of whole weeks` | Calls regulation 1(5) and Part 2. |
| reg 12(1) | 131 | In the circumstances set out in paragraph (2), a part of a week is to | encoded | spr-part3-deferral: `the whole weeks of deferral, there being` |  |
| reg 12(2) | 132 | The circumstances mentioned in paragraph (1) are where there is a part | encoded | spr-part3-deferral: `the number rounded up to a whole number`, `the whole weeks of deferral, there being` | Fork F12: applied once to the total period. |
| reg 12A(1) | 134 | Subject to regulation 23, this regulation applies in cases where, at a | encoded | spr-part3-deferral: `the modification periods of a deferral period` | With no non-uprating change the list is empty (nothing to modify). 'Subject to regulation 23' is encoded in spr-part7-overseas. |
| reg 12A(2) | 135 | Section 17(4) of the 2014 Act (amount of an increment for pensioner po | encoded | spr-part3-deferral: `the increment for each whole week of a modification period, the weekly rate being`, `the increase in the weekly rate from a period, the increment being` | Fork F11. The weekly rate 'immediately before the end of the modification period' is a stated input. |
| reg 12A(3) | 136 | The first modification period begins at the start of the deferral peri | encoded | spr-part3-deferral: `the modification periods beginning on` (the first period) |  |
| reg 12A(4) | 137-139 | Further modification periods begin on the date of the most recent or o | encoded | spr-part3-deferral: `the modification periods beginning on` (further periods) |  |
| reg 13(1) | 142 | For the purposes of section 2(3) of the 2014 Act (entitlement to state | encoded | spr-part4-qualifying-years: `the minimum number of qualifying years for a state pension payable at the reduced rate`, `the person has the minimum number of qualifying years for the reduced rate` | Ten. The number of a person's qualifying years is a fact (section 2(4) of the 2014 Act, not among the inputs). |
| reg 13(2) | 143 | For the purposes of section 4(2) of the 2014 Act (entitlement to a sta | encoded | spr-part4-qualifying-years: `the minimum number of qualifying years for a state pension payable at the transitional rate`, `the person has the minimum number of qualifying years for the transitional rate` | Ten, stated separately because the text states it separately. |
| reg 14 | 145-146 | Sharing of state pension scheme rights | inert | none (spr-part5-sharing.l4 header) | Says the Schedule has effect. The Schedule's paragraphs are each a row below. |
| reg 15(1) | 149 | A person whose dead spouse or civil partner paid graduated contributio | encoded | spr-part6-graduated: `a state pension is payable under regulation 15` | Whether the deceased 'paid graduated contributions as an insured person' is a stated input. |
| reg 15(2) | 150-154 | Such a person is entitled to a state pension if— | encoded | spr-part6-graduated: `the survivor has reached pensionable age`, `the marriage or civil partnership began before 6 April 2016`, `a state pension is payable under regulation 15` | Sub-paragraph (d) calls regulation 16. Pensionable age is a date asked as at a stated date. Fork F17. |
| reg 15(3) | 155 | A state pension under this regulation is payable at a weekly rate equa | encoded | spr-part6-graduated: `the weekly rate of a state pension under regulation 15` | NOTHING where the pension is not payable. |
| reg 15(4) | 156 | The rate of the state pension for a person under this regulation is to | encoded | spr-part6-graduated: `the rate of the person's state pension under regulation 15 after the increase` | Calls regulation 17. |
| reg 16(1) | 158-161 | For the purposes of regulation 15(2)(d), a person is entitled to an in | encoded | spr-part6-graduated: `regulation 16(1) applies`, `regulation 16(2) applies`, `regulation 16(3) applies`, `the paragraph of regulation 16 the survivor falls within` | Forks F14, F17. The three cannot overlap; asserted. |
| reg 16(2) | 162-165 | For the purposes of regulation 15(2)(d), a person is entitled to an in | encoded | spr-part6-graduated: `regulation 16(1) applies`, `regulation 16(2) applies`, `regulation 16(3) applies`, `the paragraph of regulation 16 the survivor falls within` | Forks F14, F17. The three cannot overlap; asserted. |
| reg 16(3) | 166-168 | For the purposes of regulation 15(2)(d), a person is entitled to an in | encoded | spr-part6-graduated: `regulation 16(1) applies`, `regulation 16(2) applies`, `regulation 16(3) applies`, `the paragraph of regulation 16 the survivor falls within` | Forks F14, F17. The three cannot overlap; asserted. |
| reg 16(4) | 169 | The inherited amount is half of the weekly rate of the deceased spouse | encoded | spr-part6-graduated: `the inherited amount` | Half the stated weekly rate; NOTHING when none of (1) to (3) applies. |
| reg 16(5) | 170-178 | The determination for the purposes of paragraph (4) is carried out by— | encoded | spr-part6-graduated: parameter of `the inherited amount` | Stated input: the rate from the graduated contributions the deceased paid, with up-rating orders since the death treated as in force before it and no addition under section 36(4) or 37(1) of the 1965 Act. Those parent-law tables are not among the inputs. |
| reg 16(6) | 179-181 | The date mentioned in paragraph (4) is— | encoded | spr-part6-graduated: `the date for the inherited amount` |  |
| reg 17(1) | 183 | The rate of a person’s state pension under regulation 15 is to be incr | encoded | spr-part6-graduated: `the increase in the rate of the person's state pension` |  |
| reg 17(2) | 184-187 | In this regulation, a reference to the rate of a person’s state pensio | encoded | spr-nouns: `Facts for the up-rating of a survivor's state pension` field `the rate of the person's state pension under regulation 15` (comment) | A definition of the rate to be entered: before reductions under regulations made under section 7(4) of the 2014 Act, after any reduction under section 14, and without any section 17 increase. Stated input. |
| reg 17(3) | 188-190 | The rate of the person’s state pension is increased in accordance with | encoded | spr-part6-graduated: `the up-rating case that applies`, `the rise from an increase in the full rate, applied to a base of`, `the increase in the rate of the person's state pension` | Applies only if the full rate rises. |
| reg 17(4) | 191-193 | Where paragraph (3) applies— | encoded | spr-part6-graduated: `the up-rating case that applies`, `the rise from an increase in the full rate, applied to a base of`, `the increase in the rate of the person's state pension` | Applies only if the full rate rises. |
| reg 17(5) | 194-200 | The rate of the person’s state pension is increased in accordance with | encoded | spr-part6-graduated: `the up-rating case that applies` | The two limbs of (a) separate the case; (b) says which event. |
| reg 17(6) | 201-203 | Where paragraph (5)(a) and (b)(i) applies, the rate of the person’s st | encoded | spr-part6-graduated: `the rise from an increase in the full rate, applied to a base of`, `the increase in the rate of the person's state pension` | The shortfall is paragraph (10)'s. Fork F15. |
| reg 17(7) | 204-206 | Where paragraph (5)(a) and (b)(ii) applies, the rate of the person’s s | encoded | spr-part6-graduated: `the rise from an uprating order, applied to a base of`, `the increase in the rate of the person's state pension` | The excess is paragraph (10)'s. Fork F15. |
| reg 17(8) | 207-209 | The rate of the person’s state pension is increased in accordance with | encoded | spr-part6-graduated: `the up-rating case that applies`, `the rise from an uprating order, applied to a base of`, `the increase in the rate of the person's state pension` | Applies only if an uprating order comes into force. |
| reg 17(9) | 210-212 | Where paragraph (8) applies— | encoded | spr-part6-graduated: `the up-rating case that applies`, `the rise from an uprating order, applied to a base of`, `the increase in the rate of the person's state pension` | Applies only if an uprating order comes into force. |
| reg 17(10) | 213 | In this regulation— | encoded | spr-part6-graduated: `the increase in the rate of the person's state pension` (the two local definitions) | Lead-in and the two definitions. |
| reg 17 def the excess | 214 | “the excess” means the amount by which the rate of the state pension, | encoded | spr-part6-graduated: `the increase in the rate of the person's state pension` (the two local definitions) | Lead-in and the two definitions. |
| reg 17 def the shortfall | 215 | “the shortfall” means the amount by which the sum of the rate of any s | encoded | spr-part6-graduated: `the increase in the rate of the person's state pension` (the two local definitions) | Lead-in and the two definitions. |
| reg 17 def uprating order | 216 | “uprating order” means an order under section 151A of the Administrati | inert | none | An order under section 151A of the Administration Act: the percentage it specifies is a stated input; the order itself is not among the inputs. |
| reg 18(1) | 218-224 | Subject to paragraph (8), a person is entitled to a choice under this | encoded | spr-part6-graduated: `the conditions of regulation 18(1)(a) to (d) are met`, `the person is entitled to a choice under regulation 18` | Fork F14 for sub-paragraph (d). |
| reg 18(2) | 225-227 | The person may choose to be paid— | encoded | spr-part6-graduated: `what is paid when the payment chosen is` | The two members of `Payment chosen`. |
| reg 18(3) | 228 | The manner in which that choice is to be made is the manner set out in | encoded | spr-part6-graduated: `what is paid under regulation 18` (calls `it was given in a manner the Regulations allow`) | A choice not made in the manner of regulation 5(2)-(3) is treated as no choice. |
| reg 18(4) | 229-233 | The period within which that choice is to be made is the period set ou | encoded | spr-part6-graduated: `what is paid under regulation 18` (calls `where the choice falls against its period` and `a late choice may be made`) | The Secretary of State's view that a late choice is reasonable is an input. |
| reg 18(5) | 234 | Where the person fails to make a choice within the period set out in r | encoded | spr-part6-graduated: `what is paid where no choice has been made`, `what is paid under regulation 18` | Whether the period has ended without a choice is a fact asked. |
| reg 18(6) | 235 | The amount of any lump sum to be paid to the person under regulation 1 | encoded | spr-part6-graduated: `what is paid under regulation 18`; `the lump sum payable under regulation 19` | A late choice for a state pension gives the outcome 'a state pension', so the lump sum is nil (asserted). |
| reg 18(7) | 236-239 | A choice under this regulation may be altered in the circumstances spe | encoded | spr-part6-graduated: `a choice under regulation 18 may be altered`, `the part of the lump sum under regulation 19 still to be paid` | Paragraphs (a) to (c) are readings of regulation 6; the module-level `Payment chosen` serves both sections. |
| reg 18(8) | 240 | A person is not entitled to a choice under this regulation if they are | encoded | spr-part6-graduated: `the person is entitled to a choice under regulation 18` | Whether the person is entitled to a choice under section 8(2) of the 2014 Act is a stated input. |
| reg 18(9) | 241-243 | Where paragraph (1) applies to a person and that person makes a choice | encoded | spr-part6-graduated: `what is paid when the payment chosen is` | The final choice, original or altered, is the input. |
| reg 18(10) | 244-246 | Where paragraph (1) applies to a person and that person alters a choic | encoded | spr-part6-graduated: `what is paid when the payment chosen is` | The final choice, original or altered, is the input. |
| reg 18(11) | 247 | Where paragraph (1) applies to a person and that person fails to make | encoded | spr-part6-graduated: `what is paid where no choice has been made` |  |
| reg 19(1) | 249 | Where a person is to be paid a lump sum by virtue of regulation 18, th | encoded | spr-part6-graduated: `the lump sum payable under regulation 19` | Stated input: the amount worked out under paragraph 10 or 20 of Schedule 1 to the Social Security (Graduated Retirement Benefit) Regulations 2005 (not among the inputs). |
| reg 19(2) | 250 | In paragraphs 10(6) and 20(6) of Schedule 1 to those Regulations as th | encoded | spr-part6-graduated: `the date the person becomes entitled to make a choice under regulation 18` | Fork F16. |
| reg 20(1) | 252-262 | A person is entitled to a state pension under this regulation if— | encoded | spr-part6-graduated: `a state pension is payable under regulation 20` | Sub-paragraphs (e) and (f) bite only on the two kinds of person they name (fork F18). Fork F14. |
| reg 20(2) | 263-265 | Subject to paragraph (3), a state pension under this regulation is pay | encoded | spr-part6-graduated: `the weekly rate of a state pension under regulation 20` | Half the stated rate of the increase. |
| reg 20(3) | 266 | For the purposes of paragraph (2), if at any time an order under secti | encoded | spr-part6-graduated: `the rate of a state pension under regulation 20 after an uprating order` |  |
| reg 20(4) | 267-272 | For the purposes of paragraph (2), the increase is to be determined as | encoded | spr-part6-graduated: parameter of `the weekly rate of a state pension under regulation 20` | Stated input: the increase determined as if up-rating orders between the death and the survivor reaching pensionable age had been in force before the death, and without any section 37(1) addition. |
| reg 20(5) | 273 | In this regulation, “increase in graduated retirement benefit” means a | encoded | spr-part6-graduated: parameter of `the weekly rate of a state pension under regulation 20` | The meaning of 'increase in graduated retirement benefit' (section 36(4) of the 1965 Act): the stated input. |
| reg 21(1) | 276 | An overseas resident who is entitled to a state pension under Part 1 o | encoded | spr-part7-overseas: `what regulation 21 does to an up-rating increase` | The principle that paragraphs (2) to (5) elaborate. 'Overseas resident' is not defined in these Regulations (it is the 2014 Act's): asked as a fact. |
| reg 21(2) | 277-281 | This regulation— | encoded | spr-part7-overseas: `what regulation 21 does to an up-rating increase` (first branch) | Whether Regulations have been made applying regulation 21 to the increase is a stated input; without them the result is a named 'does not apply' member, asserted. Paragraph (2)(b) ('subject to the Regulations made') is that same input. |
| reg 21(3) | 282-286 | Paragraph (4) applies in a case where— | encoded | spr-part7-overseas: `what regulation 21 does to an up-rating increase` (the deferral case) |  |
| reg 21(4) | 287-291 | Where this paragraph applies, the person mentioned in paragraph (3) is | encoded | spr-part7-overseas: `what regulation 21 does to an up-rating increase` | Fork F19. |
| reg 21(5) | 292-294 | In all other cases, a person is not entitled to up-rating increases wh | encoded | spr-part7-overseas: `what regulation 21 does to an up-rating increase` | 'All other cases' are those where paragraph (3) does not apply. Fork F19. |
| reg 21(6) | 295 | For the purposes of sections 18(4) and 20(2) and (3) of the 2014 Act, | encoded | spr-part7-overseas: `the person is in a territory specified in regulation 21(6)` | Whether the person is in a part of the Channel Islands, and whether Orders under section 179 of the Administration Act cover it, are facts asked. |
| reg 22(1) | 297 | Subject to regulation 23, this regulation applies in cases where, duri | encoded | spr-part7-overseas: `regulation 22 applies to the deferral period` |  |
| reg 22(2) | 298 | For any part of the deferral period during which the person was an ove | encoded | spr-part7-overseas: `which weekly rate the increment for a part is a percentage of`, `the weekly rate regulation 22 refers to for a part`, `the increment under regulation 22, the weekly rate being` | An overseas resident who is in Great Britain or a specified territory is in neither (2) nor (3): a named 'the Regulations do not say' member (fork F21), asserted. |
| reg 22(3) | 299 | For any part of the deferral period during which the person was not an | encoded | spr-part7-overseas: `which weekly rate the increment for a part is a percentage of`, `the weekly rate regulation 22 refers to for a part`, `the increment under regulation 22, the weekly rate being` | The percentage is regulation 10's. Fork F21. |
| reg 23(1) | 301 | This regulation applies in a case where section 17(4) of the 2014 Act | encoded | spr-part7-overseas: `regulation 23 applies to` |  |
| reg 23(2) | 302 | Section 17(4) of the 2014 Act is modified to provide that the amount o | encoded | spr-part7-overseas: `the increment under regulation 23, the weekly rate regulation 22 refers to being` | The lead-in to the steps (3) to (5). |
| reg 23(3) | 303 | The amount of the increment is first determined in accordance with the | encoded | spr-part7-overseas: `the increment under regulation 23, the weekly rate regulation 22 refers to being` (the first increment) |  |
| reg 23(4) | 304-306 | The amount of the increment is then determined in accordance with the | encoded | spr-part7-overseas: `the increment under regulation 23, the weekly rate regulation 22 refers to being` (the increment worked out under paragraph (4)) | Fork F20. |
| reg 23(5) | 307 | Any increase or decrease of the increment as determined in accordance | encoded | spr-part7-overseas: `the increment under regulation 23, the weekly rate regulation 22 refers to being` (the change in the increment) | Fork F20. |
| reg 24(1) | 311 | In this Part— | inert | none | Lead-in to definitions; the definitions are the rows that follow. |
| reg 24 def the 1975 Regulations | 312 | “the 1975 Regulations” means the Social Security (Credits) Regulations | inert | none | Names of other instruments; each is cited by its short name in the rules that use it. The instruments themselves are not among the inputs. |
| reg 24 def the 1992 Act | 313 | “the 1992 Act” means the Social Security Contributions and Benefits Ac | inert | none | Names of other instruments; each is cited by its short name in the rules that use it. The instruments themselves are not among the inputs. |
| reg 24 def the 2012 Act | 314 | “the 2012 Act” means the Welfare Reform Act 2012; | inert | none | Names of other instruments; each is cited by its short name in the rules that use it. The instruments themselves are not among the inputs. |
| reg 24 def post-commencement qualifying year | 315 | “post-commencement qualifying year” and “pre-commencement qualifying y | inert | none | Borrowed from section 4(4) and section 2(4) of the 2014 Act, not among the inputs. A qualifying year's test is a stated input wherever a rule needs one (regulation 25(2)). |
| reg 24 def qualifying year | 316 | “qualifying year” has the same meaning as in section 2(4) of the 2014 | inert | none | Borrowed from section 4(4) and section 2(4) of the 2014 Act, not among the inputs. A qualifying year's test is a stated input wherever a rule needs one (regulation 25(2)). |
| reg 24 def working tax credit | 317 | “working tax credit” means a working tax credit under section 10 of th | inert | none | A credit under section 10 of the Tax Credits Act 2002: a borrowed term, a fact in regulation 30. |
| reg 24 def year | 318 | “year” means a tax year. | encoded | spr-part8-credits-general: `the tax year a calendar day falls in` | A tax year, 6 April to 5 April, named by the calendar year in which it begins. |
| reg 24(2) | 319 | Nothing in Chapter 3 is to be construed as entitling any person to be | encoded | spr-part8-credits-general: `a credit under Chapter 3 may be given for the week` | Fork F22. Every Chapter 3 rule calls it. |
| reg 25(1) | 321-323 | For the purposes of Part 1 of the 2014 Act— | encoded | spr-part8-credits-general: `the week falls in a year before 6 April 2016` | Which Chapter credits a week, by the year the week falls in. |
| reg 25(2) | 324 | Where under this Part a person would, but for this paragraph, be entit | encoded | spr-part8-credits-general: `the amount the person is credited with` | The amount needed to make the year a qualifying year is a stated input. |
| reg 25(3) | 325 | Where under this Part a person is entitled to be credited with earning | encoded | spr-part8-credits-general: `the tax year a week falls in` | A week that falls partly in two years falls in the one it begins in. Tested at 5 and 6 April. |
| reg 26 | 327-330 | Credits under the 1975 Regulations | encoded | spr-part8-credits-general: `the person is credited under regulation 26` | The counterfactual (Category A retirement pension under the 1975 Regulations on stated assumptions) is a stated input. |
| reg 27 | 331-334 | Credits for parents and carers | encoded | spr-part8-credits-general: `the person is credited under regulation 27` | The counterfactual (section 23A of the 1992 Act) is a stated input. |
| reg 28(1) | 336 | Subject to paragraph (5), a person who satisfies the conditions in par | encoded | spr-part8-credits-general: `a Class 3 contribution is credited under regulation 28` | Lead-in: subject to paragraph (5). |
| reg 28(2) | 337-339 | The conditions are that the person— | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | Same rule serves regulation 33(2). |
| reg 28(3) | 340 | This regulation applies to a week which falls within a year beginning | encoded | spr-part8-credits-general: `a Class 3 contribution is credited under regulation 28` | Years beginning on or after 6 April 1975 and ending before 6 April 2016. |
| reg 28(4) | 341-348 | Paragraph (1) does not apply to— | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | Entitlement to credits under regulation 7A, 8A, 8B or 9E of the 1975 Regulations and a married woman's election are stated inputs. |
| reg 28(5) | 349 | A person is not entitled to be credited with a Class 3 contribution un | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` |  |
| reg 28(6) | 350-352 | An application under paragraph (5) may only be made in respect of a pa | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | 'Only in respect of a past period': fork F23. |
| reg 29(1) | 355 | Where a person is credited with earnings or contributions under the pr | encoded | spr-part8-credits-post2016: `a credit under the 1975 Regulations also counts for the 2014 Act` | The nine provisions are the members of `Provision of the 1975 Regulations`. Whether the person was credited under one is a fact about HMRC's or the Secretary of State's side, asked of the person. |
| reg 29(2) | 356-365 | The provisions specified are— | encoded | spr-part8-credits-post2016: `a credit under the 1975 Regulations also counts for the 2014 Act` | The nine provisions are the members of `Provision of the 1975 Regulations`. Whether the person was credited under one is a fact about HMRC's or the Secretary of State's side, asked of the person. |
| reg 30(1) | 367-371 | Where working tax credit is paid to a person in respect of a week in w | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 30`, `the earnings credited under regulation 30` | The lower earnings limit then in force is a stated input. |
| reg 30(2) | 372-374 | Where working tax credit is paid in respect of a couple, the reference | encoded | spr-part8-credits-post2016: `the person is the person in respect of whom working tax credit is paid` |  |
| reg 30(3) | 375-381 | Paragraph (1) does not apply to— | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 30` |  |
| reg 30(4) | 382 | In this regulation, “couple” has the same meaning as in section 3(5A) | inert | none | 'Couple' has the meaning in section 3(5A) of the Tax Credits Act 2002 (not among the inputs): the fact that credit is paid in respect of a couple is asked. |
| reg 31 | 383-384 | Credits for persons entitled to universal credit | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 31` |  |
| reg 32(1) | 386 | Subject to paragraph (4), a man born before 6th October 1953 is to be | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 32`, `the earnings credited under regulation 32` | Whether the person is a man is a stated input, as the text says. |
| reg 32(2) | 387-389 | This paragraph applies to a week which falls within— | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 32` | Years are compared as tax years; the date he attains the pensionable age of a woman born the same day is a stated input. |
| reg 32(3) | 390 | Paragraph (2) does not apply to a week which falls within a year durin | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 32` | More than 182 days: 183 days is out, 182 in (asserted). |
| reg 32(4) | 391-393 | Paragraph (1) applies to a man who is a self-employed earner only if h | encoded | spr-part8-credits-post2016: `earnings are credited under regulation 32` |  |
| reg 33(1) | 395 | Subject to paragraph (5), a person who satisfies the conditions in par | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 33` | Lead-in: subject to paragraph (5). |
| reg 33(2) | 396-398 | The conditions are that the person— | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | The same words as regulation 28(2), (4), (5), (6): one rule. |
| reg 33(3) | 399 | This regulation applies to a week which falls within a year beginning | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 33` | A year beginning on or after 6 April 2016. |
| reg 33(4) | 400-407 | Paragraph (1) does not apply to— | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | The same words as regulation 28(2), (4), (5), (6): one rule. |
| reg 33(5) | 408 | A person is not entitled to be credited with a Class 3 contribution un | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | The same words as regulation 28(2), (4), (5), (6): one rule. |
| reg 33(6) | 409-411 | An application under paragraph (5) may only be made in respect of a pa | encoded | spr-part8-credits-general: `the conditions for a forces spouse's credit are met` | The same words as regulation 28(2), (4), (5), (6): one rule. |
| reg 34(1) | 413-415 | A person is entitled to be credited with a Class 3 contribution in res | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 34` |  |
| reg 34(2) | 416-421 | The circumstances are that the partner— | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 34` | Sub-paragraph (e) is regulation 39 for the kind 'an application under regulation 34(1)(b)'. |
| reg 34(3) | 422 | Paragraph (1)(b) only applies in respect of a week that falls within a | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 34` | Paragraph (4) is a rule for how the earnings factors are counted (leaving out credits derived from the award); the earnings-factor test is a stated input that already leaves them out. |
| reg 34(4) | 423 | In calculating the earnings factors for the purpose of paragraph (3), | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 34` | Paragraph (4) is a rule for how the earnings factors are counted (leaving out credits derived from the award); the earnings-factor test is a stated input that already leaves them out. |
| reg 35(1) | 425 | Subject to paragraphs (3) and (4), a person is to be credited with a C | encoded | spr-part8-credits-post2016: `whether a Class 3 contribution is credited under regulation 35` |  |
| reg 35(2) | 426-429 | The conditions are that in the relevant week the person— | encoded | spr-part8-credits-post2016: `whether a Class 3 contribution is credited under regulation 35` |  |
| reg 35(3) | 430-435 | The person (‘A’) referred to in paragraph (1) is not entitled to be cr | encoded | spr-part8-credits-post2016: `whether a Class 3 contribution is credited under regulation 35` | Child benefit awarded to the other person, and that person's earnings factors, are stated inputs. |
| reg 35(4) | 436-438 | Where the requirements relating to the provision of care by A in parag | encoded | spr-part8-credits-post2016: `who is credited where more than one person could be` | Paragraph (4)(b), the Secretary of State's discretion in default of agreement, is a named 'left to the Secretary of State' result, asserted (fork F27). |
| reg 35(5) | 439-442 | An application under paragraph (3)(c) must— | encoded | spr-part8-credits-post2016: `the application meets regulation 35(5)` |  |
| reg 35(6) | 443-457 | The person specified in paragraph (2)(b) is— | encoded | spr-part8-credits-post2016: `the relationship is one regulation 35(6) specifies`; nouns: `Relationship to the child cared for` | The eleven kinds of relationship are the members of the type; the person's relationship is a stated input. |
| reg 35(7) | 458 | For the purposes of paragraph (6)(e) and (f), a sibling includes a sib | encoded | spr-part8-credits-post2016: `the person counts as a sibling under regulation 35(7)` | Stand-alone: the relationship member for a sibling already says it includes half-blood, step and adopted siblings. |
| reg 35(8) | 459 | For the purposes of paragraph (6)(i) and (k)(iii), a partner is a pers | encoded | spr-part8-credits-post2016: `the person counts as a partner under regulation 35(8)` | Stand-alone, for the same reason. |
| reg 36(1) | 461-463 | Subject to paragraph (3), a person is to be credited with a Class 3 co | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 36` |  |
| reg 36(2) | 464-468 | For the purposes of this regulation, a foster parent is a person appro | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 36`; nouns: `Approval as a foster parent` | The four approvals are the members of the type. |
| reg 36(3) | 469 | A person is not entitled to be credited with a Class 3 contribution un | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 36` | Regulation 39 for the kind 'an application under regulation 36'. |
| reg 37(1) | 471 | Subject to paragraph (5), a person is to be credited with a Class 3 co | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 37` |  |
| reg 37(2) | 472-476 | A person is engaged in caring in a week if the person is— | encoded | spr-part8-credits-post2016: `the person is engaged in caring under paragraph (2)(a)`, `a Class 3 contribution is credited under regulation 37` | Whether the Secretary of State considers the level of care appropriate is a stated input. |
| reg 37(3) | 477-479 | A person is not engaged in caring for the purposes of this regulation | encoded | spr-part8-credits-post2016: `the person is not excluded from caring by paragraph (3)` |  |
| reg 37(4) | 480-495 | For the purposes of paragraph (2)(a)(i), “relevant benefit” means— | encoded | spr-part8-credits-post2016: `the benefit is a relevant benefit`; nouns: `Relevant benefit` | The eleven benefits are the members of the type (including (aa)). |
| reg 37(5) | 496 | Except in a case to which paragraph (8) applies, a person is not entit | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 37` | Fork F25. |
| reg 37(6) | 497-501 | An application under paragraph (5) must include— | encoded | spr-part8-credits-post2016: `the application meets regulation 37(6)` |  |
| reg 37(7) | 502-504 | For the purposes of paragraph (6)(d), an appropriate person is a perso | encoded | spr-part8-credits-post2016: `the person is an appropriate person` | Stand-alone: the application records whether a declaration was signed by one. |
| reg 37(8) | 505 | This paragraph applies in the case of a woman in respect of a week in | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 37` | Fork F25: read literally it removes the need for an application. |
| reg 38(1) | 507-510 | A person is to be credited with a Class 3 contribution for a period of | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 38` | Fork F26. |
| reg 38(2) | 511 | A person is not entitled to be credited with a Class 3 contribution un | encoded | spr-part8-credits-post2016: `a Class 3 contribution is credited under regulation 38` |  |
| reg 39 | 512-519 | Time limit for making an application under regulation 34(1)(b), 35, 36 or 37 | encoded | spr-part8-credits-post2016: `the application is received in time` | Fork F24. |
| Sch 1(1) | 521 | The Sharing of State Scheme Rights (Provision of Information and Valua | inert | none | Introduces the amendments to the Sharing of State Scheme Rights (Provision of Information and Valuation) (No.2) Regulations 2000 (the 2000 Regulations), which are not among the inputs; amending machinery decides nothing for the person under these Regulations. |
| Sch 1(2) | 522 | In regulations 1(2), 2 and 3 in each reference to “shareable state sch | inert | none | Inserts the word 'old' into the 2000 Regulations' references to 'shareable state scheme rights'. A wording amendment to an instrument not among the inputs. |
| Sch 1(3) | 523 | In regulation 1(2) (citation, commencement and interpretation) after t | inert | none | Introduces four definitions inserted into regulation 1(2) of the 2000 Regulations. Each is its own row. |
| Sch 1(3) def new state scheme pension credit | 524 | “new state scheme pension credit” is a credit under section 49A(2)(b) | inert | none | A credit under section 49A(2)(b) of the 1999 Act: a borrowed term (the 1999 Act is not among the inputs); not used by any rule here. |
| Sch 1(3) def old state scheme pension credit | 525 | “old state scheme pension credit” is a credit under section 49(1)(b) o | inert | none | A credit under section 49(1)(b) of the 1999 Act: a borrowed term, not used by any rule here. |
| Sch 1(3) def relevant date | 526 | “relevant date” has the meaning given by section 10(3) of the Family L | encoded | spr-nouns: `Request for information about sharing` field `the relevant date` (a MAYBE DATE input); spr-part5-sharing | Defined by section 10(3) of the Family Law (Scotland) Act 1985 (not among the inputs): a borrowed term, asked as a fact. There is none in proceedings that Act does not govern, hence MAYBE. |
| Sch 1(3) def shareable new state scheme rights | 527 | “shareable new state scheme rights” has the meaning given by section 4 | inert | none | Defined by section 47(3) of the 1999 Act (not among the inputs): a borrowed term. The encoding is asked only of a person who has such rights. |
| Sch 1(4) | 528-530 | In regulation 2(3) (basic information about the sharing of state schem | inert | none | Amends regulation 2(3) of the 2000 Regulations (the basic information about sharing for old rights): wording changes in an instrument not among the inputs. |
| Sch 1(5) | 531-537 | In regulation 4 (calculation and verification of cash equivalents for | inert | none | Amends regulation 4 of the 2000 Regulations (calculation and verification of cash equivalents): adds two paragraphs and a phrase. Wording changes in an instrument not among the inputs; cash equivalents are calculated by officials. |
| Sch 1(6) | 538 | Regulation 1 becomes Part 1 of the Sharing of State Scheme Rights (Pro | inert | none | Renumbering: regulation 1 of the 2000 Regulations becomes Part 1. |
| Sch 1(7) | 539 | The title of that Part 1 is “General”. | inert | none | Gives that Part 1 its title. |
| Sch 1(8) | 540 | Regulations 2 to 5 become Part 2 of the Sharing of State Scheme Rights | inert | none | Renumbering: regulations 2 to 5 of the 2000 Regulations become Part 2. |
| Sch 1(9) | 541 | The title of that Part 2 is “Old State Scheme Pension Credits and Debi | inert | none | Gives that Part 2 its title. |
| Sch 1(10) | 542 | After Part 2, insert— | inert | none | 'After Part 2, insert—': the lead-in to the inserted Part 3. The inserted regulations 6 and 7 are the rows below. |
| Sch 1 > inserted reg 6(1) | 545-549 | The requirements imposed on the Secretary of State for the purposes of | encoded | spr-part5-sharing: `the information the person with shareable new state scheme rights is owed on request`, `the information the spouse or civil partner of the person is owed on request` | Paragraph (1)(a)(ii) (information to a court on an order) is not encoded as owed to the person: it is owed to the court. |
| Sch 1 > inserted reg 6(2) | 550 | Except where paragraphs (3) or (4) apply, the information specified in | encoded | spr-part5-sharing: `the valuations and amount that go with the request` | The default valuation, as at the date of receipt. |
| Sch 1 > inserted reg 6(3) | 551 | The information specified in this paragraph is a valuation of the pers | encoded | spr-part5-sharing: `the valuation is as at the relevant date and the relevant date is on or after 6 April 2016`, `the valuations and amount that go with the request` |  |
| Sch 1 > inserted reg 6(4) | 552 | The information specified in this paragraph is a valuation of the pers | encoded | spr-part5-sharing: `the relevant date is before 6 April 2016 and the request is received on or after it`, `the valuations and amount that go with the request` |  |
| Sch 1 > inserted reg 6(5) | 553 | The information specified in this paragraph is the amount of the perso | encoded | spr-part5-sharing: `the valuations and amount that go with the request` | The Category A amount, owed with (4). |
| Sch 1 > inserted reg 6(6) | 554-558 | The information in this paragraph is an explanation of— | encoded | spr-nouns: `Item of information about sharing` (the explanation); spr-part5-sharing: the two `the information ...` rules | The explanation is the one item owed in every case. |
| Sch 1 > inserted reg 6(7) | 559-562 | The Secretary of State shall furnish the information specified in para | encoded | spr-part5-sharing: `the last day by which the Secretary of State must furnish the information` | Forks F7, F13. |
| Sch 1 > inserted reg 6(8) | 563-566 | Where— | encoded | spr-part5-sharing: `the last day by which the Secretary of State must furnish the information` | One month beginning with the day received. |
| Sch 1 > inserted reg 7 | 567-568 | Information about the sharing of state scheme rights and divorce or dissolution of a civil partnership: valuation of shareable old or new state scheme rights | inert | none | Says the valuation is calculated and verified in accordance with guidance from time to time prepared by the Government Actuary, which is not among the inputs, and is work done by officials; it decides no question for the person except what the valuation is, which the person is simply given. |
| Sch 2(1) | 570 | The Pensions on Divorce etc. (Pension Sharing) (Scotland) Regulations | inert | none | Introduces amendments to the Pensions on Divorce etc. (Pension Sharing) (Scotland) Regulations 2000 (not among the inputs). |
| Sch 2(2) | 571-572 | In regulation 1(2) (citation, commencement and interpretation)— | inert | none | Inserts two definitions and amends a third in regulation 1(2) of those Regulations; wording changes in an instrument not among the inputs. |
| Sch 2(2) def excess amount | 573-574 | “excess amount” has the meaning given by section 47(4) of the 1999 Act | inert | none | Defined by section 47(4) of the 1999 Act: a borrowed term, not used by any rule here. |
| Sch 2(2) def shareable old state scheme rights | 575-576 | “shareable old state scheme rights” has the meaning given by section 4 | inert | none | Defined by section 47(2) of the 1999 Act: a borrowed term, not used by any rule here. |
| Sch 2(3) | 577-580 | In regulation 4(a)(v) (prescribed form of provision corresponding to p | inert | none | Amends regulation 4(a)(v) of those Regulations (the prescribed form of a provision corresponding to a pension sharing order): a form amended by wording. |
| Sch 2(4) | 581-583 | After regulation 4(a)(v), insert— | inert | none | Inserts a new item (vi) into the prescribed form (details of the specified percentage of the excess amount of the transferor's state pension as at the transfer day): a content requirement for a document drawn up by the parties and the court, not a rule about when or how a State Pension is claimed or paid. |

## Fork register

**F1. Regulation 1(4), the repealed paragraph and the live definitions.** The text shows paragraph (4) as `{repealed: In these Regulations, “}{repealed: the 2014 Act}{repealed: ” means the Pensions Act 2014.}` (line 16) and then, as its own lines, `In these Regulations—` followed by four definitions, one of which is `“the 2014 Act” means the Pensions Act 2014` (lines 17 to 21). Reading A: the single-definition form is repealed and the list is the in-force paragraph (4). Reading B: paragraph (4) as a whole is repealed and the list is a stray. **Taken: A**, because the list carries three definitions (deferral period, the 1965 Act, graduated retirement benefit) that other regulations use and that the repealed words do not contain. The row is marked `repealed or blank in this text` for line 16 and the list is covered row by row.

**F2. Regulation 1(5) and civil partners.** "Two people are to be treated as if they are not married to each other in relation to times when either of them is married to a third person." Reading A: only a marriage is taken away; civil partners stay civil partners. Reading B: the deeming also strips a civil partnership. **Taken: A**, on the words "married" and "married to a third person" (a person in a civil partnership cannot be married to a third person). The deeming is carried by `the two people are treated as married to each other` and called wherever a later regulation says "spouse", "married" or "civil partner" (regulations 11(2)(b)(ii), 15(2)(b), 18(1)(b), 20(1)(b), 28(2)(a), 33(2)(a)).

**F3. Regulation 1A, the full rate is a figure of one date.** The text states £241.30 per week. The deposited text is the revised version at 2026-04-06 and the converter's caveat says it "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish". The figure is therefore the rate in that version; earlier years had other rates (the rate is uprated each April) and are not among the inputs. **Taken:** the figure is encoded as stated, with the version named; no earlier vintage is invented. A reviewer must confirm the figure is the one in force for the date a question is asked about.

**F4. Regulation 2(2)(c)(ii), "(if any)".** A person detained under section 47 of the Mental Health Act 1983 is a prisoner only "on or before the day which the Secretary of State certifies to be the person's release date (if any)". If no day has been certified: Reading A: nothing ends the detention, so the condition is met on every day; Reading B: the condition cannot be met without a certified day, so the person is not a prisoner. **Taken: A**, because "(if any)" shows the drafter expected cases with no release date, and B would let a person detained with no release date escape the paragraph. The certification is the Secretary of State's, so it is an input (`MAYBE DATE`) and never guessed. Tested on both sides of the certified day, and with none.

**F5. Regulation 2(4).** "In determining a person's rights to relevant benefits for the purposes of this regulation, regulation 13 of the State Pension Regulations 2015 (minimum number of qualifying years), and any provisions in Northern Ireland which correspond to that regulation, shall not have effect." "Relevant benefits" is a term of section 19 of the 2014 Act (not among the inputs), and nothing in regulation 2 itself reads a person's rights to relevant benefits. Reading A: it is a rule that switches regulation 13's ten-year minimum off for one purpose. Reading B: it is a stray (the paragraph refers to the Regulations it forms part of). **Taken: A, minimally**: encoded as the one thing it says (a value `FALSE` named for that purpose), and flagged in NOTES as a text oddity for the reviewer. No rule of this encoding reads it, because no rule of this encoding determines rights to relevant benefits.

**F6. Regulation 3(2)(c), a suspended sentence.** A person who is remanded and later given a suspended sentence is not released from regulation 2(1): the suspended sentence is a "described sentence" (line 43). On the face of it a suspended sentence means no custody, yet regulation 3 brings regulation 2(1) back for the remand. **Taken as written:** the encoding follows the words and asserts it. The text does not say whether the pension withheld for the remand period is recovered, nor how: that is outside these inputs.

**F7. "Three months starting on the date" (regulation 4(2), and 6(2)(c)(i)).** Reading A: calendar months, the named date is the first day, the period ends on the day before the corresponding date three months on (so 1 March to 31 May), or on the last day of that month where there is no corresponding date (30 November to 28 February). Reading B: a period of 90 days. Reading C: ending on the corresponding date itself (1 March to 1 June). **Taken: A**, on "months" being calendar months and "starting on" counting the named day (the "beginning with" convention of the skill's phrasebook 4.5). A choice on 1 June is therefore late; tested on 31 May and 1 June, and across the month-end clamp.

**F8. "Not after 28 days starting with the date on which the option was exercised" (regulation 8(2)(b)).** Reading A: the 28 days begin on the day of the option, so the last day that may be specified is 27 days after it (1 March to 28 March). Reading B: 28 days after it (29 March). **Taken: A**, the same "starting with" counting as F7. Tested at 28 March (in) and 29 March (out).

**F9. "Any period of up to 12 months before the date on which the person cancels the suspension" (regulation 9(3)).** Edges: the cancelling date is a day on which a claim is made; "before" it excludes that day from the past period; "up to 12 months" includes a period starting on the same calendar day a year earlier (15 March 2025 for a claim on 15 March 2026). **Taken:** first day not before the date twelve calendar months earlier (the library's `add months`, which clamps at month ends), last day strictly before the cancelling date. The text does not say the period must lie inside the suspension; the encoding does not add that either.

**F9b. Regulation 6(2)(e)(ii), "within the period mentioned in sub-paragraph (c)".** Sub-paragraph (c) mentions two periods (three months from the notification; such longer period as the Secretary of State considers reasonable). Reading A: the repayment must fall within whichever of those periods the application used. Reading B: always within the three months. **Taken: A**, as a fact the person states ("was it repaid within the period in which you applied?"); the encoding does not decide which period is meant.

**F10. A choice made before its period begins (regulation 4).** Where no notice has been issued the period starts on the later of the day the person claims a state pension and the day the spouse or civil partner died (4(3)(a)); a choice on an earlier day lies before the period. The text provides for a choice in the period and a late choice (4(4), "after the period"), but not for a choice before it. **Taken:** the result names it as its own member (`before the period begins, which the text does not provide for`) and the encoding says nothing about its effect. Asserted. The same member answers a choice dated before the notice that opens the period.

**F11. Sections 17(3)-(4) of the 2014 Act, the parent Act's formula.** Regulations 10 to 12A supply the percentage, the days not counted, part weeks and the modification periods, and say they apply "for the purposes of section 17(3)" and "section 17(4)". Section 17 itself is not among the inputs. Reading A: the increase in the weekly rate is the sum, over the periods, of whole weeks times the per-week increment, which is the percentage of a weekly rate. Reading B: some other composition. **Taken: A**, marked as the Act's effect and not this instrument's; the layer 1 rules give the increment per whole week (what 12A(2) calls "the amount of an increment") and the product, separately, so a reviewer can swap the product. The whole weeks of each modification period are inputs, because the text applies regulation 12 to "the total period" and does not say how part weeks fall between modification periods.

**F12. Regulation 12, part weeks.** "A part of a week in the total period during which the person's entitlement was deferred, after any days have been discounted under regulation 11" is treated as a whole week. Reading A: the whole weeks are the days remaining after regulation 11, divided by seven and rounded up, once, for the total period. Reading B: rounding up each stretch separately. **Taken: A**, on "in the total period". Tested at 63, 70, 71 days, with and without discounted days.

**F13. Inserted regulation 6(7): which of (a), (b) and (c) is the time limit.** The Secretary of State must furnish the information "within" three months, six weeks (if the person has notified), "or" such shorter period as the court specifies. Reading A: the earliest period that applies. Reading B: the Secretary of State may choose any one that applies. **Taken: A**, because under B paragraphs (b) and (c) (a shorter period) would never bind. Tested: with the person's notice, with the court's period, with neither, and with a court period longer than three months (which does not extend the time).

**F14. "Under" and "over" pensionable age when the spouse or civil partner died (regulations 16(1)-(3), 18(1)(d), 20(1)(c)).** Reading A: the survivor was under it if the death came before the day they reached pensionable age, and over it if the death came on or after that day. Reading B: "over" is strictly after, so a death on the very day the survivor reaches pensionable age is in neither limb, and the person falls out of regulations 16(3), 18(1)(d) and 20(1)(c) altogether. **Taken: A**, so that the two limbs are exhaustive. Tested at the day itself and the day before.

**F15. Regulation 17(5) to (7): both events at once.** Where the full rate rises and an uprating order comes into force together, paragraphs (6) and (7) each increase "immediately before" their own event. Reading A: each rise is worked from the position before either event, and the two rises are added. Reading B: they are applied in sequence, the second on the rate after the first. **Taken: A**, since neither paragraph mentions the other's increase. The shortfall (full rate less the other pensions) and the excess (the survivor's pension plus the other pensions, less the full rate) are both read at the old full rate. Tested: either event alone and both.

**F16. "The date on which the person becomes entitled to make a choice under regulation 18" (regulation 19(2)).** The text does not give the date. Reading A: the later of the day the survivor reaches pensionable age and the day the spouse or civil partner dies, since regulation 18(1) requires both (the survivor has reached pensionable age, the spouse has died). Reading B: the date the survivor first claims. **Taken: A.** Tested on both orders and the equal case. The date feeds paragraphs 10(6) and 20(6) of the 2005 Regulations, which are not among the inputs, so the encoding stops at the date.

**F17. "6th April 2016" in regulations 15, 16 (and elsewhere).** The text writes the same date it gives for the Regulations coming into force. Reading A: it is one value, `the date the Regulations come into force`, used everywhere. Reading B: a separate constant per use. **Taken: A.** If a later amendment moves one and not the other, this becomes two values.

**F18. Regulation 20(1)(e) and (f).** (e) applies "in the case of a person entitled to a choice under regulation 18" and (f) "in the case of a person who is not entitled to a choice ... because regulation 18(8) applies". Reading A: a person in neither class (the deceased was entitled to an increase and was not deferred, so there is no choice) satisfies both vacuously. Reading B: (e) and (f) are conditions for everyone. **Taken: A**, because on B the person with an increase and no choice could never be paid under regulation 20(2)(a). Tested for that person (paid), for the person with the choice (paid only if they chose a state pension), and for the 18(8) person.

**F19. Regulation 21: when an overseas resident is measured.** Paragraph (4) speaks of being an overseas resident "at the time of that increase" and paragraph (5) of being one "immediately before the up-rating increase comes into force". Reading A: one moment, so one input. Reading B: two moments (the instant before, and the instant of the increase). **Taken: A**; a person who moves abroad on the day of the increase is outside what the text can distinguish.

**F20. Regulation 23(4) and (5): the change measured against what.** Paragraph (4) has regulation 12A(2) read with the weekly rate of regulation 22(2) or (3) in place of its own; 12A(2) then gives the percentage of that rate, which is also what regulation 22 gave in paragraph (3). Reading A (literal): the two increments are equal and the "increase or decrease" of paragraph (5) is nil whenever a modification period lies inside one part. Reading B: the change is measured against the increment regulation 12A(2) would give with its own rate (immediately before the end of the modification period). **Taken: A**, because B needs a baseline the text does not name; the steps are kept apart so a reviewer can swap the baseline. Asserted that the literal change is nil. The source does not answer what the change was meant to capture.

**F21. Regulation 22: an overseas resident in Great Britain or a specified territory.** Paragraph (2) covers a part during which the person was an overseas resident and was not in Great Britain or a specified territory; paragraph (3) a part during which the person was not an overseas resident. A part during which the person was an overseas resident who was in Great Britain or a territory specified in regulation 21(6) is in neither. Reading A: the Regulations do not say. Reading B: paragraph (3) by default, since the person was in Great Britain. **Taken: A**, naming the gap and asserting it.

**F22. Regulation 24(2) and a week that straddles 6 April 2016.** "Nothing in Chapter 3 is to be construed as entitling any person to be credited ... for any day ... before 6th April 2016." Reading A: a week is credited under Chapter 3 only if its first day is on or after 6 April 2016, because regulation 25(3) puts a week in the year it begins in and a week beginning before 6 April 2016 has days before it. Reading B: the credit is given for the week but only for its days on or after 6 April 2016. **Taken: A.** Tested on 3, 5 and 6 April 2016; every Chapter 3 rule calls the one gate.

**F23. Regulation 28(6) and 33(6): "in respect of a past period".** Reading A: the whole week is over before the day the application is received, so an application is received strictly after the week's last day (the first day plus six). Reading B: the week has begun. **Taken: A.** Tested on the last day of the week (out) and the day after (in).

**F24. Regulation 39(a)(i): "before the end of the year following that in which a week ... falls".** The year is a tax year ending on 5 April. Reading A: an application received on 5 April of that year is before its end (the year ends at the end of that day). Reading B: an application must be received before 5 April. **Taken: A.** Tested on 5 April 2028 (in) and 6 April 2028 (out) for a week in the year beginning 6 April 2026. Paragraph (b), regulation 35: "after the end of the year in which a week ... falls": from 6 April of the next year, with no upper bound, and no further-time allowance.

**F25. Regulation 37(5) and (8).** "Except in a case to which paragraph (8) applies, a person is not entitled to be credited ... under paragraph (2)(a) unless an application ... is received"; (8) describes a woman with a reduced rate election in force. Reading A (literal): for her, the application requirement does not apply, so she is credited under (2)(a) without one. Reading B: she is excluded from the credit altogether, as in regulations 30(3)(b) and 33(4)(b). **Taken: A.** Asserted; the source's drafting suggests B was intended, which a reviewer should confirm.

**F26. Regulation 38(1): the twelve weeks.** A week is counted by its first day. Reading A: for (a), a week whose first day falls in the 84 days ending on the day before entitlement begins; for (b) and (c), a week whose first day is one of the 84 days after the first day of the week in which entitlement or the satisfaction of regulation 37(2)(a) ends, starting seven days on. Reading B: whole weeks measured from the Sunday of a fixed national insurance week. **Taken: A**, which gives exactly twelve weeks when weeks are seven days apart, and needs no assumption about which day weeks begin.

**F27. Regulation 35(4)(b), "the Secretary of State is to exercise his discretion".** The text gives no rule. **Taken:** the result is the named member `the credit is left to the Secretary of State's discretion`, with no outcome encoded. Asserted.

## What the text turns out to say

Numbered findings. A finding ending **Asserted.** is held by an `#ASSERT` that is in the deposit; the file is named.

1. **A choice made before its period begins is not provided for (regulation 4).**
   The period for a choice is three months from the most recent notice, or, if no notice has been issued, from the later of claiming and the spouse's or civil partner's death to the day the choice is made (4(2), 4(3)); a late choice follows it (4(4)).
   Nothing says what happens to a choice made before that start.
   The encoding answers with a named result, `before the period begins, which the text does not provide for`, and regulation 18 passes it on as `the Regulations do not say, because the choice was made before its period began`.
   Fork F10.
   **Asserted.** (`spr-tests-part3.l4`, `spr-tests-part6.l4`, `spr-cases-seat.l4`)
2. **Regulation 22 gives no rule for an overseas resident who is in Great Britain or in a specified territory.**
   Paragraph (2) covers an overseas resident not in Great Britain or a specified territory; (3) covers a person who is not an overseas resident; the remaining person is in neither.
   The encoding names the result (`the Regulations do not say ...`) and gives no weekly rate (`NOTHING`) for it.
   Fork F21.
   **Asserted.** (`spr-tests-part7.l4`, `spr-cases-seat.l4`)
3. **Read literally, regulation 23 changes nothing.**
   Paragraph (4) has regulation 12A(2) read with the weekly rate of regulation 22(2) or (3) in place of its own, but 12A(2) already gives a percentage of that rate; so the "increase or decrease" of paragraph (5) is nil and the increment is the one regulation 22 gives.
   Whether the drafters meant something else (for instance a difference between the increment for a modification period and for an overseas part) is not decidable from the text.
   Fork F20.
   **Asserted.** (`spr-tests-part7.l4`, `spr-cases-seat.l4`)
4. **Regulation 37(8) takes a woman with a reduced rate election out of the application requirement, not out of the credit.**
   Paragraph (5) says an application is required "except in a case to which paragraph (8) applies", and (8) describes her; so, read literally, she is credited for 20 hours of caring without applying, and the more obvious reading (that she is excluded) would have said so.
   Fork F25.
   **Asserted.** (`spr-tests-part8-post2016.l4`, `spr-cases-seat.l4`)
5. **Regulation 35(4)(b) gives the Secretary of State a discretion and no rule.**
   Where more than one person could be credited for a week and those persons and the person awarded child benefit do not agree, "the Secretary of State is to exercise his discretion to determine which of those persons is to be credited".
   The encoding returns the named member `the credit is left to the Secretary of State's discretion`.
   Fork F27.
   **Asserted.** (`spr-tests-part8-post2016.l4`, `spr-cases-seat.l4`)
6. **After a remand, a later suspended sentence brings the withholding back (regulations 2 and 3).**
   A suspended sentence is a "described sentence" (3(2)(c)), so a person who was remanded and then given a suspended sentence is a prisoner for regulation 2(1), although a suspended sentence does not itself mean custody.
   The encoding follows the words.
   Fork F6.
   **Asserted.** (`spr-tests-part2.l4`, `spr-cases-seat.l4`)
7. **A week that begins on 1 to 5 April 2016 is a Chapter 2 week, never a Chapter 3 week.**
   Regulation 25(3) puts a week in the tax year in which it begins, so a week beginning before 6 April 2016 falls in the year ending 5 April 2016 (a pre-commencement year, regulations 26 to 28) and regulation 24(2) keeps it out of Chapter 3.
   Nothing falls between the two.
   Fork F22.
   **Asserted.** (`spr-tests-part8-general.l4`, `spr-tests-part8-post2016.l4`, `spr-cases-seat.l4`)
8. **Regulation 20(1)(e) and (f) are conditions only for those who have, or are barred from, a choice.**
   A survivor whose late spouse was entitled to an increase and was not deferred has no choice under regulation 18, so (e) and (f) are satisfied vacuously and (a) to (d) decide.
   Fork F18.
   **Asserted.** (`spr-cases-seat.l4`)
9. **When a survivor's choice becomes available is not stated (regulation 19(2)).**
   The text refers to "the date on which the person becomes entitled to make a choice under regulation 18" without giving it.
   The encoding takes the later of the day the survivor reaches pensionable age and the day the spouse or civil partner died, since regulation 18(1) needs both.
   Fork F16.
   **Asserted.** (`spr-tests-part6.l4`, `spr-cases-seat.l4`)
10. **If the full rate rises and an uprating order comes into force together, regulation 17(6) and (7) each apply.**
    Each increase is worked from the position before either event, and the two are added (neither paragraph says "after").
    Fork F15.
    **Asserted.** (`spr-tests-part6.l4`, `spr-cases-seat.l4`)
11. **The percentage that regulations 10, 12A and 22 refer to is one-ninth of 1 per cent, a fixed figure; the formula it feeds (section 17 of the 2014 Act) is not in the text.**
    The encoding reads section 17 as whole weeks of deferral, each earning an increment (fork F11); if section 17 works otherwise, the totals built on these rules would change, the rules themselves would not.

## Stated inputs (what the text defers to something not among the inputs)

Facts the text defers to something that is not among the inputs, and that each rule therefore takes as a plain input (never guessed); the places are named by module.
- **Pensionable age** and the date a person reaches it (these Regulations use it without defining it): `spr-part1-general`, `spr-part6-graduated`, `spr-part8-credits-post2016` (regulation 32).
- **Whether a person falls within section 8(1) of the 2014 Act**, and the amount of a lump sum under section 8(4); **section 17 of the 2014 Act** (the formula the percentages feed): `spr-part3-deferral`.
- **The weekly rate of the deceased's graduated retirement benefit** (regulation 16(5), from the graduated contributions paid, the 1965 Act and the up-rating orders), and the deceased's **increase in graduated retirement benefit** (regulation 20(5)): `spr-part6-graduated`.
- **The lump sum under paragraph 10 or 20 of Schedule 1 to the Social Security (Graduated Retirement Benefit) Regulations 2005** (regulation 19(1)): `spr-part6-graduated`.
- **Whether the survivor is entitled to a choice under section 8(2) of the 2014 Act** (regulation 18(8)), and **the rates of the other state pensions** under sections 2, 4, 7 and 12 (regulation 17): `spr-part6-graduated`.
- **Whether the Secretary of State "considers" something reasonable or appropriate** (regulations 4(4), 6(2)(c), 18(4), 34 to 39): a fact about an official's judgment, asked as an input: `spr-part3-deferral`, `spr-part6-graduated`, `spr-part8-credits-post2016`.
- **Whether a person is an overseas resident**, whether Regulations apply regulation 21 to an up-rating increase (21(2)(a)), and the weekly rate the person would have had if not deferred at the start and end of a part of the deferral period (regulation 22): `spr-part7-overseas`.
- **Qualifying years**: whether a tax year is one (section 2(4) of the 2014 Act), so the number of them is a plain input: `spr-part4-qualifying-years`.
- **The "relevant date"** (section 10(3) of the Family Law (Scotland) Act 1985) and **"shareable new state scheme rights"** (section 47(3) of "the 1999 Act", which these Regulations use without defining): `spr-part5-sharing`.
- **Credits under the 1975 Regulations** (a week's entitlement under regulation 7A, 7B, 8A, 8B or 9E), **the qualifying earnings factor**, **the lower earnings limit**, **the small profits threshold**, **whether a married woman's reduced rate election is in force** (section 19(4) of the 1992 Act), **ordinary residence**, **the relationship to the child** in regulation 35(6), **an approval as a foster parent**, **a relevant benefit**: `spr-part8-credits-general`, `spr-part8-credits-post2016`.
- **Dates**: the date the Regulations were made (9 February 2015, the text's own) and come into force (6 April 2016) are carried as values with `@ref`; no commencement order is needed.

## What the stable binary does not accept

**Silent: an unparenthesised `4%` as the last argument of a mixfix call.** A call written `(rule) 2.5 (the second keyword) 4% EQUALS 2.6` parses without any diagnostic and evaluates to a wrong number (0.125 where 2.6 was meant); `(4%)` is right. In a `JUST` the same mistake is loud (a type error). Every percentage argument in these modules is parenthesised.

**Loud (an error at the identifier): lower-case `ceiling` and `length`.**
Both give "I could not find a definition for the identifier".
Upper-case `CEILING` exists and works on the stable binary (`CEILING 2.5` is 3), and `count` gives a list's length.
`spr-part3-deferral.l4` rounds up as `0 MINUS FLOOR (0 MINUS x)`, which is the same number; it was written before `CEILING` was found, and was left as it was because it is tested and correct.

**Loud: mixfix heads.**
The parameters of a mixfix rule must be listed in the `GIVEN` in the order the head uses them; a different order was reported as an error and fixed in `spr-part6-graduated.l4`.
A zero-argument `WHERE` definition cannot be called with an argument.

**None of the constructs the brief lists as unsupported is used** (checked by search; this deposit did not test whether the binary rejects each): no `REFUSE`, no `#ASSERT REFUSED`, no `BECAUSE`, no `TYPICALLY`, no section `GIVEN`, a local `YMD` shim (`spr-nouns.l4`), every `NOT` parenthesised, every `#ASSERT` on one line, arithmetic bracketed across line breaks, `IMPORT` only of modules in the same folder.
A parameter that has the same name as a record field is accepted by the binary (probed), but every seat input was nevertheless checked by script to differ from every field, rule and constructor name in the layer-1 modules: none does.

## What check.sh prints

Run on 2026-10-22 with the stable `l4` 1.6.98 (path and sha256 in `encoding.json`), after the last edit to any `.l4` file, as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` from this folder (exit status 0).
`check.sh` is the skill's script (`encoding-a-subject`, `assets/check.sh`) plus two columns and two extra ways to be red: `warn` counts `DiagnosticSeverity_Warning` lines and any warning makes the run red; `written` counts lines that begin `#ASSERT`, and a module whose written assertions are not all reported as satisfied, failed or refused is red (an assertion written but never reported would otherwise be skipped silently).
The script does not read `L4_TARGET`; it was set only because the brief asks for it.
`JL4_LIBRARY_PATH` was left unset.

```
module                                    errors  warn written satisfied  failed  refused  expected
spr-cases-seat.l4                              0     0     325       325       0        0         0
spr-nouns.l4                                   0     0       0         0       0        0         0
spr-part1-general.l4                           0     0       0         0       0        0         0
spr-part2-prisoners.l4                         0     0       0         0       0        0         0
spr-part3-deferral.l4                          0     0       0         0       0        0         0
spr-part4-qualifying-years.l4                  0     0       0         0       0        0         0
spr-part5-sharing.l4                           0     0       0         0       0        0         0
spr-part6-graduated.l4                         0     0       0         0       0        0         0
spr-part7-overseas.l4                          0     0       0         0       0        0         0
spr-part8-credits-general.l4                   0     0       0         0       0        0         0
spr-part8-credits-post2016.l4                  0     0       0         0       0        0         0
spr-seat.l4                                    0     0       0         0       0        0         0
spr-tests-part1.l4                             0     0      23        23       0        0         0
spr-tests-part2.l4                             0     0      34        34       0        0         0
spr-tests-part3.l4                             0     0     115       115       0        0         0
spr-tests-part4.l4                             0     0       9         9       0        0         0
spr-tests-part5.l4                             0     0      15        15       0        0         0
spr-tests-part6.l4                             0     0      94        94       0        0         0
spr-tests-part7.l4                             0     0      36        36       0        0         0
spr-tests-part8-general.l4                     0     0      49        49       0        0         0
spr-tests-part8-post2016.l4                    0     0     165       165       0        0         0
TOTAL (21 modules)                             0     0     865       865       0        0
(a failed assertion is also an error; any other error, any warning, any refused assertion, or any written assertion not reported makes the run red)
```

And the source-reference check, `python3 -I srcrefs.py check --refs uksi-2015-173.txt spr-*.l4`:

```
srcrefs check: 470 src: lines, 103 runs, 140 locators, 0 problems
```

The 21 files are the 10 layer-1 modules, the 9 test files, and the 2 seat files; the 865 assertions are the 540 of the layer-1 tests plus the 325 of `spr-cases-seat.l4`.

## What would need doing before the encoding is worth relying on

1. **A domain expert has to read it against the official text.**
   The source is a converter's plain-text rendering of legislation.gov.uk (version 2026-04-06), not the official text, and it "may carry more than one extent version of a provision" (the converter's own caveat); every `src:` quotation in the modules is copied from that rendering by script and checks against it, not against the official page.
   Nobody has compared the rendering with the official text, and nobody has read the encoding against either.
2. **The forks need a ruling.**
   Twenty-eight readings were taken (F1 to F27 and F9b), each with the reading not taken; the ones that move an answer a person would notice are F2 (civil partners and regulation 1(5)), F6 (suspended sentence after remand), F7 and F8 (how "starting on" counts), F10 (a choice before its period), F14 (a death on the day the survivor reaches pensionable age), F16 (the date a choice becomes available), F18 (regulation 20(1)(e), (f)), F20, F21, F22, F24, F25 and F27.
   A lawyer should rule on those before any of the corresponding answers is relied on.
3. **The parent legislation is not encoded.**
   Every figure and test that the text takes from the Pensions Act 2014 (entitlement and rates, section 17's formula, who is an overseas resident), the 1975 Regulations, the 1992 Act, the 1965 Act and the 2005 Regulations is a stated input, asked of the person.
   An answer is only as good as those inputs; the seat asks for them in plain words but cannot check them.
4. **The full rate and other figures are those of one version.**
   The full rate (241.30 pounds a week, regulation 1A) and the dates in the text are as at 6 April 2026; a later version of the instrument changes them, and the encoding has to be regenerated from it.
5. **The seat is a draft form.**
   Its wording was written from the position of the person, not tested on one; the longer lists (more than one notice, more than two changes in the weekly rate, more than two persons cared for) are asked as one or two entries, and the layer-1 rules take any number.
   The questions that ask for a decision of an official (for instance "does the Secretary of State consider it reasonable") are asked as facts; a form would normally ask first whether the person has been told.
6. **It runs on the stable build only.**
   The checks below are those of `l4` 1.6.98; `L4_TARGET=unstable` was set when `check.sh` ran, but the script does not read it and no unstable build was tried.
   Nothing here depends on an unstable-only construct.
7. **Layer 1 and layer 2 have not been through an independent test author.**
   All the assertions were written by the encoder.
   On the first run of the hand-written seat cases, two places disagreed with the encoding, and both were slips in the case, not in the encoding (an arithmetic slip in a "later of" case, and a helper default that left out "it is paid to me" for a single person; PROGRESS.md has the detail); they were corrected, which shows the cases do bite and also that they are not independent evidence.
