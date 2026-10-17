# National Minimum Wage Act 1998 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the national minimum wage position for` (`nmw-goal.l4`). For one individual it answers:

- whether they qualify;
- how much additional remuneration they are owed for the pay reference periods in which they were paid less than the national minimum wage;
- if they gave a production notice: the last day for the employer to produce the records, the last day to present a complaint, and the award.

Three goals sit under it:

1. **Who qualifies** (`nmw-qualification.l4`):
   - the conditions in s 1(2), with the s 54(3) worker, s 34 agency workers, s 35 home workers and s 40 mariners;
   - the exclusions in ss 37, 37A, 43, 44, 44A, 45, 45A and 45B, plus s 3 regulations as an input;
   - the s 28(1) presumption in civil proceedings.
2. **Arrears under s 17** (`nmw-arrears.l4`):
   - the higher of the shortfall A and A/R1 × R2;
   - reduced by the additional remuneration already paid (s 17(6));
   - nothing more once it has been paid in full at any time (s 17(5)).
3. **Access to records** (`nmw-records.l4`):
   - the production deadline (s 10(9));
   - the complaint time limit (s 11(3)), with the early conciliation extension (s 11A);
   - the award of 80 times the hourly rate (s 11(2)).

As the user asked, this covers only the sections those goals need. The rest of the Act was left out on purpose (see the table).

The rates are inputs, because the Act prescribes none: the national minimum wage and each age band's rate are set by regulations under ss 1(3) and 3. So are the hours and the remuneration that counts, which are worked out under the s 2 regulations.

Dates are computed as the Act words them. The UK has no general next-working-day rule, so no date moves for a weekend or bank holiday.

## Coverage

| Provision | Disposition |
|---|---|
| s 1(1)-(2), (5) | encoded (goal 1, and s 1(1) in goal 2) |
| s 1(3)-(4), ss 2, 4 | input: the rate, the pay reference period, and the s 2 method (hours and remuneration) |
| s 3 | input: whether regulations prevent the person from qualifying; the age-band rate as R1 and R2 |
| ss 5-8 (Low Pay Commission) | out of scope: no computable answer for a worker |
| s 9 | out of scope: the duty to keep records is made by regulations |
| s 10 | encoded: (2) the reasonable belief, (9) the production deadline |
| s 11(1)-(4) | encoded: the complaint, the time limit, the award, late complaints as an input |
| s 11(4A)-(4B), s 11A | encoded: the early conciliation extension (Great Britain); Northern Ireland's Article 249B is not |
| s 12 | out of scope: the statement is made by regulations |
| ss 13-16, 19-22F | repealed in this version (they print as dots) |
| s 16A | out of scope |
| s 17 | encoded (goal 2) |
| s 18 | out of scope: it makes s 17 enforceable through the Employment Rights Act 1996 Part II; no computation |
| ss 23-26 | out of scope: detriment and dismissal apply the Employment Rights Act 1996 |
| ss 27, 29, 30 | out of scope: tribunal procedure |
| s 28(1) | encoded (goal 1) |
| s 28(2)-(3) | out of scope: these presume underpayment in deduction and contract claims; arrears are worked out from the given facts |
| ss 31-33 | out of scope: offences |
| ss 34, 35, 37, 37A, 40 | encoded (goal 1) |
| ss 36, 38, 39 | out of scope: Crown, House of Lords and House of Commons staff are covered like other employment |
| ss 41, 42 | out of scope: powers to extend the Act |
| ss 43-45B | encoded (goal 1) |
| ss 46-47 | out of scope: agricultural wages |
| ss 48, 49 | out of scope: superior employers and contracting out |
| ss 50-56, Schedules | out of scope |

## Forks (readings taken)

- **F1, s 17(1).** "Remunerated ... at a rate which is less than the national minimum wage" is taken as relevant remuneration below R1 × the hours, both worked out under the s 2 regulations. A rate of exactly R1 is not less, so s 17 does not apply.
- **F2, s 17(4).** The conversion lost the formula. Its printed form is A/R1 × R2, and the encoding uses that. Nothing is rounded: the Act states no rounding.
- **F3, s 17(5)-(6).** Each payment of additional remuneration is tested against the entitlement at the time it was made, using R2 as it stood then:
  - a payment of at least that entitlement ends s 17(1) for the period, and later rate rises revive nothing;
  - otherwise the payment reduces both amounts in s 17(1).
- **F4, s 28(1).** The three conditions in s 1(2) are inputs that may be not established (NOTHING).
  - In civil proceedings, a condition that is not established is presumed met.
  - Outside civil proceedings it is refused.
  - An exclusion counts only when its facts are established, which is the same thing as the presumption.
- **F5, s 10(9)(a).** "The period of fourteen days following the date of receipt" starts the next day, so its last day is receipt + 14.
- **F6, s 11(3).** "The period of three months following" a day ends on the corresponding day three months later, or on the last day of that month if it has no corresponding day.
- **F7, s 11A(2).** The days from the day after Day A to Day B are left out only if the limit is still running after Day A. If Day A is on or after the last day, (2) adds nothing, and (3) still applies when the limit falls between Day A and one month after Day B.
- **F8, s 11.** The award does not depend on qualification under s 1(2). Sections 10-11 give the rights to "a worker" who believes on reasonable grounds that they were underpaid.
- **F10, s 17(6).** The payments are taken off the higher amount: max(A, A/R1 × R2) − paid. The other reading would reduce A before uprating, giving (A − paid)/R1 × R2. The two readings give different answers whenever R2 differs from R1. The words "the amounts described in subsections (2) and (4) ... shall be regarded as reduced by the amount of that remuneration" reduce each amount by the payment, not A before the formula.
- **F11, s 11(3), and Dodds v Walker.** The corresponding-day rule in F6 differs from a count that runs to the end of the month only when the start day is the last day of a short month. For example, from 28 February 2027 the limit is 28 May, not 31 May.
- **F12, the top-level goal.** Outside civil proceedings, with a condition of s 1(2) not established and no exclusion established, `qualifies` and `additional remuneration owed` are NOTHING. The records fields still answer, because ss 10-11 do not depend on qualifying. This was changed after the independent pass: before, the whole position refused.
- **F9, s 44(2).** The condition that the body the work is done for is a charity, voluntary organisation, associated fund-raising body or statutory body is folded into one input: placed by a charity with such a body.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-17:

- 7 modules: 165 assertions satisfied, 0 failed, 0 other errors;
- 62 are the encoder's (`nmw-tests.l4`);
- 103 are independent (`tests-independent.l4`).

No assertion is expected to fail.

Where the encoding refuses: outside civil proceedings, a s 1(2) condition that is not established refuses in `qualifies for the national minimum wage`, and gives NOTHING at the top level.

## Open questions for a UK lawyer

- **F7.** Should early conciliation begun after the s 11(3) limit has expired get the s 11A(3) extension when Day A is the last day itself?
- **The ss 19-22F gap.** The revised text as at 7 April 2026 shows ss 19-22F (notices of underpayment and penalties) as repealed. Confirm that this matches the enforcement regime now in force.
