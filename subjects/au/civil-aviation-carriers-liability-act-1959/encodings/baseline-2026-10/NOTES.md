# Civil Aviation (Carriers' Liability) Act 1959 — passenger baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; a question that reaches a gap answers `not covered`, naming the gap, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0077` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

Every question is a function named as the passenger would ask it, with `@export` and a `@desc` on every input, grouped under `§§` headings.

## Edition

**Compilation No. 30**, compilation date 17 June 2021, includes amendments up to Act No. 148, 2020 (register id C2021C00236), retrieved 22 September 2026, as deposited at `../../registers/source-bundle/C1959A00002.txt`. The Act's body is at lines 1–585; Schedule 1A (the 1999 Montreal Convention) at lines 587–828; Schedule 1 (Warsaw) at 828–; Schedule 2 (Warsaw as amended at The Hague) after it; Schedules 3 and 5 (Guadalajara, Montreal No. 4) after that.

No instrument is brought in: the Civil Aviation (Carriers' Liability) Regulations 1991 are not deposited (see finding 2 and REQ-0089).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cacl-passenger.l4` | `cacl-cases-passenger.l4` | 85 written, 85 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The air passenger** — and, for the questions about a passenger's death, the family member who claims. The questions are the passenger's: "Which law governs my flight?", "Is the airline liable for my injury, my bag, my delay?", "Up to how much?", "By when must I complain, and by when must I sue?", "Is the ticket term that limits the airline's liability valid?", "Is the action for my relative's death for my benefit?".

Provisions addressed to the court (ss 9D(9)–(11), 9H, 12, 16, 35, 39) are encoded as what they mean to the passenger: how damages are reduced and capped. Those addressed to the Minister (ss 9K, 18, 22, 25C, 25N: notices that are evidence of which countries are parties) become a fact the passenger states — whether the countries at each end are parties to each Convention.

The 2026-10-18 defaults:

- **The Act alone**, with the Conventions it scheduled (Schedules 1A, 1, 2). The Regulations that may set higher figures are not deposited; the Act's figures are used, and the substitution is a finding (2).
- **The actors the text names:** the passenger, the carrier (with its servants and agents), the passenger's family members and personal representative, the court.
- **Judgments handed to others are answered conditionally:** whether the carrier proves it was not negligent, took all necessary (or reasonable) measures, or that the damage was solely a third party's; wilful misconduct or recklessness; the damages the court assesses and the passenger's share of responsibility. Each is an input whose `@desc` says "the court decides".
- **The Act's own definitions are worked out from facts:** domestic carrier and the reach of Part IV (ss 26, 27(1), (3)), international carriage (Art 1(2)), family member (s 5(2)–(3)), Australian international carrier (s 11A(2)) is asked as a fact because it turns on a bilateral arrangement. Borrowed terms (a State Party; commercial transport operations under an airline or charter licence) are asked as facts.
- **One case:** one passenger, one journey under one contract of carriage.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** ss 1–8 except definitions, the evidence and jurisdiction sections, Part IVA (carriers' insurance and CASA's functions), s 43.

## Scope

**In:** s 5 (family member, SDR), s 9 (SDR conversion), Part IA ss 9B, 9D(3), (6), 9G, 9H; Part II ss 11, 11A, 12(3), (6), 15, 16; Part III ss 21, 21A, 24; Part IV ss 26, 27(1), (3), 28, 29(1)–(3), 30(2)–(3), 31, 32, 34, 35(3), (6), 38, 39; the 1999 Montreal Convention Arts 1, 17, 19, 20 (as the passenger's own negligence: through the contributory negligence question), 21, 22(1), (2), (5), 25, 26, 31, 35, 52, 55; the Warsaw Convention and the Warsaw Convention as amended at The Hague Arts 1, 17, 18, 19, 20(1), 22, 23, 25, 26, 29.

**Out:** Part IIIA (the Guadalajara Convention: carriage by an "actual carrier" other than the contracting carrier) and Part IIIC (the Montreal No. 4 Convention), whose effect on a passenger's claim is not encoded (a journey covered only by Montreal No. 4 is answered as Warsaw–Hague, the regime it amends; for passengers its Art 22(1) is the same 250 000 francs, finding 9); Part IVA; s 9C and ss 11A(1)(b)–(d), 21A(1)(b)–(d), 31(1)(b), (d) as regulations (not deposited); s 33 and Montreal Art 30 (servants' and agents' own liability); successive and combined carriage (s 27(4), s 29(5); Montreal Arts 36, 38; Warsaw Arts 30, 31); jurisdiction (Montreal Art 33, Warsaw Art 28); advance payments (Montreal Art 28); costs (s 9D(11), s 12(11)); the personal representative's own claim (ss 9D(4), 12(4), 35(4)); cargo throughout (s 41, Montreal Art 18); stowaways (s 42); the Warsaw Conventions' liability for objects the passenger takes charge of (`not covered`); Warsaw Art 20(2) (negligent pilotage, cargo and baggage); Warsaw Art 22(1)'s special contract for a higher limit, for a carrier that is not an Australian international carrier.

## What the Act turns out to say

1. **Which regime governs depends on the countries at the two ends of the ticket, not on the airline's nationality.** Each Convention has the force of law "irrespective of the nationality of the aircraft" (ss 9B, 11(1), 21(1)), and applies to carriage whose places of departure and destination are in two States Parties, or in one with an agreed stopping place abroad (Art 1(2)). Montreal prevails over the Warsaw instruments between parties to it (Art 55). Part IV takes what is left: carriage between States, to or within a Territory, or between Australia and another country, on a commercial flight, "not being carriage to which" any Convention applies (s 27(1)). A return trip from Perth with a stop in Bali is international carriage under Montreal even though both ends are in Australia. Asserted.
2. **The figures in the deposit are the 1999 text's, and the Act points past them.** Schedule 1A gives 100 000 SDRs (Art 21), 4 150 (Art 22(1)) and 1 000 (Art 22(2)). The Act's definition of "the 1999 Montreal Convention" (s 5(1)(a)) takes in "any revision of the limits of liability, in accordance with Article 24 ... that has become effective", and s 9K lets the Minister declare one. No revision is deposited, so this encoding answers on the text's figures; a revision in force raises every Montreal answer. Likewise ss 9C, 11A(1)(b), 21A(1)(b) and 31 let regulations prescribe higher limits or index $925 000, 480 000 SDRs, $3 000 and $300; the Regulations are not deposited. Raised as REQ-0089 (the Civil Aviation (Carriers' Liability) Regulations 1991 and the Article 24 revisions). Asserted on the text's figures.
3. **Under Montreal, there is no limit for death or injury unless the carrier proves it was not at fault.** Art 21(1): up to 100 000 SDRs the carrier cannot exclude or limit its liability at all; Art 21(2): above that it escapes only by proving the damage was not due to its negligence or was solely a third party's. So the "limit" is 100 000 SDRs only on that proof, and otherwise there is none. Asserted.
4. **Under Part IV, wilful misconduct does not lift the limit.** The Warsaw Conventions (Art 25) and Montreal (Art 22(5), for delay and baggage) remove the limits for intentional or reckless conduct; Part IV has no such rule. A domestic passenger's injury claim stops at $925 000 (or the higher contract figure) whatever the airline did. Asserted.
5. **Part IV gives no claim for delay.** Sections 28 and 29 make the carrier liable for death, injury and baggage; nothing in Part IV makes it liable for delay. A late domestic flight is answered `not covered` (any claim lies under the contract or the general law). Asserted.
6. **The time to complain about baggage varies by regime and by what happened, and for a whole lost bag under a Convention there is none.** Montreal Art 31(2) and Warsaw Art 26(2) name damage (from receipt) and delay (from when the baggage was placed at the passenger's disposal), not total loss; s 30(2)(b) does name total loss (21 days from when it should have been placed at the passenger's disposal). Montreal: 7 and 21 days; Warsaw–Hague: 7 and 21; Warsaw unamended: 3 and 14; Part IV: 3 days for damage or partial loss, 21 for total loss, 3 from the end of the journey for cabin baggage, with the court's leave possible (s 30(3)). This encoding reads loss of part of an item as "damage" under the Conventions, and reads Art 31 and Art 26 as not setting a time for baggage the passenger kept (they speak of receipt by "the person entitled to delivery"). Both readings are interpretive choices. Asserted.
7. **Two years to sue, counted differently.** Part IV (s 34): from arrival, or, if the aircraft never arrived, from the day it ought to have arrived or the day the carriage stopped, "whichever is the later". The Conventions (Montreal Art 35, Warsaw Art 29) say "or" and leave the method to the law of the court. This encoding takes the earlier of the two dates under a Convention, the cautious reading; a court might take another. Asserted (20 January 2028 under Part IV, 15 January 2028 under Montreal, on the same facts).
8. **The Act protects the damages from deduction and from contracting out.** Insurance, superannuation, pensions and benefits, and a home inherited by a family member, are not taken into account to reduce the damages (ss 9G, 15, 38). A ticket term relieving the carrier of liability or fixing a lower limit is void, the rest of the contract standing (s 32; Montreal Art 26; Warsaw Art 23). Asserted.
9. **The Montreal No. 4 Convention does not change the passenger limit.** Schedule 5's Art 22(1) keeps 250 000 francs for persons; Montreal No. 4 changed cargo to SDRs. Part IIIC is out of scope; a journey under it is answered here as Warsaw–Hague, which on the passenger limit agrees. Not asserted.
10. **Family members are a long list, and some need dependence.** Spouse or de facto partner; parent, step-parent or grandparent; child, step-child, ward or grandchild; sibling, step- or half-sibling — all without more. A foster-sibling, foster-child or guardian counts only if wholly or partly dependent on the passenger for financial support (s 5(2)(e)). The one action is for those resident in Australia, and others only if they ask (ss 9D(6), 12(6), 35(6)). Asserted.

## What would need doing before this is worth relying on

- **The Regulations and the Article 24 revisions** (finding 2): without them every limit may be understated. REQ-0089.
- **Which countries are parties** to each Convention: the passenger is asked; a register (the Minister's s 9K, 18 and 22 notices, or ICAO's list) would let the encoding answer it.
- **Parts IIIA and IIIC**, s 33, successive and combined carriage, jurisdiction, and the personal representative's claim.
- **Case law.** No decision was read. The meaning of "accident" (Art 17), "embarking or disembarking", and the readings in findings 6 and 7 are settled, if at all, by cases.
- **State law** for flights within one State (for WA, the Civil Aviation (Carriers' Liability) Act 1961 (WA)), which applies Part IV by reference.

## The Regulations brought in (added 2026-10-23, REQ-0089)

**Module:** `cacl-regulations.l4`, beside `cacl-passenger.l4`, which it imports; cases in `cacl-cases-regulations.l4` (20 written, 20 satisfied; `l4 run` 0 errors, 0 warnings on both new files, and `cacl-cases-passenger.l4` still 85 of 85). Same seat (the air passenger), same defaults.

**Instrument:** the Civil Aviation (Carriers' Liability) Regulations 2019 as made (register id F2019L01172, unamended, in force 1 October 2019), deposited as their own subject at `subjects/au/civil-aviation-carriers-liability-regulations-2019/` with `parent_act` this Act. They repealed the 1991 Regulations that REQ-0089 named.

**What the module computes:** the Part IV limits for death or injury (s 31(1), (1A)) and for baggage (s 31(2), (3)) with the prescribed figures read from regs 6 and 7, the Act's figure, and a higher contract figure; and whether the Regulations raise or displace any limit for the passenger's regime.

11. **The Regulations prescribe exactly the Act's figures, so they change nothing.** Regs 6 and 7 prescribe $925,000, 480,000 SDRs, $3,000 and $300, the same as s 31(1AA), (1B), (2A) and (4). Paragraph (b) of each subsection applies only to a prescribed figure "higher than" the Act's, so it never takes over. There is no indexation regulation, no SDR figure for an Australian international carrier (ss 9C, 11A(1)(b), 21A(1)(b)), no ticket or baggage check provision under s 40 that could displace a s 31 limit, and no family member class under s 5(2)(f). The baseline's figures for Part IV are therefore the figures in force. Asserted.
12. **The Article 24 revisions are not deposited, for a licence reason.** The revised Montreal limits are notified by ICAO. ICAO's website terms (read 2026-10-23, https://www.icao.int/terms-and-conditions) grant use "for the User's personal, non-commercial use, without any right to resell or redistribute them or to compile or create derivative works therefrom", which is the kind of term the encoding guide sends to Michael before anything is deposited. The Register holds no s 9K notice of a revision. So the Montreal answers in `cacl-passenger.l4` stay on the Convention text's 100 000, 4 150 and 1 000 SDRs, and may be understated. Raised as REQ-0113. Not asserted beyond the module's answer that the Regulations do not touch the Montreal limits.
13. **Reg 8(2) cites a paragraph the deposited compilation of the Act does not have.** It prescribes 480,000 SDRs "for the purposes of paragraph 41C(3)(aa)"; s 41C(3) in Compilation No. 30 has paragraphs (a), (b) and (c) only. The insurance provisions are out of this seat's scope, so this is recorded, not encoded.
