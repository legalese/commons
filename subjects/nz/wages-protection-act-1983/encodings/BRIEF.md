# Encoding brief: the Wages Protection Act 1983 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Wages Protection Act 1983**: New Zealand, Public Act 1983 No 143. The source is version 25 as at 27 November 2025, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

What the Act covers:
- **ss 1-3**: title and commencement (1 February 1984), interpretation, the Crown is bound.
- **ss 4, 5, 5A**: wages to be paid without deduction, except with the worker's written consent or request (including a general deductions clause, after consultation), for a lawful purpose, and not unreasonably; withdrawing a consent.
- **s 6**: recovering an overpayment made for a period when no wages were payable (absence without authority, strike, lockout, suspension), and the notice the employer must give.
- **ss 7-10**: wages to be paid in money, or by cheque, postal order, money order or bank lodgement in the cases the Act allows.
- **ss 11, 11A**: recovery of unlawful deductions and of wages paid otherwise than in money, the time limits, and recovery from a person involved.
- **ss 12, 12A**: no stipulation on how wages are spent; no premium for employment.
- **s 13**: penalties.
- **ss 15-19 and the Schedule**: other Acts, collective agreements, the 1964 saving, administration, repeals, and the transitional provisions for the 2016 amendments.

The source is `../source/WPA1983.txt`, text extracted from the PCO's PDF; `../source/PROVENANCE.md` records it. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

## The top-level goal, and the goals under it

Top level: *for this payment of wages, were the deductions lawful; were the wages paid in a lawful manner; did the employer contravene the Act; and what may the worker, or a Labour Inspector, recover from the employer under s 11 in an action brought on a given day?*

1. **Deductions and overpayments**: ss 4, 5, 5A, 6, 15, 16.
2. **The manner of payment**: ss 7-10, 15-17.
3. **Recovery**: ss 11, 11A.
4. **Premiums, spending and penalties**: ss 12, 12A, 13.

Inputs, not worked out:
- whether a person is a worker or an employer (ERA ss 5, 6), and whether a person is "involved" (ERA s 142W);
- whether a deduction is for a lawful purpose, or unreasonable; whether consent was obtained by duress; whether the worker was consulted;
- whether another Act, a collective agreement or an order authorises a deduction or a manner of payment;
- for s 6(3)(ba), the count of working days.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`wpa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
