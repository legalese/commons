# Significant Infrastructure Government Loan Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021, in
operation 31 December 2021), informal consolidation, version in force from 29 May 2026.
The latest amendment annotated is Act 8 of 2026 (Coastal Protection and Other
Amendments Act 2026, in force 29 May 2026), which added coastal management to the
purposes in s 2.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0205** in the requirement ledger: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act authorises the Government to borrow for large infrastructure. The person it
meets is an investor holding its securities, so this row takes what a holder gets
(redemption, early redemption, interest, transfers through the MAS: ss 12-16, 20-22)
together with the limits that decide whether the loan may be raised and spent at all
(ss 2, 5, 9-11, 18). Not encoded: the foreign-currency conversion rules (s 5(5)), the
yield-to-maturity arithmetic behind the interest threshold (s 5(3)), issuing powers and
the charges on the Consolidated Fund (ss 6-8), the MAS's agency and depositary functions
(ss 17, 19), confirmation advices (s 23) and the Regulations (ss 24, 25). No Regulations
were retrieved.

## What the Act turns out to say

### 1. Spending before 3 August 2021 counts towards the threshold but cannot be paid for

s 11(3) makes capital expenditure qualifying "even if incurred before 3 August 2021",
so it counts towards the $4 billion approval threshold in s 11(5). But s 11(1) defines
nationally significant infrastructure expenditure, the only thing the money may be
spent on (s 10(1)(b)), as qualifying expenditure "incurred, on or after 3 August 2021".
Reading the two together, earlier spending helps a project qualify yet cannot itself be
met from the loan. The reading is the encoding's. Asserted.

### 2. The $90 billion cap counts what was borrowed, not what is outstanding

s 5(1)(a) adds the proposed borrowing to "the total amount of sums borrowed under any
loan earlier raised under this Act". Nothing deducts redemptions. Rolling debt over is
handled instead by s 5(2)(a): a borrowing the Minister "(in person)" designates as
refinancing is outside the cap, but only if it "is for a sum less than" the securities
redeemed or maturing in the same year. Borrowing exactly the redeemed amount is not
less, so the exception fails. Securities the MAS has on loan under s 18 are also left
out (s 5(2)(b)). The cap is breached only when the total "exceeds" $90 billion, so
exactly $90 billion is allowed. That redemptions are not deducted is an inference from
the text's silence. Asserted.

### 3. Refinancing does not lift the interest limit

The refinancing exception in s 5(2) is expressed to disapply "subsection (1)(a)" only.
The second limit, effective interest in the previous financial year "more than"
$5 billion (s 5(1)(b), (4)), still stops a refinancing loan. Asserted.

### 4. Only government spending on government-owned assets qualifies, and never land or rolling stock

Infrastructure must be "controlled and legally owned by the Government" and principally
for the public (s 2). Qualifying expenditure must be incurred by the responsible ministry
or a public authority acting on its behalf (s 11(7)), and excludes repair and
maintenance, land and rights over land, and "the acquisition, repair or maintenance of
any train, vehicle, aircraft, vessel or barge" (s 11(4)). A related facility likewise
"does not include any train, vehicle or vessel". A project needs at least $4 billion of
estimated qualifying spending, and contracts that stand alone on non-adjacent land are
disregarded in reaching it (s 11(5), (6)). Asserted.

### 5. A holder can only redeem early when the MAS invites it, and the MAS may refuse without reasons

A security not redeemable at the holder's election is redeemed at par on its maturity
date (s 12). Its holder may apply to redeem early only "upon an invitation of the MAS"
by public notice that covers the security, and "the MAS may refuse any application ...
without assigning any reason" (s 13). For an electable security, a pro-rata portion of
the half-yearly interest is paid on redemption (s 14(2)); the encoding pro-rates by
days, which the text does not specify. Interest stops after the earliest of the
maturity date, the notice date and the early redemption date, "regardless of any demand
for payment of the principal sum" (s 15). Asserted.

### 6. The MAS register beats everything else, and protects the MAS

A transfer or pledge entered in the MAS's records "has priority over any transfer or
pledge ... effected or created in any other manner before, on or after" it (s 20(3)).
Other means of transfer remain possible (s 21(1)), but the MAS must not accept notice of
them and any such notice "is void" (s 21(4)). The MAS is not liable for conversion where
it followed its depositor's instructions "even though the depositor had no right to
dispose of" the securities (s 22). Asserted.

### 7. The power to borrow cannot be delegated, and approvals are personal

s 9 forbids delegation of the Minister's powers under Part 2 "despite anything in the
Interpretation Act 1965 or any other law"; project approval under s 11 and the
refinancing designation under s 5(2) must be given "in person". The MAS's securities
lending is capped at $6.5 billion unless Parliament resolves a higher sum (s 18(2)).
Asserted.

## What would need doing before this is worth anything

- The Regulations prescribing terms of issue (s 24) were not retrieved; the holder's
  real terms (coupon, redemption notice manner) live there.
- The yield-to-maturity computation (s 5(3)) and the exchange-rate rules (s 5(5)) are
  taken as given figures, not computed.
- The layout reading in s 11(2) — that the 50-year useful-life clause governs all of
  (a) to (c), not only (c) — should be checked against the official PDF.
- No case law or parliamentary material was searched.
