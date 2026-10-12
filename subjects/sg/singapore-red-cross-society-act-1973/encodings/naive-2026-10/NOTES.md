# Singapore Red Cross Society Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/5/2023"), deposited at `../../registers/source-bundle/SRCSA1973.txt`. The revised
edition incorporates amendments up to 1 December 2021; the latest amendment annotated
is Act 11 of 2023 (in force 1 May 2023), against s 9(2).

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0214** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act has twelve sections and mostly constitutes the Society. For a person or
business outside it, the answer is s 10. This row takes s 10 (the emblem and the
offence), s 12 (where the Society's money may go), s 3(3) (membership), ss 7(2) and 8
(the Chairperson), s 9(2) (rules, with the Director-General of Health's approval) and
the four grounds named in s 5(a). Not encoded: s 1, s 2, s 4 (Geneva Conventions
recognition), s 6 (the President as patron), s 9(1) (general powers) and s 11 (the
1973 transfer of the Association's property, liabilities and staff).

## What the Act turns out to say

### 1. Calling your business "Red Cross" is a crime, and the text gives no defence

s 10(1): no person other than the Society and any person authorised by the Minister may
use the red cross on a white ground, or "the words "Red Cross" or "Geneva Cross"". The
maximum is a fine of $10,000, 6 months, or both (s 10(2)). The text states no mental
element, no good-faith or prior-use exception, and no exception for a word used in a
different sense. A shop named "Red Cross Pharmacy" without Ministerial authorisation
is caught on the face of the text. Asserted.

### 2. Only the red cross and two phrases are reserved

s 10 does not name the red crescent, the red crystal, a green pharmacy cross or the
Swiss flag itself (a white cross on red). The encoding treats them as outside s 10.
Whether another Act protects them was not looked at; this is a reading of s 10 alone.
Asserted.

### 3. No profit to members, but members may be paid for work

s 12: the Society's income and property go "solely towards the promotion of the
objects" and none may go to members "by way of dividend, bonus or otherwise by way of
profit". The proviso saves good-faith remuneration to an officer, employee or member
"in return for services rendered". Remuneration not in good faith is not saved.
Asserted.

### 4. The Society's rules need the Director-General of Health's approval

s 9(2), as amended by Act 11 of 2023 from 1 May 2023, lets the Council make rules on
seven listed matters "with the approval of the Director-General of Health". What the
provision said before the amendment is not in the deposit. The encoding reads approval
as a condition of the power and treats a topic outside (a) to (g) (a levy on
non-members, invented for the test) as outside it; both readings are inferences.
Asserted.

### 5. A Chairperson's replacement serves only the rest of the term

s 7(2): the President appoints the Chairperson for 3 years, with re-appointment
possible. s 8(1): the President may revoke "at any time" if the President "considers it
desirable in the interests of the Society". s 8(3): a replacement after death,
revocation or other vacancy is appointed "for the unexpired period". The Act says a
resignation is "by writing addressed to the President" but not when it takes effect.
Asserted.

### 6. Membership is the 1973 members plus those admitted under the rules

s 3(3). The Act leaves classes of member and terms of admission to the rules (s 9(2)(b)),
which were not retrieved. Asserted.

## What would need doing before this is worth anything

- The Society's rules and any Ministerial authorisations under s 10(1) were not
  retrieved.
- No prosecution under s 10 or case law was searched.
- Other law on the protective emblems (for example any Geneva Conventions legislation)
  was not read, so finding 2 says nothing about whether those signs are free to use.
