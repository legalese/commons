# KRS chapter 141, the individual income tax — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ky-income-tax.l4`) states the rules in the chapter's own actors and terms (resident, adjusted gross income, net income, modified gross income, threshold amount, the individual, the department), with the filing and payment duties as two regulative rules.
A **seat layer** (`ky-income-tax-seat.l4`) asks the taxpayer's questions, each with `@export` and a `@desc` on every input.
No REFUSE; parts not encoded answer `not covered`, asserted. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

Kentucky Revised Statutes, Legislative Research Commission ("Includes enactments through the 2026 Regular Session"; database updated 10/19/2026), deposited at `../../registers/source-bundle/krs-141-individual-income-tax.txt` (retrieved 2026-10-19 UTC). Unofficial; the LRC's certified versions are separate.
No instrument is deposited. The **standard deduction** is indexed yearly by the CPI-U from its 2000 base (141.081(2)) and the department's figure is an **input**. The **federal poverty guidelines** (HHS, 42 U.S.C. 9902(2)) for the threshold amount are **inputs**, as a base and an increment per person.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ky-income-tax.l4` (core), `ky-income-tax-seat.l4` (taxpayer seat) | `ky-income-tax-cases.l4` | 35 written, 35 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Expected values worked by hand before the run.
Regulative rules: 2 (file, pay). Asserted FULFILLED when kept; `#TRACE`d to breaches, with `-- expect:` lines, for a late return and for paying with an extended return.

## Seat

**The individual taxpayer** (a full-year resident for the tax computation). "Am I a Kentucky resident? What is my Kentucky AGI? Must I file? By when? How much do I owe, or get back? How much of my tax does the family size credit take away?"

Defaults (2026-10-18):
- **The chapter alone**; the CPI-indexed standard deduction and the poverty guidelines enter as inputs.
- **Actors the text names:** the individual, the department.
- **Judgments left to others:** none needed beyond the department's published standard deduction.
- **Definitions:** resident, Kentucky AGI (main adjustments), net income, modified gross income, family unit size and the family size percentage worked out; federal AGI, IRC s21 and s25A credits, s152(c) qualifying children asked as facts.
- **One case:** one return for one taxable year.
- **Machinery out:** the budget-reserve trigger analysis of 141.020(2)(a) to (c), optional tax tables, business credits, withholding by employers.

## Read with the Internal Revenue Code encoding

Kentucky starts from gross income less IRC s62 deductions, that is federal AGI (141.019(1)), with the IRC as in effect on 31 December 2025 for 2026 (141.010(21)). Federal AGI and the IRC s21 and s25A credits are inputs, answered by `subjects/us/internal-revenue-code-of-1986/`. Cross-folder IMPORT is not possible; the link is recorded here.

## Scope

**In:** 141.010(23), (25), (32); 141.019(1)(c), (e), (g), (l), (2) (with itemized deductions as one input); 141.020(1), (2)(e), (f), (g) (as the absence of an Act), (3)(a)4.-8.; 141.021 (as an input); 141.0205(2); 141.066(1), (3), (4); 141.067; 141.069(2)-(4); 141.081 (as an input); 141.160(1); 141.180(2), (3); 141.220.
**Not covered (asserted):** years before 2024; a 2027-on rate cut by Act; nonresidents and part-year residents (141.020(4), (6)); the other-state credit (141.070).
**Out:** the income gap credit (141.066(3)(d), for 2019-2020 only); spouse credits on separate returns (141.020(3)(a)5, 7, encoded in the core but not asked by the seat); the Education Opportunity Account credit; the carry-forward of the tuition credit.

## What the chapter turns out to say

1. **A flat rate that steps down by Act**: 4% for 2024 and 2025, 3.5% from 2026 (141.020(2)(e), (f)). From 2027 the rate falls only if the budget conditions are met and the General Assembly acts; "The department shall not implement an income tax rate reduction without an action by the General Assembly" ((g)4.b.). Without an Act, 3.5% continues. Asserted (case B2).
2. **The personal credits survive for age, blindness and the Guard.** The $10 personal and dependent credits of 141.020(3)(a)1-3 end with 2017, but items 4 to 8 carry no end date: $40 at 65, $40 for blindness, $20 for the Kentucky National Guard. Asserted (case E).
3. **The pension exclusion is "up to $31,110 of total distributions"** (141.019(1)(g)1.b.). The text does not say per person or per return; the encoding applies it to each spouse's own distributions (said to be the department's practice: unverified, general knowledge). Asserted.
4. **The family size credit is a poverty-guideline test on modified gross income**: the whole tax at or below 100% of the threshold, sliding by 10 points in bands up to 133% (141.066(3)). The threshold uses the HHS guideline "available on June 30 of the taxable year", for a family unit of at most 4. Asserted (cases C, D).
5. **Who must file uses the same threshold** (141.180(2)), so a single resident with modified gross income at or under one person's poverty guideline need not file. Asserted.
6. **Payment ignores extensions**: the tax is due "at the time prescribed for filing the income tax return, determined without regard to any extension" (141.220). Asserted by trace.
7. **No Kentucky earned income credit** is in the deposited chapter.
8. **The standard deduction is not in the text as a number** after 2000: it is last year's figure times a CPI-U ratio (141.081(2)), so it needs the department's annual publication.

## Before relying on it

- An independent test pass; cases checked against form 740 for 2025.
- The department's standard deduction for each year deposited, and the HHS guidelines.
- Nonresident and part-year computation, and the other-state credit.
