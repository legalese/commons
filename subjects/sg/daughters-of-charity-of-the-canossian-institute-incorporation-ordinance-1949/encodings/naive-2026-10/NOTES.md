# Daughters of Charity of the Canossian Institute Incorporation Ordinance 1949 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DCCIIO1949.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 7.
The Ordinance is dated 23 November 1949.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0231** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance decides
for a person or business it applies to; no scenario has asked a sharper question yet.
The Ordinance is seven sections and a Schedule, so the whole of it is encoded except
s 1 (short title). For an outsider it matters when dealing with the Corporation over
property (ss 3, 5), when working out who may act for it during a vacancy (ss 2(3), 6),
and for title to the two scheduled lots (s 4). Not encoded: what makes an attorney
"duly authorised", the "conditions of tenure" and "trusts" s 4 preserves, and the
Society's internal governance, about which the Ordinance says nothing.

## What the Act turns out to say

### 1. The First Assistant becomes the Corporation during a vacancy — but only after a resignation or a death

s 2(3) deems "successors in office" to include the First Assistant of the Institute
from the time the office "becomes vacant by the resignation or death of the holder",
until her successor's "formal assumption of office". A vacancy arising any other way
(removal, for instance) does not bring her in on the words, and she drops out the
moment the successor formally assumes office. The literal reading is encoded. Asserted.

### 2. The stand-in is the Corporation, yet s 5 does not let her seal

s 5(1) requires the seal to be affixed "in the presence of the person who is for the
time being Mother Superior ... or of her attorney duly authorised", and signed by "such
Mother Superior or her attorney". It does not mention the First Assistant who is a
successor in office under s 2(3). On the literal reading encoded here, a deed sealed
and signed by the First Assistant during a vacancy is not executed as s 5 requires
(unless she holds a power of attorney). Whether a court would read s 2(3) into s 5 is
not answered by the text; this is the main open question for a purchaser or mortgagee
dealing with the Corporation in a vacancy. Asserted (literal reading).

### 3. The signature, not the seal, is the evidence

s 5(2): the signing "shall be and be taken as sufficient evidence that the said seal
was duly and properly affixed". So a deed sealed before an unauthorised sister but
signed by the Mother Superior carries that evidential presumption although it was not
executed as s 5(1) requires. No deposit of the attorney's power is required, only
that she be "duly authorised". Asserted.

### 4. Two lots, 30,148.6 square metres, taken subject to their trusts

s 4 divests the persons in the third column of the Schedule and vests in the
Corporation Lot 1846 of Mukim XXIV at Kallang (21650.2 m²) and Lot 163 of Mukim XXVII
at Bedok (8498.4 m²), "subject to all conditions of tenure ... and subject also to any
trusts". The extracted Schedule table is column-shifted: "Fee simple" appears twice
and the third column reads "Vittoria Garré and Bertilia Lim." then "Vittoria Garré".
These are matched to items (1) and (2) **by order**, so that Bertilia Lim's interest
is divested only in the Kallang lot. That attribution is a reading of a shifted
table. The total area is a sum computed here, not a figure the Ordinance states.
Asserted.

### 5. Powers of disposal and litigation reach only property vested in the Corporation

s 3(1) lets the Corporation acquire and hold property of every description, but
sell, exchange, mortgage, demise or transfer only "property vested in the
Corporation"; s 3(2) lets it sue and be sued "in respect of such property". The
Ordinance confers no other power (unsecured borrowing, suing on an unrelated
matter). Asserted.

### 6. A Gazette notice proves authority, and nothing else

s 6 makes a Gazette notification of an appointment "conclusive evidence" that the
person was duly authorised "in the Colony". It does not make anyone the office-holder,
and a Mother Superior in office without a notice is still the Corporation, only
without that conclusive proof. s 7 saves everyone's rights except those mentioned in
the Ordinance and those claiming under them. The 2020 Revised Edition still speaks of
"the Colony" throughout. Asserted.

## What would need doing before this is worth anything

- Check the Schedule against the PDF (`DCCIIO1949.pdf`) to settle which estate and
  which prior holders belong to each lot.
- Find whether the Interpretation Act or case law reads s 2(3) into s 5, and how
  "Colony" is to be read today.
- No Gazette notifications, land-title records or case law were searched.
