# PROGRESS (euca encoding)

Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Status (all written, all run)

1. `euca-nouns.l4` types only (DECLARE and nothing else). Written, `l4 run` clean.
2. `euca-shared.l4` dates the Act states (ISO comment, @ref) and arithmetic helpers (defined once, here only). Written, clean.
3. `euca-s207-dates.l4` s 207 date gates. Written, clean.
4. `euca-s202-work-test.l4` s 202(a)(3). Written, clean.
5. `euca-s202-conditions.l4` s 202(a)(1), (2), (4), (5), (6), (7). Written, clean.
6. `euca-s203-period.l4` s 203(a), (b), (c) and the period-from-readings engine. Written, clean.
7. `euca-s203-indicators.l4` s 203(d), (e), (f). Written, clean.
8. `euca-s202-account.l4` s 202(b), (c). Written, clean.
9. `euca-s202-payable.l4` master rule over the above. Written, clean.
10. `euca-s204-payments.l4` s 204. Written, clean.
11. `euca-s205-definitions.l4` s 205. Written, clean.
12. `euca-s208-sea.l4` s 208. Written, clean.
13. Layer-1 tests: `euca-tests-period.l4` (50), `euca-tests-indicators.l4` (46), `euca-tests-eligibility.l4` (113), `euca-tests-account.l4` (37), `euca-tests-payments.l4` (99). All satisfied.
14. Layer 2: `euca-seat.l4` (38 questions, each @export and @desc) and `euca-cases-seat.l4` (111 assertions, all satisfied).
15. `NOTES.md` complete: all nine headings, 37 jural rows, 99 coverage rows (54 encoded, 30 fork, 15 inert), 38 forks, 28 dependencies, 25 findings.

s 201 and s 206 have no module: both are `inert` rows (pure citation; amendment of another instrument).

## Last gate

`L4=<stable l4> L4_TARGET=unstable ./check.sh`: 19 modules, 0 errors, 456 satisfied, 0 failed, 0 refused; assertions written 456.
`python3 -I srcrefs.py check --refs <text> euca-*.l4` and `--strict`: 0 problems.
Mutation check (six one-figure changes in six modules) made tests fail; all restored byte for byte.

## Quote convention

Quote lines `-- src:N | text` were produced from the raw file by an inline Python expander that reads marker lines `--@ N`, `--@ N-M` or `--@ N | start | end` and replaces them. After expansion the markers are gone.

## Dialect notes learned

- Genitive arguments to a prefix call must be parenthesised: `f (r's x)`, not `f r's x`.
- A comparison operator at the start of a continuation line must be indented deeper than the first operand's line (or put the operator at the end of the previous line).
- `LIST` of record constructions: parenthesise each element.
- Multi-line argument lists inside a THEN branch broke the parser; use WHERE locals.
- A `CONSIDER ... WHEN` cannot be written on one line in an `#ASSERT`; name it in a rule.

## Not done / left to others

- No independent test pass; expected values are the author's, hand-written from the text.
- The deposit's check.sh was not run with the main target (no fetch-main-l4.sh in the deposit).
