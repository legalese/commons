# Encodings of the Refrigeration or Air-Conditioning Work Licensing Law 5785-2025

This directory holds several encodings of the same law side by side.
Rows are equal and canon ranks none of them (`docs/directory-conventions.md`).
This page says who made each row, how, and what it covers, so that nobody compares two rows that answer different questions.
Last checked 2026-10-13.

| row | made by | how | covers | tests |
| --- | --- | --- | --- | --- |
| [`legalese`](legalese/) | Legalese | built from 2026-09-21 in a Claude Fable 5.1 session with Meng Wong (later revisions may involve other models); the reference row for the THERMOSTAT comparison | ss.2, 3, 6 with the whole Second Schedule, 7, 8, 9, 16, 17, 63 of the Law, and the Fees Regulations in three vintages (the SimpLEX draft, as made, as amended) | its own `check.sh`: five modules, one of them meant to fail on exactly 3 assertions |
| [`legalese-he`](legalese-he/) | Legalese | **generated**, not encoded: `source/revoice.py` re-voices the five modules of `legalese` into Hebrew-canonical L4 using `glossary.json` | the same as `legalese`, rule for rule | its `check.sh` compares its answers with `legalese` module by module |
| [`legalese-sonnet-5.5`](legalese-sonnet-5.5/) | Legalese | one Claude Sonnet 5.5 agent working alone in a cleanroom from THERMOSTAT's brief (`BRIEF.md`), 2026-10-13; no independent test pass | the same scope as `legalese`; its law modules are generated from `build/src/*.l4.in` | its `check.sh`: 281 assertions satisfied, and `hvac-tests-red.l4` fails on exactly 7 by design (re-run by the launching session) |
| [`legalese-opus-5.5`](legalese-opus-5.5/) | Legalese | one Claude Opus 5.5 agent working alone in a cleanroom from the same brief, binary and effort as `legalese-sonnet-5.5`, 2026-10-13; no independent test pass | the same scope as `legalese` | its `check.sh`: 202 assertions satisfied, and `tests-simplex-red.l4` fails on exactly 2 by design (re-run by the launching session) |
| [`legalese-michael`](legalese-michael/) | an external contribution (`michaellegalese`, committed 2026-09-22) | made with ChatGPT, without Legalese's `encoding-a-subject` skill or pipeline | the whole Law: all 63 sections and the four schedules, as one module with Hebrew comments; **not** the Fees Regulations | `tests.l4` (107 assertions) and `traces.l4` (6 traces), written by the run that wrote the code |

## Reading the table

**The rows do not all cover the same ground.**
`legalese-michael` covers more of the Law (all 63 sections; the sanctions chapter, the First Schedule works, the register, the council and inspection provisions) and none of the fee regulations.
`legalese`, `legalese-he`, `legalese-sonnet-5.5` and `legalese-opus-5.5` cover nine sections and the fee regulations in three vintages, and can run the SimpLEX scenarios from Figure 4 of Schwartz, Bar-Siman-Tov & Gelbard (2025); `legalese-michael` cannot.
Compare rows by what they answer on the same scenario, never by their text or by their assertion counts.

**`legalese-he` is not an independent encoding.**
If `legalese` changes, `legalese-he` must be regenerated; its `check.sh` fails when the two disagree.

**`legalese-michael` is unreviewed, and has one known defect.**
Its Fourth Schedule list has 91 refrigerants where the gazette and the current Hebrew Wikisource list 95 (488A, 489A, 490A and 491A are missing), so its refrigerant lookup answers FALSE for those four.
Its `encoding.json` records this and the review that found it.
No row has a recorded review by a domain expert: gate HG1 is "not sought" on `legalese` and `legalese-he`, and none is recorded for `legalese-michael`.

## Running them

```sh
sh legalese/check.sh        # needs an l4 at least as new as the rows; see the script
sh legalese-he/check.sh
cd legalese-michael && l4 check hvac-act.l4 && l4 run tests.l4 && l4 run traces.l4
```

Leave `JL4_LIBRARY_PATH` unset.
On an `l4` built on 2026-10-13, `legalese-michael` type-checks with no errors and all 107 of its assertions pass; it prints 82 warnings, every one the notice that `EXACTLY` is being retired.
