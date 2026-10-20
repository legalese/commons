# Land Tax Assessment Act 2002 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `lta-landtax.l4`: the module. It covers when the tax is fixed, who is liable, the private residence exemption and its relatives (building, moving, care, death, a disabled relative), taxable value, the Land Tax Act 2002 rate scale, aggregation, and the owner's deadlines.
- `lta-cases-landtax.l4`: the worked cases, built by the scratchpad generator `gen_wa_land-tax-assessment-act-2002_baseline.py`.

Two conventions run through the module:

- A financial year is named by the calendar year in which it ends, so 2029/30 is 2030.
- A day is written as the number YYYYMMDD.

## Edition

- **The Act.** The compilation of the Land Tax Assessment Act 2002 (No. 52 of 2002) deposited at `../../registers/source-bundle/mrdoc_49123.txt` (legislation.wa.gov.au mrdoc 49123, retrieved 2026-09-07). The deposit gives no compilation number or date. It includes the Land Tax Assessment Amendment (Build-to-Rent) Act 2026 (No. 6 of 2026).
- **The rates.** The Land Tax Act 2002 (No. 51 of 2002) is deposited at `subjects/au/wa/land-tax-act-2002/registers/source-bundle/mrdoc_28122.txt` (mrdoc 28122, retrieved 2026-09-07). Its compilation table ends with the Land Tax Amendment Act 2015 (No. 24 of 2015). The encoding brings in s 5 Table 11, "Land tax rates for 2015/16 and subsequent financial years", as a data table.
- **Not deposited.** The regulations that set the "prescribed percentage" for the capped value (Glossary clause 6(4)) are not deposited, so that percentage is an input.

## Checks

One case file: **70 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run lta-landtax.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with two expected values altered (21550 changed to 21551) was run. The runner reported both failures.

## Seat

**The home owner, and the owner of other land.** This is the individual whose land is assessed. The life events ask the question from that seat: "Do I pay land tax on my home?"

The Commissioner assesses, grants, revokes and reassesses. Those powers appear only as what they mean for the owner:

- whether the owner is liable;
- whether the land is exempt;
- what the owner pays;
- by when the owner must pay, report or appeal.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The Land Tax Act 2002 sets the rates and is deposited, so its Table 11 is brought in. The capped-value regulations are not deposited, so their percentage is an input.
- **The actors the text names.** Followed: the owner, joint owners, the vendor and purchaser (s 8(3)), the executor or administrator (s 23), the Commissioner and the Minister (s 20).
- **A judgment handed to someone else is answered conditionally.** Followed. The Valuer-General's unimproved value is a fact the owner states. Whether several lots form one integrated home (Glossary clause 2(4)) is the Commissioner's judgment. It is not modelled, because one case is one lot.
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out from facts: private residential property, the taxing moment (s 7(1)), the s 21 owner categories, the construction years from the commencement and completion dates, taxable value, and aggregated taxable value.
  - Asked as facts: primary residence ("sole or principal place of residence"), spouse and de facto relationship, the Social Security Act qualifications in ss 26A and 26B, war widow status (Veterans' Entitlements Act), and unimproved value (Valuation of Land Act 1978).
- **One case is the text's natural unit.** Followed. For an exemption, one lot at the taxing date. For the amount, one assessment: all of one person's own land, or all of one set of joint owners' land (s 12(3)).
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Left out: regulations (s 46), transitional provisions (s 47 and Schedule 1), and the Taxation Administration Act 2003 machinery.

**Departures:**

- Dates are YYYYMMDD numbers and years are numbers, so that the tests are simple comparisons.
- `On which day after the notice is my land tax due` returns 0 for a reassessment. That value means "see the notice" (s 6(2) defers to the Taxation Administration Act 2003). It does not mean "due at once".

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c055** (2029-07-15), handover of the new Byford house | `Is my land exempt while my new home is built`, `Is my land exempt under the two year building exemption`, `Is my land exempt under the one year building exemption`, `Is my home exempt as my primary residence`, `How much land tax must I pay` | The land is exempt for 2028/29 and 2029/30 under **s 24A** (and s 24 for 2029/30). The house is exempt under s 21 from 2030/31, as spouses living there at 30 June 2030. Even without an exemption, a lot at an assumed $250,000 pays nil. |
| Daniel **d055** (2038-05-20), apartment sold, Nedlands house bought | `Am I liable for the land tax on this land`, `Is my other home exempt while I move`, `Is my home exempt as my primary residence` | Not liable for Nedlands for 2037/38: the vendor owned it at 30 June 2037. From possession, liable but exempt under s 21. If both homes are owned at 30 June 2038, the one not lived in is exempt under **s 27** only if the first-acquired home is sold and handed over in 2038/39 and was not let. |
| Daniel **d084** (2064-01-15), "land tax: none on the home" | `Is my home exempt as my primary residence`, `How much land tax must I pay` | Wholly exempt for 2063/64 under s 21(1)(b) (spouses, at 30 June 2063). Nil to pay. Had it been let, the assumed $2,500,000 would cost $21,550. |

## Why this scope

The scope is what the three events ask, plus what any home owner meets on the way:

- when the tax is fixed and who is liable;
- the private residence exemption and its neighbours that an ordinary owner meets in a lifetime: building, moving, going into care, dying, a disabled relative at home;
- how the tax is worked out on other land (taxable value, the rate table, aggregation, joint land);
- the owner's deadlines and penalties.

Left out, because no owner in the lives meets them:

- the subdivision rules;
- non-strata home units;
- refurbishment and second-home construction (ss 25, 25A, 27A);
- the 2020–2023 construction stimulus (ss 28F–28K), whose commencement window closed on 30 June 2023;
- executor exemptions for a life tenant or future owner (ss 22, 23A);
- the inner city rebate;
- primary production;
- institutional, charitable, park and build-to-rent land;
- the earlier rate tables.

## What the Act turns out to say

1. **Chloe's land tax exemption during the build is s 24A, not s 21.** The life cites s 21. But s 21 tests use "at midnight on 30 June in the financial year before the assessment year", and on 30 June 2028 and 30 June 2029 there was no house to live in.
   - s 24A covers the 2 assessment years 2028/29 and 2029/30. The building contract (taken as made in February 2028) was in an earlier year, part of the construction was carried out in 2028/29, and completion was in 2029/30.
   - The land was owned at 30 June 2028 (settled 15 May 2028).
   - s 24 also covers 2029/30.
   - s 21 takes over from 2030/31.

   Asserted.
2. **Had the land settled after 30 June 2028, s 24A would fail.** The land must be owned at midnight on 30 June before the first year. s 24 would still cover 2029/30. A handover slipping to March 2031 moves the 2 years to 2029/30 and 2030/31, and leaves 2028/29 exposed. Asserted.
3. **Below $300,000 there is no land tax at all.** Table 11 charges nil on a taxable value "not exceeding" $300,000, and a flat $300 up to $420,000. A Byford lot at an assumed $250,000 pays nothing with or without an exemption. Asserted.
4. **The tax is fixed by who owned the land at midnight on 30 June (s 7(1)).** A contract does not shift it. Possession does: s 8(3) keeps the vendor liable "until the purchaser obtains possession". Daniel owes nothing on Nedlands for 2037/38. The seller of the apartment stays liable for 2038/39 if the buyer had not taken possession by 30 June 2038. Asserted.
5. **Moving house across 30 June needs s 27, and s 27 has conditions:**
   - the second home was acquired in the previous financial year;
   - the first-acquired home is sold *and* possession delivered during the assessment year;
   - no income was earned from the home not lived in while both were owned.

   Letting the old apartment, or failing to sell it by 30 June 2039, loses the exemption. The owner must tell the Commissioner when the handover happens (s 27(3)). Asserted.
6. **For spouses, one living there is enough.** The same holds for de facto partners of at least 2 years, whether or not they still live together (s 21(1)(b), (c)). Other co-owners need every owner who does not live there to be on the title only as a lender-required guarantor (s 21(2)). Property held in trust, and property owned by a company, are outside s 21 altogether. Asserted.
7. **Co-owners who are not partners: partial exemption (INFERENCE).** Where a co-owner neither lives there nor is a guarantor, s 21(2) denies the whole exemption. The encoding infers from s 12(2)(b) and s 18 that the interest of the owners who live there stays exempt. So a half share owned by a sibling living elsewhere leaves 50% exempt. Asserted.
8. **A house "ordinarily used for holiday accommodation" is not a private residence.** So it is not private residential property, whoever lives in it at the taxing date. Asserted.
9. **Aggregation raises the tax (s 11(1)).** A $650,000 rental and a $400,000 block held by one person are taxed on $1,050,000: **$2,200**. Taxed separately they would cost $875 + $300. An exempt home drops out of the aggregate. Jointly owned land is a separate assessment (s 12(3)). Every joint owner can be made to pay the whole of it (s 7(4)). Asserted.
10. **Taxable value is the lesser of the unimproved value and the capped value (Glossary clause 6).** The capped value is a "prescribed percentage" of last year's taxable value. The regulations that prescribe it are not deposited, so the 110% in the cases is illustrative. A lot created by subdivision in the previous year loses the cap. Asserted.
11. **The estate gets one more year, and only one (s 23).** That is the assessment year after the financial year of death, and only if no rent or income is derived before it ends. Asserted.
12. **Deadlines the owner meets:**
    - tax due on the 49th day after an original assessment notice (s 6(1));
    - errors in the notice reported by its due date, or within 21 days if it gives none, with a maximum fine of $5,000 (s 9A);
    - 60 days to appeal to the Minister against a refused or revoked s 20 exemption, and the tax is still payable meanwhile (s 20(4), (5));
    - a required report of a change affecting an exemption due no later than 30 September in the following financial year (s 20A(4)).

    Asserted.
13. **War widows and widowers get $10,000 off.** s 40 exempts "the first $10 000 of the value of the land on which land tax would otherwise be payable". Asserted.

## What would need doing before this is worth anything

- Deposit the regulations that prescribe the capped-value percentage, and bring them in.
- Check the s 21 partial-exemption inference (finding 7) and the joint-owner reading of ss 24 and 24A ("owned by an individual") against RevenueWA practice or a decision.
- Model several lots used as one home (Glossary clause 2(4)–(5)) and the partial use of a home for business (s 18(2)–(3), s 20(1)(a)).
- Add ss 22, 23A, 25, 25A, 27A and the subdivision rules if a life meets them.
- Add the Taxation Administration Act 2003 machinery (objections, interest, penalty tax) as its own encoding.
- Run the Legalese Studio stages this baseline skipped: Resolve, Refine and Test, an independent test pass, and the human gates.
