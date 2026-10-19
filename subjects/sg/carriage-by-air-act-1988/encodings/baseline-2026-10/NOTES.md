# Carriage by Air Act 1988 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. No pipeline,
no coverage table, no independent test pass, no human gate. Not for public use as
advice.

It replaces the encoding moved to `solutions/Litigate.4` on 2026-10-19. That
encoding's notes were read for scope and pitfalls; none of its L4 was copied.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1/4/2022, as deposited at `../../registers/source-bundle/CAA1988.txt` (SSO, in
force as at 2026-09-30).

**Checks:** one module (`caa-passenger.l4`) and one case file
(`caa-cases-passenger.l4`), 60 assertions satisfied, 0 errors, 0 warnings, on the
stable `l4` of VS Code extension 1.6.98. The case file is built by a generator
script with expected values written by hand from the text.

## Seat

**The passenger** — and, where the passenger has died, those who claim for the
death (s 5). The Act gives the Warsaw Convention in three texts the force of law
"so far as they relate to the rights and liabilities of carriers, carriers'
employees and agents, passengers, consignors, consignees and other persons"
(s 3(1)). Of these the passenger is the individual: carriers are undertakings,
and consignors and consignees of cargo are usually businesses. Every decision is
phrased as the passenger would ask it (`Is the carrier liable to me`, `What is the
most I can recover`, `Is my action out of time`), on facts the passenger could
state or a finding the passenger could be told of.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The
  limits are in the Schedules themselves, in francs. The Minister's order under
  s 6(4) that would set Singapore-dollar equivalents is not deposited, so no
  dollar figure is given and the answer is in francs, as the Schedules state it.
- **The actors the text names.** Followed: the carrier, its servants and agents,
  the first and last carriers, the court seised.
- **A judgment handed to someone else answered conditionally.** Followed. Wilful
  misconduct (Second Schedule, Art 25) is "the court finds ..."; whether a
  complaint was made "forthwith" is "the court finds I complained forthwith"; Art
  21 answers that the court *may* relieve the carrier, never by how much.
- **The Act's own definitions worked out, borrowed terms asked as facts.**
  "International carriage" (Art 1(2)) is worked out from where the journey starts,
  ends and stops. "High Contracting Party" (s 4(1): a country that has ratified or
  acceded) is asked as a fact. **Which of the three texts governs the journey is
  asked as a fact**: the Act says only that each applies to the carriage to which
  it applies "(as the case may require)" (s 3(1)), and does not say how to choose.
- **One case is the text's natural unit.** One journey, one passenger, one claim.
- **The Act's own terms, each with a plain gloss.** Followed: the three texts are
  named as s 2 names them, glossed with their Schedule.
- **Operative sections in; machinery out.** Followed. Out: s 12 regulations, s 13,
  the treaty machinery in Arts 36 to 41.

## Why this scope

The passenger meets Chapter I (does the Convention apply), Chapter II's ticket and
baggage-check provisions (because a defective document costs the carrier its
limits), and nearly all of Chapter III. Cargo (Arts 5 to 16 and the cargo limbs of
Arts 18 to 24), postal and State carriage (Art 2, s 4(1)(e), s 11), combined
carriage (Art 31), contribution (s 8(2), (3)) and the court's powers over parallel
proceedings beyond the aggregate (s 6(2), (3)) are not encoded.

## What the Act turns out to say

1. **Three texts, three answers.** The passenger limit is 125,000 francs under
   the Warsaw Convention (Second Schedule) and 250,000 under the Hague and Montreal
   texts (First and Third); a special contract can raise it in all three. Asserted.

2. **A ticket without the notice costs the carrier every Article 22 limit under the
   amended texts, but nothing under the 1929 text.** First and Third Art 3(2): if the
   passenger embarks with the carrier's consent without a ticket, "or if the ticket
   does not include the notice", the carrier loses "the provisions of Article 22" —
   the whole Article, so the baggage limits go too. Second Art 3(2) forfeits only
   where the carrier "accepts a passenger without a passenger ticket having been
   delivered". Asserted.

3. **The baggage check matters differently.** Under the 1929 text a check missing
   the ticket number, the number and weight of the packages, or the liability
   statement costs the carrier all its limits (Art 4(4)); under the amended texts
   only a missing check, or a missing notice (unless the check is part of a ticket
   that carries it), and only the Art 22(2) limit (Art 4(2)). Asserted.

4. **Each text loses its limits on its own test.** The 1929 text: "wilful
   misconduct" or its equivalent under the law of the court (Art 25). The amended
   texts: intent to cause damage, or recklessness with knowledge that damage would
   probably result (Art 25). A finding of wilful misconduct does nothing under the
   Hague text unless intent or recklessness is also proved. Asserted.

5. **Partial loss.** The amended texts count the packages concerned and also other
   packages on the same check whose value is affected (Art 22(2)(b) First, (c)
   Third): 20 kg plus 10 kg is 7,500 francs. The 1929 text has no such rule, and the
   encoding says so rather than guessing. Asserted.

6. **The negligent-pilotage defence exists only in the 1929 text, and only for
   baggage and cargo** (Second Art 20(2)). It defeats a baggage claim under the
   1929 text, not under the Hague text (asserted); it does not reach an injury
   claim under either (encoded, not asserted).

7. **Complaint periods shorten under the 1929 text.** Damaged baggage: 3 days from
   receipt (Second), 7 (First, Third). Delay: 14 days from being placed at the
   passenger's disposal (Second), 21 (First, Third). A partial loss counts as damage
   and runs from receipt of the remainder (s 7; encoded, not asserted). Fraud by the
   carrier saves a late complaint (Art 26(4)). Asserted.

8. **Costs on top of the limit exist only in the amended texts**, and are lost if
   the damages do not exceed a written offer made within 6 months of the
   occurrence or before the action, if later (Art 22(4) First and Third). The 1929
   text's Art 22(4) is about the franc. Asserted.

9. **The carrier's employee shares the carrier's limits only under the amended
   texts** (Art 25A, First and Third); the 1929 text has no Article 25A. Asserted.

10. **One limit across all proceedings.** s 6(1): the passenger limit "applies to
    the aggregate liability of the carrier in all proceedings", in Singapore or
    elsewhere. 250,000 less 100,000 recovered abroad leaves 150,000. Asserted.

11. **Two years, whoever is sued.** Art 29 bars the action against the carrier; s
    8(1) applies the same two years to its employee or agent acting in the scope of
    employment; s 8(4) makes an arbitration an action. Asserted.

12. **On a journey with successive carriers, the passenger may sue only the carrier
    on whose leg the accident or delay happened**, unless the first carrier expressly
    assumed the whole journey; for baggage, the first, the last and the performing
    carrier are all open (Art 30(2), (3)). Asserted.

13. **s 10 does not name the Warsaw Convention.** The military-charter exclusion
    applies to the Hague and Montreal texts only, so read literally the 1929 text
    still governs such a charter. Asserted.

## Readings and inferences

- **The 1929 text and the passenger's declared value.** Second Schedule Art 22(2)
  speaks of a declaration by "the consignor". Art 4(3)(g) of the same text puts "the
  amount of the value declared in accordance with Article 22(2)" on the passenger's
  baggage check, so the passenger's declaration is taken to count.
- **"Forthwith" is part of the time.** Art 26(4) bars an action "failing complaint
  within the times aforesaid"; the encoding reads "forthwith after the discovery"
  as part of those times, and asks the court's finding on it. Delay has no
  "forthwith" limb.
- **Baggage never delivered.** Art 26 runs from receipt; with no receipt the encoding
  returns `Article 26 sets no complaint period` (inference).
- **Delay to the passenger** is taken to fall under the Art 22(1) limit "for each
  passenger" (inference; Art 22 names no other limit for it).
- **Declared value exceeded.** Where the carrier proves the declared sum exceeds the
  actual interest or value, the limit is taken to be that actual figure (inference).
- **The two years** end on the anniversary of the reckoning date, and an action on
  that day is in time; Art 29(2) leaves the method to the law of the court
  (inference).

## What would need doing before this is worth anything

- The Minister's order under s 6(4), if there is one, should be deposited so the
  limits can be given in Singapore dollars.
- A rule for which of the three texts governs a journey (by the States' treaty
  status) is not in the Act; it is a fact here and would need a source.
- The printed Schedules were not compared with the authentic French texts that
  s 3(2) makes prevail.
- No case law was read, in particular on "accident" (Art 17), "wilful misconduct",
  and how the two years are counted.
- An aviation-law reader should check the readings above, and an independent test
  pass should be run.
