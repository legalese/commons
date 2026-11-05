# SEAMS-ANSWERED (ea3)

The seams of PLAN.md section 4 that ea3 answers.
Each row gives the label, the function in `ea3-schedules.l4`, what it takes and its result type.
A caller passes the answer in as the input PLAN.md names; it does not recompute the Schedule.
Every function below answers `NOTHING` when the Schedule gives no answer on the facts passed in; the file's `-- NOTHING-kind` comments say why each time.

| seam | label | function | takes | result |
| --- | --- | --- | --- | --- |
| S6 | Third Schedule, second column | `sch 3 the gross rate of pay for one day` | one `sch 3 Facts about the pay` (the arrangement of pay, the pay earned in the 14 days, the days worked in them, the monthly pay, the days required in the first and second weeks, the weeks for item 5's average, the rate under a formula the Commissioner approved) | MAYBE NUMBER |
| S6 | Third Schedule, third column | `sch 3 the basic rate of pay for one day` | the same `sch 3 Facts about the pay` | MAYBE NUMBER |
| S7 | Fourth Schedule | `sch 4 the hourly basic rate of pay` | one `sch 4 Facts about the pay` (the type of employee in the First column and the figures each type uses) | MAYBE NUMBER |
| S8 | Fifth Schedule | `sch 5 the number of days on which the female employee is entitled to absent herself` | one `sch 5 Facts about the work pattern` (the pattern, the work days in a week, the fixed weeks, the 3 weeks before the earlier of confinement and the first day of leave) | MAYBE NUMBER |
| keel "workman" limb (d) | First Schedule | `sch 1 the person is specified in the First Schedule` | the occupation (a `sch 1 Kind of occupation`), whether the person is on piece rates in the employer's premises, whether the person is a workman by another limb | MAYBE BOOLEAN |

Also in `ea3-schedules.l4` and offered to other parts: `sch 2 the registration fee` (takes a `Kind of claimant`, MAYBE NUMBER), `sch 3 item 5 the average number of working days in a week` (MAYBE NUMBER), `sch 5 item 4 the day by reference to which the work pattern is determined` (DATE).

The seams ea3 asks of other parts (S9 to S13) and the extra seams it found are in `SEAMS-FOUND.md` (asked) and listed in NOTES.md, "Seams (ea3)".
