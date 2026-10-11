# Maritime Conventions Act 1911 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The latest amendment annotated is Act 3 of 2019 (Merchant
Shipping (Miscellaneous Amendments) Act 2019, ss 18 and 19, commenced 24 July
2021), which repealed s 7 and is marked against s 8(1).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is **REQ-0109** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Act has ten sections, so the row takes nearly all of it: ss 1, 2,
3, 6, 8 and 9(4), (5). Not encoded: s 5 (death and injury claims may be brought in
rem or in personam; a comment only), s 9(1) to (3) (territorial extent, still listing
1911 dominions), s 10, the limitation of liability that ss 1(3), 2(2)(b) and 3(2)
preserve but do not state, the Rules of Court behind the discretionary extension in
s 8(3)(a), and the penalty for the s 6 offence, which this Act does not state.

## What the Act turns out to say

### 1. Property loss is split by fault; death and injury are not

s 1(1) divides liability for damage to the colliding ships, their cargo, freight
(which s 1(4) says "includes passage money and hire") and property on board "in
proportion to the degree in which each ship was in fault". But s 2(1) makes the
owners' liability for loss of life or personal injury on board "joint and several":
the injured person may take the whole of the damages from either ship at fault,
however small its share. A 20%-at-fault ship can be made to pay 100% of an injury
claim. Asserted.

### 2. The overpaying ship gets its money back, but only what the victim could have got

s 3(1) lets owners who paid more than their proportion recover the excess from the
other ship. s 3(2) caps it at what "could ... have been recovered in the first
instance as damages" from that other ship, so a statutory or contractual limitation
or exemption the other ship enjoyed against the victim also protects it against
contribution. Paying $500,000 at 20% fault gives $400,000 back, or only $300,000 if
that is all the victim could have recovered from the other ship. Asserted.

### 3. Equal shares only when fault cannot be weighed, and never for a blameless ship

Where "it is not possible to establish different degrees of fault, the liability
shall be apportioned equally" (s 1(1)), yet s 1(2) says no ship is liable for loss
"to which her fault has not contributed". The encoding lets s 1(2) win: a blameless
ship pays nothing even when degrees cannot be established. s 3 has no equal-shares
fallback of its own. Asserted.

### 4. A master must save lives, even an enemy's, unless it would seriously endanger his own ship

s 6(1) makes it an offence for the master or person in charge to fail to "render
assistance to every person, even if such person be a subject of a foreign State at
war with Singapore, who is found at sea in danger of being lost", so far as he can
without "serious danger to his own ship, her crew and passengers". The duty is to
persons, not property, and complying keeps the right to salvage (s 6(2)). No penalty
appears in this Act; s 10 construes it with the Merchant Shipping Act 1995, which was
not read. Asserted.

### 5. Two years against the other ship, one year for contribution, and an extension the court must give

s 8(1): claims against a ship or her owners for damage to "another ship" or injury to
a person "on board her" must be commenced within 2 years of the damage; s 8(2):
contribution within one year of payment. s 8(3)(b): the court "shall" extend the
period if there was no reasonable opportunity to arrest the defendant ship within
the jurisdiction or in the plaintiff's home waters. Reading the period as ending on
the anniversary date is an inference about counting. The text of s 8(1) does not
describe a passenger's claim against the ship she was travelling on, nor a claim for
damage to a pier; the encoding says the 2-year period does not govern those, which
is a reading of the words, not a decided point. Asserted.

### 6. A demise charterer stands in the owners' shoes

s 9(5): where "by virtue of any charter or demise, or for any other reason, the
owners are not responsible for the navigation and management of the ship", the Act
reads "owners" as the charterers or others so responsible. Asserted.

## What would need doing before this is worth anything

- The Merchant Shipping Act 1995 (construed as one with this Act by s 10) was not
  read: the s 6 penalty and the limitation-of-liability rules live there or in
  other law.
- No admiralty case law was searched, in particular on how degrees of fault are
  assessed, on damage to third-party property such as piers, and on counting the
  s 8 periods.
- The Rules of Court governing the discretionary extension in s 8(3)(a) were not read.
- Only two-ship collisions are modelled for s 1 and s 3; s 1 and s 3 speak of "2 or
  more ships".
