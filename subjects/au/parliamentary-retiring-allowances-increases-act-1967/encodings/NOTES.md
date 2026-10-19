# Parliamentary Retiring Allowances (Increases) Act 1967 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the increase position for` (`pra-rules.l4`). For a parliamentary pensioner or widow, it gives:

- the increase in the pension;
- the widow's pension;
- the day the increase takes effect.

The operative ss 3, 4 and 7 are encoded. The source is the Act as made (No. 92 of 1967), which commenced on 8 November 1967.

## Seat

The encoding is written from the seat of **the former member, or the widow, entitled to a parliamentary pension**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What increase in my pension am I entitled to, and from when; and as a widow, what is my pension?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | applied: commencement on 8 November 1967 |
| s 3 | encoded; which class a person is in (s 3(1)(a)-(b)) is an input |
| s 4 | encoded |
| ss 5-6 | out of scope: the Fund |
| s 7 | encoded: the date of the first fortnightly payment after commencement is an input |

## Forks (readings taken)

- **F1.** The tables list exact pension amounts. An amount not listed gets no increase under this Act, and the answer is NOTHING.
- **F2, ss 3(2), 4(2).** The widow's pension is a fixed rate, $48.16 a week or $2,729.17 a year, not an increase.

- **Known limits (from the independent pass).** s 3(1)(a) and (b) are one class. The first fortnightly payment date is not checked to fall after 8 November 1967. The widow's $2,729.17 in s 4(2) is read as annual; the Act does not say so.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 37 assertions satisfied, 0 failed, 0 other errors — 14 the encoder's (`pra-tests.l4`), 23 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance. The Act is historical.
