# Singapore Railway Transfer Ordinance 1918 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the other naive rows (the `writing-l4-rules` skill could not be loaded in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SRTO1918.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and comes into operation on
31 December 2021. Its Legislative History lists no amending instrument later than
1959 (Ordinances 62 and 72 of 1959 and G.N. Nos. S (N.S.) 177–179/1959). The
arrangement of sections at the top of the deposit is one line out of step with the
body; the encoding follows the body (s 1 short title to s 10 private Act).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0254** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The Ordinance is ten short sections, so the row takes almost
all of it: ss 2–9. Not encoded: the recitals (the $4,136,000 consideration is quoted,
not computed with), s 1, s 10 (deemed a private Act for the Registration of Deeds Act
1988), and anything about whether any land remains vested today, which the deposit
does not say.

## What the Act turns out to say

### 1. A private person's only claim is narrow, and a boatman has none

s 8 bars any claim for land injuriously affected, for obstruction of the flow of
water or of ships and boats, or for altered tides, "Except as in section 9 provided".
s 9 gives a right only "in respect of any lands or of any interest therein", and only
if the damage was (a) caused by what the Ordinance authorised, (b) from "the execution
of the works ... and not by their subsequent use", and (c) would have been actionable
without the Ordinance. So someone with no interest in land whose boat is held up has
nothing; a house shaken by trains after completion has nothing; a shophouse cracked by
pile-driving for the works has a claim. Seafront land flooded by tides the works
altered has a claim through s 9 although tide alteration as such is barred by s 8.
Asserted.

### 2. Interference with a right must be physical and must carry market value

Where the claim is for interference with a public or private right, s 9(d) adds that
it must be "a physical interference" with a right that "gives an additional market
value to such property apart from the uses to which any particular owner or occupier
might put it". A wharf physically cut off from the sea qualifies; a shop's lost
passing trade does not (the classification of those two cases is the encoder's
reading of (d)). Who pays, how much and before which body are not said. Asserted.

### 3. Land taken back is paid for by what was paid for it, and sometimes not at all

On taking back land vested by s 2, the Federation of Malaya gets what the Federated
Malay States paid "for the purchase of the land so resumed" plus the value of its
buildings at the date of resumption (s 4(3)(a)); if nothing was paid for that land,
only the buildings (s 4(3)(b)). For land vested later under s 3 nothing is paid for
the land, only the buildings (s 4(4)) — and s 3(4) had required no payment for it
beyond survey and demarcation. The survey cost is not returned (an inference from
silence). The recitals give one global consideration of $4,136,000 for the railway;
how a per-parcel price for s 4(3)(a) is found is not said. Asserted.

### 4. Six months' notice, and the right hand must authorise entry

Both ss 4 and 5 need 6 months' notice under the Minister's hand before the Collector
of Land Revenue may enter. Under s 4 (land vested by ss 2, 3) it is the Yang
di-Pertuan Negara who authorises entry; under s 5 (land otherwise acquired for the
railway, bought back with its buildings) it is the Minister. Asserted.

### 5. The valuer must belong to one of two British institutions

A disputed valuation (s 4(5)) or price (s 5(3)) goes to a person selected by the Yang
di-Pertuan Negara who is a Member or Associate Member of the Institution of Civil
Engineers or a Fellow or Associate of the Royal Institution of British Architects;
the decision is "final and binding on both parties". A Singapore-licensed valuer
alone does not qualify on the text. Asserted.

### 6. The 2020 text still speaks of 1959

The revised edition keeps the "Chief Secretary, Federation of Malaya", the "Colony",
the "Yang di-Pertuan Negara" and the "Legislative Council" (s 6). The encoding uses
those words as they stand and does not map them to present-day offices. s 7 lets the
works go ahead "notwithstanding that obstruction is thereby caused to the passage of
ships". Asserted (s 6 approvals, s 7 authority).

## What would need doing before this is worth anything

- Find whether any land is still vested under ss 2 or 3, and what agreements
  between the two Governments since 1959 have done to it; the deposit says nothing.
- Map the 1959 offices to present-day ones, with authority for the mapping.
- Settle the s 9(d) classification against case law on injurious affection.
- No subsidiary legislation, plan of 18 March 1913 or case law was retrieved.
