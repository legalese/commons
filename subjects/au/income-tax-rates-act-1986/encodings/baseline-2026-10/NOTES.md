# Income Tax Rates Act 1986 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `itra-rates.l4`, holds the rules and the exported questions (each with
`@export` and `@desc`). One case file, `itra-cases-rates.l4`, is built by the
scratchpad generator `gen_income-tax-rates-act-1986_baseline.py`. Its expected
values were written by hand from the text.

This baseline replaces the first-pass encoding `naive-2026-10`. It covers
everything that encoding covered and keeps its hand-checked figures. It adds:

- s 23AB, worked out from facts (the first pass took passive income as an input);
- the s 3 non-profit company definition, worked out from facts;
- the s 3A visa test;
- an explicit answer for years and cases the text does not cover.

## Edition

Income Tax Rates Act 1986, Compilation No. 66, compilation date 1 July 2026,
includes amendments up to Act No. 50, 2026 (Register id C2026C00300), as deposited
at `../../registers/source-bundle/C2004A03348.txt`.

The formulas the text deposit lost (ss 12(7), (8), 12AA, 12A, 13(10), 14(3), 15(8),
20(1), (2), Schedule 7 Parts I and II clauses 2 and 3, Schedule 11 clause 3) are
transcribed by hand from the Word rendering of the same compilation, fetched from the
Federal Register of Legislation on 2026-10-21, in
`../../registers/source-bundle/C2004A03348.formulas.md`. The encoding uses s 20(1)
and Schedule 7 Parts I and II clause 2.

No regulation sets these numbers. The rates are in the Act's own text, and each
Budget changes them by amending Act.

**Dated arm for 2023-24 (REQ-0056, 22 October 2026).** Compilation No. 62,
compilation date 1 April 2024, includes amendments up to Act No. 3, 2024 (Register id
C2024C00132), deposited beside the current text at
`../../registers/source-bundle/C2004A03348.2024-04-01.txt`. The Register returned it as
the version in force on 30 June 2024, the last day of the 2023-24 year of income. Its
lost formulas are in `C2004A03348.2024-04-01.formulas.md` and are the same as
Compilation No. 66's. Schedule 7 Parts I, II and III each have a table "for the
2020-21, 2021-22, 2022-23 or 2023-24 year of income":

- resident: 19% above the tax-free threshold to $45,000, 32.5% to $120,000, 37% to
  $180,000, then 45%;
- non-resident: the second resident personal tax rate (32.5%) to $120,000, 37% to
  $180,000, then 45%;
- working holiday makers: 15% to $45,000, 32.5% to $120,000, 37% to $180,000, then 45%.

The encoding uses these tables for 2023-24 only. Compilation No. 62 is not the
compilation that was in force for 2020-21 to 2022-23, so those years stay
`Not in the deposited text`.

Compared line by line with Compilation No. 66, the provisions encoded here read the
same: the $18,200 threshold, s 20(1)'s $4,736, and clauses 2 and 4. The one
difference is s 16 "eligible pensioner" (c), which in Compilation No. 62 also leaves
out Part 3.15A of the Social Security Act 1991. Being an eligible pensioner is asked
as a fact, so only that question's wording changes.

## Checks

- `itra-cases-rates.l4`: 94 assertions written, 94 satisfied, 0 errors, 0 warnings
  (73 before the 2023-24 arm of 2026-10-22; 68 before the formulas were recovered on
  2026-10-21). When the arm was added, the four assertions that had expected
  `Not in the deposited text` for 2023-24 were the only ones to fail. They now assert
  the 2023-24 answers, and 2022-23 cases assert `Not in the deposited text` in their
  place.
- `itra-rates.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The taxpayer.** That is the individual whose taxable income is taxed. In Daniel's
life it is also the founder, who asks at what rate his company, Jarrah Legal
Technologies Pty Ltd, is taxed.

The Act declares rates and addresses no official. So every rule is already about
what the taxpayer pays, and the questions are phrased as that person asks them:

- `How much tax is on my taxable income`
- `What is my marginal rate`
- `What tax-free threshold do I get`
- `Am I a resident taxpayer`
- `Is my company a base rate entity`
- `At what rate is my company taxed`
- `How much tax must my company pay`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No
  instrument sets them; they are in Schedule 7 and s 23.
- **The actors the text names.** Followed: resident and non-resident taxpayers,
  working holiday makers, eligible pensioners, companies.
- **A judgment handed to someone else, answered conditionally.** Nothing in scope
  turns on an official's opinion. The Commissioner's "fair and reasonable"
  reductions in ss 13 and 15 are outside the scope.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.** Followed for the Act's own definitions: prescribed non-resident, resident
  taxpayer, ordinary taxable income, working holiday maker, working holiday taxable
  income, part-year residency period, non-profit company, base rate entity and base
  rate entity passive income. The following borrowed terms are asked as facts:
  - "non-resident";
  - aggregated turnover;
  - the superannuation and employment termination remainders, which come from
    ITAA 1997 Divisions 301 and 82;
  - "non-portfolio dividend", "net capital gain" and the kinds of lender in
    s 23AB(2)(a).
- **One case is the text's natural unit.** Followed: one taxpayer and one year of
  income, or one company and one year of income.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. The s 20(1) pro-rating formula
  and Schedule 7 clause 2 (abnormal income, Parts I and II) are encoded from the
  sidecar transcription; the number of months in the part-year residency period and
  the abnormal income amount (ITAA 1997 Division 405) are asked. Clause 3 (Division 16
  or Division 392 averaging, which needs the s 392-45 "average income"), and a special
  income component met together with a superannuation or termination remainder or with
  working holiday income, get `Not covered by this encoding`.

## The lives

| Event | Decision asked | Answer |
|---|---|---|
| chloe c045, first return for 2023-24, $27,500 | `How much tax is on my taxable income`; `What is my marginal rate` | $1,767 before offsets ((27,500 - 18,200) x 19%, from Compilation No. 62), at a marginal rate of 19%. Not the nil the scenario expects (finding 14). For comparison, the 2024-25 table gives $1,488. |
| chloe c048, second return for 2024-25, $71,500 | `How much tax is on my taxable income`; `What is my marginal rate` | $12,238 before offsets, at a marginal rate of 30% |
| daniel d04a, Jarrah's first company return | `Is my company a base rate entity`; `At what rate is my company taxed`; `How much tax must my company pay` | A base rate entity at 25%; nil tax in a loss year |

Jake's k043 (2028-29, $31,000, $1,792) is not an event of this Act in the plan. It
is asserted here only as a cross-check against the ITAA 1997 baseline.

**Agreement with the ITAA 1997 baseline.**
`../../../income-tax-assessment-act-1997/encodings/baseline-2026-10/` restates
these rates in `itaa-income.l4`. Every figure it asserts is asserted here too, with
the same result:

- the $18,200 threshold;
- c045 not covered;
- c048 $12,238;
- k043 $1,792;
- a company with no passive income and $3 million turnover at 25%;
- a company with 90% passive income at 30%.

The two encodings agree.

## Why this scope

The lives ask for Schedule 7 and s 23. A Schedule 7 answer also depends on:

- who is a resident taxpayer (s 3);
- the threshold, including part-year residents (ss 16 to 20);
- the remainders and ordinary taxable income (s 3);
- working holiday makers (s 3A and clause 4).

So those are in. A company's rate depends on ss 23AA and 23AB. The non-profit
ceiling in s 23(6) is the only other limb of s 23 that an ordinary company can meet.

Left out:

- trustees and minors (ss 12(4)–(13), 13–15, 20(1A)–(3));
- notional rates and averaging (s 12(2), Schedule 8, Schedule 7 clauses 2–3);
- primary producers and minimum tax capital gains (ss 12A, 12AA);
- Schedules 9 to 12;
- RSA providers, PDFs, credit unions and life insurers (s 23(3)–(5), (7), 23A);
- funds, trusts and sovereign entities (ss 25–30);
- the machinery (ss 1, 2, 4, 5, 21).

A company of a kind left out gets `Not covered by this encoding`.

## What the Act turns out to say

1. **(Superseded on 2026-10-22 by finding 14: 2023-24 is now answered from
   Compilation No. 62.) The deposited text covers 2024-25 onwards, and nothing
   earlier.** Schedule 7
   Part I has tables "for the 2024-25 or 2025-26 year of income", "for the 2026-27
   year of income" and "for the 2027-28 year of income or a later year of income".
   Parts II and III each have one table, "for the 2024-25 year of income or a later
   year of income". For 2023-24 and earlier, every individual answer is
   `Not in the deposited text`, and that includes c045. The scenario expects nil tax
   for c045, which also relies on the low income tax offset in another Act. Asserted.
2. **Chloe's 2024-25 tax before offsets is $12,238, not the scenario's $12,842.**
   $26,800 at 16% is $4,288, and $26,500 at 30% is $7,950. Nothing in the deposit
   produces $12,842. The ITAA 1997 baseline reaches the same $12,238. Asserted.
3. **The first resident rate falls each year: 16%, then 15%, then 14%.** The other
   bands do not move: 30% to $135,000, 37% to $190,000, 45% above. On $71,500 the
   tax is $12,238, then $11,970, then $11,702. Asserted.
4. **A non-resident has no threshold, and the non-resident rates follow the resident
   table.** The first non-resident band is "the second resident personal tax rate",
   which s 3 ties to item 2 of the Part I table for the year. So $30,000 costs a
   non-resident $9,000 and a resident $1,888. The marginal rate on a non-resident's
   first dollar is 30%. Asserted.
5. **A non-resident all year can still be a "resident taxpayer".** A person paid a
   taxable veterans', military compensation or social security payment is excluded
   from "prescribed non-resident". That person gets the resident table, threshold
   included. Asserted.
6. **A working holiday maker's visa income takes up the threshold.** Clause 4 counts
   working holiday taxable income "as the first parts (starting from $0)" of ordinary
   taxable income. Part III taxes it at 15% from the first dollar. $30,000 on a
   working holiday visa costs $4,500. With $20,000 on the visa out of $60,000, the
   tax is $11,500. The s 3A test reaches a work bridging visa held while a 417 or
   462 application is undecided. Asserted.
7. **The superannuation and employment termination remainders are taxed at a flat
   45%, outside the table.** Asserted.
8. **A part-year resident's threshold is pro-rated, but not an eligible pensioner's.**
   s 18(2)(a) takes the eligible pensioner out of part-year residency, so the full
   $18,200 applies. The s 20(1) formula (recovered from the authorised rendering) is
   ($18,200 - $4,736) + $4,736 x months / 12: $13,464 for anyone with a part-year
   residency period, plus $394.67 a month. s 18(1) counts the whole month of arrival,
   so an October 2024 arrival has 9 months, a $17,016 threshold and $2,077.44 tax on
   $30,000. Asserted.
9. **The company rate has no year limits.** Under s 23(2), a base rate entity pays
   25% and any other company 30%. s 23AA sets two tests:
   - passive income must be "no more than 80%" of assessable income, so exactly 80%
     qualifies;
   - turnover must be "less than $50 million", so exactly $50 million does not.

   Jarrah, trading under $3 million turnover, is a base rate entity at 25%, with nil
   tax in a loss year. The scenario does not give Jarrah's figures; the ones used are
   assumed.

   The return is dated 30 November 2033. By inference it is for 2032-33, but the
   rate is the same either way. Asserted.
10. **Under s 23AB, interest is not passive for a lender, nor to the extent that it
    is a return on an equity interest.** An ordinary company earning 90% interest is
    not a base rate entity. A credit licensee earning the same interest has no
    passive income at all. Asserted.
11. **A non-profit company's tax is capped at 55% of income over $416, but only at
    low incomes.** The cap applies up to $762 for a base rate entity and $915 for any
    other company. Some figures:
    - $600 for a base rate entity: $101.20 rather than $150;
    - $416: nil;
    - $800 for a base rate entity: $200, because it is above $762;
    - $800 for a company that is not a base rate entity: $211.20.

    A not-for-profit whose constitution allows distributions is not a "non-profit
    company". Asserted.
12. **The text deposit drops every formula set as an image**, in ss 12(7), (8),
    12AA, 12A, 13(10), 14(3), 15(8), 20(1), (2) and Schedules 7 and 11. All are now
    transcribed in the sidecar. Those outside the seat's scope (the s 94 further tax,
    minimum tax capital gains, primary producers, Division 6AA phase-out limits,
    trustees, Schedule 11) are transcribed but not encoded.
13. **Abnormal income is taxed at five times the tax on a fifth of it.** Schedule 7
    clause 2 sets a rate per dollar of (A + B) / C: A is the clause 1 tax on the
    reduced taxable income, B is five times the extra tax on adding 20% of the special
    income component, and C is the taxable income in whole dollars. An author with a
    $100,000 abnormal income amount in $150,000 pays $35,788 rather than $36,838. For a
    non-resident whose income all falls in the 30% band it changes nothing ($18,000 on
    $60,000). Asserted.
14. **Chloe's 2023-24 tax before offsets is $1,767, not nil (c045).** Compilation
    No. 62, in force for 2023-24, taxes a resident at 19% on ordinary taxable income
    above the $18,200 tax-free threshold up to $45,000. On $27,500 that is 9,300 x 19% =
    $1,767. The scenario expects nil tax for the 2023-24 return. Nil would need offsets
    of at least $1,767, but the Low Income tax offset (ITAA 1997 ss 61-110, 61-115) is
    $700 at that income. That leaves $1,067 of income tax (asserted in the ITAA 1997
    baseline), before the Medicare levy of $150 (Medicare Levy Act baseline, REQ-0024).
    The audit's recollection of $1,767 and $1,067 matches the deposited text. This is
    for the scenario's author. Asserted.
15. **The 2023-24 table ends its bands lower: $120,000 and $180,000, not $135,000 and
    $190,000.** So $130,000 is taxed at a marginal 37% in 2023-24 but 30% in 2024-25,
    and $185,000 at 45% rather than 37%. In 2023-24 the non-resident table's item 2 is a
    plain "37%", where from 2024-25 it is "the third resident personal tax rate". Both
    are 37%, so one rule serves both years. Asserted.

## What would need doing before this is worth anything

- Encode Schedule 7 clause 3 with the ITAA 1997 s 392-45 average income, and the
  special income component where there are remainders (s 3 "special income
  component" (b)) or working holiday income (clause 4(c)).
- 2023-24 is answered (REQ-0056). For 2020-21 to 2022-23, deposit the compilations
  in force for those years. Compilation No. 62's table names them, but it is not
  their compilation, and the 1997 Act's offsets differed then (the low and middle
  income tax offset).
- Reconcile c048's $12,842 with the text, and correct whichever side is wrong.
- Model rounding to whole dollars, and the step from this Act's tax to tax payable
  after offsets (ITAA 1997 s 4-10).
- Run an independent test pass and the human gates.
