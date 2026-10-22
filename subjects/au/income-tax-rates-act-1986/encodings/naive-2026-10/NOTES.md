# Income Tax Rates Act 1986 — naive encoding

**Method: naive.** Straight from the deposited text, written with the
`writing-l4-rules` skill: a first pass that did not use the skill, conformed to it
on 14 October 2026 (see the last section). No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use.

**Edition:** Compilation No. 66, compilation date 1 July 2026, includes amendments
up to Act No. 50, 2026 (register id C2026C00300), as deposited at
`../../registers/source-bundle/C2004A03348.txt`.

**Checks:** one case file (`itra-cases-rates.l4`), 66 assertions satisfied, 0 errors, 0 warnings,
plus 9 refusals typed with `#CHECK` (the last section says why they are not yet
`#ASSERT REFUSED`). Run with the `l4` bundled in the L4 VS Code extension 1.6.93.

## Why this Act, and why scoped

This is requirement **REQ-0019** (priority 1), raised 3 times by the Western
Australian cradle-to-grave lives:

- **chloe c045** (2024-10-20). Her first tax return, for 2023-24, on taxable income of $27,500. The scenario expects nil tax.
- **chloe c048** (2025-10-25). Her second return, for 2024-25, on taxable income of $71,500. The scenario expects tax before offsets of $12,842.
- **daniel d04a** (2033-11-30). The first company return of Jarrah Legal Technologies Pty Ltd: "What rate?"

The encoding covers the provisions those events cite: Schedule 7 and s 23 (the
base rate entity). It adds what changes a Schedule 7 answer:

- the s 3 definitions (tax-free threshold, prescribed non-resident, resident
  taxpayer, ordinary taxable income);
- the superannuation and employment termination remainders, taxed at 45%;
- the working holiday maker rules (clause 4 of Parts I and II, and Part III);
- part-year residency (ss 16, 18 and 20(1));
- s 23(6), the ceiling on tax for a non-profit company.

**Not encoded:**

- the abnormal-income averaging in Schedule 7 clauses 2 and 3;
- trustees and minors (ss 12(4)–(13), 13–15);
- primary producers (s 12A);
- Schedules 8 to 12;
- RSA providers, PDFs, credit unions, life insurers, super funds and sovereign entities (s 23(3)–(5), (7), 23A, 25–30);
- s 23AB's list of passive income, which is an input here.

The low income tax offset, the Medicare levy and HELP repayments come from other
Acts. The loss carry-forward d04a also asks about is in the Income Tax Assessment Act 1997.

## What the Act turns out to say

### 1. The deposited compilation has no rates for 2023-24, the year c045 asks about

Schedule 7 Part I has three tables:

- "for the 2024-25 or 2025-26 year of income";
- "for the 2026-27 year of income";
- "for the 2027-28 year of income or a later year of income".

Nothing covers 2023-24 or earlier. So this compilation cannot answer Chloe's first
return. The first pass returned `NOTHING` for it. The conformed encoding refuses, by
name: "the deposited compilation has no Schedule 7 table for a year of income
before 2024-25". The scenario's answer of nil tax
also relies on the low income tax offset, which is outside this Act.

For comparison only: the 2024-25 table would put tax on $27,500 at $1,488 before
offsets. Asserted.

### 2. Chloe's 2024-25 tax before offsets comes to $12,238, not the scenario's $12,842

On $71,500 for 2024-25:

- 16% of $26,800 (from $18,200 to $45,000) is $4,288.
- 30% of $26,500 (from $45,000 to $71,500) is $7,950.
- The total is **$12,238**.

c048 records `tax_before_offsets: 12842`, a difference of $604. Nothing in the
deposited text produces $12,842. Asserted (12,238).

### 3. The first resident rate falls each year: 16%, then 15%, then 14%

The band from the threshold to $45,000 is taxed at:

- 16% for 2024-25 and 2025-26;
- 15% for 2026-27;
- 14% for 2027-28 and later years.

The other bands do not change: 30% to $135,000, 37% to $190,000, 45% above. On
$71,500 the tax is $12,238, then $11,970, then $11,702. Asserted.

### 4. A resident working holiday maker gets no tax-free threshold on visa income

Clause 4 counts working holiday taxable income "as the first parts (starting from
$0)" of ordinary taxable income, and the clause 1 table does not apply to it.
Part III taxes it at 15% from the first dollar, up to $45,000.

So a resident working holiday maker earning $30,000 on the visa pays $4,500. A
resident without the visa pays $1,888 on the same income. Only the income above the
visa income goes through the resident table. Asserted.

### 5. A non-resident all year can still be a "resident taxpayer" for the rates

A "prescribed non-resident" excludes anyone paid an assessable payment in the year
under the Veterans' Entitlements Act, the MRCA or the Social Security Act. Such a
person is a "resident taxpayer" under s 3 and gets the resident table, threshold
included: $1,888 on $30,000, against $9,000 at the non-resident rates. Asserted.

### 6. A base rate entity pays 25%, and both limits are strict

Under s 23(2), a base rate entity pays 25% and any other company pays 30%. Section
23AA sets two tests:

- passive income must be "no more than 80%" of assessable income, so exactly 80% qualifies;
- aggregated turnover must be "less than $50 million", so exactly $50 million does not.

Jarrah, with turnover under $3 million and trading income, is a base rate entity at
25%. In a loss year its taxable income is nil and so is its tax. Asserted.

The scenario does not give Jarrah's figures. The fixtures assume them.

### 7. A non-profit company's tax is capped at 55% of income over $416

Section 23(6) applies to non-profit companies with taxable income up to $762 (a
base rate entity) or $915 (any other company). Their tax is capped at 55% of the
excess over $416:

- nil tax on $416;
- $101.20 on $600 for a base rate entity, against $150 at 25%;
- no cap on $800 for a base rate entity, which pays $200.

Asserted.

### 8. The deposit drops the formulas

Every formula set as an image is missing. The words that introduce each one ("the
following formula:", "using the formula:", "the formula , where") are followed by
nothing. This affects:

- s 20(1), the pro-rated tax-free threshold for part-year residents;
- Schedule 7 clauses 2 and 3;
- ss 12(7), 12AA and 12A.

The pro-rated threshold is therefore an input. The October 2024 arrival case uses
an assumed $13,650. The encoding does apply s 18(2): an eligible pensioner has no
part-year residency period and keeps the full $18,200. Asserted.

## What would need doing before this is worth anything

- Retrieve the s 20 formula and the clause 2 and 3 formulas from the PDF or Word
  original, and encode them.
- Retrieve the 2023-24 rates from an earlier compilation, so that c045 can be
  answered. The endnotes would name the amending Act that replaced the table; they
  were not read for this encoding.
- Reconcile c048's $12,842 with the text, and correct whichever side is wrong.
- Encode s 23AB, so that base rate entity passive income is computed rather than taken as an input.
- Rounding to whole dollars, and the interaction with offsets in the Income Tax
  Assessment Act 1997 s 4-10, are not modelled.

## Conformed to the writing-l4-rules skill (14 October 2026)

The first pass was written without the skill. This pass rewrote both `.l4` files to
the skill's standard. It kept the scope (the same provisions), the quoted statutory
text and every expected value. Both files are now written by a new generator,
`gen_income-tax-rates-act-1986-conform.py` (scratchpad). The old generator, which
wrote only the case file, is untouched.

### What changed

- **Refusals instead of `NOTHING`.** There are seven named refusals. Each is a
  definition whose name is its message, with an `@ref` above it, at any type
  (`GIVEN a IS A TYPE`), and each is returned rather than stored:
  - a year of income before 2024-25 (Schedule 7 has no table for it in this compilation);
  - a special income component (Schedule 7 clauses 2 and 3: the formula was not deposited);
  - a part-year residency period with no pro-rated threshold supplied (s 20(1));
  - a company's year of income before 2024-25 (s 23 names no year; see finding 12);
  - a company in the capacity of a trustee (s 23(1));
  - an RSA provider, a PDF or a life insurance company (s 23(3) to (5), s 23A);
  - the tax of a recognised medium credit union (s 23(7)).

  The first pass could not reach the last six at all. It had no input for them, and
  answered as if they did not exist.
- **The Schedule 7 tables are data.** There is one row type, `Schedule 7 item`,
  with columns for the item, "exceeds", "does not exceed", the rate and the table.
  The three Part I tables are one twelve-row list; Part II and Part III are lists
  of their own. The generator lays them all out with positional `OF`, a ruler
  comment, and ditto on the constructor, `OF`, `JUST` and the table name.
  - Item 1 of Part I keeps "the tax-free threshold" as a parameter, because s 20(1)
    replaces it.
  - The Part II rates are "the second resident personal tax rate" and "the third
    resident personal tax rate". They are parameters supplied from s 3, which now
    reads them out of the applicable Part I table instead of hard-coding 30% and 37%.
  - One marginal fold serves all five tables. Clause 4 is applied directly, as "the
    part above the working holiday taxable income", instead of as the difference
    of two cumulative taxes.
  - The `no upper limit` sentinel (10^12) is gone: an open top band is `NOTHING`.
- **Domain types.**
  - `Residency in the year of income` is one type with five alternatives, after
    s 18(1)(a)-(c). It replaces the flag "became or ceased to be a resident during
    the year".
  - `Payments in the year of income` has one field for each of limbs (a), (b) and
    (ba), and limb (c) split in two. It replaces the single flag for veterans',
    military and social security payments. `an eligible pensioner` is now computed
    from it under s 16, instead of being an input.
  - `Kind of company` names the kinds that s 23(1) to (7) and s 23A tell apart.
  - The pro-rated threshold is a `MAYBE`.
- **Shape.** The encoding now uses:
  - `BRANCH` for the choice of table by year and for the two-limb company rules;
  - `CONSIDER` for residency and the `MAYBE`s;
  - percent literals (`16%`, `25%`, `55%`);
  - the prelude's `min`, `max`, `sum` and `filter` instead of hand-written helpers;
  - `@ref` above every rule;
  - labels such as `"(a)" ...` on limb chains.
- **Expected values.** No amount changed. Some changed in form, because the model
  changed:
  - 22 `JUST n` became `n`, because the tax is no longer a `MAYBE`;
  - the 4 company rates `25` and `30` became `25%` and `30%`;
  - the 5 "has a resident table" booleans became the table that applies (4) and a refusal (1);
  - the 3 `NOTHING`s became refusals.

  15 assertions and 6 refusal checks are new.

### New findings

9. **The two payment lists differ in one limb.** "Prescribed non-resident" (s 3)
   and "eligible pensioner" (s 16) list the same payments, except that s 16's (c)
   leaves out Parts 2.11, 2.12 and 2.15 of the Social Security Act 1991. A payment
   under one of those Parts therefore has two effects:
   - it makes a person who was a non-resident all year a resident taxpayer: $1,888
     on $30,000, not $9,000;
   - it does not make an arrival an eligible pensioner, so the arrival keeps a
     part-year residency period and a pro-rated threshold: $2,616 on $30,000, with
     an assumed threshold of $13,650.

   Asserted.
10. **A July arrival gets the full threshold.** Under s 18(1)(b) the period runs
    "from the beginning of that month". A person who commences to be a resident
    during July therefore has a period that is the whole year, and s 18(2)(b) says
    that is not a part-year residency period. The same holds for a departure during
    June. Asserted for the July arrival.
11. **A July departure is outside s 18(1)(a) on its words.** Paragraph (a) needs the
    person to cease to be a resident "during a subsequent month", which is a month
    after the first. A resident who leaves during July has no part-year residency
    period and keeps the full $18,200. Whether the ATO reads it that way was not
    checked. Asserted.
12. **Section 23 names no year of income.** Schedule 7 says which year each table is
    for; s 23(2) does not, and the compilation is the law as at 1 July 2026. The
    first pass answered 25% for a company in any year, including years when other
    rates applied. The conformed encoding answers from 2024-25, the first year this
    compilation's own tables cover, and refuses before it. That boundary is the
    encoder's, not the Act's.
13. **The tools on this machine are older than the skill.** Neither `l4` installed
    on 14 October 2026 has `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`. These landed
    in l4-ide at 75e08b55e on 5 September 2026. The `l4` on `PATH` (April 2026)
    lacks them, and so does the one in the VS Code extension 1.6.93 (13 October
    2026). As a result:
    - the deposited files carry each refusal's body as the prelude's `TBD`, which
      is a refusal on a current `l4` and an assumed term here;
    - each refusal is tested with `#CHECK`, which types the path without running it;
    - `python gen_income-tax-rates-act-1986-conform.py --refuse` writes the skill's
      form, `REFUSE "<name>"` and `#ASSERT REFUSED ... BECAUSE "<name>"`. On the
      installed binary its only errors are the seven unknown `REFUSE`s and the
      unparsed `BECAUSE`, so it has not been run.

    The `l4` on `PATH` has two further defects:
    - it rejects `_` digit separators, so none are used;
    - given a bare file name, it silently fails to import the prelude. The first
      pass passed only because it used no prelude names.

    Every check here was run with the extension's binary. The `PATH` binary also
    passes when it is given a path that includes a directory.

### Still short of the skill

- The refusals are not yet `REFUSE`, and are not yet asserted (finding 13).
- There is no `@export` or `@desc`. On the installed binary `TBD` is an `ASSUME`,
  which an export would publish as a parameter.
- Months of residency are not validated: a month of 13 is not rejected as invalid
  input. A person who ceased to be a resident and later commenced again in the same
  year has no constructor.
