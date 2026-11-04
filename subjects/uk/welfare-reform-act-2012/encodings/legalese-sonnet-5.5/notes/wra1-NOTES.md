# NOTES (wra1): the Welfare Reform Act 2012 (United Kingdom), 2012 c. 5, Part 1 and Schedules 1, 2, 5 and 6

Status: draft. No domain expert has read this against the source.
Written by agent `wra1` of run `iaw-wra1` (model Sonnet 5.5, stable `l4` 1.6.98, compared with the main build 1.6.108).
Target dialect: `main`, compiled by the stable build; every module has the same four counts on both builds.

## The source is not the official text

The only source is `inputs/ukpga-2012-5.txt`, a plain-text rendering made by a converter script from legislation.gov.uk.
It is not the official text, and nothing here is "verified against the official text".
`inputs/ukpga-2012-5.meta.json` records that the revised text may carry more than one extent version of a provision, and prospective provisions, which the converter does not distinguish.
A provision that appears to say two things may therefore be two versions, which is not a fork.
Licence: Crown copyright, Open Government Licence v3.0 ("Contains public sector information licensed under the Open Government Licence v3.0.").

## My ranges, and the seat

Lines 2-517 (Part 1, Chapters 1 to 3: sections 1 to 43), 2630-2922 (Schedule 1, "Universal credit: supplementary regulation-making powers", and Schedule 2, "Universal credit: amendments") and 3050-3173 (Schedule 5, "Universal credit and other working-age benefits", and Schedule 6, "Migration to universal credit"): 933 lines, 14,054 words, none blank.
The seat is the individual: a person who claims, receives or is moved to Universal Credit.
(A person who claims Personal Independence Payment, or whose benefits are capped, is served by the other parts.)
Layer 1 is the law objectively, in `wra1-*.l4` with `wra1-tests-*.l4`; layer 2 is `wra1-seat.l4` with `wra1-cases-seat.l4`, which asks the questions of that person and calls the layer-1 rules without restating them.

## Files

| file | what it holds | assertions satisfied / written |
| --- | --- | --- |
| `wra1-three-valued.l4`, `wra1-tests-three-valued.l4` | the Kleene helpers: `s 3(1) both of these are true` (AND), `s 19(2) either of these is true` (OR), `s 4(1)(d) the opposite of this` (NOT) over `MAYBE BOOLEAN` | 19 / 19 |
| `wra1-ch1-entitlement.l4`, `wra1-tests-ch1.l4` | sections 1 to 12: awards, claims, entitlement, the basic and financial conditions, the amount | 171 / 171 |
| `wra1-ch2-responsibilities.l4`, `wra1-tests-ch2.l4` | sections 13 to 29: work-related requirements, the four groups, sanctions, hardship payments, delegation; four regulative rules | 335 / 335, plus 11 `#TRACE` runs |
| `wra1-ch3-general.l4`, `wra1-tests-ch3.l4` | sections 30 to 43: abolished benefits, limited capability, couple, interpretation, pilot schemes | 103 / 103 |
| `wra1-sch1.l4`, `wra1-tests-sch1.l4` | Schedule 1: supplementary regulation-making powers | 48 / 48 |
| `wra1-sch2.l4`, `wra1-tests-sch2.l4` | Schedule 2: the amendments that put universal credit into other Acts | 116 / 116 |
| `wra1-sch5-6.l4`, `wra1-tests-sch5-6.l4` | Schedule 5 (universal credit and other working-age benefits) and Schedule 6 (migration to universal credit) | 110 / 110 |
| `wra1-seat.l4`, `wra1-cases-seat.l4` | layer 2: 48 exported questions and their cases | 199 / 199 |

Layer-1 assertions: 902.
With the seat cases: 1,101.
The keel's `wra-core.l4` and `wra-definitions.l4`, and the supplied `check.sh`, `srcrefs.py` and `fetch-main-l4.sh`, were put in the deposit for me and I did not edit them.
No `NEEDS-CORE.md`: no core type was lacking (Schedule 5 and 6 definitions are written over the core's `Provision that reduces an award` and `Work-related requirement`).

Every top-level name, including each type and constructor, begins with its provision label (`s 4(1)(a) ...`, `sch 6 para 5(4) ...`).
Some helper types and functions carry the label of a provision they do not implement, not because they restate it: `s 1(1) what I know` (the seat's yes / no / I do not know), and the Kleene helpers in `wra1-three-valued.l4` (`s 3(1) both of these are true`, `s 19(2) either of these is true`, `s 4(1)(d) the opposite of this`), are named under the provision where each is first needed, as PLAN.md section 2 requires, so that no two parts declare the same name.
A lead who skims names should not look for s 1(1) content in `what I know`, or for s 3(1), s 19(2) or s 4(1)(d) content in the helpers.
A Schedule 2 name begins `sch 2 <host Act short name> <host provision>` and carries no derived paragraph number (finding 8).

## Coverage (wra1)

How to read the table.
Each row names the raw line numbers it covers (`inputs/ukpga-2012-5.txt`), the provision, its one disposition, and either the L4 name that encodes it or the reason it is inert.
A row covers several paragraphs only when they share one disposition and one function.
A line that is a heading and has no row of its own gets an automatic row: `inert`, reason 1 (not operative, a heading).
The names in the last column are the exact names in the deposit files (checked by script against the files on 2026-11-04).
"Tests" names the test file; every `encoded` and `fork` row has at least one assertion in it.
Dispositions are the brief's four; there is no out-of-scope row and no deferred row.

The rows are written by `coverage.tsv` and `coverage-b.tsv` in my scratch folder and checked by `coverage.py check`, which asserts that every non-blank line of the three ranges falls in exactly one row.

```
non-blank lines in my ranges: 933; covered: 933; rows: 431 (332 written, 99 automatic heading rows)
rows by disposition: {'inert': 199, 'encoded': 220, 'fork': 7, 'repealed or blank in this text': 5}
non-blank lines by disposition: {'inert': 367, 'encoded': 542, 'fork': 19, 'repealed or blank in this text': 5}
inert rows by reason: {'1': 114, '2': 85}
problems: 0
```

The audit, in the terms the brief asks for:

- Text units counted: 933 non-blank lines in the three ranges (lines 2-517 = 516, 2630-2922 = 293, 3050-3173 = 124; the raw file has no blank line inside them), found by counting the file, not from the table.
- Rows in the table: 431 = 332 rows written by hand + 99 automatic heading rows.
- Rows before and after: I have no record of an earlier row count to quote; the table was written in two files and checked once by `coverage.py`, which reported 0 uncovered and 0 doubly-covered lines.
  On 2026-11-04 I changed the L4 names in the "why" column of several rows to the exact names in the files (I kept no count of them; no row was added, removed or re-dispositioned), so before and after that edit the row count is 431 both times.
  Also on 2026-11-04, a check that every line of an `encoded` or `fork` row falls inside some `@ref` range found 17 rows with uncited lines (the regulation-power subsections whose outcome is an input of another function, and three lead-in lines); I added a `@ref` block for each on the consuming function, and the check now finds none.
- Dispositions, by row: 220 `encoded`, 7 `fork`, 199 `inert` (114 reason 1, 85 reason 2, 0 reason 3), 5 `repealed or blank in this text`.
- Dispositions, by non-blank line: 542 `encoded`, 19 `fork`, 367 `inert`, 5 `repealed or blank in this text`.
- Reason 3 is 0 because the five lines the text shows as dots are `repealed or blank in this text` (their own disposition), not `inert`.
- FALSE and NOTHING audit (`audit.py`): 189 branches that answer `FALSE` or `NOTHING` in layer 1, 0 without a `-- FALSE-kind` or `-- NOTHING-kind` comment.

The five `repealed or blank in this text` rows: s 10(1A) (line 93), s 12(2)(a) (line 118), s 21(5) (line 242), s 39(2) (line 424) and the Schedule 2 paragraph at line 2697.
In each the text shows a line of dots (". . . .") where a provision stood; what it once said is not guessed.
Line 96 (s 10(4)) is not one of them: a word is replaced by dots and the sentence stands as printed, so it is `encoded`.


| lines | provision | disposition | why |
| --- | --- | --- | --- |
| 2 | Part 1 — Universal credit | inert | reason 1: not operative, a heading |
| 3 | CHAPTER 1 — Entitlement and awards | inert | reason 1: not operative, a heading |
| 4 | Introductory | inert | reason 1: not operative, a heading |
| 5 | 1 Universal credit | inert | reason 1: not operative, a heading |
| 6 | s 1(1) universal credit is payable in accordance with this Part | encoded | wra1-ch1-entitlement: `s 1(1) the benefit payable in accordance with this Part` |
| 7-9 | s 1(2)(a)-(b) to whom universal credit may be awarded (a single person; members of a couple jointly) | encoded | wra1-ch1-entitlement: `s 1(2)(a) the individual is a single person`; `s 1(2) universal credit may be awarded to these claimants` |
| 10-14 | s 1(3)(a)-(d) the four elements by reference to which an award is calculated | encoded | wra1-ch1-entitlement: `s 1(3) the elements by reference to which an award is calculated`; `s 1(3) the section that gives the element` |
| 15 | 2 Claims | inert | reason 1: not operative, a heading |
| 16-18 | s 2(1)(a)-(b) who may make a claim | encoded | wra1-ch1-entitlement: `s 2(1) a claim may be made by these claimants` |
| 19 | s 2(2) regulations may specify circumstances in which a member of a couple may claim as a single person | encoded | wra1-ch1-entitlement: `s 2(2) a member of a couple may make a claim as a single person` (the regulations' answer is an input) |
| 20 | Entitlement | inert | reason 1: not operative, a heading |
| 21 | 3 Entitlement | inert | reason 1: not operative, a heading |
| 22-24 | s 3(1)(a)-(b) a single claimant is entitled if the basic and financial conditions are met | encoded | wra1-ch1-entitlement: `s 3(1) the single claimant is entitled to universal credit` |
| 25-27 | s 3(2)(a)-(b) joint claimants are jointly entitled | encoded | wra1-ch1-entitlement: `s 3(2) joint claimants are jointly entitled to universal credit` |
| 28 | 4 Basic conditions | inert | reason 1: not operative, a heading |
| 29-30 | s 4(1)(a) at least 18 years old | encoded | wra1-ch1-entitlement: `s 4(1)(a) the person is at least 18 years old` |
| 31 | s 4(1)(b) has not reached the qualifying age for state pension credit | encoded | wra1-ch1-entitlement: `s 4(1)(b) the person has not reached the qualifying age for state pension credit` |
| 32 | s 4(1)(c) is in Great Britain | encoded | wra1-ch1-entitlement: `s 4(1)(c) the place is in Great Britain`; `s 4(1)(c) the person is in Great Britain` |
| 33 | s 4(1)(d) is not receiving education | encoded | wra1-ch1-entitlement: `s 4(1)(d) the person is not receiving education` |
| 34 | s 4(1)(e) has accepted a claimant commitment | encoded | wra1-ch1-entitlement: `s 4(1)(e) the person has accepted a claimant commitment` |
| 35 | s 4(2) regulations may provide for exceptions to the basic conditions | encoded | wra1-ch1-entitlement: input `regulations except the person from the basic condition they do not meet` of `s 4(1) the person meets the basic conditions` |
| 36 | s 4(3) regulations may specify a different minimum age for prescribed cases | encoded | wra1-ch1-entitlement: input `the different minimum age regulations prescribe for this case under section 4(3)` of `s 4(1)(a) the person is at least 18 years old` |
| 37 | s 4(4) the qualifying age for state pension credit is that in section 1(6) of the State Pension Credit Act 2002 | encoded | wra1-ch1-entitlement: input `the person has reached the qualifying age for state pension credit` of `s 4(1)(b) the person has not reached the qualifying age for state pension credit` (the Act pointed at is not among the sources, so the fact is asked) |
| 38-40 | s 4(5)(a)-(b) regulations may treat a person as being or not being in Great Britain, and disregard temporary absence | encoded | wra1-ch1-entitlement: inputs of `s 4(1)(c) the person is in Great Britain` |
| 41 | s 4(5)(c) regulations may modify the application of this Part for a person not in Great Britain who is entitled by virtue of (b) | inert | reason 2: machinery, a regulation-making power to modify the Part |
| 42-44 | s 4(6)(a)-(b) regulations may specify what "receiving education" means, and when a person is treated as receiving it | encoded | wra1-ch1-entitlement: inputs of `s 4(1)(d) the person is not receiving education` |
| 45 | s 4(7) regulations may specify circumstances in which a person is treated as having accepted or not accepted a claimant commitment | encoded | wra1-ch1-entitlement: input of `s 4(1)(e) the person has accepted a claimant commitment` |
| 46 | 5 Financial conditions | inert | reason 1: not operative, a heading |
| 47-49 | s 5(1)(a)-(b) financial conditions for a single claimant | encoded | wra1-ch1-entitlement: `s 5(1)(a) the claimant's capital is not greater than the prescribed amount`; `s 5(1)(b) the amount payable would not be less than the prescribed minimum`; `s 5(1) the financial conditions for a single claimant are met` |
| 50-52 | s 5(2)(a)-(b) financial conditions for joint claimants | encoded | wra1-ch1-entitlement: `s 5(2)(a) their combined capital is not greater than the prescribed amount`; `s 5(2)(b) the amount payable would not be less than the prescribed minimum`; `s 5(2) the financial conditions for joint claimants are met` |
| 53 | 6 Restrictions on entitlement | inert | reason 1: not operative, a heading |
| 54-57 | s 6(1)(a)-(c) entitlement does not arise (prescribed circumstances; a period shorter than a prescribed period; a prescribed period at the beginning) | encoded | wra1-ch1-entitlement: `s 6(1) entitlement to universal credit does not arise` |
| 58 | s 6(2) a period prescribed under (1)(b) or (c) may not exceed seven days | encoded | wra1-ch1-entitlement: `s 6(2) the prescribed period is within the seven-day limit` |
| 59 | s 6(3) regulations may provide for exceptions to s 6(1)(b) or (c) | encoded | wra1-ch1-entitlement: input `regulations provide an exception to subsection (1)(b) or (c)` of `s 6(1) entitlement to universal credit does not arise` |
| 60 | Awards | inert | reason 1: not operative, a heading |
| 61 | 7 Basis of awards | inert | reason 1: not operative, a heading |
| 62 | s 7(1) universal credit is payable for each complete assessment period within a period of entitlement | encoded | wra1-ch1-entitlement: `s 7(1) universal credit is payable in respect of the assessment period` |
| 63 | s 7(2) an assessment period is a period of a prescribed duration | encoded | wra1-ch1-entitlement: `s 7(2) the period is an assessment period` |
| 64-67 | s 7(3)(a)-(c) regulations may make provision about when an assessment period starts and about shorter periods | inert | reason 2: machinery, a regulation-making power (its outcome for a shorter period is NOTHING-kind in `s 7(1) universal credit is payable in respect of the assessment period`) |
| 68 | s 7(4) "period of entitlement" means a period during which entitlement subsists | encoded | wra1-ch1-entitlement: `s 7(4) the period is a period of entitlement` |
| 69 | 8 Calculation of awards | inert | reason 1: not operative, a heading |
| 70-72 | s 8(1)(a)-(b) the amount of an award is the balance of the maximum amount less the amounts to be deducted | fork | wra1-ch1-entitlement: `s 8(1) the amount of the award of universal credit for the period` (fork F-8, fork register in NOTES.md) |
| 73-77 | s 8(2)(a)-(d) the maximum amount is the total of the amounts under ss 9-12 | encoded | wra1-ch1-entitlement: `s 8(2) the maximum amount`; `s 8(2) the sum of two possibly unknown amounts` |
| 78-80 | s 8(3)(a)-(b) the amounts to be deducted (earned and unearned income) | encoded | wra1-ch1-entitlement: `s 8(3)(a) the amount deducted in respect of earned income`; `s 8(3)(b) the amount deducted in respect of unearned income` |
| 81-83 | s 8(4)(a)-(b) the income referred to (single claimant; combined income of joint claimants) | encoded | wra1-ch1-entitlement: `s 8(4) the income to which the deductions refer` |
| 84 | Elements of an award | inert | reason 1: not operative, a heading |
| 85 | 9 Standard allowance | inert | reason 1: not operative, a heading |
| 86-88 | s 9(1)(a)-(b) the calculation includes a standard allowance for a single claimant or for joint claimants | encoded | wra1-ch1-entitlement: `s 9(1) the calculation of the award includes the standard allowance` |
| 89 | s 9(2) regulations are to specify the amount of the standard allowance | inert | reason 2: machinery, a regulation-making duty (the amount is the input `the amount included under section 9 (standard allowance)` of `s 8(2) the maximum amount`) |
| 90 | s 9(3) regulations may provide for exceptions to s 9(1) | encoded | wra1-ch1-entitlement: input `regulations provide an exception to subsection (1) for these claimants` of `s 9(1) the calculation of the award includes the standard allowance` |
| 91 | 10 Responsibility for children and young persons | inert | reason 1: not operative, a heading |
| 92 | s 10(1) the calculation includes an amount for each child or qualifying young person for whom a claimant is responsible | encoded | wra1-ch1-entitlement: `s 10(1) the calculation of the award includes an amount for the person` |
| 93 | s 10(1A) a line of dots | repealed or blank in this text | the text shows only a line of dots (". . . ."); nothing is guessed about what it once said |
| 94 | s 10(2) regulations may provide an additional amount for a disabled child or qualifying young person | inert | reason 2: machinery, a regulation-making power (the amount is the input `the amount included under section 10 (responsibility for children and young persons)` of `s 8(2) the maximum amount`) |
| 95 | s 10(3) regulations are to specify, or provide for the calculation of, the amounts under (1) or (2) | inert | reason 2: machinery, a regulation-making duty |
| 96 | s 10(4) regulations may provide for exceptions to s 10(1) (a word replaced by dots; the sentence stands as printed) | encoded | wra1-ch1-entitlement: input `regulations provide an exception to subsection (1)` of `s 10(1) the calculation of the award includes an amount for the person` |
| 97 | s 10(5) "qualifying young person" means a person of a prescribed description | encoded | wra1-ch1-entitlement: `s 10(5) the person is a qualifying young person` |
| 98 | 11 Housing costs | inert | reason 1: not operative, a heading |
| 99 | s 11(1) the calculation includes an amount for liability to make payments for the accommodation occupied as a home | encoded | wra1-ch1-entitlement: `s 11(1) the calculation of the award includes an amount for housing costs` |
| 100-103 | s 11(2)(a)-(c) the accommodation must be in Great Britain and residential; it is immaterial whether whole or part of a building | encoded | wra1-ch1-entitlement: `s 11(2) the accommodation is accommodation that housing costs may be included for` |
| 104-105 | s 11(3)(a) regulations may make provision as to what is meant by payments in respect of accommodation (a word replaced by dots; the sentence stands as printed) | inert | reason 2: machinery, a regulation-making power about what is meant |
| 106-107 | s 11(3)(b)-(c) regulations may make provision as to when a claimant is treated as liable, and as occupying the accommodation as their home | encoded | wra1-ch1-entitlement: inputs `the claimant is liable to make payments in respect of the accommodation` and `the claimant occupies the accommodation as their home` of `s 11(1) the calculation of the award includes an amount for housing costs` |
| 108 | s 11(3)(d) regulations may provide for land used for the purposes of accommodation to be treated as included | inert | reason 2: machinery, a regulation-making power |
| 109 | s 11(4) regulations are to provide for the determination or calculation of any amount under s 11 | inert | reason 2: machinery, a regulation-making duty (the amount is the input `the amount included under section 11 (housing costs)` of `s 8(2) the maximum amount`) |
| 110-111 | s 11(5)(a) regulations may provide for exceptions to s 11(1) | encoded | wra1-ch1-entitlement: input `regulations provide an exception to subsection (1)` of `s 11(1) the calculation of the award includes an amount for housing costs` |
| 112-114 | s 11(5)(b)(i)-(ii) regulations may provide that an amount ends at, or does not start until, a prescribed time | inert | reason 2: machinery, a regulation-making power |
| 115 | 12 Other particular needs or circumstances | inert | reason 1: not operative, a heading |
| 116 | s 12(1) the calculation includes amounts for particular needs or circumstances as may be prescribed | encoded | wra1-ch1-entitlement: `s 12(1) the calculation of the award includes an amount for the need or circumstance` |
| 117 | s 12(2) the needs or circumstances prescribed may include | encoded | wra1-ch1-entitlement: `s 12(2) the needs or circumstances prescribed under subsection (1) may include` |
| 118 | s 12(2)(a) a line of dots | repealed or blank in this text | the text shows only a line of dots (". . . ."); nothing is guessed about what it once said |
| 119-120 | s 12(2)(b)-(c) limited capability for work and work-related activity; regular and substantial caring responsibilities for a severely disabled person | encoded | wra1-ch1-entitlement: `s 12(2) the needs or circumstances prescribed under subsection (1) may include` |
| 121 | s 12(3) regulations are to specify, or provide for the calculation of, any amount under s 12(1) | inert | reason 2: machinery, a regulation-making duty (the amount is the input `the amount included under section 12 (other particular needs or circumstances)` of `s 8(2) the maximum amount`) |
| 122-126 | s 12(4)(a)-(b) regulations may provide for an amount to end at or start at a prescribed time, and for the manner in which needs are determined | inert | reason 2: machinery, a regulation-making power |
| 127 | CHAPTER 2 — Claimant responsibilities | inert | reason 1: not operative, a heading |
| 128 | Introductory | inert | reason 1: not operative, a heading |
| 129 | 13 Work-related requirements: introductory | inert | reason 1: not operative, a heading |
| 130 | s 13(1) claimants must comply with the requirements the Secretary of State imposes | encoded | wra1-ch2-responsibilities: `s 13(1) the claimant must comply with the work-related requirement imposed` (regulative, run with #TRACE) and its twin `s 13(1) the claimant must comply with the work-related requirement`; tests: wra1-tests-ch2 |
| 131-135 | s 13(2)(a)-(d) the four work-related requirements | encoded | wra1-ch2-responsibilities: `s 13(2) the section that defines the work-related requirement` over the core type; tests: wra1-tests-ch2 |
| 136-140 | s 13(3)(a)-(d) the four groups of claimants | fork | fork F-groups (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 13(3) the section that describes the group` and `s 13(3) the group the claimant falls into`; tests: wra1-tests-ch2 |
| 141 | 14 Claimant commitment | inert | reason 1: not operative, a heading |
| 142 | s 14(1) claimant commitment | encoded | wra1-ch2-responsibilities: `s 14(1) the document is a claimant commitment`; tests: wra1-tests-ch2 |
| 143 | s 14(2) prepared by the Secretary of State, reviewed and updated | encoded | wra1-ch2-responsibilities: `s 14(2) this authority prepares, reviews and updates the claimant commitment`; tests: wra1-tests-ch2 |
| 144 | s 14(3) form the Secretary of State thinks fit | encoded | wra1-ch2-responsibilities: `s 14(3) the claimant commitment is in the form the Secretary of State thinks fit`; tests: wra1-tests-ch2 |
| 145-148 | s 14(4)(a)-(c) what a claimant commitment includes | encoded | wra1-ch2-responsibilities: `s 14(4) the claimant commitment is to include`; tests: wra1-tests-ch2 |
| 149 | s 14(5) when a claimant accepts a claimant commitment | encoded | wra1-ch2-responsibilities: `s 14(5) the claimant accepts the claimant commitment`; tests: wra1-tests-ch2 |
| 150 | Work-related requirements | inert | reason 1: not operative, a heading |
| 151 | 15 Work-focused interview requirement | inert | reason 1: not operative, a heading |
| 152 | s 15(1) work-focused interview requirement | encoded | wra1-ch2-responsibilities: `s 15(1) the requirement is a work-focused interview requirement`; tests: wra1-tests-ch2 |
| 153 | s 15(2) work-focused interview | encoded | wra1-ch2-responsibilities: `s 15(2) the interview is a work-focused interview`; tests: wra1-tests-ch2 |
| 154 | s 15(3) purposes which may be prescribed | encoded | wra1-ch2-responsibilities: `s 15(3) the purpose may be prescribed under subsection (2)`; tests: wra1-tests-ch2 |
| 155 | s 15(4) how, when and where | encoded | wra1-ch2-responsibilities: `s 15(4) the Secretary of State may specify this for a work-focused interview`; tests: wra1-tests-ch2 |
| 156 | 16 Work preparation requirement | inert | reason 1: not operative, a heading |
| 157 | s 16(1) work preparation requirement | encoded | wra1-ch2-responsibilities: `s 16(1) the requirement is a work preparation requirement`; tests: wra1-tests-ch2 |
| 158 | s 16(2) time to be devoted to an action | encoded | wra1-ch2-responsibilities: `s 16(2) the Secretary of State may specify the time to be devoted to the action`; tests: wra1-tests-ch2 |
| 159-166 | s 16(3)(a)-(g) action which may be specified | encoded | wra1-ch2-responsibilities: `s 16(3) the action may be specified under subsection (1)`; tests: wra1-tests-ch2 |
| 167 | s 16(4) work-focused health-related assessment for a person with limited capability for work | encoded | wra1-ch2-responsibilities: `s 16(4) the action may include taking part in a work-focused health-related assessment`; tests: wra1-tests-ch2 |
| 168-170 | s 16(5)(a)-(b) work-focused health-related assessment | encoded | wra1-ch2-responsibilities: `s 16(5) the assessment is a work-focused health-related assessment`; tests: wra1-tests-ch2 |
| 171-175 | s 16(6)(a)-(d) health care professional | encoded | wra1-ch2-responsibilities: `s 16(6) the person is a health care professional`; tests: wra1-tests-ch2 |
| 176 | 17 Work search requirement | inert | reason 1: not operative, a heading |
| 177-180 | s 17(1)(a)-(b) work search requirement | encoded | wra1-ch2-responsibilities: `s 17(1) the requirement is a work search requirement`; tests: wra1-tests-ch2 |
| 181 | s 17(2) time to be devoted to an action | encoded | wra1-ch2-responsibilities: `s 17(2) the Secretary of State may specify the time to be devoted to the action`; tests: wra1-tests-ch2 |
| 182-188 | s 17(3)(a)-(f) action which may be specified | encoded | wra1-ch2-responsibilities: `s 17(3) the action may be specified under subsection (1)(b)`; tests: wra1-tests-ch2 |
| 189 | s 17(4) limitations on a work search requirement | encoded | wra1-ch2-responsibilities: `s 17(4) a limitation may be imposed on a work search requirement by`; tests: wra1-tests-ch2 |
| 190-195 | s 17(5)(a)-(d) a limitation by reference to | encoded | wra1-ch2-responsibilities: `s 17(5) a limitation under subsection (4) may be`; tests: wra1-tests-ch2 |
| 196 | 18 Work availability requirement | inert | reason 1: not operative, a heading |
| 197 | s 18(1) work availability requirement | encoded | wra1-ch2-responsibilities: `s 18(1) the requirement is a work availability requirement`; tests: wra1-tests-ch2 |
| 198 | s 18(2) available for work | encoded | wra1-ch2-responsibilities: `s 18(2) the claimant is available for work`; tests: wra1-tests-ch2 |
| 199 | s 18(3) limitations on a work availability requirement | encoded | wra1-ch2-responsibilities: `s 18(3) a limitation may be imposed on a work availability requirement by`; tests: wra1-tests-ch2 |
| 200-205 | s 18(4)(a)-(d) a limitation by reference to | encoded | wra1-ch2-responsibilities: `s 18(4) a limitation under subsection (3) may be`; tests: wra1-tests-ch2 |
| 206 | s 18(5) regulations may define being able and willing immediately | encoded | wra1-ch2-responsibilities: the input `the claimant meets the definition regulations give of being able and willing immediately` of `s 18(2) the claimant is available for work`; tests: wra1-tests-ch2 |
| 207 | Application of work-related requirements | inert | reason 1: not operative, a heading |
| 208 | 19 Claimants subject to no work-related requirements | inert | reason 1: not operative, a heading |
| 209 | s 19(1) no work-related requirement on a claimant within s 19 | encoded | wra1-ch2-responsibilities: `s 19(1) the Secretary of State may impose a work-related requirement on the claimant` and the regulative twin `s 19(1) the Secretary of State shall not impose a work-related requirement` (#TRACE); tests: wra1-tests-ch2 |
| 210-214 | s 19(2)(a)-(d) claimants within s 19 | encoded | wra1-ch2-responsibilities: `s 19(2) the claimant falls within section 19`; tests: wra1-tests-ch2 |
| 215-218 | s 19(3)(a)-(c) regulations under (2)(d) may refer to hours, earnings, universal credit payable | inert | reason 2: machinery, a regulation-making power (the prescribed description of s 19(2)(d) enters as the input `the claimant is of a description regulations prescribe under subsection (2)(d)`) |
| 219-221 | s 19(4)(a)-(b) regulations under (3) may refer to the claimant alone or the couple, and may estimate | inert | reason 2: machinery, a regulation-making power |
| 222 | s 19(5) a requirement previously applying ceases | encoded | wra1-ch2-responsibilities: `s 19(5) a work-related requirement previously applying continues to have effect`; tests: wra1-tests-ch2 |
| 223-227 | s 19(6)(a)-(b) responsible carer | encoded | wra1-ch2-responsibilities: `s 19(6) the person is the responsible carer for the child`; tests: wra1-tests-ch2 |
| 228 | 20 Claimants subject to work-focused interview requirement only | inert | reason 1: not operative, a heading |
| 229-231 | s 20(1)(a)-(b) claimants within s 20 | fork | fork F-groups (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 20(1) the claimant falls within section 20`; tests: wra1-tests-ch2 |
| 232 | s 20(2) a work-focused interview requirement may be imposed | encoded | wra1-ch2-responsibilities: `s 20(2) the Secretary of State may impose this requirement on the claimant`; tests: wra1-tests-ch2 |
| 233 | s 20(3) no other requirement may be imposed; others cease | encoded | wra1-ch2-responsibilities: `s 20(2) the Secretary of State may impose this requirement on the claimant` (for the prohibition) and `s 20(3) a requirement previously applying continues to have effect`; tests: wra1-tests-ch2 |
| 234 | 21 Claimants subject to work preparation requirement | inert | reason 1: not operative, a heading |
| 235-238 | s 21(1)(a), (aa), (b) claimants within s 21 | encoded | wra1-ch2-responsibilities: `s 21(1) the claimant falls within section 21`; tests: wra1-tests-ch2 |
| 239-240 | s 21(2)-(3) a work preparation requirement and a work-focused interview requirement may be imposed | encoded | wra1-ch2-responsibilities: `s 21(2) the Secretary of State may impose this requirement on the claimant`; tests: wra1-tests-ch2 |
| 241 | s 21(4) no other requirement may be imposed; others cease | encoded | wra1-ch2-responsibilities: `s 21(2) the Secretary of State may impose this requirement on the claimant` (for the prohibition) and `s 21(4) a requirement previously applying continues to have effect`; tests: wra1-tests-ch2 |
| 242 | s 21(5) | repealed or blank in this text | repealed or blank: a line of dots in this text; what it once said is not guessed |
| 243 | 22 Claimants subject to all work-related requirements | inert | reason 1: not operative, a heading |
| 244 | s 22(1) claimants within s 22 | encoded | wra1-ch2-responsibilities: `s 22(1) the claimant falls within section 22`; tests: wra1-tests-ch2 |
| 245-247 | s 22(2)(a)-(b) the duty to impose a work search and a work availability requirement | encoded | wra1-ch2-responsibilities: `s 22(2) the Secretary of State must impose this requirement on the claimant` and the regulative twin `s 22(2) the Secretary of State must impose a work search requirement and a work availability requirement` (#TRACE); tests: wra1-tests-ch2 |
| 248-250 | s 22(3)(a)-(b) a work-focused interview and a work preparation requirement may be imposed | encoded | wra1-ch2-responsibilities: `s 22(3) the Secretary of State may impose this requirement on the claimant`; tests: wra1-tests-ch2 |
| 251 | Work-related requirements: supplementary | inert | reason 1: not operative, a heading |
| 252 | 23 Connected requirements | inert | reason 1: not operative, a heading |
| 253-256 | s 23(1)(a)-(c) interview for a purpose | encoded | wra1-ch2-responsibilities: `s 23(1) the Secretary of State may require the claimant to participate in an interview for this purpose`; tests: wra1-tests-ch2 |
| 257 | s 23(2) how, when and where | encoded | wra1-ch2-responsibilities: `s 23(2) the Secretary of State may specify this for an interview`; tests: wra1-tests-ch2 |
| 258-260 | s 23(3)(a)-(b) information, evidence, confirmation of compliance | encoded | wra1-ch2-responsibilities: `s 23(3) the Secretary of State may require the claimant to do this`; tests: wra1-tests-ch2 |
| 261-263 | s 23(4)(a)-(b) report specified changes | encoded | wra1-ch2-responsibilities: `s 23(4) the Secretary of State may require the claimant to report the change`; tests: wra1-tests-ch2 |
| 264 | 24 Imposition of requirements | inert | reason 1: not operative, a heading |
| 265-268 | s 24(1)(a)-(c) regulations may say when a requirement must or must not be imposed | inert | reason 2: machinery, a regulation-making power |
| 269 | s 24(2) must have regard to prescribed matters | encoded | wra1-ch2-responsibilities: `s 24(2) the Secretary of State must have regard to the matters regulations prescribe`; tests: wra1-tests-ch2 |
| 270 | s 24(3) may revoke or change | encoded | wra1-ch2-responsibilities: `s 24(3) the Secretary of State may revoke or change what has been imposed or specified`; tests: wra1-tests-ch2 |
| 271 | s 24(4) notification | encoded | wra1-ch2-responsibilities: `s 24(4) notification is in the manner the Secretary of State may determine`; tests: wra1-tests-ch2 |
| 272-274 | s 24(5)(a)-(b) domestic violence: 13 weeks | encoded | wra1-ch2-responsibilities: `s 24(5) the period of 13 weeks`, `s 24(5)(a) the requirement has ceased to have effect on the day`, `s 24(5)(b) the Secretary of State may impose another requirement on the day` and the regulative twin `s 24(5)(b) the Secretary of State shall not impose another requirement during the 13 weeks` (#TRACE); tests: wra1-tests-ch2 |
| 275-276 | s 24(6)(a) domestic violence has the meaning prescribed | encoded | wra1-ch2-responsibilities: the input `domestic violence, as regulations define it, is inflicted or threatened on or against the person` of `s 24(6)(b) the person is a victim of domestic violence`; tests: wra1-tests-ch2 |
| 277 | s 24(6)(b) victim of domestic violence | encoded | wra1-ch2-responsibilities: `s 24(6)(b) the person is a victim of domestic violence`; tests: wra1-tests-ch2 |
| 278 | s 24(6)(c) recently a victim | fork | fork F-24(6)(c) (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 24(6)(c) the person has recently been a victim of domestic violence`; tests: wra1-tests-ch2 |
| 279 | 25 Compliance with requirements | inert | reason 1: not operative, a heading |
| 280-282 | s 25(a)-(b) regulations may treat a claimant as having complied or taken an action | encoded | wra1-ch2-responsibilities: `s 25 the claimant is treated as having complied or taken the action`; tests: wra1-tests-ch2 |
| 283 | Reduction of benefit | inert | reason 1: not operative, a heading |
| 284 | 26 Higher-level sanctions | inert | reason 1: not operative, a heading |
| 285 | s 26(1) the award is reduced | encoded | wra1-ch2-responsibilities: `s 26(1) the amount of the award is to be reduced`; tests: wra1-tests-ch2 |
| 286-290 | s 26(2)(a)-(d) higher-level sanctionable failures | fork | fork F-26(2)(d) (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 26(2) the failure is sanctionable under section 26`; tests: wra1-tests-ch2 |
| 291 | s 26(3) ceasing work or losing pay after s 19(3) | fork | fork F-26(3) (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 26(3) the failure is sanctionable under section 26`; tests: wra1-tests-ch2 |
| 292-295 | s 26(4)(a)-(b) failures before the claim | encoded | wra1-ch2-responsibilities: `s 26(4) the earlier failure is sanctionable under section 26`; tests: wra1-tests-ch2 |
| 296-298 | s 26(5)(a)-(b) regulations may treat ceasing work as by misconduct or voluntary; may disregard small losses | encoded | wra1-ch2-responsibilities: the inputs `the ceasing or loss of pay was by reason of misconduct`, `the ceasing or loss of pay was voluntary` and `the loss of pay is below the prescribed level and regulations disregard it` of `s 26(2) the failure is sanctionable under section 26`; tests: wra1-tests-ch2 |
| 299-300 | s 26(6)(a) regulations are to provide for the amount of a reduction | inert | reason 2: machinery, a regulation-making duty (the amount is for regulations) |
| 301 | s 26(6)(b) a reduction lasts no more than three years | fork | fork F-26(6)(b) (fork register in NOTES.md); chosen reading in wra1-ch2-responsibilities: `s 26(6)(b) the period of the reduction does not exceed three years`; tests: wra1-tests-ch2 |
| 302-304 | s 26(7)(a)-(b) regulations may make the period depend on the number of failures and the gap between them | inert | reason 2: machinery, a regulation-making power |
| 305-308 | s 26(8)(a)-(c) regulations may provide for no reduction, carrying a reduction to a new award, ending or suspending a reduction | inert | reason 2: machinery, a regulation-making power |
| 309 | 27 Other sanctions | inert | reason 1: not operative, a heading |
| 310 | s 27(1) the award is reduced | encoded | wra1-ch2-responsibilities: `s 27(1) the amount of the award is to be reduced`; tests: wra1-tests-ch2 |
| 311-314 | s 27(2)(a)-(b), (3) other sanctionable failures, and not those that are higher-level | encoded | wra1-ch2-responsibilities: `s 27(2) the failure is sanctionable under section 27`; tests: wra1-tests-ch2 |
| 315-317 | s 27(4)(a)-(b) regulations are to provide for the amount and period of a reduction | inert | reason 2: machinery, a regulation-making duty |
| 318-319 | s 27(5) and (a) regulations may provide that a reduction lasts until a compliance condition is met | inert | reason 2: machinery, a regulation-making power (the compliance condition is defined by s 27(6), encoded) |
| 320-322 | s 27(5)(b) a fixed period not exceeding 26 weeks | encoded | wra1-ch2-responsibilities: `s 27(5)(b) the fixed period does not exceed 26 weeks`; tests: wra1-tests-ch2 |
| 323 | s 27(5)(c) a combination of both | inert | reason 2: machinery, a regulation-making power |
| 324-326 | s 27(6)(a)-(b) compliance condition | encoded | wra1-ch2-responsibilities: `s 27(6) the condition is a compliance condition`; tests: wra1-tests-ch2 |
| 327-329 | s 27(7)(a)-(b) a compliance condition may be revoked, varied, notified | encoded | wra1-ch2-responsibilities: `s 27(7) a compliance condition may be`; tests: wra1-tests-ch2 |
| 330-332 | s 27(8)(a)-(b) a fixed period may depend on | encoded | wra1-ch2-responsibilities: `s 27(8) a period fixed under subsection (5)(b) may depend on`; tests: wra1-tests-ch2 |
| 333-336 | s 27(9)(a)-(c) regulations may provide for no reduction, carrying a reduction to a new award, ending or suspending a reduction | inert | reason 2: machinery, a regulation-making power |
| 337 | 28 Hardship payments | inert | reason 1: not operative, a heading |
| 338-340 | s 28(1)(a)-(b) hardship payments | encoded | wra1-ch2-responsibilities: `s 28(1) a hardship payment may be made to the claimant`; tests: wra1-tests-ch2 |
| 341-346 | s 28(2)(a)-(e) regulations may make provision as to hardship, conditions, amount, period | inert | reason 2: machinery, a regulation-making power (whether the claimant is in hardship enters s 28(1) as the plain input `the claimant is or will be in hardship`) |
| 347 | s 28(2)(f) whether hardship payments are recoverable (seam 4) | encoded | wra1-ch2-responsibilities: `s 28(2)(f) the hardship payment is recoverable under section 28`; tests: wra1-tests-ch2 |
| 348 | Administration | inert | reason 1: not operative, a heading |
| 349 | 29 Delegation and contracting out | inert | reason 1: not operative, a heading |
| 350 | s 29(1) functions may be exercised by an authorised person | encoded | wra1-ch2-responsibilities: `s 29(1) this authority may exercise the Secretary of State's functions under sections 13 to 25`; tests: wra1-tests-ch2 |
| 351-354 | s 29(2)(a)-(c) an authorisation may be limited or conditional | inert | reason 2: machinery, the terms of a contracting-out authorisation between the Secretary of State and the contractor |
| 355-358 | s 29(3)(a)-(c) an authorisation may specify its duration, be varied or revoked | inert | reason 2: machinery, the terms of a contracting-out authorisation between the Secretary of State and the contractor |
| 359-362 | s 29(4)-(5) what an authorised person does is treated as done by the Secretary of State, except for the contract and criminal proceedings | encoded | wra1-ch2-responsibilities: `s 29(4) the act is treated as done by or in relation to the Secretary of State for this purpose`; tests: wra1-tests-ch2 |
| 363-366 | s 29(6)(a)-(b) an authorised person may treat the contract as repudiated on revocation | inert | reason 2: machinery, a right between the contractor and the Secretary of State; it gives the claimant no right and imposes no duty on the claimant |
| 367 | CHAPTER 3 — Supplementary and general | inert | reason 1: not operative, a heading |
| 368 | Supplementary and consequential | inert | reason 1: not operative, a heading |
| 369 | 30 Supplementary regulation-making powers | inert | reason 1: not operative, a heading |
| 370 | s 30 (Schedule 1 contains supplementary regulation-making powers) | inert | reason 1: not operative, a signpost to Schedule 1 that creates no rule |
| 371 | 31 Supplementary and consequential amendments | inert | reason 1: not operative, a heading |
| 372 | s 31 (Schedule 2 contains supplementary and consequential amendments) | inert | reason 1: not operative, a signpost to Schedule 2 that creates no rule |
| 373 | 32 Power to make supplementary and consequential provision etc | inert | reason 1: not operative, a heading |
| 374 | s 32(1) power to make supplementary, consequential, incidental or transitional provision | inert | reason 2: machinery, a regulation-making power |
| 375 | s 32(2) the appropriate authority is the Secretary of State | inert | reason 2: machinery, who makes the regulations |
| 376-378 | s 32(3)(a)-(b) the appropriate authority is the Welsh Ministers for Welsh provision | inert | reason 2: machinery, who makes the regulations |
| 379 | s 32(4) regulations may amend, repeal or revoke legislation | inert | reason 2: machinery, a regulation-making power (amendment of other legislation) |
| 380 | Universal credit and other benefits | inert | reason 1: not operative, a heading |
| 381 | 33 Abolition of benefits | inert | reason 1: not operative, a heading |
| 382-388 | s 33(1)(a)-(f) the benefits abolished | encoded | wra1-ch3-general: `s 33(1) the benefit is abolished`; tests: wra1-tests-ch3 |
| 389-390 | s 33(2)(a) "income-based jobseeker's allowance" has the same meaning as in the Jobseekers Act 1995 | encoded | wra1-ch3-general: `s 33(2)(a) the allowance is income-based jobseeker's allowance` |
| 391 | s 33(2)(b) "income-related employment and support allowance" | encoded | wra1-ch3-general: `s 33(2)(b) the allowance is income-related employment and support allowance` |
| 392 | s 33(3) Schedule 3 contains consequential amendments | inert | reason 1: not operative, a signpost to Schedule 3 that creates no rule |
| 393 | 34 Universal credit and state pension credit | inert | reason 1: not operative, a heading |
| 394 | s 34 (Schedule 4 provides for a housing element of state pension credit) | inert | reason 1: not operative, a signpost to Schedule 4 that creates no rule |
| 395 | 35 Universal credit and working-age benefits | inert | reason 1: not operative, a heading |
| 396 | s 35 (Schedule 5 makes further provision) | inert | reason 1: not operative, a signpost to Schedule 5 that creates no rule |
| 397 | 36 Migration to universal credit | inert | reason 1: not operative, a heading |
| 398 | s 36 (Schedule 6 contains provision about replacement of benefits) | inert | reason 1: not operative, a signpost to Schedule 6 that creates no rule |
| 399 | General | inert | reason 1: not operative, a heading |
| 400 | 37 Capability for work or work-related activity | inert | reason 1: not operative, a heading |
| 401-403 | s 37(1)(a)-(b) limited capability for work | encoded | wra1-ch3-general: `s 37(1) the claimant has limited capability for work on the Act's own test` |
| 404-406 | s 37(2)(a)-(b) limited capability for work-related activity | encoded | wra1-ch3-general: `s 37(2) the claimant has limited capability for work-related activity on the Act's own test` |
| 407 | s 37(3) the question is determined in accordance with regulations | encoded | wra1-ch3-general: `s 37(3) the claimant has limited capability as determined in accordance with regulations` |
| 408 | s 37(4) regulations must provide for determination on the basis of an assessment | inert | reason 2: machinery, a regulation-making duty |
| 409-411 | s 37(5)(a)-(b) regulations may require information, evidence, a medical examination | inert | reason 2: machinery, a regulation-making power |
| 412 | s 37(6) regulations may treat a claimant as having or not having limited capability | inert | reason 2: machinery, a regulation-making power |
| 413 | s 37(7) regulations may treat a claimant who fails to comply without good reason as not having it | inert | reason 2: machinery, a regulation-making power |
| 414-416 | s 37(8)(a)-(b) regulations may treat a claimant as having limited capability for work until determined | inert | reason 2: machinery, a regulation-making power |
| 417 | s 37(9) regulations may provide for determination even where treated as having it | inert | reason 2: machinery, a regulation-making power |
| 418 | 38 Information | inert | reason 1: not operative, a heading |
| 419 | s 38 information supplied under Chapter 2 or section 37 is information relating to social security | encoded | wra1-ch3-general: `s 38 the information is information relating to social security` |
| 420 | 39 Couples | inert | reason 1: not operative, a heading |
| 421-423 | s 39(1)(a)-(b) couple | encoded | wra1-ch3-general: `s 39(1) the two people are a couple` |
| 424 | s 39(2) a line of dots | repealed or blank in this text | the text shows only a line of dots (". . . ."); nothing is guessed about what it once said |
| 425-428 | s 39(3)(a)-(c) regulations may prescribe circumstances (marriage disregarded; treated as living together; household) | encoded | wra1-ch3-general: `s 39(3) the two people are a couple once the regulations supplied are applied` (the three regulations are inputs) |
| 429 | 40 Interpretation of Part 1 | inert | reason 1: not operative, a heading |
| 430-431 | s 40 "assessment period" has the meaning given by section 7(2) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 7(2)); the meaning itself is `s 7(2) the period is an assessment period` |
| 432 | s 40 "child" means a person under the age of 16 | encoded | wra1-ch3-general: `s 40 the person is a child` |
| 433 | s 40 "claim" means claim for universal credit | encoded | wra1-ch3-general: `s 40 the claim is a claim in this Part` |
| 434 | s 40 "claimant" means a single claimant or each of joint claimants | encoded | wra1-ch3-general: `s 40 the claimants` |
| 435 | s 40 "couple" has the meaning given by section 39 | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 39); the meaning is `s 39(1) the two people are a couple` |
| 436 | s 40 "disabled" has such meaning as may be prescribed | encoded | wra1-ch3-general: `s 40 the person or matter has the prescribed meaning of the term` (NOTHING-kind: points outside the text) |
| 437 | s 40 "joint claimants" | encoded | wra1-ch3-general: `s 40 the two people are joint claimants` |
| 438 | s 40 "limited capability for work" and "limited capability for work-related activity" are construed in accordance with section 37(1) and (2) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 37(1) and (2)); the meaning is `s 37(1) the claimant has limited capability for work on the Act's own test` and `s 37(2) the claimant has limited capability for work-related activity on the Act's own test` |
| 439 | s 40 "prescribed" means specified or provided for in regulations | encoded | wra1-ch3-general: `s 40 the matter is prescribed` |
| 440 | s 40 "primary legislation" | encoded | wra1-ch3-general: `s 40 the legislation is primary legislation` |
| 441 | s 40 "qualifying young person" has the meaning given in section 10(5) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 10(5)); the meaning is `s 10(5) the person is a qualifying young person` |
| 442 | s 40 "regular and substantial caring responsibilities" has such meaning as may be prescribed | encoded | wra1-ch3-general: `s 40 the person or matter has the prescribed meaning of the term` (NOTHING-kind: points outside the text) |
| 443 | s 40 "responsible carer" has the meaning given in section 19(6) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 19(6)); the meaning is `s 19(6) the person is the responsible carer for the child` |
| 444 | s 40 "secondary legislation" | encoded | wra1-ch3-general: `s 40 the instrument is secondary legislation` |
| 445 | s 40 "severely disabled" has such meaning as may be prescribed | encoded | wra1-ch3-general: `s 40 the person or matter has the prescribed meaning of the term` (NOTHING-kind: points outside the text) |
| 446 | s 40 "single claimant" | encoded | wra1-ch3-general: `s 40 the person is a single claimant` |
| 447 | s 40 "single person" is construed in accordance with section 1(2)(a) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 1(2)(a)); the meaning is `s 1(2)(a) the individual is a single person` |
| 448 | s 40 "work" has such meaning as may be prescribed | encoded | wra1-ch3-general: `s 40 the person or matter has the prescribed meaning of the term` (NOTHING-kind: points outside the text) |
| 449 | s 40 "work availability requirement" has the meaning given by section 18(1) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 18(1)); the meaning is `s 18(1) the requirement is a work availability requirement` |
| 450 | s 40 "work preparation requirement" has the meaning given by section 16(1) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 16(1)); the meaning is `s 16(1) the requirement is a work preparation requirement` |
| 451 | s 40 "work search requirement" has the meaning given by section 17(1) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 17(1)); the meaning is `s 17(1) the requirement is a work search requirement` |
| 452 | s 40 "work-focused interview requirement" has the meaning given by section 15(1) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 15(1)); the meaning is `s 15(1) the requirement is a work-focused interview requirement` |
| 453 | s 40 "work-related activity" | encoded | wra1-ch3-general: `s 40 the activity is work-related activity` |
| 454 | s 40 "work-related requirement" has the meaning given by section 13(2) | encoded | wra1-ch3-general: `s 40 where the meaning is given` (points at section 13(2)); the meaning is `s 13(2) the section that defines the work-related requirement` |
| 455 | Regulations | inert | reason 1: not operative, a heading |
| 456 | 41 Pilot schemes | inert | reason 1: not operative, a heading |
| 457-461 | s 41(1)(a)-(c) powers may be exercised for piloting purposes | inert | reason 2: machinery, a regulation-making power |
| 462-467 | s 41(2)(a)-(c) "piloting purposes" | inert | reason 2: machinery, defines the purposes for which a regulation-making power is exercised |
| 468 | s 41(3) "pilot scheme" | inert | reason 2: machinery, a label for regulations made by virtue of the section |
| 469-474 | s 41(4)(a)-(c) a pilot scheme may be limited to areas, classes or selected persons | inert | reason 2: machinery, a regulation-making power |
| 475 | s 41(5) a pilot scheme may not have effect for a period exceeding three years | encoded | wra1-ch3-general: `s 41(5) the pilot scheme's own period is within three years` |
| 476 | s 41(5)(a) the Secretary of State may by order continue a pilot scheme for not more than twelve months | encoded | wra1-ch3-general: `s 41(5)(a) the order's continuation is within twelve months` |
| 477 | s 41(5)(b) a pilot scheme may be replaced by a further pilot scheme | inert | reason 2: machinery, a regulation-making power |
| 478 | s 41(6) a pilot scheme may include consequential or transitional provision on expiry | inert | reason 2: machinery, a regulation-making power |
| 479 | 42 Regulations: general | inert | reason 1: not operative, a heading |
| 480 | s 42(1) regulations are made by the Secretary of State unless otherwise provided | inert | reason 2: machinery, who makes regulations |
| 481-483 | s 42(2)(a)-(b) powers may make different provision for different cases | inert | reason 2: machinery, how regulation-making powers are exercised |
| 484-486 | s 42(3)(a)-(b) powers include incidental provision and discretion | inert | reason 2: machinery, how regulation-making powers are exercised |
| 487 | s 42(4) each power is without prejudice to the others | inert | reason 2: machinery, how regulation-making powers are exercised |
| 488 | s 42(5) where regulations provide for an amount, the amount may be zero | inert | reason 2: machinery, how regulation-making powers are exercised (the seat layer accepts 0 as an amount) |
| 489-491 | s 42(6)(a)-(b) amounts may differ by description of person (single or couple, age) | inert | reason 2: machinery, how regulation-making powers are exercised |
| 492 | s 42(7) regulations under section 11(4) or 12(3) may make different provision for different areas | inert | reason 2: machinery, how regulation-making powers are exercised |
| 493 | 43 Regulations: procedure | inert | reason 1: not operative, a heading |
| 494 | s 43(1) regulations are made by statutory instrument | inert | reason 2: machinery, parliamentary procedure for regulations |
| 495 | s 43(2) negative resolution procedure | inert | reason 2: machinery, parliamentary procedure for regulations |
| 496-509 | s 43(3)(a)-(m) first regulations are subject to the affirmative resolution procedure | inert | reason 2: machinery, parliamentary procedure for regulations |
| 510 | s 43(4) pilot-scheme regulations: affirmative procedure | inert | reason 2: machinery, parliamentary procedure for regulations |
| 511-513 | s 43(5)(a)-(b) combined instruments: affirmative procedure | inert | reason 2: machinery, parliamentary procedure for regulations |
| 514-516 | s 43(6)(a)-(b) meaning of negative and affirmative resolution procedure | inert | reason 2: machinery, parliamentary procedure for regulations |
| 517 | s 43(7) Welsh Ministers' regulations under section 32: draft approved by the National Assembly for Wales | inert | reason 2: machinery, parliamentary procedure for regulations |
| 2630 | SCHEDULE 1 — Universal credit: supplementary regulation-making powers | inert | reason 1: not operative, a heading |
| 2631 | Entitlement of joint claimants | inert | reason 1: not operative, a heading |
| 2632 | sch 1 para 1 joint claimants without each meeting the basic conditions | encoded | wra1-sch1: `sch 1 para 1 joint claimants may be entitled without each meeting all the basic conditions`; tests: wra1-tests-sch1 |
| 2633 | Linking periods | inert | reason 1: not operative, a heading |
| 2634 | sch 1 para 2 linking periods | encoded | wra1-sch1: `sch 1 para 2 the two periods are treated as a single period`; tests: wra1-tests-sch1 |
| 2635 | Couples | inert | reason 1: not operative, a heading |
| 2636-2644 | sch 1 para 3(1)-(2) couples: claims treated as made by one member or both; awards on ceasing to be, or becoming, a couple | inert | reason 2: machinery, a regulation-making power about how a claim or award is treated |
| 2645 | Calculation of capital and income | inert | reason 1: not operative, a heading |
| 2646-2657 | sch 1 para 4(1)-(4) regulations for the calculation of capital and income | inert | reason 2: machinery, a regulation-making power (capital and income enter ss 5 and 8 as plain numbers) |
| 2658-2659 | sch 1 para 4(5)-(6) joint claimants' capital and income | encoded | wra1-sch1: `sch 1 para 4(5) the joint capital and income includes this person's separate capital and income`; tests: wra1-tests-sch1 |
| 2660 | Responsibility for children etc | inert | reason 1: not operative, a heading |
| 2661 | sch 1 para 5(1) responsibility for a child | encoded | wra1-sch1: `sch 1 para 5(1) the person is responsible for the child or qualifying young person`; tests: wra1-tests-sch1 |
| 2662 | sch 1 para 5(2) nominations of the responsible carer | encoded | wra1-sch1: `sch 1 para 5(2) the couple has jointly nominated the person as the responsible carer`; tests: wra1-tests-sch1 |
| 2663 | Vouchers | inert | reason 1: not operative, a heading |
| 2664-2665 | sch 1 para 6(1)-(2) vouchers | encoded | wra1-sch1: `sch 1 para 6(2) liability to pay all or part of the award may be discharged by a voucher`; tests: wra1-tests-sch1 |
| 2666 | sch 1 para 6(3) a voucher may not exceed the costs | encoded | wra1-sch1: `sch 1 para 6(3) the amount paid by means of the voucher is permitted`; tests: wra1-tests-sch1 |
| 2667 | sch 1 para 6(4) what a voucher is | encoded | wra1-sch1: `sch 1 para 6(4) the means is a voucher`; tests: wra1-tests-sch1 |
| 2668-2670 | sch 1 para 6(5)(a)-(b) a voucher may be limited | encoded | wra1-sch1: `sch 1 para 6(5) a voucher may be`; tests: wra1-tests-sch1 |
| 2671 | Work-related requirements | inert | reason 1: not operative, a heading |
| 2672-2675 | sch 1 para 7 EU right to reside: treated as not within s 19, 20 or 21 | encoded | wra1-sch1: `sch 1 para 7 the claimant is treated as not falling within section 19, 20 or 21` and `sch 1 para 7 the claimant falls within the section once regulations are applied`; tests: wra1-tests-sch1 |
| 2676 | Good reason | inert | reason 1: not operative, a heading |
| 2677-2678 | sch 1 para 8(a) good reason: treated as having or not having | encoded | wra1-sch1: `sch 1 para 8(a) the person is treated as having a good reason for the act or omission`; tests: wra1-tests-sch1 |
| 2679 | sch 1 para 8(b) matters to be taken into account in deciding good reason | inert | reason 2: machinery, a regulation-making power |
| 2680 | SCHEDULE 2 — Universal credit: amendments | inert | reason 1: not operative, a heading |
| 2681 | Children Act 1989 (c. 41) | inert | reason 1: not operative, a heading |
| 2682-2686 | sch 2 Children Act 1989 ss 17(9), 17A(5)(b), 29(3) and (3A), Sch 2 para 21(4): after "in receipt" insert "of universal credit (except in such circumstances as may be prescribed)" | encoded | wra1-sch2: constructor `sch 2 CA1989 s 17(9)`, `sch 2 CA1989 s 17A(5)(b)`, `sch 2 CA1989 s 29(3) and (3A)`, `sch 2 CA1989 Sch 2 para 21(4)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2687 | Child Support Act 1991 (c. 48) | inert | reason 1: not operative, a heading |
| 2688 | sch 2 Child Support Act 1991 Sch 1 para 5(4) | encoded | wra1-sch2: constructor `sch 2 CSA1991 Sch 1 para 5(4)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2689 | Social Security Administration Act 1992 (c. 5) | inert | reason 1: not operative, a heading |
| 2690 | sch 2 SSAA 1992 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2691-2692 | sch 2 SSAA s 1(4)(za) | encoded | wra1-sch2: constructor `sch 2 SSAA s 1(4)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2693-2696 | sch 2 SSAA s 5(2)(za) and s 5(6) | encoded | wra1-sch2: constructor `sch 2 SSAA s 5(2)(za)` and `sch 2 SSAA s 5(6)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2697 | sch 2 SSAA 1992 (a repealed paragraph) | repealed or blank in this text | repealed or blank: a line of dots in this text; what it once said is not guessed |
| 2698 | sch 2 SSAA s 74(2)(b) | encoded | wra1-sch2: constructor `sch 2 SSAA s 74(2)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2699 | sch 2 SSAA s 74A(7) | encoded | wra1-sch2: constructor `sch 2 SSAA s 74A(7)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2700 | sch 2 SSAA s 78(6)(d) | encoded | wra1-sch2: constructor `sch 2 SSAA s 78(6)(d)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2701 | sch 2 SSAA s 105(1)(b) | encoded | wra1-sch2: constructor `sch 2 SSAA s 105(1)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2702 | sch 2 SSAA s 106(1) to (4) | encoded | wra1-sch2: constructor `sch 2 SSAA s 106(1) to (4)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2703 | sch 2 SSAA s 108(1)(a) | encoded | wra1-sch2: constructor `sch 2 SSAA s 108(1)(a)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2704 | sch 2 SSAA s 109(1) | encoded | wra1-sch2: constructor `sch 2 SSAA s 109(1)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2705-2706 | sch 2 SSAA s 121DA(1)(hj) this Act added to the Acts of Part 6 (supply of information) | inert | reason 2: machinery, adds this Act to a list of Acts used by officials for information-sharing |
| 2707 | sch 2 SSAA s 122B(3)(b) supply of other government information | inert | reason 2: machinery, adds this Act to a list of Acts used by officials for information-sharing |
| 2708-2714 | sch 2 SSAA s 122F supply by rent officers of benefit information | inert | reason 2: machinery, a duty between rent officers and the department |
| 2715-2718 | sch 2 SSAA s 124(1) age, death and marriage: (ac) final "and" repealed, (ad) added | inert | reason 2: machinery, adds this Act to a list of Acts for regulations about proof of age, death and marriage |
| 2719 | sch 2 SSAA s 125 regulations as to notification of death | inert | reason 2: machinery, adds this Act to a list of Acts for regulations about notification of death |
| 2720 | sch 2 SSAA s 126(1) | encoded | wra1-sch2: constructor `sch 2 SSAA s 126(1)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2721-2722 | sch 2 SSAA s 130(1)(za) | encoded | wra1-sch2: constructor `sch 2 SSAA s 130(1)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2723-2724 | sch 2 SSAA s 132(1)(za) | encoded | wra1-sch2: constructor `sch 2 SSAA s 132(1)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2725-2727 | sch 2 SSAA s 150(1)(n) | encoded | wra1-sch2: constructor `sch 2 SSAA s 150(1)(n)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2728 | sch 2 SSAA s 150(7) after 2007 insert Part 1 of this Act | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2729-2730 | sch 2 SSAA 159D inserted: the lead-in and the heading of the inserted section | inert | reason 1: not operative, words that insert a section and its heading |
| 2731-2741 | sch 2 SSAA 159D(1)-(2) an alteration affecting universal credit: the amount payable changes without a further decision | encoded | wra1-sch2: `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision`; tests: wra1-tests-sch2 |
| 2742 | sch 2 SSAA 159D(3) the same amount: the award continues | encoded | wra1-sch2: `sch 2 SSAA 159D(3) the award continues in force`; tests: wra1-tests-sch2 |
| 2743-2748 | sch 2 SSAA 159D(4)-(5) a statement in the House of Commons; an award made before the proposed commencing date | inert | reason 2: machinery, how the Secretary of State may frame an award after a statement in the House of Commons; a power, not a duty, and it gives the claimant no right |
| 2749-2754 | sch 2 SSAA 159D(6) "alteration" | encoded | wra1-sch2: the input `an alteration affects the computation of the amount of universal credit to which the recipient is entitled` of `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision`; tests: wra1-tests-sch2 |
| 2755 | sch 2 SSAA 159D(6) "benefit income" | encoded | wra1-sch2: `sch 2 SSAA 159D(6) the income is benefit income`; tests: wra1-tests-sch2 |
| 2756 | sch 2 SSAA 159D(6) "the commencing date" | encoded | wra1-sch2: the input `the commencing date` of `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision`; tests: wra1-tests-sch2 |
| 2757-2759 | sch 2 SSAA 159D(6) "component" | encoded | wra1-sch2: the input `an alteration affects the computation of the amount of universal credit to which the recipient is entitled` of `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision` (a component of a contribution-based jobseeker's allowance or a contributory employment and support allowance); tests: wra1-tests-sch2 |
| 2760 | sch 2 SSAA 159D(6) "element" | encoded | wra1-sch2: `sch 2 SSAA 159D(6) the amount is an element of universal credit`; tests: wra1-tests-sch2 |
| 2761-2762 | sch 2 SSAA 160C inserted: the lead-in and the heading of the inserted section | inert | reason 1: not operative, words that insert a section and its heading |
| 2763-2772 | sch 2 SSAA 160C(1)-(4) increases due to attainment of a particular age | encoded | wra1-sch2: `sch 2 SSAA 160C(2) the increased amount is payable from the day without any further decision`; tests: wra1-tests-sch2 |
| 2773 | sch 2 SSAA 160C(5) "element" | encoded | wra1-sch2: `sch 2 SSAA 159D(6) the amount is an element of universal credit` (the same definition); tests: wra1-tests-sch2 |
| 2774-2776 | sch 2 SSAA s 165 adjustments between the National Insurance Fund and the Consolidated Fund | inert | reason 2: machinery, finance between funds |
| 2777-2785 | sch 2 SSAA s 170 Social Security Advisory Committee: the relevant enactments | inert | reason 2: machinery, adds this Act to the Committee's list of enactments |
| 2786-2791 | sch 2 SSAA s 179 reciprocal agreements | inert | reason 2: machinery, reciprocal agreements with other countries |
| 2792 | sch 2 SSAA s 180 payment of travelling expenses | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2793 | sch 2 SSAA s 182B information about postal redirection | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2794-2795 | sch 2 SSAA s 187(1)(za) | encoded | wra1-sch2: constructor `sch 2 SSAA s 187(1)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2796 | sch 2 SSAA s 191 definition of benefit | encoded | wra1-sch2: constructor `sch 2 SSAA s 191 definition of benefit` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2797 | Local Government Finance Act 1992 (c. 14) | inert | reason 1: not operative, a heading |
| 2798 | sch 2 Local Government Finance Act 1992 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2799-2802 | sch 2 LGFA Sch 4 para 6(1) and (2)(b) | encoded | wra1-sch2: constructor `sch 2 LGFA Sch 4 para 6(1)` and `sch 2 LGFA Sch 4 para 6(2)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2803-2806 | sch 2 LGFA Sch 4 para 12(1)(aa) and (d) | encoded | wra1-sch2: constructor `sch 2 LGFA Sch 4 para 12(1)(aa)` and `sch 2 LGFA Sch 4 para 12(1)(d)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2807-2809 | sch 2 LGFA Sch 8 para 6(1) and (2)(b) | encoded | wra1-sch2: constructor `sch 2 LGFA Sch 8 para 6(1)` and `sch 2 LGFA Sch 8 para 6(2)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2810 | Jobseekers Act 1995 (c. 18) | inert | reason 1: not operative, a heading |
| 2811-2812 | sch 2 JSA s 2(3C) definition of benefit | encoded | wra1-sch2: constructor `sch 2 JSA s 2(3C) definition of benefit` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2813 | Housing Act 1996 (c. 52) | inert | reason 1: not operative, a heading |
| 2814 | sch 2 Housing Act 1996 s 122 rent officers: "universal credit," added to the heading and subsection (1) | inert | reason 2: machinery, a function of rent officers towards the department |
| 2815 | Education Act 1996 (c. 56) | inert | reason 1: not operative, a heading |
| 2816 | sch 2 Education Act 1996 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2817-2818 | sch 2 EA1996 s 457(4)(b) | encoded | wra1-sch2: constructor `sch 2 EA1996 s 457(4)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2819-2821 | sch 2 EA1996 s 512ZB(4)(a) | encoded | wra1-sch2: constructor `sch 2 EA1996 s 512ZB(4)(a)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2822-2823 | sch 2 EA1996 s 512ZB(4)(b) | encoded | wra1-sch2: constructor `sch 2 EA1996 s 512ZB(4)(b)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2824 | Social Security (Recovery of Benefits) Act 1997 (c. 27) | inert | reason 1: not operative, a heading |
| 2825 | sch 2 Social Security (Recovery of Benefits) Act 1997 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2826 | sch 2 SSRBA1997 s 29 definition of benefit | encoded | wra1-sch2: constructor `sch 2 SSRBA1997 s 29 definition of benefit` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2827 | sch 2 SSRBA1997 Sch 2 table | encoded | wra1-sch2: constructor `sch 2 SSRBA1997 Sch 2 table` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2828 | Social Security Act 1998 (c. 14) | inert | reason 1: not operative, a heading |
| 2829 | sch 2 Social Security Act 1998 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2830-2833 | sch 2 SSA1998 s 2(2) use of computers: (i) final "or" repealed, (k) added | inert | reason 2: machinery, adds this Act to a list of Acts for which decisions may be made by computer |
| 2834-2836 | sch 2 SSA1998 s 8(3)(aa) | encoded | wra1-sch2: constructor `sch 2 SSA1998 s 8(3)(aa)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2837 | sch 2 SSA1998 s 8(4) adds Part 1 of this Act to a list of Acts | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2838 | sch 2 SSA1998 s 11(3) regulations with respect to decisions | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2839-2840 | sch 2 SSA1998 s 27(7)(f) | encoded | wra1-sch2: constructor `sch 2 SSA1998 s 27(7)(f)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2841-2844 | sch 2 SSA1998 s 28(3) correction of errors: (f) final "or" repealed, (h) added | inert | reason 2: machinery, adds this Act to a list of Acts |
| 2845-2846 | sch 2 SSA1998 s 39(1) "claimant" for a couple jointly claiming | encoded | wra1-sch2: `sch 2 SSA1998 39(1) this is the claimant in relation to the couple`; tests: wra1-tests-sch2 |
| 2847-2853 | sch 2 SSA1998 Sch 2 decisions against which no appeal lies: paras 6(b)(v), and a new paragraph after 7 | encoded | wra1-sch2: `sch 2 SSA1998 an appeal lies against the decision`; tests: wra1-tests-sch2 |
| 2854-2855 | sch 2 SSA1998 Sch 3 decisions against which an appeal lies: a new paragraph after 3 | encoded | wra1-sch2: `sch 2 SSA1998 an appeal lies against the decision`; tests: wra1-tests-sch2 |
| 2856 | Immigration and Asylum Act 1999 (c. 33) | inert | reason 1: not operative, a heading |
| 2857 | sch 2 Immigration and Asylum Act 1999 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2858-2861 | sch 2 IAA1999 s 97(5)(za) | encoded | wra1-sch2: constructor `sch 2 IAA1999 s 97(5)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2862 | sch 2 IAA1999 s 115(1) | encoded | wra1-sch2: constructor `sch 2 IAA1999 s 115(1)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2863 | Child Support, Pensions and Social Security Act 2000 (c. 19) | inert | reason 1: not operative, a heading |
| 2864 | sch 2 CSPSSA2000 s 69(1)(a) | encoded | wra1-sch2: constructor `sch 2 CSPSSA2000 s 69(1)(a)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2865 | Social Security Fraud Act 2001 (c. 11) | inert | reason 1: not operative, a heading |
| 2866 | sch 2 Social Security Fraud Act 2001 is amended as follows | inert | reason 1: not operative, an introductory line that creates no rule |
| 2867-2868 | sch 2 SSFA s 6A(1) disqualifying benefit: (za) universal credit (seam 7) | encoded | wra1-sch2: `sch 2 SSFA 6A(1)(za) the benefit is a disqualifying benefit`; tests: wra1-tests-sch2 |
| 2869-2870 | sch 2 SSFA s 6B(1)-(2) amended; (5) "(6)" becomes "(5A)" | inert | reason 2: machinery, a cross-reference changed |
| 2871-2876 | sch 2 SSFA s 6B(5A) regulations for universal credit as the sanctionable benefit | encoded | wra1-sch2: `sch 2 SSFA 6B(5A) regulations may provide that universal credit is payable as if this applied`; tests: wra1-tests-sch2 |
| 2877-2878 | sch 2 SSFA s 6B(7)(d) an amount of the allowance recoverable | inert | reason 2: machinery, a power to make regulations about a jobseeker's allowance, the same form as (5A)(d); the option for universal credit is encoded at 6B(5A)(d) |
| 2879-2880 | sch 2 SSFA s 7(1)-(2) amended; (2) "(3)" becomes "(2A)" | inert | reason 2: machinery, a cross-reference changed |
| 2881-2886 | sch 2 SSFA s 7(2A) regulations for universal credit as the sanctionable benefit | encoded | wra1-sch2: `sch 2 SSFA 7(2A) regulations may provide that universal credit is payable as if this applied`; tests: wra1-tests-sch2 |
| 2887-2888 | sch 2 SSFA s 7(4)(d) an amount of the allowance recoverable | inert | reason 2: machinery, a power to make regulations about a jobseeker's allowance, the same form as (2A)(d); the option for universal credit is encoded at 7(2A)(d) |
| 2889-2896 | sch 2 SSFA s 8 joint-claim jobseeker's allowance: (3)(aa), (4)(d), words repealed | inert | reason 2: machinery, a power to make regulations about a joint-claim jobseeker's allowance, not universal credit |
| 2897-2899 | sch 2 SSFA s 9(1)(za) | encoded | wra1-sch2: constructor `sch 2 SSFA s 9(1)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2900 | sch 2 SSFA s 9(2) "or" becomes "and" | inert | reason 2: machinery, a conjunction changed |
| 2901-2906 | sch 2 SSFA s 9(2A) regulations for the family member's universal credit | encoded | wra1-sch2: `sch 2 SSFA 9(2A) regulations may provide that the family member's universal credit is payable as if this applied`; tests: wra1-tests-sch2 |
| 2907-2908 | sch 2 SSFA s 9(4)(d) an amount of the allowance recoverable | inert | reason 2: machinery, a power to make regulations about a jobseeker's allowance, the same form as (2A)(d); the option for universal credit is encoded at 9(2A)(d) |
| 2909-2910 | sch 2 SSFA s 10(3)(bd) | encoded | wra1-sch2: constructor `sch 2 SSFA s 10(3)(bd)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 2911-2916 | sch 2 SSFA s 11(3) loss of benefit regulations: cross-references to 6B(5A), 7(2A), 9(2A) and "or (aa)" | inert | reason 2: machinery, cross-references changed |
| 2917 | State Pension Credit Act 2002 (c. 16) | inert | reason 1: not operative, a heading |
| 2918-2919 | sch 2 SPCA s 4(1A) a claimant is not entitled to state pension credit if a member of a couple whose other member is below the qualifying age | encoded | wra1-sch2: `sch 2 SPCA 4(1A) the claimant is entitled to state pension credit`; tests: wra1-tests-sch2 |
| 2920 | Welfare Reform Act 2007 (c. 5) | inert | reason 1: not operative, a heading |
| 2921-2922 | sch 2 WRA2007 Sch 1 para 1(5)(za) | encoded | wra1-sch2: constructor `sch 2 WRA2007 Sch 1 para 1(5)(za)` of `sch 2 host provision`, answered by `sch 2 the host provision now includes universal credit`; tests: wra1-tests-sch2 |
| 3050 | SCHEDULE 5 — Universal credit and other working-age benefits | inert | reason 1: not operative, a heading |
| 3051 | General | inert | reason 1: not operative, a heading |
| 3052-3054 | sch 5 para 1(1)(a)-(b) relevant benefit | encoded | wra1-sch5-6: `sch 5 para 1(1) the benefit is a relevant benefit`; tests: wra1-tests-sch5-6 |
| 3055-3058 | sch 5 para 1(2)(a)-(c) work-related requirement | encoded | wra1-sch5-6: `sch 5 para 1(2) the requirement is a work-related requirement`; tests: wra1-tests-sch5-6 |
| 3059-3062 | sch 5 para 1(3)(a)-(c) sanction | encoded | wra1-sch5-6: `sch 5 para 1(3) the reduction is a sanction`; tests: wra1-tests-sch5-6 |
| 3063 | Dual entitlement | inert | reason 1: not operative, a heading |
| 3064-3065 | sch 5 para 2(1)-(2) the amount of the relevant benefit payable to a person entitled to both | encoded | wra1-sch5-6: `sch 5 para 2(1) the amount payable by way of the relevant benefit`; tests: wra1-tests-sch5-6 |
| 3066-3074 | sch 5 para 2(3)-(5) requirements and sanctions for a person entitled to both | encoded | wra1-sch5-6: `sch 5 para 2 and 3 regulations may make this provision`; tests: wra1-tests-sch5-6 |
| 3075 | Movement between working-age benefits | inert | reason 1: not operative, a heading |
| 3076-3079 | sch 5 para 3(a)-(c) movement between working-age benefits | encoded | wra1-sch5-6: `sch 5 para 2 and 3 regulations may make this provision`; tests: wra1-tests-sch5-6 |
| 3080 | Hardship payments | inert | reason 1: not operative, a heading |
| 3081 | sch 5 para 4 hardship payments | encoded | wra1-sch5-6: `sch 5 para 4 regulations under section 28 may be made in relation to the person`; tests: wra1-tests-sch5-6 |
| 3082 | Earnings tapers | inert | reason 1: not operative, a heading |
| 3083-3086 | sch 5 para 5 JSA s 4(1)(b) earnings deductions in the prescribed manner | inert | reason 2: machinery, amends the Jobseekers Act 1995 so that earnings are deducted in a prescribed manner (which may include a prescribed percentage); the manner is for regulations and the allowance is another part's (wra2) |
| 3087-3091 | sch 5 para 5 WRA2007 s 2(1)(c) and (6) earnings deductions in the prescribed manner | inert | reason 2: machinery, amends the Welfare Reform Act 2007 so that earnings are deducted in a prescribed manner and construed under SSCBA 1992 ss 3, 4 and 112; the manner is for regulations and the allowance is another part's (wra2) |
| 3092 | SCHEDULE 6 — Migration to universal credit | inert | reason 1: not operative, a heading |
| 3093 | General | inert | reason 1: not operative, a heading |
| 3094 | sch 6 para 1(1) regulations for replacing existing benefits with universal credit | encoded | wra1-sch5-6: `sch 6 para 1(1) regulations may include this provision` (the guard `it is for the purposes of, or in connection with, replacing existing benefits with universal credit`); tests: wra1-tests-sch5-6 |
| 3095-3097 | sch 6 para 1(2)(a)-(b) existing benefit | encoded | wra1-sch5-6: `sch 6 para 1(2) the benefit is an existing benefit`; tests: wra1-tests-sch5-6 |
| 3098 | sch 6 para 1(3) appointed day (seat of seam 10) | encoded | wra1-sch5-6: `sch 6 para 1(3) the day is the appointed day`; tests: wra1-tests-sch5-6 |
| 3099 | Claims before the appointed day | inert | reason 1: not operative, a heading |
| 3100-3104 | sch 6 para 2(1)-(2) claims before the appointed day | encoded | wra1-sch5-6: constructors `sch 6 para 2(1)(a) a claim for universal credit made before the appointed day for a period beginning on or after that day` to `sch 6 para 2(2) an award on a claim made before the appointed day for a period before that day` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |
| 3105 | Claims after the appointed day | inert | reason 1: not operative, a heading |
| 3106-3114 | sch 6 para 3(1)-(2) claims after the appointed day | encoded | wra1-sch5-6: constructors `sch 6 para 3(1)(a) permanently or temporarily excluding a claim for universal credit after the appointed day by a person who has, or would be entitled to, an existing benefit` to `sch 6 para 3(2) an award on a claim made after the appointed day for a period before that day` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |
| 3115 | Awards | inert | reason 1: not operative, a heading |
| 3116-3129 | sch 6 para 4(1)-(3) awards | encoded | wra1-sch5-6: constructors `sch 6 para 4(1)(a) terminating an award of an existing benefit` to `sch 6 para 4(3)(b) disregarding a gap in entitlement of not more than a prescribed period` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |
| 3130 | Work-related requirements and sanctions | inert | reason 1: not operative, a heading |
| 3131-3142 | sch 6 para 5(1)-(3) work-related requirements and sanctions | encoded | wra1-sch5-6: constructors `sch 6 para 5(1)(a) the application of work-related requirements for relevant benefits` to `sch 6 para 5(3)(c) temporarily disapplying provisions of this Part about the application of sanctions` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |
| 3143-3147 | sch 6 para 5(4) "relevant benefit" | encoded | wra1-sch5-6: `sch 6 para 5(4) the benefit is a relevant benefit`; tests: wra1-tests-sch5-6 |
| 3148-3162 | sch 6 para 5(4) "work-related requirement" | encoded | wra1-sch5-6: `sch 6 para 5(4) the requirement is a work-related requirement`; tests: wra1-tests-sch5-6 |
| 3163-3167 | sch 6 para 5(4) "sanction" | encoded | wra1-sch5-6: `sch 6 para 5(4) the reduction is a sanction`; tests: wra1-tests-sch5-6 |
| 3168 | Tax credits | inert | reason 1: not operative, a heading |
| 3169-3171 | sch 6 para 6 tax credits | encoded | wra1-sch5-6: constructors `sch 6 para 6(a) modifying the application of the Tax Credits Act 2002` and `sch 6 para 6(b) recovering overpayments of working tax credit or child tax credit, including treating them as overpayments of universal credit` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |
| 3172 | Supplementary | inert | reason 1: not operative, a heading |
| 3173 | sch 6 para 7 gap in entitlement disregarded | encoded | wra1-sch5-6: constructor `sch 6 para 7 disregarding a gap in entitlement to an existing benefit` of `sch 6 provision regulations may include`; tests: wra1-tests-sch5-6 |


## Fork register (wra1)

Six forks, on seven coverage rows (the group fork covers s 13(3) and s 20(1)).
For each: the readings I saw, the text that licenses each, the one I took, and where it lives.
All six are "assumed, not ruled by a lawyer".
The chosen reading is the one a caller gets; the other reading is stated so that a lawyer can move it.

### F-8: s 8(1) "the balance" when the deductions exceed the maximum amount

- Text (lines 70-72): "The amount of an award of universal credit is to be the balance of (a) the maximum amount ..., less (b) the amounts to be deducted".
- Reading 1 (taken): the amount is the arithmetic balance, so it can be negative; the Act states no floor.
- Reading 2: an award cannot be negative, so the amount is zero when the deductions exceed the maximum.
- What licenses each: reading 1 rests on "the balance of ... less ..." and the absence of any other word in lines 70-83; reading 2 rests on nothing in the range, only on what an award is.
- Where: `s 8(1) the amount of the award of universal credit for the period` (wra1-ch1-entitlement), tested with a maximum of 100 and deductions of 80 and 50, expected `JUST (0 MINUS 30)` (wra1-tests-ch1:244).
  Seam 2 consumers (wra4's cap) receive the negative number as it stands.

### F-groups: the four groups of claimants overlap as written

- Text: s 19(2) and s 20(1) each begin "A claimant falls within this section if"; only s 21(1) ("does not fall within section 19 or 20 and") and s 22(1) ("not falling within any of sections 19 to 21") exclude the earlier groups; s 13(3) says the requirements "depend on which of the following groups the claimant falls into".
- Reading 1 (taken): each section's test is applied as written, and the single group a claimant falls into is found in the text's own order: section 19, then 20, then 21, then 22.
  So `s 20(1) the claimant falls within section 20` is true when its own words are met, even if section 19 also applies; the order is applied in `s 13(3) the group the claimant falls into`.
- Reading 2: s 20(1) carries an implied "does not fall within section 19", so the groups are mutually exclusive by construction.
- What licenses each: reading 1 follows the words of s 20(1) and the express exclusions in s 21(1) and s 22(1); reading 2 follows s 13(3)'s "which of the following groups" (one group).
- Where: `s 13(3) the group the claimant falls into`, `s 20(1) the claimant falls within section 20` (wra1-ch2-responsibilities); tests in wra1-tests-ch2.
- Why it matters: a claimant within both s 19 and s 20 is told by s 19(1) that no work-related requirement may be imposed and by s 20(2) that a work-focused interview requirement may be.
  The Act does not resolve that itself; the function for s 13(3) resolves it by order.

### F-24(6)(c): "a prescribed period has not expired since the violence was inflicted or threatened"

- Text (line 278).
- Reading 1 (taken): a period of p days has expired once p days have passed; with p = 28, the person has recently been a victim 27 days after the violence and has not 28 days after.
- Reading 2: the period expires at the end of day p, so 28 days after is still recent.
- What licenses each: both rest on "has not expired since", which does not say on which day expiry happens.
- Where: `s 24(6)(c) the person has recently been a victim of domestic violence` (wra1-ch2-responsibilities), boundary assertions with a 28-day period: 27 days is recent, 28 is not (wra1-tests-ch2:354-357).

### F-26(2)(d): "by reason of misconduct, or voluntarily and for no good reason, ceases paid work or loses pay"

- Text (line 290).
- Reading 1 (taken): misconduct, OR (voluntarily AND for no good reason).
- Reading 2: (misconduct OR voluntarily) AND for no good reason.
- What licenses each: reading 1 follows the commas, which set "by reason of misconduct" apart from "voluntarily and for no good reason"; reading 2 reads "for no good reason" as governing both.
- Where: `s 26(2) the failure is sanctionable under section 26`, limb (d), is built as misconduct OR (voluntary AND no good reason) (wra1-ch2-responsibilities:1149).
  In s 26(3) and s 26(4)(b) the whole phrase is one plain fact the caller states, so the fork bites only in s 26(2)(d).

### F-26(3): "a claimant falling within section 19 by virtue of subsection (3) of that section"

- Text (line 291), against s 19(3) (lines 215-218).
- The difficulty: s 19(3) is not a ground for falling within section 19; it says what regulations under s 19(2)(d) may refer to (hours worked, earnings or income, the amount of universal credit payable).
- Reading 1 (taken): the claimant was within section 19 because of a description prescribed under s 19(2)(d) by reference to s 19(3)'s matters; the caller states that as a plain fact (`the claimant fell within section 19 by virtue of subsection (3) of that section`).
- Reading 2: no one falls within section 19 "by virtue of subsection (3)" because (3) only describes a power, so s 26(3) is empty.
- What licenses each: reading 1 follows the purpose of s 26(3) ("so as to cease to fall within that section and to fall within section 22 instead"); reading 2 follows the literal reference.
- Where: `s 26(3) the failure is sanctionable under section 26` (wra1-ch2-responsibilities).

### F-26(6)(b): "not exceeding three years"

- Text (line 301).
- Reading 1 (taken): counting both ends, a reduction that starts on a day may last up to the day before the third anniversary.
- Reading 2: it may last up to and including the third anniversary.
- What licenses each: both rest on "not exceeding three years"; reading 1 treats a period of three years as three calendar years of days counted from the first day.
- Where: `s 26(6)(b) the period of the reduction does not exceed three years` (wra1-ch2-responsibilities), by `add years`; leap days are not tested.

The same both-ends counting is used for s 24(5) (13 weeks = 91 days, time 0 to time 90) and is measured in finding 6.


### Reading a result: FALSE and NOTHING (wra1)

This section says the rule of 2026-10-29 in the terms of this Act.
It is assumed, not ruled by a lawyer.

What a "no" is, here.
`JUST FALSE` (or a constructor meaning "the text says no") is returned only where the Act says no in its own words:

- a definition ("means", "are that", "is"): a couple (s 39(1)), a responsible carer (s 19(6)), a health care professional (s 16(6)), a compliance condition (s 27(6)), a relevant benefit (Schedule 5 para 1(1)), a sanction (Schedule 5 para 1(3), Schedule 6 para 5(4)), and the rest of s 40;
- a condition introduced with "if", "if, and only if", "does not fall within", "not falling within": the basic conditions (s 4(1)), the groups of claimants (ss 19 to 22), what makes a failure sanctionable (ss 26 and 27), what counts as accepting a claimant commitment (s 14(5));
- a flat negative: the Secretary of State "may not impose any work-related requirement" on a claimant within s 19, "may not impose any other" on one within s 20 or s 21, and may not impose "any other requirement" during the 13 weeks of s 24(5)(b); "a claimant is not entitled to state pension credit" (Schedule 2, SPCA 4(1A)); a voucher "may not in any case exceed" the costs (Schedule 1 para 6(3)); a period "may not exceed seven days" (s 6(2)); a fixed period "not exceeding 26 weeks" (s 27(5)(b)); a reduction "not exceeding three years" (s 26(6)(b)); a pilot scheme "may not have effect for a period exceeding three years" (s 41(5)).

What "not covered" is, here.
`NOTHING` (a `MAYBE` result) is returned wherever the Act hands the answer outside the text:

- every amount, rate, period and description left to regulations, which is most of Part 1: the financial conditions' capital figure and minimum, the standard allowance, the child, housing and other amounts, the length of an assessment period, the deduction percentages, the description of a claimant in s 19(2)(d), s 20(1)(b) and s 21(1)(b), the meaning of "domestic violence", the prescribed period of s 24(6)(c), the amount and period of every sanction, hardship payments and whether they are recoverable (s 28(2)(f));
- a judgment the Act leaves to the Secretary of State ("thinks fit", "considers it appropriate");
- a grant or prohibition limited by its own wording when the case falls outside the limit (reading (b));
- anything about a host Act that Schedule 2 amends: the amendment is encoded as "does this host provision now include universal credit", and what the host provision then does is not claimed.

What follows for a person in the seat.
`Under section 3(1), am I entitled to universal credit` is `NOTHING` for every set of answers, by construction: the seat passes `NOTHING` for the exception power of s 4(2) (so a failed basic condition is provisional, not a `FALSE`) and for both prescribed financial figures of s 5 (the capital limit and the minimum), none of which is among the sources.
Two cases assert it (`wra1-cases-seat.l4`).
The seat's own answer to "do I meet the basic conditions" is likewise `NOTHING` whenever a basic condition fails.
A caller must never turn `NOTHING` into `FALSE`.


## Jural relations (wra1)

Hohfeld's correlatives: a right (claim) pairs with a duty; a privilege (liberty) with a no-right; a power with a liability; an immunity with a disability.
The Act uses none of these words.
The pairing in the table is my reading of each provision, assumed and not ruled by a lawyer, and each relation is stated once, from the holder's side, never twice.
"none" means the provision creates no such relation: it is a definition, a list, a counting rule, a condition of another provision, or a signpost.
Where the table says "power, by regulations", the power is the Secretary of State's (or, in s 32, the Welsh Ministers') and the L4 rule does not encode the regulations: their outcome enters as a `MAYBE` input and `NOTHING` stays `NOTHING` (principle P1 in PROGRESS.md).
For Schedule 2 the table says what this Act does, which is to put universal credit into the host provision's list; the relation the host Act then gives is the host Act's, is not in my sources, and is not encoded (finding 4).
The L4 rule column is read from the Coverage table by script, so the names cannot drift from the files; a row that rests on inert coverage rows says so.
Every non-blank line of my ranges is under exactly one row of this table or is a heading (checked by `make_jural.py`).

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | section | L4 rule |
| --- | --- | --- | --- | --- |
| universal credit is payable under this Part | claimant (claim-right to payment) | Secretary of State (duty to pay; the subsection does not name the payer) | s 1(1) | `s 1(1) the benefit payable in accordance with this Part` |
| to whom an award may be made | none (describes the two classes of claimant) | none | s 1(2) | `s 1(2)(a) the individual is a single person`; `s 1(2) universal credit may be awarded to these claimants` |
| the four elements of an award | none (a list) | none | s 1(3) | `s 1(3) the elements by reference to which an award is calculated`; `s 1(3) the section that gives the element` |
| who may make a claim | a single person, or two people jointly (power to claim) | Secretary of State (liability to the claim) | s 2(1) | `s 2(1) a claim may be made by these claimants` |
| a member of a couple may claim as a single person where regulations provide | the member of a couple (privilege) | Secretary of State (no-right to insist on a joint claim) | s 2(2) | `s 2(2) a member of a couple may make a claim as a single person` |
| entitlement of a single claimant | the single claimant (claim-right) | Secretary of State (duty to pay) | s 3(1) | `s 3(1) the single claimant is entitled to universal credit` |
| joint entitlement of joint claimants | the joint claimants (claim-right, jointly) | Secretary of State (duty to pay) | s 3(2) | `s 3(2) joint claimants are jointly entitled to universal credit` |
| the basic conditions | none (conditions of the s 3 entitlement) | none | s 4(1)(a)-(e) | `s 4(1)(a) the person is at least 18 years old`; `s 4(1)(b) the person has not reached the qualifying age for state pension credit`; `s 4(1)(c) the place is in Great Britain`; and 3 more named in the Coverage table |
| exceptions to the basic conditions | Secretary of State (power, by regulations) | the person who does not meet a basic condition (liability) | s 4(2) | `regulations except the person from the basic condition they do not meet`; `s 4(1) the person meets the basic conditions` |
| a different minimum age | Secretary of State (power, by regulations) | the person in a prescribed case (liability) | s 4(3) | `the different minimum age regulations prescribe for this case under section 4(3)`; `s 4(1)(a) the person is at least 18 years old` |
| the qualifying age for state pension credit | none (cross-reference) | none | s 4(4) | `the person has reached the qualifying age for state pension credit`; `s 4(1)(b) the person has not reached the qualifying age for state pension credit` |
| treating a person as in or not in Great Britain | Secretary of State (power, by regulations) | the person (liability) | s 4(5)(a)-(b) | `s 4(1)(c) the person is in Great Britain` |
| modifying this Part for a person not in Great Britain | Secretary of State (power, by regulations) | the person (liability) | s 4(5)(c) | none (inert, reason 2) |
| what receiving education means | Secretary of State (power, by regulations) | the person (liability) | s 4(6) | `s 4(1)(d) the person is not receiving education` |
| treating a person as having accepted a claimant commitment | Secretary of State (power, by regulations) | the person (liability) | s 4(7) | `s 4(1)(e) the person has accepted a claimant commitment` |
| the financial conditions | none (conditions of the s 3 entitlement; their content is prescribed) | none | s 5(1)-(2) | `s 5(1)(a) the claimant's capital is not greater than the prescribed amount`; `s 5(1)(b) the amount payable would not be less than the prescribed minimum`; `s 5(1) the financial conditions for a single claimant are met`; and 3 more named in the Coverage table |
| entitlement does not arise | Secretary of State (immunity from the s 3 entitlement in these cases) | the claimant (disability: cannot acquire the entitlement) | s 6(1) | `s 6(1) entitlement to universal credit does not arise` |
| the seven-day limit on a prescribed period | none (a limit on the regulation-making power) | none | s 6(2) | `s 6(2) the prescribed period is within the seven-day limit` |
| exceptions to s 6(1)(b) or (c) | Secretary of State (power, by regulations) | the claimant (liability) | s 6(3) | `regulations provide an exception to subsection (1)(b) or (c)`; `s 6(1) entitlement to universal credit does not arise` |
| payable for each complete assessment period | claimant (claim-right) | Secretary of State (duty to pay) | s 7(1) | `s 7(1) universal credit is payable in respect of the assessment period` |
| an assessment period | none (definition; the duration is prescribed) | none | s 7(2) | `s 7(2) the period is an assessment period` |
| when an assessment period starts; shorter periods | Secretary of State (power, by regulations) | the claimant (liability) | s 7(3) | none (inert, reason 2) |
| period of entitlement | none (definition) | none | s 7(4) | `s 7(4) the period is a period of entitlement` |
| the amount of an award | claimant (claim-right to the balance) | Secretary of State (duty to pay that amount) | s 8(1) | `s 8(1) the amount of the award of universal credit for the period` |
| maximum amount, deductions and income | none (counting rules for the amount in s 8(1)) | none | s 8(2)-(4) | `s 8(2) the maximum amount`; `s 8(2) the sum of two possibly unknown amounts`; `s 8(3)(a) the amount deducted in respect of earned income`; and 2 more named in the Coverage table |
| standard allowance | claimant (claim-right to the amount in the calculation) | Secretary of State (duty to include it) | s 9(1) | `s 9(1) the calculation of the award includes the standard allowance` |
| the amount of the standard allowance | Secretary of State (power, by regulations) | the claimant (liability) | s 9(2) | none (inert, reason 2) |
| exceptions to the standard allowance | Secretary of State (power, by regulations) | the claimant (liability) | s 9(3) | `regulations provide an exception to subsection (1) for these claimants`; `s 9(1) the calculation of the award includes the standard allowance` |
| an amount for a child or qualifying young person | claimant responsible for the child (claim-right to the amount in the calculation) | Secretary of State (duty to include it) | s 10(1) | `s 10(1) the calculation of the award includes an amount for the person` |
| subsection (1A) | none (the text shows only a line of dots) | none | s 10(1A) | none (repealed or blank in this text) |
| amounts for a disabled child; the amounts | Secretary of State (power, by regulations) | the claimant (liability) | s 10(2)-(3) | none (inert, reason 2) |
| exceptions to the child amount | Secretary of State (power, by regulations) | the claimant (liability) | s 10(4) | `regulations provide an exception to subsection (1)`; `s 10(1) the calculation of the award includes an amount for the person` |
| qualifying young person | none (definition) | none | s 10(5) | `s 10(5) the person is a qualifying young person` |
| housing costs | claimant (claim-right to the amount in the calculation) | Secretary of State (duty to include it) | s 11(1) | `s 11(1) the calculation of the award includes an amount for housing costs` |
| the accommodation for housing costs | none (conditions on the amount in s 11(1)) | none | s 11(2) | `s 11(2) the accommodation is accommodation that housing costs may be included for` |
| what counts as a payment, liability or occupation | Secretary of State (power, by regulations) | the claimant (liability) | s 11(3) | `the claimant is liable to make payments in respect of the accommodation`; `the claimant occupies the accommodation as their home`; `s 11(1) the calculation of the award includes an amount for housing costs` (inert, reason 2) |
| determination of the amounts | Secretary of State (power, by regulations) | the claimant (liability) | s 11(4) | none (inert, reason 2) |
| exceptions and timing for housing costs | Secretary of State (power, by regulations) | the claimant (liability) | s 11(5) | `regulations provide an exception to subsection (1)`; `s 11(1) the calculation of the award includes an amount for housing costs` (inert, reason 2) |
| an amount for particular needs or circumstances | claimant (claim-right to the amount in the calculation, where prescribed) | Secretary of State (duty to include it) | s 12(1) | `s 12(1) the calculation of the award includes an amount for the need or circumstance` |
| the needs or circumstances that may be prescribed | none (a list that is not closed) | none | s 12(2) | `s 12(2) the needs or circumstances prescribed under subsection (1) may include` (repealed or blank in this text) |
| amounts and timing for s 12 | Secretary of State (power, by regulations) | the claimant (liability) | s 12(3)-(4) | none (inert, reason 2) |
| work-related requirements imposed | Secretary of State (claim-right that the claimant comply) | claimant (duty to comply) | s 13(1) | `s 13(1) the claimant must comply with the work-related requirement imposed`; `s 13(1) the claimant must comply with the work-related requirement` |
| the four requirements and four groups | none (a list of what the later sections define) | none | s 13(2)-(3) | `s 13(2) the section that defines the work-related requirement`; `s 13(3) the section that describes the group`; `s 13(3) the group the claimant falls into` |
| claimant commitment: what it is | none (definition) | none | s 14(1) | `s 14(1) the document is a claimant commitment` |
| preparing, reviewing and updating the commitment | Secretary of State (power) | claimant (liability) | s 14(2) | `s 14(2) this authority prepares, reviews and updates the claimant commitment` |
| the form of the commitment | Secretary of State (power) | claimant (liability) | s 14(3) | `s 14(3) the claimant commitment is in the form the Secretary of State thinks fit` |
| what the commitment includes | none (a list that is not closed) | none | s 14(4) | `s 14(4) the claimant commitment is to include` |
| when a commitment is accepted | none (definition: if, and only if) | none | s 14(5) | `s 14(5) the claimant accepts the claimant commitment` |
| work-focused interview requirement | none (definition) | none | s 15(1)-(3) | `s 15(1) the requirement is a work-focused interview requirement`; `s 15(2) the interview is a work-focused interview`; `s 15(3) the purpose may be prescribed under subsection (2)` |
| how, when and where the interview takes place | Secretary of State (power) | claimant (liability) | s 15(4) | `s 15(4) the Secretary of State may specify this for a work-focused interview` |
| work preparation requirement | none (definition) | none | s 16(1) | `s 16(1) the requirement is a work preparation requirement` |
| time to be devoted to a work preparation action | Secretary of State (power) | claimant (liability) | s 16(2) | `s 16(2) the Secretary of State may specify the time to be devoted to the action` |
| actions that may be specified | Secretary of State (power) | claimant (liability) | s 16(3)-(4) | `s 16(3) the action may be specified under subsection (1)`; `s 16(4) the action may include taking part in a work-focused health-related assessment` |
| work-focused health-related assessment; health care professional | none (definitions) | none | s 16(5)-(6) | `s 16(5) the assessment is a work-focused health-related assessment`; `s 16(6) the person is a health care professional` |
| work search requirement | none (definition) | none | s 17(1) | `s 17(1) the requirement is a work search requirement` |
| time to be devoted to a work search action | Secretary of State (power) | claimant (liability) | s 17(2) | `s 17(2) the Secretary of State may specify the time to be devoted to the action` |
| actions that may be specified | Secretary of State (power) | claimant (liability) | s 17(3) | `s 17(3) the action may be specified under subsection (1)(b)` |
| limitations on a work search requirement | claimant (immunity from the requirement beyond a limitation imposed) | Secretary of State (disability) | s 17(4)-(5) | `s 17(4) a limitation may be imposed on a work search requirement by`; `s 17(5) a limitation under subsection (4) may be` |
| work availability requirement | none (definition) | none | s 18(1)-(2) | `s 18(1) the requirement is a work availability requirement`; `s 18(2) the claimant is available for work` |
| limitations on a work availability requirement | claimant (immunity from the requirement beyond a limitation imposed) | Secretary of State (disability) | s 18(3)-(4) | `s 18(3) a limitation may be imposed on a work availability requirement by`; `s 18(4) a limitation under subsection (3) may be` |
| being able and willing immediately | Secretary of State (power, by regulations) | claimant (liability) | s 18(5) | `the claimant meets the definition regulations give of being able and willing immediately`; `s 18(2) the claimant is available for work` |
| no requirement on a claimant within s 19 | claimant within s 19 (immunity from work-related requirements) | Secretary of State (disability: may not impose one) | s 19(1) | `s 19(1) the Secretary of State may impose a work-related requirement on the claimant`; `s 19(1) the Secretary of State shall not impose a work-related requirement` |
| claimants within s 19 | none (conditions for falling within the section) | none | s 19(2) | `s 19(2) the claimant falls within section 19` |
| what regulations under s 19(2)(d) may refer to | Secretary of State (power, by regulations) | claimant (liability) | s 19(3)-(4) | none (inert, reason 2) |
| an earlier requirement ceases | claimant within s 19 (immunity) | Secretary of State (disability) | s 19(5) | `s 19(5) a work-related requirement previously applying continues to have effect` |
| responsible carer | none (definition) | none | s 19(6) | `s 19(6) the person is the responsible carer for the child` |
| claimants within s 20 | none (conditions for falling within the section) | none | s 20(1) | `s 20(1) the claimant falls within section 20` |
| a work-focused interview requirement may be imposed; no other | Secretary of State (power to impose a work-focused interview requirement); claimant within s 20 (immunity from any other) | claimant (liability); Secretary of State (disability) | s 20(2)-(3) | `s 20(2) the Secretary of State may impose this requirement on the claimant`; `s 20(3) a requirement previously applying continues to have effect` |
| claimants within s 21 | none (conditions for falling within the section) | none | s 21(1) | `s 21(1) the claimant falls within section 21` |
| work preparation and work-focused interview requirements may be imposed; no other | Secretary of State (power); claimant within s 21 (immunity from any other) | claimant (liability); Secretary of State (disability) | s 21(2)-(4) | `s 21(2) the Secretary of State may impose this requirement on the claimant`; `s 21(4) a requirement previously applying continues to have effect` |
| subsection (5) | none (the text shows only a line of dots) | none | s 21(5) | none (repealed or blank in this text) |
| claimants within s 22 | none (conditions for falling within the section) | none | s 22(1) | `s 22(1) the claimant falls within section 22` |
| a work search and a work availability requirement must be imposed | none identified (the Act names no right-holder for this duty) | Secretary of State (duty to impose, except in prescribed circumstances) | s 22(2) | `s 22(2) the Secretary of State must impose this requirement on the claimant`; `s 22(2) the Secretary of State must impose a work search requirement and a work availability requirement` |
| a work-focused interview or work preparation requirement may be imposed | Secretary of State (power) | claimant (liability) | s 22(3) | `s 22(3) the Secretary of State may impose this requirement on the claimant` |
| interviews | Secretary of State (power to require attendance) | claimant (liability) | s 23(1)-(2) | `s 23(1) the Secretary of State may require the claimant to participate in an interview for this purpose`; `s 23(2) the Secretary of State may specify this for an interview` |
| information, evidence and confirmation | Secretary of State (power to require) | claimant (liability) | s 23(3) | `s 23(3) the Secretary of State may require the claimant to do this` |
| reporting changes | Secretary of State (power to require) | claimant (liability) | s 23(4) | `s 23(4) the Secretary of State may require the claimant to report the change` |
| when a requirement must or must not be imposed | Secretary of State (power, by regulations) | claimant (liability) | s 24(1) | none (inert, reason 2) |
| regard to prescribed matters | claimant (claim-right that regard be had) | Secretary of State (duty to have regard) | s 24(2) | `s 24(2) the Secretary of State must have regard to the matters regulations prescribe` |
| revoking or changing what has been imposed | Secretary of State (power) | claimant (liability) | s 24(3) | `s 24(3) the Secretary of State may revoke or change what has been imposed or specified` |
| notification of a requirement | none (the manner of notice is for the Secretary of State to determine) | none | s 24(4) | `s 24(4) notification is in the manner the Secretary of State may determine` |
| domestic violence: 13 weeks | claimant who has recently been a victim of domestic violence (claim-right to the 13-week suspension, once regulations are made) | Secretary of State (duty: may not impose another requirement in the period) | s 24(5) | `s 24(5) the period of 13 weeks`; `s 24(5)(a) the requirement has ceased to have effect on the day`; `s 24(5)(b) the Secretary of State may impose another requirement on the day`; and 1 more named in the Coverage table |
| domestic violence and victim | none (definitions) | none | s 24(6) | `domestic violence, as regulations define it, is inflicted or threatened on or against the person`; `s 24(6)(b) the person is a victim of domestic violence`; `s 24(6)(c) the person has recently been a victim of domestic violence` |
| treating a claimant as having complied | Secretary of State (power, by regulations) | claimant (liability) | s 25 | `s 25 the claimant is treated as having complied or taken the action` |
| higher-level sanction: the award is reduced | Secretary of State (power to reduce) | claimant (liability) | s 26(1) | `s 26(1) the amount of the award is to be reduced` |
| higher-level sanctionable failures | none (the conditions on which the reduction in s 26(1) rests) | none | s 26(2)-(5) | `s 26(2) the failure is sanctionable under section 26`; `s 26(3) the failure is sanctionable under section 26`; `s 26(4) the earlier failure is sanctionable under section 26`; and 3 more named in the Coverage table |
| amount, length and variation of a higher-level reduction | Secretary of State (power, by regulations) | claimant (liability) | s 26(6)-(8) | `s 26(6)(b) the period of the reduction does not exceed three years` (inert, reason 2) |
| other sanction: the award is reduced | Secretary of State (power to reduce) | claimant (liability) | s 27(1) | `s 27(1) the amount of the award is to be reduced` |
| other sanctionable failures | none (the conditions on which the reduction in s 27(1) rests) | none | s 27(2)-(3) | `s 27(2) the failure is sanctionable under section 27` |
| amount, period and compliance condition of an other reduction | Secretary of State (power, by regulations) | claimant (liability) | s 27(4)-(9) | `s 27(5)(b) the fixed period does not exceed 26 weeks`; `s 27(6) the condition is a compliance condition`; `s 27(7) a compliance condition may be`; and 1 more named in the Coverage table (inert, reason 2) |
| hardship payments | Secretary of State (power, by regulations, to make additional payments); claimant in hardship (privilege to receive, once regulations are made) | claimant (liability); Secretary of State (no-right) | s 28(1) | `s 28(1) a hardship payment may be made to the claimant` |
| hardship payment details | Secretary of State (power, by regulations) | claimant (liability) | s 28(2) | `s 28(2)(f) the hardship payment is recoverable under section 28` (inert, reason 2) |
| authorised persons | Secretary of State (power to authorise another to exercise the functions) | the person authorised (liability); claimants (liability to an authorised person) | s 29(1) | `s 29(1) this authority may exercise the Secretary of State's functions under sections 13 to 25` |
| the terms of an authorisation | Secretary of State (power) | authorised person (liability) | s 29(2)-(3) | none (inert, reason 2) |
| what an authorised person does is treated as done by the Secretary of State | claimant (claim-right against the Secretary of State for the authorised person's acts) | Secretary of State (duty: answerable as if the act were the Secretary of State's) | s 29(4)-(5) | `s 29(4) the act is treated as done by or in relation to the Secretary of State for this purpose` |
| repudiation of the contract | authorised person (power to treat the contract as repudiated) | Secretary of State (liability) | s 29(6) | none (inert, reason 2) |
| signposts to Schedules 1, 2, 3, 4, 5 and 6 | none | none | ss 30, 31, 33(3), 34, 35, 36 | none (inert, reason 1) |
| supplementary, consequential, incidental or transitional provision | Secretary of State or the Welsh Ministers (power, by regulations) | persons affected (liability) | s 32 | none (inert, reason 2) |
| benefits abolished | Secretary of State (immunity: no claim lies to an abolished benefit) | person who would have claimed it (disability) | s 33(1) | `s 33(1) the benefit is abolished` |
| income-based JSA and income-related ESA | none (definitions) | none | s 33(2) | `s 33(2)(a) the allowance is income-based jobseeker's allowance`; `s 33(2)(b) the allowance is income-related employment and support allowance` |
| limited capability for work and for work-related activity | none (definitions: the Act's own test) | none | s 37(1)-(3) | `s 37(1) the claimant has limited capability for work on the Act's own test`; `s 37(2) the claimant has limited capability for work-related activity on the Act's own test`; `s 37(3) the claimant has limited capability as determined in accordance with regulations` |
| assessment, information, treatment as having limited capability | Secretary of State (power, by regulations) | claimant (liability) | s 37(4)-(9) | none (inert, reason 2) |
| information relating to social security | none (a classification) | none | s 38 | `s 38 the information is information relating to social security` |
| couple | none (definition) | none | s 39(1) | `s 39(1) the two people are a couple` |
| subsection (2) | none (the text shows only a line of dots) | none | s 39(2) | none (repealed or blank in this text) |
| couple: prescribed circumstances | Secretary of State (power, by regulations) | the two people (liability) | s 39(3) | `s 39(3) the two people are a couple once the regulations supplied are applied` |
| interpretation | none (definitions) | none | s 40 | `s 40 where the meaning is given`; `s 7(2) the period is an assessment period`; `s 40 the person is a child`; and 20 more named in the Coverage table |
| pilot schemes | Secretary of State (power, by regulations or order) | persons in the pilot areas or classes (liability) | s 41(1)-(4), (6) | none (inert, reason 2) |
| a pilot scheme has a time limit | persons within a pilot scheme (immunity from a scheme beyond three years) | Secretary of State (disability) | s 41(5) | `s 41(5) the pilot scheme's own period is within three years`; `s 41(5)(a) the order's continuation is within twelve months` (inert, reason 2) |
| regulations: who makes them, how, by what procedure | none (machinery) | none | ss 42, 43 | none (inert, reason 1/2) |
| joint claimants without each meeting the basic conditions | Secretary of State (power, by regulations) | joint claimants (liability) | sch 1 para 1 | `sch 1 para 1 joint claimants may be entitled without each meeting all the basic conditions` |
| linking periods | Secretary of State (power, by regulations) | claimant (liability) | sch 1 para 2 | `sch 1 para 2 the two periods are treated as a single period` |
| couples: claims, awards | Secretary of State (power, by regulations) | the couple (liability) | sch 1 para 3 | none (inert, reason 2) |
| capital and income | Secretary of State (power, by regulations) | claimant (liability) | sch 1 para 4(1)-(4) | none (inert, reason 2) |
| joint claimants' capital and income | Secretary of State (power, by regulations) | joint claimants (liability) | sch 1 para 4(5)-(6) | `sch 1 para 4(5) the joint capital and income includes this person's separate capital and income` |
| responsibility for a child; nominations of the responsible carer | Secretary of State (power, by regulations) | the persons concerned (liability) | sch 1 para 5 | `sch 1 para 5(1) the person is responsible for the child or qualifying young person`; `sch 1 para 5(2) the couple has jointly nominated the person as the responsible carer` |
| vouchers | Secretary of State (power, by regulations, to discharge liability to pay by a voucher) | claimant (liability) | sch 1 para 6(1)-(2), (4)-(5) | `sch 1 para 6(2) liability to pay all or part of the award may be discharged by a voucher`; `sch 1 para 6(4) the means is a voucher`; `sch 1 para 6(5) a voucher may be` |
| a voucher may not exceed the costs | claimant (immunity from a voucher larger than the costs) | Secretary of State (disability) | sch 1 para 6(3) | `sch 1 para 6(3) the amount paid by means of the voucher is permitted` |
| EU right to reside | Secretary of State (power, by regulations, to treat a claimant as outside ss 19 to 21) | claimant with an EU Treaty right to reside (liability) | sch 1 para 7 | `sch 1 para 7 the claimant is treated as not falling within section 19, 20 or 21`; `sch 1 para 7 the claimant falls within the section once regulations are applied` |
| good reason | Secretary of State (power, by regulations) | claimant (liability) | sch 1 para 8 | `sch 1 para 8(a) the person is treated as having a good reason for the act or omission` (inert, reason 2) |
| amendments to the Children Act 1989 and Child Support Act 1991 | none (this Act creates no relation; it puts universal credit in the host provision's list, and the host Act's relation is not encoded) | none | sch 2 (CA1989, CSA1991) | `sch 2 CA1989 s 17(9)`; `sch 2 CA1989 s 17A(5)(b)`; `sch 2 CA1989 s 29(3) and (3A)`; and 4 more named in the Coverage table (inert, reason 1) |
| amendments to the Social Security Administration Act 1992 (other than ss 159D, 160C) | none (this Act creates no relation; it puts universal credit in the host provision, or adds this Act to a list; the host Act's relation is not encoded) | none | sch 2 (SSAA 1992) | `sch 2 SSAA s 1(4)(za)`; `sch 2 host provision`; `sch 2 the host provision now includes universal credit`; and 15 more named in the Coverage table (inert, reason 1/2, repealed or blank in this text) |
| alterations that change the amount of universal credit | recipient (claim-right to the altered amount from the commencing date, without a further decision, subject to exceptions) | Secretary of State (duty to pay it) | sch 2 SSAA 159D | `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision`; `sch 2 SSAA 159D(3) the award continues in force`; `an alteration affects the computation of the amount of universal credit to which the recipient is entitled`; and 3 more named in the Coverage table (inert, reason 1/2) |
| increases from reaching a particular age | recipient (claim-right to the increased amount from the day, without a further decision, subject to subsections (3) and (4)) | Secretary of State (duty to pay it) | sch 2 SSAA 160C | `sch 2 SSAA 160C(2) the increased amount is payable from the day without any further decision`; `sch 2 SSAA 159D(6) the amount is an element of universal credit` (inert, reason 1) |
| amendments to the Local Government Finance Act 1992, Jobseekers Act 1995, Housing Act 1996, Education Act 1996 | none (this Act creates no relation; the host Act's relation is not encoded) | none | sch 2 (LGFA, JSA, HA1996, EA1996) | `sch 2 LGFA Sch 4 para 6(1)`; `sch 2 LGFA Sch 4 para 6(2)(b)`; `sch 2 host provision`; and 9 more named in the Coverage table (inert, reason 1/2) |
| amendments to the Social Security (Recovery of Benefits) Act 1997 | none (this Act creates no relation; the host Act's relation is not encoded) | none | sch 2 (SSRBA1997) | `sch 2 SSRBA1997 s 29 definition of benefit`; `sch 2 host provision`; `sch 2 the host provision now includes universal credit`; and 1 more named in the Coverage table (inert, reason 1) |
| amendments to the Social Security Act 1998 (appeals, correction of errors) | claimant (as the host Act gives: a right of appeal where the decision is in its Schedule 3 list, none where in its Schedule 2 list) | Secretary of State (as the host Act gives) | sch 2 (SSA1998) | `sch 2 SSA1998 s 8(3)(aa)`; `sch 2 host provision`; `sch 2 the host provision now includes universal credit`; and 3 more named in the Coverage table (inert, reason 1/2) |
| amendments to the Immigration and Asylum Act 1999, Child Support, Pensions and Social Security Act 2000, Social Security Fraud Act 2001 (introductory words) | none (this Act creates no relation; the host Act's relation is not encoded) | none | sch 2 (IAA1999, CSPSSA2000, SSFA intro) | `sch 2 IAA1999 s 97(5)(za)`; `sch 2 host provision`; `sch 2 the host provision now includes universal credit`; and 2 more named in the Coverage table (inert, reason 1) |
| loss of benefit: universal credit as the sanctionable benefit | Secretary of State (power, by regulations) | the person whose benefit is sanctioned (liability) | sch 2 SSFA 6B, 7, 9, 11 | `sch 2 SSFA 6A(1)(za) the benefit is a disqualifying benefit`; `sch 2 SSFA 6B(5A) regulations may provide that universal credit is payable as if this applied`; `sch 2 SSFA 7(2A) regulations may provide that universal credit is payable as if this applied`; and 5 more named in the Coverage table (inert, reason 2) |
| state pension credit and a couple below the qualifying age | Secretary of State (immunity from a state pension credit claim by a member of such a couple) | claimant (disability) | sch 2 SPCA 4(1A) | `sch 2 SPCA 4(1A) the claimant is entitled to state pension credit` |
| amendment to the Welfare Reform Act 2007 | none (this Act creates no relation; the host Act's relation is not encoded) | none | sch 2 (WRA2007) | `sch 2 WRA2007 Sch 1 para 1(5)(za)`; `sch 2 host provision`; `sch 2 the host provision now includes universal credit` |
| relevant benefit, work-related requirement, sanction | none (definitions) | none | sch 5 para 1 | `sch 5 para 1(1) the benefit is a relevant benefit`; `sch 5 para 1(2) the requirement is a work-related requirement`; `sch 5 para 1(3) the reduction is a sanction` |
| the amount of a relevant benefit where the person is entitled to both | Secretary of State (power, by regulations) | the person entitled to both (liability) | sch 5 paras 2-3 | `sch 5 para 2(1) the amount payable by way of the relevant benefit`; `sch 5 para 2 and 3 regulations may make this provision` |
| hardship payments | Secretary of State (power, by regulations) | the person (liability) | sch 5 para 4 | `sch 5 para 4 regulations under section 28 may be made in relation to the person` |
| earnings deductions in the prescribed manner | none (amends the Jobseekers Act 1995 and the Welfare Reform Act 2007; the host Acts' relations are not encoded) | none | sch 5 para 5 | none (inert, reason 2) |
| replacing existing benefits with universal credit | Secretary of State (power, by regulations) | persons entitled to existing benefits (liability) | sch 6 para 1 | `sch 6 para 1(1) regulations may include this provision`; `it is for the purposes of, or in connection with, replacing existing benefits with universal credit`; `sch 6 para 1(2) the benefit is an existing benefit`; and 1 more named in the Coverage table |
| claims before and after the appointed day; awards; work-related requirements | Secretary of State (power, by regulations) | persons concerned (liability) | sch 6 paras 2-5(3) | `sch 6 para 2(1)(a) a claim for universal credit made before the appointed day for a period beginning on or after that day`; `sch 6 para 2(2) an award on a claim made before the appointed day for a period before that day`; `sch 6 provision regulations may include`; and 6 more named in the Coverage table |
| relevant benefit, work-related requirement, sanction | none (definitions for sch 6 para 5) | none | sch 6 para 5(4) | `sch 6 para 5(4) the benefit is a relevant benefit`; `sch 6 para 5(4) the requirement is a work-related requirement`; `sch 6 para 5(4) the reduction is a sanction` |
| tax credits; gap in entitlement | Secretary of State (power, by regulations) | persons concerned (liability) | sch 6 paras 6-7 | `sch 6 para 6(a) modifying the application of the Tax Credits Act 2002`; `sch 6 para 6(b) recovering overpayments of working tax credit or child tax credit, including treating them as overpayments of universal credit`; `sch 6 provision regulations may include`; and 1 more named in the Coverage table |


## Marginal readings for a lawyer (wra1)

The brief marks two readings "for a lawyer, not for you to decide", and asks for every branch that rests on one, with the other reading stated.
Status quo taken throughout: (a) a failed "if" counts as the text's no, clause by clause within the provision that holds the "if", and a flat negative counts as the text saying no; (b) a prohibition or grant limited by its own wording does not say no outside the limit.
Each branch below carries a `-- FALSE-kind` or `-- NOTHING-kind` comment in the file, and the tables are generated from those comments (`marginal.py`), so a branch cannot be listed here without being marked there.
The location is `file:line` in the deposit file, with `wra1-` and `.l4` dropped from the file name.
A function can appear under more than one heading.
Of the 189 `FALSE` or `NOTHING` branches in layer 1, these are the ones that rest on a reading: the rest rest on "means" or "are that", a list closed with "only", a supplied regulation's answer, or on the text being silent, open, undefined or pointing outside itself.

#### Reading (a), a failed "if" counts as the text's no: 13 branches in 13 functions

The status quo takes the text's "if" to say no when the condition fails (`JUST FALSE`).
**The other reading:** "if A then B" does not itself say "if not A then not B", so when A fails the Act does not answer, and the branch would be `NOTHING`.

| function | file:line, and the words the branch rests on |
| --- | --- |
| `s 3(1) the single claimant is entitled to universal credit` | ch1-entitlement:126: "is entitled to universal credit if the claimant meets (a) ... and (b) ..." (a failed "if": lawyer's reading (a)) |
| `s 3(2) joint claimants are jointly entitled to universal credit` | ch1-entitlement:138: "are jointly entitled to universal credit if (a) each of them meets the basic conditions, and (b) they meet the financial conditions" (a failed "if": lawyer's reading (a)... |
| `s 6(1) entitlement to universal credit does not arise` | ch1-entitlement:411: "if the requirements in section 3 are met for a period shorter than a prescribed period" (a failed "if": lawyer's reading (a)) |
| `s 19(2) the claimant falls within section 19` | ch2-responsibilities:575: "A claimant falls within this section if (a) ... (d)" (a failed "if": lawyer's reading (a)), when every limb is known to fail |
| `s 20(1) the claimant falls within section 20` | ch2-responsibilities:628: "A claimant falls within this section if (a) ... or (b) ..." (a failed "if": lawyer's reading (a)), when both limbs are known to fail |
| `s 21(1) the claimant falls within section 21` | ch2-responsibilities:685: "A claimant falls within this section if the claimant does not fall within section 19 or 20 and (a) ... (aa) ... or (b) ..." (a failed "if": lawyer's reading (a)) |
| `s 24(6)(c) the person has recently been a victim of domestic violence` | ch2-responsibilities:1066: "if a prescribed period has not expired since the violence was inflicted or threatened" (a failed "if": lawyer's reading (a)) |
| `s 26(2) the failure is sanctionable under section 26` | ch2-responsibilities:1138: "It is a failure sanctionable under this section if a claimant falling within section 22 ..." (a failed "if": lawyer's reading (a)) |
| `s 26(3) the failure is sanctionable under section 26` | ch2-responsibilities:1162: "It is a failure sanctionable under this section if by reason of misconduct, or voluntarily and for no good reason, a claimant falling within section 19 by virtue of subs... |
| `s 26(4) the earlier failure is sanctionable under section 26` | ch2-responsibilities:1180: "It is a failure sanctionable under this section if, at any time before making the claim ..., the claimant (a) ... or (b) ..." (a failed "if": lawyer's reading (a)) |
| `s 27(2) the failure is sanctionable under section 27` | ch2-responsibilities:1238: "It is a failure sanctionable under this section if a claimant (a) fails for no good reason ...; (b) ..." (a failed "if": lawyer's reading (a)) |
| `s 37(1) the claimant has limited capability for work on the Act's own test` | ch3-general:71: "has limited capability for work if (a) ... and (b) ..." (a failed "if": lawyer's reading (a)) |
| `s 37(2) the claimant has limited capability for work-related activity on the Act's own test` | ch3-general:83: "has limited capability for work-related activity if (a) ... and (b) ..." (a failed "if": lawyer's reading (a)) |

#### Reading (a), a flat negative counts as the text saying no: 20 branches in 18 functions

The status quo takes "may not", "does not apply", "is not entitled", "ceases to have effect" and "not exceeding" to be the text's own no for the case they name (`JUST FALSE`).
**The other reading:** a flat negative is a rule about the case it names, and does not say what happens elsewhere; the branch for the case it does not name would be `NOTHING`, and for the case it names the answer would be unchanged.

| function | file:line, and the words the branch rests on |
| --- | --- |
| `s 6(2) the prescribed period is within the seven-day limit` | ch1-entitlement:429: "may not exceed seven days" |
| `s 19(1) the Secretary of State may impose a work-related requirement on the claimant` | ch2-responsibilities:587: "The Secretary of State may not impose any work-related requirement on a claimant falling within this section" |
| `s 19(5) a work-related requirement previously applying continues to have effect` | ch2-responsibilities:610: "any work-related requirement previously applying to the claimant ceases to have effect" |
| `s 20(2) the Secretary of State may impose this requirement on the claimant` | ch2-responsibilities:645: "The Secretary of State may not impose any other work-related requirement on a claimant falling within this section" |
| `s 20(3) a requirement previously applying continues to have effect` | ch2-responsibilities:662: "any other work-related requirement previously applying to the claimant ceases to have effect" |
| `s 21(2) the Secretary of State may impose this requirement on the claimant` | ch2-responsibilities:707: "The Secretary of State may not impose any other work-related requirement on a claimant falling within this section" |
| `s 21(4) a requirement previously applying continues to have effect` | ch2-responsibilities:725: "any other work-related requirement previously applying to the claimant ceases to have effect" |
| `s 24(5)(b) the Secretary of State may impose another requirement on the day` | ch2-responsibilities:1012: "the Secretary of State may not impose any other requirement under this Part on that claimant during that period" |
| `s 26(6)(b) the period of the reduction does not exceed three years` | ch2-responsibilities:1196: "not exceeding three years in relation to any failure sanctionable under this section" |
| `s 27(2) the failure is sanctionable under section 27` | ch2-responsibilities:1233: "a failure by a claimant is not sanctionable under this section if it is also a failure sanctionable under section 26" |
| `s 27(5)(b) the fixed period does not exceed 26 weeks` | ch2-responsibilities:1249: "a fixed period not exceeding 26 weeks" |
| `s 29(4) the act is treated as done by or in relation to the Secretary of State for this purpose` | ch2-responsibilities:1394: "Subsection (4) does not apply (a) for the purposes of so much of any contract ..."; ch2-responsibilities:1396: "Subsection (4) does not apply ... (b) for the purposes of any criminal proceedings ..." |
| `s 41(5) the pilot scheme's own period is within three years` | ch3-general:397: "A pilot scheme may not have effect for a period exceeding three years" |
| `s 41(5)(a) the order's continuation is within twelve months` | ch3-general:405: "for a period not exceeding twelve months" |
| `sch 1 para 6(3) the amount paid by means of the voucher is permitted` | sch1:132: "may not in any case exceed the total of the amounts referred to in sub-paragraph (1)" |
| `sch 2 SSAA 160C(2) the increased amount is payable from the day without any further decision` | sch2:515: "Subsection (2) does not apply where, in consequence of the recipient or other person reaching the qualifying age, a question arises" |
| `sch 2 SSA1998 an appeal lies against the decision` | sch2:569: added to "Schedule 2 (decisions against which no appeal lies)"; sch2:571: added to "Schedule 2 (decisions against which no appeal lies)" |
| `sch 2 SPCA 4(1A) the claimant is entitled to state pension credit` | sch2:703: "A claimant is not entitled to state pension credit if he is a member of a couple the other member of which has not attained the qualifying age" |

#### Reading (b), a prohibition or grant limited by its own wording does not say no outside the limit: 57 branches in 49 functions

The status quo answers `NOTHING` (`NOTHING-kind (limited by its own wording)`) when the case falls outside the limit the words set.
**The other reading:** a grant limited to a case also says that outside the case there is no such power or right, and the branch would be `JUST FALSE`.

| function | file:line, and the words the branch rests on |
| --- | --- |
| `s 1(2) universal credit may be awarded to these claimants` | ch1-entitlement:54: "may ... be awarded to ... (b) members of a couple jointly" does not say that joint claimants who are not a couple may not |
| `s 7(1) universal credit is payable in respect of the assessment period` | ch1-entitlement:447: only a "complete assessment period within a period of entitlement" is covered; s 7(3)(b) lets regulations make a shorter period payable |
| `s 10(1) the calculation of the award includes an amount for the person` | ch1-entitlement:623: "each child or qualifying young person for whom a claimant is responsible"; a person outside that description is not covered |
| `s 11(1) the calculation of the award includes an amount for housing costs` | ch1-entitlement:673: "any liability of a claimant to make payments in respect of the accommodation they occupy as their home"; a case outside that description is not covered |
| `s 13(1) the claimant must comply with the work-related requirement` | ch2-responsibilities:50: the duty is to comply with "work-related requirements" the Secretary of State imposes; where none is imposed the section is silent |
| `s 14(3) the claimant commitment is in the form the Secretary of State thinks fit` | ch2-responsibilities:118: "such form as the Secretary of State thinks fit"; a form the Secretary of State does not think fit is outside the grant |
| `s 15(4) the Secretary of State may specify this for a work-focused interview` | ch2-responsibilities:214: "how, when and where" are the matters the grant names |
| `s 16(2) the Secretary of State may specify the time to be devoted to the action` | ch2-responsibilities:240: the power is "to any particular action" specified under subsection (1) |
| `s 16(4) the action may include taking part in a work-focused health-related assessment` | ch2-responsibilities:288: "In the case of a person with limited capability for work"; a person outside that description is not covered |
| `s 17(2) the Secretary of State may specify the time to be devoted to the action` | ch2-responsibilities:370: the power is "to any particular action" specified under subsection (1)(b) |
| `s 19(1) the Secretary of State may impose a work-related requirement on the claimant` | ch2-responsibilities:589: the prohibition is for "a claimant falling within this section"; a claimant outside it is not covered here |
| `s 19(5) a work-related requirement previously applying continues to have effect` | ch2-responsibilities:612: "Where a claimant falls within this section"; a claimant outside it is not covered here |
| `s 20(2) the Secretary of State may impose this requirement on the claimant` | ch2-responsibilities:647: the grant and the prohibition are for "a claimant falling within this section" |
| `s 20(3) a requirement previously applying continues to have effect` | ch2-responsibilities:664: "where a claimant falls within this section" |
| `s 21(2) the Secretary of State may impose this requirement on the claimant` | ch2-responsibilities:709: the grants and the prohibition are for "a claimant falling within this section" |
| `s 21(4) a requirement previously applying continues to have effect` | ch2-responsibilities:727: "where a claimant falls within this section" |
| `s 22(2) the Secretary of State must impose this requirement on the claimant` | ch2-responsibilities:791: (3) gives only a power to impose a work-focused interview requirement or a work preparation requirement, not a duty; ch2-responsibilities:803: the duty is for "a claimant falling within this section" |
| `s 22(3) the Secretary of State may impose this requirement on the claimant` | ch2-responsibilities:823: the power is for "a claimant falling within this section" |
| `s 23(1) the Secretary of State may require the claimant to participate in an interview for this purpose` | ch2-responsibilities:869: "for any purpose relating to" (a) to (c) |
| `s 23(2) the Secretary of State may specify this for an interview` | ch2-responsibilities:888: "how, when and where" are the matters the grant names |
| `s 23(3) the Secretary of State may require the claimant to do this` | ch2-responsibilities:912: (a) and (b) are the two things the power names; ch2-responsibilities:914: the power is "for the purpose of verifying the claimant's compliance" |
| `s 23(4) the Secretary of State may require the claimant to report the change` | ch2-responsibilities:929: "any specified changes in their circumstances which are relevant to" (a) or (b) |
| `s 24(2) the Secretary of State must have regard to the matters regulations prescribe` | ch2-responsibilities:943: the duty is for the case where the Secretary of State "may impose" or "specify" |
| `s 24(3) the Secretary of State may revoke or change what has been imposed or specified` | ch2-responsibilities:954: the power is for the case where the Secretary of State "may impose a requirement under this Part, or specify any action" |
| `s 24(4) notification is in the manner the Secretary of State may determine` | ch2-responsibilities:965: the manner is the Secretary of State's to determine only "if not included in the claimant commitment" |
| `s 24(5)(a) the requirement has ceased to have effect on the day` | ch2-responsibilities:994: "in prescribed circumstances, where a claimant has recently been a victim of domestic violence"; outside them the paragraph says nothing; ch2-responsibilities:996: "for a period of 13 weeks"; a day outside the period is not covered |
| `s 24(5)(b) the Secretary of State may impose another requirement on the day` | ch2-responsibilities:1014: the prohibition is for prescribed circumstances in which the claimant has recently been a victim; ch2-responsibilities:1016: "during that period" |
| `s 26(1) the amount of the award is to be reduced` | ch2-responsibilities:1100: the reduction is "in the event of a failure ... sanctionable under this section"; with no such failure this section is silent |
| `s 27(1) the amount of the award is to be reduced` | ch2-responsibilities:1209: the reduction is "in the event of a failure ... sanctionable under this section"; with no such failure this section is silent |
| `s 27(7) a compliance condition may be` | ch2-responsibilities:1289: (a) and (b) are the two things the subsection names |
| `s 28(1) a hardship payment may be made to the claimant` | ch2-responsibilities:1332: the provision is for payments "where ... the claimant is or will be in hardship"; ch2-responsibilities:1335: the provision is for payments "where the amount of the claimant's award is reduced under section 26 or 27" |
| `s 29(1) this authority may exercise the Secretary of State's functions under sections 13 to 25` | ch2-responsibilities:1368: "such person as the Secretary of State may authorise for the purpose"; a person not so authorised is outside the grant |
| `s 29(4) the act is treated as done by or in relation to the Secretary of State for this purpose` | ch2-responsibilities:1399: subsection (4) is for things done "by or in relation to an authorised person ... in ... the exercise or purported exercise of the function" |
| `sch 1 para 1 joint claimants may be entitled without each meeting all the basic conditions` | sch1:39: the power is for "joint claimants" |
| `sch 1 para 2 the two periods are treated as a single period` | sch1:56: "separated by no more than a prescribed number of days"; periods further apart are not covered |
| `sch 1 para 4(5) the joint capital and income includes this person's separate capital and income` | sch1:81: the rule is "In the case of joint claimants" |
| `sch 1 para 6(2) liability to pay all or part of the award may be discharged by a voucher` | sch1:121: paragraph 6 "applies in relation to an award ... where the calculation ... includes an amount in respect of particular costs" |
| `sch 1 para 6(5) a voucher may be` | sch1:163: (a) and (b) are the two things the sub-paragraph names, and it does not say a voucher may be nothing else |
| `sch 2 SSAA 159D(2) the amount of universal credit payable on the day without any further decision` | sch2:466: subsection (2) applies where an award is in force and an alteration affects the computation, "as from the commencing date" |
| `sch 2 SSAA 159D(3) the award continues in force` | sch2:480: subsection (3) is for the case where the recipient "continues ... to be entitled to the same amount" |
| `sch 2 SSAA 160C(2) the increased amount is payable from the day without any further decision` | sch2:518: section 160C "applies where" an award is in force and an element has become applicable because of a particular age |
| `sch 2 SSA1998 39(1) this is the claimant in relation to the couple` | sch2:543: the definition is "in relation to a couple jointly claiming universal credit" |
| `sch 2 SSFA 6B(5A) regulations may provide that universal credit is payable as if this applied` | sch2:624: the power is for "one or more of the following"; sch2:626: the power is "where the sanctionable benefit is universal credit" |
| `sch 2 SSFA 7(2A) regulations may provide that universal credit is payable as if this applied` | sch2:654: the power is for "one or more of the following"; sch2:656: the power is "where the sanctionable benefit is universal credit" |
| `sch 2 SSFA 9(2A) regulations may provide that the family member's universal credit is payable as if this applied` | sch2:686: the provision is "one or more of the following"; sch2:688: the provision is "in relation to cases in which the benefit is universal credit" |
| `sch 2 SPCA 4(1A) the claimant is entitled to state pension credit` | sch2:705: subsection (1A) bars entitlement in that case; it does not give entitlement in any other |
| `sch 5 para 2(1) the amount payable by way of the relevant benefit` | sch5-6:98: the power is "where a person is entitled to that benefit and universal credit" |
| `sch 5 para 4 regulations under section 28 may be made in relation to the person` | sch5-6:155: the paragraph reaches a person "whose award of universal credit is reduced by virtue of regulations under paragraph 2(3)(b) or 3(b)"; a person reduced under section 26 or... |
| `sch 6 para 1(1) regulations may include this provision` | sch5-6:319: the power is for provision "for the purposes of, or in connection with, replacing existing benefits with universal credit" |


#### Three more readings a lawyer should see (not the brief's two)

1. **s 14(2) and s 29(1), a composition.**
   `s 14(2) this authority prepares, reviews and updates the claimant commitment` answers `JUST TRUE` for "an authorised person" as well as for the Secretary of State.
   The words of s 14(2) name the Secretary of State only; the extra branch comes from s 29(1) (the Secretary of State's functions "under sections 13 to 25" may be exercised by an authorised person).
   It is marked in the file as a composition, not the words of s 14(2).
   The other reading: s 14(2) says nothing of an authorised person, so the branch is `NOTHING`.
2. **s 29(1) for the Secretary of State.**
   `s 29(1) this authority may exercise the Secretary of State's functions under sections 13 to 25` answers `NOTHING` when the authority is the Secretary of State, and `JUST TRUE` for another person the Secretary of State has authorised, `NOTHING` for one not authorised.
   The subsection is about "such person as the Secretary of State may authorise", so it is silent about the Secretary of State's own power, which comes from sections 13 to 25 themselves.
   An earlier draft answered `JUST TRUE` for the Secretary of State, which went beyond the subsection's words; I tightened it and flipped its test (`NOTHING-kind (silent)`).
   The other reading: the Secretary of State can of course exercise their own functions, so `JUST TRUE`.
3. **Schedule 2, SSA1998 appeals, read from the host Schedule's heading.**
   `sch 2 SSA1998 an appeal lies against the decision` answers `JUST FALSE` for the two decisions the amendments add to Schedule 2 of the 1998 Act and `JUST TRUE` for the one added to Schedule 3, because the inserted text sits under the host Schedule headings "(decisions against which no appeal lies)" and "(decisions against which an appeal lies)".
   Those headings are in the amending text (lines 2847 and 2854), but a heading is not an operative sentence.
   It is listed above under reading (a), flat negatives; the other reading there is `NOTHING`.
   Whether an appeal lies for any decision not added by this Act is `NOTHING`: the 1998 Act is not among the sources.


## Seams (wra1)

PLAN.md section 8 names ten seams.
Seven touch my ranges: five as answerer (1, 2, 3, 4 and 7) and two as asker (9 and 10).
For each I give the plan's input, the name and type I actually wrote, and the difference.
**Every function I wrote returns `MAYBE BOOLEAN` or `MAYBE NUMBER` where the plan says `BOOLEAN` or `NUMBER`**, because principle P1 (PLAN.md section 7) makes a regulation-supplied value a `MAYBE` input and lets `NOTHING` flow through; the lead's wiring at the merge must pass a `MAYBE` or unwrap one, and must not turn `NOTHING` into `FALSE`.

| seam | role | the plan's input | what wra1 wrote (name, type) | difference |
| --- | --- | --- | --- | --- |
| 1 | answerer (for wra2) | `s 39(1) the person is a member of a couple` : `BOOLEAN` | `s 39(1) the two people are a couple` taking a core `Two people`, `BOOLEAN` (wra1-ch3-general); the seat adds `Under section 39(1), are the other person and I a couple` | the name differs, and the function takes a core `Two people` (the pair s 39(1) turns on), not one person; a caller who holds one person must build a `Two people` first, or the lead must wrap it |
| 2 | answerer (for wra4) | `s 8(1) the amount of the award of universal credit for the period` : `NUMBER` | the same name, `MAYBE NUMBER` (wra1-ch1-entitlement) | type only; a negative number is possible (fork F-8) |
| 3 | answerer (for wra4) | `s 3 the claimant is entitled to universal credit for the period` : `BOOLEAN` | two functions, `s 3(1) the single claimant is entitled to universal credit` and `s 3(2) joint claimants are jointly entitled to universal credit`, both `MAYBE BOOLEAN` | split by the Act's own two subsections; the plan's name is not defined; always `NOTHING` in the seat today (the financial conditions are prescribed) |
| 4 | answerer (for wra4) | `s 28(2)(f) the hardship payment is recoverable under section 28` : `BOOLEAN` (the regulations' answer, supplied) | the same name; the input is `the regulations' answer, if supplied` : `MAYBE BOOLEAN`, and the function returns `MAYBE BOOLEAN` (wra1-ch2-responsibilities) | `NOTHING` in, `NOTHING` out |
| 7 | answerer, one limb (with wra4) | a composite of the two parts' limbs | `sch 2 SSFA 6A(1)(za) the benefit is a disqualifying benefit`, `sch 2 SSFA 6B(5A) regulations may provide that universal credit is payable as if this applied`, `sch 2 SSFA 7(2A) ...`, `sch 2 SSFA 9(2A) ...` (wra1-sch2), each `MAYBE BOOLEAN` | only my limb: universal credit; a benefit named by the other part's limb is `NOTHING` here (list not closed); the lead writes the composite |
| 9 | asker (of wra2) | no input: the core's `Provision that reduces an award` and `Work-related requirement` | `sch 5 para 1(1)`, `1(2)`, `1(3)` and `sch 6 para 5(4)` definitions written over the core types (wra1-sch5-6), `BOOLEAN` | none; but the two "sanction" lists differ (finding 3) |
| 10 | asker (of wra3) | `s 150(3) the day appointed for the coming into force of section 1` : `MAYBE DATE` | the same name as the input of `sch 6 para 1(3) the day is the appointed day` : `MAYBE BOOLEAN` (wra1-sch5-6) | none |

Seams 5, 6 and 8 do not involve my ranges.
For seam 8 I did not take the shared reading, because s 102 and Schedule 11 are wra3's and wra4's.

One seam the plan lacks.
`sch 2 SSA1998 an appeal lies against the decision` (wra1-sch2) answers "is this decision on the lists in Schedules 2 and 3 to the Social Security Act 1998" for the three decisions this Act adds.
Seam 8 (wra3 and wra4) answers a related question about the same 1998 Act from the other side: whether the right of appeal arises only after the Secretary of State has considered revising the decision (SSA1998 s 12(3A)).
A caller asking "may I appeal this universal credit decision" would need both answers, and the plan does not say who composes them (my reading, assumed, not ruled).
The two `NOTHING`s are different: mine is "the decision is not one this Act added to either list", theirs is "no regulations among the sources require consideration of revision first".

Two things that look like seams and are not (as the plan says): s 4(1)(b)/s 4(4) borrow the qualifying age of the State Pension Credit Act 2002 s 1(6), and I ask it as a plain `BOOLEAN` input (`the person has reached the qualifying age for state pension credit`); s 39 defines "couple" for this Act, not for s 96.

## The seat layer (wra1-seat.l4, wra1-cases-seat.l4)

48 exported questions, grouped under `§` headings; each has `@export` and `@desc`, plain inputs (yes/no, numbers, dates, the modules' own choices), and calls the layer-1 rules without restating them.
A fact only regulations decide is asked as the three-way `s 1(1) what I know` (yes, no, I do not know), or passed on as `NOTHING` with a comment.
A record a layer-1 rule expects is built inside the question from the person's answers; a field no rule reads gets a fixed placeholder with a comment saying so.
A period is built inside the question from two dates.
Questions begin "Under section N, ..." or "Under schedule N paragraph M, ...", and for Schedule 2, which prints no paragraph numbers, "Under schedule 2 (<host provision>), ...".

**Helpers shared by the questions**


**Part 1 Chapter 1 -- Universal credit: entitlement**

- `Under section 1(2), may universal credit be awarded to me`
- `Under section 4(1)(a), am I at least 18 years old`
- `Under section 4(1)(b), have I not yet reached the qualifying age for state pension credit`
- `Under section 4(1)(c), am I in Great Britain`
- `Under section 4(1), do I meet the basic conditions`
- `Under section 3(1), am I entitled to universal credit`
- `Under section 8(1), what is the amount of my award for the period`

**Part 1 Chapter 2 -- Claimant responsibilities**

- `Under section 14(5), have I accepted my claimant commitment`
- `Under section 19(6), am I the responsible carer for my child`
- `Under section 13(3), which group of claimants am I in`
- `Under section 19(1), may the Secretary of State impose a work-related requirement on me`
- `Under section 20(2), may the Secretary of State impose this requirement on me`
- `Under section 21(2), may the Secretary of State impose this requirement on me`
- `Under section 22(2), must the Secretary of State impose this requirement on me`
- `Under section 22(3), may the Secretary of State impose this requirement on me`
- `Under section 24(4), is notice of the requirement in the manner the Secretary of State may determine`
- `Under section 24(5)(b), may the Secretary of State impose another requirement on me on that day`
- `Under section 26(2), is my failure sanctionable under section 26`
- `Under section 26(6)(b), does the period of my reduction not exceed three years`
- `Under section 27(2), is my failure sanctionable under section 27`
- `Under section 27(5)(b), does the fixed period not exceed 26 weeks`
- `Under section 28(1), may a hardship payment be made to me`
- `Under section 29(1), may this person exercise the functions of the Secretary of State under sections 13 to 25`

**Part 1 Chapter 3 -- Supplementary and general**

- `Under section 33(1), has my old benefit been abolished`
- `Under section 37(1), do I have limited capability for work on the Act's own test`
- `Under section 37(2), do I have limited capability for work-related activity on the Act's own test`
- `Under section 39(1), are the other person and I a couple`
- `Under section 39(3), are the other person and I a couple once the regulations are applied`
- `Under section 40, is this person a child`

**Schedules 1 and 2 -- supplementary powers, and the amendments that bring in universal credit**

- `Under schedule 1 paragraph 4(5), does our joint capital and income include my separate capital and income`
- `Under schedule 1 paragraph 6(3), is the amount paid by means of the voucher permitted`
- `Under schedule 1 paragraph 7, am I treated as not falling within section 19, 20 or 21`
- `Under schedule 1 paragraph 8(a), am I treated as having had a good reason`
- `Under schedule 2 (section 159D(2) of the Social Security Administration Act 1992), what amount of universal credit is payable to me on the day`
- `Under schedule 2 (section 160C(2) of the Social Security Administration Act 1992), is my increased amount payable from the day without any further decision`
- `Under schedule 2 (Schedules 2 and 3 to the Social Security Act 1998), does an appeal lie against this decision`
- `Under schedule 2 (section 4(1A) of the State Pension Credit Act 2002), am I entitled to state pension credit`
- `Under schedule 2 (section 6A(1) of the Social Security Fraud Act 2001), is this benefit a disqualifying benefit`
- `Under schedule 2, does this host provision now include universal credit`

**Schedules 5 and 6 -- working-age benefits together, and moving to universal credit**

- `Under schedule 5 paragraph 1(1), is this benefit a relevant benefit`
- `Under schedule 5 paragraph 1(3), is this reduction a sanction`
- `Under schedule 5 paragraph 2(1), what amount of the relevant benefit is payable to me`
- `Under schedule 5 paragraph 4, may regulations under section 28 be made in relation to me`
- `Under schedule 6 paragraph 1(1), may the regulations include this provision`
- `Under schedule 6 paragraph 1(2), is my old benefit an existing benefit`
- `Under schedule 6 paragraph 1(3), is this day the appointed day`
- `Under schedule 6 paragraph 5(4), is this reduction a sanction`
- `Under schedule 6 paragraph 5(4), is this benefit a relevant benefit`

(48 questions)

Layer-2 finding.
The question for s 39(3)(c) (household) first took a yes/no, which cannot say "the regulations treat the two as not members of the same household"; the case failed and I did not edit the expected value.
I added the three-way type `s 39(3) what the regulations say about our household` instead.


## What the text turns out to say (numbered findings)

1. **s 26(3) refers to something s 19(3) is not.**
   s 26(3) (line 291) speaks of "a claimant falling within section 19 by virtue of subsection (3) of that section", but s 19(3) (lines 215-218) is a note on what regulations under s 19(2)(d) may refer to, not a ground for falling within s 19.
   Taken as a plain fact the caller states (fork F-26(3)).
2. **The four groups overlap as written.**
   s 19(2) and s 20(1) each say only "falls within this section if"; s 21(1) and s 22(1) exclude the earlier groups.
   A claimant within both s 19 and s 20 is told by s 19(1) that no requirement may be imposed and by s 20(2) that an interview requirement may.
   Resolved only by the order in `s 13(3) the group the claimant falls into` (fork F-groups).
3. **Schedule 5 and Schedule 6 define "relevant benefit", "work-related requirement" and "sanction" differently.**
   "Relevant benefit" is jobseeker's allowance and employment and support allowance in Schedule 5 para 1(1), and also income support in Schedule 6 para 5(4).
   "Sanction" is a reduction under s 26 or 27, JSA 6J or 6K, WRA2007 11J in Schedule 5 para 1(3) (lines 3059-3062), and under s 26 or 27, JSA 19, 19A or 19B, WRA2007 11, 12 or 13, SSAA 2A, 2AA or 2D in Schedule 6 para 5(4) (lines 3163-3167).
   Each definition is limited by its own opening words ("In this Schedule", "In this paragraph"), so I encoded each over the core's `Provision that reduces an award` and kept them apart by name; they are not the same list and a caller must not assume one.
4. **Schedule 2 amends other Acts, and their consequences are not in the sources.**
   The encoding answers, for each host provision, "does this amendment put universal credit in it" (list membership, with the host provision's own words "except in prescribed circumstances" and "only in prescribed circumstances" kept as inputs); it does not claim what the host Act then does.
   The one place the amending text itself speaks to appeals is SSA1998: the inserted paragraphs sit under the host headings "(decisions against which no appeal lies)" (Schedule 2) and "(decisions against which an appeal lies)" (Schedule 3), and the answer is read from those headings (listed under Marginal readings).
5. **Five places show only a line of dots.**
   s 10(1A), s 12(2)(a), s 21(5), s 39(2) and the Schedule 2 paragraph at line 2697 are `repealed or blank in this text`; nothing is guessed about what stood there.
   In s 10(4) a single word is replaced by dots and the sentence stands as printed, so it is encoded (`encoded` row at line 96).
6. **"13 weeks" is `WITHIN 90`, not `WITHIN 91`.**
   s 24(5)(b) bars another requirement for a period of 13 weeks (91 days).
   `WITHIN n` includes time n and the first day is time 0, so the last day of the period is time 90; I first wrote `WITHIN 91`, and the `#TRACE` runs showed that admits time 91 (the 92nd day), so the rule was off by one.
   Measured outcomes, identical on the stable and main builds: another requirement imposed at time 50 or at time 90 is a breach; at time 91 it is not (FULFILLED); waiting to 90 leaves the rule open, waiting to 91 fulfils it.
7. **s 8(1) has no floor.**
   The award is "the balance of" the maximum amount "less" the deductions, and nothing in lines 70-83 stops it going below zero (fork F-8).
8. **Schedule paragraph numbers are not printed.**
   The raw text prints a cross-heading per paragraph or group but no number.
   For Schedules 1, 5 and 6 I derived the numbers by counting cross-headings; the count agrees with the Act's own references: s 43(3)(l) ("paragraph 4 of Schedule 1", calculation of capital and income), s 43(3)(m) ("paragraph 1(1) of Schedule 6", with "paragraphs 4, 5 and 6 of that Schedule"), and Schedule 5 para 4's reference to paragraphs 2(3)(b) and 3(b).
   Schedule 2 has one cross-heading per host Act, so I derived no paragraph numbers and labelled each function `sch 2 <host Act short name> <host provision>`.
9. **s 13(1) fixes no time.**
   "claimants must comply" has no period of its own; the time comes from the requirement imposed (ss 15 to 18, 23).
   The regulative rule therefore has no `WITHIN`: waiting never breaches it, and the `#TRACE` shows the rule printed back, still open.
   The same holds for s 19(1) (a prohibition with no period) and s 22(2) (a duty with no period).
10. **"Ceases to have effect" does not say what happens to the permitted requirement.**
    s 20(3) and s 21(4) say that "any other work-related requirement previously applying" ceases to have effect; they are silent on a work-focused interview requirement (s 20) or a work preparation or work-focused interview requirement (s 21) that was already in force, so `s 20(3)` and `s 21(4)` answer `NOTHING` for those requirements and `JUST FALSE` ("ceases") for any other.
11. **Seat: the entitlement question is always `NOTHING` today.**
    The financial conditions of s 5 turn on a prescribed capital limit and a prescribed minimum, and s 4(2) lets regulations except a person from any basic condition, so no set of answers makes `Under section 3(1)` a yes or a no (reading a result, above).
12. **Seat: a yes/no could not say what s 39(3)(c) allows.**
    The household question needed three answers (see the seat section); the failing case was a finding about my input design, not about the Act.

## What the text does not answer

The text points outside itself, so the answer is `NOTHING` or an input, for: the capital limit and the minimum of the financial conditions (s 5); the standard allowance and the child, housing and other amounts (ss 9 to 12); the length of an assessment period and shorter periods (s 7); the percentages and manner of the earned and unearned income deductions (s 8(3)); the description of a claimant in s 19(2)(d), s 20(1)(b), s 21(1)(b); the tests for limited capability (s 37, by regulations); "domestic violence" and the prescribed period of s 24(6); the amount and period of every sanction (ss 26 and 27) and what ends or suspends one; hardship payments, their conditions and whether they are recoverable (s 28(2)(f)); what "receiving education" means and when a person is treated as in Great Britain or as having accepted a commitment (s 4(5)-(7)); "good reason" (Schedule 1 para 8); who is responsible for a child (Schedule 1 para 5); the appointed day (seam 10); every Schedule 6 transitional provision; what the host provisions of Schedule 2 then do; and whether an appeal lies for a decision that this Act did not add to the 1998 Act's lists.

## Test method and its limits

- Expected values were decided from the text and written beside each assertion before running; no expected value was changed to match output.
  One test failed during the work (a Schedule 1 case where I had expected `JUST FALSE` and the text, with an unknown right to reside, gives `NOTHING`) and was corrected from the text; another showed the s 29(1) answer for the Secretary of State went beyond the words (finding in Marginal readings).
- **Scripted expansion.** The per-constructor assertion lists for Schedule 2, Schedules 5 and 6, and the seat cases were generated by a small script from tables I wrote by hand; the expected value for each category was decided by hand from the text, the script only repeated the assertion over the members.
  A reader should check the categories, not each of the hundreds of lines.
  The script is in my scratch folder and is not shipped.
- **Positive control.** On a scratch copy of `wra1-cases-seat.l4` I flipped one expected value (`JUST TRUE` to `JUST FALSE` on the first case) and ran it; the run reported `assertion failed` for that case and `assertion satisfied` for the other 198, so a failing case is visible.
  The scratch copy was deleted.
- **`#TRACE` outcomes** are printed and not asserted (the stable binary cannot assert them); each regulative rule has a decision-function twin that is asserted, and the printed outcomes of the 11 traces were read: 4 FULFILLED, 3 BREACH, 4 still open.
  `check.sh` cannot see a trace outcome; I compared the stable and main outputs of `wra1-tests-ch2.l4` by hand: they differ only in the `Code:` field of the assertion diagnostics (`<none>` on stable, `eval/assertion-passed` on main).
- **Each case file** has assertions written equal to assertions satisfied: 19, 171, 335, 103, 48, 116, 110 and 199 (counted with `grep -c '^#ASSERT'`, against the satisfied column of `check.sh`).

## What the stable binary does not accept

These were measured on 1.6.98 (and the first three re-measured on 2026-11-04 on both builds).

- **A `#TRACE` outcome cannot be asserted.**
  The stable binary prints the outcome (FULFILLED, BREACH, or the rule still owed) and has no assertion form for it, so each duty has a decision-function twin (for example `s 13(1) the claimant must comply with the work-related requirement`) that is asserted.
- **Constructor patterns bind positionally.**
  `WHEN `a single claimant` person THEN` binds the field by position, whatever the variable is called (re-measured: a pattern variable named differently from the field compiles).
- **`NOT (x) AND y` parses as `NOT ((x) AND y)`** (re-measured: `NOT (TRUE) AND FALSE` evaluates to `TRUE` on both builds).
  Every NOT in the files is parenthesised as a whole.
- **`Day r's d` does not parse as `Day (r's d)`; it is read as `(Day r)'s d`** and fails to type-check (re-measured: an error at that expression only).
  The files write `Day (r's d)`.
- A same-indent `AND` or `OR` draws a layout warning from the linter; the files indent the second operand.
- The TRACE step spelling that parses is `(WAITUNTIL n)` in parentheses.
- The first `l4 run` of a file can print `Info | updateFileDiagnostics published different from new diagnostics` before the diagnostics; it is not a diagnostic of the file and does not recur.
- A single capital letter (`A`, `B`) is not usable as a constructor name: it is read as the article (re-measured).
- `REFUSE`, `#ASSERT REFUSED`, `YMD`, `TYPICALLY`, `SET OF` and a section `GIVEN` are not used anywhere (checked by grep).
  `BECAUSE` appears only in `LEST BREACH BY ... BECAUSE` (the four regulative rules).

Tooling, not the binary: `srcrefs.py` rejects a quote line that is only dots ("quotation has no text"), so my build script drops such lines and the `@ref` locator spans the gap; in strict mode the `@ref` must equal the quoted range exactly; macOS `sed -i` needs a suffix, so I edited with perl or python.


## What check.sh prints

Run on 4 November 2026 from the deposit directory as `L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh`, with `JL4_LIBRARY_PATH` unset, after the sources were rebuilt into the deposit.
The stable binary is `1.6.98 (main, 7689b0d, 2026-10-19)`; the main build it was compared with is `1.6.108 (main, 2ae7c9b, 2026-11-02)`.
The target is `main`: every module has the same four counts on both builds.
No assertion is expected to fail (`expected_failed` is empty), and none does.
The exit status was 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wra-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
wra1-cases-seat.l4                             0       199       0        0         0 |      0       199       0        0  same
wra1-ch1-entitlement.l4                        0         0       0        0         0 |      0         0       0        0  same
wra1-ch2-responsibilities.l4                   0         0       0        0         0 |      0         0       0        0  same
wra1-ch3-general.l4                            0         0       0        0         0 |      0         0       0        0  same
wra1-sch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra1-sch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra1-sch5-6.l4                                 0         0       0        0         0 |      0         0       0        0  same
wra1-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra1-tests-ch1.l4                              0       171       0        0         0 |      0       171       0        0  same
wra1-tests-ch2.l4                              0       335       0        0         0 |      0       335       0        0  same
wra1-tests-ch3.l4                              0       103       0        0         0 |      0       103       0        0  same
wra1-tests-sch1.l4                             0        48       0        0         0 |      0        48       0        0  same
wra1-tests-sch2.l4                             0       116       0        0         0 |      0       116       0        0  same
wra1-tests-sch5-6.l4                           0       110       0        0         0 |      0       110       0        0  same
wra1-tests-three-valued.l4                     0        19       0        0         0 |      0        19       0        0  same
wra1-three-valued.l4                           0         0       0        0         0 |      0         0       0        0  same
TOTAL (18 modules)                             0      1101       0        0           |      0      1101       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**The baseline it replaced:** the keel's run printed `TOTAL (3 modules)  0 errors, 38 satisfied, 0 failed, 0 refused`, from `wra-core-tests.l4` alone.
Now: 18 modules, 1,101 satisfied (902 in the seven layer-1 test files and 199 in the seat cases), 0 errors, 0 failed, 0 refused, on both builds.
The modules with zeros are the ones that hold no directive (the layer-1 modules, the seat, the keel's core and definitions); they print `Check succeeded.` on both builds.

`l4 run` printed no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` for any of the 16 wra1 files, and `l4 check` printed no "follows code on its line" or "end of the file" notice (each file ends `Check succeeded.`).

The source quotations and `@ref` locators, `python3 -I srcrefs.py check --refs` and `--strict ../../../inputs/ukpga-2012-5.txt wra1-*.l4`:

```
srcrefs check: 799 src: lines, 175 runs, 187 locators, 0 problems
```

(the same line in both modes).

Other checks I ran:

- `coverage.py check`: every non-blank line of the three ranges is in exactly one row, 0 problems.
- `audit.py`: 189 branches that answer `FALSE` or `NOTHING`, 0 without a kind comment.
- `make_jural.py`: every coverage row that is not a heading is under exactly one jural row.
- Every L4 name in the Coverage and Jural tables was looked up as `` `name` `` in the deposit files: 0 missing.

What these numbers do not show: that a domain expert agrees with any reading (every reading is "assumed, not ruled"); that `#TRACE` outcomes are right (`check.sh` cannot see them; I read the printed outcomes of the 11 traces and compared the two builds by hand); that the expected values are right (they are mine, from the text, and a scripted expansion repeats a category's value over its members); that the Schedule 2 host Acts do what the list-membership answers imply (they are not among the sources); or that the cross-part seams are wired correctly (only the lead can test that).

## peeked

I opened nothing in a forbidden place.
I grepped one file outside `inputs/` and my own folders, once, for the spelling of `#TRACE`: `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md`, the skill the brief names.
I did not read any other directory under the runs directory, anything under `~/.claude/`, or any existing encoding.
