# Defence Forces Retirement Benefits (Pension Increases) Act 1973 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my DFRB pension increase for` (`dfrb73-rules.l4`), with `the prescribed percentage for`. It gives the increase in a DFRB pension from 5 July 1973. The encoded provisions are ss 4(2), (4), 5, 7(1)(a), (2), (4)-(5) and 12. The source is the Act as made.

**Missing formulas.** The s 4(2) formulas are images in the print. They are taken as the percentage rises ((A − B) ÷ B) × 100 and ((C − D) ÷ D) × 100, and must be checked against the print.

## Seat

The encoding is written from the seat of **the DFRB pensioner, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much does my annual pension increase from 5 July 1973?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope |
| s 4 | (2), (4) encoded; (5) applied (a widow's pension counts as one for the contributor's retirement); (3) (revised index numbers) is folded into the inputs |
| s 5 | encoded |
| s 6 | out of scope: suspended pensions |
| s 7 | (1)(a), (2), (4)-(5) encoded; (1)(b), (3), (6) (s 82ZB pensions, re-entry) are out of scope |
| ss 8-11 | out of scope |
| s 12 | noted: from the instalment due on 5 July 1973 |

## Forks (readings taken)

- **F1, s 4(2).** The formulas are as above.
- **F2, s 4(4).** The percentage is rounded to the nearest tenth, with a half rounding up.
- **F4, s 4(1) (changed after the independent pass).** "Pension" covers only a retirement or death on or before 30 September 1972. A later one gets no increase under this Act.
- **Known limits (from the independent pass).** There is no widow field for s 4(5): the contributor's retirement date is entered. The s 12 date is not computed.
- **F3, s 7(2), (4)-(5).** Months are counted from the day after the retirement or death to 30 June 1973, by corresponding dates. A remaining part month counts as a month if its days are at least half of that month's days. The total is never below one month.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 44 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`dfrb73-tests.l4`), 29 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** confirm the s 4(2) formulas.
