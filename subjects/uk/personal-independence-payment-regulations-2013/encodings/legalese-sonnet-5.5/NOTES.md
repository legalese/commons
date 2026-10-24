# Social Security (Personal Independence Payment) Regulations 2013 (S.I. 2013/377): an L4 encoding

Encoding agent `pip` (Claude Sonnet 5.5), written from the single deposited text `uksi-2013-377.txt` (646 lines).

**The source is a plain-text rendering, not the official text.**
It was made by the converter script `ukfetch.py` from the legislation.gov.uk CLML of the revised text (version 2026-04-30, download sha256 `b6dc1499...bde5`).
It is not marked up, it may carry more than one extent version of a provision, and it does not distinguish prospective provisions.
Nothing in this folder is "verified against the official text".

**Target dialect:** `main`, the stable build 1.6.98 (sha256 `82ea44ad...263e`).
The encoding was run with that binary only.

**Status:** complete first pass, unreviewed. Every section of the text has a row in the coverage table and every assertion written is satisfied (see "What check.sh prints"); nothing here has been reviewed by a lawyer, and the forks have not been ruled on.

## Seat


The seat is the individual to whom the Regulations are applied: **a person aged 16 or over with a health condition or disability who claims, or receives, personal independence payment** (the text's "C").
Why: the Commons ruling of 2026-10-18 writes every encoding from the seat of the individual to whom the law is applied, and the brief fixes this one.
Officials get no seat: the Secretary of State's powers (regs 8(1), 9(1), 11) and duties are encoded in layer 1 for what they decide, and in the seat only as what may be done to the person (reg 11), what the person must give and by when (reg 8(2)), and what the person is liable for if they do not (regs 8(3), 9(2), 9(3)).
No further seat layer was written: the text puts duties or liabilities on C alone, so there is no employer or landlord to ask about.

Layer 2 is two files.
`pip-seat.l4` holds 80 questions, each with `@export` and `@desc` on the question and on every plain input, phrased as the claimant asks it ("Do I ...?", "Am I ...?", "By what day must I ...?", "Is an amount ... payable for this day ...?").
It calls the layer-1 rules and restates none of them.
`pip-cases-seat.l4` holds 453 worked cases, at least one for every question, with the facts a real claimant would state, boundary cases on both sides of each threshold, and explicit "not covered" cases.
The questions are grouped under `§§` headings: the assessment (Part 2), the required period condition (Part 3), residence and presence (Part 4), the weekly rate and reaching the relevant age (Parts 5 and 6), payment in a care home, a hospital or custody (Part 7).

Choices of the seat layer, assumed, not ruled (each is a change that can be reverted without touching layer 1):
1. Every fact is a plain input (yes/no, number, date, or one of the modules' own choices).
An optional date is a yes/no and a date, and the optional value is built inside the question.
Where a question needs the answer to another question (for example whether regulation 23 applies to me), it takes that answer as a yes/no and says in its `@desc` which question gives it.
2. The judgments the text leaves to the Secretary of State are conditional inputs, asked as the claimant's best statement of them and never guessed: "likely ... would have determined" (regs 12, 13, 14(a)), "good reason" (regs 8(3), 9(2)), "satisfied that it would be unreasonable to expect C to return" (regs 18A, 18C), "determines that the entitlement results from the same condition" (reg 15(1)(d)).
3. The question on regulation 7(1) takes at most three descriptors of an activity with the days on which each applies (fork F-41), and the question on regulation 32(4) at most three periods of residence (fork F-42).
The layer-1 rules take any number.
4. The number of years in regulations 15(1)(b) and 15B(1)(b) is read through regulations 26(2)(b) and 26A(2)(b) (fork F-39).
5. Both versions of regulation 23A(1)(i), (j) and (k), (l) are applied to the same answers, and the two versions of regulation 27(2) have a question each (fork F-40).
6. The weekly rates (reg 24) are asked for a component and a rate; the text of the deposited version gives one set of amounts and no date from which they run.

## Jural relations


Columns: the Hohfeldian relation the provision gives, who holds it, who bears the correlative duty, liability, disability or no-right, the provision, and the layer-1 rule.
"Act" is the Welfare Reform Act 2012, which is not among the inputs: where a right is the Act's and the regulation only sets a condition or an amount, the row says so.

| relation | holder | correlative bearer | provision | L4 rule |
|---|---|---|---|---|
| none (commencement and short title) | none | none | reg 1 | `reg 1(2): these Regulations are in force in the case on` (pip-part1-general) |
| none (definitions) | none | none | reg 2, Sch 1 para 1 | pip-part1-general, pip-sch1-definitions |
| none (the activities) | none | none | reg 3 | `reg 3(1): the daily living activities`, `reg 3(2): the mobility activities` |
| liability to be assessed, on the basis of the aid or appliance C normally uses or could reasonably be expected to use | Secretary of State (power to assess) | C | reg 4(1), (2) | `reg 4(1): C's level of ability, on the basis of an assessment`, `reg 4(2): C's ability is assessed as if C were wearing or using the aid or appliance` |
| immunity of C from being assessed as satisfying a descriptor unless C can do the activity safely, to a standard, repeatedly and in reasonable time | C | Secretary of State (disability) | reg 4(2A), (4) | `reg 4(2A) and (4): C may be assessed as satisfying a descriptor, from the facts` |
| immunity of C from being treated as also having limited ability when assessed as having severely limited ability | C | Secretary of State (disability) | reg 4(3) | `reg 4(3): the level of ability C is treated as having` |
| none (scoring and the choice of descriptor) | none | none | regs 5, 6, 7, Sch 1 Parts 2 and 3 | pip-part2-assessment, pip-sch1-daily-living-table, pip-sch1-mobility-table |
| power to require information or evidence | Secretary of State | C (liability) | reg 8(1) | `reg 8(1): the Secretary of State may require C to provide the information or evidence` |
| duty to provide the information or evidence within one month, or the longer period the Secretary of State considers reasonable | Secretary of State (right) | C | reg 8(2) | `reg 8(2): the last day for providing the information or evidence`, `reg 8(2): C provided the information or evidence in time` |
| power (and duty) to make a negative determination for the component the failure related to | Secretary of State | C (liability) | reg 8(3) | `reg 8(3): a negative determination must be made in relation to the component to which the failure related` |
| power to require attendance at, or participation in, a consultation | Secretary of State | C (liability) | reg 9(1) | `reg 9(1): C may be required to take part in a consultation` |
| duty to attend or take part; negative determination for failure without good reason | Secretary of State (right, power) | C (duty, liability) | reg 9(2), (5) | `reg 9(2): a negative determination must be made because C failed to attend or participate` |
| immunity of C from reg 9(2) unless 7 days' written notice was sent or C agreed to shorter notice | C | Secretary of State (disability) | reg 9(3), (4) | `reg 9(3): regulation 9(2) can apply because the notice requirement is met` |
| right of C that the Secretary of State take C's health and disability into account in deciding good reason | C | Secretary of State | reg 10 | `reg 10: regulation 10 requires this matter to be taken into account in determining good reason` |
| power to determine afresh whether C continues to have limited or severely limited ability | Secretary of State | C (liability) | reg 11(1) | `reg 11: the Secretary of State may determine afresh whether C continues to have limited or severely limited ability, for this reason` |
| immunity of C from a fresh determination because C does paid or voluntary work | C | Secretary of State (disability) | reg 11(2) | `reg 11: the Secretary of State may determine afresh whether C continues to have limited or severely limited ability, for this reason` (the same rule applies paragraph (2)) |
| right of C to the standard rate, or the enhanced rate, of the daily living component (the Act's right; the regulation sets the required period condition) | C | Secretary of State | reg 12(1), (2) | `reg 12(1): the required period condition for the standard rate of the daily living component is met`, `reg 12(2): the required period condition for the enhanced rate of the daily living component is met` |
| right of C to the standard or enhanced rate of the mobility component (the same) | C | Secretary of State | reg 13(1), (2) | `reg 13(1): the required period condition for the standard rate of the mobility component is met`, `reg 13(2): the required period condition for the enhanced rate of the mobility component is met` |
| none (the prescribed date) | none | none | reg 14 | `reg 14(a): the prescribed date for a claim that has not been determined`, `reg 14(b): the prescribed date on a day of an award` |
| privilege of C to have the end of the earlier award serve as the prescribed date, and the 9 months run from the new claim | C | Secretary of State (no-right to insist on reg 14) | regs 15(2), (3), 15A(2), (3), 15B(2), (3) | `reg 15(2): the dates for determining entitlement under the new claim` and its siblings |
| immunity of C from the look-back limb (a) of regs 12 and 13 | C | Secretary of State (disability) | regs 15A(4), 15B(4) | `reg 15A(4): limb (a) of regulations 12 and 13 is regarded as met`, `reg 15B(4): limb (a) of regulations 12 and 13 is regarded as met` |
| conditions of C's right (the Act's s 77(3)): present in England and Wales, 104 of 156 weeks, habitual residence, immigration status | C | Secretary of State | reg 16 | `reg 16(a): C is present in England and Wales on the day` to `reg 16(d): C is a person who is not excluded by immigration control`, `reg 16: the outcome on the day` |
| none (the relevant area) | none | none | reg 16A | `reg 16A: the relevant area for the limb` |
| immunity of C from losing the presence condition while temporarily absent (13 weeks; 26 weeks for medical treatment or an evacuation) | C | Secretary of State (disability) | regs 17, 18, 18A, 18B, 18C, 18D | `reg 17(1): the first weeks of the absence for which C is treated as present`, `reg 18(1): the first weeks of the absence for which C is treated as present`, `reg 18A(1): the first weeks of the absence for which C is treated as present`, `reg 18B: the total weeks of the absence for which C is treated as present under regulations 17(1), 18(1) and 18A(1)`, `reg 18C(1): the first weeks of the absence for which C is treated as present`, `reg 18D(1): the total weeks of the absence for which C is treated as present under regulations 17(1), 18(1) and 18C(1)` |
| immunity of C from losing the presence condition while abroad in the forces, as an aircraft worker or mariner, or with a forces member | C | Secretary of State (disability) | reg 19 | `reg 19(1): C is treated as present in the relevant area`, `reg 19(2): the person is a member of Her Majesty's forces on the day`, `reg 19(3): the person is an aircraft worker`, `reg 19(3): the person is a mariner` |
| immunity of C from the habitual residence condition (forces, and their families) | C | Secretary of State (disability) | reg 20 | `reg 20: C is treated as habitually resident in Great Britain for the purposes of regulation 16(c)` |
| immunity of C from losing the presence condition while temporarily in Scotland | C | Secretary of State (disability) | reg 20A | `reg 20A: C is treated as present in England and Wales on the day` |
| immunity of C from the 104 week condition (terminal illness; relevant EU Regulation) | C | Secretary of State (disability) | regs 21, 22 | `reg 21: regulation 16 applies as if paragraph (b) were omitted`, `reg 22: regulation 16(b) does not apply on the day` |
| immunity of C from regs 16(a) to (c), for the daily living component only | C | Secretary of State (disability) | reg 23 | `reg 23: regulation 16(a) to (c) do not apply to the daily living component on the day` |
| immunity of C from regs 16(b) and (c) (refugees, certain leave) | C | Secretary of State (disability) | reg 23A | `reg 23A(1): a sub-paragraph of paragraph (1) applies to C on the day` |
| liability of C to have reg 16(c) treated as not satisfied after a move from Scotland | Secretary of State (power) | C (liability) | reg 23ZA | `reg 23ZA: regulation 16(c) is treated as not satisfied on the day by paragraph (1) or (2)` |
| immunity of C from losing presence, and extension of a fixed term, after a move to Scotland (entitled C) | C | Secretary of State (disability) | reg 23ZB | `reg 23ZB(2): C is treated as present in England and Wales on the day`, `reg 23ZB(3): the last day of the fixed term period after any extension` |
| right of C to have an ongoing claim decided after a move to Scotland; privilege of C to withdraw it | C | Secretary of State (duty to decide) | reg 23ZC(1), (5) | `reg 23ZC(1) and (5): the Secretary of State must decide C's claim under section 8 of the 1998 Act` |
| immunity of C from losing presence, and extension of a fixed term, on that decision | C | Secretary of State (disability) | reg 23ZC(7) | `reg 23ZC(7)(a): C is treated as present in England and Wales on the day`, `reg 23ZC(7)(b): the last day of the fixed term period after any extension` |
| right of C to the weekly amounts | C | Secretary of State | reg 24 | `reg 24: the weekly rate, in pounds, of this component at this rate` |
| immunity of C from section 83(1) of the Act (the relevant age) | C | Secretary of State (disability) | regs 25, 26(2)(a), 26A(2)(a), 27(1) | `reg 25: section 83(1) of the Act does not apply to C` and its siblings |
| no-right of C to a higher mobility rate than the previous award on a new claim after the relevant age | Secretary of State | C (no-right) | reg 26(2)(c), (d) | `reg 26(2)(c) and (d): the rate of the mobility component C is entitled to on the new claim` |
| disability of the Secretary of State to award a higher mobility rate, or one from a different condition, on a supersession after the relevant age | C | Secretary of State (disability) | reg 27(2), (3), (4) | `reg 27(3): the Secretary of State may award this rate of the mobility component` |
| no-right of C to payment for a day in a care home (daily living component) | Secretary of State | C (no-right) | reg 28(1) | `reg 28(1): an amount attributable to the daily living component is payable for the day` |
| immunity of C from reg 28(1) (a child in a private placement; accommodated outside the United Kingdom) | C | Secretary of State (disability) | reg 28(3), (4) | `reg 28(3): paragraph (1) does not apply to C` |
| no-right of C to payment while a hospital in-patient aged 18 or over | Secretary of State | C (no-right) | reg 29(1) | `reg 29(1): an amount attributable to either component is payable for the day` |
| immunity of C from reg 29 (under 18 on entry) | C | Secretary of State (disability) | reg 29(3) | `reg 29(3): regulation 29 does not apply because C was under 18 on the day of entry` |
| immunity of C from regs 28(1) and 29(1) for the first 28 days, and when terminally ill in a hospice; from reg 28(1) when the cost is met from private means | C | Secretary of State (disability) | reg 30(1) to (5) | `reg 30(1) and (2): payment goes on because the day is among the first 28 days`, `reg 30(3): regulation 28 or 29 does not apply because C is terminally ill in a hospice`, `reg 30(4): the institution is a hospice`, `reg 30(5): regulation 28(1) does not apply because the total cost is met from private means` |
| none (definitions of "NHS trust", "Local Health Board", "charity") | none | none | reg 30(6), (7) | `reg 30(6) and (7): definitions` |
| no-right of C to payment in custody (the Act's s 87) and immunities from it | Secretary of State | C (no-right); C (immunity) | reg 31 | `reg 31: an amount of personal independence payment is payable for the day`, `reg 31(3): section 87 does not apply because the criminal proceedings concluded`, `reg 31(6): section 87 does not apply because the custody is outside Great Britain` |
| none (periods of residence) | none | none | reg 32 | `reg 32(1): C is in a period of residence`, `reg 32(4): the days of residence in the continuous period up to and including the day` |
| none (the persons Schedule 2 takes out of "a member of Her Majesty's forces") | none | none | Sch 2 | `Sch 2 para 1: the person is specified in Schedule 2` |

## Coverage table

Columns: `| provision | source lines | disposition | where | note |`.
The table has 239 rows: 216 encoded, 22 inert (titles, recitals, headings, machinery) and 1 repealed or blank in this text.
The text has 45 regulations, 2 Schedules and 7 Parts, and each regulation has its own row or rows.

| provision | source lines | disposition | where | note |
|---|---|---|---|---|
| Part 1 heading | src:9 | inert | none | pure citation or title: "PART 1 - General" |
| title block: "Made 25th February 2013" | src:4 | encoded | pip-part1-general: `the date these Regulations were made` | the making date, carried as data with an @ref |
| title block: title, "Coming into force in accordance with regulation 1(2)" | src:1-3, src:5 | inert | none | pure citation or title: the number, subject heading and title of the instrument, and a pointer to regulation 1(2), which is encoded |
| preamble: the powers conferred by sections of the Welfare Reform Act 2012 | src:6 | inert | none | machinery: the recital of the regulation-making powers (ss 77(3), 78(3)-(4), 79(3)-(4), 80, 81, 83(3), 85, 86, 87, 92(1), 94) under which the Secretary of State makes the Regulations; it gives and takes nothing from C |
| preamble: draft approved by each House of Parliament | src:7 | inert | none | machinery: the parliamentary procedure (affirmative resolution under s 94(6) of the Act) by which the instrument was made |
| preamble: made before the end of 6 months from commencement of the provisions | src:8 | inert | none | machinery: a recital that the Regulations were made within the period the Act allows for making them |
| reg 1(1) | src:10-11 | inert | pip-part1-general: `the short title of these Regulations` (a string nothing calls) | pure citation or title: the short title |
| reg 1(2) | src:12 | encoded | pip-part1-general: `reg 1(2): these Regulations are in force in the case on` | in force in a case from the day Part 4 of the Act comes into force in it; that day is an input (out of text) |
| reg 2, lead-in "In these Regulations-" | src:13-14 | inert | none | pure citation or title: the words that introduce the definitions, each of which has its own row |
| reg 2 "the 1998 Act" | src:15 | inert | none | pure citation: names the Social Security Act 1998; every use of it is an input named for the fact (see Dependencies) |
| reg 2 "the Act" | src:16 | inert | none | pure citation: names the Welfare Reform Act 2012; each provision of it that the text depends on is an input (see Dependencies) |
| reg 2 "adult disability payment" | src:17 | encoded | pip-nouns: `the benefit paid under an earlier award`; pip-part1-general: `reg 2: this benefit is adult disability payment` | meaning is given in the Scottish 2022 Regulations (out of text); a previous award of it is a fact |
| reg 2 "aid or appliance" | src:18-20 | encoded | pip-part1-general: `reg 2: a device is an aid or appliance` | |
| reg 2 "assessment" | src:21 | encoded | pip-part1-general: `reg 2: the assessment is the assessment referred to in regulation 4`; the assessment itself is regs 4-7 in pip-part2-assessment | a pointer |
| reg 2 "C" | src:22 | encoded | pip-part1-general: `reg 2: a person is C` | |
| reg 2 "child disability payment" | src:23 | encoded | pip-nouns: `the benefit paid under an earlier award`; pip-part1-general: `reg 2: this benefit is child disability payment` | meaning given in the Scottish 2021 Regulations (out of text) |
| reg 2 "component" | src:24 | encoded | pip-nouns: `a component of personal independence payment`; pip-part1-general: `reg 2: this is a component of personal independence payment` | |
| reg 2 "descriptor" | src:25 | encoded | pip-nouns: `a row of Schedule 1`; pip-part1-general: `reg 2: a descriptor is a descriptor in column 2 ...` | the descriptors themselves are rows of the two table modules |
| reg 2 "disability living allowance" | src:26 | encoded | pip-nouns: `the benefit paid under an earlier award`; pip-part1-general: `reg 2: this benefit is disability living allowance` | defined by reference to s 71 of the 1992 Act (out of text); no rule of these Regulations reads this constructor |
| reg 2 "medical treatment" | src:27 | encoded | pip-part1-general: `reg 2: an intervention is medical treatment` | the second limb ("references to a person receiving or submitting to medical treatment are to be construed accordingly") is a construction rule and needs no code |
| reg 2 "prescribed date" | src:28 | encoded | pip-part3-required-period: `reg 14(a): ...`, `reg 14(b): ...`, `regs 14 to 15B: the provision that fixes the dates the required period condition is tested at` | the converter shows `{repealed: or 15A}`; see the fork register |
| reg 2 "previous award" | src:29 | encoded | pip-part1-general: `reg 2: an award is a previous award` | |
| reg 2 "the residence change date" | src:30 | encoded | pip-part1-general: `reg 2: the residence change date` | notification of the move is irrelevant to the date |
| reg 2 "revised" | src:31 | encoded | pip-part1-general: `reg 2: a decision on an award is revised` | meaning is given by s 9 of the 1998 Act (out of text) |
| reg 2 "run-on period" | src:32 | encoded | pip-part4-special-cases (reg 23ZB(4)) | |
| reg 2 "Scottish adult disability living allowance" | src:33 | encoded | pip-nouns: `the benefit paid under an earlier award`; pip-part1-general: `reg 2: this benefit is Scottish adult disability living allowance` | meaning given in the Scottish 2025 Regulations (out of text) |
| reg 2 "superseded" | src:34 | encoded | pip-part1-general: `reg 2: a decision on an award is superseded` | meaning is given by s 10 of the 1998 Act (out of text) |
| reg 2, last paragraph (terms defined for Part 4 of the Act) | src:35 | inert | none | pure citation: imports the definitions of Part 4 of the Welfare Reform Act 2012, which is not an input; the terms the Regulations use from it ("the relevant age", "qualifying services", and so on) are plain inputs listed under Dependencies |
| Schedule 1, heading and Part 1 heading | src:495-496 | inert | none | pure citation or title: the headings "SCHEDULE 1 - PERSONAL INDEPENDENCE PAYMENT ASSESSMENT" and "PART 1 - INTERPRETATION" |
| Sch 1 para 1, lead-in "In this Schedule,-" | src:497 | inert | none | pure citation or title: the words that introduce the definitions, each of which has its own row below |
| Sch 1 para 1 "aided" | src:498-500 | encoded | pip-sch1-definitions: `Sch 1 para 1: C does the activity aided` | cumulative with "unaided": exactly one of the two holds |
| Sch 1 para 1 "assistance" | src:501 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is assistance` | speech is excluded |
| Sch 1 para 1 "assistance dog" | src:502 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is an assistance dog` |  |
| Sch 1 para 1 "basic verbal information" | src:503 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is basic verbal information` |  |
| Sch 1 para 1 "basic written information" | src:504 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is basic written information` |  |
| Sch 1 para 1 "bathe" | src:505 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is bathing` |  |
| Sch 1 para 1 "communication support" | src:506 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is communication support` |  |
| Sch 1 para 1 "complex budgeting decisions" | src:507-510 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is a complex budgeting decision` | list read as the parts of the term, fork F-12 |
| Sch 1 para 1 "complex verbal information" | src:511 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is complex verbal information` |  |
| Sch 1 para 1 "complex written information" | src:512 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is complex written information` |  |
| Sch 1 para 1 "cook" | src:513 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is cooking` |  |
| Sch 1 para 1 "dress and undress" | src:514 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is dressing or undressing` |  |
| Sch 1 para 1 "engage socially" | src:515-518 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is engaging socially` | list read as the parts of the term, fork F-12 |
| Sch 1 para 1 "manage incontinence" | src:519 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is managing incontinence` | list read as the parts of the term, fork F-12 |
| Sch 1 para 1 "manage medication" | src:520 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is managing medication` | the converter shows dots where the register marks words as removed |
| Sch 1 para 1 "manage therapy" | src:521 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is managing therapy` |  |
| Sch 1 para 1 "medication" | src:522-525 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is medication` |  |
| Sch 1 para 1 "monitor a health condition" | src:526-533 | encoded | pip-sch1-definitions: `Sch 1 para 1: C monitors a health condition` | the converter shows dots after limb (ii); the live limbs (i) to (iv) are encoded |
| Sch 1 para 1 "orientation aid" | src:534 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is an orientation aid` |  |
| Sch 1 para 1 "prepare" | src:535 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is preparing food` |  |
| Sch 1 para 1 "prompting" | src:536 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is prompting` |  |
| Sch 1 para 1 "psychological distress" | src:537 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is psychological distress` |  |
| Sch 1 para 1 "read" | src:538 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is reading` |  |
| Sch 1 para 1 "simple budgeting decisions" | src:539-541 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is a simple budgeting decision` | list read as the parts of the term, fork F-12 |
| Sch 1 para 1 "simple meal" | src:542 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is a simple meal` |  |
| Sch 1 para 1 "social support" | src:543 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is social support` |  |
| Sch 1 para 1 "stand" | src:544 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is standing` |  |
| Sch 1 para 1 "supervision" | src:545 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is supervision` |  |
| Sch 1 para 1 "take nutrition" | src:546-548 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is taking nutrition` | limb (a) read as the parts of the term, fork F-12 |
| Sch 1 para 1 "therapeutic source" | src:549 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is a therapeutic source` |  |
| Sch 1 para 1 "therapy" | src:550-557 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is therapy` | the converter leaves the closing quotation mark off the last line; the exclusion is encoded |
| Sch 1 para 1 "toilet needs" | src:558-561 | encoded | pip-sch1-definitions: `Sch 1 para 1: this is a toilet need` | list read as the parts of the term, fork F-12 |
| Sch 1 para 1 "unaided" | src:562-564 | encoded | pip-sch1-definitions: `Sch 1 para 1: C does the activity unaided` | the mirror of "aided" |
| Sch 1 Part 2, heading and column headings | src:565-566 | inert | none | pure citation or title: "PART 2 - DAILY LIVING ACTIVITIES" and the column headings of the table |
| Sch 1 Part 2, activity 1: Preparing food | src:567-572 | encoded | pip-sch1-daily-living-table: `row for daily living 1a` to `1f`; pip-nouns: `a descriptor of daily living activity 1` | all 6 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 2: Taking nutrition | src:573-578 | encoded | pip-sch1-daily-living-table: `row for daily living 2a` to `2f`; pip-nouns: `a descriptor of daily living activity 2` | all 6 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 3: Managing therapy or monitoring a health condition | src:579-584 | encoded | pip-sch1-daily-living-table: `row for daily living 3a` to `3f`; pip-nouns: `a descriptor of daily living activity 3` | all 6 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 4: Washing and bathing | src:585-591 | encoded | pip-sch1-daily-living-table: `row for daily living 4a` to `4g`; pip-nouns: `a descriptor of daily living activity 4` | all 7 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 5: Managing toilet needs or incontinence | src:592-597 | encoded | pip-sch1-daily-living-table: `row for daily living 5a` to `5f`; pip-nouns: `a descriptor of daily living activity 5` | all 6 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 6: Dressing and undressing | src:598-603 | encoded | pip-sch1-daily-living-table: `row for daily living 6a` to `6f`; pip-nouns: `a descriptor of daily living activity 6` | all 6 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 7: Communicating verbally | src:604-608 | encoded | pip-sch1-daily-living-table: `row for daily living 7a` to `7e`; pip-nouns: `a descriptor of daily living activity 7` | all 5 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 8: Reading and understanding signs, symbols and words | src:609-613 | encoded | pip-sch1-daily-living-table: `row for daily living 8a` to `8e`; pip-nouns: `a descriptor of daily living activity 8` | all 5 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 9: Engaging with other people face to face | src:614-617 | encoded | pip-sch1-daily-living-table: `row for daily living 9a` to `9d`; pip-nouns: `a descriptor of daily living activity 9` | all 4 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 2, activity 10: Making budgeting decisions | src:618-621 | encoded | pip-sch1-daily-living-table: `row for daily living 10a` to `10d`; pip-nouns: `a descriptor of daily living activity 10` | all 4 descriptors with their points; the descriptor's own limbs stay inside its words |
| Sch 1 Part 3, heading and column headings | src:622-623 | inert | none | pure citation or title: "PART 3 - MOBILITY ACTIVITIES" and the column headings of the table |
| Sch 1 Part 3, activity 1: Planning and following journeys | src:624-629 | encoded | pip-sch1-mobility-table: `row for mobility 1a` to `row for mobility 1f` | all 6 descriptors. The register lists an unapplied effect on the Part 3 table (words substituted by the 2017 amending regulations, reg 2(4), in force 2017-03-16): the rows are encoded as printed in the deposited text |
| Sch 1 Part 3, activity 2: Moving around | src:630-635 | encoded | pip-sch1-mobility-table: `row for mobility 2a` to `row for mobility 2f` | all 6 descriptors; same caveat about the unapplied 2017 effect |
| Part 2 heading | src:36 | inert | none | pure citation or title: "PART 2 - Personal independence payment assessment" |
| reg 3(1) | src:37-38 | encoded | pip-part2-assessment: `reg 3(1): the daily living activities`, `reg 3(1): this is a daily living activity` | the ten activities of column 1 of the Part 2 table |
| reg 3(2) | src:39 | encoded | pip-part2-assessment: `reg 3(2): the mobility activities`, `reg 3(2): this is a mobility activity` | the two activities of column 1 of the Part 3 table |
| reg 4(1) | src:40-41 | encoded | pip-part2-assessment: `reg 4(1): C's level of ability, on the basis of an assessment` | the level comes from the assessment, and only where the limitation results from C's physical or mental condition |
| reg 4(2) | src:42-44 | encoded | pip-part2-assessment: `reg 4(2): C's ability is assessed as if C were wearing or using the aid or appliance` | limbs (a) and (b) reach different aids; fork F-4 |
| reg 4(2A) | src:45-49 | encoded | pip-part2-assessment: `reg 4(2A): C may be assessed as satisfying a descriptor that turns on doing the activity` and `reg 4(2A) and (4): ..., from the facts` | four necessary conditions ("only if"); fork F-5 |
| reg 4(3) | src:50 | encoded | pip-part2-assessment: `reg 4(3): the level of ability C is treated as having` | severely limited is not also limited |
| reg 4(4)(a) "safely" | src:51-52 | encoded | pip-part2-assessment: `reg 4(4)(a): the activity is done safely` | |
| reg 4(4)(b) "repeatedly" | src:51, src:53 | encoded | pip-part2-assessment: `reg 4(4)(b): the activity is done repeatedly` | |
| reg 4(4)(c) "reasonable time period" | src:51, src:54 | encoded | pip-part2-assessment: `reg 4(4)(c): the activity is done within a reasonable time period` | no more than twice the normal maximum |
| reg 5(1) | src:55-56 | encoded | pip-part2-assessment: `reg 5(1): the score C obtains in daily living activities` | a score the text cannot give (no descriptor selected) is NOTHING; fork F-7 |
| reg 5(2) | src:57 | encoded | pip-part2-assessment: `reg 5(2) and reg 6(2): the points in the row against the descriptor` | points are column 3 against the descriptor that applies under reg 7 |
| reg 5(3) | src:58-60 | encoded | pip-part2-assessment: `reg 5(3): C's level of ability to carry out daily living activities` | at least 8 limited, at least 12 severely limited; where C has undergone an assessment, else NOTHING |
| reg 6(1) | src:61-62 | encoded | pip-part2-assessment: `reg 6(1): the score C obtains in mobility activities` | |
| reg 6(2) | src:63 | encoded | pip-part2-assessment: `reg 5(2) and reg 6(2): the points in the row against the descriptor` | the same rule as reg 5(2) |
| reg 6(3) | src:64-66 | encoded | pip-part2-assessment: `reg 6(3): C's level of ability to carry out mobility activities` | |
| reg 7(1)(a) | src:67-69 | encoded | pip-part2-assessment: `reg 7(1)(a): the descriptor satisfied on over 50% of the days, where one is` | exactly 50% is not over 50% |
| reg 7(1)(b) | src:70 | encoded | pip-part2-assessment: `reg 7(1)(b): the descriptor scoring the highest points, ...` | a tie on points: the first listed is taken; fork F-6 |
| reg 7(1)(c)(i), (ii) | src:71-73 | encoded | pip-part2-assessment: `reg 7(1)(c): the descriptor that applies where none is satisfied on over 50% but two or more together are` | 0-point descriptors left out of the sum; fork F-6 |
| reg 7(1), as a whole | src:68-73 | encoded | pip-part2-assessment: `reg 7(1): the descriptor which applies to C in relation to the activity` | when none selects a descriptor the result is NOTHING (not covered); fork F-7 |
| reg 7(2) | src:74 | encoded | pip-part2-assessment: `reg 7(2): the descriptor is satisfied on the day` | the likelihood is the Secretary of State's judgment, taken as the input |
| reg 7(3)(a)(i) | src:75-77 | encoded | pip-part2-assessment: `reg 7(3)(a)(i): the required period for a claim after an interval under regulation 15 or 15A` | forks F-1, F-8 |
| reg 7(3)(a)(ii) | src:75-76, src:78 | encoded | pip-part2-assessment: `reg 7(3)(a)(ii): the required period for any other claim` | fork F-1 |
| reg 7(3)(b)(i) | src:79-80 | encoded | pip-part2-assessment: `reg 7(3)(b)(i): the required period for a day of an award in the 3 months after a claim for the purpose of regulation 15 or 15A` | "that date" read as the day of the award; fork F-9 |
| reg 7(3)(b)(ii) | src:79, src:81 | encoded | pip-part2-assessment: `reg 7(3)(b)(ii): the required period for a day of an award in any other case` | |
| reg 8(1) | src:82-83 | encoded | pip-part2-assessment: `reg 8(1): the Secretary of State may require C to provide the information or evidence` | a power of the Secretary of State; C's liability |
| reg 8(2) | src:84 | encoded | pip-part2-assessment: `reg 8(2): the last day for providing the information or evidence`, `reg 8(2): C provided the information or evidence in time` | one month, or the longer period the Secretary of State considers reasonable (an input); fork F-1 |
| reg 8(3) | src:85 | encoded | pip-part2-assessment: `reg 8(3): a negative determination must be made in relation to the component to which the failure related` | "without good reason" is the Secretary of State's judgment; fork F-10 |
| reg 9(1) | src:86-89 | encoded | pip-part2-assessment: `reg 9(1): C may be required to take part in a consultation` | in person, by telephone or by video: the manner is not a condition |
| reg 9(2) | src:90 | encoded | pip-part2-assessment: `reg 9(2): a negative determination must be made because C failed to attend or participate` | subject to (3); fork F-10 |
| reg 9(3) | src:91-93 | encoded | pip-part2-assessment: `reg 9(3): regulation 9(2) can apply because the notice requirement is met` | at least 7 days, or C agrees to a shorter period |
| reg 9(4) | src:94 | encoded | pip-part2-assessment: `reg 9(3): regulation 9(2) can apply because the notice requirement is met` | electronic notice is written notice only where C agreed to correspondence that way (an inputs of the same rule); "electronic communication" has the meaning in s 15(1) of the Electronic Communications Act 2000 (out of text) |
| reg 9(5) | src:95 | encoded | pip-part2-assessment: `reg 9(2): ...` (the input `the consultation is with a person approved by the Secretary of State`) | a consultation is one with an approved person |
| reg 10 | src:96-99 | encoded | pip-part2-assessment: `reg 10: regulation 10 requires this matter to be taken into account in determining good reason` | "include": a floor, not a closed list; silent on other matters |
| reg 11(1) | src:100-101 | encoded | pip-part2-assessment: `reg 11: the Secretary of State may determine afresh ..., for this reason` | a power of the Secretary of State; C's liability |
| reg 11(2) | src:102 | encoded | pip-part2-assessment: `reg 11: ...` | doing paid work, or voluntary work, is not a reason |
| Part 3 heading | src:103 | inert | none | pure citation or title: "PART 3 - Required period condition" |
| reg 12(1) | src:104-107 | encoded | pip-part3-required-period: `reg 12(1): the required period condition for the standard rate of the daily living component is met` | limited and not severely limited at every time in the 3 months and in the 9 months; "likely that the Secretary of State would have determined" is an input; fork F-2 |
| reg 12(2) | src:108-110 | encoded | pip-part3-required-period: `reg 12(2): the required period condition for the enhanced rate of the daily living component is met` | severely limited at every time in both windows; fork F-2 |
| reg 13(1) | src:111-114 | encoded | pip-part3-required-period: `reg 13(1): the required period condition for the standard rate of the mobility component is met` | as reg 12(1), for mobility activities |
| reg 13(2) | src:115-117 | encoded | pip-part3-required-period: `reg 13(2): the required period condition for the enhanced rate of the mobility component is met` | as reg 12(2), for mobility activities |
| reg 14(a) | src:118-120 | encoded | pip-part3-required-period: `reg 14(a): the prescribed date for a claim that has not been determined` | the claim date or, if later, the earliest date the Secretary of State would likely have found the ability over the previous 3 months (an input); no such date gives the claim date; fork F-13 |
| reg 14(b) | src:121 | encoded | pip-part3-required-period: `reg 14(b): the prescribed date on a day of an award` | each day of the award |
| reg 15(1) | src:122-129 | encoded | pip-part3-required-period: `reg 15(1): regulation 15(2) and (3) apply to the new claim` | previous PIP or ADP award ended within the years of limb (b); same component; Secretary of State's determination of the same or a resulting condition is an input; the 2 years become 1 under reg 26 (the number is an input); fork F-15 |
| reg 15(2) | src:130-132 | encoded | pip-part3-required-period: `reg 15(2): the dates for determining entitlement under the new claim` | the look-back runs from the end of the previous award; the look-forward from the new claim date; forks F-8, F-16 |
| reg 15(3) | src:133-135 | encoded | pip-part3-required-period: `reg 15(3): the dates for continued entitlement in the 3 months following the new claim` | the look-forward is each day of the award |
| reg 15(4) | src:136 | encoded | pip-part3-required-period: `reg 15(4): regulation 15 is subject to regulation 26` | a cross-reference; the substance is in pip-part6-age |
| reg 15A(1) | src:137-141 | encoded | pip-part3-required-period: `reg 15A(1): regulation 15A(2) to (5) apply to the new claim` | the converter's `{repealed: and (4)}` is read as struck; paragraph (4) is live |
| reg 15A(2) | src:142-144 | encoded | pip-part3-required-period: `reg 15A(2): the dates for determining entitlement under the new claim` | |
| reg 15A(3) | src:145-147 | encoded | pip-part3-required-period: `reg 15A(3): the dates for entitlement in the 3 months following the new claim` | |
| reg 15A(4) | src:148-150 | encoded | pip-part3-required-period: `reg 15A(4): limb (a) of regulations 12 and 13 is regarded as met` | feeds the input of regs 12 and 13 |
| reg 15A(5) | src:151 | encoded | pip-part3-required-period: `reg 15A(5): the day the previous child disability payment award is treated as having ended` | "immediately before" is read as the day before the new claim |
| reg 15B(1) | src:152-157 | encoded | pip-part3-required-period: `reg 15B(1): regulation 15B(2) to (6) apply to the new claim` | 64 or younger on 8 April 2013 means the 65th birthday falls after that date |
| reg 15B(2) | src:158-160 | encoded | pip-part3-required-period: `reg 15B(2): the dates for determining entitlement under the new claim` | |
| reg 15B(3) | src:161-163 | encoded | pip-part3-required-period: `reg 15B(3): the dates for continued entitlement in the 3 months following the new claim` | the text says "Scottish disability living allowance" in limb (a); read as the Scottish adult disability living allowance of (1)(b); fork F-17 |
| reg 15B(4) | src:164-166 | encoded | pip-part3-required-period: `reg 15B(4): limb (a) of regulations 12 and 13 is regarded as met` | |
| reg 15B(5) | src:167 | encoded | pip-part3-required-period: `reg 15B(5): regulation 15B is subject to regulation 26A` | a cross-reference; the substance is in pip-part6-age |
| reg 15B(6) | src:168 | encoded | pip-part3-required-period: `reg 15B(6): the day the previous Scottish adult disability living allowance award is treated as having ended` | |
| regs 14 to 15B, which one applies | src:119 | encoded | pip-part3-required-period: `regs 14 to 15B: the provision that fixes the dates the required period condition is tested at` | reg 14's "except where" opening; more than one of regs 15, 15A, 15B applying is not covered; fork F-14 |
| Part 4 heading | src:169 | inert | none | pure citation or title: "PART 4 - Residence and presence conditions" |
| reg 16, opening words | src:170-171 | encoded | pip-part4-special-cases: `reg 16: the outcome on the day` | "Subject to the following provisions of this Part": each later regulation modifies a limb through the `... as modified` rules; the answer is three-valued; forks F-22, F-28 |
| reg 16(a) | src:172 | encoded | pip-part4-residence: `reg 16(a): C is present in England and Wales on the day`; pip-part4-special-cases: `reg 16(a) as modified: limb (a) is met` | present, or treated as present by regs 17 to 19, 20A, 23ZB(2), 23ZC(7); disapplied by reg 23 for the daily living component |
| reg 16(b) | src:173 | encoded | pip-part4-residence: `reg 16(b): C has been present in Great Britain for not less than 104 weeks out of the 156 weeks`; pip-part4-special-cases: `reg 16(b) as modified: limb (b) is met` | treated weeks count toward the aggregate; fork F-27; boundary 103/104 asserted |
| reg 16(c) | src:174 | encoded | pip-part4-residence: `reg 16(c): C is habitually resident in the United Kingdom, the Republic of Ireland, the Isle of Man or the Channel Islands`; pip-part4-special-cases: `reg 16(c) as modified: limb (c) is met` | habitual residence is a fact the person states; fork F-22 for the conflict with reg 23ZA |
| reg 16(d) | src:175-177 | encoded | pip-part4-residence: `reg 16(d): C is a person who is not excluded by immigration control` | (i) or (ii) |
| reg 16A | src:178-181 | encoded | pip-part4-residence: `reg 16A: the relevant area for the limb` | England and Wales for limb (a); Great Britain for limb (b) |
| reg 17(1) | src:182-183 | encoded | pip-part4-residence: `reg 17(1): the first weeks of the absence for which C is treated as present` | 13 weeks; forks F-25, F-26 |
| reg 17(2) | src:184 | encoded | pip-part4-residence: `reg 17(2): C is temporarily absent` | "unlikely to exceed 52 weeks" at the beginning is a fact the person states |
| reg 18(1) | src:185-191 | encoded | pip-part4-residence: `reg 18(1): the first weeks of the absence for which C is treated as present` | 26 weeks when all four limbs of (a) and (b) hold |
| reg 18(2) | src:192 | encoded | pip-part4-residence: `reg 17(2): C is temporarily absent` | "temporarily absent" has the meaning of reg 17(2): the same rule is used |
| reg 18A(1) | src:193-199 | encoded | pip-part4-residence: `reg 18A(1): the first weeks of the absence for which C is treated as present`, `reg 18A(1)(a): ...` | the Secretary of State's satisfaction is an input; the converter's `{repealed: Great Britain}` is read as struck |
| reg 18A(2) | src:200 | encoded | pip-part4-residence: `reg 17(2): C is temporarily absent` | as reg 18(2) |
| reg 18B | src:201-202 | encoded | pip-part4-residence: `reg 18B: the total weeks of the absence for which C is treated as present under regulations 17(1), 18(1) and 18A(1)` | the longest of the three periods, at most 26 weeks; fork F-26 |
| reg 18C(1) | src:203-209 | encoded | pip-part4-residence: `reg 18C(1): the first weeks of the absence for which C is treated as present` | the same text as reg 18A with the Scottish Ministers as the satisfied party; fork F-21 |
| reg 18C(2) | src:210 | encoded | pip-part4-residence: `reg 17(2): C is temporarily absent` | as reg 18(2) |
| reg 18D | src:211-212 | encoded | pip-part4-residence: `reg 18D(1): the total weeks of the absence for which C is treated as present under regulations 17(1), 18(1) and 18C(1)` | as reg 18B; fork F-21 |
| reg 19(1) | src:213-220 | encoded | pip-part4-residence: `reg 19(1): one of the circumstances of paragraphs (a) to (c) applies`, `reg 19(1): C is treated as present in the relevant area` | no time limit; the employment prescribed for s 120 SSCBA 1992 is a fact the person states |
| reg 19(2) | src:221-223 | encoded | pip-part4-residence: `reg 19(2): the person is a member of Her Majesty's forces on the day` | "over the age of 16" read strictly; fork F-19; Schedule 2 brought in |
| reg 19(3) "aircraft worker" | src:224-228 | encoded | pip-part4-residence: `reg 19(3): the person is an aircraft worker` | fork F-20 |
| reg 19(3) "mariner" | src:229-232 | encoded | pip-part4-residence: `reg 19(3): the person is a mariner` | fork F-20 |
| reg 20 | src:233-236 | encoded | pip-part4-residence: `reg 20: C is treated as habitually resident in Great Britain for the purposes of regulation 16(c)` | |
| reg 20A | src:237-240 | encoded | pip-part4-residence: `reg 20A: C is treated as present in England and Wales on the day` | |
| reg 21 | src:241-242 | encoded | pip-part4-residence: `reg 21: regulation 16 applies as if paragraph (b) were omitted` | "terminally ill" is the Act's term, an input |
| reg 22 | src:243-247 | encoded | pip-part4-special-cases: `reg 22: regulation 16(b) does not apply on the day` | "relevant EU Regulation" and "genuine and sufficient link" are inputs |
| reg 23 | src:248-256 | encoded | pip-part4-special-cases: `reg 23: regulation 16(a) to (c) do not apply to the daily living component on the day` and `reg 23(a)`, `reg 23(b)`, `reg 23(b)(ii)` rules | daily living component only; fork F-30 |
| reg 23ZA(1) | src:257-258 | encoded | pip-part4-special-cases: `reg 23ZA(1): regulation 16(c) is treated as not satisfied on the day` | "treated as not satisfied" against regs 20, 23 and 23A(1A): fork F-22 |
| reg 23ZA(2) | src:259 | encoded | pip-part4-special-cases: `reg 23ZA(2): regulation 16(c) is treated as not satisfied on the day` | |
| reg 23ZB(1) | src:260-261 | encoded | pip-part4-special-cases: `reg 23ZB(1): this regulation applies` | on or after 6 November 2025 |
| reg 23ZB(2) | src:262 | encoded | pip-part4-special-cases: `reg 23ZB(2): C is treated as present in England and Wales on the day` | for the duration of the run-on period; fork F-29 |
| reg 23ZB(3) | src:263-266 | encoded | pip-part4-special-cases: `reg 23ZB(3): the last day of the fixed term period after any extension` | a term expiring on the last day of the run-on period is not extended; fork F-31 |
| reg 23ZB(4) | src:267-269 | encoded | pip-part4-special-cases: `reg 23ZB(4): the first day of the run-on period`, `... the last day ...`, `... the day is in the run-on period` | 13 weeks beginning on the residence change date |
| reg 23ZC(1) and (2) | src:270-277 | encoded | pip-part4-special-cases: `reg 23ZC(2): C satisfies the conditions` | |
| reg 23ZC(3) | src:278-281 | encoded | pip-part4-special-cases: `reg 23ZC(3): C has an ongoing claim on the residence change date` | |
| reg 23ZC(4) | src:282 | encoded | pip-part4-special-cases: `reg 23ZC(2)(c) and (4): C is present or treated as present on the day` | the pre-6 November 2025 reading; fork F-29 |
| reg 23ZC(5) | src:283 | encoded | pip-part4-special-cases: `reg 23ZC(1) and (5): the Secretary of State must decide C's claim under section 8 of the 1998 Act` | a duty of the Secretary of State; C's right to a decision |
| reg 23ZC(6) | src:284 | encoded | pip-part4-special-cases: `reg 23ZC(6): regulation 16(a) is read with "Great Britain" in place of "England and Wales" for the decision` | fork F-28 |
| reg 23ZC(7)(a) | src:285-286 | encoded | pip-part4-special-cases: `reg 23ZC(7)(a): C is treated as present in England and Wales on the day` | |
| reg 23ZC(7)(b) | src:287-290 | encoded | pip-part4-special-cases: `reg 23ZC(7)(b): the last day of the fixed term period after any extension` | fork F-31 |
| reg 23ZC(8) | src:291-293 | encoded | pip-part4-special-cases: `reg 23ZC(8): definitions` | definitions of "the Claims and Payments Regulations" and the date of a claim; carried as text |
| reg 23A(1)(a), (b) | src:294-297 | encoded | pip-part4-special-cases: `reg 23A(1): a sub-paragraph of paragraph (1) applies to C on the day` | facts the person states: refugee status or humanitarian protection; leave as their dependant; the heading appears twice in the text (two extent versions) |
| reg 23A(1)(c) | src:298-300 | encoded | pip-part4-special-cases: `reg 23A(1)(c): ...` | |
| reg 23A(1)(d), (e) | src:301-302 | encoded | pip-part4-special-cases: `reg 23A(1): a sub-paragraph of paragraph (1) applies to C on the day` | facts the person states; `{repealed: ...}` after (d) is read as struck |
| reg 23A(1)(f) | src:303-305 | encoded | pip-part4-special-cases: `reg 23A(1)(f): the Ukraine paragraph applies` | |
| reg 23A(1)(g) | src:306-308 | encoded | pip-part4-special-cases: `reg 23A(1)(g): the Sudan paragraph applies` | "residing in Sudan before 15 April 2023" without "immediately"; fork F-23 |
| reg 23A(1)(h) | src:309-311 | encoded | pip-part4-special-cases: `reg 23A(1)(h): the Israel and region paragraph applies` | |
| reg 23A(1)(i), Conditions A to D | src:312-326 | encoded | pip-part4-special-cases: `reg 23A(1)(i) Condition A` to `Condition D` and `reg 23A(1)(i): C met conditions A to D` | first of two versions; fork F-24 |
| reg 23A(1)(j) | src:327 | encoded | pip-part4-special-cases: `reg 23A(1)(j): ...` | |
| reg 23A(1)(k), Conditions A to D | src:328-342 | encoded | pip-part4-special-cases: `reg 23A(1)(k) Condition A` to `Condition D` and `reg 23A(1)(k): C met conditions A to D` | second version of (i); fork F-24 |
| reg 23A(1)(l) | src:343 | encoded | pip-part4-special-cases: `reg 23A(1)(l): ...` | second version of (j); fork F-24 |
| reg 23A(1A) | src:344 | encoded | pip-part4-special-cases: `reg 23A(1): a sub-paragraph of paragraph (1) applies to C on the day` | the same rule serves (1) for limb (b) and (1A) for limb (c); fork F-22 |
| reg 23A(1B), (1C) | src:345-346 | encoded | pip-part4-special-cases: `reg 23A(1B) and (1C): the paragraph still applies on the day` | 130 weeks from the day the information is issued or the evacuation started |
| reg 23A (2) as printed in the first position | src:347 | repealed or blank in this text | none | the converter shows `({repealed: 2}) {repealed: For the purposes of this regulation "immigration rules" means ...}`; the same definition is live in paragraph (2)(a) below |
| reg 23A(2) | src:348-350 | encoded | pip-part4-special-cases: `reg 23A(2): definitions` | "immigration rules" and "the Afghan Citizens Resettlement Scheme" (announced 18 August 2021) as text |
| Part 5 heading | src:351 | inert | none | pure citation or title: "PART 5 - Rate of personal independence payment" |
| reg 24(1) | src:352-355 | encoded | pip-part5-rates: `reg 24(1)(a): ...`, `reg 24(1)(b): ...`, `reg 24: the weekly rate, in pounds, of this component at this rate` | 76.70 and 114.60 pounds a week |
| reg 24(2) | src:356-358 | encoded | pip-part5-rates: `reg 24(2)(a): ...`, `reg 24(2)(b): ...` | 30.30 and 80.00 pounds a week; no rate of a component has no amount, so that case is not covered |
| Part 6 heading | src:359 | inert | none | pure citation or title: "PART 6 - Provisions relating to age" |
| reg 25 | src:360-363 | encoded | pip-part6-age: `reg 25: section 83(1) of the Act does not apply to C`, `reg 25(b): the claim made before the relevant age qualifies` | "the relevant age" is the Act's term, an input |
| reg 26(1) | src:364-365 | encoded | pip-part6-age: `reg 26(1): the exceptions of regulation 26(2) apply` | |
| reg 26(2)(a) | src:366-367 | encoded | pip-part6-age: `reg 26(2)(a): section 83(1) of the Act does not apply to C` | |
| reg 26(2)(b) | src:368 | encoded | pip-part6-age: `reg 26(2)(b): the number of years in regulation 15(1)(b)` | the number of years feeds `reg 15(1): ...` in pip-part3-required-period |
| reg 26(2)(c), (d) | src:369-372 | encoded | pip-part6-age: `reg 26(2)(c) and (d): the rate of the mobility component C is entitled to on the new claim` | nothing where reg 26(1) does not apply; a person with no mobility rate under the previous award gets none; fork F-35 |
| reg 26A(1) | src:373-374 | encoded | pip-part6-age: `reg 26A(1): the exceptions of regulation 26A(2) apply` | |
| reg 26A(2)(a) | src:375-376 | encoded | pip-part6-age: `reg 26A(2)(a): section 83(1) of the Act does not apply to C` | |
| reg 26A(2)(b) | src:377 | encoded | pip-part6-age: `reg 26A(2)(b): the number of years in regulation 15B(1)(b)` | |
| reg 27(1) | src:378-381 | encoded | pip-part6-age: `reg 27(1): section 83(1) of the Act does not apply on the revision or supersession` | |
| reg 27(2), first version | src:382-387 | encoded | pip-part6-age: `reg 27(2) (Scottish Ministers version): the restrictions in paragraph (3) apply` | the paragraph appears twice in the text; fork F-32 |
| reg 27(2), second version | src:388-393 | encoded | pip-part6-age: `reg 27(2) (Secretary of State version): the restrictions in paragraph (3) apply` | fork F-32 |
| reg 27(2A) | src:394 | encoded | pip-part6-age: `reg 27(2A): the Decisions and Appeals Regulations` | a definition, carried as text |
| reg 27(3) | src:395-399 | encoded | pip-part6-age: `reg 27(3): the Secretary of State may award this rate of the mobility component` | the text is silent on a standard rate after an original enhanced rate: NOTHING; fork F-33 |
| reg 27(4) | src:400 | encoded | pip-part6-age: `reg 27(4): entitlement under the previous award is treated as if it were under the original award` | ceased no more than 1 year before the effective date |
| Part 7 heading | src:401 | inert | none | pure citation or title: "PART 7 - Payability when person is residing in certain accommodation or is detained in custody" |
| reg 28(1) | src:402-403 | encoded | pip-part7-payability: `reg 28(1): an amount attributable to the daily living component is payable for the day` | |
| reg 28(2) | src:404-420 | encoded | pip-part7-payability: `reg 28(2): this enactment is a specified enactment`, `reg 28(2): C meets the condition in section 85(2) of the Act` | "; ..." after (e), (ee), (eea) read as struck; the seven exceptions to (f) as constructors; fork F-36 |
| reg 28(3) | src:421-426 | encoded | pip-part7-payability: `reg 28(3): paragraph (1) does not apply to C` and the (a), (aa), (b) rules | the converter's trailing "..." after (a)(ii) is read as struck |
| reg 28(4) | src:427 | encoded | pip-part7-payability: `reg 28(3)(a), (aa) and (4): the local authority placement exception applies` | |
| reg 29(1) | src:428-429 | encoded | pip-part7-payability: `reg 29(1): an amount attributable to either component is payable for the day` | |
| reg 29(2) | src:430-435 | encoded | pip-part7-payability: `reg 29(2): the costs of treatment, accommodation or related services are borne out of public funds` | |
| reg 29(3) | src:436 | encoded | pip-part7-payability: `reg 29(3): regulation 29 does not apply because C was under 18 on the day of entry` | the 18th birthday itself is not under 18 |
| reg 30(1), (2) | src:437-439 | encoded | pip-part7-payability: `reg 30(1) and (2): payment goes on because the day is among the first 28 days` | the days are those of reg 32(4); fork F-34 |
| reg 30(3) | src:440-443 | encoded | pip-part7-payability: `reg 30(3): regulation 28 or 29 does not apply because C is terminally ill in a hospice` | |
| reg 30(4) | src:444-453 | encoded | pip-part7-payability: `reg 30(4): the institution is a hospice` | |
| reg 30(5) | src:454-456 | encoded | pip-part7-payability: `reg 30(5): regulation 28(1) does not apply because the total cost is met from private means` | |
| reg 30(6) | src:457-459 | encoded | pip-part7-payability: `reg 30(6) and (7): definitions` | definitions of "NHS trust" and "Local Health Board", carried as text |
| reg 30(7) | src:460 | encoded | pip-part7-payability: `reg 30(6) and (7): definitions` | construction of "charity" in Scotland, carried as text |
| reg 31(1), (2) | src:461-463 | encoded | pip-part7-payability: `reg 31(1) and (2): section 87 does not apply because the day is among the first 28 days`, `reg 31: an amount of personal independence payment is payable for the day` | |
| reg 31(3) | src:464 | encoded | pip-part7-payability: `reg 31(3): section 87 does not apply because the criminal proceedings concluded` | |
| reg 31(4) | src:465-471 | encoded | pip-part7-payability: `reg 31(4): C satisfies one of the conditions` | |
| reg 31(5) | src:472-474 | encoded | pip-part7-payability: `reg 31(5)(a): ...`, `reg 31(5)(b): ...` | |
| reg 31(6) | src:475-477 | encoded | pip-part7-payability: `reg 31(6): section 87 does not apply because the custody is outside Great Britain` | whether C would have been excepted in Great Britain is a fact the person states; fork F-37 |
| reg 32(1) | src:478-482 | encoded | pip-part7-periods: `reg 32(1): C is in a period of residence` | |
| reg 32(2) | src:483-485 | encoded | pip-part7-periods: `reg 32(2)(a): ...`, `reg 32(2)(b) and (3): ...`, `reg 32(2) and (3): the period of residence from entry to leaving` | begins the day after entry; ends the day before leaving |
| reg 32(3) | src:486 | encoded | pip-part7-periods: `reg 32(2)(b) and (3): the last day of the period of residence` | a following period makes the earlier end on the day C leaves |
| reg 32(4) | src:487-489 | encoded | pip-part7-periods: `reg 32(4): the days of residence in the continuous period up to and including the day` and helpers | an interval of 28 days is joined, 29 is not |
| reg 32(5) | src:490-493 | encoded | pip-part7-periods: `reg 32(4)(a) and (5): the interval between the periods does not exceed the limit` | one year where all the periods are section 87 periods; fork F-38 |
| signature line | src:494 | inert | none | pure citation or title: "Signed by authority of the Secretary of State for Work and Pensions." |
| Schedule 2 heading | src:636 | inert | none | pure citation or title: "SCHEDULE 2 - Members of Her Majesty's forces: excluded persons" |
| Sch 2 para 1 | src:637 | encoded | pip-sch2-forces: `Sch 2 para 1: the person is specified in Schedule 2` | fork F-18 |
| Sch 2 para 1(a) | src:638 | encoded | pip-sch2-forces: `Sch 2 para 1(a): ...` | subject to paragraph 2 |
| Sch 2 para 1(b) | src:639 | encoded | pip-sch2-forces: `Sch 2 para 1(b): ...` | |
| Sch 2 para 1(c) | src:640 | encoded | pip-sch2-forces: `Sch 2 para 1(c): ...` | |
| Sch 2 para 2 | src:641-646 | encoded | pip-sch2-forces: `Sch 2 para 2: paragraph 1(a) does not include the person` | |

## Fork register


Each entry: the readings seen, the one taken, and the text that licenses each.
The numbers are cited from the comments of the modules.

**F-1. Periods of months, and month-end dates** (reg 7(3), reg 8(2), regs 12 and 13; `pip-dates`).
Readings: (i) a period of N months ending with date X starts on the day after the corresponding date N months earlier, and a period of N months beginning with date Y ends on the day before the corresponding date N months later; where the corresponding date does not exist the last day of the shorter month is used; (ii) a calendar-month reading (start on the first of the month) for periods that end at a month-end.
Taken: (i), through the library's `add months`, which clamps to the last day of the shorter month.
Licence: the text says only "the period of 3 months ending with the prescribed date" and "the period of 9 months beginning with the day after the prescribed date" (src:76, 78); it gives no rule for a date such as 31 May less 3 months.
The two readings differ by one day at month-ends, for example a prescribed date of 28 May.
Reg 8(2) "within one month from the date of the request" (src:84) is read the same way: the last day is the corresponding date one month on, clamped (a request on 31 January gives 28 February in a non-leap year).
Asserted for 31 January.

**F-2. "Likely that the Secretary of State would have determined" is an input, not a computation** (regs 12 and 13; `pip-part3-required-period`).
Readings: (i) the person states the outcome the text calls "likely" at every time in each window; (ii) the encoding recomputes it from a daily score.
Taken: (i).
Licence: the text asks for what "it is likely that the Secretary of State would have determined" (src:106-110), a prediction of the Secretary of State's own determination; the guide's default is a conditional input for a judgment handed to someone else.

**F-3. "Subject to the following provisions of this Part" and the order in which Part 4 exceptions apply** (reg 16; `pip-part4-residence`).
See F-14 to F-18, which record each place where two exceptions meet.

**F-4. Reg 4(2): aids "normally worn" (a) "or" aids "reasonably expected" (b).**
Readings: (i) disjunctive per aid: an aid counts if C normally wears or uses it, or if C could reasonably be expected to; (ii) a choice between two ways of assessing the whole person, one for the whole assessment.
Taken: (i).
Licence: src:42-44 read "(a) on the basis of C's ability whilst wearing or using any aid or appliance which C normally wears or uses; or (b) as if C were wearing or using any aid or appliance which C could reasonably be expected to wear or use"; the two limbs name different aids ("any aid ... which C normally wears", "any aid ... which C could reasonably be expected to wear"), and a choice between them for the whole assessment would let the assessor ignore aids C already uses.

**F-5. Reg 4(2A): "only if" makes the four limbs necessary, not sufficient.**
Taken: the rule returns whether C may be assessed as satisfying a descriptor that turns on doing the activity; whether the descriptor is then satisfied stays a finding of fact.
Licence: "C is to be assessed as satisfying a descriptor only if C can do so" (src:45).

**F-6. Reg 7(1)(b) ties and reg 7(1)(c): which descriptors are added and chosen among.**
Readings of (c): (i) the descriptors added together, and the one chosen, are the descriptors other than a 0-point descriptor that are satisfied on at least one day; (ii) the one chosen may be any descriptor including a 0-point descriptor satisfied for more days; (iii) the sum may be taken over any subset of two or more.
Taken: (i).
Licence: src:71-73 speak of "two or more descriptors (other than a descriptor which scores 0 points)" and then of "the descriptor which is satisfied for the greater or greatest proportion", the descriptors just described; (iii) gives the same result as (i) since adding more descriptors only raises the sum.
Ties: where two descriptors that are each over 50%, or satisfied for the same proportion, also score the same points (for example 1b and 1c, both 2), the text does not choose; the first listed is taken, and the points are the same either way.
Days counted as if disjoint: "periods which, when added together" (src:71) is read as the plain sum of the days stated for each descriptor.

**F-7. No descriptor applies (reg 7(1) selects none).**
Readings: (i) the activity contributes 0 points; (ii) the score is not covered.
Taken: (ii), a `NOTHING`, asserted.
Licence: reg 7(1) lists three cases (src:69-73) and says nothing for a person satisfying no descriptor on over 50% of the days and fewer than two non-zero descriptors on over 50% together (for example two non-zero descriptors on 25% of the days each, which together are exactly 50% and not over it, or one non-zero descriptor on 30% of the days and a 0-point descriptor on exactly 50%); reg 5(1) says "points (if any)" (src:56) but does not say that an activity with no applicable descriptor scores 0.

**F-8. Reg 7(3)(a)(i) names regs 15 and 15A, not 15B; and its 9-month window starts on the claim date, where reg 15(2)(b) after substitution starts on the day after.**
Taken: each as the text states it.
Licence: src:77 ("for the purpose of regulation 15 or 15A", 9 months "beginning with the date on which that claim is made") against src:132, 144, 160 (the words "the prescribed date" in regs 12(1)(b) etc. are replaced by "the date on which the new claim ... is made", so the window begins with the day after that date).
A claim after an interval under reg 15B is therefore "any other claim" for reg 7(3)(a)(ii).
The one-day difference between reg 7(3)(a)(i) and the substituted reg 12(1)(b) is recorded; neither is changed to suit the other.

**F-9. Reg 7(3)(b)(i): "the period of 9 months beginning with the day after that date".**
Readings: (i) "that date" is each day of the award; (ii) "that date" is the prescribed date.
Taken: (i), because (b)(ii) uses the same words for "each day of the award" (src:81), and reg 15(3)(b) substitutes "each day of the award" (src:135).

**F-10. "Without good reason" (regs 8(3), 9(2)) and "the component to which the failure related".**
Taken: good reason is the Secretary of State's judgment, an input phrased as "the Secretary of State is satisfied that C had good reason"; reg 10 says what must be weighed.
The rule for reg 8(3) says that a negative determination must be made in relation to the component the request related to; which component that is is a fact the person states (the seat question names the component).

**F-11. Reg 10 "include".**
Taken: a floor: the rule is true for the two listed matters and false for any other, and the name says that false means "regulation 10 does not itself require it", not "excluded".

**F-12. Lists joined by "and" in the definitions of Schedule 1, Part 1.**
For "complex budgeting decisions", "simple budgeting decisions", "engage socially", "toilet needs", "take nutrition" (a) and "manage incontinence", the list names the parts of the defined term.
Readings: (i) a thing is within the term if it is any one of the parts; (ii) a thing is within the term only if it involves all of the parts.
Taken: (i) for the question "is this within the term"; whether C can do the whole of it unaided is for the descriptor.
Licence: src:507-510, 515-518, 519, 539-541, 546-548, 558-561 ("means -- (a) ...; (b) ...; and (c) ...").
For "basic written information" the "and" in "signs, symbols and dates" is read as the kinds the information may be.

**F-13. Reg 14(a): no date from which limited ability is likely to have been determined over the previous 3 months.**
Readings: (i) the prescribed date is the date of the claim; (ii) there is no prescribed date.
Taken: (i).
Licence: src:120 says "the date of that claim or, if later, the earliest date in relation to which ... it is likely", so the date of the claim is the floor; where the person cannot show an earlier-and-later date the date of the claim is the only date the sentence names.
The input is a maybe-date, and an earlier date than the claim date is ignored ("if later").
Asserted.

**F-14. Regs 14 to 15B: a new claim that meets the conditions of more than one of regs 15, 15A and 15B.**
Reg 14 applies "except where" paragraph (2) or (3) of reg 15, 15A or 15B applies (src:119); none of the three regulations says what happens if two apply (for example C had a previous child disability payment award and a previous personal independence payment award).
Taken: not covered, a named constructor of the provision-picker, asserted.
Nothing in regs 15, 15A or 15B excludes the others: reg 15(1)(b) takes a previous award of personal independence payment or adult disability payment, reg 15A(1)(b) one of child disability payment, reg 15B(1)(b) one of Scottish adult disability living allowance, and C may have had more than one of them ending within 2 years of the new claim.

**F-15. Reg 15(1)(b) and the other regs' "ended not more than 2 years before the date on which the new claim is made".**
Readings of an award that ended on or after the day of the new claim: (i) it is within the limb (the award ended "not more than 2 years before", and zero years before is not more than 2); (ii) it is outside the limb, since the award did not end before the claim.
Taken: the award ended on the day of the new claim is within; an award ending later is outside.
The text does not say; this is a choice at the boundary, asserted both sides.

**F-16. Reg 15(2)(a), (3)(a): the prescribed date "is the date on which the previous award ended where that award was in respect of PIP or ADP".**
The words after "where" are a condition on the previous award, already required by reg 15(1)(b) and (c); the encoding takes the date from the previous award without testing the condition again.

**F-17. Reg 15B(3)(a) says "Scottish disability living allowance" where reg 15B(1)(b) and (2)(a) say "Scottish adult disability living allowance".**
Taken: the same benefit (an evident slip; there is no other award in play in that paragraph).
Neither word is changed in the quotation.

**F-18. Schedule 2 refers to "paragraph (2)" and "Paragraph (1)(a)" though its paragraphs are numbered 1 and 2.**
Taken: paragraph 2 of the Schedule and sub-paragraph 1(a) of the Schedule (src:638, 641).
Licence: there is no other paragraph (2) or (1)(a) in the Schedule for them to mean; the Schedule as converted shows the numbers "1" and "2" without brackets.

**F-19. Reg 19(2)(a): "over the age of 16".**
Readings: (i) strictly over 16, that is from the day after the 16th birthday; (ii) aged 16 or over, that is from the birthday.
Taken: (i).
Licence: reg 15A(1)(c) says "aged 16 years or over" (src:141) where it means the birthday, so the two phrases are not synonyms in this text.
Asserted at the birthday and the day after.

**F-20. Reg 19(3), "aircraft worker" and "mariner": which alternative the "where (a) ... and (b) ..." qualifies.**
Readings: (i) the "where" qualifies only the second alternative, "in any other capacity on board"; (ii) it qualifies both, so that a pilot whose contract was entered into outside the United Kingdom is not an aircraft worker.
Taken: (i).
Licence: "where" follows directly after the second alternative (src:225, 229); limb (a) itself speaks of "that other capacity", which only the second alternative has.
Limb (b) ("the contract is entered into in the United Kingdom") does not mention the capacity, so reading (ii) is open.
The exclusion of a person in employment as a member of Her Majesty's forces applies to both alternatives under either reading.
Asserted for a crew member without the contract limb.

**F-21. Regs 18A and 18B beside 18C and 18D: the same rule with two different people who must be satisfied.**
The text has both pairs (src:193-212): regs 18A and 18B (the Secretary of State) and regs 18C and 18D (the Scottish Ministers).
Both are encoded, with distinct names, and an absence carries both satisfactions as separate facts.
`regs 17 to 18D: the first weeks of the absence for which C is treated as present` takes the longer of the two totals.

**F-22. Reg 23ZA treats limb (c) as "not satisfied"; regs 20, 23 and 23A(1A) deem it satisfied or say it "does not apply".**
Readings: (i) the later-numbered or more specific rule prevails; (ii) the text does not say.
Taken: (ii): `reg 16(c) as modified` returns NOTHING when reg 23ZA applies together with reg 20, with reg 23 (daily living component) or with reg 23A(1A), and the overall answer is the named "text does not say" outcome unless another limb already fails.
Licence: none of the four says it prevails over another; reg 23ZA(1) and (2) say "treated as not satisfied" (src:258-259), reg 23 says limbs "(a) to (c)" "do not apply" (src:249), reg 23A(1A) says limb (c) "does not apply" (src:344), reg 20 says "treated as habitually resident in Great Britain" (src:234).
Asserted.

**F-23. Reg 23A(1)(g)(i) says "residing in Sudan before 15 April 2023", where (f)(i) and (h)(i) say "immediately before".**
Taken: the input is worded as the text words it; the encoding does not decide whether "before" means at any earlier time or immediately before.
The person states the fact in the text's words; the seat question asks it in those words.

**F-24. Reg 23A(1)(i) and (j) are repeated as (k) and (l) (src:312-327 and 328-343).**
The two copies differ in numbering (Condition A has (a), (b) in the first and (i), (ii) in the second) and in small words ("immigration rules made under section 3(2) of that Act" against "immigration rules"), and each has its own 130-week paragraph, (1B) and (1C).
Both are encoded, with distinct names; C is covered if either applies.
The text shows no sign of which version is in force on a given day.

**F-25. "The first 13 weeks of absence" (reg 17(1)) and "the first 26 weeks" (regs 18, 18A, 18C).**
Taken: weeks are a number, the absence's first day is the first day of the first week, and an absence of exactly 13 (or 26) weeks is wholly within the period; more than that is not.
Licence: the text says "the first 13 weeks of absence" (src:183).
Asserted at 13 and 13.5, and at 26 and 26.5.

**F-26. Regs 18B and 18D: "the total period of an absence where C is treated as present ... will not exceed 26 weeks".**
Readings: (i) the periods under regs 17(1), 18(1) and 18A(1) all run from the start of the absence, so the total is the longest of them, and no more than 26 weeks; (ii) the periods add up, capped at 26.
Taken: (i).
Licence: each of those regulations treats C as present "for the first" N weeks of the absence, so they overlap from the first day; adding them would count the same weeks twice.
The cap is applied to one absence, not across all the absences in the look-back.

**F-27. Reg 16(b): the 104 weeks count weeks C was treated as present.**
Taken: weeks treated as present under regs 17 to 19 are added to the weeks actually present.
Licence: regs 17(1), 18(1), 18A(1) and 19(1) treat C as present "for the purposes of regulation 16(a) and (b)".

**F-28. Reg 23ZC(6) reads reg 16(a) as "Great Britain"; reg 16A still gives England and Wales as the relevant area for reg 16(a).**
Taken: the base presence test of limb (a) is read as presence in Great Britain for the decision on the ongoing claim; the "treated as present" rules of regs 17 to 20A still treat C as present in England and Wales, which includes presence in Great Britain.
The text does not say whether the substitution also changes the relevant area of reg 16A.

**F-29. Reg 23ZC(4): a day before 6 November 2025 is read "to the effect that the person must be present in England and Wales, or treated for the purposes of regulation 16(a) as being present in Great Britain".**
Taken: before 6 November 2025 the condition is C present in England and Wales, or C treated by regs 17 to 19 and the like as present in Great Britain; from 6 November 2025 it is C present in England and Wales or treated by a provision other than reg 23ZC as present in England and Wales (reg 23ZC(2)(c)).
Reg 23ZB(2) is read as treating C as present only on days of the run-on period, and only "insofar as" C is not present, which the OR of limb (a) already gives.

**F-30. Reg 23(b)(ii): "except where C has been habitually resident in the United Kingdom after 31st December 2020, applied to C on 31st December 2020 and ... continuously in receipt ... on and from that date".**
Taken: (ii) is met when a relevant EU Regulation applied to C on 31 December 2020, C has not been habitually resident in the United Kingdom on any day after 31 December 2020, and C's continuous receipt of the daily living component began on or before 31 December 2020.
Licence: the "except where" clause is read as qualifying the whole of the limb that follows, which then reads as the three conditions.
The alternative, where "except where" disapplies the limb only for the first of the three, does not fit the sentence.

**F-31. Reg 23ZB(3)(b) and reg 23ZC(7)(b): "due to expire before the end of the run-on period".**
Taken: a fixed term that expires on the last day of the run-on period is not due to expire before its end, and is not extended; one that expires on any earlier day is extended to the last day of the run-on period.
Asserted both sides.

**F-32. Reg 27(2) appears twice, once naming the Scottish Ministers and once the Secretary of State (src:382-387 and 388-393).**
Both are encoded, with distinct names; the first has "the supersession proceedings were initiated by the Scottish Ministers" and the second "by the Secretary of State".
The restrictions apply if either version's conditions are met; the person states which of them initiated the proceedings, so only one date is ever supplied.
The text shows no sign of which version is in force on a given day.

**F-33. Reg 27(3)(b): an original enhanced rate and a proposed standard rate.**
Reg 27(3)(b) says the Secretary of State "may only award that rate" (the enhanced rate) where entitlement results from substantially the same condition; it says nothing on whether a lower rate may be awarded when that condition is not met.
Taken: not covered (NOTHING), asserted.
Reg 27(3)(a) is complete for an original standard rate.

**F-34. Regs 30(1) and 31(1): "the first 28 days of any period".**
Taken: the days are the days of residence in the continuous period of reg 32(4), counted from the first day of the period of residence (the day after entry, reg 32(2)(a)); day 28 is within the first 28 days and day 29 is not.
Reg 30(2) and reg 31(2) take away that grace for the run of consecutive days beginning on the day entitlement commenced while the condition continues; the run is a fact the person states.
Asserted at days 28 and 29.

**F-35. Reg 26(2)(c): severely limited ability on the new claim, and no mobility rate under the previous award.**
Reg 26(2)(c)(i) allows the enhanced rate only if C had it under the previous award; (ii) allows the standard rate only if C had that rate under it.
Taken: a person with neither gets no rate of the mobility component by these exceptions.
Reg 26(2)(d) is read the same way for limited ability: the standard rate only if C had the component at either rate.
Asserted.

**F-36. Regulation 28(2) lists the "specified enactments" for section 85(2) of the Act; what else section 85(2) needs is the Act's.**
Taken: the care home condition is the conjunction of two facts the person states (qualifying services are provided to C in a care home; the costs are borne out of public or local funds under the enactment) and the classification of the enactment in reg 28(2).
The seven enactments excepted from (f) are constructors that answer FALSE; "any other enactment relating to persons under a disability ..." answers TRUE; everything else answers FALSE.

**F-37. Reg 31(6)(b): "in similar circumstances in Great Britain, C would have been excepted".**
Taken: the person states whether C would have been excepted by a provision of reg 31; the encoding does not recompute the exception for a foreign custody.

**F-38. Reg 32(4) with (5): the interval between periods.**
Taken: the interval is the days between the last day of the earlier period and the first day of the later one; 28 days is joined and 29 is not; where (5) applies, "one year" is a year from the first day of the interval (the day after the earlier period ends), so a later period beginning exactly a year after that day is joined and one beginning a day later is not.
Asserted both sides.

**F-39. Regulation 26(1) applies where C "makes a new claim in the circumstances set out in regulation 15", and regulation 15(1)(b) is the provision whose "2 years" regulation 26(2)(b) then reads as "1 year"** (regs 15, 26, 15B, 26A; `pip-part6-age`, `pip-seat`).
Readings: (i) take the circumstances of reg 15 as they stand with 2 years, then apply the exceptions of reg 26(2): for a claim made between 1 and 2 years after the award ended, the claim is in the circumstances of reg 15, so the exceptions apply, so the years become 1, so the claim is not in the circumstances of reg 15, so the exceptions do not apply: there is no stable answer; (ii) read the number of years as 1 for a person who has reached the relevant age and 2 for a person who has not.
Taken: (ii).
The layer-1 rule `reg 15(1): regulation 15(2) and (3) apply to the new claim` takes the number of years as an input; the seat passes `reg 26(2)(b): the number of years in regulation 15(1)(b)` applied to `reg 26(1): the exceptions of regulation 26(2) apply` with the age and TRUE for "makes a new claim in the circumstances set out in regulation 15".
The same is done for reg 15B and reg 26A.
Licence: only (ii) leaves reg 26(2)(b) and reg 26A(2)(b) any work to do; the text says "the following exceptions apply" and cannot have meant a rule with no fixed point.
Asserted at exactly 1 year (the claim is within reg 15) and 1 year and a day (it is not), for a person who has reached the relevant age, in `pip-cases-seat.l4`.

**F-40. The seat applies both versions of regulation 23A(1)(i), (j) and (k), (l) to the same answers, and gives regulation 27(2) a question for each version** (seat).
The two versions of 23A(1)(i), (j) and (k), (l) differ in the numbering of their sub-paragraphs and in a few words (fork F-24), so the seat's single question on reg 23A takes one set of facts and is true if either version is satisfied.
The two versions of reg 27(2) differ in who initiated the supersession (the Scottish Ministers, the Secretary of State; fork F-32), a fact the claimant states, so there is a question for each.
Assumed, not ruled; reverting it changes `pip-seat.l4` only.

**F-41. The seat's question on regulation 7(1) takes three descriptors of an activity, each a letter and the number of days on which it applies** (seat).
The layer-1 rules take any list of descriptors with their days; the seat takes three, so a claimant with four or more descriptors that apply on some days cannot ask the question as it stands.
A letter that names no descriptor of the activity (for example letter g of mobility activity 2, which has a to f) and is given more than 0 days makes the question return NOTHING, not a score worked out from the other descriptors; a letter that names none with 0 days is padding and is ignored.
Asserted (three cases).
Assumed, not ruled.

**F-42. The seat's question on regulation 32(4) takes at most three periods of residence** (seat).
The layer-1 rule takes any list.
Assumed, not ruled.

## Dependencies on instruments outside the text

| your provision | the provision it depends on | the input you made |
|---|---|---|

Judgments handed to the Secretary of State (good reason, "likely ... would have determined", "satisfied that ... unreasonable", "determines that the entitlement results from the same condition") are not instruments and are listed in the Seat section, not here.
The Welfare Reform Act 2012 ("the Act" in the text) is not among the inputs.
Every row below is a place where the text names something outside itself and the encoding takes the outcome as a plain input, a named choice, or carried text.

| your provision | the provision it depends on | the input you made |
|---|---|---|
| reg 1(2) (commencement) | Welfare Reform Act 2012 Part 4 and the orders bringing it into force | `reg 1(2): these Regulations are in force in the case on` takes the day Part 4 comes into force for the case |
| reg 2 "revised", "superseded" | Social Security Act 1998 ss 9, 10 | carried as text in `reg 2: a decision on an award is revised` and `reg 2: a decision on an award is superseded` |
| reg 2 "adult disability payment", "child disability payment", "Scottish adult disability living allowance", "disability living allowance" | Disability Assistance for Working Age People (Scotland) Regulations 2022 reg 2; the Scottish regulations of 2021 and 2025; the Social Security Contributions and Benefits Act 1992 | the enum `the benefit paid under an earlier award` |
| reg 2 "the Act", "the 1998 Act" | Welfare Reform Act 2012; Social Security Act 1998 | none (names carried as text) |
| reg 3(1) | Welfare Reform Act 2012 s 78(4) | none (the activities come from Schedule 1) |
| reg 3(2) | Welfare Reform Act 2012 s 79(4) | none (the activities come from Schedule 1) |
| reg 4(1) | Welfare Reform Act 2012 ss 77(2), 78, 79 | the input `the limitation is a result of C's physical or mental condition` |
| reg 9(4) | Electronic Communications Act 2000 s 15(1) | the inputs `the notice was sent by electronic communication` and `C had agreed to accept correspondence by electronic communication` |
| reg 12(1), 12(2) | Welfare Reform Act 2012 s 78(1), (2) | the pairing of a rate with a regulation is carried from the parentheticals of regs 12(1) and 12(2) |
| reg 13(1), 13(2) | Welfare Reform Act 2012 s 79(1), (2) | the same for the mobility component |
| reg 15A(5) | Disability Assistance for Children and Young People (Scotland) Regulations 2021 reg 36 | the input `the new claim is made during the 13 week period provided for in regulation 36` |
| reg 15B(6) | Disability Assistance (Scottish Adult Disability Living Allowance) Regulations 2025 reg 48 | the input `the new claim is made during the 13 week period provided for in regulation 48` |
| regs 15(1), 15B(1) "previous award" | the awards of the benefits listed in reg 2 | the enum `the benefit paid under an earlier award`, and the days on which the awards ended |
| reg 16(d) | Immigration and Asylum Act 1999 s 115(9); Social Security (Immigration and Asylum) Consequential Amendments Regulations 2000 reg 2 | two inputs, one for each limb |
| reg 19(2) | Armed Forces Act 2006 s 374 ("the regular forces", "the reserve forces") | the input `the person is a member of the regular forces or the reserve forces as defined in section 374 of the Armed Forces Act 2006` |
| reg 19(1)(b) | Social Security Contributions and Benefits Act 1992 s 120 and the regulations prescribing continental shelf employment | the input `C is in employment prescribed for the purposes of section 120 of the Social Security Contributions and Benefits Act 1992 in connection with continental shelf operations` |
| reg 21, reg 30(3) | Welfare Reform Act 2012 s 82 ("terminally ill") | the input `C is terminally ill` |
| regs 22, 23 | what a "relevant EU Regulation" is; what a "genuine and sufficient link" is; the list of EEA states | the inputs `a relevant EU Regulation applies`, `C can demonstrate a genuine and sufficient link to the United Kingdom`, and the enum `a place of habitual residence` |
| reg 23(b)(ii) | whether a relevant EU Regulation applied on 31 December 2020 | the input `a relevant EU Regulation applied to C on 31 December 2020` |
| reg 23A(1)(a) to (e) | the immigration rules (Immigration Act 1971 s 3(2)); refugee status; humanitarian protection; the Afghan Relocations and Assistance Policy; the Afghan Citizens Resettlement Scheme | one input for each status |
| reg 23A(1)(f) to (l) | Immigration Act 1971 ss 2 (right of abode), 3(2), 3ZA | the inputs for leave, right of abode and no leave required |
| reg 23ZA(1) | Disability Assistance for Children and Young People (Scotland) Regulations 2021 reg 36(1) | the input `regulation 36(1) of the Disability Assistance for Children and Young People (Scotland) Regulations 2021 applies to C` and `the day is within the period set out in regulation 36(1) of those Regulations` |
| reg 23ZA(2) | Disability Assistance for Working Age People (Scotland) Regulations 2022 reg 53(1) | the input `regulation 53(1) of the Disability Assistance for Working Age People (Scotland) Regulations 2022 applies to C` and `the day is within the period set out in regulation 53(1) of those Regulations` |
| reg 23ZC(3), (5) | Social Security Act 1998 s 8; Universal Credit, Personal Independence Payment, Jobseeker's Allowance and Employment and Support Allowance (Claims and Payments) Regulations 2013 reg 31 | three inputs for the ways a claim can stop being ongoing, and `C withdraws the claim in accordance with regulation 31 of the Claims and Payments Regulations` |
| reg 23ZC(8)(b) | Claims and Payments Regulations 2013 reg 12 (the date of a claim) | carried as text in `reg 23ZC(8): definitions`; the date of the claim is an input |
| reg 24 | Welfare Reform Act 2012 s 78(3), 79(3) | none (the amounts come from the text) |
| regs 25, 26, 26A, 27 "the relevant age" | Welfare Reform Act 2012 s 83 | the input `C has reached the relevant age` and the day C reached it |
| reg 27(2) | Decisions and Appeals Regulations 2013 regs 23 and 26(1)(a) | the inputs `the award is superseded pursuant to regulation 23 of the Decisions and Appeals Regulations` and `the award is superseded pursuant to regulation 26(1)(a) of the Decisions and Appeals Regulations`; `reg 27(2A): the Decisions and Appeals Regulations` carries the name as text |
| reg 28 | Welfare Reform Act 2012 s 85 | the input `C meets the condition in section 85(2) of the Act` and its parts |
| reg 28(2) | the enactments listed in reg 28(2) (National Assistance Act 1948 Part 3; Social Work (Scotland) Act 1968 ss 59, 59A; Mental Health Act 1983; Community Care and Health (Scotland) Act 2002; Mental Health (Care and Treatment) (Scotland) Act 2003; Health and Social Care Act 2001 s 57; Care Act 2014 Part 1; Social Services and Well-being (Wales) Act 2014 Part 4; the Education Acts and Higher Education Acts named in (f)) | the enum `an enactment under which qualifying services may be provided` |
| reg 28(3) | Children Act 1989 s 17(10); Children (Scotland) Act 1995 s 93(4)(a); Social Services and Well-being (Wales) Act 2014 ss 37, 38, 42; Education Act 1996 s 320; Education (Additional Support for Learning) (Scotland) Act 2004 s 25 | one input for each |
| reg 29 | Welfare Reform Act 2012 s 86 | the input `C meets the condition in section 86(2) of the Act` |
| reg 29(2) | National Health Service Act 2006; National Health Service (Wales) Act 2006; National Health Service (Scotland) Act 1978 | the enum `an institution in which C is an in-patient` |
| reg 30(4) | National Health Service Act 2006 s 275; National Health Service (Scotland) Act 1978 s 108(1); National Health Service (Wales) Act 2006 | one input for each of (a) to (e) |
| reg 30(6) | National Health Service (Wales) Act 2006 ss 11, 18 | carried as text in `reg 30(6) and (7): definitions` |
| reg 30(7) | Charities Act 2011 s 7 | carried as text in `reg 30(6) and (7): definitions` |
| reg 31 | Welfare Reform Act 2012 s 87 | the input `section 87 of the Act applies to C on the day` |
| reg 31(4) | Mental Health Act 1983 ss 45A, 47, 50(3); Criminal Procedure (Scotland) Act 1995 s 59A; Mental Health (Care and Treatment) (Scotland) Act 2003 s 136 | one input for each, and the certified release date |
| Sch 2 para 2 | National Insurance Act 1965 Part 1 | the input `the person has previously been an insured person under Part 1 of the National Insurance Act 1965` |

The `-- out of text:` comments in the modules number 26; they are the source of the first columns above.

## What the text turns out to say


Each finding ends "Asserted." where a case or test asserts it, and says so where it does not.

1. **Regulation 7(1)(c) does not count a descriptor that scores 0 points towards the over-50% total.**
A claimant who satisfies a 0-point descriptor on 100 of 365 days and a 2-point descriptor on 90 days has two descriptors satisfied for 190 days, but only one is a scoring descriptor, so none of (a), (b) or (c) applies and the text gives the activity no points.
Asserted (`pip-cases-seat.l4`, activity 9; `pip-tests-part2.l4`).
2. **The text does not say what happens when no descriptor of an activity applies under regulation 7(1).**
Regulations 5(2) and 6(2) take "whichever of the descriptors ... applies to C under regulation 7"; regulation 7 can select none (for example one descriptor satisfied on 182 of 365 days, which is not over 50%).
The encoding returns NOTHING for the activity's points and for any score that depends on it (fork F-7).
Asserted.
3. **Regulation 26 contains a circular reference to regulation 15** (fork F-39): on a literal reading a claim made between 1 and 2 years after an award ended has no stable answer.
Asserted (the 1 year boundary, both sides).
4. **Regulation 7(3)(a)(i) and regulations 15(2)(b), 15A(2)(b) and 15B(2)(b) disagree by one day about when the 9 months begin on a claim after an interval**: regulation 7(3)(a)(i) says the 9 months begin with the date of the claim; the substitution in regulation 12(1)(b) and the others produces "the 9 months beginning with the day after" that date (fork F-8).
Regulation 7(3)(a)(i) also names regulations 15 and 15A but not 15B.
Asserted (the required period of 366 days for a claim after an interval; the question on the 9 months).
5. **Nothing says what happens when a new claim meets the conditions of more than one of regulations 15, 15A and 15B** (fork F-14).
Asserted (the "more than one ... applies" value).
6. **Regulation 23ZA treats regulation 16(c) as "not satisfied", while regulations 20, 23 and 23A(1A) deem it satisfied or say it "does not apply", and the text does not say which prevails** (fork F-22).
Asserted (NOTHING for limb (c), and "the text does not say whether the conditions of regulation 16 are met" for regulation 16 as a whole).
7. **The deposited text carries three provisions twice.**
Regulation 23A(1)(i), (j) is repeated as (k), (l) with different sub-paragraph numbering; regulation 27(2) appears with "the Scottish Ministers" and again with "the Secretary of State" in (b)(ii); regulations 18A and 18B appear beside 18C and 18D with "the Secretary of State" and "the Scottish Ministers" as the person who must be satisfied (forks F-24, F-32, F-21).
Both versions of each are encoded under separate names.
Asserted (each version, in `pip-tests-part4-special-cases.l4`, `pip-tests-part5-6.l4` and `pip-tests-part4-residence.l4`).
8. **Regulation 27(3)(b) is silent on a standard-rate proposal after an enhanced-rate original award**, where (a) covers a standard-rate original and (b) an enhanced-rate original awarded the same rate only (fork F-33).
Asserted (NOTHING).
9. **Regulation 15B(3)(a) says "Scottish disability living allowance" where regulations 15B(1)(b) and 15B(2)(a) say "Scottish adult disability living allowance"** (fork F-17).
Read as the same benefit.
Not asserted.
10. **"Over the age of 16" in regulation 19(2)(a) is read strictly**: a member of the forces is not over 16 on the 16th birthday (fork F-19).
Asserted (the birthday and the day after).
11. **"Within one month from the date of the request" (regulation 8(2)) has no rule for a request on 31 January**; read with the library's `add months`, the last day is 28 February (fork F-1).
Asserted.
12. **Regulations 23ZB and 23ZC only reach a person who becomes permanently resident in Scotland on or after 6 November 2025, and regulation 23ZC(4) reads the presence condition differently for a day before that date.**
Asserted (5 and 6 November 2025, and the 13 week run-on period, 1 December 2025 to 1 March 2026).
13. **The "first 28 days" of regulations 30(1) and 31(1) are counted from the first day of the period of residence (the day after entry, regulation 32(2)(a)), and regulations 30(2) and 31(2) take the grace away from a person already in the care home, hospital or custody when entitlement commenced** (fork F-34).
Asserted (days 28 and 29, and the run beginning with the day entitlement commenced).
14. **Regulation 32(4) joins periods separated by not more than 28 days, and regulation 32(5) makes the limit one year where both periods are periods to which section 87 applies** (fork F-38).
Asserted (an interval of 28 days joins, of 29 does not; a gap of about ten months joins only under section 87).
15. **Regulations 18B and 18D ("will not exceed 26 weeks") are read as a cap on the longest of the periods, not on their sum** (fork F-26).
Asserted.
16. **Regulation 26(2)(c) and (d) give a claimant with no mobility rate under the previous award no mobility rate on a new claim after the relevant age, whatever level of ability is found** (fork F-35).
Asserted.
17. **Regulation 14(a) gives no date when it is not likely that limited ability would have been found at every time in the previous 3 months**; the encoding takes the date of the claim (fork F-13).
Asserted.
18. **The input SECTION-INDEX.txt lists 42 of the text's 45 regulations**: it omits regulations 23ZA, 23ZB and 23ZC.
The index says the text is authoritative; the coverage table has a row for every one of the 45.
Not asserted (a property of the inputs, not of the law).
19. **No assertion fails.**
The one recorded correction of an expected value is an addition slip of mine in `pip-tests-part2.l4` (a total of 76 where the descriptors add up to 84), corrected there with a note.

## What the stable binary does not accept


The stable build 1.6.98 (dialect `main`) was the only binary used.
These are the places where it refused, or answered in a way that cost work, while this encoding was written; there may be others.
Items 1 and 2 were reproduced in probe files before this section was written; items 3 to 5 were read off the runs of this folder.

Loud (an error or a warning is printed):
1. **A name that the prelude or `daydate` already defines cannot be used once the module defines it too.**
`id` (prelude) and `the day after` (`daydate`) each give "There are multiple definitions for the identifier ... and I do not have sufficient information to make a choice between them".
No module here defines either; `pip-dates` uses the library's `the day after`, and the names of every module are unique across the folder (the seat imports all of them).
2. **`AND` and `OR` at the same indentation column draw a linter Warning**: "AND and OR operators appear at the same indentation level".
The brief counts a warning as a failure, so every such rule is split with a helper rule.
Three layouts do not warn and were checked: a group in brackets on each of two lines under an `OR`, a one-line `(a AND b) OR (c AND d)`, and `a AND (b OR c)` with the second operator nested deeper.

Silent (exit 0, nothing printed):
3. **`check.sh` prints errors, satisfied, failed and refused, but not warnings.**
A linter warning in a module does not show in its table.
To see them, run `l4 run FILE 2>&1 | grep -c 'Severity: DiagnosticSeverity_Warning'` over every `pip-*.l4` (the total is 0), and `l4 check FILE` over every module (each prints "Check succeeded", with no diagnostic matching `is at the end of the file` or `follows code on its line`).

4. **`python3 -I srcrefs.py check --strict` reports problems on this folder; `--refs` reports none.**
`--strict` asks that the `@ref` locators of a block reach exactly the lowest and the highest raw line that the block quotes; many blocks here quote a regulation's heading or a shared lead-in line above a rule whose `@ref` cites only the lines it rests on.
The brief asks for `--refs`; `--strict` is not claimed.
5. **Month and year arithmetic is the library's `add months` and `add years`**, which clamp to the last day of a shorter month; there is no other convention to choose, and the text gives none (fork F-1).

## What check.sh prints

Run as `L4=<the stable 1.6.98 binary> L4_TARGET=unstable ./check.sh` in this folder (the word `unstable` only tells the script not to compare with a second binary).
stderr:

```
check.sh: the target is unstable, so the main check was skipped.
```

stdout, verbatim:

```
module                                    errors satisfied  failed  refused  expected
pip-cases-seat.l4                              0       453       0        0         0
pip-dates.l4                                   0         0       0        0         0
pip-nouns.l4                                   0         0       0        0         0
pip-part1-general.l4                           0         0       0        0         0
pip-part2-assessment.l4                        0         0       0        0         0
pip-part3-required-period.l4                   0         0       0        0         0
pip-part4-residence.l4                         0         0       0        0         0
pip-part4-special-cases.l4                     0         0       0        0         0
pip-part5-rates.l4                             0         0       0        0         0
pip-part6-age.l4                               0         0       0        0         0
pip-part7-payability.l4                        0         0       0        0         0
pip-part7-periods.l4                           0         0       0        0         0
pip-sch1-daily-living-table.l4                 0         0       0        0         0
pip-sch1-definitions.l4                        0         0       0        0         0
pip-sch1-mobility-table.l4                     0         0       0        0         0
pip-sch2-forces.l4                             0         0       0        0         0
pip-seat.l4                                    0         0       0        0         0
pip-tests-part1.l4                             0        34       0        0         0
pip-tests-part2.l4                             0       144       0        0         0
pip-tests-part3.l4                             0        96       0        0         0
pip-tests-part4-residence.l4                   0       157       0        0         0
pip-tests-part4-special-cases.l4               0       212       0        0         0
pip-tests-part5-6.l4                           0        83       0        0         0
pip-tests-part7-payability.l4                  0       117       0        0         0
pip-tests-part7-periods.l4                     0        39       0        0         0
pip-tests-sch1-definitions.l4                  0       128       0        0         0
pip-tests-sch1-tables.l4                       0       149       0        0         0
pip-tests-sch2.l4                              0        21       0        0         0
TOTAL (28 modules)                             0      1633       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

The 28 modules are the 16 rule modules (no assertions), 11 test files and `pip-cases-seat.l4`: 453 + 34 + 144 + 96 + 157 + 212 + 83 + 117 + 39 + 128 + 149 + 21 = 1633 assertions, all satisfied; no assertion failed or was refused, and no file is meant to fail (the `expected` column is 0 throughout).

## Before this is worth relying on


1. **Check the text against the official one.**
The deposited text is a converter's plain-text rendering of the revised text of 2026-04-30, not the official text.
It may carry more than one extent version of a provision (it does: regulations 18A to 18D, 23A(1)(i) to (l) and 27(2)), words marked repealed but still shown, and prospective provisions that it does not distinguish.
2. **One outstanding effect is not applied.**
The metadata lists an effect on the Schedule 1 Part 3 table (mobility activities): "words substituted" by the Social Security (Personal Independence Payment) (Amendment) Regulations 2017 reg. 2(4), in force 2017-03-16.
The deposited text does not say what the substituted words are, and this encoding does not guess; if the table in the deposited text predates the substitution, the descriptors of activities 1 and 2 of Part 3 need checking against the in-force text.
3. **The Welfare Reform Act 2012 is not encoded.**
Sections 77 to 79 (entitlement, rates), 82 (terminal illness), 83 (the relevant age), 85 to 87 (care homes, hospitals, prisoners) and the Social Security Act 1998 are inputs; whether a person is entitled at all needs them.
4. **A lawyer should rule on the forks.**
42 forks are registered; the ones that change an answer are F-7 (no descriptor applies), F-14 (overlap of regs 15, 15A, 15B), F-17 (the "Scottish disability living allowance" slip), F-22 (reg 23ZA against regs 20, 23, 23A(1A)), F-24 and F-32 (duplicated provisions), F-33 (reg 27(3)(b)), F-39 (the circular reference between regs 15 and 26), and F-1 (month ends).
5. **The cases were written by the author of the rules.**
Each expected value was worked out from the text before the file was run, but by the same hand that chose the readings, so a wrong reading is asserted wrongly twice; nobody else has run an independent test pass.
6. **The rates (regulation 24) are those of the deposited version.**
The text gives four amounts and no date from which they run; amending regulations have changed them before.
7. **The seat limits** (three descriptors in the question on regulation 7(1), three periods in the question on regulation 32(4); forks F-41 and F-42) mean a claimant with more cannot ask those two questions as they stand.
8. **The seat has not been put through the Interact form or the pipeline**; only the binary has run it.
9. **`--strict` source-locator checking does not pass** (see "What the stable binary does not accept"); `--refs` does.
10. **Dates before the version.**
The encoding answers for the text as of 2026-04-30; a question about an earlier day is only as good as the text for that day, and the deposited text does not show how it read before.

## Checked after the run

This section was added by the session that ran the agent, after the run; the sections above are the agent's.

- `L4=<L4_BIN> L4_MAIN=<L4_BIN> ./check.sh` in this folder, with `JL4_LIBRARY_PATH` unset, on the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19): `TOTAL (28 modules) 0 1633 0 0 | 0 1633 0 0`; exit status 0; every main column reads `same`.
  The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
  The agent ran `check.sh` with `L4_TARGET=unstable`, as its brief said, so the output printed above under "What check.sh prints" is from that run.
- `srcrefs.py check --refs` against `../../registers/source-bundle/uksi-2013-377.txt`: `srcrefs check: 621 src: lines, 272 runs, 347 locators, 0 problems`.
- `srcrefs.py check --strict`: `srcrefs check: 621 src: lines, 272 runs, 347 locators, 66 problems`. These findings are counted here and have not been reviewed one by one.
- 80 `@export` seat questions; 239 coverage rows (216 encoded, 0 fork, 22 inert, 1 repealed or blank).
- Paths in the agent's files that named its run folder (`inputs/...`) were rewritten on copying to name the deposited text in `../../registers/source-bundle/`; the agent's brief is kept verbatim as `BRIEF.md`, and the paths in it are the run's own.
- The agent ran `git -C <the reference checkout> status --short` once, to confirm it had added nothing to git; the lead's transcript scan found it. It read no file of any encoding.
