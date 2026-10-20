# Encoding brief: the National Rental Affordability Scheme Act 2008 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**National Rental Affordability Scheme Act 2008** (No. 121, 2008), Commonwealth of Australia, compilation No. 4 of 5 December 2025, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2008A00121.txt` (CC BY 4.0). It is taken to have commenced on 1 July 2008. The Scheme itself is made by regulations, which are not deposited.

## Seat

The encoding is written from the seat of **the investor who owns a dwelling under the Scheme** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is my property a rental dwelling? When does its 10-year incentive period end? This year, does it meet the conditions the Act itself sets for an allocation? Which NRAS year is a given day in?"*

In scope: s 4 (incentive period, NRAS year, rental dwelling), s 7(2), (3) and (5). Out of scope: ss 1-3A, s 5-6, s 7(1), (4), (6)-(7), ss 8-12 (the Scheme's own content, variations, incentives, compensation, undertakings, delegation, regulations).

## Inputs

- The kind of dwelling (a dwelling or separately habitable part; a strata unit; a caravan, houseboat or other mobile dwelling; one the regulations exclude), and whether rent is payable.
- The first day of the incentive period.
- Whether it was lived in as a residence before the period began; whether it was unfit and not lived in from being made fit to the period's start.
- For the year: whether it was rented; whether the tenants are of the prescribed kind; each rent charge and the market value rent for the same period; whether the Secretary disapplied the rent condition; the longest vacancy and the longest the regulations allow.
- The day asked about, for the NRAS year.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`nras-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
