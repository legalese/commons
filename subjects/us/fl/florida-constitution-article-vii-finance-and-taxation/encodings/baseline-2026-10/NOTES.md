# Florida Constitution art. VII s 5(a): no personal income tax — short baseline encoding

## Method

**Baseline, short.** The personal income tax half of Florida's "tax and benefits" sample: Florida levies no tax on the income of natural persons, and this encoding states why, from the deposited Constitution, from the seat of the individual. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no independent test pass, no human gate. **Not for public use as advice.**

## Edition

Fla. Const. art. VII as displayed on Online Sunshine (stylesheet path `/constitution/2025/`), deposited at `../../registers/source-bundle/fla-const-art7.txt` (retrieved 2026-10-19). Section 5 was adopted by H.J.R. 7-B, 1971.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `fl-income-tax-limit.l4` | `fl-cases-income-tax-limit.l4` | 5 written, 5 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24).

## Seat

**The individual resident or citizen of Florida.** Questions: "Do I pay Florida income tax?" and "What is the most Florida could tax my income?". The State and the Legislature appear only as what s 5(a) forbids them to do. Defaults: the provision alone; borrowed terms (the federal or other state allowance) asked as an input; no regulative rule, because s 5(a) limits the State and puts no duty on the person.

## Scope

**In:** art. VII s 5(a), as it applies to the income of natural persons. **Out:** the same limit on estate and inheritance taxes; s 5(b) (income of "residents and citizens other than natural persons", the corporate income tax); the homestead and other exemptions in ss 3, 4 and 6, which the deposit also holds and which are property-tax matters.

## What the Constitution turns out to say

1. **No Florida statute in the deposited law taxes the income of natural persons.** The Florida law deposited in commons (chapters 83 part II, 121, 196, 366, 414, 443, 448, 626 part IX, s 409.212, and art. VII of the Constitution) contains no such tax. This is a statement about what is deposited; the whole of the Florida Statutes was not searched. Asserted ("Do I pay Florida income tax?").
2. **The ceiling is whatever federal or other state law "may ... allow to be credited upon or deducted from" its own similar tax, and the "deducted" limb is open.** s 5(a) forbids a tax on the income of resident or citizen natural persons "in excess of the aggregate of amounts which may be allowed to be credited upon or deducted from any similar tax levied by the United States or any state". Read with a credit, the limit is the amount another government would credit for a Florida tax. Read with a deduction, it is harder to say what "the aggregate of amounts ... allowed to be ... deducted" would be. This encoding does not resolve it: the allowance is an input, and the ceiling equals it. Asserted (allowance $0: ceiling $0; $500: $500).
3. **The limit protects residents and citizens of Florida only.** For anyone else, s 5(a) says nothing; the encoding answers `NOTHING` (no s 5(a) ceiling) rather than guessing. Asserted.
4. **The benefits half of Florida's sample** is the temporary cash assistance encoding at `../../../the-2026-florida-statutes-title-xxx-chapter-414-family-self/encodings/baseline-2026-10/`.

## Before relying on it

- Search the whole of the Florida Statutes for any tax measured by an individual's income (chapter 220 is corporate) and record the result.
- Federal law on credits for state income taxes is an IRC question (`subjects/us/internal-revenue-code-of-1986/`).
