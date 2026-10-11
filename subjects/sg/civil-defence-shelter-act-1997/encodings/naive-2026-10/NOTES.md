# Civil Defence Shelter Act 1997 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions as the example rows show them (the skill itself was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CDSA1997.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31 December
2021". The latest amendment annotated in the body is [15/2010], on s 23.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0138** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short, so this row takes nearly everything an owner or occupier meets: which
new homes need a shelter (ss 2, 3), public shelters (s 5), the standing duties and their
penalties (ss 4, 6, 8), when the emergency Parts switch on (s 1(3), (4)), emergency
entry and refuge (ss 9 to 11), peacetime use (s 12), entry on notice (s 15(3)), deemed
service (s 19), the other offences (ss 17, 18, 28(2)), officers' liability (s 25) and
composition (s 26). Not encoded: the s 7 designation discretion, administration and
specifications (ss 13, 14), forcible entry (s 16), ss 20 to 24, exemption (s 27), the
other regulation-making powers, and the Schedule of nine MRT-station public shelters. The
regulations and the Commissioner's specifications were not retrieved.

## What the Act turns out to say

### 1. A household shelter in your flat is not opened up to the public, and the Commissioner cannot force entry to prepare it

s 11 binds the owner or occupier of a **storey, public or improvised** shelter to let
"any person" enter and take refuge in a designated period. A household shelter is not in
the list. Likewise s 10 lets the Commissioner enter, do the preparation works (including
"the seizure and removal of any property") and recover the cost only for storey, public
or improvised shelters. A household-shelter owner who ignores a s 9 notice is left to the
s 9(2) fine. Asserted.

### 2. Only buildings whose plans were lodged on or after 1 May 1998 need a shelter, and only new builds

s 2 defines "new house" and "new building" by both the works (on vacant land or in place
of a demolished building) and the plans date (lodged "on or after 1 May 1998"). A plan
lodged on 30 April 1998, or an extension of an existing building, triggers no s 3 duty.
Hotels, hostels, dormitories and nursing homes are excluded from "house" and "flat".
In a block of flats each storey may substitute one storey shelter for household shelters
in every flat (s 3(2)(b)). Asserted.

### 3. Private non-residential buildings carry no shelter duty under the Act

s 5 lets the Commissioner require a public shelter only of a **statutory board**, in a
new non-residential building it owns. Nothing in the Act requires one of a private
office or mall (an inference from the absence of any other provision; regulations were
not read). Asserted for the s 5 conditions.

### 4. The emergency Parts last seven days without the President

Parts 4 and 5 operate only under a Minister's order under s 1(3), when an emergency is
"imminent". s 1(4): the order lapses after 7 days "unless it has been made with the
approval of the President". Asserted (day 7 in force; day 8 only with approval).

### 5. Penalties differ more than the near-identical duties suggest

The duty wording in ss 4, 6 and 8 is the same, but a household or storey shelter breach
is a fine to $5,000 plus $250 a day, while a public or improvised shelter breach adds up
to 6 months' imprisonment and $500 a day. Failing to prepare a shelter on notice (s 9),
refusing refuge (s 11) and unauthorised use (s 12) are fine-only, to $10,000 plus $500 a
day. Obstruction (s 18) can bring 6 months but no daily fine. Composition is capped at
$500, and only for prescribed offences (s 26). Asserted.

### 6. Refusing refuge has a defence; harming a shelter has an escape hatch

s 11(3): it is a defence to prove "all reasonable steps" were taken to let in those who
needed refuge. Under ss 4, 6 and 8 an alteration that would impair the shelter is lawful
with the Commissioner's written permission; maintenance and written works orders have no
such exception. Asserted.

### 7. Emergency service is fast and needs no paper

Once an order is in operation, notices may be served by broadcast, siren, telephone or
fax (s 19(2)); most are deemed received 6 hours later. Registered post takes 48 hours,
affixing to the building 24 hours (s 19(3)). Asserted.

## What would need doing before this is worth anything

- The Civil Defence Shelter Regulations and the Commissioner's technical specifications
  were not retrieved; they fill in what "maintain" and "permitted use" mean.
- No s 27 exemption orders, compoundable-offence lists or cases were searched.
- s 19(3)(d) newspaper service ("by noon on the day following") is not modelled.
- "Every day or part of a day" is counted as whole days.
