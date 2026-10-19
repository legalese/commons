# Electricity Act 2001 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`: where the
encoding cannot answer it says so with an explicit value (a constructor named
`not covered by this encoding: ...`, an answer phrased `only if the Authority
authorises ...`, or a fact the caller states, such as whether an exemption order
covers them). No pipeline, no coverage table, no independent test pass, no human
gate. It is not for public use as advice.

This encoding replaces the encoding moved to solutions on 19 October 2026 and the
first-pass encoding `naive-2026-10`. It covers everything the first pass covered
(the s 2 voltages, s 6, ss 79 and 80 with the s 80(9) and (10) defence, s 82, the
Part 10 maxima with s 92, the s 87 fine and presumption, ss 91, 93 and 94) and adds
the consumer's side of the Act: the installation licence (ss 67, 71, 83(4)),
security, disconnection and reconnection (ss 23, 24), supply during a dispute
(ss 21(3), 26), the licensee's works on my land and my trees (ss 31, 32), entry to
my premises (ss 33 to 36, 77), the licensee's equipment (s 38), emergency cut-off
(s 39), buying as a contestable consumer (s 41), what follows an accident report
(s 94(2), (5), (6)) and arrest (s 96). The first pass's hand-checked figures
($625,000 for ten days of an unlicensed activity, $110,000 for stealing $20,000 of
electricity, the per-offence maxima) were re-derived from the text and reused.
Two of its inputs are dropped because they belong to no individual: "is the
Authority" (s 6(1A)) and "is the licensee owning the cable" (ss 79(3), 80(6A)).

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1/9/2025, as deposited at `../../registers/source-bundle/EA2001.txt`, with the
amendments of Act 27 of 2024 (in force 1 July 2025) shown.

**Checks:** with the stable `l4` of VS Code extension 1.6.98,
`l4 run ea-cases-supply.l4` (29 assertions) and `l4 run ea-cases-offences.l4`
(31 assertions): 60 assertions satisfied, 0 errors, 0 warnings. Both modules also
run clean on their own. Each case file also traces one duty with a deadline
(the s 23(3) security and the s 79(2)/80(6) safety notice); both trace to
`FULFILLED`.

| file | what it holds |
|---|---|
| `ea-supply.l4` | ss 6 and 8, 67, 71 and 83(4), 21(3), 23, 24, 26, 31, 32, 33 to 36, 77, 38, 39, 41 |
| `ea-offences.l4` | s 2 voltages and electrical work, s 82, ss 79 and 80, the maxima table (ss 6(2), 72, 79 to 89, 92), s 87, ss 91, 93, 94, 96 |
| `ea-cases-supply.l4`, `ea-cases-offences.l4` | generated fixtures, hand-written expected values |

## Seat

**The individual occupier of premises supplied with electricity** — the
householder or other consumer, who may also own the premises, put solar panels on
the roof, change a fuse, hire an electrician, dig in the garden, or find a
licensee's crew at the door. The Act is written to licensees and the Energy
Market Authority, but the individual meets it as a consumer whose supply can be
cut, as an occupier whose land and door the licensees can enter, and as a person
who can be charged. Every decision is named as that person would ask it
(`May my supply be cut off for my unpaid account`, `Can this person insist on
entering my premises`, `May I do this electrical work myself`,
`What is the most I can get for`) and every input is a fact that person could
state. Where a provision speaks only to an official (s 39, s 94(2) and (5)), the
encoding says what it means for the occupier: whether a claim is barred, what will
follow a report.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed. The Act's own figures are in the text. The instruments that would
  answer questions and are *not* deposited are inputs, said so where used: an
  exemption order under s 8, a notification under s 71, the regulations under
  s 41(1) that make a consumer contestable, the regulations prescribing
  compoundable offences (s 93(2)), and the market rules (s 24(5)).
- **The actors the text names.** Followed: the Authority and its authorised
  officers, the market support services licensee, the transmission licensee, the
  retail electricity licensee, the licensed electrical worker, the licensed cable
  detection worker, the court, the Public Prosecutor. No licensee is named by
  brand.
- **A judgment handed to someone else, answered conditionally.** Followed. The
  Authority's authorisation after an inquiry into my objection (s 31(12)) is an
  input and the answer otherwise reads
  `only if the Authority authorises the works after an inquiry into my objection`;
  the court's permission under s 80(10), the licensee's opinion under s 39, the
  officer's reason to believe under s 96 and s 94(5), and the Authority's
  discretion to compound (`..., if the Authority so chooses`) are each inputs.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed for "high voltage", "electrical installation" (what is beyond
  the outlet, and EV chargers), "electrical work" (cleaning and painting out),
  "earthworks" and "trained person". "Grievous hurt" (Penal Code) is asked as a
  fact. **Departed from** for "contestable consumer": the Act defines it by how the
  consumer buys, but which consumers may become contestable is set by regulations
  under s 41(1), not deposited, so it is a fact the caller states.
- **One case is the text's natural unit.** One unpaid account, one visit to my
  premises, one electrical job, one set of earthworks, one meter, one offence.
- **The Act's own terms, each with a plain gloss.** Followed: "consumer",
  "contestable consumer", "earthworks", "electrical installation", "supply
  installation", "trained person" are used as the Act uses them and glossed in
  comments.
- **The operative sections in scope; the machinery out.** Followed in kind but
  not in full: the Act is about 320,000 characters, so the scope is what an
  occupier meets (below). Administration, licensing procedure, regulation-making,
  the Appeal Panel and commencement are out.

## Why this scope

An occupier asks: do I need a licence for my panels or my wiring; can they cut me
off, and must they put me back; can they come onto my land or into my flat; what
may I do with my own wiring; may I dig; and what could I be charged with, and how
badly. Those are ss 6, 8, 21(3), 23, 24, 26, 31 to 36, 38, 39, 41, 67, 71, 77,
79, 80, 82 to 89, 91 to 94 and 96. Left out: licensing procedure and licence
conditions (ss 7, 9 to 20B), tariffs (s 22; the figures are set by the licensee,
not the Act), s 25, s 27, Parts 4, 4A, 5A, 5B, 6, 7 and 8, s 37 (relocation at
the licensee's discretion), s 38A, cable detection licensing (s 81), the duties of
installation licensees beyond their offences (ss 72 to 76), s 85's defence (shaped
like s 80(9) and (10)), s 98 (appeal to the Minister) and the machinery.

## What the Act turns out to say

1. **A household short of income cannot be cut off for an unpaid bill until it
   has been offered advice and given at least 7 days.** s 24(2) bars a direction
   to disconnect residential premises where the failure "occurs through lack of
   sufficient income" until the licensee has offered advice on payment methods and
   the consumer has refused it, or failed to act on it, within a period "being not
   less than 7 days". A period of 5 days does not lift the protection. A household
   that could pay has no such protection, and a contestable consumer owing a
   transmission licensee is under s 24(4), with none either. Asserted.

2. **Section 24 says nothing about what a contestable consumer owes a retailer.**
   s 24(4) deals only with charges due "to a transmission licensee". The encoding
   returns `not covered by this encoding: ...` rather than guess. Encoded, not
   asserted.

3. **On its words, using your own home wiring needs an installation licence,
   unless the Authority has exempted it.** s 67(1) forbids anyone to "use ... any
   electrical or supply installation" without a licence; s 71(b) lets the
   Authority exempt installations "used exclusively for domestic purposes" by
   Gazette notification. No notification is deposited, so the exemption is an
   input; without it, using fixed wiring is an offence under s 83(4). A plugged-in
   appliance and an EV charger are not "electrical installations" at all (s 2,
   exclusions (b) and (d)). Asserted.

4. **Rooftop solar is "generation" on the words.** s 2 defines "generate" as
   producing electricity "for the purpose of giving a supply to any premises", and
   s 6(1)(a) requires a licence or a s 8 exemption. That this catches panels
   supplying one's own home is an inference from "any premises". Asserted on that
   reading, with and without an exemption order.

5. **A householder may change a lamp or a household fuse in their own
   installation, and nothing else; but rewiring a kettle's plug is not "electrical
   work" at all.** s 82(8)(a) and (b) save the lamp and the fuse only in "the
   person's own electrical installation", so a lamp at a neighbour's is not saved.
   Adding a socket is an offence unless supervised by a licensed electrical worker.
   Work on an appliance beyond the outlet falls outside "electrical installation"
   and so outside "electrical work", which also excludes cleaning and painting.
   A tradesperson who is not an electrician is saved only while off any circuit
   that "is, or may be, connected" to supply. Asserted.

6. **Who can insist on coming in depends on why.** A meter reader needs only a
   reasonable time and a "duly authenticated document" (s 34); a crew disconnecting
   an occupied dwelling also needs 6 hours' notice or my consent (s 35(2)); a survey
   needs 7 days' notice (s 33(2)); a repair crew needs 7 days' notice except in an
   emergency from a fault (s 36); and nobody "purporting to be an authorised
   officer" need be admitted without the official card (s 77(3)). Asserted for
   five visits. *Inference, not asserted:* that refusing a lawful entry is
   "hindering or obstructing" under s 88.

7. **The licensee's works on my land wait 14 days, and my objection stops them
   until the Authority authorises them.** s 31(7) requires 14 days' written notice
   (none in an emergency from a fault), s 31(9) lets the owner or occupier object
   within 14 days, and an objection not withdrawn goes to an inquiry after which
   the Authority "may authorise" the works; its decision is final (s 31(13)) and
   s 98 excludes an appeal from it. Asserted.

8. **A felled tree is compensated only if it was there first, and not near a
   public road.** s 32(3) pays for trees that predate the installation; s 32(5)
   excludes trees within 20 metres of the centre line of a public road unless they
   predate the road. Asserted. If I fell a tree near the lines myself without
   14 days' notice I pay for any damage (s 32(6), (7)), and felling on my land is
   presumed to be mine (s 32(8)). Encoded, not asserted.

9. **Stealing electricity has no ceiling on the fine.** s 87(2): "the total of"
   up to $50,000 and "an amount equal to 3 times the value of electricity", plus
   $250 a day. On $20,000 of electricity the maximum is $110,000. Asserted.

10. **Meter tampering is presumed from a physical sign only if I had custody or
    control of the meter.** s 87(4) lists five signs; a sign without custody, or
    custody with no sign (a low bill alone), does not raise the presumption.
    Asserted.

11. **Digging near a high-voltage cable risks 5 years; near a low-voltage one,
    12 months.** s 80(1) requires 7 days' written notice (modifiable by the
    Authority, so an input), location information and consultation, and licensed
    cable detection, with the s 80(4) duties; breach is $100,000 or 5 years
    (s 80(7)). Near a low-voltage cable, s 79 requires only licensed cable
    detection, at $10,000 or 12 months. Both yield to genuine safety needs, with
    written notice to the licensee within 7 days of starting, encoded as a duty
    with its deadline. Whether a late notice is itself an offence is not said.
    Asserted for six sets of earthworks.

12. **The s 80(9) defence can be lost on paper.** Relying on information from the
    licensee, the infrastructure owner or a cable detection worker needs written
    notice to the prosecutor "within 14 clear days before the hearing", or the
    court's permission (s 80(10), Act 27 of 2024). Read here as at least 14 clear
    days before; that is an inference, and the words could be read the other way.
    Asserted on that reading.

13. **Two penalty shapes are lopsided.** s 6(2) (unlicensed activity) carries
    $500,000 and $12,500 a day and **no imprisonment**; s 83(2) (wilfully tampering
    with an installation so as to endanger life or property) carries 5 years and
    **no fine**. The table shows these as `NOTHING`, not 0. Offences with no stated
    penalty (ss 82(7), 86, 88, 89, 94(7)) take s 92: $10,000 or 12 months, $250 a
    day. Asserted for four offences.

14. **"High voltage" and "low voltage" overlap.** Both definitions join their
    limits with "or", so 900V a.c. between conductors and 601V to Earth meets both.
    Treated as high voltage (an inference). Asserted on that reading.

15. **A new contestable consumer who does nothing is deemed to buy at wholesale
    prices after 30 days.** s 41(7): failing to choose within 30 days (or any
    further period the Authority allows) deems purchase "indirectly from any
    wholesale electricity market through a market support services licensee at
    prevailing market prices". Asserted.

16. **The licensee's meter is not mine and cannot be taken for my debts.** s 38.
    Asserted. **And the licensee is not liable for an emergency cut-off** made in
    its opinion that immediate action was necessary (s 39(2)). Encoded, not
    asserted.

17. **An accident with a death goes to the Public Prosecutor twice.** The
    officer's preliminary findings go there on loss of life or reason to believe of
    serious injury (s 94(2)(e)), and if an inquiry is required under s 94(5) its
    findings go there too (s 94(6)). Asserted for one case.

## What would need doing before this is worth anything

- The s 8 exemption orders and the s 71 notifications, to settle whether rooftop
  solar and domestic wiring need licences in practice (findings 3 and 4).
- The regulations under s 41(1) (who is contestable), s 93(2) (what is
  compoundable) and s 24(6) (apportioning payments), and the market rules.
- s 85's defence, s 38A, and the duties of installation licensees (ss 72 to 76)
  for an occupier who holds an installation licence.
- The reading of "within 14 clear days before the hearing" (finding 12) and of the
  overlapping voltage definitions (finding 14).
- No regulations, Authority directions, codes of practice or case law were read,
  and no human gate has been sought.
