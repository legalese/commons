# Encoding brief: the Tax Administration Act 1994 (New Zealand), PAYE reporting, filing and penalties, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Tax Administration Act 1994**: New Zealand, Public Act 1994 No 166. The source is the version as at 4 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_1994_166.txt` (sha256 `9aa6d56e3b0aab85fd895c0667717c73b39c75909d4f192854cb7d8dd7a27bab`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels, formulas and tables. Within the scope below, nothing computable is lost.

**Definitions from the Income Tax Act 2007.** Section 3 gives undefined terms their Income Tax Act meaning. Two are used here: **working day** (Income Tax Act s YA 1: not a Saturday, Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Matariki Observance Day or Labour Day; the Monday after Waitangi Day or Anzac Day when either falls on a weekend; or 25 December to 15 January), and **late balance date** (s YE 1(7): an approved income year ending between 1 April and 30 September). The rate for a non-notified tax code (0.45) is in the Income Tax Act, schedule 2, part A, clause 3.

## Scope

- **Employment income information**: ss 23E, 23F (the non-electronic group, its $50,000 threshold and its choice of payday), 23H (new employers), 23M (ceasing to employ).
- **Tax codes**: s 24E (non-notified tax codes).
- **Returns**: s 33(1) (who must file), s 37(1) and (4)-(5) (the due date, and the latest date to which time may be extended through a tax agent).
- **Time bar**: s 108(1), (2).
- **Late filing penalty**: s 139A(2)-(3), (5), (9).
- **Late payment penalty**: s 139B(1)-(2B), (3)-(4) (the initial 1% and 4% penalties and the incremental 1%).
- **Shortfall penalties**: ss 141A-141E (the rates), 141FB (previous behaviour), 141G (voluntary disclosure), 141H (adequate disclosure), 141I (temporary shortfall), 141J (limitation), 141JAA (the $50,000 cap), 141K (obstruction).

## The top-level goal, and the goals under it

Top level: *for a taxpayer and a tax year: by when must the return be filed, what late filing penalty applies, what late payment penalty has accrued on unpaid tax at a date, what shortfall penalty applies to a tax shortfall, and until when may the Commissioner increase the assessment?*

1. **Working days and employment income information**: ss 23E-23M, 24E, with the Income Tax Act working day.
2. **Returns and the time bar**: ss 33, 37, 108.
3. **Late filing and late payment penalties**: ss 139A, 139B.
4. **Shortfall penalties**: ss 141A-141K, 141JAA.

Inputs, not worked out: the default date (due date) of the tax; whether the Commissioner has notified penalties; the taxpayer's culpability, disclosures and history; the PAYE and ESCT amounts for the threshold; Matariki Observance Days; whether a tax is one on which incremental penalties no longer run (s 139B(2B)).

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`taa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
