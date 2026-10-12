# Brothers of St. Gabriel Ordinance 1950 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/BSGO1950.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 6.
The Ordinance is dated 2 March 1950.

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0229** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections, so all of it is in scope except the
short title (s 1). For someone outside the Congregation it matters when dealing
with the Corporation's property and checking that its deeds were executed by the
right person. Not encoded: the content of s 48 of the Conveyancing and Law of
Property Act 1886 (whether a power of attorney was "deposited" is a stated fact),
how either office is filled, and what "formal assumption of office" consists of.

## What the Act turns out to say

### 1. The Brother Procurator stands in only after a resignation or a death

s 2(3) deems "successors in office" to include the Brother Procurator from the time
the office "becomes vacant by the resignation or death of the holder" until the
successor's "formal assumption of office". On the words, a vacancy arising any
other way does not trigger the deeming. The stand-in period ends at formal
assumption, not at appointment. Asserted.

### 2. Section 4 does not repeat that limit, so the two sections pull apart

s 4(1) lets the Brother Procurator witness the sealing and sign "when the office is
vacant", with no mention of resignation or death. The encoding follows s 4: a deed
witnessed and signed by the Procurator is validly executed in any vacancy
(including one "for some other reason"), even though s 2(3) would not make him a
successor in office in that vacancy. The text does not reconcile the two. While the
office is filled, a deed executed by the Procurator does not meet s 4. Asserted.

### 3. A deed needs the seal, a qualified witness and a qualified signer

s 4(1) requires all three. The Titular Superior qualifies while the office is filled,
the Procurator while it is vacant, and an attorney "of any one of them" only if the
power of attorney was deposited under s 48 of the Conveyancing and Law of Property
Act 1886. Reading the attorney limb as applying whether or not the office is vacant
is an inference from "any one of them". s 4(2): the signing alone is "sufficient
evidence" that the seal was duly affixed and is the lawful seal. Asserted.

### 4. The Gazette settles authority for both offices

s 5: a Gazette notification of the appointment of the Titular Superior **or** the
Brother Procurator is "conclusive evidence" that the person was duly authorised. A
buyer or lender can rely on it. Asserted.

### 5. Disposal powers reach only what is vested in the Corporation

s 3(1) lets the Corporation acquire and hold any property, but sell, exchange,
mortgage, lease or otherwise dispose only of property "vested in the Corporation".
s 3(2) gives capacity to sue and be sued "in respect of such property"; the
Ordinance grants nothing beyond that (the general law is not encoded). Asserted.

### 6. The 2020 Revised Edition still speaks of the Colony

The revised text keeps "the Colony of Singapore" in ss 2(1), 3(2) and 5, and names
the first holder, "The Reverend Brother Vincent". s 6 saves everyone's rights except
those mentioned in the Ordinance and those claiming through them. Asserted (s 6).

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; what makes a
  power of attorney "deposited" is taken as given.
- The gap between s 2(3) and s 4(1) on the cause of a vacancy needs a lawyer's
  reading, or case law; none was searched.
- Whether the Interpretation Act reads "the Colony of Singapore" as Singapore was not
  checked.
