# Multimodal Transport Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
23/9/2026), as deposited at `../../registers/source-bundle/MTA2021.txt`. The latest
amendment annotated is Act 17 of 2025 (Transport Sector (Miscellaneous Amendments)
Act 2025), in force 23 September 2026, against s 11(2) and (3).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0102**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. A business
meets it when it ships goods door to door across a border by two or more modes, or
runs the forwarding business that contracts to do so.

The Act is short (31 sections). This row takes when it applies (ss 2, 3),
registration (ss 4 to 6), the document as evidence (s 11), the operator's liability
and its limits (ss 15, 17, 18, 20, 21, 23), the consignor's dangerous-goods duties
(s 24), notice of loss (s 25) and the time bar (s 26). Not encoded: the register and
designated appeal hearers (ss 7, 8), the issue and contents of the document and who
may claim delivery (ss 9, 10, 14), valuation (s 16), the mandatory-law limit for a
localised loss (s 19), the servant-and-agent aggregate (s 22), arbitration (s 27),
void stipulations (s 28), general average and saved laws (ss 29, 30) and
regulations (s 31). No regulations were retrieved, so the prescribed fee,
particulars and minimum assets are unknown. The Act creates no offences.

## What the Act turns out to say

### 1. Declaring the value lifts the sea limit but not the land-and-air limit

s 17(2) disapplies "Subsection (1)" — the 666.67 SDR per package / 2 SDR per kg
limit — when the consignor declares the nature and value of the goods and it is
inserted in the document. s 18, the 8.33 SDR per kg limit for a contract with no sea
or inland-waterway carriage, has no such carve-out. Read literally, a shipper who
declares a high value on a truck-and-air contract still recovers at most 8.33 SDR per
kg. Whether Parliament meant that is not something the text settles. Asserted (on
50,000 SDR of loss and 1,000 kg: 50,000 with sea carriage and a declaration, 8,330
without sea carriage despite a declaration).

### 2. No sea leg means a per-kilogram limit only

s 17(1) is "subject to" s 18, and s 18 says liability "is limited to an amount not
exceeding 8.33 SDR per kilogram". This encoding reads s 18 as replacing the s 17
limit, so a light, many-package land-and-air consignment gets no per-package
alternative. That is a reading, not the text's words. With sea carriage the limit is
the higher of the two s 17 measures (3 packages of 1,000 kg: 2,000.01 SDR, not
2,000). Asserted.

### 3. Nothing at all for delay unless the consignor declared an interest in time

s 15(3): no liability for delay "unless the consignor has made a declaration of
interest in timely delivery which has been accepted". Even then s 20 caps it at
"the freight under the contract", and s 21 caps the total of loss and delay at the
total-loss limit under ss 17 and 18. Asserted.

### 4. Only the operator's own reckless act breaks its limit

s 23(1) removes the operator's limit where the loss resulted from "an act or omission
of the multimodal transport operator" done intentionally or "recklessly and with
knowledge" that loss would probably result; s 23(2) does the same to a servant,
agent or subcontractor for their own act. The heading speaks of a "personal act or
omission". Read literally, a servant's reckless act — for which the operator is
liable under s 13 — does not cost the operator its own limit. Asserted.

### 5. Nautical fault and shipboard fire excuse the operator only at sea

The s 15(2)(b)(vii) defences — the master's error "in the navigation or in the
management of the ship" and fire not caused by "the actual fault or privity of the
carrier" — apply only "where the goods are carried by sea or inland waterways". The
other excepted causes (force majeure, the shipper's own act, bad packing, inherent
defect, strikes) apply on any leg. A subcontracted trucker's carelessness is no
defence: s 13 makes the operator answer for it. Asserted.

### 6. Undelivered goods: 90 days to treat as lost, then 9 months to sue

s 15(6): goods not delivered within 90 consecutive days after the due date may be
treated as lost. s 26(b) lets the action be brought within 9 months after the due
date *or* after that 90-day point, so the later one governs, roughly a year from the
due date. For delivered goods the 9 months run from delivery. Parties may "expressly
agree" otherwise, and the text does not limit that to a longer period (not encoded).
Asserted (except the agreement).

### 7. Notice of hidden damage within 6 days, or the handover counts as sound delivery

s 25: unless written notice is given at handover (or, for damage "not apparent",
within 6 consecutive days after the day of handover), the handover is prima facie
evidence of delivery as described. Asserted.

### 8. The consignor carries the risk of undeclared dangerous goods

s 24(4): if the consignor does not tell the operator of the goods' dangerous
character and the operator does not otherwise know, the consignor is liable for the
operator's related losses and the goods may be "unloaded, destroyed or rendered
innocuous" without compensation. If the operator did know, it may still do so once
the goods become "an actual danger to life or property", unless general average is
owed or it failed to take reasonable measures (s 24(6)). Asserted.

### 9. Registration is a Singapore-company, insured, annual licence with no court appeal

s 4(4) lists conditions the competent body must see before issuing — a Companies Act
company or registered business name, a principal place of business in Singapore,
acceptable insurance or financial cover, the prescribed minimum assets — but s 4(3)
says it "may" issue, so meeting them is necessary, not sufficient. A certificate
lasts one year (s 4(5)); a renewal filed less than 3 months before expiry is treated
as a fresh application (s 5(2)). Cancellation needs at least 28 days for
representations (s 6(3)); appeals go to the Minister within 14 days, "whose decision
is final", and a cancellation takes effect despite an appeal (s 6(7)). Asserted,
except s 6(7).

### 10. A clean document becomes conclusive once a consignee relies on it

s 11(2) (inserted by Act 17 of 2025): proof contrary to the document is not
admissible once it is transferred, or sent by electronic data interchange, to a
consignee who acknowledged receipt and relied on it in good faith. The encoding
assumes a document qualified "shipper's weight, load and count" or "shipper-packed
container" is not conclusive either; the text of (2) does not repeat that proviso
(an inference). Asserted.

## What would need doing before this is worth anything

- The regulations under s 31 (fees, prescribed particulars, minimum assets) were not
  retrieved.
- s 19 (a mandatory-law limit for the stage where loss occurred, e.g. an air or sea
  convention) can displace every SDR figure here and is not encoded.
- No SDR-to-dollar conversion is attempted; the Act defines SDR by the IMF's website.
- Day and month counting ("within 14 days", "within 90 consecutive days", "9 months")
  is modelled with simple numbers; the inclusive or exclusive reading is an inference.
- No case law was searched, and no ASEAN member-country notification was retrieved.
