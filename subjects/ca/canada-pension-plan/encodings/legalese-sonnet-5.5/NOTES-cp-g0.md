# NOTES: the keel of the Canada Pension Plan encoding (cp-g0)

This folder holds the shared vocabulary ("the keel") for the Canada Pension Plan Act (R.S.C. 1985, c. C-8) and the Canada Pension Plan Regulations (C.R.C., c. 385).
It is written for the eight piece agents (cp1 to cp6, cr1, cr2) who encode the rest of the text and cannot see one another.
The two source files are `R.S.C.-1985-c.-C-8.txt` and `C.R.C.-c.-385.txt`.
Each is an unofficial plain-text rendering made by a converter script from the Justice Laws consolidation (the Act file says it is current to 2026-09-30 and last amended 2024-12-17).
Nothing in this folder has been checked against the official text, and nothing here claims to be.
Every `src:N` locator in the `.l4` files is a line number of the Act file.

The keel covers lines 1 to 121 of the Act file: the notice and title block, section 1, section 2 (interpretation), sections 3 and 4 (where the Act applies) and section 4.1 (electronic means).
No enactment, assent or commencement date appears in those lines, so no date of that kind is carried as a value.
The title block gives the citation "R.S.C., 1985, c. C-8" and nothing more.
The seat of every piece is the individual to whom the law is applied: a worker, self-employed person, survivor, child or person with a disability.

**Files.**

| file | what it holds |
| --- | --- |
| `cpp-core.l4` | the shared types and the `YMD` date shim; declarations only, no rules |
| `cpp-core-calendar.l4` | month arithmetic and time limits (infrastructure; no provision licenses it) |
| `cpp-core-age.l4` | section 2(2): when a specified age is deemed to be reached |
| `cpp-core-definitions.l4` | section 2(1): the definitions that can be worked out from facts |
| `cpp-core-application.l4` | sections 3, 4 and 4.1: provinces with a comprehensive plan, and where the Act applies |
| `cpp-core-tests-calendar.l4`, `cpp-core-tests-age.l4`, `cpp-core-tests-definitions.l4`, `cpp-core-tests-application.l4` | tests with hand-written expected values; not to be copied into a piece folder |
| `PROGRESS.md` | what was done and what each decision rests on |

## Vocabulary

Every type and every constructor of an enumeration in `cpp-core.l4`, one row each.
The `licensed by` column names the provision that gives the type its members; line numbers are lines of the Act file.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `YMD` | function (shim) | `YMD year month day` builds a DATE; the stable `daydate` has none, so the core defines it as `Date day month year`; never define it again | none; a gap of the stable binary (see "What the stable binary does not accept") |
| `Tier` | enumeration | the three parallel regimes: base, first additional (from 2019), second additional (from 2024); almost every defined term of Parts I and II comes in all three | s 2(1) "base contribution", "first additional contribution", "second additional contribution", lines 25, 45, 67 |
| `the base tier` | constructor of `Tier` | the base contribution and everything computed alongside it | line 25; subsections 8(1), 9(1), 10(1) |
| `the first additional tier` | constructor of `Tier` | the first additional contribution and its parallel terms | line 45; subsections 8(1.1), 9(1.1), 10(1.1) |
| `the second additional tier` | constructor of `Tier` | the second additional contribution and its parallel terms | line 67; subsections 8(1.2), 9(1.2), 10(1.2) |
| `Contributing capacity` | enumeration | the three capacities in which a contribution is made and a contribution rate is set | s 2(1) "contribution rate", line 34; sections 8, 9, 10 |
| `contributing as an employee` | constructor of `Contributing capacity` | an employee (section 8) | line 34 |
| `contributing as an employer` | constructor of `Contributing capacity` | an employer (section 9) | line 34 |
| `contributing as a self-employed person` | constructor of `Contributing capacity` | a self-employed person (section 10) | line 34 |
| `Kind of benefit` | enumeration | the eight benefits the Act pays, in the order of paragraphs 44(1)(a) to (h) | s 44(1), lines 973 to 995 |
| `a retirement pension` | constructor of `Kind of benefit` | paragraph 44(1)(a) | line 973 |
| `a disability pension` | constructor of `Kind of benefit` | paragraph 44(1)(b) | line 974 |
| `a death benefit` | constructor of `Kind of benefit` | paragraph 44(1)(c) | line 979 |
| `a survivor's pension` | constructor of `Kind of benefit` | paragraph 44(1)(d) | line 980 |
| `a disabled contributor's child's benefit` | constructor of `Kind of benefit` | paragraph 44(1)(e) | line 988 |
| `an orphan's benefit` | constructor of `Kind of benefit` | paragraph 44(1)(f) | line 993 |
| `a post-retirement benefit` | constructor of `Kind of benefit` | paragraph 44(1)(g) | line 994 |
| `a post-retirement disability benefit` | constructor of `Kind of benefit` | paragraph 44(1)(h) | line 995 |
| `Minister` | enumeration | the two Ministers the Act names: National Revenue for Part I and section 4.1, Employment and Social Development for Parts II and III | s 5(1) line 124; s 42(1) line 945; s 91 line 2636 |
| `the Minister of National Revenue` | constructor of `Minister` | Part I (section 5(1)); section 4.1; the administration of Part I (section 92(2)) | lines 124, 120 |
| `the Minister of Employment and Social Development` | constructor of `Minister` | Parts II and III (sections 42(1), 91); the Minister of section 3 and subsection 4(3) | lines 945, 2636 |
| `Time limit` | enumeration with fields | a period counted in days, months or years; the one way a time limit is written | s 2(1) "balance-due day" line 23 (6 months); "common-law partner" line 31 (one year); s 3(2) line 99 (twelve months) |
| `a number of days` | constructor of `Time limit` | field `number of days`, NUMBER | as above |
| `a number of months` | constructor of `Time limit` | field `number of months`, NUMBER | as above |
| `a number of years` | constructor of `Time limit` | field `number of years`, NUMBER | as above |
| `Province` | record | a province as the Act sees it: fields `name of the province` (STRING) and `a province providing a comprehensive pension plan` (BOOLEAN); the Act names no province and neither does the keel | s 3(1) "province providing a comprehensive pension plan", line 92 |
| `Unadjusted pensionable earnings` | record | the Act's collective noun for the three amounts: fields `base unadjusted pensionable earnings`, `first additional unadjusted pensionable earnings`, `second additional unadjusted pensionable earnings`, all NUMBER, dollars | s 2(1) "unadjusted pensionable earnings", line 79 |

**Types declared in the other modules (not in the core).**

These come with the module that needs them, so a piece that imports that module gets them; a piece must not declare a type or constructor with the same name.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Provision about reaching an age` (in `cpp-core-age.l4`) | enumeration, 11 constructors | the ten places where section 2(2) does not apply, plus `any other provision`; the constructors are `paragraph 13(1)(c)`, `paragraph 13(1)(e)`, `paragraph 13(1.2)(c)`, `paragraph 17(c)`, `paragraph 17.1(c)`, `paragraph 19(c)`, `paragraph 19(d)`, `paragraph 44(3)(a)`, `section 70`, `subparagraph 72(a)(iii)`, `any other provision` | s 2(2), line 85 |
| `Kind of representative` (in `cpp-core-definitions.l4`) | enumeration, 8 constructors | `a guardian`, `a curator`, `a committee`, `an executor`, `a liquidator of a succession`, `an administrator`, `another legal representative`, `not a representative` | s 2(1) "representative", line 61 |
| `Kind of position` (in `cpp-core-definitions.l4`) | enumeration, 10 constructors | `a judicial office`, `the office of a minister of the Crown`, `the office of a lieutenant governor`, `the office of a member of the Senate or House of Commons`, `the office of a member of a legislative assembly`, `the office of a member of a legislative or executive council`, `an office whose incumbent is elected by popular vote`, `an office whose incumbent is elected or appointed in a representative capacity`, `the position of a corporation director`, `another position` | s 2(1) "office", line 52 |
| `Kind of activity` (in `cpp-core-definitions.l4`) | enumeration, 9 constructors | `a profession`, `a calling`, `a trade`, `a manufacture`, `an undertaking of any kind whatever`, `an adventure or concern in the nature of trade`, `an office`, `an employment`, `another activity` | s 2(1) "business", line 30 |
| `Kind of matter that may be prescribed` (in `cpp-core-definitions.l4`) | enumeration, 2 constructors | `a form or the information to be given on a form`, `any other matter` | s 2(1) "prescribed", lines 57 to 59 |

**Rules you can call.**

Every rule name below is taken: do not define another rule, type, constructor or field with the same name in your own module.
Rules are called with their arguments in the order shown.
A MAYBE result is `JUST value` or `NOTHING`; `NOTHING` always means the text does not decide.

| rule | arguments | returns | source |
| --- | --- | --- | --- |
| `the month of a date` | date | DATE, the first day of that date's month | none (calendar) |
| `the month following the month of a date` | date | DATE, the first day of the next month; December rolls into January | none (calendar) |
| `the month number of a date` | date | NUMBER, year times 12 plus month | none (calendar) |
| `the number of months from the month of one date to the month of another` | date, date | NUMBER of calendar months; days ignored; negative if the second is earlier | none (calendar) |
| `the date a time limit ends` | start date, `Time limit` | DATE | none (calendar) |
| `the date a time limit before a date goes back to` | end date, `Time limit` | DATE | none (calendar) |
| `a date is within a time limit after a start date` | date, start date, `Time limit` | BOOLEAN | none (calendar) |
| `the date a person actually reaches a specified age` | date of birth, age | DATE, the birthday | none (helper for s 2(2)) |
| `the actual age of a person in whole years on a date` | date of birth, date | NUMBER | none (helper for s 2(2)) |
| `s 2(2) — the date a person is deemed to reach a specified age` | date of birth, age | DATE, first day of the month after the birthday's month | s 2(2), line 85 |
| `s 2(2) — the date a person is treated as reaching a specified age for a provision` | `Provision about reaching an age`, date of birth, age | DATE; the birthday itself for the ten excepted provisions, the deemed date otherwise | s 2(2), line 85 |
| `s 2(2) — the person is treated as having reached a specified age on a date for a provision` | `Provision about reaching an age`, date of birth, age, date | BOOLEAN | s 2(2), line 85 |
| `s 2(2)(a) — a month is counted in a period of months ending with a specified age` | month (any date in it), date of birth, age | BOOLEAN | s 2(2)(a), line 86 |
| `s 2(2)(b) — a month is counted in a period of months commencing with a specified age` | month (any date in it), date of birth, age | BOOLEAN | s 2(2)(b), line 87 |
| `s 2(1) — an applicant, in Part II` | three BOOLEANs (limbs a, b, c) | BOOLEAN | line 17 to 20 |
| `s 2(1) — a beneficiary` | BOOLEAN | BOOLEAN | line 28 |
| `s 2(1) — a contributor` | BOOLEAN, BOOLEAN, LIST OF NUMBER (per-year 53(1)(b)(i) amounts), BOOLEAN | BOOLEAN | line 35 |
| `s 2(1) — a representative of a person` | `Kind of representative` | BOOLEAN | line 61 |
| `s 2(1) — employment` | BOOLEAN (contract of service), BOOLEAN (tenure of an office) | BOOLEAN | line 43 |
| `s 2(1) — an office` | `Kind of position`, BOOLEAN (stipend) | BOOLEAN | line 52 |
| `s 2(1) — an officer` | BOOLEAN (holds it), `Kind of position`, BOOLEAN (stipend) | BOOLEAN | line 52 |
| `s 2(1) — an employee` | BOOLEAN (in employment), BOOLEAN (an officer) | BOOLEAN | line 41 |
| `s 2(1) — an employer` | BOOLEAN (liable to pay), BOOLEAN (the other is an officer), BOOLEAN (officer is paid by the person) | BOOLEAN | line 42 |
| `s 2(1) — a business` | `Kind of activity` | MAYBE BOOLEAN | line 30 |
| `s 2(1) — a benefit`, `s 2(1) — a pension`, `s 2(1) — a contribution` | BOOLEAN | BOOLEAN | lines 29, 53, 33 |
| `s 2(1) — the tier of a contribution made under a subsection` | subsection as STRING ("8(1)", "9(1.1)", "10(1.2)" ...) | MAYBE `Tier` | lines 25, 45, 67 |
| `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | `Tier`, `Contributing capacity` | STRING | lines 25, 45, 67 |
| `s 2(1) — the unadjusted pensionable earnings of a tier` | `Unadjusted pensionable earnings`, `Tier` | NUMBER | line 79 |
| `s 2(1) — the year that contains a date`, `s 2(1) — the first day of a year`, `s 2(1) — the last day of a year` | date; year; year | NUMBER; DATE; DATE | line 80 |
| `s 2(1) — the balance-due day of a person for a year` | year, MAYBE DATE (date of death; NOTHING if living) | DATE | lines 22 to 24 |
| `s 2(1) — a common-law partner of a contributor at a relevant time` | BOOLEAN (cohabiting then), DATE (day the continuous cohabitation began), DATE (relevant time) | BOOLEAN | line 31 |
| `s 2(1) — a common-law partner of a contributor at the contributor's death` | BOOLEAN (cohabiting at the death), DATE (began), DATE (date of death) | BOOLEAN | line 31 |
| `s 2(1) — prescribed` | `Kind of matter that may be prescribed`, BOOLEAN (Minister authorized), BOOLEAN (prescribed by regulation), BOOLEAN (by prescribed rules) | BOOLEAN | lines 57 to 59 |
| `s 2(1) — a Social Insurance Number`, `s 2(1) — a Social Insurance Number Card` | BOOLEAN | BOOLEAN | line 73 |
| `s 3(1) — the date that divides paragraph (a) from paragraph (b)` | none | DATE, 3 May 1965 | lines 93, 94 |
| `s 3(1) — a province providing a comprehensive pension plan` | BOOLEAN (prescribed), MAYBE DATE (intention signified), MAYBE DATE (written notice given), NUMBER (year contributions begin), BOOLEAN (benefits comparable), BOOLEAN (obligations assumed) | BOOLEAN | lines 91 to 96 |
| `s 3(1) — a provincial pension plan` | BOOLEAN, BOOLEAN | BOOLEAN | line 97 |
| `s 3(2) — the last day by which the legislature must have provided by law` | DATE (written notice given) | DATE | line 99 |
| `s 3(2) — the Governor in Council must prescribe the province` | DATE (notice), MAYBE DATE (law made), BOOLEAN (law provides for plan and assumption) | BOOLEAN | line 99 |
| `s 3(3) — the day a regulation under subsection (2) becomes effective` | DATE (notice) | DATE | line 101 |
| `s 4(1)(a) — the Act's provisions on employee and employer contributions reach the employment` | BOOLEAN (in a province with a plan), BOOLEAN (subsection (2) treats it as employment elsewhere) | BOOLEAN | lines 103, 104 |
| `s 4(1)(b) — the Act's provisions on self-employed contributions reach the person for the year` | MAYBE `Province` (where resident on the day s 4(5) fixes) | BOOLEAN | line 105 |
| `s 4(2) — the employment is described in subsection (2)` | BOOLEAN (in a province with a plan), BOOLEAN (Crown or its agent), BOOLEAN (plan outside the province's authority) | BOOLEAN | lines 107 to 110 |
| `s 4(3) — the employment is subject to the provincial pension plan under an agreement` | BOOLEAN (described in (2)), BOOLEAN (agreement in force) | BOOLEAN | line 112 |
| `s 4(2) — the Act applies to the employment as though it were employment in another province` | BOOLEAN (described in (2)), BOOLEAN (agreement in force) | BOOLEAN | lines 107, 110 |
| `s 4(4) — the province in which a person is deemed employed` | MAYBE `Province` (where he reports for work; NOTHING if not required to), `Province` (where the paying establishment is) | `Province` | line 114 |
| `s 4(5) — the day taken as the last day of a year for paragraph (1)(b)` | year, MAYBE DATE (last day in the year he resided in Canada; NOTHING if he did not reside in Canada in the year) | DATE | line 116 |
| `s 4.1 — this section permits the Minister to use electronic means` | `Minister`, BOOLEAN (under this Act) | BOOLEAN; FALSE means the section gives no permission, not that use is forbidden | line 120 |

Three private helpers carry the prefix too: `s 2(1) — the subsection of section 8 for a tier`, the same for section 9 and for section 10.

## Naming conventions

- **A rule** is named `s N(x) — what it decides`, with an em dash, for the Act; use `reg N(x) — what it decides` for the Regulations.
  The section number makes the name unique across pieces because the pieces own different sections; do not leave it off.
  A rule that no provision states (a helper) carries no prefix and says "none" in its comment.
- **A BOOLEAN rule** is named as the proposition it decides ("the employment is described in subsection (2)"); a NUMBER, DATE or STRING rule is named as the thing it returns ("the balance-due day of a person for a year").
  Phrase it from the individual's side wherever the provision allows ("the Act reaches the employment", not "the provision does not apply").
- **An input** (a `GIVEN` name) is the fact in the provision's own words, affirmative, in backticks, with no leading `is` or `has` (the genitive supplies the verb; Meng's ruling of 2026-09-13).
  A plain fact is a BOOLEAN named as the statement ("`the employment is in a province providing a comprehensive pension plan`").
- **A field** of a record starts at the complement too: `` `name of the province` ``, not `` `has a name` ``.
- **An enumeration constructor** is a lower-case phrase with its article, in backticks: `` `a retirement pension` ``, `` `the base tier` ``.
  A type name is a capitalised phrase: `Tier`, `Kind of benefit`.
  A constructor is global, so a generic one (`a child`, `the employer`) is likely to clash with another piece; add the noun that makes it specific.
- **Money** is a NUMBER of Canadian dollars, with cents as decimals; there is no currency type.
- **A rate or percentage** is a NUMBER that is a fraction: write `5.95%` and the value is 0.0595.
  A rate in the text as "4.95 per cent" is written `4.95%`.
- **A year** is a NUMBER, the calendar year (section 2(1) "year"): 2026.
- **An age** is a NUMBER of whole years, tested only through the section 2(2) rules (see the instructions).
- **A count of months or days** is a NUMBER.
- **A month** is the DATE of its first day, written `YMD y m 1`; `the month of a date` finds it.
  Never build a month by subtracting from a month number: `Date 1 0 2026` is 1 January 2026, not December 2025.
- **A date** is a DATE written `YMD year month day`.
- **A time limit** is a `Time limit` (days, months or years); `the date a time limit ends` and `the date a time limit before a date goes back to` turn one and a date into a date.
  "N days after d" is d plus N days; "N months after d" is `add months`, which clamps to the last day of a shorter month (fork F1).
- **Not covered** is `NOTHING` or an explicit constructor, asserted in a test; never `FALSE` or `0` as a default.
- **A fact the piece does not decide** (the value of another section) is a plain input named `the <defined term>` in the Act's spelling, with the unit where the type does not say it: the table under "Defined terms" gives the name and type of each.
  A section that returns a figure for a year is called with that year's value; a piece that needs several years takes a list of its own.
- **A rule that is the same in all three tiers** takes a `Tier`; a rule that differs by tier is written once for each tier, and the name says which (`the base tier`, `the first additional tier`, `the second additional tier`).
- **A type your piece declares** that is not a term the Act or Regulations define in your range gets your piece code as its first word (`cp3 Earnings record`); constructors are phrased fully enough not to repeat anything in the Vocabulary tables.
- **Quotations and citations** follow `encoding-a-subject/references/source-locators.md`: quote lines `-- src:N | text` made by `srcrefs.py quote`, and `@ref Act s 12(1) (src:N-M)` or `@ref Reg 12(1) (src:N-M)` directly above the declaration.
- **Tests** live in `cpp-<piece>-tests-<topic>.l4` with hand-written expected values and one assertion to a line.

## Defined terms

Section 2(1) has 61 entries defining 63 terms (line 52 defines "office" and "officer", line 73 defines "Social Insurance Number" and "Social Insurance Number Card"), one row each below.
Of the 63: 23 are encoded here (rules in `cpp-core-definitions.l4`, or the core record), 33 only point to a section that another piece encodes, 2 are inert ("Consumer Price Index" and "deduct") and 5 are repealed.
"By reference" means the term has the meaning of a section in another piece's range; the piece named encodes that section, and any other piece takes the value as an input of the name and type in the last column.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| "additional maximum pensionable earnings" | s 2(1), line 16 | by reference: encoded by piece cp1, s 17.1, taken there as an input | input `the additional maximum pensionable earnings`, NUMBER, dollars, for the year at hand |
| "applicant" | s 2(1), line 17 | `cpp-core-definitions.l4`: `s 2(1) — an applicant, in Part II` | three limbs (a), (b), (c); defined for Part II only, so there is no Part input |
| "average monthly pensionable earnings" | s 2(1), line 21 | by reference: encoded by piece cp3, s 47 or s 48, taken there as an input | input `the average monthly pensionable earnings`, NUMBER, dollars a month |
| "balance-due day" | s 2(1), line 22 | `cpp-core-definitions.l4`: `s 2(1) — the balance-due day of a person for a year` | death from 1 November to 30 April: six months after the death (fork F1); any other case: 30 April of the following year |
| "base contribution" | s 2(1), line 25 | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the base tier` is the type that carries it; subsections 8(1), 9(1), 10(1) |
| "base unadjusted pensionable earnings" | s 2(1), line 26 | by reference: encoded by piece cp3, s 53, taken there as an input | field `base unadjusted pensionable earnings` of the core record `Unadjusted pensionable earnings`, NUMBER, dollars |
| "basic exemption" | s 2(1), line 27 | by reference: encoded by piece cp1, s 19, taken there as an input | input `the basic exemption`, NUMBER, dollars |
| "beneficiary" | s 2(1), line 28 | `cpp-core-definitions.l4`: `s 2(1) — a beneficiary` | one condition: a benefit has become payable |
| "benefit" | s 2(1), line 29 | `cpp-core-definitions.l4`: `s 2(1) — a benefit`; the eight kinds are the core enumeration `Kind of benefit` | the eight kinds come from s 44(1)(a) to (h), which cp3 encodes |
| "business" | s 2(1), line 30 | `cpp-core-definitions.l4`: `s 2(1) — a business` | MAYBE BOOLEAN: NOTHING for an activity the list does not decide (fork F4) |
| "common-law partner" | s 2(1), line 31 | `cpp-core-definitions.l4`: `s 2(1) — a common-law partner of a contributor at a relevant time`, `s 2(1) — a common-law partner of a contributor at the contributor's death` | one year of continuous cohabitation (fork F1, F7); at a death the relevant time is the date of death |
| "Consumer Price Index" | s 2(1), line 32 | not encoded: inert (see the coverage table) | an external published series (Statistics Canada); `the Consumer Price Index`, NUMBER, an index value, supplied as an input by whoever needs it |
| "contribution" | s 2(1), line 33 | `cpp-core-definitions.l4`: `s 2(1) — a contribution` | one condition: a contribution under this Act |
| "contribution rate" | s 2(1), line 34 | by reference: encoded by piece cp1, s 11.1, taken there as an input | input `the contribution rate`, NUMBER, a fraction (5.95% is 0.0595), for a `Contributing capacity` and a year; the capacities come from this entry (core enumeration) |
| "contributor" | s 2(1), line 35 | `cpp-core-definitions.l4`: `s 2(1) — a contributor` | four ways in; the 53(1)(b)(i) amounts are taken per year as a list (fork F6) |
| "contributory period" | s 2(1), line 36 | by reference: encoded by piece cp3, s 49, taken there as an input | input `the contributory period, in months`, NUMBER, a count of months |
| "contributory salary and wages" | s 2(1), line 37 | by reference: encoded by piece cp1, s 12, taken there as an input | input `the contributory salary and wages`, NUMBER, dollars |
| "contributory self-employed earnings" | s 2(1), line 38 | by reference: encoded by piece cp1, s 13, taken there as an input | input `the contributory self-employed earnings`, NUMBER, dollars |
| "deduct" | s 2(1), line 39 | not encoded: inert (see the coverage table) | "deduct includes withhold" widens a verb; no rule can use it |
| "disabled" | s 2(1), line 40 | by reference: encoded by piece cp3, s 42 (subsection 42(2)), taken there as an input | BOOLEAN input `the contributor is disabled` |
| "employee" | s 2(1), line 41 | `cpp-core-definitions.l4`: `s 2(1) — an employee` | "includes an officer": in employment, or an officer |
| "employer" | s 2(1), line 42 | `cpp-core-definitions.l4`: `s 2(1) — an employer` | the extra limb applies only in relation to an officer |
| "employment" | s 2(1), line 43 | `cpp-core-definitions.l4`: `s 2(1) — employment` | a contract of service or apprenticeship, or the tenure of an office |
| "excepted employment" | s 2(1), line 44 | by reference: encoded by piece cp1, subsection 6(2), taken there as an input | BOOLEAN input `the employment is excepted employment` |
| "first additional contribution" | s 2(1), line 45 | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the first additional tier`; subsections 8(1.1), 9(1.1), 10(1.1) |
| "first additional contribution rate" | s 2(1), line 46 | by reference: encoded by piece cp1, s 11.2, taken there as an input | input `the first additional contribution rate`, NUMBER, a fraction |
| "first additional contributory period" | s 2(1), line 47 | by reference: encoded by piece cp3, s 49.1, taken there as an input | input `the first additional contributory period, in months`, NUMBER |
| "first additional monthly pensionable earnings" | s 2(1), line 48 | by reference: encoded by piece cp3, s 48.1, taken there as an input | input `the first additional monthly pensionable earnings`, NUMBER, dollars a month |
| "first additional unadjusted pensionable earnings" | s 2(1), line 49 | by reference: encoded by piece cp3, s 53.1, taken there as an input | field `first additional unadjusted pensionable earnings` of the core record, NUMBER, dollars |
| "maximum contributory earnings" | s 2(1), line 50 | by reference: encoded by piece cp1, s 16, taken there as an input | input `the maximum contributory earnings`, NUMBER, dollars |
| "maximum pensionable earnings" | s 2(1), line 51 | by reference: encoded by piece cp1, s 17, taken there as an input | input `the maximum pensionable earnings`, NUMBER, dollars |
| "office" | s 2(1), line 52 | `cpp-core-definitions.l4`: `s 2(1) — an office` | the listed offices are offices even without a stipend; any other position needs a fixed or ascertainable stipend |
| "officer" | s 2(1), line 52 | `cpp-core-definitions.l4`: `s 2(1) — an officer` | a person holding such an office; line 52 defines both terms |
| "pension" | s 2(1), line 53 | `cpp-core-definitions.l4`: `s 2(1) — a pension` | one condition: a pension payable under this Act |
| "Pension Appeals Board" | s 2(1), line 54 | not encoded: repealed in this text | [Repealed, 2012, c. 19, s. 225] |
| "Pension Index" | s 2(1), line 55 | by reference: encoded by piece cp3, s 43, taken there as an input | input `the Pension Index`, NUMBER |
| "pensionable employment" | s 2(1), line 56 | by reference: encoded by piece cp1, subsection 6(1), taken there as an input | BOOLEAN input `the employment is pensionable employment` |
| "prescribed" | s 2(1), line 57 | `cpp-core-definitions.l4`: `s 2(1) — prescribed` | form or information on a form: only the Minister's authorization counts; anything else: a regulation or rules prescribed by regulation |
| "Record of Earnings" | s 2(1), line 60 | by reference: encoded by piece cp6, s 95, taken there as an input | a person's unadjusted pensionable earnings by year; there is no single input, so each piece that needs it declares its own list of the core record `Unadjusted pensionable earnings` |
| "representative" | s 2(1), line 61 | `cpp-core-definitions.l4`: `s 2(1) — a representative of a person` | the enumeration `Kind of representative` lists the capacities |
| "Review Committee" | s 2(1), line 62 | not encoded: repealed in this text | [Repealed, R.S., 1985, c. 30 (2nd Supp.), s. 1] |
| "Review Tribunal" | s 2(1), line 63 | not encoded: repealed in this text | [Repealed, 2012, c. 19, s. 225] |
| "salary and wages on which a base contribution has been made" | s 2(1), line 64 | by reference: encoded by piece cp1, s 15, taken there as an input | input `the salary and wages on which a base contribution has been made`, NUMBER, dollars |
| "salary and wages on which a first additional contribution has been made" | s 2(1), line 65 | by reference: encoded by piece cp1, s 15.1, taken there as an input | input `the salary and wages on which a first additional contribution has been made`, NUMBER, dollars |
| "salary and wages on which a second additional contribution has been made" | s 2(1), line 66 | by reference: encoded by piece cp1, s 15.2, taken there as an input | input `the salary and wages on which a second additional contribution has been made`, NUMBER, dollars |
| "second additional contribution" | s 2(1), line 67 | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the second additional tier`; subsections 8(1.2), 9(1.2), 10(1.2) |
| "second additional contribution rate" | s 2(1), line 68 | by reference: encoded by piece cp1, s 11.2, taken there as an input | input `the second additional contribution rate`, NUMBER, a fraction |
| "second additional contributory period" | s 2(1), line 69 | by reference: encoded by piece cp3, s 49.2, taken there as an input | input `the second additional contributory period, in months`, NUMBER |
| "second additional monthly pensionable earnings" | s 2(1), line 70 | by reference: encoded by piece cp3, s 48.2, taken there as an input | input `the second additional monthly pensionable earnings`, NUMBER, dollars a month |
| "second additional unadjusted pensionable earnings" | s 2(1), line 71 | by reference: encoded by piece cp3, s 53.2, taken there as an input | field `second additional unadjusted pensionable earnings` of the core record, NUMBER, dollars |
| "self-employed earnings" | s 2(1), line 72 | by reference: encoded by piece cp1, s 14, taken there as an input | input `the self-employed earnings`, NUMBER, dollars |
| "Social Insurance Number" | s 2(1), line 73 | `cpp-core-definitions.l4`: `s 2(1) — a Social Insurance Number` | one condition: assigned under an Act of Parliament; line 73 defines both terms |
| "Social Insurance Number Card" | s 2(1), line 73 | `cpp-core-definitions.l4`: `s 2(1) — a Social Insurance Number Card` | one condition: issued under that authority |
| "spouse" | s 2(1), line 74 | not encoded: repealed in this text | [Repealed, 2000, c. 12, s. 42] |
| "total first additional pensionable earnings" | s 2(1), line 75 | by reference: encoded by piece cp3, s 50.1, taken there as an input | input `the total first additional pensionable earnings`, NUMBER, dollars |
| "total pensionable earnings" | s 2(1), line 76 | by reference: encoded by piece cp3, s 50, taken there as an input | input `the total pensionable earnings`, NUMBER, dollars |
| "total pensionable earnings of a contributor attributable to base contributions made under this Act" | s 2(1), line 77 | not encoded: repealed in this text | [Repealed, 2018, c. 12, s. 361] |
| "total second additional pensionable earnings" | s 2(1), line 78 | by reference: encoded by piece cp3, s 50.2, taken there as an input | input `the total second additional pensionable earnings`, NUMBER, dollars |
| "unadjusted pensionable earnings" | s 2(1), line 79 | `cpp-core-definitions.l4`: core record `Unadjusted pensionable earnings`; `s 2(1) — the unadjusted pensionable earnings of a tier` | the collective noun for the three amounts; the record keeps them together and the rule picks one by tier |
| "year" | s 2(1), line 80 | `cpp-core-definitions.l4`: `s 2(1) — the year that contains a date`, `s 2(1) — the first day of a year`, `s 2(1) — the last day of a year` | a calendar year: 1 January to 31 December |
| "Year's Additional Maximum Pensionable Earnings" | s 2(1), line 81 | by reference: encoded by piece cp1, s 18.1, taken there as an input | input `the Year's Additional Maximum Pensionable Earnings`, NUMBER, dollars |
| "Year's Basic Exemption" | s 2(1), line 82 | by reference: encoded by piece cp1, s 20, taken there as an input | input `the Year's Basic Exemption`, NUMBER, dollars |
| "Year's Maximum Pensionable Earnings" | s 2(1), line 83 | by reference: encoded by piece cp1, s 18, taken there as an input | input `the Year's Maximum Pensionable Earnings`, NUMBER, dollars |
| "province providing a comprehensive pension plan" | s 3(1), lines 92 to 96 | `cpp-core-application.l4`: `s 3(1) — a province providing a comprehensive pension plan`; the core record `Province` | the status comes from a regulation that is not deposited, so a caller normally supplies the flag (fork F3) |
| "provincial pension plan" | s 3(1), line 97 | `cpp-core-application.l4`: `s 3(1) — a provincial pension plan` | two conditions |

Terms defined elsewhere in the Act (none is encoded here; each is named so the piece that owns it is known):

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| "Minister" (Part I) | s 5(1), line 124 | by reference: encoded by piece cp1, section 5(1), taken there as an input | the core enumeration `Minister` has `the Minister of National Revenue` |
| "authorized person", "documents", "dwelling-house", "judge" | s 25(1), lines 681 to 686 | by reference: encoded by piece cp2, section 25(1), taken there as an input | search and seizure vocabulary |
| "basic number of contributory months", "child", "decision-making responsibility", "dependent child", "disabled contributor's child", "family allowance recipient", "Maximum Pensionable Earnings Average", "Minister" (Part II), "orphan", "parenting time", "substantially gainful", "surviving spouse with dependent children" [Repealed], "survivor", "survivor with dependent children", "wholly or substantially" | s 42(1), lines 926 to 954 | by reference: encoded by piece cp3, section 42(1), taken there as an input | "decision-making responsibility" has the meaning in the Divorce Act, not deposited; "substantially gainful" and "wholly or substantially" have the meaning that may be prescribed; "survivor" turns on "common-law partner", for which `s 2(1) — a common-law partner of a contributor at the contributor's death` is the rule; the core enumeration `Minister` has `the Minister of Employment and Social Development` |
| "disabled" (when a person is deemed disabled) | s 42(2), lines 955 to 960 | by reference: encoded by piece cp3, section 42(2), taken there as an input | see the s 2(1) row for "disabled" |
| "first additional joint contributory period", "joint contributory period", "period of cohabitation", "second additional joint contributory period" | s 65.1(8), lines 2149 to 2166 | by reference: encoded by piece cp4, section 65.1(8), taken there as an input | "period of cohabitation" has the prescribed meaning (the Regulations, cr2) |
| "parent" (reciprocal meaning to "child") | s 74(3.1), line 2388 | by reference: encoded by piece cp5, section 74(3.1), taken there as an input |  |
| "document", "dwelling-house", "judge" | s 90.2(1), lines 2589 to 2593 | by reference: encoded by piece cp5, section 90.2(1), taken there as an input |  |
| "additional Canada Pension Plan", "base Canada Pension Plan", "Investment Board", "Minister" (Part III) | s 91, lines 2633 to 2636 | by reference: encoded by piece cp6, section 91, taken there as an input |  |
| "administration", "federal institution", "public officer" | s 104(1), lines 2725 to 2727 | by reference: encoded by piece cp6, section 104(1), taken there as an input | "public officer" includes an individual prescribed by regulation 37(4) (cr2) |
| "included province" | s 113.1(16) line 3013 and s 114(1) line 3017 | by reference: encoded by piece cp6, section 114(1), taken there as an input | a province other than Yukon, the Northwest Territories or Nunavut, except a province providing a comprehensive pension plan; uses `Province` |
| "appropriate provincial Minister" | s 117(4), line 3084 | by reference: encoded by piece cp6, section 117(4), taken there as an input |  |
| "board of referees", "Pension Appeals Board", "Review Tribunal", "Social Security Tribunal", "umpire" | Related Provisions s 251, lines 3170 to 3174 | by reference: encoded by piece cp5, Related Provisions section 251, taken there as an input | transitional |
| "additional Canada Pension Plan", "Additional Canada Pension Plan Account", "Canada Pension Plan Account", "Minister" | Amendments Not in Force s 62, lines 3251 to 3254 | by reference: encoded by piece cp5, Amendments Not in Force section 62, taken there as an input | not in force; never merged into the rules in force |

Terms defined in the Regulations (none is encoded here):

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| "Act", "Minister" (Parts I to IV: the Minister of National Revenue; Part V: the Minister of section 42(1)), "Chairman", "Commissioner", "Vice-Chairman" [Repealed] | reg 2(1), lines 13 to 19 | by reference: encoded by piece cr1, regulation 2(1), taken there as an input | the two Ministers are the core enumeration `Minister` |
| "agriculture", "agricultural enterprise", "fishing", "forestry", "horticulture", "hunting", "international organization", "logging", "lumbering", "trapping" | reg 2(2), lines 20 to 51 | by reference: encoded by piece cr1, regulation 2(2), taken there as an input | the subsection applies "for the purposes of the Act and these Regulations", so cp1 meets these terms in paragraph 6(2)(a) of the Act (line 138) and takes them as inputs |
| "timber" | reg 2(3), line 52 | by reference: encoded by piece cr1, regulation 2(3), taken there as an input |  |
| "employee's contribution", "employer's contribution", "ordinary remuneration", "pay day", "pay period", "remuneration", "year's maximum base contribution", "year's maximum first additional contribution", "year's maximum second additional contribution", "employed on a non-continuous basis" [Repealed], "year's maximum contribution" [Repealed] | reg 3, lines 57 to 71 | by reference: encoded by piece cr1, regulation 3, taken there as an input | "remuneration" has the same meaning as "contributory salary and wages" in section 12 of the Act |
| (Part II reads Part I's words) | reg 9, line 197 | by reference: encoded by piece cr1, regulation 9, taken there as an input |  |
| "employer operating in Canada", "employment in international transportation", "establishment in Canada", "ship" | reg 15(1), lines 221 to 236 | by reference: encoded by piece cr1, regulation 15(1), taken there as an input |  |
| "an employee engaged locally outside Canada"; "place of domicile in Canada"; "agreement with the crew", "inland voyage"; "railway company"; "legislation" | reg 16(3) line 260; reg 18(3) line 271; reg 18 lines 275 to 276; reg 20(3) line 288; reg 34.1(3) line 390 | by reference: encoded by piece cr1, regulations 16, 18, 20 and 34.1, taken there as inputs |  |
| "Canada child benefit", "Child Tax Benefit" [Repealed], "Director" [Repealed], "personal representative" | reg 37(1), lines 421 to 424 | by reference: encoded by piece cr2, regulation 37(1), taken there as an input |  |
| "cost" (includes travel and living expenses) | reg 68(4) line 681 and reg 69(4) line 699 | by reference: encoded by piece cr2, regulations 68 and 69, taken there as an input |  |
| "authority", "excess payment" | reg 76(1), lines 748 to 749 | by reference: encoded by piece cr2, regulation 76(1), taken there as an input |  |
| "family allowance recipient" (extended) | reg 77(1), line 774 | by reference: encoded by piece cr2, regulation 77(1), taken there as an input | extends the Act's definition at line 939 |
| "average bank rate", "bank rate", "debt", "demand for payment", "due date" | reg 87(1), lines 860 to 870 | by reference: encoded by piece cr1, regulation 87(1), taken there as an input | "due date" is not the Act's "balance-due day" |

## Instructions to the pieces

1. **Copy the five modules** `cpp-core.l4`, `cpp-core-calendar.l4`, `cpp-core-age.l4`, `cpp-core-definitions.l4` and `cpp-core-application.l4` into your folder and import by name with backticks: ``IMPORT `cpp-core` ``.
   `IMPORT` finds only modules in the importing file's own folder.
   Do not copy the test files.
   Copy all five even if you call only one rule: the calendar module imports `cpp-core`, and the age, definitions and application modules import `cpp-core` and `cpp-core-calendar`.
   In your own files import `cpp-core` for the types and the modules whose rules you call.
2. **Every name in the five modules is taken.**
   A name defined in two imported modules cannot be used at all, so a piece that re-coins one of them breaks every later file that imports both.
   The names are the rows of the two Vocabulary tables and the rule table above, plus `YMD`.
   The generic ones a piece is most likely to re-coin are `YMD`, `the month of a date`, `the date a time limit ends`, `the actual age of a person in whole years on a date` and the type names `Tier`, `Minister`, `Province`, `Time limit`.
3. **Test an age only through section 2(2).**
   Where the Act speaks of a person reaching a specified age, call `s 2(2) — the person is treated as having reached a specified age on a date for a provision`, or the rule that returns the date, and never subtract years yourself.
   Pass the `Provision about reaching an age` constructor for the provision you are encoding when it is on the list: cp1 for `paragraph 13(1)(c)`, `paragraph 13(1)(e)`, `paragraph 13(1.2)(c)`, `paragraph 17(c)`, `paragraph 17.1(c)`, `paragraph 19(c)` and `paragraph 19(d)`; cp3 for `paragraph 44(3)(a)`; cp5 for `section 70` and `subparagraph 72(a)(iii)`.
   Pass `any other provision` for every other provision, including the ones in the Regulations.
   Periods of months follow paragraphs (a) and (b): a period ending with the age counts the month of the birthday, one commencing with the age starts the month after.
4. **A province's plan status is a supplied fact.**
   The Act names no province; whether one is "a province providing a comprehensive pension plan" turns on a regulation that is not deposited.
   Take a `Province` as an input and read its flag; do not write a province's name into a rule.
   The keel's tests use invented provinces.
5. **Take another piece's value as an input**, named and typed as in the "Defined terms" tables, and say in your own NOTES.md which section of which piece it comes from.
   Do not import another piece's module: you cannot see it.
6. **Use rule-level `GIVEN` throughout**, as the keel does.
   A section-level `GIVEN` under a `§` parsed on the build named in the brief in one probe, but the keel does not use it and a piece should not rely on it.
7. **`#EVAL` of a bare `NOTHING`** does not accept a type ascription (`(NOTHING : MAYBE NUMBER)` is a parse error); assert `rule args EQUALS NOTHING` on a typed rule instead.
8. **Cite every rule with `@ref`** and run `python3 -I srcrefs.py check --refs <raw text> <your .l4 files>`: Act modules against the Act file, Regulations modules against the Regulations file.
   The keel's calendar helpers and its two "not a provision" age helpers (`the date a person actually reaches a specified age`, `the actual age of a person in whole years on a date`) carry no `@ref` because no provision licenses them.
9. **Dates.**
   Lines 1 to 121 contain no date of enactment, assent or commencement; the keel carries none.
   A piece whose range holds a commencement rule or date carries it as a value with an `@ref`, as the brief says.
10. **Money, rates, months and years** are written as the "Naming conventions" say; a rate is a fraction (`5.95%` is 0.0595), so a rate table is written with `%` literals.

## Coverage table

One row per provision of lines 1 to 121 of the Act file: the notice, the title block, each section, each subsection that differs, and each term defined in section 2(1).
The 16 heading lines of the range (9, 10, 13, 14, 84, 89, 90, 98, 100, 102, 106, 111, 113, 115, 118, 119) each sit in the `source lines` column of a row: the marginal notes with the provision they head, the four group headings in rows of their own.
Lines 1 to 121 hold no Related Provisions and no Amendments Not in Force: those open at lines 3138 and 3298 of the Act file and belong to piece cp5.
Dispositions: `encoded` (a rule here, or by reference to the piece named); `inert` (no rule can use it; the reason is in the note); `repealed or blank in this text`; `fork` (an encoding choice recorded in the fork register).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Converter notice | 1-3 | inert | none | text added by the converter: says the file is an unofficial reproduction, gives the source URL and the currency date (2026-09-30, last amended 2024-12-17) and says historical notes, footnotes and the French version are omitted; it is not part of the Act and changes no right or duty, and its currency date is not an enactment or commencement date |
| Title | 5 | inert | none | the title "Canada Pension Plan"; a pure title |
| Citation | 6 | inert | none | "R.S.C., 1985, c. C-8"; a pure citation, with no date of enactment or assent |
| Long title | 7 | inert | none | "An Act to establish a comprehensive program of old age pensions and supplementary benefits in Canada payable to and in respect of contributors"; a statement of purpose with no operative content |
| Group heading "Short Title" | 9 | inert | none | heading only |
| s 1 (marginal note "Short title") | 10-11 | inert | none | "This Act may be cited as the Canada Pension Plan."; the short title, which gives no right or duty |
| Group heading "Interpretation" | 13 | inert | none | heading only |
| s 2(1) chapeau (marginal note "Definitions") | 14-15 | inert | none | "In this Act,": frames the definitions, each of which has its own row below |
| s 2(1) "additional maximum pensionable earnings" | 16 | encoded | by reference: cp1, s 17.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "applicant" | 17 | encoded | `cpp-core-definitions.l4`: `s 2(1) — an applicant, in Part II` | three limbs (a), (b), (c); defined for Part II only, so there is no Part input |
| s 2(1) "average monthly pensionable earnings" | 21 | encoded | by reference: cp3, s 47 or s 48 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "balance-due day" | 22 | encoded | `cpp-core-definitions.l4`: `s 2(1) — the balance-due day of a person for a year` | death from 1 November to 30 April: six months after the death (fork F1); any other case: 30 April of the following year |
| s 2(1) "base contribution" | 25 | encoded | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the base tier` is the type that carries it; subsections 8(1), 9(1), 10(1) |
| s 2(1) "base unadjusted pensionable earnings" | 26 | encoded | by reference: cp3, s 53 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "basic exemption" | 27 | encoded | by reference: cp1, s 19 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "beneficiary" | 28 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a beneficiary` | one condition: a benefit has become payable |
| s 2(1) "benefit" | 29 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a benefit`; the eight kinds are the core enumeration `Kind of benefit` | the eight kinds come from s 44(1)(a) to (h), which cp3 encodes |
| s 2(1) "business" | 30 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a business` | MAYBE BOOLEAN: NOTHING for an activity the list does not decide (fork F4) |
| s 2(1) "common-law partner" | 31 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a common-law partner of a contributor at a relevant time`, `s 2(1) — a common-law partner of a contributor at the contributor's death` | one year of continuous cohabitation (fork F1, F7); at a death the relevant time is the date of death |
| s 2(1) "Consumer Price Index" | 32 | inert | none | names the index Statistics Canada publishes under the Statistics Act; the figures are data, not law, so any piece that needs an index value takes it as an input (`the Consumer Price Index`) and nothing in the Act can be computed from this entry |
| s 2(1) "contribution" | 33 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a contribution` | one condition: a contribution under this Act |
| s 2(1) "contribution rate" | 34 | encoded | by reference: cp1, s 11.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "contributor" | 35 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a contributor` | four ways in; the 53(1)(b)(i) amounts are taken per year as a list (fork F6) |
| s 2(1) "contributory period" | 36 | encoded | by reference: cp3, s 49 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "contributory salary and wages" | 37 | encoded | by reference: cp1, s 12 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "contributory self-employed earnings" | 38 | encoded | by reference: cp1, s 13 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "deduct" | 39 | inert | none | "deduct includes withhold" widens the verb "deduct"; both words denote the same act and no rule can tell them apart, so there is nothing to compute |
| s 2(1) "disabled" | 40 | encoded | by reference: cp3, s 42 (subsection 42(2)) | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "employee" | 41 | encoded | `cpp-core-definitions.l4`: `s 2(1) — an employee` | "includes an officer": in employment, or an officer |
| s 2(1) "employer" | 42 | encoded | `cpp-core-definitions.l4`: `s 2(1) — an employer` | the extra limb applies only in relation to an officer |
| s 2(1) "employment" | 43 | encoded | `cpp-core-definitions.l4`: `s 2(1) — employment` | a contract of service or apprenticeship, or the tenure of an office |
| s 2(1) "excepted employment" | 44 | encoded | by reference: cp1, subsection 6(2) | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "first additional contribution" | 45 | encoded | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the first additional tier`; subsections 8(1.1), 9(1.1), 10(1.1) |
| s 2(1) "first additional contribution rate" | 46 | encoded | by reference: cp1, s 11.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "first additional contributory period" | 47 | encoded | by reference: cp3, s 49.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "first additional monthly pensionable earnings" | 48 | encoded | by reference: cp3, s 48.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "first additional unadjusted pensionable earnings" | 49 | encoded | by reference: cp3, s 53.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "maximum contributory earnings" | 50 | encoded | by reference: cp1, s 16 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "maximum pensionable earnings" | 51 | encoded | by reference: cp1, s 17 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "office" | 52 | encoded | `cpp-core-definitions.l4`: `s 2(1) — an office` | the listed offices are offices even without a stipend; any other position needs a fixed or ascertainable stipend |
| s 2(1) "officer" | 52 | encoded | `cpp-core-definitions.l4`: `s 2(1) — an officer` | a person holding such an office; line 52 defines both terms |
| s 2(1) "pension" | 53 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a pension` | one condition: a pension payable under this Act |
| s 2(1) "Pension Appeals Board" | 54 | repealed or blank in this text | none | [Repealed, 2012, c. 19, s. 225] |
| s 2(1) "Pension Index" | 55 | encoded | by reference: cp3, s 43 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "pensionable employment" | 56 | encoded | by reference: cp1, subsection 6(1) | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "prescribed" | 57 | encoded | `cpp-core-definitions.l4`: `s 2(1) — prescribed` | form or information on a form: only the Minister's authorization counts; anything else: a regulation or rules prescribed by regulation |
| s 2(1) "Record of Earnings" | 60 | encoded | by reference: cp6, s 95 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "representative" | 61 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a representative of a person` | the enumeration `Kind of representative` lists the capacities |
| s 2(1) "Review Committee" | 62 | repealed or blank in this text | none | [Repealed, R.S., 1985, c. 30 (2nd Supp.), s. 1] |
| s 2(1) "Review Tribunal" | 63 | repealed or blank in this text | none | [Repealed, 2012, c. 19, s. 225] |
| s 2(1) "salary and wages on which a base contribution has been made" | 64 | encoded | by reference: cp1, s 15 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "salary and wages on which a first additional contribution has been made" | 65 | encoded | by reference: cp1, s 15.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "salary and wages on which a second additional contribution has been made" | 66 | encoded | by reference: cp1, s 15.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "second additional contribution" | 67 | encoded | `cpp-core-definitions.l4`: `s 2(1) — the tier of a contribution made under a subsection`, `s 2(1) — the subsection that imposes a contribution of a tier and capacity` | the `Tier` `the second additional tier`; subsections 8(1.2), 9(1.2), 10(1.2) |
| s 2(1) "second additional contribution rate" | 68 | encoded | by reference: cp1, s 11.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "second additional contributory period" | 69 | encoded | by reference: cp3, s 49.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "second additional monthly pensionable earnings" | 70 | encoded | by reference: cp3, s 48.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "second additional unadjusted pensionable earnings" | 71 | encoded | by reference: cp3, s 53.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "self-employed earnings" | 72 | encoded | by reference: cp1, s 14 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "Social Insurance Number" | 73 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a Social Insurance Number` | one condition: assigned under an Act of Parliament; line 73 defines both terms |
| s 2(1) "Social Insurance Number Card" | 73 | encoded | `cpp-core-definitions.l4`: `s 2(1) — a Social Insurance Number Card` | one condition: issued under that authority |
| s 2(1) "spouse" | 74 | repealed or blank in this text | none | [Repealed, 2000, c. 12, s. 42] |
| s 2(1) "total first additional pensionable earnings" | 75 | encoded | by reference: cp3, s 50.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "total pensionable earnings" | 76 | encoded | by reference: cp3, s 50 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "total pensionable earnings of a contributor attributable to base contributions made under this Act" | 77 | repealed or blank in this text | none | [Repealed, 2018, c. 12, s. 361] |
| s 2(1) "total second additional pensionable earnings" | 78 | encoded | by reference: cp3, s 50.2 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "unadjusted pensionable earnings" | 79 | encoded | `cpp-core-definitions.l4`: core record `Unadjusted pensionable earnings`; `s 2(1) — the unadjusted pensionable earnings of a tier` | the collective noun for the three amounts; the record keeps them together and the rule picks one by tier |
| s 2(1) "year" | 80 | encoded | `cpp-core-definitions.l4`: `s 2(1) — the year that contains a date`, `s 2(1) — the first day of a year`, `s 2(1) — the last day of a year` | a calendar year: 1 January to 31 December |
| s 2(1) "Year's Additional Maximum Pensionable Earnings" | 81 | encoded | by reference: cp1, s 18.1 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "Year's Basic Exemption" | 82 | encoded | by reference: cp1, s 20 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(1) "Year's Maximum Pensionable Earnings" | 83 | encoded | by reference: cp1, s 18 | a definition that only points to the section named; that piece encodes the section; the input name is in the Defined terms table |
| s 2(2) rule (marginal note "When specified age deemed to be reached") | 84-85 | encoded | `cpp-core-age.l4`: `s 2(2) — the date a person is deemed to reach a specified age`, `s 2(2) — the date a person is treated as reaching a specified age for a provision`, `s 2(2) — the person is treated as having reached a specified age on a date for a provision` | the first day of the month after the month of the birthday (fork F2 for 29 February) |
| s 2(2) exceptions (the ten references) | 85 | encoded | `cpp-core-age.l4`: the enumeration `Provision about reaching an age` | paragraphs 13(1)(c), 13(1)(e), 13(1.2)(c), 17(c), 17.1(c), 19(c), 19(d), 44(3)(a), section 70, subparagraph 72(a)(iii) |
| s 2(2)(a) | 86 | encoded | `cpp-core-age.l4`: `s 2(2)(a) — a month is counted in a period of months ending with a specified age` | the month of the birthday is included |
| s 2(2)(b) | 87 | encoded | `cpp-core-age.l4`: `s 2(2)(b) — a month is counted in a period of months commencing with a specified age` | the month of the birthday is not included |
| Group heading "Application and Operation of Act" | 89 | inert | none | heading only |
| s 3(1) chapeau (marginal note "Definitions") | 90-91 | inert | none | "In this Act,": frames the two definitions below |
| s 3(1) "province providing a comprehensive pension plan", paragraphs (a) and (b)(i), (ii) | 92-96 | fork | `cpp-core-application.l4`: `s 3(1) — a province providing a comprehensive pension plan`; the core record `Province` | the rule is complete, but the status turns on a regulation that is not deposited, so a caller normally supplies the flag (fork F3) |
| s 3(1) "provincial pension plan" | 97 | encoded | `cpp-core-application.l4`: `s 3(1) — a provincial pension plan` | two conditions |
| s 3(2) (marginal note "Prescription of province after notice given") | 98-99 | encoded | `cpp-core-application.l4`: `s 3(2) — the last day by which the legislature must have provided by law`, `s 3(2) — the Governor in Council must prescribe the province` | a duty of the Governor in Council; for the individual it fixes when a province becomes one providing a plan |
| s 3(3) (marginal note "Effective date of prescription") | 100-101 | encoded | `cpp-core-application.l4`: `s 3(3) — the day a regulation under subsection (2) becomes effective` | the first day of the third year following the year of the notice |
| s 4(1) chapeau and paragraph (a) (marginal note "Application in respect of province providing comprehensive pension plan") | 102-104 | encoded | `cpp-core-application.l4`: `s 4(1)(a) — the Act's provisions on employee and employer contributions reach the employment` | "except as provided in subsection (2)" is the second input |
| s 4(1)(b) | 105 | encoded | `cpp-core-application.l4`: `s 4(1)(b) — the Act's provisions on self-employed contributions reach the person for the year` | a person resident in no province is not taken out by the paragraph (fork F8) |
| s 4(2) (marginal note "Exception") | 106-110 | fork | `cpp-core-application.l4`: `s 4(2) — the employment is described in subsection (2)`, `s 4(2) — the Act applies to the employment as though it were employment in another province` | "if and to the extent" in paragraph (b) is modelled all or nothing (fork F5) |
| s 4(3) (marginal note "Agreement with government of province providing comprehensive pension plan") | 111-112 | encoded | `cpp-core-application.l4`: `s 4(3) — the employment is subject to the provincial pension plan under an agreement` | the Ministers' power to make the agreement is not modelled; "an agreement is in force" is the input |
| s 4(4) (marginal note "Province in which person deemed employed") | 113-114 | encoded | `cpp-core-application.l4`: `s 4(4) — the province in which a person is deemed employed` | the reporting establishment first, the paying establishment if he need not report |
| s 4(5) (marginal note "Reference to last day of year") | 115-116 | encoded | `cpp-core-application.l4`: `s 4(5) — the day taken as the last day of a year for paragraph (1)(b)` |  |
| Group heading "Electronic Alternatives" | 118 | inert | none | heading only |
| s 4.1 (marginal note "Minister's power") | 119-120 | encoded | `cpp-core-application.l4`: `s 4.1 — this section permits the Minister to use electronic means` | a permission to the Minister of National Revenue, not a duty and not a prohibition (fork F9) |

Counts: 89 rows; `encoded` 69, `inert` 13, `repealed or blank in this text` 5, `fork` 2.
The 89 rows are: the notice and the three lines of the title block (4); the four group headings (4); section 1 (1); the chapeau of section 2(1) (1); the 63 terms of section 2(1) (63); section 2(2) with its exceptions and paragraphs (a) and (b) (4); section 3 with its chapeau, two definitions, subsection (2) and subsection (3) (5); section 4 with paragraphs (1)(a) and (1)(b) and subsections (2) to (5) (6); section 4.1 (1).

## Fork register

Each entry is a choice the text leaves open.
All are **assumed, not ruled**: none has been decided by Meng or by a court, and each can be reversed alone.

| id | provision | the readings | taken here | effect if the other reading is right |
| --- | --- | --- | --- | --- |
| F1 | month-end arithmetic: "6 months after the day of death" (line 23), "a continuous period of at least one year" (line 31), "twelve months before" (line 99) | (A) the result is clamped to the last day of a shorter month; (B) it rolls into the next month | A, because `add months` and `add years` in `daydate` clamp; the Interpretation Act, which would say, is not deposited | a death on 31 December gives a balance-due day of 30 June (A) or 1 July (B); one on 31 March gives 30 September (A) or 1 October (B) |
| F2 | the birthday of a person born on 29 February, in a year with no 29 February (s 2(2), line 85) | (A) 28 February; (B) 1 March | A, by `add years` | the deemed date is one month later (1 April instead of 1 March) for that person in those years |
| F3 | where the status "province providing a comprehensive pension plan" comes from (s 3(1), lines 92 to 96) | (A) a regulation prescribes the province, so the status is a supplied fact; (B) the status is derived from the facts in paragraphs (a) and (b) | both are encoded: the rule derives it from the facts, and the `Province` record carries a flag a caller sets; the prescribing regulation is not deposited | a seat layer must set the flag for each province it names, and the Act does not name one |
| F4 | "business includes ..." (s 2(1), line 30) | (A) the list is closed, so any other activity is not a business; (B) "includes" leaves the ordinary meaning open | B: an activity outside the list gives `NOTHING` | a caller treating the list as closed would read `NOTHING` as FALSE |
| F5 | "if and to the extent that" (s 4(2)(b), line 109) | (A) an employment is wholly inside or wholly outside the province's authority; (B) an employment can be split by extent | A: the caller splits an employment by extent and calls the rule for each part | a part-and-part employment is two calls instead of one |
| F6 | "a person the amount of whose earnings ... for a year ... exceeds zero" (s 2(1), line 35) | (A) any one year with an amount over zero is enough; (B) the amount must be over zero in the year in question | A: the rule takes a list of yearly amounts | a person with a zero in the year asked about but a positive year earlier is a contributor under A only |
| F7 | "a continuous period of at least one year" (s 2(1), line 31) | (A) one year is complete on the same calendar day a year later; (B) it needs one day more | A: cohabitation begun 1 March 2025 is a year on 1 March 2026 | a relevant time exactly one year after the start is not enough under B |
| F8 | "persons who on the last day of that year were resident in a province providing a comprehensive pension plan" (s 4(1)(b), line 105) | (A) a person resident in no province is not taken out; (B) paragraph (b) says nothing of them | A: `NOTHING` for the province gives TRUE (the Act's provisions reach the person) | the section 10 conditions (not in this range) then decide for such a person |
| F9 | "may use electronic means" (s 4.1, line 120) | (A) a permission modelled as a BOOLEAN that is FALSE when the section gives none; (B) a MAYBE | A, so FALSE means "this section gives no permission" | a reader may take FALSE as a prohibition, which it is not |

## What the stable binary does not accept

The binary is the one named in the brief (`l4` 1.6.98).
Each line below was run on it while writing the keel, with the message it printed; nothing is borrowed from another document.

- `REFUSE "no"`: `I could not find a definition for the identifier REFUSE`.
- `#ASSERT REFUSED rule`: `I could not find a definition for the identifier REFUSED`.
- A bare `BECAUSE "x"` after an expression: `unexpected BECAUSE`.
- `f IS A NUMBER TYPICALLY 3` on a record field: `unexpected 3`.
- A bodiless `DECLARE Opaque`: `unexpected end of input`.
- `YMD` after `IMPORT daydate`: `I could not find a definition for the identifier YMD`; `cpp-core.l4` defines it.
- `#EVAL (NOTHING : MAYBE NUMBER)`: `unexpected :`.
- An `IF ... THEN ...` / `ELSE IF ... THEN ...` chain with each `THEN` written at the indent of the first `IF` stopped at the word after the second `THEN` with `incorrect indentation (got 10, should be greater than 10)`; the keel uses `BRANCH ... OTHERWISE` instead.

Behaviours that are not errors but surprise:

- `Date 1 0 2026` evaluates to 1 January 2026, not December 2025; `Date 1 13 2026` is 1 January 2027; `Date 31 2 2026` is 3 March 2026.
- A name of more than one word must be in backticks wherever it is used, a test fixture included; `Province A` unquoted is a parse error, and ordinary L4 syntax, not a gap of this binary.
- `add months` and `add years` clamp: 31 August 2026 plus 6 months is 28 February 2027; 29 February 2024 plus 1 year is 28 February 2025.
- `add months date (0 MINUS n)` goes back n months, and `date PLUS (0 MINUS n)` goes back n days.
- A section-level `GIVEN` under a `§` parsed and evaluated on this binary in one probe (a rule over it returned 5 for the argument 4); the keel does not use it.

Accepted and used by the keel: `LIST 0, 1500` and `EMPTY` as list values, `any (GIVEN amount YIELD amount GREATER THAN 0) list`, `MAYBE` inputs with `CONSIDER ... WHEN NOTHING THEN ... WHEN JUST x THEN ...`, `CONSIDER ... OTHERWISE`, `BRANCH`, `WHERE` after a `CONSIDER`, enumerations whose constructors carry a field (`a number of days WITH number of days IS 90`), and record literals with `WITH`.

## What check.sh prints

The command was `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, run in this folder, and it printed:

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
cpp-core-age.l4                                0         0       0        0         0
cpp-core-application.l4                        0         0       0        0         0
cpp-core-calendar.l4                           0         0       0        0         0
cpp-core-definitions.l4                        0         0       0        0         0
cpp-core-tests-age.l4                          0        36       0        0         0
cpp-core-tests-application.l4                  0        54       0        0         0
cpp-core-tests-calendar.l4                     0        23       0        0         0
cpp-core-tests-definitions.l4                  0       114       0        0         0
cpp-core.l4                                    0         0       0        0         0
TOTAL (9 modules)                              0       227       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Read it by column: `errors` counts error diagnostics, `satisfied` the assertions that held, `failed` those that did not, `refused` those that could not be evaluated, and `expected` the failures a module is allowed.
The tests are the four `cpp-core-tests-*.l4` modules; the five library modules carry no assertions, so their zeros mean they compile and say nothing about their behaviour.
Beyond `check.sh`: `python3 -I srcrefs.py check --refs` on the Act file and the nine modules reported 0 problems, and `l4 check` on each module printed no error or warning and none of the `@ref` placement warnings ("is at the end of the file", "follows code on its line").
A short throwaway file that imported all five modules and called a rule from the calendar, age, definitions and application modules (four assertions, all satisfied) was run and deleted.

