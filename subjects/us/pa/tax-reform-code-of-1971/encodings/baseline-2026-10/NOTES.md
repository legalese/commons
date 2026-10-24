# Tax Reform Code of 1971, Article III (Pennsylvania personal income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18.
The core, `pa-pit.l4`, is written in Article III's own actors and terms and takes no seat. The duties to file a return and to pay (ss 330(a), 332) are regulative rules (`PARTY … MUST … WITHIN … LEST BREACH`), and the claimant's right to claim Tax Forgiveness with the return (s 336.1) is a `MAY`. The computations (the tax, the credit for tax paid to another state, the share forgiven, the balance) are functions.
The seat layer, `pa-pit-seat.l4`, asks the taxpayer's questions, each with `@export` and a `@desc` on every input. It calls the core and restates no rule.
There is no REFUSE. A part-year resident answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

There was no earlier encoding of this Act.

## Edition

The Tax Reform Code of 1971 (Act of Mar. 4, 1971, P.L. 6, No. 2) as served by the Pennsylvania General Assembly at palegis.us on 24 October 2026, deposited whole at `../../registers/source-bundle/pa-1971-act-2-tax-reform-code.txt`. Article III, Personal Income Tax, is at lines 4863–7640. The page gives no "current through" date. The latest amendment notes in the text are from December 2025.

Nothing else is brought in. Article III sets its figures in the text itself (the 3.07 per cent rate, the s 304 limits and bands), and none of them is indexed, so no annual publication is needed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `pa-pit.l4`, `pa-pit-seat.l4` | `pa-pit-cases.l4` | 35 written, 35 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE` breach checks (no return by the due date, and payment after it) were read as `BREACH` by the taxpayer, as their `-- expect:` comments say. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**, resident or nonresident for the whole year, including the claimant for the special tax provisions for poverty ("Tax Forgiveness" on the return). Questions: "Am I a Pennsylvania resident?", "Must I file?", "How much tax is imposed on me?", "What share of my tax is forgiven?", "What is the most poverty income I can have for full forgiveness?", "What credit do I get for tax paid to another state?", "What do I still owe, or get back?".

The department's duties (assessment, regulations, proof of eligibility under s 336.2) appear only as what they mean for the person.

Defaults:
- **The Act alone.** Article III only. No regulation is brought in. 61 Pa. Code (the department's regulations) is not deposited.
- **The actors the text names:** the taxpayer, the claimant, the department.
- **Judgments left to others:** none arises in the encoded sections. The annualising of a short year under s 304(d)(3) is "in such manner as the department may prescribe" and is out of scope.
- **Definitions worked out from facts:** resident individual (s 301(p)), married claimant (s 304(d)(1)(i)–(ii)), claimant (s 301(c.2)). **Borrowed terms asked as facts:** dependent under IRC s 151 (ss 301(c.2), (e.1)), and the day the federal return is due (s 330(a); IRC s 6072, not deposited). Also asked as facts: what falls in each class of s 303, the Pennsylvania-source amounts for a nonresident (s 301(k)), and the amount of "poverty income" (s 301(o.2)), whose exclusions are listed in the `@desc`.
- **One case:** one individual and one taxable year. For Tax Forgiveness, a married claimant's poverty income is the joint figure, as s 304(d)(1) says.
- **Terms:** the Act's own ("classes of income", "special tax provisions", "poverty income"), each glossed.
- **Machinery out:** the contribution check-offs, regulations powers, transfers of funds, effective dates.

## Read with

`subjects/us/internal-revenue-code-of-1986/` (federal), for IRC s 151 dependants and the federal return due date, which are inputs here. Pennsylvania does **not** start from federal AGI: it taxes its own eight classes, so nothing else from the IRC is needed. Cross-folder IMPORT is not possible in the stable `l4`, so the link is recorded here, not in code.

## Scope

**In:** s 301(c.2), (e.1), (m), (o.2) (as a fact), (p), (s.1); s 302(a), (b); s 303(a) (one amount per class); s 304(d)(1), (2); s 312; s 314(a), (b); s 330(a); s 332; s 336.1(1).

**Out:** part-year residents (`not covered`); estates and trusts (s 305) and partnerships and S corporations (ss 306–307.21); the sourcing rules for nonresidents (s 301(k)), taken as a fact; s 304(d)(3); employer withholding (ss 316–324.5) and estimated tax (ss 325–326), which appear only as one payments input; returns of married, deceased or disabled persons (s 331); extensions (s 334); assessment, refunds, interest, penalties and crimes (ss 337–353); the check-offs (ss 315–315.14).

## What the Act turns out to say

1. **Every taxpayer with any income must file, however little.** Section 330(a) requires a return "by or for every taxpayer having income for the taxable year", and Article III has no filing threshold. A student with $10 of interest must file. A person whose only "income" is a net business loss has no income in any class and need not. Asserted.
2. **A loss in one class does not reduce income in another.** Section 302(a) taxes "each dollar of income received" in "each of the classes of income" of s 303. Each net class (net profits, net gains from property, rents and royalties, estate and trust income) is computed net of its own losses ("Net gains or net income, less net losses", s 303(a)(3)), but nothing in Article III lets a net loss carry from one class to another. The encoding therefore counts a class with a net loss as nothing. A wage-earner with a $3,000 loss on shares pays tax on all of their wages (50,200 × 3.07% = $1,541.14). This reading rests on the structure of the text: no sentence states it expressly. Asserted.
3. **One flat rate, with no personal exemption and no standard deduction.** The tax is "three and seven hundredths per cent" on each dollar (s 302(a), (b)). The only relief for a low income is the special tax provisions for poverty. Asserted.
4. **Tax Forgiveness is a cliff in ten steps of $250.** It is all forgiven up to $6,500 of poverty income ($13,000 joint for a married claimant), plus $9,500 for each dependent child. Above that, it falls by ten points for each $250 or part of $250, and nothing is forgiven from $2,250.01 over the limit (s 304(d)(1), (2)). Each band is "not in excess of", so a figure exactly on a boundary takes the higher percentage: $500 over gives 80 per cent, and $2,250 over gives 10 per cent. Asserted.
5. **Married means married unless both conditions hold.** A married claimant is treated as unmarried only if the spouses file separate returns **and** either lived apart for the whole of the last six months of the year or are separated under a written agreement (s 304(d)(1)(i), (ii)). Spouses who file separately but live together are still married, and their joint poverty income is tested against $13,000. Asserted.
6. **A person who can be claimed as someone else's dependent gets no Tax Forgiveness.** "Claimant" excludes "a dependent of another taxpayer for purposes of section 151" of the IRC (s 301(c.2)), so a student whom her parents claim pays the full tax however low her income. Asserted.
7. **"Poverty income" is broader than taxable income in one direction and narrower in another.** It counts "all moneys or property ... received of whatever nature", including tax-exempt interest, but leaves out Social Security, retirement benefits, unemployment compensation, public assistance and workers' compensation (s 301(o.2)). The person states the figure. The encoding does not derive it from the classes of income.
8. **The order of the credits is partly a reading.** Section 314(a) says the other-state credit is allowed "before allowance of any credit under section 312" (withholding). Section 304 forgives a share of "any moneys which have been paid over to (or would ... be payable to) the Commonwealth". The encoding applies the forgiven share to the tax after the s 314 credit and before withholding, so forgiven tax that was withheld comes back. Single parent, two children, $26,000: tax $798.20, 80 per cent forgiven, so $638.56 of the $798.20 withheld comes back. The text does not fix the order of s 304 and s 314. Asserted as encoded, not as settled law.
9. **The other-state credit is capped by proportion.** The credit cannot exceed the Pennsylvania tax multiplied by the share of the taxpayer's income that the other state taxed (s 314(b)). It is for residents only. Asserted.
10. **An extension to file does not extend the time to pay.** Tax is due "on or before the date fixed for filing such return (determined without regard to any extension of time for filing the return)" (s 332). Traced: a payment 45 days after the due date is a breach.
11. **There is no state earned income tax credit or child credit in the deposited text.** Article III has neither. The only reference to the federal EITC is s 304.1, which directs a study comparing it with Tax Forgiveness. The whole Act, as served on 2026-10-24, has no refundable personal credit of either kind. A "Working Pennsylvanians Tax Credit" is said to have been enacted in 2025 (unverified (general knowledge)). If it exists, it is not in this text, or it is in another Act. That needs checking before this encoding is relied on.

## Before relying on it

- An independent test pass, and a check of finding 2 and finding 8 against the department's regulations (61 Pa. Code ch. 101 onward, not deposited) and case law.
- The rules for part-year residents, and for nonresident sourcing.
- Confirm whether any refundable credit for working families was enacted after the text served on 2026-10-24 (finding 11).
