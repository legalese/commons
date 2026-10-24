# Kansas income tax act (K.S.A. 79-32), individuals — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18 and the brief of 24 October 2026 for US tax and benefits.
A **seat-neutral core** (`ks-income-tax.l4`) states the rules in the act's own actors and terms (resident individual, Kansas adjusted gross income, Kansas deduction, Kansas personal exemptions, Kansas taxable income, the individual, the director of taxation), with the filing and payment duties as two regulative rules.
A **seat layer** (`ks-income-tax-seat.l4`) asks the taxpayer's questions, each with `@export` and a `@desc` on every input, built only from the core.
No REFUSE; parts not encoded answer `not covered`, asserted. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

## Edition

Kansas Statutes as published online by the Office of Revisor of Statutes, read 2026-10-20 ("amendments and new laws enacted during the 2025 legislative session"), deposited at `../../registers/source-bundle/ksa-79-32-individual-income-tax.txt` and `ksa-79-32-individual-credits-eitc-safesr-food.txt` (retrieved 2026-10-19 UTC). Unofficial: the authenticated K.S.A. are the printed volumes. 2026 session laws are not checked.
No instrument is brought in: every figure (5.2% / 5.58%, the $23,000 / $46,000 bands, the standard deductions, the exemptions, 17%, 50%, 75%) is in the act. The federal poverty level for SAFESR is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ks-income-tax.l4` (core), `ks-income-tax-seat.l4` (taxpayer seat) | `ks-income-tax-cases.l4` | 46 written, 46 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Expected values worked by hand before the run.
Regulative rules: 2 (filing, payment). Each asserted FULFILLED when kept and `#TRACE`d to a breach, with an `-- expect:` line, when late.

## Seat

**The individual taxpayer**, resident or not, single, joint or head of household. "Am I a Kansas resident? Must I file? When are my return and my tax due? What is my Kansas AGI and taxable income? How much do I owe, or get back? What are my earned income and senior property tax credits?"
The director of taxation's powers (to extend payment) are inputs: months of extension.

Defaults (2026-10-18):
- **The act alone**; nothing needed from an instrument.
- **Actors the text names:** the individual, the director of taxation, the secretary of revenue.
- **Judgments left to others:** "proof to the contrary" of residence; the director's payment extension; the secretary's 79-32,110c rate certification (an input that makes the answer `not covered`).
- **Definitions:** resident individual, Kansas AGI (main modifications), Kansas deduction, exemptions, taxable income worked out; federal AGI, the federal filing requirement, federal dependents, federal additional standard deductions, IRC s32 and s21 credits, household income and the poverty level asked as facts.
- **One case:** one return for one taxable year.
- **Machinery out:** corporate, fiduciary and partnership provisions, tax tables, electronic filing by preparers.

## Read with the Internal Revenue Code encoding

Kansas starts from **federal adjusted gross income** (79-32,117(a)). Federal AGI, the IRC s32 earned income credit, the IRC s21 child and dependent care credit, federal dependents and the federal additional standard deduction count are inputs, answered by `subjects/us/internal-revenue-code-of-1986/` (encoded by another session, 24 October 2026). Cross-folder IMPORT does not work in the stable `l4`; the link is recorded here.

## Scope

**In:** 79-32,109(b); 79-32,110(a)(1)(B), (a)(2)(B), (b) (and 79-32,110b's identical schedules); 79-32,111c(a), (b); 79-32,115 (as filing status); 79-32,116; 79-32,117(a), (b)(i), (c)(i), (ii), (vii), (xviii)(B) (other modifications one input each way); 79-32,118; 79-32,119; 79-32,120(a)(1)(B), (a)(5), (b); 79-32,121(a); 79-32,121b(a), (b)(1); 79-32,128(b) (as Kansas-source input); 79-32,205; 79-32,263; 79-32,265; 79-3220(a)(1), (3); 79-3221(b), (c)(3); 79-3225(a), (b).

**Not covered (asserted):** tax years before 2025; married filing separately; the credit for tax paid to another state (79-32,111(a)); a 79-32,110c rate reduction; the 100% disabled veteran's exemption.
**Out:** lump-sum distributions (79-32,110a); the combat-zone rules (79-3221(d) to (j)); 79-32,128(a)'s resident election for part-year residents; the business credits limited by 79-32,264.

## What the act turns out to say

1. **Two rate sections, one schedule.** 79-32,110 and 79-32,110b (both amended by 2025 Acts, "[See Revisor's Note]") print identical individual schedules for 2024 on: 5.2% up to $23,000 ($46,000 joint) and 5.58% above. They differ only in whether the rates are "modified pursuant to" 79-32,110c, the 2025 trigger by which the secretary of revenue reduces rates when revenues exceed an inflation-adjusted base and the budget stabilization fund is at 15%. A year with a published reduction answers `not covered`. Asserted.
2. **Two exemption sections, not reconciled.** 79-32,121 (L. 2025, ch. 112) and 79-32,121b (L. 2025, ch. 123) both give $18,320 joint, $9,160 otherwise and $2,320 a dependent. 79-32,121 adds $2,320 for an unborn child (a dependent born in the year, or a stillbirth with a certificate); 79-32,121b adds $2,320 for a head of household. The encoding counts the base once and applies both additions. For a 100% disabled veteran they conflict ($2,250 against $2,320), so that case is `not covered`. Both readings should go to Michael; the Revisor's Note (not deposited) may settle it.
3. **Social security is fully subtracted from 2024** (79-32,117(c)(xviii)(B)), with no income cap. Asserted.
4. **The order of credits.** 79-32,111c(b) caps the care credit at "the tax ... reduced by the sum of any other credits allowable". Read literally, that includes the refundable EITC and SAFESR, which would shrink or remove the care credit whenever they cover the tax. The encoding applies the non-refundable care credit to the tax first and the refundable credits after it. On case F's facts (tax $520, care credit $600, EITC $85) the encoding gives an $85 refund; the literal reading would cap the care credit at $435 and give $0. This should be checked against the department's form order.
5. **Filing and paying have different clocks.** A federal (IRS) extension moves the Kansas filing date (79-3221(c)(3)) without any Kansas request, but not the payment date: tax is due on the 15th day of the fourth month (79-3225(a)) unless the director extends it, by up to six months. Asserted.
6. **A balance under $5 is canceled** (79-3225(a): "When the tax as shown to be due on a return is less than $5, such tax shall be canceled"). Asserted (case B).
7. **The food sales tax credit has ended**: 79-32,271 applies only to taxable years "ending prior to January 1, 2025". It is not encoded.
8. **Credits need valid social security numbers** for the filer, spouse and every dependent (79-32,265), except the credit for tax paid to another state. Asserted (case C).
9. **The standard deduction for a married person filing separately is not stated**: 79-32,119(c)(2) gives $8,240 for "married filing status" and (d) speaks of separate returns only for the federal additional amount. Separate filing is `not covered`.

## Before relying on it

- An independent test pass; the cases checked against form K-40 for 2025.
- The Revisor's Notes on 79-32,110 / 110b and 79-32,121 / 121b read, and findings 2 and 4 settled.
- 2026 session laws checked.
- Whether any 79-32,110c reduction was certified for 2026.
