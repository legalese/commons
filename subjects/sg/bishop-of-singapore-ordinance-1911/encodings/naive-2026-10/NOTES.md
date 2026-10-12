# Bishop of Singapore Ordinance 1911 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/BSO1911.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 6.

**Checks:** one module (`bso-corporation.l4`), one case file
(`bso-cases-corporation.l4`), 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0227** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections, so this row takes all of them except
the short title (ss 2-6). For someone outside the Church it matters when buying,
leasing or lending against the Corporation's property, and for title to land conveyed
to "The Bishop of Singapore" before 1911.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here), and
what "the respective estates and interests" in s 3 amount to.

## What the Act turns out to say

### 1. A deed signed by the Bishop is evidence of due sealing even where the sealing was wrong

s 4(1) needs three things: the Corporation's seal, affixed "in the presence of the
Bishop of Singapore for the time being or his attorney duly authorised by a power of
attorney deposited under section 48 of the Conveyancing and Law of Property Act 1886",
and the signature of the Bishop or such an attorney. s 4(2) then makes "such signing"
"sufficient evidence that the said seal was duly and properly affixed". So a deed
sealed before a church officer but signed by the Bishop does not meet s 4(1), yet its
signature is sufficient evidence that it does. The text says "sufficient", not
"conclusive". Asserted.

### 2. An attorney whose power was never deposited cannot execute

The attorney limb of s 4(1) is confined to a power of attorney deposited under s 48 of
the 1886 Act. A conveyance sealed before and signed by an attorney with an undeposited
power fails s 4(1) and gets no help from s 4(2). Witness and signer need not be the
same person on the words of s 4(1); that reading is encoded. Asserted.

### 3. The 2020 Revised Edition still speaks of 1911

s 2(1) defines the Corporation as Bishop Ferguson-Davie "and his successors in office
who are Bishops of the Church of England and recognised by the Archbishop of
Canterbury for the time being" as authorised for "the Settlements of Singapore, Penang
and Malacca". Both conditions are encoded as written: a recognised bishop of another
church, or a Church of England bishop not so recognised, does not hold the office.
Asserted.

### 4. Only pre-1911 land in the three Settlements was swept in

s 3 vests in the Corporation "all immovable property situated in the Settlements of
Singapore, Penang and Malacca heretofore conveyed or assigned to or vested in 'The
Bishop of Singapore'", "whether with or without the name of the ecclesiastic". Movable
property, land elsewhere, and land conveyed after the Ordinance are not caught; the
naming of the individual bishop makes no difference. Reading "heretofore" as before
3 November 1911 is an inference from the word. Asserted.

### 5. The Gazette proves authorisation, and only that

s 5: a Gazette notification of the appointment is "conclusive evidence that such
person was duly authorised to exercise the said office". It is a separate test from
s 2(1); on its words it does not prove the person is a Bishop of the Church of England
(an inference from the wording). Asserted.

### 6. Powers reach vested property only; everyone else's rights are saved

s 2(3) lets the Corporation acquire and hold property of every description, but sell,
mortgage, demise or otherwise dispose only of property "vested in the Corporation", and
sue and be sued "in respect of such property". The Ordinance grants no other power
(whether the general law supplies one is not encoded). s 6 saves the rights of the
Government and every other person "except such as are mentioned in this Ordinance and
those claiming by, from or under them". Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- No case law, Gazette notifications or later legislation touching the Anglican Church
  in Singapore were searched; whether anything outside this text affects the
  Corporation's identity under s 2(1) is unknown here.
- The evidential effect of s 4(2) ("sufficient evidence") against contrary proof is
  not modelled.
