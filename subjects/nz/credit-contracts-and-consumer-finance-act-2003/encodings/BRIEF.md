# Encoding brief: the Credit Contracts and Consumer Finance Act 2003 (New Zealand), cancellation, interest, high-cost credit, hardship and statutory damages, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Credit Contracts and Consumer Finance Act 2003 (CCCFA)**: New Zealand, Public Act 2003 No 52. The source is the version as at 1 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2003_52.txt` (sha256 `be069b0a74127a8679c4074e7eecb4ee108c378a8e688fbbc76dadc9ae23130a`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels. This matters in **s 89(2)**, which sets a $200 minimum for "the amount of the statutory damages under subsection (1)(d)": with the labels lost, the encoding reads (1)(d) as the general limb ("in the case of any other breach, the lesser of $6,000 or 5% of ..."), the only limb whose amount can be small. Schedule 1 (key information) is not needed.

**Working day** is defined in s 5 (the same days as the Legislation Act 2019, s 13).

## Scope

- **Cancellation and disclosure**: s 18(2) (the maximum period of a continuing disclosure statement: 45 working days for revolving credit, otherwise 6 months), s 27 (cancellation within 5 working days of initial disclosure, or at any time without it; returning the advance within 5 working days, or paying the cash price within 15 working days of the notice), s 29 (exceptions).
- **Interest**: s 39 (daily rate on daily balances; periodic rates of the annual rate ÷ 52, 26, 12, 4 or 2), s 40 (default interest only on the amount in default or the excess over the limit, and not on amounts accelerated except under an on-demand facility).
- **High-cost credit**: s 45C (50% or more), s 45E (costs of borrowing not to exceed the first advance), s 45F (no contract with someone who has, or had in the preceding 15 days, a balance on another creditor's high-cost contract), s 45G (no contract with someone who entered 2 or more in the preceding 90 days), s 45H (0.8% a day), s 45I (no compound interest).
- **Hardship**: s 55(3) (a further application only after 4 months, unless the creditor agrees or the reasons differ), s 57 (when an application may not be made), s 57A (the creditor's 5, 10 and 20 working days, and the extension after a request for information).
- **Statutory damages**: s 89 (the amounts for each kind of breach; the $6,000 / 5% limb; $200 minimum; the highest of simultaneous breaches).

## The top-level goal, and the goals under it

Top level: *for a consumer credit contract: is it high-cost and may it be entered into, is the debtor's cancellation in time, are the costs of borrowing within the caps, may a hardship application be made and by when must the creditor answer it, and what statutory damages follow a breach?*

1. **Cancellation and disclosure**: ss 18, 27, 29.
2. **Interest and high-cost credit**: ss 39, 40, 45C, 45E-45I.
3. **Hardship**: ss 55, 57, 57A.
4. **Statutory damages**: s 89.

Inputs, not worked out: the contract's rates, balances, fees and payments; dates of disclosure, notice, applications and requests; the debtor's other high-cost contracts; default history; the breach and the amounts s 89 measures; Matariki Observance Days.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`cccfa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
