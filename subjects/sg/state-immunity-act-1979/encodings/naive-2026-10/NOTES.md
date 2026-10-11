# State Immunity Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation "version in force from
1/4/2022", deposited at `../../registers/source-bundle/SIA1979.txt`. The revised
edition incorporates amendments up to 1 December 2021; the latest amendment annotated
in the body is Act 25 of 2021 wef 01/04/2022 (the "notice of intention to contest or
not contest" wording).

**Checks:** one module (`sia-immunity.l4`), one case file (`sia-cases-immunity.l4`),
50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

The Act is **REQ-0140** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. Here that person is someone with a claim against a foreign State: a
supplier, an embassy employee, a landlord, someone injured. The questions are whether
a Singapore court will hear the claim, how the State must be served, and what a
winning claimant can enforce.

Encoded: ss 3 to 9, 11, 13, 14, 15, 16(1), (2), (4) and 19. Not encoded: s 1(2), (3)
(matters before 26 October 1979), s 4(6), (7), s 8(3), (4), s 10 (bodies corporate),
s 12 (Admiralty), s 15(1) and (5), s 16(3), (5), (6), s 17 (Presidential orders) and
s 18 (the Minister's certificate). Immunity outside Part 2 (common law, diplomatic,
consular) is not modelled.

## What the Act turns out to say

### 1. Winning against a State is not collecting from it

Even where a State is not immune and loses, s 15(2) says no injunction, no specific
performance, no order for recovery of land, and no enforcement process against its
property. Only the State's written consent (s 15(3)) or property "in use or intended
for use for commercial purposes" (s 15(4)) opens enforcement, and a clause merely
submitting to the courts "is not to be regarded as a consent". A central bank's
property is never treated as commercial for s 15(4) (s 16(4)), though written consent
still works. An injunction needs consent; commercial use does not help. Asserted.

### 2. A commercial transaction needs no link to Singapore

s 5(1)(a) removes immunity for "a commercial transaction entered into by the State"
with no requirement that it be made or performed in Singapore; only (b), for
non-commercial contracts, asks for performance in Singapore. The exception falls away
if the parties are States or "have otherwise agreed in writing" (s 5(2)). A loan to a
foreign government made abroad is therefore not immune. Asserted. (Whether the court
otherwise has jurisdiction over a foreign contract is outside this Act and not
modelled.)

### 3. An embassy's own nationals usually cannot sue it in Singapore; locals can

s 6 removes immunity for employment contracts made in, or performed in, Singapore, but
not if the employee is a national of the State when the proceedings are brought, or
was neither a Singapore citizen nor habitually resident in Singapore when hired.
For a commercial office of the State, those two bars apply only if the employee was
habitually resident in the State when hired (s 6(3)). A written agreement to the
contrary bars the claim unless Singapore law requires a Singapore court (s 6(4)).
s 5 expressly does not reach employment contracts. Asserted.

### 4. Defending the case is submitting to it; appearing to claim immunity is not

Instituting proceedings or taking "any step" in them is deemed submission (s 4(3)),
except a step only to claim immunity or one taken in excusable ignorance (s 4(4), (5)).
A clause choosing Singapore law "is not to be regarded as a submission" (s 4(2)).
And the court must give effect to immunity even if the State does nothing (s 3(2)).
Asserted.

### 5. A State must be served through the two foreign ministries, with two extra months

Service is by transmission through MFA Singapore to the State's foreign ministry, and
the time to respond begins only 2 months after receipt (s 14(1), (2)). No default
judgment without proof of that service and expiry of the extended time (s 14(4)),
unless the State agreed another manner of service (s 14(6)). A State that files a
notice of intention to contest cannot later object to the manner of service
(s 14(3)). Asserted.

### 6. State companies are immune only for sovereign acts

A "separate entity" (distinct from the executive organs and able to sue and be sued)
is immune "if, and only if" the proceedings concern something it did in the exercise
of sovereign authority and a State would have been immune (s 16(2)). A head of State
is "a State" only "in his or her public capacity" (s 16(1)(a)). Asserted.

### 7. Injuries in Singapore and local property are not immune, but the embassy itself is

s 7 removes immunity for death, personal injury or property damage caused by an act or
omission in Singapore, with no commercial condition. s 8(1) covers immovable property in
Singapore, but s 19(1) excludes proceedings about a State's title to or possession of
diplomatic mission property. Part 2 does not apply at all to criminal proceedings,
visiting armed forces, or taxation other than customs, excise, GST and tax on
commercial premises (s 19(2), s 13). Asserted.

## What would need doing before this is worth anything

- In the encoding "Part 2 does not apply" (s 19(2)) yields "not immune under Part 2";
  it says nothing about whatever immunity applies outside the Act. That reading is an
  inference about how to present the result, not something the text states.
- The case-law meaning of "exercise of sovereign authority" (s 5(3)(c), s 16(2)) and of
  "in use ... for commercial purposes" (s 15(4)) is reduced to a flag.
- s 12 (ships and cargo), s 10, the pre-1979 transitional rule, and the effect of any
  s 17 Presidential order were not encoded; no orders or cases were retrieved.
