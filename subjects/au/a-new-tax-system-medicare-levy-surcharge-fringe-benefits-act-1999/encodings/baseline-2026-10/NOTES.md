# A New Tax System (Medicare Levy Surcharge—Fringe Benefits) Act 1999 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `mlsfb-surcharge.l4`, holds the rules and the exported questions (each
with `@export` and `@desc`). One case file, `mlsfb-cases-surcharge.l4`, is built by
the scratchpad generator
`gen_a-new-tax-system-medicare-levy-surcharge-fringe-benefits-act-1999_baseline.py`.
Its expected values were written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

A New Tax System (Medicare Levy Surcharge—Fringe Benefits) Act 1999, Compilation
No. 42, compilation date 1 July 2026, includes amendments up to Act No. 58, 2026
(Register id C2026C00288), as deposited at
`../../registers/source-bundle/C2004A00412.txt`.

No instrument sets the Act's numbers. Its one figure, $28,011 (ss 15(1)(c),
16(2)(c)), is in its own text.

Also used: the Private Health Insurance Act 2007, ss 22-30, 22-35, 22-40 and 45-1,
as deposited at
`../../../private-health-insurance-act-2007/registers/source-bundle/C2007A00031.txt`.
Sections 3(1) and 6 of this Act borrow their thresholds and tiers from there, and
s 4 borrows its excess limits.

## Checks

- `mlsfb-cases-surcharge.l4`: 37 assertions written, 37 satisfied, 0 errors, 0
  warnings.
- `mlsfb-surcharge.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The taxpayer without private patient hospital cover who receives reportable
fringe benefits.** This is the employee whose payment summary shows a reportable
fringe benefits total. The Act addresses no official: s 10 imposes the surcharge,
and Part 3 says how much is payable by "the person". So every rule is already
about that person, and the questions are phrased as they ask them:

- `Must I pay the surcharge on my fringe benefits`
- `How much surcharge do I pay on my fringe benefits`
- `What is my surcharge rate`
- `Which income tier am I in`
- `Which Division applies to me`
- `Is my income above the surcharge line`
- `Am I married to this person`
- `Am I taken to be married to my spouse who died`
- `Does my policy count as hospital cover`
- `Do I count as uncovered on this day`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No
  instrument sets them. The tiers come from the Private Health Insurance Act, which
  s 6 names, and that Act's deposit is used.
- **The actors the text names.** Followed: the person, the spouse, dependants and
  prescribed persons. A trust appears only as the spouse's share of its net income
  (ss 15(2), 16(5)).
- **A judgment handed to someone else, answered conditionally.** Nothing in scope
  turns on an official's opinion.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.**
  - Worked out from facts:
    - married (s 7);
    - private patient hospital cover (s 4);
    - tier 2 and tier 3 earner (s 6, through PHI Act s 22-30 as modified);
    - the cover test on a day, with the special rules for prescribed persons
      (ss 13(2), 14(2));
    - which Division applies.
  - Asked as facts:
    - legal marriage, and registration under a prescribed State or Territory law;
    - "dependant" (s 5, through Part VIIB of the 1936 Act);
    - "prescribed person" (s 8, through s 251U);
    - "income for surcharge purposes" (ITAA 1997);
    - "reportable fringe benefits total" (FBTAA 1986);
    - "resident of Australia" (1936 Act s 6(1)).
- **One case is the text's natural unit.** Followed: one taxpayer and one year of
  income.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. There are two departures,
  each because the deposit drops a formula or a figure:
  - **The part-year formulas** in ss 12(3), 13(4) and 16(4) are missing ("the amount
    worked out using the formula:" is followed by nothing). A part-year surcharge is
    therefore `Not in the deposited text`, as in the Medicare Levy Act baseline.
  - **The PHI Act's indexed tier thresholds** are not deposited, and nor is its
    s 22-40(4) formula for two or more children. All of these are inputs.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| chloe c073 (2034-04-01), turns 31; hospital cover taken out before 1 July to avoid the loading | `Must I pay the surcharge on my fringe benefits`, `How much surcharge do I pay on my fringe benefits` | For 2033-34, uncovered until 1 April 2034, with Chloe on $110,000 and Liam on $60,000: no surcharge. The couple's $170,000 does not exceed the family tier 1 threshold of $180,000 (the stand-in). If Liam earned $80,000, the s 16(2) test would be met. Division 4 would then apply for only part of the year, so the amount is `Not in the deposited text`. For 2034-35, covered all year: nil. |

The scenario states that Chloe is married to Liam, that Oliver and Ella are their
children, and that she earns $110,000 from February 2034. It does not state:

- her reportable fringe benefits total (assumed $3,000);
- Liam's income (assumed $60,000, and $80,000 in a variant);
- the day the cover began (assumed 1 April 2034, the event date).

The event's main question, the Lifetime Health Cover loading, belongs to the Private
Health Insurance Act 2007, Division 34, and is not encoded here.

## Why this scope

The Act is short. All of its operative provisions are in:

- definitions that work from facts (ss 4-8);
- imposition (s 10);
- the three Divisions (ss 11-16).

Left out:

- **Machinery:** ss 1, 2 and 9.
- **s 3(2)**, which carries Part VIIB meanings across. It is a rule of
  interpretation, honoured by asking those terms as facts.
- **s 10(4)**, which applies the Act from 1999-2000. Every year asked is later.
- **The s 10(1) note's offset** under ITAA 1997 Subdiv 61-L.
- **The Schedule 2F s 271-105(1) assumption** in working out a trust's net income
  (ss 15(2)(b), 16(5)(b)). The spouse's trust share is asked as a figure.
- **Rounding.**

This is consistent with the Medicare Levy Act 1986 baseline
(`../../../medicare-levy-act-1986/encodings/baseline-2026-10`), which shares:

- the structure (three surcharge cases, single, single with dependants and married);
- the cover rule ($750/$1,500);
- the tiers and the $28,011 floor;
- the treatment of missing formulas and undeposited indexed thresholds.

That baseline asked "married" and "dependant" as facts and noted that the PHI Act
borrows them from here. This encoding works "married" out (s 7).

## What the Act turns out to say

1. **The surcharge is charged on fringe benefits, not on income.** The charge is 1%,
   1.25% or 1.5% of the reportable fringe benefits total (ss 12(2), (4), (5);
   13(3), (5), (6); 15(1), (3), (4)). The test is on income for surcharge purposes.
   Asserted.
2. **"Married" is wider than legal marriage, and narrower too.**
   - It takes in registered relationships and de facto couples (s 7(1)).
   - A de facto or registered relationship with someone new displaces a legal
     marriage to someone else (s 7(1A)).
   - Couples living separately and apart are not married (s 7(2)).
   - A widow or widower stays married until 30 June (s 7(3)).

   The Private Health Insurance Act 2007 borrows this meaning in ss 22-5(4)(b),
   22-30(1)(a) and 22-40(4). Asserted.
3. **The families table is reached by any non-spouse dependant on any day.** Section
   6(3) replaces the PHI Act's s 22-30(1)(b) "contributes in a substantial way to the
   maintenance" test. The new test asks whether the person "has one or more
   dependants ... other than a dependant to whom the person is married" on any day.
   Asserted, for a single parent.
4. **A married person with low income of their own pays none.** Under s 15(1)(c),
   a married person whose own income for surcharge purposes does not exceed $28,011
   pays no surcharge, even when the couple's income is well over the family
   threshold. Asserted.
5. **The couple test counts a spouse's trust share; the tiers do not.** Under
   ss 15(2) and 16(5), a spouse's presently entitled share of trust income assessed
   to the trustee under s 98 counts towards the couple test, but only "in working out
   whether subsection (1) applies". So a couple can meet the test while the person,
   on the PHI Act tables, is no tier earner at all. Such a person pays the base 1%.
   Asserted.
6. **Prescribed-person special rules for families.**
   - A person who would be a defence, veterans or certain-payments prescribed person
     but for their dependants (s 251U(2)) is taken to be covered.
   - Prescribed dependants are disregarded (ss 13(2), 14(2)).

   For a single person without dependants (s 12) there is no such rule. Asserted, on
   the day test.
7. **A non-resident pays none.** The surcharge falls only on a person who is a
   resident "at any time during the year of income" (s 10(1)). Asserted.
8. **Only Division 4 carries a year.** Divisions 2 and 3 use no dollar figure of
   this Act's own; their thresholds are the PHI Act's. Only Division 4's $28,011
   carries a year. As in the Medicare Levy Act baseline, the encoding infers, but the
   deposit does not state, that $28,011 is the 2025-26 figure. So a married person's
   2023-24 year is `Not in the deposited text`, while a single person's 2023-24 year
   is answered. This is narrower than the Medicare Levy Act baseline, which gates
   every surcharge answer on the year. Asserted.
9. **The deposit drops every formula:** the part-year formulas in ss 12(3), 13(4)
   and 16(4). Section 16(4)'s "where: number of applicable days ..." survives, which
   suggests the formula is a proportion by days. That is an inference, and it is not
   encoded. Asserted, as `Not in the deposited text`.
10. **c073: hospital cover taken out part-way through the year leaves a part-year
    case.** If Chloe and Liam's income were over the family threshold, Chloe would
    owe surcharge for 1 July 2033 to 31 March 2034 under s 16. The amount needs the
    missing s 16(4) formula. On the assumed incomes there is none. Asserted.

## What would need doing before this is worth anything

- Obtain the part-year formulas (ss 12(3), 13(4), 16(4)) from the authoritative
  text, so that they can replace the `Not in the deposited text` answers.
- Confirm from Act No. 58, 2026's application item which year the $28,011 is for.
  Retrieve earlier compilations for earlier years.
- Deposit the indexed PHI Act tier thresholds for each year (they are published,
  not legislated), and the s 22-40(4) formula.
- State Chloe's reportable fringe benefits total, Liam's income and the cover date
  in the scenario.
- Encode the Lifetime Health Cover loading (PHI Act Division 34), which is what
  c073 mainly asks.
- An independent test pass and a human gate.
