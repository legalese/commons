# Code of Alabama 1975, Title 40, Chapter 18 (individual income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
The core rules are written in the Code's own actors and terms; the taxpayer's questions (`@export`, `@desc`, under `§ Questions for the taxpayer`) are derived from them and restate nothing.
Where the Code states a duty with a time (file, pay, hand in a Form A-4, give a wage statement), it is a regulative rule with the party as a parameter.
There is no REFUSE; a case outside the encoding answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for use as tax advice.**

This is part of the US "tax and benefits" sample for Alabama (24 October 2026). The benefits half is `../../../code-of-alabama-1975-title-38-chapters-1-and-4-public-assistance/encodings/baseline-2026-10/`.

## Edition

The Code of Alabama 1975 as ALISON served it on 2026-10-20, deposited at:

- `../../registers/source-bundle/ala-code-40-18-art1.txt` (Article 1, ss 40-18-1 to 40-18-62)
- `../../registers/source-bundle/ala-code-40-18-art2-div1.txt` (Article 2 Division 1, ss 40-18-70 to 40-18-86)

ALISON gives no "current through" date. Its own notes flag ss 40-18-14 and 40-18-15 as amended by Acts not yet reflected (findings 1 and 2).
No annually set figure is needed: Alabama's brackets, standard deduction and exemptions are fixed in the statute, not indexed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `al-income-tax.l4` | `al-income-tax-cases.l4` | 43 written, 43 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). The case file also has four `#TRACE`s, each with an `-- expect:` comment that matched the output (a breached trace satisfies neither an assertion nor its negation, so breaches are checked this way).
Every expected value was worked out by hand from the text.

## Seat

**The individual Alabama taxpayer**, who is also, for withholding, an employee. The questions are the ones that person asks: "Am I an Alabama resident?", "Must I file?", "What is my standard deduction?", "What are my exemptions?", "Is my severance pay exempt?", "How much do I owe?", "By when must my employer give me my wage statement?".
The employer appears only as a party to the regulative rules (s 40-18-73(c), s 40-18-75); there is no employer seat.

The 2026-10-18 defaults, all followed:

- **The Act alone.** Chapter 18 only. No instrument sets a number it needs.
- **The actors the text names:** the taxpayer, the employee, the employer, the Department of Revenue.
- **Judgments left to others** are asked as facts: whether a termination was due to misconduct (s 40-18-19.1(d)), whether a person is a dependent.
- **Definitions** worked out where Chapter 18 gives them (taxable income, s 40-18-15.1; the residence presumption, s 40-18-2(b)). Borrowed and item-by-item terms are stated by the person as figures: Alabama adjusted gross income (s 40-18-14.2), itemised deductions (s 40-18-15(a)), federal income tax paid or accrued (s 40-18-15(c)), taxable retirement income (s 40-18-19(a)(13)), head of family (26 U.S.C. 2(b), via s 40-18-1(15)).
- **One case:** one return for one tax year (a joint return is one case).
- **The Code's own terms**, quoted above each rule.
- **Machinery out:** rule-making powers (ss 40-18-19(c), 40-18-57), appropriations, inspection of returns.

## Read with the federal encoding

Alabama starts from its own gross income, not from federal AGI, but borrows the Internal Revenue Code item by item, and lets the taxpayer deduct federal income tax (s 40-18-15(c)). Both figures are inputs here. The federal encoding is `subjects/us/internal-revenue-code-of-1986/` (being encoded on 2026-10-24 by another session); the stable `l4` cannot IMPORT across folders, so the link is recorded here only.

## Scope

**In:** s 40-18-2(a)(1), (b); s 40-18-5; s 40-18-15(b)(1) (the election), (b)(4), (c); s 40-18-15.1; s 40-18-19(a)(8), (9)a, d, e, (13); s 40-18-19.1(b), (d); s 40-18-27(a), (c); s 40-18-42(a); s 40-18-50; s 40-18-73(a), (c), (g); s 40-18-75(a).

**Out:** ss 40-18-14 and 40-18-14.2 (gross income and AGI item by item: an input); s 40-18-15(a) item by item (one total); s 40-18-15(b)(1)-(3) and s 40-18-19(a)(9)b, c (the tables for earlier years: a tax year before 2022 answers `not covered`); nonresidents (ss 40-18-15(e), 40-18-19(b) prorate: `not covered`); the other exemptions of s 40-18-19(a) (state and federal pensions, defined-benefit plans, firefighters and peace officers, PACT, ABLE, foreign housing, National Guard from 2027): they reduce gross income and are left to the AGI the person states; the credits (s 40-18-21 and Article 4B, not deposited); estimated tax (s 40-18-80, which borrows 26 U.S.C. 6654); withholding amounts (s 40-18-71, set by the department's tables); corporations, estates, trusts and pass-through entities.

## What the Code turns out to say

1. **Section 40-18-14 is flagged as amended by Act 2026-551 (effective 1 May 2026), and the deposited text may not include it.** The encoding takes Alabama AGI as an input, so no rule here reads s 40-18-14; but the person's figure must follow the amended section.
2. **Section 40-18-15 is flagged as amended by Act 2026-604 (effective 1 October 2026).** The standard deduction table of s 40-18-15(b)(4) and the federal income tax deduction of s 40-18-15(c) are encoded as deposited. If Act 2026-604 changed either, the answers for 2026 onward are wrong. Read the Act before relying on them.
3. **"Reduced further by $25 for each $500 of adjusted gross income in excess of $25,500" is read as each complete $500.** At $25,999 the single deduction stays $3,000; at $26,000 it is $2,975. The text does not say how a part of $500 is treated; the department's published tables (not deposited) would settle it. Asserted.
4. **Paragraphs (9)b and c (2007 onward) and (9)d and e (2022 onward) overlap; the encoding applies d and e from 2022.** Neither pair says it replaces the other. For AGI between $20,000 and $50,000, c gives $500 and d gives $1,000. Reading the later, more specific paragraphs as governing gives $1,000 up to $50,000, $500 to $100,000, and, above $100,000, where neither d nor e applies, the $300 of paragraph a, which was never repealed. Asserted (AGI $100,001: $300).
5. **The $6,000 retirement income exemption is per individual taxpayer aged 65 or over.** On a joint return the encoding allows it to each spouse who is 65 or over, each against that spouse's own retirement income. The text says only "individual taxpayers". It is taken off after AGI, with the other s 40-18-19 exemptions, so it does not move the AGI bands of the standard deduction or the dependent exemption. Asserted (case F).
6. **Residence is a presumption.** Section 40-18-2(b) says such persons "shall be presumed to be residing within the state"; the question answers the presumption, not residence itself. "More than seven months": seven exactly does not raise it. Asserted.
7. **The filing threshold uses the standard deduction, which itself depends on AGI.** Section 40-18-27(a) compares gross income with "the allowable standard deduction ... and the personal exemption ... as allowed for his or her respective filing status". The encoding takes the standard deduction at the person's AGI, and no dependent exemption. Asserted (single $5,000: must file; joint $11,000: need not).
8. **The personal exemption is read by filing status.** A joint return gets $3,000; two spouses living apart would each have $1,500, which is the same total. Married filing separately is always $1,500 ("each spouse must claim ... $1,500").
9. **No state earned income credit or child credit** appears in the deposited Article 1. The deposited text has no exemption naming Social Security benefits; whether they are taxed turns on s 40-18-14, which is pending amendment, and is not encoded.
10. **Alabama lets individuals deduct federal income tax paid or accrued** (s 40-18-15(c)), whether or not they itemise. Asserted in cases A to F.
11. **Failing to file in time is a misdemeanour**, fined $10 to $1,000 (s 40-18-50). It is the `LEST` of the filing duty. Asserted by trace.
12. **An employee who gives no Form A-4 is not in breach of anything with a penalty;** the consequence is that "the employer must withhold ... using no exemptions" (s 40-18-73(c)). That duty has no time, so it stays owed until done. Inflating exemptions carries a $500 penalty (s 40-18-73(a), s 40-29-75, the latter not deposited). Traced.
13. **The wage statement is due by 31 January of the next year, or within 30 days of the last payment if the job ended during the year** (s 40-18-75(a)). The department may extend by up to 30 days ((c)); an extension is not modelled. Asserted.

## Before relying on it

- Read Acts 2026-551 and 2026-604 and deposit them; recheck the standard deduction and the AGI rules.
- Settle the "for each $500" rounding against the department's tables.
- Add nonresidents and part-year residents (the proration of ss 40-18-15(e) and 40-18-19(b)).
- An independent test pass.
