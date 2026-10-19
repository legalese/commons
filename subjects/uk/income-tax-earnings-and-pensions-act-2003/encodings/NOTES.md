# Income Tax (Earnings and Pensions) Act 2003 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the employee position for` (`itepa-goal.l4`). It answers:

- **Company car:** the appropriate percentage and the cash equivalent.
- **Cheap loan:** the cash equivalent.
- **Termination:**
  - the earliest lawful termination date;
  - the post-employment notice pay;
  - the part of the termination awards taxed as earnings;
  - the part taxed above the £30,000 threshold.

All three goals sit in `itepa-rules.l4`:

1. **Company car:** ss 120(1), 121(1), 132(3), 133(2)-(3), 139(2)-(4), 141(2), 143(1)-(3) and 144(1)-(3).
2. **Cheap loans:** ss 175(1)-(3), 180(1)-(2) and 182.
3. **Termination payments:** ss 402A, 402B, 402C(3)-(4), 402D(1)-(6A), 402E(2)-(7), 403(1), (4) and 404(4).

The source is the revised text at 15 July 2026.

**Missing formulas.** The deposited conversion drops the formulas printed as images. Three are taken from the published Act and must be checked against it:

- s 143(3): (U ÷ Y) × A;
- s 182, step 3: A × I × M ÷ 12;
- s 402D(1): ((BP × D) ÷ P) − T.

The table in s 139(1), for cars under 75 g/km, is missing too. Such cars answer NOTHING.

## Seat

The encoding is written from the seat of **the employee**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "How much is taxed on me for my company car this year? For my cheap or interest-free loan from my employer? And when my job ends, how much of my termination package is taxed as earnings, and how much of the rest above £30,000?"

The facts it asks for are ones that person can state from their contract, payslips and the employer's figures.

## Coverage

| Provision | Disposition |
|---|---|
| Parts 1-2 | out of scope: charge, residence |
| Part 3 Chapters 1-5 | out of scope: general earnings, other benefits |
| s 114-119 | out of scope (that the car is made available by reason of employment is assumed) |
| s 120 | (1) encoded; (2)-(4) are out of scope |
| ss 120A, 121A-121B | out of scope: optional remuneration arrangements |
| s 121 | (1) encoded; (2)-(3) (gas cars, classic cars, shared cars) are out of scope |
| ss 122-131 | the price and accessories are inputs |
| s 132 | (3) encoded |
| s 133 | (2)-(3) applied: only cars registered on or after 1 January 1998 with a CO2 figure |
| ss 134-138 | whether the car has a CO2 figure is an input (the figure) |
| s 139 | (2)-(4) encoded; (1)'s table is missing from the text: NOTHING |
| s 140, s 142 | out of scope |
| s 141 | (2) encoded |
| s 143 | (1)-(3) encoded; (4) (temporary replacement) is out of scope |
| s 144 | (1)-(3) encoded |
| ss 145-172 | out of scope |
| s 173-174 | out of scope (an employment-related loan is assumed) |
| s 175 | (1)-(3) encoded; (1A)-(1B), (4)-(5) are out of scope |
| ss 176-179 | whether an exception applies is an input |
| s 180 | (1)(a), (2) encoded; (1)(b), (3)-(5) (non-qualifying loans) are out of scope |
| s 181 | the official rate is an input |
| s 182 | encoded |
| s 183 | out of scope: the alternative method |
| ss 184-400 | out of scope |
| s 401-402 | that a payment is within the Chapter is assumed |
| ss 402A-402E | encoded; s 402D(7)-(12) (basic pay, anti-avoidance) and s 402E(8)-(10) (limited-term contracts) are inputs or out of scope |
| s 403 | (1), (4) encoded; (2)-(3), (5)-(6) are out of scope |
| s 404 | (4) applied as earlier amounts; (1)-(3), (5)-(6) are out of scope |
| ss 404A onwards | out of scope |

## Forks (readings taken)

- **F1, the missing formulas.** They are taken from the published Act, as above.
- **F2, s 139.** The CO2 figure is rounded down to a whole number, then to a multiple of 5. The percentage is 21 + (figure − 75) ÷ 5, at most 37. A diesel car under s 141 adds 4, at most 35. Below 75 the answer is NOTHING.
- **F3, s 402E(7).**
  - With notice in days, the earliest lawful termination date is the trigger date + the notice days.
  - With notice in whole months, it is the corresponding date that many months after the trigger date, or the last day of the month where there is none.
  - The notice period in days is that date minus the last day of employment, and nil if it is not later.
- **F4, s 402D(6).** The whole-months case applies when pay is monthly in equal instalments, the notice is in whole months, and the earliest lawful termination date is the corresponding date k months after the last day of employment (k from 1 to the months of notice). Then P is 1 and D is k. Other monthly pay uses P = 30.42 and D in days. Otherwise P is the days in the last pay period.
- **F5, s 403.** The amount taxed is what remains after s 402B, including redundancy pay and the approved contractual part, to the extent that it exceeds what is left of the £30,000 after earlier amounts.
- **F6, s 144.** A payment counts only if it was required as a condition of private use and paid by 6 July after the tax year.
- **F7, s 143(2).** Unavailable days are the days before the first day available, the days after the last, and the days given in periods of 30 days or more.
- **Known limits (from the independent pass).**
  - s 144(1)(b): there is no input for the amount required; whatever was paid in time is deducted (a partial payment is deducted, as in HMRC practice; the literal reading may give none).
  - s 143(2): unavailable days in long periods are an input and could overlap the days before the first or after the last day available.
  - s 402D(6): whole months are found by stepping by months from the last day, clamping to month ends; 28 February to 31 March is not treated as one whole month.
  - s 402E(2)(b): a notice case with no notice date falls back to the last day of employment.
  - s 402D(5), s 180(1)(b), the split under s 402C(2)(b) and the order in s 404(5) are left to the inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 5 modules: 146 assertions satisfied, 0 failed, 0 other errors — 46 the encoder's (`itepa-tests.l4`), 100 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** confirm the three formulas against the official print.
- **F4:** is a notice period ending on the corresponding date of a later month "otherwise a whole number of months"?
