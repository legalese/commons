# Scheut Missions Ordinance 1938 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SMO1938.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". One amendment annotation appears in the body: "[7/97]" under s 7.
The Ordinance is dated 16 September 1938. The deposit's metadata records it as the
current version as at 1 October 2026. The arrangement of sections printed at the top
of the deposit is out of step with the numbers; the body's numbering (ss 1-7) is
followed.

**Checks:** one module (`smo-corporation.l4`), one case file
(`smo-cases-corporation.l4`), 50 assertions satisfied, 0 errors, 0 warnings. One
deliberate mutation (the Municipal Commissioners' total changed by 0.1 m2) was caught.

## Why this Act, and why scoped

Requirement **REQ-0249** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The operative part has seven short sections, so this row takes all of
them except the short title (ss 2-7), with the two Schedules. For someone outside the
Mission it matters when buying, leasing or lending against the Corporation's land,
when suing it, and for title to the eight scheduled parcels.

Not encoded: s 2(2) (remaking the seal); the recitals except as they explain the
Schedules; the content of s 48 of the Conveyancing and Law of Property Act 1886
("filed" and "deposited" are bare inputs); parcel boundaries and grant histories;
whether any parcel is still held (the deposit does not say).

## What the Act turns out to say

### 1. A successor's attorney may sign the deed but may not stand in for him at the sealing

s 6(1) lists who may be present when the seal is affixed: Quintens, "his attorney duly
authorised by a power of attorney deposited under section 48", or "his successor ...
duly qualified as aforesaid". It then lists who may sign: Quintens "or his attorney or
by his successor or the attorney of such successor as aforesaid". The successor's
attorney appears only in the second list. Read as written, a mortgage sealed before a
successor's attorney and signed by the successor is not duly sealed, though one sealed
before the successor and signed by his attorney is. s 6(2) makes "such signing"
"sufficient evidence of the due sealing", so the first deed still carries sufficient
evidence that it passes. Whether the drafter meant the asymmetry is not knowable from
the text. Asserted.

### 2. A successor Procureur is not the Corporation until the filing is gazetted

s 2(1) makes Quintens "and his successors ... duly qualified as hereinafter provided"
the Corporation. s 5(1) qualifies a successor only "unless and until" he has, "with the
approval of the Minister signified under his hand and seal", caused "the power of
attorney or other instrument constituting him Procureur" to be "duly filed in the
Registry of the Supreme Court" under s 48 of the Conveyancing and Law of Property Act
1886, and "a notification of such filing has appeared in the Gazette". All four are
required; a successor approved and filed but not yet gazetted is not qualified, and
cannot execute under s 6. Quintens needed none of them. The Gazette is "sufficient
evidence" (s 5(2)), not "conclusive". Asserted.

### 3. One parcel was bought in the name of a man who died in Manila in 1934

The recitals say the First Schedule lands were purchased in the name of the agent,
Richard Quintens, and the Second Schedule land (item 8, 7,881.5 m2 at Lot 55 Town
Subdivision XXV, with the house at No. 24 Nassim Road) in the name of "the former
agent", Father Michael De Meester, who "has left the Colony and died on 22 March 1934
in Manila". Both out of "funds belonging to the Mission". s 4 vests both Schedules in
the Corporation "for the estate and interest for which the same are held" -- it passes
what the nominee held, no more. Asserted (Schedule and nominee flag; the vesting rule
is a bare input).

### 4. The scheduled land is 17,549.7 m2, after 181.5 m2 went to the Municipal Commissioners

First Schedule: Ulu Pandan 1,013.6 and 831.5 m2; Geylang three lots of 1,617.1,
1,599.6 and 1,580.6 m2 (4,797.3); Killiney Road 679.7 m2 with four houses (Nos. 19,
21, 23, 25); Claymore Lot 242 435.8 m2; Somerset Road 402.1 m2 (No. 90) and 1,508.2 m2
(No. 100). Together 9,668.2 m2; with Nassim Road, 17,549.7 m2. Items 5, 6 and 7 each
lost a portion "acquired by the Municipal Commissioners of the Town of Singapore"
(35.4, 28.0 and 118.1 m2, together 181.5). Item 4 is "now estimated" at 679.7 m2
against 674.4 m2 in the 1931 mortgage plan; the resurvey figure is used. No item
states a rent or a lease term. Hand-added and asserted.

### 5. The property power has no territorial limit, and the Corporation may be sued anywhere

s 3 lets the Corporation "acquire, purchase, take, hold and enjoy movable and
immovable property of every description" -- no "within the Colony", unlike the
Portuguese Missions Ordinance 1910 s 4 -- and dispose of property "vested in the
Corporation". It "may sue and be sued ... in all Courts of Justice" by its corporate
name, with no limit to its property. The Ordinance confers no power to borrow without
security and says nothing about how process is served on the Corporation. Asserted.

### 6. The saving clause leaves everyone's rights alone except those mentioned

s 7: nothing affects the rights of the Government, of bodies politic or corporate, "or
of any other persons except such as are mentioned in this Ordinance, and those claiming
by, from or under them". s 4 vests "Subject to section 7". The reading encoded (the
Ordinance may affect only persons mentioned and those claiming under them) is an
inference; the closing words could instead attach to the saved classes. Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "filed" and
  "deposited" are bare inputs.
- No Gazette notifications under s 5, land-title records or case law were searched;
  who the current Procureur is, and whether any scheduled parcel is still held under
  the Ordinance, is unknown here.
- The evidential weight of "sufficient evidence" in ss 5(2) and 6(2) against contrary
  proof is not modelled.
- The successor's-attorney asymmetry in s 6(1) (finding 1) needs a lawyer's reading
  before anyone relies on it either way.
