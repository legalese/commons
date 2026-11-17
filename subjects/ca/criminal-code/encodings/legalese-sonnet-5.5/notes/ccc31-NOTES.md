# NOTES.md -- part ccc31 of the Criminal Code (Canada), R.S.C., 1985, c. C-46: lines 18464-19055 (Forms 24 to 54 and the heading RELATED PROVISIONS)

Status (written 2026-11-13 by part agent `ccc31`, Claude Sonnet 5.5): written after the modules; every number below was produced by a command run in this session (`check.sh`, `work/coverage.py`, `work/verify-quotes.py`, `srcrefs.py`) and the check output is pasted at the end, not retyped.
The target is the stable `l4` (1.6.110, `main`, e51181d, 2026-11-11) checked against a second stable build (1.6.109, 4c887e0): `check.sh` compares the two.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30).
It is not the official text, and nothing here is claimed verified against the official text.
The French version is equally authoritative and is not among the sources.

Where PLAN.md and the brief differ, the brief governs.
The one place they differ is the plan's row for ccc31, which says "sections 1 to 9 (38 section headings)": the range holds no sections.
It holds the 38 FORM headings from FORM 24 to FORM 54 (counted by script: 38 lines beginning `FORM `) and the heading RELATED PROVISIONS, and "1 to 9" are the Forms' own internal numbered paragraphs (Forms 51 to 54) and parts (Form 32).
The names below are therefore labelled `form N ...`, never `s N ...`: `s 1` belongs to the keel, and the sections the Forms cite (550, 708, 827 ...) belong to other parts (Finding 1).

## What is encoded and what is not

Everything in lines 18464-19055 has a row in the coverage table below and one disposition: no row is `out-of-scope` or `deferred`.
A Form is encoded only where its text states a command, an authorization, a condition, a period, a right, a prohibition or a consequence.
What a Form shows and does not say is wording only: the caption (Canada, Province, territorial division), the identification of the person, the dating, signing and sealing lines, the declarant's boxes of wishes, the records of a conviction or an acquittal, and the certificates (Forms 31, 33, 36, 37, 38, 42, 43, 44, 45).
Each such row says in its own words what makes it wording, so that a reviewer can disagree row by row.
A recital that is the ground of a command ("Whereas ... This is therefore to direct you") is not wording: it is the premise of the command's function (fork F18).
Not in this range: every Form before FORM 24 (part ccc30), the related and transitional provisions after the heading (part ccc32), and every section of the Code (other parts).

Layer 1 is six modules (`ccc31-forms-periods`, `-custody`, `-process`, `-statements`, `-orders`, `-soira`) and six test files (`ccc31-tests-periods`, `-custody`, `-process`, `-statements`, `-orders`, `-soira`); layer 2 is `ccc31-seat.l4` and `ccc31-cases-seat.l4`.
Two of the six modules, and their tests, were written by small scripts in `work/` (not shipped) because the Forms repeat their own shape: `ccc31-forms-statements.l4` (Forms 34.2, 34.3 and 48.2 are one Form three times) and `ccc31-forms-soira.l4` (Forms 52, 53 and 54), with `ccc31-tests-soira.l4` and the seat and its cases.
The expected value of every test is written in those scripts by hand from the text, before any run.

## Seat

The seat is a person who is, or may be, accused of an offence under the Code, asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction (assumed, not ruled: Singapore's Penal Code is the model, per the maintainer's instruction of 2026-11-09, but this is a plain seat layer; no charge-generator contract).
This range holds the prescribed Forms, so the questions it answers for that person are what a warrant, an order, a recognizance, a notice or a statement in a Form says about them: whether they may be held and for how long, what they must do and by when, what rights the Form gives them, and what may follow if they do not comply.
There is never a seat for an official: the keeper, the sheriff, the justice and the Review Board appear only as what their duties and powers mean for the person.
`ccc31-seat.l4` asks 56 questions in seven `§` groups, in the order of the Forms; each has `@export` and `@desc` on every input.
Several groups arise only in a situation the person may not be in (held in custody, endorsed, on probation, served with a notice): the group's comment says which, so that the form can ask "Has this happened to you?" first.

Departures from the brief, recorded here so that a reviewer can overrule them:
- **The names of the seat questions.** The brief says to begin every question "Under section N," or "Under schedule N paragraph M,". A Form is neither, and its numbering (Form 24, paragraph 2) is the Act's own, so the questions begin "Under Form N," or "Under Form N paragraph M,". Some Forms are prescribed for several sections (Form 32 for fifteen), so naming the question by one of them would claim a scope the answer does not have.
- **MAYBE answers.** Every seat question answers a `MAYBE` (50 `MAYBE BOOLEAN`, one `MAYBE NUMBER`, one `MAYBE DATE`, four `MAYBE STRING`), so that "not covered" is `null` and never `false`; the head comment of the seat says how to read it.
- **Seam answers asked as plain facts.** The seat cannot ask a person for "the answer of s 522"; it asks the fact (is the offence one mentioned in s 522?) and passes `JUST` of it. Where the person does not know, they answer false, and the result must be read with care: the seat comment says so.
- **A question with no fact to ask.** Three questions ("Under Form 34.2 / 34.3 / 48.2, is the statement an application for compensation or restitution") ask nothing the person knows, because the Form answers them flatly ("this is not an application"). Each takes one yes/no input, "I ask the question", so that the form has an input to show; answering false gives `null`.
- **Choices written as short strings.** Where a Form lets the court tick one of several alternatives (Form 25 (a) to (c), Form 35, Form 46 (a) to (g), the List of Conditions), the seat asks which alternative with a short string ("a", "b" ...) and the `@desc` lists the allowed values; any other string answers `null`.

### Reading a result: FALSE and NOTHING (ccc31)

Every decision function of layer 1 answers `MAYBE BOOLEAN`; a few answer a `MAYBE` of a type of their own (a period, a surety-declaration box, a consequence) or a `MAYBE NUMBER`, and the date function answers a `DATE`.
- `JUST TRUE`: on the facts given, the Form's words reach the case. For a "may" in the Form ("may be forfeited", "you may be subject to") it means the Form says it may happen, a liability and not a certainty.
- `JUST FALSE`, a "no": the Form says no in its own words. In this range that means: an "unless" once met (payment, a recognizance entered), an "until" once reached (the trial, delivery by due course of law), a period that has run or has not begun (a term of imprisonment, a probation period, "in force for a total of ___ days", a reporting period), an "if", "while" or "whenever" that fails (an "if a verdict ... has been rendered", "whenever required under section 4.1 or 4.3"), a flat negative ("must not include", "this is not an application", "not earlier than", "not less than seven"), and a bare "must" not done (the duty is not met: fork F5). Every such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- A function named for a grant or a power ("may be forfeited", "may ask", "may apply") whose "if" gate fails answers `NOTHING`, not `JUST FALSE`, unless the text closes the gate itself ("only if", "must not ... except", "not earlier than"): forks F4 and F20 to F25, the sweep of the marginal readings.
- `NOTHING`, "not covered": a premise the Form recites is not made out ("Whereas ... This is therefore"), a grant or command limited by its own wording and the case outside the limit ("within the (territorial division)", "to one of the following police officers"), a list given without "only" (the sections after each condition of Form 32, the examples in a victim impact statement), a term the Form borrows from another section or Act whose answer is an input and is not JUST TRUE, or the Form is silent. Every such branch carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller must never turn `NOTHING` into `FALSE`. In particular a seam answer that is not `JUST TRUE` (for example `s 2 peace officer` answering `JUST FALSE`) gives `NOTHING` here, not `JUST FALSE` (fork F19).
- `REFUSE` is not used (the stable line has none, by the brief): "not covered" is `NOTHING`, asserted with `EQUALS NOTHING`.
- Mechanical checks: `work/verify-quotes.py` checks that every branch answering `NOTHING` has a tag from the six, every branch answering `JUST FALSE` has a FALSE-kind tag with a quotation, and that every quoted fragment occurs, in order, in the text of the range.

## Method: what is a rule in a Form (assumed, not ruled)

The brief says a Form that only prescribes the wording of a document is machinery unless its text states a rule.
The line was drawn by one test, applied sentence by sentence: does the sentence carry an "unless", "until", "if", "while", "whenever", "for the term of", "for a period of", "must", "must not", "may", "you have the right", "authorize", "direct", "command", or a consequence?
If so it is encoded; if it only names, dates, identifies, signs or ticks, it is wording.
Two rows are close calls and are encoded, not left inert: the "Whereas" recitals (they are the grounds of a command: fork F18) and the Form 32 paragraphs where the signatory "understands" a consequence (they state the consequence).
Three declarations of the signatory's own agreement in Form 32 ("I agree to (promise or deposit) the amount", "I understand my role ... and I agree to act as a surety") are left inert (reason 2): they carry no condition, period or consequence, and the consequence of failing is the next line, which is encoded.

### Seat questions (ccc31), in the order of the Forms

Each question and the layer-1 rule its body calls (the seat restates none); the answer is a `MAYBE` of the type shown.

1. `Under Form 24, is the keeper directed to keep the witness who would not enter into the recognizance in custody until my trial` -- calls `form 24 the keeper is directed to keep the witness in custody`; answers `MAYBE BOOLEAN`.
2. `Under Form 25, am I still to be kept in custody under the warrant of committal for contempt` -- calls `form 25 the keeper is ordered to keep the defaulter in custody`; answers `MAYBE BOOLEAN`.
3. `Under Form 25, does the warrant protect the keeper who keeps me in custody as the order directs` -- calls `form 25 this is a sufficient warrant for the keeper`; answers `MAYBE BOOLEAN`.
4. `Under Form 26, am I still to be kept in custody for not paying the costs of an appeal` -- calls `form 26 the keeper is commanded to keep the defaulter in custody`; answers `MAYBE BOOLEAN`.
5. `Under Form 27, am I still to be kept in custody for the forfeiture of an amount` -- calls `form 27 the keeper is ordered to keep the defaulter in custody`; answers `MAYBE BOOLEAN`.
6. `Under Form 30, is the keeper to have me before the justice at the time and place stated` -- calls `form 30 the keeper is directed to have the accused before the justice`; answers `MAYBE BOOLEAN`.
7. `Under Form 35, am I still to be imprisoned in default of paying the sums in my conviction` -- calls `form 35 the imprisonment in default of payment still applies`; answers `MAYBE BOOLEAN`.
8. `Under Form 39, must the keeper release me` -- calls `form 39 the keeper is directed to release the person`; answers `MAYBE BOOLEAN`.
9. `Under Form 49, am I to be kept in custody until I am delivered by due course of law` -- calls `form 49 the keeper is directed to keep the accused in custody`; answers `MAYBE BOOLEAN`.
10. `Under Form 49, must I comply with a condition of the warrant while I am in the hospital or other place` -- calls `form 49 the accused is subject to the condition`; answers `MAYBE BOOLEAN`.
11. `Under Form 50, is the keeper commanded to execute the warrant of committal as the Review Board has decided` -- calls `form 50 the keeper is commanded to execute the warrant`; answers `MAYBE BOOLEAN`.
12. `Under Form 28, may I be arrested in the territorial division the endorsement names` -- calls `form 28 the endorsement authorizes the arrest of the accused`; answers `MAYBE BOOLEAN`.
13. `Under Form 29, does the endorsement authorize my release under section 499 on this endorsed warrant` -- calls `form 29 the endorsement authorizes the release of the accused under section 499`; answers `MAYBE BOOLEAN`.
14. `Under Form 29.1, may I, a witness arrested on a warrant, be released on the endorsement` -- calls `form 29.1 the endorsement authorizes the release of the witness`; answers `MAYBE BOOLEAN`.
15. `Under Form 32 part 2, may the amount or security I promised or deposited be forfeited` -- calls `form 32 part 2 the amount or security may be forfeited`; answers `MAYBE BOOLEAN`.
16. `Under Form 32 part 3, does my recognizance list the conditions ordered and how long each lasts` -- calls `form 32 part 3 the recognizance lists the conditions ordered and the duration of each`; answers `MAYBE BOOLEAN`.
17. `Under Form 32 part 4, may I apply to a judge or justice to cancel or vary a condition of my recognizance` -- calls `form 32 part 4 the person may apply to cancel or vary a condition`; answers `MAYBE BOOLEAN`.
18. `Under Form 32 part 5, are the conditions of my recognizance still in effect` -- calls `form 32 part 5 the conditions remain in effect`; answers `MAYBE BOOLEAN`.
19. `Under Form 32 part 6, must I comply with a condition listed in my recognizance` -- calls `form 32 part 6 the person must comply with the condition`; answers `MAYBE BOOLEAN`.
20. `Under Form 32 part 6, may the money my surety promised or deposited be forfeited` -- calls `form 32 part 6 the money the surety has promised or deposited may be forfeited`; answers `MAYBE BOOLEAN`.
21. `Under Form 32, is a condition in the List of Conditions one the Form lists for this section` -- calls `form 32 the condition is listed for the section`; answers `MAYBE BOOLEAN`.
22. `Under Form 34, how much is the sheriff still commanded to levy from my goods and lands` -- calls `form 34 the amount the sheriff is commanded to levy from the person`; answers `MAYBE NUMBER`.
23. `Under Form 40, is my challenge to the array of the panel of jurors on this ground in the Form's terms` -- calls `form 40 the challenge to the array is in the Form's terms`; answers `MAYBE BOOLEAN`.
24. `Under Form 41, is my challenge to a juror for cause on this ground in the Form's terms` -- calls `form 41 the challenge for cause is in the Form's terms`; answers `MAYBE BOOLEAN`.
25. `Under Form 34.1, may a victim claim this loss from me as restitution` -- calls `form 34.1 the loss may be claimed as restitution`; answers `MAYBE BOOLEAN`.
26. `Under Form 34.2, may a victim impact statement include this content` -- calls `form 34.2 the statement may include the item`; answers `MAYBE BOOLEAN`.
27. `Under Form 34.2, is a victim impact statement an application for compensation or restitution` -- calls `form 34.2 this is an application for compensation or restitution`; answers `MAYBE BOOLEAN`.
28. `Under Form 34.3, may a community impact statement include this content` -- calls `form 34.3 the statement may include the item`; answers `MAYBE BOOLEAN`.
29. `Under Form 34.3, is a community impact statement an application for compensation or restitution` -- calls `form 34.3 this is an application for compensation or restitution`; answers `MAYBE BOOLEAN`.
30. `Under Form 48.2, may a victim impact statement for a person found not criminally responsible include this content` -- calls `form 48.2 the statement may include the item`; answers `MAYBE BOOLEAN`.
31. `Under Form 48.2, is a victim impact statement for a person found not criminally responsible an application for compensation or restitution` -- calls `form 48.2 this is an application for compensation or restitution`; answers `MAYBE BOOLEAN`.
32. `Under Form 46, on what date do the conditions of my probation order begin` -- calls `form 46 the conditions begin on`; answers `MAYBE DATE`.
33. `Under Form 46, do the conditions of my probation order bind me on this day` -- calls `form 46 the offender must comply with the conditions on the day`; answers `MAYBE BOOLEAN`.
34. `Under Form 46, am I in compliance with the standing conditions of my probation order` -- calls `form 46 the offender is in compliance with the standard conditions`; answers `MAYBE BOOLEAN`.
35. `Under Form 47, does an order made on these grounds authorize and require the disclosure of my income tax information` -- calls `form 47 the order authorizes and requires the addressee to produce the information`; answers `MAYBE BOOLEAN`.
36. `Under Form 51 paragraph 1, is the first day I am told to report to give a sample a permitted day` -- calls `form 51 para 1 the first report is on a permitted day`; answers `MAYBE BOOLEAN`.
37. `Under Form 51 paragraph 2, must I report to give a sample on this day` -- calls `form 51 para 2 the person must report on the day`; answers `MAYBE BOOLEAN`.
38. `Under Form 51 paragraph 3, may I apply to a court to end the obligation to provide samples` -- calls `form 51 para 3 the person may apply to terminate the obligation`; answers `MAYBE BOOLEAN`.
39. `Under Form 51 paragraph 4, what may follow if I do not comply with the obligation to provide samples` -- calls `form 51 para 4 the consequence of not complying`; answers `MAYBE STRING`.
40. `Under Form 48, does the court have grounds to order an assessment of my mental condition for this purpose` -- calls `form 48 the court has grounds to order an assessment for the purpose`; answers `MAYBE BOOLEAN`.
41. `Under Form 48, is the assessment order of the court still in force on this day` -- calls `form 48 the order is in force`; answers `MAYBE BOOLEAN`.
42. `Under Form 48, must I comply with a condition of the assessment order of the court` -- calls `form 48 the accused must comply with the condition`; answers `MAYBE BOOLEAN`.
43. `Under Form 48.1, does the Review Board have grounds to order an assessment of my mental condition for this purpose` -- calls `form 48.1 the Review Board has grounds to order an assessment for the purpose`; answers `MAYBE BOOLEAN`.
44. `Under Form 48.1, is the assessment order of the Review Board still in force on this day` -- calls `form 48.1 the order is in force`; answers `MAYBE BOOLEAN`.
45. `Under Form 52 paragraph 2, for how many years must I report to the registration centre` -- calls `form 52 para 2 the period for which the person must report`; answers `MAYBE STRING`.
46. `Under Form 52 paragraph 2, must I report to the registration centre on this day` -- calls `form 52 para 2 the person must report on the day`; answers `MAYBE BOOLEAN`.
47. `Under Form 52 paragraph 6, may I apply to a court to end my duty to comply with the Sex Offender Information Registration Act` -- calls `form 52 para 6 the person may apply to terminate the order`; answers `MAYBE BOOLEAN`.
48. `Under Form 52 paragraph 7, may I be fined or imprisoned if I do not comply` -- calls `form 52 para 7 the consequence of contravening the order`; answers `MAYBE BOOLEAN`.
49. `Under Form 53 paragraph 2, for how many years must I report to the registration centre` -- calls `form 53 para 2 the period for which the person must report`; answers `MAYBE STRING`.
50. `Under Form 53 paragraph 2, must I report to the registration centre on this day` -- calls `form 53 para 2 the person must report on the day`; answers `MAYBE BOOLEAN`.
51. `Under Form 53 paragraph 7, may I apply to a court to end my duty to comply with the Sex Offender Information Registration Act` -- calls `form 53 para 7 the person may apply to terminate the obligation`; answers `MAYBE BOOLEAN`.
52. `Under Form 53 paragraph 8, may I be fined or imprisoned if I do not comply` -- calls `form 53 para 8 the consequence of contravening the obligation`; answers `MAYBE BOOLEAN`.
53. `Under Form 54 paragraph 2, for how many years must I report to the registration centre` -- calls `form 54 para 2 the period for which the person must report`; answers `MAYBE STRING`.
54. `Under Form 54 paragraph 2, must I report to the registration centre on this day` -- calls `form 54 para 2 the person must report on the day`; answers `MAYBE BOOLEAN`.
55. `Under Form 54 paragraph 7, may I apply to a court to end my duty to comply with the Sex Offender Information Registration Act` -- calls `form 54 para 7 the person may apply to terminate the obligation`; answers `MAYBE BOOLEAN`.
56. `Under Form 54 paragraph 8, may I be fined or imprisoned if I do not comply` -- calls `form 54 para 8 the consequence of not complying`; answers `MAYBE BOOLEAN`.

### Seat audit of 2026-11-12

Requested by the lead after a direction/subject defect class was found in a sister encoding: a seat question whose name asks one thing while the layer-1 function it returns answers another.
All 56 seat questions were read, each name and `@export` text against the function its body calls (the list above gives the pairs).
**Direction mismatches (a permission title over a bar, or the reverse): 0.** No layer-1 function of this part answers a bar; every function answers the Form's positive limb, and the questions that ask the negative limb ask it as such ("may I be fined ... if I do not comply", "is the first day ... a permitted day").
**Subject mismatches: 9** (the question named a right, a permission or a premise that the function does not answer). Each was retitled, with its `@export` text where that spoke of the old subject; the inputs, their `@desc`s and the answers did not change, and no answer was negated (a function's `NOTHING` is not a grant or a bar).
The 39 assertions of `ccc31-cases-seat.l4` that call these nine questions were restated in place with `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>`; facts and expected values are unchanged.

| was | now | what the function answers |
| --- | --- | --- |
| Under Form 24, may the witness who would not enter into the recognizance be kept in custody until my trial | Under Form 24, is the keeper directed to keep the witness who would not enter into the recognizance in custody until my trial | `form 24 the keeper is directed to keep the witness in custody`: a direction, not a permission |
| Under Form 29, am I to be released under section 499 on this endorsed warrant | Under Form 29, does the endorsement authorize my release under section 499 on this endorsed warrant | `form 29 the endorsement authorizes the release of the accused under section 499`: an authorization, not an entitlement |
| Under Form 34, how much may the sheriff still levy from my goods and lands | Under Form 34, how much is the sheriff still commanded to levy from my goods and lands | `form 34 the amount the sheriff is commanded to levy from the person`: a command, not a permission |
| Under Form 40, may I challenge the array of the panel of jurors on this ground | Under Form 40, is my challenge to the array of the panel of jurors on this ground in the Form's terms | `form 40 the challenge to the array is in the Form's terms`: whether the challenge is in the Form's terms, not whether the right exists |
| Under Form 41, may I challenge a juror for cause on this ground | Under Form 41, is my challenge to a juror for cause on this ground in the Form's terms | `form 41 the challenge for cause is in the Form's terms`: as for Form 40 |
| Under Form 34.1, may a victim claim restitution from me for a loss whose amount the court cannot readily ascertain | Under Form 34.1, may a victim claim this loss from me as restitution | `form 34.1 the loss may be claimed as restitution`: the old title fixed the premise that the amount cannot be ascertained, while the function answers both cases |
| Under Form 47, may an order require the disclosure of my income tax information | Under Form 47, does an order made on these grounds authorize and require the disclosure of my income tax information | `form 47 the order authorizes and requires the addressee to produce the information`: what an order made on the recitals says, not a power of the court |
| Under Form 48, may the court order an assessment of my mental condition for this purpose | Under Form 48, does the court have grounds to order an assessment of my mental condition for this purpose | `form 48 the court has grounds to order an assessment for the purpose`: the grounds the Form recites, not the power |
| Under Form 48.1, may the Review Board order an assessment of my mental condition for this purpose | Under Form 48.1, does the Review Board have grounds to order an assessment of my mental condition for this purpose | `form 48.1 the Review Board has grounds to order an assessment for the purpose`: as for Form 48 |

Read and left as they are: "must I comply with a condition of the warrant while I am in the hospital" (Form 49) over `the accused is subject to the condition` ("shall be subject": the same status), and "am I to be kept in custody" / "is the keeper to have me before the justice" / "must the keeper release me" over the Forms' "directed", "ordered" and "commanded" functions (the same direction).
The seat's head comment and the `@export` texts already said "true = the keeper is directed ..." where they now ask it.
Counts after the audit: 56 questions, 56 `@export`s, 232 cases, 232 assertions satisfied (unchanged).

## Coverage (ccc31)

One row per unit of lines 18464-19055: every Form heading, every part of a Form that states or recites something (the command, the recital, the paragraph, the box, the bullet, the table row) and every caption and signing line, each with exactly one disposition and the L4 name that encodes it.
Built by `work/coverage.py` from the text; the script checks that every non-blank line of the range is in exactly one row.

Audit (counted by script, `work/build-notes.py`): the range has 592 lines, 551 of them non-blank. The text units counted by a pattern at the start of a line are 196 (38 Form headings (lines beginning FORM); 33 lettered paragraphs "(a)", "(e.1)" at the start of a line; 38 numbered paragraphs "1 ", "6.1 " of Forms 51 to 54 and Form 32 parts; 27 boxes at the start of a line; 60 bullets "•" and "–"). The table had 323 rows when first drafted and has 323 now: the three rows for the signatories' own agreements in Form 32 (lines 18579, 18594, 18595) changed disposition from `encoded` to `inert`, and the count did not change. Non-blank lines in no row: 0; in more than one row: 0.

By disposition: 153 `encoded`, 37 `fork` (a reading was chosen: the row points at the entry of the fork register and at the rule that encodes it), 44 `inert` reason 1 (headings), 88 `inert` reason 2 (the wording of a document), 0 `inert` reason 3, 1 `repealed or blank in this text` (Form 28.1, line 18527).
The distinct L4 names cited by the table are all defined (checked: `python3 -I work/coverage.py --names` reports none missing).

| row | lines | disposition | L4 name | what the text shows |
| --- | --- | --- | --- | --- |
| F24-h | 18464 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F24-cap | 18465-18467 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F24-addr+cmd | 18468 | encoded | `form 24 the peace officers are directed to arrest and convey the witness` | the warrant is addressed to the peace officers in the territorial division and to the keeper of the prison |
| F24-rec1 | 18469 | encoded | `form 24 the peace officers are directed to arrest and convey the witness` | recital that the accused was committed for trial: a premise of the direction |
| F24-rec2 | 18470 | encoded | `form 24 the peace officers are directed to arrest and convey the witness` | recital that the witness appeared at the preliminary inquiry, was required to enter into a recognizance and failed or refused: premises of the direction |
| F24-cmd | 18471 | encoded | `form 24 the peace officers are directed to arrest and convey the witness`; `form 24 the duties of the peace officers and the keeper` | the direction to arrest, if necessary, take and convey the witness to the prison and deliver them to the keeper with the precept |
| F24-precept | 18472 | fork | `form 24 the keeper is directed to keep the witness in custody` | fork F1 (an "unless" once met): the keeper keeps the witness until the trial, unless before that time the witness enters into the recognizance |
| F24-sig | 18473-18474 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F25-h | 18476 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F25-cap | 18477-18479 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F25-addr | 18480 | encoded | `form 25 the peace officers are ordered to arrest and convey the defaulter` | the warrant is addressed to the peace officers in the territorial division and to the keeper of the prison |
| F25-rec1 | 18481 | encoded | `form 25 the peace officers are ordered to arrest and convey the defaulter` | recital: conviction for contempt for not attending to give evidence although subpoenaed or bound by recognizance, with no sufficient excuse: premises of the order |
| F25-rec2 | 18482 | encoded | `form 25 the peace officers are ordered to arrest and convey the defaulter` | recital: the punishment ordered after the conviction: a premise of the order |
| F25-rec3 | 18483 | encoded | `form 25 the peace officers are ordered to arrest and convey the defaulter` | recital that the defaulter has not paid the amounts ordered ("delete if not applicable"): a premise only where amounts were ordered |
| F25-cmd | 18484 | encoded | `form 25 the peace officers are ordered to arrest and convey the defaulter`; `form 25 the duties of the peace officers and the keeper` | the order to arrest, if necessary, take and convey the defaulter to the prison and deliver them to the keeper |
| F25-keeper | 18485 | encoded | `form 25 the keeper is ordered to keep the defaulter in custody`; `form 25 this is a sufficient warrant for the keeper` | the order to receive and keep the defaulter, and "for so doing this is a sufficient warrant"; the asterisk after "there" has no footnote in this text (finding) |
| F25-a | 18486 | encoded | `form 25 the keeper is ordered to keep the defaulter in custody` | (a) for the term of ___ |
| F25-b | 18487 | fork | `form 25 the keeper is ordered to keep the defaulter in custody` | (b) for the term of ___, unless the sums and the costs and charges are sooner paid: fork F1 (an "unless" once met) |
| F25-c | 18488 | fork | `form 25 the keeper is ordered to keep the defaulter in custody` | (c) two terms, "unless the sums ... are sooner paid": fork F2 (which term the "unless" reaches) |
| F25-sig | 18489-18491 | inert (reason 2) | - | the date, place and signature lines; wording only and the seal |
| F26-h | 18493 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F26-cap | 18494-18496 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F26-addr | 18497 | encoded | `form 26 the peace officers are commanded to take and convey the defaulter` | the warrant is addressed to the peace officers of the territorial division and to the keeper of the prison |
| F26-rec1 | 18498 | encoded | `form 26 the peace officers are commanded to take and convey the defaulter` | recital: on the hearing of an appeal it was adjudged that the defaulter pay costs to the Clerk of the Court: a premise |
| F26-rec2 | 18499 | encoded | `form 26 the peace officers are commanded to take and convey the defaulter` | recital: the Clerk of the Court has certified that the defaulter has not paid within the time limited: a premise |
| F26-cmd | 18500 | encoded | `form 26 the peace officers are commanded to take and convey the defaulter`; `form 26 the duties of the peace officers and the keeper` | the command to the peace officers to take the defaulter and safely convey and deliver them to the keeper with the precept |
| F26-keeper | 18501 | fork | `form 26 the keeper is commanded to keep the defaulter in custody`; `form 26 this is a sufficient warrant for the keeper` | the command to receive and imprison for the term, "unless the said sum and the costs and charges ... are sooner paid", and "for so doing this is a sufficient warrant": fork F1 (an "unless" once met) |
| F26-sig | 18502-18503 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F27-h | 18505 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F27-cap | 18506-18508 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F27-addr | 18509 | encoded | `form 27 the sheriff is ordered to arrest and convey the defaulter` | the warrant is addressed to the sheriff of the territorial division and to the keeper of the prison |
| F27-issued | 18510 | encoded | `form 27 the sheriff is ordered to arrest and convey the defaulter` | the warrant is issued for the arrest of the named defaulter or defaulters |
| F27-cmd | 18511 | encoded | `form 27 the sheriff is ordered to arrest and convey the defaulter`; `form 27 the duties of the sheriff and the keeper` | the order to arrest the defaulter(s), convey them safely to the prison and deliver them to the keeper with the order |
| F27-keeper | 18512 | fork | `form 27 the keeper is ordered to keep the defaulter in custody` | the order to keep the defaulter "for a period of ___ or until satisfaction is made of a judgment debt": fork F3 (which comes first); the debt is due to Her Majesty for forfeiture of an amount set out in an undertaking, release order or recognizance |
| F27-sig | 18513-18516 | inert (reason 2) | - | the date, place and signature lines; wording only, the name of the judge who issued it, and the seal |
| F28-h | 18518 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F28-cap | 18519-18521 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F28-auth | 18522 | encoded | `form 28 the endorsement authorizes the arrest of the accused` | the justice authorizes, in accordance with the application, the arrest of the accused within the territorial division |
| F28-sig | 18523-18524 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F28.1-h | 18526 | inert (reason 1) | - | the heading of Form 28.1, which has no title in this text |
| F28.1-rep | 18527 | repealed or blank in this text | - | the text shows "[Repealed, 2007, c. 22, s. 26]" |
| F29-h | 18529 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F29-cap | 18530-18532 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F29-auth | 18533 | encoded | `form 29 the endorsement authorizes the release of the accused under section 499` | where the warrant is issued under s 507, 508 or 512 for an offence other than one mentioned in s 522, the justice authorizes the release of the accused under s 499 |
| F29-sig | 18534-18535 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F29.1-h | 18537 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F29.1-cap | 18538-18540 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F29.1-auth | 18541 | encoded | `form 29.1 the endorsement authorizes the release of the witness` | where the warrant is issued under s 705(1) or (2) for a witness served with a subpoena or bound by a recognizance, the judge or justice authorizes release under s 705(4) and (5) |
| F29.1-cond | 18542 | fork | `form 29.1 the endorsement authorizes the release of the witness` | "This endorsement is subject to the following conditions: (specify conditions)": the release is subject to them: listed, not flipped, fork F26 (a "may"-named grant with a "subject to" gate: JUST FALSE taken, NOTHING the other reading) |
| F29.1-sig | 18543-18544 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F30-h | 18546 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F30-cap | 18547-18549 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F30-addr | 18550 | inert (reason 2) | - | the order is addressed to the keeper of the prison: the addressee; wording only |
| F30-rec | 18551 | encoded | `form 30 the keeper is directed to have the accused before the justice` | recital: the earlier warrant of committal, the date until which the keeper must keep the accused, and "unless you should be ordered otherwise before that time": the premise of the direction |
| F30-dir | 18552 | encoded | `form 30 the keeper is directed to have the accused before the justice`; `form 30 the duty of the keeper` | the direction to have the accused before the justice at the place and hour to answer to the charge |
| F30-sig | 18553-18554 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F31-h | 18556 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F31-cap | 18557-18559 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F31-dep | 18560-18562 | inert (reason 2) | - | the opening of the depositions and the words "having been duly sworn, deposes as follows": the wording of the record of a deposition; it commands nothing and states no condition |
| F31-cert | 18563-18564 | inert (reason 2) | - | the justice's certificate that the depositions were taken in the presence and hearing of the accused, and the signature: the wording of a certificate; the rule it records is in the section the Form is used under, not in the Form |
| F32-h | 18566 | inert (reason 1) | - | the Form heading and the fifteen sections under which the recognizance is used; the list is not used by any rule here (the conditions below carry their own section lists) |
| F32-cap | 18567-18569 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F32-p1 | 18570-18577 | inert (reason 2) | - | part 1 Identification: the fields (surname, date of birth, address, telephone, employment); wording only |
| F32-p2-h | 18578 | inert (reason 1) | - | the heading of part 2 |
| F32-p2-promise | 18579 | inert (reason 2) | - | "Pursuant to (provision) of the Criminal Code, I agree to (promise or deposit) the amount of $ , or the other valuable security described here": the signatory's own statement of agreement, with the amount left blank; what follows from a failure to comply is the next line (F32-p2-forf) |
| F32-p2-forf | 18580 | fork | `form 32 part 2 the amount or security may be forfeited` | "I understand that if I fail to comply with any of the conditions listed below, this amount or security may be forfeited": fork F4 (a failed "if" under a "may": NOTHING) |
| F32-p3 | 18581-18582 | fork | `form 32 part 3 the recognizance lists the conditions ordered and the duration of each` | part 3: "(List the conditions that have been ordered by the court and indicate the duration for which each condition remains in effect.)": fork F5 (a bare "must" not done) |
| F32-p4 | 18583-18584 | encoded | `form 32 part 4 the person may apply to cancel or vary a condition` | part 4 Variation: the person may apply to a judge or justice of the peace to have any condition in the Form cancelled or varied |
| F32-p5 | 18585-18586 | fork | `form 32 part 5 the conditions remain in effect` | part 5: the conditions remain in effect until cancelled or changed or until the person is discharged, sentenced or otherwise detained by the court (ss 763 and 764): the "until" bar, fork F6 |
| F32-p6-h | 18587 | inert (reason 1) | - | the heading of part 6 |
| F32-p6-person | 18588-18590 | encoded | `form 32 part 6 the person must comply with the condition` | the person giving the recognizance "understand[s] the contents of this form and agree[s] to comply with the conditions that are listed above" |
| F32-p6-psig | 18591-18592 | inert (reason 2) | - | the signature and printed name of the person; wording only |
| F32-p6-s-h | 18593 | inert (reason 2) | - | "SURETY (if applicable):": the caption of the surety's block; wording only |
| F32-p6-s-role | 18594 | inert (reason 2) | - | "I understand my role and my responsibilities under this recognizance and I agree to act as a surety": the surety's own statement of understanding and agreement; the responsibilities it refers to are stated elsewhere (F32-p6-s-forf, F32-p5) |
| F32-p6-s-amt | 18595 | inert (reason 2) | - | "I agree to (promise or deposit) as security to the court the amount of $": the surety's own statement of agreement, with the amount left blank; what follows from a failure to comply is the next line (F32-p6-s-forf) |
| F32-p6-s-forf | 18596 | fork | `form 32 part 6 the money the surety has promised or deposited may be forfeited` | the surety understands that if the person fails to comply the money promised or deposited may be forfeited: fork F20 |
| F32-p6-decl | 18597-18599 | encoded | `form 32 part 6 the surety declaration box that applies` | the Surety Declaration: attached (s 515.1) or the surety excepted (s 515.1(2)), "if applicable" |
| F32-p6-ssig | 18600-18602 | inert (reason 2) | - | the surety's date, place, signature and printed name; wording only |
| F32-p6-jsig | 18603-18606 | inert (reason 2) | - | the judge, provincial court judge, justice or clerk of the court's date, place, signature and printed name; wording only |
| F32-list-h | 18607 | inert (reason 1) | - | the heading "List of Conditions" |
| F32-c-a | 18608 | encoded | `form 32 the condition is listed for the section` | condition (a) has a surety, with the sections the Form lists it for |
| F32-c-b | 18609 | encoded | `form 32 the condition is listed for the section` | condition (b) agrees to keep the peace and be of good behaviour, with the sections the Form lists it for |
| F32-c-c | 18610 | encoded | `form 32 the condition is listed for the section` | condition (c) abstains from possessing a firearm and other weapons and surrenders them, with the sections the Form lists it for |
| F32-c-d | 18611 | encoded | `form 32 the condition is listed for the section` | condition (d) participates in a treatment program, with the sections the Form lists it for |
| F32-c-e | 18612 | encoded | `form 32 the condition is listed for the section` | condition (e) wears an electronic monitoring device (the Attorney General makes the request), with the sections the Form lists it for |
| F32-c-e.1 | 18613 | encoded | `form 32 the condition is listed for the section` | condition (e.1) wears an electronic monitoring device (the Attorney General has consented), with the sections the Form lists it for |
| F32-c-e.2 | 18614 | encoded | `form 32 the condition is listed for the section` | condition (e.2) abstains from communicating with the intimate partner and others, with the sections the Form lists it for |
| F32-c-f | 18615 | encoded | `form 32 the condition is listed for the section` | condition (f) remains within a specified geographic area, with the sections the Form lists it for |
| F32-c-f.1 | 18616 | encoded | `form 32 the condition is listed for the section` | condition (f.1) refrains from going to any specified place, with the sections the Form lists it for |
| F32-c-g | 18617 | encoded | `form 32 the condition is listed for the section` | condition (g) returns to and remains at their place of residence at specified times, with the sections the Form lists it for |
| F32-c-h | 18618 | encoded | `form 32 the condition is listed for the section` | condition (h) abstains from the consumption of drugs, with the sections the Form lists it for |
| F32-c-i | 18619 | encoded | `form 32 the condition is listed for the section` | condition (i) abstains from the consumption of alcohol or any other intoxicating substance, with the sections the Form lists it for |
| F32-c-j | 18620 | encoded | `form 32 the condition is listed for the section` | condition (j) abstains from any contact with a person under 18, with the sections the Form lists it for |
| F32-c-k | 18621 | encoded | `form 32 the condition is listed for the section` | condition (k) abstains from using the Internet or other digital network, with the sections the Form lists it for |
| F32-c-l | 18622 | encoded | `form 32 the condition is listed for the section` | condition (l) abstains from attending a public park, swimming area, daycare centre, schoolground or playground, with the sections the Form lists it for |
| F32-c-m | 18623 | encoded | `form 32 the condition is listed for the section` | condition (m) appears personally or by counsel at the sittings of the appeal court, with the sections the Form lists it for |
| F32-c-n | 18624 | encoded | `form 32 the condition is listed for the section` | condition (n) appears in court as required, with the sections the Form lists it for |
| F32-c-o | 18625 | encoded | `form 32 the condition is listed for the section` | condition (o) refrains from dealing with restrained property, with the sections the Form lists it for |
| F32-c-p | 18626 | encoded | `form 32 the condition is listed for the section` | condition (p) agrees to prosecute the writ of certiorari at their own expense, with the sections the Form lists it for |
| F32-c-q | 18627 | fork | `form 32 the condition is listed for the section` | (q) "any other reasonable conditions, including": an open list (fork F7) |
| F32-c-q1 | 18628 | fork | `form 32 the condition is listed for the section` | (q) bullet 1: reports at specified times to a peace officer or other person designated (fork F7) |
| F32-c-q2 | 18629 | fork | `form 32 the condition is listed for the section` | (q) bullet 2: remains within designated territorial jurisdiction (fork F7) |
| F32-c-q3 | 18630 | fork | `form 32 the condition is listed for the section` | (q) bullet 3: notifies a peace officer or other person designated of any change of address, employment or occupation (fork F7) |
| F32-c-q4 | 18631 | fork | `form 32 the condition is listed for the section` | (q) bullet 4: abstains from communicating with a victim, witness or other specified person (fork F7) |
| F32-c-q5 | 18632 | fork | `form 32 the condition is listed for the section` | (q) bullet 5: deposits all their passports as the judge, provincial court judge or justice directs (fork F7) |
| F33-h | 18634 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F33-body | 18635-18640 | inert (reason 2) | - | the certificate of default (that the person has not appeared or has not complied, and that the ends of justice have been defeated or delayed), the nature and reason for the default, the names of the principal and sureties, the date, signature and seal: the wording of a certificate; the conditions on which it is made are in the section the Form is used under |
| F34-h | 18642 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F34-style | 18643-18644 | inert (reason 2) | - | "Elizabeth II by the Grace of God, etc." and the address "To the sheriff of (territorial division), GREETING": the style of a writ; wording only |
| F34-levy | 18645 | encoded | `form 34 the amount the sheriff is commanded to levy from the person`; `form 34 the duties of the sheriff` | the command to levy of the goods and chattels, lands and tenements of each person the amount set opposite the name |
| F34-table | 18646 | encoded | `form 34 the amount the sheriff is commanded to levy from the person` | the table headings: Name, Address, Occupation, Amount; the amount is the one opposite the name |
| F34-return | 18647 | encoded | `form 34 the sheriff is commanded to make a return`; `form 34 the duties of the sheriff` | the command to make a return of what the sheriff has done in execution of the writ |
| F34-sig | 18648-18650 | inert (reason 2) | - | the date, place and signature lines; wording only and the seal |
| F34.1-h | 18652 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F34.1-cap | 18653-18655 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F34.1-addr | 18656 | encoded | `form 34.1 the statement is addressed to a court sentencing an offender convicted or discharged under section 730` | the statement is addressed to the court sentencing the named offender who was convicted, or was discharged under s 730 |
| F34.1-box | 18657-18659 | inert (reason 2) | - | "I, (name), declare that (check the appropriate box)" and the two boxes (not seeking / seeking restitution): the declarant's election; wording only |
| F34.1-decl | 18660-18666 | inert (reason 2) | - | the declaration of losses and damages and the table (Description, Amount; rows 1 to 4): the declarant's particulars; wording only |
| F34.1-asc | 18667 | encoded | `form 34.1 the loss may be claimed as restitution`; `form 34.1 the declarant is responsible for providing the documents` | the losses must be readily ascertainable by the court; the declarant is responsible for providing the documents |
| F34.1-sig | 18668-18669 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F34.2-h | 18671 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F34.2-intro | 18672 | encoded | `form 34.2 the statement may include the item` | the Form "may be used" to describe harm, damage or loss; "You may attach additional pages" |
| F34.2-must | 18673 | fork | `form 34.2 the statement may include the item` | "Your statement must not include": the lead-in of the five prohibitions (fork F8, the court-approval exception) |
| F34.2-b1 | 18674 | encoded | `form 34.2 the statement may include the item` | prohibition 1: a statement about the offence or the offender that is not relevant to the harm or loss |
| F34.2-b2 | 18675 | encoded | `form 34.2 the statement may include the item` | prohibition 2: any unproven allegations |
| F34.2-b3 | 18676 | encoded | `form 34.2 the statement may include the item` | prohibition 3: any comments about an offence for which the offender was not convicted |
| F34.2-b4 | 18677 | encoded | `form 34.2 the statement may include the item` | prohibition 4: any complaint about an individual, other than the offender, involved in the investigation or prosecution |
| F34.2-b5 | 18678 | fork | `form 34.2 the statement may include the item` | prohibition 5: except with the court's approval, an opinion or recommendation about the sentence (fork F8) |
| F34.2-may | 18679 | encoded | `form 34.2 the statement may include the item`; `form 34.2 the declarant is required to include all the examples` | "You may present a detailed account of the impact ... You are not required to include all of this information" |
| F34.2-emo | 18680-18685 | encoded | `form 34.2 the statement may include the item` | Emotional impact: the heading, the prompt and four examples (lifestyle and activities, relationships, work or study, feelings) |
| F34.2-phy | 18686-18692 | encoded | `form 34.2 the statement may include the item` | Physical impact: the heading, the prompt and five examples (pain, hospitalization, treatment, further treatment, disability) |
| F34.2-eco | 18693-18698 | encoded | `form 34.2 the statement may include the item` | Economic impact: the heading, the prompt and four examples (property, lost work, medical costs, uninsured costs) |
| F34.2-note | 18699 | encoded | `form 34.2 this is an application for compensation or restitution` | "Please note that this is not an application for compensation or restitution" |
| F34.2-fear | 18700-18703 | encoded | `form 34.2 the statement may include the item` | Fears for security: the heading, the prompt and two examples (contact with the offender, contact with family and friends) |
| F34.2-draw | 18704-18705 | encoded | `form 34.2 the statement may include the item` | Drawing, poem or letter: the declarant may use the space to draw a picture or write a poem or letter |
| F34.2-box | 18706-18707 | inert (reason 2) | - | the two boxes (present the statement in court; receive information respecting the sentence): the declarant's wishes; wording only |
| F34.2-true | 18708-18710 | inert (reason 2) | - | "To the best of my knowledge, the information contained in this statement is true", the date and signature: a declaration; wording only |
| F34.2-behalf | 18711-18713 | inert (reason 2) | - | the prompt to say why the statement was completed on behalf of the victim, and the date and signature: a prompt in the wording of the Form ("please indicate"); who may act for the victim is s 2.2, in the keel |
| F34.3-h | 18715 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F34.3-intro | 18716 | encoded | `form 34.3 the statement may include the item` | the Form "may be used" to describe the harm or loss suffered by a community; "You may attach additional pages" |
| F34.3-must | 18717 | fork | `form 34.3 the statement may include the item` | "Your statement must not include": the lead-in of the five prohibitions (fork F8) |
| F34.3-b1 | 18718 | encoded | `form 34.3 the statement may include the item` | prohibition 1: a statement about the offence or the offender that is not relevant to the harm or loss suffered by the community |
| F34.3-b2 | 18719 | encoded | `form 34.3 the statement may include the item` | prohibition 2: any unproven allegations |
| F34.3-b3 | 18720 | encoded | `form 34.3 the statement may include the item` | prohibition 3: any comments about an offence for which the offender was not convicted |
| F34.3-b4 | 18721 | encoded | `form 34.3 the statement may include the item` | prohibition 4: any complaint about an individual, other than the offender, involved in the investigation or prosecution |
| F34.3-b5 | 18722 | fork | `form 34.3 the statement may include the item` | prohibition 5: except with the court's approval, an opinion or recommendation about the sentence (fork F8) |
| F34.3-name | 18723-18724 | inert (reason 2) | - | the prompts "Name of community on whose behalf the statement is made" and "Explain how the statement reflects this community's views": prompts in the wording of the Form |
| F34.3-may | 18725 | encoded | `form 34.3 the statement may include the item` | "You may present a detailed account of the impact the offence has had on the community ... examples ... You are not required to include all of this information" |
| F34.3-emo | 18726-18732 | encoded | `form 34.3 the statement may include the item` | Emotional impact: the heading, the prompt and five examples |
| F34.3-phy | 18733-18736 | encoded | `form 34.3 the statement may include the item` | Physical impact: the heading, the prompt and two examples |
| F34.3-eco | 18737-18741 | encoded | `form 34.3 the statement may include the item` | Economic impact: the heading, the prompt and three examples |
| F34.3-note | 18742 | encoded | `form 34.3 this is an application for compensation or restitution` | "Please note that this is not an application for compensation or restitution" |
| F34.3-fear | 18743-18744 | encoded | `form 34.3 the statement may include the item` | Fears for security: the heading and the prompt |
| F34.3-draw | 18745-18746 | encoded | `form 34.3 the statement may include the item` | Drawing, poem or letter |
| F34.3-box | 18747 | inert (reason 2) | - | the box (present this statement in court): the declarant's wish; wording only |
| F34.3-true | 18748-18750 | inert (reason 2) | - | the declaration of truth, the date and signature; wording only |
| F35-h | 18752 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F35-cap | 18753-18755 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F35-stem | 18756 | inert (reason 2) | - | "Be it remembered that ... was tried under Part (XIX or XXVII) ... was convicted of the said offence and the following punishment was imposed": the record of a conviction; wording only |
| F35-a | 18757 | inert (reason 2) | - | (a) imprisonment for the term of ___: the record of the punishment; wording only |
| F35-b | 18758 | fork | `form 35 the imprisonment in default of payment still applies` | (b) forfeit and pay, and "in default of payment ... to be imprisoned ... unless the said sums and the costs and charges ... are sooner paid": fork F1 |
| F35-c | 18759 | fork | `form 35 the imprisonment in default of payment still applies` | (c) imprisonment and, in addition, forfeit and pay, with the same default term: fork F1; the default term only |
| F35-sig | 18760-18762 | inert (reason 2) | - | the date, place and signature lines; wording only and the seal |
| F36-h | 18764 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F36-body | 18765-18770 | inert (reason 2) | - | the record of an order against an offender ("it was ordered and adjudged that (set out the order made)"), the date and signature: wording only |
| F37-h | 18772 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F37-body | 18773-18779 | inert (reason 2) | - | the record of an acquittal ("was found not guilty of the said offence"), the date, signature and seal: wording only |
| F38-h | 18781 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F38-body | 18782-18789 | inert (reason 2) | - | the record of a conviction for contempt (the defaulter "did not attend ... although duly subpoenaed ... and has not shown any sufficient excuse") and of the punishment under s 708: the wording of a record; the conditions of the offence are in s 708 |
| F39-h | 18791 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F39-cap | 18792-18794 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F39-addr | 18795 | inert (reason 2) | - | the order is addressed to the keeper of the prison: the addressee; wording only |
| F39-dir | 18796 | encoded | `form 39 the keeper is directed to release the person`; `form 39 the duty of the keeper` | "You are directed to release E.F., detained by you under a (warrant of committal or order) dated (date), if E.F. is detained by you for no other cause" |
| F39-sig | 18797-18798 | inert (reason 2) | - | the date, place and signature lines; wording only and the seal |
| F40-h | 18800 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F40-cap | 18801-18806 | inert (reason 2) | - | the caption and the style of cause "The Queen v. C.D."; wording only |
| F40-chal | 18807 | encoded | `form 40 the challenge to the array is in the Form's terms` | the prosecutor or the accused challenges the array of the panel on the ground that the sheriff or deputy sheriff who returned the panel was guilty of partiality, fraud or wilful misconduct |
| F40-sig | 18808-18809 | inert (reason 2) | - | the date and the signature of counsel; wording only |
| F41-h | 18811 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F41-cap | 18812-18817 | inert (reason 2) | - | the caption and the style of cause "The Queen v. C.D."; wording only |
| F41-chal | 18818 | fork | `form 41 the challenge for cause is in the Form's terms` | the prosecutor or the accused challenges a juror on a ground "in accordance with subsection 638(1)": fork F9 |
| F41-sig | 18819 | inert (reason 2) | - | the signature of counsel; wording only |
| F42-h | 18821 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F42-body | 18822-18827 | inert (reason 2) | - | the clerk's certificate that a party ordered to pay costs of an appeal has not paid within the time limited, with the style of cause, date, signature and seal: the wording of a certificate; the duty to pay is in s 827 |
| F43-h | 18829 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F43-body | 18830-18832 | inert (reason 2) | - | the keeper's receipt: "I hereby certify that I have received ... one A.B., together with a (warrant or order)": the wording of a receipt; it states a fact and no rule |
| F44-h | 18834 | inert (reason 1) | - | the heading of Form 44 (Section 667), which has no title in this text |
| F44-body | 18835-18838 | inert (reason 2) | - | the fingerprint examiner's certificate of a person's record of conviction, with the date and signature: the wording of a certificate of facts |
| F45-h | 18840 | inert (reason 1) | - | the heading of Form 45 (Section 667), which has no title in this text |
| F45-body | 18841-18843 | inert (reason 2) | - | the fingerprint examiner's certificate that two sets of fingerprints are those of the same person, with the date and signature: the wording of a certificate of facts |
| F46-h | 18845 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F46-cap | 18846-18848 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F46-rec | 18849 | inert (reason 2) | - | recital of the plea or finding of guilt and the charge (the offender "pleaded guilty to or was tried under Part XIX, XX or XXVII ... and was convicted or found guilty"); the record of the conviction on which the order rests; wording only |
| F46-adj | 18850 | fork | `form 46 the court's adjudication` | "And whereas on the day the court adjudged*": the asterisk has no footnote in this text (finding); the seven alternatives (a) to (g) follow: fork F10 |
| F46-a | 18851 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (a) discharge on conditions |
| F46-b | 18852 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (b) sentence suspended and release on conditions |
| F46-c | 18853 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (c) a fine, with imprisonment in default, and the conditions in addition |
| F46-d | 18854 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (d) imprisonment and, in addition, the conditions: they run from the expiration of the sentence |
| F46-e | 18855 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (e) following the expiration of a conditional sentence order: the conditions run from its expiration |
| F46-f | 18856 | encoded | `form 46 the conditions begin on`; `form 46 the court's adjudication` | (f) following the expiration of a sentence of imprisonment for another offence: the conditions run from its expiration |
| F46-g | 18857 | fork | `form 46 the offender must comply with the conditions on the day` | (g) an intermittent sentence: the conditions apply "when not in confinement": fork F11 (a "when" limb) |
| F46-now | 18858 | fork | `form 46 the offender must comply with the conditions on the day`; `form 46 the offender is in compliance with the standard conditions`; `form 46 the duty to keep the peace and be of good behaviour`; `form 46 the duty to appear before the court when required`; `form 46 the duty to notify the court or probation officer of a change` | "Now therefore the said offender shall, for the period of ___ from the date of this order (or ...) comply with ... keep the peace and be of good behaviour, appear before the court when required ..., notify ... in advance of any change of name or address and promptly notify ... of any change of employment or occupation": fork F12 (counting the period; "promptly"; a bare "shall" not done) |
| F46-add | 18859 | encoded | `form 46 the additional condition may be stated` | "(here state any additional conditions prescribed pursuant to subsection 732.1(3))" |
| F46-sig | 18860-18861 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F47-h | 18863 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F47-cap | 18864-18866 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F47-to | 18867 | inert (reason 2) | - | the addressee ("To A.B., of , (office or occupation)"); wording only |
| F47-rec1 | 18868 | encoded | `form 47 the order authorizes and requires the addressee to produce the information` | recital: on oath, reasonable grounds to believe that E.F. has committed or benefited from the commission of the offence and the information is likely to be of substantial value: a premise |
| F47-rec2 | 18869 | encoded | `form 47 the order authorizes and requires the addressee to produce the information` | recital: reasonable grounds to believe that it is in the public interest to allow access: a premise |
| F47-cmd | 18870 | encoded | `form 47 the order authorizes and requires the addressee to produce the information`; `form 47 the production meets the order`; `form 47 the duty of the addressee` | the authorization and requirement to produce the information and documents to one of the named police officers, between the hours and during the period the judge directs, subject to conditions |
| F47-sig | 18871-18872 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F48-h | 18874 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F48-cap | 18875-18877 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F48-stem | 18878 | encoded | `form 48 the court has grounds to order an assessment for the purpose` | "Whereas I have reasonable grounds to believe that evidence of the mental condition of (name of accused), who has been charged with ___, may be necessary to determine": the lead-in of the five purposes |
| F48-p1 | 18879 | encoded | `form 48 the court has grounds to order an assessment for the purpose` | purpose 1: whether the accused is unfit to stand trial |
| F48-p2 | 18880 | encoded | `form 48 the court has grounds to order an assessment for the purpose` | purpose 2: whether the accused suffered from a mental disorder so as to be exempt from criminal responsibility under s 16(1) |
| F48-p3 | 18881 | fork | `form 48 the court has grounds to order an assessment for the purpose` | purpose 3: whether the balance of the mind was disturbed, if the accused is a female person charged with an offence arising out of the death of her newly-born child: fork F13 (the words "if ... female person") |
| F48-p4 | 18882 | encoded | `form 48 the court has grounds to order an assessment for the purpose` | purpose 4: the appropriate disposition under s 672.54, 672.58 or 672.64 or whether to revoke a high-risk finding under s 672.84(3), if a verdict of unfit or not criminally responsible has been rendered |
| F48-p5 | 18883 | encoded | `form 48 the court has grounds to order an assessment for the purpose` | purpose 5: whether the court should order a stay of proceedings under s 672.851, if a verdict of unfit has been rendered |
| F48-per | 18884 | encoded | `form 48 the order is in force` | the assessment is ordered to be conducted by or at a named person, service or place, for a period of ___ days |
| F48-tot | 18885 | fork | `form 48 the order is in force` | the order is in force for a total of ___ days, including travelling time: fork F14 (counting the days) |
| F48-cus | 18886-18888 | encoded | `form 48 the accused is to remain in custody or out of custody`; `form 48 the accused must comply with the condition` | the accused is to remain in custody at a named place, or out of custody on conditions |
| F48-sig | 18889-18890 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F48.1-h | 18892 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F48.1-cap | 18893-18895 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F48.1-stem | 18896 | encoded | `form 48.1 the Review Board has grounds to order an assessment for the purpose` | "Whereas I have reasonable grounds to believe that evidence of the mental condition ... may be necessary to": the lead-in of the two purposes |
| F48.1-p1 | 18897 | encoded | `form 48.1 the Review Board has grounds to order an assessment for the purpose` | purpose 1: to make a disposition under s 672.54 or determine whether to refer a high-risk finding for review under s 672.84(1), if a verdict of unfit or not criminally responsible has been rendered |
| F48.1-p2 | 18898 | encoded | `form 48.1 the Review Board has grounds to order an assessment for the purpose` | purpose 2: to determine whether to recommend an inquiry into a stay of proceedings under s 672.851, if a verdict of unfit has been rendered |
| F48.1-per | 18899 | encoded | `form 48.1 the order is in force` | "I hereby order an assessment ... for a period of ___ days" |
| F48.1-tot | 18900 | fork | `form 48.1 the order is in force` | in force for a total of ___ days, including travelling time: fork F14 |
| F48.1-cus | 18901-18903 | encoded | `form 48.1 the accused is to remain in custody or out of custody`; `form 48.1 the accused must comply with the condition` | the accused is to remain in custody at a named place, or out of custody on conditions |
| F48.1-sig | 18904-18905 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F48.2-h | 18907 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F48.2-intro | 18908 | encoded | `form 48.2 the statement may include the item` | the Form "may be used" to describe the harm or loss arising from the conduct for which the accused was found not criminally responsible; "You may attach additional pages" |
| F48.2-must | 18909 | fork | `form 48.2 the statement may include the item` | "Your statement must not include": the lead-in of the five prohibitions (fork F8) |
| F48.2-b1 | 18910 | encoded | `form 48.2 the statement may include the item` | prohibition 1: a statement about the conduct of the accused that is not relevant to the harm or loss |
| F48.2-b2 | 18911 | encoded | `form 48.2 the statement may include the item` | prohibition 2: any unproven allegations |
| F48.2-b3 | 18912 | encoded | `form 48.2 the statement may include the item` | prohibition 3: any comments about conduct for which the accused was not found not criminally responsible |
| F48.2-b4 | 18913 | encoded | `form 48.2 the statement may include the item` | prohibition 4: any complaint about an individual, other than the accused, involved in the investigation or prosecution |
| F48.2-b5 | 18914 | fork | `form 48.2 the statement may include the item` | prohibition 5: except with the court's or Review Board's approval, an opinion or recommendation about the disposition (fork F8) |
| F48.2-ex | 18915 | encoded | `form 48.2 the statement may include the item`; `form 48.2 the declarant is required to include all the examples` | "The following sections are examples of information you may wish to include ... You are not required to include all of this information" |
| F48.2-emo | 18916-18921 | encoded | `form 48.2 the statement may include the item` | Emotional impact: the heading, the prompt and four examples |
| F48.2-phy | 18922-18928 | encoded | `form 48.2 the statement may include the item` | Physical impact: the heading, the prompt and five examples |
| F48.2-eco | 18929-18934 | encoded | `form 48.2 the statement may include the item` | Economic impact: the heading, the prompt and four examples |
| F48.2-note | 18935 | encoded | `form 48.2 this is an application for compensation or restitution` | "Please note that this is not an application for compensation or restitution" |
| F48.2-fear | 18936-18939 | encoded | `form 48.2 the statement may include the item` | Fears for security: the heading, the prompt and two examples |
| F48.2-draw | 18940-18941 | encoded | `form 48.2 the statement may include the item` | Drawing, poem or letter |
| F48.2-box | 18942-18945 | inert (reason 2) | - | the four boxes (read or present the statement; receive information about hearings; receive information about any disposition; receive notice of a discharge and the intended residence): the declarant's wishes; wording only |
| F48.2-true | 18946-18948 | inert (reason 2) | - | the declaration of truth, the date and signature; wording only |
| F49-h | 18950 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F49-sub | 18951-18952 | inert (reason 1) | - | the sub-heading "Disposition of Detention" |
| F49-cap | 18953-18955 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F49-addr | 18956 | encoded | `form 49 the peace officers are commanded to take and convey the accused` | the warrant is addressed to the peace officers in the territorial division and to the keeper (administrator, warden) of the prison, hospital or other place |
| F49-iss | 18957 | inert (reason 2) | - | "This warrant is issued for the committal of A.B., of , (occupation), hereinafter called the accused": the identification of the accused; wording only |
| F49-chg | 18958 | encoded | `form 49 the peace officers are commanded to take and convey the accused` | recital of the charge: a premise |
| F49-found | 18959-18961 | encoded | `form 49 the peace officers are commanded to take and convey the accused` | recital that the accused was found unfit to stand trial or not criminally responsible on account of mental disorder: a premise |
| F49-cmd | 18962 | encoded | `form 49 the peace officers are commanded to take and convey the accused`; `form 49 the duties of the peace officers and the keeper` | the command to take the accused in custody and convey them safely to the place and deliver them to the keeper with the precept |
| F49-keep | 18963 | fork | `form 49 the keeper is directed to keep the accused in custody` | the precept to receive the accused and keep them safely "until the accused is delivered by due course of law": the "until" bar, fork F6 |
| F49-cond | 18964 | encoded | `form 49 the accused is subject to the condition` | "The following are the conditions to which the accused shall be subject while in your (prison, hospital or other appropriate place)" |
| F49-pow | 18965 | encoded | `form 49 the keeper holds the delegated power` | "The following are the powers regarding the restrictions ... on the liberty of the accused that are hereby delegated to you the said keeper" |
| F49-sig | 18966-18967 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F50-h | 18969 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F50-sub | 18970-18971 | inert (reason 1) | - | the sub-heading "Placement Decision" |
| F50-cap | 18972-18974 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F50-addr | 18975 | encoded | `form 50 the keeper is commanded to execute the warrant` | the warrant is addressed to the peace officers in the territorial division and to the keeper (administrator, warden) of the prison, hospital or other place where the accused is detained |
| F50-iss | 18976 | inert (reason 2) | - | "This warrant is issued for the committal of A.B. ... hereinafter called the accused": the identification of the accused; wording only |
| F50-chg | 18977 | encoded | `form 50 the keeper is commanded to execute the warrant` | recital of the charge: a premise |
| F50-found | 18978-18980 | encoded | `form 50 the keeper is commanded to execute the warrant` | recital that the accused was found unfit to stand trial or not criminally responsible: a premise |
| F50-rb | 18981 | encoded | `form 50 the keeper is commanded to execute the warrant` | recital that the Review Board has held a hearing and decided that the accused shall be detained in custody: a premise |
| F50-court | 18982 | encoded | `form 50 the keeper is commanded to execute the warrant` | recital that the accused is required to be detained pursuant to a warrant of committal issued by a court: a premise |
| F50-cmd | 18983-18985 | encoded | `form 50 the keeper is commanded to execute the warrant`; `form 50 the duty of the keeper` | the command to execute the warrant of committal issued by the court according to its terms, or the warrant issued herewith by the Review Board |
| F50-sig | 18986-18987 | inert (reason 2) | - | the date, place and signature lines; wording only |
| F51-h | 18989 | inert (reason 1) | - | the Form heading and the eight paragraphs under which the notice is given (732.1(3)(c.2), 742.3(2)(a.2), 810(3.02)(c), 810.01(4.1)(g), 810.03(7)(h), 810.011(6)(f), 810.1(3.02)(i), 810.2(4.1)(g)); the list names the orders the notice follows and states no rule |
| F51-to | 18990 | inert (reason 2) | - | the addressee and particulars (name, occupation, address, date of birth, gender); wording only |
| F51-bec | 18991-18992 | encoded | `form 51 the person is subject to the obligation to provide samples` | "Because, on (date), you were ordered ... to provide samples of a bodily substance prescribed by regulation at regular intervals for the purpose of analysis; You are provided with this notice to inform you of your obligations" |
| F51-p1 | 18993 | fork | `form 51 para 1 the first report is on a permitted day`; `form 51 para 1 the person reports within the hours stated` | paragraph 1: report on a day not earlier than 24 hours after the day on which the notice is served, at any time from one time to another, at the designated place: fork F15 (counting "24 hours after the day") |
| F51-p2 | 18994 | encoded | `form 51 para 2 the number of days stated is permitted`; `form 51 para 2 the person must report on the day` | paragraph 2: every N days, N not less than seven, after the first report, at any time from one time to another |
| F51-p3 | 18995 | encoded | `form 51 para 3 the person may apply to terminate the obligation`; `form 51 para 3 the person may appeal the decision` | paragraph 3: the right to apply to a court to terminate the obligation and the right to appeal any decision of that court |
| F51-p4 | 18996 | encoded | `form 51 para 4 the consequence of not complying` | paragraph 4: a fine or imprisonment, or both; for a conditional sentence, proceedings under s 742.6, the consequences of which may include imprisonment |
| F51-p5 | 18997 | encoded | `form 51 para 5 the results of the analysis may be used in proceedings against the person` | paragraph 5: the results may be used or disclosed in accordance with the Criminal Code, including in proceedings against the person |
| F51-sig | 18998-18999 | inert (reason 2) | - | the service line ("Served on (date), at (place)") and the signature of the probation officer, supervisor or designated person; wording only |
| F52-h | 19001 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F52-cap | 19002-19004 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F52-to | 19005 | inert (reason 2) | - | the addressee and particulars; wording only |
| F52-intro | 19006 | encoded | `form 52 the order applies to the person` | "You have been convicted of or found not criminally responsible ... a designated offence within the meaning of subsection 490.011(1)" |
| F52-p1 | 19007 | encoded | `form 52 para 1 the person must report for the first time` | paragraph 1: report for the first time to the registration centre, whenever required under s 4(1) of the Sex Offender Information Registration Act |
| F52-p2 | 19008 | encoded | `form 52 para 2 the period for which the person must report`; `form 52 para 2 the person must report on the day` | paragraph 2: report subsequently, whenever required under s 4.1 or 4.3 of that Act, for a period of ___ years after the order is made, or for life if 490.013(2)(c), (3), (5) or (6) applies |
| F52-p3 | 19009 | encoded | `form 52 para 3 information will be collected` | paragraph 3: information will be collected under ss 5 and 6 of that Act at the registration centre |
| F52-p4 | 19010 | encoded | `form 52 para 4 information will be registered` | paragraph 4: information will be registered in a database and may be consulted, disclosed and used as that Act sets out |
| F52-p5 | 19011 | fork | `form 52 para 5 the person may ask for a correction` | paragraph 5: if the person believes the registered information contains an error or omission, they may ask for it to be corrected: fork F21 (a failed "if" under a "may": NOTHING taken) |
| F52-p6 | 19012 | encoded | `form 52 para 6 the person may apply to terminate the order`; `form 52 para 6 the person may appeal the decision` | paragraph 6: the right to apply to a court to terminate the order and the right to appeal the decision |
| F52-p7 | 19013 | encoded | `form 52 para 7 the consequence of contravening the order` | paragraph 7: a fine or imprisonment, or both, if found to have contravened the order |
| F52-p8 | 19014 | encoded | `form 52 para 8 the consequence of providing false or misleading information` | paragraph 8: a fine or imprisonment, or both, if found to have provided false or misleading information |
| F52-sig | 19015-19017 | inert (reason 2) | - | the date, place and signature lines; wording only of the judge or clerk, and the signature of the person subject to the order |
| F53-h | 19019 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F53-cap | 19020-19022 | inert (reason 2) | - | the caption (Canada, Province, territorial division); wording only |
| F53-to | 19023 | inert (reason 2) | - | the addressee ("a person referred to in subsection 490.02(1)"); wording only |
| F53-intro | 19024 | encoded | `form 53 the person is required to comply` | "Because ... you were convicted of, or found not criminally responsible ..., one or more offences referred to in paragraph (a), (c), (c.1), (d), (d.1) or (e) of the definition designated offence ... this is provided to give you notice that you are required to comply with the Sex Offender Information Registration Act" |
| F53-p1 | 19025 | encoded | `form 53 para 1 the person must report for the first time` | paragraph 1: report for the first time, whenever required under s 4(2) of that Act |
| F53-p2 | 19026 | encoded | `form 53 para 2 the period for which the person must report`; `form 53 para 2 the person must report on the day` | paragraph 2: report subsequently for a period of ___ years after being sentenced or found not criminally responsible, or for life if 490.022(3)(c) or (d) applies, or for any shorter period under s 490.022(2) |
| F53-p3 | 19027 | encoded | `form 53 para 3 information will be collected` | paragraph 3: information will be collected under ss 5 and 6 |
| F53-p4 | 19028 | encoded | `form 53 para 4 information will be registered` | paragraph 4: information will be registered and may be consulted, disclosed and used |
| F53-p5 | 19029 | fork | `form 53 para 5 the person may ask for a correction` | paragraph 5: the person may ask for an error or omission to be corrected: fork F22 (a failed "if" under a "may": NOTHING taken) |
| F53-p6 | 19030 | encoded | `form 53 para 6 the person may apply for an exemption`; `form 53 para 6 the person may appeal the decision on the exemption` | paragraph 6: the right to apply to a court to be exempted from the obligation, and to appeal |
| F53-p7 | 19031 | encoded | `form 53 para 7 the person may apply to terminate the obligation`; `form 53 para 7 the person may appeal the decision on termination` | paragraph 7: the right to apply to a court to terminate the obligation, and to appeal |
| F53-p8 | 19032 | encoded | `form 53 para 8 the consequence of contravening the obligation` | paragraph 8: a fine or imprisonment, or both |
| F53-p9 | 19033 | encoded | `form 53 para 9 the consequence of providing false or misleading information` | paragraph 9: a fine or imprisonment, or both |
| F53-sig | 19034 | inert (reason 2) | - | the date and place line; wording only |
| F54-h | 19036 | inert (reason 1) | - | the Form heading: its title and the section(s) under which it is used; names a cross-reference and states no rule |
| F54-to | 19037 | inert (reason 2) | - | the addressee and particulars (name, occupation, address, date of birth, gender); wording only |
| F54-intro | 19038-19039 | encoded | `form 54 the person is required to comply` | "Because, on (date), you were convicted of or found not criminally responsible ... for an offence ... that the Attorney General of the province, or the minister of justice of the territory, has identified as being equivalent to ... an offence referred to in paragraph (a) of the definition primary offence ... You are provided with this to inform you that you are required to comply" |
| F54-p1 | 19040 | encoded | `form 54 para 1 the person must report for the first time` | paragraph 1: report for the first time, whenever required under s 4(2) of that Act |
| F54-p2 | 19041 | encoded | `form 54 para 2 the period for which the person must report`; `form 54 para 2 the person must report on the day` | paragraph 2: report subsequently for a period of ___ years after the day of sentence or verdict, or for life if 490.02904(3)(c) or (d) applies, or for any shorter period under s 490.02904(2) |
| F54-p3 | 19042 | encoded | `form 54 para 3 information will be collected` | paragraph 3: information will be collected |
| F54-p4 | 19043 | encoded | `form 54 para 4 information will be registered` | paragraph 4: information will be registered |
| F54-p5 | 19044 | fork | `form 54 para 5 the person may ask for a correction` | paragraph 5: the person may ask for an error or omission to be corrected: fork F23 (a failed "if" under a "may": NOTHING taken) |
| F54-p6 | 19045 | encoded | `form 54 para 6 the person may apply for an exemption`; `form 54 para 6 the person may appeal the decision on the exemption` | paragraph 6: the right to apply to a court to be exempted, and to appeal |
| F54-p6.1 | 19046 | fork | `form 54 para 6.1 the person may apply to vary the duration`; `form 54 para 6.1 the person may appeal the decision on the duration` | paragraph 6.1: the right to apply to a court to vary the duration if the obligation is for life because of more than one offence, and to appeal: fork F24 and fork F25 (a failed "if" under a right to apply and to appeal: NOTHING taken) |
| F54-p7 | 19047 | encoded | `form 54 para 7 the person may apply to terminate the obligation`; `form 54 para 7 the person may appeal the decision on termination` | paragraph 7: the right to apply to a court to terminate the obligation, and to appeal |
| F54-p8 | 19048 | encoded | `form 54 para 8 the consequence of not complying` | paragraph 8: a fine or imprisonment, or both, if found not to have complied |
| F54-p9 | 19049 | encoded | `form 54 para 9 the consequence of providing false or misleading information` | paragraph 9: a fine or imprisonment, or both |
| F54-sig | 19050-19052 | inert (reason 2) | - | the service line and the "For administrative use only" line (the date of sentence or verdict); wording only |
| RP-h | 19054-19055 | inert (reason 1) | - | the heading "RELATED PROVISIONS" which opens the related and transitional provisions of amending Acts; the provisions that follow (lines 19056 on) belong to part ccc32 |

## Fork register (ccc31)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry: the provision and function, the readings and the text that licenses each, the reading taken.
The taken reading is the status quo for a human reviewer to overrule; the rows of the coverage table marked `fork` point here.
Line numbers are those of `R.S.C.-1985-c.-C-46.txt`.

- **F1. An "unless" or "until" once met** (the keeper's precepts of Forms 24, 25 (b) and (c), 26, 27, 35 (b) and (c); `form 24 the keeper is directed to keep the witness in custody`, `form 25 the keeper is ordered to keep the defaulter in custody`, `form 26 the keeper is commanded to keep the defaulter in custody`, `form 27 the keeper is ordered to keep the defaulter in custody`, `form 35 the imprisonment in default of payment still applies`; lines 18472, 18487-18488, 18501, 18512, 18758-18759). The text says "keep them there safely until the trial of the accused on the charge, unless before that time the witness enters into the recognizance"; "unless the said sum and the costs and charges ... are sooner paid"; "unless the said sums and the costs and charges ... are sooner paid". Reading A (taken): once the "unless" is met (the witness has entered into the recognizance; the sums, costs and charges are all paid) or the "until" is reached (the trial has taken place), the answer is `JUST FALSE`: the "until" bar of the ruling of 2026-11-05 (d), which asks for the bar and never the claim that the person "has been released". Reading B: an "unless" or "except" once met is one of the six questions the maintainer ruled are decided case by case (2026-11-05), and the text does not itself say what follows, so `NOTHING`. Licence: "until", "unless" (A); the six-questions ruling (B). Within A, for Form 24 "until the trial" is taken as "once the trial has taken place" (the input); the other readings are "once the trial begins" and "once it ends", which the text does not distinguish. For Form 26, "the said sum and the costs and charges" is read as needing ALL of them paid (the sum, and the costs and charges of the committal and of conveying the defaulter); the sum paid alone leaves the answer `JUST TRUE` (tested).
- **F2. Form 25 (c): which term "unless the sums ... are sooner paid" reaches** (line 18488: "(c) for the term of and for the term of (if consecutive so state) unless the sums and the costs and charges of the committal and of conveying the defaulter to the prison are sooner paid"). Reading A: the "unless" reaches both terms, so payment during the first term ends the custody. Reading B: it reaches only the second term (the term in default of paying the amounts), as the matching words of Form 35 (c) do. The text does not choose. Taken: where payment is made while the first term is still running the answer is `NOTHING` (NOTHING-kind (limited by its own wording)); once the first term has run and the sums are paid, both readings agree: `JUST FALSE` (tested). Also: the two terms are concurrent unless "(if consecutive so state)"; the function takes the statement as an input and, if it is stated, adds the second term after the first.
- **F3. Form 27: "for a period of ___ or until satisfaction is made of a judgment debt"** (line 18512). Reading A (taken): custody ends at the earlier of the end of the period and the satisfaction of the debt. Reading B: the two are alternatives of which whoever completes the Form chooses one; the function gives the same answer when the Form is completed with one of them and the caller leaves the other input at its inert value. The debt must be "due to Her Majesty the Queen in respect of the forfeiture of an amount set out in (an undertaking ... a release order ... a recognizance)"; the function takes that as an input and answers `NOTHING` if it is not so.
- **F4. `form 32 part 2 the amount or security may be forfeited`** (line 18580: "I understand that if I fail to comply with any of the conditions listed below, this amount or security may be forfeited"). The function is named for a power ("may be forfeited": the court's power, the person's liability). `JUST TRUE` is the Form's "may", not "is forfeited". When there is no failure to comply: reading A (taken): the "if" gate is not closed by the text with "only if", and the Guide gives `NOTHING` where the text limits a grant in its own wording, so `NOTHING`; reading B: a failed "if" is the text's own no (marginal reading (a)), so `JUST FALSE`.
- **F5. A bare "must" not done** (Form 32 part 3 line 18581-18582; Form 46 line 18858; Form 47 line 18870). The function answers whether the duty is met: reading A (taken) a duty not done is `JUST FALSE` (the function says "the recognizance lists the conditions ordered", "the offender is in compliance", "the production meets the order", and the answer to that question is no); reading B: the text does not say what follows, so `NOTHING`. This is one of the six case-by-case questions of 2026-11-05 ("a bare 'must' not done"). The functions never say what follows a failure: no remedy, sanction or consequence is invented.
- **F6. The "until" bars of Form 32 part 5 and Form 49** (lines 18586, 18963). Part 5: the conditions remain in effect "until they are cancelled or changed or until I have been discharged, sentenced or otherwise detained by the court (sections 763 and 764)"; Form 49: the keeper keeps the accused "until the accused is delivered by due course of law". Ruling of 2026-11-05 (d): `JUST TRUE` before the end event and `JUST FALSE` after, never "the conditions have ended". The end events are plain inputs ("otherwise detained", "delivered by due course of law" are open-textured judgments the caller makes). Sections 763 and 764 are cited in the Form and are not among the sources.
- **F7. The List of Conditions of Form 32 and its parentheses** (lines 18607-18632). Each condition names the sections it is used under in parentheses ("(a) has a surety (sections 462.34, 490.9, 550, 779, 810, 817 and 832 of the Criminal Code)") and no list is closed with "only". Reading A (taken): a condition asked about under a section the Form does not list for it is `NOTHING` (list not closed). Reading B: the Form lists where each condition is used, so a section not listed is `JUST FALSE`. Entry (q) ("any other reasonable conditions, including:") names no section for the stem or for its five entries, so every section is `NOTHING` for it under either reading of "including" (an open list). Not a fork but a finding: the list cites section 83.3 which the Form's heading does not (Finding 5).
- **F8. "except with the court's approval, an opinion or recommendation about the sentence"** (Forms 34.2 line 18678, 34.3 line 18722; Form 48.2 line 18914, "the court's or Review Board's approval, ... about the disposition"). Without approval: `JUST FALSE` (a flat negative, ruling N2). With approval: reading A (taken) the Form is silent on whether the opinion may be included (the permission may rest in the section the Form is used under), so `NOTHING` (limited by its own wording); reading B: "except ... approval" lifts the prohibition, so `JUST TRUE`. An "unless" or "except" once it is met is one of the six case-by-case questions of 2026-11-05.
- **F9. Form 41: "(set out ground of challenge in accordance with subsection 638(1) of the Criminal Code)"** (line 18818). Whether the ground is one of subsection 638(1) is the answer of the part that owns it, an input. Reading A (taken): a ground that the seam says is not one of 638(1) is `NOTHING` (the Form's direction is a direction to the person completing the Form, not a "no"); reading B: it is `JUST FALSE`.
- **F10. Form 46: "the court adjudged*" and the seven alternatives** (lines 18850-18857). The asterisk after "adjudged" has no footnote in this text. Reading A (taken): the court ticks one of (a) to (g), and the function takes the one ticked. Reading B: more than one may be combined (for example a fine under (c) with an intermittent sentence under (g)), which the encoding does not model.
- **F11. Form 46 (g): "comply with the following conditions when not in confinement"** (line 18857). "When" counts as "where" (the 2026-11-05 ruling (c)), so a day in confinement is `JUST FALSE`. Reading B: a "when" limb that fails is a scope limit and the answer is `NOTHING`.
- **F12. Form 46: "for the period of ___ from the date of this order" and the four standing conditions** (line 18858). (i) The period is counted by fork F16. (ii) "promptly" fixes no period in the text, so the caller says whether the notice was prompt (a plain input) and the regulative rule takes the number of days as an input. (iii) "keep the peace and be of good behaviour" is a single standing condition, so the function takes it as one fact. (iv) A condition that did not arise (no change of address) is met vacuously. (v) For (a), (b), (c) and (g) the period runs from the date of the order; for (d), (e) and (f) from the date of expiration of the sentence of imprisonment or conditional sentence order (the text's own words).
- **F13. Form 48 and 48.1: the purposes introduced by "if"** (lines 18881-18883, 18897-18898). Purpose 3 "if the accused is a female person charged with an offence arising out of the death of her newly-born child"; purpose 4 "if a verdict of unfit ... or ... not criminally responsible ... has been rendered"; purpose 5 "if a verdict of unfit to stand trial has been rendered". Reading A (taken): a failed "if" is `JUST FALSE` (marginal reading (a)); reading B: `NOTHING`. For purpose 3, whether the child is a "newly-born child" is s 2's definition, an input: its answer passes through (`JUST FALSE` gives `JUST FALSE`, `NOTHING` gives `NOTHING`). The text of purpose 3 says "female person"; the seat asks it as a fact about the accused.
- **F14. Form 48 and 48.1: "in force for a total of ___ days, including travelling time"** (lines 18885, 18900). Counted by F16: the order is in force on the day of the order and on the following days up to the total. The text also says the assessment is "for a period of ___ days": the encoding does not test that the assessment period fits in the total, because the text does not say so in terms (Finding 8).
- **F15. Form 51 paragraph 1: "a day not earlier than 24 hours after the day on which the notice is served"** (line 18993). Reading A (taken): the day must be at least one calendar day after the day of service (a date shows no hour). Reading B: 24 hours after the moment of service, which a date cannot test. The times "at any time from (time) to (time)" are taken with both ends included.
- **F16. Counting a period that runs from a day** (every Form that says "for the term of", "for a period of", "for the period of ... from the date", "in force for a total of ... days", "for a period of ___ years after"). The Interpretation Act, which would say how, is not among the sources. Reading A (taken, `forms 24-54 the first day after a period that begins on a day`): the period begins on the day named and runs for the stated years, months and days (30 days from 1 January are 1 to 30 January; one month from 31 January ends at the start of 28 February, as `add months` clamps; "less a day" takes one day off). Reading B: the day named is excluded and the period begins the day after.
- **F17. Form 29: "an offence other than an offence mentioned in section 522"** (line 18533). "(other than X)" is one of the six case-by-case questions of 2026-11-05. Reading A (taken): an offence mentioned in s 522 is outside the Form and the answer is `NOTHING` (the Form says nothing of it); reading B: `JUST FALSE`. Whether the offence is mentioned in s 522 is the answer of the part that owns s 522, an input; the Form's section list "507, 508 or 512" is tested with the core's `Provision of the Code` (rule R1).
- **F18. A recital not made out** ("Whereas ... This is therefore to direct you / command you / authorize and require you", Forms 24, 25, 26, 27, 30, 47, 48, 48.1, 49, 50 and the openings of 52, 53, 54). Reading A (taken): `NOTHING` (limited by its own wording): the command rests on its recitals and the Form says nothing of what follows when one is not made out. Reading B: "therefore" is an "if" and a failed "if" is the text's no (marginal reading (a)), so `JUST FALSE`.
- **F19. A seam answer that is not `JUST TRUE`** (`s 2 peace officer`, `s 2 prison`, `s 2 justice`, `s 522`, `s 638(1)`, `s 490.011(1)`, `s 490.013`, ...). The Form addresses "the peace officers", "the keeper of the (prison)", "a justice". A caller whose borrowed term answers `JUST FALSE` is outside the Form, and the Form is silent about that case, so the answer is `NOTHING`, not `JUST FALSE`. Reading B: a borrowed term that the other part answers "no" is a "no" here.
- **F20. `form 32 part 6 the money the surety has promised or deposited may be forfeited`** (line 18596: "I understand that if the person who is giving this recognizance fails to comply with any of the conditions in this recognizance, the money that I have promised or deposited may be forfeited"). Named for a power ("may be forfeited"). When the person giving the recognizance has not failed to comply: reading A (taken) `NOTHING` (the "if" is not closed with "only if"; a grant limited by its own wording); reading B: `JUST FALSE` (a failed "if" is the text's own no).
- **F21. `form 52 para 5 the person may ask for a correction`** (line 19011: "If you believe that the information registered in the database contains an error or omission, you may ask ..."). Named for a power ("may ask"). When the person does not believe there is an error or omission: reading A (taken) `NOTHING`; reading B: `JUST FALSE` (a failed "if").
- **F22. `form 53 para 5 the person may ask for a correction`** (line 19029): as F21; reading A (taken) `NOTHING`; reading B `JUST FALSE`.
- **F23. `form 54 para 5 the person may ask for a correction`** (line 19044): as F21; reading A (taken) `NOTHING`; reading B `JUST FALSE`.
- **F24. `form 54 para 6.1 the person may apply to vary the duration`** (line 19046: "You have the right to apply to a court to vary the duration of the obligation ... if the obligation applies for life because you were convicted or found not criminally responsible ... for more than one offence"). Named for a right to apply ("may apply"). When the obligation does not apply for life because of more than one offence: reading A (taken) `NOTHING` (a right limited by its own "if"); reading B `JUST FALSE` (a failed "if").
- **F25. `form 54 para 6.1 the person may appeal the decision on the duration`** (line 19046: "... and you have the right to appeal the decision of that court"). Named for a right to appeal ("may appeal"); the right is stated in the same sentence as the "if" of F24. Same gate failing: reading A (taken) `NOTHING`; reading B `JUST FALSE`.

### Listed, not flipped (name-test sweep of 2026-11-12)

A function named for a grant or a power, answering `JUST FALSE`, whose gate is "where", "when", "upon" or an equivalent condition: not flipped, listed here, one row per function. Assumed, not ruled, that these equivalents go with the listed group; the other reading is for the maintainer or a lawyer (ruling (b) of the Guide's "Periods, where and scope limits" paragraph says `JUST FALSE`; the Guide's line on grants points to `NOTHING`).
- **F26. `form 29.1 the endorsement authorizes the release of the witness`** (line 18542: "This endorsement is subject to the following conditions: (specify conditions)"). Named for an authorization. The gate is "subject to the following conditions", an equivalent of "so long as" and "provided that": when a condition the endorsement specifies is not complied with the answer is `JUST FALSE` (taken); the other reading is `NOTHING` (a grant limited by its own wording).
- **"Entitled"-named functions: none in this part.**

## Jural relations (ccc31)

One row per group of provisions that creates a relation.
Hohfeld's correlatives: right and duty; privilege and no-right; power and liability; immunity and disability.
A provision that creates none (the caption, the identification, the dating and signing lines, a declarant's box, a record or certificate of a fact, a heading) is listed once as `none`.
Each relation is stated once, as a relation between two parties, and named neutrally; the L4 rule is the one rule that encodes it (the seat layer restates none).
The keel's `Party` type has no sheriff, fingerprint examiner or Review Board chairperson: they appear below as the Forms name them (NEEDS-CORE.md).

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | Form and lines | L4 rule |
| --- | --- | --- | --- | --- |
| the captions, headings, identification of persons, dating, signing and sealing lines of every Form; Forms 28.1 (repealed), 31, 33, 36, 37, 38, 42, 43, 44, 45 (records and certificates); the declarant's boxes and declarations of Forms 34.1, 34.2, 34.3, 48.2; the signatories' own agreements in Form 32; RELATED PROVISIONS | none | none | see the coverage table | none |
| the direction to arrest and convey a witness who would not enter into a recognizance | power: the justice or clerk who issued the warrant, and through it the peace officers, to arrest if necessary and convey the witness | duty: the peace officers to convey and deliver; liability: the witness to be arrested and conveyed | Form 24, 18468-18471 | `form 24 the peace officers are directed to arrest and convey the witness`, `form 24 the duties of the peace officers and the keeper` |
| the keeper's custody of that witness until the trial | right: the court and the accused (the witness is held for the trial); privilege/power: the witness, who ends the custody by entering into the recognizance | duty: the keeper to receive and keep; liability: the keeper to release when the witness enters into the recognizance; no-right: the keeper to hold on after the trial | Form 24, 18472 | `form 24 the keeper is directed to keep the witness in custody` |
| the warrant for contempt: arrest, conveyance, and custody for the term | power: the court that convicted; right: the court | duty: the peace officers and the keeper; liability: the witness who defaulted | Form 25, 18480-18488 | `form 25 the peace officers are ordered to arrest and convey the defaulter`, `form 25 the keeper is ordered to keep the defaulter in custody` |
| the sufficiency of the warrant for the keeper | immunity: the keeper who keeps as the order directs | disability: anyone who would complain of the keeping | Form 25, 18485; Form 26, 18501 | `form 25 this is a sufficient warrant for the keeper`, `form 26 this is a sufficient warrant for the keeper` |
| the warrant for costs of an appeal | power: the court; right: the Clerk of the Court and the payee of the costs | duty: the peace officers and the keeper; liability: the person adjudged to pay; power of that person to end the custody by paying the sum, the costs and the charges | Form 26, 18497-18501 | `form 26 the peace officers are commanded to take and convey the defaulter`, `form 26 the keeper is commanded to keep the defaulter in custody` |
| the warrant on forfeiture of amounts | right: Her Majesty (the judgment debt); power: the judge or clerk who issued it | duty: the sheriff to arrest and convey, the keeper to keep; liability: the defaulter; the defaulter's power to end the custody by satisfying the debt | Form 27, 18509-18512 | `form 27 the sheriff is ordered to arrest and convey the defaulter`, `form 27 the keeper is ordered to keep the defaulter in custody` |
| the endorsement authorizing arrest in another division | power: the justice who endorses | liability: the accused (arrestable within the territorial division named) | Form 28, 18522 | `form 28 the endorsement authorizes the arrest of the accused` |
| the endorsement authorizing release | power: the justice who endorses; privilege: the officer who releases under s 499 | liability: the accused (released); no-right: anyone to insist on detention | Form 29, 18533 | `form 29 the endorsement authorizes the release of the accused under section 499` |
| the endorsement authorizing release of a witness | power: the judge or justice; privilege: the person released | liability: the witness (released subject to the conditions the endorsement specifies) | Form 29.1, 18541-18542 | `form 29.1 the endorsement authorizes the release of the witness` |
| the order to bring the accused before a justice | right: the justice and the court; power: the justice who made the order | duty: the keeper to have the accused before the justice at the place and hour; right: the accused to be dealt with according to law | Form 30, 18551-18552 | `form 30 the keeper is directed to have the accused before the justice`, `form 30 the duty of the keeper` |
| the recognizance's forfeiture | power: the court (to forfeit); the Crown | liability: the person giving the recognizance, and the surety, who may lose the amount or security promised or deposited on a failure to comply | Form 32 parts 2 and 6, 18580, 18596 | `form 32 part 2 the amount or security may be forfeited`, `form 32 part 6 the money the surety has promised or deposited may be forfeited` |
| the duty to list the conditions and their duration | right: the person giving the recognizance (to know the conditions and for how long) | duty: the court or clerk completing the Form | Form 32 part 3, 18581-18582 | `form 32 part 3 the recognizance lists the conditions ordered and the duration of each` |
| the power to apply to cancel or vary a condition | power: the person giving the recognizance (to apply to a judge or a justice of the peace) | liability: the court, which must hear and may vary | Form 32 part 4, 18583-18584 | `form 32 part 4 the person may apply to cancel or vary a condition` |
| the duration of the conditions | right: the person (conditions end when cancelled, changed, or the person is discharged, sentenced or detained) | duty: the person to comply while they last; disability: the court to hold the person to them after | Form 32 part 5, 18585-18586; part 6, 18588-18590 | `form 32 part 5 the conditions remain in effect`, `form 32 part 6 the person must comply with the condition` |
| the surety's declaration | none stated beyond the choice of two boxes (declaration attached, or surety excepted) | the surety | Form 32 part 6, 18597-18599 | `form 32 part 6 the surety declaration box that applies` |
| the List of Conditions | power: the court (to order the conditions under the sections cited) | liability: the person (to the condition ordered) | Form 32, 18608-18632 | `form 32 the condition is listed for the section` |
| the writ of fieri facias | power: Her Majesty's creditors named in the writ, through the sheriff | duty: the sheriff to levy the amount set opposite each name and to make a return; liability: each person named (goods, chattels, lands and tenements) | Form 34, 18645-18647 | `form 34 the amount the sheriff is commanded to levy from the person`, `form 34 the sheriff is commanded to make a return`, `form 34 the duties of the sheriff` |
| the statement on restitution | right: the victim (to claim restitution); power: the court | duty: the declarant to provide documents; the loss must be readily ascertainable; liability: the offender to be ordered to make restitution | Form 34.1, 18656-18667 | `form 34.1 the statement is addressed to a court sentencing an offender convicted or discharged under section 730`, `form 34.1 the loss may be claimed as restitution`, `form 34.1 the declarant is responsible for providing the documents` |
| the victim impact statement, the community impact statement and the one for a person found not criminally responsible | privilege: the victim or community (to present what the Form allows); immunity: the offender or accused (against the content the Form excludes: unproven allegations, comments about offences not proved, complaints about others, opinions about the sentence without approval) | no-right: the declarant (to include the excluded content); disability: the declarant without the court's approval | Forms 34.2, 34.3, 48.2, 18672-18714, 18716-18750, 18908-18948 | `form 34.2 the statement may include the item`, `form 34.3 the statement may include the item`, `form 48.2 the statement may include the item` and the three `... this is an application for compensation or restitution` and `... the declarant is required to include all the examples` |
| the punishment imposed and the default term | power: the court; right: the Crown to the sums | duty: the accused to pay forthwith or within the time fixed; liability: the accused to imprisonment in default, unless sooner paid | Form 35, 18758-18759 | `form 35 the imprisonment in default of payment still applies` |
| the order to discharge a person in custody | right: the person detained (to be released); power: the judge, justice or clerk | duty: the keeper to release if the person is detained for no other cause | Form 39, 18795-18796 | `form 39 the keeper is directed to release the person`, `form 39 the duty of the keeper` |
| the challenges to the array and for cause | power: the prosecutor and the accused (to challenge) | liability: the sheriff or deputy sheriff who returned the panel; the juror challenged | Forms 40 and 41, 18807, 18818 | `form 40 the challenge to the array is in the Form's terms`, `form 41 the challenge for cause is in the Form's terms` |
| the probation order's conditions | power: the court; right: the court and the probation officer (to compliance) | duty: the offender to keep the peace and be of good behaviour, appear when required, notify in advance of a change of name or address, promptly notify of a change of employment or occupation, for the period; liability: the offender | Form 46, 18851-18859 | `form 46 the conditions begin on`, `form 46 the offender must comply with the conditions on the day`, `form 46 the offender is in compliance with the standard conditions`, `form 46 the additional condition may be stated`, the four `form 46 the duty to ...` rules |
| the order to disclose income tax information | power: the judge and the police officers named | duty: the addressee to produce the information and documents; liability: the person whose information it is | Form 47, 18868-18870 | `form 47 the order authorizes and requires the addressee to produce the information`, `form 47 the production meets the order`, `form 47 the duty of the addressee` |
| the assessment orders | power: the court (Form 48) and the Review Board (Form 48.1) to order an assessment on reasonable grounds | liability: the accused, who is assessed for the period, in custody or out of custody on conditions; duty: the accused to comply with the conditions | Forms 48 and 48.1, 18878-18903 | `form 48 the court has grounds to order an assessment for the purpose`, `form 48 the order is in force`, `form 48 the accused is to remain in custody or out of custody`, `form 48 the accused must comply with the condition` and the `form 48.1` counterparts |
| the warrants of committal for the mentally disordered | power: the court or Review Board; privilege: the keeper (delegated powers over the accused's liberty) | duty: the peace officers to convey; the keeper to receive and keep until delivered by due course of law; liability: the accused, to the conditions and the delegated restrictions while in the place | Form 49, 18956-18965; Form 50, 18975-18985 | `form 49 ...` (five rules), `form 50 the keeper is commanded to execute the warrant`, `form 50 the duty of the keeper` |
| the notice to provide samples | power: the Attorney General (the place designated) and the court (to order samples) | duty: the person to report on a permitted day, within the hours, every stated number of days (not less than seven); liability: a fine or imprisonment, or both, or proceedings under s 742.6; right: to apply to terminate, to appeal | Form 51, 18991-18997 | `form 51 the person is subject to the obligation to provide samples`, `form 51 para 1 ...` to `form 51 para 5 ...` |
| the sex offender registration order and notices | power: the court and the Attorney General or minister of justice (identifying equivalent offences); the registration centre (to collect and register) | duty: the person to report for the first time and subsequently for the period or for life, to provide true information; liability: a fine or imprisonment, or both; right: to ask for a correction, to apply to terminate, to be exempted or to vary the duration, and to appeal | Forms 52, 53, 54, 19006-19049 | `form 52 ...`, `form 53 ...` and `form 54 ...` (the rules named in the coverage table) |

## Marginal readings for a lawyer (ccc31)

The two readings the brief leaves open for a lawyer, applied as the status quo (the rule of 2026-10-29; assumed, not ruled): (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.

Branches that rest on reading (a) (the other reading: `NOTHING`, because "if A then B" does not itself say "if not A then not B"):
- `form 29.1 the endorsement authorizes the release of the witness`: a condition the endorsement specifies is not complied with ("subject to the following conditions"): `JUST FALSE`. It is named for an authorization; it is listed, not flipped, in the fork register (F26).
- `form 48 the court has grounds to order an assessment for the purpose` (purposes 3, 4, 5) and `form 48.1 the Review Board has grounds to order an assessment for the purpose` (both purposes): the "if" fails: `JUST FALSE` (fork F13).
- `form 51 para 4 the consequence of not complying`, `form 52 para 7`, `form 52 para 8`, `form 53 para 8`, `form 53 para 9`, `form 54 para 8`, `form 54 para 9`: the person is not found to have contravened, not complied or provided false information ("If you are found to"): `JUST FALSE` or the "no consequence" constructor.
- `form 39 the keeper is directed to release the person`: detained for another cause ("if E.F. is detained by you for no other cause"): `JUST FALSE`.
- `form 49 the accused is subject to the condition`: the accused is not in the keeper's place ("while in your (prison, hospital or other appropriate place)"): `JUST FALSE`.
- `form 46 the offender must comply with the conditions on the day` for paragraph (g): in confinement ("when not in confinement"): `JUST FALSE` (fork F11).
- `form 52 para 1`, `form 53 para 1`, `form 54 para 1` and `form 52 para 2 the person must report on the day` (and 53, 54): not "required under subsection 4(1) or 4(2)", or under "section 4.1 or 4.3", of the Sex Offender Information Registration Act ("whenever required": the "whenever" counts as "where", ruling of 2026-11-05 (c)): `JUST FALSE`.
- The "until" and "unless" branches of forks F1 and F6 (the witness has entered into the recognizance, the trial has taken place, the sums are sooner paid, delivery by due course of law, the end events of Form 32 part 5) rest on the ruling of 2026-11-05 (d) and, for "unless once met", on the six case-by-case questions of the same date.
- Flat negatives counted as the text's no (ruling N2): `form 34.1 the loss may be claimed as restitution` ("must be readily ascertainable"); `form 34.2`, `form 34.3` and `form 48.2` `the statement may include the item` ("Your statement must not include"), `... this is an application for compensation or restitution` ("this is not an application"), `... the declarant is required to include all the examples` ("You are not required"); `form 51 para 1 the first report is on a permitted day` ("not earlier than"); `form 51 para 2 the number of days stated is permitted` ("not less than seven").
- Periods the text fixes in its own words, outside which the answer is `JUST FALSE` (ruling of 2026-11-05 (a)): every term, period and "total number of days" (Forms 25, 26, 27, 35, 46, 48, 48.1) and the reporting periods of Forms 52, 53 and 54.

Branches that rest on reading (b) (a grant or command limited by its own wording and the case outside the limit: `NOTHING`; the other reading: `JUST FALSE`):
- the seven functions the name-test sweep of 2026-11-12 moved from `JUST FALSE` to `NOTHING` because each is named for a power or a right and its "if" gate failed (the other reading, `JUST FALSE`, a failed "if" read as the text's own no; one fork line each in the fork register): `form 32 part 2 the amount or security may be forfeited` (F4) and `form 32 part 6 the money the surety has promised or deposited may be forfeited` (F20), no failure to comply; `form 52 para 5`, `form 53 para 5` and `form 54 para 5` `the person may ask for a correction` (F21, F22, F23), the person does not believe there is an error or omission; `form 54 para 6.1 the person may apply to vary the duration` and `... may appeal the decision on the duration` (F24, F25), the obligation does not apply for life because of more than one offence.
- every command of a "Whereas ... This is therefore" Form whose recital is not made out (fork F18), and every borrowed-term seam that is not `JUST TRUE` (fork F19);
- `form 28 the endorsement authorizes the arrest of the accused`: the arrest is outside the territorial division ("within the (territorial division)");
- `form 29 the endorsement authorizes the release of the accused under section 499`: another section, or an offence mentioned in s 522 (fork F17);
- `form 25 this is a sufficient warrant for the keeper` and `form 26 this is a sufficient warrant for the keeper`: the keeper does not keep as directed ("for so doing");
- `form 32 part 4 the person may apply to cancel or vary a condition` ("any condition in this form", "a judge or a justice of the peace"); `form 32 part 6 the person must comply with the condition`; `form 32 the condition is listed for the section` (fork F7);
- `form 34 the amount the sheriff is commanded to levy from the person`: a person not named in the writ;
- `form 40` and `form 41`: a challenger who is not the prosecutor or the accused, a ground the Form does not name (fork F9);
- `form 48 the accused is to remain in custody or out of custody`, `form 48 the accused must comply with the condition` (and 48.1), `form 50 the keeper is commanded to execute the warrant`: the box not ticked;
- `form 34.1 the declarant is responsible for providing the documents`; the statement-content functions for content the Form does not name (the examples are not a closed list) and, with approval, for an opinion or recommendation (fork F8);
- the paragraphs 3, 4, 5, 6 and 7 functions of Forms 51 to 54 for a person who is not the person the notice is given to, and the "appeal the decision" functions where no court has decided the application ("any decision of that court").

### Name-test sweep of 2026-11-12

Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorized" was read against the three tests of the lead's instruction: 33 functions.
Nineteen of them answer only `JUST TRUE` or `NOTHING` and have no `JUST FALSE` branch to examine (the Form 28, 29, 32 part 4, 46, 47, 49, 51 paragraph 3 and 5, and Forms 52 to 54 paragraph 6 and 7 functions among them).
The other 14 had a `JUST FALSE` branch: seven were flipped, six kept, one listed.
A bar, a duty, or a question that is not named for a grant or a power keeps `JUST FALSE` and is not counted.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 7 | 6 | 1 | 0 |

Flipped to `NOTHING` (the gate is an "if" that the text does not close with "only if"; one fork line each, F4 and F20 to F25; the other reading is `JUST FALSE`, a failed "if" read as the text's own no):
- `form 32 part 2 the amount or security may be forfeited`
- `form 32 part 6 the money the surety has promised or deposited may be forfeited`
- `form 52 para 5 the person may ask for a correction`
- `form 53 para 5 the person may ask for a correction`
- `form 54 para 5 the person may ask for a correction`
- `form 54 para 6.1 the person may apply to vary the duration`
- `form 54 para 6.1 the person may appeal the decision on the duration`

Kept `JUST FALSE` (the text closes the gate itself):
- `form 51 para 1 the first report is on a permitted day` ("not earlier than 24 hours after the day on which the notice is served")
- `form 51 para 2 the number of days stated is permitted` ("not less than seven")
- `form 34.1 the loss may be claimed as restitution` ("must be readily ascertainable by the court")
- `form 34.2 the statement may include the item`, `form 34.3 the statement may include the item` and `form 48.2 the statement may include the item` ("Your statement must not include", and "except with the court's approval" for the opinion or recommendation: a prohibition and its exception, closed by the text)

Listed, not flipped, "may" with where/when/upon or an equivalent ("subject to the following conditions", read as "so long as"): `form 29.1 the endorsement authorizes the release of the witness` (F26).

Listed, "entitled"-named: none.

Outside the sweep: named "it is lawful": 0 (no layer-1 function and no seat question of this part has "lawful" in its name).

Callers: the seat questions "Under Form 32 part 2, ..." and "Under Form 32 part 6, ..." return the flipped functions, so their `@export` texts now say "null = the person has not failed to comply" and their cases expect `NOTHING`; no layer-1 function reads a flipped function.

## Rulings carried, word for word

Each ruling is recorded again, word for word, in the NOTES.md of each row that carries that rule's `NOTHING-kind` tags: this row has a fork register, so they are recorded here, copied by script from the brief.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Where each ruling bites in this range: N2 (a flat negative counts as the text's no): `form 34.1 the loss may be claimed as restitution`, the statement-content functions ("must not include", "is not an application", "not required"), `form 51 para 1` and `para 2` ("not earlier than", "not less than seven"). Periods, "where" and scope limits: (a) every term, period and total number of days of Forms 25, 26, 27, 35, 46, 48, 48.1 and the reporting periods of Forms 52 to 54; (b) "if", "while" and "whenever" limbs (Forms 29.1, 39, 48, 48.1, 49, 51, 52 to 54; where the function is named for a grant or a power and its "if" fails, the answer is NOTHING: forks F4 and F20 to F25); (c) the "when" limb of Form 46 (g) and the limits of a grant ("within the (territorial division)", "to one of the following police officers", the sections after each condition of Form 32). Delegated definitions: (a) the List of Conditions of Form 32 and the section list of Form 29 are lists the Form hands to sections, tested as R1 lists, with `NOTHING` outside them (fork F7, F17); (b) no "it is a defence" in this range; (d) the "until" bars of Forms 24, 32 part 5 and 49 (forks F1, F6). Case by case: "an unless or except once it is met" (F1, F8), "a bare must not done" (F5), "(other than X)" (F17), "a duty whose if or where is unmet" (F13, Forms 52 to 54); each site has its fork line.

## Seams (ccc31)

PLAN.md section 6 lists no seams for ccc31 beyond "the section 2 terms it will meet", and the brief's "PLAN.md section 8" does not exist in the copy of PLAN.md this part was given (it ends at section 6).
So each seam below is either one the plan names (`s 2 <term>: ...`, PLAN.md section 4, taken from the keel's `ccc-definitions.l4`) or one found in the text and named in the plan's convention `s <label> <what is asked>` (rule R4: typed `MAYBE BOOLEAN` so that a caller never turns NOTHING into FALSE).
The seat layer passes the plain fact as `JUST <fact>` (NOTES.md "Seat"); the lead's merged seat takes the answer from the part that owns the section.

Taken from the plan (section 2 terms of `ccc-definitions.l4`), all `MAYBE BOOLEAN`:
- `s 2 peace officer: the person addressed is a peace officer in the territorial division` (Forms 24, 25, 26, 49; the plan marks `peace officer` as able to answer NOTHING). Forms 27 and 34 are addressed to the sheriff, who is a peace officer by paragraph (a) of the definition in s 2 ("peace officer includes (a) a mayor, warden, reeve, sheriff, deputy sheriff, sheriff's officer and justice of the peace", line 140): the regulative rules use `a peace officer` as the actor and the wanted constructor `the sheriff` is recorded in NEEDS-CORE.md.
- `s 2 prison: the place named is a prison` (Forms 24, 25, 26, 27; `prison` can answer NOTHING).
- `s 2 justice: the person who signs the endorsement is a justice` (Form 28; `justice` answers no NOTHING in the keel).
- `s 2 newly-born child: the child is a newly-born child` (Form 48 purpose 3; `newly-born child` can answer NOTHING).
Terms the range meets and that no rule of this part turns on, so no input was needed: `day`, `territorial division`, `offender`, `mental disorder`, `recognizance`, `clerk of the court`, `property`, `provincial court judge`, `Attorney General` (the plan counts them by occurrence in the range; they occur in the Forms' wording, not in any condition a function tests).

Found in the text, not in the plan (each a `MAYBE BOOLEAN` input of the function that needs it; the part that should answer is named):
- `s 522 the offence is mentioned in section 522` (Form 29, line 18533): the part that owns s 522 (Part XVI, release by a judge).
- `s 638(1) the ground is a ground of challenge under subsection 638(1)` (Form 41, line 18818): the part that owns s 638.
- `s 732.1(3) the condition is one the court may prescribe under subsection 732.1(3)` (Form 46, line 18859): the part that owns s 732.1.
- `s 490.011(1) the offence is a designated offence` (Form 52, line 19006); `s 490.011(1) the offence is referred to in paragraph (a), (c), (c.1), (d), (d.1) or (e) of the definition designated offence` (Form 53, line 19024); `s 490.011(1) the equivalent offence is referred to in paragraph (a) of the definition primary offence` (Form 54, line 19038-19039): the part that owns s 490.011.
- `s 227 of the National Defence Act the offence is referred to in paragraph (a) or (c) of the definition designated offence` (Form 53, line 19024): an Act that is not among the sources; a plain input.
- `s 490.013(2)(c) the order applies for life`, `s 490.013(3) ...`, `s 490.013(5) ...`, `s 490.013(6) ...` (Form 52 paragraph 2, line 19008); `s 490.022(3)(c) the obligation applies for life`, `s 490.022(3)(d) ...` (Form 53 paragraph 2, line 19026); `s 490.02904(3)(c) the obligation applies for life`, `s 490.02904(3)(d) ...` (Form 54 paragraph 2, line 19041): the parts that own those sections. Any one answering `JUST TRUE` makes the period "for life"; all answering `JUST FALSE` leaves the period of years; any other answer is `NOTHING` (tested).
- The shorter periods "set out in subsection 490.022(2)" and "determined under subsection 490.02904(2)" (Forms 53, 54) are taken as two plain inputs (a flag and a number of years); the owner of those subsections may answer them.
- Plain facts of other Acts: whether a person is "required under subsection 4(1) of that Act", "under subsection 4(2)", "under section 4.1 or 4.3" of the Sex Offender Information Registration Act (not among the sources) are BOOLEAN inputs (`the person is required to report ...`).
- Cross-references only (cited in the Forms, no input needed, because the Form's own words carry the rule and the cited section's answer is not asked): sections 763 and 764 (Form 32 part 5), 515.1 and 515.1(2) (the surety declaration), 499 and 522 (Form 29), 705(4) and (5) (Form 29.1), 730 (Form 34.1), 16(1), 672.54, 672.58, 672.64, 672.84(1), 672.84(3), 672.851 (Forms 48 and 48.1), 742.6 (Form 51), 462.32, 462.33(3), 462.37, 462.38 (Form 32 (o)).

Seams of the plan's section 3 used: rule R1 (a provision that names offences or sections by number is tested against the core record `Provision of the Code`): Form 29 (sections 507, 508, 512), Form 29.1 (section 705, subsections "(1)" and "(2)") and the List of Conditions of Form 32 (the section numbers of each condition, decimals: 810.01 is not 810, tested).
Rule R5 (a cycle between two parts): none found.

## Findings

### What the text turns out to say (numbered)

1. The plan's row for ccc31 ("sections 1 to 9 (38 section headings)") does not describe this range. The range holds 38 lines that begin `FORM ` (FORM 24 to FORM 54, with 28.1, 29.1, 34.1, 34.2, 34.3, 48.1 and 48.2 between them), counted by script, so the "38 section headings" are the 38 Form headings; "1 to 9" are the Forms' own internal numbered paragraphs (Forms 51 to 54 number theirs 1 to 9; Form 32 has parts 1 to 6). Naming a function `s 1 ...` or `s 550 ...` would collide with the keel's `s 1 the short title` and with the part that owns section 550, so every name is `form N ...`.
2. Eleven lines of the range carry an asterisk with no footnote anywhere in this rendering: 18485 (Form 25, "keep them safely there*"), 18756 (Form 35, "namely,*"), 18830 (Form 43, "issued by (set out court or justice, as the case may be).*"), 18850 (Form 46, "the court adjudged*"), 18878 (Form 48, "may be necessary to determine *"), 18885 (Form 48, "the accused is to remain *"), 18896 and 18900 (Form 48.1), 18959 and 18978 (Forms 49 and 50, "the accused was found*"), 18983 (Form 50, "to command you ... to*"). Each marks a choice among the alternatives that follow it (boxes or paragraphs (a) to (g)); the instruction to choose is not in the text. The functions take the alternative chosen as an input (forks F10 and others).
3. Form 28.1 has a heading with no title and the text "[Repealed, 2007, c. 22, s. 26]" (line 18527), the only repealed unit of the range. Forms 44 and 45 have a heading ("FORM 44 (Section 667)", "FORM 45 (Section 667)") and no title in this text.
4. Form 25's third recital carries a drafting instruction inside the Form: "And because the defaulter has not paid the amounts ordered to be paid; (delete if not applicable)" (line 18483). The function reads it as a recital that stands only where amounts were ordered, and tests both sides.
5. Form 32's heading names fifteen sections (2, 462.34, 490.9, 550, 683, 706, 707, 779, 810, 810.01, 810.03, 810.1, 810.2, 817 and 832) and its List of Conditions cites fourteen (83.3, 462.34, 490.9, 550, 706, 707, 779, 810, 810.01, 810.03, 810.1, 810.2, 817, 832), computed by script. Section 83.3 appears in conditions (b) and (c) and not in the heading; sections 2 and 683 are in the heading and no condition cites them.
6. Form 32 condition (e) ("wears an electronic monitoring device (if the Attorney General makes the request)") cites 810.01, 810.1 and 810.2 and (e.1) ("if the Attorney General has consented to this condition") cites 810.03 only, so the request-or-consent distinction follows the section.
7. Forms 52, 53 and 54 are three versions of one notice. Only Forms 53 and 54 add "or for any shorter period set out in subsection 490.022(2)" and "... determined under subsection 490.02904(2)"; Forms 53 and 54 have an exemption paragraph (6, "exempt you from the obligation") and a termination paragraph (7), and Form 54 adds a paragraph 6.1 (vary the duration, if the obligation applies for life because of more than one offence); Form 52 has no exemption paragraph and its paragraph 6 is termination. Form 52 and Form 53 name "the Canadian Forces Provost Marshal" in paragraph 5 ("if applicable") and Form 54 does not.
8. Form 48 and Form 48.1 say both "for a period of ___ days" (the assessment) and "in force for a total of ___ days, including travelling time" (the order). The text does not say that the second is at least the first, though "including travelling time" implies it, so no function tests it (fork F14).
9. Form 29 says "Whereas this warrant is issued under section 507, 508 or 512 ... in respect of an offence other than an offence mentioned in section 522 ..., I hereby authorize the release of the accused pursuant to section 499": the justice's endorsement is what lets the officer in charge release under s 499, and it does so only for those three sections and those offences (fork F17).
10. Forms 34.2, 34.3 and 48.2 are one Form three times, with three differences: Form 34.3's first prohibition speaks of "harm or loss suffered by the community" and its Form asks the community's name and "how the statement reflects this community's views"; Form 48.2 speaks of "conduct" and of the accused "not found not criminally responsible", and its approval is "the court's or Review Board's"; Form 34.2 and 34.3 have a drawing, poem or letter section and Form 34.3 has no "present in court" and "receive information" pair (one box only).
11. Form 46's paragraph (e) says "the offender's conditional sentence order related to this or another offence" and (f) "the offender's sentence of imprisonment related to another offence": a conditional sentence order may be for this offence, a sentence of imprisonment under (f) only for another (the sentence for this offence is (d)).
12. Forms 51 and 46 carry rules in their drafting instructions ("(specify a number not less than seven)", "(specify a day not earlier than 24 hours after the day on which the notice is served)", "(here state any additional conditions prescribed pursuant to subsection 732.1(3))"): they are rules about the content of the document, encoded as such (`form 51 para 1 ...`, `form 51 para 2 ...`, `form 46 the additional condition may be stated`).
13. The text still says "Elizabeth II by the Grace of God", "Her Majesty's name", "The Queen v. C.D." and "Her Majesty the Queen" (Forms 24 to 27, 34, 40, 41, 49, 50); they are wording, and the encoding speaks of "Her Majesty" only where a function is about a debt due to her (Form 27).
14. The range ends at the blank line 19055 after the heading RELATED PROVISIONS (line 19054); the first related provision (1991, c. 43, s. 10) begins at line 19056, in part ccc32.
15. Form 24's recital says the accused "was committed for trial on a charge", and the witness "appeared as a witness on the preliminary inquiry": the Form is the warrant for a witness at the preliminary inquiry who will not enter into a recognizance to appear at the trial. It is not a warrant for the accused, who appears in the seat layer as the person whose trial the witness is held for.

### What the stable binary does not accept

Measured in this session on 1.6.110 (main, e51181d) and rerun on 1.6.109 (main, 4c887e0); each probe was a small file run with `l4 check` or `l4 run`.
- A trace cannot be asserted. `#ASSERT `rule` EQUALS FULFILLED` is "assertion could not be evaluated"; `#ASSERT (`rule` AT 0 WITH PARTY ... DOES ... AT 1) EQUALS FULFILLED` is a parse error (`unexpected AT`). So each regulative rule of this part is run with `#TRACE` (its outcome is printed and read by eye, and recorded in the test file's comment) and its duty is also a decision function over the facts, which carries the assertions. `check.sh` counts no trace. The outcomes of the 20 traces were compared by running the three test files that hold them on both builds and diffing the whole output: identical.
- `x IS IN list` is a parse error (`unexpected IS`); the prelude's `elem x list` is accepted. Write `elem (section's `section`) (list)`: without the brackets `elem section's `section`` reads as `(elem section)'s `section``.
- A pattern that names the fields of a constructor, `WHEN `c` WITH x THEN`, is a parse error (`unexpected WITH`); the binding form `WHEN `c` x THEN` is accepted.
- `TEXT` is not a type (`STRING` is); `CONCAT "for " (TOSTRING n) " years"` (no commas) is a parse error and `CONCAT "for ", TOSTRING n, " years"` is accepted.
- Accepted, and used throughout: parentheses, apostrophes, colons, decimal points and digits inside backtick names (`form 34.2 ...`, `s 2 peace officer: the person ...`, `form 32 condition (e.1) ...`); `MAYBE BOOLEAN` and `MAYBE` of a declared type; `PROVIDED NOT paid` on a `SHANT` whose action carries the payload (`entered`, a fresh name bound by the event); `WAITUNTIL`; `Date day month year` and `DATE PLUS NUMBER`; `Day date`; `add months`.
- Not probed and therefore not claimed: `@export` on a function with no inputs (the seat has none such), and the `unstable` dialect.

### Limits of this work

- The expected values of the tests are written by hand from the text before each run, but by the same agent that wrote the functions. The independent test pass the skill recommends (a fresh session that decides the answers before reading the encoding) was not run: no subagent was available.
- `work/verify-quotes.py` checks that each quoted fragment occurs, in order, somewhere in the text of the range, not that it occurs in the Form the function cites; `srcrefs.py check --refs` and `--strict` check the quotation lines and the `@ref` locators. Neither checks that an encoding means what the text says: that is for a reviewer.
- A function asked about a day uses dates; a time of day is a number of minutes after midnight (the keel counts `day` and `night` the same way).
- The seat layer asks seam answers as plain facts (NOTES.md "Seat"); a person who does not know whether an offence is "mentioned in section 522" must answer false, and the result then reads `null`, never "false".

## Open questions for a domain expert

- Fork F16: does the Interpretation Act count the day named as the first day of a period "from" it? The answers of every term, period and "total number of days" move by a day if it does not.
- Fork F2: does "unless the sums ... are sooner paid" in Form 25 (c) reach the first term?
- Fork F1: is "until the trial" the beginning or the end of the trial (Form 24)?
- Fork F8: with the court's approval, may an opinion or recommendation about the sentence be included (Forms 34.2, 34.3, 48.2)?
- Is the sheriff of Forms 27 and 34 to be a distinct `Party` (the encoding takes a peace officer)?
- What do the eleven asterisks of Finding 2 say?

## What `check.sh` printed

Target `main`: every module is run with the stable `l4` that wrote it (1.6.110, main, e51181d, 2026-11-11) and with a second stable build (1.6.109, main, 4c887e0, 2026-11-04); the main columns must match. Environment: `JL4_LIBRARY_PATH` unset. Command: `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`.

**Baseline (the keel's three files, before any ccc31 file existed), `work/baseline.txt`:**

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
TOTAL (3 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**Final run, `work/check-final.txt`:**

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc31-cases-seat.l4                            0       232       0        0         0 |      0       232       0        0  same
ccc31-forms-custody.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-orders.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-periods.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-process.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-soira.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc31-forms-statements.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc31-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc31-tests-custody.l4                         0        93       0        0         0 |      0        93       0        0  same
ccc31-tests-orders.l4                          0       113       0        0         0 |      0       113       0        0  same
ccc31-tests-periods.l4                         0        17       0        0         0 |      0        17       0        0  same
ccc31-tests-process.l4                         0       116       0        0         0 |      0       116       0        0  same
ccc31-tests-soira.l4                           0       136       0        0         0 |      0       136       0        0  same
ccc31-tests-statements.l4                      0        53       0        0         0 |      0        53       0        0  same
TOTAL (17 modules)                             0       760       0        0           |      0       760       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

A negative control was run on a copy of the folder: one expected value in `ccc31-tests-process.l4` was changed to a wrong value, and `check.sh` exited 1 with that file at 1 error, 115 satisfied, 1 failed (and the same on the main build); the copy was then deleted.

No test is expected to fail, so `expected_failed` in `check.sh` is empty and every `expected` column reads 0.

**Source locators**, `python3 -I srcrefs.py check --refs <text> <files>` and `--strict`, over all layer-1 files and tests (layer 2 and the tests carry no quotation lines):

```
srcrefs --refs:
srcrefs check: 490 src: lines, 29 runs, 145 locators, 0 problems
srcrefs --strict:
srcrefs check: 490 src: lines, 29 runs, 145 locators, 0 problems
```

**Kinds and quotations**, `python3 -I work/verify-quotes.py`:

```
verify-quotes: 115 NOTHING branches, 74 JUST FALSE branches, 206 quoted fragments, 0 problems
```

**Every rule is exercised**, `python3 -I work/check-asserted.py` (every top-level name defined in a layer-1 module occurs as the target of an `#ASSERT` or `#TRACE` in a test file):

```
top-level names defined in the layer-1 modules: 123; asserted or traced directly in a test file: 123; reached only through an asserted seat question: 0; not exercised: 0
```

**Warnings**: `l4 check` on every file, filtered for the two printed warnings the skill names ("is at the end of the file", "follows code on its line") and for any `Warning` severity:

```
(warning filter over 14 files: lines above, if any)
```

## Files

In this folder: `NEEDS-CORE.md`, `NOTES.md`, `PROGRESS.md`, `ccc-core.l4`, `ccc-definitions.l4`, `ccc-interpretation.l4`, `ccc31-cases-seat.l4`, `ccc31-forms-custody.l4`, `ccc31-forms-orders.l4`, `ccc31-forms-periods.l4`, `ccc31-forms-process.l4`, `ccc31-forms-soira.l4`, `ccc31-forms-statements.l4`, `ccc31-seat.l4`, `ccc31-tests-custody.l4`, `ccc31-tests-orders.l4`, `ccc31-tests-periods.l4`, `ccc31-tests-process.l4`, `ccc31-tests-soira.l4`, `ccc31-tests-statements.l4`, `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`.

The keel's `ccc-core.l4`, `ccc-definitions.l4` and `ccc-interpretation.l4` are read-only copies; `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are the supplied ones; `PROGRESS.md` is this part's working record.
