# Arkansas Code 26-51-201(a)(3) (income tax rate tables, from 2024) — baseline encoding

## Method

**Baseline.** Written straight from the deposited Act, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
One function computes the tax on net income; two questions are exported with `@export` and `@desc`.
No regulative rule: the only "shall" in the deposited text is "shall determine the amount of income tax due ... in accordance with the table", which is a computation. Duties to file and pay are in parts of Chapter 51 that could not be deposited.
No REFUSE; a tax year before 2024 answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not tax advice.**

## Edition, and why an Act

The Arkansas Code is published online only through LexisNexis's Code of Arkansas Public Access, which served a CAPTCHA on 2026-09-23; that is a no, and the Code is not deposited. The General Assembly publishes the Acts on its own site, and Acts 2024 (2nd Ex. Sess.), No. 1, s 1 amends Ark. Code 26-51-201(a)(3) "to read as follows", setting the subdivision out in full. It is deposited at `../../registers/source-bundle/ar-acts-2024-2nd-ex-sess-act-1.txt`, with the tables as enacted in `ar-acts-2024-2nd-ex-sess-act-1.formulas.md`, because the plain text loses the Act's strike-through (each changed figure appears twice). Act 4 of the same session is identical and was compared, not deposited.

The Bureau of Legislative Research's "Code Sections Amended" lists for the 2025 Regular Session and the 2026 Fiscal Session (read 2026-10-24) show no later amendment of s 26-51-201(a)(3).

**Inputs:** net income (Chapter 51, not deposited).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ar-income-tax-rates.l4` | `ar-income-tax-rates-cases.l4` | 17 written, 17 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked out by hand from the transcribed tables.

## Seat

**The individual Arkansas taxpayer.** Questions: "What is my Arkansas tax on my net income?", "What bracket adjustment do I get?".
Defaults followed: the Act alone; the actors it names ("every resident, individual, trust, or estate"); one case is one tax year's net income; the Act's own terms. Departure: the Act is a session law, not the Code, because the Code could not be deposited.

## Scope

**In:** s 26-51-201(a)(3)(A), (B), (C), for tax years beginning on or after 1 January 2024.
**Out:** everything else: net income itself, deductions, the personal tax credits, residence and part-year rules, filing and payment, any inflation adjustment of these tables elsewhere in s 26-51-201, and tax years before 2024.

## What the Act turns out to say

1. **Two tables, chosen by net income.** Up to $89,600, table A: 0%, 2%, 3%, 3.4% and 3.9%. Above $89,600, table B: 2% on the first $4,500 and 3.9% on the rest, so the lower rows of table A are taken back. Asserted.
2. **The tables are read as marginal: each rate applies to the part of net income within its row.** The Act says only that the tax is determined "in accordance with the table". The marginal reading makes the tax continuous across table A's rows, and puts the table A and table B results within $2 of each other at the $89,600/$89,601 boundary once the $310 bracket adjustment is taken off, which is what the adjustment is for. Asserted ($89,600: $3,097.04; $89,650: $3,100.85).
3. **The bracket adjustment phases out by $10 for each $100 of net income** from $310 at $89,601-$89,700 to $10 at $92,601-$92,700, and is nil from $92,701. Encoded as that arithmetic; all 32 rows agree with the transcribed table. Asserted at each edge.
4. **In the phase-out band the marginal rate is about 13.9%.** From $89,601 to $92,700 the tax rises $3.90 for each $100 of income, plus the $10 lost from the adjustment every $100. A consequence of the Act's tables, not stated in it.
5. **The table rows run in whole dollars** ($5,299, then $5,300). Net income with cents between two rows is treated as falling in the lower one; the Department of Finance and Administration's own tables are not deposited.

## Before relying on it

- Read the full s 26-51-201 (not available from an allowed source) for any inflation indexing of these tables, and Chapter 51 for net income, the personal tax credits and the standard deduction.
- Have a person check the transcribed tables against the Act's PDF, since strike-through could not be seen in this session.
- An independent test pass.
