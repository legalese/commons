# Bills of Lading Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/BLA1992.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. The latest amendment annotated in the body is 5/2021, on s 5(1).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0100** in `subjects/sg/requirements.jsonl`. It is in Tier 2 of the
remaining Singapore Acts, which are ordered by how often they touch everyday life.
The requirement asks what the Act decides for a person or business it applies to.
No scenario has asked a sharper question yet.

The Act has six sections, so this row encodes all of its operative text (ss 1 to 5):
- which documents it covers;
- who is the lawful holder of a bill of lading;
- when rights of suit against the carrier pass, and what happens to the original
  party's rights;
- when liabilities follow;
- when a bill is conclusive evidence of shipment.

Three things are not encoded:
- the short title (s 6);
- the extended meaning of "identified" in s 5(3), which is recorded only as an input
  flag;
- the Hague-Visby Rules, which s 5(5) leaves untouched. They are given force by the
  Carriage of Goods by Sea Act 1972, which was not read here.

## What the Act turns out to say

### 1. Rights come with holding the document. Liabilities come only with acting on it

s 2(1) passes "all rights of suit" to the lawful holder, the waybill consignee or the
delivery-order party simply by their becoming that person. s 3(1) puts the contract's
liabilities on that person only if they also do one of three things:
- take or demand delivery;
- make a claim against the carrier;
- have taken or demanded delivery before the rights vested.

So a holder who never asks for the goods and never sues has the rights without the
liabilities. Asserted.

### 2. Endorsing a bill of lading ends the shipper's right to sue, but a waybill does not

s 2(5) says the transfer extinguishes any entitlement that derives from having been an
original party, "where that document is a bill of lading". For a sea waybill it is
"without prejudice" to the original party's rights. So under a waybill, the shipper
and the consignee can both hold rights of suit at once. An earlier holder of any
document loses the rights it took under s 2(1) when they pass to the next person.
Asserted.

### 3. The shipper stays liable after its rights have gone

s 3(3) keeps "the liabilities under the contract of any person as an original party".
Together with s 2(5), this means the shipper under a bill of lading loses its rights
of suit but keeps its liabilities. Asserted, though the rule is a constant.

### 4. A non-transferable "bill" is not a bill of lading

s 1(2)(a) excludes from "bill of lading" any document "incapable of transfer either
by indorsement or, as a bearer bill, by delivery". s 1(3) then defines a sea waybill
as any document "which is not a bill of lading" but is a receipt evidencing a
contract of carriage by sea and identifies the person to deliver to. Read in that
order, a straight bill naming its consignee is a sea waybill under this Act. That is
my reading of how the two definitions cascade; no case was checked.

A received-for-shipment bill is expressly included (s 1(2)(b)). A delivery order counts
only if the undertaking is the carrier's (s 1(4)(b)), so a seller's or merchant's
delivery order falls outside the Act. Asserted.

### 5. A spent bill passes no rights, with two exceptions

s 2(2) deals with a bill taken after "possession of the bill no longer gives a right
(as against the carrier) to possession of the goods". Its holder gets no rights,
unless:
- the holder took it under arrangements made before the bill was spent; or
- the bill came back to the holder when goods or documents were rejected.

Such a buyer is still a holder under s 5(2)(c). Lost or mixed goods do not stop the Act
from operating (s 5(4)). Asserted.

### 6. Good faith is the whole test for lawful holder

s 5(2) makes a person the "lawful holder" wherever they became the holder "in good
faith". A holder in bad faith gets no rights under s 2(1), and does not take on
liabilities under s 3 either, even after demanding delivery. Asserted.

### 7. Only a bill of lading binds the carrier to what it says was shipped

s 4 makes a signed bill that represents goods as shipped or received for shipment
"conclusive evidence against the carrier", but only "in favour of a person who has
become the lawful holder". The bill must be signed by the master or by someone with
the carrier's express, implied or apparent authority. The Act gives a sea waybill
nothing like this. Asserted.

## What would need doing before this is worth anything

- The Carriage of Goods by Sea Act 1972 and the Hague-Visby Rules (s 5(5)) were not
  read, and they govern most of what a cargo claimant can actually recover.
- No case law was searched. In particular, nobody has checked the straight-bill
  reading in finding 4, or what "good faith" and "spent" mean in practice.
- s 5(3) (a description that lets the identified person change after issue) is
  recorded only as an input flag.
- The "terms of the order" in s 2(3)(a) are not modelled.
