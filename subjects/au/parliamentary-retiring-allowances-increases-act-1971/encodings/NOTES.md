# Parliamentary Retiring Allowances (Increases) Act 1971 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the increase position for` (`pra71-rules.l4`). It gives the increase, or the widow's pension, under ss 3-8, and the day it takes effect (s 12). The source is the Act as made (No. 75 of 1971).

## Seat

The encoding is written from the seat of **the former member or office-holder, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What increase in my pension am I entitled to; and as a widow, what is my pension or its increase?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | applied: commencement on 1 October 1971 |
| ss 3-8 | encoded; the class is an input |
| ss 9-11 | out of scope: the Funds |
| s 12 | noted: from the first fortnightly payment after commencement (an input date) |

## Forks (readings taken)

- **F1.** The tables list exact amounts. An amount not listed gets no increase, and the answer is NOTHING.
- **F2, s 6(2).** The widow's increase is five-sixths of the increase her husband's pension received under s 6(1). His pension amount is the input.
- **F3, s 8.** "Increased by one-half" means the increase is half the pension.
- **F4, s 12(2).** For a pension under s 7 first payable after commencement, the start date is the first fortnightly payment of that pension. The same input date serves.

- **Known limits (from the independent pass).** The s 7 and s 8 date conditions are folded into the class. The s 12 date is given to every increase, including s 6(2) (which s 12 does not list) and s 7 cases first payable after commencement.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 48 assertions satisfied, 0 failed, 0 other errors — 14 the encoder's (`pra71-tests.l4`), 34 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance. The Act is historical.
