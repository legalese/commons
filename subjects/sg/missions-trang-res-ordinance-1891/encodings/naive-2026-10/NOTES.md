# Missions Étrangères Ordinance 1891 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MEO1891.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 4.
The Ordinance is dated 13 November 1891.

**Checks:** one module (`meo-corporation.l4`), one case file
(`meo-cases-corporation.l4`), 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0239** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has four sections, so this row takes all of them except
the short title (ss 2-4). For someone outside the Society it matters when buying,
leasing or lending against the Corporation's property: is the person executing a
duly qualified Procureur, and is the deed duly sealed?

Not encoded: the preamble; the content of s 48 of the Conveyancing and Law of
Property Act 1886 (whether an instrument was "filed" or "registered" under it is a
stated fact here); how the Society appoints its Procureur, about which the Ordinance
says nothing.

## What the Act turns out to say

### 1. A Procureur is not the Corporation until the Gazette says so

s 2(1) makes the Procureur and his successors a body corporate only when "duly
qualified as hereinafter provided", and s 2(4) says no person is duly qualified
"unless and until" he has, "with the approval of the Minister signified under his
hand and seal", filed the instrument constituting him Procureur in the Registry of
the Supreme Court under s 48 of the 1886 Act, "and unless and until a notification of
such filing has appeared in the Gazette". A Procureur appointed by the Society, with
his filing approved and made, is still not duly qualified while the notification is
pending. Asserted.

### 2. The Gazette notification is both a condition and the proof — but only "sufficient" proof

s 2(5): the notification "shall be sufficient evidence of the appointment, and that
the person therein named is duly qualified". The same notification that completes
qualification under s 2(4) is evidence of it. The text says "sufficient", not
"conclusive": a notification of a filing made without the Minister's approval is,
on the encoding, evidence of qualification for someone who does not meet s 2(4); so
is a notification naming a former Procureur. Whether such evidence can be rebutted
is not modelled. Asserted.

### 3. A deed signed by the Procureur is evidence of due sealing even where the sealing was wrong

s 3(1): no instrument "shall be deemed to be duly sealed" unless the seal "has been
affixed in the presence of the Procureur duly qualified as aforesaid, or his attorney
duly authorised by a power of attorney registered under section 48", and it "is
signed by the Procureur or his attorney". s 3(2): "Such signing shall be sufficient
evidence of the due sealing". So a deed sealed before another member of the Society
but signed by the Procureur fails s 3(1), yet its signature is sufficient evidence
that it was duly sealed. Asserted.

### 4. Neither an ungazetted Procureur nor an unregistered attorney can execute

The presence limb of s 3(1) needs the Procureur "duly qualified as aforesaid" or an
attorney under a power "registered" under s 48. A conveyance sealed before and
signed by a Procureur not yet gazetted, or by an attorney whose power is not
registered, fails s 3(1) and gets no help from s 3(2). Reading "the Procureur" and
"his attorney" in the signing limb as the same qualified persons is an inference from
"as aforesaid" and the definite article. Witness and signer need not be the same
person on the words of s 3(1); that reading is encoded. s 2(4) says the Procureur's
own instrument is "filed", s 3(1) that the attorney's power is "registered".
Asserted.

### 5. Powers over property reach vested property only; nothing about suing

s 2(3) lets the Corporation "acquire, purchase, take, hold and enjoy movable and
immovable property of every description", but sell, mortgage, demise or otherwise
dispose only of property "vested in the Corporation". The Ordinance says nothing
about suing or being sued, or about borrowing other than by mortgage; whether the
general law supplies these is not encoded. The seal "may from time to time be
broken, changed, altered and made anew" (s 2(2)). Asserted.

### 6. Only the Government's rights are saved

s 4: "Nothing in this Ordinance shall affect the rights of the Government." No other
person is named. The encoding says only that s 4 does not save anyone else's rights;
it does not say the Ordinance affects them. Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "filed" and
  "registered" are bare inputs, and whether they mean the same thing under s 48 is
  unknown here.
- No Gazette notifications, case law or later legislation touching the Society or its
  property in Singapore were searched; who holds the office today is unknown here.
- The evidential effect of "sufficient evidence" in ss 2(5) and 3(2) against contrary
  proof is not modelled.
