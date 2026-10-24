# Unemployment Insurance Code, Chapter 5 (California unemployment benefits) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the unemployed worker (the claimant), with the design defaults ruled on 2026-10-18.
The core rules use the Code's own actors and terms; the worker's questions (`@export`, `@desc`, under `§ Questions for the unemployed worker`) are derived from them.
Duties with times are regulative rules with the party as a parameter: the weekly work search (s 1253(e)), the last employer's 10 days to submit facts (s 1327), and the 30-day appeal (s 1328).
No REFUSE; a claim effective before 2005 answers `not covered`, and a test asserts it.
The 31 rows of the s 1280(c) table were generated from the deposited text by a script, which also checked that the rows are contiguous and rise $1 a row; they were not typed by hand. Expected values in the cases were worked by hand.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not advice.**

Why unemployment insurance for California's benefits half: its amounts are wholly in the statute (the s 1280 table and the $450 maximum). CalWORKs' maximum aid payments (Welf. & Inst. Code 11450) and the SSP payment standards (s 12200) are deposited too, but are recomputed each year by cost-of-living adjustments and Budget Act changes that are not deposited; they are candidates for a later pass.

## Edition

The Legislative Counsel's official bulk database export (code tables updated 2026-10-03), deposited 2026-10-20 as unofficial plain text: `../../registers/source-bundle/ca-uic-div1-part1-ch5-unemployment-compensation-benefits-2026-10.txt` (Chapter 5 whole). No annual figure is needed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ca-unemployment.l4` | `ca-unemployment-cases.l4` | 43 written, 43 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s with `-- expect:` comments matched (no work search: breach; employer's facts late: breach).

## Seat

**The unemployed worker who claims benefits.** Questions: "How much a week?", "Have I earned enough?", "What is the most I can get?", "What will I get for a week with some wages?", "Does my pension reduce it?", "Am I eligible this week?", "Does the way my job ended disqualify me?", "How much must I earn to requalify?".

The 2026-10-18 defaults:

- **The Act alone:** Chapter 5.
- **The actors the text names:** the claimant, the last employing unit, the department and its director, the administrative law judge.
- **Judgments left to the director** asked as facts: good cause, misconduct, whether a search followed the office's instructions, able and available. The s 1256 presumption is worked out: without the employer's written notice, the claimant is presumed not to have quit without good cause or been discharged for misconduct.
- **One case:** one claimant, one benefit year.
- **Machinery out:** the appeals board, overpayment collection, employer charging.

## Scope

**In:** s 1252(a)(1), (2); s 1253(a)-(f); s 1255.3(a), (c); s 1256; s 1257(b); s 1260(a), (b); s 1279; s 1280(c); s 1281; s 1327; s 1328.

**Out:** claims effective before 2005 (`not covered`); s 1253.5 and the other special eligibility sections; s 1257(a) and s 1260(c), (d) (false statements); s 1262 (trade disputes) and the other disqualifications; extended duration benefits; the alternate base period (s 1275: the worker states base-period wages); disability insurance (Part 2).

## Read with

- the federal frame: FUTA (26 U.S.C. 3304) and SSA Title III, deposited in `subjects/us/internal-revenue-code-of-1986/` and `subjects/us/social-security-act/`;
- the tax side: California does not tax unemployment compensation (Rev. & Tax. Code 17083 switches off IRC s 85); see `../../../revenue-and-taxation-code-division-2-part-10-personal-income-tax/encodings/baseline-2026-10/`. It is federal gross income.

## What the Code turns out to say

1. **The $450 weekly maximum has not changed since 2005** (s 1280(c)(3)). Above $1,832.99 in the highest quarter the amount is 50% of that quarter's wages divided by 13, raised to the next dollar, so $450 is reached at $11,700 of highest-quarter wages. Asserted.
2. **Below $900 in the highest quarter the table has no row**, and s 1281(a) separately requires $1,300 in the highest quarter, or $900 with base-period wages of 1.25 times it. Asserted.
3. **The maximum award is the lower of 26 weeks' benefit and half the base-period wages** (s 1281(b)), raised to the next dollar. Asserted.
4. **A week with wages pays the weekly amount less the smaller of (wages over $25) and (wages over 25% of the wages)** (s 1279(a)), raised to the next dollar: at low earnings $25 is kept, at higher earnings a quarter. The same week counts as unemployment only if wages less the greater of $25 or 25% are below the weekly amount (s 1252(a)(2)). Asserted.
5. **The quit and misconduct disqualification ends only on earnings of five times the weekly amount in bona fide work after registering** (s 1260(a)); there is no fixed number of weeks. Refusing suitable work costs 2 to 10 consecutive weeks (s 1260(b)). Asserted.
6. **The claimant is presumed not to have quit without good cause or been fired for misconduct unless the employer gives written notice with facts sufficient to overcome the presumption** (s 1256), which the employer must send within 10 days of the claim notice (s 1327). Asserted and traced.
7. **Some quits are good cause by statute**: following a spouse or domestic partner (including one to whom marriage or partnership is imminent) where commuting is impractical, and protecting the family from domestic violence ("may be deemed"); electing a seniority layoff ("shall be deemed"); and compulsory retirement under a collective agreement. The "may" cases are encoded as not disqualifying, which is how they come out if the director so deems. Asserted.
8. **The appeal window is 30 days from service of the notice**, extendable for good cause including "mistake, inadvertence, surprise, or excusable neglect" (s 1328). Traced.
9. **A pension reduces benefits only if paid under a plan maintained or contributed to by a base-period or chargeable employer** (s 1255.3(c)), and the reduction operates only while FUTA requires it ((b)). Asserted.

## Before relying on it

- Add the alternate base period (s 1275) and the special eligibility rules (students, school employees, trade disputes).
- EDD's regulations on the work search and certification are not deposited.
- An independent test pass.
