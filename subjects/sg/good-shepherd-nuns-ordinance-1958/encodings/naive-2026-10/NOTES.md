# Good Shepherd Nuns Ordinance 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/GSNO1958.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 5;
the Legislative History names Act 7 of 1997 (in force 1 October 1997). Ordinance 45
of 1958, commenced 21 November 1958. The arrangement of sections at the top of the
deposit is shifted by one line in extraction; section numbers here follow the body.

**Checks:** one module (`gsn-corporation.l4`), one case file
(`gsn-cases-corporation.l4`), 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0235** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has five sections, so this row takes all of them except
the short title (ss 2-5). For someone outside the Congregation it matters when
buying, leasing or lending against the Corporation's property, and in checking that a
deed was executed by the right person.

Not encoded: the recitals (the Home at 790 Thomson Road, the work at 140 Ampang Road,
Kuala Lumpur); the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here); whether
the Ordinance can reach property in the Federation of Malaya.

## What the Act turns out to say

### 1. "Appointed as hereinafter provided" points at nothing

s 2(1) incorporates Reverend Mother Mary of St. Liguori "and her successors for the
time being in office ... duly authorised and appointed as hereinafter provided". No
later section says how a successor is appointed. The only later provision on
appointment is s 4, a rule of evidence: a Gazette notification is "conclusive
evidence that such person was duly authorised". The encoding keeps the two apart:
holding the office needs being in office and duly appointed; separately, an inference
treats a gazetted office-holder as authorised even if the appointment was irregular,
because the evidence is "conclusive". Asserted.

### 2. The Gazette proves she *was* authorised, not that she still is

s 4 speaks in the past tense ("was duly authorised"). Read on its words, a former
Mother Superior's old notification still proves her past authorisation, but does not
make her the office-holder now, and s 3(1) lets only the Mother Superior "for the time
being" execute. A deed sealed before and signed by a former Mother Superior fails. The
past-tense reading is an inference from the wording. Asserted.

### 3. The Corporation is not expressly given power to sue or be sued

s 2(3) lets the Corporation acquire, take, hold and enjoy property "of every
description", and sell, convey, assign, surrender, mortgage, demise, transfer or
otherwise dispose of property "vested in the Corporation". Unlike the Bishop of
Singapore Ordinance 1911 s 2(3), there are no words about suing and being sued.
The encoding returns FALSE for powers the Ordinance does not grant; whether the
general law gives them to a body corporate is not encoded. Asserted.

### 4. A deed signed by the Mother Superior is evidence of due sealing even where the sealing was wrong

s 3(1) needs the seal, affixed "in the presence of the Reverend Mother Superior for the
time being or her attorney, duly authorised by power of attorney deposited under
section 48 of the Conveyancing and Law of Property Act 1886", and the signature of one
of them. s 3(2) makes "such signing" "sufficient evidence that the said seal was duly
and properly affixed". So a deed sealed before another nun but signed by the Mother
Superior fails s 3(1) yet carries sufficient evidence that it complied. An attorney
with an undeposited power can do neither. The Ordinance makes no provision for a
vacancy in the office. Asserted.

### 5. Everyone else's rights are saved, except those "expressly mentioned"

s 5 saves the rights of the Government, bodies politic and corporate "and all others,
except such as are expressly mentioned in this Ordinance and those claiming by, from
or under them". Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- No Gazette notifications of appointment, case law, or later legislation about the
  Congregation were searched; who holds the office now is unknown here.
- Whether the Corporation can sue and be sued under the general law, and the effect
  of the Ordinance on property in Malaysia, were not examined.
- The evidential weight of s 3(2) ("sufficient evidence") against contrary proof is
  not modelled.
