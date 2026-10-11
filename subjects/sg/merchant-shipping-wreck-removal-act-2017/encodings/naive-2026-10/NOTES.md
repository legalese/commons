# Merchant Shipping (Wreck Removal) Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MSWRA2017.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021"; the retrieval record calls it the current version as at
1 October 2026. The Legislative History lists only the original Act 25 of 2017
(commenced 8 September 2017), and the body carries no amendment annotations.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0108**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. A business
meets this Act when it owns, operates or insures a ship of 300 gross tonnage or more
that flies the Singapore flag or calls at a Singapore port, and when one of its ships
sinks, strands or loses cargo at sea.

The Act is short (31 sections plus the Nairobi Convention in the First Schedule).
This row takes what a wreck is and when the Act applies (ss 2, 3, 20(1)), reporting
(s 4), when the Director may remove a wreck (ss 5, 7, 8), the owner's liability for
the Director's costs (s 10 with Article 10(1)), the time bar (s 13), compulsory
insurance (ss 14, 15, 20(2), Second Schedule), certificates (s 16), the claim against
the insurer (s 17), the maximum penalties (ss 4(7), 15(4), (5), 23(5)) and
composition (s 28). Not encoded: locating and marking (s 6), the Article 6 hazard
criteria (s 9), sale of the wreck (s 8(3)), limitation of liability (s 12, which
hands it to Part 8 of the Merchant Shipping Act 1995, not read), detention
(s 15(6), (7)), admiralty jurisdiction and recourse (ss 18, 19), enforcement powers
and the corporate-officer rules (ss 21 to 25), and ss 26, 27, 29 to 31. No
regulations were retrieved, so the compoundable offences, fees and the evidence of
insurance required by s 7(1)(b) are unknown.

## What the Act turns out to say

### 1. "Singapore's Convention area" is the exclusive economic zone only

s 2 defines "Singapore's Convention area" as "the exclusive economic zone of
Singapore", and Part 3 (removal, s 5) and the owner's liability (s 10(1)(a)) apply
only to a wreck there. The Act does not take up the Article 3(2) option of extending
the Convention to territory and the territorial sea. On the ordinary meaning of
"exclusive economic zone" (the Act's own fallback is an area "beyond and adjacent to
the territorial sea"), a wreck inside Singapore's port or territorial sea is outside
this Act's removal and cost-recovery scheme, and outside the s 4 reporting duty. That
reading is an inference; other legislation may cover those waters, but none was read.
Asserted for reporting.

### 2. Three years from the notice, not from the hazard finding, and no rule without a notice

s 13 bars an action unless begun by the earlier of 3 years after the Director's
**s 7 notice** and 6 years after the casualty. Article 13 of the Convention instead
runs 3 years "from the date when the hazard has been determined", and adds that for a
series of occurrences the 6 years run from the first; neither point is in s 13. Nor
does s 13 say what happens where the Director removed the wreck without any notice
because the owner "cannot be contacted" (s 8(1)(b)). The encoding then applies the
6-year limb alone, which is an inference. Asserted.

### 3. One report excuses the other, even an incomplete one

s 4(4): if either the master or the operator reports, "the other ... is not required
to make the report". If no report is made both are guilty (s 4(5)); if the report is
incomplete only the one "who made the report" is guilty (s 4(6)). So an operator
whose master files an incomplete report commits no offence. Maximum $10,000 (s 4(7)).
The duty falls only on Singapore ships, and only for wrecks in a Convention area.
Asserted.

### 4. A Singapore ship needs the Director's certificate at every port in the world

s 15(1) bars a Singapore ship of 300 GT or more from entering or leaving "a port in
Singapore, or a port in a country other than Singapore" unless insured, certified by
the Director and carrying a copy of the certificate. A foreign ship needs only cover
and written evidence on board, and only at Singapore ports (s 15(2)). The master and
the operator are each liable to $20,000 (s 15(4)). Port includes an offshore facility
in the territorial sea (s 15(8)). Excluded are State-owned ships carrying their
State's certificate (s 20(2)) and harbour and pleasure craft that are licensed,
insured as the Port Master requires **and** stay within port limits (Second
Schedule); a licensed harbour craft that goes beyond port limits is caught. Asserted.

### 5. Partial blame does not excuse the owner

The owner escapes the Director's costs only by proving war, insurrection or an
"exceptional, inevitable and irresistible" natural phenomenon, or that the casualty
was **wholly** caused by a third party's intentional act or by an authority's
negligent upkeep of navigational aids (s 10(4), Article 10(1)), or where liability
would conflict with a listed oil, HNS, nuclear or bunker convention (s 10(3)). The
insurer has the owner's defences plus one of its own: the owner's wilful misconduct
(s 17(3), (4)). Asserted.

### 6. Composition is capped at $1,000 for every offence in the Act

s 28 caps a composition sum at the lower of half the maximum fine and $1,000. The
lowest maximum fine in the Act is $10,000 (s 4(7)), so the cap is always $1,000.
Whether any offence is compoundable depends on regulations not retrieved. Asserted
for the $10,000 offence.

### 7. A cross-reference that does not quite fit (observation)

s 15(6) allows detention where a person "attempts to navigate a ship into or out of
a port in Singapore in contravention of subsection (4)". Subsection (4) creates the
offence; the prohibitions are in (1) and (2). The encoding does not model detention.
Not asserted.

## What would need doing before this is worth anything

- Read Part 8 of the Merchant Shipping Act 1995 to encode the s 12 limit, and
  whatever regulations prescribe compoundable offences and evidence of insurance.
- Check whether other legislation governs wrecks in Singapore's port and territorial
  sea (finding 1).
- The "to the extent" partial conflict in s 10(3) and joint liability under s 10(5)
  are not modelled.
- No case law was searched.
