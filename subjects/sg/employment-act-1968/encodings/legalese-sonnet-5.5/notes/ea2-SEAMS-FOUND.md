# Seams found by part ea2 that PLAN.md section 4 lacks, and one it lists that ea2 did not take

Format as PLAN.md section 4 asks: asking section, answering section, the input name and the type used.

| # | asking section (ea2) | answering section | input name and type used | note |
| --- | --- | --- | --- | --- |
| F-S1 | s 87A(3): "The childcare leave is in addition to the rest days, holidays, annual leave and sick leave to which an employee is entitled under sections 36, 88, 88A and 89" | s 36 (ea1: rest days); ss 88, 88A, 89 are in ea2 itself | `the rest days under section 36`: NUMBER (a plain count the caller states) | The total in `s 87A(3) the total days off the employee is entitled to` adds five counts. The holidays, annual leave and sick leave counts are this part's own answers, passed in by the caller as numbers; the rest-days count is ea1's. No MAYBE: a count of days is a plain comparison. |
| F-S2 | s 84A(3): "in addition to any retrenchment benefit or other payment" | s 45 "Payment of retrenchment benefit" (ea1; heading at line 2097 of EmA1968.txt) | none taken: `s 84A(3) the payment is in addition to a retrenchment benefit or other payment` asks only whether the payment is one that s 84A(1) refers to | s 45 is ea1's; nothing in s 84A(3) needs its amount or whether it is payable, so no input crosses the seam. |
| F-S3 | s 84(2) and s 84(3): "section 3 of the Employment Claims Act 2016 allows the claim"; "the Tribunal" | the Employment Claims Act 2016 (not among the sources); the keel's `s 2(1) "Tribunal"` | `section 3 of the Employment Claims Act 2016 allows the claim`: MAYBE BOOLEAN (asked as a fact); `the answer of s 2(1) "Tribunal"`: MAYBE BOOLEAN (the keel's definition) | A borrowed term, asked as an input (Guide section 4). |
| F-S4 | s 76(4) and s 76(5): "a class of employees the Minister has specified by notification in the Gazette" | the Minister's notification (not among the sources) | `she belongs to a class of employees the Minister has specified by notification in the Gazette`: BOOLEAN | Asked as a fact. |

## PLAN seams that ea2 did not take

| # | asking section | why not |
| --- | --- | --- |
| S14 | s 105(1)(a): "an offence under section 21, 22 or 23 read with section 34" | s 105(1)(a) turns on what the inspecting officer REASONABLY SUSPECTS, not on whether the offence was committed, so s 34's answer (`the answer of s 34 the employer is guilty of an offence under s 21, 22 or 23`) is not the fact the sub-paragraph needs. `s 105(1) the inspecting officer may arrest the person without warrant` takes the suspicion as a plain BOOLEAN input. If the lead wants S14 wired, it would feed a plain BOOLEAN only where the officer's suspicion is the s 34 offence in fact. |

## Seams taken as inputs (the asking side in ea2), for reference

S1, S2, S3: `the answer of s 35(a)`, `the answer of s 35(b)` (MAYBE BOOLEAN), in ea2-part-10-holiday-annual.l4 (s 88(4A), s 88A(6)) and ea2-duties.l4 (s 88A(6)(a)).
S5: `the answer of s 41A(2)` (MAYBE BOOLEAN), in s 88(4).
S6: `the answer of sch 3 gross rate of pay per day` and `the answer of sch 3 basic rate of pay per day` (MAYBE NUMBER), in ss 76(1A), 76(3), 79(1), 87A(5), 88(4), 88(4A), 88A(7), 88A(8), 89(5) and 107A(1) and (2).
S8: `the answer of sch 5 days` (MAYBE NUMBER), in s 76(1)(c)(ii).
