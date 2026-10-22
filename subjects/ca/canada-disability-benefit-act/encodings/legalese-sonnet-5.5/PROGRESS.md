# PROGRESS (run porridge-ca-cdba-b, Sonnet 5.5, solo)

Disk is the memory. After any compaction re-read this file, NOTES.md and the text (INPUTS_DIR), not a summary.
The numbers (assertions satisfied per file, coverage counts) are in NOTES.md under "What check.sh prints" and "Coverage table"; they are not repeated here so they cannot drift.

## State

All deliverables are written; the last step was the final `check.sh` run and the report.

- Layer 1: every module in the table below, each with a tests file (except `cdba-nouns.l4`, which holds types only), all clean.
- Layer 2: `cdba-seat.l4` (the seat's questions) and `cdba-cases-seat.l4` (at least one case per question, with the not-covered answers asserted).
- `NOTES.md` (seat, jural relations, coverage table, fork register, findings, stable-binary limits, check.sh output, what is needed before reliance), `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md` (copy), `check.sh`, `srcrefs.py`.

## Paths

- INPUTS_DIR = ../../registers/source-bundle
- DEPOSIT = .../porridge-ca-cdba-b/deposit ; this folder is DEPOSIT/encodings/legalese-sonnet-5.5
- L4_BIN = l4 (1.6.98, sha256 82ea44ad...263e)
- Run: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` from this folder.
- srcrefs: files `cdba-act*.l4` are checked against S.C.-2023-c.-17.txt, every other file against SOR-2025-35.txt (check.sh does both).

## Design decisions (each licensed by the section named; the fork register in NOTES.md has the arguments)

- Stable (main) dialect only: no section GIVEN, REFUSE, TYPICALLY, opaque DECLARE or sets; `YMD` defined once in cdba-calendar.l4.
- A criterion of Regs s 2(1) is met "for a month" when it holds throughout the month (F1, licensed by s 2(2) and s 2(3)).
- Exact elapsed age; 29 February attains an age on 28 February (F2, s 2(2)).
- The spouse or partner condition has nothing to bite on for a person with no partner (F7, s 6(2)); it overrides the exceptions (F4, ss 2(4), 2(6)).
- Borrowed terms are asked as facts (F6); the taxation year is the calendar year (F8).
- The basic amount payable is the formula or zero (F9, s 6(1)); s 8(2) engages for an amount above zero and not above 20, and counts the first payable month (F10).
- A suspension the beneficiary asked for does not trigger s 4(4) (F11) and voids a month only if in force throughout it (F12, s 11(2)(a)).
- Time counting: F14 (s 4(3)), F15 (calendar-unit periods include the anniversary day), F16 (s 39: ends the day before the sixth anniversary).
- Judgments of the Minister are conditional inputs; duties are tests of whether the duty has arisen and of its amount.
- Dates are data: the assent date and the order bringing the Act into force are not in the text and are inputs; Regs s 42 (15 May 2025) is a value.

## Modules

| file | covers |
|---|---|
| cdba-nouns.l4 | shared records and choices |
| cdba-calendar.l4 | YMD shim, month helpers |
| cdba-reg-definitions.l4 | Regs s 1 |
| cdba-reg-eligibility.l4 | Regs ss 2, 2.1 (s 3 inert) |
| cdba-reg-application.l4 | Regs ss 4, 5 |
| cdba-reg-amount.l4 | Regs ss 6, 6.1 |
| cdba-reg-payment.l4 | Regs ss 7 to 9.1 |
| cdba-reg-suspension.l4 | Regs ss 10, 11 |
| cdba-reg-death.l4 | Regs ss 12 to 16 |
| cdba-reg-reviews.l4 | Regs ss 17 to 19, 31 |
| cdba-reg-appeals.l4 | Regs ss 20 to 29 |
| cdba-reg-compliance.l4 | Regs ss 32, 34 |
| cdba-reg-penalties.l4 | Regs ss 35, 36 |
| cdba-reg-debts.l4 | Regs ss 37 to 40, 42 |
| cdba-act.l4 | Act ss 4 to 9, 10.1, 14 |
| cdba-seat.l4, cdba-cases-seat.l4 | layer 2 |

Each module that holds rules has a `cdba-tests-*.l4` file (calendar, reg-definitions, reg-eligibility, reg-application, reg-amount, reg-payment, reg-suspension, reg-death, reg-reviews, reg-appeals, reg-compliance, reg-penalties, reg-debts, act).

## What would be next

Nothing in the brief is outstanding. The open items are the ones in NOTES.md under "What would need doing before this encoding is worth relying on".
