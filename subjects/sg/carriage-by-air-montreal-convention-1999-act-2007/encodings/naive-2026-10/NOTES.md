# Carriage by Air (Montreal Convention, 1999) Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 28/12/2024, as
deposited at `../../registers/source-bundle/CAMC1999A2007.txt`. The latest amendment
annotated is the Third Addendum to the Schedule, [S 1006/2024 wef 28/12/2024].
Section numbers follow the body; the arrangement of sections at the top of the
deposit is one place out of step.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0101**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The Act itself is 14 short sections. Almost everything a traveller or shipper meets
is in the Montreal Convention, set out in the Schedule and given "the force of law in
Singapore" by s 3(1). This row takes the claims: when the Convention applies (Art 1),
liability and limits for death or injury, delay, baggage and cargo (Arts 17 to 22 and
the three Addenda), when missing baggage or cargo counts as lost (Arts 13(3), 17(3)),
complaint deadlines (Art 31, s 8), the two-year bar and contribution (Art 35, s 9),
costs after a written offer (Art 22(6)), non-compensatory damages (Art 29), clauses
varying the limits (Arts 25, 26, 49) and where to sue (Art 33). Not encoded:
documentation, cargo disposition and delivery, contributory negligence (Art 20),
currency conversion (Art 23), review of limits (Art 24, s 7), advance payments,
servants and agents, successive and actual carriers, arbitration, insurance (s 10),
the Minister's powers (ss 11 to 13) and the final clauses.

## What the Act turns out to say

### 1. No ceiling for death or injury unless the airline proves it was blameless

Art 21(1): up to the threshold the carrier "shall not be able to exclude or limit its
liability". Above it, the carrier escapes the excess only if it proves the damage was
not due to its negligence, or was solely due to a third party (Art 21(2)). Otherwise
there is no upper limit at all. Proven damages of 500,000 SDR are recoverable in full
unless the carrier proves one of those, when they fall to 151,880 SDR. Asserted.

### 2. Recklessness breaks the delay and baggage limits but not the cargo limit

Art 22(5) lifts "paragraphs 1 and 2" (delay of passengers, baggage) where the damage
came from intent or recklessness with knowledge that damage would probably result.
Paragraph 3 (cargo) is not mentioned, so the per-kilogramme cap holds even then.
Asserted (50 kg of cargo stays at 1,300 SDR with or without recklessness).

### 3. The limits have been raised three times, and the Schedule carries all three

The Addenda raise the limits with effect from 30 December 2009, 28 December 2019 and
28 December 2024. The current figures are 151,880 SDR (Art 21 threshold), 6,303
(delay per passenger), 1,519 (baggage per passenger) and 26 per kilogramme (cargo),
against the Convention's original 100,000 / 4,150 / 1,000 / 17. Which date selects the
figure (occurrence, contract or judgment) is not said; the encoding takes a single
"relevant date" and says so as an inference. Asserted, including the day either side
of 28 December 2024.

### 4. Seven days for damaged baggage, in writing, or no action at all

Art 31(2) to (4): a complaint about damage must be made "at the latest" within 7 days
of receipt for checked baggage, 14 for cargo, and 21 days for delay; "Every complaint
must be made in writing"; otherwise "no action shall lie", save fraud by the carrier.
s 8 makes partial loss count as damage, so a bag delivered with items missing is under
the 7-day rule. A bag never delivered is not under Art 31 at all: after 21 days overdue
the passenger may treat it as lost (Art 17(3)), and only the two-year bar applies.
Asserted.

### 5. Contribution claims run from the judgment, not the flight

Art 35 extinguishes the right to damages two years after arrival. s 9(2) says Art 35
does not apply to contribution between persons liable, and s 9(3) gives two years from
the judgment or award against the person seeking contribution. Asserted.

### 6. A good early written offer can cost the claimant their costs

Art 22(6) lets the court add costs and interest on top of the limits, except where the
damages awarded do not exceed a written offer made within six months of the occurrence,
or before the action began if that is later. Asserted.

### 7. The passenger's home can be a forum; nationality cannot

For death or injury Art 33(2) adds the State Party of the passenger's "principal and
permanent residence", if the carrier flies there and does business from premises there.
Art 33(3)(b): nationality "shall not be the determining factor". The place of departure
is not, as such, on the list. Asserted.

### 8. Smaller points

Punitive and exemplary damages are never recoverable (Art 29). A clause raising or
removing the limits is valid (Art 25); one lowering them or choosing another forum is
void (Arts 26, 49). Packing by the shipper and customs seizure are cargo defences;
packing by the carrier is not (Art 18(2)). The Act does not reach occurrences before
16 November 2007 (s 3(2)). Asserted.

## What would need doing before this is worth anything

- Art 20 (contributory negligence) reduces every award and is not modelled.
- The choice of date for the revised limits is an inference; a court decision or the
  Gazette orders would settle it.
- Where the carrier proves a declared value exceeds the actual interest, the encoding
  caps at the actual interest; the text says only that the declared-sum cap then fails.
- "At the expiration of" 21 or 7 days is read as at least that many whole days; the
  boundary day is not asserted. Months are used for the two-year periods, though Art
  35(2) leaves the counting method to the court.
- Successive and actual carriers (codeshares) and servants and agents are not encoded.
- No case law, no regulations under ss 10 and 12, and no list of States Parties were
  retrieved.
