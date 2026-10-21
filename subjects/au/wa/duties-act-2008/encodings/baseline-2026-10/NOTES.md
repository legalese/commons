# Duties Act 2008 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

This encoding replaces the first-pass encoding `naive-2026-10`. It covers everything that encoding covered and reuses its hand-checked figures, all of which were re-derived from the text and still hold. It adds:

- s 27 dutiable value;
- the Chapter 6A off-the-plan concession;
- who pays, and the deadlines to lodge, pay and apply (ss 20, 23, 25, 144, 205M, 266O);
- vehicle liability (ss 229, 230, 232);
- the general rate and the first home owner rates as data tables.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `da-property.l4`: homes and shares: transfer duty, first home owner concession, foreign transfer duty, off-the-plan concession, landholder duty, deadlines.
- `da-vehicles.l4`: vehicle licence duty.
- `da-cases-property.l4` and `da-cases-vehicles.l4`: built by the scratchpad generator `gen_wa_duties-act-2008_baseline.py`.

## Edition

The compilation of the Duties Act 2008 (No. 11 of 2008) deposited at `../../registers/source-bundle/mrdoc_49812.txt` (legislation.wa.gov.au mrdoc 49812, retrieved 2026-09-07).

- The deposit gives no compilation number or date.
- Its compilation table ends with the Help to Buy (Commonwealth Powers) Act 2025 Pt. 4 Div. 1, in operation 19 Dec 2025.
- The rates and thresholds are in the Act itself (Schedule 2, s 142(1)(b), s 266L). No regulation is used.
- **Formulas lost from the `.txt` deposit, recovered.** R in s 236(2)(b) (an image) and X, Y, Z, A and B in s 266L(2), (3), (3A), (5) and (6) (Word equations) did not survive conversion. They, and the other formulas of the Act, are transcribed by hand from the authorised Word rendering of the same document (mrdoc 49812, fetched 2026-10-21) in `../../registers/source-bundle/mrdoc_49812.formulas.md`, and R and the s 266L formulas are encoded.

## Checks

Two case files, **74 assertions satisfied** (63 in `da-cases-property.l4`, 11 in `da-cases-vehicles.l4`), 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98).

A copy with one expected value altered was run as a control. The runner reported the failure.

## Seat

**The buyer: of a home, of a car, or of shares in a company.** For a home, that is the transferee or purchaser named in Schedule 1 column 4. For a car, it is the person to whom the licence is granted or transferred (s 232(1)). For shares, it is the acquirer under Chapter 3.

All nine life events ask this Act the same question from that seat: "What duty must I pay, and do I get a concession?" The Commissioner's assessment powers are encoded only as what they mean for the buyer.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The numbers are in the Act's own Schedule 2 and sections, so no regulation was needed.
- **The actors the text names.** Followed: the buyer (transferee, purchaser, acquirer, licence holder) and the Commissioner.
- **A judgment handed to someone else is answered conditionally.** Followed. The Commissioner's opinion that a new dwelling is suitable as a residence (s 266G(1)(b)) is a fact the buyer states. The answer holds if the Commissioner is of that opinion.
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed. Worked out from facts:
  - dutiable value (s 27);
  - first home owner concessional transaction (s 142(1));
  - foreign individual (s 205A);
  - landholder and significant interest (ss 155(2), 161);
  - concessional off-the-plan agreement (ss 266F, 266FA).

  Asked as facts:
  - "concessional first home owner", which s 142A takes from the FHOG Act;
  - "home", from the FHOG Act (s 141(2));
  - metropolitan or Peel region, from the Planning and Development Act 2005;
  - citizen, permanent visa and special category visa, from the Commonwealth Acts;
  - heavy vehicle, from the Road Traffic (Vehicles) Act 2012.
- **One case is the text's natural unit.** Followed: one purchase (one dutiable transaction), one licence grant or transfer, one acquisition of shares.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Left out: administration, the Commissioner's powers, objections and anti-avoidance (Chapter 7).

**Departures:**

- Dates in Chapter 6A are entered as YYYYMMDD numbers, not dates, so that the window tests are simple comparisons.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c051** (2028), Byford house-and-land package, $620,000 | `What transfer duty must I pay`, `Is my purchase a first home owner concessional transaction` | Concessional, but **$16,356**, not nil, if the $620,000 is land that includes a home |
| Chloe **c074** (2034), $28,000 used car | `What vehicle licence duty must I pay` | **$896**: R = 3.20, not the life's $770 |
| Chloe **c081** (2040), Baldivis townhouse, $1,300,000 | `What transfer duty must I pay` | **$58,065.50** |
| Chloe **c094** (2070), Mandurah strata apartment, no price stated | `What transfer duty must I pay` (general rate) | Asserted at an assumed $800,000: $32,315.50 |
| Daniel **d037** (2028), East Perth, $1,600,000, citizen and permanent resident | `What transfer duty must I pay`, `What foreign transfer duty must I pay`, `Am I a foreign individual` | $73,515.50; no foreign transfer duty |
| Daniel **d055** (2038), Nedlands, $4,200,000 | `What transfer duty must I pay` | **$207,415.50**; no foreign duty |
| Daniel **d065** (2043), Jarrah buys Formly | `Is what I am buying dutiable property`, `Must I pay landholder duty` | Shares are not dutiable property; landholder duty only if Formly holds $2m+ of WA land (none assumed) |
| Daniel **d071** (2050), Jarrah sold to a listed buyer | `Must I pay landholder duty`, `What landholder duty must I pay` | As d065: none unless Jarrah is land-rich |
| Jake **k074** (2042), off-the-plan apartment, $390,000 | `What transfer duty must I pay`, `Is my agreement a concessional off-the-plan agreement` | Nil at the first home owner rate; the off-the-plan concession is not available in 2042 |

## Why this scope

The scope is what the nine events ask, plus what any buyer in the same seat meets on the way: who pays, how the value is fixed, when to lodge and pay, and when a concession must be claimed.

The plan named Chapter 6A as bearing on k074, so it is in. Everything else in this very large Act was left out because no buyer in the lives meets it:

- the other dutiable transactions;
- the exemptions;
- foreign landholder duty;
- the detailed landholder machinery.

## What the Act turns out to say

1. **Two of the lives' general-rate figures are wrong.** Schedule 2 Division 1 charges "$28 453 + $5.15 per $100 or part of $100 above $725 000". That gives $58,065.50 for c081 (the life expects $55,185) and $207,415.50 for d055 (the life expects $207,378). d037's $73,515 drops 50 cents. Asserted.
2. **c051 is not nil.** For a first home that is land including a home in the metropolitan or Peel region, $620,000 is above the $500,000 nil band and under the $700,000 cap. It pays $13.63 per $100 above $500,000: **$16,356**. Nil is reachable only if the dutiable transaction is vacant land at or under $350,000, with the building contract outside duty. That reading of the package is an inference, and the land price is not stated. Asserted.
3. **The off-the-plan concession is closed to Jake.** Every window in ss 266F(1)(c) and 266FA(1)(c) ends on **30 June 2026**. An agreement made in 2042 is not a concessional off-the-plan agreement on this compilation. Jake's duty is nil anyway at the first home owner rate. Asserted.
4. **How the off-the-plan concession works:**
   - It is the lesser of **$50,000** and a percentage of the duty that would otherwise be payable (s 266L).
   - The percentage is 100%, 75% or 50% for preconstruction agreements, and 75% or 37.5% under construction, by concession day and value.
   - It comes off transfer duty first, and only the remainder comes off foreign transfer duty (s 266K(3)).
   - A foreign buyer of a $600,000 lot in April 2025 pays no transfer duty, and $14,515 of the $42,000 foreign duty.

   Asserted.
5. **The off-the-plan concession tapers in the middle bands.** The recovered formulas (`mrdoc_49812.formulas.md`) take the low-band percentage and subtract, for every $100 of dutiable value above the band, 0.05 of a percentage point before construction (X, Y, Z: 100 to 50 over $100,000) or 0.0375 during it (A, B: 75 to 37.5). An $800,000 preconstruction agreement entered on 1 April 2025 gets Z = 75%, so $8,078.875 transfer duty on $32,315.50; under construction on 1 October 2025 it gets B = 56.25%, a concession of $18,177.46875. The Act states no rounding for the concession. Asserted.
6. **c074's $770 is a flat 2.75%, which the text allows only up to $25,000; the duty is $896.** Above $25,000 the rate is R% with R = 2.75 + [(DV − 25000) / 6666.66] "rounded to 2 decimal places" (s 236(2)(b), recovered), rising to 6.50 at $50,000, then 6.5% above $50,000. A $28,000 car gives R = 3.20 and $896. The result is "rounded down to the nearest 5 cents". R is rounded half up (an inference: the Act names no rule). Asserted.
7. **Dutiable value is the greater of the price and the unencumbered value (s 27(b)(iii)), and the first home owner cap tests the unencumbered value (s 142(1)(b)).** A first home bought for $690,000 but worth $710,000 loses the concession and pays $27,740 at the general rate. Asserted.
8. **A permanent resident is not a foreign individual (s 205A).** Neither is a New Zealand citizen on a special category visa. So d037 owes no foreign transfer duty. Foreign transfer duty is 7% (s 205O), and joint tenants are treated as tenants in common in equal shares (s 205L). The encoding infers that the 7% falls on each foreign buyer's share: one temporary-visa holder with a citizen at $1,600,000 owes $56,000. Asserted.
9. **Shares are not dutiable property (s 15).** A share purchase attracts duty only as landholder duty, where all of these hold:
   - the company holds WA land assets of **$2,000,000 or more** (s 155(2));
   - the buyer reaches or adds to a **50%** interest, or **90%** for a listed company (s 161);
   - the duty is then charged at the general rate on that percentage of the land and chattels (ss 184, 186, 188).

   d065 and d071 turn on Formly's and Jarrah's WA land, which the lives do not state. Asserted on assumed holdings.
10. **Deadlines the buyer meets:**
    - lodge within **2 months** of liability arising (s 23), on pain of a fine of up to **$5,000**; the same for a foreign transfer duty declaration (s 205M);
    - pay within one month of the assessment notice, or 12 months for a conditional agreement or a transfer registrable under the Transfer of Land Act, or 3 years for a subdivision or issue-of-title conditional agreement (s 25);
    - seek the first home owner rate by reassessment within 12 months of completion, or 3 months after the grant is paid if later (s 144(2));
    - apply for the off-the-plan concession within 12 months of completion (s 266O).

    Asserted.
11. **The two scales are close at the caps.** At exactly $725,000 the fourth band gives $28,452.50, while the fifth band starts from $28,453. The first home owner rate meets the general rate almost exactly at the $700,000 cap: $27,260 against $27,265, and $27,269.75 for $1 more. Asserted.

## What would need doing before this is worth anything

- Correct the c074 facts ($770) to $896.
- Encode the FHOG Act test for "concessional first home owner" and its meaning of "home", or link to an encoding of that Act. Settle how a house-and-land package is split between land and building.
- Add further concessional transactions and the s 145 clawback. Add the off-the-plan replacement, multi-lot and aggregation rules.
- Add linked entities, relevant arrangements and the s 189 reduction to landholder duty. Add foreign landholder duty, and foreign corporations and trusts.
- Correct the lives' figures (c051, c074, c081, d055) and the ledger's provision references (Division 3, not 4; Chapter 3A, not "Chapter 2 Part 3B"; Schedule 2, not "Chapter 2 Part 5").
- Check against Revenue WA's calculators and rulings. None were consulted.
