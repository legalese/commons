# Social Security Benefits Up-rating Order 2026 (S.I. 2026/148): the L4 encoding `legalese-sonnet-5.5`

The source is `uksi-2026-148.txt`, a plain-text rendering, made by a converter script, of the version of the Order dated 2026-03-05 on legislation.gov.uk (the text as made; the converter's own caveat is that tables are rendered as `| cell | cell |` rows and that explanatory notes are omitted).
It is not the official text, and nothing in this folder is claimed to be verified against the official text.
`src:N` is line N of that file.

The Order is an up-rating order.
It states new figures for the benefits and pensions of 2026-27, almost all by amending figures in other instruments (the Contributions and Benefits Act 1992, the Income Support Regulations, the Housing Benefit Regulations and the rest named in article 2), and it fixes the dates from which the new figures apply.
Those other instruments are not among the inputs and are not encoded.
So layer 1 encodes what the Order itself says: every figure it states, as a value cited to its lines with the conditions its own rows and columns attach, and every date it fixes.
Where the Order leaves the person's category to another instrument (whether paragraph 13(1)(a) is met, whether the person is over pensionable age, the sum they get now) the category is a plain yes-or-no, number or date input named for the fact.
Most seat questions are therefore rate lookups: of the 131 seat questions, 114 return a figure the Order prints (chosen by facts the person states), 10 compute a percentage of a sum the person gives (nine apply the Order's 3.8 per cent, or 0.8 per cent, increase; one takes 30 per cent for Schedule 1 Part V item 10(c)), and 7 answer a date, extent, name, classification or revocation question.

### What is in the folder

| files | what |
|---|---|
| `uro-nouns` | the nouns and enumerations the text needs (a pair of old and new sum, the territories, the changes article 7 dates, the Schedule 4 sums article 3 names, the positions relative to pensionable age) and the `YMD` shim |
| `uro-part1-intro` | the title block (the date the Order was made), article 1 (extent, the fifteen commencement heads, the universal credit override, which changes article 7 dates) and article 2 (the short names) |
| `uro-part2-arts-3-to-6`, `uro-part2-art7-effect-dates`, `uro-part2-arts-8-to-19` | articles 3 to 19 |
| `uro-schedule1-contributions-act-rates` | Schedule 1 (Schedule 4 to the Contributions and Benefits Act as amended) |
| `uro-part3-income-support`, `uro-part3-housing-benefit` | articles 20 to 24 and Schedules 2 to 7 |
| `uro-part4-jsa` | articles 25 to 28 and Schedules 8 to 10 |
| `uro-part5-pension-credit`, `uro-part6-esa`, `uro-part7-universal-credit`, `uro-part8-revocation` | articles 29 to 34 and Schedules 11 to 13 |
| `uro-tests-*` (nine files) | layer-1 tests, one file per module group, expected values written by hand from the text with the source line beside them |
| `uro-seat`, `uro-cases-seat` | layer 2: the seat's questions and at least one case for each |

### How the files were made

The layer-1 modules were generated from template files by throwaway scripts that read the text file.
The scripts quote source lines mechanically (`-- src:N | ...`), read each "for X substitute Y" and "remains unchanged" figure out of the text line it cites, and lay out the repeated tables (the six non-dependant deduction tables are one template expanded six times).
The scripts are not part of this folder; they sit in a scratch directory, and the generated `.l4` files are the deposit.
`uro-tests-non-dependant-deductions.l4` checks that the six tables equal each other and equal the fifteen pairs of figures printed at src:196-214.
`uro-tests-part4-jsa.l4` and `uro-tests-non-dependant-deductions.l4` were laid out with formatting scripts from hand-chosen values so that positions in long argument lists cannot slip.
`uro-seat.l4` and `uro-cases-seat.l4` were laid out from one hand-written question table by a script (the one place the syntax of `@export` and `@desc` is spelled); every question wording, input description, case and expected value in that table was written by hand.
The commencement dates are data: each is a defined value with an `@ref`, and the dates that depend on the beneficiary's own benefit week or assessment period are inputs.

## Seat

The seat is a person who receives, or may claim, a UK social security benefit or pension that the Order up-rates (the State Pension, Pension Credit, Jobseeker's Allowance, Employment and Support Allowance, Income Support, Housing Benefit, Universal Credit, the benefits of Schedule 4 to the Contributions and Benefits Act 1992 and the others the Order names), asking what the weekly rate or amount is for them, from what date, and whether the Order reaches where they live.
Commons rules (2026-10-18) that every encoding is written from the seat of the individual to whom the law is applied, never the regulator's; the brief for this text names the seat in the words above.
The Order is made by the Secretary of State with the Treasury's consent and addresses nobody in particular; it amends figures in other instruments, so the only reader for whom it decides anything is the person who is paid, or assessed, at those figures.
There is no seat of an official: the Secretary of State's reviews, the laying of the draft and the Treasury's consent are the inert preamble row, and the dating articles (1 and 7) are asked from the beneficiary's side ("on what date does this come into force for me?").
The questions are phrased as that person asks them, and the facts are ones that person can state: age, whether they are in a couple, which condition of a parent regulation they meet, the first day of their first benefit week, the sum they get now.

Departures from the defaults ruled on 2026-10-18, recorded here and not fixed:

- The parent instruments' own rules are not encoded, because they are not among the inputs. A question the Order cannot answer by itself (whether the person meets the condition in a paragraph of a parent instrument) is asked as a fact, named for that fact.
- One case is one claim for one benefit. A person who claims several benefits asks the questions of each.
- The seat does not tell a person whether they qualify for the benefit at all; it tells them the figure the Order gives for the position they describe.
- Where the Order prints rows only for some kinds of claimant (Schedule 11 prints only the single claimant; Schedule 6 does not print rows (1)(a), (2)(a) and (3)), no question is asked for the rows the text does not print (fork F-07).
- The seat layer declares one enumeration of its own (`a benefit whose non-dependant deductions the Order changes`) to choose among the six identical tables of non-dependant deductions; it is thin dispatch and states no rule.
- Schedule 8 (3) asks for twenty-three facts, eleven about each member of the couple and whether they are married or civil partners; the two members are built as records in the question's WHERE and the layer-1 rule is called, so the rule is not restated.

The questions, in the order of the text except that the one question on the six identical tables of non-dependant deductions (articles 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7)) comes after article 24 (each question's `@desc` for every input is in `uro-seat.l4`):


**The Order: where and when it applies to me, and what its short names mean (articles 1 and 2)**

| cite | question | returns |
|---|---|---|
| art 1(2) | Does this provision of the Order extend to where I live? | BOOLEAN |
| art 1(3) and (4) | On what date does this article of the Order come into force for me? | MAYBE DATE |
| art 1(5) | Does the change in my sum take effect on the date article 7 specifies? | BOOLEAN |
| art 2 | What does this short name in the Order stand for? | STRING |

**Part 2: pensions, benefits and statutory payments (articles 3 to 19 and Schedule 1)**

*Schedule 4 to the Contributions and Benefits Act (article 3)*

| cite | question | returns |
|---|---|---|
| art 3 | What does article 3 do to this sum in Schedule 4 to the Contributions and Benefits Act? | what art 3 does to a sum in Schedule 4 |

*Retirement pension and related sums (articles 4 to 6)*

| cite | question | returns |
|---|---|---|
| art 4(1) | What is my retirement allowance sum after the increase of 3.8 per cent? | NUMBER |
| art 4(2) | What is the sum in section 44(4) of the Contributions and Benefits Act after the Order? | NUMBER |
| art 4(3) | What is my pension sum after the increase of 3.8 per cent? | MAYBE NUMBER |
| art 4(4)(a) | What is my shared additional pension after the increase of 3.8 per cent? | NUMBER |
| art 4(4)(b) | What is my increase under paragraph 2 of Schedule 5A after the increase of 3.8 per cent? | NUMBER |
| art 5 | What is my guaranteed minimum increase after the Order? | MAYBE NUMBER |
| art 6(1) | What is the full rate of the state pension after the Order? | NUMBER |
| art 6(2) | What is my section 17 increase to the state pension after the increase of 3.8 per cent? | NUMBER |
| art 6(3) | What is my state pension amount after the increase of 3.8 per cent? | MAYBE NUMBER |

*Dates on which the changes take effect (article 7)*

| cite | question | returns |
|---|---|---|
| art 7 | On what date does the change in my benefit take effect? | MAYBE DATE |

*Statutory payments (articles 8 to 10)*

| cite | question | returns |
|---|---|---|
| arts 8 to 10 | What is the weekly rate of my statutory payment after the Order? | NUMBER |

*Graduated retirement benefit and Category C and maximum additional pensions (articles 11 to 13)*

| cite | question | returns |
|---|---|---|
| art 11(1) | What is the sum of graduated retirement benefit in pence after the Order? | NUMBER |
| art 11(2) to (4) | What is my graduated retirement sum after the increase of 3.8 per cent? | MAYBE NUMBER |
| art 12 | What is the Category C retirement pension for widows after the Order? | NUMBER |
| art 13 | What is the maximum additional pension for survivors after the Order? | NUMBER |

*Disability and incapacity benefits (articles 14 to 17)*

| cite | question | returns |
|---|---|---|
| art 14 | What is my weekly rate of disability living allowance after the Order? | NUMBER |
| art 15 | What is my weekly rate of personal independence payment after the Order? | NUMBER |
| art 16 | What is my age addition to incapacity benefit after the Order? | NUMBER |
| art 17 | What is my transitional invalidity allowance sum after the Order? | NUMBER |

*Bereavement benefits (articles 18 and 19)*

| cite | question | returns |
|---|---|---|
| art 18 | What is my weekly rate of bereavement benefit after the Order? | NUMBER |
| art 19 | What is my bereavement support payment sum after the Order? | NUMBER |

*Schedule 1: the weekly rates in Schedule 4 to the Contributions and Benefits Act*

| cite | question | returns |
|---|---|---|
| Sch 1 Part I | What is my weekly rate of a contributory benefit in Part I of Schedule 4? | NUMBER |
| Sch 1 Part III | What is my weekly rate of a non-contributory benefit in Part III of Schedule 4? | NUMBER |
| Sch 1 Part IV | What is my increase for an adult dependant after the Order? | MAYBE NUMBER |
| Sch 1 Part V item 1 | What is my weekly disablement pension for my degree of disablement? | MAYBE NUMBER |
| Sch 1 Part V item 2 | What is the most I can be paid for constant attendance with my disablement pension? | NUMBER |
| Sch 1 Part V item 6 | What is my increase of unemployability supplement? | NUMBER |
| Sch 1 Part V item 10(c) | What is my widow's pension at the lower permanent rate? | NUMBER |
| Sch 1 Part V | What is my single-figure industrial injuries rate? | NUMBER |

**Part 3: income support and housing benefit (articles 20 to 24 and Schedules 2 to 7)**

*Income support: sums (articles 20 to 22)*

| cite | question | returns |
|---|---|---|
| art 20(2) | What is the sum of 3,000 in the income support rules after the Order? | NUMBER |
| art 20(3)(b) | What is the sum in paragraph 2(1) of Part I of Schedule 2 to the Income Support Regulations after the Order? | NUMBER |
| art 20(4) | What is my family premium in income support after the Order? | NUMBER |
| art 21 | What is my special transitional addition to income support after the increase of 3.8 per cent? | NUMBER |
| art 22 | What is the relevant sum for income support in a trade dispute after the Order? | NUMBER |

*Income support: personal allowances (Schedule 2 to the Order)*

| cite | question | returns |
|---|---|---|
| Sch 2 (1) | What is my personal allowance in income support as a single claimant? | MAYBE NUMBER |
| Sch 2 (2) | What is my personal allowance in income support as a lone parent? | MAYBE NUMBER |
| Sch 2 (3) | What is our personal allowance in income support as a couple? | MAYBE NUMBER |

*Income support: premiums (Schedule 3 to the Order)*

| cite | question | returns |
|---|---|---|
| Sch 3 (2) | What is my pensioner premium in income support where paragraph 9 applies to me? | MAYBE NUMBER |
| Sch 3 (2A) | What is my pensioner premium in income support where paragraph 9A applies to me? | MAYBE NUMBER |
| Sch 3 (3) | What is my higher pensioner premium in income support? | MAYBE NUMBER |
| Sch 3 (4) | What is my disability premium in income support? | NUMBER |
| Sch 3 (5) | What is my severe disability premium in income support? | NUMBER |
| Sch 3 (6) | What is my disabled child premium in income support? | NUMBER |
| Sch 3 (7) | What is my carer premium in income support? | NUMBER |
| Sch 3 (8)(a) | What is my enhanced disability premium in income support for children and young persons? | NUMBER |
| Sch 3 (8)(b) | What is my enhanced disability premium in income support if I am neither a child or young person nor in a couple? | MAYBE NUMBER |
| Sch 3 (8)(c) | What is my enhanced disability premium in income support if I am in a couple? | MAYBE NUMBER |

*Housing benefit (article 23)*

| cite | question | returns |
|---|---|---|
| art 23(2) | What is the sum in regulation 27(3) of the Housing Benefit Regulations after the Order? | NUMBER |
| art 23(4) | What is my ineligible service charge in housing benefit after the Order? | NUMBER |
| art 23(5) | What is my fuel charge figure in housing benefit after the Order? | NUMBER |
| art 23(6)(b) | What is the sum in paragraph 2(1) of Part 1 of Schedule 3 to the Housing Benefit Regulations after the Order? | NUMBER |
| art 23(7) | What is my family premium in housing benefit after the Order? | MAYBE NUMBER |
| art 23(9) | What is my component amount in housing benefit after the Order? | MAYBE NUMBER |
| art 23(10) | What is the earnings disregard in housing benefit after the Order? | NUMBER |
| art 23(11) | What is the disregard of income other than earnings in housing benefit after the Order? | NUMBER |

*Housing benefit: personal allowances and premiums (Schedules 4 and 5 to the Order)*

| cite | question | returns |
|---|---|---|
| Sch 4 (1) | What is my personal allowance in housing benefit as a single claimant? | NUMBER |
| Sch 4 (2) | What is my personal allowance in housing benefit as a lone parent? | NUMBER |
| Sch 4 (3) | What is our personal allowance in housing benefit as a couple? | NUMBER |
| Sch 5 (5) | What is my disability premium in housing benefit? | NUMBER |
| Sch 5 (6) | What is my severe disability premium in housing benefit? | NUMBER |
| Sch 5 (7) | What is my disabled child premium in housing benefit? | NUMBER |
| Sch 5 (8) | What is my carer premium in housing benefit? | NUMBER |
| Sch 5 (9)(a) | What is my enhanced disability premium in housing benefit for children and young persons? | NUMBER |
| Sch 5 (9)(b) | What is my enhanced disability premium in housing benefit if I am neither a child or young person nor in a couple? | MAYBE NUMBER |
| Sch 5 (9)(c) | What is my enhanced disability premium in housing benefit if I am in a couple? | MAYBE NUMBER |

*Housing benefit for persons over the qualifying age for state pension credit (article 24)*

| cite | question | returns |
|---|---|---|
| SPC) Regulations after the Order (art 24(2) | What is the sum in regulation 30(3) of the Housing Benefit? | NUMBER |
| SPC) after the Order (art 24(4) | What is my ineligible service charge in housing benefit? | NUMBER |
| SPC) after the Order (art 24(5) | What is my fuel charge figure in housing benefit? | NUMBER |
| SPC) Regulations after the Order (art 24(6)(b) | What is the sum in paragraph 2(1) of Part 1 of Schedule 3 to the Housing Benefit? | NUMBER |
| SPC) after the Order (art 24(7) | What is my family premium in housing benefit? | MAYBE NUMBER |
| SPC) after the Order (art 24(9) | What is the earnings disregard in housing benefit? | NUMBER |
| SPC) after the Order (art 24(10) | What is the disregard of income other than earnings in housing benefit? | NUMBER |

*Housing benefit (SPC): personal allowances and premiums (Schedules 6 and 7 to the Order)*

| cite | question | returns |
|---|---|---|
| SPC) as a single claimant or lone parent (Sch 6 (1) | What is my personal allowance in housing benefit? | MAYBE NUMBER |
| SPC) as a couple (Sch 6 (2) | What is our personal allowance in housing benefit? | MAYBE NUMBER |
| SPC) in a polygamous marriage (Sch 6 (4) and (5) | What is my personal allowance in housing benefit? | MAYBE NUMBER |
| SPC) (Sch 7 (1) | What is my severe disability premium in housing benefit? | NUMBER |
| SPC) (Sch 7 (2) | What is my enhanced disability premium in housing benefit? | NUMBER |
| SPC) (Sch 7 (3) | What is my disabled child premium in housing benefit? | NUMBER |
| SPC) (Sch 7 (4) | What is my carer premium in housing benefit? | NUMBER |

*Non-dependant deductions (articles 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7))*

| cite | question | returns |
|---|---|---|
| arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7) | What is my non-dependant deduction after the Order? | NUMBER |

**Part 4: jobseeker's allowance (articles 25 to 28 and Schedules 8 to 10)**

| cite | question | returns |
|---|---|---|
| art 25 | What is my weekly amount of contribution-based jobseeker's allowance after the Order? | NUMBER |
| art 26(2) | What is the sum of 3,000 in the jobseeker's allowance rules after the Order? | NUMBER |
| art 26(3)(b) | What is the sum in paragraph 2(1) of Part 1 of Schedule 1 to the JSA Regulations 1996 after the Order? | NUMBER |
| art 26(4) | What is my family premium in jobseeker's allowance after the Order? | NUMBER |
| art 27 | What is the prescribed sum for a trade dispute in jobseeker's allowance after the Order? | NUMBER |
| art 28 | What is my weekly amount of jobseeker's allowance under the 2013 Regulations after the Order? | NUMBER |

*Jobseeker's allowance: personal allowances (Schedule 8 to the Order)*

| cite | question | returns |
|---|---|---|
| Sch 8 (1) | What is my personal allowance in jobseeker's allowance as a single claimant? | MAYBE NUMBER |
| Sch 8 (2) | What is my personal allowance in jobseeker's allowance as a lone parent? | MAYBE NUMBER |
| Sch 8 (3) | What is our personal allowance in jobseeker's allowance as a couple? | MAYBE NUMBER |

*Jobseeker's allowance: premiums (Schedules 9 and 10 to the Order)*

| cite | question | returns |
|---|---|---|
| qualifying age for state pension credit) (Sch 9 (2) | What is my pensioner premium in jobseeker's allowance? | NUMBER |
| Sch 9 (3) | What is my pensioner premium in jobseeker's allowance where my partner is 75 or over? | MAYBE NUMBER |
| Sch 9 (4) | What is my higher pensioner premium in jobseeker's allowance? | NUMBER |
| Sch 9 (5) | What is my disability premium in jobseeker's allowance? | NUMBER |
| Sch 9 (6) | What is my severe disability premium in jobseeker's allowance? | NUMBER |
| Sch 9 (7) | What is my disabled child premium in jobseeker's allowance? | NUMBER |
| Sch 9 (8) | What is my carer premium in jobseeker's allowance? | NUMBER |
| Sch 9 (9)(a) | What is my enhanced disability premium in jobseeker's allowance for children and young persons? | NUMBER |
| Sch 9 (9)(b) | What is my enhanced disability premium in jobseeker's allowance if I am neither a child or young person nor in a couple? | MAYBE NUMBER |
| Sch 9 (9)(c) | What is my enhanced disability premium in jobseeker's allowance if I am in a couple? | MAYBE NUMBER |
| Sch 10 (1) | What is our pensioner premium in jobseeker's allowance as a joint-claim couple? | MAYBE NUMBER |
| Sch 10 (2) | What is our higher pensioner premium in jobseeker's allowance as a joint-claim couple? | MAYBE NUMBER |
| Sch 10 (3) | What is our disability premium in jobseeker's allowance as a joint-claim couple? | MAYBE NUMBER |
| Sch 10 (4) | What is our severe disability premium in jobseeker's allowance as a joint-claim couple? | MAYBE NUMBER |
| Sch 10 (5) | What is our carer premium in jobseeker's allowance as a joint-claim couple? | NUMBER |
| Sch 10 (6) | What is our enhanced disability premium in jobseeker's allowance as a joint-claim couple? | MAYBE NUMBER |

**Part 5: state pension credit (article 29)**

| cite | question | returns |
|---|---|---|
| art 29(2) | What is my guarantee credit sum in state pension credit after the Order? | NUMBER |
| art 29(3) | What is my savings credit sum in state pension credit after the Order? | NUMBER |
| art 29(5) and (6) | What is my additional amount for a child in state pension credit after the Order? | NUMBER |
| art 29(7) | What is my sum in state pension credit for a polygamous marriage after the Order? | NUMBER |

**Part 6: employment and support allowance (articles 30 and 31 and Schedules 11 and 12)**

| cite | question | returns |
|---|---|---|
| art 30(2) and (3) | What is my prescribed amount in employment and support allowance as a single claimant? | NUMBER |
| art 30(4) and (5) | What is my pensioner premium in employment and support allowance? | MAYBE NUMBER |
| art 30(4) and (5) | What is my carer premium in employment and support allowance? | MAYBE NUMBER |
| art 30(6)(b) | What is my work-related activity component for a contributory allowance after the Order? | MAYBE NUMBER |
| art 30(6)(c) | What is my support component for a contributory allowance after the Order? | NUMBER |
| art 31(1) | What is my prescribed amount in employment and support allowance under the 2013 Regulations after the Order? | NUMBER |
| art 31(2) | What is my regulation 62(2) amount after the Order in a case within paragraphs 2 to 7? | MAYBE NUMBER |
| art 31(3) | What is my modified regulation 62 amount after the Order? | MAYBE NUMBER |

**Part 7: universal credit (articles 32 and 33 and Schedule 13)**

| cite | question | returns |
|---|---|---|
| art 32(1) | What is my work allowance sum in universal credit after the Order? | NUMBER |
| art 32(3) | What is my housing cost contribution in universal credit after the Order? | NUMBER |
| art 33(a) | What is my sum in the severe disability premium protection in universal credit after the Order? | NUMBER |
| art 33(b) | What is my additional amount in the transitional protection in universal credit after the Order? | NUMBER |
| Sch 13 | What is the child element in universal credit for my child? | MAYBE NUMBER |
| Sch 13 | What is the additional amount in universal credit for my disabled child? | NUMBER |
| Sch 13 | What is the carer element in universal credit? | NUMBER |
| Sch 13 | What is the most I can get for childcare costs in universal credit? | MAYBE NUMBER |

**Part 8: revocation (article 34)**

| cite | question | returns |
|---|---|---|
| art 34 | Has the Social Security Benefits Up-rating Order 2025 been revoked on this date? | BOOLEAN |

## Jural relations

The Order creates no claim, duty, power or liability of its own.
It fixes the amount of those that the parent instruments create, and the dates from which the new amounts apply.
The Order names only one party to those relations, the Secretary of State (the preamble; the carer's allowance arrangement in article 7(4)(b) and (5)(a)(i)); every other payer or decision-maker is a creature of a parent instrument and is written below as "payer under the parent instrument".
Each row is a group of provisions that fix the amount of one kind of relation; the L4 rule is named by the label that opens its name (the module is in the coverage table).

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | the relation whose amount or date it fixes | L4 rule |
|---|---|---|---|---|
| art 3; Sch 1 Parts I, III, IV, V | the beneficiary: claim | payer under the parent instrument (the Contributions and Benefits Act) | the weekly rate of a contributory or non-contributory benefit, an increase for a dependant, an industrial injuries benefit | `art 3`, `Sch 1 Part I`, `Sch 1 Part III`, `Sch 1 Part IV`, `Sch 1 Part V item 1` to `item 12` |
| arts 4, 5, 6, 11, 12, 13 | the pensioner or survivor: claim | payer under the parent instrument | the amount of a retirement pension, additional pension, guaranteed minimum increase, state pension, graduated retirement benefit, Category C pension or maximum additional pension | `art 4(1)` to `art 4(4)(b)`, `art 5`, `art 6(1)` to `art 6(3)`, `art 11(1)` to `art 11(4)`, `art 12`, `art 13` |
| arts 8 to 10 | the employee or parent: claim | payer under the parent regulations (not named in the Order) | the weekly rate of statutory sick, maternity, paternity, adoption, shared parental, parental bereavement and neonatal care pay | `art 8`, `art 9`, `art 10(1)(a)` to `art 10(4)` |
| arts 14 to 19 | the disabled, incapacitated or bereaved claimant: claim | payer under the parent instrument | the weekly rate of disability living allowance, personal independence payment, age addition, transitional invalidity allowance, bereavement benefits and bereavement support payment | `art 14`, `art 15`, `art 16`, `art 17`, `art 18`, `art 19` |
| arts 20, 21, 22; Sch 2, 3 | the income support claimant: claim to benefit assessed against the applicable amount | payer under the parent instrument | the personal allowances and premiums that make up the applicable amount, the special transitional addition, the trade-dispute sum | `art 20(2)` to `art 20(4)`, `art 21`, `art 22`, `Sch 2 (1)` to `(3)`, `Sch 3 (2)` to `(8)(c)` |
| arts 23, 24; Sch 4 to 7 | the housing benefit claimant: claim to benefit assessed against the applicable amount | payer or authority under the parent regulations | the same, for housing benefit and for persons over the qualifying age for state pension credit | `art 23(2)` to `art 24(10)`, `Sch 4 (1)` to `Sch 7 (4)` |
| arts 25 to 28; Sch 8 to 10 | the jobseeker: claim | payer under the parent instrument | the age-related amounts of contribution-based jobseeker's allowance, the applicable amount, the trade-dispute sum, the 2013 amounts | `art 25` to `art 28`, `Sch 8 (1)` to `Sch 10 (6)` |
| art 29 | the pension credit claimant: claim | payer under the parent instrument | the guarantee credit, savings credit, additional amounts for a child and polygamous marriage sums | `art 29(2)` to `art 29(7)` |
| arts 30, 31; Sch 11, 12 | the employment and support allowance claimant: claim | payer under the parent instrument | the prescribed amount, the pensioner and carer premiums, the components | `art 30(2) and (3)`, `art 30(4) and (5)`, `art 30(6)(b)`, `art 30(6)(c)`, `art 31(1)` to `art 31(3)` |
| arts 32, 33; Sch 13 | the universal credit claimant: claim | payer under the parent instrument | the work-allowance sums, housing cost contributions, the elements, the transitional protections | `art 32(1)`, `art 32(3)`, `art 33(a)`, `art 33(b)`, `Sch 13` |
| arts 20(6), 23(3), 24(3), 26(7), 29(4), 30(7) | the decision-maker under the parent instrument: power to deduct | the claimant: liability to a deduction of the stated sum | the non-dependant deductions (the Order's own words) | `art 20(6)(b)` to `art 30(7)(e)(ii)` |
| arts 1(3) to (5), 7 | the beneficiary: claim to the new amount from the stated date | payer under the parent instrument: duty to pay the new amount from that date | the date from which the new amount applies | `art 1(3)(a)` to `art 1(5)`, `art 7` |
| art 22, art 27 | none | none | a trade dispute: the Order fixes the sum (53.00) and creates no relation; what the sum does to a claimant is in the parent instrument, which the Order does not reproduce | `art 22`, `art 27` |
| art 1(1), preamble, signature | none | none | citation, recitals, signature and consent | none |
| art 1(2) | none | none | where the Order applies (extent) | `art 1(2)` |
| art 2, art 6(4) | none | none | definitions of the short names and of "old state pension" | `art 2`, `art 6(3)(a)` |
| arts 20(1), 23(1), 24(1), 26(1), 29(1), 30(1) | none | none | reading conventions for numbered references | none |
| arts 20(5), 23(8), 24(8), 26(5), 26(6), 32(2) | none (they point to the Schedule that carries the figures) | none | pointers to Schedules 3, 5, 7, 9, 10 and 13 | the Schedule rules |
| art 34 | none | none | revocation of the Social Security Benefits Up-rating Order 2025 | `art 34` |
| Part and Schedule headings | none | none | titles | none |

## Coverage table

The text has 34 articles, 13 Schedules, 8 Parts and 14 sub-Part headings inside Schedules; the table has 247 rows.
There is one row per article, and one row per paragraph or sub-paragraph of an article where the paragraphs differ in disposition or in the rule they state (articles 1 to 7 and the multi-part articles are by paragraph; an article whose paragraphs are one rule is one row).
There is one row per Schedule title, and one row per table or paragraph of each Schedule.
The heading line of each article, and the sub-Part headings of Schedules 1 to 3, are in the first row of their article or table; the sub-Part headings of Schedules 4 to 13 are in the Schedule's heading row; the 8 Part titles and the 13 Schedule titles are their own rows.
Dispositions: 154 `encoded`, 62 `fork` (encoded with the reading named in the fork register), 31 `inert` (each with its reason from the permitted list), 0 `repealed or blank in this text`.
The text contains no repealed or blank provision: a search for "repeal", "STRUCK", runs of dots and "not in force" found nothing.
`where` lists the layer-1 rules whose `@ref` cover the row's own lines, by module; `seat:` names the seat questions that reach the row's rules, directly or through another rule.
The table is generated from the deposit by a script, so a rule renamed in a module is renamed here.


| provision | source lines | disposition | where | note |
|---|---|---|---|---|
| title block | src:1-5 | encoded | `uro-part1-intro`: `title block` | layer 1 only: the date the Order was made (2nd March 2026) is carried as a defined value; no beneficiary asks it. |
| preamble | src:6-10 | inert | - | machinery: the recitals. They record that the Secretary of State made the reviews required by sections 150, 151A and 150A of the Social Security Administration Act 1992, that a draft was laid and approved, that the Treasury consented, and which powers are exercised. They are the making of the Order, not a rule about any beneficiary. |
| Part 1 heading | src:11 | inert | - | pure citation or title: the heading of Part 1 (Introduction); it names the Part and states nothing the person could ask. |
| art 1(1) | src:12-13 | inert | - | pure citation: the short title, 'the Social Security Benefits Up-rating Order 2026'. The title is carried as text in the title block rule. |
| art 1(2) lead-in | src:14 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(a) | src:15 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(b)(i) | src:16-17 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(b)(ii) | src:16,18 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(b)(iii) | src:16,19 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(c) | src:20 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(d) | src:21 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(2)(e) | src:22 | encoded | `uro-part1-intro`: `art 1(2)` | seat: art 1(2). |
| art 1(3) lead-in | src:23 | encoded | `uro-part1-intro`: `art 1(3) and (4)` | seat: art 1(3) and (4). |
| art 1(3)(a) | src:24 | encoded | `uro-part1-intro`: `art 1(3)(a)`, `art 1(3) and (4)` | seat: art 1(3) and (4). |
| art 1(3)(b)(i) | src:25-26 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(b)` | F-03: 'subject to paragraph (9)' read as displacing (7) only for the article 25(b) earnings-limit sum. seat: art 1(3) and (4). |
| art 1(3)(b)(ii) | src:25,27 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(b)` | seat: art 1(3) and (4). |
| art 1(3)(c) | src:28 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(c)` | seat: art 1(3) and (4). |
| art 1(3)(d) | src:29 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(d)` | seat: art 1(3) and (4). |
| art 1(3)(e) | src:30 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(e)` | seat: art 1(3) and (4). |
| art 1(3)(f) | src:31 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(f)` | seat: art 1(3) and (4). |
| art 1(3)(g) | src:32 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(g)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(h) | src:33 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(h)` | seat: art 1(3) and (4). |
| art 1(3)(i) | src:34 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(i)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(j) | src:35 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(j)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(k) | src:36 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(k)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(l) | src:37 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(l)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(m) | src:38 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(m)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(n) | src:39 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(n)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(3)(o) | src:40 | encoded | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(3)(o)` | seat: art 1(3) and (4), art 34. |
| art 1(4) | src:41 | fork | `uro-part1-intro`: `art 1(3) and (4)`, `art 1(4)` | F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 1(3) and (4). |
| art 1(5) | src:42-45 | encoded | `uro-part1-intro`: `art 1(5)` | seat: art 1(5). |
| art 2 | src:46-61 | encoded | `uro-part1-intro`: `art 2` | seat: art 2. |
| Part 2 heading | src:62 | inert | - | pure citation or title: the heading of Part 2 (Social security benefits and pensions); it names the Part and states nothing the person could ask. |
| art 3(1) | src:63-64 | encoded | `uro-part2-arts-3-to-6`: `art 3` | seat: art 3. |
| art 3(2)(a) | src:65-66 | fork | `uro-part2-arts-3-to-6`: `art 3` | F-11: the Schedule rows matching the carve-outs of article 3(2) are identified by inference. seat: art 3. |
| art 3(2)(b) | src:65,67 | fork | `uro-part2-arts-3-to-6`: `art 3` | F-11: the Schedule rows matching the carve-outs of article 3(2) are identified by inference. seat: art 3. |
| art 4(1) | src:68-69 | fork | `uro-part2-arts-3-to-6`: `art 4(1)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(1). |
| art 4(2)(a) | src:70-71 | encoded | `uro-part2-arts-3-to-6`: `art 4(2)(a)`, `art 4(2)` | seat: art 4(2). |
| art 4(2)(b) | src:70,72 | encoded | `uro-part2-arts-3-to-6`: `art 4(2)`, `art 4(2)(b)` | seat: art 4(2). |
| art 4(3)(a) | src:73-74,78 | fork | `uro-part2-arts-3-to-6`: `art 4(3)(a)`, `art 4(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(3). |
| art 4(3)(b) | src:73,75,78 | fork | `uro-part2-arts-3-to-6`: `art 4(3)(b)`, `art 4(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(3). |
| art 4(3)(c) | src:73,76,78 | fork | `uro-part2-arts-3-to-6`: `art 4(3)(c)`, `art 4(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(3). |
| art 4(3)(d) | src:73,77-78 | fork | `uro-part2-arts-3-to-6`: `art 4(3)(d)`, `art 4(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(3). |
| art 4(4)(a) | src:79-80,82 | fork | `uro-part2-arts-3-to-6`: `art 4(4)(a)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(4)(a), art 4(4)(b). |
| art 4(4)(b) | src:79,81-82 | fork | `uro-part2-arts-3-to-6`: `art 4(4)(b)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 4(4)(a), art 4(4)(b). |
| art 5(a) | src:83-85 | fork | `uro-part2-arts-3-to-6`: `art 5(a)`, `art 5` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 5. |
| art 5(b) | src:83,86 | fork | `uro-part2-arts-3-to-6`: `art 5`, `art 5(b)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 5. |
| art 6(1) | src:87-88 | encoded | `uro-part2-arts-3-to-6`: `art 6(1)` | seat: art 6(1). |
| art 6(2) | src:89 | fork | `uro-part2-arts-3-to-6`: `art 6(2)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 6(2). |
| art 6(3)(a) | src:90-91,95 | fork | `uro-part2-arts-3-to-6`: `art 6(3)`, `art 6(3)(a)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 6(3). |
| art 6(3)(b) | src:90,92,95 | fork | `uro-part2-arts-3-to-6`: `art 6(3)(b)`, `art 6(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 6(3). |
| art 6(3)(c) | src:90,93,95 | fork | `uro-part2-arts-3-to-6`: `art 6(3)(c)`, `art 6(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 6(3). |
| art 6(3)(d) | src:90,94-95 | fork | `uro-part2-arts-3-to-6`: `art 6(3)(d)`, `art 6(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 6(3). |
| art 6(4) | src:96 | encoded | `uro-part2-arts-3-to-6`: `art 6(3)(a)` | a definition of 'old state pension' by reference to section 22 of the Pensions Act 2014 (outside the text); recorded on the article 6(3)(a) rule, whose amount is an input. seat: art 6(3). |
| art 7(1) | src:97-98 | fork | `uro-part2-art7-effect-dates`: `art 7` | F-03: 'subject to paragraph (9)' read as displacing (7) only for the article 25(b) earnings-limit sum. seat: art 7. |
| art 7(2) | src:99 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(2)` | seat: art 7. |
| art 7(3) | src:100 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(3)` | seat: art 7. |
| art 7(4) | src:101-104 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(4)(a)`, `art 7(4)(b)`, `art 7(4)(b), (5)(a)(i)` | seat: art 7. |
| art 7(5) | src:105-115 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(5)(a)(i)`, `art 7(5)` | seat: art 7. |
| art 7(6) | src:116 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(6)` | seat: art 7. |
| art 7(7) | src:117 | fork | `uro-part2-art7-effect-dates`: `art 7`, `art 7(7)` | F-03: 'subject to paragraph (9)' read as displacing (7) only for the article 25(b) earnings-limit sum. seat: art 7. |
| art 7(8) | src:118 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(8)` | seat: art 7. |
| art 7(9) | src:119-122 | fork | `uro-part2-art7-effect-dates`: `art 7`, `art 7(9)` | F-03: 'subject to paragraph (9)' read as displacing (7) only for the article 25(b) earnings-limit sum; F-06: a first benefit week or assessment period beginning before 6 April 2026 is outside the text: NOTHING. seat: art 7. |
| art 7(10) | src:123 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(10)` | seat: art 7. |
| art 7(11) | src:124 | encoded | `uro-part2-art7-effect-dates`: `art 7`, `art 7(11)` | seat: art 7. |
| art 8 | src:125-126 | encoded | `uro-part2-arts-8-to-19`: `art 8`, `arts 8 to 10` | seat: arts 8 to 10. |
| art 9 | src:127-128 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 9` | seat: arts 8 to 10. |
| art 10(1)(a) | src:129-131 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 10(1)(a)` | seat: arts 8 to 10. |
| art 10(1)(b) | src:129-130,132 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 10(1)(b)` | seat: arts 8 to 10. |
| art 10(2) | src:133 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 10(2)` | seat: arts 8 to 10. |
| art 10(3) | src:134 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 10(3)` | seat: arts 8 to 10. |
| art 10(4) | src:135 | encoded | `uro-part2-arts-8-to-19`: `arts 8 to 10`, `art 10(4)` | seat: arts 8 to 10. |
| art 11(1) | src:136-139 | encoded | `uro-part2-arts-8-to-19`: `art 11(1)`, `art 11(2) to (4)` | the Order states both the increase and the result (17.83 pence, 18.51 pence); the pair is a value. seat: art 11(1), art 11(2) to (4). |
| art 11(2) | src:140 | fork | `uro-part2-arts-8-to-19`: `art 11(2) to (4)`, `art 11(2)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 11(2) to (4). |
| art 11(3) | src:141 | fork | `uro-part2-arts-8-to-19`: `art 11(2) to (4)`, `art 11(3)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 11(2) to (4). |
| art 11(4) | src:142 | fork | `uro-part2-arts-8-to-19`: `art 11(2) to (4)`, `art 11(4)` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 11(2) to (4). |
| art 12 | src:143-144 | encoded | `uro-part2-arts-8-to-19`: `art 12` | seat: art 12. |
| art 13 | src:145-146 | encoded | `uro-part2-arts-8-to-19`: `art 13` | seat: art 13. |
| art 14 | src:147-153 | encoded | `uro-part2-arts-8-to-19`: `art 14(a)`, `art 14`, `art 14(b)`, and 3 more | seat: art 14. |
| art 15 | src:154-159 | encoded | `uro-part2-arts-8-to-19`: `art 15(a)`, `art 15`, `art 15(b)`, and 2 more | seat: art 15. |
| art 16(1) | src:160-163 | encoded | `uro-part2-arts-8-to-19`: `art 16(1)(a)`, `art 16(1)`, `art 16`, `art 16(1)(b)` | seat: art 16. |
| art 16(2) | src:164 | encoded | `uro-part2-arts-8-to-19`: `art 16`, `art 16(2)` | seat: art 16. |
| art 17(1) | src:165-169 | encoded | `uro-part2-arts-8-to-19`: `art 17(1)(a)`, `art 17(1)`, `art 17`, and 2 more | seat: art 17. |
| art 17(2) | src:170 | encoded | `uro-part2-arts-8-to-19`: `art 17`, `art 17(2)` | seat: art 17. |
| art 18 | src:171-174 | encoded | `uro-part2-arts-8-to-19`: `art 18(a)`, `art 18`, `art 18(b)` | seat: art 18. |
| art 19 | src:175-180 | encoded | `uro-part2-arts-8-to-19`: `art 19(a)`, `art 19`, `art 19(b)`, and 2 more | all four sums 'remain unchanged': carried as pairs with equal fields (F-08). seat: art 19. |
| Part 3 heading | src:181 | inert | - | pure citation or title: the heading of Part 3 (Income support and housing benefit); it names the Part and states nothing the person could ask. |
| art 20(1) | src:182-183 | inert | - | pure citation: a reading convention. A numbered regulation or Schedule in article 20 means that of the Income Support Regulations unless stated otherwise. It states no figure or condition; the rule names spell the instrument out. |
| art 20(2) | src:184-187 | encoded | `uro-part3-income-support`: `art 20(2)` | seat: art 20(2). |
| art 20(3)(a) | src:188-189 | encoded | `uro-part3-income-support`: `Sch 2 (1)` (also cited as art 20(3)(a)) | points to Schedule 2: the personal allowances of paragraph 1 are encoded under Sch 2; this sub-paragraph states none of its own. seat: art 20(3)(b), Sch 2 (1). |
| art 20(3)(b) | src:188,190 | encoded | `uro-part3-income-support`: `art 20(3)(b)` | seat: art 20(3)(b). |
| art 20(4) | src:191-193 | encoded | `uro-part3-income-support`: `art 20(4)(a)`, `art 20(4)`, `art 20(4)(b)` | seat: art 20(4). |
| art 20(5) | src:194 | encoded | `uro-part3-income-support`: `Sch 3 (2)` | points to Schedule 3: the figures are encoded under Sch 3; this paragraph states none of its own. seat: Sch 3 (2). |
| art 20(6) | src:195-214 | encoded | `uro-part3-income-support`: `art 20(6)(a)`, `art 20(6)`, `art 20(6)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 21 | src:215-216 | fork | `uro-part3-income-support`: `art 21` | F-01: rounding of a percentage increase is not stated; the exact product is returned. seat: art 21. |
| art 22 | src:217-218 | encoded | `uro-part3-income-support`: `art 22` | seat: art 22. |
| art 23(1) | src:219-220 | inert | - | pure citation: a reading convention. A numbered regulation or Schedule in article 23 means that of the Housing Benefit Regulations unless stated otherwise. It states no figure or condition. |
| art 23(2) | src:221-223 | encoded | `uro-part3-housing-benefit`: `art 23(2)(a)`, `art 23(2)`, `art 23(2)(b)` | seat: art 23(2). |
| art 23(3) | src:224-243 | encoded | `uro-part3-housing-benefit`: `art 23(3)(a)`, `art 23(3)`, `art 23(3)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 23(4) | src:244-249 | encoded | `uro-part3-housing-benefit`: `art 23(4)(a)`, `art 23(4)`, `art 23(4)(b)`, and 3 more | seat: art 23(4). |
| art 23(5) | src:250-253 | encoded | `uro-part3-housing-benefit`: `art 23(5)(a)`, `art 23(5)`, `art 23(5)(b)`, `art 23(5)(c)` | seat: art 23(5). |
| art 23(6)(a) | src:254-255 | encoded | `uro-part3-housing-benefit`: `Sch 4 (1)` (also cited as art 23(6)(a)) | points to Schedule 4: the personal allowances of paragraph 1 are encoded under Sch 4; this sub-paragraph states none of its own. seat: art 23(6)(b), Sch 4 (1). |
| art 23(6)(b) | src:254,256 | encoded | `uro-part3-housing-benefit`: `art 23(6)(b)` | seat: art 23(6)(b). |
| art 23(7) | src:257-259 | fork | `uro-part3-housing-benefit`: `art 23(7)(a)`, `art 23(7)`, `art 23(7)(b)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 23(7). |
| art 23(8) | src:260 | encoded | `uro-part3-housing-benefit`: `Sch 5 (5)` | points to Schedule 5: the figures are encoded under Sch 5; this paragraph states none of its own. seat: Sch 5 (5). |
| art 23(9) | src:261-263 | fork | `uro-part3-housing-benefit`: `art 23(9)(a)`, `art 23(9)`, `art 23(9)(b)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 23(9). |
| art 23(10) | src:264 | encoded | `uro-part3-housing-benefit`: `art 23(10)` | seat: art 23(10). |
| art 23(11) | src:265 | encoded | `uro-part3-housing-benefit`: `art 23(11)` | seat: art 23(11). |
| art 24(1) | src:266-267 | inert | - | pure citation: a reading convention. A numbered regulation or Schedule in article 24 means that of the Housing Benefit (SPC) Regulations unless stated otherwise. It states no figure or condition. |
| art 24(2) | src:268-270 | encoded | `uro-part3-housing-benefit`: `art 24(2)(a)`, `art 24(2)`, `art 24(2)(b)` | seat: art 24(2). |
| art 24(3) | src:271-290 | encoded | `uro-part3-housing-benefit`: `art 24(3)(a)`, `art 24(3)`, `art 24(3)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 24(4) | src:291-296 | encoded | `uro-part3-housing-benefit`: `art 24(4)(a)`, `art 24(4)`, `art 24(4)(b)`, and 3 more | seat: art 24(4). |
| art 24(5) | src:297-300 | encoded | `uro-part3-housing-benefit`: `art 24(5)(a)`, `art 24(5)`, `art 24(5)(b)`, `art 24(5)(c)` | seat: art 24(5). |
| art 24(6)(a) | src:301-302 | encoded | `uro-part3-housing-benefit`: `Sch 6 (1)` (also cited as art 24(6)(a)) | points to Schedule 6: the personal allowances of paragraph 1 are encoded under Sch 6; this sub-paragraph states none of its own. seat: art 24(6)(b), Sch 6 (1). |
| art 24(6)(b) | src:301,303 | encoded | `uro-part3-housing-benefit`: `art 24(6)(b)` | seat: art 24(6)(b). |
| art 24(7) | src:304 | fork | `uro-part3-housing-benefit`: `art 24(7)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 24(7). |
| art 24(8) | src:305 | encoded | `uro-part3-housing-benefit`: `Sch 7 (1)` | points to Schedule 7: the figures are encoded under Sch 7; this paragraph states none of its own. seat: Sch 7 (1). |
| art 24(9) | src:306 | encoded | `uro-part3-housing-benefit`: `art 24(9)` | seat: art 24(9). |
| art 24(10) | src:307 | encoded | `uro-part3-housing-benefit`: `art 24(10)` | seat: art 24(10). |
| Part 4 heading | src:308 | inert | - | pure citation or title: the heading of Part 4 (Jobseeker's allowance); it names the Part and states nothing the person could ask. |
| art 25 | src:309-312 | encoded | `uro-part4-jsa`: `art 25(a)`, `art 25`, `art 25(b)` | seat: art 25. |
| art 26(1) | src:313-314 | inert | - | pure citation: a reading convention. A numbered regulation or Schedule in article 26 means that of the JSA Regulations 1996 unless stated otherwise. It states no figure or condition. |
| art 26(2) | src:315-318 | encoded | `uro-part4-jsa`: `art 26(2)` | seat: art 26(2). |
| art 26(3)(a) | src:319-320 | encoded | `uro-part4-jsa`: `Sch 8 (1)` (also cited as art 26(3)(a)) | points to Schedule 8: the personal allowances of paragraph 1 are encoded under Sch 8; this sub-paragraph states none of its own. seat: art 26(3)(b), Sch 8 (1). |
| art 26(3)(b) | src:319,321 | encoded | `uro-part4-jsa`: `art 26(3)(b)` | seat: art 26(3)(b). |
| art 26(4) | src:322-324 | encoded | `uro-part4-jsa`: `art 26(4)(a)`, `art 26(4)`, `art 26(4)(b)` | seat: art 26(4). |
| art 26(5) | src:325 | encoded | `uro-part4-jsa`: `Sch 9 (2)` | points to Schedule 9: the figures are encoded under Sch 9; this paragraph states none of its own. seat: Sch 9 (2). |
| art 26(6) | src:326 | encoded | `uro-part4-jsa`: `Sch 10 (1)` | points to Schedule 10: the figures are encoded under Sch 10; this paragraph states none of its own. seat: Sch 10 (1). |
| art 26(7) | src:327-346 | encoded | `uro-part4-jsa`: `art 26(7)(a)`, `art 26(7)`, `art 26(7)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 27 | src:347-348 | encoded | `uro-part4-jsa`: `art 27` | seat: art 27. |
| art 28 | src:349-352 | encoded | `uro-part4-jsa`: `art 28(a)`, `art 28`, `art 28(b)` | seat: art 28. |
| Part 5 heading | src:353 | inert | - | pure citation or title: the heading of Part 5 (State pension credit); it names the Part and states nothing the person could ask. |
| art 29(1) | src:354-355 | inert | - | pure citation: a reading convention. A numbered regulation or Schedule in article 29 means that of the State Pension Credit Regulations. It states no figure or condition. |
| art 29(2) | src:356-361 | encoded | `uro-part5-pension-credit`: `art 29(2)(a)`, `art 29(2)`, `art 29(2)(b)`, and 3 more | seat: art 29(2). |
| art 29(3) | src:362 | encoded | `uro-part5-pension-credit`: `art 29(3)` | seat: art 29(3). |
| art 29(4) | src:363-382 | encoded | `uro-part5-pension-credit`: `art 29(4)(a)`, `art 29(4)`, `art 29(4)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 29(5) | src:383-387 | encoded | `uro-part5-pension-credit`: `art 29(5)(a)`, `art 29(5) and (6)`, `art 29(5)(b)(i)`, `art 29(5)(b)(ii)` | seat: art 29(5) and (6). |
| art 29(6) | src:388 | encoded | `uro-part5-pension-credit`: `art 29(5) and (6)`, `art 29(6)` | seat: art 29(5) and (6). |
| art 29(7) | src:389-391 | encoded | `uro-part5-pension-credit`: `art 29(7)(a)`, `art 29(7)`, `art 29(7)(b)` | seat: art 29(7). |
| Part 6 heading | src:392 | inert | - | pure citation or title: the heading of Part 6 (Employment and support allowance); it names the Part and states nothing the person could ask. |
| art 30(1) | src:393-394 | inert | - | pure citation: a reading convention. A numbered Schedule in article 30 means that of the ESA Regulations 2008 unless stated otherwise. It states no figure or condition. |
| art 30(2) | src:395 | encoded | `uro-part6-esa`: `art 30(2) and (3)` | points to Schedule 11 paragraph 1; the single-claimant rows are encoded there. seat: art 30(2) and (3). |
| art 30(3) | src:396 | fork | `uro-part6-esa`: `art 30(2) and (3)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. points to Schedule 11 paragraph 2 for the cases within paragraphs 2 to 7 of Schedule 2 to the 2017 Regulations. seat: art 30(2) and (3). |
| art 30(4) | src:397 | fork | `uro-part6-esa`: `art 30(4) and (5)` | F-14: the two unlabelled tables are taken as paragraphs 1 and 2 of Schedule 12. seat: art 30(4) and (5). |
| art 30(5) | src:398 | fork | `uro-part6-esa`: `art 30(4) and (5)` | F-14: the two unlabelled tables are taken as paragraphs 1 and 2 of Schedule 12; F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 30(4) and (5). |
| art 30(6)(a) | src:399-400 | inert | - | amendment of another instrument: it inserts the words 'for the purposes of an income-related allowance' after 'component' in paragraph 12 of Part 4 of Schedule 4 to the ESA Regulations 2008, in the cases within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017. It is a wording change and states no figure, so there is nothing to compute; paragraph (b) and (c) carry the figures that follow it. |
| art 30(6)(b) | src:399,401-402 | fork | `uro-part6-esa`: `art 30(6)(b)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 30(6)(b). |
| art 30(6)(c) | src:399,403-404 | encoded | `uro-part6-esa`: `art 30(6)(c)` | seat: art 30(6)(c). |
| art 30(7) | src:405-424 | encoded | `uro-part6-esa`: `art 30(7)(a)`, `art 30(7)`, `art 30(7)(b)`, and 13 more | seat: arts 20(6), 23(3), 24(3), 26(7), 29(4) and 30(7). |
| art 31(1) | src:425-429 | encoded | `uro-part6-esa`: `art 31(1)(a)`, `art 31(1)`, `art 31(1)(b)`, `art 31(1)(c)` | seat: art 31(1). |
| art 31(2) | src:430-432 | fork | `uro-part6-esa`: `art 31(2)(a)`, `art 31(2)`, `art 31(2)(b)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 31(2). |
| art 31(3) | src:433-435 | fork | `uro-part6-esa`: `art 31(3)(a)`, `art 31(3)`, `art 31(3)(b)` | F-15: an amendment 'as it has effect in' a kind of case: the case is an input and a person outside it gets NOTHING. seat: art 31(3). |
| Part 7 heading | src:436 | inert | - | pure citation or title: the heading of Part 7 (Universal credit); it names the Part and states nothing the person could ask. |
| art 32(1) | src:437-440 | encoded | `uro-part7-universal-credit`: `art 32(1)(a)`, `art 32(1)`, `art 32(1)(b)` | seat: art 32(1). |
| art 32(2) | src:441 | encoded | `uro-part7-universal-credit`: `Sch 13` | points to Schedule 13: the figures are encoded under Sch 13; this paragraph states none of its own. seat: Sch 13. |
| art 32(3) | src:442 | encoded | `uro-part7-universal-credit`: `art 32(3)` | seat: art 32(3). |
| art 33 | src:443-454 | encoded | `uro-part7-universal-credit`: `art 33(a)(i)`, `art 33(a)`, `art 33(a)(ii)`, and 7 more | seat: art 33(a), art 33(b). |
| Part 8 heading | src:455 | inert | - | pure citation or title: the heading of Part 8 (Revocation); it names the Part and states nothing the person could ask. |
| art 34 | src:456-457 | encoded | `uro-part8-revocation`: `art 34` | seat: art 34. |
| signature and consent | src:458-459 | inert | - | machinery: the signature by authority of the Secretary of State for Work and Pensions and the words 'We consent,' of the Treasury. They complete the making of the Order. |
| Sch 1 heading | src:460 | inert | - | pure citation or title: the title of Schedule 1, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 1 Part I item 2 | src:461-464 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part I` | seat: Sch 1 Part I. |
| Sch 1 Part I item 2A | src:465 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part I` | seat: Sch 1 Part I. |
| Sch 1 Part I item 5 | src:466 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part I` | seat: Sch 1 Part I. |
| Sch 1 Part III item 1 | src:467-471 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | seat: Sch 1 Part III. |
| Sch 1 Part III item 2 | src:472 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | seat: Sch 1 Part III. |
| Sch 1 Part III item 3 | src:473-476 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | seat: Sch 1 Part III. |
| Sch 1 Part III item 4 | src:477 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | seat: Sch 1 Part III. |
| Sch 1 Part III item 7 | src:478 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | seat: Sch 1 Part III. |
| Sch 1 Part III item 8 | src:479 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part III` | F-11: the Schedule rows matching the carve-outs of article 3(2) are identified by inference. seat: Sch 1 Part III. |
| Sch 1 Part IV item 1A | src:480-485 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part IV` | F-04: a beneficiary exactly at pensionable age is in neither 'under' nor 'over': NOTHING. seat: Sch 1 Part IV. |
| Sch 1 Part IV item 2 | src:486 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part IV` | seat: Sch 1 Part IV. |
| Sch 1 Part IV item 8 | src:487 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part IV` | seat: Sch 1 Part IV. |
| Sch 1 Part V item 1 | src:488-503 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V item 1`, `Sch 1 Part V` | F-07: rows the text does not print are not invented: NOTHING. seat: Sch 1 Part V item 1, Sch 1 Part V. |
| Sch 1 Part V item 2 | src:504-505 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 2(a)`, `Sch 1 Part V item 2`, `Sch 1 Part V item 2(b)` | seat: Sch 1 Part V item 2, Sch 1 Part V. |
| Sch 1 Part V item 3 | src:506 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 3` | seat: Sch 1 Part V. |
| Sch 1 Part V item 4 | src:507 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 4` | seat: Sch 1 Part V. |
| Sch 1 Part V item 5 | src:508 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 5` | seat: Sch 1 Part V. |
| Sch 1 Part V item 6 | src:509-513 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 6` | seat: Sch 1 Part V item 6, Sch 1 Part V. |
| Sch 1 Part V item 7 | src:514 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 7` | F-11: the Schedule rows matching the carve-outs of article 3(2) are identified by inference. seat: Sch 1 Part V. |
| Sch 1 Part V item 8 | src:515 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 8` | seat: Sch 1 Part V. |
| Sch 1 Part V item 9 | src:516 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 9` | seat: Sch 1 Part V. |
| Sch 1 Part V item 10 | src:517-518 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 10(b)`, `Sch 1 Part V item 10(c)` | F-05: which of the two section 44(4) sums is 'the first sum' is not stated: an input; F-07: rows the text does not print are not invented: NOTHING. seat: Sch 1 Part V item 10(c), Sch 1 Part V. |
| Sch 1 Part V item 11 | src:519 | encoded | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 11` | seat: Sch 1 Part V. |
| Sch 1 Part V item 12 | src:520 | fork | `uro-schedule1-contributions-act-rates`: `Sch 1 Part V`, `Sch 1 Part V item 12` | F-11: the Schedule rows matching the carve-outs of article 3(2) are identified by inference. seat: Sch 1 Part V. |
| Sch 2 heading | src:521-522 | inert | - | pure citation or title: the title of Schedule 2, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself; its lines are also quoted by the @ref of the Sch 2 (1) rule. |
| Sch 2 para (1) single claimant | src:523-529 | encoded | `uro-part3-income-support`: `Sch 2 (1)` | seat: Sch 2 (1). |
| Sch 2 para (2) lone parent | src:530-534 | encoded | `uro-part3-income-support`: `Sch 2 (2)` | seat: Sch 2 (2). |
| Sch 2 para (3) couple | src:535-555 | encoded | `uro-part3-income-support`: `Sch 2 (3)` | seat: Sch 2 (3). |
| Sch 3 heading | src:556-557 | inert | - | pure citation or title: the title of Schedule 3, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself; its lines are also quoted by the @ref of the Sch 3 (2) rule. |
| Sch 3 para 15(2), (2A), (3) | src:558-561 | encoded | `uro-part3-income-support`: `Sch 3 (2)`, `Sch 3 (2A)`, `Sch 3 (3)` | seat: Sch 3 (2), Sch 3 (2A), Sch 3 (3). |
| Sch 3 para (4) disability premium | src:562-564 | encoded | `uro-part3-income-support`: `Sch 3 (4)` | seat: Sch 3 (4). |
| Sch 3 para (5) severe disability premium | src:565-569 | encoded | `uro-part3-income-support`: `Sch 3 (5)` | seat: Sch 3 (5). |
| Sch 3 para (6) disabled child premium | src:570 | encoded | `uro-part3-income-support`: `Sch 3 (6)` | seat: Sch 3 (6). |
| Sch 3 para (7) carer premium | src:571 | encoded | `uro-part3-income-support`: `Sch 3 (7)` | seat: Sch 3 (7). |
| Sch 3 para (8) enhanced disability premium | src:572-578 | fork | `uro-part3-income-support`: `Sch 3 (8)(a)`, `Sch 3 (8)(b)`, `Sch 3 (8)(c)` | F-09: the rows are 'in respect of' different persons and the Order does not total them: one rule per row. seat: Sch 3 (8)(a), Sch 3 (8)(b), Sch 3 (8)(c). |
| Sch 4 heading | src:579-581 | inert | - | pure citation or title: the title of Schedule 4, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 4 para (1) single claimant | src:582-585 | fork | `uro-part3-housing-benefit`: `Sch 4 (1)` | F-10: heads listed in parallel: the first printed head that holds wins. seat: Sch 4 (1). |
| Sch 4 para (2) lone parent | src:586-589 | fork | `uro-part3-housing-benefit`: `Sch 4 (2)` | F-10: heads listed in parallel: the first printed head that holds wins. seat: Sch 4 (2). |
| Sch 4 para (3) couple | src:590-593 | fork | `uro-part3-housing-benefit`: `Sch 4 (3)` | F-10: heads listed in parallel: the first printed head that holds wins. seat: Sch 4 (3). |
| Sch 5 heading | src:594-596 | inert | - | pure citation or title: the title of Schedule 5, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 5 para 20(5) disability premium | src:597-599 | encoded | `uro-part3-housing-benefit`: `Sch 5 (5)` | seat: Sch 5 (5). |
| Sch 5 para (6) severe disability premium | src:600-604 | encoded | `uro-part3-housing-benefit`: `Sch 5 (6)` | seat: Sch 5 (6). |
| Sch 5 para (7) disabled child premium | src:605 | encoded | `uro-part3-housing-benefit`: `Sch 5 (7)` | seat: Sch 5 (7). |
| Sch 5 para (8) carer premium | src:606 | encoded | `uro-part3-housing-benefit`: `Sch 5 (8)` | seat: Sch 5 (8). |
| Sch 5 para (9) enhanced disability premium | src:607-613 | fork | `uro-part3-housing-benefit`: `Sch 5 (9)(a)`, `Sch 5 (9)(b)`, `Sch 5 (9)(c)` | F-09: the rows are 'in respect of' different persons and the Order does not total them: one rule per row. seat: Sch 5 (9)(a), Sch 5 (9)(b), Sch 5 (9)(c). |
| Sch 6 heading | src:614-616 | inert | - | pure citation or title: the title of Schedule 6, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 6 para (1)(b),(c) | src:617-619 | fork | `uro-part3-housing-benefit`: `Sch 6 (1)` | F-07: rows the text does not print are not invented: NOTHING; F-16: 'has attained pensionable age before 1st April 2021' read as a test on the date the age was attained. seat: Sch 6 (1). |
| Sch 6 para (2)(b),(c) | src:620-622 | fork | `uro-part3-housing-benefit`: `Sch 6 (2)` | F-07: rows the text does not print are not invented: NOTHING; F-16: 'has attained pensionable age before 1st April 2021' read as a test on the date the age was attained. seat: Sch 6 (2). |
| Sch 6 para (4) | src:623-625 | fork | `uro-part3-housing-benefit`: `Sch 6 (4) and (5)` | F-16: 'has attained pensionable age before 1st April 2021' read as a test on the date the age was attained. seat: Sch 6 (4) and (5). |
| Sch 6 para (5) | src:626-628 | fork | `uro-part3-housing-benefit`: `Sch 6 (4) and (5)` | F-16: 'has attained pensionable age before 1st April 2021' read as a test on the date the age was attained. seat: Sch 6 (4) and (5). |
| Sch 7 heading | src:629-631 | inert | - | pure citation or title: the title of Schedule 7, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 7 para 12(1) severe disability premium | src:632-636 | encoded | `uro-part3-housing-benefit`: `Sch 7 (1)` | seat: Sch 7 (1). |
| Sch 7 para (2) enhanced disability premium | src:637 | encoded | `uro-part3-housing-benefit`: `Sch 7 (2)` | seat: Sch 7 (2). |
| Sch 7 para (3) disabled child premium | src:638 | encoded | `uro-part3-housing-benefit`: `Sch 7 (3)` | seat: Sch 7 (3). |
| Sch 7 para (4) carer premium | src:639 | encoded | `uro-part3-housing-benefit`: `Sch 7 (4)` | seat: Sch 7 (4). |
| Sch 8 heading | src:640-642 | inert | - | pure citation or title: the title of Schedule 8, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 8 para (1) single claimant | src:643-650 | encoded | `uro-part4-jsa`: `Sch 8 (1)` | seat: Sch 8 (1). |
| Sch 8 para (2) lone parent | src:651-657 | encoded | `uro-part4-jsa`: `Sch 8 (2)` | seat: Sch 8 (2). |
| Sch 8 para (3) couple | src:658-692 | fork | `uro-part4-jsa`: `Sch 8 (3)`, `Sch 8 (3)(a)(iii), (vii)`, `Sch 8 (3)(f)`, `Sch 8 (3)(g), (h)` | F-10: heads listed in parallel: the first printed head that holds wins; F-12: '(i) or (ii); and (iii)' read as printed. seat: Sch 8 (3). |
| Sch 9 heading | src:693-695 | inert | - | pure citation or title: the title of Schedule 9, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 9 para 20(2) pensioner premium | src:696-699 | encoded | `uro-part4-jsa`: `Sch 9 (2)` | seat: Sch 9 (2). |
| Sch 9 para (3) pensioner premium partner 75 | src:700 | encoded | `uro-part4-jsa`: `Sch 9 (3)` | seat: Sch 9 (3). |
| Sch 9 para (4) higher pensioner premium | src:701-703 | encoded | `uro-part4-jsa`: `Sch 9 (4)` | seat: Sch 9 (4). |
| Sch 9 para (5) disability premium | src:704-706 | encoded | `uro-part4-jsa`: `Sch 9 (5)` | seat: Sch 9 (5). |
| Sch 9 para (6) severe disability premium | src:707-711 | encoded | `uro-part4-jsa`: `Sch 9 (6)` | seat: Sch 9 (6). |
| Sch 9 para (7) disabled child premium | src:712 | encoded | `uro-part4-jsa`: `Sch 9 (7)` | seat: Sch 9 (7). |
| Sch 9 para (8) carer premium | src:713 | encoded | `uro-part4-jsa`: `Sch 9 (8)` | seat: Sch 9 (8). |
| Sch 9 para (9) enhanced disability premium | src:714-720 | fork | `uro-part4-jsa`: `Sch 9 (9)(a)`, `Sch 9 (9)(b)`, `Sch 9 (9)(c)` | F-09: the rows are 'in respect of' different persons and the Order does not total them: one rule per row. seat: Sch 9 (9)(a), Sch 9 (9)(b), Sch 9 (9)(c). |
| Sch 10 heading | src:721-723 | inert | - | pure citation or title: the title of Schedule 10, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 10 para 20M(1) | src:724 | encoded | `uro-part4-jsa`: `Sch 10 (1)` | seat: Sch 10 (1). |
| Sch 10 para (2) | src:725 | encoded | `uro-part4-jsa`: `Sch 10 (2)` | seat: Sch 10 (2). |
| Sch 10 para (3) | src:726 | encoded | `uro-part4-jsa`: `Sch 10 (3)` | seat: Sch 10 (3). |
| Sch 10 para (4) | src:727-729 | encoded | `uro-part4-jsa`: `Sch 10 (4)` | seat: Sch 10 (4). |
| Sch 10 para (5) | src:730 | encoded | `uro-part4-jsa`: `Sch 10 (5)` | seat: Sch 10 (5). |
| Sch 10 para (6) | src:731 | encoded | `uro-part4-jsa`: `Sch 10 (6)` | seat: Sch 10 (6). |
| Sch 11 heading | src:732 | inert | - | pure citation or title: the title of Schedule 11, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 11 paragraph 1 | src:733-738 | fork | `uro-part6-esa`: `Sch 11 paragraph 1 (1)` | F-07: rows the text does not print are not invented: NOTHING; F-10: heads listed in parallel: the first printed head that holds wins. seat: art 30(2) and (3). |
| Sch 11 paragraph 2 | src:739-744 | fork | `uro-part6-esa`: `Sch 11 paragraph 2 (1)` | F-07: rows the text does not print are not invented: NOTHING; F-10: heads listed in parallel: the first printed head that holds wins. seat: art 30(2) and (3). |
| Sch 12 heading | src:745-746 | inert | - | pure citation or title: the title of Schedule 12, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 12 first table | src:747-755 | fork | `uro-part6-esa`: `Sch 12 paragraph 1 (1)`, `Sch 12 paragraph 1 (3)` | F-13: row (iii) of the first table is read as printed, so the work-related activity component does not matter under paragraph 1; F-14: the two unlabelled tables are taken as paragraphs 1 and 2 of Schedule 12. seat: art 30(4) and (5). |
| Sch 12 second table | src:756-765 | fork | `uro-part6-esa`: `Sch 12 paragraph 2 (1)` | F-14: the two unlabelled tables are taken as paragraphs 1 and 2 of Schedule 12. seat: art 30(4) and (5). |
| Sch 13 heading | src:766 | inert | - | pure citation or title: the title of Schedule 13, which says which provision of which instrument the Schedule sets out as amended; it states no figure itself. |
| Sch 13 child element | src:767-770 | encoded | `uro-part7-universal-credit`: `Sch 13` | seat: Sch 13. |
| Sch 13 disabled child additional amount | src:771-773 | encoded | `uro-part7-universal-credit`: `Sch 13` | seat: Sch 13. |
| Sch 13 carer element | src:774 | encoded | `uro-part7-universal-credit`: `Sch 13` | seat: Sch 13. |
| Sch 13 childcare costs element | src:775-777 | encoded | `uro-part7-universal-credit`: `Sch 13` | seat: Sch 13. |

## Fork register

Where I looked for ambiguity, since "none found" would not be believed.
Dates at which a condition is tested: article 1(3) to (5) and article 7 (F-03, F-06), and "has attained pensionable age before 1st April 2021" in Schedule 6 (F-16).
Cumulative or alternative conditions: the heads of Schedules 2 and 8 (F-10, F-12), the "(i) or (ii); and (iii)" lists of Schedule 8 (3)(g) and (h) (F-12), and the sub-paragraphs of article 1(2)(b).
Overlaps between rules: heads listed in parallel in Schedules 4, 8 and 11 (F-10); the exceptions of article 3(2) against the rows of Schedule 1 (F-11).
Places where the text defers to something not in the inputs are in the next section; the ones that change a reading are F-05 and F-15.
Places where the printed table is silent: F-04, F-07, F-13.
Wording slips in the text are in the findings (finding 15).

Each entry gives where, the readings seen, the one taken, and the text that licenses it.
F-02 and F-08 are findings and a modelling choice that the modules cite by that number; they are not readings between which the text leaves a choice.

**F-01 Rounding of a percentage increase.**
Where: articles 4(1), 4(3), 4(4), 5, 6(2), 6(3), 11(2) to (4), 21.
Readings: (a) the exact product; (b) the product rounded to the nearest penny, half up; (c) the product rounded down.
Taken: (a), the exact product (100 becomes 103.8, 20.50 becomes 21.279).
Text: the Order says "increased by 3.8 per cent" (and "0.8 per cent" in article 5(b)) and never says how to round.
The two places that state both ends fit (b) and not (c): article 11(1) says 17.83 pence increased by 3.8 per cent has effect as 18.51 pence (the product is 18.50754) and article 4(2)(a) substitutes 140.65 for 135.50 (the product is 140.649).
The Order does not say that those two results are the rule, so (a) is returned and the rounding is left to the person.
Asserted in `uro-tests-part2-arts-3-to-7.l4` and `uro-tests-part2-arts-8-to-19.l4`.

**F-02 (finding) The Order's substituted sums are not computed from the percentage.**
Where: article 4(2)(b), article 6(1).
The rules never derive a substituted sum from "3.8 per cent": 176.45 increased by 3.8 per cent is 183.16 to the penny, but article 4(2)(b) substitutes 184.90; 230.25 increased by 3.8 per cent is 239.00 to the penny, but article 6(1) substitutes 241.30.
Both stated figures are about 4.8 per cent above the old ones.
The Order does not say why, and no reading is chosen: the stated figure is the value.
Asserted in `uro-tests-part2-arts-3-to-7.l4`.

**F-03 "Paragraph (7), which is subject to the provisions of paragraph (9)".**
Where: article 7(1), (7), (9); article 1(3)(b)(i); article 1(5)(b).
Readings: (a) paragraph (9) displaces paragraph (7) only for the article 25(b) sum, in so far as it is the adult-dependant earnings limit; (b) paragraph (9) displaces paragraph (7) for every increase for a dependant with incapacity benefit or severe disablement allowance.
Taken: (a).
Text: paragraph (9) speaks only of "the sum specified in article 25(b)" in so far as it is relevant to whether a benefit is increased for an adult dependant whose earnings exceed a specified amount.
Article 1(3)(b)(i) refers to "any increase to which article 7(9)(b) applies", which article 3 does not itself state; it is taken as a yes-or-no input, "the increase is an article 7(9)(b) increase".
Asserted in `uro-tests-part1.l4` and `uro-tests-part2-arts-3-to-7.l4`.

**F-04 "Under" and "over" pensionable age.**
Where: Schedule 1 Part IV item 1A.
Readings: (a) a beneficiary exactly at pensionable age is in neither head and gets no answer; (b) at pensionable age counts as over; (c) it counts as under.
Taken: (a), NOTHING.
Text: the heads read "where the beneficiary is under pensionable age" and "where the beneficiary is over pensionable age" (src:484-485).
Asserted in `uro-tests-schedule1.l4`.

**F-05 "The first sum specified in section 44(4)".**
Where: Schedule 1 Part V item 10(c).
Readings: (a) 140.65; (b) 184.90.
Taken: neither; the sum is an input, so 30 per cent of what the person gives.
Text: article 4(2) substitutes two sums in section 44(4) (140.65 for 135.50 and 184.90 for 176.45) and item 10(c) says "30 per cent of the first sum specified in section 44(4)"; the Order does not say which of its two is the first.
Asserted in `uro-tests-schedule1.l4`.

**F-06 A first benefit week or assessment period that begins before 6 April 2026.**
Where: article 1(3)(g), (i) to (n); article 1(4); article 7(9).
Readings: (a) the date is outside the text and the answer is NOTHING; (b) the Order's date applies from 6 April 2026 whatever the benefit week.
Taken: (a).
Text: the heads say "the first benefit week to commence for that beneficiary on or after 6th April 2026", so a benefit week that begins earlier is not the one the head names; the Order says nothing about what applies to it.
Asserted in `uro-tests-part1.l4`.

**F-07 Rows the text does not print.**
Where: Schedule 1 Part V item 1 (a degree of disablement not in column (1)) and item 10(a); Schedule 6 rows (1)(a), (2)(a), (3); Schedule 11 rows other than "(1) Single claimant".
Readings: (a) the row is not in the text, so no figure and NOTHING; (b) the row is unchanged by the Order and so is whatever the parent instrument says.
Taken: (a).
Text: each Schedule is headed "as amended by this Order" and prints the rows it amends; the Order does not say that an unprinted row is unchanged.
Where there is a rule to ask the question (a degree of disablement not printed) NOTHING is asserted in `uro-tests-schedule1.l4`; for an unprinted row there is no rule, so no case can ask.

**F-08 (modelling choice) A sum that "remains unchanged".**
Where: articles 19, 20(2), 23(2), 23(5), 23(7)(a), 23(10), 23(11), 24(2), 24(5), 24(9), 24(10), 26(2).
The Order states the figure and says it remains unchanged.
The module carries it as a pair of old and new sum with equal fields, so an unchanged sum and a changed sum are asked in the same way.
It is not a reading between which the text leaves a choice.
Asserted in `uro-tests-part2-arts-8-to-19.l4` and `uro-tests-part3-housing-benefit.l4`.

**F-09 The rows of an enhanced disability premium are not totalled.**
Where: Schedule 3 (8), Schedule 5 (9), Schedule 9 (9).
Readings: (a) each row is its own sum "in respect of" its own persons, asked separately; (b) the rows are added for a family that has several kinds of person.
Taken: (a).
Text: each row is "in respect of each child or young person", "in respect of each person who is neither ...", or "where the claimant is a member of a couple ..."; the Order does not say that they add.
Asserted in `uro-tests-part3-income-support.l4`, `uro-tests-part3-housing-benefit.l4` and `uro-tests-part4-jsa.l4`.

**F-10 Heads listed in parallel.**
Where: Schedule 4 (1) to (3), Schedule 8 (3), Schedule 11 paragraphs 1 and 2.
Readings: (a) the first printed head that holds governs; (b) the higher figure governs; (c) no answer where two heads both hold.
Taken: (a).
Text: the heads are listed (a), (b), (c) with no "except where"; a single claimant who is entitled to main phase employment and support allowance and is under 25 (Schedule 4) is in head (a) at 95.55 and head (c) at 75.65, and the Order does not say which governs.
In Schedule 4 and in Schedule 11 the first head is also the higher, so (a) and (b) agree on every case.
In Schedule 8 (3), heads (g) and (h) overlap head (e)(ii) when the under-18 member is treated as responsible for a child; (e) comes first and gives 150.15.
Asserted in `uro-tests-part3-housing-benefit.l4`, `uro-tests-part4-jsa.l4` and `uro-tests-part5-to-8.l4`.

**F-11 The exceptions of article 3(2) against the rows of Schedule 1.**
Where: article 3(2)(a), (b); Schedule 1 Part III item 8, Part V items 7 and 12.
Readings: (a) Schedule 1 prints those rows as the figures with which Schedule 4 has effect, and the encoding returns the printed figure; (b) it computes a before and after for them.
Taken: (a).
Text: article 3(2) excepts "age addition" and the child increases from the sums to be increased, and Schedule 1 still prints a figure for age addition (0.25) and for two Part V rows (11.35 each, "increase under paragraph 4 of Schedule 7" and "allowance in respect of children ... under paragraph 18 of Schedule 7"); which rows are the excepted ones is inferred from their descriptions, and the Order does not say what they were before.
Asserted in `uro-tests-schedule1.l4` and `uro-tests-part2-arts-3-to-7.l4`.

**F-12 "(i) or (ii); and (iii)" in Schedule 8 (3)(g) and (h).**
Where: Schedule 8 (3)(g), (h).
Readings: (a) as printed, (i) and (ii) are alternatives and (iii) is additional; (b) all three apply together ("none of the regulations ...; and not the subject of a direction; and ...").
Taken: (a).
Text: src:686-688 and src:690-692 punctuate "(i) ... ; or (ii) ... ; and (iii)".
Because head (f) is tried before (g) and (h) and covers every under-18 member who is within regulations 59 to 61, within a section 16 direction or meeting the income support requirements, the choice cannot change an answer.
Asserted in `uro-tests-part4-jsa.l4`.

**F-13 Schedule 12 paragraph 1, row (iii), and the work-related activity component.**
Where: Schedule 12 first table; article 30(4).
Readings: (a) row (iii) is read as printed, "is not entitled to the support component", so a claimant entitled to the work-related activity component and not to the support component is within it; (b) the claimant gets no answer because row (i), the work-related activity row, is not printed.
Taken: (a).
Text: the first table prints (a)(ii), (a)(iii), (b)(ii) and (b)(iii) only, and its (iii) says "is not entitled to the support component" (src:751, 754), where the second table's (iii) says "is not entitled to either of those components" (src:761, 765).
Paragraph 1 therefore does not look at the work-related activity component at all; the seat keeps the question because paragraph 2 does.
Asserted in `uro-tests-part5-to-8.l4`.

**F-14 Which unlabelled table is paragraph 1 of Schedule 12.**
Where: Schedule 12; article 30(4) and (5).
Readings: (a) the first table is paragraph 1 and the second is paragraph 2; (b) the reverse.
Taken: (a).
Text: the paragraph markers of Schedule 12 were lost in the conversion (Schedule 11's markers "1" and "2" survive at src:733 and 739).
Article 30(4) sends paragraph 11(1) and (3) of Schedule 4 to paragraph 1 of Schedule 12 and article 30(5) sends paragraph 11(1) alone to paragraph 2; the first table has a carer premium (3) and the second does not.
In a case of article 30(5) the Order therefore sets no carer premium, and the encoding answers NOTHING for it.
Asserted in `uro-tests-part5-to-8.l4` and `uro-cases-seat.l4`.

**F-15 An amendment "as it has effect in" a kind of case.**
Where: articles 23(7), 23(9)(a), 24(7), 30(3), 30(5), 30(6)(b), 31(2), 31(3).
Readings: (a) the figure is for that kind of case only, the case is a yes-or-no input, and a person outside it gets NOTHING; (b) the figure is for everybody.
Taken: (a).
Text: article 23(7) amends paragraph 3 "as it has effect in a case falling within regulation 4 of the Housing Benefit (Abolition of the Family Premium and date of claim) (Amendment) Regulations 2015", and the others are worded alike.
Asserted in `uro-tests-part3-housing-benefit.l4` and `uro-tests-part5-to-8.l4`.

**F-16 "Has attained pensionable age before 1st April 2021".**
Where: Schedule 6 (1), (2), (4), (5).
Readings: (a) the date the member attained pensionable age is before 1 April 2021; (b) the member has attained it at the time of the claim and did so before that date.
Taken: (a); the two coincide whenever the member has attained it, and a member who has not is in no printed row.
Text: src:618-628.
Asserted in `uro-tests-part3-housing-benefit.l4`.

## Dependencies on instruments outside the text

The Order amends figures in many other instruments, none of which is among the inputs.
Everything the encoding needs from them is a plain input, named for the fact and marked in the module with `-- out of text: <instrument and provision>`.
The table is generated from those comments and from the inputs under them; it has 113 rows.

The ones that matter most:
- The sum the person gets now, for every percentage increase (articles 4, 5, 6, 11, 21), because the Order does not print the old sums.
- The beneficiary's first benefit week (defined in the Income Support Regulations, the JSA Regulations 1996 and 2013, the State Pension Credit Regulations, the ESA Regulations 2008 and 2013 and the Computation of Earnings Regulations) or first assessment period (section 7(2) of the Welfare Reform Act 2012) on or after 6 April 2026, which dates articles 20 to 22 and 25 to 33 and the article 25(b) sum.
- Whether the person meets the condition of a paragraph or regulation of a parent schedule (paragraphs 1A, 9, 9A, 10, 11(1), 13, 13A, 14, 14ZA of Schedule 2 to the Income Support Regulations, and their Housing Benefit, JSA and ESA counterparts; regulations 57(2), 59 to 62 of the JSA Regulations 1996; section 16 and section 3(1)(f)(iii) of the Jobseekers Act 1995), which selects the row of a premium or allowance.
- Pensionable age, and the date it was attained (Schedule 1 Part IV, Part V item 6, Schedule 6).
- Whether the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017 or regulation 4 of the 2015 Housing Benefit Regulations (F-15).
- The first sum in section 44(4) (F-05).


| your provision | the provision it depends on | the input you made |
|---|---|---|
| `art 1(3)(e)` | Contributions and Benefits Act 1992 s 35A(1) (rate of maternity allowance) | `the purpose is the maternity allowance rate under section 35A(1)` |
| `art 1(3)(g)` | Income Support Regulations 1987 reg 2(1) ('benefit week') | `first day of first benefit week on or after 6th April 2026` |
| `art 1(3)(h)` | Housing Benefit Regulations 2006 reg 2(1) and the Housing Benefit (SPC) Regulations 2006 ('rent') | `rent is payable weekly or at a multiple of a week` |
| `art 1(3)(i)` | Jobseeker's Allowance Regulations 1996 reg 1(3) ('benefit week') | `first day of first benefit week (JSA Regulations 1996)` |
| `art 1(3)(j)` | Jobseeker's Allowance Regulations 2013 ('benefit week') | `first day of first benefit week (JSA Regulations 2013)` |
| `art 1(3)(k)` | State Pension Credit Regulations 2002 ('benefit week') | `first day of first benefit week (State Pension Credit Regulations)` |
| `art 1(3)(l)` | Employment and Support Allowance Regulations 2008 ('benefit week') | `first day of first benefit week (ESA Regulations 2008)` |
| `art 1(3)(m)` | Employment and Support Allowance Regulations 2013 ('benefit week') | `first day of first benefit week (ESA Regulations 2013)` |
| `art 1(3)(n)` | Welfare Reform Act 2012 s 7(2) and the Universal Credit Regulations 2013 ('assessment period') | `first day of first assessment period on or after 6th April 2026` |
| `art 1(4)` | Welfare Reform Act 2012 s 7(2) ('assessment period') | `the article`; `a universal credit award is in force`; `the purpose is unearned income under that award`; `first day of first assessment period on or after 6th April 2026` |
| `art 1(3) and (4)` | the 'benefit week' and 'assessment period' instruments listed above for art 1(3)(g) to (n); Housing Benefit Regulations 'rent'; Contributions and Benefits Act s 35A(1) | `the article`; `the increase is an article 7(9)(b) increase`; `the purpose is the maternity allowance rate under section 35A(1)`; `rent is payable weekly or at a multiple of a week`; `first day of first benefit week on or after 6th April 2026`; `a universal credit award is in force`; `the purpose is unearned income under that award`; `first day of first assessment period on or after 6th April 2026` |
| `art 7(4)(b), (5)(a)(i)` | the Secretary of State's arrangement to pay carer's allowance on a Wednesday | `the Secretary of State has made arrangements for it to be paid on a Wednesday` |
| `art 7(9)` | Social Security Benefit (Computation of Earnings) Regulations 1996 reg 7(b) and reg 2(1) ('benefit week') | `regulation 7(b) of the Computation of Earnings Regulations applies`; `the first day of the beneficiary's first benefit week to commence on or after the date in art 7(9)` |
| `art 7` | Social Security Benefit (Computation of Earnings) Regulations 1996 reg 7(b) and reg 2(1) (art 7(9)); the Secretary of State's arrangement to pay carer's allowance on a Wednesday (art 7(4)(b), (5)(a)(i)) | `which change`; `the Secretary of State has made arrangements for it to be paid on a Wednesday`; `regulation 7(b) of the Computation of Earnings Regulations applies`; `the first day of the beneficiary's first benefit week to commence on or after the date in art 7(9)` |
| `art 4(1)` | Contributions and Benefits Act 1992 Sch 7 para 13(4) (the sums calculated for a beneficiary's retirement allowance) | `the sum calculated under paragraph 13(4) of Schedule 7` |
| `art 4(3)(a)` | Contributions and Benefits Act 1992 (additional pension; 'final relevant year') | `the first calendar year of the final relevant year`; `the additional pension` |
| `art 4(3)(b)` | Contributions and Benefits Act 1992 Sch 5 (increase of retirement pension where entitlement is deferred) | `the increase in the rate of a retirement pension under Schedule 5 (entitlement deferred)` |
| `art 4(3)(c)` | Contributions and Benefits Act 1992 Sch 5 para 7A (lump sum) | `the lump sum under paragraph 7A of Schedule 5` |
| `art 4(3)(d)` | Contributions and Benefits Act 1992 ss 126A, 63 and 150 (order-made sums) | `the sum payable as part of a Category A or B retirement pension by virtue of an order` |
| `art 4(3)` | Contributions and Benefits Act 1992 (the places art 4(3) lists) | `which sum`; `the first calendar year of the final relevant year`; `the sum before the increase` |
| `art 4(4)(a)` | Contributions and Benefits Act 1992 ss 55A and 55AA (shared additional pension) | `the shared additional pension under section 55A or 55AA` |
| `art 4(4)(b)` | Contributions and Benefits Act 1992 Sch 5A para 2 | `the increase in a shared additional pension under paragraph 2 of Schedule 5A` |
| `art 5(a)` | Pension Schemes Act 1993 s 15(1) and the tax year of the earnings factors | `the first calendar year of the tax year of the earnings factors`; `the sum payable under section 15(1) of the Pension Schemes Act` |
| `art 5(b)` | Pension Schemes Act 1993 s 15(1) and the tax year of the earnings factors | `the first calendar year of the tax year of the earnings factors`; `the sum payable under section 15(1) of the Pension Schemes Act` |
| `art 5` | Pension Schemes Act 1993 s 15(1) and the tax year of the earnings factors | `the first calendar year of the tax year of the earnings factors`; `the sum payable under section 15(1) of the Pension Schemes Act` |
| `art 6(2)` | Pensions Act 2014 s 17 | `the increase under section 17 of the Pensions Act in the rate of a state pension` |
| `art 6(3)(a)` | Pensions Act 2014 s 9 | `the survivor's pension based on inheritance of deferred old state pension` |
| `art 6(3)(b)` | Pensions Act 2014 Sch 2 para 4(3) | `the amount of a transitional rate state pension that exceeds the full rate` |
| `art 6(3)(c)` | Pensions Act 2014 Sch 4 paras 5(3) and 6 | `the amount of a survivor's pension that exceeds the full rate, alone or with other pensions` |
| `art 6(3)(d)` | Pensions Act 2014 Sch 9 paras 5(3) and 6 | `the amount of a shared state pension that exceeds the full rate, alone or with other pensions` |
| `art 6(3)` | Pensions Act 2014 ss 9 and Schs 2, 4, 9 (the amounts art 6(3) lists) | `which amount`; `the amount before the increase` |
| `art 11(2)` | Social Security (Graduated Retirement Benefit) (No | `the increase of graduated retirement benefit under Schedule 2 to the 1978 Regulations` |
| `art 11(3)` | Social Security (Graduated Retirement Benefit) Regulations 2005 Sch 1 | `the lump sum under Schedule 1 to the Social Security (Graduated Retirement Benefit) Regulations 2005` |
| `art 11(4)` | National Insurance Act 1965 s 37(1) | `the addition under section 37(1) of the National Insurance Act 1965` |
| `art 11(2) to (4)` | Social Security (Graduated Retirement Benefit) (No | `which sum`; `the sum before the increase` |
| `art 16` | Employment and Support Allowance (Up-rating Modification) (Transitional) Regulations 2008 reg 2(3) | `which one`; `the claimant is entitled to long-term incapacity benefit and was subject to regulation 2(3) of the ESA Up-rating Modification Transitional Regulations 2008` |
| `art 17` | Employment and Support Allowance (Up-rating Modification) (Transitional) Regulations 2008 reg 2(3) | `which one`; `the claimant is entitled to long-term incapacity benefit and was subject to regulation 2(3) of the ESA Up-rating Modification Transitional Regulations 2008` |
| `art 23(7)` | Housing Benefit (Abolition of the Family Premium and date of claim) (Amendment) Regulations 2015 reg 4 | `which one`; `the case falls within regulation 4 of the Housing Benefit (Abolition of the Family Premium and date of claim) (Amendment) Regulations 2015` |
| `art 23(9)` | Employment and Support Allowance and Universal Credit (Miscellaneous Amendments and Transitional and Savings Provisions) Regulations 2017 Sch 2 paras 2 to 7 | `which one`; `the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017` |
| `art 24(7)` | Housing Benefit (Abolition of the Family Premium and date of claim) (Amendment) Regulations 2015 reg 4 | `the case falls within regulation 4 of the Housing Benefit (Abolition of the Family Premium and date of claim) (Amendment) Regulations 2015` |
| `Sch 4 (1)` | Employment and Support Allowance Regulations 2008 ('main phase employment and support allowance') | `the claimant is entitled to main phase employment and support allowance`; `the claimant's age` |
| `Sch 4 (2)` | Employment and Support Allowance Regulations 2008 ('main phase employment and support allowance') | `the claimant is entitled to main phase employment and support allowance`; `the claimant's age` |
| `Sch 4 (3)` | Employment and Support Allowance Regulations 2008 ('main phase employment and support allowance') | `the claimant is entitled to main phase employment and support allowance`; `the claimant's age`; `the claimant's partner's age` |
| `Sch 5 (5)` | Housing Benefit Regulations 2006 Sch 3 para 12 | `which condition` |
| `Sch 5 (6)` | Housing Benefit Regulations 2006 Sch 3 para 14(2), (5); Universal Credit Regulations 2013 reg 29 | `which condition`; `someone is in receipt of a carer's allowance or carer support payment or has an award of universal credit which includes the carer element, or the claimant or a partner satisfies the condition only by virtue of paragraph 14(5)` |
| `Sch 5 (7)` | Housing Benefit Regulations 2006 Sch 3 Part 3 para 16 | `the number of children and young persons in respect of whom the condition in paragraph 16 of Part 3 is satisfied` |
| `Sch 5 (8)` | Housing Benefit Regulations 2006 Sch 3 para 17 | `the number of persons who satisfy the condition in paragraph 17` |
| `Sch 5 (9)(a)` | Housing Benefit Regulations 2006 Sch 3 para 15 | `the number of children and young persons in respect of whom the conditions in paragraph 15 are satisfied` |
| `Sch 5 (9)(b)` | Housing Benefit Regulations 2006 Sch 3 para 15 | `the person is neither a child or young person nor a member of a couple or polygamous marriage`; `the conditions in paragraph 15 are satisfied in respect of the person` |
| `Sch 5 (9)(c)` | Housing Benefit Regulations 2006 Sch 3 para 15 | `the claimant is a member of a couple or polygamous marriage`; `the conditions in paragraph 15 are satisfied in respect of a member of that couple or polygamous marriage` |
| `Sch 6` | pensionable age | `the member has attained pensionable age`; `the date on which the member attained pensionable age` |
| `Sch 6 (1)` | pensionable age | `the claimant has attained pensionable age`; `the date on which the claimant attained pensionable age` |
| `Sch 6 (2)` | pensionable age | `the claimant has attained pensionable age`; `the date on which the claimant attained pensionable age`; `the claimant's partner has attained pensionable age`; `the date on which the claimant's partner attained pensionable age` |
| `Sch 6 (4)` | pensionable age | `who` |
| `Sch 6 (5)` | pensionable age | `who` |
| `Sch 6 (4) and (5)` | pensionable age | `who`; `one or more members of the marriage have attained pensionable age before 1st April 2021`; `all members of the marriage have attained pensionable age on or after 1st April 2021` |
| `Sch 7 (1)` | Housing Benefit (SPC) Regulations 2006 Sch 3 para 6(2), (7); Universal Credit Regulations 2013 reg 29 | `which condition`; `someone is in receipt of a carer's allowance or carer support payment or has an award of universal credit which includes the carer element, or the claimant or a partner satisfies the condition only by virtue of paragraph 6(7)` |
| `Sch 7 (2)` | Housing Benefit (SPC) Regulations 2006 Sch 3 para 7 | `the number of children and young persons in respect of whom the conditions in paragraph 7 are satisfied` |
| `Sch 7 (3)` | Housing Benefit (SPC) Regulations 2006 Sch 3 para 8 | `the number of children and young persons in respect of whom the condition in paragraph 8 is satisfied` |
| `Sch 7 (4)` | Housing Benefit (SPC) Regulations 2006 Sch 3 para 9 | `the number of persons who satisfy the condition in paragraph 9` |
| `art 21` | Income Support (Transitional) Regulations 1987 reg 15, the special transitional addition before the Order | `the special transitional addition to income support` |
| `Sch 2 (1)` | Income Support Regulations 1987 Sch 2 paras 1A and 11(1)(a) | `the claimant's age`; `the claimant falls within a circumstance specified in paragraph 1A`; `the claimant satisfies the condition in paragraph 11(1)(a)` |
| `Sch 2 (2)` | Income Support Regulations 1987 Sch 2 paras 1A and 11(1)(a) | `the claimant's age`; `the claimant falls within a circumstance specified in paragraph 1A`; `the claimant satisfies the condition in paragraph 11(1)(a)` |
| `Sch 2 (3)` | Income Support Regulations 1987 reg 4ZA and Sch 2 para 1A; Jobseekers Act 1995 ss 3(1)(f)(iii) and 16; income-related employment and support allowance | `the claimant's age`; `the claimant's partner's age`; `at least one of them is treated as responsible for a child`; `the claimant qualifies for income support under regulation 4ZA or income-related employment and support allowance, or would if not a member of a couple`; `the partner qualifies for income support under regulation 4ZA or income-related employment and support allowance, or would if not a member of a couple`; `the claimant satisfies the requirements of section 3(1)(f)(iii) of the Jobseekers Act 1995`; `the partner satisfies the requirements of section 3(1)(f)(iii) of the Jobseekers Act 1995`; `a direction under section 16 of the Jobseekers Act 1995 is in force in respect of the claimant`; `a direction under section 16 of the Jobseekers Act 1995 is in force in respect of the partner`; `one member of the couple falls within a circumstance specified in paragraph 1A` |
| `Sch 3 (2)` | Income Support Regulations 1987 Sch 2 paras 9, 9A and 10 | `paragraph 9 applies to the claimant` |
| `Sch 3 (2A)` | Income Support Regulations 1987 Sch 2 paras 9, 9A and 10 | `paragraph 9A applies to the claimant` |
| `Sch 3 (3)` | Income Support Regulations 1987 Sch 2 paras 9, 9A and 10 | `paragraph 10 applies to the claimant` |
| `Sch 3 (4)` | Income Support Regulations 1987 Sch 2 para 11(1) | `which condition` |
| `Sch 3 (5)` | Income Support Regulations 1987 Sch 2 para 13(2) and (3A) | `which condition`; `someone is in receipt of a carer's allowance or carer support payment, or the claimant or a partner satisfies the condition only by virtue of paragraph 13(3A)` |
| `Sch 3 (6)` | Income Support Regulations 1987 Sch 2 para 14 | `the number of children and young persons in respect of whom the condition in paragraph 14 is satisfied` |
| `Sch 3 (7)` | Income Support Regulations 1987 Sch 2 para 14ZA | `the number of persons who satisfy the condition in paragraph 14ZA` |
| `Sch 3 (8)(a)` | Income Support Regulations 1987 Sch 2 para 13A | `the number of children and young persons in respect of whom the conditions in paragraph 13A are satisfied` |
| `Sch 3 (8)(b)` | Income Support Regulations 1987 Sch 2 para 13A | `the person is neither a child or young person nor a member of a couple or polygamous marriage`; `the conditions in paragraph 13A are satisfied in respect of the person` |
| `Sch 3 (8)(c)` | Income Support Regulations 1987 Sch 2 para 13A | `the claimant is a member of a couple or polygamous marriage`; `the conditions in paragraph 13A are satisfied in respect of a member of that couple or polygamous marriage` |
| `Sch 8 (1)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 61, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16 | `the claimant's age`; `the claimant falls within paragraph (2) of regulation 57`; `regulation 59, 60 or 61 applies to the claimant`; `a direction under section 16 is in force in respect of the claimant`; `the claimant satisfies the condition in paragraph 13(1)(a) of Part 3` |
| `Sch 8 (2)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 61, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16 | `the claimant's age`; `the claimant falls within paragraph (2) of regulation 57`; `regulation 59, 60 or 61 applies to the claimant`; `a direction under section 16 is in force in respect of the claimant`; `the claimant satisfies the condition in paragraph 13(1)(a) of Part 3` |
| `Sch 8 (3)(f)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 62, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16; income support and income-related employment and support allowance entitlement | `m` |
| `Sch 8 (3)(g), (h)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 62, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16; income support and income-related employment and support allowance entitlement | `m` |
| `Sch 8 (3)(a)(iii), (vii)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 62, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16; income support and income-related employment and support allowance entitlement | `m` |
| `Sch 8 (3)` | Jobseeker's Allowance Regulations 1996 regs 57(2), 59 to 62, Sch 1 Part 3 para 13(1)(a); Jobseekers Act 1995 s 16; income support and income-related employment and support allowance entitlement | `the claimant`; `the claimant's partner`; `the claimant and the partner are married or civil partners` |
| `Sch 9 (2)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 10 | `which condition` |
| `Sch 9 (3)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 11 | `the claimant satisfies the condition in paragraph 11` |
| `Sch 9 (4)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 12(1) | `which condition` |
| `Sch 9 (5)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 13(1) | `which condition` |
| `Sch 9 (6)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 15(1), (2), (5) | `which condition`; `someone is in receipt of a carer's allowance or carer support payment, or a partner of the claimant satisfies the condition by virtue of paragraph 15(5)` |
| `Sch 9 (7)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 16 | `the number of children and young persons in respect of whom the conditions in paragraph 16 are satisfied` |
| `Sch 9 (8)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 17 | `the number of persons who satisfied the condition in paragraph 17` |
| `Sch 9 (9)(a)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 15A | `the number of children and young persons in respect of whom the conditions in paragraph 15A are satisfied` |
| `Sch 9 (9)(b)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 15A | `the person is neither a child or young person nor a member of a couple or polygamous marriage`; `the conditions in paragraph 15A are satisfied in respect of the person` |
| `Sch 9 (9)(c)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part III para 15A | `the claimant is a member of a couple or polygamous marriage`; `the conditions in paragraph 15A are satisfied in respect of a member of that couple or polygamous marriage` |
| `Sch 10 (1)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20E | `one member of the joint-claim couple has attained the qualifying age for state pension credit and the condition in paragraph 20E is satisfied` |
| `Sch 10 (2)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20F | `one member of the joint-claim couple satisfies the condition in paragraph 20F` |
| `Sch 10 (3)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20G(1) | `one member of the joint-claim couple satisfies the condition in paragraph 20G(1)` |
| `Sch 10 (4)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20I(1), (4) | `one member of the joint-claim couple satisfies the condition in paragraph 20I(1)`; `someone is in receipt of a carer's allowance or carer support payment, or either member satisfies that condition only by virtue of paragraph 20I(4)` |
| `Sch 10 (5)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20J | `the number of persons who satisfied the condition in paragraph 20J` |
| `Sch 10 (6)` | Jobseeker's Allowance Regulations 1996 Sch 1 Part IVA para 20IA | `the conditions in paragraph 20IA are satisfied in respect of a member of the joint-claim couple` |
| `art 30(2) and (3)` | Employment and Support Allowance Regulations 2008 (the Act is the one those Regulations name); Employment and Support Allowance and Universal Credit (Miscellaneous Amendments and Transitional and Savings Provisions) Regulations 2017 Sch 2 paras 2 to 7 | `the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017`; `the claimant satisfies the conditions set out in section 2(2) of the Act`; `the claimant satisfies the conditions set out in section 2(3) of the Act`; `the claimant is a member of the work-related activity group`; `the claimant's age` |
| `art 30(4) and (5)` | Employment and Support Allowance Regulations 2008 Sch 4 paras 5, 8(1), 11; the 2017 Regulations Sch 2 paras 2 to 7 | `the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017`; `paragraph 5 applies to the claimant`; `the claimant is a member of a couple`; `the claimant is entitled to the support component`; `the claimant is entitled to the work-related activity component` |
| `art 30(6)(b)` | the 2017 Regulations Sch 2 paras 2 to 7 | `the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017` |
| `art 31(2)` | the 2017 Regulations Sch 2 paras 2 to 7 | `which one`; `the case falls within paragraphs 2 to 7 of Schedule 2 to the ESA and UC Regulations 2017` |
| `art 31(3)` | Employment and Support Allowance (Transitional Provisions, Housing Benefit and Council Tax Benefit) (Existing Awards) (No | `which one`; `regulation 62 applies as modified by paragraph 12 of Schedule 2 to the Employment and Support Allowance (Transitional Provisions, Housing Benefit and Council Tax Benefit) (Existing Awards) (No. 2) Regulations 2010 as that paragraph is modified by paragraph 21(10) of Schedule 4 to the Welfare Reform Act 2012 (Commencement No. 9 and Transitional and Transitory Provisions and Commencement No. 8 and Savings and Transitional Provisions (Amendment)) Order 2013` |
| `Sch 11 paragraph 1 (1)` | Employment and Support Allowance Regulations 2008 (the Act; 'work-related activity group') | `the claimant satisfies the conditions set out in section 2(2) of the Act`; `the claimant is a member of the work-related activity group`; `the claimant's age` |
| `Sch 11 paragraph 2 (1)` | Employment and Support Allowance Regulations 2008 (the Act; 'work-related activity group') | `the claimant satisfies the conditions set out in section 2(2) of the Act`; `the claimant satisfies the conditions set out in section 2(3) of the Act`; `the claimant's age` |
| `Sch 12 paragraph 1 (1)` | Employment and Support Allowance Regulations 2008 Sch 4 paras 5 and 8(1) | `paragraph 5 applies to the claimant`; `the claimant is a member of a couple`; `the claimant is entitled to the support component`; `the claimant is entitled to the work-related activity component` |
| `Sch 12 paragraph 1 (3)` | Employment and Support Allowance Regulations 2008 Sch 4 paras 5 and 8(1) | `the number of persons who satisfy the condition specified in paragraph 8(1)` |
| `Sch 12 paragraph 2 (1)` | Employment and Support Allowance Regulations 2008 Sch 4 paras 5 and 8(1) | `paragraph 5 applies to the claimant`; `the claimant is a member of a couple`; `the claimant is entitled to the support component`; `the claimant is entitled to the work-related activity component` |
| `Sch 13` | Universal Credit Regulations 2013 (which child is first; 'qualifying young person') | `the place of the child or qualifying young person in the order of the children` |
| `Sch 13` | Universal Credit Regulations 2013 (disabled child additional amount) | `which rate` |
| `Sch 13` | Universal Credit Regulations 2013 (childcare costs element) | `the number of children` |
| `Sch 1 Part IV` | pensionable age (Pensions Act 1995 Sch 4 / Pensions Act 2014 definitions) | `which benefit`; `the beneficiary's position relative to pensionable age` |
| `Sch 1 Part V item 2` | Contributions and Benefits Act 1992 Sch 7 (constant attendance; exceptionally severe disablement) | `the disablement is exceptionally severe` |
| `Sch 1 Part V item 6` | Contributions and Benefits Act 1992 Sch 7 para 3 (qualifying date) and pensionable age | `the age of the beneficiary on the qualifying date`; `the qualifying date fell before 5th July 1948`; `the beneficiary had attained pensionable age before 6th April 1979` |
| `Sch 1 Part V item 10(c)` | Contributions and Benefits Act 1992 s 44(4), the first sum | `the first sum specified in section 44(4)` |

## What the text turns out to say

1. The Order has no single commencement date. Article 1(3) fixes 1 April 2026 (heads (a), (b)(i) and, where the rent is not payable weekly, (h)), 5 April (article 9, except for the maternity allowance rate, which is 6 April), 6 April (heads (b)(ii), (c), (h) with a weekly rent, and (d) at 00.01 for articles 5 and 8), 9 April (head (f), articles 16 and 17) and 5 May (head (o), article 34); and it dates articles 20 to 22 and 25 to 33 from the first day of the beneficiary's own first benefit week (assessment period for articles 32 and 33) on or after 6 April 2026. Asserted.
2. "Comes into force" (article 1(3), (4)) and "takes effect" (article 7) are two clocks. Article 3 is in force on 6 April (article 1(3)(b)(ii)) while the change in the disablement benefit sums takes effect on 8 April (article 7(5)); article 1(5) names the changes that take the article 7 date (articles 3, 4, 5, 6, 11, 12, 13 and article 25(b) so far as it limits an adult dependant's earnings). Asserted.
3. Article 7 dates the changes on 6 April (paragraphs (2), (3), (4), (6), (10), (11)), on 8 April (paragraphs (5) and (8), and carer's allowance paid on a Wednesday), on 9 April (paragraph (7)), and, for the article 25(b) sum, on the first day of the beneficiary's first benefit week beginning on or after 6 April 2026, or on or after 1 April where regulation 7(b) of the Computation of Earnings Regulations applies. Asserted.
4. The sum in article 25(b) (92.05 becomes 95.55, in regulation 79(1)(c) of the JSA Regulations 1996) is also borrowed, by article 7(9) and article 1(5)(b), as the earnings limit that decides whether a benefit is increased for an adult dependant. Asserted.
5. The percentage increases carry no rounding rule, and the Order's own substituted sums are not all 3.8 per cent (F-01, F-02). Asserted.
6. Article 3(2) excepts age addition and the child increases from the sums to be increased, yet Schedule 1 prints a figure for each (0.25; 11.35; 11.35). The encoding returns the printed figure (F-11). Asserted.
7. Schedule 1 Part V item 10 prints (b) and (c) but not (a), so there is no (a) row, and (c) is 30 per cent of "the first sum specified in section 44(4)", which the Order does not identify (F-05, F-07). Asserted for (c); there is no rule for (a), so no case asks.
8. The six non-dependant deduction tables (articles 20(6), 23(3), 24(3), 26(7), 29(4), 30(7)) are identical, fifteen pairs each; the seat asks one question with the benefit as an input. Asserted.
9. Article 23(7)(a) says the family premium figure "remains unchanged" at 22.20 while (b) raises 19.48 to 20.22, in cases within regulation 4 of the 2015 Regulations; article 24(7) states only the substitution of 20.22 for 19.48 in the same kind of case. Asserted.
10. Schedule 2 (3) (income support, couples) reaches no figure for a claimant under 18 whose partner is 18 or over and is not within head (e): heads (f) and (g) speak of a claimant aged 18 or over and a partner under 18, never the reverse. The answer is NOTHING, not a guessed figure. Asserted.
11. Schedule 8 (3) (jobseeker's allowance, couples) reaches no figure for a couple both under 18 who are within none of heads (a) to (d); income support's Schedule 2 (3)(c) has a residual head for that case and Schedule 8 (3) does not. The answer is NOTHING. Asserted.
12. Schedule 11 prints only "(1) Single claimant" in both paragraphs, so the Order states no prescribed amount for a lone parent or a couple in employment and support allowance (F-07). Not asserted: there is no rule to ask.
13. Schedule 12's two tables are told apart only by their contents (F-14), the first table's row (iii) reads differently from the second's (F-13), and in a case of article 30(5) the Order sets no carer premium. Asserted.
14. Article 32(1) replaces 684.00 and 411.00 "in each place where it occurs" in the table in regulation 22 without saying how many places; the encoding looks up by the old figure (710.00 and 427.00). Asserted.
15. A slip in the text: article 10(1)(a) at src:131 has an opening quotation mark and no closing one ("£194.32; and"). The figure reads 194.32 all the same, as do the other statutory pay rates (194.32 for paternity, adoption, shared parental, parental bereavement and neonatal care pay; 123.25 for sick pay). Asserted.
16. Articles 16(2) and 17(2) do not substitute figures; they say the sums "shall be increased to" 15.50 and 8.60 (and 8.60 for article 17(2)(c)) for a claimant entitled to long-term incapacity benefit who was subject to regulation 2(3) of the 2008 Regulations, and paragraph (1) in each is "subject to paragraph (2)". The claimant's status is an input. Asserted.
17. Article 19 restates the four bereavement support payment sums (350, 3,500, 100, 2,500) as unchanged. Asserted.
18. Schedule 6 gives two personal allowances by when pensionable age was attained: 256.00 and 238.00 for a single claimant, 383.35 and 363.25 for a couple, 127.35 and 125.25 for each additional spouse in a polygamous marriage. Asserted.
19. Article 34 revokes the 2025 Order on 5 May 2026 (article 1(3)(o)), after every date in heads (a) to (n); the Order is silent about the 2025 Order's effect for the intervening weeks. Asserted for the date; the silence has no rule to ask.
20. Schedule 13 gives the universal credit child element as 351.88 for the first child and 303.94 for the second and each later child, the disabled child additional amount as 164.79 (lower) and 514.71 (higher), the carer element as 209.34, and the childcare costs element as at most 1,071.09 for one child and 1,836.16 for two or more. Asserted.


## What the stable binary does not accept

The binary is the stable 1.6.98 build (`main`); `JL4_LIBRARY_PATH` was unset.

Probed with small files in this run (the diagnostics are quoted):

- `#ASSERT REFUSED ...`: "could not find a definition for the identifier REFUSED". A case outside the encoding is a `NOTHING` or a named constructor, asserted.
- `YMD` is missing from the prelude: "could not find a definition for the identifier YMD". `uro-nouns` defines `YMD y m d MEANS Date d m y`.
- An `#ASSERT` continued on a second line: the second line is "unexpected 2 ... expecting %, ;, OF, end of input, or space token". Every `#ASSERT` is on one line.
- `NOT FALSE AND FALSE` is satisfied and `(NOT FALSE) AND FALSE` fails, so `NOT` takes everything to its right. Every `NOT` is parenthesised.
- A name defined in two imported modules cannot be used: "There are multiple definitions for the identifier". Every top-level name (rules, constructors, record fields, enumerations) is unique across the `uro-` modules.
- `TYPICALLY 3` on a record field: a parse error. Not used.
- A genitive on a function result needs parentheses: `(`f` x)'s `field``; written bare it binds to `x`, and the checker says the projection's argument is a number.
- `§` and `§§` headings are accepted.

Found while writing and left green in the deposit (each is used by a module that `check.sh` runs): `WITH` record construction inside `WHERE` (the two members of Schedule 8 (3) in the seat); `MAYBE` of a record; `CONSIDER ... WHEN JUST ... THEN ... WHEN NOTHING THEN NOTHING`; `BRANCH IF ... THEN ... OTHERWISE`; a seat question with `@export` above `GIVEN`, `@desc` after each input, `GIVETH` and `DECIDE`.

From the Commons guide, section 5, not probed again here: `IMPORT` finds only modules in the importing file's own folder, so every `.l4` file is flat in this folder; no `REFUSE` or `BECAUSE`; no `DateTime` or `EVERY`.

From `srcrefs.py`, not the binary: a locator `src:N-M` needs a quote line covering both N and M in the same file, a locator is a `-` range and never a list with commas, and every run of quote lines needs a locator over it.
A rule that cites two separate places therefore carries two `@ref` lines.
The six pointer paragraphs (arts 20(5), 23(8), 24(8), 26(5), 26(6), 32(2)) and the four pointer sub-paragraphs (arts 20(3)(a), 23(6)(a), 24(6)(a), 26(3)(a)) are each a quote line and an `@ref` of their own on the first rule of the Schedule they point to.
`srcrefs.py check --strict`, which is not asked for here, reports 86 problems: 82 of the form 'line N not covered by the quote lines it follows', 3 'not exact', 1 'orphan quotation' on these files: in the main a `@ref` range that is wider than the quote lines above it.

## What check.sh prints

Run as `L4=<the stable l4> L4_TARGET=unstable ./check.sh` in this folder (the stable binary is already `main`, so `unstable` only tells the script not to compare with a second binary), exit status 0:

```
module                                    errors satisfied  failed  refused  expected
uro-cases-seat.l4                              0       394       0        0         0
uro-nouns.l4                                   0         0       0        0         0
uro-part1-intro.l4                             0         0       0        0         0
uro-part2-art7-effect-dates.l4                 0         0       0        0         0
uro-part2-arts-3-to-6.l4                       0         0       0        0         0
uro-part2-arts-8-to-19.l4                      0         0       0        0         0
uro-part3-housing-benefit.l4                   0         0       0        0         0
uro-part3-income-support.l4                    0         0       0        0         0
uro-part4-jsa.l4                               0         0       0        0         0
uro-part5-pension-credit.l4                    0         0       0        0         0
uro-part6-esa.l4                               0         0       0        0         0
uro-part7-universal-credit.l4                  0         0       0        0         0
uro-part8-revocation.l4                        0         0       0        0         0
uro-schedule1-contributions-act-rates.l4       0         0       0        0         0
uro-seat.l4                                    0         0       0        0         0
uro-tests-non-dependant-deductions.l4          0        40       0        0         0
uro-tests-part1.l4                             0       116       0        0         0
uro-tests-part2-arts-3-to-7.l4                 0        95       0        0         0
uro-tests-part2-arts-8-to-19.l4                0        61       0        0         0
uro-tests-part3-housing-benefit.l4             0        85       0        0         0
uro-tests-part3-income-support.l4              0        71       0        0         0
uro-tests-part4-jsa.l4                         0        92       0        0         0
uro-tests-part5-to-8.l4                        0        80       0        0         0
uro-tests-schedule1.l4                         0        72       0        0         0
TOTAL (24 modules)                             0      1106       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

and `python3 -I srcrefs.py check --refs <uksi-2026-148.txt> uro-*.l4`:

```
srcrefs check: 742 src: lines, 339 runs, 456 locators, 0 problems
```

There is no failing and no refused assertion, and no assertion is written to fail.

## Before this is worth relying on

- Check every figure against the official text of S.I. 2026/148. The source here is a plain-text rendering by a converter script; the encoding is only as good as it is, and the converter lost the paragraph markers of Schedule 12 (F-14).
- Have someone who knows the parent instruments confirm the readings F-01 (rounding), F-03 (article 7), F-10 and F-12 (heads in parallel), F-13 and F-14 (Schedule 12), and F-15 ("as it has effect in"). Each is a choice between readings the text leaves open.
- The parent instruments are not encoded. A question the Order cannot answer alone (is the person within paragraph 13(1)(a)? what sum do they get now? when did their benefit week begin?) is a fact the person has to supply correctly, and the seat does not tell them whether they qualify at all.
- Sums that the Order raises by a percentage are returned as an exact product with no rounding (F-01); a person with a real sum in pounds and pence has to round it as the payer does.
- The commencement dates that depend on a benefit week or an assessment period are inputs; the definition of each lies in another instrument.
- The layer-1 modules are generated from templates that read the text file; a change to the text file needs the templates re-run, not the modules edited.
- Nothing here has been run against a second compiler: the stable build 1.6.98 is the only one used.

## Checked after the run

This section was added by the session that ran the agent, after the run; the sections above are the agent's.

- `L4=<L4_BIN> L4_MAIN=<L4_BIN> ./check.sh` in this folder, with `JL4_LIBRARY_PATH` unset, on the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19): `TOTAL (24 modules) 0 1106 0 0 | 0 1106 0 0`; exit status 0; every main column reads `same`.
  The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
  The agent ran `check.sh` with `L4_TARGET=unstable`, as its brief said, so the output printed above under "What check.sh prints" is from that run.
- `srcrefs.py check --refs` against `../../registers/source-bundle/uksi-2026-148.txt`: `srcrefs check: 742 src: lines, 339 runs, 456 locators, 0 problems`.
- `srcrefs.py check --strict`: `srcrefs check: 742 src: lines, 339 runs, 456 locators, 86 problems`. These findings are counted here and have not been reviewed one by one.
- 131 `@export` seat questions; 247 coverage rows (154 encoded, 62 fork, 31 inert, 0 repealed or blank).
- Paths in the agent's files that named its run folder (`inputs/...`) were rewritten on copying to name the deposited text in `../../registers/source-bundle/`; the agent's brief is kept verbatim as `BRIEF.md`, and the paths in it are the run's own.
- The layer-1 modules of this encoding were generated by throwaway scripts and templates that the agent kept in a scratch folder outside its deposit (which its brief forbade); the generated `.l4` files are the deposit, the scripts are not in this folder, and a change to the text means re-running the generator, not editing a module by hand. The agent's own `NOTES.md` says so.
