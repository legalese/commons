# Montana unemployment insurance (MCA Title 39, ch. 51, parts 2, 21, 22, 23) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the claimant, with the design defaults ruled on 2026-10-18.
A seat-neutral core (`mt-ui.l4`) holds the rules in the Code's own terms. The seat layer (`mt-ui-seat.l4`) asks the claimant's questions, with `@export` and a `@desc` on every input, from plain facts: the wages paid in each of the last five completed quarters, the week's hours and earnings, and how the job ended. It restates no rule.
`mt-ui-cases.l4` tests the seat layer.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.** There was no earlier encoding of this subject.

## Edition

Montana Code Annotated 2025 (laws through the 2025 session), site marked "Updated August 2026", retrieved 2026-10-19 UTC. It is deposited at `../../registers/source-bundle/mca-39-51-part-2.txt`, `-part-21.txt`, `-part-22.txt` and `-part-23.txt`.

Two figures set each year are inputs, because nothing that sets them is deposited:

- **The average annual wage.** The department computes it each year from contribution reports (39-51-2201(2)).
- **Whether contribution Schedule I is in force.** This is decided under 39-51-1218, which is in part 12 and not deposited.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mt-ui.l4` (core), `mt-ui-seat.l4` (seat) | `mt-ui-cases.l4` | 40 written, 40 satisfied |

`l4 run` on all three files gave 0 errors and 0 warnings (2026-10-24). One `#TRACE` checks a breach: the department gives no advice at filing. Its `-- expect:` comment was read against the output, which ends `BREACH BY the department of labor and industry`.
Every expected value was worked out by hand from the text. One hand calculation was wrong at first (66.5% of $1,153.85 is $767.31025, not $767.30025). It was corrected by redoing the arithmetic, not by copying the output.

## Seat

**The claimant**: a person who has lost work in Montana and asks the following.

- "Do I qualify?"
- "How much a week, and for how many weeks?"
- "Am I disqualified because of how my job ended?"
- "Must I take this job?"
- "What do I get for a week I worked part-time?"
- "Must I pay it back?"

The defaults of 2026-10-18:

- **The Code alone.** The parts deposited, with the yearly figures as inputs.
- **The actors the text names:** the claimant (the "individual") and the department of labor and industry.
- **Judgments handed to others are answered conditionally.** Each of these is an input:
  - misconduct and gross misconduct (39-51-201(19), (13), 39-51-2303), as the department determines;
  - good cause;
  - the department's weighing of the 39-51-2304(2) suitability factors;
  - the 39-51-2104(1) findings (able, available, seeking work).
- **Definitions worked out from facts:**
  - the base period (39-51-201(2)(a), (b)), from the five quarters' wages;
  - qualifying wages;
  - total unemployment (39-51-2101);
  - the average weekly wage;
  - suitable work (39-51-2304(3), (4)).
- **One case:** one claim (one benefit year), and one week for the week questions.
- **Machinery out:** contributions and experience rating, administration, the fund, and the department's rule-making.

## Regulative rules

Two `DEONTIC` rules. The parties are parameters.

1. **At a new claim** (`the duties when I file a new claim`), two duties run in parallel (`RAND`), both "at the time" of filing (`WITHIN 0`):
   - **39-51-2208(2):** the claimant **shall disclose** whether a food stamp overissuance is owed.
   - **39-51-2207(1):** the department **shall advise** that benefits are federally taxable, that estimated-tax rules apply, and that withholding **may** be elected and changed. That permission is a `MAY` under the department's `HENCE`.
2. **39-51-2306(2)** (`the duty to repay a doubly paid week`): a claimant later paid workers' compensation or other unemployment benefits for a week already paid **shall repay** those benefits. No time is stated, so the rule has no `WITHIN`.

## Read with the federal frame

These federal laws set what a state UI law must contain:

- FUTA s 3304(a) (`subjects/us/internal-revenue-code-of-1986/`, `usc26-ch23.txt`);
- SSA Title III (`subjects/us/social-security-act/`, `usc42-ch7-schIII.txt`);
- the Federal-State Extended Unemployment Compensation Act of 1970 (`subjects/us/federal-state-extended-unemployment-compensation-act-of-1970/`).

Several of them show up in Montana's text:

- 39-51-2304(3) mirrors FUTA s 3304(a)(5);
- 39-51-2307(3), approved training, mirrors (a)(8);
- 39-51-2207, the withholding election, mirrors (a)(18).

Benefits are gross income under IRC s 85. Cross-folder IMPORT is not possible in the stable `l4`, so these links are recorded here only.

## Scope

**In:**

- 39-51-201(2)(a), (b), (3), (26);
- 39-51-2101;
- 39-51-2104(1), (2);
- 39-51-2105;
- 39-51-2201;
- 39-51-2202;
- 39-51-2203, as an input amount;
- 39-51-2204;
- 39-51-2207(1);
- 39-51-2208(2);
- 39-51-2302;
- 39-51-2303;
- 39-51-2304;
- 39-51-2306(2).

**Out:**

- combined-wage claims and the temporary-disability base period (39-51-201(2)(c), (d));
- 39-51-2102;
- reemployment profiling (39-51-2104(3));
- 39-51-2106 to 39-51-2111: railroad wages; second benefit year; school employees and athletes; aliens; domestic violence;
- 39-51-2205;
- the food stamp deduction mechanics (39-51-2208(3)-(7));
- strikes (39-51-2305);
- receipt of other benefits as a disqualification for the week (39-51-2306(1));
- school attendance (39-51-2307), except as a requalification under 39-51-2302(3);
- extended benefits;
- claims procedure and appeals (part 24, not deposited).

## What the Code turns out to say

1. **Half the average annual wage qualifies on its own.** Section 39-51-2105 has two limbs joined by "or". Under (2), total base-period wages of at least 50% of the average annual wage qualify even when they are earned in a single quarter, so the 1.5-times-the-high-quarter test in (1) need not be met. Asserted (Eve: $31,000 in one quarter qualifies; she gets 8 weeks).
2. **"1% ... or ... 1.9%": the text does not say which.** Section 39-51-2201(1) gives the weekly benefit amount as 1% of base-period wages "or" 1.9% of the two highest quarters, and does not choose between them. This encoding takes the greater. That is an interpretive choice, not checked against department practice. Asserted (Ana: 437, not 420).
3. **The maximum and minimum are not rounded.** The weekly benefit amount is rounded down to the dollar (39-51-2201(1)). The maximum (66.5% or 67.5% of the average weekly wage) and the minimum (19% or 20%) are not rounded anywhere in the text. A capped claimant's amount therefore carries fractions of a cent until the department rounds it. Asserted (Ben: $767.31025).
4. **The alternative base period applies only when the regular one fails.** Section 39-51-201(2)(b) applies only "if the individual does not have sufficient wages to qualify" under (a). It is not available simply because it would pay more. Asserted (Cal qualifies only on the most recent four quarters).
5. **The order of the weekly reductions is not stated.** The text has three reductions: the availability fifths (39-51-2104(2)(a)), the earnings rule (39-51-2202) and the pension offset (39-51-2203). This encoding applies the first two to the weekly benefit amount and then the pension, never going below zero. Partial days count as whole days ("each day or part of a day").
6. **Earning twice the weekly benefit amount, or working 40 hours, ends the week's claim entirely.** In either case the person is not "totally unemployed" (39-51-2101(1)(b)(ii), (2)). So 39-51-2202's partial payment works only below those limits. Asserted.
7. **A drug-test discharge disqualifies with no stated end.** Section 39-51-2303(3) says the individual "must be disqualified for benefits after being discharged" for failing or refusing a compliant test. Unlike (1) and (2), it sets no requalifying earnings and no period. The exception for a marijuana test of a registered cardholder is encoded. Asserted.
8. **"After 13 weeks of unemployment".** This is read as more than 13 weeks. After that point, an offer at 75% of previous insured earnings is suitable work even without the department's weighing, but never one below the federal minimum wage or one barred by (3). Asserted (14 weeks suitable, 13 not).
9. **Refusing suitable work costs twice.** The claimant is disqualified until earning six times the weekly benefit amount. The maximum benefit amount is also cut by six times the weekly benefit amount (39-51-2304(1)(b)). Asserted.

## Before relying on it

- Deposit 39-51-1218 (the contribution schedules), part 24 (claims and appeals) and part 12. Deposit the department's published average annual wage and its maximum and minimum weekly benefit amounts for the benefit year, and replace the inputs with them.
- Check findings 2, 3 and 5 against the department's practice.
- Do an independent test pass.
