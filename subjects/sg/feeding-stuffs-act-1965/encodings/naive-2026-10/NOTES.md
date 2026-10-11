# Feeding Stuffs Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FSA1965.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021; the latest amendment annotated in the body is [11/2019]. The
retrieval metadata calls it the current version as at 1 October 2026. The
arrangement of sections at the top of the deposit is out of step by one; this row
follows the section numbers in the body.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0089**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act has 11 sections,
so the row covers nearly all of it: the licence (s 4), the seller's statutory
statement (s 5), the manufacturer's warranty (s 6), the purchaser's sample (s 7),
arrest without warrant (s 8(3)), the privilege in s 8A(2), every offence (ss 4(5),
10) and the ceiling on penalties in rules (s 11(3)). Not encoded: administration and
appointments (s 3), entry and inspection (s 8(1), (2)), the s 8A procedure beyond
(2), fees paid to the Agency (s 9), and the rule-making power beyond the penalty
ceiling. No rules under s 11 were retrieved, so every prescribed form, particular
and fee is unknown here.

## What the Act turns out to say

### 1. Selling feed that analysis finds dangerous is an offence without fault

s 10(4): where a simple feed, feed concentrate or compound feed that has been sold
is "found on analysis to contain any ingredient deleterious or dangerous to
animals", the seller, manufacturer or proprietor "shall be deemed to be guilty of an
offence". The text gives no knowledge element and no defence; a case where the
seller did not know still convicts. Asserted.

### 2. Two classes of feed: "animal feed", and the three named kinds

The licence (s 4), the warranty (s 6), the deleterious-ingredient offence (s 10(4))
and the refusal-to-sample offence (s 10(6)) apply only to simple feeds, feed
concentrates and compound feeds. The statutory statement (s 5) and the purchaser's
sample (s 7) apply to any animal feed. A "simple feed" exists only once the Minister
gazettes it, so a livestock feed never gazetted, and neither concentrate nor
compound, needs no licence to sell and falls outside s 10(4) and (6) (an inference
from the definitions; whether such feeds exist in practice is not in the text).
Asserted for the encoding's "another animal feed".

### 3. A licence is needed to import, manufacture, process for sale or sell — not to buy

s 4(4) lists the four dealings; buying and keeping feed for one's own animals are not
among them. The Director-General may revoke or suspend a licence "in his discretion,
at any time" (s 4(3)); the Act gives no criteria and no appeal. Asserted (the
dealings; revocation is not modelled).

### 4. The heading says the purchaser furnishes the statement; the text says the seller

s 5 is headed "Obligation to furnish statutory statement by purchaser", but its
words require "every person who sells animal feeds" to furnish it "to the
purchaser". The encoding follows the words. Asserted.

### 5. One penalty for everything in the Act; half of it for rules

Every offence in the Act carries the same maximum, $1,000 or 12 months or both
(ss 4(5), 10(1) to (6)). Rules may impose at most $500 or 6 months (s 11(3)(b)), but
may add cancellation or suspension of a licence (s 11(3)(c)), which the Act's own
offences do not mention. Asserted.

### 6. Arrest without warrant only when identity or flight is in doubt

s 8(3): the Director-General or an authorised officer may arrest a suspect without
warrant only if the person refuses a name and address, gives an address outside
Singapore, or there are reasonable grounds to believe the name or address is false or
that the person will abscond. s 8A(2) lets a person decline a statement that tends to
expose them to a criminal charge, penalty or forfeiture. Asserted.

## What would need doing before this is worth anything

- The rules under s 11 (forms, particulars of the statement and warranty, fees,
  therapeutic substances, the warranty tolerances of s 11(2)(c)) were not retrieved;
  without them the content of every duty is unknown.
- No Gazette notification declaring "simple feeds" was searched, so the class is
  empty in fact as far as this row knows.
- "As soon as possible" in s 5 is not modelled as a deadline.
- No case law was searched.
