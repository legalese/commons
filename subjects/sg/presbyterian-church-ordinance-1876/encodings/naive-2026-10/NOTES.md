# Presbyterian Church Ordinance 1876 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PCO1876.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The body carries no amendment annotation. The Ordinance is dated
24 March 1876.

**Checks:** one module (`pco-sale.l4`), one case file (`pco-cases-sale.l4`),
44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0243** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has three sections, so this row takes all of them except
the short title (ss 2-3). For someone outside the congregation it matters only to a
purchaser of the land comprised in Indenture No. 215 of 25 January 1827: who could sell
it, and whether their receipt discharges the buyer.

Not encoded: the identity of the land beyond its description (whether a parcel is the
Indenture No. 215 land is a stated fact); the trusts of the grant of 6 May 1875 beyond
the purpose the preamble recites; what "costs and expenses attending the sale" include;
what happens if the costs exceed the price; whether the sale ever took place (the
deposit does not say).

## What the Act turns out to say

### 1. A purchaser who pays the right people need not care where the money goes

s 3(3): receipts "given by the persons exercising the power of sale hereby conferred
shall be sufficient discharges to the purchasers, who shall not be bound to see to the
application of such purchase money". So if the trustees later spend the price on
something s 3(1) forbids, the purchaser is untouched. The protection depends on the
receipt coming from a group that can exercise the s 2 power; a receipt from trustees
appointed after 1876, or from a group that s 2 does not authorise, is not made a
discharge by s 3(3). Asserted.

### 2. Only the seven named men, or their survivors, could ever sell

s 2 gives the power to "the said trustees", named one by one, "or the survivors of
them, or any 2 or more of such surviving trustees who are for the time being resident
within the Colony". No successor trustee is named, so a trustee appointed later is
outside every limb. All the survivors together may act wherever they live; a smaller
group needs at least two, resident in the Colony. A single survivor acting alone is
encoded as within "the survivors of them" where he is the only survivor (an inference;
the text uses the plural), and outside the power where others survive. A group of three
that includes one non-resident member and does not include every survivor is encoded as
outside the power (a reading: the text could also be read as letting the two resident
members act, with the third merely joining). Asserted.

### 3. The net proceeds may build a church or chapel on the granted land, and nothing else

s 3(1): the money, "after deducting the costs and expenses attending the sale", is paid
to the trustees of the land granted by the Crown, and "shall be applied by such trustees
to the building of such church or chapel only". Repairing the old chapel, the
congregation's general expenses, buying more land or building elsewhere are all
excluded. The purpose clause also mentions "other place of worship"; on the word "only"
in the application clause, a place of worship that is not a church or chapel is encoded
as excluded (a reading). Net proceeds are gross price less costs. Asserted.

### 4. The power covers the old land and the 1876 buildings only, and is a power to sell

s 2 reaches the land "comprised in and demised by" Indenture No. 215 "and also all
erections and buildings which have been erected and are now standing on the said
premises", with power to execute assurances, give effectual receipts and do all other
acts "for completing such sale". A building put up after the Ordinance, other land of
the congregation, and a mortgage of the land are encoded as outside the power (the
mortgage point is an inference from "sell and dispose of ... completing such sale").
Asserted.

### 5. The new church is held on the 1875 grant's trusts, known here only by the preamble

s 3(2): the building "shall be held subject to the trusts set out in the grant above
recited, and dated 6 May 1875". The grant was not retrieved. The preamble recites it as
being for "religious worship and use of the members of any denomination of Christians
holding as their confession of faith" the Westminster Standard. That recited purpose is
encoded; it is a recital, not an enacting provision. Asserted.

## What would need doing before this is worth anything

- The grant of 6 May 1875 and Indenture No. 215 were not read; the trusts and the land
  are bare inputs.
- Nothing outside the deposit was searched: whether the sale happened, whether the
  power is spent, and whether later legislation affects the land are unknown here.
- The two readings flagged in findings 2 and 3 (a mixed resident/non-resident group;
  "other place of worship") would need a lawyer's view.
