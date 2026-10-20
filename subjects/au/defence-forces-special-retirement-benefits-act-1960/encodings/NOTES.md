# Defence Forces Special Retirement Benefits Act 1960 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the soldier position for` (`dfsrb-rules.l4`). It answers:

- whether the Act applies to me;
- my benefit (a gratuity under s 6 or s 7, or a pension under s 9 or s 10);
- the special gratuity in pounds;
- my pension rate in pounds a year;
- the prescribed day by which my contribution must be paid.

The encoded provisions are ss 4, 6, 7, 9(1)-(2), (4)-(5), 10(1)-(2), (4)-(5) and the First Schedule. The source is the compilation prepared on 19 April 2001; the Act commenced on 1 February 1961.

## Seat

The encoding is written from the seat of **the Regular Army soldier discharged in the 1961 reduction**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does the Act apply to me; what gratuity or pension do I get?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery; the category is an input (s 3(2)(b)) |
| s 4 | encoded |
| s 5 | applied: completed years of service for pension are an input |
| s 6 | encoded; the refund of contributions is noted, not computed |
| s 7 | (1)(b), (2) encoded; the s 42 gratuity and refund are not computed |
| s 8 | out of scope |
| s 9 | (1)-(2), (4)-(5) encoded; the Board's and Actuary's figures are inputs; (3), (6)-(7) are out of scope |
| s 10 | (1)-(2), (4)-(5) encoded; the Board's figures are inputs; (3), (6)-(7) are out of scope |
| s 11 | repealed |
| s 12 | out of scope |
| First Schedule | encoded |
| Second Schedule | out of scope: for repealed s 11 |

## Forks (readings taken)

- **F1, s 4(1).** "The period of three months commencing on" 1 February 1961 ends on 30 April 1961; nine months end on 31 October 1961.
- **F2, s 4(2)(c).** The 55th birthday must fall after the last day of the prescribed period. An engagement must expire after it too (s 4(2)(a)(iii)).
- **F3, ss 7, 9.** A soldier with 15 to 19 years who would not have reached 20 years by 55 is not entitled to a s 9 pension and takes the s 7 gratuity.
- **F4, ss 9(2), 10(2) prescribed day.** "The day occurring one month after service" of the statement is the corresponding day a month later; a contribution must be paid before it, so on the prescribed day is too late.
- **F5, ss 9(5), 10(5).** A contribution at or above the maximum gives the maximum rate; below it, the rate is scaled in proportion. For a person contributing for additional benefits, the scale runs from the minimum to the normal rate up to the normal contribution, and from the normal to the maximum rate above it.
- **Known limits (from the independent pass).**
  - Years of service, the 20-by-55 test and the Board's figures are inputs.
  - A contribution above the maximum gives the maximum rate; the Act speaks only of equal or less.
  - s 9(7)/10(7) (death before the prescribed day) are out of scope.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 67 assertions satisfied, 0 failed, 0 other errors — 25 the encoder's (`dfsrb-tests.l4`), 42 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F4:** for a statement served on 31 January, is the prescribed day 28 February?
