# Emergency Services Levy Act 2002 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `esl-levy.l4`: the module. It covers the Act's one operative section and the Part 6A rules of the Fire and Emergency Services Act 1998 that the land owner meets: whether the land is leviable, who is liable, how the amount is worked out, the notice, the due date, interest, buying and selling, sale and caveat for unpaid levy, and objections.
- `esl-cases-levy.l4`: the worked cases, built by the scratchpad generator `gen_wa_emergency-services-levy-act-2002_baseline.py`.

Conventions: a levy year is a financial year, named by the calendar year in which it ends (2029/30 is 2030); a day is the number YYYYMMDD.

## The split: what this Act does, and where the levy really lives

The Emergency Services Levy Act 2002 has three sections: short title, commencement, and s 3:

> "The emergency services levy determined under Part 6A of the Fire and Emergency Services Act 1998 is imposed."

That is all it does. It fixes no rate, no amount, no payer, no due date. It exists so that the levy is imposed as a tax by an Act that does nothing else. (Labelled INFERENCE: the reason for the separate Act is not stated in the deposit. The long title says only "An Act to impose the emergency services levy".)

Everything the owner meets is elsewhere:

| What | Where | In this encoding |
|---|---|---|
| The levy imposed | ESL Act s 3 | encoded (`Does the Emergency Services Levy Act itself fix how much levy I pay`: FALSE) |
| Which land, who is liable, how worked out, notice, due date, interest, recovery, sale, objection | Fire and Emergency Services Act 1998 Part 6A (ss 36B–36ZH), with ss 3 and 3A | **brought in**: deposited at `subjects/au/wa/fire-and-emergency-services-act-1998`, which has no encoding of its own |
| The rate in the dollar, the minimum and maximum, for each ESL category and purpose of use, each year | the Minister's Gazette determination under FES Act ss 36G–36I | **inputs**: indexed as `wa/emergency-services-levy-annual-determination`, text not deposited |
| The gross rental value | Valuation of Land Act 1978 (borrowed term) | a fact |
| Pensioner and senior rebates and deferments | Rates and Charges (Rebates and Deferments) Act 1992 | not encoded; asked as a fact where Part 6A defers to it |

So this baseline is, in substance, a baseline of FES Act Part 6A from the owner's seat, filed under the Act that imposes the levy, because that is where the life cites it.

## Edition

- **The Act.** The compilation of the Emergency Services Levy Act 2002 (No. 39 of 2002) deposited at `../../registers/source-bundle/mrdoc_24246.txt` (legislation.wa.gov.au mrdoc 24246, retrieved 2026-09-07). Its compilation table ends with the Fire and Emergency Services Legislation Amendment Act 2012 (No. 22 of 2012), which amended the long title and s 3.
- **Part 6A.** The Fire and Emergency Services Act 1998 (No. 41 of 1998) deposited at `subjects/au/wa/fire-and-emergency-services-act-1998/registers/source-bundle/mrdoc_49451.txt` (mrdoc 49451, retrieved 2026-09-07).
- **Not deposited.** The annual Gazette determination (rates, minimum, maximum, by ESL category area and purpose of use), the regulations that prescribe ESL categories (s 36F(1)) and exemptions (s 36D), and the Gazette interest rates (s 36S(2)). All are inputs or facts. The figures used in the cases (1.2 cents in the dollar, minimum $90, maximum $450, gross rental value $25,000) are **illustrative**, not the real determination.

## Checks

One case file: **39 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run esl-levy.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with two expected values altered (300 to 301, 20290531 to 20290530) was run. The runner reported both failures.

## Seat

**The land owner.** The life asks "What emergency services levy is charged on my home?", and Part 6A makes "the owner of leviable land" the person liable (s 36P(1)).

The Minister determines, the local government assesses and serves, the FES Commissioner recovers, applies for sale and lodges caveats. Those powers appear only as what they mean for the owner: is my land levied, am I liable, how much, how the notice comes, by when, what follows non-payment, and how to object.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed, with the necessary extension. The Act sets nothing; the instrument that does is Part 6A of the FES Act, which is deposited and brought in. The annual determination is not deposited, so its numbers are inputs.
- **The actors the text names.** Followed: the owner, joint owners, the local government, the FES Commissioner, the Minister, the Supreme Court, the State Administrative Tribunal.
- **A judgment handed to someone else is answered conditionally.** Followed. The Minister's determination (including any "other basis" under s 36H(3)), the declaration of ESL category areas, an extension of time to object, and the Supreme Court's order for sale are all inputs or conditions ("an application may be made", not "the land will be sold").
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed. Worked out: leviable land (s 3, ss 36B, 36D, 36E), owner (s 3A(a)(i), (d)), the levy year and its dates. Asked as facts: gross rental value (Valuation of Land Act 1978), whether land is in an ESL category area, whether the regulations exempt it, entitlement to a rebate or deferment under the 1992 Act.
- **One case is the text's natural unit.** Followed: one parcel of land for one levy year.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Left out: local government estimates and accounts (ss 36A, 36U–36Y), records (s 36C), the Minister's method (s 36G(3)–(5)), State land arrangements (ss 36L(1)(a), 36N), ESL agreements (Division 9), and the rest of the FES Act.

**Departures:**

- Dates are YYYYMMDD numbers and years are numbers, so that the tests are simple comparisons.
- Only owners under s 3A(a)(i) (Crown lessees) and (d) (Torrens proprietors, mortgagees in possession) are modelled; Crown land vested in or controlled by a body, the State, deeds-registered land and mining or petroleum holders are not.
- Partial exemption by regulation (s 36D(a)) is not modelled: only whole exemption.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c055** (2029-07-15), handover of the new Byford house: "council rates; the emergency services levy" | `Is my land leviable`, `Am I liable to pay the levy`, `How much levy is charged on my land`, `How will my levy notice come to me`, `Can I be made to pay all of the levy on land I own with others`, `What part of the year's levy is apportioned to me` | Leviable if Byford is in a declared ESL category area (assumed; the category is in the undeposited determination). Chloe and Liam, registered proprietors as joint tenants, are liable, each for the whole. For 2029/30 the levy is the rate in the dollar of the gross rental value in force at 1 July 2029, held between the minimum and maximum: at the illustrative figures, $300. It comes on the Shire's 2029/30 rate notice, payable to the Shire, not earlier than 35 days after issue. For the 2027/28 year in which the land settled (15 May 2028), the levy is apportioned day by day: 46 of 366 days. |

## Why this scope

The scope is what the event asks — who levies what on a new house, and how much — plus what any home owner meets afterwards: the notice and due date, instalments, interest, buying and selling land with levy outstanding, what can be done to land if the levy goes unpaid, and how to object.

Left out, because no owner in the lives meets them: local government finance, ESL agreements, State land, and the fees for emergency services and volunteer firefighter compensation elsewhere in the FES Act.

## What the Act turns out to say

1. **The Act does one thing: it imposes the levy.** s 3 imposes "the emergency services levy determined under Part 6A of the Fire and Emergency Services Act 1998". No rate, payer or date is in it. Asserted.
2. **The life cites sections that do not exist.** Chloe's facts cite the ESL Act "ss 5-7"; the Act has only ss 1–3. The index entry for the annual determination says the levy is imposed by "s 4"; it is s 3. Both citations should be corrected to ESL Act s 3 and FES Act Part 6A.
3. **The levy is on land, not on the house, and on all land in an ESL category area** (s 36B), unless the regulations exempt that kind of land (s 36D). Land outside every declared area pays nothing. Asserted.
4. **A general exemption in another law does not help.** An earlier Act exempting from "any rate, tax or imposition" never frees the owner; a later Act frees the owner only if it "expressly exempts a person from liability to pay the levy" (s 36E). Asserted.
5. **The owner pays, not the tenant, and not a lender out of possession.** s 3A(d): the Torrens proprietor, "except a mortgagee who is not a mortgagee in possession". A tenant of freehold land is not an owner (INFERENCE from the text). Asserted.
6. **Joint owners are each liable for the whole** (s 36P(3)), and a notice served on one is served on all (s 36J(3)). Chloe and Liam, as joint tenants, are each liable for all of it. Asserted.
7. **The amount is a rate in the dollar of the gross rental value at 1 July of the levy year** (s 36H(1)), raised to any minimum and cut to any maximum the Minister determines (s 36I), which apply "despite any other provision of this Part", so even to a levy set on "another basis" under s 36H(3). The rate may differ by ESL category area and by purpose of use (s 36G(4)). Asserted with illustrative figures.
8. **The rates must be gazetted before 31 May for the next levy year**, unless the Minister declares another day (s 36G(1)–(2)). A change in an area's category cannot take effect in the levy year its notice is published (s 36F(3)). Asserted.
9. **The levy arrives with the council rates.** The local government assesses it and serves notice "as part of the rate notice", or separately if no rate notice is given (s 36J(4)); it is paid to whoever served the notice (s 36P(2)). Asserted.
10. **It cannot fall due earlier than 35 days after the notice's issue date** (s 36M(2)), is payable in one payment unless instalments are approved or a payment agreement is made with the council (ss 36Q, 36R(2)), and interest runs from the due date unless the owner is entitled to a rebate or deferment under the 1992 Act or is of a prescribed kind (s 36S). Asserted.
11. **Buying land: the levy follows the land.** It is a charge on the land (s 36O); it can be recovered from "a person who becomes the owner of the land while the levy is unpaid" (s 36Z(1)(b)); between successive owners it is apportioned day by day (s 36T(1)(a)), and an owner must reimburse anyone else who paid it unless they agreed otherwise (s 36T(2)). None of this changes whom the council can pursue (s 36T(3)). Asserted.
12. **Unpaid for 3 years, the land can be sold.** After 3 years unpaid the FES Commissioner may apply to the Supreme Court for sale, after at least 6 months' newspaper notice and notice to the owner if their whereabouts are known (s 36ZC). While any levy is unpaid a caveat can be lodged (s 36ZD). Asserted.
13. **The only objection Part 6A gives is to the purpose of use**, and only where the rate or the minimum or maximum depends on it (s 36ZE(1)). It goes to the Minister in writing within 60 days of service of the notice, extendable by the Minister; then to the State Administrative Tribunal (s 36ZF). The levy remains payable meanwhile; an overpayment is refunded and an underpayment cannot be pursued for 30 days after the adjustment notice (s 36ZH). Objections to the gross rental value itself go under the Valuation of Land Act 1978, not here. Asserted (except the last sentence, which is from s 36ZH(1)(a) and not asserted).

## What would need doing before this is worth anything

- Deposit the annual Gazette determinations (categories, rates, minimum and maximum by purpose of use) and bring in the real figures; the Gazette is outside the WA Legislation site's CC BY licence, so this needs a licensing decision.
- Deposit and encode the FES regulations on ESL categories (s 36F(1)) and exemptions (s 36D), and the Rates and Charges (Rebates and Deferments) Act 1992 for pensioners and seniors.
- Correct the citations in Chloe's facts (ESL Act "ss 5-7") and in the annual-determination index entry ("s 4") to ESL Act s 3 and FES Act Part 6A.
- An independent test pass, a coverage table of Part 6A, and a human gate.
