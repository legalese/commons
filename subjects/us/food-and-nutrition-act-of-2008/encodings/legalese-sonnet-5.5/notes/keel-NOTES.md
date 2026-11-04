# NOTES: Food and Nutrition Act of 2008 (7 U.S.C. ch. 51), the keel range: lines 1-135 (s 2011 and s 2012)

Status, 2026-11-04.
Written by the keel agent for row `iaw-snap-k`, on the stable binary 1.6.98 (`l4-stable-98`).
Where a claim says "run", a command was run on the files as they stand; where it says "read", I read the cited lines of `usc07-ch51.txt`.
Nothing here is verified against the official text, and no lawyer has read it.

## What the source is

`usc07-ch51.txt` is a plain-text rendering made by a converter script from the Office of the Law Revision Counsel's USLM XML (release point Public Law 119-121).
It is not the official text.
Its own header says it keeps the section text, tables and source credits and omits the editorial and statutory notes.
Title 7 is not positive law, so the Statutes at Large remain the legal evidence (the same header says so).
Because the notes are omitted, a cross-reference that says "See References in Text note below" points at nothing in this file (line 137, s 2012a, in snap1's range).
`fna-snap-cola-fy2027.txt` (the USDA's fiscal-year 2027 cost-of-living page) is input data, not statute.
No quotation in the `.l4` files was typed: every `-- src:` line was copied from the raw file by `tools/expand-quotes.py`, and `srcrefs.py check --refs` compares each one back to the file.

## The seat

The individual household member who applies for, or receives, benefits under the Supplemental Nutrition Assistance Program, asking on facts they can state whether the household is eligible, how its income and deductions count, what its allotment is, what disqualifies a member, and what follows from a violation.
The keel's range holds the definitions those questions use, not the questions.
So there is no `@export` here: the seat layer belongs to the parts.
Each s 2012 function takes the facts a member could state about a person, a card, a seller or a meal, and answers `MAYBE BOOLEAN`.

## Files

| file | what it is | size (run: `wc -l`, `grep -c`) |
| --- | --- | --- |
| `snap-core.l4` | the shared nouns: 16 `DECLARE`s, no rule, no directive | 160 lines |
| `snap-definitions.l4` | s 2012 (a)-(v) as 48 `MEANS` functions, with the facts only one definition reads | 1147 lines, 64 `@ref` locators, 68 `FALSE-kind` and 21 `NOTHING-kind` comments |
| `snap-definitions-tests.l4` | one assertion per branch and per side of every threshold, written from the text before running | 503 lines, 265 `#ASSERT` |
| `PLAN.md` | what each part agent should expect, and the seams | |
| `NOTES.md` | this file | |
| `PROGRESS.md` | the state of the work | |
| `tools/expand-quotes.py` | copies `--QUOTE` lines out of the raw text into `-- src:` lines | the delivered files contain no `--QUOTE` lines |
| `tools/verify-quotes.py` | checks that the words quoted inside each `FALSE-kind` and `NOTHING-kind` comment occur in the raw text | prints a count; exit 1 on a miss |

## Coverage table (lines 1-135 of `usc07-ch51.txt`)

Dispositions are `encoded`, `inert` (with its reason number), `fork` and `repealed or blank in this text`.
Inert reasons: (1) not operative, (2) machinery, (3) text shown repealed or blank.
A function named `s 2012(x) ...` is in `snap-definitions.l4`; its tests are in `snap-definitions-tests.l4`.

| lines | provision | disposition | where |
| --- | --- | --- | --- |
| 1-17 | converter header, source note, title 7 and chapter 51 headings | inert (1) | not operative: a file header and headings |
| 18 | s 2011 heading | inert (1) | a heading |
| 19 | s 2011, declaration of policy, first paragraph, ending "a supplemental nutrition assistance program is herein authorized" | inert (1) | a policy and findings clause; creates no rule, and the program's operative terms begin at s 2013 (snap1) |
| 20 | s 2011, second paragraph ("That program includes as a purpose to assist low-income adults in obtaining employment...") | inert (1) | a purpose clause; creates no rule |
| 21 | s 2011 source credit | inert (1) | not operative: an editorial history of enactments |
| 22 | blank line | repealed or blank in this text | blank |
| 23 | s 2012 heading | inert (1) | a heading |
| 24 | s 2012 chapeau, "As used in this chapter, the term:" | inert (1) | it only introduces the definitions; the reach "in this chapter" is why every part asks a s 2012 answer as an input (`PLAN.md`) |
| 25 | (a) access device | encoded | `s 2012(a) the thing is an access device` |
| 26 | (b) allotment | encoded | `s 2012(b) the allotment for the month` (a sum, `NUMBER`) |
| 27 | (c) allowable medical expenses | encoded | `s 2012(c) the expenditure is an allowable medical expense` |
| 28-31 | (d) benefit | encoded | `s 2012(d) the assistance is a benefit` |
| 32-33 | (e) benefit issuer | encoded | `s 2012(e) the entity is a benefit issuer` |
| 34 | (f) certification period: the 12 and 24 month limit | encoded | `s 2012(f) the certification period is within the limit` |
| 34 | (f) certification period: at least one contact every 12 months | encoded | `s 2012(f) the State agency has had the required contact` |
| 34 | (f) last sentence: the limits "may be extended until the end of any transitional benefit period established under section 2020(s)" | encoded | the `NOTHING` branch (points outside the text) of both (f) functions; the extension is snap4's |
| 35 | (g) coupon | fork | F-1: `s 2012(g) the thing is a coupon` (taken) and `s 2012(g) the thing is a coupon, on the reading that "issued in lieu of a coupon" qualifies every kind` |
| 36 | (h) drug addiction or alcoholic treatment and rehabilitation program | encoded | `s 2012(h) the program is a drug addiction or alcoholic treatment and rehabilitation program` |
| 37-38 | (i) EBT card | encoded | `s 2012(i) the card is an EBT card` |
| 39-40 | (j)(1) sixty years of age or older | encoded | `s 2012(j)(1) the member is sixty years of age or older` |
| 41-43 | (j)(2) supplemental security income and like benefits | encoded | `s 2012(j)(2) the member receives supplemental security income or a like benefit` |
| 44 | (j)(3) disability or blindness payments | encoded | `s 2012(j)(3) the member receives disability or blindness payments` |
| 45-47 | (j)(4) veteran | encoded | `s 2012(j)(4) the member is a veteran with a total disability or in need of aid and attendance` |
| 48-50 | (j)(5) surviving spouse of a veteran | encoded | `s 2012(j)(5) the member is a surviving spouse of a veteran with the listed status` |
| 51-53 | (j)(6) child of a veteran | encoded | `s 2012(j)(6) the member is a child of a veteran with the listed status` |
| 54 | (j)(7) railroad retirement annuity | encoded | `s 2012(j)(7) the member receives a railroad retirement annuity of the listed kind` |
| 39-54 | (j) the term as a whole | encoded | `s 2012(j) the member is an elderly or disabled member` (with the helper `s 2012(j) one of the limbs holds`) |
| 55 | (k) food: the introductory clause and clauses (1) to (9) | encoded | `s 2012(k) the item or meal is food`, with `s 2012(k)(3) the meal is food`, `(4)`, `(6) the equipment is food` and `(9)`; clauses (5), (7) and (8) are branches of the first |
| 56-62 | (l) homeless individual | encoded | `s 2012(l) the individual is a homeless individual` |
| 64-66 | (m)(1) household | encoded | the first limbs of `s 2012(m) the individual or group is a household` |
| 67 | (m)(2) spouses, parents and children, children under parental control | encoded | `s 2012(m)(2) the pair is treated as customarily purchasing and preparing meals together` |
| 68 | (m)(3) a person sixty or older unable to buy and prepare food | encoded | `s 2012(m)(3) the individual is considered an individual household with the spouse` |
| 69 | (m)(4) "In no event ... institution or boarding house ... pay compensation ... for meals" | fork | F-5: `s 2012(m)(4) the individual or group may constitute a household` |
| 70-75 | (m)(5) persons not residents of institutions | fork | F-3 (is (A) one class or two) and F-5: `s 2012(m)(5) the person is not a resident of an institution and is an individual household` |
| 63-75 | (m) the paragraphs combined | fork | F-5 decides the order: `s 2012(m) the individual or group is a household` |
| 76 | (n) reservation | encoded | `s 2012(n) the area is a reservation` |
| 77-81 | (o)(1) the establishment, route or online entity, with its 7-foods and 50-percent tests | encoded | `s 2012(o)(1) the seller is a retail food store under paragraph (1)` (the closing words "as determined by visual inspection, sales records..." are not modelled, see Limits) |
| 82-84 | (o)(2), (o)(3), (o)(4) | encoded | facts of `s 2012(o) the seller is a retail food store` |
| 85-94 | (o)(5) the purchasing and delivery service | encoded | `s 2012(o)(5) the service is a retail food store under paragraph (5)` |
| 77-94 | (o) the five paragraphs combined (the "and" before (5)) | fork | F-2: `s 2012(o) the seller is a retail food store` |
| 95 | (p) Secretary | encoded | `s 2012(p) the officer is the Secretary` |
| 96-102 | (q) staple foods | encoded | `s 2012(q) the food is a staple food` |
| 103 | (r) State | encoded | `s 2012(r) the place is a State` |
| 104 | (s) State agency | encoded | `s 2012(s) the body is a State agency` |
| 105 | (t) supplemental nutrition assistance program | encoded | `s 2012(t) the program is the supplemental nutrition assistance program` |
| 106-111 | (u)(1) the thrifty food plan and its three conditions | encoded | `s 2012(u)(1) the plan is the thrifty food plan` |
| 112-122 | (u)(2) the household ratios | fork | F-4: `s 2012(u)(2) the household adjustment ratio` |
| 123-127 | (u)(3) cost adjustments | encoded | `s 2012(u)(3)(A) the Secretary must make a cost adjustment for the area`, `(B) the plan cost for Guam or the Virgin Islands`, `(C) the Secretary must adjust the cost to reflect the Consumer Price Index on the date` |
| 128-130 | (u)(4)(A) re-evaluation not earlier than 1 October 2027 | encoded | `s 2012(u)(4)(A) the Secretary may re-evaluate the market baskets on the date` |
| 131-132 | (u)(4)(B) cost neutrality | encoded | `s 2012(u)(4)(B) the cost after a re-evaluation is allowed` |
| 133 | (v) tribal organization | encoded | `s 2012(v) the body is a tribal organization` |
| 134 | s 2012 source credit | inert (1) | not operative: an editorial history of enactments |
| 135 | blank line | repealed or blank in this text | blank |

Line 63 is the bare "(m)" and line 64 the "(1)" heading of paragraph (m).
No provision in lines 1-135 is shown repealed.

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives every reading, the words that license it, and the rule that encodes the reading taken.
Only the reading taken is a rule, except F-1, where both are.
"Assumed, not ruled" applies to every choice: no lawyer has ruled on any of them.

### F-1. s 2012(g), line 35: what does "issued in lieu of a coupon" qualify?

The words are: "“Coupon” means any coupon, stamp, type of certificate, authorization card, cash or check issued in lieu of a coupon."

| reading | licensed by | outcome that differs |
| --- | --- | --- |
| R1 (taken): it qualifies only "cash or check" | proximity: the phrase follows the last two items, and a coupon issued in lieu of a coupon would be an odd thing to say of the first four | a stamp, a type of certificate or an authorization card is a coupon whatever it was issued for |
| R2: it qualifies every item in the list | the list has no comma before "issued in lieu of", so the phrase can govern the whole series | a stamp issued for another reason is not a coupon |

R1 is `s 2012(g) the thing is a coupon`.
R2 is `s 2012(g) the thing is a coupon, on the reading that "issued in lieu of a coupon" qualifies every kind`.
Both are tested, and the two functions are asserted to disagree on a stamp issued for another reason.
Cash or a check that was not issued in lieu of a coupon is `JUST FALSE` on both readings.

### F-2. s 2012(o), lines 77-94: does the "and" before paragraph (5) make the five paragraphs cumulative?

The words are: "“Retail food store” means— (1) ...; (2) ...; (3) ...; (4) ...; and (5) ...".

| reading | licensed by | outcome that differs |
| --- | --- | --- |
| R1 (taken): five alternative kinds of seller | each paragraph names a different kind of seller (a store or route in (1), the places in (k) in (2), a hunting and fishing store in (3), a cooperative or a farmer in (4), a delivery service in (5)); "and" ends the list | an ordinary grocery store that meets (1) is a retail food store |
| R2: a seller must meet all five | the literal "and" after (4) | no seller could meet all five at once, as they name different kinds of seller; this is my reading of the five descriptions, not a decision I found in the text |

R1 is `s 2012(o) the seller is a retail food store`.
R2 is not a function: a caller who wants it combines the five paragraph answers with `AND`.

### F-3. s 2012(m)(5)(A), line 71: one class of person or two?

The words are: "Residents of federally subsidized housing for the elderly, disabled or blind recipients of benefits under title I, II, X, XIV, or XVI of the Social Security Act."

| reading | licensed by | outcome that differs |
| --- | --- | --- |
| R1 (taken): two classes, (i) residents of federally subsidized housing for the elderly, and (ii) disabled or blind recipients of benefits under the listed titles | the comma after "elderly" separates two noun phrases | a resident of subsidized elderly housing who gets no disability benefit is an individual household, and so is a disabled or blind recipient who does not live in such housing |
| R2: one class, residents of federally subsidized housing for the elderly who are also disabled or blind recipients | "residents of ... housing for the elderly, disabled or blind recipients" read as one description | only a person who is both qualifies |

R1 is the first two fields of `s 2012(m)(5) person`, either of which suffices.
R2 is not a function: a caller who wants it ANDs the two fields.
Tested: each field alone gives `JUST TRUE`.

### F-4. s 2012(u)(2)(I), line 122: what does the 200 percent cap?

The words are: "For a household of 9 persons or more, an additional 22 percent per person, which additional percentage shall not total more than 200 percent."

| reading | licensed by | outcome that differs |
| --- | --- | --- |
| R1 (taken): the additional percentage over the 8-person 180 percent is capped at 200 percent, so the ratio never exceeds 1.80 + 2.00 = 3.80 | "which additional percentage shall not total": the cap is on the sum of the additions | for 9 persons the ratio is 1.80 + 0.22 = 2.02; it stops growing at 18 persons, because 10 additions of 0.22 exceed 2.00 |
| R2: the ratio itself may not exceed 200 percent | "200 percent" is the same unit as the ratios in (A) to (H), each a percentage of the 4-person allotment | every household of 9 or more would get exactly 2.00 times the 4-person figure |

R1 is `s 2012(u)(2) the household adjustment ratio`.
Evidence outside the Act, checked by reading `fna-snap-cola-fy2027.txt`: its maximum-allotment table says "9-17 | $225 per additional person" and "18+ | $3,887", and $3,887 = $1,841 + 2 x $1,023 (the 8-person and 4-person figures for the 48 States), which is R1; $225 is 22 percent of $1,023 rounded.
That page is the USDA's reading, not the Act's words, so it supports R1 without settling it.

### F-5. s 2012(m)(4) against (m)(5), lines 69-75: does paragraph (5) override paragraph (4) wholly?

The words are paragraph (4): "In no event shall any individual or group of individuals constitute a household if they reside in an institution or boarding house, or else live with others and pay compensation to the others for meals."
And paragraph (5): "For the purposes of this subsection, the following persons shall not be considered to be residents of institutions and shall be considered to be individual households".

| reading | licensed by | outcome that differs |
| --- | --- | --- |
| R1 (taken): a person in (5) is an individual household whatever (4) says | "shall be considered to be individual households" is affirmative, and (5) is the specific list | a (5) person who also pays others for meals is a household |
| R2: (5) defeats only the "institution or boarding house" limb of (4) | (5) says only that these persons are not "residents of institutions"; "In no event" in (4) is the stronger phrase, and its second limb is about meals, not institutions | a (5) person who pays others for meals is still barred |

R1 is the order of the branches in `s 2012(m) the individual or group is a household`: the (5) branch comes before the (4) branch.
Tested: a person in subsidized housing for the elderly who is also barred by (4) is a household (`JUST TRUE`).
R2 is not a function.

## Reading a result: FALSE and NOTHING

### Reading a result: FALSE and NOTHING

Every s 2012 function answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.
Run on the stable binary, a function whose `GIVETH` is `MAYBE BOOLEAN` returns exactly one of the three.

What `JUST TRUE` is: the text says yes.
A person aged 60 is an elderly or disabled member because paragraph (j)(1) says so.

What `JUST FALSE` is in this subject: the text says no in its own words.
Almost all of these come from one source, the Act's own word "means".
Section 2012 defines each term with "means", so a case that matches none of a definition's limbs is not that thing: a seller that meets none of the five paragraphs is not a retail food store.
The others are flat negatives ("shall not exceed 12 months", "do not include accessory food items", "In no event shall", "shall not increase"), the word "except", and a condition the text introduces with "if", "when", "while" or "unless" that the case fails.
Each such branch carries a `-- FALSE-kind (the text says no in its own words): "<the quoted words>"` comment, and `tools/verify-quotes.py` checks that the words occur in the raw text (run: 99 pieces checked, 0 not found).

What `NOTHING` is, "not covered": the text does not say.
It has these causes in this row, with the number of branches that carry each `NOTHING-kind` label (run: `grep -o`):

| `NOTHING-kind` | branches | example |
| --- | --- | --- |
| points outside the text | 11 | whether the Secretary has determined that "other means" count as a benefit, that a State benefit meets the title XVI criteria, or that a tribal organization is capable (the caller cannot say whether the Secretary has determined it); whether a private establishment is permitted under section 2018(h); whether a period falls in a transitional benefit period under section 2020(s) |
| silent | 5 | a household size below 1 has no ratio; a day other than 1 October has no duty in (u)(3)(C); paragraph (m)(4) says who may not be a household and not who may |
| list not closed | 2 | "accessory food items, such as coffee, tea, cocoa..." does not say that a given other food is not one; paragraph (m)(5) lists persons and does not say that no one else qualifies |
| limited by its own wording | 3 | paragraph (m)(2) deems only parents with children 21 or younger and children under 18 "(excluding foster children)"; paragraph (m)(3) reaches only a person who lives with others, is sixty or older, and cannot buy and prepare food; (u)(4)(A) says "Not earlier than October 1, 2027" and does not say what the Secretary may do before |
| includes | 0 | none used: the "including" phrases in (a), (c), (l) and (o)(4) are folded into the facts the caller states |
| undefined term | 0 | none used: "adult" in (f), and the borrowed terms of title 38, title XIX and 25 U.S.C. 5304, are asked as facts |

Three rules for a caller.
Never turn `NOTHING` into `FALSE`: a missing determination of the Secretary is not a "no".
A `JUST FALSE` from one limb, such as `s 2012(j)(1)` for a member aged 59, answers that limb only; ask `s 2012(j) the member is an elderly or disabled member` for the term.
A `JUST FALSE` from `s 2012(m)(4)` means the group may not constitute a household; `NOTHING` from it means only that paragraph (4) does not bar them.
A `NOTHING` from `s 2012(m)(2)` or `s 2012(m)(3)` means only that the deeming does not reach the case: ask `s 2012(m) the individual or group is a household`, whose "means" closure gives the no when the pair does not in fact buy and cook together.
Every input that carries a determination of the Secretary has three values, and the caller picks the one that is true: `JUST TRUE` is "the Secretary has made the determination", `JUST FALSE` is "the Secretary has made no such determination, or made the opposite one", and `NOTHING` is "I cannot say whether the Secretary has".
So a caller who knows that no determination exists passes `JUST FALSE` and gets the text's no for a failed "if"; only a caller who does not know gets `NOTHING` back.

## Marginal readings for a lawyer

The rule of 2026-10-29 (assumed, not ruled by a lawyer) takes two readings as the status quo and asks that every branch resting on one be listed with the other reading stated.
(a): a failed "if" (or "when", "except", "unless", "subject to the conditions that") counts as the text's no, clause by clause, within the provision that holds it, and a flat negative counts as the text saying no.
(b): a prohibition or grant limited by its own wording does not.
I derived the lists by running `grep -n FALSE-kind snap-definitions.l4` filtered for condition and negation words (if, when, unless, except, excluding, only, shall not, do not, does not, may not, no event, not more than, but not, other than, must, shall), then reading the whole file against them; I did not rely on the in-code "Marginal readings" pointers alone (there are seven).
Not listed, because the brief names them as the text's own no: a case that falls out of a definition's closed list under "means" (every `OTHERWISE JUST FALSE` that quotes the definition's opening words), and a limb of the Act's own list that the caller does not satisfy.
The functions are cited by name; `grep -n` finds the branch.

### Reading (a): a failed condition, or a flat negative, answered `JUST FALSE`

For every row the other reading is `NOTHING`: the text does not say what follows when the condition fails, because "if A then B" is not "if not A then not B".

| id | function | branch answered `JUST FALSE` | the words |
| --- | --- | --- | --- |
| MA-1 | `s 2012(c) the expenditure is an allowable medical expense` | a health and accident or income maintenance policy | "(excluding the costs of health and accident or income maintenance policies)" |
| MA-2 | `s 2012(d) the assistance is a benefit` | the Secretary determined that the other means do not count | "other means of providing assistance, as determined by the Secretary" |
| MA-3 | `s 2012(f) the certification period is within the limit` | longer than 12 months without all adults elderly or disabled, or longer than 24 months | "shall not exceed 12 months, except that ... up to 24 months if all adult household members are elderly or disabled" |
| MA-4 | `s 2012(f) the State agency has had the required contact` | no contact in the 12 months | "shall have at least 1 contact with each certified household every 12 months" (a duty with a numeric floor; whether failing it is "the text says no" is the open point) |
| MA-5 | `s 2012(j)(2) the member receives supplemental security income or a like benefit` | the Secretary determined the (2)(B) benefits are not as stringent | "if the Secretary determines that such benefits are conditioned on meeting disability or blindness criteria at least as stringent" |
| MA-6 | `s 2012(j)(7) the member receives a railroad retirement annuity of the listed kind` | either "if" fails (the service counted as "employment"; an application for disability benefits filed) | "if the individual's service ... had been included in the term “employment” ... and if an application for disability benefits had been filed" |
| MA-7 | `s 2012(k) the item or meal is food` | an alcoholic beverage; tobacco (two branches) | "except alcoholic beverages, tobacco" |
| MA-8 | `s 2012(k) the item or meal is food` | a hot food not authorized under clauses (3), (4), (5), (7), (8) or (9) | "hot foods or hot food products ready for immediate consumption other than those authorized pursuant to clauses (3), (4), (5), (7), (8), and (9)" |
| MA-9 | `s 2012(k)(6) the equipment is food` | equipment for transportation, clothing or shelter, or a firearm, ammunition or explosive | "(but not equipment for purposes of transportation, clothing, or shelter, and not firearms, ammunition, and explosives)" |
| MA-10 | `s 2012(k)(6) the equipment is food` | the Secretary determined the area is not extremely difficult to reach stores | "if the Secretary determines that such households are located in an area of the State where it is extremely difficult to reach stores selling food" |
| MA-11 | `s 2012(m)(3) the individual is considered an individual household with the spouse` | the income of the others exceeds the poverty line by more than 65 percent | "if the income ... of the others, excluding the spouse, does not exceed the poverty line ... by more than 65 per centum" (this answer means only that paragraph (3) does not deem them a household; paragraphs (1) and (2) still can) |
| MA-12 | `s 2012(m)(4) the individual or group may constitute a household`, and `s 2012(m) the individual or group is a household` | resides in an institution or boarding house, or pays compensation for meals (one branch in each function) | "In no event shall any individual or group of individuals constitute a household if they reside in an institution or boarding house, or else live with others and pay compensation to the others for meals" (a flat negative; see also F-5) |
| MA-13 | `s 2012(q) the food is a staple food` | coffee, tea, cocoa, drinks, candy, condiments and spices | "“Staple foods” do not include accessory food items, such as coffee, tea, cocoa, carbonated and uncarbonated drinks, candy, condiments, and spices." |
| MA-14 | `s 2012(u)(1) the plan is the thrifty food plan` | any of the three conditions (A), (B), (C) fails | "subject to the conditions that— (A) ...; (B) ...; and (C) ..." (read as "if" limbs) |
| MA-15 | `s 2012(u)(4)(B) the cost after a re-evaluation is allowed` | the cost after re-evaluation is higher than before | "The Secretary shall not increase the cost of the thrifty food plan based on a re-evaluation under this paragraph." (a flat negative; a cost that does not rise is `NOTHING`, because the text forbids a rise and does not say a non-rise is permitted) |
| MA-16 | `s 2012(s) the body is a State agency` | a tribal organization the Secretary determined is not capable | "the tribal organization of an Indian tribe determined by the Secretary to be capable of effectively administering a food distribution program" |

Rows MA-2, MA-5, MA-10 and MA-16 rest on a determination of the Secretary.
Their input has three values (see "Reading a result"), so the failed "if" gives `JUST FALSE` when the caller says the Secretary has made no such determination, and `NOTHING` only when the caller cannot say.
The independent review of 2026-11-04 passed `NOTHING` for "no determination yet" (items 11b and 24 below) because the field comments of the first version read "NOTHING: no determination supplied"; those comments are corrected.
The other reading: an unexercised power of the Secretary is a failed "if" whatever the caller knows, so `NOTHING` input should also give `JUST FALSE`; I did not take it, because it would turn "unknown" into "no".

### Reading (b): a limit in the text's own wording

Two kinds of row.
First, the branches answered `JUST FALSE` where the case has the category of a limb but fails the limb's own qualifier.
The taken reading is that the qualifier is part of what a "means" definition means, so a case that fails it is outside the closed list.
The other reading is `NOTHING`: "when", "in the case of", a stated period or a named complement limits the grant in its own wording, and the text does not say what happens outside the limit.

| id | function | the case answered `JUST FALSE` | the limit |
| --- | --- | --- | --- |
| MB-1 | `s 2012(c) the expenditure is an allowable medical expense` | prescription drugs not prescribed by a licensed practitioner; over-the-counter medication not approved by one; eye glasses not prescribed by a physician skilled in eye disease or an optometrist; transport that is not reasonable and necessary; an attendant or child care not due to age, infirmity or illness | "when prescribed by a licensed practitioner authorized under State law", "when approved by a licensed practitioner or other qualified health professional", "prescribed by a physician skilled in eye disease or by an optometrist", "reasonable costs of transportation necessary to secure medical treatment or services", "due to age, infirmity, or illness" |
| MB-2 | `s 2012(g) the thing is a coupon` | cash or a check not issued in lieu of a coupon | "issued in lieu of a coupon" (see F-1) |
| MB-3 | `s 2012(k) the item or meal is food` | a deposit fee that is not in excess of the State reimbursement; seeds and plants not for a garden for the household's own food | "in excess of the amount of the State fee reimbursement (if any)", "for use in gardens to produce food for the personal consumption of the eligible household" |
| MB-4 | `s 2012(k)(3)`, `(k)(4)`, `(k)(6)`, `(k)(9)` meal and equipment functions, and the branches for clauses (5), (7) and (8) | a meal or equipment outside the case the clause names (the eater is not in the class; the meal is not delivered to the home; the household is not in Alaska; the provider is not one of the two named) | "in the case of ..." in each clause |
| MB-5 | `s 2012(l) the individual is a homeless individual` | a temporary accommodation in another person's residence for more than 90 days | "(C) a temporary accommodation for not more than 90 days in the residence of another individual" (a stated period) |
| MB-6 | `s 2012(o)(1) the seller is a retail food store under paragraph (1)` | fewer than 7 foods in a category, or perishables in fewer than 3 categories, and not over 50 percent of sales in staples (exactly 50 percent is not "over") | "a variety of at least 7 foods in each of the 4 categories ... including perishable foods in at least 3 of the categories", "over 50 percent of the total sales" |
| MB-7 | `s 2012(o)(5) the service is a retail food store under paragraph (5)` | any of the three conditions (A), (B), (C) fails | "a governmental or private nonprofit food purchasing and delivery service that— (A) ...; (B) ...; and (C) ..." |
| MB-8 | `s 2012(r) the place is a State` | a reservation of an Indian tribe whose tribal organization does not meet the requirements of the chapter | "the reservations of an Indian tribe whose tribal organization meets the requirements of this chapter for participation as a State agency" |

Second, the three branches answered `NOTHING` because the text limits itself, where a lawyer may prefer `JUST FALSE`.

| id | function | the case answered `NOTHING` | the other reading |
| --- | --- | --- | --- |
| MB-9 | `s 2012(m)(3) the individual is considered an individual household with the spouse` | a person who is under sixty, or does not live with others, or can buy and prepare food, or has no physician's certificate | `JUST FALSE`: paragraph (3) reaches only "an individual who lives with others, who is sixty years of age or older, and who is unable to purchase food and prepare meals" |
| MB-10 | `s 2012(u)(4)(A) the Secretary may re-evaluate the market baskets on the date` | any date before 1 October 2027 | `JUST FALSE`: "Not earlier than October 1, 2027, the Secretary may re-evaluate" can be read as a bar before that date |
| MB-11 | `s 2012(m)(2) the pair is treated as customarily purchasing and preparing meals together` | a parent with a child over 21; a foster child; a child 18 or over under parental control of a non-parent | `JUST FALSE`: the deeming covers "parents and their children 21 years of age or younger" and "children (excluding foster children) under 18 years of age", and "(excluding foster children)" can be read like "except" |

## Jural relations

Hohfeld's correlatives: right and duty, privilege and no-right, power and liability, immunity and disability.
Each relation is stated once, from the holder to the bearer.
Almost all of lines 1-135 are definitions and creates none, so the long run of `none` rows is the finding: the keel's range sets the vocabulary, and the relations (a household against the State agency, a person against the Secretary) are in the parts.
The Secretary's determinations are carried as `MAYBE BOOLEAN` input fields, so for those rows the L4 column names the field, not a rule.
Where the text names no holder of a correlative, the row says so; where I inferred the holder, the row says "inferred".

| lines | provision | holder | bearer | relation | L4 |
| --- | --- | --- | --- | --- | --- |
| 1-22 | front matter, s 2011 (policy and purpose) | none | none | none: a policy statement creates no relation | none |
| 23-24 | s 2012 heading and chapeau | none | none | none | none |
| 25 | (a) access device | none | none | none: a definition | `s 2012(a) the thing is an access device` |
| 26 | (b) allotment | none | none | none: a definition | `s 2012(b) the allotment for the month` |
| 27 | (c) allowable medical expenses | none | none | none: a definition | `s 2012(c) the expenditure is an allowable medical expense` |
| 28-31 | (d) benefit: "other means ... as determined by the Secretary" | the Secretary | a household (its assistance may be delivered by a means the Secretary chooses) | power and liability | field `the Secretary has determined the other means` of `s 2012(d) assistance`, read by `s 2012(d) the assistance is a benefit` |
| 28-31 | (d) benefit, the rest | none | none | none: a definition | `s 2012(d) the assistance is a benefit` |
| 32-33 | (e) benefit issuer | none | none | none: a definition | `s 2012(e) the entity is a benefit issuer` |
| 34 | (f) "shall not exceed 12 months, except ... 24 months" | none named | the State agency (inferred: it certifies) | disability: it cannot certify a longer period | `s 2012(f) the certification period is within the limit` |
| 34 | (f) "A State agency shall have at least 1 contact with each certified household every 12 months" | each certified household (inferred: the text names the household as the object of the contact) | the State agency | claim and duty | `s 2012(f) the State agency has had the required contact` |
| 34 | (f) "The limits ... may be extended until the end of any transitional benefit period established under section 2020(s)" | not named: the power lies in section 2020(s), which is snap4's | not named | power and liability, held elsewhere | the `NOTHING` branch of both (f) functions |
| 35 | (g) coupon | none | none | none: a definition | `s 2012(g) the thing is a coupon` |
| 36 | (h) treatment program | none | none | none: a definition | `s 2012(h) ...` |
| 37-38 | (i) EBT card | none | none | none: a definition | `s 2012(i) the card is an EBT card` |
| 39-54 | (j)(2)(B) "if the Secretary determines that such benefits are conditioned on ... criteria at least as stringent" | the Secretary | the member (its status as elderly or disabled turns on the determination) | power and liability | field `the Secretary determines that the (2)(B) benefits ...` of `s 2012(j) facts about the member` |
| 39-54 | (j) the rest of the paragraphs | none | none | none: a definition | `s 2012(j) the member is an elderly or disabled member` |
| 55 | (k)(6) "if the Secretary determines that such households are located in an area ... extremely difficult to reach stores" | the Secretary | an eligible Alaska household (whether it may buy hunting and fishing equipment with benefits) | power and liability | field `the Secretary determines that the household ...` of `equipment under clause (6)` |
| 55 | (k)(7) "or under standards determined by the Secretary to be comparable" | the Secretary | a group living arrangement | power and liability | carried inside one `BOOLEAN` field of `a meal under clause (7)` (not separated) |
| 55 | (k) the rest | none | none | none: a definition | `s 2012(k) the item or meal is food` |
| 56-62 | (l) homeless individual | none | none | none: a definition | `s 2012(l) the individual is a homeless individual` |
| 63-68 | (m)(1), (2), (3) | none | none | none: definitions and a counting rule | `s 2012(m)(2) ...`, `s 2012(m)(3) ...` |
| 69 | (m)(4) "In no event shall any individual or group of individuals constitute a household" | none named | the individual or group | disability: they cannot constitute a household | `s 2012(m)(4) the individual or group may constitute a household` |
| 70-75 | (m)(5) persons who "shall not be considered to be residents of institutions" | the person named in (A) to (E) (inferred) | the State agency (inferred): it may not treat them as institution residents | immunity and disability | `s 2012(m)(5) the person is not a resident of an institution and is an individual household` |
| 76 | (n) reservation | none | none | none: a definition | `s 2012(n) the area is a reservation` |
| 77-94 | (o) retail food store | none | none | none: a definition | `s 2012(o) the seller is a retail food store` |
| 95 | (p) Secretary | none | none | none: a definition | `s 2012(p) the officer is the Secretary` |
| 96-102 | (q) staple foods | none | none | none: a definition | `s 2012(q) the food is a staple food` |
| 103 | (r) State | none | none | none: a definition | `s 2012(r) the place is a State` |
| 104 | (s)(2) "determined by the Secretary to be capable" | the Secretary | the tribal organization (it becomes a State agency) | power and liability | field `the Secretary determines that the tribal organization is capable ...` of `s 2012(s) agency` |
| 104 | (s) the rest | none | none | none: a definition | `s 2012(s) the body is a State agency` |
| 105 | (t) the program | none | none | none: a definition | `s 2012(t) ...` |
| 106-111 | (u)(1)(A) and (C): the baskets "shall only be changed pursuant to paragraph (4)"; the cost "may only be adjusted in accordance with this subsection" | none named | the Secretary | disability: no power to change the baskets or adjust the cost otherwise | fields of `s 2012(u)(1) plan`, read by `s 2012(u)(1) the plan is the thrifty food plan` |
| 106-111 | (u)(1)(B) "the cost ... shall be the basis for uniform allotments for all households" | households (inferred) | the Secretary (inferred) | claim and duty | the same field |
| 112-122 | (u)(2) "The Secretary shall make household adjustments using the following ratios" | households | the Secretary | claim and duty | `s 2012(u)(2) the household adjustment ratio` |
| 123-125 | (u)(3)(A) cost adjustments for Hawaii and urban and rural Alaska | households in those places (inferred) | the Secretary | claim and duty | `s 2012(u)(3)(A) the Secretary must make a cost adjustment for the area` |
| 126 | (u)(3)(B) plans for Guam and the Virgin Islands, "not to exceed the cost of food in the 50 States" | households there (inferred) | the Secretary | claim and duty, and a disability: no power to exceed the 50-State cost | `s 2012(u)(3)(B) the plan cost for Guam or the Virgin Islands` |
| 127 | (u)(3)(C) the October 1 adjustment | households (inferred) | the Secretary | claim and duty | `s 2012(u)(3)(C) the Secretary must adjust the cost to reflect the Consumer Price Index on the date` |
| 128-130 | (u)(4)(A) "the Secretary may re-evaluate" not earlier than 1 October 2027 | the Secretary | anyone who would object (no-right) | privilege and no-right | `s 2012(u)(4)(A) the Secretary may re-evaluate the market baskets on the date` |
| 131-132 | (u)(4)(B) "shall not increase the cost" | none named | the Secretary | disability: no power to raise the cost by re-evaluation | `s 2012(u)(4)(B) the cost after a re-evaluation is allowed` |
| 133 | (v) tribal organization | none | none | none: a definition | `s 2012(v) the body is a tribal organization` |
| 134-135 | source credit; blank line | none | none | none | none |

## Independent review of the keel range, 2026-11-04

The independent reviewer's tests (`tests-independent.l4`) failed seven assertions in lines 1-135.
Each is judged here against the grounds in the brief: `JUST FALSE` for a "means" definition, a condition the text introduces with "if", "only if", "as long as", "unless" (and "so long as", "while", "until", "except", "save", "provided that"), a list closed with "only", or a flat negative ("does not", "shall not", "may not", "is not entitled"); `NOTHING` for silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
Two readings of the rule are open for a lawyer and no ruling has been made.

| id | verdict | the ground, and why it beats the other |
| --- | --- | --- |
| 6 | reviewer slip | The text: "The limits specified in this subsection may be extended until the end of any transitional benefit period established under section 2020(s) of this title." (line 34). It is a permission ("may be extended") bounded by "until the end of" a period that section 2020(s) fixes, and the end date is not an input. Neither `JUST TRUE` nor `JUST FALSE` follows; `NOTHING` (points outside the text). No code change. |
| 11b | `NOTHING`-kind kept, documentation fixed | "if the Secretary determines that such benefits are conditioned on meeting disability or blindness criteria" (line 43; the reviewer wrote "only if", the text says "if"). Two grounds collide: a failed "if" (`JUST FALSE`) and a power outside the sources (`NOTHING`). The input has three values, so both are met: `JUST FALSE` input ("no determination has been made") returns `JUST FALSE`; `NOTHING` input ("I cannot say") returns `NOTHING`, because `JUST FALSE` there would turn unknown into no. The reviewer passed `NOTHING` for "no determination yet" because my field comment said "NOTHING: no determination supplied" and one of my fixtures was named "Secretary has not decided" with `NOTHING`. Both are corrected; a new fixture asserts `JUST FALSE`. |
| 24 | `NOTHING`-kind kept, documentation fixed | Same as 11b: "if the Secretary determines that such households are located in an area of the State where it is extremely difficult..." (line 55). The `JUST FALSE` finding already returned `JUST FALSE` (existing assertion); the comments are corrected. |
| 33b | `NOTHING`-kind (limited by its own wording) | "parents and their children 21 years of age or younger who live together" (line 67). The deeming grant is limited by a stated age, and a 22-year-old falls outside it. The FALSE grounds do not fit: it is not a "means" clause, not an "if", not a closed list, not a flat negative. The no belongs to the defined term: `s 2012(m)` returns `JUST FALSE` for the pair when they do not in fact buy and cook together (new assertion). The label on the branch is corrected from "silent" to "limited by its own wording". |
| 34 | `NOTHING`-kind (limited by its own wording), a fork with "except" | "children (excluding foster children) under 18 years of age who live with and are under the parental control of a person" (line 67). The words read like "except", which the brief lists for `JUST FALSE`. I rely on the more specific ground: the exclusion is part of how the grant describes its class ("shall be treated as a group ... even if they do not do so"), and the brief names a grant limited by its own wording. Outside the grant the text does not say the foster child and foster parent are not a group; they may in fact buy and cook together. The other reading (`JUST FALSE`) is MB-11. The defined term returns `JUST FALSE` for a foster pair who do not buy and cook together (new assertion). |
| 36 | `NOTHING`-kind (limited by its own wording) | "an individual who lives with others, who is sixty years of age or older, and who is unable to purchase food" (line 68). "Sixty" is in a relative clause, not in an "if"; only the income test is an "if", and a failed income test returns `JUST FALSE` (existing assertion). A 59-year-old is outside the grant; paragraphs (1) and (2) govern ("Notwithstanding paragraphs (1) and (2)"). `s 2012(m)` returns `JUST FALSE` for such a person who does not buy and cook apart (new assertion). |
| 54a | `NOTHING`-kind (limited by its own wording: a stated period) | "Not earlier than October 1, 2027, the Secretary may re-evaluate the market baskets of the thrifty food plan" (line 130). A permission limited by a stated period, which is the brief's own example for `NOTHING`; the negation sits in a time phrase, not in a listed flat negative ("does not", "shall not", "may not"). The other reading (`JUST FALSE`: a bar before the date) is MB-10, and is one of the two open readings (b). |

Changes made: comments only in `snap-definitions.l4` (the field comments of the four Secretary inputs, the matching branch comments, and the label of the paragraph (2) `NOTHING` branch); in `snap-definitions-tests.l4` two fixtures renamed, five assertions added (265 now), no expectation changed.
No function signature, type or exported name changed in either file; `snap-core.l4` is untouched.

## What the stable binary does not accept

The binary governs where a skill describes a construct it rejects.
These were found during this row, and the five below were re-run on 2026-11-04 on `l4-stable-98` (1.6.98) as one-file probes, then deleted:

| what I tried | what the binary did |
| --- | --- |
| `REFUSE` and `#ASSERT REFUSED` | not available (the brief says so; I did not use them). "Not covered" is `NOTHING` in a `MAYBE` result, asserted |
| `length (LIST 1, 2, 3)` | "I could not find a definition for the identifier length". The prelude name used here is `count` |
| an `IF ... THEN ... ELSE IF ... THEN ... ELSE ...` chain | the last line, `ELSE NOTHING`, is rejected: "incorrect indentation (got 10, should be greater than 10)". `BRANCH` with `IF ... THEN ...` lines and a final `OTHERWISE` is what works |
| `NOT a OR b` | parsed as `NOT (a OR b)`: with `f MEANS NOT a OR b`, `f TRUE TRUE` and `f FALSE TRUE` both failed an assertion that expected `TRUE`. Every `NOT` here is parenthesised |
| `DECLARE T IS ONE OF Foo Bar` on one line | a parse error at the second constructor ("unexpected Bar"). One constructor per line works |
| the same constructor name in two `DECLARE`s, or a record field named like a constructor | **loud only at the use site, silent at the declaration**: both files compile with no diagnostic, and the error "There are multiple definitions for the identifier" appears only where the name is used. A module with a clash therefore passes a bare `l4 check`. This is why the tests file ends with a section that names every constructor of every enumeration in the core and builds each record type: it found a clash between `Party` and a `Kind of seller` type I had drafted (both had `a retail food store`), and I removed the second type |

I also did not use `YMD` (dates are `Date day month year`), `WAIT UNTIL`, or `TYPICALLY` on a field; I did not test whether the stable binary rejects them.

## Limits of this encoding

- The text is a converter's rendering; no editorial or statutory note was available. The footnote in s 2012a ("See References in Text note below") cannot be followed, and its letters "(f) and (i)" of section 2012 do not match today's (f) (certification period) and (i) (EBT card). This is snap1's to record.
- Borrowed terms are facts the caller states: title 38 ratings, title XIX assistance, section 221(i) of the Social Security Act, the Railroad Retirement Act, 25 U.S.C. 5304, the Public Health Service Act part B. Nothing here defines them.
- `s 2012(o)(1)` ends with "as determined by visual inspection, sales records, purchase records, counting of stockkeeping units, or other inventory or accounting recordkeeping methods that are customary or reasonable in the retail food industry". That names how the sales share is found, and is not modelled: the caller states the share as a number (a fraction, 0.5 is 50 percent).
- `s 2012(c)` (2): the parenthetical about a person who was a household member before entering a hospital or nursing home is an example of whose care counts, so it adds no field.
- The Act's dates are rules on a date input (`s 2012(u)(3)(C)`, `s 2012(u)(4)(A)`); the amendment history in the source credits is not encoded.
- Money is a `NUMBER` of dollars; a ratio is a fraction (30 percent is 0.30).
- The cost-of-living figures are not in the core: only the row types are (`PLAN.md` says which part fills which table).

## Open questions

1. F-1 to F-5: which reading is right. Each is "assumed, not ruled".
2. MA-4 (`s 2012(f)` contact): is a "shall" duty with a numeric floor "the text says no" when the count is zero, or `NOTHING`?
3. MB-1 to MB-8 and MB-9 to MB-11: reading (b) is applied two ways in this file (qualifier failures are `JUST FALSE` under "means", three self-limiting grants are `NOTHING`). A lawyer may want one rule for both.
4. Does the s 2012a reference to "subsections (f) and (i)" mean today's (h)? Not answerable from this text.

## What check.sh printed (run, 2026-11-04, after the last edit to any `.l4` file, following the independent review)

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
snap-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap-definitions-tests.l4                      0       265       0        0         0 |      0       265       0        0  same
snap-definitions.l4                            0         0       0        0         0 |      0         0       0        0  same
TOTAL (3 modules)                              0       265       0        0           |      0       265       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Also run: `l4 run` on each of the three modules, grepped for `DiagnosticSeverity_Error`, `DiagnosticSeverity_Warning`, "is at the end of the file" and "follows code on its line": 0 hits each.
`python3 -I srcrefs.py check --refs usc07-ch51.txt snap-core.l4 snap-definitions.l4 snap-definitions-tests.l4`: "119 src: lines, 23 runs, 65 locators, 0 problems".
`python3 -I tools/verify-quotes.py usc07-ch51.txt snap-definitions.l4`: "101 quoted pieces checked, 0 not found".
Assertions written (`grep -c '^#ASSERT'`): 265; satisfied: 265.
