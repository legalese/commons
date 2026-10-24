# Iowa Code chapter 422, subchapter II (personal net income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ia-income-tax.l4`) states the rules in the chapter's own actors and terms ("resident", "nonresident", "net income", "taxable income", "the individual", "the department"), with the return-and-pay duty and the 422.12C(2) bar written as regulative rules.
A **seat layer** (`ia-income-tax-seat.l4`) asks the taxpayer's questions, each with `@export` and a `@desc` on every input, built only from the core.
There is no REFUSE; a question that reaches a part not encoded answers `not covered` with the reason, and the cases assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

**Iowa Code 2026** (Legislative Services Agency; laws through the 2025 regular session; official PDFs stamped 9 December 2025), chapter 422 as deposited at `../../registers/source-bundle/ia-code-ch-422-2026.txt` (unofficial text converted from the Agency's XML, retrieved 2026-10-19). Acts of the 2026 session are not applied.
No instrument is brought in: every figure used (3.8%, 4.3%, $9,000 / $13,500, $24,000 / $32,000, the 422.12 credit amounts, 15%, the 422.12C bands) is fixed in the Code text itself. None of them is indexed by the 422.4(1) inflation factor.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ia-income-tax.l4` (core), `ia-income-tax-seat.l4` (taxpayer seat) | `ia-income-tax-cases.l4` | 46 written, 46 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.
Every expected value was worked by hand from the text before the run. One hand calculation was wrong (case I left out the $40 dependent credit); the encoding was right and the case comment was corrected.
Regulative rules: 2. `the 422.13 and 422.21 duty to make a return and pay` is asserted FULFILLED on a filing in time and `#TRACE`d with an `-- expect:` line for a late one; `the 422.12C(2) bar on claiming both credits` is asserted FULFILLED where the early childhood credit is not claimed and `#TRACE`d to a breach where it is. (A breached trace cannot be compared with `EQUALS` in the stable `l4`, so breaches are traced, not asserted.)

## Seat

**The individual taxpayer**: a person earning wages, a pension or other income, and the couple filing jointly. "Am I a resident? Must I file? By when? What is my net income? How much do I owe, or get back? What are my earned income and child care credits?"
Provisions addressed to the department or the director are encoded as what they mean for that person: the director's extension is extra days; the department's rules for nonresident allocation make that part `not covered`.

Defaults (2026-10-18):
- **The Act alone:** chapter 422, subchapter II, plus 422.21 and 422.24 from subchapter VI. Nothing needed from an instrument.
- **Actors the text names:** the individual (resident or nonresident), the department, the director.
- **Judgments left to others:** the director's further time for filing (422.21(1)) is an input.
- **Definitions:** "resident" (422.4(14)), "net income" (422.7, main adjustments), "taxable income" (422.4(15)) worked out; borrowed federal terms (federal taxable income under IRC s63, taxable social security under s86, the federal EIC under s32, the federal child care credit under s21, "dependent", "head of household", federal filing status) are asked as facts.
- **One case:** one return for one tax year.
- **Terms:** the Code's own, quoted above each rule.
- **Machinery out:** checkoffs, confidentiality, administration other than 422.21 and 422.24, the corporate and financial institution taxes.

## Read with the Internal Revenue Code encoding

Iowa starts from **federal taxable income** (IRC s63), not federal AGI (422.7), and uses the federal filing status (422.5(11)). The federal figures here are inputs; they are answered by `subjects/us/internal-revenue-code-of-1986/` (encoded by another session on 24 October 2026). Cross-folder IMPORT does not work in the stable `l4`, so the link is recorded here, not in code.

## Scope

**In:** 422.4(9), (14), (15); 422.5(1)(a), (2), (3), (11); 422.7 opening words and subsections 1, 2, 8, 19(a), 20, 29 (all other 422.7 adjustments are one input each way); 422.12(2)(a), (b); 422.12B; 422.12C(1), (2)(a), (3); 422.13(1), (2); 422.21(1); 422.24(1).

**Out, answering `not covered`:** married filing separately (422.5(2), (3), 422.13(2)); the tax of nonresidents and part-year residents (422.5(1)(b), 422.8(2)); the credit for tax paid to another state (422.8(1)); the combat-zone extension (422.21(2), IRC s7508(a)).

**Out, silently:** S corporation proration (422.5(1)(b)(2)); lump-sum distributions (422.5(7)); 422.5(6), (8)-(10); business and investment credits (422.10 to 422.11Z, 422.12N to Q); volunteer fire fighter and reserve peace officer credits (422.12(2)(c), (d)); the adoption credit (422.12A); 422.12C(4); the employer's withholding duties (422.16); estimated tax; penalties and interest (422.25).

## What the chapter turns out to say

1. **Iowa has a flat 3.8% tax on taxable income for tax years from 2025** (422.5(1)(a)); 422.5A, the old rate schedule, is repealed. There is no Iowa standard deduction or personal exemption deduction: the starting point, federal taxable income, already has the federal deduction taken out, and Iowa's personal exemption survives only as a credit against tax (422.12(2)(a): $40 or $80, $40 a dependent, $20 for 65 or older, $20 for blindness). Asserted (cases A to I).
2. **The low-income limits work on net income with the federal deductions added back** (422.5(2)(a), (3)(a)), so a single person with $12,000 of wages and a $12,000 standard deduction has $12,000 for the test, not $0. Above the limit the tax is cut so the person keeps the limit amount, and for joint filers, heads of household and surviving spouses it is never more than 4.3% of the excess (422.5(2)(b), (3)(b)). Asserted (cases D, E, G).
3. **A surviving spouse is not named in the personal exemption credit** (422.12(2)(a)(1) names a single individual and a married person filing separately; (2) a head of household and a joint return). The encoding gives the $40 amount. Whether a surviving spouse gets $40 or $80 should be checked against the department's rules.
4. **"The appropriate dollar amount" in 422.13(1)** is read as the 422.5(3) amount when the taxpayer or spouse is 65 or older, otherwise the 422.5(2) amount. Asserted.
5. **Two age tests.** 422.5(3) asks whether the person is 65 "on December 31 of the tax year"; 422.12(2)(a)(4) whether they attained 65 "before the close of the tax year or on the first day following". A person whose 65th birthday is on 1 January after the year gets the $20 credit but not the 422.5(3) limit. The seat asks age on December 31, so it misses that one-day case.
6. **Married filing separately.** 422.5(2)(b) gives the 4.3% alternate tax to the joint, head of household and surviving spouse group, then says separate filers "shall compute the alternate tax ... using the total net income of the spouses". Which separate filers get it is not clear from the text, so separate filing is `not covered`.
7. **The pension subtraction (422.7(19)) has no dollar cap** for a person who is 55 or older, disabled or a qualifying survivor; a spouse's pension on a joint return is subtracted only if that spouse qualifies. Asserted. The age is read as the age in the tax year; the subsection does not say when it is measured.
8. **No rounding** is stated for the tax or the credits in chapter 422; none is applied.
9. **Paying is part of filing.** 422.24(1) makes the total tax due payable "at the time of filing the return", so the duty is encoded as one act, filing and paying, due on the last day of the fourth month after the tax year (30 April for a calendar year). Asserted for calendar and fiscal years, including a leap-year February.

## Before relying on it

- An independent test pass, and a check of the cases against the department's IA 1040 for tax year 2025.
- The 2026 session Acts applied.
- The nonresident and part-year proration, the out-of-state credit and separate filing encoded, from the department's rules (IAC 701), which are not deposited.
- The IRC encoding's federal taxable income, s86, s32 and s21 figures fed in, once a cross-folder import exists.
