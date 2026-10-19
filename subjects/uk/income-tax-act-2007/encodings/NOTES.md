# Income Tax Act 2007 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the taxpayer position for` (`ita-goal.l4`). It is for an individual who is UK resident, is not a Scottish or Welsh taxpayer, and has no property income. It answers:

- adjusted net income;
- the personal allowance;
- the savings allowance;
- the tax before reductions;
- the marriage allowance reduction;
- the income tax liability;
- whether I may elect to transfer part of my allowance.

All three goals sit in `ita-rules.l4`:

1. **Personal allowance:** ss 35, 55B(6), 58 and 415.
2. **Income tax liability:** ss 8, 10(2)-(3A), (5)-(6), 12, 12A, 12B, 13, 13A, 16, 23 Steps 3-6, 25(3A) and 414(2).
3. **Marriage allowance:** ss 55B(1)-(5) and 55C(1).

The source is the revised text at 16 September 2026.

The basic, higher and additional rates, and the savings basic, higher and additional rates, are "determined ... by Parliament" (ss 6(2), 7A) and are inputs. The figures the Act itself sets are encoded:

- the limits: £37,700 and £5,000;
- the allowances: £12,570, £1,000, £500 and the £500 dividend nil rate band;
- the dividend rates: 10.75%, 35.75% and 39.35%.

## Seat

The encoding is written from the seat of **the individual taxpayer**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "What is my personal allowance this year? How much income tax do I owe on my wages, savings and dividends, after Gift Aid and pension contributions? Can I transfer part of my allowance to my spouse or civil partner, or receive it, and what is it worth?"

The facts it asks for are ones that person can state from their payslips, bank and dividend statements and donation records.

## Coverage

| Provision | Disposition |
|---|---|
| Part 1 | out of scope |
| s 6, 7A | the rates are inputs |
| ss 7-8 | the savings and dividend rates are applied as printed |
| s 9 | out of scope: trusts |
| s 10 | (2)-(3A), (5)-(6) encoded; (4) other provisions only as encoded |
| ss 11-11C, 11CA-11CB | out of scope: non-individuals, Scottish, Welsh, non-UK residents, property income |
| s 11D | applied, with the savings rates as inputs |
| ss 12-13A | encoded |
| s 14-15 | out of scope |
| s 16 | applied: savings, then dividends, as the highest part of income |
| ss 17-21 | out of scope |
| s 23 | Steps 3-6 applied; Step 2 reliefs and Step 7 charges are out of scope (income is given net) |
| ss 24-30 | out of scope, except s 25(3A) (the order of deducting the allowance) |
| s 35 | encoded |
| ss 36-55 | out of scope: blind person's and married couple's allowances |
| ss 55A-55C | encoded for UK residents (s 55C(2) applies only under s 56(3)); ss 55D-55E (procedure, limits) are out of scope |
| s 56 | residence is assumed |
| s 58 | Steps 1-3 encoded; Step 4 (trade union relief) is out of scope |
| Parts 4-7 | out of scope: losses and other reliefs |
| s 414 | (2) encoded; s 414A (Scottish and Welsh) is out of scope |
| s 415 | encoded |
| ss 416-430 | whether a gift is a qualifying donation is assumed |
| the rest of the Act | out of scope |

## Forks (readings taken)

- **F1, s 25(2)-(3A) (changed after the independent pass).** The personal allowance is deducted from non-savings income first (s 25(3A)). Between savings and dividends it is deducted in whichever order gives less tax (s 25(2)), so it may go against dividends and keep savings at the starting rate.
- **F2, s 35(3).** The tapered allowance is rounded up to a whole pound, and is not below nil.
- **F3, s 10(5A).** The higher rate limit is 2 × £12,570 + £100,000 = £125,140. Gift Aid and pension contributions increase it and the basic rate limit by the grossed-up and gross amounts (s 414(2)(b), s 10(6)).
- **F4, ss 12, 12A, 13A.** Income at the starting rate for savings, the savings nil rate and the dividend nil rate still uses up the bands. The starting rate covers taxable savings within the first £5,000 of taxable income.
- **F5, s 12B.** Higher-rate income means taxable income above the basic rate limit; additional-rate income means taxable income above the higher rate limit. Income that would be so charged but for the nil rates counts.
- **F6, ss 55B(2)(b)-(ba), 55C(1)(c)-(ca) (changed after the independent pass).** "Not liable to tax at a rate other than" the listed rates is read as follows. Non-savings income is within the basic rate limit. No savings above it are charged except at the starting rate or the savings nil rate. No dividends lie above it, even those within the dividend nil rate (s 55B(2)(ba)).
- **F7, s 55B(4)-(5).** The transferable amount is 10% of £12,570 = £1,257, rounded up to £1,260. The reduction is the basic rate of it, given at Step 6 and so no more than the tax before it.
- **F9, s 55B(6).** The transferring spouse's allowance is reduced whenever they have elected; the encoding assumes the other spouse is entitled to the reduction.
- **F8, s 55C(2).** The net-income condition applies only to individuals resident by virtue of s 56(3), outside this encoding's seat.
- **Known limits (from the independent pass).**
  - The marriage or civil partnership itself (s 55C(1)(a)) and the married couple's allowance exclusion (s 55B(2)(d)) are assumed.
  - Negative inputs are not rejected.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 5 modules: 127 assertions satisfied, 0 failed, 0 other errors — 42 the encoder's (`ita-tests.l4`), 85 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F6:** is a gaining party whose dividends fall within the £500 nil band but above the basic rate limit excluded (s 55B(2)(ba))? The encoding excludes them, but allows savings above the limit at the savings nil rate.
