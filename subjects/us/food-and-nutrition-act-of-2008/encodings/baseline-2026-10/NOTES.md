# Food and Nutrition Act of 2008 (SNAP): baseline encoding for the household applying

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A day with no deposited figures, or a household outside the 48 contiguous States and DC, answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`snap-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms ("the household", "the State agency", "an individual"). Computations (income, deductions, tests, the allotment, the time limit) are functions. Where the text says "shall" or sets a deadline, there is a regulative rule (`DEONTIC`): six in all.
- **`snap-seat.l4`**, the applicant's seat. It asks 16 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed to keep. No requirement ledger covers the US, so no ledger line is closed.

## Edition

- **Statute:** 7 U.S.C. chapter 51 (ss 2011–2036d), from the Office of the Law Revision Counsel's USLM XML at release point **Public Law 119-121 (current through 9 October 2026)**, as deposited at `../../registers/source-bundle/usc07-ch51.txt`. The text includes the amendments made by Pub. L. 119-21 (4 July 2025) to ss 2012, 2014 and 2015.
- **Annual figures:** the USDA Food and Nutrition Administration's *SNAP Cost-of-Living Adjustment (COLA) Information*, FY 2027 (effective 1 October 2026 to 30 September 2027), as deposited at `../../registers/source-bundle/fna-snap-cola-fy2027.txt` and recorded in `../../registers/annual-figures.json`. They are encoded as **one dated table**, `FY 2027 figures`, and `the SNAP figures in force on` a day returns them only for a day in FY 2027. For any other day, the answer is `not covered`. Only the column for the 48 States and DC is encoded. The Alaska, Hawaii, Guam and Virgin Islands columns are in the deposit but are not encoded.

Figures that the Act itself fixes are statutory constants: the $35 medical threshold (s 2014(e)(5)), 20 percent of earned income, 50 percent of income for shelter, 30 percent of net income for the allotment, $150 and $100 for expedited service, 30 and 7 days, 15 days before expiry, 3 months in 36, 80 hours in 30 days, 180 days. The federal minimum wage (29 U.S.C. 206, not deposited) is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `snap-core.l4`, `snap-seat.l4` | `snap-cases-applicant.l4` | 121 written, 121 satisfied |

In addition, 7 `#TRACE`s carry an `-- expect:` line: six breaches by the State agency and one obligation still pending. Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text and the COLA tables, with the arithmetic in the comment above the assertion.

## Seat

**The individual applying for SNAP for their household**, speaking for the household. They ask: "Who counts as my household?", "Do we pass the income and resource tests?", "How much will we get, and for the first month?", "Must I work, and what happens if I don't?", "Does the time limit cut me off?", "How fast must the State act on our application or renewal?".

Most of s 2020 is addressed to the State agency, through the State plan of operation. Those duties are encoded as what the applicant is owed and by when: the right to apply on the day of the first visit, a written statement of what the household must do, benefits within 30 days (7 if expedited), a notice of expiration, the renewal allotment within a month of the last one, and benefits continuing after a timely request for a hearing. In the core they are regulative rules with the State agency and the household as parties.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** That instrument is the FY 2027 COLA tables. The SNAP regulations (7 CFR parts 271–285) are not deposited.
- **The actors the text names:** the household, the individual member, the State agency.
- **Judgments left to others are answered conditionally, as inputs:** "physically and mentally fit", "medically certified as unfit", "good cause", a waiver area (s 2015(o)(4)), a State exemption (s 2015(o)(6)), the State's child support option (s 2014(e)(4)), and what counts as a "timely" hearing request.
- **The Act's own definitions are worked out from facts:** household (s 2012(m)), elderly or disabled member (s 2012(j), with paragraphs (2)(B) and (4)–(7) asked as one fact), gross and net income, every deduction, the tests, the allotment, the time limit and expedited service. Borrowed terms are asked as facts: SSI, TANF, Social Security disability payments, Indian or Urban Indian.
- **One case:** one household in one month, or one individual for the work questions.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** retailers (ss 2018–2021), claims and enforcement (ss 2022–2024), quality control and funding (ss 2025, 2027), research and grants, and the Puerto Rico and American Samoa block grants.

## Scope

**In:**

- s 2012(j) and (m)
- s 2012(u)(2), read against the published table (see finding 3)
- s 2014(a): categorical eligibility when every member receives TANF, SSI or aid to the aged, blind or disabled
- s 2014(c): the gross and net income tests
- s 2014(d): income after the exclusions is an input, except that the (d)(6) child support exclusion is computed
- s 2014(e)(1)–(6): the standard, earned income, dependent care, child support, excess medical and excess shelter deductions, the shelter cap and its exception, and the homeless shelter deduction
- s 2014(g)(1): the resource limits
- s 2014a: reporting a move out of the State
- s 2015(d)(1)–(2): the work requirements, the exemptions and the periods of ineligibility
- s 2015(o)(2), (3), (4) and (6) (as facts), and (5)(A)
- s 2017(a) and (c)(1)
- s 2020(e)(2)(B)(iii), (e)(3), (e)(4), (e)(9) and (e)(10)

**Out:**

- the s 2014(d) exclusions, item by item (the inputs ask for income already net of them)
- the standard utility allowance rules (s 2014(e)(6)(C)): shelter costs are an input, with any allowance the State uses
- sponsored aliens' deemed income (s 2014(i))
- s 2014(j) (see finding 8)
- prospective and retrospective budgeting and periodic reporting (ss 2014(f), 2015(c))
- disqualifications other than work: fraud, strikers, students (s 2015(e)), alien eligibility (s 2015(f)), drug felons, fleeing felons, child support cooperation and arrears, lottery winnings
- s 2015(d)(1)(B) beyond its 180-day cap, s 2015(d)(4) (employment and training), s 2015(o)(5)(B)–(C) (keeping eligibility and the one-time 3-month grace)
- s 2017(c)(3) (combined allotment), (d) (reduction for another program's sanction), (e)–(f) (group facilities)
- s 2020 apart from the paragraphs listed above
- the simplified program (s 2035)
- Alaska, Hawaii, Guam and the Virgin Islands

Household size counts eligible members only. Under s 2015(f), the income of a member made ineligible as an alien is still counted (less, at State option, a pro rata share). The `@desc` says so, and the figure is the applicant's to give.

## Read with the Social Security Act encoding

`../../../social-security-act/` (being encoded on 2026-10-24 by another session, from `subjects/us/social-security-act/registers/source-bundle/`) answers the questions that feed this encoding's inputs:

- **The Title II benefit amount** (OASDI retirement, survivors, disability). SNAP counts it as unearned income (s 2014(d) excludes only what it lists). In the elderly couple case it is the $2,600.
- **SSI eligibility and amount** (Title XVI). An SSI recipient is an "elderly or disabled member" (s 2012(j)(2)(A)). A household in which every member receives SSI is categorically eligible (s 2014(a)), and its SSI counts as income for the allotment.
- **TANF** (Title IV-A). TANF receipt by every member gives categorical eligibility (s 2014(a)). Under s 2015(d)(2)(A), complying with a TANF work registration requirement exempts a person from SNAP's.
- **Medicare premiums** (Title XVIII, s 1395r). These are allowable medical expenses (s 2012(c)(5)) for the excess medical deduction.
- **Disability under s 221(i)** (42 U.S.C. 421(i)). This is the "permanent disability" in s 2012(j)(3), (5), (6) and (m)(3).

The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here and not in code. Under 26 U.S.C. 6409 (not deposited), a federal tax refund, including the EITC, is not income or a resource for federal means-tested programs. Within this Act, s 2014(g)(3) excludes an EITC from resources for 12 months for a continuing participant.

## What the Act turns out to say

1. **The gross income test does not apply to a household with an elderly or disabled member.** Section 2014(c)(2) applies the 130-percent test only "in the case of a household that does not include an elderly or disabled member". The elderly couple's $2,600 is over the $2,345 gross limit for two, but they are eligible, and the same household without an elderly member is not. Asserted.
2. **The shelter cap does not apply to such a household either.** Under s 2014(e)(6)(B), the cap applies "In the case of a household that does not contain an elderly or disabled individual". The couple's shelter deduction is $891, above the $769 cap. A non-elderly household of the same means gets $769. Asserted.
3. **The published maximum allotment follows the s 2012(u)(2) ratios, including the 200-percent cap.** The FY 2027 table's "18+ | $3,887" is the 4-person $1,023 at 180 percent plus the 200-percent ceiling on the additional 22 percent per person (380 percent of $1,023 is $3,887.40). The "9-17 | $225 per additional person" row is 22 percent of $1,023 ($225.06). The encoding uses the table, and the sizes beyond 8 are asserted.
4. **The $25 minimum allotment is not 8 percent of the published one-person allotment.** Section 2017(a) sets the minimum at "8 percent of the cost of the thrifty food plan for a household containing 1 member ... rounded to the nearest whole dollar increment". Eight percent of the published $306 is $24.48, which rounds to $24, but the table says $25. The table figure is consistent with 8 percent of the unrounded one-person cost (30 percent of the 4-person cost, about $306.90, which gives $24.55, rounding to $25). The encoding uses the published $25.
5. **The allotment is rounded once, at the end.** Section 2017(a) rounds "the value of the allotment ... to the nearest lower whole dollar", not the 30-percent reduction. The single adult gets $306 − $52.35 = $253.65, which rounds down to $253. The State practice of rounding the 30 percent up first is not in the Act. Here both give $253, but they can differ. Asserted.
6. **The time limit reaches people aged 60 to 65, whom the general work requirements do not.** Section 2015(d)(1)(A) applies only "under the age of 60". Section 2015(o)(3)(A), as amended by Pub. L. 119-21, excepts only those "under 18, or over 65". So a 65-year-old with three countable months is cut off, and a 66-year-old is not. Asserted. Two consequences:
   - Someone aged 60 to 65 is also an "elderly or disabled member" (s 2012(j)(1)), so their household escapes the gross test and the shelter cap (findings 1 and 2) while they remain subject to the time limit.
   - The (o)(3)(D) exception for anyone "otherwise exempt under subsection (d)(2)" is read here as the (d)(2) categories whatever the age, although (d)(2) speaks of a person "who otherwise would be required to comply with" (d)(1). That is a reading, not tested against any ruling.
7. **The time-limit exception for parents now stops at a child under 14.** Under s 2015(o)(3)(C), as amended, the exception is for "a dependent child under 14 years of age". The general (d)(2)(B) exemption is for a child "under age six". A parent of a 10-year-old is outside the time limit but must register for work. A parent whose children are all 14 or older is subject to both. Asserted.
8. **Section 2014(j) is not encoded.** It says a State agency "shall consider a household member who receives" SSI or TANF "to have satisfied the resource limitations". It speaks of a member, while the resource test in s 2014(g) is a household test. Whether one SSI member lifts the test for the household is not answered by the text. The encoding applies the resource test unless every member receives the benefits (s 2014(a)).
9. **For a 1- or 2-person household at the net limit, the minimum allotment does all the work.** At the net limit of $1,330 for one person, the formula gives $306 − $399, which is below zero, so the household gets the $25 minimum. One dollar more of net income makes it ineligible. Asserted.
10. **First-month proration: the Act says neither whether the day of application counts nor how to round.** Section 2017(c)(1) counts "the number of days (from the date of application) remaining in the month". The encoding counts the day of application as a remaining day (15 days from 16 November) and does not round the prorated value: $253 × 15/30 = $126.50. Both are readings; the regulations, which settle them, are not deposited. The rule that "no allotment may be issued" below $10 is applied and asserted.
11. **The Act gives no deadline for refusing an application, and no deadline for a hearing decision.** The 30 days in s 2020(e)(3) are a duty to "complete certification of and provide an allotment ... to any eligible household". For an ineligible household the Act says only "promptly", and a fair hearing must be followed by "a prompt determination". The regulative rule therefore owes an ineligible household only the written statement, and the hearing rule is a prohibition on cutting benefits that runs to the end of the certification period. A cut after an adverse decision is a different act and does not breach it.
12. **Reporting a move out of the State has no period.** Under s 2014a the household "is required to report in a manner prescribed by the Secretary". With no `WITHIN`, the obligation never becomes a breach by time alone, and a trace 400 days on is still pending. Asserted by `#TRACE`.
13. **"One month after" the last allotment is not defined.** For s 2020(e)(4), the encoding takes the same day of the next month, or that month's last day where it is shorter (31 January to 28 February 2027). That is a reading. Asserted.
14. **Energy assistance now helps only households with an elderly or disabled member.** Section 2014(e)(6)(C)(iv), as amended by Pub. L. 119-21, makes the heating and cooling standard utility allowance available, because of a LIHEAP payment, only "to households with an elderly or disabled member". Section 2014(k)(4) treats a State energy payment to a household without such a member as income. The encoding takes shelter costs, including any utility allowance, as one input, so neither is computed. Noted for a later pass.
15. **Internet costs are out of shelter costs.** Section 2014(e)(6)(E) says "Any service fee associated with internet connection shall not be used". The shelter `@desc` tells the applicant to leave internet out.

## Before relying on it

- An independent test pass, and a check of every figure against the COLA page's print PDF, which is not deposited.
- Deposit and encode the SNAP regulations (7 CFR 273), which settle the readings in findings 6, 10 and 13, timely hearing requests, the standard utility allowances, and the income and resource exclusions this encoding takes as inputs.
- The FY 2028 COLA tables when published (from 1 October 2027). Add them as a second row of the dated table.
- The Alaska, Hawaii, Guam and Virgin Islands columns (already deposited).
- Students (s 2015(e)) and alien eligibility (s 2015(f)) as member-level eligibility questions.
- The State options each State elects (child support deduction, SUA, broad-based categorical eligibility under State TANF-funded programs, the s 2015(d)(1)(B) household sanction). These are State law, for the state samples.
