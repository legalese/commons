# Montana individual income tax (MCA Title 15, ch. 30, parts 21 and 23) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
A seat-neutral core (`mt-iit.l4`) states the rules in the Code's own terms; the seat layer (`mt-iit-seat.l4`) asks the taxpayer's questions, with `@export` and a `@desc` on every input, and restates no rule; the case file (`mt-iit-cases.l4`) tests the seat layer.
There is no REFUSE: a tax year the deposited text does not reach answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.** There was no earlier encoding of this subject.

## Edition

Montana Code Annotated 2025 (laws through the 2025 session), site marked "Updated August 2026", retrieved 2026-10-19 UTC, as deposited at:

- `../../registers/source-bundle/mca-15-30-part-21.txt` (rate and general provisions), and
- `../../registers/source-bundle/mca-15-30-part-23.txt` (credits).

Both versions of 15-30-2103 are deposited and both are encoded: the "(Temporary)" version, which terminates 31 December 2026 (sec. 7, Ch. 227, L. 2025), for tax year 2026, and the version "(Effective January 1, 2027)" for 2027 on.

No instrument is brought in. Figures the department sets each year are inputs: the indexed age-65 subtraction (15-30-2120(3)(g), (7)) and, from 2028, the indexed brackets (15-30-2103(3)). No department publication was deposited.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mt-iit.l4` (core), `mt-iit-seat.l4` (seat) | `mt-iit-cases.l4` | 41 written, 41 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Two `#TRACE`s check breaches (the stable `l4` cannot assert a breach); each has an `-- expect:` comment and was read: both end in `BREACH` by the right party.
Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**, resident, part-year or nonresident, and, for the elderly homeowner and renter credit, **the claimant** (a person 62 or over). The questions are the ones that person asks: "Am I a Montana resident?", "What is my Montana taxable income?", "How much tax do I owe?", "How much is my earned income credit?", "Can I get the elderly credit, and how much?", "By when must I claim it?".

The defaults of 2026-10-18:

- **The Code alone**, parts 21 and 23 as deposited. No instrument sets a number these parts need for 2026 or 2027; the indexed figures are inputs.
- **The actors the text names:** the taxpayer, the claimant, the department of revenue.
- **Judgments handed to others are answered conditionally:** the department's finding that title was taken primarily for the credit (15-30-2338(3)) is an input.
- **Definitions worked out from facts:** resident (15-30-2101(31)), Montana taxable income (15-30-2101(22), 15-30-2120), household income (15-30-2337(8)), rent-equivalent tax (15-30-2337(11)). **Borrowed terms asked as facts:** federal taxable income (IRC s 63), filing status (IRC ss 2, 7703, by 15-30-2113), the federal earned income credit (IRC s 32), net long-term capital gains (IRC s 1222), gross household income.
- **One case:** one return for one tax year (one claim period for the elderly credit).
- **Machinery out:** 15-30-2303 (review of credits), 15-30-2386 to 15-30-2393 (checkoffs and accounts), the department's rule-making powers.

## Regulative rules

Two `DEONTIC` rules, so the seat is a parameter:

1. 15-30-2112 — a taxpayer who changes from resident to nonresident, or back, during the year **shall file a return** (`the duty to file on a change of residence`). The due date is in part 26, which is not deposited, so the days to it are an input.
2. 15-30-2339(1) — the elderly credit claim **must be submitted** by the return due date, or by 15 April of the following year for a person not required to file (`the elderly credit claim deadline`); on a breach the reason names the department's extension for good cause (15-30-2339(3)) and the 3-year revision (15-30-2339(5)), which has its own date question.

## Read with the federal Internal Revenue Code encoding

Montana starts from federal taxable income (15-30-2101(22)), takes every status from the federal return (15-30-2113), and sets its earned income credit at 20% of the federal one (15-30-2318). Those federal figures are inputs here; they are encoded in `subjects/us/internal-revenue-code-of-1986/` (being encoded on 2026-10-24 by another session). The stable `l4` cannot IMPORT across folders, so the link is recorded here and in the module header only.

## Scope

**In:** 15-30-2101(12), (22), (31) and the definitions those use; 15-30-2103 (both versions), (1) and (2), and (3) for 2027; 15-30-2104(1)(a); 15-30-2112; 15-30-2113 (as the source of filing status); 15-30-2120(1), (2)(a), (2)(i), (2)(j), (3)(b), (3)(c) (as an amount), (3)(g), (6)(a); 15-30-2318; 15-30-2337 to 15-30-2341 (except (4) of 15-30-2338 and (4) of 15-30-2341).

**Taken as one input each:** the other additions in 15-30-2120(2) and the other subtractions in 15-30-2120(3)–(5) and (8)–(11) (family education savings, military retirement, volunteer firefighters, and the rest).

**Out:** 15-30-2104(2) (the elective sales tax for nonresident sellers), 15-30-2105 (lump-sum distributions), 15-30-2106 (nonresident compensation exclusion, an input to Montana source income), 15-30-2151 to 15-30-2154 (estates and trusts), 15-30-3704 (an exception to the capital gains rates; not deposited), 15-30-2302 (credit for taxes paid to other states), the business and contribution credits of part 23, and parts 25 (withholding) and 26 (returns, who must file, due dates), which are not deposited.

## What the Code turns out to say

1. **No subtraction for Social Security benefits.** Nothing in 15-30-2120(3) subtracts Social Security benefits, and 15-30-2101(21)(a)(xiv) counts them as Montana source income. Benefits taxable federally under IRC s 86 therefore stay in Montana taxable income. This confirms the inference recorded in `subjects/us/mt/README.md`. The encoding has no Social Security input for that reason.
2. **For tax year 2027 the brackets are the statutory figures exactly.** The version of 15-30-2103 effective 1 January 2027 has the department multiply the brackets by the "modified inflation factor", which is CPI-U for June of the previous tax year divided by CPI-U for June 2026 (15-30-2103(4)(a), 15-30-2101(12)). For tax year 2027 that is June 2026 over June 2026, which is 1. So $130,000 / $97,500 / $65,000 with a 5.4% top rate apply as written. From 2028 the published bracket is an input. Asserted (the 2027 head of household case).
3. **Tax year 2026 has fixed, unindexed brackets, and earlier years are not covered.** The temporary 15-30-2103 has no indexing subsection. It sets 4.7% to $95,000 / $71,250 / $47,500 and 5.65% above, and terminates on 31 December 2026. The deposited text shows no start date, because section histories were removed, so years before 2026 answer `not covered`. Asserted.
4. **15-30-2104 speaks only of nonresidents.** The ratio of Montana source income to total income is applied here to part-year residents too, because "Montana source income" (15-30-2101(21)) takes in everything received "while a resident". This is an interpretive choice, made by the encoder.
5. **15-30-2340(5) triggers on "household income" but its table is headed "Gross household income".** Household income is gross household income less $12,600 (15-30-2337(8)). Eligibility requires gross household income under $45,000 (15-30-2338(1)(d)), so on the opening words the subsection could only apply where household income is $35,000 or more, that is gross household income of $47,600 or more, and it would never apply. This encoding follows the table, by gross household income. Asserted (the $38,000 case: 30% of the credit).
6. **A claimant who owns part and rents part of a homestead loses the reduction twice.** 15-30-2340(3) subtracts "the deduction specified in subsection (4)" from the owned portion and again from the rented portion. The encoding follows the text, and floors each portion at zero. Asserted (the $20,000 case: 541 + 41 = 582).
7. **The state income tax add-back (15-30-2120(2)(j)).** It is read as the lesser of the state income tax itemized and the excess of the itemized total over the federal standard deduction. A taxpayer who itemized only slightly more than the standard deduction adds back only that excess. Asserted.
8. **The earned income tax credit is for residents only, and is fully refundable.** It is 20% of the federal credit (15-30-2318(1), (2), (4)), and a nonresident gets none. The 501(d) reduction percentage is encoded. Asserted.
9. **The elderly credit's figures are not indexed in the text.** These are the $12,600 deduction in household income, the $45,000 ceiling, the reduction table and the $1,150 cap. The credit is refundable even with no taxable income (15-30-2340(7)).
10. **ABLE contribution caps are not indexed, but the family education savings cap is.** ABLE is $3,000, or $6,000 joint (15-30-2120(6)). The family education savings cap of $4,500 / $9,000 is indexed from 2026 on (15-30-2120(11)), so it is part of the "other subtractions" input.

## Before relying on it

- Deposit part 26 (returns: who must file, due dates) and part 25 (withholding), and 15-30-3704.
- Deposit the department's published figures for the indexed age-65 subtraction and the family education savings cap for 2026.
- An independent test pass, and a check of findings 4 to 7 against department guidance.
