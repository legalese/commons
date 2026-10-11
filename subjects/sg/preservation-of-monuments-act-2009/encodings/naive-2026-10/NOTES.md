# Preservation of Monuments Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill and the finished naive rows. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PMA2009.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amendment annotated in the text is [36/2021], the
Preservation of Monuments (Amendment) Act 2021, commenced 30 November 2021 according
to the Legislative History.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0129** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The row covers what an owner, occupier, buyer, contractor or passer-by meets: notice
of dealings (s 11(10), (11)), the dwelling-house saving (s 12), preservation notices
and appeals (s 13), works needing the Board's permission and their defences (s 15),
information notices (ss 16, 17), enforcement-notice appeals and penalties (ss 19, 20),
wilful defacing (s 22), the public-body carve-out (s 22A), forcible entry and
obstruction (s 27(2A), (3)) and composition (s 31). Not encoded: the Board's
functions and powers, appointments, how a preservation order is made and registered
against title, arrest, officers' liability for corporate offences (s 29), the Part 5
transfer from the old Preservation of Monuments Board, the general exemption (s 32),
service of documents and transitional provisions.

## What the Act turns out to say

### 1. Repainting a national monument without permission is an offence even if you did not know it was one

s 15(1) forbids anyone to "repair, renovate, repaint or redecorate" a national or
proposed national monument without the Board's prior written permission, and attaches
no mental element. s 15(1A), which covers acts on a monument "which is a site"
(clearing trees, digging, parking a vehicle, enclosing it), applies only to a person
"knowing or reckless" as to its status. So parking on a protected site in ignorance is
not a s 15 contravention, but repainting a protected shophouse in ignorance is.
Asserted.

### 2. The penalties are heavy, and a company's are double

Unauthorised works (s 15(4)) and ignoring an enforcement notice (s 20(2)) carry, for an
individual, up to $100,000 or 12 months or both plus $5,000 a day after conviction;
"in any other case" up to $200,000 plus $10,000 a day, with no imprisonment. The court
must have regard to any financial benefit from the offence (ss 15(7), 20(3)) and may
order restoration or payment of its cost (s 15(5)). Failing a preservation notice
(s 13(7)) is far lighter: $20,000 plus $200 a day. Asserted (the restoration order
and the financial-benefit factor are described, not encoded).

### 3. The Government and statutory authorities are outside Part 4 on their own land, but the Board is not

s 22A: "Nothing in Part 4 applies" to the Government or a statutory authority "(other
than the Board)" acting under other written law in relation to a monument on State
land or land in its care, control or management. A statutory authority demolishing
part of a monument on land it manages commits no s 15 offence; the same authority on
private land, or the National Heritage Board itself, would. A private person acting in
good faith on another authority's order has only the s 15(8)(b) defence, which they
must prove. Asserted.

### 4. Selling or leasing a monument needs notice to the Board both before and after

s 11(10): anyone who intends to transfer, assign, demise or otherwise deal with a
national or proposed national monument (or land affected by an order) must give the
Board not less than two weeks' written notice beforehand and written notice of
completion within two weeks after. Either failure is an offence up to $10,000
(s 11(11)). Two weeks is encoded as 14 days. Asserted.

### 5. A notice bites while it is under appeal

Preservation and enforcement notices may be appealed to the Minister within 14 days
of service or a longer period the Minister allows (ss 13(3), 19(1)); the Minister's
decision is final. But the notice "takes effect ... despite any appeal ... that is
pending" unless the Minister directs a stay (ss 13(5), (6), 19(4), (5)). Asserted.

### 6. A home lasts only a year as a monument unless the State acquires it

s 12: where a preservation order covers a structure that appears to the Board to be
occupied as a dwelling house, not vested in the Board or the Government, the order
ceases to have effect for that structure if it is not acquired under the Land
Acquisition Act 1966 within one year of the order. Asserted.

### 7. Smaller points

- Information notices: non-compliance becomes an offence only after the 21-day period
  "beginning with the day on which" the notice was served, so day 21 is the last day
  (s 17(1)); a defence if the information could not with reasonable diligence have
  been ascertained (s 17(2)); a knowing or reckless false statement is itself an
  offence (s 17(3)). Asserted.
- Entry is normally "without using force" (s 27(1)), but forcible entry without warrant
  is allowed where an offence under s 13(7), 15(4), 20(1)(a) or 22(1) is reasonably
  suspected and entry is refused or impossible (s 27(2A)). Obstruction alone is not on
  that list. Asserted.
- Composition is capped at the lower of half the maximum fine or $5,000 (s 31(1)), so
  $5,000 is the effective cap for every offence the Act itself creates (each carries a
  maximum of at least $10,000), but not for a regulation offence,
  whose fine may not exceed $5,000 (s 35(3)(b)) and so compounds for at most $2,500.
  Which offences are prescribed as compoundable was not retrieved; the base fine
  (without the daily continuing fine) is used as "the maximum fine". Asserted.
- Who pays for works done in default (described, not encoded): under s 14(b) the
  Board's costs of carrying out a preservation notice are recoverable as a civil debt
  from whoever was owner or occupier "on the date of the preservation notice", so a
  later buyer is not the debtor under that provision; under s 20(1)(c), from the
  person who failed to comply with the enforcement notice.

## What would need doing before this is worth anything

- The regulations under s 35 were not retrieved: they may prescribe further acts
  needing permission (s 15(1)(d)), extra owner duties, and which offences are
  compoundable. "Visiting" and "photographing" are treated as needing no permission
  only because they are not in s 15(1) or (1A); that is an inference.
- The list of national monuments (s 11(12)) and the Board's maintenance guidelines
  (s 13(1)) were not consulted.
- The officers' liability rule (s 29) and the restoration orders (ss 15(5), 22(2)) are
  not encoded.
- No case law was searched.
