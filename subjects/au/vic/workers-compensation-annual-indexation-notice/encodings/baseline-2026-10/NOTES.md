# Victorian workers' compensation indexation notice, 1 July 2026: baseline encoding for the injured worker, and for the family of a worker who dies

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question the deposit cannot answer returns an explicit `not covered` value with its reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is the only Victorian encoding, because the notice is the only Victorian text deposited. The brief says to encode only what is deposited, and robots.txt on both Victorian legislation hosts has kept every Act and statutory rule in the Victorian sample undeposited (jurisdiction README, "Sourcing").

It is written in three layers:

- **The seat-neutral core.** `wcin-wirc-2013.l4` holds the Workplace Injury Rehabilitation and Compensation Act 2013 notice; `wcin-aca-1985.l4` holds the Accident Compensation Act 1985 notice. Each row that pays or limits a benefit to an individual is there, in the notice's own words, with both printed figures. So is the arithmetic a row states of itself: a ceiling "less 80% of worker's current weekly earnings", a lump sum "in the following shares ... Balance", a maximum "in equal shares". So is every maximum applied to a total (s 217, s 98C(7) and (8), s 221(4)), every condition a row states (the "more than 100km" of s 224(1)(d), (e) and s 99(1)(d); the severe injury and hospitalisation of s 224(1)(d)), and the reading of a "minimum" earnings figure. Two small shared modules carry the types and the shared arithmetic (`wcin-common.l4`) and the dates (`wcin-dates.l4`, built-in date functions only, no daydate).
- **`wcin-seat.l4`**, the injured worker's seat: 18 questions, each with `@export` and a `@desc` on every input, under `§§` headings.
- **`wcin-seat-family.l4`**, the seat of the dependants and close family members of a worker who dies: 14 questions.

Neither seat restates a rule: each finds the column in force on the day and the Act the claim is under, builds the core's inputs, and calls the core. (Until the fix of 24 October 2026 the seats applied four rules themselves; finding 16.) Their names differ, so one case file imports both for the mirror cases.

**No regulative rules.** The notice states no "must", "may" or deadline. It prints amounts; the duties that use them are in the Acts. So there is no `DEONTIC` here. Even "Contribution to be made by worker towards cost of supported accommodation" (2013 Act s 229(4), 1985 Act s 99(15)) is only a figure: the duty to contribute is the Act's.

No requirement ledger covers Victoria, so no ledger line is closed.

## Edition

**Victoria Government Gazette No. S 363, Tuesday 30 June 2026 (Special)**, 20 pages, deposited at `../../registers/source-bundle/GG2026S363.txt` (text sha256 `04c8fe556bca3ef38185cf933965d9a6526da59cac06fb470eec02fe5945499a`, checked 2026-10-24; line ranges in `GG2026S363.meta.json`).

Two of its three notices are encoded:

- the **Workplace Injury Rehabilitation and Compensation Act 2013** notice, Gazette pages 11-18, text lines 389-733, in `wcin-wirc-2013.l4`;
- the **Accident Compensation Act 1985** notice, Gazette pages 1-8, text lines 9-336, in `wcin-aca-1985.l4`.

The Workers Compensation Act 1958 notice (pages 9-10, lines 338-387) is out of scope.

**The period rule.** Each table has the columns "Rate before 1 July 2026" and "Rate from 1 July 2026". The notice says weekly payments "are varied on 1 July each year", and indexes the other amounts by the year's change in the CPI or AWE. So the "before" column is read as the figures for **1 July 2025 to 30 June 2026**, and the "from" column as the figures for **1 July 2026 to 30 June 2027**. Any other day answers `not covered`, asserted at both edges of both years. The next notice, for 1 July 2027, should be deposited beside this one.

**The parent Acts are not deposited.** The Acts decide every fact the notice's figures are used with, so those facts are inputs. Their sources, when deposited, will be:

- `subjects/au/vic/workplace-injury-rehabilitation-and-compensation-act-2013/` (Act 67/2013, version 054 indexed, not deposited);
- `subjects/au/vic/workplace-injury-rehabilitation-and-compensation-regulations-2024/` (indexed, not deposited);
- the Accident Compensation Act 1985 (not indexed).

The inputs these Acts would answer:

- which Act governs the claim, and the day of the claim (the notice prints rows for each Act and, for the 1985 Act, by claim date);
- which day counts for an amount: the day of injury, of the claim, of payment, or of the last indexation;
- the entitlement periods, and the percentages and week counts in each;
- current work capacity, a "serious injury", the approval of an application under s 165(1) or s 93CD(1);
- the uncapped weekly payment, the uncapped weekly pension and the formula lump sum (pre-injury average weekly earnings, the percentages, the formulas that combine a row's amounts);
- the impairment benefit rating, how it is described ("modified", "spinal"), and 'T' and 'P';
- who is a dependent partner, a dependent child, an orphan, another dependant, a close family member, a non-dependent family member;
- whether a worker is "severely injured";
- which of s 134AB and s 135A governs a 1985 Act damages claim;
- whether the no-disadvantage provision (s 221) applies, and the Schedule 4 total for several losses.

`encoding.json` has an empty `also_reads`, because none of these texts is deposited.

## Checks

| Modules | Case file | Assertions |
|---|---|---|
| `wcin-common.l4`, `wcin-dates.l4`, `wcin-wirc-2013.l4`, `wcin-aca-1985.l4`, `wcin-seat.l4` | `wcin-cases-worker.l4` | 229 written, 229 satisfied |
| the same, with `wcin-seat-family.l4` | `wcin-cases-family.l4` | 135 written, 135 satisfied (7 of them mirror cases) |

`l4 run` on all eight files: 0 errors, 0 warnings (2026-10-24, re-run after the fix in finding 16). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A probe file with a deliberately wrong assertion was run first, to confirm that failures are reported; it was not kept.

Every expected value was written by hand from the printed rows, with the line number and the arithmetic in the comment above the assertion.
Every encoded row is reached by at least one case, and the worker's case file asserts every Schedule 4 item.

A script (in the session scratchpad, not kept here) also compared the modules with the deposited text:

- Every pair of figures the modules print appears on a row of its own notice.
- Every pair of figures printed on a row of each notice appears in that notice's module, except on the out-of-scope employer, insurer and self-insurer rows. This check is by figures, not by row; the cases check the rows one by one.
- Every row's "from" figure is its "before" figure indexed by 2.350% (AWE) or 3.093% (CPI), to the nearest $10 (or $1 under $1,000), except the rows listed in finding 2. That covers all 249 lines of the two notices that print a pair of figures. The first version of these notes said the exceptions were only the unindexed rows of finding 2; they are not. Rows that are $10 off, and one row rounded to $100, are exceptions too. The check was re-run on 2026-10-24 and finding 2 now lists every exception.

## Seats

Both seats are individuals. There is no employer, insurer or official seat, because the notice puts no duty on any party.

- **The injured worker** (`wcin-seat.l4`), with a claim under the 2013 Act or, for an older claim, the 1985 Act. *What is the most I can be paid each week? What will my weekly payments be after the maximum? What minimum earnings keep my weekly payments, and do mine reach it? What deemed pre-injury earnings apply to me? What does the notice print for my impairment rating, and what is my lump sum after the maximum? What does it print for a further impairment, a loss of a foetus, an injury in s 90D? What is my total after the limits? What does the no-disadvantage table give, and what is my total after s 221(4)? What must I contribute to supported accommodation? What can provisional payments cover? What can my family be paid for counselling, or to be with me in hospital? What can I be paid for a dispute? What are my damages thresholds and maxima?*
- **The dependants and close family members of a worker who dies** (`wcin-seat-family.l4`): the dependent partner, the dependent child (or whoever asks for the child), other dependants, close and non-dependent family members. It also covers the family of a severely injured worker, for the hospital travel row. *How much is my share of the lump sum? What is the most the lump sum can be for partners and children, for children without a partner, for other dependants? What is set for grief or loss? What can I be reimbursed? What is the most my weekly pension can be, what does the notice print for its calculation, and what is my pension after the maximum? What can be paid for counselling, for travel to the funeral, for travel to the hospital? What does the notice set for damages for the death?*

**Mirror cases** ask the same facts from both seats, with answers that agree:

- family counselling (2013 Act s 224(1)(b));
- hospital travel (s 224(1)(d)): 250 km, 80 km, and a worker not severely injured.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Departed from, of necessity: the instrument is deposited and its Acts are not. Everything the Acts decide is an input (see Edition).
- **The actors the text names.** Followed: the worker, the dependent partner(s), the dependent child(ren), the orphan child(ren), partially dependent partners, other dependants, close family members, non-dependent family members, the family of a severely injured worker.
- **A judgment handed to someone else answered conditionally.** Followed: a serious injury, a severe injury, the approval of an application, the impairment rating and the dependency questions are inputs.
- **Definitions worked out, borrowed terms asked.** The notice defines nothing; every term is the Acts' and is asked.
- **One case is the text's natural unit.** Followed: one claim (one worker's injury, or one worker's death), on one day.
- **The text's own terms with a plain gloss.** Followed: the enumerations use the notice's own words, glossed in each `@desc`.
- **Operative rows in; machinery out.** Followed. The indexation arithmetic is out: the figures are encoded as printed, never recomputed, because the rounding rules are in the Acts. So are the employer, insurer and self-insurer rows.

## Scope

**In, part 1: the 2013 Act notice (lines 389-733).** Rows that pay or limit a benefit to an individual:

- weekly payments: ss 161(a)(ii), 161(b)(ii), 162(a)(ii), 162(b)(ii), 163(2)(b), 164(1)(c), 165(4)(a), 165(5)(b), 166(1)(d);
- pre-injury average weekly earnings: s 153(5) with Schedule 2 items 1 and 10, s 544 with Schedule 2 item 11;
- death: s 236(1)-(6), with the shares computed as the rows state them; ss 237(1), 237(2), 237AA(1), 237A(1), 240(9);
- dependants' weekly pensions: s 241(2)-(7), the first 13 weeks and after;
- provisional payments: s 243(1)(b);
- non-economic loss: ss 211(2)(b)-(f), 212(b)-(e), 213(1)(a)-(e), 214(1), 214A(a)-(e), 217(1), (2);
- the no-disadvantage table: s 221 with Schedule 4, all 48 items, and the s 221(4) total;
- medical and like services: s 224(1)(b), (d), (e), and the worker's contribution, s 229(4);
- dispute costs: s 301(3), (4);
- damages: s 340(a), (b), and s 366(2).

**In, part 2: the 1985 Act notice (lines 9-336).** The same kinds of rows for an older claim, each Act in its own module:

- death: ss 92A(4)-(9), (11A), 92AA;
- dependants' weekly pensions: s 92B(3)-(8), for claims before and on or after 5 April 2010;
- provisional payments: s 92D(1)(b);
- weekly payments: ss 93A, 93B, 93C, 93CA(1)(c), 93CD(4)(a), (5), 93CDA(1)(d), for claims before 12 November 1997, from 12 November 1997 to before 5 April 2010, and on or after 5 April 2010, with or without a serious injury;
- non-economic loss: s 98C(2)(e), (f), (3)(d), (e), (3B), (7), (8);
- medical and like services: s 99(1)(b), (d), (15);
- damages: ss 134AB(22), 135A(7), 135C(2);
- pre-injury average weekly earnings: s 100B with Schedule 1A item 11. The task listed "100B with Sch 1A"; the two s 5A(5) rows with Schedule 1A items 1 and 10 (lines 320-331) are the same kind of row as the 2013 Act's s 153(5) items 1 and 10, so they are in too.

**Out.**

- The Workers Compensation Act 1958 notice (lines 338-387).
- Every employer, insurer and self-insurer row:
  - 2013 Act: s 106(1) and (2), s 72(1)(c), s 225(2), Schedule 6 clause 1(1), Schedule 7 clause 3(1), s 388(5);
  - 1985 Act: ss 99(5), 125(1)(a)(iii), 125A(3)(c), 129B(7).
- The indexation arithmetic itself.
- Everything the Acts decide (see Edition).

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here and not in code.

- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`.
  - Part 3.14 (compensation preclusion and recovery) and s 17. Its questions `Is what I received compensation under s 17(2), (2A) and (2B)?`, `Is my payment a compensation affected payment (s 17(1))?`, `What is the compensation part of my lump sum, in dollars (s 17(3), (4A))?` and `By how much is my daily rate reduced for periodic compensation, in dollars a day (s 1173)?` apply to the amounts here:
    - the weekly payments and dependants' weekly pensions are periodic compensation;
    - the death lump sum, the non-economic loss lump sum and the damages are lump sums.
- **Income Tax Assessment Act 1997 (Cth)**, `subjects/au/income-tax-assessment-act-1997/encodings/baseline-2026-10/`. Weekly payments replace earnings and are income: `Is this ordinary income part of my assessable income (s 6-5)?`. Whether a lump sum here is income or capital is not answered by either encoding.
- **The parent Acts**, when deposited: `subjects/au/vic/workplace-injury-rehabilitation-and-compensation-act-2013/` and `subjects/au/vic/workplace-injury-rehabilitation-and-compensation-regulations-2024/` (see Edition). A seat layer over an encoding of the Act would take its figures from this encoding's tables.

## What the notice turns out to say

1. **The CPI percentage printed is not the one the printed index numbers give.** Both notices say Melbourne CPI went "from 98.0 to 101.0 which is an increase of 3.093%" (lines 25-27, 405-407). 101.0 / 98.0 is 1.030612: an increase of **3.061%**. The figures were indexed by 3.093%:
   - $759,510 x 1.03093 = $783,001.64, printed $783,000; at 3.061% it would be $782,760.
   - $20,000 becomes $20,620 (3.061% gives $20,612, so $20,610).
   - $45,300 becomes $46,700 (3.061% gives $46,687, so $46,690).

   The AWE figures agree with their percentage: $1,498.40 / $1,464.00 = 1.02350. The encoding uses the printed figures and recomputes none, so the answers are the Gazette's. Asserted through the printed figures.
2. **Some "from" figures are not the "before" figures indexed.** Every other row rises by 2.350% (AWE) or 3.093% (CPI), give or take rounding.
   - 2013 Act s 241(7)(b): **$976 to $1,500** (+53.7%; 976 x 1.0235 is about $999).
   - 1985 Act s 92B(8)(b): **$715 to $1,500** (claims before 5 April 2010) and **$976 to $1,500** (on or after).
   - 1985 Act ss 92B(3)(b)(ii), 92B(4)(b)(ii) and 92B(7)(b), the pre-5 April 2010 rows: **$2,150 to $3,000**, where indexation gives $2,200 (as the other pre-2010 rows show).

   The new figures are half or all of the $3,000 maximum. The old ones were about a third of $2,930 and $2,150. That looks like a change in the Acts or a correction, but the deposit does not say. Encoded as printed and asserted in both columns.

   Smaller rounding points, each encoded as printed:
   - s 340(a)(ii) and s 134AB(22)(a)(ii) print $1,798,500. That is $1,744,530 x 1.03093 = $1,798,488, rounded to the nearest $100 where other rows round to $10.
   - **$10 above the indexed figure (CPI).** The 2013 Act's Schedule 4 items at $374,230 print $385,810. They are total loss of the sight of both eyes, of an only eye, both hands, both feet, a hand and a foot, quadriplegia, paraplegia and total impairment of the spine (lines 610-614, 670-672). The s 221(4) maximum total prints the same (line 673). $374,230 x 1.03093 = $385,804.93, which is $385,800 to the nearest $10.
   - **$10 below the indexed figure (AWE).** s 366(2) and s 135C(2), death of a person, print $1,267,530 to $1,297,310 (lines 706, 319). $1,267,530 x 1.0235 = $1,297,316.96, which is $1,297,320 to the nearest $10.
   - Outside the scope, the employer's s 106(1) and (2) row prints $2,967,330 to $3,059,120 (line 718). x 1.03093 gives $3,059,109.52, so $3,059,110.

   These may come from indexing unrounded amounts, but the deposit does not say. Each is asserted through its printed figure (the cases assert $385,810, $374,230, $1,297,310 and $1,267,530).
3. **Rows with several amounts carry no labels.** Lines 534-601 print the amounts one under another:
   - two amounts: ss 211(2)(b)-(e)(i), 212(b)-(d)(i), 213(1)(a) and (d), 214A(a) and (d);
   - three amounts: 213(1)(c) and 214A(c);
   - one amount: 213(1)(b) and (e), 214A(b) and (e).

   The amounts are not labelled. The deposit's conversion note calls them a base amount and a per-percentage-point amount, but the notice does not.
   - **Same figures, different rows.** ss 211(2)(b)(i) (a modified whole person impairment) and (b)(ii) (a modified spinal impairment) print the same pair, $16,430 and $14,000. ss 211(2)(c)(i), (c)(ii)(A) and (c)(ii)(B) print the same pair, $26,530 and $3,980, and (A) and (B) print identical words.
   - **Undefined terms.** 'T' and 'P' (ss 213, 214A) are not defined in the notice.
   - **A band of one point.** s 212(b) covers a psychiatric impairment that "is 30%", a single point.

   The formula that combines the amounts is in the Act. So the encoding prints the amounts, and gives a lump sum only where the notice itself settles it:
   - above 80%, the single amount printed;
   - above 70% and not above 80%, the formula amount (an input) or the printed maximum, whichever is less.

   Every other band answers `not covered`. READING: where a modified or spinal rating also fits a general row, the specific row (b) or (c)(ii) is taken. Asserted.

   READING, added 24 October 2026: a "modified spinal impairment" is "a spinal impairment" in s 211(2)(c)(ii) (lines 542-547), because the notice's words describe a spinal impairment that has been modified. So a modified spinal impairment rated from 11% to less than 30% takes (c)(ii), and one rated exactly 30% takes (c)(i). Below 11% it takes (b)(ii) first, as before. A modified whole person impairment is not spinal and takes (c)(i). The amounts are the same in (c)(i) and (c)(ii) ($26,530 and $3,980), so only the provision returned changes (finding 16). Asserted at 11%, 15% and 30%.
4. **Weekly payments move on the worker's anniversary, not on 1 July.** The 2013 Act notice says weekly payments "are varied on 1 July each year" and "are indexed on the anniversary of the entitlement to weekly payments" (lines 397-402). The 1985 Act notice adds "or on the deemed anniversary date which for the purposes of this section is 1 July" (lines 21-22). So whether the 1 July 2026 maximum applies to a worker's payment depends on a date the notice does not give.
   - The weekly payment questions ask for **the day the worker's weekly payments were last indexed**, and use the column in force on that day. READING: between anniversaries the payment, and its maximum, stay as they were.
   - A worker last indexed on 1 September 2025 still has the $2,930 maximum in August 2026. Asserted.
   - **A worker not yet indexed** gives the day the entitlement to weekly payments began. This is a worker whose entitlement began less than a year ago and, under the 1985 Act, before any deemed 1 July anniversary; the 2013 Act notice prints no deemed anniversary. Under the same reading, the payment and its maximum stay as they were when the entitlement began, until the first indexation. Both `@desc`s say so (added 24 October 2026, finding 16). A worker whose entitlement began on 1 March 2026 has the $2,930 maximum in August 2026. Asserted.
   - If the Act applies the new maximum to every payment from 1 July, the input should be the payment day instead, and that worker's answer would be $3,000.
5. **Misprints.** None changes a figure; not asserted.
   - The 2013 Act notice's heading has "WORKPLACE INJURY REHABILIATION AND COMPENSATION ACT 2013" (line 393).
   - Both notices have "dependent partner of partners" (lines 32, 417, 421) for "partner or partners".
   - s 162(a)(ii) reads "Maximum weekly payment for claims" (line 505), a leftover "for claims" in a row with no claim dates.
   - "dependants" and "dependents" alternate (lines 71, 455, 450).
6. **The two notices split the death lump sum at different numbers of children.**
   - The 2013 Act notice has "more than one dependent child but not more than 5" and "more than 5" (s 236(4), (5)).
   - The 1985 Act notice has "not more than four" and "more than four" (s 92A(7), (8)).
   - The dependants' pension rows of both notices use four.

   A partner with five children gets $587,150 and each child $39,170 under the 2013 Act. Under the 1985 Act the partner gets $587,270 and each child $39,146 ($195,730 / 5). Each is encoded as printed. Asserted.
7. **"After" where every other row says "on or after".** The second s 92B(3)(b)(iii) row is "for claims made after 5 April 2010" (line 117). Read literally, a claim made on 5 April 2010 is in neither row. Both rows print the same figures ($1,470 and $1,500), so it is read as "on or after", which changes no answer. Asserted ($1,500).
8. **The 1985 Act notice prints non-economic loss only above 70%.**
   - It has s 98C(2)(e), (f), (3)(d), (e), and the single rows s 98C(3B), (7), (8). It has no row for a lower rating.
   - It prints the heading "Permanent Impairment – Calculation of Amounts of Non-economic Loss for Further Injury Industrial Deafness" (lines 274-276) with no row under it.

   A 1985 Act rating of 70% or less answers `not covered`. Asserted.
9. **s 163(2)(b) deducts earnings from a worker with no work capacity.** It is printed under "Where worker has no current work capacity" (line 511) but reads "Maximum weekly payment – less 80% of worker's current weekly earnings". The 1985 Act rows for the same stage (s 93C(2)(c), (d)) deduct nothing. Encoded as printed: $3,000 less 80% of $250 is $2,800. Asserted.
10. **Gaps in the weekly payment rows.** No maximum is printed for:
    - a 1985 Act claim made before 12 November 1997, with a serious injury and a current work capacity, in the second entitlement period;
    - a worker after the second entitlement period with a current work capacity and no approved application, under either Act;
    - the continuation for an incapacity arising from surgery (s 164, s 93CA), which has only a minimum earnings row.

    The first two answer `not covered`. Asserted. The third is asked only as its minimum.
11. **Rows that give no unit or recipient.**
    - The supported accommodation contribution ($46) and the dispute costs ($79 for transport, $546 for loss of income) say neither per day nor per attendance.
    - The provisional payments maximum ($11,670, s 243(1)(b), s 92D(1)(b)) is printed after the death rows in both notices, and the notice does not say on whose claim it is paid. It is asked in the worker's seat.
    - The damages rows print "Threshold" and "Maximum". What a threshold does (bars damages at or under it, or is deducted) is the Act's.

    The figures are encoded; nothing is computed from them except a maximum.
12. **Two maxima for other dependants, with no stated relation.**
    - s 237(2), "Maximum lump sum for any other dependants if no dependent partner or dependent child or partially dependent partner": $783,000.
    - s 237AA(1), "Maximum lump sum for other dependents", with no condition: $20,620.
    - The 1985 Act's s 92A(9) and s 92A(8C) are the same pair.

    The notice does not say which applies when. Each is its own question; the encoding does not choose. Asserted.
13. **Weekly pension rows of three kinds.** The rows are "Maximum weekly pension ...", "Weekly pension calculation ..." and "Weekly pension for ... where there are more than four dependent children".
    - The **maximum** rows are applied as maxima, divided equally where the row says "in equal shares".
    - The **other two kinds** print an amount for a calculation the Act makes. The 1985 Act rows add "and overall cap applies", a condition only the Act can settle. They are answered as printed figures, with the row's own words, not as pensions.
    - **Equal shares.** The 2013 Act's s 241(7)(b) has no "in equal shares", where the 1985 Act's s 92B(8)(b) has it. Encoded literally: shared under the 1985 Act, not under the 2013 Act.
    - **Orphans.** s 241(6)(b) and (7)(b) speak of "each dependent child" and "dependent children" without excluding orphans, and are read literally.

    Asserted.
14. **The lump sum split names orphans only where there is no partner.** s 236(2) (and s 92A(5)) splits the lump sum equally among "an orphan child or orphan children". s 236(6) (and s 92A(8A)) gives only a "Maximum lump sum for dependent children if no dependent partner". So children with no dependent partner who are not orphans get a maximum and no stated share: `not covered`. Asserted.
15. **Outside the scope, a stale date.** The Workers Compensation Act 1958 notice says its rates are payable "on and from 1 July 2005" (line 353), in the notice for 1 July 2026. Not encoded.
16. **Corrections after an independent verification (24 October 2026).** A verifier reported five issues. Each was checked against the deposited text, and all five held. None changed a figure, and every earlier assertion still holds.
    - **The seats applied rules.** `wcin-seat.l4` applied the s 217 and s 98C(7), (8) maxima and the s 221(4) maximum with its own `min`. The core's s 221(4) function was left unused. The seat also read "minimum" as "at least" itself. `wcin-seat-family.l4` decided the "more than 100km" of s 224(1)(e) and s 99(1)(d) itself. Each is now in the core:
      - `the 2013 Act total non-economic loss after the s 217 maximum for` and `the 1985 Act total non-economic loss after the s 98C(7) or (8) maximum for`;
      - the existing `the 2013 Act Schedule 4 total after the s 221(4) maximum of`;
      - `the 2013 Act s 224(1)(e) maximum for a burial or cremation at` and `the 1985 Act s 99(1)(d) maximum for a burial or cremation at`;
      - the "minimum" reading, `weekly earnings of … reach the minimum of …`, in `wcin-common.l4`.

      The seats now only choose the column and the Act. New cases assert the day edges of the rewritten questions and 101 km.
    - **The recorded check result was wrong.** The Checks section said every "from" figure was its "before" figure indexed, except the unindexed rows. The $10 differences on the $374,230 rows and on s 366(2) and s 135C(2) were missed. Finding 2 now lists them.
    - **`NOT` without brackets.** Three `IF NOT …` (2013 Act s 163(2)(b) and s 224(1)(d) rules, 1985 Act after the second entitlement period) are now `IF (NOT …)`. They parsed correctly before.
    - **A worker not yet indexed** could not answer the weekly payment questions' day input. Both `@desc`s now say to give the day the entitlement began (finding 4). Asserted.
    - **A modified spinal impairment from 11% to less than 30%** was sent to s 211(2)(c)(i), because only `a spinal impairment` counted as spinal. It now takes (c)(ii), under the reading in finding 3. The amounts were and are the same. Asserted.

**Readings**, none of them stated by the notice:

- the period rule;
- the last-indexation day for weekly payments, and the day the entitlement began for a worker not yet indexed (finding 4);
- specific impairment rows first, and a modified spinal impairment counted as a spinal impairment (finding 3);
- a "minimum" is reached by earnings of at least the figure;
- a ceiling that "less" would take below nothing is 0;
- "more than 100km" is strictly more than 100 km;
- "on or after 5 April 2010" for s 92B(3)(b)(iii) (finding 7).

## Before relying on it

- **Deposit the parent Acts**: the Workplace Injury Rehabilitation and Compensation Act 2013, its Regulations 2024, and the Accident Compensation Act 1985 (saved by hand, since robots.txt bars fetching them). Then encode the formulas this encoding takes as inputs:
  - pre-injury average weekly earnings;
  - the entitlement-period percentages and the step-downs;
  - the non-economic loss formulas that combine a row's amounts;
  - the pension calculations and the "overall cap";
  - the death lump sum for partially dependent partners and other dependants.
- **Check findings 1 and 2 against the published Gazette PDF** and against WorkSafe Victoria's published benefit rates, and ask whether a 2025-26 amendment explains finding 2.
- Settle the readings above against the Acts, above all finding 4 (which maximum applies between anniversaries) and finding 12 (s 237(2) against s 237AA(1)).
- **Deposit the next notice** (Gazette, about 30 June 2027) beside this one, and add its two columns.
- An independent test pass, and a human gate.

## Licence

The deposited Gazette text is not openly licensed. It is deposited and quoted under **the owner's ruling of 24 October 2026** (Michael: "On NT, Vic and SA, yes please go ahead."), recorded in `SOURCE-LICENSE.md` here and in the subject folder.

- **Government Printer's notice:** Victoria Government Gazette, published by IVE Group Limited with the authority of the Government Printer for the State of Victoria. (c) State of Victoria 2026. "This publication is copyright. No part may be reproduced by any process except in accordance with the provisions of the Copyright Act."
- **Unofficial version:** the quotations in this encoding come from a plain-text conversion by Legalese Commons of the Gazette's PDF, not the published Gazette. Check the published Gazette before relying on them.

Every module and case file carries both in its header. The L4 is Apache-2.0; the quoted text keeps the State of Victoria's copyright.
