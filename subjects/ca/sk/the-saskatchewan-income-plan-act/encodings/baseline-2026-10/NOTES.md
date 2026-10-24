# The Saskatchewan Income Plan Act and The Seniors Income Plan Regulations — baseline encoding

## Method

**Baseline.** Written straight from the deposited texts, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; nothing here needs a not-covered answer, because the regulations state every amount.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in `sk-sip.l4`, with one regulative rule. The senior's questions are in `sk-sip-seat.l4`, which IMPORTs the core and calls its rules; nothing is restated. Each question has `@export` and every input a `@desc`. There was no earlier encoding to keep.

This is the smaller of the two Saskatchewan benefit encodings. It sits beside Saskatchewan Income Support (`../../../the-saskatchewan-assistance-act/encodings/baseline-2026-10/`), and unlike that program its amounts are all in the regulations.

## Licence and notice

Quoted under the Government of Saskatchewan's non-commercial reproduction terms, with the **owner's ruling of 24 Oct 2026** that texts permitting reproduction but silent on adaptation may be quoted in L4 encodings in Commons. Every module opens with the "unofficial version, not an official version" notice and "© 2026, Government of Saskatchewan." See `SOURCE-LICENSE.md` (a copy of the subject's).

## Edition

- **The Saskatchewan Income Plan Act**, S.S. 1986, c. S-25.1, King's Printer consolidation, "Last update posted: 26 Oct 2018", at `../../registers/source-bundle/S.S.-1986-c.-S-25.1.txt`.
- **The Seniors Income Plan Regulations**, R.R.S. c. S-25.1 Reg 3, "Last update posted: 9 June 2023" (amended to SR 39/2023, which set the $360 and $325 maxima), at `../../registers/source-bundle/R.R.S.-c.-S-25.1-Reg-3.txt`.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sk-sip.l4`, `sk-sip-seat.l4` | `sk-sip-cases.l4` | 35 written, 35 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the text.

## Seat

**The senior who receives, or asks about, the Seniors Income Plan**: "Am I eligible? How much will I get each month? When does a move into a special-care home change it? If I was underpaid, from when will I be paid? When does it stop? Can it be taken?"

The 2026-10-18 defaults:

- **The Act, with the regulations that set its numbers:** the Seniors Income Plan Regulations, deposited, set every amount.
- **The actors the text names:** the beneficiary and the minister.
- **Judgments handed to others:** none needed. The federal minister's determinations of the GIS and the Allowance are inputs.
- **Definitions worked out from facts:** resident (Act s 2(e)), pensioner (Reg s 2(f)), resident of a facility (Reg s 2(g), asked as one fact), payment period (Reg s 2(e)). **Borrowed terms are asked as facts:** the OAS pension, the GIS and the Allowance, and the amount by which the GIS and the spouse's Allowance fall short of the maximum under the federal Table of Rates.
- **One case:** one beneficiary in one month.
- **The texts' own terms**, quoted in the comment above each rule.
- **Machinery out:** the federal-provincial agreement (Act s 10.1), regulation-making (Act s 11), the method of payment (Reg s 8).

## Regulative rules

One: `the minister's duty to pay my arrears` (Reg s 9(1)): where an underpayment is discovered, the minister MUST calculate and pay the benefits owing (no time is set). How far back is a date function (Reg s 9(2)).

## Scope

**In:** Act ss 2(d)-(f), 4, 6, 7, 8, 9; Reg ss 2, 4, 5, 6, 7, 9.

**Out:** Act ss 3 (appropriation), 5 (application form), 10.1, 11; Reg ss 3 (the basis of entitlement, which only says entitlement follows the monthly GIS), 8, 10, 11.

Read with `subjects/ca/old-age-security-act/` (the federal OAS Act and Regulations): the GIS, the Allowance and the Table of Rates are its business, and this encoding takes the reductions as inputs.

## What the texts turn out to say

1. **A small top-up for GIS recipients only.** The maximum is $360 a month for a single pensioner or a pensioner whose spouse is not a pensioner, $325 each where both are pensioners, and $50 in a special-care home (Reg s 4). It is paid monthly (Act s 6) to Saskatchewan residents who receive both the OAS pension and the GIS (Act s 4). Asserted.
2. **"Meets the requirements prescribed in the regulations" adds nothing.** Act s 4(c) refers to prescribed requirements, but the regulations prescribe none beyond being a "pensioner". Asserted (eligibility on the Act's three facts).
3. **The clawback runs off the GIS, at steep rates.** The maximum falls by $1.90 for each $1 the single person's GIS is reduced, $2.10 where both are pensioners, and $6.55 where the spouse is neither a pensioner nor on the Allowance (Reg s 5(2)(a)(i)-(iii)). For a spouse on the Allowance, it falls by $1.90 for each $3 (or part of $3) the Allowance is reduced ((iv)). "For every $1" is read proportionally, so a reduction of cents reduces SIP by cents. A reading that counts whole dollars only would differ by less than $6.55. Interpretive. Asserted.
4. **The $50 facility maximum is not reduced.** Section 5(2)(a) reduces "the maximum benefit payable pursuant to subsection 4(1)". The $50 of s 4(2) is not mentioned, so a facility resident gets $50 whatever their GIS, as long as they are a pensioner. Section 4(2) is "subject to section 5", which may be meant to reach it. Interpretive. Asserted as encoded.
5. **Minimum payments.** A positive benefit under $15 is raised to $15, or under $5 to $5 for a facility resident (Reg s 6). A reduction to nil stays nil. Asserted.
6. **Facility moves take effect two months on** (Reg s 7). Asserted (November 2026 to January 2027).
7. **Arrears go back only to the start of the July-to-June payment period** in which the underpayment was found (Reg s 9(2), s 2(e)). Asserted.
8. **The benefit cannot be assigned, charged, attached, anticipated or given as security**, and such a transaction is void (Act s 8(1)). An overpayment may be recovered from future payments (Act s 9). Asserted.
9. **Currency.** The Act was last consolidated on 26 Oct 2018 and the regulations on 9 June 2023. Later amendments, if any, are not reflected.

## What would need doing before this is worth relying on

- **The federal Table of Rates**, deposited from the OAS side, so the GIS reduction can be computed from income rather than entered.
- **A check of findings 3 and 4** against ministry practice (none was read).
- **An independent test pass.**
