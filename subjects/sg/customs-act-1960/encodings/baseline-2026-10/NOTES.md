# Customs Act 1960 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

This encoding replaces the encoding of this Act moved to solutions on 2026-10-19
and the first-pass encoding `naive-2026-10`. It covers everything the first pass
covered, and reuses the first pass's hand-checked fines where they still hold.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
30 September 2026 (amendments to Act 16 of 2026), as deposited at
`../../registers/source-bundle/CA1960.txt`.

**Checks:** one module, one case file. 60 assertions satisfied, 0 errors,
0 warnings, with the stable `l4` from VS Code extension 1.6.98. One `#TRACE`
runs the s 93 duty as a regulative rule and ends `FULFILLED`.

## Seat

**The traveller crossing Singapore's border**, and after a seizure the owner of
the goods or vehicle seized. The traveller is the person this Act most often
reaches: at the Red or Green Channel, when searched, when questioned, when
goods are seized, and when leaving by car. Every decision is phrased as that
person would ask it (`Must I declare and pay duty before I proceed`,
`What is the least I can be fined`, `By what date must my written claim be made`),
and every fact is one the traveller could state.

The 2026-10-18 defaults, one by one:

- **The Act alone, with the instruments that set its numbers brought in if
  deposited.** Followed. None is deposited, so the duty evaded, the duty free
  allowance (whether I exceed it), the compoundable-offence list and the
  minimum fuel under the s 136 order are inputs, and each place says so.
- **The actors the text names.** Followed: the proper officer, the senior
  officer, the Director-General, the court, the District Judge or Magistrate.
- **A judgment handed to someone else answered conditionally.** Followed: the
  Director-General's satisfaction (s 19(3)(b)), the court's finding of no
  reasonable or probable cause (s 127), and a senior officer's decision to
  compound (s 126) are inputs, never guessed.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed: "specified offence", "relevant tobacco products",
  "uncustomed goods" (via s 93(3)), the s 128KA vehicle owner/hirer split and
  "owner" including a hire-purchase hirer are worked out. "Duty free allowance"
  is not defined in the Act and is asked as a fact; so is "specified goods",
  which turns on whether another offence was committed.
- **One case is the text's natural unit.** Followed: one arrival, one search,
  one seizure, one offence, one departure.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in scope, machinery out.** Followed. Officers,
  warehousing, licensing, drawback and the regulation-making powers are out.

## Why this scope

The Act is long (about 300 KB as deposited) and most of it addresses
importers, warehouse licensees, manufacturers and ship masters. This encoding
keeps to the provisions a traveller most meets: declaring (s 93), search
(s 109), questions (s 129), the baggage, possession and duty-free-allowance
offences and their penalties (ss 128 to 128L), the presumptions (ss 115, 115A,
128L(6)), seizure and what follows (ss 110(3), (4), 124, 126(2), 127), prison
in default of a fine (s 119), refunds and short levies (ss 19, 20) and the fuel
rule for leaving by car (s 136). Left out: Parts 2 to 11 otherwise, most of
Part 12, search warrants and arrest, ss 128A, 128C, 128D, 128F to 128H, 128K,
130 to 135 and 137 onwards.

## What the Act turns out to say

### 1. The Green Channel with goods over the allowance is a presumption of guilt

s 93(4): a person who goes through the Green Channel with dutiable goods over
the allowance "is presumed, until the contrary is proved, to be in possession
of uncustomed goods", and s 93(3) deems unpaid goods uncustomed. Possession
of uncustomed goods is a s 128I offence. Asserted.

### 2. Giving away a duty-free bottle is a specified offence with a minimum fine

s 128J catches one who "gives away ... to any person in Singapore goods which
are the person's duty-free allowances". s 128L(7) makes it a specified offence.
On $40 of duty the floor is $400 and the ceiling $5,000; where the duty cannot
be ascertained, there is no floor and the ceiling is $10,000. Asserted.

### 3. The minimum fines are floors, and tobacco raises them

s 128L(2): 10 times the duty or $5,000, whichever is less, with a $1,000 floor
for tobacco products, so $10 of duty on cigarettes carries $1,000 at least.
Over 2 kg of tobacco (s 128L(4)): 15 times the duty and up to 3 years; $2,000
of duty gives $30,000 to $40,000. Asserted.

### 4. A repeat offender with over 2 kg of tobacco must go to prison

s 128L(5A) says the person "shall be punished with" a fine **and** up to
6 years, where (4) and (5) say "or to both". On $2,000 of duty the fine is at
least $60,000. Asserted.

### 5. Forgetting to declare is no defence, and knowing is presumed

ss 128(2), 128B(2), 129(2): "it is no defence to allege" inadvertence or lack
of intent; s 128B(2) adds not knowing a declaration was required. For the
specified offences s 128L(6) deems the goods known to be dutiable, uncustomed
or prohibited "unless the contrary is proved by the person". Asserted.

### 6. Lending your car can be an offence in itself (since 1 April 2025)

s 128KA(2), added by Act 6 of 2025: an owner who lets someone use the vehicle
to carry goods tied to a smuggling offence is guilty "unless the owner ... has
exercised due care", fine up to $10,000. If the owner had hired it out, the
hirer and not the owner is the one named. s 128KA is not in the list of
specified offences, so the s 128L floors do not apply to it. Separately,
s 115A(3) presumes goods found in a vehicle to be in the possession of the
owner and of the person in charge. Asserted.

### 7. You may insist on some things when searched

s 109: a person searched may ask for a senior officer to be present and must
then not be searched without one (but may be detained until one comes); may
ask to be present at the search of their baggage; and "A woman must not be
searched except by a woman." Asserted.

### 8. You need not answer a question that would incriminate you

s 129(3): "Nothing in this section obliges a person to answer any question
which would have a tendency to expose the person to a criminal charge or to a
penalty or forfeiture." Otherwise refusing is an offence ($5,000 or
12 months). Asserted.

### 9. Seized goods are lost after one month unless you claim in writing

s 124(1): with no prosecution, seized goods are "deemed to be forfeited at the
expiry of one month from the date of seizure unless a claim ... is made before
that date"; s 124(2) requires written notice to a senior officer. Goods seized
on 3 March 2026 must be claimed before 3 April 2026. The claimant carries the
s 115 burden (s 124(6)). s 110(3) requires written notice of the seizure and
its grounds unless the seizure was on the owner or in their presence.
Asserted.

### 10. Compounding releases what was seized, with two exceptions

s 126(2): on payment "any properties seized must be released", unless they are
absolutely prohibited imports or goods made in Singapore without a licence,
which are forfeited. s 127: no costs or damages for a seizure beyond return of
the goods or their value, unless it was "without reasonable or probable
cause". Asserted.

### 11. Five years each way for refunds and short levies, forever for fraud

s 19(3): a refund claim must be made within 5 years and the Director-General
must be satisfied. s 20(1A), (1B): a demand for a short levy must be in
writing, state the amount or circumstances, and be made within 5 years of
payment, unless the shortfall came from the payer's fraud or evasion.
Asserted.

### 12. Permission after being stopped does not undo the fuel offence

s 136(3): permission given after the attempt lets the driver leave "without
affecting any liability ... for such attempt". Driving past the Customs gantry
is presumed an attempt. The minimum fuel is in an order that is not deposited;
the cases use three quarters of a tank as a stand-in. Asserted with permission
given beforehand and with none.

### Inferences, labelled in the module

- s 93(4)'s second limb says "any goods" with no allowance; it is read with
  subsection (1)'s dutiable goods.
- The Act does not say whether s 128L(3) or (4) governs a repeat offender whose
  earlier offence did not involve tobacco and whose present one involves over
  2 kg; the heavier scale (4) is taken.
- s 119's "one additional month for every $100" is read as whole $100 steps
  ($1,000 unpaid gives 14 months).
- "One month" and "5 years" are counted to the same day; a seizure on the
  29th to 31st before a shorter month rolls over, which the Act does not
  address.
- Where the duty cannot be ascertained and the scale is (4), (5) or (5A), or
  the offence is under s 128 or s 128B, the encoding returns `NOTHING`: the Act
  gives no figure for those cases.

## What would need doing before this is worth anything

- **Deposit the subsidiary legislation**: duty rates, the duty free allowances,
  the compoundable offences under s 126, the customs ticket offences under
  s 125A and the s 136 fuel order. Without them no case here computes a real
  fine from real goods.
- **No case law was searched.** Sentencing under s 128L and the reach of the
  s 115A and s 128L(6) presumptions are heavily litigated.
- Search warrants, arrest and computer inspection (Part 13) and the
  importer-facing offences are not encoded.
