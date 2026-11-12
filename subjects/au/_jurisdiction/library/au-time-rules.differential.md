# Differential report for `au-time-rules.l4`

Status: measured on binary 1.6.110, with the module whose sha256 is given below; the older binary 1.6.98 was used for `l4 check` and for the tests, not for the differential.

## What was compared

The shared module was compared with each of the nine source modules listed in `au-time-rules.MANIFEST.json`.
A script wrote, for each jurisdiction, two files of `#EVAL` lines.
The first file imports `prelude`, `daydate` and that jurisdiction's own source module, and nothing else.
The second file imports `prelude`, `daydate` and `au-time-rules`, and nothing else.
Both files hold the same probes, one `#EVAL` per line, and the second names the jurisdiction in every call.
Before each run the script copied the module and the nine source modules into a scratch folder, and the copies are what was compiled.
The script printed the sha256 of each source copy against the file in the worktree, and all nine matched.
The scratch copy of the module that was measured has sha256 `5cea7b3bed3ae209a43bc17afdc2aa5446fd99204d7907001ac40edc45a35200`.
The file in this folder, sha256 `7f4d21e955392b1ef653369d8116f7d5a39a5187774357be5552d4ef3ae72afa`, differs from it in four comment lines only (the wording of two NOTHING remarks); after that change `l4 check` and all 1005 assertions of the tests were run again on both binaries, and the differential was not run again.
`JL4_LIBRARY_PATH` was unset for every run, so each binary used its own embedded prelude.

## How a run was accepted

A run was accepted when it produced no error other than an evaluation error on a single probe, and printed exactly one result for every probe.
The binary exited with code 0 in 12 of the 18 runs (nine jurisdictions, two sides each).
In the SA, Tas, ACT runs, on both sides, it exited with code 1, because of the evaluation errors listed in the section on probes that stop with an error; every probe still printed one result.
Those three jurisdictions were run again with the probes that supply 2.5 removed: SA 908 / 908; Tas 783 / 783; ACT 1241 / 1241, and both sides exited with code 0.
Results were matched to probes by line number, so a run that printed nothing could not compare equal to another run that printed nothing.
The two sides print different type names, so each side's answer is converted to a common form before comparing: a date, a number, `TRUE`, `FALSE` or `NOTHING`.
A moment is compared as a number: the day's serial number times 3, plus 0 for the beginning of the day, 1 for the last moment of the day, or 2 for midnight at the end of the day.
An evaluation error on a single probe counts as that probe's result; where both sides stop with the same error, that counts as agreement and is listed in its own section below.
A probe for which the source module has no function is not counted in `agree / probes`; it is checked separately that the shared module prints `NOTHING` for it.

## The probe grid

Dates include month ends (31 January 2024 and 2025, 28 and 29 February, 31 March, 30 April, 30 June), leap days (29 February 2024 and 2028), and year ends (31 December 2024 and 2025, 1 January 2026).
Each weekday is covered by the seven days from Monday 3 March 2025 to Sunday 9 March 2025.
Holiday inputs are eight sets: none; a public holiday on 3 March 2025 covering the whole day; the same covering only part of the day; a bank holiday; a public service holiday; a day the office is closed; a run of several kinds on 3 to 7 March 2025; and the Christmas days of 2025 with a bank holiday on 1 January 2026.
Counts include whole numbers, zero, and 2.5 where a jurisdiction does not check for a whole number.
Ages include 29 February birthdays and the eighteenth anniversary.
Each family has the same grid for every jurisdiction, and the grid sizes are in the table of grid sizes below.

## Totals

Probes for which a source module has a function: 8571.
Probes on which the two sides agree: 8571.
Probes on which they disagree: 0.
Probes for which the source module has no function: 6612.
Probes among them on which the shared module prints `NOTHING`: 6612.
Probes on which both sides stop with the same evaluation error (included in the agreeing count): 32.

| Jurisdiction | agree / probes | not encoded: NOTHING / checks |
|---|---|---|
| Cth | 970 / 970 | 717 / 717 |
| NSW | 1042 / 1042 | 645 / 645 |
| Vic | 857 / 857 | 830 / 830 |
| Qld | 1165 / 1165 | 522 / 522 |
| WA | 667 / 667 | 1020 / 1020 |
| SA | 936 / 936 | 751 / 751 |
| Tas | 819 / 819 | 868 / 868 |
| ACT | 1278 / 1278 | 409 / 409 |
| NT | 837 / 837 | 850 / 850 |

## agree / probes, by family and jurisdiction

Each cell is the number of probes on which the two sides agree over the number of probes for which the source module has a function.
`none` means the source module has no function for the family.

| Family | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| F01 does a period expressed this way include the specified day | 7 / 7 | 2 / 2 | 6 / 6 | 3 / 3 | 6 / 6 | 8 / 8 | 2 / 2 | 7 / 7 | 10 / 10 |
| F02 the first day counted in a period | 28 / 28 | 8 / 8 | 24 / 24 | 12 / 12 | 12 / 12 | 16 / 16 | 8 / 8 | 28 / 28 | 8 / 8 |
| F03a the last day of a period of days | 56 / 56 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 56 / 56 | 42 / 42 | 42 / 42 | 42 / 42 |
| F03b the last day of a period of months | 74 / 74 | 46 / 46 | 46 / 46 | 54 / 54 | 54 / 54 | 72 / 72 | 46 / 46 | 54 / 54 | 46 / 46 |
| F03c the last day of a period of years or calendar years | 37 / 37 | 46 / 46 | 23 / 23 | 27 / 27 | 27 / 27 | 36 / 36 | 23 / 23 | 54 / 54 | 23 / 23 |
| F03d the last day of a period of weeks | 48 / 48 | 24 / 24 | 24 / 24 | 48 / 48 | 48 / 48 | 48 / 48 | 24 / 24 | 48 / 48 | 24 / 24 |
| F04 the last day of a period that ends by reference to a day | 28 / 28 | none | 24 / 24 | none | 8 / 8 | 12 / 12 | none | none | none |
| F05 the first day of a period of days that ends by reference to a day | none | none | none | 24 / 24 | 24 / 24 | none | 24 / 24 | 72 / 72 | 24 / 24 |
| F06 the latest day on which a thing may be done | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 | 64 / 64 |
| F07 the day a time calculated backwards is taken to fall on | none | none | none | 56 / 56 | none | none | 56 / 56 | none | none |
| F08 the latest day on which a thing may be done within a period | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 | 90 / 90 |
| F09 is a day of rest | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 | 80 / 80 |
| F10 is a business day | 64 / 64 | 64 / 64 | none | 64 / 64 | none | 64 / 64 | none | 64 / 64 | 64 / 64 |
| G01a comes into operation | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 | 42 / 42 |
| G01b stops operating | none | 42 / 42 | 42 / 42 | 42 / 42 | none | 42 / 42 | 42 / 42 | 42 / 42 | none |
| G01c midnight | none | 42 / 42 | 42 / 42 | 42 / 42 | none | none | none | 42 / 42 | none |
| G02 the day an Act that says nothing about its commencement commences | 42 / 42 | 42 / 42 | none | 42 / 42 | 42 / 42 | 42 / 42 | none | 42 / 42 | 42 / 42 |
| G03 the day an Act commences when the day fixed is not later than the day of publication | none | 80 / 80 | 80 / 80 | 80 / 80 | none | none | none | 80 / 80 | none |
| G04 the day an Act to commence on a day to be fixed commences automatically | none | none | 106 / 106 | 106 / 106 | none | 106 / 106 | none | 106 / 106 | none |
| G05 the day an amending Act is repealed automatically | none | 62 / 62 | none | 62 / 62 | none | none | none | 62 / 62 | none |
| G06a the day a person attains an age in years | 70 / 70 | 70 / 70 | 10 / 10 | none | none | 70 / 70 | none | 70 / 70 | 70 / 70 |
| G06b the age in years of a person on a day | none | none | none | 55 / 55 | none | none | none | 55 / 55 | none |
| G07 the day service by post is taken to be effected | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 | 54 / 54 |
| G08 the n-th sitting day after a day | 120 / 120 | 120 / 120 | none | none | none | none | 120 / 120 | none | 120 / 120 |
| G09 financial years and calendar years | 56 / 56 | 12 / 12 | 48 / 48 | 36 / 36 | 32 / 32 | 24 / 24 | 32 / 32 | 24 / 24 | 24 / 24 |
| G10 clear days and days between events | none | none | none | 30 / 30 | 32 / 32 | none | 60 / 60 | 46 / 46 | none |
| F11 the limit on the search for a day that is not a day of rest | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 | 10 / 10 |

## Not encoded: the shared module prints NOTHING, by family and jurisdiction

Each cell is the number of probes on which the shared module printed `NOTHING` over the number of probes for which the source module has no function.

| Family | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| F01 does a period expressed this way include the specified day | 3 / 3 | 8 / 8 | 4 / 4 | 7 / 7 | 4 / 4 | 2 / 2 | 8 / 8 | 3 / 3 | none |
| F02 the first day counted in a period | 12 / 12 | 32 / 32 | 16 / 16 | 28 / 28 | 28 / 28 | 24 / 24 | 32 / 32 | 12 / 12 | 32 / 32 |
| F03a the last day of a period of days | 14 / 14 | 28 / 28 | 28 / 28 | 28 / 28 | 28 / 28 | 14 / 14 | 28 / 28 | 28 / 28 | 28 / 28 |
| F03b the last day of a period of months | 16 / 16 | 44 / 44 | 44 / 44 | 36 / 36 | 36 / 36 | 18 / 18 | 44 / 44 | 36 / 36 | 44 / 44 |
| F03c the last day of a period of years or calendar years | 53 / 53 | 44 / 44 | 67 / 67 | 63 / 63 | 63 / 63 | 54 / 54 | 67 / 67 | 36 / 36 | 67 / 67 |
| F03d the last day of a period of weeks | none | 24 / 24 | 24 / 24 | none | none | none | 24 / 24 | none | 24 / 24 |
| F04 the last day of a period that ends by reference to a day | 12 / 12 | 40 / 40 | 16 / 16 | 40 / 40 | 32 / 32 | 28 / 28 | 40 / 40 | 40 / 40 | 40 / 40 |
| F05 the first day of a period of days that ends by reference to a day | 72 / 72 | 72 / 72 | 72 / 72 | 48 / 48 | 48 / 48 | 72 / 72 | 48 / 48 | none | 48 / 48 |
| F06 the latest day on which a thing may be done | none | none | none | none | none | none | none | none | none |
| F07 the day a time calculated backwards is taken to fall on | 56 / 56 | 56 / 56 | 56 / 56 | none | 56 / 56 | 56 / 56 | none | 56 / 56 | 56 / 56 |
| F08 the latest day on which a thing may be done within a period | none | none | none | none | none | none | none | none | none |
| F09 is a day of rest | none | none | none | none | none | none | none | none | none |
| F10 is a business day | none | none | 64 / 64 | none | 64 / 64 | none | 64 / 64 | none | none |
| G01a comes into operation | none | none | none | none | none | none | none | none | none |
| G01b stops operating | 42 / 42 | none | none | none | 42 / 42 | none | none | none | 42 / 42 |
| G01c midnight | 42 / 42 | none | none | none | 42 / 42 | 42 / 42 | 42 / 42 | none | 42 / 42 |
| G02 the day an Act that says nothing about its commencement commences | none | none | 42 / 42 | none | none | none | 42 / 42 | none | none |
| G03 the day an Act commences when the day fixed is not later than the day of publication | 80 / 80 | none | none | none | 80 / 80 | 80 / 80 | 80 / 80 | none | 80 / 80 |
| G04 the day an Act to commence on a day to be fixed commences automatically | 106 / 106 | 106 / 106 | none | none | 106 / 106 | none | 106 / 106 | none | 106 / 106 |
| G05 the day an amending Act is repealed automatically | 62 / 62 | none | 62 / 62 | none | 62 / 62 | 62 / 62 | 62 / 62 | none | 62 / 62 |
| G06a the day a person attains an age in years | none | none | 60 / 60 | 70 / 70 | 70 / 70 | none | 70 / 70 | none | none |
| G06b the age in years of a person on a day | 55 / 55 | 55 / 55 | 55 / 55 | none | 55 / 55 | 55 / 55 | 55 / 55 | none | 55 / 55 |
| G07 the day service by post is taken to be effected | none | none | none | none | none | none | none | none | none |
| G08 the n-th sitting day after a day | none | none | 120 / 120 | 120 / 120 | 120 / 120 | 120 / 120 | none | 120 / 120 | none |
| G09 financial years and calendar years | none | 44 / 44 | 8 / 8 | 20 / 20 | 24 / 24 | 32 / 32 | 24 / 24 | 32 / 32 | 32 / 32 |
| G10 clear days and days between events | 92 / 92 | 92 / 92 | 92 / 92 | 62 / 62 | 60 / 60 | 92 / 92 | 32 / 32 | 46 / 46 | 92 / 92 |
| F11 the limit on the search for a day that is not a day of rest | none | none | none | none | none | none | none | none | none |

## Grid sizes

The brief asks for at least 40 inputs per family.
Every family's grid has at least 40 inputs, except the two below, where the family has fewer than 40 distinct inputs to give.

- F01 does a period expressed this way include the specified day: 10 inputs, which is every one of the ten ways a period can be expressed; the grid is exhaustive.
- F11 the limit on the search for a day that is not a day of rest: 10 inputs, the positions 0, 1, 5, 50, 398, 399, 400, 401, 402 and 449 in a run of 450 consecutive public holidays, around the limit of 400 days.

Inputs in each family's grid: F01 10; F02 40; F03a 70; F03b 90; F03c 90; F03d 48; F04 40; F05 72; F06 64; F07 56; F08 90; F09 80; F10 64; G01a 42; G01b 42; G01c 42; G02 42; G03 80; G04 106; G05 62; G06a 70; G06b 55; G07 54; G08 120; G09 56; G10 92; F11 10.

The number of inputs compared against a source module is smaller where that module takes only some of the grid, for example a module that accepts three of the ten ways to express a period.
The `agree / probes` table above gives every count; the cells with fewer than 40 compared inputs are these.

- F01 does a period expressed this way include the specified day: Cth 7, NSW 2, Vic 6, Qld 3, WA 6, SA 8, Tas 2, ACT 7, NT 10.
- F02 the first day counted in a period: Cth 28, NSW 8, Vic 24, Qld 12, WA 12, SA 16, Tas 8, ACT 28, NT 8.
- F03c the last day of a period of years or calendar years: Cth 37, Vic 23, Qld 27, WA 27, SA 36, Tas 23, NT 23.
- F03d the last day of a period of weeks: NSW 24, Vic 24, Tas 24, NT 24.
- F04 the last day of a period that ends by reference to a day: Cth 28, Vic 24, WA 8, SA 12.
- F05 the first day of a period of days that ends by reference to a day: Qld 24, WA 24, Tas 24, NT 24.
- G06a the day a person attains an age in years: Vic 10.
- G09 financial years and calendar years: NSW 12, Qld 36, WA 32, SA 24, Tas 32, ACT 24, NT 24.
- G10 clear days and days between events: Qld 30, WA 32.
- F11 the limit on the search for a day that is not a day of rest: Cth 10, NSW 10, Vic 10, Qld 10, WA 10, SA 10, Tas 10, ACT 10, NT 10.

## Probes on which both sides stop with the same error

- SA, F03b the last day of a period of months: 9 probes, `eval/not-an-integer`, for example `n=2.5 unit=Months how=begins at, on or with a specified day anchor=(31, 1, 2025)`.
- SA, G06a the day a person attains an age in years: 10 probes, `eval/internal-error`, for example `born=(29, 2, 2024) years=2.5`.
- Tas, F03b the last day of a period of months: 6 probes, `eval/not-an-integer`, for example `n=2.5 unit=Months how=begins from a specified day anchor=(31, 1, 2025)`.
- ACT, G06a the day a person attains an age in years: 7 probes, `eval/internal-error`, for example `born=(28, 2, 2001) years=2.5`.

The probe supplies a count of 2.5 where the jurisdiction's module does not check for a whole number; the source module and the shared module both reach the same evaluation error.

## Positive controls

A differential that agrees everywhere proves little unless it can be shown to disagree when the module is wrong.
So the module was changed in one place (`JUST (anchor PLUS n)` became `JUST (anchor PLUS (n PLUS 1))`, which affects the jurisdictions that count days from the given day) and the differential was run again on Cth, Vic, Qld, Tas and NT for families F03a and F08.
Result: Vic F03a 0 / 42 and F08 47 / 90; Qld F03a 6 / 42 and F08 30 / 90; Tas F03a 0 / 42 and F08 81 / 90; NT F03a 12 / 42 and F08 47 / 90; Cth, which does not use that line, stayed at 56 / 56 and 90 / 90.
Running the changed module against the tests file produced 13 failed assertions out of 1005.
The first full differential run also found a real defect in an earlier draft of the module: the Cth business-day branch read `NOT (a) AND NOT (b)` as `NOT ((a) AND NOT (b))`, and three probes disagreed until each operand was parenthesised.

## Where the module answers NOTHING instead of reproducing a source module

No probe in the grid disagrees, so none of the cases below was reached by a probe as a disagreement.
Each is a case where a source module computes something that the shared surface does not carry, found by reading the source modules against the shared module.

- Cth: `the day the enactment commences` (s 3A): an Act to alter the Constitution commences on the day of Royal Assent (s 3A(3)); the shared function has no argument for the kind of Act and gives the s 3A(2) day only.
- Cth: `the last day on which the thing may be done` (s 36(2)): the source takes a flag that an Act requires or allows the thing to be done, and returns the last day unchanged when the flag is FALSE; the shared function has no flag and reproduces the TRUE case.
- NSW: `s 24 the moment an Act or statutory rule commences on a particular day`: the source answers NOTHING for another instrument; the shared function takes no kind of text and answers as the source does for an Act or a statutory rule.
- NSW: `s 23(1) and (5) the day an Act commences`: the basis in which a day is appointed under s 23(2) (no earlier than the date of assent and no later than 28 days after it) is not carried; the shared function takes a fixed day and a publication day.
- Vic: `s44(3) day to which a time limited for doing an act or thing extends`: the source takes a flag that the time is limited for doing an act or thing, and answers NOTHING when the flag is FALSE; the shared function reproduces the TRUE case.
- Vic: `the day an Act that says nothing about its commencement commences` answers NOTHING: Vic s 10A is carried by `the day an Act to commence on a day to be fixed commences automatically`.
- Tas: `the day an Act that says nothing about its commencement commences` answers NOTHING: tas-interpretation-time s 9(2) and (3) depend on the day section 8 of the 1981 amending Act commenced, which that module takes as an input and this surface does not.
- ACT: `s 89 (1): the day an amending law is automatically repealed`: the alternative limb of paragraph (b) is not read.
- NSW, Vic, Qld, SA: `the day service by post is taken to be effected`: the NSW function's ordinary-course day (s 76(1)(b)) is not read, and neither is a flag in the Vic (s 49), Qld (s 39A(1)(b)) and SA (s 51(5)) functions; the branch comments say what each branch computes.
- All nine: a period of weeks answers NOTHING for every jurisdiction, as the source modules that mention a period of weeks return NOTHING for it.
- Cth, WA, SA, ACT: the alternative-reading functions (Cth 2, WA 2, SA 2, ACT 3, found by a text match on the function names) are not carried; the Vic readings A and B are both inside `the last day of months where Vic's two readings agree`.
- NSW, Vic, WA, SA, Tas, ACT, NT: the functions that compare points in time or ask whether a provision is in operation at a moment (for example SA `ss 28 and 30: a provision is in operation at a moment`, WA `a written law is in operation at`, ACT `s 74: the first point is earlier than the second`) are not carried.
- All nine: the further families of source functions listed at the end of the NOTES (points in time, repeal, commencement of other instruments, dates the Acts name, time of day, duties with no time provided, sitting days and regulations, appointments, service, ages, and the components of the carried rules) are not carried.

The NOTES also list, mechanically, every function in a source module whose name does not appear in the shared module, with a count per module.

## Adapters used on the source side

The source modules differ in how they take their inputs, so a small adapter turns each probe into a call to the source function.
The adapters only reshape inputs and outputs; where an adapter had to choose, the choice is listed here.

- Qld and Tas have no function for the first day counted in a period; the F02 probes for them use their functions that say whether a given day is counted.
- Holiday lists are passed as the dates of the public holidays, the bank holidays or the days the office is closed, according to what each source function takes; only SA and NT read the part-day flag.
- Sitting days are a list of dates in the shared module; the Cth source takes sitting records with a beginning and an adjournment, so the adapter builds records whose two days are the same.
- For the ACT calendar-year unit the adapter calls the source function for a run of calendar years, which starts on 1 January.
- For the moment families the adapters convert each module's own moment type to the number described above.
- A source function that takes the year in which a financial year begins (Qld, SA, ACT) is called with the year before the year of ending.

## Unnamed source functions

| Jurisdiction | Functions in the source module | Names that do not appear in the shared module |
|---|---|---|
| Cth | 27 | 10 |
| NSW | 31 | 13 |
| Vic | 48 | 29 |
| Qld | 34 | 12 |
| WA | 35 | 21 |
| SA | 35 | 19 |
| Tas | 61 | 41 |
| ACT | 60 | 39 |
| NT | 39 | 25 |

The test is a text match on the function name, so a function that is carried under different wording is counted as unnamed, and a name that appears only in a comment is counted as named.
The list is in the NOTES.
