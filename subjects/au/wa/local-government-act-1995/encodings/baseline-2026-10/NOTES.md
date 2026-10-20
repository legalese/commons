# Local Government Act 1995 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `lga-rates.l4`: the module. It covers Part 6 Division 6 (rates and service charges) as the ratepayer meets it: rateable land, the valuation basis, the amount, the rate notice, due dates and instalments, interest, recovery, action against the land, and objections.
- `lga-cases-rates.l4`: the worked cases, built by the scratchpad generator `gen_wa_local-government-act-1995_baseline.py`.

Conventions: a day is the number YYYYMMDD; money is in dollars; a rate in the dollar is a decimal (0.07 is 7 cents); an interest rate is a percentage a year.

## Edition

- **The Act.** The Local Government Act 1995 (No. 74 of 1995) deposited at `../../registers/source-bundle/mrdoc_49599.txt` (legislation.wa.gov.au mrdoc 49599, retrieved 2026-09-07). The deposit states no compilation date. The Part 6 amendment notes run to No. 7 of 2026 (s 6.26).
- **Not deposited.** No regulations are deposited. The numbers they set are therefore inputs or left out:
  - the maximum interest rate on overdue rates (s 6.51(2)): an input;
  - the maximum instalment charge (s 6.45(4)(e)): the charge itself is an input;
  - the method of calculating interest (s 6.51(5)): simple daily interest is ASSUMED, and labelled so;
  - the minimum payment limits across the district (s 6.35(4)): not encoded.
- **Not applied.** Note 1M records modifications to ss 6.13, 6.33-6.36, 6.45 and 6.51 by the Local Government (COVID-19 Response) Order 2020 (SL 2020/57). The Order is not deposited and is not applied.

## Checks

One case file: **70 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run lga-rates.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with two expected values altered (5600 to 5601, 235 to 236) was run. The runner reported both failures.

## Seat

**The ratepayer: the owner of rateable land.** The life events ask from this seat: "Who levies rates on my home?" Under s 6.44(1) the owner for the time being is the person liable, so the owner is the individual the Division is applied to.

Most of the Division tells the local government or the Minister what to do: impose, determine, notify, reassess, recover, sell. Those provisions appear only as what they mean for the owner:

- what may be charged;
- what notice the owner must be given, and by when;
- when the owner must pay;
- what may be done to the owner's land.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows. No regulations are deposited, so the prescribed numbers are inputs (see Edition). Each council's rates in the dollar, minimum payments and interest rate are budget decisions, not instruments: they are inputs too.
- **The actors the text names.** Followed: the owner, joint owners, successive owners, a lessee, an occupier, the local government, the Minister, the State Administrative Tribunal.
- **A judgment handed to someone else is answered conditionally.** Followed. The Minister's determination of the valuation method (s 6.28(1)) is asked as a fact. Where the owner does not know it, the answer is "gross rental value (or unimproved value), if the Minister's determination follows the general principle". The values are the Valuer-General's under the Valuation of Land Act 1978, and are inputs.
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: rateable land (s 6.26, for the ordinary cases), the general rates after a minimum payment, lawful due dates, reassessment, the objection route.
  - Asked as facts: "owner" (s 1.4, applied by s 6.25), "gross rental value" and "unimproved value" (Valuation of Land Act 1978), and entitlement to a rebate or deferment (Rates and Charges (Rebates and Deferments) Act 1992).
- **One case is the text's natural unit.** Followed: one parcel of rateable land for one financial year.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Budgets, funds, borrowing and the district-wide limits (ss 6.34, 6.35(2)-(6)) are out.

**Departures:**

- Dates are YYYYMMDD numbers, with a day-count function written in L4, so that the 35-day, 28-day and 2-month tests are simple comparisons.
- The rebates and deferments are pointed to, not encoded, as instructed. They live in the Rates and Charges (Rebates and Deferments) Act 1992, deposited beside this subject. Only the effect this Act gives them is encoded: no interest and no instalment charge (s 6.51(4)).

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c055** (2029-07-15), handover of the new Byford house: "Who levies what on a new house?" | `Who levies rates on my home`, `Is my land rateable`, `On what valuation is my land rated`, `Which valuation are my rates worked out on`, `How much are my general rates`, `Am I paying the minimum payment`, `Must my rates be reassessed`, `How may I pay my rates`, `Is my due date lawful`, `Where does my complaint go`, `What share of the year's rates is mine as buyer` | The local government of the district levies the rates. The lot is rateable, vacant or built on. On non-rural land the basis is gross rental value, conditionally, unless the Minister's determination says otherwise. An interim valuation after completion is used (s 6.28(5)). The changed rateable value forces a reassessment and a new notice (s 6.40(1)(a)). Chloe may then pay in one sum or by the instalments remaining (s 6.45(2)). With illustrative figures, the vacant lot pays the $1,500 minimum and the house $2,600. |
| Daniel **d084** (2064-01-15), council rates in Nedlands | `Am I liable to pay the rates`, `Can I be made to pay all the rates on land I own with others`, `On what valuation is my land rated`, `How much are my general rates`, `How much is each instalment`, `Does interest run on my overdue rates`, `Where are the pensioner and seniors rebates and deferments` | Daniel and Priya are liable jointly and severally. With an assumed determination on gross rental value, an illustrative $80,000 at 7 cents gives $5,600, or 4 instalments of $1,405 with a $20 charge. Interest on late rates runs only if the council resolved it when imposing the rates, and not at all if either is entitled to a rebate or deferment under the 1992 Act. That entitlement is asked both ways. |

## Why this scope

The scope is what the two events ask, plus what any ratepayer meets in a year of rates. That means who levies, on what valuation, how much, when due, by what instalments, what happens when payment is late, and how to object.

Recovery and action against the land (ss 6.56-6.69) are in because they say what can be done to the owner.

Left out:

- the budget and funds (Divisions 1-5);
- mining and petroleum interests;
- the phasing in of valuations (Schedule 6.1);
- the district-wide limits on minimum payments and the general rate yield;
- how specified area rates and service charges must be spent;
- the procedure for leasing, sale and transfer (Schedules 6.2 and 6.3);
- the emergency services levy and water charges, which c055 also cites but which come under other Acts.

## What the Act turns out to say

1. **The Act does not choose gross rental value or unimproved value for a home.** The Minister determines the method by Gazette notice (s 6.28(1)). The Act gives only a "general principle" the Minister must have regard to: unimproved value for land used predominantly for rural purposes, gross rental value for non-rural use (s 6.28(2)). A determination governs even against that principle. Asserted.
2. **A minimum payment replaces the rate in the dollar; it is not added to it.** s 6.35(1) allows a minimum payment "greater than the general rate which would otherwise be payable", so the owner pays the greater of the two. Chloe's vacant lot at an illustrative $900 of general rate pays the $1,500 minimum. Asserted.
3. **Building the house changes the rates during the year, but changing the land's category does not.** s 6.28(5) uses an interim valuation made during the year. s 6.40(1)(a) then requires a reassessment and a notice to the owner. s 6.33(4) forbids amending the assessment merely because the differential-rating characteristics changed, but expressly not where the rateable value changed. After a reassessment the owner may pay by the instalments remaining (s 6.45(2)). Asserted.
4. **No rates can fall due less than 35 days after the notice's issue date (s 6.50(2)).** Instalments after the first must be at least 2 months apart (s 6.50(3)). Each instalment notice must come at least 28 days before the instalment is due (s 6.41(2)(b)). Asserted.
5. **Interest is not automatic.** It runs only if the council resolved it "at the time of imposing" the rates, at the budget rate, capped by a prescribed maximum (s 6.51(1), (2)). Asserted.
6. **This is where the rebates connect.** A person entitled to a rebate or deferment under the Rates and Charges (Rebates and Deferments) Act 1992 is charged no interest and no instalment charge (s 6.51(4)). The due date (s 6.50(1)(c)), the charge on the land (s 6.43), discounts and concessions (ss 6.46, 6.47) and recovery (s 6.55(1)) are all "subject to" that Act. The rebates themselves are not in this Act. Asserted for s 6.51(4).
7. **A valuation cannot be objected to under this Act.** s 6.80 sends valuation objections to the Valuation of Land Act 1978. The s 6.76 grounds are narrow: the wrong owner or occupier, land not rateable, or the wrong differential characteristics. A complaint that the rate in the dollar is too high has no objection route. The only routes are a submission when differential rates are proposed (21 days, s 6.36(3)) or a general-interest reference to the State Administrative Tribunal (s 6.82). Asserted.
8. **An objection does not stop the bill.** Liability continues pending the objection (s 6.81). The objection must be in writing, made within 42 days of service of the rate notice, by the owner named in the record or their agent or attorney (s 6.76(2), (3)). Review in the State Administrative Tribunal must be sought within 42 days (s 6.77). Asserted.
9. **A notice can be served without being received.** Delivery to the address in the rate record is deemed service (s 6.41(3)). Email needs the owner's consent (s 6.41(4)). Not asserted (encoded).
10. **Buyer and seller share the year's rates by the day (s 6.52(1)(a)), but the council is not bound by that (s 6.52(3)).** A buyer who takes title while rates are unpaid can be pursued for them (s 6.55(1)(ii)). They are a charge on the land (s 6.43). Asserted.
11. **After 3 years unpaid the council may take possession and lease, sell or transfer the land (s 6.64(1)).** It may lodge a caveat as soon as rates are in arrears (s 6.64(3)). An owner may stop a sale by paying up to 7 days before it; after that, only on terms the council accepts (s 6.69). Asserted.

## What would need doing before this is worth anything

- Deposit the Local Government (Financial Management) Regulations 1996, and bring in the prescribed maximum interest rate, the maximum instalment charge, the method of calculating interest and the minimum payment limits.
- Deposit the Minister's valuation-method determinations (Gazette notices) for the districts in the lives, so that the valuation basis is a lookup rather than a conditional answer.
- Encode the Rates and Charges (Rebates and Deferments) Act 1992 as its own encoding, and link its entitlement to the `I am entitled to a rebate or deferment` input here.
- Check whether the COVID-19 Response Order modifications still have any effect.
- Run the Legalese Studio stages this baseline skipped: Resolve, Refine and Test, an independent test pass, and the human gates.
