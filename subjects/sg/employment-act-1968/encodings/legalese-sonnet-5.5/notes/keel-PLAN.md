# PLAN: the Employment Act 1968 (Singapore), for the three part agents

Status: written by the keel after `ea-core.l4`, `ea-definitions.l4` and their tests were finished and checked (`check.sh`: 0 errors, 155 assertions satisfied, same on the 1.6.108 column).
Where this file says what the text contains, it was checked against `inputs/EmA1968.txt` by `grep` on 2026-11-05; the places where it is a proposal and not a fact say "proposed".

Source: `EmA1968.txt`, a plain-text rendering made by a converter script from Singapore Statutes Online (2020 Revised Edition, informal consolidation, "version in force from 5/12/2025").
It is not the official text, and nothing here is "verified against the official text".

## 1. Who does what

| agent | line ranges of `EmA1968.txt` (copied unchanged from `inputs/PARTS.md`) | words |
| --- | --- | --- |
| keel | 1-784 | 3906 |
| ea1 | 785-2596 | 11824 |
| ea2 | 2597-4611 | 11938 |
| ea3 | 4612-6790 | 11039 |

What the lines are, by the text's own headings (checked with a grep for `PART` and `SCHEDULE` lines):
- keel 1-784: title page, Arrangement of Sections, Part 1 (ss 1-7), including all of s 2(1), the definitions.
- ea1 785-2596: Parts 2 to 6 (heading lines 786, 1266, 1746, 2368, 2475): contracts of service, payment of salary, rest days and hours of work, and the rest of those Parts.
- ea2 2597-4611: Parts 6A to 14 (heading lines 2598, 2619, 2632, 2759, 3378, 3798 (Part 11, repealed), 3804, 4140, 4419).
- ea3 4612-6790: Part 15 (line 4613), Part 15A (5012), Part 16 (5228), the First Schedule (5513), Second (5530), Third (5542-5712), Fourth (5713-5758) and Fifth (5759-5825), and the Legislative History (5826 on).
  The Legislative History is a table of earlier enactments, not a provision of the Act; the brief's rules decide whether a row of it is `inert` (reason 1).

Not owned by any row of `PARTS.md`: `inputs/EmA1968-S200-2019.txt` (the Employment (Retrenchment Reporting) Notification 2019), which the brief names as in scope.
It is made under s 96A (line 3983, inside ea2's range), so this plan recommends that ea2 takes it.
The lead must confirm; the keel has not encoded it.

## 2. Files and names (every part follows these exactly)

1. **Files.** Every module of part `X` begins `X-` (`ea1-...`, `ea2-...`, `ea3-...`). Every module of the keel begins `ea-`. The core is `ea-core.l4`; a part never edits it and never waits for it.
2. **Imports.** A part imports `prelude`, `daydate`, `ea-core` and its own other modules. It does not import another part. It does NOT import `ea-definitions` (section 5 says why and what to do instead).
3. **Every top-level name begins with the section label it implements**, in the Act's own numbering: `s 4(2)(a) ...`, `sch 3 para 2 ...`. This holds for functions, constants, **types, and the constructors of the types a part declares**: a constructor name is global to the merged folder, and two parts that both write `Yes` or `Other` break the merge. Types and constructors that more than one part needs live only in the core.
4. **No two parts define the same name.** A name defined in two modules that are imported together cannot be used at all.
5. **A part never defines a name beginning `s 2(1)`, `s 3`, `s 5`, `s 6` or `s 7`**: those belong to the keel.
6. **If a part needs a type or constructor the core lacks**, it defines it under its own section prefix and records it in `NEEDS-CORE.md` in its own folder; the lead hoists it at the merge.
7. **A function's name says what the section says**: `s 47(2) the instrument is valid`, not `is the instrument valid`, not `may I ...`.
8. **Every rule has its own `GIVEN`.** Main (1.6.108 and 1.6.109) does not accept a `GIVEN` shared by the rules under a `§` heading: the later rules report `check/unknown-identifier` for its name (measured 2026-11-05).
9. **Money is a `NUMBER` of Singapore dollars; a count of days, weeks, months or years is a `NUMBER`; a calendar day is `Date day month year`; an amount or date the Act does not give is a `MAYBE`, never a made-up zero.**

### Dialect facts the keel measured (main, 1.6.108 and 1.6.109)

- Parentheses and double quotes inside a backtick name parse: `` `s 2(1) "week" the period is a week` `` is a valid name. A backtick name with double quotes also works as a `GIVEN` parameter name, so `the answer of s 2(1) "workman" the person is one` is a valid input (probed on both builds).
- `NOT` needs parentheses; each `#ASSERT` is on one line; no `REFUSE`, no `#ASSERT REFUSED`, no `BECAUSE`; `Date day month year`, never your own `YMD`.
- `length` and `isEmpty` are not in the prelude. `null`, `all` and `sum` are.
- **A long sum written with `PLUS` through local names in a `WHERE` can make `l4 check` run for minutes and print nothing** (it did here: killed at 60 seconds, no error, no output). Write `sum (LIST ...)` over inline terms, one term per line; that took about a second on both builds. Define a local before the expression that uses it. `NOTES.md` has the measurements.
- A failing `#ASSERT` is an error in the output ("assertion failed"), so `check.sh` goes red on it. `check.sh` does not count warnings: also grep each module's `l4 run` output for `DiagnosticSeverity_Warning`.

## 3. What each part should expect to use from the core

`ea-core.l4` declares exactly these sixteen types and nothing else: no rule, no constant, no assertion.
Constructor names are whole phrases.
"First cited at" is the `@ref` above the type in the core, which quotes that provision.

| core type | what it is | first cited at |
| --- | --- | --- |
| `Party to a contract of service` | the employee or the employer | s 10(1) |
| `Kind of employer` | individual, body corporate, partnership, unincorporated association other than a partnership, the Government, a statutory authority, the personal representatives or trustees of a deceased employer | s 2(1) "employer" |
| `Official or body the Act names` | President, Minister, Commissioner, deputies and assistants, authorised officer, inspecting officer, authorised person, medical officer, Comptroller of Income Tax, the Employment Claims Tribunal, the Industrial Arbitration Court, the High Court's General Division, a District Court, a Magistrate's Court, a Youth Court; never a seat | s 3(1) |
| `Kind of claimant` | employee, employer, subcontractor for labour | Second Schedule |
| `Family relationship to the employee`, `Family member of the employee` | the relationship, whether the person lives with or depends on the employee, and age | s 2(1) "dependant" |
| `Basis of pay` | the unit pay is fixed for: hour, day, week, month, other period, completed piece, task | s 2(1) "basic rate of pay" |
| `Pay for a period` | one `NUMBER` for each item of pay that "salary", "gross rate of pay" and "basic rate of pay" count or leave out | s 2(1) "salary" |
| `Kind of day` | working day, rest day, public holiday, substituted day, and the kinds of leave day | s 89(6) |
| `Period of days` | first day and last day, both counted | s 20(1) |
| `Dates of the employment` | began on, and ended on (a `MAYBE DATE`) | s 9(1) |
| `How the employment ended` | not ended; specified work done or period expired; resigned; dismissed; ended otherwise | s 87A(6) |
| `Ground of dismissal` | misconduct; redundancy or reorganisation; some other ground or none | s 14(1) |
| `Notice of termination` | given by, given on, last day of the notice, in writing | s 10(5) |
| `Relief a claimant may seek` | reinstatement, compensation, a sum the Commissioner considers just | s 14(2) |
| `Penalty on conviction` | least fine, greatest fine (`MAYBE`), longest imprisonment in months (`MAYBE`) | s 34(2) |

Reading the table: a field is a fact a witness could state, not a rule.
Whether the facts make a person an "employee" or a "workman" is a rule, and it lives in the keel's `ea-definitions`.
The core has no constants: no figure in the text is stated in more than one part's range, so each figure stays with the section that states it.

## 4. Seams

A seam is a provision in one part whose answer another part's provision needs.
Parts run in parallel and cannot import each other, so the asking part takes the answer as an INPUT, and the lead wires it at the merge.

The contract (proposed, not yet exercised by any part):
- The asking part adds a `GIVEN` parameter to each rule that needs the answer, named `the answer of <label>` (for example `the answer of s 35(a)`), with exactly the type in the table, which is the answering rule's result type: a `MAYBE BOOLEAN` or `MAYBE NUMBER`, so that a `NOTHING` is carried on and never turned into `FALSE`.
- The asking rule answers `NOTHING` where its answer depends on a `NOTHING` input.
- The answering part names its function by its own section label as usual, and lists in `SEAMS-ANSWERED.md` (its folder) the label, the function name and its result type, for every row below it answers.
- Any seam not in the table that a part finds goes in `SEAMS-FOUND.md` (asking section, answering section, the input name and the type used).

Each row below was found by a grep of the text on 2026-11-05 for the cited reference, and read.

| # | asking section (part) | answering section (part) | input: name and type |
| --- | --- | --- | --- |
| S1 | s 88(4A) (ea2), line 3435: "an employee to whom Part 4 applies by virtue of section 35(b) or who is a workman mentioned in section 35(a)" | s 35(a) (ea1) | `the answer of s 35(a)`: MAYBE BOOLEAN |
| S2 | the same sentence of s 88(4A) (ea2) | s 35(b) (ea1) | `the answer of s 35(b)`: MAYBE BOOLEAN |
| S3 | s 88A, line 3541 (ea2) | s 35(a), s 35(b) (ea1) | the two inputs of S1 and S2 |
| S4 | s 27(3)(b)(i) (ea1), line 1531: "annual leave in excess of the annual leave to which the employee is entitled under section 88A" | s 88A (ea2) | `the answer of s 88A the days of paid annual leave`: MAYBE NUMBER |
| S5 | s 88(4) (ea2): the extra day's salary for work on a public holiday | s 41A(2) (ea1), line 2061 on: the Commissioner's written order directing that the entitlement to extra pay under 37(2) or (3), 38(4), 40(4) or 88(4) does not apply | `the answer of s 41A(2)`: MAYBE BOOLEAN |
| S6 | ss 11, 20A, 28, 37, 38 (ea1); ss 76, 87A, 88, 88A, 89 (ea2): a day's pay at the gross rate or the basic rate (the sections found by a grep for "rate of pay") | s 107A (ea2), which says only that the rate per day of an employee on a monthly rate or on piece rates "is to be calculated in accordance with" the second or third column of the Third Schedule; and the Third Schedule (ea3) | `the answer of sch 3 gross rate of pay per day`: MAYBE NUMBER; `the answer of sch 3 basic rate of pay per day`: MAYBE NUMBER |
| S7 | s 38 (ea1), lines 1970-1972, the Fourth Schedule | Fourth Schedule (ea3) | `the answer of sch 4 hourly basic rate of pay`: MAYBE NUMBER |
| S8 | s 76 (ea2), line 2800 | Fifth Schedule (ea3) | `the answer of sch 5 days`: MAYBE NUMBER |
| S9 | s 126A(a) and s 126B (ea3), lines 5020-5057 | s 95(1) (ea2) | `the answer of s 95(1)`: MAYBE BOOLEAN, meaning "the employer failed to comply" |
| S10 | s 126A(a) and s 126B (ea3) | s 95A(2) (ea2) | `the answer of s 95A(2)`: MAYBE BOOLEAN, the same meaning |
| S11 | s 126A(a) and s 126B (ea3) | s 96(1) (ea2) | `the answer of s 96(1)`: MAYBE BOOLEAN, the same meaning |
| S12 | s 126A(aa) and s 126B (ea3) | s 96A (ea2) with the Notification (S 200/2019) | `the answer of s 96A`: MAYBE BOOLEAN, meaning "the employer failed to comply with a requirement in the notification" |
| S13 | s 116(3) (ea3), line 4720: "liable as a principal under section 65 to pay any salary due" | s 65 (ea1) | `the answer of s 65 the principal is liable to pay the salary`: MAYBE BOOLEAN |
| S14 | s 105(1)(a) (ea2): "an offence under section 21, 22 or 23 read with section 34" | s 34 (ea1) | `the answer of s 34 the employer is guilty of an offence under s 21, 22 or 23`: MAYBE BOOLEAN |
| S15 | s 48 (ea1), line 2296: "shall be guilty of an offence" with no penalty stated | s 112 (ea2): the penalty "for which no penalty is otherwise provided", first offence and subsequent offence | `the answer of s 112 first conviction` and `the answer of s 112 subsequent conviction`: each MAYBE of `Penalty on conviction` |
| S16 | s 14, s 33 and s 35 (ea1), the lines that say "managerial or executive" | no section defines it | `the employee is employed in a managerial or an executive position`: BOOLEAN (a plain fact, not a seam; the name is fixed so that the modules agree) |

Notes:
- S6 is the large one. `Pay for a period` (core) lets ea3 work out the two daily rates from the contract's items; ea1 and ea2 must not recompute them. The Third Schedule is about an employee on a monthly rate or on piece rates (s 107A says so); for an hourly, daily or weekly rate the text is silent, and ea3 decides, records it as a fork, and answers `NOTHING` where it cannot.
- S15: the caller picks the first or the subsequent conviction; the asking part passes the record through.
- The keel's own definitions that take another part's answer take it the same way: "overtime" takes the Part 4 limit (ea1, ss 38 and 40), "civil contravention" takes the s 126A declaration (ea3), "workman" takes the First Schedule (ea3).

## 5. The keel's definitions, and what the parts do about them

**Settled by the lead (the keel assumed otherwise):** the parts DO have `ea-definitions.l4`, as a read-only copy in their folder, beside `ea-core.l4`.
A part `IMPORT`s `ea-core` and `ea-definitions` and calls the keel's functions directly, by the exact names in the table below.
Ignore every passage in this file that says a part takes `the answer of <keel function>` as an input: that was the plan for parts without the module.
A part's own names never start `s 2(1)`, `s 3`, `s 5`, `s 6` or `s 7`, so nothing collides. The keel's tests module `ea-definitions-tests.l4` is not distributed.

The keel's functions, with what each takes (in order) and what it answers.
`MAYBE BOOLEAN` answers `JUST TRUE`, `JUST FALSE` (the Act says no) or `NOTHING` (the Act does not say).

| function | takes, in order | answers |
| --- | --- | --- |
| `s 2(1) "basic rate of pay" the amount` | `Pay for a period` | NUMBER |
| `s 2(1) "gross rate of pay" the amount` | `Pay for a period` | NUMBER |
| `s 2(1) "salary" the amount` | `Pay for a period` | NUMBER |
| `s 2(1) "wages" the amount` | `Pay for a period` | NUMBER |
| `s 2(1) "productivity incentive payment" the payment is one` | 4 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "day" the period is a day` | NUMBER, BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "week" the period is a week` | NUMBER, BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "hours of work" the number of hours` | 2 x NUMBER | NUMBER |
| `s 2(1) "overtime" the number of hours` | NUMBER, MAYBE NUMBER | MAYBE NUMBER |
| `s 2(1) "authorised officer" the person is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "inspecting officer" the person is one` | BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "medical officer" the person is one` | 4 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "medical practitioner" the person is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "approved medical institution" the institution is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "dependant" the member of the family is one` | `Family member of the employee` | MAYBE BOOLEAN |
| `s 2(1) "domestic worker" the person is one` | `s 2(1) "domestic worker" Kind of work`, BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "seafarer" the person is one` | 5 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "contractor" the person is one` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "principal" the person is one` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "subcontractor" the person is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "subcontractor for labour" the person is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "constructional work" the work is constructional work` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "constructional contractor" the person is one` | 4 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "contract of service" the agreement is one` | 4 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "workman" proviso: the person is deemed to be a workman` | BOOLEAN, LIST OF `s 2(1) "workman" Time in one salary period` | MAYBE BOOLEAN |
| `s 2(1) "workman" the person is one` | 6 x BOOLEAN, MAYBE BOOLEAN, BOOLEAN, MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "employee" the person is one` | 7 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "employer" the person is one` | 5 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "dismiss" the ending of the contract is a dismissal` | 4 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "place of employment" the place is one` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "no-pay leave" the leave is no-pay leave` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "quarters" the building is quarters` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "machinery" the thing is machinery` | `s 2(1) "machinery" Kind of thing` | MAYBE BOOLEAN |
| `s 2(1) "industrial undertaking" the undertaking is one` | 5 x BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "collective agreement" the agreement is one` | MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "mediation request" the request is one` | MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "stillborn child" the child is one` | MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "Tribunal" the body is the Tribunal` | MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "civil contravention" the contravention is one` | MAYBE BOOLEAN | MAYBE BOOLEAN |
| `s 2(1) "confinement" the event is a confinement` | 2 x BOOLEAN | MAYBE BOOLEAN |
| `s 3(1) the officer's performance of the Commissioner's duty or exercise of the Commissioner's power is deemed duly done` | `Official or body the Act names`, BOOLEAN | MAYBE BOOLEAN |
| `s 5 this Act, or the Part or provision, applies at the premises` | 3 x BOOLEAN | MAYBE BOOLEAN |
| `s 6 this Act relieves the employer of the duty or liability` | BOOLEAN | MAYBE BOOLEAN |
| `s 6 this Act limits the power given to the public officer` | BOOLEAN | MAYBE BOOLEAN |

Definitions in the parts' ranges that are left to the parts (found by a grep for "In this section", "In this Part", "In this Schedule" and quoted terms; the part owns the full reading):
- ea1: s 18A(13) ("affected employee", "trade union", "transfer", "undertaking"); s 26(2) ("CSHL Scheme recovery body", "MediShield Life Scheme recovery body"); s 33(7) ("employees" is deemed to include ...); s 37(3A) ("normal hours of work" and the rest of that subsection); s 41 ("week" for ss 36, 38 and 40); s 47(5) ("award", "collective agreement", "company", "operative date", "VCC Act"); s 50 ("annual wage supplement", "variable payment", "wages").
- ea2: s 66A(1) ("part-time employee"); s 67A ("child", "young person"); s 87A(8); s 95(5) ("employee record"); s 95A(7) ("key employment term"); s 113A(6) ("body corporate", "partner").
- ea3: s 115(4) ("employer" includes the transferor and the transferee); Third Schedule item 5 ("average number of working days in a week", "week"); Fifth Schedule items 4, 5 and 6 ("week", "work pattern" and the rules for the calculation).

## 6. Things the parts will meet

- **The converter garbled s 14(2A).** Line 934 reads `(a) after having served that employer for at least 6 months in any position ...` and restarts the lettering at (a): it is the tail of limb (a) of subsection (2A), not a new limb (a). The nesting was lost at a page break. Treat limb (a) as "an employee employed in a managerial or an executive position who is dismissed with notice, or without notice but with payment of salary in lieu, after having served that employer for at least 6 months in any position", and record this reading in the fork register. A grep for a restarted `(a)` found the same glitch at line 3370, in s 87A(8) (the "relevant period" definition). The Third, Fourth and Fifth Schedules (lines 5542-5825) are tables flattened by the converter, with some rows split across lines; read them as tables and expect cell-by-cell checks to be needed.
- **Dated shapes are outside the keel's range.** The keel found none in lines 1-784 (only the date of enactment and amendment notes). A grep of the other ranges for a calendar date found them in ss 34, 48 and 65 (ea1), ss 76, 84, 84A, 87, 87A and 95A (ea2) and s 115 (ea3). Which of them are rules that differ by date (for example confinement or notice before and after a day) and which are only citations of an earlier enactment is for the owning part to read. Whether any earns a second encoding in the unstable dialect is for that part to judge, after its main encoding is complete.
- **Other Acts are not among the sources** ("Employment Claims Act 2016", "Industrial Relations Act 1960", "Work Injury Compensation Act 2019" and others). Ask the borrowed fact as an input and say so; the keel's pointer definitions (collective agreement, mediation request, stillborn child, Tribunal) do exactly that.
- **Figures left to the Minister or to regulations** ("prescribed", "such other amount") are inputs or `NOTHING`, never guessed.
- **Reading a result.** `JUST TRUE` and `JUST FALSE` are answers the text gives in its own words; `NOTHING` is "the Act does not answer on these facts" and is never read as no. Every branch that answers no carries `-- FALSE-kind (the text says no in its own words): "<quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording. The keel's `NOTES.md` has the section `### Reading a result: FALSE and NOTHING` and the policy for "means ... and includes" (fork F2), which the parts should follow so the merged row reads one way.
- **Uniform policy for "means X and includes Y"** (fork F2 in the keel's `NOTES.md`): `JUST TRUE` if X or Y, otherwise `NOTHING` (NOTHING-kind includes). Follow it unless the text gives a reason not to, and record the exception.
