# PROGRESS -- dg-g0, the keel for the Delaware General Corporation Law (8 Del. C. ch. 1)

Kept current as the work goes.
If context is compacted, re-read this file, `NOTES.md` and the text, not a summary.

## Status

- [x] Read the brief, `SOURCES.md`, `STUB-SOURCE-LICENSE.md`, `SECTION-INDEX.txt`, the Commons guide copies, the example seat layer, both skills, `dialects.md`, `drafting-patterns.md`, `source-locators.md` and the source-pattern pages that bear on definitions, parties, quantities, dates and non-rules.
- [x] Confirmed the binary: `1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44ad...263e` as named in the brief.
- [x] Measured the dialect on this binary: all 58 numbered probes are rejected, all 23 `alt-*` probes check clean, `YMD` is missing.
- [x] Surveyed the text: headings, definitional sentences (111 rows of defined terms), periods (days, weeks, months, years), amounts (dollars), proportions, vote thresholds, cross-piece citations (counted per piece), outside statutes, dates, heading notes.
- [x] Chose the vocabulary and took the advisor's review of the plan; after the review of the finished work, added `a natural person` to `Kind of entity` (three definitions of "person" begin "any individual"), a quorum sentence to the instructions, the scope kind to every defined-term row, and sentence-per-line instructions.
- [x] Wrote `dg-core.l4` (10 types, 56 constructors, 17 rules) with `@ref` and `src:` quote lines; `l4 check` clean; `srcrefs.py check --refs`: 0 problems.
- [x] Wrote `dg-core-tests-core.l4`: 87 assertions, all satisfied; expected values written by hand from the text; checked that a wrong expectation does fail.
- [x] Ran `check.sh` (`L4_TARGET=unstable`): 0 errors, 0 failed, 0 refused.
- [x] Throwaway import test (a three-line file importing `dg-core` and calling `the date ... after` and `the vote carries`): ran, then deleted.
- [x] Wrote `NOTES.md` under the eight required headings. The Vocabulary table is generated from `dg-core.l4` and checked against it, so no type or constructor is missing; the Defined terms table has 111 rows, each opening with the text's own words copied mechanically.
- [x] Deleted the scratch folder under DEPOSIT (`scratch-keel`, made while working) and ran the final `check.sh`.
- [ ] Final report: only the report remains.

## Decisions taken, and the section that licenses each

| decision | licensed by |
| --- | --- |
| The keel has no range, so no `dg-core-<topic>.l4` interpretation module and a coverage table with one explanatory row | brief; the Law has no interpretation section |
| `Period` (a number of calendar days, weeks, months or years) is the one way to write a time limit; dates are made with a `YMD` shim defined once in the core | sections 213(a), 164, 371(b)(1), 212(b) use days, weeks, months and years |
| Money is a bare NUMBER in US dollars; a proportion is an exact NUMBER, a fraction of 1 | sections 391 (dollar amounts), 203(a)(3) ("66 2/3%"), 216 ("1/3") |
| `Kind of corporation`: a stock corporation, or one of three nonstock kinds | 114(d)(1) to (4) |
| `Where an entity is formed`, `Kind of entity` and `Entity` | 371(a), 388(a)(1), 388(a)(2), 265(a), 203(c)(6), 254(a) |
| `Actor`: the 18 parties that two or more pieces name, and an escape for the rest | 107, 124(3), 132(a), 141(a), 142(a), 145(a), 165, 211(a)(2), 212(b), 226(a), 231(a), 279, 291, 103(a), 114(a)(1) |
| `Where a provision is made`: the certificate, the bylaws, a board resolution, or none of them | 141(b), 151(a), 216 |
| `Vote base`, `Vote requirement`, `a majority of`, `at least ... of` and `the vote carries` (a `MAYBE BOOLEAN`: counts that cannot be a vote are not covered) | 216, 242(b), 141(b), 141(c), 203(a)(3), 223(a), 212(a) |
| Counts are of votes, not shares | 212(a) |
| Rules are named with their section locator first, so eleven pieces cannot coin one name | the dialect: a name defined in two imported modules cannot be used |

## Finding worth passing on

The most-cited section is § 103 (85 citations, owned by dg1), then § 251 (50, dg6), § 204 (21, dg4), § 102 (20, dg1) and § 391 (18, dg11): the pieces will take the status "filed in accordance with § 103" and the amount "payable under § 391" as inputs again and again, so NOTES.md fixes one naming pattern for them.
