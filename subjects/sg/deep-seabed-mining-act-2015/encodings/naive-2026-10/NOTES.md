# Deep Seabed Mining Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DSMA2015.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The latest amendment annotated in the body is [40/2019], on the
definition of "Singapore national" in s 2.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0119** in `subjects/sg/requirements.jsonl`: tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is short (25 sections). This row takes what a person or company actually
meets: the prohibition and its exceptions (ss 2, 4, 5), who may hold or take a
transfer of a licence (ss 6(3), 7, 12(2), 25), lapse, suspension and revocation (ss
13, 14), the representations timetable (s 15), wind-down directions and who may be
given them (s 16), financial penalties (ss 10(4), 11(3), 16(5), 24(2)(g)) and
officers' liability (s 21). Not encoded: the Minister's discretion over licence
content, duration and conditions (ss 6(1), (2), 8, 9, 10(1)-(3), 11), the Court's
remedies under Annex III, Article 22 (s 17), registration and enforcement of Seabed
Disputes Chamber decisions and arbitral awards (ss 18-20), recovery of penalties (s
22), Rules of Court and regulations beyond s 24(2)(g), and the Convention, the
Agreement and ISA rules themselves.

## What the Act turns out to say

### 1. The prohibition binds only Singapore nationals, and a PR is not one

s 4(1): "a Singapore national must not explore for or exploit any resource in the
Area". s 2 defines a Singapore national as a Singapore citizen or an entity
incorporated, formed or established in Singapore under any written law. A permanent
resident who is not a citizen, a foreign individual and a foreign company are outside
s 4 altogether. Asserted (citizen and LLP are nationals; PR and foreign company are
not; a PR mining on his own account commits no offence under s 4).

### 2. Only a Singapore *company* can ever mine lawfully; other Singapore entities cannot

The exceptions in s 5 cover a Singapore company (s 5(1)) and an individual Singapore
citizen (s 5(2)). A Singapore limited liability partnership is a Singapore national
under s 2(b) but is neither, and s 7(1) says "Only a Singapore company may apply for
and be granted a licence". On the encoding, an LLP that somehow held a licence and an
ISA contract would still commit the s 4 offence. Asserted. (That an LLP is "formed or
established in Singapore under any written law" is an inference from the Limited
Liability Partnerships Act being mentioned in s 21(5); this Act does not say so in s 2.)

### 3. A Singapore company sponsored by another State commits an offence; its citizen employees do not

s 5(2)(a)(ii) lets a Singapore citizen work for "a person who has entered into an ISA
contract under the sponsorship of any State other than Singapore", within the scope of
that contract, while it remains in force. No such exception exists for a Singapore
company: s 5(1) requires a Singapore licence. So a Singapore company holding an ISA
contract sponsored elsewhere is guilty, while a citizen working for the same kind of
contractor is not. Asserted.

### 4. A terminated ISA contract kills the licence; a suspended one only lets the Minister act

s 13(c): the licence lapses when "the corresponding ISA contract is terminated for any
reason". s 14(1)(b): if it is merely "suspended for any reason", the Minister *may*
suspend or revoke. A licence also lapses if no ISA contract is entered within 12
months of grant or transfer "(or such longer period as the Minister may allow)" — the
Minister can lengthen but not shorten it, so a 6-month allowance is read as 12.
Asserted.

### 5. Wind-down directions reach former directors, but not former senior managers, and not on suspension

s 16 applies on expiry, transfer, lapse or notified revocation — not suspension.
Directions may go to the licensee, a current director or senior manager, or, only if
none of them is able to comply, "any person who was a director ... in the period of 6
months immediately preceding" the event. A former senior manager is not in that last
category. Compliance gives immunity from loss caused to others, but not for acts the
direction did not require (s 16(6), (7)). Asserted.

### 6. Penalties: high fines, short prison, and no excuse for a condition breach

s 4(2): up to $300,000 for anyone, plus up to 3 months' imprisonment for an individual,
and for a continuing offence up to $50,000 a day after conviction, capped at $500,000.
The administrative financial penalty is $40,000 throughout, but for breach of a licence
condition (s 10(4)) there is no "without reasonable excuse" qualifier, unlike
non-compliance with a direction (ss 11(3), 16(5)). Regulations may attach either a
penalty or an offence to a provision, "but not both" (s 24(2)(g)). Officers are guilty
with the body corporate on consent, connivance or neglect (s 21). Asserted.

### 7. The licence-transfer test leans on s 7 (inference)

s 12(2) allows transfer only to a Singapore company "eligible under section 7 to be
granted a licence". The encoding reads that as the whole of s 7, including the
Minister's s 7(3) satisfaction; it could be read as s 7(1) alone. Labelled as an
inference in the `.l4`. Asserted on the encoding's reading.

## What would need doing before this is worth anything

- No regulations under s 24 were retrieved: prescribed licence criteria, lapsing
  events, fees and any penalty-or-offence provisions are flags only.
- The Convention's Annex III, Article 4 qualification standards and Article 22 liability
  are not encoded; s 17 and Part 3 are left out entirely.
- "One month" in s 15 is modelled in months, not calendar days; the interaction of the
  s 15(2) and (4) periods is not computed.
- No case law or ISA practice was searched.
