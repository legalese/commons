# Notes for the pieces: the Universal Credit Regulations 2013 (S.I. 2013/376), regulation 2 and the shared vocabulary

Written by the keel agent `uc-g0`.
This file is the guide that uc1, uc2, uc3 and uc4 read before they import anything.

**The source is a plain-text rendering, not the official text.**
`../../registers/source-bundle/uksi-2013-376.txt` was made by a converter script from the revised text on legislation.gov.uk (version 2026-07-16).
It is not marked up and it is not the official text; nothing in this encoding has been verified against the official text.
Every `-- src:N | ...` line in the modules copies line N of that file, mechanically, with `srcrefs.py quote`.

**The seat** is a person who claims or receives Universal Credit, alone or as one of a couple, asking whether they are entitled to it, how much, and what they must do or tell the Secretary of State.
The keel writes no seat layer and no `@export`.

**The parent Act is not an input.**
The Welfare Reform Act 2012 and the other Acts and instruments that regulation 2 cites are not among the inputs, so where a rule depends on one of them, its effect is a stated input: a BOOLEAN, or the core’s enumeration, named for the fact.

**Dates.**
My range (lines 12-117) contains no made, commencement or in-force provision: the title block (lines 3-4) and regulation 1 are uc1’s.
The keel does nothing about dates of enactment or commencement.

**Unapplied effects.**
The deposit’s metadata lists 12 outstanding effects: ten against the table of contents and two against regulation 99(6)(a) and (b); none names regulation 2.
It also records 4 prospective unapplied effects without saying which provisions they touch; the text may therefore carry wording that is not yet, or no longer, in force without marking it.

**Files.**
The modules are `uc-core.l4` (the core) and `uc-core-persons.l4`, `uc-core-bodies.l4`, `uc-core-payments.l4` (regulation 2’s definitions that can be worked out from facts), each with a `uc-core-tests-<topic>.l4` beside it (`uc-core-tests-core.l4` tests the core).

## Vocabulary

Every type, enumeration constructor, record field and rule in `uc-core.l4`, one row each.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Claim basis` | enumeration | how a claim is made | reg 3(3) (line 123); reg 22(3) (line 474); reg 78(2) (lines 1268-1270) |
| `a single claimant` | constructor of `Claim basis` | one person claims and is not a member of a couple | reg 3(3), reg 22(3), reg 78(2) |
| `joint claimants` | constructor of `Claim basis` | the two members of a couple claim together | reg 3(3), reg 22(3), reg 78(2) |
| `a single claimant who is a member of a couple` | constructor of `Claim basis` | a member of a couple who claims as a single person, in the cases of regulation 3(3) | reg 3(3), reg 22(3), reg 78(2) |
| `Nation of Great Britain` | enumeration | the three nations by which regulation 2 sorts foster parent, local authority and others | reg 2, lines 49-51 |
| `England` | constructor of `Nation of Great Britain` | the nation | reg 2, lines 49-51 |
| `Wales` | constructor of `Nation of Great Britain` | the nation | reg 2, lines 49-51 |
| `Scotland` | constructor of `Nation of Great Britain` | the nation | reg 2, lines 49-51 |
| `Benefit` | enumeration | a benefit or payment that regulation 2 names; a fact "is entitled to" or "is receiving" is a LIST OF Benefit | reg 2, lines 17-116 |
| `adult disability payment` | constructor of `Benefit` | the payment that regulation 2 of the Disability Assistance for Working Age People (Scotland) Regulations 2022 defines | reg 2, line 17 |
| `attendance allowance` | constructor of `Benefit` | five kinds of payment (lines 18-24); the limbs are tested by `reg 2 — attendance allowance` in uc-core-payments.l4 | reg 2, line 18 |
| `carer's allowance` | constructor of `Benefit` | a carer's allowance under section 70 of the Contributions and Benefits Act | reg 2, line 28 |
| `carer support payment` | constructor of `Benefit` | the carer support payment component of carer support under the Carer’s Assistance (Carer Support Payment) (Scotland) Regulations 2023 | reg 2, line 30 |
| `child disability payment` | constructor of `Benefit` | the payment that regulation 2 of the DACYP Regulations defines | reg 2, line 31 |
| `disability living allowance` | constructor of `Benefit` | an allowance under section 71 of the Contributions and Benefits Act | reg 2, line 41 |
| `employment and support allowance` | constructor of `Benefit` | an allowance under Part 1 of the Welfare Reform Act 2007 as amended | reg 2, line 44 |
| `industrial injuries benefit` | constructor of `Benefit` | a benefit under Part 5 of the Contributions and Benefits Act | reg 2, line 59 |
| `jobseeker's allowance` | constructor of `Benefit` | an allowance under the Jobseekers Act 1995 as amended | reg 2, line 61 |
| `maternity allowance` | constructor of `Benefit` | a maternity allowance under section 35 or 35B of the Contributions and Benefits Act | reg 2, line 75 |
| `Scottish adult disability living allowance` | constructor of `Benefit` | the allowance that regulation 2 of the Disability Assistance (Scottish Adult Disability Living Allowance) Regulations 2025 defines | reg 2, line 80 |
| `statutory paternity pay` | constructor of `Benefit` | statutory paternity pay under Part 12ZA of the Contributions and Benefits Act (the line shows repealed words as "...") | reg 2, line 81 |
| `pension age disability payment` | constructor of `Benefit` | the payment that regulation 2 of the Disability Assistance for Older People (Scotland) Regulations 2024 defines | reg 2, line 84 |
| `personal independence payment` | constructor of `Benefit` | an allowance under Part 4 of the Welfare Reform Act 2012 | reg 2, line 85 |
| `statutory adoption pay` | constructor of `Benefit` | a payment under Part 12ZB of the Contributions and Benefits Act | reg 2, line 98 |
| `statutory maternity pay` | constructor of `Benefit` | a payment under Part 12 of the Contributions and Benefits Act | reg 2, line 99 |
| `statutory neonatal care pay` | constructor of `Benefit` | a payment under Part 12ZE of the Contributions and Benefits Act | reg 2, line 100 |
| `statutory parental bereavement pay` | constructor of `Benefit` | statutory parental bereavement pay payable in accordance with Part 12ZD of the Contributions and Benefits Act | reg 2, line 101 |
| `statutory shared parental pay` | constructor of `Benefit` | statutory shared parental pay payable in accordance with Part 12ZC of the Contributions and Benefits Act | reg 2, line 102 |
| `statutory sick pay` | constructor of `Benefit` | a payment under Part 11 of the Contributions and Benefits Act | reg 2, line 103 |
| `war disablement pension` | constructor of `Benefit` | any retired pay, pension or allowance payable in respect of disablement under an instrument specified in section 639(2) of ITEPA; tested by `reg 2 — war disablement pension` in uc-core-payments.l4 | reg 2, line 112 |
| `widowed mother's allowance` | constructor of `Benefit` | an allowance under section 37 of the Contributions and Benefits Act | reg 2, line 114 |
| `widowed parent's allowance` | constructor of `Benefit` | an allowance under section 39A of the Contributions and Benefits Act | reg 2, line 115 |
| `widow's pension` | constructor of `Benefit` | a pension under section 39 of the Contributions and Benefits Act | reg 2, line 116 |
| `Element of an award` | enumeration | the amounts that make up an award | reg 23(1) and (2), lines 499-508 |
| `standard allowance` | constructor of `Element of an award` | section 9 of the Act | reg 23, line 500 |
| `child element` | constructor of `Element of an award` | regulation 24 (uc1) | reg 23, line 501; reg 2 line 33 |
| `housing costs element` | constructor of `Element of an award` | regulation 25 (uc1) | reg 23, line 502; reg 2 line 57 |
| `LCWRA element` | constructor of `Element of an award` | regulation 27 (uc1) | reg 23, line 506; reg 2 line 73 |
| `carer element` | constructor of `Element of an award` | regulation 29 (uc1) | reg 23, line 507; reg 2 line 29 |
| `childcare costs element` | constructor of `Element of an award` | regulation 31 (uc1) | reg 23, line 508; reg 2 line 32 |
| `Work-related group` | enumeration | the groups of claimants that sections 19 to 22 of the Act sort claimants into, named as regulation 90 names them | reg 12, line 330 (uc1); reg 62, line 1061 (uc2); reg 90(1) and (2), lines 1412-1415 (uc4) |
| `subject to no work-related requirements` | constructor of `Work-related group` | section 19 of the Act | reg 90, line 1412 |
| `subject to work-focused interview requirement only` | constructor of `Work-related group` | section 20 of the Act | reg 90, line 1414 |
| `subject to work-preparation requirement` | constructor of `Work-related group` | section 21 of the Act | reg 90, line 1414 |
| `subject to all work-related requirements` | constructor of `Work-related group` | section 22 of the Act | reg 90, line 1415 (and regulations 12 and 62, lines 330 and 1061, which ask only about section 22) |
| `Capability for work` | record | what Part 5 decides about a claimant (uc4 decides it; the other pieces read it) | regs 38, 39(1), 40(1), 40A(1), lines 745-785 |
| `limited capability for work` | field of `Capability for work` (BOOLEAN) | regulation 39 | Part 5 |
| `limited capability for work and work-related activity` | field of `Capability for work` (BOOLEAN) | regulation 40 | Part 5 |
| `severe conditions criteria claimant` | field of `Capability for work` (BOOLEAN) | regulation 40A | Part 5 |
| `Assessment period` | record | the month for which an award is worked out; regulation 21 (uc1) says how one is found | reg 21(1), line 432 |
| `first day` | field of `Assessment period` (DATE) | the first day of the period | reg 21(1) |
| `last day` | field of `Assessment period` (DATE) | the last day of the period, itself inside it | reg 21(1) |
| `Unit of time` | enumeration | the unit of a time limit | reg 4, line 149; reg 11, line 289 |
| `days` | constructor of `Unit of time` | a number of days | reg 4, reg 11 (and the text generally) |
| `weeks` | constructor of `Unit of time` | a number of weeks | reg 4, reg 11 (and the text generally) |
| `months` | constructor of `Unit of time` | a number of months | reg 4, reg 11 (and the text generally) |
| `years` | constructor of `Unit of time` | a number of years | reg 4, reg 11 (and the text generally) |
| `Time limit` | record | a number and its unit, so that "6 months" is never written as 180 | reg 4, line 149; reg 11, line 289 |
| `quantity` | field of `Time limit` (NUMBER) | how many units | as above |
| `unit` | field of `Time limit` (`Unit of time`) | which unit | as above |
| `Payment interval` | enumeration | how often a payment is made, for working out its monthly equivalent | reg 73(2), lines 1189-1192; Sch 4 para 7(2), lines 2195-2199; Sch 5 para 13(3), lines 2684-2688 |
| `weekly payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it times 52, over 12 | as above |
| `two-weekly payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it times 26, over 12 | as above |
| `four-weekly payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it times 13, over 12 | as above |
| `monthly payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it unchanged | as above |
| `three-monthly payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it times 4, over 12 | as above |
| `annual payments` | constructor of `Payment interval` | a payment made at this interval comes to a month by taking it over 12 | as above |
| YMD | rule | the stable prelude has no YMD; this is the shim, `YMD year month day` is `Date day month year` | brief ("Smaller gaps") |
| `core — the number of days in an assessment period` | rule | last day minus first day plus 1 | reg 21(1), line 432 |
| `core — the date reached by adding a time limit to a date` | rule | the start date plus the limit; months and years clamp the day of the month | reg 4, line 149 |
| `core — the monthly equivalent of a payment` | rule | an amount and a `Payment interval` to the monthly amount, unrounded | reg 73(2), Sch 4 para 7(2), Sch 5 para 13(3) |
| `core — an amount rounded to the nearest penny` | rule | half a penny or more counts as a penny; a smaller fraction is disregarded; assumed placement, see fork F1 | reg 6(1), line 172 |
| `core — an amount with any fraction of a pound disregarded` | rule | truncation to whole pounds | reg 6(1A), lines 173-176 |

**Why each core type is in the core.**
A type belongs in the core only if two or more pieces need it.
The count below is of lines of the text outside regulation 2 that mention the thing, by piece (uc1, uc2, uc3, uc4); a line count is a rough proxy for use, not a measure of it.
Nations of Great Britain: 28, 9, 26, 8.
Assessment period: 49, 64, 8, 22.
A period written "N months", "N weeks" or "N years" (the `Time limit`): 19, 27, 38, 26.
Couple (the `Claim basis`): 23, 19, 13, 11; "joint claimants": 15, 6, 3, 15.
Entitled to one of the benefits regulation 2 names (`Benefit`): 4, 3, 2, 6.
Housing costs element (`Element of an award`): 8, 4, 51, 0; LCWRA element: 14, 1, 8, 0; carer element: 11, 1, 0, 0; child element: 5, 0, 0, 1.
Limited capability for work (`Capability for work`): 18, 1, 9, 40.
Section 22 of the Act (`Work-related group`): regulation 12 (uc1, line 330), regulation 62 (uc2, line 1061), and regulation 90 (uc4).
The weekly-to-monthly table (`Payment interval`): regulation 73(2) (uc2) and Schedule 4 para 7(2) and Schedule 5 para 13(3) (uc3).
The rounding rules: regulation 6(1) (uc1) applies to every calculated amount, and regulation 6(1A) names regulations 82(1)(a) (uc2), 90 and 99(6) (uc4).

The topic modules add these types (each is imported only if you import that module):

| module | name | kind | what it is | licensed by |
| --- | --- | --- | --- | --- |
| uc-core-persons.l4 | `Sight certificate` | record | two BOOLEANs: certified as severely sight impaired or blind; certified by a consultant ophthalmologist | reg 2 "blind", line 26 |
| uc-core-persons.l4 | `Listed relation` | enumeration | the eleven relations of limb (a) of "close relative", each written `a parent`, `a parent-in-law`, `a son`, `a son-in-law`, `a daughter`, `a daughter-in-law`, `a step-parent`, `a step-son`, `a step-daughter`, `a brother`, `a sister`, and `not a listed relation` | reg 2 "close relative", lines 34-36 |
| uc-core-persons.l4 | `Possible close relative` | record | the relation of the person to the claimant and the relation of that person’s partner to the claimant | reg 2 "close relative" |
| uc-core-persons.l4 | `Placement of a child with a person` | record | nation of the placement; placed under the placement regulations; a foster carer or kinship carer | reg 2 "foster parent", lines 48-51 |
| uc-core-persons.l4 | `Practitioner` | record | four BOOLEANs for the limbs of "health care professional" | reg 2 "health care professional", lines 53-56 |
| uc-core-persons.l4 | `Care of a child` | record | three BOOLEANs, one per statute | reg 2 "looked after by a local authority", line 74 |
| uc-core-persons.l4 | `Work done by a person` | record | three BOOLEANs for "paid work" | reg 2 "paid work", line 82 |
| uc-core-persons.l4 | `Detention` | record | four BOOLEANs for "prisoner" | reg 2 "prisoner", lines 87-90 |
| uc-core-persons.l4 | `Relationship to a child or qualifying young person` | record | six BOOLEANs for the two limbs of "step-parent" | reg 2 "step-parent", lines 104-106 |
| uc-core-persons.l4 | `Illness` | record | suffering from a progressive disease; the months within which death can reasonably be expected | reg 2 "terminally ill", line 108 |
| uc-core-bodies.l4 | `Kind of council` | enumeration | the nine kinds of council the three lists name, and `another kind of body` | reg 2 "local authority", lines 62-65 |
| uc-core-bodies.l4 | `Body that may be a local authority` | record | the nation it is asked in relation to, and the kind of body | reg 2 "local authority" |
| uc-core-bodies.l4 | `Giver of assistance` | enumeration | a local authority; the Scottish Ministers; the Welsh Ministers; a person authorised to act for or provide a service to them; another giver | reg 2 "local welfare provision", line 66 |
| uc-core-bodies.l4 | `Assistance given to individuals` | record | the giver and seven BOOLEANs for the lead-in and the two purposes | reg 2 "local welfare provision", lines 66-72 |
| uc-core-bodies.l4 | `Whether the definition of enactment applies` | enumeration | `included by the definition of enactment`; `not decided by the definition of enactment` | reg 2 "enactment", line 45 |
| uc-core-bodies.l4 | `Provision whose standing as an enactment is asked` | record | comprised in, or made under, an Act of the Scottish Parliament or the National Assembly of Wales | reg 2 "enactment" |
| uc-core-payments.l4 | `Payment that may be an attendance allowance` | record | five BOOLEANs, one per limb (a), (b), (d), (e), (f) | reg 2 "attendance allowance", lines 18-24 |
| uc-core-payments.l4 | `Payment that may be a war disablement pension` | record | three BOOLEANs | reg 2 "war disablement pension", line 112 |

and these rules, all named `reg 2 — ...`:

| module | rule | takes | answers | licensed by |
| --- | --- | --- | --- | --- |
| uc-core-persons.l4 | `reg 2 — blind` | `Sight certificate` | BOOLEAN | line 26 |
| uc-core-persons.l4 | `reg 2 — close relative` | `Possible close relative` | BOOLEAN | lines 34-36 |
| uc-core-persons.l4 | `reg 2 — foster parent` | `Placement of a child with a person` | BOOLEAN | lines 48-51 |
| uc-core-persons.l4 | `reg 2 — health care professional` | `Practitioner` | BOOLEAN (not for regulation 98) | lines 53-56 |
| uc-core-persons.l4 | `reg 2 — looked after by a local authority` | `Care of a child` | BOOLEAN | line 74 |
| uc-core-persons.l4 | `reg 2 — paid work` | `Work done by a person` | BOOLEAN | line 82 |
| uc-core-persons.l4 | `reg 2 — the claimant has a partner` | `Claim basis` | BOOLEAN (not for regulation 77) | line 83 |
| uc-core-persons.l4 | `reg 2 — prisoner, limbs (a) and (b)` | `Detention` | BOOLEAN; helper, before the closing words | lines 87-89 |
| uc-core-persons.l4 | `reg 2 — prisoner` | `Detention` | BOOLEAN | lines 87-90 |
| uc-core-persons.l4 | `reg 2 — step-parent, limb (a)` | `Relationship to a child or qualifying young person` | BOOLEAN; helper | line 105 |
| uc-core-persons.l4 | `reg 2 — step-parent, limb (b)` | `Relationship to a child or qualifying young person` | BOOLEAN; helper | line 106 |
| uc-core-persons.l4 | `reg 2 — step-parent` | `Relationship to a child or qualifying young person` | BOOLEAN | lines 104-106 |
| uc-core-persons.l4 | `reg 2 — the months within which death must be expected for a person to be terminally ill` | nothing | NUMBER (12) | line 108 |
| uc-core-persons.l4 | `reg 2 — terminally ill` | `Illness` | BOOLEAN | line 108 |
| uc-core-bodies.l4 | `reg 2 — local authority` | `Body that may be a local authority` | BOOLEAN | lines 62-65 |
| uc-core-bodies.l4 | `reg 2 — local welfare provision, the giver` | `Assistance given to individuals` | BOOLEAN; helper | line 66 |
| uc-core-bodies.l4 | `reg 2 — local welfare provision, limb (a)` | `Assistance given to individuals` | BOOLEAN; helper | lines 67-69 |
| uc-core-bodies.l4 | `reg 2 — local welfare provision, limb (b)` | `Assistance given to individuals` | BOOLEAN; helper | lines 70-72 |
| uc-core-bodies.l4 | `reg 2 — local welfare provision` | `Assistance given to individuals` | BOOLEAN | lines 66-72 |
| uc-core-bodies.l4 | `reg 2 — enactment` | `Provision whose standing as an enactment is asked` | `Whether the definition of enactment applies` | line 45 |
| uc-core-payments.l4 | `reg 2 — attendance allowance` | `Payment that may be an attendance allowance` | BOOLEAN | lines 18-24 |
| uc-core-payments.l4 | `reg 2 — war disablement pension` | `Payment that may be a war disablement pension` | BOOLEAN | line 112 |

## Naming conventions

| item | convention |
| --- | --- |
| Rule | A rule is named `` `<provision> — <the thing, in the text’s own words>` ``, with the em dash (U+2014, copy it from here) and one space either side: `` `reg 24(1) — the child element` ``, `` `Sch 4 para 7(2) — the monthly equivalent of a payment` ``. A rule for one limb of a definition ends `, limb (a)`. The keel’s helpers begin `core —`; regulation 2’s definitions begin `reg 2 —`. Provision labels are unique to a piece, which is what keeps two pieces’ rule names from colliding (see Instructions to the pieces, item 4). |
| Input | A rule takes each fact as its own `GIVEN` (the stable build has no section `GIVEN`). The `GIVEN` name is the text’s word for it, lower case, singular, with no `is` or `has` in front: `claimant`, `claim basis`, `assessment period`. Where a concept has several facts, take them as one record (a `DECLARE ... HAS`) so that a seat layer can build the record from plain answers. |
| Record field | A field states the fact in the affirmative, in the text’s words, and does not begin with `is` or `has` (the genitive supplies the verb: `certificate’s `certified by a consultant ophthalmologist``). A negative lives in the rule as `NOT (...)`, never in a field called "not ..." (a double negative has no diagnostic). |
| Enumeration constructor | The text’s own words as a phrase in backticks, lower case except proper names: `` `joint claimants` ``, `` `a district council` ``. A constructor is a whole phrase, not a bare common word, so that two pieces rarely choose the same one. The core has seven bare words, and a piece must not use any of them as a constructor of its own: `England`, `Wales`, `Scotland` and the units `days`, `weeks`, `months`, `years`. |
| Type | A noun phrase naming the concept, capitalised first word only: `Claim basis`, `Assessment period`. Types a piece declares are named for what they hold in that provision, not generically (not `Child`, `Person`, `Period`). |
| Question | The keel writes no `@export`; whether a piece does is in that piece’s own brief. Whichever it is, a top-level rule should answer one question a person in the seat would ask, and be named for its provision; a seat layer phrases the questions "as the person asks them" and takes plain inputs. |
| Money | A NUMBER of pounds sterling; pence are decimals (`338.58`). There is no currency type. A calculated amount is rounded once, at the end, with `core — an amount rounded to the nearest penny` (regulation 6(1)); where a provision says "fraction of a pound disregarded" use `core — an amount with any fraction of a pound disregarded` (regulation 6(1A)). Regulation 6(2) says regulation 6 does not apply to the daily rate in regulation 111. |
| Percentage | The `%` literal: `55%` is 0.55. A percentage is never a bare 55. Apply it with `TIMES`. |
| Fraction | A NUMBER in which 1 is the whole: one half is `0.5`. Never a count of percentage points. |
| Days | A NUMBER of whole days. A longer period is a `Time limit` (a quantity and a `Unit of time`), added to a date with `core — the date reached by adding a time limit to a date`; do not turn weeks, months or years into days by hand. |
| Ages and hours | An age is a NUMBER of complete years at the date the provision speaks of. Hours are a NUMBER of hours per week unless the provision says otherwise; an hourly rate is a NUMBER of pounds per hour. |
| Dates | A DATE, written `YMD year month day` (the shim in the core). Compare dates with `AT LEAST` and `AT MOST` (inclusive). `add months` and `add years` move the day of the month back to the last day of a shorter month (31 August plus 6 months is 28 February). |
| A fact outside a piece | Take it as a plain input, named exactly as the defined term in the text (`pre-2026 claimant`, `qualifying young person`, `limited capability for work`), as a BOOLEAN or the core’s type, with a comment `-- by reference: encoded by uc?, reg N`. Never re-derive another piece’s result. The "Defined terms" table says which piece owns each term. |
| Benefits | Which benefits a person is entitled to, or receives, is a `LIST OF Benefit`. The core supplies the enumeration; your field name carries the verb your provision uses ("entitled to", "receiving", "in receipt of"), because the text distinguishes them. |
| A judgment of the Secretary of State | A BOOLEAN input worded as the condition ("the Secretary of State is satisfied that ..."), so the rule answers conditionally. Never guess it. |
| Not covered | Where the encoding cannot answer, return an explicit value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default. |
| Locators | A quote run `-- src:N | ...` is followed by `@ref <provision> (src:N-M)` and then the declaration it supports. The locator reaches exactly the lowest and highest line quoted. Run `srcrefs.py check --strict`. |
| Tests | One `uc-<piece>-tests-<topic>.l4` per module. One `#ASSERT` per line; expected values are written by hand from the text, with the provision in a comment; a boundary on each side of every threshold. |

## Defined terms

Every term regulation 2 defines (71), in the order of the text.
Dotted rows (lines 15, 21, 25, 93, 113) define nothing and are in the coverage table.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| `the Act` | line 14 | inert: pure citation of the Welfare Reform Act 2012 | The Act is not among the inputs; every effect of it that a rule needs is a stated input. |
| `adopter` | line 16 | by reference: encoded by uc4, reg 89(3)(a), taken there as an input | Used by uc3 (line 2284) and uc4 (lines 1395, 1405, 1744). |
| `adult disability payment` | line 17 | uc-core.l4: constructor `adult disability payment` of `Benefit` | Defined by a Scottish instrument that is not an input; whether a payment is one is a stated input. |
| `attendance allowance` | lines 18-24 | uc-core-payments.l4: `reg 2 — attendance allowance`; constructor `attendance allowance` of `Benefit` | Limb (c), line 21, is dots in this text and is not encoded; the limbs tested are (a), (b), (d), (e), (f). |
| `blind` | line 26 | uc-core-persons.l4: `reg 2 — blind` | Used by uc1 (line 516) and uc3 (line 2324). |
| `care leaver` | line 27 | by reference: encoded by uc1, reg 8, taken there as an input | Used by uc1 (lines 195, 207) and uc3 (lines 2176, 2177, 2483). |
| `carer's allowance` | line 28 | uc-core.l4: constructor `carer's allowance` of `Benefit` | Section 70 of the Contributions and Benefits Act is not an input. |
| `carer element` | line 29 | by reference: encoded by uc1, reg 29, taken there as an input; the core has constructor `carer element` of `Element of an award` | Regulation 29 is uc1’s. Used outside regulation 2 on 11 lines of uc1’s range and 1 of uc2’s. |
| `carer support payment` | line 30 | uc-core.l4: constructor `carer support payment` of `Benefit` | Scottish Regulations 2023 not an input. |
| `child disability payment` | line 31 | uc-core.l4: constructor `child disability payment` of `Benefit` | Defined by the DACYP Regulations, not an input. |
| `childcare costs element` | line 32 | by reference: encoded by uc1, reg 31, taken there as an input; the core has constructor `childcare costs element` | Regulations 31 to 35 are uc1’s. Used outside regulation 2 on 7 lines of uc1’s range and 2 of uc2’s. |
| `child element` | line 33 | by reference: encoded by uc1, reg 24, taken there as an input; the core has constructor `child element` | Regulation 24 is uc1’s. Used outside regulation 2 on 5 lines of uc1’s range and 1 of uc4’s. |
| `close relative` | lines 34-36 | uc-core-persons.l4: `reg 2 — close relative` | Used outside regulation 2 on 3 lines of uc1’s range, 1 of uc2’s, 5 of uc3’s and 1 of uc4’s. Fork F2. |
| `confinement` | line 37 | by reference: encoded by uc1, reg 8, taken there as an input | Used by uc1 (193, 214) and uc4 (1394, 1744). |
| `Contributions and Benefits Act` | line 38 | pure citation; no rule | Social Security Contributions and Benefits Act 1992. |
| `course of advanced education` | line 39 | by reference: encoded by uc1, reg 12, taken there as an input | Used by uc1 only. |
| `the DACYP Regulations` | line 40 | pure citation; no rule | Disability Assistance for Children and Young People (Scotland) Regulations 2021. |
| `disability living allowance` | line 41 | uc-core.l4: constructor `disability living allowance` of `Benefit` | Section 71 of the Contributions and Benefits Act. |
| `earned income` | line 42 | by reference: encoded by uc2, Chapter 2 of Part 6 (reg 52 onward), taken there as an input | Used outside regulation 2 on 8 lines of uc1’s range, 51 of uc2’s, 4 of uc3’s and 5 of uc4’s. |
| `EEA Regulations` | line 43 | pure citation; no rule | Immigration (European Economic Area) Regulations 2016, read with Schedule 4 to the 2020 Regulations. |
| `employment and support allowance` | line 44 | uc-core.l4: constructor `employment and support allowance` of `Benefit` | Welfare Reform Act 2007 Part 1. |
| `enactment` | line 45 | uc-core-bodies.l4: `reg 2 — enactment` | Used by uc2 (1352, 2852, 2858) and uc4 (2777, 2778). Returns an explicit "not decided" outcome, never FALSE. |
| `ESA Regulations` | line 46 | pure citation; no rule | Employment and Support Allowance Regulations 2013. |
| `expected number of hours per week` | line 47 | by reference: encoded by uc4, reg 88, taken there as an input | Used by uc4 only. |
| `foster parent` | lines 48-51 | uc-core-persons.l4: `reg 2 — foster parent` | Used outside regulation 2 on 5 lines of uc1’s range, 8 of uc3’s and 12 of uc4’s. |
| `grant` | line 52 | by reference: encoded by uc2, reg 68, taken there as an input | Used by uc1 (341, 363) and uc2. |
| `health care professional` | lines 53-56 | uc-core-persons.l4: `reg 2 — health care professional` | Except in regulation 98, which has its own meaning in reg 98(4) (uc4). Used outside regulation 2 on 1 line of uc3’s range and 7 of uc4’s. Fork F6. |
| `housing costs element` | line 57 | by reference: encoded by uc1, reg 25, taken there as an input; the core has constructor `housing costs element` | Regulation 25 is uc1’s; Schedules 1 to 5 (uc3) work out its amount. Used outside regulation 2 on 8 lines of uc1’s range, 4 of uc2’s and 51 of uc3’s. |
| `individual threshold` | line 58 | by reference: encoded by uc4, reg 90(2), taken there as an input | Used outside regulation 2 on 5 lines of uc2’s range and 10 of uc4’s. |
| `industrial injuries benefit` | line 59 | uc-core.l4: constructor `industrial injuries benefit` of `Benefit` | Part 5 of the Contributions and Benefits Act. |
| `ITEPA` | line 60 | pure citation; no rule | Income Tax (Earnings and Pensions) Act 2003. |
| `jobseeker's allowance` | line 61 | uc-core.l4: constructor `jobseeker's allowance` of `Benefit` | Jobseekers Act 1995 as amended. |
| `local authority` | lines 62-65 | uc-core-bodies.l4: `reg 2 — local authority` | Used outside regulation 2 on 8 lines of uc1’s range, 1 of uc2’s, 13 of uc3’s and 1 of uc4’s. |
| `local welfare provision` | lines 66-72 | uc-core-bodies.l4: `reg 2 — local welfare provision` | Used by uc2 only (line 2863, Schedule 10). Fork F7. |
| `LCWRA element` | line 73 | by reference: encoded by uc1, reg 27, taken there as an input; the core has constructor `LCWRA element` | Regulation 27 is uc1’s. Used outside regulation 2 on 14 lines of uc1’s range, 1 of uc2’s and 8 of uc3’s. |
| `looked after by a local authority` | line 74 | uc-core-persons.l4: `reg 2 — looked after by a local authority` | Used outside regulation 2 on 6 lines of uc1’s range, 1 of uc3’s and 1 of uc4’s. |
| `maternity allowance` | line 75 | uc-core.l4: constructor `maternity allowance` of `Benefit` | Sections 35 and 35B of the Contributions and Benefits Act. |
| `Medical Evidence Regulations` | line 76 | pure citation; no rule | Social Security (Medical Evidence) Regulations 1976. |
| `monthly earnings` | line 77 | by reference: encoded by uc4, reg 90(6), taken there as an input | Used by uc1 (582) and uc4. |
| `national insurance contribution` | line 78 | pure citation; no rule | Means a contribution under Part 1 of the Contributions and Benefits Act, which is not an input. Used by uc2 (963, 981, 990, 1069) and uc4 (1428, 1429). |
| `National Minimum Wage Regulations` | line 79 | pure citation; no rule | The hourly rates in regulations 4 and 4A are not inputs: any piece that needs one takes the amount as a NUMBER input (pounds per hour). |
| `Scottish adult disability living allowance` | line 80 | uc-core.l4: constructor `Scottish adult disability living allowance` of `Benefit` | Scottish Regulations 2025, not an input. |
| `statutory paternity pay` | line 81 | uc-core.l4: constructor `statutory paternity pay` of `Benefit` | The line shows repealed words as "...". Fork F9. |
| `paid work` | line 82 | uc-core-persons.l4: `reg 2 — paid work` | Used outside regulation 2 on 12 lines of uc1’s range, 3 of uc2’s and 40 of uc4’s. Fork F3. |
| `partner` | line 83 | uc-core-persons.l4: `reg 2 — the claimant has a partner` | Except in regulation 77 (uc2 defines its own). Used outside regulation 2 on 5 lines of uc1’s range, 19 of uc2’s, 5 of uc3’s and 1 of uc4’s. |
| `pension age disability payment` | line 84 | uc-core.l4: constructor `pension age disability payment` of `Benefit` | Scottish Regulations 2024, not an input. |
| `personal independence payment` | line 85 | uc-core.l4: constructor `personal independence payment` of `Benefit` | Part 4 of the Welfare Reform Act 2012. |
| `pre-2026 claimant` | line 86 | by reference: encoded by uc1, reg 27A(1), taken there as an input (and uc3, Schedule 5A para 1, adds further circumstances) | Regulation 27A(1) (uc1, line 572) and Schedule 5A (uc3, line 2698) each say when a claimant is one; regulation 27 (uc1) reads the result. |
| `prisoner` | lines 87-90 | uc-core-persons.l4: `reg 2 — prisoner` | Used outside regulation 2 on 11 lines of uc1’s range, 5 of uc3’s and 1 of uc4’s. Fork F4. |
| `qualifying young person` | line 91 | by reference: encoded by uc1, reg 5, taken there as an input | Used by all four pieces. |
| `redundancy` | line 92 | pure citation; no rule | Means redundancy within section 139(1) of the Employment Rights Act 1996, not an input. Used by uc2 (1109) and uc4 (1765, 1766). |
| `regular and substantial caring responsibilities for a severely disabled person` | line 94 | by reference: encoded by uc1, reg 30, taken there as an input | Used by uc1 only. |
| `relevant childcare` | line 95 | by reference: encoded by uc1, reg 35, taken there as an input | Used by uc1 only. |
| `responsible for a child or qualifying young person` | line 96 | by reference: encoded by uc1, reg 4, taken there as an input | Used by all four pieces; the keel’s `reg 2 — step-parent` takes it as a fact. |
| `severe conditions criteria claimant` | line 97 | by reference: encoded by uc4, reg 40A(2), taken there as an input; the core has field `severe conditions criteria claimant` of `Capability for work` | Read by uc1 (564, 567, 730, 731). |
| `statutory adoption pay` | line 98 | uc-core.l4: constructor `statutory adoption pay` of `Benefit` | Part 12ZB of the Contributions and Benefits Act. Line 98 prints "Contributions Benefits Act" (the word "and" is missing); quoted as printed. |
| `statutory maternity pay` | line 99 | uc-core.l4: constructor `statutory maternity pay` of `Benefit` | Part 12 of the Contributions and Benefits Act. |
| `statutory neonatal care pay` | line 100 | uc-core.l4: constructor `statutory neonatal care pay` of `Benefit` | Part 12ZE of the Contributions and Benefits Act. |
| `statutory parental bereavement pay` | line 101 | uc-core.l4: constructor `statutory parental bereavement pay` of `Benefit` | Part 12ZD of the Contributions and Benefits Act. |
| `statutory shared parental pay` | line 102 | uc-core.l4: constructor `statutory shared parental pay` of `Benefit` | Part 12ZC of the Contributions and Benefits Act. |
| `statutory sick pay` | line 103 | uc-core.l4: constructor `statutory sick pay` of `Benefit` | Part 11 of the Contributions and Benefits Act. |
| `step-parent` | lines 104-106 | uc-core-persons.l4: `reg 2 — step-parent` | Used by uc4 only (lines 1442, 1521). In relation to a child or qualifying young person. Fork F2 concerns the close-relative list. |
| `student loan` | line 107 | by reference: encoded by uc2, reg 68, taken there as an input | Used by uc1 (341, 363) and uc2. |
| `terminally ill` | line 108 | uc-core-persons.l4: `reg 2 — terminally ill` | Used by uc1 (398, 565, 591, 730, 731) and uc4 (2801). |
| `total outstanding reduction period` | line 109 | by reference: encoded by uc4, reg 101(5), taken there as an input | Used by uc4 only. |
| `trade dispute` | line 110 | pure citation; no rule | Means a trade dispute within section 244 of the Trade Union and Labour Relations (Consolidation) Act 1992, not an input. Used by uc2 (968, 969) and uc4 (1756, 1761). |
| `unearned income` | line 111 | by reference: encoded by uc2, Chapter 3 of Part 6 (reg 66 onward), taken there as an input | Used outside regulation 2 on 3 lines of uc1’s range and 20 of uc2’s. |
| `war disablement pension` | line 112 | uc-core-payments.l4: `reg 2 — war disablement pension`; constructor `war disablement pension` of `Benefit` | Not used outside regulation 2; inside it, limb (e) of "attendance allowance" uses it. The list in section 639(2) of ITEPA is not an input. |
| `widowed mother's allowance` | line 114 | uc-core.l4: constructor `widowed mother's allowance` of `Benefit` | Section 37 of the Contributions and Benefits Act. |
| `widowed parent's allowance` | line 115 | uc-core.l4: constructor `widowed parent's allowance` of `Benefit` | Section 39A of the Contributions and Benefits Act. |
| `widow's pension` | line 116 | uc-core.l4: constructor `widow's pension` of `Benefit` | Section 39 of the Contributions and Benefits Act. |

**By kind:** 23 by reference to another provision of these Regulations (a pointer); 22 a benefit named as a constructor of `Benefit`; 15 a rule in a topic module; 11 a citation of an instrument or of another Act.

(`attendance allowance` and `war disablement pension` are both a rule and a constructor; they are counted as rules.)

## Instructions to the pieces

1. **Import.** ``IMPORT `uc-core` `` and, for the definitions you use, ``IMPORT `uc-core-persons` ``, ``IMPORT `uc-core-bodies` ``, ``IMPORT `uc-core-payments` ``. Hyphenated module names need backticks. Imports are transitive: importing a topic module also brings in the core. A second `IMPORT` of a module already imported is harmless (probed).
2. **Do not redefine anything in the Vocabulary table or in the keel’s rules.** That includes `YMD`, the three nations, `Benefit`, `Element of an award`, `Claim basis`, the rounding rules and the monthly-equivalent rule. Call them. Do not write a regulation 6 rule (uc1): use `core — an amount rounded to the nearest penny`. Do not write the ×52÷12 conversion again (uc2 regulation 73(2); uc3 Schedule 4 para 7(2), Schedule 5 para 13(3)): use `core — the monthly equivalent of a payment`.
3. **Take the definitions in regulation 2 from the keel when you can.** `reg 2 — blind`, `close relative`, `foster parent`, `health care professional` (not for regulation 98), `local authority`, `local welfare provision`, `looked after by a local authority`, `paid work`, `the claimant has a partner` (not for regulation 77), `prisoner`, `step-parent`, `terminally ill`, `attendance allowance`, `war disablement pension` and `enactment` are rules. Build the record they take from your inputs; do not copy the rule. Where a record has more fields than your provision needs, say so in a comment and give the field a fixed placeholder.
4. **Names must be unique across the whole encoding, because a seat layer will import all the pieces at once.** Measured on the stable binary (1.6.98): two imported modules that each declare a type of the same name make that name unusable (error); two rules of the same name likewise, even with the same type; two enumeration constructors of the same word are accepted where the expected type is known and an error where it is not (a bare `#EVAL red`); the same field name in two records is fine. So: name every rule with your own provision label; give every type a name specific to its provision; make every constructor a whole phrase; never reuse a name from the Vocabulary table, above all the seven bare words in the core (`England`, `Wales`, `Scotland`, `days`, `weeks`, `months`, `years`), because a piece that declares its own `IS ONE OF ... months ...` makes a bare `months` untyped-ambiguous in every file that imports both.
5. **"Except in" definitions.** The definition of `partner` is "except in regulation 77" (uc2 defines its own meaning there) and of `health care professional` "except in regulation 98" (uc4 defines its own in regulation 98(4)). Do not use the keel’s rule in those two regulations.
6. **Cross-piece facts.** A fact another piece works out is a plain input to yours, named exactly as the defined term. The ones the usage count found: `pre-2026 claimant` (regulation 27A(1), uc1, and Schedule 5A para 1, uc3, each give circumstances, and regulation 27 reads the result. Proposed, for uc1 and uc3 to follow, not ruled: uc1 encodes regulation 27A(1) and takes "meets a circumstance in Schedule 5A" as a BOOLEAN input; uc3 encodes Schedule 5A para 1; the seat layer feeds uc3’s answer to uc1’s input); `qualifying young person` (regulation 5, uc1; used by all four pieces); `responsible for a child or qualifying young person` (regulation 4, uc1; all four); `limited capability for work`, `limited capability for work and work-related activity`, `severe conditions criteria claimant` (Part 5, uc4; read by uc1, uc2, uc3: use the core’s `Capability for work`); `monthly earnings`, `individual threshold`, `expected number of hours per week` (uc4; read by uc1 and uc2); `earned income`, `unearned income`, `student loan`, `grant` (Part 6, uc2; read by uc1, uc3, uc4); `care leaver`, `confinement`, `course of advanced education`, `relevant childcare`, `regular and substantial caring responsibilities` (uc1; read by uc3 and uc4). One test is written twice by the text and each piece does its own: pregnant and 11 weeks or less before the expected week of confinement, or 15 weeks or less since the date of confinement (uc1 regulation 8(1)(f), line 193; uc4 regulation 89(1)(c), line 1394). Everything else the pieces share is in the core.
7. **Stated inputs for other instruments.** The National Minimum Wage hourly rates (regulations 4 and 4A of the 2015 Regulations), the Act’s provisions, and every Act cited by a definition are stated inputs: a NUMBER (pounds per hour) or a BOOLEAN, worded for the seat in a `@desc` by the later seat layer.
8. **Stable dialect.** Read "What the stable binary does not accept" below before you write a line. In particular: keep every `#ASSERT` on one line; parenthesise every `NOT`; do not put `AND` and `OR` at the same indentation in one expression (it is a warning, and check.sh does not count warnings: split the expression into helper rules, as the keel does in `reg 2 — prisoner` and `reg 2 — step-parent`).
9. **Do not edit the keel’s files.** If the core is missing something you need, define it locally under a name prefixed by your provision label, and say in your own notes that you wanted it in the core.
10. **Gate.** `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` must print 0 errors, 0 failed and 0 refused; `python3 -I srcrefs.py check --refs <the .txt> <your .l4 files>` must report 0 problems; and `l4 run` on each file must show no `DiagnosticSeverity_Warning` (grep for it: check.sh does not count warnings).

## Coverage table

One row per provision of lines 12-117.
Regulation 2 is one section with one heading; its content is a list of definitions, and each definition (and each blank row) has a row.
The cross-heading at line 117 has a row too.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| reg 2 heading "Interpretation" and the opening words "In these Regulations—" | 12-13 | inert | none | The heading of the section and the words that introduce the list of definitions. They carry no rule; every definition that follows has its own row below. |
| reg 2, "the Act" | 14 | inert | none | Means the Welfare Reform Act 2012. A pure citation: the Act is not an input, so wherever a regulation depends on a provision of it, the piece takes that provision’s effect as a stated input. |
| reg 2, a blank row between "the Act" and "adopter" | 15 | repealed or blank in this text | none | The line is "..." and nothing else: a definition repealed or removed. Not reconstructed. |
| reg 2, "adopter" | 16 | inert | encoded by uc4, reg 89(3)(a) | A pointer to regulation 89(3)(a); the meaning is encoded there by uc4, so this row has nothing to compute. |
| reg 2, "adult disability payment" | 17 | encoded | uc-core.l4: constructor `adult disability payment` of `Benefit` | Named as a constructor of `Benefit`; its meaning rests on regulation 2 of the Scottish Regulations 2022, which is not an input. |
| reg 2, "attendance allowance" | 18-24 | encoded | uc-core-payments.l4: `reg 2 — attendance allowance`; constructor `attendance allowance` of `Benefit` | Limbs (a), (b), (d), (e), (f) are one BOOLEAN each in `Payment that may be an attendance allowance`; limb (c) is its own row below (fork F8). |
| reg 2, "attendance allowance" limb (c) | 21 | repealed or blank in this text | none | The line is a row of dots after limb (b). The limbs are lettered (a), (b), (d), (e), (f) around it; the gap is kept, not filled (fork F8). |
| reg 2, a blank row after "attendance allowance" | 25 | repealed or blank in this text | none | The line is "..." and nothing else. |
| reg 2, "blind" | 26 | encoded | uc-core-persons.l4: `reg 2 — blind` | Certified as severely sight impaired or blind AND certified by a consultant ophthalmologist. |
| reg 2, "care leaver" | 27 | inert | encoded by uc1, reg 8 | A pointer to regulation 8; encoded there by uc1. |
| reg 2, "carer's allowance" | 28 | encoded | uc-core.l4: constructor `carer's allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "carer element" | 29 | inert | encoded by uc1, reg 29 | A pointer to regulation 29; encoded there by uc1. The core names the element in `Element of an award`. |
| reg 2, "carer support payment" | 30 | encoded | uc-core.l4: constructor `carer support payment` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "child disability payment" | 31 | encoded | uc-core.l4: constructor `child disability payment` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "childcare costs element" | 32 | inert | encoded by uc1, reg 31 | A pointer to regulation 31; encoded there by uc1. The core names the element. |
| reg 2, "child element" | 33 | inert | encoded by uc1, reg 24 | A pointer to regulation 24; encoded there by uc1. The core names the element. |
| reg 2, "close relative" | 34-36 | fork | uc-core-persons.l4: `reg 2 — close relative` | Limb (a) lists eleven relations, limb (b) adds the other member of a couple of which one is listed; both limbs are in one rule. Fork F2: the step relations. |
| reg 2, "confinement" | 37 | inert | encoded by uc1, reg 8 | A pointer to regulation 8; encoded there by uc1. |
| reg 2, "Contributions and Benefits Act" | 38 | inert | none | An abbreviation of the title of an Act that is not an input. Pure citation. |
| reg 2, "course of advanced education" | 39 | inert | encoded by uc1, reg 12 | A pointer to regulation 12; encoded there by uc1. |
| reg 2, "the DACYP Regulations" | 40 | inert | none | An abbreviation of an instrument’s title; used by the definition of child disability payment. Pure citation. |
| reg 2, "disability living allowance" | 41 | encoded | uc-core.l4: constructor `disability living allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "earned income" | 42 | inert | encoded by uc2, Chapter 2 of Part 6 (reg 52 onward) | A pointer to Chapter 2 of Part 6; encoded there by uc2. |
| reg 2, "EEA Regulations" | 43 | inert | none | An abbreviation of an instrument’s title and a rule of reading for references to it. Pure citation. |
| reg 2, "employment and support allowance" | 44 | encoded | uc-core.l4: constructor `employment and support allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "enactment" | 45 | fork | uc-core-bodies.l4: `reg 2 — enactment` | "Includes" is open-ended, so the rule can say yes for two things and never says no. Fork F5. |
| reg 2, "ESA Regulations" | 46 | inert | none | An abbreviation of an instrument’s title. Pure citation. |
| reg 2, "expected number of hours per week" | 47 | inert | encoded by uc4, reg 88 | A pointer to regulation 88; encoded there by uc4. |
| reg 2, "foster parent" | 48-51 | encoded | uc-core-persons.l4: `reg 2 — foster parent` | England and Wales: placed under the placement Regulations. Scotland: placed under the 2009 Regulations AND a foster carer or kinship carer. |
| reg 2, "grant" | 52 | inert | encoded by uc2, reg 68 | A pointer to regulation 68; encoded there by uc2. |
| reg 2, "health care professional" | 53-56 | fork | uc-core-persons.l4: `reg 2 — health care professional` | Three limbs, in one rule. Fork F6: the scope of the registration words in limb (c). Not for regulation 98. |
| reg 2, "housing costs element" | 57 | inert | encoded by uc1, reg 25 | A pointer to regulation 25; encoded there by uc1. The core names the element. |
| reg 2, "individual threshold" | 58 | inert | encoded by uc4, reg 90(2) | A pointer to regulation 90(2); encoded there by uc4. |
| reg 2, "industrial injuries benefit" | 59 | encoded | uc-core.l4: constructor `industrial injuries benefit` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "ITEPA" | 60 | inert | none | An abbreviation of an Act’s title. Pure citation. |
| reg 2, "jobseeker's allowance" | 61 | encoded | uc-core.l4: constructor `jobseeker's allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "local authority" | 62-65 | encoded | uc-core-bodies.l4: `reg 2 — local authority` | England, Wales and Scotland each list their kinds of council; the rule takes the nation and the kind of body. |
| reg 2, "local welfare provision" | 66-72 | fork | uc-core-bodies.l4: `reg 2 — local welfare provision` | The lead-in and two purposes in one rule, with helper rules per limb. Fork F7: the lead-in applies to both purposes. |
| reg 2, "LCWRA element" | 73 | inert | encoded by uc1, reg 27 | A pointer to regulation 27; encoded there by uc1. The core names the element. |
| reg 2, "looked after by a local authority" | 74 | encoded | uc-core-persons.l4: `reg 2 — looked after by a local authority` | Looked after within the meaning of any of the three statutes; each is a stated input. |
| reg 2, "maternity allowance" | 75 | encoded | uc-core.l4: constructor `maternity allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "Medical Evidence Regulations" | 76 | inert | none | An abbreviation of an instrument’s title. Pure citation. |
| reg 2, "monthly earnings" | 77 | inert | encoded by uc4, reg 90(6) | A pointer to regulation 90(6); encoded there by uc4. |
| reg 2, "national insurance contribution" | 78 | inert | none | A definition by citation of another Act; whether a payment is such a contribution is a stated input wherever a regulation needs it. |
| reg 2, "National Minimum Wage Regulations" | 79 | inert | none | An abbreviation of an instrument’s title. Pure citation; the rates it sets are stated inputs. |
| reg 2, "Scottish adult disability living allowance" | 80 | encoded | uc-core.l4: constructor `Scottish adult disability living allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory paternity pay" | 81 | encoded | uc-core.l4: constructor `statutory paternity pay` of `Benefit` | Named as a constructor of `Benefit`; the definition as it stands is quoted mechanically, dots included (fork F9). |
| reg 2, "paid work" | 82 | fork | uc-core-persons.l4: `reg 2 — paid work` | Work for payment, but not being engaged by a charity or as a volunteer where the payment is only in respect of expenses. Fork F3. |
| reg 2, "partner" | 83 | encoded | uc-core-persons.l4: `reg 2 — the claimant has a partner` | The other member of a couple. The rule reads the `Claim basis`; membership of a couple is the Act’s section 39, a stated input. |
| reg 2, "pension age disability payment" | 84 | encoded | uc-core.l4: constructor `pension age disability payment` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "personal independence payment" | 85 | encoded | uc-core.l4: constructor `personal independence payment` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "pre-2026 claimant" | 86 | inert | encoded by uc1, reg 27A(1) | A pointer to regulation 27A(1); encoded there by uc1. Schedule 5A, in uc3’s range, extends it (see Instructions to the pieces, item 6). |
| reg 2, "prisoner" | 87-90 | fork | uc-core-persons.l4: `reg 2 — prisoner` | Custody pending trial or sentence, under sentence, or on temporary release; but not detained in hospital under the mental health Acts. Fork F4: the closing words apply to both limbs. |
| reg 2, "qualifying young person" | 91 | inert | encoded by uc1, reg 5 | A pointer to regulation 5; encoded there by uc1. |
| reg 2, "redundancy" | 92 | inert | none | A definition by citation of another Act; a stated input wherever a regulation needs it. |
| reg 2, a blank row between "redundancy" and "regular and substantial caring responsibilities" | 93 | repealed or blank in this text | none | The line is "..." and nothing else. |
| reg 2, "regular and substantial caring responsibilities for a severely disabled person" | 94 | inert | encoded by uc1, reg 30 | A pointer to regulation 30; encoded there by uc1. |
| reg 2, "relevant childcare" | 95 | inert | encoded by uc1, reg 35 | A pointer to regulation 35; encoded there by uc1. |
| reg 2, "responsible for a child or qualifying young person" | 96 | inert | encoded by uc1, reg 4 | A pointer to regulation 4; encoded there by uc1. |
| reg 2, "severe conditions criteria claimant" | 97 | inert | encoded by uc4, reg 40A(2) | A pointer to regulation 40A(2); encoded there by uc4. |
| reg 2, "statutory adoption pay" | 98 | encoded | uc-core.l4: constructor `statutory adoption pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory maternity pay" | 99 | encoded | uc-core.l4: constructor `statutory maternity pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory neonatal care pay" | 100 | encoded | uc-core.l4: constructor `statutory neonatal care pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory parental bereavement pay" | 101 | encoded | uc-core.l4: constructor `statutory parental bereavement pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory shared parental pay" | 102 | encoded | uc-core.l4: constructor `statutory shared parental pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "statutory sick pay" | 103 | encoded | uc-core.l4: constructor `statutory sick pay` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "step-parent" | 104-106 | encoded | uc-core-persons.l4: `reg 2 — step-parent` | Not the parent, and either limb (a) or limb (b); `responsible for` is a fact from regulation 4. |
| reg 2, "student loan" | 107 | inert | encoded by uc2, reg 68 | A pointer to regulation 68; encoded there by uc2. |
| reg 2, "terminally ill" | 108 | encoded | uc-core-persons.l4: `reg 2 — terminally ill` | A progressive disease, and death in consequence reasonably expected within 12 months (12 or fewer). The months are a clinician’s estimate, a stated input. |
| reg 2, "total outstanding reduction period" | 109 | inert | encoded by uc4, reg 101(5) | A pointer to regulation 101(5); encoded there by uc4. |
| reg 2, "trade dispute" | 110 | inert | none | A definition by citation of another Act; a stated input wherever a regulation needs it. |
| reg 2, "unearned income" | 111 | inert | encoded by uc2, Chapter 3 of Part 6 (reg 66 onward) | A pointer to Chapter 3 of Part 6; encoded there by uc2. |
| reg 2, "war disablement pension" | 112 | encoded | uc-core-payments.l4: `reg 2 — war disablement pension`; constructor `war disablement pension` of `Benefit` | Retired pay, pension or allowance; payable in respect of disablement; under an instrument specified in section 639(2) of ITEPA (a stated input). |
| reg 2, a blank row after "war disablement pension" | 113 | repealed or blank in this text | none | The line is "..." and nothing else. |
| reg 2, "widowed mother's allowance" | 114 | encoded | uc-core.l4: constructor `widowed mother's allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "widowed parent's allowance" | 115 | encoded | uc-core.l4: constructor `widowed parent's allowance` of `Benefit` | Named as a constructor of `Benefit`. |
| reg 2, "widow's pension" | 116 | encoded | uc-core.l4: constructor `widow's pension` of `Benefit` | Named as a constructor of `Benefit`. |
| cross-heading "The Benefit Unit" | 117 | inert | none | A cross-heading printed before regulation 3 and so inside the keel’s line range. It is a heading and carries no rule; regulation 3 (line 118) is uc1’s. |

**Summary:** 78 rows: 31 encoded, 36 inert, 5 repealed or blank in this text, 6 fork.
Headings in lines 12-117: 1 section heading (regulation 2) and 1 cross-heading ("The Benefit Unit"), which have 2 rows (the first row, and the last).
Definitions: 71 rows, one per defined term; blank rows: 5 (lines 15, 21, 25, 93, 113).

## Fork register

Each row is a place where the text could be read two ways, or the keel had to choose.
The reading taken is the one encoded.

| id | provision | the question | reading taken | other reading | where |
| --- | --- | --- | --- | --- | --- |
| F1 | reg 6(1), reg 6(1A); lines 172-176 (outside the keel’s range) | Where does the rounding live, and how is a negative amount rounded? | The core holds `core — an amount rounded to the nearest penny` and `core — an amount with any fraction of a pound disregarded`, because pieces cannot import each other and all four compute amounts. A negative amount is rounded on its size and keeps its sign (the text speaks only of "a fraction of a penny"). **Assumed, not ruled.** | uc1 defines regulation 6 in its own module and the others copy it; or a negative amount rounds towards plus infinity. | uc-core.l4 |
| F2 | reg 2 "close relative"; lines 34-36 | "Step-parent", "step-son" and "step-daughter" are on the list, but "step-parent" is defined in regulation 2 only "in relation to a child or qualifying young person". Does limb (b) need the couple to exist as a matter of law? | The listed relations are stated facts about the person; `reg 2 — step-parent` is not applied to them. For limb (b) the other member’s relation is recorded in `relation of the partner to the person`; that they are a couple is the Act’s section 39, a stated input. | Apply the step-parent definition to the claimant’s step relatives. | uc-core-persons.l4 |
| F3 | reg 2 "paid work"; line 82 | (i) Do the words "in circumstances in which the payment ... is in respect of expenses" govern both "engaged by a charitable or voluntary organisation" and "as a volunteer"? (ii) Is a payment of wages and expenses "in respect of expenses"? | (i) Both. (ii) Only a payment that is wholly in respect of expenses takes the work out of paid work; a volunteer paid a fee plus expenses is in paid work. | (i) The expenses words qualify only the volunteer limb. (ii) Any element of expenses is enough. | uc-core-persons.l4 |
| F4 | reg 2 "prisoner"; lines 87-90 | Do the closing words "other than a person who is detained in hospital under the provisions of the Mental Health Act 1983 ..." qualify limb (a) only, or (a) and (b)? | Both limbs: they sit after limb (b) and are set off by a comma, so a person on temporary release who is detained in hospital is not a prisoner. | The words qualify only limb (b). | uc-core-persons.l4 |
| F5 | reg 2 "enactment"; line 45 | "Includes" is open-ended: the definition does not say what an enactment is, only two things it covers. | The rule answers `included by the definition of enactment` for the two things and `not decided by the definition of enactment` for everything else. It never answers no. A piece that needs "is this an enactment" takes that as an input and may use the keel’s rule only to short-cut the two included cases. | Treat the list as exhaustive. | uc-core-bodies.l4 |
| F6 | reg 2 "health care professional"; lines 53-56 | Does "registered with a regulatory body established by Order in Council under section 60 of the Health Act 1999" qualify both the occupational therapist and the physiotherapist? Limbs (a) and (b) say "registered" in their own words. | It qualifies both, and the registration in (a) and (b) is the status itself, taken as a fact. The definition is "except in regulation 98", where regulation 98(4) (uc4) gives another meaning. | It qualifies only the physiotherapist. | uc-core-persons.l4 |
| F7 | reg 2 "local welfare provision"; lines 66-72 | Does "occasional financial or other assistance given by" the listed givers apply to both purposes? Are (b)(i) and (b)(ii) alternatives? Does "them" mean all three givers? | The lead-in applies to both purposes; (b)(i) and (b)(ii) are alternatives; "them" means the local authority, the Scottish Ministers and the Welsh Ministers, so a person authorised to act for any of them is a giver. | The lead-in introduces limb (a) only. | uc-core-bodies.l4 |
| F8 | reg 2 "attendance allowance"; lines 21 and 25 | Limb (c) is a row of dots and line 25 is "..."; was something repealed, or is the converter hiding it? | The limbs (a), (b), (d), (e), (f) are encoded with their letters kept; the gap is not filled. The metadata lists 12 outstanding effects and none names regulation 2, so the dots are read as wording already repealed. | Reconstruct a limb (c) from another source (not done: the inputs are the only source). | uc-core-payments.l4 |
| F9 | reg 2 "statutory paternity pay" and "statutory adoption pay"; lines 81 and 98 | Line 81 begins "“... statutory paternity pay” means ..." with dots where words were repealed. Line 98 prints "Contributions Benefits Act" without "and". | Quoted as printed; the definition is encoded as the benefit named in the quotation (a constructor of `Benefit`). Nothing is repaired. | Repair the typo or supply the repealed words. | uc-core.l4 |
| F10 | regs 3(3), 22(3), 78(2); lines 123, 474, 1268-1270 | The text speaks of a claimant who "is a member of a couple, but makes a claim as a single person". It has no name for the claim bases. | The keel names three: `a single claimant`, `joint claimants`, `a single claimant who is a member of a couple`. `reg 2 — the claimant has a partner` is TRUE for the last two. Membership of a couple is the Act’s section 39, a stated input. | Two constructors, with the couple status as a separate BOOLEAN. | uc-core.l4, uc-core-persons.l4 |
| F11 | reg 73(2); Sch 4 para 7(2); Sch 5 para 13(3); lines 1189-1192, 2195-2199, 2684-2688 | Regulation 73(2) lists weekly, four-weekly, three-monthly and annual payments; the two schedules also list two-weekly. All say "so for example". | One table in the core, with all six intervals, for all three users. A piece that wants regulation 73(2)’s list alone simply does not use `two-weekly payments`. | Three tables, one per place. | uc-core.l4 |
| F12 | reg 2 "terminally ill"; line 108 | "Can reasonably be expected within 12 months": is 12 months itself within it? Who supplies the expectation? | Inclusive: an expectation of 12 months or fewer. The expectation is a clinician’s estimate, so the number of months is a stated input; it is never read when there is no progressive disease, and a seat layer may put any placeholder there. | Exclusive: fewer than 12. | uc-core-persons.l4 |
| F13 | reg 2 "foster parent"; lines 48-51 | England and Wales say "a person with whom a child is placed under" the Regulations; Scotland says "a foster carer or kinship carer with whom a child is placed". Which nation is "in relation to"? | The nation in which the child is placed. England and Wales: placement under the placement Regulations is enough. Scotland: placement under the 2009 Regulations AND being a foster carer or kinship carer. Whether the placement is under the Regulations is a stated input (the Regulations are not inputs). | Require foster-carer status in England and Wales too. | uc-core-persons.l4 |

## What the stable binary does not accept

Probed means: tried by the keel on the stable binary, 1.6.98, on 2026-10-22.
Stated means: taken from the brief and from `dialects.md`, and not re-probed by the keel.

| construct | probed or stated | write instead / consequence |
| --- | --- | --- |
| `YMD` does not exist; `Date day month year` does | probed | the core defines the shim, `YMD year month day`. `add months` and `add years` exist and clamp the day (31 August plus 6 months is 28 February; 29 February 2024 plus 1 year is 28 February 2025). |
| `Day` is overloaded (three definitions in `daydate`) | probed | `#CHECK Day` is an error. Do not `#CHECK` an overloaded name. |
| `TRUNC` takes two arguments | probed | `TRUNC amount 0`, not `TRUNC amount`. |
| `AND` and `OR` at the same indentation level in one expression | probed | A `DiagnosticSeverity_Warning`: "AND and OR operators appear at the same indentation level". check.sh does not count warnings. Parenthesise every operand and split the expression into helper rules. |
| A bodiless `DECLARE Thing` | probed | Rejected ("unexpected end of input"). Give a type a field. |
| `#ASSERT REFUSED` | probed | Rejected (`REFUSED` has no definition). There is no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`; return an explicit "not covered" value and assert it. |
| A hyphenated module name in `IMPORT` | probed | Needs backticks: ``IMPORT `uc-core` ``. |
| Two modules declaring the same type, rule or bare constructor word | probed | See Instructions to the pieces, item 4. |
| Imports | probed | Transitive; a repeated `IMPORT` is harmless; a module in another folder is not found (stated). |
| A two-line `#ASSERT` with an indented continuation | probed | `l4 check` accepted it. The brief says a continuation line is rejected; keep every `#ASSERT` on one line. |
| `NOT a EQUALS b` | probed | `l4 check` accepted `NOT t’s a EQUALS 1` without a diagnostic. The brief says `NOT a AND b` parses as `NOT (a AND b)`. Parenthesise every `NOT` anyway. |
| No section `GIVEN`, no `TYPICALLY` on a field, no sets, no `@lang`, no `@infixl` | stated | Every rule takes its own `GIVEN`s. |
| `WAIT UNTIL` | stated | Spelled `WAITUNTIL`. |
| `OF` positional construction | stated | Silently order-dependent; the keel builds records with `WITH` and names every field. |
| Comparing a `DEONTIC` value with `EQUALS` | stated | Not accepted. |
| Field names beginning `is` or `has` | stated | The genitive `’s` supplies the verb; the keel uses none. |

## What check.sh prints

The compiler is `1.6.98 (main, 7689b0d, 2026-10-19)`.
Command, from the encodings folder: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
The brief says to run check.sh with `L4_TARGET=unstable`, so it prints "the target is unstable, so the main check was skipped" on stderr (the last line below).
The binary that ran every module is the stable build 1.6.98 itself, so there is no second compiler to compare it with.

```
module                                    errors satisfied  failed  refused  expected
uc-core-bodies.l4                              0         0       0        0         0
uc-core-payments.l4                            0         0       0        0         0
uc-core-persons.l4                             0         0       0        0         0
uc-core-tests-bodies.l4                        0        34       0        0         0
uc-core-tests-core.l4                          0        32       0        0         0
uc-core-tests-payments.l4                      0        11       0        0         0
uc-core-tests-persons.l4                       0        67       0        0         0
uc-core.l4                                     0         0       0        0         0
TOTAL (8 modules)                              0       144       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
check.sh: the target is unstable, so the main check was skipped.
```

`python3 -I srcrefs.py check --refs` over every `.l4` file in the folder:

```
srcrefs check: 184 src: lines, 51 runs, 60 locators, 0 problems
```

`python3 -I srcrefs.py check --strict` over the same files:

```
srcrefs check: 184 src: lines, 51 runs, 60 locators, 0 problems
```

Warnings and errors, counted by grepping `l4 run` output for `DiagnosticSeverity_Warning` and `DiagnosticSeverity_Error` on each of the 8 modules: 0.
