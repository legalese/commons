# Industrial Relations Act 2016 (Qld): baseline encoding for the employee bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the negatives rulings of 2026-11-04 and 2026-11-05.
Focus: the provisions a claimant meets (an employee claiming unfair dismissal, notice or redundancy pay, a general protections remedy, or unpaid wages and superannuation).
There is no REFUSE in it. It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`qira-dates.l4`**: date and amount helpers on the stable prelude's date primitives (the `daydate` library is not imported). The date readings are stated at its top.
- **`qira-claims.l4`**: the seat-neutral core, in the Act's own actors ("the employee", "the employer", "the commission", "the registrar"). The exclusions, time limits, caps, tables and lists are functions. Four regulative rules (`DEONTIC`): the reinstatement application (s 317(2)), insisting that a rejected application proceed (s 317(6)-(7)), the general protections dismissal application (s 310(1)-(2)) and the employer's duty to pay wages at least monthly (s 373(1)). A deadline for something the employee chooses to do is a `DO` rule, and missing it is no breach.
- **`qira-seat.l4`**: the employee's seat. It asks 25 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings with the situation in which each group arises. It builds the core's records from plain answers and restates no rule. Inputs with the same meaning carry the same name in every question, so the form can ask them once. The long argument lists were laid out by a small script in the session scratchpad; it holds no expected values and is not part of the encoding.
- **`qira-cases-employee.l4`**: the cases.

No earlier encoding of this Act existed. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Industrial Relations Act 2016** (act-2016-063), the current in-force version on 22 September 2026, as deposited at `../../registers/source-bundle/act-2016-063.txt` (retrieved 2026-09-22, unofficial HTML conversion).

Not deposited, so taken as inputs or left out (each is named where it bites):

- the **Industrial Relations Regulation 2018** (exclusions under s 315(6)-(7), prescribed misconduct under s 121(2)(e), service disregarded under s 123(2), commission and piece rates under s 124(3), employees excluded from redundancy pay under s 125(3)(e), the application fee under s 311, the deduction floor under s 376(4));
- the **high income threshold** of the Fair Work Act 2009 (Cwlth) s 333 (an input, in dollars a year; the Commonwealth figure is indexed each year);
- the **value of a penalty unit** (Penalties and Sentences Act 1992 (Qld); an input).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `qira-dates.l4`, `qira-claims.l4`, `qira-seat.l4` | `qira-cases-employee.l4` | 117 written, 117 satisfied |

In addition, three `#TRACE`s carry an `-- expect:` line: a late reinstatement application, left at the permission to ask for a further period; an insistence given in time, left at the commission's duty to deal with the application; and wages paid a day late, a breach by the employer. Each was read and matches its expectation. A deliberately wrong assertion was run in the scratchpad to confirm a failure shows as `DiagnosticSeverity_Error`.

`l4 run` on all four files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the working in the comment above the assertion. The case figures for the high income threshold ($183,100) and a penalty unit ($166.90) are inputs, not law encoded here.

## Seat

**The employee** (or former employee) bringing or weighing a claim against the employer. They ask:

- "Can I claim unfair dismissal, or am I excluded?"
- "By when must I apply, and what if I am late or my application is rejected?"
- "Has my application lapsed?"
- "What will the commission weigh, and what is the most compensation it can give?"
- "Do the severance and mass-dismissal rules protect me, and by when must I apply?"
- "Which Christmas holidays must I be paid for after a stand-down? Can I be stood down without pay?"
- "How much notice, or pay instead of notice, am I owed? Can I be dismissed on the spot?"
- "Am I owed redundancy pay, and how much?"
- "By when must I apply under the general protections?"
- "Can I still recover unpaid wages or super, and where? Can my employer claw back an overpayment from my wages?"

There is **no second seat** yet. An employer seat (`qira-seat-employer.l4`) over the same core would be welcome. The commission, the registrar, magistrates and inspectors are officials and get no seat; what they decide appears only as an input the employee answers conditionally, or as what the employee is owed (the commission's duty to deal with an application the employee insists on, s 317(7)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** The regulation is not deposited (above); its figures and classes are not guessed.
- **The actors the text names:** the employee, the employer, the commission, the registrar, an organisation acting for the employee.
- **Judgments left to others are answered conditionally, as inputs:** whether a longer probation is "a reasonable period" (s 315(1)(b)); whether the main purpose of a fixed engagement was to avoid division 2 (s 315(1)(d)(i)); whether reinstatement "would be impracticable" (s 322(1)); whether a substantial reason for a fixed engagement was to avoid redundancy pay (s 125(4)); whether the employee "can show" the conduct did not make continuing unreasonable (s 121(3)); a s 127 order reducing redundancy pay. The commission's weighing under s 320 is not decided: only the list of matters it must consider is worked out.
- **The Act's own definitions are worked out from facts:** the probationary period, short term casual employee (s 315(9)), the s 315 exclusions, the notice period (s 123), redundancy pay (s 126), the s 332 holidays. Borrowed terms are asked as facts: industrial instrument coverage, public service officer on tenure (Public Sector Act 2022), the high income threshold, a labour market program. **Continuous service** is the employee's start date, taking in service with a former employer that s 132 carries over (s 315(3)); the Act's continuity rules are not worked out.
- **One case:** one employment, ended by one dismissal (or one unpaid amount, one overpayment).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the commission and registry, the industrial magistrates' constitution, appeals procedure, organisations, the information statement.

## Scope

**In:**

- ch 2 pt 2 div 13 sdiv 1 (notice of termination): s 120 (exclusions), s 121 (dismissal for misconduct), s 122(3) (6-year limit), s 123 (minimum notice), s 124 (compensation instead of notice)
- ch 2 pt 2 div 13 sdiv 2 (redundancy pay): ss 125-127
- ch 8 pt 1 div 8 (general protections compliance): s 310 (time limits); s 309 (who may apply) is not encoded
- ch 8 pt 2 (dismissals), the whole Part: s 315 (exclusions, including (3), (4), (5), (8), (9)); s 316; s 317 (application, time, rejection and insistence); s 318(4) (lapse); s 320 (matters considered); s 322 (compensation and its cap); s 323(1)(a)(i) (the 50 penalty unit further order); ss 325-331 (severance orders, mass dismissals, their application times and the 135 and 16 penalty unit amounts); s 332 (December stand-down); s 333 (stand-down without pay). ss 318(1)-(3), (5)-(6), 319, 321, 324, 334 and 335 are the commission's process and powers and are not encoded, because nothing in them is a figure, a date or a test the employee can work out.
- ch 9 pt 2 div 3 (paying and recovering wages): s 373(1) (wages at least monthly, as a regulative rule); s 376(2)-(3) (recovering an overpayment by deduction); s 378 (a child may claim, in the question text); s 379 (recovery before a magistrate, time and bar)
- s 396 (recovering unpaid superannuation contributions, time limit)
- ch 11: ss 475-477 (the commission's unpaid wages jurisdiction: the $100,000 cap, the bar, the 6 years)

**Out:**

- the rest of ch 2 (minimum wage, hours, flexible work, annual, personal, domestic and family violence, parental and long service leave, public holidays, emergency and jury service leave, superannuation, information statements): entitlements rather than the claims machinery; each would be its own layer
- ss 311 (fee, prescribed by regulation), 312-314 (conciliation and orders on a general protections application: the commission's process), and the general protections themselves (ch 8 pt 1 divs 1-7): what is protected is a separate and large layer
- ss 371-372, 373(2)-(5), 374-375, 377, 380: payment mechanics, apprentices' training time, enforcement of orders
- ch 9 pt 2 divs 4-5 (clothing outworkers, including s 386; rural and mining wages) and ss 394-395
- ch 11 pt 3 div 4 (fair work claims in an Industrial Magistrates Court: the Fair Work Act 2009 (Cwlth) supplies those claims)
- appeals (ch 11 pt 6), civil penalties (ch 11 pt 7), courier service contracts, contract instruments, industrial organisations, and the transitional chapters

## Forks (readings taken where the text leaves a choice)

Recorded under the ruling of 2026-11-05 ("Questions with no convention: decide case by case"), one line each, for a reviewer to overrule.

- **F1** ss 120(c), 315(1)(d), 315(4)(c) with s 125(3)(c); `the employee is engaged for a specific period or task`; a season counts as a specific period; the other reading leaves a seasonal employee outside the s 120 and s 315 exclusions.
- **F2** s 121(1)(b)-(3); `the employer may dismiss without notice or compensation`; a listed kind of misconduct (theft, assault, harassment, fraud, prescribed) answers JUST TRUE unless the employee can show otherwise (JUST FALSE); other conduct answers NOTHING ("includes" leaves the list open); no misconduct answers JUST FALSE ("only if"). The other reading makes every case turn on the "of a type that would make it unreasonable" judgment, with the list only defining "misconduct".
- **F3** s 332(2); `the stand-down public holidays the employer must pay`; a holiday is "between the stand-down and the re-employment" if it falls on or after the stand-down day and before the re-employment day; the other reading excludes a holiday falling on the stand-down day.
- **F4** s 333; `s 333 lets the employer stand the employee down without pay`; outside the grant (the employee can be usefully employed, or the cause is the employer's) the answer is NOTHING (a limit on a grant, ruling (c)); an instrument providing otherwise is JUST FALSE ("unless").
- **F5** s 120; the notice questions return a "does not apply to me (s 120)" answer for an excluded employee, and the s 121 question NOTHING; the other reading answers "no notice is owed", which the text does not say (the employee's contract or instrument may still require notice).

### Rulings on negatives and legal effects, as recorded in docs/ENCODING-GUIDE.md

The rule of 2026-10-29: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

Periods, "where" and scope limits (ruled 2026-11-05): (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`.

The boolean questions here (who s 316 covers, Division 3, s 328, the lapse, the s 376 deduction window, whether an unpaid amount can still be ordered) answer a plain yes or no because the text says no in its own words in each: "does not apply to" (s 315), "if" (s 328), "lapses if ... not, within 6 months" (s 318(4)), "must start within 1 year ... may extend over a period of 6 years" (s 376(3)), "must be made within 6 years" (ss 379(3), 476(4)).

## What the Act turns out to say

1. **The reinstatement application has two clocks with different tests.** s 317(2)(b) lets the commission allow a further period "on an application made at any time", with no test stated; s 310(2), for a general protections dismissal application, allows one only on "exceptional circumstances", with five listed considerations. Both are left to the commission; the rules leave a permission to ask.
2. **A rejected application can be revived by the employee alone.** s 317(4)-(7): the registrar may reject an application from an excluded employee, but written notice within 21 days after the rejection notice is received obliges the commission to deal with it. Asserted (trace and dates).
3. **A shorter probation lifts the probationary exclusion altogether.** s 315(1)(a) excludes the first 3 months "unless the employee and employer agree in writing that the employee serve (i) a period of probation that is shorter than the probationary period". Read literally, an employee who agreed a one-month probation can claim unfair dismissal even when dismissed inside that month: nothing excludes them. Asserted. A court might read the shorter period in as the new exclusion; the text does not.
4. **An unreasonable longer probation does not displace the first 3 months.** If the agreed longer probation is not reasonable, (b) does not apply, but (a) still excludes a dismissal in the first 3 months, because a longer period is not one of (a)'s "unless" cases. Asserted.
5. **s 315(4)(d) is redundant.** Division 3 already does not apply to "an employee with less than 1 year of continuous service" (s 315(5)), which covers every dismissal in the first 3 months.
6. **No regulation is deposited.** s 315(6)-(7) lets a regulation exclude further employees, including by a wage ceiling; none is applied, so an employee a regulation excludes would get a wrong yes. The same goes for ss 121(2)(e), 123(2), 124(3), 125(3)(e) (taken as an input), 311 and 376(4).
7. **Division 3 has no anti-avoidance exception.** s 315(1)(d) lets a fixed-term employee claim unfair dismissal if the main purpose was to avoid division 2, and s 125(4) does the same for redundancy pay, but s 315(4)(c) excludes every employee engaged for a specific period or task from division 3 without exception. Asserted.
8. **Two wordings for the same high income test.** s 315(1)(e) and (4)(f) say "not employed under an industrial instrument"; s 120(f)(i) says "to whom an applicable industrial instrument does not apply". They are read as one fact.
9. **"The wages ... for the 6 months immediately after the dismissal, paid at the rate ... immediately before" (s 322(2)(a))** is read as half a year's wages at that rate. A weekly-rate reading (26 weeks) differs by a few days' pay. The cap for an employee outside an instrument is the lesser of that and half the high income threshold (s 322(2)(b)). Asserted at both sides.
10. **The notice table's edges.** s 123(1)(a) says "not more than 1 year" and "more than 1 year": service of exactly one year (to the anniversary) gets 1 week, a day more gets 2. The extra week for an employee "45 years of age or over" who has "completed at least 2 years" applies on the 45th birthday and the second anniversary. The section does not say on what day service and age are measured; the day the dismissal takes effect is used. Asserted.
11. **Redundancy pay at exactly 2 years** falls in the first row ("at least 1 year but not more than 2 years": 4 weeks); the next day it is 6 weeks. There is no 5-week row. Asserted.
12. **The two unpaid wages forums bar each other unevenly.** s 476(3) bars a commission application if one "has been made under section 379, 386 or 396 for the same matter"; s 379(5) bars a magistrate application only for "section 475 or 396", not s 386. Encoded as written (s 386 itself is out of scope).
13. **The 6 years is counted twice, consistently.** ss 379(3) and 476(4) require the application "within 6 years after the amount claimed became payable", and ss 379(4)(a) and 477(1)(a)(i) limit the order to amounts unpaid "within the 6 years before the date of the application". Read together, an amount that became payable exactly 6 years before the application is in time. Asserted on the anniversary and the day after, including a 29 February start.
14. **An overpayment can be deducted from wages for 6 years, but only if deductions start within 1 year** (s 376(3)). This does not limit the employer's other ways to recover (s 376(2) "Without limiting"). Asserted.
15. **The December stand-down rule counts dismissal as a stand-down** (s 332(3)), so an employee dismissed in December and re-employed by the end of January is owed the four named holidays that fall between. The section names calendar days; whether a substituted public holiday counts is not read. Asserted, with fork F3.

## Before relying on it

- Deposit the Industrial Relations Regulation 2018 and apply its exclusions, prescribed misconduct and amounts (finding 6).
- Encode continuity of service (s 132 and the Act's continuity rules) so the start date need not be the employee's own figure.
- Encode the general protections themselves (ch 8 pt 1 divs 1-7), so the s 310 questions can be asked only of an employee who has a claim.
- Add the leave entitlements of ch 2 as a further layer, and an employer seat.
- An independent test pass and a lawyer's review of findings 3, 9 and 10 and forks F1-F3.
