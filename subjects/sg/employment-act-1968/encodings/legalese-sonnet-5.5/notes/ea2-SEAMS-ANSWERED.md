# Seams answered by part ea2 (PLAN.md section 4)

Each row is a seam in the PLAN's table whose ANSWERING side is in ea2's range.
The function is defined in the file named, takes the inputs shown in its `GIVEN`, and returns the result type shown.
Where a seam's answer is an input the lead wires at the merge, the asking part's `the answer of <label>` takes exactly this result type.

| PLAN seam | label | function | file | result type |
| --- | --- | --- | --- | --- |
| S4 | s 88A | `s 88A the days of paid annual leave` | ea2-part-10-holiday-annual.l4 | MAYBE NUMBER |
| S9 | s 95(1) | `s 95(1) the employer failed to comply` | ea2-part-12-records.l4 | MAYBE BOOLEAN: JUST TRUE where the Act says the employer failed, NOTHING otherwise (the Act has no sentence that says an employer complied, so no JUST FALSE is given) |
| S10 | s 95A(2) | `s 95A(2) the employer failed to comply` | ea2-part-12-records.l4 | MAYBE BOOLEAN, the same meaning |
| S11 | s 96(1) | `s 96(1) the employer failed to comply` | ea2-part-12-records.l4 | MAYBE BOOLEAN, the same meaning |
| S12 | s 96A with S 200/2019 | `s 96A the employer failed to comply with a requirement in the notification` | ea2-part-12-records.l4 (fed by `S 200/2019 para 3(1) the Notification applies to the employer` and `S 200/2019 the employer met every requirement concerning the report` in ea2-notification.l4) | MAYBE BOOLEAN, meaning "the employer failed to comply with a requirement in the notification" |
| S15 | s 112 | `s 112 first conviction` and `s 112 subsequent conviction` | ea2-part-14.l4 | each MAYBE (`Penalty on conviction`); the caller picks the first or the subsequent one |

The PLAN names the S9 to S12 inputs `the answer of s 95(1)`, `the answer of s 95A(2)`, `the answer of s 96(1)` and `the answer of s 96A`.
The functions above are the rules the lead wires to those inputs.
