# SEAMS-ANSWERED (ea1)

The seams of `PLAN.md` section 4 that ea1's functions answer.
Each row gives the label, the function (in the module named), and its result type, so the asking part can pass the result into its input `the answer of <label>`.
Types checked against the modules on 2026-11-05 (`l4` 1.6.109).

| seam | label | function (module) | inputs | result type |
| --- | --- | --- | --- | --- |
| S1 | `s 35(a)` | `s 35(a) the workman is one to whom Part 4 applies by virtue of section 35(a)` (`ea1-part4a-rest-hours`) | `the person is a workman` BOOLEAN; `the monthly salary measured against the ceiling` MAYBE NUMBER; `the amount the Minister has prescribed in substitution for $4,500` MAYBE NUMBER | MAYBE BOOLEAN |
| S2 | `s 35(b)` | `s 35(b) the employee is one to whom Part 4 applies by virtue of section 35(b)` (`ea1-part4a-rest-hours`) | `the person is a workman` BOOLEAN; `the employee is employed in a managerial or an executive position` BOOLEAN; `the monthly salary measured against the ceiling` MAYBE NUMBER; `the amount the Minister has prescribed in substitution for $2,600` MAYBE NUMBER | MAYBE BOOLEAN |
| (S3) | `s 35(a)` and `s 35(b)` | the two functions above, wired together by `s 35 Part 4 applies to the employee` (`ea1-part4a-rest-hours`), which takes `the answer of s 35(a)` and `the answer of s 35(b)` | MAYBE BOOLEAN; MAYBE BOOLEAN | MAYBE BOOLEAN |
| S5 | `s 41A(2)` | `s 41A(2) the entitlement to be paid for extra work does not apply to the employee` (`ea1-part4a-rest-hours`) | `the Commissioner has made a written order after considering the operational needs of the employer and the interests of the employee or class of employees` BOOLEAN; `the order covers the employee` BOOLEAN | MAYBE BOOLEAN |
| S13 | `s 65 the principal is liable to pay the salary` | `s 65 the principal is liable to pay the salary` (`ea1-part6-contractors`) | the principal contracts with a contractor for labour or work BOOLEAN; salary is due to a workman by the contractor or a subcontractor BOOLEAN; `the contract is for constructional work` BOOLEAN; `the principal is also a constructional contractor` BOOLEAN | MAYBE BOOLEAN |
| S14 | `s 34 the employer is guilty of an offence under s 21, 22 or 23` | `s 34 the employer is guilty of an offence under s 21, 22 or 23` (`ea1-part3b-deductions`) | `the employer contravenes section 21, 22 or 23` BOOLEAN | MAYBE BOOLEAN |
| Part 4 limit, one day | (keel `s 2(1) "overtime"` asks for "the limit of hours specified in Part 4") | `s 38(1) the limit of hours in one day` (`ea1-part4a-rest-hours`) | `by agreement under the contract of service the number of hours of work on one or more days of the week is less than 8` BOOLEAN; `by agreement ... the number of days on which the employee is required to work in a week is not more than 5` BOOLEAN; `section 38(9) takes the employee out of this section` BOOLEAN; `a written order under section 41A(1) exempts the employee from section 38(1)` BOOLEAN | MAYBE NUMBER |
| Part 4 limit, one week | the same | `s 38(1) the limit of hours in one week` (`ea1-part4a-rest-hours`) | `by agreement ... the number of hours of work in every alternate week is less than 44` BOOLEAN; `section 38(9) takes the employee out of this section` BOOLEAN; `a written order under section 41A(1) exempts the employee from section 38(1)` BOOLEAN | MAYBE NUMBER |
| Part 4 limit, one week (shift work) | the same | `s 40(1) the limit of hours in one week` (`ea1-part4a-rest-hours`) | `section 40 applies to the employee` MAYBE BOOLEAN | MAYBE NUMBER |

Notes:
- S3 (ea2's s 88A) is a use of S1 and S2, not a separate function: ea2 passes the results of the two functions above into its own two inputs.
- S5: the two inputs are plain BOOLEAN facts; the result is `JUST TRUE` when both hold and `NOTHING` otherwise (the section grants a power limited by its own wording; tests in `ea1-tests-part4a.l4`).
- S13: the function is ea1's own with four BOOLEAN inputs; the lead wires its MAYBE BOOLEAN result into ea3's input `the answer of s 65 the principal is liable to pay the salary`.
- `s 35 the monthly salary measured against the ceiling` (`ea1-part4a-rest-hours`, a `Pay for a period` in, MAYBE NUMBER out) works out the number S1 and S2 take; ea2 may call it.
