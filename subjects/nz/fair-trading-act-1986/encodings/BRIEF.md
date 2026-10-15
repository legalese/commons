# Encoding brief: the Fair Trading Act 1986 (New Zealand), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Fair Trading Act 1986**: New Zealand, Public Act 1986 No 121. The source is the version as at 1 July 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_1986_121.txt` (sha256 `1492a0dc367352065b5dbdfcb70b4617a808a22efd0e68d272b8739f9d77c036`), converted from the PCO's XML on 2026-10-13 (`act_public_1986_121.meta.json` beside it). There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** The paragraph labels ((a), (b), (i) …) are not in the text; a provision's place in its list gives its label. Sections that have been repealed appear as headings with no text.

What the Act covers:
- **ss 1-6**: purpose, interpretation (consumer, goods, services, trade), application to conduct outside New Zealand and to the Crown, the Takeovers Code, and no contracting out except between parties in trade (ss 5C, 5D).
- **Part 1, ss 7-26E**: unfair conduct: unconscionable conduct, misleading and deceptive conduct, unsubstantiated and false representations, land, vendor bids, news media, trade marks, gifts and prizes, bait advertising, referral selling, payment without intending to supply, unsolicited goods and services, business activities, harassment, pyramid selling, false trade descriptions, unfair contract terms and the specified trade contract thresholds.
- **Part 2, ss 27-28B**: consumer information standards; trader status online.
- **Parts 3 and 4, ss 29-36**: product safety standards, unsafe goods notices, recalls, product safety officers, suspension of supply; safety of services.
- **Part 4A, ss 36A-36ZF**: layby sales, uninvited direct sales, extended warranties, gift card expiry dates, auctions.
- **Part 5, ss 37-46M**: jurisdiction, offences and fines, infringement offences, injunctions and orders, the 3-year limit for s 43 orders, defences, undertakings, management banning orders, declarations of unfair contract terms.
- **Part 6 and Schedules**: Commission powers, overseas regulators, financial products, transitional provisions.

## The top-level goal, and the goals under it

Top level: *for this conduct, in these circumstances, does it contravene the Act, which provision, is it an offence, what is the maximum fine, who may bring proceedings, and by when must a person apply for an order under s 43?*

1. **Conduct (Part 1)**, with ss 2-5D.
2. **Consumer transactions and auctions (Part 4A)**.
3. **Product and service safety (Parts 2-4)**.
4. **Enforcement (Part 5)**.

Inputs, not worked out:
- whether conduct is misleading, deceptive, unconscionable, unsubstantiated, false, harassing, coercive or unfair; whether a contract is a standard form contract; whether a term is transparent;
- whether a consumer information, product safety or services safety standard exists and was complied with; whether a notice is in force;
- which days are working days (the encoding counts working days from a list of non-working weekdays given as an input);
- prescribed amounts (infringement fees) and Disputes Tribunal limits set by other Acts, where the text refers to them.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`fta-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
