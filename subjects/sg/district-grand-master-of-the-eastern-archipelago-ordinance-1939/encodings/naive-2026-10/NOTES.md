# District Grand Master of the Eastern Archipelago Ordinance 1939 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DGMEAO1939.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the only amendment annotated in the
body is [7/97] on s 8 (Act 7 of 1997, Statutes (Miscellaneous Amendments) Act 1997, in
force 1 October 1997, per the Legislative History).

**Checks:** one case file, 42 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0232** in `subjects/sg/requirements.jsonl`: Tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has eight sections and the row takes all of them except
the short title. The people it decides anything for are a Lodge or trustee handing
Masonic property to the Corporation, and anyone buying from, lending to, leasing from
or otherwise dealing with it. Not encoded: the general law it displaces or relies on
(s 15 Trustees Act 1967, s 48 Conveyancing and Law of Property Act 1886, neither read),
the laws and regulations of the Craft referred to in s 4(2), and what the
Government's rights saved by s 8 are.

## What the Act turns out to say

### 1. A buyer from the Corporation need not look behind the Masonic trusts

s 4 puts everything the Corporation holds on trust, yet s 5 says that "in favour of any
purchaser from and any person dealing with the Corporation" it has full power to sell,
mortgage, lease or otherwise dispose "as if the Corporation were the true and
beneficial owner". The only limit is "the terms of the instrument of trust (if any)
affecting the same". The encoding reads that limit as an instrument that forbids the
disposition; how far a restrictive term reaches a buyer is not stated. Asserted.

### 2. Nothing the Corporation holds is its own

s 4(1): property transferred by trustees holding it for Free Masonry or for a Lodge
stays on "such trusts". s 4(2): property "not ... impressed with any trust express or
implied" is held on trust for Free Masonry in general or Masonic charitable uses as
the Corporation directs, subject to the laws of the Craft. So even an outright gift or
an ordinary purchase ends up on a Masonic trust. Property impressed with some other,
non-Masonic trust is not dealt with by s 4; that it stays on that trust is an
inference. Asserted.

### 3. The office-holder is appointed in England, and the Gazette proves it

s 2(1): the Corporation is the District Grand Master "by patent of appointment from the
Grand Master of the United Grand Lodge of Ancient Free and Accepted Masons of England"
and his successors "so authorised and appointed". No Singapore authority appoints. s 7:
a Gazette notification of the appointment is "conclusive evidence" of authority. The
encoding treats a missing notification as leaving authority to other proof, which is an
inference. Asserted.

### 4. A deed needs sealing in the right presence and the right signature

s 6(1): the seal must be affixed in the presence of the District Grand Master for the
time being or his attorney under a power of attorney **deposited** under s 48 of the
Conveyancing and Law of Property Act 1886, and the instrument signed by one of them. An
undeposited power, a former District Grand Master or a Lodge officer will not do. s 6(2):
the signing is "sufficient evidence" that the seal was duly affixed. The text does not
require the witness and the signer to be the same person, and the encoding does not.
Asserted.

### 5. A sole-trustee receipt rule that overrides the Trustees Act

s 3(2): "notwithstanding anything to the contrary contained in section 15 of the
Trustees Act 1967", where immovable property is vested in the Corporation as **sole**
trustee on trust for sale or with power of sale, it may give valid receipts for the
proceeds. All three conditions are needed. What s 15 says was not read. Asserted.

### 6. The Government's rights are untouched

s 8: "Nothing in this Ordinance shall affect the rights of the Government." It carries
the only amendment annotation, [7/97]; what Act 7 of 1997 changed in it is not shown in
the deposit. Asserted.

## What would need doing before this is worth anything

- Read s 15 of the Trustees Act 1967 and s 48 of the Conveyancing and Law of Property
  Act 1886, which ss 3(2) and 6 displace or rely on.
- Settle how far "the terms of the instrument of trust (if any)" in s 5 binds a
  purchaser who has not seen the instrument.
- No case law, Gazette notifications or land-register practice were searched.
