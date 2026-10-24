# Social Security Act (Titles II and XVI, and Medicare entitlement and enrollment) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the Act is applied, with the design defaults ruled on 2026-10-18.
There was no earlier encoding of this Act to keep, so this is a baseline, not a seat layer.
The rules are written seat-neutral, in the Act's own actors and terms, in three core modules. The person's questions are in a seat module that calls them and restates nothing.
There is no REFUSE. A question that reaches a gap answers `not covered` (or `benefit not covered`) with the reason, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

| Module | What it holds |
|---|---|
| `ssa-figures.l4` | The dated table of figures set each year: `the figures for` a calendar year, which is `JUST` the 2026 figures for 2026 and `NOTHING` otherwise. It also holds the fixed statutory amounts: the SSI resource limits of $2,000 and $3,000, and the $255 lump-sum cap. |
| `ssa-common.l4` | The answer types, calendar months (one number: year × 12 + month − 1), attaining an age, the Act's rounding rules, and the parties and acts of the regulative rules. |
| `ssa-title-ii.l4` | Title II: s 413, s 414, s 416(l), s 415(a)–(b), s 403(a)(1), s 402(a), (d), (e)/(f), (i), (j), (q), (w), s 423(a)–(d), s 403(b), (f), (h), s 405(b), (g). |
| `ssa-title-xvi.l4` | Title XVI: s 1382c(a)(1), s 1382a, s 1382b(a), s 1382(a)–(c)(7), (e)(1)–(2), s 1383(c), (e). |
| `ssa-medicare.l4` | s 426(a), (b), (h), s 1395i-2(a), s 1395o(a), s 1395p(d)–(g), (i), s 1395q(a), s 1395r(a)(3), (b). |
| `ssa-seat.l4` | 38 `@export` questions with a `@desc` on every input, under eight `§§` groups. |

## Edition

- **Statute.** 42 U.S.C. chapter 7, as deposited at `../../registers/source-bundle/`: `usc42-ch7-schII.txt` (Title II, ss 401–434), `usc42-ch7-schXVI.txt` (Title XVI, ss 1381–1385) and `usc42-ch7-schXVIII-eligibility.txt` (ss 1395c, 1395i-2, 1395i-2a, 1395j, 1395o–1395r, 1395w-101). All three are from the Office of the Law Revision Counsel's USLM XML at release point Public Law 119-121, current through 9 October 2026, retrieved 2026-10-19. `subject.json` still names govinfo's 2024 edition, which was the 2026-09-22 index. The deposit's `SOURCE-LICENSE.md` and `.meta.json` files record the OLRC text that is actually encoded. Title 42 is not positive law, so the Code is prima facie evidence and the Statutes at Large are the law.
- **Figures.** Calendar year 2026 only, from `fr-2025-19763-ssa-cola-2026.txt` (SSA, *Cost-of-Living Increase and Other Determinations for 2026*, 90 FR 49047, 3 November 2025) and `fr-2025-20251-cms-part-b-2026.txt` (CMS Part B premium and deductible for 2026, 90 FR 52063). They are recorded in `../../registers/annual-figures.json`. Every figure in `ssa-figures.l4` was checked against the notice text:

| Figure | 2026 | Sets | Source |
|---|---|---|---|
| PIA bend points | $1,286, $7,749 | s 415(a)(1)(B) | 90 FR 49047 |
| Family maximum bend points | $1,643, $2,371, $3,093 | s 403(a)(2) | 90 FR 49047 |
| Quarter of coverage | $1,890 | s 413(d) | 90 FR 49047 |
| Earnings test exempt amounts | $2,040 a month ($24,480 a year); $5,430 ($65,160) in the year retirement age is reached | s 403(f)(8) | 90 FR 49047 |
| Contribution and benefit base | $184,500 | s 430 | 90 FR 49047 (recorded, not used) |
| Cost-of-living increase | 2.8% | s 415(i) | 90 FR 49047 (recorded, not used) |
| SSI federal benefit rate | $994 individual, $1,491 couple | s 1382(b), s 1382f | 90 FR 49047 |
| SSI student earned income exclusion | $2,410 a month, $9,730 a year | s 1382a(b)(1) (limits set by 20 CFR 416.1112) | 90 FR 49047 |
| SGA, blind | $2,830 a month | s 423(d)(4)(A) | 90 FR 49047 |
| SGA, non-blind | $1,690 a month | 20 CFR 404.1574 (regulation): **ADMIN-POLICY**, a published figure, not the Act | 90 FR 49047 |
| Part B standard premium | $202.90 a month | s 1395r(a)(3) | 90 FR 52063 |
| Part B deductible | $283 | s 1395l(b) | 90 FR 52063 (recorded, not used) |

The 2027 determinations were not in the Federal Register on 2026-10-19. News coverage reports a 3.6% COLA. Any question about another year therefore answers `not covered`.

## Checks

| File | Assertions written | Satisfied |
|---|---|---|
| `ssa-cases-worker-retiree.l4` | 83 | 83 |
| `ssa-cases-survivor-disabled.l4` | 68 | 68 |
| `ssa-cases-ssi-medicare.l4` | 75 | 75 |
| **Total** | **226** | **226** |

`l4 run` on all nine `.l4` files gives 0 errors and 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read; a deliberate `#ASSERT 1 EQUALS 2` was run once to confirm that a failure shows as `assertion failed`, `DiagnosticSeverity_Error`.

The regulative rules are tested two ways. Where the trace ends FULFILLED, they are asserted with `#ASSERT EVALTRACE … EQUALS FULFILLED` (11 assertions). Where they are breached, they are run with `#TRACE` and an `-- expect:` line (4 traces: s 403(h)(1)(A), s 1383(e), s 1382(e)(2) and s 1383(c)(2)). Each of the four printed `DEONTIC BREACHED` with the expected party and reason.

Every expected value was worked by hand from the text and the notice. The working is in the comment above each assertion. Every person in the cases is hypothetical. No scenario life exists yet for the United States, and there is no US requirement ledger.

## Seat

**The individual to whom the Act is applied**, asking about their own record:

- **the worker earning credits**: "How many quarters of coverage do my earnings give me? Am I fully insured? Am I insured for disability?"
- **the retiree**: "When do I reach full retirement age? What is my PIA? From which month can my benefit begin? How much is it if I start early or late?"
- **the working beneficiary**: "How much will be withheld because I work? Must I report my earnings, and by when? What happens if I don't?"
- **the survivor**: "Am I the widow(er)? How much is my widow's benefit? What does my child get? How much of the lump sum, and by when do I apply?"
- **the disabled person**: "Am I entitled? From which month? How much? Are my earnings over SGA? When does Medicare start?"
- **the SSI applicant**: "Am I aged, blind or disabled? What is my countable income? How much SSI? From which month? What if I report late?"
- **the person reaching Medicare age**: "Am I entitled to Part A? Can I buy it? When is my Part B enrollment period? When am I covered? What will my premium be?"
- **anyone with a decision to challenge**: "By when must I ask for a hearing, or go to court?"

Most provisions address the Commissioner of Social Security or the Secretary. They are encoded for what they mean to the person: what must be decided and by when (s 1383(c)(2)), what may be deducted (s 403(b), (h)(2), s 1383(e)(2)), and when coverage starts (s 1395q).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers**: the two 2026 Federal Register notices, deposited. No regulation is deposited. Where the Act leaves a figure or a time to regulation (the non-blind SGA amount, the student exclusion limits, the time to report a change under s 1383(e)), the published figure is used and marked, or the time is an input.
- **The actors the text names**: the individual and the Commissioner of Social Security. The Secretary of HHS appears only in the Medicare provisions' wording.
- **Judgments handed to others are answered conditionally**: disability (s 423(d), s 1382c(a)(3)), blindness, dependency (s 402(d)(3)–(4)), good cause (s 403(l), s 1383(e)(2)) and the Commissioner's resource limits under s 1382b(a)(2)(A) are asked as facts ("whether Social Security finds …").
- **The Act's own definitions worked out from facts**: quarter of coverage, fully, currently and disability insured, retirement age, elapsed years, benefit computation years, PIA, family maximum, widow and widower, surviving divorced spouse, reduction period, increment months, excess earnings, countable income, the initial enrollment period. **Borrowed terms asked as facts**: AIME (its indexing needs the national average wage index series, not deposited), "child" (s 416(e)), and the s 414(c) SSN criterion.
- **One case**: one person and one earnings record, for one month or one year.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out**: the trust funds (s 401), administration and procedure beyond the hearing and court deadlines (s 405 except (b)(1) and (g)), representatives, penalties for fraud, the COLA and wage-index computations themselves (ss 409(k), 415(i), 430: their results come from the notice), and the annual determination duties.

**One departure, recorded as finding 1**: when an age is attained.

## Read with the Internal Revenue Code baseline

`../../../internal-revenue-code-of-1986/encodings/baseline-2026-10/` is being written by another session on the same day; check that it exists before relying on the link. It takes the federal income tax side of these benefits, and none of it is restated here:

- **IRC s 86**: up to 50% or 85% of Social Security benefits are taxable. The test adds half the benefits to modified AGI and compares the total with the base amount ($25,000; $32,000 on a joint return) and the adjusted base amount ($34,000; $44,000 joint), as deposited at `usc26-ch1-schB-ptI-III.txt`. A "social security benefit" there is "any amount received ... by reason of entitlement to a monthly benefit under title II" (s 86(d)(1)(A)): the old-age, widow's, child's and disability benefits this encoding answers. Benefits withheld under the s 403(b) earnings test are not received. Section 86(d)(2) reduces the year's benefits by any repayment of benefits received earlier, which is how an overpayment recovered after a late earnings report comes through.
- **IRC ss 3101, 1401–1402 (FICA, SECA)**: these are charged on the wages and self-employment income that s 413 credits toward quarters of coverage and that s 415(b) indexes into the AIME. Both stop at the s 430 base, $184,500 in 2026.
- **IRC ss 24, 32 and 26 U.S.C. 6409**: s 1382b(a)(11) keeps EITC and refundable child tax credit refunds out of SSI resources for 9 months. That exclusion goes into the "resources the law excludes" input. Section 6409, the general rule for all federal means-tested programmes, is not deposited.

The stable `l4` cannot IMPORT across subject folders, so the link is recorded here and not in code.

## Scope

**In.**
- **Title II.**
  - Quarters of coverage after 1977 (s 413(a)(2)(A)(ii), (B)(vii), (d)).
  - Fully and currently insured (s 414(a)(1)–(2), (b), (c) as one fact).
  - Insured for disability (s 423(c)(1)(A), (B)(i)–(ii), with the blind exception and the odd-quarter rule).
  - Retirement age and early retirement age (s 416(l)), and s 403(j).
  - The PIA formula for those first eligible in 2026 (s 415(a)(1)(A)–(B), (a)(3)(B)), benefit computation years (s 415(b)(2)(A), without the child-care drop-out years) and AIME from a given total (s 415(b)(1)).
  - The family maximum formula (s 403(a)(1)).
  - Old-age entitlement, its first month and retroactivity (s 402(a), (j)(1), (j)(4)(A)).
  - The early-retirement reduction (s 402(q)(1), (6), (7) as one input, (8), (9)) and the delayed-retirement increase (s 402(w)(1), (2), (6)).
  - Widow's and widower's benefits (s 402(e)(1)(A)–(D), (F)(i), (e)(2)(A), (C), (D), (e)(3), (e)(4), (e)(5)(A); s 402(f) mirrors (e)), with s 416(c), (d), (g), (k).
  - Child's benefits (s 402(d)(1)–(2)).
  - The lump-sum death payment and its two-year limit (s 402(i)).
  - Disability benefits: entitlement, the waiting period, ALS, retroactivity and amount (s 423(a)(1)–(2), (b), (c)(2)), and the blind SGA amount (s 423(d)(4)(A)).
  - The earnings test (s 403(b)(1), (f)(1) as a cap, (f)(3), (f)(8)).
  - The report of earnings, its deadline, extension and additional deductions (s 403(h)(1)(A), (h)(2), (l)).
  - The hearing and court deadlines (s 405(b)(1), (g)).
- **Title XVI.**
  - Aged, blind, or disabled individual (s 1382c(a)(1)).
  - Countable income: s 1382a(a), and the exclusions in s 1382a(b)(1), (2)(A), (4)(A)–(C) and (6).
  - Resources: s 1382(a)(3), and s 1382b(a), with the exclusions as one figure.
  - Eligibility and the benefit (s 1382(a)(1)–(2), (b)), the one-third reduction (s 1382a(a)(2)(A)(i)), and public institutions and Medicaid facilities (s 1382(e)(1)(A)–(B)).
  - When an application takes effect (s 1382(c)(7)).
  - The duty to apply for other benefits (s 1382(e)(2)) and the duty to report, with its penalty (s 1383(e)(1)(A), (e)(2)).
  - The hearing and the 90-day determination (s 1383(c)(1)–(2)).
- **Medicare.**
  - Part A: s 426(a), (b), (h), and buying Part A under s 1395i-2(a).
  - Part B eligibility (s 1395o(a)).
  - Enrollment periods: initial, general, deemed and the employer-coverage special period (s 1395p(d), (e), (f), (g)(2)(A), (i)(1), (3)).
  - When coverage starts for months from 2023 (s 1395q(a)(2)(A), (C), (D)(ii), (3)(A)).
  - The premium and the late-enrollment increase (s 1395r(a)(2)–(3), (b)).

**Out.**
- **Title II.**
  - Spouse's benefits (s 402(b), (c)), mother's and father's (s 402(g)) and parent's (s 402(h)) benefits, except where they appear as conditions.
  - The s 402(q)(3) combined reduction, (q)(5) certificates and (q)(10)–(11).
  - The s 402(e)(2)(B) re-indexing for a worker who died before 62.
  - In the disabled widow's waiting period, the counting of SSI months (s 402(e)(5)(B)) and re-entitlement without a new waiting period ((e)(1)(F)(ii)).
  - The (e)(1)(C)(ii)–(iii) conversions and the (e)(4)(B)–(C) later starts of the disability period.
  - Re-entitlement within 60 months (s 423(a)(1)(iii)), insured status after an earlier young-worker period of disability (s 423(c)(1)(B)(iii), answered `not covered`), and the disability determination itself (s 421, s 423(d)(2)–(5), (f)).
  - Trial work and the extended period of eligibility (s 422).
  - The special minimum PIA (s 415(a)(1)(C)), whose increased amount is not deposited.
  - PIAs for eligibility before 2026 (s 415(i) increases not deposited: `not covered`), before 1979 (`not covered`) and after 2026 (`not covered`).
  - The disability family maximum (s 403(a)(6)), and sharing out the family maximum among beneficiaries.
  - Deductions under s 403(c)–(d) for noncovered work abroad, the s 403(g) report and its penalties, and the charging order month by month (s 403(f)(1) beyond the total).
  - Overpayments (s 404), representation (s 406), assignment (s 407), penalties (s 408), and suspension of benefits for aliens abroad, prisoners and fugitives (s 402(t), (x), (y)).
  - The disability offset against workers' compensation (s 424a), not deposited.
- **Title XVI.**
  - Deeming of an ineligible spouse's or parent's income and resources (s 1382c(f)): `not covered`.
  - The child disability standard (s 1382c(a)(3)(C)), except as a fact.
  - Infrequent or irregular income (s 1382a(b)(3)) and the other income exclusions in s 1382a(b)(5), (7)–(25).
  - Plans for achieving self-support.
  - The resource transfer penalty (s 1382b(c)) and trusts (s 1382b(e)).
  - The couple rate in a medical facility (`not covered`).
  - Presumptive disability, representative payees, and the payment and recovery machinery of s 1383 beyond (c) and (e).
  - Sponsor deeming for aliens (s 1382j).
  - State supplementation (s 1382e), which is State law and a State's agreement, not deposited.
  - 8 U.S.C. 1612 limits on SSI for aliens, not deposited (finding 9).
- **Medicare.**
  - ESRD entitlement (s 426-1), the s 426(f) counting of earlier disability periods, s 1395i-2a, and the premium for buying Part A (s 1395i-2(d); the 2026 amount is not deposited).
  - Coverage start dates before 2023, and the coverage start for special enrollment periods.
  - The income-related monthly adjustment (s 1395r(i)), the s 1395r(f) hold-harmless limit, and the deduction of the premium from benefits (s 1395s, not deposited).
  - Part D (s 1395w-101) beyond what is deposited.
  - Immunosuppressive-drug coverage (s 1395o(b)).
- **Elsewhere in the subject's source bundle**: TANF (Title IV-A) and unemployment insurance administration (Title III). They were deposited for the State samples, are encoded by the State sessions, and are not part of this encoding.

## What the Act turns out to say

1. **"Attains age" is not defined.** The Act says "has attained age 62", "attains retirement age" and "the first month throughout which" a person is a given age, but never says when an age is attained. The encoding takes the common-law rule that the Social Security Administration applies by regulation (20 CFR 404.2(c)(4), not deposited): an age is attained on the day before the birthday. It is one rule in `ssa-common.l4` (`the month in which age 0 is attained`). It moves the month only for a person born on the 1st of a month: born 1 January 1957, retirement age falls in April 2023, not May. Born 1 July 1961, Part A begins in June 2026, not July. Asserted. Under the regulation, a person born on the 2nd attains each age on the 1st, so is that age "throughout" the month of the birthday. Asserted (born 2 May 1964: benefits from May 2026).
2. **The text encoded is the OLRC's, not govinfo's.** `subject.json` records the 2026-09-22 index of govinfo's 2024 edition, but the text deposited on 2026-10-19 is the OLRC's release point Public Law 119-121. That text has no windfall elimination provision in s 415(a) (it runs (1)–(6)) and no government pension offset in s 402(k). This is consistent with their repeal in January 2025. The encoding has neither.
3. **Every PIA except a 2026 first-eligibility PIA is out of reach of the deposit.** Under s 415(a)(1)(A) the PIA is "thereafter increased as provided in subsection (i)". A person first eligible before 2026 has a PIA raised by each December's COLA, and those increases are not deposited. So the PIA question answers `not covered` for them, asserted, and the benefit questions take the person's PIA as an input. For someone first eligible in 2026 the formula answer stands until the December 2026 COLA, which the 2027 notice will set.
4. **Delayed retirement credits come in arrears.** Under s 402(w)(3), the increment months are totalled each year and applied "beginning with benefits for January of the year following", or at 70. The encoding answers the amount once all increment months are credited. In the year benefits start after retirement age, the first months are paid at a lower amount.
5. **The early-retirement reduction is credited back at retirement age.** Under s 402(q)(7)(A), months in which benefits were withheld under the earnings test are left out of the "adjusted reduction period". Starting at 62 and losing 12 months to the earnings test raises Ana's $1,408 to $1,508 from retirement age. Asserted.
6. **The widow's reduction is a line, revised by the Commissioner.** Section 402(q)(9)(B) tells the Commissioner to revise the monthly reduction "periodically" so that it is 28.5% at 60 and falls "by linear interpolation" to 0 at retirement age. The encoding computes the line itself: 28.5% × the months in the reduction period ÷ the months from 60 to retirement age. A published monthly factor may differ from it in the last cent. For a disabled widow under 60, the reduction period starts at 60 (s 402(q)(6)(A)(iii)), so she bears the full 28.5%. Asserted.
7. **"Two years after the date of death" from 29 February.** There is no 29 February two years on. The stable `l4` date arithmetic rolls 29 February 2026 to 1 March 2026, so that is the deadline given. Asserted. An application on the second anniversary is treated as in time. The s 416(j) rule, which moves a deadline that falls on a weekend or holiday, is not encoded.
8. **The earnings test is charged month by month.** Section 403(f)(1) charges the excess earnings to the year's months in order, a whole month's benefits at a time. The encoding gives the total deducted: the excess earnings, but no more than the benefits for the months that can be charged. Which months the person goes without, and the non-service months of the grace year ((f)(1)(E)), are left to the "months that can be charged" input.
9. **Title XVI alone does not settle an alien's SSI.** Section 1382c(a)(1)(B) admits "an alien lawfully admitted for permanent residence or otherwise permanently residing in the United States under color of law". The welfare reform law of 1996 (8 U.S.C. 1612, not deposited) narrows this sharply. The encoding answers only what Title XVI says, and the `@desc` warns of it.
10. **The order of the $20 exclusion is not stated.** Section 1382a(b)(2)(A) excludes "the first $240 per year ... of income (whether earned or unearned)" other than need-based income. It does not say which income it comes off first. The encoding takes it off unearned income first, which gives the applicant more because earned income is later halved, and applies what is left to earned income before the $65. Section 1382a(b)(4) excludes earned income "not excluded by the preceding paragraphs", which is why the remainder goes there. Asserted ($100 earned with $300 needs-based income: $307.50).
11. **SSI's rates are annual in the Act and monthly in practice.** Section 1382(b) states yearly rates ($1,752, $2,628, "or, if greater, the amount determined under section 1382f"). The exclusions are $240 and $780 a year "or proportionately smaller amounts for shorter periods", which is $20 and $65 a month. The notice rounds the yearly rate down to a multiple of $12 ($11,928 and $17,892) and divides by 12, giving $994 and $1,491. The encoding works in months throughout. The medical-facility rate of "$360 per year" is $30 a month. Asserted.
12. **Which limbs of s 426(a)(2)(A) need an application?** The clause runs: "is entitled to monthly insurance benefits under section 402, would be entitled to those benefits except that he has not filed an application therefor ..., or would be entitled ... but for the failure of another individual ..., and, in conformity with regulations of the Secretary, files an application for hospital insurance benefits". The encoding reads the final "files an application" as a condition only of the not-yet-entitled limbs, so a person already on s 402 benefits at 65 is entitled to Part A without a separate application. Asserted. A reading that makes everyone apply would change only that case.
13. **The late-enrollment increase is not rounded in the Act.** Section 1395r(b) adds "10 percent of the monthly premium so determined for each full 12 months". It says nothing about rounding, so the encoding leaves it unrounded: $202.90 + 20% = $243.48. Asserted.
14. **The non-blind SGA amount is not in the Act.** The Act fixes only the blind amount (s 423(d)(4)(A), by reference to the pre-1996 exempt amount). The $1,690 for everyone else comes from regulation (20 CFR 404.1574) and is published in the same notice. It is used and marked ADMIN-POLICY. The answer to "are my earnings above SGA" for a non-blind person is therefore regulation, not statute.
15. **The final rounding comes after the Part B deduction.** Section 415(g) rounds a benefit down to $1 "after any deduction under section 1395s(a)(1)", the Part B premium. Section 1395s is not deposited, so the encoding rounds the benefit before any premium is taken. For someone paying Part B from their benefit, the net amount can differ by up to $1.
16. **The deadline to report changes is not in the Act.** Under s 1383(e)(1)(A) the Commissioner prescribes "the reporting of events and changes in circumstances". The time allowed is in regulation (not deposited), so the regulative rule takes the number of days as an input. Only the penalty ($25, $50, $100) is statutory. Asserted.

## Before relying on it

- **The disabled widow's waiting period** is applied (s 402(e)(1)(F)(i), (e)(5)(A)), but the person states the first full month of disability. Months of SSI eligibility, which count toward it under (e)(5)(B), are not counted. A widow on SSI may therefore be told her entitlement starts later than it does.
- An independent test pass, with cases written by someone who has not read the encoding, especially for the s 402(q) and (w) arithmetic and the SSI income order.
- The 2027 Federal Register notices, deposited and added to `the figures for`, once they are published. Earlier years' notices are needed if earlier PIAs and earnings-test years are wanted.
- The national average wage index series (s 409(k)), so AIME can be computed from an earnings record rather than asked.
- Deeming (s 1382c(f)), the spouse's benefits (s 402(b), (c)), the family maximum distribution (s 403(a)), and s 1395s (the premium deduction).
- 8 U.S.C. 1612 and 20 CFR 404.2, 404.1574 and 416.714, if the published figures and timings are to be cited rather than input.
- A check that `../../../internal-revenue-code-of-1986/encodings/baseline-2026-10/` exists and that its s 86 inputs match these outputs.
- The Legalese Cloud deployment (`us-social-security-act-individual`, 34 characters) is done by a person. This file does not deploy anything.
