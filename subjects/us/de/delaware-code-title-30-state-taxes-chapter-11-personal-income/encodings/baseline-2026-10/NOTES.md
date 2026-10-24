# Delaware Code Title 30, chapter 11 (Personal Income Tax): the resident individual — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the resident taxpayer, with the design defaults ruled on 2026-10-18.
No REFUSE: nonresidents, part-year residents and years before 2022 answer `not covered`, asserted.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

The Delaware Code Online, Title 30, chapter 11, whose notice says it "includes all acts enacted as of September 10, 2026, up to and including 85 Del. Laws, c. 518", deposited at `../../registers/source-bundle/de-code-t30-ch11-2026-09-10.txt` (retrieved 2026-10-19 from delcode.delaware.gov). Every figure used is in the statute: the rates, the standard deduction, the $110 credits, the pension limits by year, the filing thresholds and the EITC percentages. The Director's tax tables (s 1102(d)) are not deposited, so the tax is worked from the rates.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `de-income-tax.l4` | `de-cases-income-tax.l4` | 48 written, 48 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). One `#TRACE` ends in a breach, with an `-- expect:` line; it was read and matches. Expected values were worked by hand, with the working above each assertion.

## Seat

**The individual taxpayer resident in Delaware** (alone, or with a spouse on a joint return). Questions: "Am I a resident?", "Must I file?", "Must we file separately?", "How much of my pension is subtracted?", "What is my standard deduction?", "What is the tax on my taxable income?", "How much do I owe?", "Which EITC option is better for me?", "By when must I file and pay?".

The Department of Finance (Division of Revenue) appears only as where the return is filed and the tax paid.

The 2026-10-18 defaults:

- **The Act alone.** Chapter 11 only; the penalties and interest are in 30 Del. C. ch. 5, not deposited, and are named in the breach message only.
- **Actors:** the resident individual, resident spouses, the Department of Finance.
- **Judgments handed to others:** none needed in scope.
- **Definitions:** "resident individual" (s 1103), Delaware adjusted gross income (s 1105 with s 1106(b)(2) to (4)), the standard deduction, the s 1106(b)(3) subtraction, "legally domiciled" (f.4.B, by s 1103) are worked out from facts. Borrowed federal terms are asked: federal AGI, the Social Security included in it (IRC s 86), the number of federal personal exemptions, whether a federal return is required, the federal EIC.
- **Departure:** the s 1106(a) additions and the other s 1106(b) subtractions are asked as two totals; itemized deductions (s 1109) are asked as a total.
- **One case:** one return for one calendar year.
- **Machinery out:** the check-off funds (subchapter IX), the DE529 procedures, withholding by employers.

## Read with the federal encodings

`subjects/us/internal-revenue-code-of-1986/` (a baseline being written on 2026-10-24 by another session): federal AGI (IRC s 62), the taxable Social Security benefits (IRC s 86), personal exemptions (IRC s 151), who must file federally (IRC s 6012), the earned income credit (IRC s 32). s 1101 gives every term its federal meaning, with rolling conformity ("as the same may have been or shall become effective"). The stable `l4` cannot IMPORT across subject folders, so the link is recorded here.

## Scope

**In:** s 1102(a)(14); s 1103; s 1105; s 1106(b)(2), (b)(3)b. to f., (b)(4); s 1107; s 1108(a)(3), (b); s 1110(b), (c); s 1117(a)(2), (b) (as the choice of option); s 1161(1); s 1162(a)(1) to (3); s 1168.

**Out:** subchapter III (nonresidents) and s 1165 (part-year): `not covered`; years before 2022: `not covered`; fiscal years; estates and trusts; s 1102(b) lump-sum tax; s 1102(d) tables; s 1106(a) and the other (b) items (inputs); s 1109 (input); credits in ss 1111 to 1114 and 1118; s 1162(a)(4), (b); withholding and estimated tax; penalties.

## What the chapter turns out to say

1. **The chapter states the filing thresholds itself.** A resident must file if required to file federally, or if single with Delaware AGI "more than $9,378", or if married and entitled to file jointly with combined Delaware AGI "more than $15,449" (s 1161(1)). These are fixed figures, not indexed. Asserted at $9,378 / $9,379 and $15,449 / $15,450.
2. **No rate is set on the first $2,000 of taxable income.** s 1102(a)(14) begins at "2.2% of taxable income in excess of $2,000": the first $2,000 bears no tax. The Director's tables for taxable income up to $60,000 (s 1102(d)) are "computed on the basis of the rates", so they may differ from this encoding by rounding. Asserted ($1,500: nil; $5,000: $66).
3. **A military pension is also a pension "from ... the United States".** s 1106(b)(3) lists "pensions from employers, the United States, this State, or any subdivision" and, separately from 2022, "a United States military pension". This encoding counts a military pension in the first list too, so a person 60 or older in 2022 to 2026 gets up to $12,500 on it, and a person under 60 the greater of $2,000 or the military limit. From 2027 the military limit rises ($15,000; $20,000 in 2028; $25,000 from 2029) for both age groups. Asserted.
4. **The low-income subtraction says "over 60 years of age"; the pension subtraction says "age 60 or older".** The encoding reads both as 60 or more. On a joint return where only one spouse qualifies, s 1106(b)(2) gives no rule; this encoding applies the single-person rule to that spouse with the joint AGI. Both interpretive. Asserted.
5. **On a joint return, each spouse is read as "the taxpayer" for the $2,500 age and blindness additions.** s 1108(b)(2) and (4) cover a spouse only where "a joint return is not made" or "a separate return is made". Without this reading, an older spouse on a joint return would get nothing. Asserted (joint, both 66: $11,500).
6. **The age tests in ss 1106 and 1110 name no date.** s 1108(b)(1) says "before the close of the taxable year"; the others do not. This encoding takes every age at the close of the year.
7. **The EITC is a choice, and the refundable option wins when the tax is small.** s 1117(a)(2) lets the resident "claim either" 20%, capped at "the tax otherwise due", or 4.5%, with the excess refunded. This encoding reads "the tax otherwise due" as the tax after the s 1110 personal credits (the order of credits is not stated) and picks the option with the lower balance. Asserted (tax $125, federal EIC $4,000: option b, -$55; tax $1,000, EIC $1,000: option a).
8. **The personal credit counts federal personal exemptions, whatever their federal dollar value.** s 1110(b)(1) gives $110 "for each personal exemption to which such individual is entitled for the taxable year for federal income tax purposes". The number is an input. Whether the federal exemption amount being nil affects the count is an IRC question for the federal encoding.
9. **The over-60 pension subtraction needs years of residence.** s 1106(b)(3)f.4: at least 3 years of domicile for those domiciled before 1 January 2027, and 5 years for those who come later; "legally domiciled" means a resident under s 1103. Asserted (2 years: nil; 5 years after 2027: $12,500).
10. **Late filing and payment have no consequence in this chapter.** s 1168 fixes the 30 April date; the penalties and interest are in chapter 5 of Title 30, which is not deposited. The rule is traced to its breach.

## Before relying on it

- Deposit 30 Del. C. ch. 5 (administration, penalties, interest, refunds) and encode them with s 1168.
- Encode s 1106(a) and the remaining (b) items, and s 1109, so the person states federal figures only.
- Nonresidents and part-year residents.
- Compare with the Division of Revenue's tax tables (finding 2).
- An independent test pass.
