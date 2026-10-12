# Franciscan Missionaries of the Divine Motherhood Ordinance 1954 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FMDMO1954.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 5.
The Ordinance is dated 28 October 1954. Section numbers follow the body; the
arrangement at the top of the deposit is shifted by the PDF extraction.

**Checks:** one module (`fmd-corporation.l4`), one case file
(`fmd-cases-corporation.l4`), 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0234** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has five sections, so this row takes all of them except
the short title (ss 2-5). For someone outside the Mission it matters when buying,
leasing or lending against the Corporation's property, and in checking that a deed
was executed by the right person.

Not encoded: the preamble (constitution at Guildford on 26 November 1935, the work at
Tan Tock Seng Hospital and Trafalgar Home, the intended Mount Alvernia Hospital),
which recites but enacts nothing; the content of s 48 of the Conveyancing and Law of
Property Act 1886 (whether a power of attorney was "deposited" under it is a stated
fact here); how a Reverend Mother Superior is appointed.

## What the Act turns out to say

### 1. The Ordinance gives the Corporation no power to sue or be sued

s 2(3) lets the Corporation "acquire, purchase, take, hold and enjoy" property and
sell, mortgage, demise or otherwise dispose of property "vested in the Corporation".
It stops there. The Bishop of Singapore Ordinance 1911 (s 2(3)) and the Brothers of
St. Gabriel Ordinance 1950 (s 3(2)), as deposited in this repository, both add that
the corporation "may sue and be sued" in respect of its property; this one does not.
Whether the general law of body corporates fills the gap is outside the text and not
encoded: the encoding answers only what this Ordinance grants. Asserted.

### 2. "As hereinafter provided" points at nothing

s 2(1) incorporates Mother Mary Angela and her successors "duly authorised and
appointed as hereinafter provided". No later section provides how a Superior is
authorised or appointed. The nearest is s 4, which makes a Gazette notification of the
appointment "conclusive evidence that such person was duly authorised". The encoding
takes appointment as a stated fact and lets a Gazette notification stand in for proof
of it; that the cross-reference was meant to be s 4 is an inference. Asserted.

### 3. A deed signed by the Superior is evidence of due sealing even where the sealing was wrong

s 3(1) needs the Corporation's seal, affixed "in the presence of the Reverend Mother
Superior for the time being or her attorney, duly authorised by power of attorney
deposited under section 48 of the Conveyancing and Law of Property Act 1886", and the
signature of the Superior or such an attorney. s 3(2) makes "such signing" "sufficient
evidence that the seal was duly and properly affixed". So a deed sealed before an
ordinary sister but signed by the Superior fails s 3(1), yet its signature is
sufficient evidence that the seal was duly affixed. "Sufficient", not "conclusive". Asserted.

### 4. No stand-in during a vacancy, and an undeposited attorney cannot execute

Only the Superior "for the time being" or a deposited attorney qualifies under s 3(1).
A former Superior does not, and the Ordinance names no one to act while the office is
vacant (the Brothers of St. Gabriel Ordinance has a Brother Procurator for that; this
one has nothing). An attorney whose power was not deposited fails s 3(1) and gets no
help from s 3(2). Asserted.

### 5. The 2020 Revised Edition still incorporates the Superior "in Malaya"

The corporate name and the office in s 2(1) and s 4 are those of the Reverend Mother
Superior "in Malaya". A Superior of the congregation for another region is not the
Corporation. Asserted.

### 6. Everyone else's rights are saved

s 5: "Nothing in this Ordinance shall affect the right of the Government, all bodies
politic and corporate, and all others except such as are mentioned in this Ordinance,
and those claiming by, from or under them." Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- Whether the Corporation can sue and be sued under the general law (finding 1) was
  not researched.
- No Gazette notifications, case law or later legislation touching the Mission or
  Mount Alvernia Hospital were searched.
- The evidential effect of s 3(2) ("sufficient evidence") against contrary proof is
  not modelled.
