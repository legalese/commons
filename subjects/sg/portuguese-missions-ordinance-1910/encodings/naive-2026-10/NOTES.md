# Portuguese Missions Ordinance 1910 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PMO1910.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". Two amendment annotations appear in the body: "[Act 25 of 2021
wef 01/04/2022]" under s 5 and "[7/97]" under s 8. The deposit's metadata records it
as the current version as at 1 October 2026.

**Checks:** one module (`pmo-corporation.l4`), one case file
(`pmo-cases-corporation.l4`), 50 assertions satisfied, 0 errors, 0 warnings. One
deliberate mutation (the total rent changed by one cent) was caught.

## Why this Act, and why scoped

Requirement **REQ-0241** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The operative part has eight short sections, so this row takes all of
them except the short title (ss 2-8), with the five Schedules. For someone outside
the Commission it matters when buying, leasing or lending against the Corporation's
land, when suing or serving it, and for title to the ten scheduled parcels.

Not encoded: the long recitals (1826-1870 leases, assignments and Portuguese
Ordinances) except as they explain the Schedules; the content of s 48 of the
Conveyancing and Law of Property Act 1886 ("deposited" is a bare input); parcel
boundaries; whether any parcel is still held (the deposit does not say).

## What the Act turns out to say

### 1. Two of the ten 999-year terms do not run from their own lease's date

Eight Schedule items are leased "for the term of 999 years from the date thereof".
Item 9 (Lot No. 2 of lease No. 1577, dated 3 March 1865) runs "from the day of the
date of the original lease No. 1577 dated 5 November 1862"; item 10 (lease No. 300,
dated 7 May 1841) runs "from the 11 June 1827", fourteen years before the lease was
made. The terms end between 2825 (the 1826 Commercial Square leases, items 5-8) and
2861 (item 9). s 3 vests the parcels only "for the residue of the term of years".
Year arithmetic only. Asserted.

### 2. A successor Agent is not the Corporation until the Gazette says so

s 2(1) makes Cardozo "and his successors ... duly qualified as hereinafter provided"
the Corporation. s 6(1) qualifies a successor only "unless and until" he is appointed
by the Bishop of Macao as President "by instrument in writing", the instrument is
"produced to the Minister" and "approved by him", and "a notification of such
approval has appeared in the Gazette". All four are required; a successor approved
but not yet gazetted is not qualified. Cardozo needed none of them. The Gazette is
"sufficient evidence" (s 6(2)), not "conclusive", unlike the "conclusive evidence" in
the Bishop of Singapore Ordinance 1911 s 5. Asserted.

### 3. A deed executed by an ungazetted successor is not duly sealed

s 7(1): the seal must be affixed in the presence of Cardozo, his successor "duly
qualified as aforesaid", or either's attorney under a power "deposited under
section 48 of the Conveyancing and Law of Property Act 1886", and signed by one of
them. So a successor who has not completed s 6 cannot execute, and neither can an
attorney whose power was never deposited. s 7(2) makes "such signing" "sufficient
evidence of the due sealing": a deed sealed with no qualified person present but
signed by the Agent fails s 7(1) yet carries sufficient evidence that it passes.
Asserted.

### 4. The scheduled land rents for $272.37 a year in all

The Schedules' annual rents are $20, $27, $15.50, $30, $14.50 three times, $80, $28
and $28.37, together $272.37, over 25,182.3 m2 in Singapore Town (High Street, North
Bridge Road to Beach Road, Commercial Square, New Bridge Road by the Singapore River).
Hand-added and asserted.

### 5. Acquisition is confined to the Colony, disposal to vested property; suits are not confined at all

s 4 lets the Corporation acquire and hold property "within the Colony" and sell,
exchange, mortgage, demise or otherwise dispose of property "vested in the
Corporation". s 5(1) lets it sue and be sued "in any of the Courts of the Colony"
with no limit to its property (the Bishop of Singapore Ordinance confines its
Corporation to suits "in respect of such property"). s 5(2) says process "may" be
served by leaving it at the Corporation's residence in Singapore; whether other modes
are good is outside the text. Asserted.

### 6. The saving clause names four dead men's representatives

s 8 saves everyone's rights, the Government's included, "except such as are mentioned
in this Ordinance" and those claiming under them "or any of the legal personal
representatives of" Isaiah Zechariah, Joaquim Jozé Leite ("Liete or Letta"), Nicholao
Rodrigues Pereira de Borja and Manuel Lourenço de Gouvêa. The recitals say the three
priests died at Macao in 1845, 1858 and 1885 and that it "is not known who are their
respective legal personal representatives". s 3 vests "Subject to section 8". The
reading encoded (the Ordinance may affect only those three classes) is an inference
from the sentence, whose punctuation admits others. Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- No Gazette notifications under s 6, land-title records or case law were searched;
  who the current Agent is, and whether any scheduled parcel is still held under the
  Ordinance, is unknown here.
- The evidential weight of "sufficient evidence" in ss 6(2) and 7(2) against contrary
  proof is not modelled.
- Lease terms are computed by year only; the exact end dates follow the start day and
  month in the Schedules.
