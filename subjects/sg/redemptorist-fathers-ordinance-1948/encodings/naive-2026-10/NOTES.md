# Redemptorist Fathers Ordinance 1948 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/RFO1948.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 6;
the Legislative History names Act 7 of 1997 (s 6 read with item (29) of the First
Schedule, in force 1 October 1997). Ordinance 9 of 1948, commenced 23 March 1948.
The arrangement of sections at the top of the deposit is shifted by one line in
extraction; section numbers here follow the body.

**Checks:** one module (`rfo-corporation.l4`), one case file
(`rfo-cases-corporation.l4`), 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0245** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections, so this row takes all of them except
the short title (ss 2-6). For someone outside the Congregation it matters when
buying, leasing or lending against the Corporation's property, when suing it or being
sued by it about that property, and in checking that a deed was executed by the right
person, including while the office of Titular Superior is vacant.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here); how a
Titular Superior or Reverend Father Minister is appointed (the Ordinance does not say);
what "formal assumption of office" involves (a stated fact); the reference to "the
Courts of the Colony of Singapore", read simply as the courts.

## What the Act turns out to say

### 1. Two different vacancy rules: s 2(3) covers only resignation or death, s 4 covers any vacancy

s 2(3) deems "successors in office" to include the Reverend Father Minister "from the
time when the office ... becomes vacant by the resignation or death of the holder for
the time being, until the formal assumption of office by his successor". A vacancy
arising any other way (a recall or transfer, say) is not mentioned, so on the words
the Father Minister is not then a successor in office. But s 4(1) lets the Father
Minister seal and sign "when the office is vacant", with no such limit. So after a
recall the Father Minister can validly execute the Corporation's deeds under s 4 while
not being, under s 2(3), part of the Corporation. The encoding keeps the two rules as
written; reading the s 2(3) list as exhaustive is the literal reading, not a settled
one. Asserted.

### 2. An appointed successor is not the Corporation until he formally assumes office

Because the Father Minister holds "until the formal assumption of office by his
successor", a successor who has been appointed but has not formally assumed office is
not yet the office-holder, and the Father Minister still is. Asserted.

### 3. The Corporation may sue and be sued, but only "in respect of such property"

s 3(2): "The Corporation may sue and be sued in respect of such property in any of the
Courts of the Colony of Singapore." The power is given, but tied to property. The
encoding reads "such property" as the property of s 3(1) vested in the Corporation (an
inference) and gives no power to sue or be sued about anything else. The powers of
disposal in s 3(1) (sell, convey, assign, exchange, surrender, yield up, mortgage,
demise, re-assign, transfer) likewise reach only property "vested in the Corporation".
Asserted.

### 4. Who may seal depends on whether the office is filled, and a dead Superior's attorney cannot

s 4(1) requires the seal to be affixed in the presence of the Titular Superior "for the
time being", or "when the office is vacant" the Reverend Father Minister, "as the case
may be", or "the attorney of any one of them" under a power deposited under s 48 of the
Conveyancing and Law of Property Act 1886, and signed by one of the same. The encoding
reads "as the case may be" as limiting each attorney to the period in which his
principal may act (an inference): so the Father Minister cannot execute while a
Superior is in office, and the late Superior's attorney cannot execute after his death.
Asserted.

### 5. A signature by the right person is evidence of due sealing even where the sealing was wrong

s 4(2) makes "such signing" "sufficient evidence that the said seal was duly and
properly affixed, and that the same is the lawful seal of the Corporation". A deed
sealed before another Father but signed by the Titular Superior fails s 4(1) yet
carries sufficient evidence that it complied. Asserted.

### 6. The Gazette proves authorisation for the office it names, and only that

s 5: a Gazette notification of the appointment of any person as Titular Superior "or of
Reverend Father Minister, as the case may be" is "conclusive evidence that such person
was duly authorised to exercise the said office in the Colony". A notice naming one
office does not prove authority for the other. The past tense ("was duly authorised")
says nothing about whether the person is still in office (an inference). Asserted.

### 7. Everyone else's rights are saved, except those "mentioned"

s 6 saves the rights of the Government, bodies politic and corporate "and all others,
except such as are mentioned in this Ordinance and those claiming by, from or under
them". Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- No Gazette notifications of appointment, case law, or later legislation about the
  Congregation were searched; who holds the office now is unknown here.
- Whether the s 2(3) list (resignation or death) is exhaustive, and how it fits with
  the unqualified vacancy in s 4(1), needs a lawyer's reading.
- Whether the Corporation can sue and be sued on other matters under the general law
  was not examined.
- The evidential weight of s 4(2) ("sufficient evidence") against contrary proof is
  not modelled.
