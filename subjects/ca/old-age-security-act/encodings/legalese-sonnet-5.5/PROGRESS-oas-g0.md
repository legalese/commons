# PROGRESS (keel agent oas-g0)

Updated as I go. If context is compacted, re-read this file, NOTES.md and the text, not a summary.

## Status (2026-10-22)

- [x] Read the brief, both skills (SKILL.md, dialects.md, drafting-patterns.md, source-patterns, source-locators.md), ENCODING-GUIDE.md, COMMONS-CLAUDE.md, the example seat layer, SOURCES.md and STUB-SOURCE-LICENSE.md.
- [x] Read my range (Act lines 13-91), the Parts and sections the definitions point to, and the Regulations' definitions and rounding sections.
- [x] `oas-core.l4`: YMD shim, Benefit, Kind of pension, Kind of allowance, Party, Calendar span, Unit of time, Time limit, Sentence of imprisonment.
- [x] `oas-core-measures.l4` + tests (60 satisfied): months, ages, time limits, rounding.
- [x] `oas-core-periods.l4` + tests (59): payment period, payment quarter, first and second adjustment quarters, Consumer Price Index.
- [x] `oas-core-terms.l4` + tests (37): applicant, beneficiary, pensioner, survivor, common-law partner, cheque, release, Part of each benefit.
- [x] `oas-core-pension.l4` + tests (31): specially qualified individual, special qualifying factor, s 2.1.
- [x] `oas-core-income.l4` + tests (42): income, paragraph by paragraph.
- [x] `NOTES.md` with the eight required headings.
- [x] check.sh: 0 errors, 229 satisfied, 0 failed, 0 refused (11 modules). srcrefs: 0 problems. Import smoke tests: all six modules and all six together.
- [x] Last pass: scratch folder deleted (every module was rebuilt from its template first and was identical), every check re-run on the final files, final report.

## Decisions taken (with the section that licenses each)

- A month is the DATE of its first day (s 2 "payment period", "payment quarter"; the Act pays by the month).
- Money is a NUMBER of dollars, a percentage a fraction (`0.6%` is 0.006; s 7.1(1)), a time limit a `Time limit` record (convention; the text's limits are in days, months and years: ss 27.1(1), 11(7)(a), 29(1)).
- Payment period (a) "fiscal year": April to March, inferred from (b) beginning on April 1, 1998 (fork F2).
- Consumer Price Index: unrounded mean of the three monthly figures; the Regulations s 9(2) rounding is oa3's (fork F10).
- s 2.1: three rules that answer with the amount before any increase under 7.1(1) or (2); the increased amount is an input that makes no difference (fork F8).
- Specially qualified individual: the ten-year test uses the aggregate as of the last day of the immediately preceding month (fork F4).
- Common-law partner: the anniversary day counts as one year, and the relevant time of a living individual is the day the question is asked (fork F6).
- Release: "that has not been terminated or revoked" qualifies both parole and statutory release (fork F7).
- Age: attained on the anniversary of the birth; a 29 February birth is 28 February in a non-leap year (fork F5).
- "income" (a)(i) gives no amount after June 2020: NOTHING, then 0 in the paragraph (a) sum (fork F3); (b.1) reading F1; negative income not floored (F11).
- "spouse" is repealed and undefined: a plain fact (F9).
- Pieces label every name they declare with the section label; the keel's names carry none; the keel defines `YMD`, so no piece may.

## Facts checked while writing (the cheapest check that could falsify each)

- Imports are transitive, and a second `YMD` in a file that imports `oas-core` fails with "multiple definitions" (probe, deleted).
- Section-labelled names (`s 12(2): ...`) work for a type, a constructor and a rule (probe, deleted).
- `0.6%` equals 0.006 (probe).
- Every Party constructor's provenance comment was checked against the text by grep and section lookup, and four citations that were wrong or unverified were corrected (sponsor, representative, Federal Court, spouse or common-law partner).
- The Act's related provisions and amendments not in force (lines 1146-1239) amend nothing in ss 2, 2.1, 2.2.
