# NOTES: part ssc3, Social Security Contributions and Benefits Act 1992 (UK), sections 43 to 62

Part ssc3 encodes lines 1230 to 1911 of `inputs/ukpga-1992-4.txt`: retirement pensions (Categories A and B), the additional pension, the shared additional pension, the child's special allowance, deferment, failure to satisfy contribution conditions, and graduated retirement benefit.
That is sections 43 to 55 (Part II, Chapter I), 55A to 55C, 56 (the child's special allowance), 57 to 59 (blank in this text), and 60 to 62.

**Status, 2026-11-04.**
Everything stated below as running was run on that date and the numbers come from the logs named beside them: `check.sh` (stable 1.6.98 and main 1.6.108, section "What check.sh prints"), `srcrefs.py check --refs` and `--strict`, and `work/dispositions.py --audit`.
Nothing in this file is a plan: where something is not done, it says "not done" in the sentence that mentions it.
The source text is a plain-text rendering made by a converter script; it is not the official text, and nothing here claims to have been verified against the official text.

## What was written

Layer 1 is the law, objectively: eight modules, each importing the read-only keel `ssc-core.l4` and the helper module `ssc3-helpers.l4`.
Every rule carries `@ref` with a `src:` locator and verbatim `-- src:` quote lines copied by script from the text file.

| File | Sections |
| --- | --- |
| `ssc3-helpers.l4` | three-valued helpers (`ssc3 helper all of`, `any of`, `not`, `known`, `sum of`) and tax-year arithmetic; no section |
| `ssc3-a0-s61za-s61zc.l4` | 61ZA, 61ZB, 61ZC (units of additional pension and the bar on two pensions) |
| `ssc3-a-s43-s44.l4` | 43, 44 |
| `ssc3-b-s44a-s44c.l4` | 44A, 44B, 44C |
| `ssc3-c-s45-s46.l4` | 45, 45AA, 45B, 46 (45A is blank in this text) |
| `ssc3-d-s47-s48c.l4` | 47, 48, 48A, 48AA, 48B, 48BB, 48C |
| `ssc3-e-s51-s55.l4` | 51, 51ZA, 51A, 52, 55 (section 54 is regulation-making powers only and is inert in the coverage table) |
| `ssc3-f-s55a-s56.l4` | 55A, 55AA, 55B, 55C, 56 |
| `ssc3-g-s60-s62.l4` | 60, 60A, 61, 61A, 62 |
| `ssc3-tests-a.l4` to `ssc3-tests-g.l4` | tests for the modules above (a covers helpers, a0 and a) |
| `ssc3-seat.l4`, `ssc3-cases-seat.l4` | layer 2, the seat, and its cases |

Sections 49, 50, 53, 57, 58 and 59 show only their titles and a row of dots in this text; they are `repealed or blank` in the coverage table.
Section 45A is likewise blank.

**Method.**
Each section was read in the text, encoded isomorphically (one function per subsection or paragraph that decides something, in the text's order), and tested with expected values written by hand from the section before the code was run.
A failing assertion was treated as a finding and never as a reason to edit the expected value.
One case in which an expectation of mine was wrong is recorded as finding 12 below, with the quoted words that settle it.
Positive control: a deliberately wrong assertion in a scratch copy failed with "assertion failed" and was removed.

## Conventions this part departs from, or adds

- **Helper names.** PLAN 1.2 names shared helpers without a prefix.
  This part prefixes its three-valued helpers `ssc3 helper ...`, so that no other part can define the same name.
  The merged seat imports every part at once, and a name defined in two modules cannot be used at all.
- **Unmodified amount.** Where a provision modifies an amount "in the case of" a class of person and the person is outside the class, the function returns the amount unmodified, not NOTHING.
  The branches are marked `unmodified, not a "no"` in the code and listed as reading (c) in "Marginal readings for a lawyer".
- **Regulations that fix a condition or a quantity.** Where the Act makes the content of a regulation a condition of entitlement or a quantity of a benefit (a "prescribed proportion", "such percentage as equals ...", "the weekly rate prescribed"), the provision is encoded and the content arrives as an input.
  A bare power to make machinery, or to amend another Act, is inert reason 2.
- **Signposts and roadmaps** ("For units of additional pension, see section 14A.", "Section 51ZA contains special rules ...", "Schedule 5 has effect") create no rule and are inert reason 1.
- **Tax years** are named by the calendar year in which they begin on 6 April (`Tax year` OF 2016 is 2016-17).
- **"Over" and "under" an age** (section 173(a)) mean has attained and has not attained; "over pensionable age at a time" is the keel's date of attaining it, at most that time.
- **This brief governs over PLAN.md** where they differ; the places are the helper prefix above, the S16 split and the S17 wording in "Seams (ssc3)".

## Seat (ssc3)

**The seat** is a person who works, is self-employed, or claims a contributory or non-contributory benefit, statutory pay or Child Benefit in Great Britain, asking on facts they can state whether and how much they receive by way of a retirement pension, additional pension, shared additional pension or child's special allowance, and what increases, reduces, defers or ends it.
The layer is two files: `ssc3-seat.l4` (42 questions) and `ssc3-cases-seat.l4` (161 cases).
Every question begins "Under section N," with the Act's own numbering, has `@export` and `@desc`, takes plain inputs (yes/no, numbers, dates), and sits under a `§§` heading in the text's order.
No question restates a rule: each builds the records the layer-1 modules expect (a `Person`, a list of pensions) in its `WHERE` and calls the layer-1 function.

**Questions, in the file's order.**

*Section 43: when I qualify for more than one retirement pension*

- Under section 43, which retirement pension am I entitled to for a week when I qualify for both a Category A and a Category B pension?

*Section 44: Category A retirement pension*

- Under section 44(1), am I entitled to a Category A retirement pension?
- Under section 44(1), on what day do I become entitled to a Category A retirement pension?
- Under section 44(1), is my Category A retirement pension running on a given day?
- Under section 44(2), is my Category A retirement pension payable in respect of a given day?
- Under section 44(4), what is the weekly rate of my basic pension, in pounds?

*Sections 44A to 44C: earnings factors the Act gives me for a year or a week*

- Under section 44A, what earnings factor am I treated as having for a tax year in which my own earnings factor was low?
- Under section 44B, what earnings factor am I treated as having for a tax year from the flat rate introduction year?
- Under section 44C, what earnings factor credit do I get for a week?

*Sections 45 to 45B: additional pension*

- Under section 45(1), what is the weekly rate of my additional pension, in pounds, if I reached pensionable age before 6 April 1999?
- Under section 45(2), what is the weekly rate of my additional pension, in pounds, if I reached pensionable age on or after 6 April 1999?
- Under section 45AA, what are my qualifying earnings for a year in which a tax credit was paid, in pounds?
- Under section 45B, what is the weekly rate of my additional pension, in pounds, after a pension debit?

*Section 47: increase of a Category A pension for a long-term incapacity age addition*

- Under section 47(1), by how much, in pounds a week, is my Category A pension increased because I got an age addition to long-term incapacity benefit?

*Section 48: Category A pension from a former spouse's or civil partner's contributions*

- Under section 48(1), can my former spouse's or civil partner's contributions be treated as my own for a Category A retirement pension?

*Section 48A: Category B pension for a married person or civil partner*

- Under section 48A(1), am I, as a married person, entitled to a Category B retirement pension on my spouse's contributions?
- Under section 48A(3), am I, as a civil partner, entitled to a Category B retirement pension on my civil partner's contributions?

*Section 48AA: Category B pension after a divorce or the dissolution of a civil partnership*

- Under section 48AA(1), am I, after a divorce, entitled to a Category B retirement pension on my former spouse's contributions?

*Section 48B: Category B pension for a widow, widower or surviving civil partner*

- Under section 48B(1), am I, as a widow or widower, entitled to a Category B retirement pension on my late spouse's contributions?
- Under section 48B(1A), am I, as a surviving civil partner, entitled to a Category B retirement pension on my late civil partner's contributions?
- Under section 48B(2), what is the weekly rate of my Category B retirement pension, in pounds?

*Section 48BB: Category B pension for someone who was getting a widowed parent's allowance or bereavement allowance*

- Under section 48BB(4), am I entitled to a Category B retirement pension on the contributions of my late spouse or civil partner after getting bereavement allowance or widowed parent's allowance?

*Sections 51 and 52: Category B pension for a widow or widower, and the increase to a Category A pension*

- Under section 51(1), am I, as a widow or widower, entitled to a Category B retirement pension?
- Under section 51A, by how much is the basic pension in my Category A retirement pension increased because of my spouse's or civil partner's contributions, in pounds?
- Under section 52(2), by how much is the basic pension in my Category A retirement pension increased because I am a surviving spouse, in pounds?

*Section 55: deferment of retirement pension*

- Under section 55(3), is my retirement pension deferred?

*Sections 55A to 55C: shared additional pension*

- Under section 55A(1), am I entitled to a shared additional pension because of an old state scheme pension credit?
- Under section 55A(3), what is the weekly rate of my shared additional pension, in pounds?
- Under section 55AA(1), am I entitled to a shared additional pension because of a new state scheme pension credit?
- Under section 55AA(3), what is the weekly rate of my shared additional pension, in pounds?
- Under section 55B, what is the weekly rate of my shared additional pension, in pounds, after a pension debit?
- Under section 55C(3), is my shared additional pension deferred?

*Section 56: child's special allowance*

- Under section 56(1), is the child's special allowance payable to me for a day?
- Under section 56(1), what is the weekly rate of my child's special allowance, in pounds?

*Sections 60 to 62: contribution failures, units of additional pension, and gender change*

- Under section 60(2), are the contribution conditions taken to be satisfied for my Category B retirement pension, because my spouse or civil partner died of an industrial injury or disease?
- Under section 60A, what proportion of my benefit am I entitled to although the paragraph 5A contribution condition is not satisfied?
- Under section 61ZA, are the contribution conditions for my Category A retirement pension taken to be satisfied because of my units of additional pension?
- Under section 61ZB, are the contribution conditions for my Category B retirement pension taken to be satisfied because of my late spouse's or civil partner's units of additional pension?
- Under section 61ZC(1), may I have both a Category A retirement pension because of units of additional pension and a Category B retirement pension, despite section 43?
- Under section 61ZC(2), may I have both a Category A retirement pension and a Category B retirement pension because of my late spouse's or civil partner's units of additional pension, despite section 43?
- Under section 61A, are the contributions I paid in error treated as properly paid for my additional pension?
- Under section 62, am I treated like a woman whose husband has died, because my late wife changed gender?

**What the seat fixes, stated once** (the same list heads `ssc3-seat.l4`).

- A `Person` is built from whether the person is a woman (the Act says "woman" and "man" and defines "woman" for section 140A only), a date of birth, and the date the person attains pensionable age.
  That date is borrowed from the Pensions Act 1995 through section 122(1) and is a fact the person states.
  A question asks for the date of birth only where a layer-1 rule reads it (the spouse's or deceased's, in ss 48A, 48AA, 48B); elsewhere the field has a fixed placeholder and a comment at the use says which rule reads which field.
  I checked which fields each rule reads by searching the modules for the field names; the one slip found that way (ss 48AA(1), 48B(1) and 48B(1A) read the other person's date of attaining pensionable age) was corrected before the cases were run.
- `marital status` is read by no rule in ss 43 to 62; the seat sets it to the status the question presupposes.
- The contribution conditions of Schedule 3 Part I (paragraphs 5, 5A, 6) are another part's answer.
  The person states one yes/no.
  Where a layer-1 rule has a slot for paragraph 5 and a slot for paragraph 5A, the same answer goes to both, because the rule picks the slot by the date of attaining pensionable age (s 44(1A)).
- Amounts that regulations, orders or the Secretary of State set (the amount for each unit of additional pension, revaluation percentages, the Schedule 4 rates, the Schedule 4A and 4B amounts) are asked in pounds or per cent; the seat never supplies one.
- **What the seat calls.** The seat calls 79 of the 253 top-level `s ...` and `sch ...` names in layer 1 (functions and types), at least one in every section that has a layer-1 name (checked by searching `ssc3-seat.l4` for each `s ...` name of the section and finding none missing).
  In each section the seat calls the function that gives the person's answer and leaves its sub-functions to layer 1, where they are tested.

**Seat readings, flagged and not decided.**

- **s 45(2).** Section 46(4) answers JUST TRUE inside its case and NOTHING outside it ("limited by its own wording").
  The question for s 45(2) passes `s 46(4) ... EQUALS JUST TRUE` as the fact "paragraph (d) is omitted", so outside the bereavement case paragraph (d) stays as enacted.
  The other reading would turn every ordinary additional pension into NOTHING.
  It is reading (b) in "Marginal readings for a lawyer (ssc3)": a limit in the wording (s 46(4) applies "in a case where the deceased ... died under pensionable age") read as leaving the rest of s 45(2) untouched.
- **s 43.** The two fields of a pension in contention that say it was awarded because of s 61ZA or s 61ZB (`s 43 Pension in contention`, `ssc3-a-s43-s44.l4:29-30`) are fixed to no in the s 43 question, with a "Placeholders:" comment at the use.
  The pairings that s 61ZC lifts out of s 43(1) are asked in the two s 61ZC questions and are not reachable through the s 43 question.
- **s 45AA.** Subsection (4) speaks of "any woman" with an unrevoked reduced-rate election; the question asks that election as one yes/no (the description says: no, if you are a man).
  A "no" leaves s 45AA(4) on its NOTHING side (it takes nothing away), so subsection (1) applies and the figure is given; a "yes" gives NOTHING because the text says subsection (1) does not apply and names no other figure.
- **ss 61ZC(1) and (2).** The two questions are put the way the person puts them ("may I have both ... despite section 43?"), so `JUST TRUE` means yes, they may, and `NOTHING` means the subsection does not reach the facts.
  The layer-1 functions are named for the text's own words ("section 43 does not prevent entitlement to both pensions"), and the seat passes their answer through unchanged because the two phrasings say the same thing.
- **s 61A.** The question asks four yes/no facts and passes them to `s 61A(1)` and `s 61A(2)`; a "no" to any of the four gives `JUST FALSE`.
  That includes "no regulations under section 61A(2) so provide", which is the last limb of the same "Regulations may, where (a) ... and (b) ..., provide" list as the two limbs the layer-1 tag quotes, read like a failed "where" (marginal reading (a2)); layer 1 asserts it (`ssc3-tests-g.l4`, the case `(JUST TRUE) TRUE (JUST FALSE)`) and the seat has a case for it.
  The other reading is that a power not exercised is silence, and the answer would be `NOTHING`.
- **s 47(1).** The question calls s 61(1) with the benefit fixed to `Category A retirement pension`, because the increase under s 47(1) is an increase of that pension.
- **s 48B(2).** The basic pension is asked of s 44(4) with the flag "lower rate of short-term incapacity benefit" set to no, because a retirement pension is not that sum.
- **ss 48A(1), 48AA(1), 48B(1), 51(1).** The gender-recognition facts of s 51ZA are asked as two yes/no answers and passed through the s 51ZA function; for a man the function answers no because s 51ZA speaks of a woman.
- **s 56(1).** The question asks all twenty-two facts that the layer-1 chain needs (ss 56(1) to (6)) and calls the chain.
  The two seat cases that first exercised s 56(3) had the bar inverted by me (finding 12); the text says "that amount shall not be payable unless one of the conditions specified in subsection (4) below is satisfied".

**Wiring from layer 1 to the seat** (a seam answered by another section of this part is called, not asked): s 51ZA(1) into s 48A(2); s 51ZA(2) into s 48AA(2); s 51ZA(3) into s 48B(1ZA); s 61(1) into s 47(1); s 46(4) into s 45(2); s 55(3) into s 55C(3); s 60(3) into s 60(2); s 62(4) into s 62(3); s 44A(2)(a) to (d), (3), (4)(a), (4)(b) into s 44A(2) and (1); s 44B(3) to (5) into s 44B(2); s 44C(3) into s 44C(2); s 56(2) to (6) into s 56(1); s 61ZA(1) into s 61ZA(2); s 44(4) into s 48B(2); s 48C(3) into s 48B(2); s 45(2A) into ss 45(1) and 45(2); s 45AA(4) into s 45AA(1); s 61A(1) into s 61A(2).

## Coverage (ssc3)

Every non-blank line of the range (lines 1230 to 1911 of `inputs/ukpga-1992-4.txt`) belongs to exactly one unit, and every unit has exactly one disposition: `encoded`, `inert` with a reason number (1, 2 or 3 as the brief defines them; reason 3 is shown as `repealed or blank in this text`), or `fork`.
There is no `out-of-scope` row and no `deferred` row.
The table is generated by `work/dispositions.py --table` from the encodings themselves (a unit is `encoded` when a top-level name carries its section label, or when an `@ref` locator range covers its lines), so a row cannot claim a function that does not exist.
The `work/` folder is scratch and is not shipped; the table is reproduced here in full.

**Counts per disposition** (units, not table lines):

| Disposition | Units |
| --- | --- |
| encoded | 523 |
| fork (the chosen reading is encoded; see the Fork register) | 24 |
| inert, reason 1 (not operative) | 58 |
| inert, reason 2 (machinery) | 48 |
| repealed or blank in this text (reason 3) | 16 |
| **Total units** | **669** |

**Audit counts.**

- Text units counted: 669, from 682 non-blank lines.
- Independent cross-check, made with a different scan (lines that begin with a section number and tab, a subsection number `(1)`, a paragraph letter `(a)`, or an opening quotation mark): 622 such marker lines, of which 621 begin a unit.
  The one that does not is line 1434, the formula line `“N = ...` that continues s 46(3).
  The other 48 units begin with no marker: 33 closing-words units, 7 cross-headings, 7 blank bodies, and s 44A(A1), whose marker `(A1)` my scan does not match.
  621 + 48 = 669.
  Thirteen non-blank lines are the wrapped second line of a unit, and every one lies inside a unit.
- Rows before and after: the automatic pass (headings, section titles, blank rows, `@ref` line coverage, name match) gave 612 of the 669 units a row.
  57 units had none and were classified by hand: 9 as inert reason 1 (signposts and roadmaps) and 48 as inert reason 2 (powers and machinery).
  The hand pass also moved 24 of the 612 from `encoded` to `fork`.
  After: 669 rows, none unclassified (`work/dispositions.py --audit` prints `unclassified: []`, and `missing: []`, `doubled: []` for the lines).
  The table below merges runs of adjacent units with the same disposition and target into one line, each line naming every unit it covers: 331 lines.

**Inert rows, by reason.**

- Reason 1 (58 units): 7 cross-headings of the Act; 42 section titles; 9 signposts and roadmaps that create no rule: s 47(3B), s 48A(8), s 48AA(9), s 48B(9), s 51(10), s 61ZA(4) and s 61ZB(4) (each a "see section ..." or "Section 51ZA contains special rules" pointer), and s 55(2) and s 55C(2) (roadmaps to Schedules 5 and 5A).
- Reason 2 (48 units): ss 44(7A), 45(8), 45B(7) and (7A) with their paragraphs, 54(1) and 54(2), 55A(6) and (6A) with paragraphs, 55B(7) and (7A) with paragraphs, 60(5), 61A(4) with paragraphs, 61A(6) with paragraphs, 62(1) with paragraphs and 62(2).
  Each is a power to make regulations, or a saving for such powers, with no rule for the person until the regulations exist.
  Where the Act makes the content of such regulations a condition or a quantity of entitlement, the provision that does so is encoded and the content is an input (s 55(3)(b) for the election under s 54, s 60(4) for the rate prescribed under s 60(1), s 45B(4) and s 55A(4) for the cash equivalent).
- Reason 3 (16 units, shown as `repealed or blank in this text`): the sections and subsections the text shows only as a row of dots (ss 44(5), 44B(7)(a), 45A, 46(1), 49, 50, 53, 54(3), 54(4), 57, 58, 59, 60(1)(ab), 60(3)(a), 60(3)(bb) and 60(6)).

| Units | Lines | Disposition | Encoded as, reason, or fork |
| --- | --- | --- | --- |
| heading@1230 | 1230 | inert (reason 1) | cross-heading of the Act, not operative |
| 43 | 1231 | inert (reason 1) | the title of the section, not operative |
| 43(1), 43(2), 43(2)(a), 43(2)(b), 43(2) closing words | 1232-1236 | encoded | ssc3-a-s43-s44.l4: `s 43(1) the pensions the person is entitled to for the week` ; tests: ssc3-tests-a.l4 |
| 43(3), 43(3)(a), 43(3)(aa), 43(3)(b), 43(3) closing words | 1237-1241 | encoded | ssc3-a-s43-s44.l4: `s 43(3) the pension the person is entitled to out of the group`; `s 43(3) the person may give notice` ; tests: ssc3-tests-a.l4 |
| 43(4) | 1242 | fork F2 | ssc3-a-s43-s44.l4: `s 43(4) the notices that specify a pension in the group and have effect for the week`; `s 43(3) the pension the person is entitled to out of the group`; `s 43(3) the person may give notice` ; tests: ssc3-tests-a.l4 ; see Fork register F2 |
| 43(5) | 1243 | encoded | ssc3-a-s43-s44.l4: `s 43(5) the name of the most favourable pension`; `s 43(3) the pension the person is entitled to out of the group` ; tests: ssc3-tests-a.l4 |
| 43(6) | 1244 | encoded | ssc3-a-s43-s44.l4: `s 43(6) the pension is a retirement pension for the purposes of section 43` ; tests: ssc3-tests-a.l4 |
| 44 | 1245 | inert (reason 1) | the title of the section, not operative |
| 44(1), 44(1)(a), 44(1)(b) | 1246-1248 | encoded | ssc3-a-s43-s44.l4: `s 44(1) the person is entitled to a Category A retirement pension` ; tests: ssc3-tests-a.l4 |
| 44(1) closing words | 1249 | encoded | ssc3-a-s43-s44.l4: `s 44(1) the person is entitled to a Category A retirement pension`; `s 44(1) the day on which the person becomes entitled`; `s 44(1) the entitlement is running on the day` ; tests: ssc3-tests-a.l4 |
| 44(1A), 44(1A)(a), 44(1A)(b) | 1250-1252 | encoded | ssc3-a-s43-s44.l4: `s 44(1A) the relevant conditions or condition` ; tests: ssc3-tests-a.l4 |
| 44(2) | 1253 | encoded | ssc3-a-s43-s44.l4: `s 44(2) the Category A retirement pension is payable in respect of the day` ; tests: ssc3-tests-a.l4 |
| 44(3), 44(3)(a) | 1254-1255 | encoded | ssc3-a-s43-s44.l4: `s 44(3)(a) the Category A retirement pension consists of a basic pension`; `s 44(3)(b) an additional pension is payable as part of the Category A retirement pension` ; tests: ssc3-tests-a.l4 |
| 44(3)(b), 44(3) closing words | 1256-1257 | encoded | ssc3-a-s43-s44.l4: `s 44(3)(b) an additional pension is payable as part of the Category A retirement pension` ; tests: ssc3-tests-a.l4 |
| 44(4) | 1258-1259 | encoded | ssc3-a-s43-s44.l4: `s 44(4) the weekly rate of the basic pension in pounds`; `s 44(4) the day of entitlement is one for which the lower rate is payable` ; tests: ssc3-tests-a.l4 |
| 44(5) | 1260 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 44(5A), 44(5A)(a) | 1261-1262 | encoded | ssc3-a-s43-s44.l4: `s 44(5A)(a) there is a surplus in the pensioner's earnings factor for the relevant year`; `s 44(5A)(b) the amount of the surplus in pounds`; `s 44(5A)(c) the adjusted amount of the surplus in pounds` ; tests: ssc3-tests-a.l4 |
| 44(5A)(b) | 1263 | encoded | ssc3-a-s43-s44.l4: `s 44(5A)(b) the amount of the surplus in pounds`; `s 44(5A)(c) the adjusted amount of the surplus in pounds` ; tests: ssc3-tests-a.l4 |
| 44(5A)(c) | 1264 | fork F6 | ssc3-a-s43-s44.l4: `s 44(5A)(c) the adjusted amount of the surplus in pounds` ; tests: ssc3-tests-a.l4 ; see Fork register F6 |
| 44(6), 44(6)(za), 44(6)(a), 44(6)(a)(i), 44(6)(a)(ii), 44(6)(b), 44(6)(b)(i), 44(6)(b)(ii) | 1265-1272 | encoded | ssc3-a-s43-s44.l4: `s 44(6) the pensioner's earnings factor for the relevant year` ; tests: ssc3-tests-a.l4 |
| 44(7) | 1273 | encoded | ssc3-a-s43-s44.l4: `s 44(7)(a) the tax year is a relevant year`; `s 44(7)(b) the final relevant year`; `s 44(7)(c) the applicable limit in pounds` ; tests: ssc3-tests-a.l4 |
| 44(7)(a) | 1274 | fork F1 | ssc3-a-s43-s44.l4: `s 44(7)(a) the tax year is a relevant year`; `s 44(7)(b) the final relevant year`; `s 44(7)(c) the applicable limit in pounds` ; tests: ssc3-tests-a.l4 ; see Fork register F1 |
| 44(7)(a)(i), 44(7)(a)(ii) | 1275-1276 | encoded | ssc3-a-s43-s44.l4: `s 44(7)(a) the tax year is a relevant year`; `s 44(7)(b) the final relevant year`; `s 44(7)(c) the applicable limit in pounds` ; tests: ssc3-tests-a.l4 |
| 44(7)(b) | 1277 | fork F1 | ssc3-a-s43-s44.l4: `s 44(7)(b) the final relevant year`; `s 44(7)(c) the applicable limit in pounds` ; tests: ssc3-tests-a.l4 ; see Fork register F1 |
| 44(7)(c), 44(7)(c)(i), 44(7)(c)(ii) | 1278-1280 | encoded | ssc3-a-s43-s44.l4: `s 44(7)(c) the applicable limit in pounds` ; tests: ssc3-tests-a.l4 |
| 44(7A) | 1281 | inert (reason 2) | a power for the Secretary of State to prescribe how earnings factors are calculated; the calculated factors arrive as inputs (reason 2) |
| 44(8) | 1282 | encoded | ssc3-a-s43-s44.l4: `s 44(8) the order is treated as an order under section 148 of the Administration Act` ; tests: ssc3-tests-a.l4 |
| 44A | 1283 | inert (reason 1) | the title of the section, not operative |
| 44A(A1) | 1284 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(A1) subsections (1) to (4) apply to the year` ; tests: ssc3-tests-b.l4 |
| 44A(1), 44A(1)(a), 44A(1)(b) | 1285-1287 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2) any of the conditions in subsection (2) is satisfied`; `s 44A(1) the deemed earnings factor in pounds` ; tests: ssc3-tests-b.l4 |
| 44A(2) | 1288 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2) any of the conditions in subsection (2) is satisfied` ; tests: ssc3-tests-b.l4 |
| 44A(2)(a), 44A(2)(a)(i), 44A(2)(a)(ii) | 1289-1291 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2)(a) the earnings factor lies from the qualifying earnings factor up to the low earnings threshold` ; tests: ssc3-tests-b.l4 |
| 44A(2)(b), 44A(2)(b)(i), 44A(2)(b)(ii) | 1292-1294 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2)(b) carer's allowance condition` ; tests: ssc3-tests-b.l4 |
| 44A(2)(c), 44A(2)(c)(i), 44A(2)(c)(ii) | 1295-1297 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2)(c) responsibilities at home condition` ; tests: ssc3-tests-b.l4 |
| 44A(2)(d), 44A(2)(d)(i), 44A(2)(d)(ii) | 1298-1300 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(2)(d) incapacity benefit condition` ; tests: ssc3-tests-b.l4 |
| 44A(3), 44A(3)(a), 44A(3)(b) | 1301-1303 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(3) the requirement referred to in subsection (2)(d) is satisfied` ; tests: ssc3-tests-b.l4 |
| 44A(4), 44A(4)(a), 44A(4)(a)(i), 44A(4)(a)(ii) | 1304-1307 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(4)(a) the pensioner's working life in years`; `s 44A(4)(b) one tenth of the working life rounded to the nearest whole year` ; tests: ssc3-tests-b.l4 |
| 44A(4)(b) | 1308 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(4)(b) one tenth of the working life rounded to the nearest whole year` ; tests: ssc3-tests-b.l4 |
| 44A(4A), 44A(4A)(a), 44A(4A)(b) | 1309-1311 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(4A) the requirement in subsection (2)(d) and subsections (3) and (4) apply to the pensioner` ; tests: ssc3-tests-b.l4 |
| 44A(5) | 1312 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(5) the low earnings threshold in pounds` ; tests: ssc3-tests-b.l4 |
| 44A(5A) | 1313 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(5A) the applicable limit in pounds` ; tests: ssc3-tests-b.l4 |
| 44A(6) | 1314 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(6) the scheme is an occupational pension scheme`; `s 44A(6) the scheme is a personal pension scheme` ; tests: ssc3-tests-b.l4 |
| 44A(7), 44A(7)(a), 44A(7)(b), 44A(7)(c), 44A(7)(c)(i), 44A(7)(c)(ii), 44A(7) closing words | 1315-1321 | encoded | ssc3-b-s44a-s44c.l4: `s 44A(7) the allowance is qualifying employment and support allowance` ; tests: ssc3-tests-b.l4 |
| 44B | 1322 | inert (reason 1) | the title of the section, not operative |
| 44B(1) | 1323 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(1) this section applies to the year` ; tests: ssc3-tests-b.l4 |
| 44B(2), 44B(2)(a), 44B(2)(b) | 1324-1326 | fork F4 | ssc3-b-s44a-s44c.l4: `s 44B(2) the deemed earnings factor in pounds` ; tests: ssc3-tests-b.l4 ; see Fork register F4 |
| 44B(3), 44B(3)(a), 44B(3)(b) | 1327-1329 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(3) Condition A is satisfied` ; tests: ssc3-tests-b.l4 |
| 44B(4), 44B(4)(a), 44B(4)(b) | 1330-1332 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(4) Condition B is satisfied` ; tests: ssc3-tests-b.l4 |
| 44B(5) | 1333 | fork F5 | ssc3-b-s44a-s44c.l4: `s 44B(5) Condition C is satisfied` ; tests: ssc3-tests-b.l4 ; see Fork register F5 |
| 44B(6), 44B(6)(a), 44B(6)(b) | 1334-1336 | fork F4 | ssc3-b-s44a-s44c.l4: `s 44B(6)(b) Condition A is available`; `s 44B(6)(a) the aggregate is one that subsection (2)(b) refers to` ; tests: ssc3-tests-b.l4 ; see Fork register F4 |
| 44B(7) | 1337 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(7)(b) the low earnings threshold in pounds`; `s 44B(7)(c) the pensioner's earnings factor for a relevant year` (by its paragraphs) ; tests: ssc3-tests-b.l4 |
| 44B(7)(a) | 1338 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 44B(7)(b) | 1339 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(7)(b) the low earnings threshold in pounds` ; tests: ssc3-tests-b.l4 |
| 44B(7)(c) | 1340 | encoded | ssc3-b-s44a-s44c.l4: `s 44B(7)(c) the pensioner's earnings factor for a relevant year` ; tests: ssc3-tests-b.l4 |
| 44C | 1341 | inert (reason 1) | the title of the section, not operative |
| 44C(1) | 1342 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(1) this section applies to the year` ; tests: ssc3-tests-b.l4 |
| 44C(2), 44C(2)(a), 44C(2)(b), 44C(2) closing words | 1343-1347 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(2) the earnings factor credit for the week in pounds` ; tests: ssc3-tests-b.l4 |
| 44C(3), 44C(3)(a), 44C(3)(b), 44C(3)(c), 44C(3)(d), 44C(3)(d)(i), 44C(3)(d)(ii), 44C(3)(e) | 1348-1355 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(3) the pensioner is eligible for earnings factor enhancement in respect of the week` ; tests: ssc3-tests-b.l4 |
| 44C(4) | 1356 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(4) the scheme is an occupational pension scheme`; `s 44C(4) the scheme is a personal pension scheme` ; tests: ssc3-tests-b.l4 |
| 44C(5) | 1357 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(5) the aggregate amount of credits the pensioner is entitled to for Condition B` ; tests: ssc3-tests-b.l4 |
| 44C(6) | 1358 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(6) the tax year the week is treated as falling in` ; tests: ssc3-tests-b.l4 |
| 44C(7), 44C(7)(a), 44C(7)(b) | 1359-1361 | encoded | ssc3-b-s44a-s44c.l4: `s 44C(7)(b) the earnings factor the person is treated as having for the year by virtue of subsection (2)` ; tests: ssc3-tests-b.l4 |
| 45 | 1362 | inert (reason 1) | the title of the section, not operative |
| 45(1), 45(1)(a) | 1363-1364 | encoded | ssc3-c-s45-s46.l4: `s 45(1) the weekly rate of the additional pension in pounds` ; tests: ssc3-tests-c.l4 |
| 45(1)(b) | 1365 | encoded | ssc3-c-s45-s46.l4: `s 45(1)(b) the weekly amount for the units of additional pension in pounds`; `s 45(1) the weekly rate of the additional pension in pounds` ; tests: ssc3-tests-c.l4 |
| 45(2), 45(2)(a), 45(2)(b), 45(2)(c), 45(2)(d), 45(2)(e) | 1366-1371 | encoded | ssc3-c-s45-s46.l4: `s 45(2) the weekly rate of the additional pension in pounds` ; tests: ssc3-tests-c.l4 |
| 45(2A) | 1372 | encoded | ssc3-c-s45-s46.l4: `s 45(2A) the specified amount for each unit in pounds` ; tests: ssc3-tests-c.l4 |
| 45(3), 45(3)(a), 45(3)(b) | 1373-1375 | encoded | ssc3-c-s45-s46.l4: `s 45(3) the relevant percentage` ; tests: ssc3-tests-c.l4 |
| 45(3A), 45(3A)(a), 45(3A)(b) | 1376-1378 | encoded | ssc3-c-s45-s46.l4: `s 45(3A) the tax year falls within this subsection` ; tests: ssc3-tests-c.l4 |
| 45(4), 45(4)(a) | 1379-1380 | encoded | ssc3-c-s45-s46.l4: `s 45(4)(a) X` ; tests: ssc3-tests-c.l4 |
| 45(4)(b), 45(4) closing words | 1381-1382 | encoded | ssc3-c-s45-s46.l4: `s 45(4)(b) N` ; tests: ssc3-tests-c.l4 |
| 45(5), 45(5)(a), 45(5)(b), 45(5)(c), 45(5) closing words | 1383-1387 | encoded | ssc3-c-s45-s46.l4: `s 45(5) N after the years directed to be disregarded`; `s 45(5) the year is one the regulations may direct to be disregarded` ; tests: ssc3-tests-c.l4 |
| 45(6) | 1388 | encoded | ssc3-c-s45-s46.l4: `s 45(6) the weekly equivalent of the amount in pounds` ; tests: ssc3-tests-c.l4 |
| 45(7) | 1389 | encoded | ssc3-c-s45-s46.l4: `s 45(7) the amount calculated under subsection (6) is taken to be zero` ; tests: ssc3-tests-c.l4 |
| 45(8) | 1390 | inert (reason 2) | the sums are subject to alteration by orders under section 150 of the Administration Act; the sums arrive as inputs (reason 2) |
| 45AA | 1391 | inert (reason 1) | the title of the section, not operative |
| 45AA(1), 45AA(1)(a), 45AA(1)(b) | 1392-1394 | encoded | ssc3-c-s45-s46.l4: `s 45AA(1) the qualifying earnings treated as paid in pounds` ; tests: ssc3-tests-c.l4 |
| 45AA(2), 45AA(2)(a), 45AA(2)(b) | 1395-1397 | encoded | ssc3-c-s45-s46.l4: `s 45AA(1) the qualifying earnings treated as paid in pounds`; `s 45AA(2) the person in respect of whom the credit is paid` ; tests: ssc3-tests-c.l4 |
| 45AA(3) | 1398 | encoded | ssc3-c-s45-s46.l4: `s 45AA(1) the qualifying earnings treated as paid in pounds` ; tests: ssc3-tests-c.l4 |
| 45AA(4) | 1399 | encoded | ssc3-c-s45-s46.l4: `s 45AA(4) subsection (1) applies to the woman` ; tests: ssc3-tests-c.l4 |
| 45AA(5), 45AA(5)“couple” | 1400-1401 | encoded | ssc3-c-s45-s46.l4: `s 45AA(5) the two persons are a couple`; `s 45AA(5) the tax year is a relevant year` ; tests: ssc3-tests-c.l4 |
| 45AA(5)“relevant year” | 1402 | encoded | ssc3-c-s45-s46.l4: `s 45AA(5) the tax year is a relevant year` ; tests: ssc3-tests-c.l4 |
| 45A | 1403 | inert (reason 1) | the title of the section, not operative |
| 45A [text] | 1404 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 45B | 1405 | inert (reason 1) | the title of the section, not operative |
| 45B(1), 45B(1)(a), 45B(1)(b) | 1406-1408 | encoded | ssc3-c-s45-s46.l4: `s 45B(1) the weekly rate of the additional pension is reduced` ; tests: ssc3-tests-c.l4 |
| 45B(2) | 1409 | encoded | ssc3-c-s45-s46.l4: `s 45B(2) the weekly rate of the additional pension after the reduction in pounds` ; tests: ssc3-tests-c.l4 |
| 45B(3) | 1410 | fork F6 | ssc3-c-s45-s46.l4: `s 45B(2) the weekly rate of the additional pension after the reduction in pounds` ; tests: ssc3-tests-c.l4 ; see Fork register F6 |
| 45B(4) | 1411 | encoded | ssc3-c-s45-s46.l4: `s 45B(4) the appropriate weekly amount in pounds` ; tests: ssc3-tests-c.l4 |
| 45B(5), 45B(5)(a), 45B(5)(b) | 1412-1414 | encoded | ssc3-c-s45-s46.l4: `s 45B(5) the day the notional pension becomes payable` ; tests: ssc3-tests-c.l4 |
| 45B(6) | 1415 | encoded | ssc3-c-s45-s46.l4: `s 45B(6) the relevant revaluation percentage` ; tests: ssc3-tests-c.l4 |
| 45B(7) | 1416 | inert (reason 2) | the regulation-making power about cash equivalents, including its subsection (7A) and paragraphs; the appropriate weekly amount arrives as an input (reason 2) |
| 45B(7A), 45B(7A)(a), 45B(7A)(b) | 1417-1419 | inert (reason 2) | the regulation-making power about cash equivalents (reason 2) |
| 45B(8), 45B(8)“final relevant year” | 1420-1421 | encoded | ssc3-c-s45-s46.l4: `s 45B(8) the final relevant year`; `s 45B(8) the debit is a state scheme pension debit`; `s 45B(8) the valuation day` ; tests: ssc3-tests-c.l4 |
| 45B(8)“state scheme pension debit” | 1422 | encoded | ssc3-c-s45-s46.l4: `s 45B(8) the debit is a state scheme pension debit`; `s 45B(8) the valuation day` ; tests: ssc3-tests-c.l4 |
| 45B(8)“valuation day” | 1423 | encoded | ssc3-c-s45-s46.l4: `s 45B(8) the valuation day` ; tests: ssc3-tests-c.l4 |
| 46 | 1424 | inert (reason 1) | the title of the section, not operative |
| 46(1) | 1425 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 46(2) | 1426 | encoded | ssc3-c-s45-s46.l4: `s 46(2) the substituted definition of N applies` ; tests: ssc3-tests-c.l4 |
| 46(2)“N” | 1427 | encoded | ssc3-c-s45-s46.l4: `s 46(2) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(2)(a) | 1428 | encoded | ssc3-c-s45-s46.l4: `s 46(2)(a) the number of tax years which begin after 5th April 1978 and end before the date`; `s 46(2) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(2)(b) | 1429 | fork F1 | ssc3-c-s45-s46.l4: `s 46(2)(b) the number of tax years from the sixteenth birthday or 1978-79 to the year before S would have attained pensionable age`; `s 46(2) the substituted N` ; tests: ssc3-tests-c.l4 ; see Fork register F1 |
| 46(2)(b)(i), 46(2)(b)(ii) | 1430-1431 | encoded | ssc3-c-s45-s46.l4: `s 46(2)(b) the number of tax years from the sixteenth birthday or 1978-79 to the year before S would have attained pensionable age`; `s 46(2) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(2) closing words | 1432 | encoded | ssc3-c-s45-s46.l4: `s 46(2) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(3) | 1433-1434 | encoded | ssc3-c-s45-s46.l4: `s 46(3) the substituted N`; `s 46(3) the substituted definition of N applies` ; tests: ssc3-tests-c.l4 |
| 46(3)(a) | 1435 | encoded | ssc3-c-s45-s46.l4: `s 46(3)(a) the number of tax years which begin after 5th April 1978 and end before the date`; `s 46(3) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(3)(b) | 1436 | fork F1 | ssc3-c-s45-s46.l4: `s 46(3)(b) the number of tax years from the sixteenth birthday or 1978-79 to the year before S would have attained pensionable age`; `s 46(3) the substituted N` ; tests: ssc3-tests-c.l4 ; see Fork register F1 |
| 46(3)(b)(i), 46(3)(b)(ii) | 1437-1438 | encoded | ssc3-c-s45-s46.l4: `s 46(3)(b) the number of tax years from the sixteenth birthday or 1978-79 to the year before S would have attained pensionable age`; `s 46(3) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(3) closing words | 1439 | encoded | ssc3-c-s45-s46.l4: `s 46(3) the substituted N` ; tests: ssc3-tests-c.l4 |
| 46(4), 46(4)(a), 46(4)(b) | 1440-1442 | encoded | ssc3-c-s45-s46.l4: `s 46(4) section 45 has effect subject to the additional modifications` ; tests: ssc3-tests-c.l4 |
| 47 | 1443 | inert (reason 1) | the title of the section, not operative |
| 47(1) | 1444 | encoded | ssc3-d-s47-s48c.l4: `s 47(1) the increase of the weekly rate in pounds` ; tests: ssc3-tests-d.l4 |
| 47(1)(a) | 1445 | encoded | ssc3-d-s47-s48c.l4: `s 47(1)(a) the day falls within the period of weeks ending immediately before the day the pensioner attains pensionable age`; `s 47(1) the increase of the weekly rate in pounds` ; tests: ssc3-tests-d.l4 |
| 47(1)(b) | 1446 | encoded | ssc3-d-s47-s48c.l4: `s 47(1)(b) the last day before the beginning of the period`; `s 47(1) the increase of the weekly rate in pounds` ; tests: ssc3-tests-d.l4 |
| 47(1) closing words | 1447 | encoded | ssc3-d-s47-s48c.l4: `s 47(1) the increase of the weekly rate in pounds` ; tests: ssc3-tests-d.l4 |
| 47(2) | 1448 | encoded | ssc3-d-s47-s48c.l4: `s 47(2) the increase after the deduction in pounds` ; tests: ssc3-tests-d.l4 |
| 47(3) | 1449 | encoded | ssc3-d-s47-s48c.l4: `s 47(3) the relevant amount in pounds` ; tests: ssc3-tests-d.l4 |
| 47(3A) | 1450 | encoded | ssc3-d-s47-s48c.l4: `s 47(3A) the additional pension for subsections (2) and (3) in pounds` ; tests: ssc3-tests-d.l4 |
| 47(3B) | 1451 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "For units of additional pension, see section 14A." |
| 47(4) | 1452 | encoded | ssc3-d-s47-s48c.l4: `s 47(4) the additional pension in pounds` ; tests: ssc3-tests-d.l4 |
| 47(5) | 1453 | encoded | ssc3-d-s47-s48c.l4: `s 47(5) the rate of the age addition in pounds` ; tests: ssc3-tests-d.l4 |
| 47(6) | 1454 | encoded | ssc3-d-s47-s48c.l4: `s 47(6) the number of weeks of subsection (1)` ; tests: ssc3-tests-d.l4 |
| 48 | 1455 | inert (reason 1) | the title of the section, not operative |
| 48(1), 48(1)(a), 48(1)(b), 48(1) closing words | 1456-1459 | encoded | ssc3-d-s47-s48c.l4: `s 48(1) the former spouse's or civil partner's contributions may be treated as the person's own` ; tests: ssc3-tests-d.l4 |
| 48(2) | 1460 | encoded | ssc3-d-s47-s48c.l4: `s 48(2) subsection (1) is disapplied for the person` ; tests: ssc3-tests-d.l4 |
| 48(2A) | 1461 | encoded | ssc3-d-s47-s48c.l4: `s 48(2A) regulations under subsection (1) may provide for contributions in respect of the time to be treated as another person's` ; tests: ssc3-tests-d.l4 |
| 48(3) | 1462 | encoded | ssc3-d-s47-s48c.l4: `s 48(3) the relationship is not excluded by subsection (3)` ; tests: ssc3-tests-d.l4 |
| 48(4) | 1463 | encoded | ssc3-d-s47-s48c.l4: `s 48(4) the relationship is a relevant relationship` ; tests: ssc3-tests-d.l4 |
| 48(5) [version 1] | 1464 | encoded | ssc3-d-s47-s48c.l4: `s 48(5) first version: the civil partnership is treated as having terminated by reason of the conversion` ; tests: ssc3-tests-d.l4 |
| 48(5) [version 2], 48(5)(a), 48(5)(b), 48(5)(c), 48(5)(d) | 1465-1469 | encoded | ssc3-d-s47-s48c.l4: `s 48(5) the civil partnership is treated as having terminated` ; tests: ssc3-tests-d.l4 |
| 48(6) | 1470 | encoded | ssc3-d-s47-s48c.l4: `s 48(6) the marriage is treated as having terminated` ; tests: ssc3-tests-d.l4 |
| 48A | 1471 | inert (reason 1) | the title of the section, not operative |
| 48A(1), 48A(1)(a), 48A(1)(b), 48A(1)(b)(i), 48A(1)(b)(ii) | 1472-1476 | encoded | ssc3-d-s47-s48c.l4: `s 48A(1) the married person is entitled to a Category B retirement pension by virtue of the spouse's contributions` ; tests: ssc3-tests-d.l4 |
| 48A(2), 48A(2)(a), 48A(2)(b) | 1477-1479 | encoded | ssc3-d-s47-s48c.l4: `s 48A(2) subsection (1) does not confer a right on the person` ; tests: ssc3-tests-d.l4 |
| 48A(3), 48A(3)(a), 48A(3)(b), 48A(3)(b)(i), 48A(3)(b)(ii), 48A(3)(b)(iii) | 1480-1485 | encoded | ssc3-d-s47-s48c.l4: `s 48A(3) the civil partner is entitled to a Category B retirement pension by virtue of the contributions of the contributing civil partner` ; tests: ssc3-tests-d.l4 |
| 48A(4) | 1486 | encoded | ssc3-d-s47-s48c.l4: `s 48A(4) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-d.l4 |
| 48A(5), 48A(5)(a), 48A(5)(b) | 1487-1489 | encoded | ssc3-d-s47-s48c.l4: `s 48A(5) the person ceases to be entitled to the Category B retirement pension under section 48A` ; tests: ssc3-tests-d.l4 |
| 48A(6), 48A(6)(a), 48A(6)(b) | 1490-1492 | encoded | ssc3-d-s47-s48c.l4: `s 48A(6) the relevant contribution condition` ; tests: ssc3-tests-d.l4 |
| 48A(6A), 48A(6A)(a), 48A(6A)(b) | 1493-1495 | encoded | ssc3-d-s47-s48c.l4: `s 48A(6A) the person is treated as having ceased to be in a civil partnership` ; tests: ssc3-tests-d.l4 |
| 48A(6B) | 1496 | encoded | ssc3-d-s47-s48c.l4: `s 48A(6B) the person is treated as having ceased to be married` ; tests: ssc3-tests-d.l4 |
| 48A(7) | 1497 | encoded | ssc3-d-s47-s48c.l4: `s 48A(7) the earnings factor of the spouse or contributing civil partner for the tax year is taken into account` ; tests: ssc3-tests-d.l4 |
| 48A(8) | 1498 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "Section 51ZA contains special rules ..." |
| 48AA | 1499 | inert (reason 1) | the title of the section, not operative |
| 48AA(1), 48AA(1)(a), 48AA(1)(a)(i), 48AA(1)(a)(ii), 48AA(1)(b), 48AA(1)(b)(i), 48AA(1)(b)(ii) | 1500-1506 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(1) the person whose marriage has been dissolved is entitled to a Category B retirement pension by virtue of the former spouse's contributions` ; tests: ssc3-tests-d.l4 |
| 48AA(2), 48AA(2)(a), 48AA(2)(b) | 1507-1509 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(2) subsection (1) does not confer a right on the person` ; tests: ssc3-tests-d.l4 |
| 48AA(3), 48AA(3)(a), 48AA(3)(a)(i), 48AA(3)(a)(ii), 48AA(3)(b), 48AA(3)(b)(i), 48AA(3)(b)(ii), 48AA(3)(b)(iii) | 1510-1517 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(3) the person whose civil partnership has been dissolved is entitled to a Category B retirement pension by virtue of the former civil partner's contributions` ; tests: ssc3-tests-d.l4 |
| 48AA(4), 48AA(5) | 1518-1519 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(4) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-d.l4 |
| 48AA(6), 48AA(6)(a), 48AA(6)(b) | 1520-1522 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(6) the relevant contribution condition` ; tests: ssc3-tests-d.l4 |
| 48AA(7) | 1523 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(7) the earnings factor of the former spouse or civil partner for the tax year is taken into account` ; tests: ssc3-tests-d.l4 |
| 48AA(8) | 1524 | encoded | ssc3-d-s47-s48c.l4: `s 48AA(8) the date on which the marriage or civil partnership is treated as dissolved` ; tests: ssc3-tests-d.l4 |
| 48AA(9) | 1525 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "Section 51ZA contains special rules ..." |
| 48B | 1526 | inert (reason 1) | the title of the section, not operative |
| 48B(1), 48B(1)(a), 48B(1)(a)(i), 48B(1)(a)(ii), 48B(1)(b) | 1527-1531 | encoded | ssc3-d-s47-s48c.l4: `s 48B(1) the person whose spouse died is entitled to a Category B retirement pension by virtue of the spouse's contributions` ; tests: ssc3-tests-d.l4 |
| 48B(1ZA), 48B(1ZA)(a), 48B(1ZA)(b) | 1532-1534 | encoded | ssc3-d-s47-s48c.l4: `s 48B(1ZA) subsection (1) does not confer a right on the person` ; tests: ssc3-tests-d.l4 |
| 48B(1ZB), 48B(1ZB)(a), 48B(1ZB)(a)(i), 48B(1ZB)(a)(ii), 48B(1ZB) closing words, 48B(1ZB)(b) | 1535-1540 | encoded | ssc3-d-s47-s48c.l4: `s 48B(1ZB) the relevant contribution condition` ; tests: ssc3-tests-d.l4 |
| 48B(1A), 48B(1A)(a), 48B(1A)(a)(i), 48B(1A)(a)(ii), 48B(1A)(b) | 1541-1545 | encoded | ssc3-d-s47-s48c.l4: `s 48B(1A) the person whose civil partner died is entitled to a Category B retirement pension by virtue of the civil partner's contributions` ; tests: ssc3-tests-d.l4 |
| 48B(1B), 48B(1B)(a), 48B(1B)(b) | 1546-1548 | encoded | ssc3-d-s47-s48c.l4: `s 48B(1B) the relevant contribution condition` ; tests: ssc3-tests-d.l4 |
| 48B(2), 48B(2)(a), 48B(2)(b), 48B(2) closing words | 1549-1552 | encoded | ssc3-d-s47-s48c.l4: `s 48B(2) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-d.l4 |
| 48B(3) | 1553 | encoded | ssc3-d-s47-s48c.l4: `s 48B(3) the tax year taken as the tax year in which the pensioner attained pensionable age` ; tests: ssc3-tests-d.l4 |
| 48B(3A) | 1554 | encoded | ssc3-d-s47-s48c.l4: `s 48B(3A) the earnings factor of the deceased for the tax year is taken into account` ; tests: ssc3-tests-d.l4 |
| 48B(4), 48B(4)(a), 48B(4)(b) | 1555-1557 | encoded | ssc3-d-s47-s48c.l4: `s 48B(4) the woman whose husband died before she attained pensionable age is entitled to a Category B retirement pension` ; tests: ssc3-tests-d.l4 |
| 48B(4A), 48B(4A)(a), 48B(4A)(b) | 1558-1560 | encoded | ssc3-d-s47-s48c.l4: `s 48B(4A) the man whose wife died before he attained pensionable age is entitled to a Category B retirement pension` ; tests: ssc3-tests-d.l4 |
| 48B(5), 48B(5)(a), 48B(5)(b) | 1561-1563 | encoded | ssc3-d-s47-s48c.l4: `s 48B(5) the condition is satisfied` ; tests: ssc3-tests-d.l4 |
| 48B(6), 48B(6)(a), 48B(6)(b) | 1564-1566 | encoded | ssc3-d-s47-s48c.l4: `s 48B(6) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-d.l4 |
| 48B(7) | 1567 | encoded | ssc3-d-s47-s48c.l4: `s 48B(7) the man is entitled by virtue of section 38 on the assumption` ; tests: ssc3-tests-d.l4 |
| 48B(8) | 1568 | encoded | ssc3-d-s47-s48c.l4: `s 48B(8) subsections (4) to (7) are disapplied` ; tests: ssc3-tests-d.l4 |
| 48B(9) | 1569 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "Section 51ZA contains special rules ..." |
| 48B(10), 48B(10)(a), 48B(10)(b), 48B(11) | 1570-1573 | encoded | ssc3-d-s47-s48c.l4: `s 48B(11) the weekly rate of the additional pension after the increase in pounds` ; tests: ssc3-tests-d.l4 |
| 48BB | 1574 | inert (reason 1) | the title of the section, not operative |
| 48BB(1), 48BB(1)(a), 48BB(1)(b) | 1575-1577 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(2) the pensioner is entitled to a Category B retirement pension at the rate of the widowed parent's allowance` ; tests: ssc3-tests-d.l4 |
| 48BB(2) | 1578 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(2) the pensioner is entitled to a Category B retirement pension at the rate of the widowed parent's allowance`; `s 48BB(2) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-d.l4 |
| 48BB(3), 48BB(3)(a), 48BB(3)(a)(i), 48BB(3)(a)(ii), 48BB(3)(b), 48BB(4) | 1579-1584 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(4) the pensioner is entitled to a Category B retirement pension by virtue of the contributions of the spouse or civil partner` ; tests: ssc3-tests-d.l4 |
| 48BB(5) | 1585 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(5) the weekly rate of the Category B retirement pension before the adjustments in pounds` ; tests: ssc3-tests-d.l4 |
| 48BB(6) | 1586 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(6) the tax year taken as the tax year in which the pensioner attained pensionable age` ; tests: ssc3-tests-d.l4 |
| 48BB(7) | 1587 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(7) the weekly rate before any reduction under subsection (8) in pounds` ; tests: ssc3-tests-d.l4 |
| 48BB(8), 48BB(8)(a), 48BB(8)(b) | 1588-1590 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(8) the weekly rate after the reduction in pounds` ; tests: ssc3-tests-d.l4 |
| 48BB(9), 48BB(9)(a), 48BB(9)(b) | 1591-1593 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(9) the relevant time` ; tests: ssc3-tests-d.l4 |
| 48BB(10) | 1594 | encoded | ssc3-d-s47-s48c.l4: `s 48BB(10) the weekly rate after the increase in pounds` ; tests: ssc3-tests-d.l4 |
| 48C | 1595 | inert (reason 1) | the title of the section, not operative |
| 48C(1) | 1596 | encoded | ssc3-d-s47-s48c.l4: `s 48C(1) the entitlement to a Category B retirement pension is running on the day` ; tests: ssc3-tests-d.l4 |
| 48C(2), 48C(2)(a), 48C(2)(b), 48C(2) closing words | 1597-1600 | encoded | ssc3-d-s47-s48c.l4: `s 48C(2) section 47(1) applies also for the increase of the Category B retirement pension` ; tests: ssc3-tests-d.l4 |
| 48C(3) | 1601 | encoded | ssc3-d-s47-s48c.l4: `s 48C(3) the words "half of" are omitted from section 48B(2)(b)` ; tests: ssc3-tests-d.l4 |
| 48C(4) | 1602 | encoded | ssc3-d-s47-s48c.l4: `s 48C(4) the person to whom a reference to the pensioner is taken to refer` ; tests: ssc3-tests-d.l4 |
| 49 | 1603 | inert (reason 1) | the title of the section, not operative |
| 49 [text] | 1604 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 50 | 1605 | inert (reason 1) | the title of the section, not operative |
| 50 [text] | 1606 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 51 | 1607 | inert (reason 1) | the title of the section, not operative |
| 51(1), 51(1)(a), 51(1)(b), 51(1)(c) | 1608-1611 | encoded | ssc3-e-s51-s55.l4: `s 51(1) the person whose spouse died is entitled to a Category B retirement pension` ; tests: ssc3-tests-e.l4 |
| 51(2), 51(2)(a), 51(2)(b) | 1612-1614 | encoded | ssc3-e-s51-s55.l4: `s 51(2) subsection (1) does not confer a right on the person` ; tests: ssc3-tests-e.l4 |
| 51(3), 51(3)(a), 51(3)(b) | 1615-1617 | encoded | ssc3-e-s51-s55.l4: `s 51(3) the relevant contribution condition` ; tests: ssc3-tests-e.l4 |
| 51(4), 51(4)(a), 51(4)(b), 51(4)(c) | 1618-1621 | encoded | ssc3-e-s51-s55.l4: `s 51(4) the person whose civil partner died is entitled to a Category B retirement pension` ; tests: ssc3-tests-e.l4 |
| 51(5), 51(5)(a), 51(5)(b) | 1622-1624 | encoded | ssc3-e-s51-s55.l4: `s 51(5) the relevant contribution condition` ; tests: ssc3-tests-e.l4 |
| 51(6) | 1625 | encoded | ssc3-e-s51-s55.l4: `s 51(6) the person to whom a reference to the pensioner is taken to refer`; `s 51(6) the weekly rate of the Category B retirement pension in pounds` ; tests: ssc3-tests-e.l4 |
| 51(7), 51(7)(a), 51(7)(b), 51(7)(c), 51(7) closing words | 1626-1630 | encoded | ssc3-e-s51-s55.l4: `s 51(7) the amount of additional pension after any halving in pounds` ; tests: ssc3-tests-e.l4 |
| 51(8) | 1631 | encoded | ssc3-e-s51-s55.l4: `s 51(8) the earnings factor of the spouse or deceased civil partner for the tax year is taken into account` ; tests: ssc3-tests-e.l4 |
| 51(9) | 1632 | encoded | ssc3-e-s51-s55.l4: `s 51(9) the entitlement to a Category B retirement pension under section 51 is running on the day` ; tests: ssc3-tests-e.l4 |
| 51(10) | 1633 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "Section 51ZA contains special rules ..." |
| 51(11), 51(11)(a), 51(11)(b), 51(12) | 1634-1637 | encoded | ssc3-e-s51-s55.l4: `s 51(12) the weekly rate of the additional pension after the increase in pounds` ; tests: ssc3-tests-e.l4 |
| 51ZA | 1638 | inert (reason 1) | the title of the section, not operative |
| 51ZA(1), 51ZA(1)(a), 51ZA(1)(b) | 1639-1641 | encoded | ssc3-e-s51-s55.l4: `s 51ZA(1) section 48A(2)(b) does not prevent the woman from being entitled` ; tests: ssc3-tests-e.l4 |
| 51ZA(2), 51ZA(2)(a), 51ZA(2)(b) | 1642-1644 | encoded | ssc3-e-s51-s55.l4: `s 51ZA(2) section 48AA(2)(b) does not prevent the woman from being entitled` ; tests: ssc3-tests-e.l4 |
| 51ZA(3), 51ZA(3)(a), 51ZA(3)(b), 51ZA(3) closing words | 1645-1648 | encoded | ssc3-e-s51-s55.l4: `s 51ZA(3) the case of a woman whose dead spouse changed gender applies` ; tests: ssc3-tests-e.l4 |
| 51ZA(4), 51ZA(4)(a), 51ZA(4)(b) | 1649-1651 | encoded | ssc3-e-s51-s55.l4: `s 51ZA(4) section 51(1) does not confer a right on the woman` ; tests: ssc3-tests-e.l4 |
| 51A | 1652 | inert (reason 1) | the title of the section, not operative |
| 51A(1), 51A(1)(a), 51A(1)(b) | 1653-1655 | encoded | ssc3-e-s51-s55.l4: `s 51A(1) this section has effect` ; tests: ssc3-tests-e.l4 |
| 51A(2), 51A(2)(a), 51A(2)(b) | 1656-1658 | encoded | ssc3-e-s51-s55.l4: `s 51A(2) the increase of the basic pension in the Category A retirement pension in pounds` ; tests: ssc3-tests-e.l4 |
| 51A(3) | 1659 | encoded | ssc3-e-s51-s55.l4: `s 51A(3) this section does not apply` ; tests: ssc3-tests-e.l4 |
| 52 | 1660 | inert (reason 1) | the title of the section, not operative |
| 52(1), 52(1)(a), 52(1)(b) | 1661-1663 | encoded | ssc3-e-s51-s55.l4: `s 52(1) this section has effect` ; tests: ssc3-tests-e.l4 |
| 52(2), 52(2)(a), 52(2)(b), 52(2)“full amount” | 1664-1667 | encoded | ssc3-e-s51-s55.l4: `s 52(2) the increase of the basic pension in the Category A retirement pension in pounds` ; tests: ssc3-tests-e.l4 |
| 52(3), 52(3)(a), 52(3)(b) | 1668-1670 | encoded | ssc3-e-s51-s55.l4: `s 52(3) the increase of the additional pension in the Category A retirement pension in pounds` ; tests: ssc3-tests-e.l4 |
| 52(3A) | 1671 | encoded | ssc3-e-s51-s55.l4: `s 52(3A) the additional pension for subsection (3) in pounds` ; tests: ssc3-tests-e.l4 |
| 52(3B) | 1672 | encoded | ssc3-e-s51-s55.l4: `s 52(3B) the further increase of the additional pension in the Category A retirement pension in pounds` ; tests: ssc3-tests-e.l4 |
| 52(4) | 1673 | encoded | ssc3-e-s51-s55.l4: `s 52(4) this section does not apply` ; tests: ssc3-tests-e.l4 |
| 53 | 1674 | inert (reason 1) | the title of the section, not operative |
| 53 [text] | 1675 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 54 | 1676 | inert (reason 1) | the title of the section, not operative |
| 54(1), 54(1)(a), 54(1)(b), 54(1) closing words | 1677-1680 | inert (reason 2) | a power to make regulations about an election; the election's effect on deferment arrives at section 55(3)(b) as an input (reason 2) |
| 54(2) | 1681 | inert (reason 2) | a power to modify this Part by regulations (reason 2) |
| 54(3), 54(4) | 1682-1683 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 55 | 1684 | inert (reason 1) | the title of the section, not operative |
| 55(1) | 1685 | encoded | ssc3-e-s51-s55.l4: `s 55(1) Schedule 5 has effect` ; tests: ssc3-tests-e.l4 |
| 55(2) | 1686-1693 | inert (reason 1) | a roadmap of what a Schedule contains, which creates no rule (reason 1) (Schedule 5) |
| 55(3), 55(3)(a), 55(3)(b), 55(3) closing words | 1694-1697 | encoded | ssc3-e-s51-s55.l4: `s 55(3) the retirement pension is deferred` ; tests: ssc3-tests-e.l4 |
| heading@1698 | 1698 | inert (reason 1) | cross-heading of the Act, not operative |
| 55A | 1699 | inert (reason 1) | the title of the section, not operative |
| 55A(1), 55A(1)(a), 55A(1)(b) | 1700-1702 | encoded | ssc3-f-s55a-s56.l4: `s 55A(1) the person is entitled to a shared additional pension under section 55A` ; tests: ssc3-tests-f.l4 |
| 55A(2) | 1703 | encoded | ssc3-f-s55a-s56.l4: `s 55A(2) the entitlement to the shared additional pension under section 55A is running on the day` ; tests: ssc3-tests-f.l4 |
| 55A(3) | 1704 | fork F6 | ssc3-f-s55a-s56.l4: `s 55A(3) the weekly rate of the shared additional pension in pounds` ; tests: ssc3-tests-f.l4 ; see Fork register F6 |
| 55A(4) | 1705 | encoded | ssc3-f-s55a-s56.l4: `s 55A(4) the appropriate weekly amount in pounds` ; tests: ssc3-tests-f.l4 |
| 55A(5) | 1706 | encoded | ssc3-f-s55a-s56.l4: `s 55A(5) the relevant revaluation percentage` ; tests: ssc3-tests-f.l4 |
| 55A(6) | 1707 | inert (reason 2) | the regulation-making power about cash equivalents, including its subsection (6A) and paragraphs; the appropriate weekly amount arrives as an input (reason 2) |
| 55A(6A), 55A(6A)(a), 55A(6A)(b) | 1708-1710 | inert (reason 2) | the regulation-making power about cash equivalents (reason 2) |
| 55A(7), 55A(7)“final relevant year” | 1711-1712 | encoded | ssc3-f-s55a-s56.l4: `s 55A(7) the final relevant year` ; tests: ssc3-tests-f.l4 |
| 55A(7)“old state scheme pension credit” | 1713 | encoded | ssc3-f-s55a-s56.l4: `s 55A(7) the credit is an old state scheme pension credit` ; tests: ssc3-tests-f.l4 |
| 55A(7)“valuation day” | 1714 | encoded | ssc3-f-s55a-s56.l4: `s 55A(7) the valuation day` ; tests: ssc3-tests-f.l4 |
| 55AA | 1715 | inert (reason 1) | the title of the section, not operative |
| 55AA(1), 55AA(1)(a), 55AA(1)(b) | 1716-1718 | encoded | ssc3-f-s55a-s56.l4: `s 55AA(1) the person is entitled to a shared additional pension under section 55AA` ; tests: ssc3-tests-f.l4 |
| 55AA(2) | 1719 | encoded | ssc3-f-s55a-s56.l4: `s 55AA(2) the entitlement to the shared additional pension under section 55AA is running on the day` ; tests: ssc3-tests-f.l4 |
| 55AA(3) | 1720 | encoded | ssc3-f-s55a-s56.l4: `s 55AA(3) the weekly rate of the shared additional pension in pounds` ; tests: ssc3-tests-f.l4 |
| 55AA(4) | 1721 | encoded | ssc3-f-s55a-s56.l4: `s 55AA(4) the credit is a new state scheme pension credit` ; tests: ssc3-tests-f.l4 |
| 55B | 1722 | inert (reason 1) | the title of the section, not operative |
| 55B(1), 55B(1)(a), 55B(1)(b) | 1723-1725 | encoded | ssc3-f-s55a-s56.l4: `s 55B(1) the weekly rate of the shared additional pension after the reduction in pounds` ; tests: ssc3-tests-f.l4 |
| 55B(2) | 1726 | encoded | ssc3-f-s55a-s56.l4: `s 55B(2) the reduction of the weekly rate in pounds` ; tests: ssc3-tests-f.l4 |
| 55B(3) | 1727 | fork F6 | ssc3-f-s55a-s56.l4: `s 55B(3) the reduction of the weekly rate in pounds` ; tests: ssc3-tests-f.l4 ; see Fork register F6 |
| 55B(4) | 1728 | encoded | ssc3-f-s55a-s56.l4: `s 55B(4) the appropriate weekly amount in pounds` ; tests: ssc3-tests-f.l4 |
| 55B(5), 55B(5)(a), 55B(5)(b) | 1729-1731 | encoded | ssc3-f-s55a-s56.l4: `s 55B(5) the day the notional pension becomes payable` ; tests: ssc3-tests-f.l4 |
| 55B(6) | 1732 | encoded | ssc3-f-s55a-s56.l4: `s 55B(6) the relevant revaluation percentage` ; tests: ssc3-tests-f.l4 |
| 55B(7) | 1733 | inert (reason 2) | the regulation-making power about cash equivalents, including its subsection (7A) and paragraphs; the appropriate weekly amount arrives as an input (reason 2) |
| 55B(7A), 55B(7A)(a), 55B(7A)(b) | 1734-1736 | inert (reason 2) | the regulation-making power about cash equivalents (reason 2) |
| 55B(8), 55B(8)“final relevant year” | 1737-1738 | encoded | ssc3-f-s55a-s56.l4: `s 55B(8) the final relevant year` ; tests: ssc3-tests-f.l4 |
| 55B(8)“old state scheme pension debit” | 1739 | encoded | ssc3-f-s55a-s56.l4: `s 55B(8) the debit is an old state scheme pension debit` ; tests: ssc3-tests-f.l4 |
| 55B(8)“valuation day” | 1740 | encoded | ssc3-f-s55a-s56.l4: `s 55B(8) the valuation day` ; tests: ssc3-tests-f.l4 |
| 55C | 1741 | inert (reason 1) | the title of the section, not operative |
| 55C(1) | 1742 | encoded | ssc3-f-s55a-s56.l4: `s 55C(1) Schedule 5A has effect` ; tests: ssc3-tests-f.l4 |
| 55C(2) | 1743-1746 | inert (reason 1) | a roadmap of what a Schedule contains, which creates no rule (reason 1) (Schedule 5A) |
| 55C(3), 55C(3)(a), 55C(3)(b), 55C(3) closing words | 1747-1750 | encoded | ssc3-f-s55a-s56.l4: `s 55C(3) the shared additional pension is deferred` ; tests: ssc3-tests-f.l4 |
| heading@1751 | 1751 | inert (reason 1) | cross-heading of the Act, not operative |
| 56 | 1752 | inert (reason 1) | the title of the section, not operative |
| 56(1) | 1753 | encoded | ssc3-f-s55a-s56.l4: `s 56(1) the weekly rate of the child's special allowance in pounds`; `s 56(1) the woman is entitled to a child's special allowance`; `s 56(1) the child's special allowance is payable to the woman for the day, subject to subsections (2), (3) and (6)` ; tests: ssc3-tests-f.l4 |
| 56(1)(a), 56(1)(b), 56(1)(b)(i), 56(1)(b)(ii), 56(1)(c), 56(1)(c)(i), 56(1)(c)(ii) | 1754-1760 | encoded | ssc3-f-s55a-s56.l4: `s 56(1) the woman is entitled to a child's special allowance` ; tests: ssc3-tests-f.l4 |
| 56(2), 56(2)(a), 56(2)(b) | 1761-1763 | encoded | ssc3-f-s55a-s56.l4: `s 56(2) payment of the child's special allowance is barred for the period` ; tests: ssc3-tests-f.l4 |
| 56(3) | 1764 | encoded | ssc3-f-s55a-s56.l4: `s 56(3) payment of the amount is barred by subsection (3)` ; tests: ssc3-tests-f.l4 |
| 56(4), 56(4)(a), 56(4)(b) | 1765-1767 | encoded | ssc3-f-s55a-s56.l4: `s 56(4) one of the conditions specified in subsection (4) is satisfied` ; tests: ssc3-tests-f.l4 |
| 56(5), 56(5)(a), 56(5)(a)(i), 56(5)(a)(ii), 56(5)(b) | 1768-1772 | encoded | ssc3-f-s55a-s56.l4: `s 56(5) the condition in subsection (4)(b) is satisfied` ; tests: ssc3-tests-f.l4 |
| 56(6), 56(6)(a), 56(6)(b), 56(6) closing words | 1773-1776 | encoded | ssc3-f-s55a-s56.l4: `s 56(6) payment of the child's special allowance for the day is barred by subsection (6)` ; tests: ssc3-tests-f.l4 |
| heading@1777 | 1777 | inert (reason 1) | cross-heading of the Act, not operative |
| 57 | 1778 | inert (reason 1) | the title of the section, not operative |
| 57 [text] | 1779 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 58 | 1780 | inert (reason 1) | the title of the section, not operative |
| 58 [text] | 1781 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| heading@1782 | 1782 | inert (reason 1) | cross-heading of the Act, not operative |
| 59 | 1783 | inert (reason 1) | the title of the section, not operative |
| 59 [text] | 1784 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| heading@1785 | 1785 | inert (reason 1) | cross-heading of the Act, not operative |
| 60 | 1786 | inert (reason 1) | the title of the section, not operative |
| 60(1), 60(1)(a), 60(1)(aa) | 1787-1789 | encoded | ssc3-g-s60-s62.l4: `s 60(1) the retirement pension would be payable only by virtue of section 60` ; tests: ssc3-tests-g.l4 |
| 60(1)(ab) | 1790 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 60(1)(b), 60(1)(c), 60(1)(d), 60(1) closing words | 1791-1794 | encoded | ssc3-g-s60-s62.l4: `s 60(1) the retirement pension would be payable only by virtue of section 60` ; tests: ssc3-tests-g.l4 |
| 60(2), 60(2)(a), 60(2)(a)(i), 60(2)(a)(ii), 60(2)(b), 60(2) closing words | 1795-1800 | encoded | ssc3-g-s60-s62.l4: `s 60(2) the contribution conditions are taken to be satisfied for the entitlement of the widow, widower or surviving civil partner` ; tests: ssc3-tests-g.l4 |
| 60(3) | 1801 | encoded | ssc3-g-s60-s62.l4: `s 60(3) the benefit is one of those referred to in subsection (2)` ; tests: ssc3-tests-g.l4 |
| 60(3)(a) | 1802 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 60(3)(b), 60(3)(ba) | 1803-1804 | encoded | ssc3-g-s60-s62.l4: `s 60(3) the benefit is one of those referred to in subsection (2)` ; tests: ssc3-tests-g.l4 |
| 60(3)(bb) | 1805 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 60(3)(c), 60(3)(d) | 1806-1807 | encoded | ssc3-g-s60-s62.l4: `s 60(3) the benefit is one of those referred to in subsection (2)` ; tests: ssc3-tests-g.l4 |
| 60(4) | 1808 | encoded | ssc3-g-s60-s62.l4: `s 60(4) the weekly rate payable by virtue of regulations under section 60(1) in pounds` ; tests: ssc3-tests-g.l4 |
| 60(5) | 1809 | inert (reason 2) | what the rate prescribed by regulations under subsection (1) may vary with, which is for the regulations (reason 2); the prescribed rate arrives as an input at section 60(4) |
| 60(6) | 1810 | repealed or blank in this text | the text shows only a row of dots (repealed or omitted) |
| 60(7), 60(7)(a), 60(7)(b), 60(7) closing words | 1811-1814 | encoded | ssc3-g-s60-s62.l4: `s 60(7) the entitlement as respects the retirement pension is satisfied by a single payment` ; tests: ssc3-tests-g.l4 |
| 60(8) | 1815 | encoded | ssc3-g-s60-s62.l4: `s 60(8) subsection (2) has effect` ; tests: ssc3-tests-g.l4 |
| 60(9) | 1816 | encoded | ssc3-g-s60-s62.l4: `s 60(9) the pension counts as a Category A or Category B retirement pension in section 60` ; tests: ssc3-tests-g.l4 |
| 60A | 1817 | inert (reason 1) | the title of the section, not operative |
| 60A(1) | 1818 | encoded | ssc3-g-s60-s62.l4: `s 60A(1) subsection (2) applies` ; tests: ssc3-tests-g.l4 |
| 60A(2) | 1819 | fork F8 | ssc3-g-s60-s62.l4: `s 60A(2) the proportion of the benefit to which the person is entitled` ; tests: ssc3-tests-g.l4 ; see Fork register F8 |
| 60A(3) | 1820 | encoded | ssc3-g-s60-s62.l4: `s 60A(3) the year of the contributor's working life falls within this subsection` ; tests: ssc3-tests-g.l4 |
| 60A(4) | 1821 | encoded | ssc3-g-s60-s62.l4: `s 60A(4) the contributor` ; tests: ssc3-tests-g.l4 |
| 60A(5), 60A(5)(a), 60A(5)(a)(i), 60A(5)(a)(ii), 60A(5)(b), 60A(5) closing words | 1822-1827 | encoded | ssc3-g-s60-s62.l4: `s 60A(5) the condition in Schedule 3, Part I, paragraph 5A is taken to be satisfied for the entitlement of the widow, widower or surviving civil partner` ; tests: ssc3-tests-g.l4 |
| 60A(6), 60A(6)(a), 60A(6)(b), 60A(6) closing words | 1828-1831 | fork F7 | ssc3-g-s60-s62.l4: `s 60A(6) the contribution condition in Schedule 3, Part I, paragraph 5A is satisfied for the purposes of subsections (1) to (3)` ; tests: ssc3-tests-g.l4 ; see Fork register F7 |
| 61 | 1832 | inert (reason 1) | the title of the section, not operative |
| 61(1) | 1833 | encoded | ssc3-g-s60-s62.l4: `s 61(1) the increase under section 47(1) is excluded` ; tests: ssc3-tests-g.l4 |
| 61(2), 61(2)(a), 61(2)(b), 61(2) closing words | 1834-1837 | encoded | ssc3-g-s60-s62.l4: `s 61(2) the increase of the short-term incapacity benefit under section 47(1) or Part IV is excluded` ; tests: ssc3-tests-g.l4 |
| 61ZA | 1838 | inert (reason 1) | the title of the section, not operative |
| 61ZA(1), 61ZA(1)(a), 61ZA(1)(b) | 1839-1841 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZA(1) this section applies to the person` ; tests: ssc3-tests-a.l4 |
| 61ZA(2) | 1842 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZA(2) the relevant contribution conditions are taken to be satisfied` ; tests: ssc3-tests-a.l4 |
| 61ZA(3) | 1843 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZA(3) the weekly rate of the pension the person is entitled to because of section 61ZA` ; tests: ssc3-tests-a.l4 |
| 61ZA(4) | 1844 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "For units of additional pension, see section 14A." |
| 61ZB | 1845 | inert (reason 1) | the title of the section, not operative |
| 61ZB(1), 61ZB(1)(a), 61ZB(1)(b) | 1846-1848 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZB(1) this section applies to the person` ; tests: ssc3-tests-a.l4 |
| 61ZB(2) | 1849 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZB(2) the relevant contribution conditions are taken to be satisfied` ; tests: ssc3-tests-a.l4 |
| 61ZB(3) | 1850 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZB(3) the weekly rate of the pension the person is entitled to because of section 61ZB` ; tests: ssc3-tests-a.l4 |
| 61ZB(4) | 1851 | inert (reason 1) | a signpost to another provision, which creates no rule (reason 1): "For units of additional pension, see section 14A." |
| 61ZC | 1852 | inert (reason 1) | the title of the section, not operative |
| 61ZC(1), 61ZC(1)(a), 61ZC(1)(b) | 1853-1855 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZC(1) section 43 does not prevent entitlement to both pensions` ; tests: ssc3-tests-a.l4 |
| 61ZC(2), 61ZC(2)(a), 61ZC(2)(b) | 1856-1858 | fork F3 | ssc3-a0-s61za-s61zc.l4: `s 61ZC(2) section 43 does not prevent entitlement to both pensions` ; tests: ssc3-tests-a.l4 ; see Fork register F3 |
| 61ZC(3), 61ZC(3)(a) | 1859-1860 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZC(3)(a) section 43(2)(a) includes a Category A and a Category B retirement pension` ; tests: ssc3-tests-a.l4 |
| 61ZC(3)(b) | 1861 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZC(3)(b) the pension counts as a Category A retirement pension in sections 43(3)(a) and (aa), 51A and 52` ; tests: ssc3-tests-a.l4 |
| 61ZC(3)(c) | 1862 | encoded | ssc3-a0-s61za-s61zc.l4: `s 61ZC(3)(c) the pension counts as a Category B retirement pension in sections 43(3)(a) and 52` ; tests: ssc3-tests-a.l4 |
| 61A | 1863 | inert (reason 1) | the title of the section, not operative |
| 61A(1), 61A(1)(a), 61A(1)(b) | 1864-1866 | encoded | ssc3-g-s60-s62.l4: `s 61A(1) this section applies in the case of the individual` ; tests: ssc3-tests-g.l4 |
| 61A(2), 61A(2)(a), 61A(2)(b), 61A(2) closing words | 1867-1870 | encoded | ssc3-g-s60-s62.l4: `s 61A(2) the contributions are treated as properly paid, as if the individual had been an employed earner, for the additional pension` ; tests: ssc3-tests-g.l4 |
| 61A(3), 61A(3)(a), 61A(3)(b), 61A(3)(c), 61A(3)(ca), 61A(3)(d) | 1871-1876 | encoded | ssc3-g-s60-s62.l4: `s 61A(3) the additional pension is one to which subsection (2) refers` ; tests: ssc3-tests-g.l4 |
| 61A(4), 61A(4)(a), 61A(4)(b), 61A(4) closing words | 1877-1880 | inert (reason 2) | a power to make regulations affecting regulations under another Act (reason 2) |
| 61A(5) | 1881 | encoded | ssc3-g-s60-s62.l4: `s 61A(5) regulations under paragraph 8(1)(m) of Schedule 1 may require the amounts to be repaid` ; tests: ssc3-tests-g.l4 |
| 61A(6), 61A(6)(a), 61A(6)(b), 61A(6)(c), 61A(6) closing words | 1882-1886 | inert (reason 2) | a power to make regulations treating a person as an employed earner for the Pension Schemes Act 1993, which is not among the sources (reason 2) |
| heading@1887 | 1887 | inert (reason 1) | cross-heading of the Act, not operative |
| 62 | 1888 | inert (reason 1) | the title of the section, not operative |
| 62(1), 62(1)(a), 62(1)(aa), 62(1)(aa)(i), 62(1)(aa)(ii), 62(1) closing words, 62(1)(ab), 62(1)(ac), 62(1)(ad), 62(1)(ad)(i), 62(1)(ad)(ii), 62(1) closing words, 62(1)(ae), 62(1)(ae)(i), 62(1)(ae)(ii), 62(1) closing words, 62(1)(b), 62(1)(c) | 1889-1906 | inert (reason 2) | a power to make regulations amending sections 36 and 37 of the National Insurance Act 1965 (reason 2) |
| 62(2) | 1907 | inert (reason 2) | a saving for other powers to modify the 1965 Act's sections (reason 2) |
| 62(3) | 1908 | encoded | ssc3-g-s60-s62.l4: `s 62(3) the woman and her late wife are treated in the same way as a woman and her late husband for sections 36 and 37 of the National Insurance Act 1965` ; tests: ssc3-tests-g.l4 |
| 62(4), 62(4)(a), 62(4)(b) | 1909-1911 | encoded | ssc3-g-s60-s62.l4: `s 62(4) the case is a relevant gender change case` ; tests: ssc3-tests-g.l4 |

## Fork register (ssc3)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the readings, the one taken, the words that license each, and where the chosen reading sits in the code.
No fork was settled by a lawyer.
Where the text does not choose, the code answers `NOTHING` and the entry says so.

| Fork | Text | Reading A | Reading B | Taken | Where | Tests |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | ss 44(7)(a), 44(7)(b), 46(2)(b), 46(3)(b), through the keel's reading of s 173 | A person born on 29 February attains an age, in a year with no 29 February, at the commencement of 28 February | At the commencement of 1 March | Neither: `NOTHING` on 28 February of that year only, for a person born on 29 February | `s 44(7)(a) the tax year is a relevant year`, `s 44(7)(b) the final relevant year`, `s 46(2)(b) ...`, `s 46(3)(b) ...` pass the keel's `NOTHING` on (they take `s 173 the day the person attains the age of 16` as an input) | ssc3-tests-a.l4, ssc3-tests-c.l4 |
| F2 | s 43(4) | A notice dated the day the week commences governs that week | A notice has effect only for a week that commences after its date, so a notice dated the day the week commences has no effect for that week | B: the notice does not govern, so s 43(5) (the most favourable pension) applies | `s 43(4) the notices that specify a pension in the group and have effect for the week` | ssc3-tests-a.l4 |
| F3 | s 61ZC(2), with s 43(3)(a) and s 61ZC(3)(c) | s 43(1) still bars an ordinary Category B pension held beside a Category A pension and a Category B pension because of s 61ZB, because s 61ZC(2) lifts the bar only for "one Category B retirement pension because of section 61ZB" | s 43(3)(a) still lets the person choose among the Category B pensions, including the ordinary one, because s 61ZC(3)(c) removes only the s 61ZB pension from "Category B retirement pension" in s 43(3)(a) | `NOTHING`: the text does not say what becomes of the ordinary Category B pension | `s 61ZC(2) section 43 does not prevent entitlement to both pensions`, `s 43(1) the pensions the person is entitled to for the week` | ssc3-tests-a.l4 |
| F4 | ss 44B(2)(b) and 44B(6) | The deeming still produces the low earnings threshold, since subsection (6) only widens the aggregates that qualify | Subsection (6)(a) reads (2)(b) as an aggregate "greater than the QEF, but less than the low earnings threshold", which names a range and no amount | `NOTHING`: a range gives no amount | `s 44B(2) the deemed earnings factor in pounds`, `s 44B(6)(a) the aggregate is one that subsection (2)(b) refers to`, `s 44B(6)(b) Condition A is available` | ssc3-tests-b.l4, ssc3-cases-seat.l4 |
| F5 | s 44B(5) | "entitled to 52 earnings factor credits": at least 52 | Exactly 52 | A: at least 52 (a year can have 53 weeks, and a credit is given for each qualifying week; the words do not cap the number) | `s 44B(5) Condition C is satisfied` | ssc3-tests-b.l4 |
| F6 | ss 44(5A)(c), 45B(3), 55A(3), 55B(3), 48B(11), 48BB(10), 51(12) | Where the text says "multiplied by the relevant revaluation percentage" (ss 45B(3), 55A(3), 55B(3)) the amount is multiplied by P/100; where it says "increased by" a percentage (ss 44(5A)(c), 48B(11), 48BB(10), 51(12)) the amount is multiplied by 1 + P/100 | An order that specifies a percentage specifies an increase, so every one of them is 1 + P/100 | A: the words of each provision, as stated; P is asked as a percentage | `s 44(5A)(c)` (ssc3-a-s43-s44.l4:345), `s 45B(3)` (ssc3-c-s45-s46.l4:400), `s 55A(3)` and `s 55B(3)` (ssc3-f-s55a-s56.l4:15), `s 48B(11)` and `s 48BB(10)` (ssc3-d-s47-s48c.l4:744), `s 51(12)` (ssc3-e-s51-s55.l4:227) | ssc3-tests-a.l4, ssc3-tests-c.l4, ssc3-tests-d.l4, ssc3-tests-e.l4, ssc3-tests-f.l4 |
| F7 | s 60A(6) | "includes a reference to that condition ... as modified by virtue of paragraph 5A(4)": where paragraph 5A(4) modifies the condition, the modified condition is the one used | The unmodified condition is also a reference to "that condition" | A: the modified condition where 5A(4) modifies it; otherwise the unmodified one | `s 60A(6) the contribution condition in Schedule 3, Part I, paragraph 5A is satisfied for the purposes of subsections (1) to (3)` | ssc3-tests-g.l4, ssc3-cases-seat.l4 |
| F8 | s 60A(2) | The proportion is "a prescribed proportion" of the benefit for each qualifying year, so the person's proportion is the prescribed proportion times the number of such years | The prescribed proportion is the whole proportion, however many years qualify | A: per year, times the number of years | `s 60A(2) the proportion of the benefit to which the person is entitled` | ssc3-tests-g.l4, ssc3-cases-seat.l4 |

Words that license each reading, quoted from the text file:

- **F1.** src:4341 (s 173, outside this part): "the time at which a person attains a particular age expressed in years is the commencement of the relevant anniversary of the date of his birth."
  The text does not say what the anniversary of 29 February is in a year without one.
  The keel (`KEEL-NOTES.md`, F1) answers `NOTHING` on 28 February of that year only, because the two readings agree on every other day.
- **F2.** src:1242: "(4) If a person gives such a notice, the pension so specified shall be the one to which he is entitled in respect of any week commencing after the date of the notice." and src:1243: "(5) If no such notice is given, the person shall be entitled to whichever of the pensions is from time to time the most favourable to him".
  A week commencing on the date of the notice does not "commence after" it.
- **F3.** src:1858 (s 61ZC(2)): "(b) one Category B retirement pension because of section 61ZB (or, if there is more than one such Category B retirement pension, the most favourable of them)."
  The sentence lifts the bar for exactly one Category B pension because of s 61ZB, together with a Category A pension.
- **F4.** src:1335 and 1336 (s 44B(6)): "(a) subsection (2)(b) referred to an aggregate of earnings factors greater than the QEF, but less than the low earnings threshold, for the year (rather than to one equal to that threshold); and (b) Condition A in subsection (3) (and the reference to it in subsection (2)) were omitted."
  The text names a range and no amount.
- **F5.** src:1333 (s 44B(5)): "Condition C is that the pensioner is entitled to 52 earnings factor credits for that year under section 44C below."
- **F6.** src:1410 (s 45B(3)): "reduced by the appropriate weekly amount multiplied by the relevant revaluation percentage" and src:1573 (s 48B(11)): "increased by such percentage as equals the overall percentage by which ... that weekly rate would have increased".
  src:1264 (s 44(5A)(c)): "the adjusted amount of the surplus is the amount of that excess, as increased by the last order under section 148 of the Administration Act".
  The text does not say whether the percentage that an order specifies is a multiplier or an increase; the sources do not include section 148 or an order.
- **F7.** src:1831 (s 60A(6)): "includes a reference to that condition or those requirements as modified by virtue of paragraph 5A(4)."
- **F8.** src:1819 (s 60A(2)): "shall nevertheless be entitled to a prescribed proportion of that benefit in respect of each of the years of the contributor's working life that falls within subsection (3) below."

**Other readings that are not forks, because the text decides them.**

- **s 48(5) has two wordings in the text.** Src:1464 is the first wording (one conversion rule).
  Src:1465 to 1469 is the second, with paragraphs (a) to (d).
  The converter text shows both successively.
  Both are encoded (`s 48(5) first version: ...` and `s 48(5) the civil partnership is treated as having terminated`) and tested; the text does not say which wording is in force, so neither is dropped.
- **s 52(2)'s "full amount"** is the s 44(4) rate (184.90 as the text states it), not the lower rate.
  The text says "the full amount" of the basic pension; s 44(4)'s second sentence gives the lower rate only "so far as the sum is relevant for the purpose of calculating the lower rate of short-term incapacity benefit".

## Jural relations (ssc3)

One row per provision (or run of provisions of one kind) that creates a relation between two parties, naming the party who holds the right, privilege, power or immunity, the party who bears the correlative duty, no-right, liability or disability, the section, and the L4 rule.
The two parties in this Part are almost always the person (the pensioner or claimant) and the Secretary of State, who pays and decides.
The Hohfeld pairs are: right and duty; privilege and no-right; power and liability; immunity and disability.
Each relation is encoded once, as a decision function named for its section (the person's side is the question the seat asks).
A provision that creates no relation (a definition, a counting rule, a rate of calculation) is listed as `none`.
Rules that bind only an official are encoded in layer 1 for what they decide.

| Section | Holder | Bearer | Kind | L4 rule (file) |
| --- | --- | --- | --- | --- |
| 43(1) | Secretary of State | the person | immunity / disability (no second retirement pension for the same period) | `s 43(1) the pensions the person is entitled to for the week` (a) |
| 43(2) | the person | Secretary of State | right / duty (a Part II and a Part III pension together) | `s 43(2)(a)`, `s 43(2)(b)` (a) |
| 43(3), (4) | the person | Secretary of State | power / liability (notice specifying the pension; the Secretary of State is bound by it for later weeks) | `s 43(3) the person may give notice` (regulative rule), `s 43(4) ...` (a) |
| 43(5) | the person | Secretary of State | right / duty (the most favourable pension) | `s 43(5) the name of the most favourable pension` (a) |
| 43(6) | none | none | definition (a pension under s 55A or 55AA is not a retirement pension for s 43) | `s 43(6)` (a) |
| 44(1), 44(1A) | the person | Secretary of State | right / duty (Category A pension from pensionable age, for life); 44(1A) is none (which contribution test) | `s 44(1) the person is entitled ...`, `s 44(1) the day on which ...`, `s 44(1) the entitlement is running ...`, `s 44(1A)` (a) |
| 44(2) | Secretary of State | the person | privilege / no-right (no payment before the day the entitlement is regarded as commencing) | `s 44(2) ...` (a) |
| 44(3) | none | none | counting rule (basic and additional pension) | `s 44(3)(a)`, `s 44(3)(b)` (a) |
| 44(4) | the person | Secretary of State | right / duty (the weekly rate of the basic pension) | `s 44(4) the weekly rate of the basic pension in pounds` (a) |
| 44(5A) to 44(8) | none | none | counting rules (surplus, earnings factor, relevant year, applicable limit, orders) | `s 44(5A)(a)` to `s 44(8)` (a) |
| 44A, 44B, 44C | the person | Secretary of State | right / duty (to be treated as having an earnings factor, or an earnings factor credit, for a year or week); 44A(3) to (7), 44B(1), (6), (7), 44C(1), (4) to (7) are none (counting and definitions) | `s 44A(1)`, `s 44A(2)`, `s 44B(2)`, `s 44C(2)`, `s 44C(3)` (b) |
| 45(1), (2) | the person | Secretary of State | right / duty (the weekly rate of the additional pension) | `s 45(1)`, `s 45(2)` (c) |
| 45(3) to (8) | none | none | calculation rules (relevant percentage, N, X, weekly equivalent, units, rounding) | `s 45(3)` to `s 45(7)` (c) |
| 45AA | the person | Secretary of State | right / duty (qualifying earnings treated as paid, for credits of working families' tax credit or disabled person's tax credit); 45AA(2), (3), (5) none | `s 45AA(1)`, `s 45AA(4)` (c) |
| 45A | none | none | blank in this text (the text shows only a row of dots, src:1404; nothing was inferred about what stood there) | (coverage table) |
| 45B | Secretary of State | the person | power / liability (to reduce the additional pension on a pension debit) | `s 45B(1)`, `s 45B(2)`, `s 45B(4)`, `s 45B(6)` (c) |
| 46 | none | none | modifies the calculation of N and the percentage for the classes it names | `s 46(2)`, `s 46(3)`, `s 46(4)` (c) |
| 47(1) | the person | Secretary of State | right / duty (increase of the Category A pension by the age addition) | `s 47(1) the increase of the weekly rate in pounds` (d) |
| 47(2) to 47(6) | none | none | calculation rules (deduction, additional pension, age addition rate, weeks) | `s 47(2)` to `s 47(6)` (d) |
| 48(1) | the person | Secretary of State | right / duty (a former spouse's or civil partner's contributions treated as the person's own) | `s 48(1) ...` (d) |
| 48(2), 48(3) | Secretary of State | the person | immunity / disability (subsection (1) disapplied for early cases; only the last relevant relationship) | `s 48(2)`, `s 48(3)` (d) |
| 48(2A), 48(4) to 48(6) | none | none | definitions and rules of reading (regulations about time; relevant relationship; civil partnership or marriage not terminated by conversion) | `s 48(2A)`, `s 48(4)`, `s 48(5)`, `s 48(6)` (d) |
| 48A(1), 48A(3) | the person (married or in a civil partnership) | Secretary of State | right / duty (Category B pension on the spouse's or civil partner's contributions) | `s 48A(1)`, `s 48A(3)` (d) |
| 48A(2) | Secretary of State | the person | immunity / disability (no right for a man whose spouse, or a woman whose wife, was born before 6 April 1950) | `s 48A(2)` (d) |
| 48A(4) | the person | Secretary of State | right / duty (the rate) | `s 48A(4)` (d) |
| 48A(5) | Secretary of State | the person | privilege / no-right (the pension stops on death or ending of the marriage or partnership) | `s 48A(5)` (d) |
| 48A(6) to 48A(8) | none | none | definitions and signpost | `s 48A(6)` to `s 48A(7)` (d) |
| 48AA(1), 48AA(3) | the person (divorced or dissolved) | Secretary of State | right / duty (Category B pension on the former spouse's or civil partner's contributions) | `s 48AA(1)`, `s 48AA(3)` (d) |
| 48AA(2) | Secretary of State | the person | immunity / disability (as 48A(2)) | `s 48AA(2)` (d) |
| 48AA(4) to 48AA(9) | the person (4); none otherwise | Secretary of State (4) | right / duty (rate); definitions and signpost | `s 48AA(4)` to `s 48AA(8)` (d) |
| 48B(1), 48B(1A) | the person (widowed) | Secretary of State | right / duty (Category B pension on the late spouse's or civil partner's contributions) | `s 48B(1)`, `s 48B(1A)` (d) |
| 48B(1ZA) | Secretary of State | the person | immunity / disability | `s 48B(1ZA)` (d) |
| 48B(2) | the person | Secretary of State | right / duty (the rate: basic pension and half the additional pension) | `s 48B(2)` (d) |
| 48B(4), 48B(4A), 48B(5) to 48B(8) | the person | Secretary of State | right / duty (Category B pension of a woman whose husband, or man whose wife, died before pensionable age); 48B(5) to (8) are conditions | `s 48B(4)`, `s 48B(4A)`, `s 48B(5)` to `s 48B(8)` (d) |
| 48B(3), (3A), (9) to (11) | none | none | counting rules, signpost, percentage increase | `s 48B(3)`, `s 48B(3A)`, `s 48B(11)` (d) |
| 48BB(2), 48BB(4) | the person | Secretary of State | right / duty (Category B pension for a person who had a widowed parent's allowance or bereavement allowance) | `s 48BB(2)`, `s 48BB(4)` (d) |
| 48BB(5) to 48BB(10) | the person | Secretary of State | right / duty (the rate, after the reductions and the increase) | `s 48BB(5)` to `s 48BB(10)` (d) |
| 48C | none | none | when the entitlement runs; "half of" omitted for early deaths; who "the pensioner" means | `s 48C(1)` to `s 48C(4)` (d) |
| 49, 50, 53, 57, 58, 59 | none | none | blank in this text | (coverage table) |
| 51(1) | the person (widowed) | Secretary of State | right / duty (Category B pension) | `s 51(1)`, `s 51(4)` (e) |
| 51(2) | Secretary of State | the person | immunity / disability | `s 51(2)` (e) |
| 51(3) to 51(12) | the person (6, 7 rate); none otherwise | Secretary of State | right / duty (rate); contribution condition, earnings factor, when the entitlement runs | `s 51(3)` to `s 51(12)` (e) |
| 51ZA | the person | Secretary of State | immunity / disability (the bar in ss 48A(2)(b), 48AA(2)(b), 48B(1ZA), 51(2) does not apply to a woman whose spouse changed gender) | `s 51ZA(1)` to `s 51ZA(4)` (e) |
| 51A | the person | Secretary of State | right / duty (increase of the basic pension in the Category A pension for married people); 51A(3) disapplies | `s 51A(1)`, `s 51A(2)`, `s 51A(3)` (e) |
| 52 | the person | Secretary of State | right / duty (increase for a surviving spouse); 52(4) immunity of the Secretary of State | `s 52(1)` to `s 52(4)` (e) |
| 54 | Secretary of State | persons of the prescribed description | power / liability (regulations on election; inert, reason 2) | (coverage table) |
| 55 | the person | Secretary of State | right / duty (increase or lump sum where entitlement is deferred; Schedule 5 is not among the sources) | `s 55(1)`, `s 55(3)` (e) |
| 55A, 55AA | the person (with a pension credit) | Secretary of State | right / duty (shared additional pension); 55A(3) to (5) the rate | `s 55A(1)` to `s 55A(5)`, `s 55AA(1)` to `s 55AA(4)` (f) |
| 55B | Secretary of State | the person | power / liability (reduction of the shared additional pension on a pension debit) | `s 55B(1)` to `s 55B(8)` (f) |
| 55C | the person | Secretary of State | right / duty (increase or lump sum where the shared additional pension is deferred) | `s 55C(1)`, `s 55C(3)` (f) |
| 56(1) | the woman | Secretary of State | right / duty (child's special allowance) | `s 56(1) the woman is entitled ...`, `s 56(1) the weekly rate ...` (f) |
| 56(2), 56(3), 56(6) | Secretary of State | the woman | immunity / disability (payment barred on remarriage or cohabitation, unless a subsection (4) condition holds, and after 5 April 1987 except for those saved) | `s 56(2)`, `s 56(3)`, `s 56(6)`, `s 56(1) ... payable` (f) |
| 56(4), 56(5) | none | none | conditions (Part IX living with; contributions) | `s 56(4)`, `s 56(5)` (f) |
| 60(1), 60(2) | the person | Secretary of State | right / duty (benefit despite a contribution failure, by regulations; or the widow's, widower's or surviving civil partner's pension where the employed earner died of an industrial injury or disease on or after 11 April 1988) | `s 60(1)`, `s 60(2)`, `s 60(8)` (g) |
| 60(3), 60(9) | none | none | which benefits are meant | `s 60(3)`, `s 60(9)` (g) |
| 60(4) | the person | Secretary of State | right / duty (the weekly rate by regulations) | `s 60(4)` (g) |
| 60(5) | Secretary of State | persons concerned | power / liability (regulations on what the rate varies with; inert, reason 2) | (coverage table) |
| 60(7) | Secretary of State | the person | power / liability (to satisfy the entitlement by a single payment, if regulations so provide) | `s 60(7)` (g) |
| 60(8) | Secretary of State | the person | immunity / disability (subsection (2) only for deaths on or after 11 April 1988) | `s 60(8)` (g) |
| 60A(1) to 60A(3), 60A(5), 60A(6) | the person | Secretary of State | right / duty (a prescribed proportion of the benefit for each qualifying year; the paragraph 5A condition taken to be satisfied for a widow, widower or surviving civil partner) | `s 60A(1)` to `s 60A(6)` (g) |
| 61(1), 61(2) | Secretary of State | the person | immunity / disability (no increase of benefit under s 47(1) or Part IV for a failure to satisfy a contribution condition) | `s 61(1)`, `s 61(2)` (g) |
| 61A(1) to 61A(3), 61A(5) | the individual | Secretary of State | right / duty (contributions paid in error treated as properly paid, where regulations so provide) | `s 61A(1)` to `s 61A(5)` (g) |
| 61ZA, 61ZB | the person | Secretary of State | right / duty (the contribution conditions are taken to be satisfied where there are units of additional pension); 61ZA(3), 61ZB(3) the rate | `s 61ZA(1)` to `s 61ZB(3)` (a0) |
| 61ZC | the person | Secretary of State | immunity / disability (s 43(1) does not bar the combinations it names) | `s 61ZC(1)` to `s 61ZC(3)(c)` (a0) |
| 62(3), 62(4) | the woman | Secretary of State | right / duty (treated as a woman and her late husband for ss 36 and 37 of the National Insurance Act 1965) | `s 62(3)`, `s 62(4)` (g) |
| 62(1), 62(2) | Secretary of State | persons concerned | power / liability (regulations amending the 1965 Act; inert, reason 2) | (coverage table) |

File letters: (a) ssc3-a-s43-s44.l4, (a0) ssc3-a0-s61za-s61zc.l4, (b) ssc3-b-s44a-s44c.l4, (c) ssc3-c-s45-s46.l4, (d) ssc3-d-s47-s48c.l4, (e) ssc3-e-s51-s55.l4, (f) ssc3-f-s55a-s56.l4, (g) ssc3-g-s60-s62.l4.

## Marginal readings for a lawyer (ssc3)

These are the two readings the brief reserves for a lawyer, taken as the status quo and flagged here, not decided.
(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if".
That is an inference, because "if A then B" does not itself say "if not A then not B"; flat negatives count as the text saying no.
(b) A prohibition or grant limited by its own wording does not count as the text's no outside the limit; the answer there is NOTHING.

Four other readings are tagged in the code so that a branch resting on one can be found:

- **(a2)** "where", "in the case of", "in any case where" and "in cases where" are read like "if": a case outside them fails to a no (the same inference as (a), for a different introducing word).
- **(c)** A modifier outside its case returns the unmodified amount (the rows below name them).
  The text does not say what applies outside the case, but it does not say the amount is anything other than what the earlier subsection fixed.
- **(d)** In s 60(3), "are the following" is read as a closed list, so a benefit not named is not one the subsection refers to.
- **(b)** is also recorded at the seat: `s 46(4) ... EQUALS JUST TRUE` in the question for s 45(2).

Branches resting on a marginal reading: 111 (reading a: 32, a2: 24, b: 48, c: 6, d: 1); in addition 118 branches carry a `FALSE-kind` quotation of the words that say no.

Each row names the function, where the branch sits, the reading it rests on, the words relied on, and the other reading.
The table is generated by `work/notes_gen.py marginal` from the tags in the modules, so a branch cannot rest on a reading without appearing here.

| Function | File:line | Reading | The words relied on | The other reading |
| --- | --- | --- | --- | --- |
| `s 61ZA(1) this section applies to the person` | ssc3-a0-s61za-s61zc.l4:32 | (a) failed "if" = no | "This section applies to a person who has one or more units of additional pension if the person" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 61ZA(2) the relevant contribution conditions are taken to be satisfied` | ssc3-a0-s61za-s61zc.l4:48 | (b) limited by its own wording = NOTHING | the deeming is for "the purposes of the person's entitlement" in the s 61ZA(1) case only | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZA(3) the weekly rate of the pension the person is entitled to because of section 61ZA` | ssc3-a0-s61za-s61zc.l4:61 | (b) limited by its own wording = NOTHING | the sentence speaks only of "a person [who] is entitled to a Category A retirement pension because of this section" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZB(1) this section applies to the person` | ssc3-a0-s61za-s61zc.l4:77 | (a) failed "if" = no | "This section applies to a person whose spouse or civil partner died with one or more units of additional pension if the person" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 61ZB(2) the relevant contribution conditions are taken to be satisfied` | ssc3-a0-s61za-s61zc.l4:91 | (b) limited by its own wording = NOTHING | the deeming is for "the person's entitlement to that Category B retirement pension" in the s 61ZB(1) case only | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZB(3) the weekly rate of the pension the person is entitled to because of section 61ZB` | ssc3-a0-s61za-s61zc.l4:102 | (b) limited by its own wording = NOTHING | the sentence speaks only of "a person [who] is entitled to a Category B retirement pension because of this section" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZC(1) section 43 does not prevent entitlement to both pensions` | ssc3-a0-s61za-s61zc.l4:118 | (b) limited by its own wording = NOTHING | the lifting of the bar is for "a Category A retirement pension because of section 61ZA" together with "one Category B retirement pension" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZC(2) section 43 does not prevent entitlement to both pensions` | ssc3-a0-s61za-s61zc.l4:132 | (b) limited by its own wording = NOTHING | the lifting of the bar is for "a Category A retirement pension" together with "one Category B retirement pension because of section 61ZB" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61ZC(3)(a) section 43(2)(a) includes a Category A and a Category B retirement pension` | ssc3-a0-s61za-s61zc.l4:143 | (b) limited by its own wording = NOTHING | the inclusion is "in a case in which subsection (1) or (2) of this section applies" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44(1) the person is entitled to a Category A retirement pension` | ssc3-a-s43-s44.l4:225 | (a) failed "if" = no | "A person shall be entitled to a Category A retirement pension if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 44(1) the entitlement is running on the day` | ssc3-a-s43-s44.l4:256 | (b) limited by its own wording = NOTHING | "he shall become so entitled on the day on which he attains pensionable age" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44(1) the entitlement is running on the day` | ssc3-a-s43-s44.l4:261 | (b) limited by its own wording = NOTHING | the entitlement continues "throughout his life" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44(2) the Category A retirement pension is payable in respect of the day` | ssc3-a-s43-s44.l4:273 | (b) limited by its own wording = NOTHING | the bar is for "any period falling before the day"; from that day on the subsection says nothing, and when the pension is payable is left to the entitlement of s 44(1) an... | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44(3)(b) an additional pension is payable as part of the Category A retirement pension` | ssc3-a-s43-s44.l4:294 | (b) limited by its own wording = NOTHING | the additional pension is "payable where" there are surpluses or units; the text does not say it is not payable otherwise | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44(5A)(a) there is a surplus in the pensioner's earnings factor for the relevant year` | ssc3-a-s43-s44.l4:326 | (a) failed "if" = no | "there is a surplus ... if that factor exceeds the qualifying earnings factor for that year" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 44A(A1) subsections (1) to (4) apply to the year` | ssc3-b-s44a-s44c.l4:29 | (b) limited by its own wording = NOTHING | the subsection says to which years (1) to (4) apply, not that they apply to no other | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44A(1) the deemed earnings factor in pounds` | ssc3-b-s44a-s44c.l4:135 | (b) limited by its own wording = NOTHING | the pensioner is deemed to have a factor "if any of the conditions ... is satisfied"; no amount is named where the other factors already exceed the threshold | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44A(5) the low earnings threshold in pounds` | ssc3-b-s44a-s44c.l4:206 | (b) limited by its own wording = NOTHING | the threshold is stated "for the first appointed year and subsequent tax years" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44B(1) this section applies to the year` | ssc3-b-s44a-s44c.l4:270 | (b) limited by its own wording = NOTHING | the subsection says to which years the section applies; section 44A(A1) covers the earlier ones | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44B(2) the deemed earnings factor in pounds` | ssc3-b-s44a-s44c.l4:328 | (b) limited by its own wording = NOTHING | s 44B(6)(a) replaces "equal to" by "greater than the QEF, but less than the low earnings threshold", which names a range and no amount | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44B(2) the deemed earnings factor in pounds` | ssc3-b-s44a-s44c.l4:332 | (b) limited by its own wording = NOTHING | the pensioner is deemed to have the factor "if any of Conditions A to C ... is satisfied" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44C(1) this section applies to the year` | ssc3-b-s44a-s44c.l4:388 | (b) limited by its own wording = NOTHING | the subsection says to which years the section applies | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 44C(3) the pensioner is eligible for earnings factor enhancement in respect of the week` | ssc3-b-s44a-s44c.l4:417 | (a) failed "if" = no | "A pensioner is eligible for earnings factor enhancement in respect of a week if one or more of the following apply" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 44C(2) the earnings factor credit for the week in pounds` | ssc3-b-s44a-s44c.l4:451 | (b) limited by its own wording = NOTHING | the pensioner "is entitled to" a credit for a week that falls in a relevant year to which the section applies and in which the pensioner is eligible; the text does not sa... | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45(5) the year is one the regulations may direct to be disregarded` | ssc3-c-s45-s46.l4:118 | (a) failed "if" = no | "if it is a tax year after 5th April 1978 in which the pensioner" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 45(3) the relevant percentage` | ssc3-c-s45-s46.l4:136 | (b) limited by its own wording = NOTHING | paragraph (b) starts with the tax year 1999-2000; an earlier pensioner is under subsection (1) | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45(1) the weekly rate of the additional pension in pounds` | ssc3-c-s45-s46.l4:168 | (b) limited by its own wording = NOTHING | subsection (1) is "in any case where the pensioner attained pensionable age in a tax year before 6th April 1999"; later pensioners are under subsection (2) | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45(2) the weekly rate of the additional pension in pounds` | ssc3-c-s45-s46.l4:202 | (b) limited by its own wording = NOTHING | subsection (2) is "in any case where the pensioner attained pensionable age in a tax year after 5th April 1999"; earlier pensioners are under subsection (1) | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45AA(1) the qualifying earnings treated as paid in pounds` | ssc3-c-s45-s46.l4:274 | (b) limited by its own wording = NOTHING | the subsection operates "where ... working families' tax credit is paid ... or disabled person's tax credit is paid" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45AA(1) the qualifying earnings treated as paid in pounds` | ssc3-c-s45-s46.l4:277 | (b) limited by its own wording = NOTHING | subsection (4) says (1) "does not apply", so the earnings are not increased and this section gives no figure | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 45B(1) the weekly rate of the additional pension is reduced` | ssc3-c-s45-s46.l4:336 | (b) limited by its own wording = NOTHING | the reduction is "in any case where" both facts hold; the text does not say there is none otherwise | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 46(2) the substituted definition of N applies` | ssc3-c-s45-s46.l4:450 | (b) limited by its own wording = NOTHING | the substitution is for "a case where the deceased ... died under pensionable age" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 46(2) the substituted definition of N applies` | ssc3-c-s45-s46.l4:454 | (b) limited by its own wording = NOTHING | the substitution is for the listed calculations only | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 46(3) the substituted definition of N applies` | ssc3-c-s45-s46.l4:547 | (b) limited by its own wording = NOTHING | the substitution is for a calculation "by virtue of section 48BB" where the deceased "died under pensionable age" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 46(4) section 45 has effect subject to the additional modifications` | ssc3-c-s45-s46.l4:562 | (b) limited by its own wording = NOTHING | the modifications are "for the purpose of determining the additional pension ... by virtue of section 39C(1) ... where the deceased ... died under pensionable age" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 47(1) the increase of the weekly rate in pounds` | ssc3-d-s47-s48c.l4:88 | (a) failed "if" = no | "the weekly rate of a Category A retirement pension shall be increased if the pensioner was entitled to an age addition" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48(2) subsection (1) is disapplied for the person` | ssc3-d-s47-s48c.l4:178 | (a) failed "if" = no | "shall not apply ... if the termination of his relevant relationship also occurred before that date" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48(1) the former spouse's or civil partner's contributions may be treated as the person's own` | ssc3-d-s47-s48c.l4:215 | (a2) "where" / "in the case of" read like "if" | "Where a person who attained pensionable age before 6 April 2016 -- (a) has been in a relevant relationship, and (b) ... does not with his own contributions satisfy the c... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 48A(1) the married person is entitled to a Category B retirement pension by virtue of the spouse's contributions` | ssc3-d-s47-s48c.l4:326 | (a) failed "if" = no | "A married person is entitled to a Category B retirement pension by virtue of the contributions of his or her spouse if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48A(3) the civil partner is entitled to a Category B retirement pension by virtue of the contributions of the contributing civil partner` | ssc3-d-s47-s48c.l4:357 | (a) failed "if" = no | "A person who is a civil partner is entitled to a Category B retirement pension by virtue of the contributions of his or her civil partner (\"the contributing civil partn... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48A(5) the person ceases to be entitled to the Category B retirement pension under section 48A` | ssc3-d-s47-s48c.l4:385 | (a) failed "if" = no | "A person ceases to be entitled to a Category B retirement pension under this section if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48AA(1) the person whose marriage has been dissolved is entitled to a Category B retirement pension by virtue of the former spouse's contributions` | ssc3-d-s47-s48c.l4:481 | (a) failed "if" = no | "A person who has been in a marriage that has been dissolved is entitled to a Category B retirement pension by virtue of the contributions of his or her former spouse if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48AA(3) the person whose civil partnership has been dissolved is entitled to a Category B retirement pension by virtue of the former civil partner's contributions` | ssc3-d-s47-s48c.l4:514 | (a) failed "if" = no | "A person who has been in a civil partnership that has been dissolved is entitled to a Category B retirement pension by virtue of the contributions of his or her former c... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48AA(8) the date on which the marriage or civil partnership is treated as dissolved` | ssc3-d-s47-s48c.l4:557 | (b) limited by its own wording = NOTHING | the subsection speaks of "a voidable marriage or civil partnership which has been annulled" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 48B(1) the person whose spouse died is entitled to a Category B retirement pension by virtue of the spouse's contributions` | ssc3-d-s47-s48c.l4:634 | (a) failed "if" = no | "A person (\"the pensioner\") whose spouse died while they were married is entitled to a Category B retirement pension by virtue of the contributions of his or her spouse... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48B(1A) the person whose civil partner died is entitled to a Category B retirement pension by virtue of the civil partner's contributions` | ssc3-d-s47-s48c.l4:679 | (a) failed "if" = no | "A person (\"the pensioner\") whose civil partner died while they were civil partners of each other is entitled to a Category B retirement pension by virtue of the contri... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48B(11) the weekly rate of the additional pension after the increase in pounds` | ssc3-d-s47-s48c.l4:761 | (c) modifier outside its case returns the unmodified amount | unmodified, not a "no": subsection (11) increases the amount "in the case of" a pensioner whose spouse or civil partner (a) attained pensionable age on or after 6 April 2... | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 48B(8) subsections (4) to (7) are disapplied` | ssc3-d-s47-s48c.l4:769 | (a2) "where" / "in the case of" read like "if" | "Nothing in subsections (4) to (7) above applies in a case where the spouse dies on or after 9 April 2001" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 48B(4) the woman whose husband died before she attained pensionable age is entitled to a Category B retirement pension` | ssc3-d-s47-s48c.l4:799 | (a) failed "if" = no | "A woman (\"the pensioner\") whose husband died before she attained pensionable age is entitled to a Category B retirement pension by virtue of the contributions of her h... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48B(7) the man is entitled by virtue of section 38 on the assumption` | ssc3-d-s47-s48c.l4:818 | (b) limited by its own wording = NOTHING | the assumption is made "that a man is entitled" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 48B(4A) the man whose wife died before he attained pensionable age is entitled to a Category B retirement pension` | ssc3-d-s47-s48c.l4:833 | (a) failed "if" = no | "A man (\"the pensioner\") whose wife died before he attained pensionable age is entitled to a Category B retirement pension by virtue of the contributions of his wife if... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 48BB(2) the pensioner is entitled to a Category B retirement pension at the rate of the widowed parent's allowance` | ssc3-d-s47-s48c.l4:869 | (a2) "where" / "in the case of" read like "if" | "Subsection (2) below applies where a person (\"the pensioner\") who attained pensionable age before 6 April 2016 -- (a) was, immediately before attaining that age, entit... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 48BB(4) the pensioner is entitled to a Category B retirement pension by virtue of the contributions of the spouse or civil partner` | ssc3-d-s47-s48c.l4:902 | (a2) "where" / "in the case of" read like "if" | "Subsections (4) to (10) below apply where a person (\"the pensioner\") who attained pensionable age before 6 April 2016 -- (a) was ... either -- (i) entitled to a bereav... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 48C(1) the entitlement to a Category B retirement pension is running on the day` | ssc3-d-s47-s48c.l4:1011 | (b) limited by its own wording = NOTHING | entitlement "shall begin on the day on which the conditions of entitlement become satisfied" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 48C(1) the entitlement to a Category B retirement pension is running on the day` | ssc3-d-s47-s48c.l4:1015 | (b) limited by its own wording = NOTHING | it "shall continue for life" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 48C(2) section 47(1) applies also for the increase of the Category B retirement pension` | ssc3-d-s47-s48c.l4:1031 | (b) limited by its own wording = NOTHING | the extension is "in any case where" both facts hold | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 48C(3) the words "half of" are omitted from section 48B(2)(b)` | ssc3-d-s47-s48c.l4:1039 | (a2) "where" / "in the case of" read like "if" | "In the case of a pensioner whose spouse died on or before 5th October 2002 ... shall have effect with the omission" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 48C(4) the person to whom a reference to the pensioner is taken to refer` | ssc3-d-s47-s48c.l4:1052 | (b) limited by its own wording = NOTHING | the reading is "in the application of the provisions ... by virtue of sections ... 48B(2) or 48BB(5)" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 51ZA(4) section 51(1) does not confer a right on the woman` | ssc3-e-s51-s55.l4:79 | (a) failed "if" = no | "Section 51(1) does not confer a right ... on a woman if (a) ... and (b) ..." | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 51(1) the person whose spouse died is entitled to a Category B retirement pension` | ssc3-e-s51-s55.l4:99 | (a) failed "if" = no | "A person (\"the pensioner\") whose spouse died while they were married is entitled to a Category B retirement pension if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 51(4) the person whose civil partner died is entitled to a Category B retirement pension` | ssc3-e-s51-s55.l4:131 | (a) failed "if" = no | "A person (\"the pensioner\") whose civil partner died while they were civil partners of each other is entitled to a Category B retirement pension if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 51(6) the person to whom a reference to the pensioner is taken to refer` | ssc3-e-s51-s55.l4:156 | (b) limited by its own wording = NOTHING | the reading is made for "a person's Category B retirement pension under this section" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 51(6) the person to whom a reference to the pensioner is taken to refer` | ssc3-e-s51-s55.l4:160 | (c) modifier outside its case returns the unmodified amount | Outside those cases the amount stands as determined under (6) | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 51(7) the amount of additional pension after any halving in pounds` | ssc3-e-s51-s55.l4:179 | (c) modifier outside its case returns the unmodified amount | unmodified, not a "no": the halving is made "in the case of" (a), (b) or (c); outside them the amount stands | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 51(9) the entitlement to a Category B retirement pension under section 51 is running on the day` | ssc3-e-s51-s55.l4:218 | (b) limited by its own wording = NOTHING | a person "becomes entitled ... on the day on which the conditions of entitlement become satisfied" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 51(9) the entitlement to a Category B retirement pension under section 51 is running on the day` | ssc3-e-s51-s55.l4:222 | (b) limited by its own wording = NOTHING | the entitlement "continues throughout the person's life" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 51(12) the weekly rate of the additional pension after the increase in pounds` | ssc3-e-s51-s55.l4:244 | (c) modifier outside its case returns the unmodified amount | unmodified, not a "no": subsection (12) increases the amount "in the case of" a pensioner whose spouse or civil partner (a) attained pensionable age on or after 6 April 2... | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 51ZA(1) section 48A(2)(b) does not prevent the woman from being entitled` | ssc3-e-s51-s55.l4:262 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): outside "a case where (a) ... and (b) ..." the section does not lift the bar, and section 48A(2)(b) stands by its own terms | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51ZA(2) section 48AA(2)(b) does not prevent the woman from being entitled` | ssc3-e-s51-s55.l4:278 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): outside "a case where (a) ... and (b) ..." the section does not lift the bar, and section 48AA(2)(b) stands by its own terms | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51ZA(3) the case of a woman whose dead spouse changed gender applies` | ssc3-e-s51-s55.l4:297 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): outside "a case where (a) ... and (b) ..." the section does not lift the bar and does not change the reading, and section 48B(1ZA)(b) and (1ZB)(a)(ii) stand... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51A(1) this section has effect` | ssc3-e-s51-s55.l4:312 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both hold | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51A(3) this section does not apply` | ssc3-e-s51-s55.l4:322 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section does not apply in any case where both parties to the marriage attained pensionable age before 6th April 1979" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51A(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:345 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both entitlements arise | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 51A(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:347 | (a) failed "if" = no | "If by reason of a deficiency of contributions the basic pension ... falls short" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 51A(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:354 | (a) failed "if" = no | "falls short of the weekly rate" -- a basic pension that does not fall short is not increased | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 52(1) this section has effect` | ssc3-e-s51-s55.l4:370 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both entitlements arise | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 52(4) this section does not apply` | ssc3-e-s51-s55.l4:381 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section does not apply in any case where the death ... occurred before 6th April 1979 and the surviving spouse had attained pensionable age before tha... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 52(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:404 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both entitlements arise | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 52(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:406 | (a) failed "if" = no | "If by reason of a deficiency of contributions the basic pension ... falls short of the full amount" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 52(2) the increase of the basic pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:413 | (a) failed "if" = no | "falls short of the full amount" -- a basic pension that does not fall short is not increased | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 52(3) the increase of the additional pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:445 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both entitlements arise | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 52(3) the increase of the additional pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:452 | (a) failed "if" = no | "If the additional pension ... falls short of the maximum amount" -- a pension that does not fall short is not increased | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 52(3B) the further increase of the additional pension in the Category A retirement pension in pounds` | ssc3-e-s51-s55.l4:470 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "This section has effect where" both entitlements arise | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 55(1) Schedule 5 has effect` | ssc3-e-s51-s55.l4:511 | (b) limited by its own wording = NOTHING | Schedule 5 "has effect" where entitlement is deferred; the section does not say it has no effect otherwise | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 55A(1) the person is entitled to a shared additional pension under section 55A` | ssc3-f-s55a-s56.l4:55 | (a) failed "if" = no | "A person is entitled to a shared additional pension under this section if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 55A(2) the entitlement to the shared additional pension under section 55A is running on the day` | ssc3-f-s55a-s56.l4:74 | (b) limited by its own wording = NOTHING | the entitlement "shall continue throughout his life" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 55AA(1) the person is entitled to a shared additional pension under section 55AA` | ssc3-f-s55a-s56.l4:136 | (a) failed "if" = no | "A person is entitled to a shared additional pension under this section if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 55AA(2) the entitlement to the shared additional pension under section 55AA is running on the day` | ssc3-f-s55a-s56.l4:155 | (b) limited by its own wording = NOTHING | the entitlement "continues throughout his or her life" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 55B(3) the reduction of the weekly rate in pounds` | ssc3-f-s55a-s56.l4:249 | (c) modifier outside its case returns the unmodified amount | rate stands . The text sets no floor, and none is invented | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 55B(1) the weekly rate of the shared additional pension after the reduction in pounds` | ssc3-f-s55a-s56.l4:268 | (c) modifier outside its case returns the unmodified amount | unmodified, not a "no": the weekly rate "shall be reduced as follows in any case where" (a) and (b) hold; outside that case the rate stands | NOTHING here: outside the modifier's case the text is silent about the amount. |
| `s 55C(1) Schedule 5A has effect` | ssc3-f-s55a-s56.l4:285 | (b) limited by its own wording = NOTHING | Schedule 5A "has effect" where entitlement is deferred; the section does not say it has no effect otherwise | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 56(1) the woman is entitled to a child's special allowance` | ssc3-f-s55a-s56.l4:344 | (a) failed "if" = no | "a woman whose marriage has been terminated by divorce shall be entitled to a child's special allowance ... if" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 56(3) payment of the amount is barred by subsection (3)` | ssc3-f-s55a-s56.l4:430 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): the bar is made "Where, apart from this subsection, a person is entitled to receive" payment | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 56(6) payment of the child's special allowance for the day is barred by subsection (6)` | ssc3-f-s55a-s56.l4:447 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): the bar is made for "any period after 5th April 1987" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 60(3) the benefit is one of those referred to in subsection (2)` | ssc3-g-s60-s62.l4:57 | (d) "are the following" read as a closed list | in NOTES.md): "The benefits referred to in subsection (2) above are the following" -- read as a closed list | NOTHING for a benefit the list does not name: "are the following" does not close the list. |
| `s 60(2) the contribution conditions are taken to be satisfied for the entitlement of the widow, widower or surviving civil partner` | ssc3-g-s60-s62.l4:78 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "in any case where (a) an employed earner who is married or a civil partner dies as a result of ... and (b) the contribution conditions are not wholly satis... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 60(1) the retirement pension would be payable only by virtue of section 60` | ssc3-g-s60-s62.l4:113 | (a2) "where" / "in the case of" read like "if" | "in cases where the first contribution condition ... is satisfied and the second contribution condition so specified is not" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 60(1) the retirement pension would be payable only by virtue of section 60` | ssc3-g-s60-s62.l4:120 | (b) limited by its own wording = NOTHING | this function asks of a retirement pension, and the benefits section 60(1) lists are more than that | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 60(4) the weekly rate payable by virtue of regulations under section 60(1) in pounds` | ssc3-g-s60-s62.l4:151 | (b) limited by its own wording = NOTHING | the regulations "shall provide" for a rate "less than" the full rate; a prescribed rate that is not less is outside what the text contemplates | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 60(7) the entitlement as respects the retirement pension is satisfied by a single payment` | ssc3-g-s60-s62.l4:172 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "Regulations may provide that where (a) ... and (b) ..." | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 60A(1) subsection (2) applies` | ssc3-g-s60-s62.l4:213 | (a) failed "if" = no | "Subsection (2) below applies if the contribution condition ... is not satisfied in relation to a benefit to which that paragraph applies" | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 60A(3) the year of the contributor's working life falls within this subsection` | ssc3-g-s60-s62.l4:227 | (a) failed "if" = no | "A year of the contributor's working life falls within this subsection if it is a year in relation to which the requirements in paragraph 5A(2)(a) and (b) ... are satisfi... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 60A(2) the proportion of the benefit to which the person is entitled` | ssc3-g-s60-s62.l4:246 | (a) failed "if" = no | "A person who would have been entitled to the benefit had the condition been satisfied shall nevertheless be entitled" under (2), which applies only "if the contribution ... | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 60A(5) the condition in Schedule 3, Part I, paragraph 5A is taken to be satisfied for the entitlement of the widow, widower or surviving civil partner` | ssc3-g-s60-s62.l4:271 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "In any case where (a) an employed earner who is married or a civil partner dies on or after 6th April 2010 as a result of ... and (b) the contribution cond... | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 61(1) the increase under section 47(1) is excluded` | ssc3-g-s60-s62.l4:303 | (b) limited by its own wording = NOTHING | section 61(1) names a Category A or B retirement pension, a widowed mother's allowance and a widowed parent's allowance | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61(2) the increase of the short-term incapacity benefit under section 47(1) or Part IV is excluded` | ssc3-g-s60-s62.l4:319 | (a2) "where" / "in the case of" read like "if" | "the benefit shall not be increased under section 47(1) above or under Part IV below" where (a) and (b) both hold | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 61A(1) this section applies in the case of the individual` | ssc3-g-s60-s62.l4:338 | (a) failed "if" = no | "This section applies in the case of any individual if" (a) and (b) | NOTHING here: a failed "if" is silent, because "if A then B" does not say "if not A then not B". |
| `s 61A(3) the additional pension is one to which subsection (2) refers` | ssc3-g-s60-s62.l4:362 | (b) limited by its own wording = NOTHING | paragraph (b) names a Category B retirement pension "for widows, widowers or surviving civil partners (payable by virtue of section 48B or 48BB)" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 61A(2) the contributions are treated as properly paid, as if the individual had been an employed earner, for the additional pension` | ssc3-g-s60-s62.l4:379 | (a2) "where" / "in the case of" read like "if" | in NOTES.md): "Regulations may, where (a) this section applies ... and (b) the Inland Revenue are of the opinion that it is appropriate" | NOTHING here: "where" or "in the case of" only names the case the provision is about. |
| `s 61A(5) regulations under paragraph 8(1)(m) of Schedule 1 may require the amounts to be repaid` | ssc3-g-s60-s62.l4:395 | (b) limited by its own wording = NOTHING | the prohibition is made "Where such provision ... applies" | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |
| `s 62(3) the woman and her late wife are treated in the same way as a woman and her late husband for sections 36 and 37 of the National Insurance Act 1965` | ssc3-g-s60-s62.l4:422 | (b) limited by its own wording = NOTHING | the equal treatment is made "In relevant gender change cases"; sections 36 and 37 of the 1965 Act are not among the sources | The complement here: a limit in the provision's own wording is read as the text's answer outside the limit (JUST FALSE outside a grant; JUST TRUE outside a prohibition). |

### Reading a result: FALSE and NOTHING (ssc3)

In this part a result is of one of two kinds.
`JUST FALSE` (or a flat `FALSE` where the function returns a plain `BOOLEAN`) means the text says no in its own words: a definition that says "means", a condition introduced by "if", "only if", "unless", "so long as", "while", "until", "except", "save" or "provided that" that the facts fail, a closed "only" list, or a flat negative ("shall not be payable", "does not apply", "is not entitled").
For a pensioner that is: "the Act says you are not entitled" (for example, the contribution conditions are not satisfied; attained pensionable age on 6 April 2016, not before; the claim is not for a Category A pension).
`NOTHING` (or a named "not covered" case) means the Act does not answer on these facts.
For a pensioner that is: "this Act does not say" (for example, a day before the pension began, the day after death, a revalued reduction larger than the pension itself, two notices that both have effect, a rate or percentage that regulations set and that has not been given).
A caller must never turn `NOTHING` into `FALSE`: the layer-1 functions pass `NOTHING` on, and the seat answers `NOTHING` in the same cases.
The one place where this part reads `NOTHING` as "no" is the seat's use of s 46(4) in the question for s 45(2), which is recorded above and in "Seat (ssc3)".

## Seams (ssc3)

A seam is an answer that another part owes this one, or that this part owes another.
The core's definitions module is not in this sandbox, so every answer owed by another section arrives as a `GIVEN` input named for the section that answers it, in the form `s 30DD(6) the scheme is an occupational pension scheme`.
`work/seams_scan.py` lists them from the modules; the list below is that scan's output, sorted by the section that owes the answer.

**Asked of other parts** (inputs this part takes).

| Input | Owed by | Used in |
| --- | --- | --- |
| `sch 3 pt I para 5 / para 5A ... the contribution condition(s) ... are satisfied` (Category A; by the contributor; the first and second condition for a benefit) | Schedule 3 (S1 family) | ss 44(1), 48A, 48AA, 48B, 51, 60(1) |
| `sch 3 pt I the contribution conditions ... satisfied by the person's own contributions in respect of the tax year in which the relationship terminated` | Schedule 3 | s 48(1) |
| `sch 3 pt I para 6 the contribution condition for a child's special allowance is satisfied by the husband` | Schedule 3 | s 56(1) |
| `sch 4 pt I para 5 the weekly rate of a Category B retirement pension` and `sch 4 pt I para 6 the weekly rate of a child's special allowance` | Schedule 4 | ss 48A(4), 48AA(4), 56(1) |
| `sch 4A ... amount` and `sch 4B ... amount` | Schedules 4A and 4B | s 45(2) |
| `s 22(5) the person was credited with contributions or earnings by regulations` | s 22 (S11) | s 45(5) |
| `s 137(1) the two persons are a couple` | s 137 (S12) | s 45AA |
| `s 30DD(6) the scheme is an occupational pension scheme` and `... a personal pension scheme` | s 30DD (S13) | ss 44A, 44C |
| `s 23A(3) the person was a relevant carer in respect of the week` | s 23A (S14) | s 44C(3) |
| `s 39(1)` and `s 39C(1)` `the additional pension falls to be calculated under section 45 by virtue of this section` | ss 39, 39C (S15) | s 46 |
| `s 39A the weekly rate of the widowed parent's allowance` | s 39A | s 48BB(2) |
| `s 30B(7)` three inputs: entitled to an age addition on a day within the period; entitled on the last day before the period; the weekly rate of the age addition | s 30B(7) (S16, split) | s 47(1) |
| `s 38` three inputs: the pensioner is entitled, or treated as entitled, to a widow's pension; the pensioner, if a woman, would be entitled; the weekly rate of that pension | s 38 (S17) | s 48B(5) to (7) |
| `s 143(1)(b) the contributions are over and above those required` | s 143 (S18) | s 56(5) |
| `s 94(1) the personal injury is of a kind mentioned in section 94(1)` | s 94 (S19) | ss 60(2), 60A(5) |
| `s 108(1) the disease or injury is such as is mentioned in section 108(1)` (added, not in PLAN) | s 108 | ss 60(2), 60A(5) |
| `Part IX the beneficiary would be treated as having the child living with them` (added, not in PLAN) | Part IX | s 56(4)(a) |
| `s 173 the day the person attains the age of 16` and `s 173(a) the child is under 6`, `the pensioner was over 45`, `the pensioner was under 55` | s 173 (K2) | ss 44(7), 44A(2)(c), 45AA(5), 46, 48BB |
| the percentages and amounts that orders under ss 148, 148A and 150 of the Administration Act and regulations set | the Administration Act | ss 44(5A)(c), 44A(5), 44B(7), 45B(6), 48B(11), 48BB(10), 51(12), 55A(5), 55B(6) |

**Answered for other parts** (inputs other parts may take from this part).

- S3: `s 44(4) the weekly rate of the basic pension in pounds` (ssc3-a-s43-s44.l4).
- S10 and S37: `s 55(3) the retirement pension is deferred` and `s 55C(3) the shared additional pension is deferred`.
  A second name for S10, `s 55(3) the pension is deferred`, has the same inputs and body.
- S22: `s 60(1) the retirement pension would be payable only by virtue of section 60`, for the s 60(1) path alone, and `s 60 the retirement pension would be payable only by virtue of section 60 as a whole` (ss 60(1) and 60(2) together) for the wording of s 61(2) and of ssc4's s 87(2).
- S31 (shape mismatch): ssc8 wants one `Tax year` as "the relevant year".
  Section 44(7) defines a class of years, so this part gives `s 44(7)(a) the tax year is a relevant year` and `s 44(7)(b) the final relevant year`, and the other part has to choose between them.

**Seams the plan had wrong, or lacked.**

- **S16 is split.** PLAN names one input for s 30B(7); the text of s 47(1) needs two entitlement limbs (a day within the 8 weeks; the last day before them) and the rate, so there are three inputs.
- **S17's wording.** PLAN speaks of a "late spouse" for the s 38 inputs; in s 48B(5) to (7) the widow's pension in question is the pensioner's, so the inputs are named for the pensioner.
- **Added seams**: `s 108(1)` (ss 60(2), 60A(5)) and `Part IX` (s 56(4)(a)).
- **Percentages.** The percentages in ss 148 and 150 are asked as percentages (fork F6).

## What the text turns out to say (numbered findings)

Each finding is something the encoding made visible, with the words that show it.

1. **The text prints the rates.**
   Section 44(4) (src:1258) reads "The weekly rate of the basic pension shall be £184.90 except that, so far as the sum is relevant for the purpose of calculating the lower rate of short-term incapacity benefit under section 30B(3) above, it shall be £140.65."
   Section 44A(5) (src:1312) prints the low earnings threshold, £9,500, "(but subject to section 148A of the Administration Act)".
   Layer 1 carries those figures as constants and takes the altered figure as an input where the text allows one (s 44A(5), s 44B(7)(b)).
   A later version of the text with other figures changes `s 44(4)` and the s 44A(5) constant, and no other rule.
2. **Section 48(5) appears twice.**
   The text has two successive wordings of subsection (5): src:1464 (one conversion rule) and src:1465 to 1469 (the same rule with paragraphs (a) to (d), adding the Scottish conversions).
   Both are encoded; the text does not say which is in force (see the Fork register).
3. **Section 48BB(8) counts a fraction of a year as a year.**
   The reduction is "7 per cent. of what it would be apart from this subsection multiplied (a) by the number of years by which the pensioner's age at that time was less than 55 (any fraction of a year being counted as a year), or (b) by ten, if that number exceeds ten."
   The code uses 55 minus the pensioner's age in completed years, at most 10, which agrees with the text: a pensioner aged 54 years 6 months is counted as 1 year under 55, and 55 minus 54 is 1.
4. **The date 5 October 2002 is stated from both sides.**
   Section 48BB(7) (src:1587) halves the pension where the spouse or civil partner "dies after 5th October 2002"; section 48C(3) (src:1601) omits "half of" from s 48B(2)(b) where the spouse "died on or before 5th October 2002".
   A death on 5 October 2002 is not halved; one on 6 October 2002 is (`s 48C(3)` is tested on both days, and the seat cases do the same for s 48B(2)).
5. **"Full amount" in section 52(2) is defined by section 44(4).**
   The text says "full amount" means "the sum specified in section 44(4) above as the weekly rate of the basic pension in a Category A retirement pension".
   The code uses the £184.90 branch of `s 44(4)`, not the lower rate.
6. **No floor is invented.**
   Where a reduction of the additional pension (s 45B) or shared additional pension (s 55B) would exceed the rate, the text names no floor, so the answer is NOTHING; it is not zero.
7. **Deeming provisions hold only inside their case.**
   Sections 61ZA(2), 61ZB(2), 60(2) and 60A(5) each say that a contribution condition is "taken to be satisfied" in the case they describe.
   Outside the case they say nothing, so the answer is NOTHING (reading (b)), not "not satisfied".
8. **Section 46(4) answers yes or not covered, never no.**
   Its modifications apply "in a case where the deceased ... died under pensionable age" and the text does not say what becomes of the rest, so the function answers JUST TRUE inside the case and NOTHING outside it.
   The seat passes `EQUALS JUST TRUE` into s 45(2) (see Seat (ssc3)).
9. **Two dates for two purposes.**
   The contribution test of s 44(1A) turns on attaining pensionable age before 6 April 2010 (paragraph 5) or on or after it (paragraph 5A); the entitlement itself in s 44(1)(a) turns on attaining it before 6 April 2016.
   The same 6 April 2016 cut-off recurs in ss 48(1), 48A, 48AA, 48B, 48BB, 55A and 55AA.
   Section 60(8) has its own date (11 April 1988) for s 60(2).
   Section 60A(5) has a third (6 April 2010).
10. **Two notices.**
    Section 43(3) lets a person "from time to time give notice", and s 43(4) and (5) say what a notice or its absence does, but nothing says which of two notices that both have effect prevails; the answer is NOTHING.
11. **Section 60(7) is a power with a rate left to regulations.**
    "Regulations may provide that where" the pension consists only of the additional pension with no basic pension and it and any graduated retirement benefit "together amount to less than the prescribed rate", the entitlement is satisfied by "a single payment of the prescribed amount".
    Whether regulations so provide and the prescribed rate are inputs, and the code answers NOTHING where the prescribed rate is not given.
    The function answers whether the entitlement is satisfied by a single payment; it does not compute the prescribed amount of that payment.
12. **A seat expectation of mine was inverted, and the text corrected it.**
    The first draft of two seat cases for s 56(1) expected payment to be barred when a subsection (4) condition was satisfied.
    Section 56(3) says the amount "shall not be payable unless one of the conditions specified in subsection (4) below is satisfied", so a satisfied condition lifts the bar.
    The code was right and the expectations were wrong; they were corrected from the quoted words, and a third case (contributions of 9 against 10, no condition satisfied, not payable) was added.
    No other expectation in this part was changed to match the code.
13. **Section 52(3) refers to regulations that fix a maximum.**
    The additional pension is increased where it "falls short of the maximum amount specified in regulations"; `s 52(3)` takes that maximum as `MAYBE NUMBER` and answers NOTHING when it is not given.
14. **Dotted rows.**
    The converter prints a row of dots for text that is repealed or omitted (for example s 44(5), s 45A, s 54(3) and (4)); they are rows of reason 3 and nothing was inferred about what stood there.

## What the stable binary does not accept

The stable binary (1.6.98) governs; where a skill describes a construct it rejects, the binary wins.
Observed in this run:

- **`REFUSE` and `BECAUSE` do not exist.** "Not covered" is `NOTHING` or a named constructor, asserted.
- **`GIVEN` inside a `MEANS` body is not accepted.** A function that needs a parameter takes it in a top-level `GIVEN` before its definition.
- **A multi-word type constructor needs backticks** in an application: `` `Tax year` OF 2016 ``, not `Tax year OF 2016`.
- **A multi-line `LIST` argument must be wrapped in parentheses** where it is passed to a function.
- **Mixing `AND` and `OR` at the same indentation draws a linter warning.** `check.sh` counts error diagnostics and assertion lines and does not count warnings, but the brief requires none, so the code uses `BRANCH` or explicit parentheses; a separate scan of every file for `DiagnosticSeverity_Warning` is reported under "What check.sh prints".
- **A fixture that takes arguments needs a top-level `GIVEN`/`GIVETH`** before its `MEANS` (the `a person attaining pensionable age on` fixture of `ssc3-tests-a.l4` is written that way).
- **Regulative rules.** The one regulative rule in this part, `s 43(3) the person may give notice`, is run with `#TRACE` and gives `FULFILLED` on stable 1.6.98 and on main 1.6.108 (`work/final/ssc3-tests-a.l4.log` and `work/final/ssc3-tests-a.main.log`: the same four `FULFILLED` lines, no `BREACH`, in both).
  The same duty is encoded as a decision function (`s 43(3) the pension the person is entitled to out of the group`) and asserted.
- **`YMD`.** This part never defines `YMD` and writes `Date d m y`, so the multiple-definition failure the brief describes does not arise.

## What the text does not answer

Where a function answers `NOTHING`, one of these holds (the code marks each branch `NOTHING-kind (...)` with the reason; the counts are over the layer-1 modules):

Occurrences of the `NOTHING-kind` tag in the eight layer-1 modules: 114.

- 48 branches `NOTHING-kind (limited by its own wording)`
- 32 branches `NOTHING-kind (points outside the text)`
- 27 branches `NOTHING-kind (silent)`
- 5 branches `NOTHING-kind (undefined term)`
- 2 branches `NOTHING-kind (list not closed)`

**Ministerial substitutions that would change an answer.**
The figures and dates the text prints are constants in layer 1: the basic pension rates in s 44(4), the low earnings threshold in s 44A(5), the date 6 April 2016 in ss 44(1), 48(1), 48A, 48AA, 48B, 48BB, 55A, 55AA, the date 6 April 2010 in s 44(1A), the date 6 April 1999 in ss 45(1) and 45(2), the date 5 October 2002 in ss 48BB(7) and 48C(3), the date 11 April 1988 in s 60(8), the age 55 and the 7 per cent in s 48BB(8), and the 8 weeks of s 47(1) (s 47(6) lets regulations specify more, and that is an input).
A substitution of any of them changes the answers of the functions named, and of the seat questions that call them, and of nothing else.
The seat takes none of them as input, except where the layer-1 function does.

**Sources not among the inputs.**
Schedule 5 (the increase for deferment) and Schedule 5A, Schedules 3, 4, 4A and 4B, the Administration Act, the Pensions Act 1995 (pensionable age) and Part IX and the other sections named in "Seams (ssc3)" are not among the sources, so the provisions that depend on them take the borrowed fact as an input.
## What check.sh prints

Run on 2026-11-04 as `L4=$SP/bin/l4-stable-98 L4_MAIN=$SP/bin/l4-main-108 ./check.sh` in the deposit directory; the log is `work/final/check.log`.
Stable is 1.6.98 and main is 1.6.108.
The totals line reads 19 modules, 0 errors, 1185 assertions satisfied, 0 failed, 0 refused, and 19 of the 19 module rows end in `same` (the four main counts equal the stable counts).
It replaces the earlier runs of this part: 1021 assertions satisfied over 17 modules (before the seat was added) and 1152 over 19 modules (with 129 seat cases, before the last seat questions were added).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc3-a-s43-s44.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-a0-s61za-s61zc.l4                         0         0       0        0         0 |      0         0       0        0  same
ssc3-b-s44a-s44c.l4                            0         0       0        0         0 |      0         0       0        0  same
ssc3-c-s45-s46.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-cases-seat.l4                             0       161       0        0         0 |      0       161       0        0  same
ssc3-d-s47-s48c.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc3-e-s51-s55.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-f-s55a-s56.l4                             0         0       0        0         0 |      0         0       0        0  same
ssc3-g-s60-s62.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc3-helpers.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc3-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc3-tests-a.l4                                0       144       0        0         0 |      0       144       0        0  same
ssc3-tests-b.l4                                0       124       0        0         0 |      0       124       0        0  same
ssc3-tests-c.l4                                0       138       0        0         0 |      0       138       0        0  same
ssc3-tests-d.l4                                0       260       0        0         0 |      0       260       0        0  same
ssc3-tests-e.l4                                0       122       0        0         0 |      0       122       0        0  same
ssc3-tests-f.l4                                0       121       0        0         0 |      0       121       0        0  same
ssc3-tests-g.l4                                0       115       0        0         0 |      0       115       0        0  same
TOTAL (19 modules)                             0      1185       0        0           |      0      1185       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
check.sh exit 0
```

**The scan check.sh does not do.**
`check.sh` counts error diagnostics only (`DiagnosticSeverity_Error`, `check.sh` lines 193 and 227); a warning is not counted.
The brief requires no warning on any file, so `work/final-run.sh` ran `l4 run` on every `ssc3-*.l4` with the stable binary and counted both severities, with the number of `assertion satisfied` messages and of any other message.
The two `other-messages` of `ssc3-tests-a.l4` are the output of its one `#TRACE` directive (the line `FULFILLED` and the trace block `PARTY ... MAY ... HENCE FULFILLED`); `work/final/ssc3-tests-a.main.log` has the same four `FULFILLED` lines as the stable log and no `BREACH`.
The 1185 assertions are the 1024 of the seven test files plus the 161 of `ssc3-cases-seat.l4`; `ssc3-seat.l4` holds the questions and no assertion.
Its output, verbatim (`work/final/diag-summary.txt`):

```
ssc3-a-s43-s44.l4            errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-a0-s61za-s61zc.l4       errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-b-s44a-s44c.l4          errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-c-s45-s46.l4            errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-cases-seat.l4           errors 0 warnings 0 satisfied 161 other-messages 0
ssc3-d-s47-s48c.l4           errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-e-s51-s55.l4            errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-f-s55a-s56.l4           errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-g-s60-s62.l4            errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-helpers.l4              errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-seat.l4                 errors 0 warnings 0 satisfied 0 other-messages 0
ssc3-tests-a.l4              errors 0 warnings 0 satisfied 144 other-messages 2
ssc3-tests-b.l4              errors 0 warnings 0 satisfied 124 other-messages 0
ssc3-tests-c.l4              errors 0 warnings 0 satisfied 138 other-messages 0
ssc3-tests-d.l4              errors 0 warnings 0 satisfied 260 other-messages 0
ssc3-tests-e.l4              errors 0 warnings 0 satisfied 122 other-messages 0
ssc3-tests-f.l4              errors 0 warnings 0 satisfied 121 other-messages 0
ssc3-tests-g.l4              errors 0 warnings 0 satisfied 115 other-messages 0
diag scan done
```
