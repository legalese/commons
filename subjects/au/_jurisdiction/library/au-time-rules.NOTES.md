# Notes on `au-time-rules.l4`

Status: the module, its tests and its differential were run on 2026-11-12 against commons main ece722340, on binaries 1.6.110 and 1.6.98; this is an assumed design, not ruled, and every file in this folder is new.

## What this module is

`au-time-rules.l4` is one self-contained L4 module that carries the rule families listed in the table below from the nine Australian interpretation-Act time modules, selectable by a `Jurisdiction` (Cth, NSW, Vic, Qld, WA, SA, Tas, ACT, NT).
It does not carry every function of the nine source modules: two counts of definition names in the nine source modules, made by different patterns, found 209 of 370 and 201 of 336 absent by name from the shared module, many of them helpers or longer forms of carried rules and some of them whole rules left out; the "not carried" lines below name what was left out.
Each of the nine source modules declares its own types, so they cannot be imported together, and commons forbids an IMPORT across subjects.
A later Australian encoding that needs a time rule copies this one file instead of re-deriving the rule.
Every behaviour comes from one of the nine source modules; the branch comment on each jurisdiction names the source module and its function.
Where a source module does not encode a rule, the function answers `NOTHING` for that jurisdiction, and the table below says so.
The file describes what each source module computes and does not assess the Acts.

## Files in this folder

| File | Lines | sha256 of the file when these notes were written |
|---|---|---|
| `au-time-rules.l4` | 1647 | `7f4d21e955392b1ef653369d8116f7d5a39a5187774357be5552d4ef3ae72afa` |
| `au-time-rules-tests.l4` | 1514 | `e5e039299064f91357227311415802fce167cf06509907665ac99e8da5d2ca12` |
| `au-time-rules.MANIFEST.json` | 70 | not recorded: it carries the hashes |
| `au-time-rules.differential.md` | 217 | not recorded: it changes with the differential |
| `au-time-rules.NOTES.md` | this file | not recorded |

The manifest lists the nine source modules with their paths, sha256 values and line counts, and also records the module and the tests.

## How a later encoding copies the module

1. Copy `au-time-rules.l4` byte for byte into the folder of the new module, because an IMPORT names a module and only the importing file's own folder is searched.
2. Record in the new encoding's NOTES the path of this original, `subjects/au/_jurisdiction/library/au-time-rules.l4`, and its sha256 from the table above or from `shasum -a 256`.
3. Check the copy with `shasum -a 256` against the recorded value.
4. Write `IMPORT prelude`, `IMPORT daydate` and ``IMPORT `au-time-rules` `` in the new module.
5. Pass a `Jurisdiction` as the first argument of every function that takes one, and pass holidays and days of rest as inputs (next section).
6. Do not edit the copy; a change belongs in the original, followed by a new sha256 and a new copy.

The tests file `au-time-rules-tests.l4` imports the sibling module, so it only runs beside it.
Its 1005 assertions double as worked examples; for instance:

```
#ASSERT (`the last day of a period` NSW 2 Months `begins from a specified day` (Date 29 2 2024)) EQUALS (JUST (Date 30 4 2024))
#ASSERT (`the day a person attains an age in years` SA (Date 29 2 2024) 1) EQUALS (JUST (Date 1 3 2025))
```

The tests are grouped by shared function and jurisdiction.
There are 261 groups; each group has at least three assertions, drawn from inputs that include month ends, 29 February, year ends, a Sunday and a holiday input where the function can be asked about them.
For a jurisdiction whose source module does not encode a function, the group asserts that the shared function answers NOTHING.
The exceptions to three assertions on inputs the source module answers are: NSW a period expressed in this way includes the specified day; Tas a period expressed in this way includes the specified day, where the source module takes only two of the ten ways to express a period, so each has two such assertions and two NOTHING assertions for the others.

## What the caller supplies

Holidays and days of rest are inputs, never built in.
A `Days of rest and closure` holds four lists: public holidays (each with a flag that it covers only part of the day), bank holidays, public service holidays, and days the office is closed for the whole day.
Saturday and Sunday are computed.
Only SA and NT read the part-day flag.
The sitting days of a House are a list of dates, and the day a letter would be delivered in the ordinary course of post is a date.
The date of assent, the day a proclamation is published and similar days are arguments of the functions that need them.

## The surface

Every function that is selected by a jurisdiction takes a `Jurisdiction` first; the small helpers and the functions named with a jurisdiction prefix (Vic, ACT, Tas, NSW) do not.
A function for which a jurisdiction may have no answer returns a `MAYBE`, with `NOTHING` as the missing answer.
The types are `Jurisdiction`, `Unit of a period` (Days, Weeks, Months, Years, `Calendar years`), `How a period is expressed` (ten constructors), `A public holiday`, `Days of rest and closure`, `What is to be done` (filing or registering a document; something at an office of a public entity; anything else; anything else, by or in relation to an authorised deposit-taking institution), `Point in a day` and `Moment in a day`.
The functions, by section, are below; the parameters are shown as in the module.

### Small helpers

- `is a whole number of at least 1` takes n (NUMBER) and gives BOOLEAN.
- `is a public holiday, whether or not it covers only part of the day` takes d (DATE), holidays (LIST OF `A public holiday`) and gives BOOLEAN.
- `is a public holiday that covers the whole day` takes d (DATE), holidays (LIST OF `A public holiday`) and gives BOOLEAN.
- `is a Sunday` takes d (DATE) and gives BOOLEAN.

### Which expression a period is tied to a day by (Cth s 36(1) table; NSW s 36(1); Vic s 44(1) and (2); Qld s 38(1); WA s 61(1); SA s 44(1) table; Tas s 29(1); ACT s 151 table 151; NT s 28(1) and (1A))

- `a period expressed in this way includes the specified day` takes j (Jurisdiction), how (`How a period is expressed`) and gives MAYBE BOOLEAN.
- `the specified day names the start of a period expressed in this way` takes j (Jurisdiction), how (`How a period is expressed`) and gives BOOLEAN.
- `the first day counted in a period` takes j (Jurisdiction), how (`How a period is expressed`), anchor (DATE) and gives MAYBE DATE.
- `the last day of a period that ends by reference to a day` takes j (Jurisdiction), how (`How a period is expressed`), anchor (DATE) and gives MAYBE DATE.
- `the first day of a period of days that ends by reference to a day` takes j (Jurisdiction), n (NUMBER), how (`How a period is expressed`), anchor (DATE) and gives MAYBE DATE.

### Calendar months and years: the ways the source modules count them (Cth s 2G; NSW Sch 4 "calendar month"; Vic s 44(6); Qld Sch 1 "calendar month"; WA s 62; SA s 4 "month" and "year"; Tas s 46; ACT dictionary "month"; NT s 17)

- `the last day of months counted straight to the corresponding day` takes n (NUMBER), s (DATE) and gives DATE.
- `the last day of months counted with add months` takes firstDay (DATE), numberOfMonths (NUMBER) and gives DATE.
- `the last day of one calendar month starting on` takes s (DATE) and gives DATE.
- `the last day of months counted one calendar month at a time` takes n (NUMBER), s (DATE) and gives DATE.
- `the last day of months where Vic's two readings agree` takes anchor (DATE), n (NUMBER) and gives MAYBE DATE.
- `the same-numbered day in the month reached` takes start (DATE), months (NUMBER) and gives MAYBE DATE.
- `the last day of one year beginning on` takes firstDay (DATE) and gives DATE.
- `the last day of years counted one year at a time` takes firstDay (DATE), numberOfYears (NUMBER) and gives DATE.

### The last day of a period of days, months or years (Cth s 36(1) with s 2G; NSW s 36(1) and Sch 4; Vic s 44(1); Qld s 38(1); WA ss 61, 62; SA s 44(1); Tas s 29(1) and s 46; ACT s 151 and dictionary; NT s 28(1))

- `the last day of a period` takes j (Jurisdiction), n (NUMBER), unit (`Unit of a period`), how (`How a period is expressed`), anchor (DATE) and gives MAYBE DATE.

### Days of rest, and the day a thing may be done when its last day is one (Cth s 36(2) and (3); NSW s 36(2); Vic s 44(3) and (4); Qld s 38(2), (3) and (5); WA s 61(1)(e) and (2); SA s 44(2); Tas s 29(3) to (6); ACT s 151A; NT s 28(2))

- `the jurisdiction states a rule for this kind of thing` takes j (Jurisdiction), kind (`What is to be done`) and gives BOOLEAN.
- `is a day of rest` takes j (Jurisdiction), kind (`What is to be done`), d (DATE), rest (`Days of rest and closure`) and gives BOOLEAN.
- `the first day from a day that is not a day of rest` takes j (Jurisdiction), kind (`What is to be done`), d (DATE), rest (`Days of rest and closure`) and gives DATE.
- `Vic: the first day from a day that is not a holiday, within a limit on the search` takes d (DATE), fuel (NUMBER), rest (`Days of rest and closure`) and gives MAYBE DATE.
- `ACT: the first working day from a day, within a limit on the search` takes kind (`What is to be done`), d (DATE), rest (`Days of rest and closure`), left (NUMBER) and gives MAYBE DATE.
- `the latest day on which a thing may be done` takes j (Jurisdiction), kind (`What is to be done`), lastDay (DATE), rest (`Days of rest and closure`) and gives MAYBE DATE.
- `the day a time calculated backwards is taken to fall on` takes j (Jurisdiction), kind (`What is to be done`), d (DATE), rest (`Days of rest and closure`) and gives MAYBE DATE.
- `the first earlier day that is not a day of rest` takes j (Jurisdiction), kind (`What is to be done`), d (DATE), rest (`Days of rest and closure`) and gives DATE.
- `Tas: the day reached counting days forwards, days of rest not reckoned` takes start (DATE), remaining (NUMBER), rest (`Days of rest and closure`) and gives DATE.
- `the latest day on which a thing may be done within a period` takes j (Jurisdiction), kind (`What is to be done`), n (NUMBER), unit (`Unit of a period`), how (`How a period is expressed`), anchor (DATE), rest (`Days of rest and closure`) and gives MAYBE DATE.

### Business days (Cth s 2B; NSW Sch 4 and s 76(2); Qld Sch 1; SA s 4; ACT dictionary; NT s 17)

- `is a business day` takes j (Jurisdiction), d (DATE), rest (`Days of rest and closure`) and gives MAYBE BOOLEAN.

### When an enactment begins and stops operating, and at what moment of the day (Cth ss 3 and 3A; NSW ss 23, 24, 71 and Sch 4; Vic ss 11, 12, 24, 25 and 44(6)(a); Qld ss 15A, 15B, 18 and Sch 1; WA ss 20, 21; SA ss 27, 28, 30; Tas ss 9, 14, 16; ACT ss 73, 74, 85; NT ss 5, 6A)

- `the moment an enactment comes into operation on a day` takes j (Jurisdiction), d (DATE) and gives MAYBE `Moment in a day`.
- `the moment an enactment stops operating on its expiry day` takes j (Jurisdiction), d (DATE) and gives MAYBE `Moment in a day`.
- `midnight in relation to a day` takes j (Jurisdiction), d (DATE) and gives MAYBE `Moment in a day`.

### The day an Act commences when it says nothing about its commencement (Cth s 3A; NSW s 23(1)(a); Qld s 15A; WA s 20; SA s 27(1); ACT s 73(1); NT s 5(4))

- `the day an Act that says nothing about its commencement commences` takes j (Jurisdiction), assent (DATE) and gives MAYBE DATE.

### A day fixed for commencement that is not later than the day the proclamation or notice is published (NSW s 23(5); Vic s 11(2A); Qld s 15D; ACT s 77(3) and (4))

- `the day an Act commences when the day fixed is not later than the day of publication` takes j (Jurisdiction), fixedDay (DATE), publishedDay (DATE), `the proclamation was made on or before the fixed day` (BOOLEAN), `the notice clearly indicates an earlier commencement and provides for it under authority given by an Act` (BOOLEAN) and gives MAYBE DATE.

### An Act to commence on a day to be fixed that has not commenced by a time limit (Vic s 10A(3) and (4); Qld s 15DA; SA s 27(6) and (7); ACT s 79(1))

- `the day an Act to commence on a day to be fixed commences automatically` takes j (Jurisdiction), assentOrNotification (DATE), `the Act says that the automatic rule does not apply` (BOOLEAN), `the months a regulation has extended the period to, or 0 if none` (NUMBER) and gives MAYBE DATE.

### When an amending Act is repealed automatically (NSW s 30C(2) and (3); Qld s 22C(1); ACT s 89(1))

- `the day an amending Act is repealed automatically` takes j (Jurisdiction), assent (DATE), `the day on which the last provision commenced` (DATE) and gives MAYBE DATE.

### The day a person attains an age, and a person's age on a day (Cth s 37A; NSW s 37; Vic s 55(2); Qld s 38A; SA s 49; ACT s 149; NT s 30)

- `the day a person attains an age in years` takes j (Jurisdiction), born (DATE), years (NUMBER) and gives MAYBE DATE.
- `the age in years of a person on a day` takes j (Jurisdiction), born (DATE), day (DATE) and gives MAYBE NUMBER.

### Service by post (Cth s 29; NSW s 76; Vic s 49; Qld s 39A; WA s 75(1); SA s 51(5); Tas s 30; ACT s 250; NT s 25)

- `NSW: the n-th working day after a day` takes d (DATE), n (NUMBER), rest (`Days of rest and closure`) and gives DATE.
- `the day service by post is taken to be effected` takes j (Jurisdiction), `the document was properly addressed, prepaid and posted as a letter` (BOOLEAN), posted (DATE), `the day it would be delivered in the ordinary course of post` (DATE), `the day service in fact took place, if the contrary is proved` (MAYBE DATE), rest (`Days of rest and closure`) and gives MAYBE DATE.

### Sitting days of a House (Cth s 2M; NSW s 18; Tas s 44; NT s 17 "sitting day")

- `the n-th sitting day after a day` takes j (Jurisdiction), n (NUMBER), d (DATE), sittings (LIST OF DATE) and gives MAYBE DATE.

### Financial years and calendar years (Cth s 2B; NSW Sch 4; Vic s 44(6); Qld Sch 1; WA s 5; SA s 4; Tas s 45(1); ACT dictionary and s 89(2); NT s 17)

- `the first day of the financial year ending in` takes j (Jurisdiction), yearOfEnding (NUMBER) and gives MAYBE DATE.
- `the last day of the financial year ending in` takes j (Jurisdiction), yearOfEnding (NUMBER) and gives MAYBE DATE.
- `the first day of the calendar year` takes j (Jurisdiction), year (NUMBER) and gives MAYBE DATE.
- `the last day of the calendar year` takes j (Jurisdiction), year (NUMBER) and gives MAYBE DATE.
- `the year in which the financial year containing a day ends` takes j (Jurisdiction), d (DATE) and gives MAYBE NUMBER.

### Clear days and days between events (Qld s 38(1); Tas s 29(2); WA s 61(1)(f) and (g); ACT s 151 table 151 item 5)

- `the earliest day on which the purpose can be fulfilled after clear days` takes j (Jurisdiction), n (NUMBER), given (DATE) and gives MAYBE DATE.
- `the latest day for the earlier event so that clear days lie between` takes j (Jurisdiction), n (NUMBER), laterDay (DATE) and gives MAYBE DATE.
- `the number of days counted between two events` takes j (Jurisdiction), `clear days, or at least a number of days` (BOOLEAN), firstEvent (DATE), secondEvent (DATE) and gives MAYBE NUMBER.

## Rule families by jurisdiction

The table names, for each rule family of the differential, whether the jurisdiction's source module encodes it.
`yes` means the shared function reproduces the source module for that jurisdiction, apart from the cases listed under what is not reproduced (the source functions are named in the next section); `not encoded` means the source module has no rule for the family and the shared function answers `NOTHING`; `not carried` means the source module has a rule that the shared surface does not carry (see the section on what is not reproduced).

| Family | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| F01 does a period expressed this way include the specified day | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F02 the first day counted in a period | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F03 the last day of a period of days, weeks, months, years or calendar years (F03a to F03d) | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F04 the last day of a period that ends by reference to a day | yes | not encoded | yes | not encoded | yes | yes | not encoded | not encoded | not encoded |
| F05 the first day of a period of days that ends by reference to a day | not encoded | not encoded | not encoded | yes | yes | not encoded | yes | yes | yes |
| F06 the latest day on which a thing may be done | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F07 the day a time calculated backwards is taken to fall on | not encoded | not encoded | not encoded | yes | not encoded | not encoded | yes | not encoded | not encoded |
| F08 the latest day on which a thing may be done within a period | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F09 is a day of rest | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| F10 is a business day | yes | yes | not encoded | yes | not encoded | yes | not encoded | yes | yes |
| G01a the moment an enactment comes into operation | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| G01b the moment an enactment stops operating | not encoded | yes | yes | yes | not encoded | yes | yes | yes | not encoded |
| G01c midnight in relation to a day | not encoded | yes | yes | yes | not encoded | not encoded | not encoded | yes | not encoded |
| G02 the day an Act that says nothing about its commencement commences | yes | yes | not carried | yes | yes | yes | not carried | yes | yes |
| G03 the day an Act commences when the day fixed is not later than the day of publication | not encoded | yes | yes | yes | not encoded | not encoded | not encoded | yes | not encoded |
| G04 the day an Act to commence on a day to be fixed commences automatically | not encoded | not encoded | yes | yes | not encoded | yes | not encoded | yes | not encoded |
| G05 the day an amending Act is repealed automatically | not encoded | yes | not encoded | yes | not encoded | not encoded | not encoded | yes | not encoded |
| G06a the day a person attains an age in years | yes | yes | yes | not encoded | not encoded | yes | not encoded | yes | yes |
| G06b the age in years of a person on a day | not encoded | not encoded | not encoded | yes | not encoded | not encoded | not encoded | yes | not encoded |
| G07 the day service by post is taken to be effected | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| G08 the n-th sitting day after a day | yes | yes | not encoded | not encoded | not encoded | not encoded | yes | not encoded | yes |
| G09a the first day of the financial year ending in | yes | not encoded | yes | not encoded | yes | not encoded | yes | not encoded | yes |
| G09b the last day of the financial year ending in | yes | not encoded | yes | yes | yes | yes | yes | yes | not encoded |
| G09c the first day of the calendar year | yes | not encoded | yes | yes | not encoded | not encoded | not encoded | not encoded | not encoded |
| G09d the last day of the calendar year | yes | yes | yes | yes | not encoded | yes | not encoded | yes | yes |
| G09e the year in which the financial year containing a day ends | yes | not encoded | not encoded | not encoded | yes | not encoded | yes | not encoded | not encoded |
| G10a the earliest day on which the purpose can be fulfilled after clear days | not encoded | not encoded | not encoded | yes | not encoded | not encoded | yes | not encoded | not encoded |
| G10b the latest day for the earlier event so that clear days lie between | not encoded | not encoded | not encoded | not encoded | not encoded | not encoded | yes | yes | not encoded |
| G10c the number of days counted between two events | not encoded | not encoded | not encoded | not encoded | yes | not encoded | not encoded | yes | not encoded |

F03 covers the last day of a period of days, weeks, months, years or calendar years; the next table splits it by unit.
The Vic age function answers for eighteen years only, and any other age is NOTHING there.
F11 is the limit on the search for a day that is not a day of rest, which applies to Vic and ACT only (400 days); it is a property of F06, so it has no row of its own.

## The source function behind each cell

### F01 does a period expressed this way include the specified day

- Cth: au-interpretation-time `a period expressed in this way includes the specified day` (Cth s 36(1) items 1 to 7).
- NSW: nsw-interpretation-time `s 36(1) the first day counted in a period dating from a given day` (the given day is left out).
- Vic: vic-interpretation-time `s44(1)-(2) the day a period is expressed to begin on or end on is counted in the period`.
- Qld: qld-interpretation-time `a day is counted in a period beginning on a given day (s 38(1))` (the given day is left out).
- WA: wa-interpretation-time `the first day of a period` (s 61(1)(a), (b)) with `the end of a period expressed to end on` (s 61(1)(d)) and `the time within a time before a day` (s 61(1)(c)).
- SA: sa-interpretation-time `s 44(1): the first day counted in a period` and `s 44(1) items 4, 5 and 7`, with item 1.
- Tas: tas-interpretation-time `s 29(1): a day is counted in a period of days reckoned forwards from` (the given day is left out).
- ACT: act-interpretation-time `s 151 (2), table 151: the period includes the stated day`.
- NT: nt-interpretation-time `s 28(1), (1A): the given day, act or event is counted in the period`.

### F02 the first day counted in a period

The first day counted is the given day or the day after it, according to the F01 function of the same jurisdiction; the source functions are those of F01.

### F03 the last day of a period of days, weeks, months, years or calendar years (F03a to F03d)

- Cth: au-interpretation-time `the last day of a counted period of` (s 36(1) with s 2G); years answer NOTHING there.
- NSW: nsw-interpretation-time `s 36 the last day of a period of n units dating from a given day`; a year answers NOTHING, a calendar year only from 1 January.
- Vic: vic-interpretation-time `s44 last day counted forward from a day` with `s44 last day, start left out`.
- Qld: qld-interpretation-time `the last day of a period beginning on a given day (s 38(1))`.
- WA: wa-interpretation-time `reckon a period` (the last day by the calendar).
- SA: sa-interpretation-time `s 44(1): the last day of a period`.
- Tas: tas-interpretation-time `s 29(1): the last day of a period of days reckoned forwards from`, `s 29(1) and s 46: the last day of a period of calendar months reckoned forwards from`; years and weeks answer NOTHING there.
- ACT: act-interpretation-time `s 151: the last day of a period of days, months or years that begins on or from a stated day`.
- NT: nt-interpretation-time `s 28(1): the last day of a period dating from`.

### F04 the last day of a period that ends by reference to a day

- Cth: au-interpretation-time `the last day of the period`.
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: vic-interpretation-time `s44(2) last day of a period expressed to end on or be reckoned to a day`.
- Qld: no such rule in qld-interpretation-time (answers NOTHING).
- WA: wa-interpretation-time `the end of a period expressed to end on` (the last day by the calendar).
- SA: sa-interpretation-time `s 44(1) items 4, 5 and 7: the last day of a period that ends by reference to a specified day`.
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: no such rule in act-interpretation-time (answers NOTHING).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### F05 the first day of a period of days that ends by reference to a day

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: qld-interpretation-time `the earliest day of a period of days calculated backwards from a given day (s 38(1) and (3))`, read for `ends before a specified day`.
- WA: wa-interpretation-time `the time within a time before a day` (s 61(1)(c)).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: tas-interpretation-time `s 29(1): the first day of a period of days reckoned backwards from`, read for `ends before a specified day`.
- ACT: act-interpretation-time `s 151: the first day of a period of days that ends at, by, on or with, or before, a stated day`.
- NT: nt-interpretation-time `s 28(1A): the first day of a period ending on`.

### F06 the latest day on which a thing may be done

- Cth: au-interpretation-time `the last day on which the thing may be done` (with an Act that requires or allows the thing taken as true).
- NSW: nsw-interpretation-time `s 36(2) the latest day on which the thing may be done when the period ends on a day`.
- Vic: vic-interpretation-time `s44(3) day to which a time limited for doing an act or thing extends` (with the time limited for doing an act taken as true).
- Qld: qld-interpretation-time `the day a time or last day calculated forwards is taken to fall on (s 38(2))`.
- WA: wa-interpretation-time `the next day that is not an excluded day, counting the day itself`.
- SA: sa-interpretation-time `s 44(2): the last day on which a thing may be done`.
- Tas: tas-interpretation-time `s 29(3)(a): the last day on which an act is in due time, a time reckoned forwards ending on`.
- ACT: act-interpretation-time `s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day`.
- NT: nt-interpretation-time `s 28(2): the last day on which the thing may be done, for a period whose last day is`.

### F07 the day a time calculated backwards is taken to fall on

- Cth: not encoded in au-interpretation-time.
- NSW: not encoded in nsw-interpretation-time.
- Vic: not encoded in vic-interpretation-time.
- Qld: qld-interpretation-time `the day a time or earliest day calculated backwards is taken to fall on (s 38(3))`.
- WA: not encoded in wa-interpretation-time.
- SA: not encoded in sa-interpretation-time.
- Tas: tas-interpretation-time `s 29(3)(b): the day on or before which an act is in due time, a time reckoned backwards ending on`.
- ACT: not encoded in act-interpretation-time.
- NT: not encoded in nt-interpretation-time.

### F08 the latest day on which a thing may be done within a period

This function composes the last day of a period (F03) with the rule for a last day that is a day of rest (F06) of the same jurisdiction, so its source functions are those two.
Tas applies s 29(6) instead when the period is 1 to 6 days.

- Cth: F03 the last day of a counted period of, then F06 the last day on which the thing may be done.
- NSW: F03 s 36 the last day of a period of n units dating from a given day, then F06 s 36(2) the latest day on which the thing may be done when the period ends on a day.
- Vic: F03 s44 last day counted forward from a day ; s44 last day, start left out, then F06 s44(3) day to which a time limited for doing an act or thing extends.
- Qld: F03 the last day of a period beginning on a given day (s 38(1)), then F06 the day a time or last day calculated forwards is taken to fall on (s 38(2)).
- WA: F03 reckon a period, then F06 the next day that is not an excluded day, counting the day itself.
- SA: F03 s 44(1): the last day of a period, then F06 s 44(2): the last day on which a thing may be done.
- Tas: F03 s 29(1): the last day of a period of days reckoned forwards from ; s 29(1) and s 46: the last day of a period of calendar months reckoned forwards from, then F06 s 29(3)(a): the last day on which an act is in due time, a time reckoned forwards ending on; for 1 to 6 days, s 29: the last day for doing an act within a number of days reckoned forwards from.
- ACT: F03 s 151: the last day of a period of days, months or years that begins on or from a stated day, then F06 s 151A (2): the day on which the thing must or may be done, where the particular day or the last day of the period is that day.
- NT: F03 s 28(1): the last day of a period dating from, then F06 s 28(2): the last day on which the thing may be done, for a period whose last day is.

### F09 is a day of rest

- Cth: au-interpretation-time `is a Saturday, a Sunday or a holiday` (public holidays and days the office is closed for the whole day).
- NSW: nsw-interpretation-time `s 36(2) the day is a Saturday, a Sunday, or a public holiday or bank holiday in the place`.
- Vic: vic-interpretation-time `s44(4) a day is a holiday`.
- Qld: qld-interpretation-time `is an excluded day (s 38(5))`: for filing or registering, only a day the office is closed; otherwise a day that is not a business day.
- WA: wa-interpretation-time `is an excluded day` (public service holidays, bank holidays and public holidays).
- SA: sa-interpretation-time `s 4: is a business day` negated: Saturday, Sunday or a public holiday that covers the whole day.
- Tas: tas-interpretation-time `s 29(3): a day is an excluded day`: Sunday or a listed holiday; Saturday is not one.
- ACT: act-interpretation-time `s 151A (4): the day is a working day for doing the thing` negated.
- NT: nt-interpretation-time `s 28(2): the day is a Saturday, a Sunday or a public holiday`.

### F10 is a business day

- Cth: au-interpretation-time `is a business day` (not a Saturday, a Sunday or a public holiday in the place concerned; days an office is closed are not read).
- NSW: nsw-interpretation-time `Schedule 4 the day is a business day` and `s 76(2) the day is a working day` (public and bank holidays).
- Vic: no definition of a business day in vic-interpretation-time (answers NOTHING).
- Qld: qld-interpretation-time `is a business day (Schedule 1)` (public, special and bank holidays).
- WA: no definition of a business day in wa-interpretation-time (answers NOTHING).
- SA: sa-interpretation-time `s 4: is a business day` (a part-day public holiday does not count).
- Tas: no definition of a business day in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `dictionary, business day: the day is a business day` (public and bank holidays).
- NT: nt-interpretation-time `s 17 "business day": the day is a business day` (a part-day public holiday does not count).

### G01a the moment an enactment comes into operation

- Cth: au-interpretation-time `the moment the enactment comes into operation` (s 3).
- NSW: nsw-interpretation-time `s 24 the moment an Act or statutory rule commences on a particular day` (an Act or a statutory rule; another instrument is NOTHING there and is not reproduced here).
- Vic: vic-interpretation-time `s11 moment an Act or provision comes into operation on a fixed day` (s 11(1)) and `s24 moment a subordinate instrument that is not a statutory rule comes into operation`.
- Qld: qld-interpretation-time `the moment a provision commences on a day (s 15B)`.
- WA: wa-interpretation-time `the moment a written law comes into operation` (s 21).
- SA: sa-interpretation-time `s 28: the moment an Act or provision comes into operation on a particular day`.
- Tas: tas-interpretation-time `s 9(5): the moment at which an Act or instrument expressed to commence on a day takes effect`.
- ACT: act-interpretation-time `s 74 (1), (2): the beginning of a day` (s 74: unless a different time is provided).
- NT: nt-interpretation-time `s 6A: the moment at which an Act or a provision commences` (unless a time of day is provided in the Act).

### G01b the moment an enactment stops operating

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: nsw-interpretation-time `s 71 the moment an Act or instrument expressed to expire or remain in force until a day stops operating`.
- Vic: vic-interpretation-time `s12 moment until which a temporary Act or provision continues in operation`.
- Qld: qld-interpretation-time `the last moment an Act or provision has effect (s 18)`.
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: sa-interpretation-time `s 30: the moment up to which an expiring provision continues to have effect`.
- Tas: tas-interpretation-time `s 14(2): the last moment of operation of an enactment expressed to expire or remain in force until a specified day`.
- ACT: act-interpretation-time `s 85: when the repeal of a law takes effect`, for a law not remade on that day (the repeal takes effect at midnight on the day).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G01c midnight in relation to a day

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: nsw-interpretation-time `Schedule 4 midnight in relation to a particular day`.
- Vic: vic-interpretation-time `s44(6)(a) midnight in relation to a day is the point at which that day ends`.
- Qld: qld-interpretation-time `midnight of a day, the point of time at which the day ends (Schedule 1)`.
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 74 and dictionary, midnight` (midnight at the end of the day).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G02 the day an Act that says nothing about its commencement commences

- Cth: au-interpretation-time `the day the enactment commences` (s 3A(2): the 28th day after the day of Royal Assent; an Act to alter the Constitution is not reproduced here).
- NSW: nsw-interpretation-time `s 23(1)(a) the day an Act commences when nothing else provides` (the day occurring 28 days after assent).
- Vic: s 10A names a day to be proclaimed or the first anniversary; see the automatic-commencement section below; the answer here is NOTHING.
- Qld: qld-interpretation-time `the day an Act commences on the date of assent (s 15A)` (the Act does not otherwise expressly provide).
- WA: wa-interpretation-time `the day an Act comes into operation` (s 20: assent before 1 July 1984, the day of assent; otherwise the 28th day after).
- SA: sa-interpretation-time `s 27(1): the day an Act with no commencement provision comes into operation`.
- Tas: tas-interpretation-time s 9(2) and (3) depend on the day section 8 of the 1981 amending Act commenced, which the module takes as an input and this surface does not; the answer here is NOTHING.
- ACT: act-interpretation-time `s 73 (1) and s 74 (1): when an Act commences` (the day after the notification day; the input is read as the notification day).
- NT: nt-interpretation-time `s 5: the day on which an Act or a provision commences` (the day after the day assent is declared).

### G03 the day an Act commences when the day fixed is not later than the day of publication

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: nsw-interpretation-time `s 23(1) and (5) the day an Act commences` (a day fixed by proclamation, published later: the later of the two).
- Vic: vic-interpretation-time `s11 commencement once the proclamation is published` (the proclamation made on or before the fixed day; otherwise NOTHING).
- Qld: qld-interpretation-time `the day an Act commences when a day is fixed by proclamation (s 15D)` (the later of the two).
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 77 (3), (4): when a law commences under a commencement notice` (the day after the notification day, unless the notice clearly indicates an earlier commencement under authority given by an Act).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G04 the day an Act to commence on a day to be fixed commences automatically

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: vic-interpretation-time `s10A first anniversary of the passing of an Act` (NOTHING where the year has no same-numbered day).
- Qld: qld-interpretation-time `the day a postponed law automatically commences (s 15DA)`; the two further inputs are the Act's own statement that s 15DA does not apply and the months a regulation has extended the period to (0 if none).
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: sa-interpretation-time `s 27(6) and (7): the day an Act or provision to be brought into operation by proclamation comes into operation`, with the provision covered by s 27(6), no proclamation made, and the Act's own statement that s 27(6) does not apply.
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 79 (1): when a postponed law automatically commences`: the first day after 6 months beginning on the notification day (the input is read as the notification day).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G05 the day an amending Act is repealed automatically

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: nsw-interpretation-time `s 30C(2) and (3) the day an amending Act is repealed` (the day after the last commencement, or the day after assent if the last commencement is before assent).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: qld-interpretation-time `the moment an amending Act is automatically repealed (s 22C(1))` (an amending Act enacted after 30 June 1994; the module's own flag that the Act is an amending Act is taken as true); read at the day it falls on.
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 89 (1): the day an amending law is automatically repealed` (all provisions commenced; the alternative limb of paragraph (b) is not read).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G06a the day a person attains an age in years

- Cth: au-interpretation-time `the moment a person attains the age` (s 37A: NOTHING where that year has no anniversary day; the day of the moment is returned).
- NSW: nsw-interpretation-time `s 37 the moment a person attains an age in years` (the day of the moment is returned).
- Vic: vic-interpretation-time `s55(2) day on which a person born on a day reaches eighteen years, taken as the eighteenth anniversary`; the module encodes eighteen years only, so any other age is NOTHING.
- Qld: qld-interpretation-time has no day on which an age is attained; it computes an age on a day (`the age in years of a person on a day`) (answers NOTHING).
- WA: no age rule in wa-interpretation-time (answers NOTHING).
- SA: sa-interpretation-time `s 49: the moment a person attains an age in years` (1 March in a year without 29 February for a person born on 29 February; the day of the moment is returned).
- Tas: no age rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 149: the day a person attains an age in years`.
- NT: nt-interpretation-time `s 30(1): the day on which a person attains the age` (28 February in a year without 29 February for a person born on 29 February).

### G06b the age in years of a person on a day

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: qld-interpretation-time `the age in years of a person on a day (s 38A)` (NOTHING on 28 February of a year without 29 February for a person born on 29 February).
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 149: the age in years of a person on a day`.
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G07 the day service by post is taken to be effected

- Cth: au-interpretation-time `the day service by post is taken to be effected` (s 29(1)): the contrary day if proved, otherwise the ordinary-course day; NOTHING if not properly done.
- NSW: nsw-interpretation-time `s 76(1)(b) the day service by post in Australia or an external Territory is taken to be effected` (the seventh working day after posting; the ordinary-course day is not read).
- Vic: vic-interpretation-time `s49 day on which service by post is deemed effected` (the ordinary-course day; NOTHING where the contrary is proved; the flag is not read).
- Qld: qld-interpretation-time `the time service by post is taken to have been effected (s 39A(1)(b))` (the ordinary-course day; NOTHING where the contrary is proved; the flag is not read).
- WA: wa-interpretation-time `the day service by post is deemed effected` (s 75(1)): the contrary day if proved, otherwise the ordinary-course day; NOTHING if not properly done.
- SA: sa-interpretation-time `s 51(5): the moment service by post is taken to be effected` (the contrary day if proved, otherwise the ordinary-course day; the flag is not read).
- Tas: tas-interpretation-time `s 30(1): the day service by post is deemed to have been effected` (the ordinary-course day; NOTHING if not properly done or the contrary is proved).
- ACT: act-interpretation-time `s 250: the day a document is taken to be served`, by prepaid post (the ordinary-course day).
- NT: nt-interpretation-time `s 25(2), (3), (4): the day on which a document is taken to be served`, by prepaid post (the ordinary-course day).

### G08 the n-th sitting day after a day

- Cth: au-interpretation-time `the sitting day that is the n-th after` (s 2M with s 36(1) item 6).
- NSW: nsw-interpretation-time `s 18 the nth sitting day of a House after a day`.
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: no such rule in qld-interpretation-time (answers NOTHING).
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: tas-interpretation-time `s 44: the sitting day of a House that is the number given after a day`.
- ACT: no such rule in act-interpretation-time (answers NOTHING).
- NT: nt-interpretation-time `s 17 "sitting day": the nth sitting day after`.

### G09a the first day of the financial year ending in

- Cth: au-interpretation-time `the financial year containing` (a financial year runs from 1 July to 30 June; the first day of the span is returned).
- NSW: no financial-year rule in nsw-interpretation-time (answers NOTHING).
- Vic: vic-interpretation-time `s44(6)(d) first day of the financial year ending on 30 June of a year`.
- Qld: qld-interpretation-time has `the last day of the financial year beginning on 1 July (Schedule 1)` only, with no first-day function (answers NOTHING).
- WA: wa-interpretation-time `the first day of the financial year ending in`.
- SA: sa-interpretation-time has `s 4: the last day of the financial year starting on 1 July` only, with no first-day function (answers NOTHING).
- Tas: tas-interpretation-time `s 45(1): the first day of the financial year ending in the year`.
- ACT: act-interpretation-time has `s 89 (2): the day an appropriation Act is automatically repealed` only, with no first-day function (answers NOTHING).
- NT: nt-interpretation-time `s 17 "financial year": the first day of the financial year ending on 30 June of`.

### G09b the last day of the financial year ending in

- Cth: au-interpretation-time `the financial year containing` (the last day of the span is returned).
- NSW: no financial-year rule in nsw-interpretation-time (answers NOTHING).
- Vic: vic-interpretation-time `s44(6)(d) midnight at which the financial year ending in a calendar year ends` (the day of that midnight).
- Qld: qld-interpretation-time `the last day of the financial year beginning on 1 July (Schedule 1)` (it takes the year the financial year begins in).
- WA: wa-interpretation-time `the last day of the financial year ending in`.
- SA: sa-interpretation-time `s 4: the last day of the financial year starting on 1 July` (it takes the year the financial year starts in).
- Tas: tas-interpretation-time `s 45(1): the last day of the financial year ending in the year`.
- ACT: act-interpretation-time `s 89 (2): the day an appropriation Act is automatically repealed` (it takes the year the financial year begins in).
- NT: nt-interpretation-time has `s 17 "financial year": the first day of the financial year ending on 30 June of` only, with no last-day function (answers NOTHING).

### G09c the first day of the calendar year

- Cth: au-interpretation-time `the calendar year containing` (the first day of the span is returned).
- NSW: no first-day-of-calendar-year function in nsw-interpretation-time (answers NOTHING).
- Vic: vic-interpretation-time `s44(6)(e) first day of the calendar year ending on 31 December of a year`.
- Qld: qld-interpretation-time `the first day of the calendar year (Schedule 1)`.
- WA: no calendar-year function in wa-interpretation-time (answers NOTHING).
- SA: no first-day-of-calendar-year function in sa-interpretation-time (answers NOTHING).
- Tas: no calendar-year function in tas-interpretation-time (answers NOTHING).
- ACT: no first-day-of-calendar-year function in act-interpretation-time (answers NOTHING).
- NT: no first-day-of-calendar-year function in nt-interpretation-time (answers NOTHING).

### G09d the last day of the calendar year

- Cth: au-interpretation-time `the calendar year containing` (the last day of the span is returned).
- NSW: nsw-interpretation-time `s 36(1) and Schedule 4 the last day of a period of n calendar years dating from a given day` (one calendar year dating from 31 December of the year before).
- Vic: vic-interpretation-time `s44(6)(e) midnight at which a calendar year ends` (the day of that midnight).
- Qld: qld-interpretation-time `the last day of the calendar year (Schedule 1)`.
- WA: no calendar-year function in wa-interpretation-time (answers NOTHING).
- SA: sa-interpretation-time `s 4: the last day of the calendar year`.
- Tas: no calendar-year function in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `dictionary, calendar year and year: the last day of a run of calendar years beginning at the start of a day` (one calendar year beginning on 1 January).
- NT: nt-interpretation-time `s 17 "calendar year": the last day of the calendar year of`.

### G09e the year in which the financial year containing a day ends

- Cth: au-interpretation-time `the financial year containing` (the year of its last day).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: no such rule in qld-interpretation-time (answers NOTHING).
- WA: wa-interpretation-time `the calendar year in which the financial year containing the date ends`.
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: tas-interpretation-time `s 45(1): the year in which the financial year containing a day ends`.
- ACT: no such rule in act-interpretation-time (answers NOTHING).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G10a the earliest day on which the purpose can be fulfilled after clear days

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: qld-interpretation-time `the earliest day on which the purpose can be fulfilled after clear days (s 38(1)(a))`.
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: tas-interpretation-time `s 29(2): the earliest day on which the purpose may be fulfilled after a number of clear days from`.
- ACT: no such rule in act-interpretation-time (answers NOTHING).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G10b the latest day for the earlier event so that clear days lie between

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: no such rule in qld-interpretation-time (answers NOTHING).
- WA: no such rule in wa-interpretation-time (answers NOTHING).
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: tas-interpretation-time `s 29(2): the latest day on which the purpose may be fulfilled before a number of clear days from`.
- ACT: act-interpretation-time `s 151 (2), table 151 item 5: the latest day for the earlier event, so that the given number of days lie between the 2 events`.
- NT: no such rule in nt-interpretation-time (answers NOTHING).

### G10c the number of days counted between two events

- Cth: no such rule in au-interpretation-time (answers NOTHING).
- NSW: no such rule in nsw-interpretation-time (answers NOTHING).
- Vic: no such rule in vic-interpretation-time (answers NOTHING).
- Qld: no such rule in qld-interpretation-time (answers NOTHING).
- WA: wa-interpretation-time `the number of days counted between two events`: clear days, or at least a number of days, exclude both event days; any other count excludes the first event's day and includes the second's.
- SA: no such rule in sa-interpretation-time (answers NOTHING).
- Tas: no such rule in tas-interpretation-time (answers NOTHING).
- ACT: act-interpretation-time `s 151 (2), table 151 item 5: the number of days between 2 events` (both event days excluded).
- NT: no such rule in nt-interpretation-time (answers NOTHING).

## Units of a period, by jurisdiction

This table is read from the body of `the last day of a period`.

| Unit | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| Days | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| Weeks | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING |
| Months | yes: straight to the corresponding day | yes: one calendar month at a time | yes: two readings, answered where they agree | yes: one calendar month at a time | yes: with add months | yes: straight to the corresponding day | yes: the same-numbered day, otherwise NOTHING | yes: one calendar month at a time | yes: one calendar month at a time |
| Years | NOTHING | NOTHING | yes: 12 months each, two readings | yes: 12 months each, one month at a time | yes: 12 months each, with add months | yes: one year at a time | NOTHING | yes from 1 January only | yes: 12 months each, one month at a time |
| Calendar years | NOTHING | yes from 1 January only | NOTHING | NOTHING | NOTHING | NOTHING | NOTHING | yes from 1 January only | NOTHING |

The count n is checked differently in each jurisdiction, as the source modules do: Cth, NSW, WA and NT require a whole number of at least 1; Qld, SA and ACT require only that n is at least 1; Vic and Tas do not check.

## The unified expression map

The ten constructors of `How a period is expressed` are the phrases the source modules use to tie a period to a day.
Each jurisdiction answers only the expressions its own module encodes.
The three tables below were produced by asking the shared module (`Y` means the module gave an answer for at least one input).
For NSW, Qld, Tas and NT, the mapping from the source function to these expressions is an assumption of this module.

### Counting forward from a day: `the first day counted in a period` and `the last day of a period` (days)

| Expression | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| `between two days` | Y |  |  |  |  |  |  |  |  |
| `begins at, on or with a specified day` | Y |  | Y | Y | Y | Y |  | Y |  |
| `begins from a specified day` | Y | Y | Y | Y | Y |  | Y | Y | Y |
| `begins after a specified day` | Y |  |  |  | Y | Y |  | Y |  |
| `begins on, from or after the happening of an act or event` |  | Y |  | Y |  | Y | Y |  | Y |
| `continues until a specified day` |  |  |  |  |  |  |  |  |  |
| `ends at, on or with a specified day` |  |  |  |  |  |  |  |  |  |
| `ends before a specified day` |  |  |  |  |  |  |  |  |  |
| `is reckoned to a specified day` |  |  |  |  |  |  |  |  |  |
| `occurs between two events` |  |  |  |  |  |  |  |  |  |

### A period that ends by reference to a day: `the last day of a period that ends by reference to a day`

| Expression | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| `between two days` | Y |  |  |  |  |  |  |  |  |
| `begins at, on or with a specified day` |  |  |  |  |  |  |  |  |  |
| `begins from a specified day` |  |  |  |  |  |  |  |  |  |
| `begins after a specified day` |  |  |  |  |  |  |  |  |  |
| `begins on, from or after the happening of an act or event` |  |  |  |  |  |  |  |  |  |
| `continues until a specified day` | Y |  |  |  | Y | Y |  |  |  |
| `ends at, on or with a specified day` | Y |  | Y |  | Y | Y |  |  |  |
| `ends before a specified day` | Y |  |  |  |  | Y |  |  |  |
| `is reckoned to a specified day` |  |  | Y |  |  |  |  |  |  |
| `occurs between two events` |  |  |  |  |  |  |  |  |  |

### Counting backward from a day: `the first day of a period of days that ends by reference to a day`

| Expression | Cth | NSW | Vic | Qld | WA | SA | Tas | ACT | NT |
|---|---|---|---|---|---|---|---|---|---|
| `between two days` |  |  |  |  |  |  |  |  |  |
| `begins at, on or with a specified day` |  |  |  |  |  |  |  |  |  |
| `begins from a specified day` |  |  |  |  |  |  |  |  |  |
| `begins after a specified day` |  |  |  |  |  |  |  |  |  |
| `begins on, from or after the happening of an act or event` |  |  |  |  |  |  |  |  |  |
| `continues until a specified day` |  |  |  |  |  |  |  | Y |  |
| `ends at, on or with a specified day` |  |  |  |  |  |  |  | Y | Y |
| `ends before a specified day` |  |  |  | Y | Y |  | Y | Y |  |
| `is reckoned to a specified day` |  |  |  |  |  |  |  |  |  |
| `occurs between two events` |  |  |  |  |  |  |  |  |  |

## Rest days and the day a thing may be done

Seven jurisdictions step forward to the first day that is not a day of rest; Vic and ACT do so with a limit of 400 days on the search, which the module reproduces.
Tas applies s 29(6) instead when the period is 1 to 6 days.
Qld and ACT read the kind of thing to be done (`What is to be done`); the other jurisdictions ignore it.
Qld, for filing or registering a document, treats only a day the office is closed as a day of rest; for anything else it uses the business-day rule.
Tas treats Sunday and a listed holiday as days of rest, and Saturday is not one.

## What the module does not reproduce

The first list was found by reading the source modules against the shared module.

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

The second list is mechanical: every function defined in a source module whose name does not appear anywhere in the shared module.
The test is a text match, so a function carried under different wording is listed, and a name that appears only in a comment is not.

| Jurisdiction | Functions in the source module | Not named in the shared module |
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

## Forks and assumptions

Each item below is assumed, not ruled, and can be reverted by deleting the files in this folder.

- The shared surface, one function per rule family with the `Jurisdiction` first, is a design choice of this module and not a ruling.
- The ten constructors of `How a period is expressed` are the union of the phrases the source modules use; the mapping of NSW, Qld, Tas and NT functions to them is an assumption, shown in the expression map.
- A backward period is read as `ends before a specified day` for Qld and Tas, and the map shows the other expressions each jurisdiction answers.
- The month-counting variants are kept as separate ports: straight to the corresponding day (Cth, SA), `add months` (WA), one calendar month at a time (NSW, Qld, ACT, NT), two readings answered where they agree (Vic), and the same-numbered day or NOTHING (Tas).
- Cth and SA use one body for months; WA has its own, which uses `add months` as its source module does.
- The part-day flag on a public holiday is read by SA and NT only; the other jurisdictions ignore it.
- Sitting days are a list of dates, a different shape from the Cth sitting records, which pair a beginning with an adjournment.
- The year argument of a financial-year function is the year in which the financial year ends; Qld, SA and ACT source functions take the year in which it begins, and the shared function converts.
- For a person born on 29 February, the anniversary in a year without 29 February is answered as each source module answers it: NOTHING (Cth, NSW, ACT), 1 March (SA), 28 February (NT).

## Binary compatibility

The module and the tests were checked with both binaries, run from a copy outside the repository, with `JL4_LIBRARY_PATH` unset.
Binary 1.6.110 (main e51181d, 2026-11-11) reported no error on `l4 check` of either file, and `l4 run` of the tests satisfied 1005 of 1005 assertions.
Binary 1.6.98 (main 7689b0d, 2026-10-19) reported no error on `l4 check` of either file, and `l4 run` of the tests satisfied 1005 of 1005 assertions.
No syntax was found that the newer binary accepts and the older rejects, so no older-compatible alternative form was needed.
The differential was run on 1.6.110 only.

## Source functions the shared module does not carry, grouped

Every function defined in a source module whose name does not appear anywhere in the shared module is listed here, once, under the first heading whose keywords match its name.
The grouping is a keyword match made for these notes; the function names are the source modules' own.
The sentence under each heading says what the shared module does carry in that area; it does not say that every name in the group is a separate rule.
The last group holds the names that no keyword matched.

### Points in time: instants, seconds, ordering, and whether a provision is in operation at a moment (28)

The shared module returns the moment an enactment begins or stops operating, as a day and a point in that day, and has no function that orders moments or tests a moment against a period.

- Cth: `the start of the day`
- NSW: `Schedule 4 the last day of the calendar month commencing at the beginning of a day`
- NSW: `the instant a day point denotes, counted in half days`
- NSW: `day point is no later than day point`
- Qld: `the number of seconds in a day`
- Qld: `the instant of a moment`
- Qld: `the first moment is the same instant as the second moment`
- Qld: `the first moment is before the second moment`
- Qld: `the last day of the calendar month starting at the beginning of a day (Schedule 1)`
- WA: `a written law is in operation at`
- SA: `s 4: seconds in a day`
- SA: `s 4: the beginning of a day`
- SA: `s 4: the end of a day`
- SA: `s 4: the position of a moment in seconds`
- SA: `ss 28 and 30: a provision is in operation at a moment`
- Tas: `the offset of a part of a day`
- Tas: `the position on the timeline of a moment`
- Tas: `s 9(5): the moment immediately before an Act or instrument expressed to commence on a day takes effect`
- Tas: `s 16(4): the moment at which an Act or instrument expressed to expire or cease to have effect on a particular day expires`
- Tas: `s 9(5) and s 14(2): an enactment commencing on a day and expiring on a day is in operation at a moment`
- Tas: `the earlier of two days`
- ACT: `s 74 and dictionary, midnight: the number of minutes from the start of the day to a time of day`
- ACT: `s 74: a single number that orders points in time`
- ACT: `s 74: the first point is earlier than the second`
- ACT: `s 74: the earliest of some points in time`
- ACT: `s 74: the latest of some points in time`
- NT: `the number of minutes from day zero of the day count to the moment`
- NT: `s 6A: the Act or provision has commenced at`

### Automatic repeal and the effect of a repeal (16)

The shared module carries the day an amending Act is repealed automatically (NSW, Qld, ACT s 89(1)) and none of the other repeal rules.

- NSW: `s 30D the moment a repeal on a day takes effect`
- Tas: `s 14(1): a repealing Act was passed after 5th August 1853`
- ACT: `s 89 (3), (4): the point in time immediately after which the provision is automatically repealed`
- ACT: `s 89 (5), (6): the latest of some days`
- ACT: `s 89 (5): the day a commencement notice is automatically repealed`
- ACT: `s 89 (6): the day an instrument making or evidencing appointments is automatically repealed`
- ACT: `s 89 (8): the day a law is automatically repealed, if the day would be earlier than its notification day`
- NT: `s 11: the repeal has the effect of reviving the previous Act or part`
- NT: `s 12(a): the thing was in force or existing at the time at which the repeal takes effect`
- NT: `s 12(a): the repeal revives the thing`
- NT: `s 12(b), (c), (d): the repeal affects the thing`
- NT: `s 12: the thing may be instituted, continued, enforced or imposed as if the repealing Act had not been made`
- NT: `s 13: the sections that apply as if the law of the State were an Act or part repealed`
- NT: `s 16: the sections that apply as though the Act or part had been repealed`
- NT: `s 14: the repealed provisions continue in force on`
- NT: `s 15: a reference to the provision repealed is taken to be a reference to the provision re-enacted`

### Appointments, offices and acting periods (9)

No shared function was written for periods that attach to an office or an appointment (Qld s 24B, Vic s 64B, Tas s 21(3)(b)).

- NSW: `s 23(2) the day appointed is no earlier than the date of assent and no later than the day occurring 28 days after`
- Vic: `s64B(1) first day of the period of a purported appointment`
- Vic: `s64B(1) last day of the period of a purported appointment`
- Vic: `s64B(1) the appointment was made during the period of a purported appointment`
- Qld: `the latest last day of the term of an acting appointment because of a vacancy (s 24B(5))`
- Qld: `the last day an appointee may continue to act at the end of a year from the day of the vacancy (s 24B(6)(c))`
- Tas: `s 21(3)(b): the last day on which the holder may continue to exercise the powers after a fixed term`
- ACT: `s 81 (6): when an appointment or instrument that declares subsection (6) applies commences`
- ACT: `s 81 (7): when an appointment or instrument made under s 81 commences`

### Sitting days and the publication of regulations (7)

The shared module carries the n-th sitting day after a day, and not `is a sitting day` (Cth) or the Tas s 47 rules about publishing and laying regulations.

- Cth: `is a sitting day`
- Tas: `s 47(3)(a) and (b): the last day for publication or notification of regulations in the Gazette`
- Tas: `s 47(3)(a) and (b): the regulations were published or notified in the Gazette within 21 days after the day they were made`
- Tas: `s 47(3)(c): the last of the first 10 sitting days of the House after publication or notification`
- Tas: `s 47(4): the last of the first 15 sitting days of the House after a regulation is laid before it`
- Tas: `s 47(7): the last day of the 12 months after the disallowance of a regulation`
- Tas: `s 47(7): the 30th sitting day of the House after the regulation is laid upon the table`

### Service of documents (3)

The shared module carries one function for service by post per jurisdiction; these are further functions of the same or neighbouring sections.

- Vic: `s49 service by post is deemed effected`
- Tas: `s 30(2): the day service by registered post is deemed to have been effected`
- ACT: `s 250 (4): the sender has reason to suspect the document was not received`

### Ages and anniversaries (6)

The shared module carries the day a person attains an age and the age on a day for the jurisdictions that have them; these are further functions of the age and anniversary sections (Vic s 55(2), NT s 30, ACT s 149) and a helper of SA s 27(6).

- NSW: `s 37 the person is under the age of n years at a moment`
- Vic: `s55(2)(b) had not attained the full age of 18 years before 26 January 1984`
- SA: `s 27(6): the anniversary of a day in a later year`
- ACT: `s 149: the birthday falls in the year`
- NT: `s 30(2), (3): the day on which the anniversary of the birth occurs in`
- NT: `s 30(1): the person has attained the age on`

### Time of day and standard time (5)

No shared function was written for the expressions of clock time that Vic s 44(5) and (7) and NT ss 28(3) to (5) and 29 deal with.

- Vic: `s44(7) the time that now, heretofore and hereafter refer to`
- Vic: `s44(5) hours ahead of Coordinated Universal Time that an expression of time means`
- NT: `s 29: the time after midnight for four digits`
- NT: `s 28(3): a reference to time is read as a reference to`
- NT: `s 28(4), (5): a time expression is read as`

### Duties with no time provided, and extensions of time (7)

No shared function was written for the rules that say when a thing must be done if no time is fixed (Qld s 38(4), SA s 44(3), and the WA functions below).

- Qld: `when a thing is to be done if no time is provided (s 38(4))`
- WA: `the last day for an act or thing when no time may be fixed`
- WA: `the act or thing must be done with all convenient speed and as often as occasion arises`
- WA: `an application to extend may be made after the time has expired`
- WA: `the period the Second Schedule section allows`
- WA: `the last day to make the complaint and commence the proceedings`
- SA: `s 44(3): the thing must be done as soon as is reasonably practicable`

### Alternative readings (9)

The shared module follows the main reading of each source module and carries none of the alternative readings.

- Cth: `ALTERNATIVE READING: the last day of a period of`
- Cth: `ALTERNATIVE READING: the last day of a counted period, expressed as`
- WA: `reckon a period counting the named day as its first day, the other reading`
- WA: `the time within a time before a day, rolling back from an excluded last day, the other reading`
- SA: `s 4 and s 44(1) item 8, alternative reading: the last day of a period of months counted one month at a time`
- SA: `s 4, alternative reading: the last day of a period of years counted in one step`
- ACT: `dictionary, month, other reading: the last day of N months counted to the corresponding day of the Nth following calendar month`
- ACT: `dictionary, year, other reading: the last day of N years counted as 12 months each from any starting day`
- ACT: `s 151, other reading of years: the last day of a period of days, months or years that begins on or from a stated day`

### Dates the Acts name (23)

No shared function was written for the rules that turn on a date the Act itself names (for example Vic ss 2, 9(2), 10(3), 21, 36, 38AA and 38EA, Tas ss 6(7), 14(1), 44 and 46C(2), ACT ss 126 and 146).

- NSW: `s 30C(6) the amending Act was enacted after 1 January 2009`
- Vic: `s9(2)(e) last day of the period in which an Act is cited by its number only`
- Vic: `s9(2)(f) first day of the period in which an Act is cited by year and number`
- Vic: `s10(3) first day on which an Act passed without a short title leaves its long title out of the Act`
- Vic: `s21(1) day on which Imperial and New South Wales Acts are read as references to Victoria`
- Vic: `s21(2) day on which an Act is read as referring to the Legislative Council of Victoria`
- Vic: `s36 first day of the period in which headings, examples, notes, diagrams and punctuation form part of an Act`
- Vic: `s38AA(2) day Standards Australia took over from the Standards Association of Australia`
- Vic: `s38EA(2) first day on which registered medical practitioner is defined`
- Vic: `endnote 2 day sections 57, 58, 60 and 61 of Act No. 55/2025 came into operation`
- Tas: `s 9(2): the day an Act assented to before the commencement of section 8 of the 1981 Amendment Act is deemed to have come into operation`
- Tas: `s 9(3): the day an Act assented to on or after the commencement of section 8 of the 1981 Amendment Act comes into operation`
- Tas: `s 6(7): an Act was passed after 5th August 1853`
- Tas: `s 44: a matter is before 12th April 1927`
- Tas: `s 46: the date of the letters patent under the Great Seal that first constituted the Supreme Court`
- Tas: `s 10A(2): a provision was passed after the commencement of the Justice Legislation (Miscellaneous Amendments) Act 2000`
- Tas: `s 38(2)(c): a term of imprisonment exceeds 3 years`
- Tas: `s 47(10): a regulation was made before the commencement of the Legislation Publication Act 1996`
- Tas: `s 47(11): a regulation was made on or after the commencement of the Legislation Publication Act 1996`
- Tas: `s 46C(2): a written law was enacted or made before the commencement of the Australia Acts`
- ACT: `s 146 (4): the application date`
- ACT: `s 146 (4): the law or the provision is an applicable law or applicable provision`
- ACT: `s 126 (2): the heading to a section or subsection is part of the Act or instrument`

### Commencement of other instruments, provisions and parts, and the power to fix a day (36)

The shared module carries the commencement of an Act in the cases of the table above; this group holds further commencement rules (statutory rules, subsidiary legislation, name and citation provisions, early and retrospective commencement), and some names may be wrappers of a function the shared module carries under another name.

- NSW: `s 39(1)(b) and (2A) the day a statutory rule commences`
- Vic: `s2 day the Act came into operation`
- Vic: `s11(3) date of the passing of an Act`
- Vic: `s11(4) date of commencement of an Act or portion whose provisions began on different days`
- Vic: `s10A(3),(4) day an Act with no commencement provision is taken to come into operation`
- Qld: `the moment the citation and commencement provisions of an Act commence (s 15C(1))`
- WA: `the day this Act came into operation`
- WA: `counts as passed or made after the commencement for ss 17, 25, 43(6), 50 and 64`
- WA: `the day the proclamation provision and the short title come into operation`
- WA: `the power to fix a day extends to a day not prior to publication`
- WA: `the power to fix a day extends to the number of different days fixed`
- WA: `the day an instrument or notice made early takes effect`
- WA: `the day a reference to commencement means`
- WA: `the day subsidiary legislation comes into operation`
- WA: `the power to fix a day for subsidiary legislation extends to the number of different days fixed`
- WA: `the power may be exercised on`
- SA: `s 27(2): the day a Bill is taken to have been assented to`
- SA: `s 27(3) and (5): the day fixed by the proclamations made so far`
- Tas: `s 9(3A): the day the provision for commencement by proclamation and the short title provision come into operation`
- Tas: `s 9(4): the day an Act reserved for the signification of the Sovereign's pleasure comes into operation`
- Tas: `s 38A(2)(c): the day fixed for commencement is a day on or after publication or notification in the Gazette`
- Tas: `s 38A(2)(d): the day an instrument other than one fixing a commencement day takes effect`
- Tas: `s 38A(2)(d): an instrument may not be expressed to take effect on a day before publication or notification`
- ACT: `s 73 (2), (3), (4): the commencement chosen from the default and the commencement provided`
- ACT: `s 73 (2) and (3): when a legislative instrument commences`
- ACT: `s 73 (4): when a statutory instrument that is not a legislative instrument commences`
- ACT: `s 75 (1), (2): when the provisions providing for a law's name and commencement commence`
- ACT: `s 75AA (2): when a provision identifying the amended law commences`
- ACT: `s 75A (1): an Act or legislative instrument commences retrospectively`
- ACT: `s 75A (2): a statutory instrument that is not a legislative instrument commences retrospectively`
- NT: `s 17 "calendar month": the last day of the calendar month commencing at the beginning of`
- NT: `s 17 "year": the last day of consecutive years, the first commencing at the beginning of`
- NT: `s 6: the first day on which a proposed law reserved for the Governor-General has effect`
- NT: `s 6B: the commencement of the provisions concerned`
- NT: `s 63B: the day on which subordinate legislation commences`
- NT: `s 63B(3), (4): the provision of subordinate legislation is of no effect`

### Rolling off a day of rest, business days and periods composed of other rules (26)

Many of these are the long or short forms of rules the shared module carries through `the latest day on which a thing may be done` and its composition with `the last day of a period`; others (Tas s 29(4) and (5), ACT s 151(3)) are rules not carried.

- Cth: `is a holiday for the time for doing a thing`
- Cth: `the thing is done within the time allowed`
- NSW: `s 36(1) the day falls within a period of n days dating from a given day`
- NSW: `s 36(2) the first day, on or after a day, that is not a Saturday, a Sunday, or a public holiday or bank holiday in the place`
- NSW: `s 36 the latest day on which a thing may be done within a period of n units dating from a given day`
- Qld: `the last day on which the purpose can be fulfilled within days (s 38(1)(b))`
- Qld: `the day on which the purpose is to be fulfilled is counted in the period (s 38(1)(a) and (b))`
- Qld: `the day a period beginning on a given day ends once moved off an excluded day (s 38(1) and (2))`
- WA: `the previous day that is not an excluded day, counting the day itself`
- SA: `s 46: an exclusion of public holidays extends to a holiday`
- SA: `s 44(2): the next day that is a business day`
- SA: `s 44(1) and (2): the last day on which a thing may be done within a period`
- Tas: `s 29(3): the next day afterwards not being an excluded day`
- Tas: `s 29(3): the next day before not being an excluded day`
- Tas: `s 29(5): the day on which an act directed or allowed to be done on a particular day is in due time`
- Tas: `s 29(4): the last day on which a document may be filed or registered`
- Tas: `s 29(6): the day reached by counting days backwards from a day, excluded days not reckoned`
- Tas: `s 29(6): the last day of a time not exceeding 6 days reckoned forwards from`
- Tas: `s 29(6): the first day of a time not exceeding 6 days reckoned backwards from`
- Tas: `s 29(3)(a) and s 46: the last day on which an act is in due time, a period of calendar months reckoned forwards from`
- ACT: `s 151 (3): the thing may be done on the stated day`
- ACT: `dictionary, working day: the day is a working day`
- ACT: `s 151 and s 151A: the last day on which the thing may be done within a period that begins on or from a stated day`
- ACT: `dictionary, working day: the first working day after a day, searching a limited number of days`
- NT: `s 28(2): the first day, on or after the day, that is not a Saturday, a Sunday or a public holiday`
- NT: `s 28(1), (2): the last day on which a thing may be done within a period dating from`

### Components, other forms of carried rules, and names no keyword matched (34)

Many of these are the long or short form of a rule the shared module carries (for example NSW `s 36(1) the last day of a period of n days dating from a given day`) or a helper for it, and some are rules not carried.
Whether each is carried was not checked name by name.

- Cth: `is one of the 12 calendar months`
- Cth: `the last day of a month starting on`
- Cth: `the specified day names the end of a period expressed in this way`
- Cth: `the first day of the period`
- NSW: `s 36(1) the last day of a period of n days dating from a given day`
- NSW: `s 36(1) and Schedule 4 the last day of a period of n calendar months dating from a given day`
- Vic: `s55(2)(a) day before which the three months are counted`
- Vic: `s44(1) first day counted in a period expressed to begin on or be reckoned from a day`
- Vic: `s44(1) last day of a period of n days reckoned from a day`
- Vic: `s44(1),(6)(b) last day of n calendar months reckoned from a day, reading A`
- Vic: `s44(1),(6)(b) last day of n calendar months reckoned from a day, reading B`
- Vic: `s44(1),(6)(c) last day of n years reckoned from a day`
- Vic: `s44 last day of a period counted forward from a day`
- Vic: `s44(6)(b) first day of n calendar months ending immediately before a day`
- Vic: `s25 moment until which a temporary subordinate instrument or provision continues in operation`
- WA: `what the Act says a word for a length of time means`
- WA: `the end of a period whose last day by the calendar is`
- SA: `s 4: is one of the 12 months of the calendar year`
- SA: `s 4: the number of days in a week the Act states`
- SA: `s 4: the first day of the month a number of months after the month of a day`
- SA: `s 44(1) item 1: the days of a period expressed to occur between 2 days`
- SA: `s 44(1) item 1: a day is one of the days of a period expressed to occur between 2 days`
- Tas: `s 29(1) and s 46: the first day of a period of calendar months reckoned backwards from`
- Tas: `s 29(1): the last day of a period of years reckoned forwards from`
- Tas: `s 29(1): the last day of a period of weeks reckoned forwards from`
- ACT: `s 151 (2), table 151: the first day of a period that begins at, on, with or from a stated day`
- ACT: `s 151: the last day of a period of days that begins on or from a stated day`
- ACT: `dictionary, month: the last day of the month that begins at the start of a day`
- ACT: `dictionary, month: the first day of the month that ends at the end of a stated day`
- ACT: `dictionary, month: the first day of a run of successive months that ends at the end of a stated day`
- ACT: `s 73 (4) (a): the day a statutory instrument that is not a legislative instrument is made or approved`
- ACT: `s 75 (3): the notification day of a statutory instrument that is not a legislative instrument`
- ACT: `s 151 (5), s 151A (4), s 151C (6): the law or the provision is an applicable law or applicable provision`
- NT: `s 28(1): the first day counted in a period dating from`

