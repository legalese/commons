# PLAN: the six part agents for the Food and Nutrition Act of 2008 (7 U.S.C. ch. 51)

Status, 2026-11-04.
Written by the keel agent after encoding lines 1-135 (s 2011 and s 2012).
How the parts below were assigned: `inputs/PARTS.md`, copied unchanged.
How the seams were found: group A from the cross-references written inside the parts' ranges (run: a regex scan of `usc07-ch51.txt` for "section 2012" and for the section numbers, mapped to line ranges); group B from the fields I had to leave open in `snap-definitions.l4`; group C from literal "section 20NN" mentions only.
I read the bodies of s 2011 and s 2012 (lines 1-135) in full, and the cross-reference lines quoted below.
I did not read the other bodies for this plan, so every part-to-part seam in group C is "from references, body not read": a count of mentions, not a finding that the dependence exists.
The source is a converter's plain-text rendering of the Code, not the official text, and nothing here is verified against the official text.

## 1. What you receive and may not do

- You receive `snap-core.l4` and nothing else of mine. It is read-only: never edit it, never wait for it.
- You cannot import another part, and you cannot import `snap-definitions` (it is not given to you). A section 2012 answer you need comes in as an input (section 4).
- The text is lines of `inputs/usc07-ch51.txt`. Quote it mechanically (`-- src:` lines, `@ref` locators), and run `python3 -I srcrefs.py check --refs <raw text> <your .l4 files>` until it reports 0 problems.
- The rule for FALSE and NOTHING (the rule of 2026-10-29) is the same for every part. `NOTES.md` section "Reading a result: FALSE and NOTHING" shows it worked on the definitions, and `## Marginal readings for a lawyer` shows how to list the branches that rest on a failed "if" or a self-limiting wording.

## 2. Naming rules (every part follows them)

1. A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name.
2. Every top-level name a part defines (function, constant, type, constructor not in the core) **begins with the section label it implements, in the form `s 4(2)(a) ...`**: the Act's own numbering, for example `s 2014(d) a household with an elderly member` or `s 2015(f) the individual is an eligible alien`. Parentheses inside a backtick name parse on the stable binary.
3. Types and constructors shared across parts live only in the core. A part may not edit it.
4. If you need a type or constructor the core lacks, define it in your own module under your own section prefix, record it in `NEEDS-CORE.md` in your sandbox, and the lead hoists it into the core at the merge.
5. File names: every module of part `X` begins with `X-` (`snap1-...`). Every module of mine begins with `snap-`.
6. A name the core already has is not yours to define, even in a different type: a constructor shared by two types, or a record field named like a constructor, compiles and errors only where it is used (NOTES.md, "What the stable binary does not accept"). End your tests with a section that touches every constructor and field you declared.
7. Dates are `Date day month year`. Never define a `YMD`. Money is a `NUMBER` of dollars.
8. A seam input (section 4) is a `GIVEN` parameter of the asking function or a field of a record your module declares. It is never a top-level constant, so it cannot collide with another part's name.
9. Keep a file `SEAMS.md` in your sandbox with two lists: ASKS (input name, type, answering section) and ANSWERS (function name, type, section). This is my addition (assumed, not ruled): parts cannot see each other, so the lead needs it to wire the merge by name.

## 3. The core, by type (what `snap-core.l4` holds)

| type | what it is |
| --- | --- |
| `Area` | seven places at the grain of the USDA cost-of-living tables: `the 48 contiguous States and the District of Columbia`, `Alaska, urban`, `Alaska, rural 1`, `Alaska, rural 2`, `Guam`, `Hawaii`, `the Virgin Islands of the United States`. "Rural 1" and "Rural 2" are the USDA's subdivision, not the Act's words |
| `Kind of place` | what kind of place something is for s 2012(r): a State, DC, Guam, the Virgin Islands, a reservation of an Indian tribe, `any other place` |
| `Immigration status` | five values for s 2015(f)(2)(A)-(D): citizen or national, lawful permanent resident, Cuban or Haitian entrant, Compact of Free Association resident, `any other status` |
| `Individual` | eight facts a witness can state: age, physically and mentally fit, pregnant, immigration status, resident of the United States, receives supplemental security income, hours worked per week averaged monthly, enrolled at least half-time in higher education |
| `Income item` | one monthly item: description, monthly amount in dollars, earned income |
| `Household` | the members (a list of `Individual`), where it lives (`Area`), the income items |
| `Party` | twelve parties the Act puts rights, duties, powers and liabilities on, including `the State agency`, `the Secretary`, `a tribal organization`, `a benefit issuer`, `a retail food store`, `a wholesale food concern`, `a sponsor of an alien`, `a court`, `an administrative agency` |
| `Kind of decision` | nine outcomes a decision-maker reaches: certify, deny an application, terminate a certification, reduce an allotment, disqualify an individual, approve a store, disqualify a store, establish a claim for an overissuance, grant a waiver |
| `Period of ineligibility` | seven values: days, months, years, `permanently`, `until a stated condition ends`, and two "not covered" values (`for a period the Secretary prescribes by regulation, not stated in this text`, `for a period the State agency determines, not stated in this text`) |
| `Form of benefit` | the two forms of s 2012(d): an electronic benefit transfer under s 2016(h), other means the Secretary determines |
| `Benefit` | value in dollars, form, the date the month it is for begins |
| `Certification period` | first day, length in months |
| `Claim` | amount in dollars, owed by (`Party`), owed to (`Party`) |
| `Dollars by area`, `Table row`, `Annual table` | the row types for the USDA cost-of-living tables: seven dollar columns, a household size and its dollars, a fiscal year with a description and a list of rows. **No figures are in the core** |

What is deliberately not in the core, because answering it needs the Act: "is an elderly or disabled member", "is a household", "is food", "is a retail food store", "is a State agency", "is eligible". Ask those as inputs (section 4).
The `Period of ineligibility` "not covered" constructors are for a provision that hands the length to the Secretary or the State: answer with one of them, never with a guessed number.

## 4. How to ask a section 2012 answer (the convention for every part)

You cannot import `snap-definitions`. If a provision of yours depends on a s 2012 term, take the answer as an input **named exactly like the function that gives it, and typed as that function's result**.
Nearly all of them return `MAYBE BOOLEAN`, so the input is `MAYBE BOOLEAN`.
A plain `BOOLEAN` input would force the caller to turn `NOTHING` into `FALSE`, which the rule forbids.

```
GIVEN `s 2012(j) the member is an elderly or disabled member` IS A MAYBE BOOLEAN
GIVETH A MAYBE BOOLEAN
`s 2014(e)(5) the household has an excess medical expense deduction` MEANS
    ...
```

Pass `NOTHING` through: if the input is `NOTHING`, your answer is `NOTHING` unless another limb of your rule decides it without that input.

The functions in `snap-definitions.l4`, with their types (all `MAYBE BOOLEAN` unless shown):

| function | takes (summary) |
| --- | --- |
| `s 2012(a) the thing is an access device` | a thing with three facts |
| `s 2012(b) the allotment for the month` | a list of `Benefit` and a month; returns a `NUMBER` |
| `s 2012(c) the expenditure is an allowable medical expense` | an expenditure of one of nine kinds, with the facts each kind needs |
| `s 2012(d) the assistance is a benefit` | the assistance, its form, and the Secretary's determination (a `MAYBE BOOLEAN`) |
| `s 2012(e) the entity is a benefit issuer` | an entity with four facts |
| `s 2012(f) the certification period is within the limit`; `s 2012(f) the State agency has had the required contact` | the period and whether all adults are elderly or disabled; the contacts in 12 months |
| `s 2012(g) the thing is a coupon` (and the F-1 other reading) | the kind of thing, issued in lieu of a coupon |
| `s 2012(h) the program is a drug addiction or alcoholic treatment and rehabilitation program` | the program's four facts |
| `s 2012(i) the card is an EBT card` | two facts |
| `s 2012(j) the member is an elderly or disabled member` (limbs `(j)(1)` to `(j)(7)`) | an `Individual` and 18 facts about the member |
| `s 2012(k) the item or meal is food` (and `(k)(3)`, `(k)(4)`, `(k)(6)`, `(k)(9)`) | what is bought or served, with the facts each clause needs |
| `s 2012(l) the individual is a homeless individual` | the individual's night-time residence |
| `s 2012(m) the individual or group is a household` (and `(m)(2)`, `(m)(3)`, `(m)(4)`, `(m)(5)`) | the circumstances, and the answers of paragraphs (2) to (5) |
| `s 2012(n) the area is a reservation`; `s 2012(p) the officer is the Secretary`; `s 2012(t) the program is the supplemental nutrition assistance program`; `s 2012(v) the body is a tribal organization` | two or three facts each |
| `s 2012(o) the seller is a retail food store` (and `(o)(1)`, `(o)(5)`) | the five paragraphs' answers |
| `s 2012(q) the food is a staple food` | the kind of food |
| `s 2012(r) the place is a State` | a `Kind of place` and whether the tribal organization meets the requirements |
| `s 2012(s) the body is a State agency` | the body's facts and the Secretary's determination |
| `s 2012(u)(1) the plan is the thrifty food plan` | six facts |
| `s 2012(u)(2) the household adjustment ratio` | a household size; returns `MAYBE NUMBER` (a fraction of the 4-person allotment) |
| `s 2012(u)(3)(A) ...`, `(u)(3)(B) ...`, `(u)(3)(C) ...`, `s 2012(u)(4)(A) ...`, `s 2012(u)(4)(B) ...` | an `Area`; two costs (returns a `NUMBER`); a date; a date; two costs |

## 5. The parts

Line ranges are copied unchanged from `inputs/PARTS.md`.
"Sections" are from the section headings (`§` lines) of `usc07-ch51.txt`, mapped to your ranges by line number (run).
"Core names to expect" is a forecast from the headings, not from reading the bodies.
"Defined terms used" counts text matches of the term's wording in your ranges (run); it measures how often the term appears, not how many rules depend on it.

### snap1: lines 136-491, 1341-1424

- Sections: s 2012a (publicly operated community health centers), s 2013 (establishment of the program), s 2014 (eligible households), s 2014a (change of State of residence), s 2018 (approval of retail food stores and wholesale food concerns), s 2019 (redemption of benefits).
- Core names to expect: `Household`, `Individual`, `Income item`, `Area`, `Immigration status`, `Dollars by area`, `Table row`, `Annual table`, `Party` (`a retail food store`, `a wholesale food concern`, `the State agency`, `the Secretary`, `a benefit issuer`), `Kind of decision` (approve and disqualify a store).
- **COLA tables you own** (from `fna-snap-cola-fy2027.txt`, fiscal year 2027, 1 October 2026 to 30 September 2027): the three income standards (Table 1 net monthly limit at 100 percent of the poverty level, Table 2 gross at 130 percent, Table 3 at 165 percent where elderly or disabled members are a separate household), the standard deductions, the maximum excess shelter deductions, the homeless shelter deduction, the maximum asset limits. All feed s 2014. Fill `Annual table` rows and say the fiscal year.
- Defined terms used (text matches): benefit 64, program 33, retail food store 26, elderly or disabled 9, tribal organization 11, reservation 6, certification period 4, treatment and rehabilitation program 3, staple food 2.
- The Act's own definitions inside your ranges, which are yours: "payment error rate" (s 2013), "traditional and locally- and regionally-grown" (s 2013), "earned income" (s 2014), "eligible incentive food" (s 2018). Found by a scan for a quoted term followed by "means" or "has the meaning", so it may miss a form.
- Also yours: s 2012a, which refers to "subsections (f) and (i) of section 2012" (section 6, difficulty 3).

### snap2: lines 492-912, 2698-2730, 2805-2841

- Sections: s 2015 (eligibility disqualifications), s 2027 (appropriations and allotments to States), s 2029 (workfare), s 2030 (repealed: the heading at line 2840 says so; record it as `repealed or blank in this text`).
- Core names to expect: `Individual`, `Household`, `Immigration status`, `Kind of decision` (disqualify an individual, terminate a certification, reduce an allotment, deny an application), `Period of ineligibility` (use the "not covered" constructors where the Act hands the length to the Secretary or the State), `Party`.
- COLA tables you own: none.
- Defined terms used (text matches): benefit 56, program 63, certification period 3, reservation 5, elderly or disabled 1, homeless individual 1, treatment and rehabilitation program 1.
- The Act's own definitions inside your ranges, which are yours: "employment and training program", "workforce partnership", "fleeing", "work program", "noncontiguous State", "caseload", "covered individual" (s 2015), "funds saved ..." (s 2029).

### snap3: lines 913-1340, 1796-1910

- Sections: s 2016 (issuance and use of benefits), s 2016a (EBT benefit fraud prevention), s 2017 (value of allotment), s 2022 (disposition of claims), s 2023 (administrative and judicial review), s 2024 (violations and enforcement).
- Core names to expect: `Benefit`, `Form of benefit`, `Claim`, `Party`, `Area`, `Dollars by area`, `Table row`, `Annual table`, `Certification period`, `Kind of decision` (establish a claim for an overissuance).
- **COLA tables you own:** the maximum monthly allotments (the 48 States and DC, Alaska urban and rural 1 and 2, Hawaii, Guam, the Virgin Islands) and the minimum monthly allotment. Both feed s 2017. See difficulty 1 below before you fill the maximum-allotment table.
- Defined terms used (text matches): benefit 195, retail food store 35, program 31, coupon 4, EBT card 5, benefit issuer 2, certification period 3, reservation 2, thrifty food plan 2, access device 1, tribal organization 1.
- The Act's own definitions inside your ranges, which are yours: the s 2016(h) terms ("affiliate", "company", "electronic benefit transfer service", "point-of-sale service", "electronic benefit transfer card", "electronic benefit transfer contract", "interoperability", "interstate transaction", "portability", "settling", and others), "initial month" (s 2017), "uncollected overissuance" (s 2022). Line 1245 (s 2016a) says "allotment", "benefit", "household", "retail food store" and "State agency" have the meaning given in s 2012: ask those as inputs (section 6, group A).

### snap4: lines 1425-1795, 2951-2978, 3265-3325

- Sections: s 2020 (administration), s 2021 (civil penalties and disqualification of retail food stores and wholesale food concerns), s 2032 (automated data processing), s 2036b (retail food store and recipient trafficking), s 2036c (annual State report on verification), s 2036d (pilot projects).
- Core names to expect: `Party` (`the State agency`, `the Secretary`, `a retail food store`, `a wholesale food concern`, `a court`), `Kind of decision`, `Period of ineligibility`, `Certification period`, `Benefit`.
- COLA tables you own: none.
- Defined terms used (text matches): benefit 80, program 58, retail food store 20, coupon 13, certification period 9, reservation 7, tribal organization 6, elderly or disabled 2, EBT card 2, homeless individual 2.
- The Act's own definitions inside your ranges, which are yours: "fee agent", "indication of multiple issuance" (s 2020), "eligible entity", "public agency" (s 2036d).
- Yours to answer for s 2012(f): s 2020(s) (transitional benefits option, line 1604).

### snap5: lines 1911-2391, 2656-2697, 2731-2804

- Sections: s 2025 (administrative cost-sharing and quality control), s 2026a (healthy fluid milk incentives projects), s 2028 (consolidated block grants for Puerto Rico and American Samoa).
- Core names to expect: `Party`, `Claim`, `Benefit`, `Kind of decision`. Puerto Rico and American Samoa are in no `Area` value and in `Kind of place` only as `any other place`: declare what s 2028 needs under your own prefix and record it in `NEEDS-CORE.md`.
- COLA tables you own: none.
- Defined terms used (text matches): benefit 30, program 43, thrifty food plan 2, homeless individual 1, reservation 1.
- The Act's own definitions inside your ranges, which are yours: "work supplementation or support program", "payment error rate", "overpayment error rate", "underpayment error rate", "good cause", "AFDC program", "base period", "medicaid program" (s 2025), "fluid milk" (s 2026a), "governmental entity" (s 2028).

### snap6: lines 2392-2655, 2842-2950, 2979-3264

- Sections: s 2026 (research, demonstration, and evaluations), s 2031 (Minnesota Family Investment Project), s 2033 (repealed: the heading at line 2979 says so), s 2034 (community food projects), s 2035 (simplified program), s 2036 (commodities for the emergency food assistance program), s 2036a (nutrition education and obesity prevention grant program).
- Core names to expect: `Party`, `Benefit`, `Area`, `Annual table`, `Kind of decision`.
- COLA tables you own: none.
- Defined terms used (text matches): benefit 88, program 90, EBT card 2, thrifty food plan 2, retail food store 1, tribal organization 1.
- The Act's own definitions inside your ranges, which are yours: "family", "contract", "caregiver", "State" (s 2031), "community food project", "gleaner", "hunger-free communities goal" (s 2034), "Federal costs" (s 2035), "eligible individual" (s 2036a).

## 6. Seams

A seam is a provision in one place whose answer another provision needs. For every seam the asking side takes the answer as an input; names follow section 4.

### Group A. A part asks a section 2012 answer (answered by `snap-definitions`, which the part does not get)

The evidence column is the line of `usc07-ch51.txt` that makes the reference (run).
Where no keel function answers the exact question, the type is `BOOLEAN` and the name says what is asked; the lead decides at the merge whether to add a function.

| asking section (part) | answering section | input name | type | evidence |
| --- | --- | --- | --- | --- |
| s 2014 (snap1) | s 2012(m)(4) | `s 2012(m)(4) the individual or group may constitute a household` | `MAYBE BOOLEAN` | line 215 names "section 2012(m)(4)" |
| s 2014 (snap1), and every part that says "elderly or disabled" | s 2012(j) | `s 2012(j) the member is an elderly or disabled member` | `MAYBE BOOLEAN` | defined term, snap1 9 times, snap4 2, snap2 1 |
| s 2014, s 2015, s 2029 and others (the term "household") | s 2012(m) | `s 2012(m) the individual or group is a household` | `MAYBE BOOLEAN` | defined term |
| s 2014 (snap1), s 2015 (snap2) (the term "homeless individual") | s 2012(l) | `s 2012(l) the individual is a homeless individual` | `MAYBE BOOLEAN` | defined term, snap1 1, snap2 1, snap4 2, snap5 1 |
| s 2018 (snap1) | s 2012(k)(3) | `s 2012(k)(3) the facility is one referred to in section 2012(k)(3)` | `BOOLEAN` | line 1392; the keel function answers a meal, not a facility |
| s 2018 (snap1) | s 2012(k) | `s 2012(k) the group living arrangement is one referred to in section 2012(k)` | `BOOLEAN` | line 1393 |
| s 2019 (snap1) | s 2012(o)(4) | `s 2012(o)(4) the seller is a private nonprofit cooperative food purchasing venture or an agricultural producer marketing directly to consumers` | `BOOLEAN` | line 1422; the keel holds paragraph (4) as a field of `s 2012(o)`, not a function |
| s 2016 (snap3) | s 2012(k)(5), (7), (8) and (3), (4), (9) | `s 2012(k) the establishment is one described in paragraphs (5), (7) and (8) of section 2012(k)`, and the same for paragraphs (3), (4) and (9) | `BOOLEAN` each | lines 935 and 936 |
| s 2016a (snap3) | s 2012(b), (d), (m), (o), (s) | `s 2012(b) the allotment for the month` (`NUMBER`); `s 2012(d) the assistance is a benefit`, `s 2012(m) the individual or group is a household`, `s 2012(o) the seller is a retail food store`, `s 2012(s) the body is a State agency` (each `MAYBE BOOLEAN`) | as shown | line 1245 |
| s 2017 (snap3) | s 2012(m)(5) | `s 2012(m)(5) the facility is one described in subparagraph (B), (C), (D) or (E) of section 2012(m)(5)` and `... the program is a drug or alcoholic treatment program described in section 2012(m)(5)(E)` | `BOOLEAN` each | lines 1280 and 1289 |
| s 2017 (snap3) | s 2012(u) | `s 2012(u)(2) the household adjustment ratio` (`MAYBE NUMBER`) if you use the ratios, or take the plan cost from the COLA table you fill | | line 1263 ("the cost to such households of the thrifty food plan"; "as determined by the Secretary under section 2012") |
| s 2020 (snap4) | s 2012(s)(1), (s)(2) | `s 2012(s) the body is a State agency` | `MAYBE BOOLEAN` | lines 1430, 1462, 1533; the Act cites (s)(1) and (s)(2) separately, the keel function answers both limbs together |
| s 2020 (snap4) | s 2012(k)(3), (4), (9) | the same inputs as the s 2016 row | `BOOLEAN` | line 1548 |
| s 2025 (snap5), s 2028 (snap5), s 2036 (snap6) | s 2012(u)(3) | `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between the two dates` | `NUMBER` | lines 1941, 2741, 3119, 3130; no keel function computes the percentage, it is a published figure and a conditional input |
| s 2026 (snap6) | s 2012(m)(4), (m)(5) | a reference to two provisions, apparently a list of provisions; take `s 2012(m)(4) ...` and `s 2012(m)(5) ...` as inputs only if a rule of yours tests household status | `MAYBE BOOLEAN` | line 2419 |
| s 2014 and s 2015 (snap1, snap2), where the text says "State", "State agency", "tribal organization", "retail food store", "coupon", "EBT card" | s 2012(r), (s), (v), (o), (g), (i) | `s 2012(r) the place is a State`, `s 2012(s) the body is a State agency`, `s 2012(v) the body is a tribal organization`, `s 2012(o) the seller is a retail food store`, `s 2012(g) the thing is a coupon`, `s 2012(i) the card is an EBT card` | `MAYBE BOOLEAN` | defined terms; counts in section 5 |

### Group B. A section 2012 function waits for a part (fields I could not fill)

The input is already a field in `snap-definitions.l4`.
The answering part writes a function whose name begins with its own section label and lists it under ANSWERS in `SEAMS.md`; the lead wires the field to it at the merge.

| my field (function it feeds) | answering section (part) | type | what the answering part exports |
| --- | --- | --- | --- |
| `the period or the contact falls within a transitional benefit period under section 2020(s)` (`s 2012(f) ...`) | s 2020(s) (snap4), line 1604 | `BOOLEAN` | whether a period or a contact falls in a transitional benefit period |
| `issued under section 2016(h) of this title` (`s 2012(i) the card is an EBT card`) | s 2016(h) (snap3), line 976 | `BOOLEAN` | whether a card was issued under s 2016(h) |
| `the form` = `an electronic benefit transfer under section 2016(h)` (`s 2012(d) ...`) | s 2016(h) (snap3) | a `Form of benefit` | what an EBT under s 2016(h) is |
| `permitted under section 2018(h)` (three fields, clauses (3), (4), (9) of `s 2012(k)`) | s 2018(h) (snap1), line 1379 | `BOOLEAN` | whether a private establishment's meals at concessional prices are permitted |
| `income of the others, excluding the spouse, determined under section 2014(d)` (`s 2012(m)(3)`) | s 2014(d) (snap1), line 223 | `NUMBER` | the monthly income of the others, in dollars |
| `the poverty line described in section 2014(c)(1)` (`s 2012(m)(3)`) | s 2014(c)(1) (snap1), line 218 | `NUMBER` | the poverty line for that household, in dollars; the keel multiplies it by 1.65 |
| `the Secretary determines that the tribal organization is capable of ... section 2013(b) ... section 2020(d)` (`s 2012(s) agency`) | s 2013(b) (snap1), line 166, and s 2020(d) (snap4), line 1461 | `MAYBE BOOLEAN` | the Secretary's determination, as a conditional input |
| the Secretary's determinations in `s 2012(d)`, `s 2012(j)(2)(B)`, `s 2012(k)(6)` | none: the Act hands each to the Secretary | `MAYBE BOOLEAN` | nobody; the caller supplies it with three values: `JUST TRUE` = the Secretary has made it, `JUST FALSE` = it has made none or the opposite, `NOTHING` = the caller cannot say |

### Group C. Part-to-part, from references only (bodies not read)

Each cell counts the literal mentions "section 20NN" in the asking section that name the answering section (run).
It is where to look, not a finding that a rule depends on the other.
Name the input for the answering section (`s 2015(d) <what you ask>`), type it `MAYBE BOOLEAN` unless it is a number or a date, and list it under ASKS in `SEAMS.md`.

| asking section (part) | asks (answering section, part, mentions) |
| --- | --- |
| s 2013 (snap1) | s 2025 (snap5) 1; s 2027 (snap2) 1 |
| s 2014 (snap1) | s 2015 (snap2) 7; s 2025 (snap5) 4; s 2016 (snap3) 1; s 2020 (snap4) 1; s 2022 (snap3) 1 |
| s 2018 (snap1) | s 2020 (snap4) 4; s 2021 (snap4) 2; s 2016 (snap3) 1; s 2023 (snap3) 1 |
| s 2019 (snap1) | s 2016 (snap3) 1 |
| s 2015 (snap2) | s 2014 (snap1) 3; s 2020 (snap4) 3; s 2024 (snap3) 2; s 2025 (snap5) 2 |
| s 2027 (snap2) | s 2014 (snap1) 2; s 2025 (snap5) 2; s 2016 (snap3) 1; s 2020 (snap4) 1; s 2022 (snap3) 1; s 2026 (snap6) 1 |
| s 2029 (snap2) | s 2017 (snap3) 1 |
| s 2016 (snap3) | s 2015 (snap2) 3; s 2014 (snap1) 2; s 2025 (snap5) 2; s 2026 (snap6) 2 |
| s 2016a (snap3) | s 2020 (snap4) 3; s 2027 (snap2) 1 |
| s 2017 (snap3) | s 2020 (snap4) 3; s 2014 (snap1) 1 |
| s 2022 (snap3) | s 2025 (snap5) 5; s 2013 (snap1) 1; s 2015 (snap2) 1 |
| s 2023 (snap3) | s 2025 (snap5) 5; s 2021 (snap4) 3; s 2018 (snap1) 1 |
| s 2024 (snap3) | s 2015 (snap2) 2; s 2018 (snap1) 1 |
| s 2020 (snap4) | s 2015 (snap2) 8; s 2025 (snap5) 3; s 2014 (snap1) 2; s 2022 (snap3) 2; s 2023 (snap3) 2; s 2027 (snap2) 2; s 2026 (snap6) 1; s 2035 (snap6) 1 |
| s 2021 (snap4) | s 2023 (snap3) 4; s 2024 (snap3) 1 |
| s 2032 (snap4) | s 2025 (snap5) 2 |
| s 2036b (snap4) | s 2013 (snap1) 1 |
| s 2025 (snap5) | s 2015 (snap2) 21; s 2020 (snap4) 4; s 2027 (snap2) 3; s 2023 (snap3) 2; s 2017 (snap3) 1; s 2022 (snap3) 1; s 2026 (snap6) 1; s 2029 (snap2) 1 |
| s 2028 (snap5) | s 2027 (snap2) 2 |
| s 2026 (snap6) | s 2015 (snap2) 11; s 2014 (snap1) 5; s 2020 (snap4) 5; s 2027 (snap2) 3; s 2016 (snap3) 2; s 2017 (snap3) 2; s 2025 (snap5) 1; s 2029 (snap2) 1 |
| s 2031 (snap6) | s 2025 (snap5) 4; s 2014 (snap1) 2; s 2020 (snap4) 2; s 2015 (snap2) 1 |
| s 2035 (snap6) | s 2017 (snap3) 2; s 2020 (snap4) 3; s 2014 (snap1) 1; s 2016 (snap3) 1; s 2025 (snap5) 1 |
| s 2036a (snap6) | s 2020 (snap4) 1; s 2025 (snap5) 1; s 2027 (snap2) 1 |

Three consequences for the answering parts.
s 2015 (snap2) is asked by snap1, snap4, snap5 and snap6 (7, 8, 21 and 11 mentions): give each subsection that others cite its own small function, named `s 2015(x) ...`.
s 2020 (snap4) and s 2025 (snap5) are asked by four parts or more: the same advice.
s 2014 (snap1) is asked by snap2, snap3, snap4 and snap6: its income and deduction results should be separate functions, not one large rule.

## 7. Definitions: encoded by the keel, and left to the parts

- Encoded in `snap-definitions.l4`: every paragraph of s 2012, (a) to (v). Nothing in s 2012 is left to a part.
- Not encoded and not mine: s 2012a (lines 136-139, snap1's range) modifies s 2012; see difficulty 3.
- Left to the parts: the Act's own in-section definitions in the parts' ranges, listed per part in section 5.
- Not in s 2012 and defined nowhere in lines 1-135 (run: `grep -ci` of the wording over lines 1-135 returns 0): "wholesale food concern" (first used at line 917, in s 2016), "adult" (used twice in lines 1-135, in s 2012(f); there it is a fact the caller states).

## 8. Difficulties the parts will meet

1. **The maximum-allotment table's "9-17" and "18+" rows are not head-counts.** In `fna-snap-cola-fy2027.txt` the "9-17" row gives a dollar amount per additional person above 8 (the 48 States: $225), and "18+" gives a total ($3,887). `Table row` holds a household size and a bare `NUMBER`, so a row of size 9 could be mistaken for the total for nine people. snap3 should write out the rows it means (1 to 8 as totals; the per-person increment under a name that says so; the cap as a total) and state which is which. The core's comment says the same. The matching rule is s 2012(u)(2) as read in F-4 (NOTES.md): $225 is 22 percent of $1,023 rounded, and $3,887 = $1,841 + 2 x $1,023.
2. **"Wholesale food concern" has no definition in s 2012.** `Party` has a constructor for it; snap1 (s 2018) and snap4 (s 2021) take "is a wholesale food concern" as a fact the caller states. Do not define it.
3. **s 2012a refers to letters that do not match.** It says the provisions of "subsections (f) and (i) of section 2012 ... concerning private, nonprofit drug addiction or alcohol treatment and rehabilitation programs ... shall henceforth also be applicable to publicly operated community health centers", with a footnote pointing at a "References in Text note" that the converter omitted. Today's (f) is the certification period and (i) is the EBT card; the programs are (h). The keel's `s 2012(h)` already accepts "a publicly operated community mental health center". snap1 must not assume which subsection is meant: record it as `NOTHING` (points outside the text) or as a fork, with both readings.
4. **The Secretary's determinations are conditional inputs, never guessed.** Where the Act says "as determined by the Secretary" or "if the Secretary determines", the answer is a `MAYBE BOOLEAN` field with three values: `JUST TRUE` = the Secretary has made the determination, `JUST FALSE` = it has made no such determination or made the opposite one (a failed "if"), `NOTHING` = the caller cannot say. Do not collapse `NOTHING` to `FALSE`; do pass `JUST FALSE` when you know there is no determination.
5. **The core `Area` is finer than the Act and coarser than the USDA tables in one place.** The Act names five places (s 2014(c)(1)); the cost-of-living tables split rural Alaska into "Rural 1" and "Rural 2". A part may coarsen the seven values (the income standards lump the 48 States, Guam and the Virgin Islands; the standard deduction lumps Alaska) but cannot refine them.
6. **Two repealed sections are in your ranges.** s 2030 (snap2) and s 2033 (snap6): the headings say "Repealed". Give each a coverage row `repealed or blank in this text`, and say what the heading shows.
7. **A constructor name can collide silently.** See naming rule 6. I found a clash of this kind in my own draft (two types both with `a retail food store`) only because a test touched every constructor.
8. **Fiscal-year data goes in a table keyed by the year.** snap1 and snap3 fill `Annual table` with `fiscal year` 2027 (1 October 2026 to 30 September 2027) and say so. The figures are the USDA's, not the Act's.
9. **Dates and amendments.** Dates are `Date day month year`. The Act's own dates in s 2012 (1 October 2025 and each 1 October after; not earlier than 1 October 2027) are rules on a date input in `snap-definitions.l4`; amendment history in the source credits is not encoded anywhere.
10. **The text is a converter's rendering.** Editorial and statutory notes are omitted, and Title 7 is not positive law. Say so in your files and claim nothing is verified against the official text.
