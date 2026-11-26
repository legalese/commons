## Procedure layer: the buy-back of a company's own shares (Companies Act 1967 ss 76B to 76K)

Module `sg-proc-share-buyback.l4`, tests `sg-proc-share-buyback-tests.l4`, both in this folder.
The module is a regulative layer over the Boolean encodings in `sga3-76b.l4`, `sga3-76c-76e.l4`, `sga3-76f-76g.l4` and `sga3-76h-76k.l4`: it imports them and calls their gate functions, and it restates none of them.
It is one chain of steps: an authority (s 76C, s 76D or s 76E); in parallel, the lodging of a copy of the resolution (s 76B(9)(a)) and the purchase within the authority (s 76B(7), (9)(c), s 76F); then the notice of purchase (s 76B(9)(b)) and the reduction on cancellation (s 76G(1)); and for treasury shares the dealing and the notice (s 76K(1C), (1D)) and the excess disposed of within 6 months (s 76I(3)).
Every DEONTIC has the type `DEONTIC Party `share buy-back act``.

### The seat of each DEONTIC, and its TIMELINE line

- `s 76B(9)(b) and s 76G(1) after the purchase the directors of a public company lodge the notice of purchase and the company reduces its share capital or profits`
  - Seat: s 76B(9)(b) (src:8467-8493) and s 76G(1) (src:9019-9039).
  - TIMELINE: unit=calendar day; day 0=the day the shares are deemed purchased or acquired, the day the company would, apart from section 76B(5), become entitled to exercise the rights attached to them (s 76B(9)(c)); counting="within 30 days after the purchase or acquisition of the shares" for the notice, the integer line being the count of days with the last day day 30 (sg-periods P1, P2: the day of the purchase is not counted); s 76G(1) puts no time on the reduction, so no clock is encoded for it
- `s 76B and s 76F the company purchases or acquires its shares within the authority while it is solvent`
  - Seat: s 76B(7) (src:8414-8422), s 76B(9)(c) (src:8498-8501), s 76F(1) (src:8939-8954) and s 76F(2)(a) (src:8962-8967).
  - TIMELINE: unit=calendar day; day 0=the day the resolution authorising the purchase is passed; counting="a date on which the authority is to expire" (ss 76C(2)(c), 76D(3)(a), 76E(2)(c)): the purchase may be made on any day up to and including the expiry date, so n is the days from day 0 to the expiry date, computed from the two DATE inputs by DATE_SERIAL by the caller; a public company's purchase is the day it becomes entitled to exercise the rights (s 76B(9)(c)), a private company's is its lodging (s 76B(7)); the solvency of s 76F(4) is tested at the date of the payment, which the caller states
- `s 76B(9)(a) after the resolution the directors of a public company lodge its copy and the company purchases within the authority`
  - Seat: s 76B(9)(a) (src:8459-8465).
  - TIMELINE: unit=calendar day; day 0=the day the resolution mentioned in section 76C, 76D or 76E is passed; counting="within 30 days after the passing of a resolution", the integer line being the count of days with the last day day 30 (sg-periods P1, P2); the purchase window runs in parallel from the same day 0 (RAND) and is the rule above
- `s 76C the company in general meeting authorises an equal access scheme in advance and the lodging and the purchase follow`
  - Seat: s 76C(1) (src:8511-8518) and s 76C(2)(c) (src:8532-8535).
  - TIMELINE: unit=calendar day; day 0=the day of the general meeting at which the company authorises the equal access scheme; counting=silent for the authority (the text sets no time for the meeting); the steps after it count as the two rules above state, the purchase window ending on the expiry date the notice specifies (s 76C(2)(c)), n being DATE_SERIAL of the expiry date minus DATE_SERIAL of the meeting date
- `s 76D the company passes a special resolution authorising a selective off-market purchase and the lodging and the purchase follow`
  - Seat: s 76D(1) (src:8595-8600), (2) (src:8604-8609), (2A) (src:8611-8619), (3)(a) (src:8623-8630) and (7) (src:8706-8716).
  - TIMELINE: unit=calendar day; day 0=the day of the meeting at which the special resolution is passed; counting="not less than 15 days ending with the date of the meeting" for the inspection (s 76D(7)(a)): the 15 days run back from day 0, so they are checked by the existing gate from the two DATE inputs and are not a step of the trace; the consent of s 76D(2A) comes "before passing the special resolution" and is likewise a gate input; the steps after the resolution count as the rules above state
- `s 76E the company in general meeting authorises a market purchase in advance and the lodging and the purchase follow`
  - Seat: s 76E(1) (src:8890-8893) and s 76E(2)(c) (src:8905-8908).
  - TIMELINE: unit=calendar day; day 0=the day of the general meeting at which the company authorises the market purchase; counting=silent for the authority (the text sets no time for the meeting); the steps after it count as the rules above state, the purchase window ending on the expiry date the notice specifies (s 76E(2)(c))
- `s 76E(1) the company must not make a market purchase unless it has been authorised in advance by the company in general meeting`
  - Seat: s 76E(1) (src:8890-8893).
  - TIMELINE: unit=calendar day; day 0=the day the company makes a purchase or acquisition of its own shares on a securities exchange; counting=silent (the bar has no time limit; whether the purchase was authorised in advance is a gate input)
- `s 76F(3) a director or chief executive officer must not approve or authorise the purchase, acquisition or release knowing that the company is not solvent`
  - Seat: s 76F(3) (src:8978-8983).
  - TIMELINE: unit=calendar day; day 0=the day the director or chief executive officer approves or authorises the purchase, acquisition or release; counting=silent (the text puts no time on the offence)
- `s 76K(1D) after the cancellation or disposal the directors of a public company lodge the prescribed notice`
  - Seat: s 76K(1D) (src:9197-9201).
  - TIMELINE: unit=calendar day; day 0=the day the public company cancels or disposes of the treasury shares; counting="within 30 days after the cancellation or disposal of treasury shares", the integer line being the count of days with the last day day 30 (sg-periods P1, P2)
- `s 76K(1C) the public company cancels or disposes of its treasury shares and the directors then lodge the prescribed notice`
  - Seat: s 76K(1C) (src:9174-9175), calling the rule for s 76K(1D) above.
  - TIMELINE: unit=calendar day; day 0=the day the public company cancels or disposes of the treasury shares; counting="at any time" for the company's own step (the text sets no time, so no clock is encoded for it); the directors' notice then follows through HENCE with the 30 days of the rule above
- `s 76I(3) the company must dispose of or cancel the excess treasury shares before the end of the 6 months and a public company's directors then lodge the notice`
  - Seat: s 76I(3) (src:9086-9090), calling the rule for s 76K(1D) after the disposal.
  - TIMELINE: unit=calendar day; day 0=the day on which the contravention of s 76I(1) or (2) occurs; counting="before the end of the period of 6 months beginning with the day on which that contravention occurs, or such further period as the Registrar may allow": the day of the contravention is day 1 of the 6 months (sg-periods P10), so the period ends the day before the same date 6 months on, the last day being in time, and n is DATE_SERIAL of that last day minus DATE_SERIAL of the day of the contravention, computed here from the DATE inputs; where the Registrar has allowed a further period the caller states its last day and n runs to it; the public company's notice then runs "within 30 days after the cancellation or disposal" from the day of the cancellation or disposal (through HENCE), the integer line being the count of days (P1, P2)

### How the clocks run

A step that follows another through HENCE counts from the day the earlier step happened.
So the lodging of the copy (30 days from the resolution) and the purchase window (from the resolution to the expiry date) run together (RAND) from day 0, the resolution, and the notice of purchase follows the purchase through HENCE, so its 30 days run from the purchase day, not from the resolution.
The 15 days of s 76D(7)(a) run backwards from the meeting and the consent of s 76D(2A) comes before the resolution: both are checked by the existing gates from the inputs, and neither is a step of a trace.
The 6 months of s 76I(3) are counted by `period: the last day of a period beginning with` (sg-periods P10, assumed and not ruled by a lawyer) and turned into a day count with DATE_SERIAL; the 30-day periods are bare day counts (P1, P2: the day of the event is not counted, so the last day is day 30).

### Forks

- FORK: s 76B(9)(b) | "the directors of the company" are one party, Director "D", who lodges for all of them, and a public company's failure is a BREACH of that party | a breach of each director separately
- FORK: s 76G(1) | the text states no time for the reduction, so the period is the found input of the section module (`sga3-76f-76g.l4:268-286`, Interpretation Act 1965 s 52: all convenient speed; decided, assumed, not ruled; see `notes/lest-without-deadline.md`), counted from the purchase, and a late or missing reduction is a BREACH by the company | a MUST with no WITHIN and no breach path, or a time taken from the 30 days of s 76B(9)(b)
- FORK: s 76G(1) | the duty arises only where the shares are cancelled under s 76B(5) and not held in treasury under s 76H, which the caller states in one input | the duty arises on every purchase
- FORK: s 76B(7) | for a private company the lodging is the step by which the purchase is made, so the permitted act is the lodging and no clock runs from it | the lodging as a duty after a separate purchase
- FORK: s 76B(9)(c) | a public company's purchase is the day it becomes entitled to exercise the rights, because (c) deems the shares purchased then | the day the agreement is made
- FORK: s 76C(2)(c) | the permission to purchase lapses at the expiry date with nothing owed (LEST FULFILLED) | a purchase after expiry as a BREACH
- FORK: s 76F(2)(a) | where the company is not solvent the very act the permission names (becoming entitled, for a public company; lodging, for a private one) is barred, and doing it ends FULFILLED with 'the purchase is not lawful' beside it, because the text says only that no purchase is lawful and lays no duty on a named party; the officer's offence is s 76F(3), encoded separately (SG-share-buyback-1, independent review) | a BREACH by the company, as the rule stood before the review
- FORK: s 76B(9)(a) | the lodging of the copy and the purchase are two parts of one rule that run together, each from day 0 (RAND), because (a) runs from the resolution and not from the purchase | the lodging chained after the purchase through HENCE
- FORK: s 76C(2)(c) | where the expiry date is later than the date the next annual general meeting is or is required to be held, the authority step is still open but nothing follows it, no copy to lodge and no purchase window | the authority valid up to the stated expiry date, or the resolution not passed at all
- FORK: s 76C(1) | the authority is "authorised in advance by the company in general meeting" and the text names no majority, so the step is a MAY of the company with no resolution type | an ordinary resolution
- FORK: s 76D(2A) | the consent is a bar on passing the special resolution: where the existing gate says the consent was not obtained before, the company SHANT pass it and a pass is a BREACH, although the text says only that the company "must, before passing the special resolution, obtain the consent" | the consent as a step of the chain before the resolution
- FORK: s 76D(7) | where the inspection requirement or the expiry date fails, the special resolution may still be passed but is not effective, so nothing follows it | the resolution cannot be passed at all
- FORK: s 76E(2)(c) | as for s 76C(2)(c): an expiry date later than the next annual general meeting leaves the authority step open and nothing after it | the authority valid up to the stated expiry date
- FORK: s 76E(1) | the bar is a SHANT of the company with a BREACH where the purchase is made without advance authority, although the text states no consequence | no breach, the purchase being merely unauthorised
- FORK: s 76F(3) | the company's insolvency and the person's knowledge of it are gate inputs and the forbidden act is the approval alone | the knowledge inside the act, as "approve ... knowing that the company is not solvent"
- FORK: s 76F(3) | the existing s 76F(1) gate is called with the payment kind fixed to (1)(a), the payment for acquiring a right with respect to a purchase, although the rule's act also covers a release of obligations; the solvency question of s 76F(4) is the same for each kind | a gate call for each kind of payment
- FORK: s 76F(3) | the penalty ("a fine not exceeding $100,000 or to imprisonment for a term not exceeding 3 years", "or" and not "or both") is in the BECAUSE text and not a step | the conviction as a further step
- FORK: s 76K(1D) | the notice is owed by Director "D" for all the directors, and only by a public company: a private company's notice under s 76K(1A) is the means by which it cancels or disposes, with no time and no duty | the private company's lodging as a MUST with no clock
- FORK: s 76K(1C) | the company's cancellation or disposal is one step, a MAY with no clock, whatever the kind of dealing, and the existing gate says which kinds the list allows | one step for each of (a) to (e)
- FORK: s 76I(3) | "before the end of the period" is read as on or before the last day of the 6 months | strictly before the last day
- FORK: s 76I(3) | the Registrar's further period is an input fixed before the chain starts (a flag and a last day), because the text names no day by which the Registrar must allow it | the allowance as a step of the Registrar after the 6 months lapse
- FORK: s 76K(1D) | a private company has no step after the cancellation or disposal: s 76K(1A) says it may cancel or dispose by lodging a notice, a means with no time and no duty | the private company's lodging as a MUST with no clock

### What the text leaves silent (no clock and no breach is encoded for it)

- The day of the general meeting that authorises a purchase (ss 76C(1), 76D(2), 76E(1)): the authority is a MAY with no time limit, so a chain that never starts stays open.
- A number of days for the reduction of capital or profits in s 76G(1): the found period of all convenient speed sets it (see "Do-once duties and the found period").
- Any consequence of a notice that does not comply with s 76C(2), s 76D(3) or s 76E(2): only the expiry date is gated (fork s 76C(2)(c)); the other contents are not encoded.
- Any consequence of passing a selective resolution without the consent of s 76D(2A), or of a market purchase without authority (s 76E(1)): the module makes each a forbidden act with a BREACH, as a fork.
- What "no purchase or acquisition ... is lawful" (s 76F(2)(a)) leads to: the module bars the act the permission names (becoming entitled to exercise the rights, or a private company's lodging) while the company is not solvent, and doing it ends FULFILLED with the unlawfulness beside it; the text states nothing else, and lays no duty on a named party.
- When the Registrar may allow the further period of s 76I(3): the module takes it as an input fixed before the chain starts.
- A time for a private company's notice under s 76K(1A) and for the Registrar's updating of the electronic register (ss 76B(8), 76K(1B)): the module encodes no step for either.
- Whether the "general meeting" of ss 76C(1) and 76E(1) needs an ordinary or a special resolution: the text names none, so the module names none.

### Which build verified the traces

The traces were run with the unstable builds `unstable-20261125-a50cbd0` (first build checked, 48 traces) and `unstable-20261126-90eed8e` (after the independent review, 51 traces) and with the stable build the stable build 112, with `JL4_LIBRARY_PATH` unset.
Unstable `unstable-20261126-90eed8e`: 51 traces, 51 match the class written above each from the text, zero error diagnostics, the 3 `#ASSERT`s satisfied, and no warning from the files.
Stable: 51 traces, 48 match, 3 differ; zero error diagnostics; the 3 `#ASSERT`s satisfied.
Two scratch copies were used as a sensitivity check before the independent review and deleted.
Both were run when the test file had 40 traces and before the s 76K(1C) rule and its helper were added in their present form, and before the insolvent branch was changed to forbid the permitted act, so the 30 days of the s 76K(1D) rule, the later traces and that branch were never under a mutant.
One copy had the two `LEST FULFILLED` removed: the same classes on both builds (40 of 40 on unstable, 38 of 40 on stable).
The other had each of the three `WITHIN 30` then in the module made `WITHIN 31` and `6 Months` made `5 Months`: 6 of the 40 traces changed class on unstable, so those traces do read the day counts.

### READS-DIFFERENTLY-ON-MAIN

The list is at the end of `sg-proc-share-buyback-tests.l4`.
Three traces read differently on the stable build, by test-file line:

- test-file line 82: expected FULFILLED, MAIN prints RESIDUAL: No purchase before the authority expires: the permission lapses with nothing owed.
- test-file line 200: expected FULFILLED, MAIN prints RESIDUAL: Not a class case (all the shares in the class, or no class): no consent is needed; the resolution on day 0, then the copy on day 30 while the purchase
- test-file line 325: expected FULFILLED, MAIN prints RESIDUAL: The authority expired on day 10 and the company becomes entitled to exercise the rights on day 11: the permission to purchase has lapsed with nothing 

Each is a MAY with a WITHIN that lapses: the unstable build reads the permission as lapsed with nothing owed (FULFILLED); the stable build prints a still-open notice-of-purchase duty (the step after the MAY), RESIDUAL.

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST or branch, and here.
This unit has these, and two traces moved from BREACH to FULFILLED or RESIDUAL after the independent review:

- `s 76F(2)(a)`: "no purchase or acquisition ... is lawful" (src:8965-8967) lays no duty on a named party, so the act the permission names, done while the company is not solvent, ends FULFILLED (and the directors' lodging of the copy stays open where it was open).
- `s 76C(2)(c)`, `s 76D(3)(a)`, `s 76E(2)(c)`: the permission to purchase lapses at the expiry date with nothing owed.

The BREACHes that stay are duties and prohibitions on a named party: the directors' notices (s 76B(9)(a), (b), s 76K(1D)), the reduction (s 76G(1)), the disposal of the excess (s 76I(3)), the consent before the special resolution (s 76D(2A), "the company must, before passing"), the market purchase without authority (s 76E(1), "must not") and the director's approval (s 76F(3), with its offence).

### Do-once duties and the found period

Decided by Claude on 2026-11-27 (assumed, not ruled), to align the layer with the section modules (`notes/lest-without-deadline.md`): a duty to do a thing once with no number of days in the text takes a rule-level input of days, and a late act is a BREACH by the bearer.

| duty | class | input | twin in the section module |
| ---- | ----- | ----- | ---- |
| s 76G(1): the company must reduce its share capital or profits by the purchase price | no time stated, Interpretation Act 1965 s 52 | `the period of all convenient speed, as found` | `sga3-76f-76g.l4:282-290` |

The input is passed down the chain (`s 76B(9)(b) and s 76G(1)`, `s 76B and s 76F`, `s 76B(9)(a)`, `s 76C`, `s 76D`, `s 76E`) as a plain argument; the tests pass 30.

### Duties left without a clock

None among the do-once duties of this unit: the notices, the disposal of the excess and the lodging of the copy have days in the text, and the authorities (ss 76C(1), 76D(2), 76E(1)) and the dealing with treasury shares (s 76K(1C)) are powers.

### Differences from the existing DEONTIC

The existing DEONTICs for these sections were read after this module and its traces were written.

- **s 76B(9)(a), `sga3-76b.l4:508`.**
  The existing rule applies to any company: a private company that is asked is owed the lodging within 30 days.
  This module applies it to a public company only, because the text begins "Where a public company purchases or acquires shares issued by it" (src:8459-8460), and gives a private company the lodging of s 76B(7) as the step by which it purchases (src:8414-8416).
  The existing rule takes day 0 from the trace; here day 0 is the resolution step of a route, and the lodging runs together with the purchase window.
- **s 76B(9)(b), `sga3-76b.l4:536`.**
  The same public-company gate (src:8459-8460).
  The existing rule has no purchase step before it; here the notice follows the purchase through HENCE, and the purchase is itself limited by the authority's expiry date (src:8532-8535), so a purchase on the day after the expiry date opens no notice duty.
- **s 76E(1), `sga3-76c-76e.l4:928`.**
  The existing rule takes only "authorised in advance" and makes any unauthorised purchase a BREACH.
  This module also asks whether the purchase is made on a securities exchange, because the bar is on a purchase "on a securities exchange (called in this section a market purchase)" (src:8890-8892): a purchase elsewhere is not in the bar, and the rule is FULFILLED at once.
  The party is a `Party` and not a name string.
- **s 76F(3), `sga3-76f-76g.l4:188`.**
  The existing rule has no gate; the knowledge is part of the forbidden act, so every approval done is a BREACH.
  This module gates the rule on the company not being solvent (through the existing s 76F(1) gate) and on the person knowing it (src:8978-8981), so an approval where the company is solvent, or where the person does not know, is FULFILLED.
  The BECAUSE text here carries the penalty ("a fine not exceeding $100,000 or to imprisonment for a term not exceeding 3 years", src:8981-8983); the existing one does not.
- **s 76G(1), `sga3-76f-76g.l4:282`.**
  The existing rule applies to every purchase and has `WITHIN` the found period of all convenient speed and a `LEST BREACH` (`sga3-76f-76g.l4:285-290`).
  This module owes the reduction only where the shares are "cancelled under section 76B(5)" (src:9019-9021), that is, not held in treasury, and takes the same input and the same breach, so the two layers answer alike for a late reduction (since the independent review; before it this module had no clock).
- **s 76I(3), `sga3-76h-76k.l4:181`.**
  The existing rule takes the number of days from the caller and has no gate: it asks for disposal even where treasury shares do not exceed 10%.
  This module counts the 6 months itself, from the day of the contravention (src:9086-9090), gates on the existing s 76I(1) and (2) functions, takes the Registrar's further period as an input, and chains the s 76K(1D) notice after the disposal.
- **s 76K(1D), `sga3-76h-76k.l4:431`.**
  The existing rule applies to any company, with no step before it.
  This module applies it to a public company only ("Where a public company cancels or disposes treasury shares in accordance with subsection (1C)", src:9197-9198), after a dealing that the existing s 76K(1C) gate allows, and from the day of that dealing.
- **s 76J(2), `sga3-76h-76k.l4:282`, and s 76K(3), `sga3-76h-76k.l4:496`.**
  This module has no counterpart: neither has a clock, and neither is a step of the chain.
- **Nothing in the existing DEONTICs** covers the authority steps of ss 76C, 76D and 76E, the 75% consent and the inspection gate of s 76D, the 20% limit, or the solvency of the purchase under s 76F(2)(a).

### What was not encoded, and why

- The 20% limit of s 76B(3) to (3E) and the "relevant period" of s 76B(4): a numeric gate with no step of its own; `sga3-76b.l4` already answers it, and nothing in the text makes it a duty with a clock.
- The notice contents of ss 76C(2), 76D(3) and 76E(2) other than the expiry date, and the resolution contents of ss 76C(3), 76D(4) and 76E(3): they are conditions on the document, not steps with a time; the existing gates answer them.
- The variation, revocation and release of an authority or agreement (ss 76C(4), 76D(5), (9), (12), 76E(4)) and contingent purchase contracts (s 76DA): outside the chain named for this unit.
- ss 76H(1), (2) and 76J (the company may hold treasury shares; it must be entered in the register; it must not exercise their rights): powers and bars with no clock and no step in the chain.
- ss 76K(1) to (1B), (2), (3) and (4): the dealings are in the gate of s 76K(1C); the private company's notice (1A) is a means with no time; the rest are definitions and bars with no clock.
- The existing module's own `Party` constructors are used; no new party is declared.
- No existing function needed changing.
