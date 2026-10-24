# Land Tax Act 2000 (Tas), with the Land Tax Rating Act 2000, the Land Tax Regulations 2021, and the Local Government (Rates and Charges Remissions) Act 1991 and Regulations 2024: baseline encoding

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18 and the brief for the tax-and-benefits encodings of 24 October 2026. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.

There was no pipeline, no coverage table and no human gate. An independent verifier reviewed the encoding on 2026-10-24 and raised five issues; all five were checked against the deposited texts, found real and fixed the same day (findings 1 and 23-26). Not for public use as advice.

**The Remissions Act and its Regulations are encoded here.** The Local Government (Rates and Charges Remissions) Act 1991 and the Local Government (Rates and Charges Remissions) Regulations 2024 have no encoding folder of their own: their rules are in `rcr-core.l4` in this folder. The reason is the jurisdiction README's own pairing. These are the two yearly charges on a home that a resident owns, and both are relieved by a Commonwealth card. Both fix eligibility on 1 July. Both relieve a card-holding pensioner on their principal residence. The rates remission is enforced by the Commissioner of State Revenue (ss 4B-4F), as land tax is. Cross-folder IMPORT does not work, so one folder lets one seat layer ask both sets of questions. The Land Tax Rating Act 2000 and the Land Tax Regulations 2021 are brought in the same way, because they hold the numbers.

The encoding has two layers:

- **A seat-neutral core** in the instruments' own actors and terms: the owner (s 3A), the related person, the taxpayer, the Commissioner of State Revenue, the eligible pensioner who applies, the municipality, the person given a remission, the surviving spouse and the objector. Where the text says "must" or sets a deadline, the rule is regulative (`DEONTIC`, `PARTY ... MUST/DO/SHANT ... WITHIN ... HENCE ... LEST`). There are 11 such rules. Computations (the land tax, the s 7 rounding, the maximum remission and the amount remitted) are functions.
- **A seat layer** (`lta-seat.l4`) that asks the owner's questions with plain inputs. It builds the core's records and restates no rule.

| File | What it holds |
|---|---|
| `lt-common.l4` | Arithmetic and date helpers, the financial year, the "not covered" answers, and the parties and steps of every regulative rule |
| `lta-core.l4` | Core: Land Tax Act ss 3A, 3B, 6, 7, 8, 10, 11(3), 11(5)-(6), 11A, 13, 14, 16, 19(a)-(b), 20, 23, 24, 26, 27, 37, 37A, 37B; Land Tax Rating Act ss 4-7 and Schedule 1; Land Tax Regulations reg 5; the edge of the encoded amount (Div 1A and the other exemptions, answered `not covered`). Six regulative rules (ss 10(2), 11(5)-(6), 13, 16, 37, 37A) |
| `rcr-core.l4` | Core: Remissions Act ss 3, 4(1)-(9), 4A, 4B, 4C, 4E, 4F; Regulations 2024 regs 4, 5, 6. Five regulative rules (s 4(1)-(1A), s 4(9), s 4A, s 4B, ss 4C-4F) |
| `lta-seat.l4` | Seat layer: 33 exported questions, `@desc` on every input, under `§§` headings in the order of the instruments |
| `lta-cases-core.l4`, `rcr-cases-core.l4` | Cases for the two core modules, with `#TRACE`s for the regulative rules |
| `lta-cases-seat.l4` | Cases for the seat layer, asked with plain answers. Several use the same facts as the core cases and must agree with them |

A financial year is named by the year in which it **begins** on 1 July: 2026 is 2026-27.

## Edition

All five texts are the consolidations that the Tasmanian Legislation website served as current at point in time 2026-10-20. They were retrieved on 2026-10-19 (UTC) and deposited on 2026-10-20.

| Instrument | Source id | Version published | Deposited at |
|---|---|---|---|
| Land Tax Act 2000 | act-2000-074 | 2026-10-14 | `../../registers/source-bundle/act-2000-074.txt` |
| Land Tax Rating Act 2000 | act-2000-073 | 2024-07-12 | `../../../land-tax-rating-act-2000/registers/source-bundle/act-2000-073.txt` |
| Land Tax Regulations 2021 | sr-2021-096 | 2021-12-01 | `../../../land-tax-regulations-2021/registers/source-bundle/sr-2021-096.txt` |
| Local Government (Rates and Charges Remissions) Act 1991 | act-1991-008 | 2019-05-23 | `../../../local-government-rates-and-charges-remissions-act-1991/registers/source-bundle/act-1991-008.txt` |
| Local Government (Rates and Charges Remissions) Regulations 2024 | sr-2024-055 | 2024-10-16 | `../../../local-government-rates-and-charges-remissions-regulations-2024/registers/source-bundle/sr-2024-055.txt` |

**Years covered.**

- **Land tax: from 2026-27.** The deposited Land Tax Act shows ss 13 and 37 as amended by No. 19 of 2026 (applied 1 July 2026), but not their earlier wording. Schedule 1 to the Rating Act was last amended from 1 July 2024 (No. 5 of 2024). So 2026-27 is the first year for which every encoded provision is the deposited one. Any land tax question about an earlier year answers `not covered`, and this is asserted.
- **Rates remission: from 2024-25.** The 2024 Regulations set the 2024-25 base. A year before 2024-25 answers `not covered`. This matters for a s 4(1D) claim reaching back into 2023-24, and is asserted.

**Inputs the deposit does not hold:**

- the land value (s 23: the Valuer-General's valuation, with any adjustment factor);
- the Hobart CPI March-quarter figures for reg 5 (ABS). The case files use **illustrative** figures: 137.1, 139.3, 142.0 and 145.5 for March 2024 to March 2027;
- the value of a penalty unit, so penalties are answered in penalty units.

**The reg 5(2) formula.** It appears in the source only as an image. It was transcribed at deposit as "A = B × (C / D)", and that is what is encoded. It should be checked against the image (README, "Formulas shown as images").

## Checks

`l4 run` on every `.l4` in the folder gives **0 errors and 0 warnings**, with **373 assertions written and 373 satisfied** (2026-10-24, after the fixes; 335 of 335 before them).

| File | Assertions | `#TRACE`s (each with an `-- expect:` line, read and as expected) |
|---|---|---|
| `lt-common.l4`, `lta-core.l4`, `rcr-core.l4`, `lta-seat.l4` | (modules) | each runs clean on its own |
| `lta-cases-core.l4` | 153 | 7: five breaches by the owner (late payment, a late s 11(6) statement, the s 13 instalment path twice, late s 16 notice) and two pending obligations of the Commissioner to grant a rebate (s 37, s 37A) |
| `rcr-cases-core.l4` | 104 | 5: the municipality's obligation to remit, pending after an application on 30 March; a breach of s 4(9) (notice on 1 July); a breach of s 4A; the s 4B obligation to repay, pending (no period is set); the Commissioner's obligation to determine an objection, pending |
| `lta-cases-seat.l4` | 116 | none |

**Control.** A copy of `lta-cases-core.l4` with one expected value altered ($1,017.50 to $1,017.60) was run. The runner reported that assertion as failed, and the copy was then deleted. After the fixes, a copy of `lta-cases-seat.l4` with two new expected values altered (the foreign owner's nil home to $1, and the 2024-25 maximum with no CPI figures to $379.42) reported exactly those two assertions as failed, and was deleted.

**Expected values.** Each was worked by hand from the deposited texts. The arithmetic of Schedule 1, Rating Act s 7 and reg 5 was checked in an independent calculator, `au-tas-4/hand.py` in the session scratchpad, written from the statutory words with exact fractions. No value was copied from the encoding's output.

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

## Seat

**The individual who owns land in Tasmania and pays council rates on it.** That covers a home owner, a joint owner, the owner of a shack or of investment land, and a pensioner or a pensioner's surviving spouse. The personal representative or beneficiary asking about a deceased sole owner's home (s 6(10)-(12)) is in the same seat. The questions are the ones that person asks:

- "Do I pay land tax this year on my home, my shack or my rental, and how much?"
- "Is my land exempt because I hold a pensioner card?"
- "Can I get a rebate for building, or for moving between two homes, and by when must I apply?"
- "What remission do I get on my council rates and charges this year, and by when must I apply?"
- "What must I tell the council, and when?", and also "What must I tell the Commissioner?", including the statement of interest the Commissioner may ask a new owner for (s 11(5)-(6)).

**No other seat.** The Commissioner of State Revenue and the municipality are parties to rules, never seats. Their duties (to grant a rebate, to remit 30%, to determine an objection) appear as regulative rules, for what they mean to the owner. The text puts real duties on no other private party within this scope.

How each default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The Rating Act and the two sets of Regulations are brought in. The Remissions Act is a second Act, folded in by the task's plan (see Method).
- **The actors the text names.** Followed.
- **A judgment handed to someone else is answered conditionally.** Followed. These are answered as "yes, if the Commissioner is satisfied of these facts":
  - adjoining land (s 6(2));
  - the rebates (ss 37(3), 37A(3));
  - the disaster extension (s 37B(4));
  - repayment of a remission (s 4B).

  Section 36 puts the onus on the owner, and until the owner establishes the facts the Commissioner is to treat the land as general land (s 36(2)). Every answer assumes the owner has established the facts given.
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: owner (s 3A), the joint tenancy shares (s 3B), the Help to Buy disregard (s 11A), principal residence land (s 6), primary production land (s 7), general land (s 8), qualifying home business (s 3), the s 26(2A) land area, eligible pensioner (reg 4), prescribed institution (reg 6), occupying as a principal dwelling (s 4(3)), and the maximum remission (reg 5).
  - Asked as facts: related person and spouse (Relationships Act 2003); Pensioner Concession Card and Health Care Card (Social Security Act 1991); special rate pension and TPI (Veterans' Entitlements Act 1986 s 24); war widow(er) (VEA s 30(1), MRCA s 12); MRCA s 199; retirement village; Help to Buy arrangement (Help to Buy Act 2024); water and sewerage customer (Water and Sewerage Industry Act 2008, indexed only); residential care (Aged Care Act 1997 s 41-3); nursing-home type patient (Health Insurance Act 1973 s 3).
- **One case is the text's natural unit.** Followed: one taxpayer's land for one financial year. Joint owners are one taxpayer (s 14(2)(a)). For the rates, one property and one financial year.
- **The Act's own terms, each with a plain gloss.** Followed. The comments quote the statutory words, and each seat `@desc` glosses them.
- **Operative sections in; machinery out.** Followed.

**Departures and simplifications in the seat layer:**

- The amount question takes the home, the shacks together and the rentals together as three parcels, because s 24 aggregates them anyway. It does not ask about a s 37B extension for other land (taken as no). The principal residence question asks it.
- The amount question also asks two facts that mark the edge of the encoding: whether an owner is a foreign person within s 16C(1)(b), and whether any of the land is exempt on a ground other than s 19(a)-(b). Either can make it answer `not covered` (finding 24).
- The pensioner exemption question asks the share facts plainly (the share held, the number of joint tenants, any Help to Buy share) and has the core's 50% test count them (finding 26).
- The rates application question asks the card facts once, for 1 July, and takes them to hold on the day of applying too. Its single "in a facility" answer stands for any of the three reg 6 institutions, which s 4(3) treats alike.
- The remission and repayment questions take "eligible and living there on 1 July" as one answer for each year, worked out by the eligibility and application questions.

## Scope

**In.**

*Land Tax Act 2000:*

- ss 3 (the definitions used), 3A(1)-(2), 3B, 11A: the owner and the interest counted;
- s 6(1), (2), (8), (9)-(12): principal residence land, adjoining land, retirement villages, and the year after a sole owner's death;
- ss 7, 8: primary production land and general land;
- s 10(1)-(2), with s 39(10) for the "relevant day": who is liable, and when the tax is due;
- s 11(3): ownership changes on completion;
- s 11(5)-(6): a person served with the Commissioner's notice must state their interest in the land by statutory declaration lodged within 14 days, as a regulative rule (finding 25);
- s 13: instalments, with s 13(2) as a regulative rule;
- s 14(1)-(2): joint owners;
- s 16: notice of a change within 30 days, as a regulative rule;
- s 19(a)-(b) with Land Tax Regulations reg 5: the pensioner exemption;
- ss 20, 23 (the value an input), 24(1)-(1A): the amount and aggregation;
- s 26 with s 3 "qualifying home business", and s 27: apportionment;
- s 37 and s 37A, as regulative rules; s 37B.

*Land Tax Rating Act 2000:* ss 4, 5, 6, 7 and Schedule 1.

*Remissions Act 1991:* s 3; s 4(1)-(9), with s 4(1)-(1A) and s 4(9) as regulative rules; s 4A, s 4B and ss 4C, 4E, 4F, as regulative rules.

*Remissions Regulations 2024:* regs 4, 5, 6.

**Out.**

- Foreign investor land tax (Div 1A; Rating Act s 6A), including the s 16J notice. Where an owner is a foreign person within s 16C(1)(b) and the land includes general land, the amount answers `not covered` (finding 24).
- Trusts, companies and home-unit companies: s 6(3)-(5), s 24(2)-(4), ss 28, 31-35, Div 5, and s 37(1)(b)(ii).
- Cooperative housing societies (s 30).
- Crown, trust, retirement village and other exempt land: ss 17, 18, 19(ba)-(e), 19A-19EA, 29, 30A. Where any of them reaches the land, the amount answers `not covered` (finding 24).
- s 11(1) and (4): the Commissioner's list of owners and the Valuer-General's details of valuations (machinery).
- Subdivisions: ss 23(2), 25.
- The special rate (s 38) and recovery (ss 39-40), apart from the s 39(10) "relevant day" that s 10(2) borrows.
- Assessment and reassessment (s 12).
- Land Tax Regulations reg 4 (owners of land not under the Land Titles Act 1980).
- The Taxation Administration Act 1997 (Tas), which s 9 applies to land tax: objections, interest and penalty tax on land tax are not answered.
- In the Remissions Act: s 4D, the late objection (as a note: it needs the Commissioner's permission on a written application with detailed reasons, and a refusal is final); ss 4G-4I (investigations); ss 5, 6 (reimbursement of the municipality, Treasurer's directions); s 8.

There is no Tasmanian requirement ledger and no Tasmanian scenario life, so no ledger line is closed and no life event is cited.

## Links to other encodings

Cross-folder IMPORT does not work. These are links in the notes only.

- **Social Security Act 1991 (Cth):** `../../../../social-security-act-1991/encodings/baseline-2026-10/` and `../naive-2026-10/`.
  - The Pensioner Concession Card (land tax s 19(a)(i); reg 4(2)(a)-(b)) and the Health Care Card (reg 4(2)(c)) are issued under that Act. Holding one is an input here.
  - Neither SSA encoding answers card eligibility yet. A grep of their modules and notes finds no "concession card" or "health care card".
- **Veterans' Entitlements Act 1986 (Cth):** `../../../../veterans-entitlements-act-1986/encodings/baseline-2026-10/`.
  - The special rate pension under s 24 (land tax s 19(b); reg 4(1) "totally and permanently incapacitated person") and the war widow(er)'s pension at the s 30(1) rate (reg 4(1)). Both are encoded there.
  - The Repatriation Health Card - For All Conditions (Land Tax Regulations reg 5), and a Pensioner Concession Card issued as a VEA fringe benefit.
- **Military Rehabilitation and Compensation Act 2004 (Cth):** `../../../../military-rehabilitation-and-compensation-act-2004/encodings/baseline-2026-10/`.
  - Section 199, which makes a person "totally and permanently incapacitated" for reg 4, and section 12, for a wholly dependent partner as a war widow(er) for reg 4.
  - Its notes do not mention either section, so both are inputs here.
- **Aged Care Act 1997 (Cth):** cited in reg 6(a). There is **no subject** for it under `subjects/au/`; the task said one exists, but it does not.
  - `../../../../aged-care-act-2024/encodings/baseline-2026-10/` encodes its successor.
  - `../../../../aged-care-consequential-and-transitional-provisions-act-2024/` repeals the 1997 Act (finding 18).
- **Health Insurance Act 1973 (Cth):** `../../../../health-insurance-act-1973/encodings/baseline-2026-10/`. A "nursing-home type patient" (s 3) is cited in reg 6(b).
- **Help to Buy Act 2024 (Cth):** `../../../../help-to-buy-act-2024/` (subject, text deposited, no encoding). A "Help to Buy arrangement" is the term s 11A borrows.
- **Tasmania:**
  - `../../../duties-act-2001/`: the pensioner duty concession turns on the same Commonwealth cards.
  - `../../../first-home-owner-grant-act-2000/`: like s 11A, it carves Help to Buy out of its joint-owner rules.
  - `../../../water-and-sewerage-industry-act-2008/` is indexed only; "customer" is a fact here.

## What the Acts turn out to say

1. **Section 19(a)-(b) changes the amount payable only where the home or farm is apportioned (the finding asked for).**
   - Rating Act ss 4 and 5 rate principal residence land and primary production land at nil, including their share of an apportioned parcel. So for a home or farm wholly used as such, s 19 changes nothing: the pensioner's home pays nil with or without it.
   - It changes the amount where part of the parcel is used for something else (s 26 or s 27). Section 26(1) apportions "the land value of the land", and the land stays principal residence land under s 6(1). Section 19 says land tax "is not payable in respect of" that land. Read literally with s 10(1), which charges only land "that is not exempt land", nothing is payable on the parcel. That includes the part apportioned to general land, and that part is no longer aggregated with the owner's other general land.
   - Example: a $400,000 home with a shop on 70 of its 700 m² of land area (s 26(2A)), plus a $300,000 rental. That is $1,017.50 without the card and $837.50 with it, $180 less. A $500,000 home with 30% used otherwise pays $162.50 without the card and nil with it.
   - The contrary reading confines the exemption to the principal residence part. On that reading s 19 is redundant for the amount payable. One constant switches between the readings (`READING: s 19 exempts the whole parcel ...`).
   - On either reading s 19 is not idle: it makes the land "exempt land", so losing the card is a change the owner must notify within 30 days under s 16(a) (finding 21).
   - **The case for each reading** (weighed after the independent verification of 2026-10-24, which pointed out that the first version gave only one side):
     - *For the whole parcel (the default):* s 26(1) starts from land that is principal residence land and "is used for other purposes", and apportions its value, not the land; s 19 says land tax "is not payable in respect of" that land, and s 10(1) charges only land "that is not exempt land"; where the Act means an exemption to reach only part of a parcel it says so, apportioning "between exempt land and general land" (ss 19A(2), 19B(2), 19C(2), 29, 30A), and s 19(a)-(b) has no such words; and s 16A(2)(a) has to provide that, for Division 1A, "a reference to general land includes a reference to" a part apportioned as general land, which suggests that elsewhere the part is not general land in its own right.
     - *For the principal residence part only:* s 26(1) apportions the value "between principal residence land and general land", so the Act itself names the apportioned part general land; Rating Act s 6(2) provides that the land tax "in respect of the apportioned assessed land value in respect of any general land is to be calculated in accordance with Schedule 1", in mandatory terms and with no exception for exempt land; and s 16A(2)(a) treats that part as general land, if only for Division 1A. The redundancy this reading gives s 19 is answered by s 19's other work (exempt land status, s 16).
     - Neither side is conclusive on the deposited text, so the default is kept, flagged and listed for settling below.
   - On the contrary reading the examples become $1,017.50 with the card as without it, and $162.50 for the $500,000 home. The core works the parcel's general land value out on either reading (`the value of the parcel that is general land, on the reading`), and the cases assert both.

   Asserted both ways.
2. **Different cards open the two concessions.**
   - Land tax (s 19, reg 5) needs one of: a Pensioner Concession Card; the DVA gold card with a war widow(er) endorsement; or the VEA special rate pension together with total and permanent incapacity.
   - The rates remission (reg 4) needs one of: a Pensioner Concession Card (even while inoperative abroad); a Health Care Card; total and permanent incapacity under VEA s 24 or MRCA s 199; a VEA s 30(1) war widow(er)'s pension; or MRCA s 12 dependency.
   - So a Health Care Card holder, an MRCA s 199 veteran and an MRCA dependant partner get the rates remission but not the land tax exemption, unless they also hold a Pensioner Concession Card.
   - A special rate pensioner not found totally and permanently incapacitated gets no land tax exemption.

   Asserted.
3. **Three equal joint owners who all live in their home pay land tax on it.** Section 3B treats joint tenants as tenants in common in equal shares. Section 6(1) needs "an owner of at least a 50% interest" (or a related person of one) to live there.
   - Three siblings with a third each: no one holds 50%, so the home is general land. A $400,000 home pays $1,287.50.
   - Two joint tenants hold 50% each and qualify.

   Asserted.
4. **Help to Buy (s 11A).** The Act does not say how the other interests are measured once the Commonwealth's or Housing Australia's interest is left out of account. The reading taken makes the remaining interests the whole.
   - A couple holding 70% as joint tenants, with Housing Australia holding 30%, have 35% of the land each, which counts as 50% each. Their home is principal residence land.
   - Without s 11A neither would hold 50%, and the home would be general land. The reading is the one that gives s 11A effect for the 50% tests.

   Asserted.
5. **The general land scale has a $50 step at $125,000.** $124,999 pays nil and $125,000 pays $50. The two upper bands meet exactly at $500,000: $50 + 0.45c × 375,000 = $1,737.50, the figure in item 3. Asserted.
6. **Section 7 rounds to 10 cents, and 5 cents rounds down.** $50.45 becomes $50.40; 5.4 cents remaining rounds up. Reading: "the number of cents remaining" keeps any fraction of a cent. Section 13's "exceeds $500" is applied to the rounded tax:
   - $225,011 of general land gives $500.0495, rounded to $500.00: no instalments;
   - $225,012 gives $500.054, rounded to $500.10: instalments may be accepted.

   Asserted.
7. **Aggregation and joint owners.** Section 24(1) aggregates an owner's parcels of the same class. A $200,000 shack and a $300,000 rental pay $1,737.50 together, against $387.50 + $837.50 = $1,225 apart. Two readings are taken:
   - the general land part of an apportioned home is aggregated with the owner's other general land;
   - joint owners, "a single taxpayer" (s 14(2)(a)), are assessed apart from land any one of them owns alone. This one is a constant.

   Each joint owner is liable for the whole tax (s 14(2)(b)). Asserted.
8. **Facts are taken at 1 July.** Sections 6(1) and 19 name no date. They are read with s 10(1) (the owner at the commencement of the financial year) and s 20(1)(a) (the value as at 1 July). Card or residence facts arising on 2 July count only from the next year. The rates remission tests eligibility on 1 July in terms (s 4(1A), (1C), (1D)).
9. **Land that is both principal residence land and primary production land.** The Act does not rank the two classes; the encoding reports principal residence land. Both are rated nil and both are reached by s 19, so no amount turns on it.
10. **Settlement on 1 July.** Section 10(1) charges "the owner ... as at the commencement of the financial year", and s 11(3) makes a change of ownership take effect on completion. Reading: completion on 1 July comes after the commencement of that day, so the seller is liable for that year and the buyer is not. Under s 10(2) the tax falls due on the Commissioner's date, or on the day a sale is completed if that is earlier. Asserted.
11. **The maximum remission is rounded twice.** Regulation 5(2) rounds A to the cent and then to the dollar.
    - With the illustrative CPI, 379.41 × 139.3 / 137.1 = 385.4983. That rounds to $385.50 and then to **$386**; rounding straight to the dollar would give $385.
    - The 2024-25 base figures ($379.41 and $558.50) are not whole dollars. With no CPI change, the 2025-26 figure stays $379.41 under reg 5(3) rather than rounding to $379.

    Asserted.
12. **What B carries forward when reg 5(3) applies.** B is "the maximum amount, before rounding, that could be remitted" in the preceding year. Reading: when reg 5(3) keeps the preceding year's maximum, B carries that year's unrounded figure too.
    - Illustrative case: the CPI falls to 138.5 in March 2026, then rises to 141.0. The 2026-27 maximum stays $386, and 2027-28 is **$392**.
    - Carrying the lower computed figure (383.2844) would give $390.

    Asserted.
13. **The s 37 building rebate:**
    - Section 37 sets no time limit for applying. The Taxation Administration Act 1997 is not deposited.
    - The occupier must not have owned other principal residence land "during that financial year". So an owner who builds and moves out of a home they still owned at 1 July gets no s 37 rebate.
    - Section 37A then needs one of the two to have been bought in the 3 months before 1 July. A builder who bought the block earlier and sells the old home in the year may get neither rebate.

    Asserted for s 37.
14. **The rates application deadline is 30 March.** "Before 31 March in a financial year" makes 30 March the last day. An application from 31 March to 30 June is not made "before 31 March" in that year. Applying from 1 July instead loses nothing for an applicant still eligible: s 4(1D) brings back the year just missed (applied 1 July 2027, remitted 2026-27 and 2027-28). Asserted.
15. **Regulation 4(a) and (b).** Paragraph (b) adds a current card "inoperative because the person is temporarily out of Australia". So (a) is read as a card in operation, and a card inoperative for another reason does not count.
16. **Section 4(1D) and (1C):**
    - Section 4(1D) needs only an application under s 4(1) and eligibility on the previous 1 July. It remits the previous year even where s 4(1A) refuses the year of application, for example where the pensioner left the home before 1 July but is still liable for the rates.
    - Reading: once s 4(1C) ends the remission, it does not revive without a fresh application.

    Asserted.
17. **Section 4(3C) limits remissions while in care.** A remission while in a prescribed institution, for a single person or for both spouses, runs for at most 2 consecutive financial years. The third is refused; that is the reading of the count. The limit does not reach a person in care whose spouse still lives at home (s 4(3)(b)(ii)). A statutory declaration is required (s 4(3A)-(3B)). Asserted.
18. **Regulation 6(a) cites a repealed Act.** It refers to s 41-3 of the Aged Care Act 1997 (Cth).
    - The deposited Aged Care (Consequential and Transitional Provisions) Act 2024 repeals "the whole of" that Act (Sch 3 item 1), from the commencement of the Aged Care Act 2024: 1 November 2025, per its commencement table.
    - Its s 4 maps references in "another Act" to the 2024 Act. Whether that reaches a Tasmanian regulation is not settled here.
    - No subject for the 1997 Act exists under `subjects/au/`. Living in residential aged care is asked as a fact.

    Not asserted.
19. **Section 37A(3)(a) needs either home, not both, to have been acquired in the 3 months before 1 July.** The text reads "became the owner of the principal residence land or the other land". The task brief summarised it as both homes. Asserted both ways: the new home bought in May, and the new home bought and moved into in May while the old home is the one left.
20. **The s 37A timing.** The sale contract must be made "before 1 October", so 30 September is the last day. The application must be lodged after the buyer takes possession and no later than 30 September after the year ends. Applying on day 346 after possession, when the last day is day 345, is too late. Asserted, with traces.
21. **Two notice duties, on two clocks.**
    - Land tax s 16: written notice to the Commissioner within 30 days of the change, or a fine of up to 10 penalty units.
    - Rates s 4(9): written notice to the council before the end of the financial year (30 June), or up to 2 penalty units. Section 4A also carries up to 2 penalty units, for a false or misleading statement.
    - Losing the card that made a home exempt triggers both.
    - The value of a penalty unit is not deposited.

    Asserted, with traces.
22. **The surviving spouse.**
    - Under s 4(4)-(6) the surviving spouse need not be an eligible pensioner. Their application covers only the year of application and, under s 4(1D), the year before.
    - Under s 4(7)-(8) an unpaid remission passes to the spouse only for the year of death, plus the previous year if the death falls in the year of application. Nothing passes for later years.

    Asserted.

Findings 23 to 26 are corrections made after the independent verification of 2026-10-24. Finding 1 was also revised then.

23. **The 2024-25 maximum remission needs no CPI figure.** Regulation 5(4) sets it directly ($379.41 for a water and sewerage customer, $558.50 otherwise). Regulation 5(2) first indexes it for 2025-26, with C the March 2025 figure and D the March 2024 figure.
    - The first version required one figure for 2024-25. Given none, it answered `not covered` because "a Hobart CPI figure that the year's maximum remission needs was not given", which is false for that year. The seat's `@desc` asked for "one figure for 2024-25" too.
    - Corrected: the core now works out how many figures a year needs (`the number of Hobart CPI figures reg 5 needs for`): none for 2024-25, and n + 1 for the year n years later. The `@desc` now says none is needed for 2024-25.
    - No asserted value was wrong; the only 2024-25 assertion had passed a one-item list.

    Asserted: with no figures, 2024-25 gives $379.41 and $558.50, and a 2024-25 remission of 30% of $1,500 is capped at $379.41; 2025-26 with March 2024 alone, and 2027-28 with three figures, are `not covered`.
24. **The amount question now finds the cases it does not cover.** Two parts of the Act can change an individual owner's land tax and are not encoded. The first version answered both with the plain Schedule 1 figure.
    - *Foreign investor land tax.* Under s 16C(1) an owner is liable if, at the start of the year, (a) the land is general land capable of residential use, and (b) an owner is a foreign person who acquired an interest by a dutiable transaction or by survivorship on or after 1 July 2022 (or became a foreign person, other than a foreign natural person, on or after that day). Rating Act s 6A charges 2% of the assessed land value, "in addition to" the Schedule 1 amount. A foreign natural person is an individual owner and inside the seat, so the first version understated their tax without warning. Example: a $300,000 rental, on which Schedule 1 charges $837.50 and s 6A may add $6,000.
    - *The other exemptions.* Land under a conservation covenant (s 19A), approved new rentals and former short-stay properties (ss 19D, 19E), retirement village land (s 19(ba)-(bb)) and the other Division 2 exemptions take land, or part of it, out of the tax. The first version taxed such land in full.
    - Corrected: the amount question asks both facts, and the core's `the land tax payable, within the encoded scope, for the financial year on` answers `not covered` with the reason. The foreign-person screen applies only where the owner has some general land, counting a part apportioned as general land (s 16A(2)(a)). With none, s 16C(1)(a) cannot be met and the Schedule 1 amount (nil) stands. Paragraph (a)'s residential test and the s 16D carve-outs are not worked out, so the screen leans to `not covered`.
    - The plain Schedule 1 question now says that it leaves out foreign investor land tax.

    Asserted: a foreign owner's rental, and a foreign owner's home with a shop ($40,000 apportioned as general land), are `not covered`; a foreign owner with only a home, or only a home and a farm, pays nil; a conservation covenant is `not covered`; a year before 2026-27 gives the year's own reason first.
25. **Section 11(5)-(6) puts a 14-day duty on a new owner.** If it appears to the Commissioner that a person has become an owner and no details have been received, the Commissioner may serve a notice requiring the person "to state any interest in the land". The statement "is to be" by statutory declaration, "lodged with the Commissioner within 14 days after service of the notice".
    - The first version encoded s 11(3) only, and listed s 11(5)-(6) as neither in nor out.
    - Corrected: s 11(5)-(6) is now a regulative rule on the owner, clocked from service, and the seat asks what the person must do once served.
    - Section 11 sets no penalty. Whether the Taxation Administration Act 1997 adds one is not answered, because that Act is not deposited.
    - Section 11(1) and (4) (the Commissioner's list and the Valuer-General's details) are machinery and stay out.

    Asserted, with a trace: lodged on day 14, in time; on day 15, a breach by the owner.
26. **The pensioner exemption question restated the 50% test.** It took "my share for land tax" and tested it `AT LEAST 50` in the seat layer, repeating ss 6(1) and 19 instead of using the core's `is an owner of at least a 50% interest`. It also asked for a derived figure (the share after s 3B and s 11A) instead of plain facts.
    - Corrected: the question asks the share held, the number of joint tenants and any Help to Buy share, as the share question does, and passes them to the core.
    - The answers are unchanged where the old input was the counted share.

    Asserted: two joint tenants of the whole are exempt and three are not; a couple holding 70% with Housing Australia holding 30% are exempt (35 of 70 is 50%, finding 4); 35% with no Help to Buy share is not; a 60% tenant in common is.

## What would need doing before this is worth relying on

- Deposit the Taxation Administration Act 1997 (Tas), which governs land tax objections, interest and penalty tax (and may penalise a late s 11(6) statement), and the Penalty Units and Other Penalties Act 1987 (Tas).
- Deposit the Hobart CPI March-quarter figures (ABS) for reg 5, and the regulations in force before 2024-25 if earlier years are to be answered.
- Deposit the wording of ss 13 and 37 before 1 July 2026 if 2024-25 or 2025-26 land tax is to be answered.
- Check the reg 5(2) formula against the source image.
- Settle the readings in findings 1, 4, 6, 7, 10, 12, 15, 16 and 17 with the State Revenue Office's practice or the owner.
- Resolve reg 6(a) after the repeal of the Aged Care Act 1997 (finding 18).
- Deposit the Water and Sewerage Industry Act 2008 text for "customer".
- Encode the out-of-scope parts as needed: trusts and companies, foreign investor land tax (Div 1A with Rating Act s 6A, so that a foreign owner gets an amount instead of `not covered`), the other exemptions.
- The amount question screens out foreign investor land tax and the other exemptions (finding 24), but not land the owner holds as a trustee (s 6(3)-(5), s 24(4)) or land being subdivided (s 25). The seat is taken to be an individual owning in their own right, with no subdivision; a screen for both would be the next step.
- Check against State Revenue Office calculators and rulings. None were consulted.
