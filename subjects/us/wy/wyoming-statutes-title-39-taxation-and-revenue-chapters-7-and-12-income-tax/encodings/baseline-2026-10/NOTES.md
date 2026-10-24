# Wyoming income tax (W.S. 39-7-101, 39-12-101) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual who lives or works in Wyoming, with the design defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no independent test pass, no human gate. **Not for public use as advice.**

This is the short encoding the tax-and-benefits brief asks for where a state has no wage income tax: it records the finding in executable form, so the Interact form can answer the question.

## Edition

The Legislative Service Office's title 39 PDF (created 2026-10-14), downloaded 2026-10-19T18:00:49Z, as deposited at `../../registers/source-bundle/wy-stat-39-ch07-ch12.txt` (unofficial): chapters 7 and 12 in full, two sections.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wy-income-tax.l4` | `wy-income-tax-cases.l4` | 5 written, 5 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24).

## Seat

**The individual** who lives or works in Wyoming. Questions: "Do I owe Wyoming income tax?" and "Does the state, or may my county, city or town, tax my wages?". Defaults followed: the Act alone; the actors it names (the state and its political subdivisions); one case is one person. There is no regulative rule: the text states no duty of the individual.

## What the law turns out to say

1. **Wyoming imposes no income tax.** Chapter 7 (Income Taxes) consists of "39-7-101. Repealed By Laws 1998, ch. 5, § 4." and nothing else in the deposited text levies one. Asserted.
2. **No local government may tax income either.** W.S. 39-12-101: the state "does hereby preempt for itself the field of imposing and levying income taxes, earning taxes, or any other form of tax based on wages or other income and no county, city, town or other political subdivision shall have the right to impose, levy or collect such taxes." The state keeps the power; it does not use it. Asserted.
3. **What a Wyoming individual does meet**: federal income tax (`subjects/us/internal-revenue-code-of-1986/`), and, if 65 or over or totally disabled, the income-tested refund of sales, property and energy taxes in W.S. 39-11-109(c), encoded beside this at `../../../wyoming-statutes-title-39-taxation-and-revenue-chapter-11-administration/encodings/baseline-2026-10/`.

## Before relying on it

Compare with the official Wyoming Statutes. Nothing else is needed: the whole of the law is two sections.
