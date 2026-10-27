# PROGRESS: keel cp-g0 (Canada Pension Plan Act and Regulations)

State: the five library modules, the four test modules, NOTES.md and this file are written.
Every gate named in the brief was run on the final files; the numbers are in NOTES.md under "What check.sh prints".

## Done

- Read the brief, the two skills and their references, the Commons guide, the section index, SOURCES.md, and Act lines 1 to 131, 132 to 335, 925 to 1076, with the Regulations' interpretation sections.
- `cpp-core.l4`: `YMD` shim; types `Tier`, `Contributing capacity`, `Kind of benefit`, `Minister`, `Time limit`, `Province`, `Unadjusted pensionable earnings`.
- `cpp-core-calendar.l4`: months and time limits (infrastructure; no provision licenses it, so no `@ref`).
- `cpp-core-age.l4`: section 2(2), including the enumeration of the ten excepted provisions.
- `cpp-core-definitions.l4`: the 23 terms of section 2(1) that can be worked out from facts.
- `cpp-core-application.l4`: sections 3, 4 and 4.1.
- Tests: calendar 23, age 36, definitions 114, application 54 assertions; every expected value was worked out by hand from the text or the calendar.
- NOTES.md with the eight required headings; coverage table of 89 rows covering all 16 heading lines of the range.

## Decisions and the provision that licenses each

- Three tiers as an enumeration: section 2(1) "base contribution", "first additional contribution", "second additional contribution" (lines 25, 45, 67).
- Three capacities: sections 8, 9, 10 and section 2(1) "contribution rate" (line 34).
- Eight benefits: section 44(1)(a) to (h) (lines 973 to 995); needed by cp3, cp4, cp5 and cr2.
- Two Ministers: section 5(1) (line 124), section 42(1) (line 945), section 91 (line 2636), section 4.1 (line 120).
- A month is the DATE of its first day; `Date 1 0 2026` is 1 January 2026, so no month is built by subtraction.
- A time limit is days, months or years; month arithmetic clamps (fork F1, assumed, not ruled).
- Section 2(2) is one rule over a `Provision about reaching an age` so that the ten exceptions are named once and each piece passes its own.
- Pointer definitions ("has the meaning assigned by section N") get no rule here; they are `encoded` in the coverage table by reference to the piece that owns the section, and the Defined terms table gives the input name and type.
- Repealed entries (5) are `repealed or blank in this text`; "Consumer Price Index" and "deduct" are `inert` with their reasons.
- No enactment, assent or commencement date appears in lines 1 to 121, so none is carried.

## Not done, and why

- No seat layer and no `@export`, as the brief says.
- The regulation that prescribes a province providing a comprehensive pension plan is not deposited; the province's status is a supplied fact (fork F3).
- `L4_TARGET=main` was not run: the brief asks for `L4_TARGET=unstable`, so the main-build comparison in `check.sh` was skipped.
