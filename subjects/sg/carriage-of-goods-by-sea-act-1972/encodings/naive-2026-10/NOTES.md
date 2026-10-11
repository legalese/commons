# Carriage of Goods by Sea Act 1972 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CGSA1972.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021; no later amendment is annotated. The Schedule is "The Hague Rules
as amended by the Brussels Protocol 1968" (the name "Hague-Visby Rules" used in
`encoding.json` is the common name, not the deposit's).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0099**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The person here is a
shipper, a cargo owner or a holder of a bill of lading whose goods are lost or
damaged at sea.

The Act itself is six sections; almost all of its substance is the Schedule. This row
takes when the Rules govern (ss 2, 3, Articles I(c), V, X), what the carrier answers
for (s 4, Articles III(1), (2), IV(1), (2), (4)), the package limit (Article IV(5)),
notice and the time bar (Article III(6), (6bis)), what the bill proves (s 3(5), s 5,
Article III(4)), which contract terms survive (Articles III(8), V, VI, VII) and
dangerous goods (Article IV(6)). Not encoded: the s 3(8) franc conversion order, the
valuation rule of Article IV(5)(b), the shipper's indemnity (Article III(5)) beyond
s 5, Article IV bis, the "shipped" bill (Article III(7)), s 6 and Articles VIII, IX,
and the list of contracting States.

## What the Act turns out to say

### 1. The limit is written in gold francs, and the dollar figure is not in the Act

Article IV(5)(a) caps liability at "10,000 francs per package or unit or 30 francs
per kilo of gross weight ... whichever is the higher", and (d) defines a franc as
"65.5 milligrammes of gold of millesimal fineness 900". The Singapore-dollar
equivalent is left to a ministerial order under s 3(8), which is not in the deposit.
So a cargo owner reading the Act cannot learn the cap in dollars. The encoding works
in francs: a single 5,000 kg machine worth 500,000 francs recovers 150,000 (the
weight limit beats the one-package limit of 10,000). Asserted.

### 2. Declaring the value removes the cap; mis-stating it removes everything

The cap does not apply if "the nature and value of such goods have been declared by
the shipper before shipment and inserted in the bill of lading" (IV(5)(a)), nor if the
carrier acted "with intent to cause damage, or recklessly and with knowledge that
damage would probably result" (IV(5)(e)). But if the nature or value "has been
knowingly mis-stated by the shipper in the bill of lading", the carrier is not
responsible "in any event" (IV(5)(h)) — recovery is nil even where a value was
declared. A higher agreed maximum counts; a lower one does not (IV(5)(g)). Asserted.

### 3. A container is one package unless the bill counts what is inside

IV(5)(c): the packages "enumerated in the bill of lading as packed in" a container
are the packages; "Except as aforesaid such article of transport shall be considered
the package or unit". A container of 20 cartons not listed in the bill is one package
for the limit; one listing 200 cartons is 200. Asserted.

### 4. Shipments from Singapore are covered even when they never leave Singapore

Article X applies the Rules to carriage "between ports in 2 different States", but
s 3(2) extends them to every shipment where "the port of shipment is a port in
Singapore, whether or not the carriage is between ports in 2 different States".
There must still be a bill of lading or similar document of title (s 3(3)); a
non-negotiable receipt is covered only with an express clause (s 3(4)(b)), and charter
parties not at all (Article V). Asserted.

### 5. Deck cargo is excluded only if the bill says so and it is so carried

Article I(c) excludes live animals and cargo "stated as being carried on deck and is
so carried". Cargo carried on deck without that statement stays within the Rules.
Deck cargo and live animals come back in only through an express paramount clause
(s 3(6)), not through s 3(2). Asserted.

### 6. Navigational negligence is excused; careless stowage is not

Article IV(2)(a) excuses the carrier for the crew's "neglect, or default ... in the
navigation or in the management of the ship", and (b) for fire unless caused by "the
actual fault or privity of the carrier". But the carrier must "properly and carefully
... stow" (III(2)), and for unseaworthiness the burden of proving due diligence is
on the carrier (IV(1)); s 4 removes any absolute warranty of seaworthiness. Asserted.

### 7. One year to sue, extendable only by agreement after the event

III(6): the carrier is "discharged from all liability whatsoever" unless suit is
brought within one year of delivery, extendable only "if the parties so agree after
the cause of action has risen". An indemnity action against a third person (6bis)
gets the forum's period, but never less than 3 months from settlement or service.
Late notice of loss does not bar the claim; it only makes removal prima facie
evidence of delivery as described. Counting the year as 12 whole months is an
inference. Asserted.

### 8. A third party's bulk weight binds no one

III(4) makes the bill conclusive once transferred to a good-faith third party. But
s 5, "despite anything in the Rules", denies even prima facie effect to a bulk weight
"ascertained or accepted by a third party" and stated as such, and relieves the
shipper of guaranteeing it. For a non-negotiable receipt the conclusive rule is
omitted (s 3(5)(b)(i)). Asserted.

### 9. Contracting out is narrow

Clauses relieving negligence liability are "null and void", and "A benefit of
insurance in favour of the carrier" is treated as one (III(8)). Only a special
agreement under Article VI — no bill, a receipt marked non-negotiable, and not an
"ordinary commercial shipment" — may lower the carrier's duties. Terms about the
period before loading and after discharge are free (VII); raising the carrier's
liability is allowed if embodied in the bill (V). Asserted.

## What would need doing before this is worth anything

- The s 3(8) order fixing dollar equivalents for the franc limits must be found and
  deposited; without it the limits cannot be stated in money a user would recognise.
- The list of contracting States (Article X(a), (b)) is not in the deposit.
- No case law was searched, in particular on "package or unit", "reasonable
  deviation", or what counts as a "similar document of title".
- Article IV bis (claims in tort and against servants) and the valuation rule of
  IV(5)(b) are not encoded.
