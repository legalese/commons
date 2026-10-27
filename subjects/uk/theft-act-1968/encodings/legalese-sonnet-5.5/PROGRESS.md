# PROGRESS (Theft Act 1968, legalese-sonnet-5.5)

Written first, updated as work lands. After any compaction: re-read this file, NOTES.md and the text (`../../registers/source-bundle/ukpga-1968-60.txt`), not a summary.

## Method

- One agent, working alone from `BRIEF.md`, on stable `l4` 1.6.98 (`main`, 7689b0d, 2026-10-19), sha256 82ea44ad...263e, checked against the brief.
- Dialect: `main`. No section `GIVEN`, no `REFUSE`/`REFUSED`/`BECAUSE`, no `TYPICALLY`, no `YMD` (use `Date d m y`), no sets, no opaque `DECLARE`, no `@lang` or unknown `@word`, no hierarchy library, no field opening.
- Quote lines are produced by `python3 -I srcrefs.py quote <raw text> N M` (the copy of the skill's srcrefs.py is in this folder), and `@ref ... (src:N-M)` sits above the declaration the run supports.
- Fixtures in the case files are record literals with every yes/no field `FALSE` unless the name says otherwise; expected values were written by hand from the text before the run.
- Read the diagnostics, not the exit code: per file, errors, warnings, satisfied, failed, refused, and the two `@ref` warnings (`is at the end of the file`, `follows code on its line`).

## Layer 1 modules (all in this folder, flat)

| module | sections |
|---|---|
| theft-nouns.l4 | the records, enumerations and penalty types every module reads (declarations only) |
| theft-s01-06-definition.l4 | ss 1 to 6 |
| theft-s34-interpretation.l4 | s 34 |
| theft-s07-14-offences.l4 | ss 7 to 14, including 12A |
| theft-s15-21-fraud.l4 | ss 15 to 21 (15, 15A, 15B, 16 blank) |
| theft-s22-25-goods.l4 | ss 22 to 25 |
| theft-s26-29-procedure.l4 | ss 26 to 29 |
| theft-s30-36-general.l4 | ss 30 to 36 and the dates the Act carries |
| theft-schedules.l4 | Schedule 1 paragraph 2 (Schedules 2 and 3 are inert) |

Case files: `theft-cases-s01-06.l4`, `-s07-14`, `-s15-21` (also covers s 34(2)(a)), `-s22-25` (also covers s 34(2)(b)), `-s26-29`, `-s30-36`, `-schedules`.

## Status

- [x] layer 1, every section and Schedule 1 paragraph 2 encoded or entered in the coverage table
- [x] layer 1 case files, all assertions satisfied (567)
- [x] seat layer: `theft-seat.l4` (78 exported questions) and `theft-cases-seat.l4` (371 assertions, all satisfied)
- [x] `encoding.json`, `SOURCE-LICENSE.md`, final `NOTES.md` (Seat, Jural relations, forks 1 to 36, findings 1 to 20, what the binary does not accept, what `check.sh` prints, before relying)
- [x] final checks: `check.sh` 18 modules, 0 errors, 938 satisfied, 0 failed, 0 refused; per-module warnings 0; `srcrefs.py check --refs --strict` 0 problems
- [ ] after hand-over: nothing owed by this run; the only open item is a domain expert's read against the official text

## Files written (all in this folder, flat)

`theft-nouns.l4`, `theft-s01-06-definition.l4`, `theft-s34-interpretation.l4`, `theft-s07-14-offences.l4`, `theft-s15-21-fraud.l4`, `theft-s22-25-goods.l4`, `theft-s26-29-procedure.l4`, `theft-s30-36-general.l4`, `theft-schedules.l4`, `theft-seat.l4`, the eight `theft-cases-*.l4` files, `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, and copies of `check.sh`, `srcrefs.py` and `BRIEF.md`.

## Decisions of note (see NOTES.md fork register)

- s 2 defines "dishonestly" for s 1 only (s 1(3)); in ss 13, 17, 20, 22, 24A it is a stated fact.
- Penalties are the greatest the section states, kept as a ceiling record; fines are a level on the standard scale and no sum is supplied.
- `Outcome of a charge` has three values: no offence, an offence with the stated penalty, an offence for which the text states no penalty (the not-covered value).
- `NOT (a) OR b` on one line parses as `NOT ((a) OR b)` on the stable binary; written `(NOT (a)) OR b`.
