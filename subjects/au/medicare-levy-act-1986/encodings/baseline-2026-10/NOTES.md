# Medicare Levy Act 1986 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `mla-levy.l4`, holds the rules and the exported questions (each with
`@export` and `@desc`). One case file, `mla-cases-levy.l4`, is built by the
scratchpad generator `gen_medicare-levy-act-1986_baseline.py`. Its expected values
were written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

Medicare Levy Act 1986, Compilation No. 53, compilation date 1 July 2026, includes
amendments up to Act No. 58, 2026 (Register id C2026C00295), as deposited at
`../../registers/source-bundle/C2004A03351.txt`.

No instrument sets the Act's numbers. The low-income figures are in its own text
(ss 3, 8 and 8D), and an amending Act changes them each year.

Also used: the Private Health Insurance Act 2007, ss 22-30, 22-35, 22-40, 22-45
and 45-1, as deposited at
`../../../private-health-insurance-act-2007/registers/source-bundle/C2007A00031.txt`.
Section 3A of this Act borrows its income tiers from there, and s 3(5) borrows its
excess limits.

The A New Tax System (Medicare Levy Surcharge—Fringe Benefits) Act 1999 matters
here only for the meaning of "dependant" and "married" in s 3A(3). Those are asked
as facts, so that Act is not encoded.

## Checks

- `mla-cases-levy.l4`: 68 assertions written, 68 satisfied, 0 errors, 0 warnings.
- `mla-levy.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The taxpayer.** That is the individual on whose taxable income the levy, and any
surcharge, is imposed. The Act addresses no official: every section says what
levy is payable. So every rule is already about the taxpayer, and the questions are
phrased as that person asks them:

- `How much Medicare levy do I pay`
- `Is my income under the threshold`
- `How much levy on my own income`
- `Am I in the family case`
- `What is my family income threshold`
- `By how much is my levy reduced for my family`
- `By how much is my spouse's levy reduced`
- `Must I pay the surcharge`
- `How much surcharge do I pay`
- `Which income tier am I in`
- `Does my policy count as hospital cover`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No
  instrument sets them. The surcharge tiers come from the Private Health Insurance
  Act, which s 3A names, and that Act's deposit is used.
- **The actors the text names.** Followed: the person, the spouse, dependants,
  prescribed persons and people entitled to the s 160AAAA rebate. Trustees are left
  out; see "Why this scope".
- **A judgment handed to someone else, answered conditionally.** Nothing in scope
  turns on an official's opinion.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.**
  - Worked out from facts: threshold amount, phase-in limit, family income, family
    income threshold, the s 3(3) married rules, private patient hospital cover
    (s 3(5)), and tier 2 and tier 3 earner (s 3A, through PHI Act s 22-30).
  - Asked as facts: "married" and "spouse" (Part VIIB of the 1936 Act), "dependant"
    (ss 251R, 251V), "prescribed person" (s 251U), "income for surcharge purposes"
    (ITAA 1997), entitlement to the s 160AAAA rebate, the Subdiv 61-A offset and the
    Subdiv 961-A and 961-B notional offsets, and whether family tax benefit was
    payable.
- **One case is the text's natural unit.** Followed: one taxpayer and one year of
  income.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. There are three departures,
  each because the deposit drops a formula or a figure:
  - **The s 8(2) reduction formula** is missing ("calculated in accordance with the
    formula:" is followed by nothing). The reduction is therefore an input, and the
    encoding applies s 8(3) and (4) to it.
  - **The part-year surcharge formulas** in ss 8B(2)(b), 8C(3)(b) and 8D(4) are
    missing. A part-year surcharge is therefore `Not in the deposited text`.
  - **The PHI Act's indexed tier thresholds** are not deposited, and nor is its
    s 22-40(4) formula for two or more children. All of these are inputs.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| chloe c045, first return, for 2023-24, taxable income $27,500 | `How much Medicare levy do I pay` | `Not in the deposited text`, because 2023-24 comes before the deposited figures. Under the deposited figures, $27,500 does not exceed $28,011, so the levy is nil. The 2% rate alone would give $550. |
| chloe c048, second return, for 2024-25, taxable income $71,500 | `How much Medicare levy do I pay` | `Not in the deposited text` for 2024-25. Under the deposited figures it is $1,430, which is the full 2% and matches the scenario's `medicare_levy: 1430`. There is no surcharge: $71,500 is under the singles tier 1 threshold in any year. |

Chloe's hospital cover is not stated in the scenario. The cases assume she has none,
and that her income for surcharge purposes equals her taxable income.

## Why this scope

The seat is the individual taxpayer, and both life events ask only what levy
Chloe pays. The baseline therefore covers what any individual meets:

- the rate;
- the low-income threshold and the shading-in, for ordinary taxpayers and for
  seniors and pensioners;
- the family threshold;
- the surcharge for a person without hospital cover;
- the prescribed-person reduction.

Left out:

- **Trustees** (ss 6(2)-(6), 7(3)-(4), 8E-8G, 10). They are a different seat.
- **s 9A (lump sums in arrears).** It reworks taxable income through 1936 Act
  concepts (s 159ZR). A case with such a lump sum gets
  `Not covered by this encoding`.
- **Machinery:** ss 1, 2, 4, 5 and 11.
- **Rounding.**

This is consistent with the Income Tax Rates Act and ITAA 1997 baselines in this
repository. Both leave the levy to this Act, both use the same taxable incomes for
c045 and c048, and both find 2023-24 outside their deposits.

## What the Act turns out to say

1. **The figures carry no year.** The compilation states each low-income figure
   once ($28,011, $35,013, $44,268, $55,335, $47,238, $4,338, $61,623). The
   amendment history shows them amended every year, last by Act No. 58, 2026,
   commencing 1 July 2026. The encoding infers, but the deposit does not state, that
   these are the 2025-26 figures and that they stand for later years until amended.
   Earlier years are `Not in the deposited text`. Asserted.
2. **The rate is 2%** (s 6(1)), and it carries no year. Asserted.
3. **Shading-in.** Between the threshold amount and the phase-in limit, the levy
   "shall not exceed 10% of the amount of the excess" (s 7(2)). With the deposited
   figures, 10% of the excess meets 2% at the phase-in limit, to within a few
   cents. Asserted on $31,011 ($300) and $34,011 ($600).
4. **Seniors and pensioners.** For someone entitled to the s 160AAAA rebate, the
   threshold amount is $44,268, the phase-in limit is $55,335 and the family
   threshold is $61,623 (ss 3(1), 8(7)). Asserted.
5. **Single parents.** A single parent's family threshold rises by $4,338 only for a
   child for whom family tax benefit was payable to that parent (s 8(6)). Asserted.
6. **Apportionment between spouses.** Under s 8(3), a married person keeps only the
   share of the s 8(2) reduction that matches their own share of family income.
   Under s 8(4), any part of that share they cannot use reduces their spouse's levy.
   Asserted.
7. **The surcharge's income test and charge use different bases.** The test is on
   income for surcharge purposes, but the charge is a percentage of taxable income:
   1%, 1.25% for a tier 2 earner, 1.5% for a tier 3 earner. Asserted.
8. **A married person with low income of their own pays no surcharge.** Under
   s 8D(3)(c), a married person whose own income for surcharge purposes does not
   exceed $28,011 pays no surcharge, even when the couple's income is over the
   family tier 1 threshold. Asserted.
9. **Hospital cover with a large excess does not count.** A policy whose excess is
   more than $750 a year (one person insured) or $1,500 (any other policy) is not
   private patient hospital cover (s 3(5); PHI Act s 45-1). Asserted.
10. **The tier 1 threshold never falls.** The singles tier 1 threshold was $90,000
    for 2021-22 and 2022-23, and indexation never lowers it (PHI Act ss 22-35,
    22-45(3), (3A)). So an income at or under $90,000 attracts no surcharge in any
    later year. Asserted for c048.
11. **The deposit drops every formula:** s 8(2), and the part-year formulas in
    ss 8B, 8C and 8D. Asserted, as inputs and as `Not in the deposited text`.
12. **c045 cannot be checked against the scenario.** The scenario says Chloe's
    2023-24 levy is "nil under the threshold". That cannot be checked from this
    deposit, because the 2023-24 threshold is not in it. Under the deposited figures,
    $27,500 is under the threshold. Asserted.

## What would need doing before this is worth anything

- Retrieve the earlier compilations, or the amending Acts (No. 4, 2024 and No. 28,
  2025), so that the 2023-24 and 2024-25 figures for c045 and c048 can be encoded.
  Confirm from Act No. 58, 2026's application item which year the current figures
  are for.
- Obtain the s 8(2) and part-year surcharge formulas from the authoritative text, so
  that they can replace the input and the `Not in the deposited text` answers.
- Deposit the indexed PHI Act tier thresholds for each year (they are published,
  not legislated), and the s 22-40(4) formula.
- Encode s 9A, and the trustee provisions if a trustee seat is wanted.
- An independent test pass and a human gate.
