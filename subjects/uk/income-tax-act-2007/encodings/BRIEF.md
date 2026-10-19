# Encoding brief: the Income Tax Act 2007 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Income Tax Act 2007** (2007 c. 3), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 16 September 2026, deposited at `../registers/source-bundle/ukpga-2007-3.txt` (Crown copyright, Open Government Licence v3.0).

## Seat

The encoding is written from the seat of **the individual taxpayer**: UK resident, not a Scottish or Welsh taxpayer, with no property income (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the taxpayer's words: *"What is my personal allowance this year? How much income tax do I owe on my wages, savings and dividends, after Gift Aid and pension contributions? Can I transfer part of my allowance to my spouse or civil partner, or receive it, and what is it worth?"*

1. **Personal allowance** (ss 35, 58, 415): adjusted net income (net income less the grossed-up Gift Aid and the gross relief-at-source pension contributions); the £12,570 allowance reduced by half the excess over £100,000, rounded up to a whole pound, not below nil; reduced by the transferable amount if I have elected to transfer it (s 55B(6)).
2. **Income tax liability** (ss 8, 10(2)-(3A), (5)-(6), 12, 12A, 12B, 13, 13A, 16, 23, 25(3A), 414(2)):
   - the allowance deducted from non-savings income first (s 25(3A)), then from savings or dividends in the way that gives the greatest reduction (s 25(2));
   - savings and then dividends as the highest part of income (s 16);
   - the basic rate limit £37,700 and the higher rate limit (twice £12,570 plus £100,000 = £125,140), each increased by the grossed-up Gift Aid and gross pension contributions (ss 10(5A), (6), 414(2));
   - the starting rate for savings (0% up to £5,000 of income, so far as savings), the savings allowance (£1,000, £500 or nil) at the savings nil rate, the dividend nil rate on the first £500 of dividends, and the dividend ordinary, upper and additional rates (10.75%, 35.75%, 39.35%), with nil-rate income still using up the bands;
   - the tax reduction for a marriage allowance (Step 6).
3. **Marriage allowance** (ss 55B-55C):
   - the transferable amount (10% of £12,570, rounded up to a multiple of £10: £1,260);
   - whether I may elect to transfer (I am entitled to a personal allowance and, with it reduced, I would pay no more than basic rate; the net-income condition of s 55C(2) applies only to those resident under s 56(3));
   - whether, as the gaining party, I am entitled to the reduction (no tax above the basic rate, the dividend ordinary rate or nil rates), and its amount (the basic rate of the transferable amount, not more than the tax before it).

Left out on purpose: Scottish and Welsh taxpayers, non-residents, property income rates, trusts, the reliefs deductible at Step 2 (losses and the rest), blind person's and married couple's allowances, other tax reductions, Step 7 charges, the remittance basis, and the anti-avoidance Parts.

## Inputs, not worked out

- The rates determined by Parliament for the year (ss 6, 7A): basic, higher and additional rates, and the savings basic, higher and additional rates.
- Non-savings income, savings income and dividend income (net of any Step 2 reliefs).
- Gift Aid donations paid (net), and gross pension contributions under relief at source.
- Whether I have elected to transfer allowance, or my spouse or civil partner has elected to transfer to me.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ita-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
