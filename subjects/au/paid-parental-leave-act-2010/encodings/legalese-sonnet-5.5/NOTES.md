# Notes: Paid Parental Leave Act 2010 (Commonwealth), Chapter 2 Parts 2-1 to 2-3 Division 4

Status: draft.
This is a point-in-time record of an encoding written by a single Sonnet 5.5 agent working alone from the brief.
No domain expert has read it against the text.
The numbers below were produced by the checks named beside them, run on the writing build and the main build named in the section headed "What check.sh prints".

## Source and target

The text encoded is compilation C2026C00425 (Compilation No. 49, in force from 19 September 2026), as rendered to plain text by a converter script.
It is not the authorised text, some spaces in it are non-breaking, and nothing here is verified against the official compilation.
The picture that carries the formula in section 43(1) is not in the text file; the sidecar `C2026C00425.formulas.md` in the source bundle transcribes it, and the time module cites it in a plain comment beside the one place that uses it.
Scope: Chapter 2 Parts 2-1 and 2-2, and Part 2-3 Divisions 1 to 4 (sections 7 to 44), with the Dictionary entries those provisions use; edition: the compilation above.
Target: `main`.
The writing build is 1.6.98 (main, 7689b0d, 2026-10-19); the build `check.sh` compared with is 1.6.110 (main, e51181d, 2026-11-11).

## Seat

The seat is a parent, or the partner or adoptive parent of one, who has claimed parental leave pay for flexible PPL days for a child.
That person asks whether the Secretary can determine that parental leave pay is payable to them, what the eligibility, work and income tests need, and when another claimant's permission is needed.
Chapter 2 is addressed to the Secretary (who must or may or cannot make a determination), but every outcome lands on the claimant, so the questions are the claimant's: they say what the claimant must show, what the Secretary cannot do to them, and what the claimant must obtain from someone else.
There is no seat for the Secretary.
The seat layer is `ppl-seat.l4` (23 exported questions, each with `@export` and an `@desc` on every input) and `ppl-cases-seat.l4` (one or more cases for every question).
The cases include ones that assert `NOTHING` for the places where the text does not answer and the form can ask the question: the second birthday of a child born on 29 February, the income limits the Act does not state, who may give a permission, paragraphs 14(2)(d) and (e), the day a permission is varied, and a request to revoke that does not meet section 25(1); the hours of a day in two payment periods are tested in the modules only, because the work test form takes paid-work blocks only.
The seat form takes plain inputs and builds the records the modules expect inside each question; it calls the module rules and restates none.
Two limits of the form are recorded in the comments of `ppl-seat.l4`: the work test question describes the work test period as up to five blocks of days with the paid work done on each day of the block, and the income test question takes the two income limits that apply as figures because the indexed limits depend on published Consumer Price Index numbers.

## What is encoded and what is not

Layer 1 is the law, one module for each Part or Division, each with its own tests; the modules are listed here in reading order.

| module | what it holds | tests |
|---|---|---|
| `ppl-provisions.l4` | the provision index: every Chapter, Part, Division, section and sub-unit of the in-scope text, with its heading and line | in the file |
| `ppl-xrefs.l4` | the cross-reference rows: every reference from an in-scope provision to a provision of this Act or to another Act or instrument, tested against the index | in the file |
| `ppl-logic.l4` | three-valued helpers (both, either, opposite of a result) used by the rule modules | `ppl-tests-logic.l4` |
| `ppl-time.l4` | every date, period and amount the text states: flexible PPL days and the second birthday, the limits of days, the waiting period, the work test period and its counting, the income limits and their indexation | `ppl-tests-time.l4` |
| `ppl-nouns.l4` | the records the rules read | used by every test |
| `ppl-definitions.l4` | the Dictionary entries the in-scope text uses, as a table and as functions | `ppl-tests-definitions.l4` |
| `ppl-key-provisions.l4` | Part 2-1 | `ppl-tests-key-provisions.l4` |
| `ppl-determinations.l4` | Part 2-2 | `ppl-tests-determinations.l4` |
| `ppl-eligibility.l4` | Part 2-3 Division 2 | `ppl-tests-eligibility.l4` |
| `ppl-work-test.l4` | Part 2-3 Division 3 | `ppl-tests-work-test.l4` |
| `ppl-income-test.l4` | Part 2-3 Division 4 Subdivision A, with the limits and their indexation in `ppl-time.l4` | `ppl-tests-income-test.l4` |
| `ppl-seat.l4` | layer 2: the claimant's questions | `ppl-cases-seat.l4` |

Not encoded: Part 2-3 Division 5 (the Australian residency test) and Division 6 (caring for a child), Part 2-4 (claims), Chapters 3 to 6, the schedules and the endnotes, and every Dictionary entry the in-scope text does not use.
Where an in-scope rule needs one of those, the fact is an input: whether the Australian residency test is satisfied, whether the person is caring for the child, whether an effective claim has been made.
Facts the Act borrows from other instruments are inputs: the PPL rules (what is paid work or paid leave, the prescribed exceptional circumstances and conditions, the hours taken for a payment period), the Social Security Act (adjusted taxable income through the Family Assistance Act, visa classes, refugee and family member), the Migration Act 1958, the Family Law Act 1975, the Financial Framework (Supplementary Powers) Regulations 1997 and the Consumer Price Index numbers.
Cross-references to those instruments are rows in `ppl-xrefs.l4` whose target is marked as another instrument.

Conventions used throughout, each stated once here:

- A rule answers `JUST TRUE` or `JUST FALSE` where the text says so in its own words and `NOTHING` where it is silent, lists without closing the list, or points outside the sources.
- A bar ("cannot", "must not") answers `JUST FALSE` when it applies and `NOTHING` when it does not, because the text does not then say that the Secretary can.
- A duty with an "if" that is not met answers `NOTHING`, except in sections 13(6) and 14(4), which state the converse in the same section and so answer `JUST FALSE`.
- A requirement ("must be given", "must state") answers `JUST TRUE` when every item is met and `JUST FALSE` when one is not.
- "The Secretary is satisfied that X" is encoded as X on the facts as stated (F2).

## Jural relations

| provision | position | holder | other party | encoded in |
|---|---|---|---|---|
| ss 13(1), 13(2) | duty | the Secretary, to make a determination on a PPL claim and to determine that parental leave pay is payable | the PPL claimant (claim-right) | `ppl-determinations`: `the Secretary must make a determination on the PPL claim under section 13`, `the Secretary must determine that parental leave pay is payable under section 13(2)` |
| s 13(6) | duty | the Secretary, to determine not payable and, in the case stated, conditionally eligible | the PPL claimant (claim-right) | `ppl-determinations`: `the Secretary must determine that parental leave pay is not payable under section 13(6)(a)`, `the Secretary must determine that the claimant is conditionally eligible under section 13(6)(b)` |
| ss 14(1), 14(2), 14(4) | duty | the Secretary, as for a special PPL claim | the special PPL claimant (claim-right) | `ppl-determinations` |
| ss 11B, 11C, 18, 19B, 20, 21 | disability | the Secretary, who has no power to make the determination in the cases stated | the person claiming (immunity from that determination being made) | `ppl-key-provisions`, `ppl-determinations`: the functions named `the Secretary can make a determination under section 13 or 14 for a flexible PPL day, as section 11B bears on it` (and 11C) and `the Secretary can make a payability determination, as section 18 bears on it` (and 19B, 20, 21) |
| s 11A | claim-right | a person for whom a determination is in force, that parental leave pay is payable to them for the day | the Commonwealth, whose duty to pay is outside the in-scope text | `ppl-key-provisions` |
| ss 15(1), 15(2) | power | the birth mother, an adoptive parent, an adoptive parent nominated, or a person in the prescribed exceptional circumstances, to give a permission | the claimant who receives it (liability) | `ppl-determinations`: `a person may give permission to a PPL claimant under subsection 15(1)`, `a person may give permission to a special PPL claimant under subsection 15(2)` |
| s 15(4) | power | the person who gave a permission, to vary or revoke it | the claimant who holds it (liability) | `ppl-determinations`: `a person may vary or revoke a permission they have given` |
| ss 15(6)(d), 15(7)(d) | immunity | the person to whom the determination relates, whose determination is unaffected for the days that have already occurred when the permission is varied or revoked | the person who gave the permission (disability) | `ppl-determinations`, `ppl-time` |
| ss 15(6)(e)-(f), 15(7)(e)-(f) | duty | the Secretary, to vary the determination to remove the days and to determine not payable for them | the person to whom the determination relates (claim-right) | `ppl-determinations`, `ppl-time` |
| ss 15(3), 15(5) | requirement on the exercise of a power | the form and content that a permission, and a variation or revocation of it, must have | the giver | `ppl-determinations` |
| s 18(2), 18(3) | power | a PPL claimant, to verify the child's birth by giving the form and the information | the Secretary (liability): the bar in s 18(1) lifts | `ppl-determinations`: `a person verifies a child's birth` |
| ss 22, 27 | liberty | the Secretary, to act on the assumption that the state of affairs known will remain unchanged | the claimant (no-claim) | `ppl-determinations` |
| s 23 | fact on which positions depend | the period for which a payability determination is in force | not a Hohfeldian position | `ppl-determinations`, `ppl-time` |
| ss 24, 29 | duty | the Secretary, to give the claimant a notice | the claimant (claim-right) | `ppl-determinations`: `a notice of a payability determination meets section 24`, `the Secretary has met the duty to give notice of an initial eligibility determination` |
| s 25 | power and duty | the claimant may request revocation; the Secretary must then revoke | the claimant (power), the Secretary (liability and duty) | `ppl-determinations`, `ppl-time` |
| s 26A | power | the Secretary, to make an initial eligibility determination | the claimant (liability) | `ppl-determinations` |
| ss 31AA, 31AB, 31ABA, 31A | fact on which positions depend | eligible or not eligible on a flexible PPL day; the Secretary's disability under s 11B depends on it | not a Hohfeldian position | `ppl-eligibility`, `ppl-time` |
| Division 3, Division 4 | fact on which positions depend | satisfies or does not satisfy the work test or the income test | not a Hohfeldian position | `ppl-work-test`, `ppl-income-test`, `ppl-time` |

## Coverage

Each row is one section, subsection, paragraph (sub-paragraphs fall inside their paragraph's row), note, step, heading or Dictionary entry; every non-blank line of the in-scope text falls in some row.
Text units counted: 407 rows of the in-scope text in Parts 2-1 to 2-3 Division 4 (including headings and notes), and 69 Dictionary entries; the last five rows stand for the out-of-scope Chapters, Parts and Divisions.

| disposition | rows |
|---|---|
| encoded | 362 |
| fork | 45 |
| inert | 69 |
| repealed or blank in this text | 0 |
| out of scope | 5 |
| total | 481 |

Inert rows are headings, guides and notes (the first reason: not operative) and the Minister's power to determine a kind of visa by legislative instrument in s 31A(1A) (the second reason: machinery, a rule-making power); no row is shown repealed or blank.
Treating a guide to a Part and an explanatory note as not operative is an assumed reading: neither states a rule of its own, and each points to or restates operative text that is encoded.
A section's heading line is part of the row headed with the section number and `(heading and opening lines)` when no rule text sits in it.
The "where" column lists the functions whose `@ref` quotes a line of the row.

| unit | lines | disposition | where | note |
|---|---|---|---|---|
| Front matter, contents, Chapter 1 Part 1-1 Introduction | 1-95 | out of scope |  | Title, contents and introductory provisions. |
| Chapter 1 Part 1-2 Definitions, apart from the entries listed above | 96-355 | out of scope |  | The guide to the Part and the Dictionary entries the in-scope text does not use; the entries it uses have the rows headed Dictionary. |
| Dictionary: adjusted taxable income | 107 | encoded | ppl-definitions: the Dictionary entry for adjusted taxable income |  |
| Dictionary: Australian residency test | 131 | encoded | ppl-definitions: the Dictionary entry for Australian residency test |  |
| Dictionary: Australian resident | 132 | encoded | ppl-definitions: the Dictionary entry for Australian resident |  |
| Dictionary: birth verification form | 141 | encoded | ppl-definitions: the Dictionary entry for birth verification form |  |
| Dictionary: born prematurely | 142 | encoded | ppl-definitions: a child is born prematurely; ppl-definitions: the Dictionary entry for born prematurely; ppl-time: the period of gestation is less than 37 weeks |  |
| Dictionary: business | 143 | encoded | ppl-definitions: an occupation is a business; ppl-definitions: the Dictionary entry for business |  |
| Dictionary: caring | 144 | encoded | ppl-definitions: the Dictionary entry for caring |  |
| Dictionary: claim | 149 | encoded | ppl-definitions: a request is a claim; ppl-definitions: the Dictionary entry for claim |  |
| Dictionary: claimant | 150 | encoded | ppl-definitions: a person is a claimant; ppl-definitions: the Dictionary entry for claimant |  |
| Dictionary: claimant’s work cessation day | 152 | encoded | ppl-definitions: the Dictionary entry for claimant’s work cessation day |  |
| Dictionary: conditional eligibility determination | 159 | encoded | ppl-definitions: a determination is a conditional eligibility determination; ppl-definitions: the Dictionary entry for conditional eligibility determination |  |
| Dictionary: controls an entity | 162 | encoded | ppl-definitions: the Dictionary entry for controls an entity |  |
| Dictionary: COVID-19 affected claimant | 164-173 | encoded | ppl-definitions: a person is a COVID-19 affected claimant; ppl-definitions: the Dictionary entry for COVID-19 affected claimant; ppl-time: a day is between 22 March 2020 and 31 March 2021 |  |
| Dictionary: COVID-19 Australian Government payment | 174 | encoded | ppl-definitions: the Dictionary entry for COVID-19 Australian Government payment |  |
| Dictionary: COVID-19 Australian Government payment period | 175 | encoded | ppl-definitions: the Dictionary entry for COVID-19 Australian Government payment period |  |
| Dictionary: effective claim | 183 | encoded | ppl-definitions: a claim is an effective claim; ppl-definitions: the Dictionary entry for effective claim |  |
| Dictionary: eligible | 184 | encoded | ppl-definitions: the Dictionary entry for eligible |  |
| Dictionary: employee | 185-187 | encoded | ppl-definitions: a person is an employee; ppl-definitions: the Dictionary entry for employee |  |
| Dictionary: employer | 188 | encoded | ppl-definitions: a person is an employer; ppl-definitions: the Dictionary entry for employer |  |
| Dictionary: entity | 199-205 | encoded | ppl-definitions: a party is an entity; ppl-definitions: the Dictionary entry for entity |  |
| Dictionary: exceptional circumstances | 206-208 | encoded | ppl-definitions: a claim is made in exceptional circumstances; ppl-definitions: the Dictionary entry for exceptional circumstances |  |
| Dictionary: Family Assistance Act | 210 | encoded | ppl-definitions: the Dictionary entry for Family Assistance Act |  |
| Dictionary: family PPL income limit | 212 | encoded | ppl-definitions: the Dictionary entry for family PPL income limit |  |
| Dictionary: farm household allowance | 213 | encoded | ppl-definitions: the Dictionary entry for farm household allowance |  |
| Dictionary: flexible PPL day | 219 | encoded | ppl-definitions: the Dictionary entry for flexible PPL day |  |
| Dictionary: has not previously satisfied the work and income tests | 227-229 | encoded | ppl-definitions: a person has not previously satisfied the work and income tests in relation to a child; ppl-definitions: the Dictionary entry for has not previously satisfied the work and income tests |  |
| Dictionary: holder | 230 | encoded | ppl-definitions: the Dictionary entry for holder |  |
| Dictionary: income test | 234 | encoded | ppl-definitions: the Dictionary entry for income test |  |
| Dictionary: income year | 235 | encoded | ppl-definitions: the Dictionary entry for income year |  |
| Dictionary: indexation day | 236 | encoded | ppl-definitions: the Dictionary entry for indexation day |  |
| Dictionary: indexation factor | 237 | encoded | ppl-definitions: the Dictionary entry for indexation factor |  |
| Dictionary: indexed amount | 238 | encoded | ppl-definitions: the Dictionary entry for indexed amount |  |
| Dictionary: individual PPL income limit | 239 | encoded | ppl-definitions: the Dictionary entry for individual PPL income limit |  |
| Dictionary: initial eligibility determination | 240 | encoded | ppl-definitions: the Dictionary entry for initial eligibility determination |  |
| Dictionary: instalment | 247 | encoded | ppl-definitions: a payment is an instalment; ppl-definitions: the Dictionary entry for instalment |  |
| Dictionary: instalment period | 248 | encoded | ppl-definitions: the Dictionary entry for instalment period |  |
| Dictionary: jobkeeper payment | 250 | encoded | ppl-definitions: the Dictionary entry for jobkeeper payment |  |
| Dictionary: jobkeeper payment period | 251 | encoded | ppl-definitions: the Dictionary entry for jobkeeper payment period |  |
| Dictionary: paid work | 267 | encoded | ppl-definitions: the Dictionary entry for paid work |  |
| Dictionary: parent | 268-271 | fork | ppl-definitions: the Dictionary entry for parent; ppl-definitions: the person is a parent of the child under the Dictionary; ppl-definitions: the person is a parent of the child, taking the ordinary sense where the Dictionary gives none | F15: where the Dictionary gives no meaning, the ordinary sense is asked as a fact |
| Dictionary: parental leave pay | 272 | encoded | ppl-definitions: a payment is parental leave pay; ppl-definitions: the Dictionary entry for parental leave pay |  |
| Dictionary: partner | 273 | encoded | ppl-definitions: the Dictionary entry for partner |  |
| Dictionary: payability determination | 274 | encoded | ppl-definitions: a determination is a payability determination; ppl-definitions: the Dictionary entry for payability determination |  |
| Dictionary: permanent visa | 282 | encoded | ppl-definitions: the Dictionary entry for permanent visa |  |
| Dictionary: permissible break | 283 | encoded | ppl-definitions: the Dictionary entry for permissible break |  |
| Dictionary: PPL | 284 | encoded | ppl-definitions: the Dictionary entry for PPL |  |
| Dictionary: PPL claim | 291 | encoded | ppl-definitions: the Dictionary entry for PPL claim |  |
| Dictionary: PPL claimant | 292 | encoded | ppl-definitions: a person is a PPL claimant; ppl-definitions: the Dictionary entry for PPL claimant |  |
| Dictionary: PPL rules | 295 | encoded | ppl-definitions: the Dictionary entry for PPL rules; ppl-definitions: the rules are the PPL rules |  |
| Dictionary: provisional indexed amount | 305 | encoded | ppl-definitions: the Dictionary entry for provisional indexed amount |  |
| Dictionary: qualifying period | 306 | encoded | ppl-definitions: the Dictionary entry for qualifying period |  |
| Dictionary: qualifying work | 307 | encoded | ppl-definitions: the Dictionary entry for qualifying work |  |
| Dictionary: reference income year | 308 | encoded | ppl-definitions: the Dictionary entry for reference income year |  |
| Dictionary: relevant family PPL income limit | 310 | encoded | ppl-definitions: the Dictionary entry for relevant family PPL income limit |  |
| Dictionary: relevant individual PPL income limit | 311 | encoded | ppl-definitions: the Dictionary entry for relevant individual PPL income limit |  |
| Dictionary: Secretary | 315 | encoded | ppl-definitions: a person is the Secretary; ppl-definitions: the Dictionary entry for Secretary |  |
| Dictionary: Social Security Act | 318 | encoded | ppl-definitions: the Dictionary entry for Social Security Act |  |
| Dictionary: social security benefit | 319 | encoded | ppl-definitions: the Dictionary entry for social security benefit |  |
| Dictionary: social security pension | 321 | encoded | ppl-definitions: the Dictionary entry for social security pension |  |
| Dictionary: special category visa | 322 | encoded | ppl-definitions: the Dictionary entry for special category visa |  |
| Dictionary: special PPL claim | 323 | encoded | ppl-definitions: the Dictionary entry for special PPL claim |  |
| Dictionary: special PPL claimant | 324 | encoded | ppl-definitions: a person is a special PPL claimant; ppl-definitions: the Dictionary entry for special PPL claimant |  |
| Dictionary: stillborn | 325-328 | encoded | ppl-definitions: a child is stillborn; ppl-definitions: the Dictionary entry for stillborn; ppl-time: the child weighed at least 400 grams or the gestation was at least 20 weeks |  |
| Dictionary: this Act | 340 | encoded | ppl-definitions: an instrument is part of this Act; ppl-definitions: the Dictionary entry for this Act |  |
| Dictionary: verifies a child’s birth | 346 | encoded | ppl-definitions: the Dictionary entry for verifies a child’s birth |  |
| Dictionary: vocational placement | 348-351 | encoded | ppl-definitions: a placement is a vocational placement; ppl-definitions: the Dictionary entry for vocational placement |  |
| Dictionary: week day | 352 | encoded | ppl-definitions: the Dictionary entry for week day; ppl-time: a day is a week day |  |
| Dictionary: work test | 354 | encoded | ppl-definitions: the Dictionary entry for work test |  |
| Dictionary: work test period | 355 | encoded | ppl-definitions: the Dictionary entry for work test period |  |
| Part 2-1 heading | 357 | inert |  | not operative: heading |
| Division 1 heading | 358 | inert |  | not operative: heading |
| s 7 (heading and opening lines) | 359-365 | inert |  | not operative: a guide to the Part, stating no rule of its own |
| Division 3 heading | 366 | inert |  | not operative: heading |
| s 11A (heading and opening lines) | 367-368 | encoded | ppl-key-provisions: parental leave pay is payable to a person for a flexible PPL day |  |
| s 11A Note | 369 | inert |  | not operative: an explanatory note |
| s 11B (heading and opening lines) | 370-371 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-key-provisions: the Secretary can make a determination under section 13 or 14 for a flexible PPL day, as section 11B bears on it |  |
| s 11B Note | 372 | inert |  | not operative: an explanatory note |
| s 11C (heading and opening lines) | 373-374 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-key-provisions: the Secretary can make a determination under section 13 or 14 for a flexible PPL day, as section 11C bears on it |  |
| s 11C(a) | 375 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-key-provisions: the Secretary can make a determination under section 13 or 14 for a flexible PPL day, as section 11C bears on it |  |
| s 11C(b) | 376 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-key-provisions: the Secretary can make a determination under section 13 or 14 for a flexible PPL day, as section 11C bears on it |  |
| s 11C Note | 377 | inert |  | not operative: an explanatory note |
| s 11D (heading and opening lines) | 378-379 | encoded | ppl-time: a day is a flexible PPL day for a child born on |  |
| s 11D(a) | 380 | encoded | ppl-time: a day is a flexible PPL day for a child born on |  |
| s 11D(b) | 381 | fork | ppl-time: a day is a flexible PPL day for a child born on; ppl-time: a day is no later than the last flexible PPL day; ppl-time: the last flexible PPL day for a child born on; ppl-time: the second birthday of a child born on | F1: the second birthday of a child born on 29 February is not stated; the answer is NOTHING |
| Part 2-2 heading | 382 | inert |  | not operative: heading |
| Division 1 heading | 383 | inert |  | not operative: heading |
| s 12 (heading and opening lines) | 384-389 | inert |  | not operative: a guide to the Part, stating no rule of its own |
| Division 2 heading | 390 | inert |  | not operative: heading |
| s 13 (heading and opening lines) | 391-392 | inert |  | not operative: the section heading and sub-headings |
| s 13(1) | 393 | fork | ppl-determinations: the Secretary must make a determination on the PPL claim under section 13 | F20: a duty stated with an 'if' that is not met is taken as not answered; the other reading is that the text then says there is no duty |
| s 13(1)(a) | 394 | encoded | ppl-determinations: the Secretary must make a determination on the PPL claim under section 13 |  |
| s 13(1)(b) | 395-397 | encoded | ppl-determinations: the Secretary must make a determination on the PPL claim under section 13 |  |
| s 13(2) | 398 | fork | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) | F2: "the Secretary is satisfied" is read as the matters holding on the facts as stated |
| s 13(2)(a) | 399 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) |  |
| s 13(2)(b) | 400-403 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) |  |
| s 13(2)(c) | 404-407 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) |  |
| s 13(2)(d) | 408-411 | encoded | ppl-determinations: a permission is needed before the Secretary can determine a PPL claim; ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) |  |
| s 13(2)(e) | 412-415 | encoded | ppl-determinations: a permission is needed before the Secretary can determine a PPL claim; ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 13(2) |  |
| s 13 Note | 416 | inert |  | not operative: an explanatory note |
| s 13(3) | 417 | fork | ppl-determinations: a person is covered by subsection 13(3) | F3: the list is not closed with 'only'; a person not on it is taken as not covered where an antecedent asks |
| s 13(3)(a) | 418-420 | encoded | ppl-determinations: a person is covered by subsection 13(3) |  |
| s 13(3)(b) | 421 | encoded | ppl-determinations: a person is covered by subsection 13(3) |  |
| s 13(3)(c) | 422 | encoded | ppl-determinations: a person is covered by subsection 13(3) |  |
| s 13(4) | 423 | fork | ppl-determinations: a person is covered by subsection 13(4) | F3: as for 13(3) |
| s 13(4)(a) | 424 | encoded | ppl-determinations: a person is covered by subsection 13(4) |  |
| s 13(4)(b) | 425 | encoded | ppl-determinations: a person is covered by subsection 13(4) |  |
| s 13(5) | 426-427 | encoded | ppl-determinations: the claimed days that a determination under section 13(2) must specify as payable |  |
| s 13(6) | 428 | encoded | ppl-determinations: the Secretary must determine that parental leave pay is not payable under section 13(6)(a) |  |
| s 13(6)(a) | 429 | encoded | ppl-determinations: the Secretary must determine that parental leave pay is not payable under section 13(6)(a) |  |
| s 13(6)(b) | 430-433 | encoded | ppl-determinations: the Secretary must determine that the claimant is conditionally eligible under section 13(6)(b) |  |
| s 13(7) | 434 | encoded | ppl-determinations: the claimed days that a determination under section 13(6) must specify as not payable |  |
| s 14 (heading and opening lines) | 435-436 | inert |  | not operative: the section heading and sub-headings |
| s 14(1) | 437 | fork | ppl-determinations: the Secretary must make a determination on the special PPL claim under section 14 | F20: a duty stated with an 'if' that is not met is taken as not answered; the other reading is that the text then says there is no duty |
| s 14(1)(a) | 438 | encoded | ppl-determinations: the Secretary must make a determination on the special PPL claim under section 14 |  |
| s 14(1)(b) | 439-441 | encoded | ppl-determinations: the Secretary must make a determination on the special PPL claim under section 14 |  |
| s 14(2) | 442 | fork | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) | F2: "the Secretary is satisfied" is read as the matters holding on the facts as stated |
| s 14(2)(a) | 443 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) |  |
| s 14(2)(b) | 444 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) |  |
| s 14(2)(c) | 445 | encoded | ppl-determinations: a permission is needed before the Secretary can determine a special PPL claim; ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) |  |
| s 14(2)(d) | 446 | fork | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) | F4: 'the permission' is named without the condition that (c) carries; with no permission the answer is NOTHING |
| s 14(2)(e) | 447 | fork | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary must determine that parental leave pay is payable under section 14(2) | F4: as for (d) |
| s 14 Note | 448 | inert |  | not operative: an explanatory note |
| s 14(3) | 449-450 | encoded | ppl-determinations: the claimed days that a determination under section 14(2) must specify as payable |  |
| s 14(4) | 451 | encoded | ppl-determinations: the Secretary must determine that parental leave pay is not payable under section 14(4)(a) |  |
| s 14(4)(a) | 452 | encoded | ppl-determinations: the Secretary must determine that parental leave pay is not payable under section 14(4)(a) |  |
| s 14(4)(b) | 453-457 | encoded | ppl-determinations: the Secretary must determine that the special PPL claimant is conditionally eligible under section 14(4)(b) |  |
| s 14(5) | 458 | encoded | ppl-determinations: the claimed days that a determination under section 14(4) must specify as not payable |  |
| s 15 (heading and opening lines) | 459-460 | inert |  | not operative: the section heading and sub-headings |
| s 15(1) | 461 | encoded | ppl-determinations: a person may give permission to a PPL claimant under subsection 15(1) |  |
| s 15(1)(a) | 462 | encoded | ppl-determinations: a person may give permission to a PPL claimant under subsection 15(1) |  |
| s 15(1)(b) | 463-466 | encoded | ppl-determinations: a person may give permission to a PPL claimant under subsection 15(1) |  |
| s 15(1)(c) | 467 | encoded | ppl-determinations: a person may give permission to a PPL claimant under subsection 15(1) |  |
| s 15(2) | 468 | encoded | ppl-determinations: a person may give permission to a special PPL claimant under subsection 15(2) |  |
| s 15(2)(a) | 469 | encoded | ppl-determinations: a person may give permission to a special PPL claimant under subsection 15(2) |  |
| s 15(2)(b) | 470 | encoded | ppl-determinations: a person may give permission to a special PPL claimant under subsection 15(2) |  |
| s 15(3) | 471 | encoded | ppl-determinations: a permission meets the requirements of subsection 15(3) |  |
| s 15(3)(a) | 472 | encoded | ppl-determinations: a permission meets the requirements of subsection 15(3) |  |
| s 15(3)(b) | 473 | encoded | ppl-determinations: a permission meets the requirements of subsection 15(3) |  |
| s 15(3)(c) | 474 | encoded | ppl-determinations: a permission meets the requirements of subsection 15(3) |  |
| s 15 Note 1 | 475 | inert |  | not operative: an explanatory note |
| s 15 Note 2 | 476-477 | inert |  | not operative: an explanatory note |
| s 15(4) | 478 | encoded | ppl-determinations: a person may vary or revoke a permission they have given |  |
| s 15(4)(a) | 479 | encoded | ppl-determinations: a person may vary or revoke a permission they have given |  |
| s 15(4)(b) | 480 | encoded | ppl-determinations: a person may vary or revoke a permission they have given |  |
| s 15(5) | 481 | encoded | ppl-determinations: a variation or revocation of a permission meets the requirement of subsection 15(5) |  |
| s 15(6) | 482 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied |  |
| s 15(6)(a) | 483 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied |  |
| s 15(6)(b) | 484 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied |  |
| s 15(6)(c) | 485-486 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied |  |
| s 15(6)(d) | 487 | fork | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied; ppl-time: a day has already occurred when the permission is varied or revoked | F5: the day on which the permission is varied or revoked is in neither class; the answer is NOTHING |
| s 15(6)(e) | 488-490 | fork | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied; ppl-time: a day has already occurred when the permission is varied or revoked; ppl-time: the number of days removed from the determination on a variation | F5: the day on which the permission is varied or revoked is in neither class; the answer is NOTHING |
| s 15(6)(f) | 491 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is varied |  |
| s 15 Note | 492 | inert |  | not operative: an explanatory note |
| s 15(7) | 493 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked |  |
| s 15(7)(a) | 494 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked |  |
| s 15(7)(b) | 495 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked |  |
| s 15(7)(c) | 496-497 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked |  |
| s 15(7)(d) | 498 | fork | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked; ppl-time: a day has already occurred when the permission is varied or revoked | F5: the day on which the permission is varied or revoked is in neither class; the answer is NOTHING |
| s 15(7)(e) | 499 | fork | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked; ppl-time: a day has already occurred when the permission is varied or revoked | F5: the day on which the permission is varied or revoked is in neither class; the answer is NOTHING |
| s 15(7)(f) | 500 | encoded | ppl-determinations: the number of days the Secretary must remove from the determination when a permission is revoked |  |
| s 15 Note | 501 | inert |  | not operative: an explanatory note |
| Division 3 heading | 502 | inert |  | not operative: heading |
| s 18 (heading and opening lines) | 503 | inert |  | not operative: the section heading and sub-headings |
| s 18(1) | 504-505 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 18 bears on it |  |
| s 18(2) | 506 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(2)(a) | 507 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(2)(b) | 508 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3) | 509 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3)(a) | 510 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3)(b) | 511 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3)(c) | 512-513 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3)(d) | 514 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(3)(e) | 515 | encoded | ppl-determinations: a person verifies a child's birth |  |
| s 18(4) | 516 | encoded | ppl-determinations: a form is a birth verification form |  |
| s 19B (heading and opening lines) | 517-518 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 19B bears on it; ppl-time: a child is born after 31 March 2021 |  |
| s 20 (heading and opening lines) | 519-520 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 20 bears on it |  |
| s 20(a) | 521 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 20 bears on it |  |
| s 20(b) | 522 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 20 bears on it |  |
| s 21 (heading and opening lines) | 523 | inert |  | not operative: the section heading and sub-headings |
| s 21(1) | 524 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 21 bears on it |  |
| s 21(1)(a) | 525-527 | fork | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 21 bears on it; ppl-time: the total of flexible PPL days for more than one person, for a child born on | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 21(1)(b) | 528 | encoded | ppl-determinations: the Secretary can determine that parental leave pay is payable; ppl-determinations: the Secretary can make a payability determination, as section 21 bears on it |  |
| s 21(2) | 529 | encoded | ppl-determinations: the Secretary can make a payability determination, as section 21 bears on it |  |
| Division 4 heading | 530 | inert |  | not operative: heading |
| s 22 (heading and opening lines) | 531-532 | encoded | ppl-determinations: the Secretary may act on the assumption that the state of affairs known will remain unchanged, for a payability determination |  |
| s 23 (heading and opening lines) | 533-534 | encoded | ppl-determinations: a payability determination is in force on a day; ppl-time: the day a payability determination comes into force |  |
| s 23(a) | 535 | encoded | ppl-determinations: a payability determination is in force on a day |  |
| s 23(b) | 536 | encoded | ppl-determinations: a payability determination is in force on a day |  |
| s 24 (heading and opening lines) | 537-538 | encoded | ppl-determinations: a notice of a payability determination meets section 24 |  |
| s 24(a) | 539 | encoded | ppl-determinations: a notice of a payability determination meets section 24 |  |
| s 24(c) | 540 | encoded | ppl-determinations: a notice of a payability determination meets section 24 |  |
| s 24(d) | 541 | encoded | ppl-determinations: a notice of a payability determination meets section 24 |  |
| s 24(e) | 542 | encoded | ppl-determinations: a notice of a payability determination meets section 24 |  |
| s 25 (heading and opening lines) | 543 | inert |  | not operative: the section heading and sub-headings |
| s 25(1) | 544 | fork | ppl-determinations: the Secretary must revoke the determination on request | F20: a duty stated with an 'if' that is not met is taken as not answered; the other reading is that the text then says there is no duty |
| s 25(1)(a) | 545 | encoded | ppl-determinations: the Secretary must revoke the determination on request |  |
| s 25(1)(b) | 546 | encoded | ppl-determinations: the Secretary must revoke the determination on request |  |
| s 25(1)(c) | 547 | fork | ppl-determinations: the Secretary must revoke the determination on request; ppl-time: a request to revoke is made before the last day of the instalment period | F19: a request on the last day of the instalment period is not made before it |
| s 25(1)(d) | 548-549 | encoded | ppl-determinations: the Secretary must revoke the determination on request |  |
| s 25(2) | 550 | encoded | ppl-time: the day a revocation is taken to come into force |  |
| Division 5 heading | 551 | inert |  | not operative: heading |
| s 26A (heading and opening lines) | 552-553 | fork | ppl-determinations: the Secretary may make an initial eligibility determination | F20: a grant limited by its own conditions is not answered where a condition is not met |
| s 26A(a) | 554 | encoded | ppl-determinations: the Secretary may make an initial eligibility determination |  |
| s 26A(b) | 555 | encoded | ppl-determinations: the Secretary may make an initial eligibility determination |  |
| s 26A(c) | 556 | encoded | ppl-determinations: the Secretary may make an initial eligibility determination |  |
| s 27 (heading and opening lines) | 557-558 | encoded | ppl-determinations: the Secretary may act on the assumption that the state of affairs known will remain unchanged, for an initial eligibility determination |  |
| s 28 (heading and opening lines) | 559-560 | encoded | ppl-time: the day an initial eligibility determination comes into force |  |
| s 29 (heading and opening lines) | 561-562 | encoded | ppl-determinations: the Secretary has met the duty to give notice of an initial eligibility determination |  |
| Part 2-3 heading | 563 | inert |  | not operative: heading |
| Division 1 heading | 564 | inert |  | not operative: heading |
| s 30 (heading and opening lines) | 565-571 | inert |  | not operative: a guide to the Part, stating no rule of its own |
| Division 2 heading | 572 | inert |  | not operative: heading |
| s 31AA (heading and opening lines) | 573 | inert |  | not operative: the section heading and sub-headings |
| s 31AA(1) | 574 | encoded | ppl-eligibility: a person is eligible for parental leave pay on a flexible PPL day for a child |  |
| s 31AA(1)(a) | 575 | encoded | ppl-eligibility: a person is eligible for parental leave pay on a flexible PPL day for a child |  |
| s 31AA(1)(b) | 576-577 | encoded | ppl-eligibility: a person is eligible for parental leave pay on a flexible PPL day for a child |  |
| s 31AA(2) | 578 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule |  |
| s 31AA(2)(a) | 579 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule |  |
| s 31AA(2)(b) | 580 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule |  |
| s 31AA(2)(c) | 581 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule; ppl-time: the hours of paid work on the day are no more than one |  |
| s 31AA(2)(d) | 582 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule |  |
| s 31AA(2)(e) | 583-586 | encoded | ppl-eligibility: a person is eligible under the main eligibility rule |  |
| s 31AA(3) | 587 | encoded | ppl-eligibility: a person is eligible when the child is stillborn or has died |  |
| s 31AA(3)(a) | 588 | encoded | ppl-eligibility: a person is eligible when the child is stillborn or has died |  |
| s 31AA(3)(b) | 589 | encoded | ppl-eligibility: a person is eligible when the child is stillborn or has died |  |
| s 31AA(3)(c) | 590-591 | encoded | ppl-eligibility: a person is eligible when the child is stillborn or has died |  |
| s 31AA(4) | 592 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(4)(a) | 593 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(4)(b) | 594 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(4)(c) | 595-597 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(4)(d) | 598 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(4)(e) | 599-600 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are not a special PPL claimant in exceptional circumstances |  |
| s 31AA(5) | 601 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are a special PPL claimant in exceptional circumstances |  |
| s 31AA(5)(a) | 602 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are a special PPL claimant in exceptional circumstances |  |
| s 31AA(5)(b) | 603-605 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are a special PPL claimant in exceptional circumstances |  |
| s 31AA(5)(c) | 606 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are a special PPL claimant in exceptional circumstances |  |
| s 31AA(5)(d) | 607 | encoded | ppl-eligibility: a person is eligible when they meet prescribed conditions and are a special PPL claimant in exceptional circumstances |  |
| s 31AB (heading and opening lines) | 608-609 | inert |  | not operative: the section heading and sub-headings |
| s 31AB(1) | 610-611 | encoded | ppl-eligibility: a person is not eligible on a flexible PPL day under section 31AB |  |
| s 31AB(2) | 612 | encoded | ppl-eligibility: subsection 31AB(2) applies to the relevant claimant |  |
| s 31AB(2)(a) | 613 | fork | ppl-eligibility: subsection 31AB(2) applies to the relevant claimant; ppl-time: determinations in force cover the number of flexible PPL days that the limit specifies | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 31AB(2)(b) | 614-615 | encoded | ppl-eligibility: subsection 31AB(2) applies to the relevant claimant |  |
| s 31AB(3) | 616 | encoded | ppl-eligibility: subsection 31AB(3) applies to the relevant claimant |  |
| s 31AB(3)(a) | 617 | encoded | ppl-eligibility: subsection 31AB(3) applies to the relevant claimant |  |
| s 31AB(3)(b) | 618 | fork | ppl-eligibility: subsection 31AB(3) applies to the relevant claimant; ppl-time: determinations in force cover the number of flexible PPL days that the limit specifies | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 31AB(3)(c) | 619 | encoded | ppl-eligibility: subsection 31AB(3) applies to the relevant claimant |  |
| s 31AB(3)(d) | 620-621 | encoded | ppl-eligibility: subsection 31AB(3) applies to the relevant claimant |  |
| s 31AB(4) | 622 | encoded | ppl-eligibility: subsection 31AB(4) applies to the relevant claimant |  |
| s 31AB(4)(a) | 623 | fork | ppl-eligibility: subsection 31AB(4) applies to the relevant claimant; ppl-time: determinations in force cover the number of flexible PPL days that the limit specifies | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 31AB(4)(b) | 624 | encoded | ppl-eligibility: subsection 31AB(4) applies to the relevant claimant |  |
| s 31AB(4)(c) | 625-626 | encoded | ppl-eligibility: subsection 31AB(4) applies to the relevant claimant |  |
| s 31AB(5) | 627 | encoded | ppl-eligibility: subsection 31AB(5) applies to the relevant claimant |  |
| s 31AB(5)(a) | 628 | fork | ppl-eligibility: subsection 31AB(5) applies to the relevant claimant; ppl-time: determinations in force cover the number of flexible PPL days that the limit specifies | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 31AB(5)(b) | 629 | encoded | ppl-eligibility: subsection 31AB(5) applies to the relevant claimant |  |
| s 31AB(5)(c) | 630-631 | encoded | ppl-eligibility: subsection 31AB(5) applies to the relevant claimant |  |
| s 31AB(6) | 632 | encoded | ppl-eligibility: subsection 31AB(6) applies to the relevant claimant |  |
| s 31AB(6)(a) | 633 | encoded | ppl-eligibility: subsection 31AB(6) applies to the relevant claimant |  |
| s 31AB(6)(b) | 634 | fork | ppl-eligibility: subsection 31AB(6) applies to the relevant claimant; ppl-time: determinations in force cover the number of flexible PPL days that the limit specifies | F8: 'in relation to the number of flexible PPL days' (and 'on a total of N') is read as at least that number |
| s 31AB(6)(c) | 635 | encoded | ppl-eligibility: subsection 31AB(6) applies to the relevant claimant |  |
| s 31AB(6)(d) | 636-637 | encoded | ppl-eligibility: subsection 31AB(6) applies to the relevant claimant |  |
| s 31AB(7) | 638-639 | encoded | ppl-eligibility: subsection 31AB(7) applies to the relevant claimant |  |
| s 31AB(8) | 640 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant |  |
| s 31ABA (heading and opening lines) | 641-642 | inert |  | not operative: the section heading and sub-headings |
| s 31ABA(1) | 643 | encoded | ppl-time: the total limit of flexible PPL days for a child born on |  |
| s 31ABA(1)(a) | 644 | encoded | ppl-time: the total limit of flexible PPL days for a child born on |  |
| s 31ABA(1)(b) | 645 | fork | ppl-time: the total limit of flexible PPL days for a child born on | F7: 'between 1 July X and 30 June Y' is read as including both days |
| s 31ABA(1)(c) | 646 | fork | ppl-time: the total limit of flexible PPL days for a child born on | F7: 'between 1 July X and 30 June Y' is read as including both days |
| s 31ABA(1)(d) | 647 | encoded | ppl-time: the total limit of flexible PPL days for a child born on |  |
| s 31ABA Note 1 | 648 | inert |  | not operative: an explanatory note |
| s 31ABA Note 2 | 649-650 | inert |  | not operative: an explanatory note |
| s 31ABA(2) | 651 | encoded | ppl-time: the claimant limit of flexible PPL days when partnered, for a child born on |  |
| s 31ABA(2)(a) | 652 | encoded | ppl-time: the claimant limit of flexible PPL days when partnered, for a child born on |  |
| s 31ABA(2)(b) | 653 | fork | ppl-time: the claimant limit of flexible PPL days when partnered, for a child born on | F7: 'between 1 July X and 30 June Y' is read as including both days |
| s 31ABA(2)(c) | 654 | fork | ppl-time: the claimant limit of flexible PPL days when partnered, for a child born on | F7: 'between 1 July X and 30 June Y' is read as including both days |
| s 31ABA(2)(d) | 655 | encoded | ppl-time: the claimant limit of flexible PPL days when partnered, for a child born on |  |
| s 31A (heading and opening lines) | 656-657 | inert |  | not operative: the section heading and sub-headings |
| s 31A(1) | 658 | encoded | ppl-eligibility: a person is subject to a newly arrived resident's waiting period under subsection 31A(1) |  |
| s 31A(1)(a) | 659 | encoded | ppl-eligibility: a person is subject to a newly arrived resident's waiting period under subsection 31A(1) |  |
| s 31A(1)(b) | 660-663 | encoded | ppl-eligibility: a person is subject to a newly arrived resident's waiting period under subsection 31A(1) |  |
| s 31A(1A) | 664 | inert | ppl-eligibility: a person is subject to a newly arrived resident's waiting period under subsection 31A(1) | machinery: the Minister's power to determine by legislative instrument a kind of visa; the kinds determined are asked as an input to s 31A(1) |
| s 31A(1B) | 665-666 | encoded | ppl-eligibility: a person is subject to a newly arrived resident's waiting period under subsection 31A(1) |  |
| s 31A(2) | 667 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(2)(a) | 668 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(2)(b) | 669 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(2)(c) | 670-671 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(2)(d) | 672 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(2)(e) | 673 | fork | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period; ppl-time: a newly arrived resident's waiting period has ended | F6: 104 weeks is taken as 728 days |
| s 31A(3) | 674 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(3)(a) | 675 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(3)(b) | 676-677 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(3)(c) | 678 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(3)(d) | 679 | fork | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period; ppl-time: a newly arrived resident's waiting period has ended | F6: 104 weeks is taken as 728 days |
| s 31A(4) | 680 | fork | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period | F6: 104 weeks is taken as 728 days |
| s 31A(4)(a) | 681 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period |  |
| s 31A(4)(b) | 682-683 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period; ppl-time: the day a newly arrived resident's waiting period starts under subsection (4) |  |
| s 31A(4)(c) | 684 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period; ppl-time: the day a newly arrived resident's waiting period starts under subsection (4) |  |
| s 31A(4)(d) | 685-687 | encoded | ppl-eligibility: the day a newly arrived resident's waiting period starts; ppl-time: a day is in a newly arrived resident's waiting period; ppl-time: a newly arrived resident's waiting period has ended; ppl-time: the day a newly arrived resident's waiting period starts under subsection (4) |  |
| s 31A(6A) | 688 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6A) for a flexible PPL day |  |
| s 31A(6A)(a) | 689 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6A) for a flexible PPL day |  |
| s 31A(6A)(b) | 690-694 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6A) for a flexible PPL day |  |
| s 31A(6A)(c) | 695-696 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6A) for a flexible PPL day |  |
| s 31A(6B) | 697 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6B) to a period |  |
| s 31A(6B)(b) | 698 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6B) to a period; ppl-time: the claim is for a period of at least 10 flexible PPL days |  |
| s 31A(6B)(c) | 699 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6B) to a period |  |
| s 31A(6B)(d) | 700-703 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6B) to a period |  |
| s 31A(6B)(e) | 704-705 | encoded | ppl-eligibility: subsection 31A(1) does not apply under subsection 31A(6B) to a period |  |
| s 31A(7) | 706 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7) to a day |  |
| s 31A(7A) | 707 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7A) to a day |  |
| s 31A(7A)(a) | 708 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7A) to a day |  |
| s 31A(7A)(b) | 709-711 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7A) to a day |  |
| s 31A(7A)(c) | 712 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7A) to a day |  |
| s 31A(7A)(d) | 713 | encoded | ppl-eligibility: subsection 31AB(8) applies to the relevant claimant; ppl-eligibility: subsection 31AB(8) does not apply under subsection 31A(7A) to a day |  |
| s 31A(8) | 714 | encoded | ppl-eligibility: the provision of the Social Security Act that gives the meaning of a term in subsection 31A(7A) |  |
| s 31A(8)(a) | 715 | encoded | ppl-eligibility: the provision of the Social Security Act that gives the meaning of a term in subsection 31A(7A) |  |
| s 31A(8)(b) | 716 | encoded | ppl-eligibility: the provision of the Social Security Act that gives the meaning of a term in subsection 31A(7A) |  |
| s 31A(8)(c) | 717 | encoded | ppl-eligibility: the provision of the Social Security Act that gives the meaning of a term in subsection 31A(7A) |  |
| Division 3 heading | 718 | inert |  | not operative: heading |
| s 32 (heading and opening lines) | 719-721 | encoded | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day |  |
| s 32 Step 1 | 722 | encoded | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day |  |
| s 32 Note | 723 | inert | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day | not operative: an explanatory note |
| s 32 Step 2 | 724 | encoded | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day |  |
| s 32 Note | 725 | inert | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day | not operative: an explanatory note |
| s 32 Step 3 | 726 | encoded | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day |  |
| s 32 Note | 727 | inert | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day | not operative: an explanatory note |
| s 32 Step 4 | 728 | encoded | ppl-time: the number of consecutive days in a qualifying period; ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day; ppl-work-test: the window of 295 consecutive days from an index is a qualifying period with enough hours |  |
| s 32(a) | 729 | inert | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day; ppl-work-test: the window of 295 consecutive days from an index is a qualifying period with enough hours | not operative: part of Note 1 |
| s 32(b) | 730 | inert | ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day; ppl-work-test: the window of 295 consecutive days from an index is a qualifying period with enough hours | not operative: part of Note 1 |
| s 32 Step 5 | 731 | fork | ppl-time: the hours of qualifying work needed in a qualifying period; ppl-work-test: a person satisfies the work test by the method statement in section 32; ppl-work-test: a person satisfies the work test on a day; ppl-work-test: the window of 295 consecutive days from an index is a qualifying period with enough hours | F11: failing step 5 is taken as not satisfying the work test; a qualifying period is any run of exactly 295 days in the work test period |
| s 32 Note 1 | 732 | inert |  | not operative: an explanatory note |
| s 32(a) | 733 | inert |  | not operative: part of Note 1 |
| s 32(b) | 734-735 | inert |  | not operative: part of Note 1 |
| s 32 Note 1A | 736 | inert |  | not operative: an explanatory note |
| s 32 Note 3 | 737 | inert |  | not operative: an explanatory note |
| s 32 Note 4 | 738 | inert |  | not operative: an explanatory note |
| s 32 Note 5 | 739 | inert |  | not operative: an explanatory note |
| s 33 (heading and opening lines) | 740-741 | inert |  | not operative: the section heading and sub-headings |
| s 33(1A) | 742 | encoded | ppl-work-test: section 33 applies to a claimant |  |
| s 33(1B) | 743 | encoded | ppl-work-test: section 33 applies to the first person as if they were the claimant |  |
| s 33 Note | 744-745 | inert |  | not operative: an explanatory note |
| s 33(1) | 746 | encoded | ppl-time: the day the work test period is counted back from; ppl-time: the first day of the work test period; ppl-time: the last day of the work test period; ppl-time: the number of days in the work test period |  |
| s 33(1)(a) | 747-750 | encoded | ppl-time: the day the work test period is counted back from |  |
| s 33(1)(b) | 751-754 | encoded | ppl-time: the day the work test period is counted back from |  |
| s 33(1)(c) | 755 | encoded | ppl-time: the day the work test period is counted back from |  |
| s 33(2) | 756 | encoded | ppl-time: the day the work test period is counted back from; ppl-time: the first day of the work test period; ppl-time: the last day of the work test period; ppl-time: the number of days in the work test period |  |
| s 33(2)(a) | 757-760 | encoded | ppl-time: the day the work test period is counted back from |  |
| s 33(2)(b) | 761 | encoded | ppl-time: the day the work test period is counted back from |  |
| s 33(2A) | 762 | encoded | ppl-work-test: subsection 33(2A) applies in relation to a claimant |  |
| s 33(2A)(a) | 763 | encoded | ppl-work-test: subsection 33(2A) applies in relation to a claimant |  |
| s 33(2A)(b) | 764 | encoded | ppl-work-test: subsection 33(2A) applies in relation to a claimant |  |
| s 33(2A)(c) | 765 | encoded | ppl-work-test: subsection 33(2A) applies in relation to a claimant |  |
| s 33(2A)(d) | 766 | encoded | ppl-work-test: subsection 33(2A) applies in relation to a claimant |  |
| s 33A (heading and opening lines) | 767-768 | encoded | ppl-time: the number of days in the work test period |  |
| s 33A(a) | 769 | encoded | ppl-time: the number of days in the work test period |  |
| s 33A(b) | 770 | encoded | ppl-time: the number of days in the work test period |  |
| s 34 (heading and opening lines) | 771 | inert |  | not operative: the section heading and sub-headings |
| s 34(1) | 772 | encoded | ppl-work-test: a person performs qualifying work on a day |  |
| s 34(1)(a) | 773 | fork | ppl-time: at least one hour; ppl-work-test: a person performs qualifying work on a day | F9: the hours counted on an ordinary day are those of paid work plus those of paid leave, each only if at least one hour |
| s 34(1)(b) | 774 | fork | ppl-time: at least one hour; ppl-work-test: a person performs qualifying work on a day | F9: as for (a) |
| s 34(1)(ca) | 775 | encoded | ppl-work-test: a person performs qualifying work on a day |  |
| s 34(1)(e) | 776 | encoded | ppl-work-test: a person performs qualifying work on a day |  |
| s 34(1)(f) | 777 | encoded | ppl-work-test: a person performs qualifying work on a day |  |
| s 34(2) | 778 | encoded | ppl-work-test: a period of leave is paid leave |  |
| s 34(3) | 779 | encoded | ppl-work-test: a period is a jobkeeper payment period for a person |  |
| s 34(3)(a) | 780 | encoded | ppl-work-test: a period is a jobkeeper payment period for a person |  |
| s 34(3)(b) | 781 | encoded | ppl-work-test: a period is a jobkeeper payment period for a person |  |
| s 34(4) | 782 | encoded | ppl-work-test: a payment is a jobkeeper payment |  |
| s 34(4)(a) | 783 | encoded | ppl-work-test: a payment is a jobkeeper payment |  |
| s 34(4)(b) | 784 | encoded | ppl-work-test: a payment is a jobkeeper payment |  |
| s 34(5) | 785 | encoded | ppl-work-test: a period is a COVID-19 Australian Government payment period for a person |  |
| s 34(6) | 786 | encoded | ppl-work-test: a payment is a COVID-19 Australian Government payment |  |
| s 34(6)(a) | 787 | encoded | ppl-work-test: a payment is a COVID-19 Australian Government payment |  |
| s 34(6)(b) | 788 | encoded | ppl-work-test: a payment is a COVID-19 Australian Government payment |  |
| s 35 (heading and opening lines) | 789-790 | inert |  | not operative: the section heading and sub-headings |
| s 35(1) | 791 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35(2) | 792-793 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35(3) | 794 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35(3)(a) | 795 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35(3)(b) | 796-797 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35(4) | 798-799 | encoded | ppl-work-test: a person controls an entity |  |
| s 35(5) | 800 | encoded | ppl-work-test: a person performs paid work on a day |  |
| s 35A (heading and opening lines) | 801-802 | inert |  | not operative: the section heading and sub-headings |
| s 35A(1) | 803-804 | encoded | ppl-time: the hours taken for a flexible PPL day for a previous child; ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(2) | 805 | fork | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child | F10: with paid work and paid leave both, subsections (2) and (3) give two figures; NOTHING when they differ |
| s 35A(2)(a) | 806 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(2)(b) | 807-808 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(2)(c) | 809 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(2)(d) | 810-811 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(3) | 812 | fork | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child | F10: as for (2) |
| s 35A(3)(a) | 813 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(3)(b) | 814-815 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(3)(c) | 816 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35A(3)(d) | 817 | encoded | ppl-work-test: the hours of qualifying work on a day that is a flexible PPL day for a previous child |  |
| s 35B (heading and opening lines) | 818 | inert |  | not operative: the section heading and sub-headings |
| s 35B(1) | 819 | fork | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period | F10: a day in both kinds of payment period; NOTHING when the two figures differ |
| s 35B(2) | 820 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 35B(2)(a) | 821 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 35B(2)(b) | 822 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 35C (heading and opening lines) | 823 | inert |  | not operative: the section heading and sub-headings |
| s 35C(1) | 824 | fork | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period | F10: as for 35B(1) |
| s 35C(2) | 825 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 35C(2)(a) | 826 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 35C(2)(b) | 827 | encoded | ppl-work-test: the hours of qualifying work on a day in a jobkeeper payment period or a COVID-19 Australian Government payment period |  |
| s 36 (heading and opening lines) | 828 | inert |  | not operative: the section heading and sub-headings |
| s 36(1) | 829-830 | encoded | ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break |  |
| s 36(2) | 831-832 | fork | ppl-time: the days between two qualifying work days are a permissible break; ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break | F12: the next qualifying work day may lie after the work test period (asked as an input); the 84 days are counted as the days with no qualifying work |
| s 36(3) | 833 | encoded | ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break |  |
| s 36(3)(a) | 834 | encoded | ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break |  |
| s 36(3)(b) | 835 | encoded | ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break |  |
| s 36(3)(c) | 836-837 | fork | ppl-time: the later qualifying work day is no more than 84 days after the earlier; ppl-work-test: the day at an index is a qualifying work day or falls within a permissible break | F13: the 84 days are counted from the earlier qualifying work day to the later one |
| s 36A (heading and opening lines) | 838 | inert |  | not operative: the section heading and sub-headings |
| s 36A(1) | 839 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A; ppl-work-test: a person satisfies the work test on a day |  |
| s 36A(1)(a) | 840-842 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A; ppl-work-test: a person satisfies the work test on a day |  |
| s 36A(1)(b) | 843 | fork | ppl-work-test: a person also satisfies the work test on a day under section 36A; ppl-work-test: a person satisfies the work test on a day | F14: 'would have satisfied the work test ... if that circumstance had not existed' is asked as a fact |
| s 36A(2) | 844 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A |  |
| s 36A(2)(a) | 845 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A |  |
| s 36A(2)(b) | 846-848 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A |  |
| s 36A(2)(c) | 849 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36A |  |
| s 36AA (heading and opening lines) | 850-851 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36AA; ppl-work-test: a person satisfies the work test on a day |  |
| s 36AA(a) | 852 | encoded | ppl-work-test: a person also satisfies the work test on a day under section 36AA; ppl-work-test: a person satisfies the work test on a day |  |
| s 36AA(b) | 853 | fork | ppl-work-test: a person also satisfies the work test on a day under section 36AA; ppl-work-test: a person satisfies the work test on a day | F14: as for 36A(1)(b) |
| Division 4 heading | 854 | inert |  | not operative: heading |
| Subdivision A heading | 855 | inert |  | not operative: heading |
| s 37 (heading and opening lines) | 856 | inert |  | not operative: the section heading and sub-headings |
| s 37(1) | 857 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(1)(a) | 858 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(1)(b) | 859-860 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(2) | 861 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(2)(a) | 862 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(2)(b) | 863-864 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(2)(c) | 865 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(2)(d) | 866 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(3) | 867 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(3)(a) | 868 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(3)(b) | 869-870 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(3)(c) | 871 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 37(3)(d) | 872-874 | encoded | ppl-income-test: a person satisfies the income test on a day |  |
| s 38 (heading and opening lines) | 875-876 | encoded | ppl-income-test: a person's adjusted taxable income for an income year |  |
| s 38 Note | 877 | inert |  | not operative: an explanatory note |
| s 39 (heading and opening lines) | 878-879 | encoded | ppl-income-test: the end day of the reference income year for a person; ppl-time: the end day of the reference income year |  |
| s 39(a) | 880 | fork | ppl-income-test: the end day of the reference income year for a person; ppl-time: the end day of the reference income year | F18: an income year ending on the earlier day itself has not ended before it |
| s 39(a)(i) | 881 | encoded | ppl-income-test: the end day of the reference income year for a person; ppl-time: the end day of the reference income year |  |
| s 39(a)(ii) | 882 | encoded | ppl-income-test: the end day of the reference income year for a person; ppl-time: the end day of the reference income year |  |
| s 40 (heading and opening lines) | 883 | inert |  | not operative: the section heading and sub-headings |
| s 40(1) | 884 | encoded | ppl-income-test: the relevant individual PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 40(1)(a) | 885 | encoded | ppl-income-test: the relevant individual PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 40(1)(b) | 886 | encoded | ppl-income-test: the relevant individual PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 40(2) | 887 | encoded | ppl-income-test: the relevant family PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 40(2)(a) | 888 | encoded | ppl-income-test: the relevant family PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 40(2)(b) | 889 | encoded | ppl-income-test: the relevant family PPL income limit; ppl-time: the earlier of the claim day and the birth day |  |
| s 41 (heading and opening lines) | 890 | inert |  | not operative: the section heading and sub-headings |
| s 41(1) | 891 | encoded | ppl-time: the individual PPL income limit that applies on a day |  |
| s 41(1)(a) | 892 | fork | ppl-time: the individual PPL income limit that applies on a day; ppl-time: the individual limit stated for a day | F17: the individual limit is stated from 1 October 2010 only; earlier days: NOTHING |
| s 41(1)(b) | 893 | encoded | ppl-time: the individual PPL income limit that applies on a day; ppl-time: the individual limit after indexation in the year |  |
| s 41(2) | 894 | encoded | ppl-time: the family PPL income limit that applies on a day |  |
| s 41(2)(a) | 895 | fork | ppl-time: the family PPL income limit that applies on a day; ppl-time: the family limit stated for a day | F17: the family limit is stated from 1 July 2023 only; earlier days: NOTHING |
| s 41(2)(b) | 896 | encoded | ppl-time: the family PPL income limit that applies on a day; ppl-time: the family limit after indexation in the year |  |
| Subdivision B heading | 897 | inert |  | not operative: heading |
| s 42 (heading and opening lines) | 898-899 | inert |  | not operative: the section heading and sub-headings |
| s 42(1) | 900 | encoded | ppl-time: the year of the 1 July on or before a day |  |
| s 42(2) | 901-902 | encoded | ppl-time: the family limit after indexation in the year; ppl-time: the individual limit after indexation in the year; ppl-time: the year of the 1 July on or before a day |  |
| s 42(3) | 903-904 | encoded | ppl-time: the indexed amount on an indexation day |  |
| s 42 Step 1 | 905 | encoded | ppl-time: the indexed amount on an indexation day |  |
| s 42 Step 2 | 906 | encoded | ppl-time: the indexed amount on an indexation day |  |
| s 42 Step 3 | 907 | encoded | ppl-time: the indexed amount on an indexation day |  |
| s 42 Step 4 | 908 | encoded | ppl-time: the indexed amount on an indexation day |  |
| s 43 (heading and opening lines) | 909 | inert |  | not operative: the section heading and sub-headings |
| s 43(1) | 910-914 | fork | ppl-time: the index number of the base December quarter; ppl-time: the index number of the reference December quarter; ppl-time: the year of the reference December quarter | F16: the Consumer Price Index numbers are asked as inputs; the previous amount is carried year by year from the stated amount |
| s 43(2) | 915 | encoded | ppl-time: the indexation factor rounded |  |
| s 43(3) | 916-917 | encoded | ppl-time: the indexation factor rounded |  |
| s 43(4) | 918 | encoded | ppl-income-test: an index number is used in working out an amount under section 43 |  |
| s 43(4)(a) | 919 | encoded | ppl-income-test: an index number is used in working out an amount under section 43 |  |
| s 43(4)(b) | 920 | encoded | ppl-income-test: an index number is used in working out an amount under section 43 |  |
| s 44 (heading and opening lines) | 921 | inert |  | not operative: the section heading and sub-headings |
| s 44(1) | 922 | encoded | ppl-time: the indexed amount |  |
| s 44(2) | 923 | encoded | ppl-time: the indexed amount |  |
| s 44(3) | 924 | encoded | ppl-time: the indexed amount |  |
| Chapter 2 Part 2-3 Divisions 5 and 6 | 925-969 | out of scope |  | The Australian residency test and caring for a child; the in-scope text asks both as facts. |
| Chapter 2 Part 2-4 | 970-1089 | out of scope |  | How to claim parental leave pay; the in-scope text asks whether an effective claim has been made as a fact. |
| Chapters 3 to 6, schedules and endnotes | 1090-end | out of scope |  | Payment of instalments, superannuation contributions, compliance, review of decisions, miscellaneous provisions and the history of the Act. |

## Fork register

Each entry gives the provision, the rule that carries the reading taken, the readings seen, the one taken, and the text that licenses each.

| id | provision | rule | readings seen and the one taken | text that licenses each |
|---|---|---|---|---|
| F1 | s 11D(b) | `the second birthday of a child born on`, `the last flexible PPL day for a child born on` (`ppl-time`) | For a child born on 29 February the second birthday is (a) 28 February, (b) 1 March, or (c) not stated. Taken: (c), answer `NOTHING`. | 11D(b) says "the day before the child's second birthday" and the sources state no rule for counting a birthday that does not exist in the second year. |
| F2 | ss 13(2), 13(6), 14(2), 14(4), 15(1), 26A, 36A, 36AA | the functions of those sections (`ppl-determinations`, `ppl-work-test`) | "The Secretary is satisfied that X" can be read as a decision the Secretary has taken or as X holding on the facts. Taken: X on the facts as stated. | The sections state the matters of which the Secretary is to be satisfied, and the claimant asks whether those matters are met. |
| F3 | ss 13(3), 13(4) | `a person is covered by subsection 13(3)`, `a person is covered by subsection 13(4)` (`ppl-determinations`) | A person not on the list is (a) not covered or (b) not answered. Taken: (a), a plain `BOOLEAN`, because paragraphs 13(2)(b), (d) and (e) begin "if the PPL claimant is a person covered by" and need an antecedent. | "The following persons are covered" does not close the list with "only". |
| F4 | s 14(2)(d), (e) | `the Secretary must determine that parental leave pay is payable under section 14(2)` (`ppl-determinations`) | For a special PPL claimant to whom (c) does not apply, paragraphs (d) and (e) can be read as (a) requiring a permission or (b) not applying. Taken: the text does not say; with no permission the answer is `NOTHING`. | Paragraphs (d) and (e) refer to "the permission". |
| F5 | ss 15(6)(d)-(e), 15(7)(d)-(e) | `a day has already occurred when the permission is varied or revoked` (`ppl-time`) | The day on which the permission is varied or revoked is (a) a day that has already occurred, (b) one that has not yet occurred, or (c) neither. Taken: (c), answer `NOTHING`. | The text names only days that "have already occurred" and days that "have not yet occurred" at that time. |
| F6 | ss 31A(2)(e), (3)(d), (4) | `a newly arrived resident's waiting period has ended` (`ppl-time`) | 104 weeks is (a) 728 days or (b) a count of calendar weeks. Taken: (a). | A week is seven days; the text gives no other rule. |
| F7 | ss 31ABA(1)(b)-(c), (2)(b)-(c) | `the total limit of flexible PPL days for a child born on`, `the claimant limit of flexible PPL days when partnered, for a child born on` (`ppl-time`) | "Born between 1 July 2024 and 30 June 2025" includes both days or excludes them. Taken: includes both. | The limbs before and after ("before 1 July 2024", "on or after 1 July 2026") leave no gap only if the end days belong to the middle limbs. |
| F8 | ss 31AB(2)(a), (3)(b), (4)(a), (5)(a), (6)(b), 21(1)(a) | `determinations in force cover the number of flexible PPL days that the limit specifies` (`ppl-time`), `the Secretary can make a payability determination, as section 21 bears on it` (`ppl-determinations`) | "In relation to the number of flexible PPL days specified" and "on a total of 10 flexible PPL days" mean (a) exactly that number or (b) at least that number. Taken: at least. | A count above the limit also exhausts it; the notes to s 31ABA say the limit "has been reached". |
| F9 | ss 34(1)(a), (b) | `the hours of qualifying work a person is taken to have performed on a day` (`ppl-work-test`) | The hours counted on a day that is a qualifying work day only because of paid work or paid leave are (a) the hours of paid work, (b) the hours of paid work plus the hours of paid leave, each counted only if at least one hour. Taken: (b). | Sections 35A to 35C state the hours only for other days; step 5 asks for "hours of qualifying work" without saying how an ordinary day is counted. |
| F10 | ss 35A(2)-(3), 35B(1), 35C(1) | `the hours of qualifying work a person is taken to have performed on a day` (`ppl-work-test`) | Where two subsections each fix the hours for the same day: (a) the larger, (b) the sum, (c) not stated. Taken: (c) when the two figures differ, answer `NOTHING`; the common figure when they agree. | Each subsection says the person "is taken to have performed" its figure; sections 35B(2)(b) and 35C(2)(b) say "despite section 35A", and no provision says how 35B and 35C yield to each other or how 35A(2) and 35A(3) do. |
| F11 | s 32 step 5 | `a person satisfies the work test by the method statement in section 32` (`ppl-work-test`) | A person who fails step 5 (a) does not satisfy the work test or (b) is not answered. A qualifying period is (c) any run of exactly 295 days in the work test period, or (d) the longest such run. Taken: (a) and (c). | Section 32 says it is how "to work out whether a person satisfies the work test", and Note 1 says a person may "also" satisfy it in the cases of s 36A. |
| F12 | s 36(2) | `the day at an index is a qualifying work day or falls within a permissible break` (`ppl-work-test`) | A run of days without qualifying work at the end of the work test period is a permissible break if (a) the next qualifying work day, possibly after the period, is within 84 days of the last one, or (b) never. Taken: (a), the later day asked as an input. | The first qualifying work day is to be "in the work test period"; the next one is not so limited. |
| F13 | ss 36(2), 36(3)(c) | `the days between two qualifying work days are a permissible break`, `the later qualifying work day is no more than 84 days after the earlier` (`ppl-time`) | The two 84-day limits count (a) the days with no qualifying work (36(2)) and (b) the days from the earlier to the later qualifying work day (36(3)(c)). Taken: each as printed. | 36(2) says "at least 1 day but not more than 84 consecutive days on which the person did not perform qualifying work"; 36(3)(c) says "no more than 84 consecutive days after the earlier qualifying work day". |
| F14 | ss 36A(1)(b), 36AA(b) | `a person also satisfies the work test on a day under section 36A` and the same name ending `under section 36AA` (`ppl-work-test`) | "Would have satisfied the work test ... if that circumstance had not existed" is (a) computed by re-running the method statement without the circumstance or (b) a fact stated by the claimant. Taken: (b). | The text states the counterfactual but not how the circumstance would be removed from the days. |
| F15 | Dictionary: parent | `the person is a parent of the child under the Dictionary`, `the person is a parent of the child, taking the ordinary sense where the Dictionary gives none` (`ppl-definitions`) | For a child who is neither adopted, nor born by an artificial conception procedure, nor born by a surrogacy arrangement, "parent" is (a) not defined or (b) the ordinary sense. Taken: the Dictionary answers `NOTHING` and the ordinary sense is asked as a fact. | The entry gives meanings for the three cases only and says for the third that it "includes" a parent under section 60HB. |
| F16 | ss 42(3), 43 | `the indexed amount on an indexation day`, `the individual limit after indexation in the year`, `the family limit after indexation in the year` (`ppl-time`) | The December quarter index numbers are (a) in the Act or (b) published elsewhere. Taken: (b), asked as a list of year and number; the previous amount is carried from the stated amount year by year. | Section 43(1) defines the index number as the All Groups Consumer Price Index number "published by the Australian Statistician". |
| F17 | ss 41(1)(a), 41(2)(a) | `the individual limit stated for a day`, `the family limit stated for a day` (`ppl-time`) | For days before 1 October 2010 (individual) and before 1 July 2023 (family), the limit is (a) not stated or (b) some figure. Taken: (a), answer `NOTHING`. | Section 41 states a limit only for the periods it names. |
| F18 | s 39 | `the end day of the reference income year` (`ppl-time`) | An income year that ends on the earlier day itself (a) has ended before it or (b) has not. Taken: (b). | "Ended before" the earlier day. |
| F19 | s 25(1)(c) | `a request to revoke is made before the last day of the instalment period` (`ppl-time`) | A request made on the last day of the instalment period is (a) made before it or (b) not. Taken: (b). | "Before the last day". |
| F20 | ss 13(1), 14(1), 25(1), 26A | `the Secretary must make a determination on the PPL claim under section 13`, `the Secretary must make a determination on the special PPL claim under section 14`, `the Secretary must revoke the determination on request`, `the Secretary may make an initial eligibility determination` (`ppl-determinations`) | A duty ("must") or a grant ("may") that the text states with an "if" is, where the "if" is not met, (a) not answered, as a norm limited by its own wording whose outside case the text leaves open, or (b) answered `JUST FALSE`, as a condition introduced with "if". Taken: (a), `NOTHING`, for all four; the duties of ss 13(6) and 14(4), which state the converse in the text, answer `JUST FALSE`. | Each of these provisions says what the Secretary "must" or "may" do "if" its conditions hold and says nothing of the case where they do not. |

## What the Act turns out to say

1. A day is a flexible PPL day for a child if it falls from the day the child is born to the day before the child's second birthday; for a child born on 15 March 2024 the first such day is 15 March 2024 and the last is 14 March 2026. Asserted.
2. The text does not say what the second birthday of a child born on 29 February is, so it gives no last flexible PPL day for that child. Asserted.
3. The most flexible PPL days that can be paid for a child, counting everyone who claims, is 100 for a child born before 1 July 2024, 110 for a child born from 1 July 2024 to 30 June 2025, 120 from 1 July 2025 to 30 June 2026, and 130 on or after 1 July 2026. Asserted.
4. A claimant who had a partner at the first effective claim is limited, on the same dates, to 90, 100, 105 and 110 flexible PPL days. Asserted.
5. A person is not eligible on a flexible PPL day when determinations are in force for the limit, when the claimant is deceased, or when the day is in a newly arrived resident's waiting period (unless subsection 31A(7) or (7A) applies). Asserted.
6. The newly arrived resident's waiting period is 104 weeks, taken as 728 days: after 727 days in Australia it has not ended and after 728 it has. Asserted.
7. The main eligibility rule asks for no more than one hour of paid work on the day: one hour qualifies and an hour and a half does not. Asserted.
8. The Secretary cannot make a determination for a flexible PPL day unless the person was or will be eligible on that day (section 11B), and cannot make one unless the person has made an effective PPL claim or special PPL claim for that day (section 11C). Asserted.
9. The Secretary must not make a payability determination that makes a flexible PPL day payable to a second person once the days payable to more than one person total 10 (child born before 1 July 2025) or 20 (child born on or after that day), and the PPL rules may prescribe days that do not count; the prescribed days are an input. Asserted.
10. The Secretary must not make a payability determination for a COVID-19 affected claimant whose child is born after 31 March 2021, and must not make one where parental leave pay is or was payable for another child of the same multiple birth. Asserted.
11. A birth is verified by a completed form and, for a parent other than an adoptive parent of a child who is not stillborn and who is responsible under State or Territory law for having the birth entered in the official record, information that the birth has been entered or that the person has applied. Asserted.
12. A permission is needed for a person covered by subsection 13(3) (a parent who is not the birth mother or an adoptive parent, the partner of the birth mother, or the partner of such a parent) and for a person covered by subsection 13(4) (an adoptive parent once a payability determination is in force for another adoptive parent, or the partner of an adoptive parent), unless the circumstances prescribed by the rules apply to the claimant. Asserted.
13. A permission supports a determination only if it has been given, has not been revoked, and specifies at least as many flexible PPL days as would be payable: 20 days specified supports 20 payable and does not support 21. Asserted.
14. Who may give a permission is listed in section 15(1) and (2); the text does not say whether anyone else may. Asserted.
15. When a permission is varied, the days of the determination that have not yet occurred and that exceed the number now specified are removed: for 20 days with 12 not yet occurred and a permission varied to 15, 5 are removed. Asserted.
16. A payability determination is in force from the day it is made until it is revoked (the revocation taking effect on the day of the request) or set aside. Asserted.
17. A request to revoke made before the last day of the instalment period obliges the Secretary to revoke; a request made on that day or after is not covered by the obligation. Asserted.
18. The work test period is the 392 days (600 for a COVID-19 affected claimant) immediately before a day that section 33 selects: the work cessation day, the expected date of birth, or the day the child is born, and for an initial eligibility determination the work cessation day or the expected date of birth. Asserted.
19. A qualifying period is 295 consecutive days of qualifying work or permissible break within the work test period, and the work test is satisfied if the person performed at least 330 hours of qualifying work in a qualifying period. Asserted.
20. A break of 84 consecutive days with no qualifying work between two qualifying work days is a permissible break and a break of 85 days is not. Asserted.
21. A day that is a flexible PPL day for a previous child, on which parental leave pay was payable, counts for 7.6 hours, or for the greater of 7.6 hours and the hours of paid work (or of paid leave) on the day. Asserted.
22. Where a day is in both a jobkeeper payment period and a COVID-19 Australian Government payment period, the text does not say which of the two figures applies. Asserted.
23. The individual PPL income limit stated in the Act is $150,000 from 1 October 2010 to before 1 July 2021, and the family limit is $350,000 from 1 July 2023 to before 1 July 2024; the Act states no other figure, and the limits that apply later are indexed. Asserted.
24. The income test is met if the person's adjusted taxable income for the reference income year is not more than the individual limit, or, without a partner, not more than the family limit, or, with a partner, if the two incomes together are not more than the family limit. Asserted.
25. The limits that apply are those on the earlier of the day the person made the claim and the day the child was born, and the reference income year is the income year that ended before that earlier day. Asserted.
26. The indexation factor is the reference December quarter index number over the base December quarter index number, worked to 3 decimal places and increased by 0.001 if the fourth decimal place is more than 4, and is increased to 1 if it would be less than 1; the provisional indexed amount is rounded to the nearest dollar, a half dollar rounding up. Asserted.
27. For a special PPL claimant who is not the partner of a person in the prescribed exceptional circumstances and has no permission, the text does not say whether paragraphs 14(2)(d) and (e) are met. Asserted.
28. The Secretary may make an initial eligibility determination if the days are specified in an effective claim, the work and income tests are met (where no other initial eligibility determination is in force) and the Australian residency test is met; the encoding answers `NOTHING` where a condition is not met (F20). Asserted.
29. For a claimant with a partner who, or whose partner, is in the circumstances the PPL rules prescribe as exceptional (section 31AB(6)), the 90-day limit for a child born before 1 July 2024 is reached by determinations under section 13 or 14 for the claimant, where section 31AB(3) counts determinations under section 13 only: 90 days reaches it and 89 does not. Asserted.
30. When the Secretary has decided a claim, the days the determination must specify as payable are the claimed days for which the Secretary is satisfied of the matters, and the days it must specify as not payable are the others. Asserted.

## What the text does not answer

Each of the first seven returns `NOTHING` and has a case that asserts it; the last is a boundary of the sources.

- The second birthday of a child born on 29 February (F1).
- The individual limit before 1 October 2010 and from 1 July 2021, and the family limit before 1 July 2023 and from 1 July 2024, without the index numbers (F16, F17).
- Whether paragraphs 14(2)(d) and (e) are met by a special PPL claimant to whom paragraph (c) does not apply (F4).
- Whether the day a permission is varied or revoked is a day that has already occurred (F5).
- The hours of a day in both a jobkeeper payment period and a COVID-19 Australian Government payment period when the PPL rules give different figures, and of a day with both paid work and paid leave that is a flexible PPL day for a previous child (F10).
- Who may give a permission, outside the lists in section 15(1) and (2).
- Whether a person who satisfies none of the stated conditions of a duty (13(1), 14(1), 25(1)) is owed a determination or a revocation.
- Anything that depends on the PPL rules, the Social Security Act, the Family Assistance Act, the Migration Act 1958, the Family Law Act 1975 or the Consumer Price Index, none of which is among the sources; the encoding takes these as inputs and decides none of them.

## What the stable binary does not accept

The binary governs; this is what 1.6.98 rejected or parsed differently while the encoding was written.

Loud (a parse or type error names the line):

- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (except `LEST BREACH ... BECAUSE`); a case outside the encoding returns `NOTHING` instead.
- `length` is not defined; `count` gives the number of elements.
- `MORE THAN` is not a comparison; `GREATER THAN` is.
- `x NOT EQUALS y` does not parse; write `NOT (x EQUALS y)`.
- A nested `ELSE IF` at one column is rejected for indentation; use `BRANCH`.
- A list item built with `OF` must be parenthesised.
- A `GIVEN` that follows a list-typed parameter on the same line does not parse; put the list parameter last.
- A `WITH` constructs a record from named fields; it does not update one, and it cannot be chained.
- `MODULO` needs integers (`Expected an Integer but got the fractional number`); test integrality with `FLOOR x EQUALS x`.
- A record field access used as a function argument needs its own parentheses.
- A continuation line that begins with `AND`, or a record construction spread over lines in a `WHERE`, needs an indentation deeper than the line it continues.
- An inline `CONSIDER` inside the lambda of `map` does not parse; give the lambda a named helper.

Silent (an answer other than the one intended, and no error):

- `NOT a AND b` and `NOT a OR b` parse as `NOT (a AND b)` and `NOT (a OR b)`; parenthesise every `NOT`.
- `Date 29 2 2023` rolls forward to 1 March 2023; a date that does not exist is not an error.

## What check.sh prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ppl-cases-seat.l4                              0       105       0        0         0 |      0       105       0        0  same
ppl-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ppl-determinations.l4                          0         0       0        0         0 |      0         0       0        0  same
ppl-eligibility.l4                             0         0       0        0         0 |      0         0       0        0  same
ppl-income-test.l4                             0         0       0        0         0 |      0         0       0        0  same
ppl-key-provisions.l4                          0         0       0        0         0 |      0         0       0        0  same
ppl-logic.l4                                   0         0       0        0         0 |      0         0       0        0  same
ppl-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
ppl-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
ppl-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
ppl-tests-definitions.l4                       0       101       0        0         0 |      0       101       0        0  same
ppl-tests-determinations.l4                    0       162       0        0         0 |      0       162       0        0  same
ppl-tests-eligibility.l4                       0       105       0        0         0 |      0       105       0        0  same
ppl-tests-income-test.l4                       0        33       0        0         0 |      0        33       0        0  same
ppl-tests-key-provisions.l4                    0         9       0        0         0 |      0         9       0        0  same
ppl-tests-logic.l4                             0        22       0        0         0 |      0        22       0        0  same
ppl-tests-time.l4                              0       163       0        0         0 |      0       163       0        0  same
ppl-tests-work-test.l4                         0        95       0        0         0 |      0        95       0        0  same
ppl-time.l4                                    0         0       0        0         0 |      0         0       0        0  same
ppl-work-test.l4                               0         0       0        0         0 |      0         0       0        0  same
ppl-xrefs.l4                                   0       278       0        0         0 |      0       278       0        0  same
TOTAL (21 modules)                             0      1073       0        0           |      0      1073       0        0
```

The source-reference checker, `srcrefs.py`, run over every `.l4` file once to check each quoted line and locator against the text and once in strict mode, reports 0 problems both times.
Every module runs with no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`; the case file has as many assertions satisfied as written.

## What would need doing before the encoding is worth relying on

- A domain expert reads every module against the authorised compilation; the text used here is a converter's rendering.
- The PPL rules are read and their prescribed circumstances, conditions, hours and paid-work and paid-leave rules put where this encoding asks facts.
- Divisions 5 and 6 of Part 2-3 and Part 2-4 are encoded, so that the residency, caring and claim facts stop being inputs.
- The Consumer Price Index numbers are put in and the indexed income limits checked against the Department's published figures.
- The forks are ruled: each fork row names the entry.
- The seat form is widened to take paid leave, previous-child days and the payment periods in the work test question.
