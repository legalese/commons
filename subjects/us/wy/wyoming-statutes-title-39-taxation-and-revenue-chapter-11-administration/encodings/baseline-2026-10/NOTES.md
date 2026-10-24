# Wyoming refund for the elderly and disabled (W.S. 39-11-109(c)) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the Wyoming resident aged 65 or over or totally disabled, with the design defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

Wyoming has no income tax (see the encoding at `../../../wyoming-statutes-title-39-taxation-and-revenue-chapters-7-and-12-income-tax/encodings/baseline-2026-10/`). This refund, "a refund and partial exemption of taxes paid under the sales and use taxes, property tax relief and utility or energy cost relief" (39-11-109(c)(v)), is the income-tested tax provision a Wyoming individual meets, so it is the tax half of Wyoming's tax-and-benefits sample.

## Edition

The Legislative Service Office's title 39 PDF (created 2026-10-14), downloaded 2026-10-19, as deposited at `../../registers/source-bundle/wy-stat-39-ch11.txt` (unofficial). Only W.S. 39-11-109(c) is encoded.

**Inputs.** The asset ceiling per adult ($25,000 printed, "adjusted annually by the state average Wyoming cost-of-living index", (c)(vii)) and the appropriation fraction ((c)(viii)(A), set each fiscal year from the appropriation and total claims).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wy-elderly-disabled-refund.l4` | `wy-elderly-disabled-refund-cases.l4` | 20 written, 20 satisfied |

Plus three `#TRACE`s of the application rule with `-- expect:` comments (two FULFILLED, one breach by the department of health, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The applicant**: a Wyoming resident aged 65 or over, or 18 or over and totally disabled. Questions: "Do I qualify?", "How much will I get?", and, as a rule with deadlines, "By when must I apply, and by when must the refund be sent?". The department of health's duty to mail the warrant by December 20 is encoded as what the applicant must be given.

Defaults (2026-10-18): the Act alone (the department of health's rules under (c)(vi) are not deposited); the actors it names; the department's determinations of "income" beyond the listed items and of household assets by rule are asked as facts; one case is one application for one year.

## Scope

**In:** W.S. 39-11-109(c)(i)(C), (D), (F); (c)(ii); (c)(iii)-(iv) (a rule: the application by the last working day in August, then the warrant by December 20); (c)(vii); (c)(viii).

**Out:** the rest of W.S. 39-11-109 and of chapter 11; the property tax exemptions and refunds of chapter 13 (39-13-105, 39-13-109), which are asked only as the amount that reduces this refund.

## What the law turns out to say

1. **The refund is $800 for a single person and $900 for a married couple, scaled down as income rises, and nil at $17,500 or $28,500.** Asserted.
2. **"Reduced by the percentage that his actual income exceeds ten thousand dollars" is read as (income − $10,000) ÷ $10,000.** A single person with $12,000 gets $640; with $17,000, $240. For a couple the base is $16,000, so at $28,000 the refund is $225. The words could be read otherwise, but on this reading the refund stays positive right up to the income limits, which fits them. An interpretive choice, asserted.
3. **Income includes the benefits a person may also be getting**: "public assistance payments, unemployment compensation, federal social security payments, veteran's benefits and disability payments" ((c)(i)(C)). So POWER (`../../../wyoming-statutes-title-42-welfare-chapter-2-public-assistance/encodings/baseline-2026-10/`), unemployment and Social Security reduce this refund.
4. **Last year's property tax relief comes off the refund** ((c)(viii)), and the whole refund is scaled by the appropriation fraction, never above the (c)(ii) amount. Asserted.
5. **Residence needs a full year and no claim of residence elsewhere** ((c)(i)(D)). Asserted.
6. **The application is the person's choice; the warrant is the department's duty.** Apply by the last working day in August, under oath, with last year's federal return or a statement that none was required; the department "shall" mail warrants by December 20. Written as `DO … LEST FULFILLED` with the department's `MUST` under `HENCE`. Traced.

## Before relying on it

- Deposit the department of health's rules for the refund (the income and asset definitions) and the current asset ceiling.
- An independent test pass.
