# Home Building Contracts Act 1991 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc` (29 questions).

Files:

- `hbc-contracts.l4`: which contracts the Act covers, what the contract must contain, the deposit cap and progress payments, termination, variations, the building permit condition, the fixed price and price rises, defects, inspection, contracting out, home indemnity insurance, and the complaint time limits.
- `hbc-cases-contracts.l4`: built by the scratchpad generator `gen_wa_home-building-contracts-act-1991_baseline.py`.

## Edition

- **The Act.** The compilation of the Home Building Contracts Act 1991 (No. 61 of 1991) deposited at `../../registers/source-bundle/mrdoc_45904.txt` (legislation.wa.gov.au mrdoc 45904, retrieved 2026-09-07). The deposit gives no compilation number or date. Its compilation table ends with the Directors' Liability Reform Act 2023 Pt. 3 Div. 34, in operation 5 Apr 2023.
- **The Regulations.** The Home Building Contracts Regulations 1992, version 03-k0-00, currency from 1 Sep 2025, deposited at `../../../home-building-contracts-regulations-1992/registers/source-bundle/mrdoc_48796.txt` (mrdoc 48796, retrieved 2026-10-20). Used:
  - r 2A: the s 3 thresholds become $7,500 and $500,000 (the Act's text says $6,000 and $200,000);
  - r 3 and Schedule 1: the Notice for the Home Owner, which is also the only source used for the complaint time limits;
  - r 3A: a 20% deposit for cabinetry work more than half off-site;
  - r 5: a $500 maximum excess;
  - r 7: the s 25A minimum amount becomes $20,000 (the Act says $10,000);
  - r 7A: deposit cover becomes $40,000 (the Act says $20,000);
  - r 7B: minimum cover becomes $200,000 (the Act says $100,000).

Working days and months are counts the owner states; the encoding does no calendar arithmetic.

## Checks

One case file, **50 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). The module alone also checks with no errors or warnings.

A copy with one expected value altered (the c051 deposit cap, $22,100 to $22,000) was run as a control. The runner reported the failures.

## Seat

**The home owner contracting a builder**: the "owner", "the person for whom ... home building work is to be performed under the contract" (s 3(1)).

The life event asks, in the owner's words, "What must my building contract contain, and must I be insured?" Most of the Act is addressed to the builder: it must ensure the contract is written and signed (s 4(4)), must not take more than the capped deposit (s 10), must not include a rise-and-fall clause (s 13), and must insure the work (s 25C). Each is encoded as what it means for the owner: whether the contract is covered, what may be asked of the owner and when, whether the owner may end the contract, and what the insurance gives the owner.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The Regulations are deposited and override five of the Act's own figures (see Edition).
- **The actors the text names.** Followed: the owner, the builder, the insurer, the Minister (exemption periods, as a fact) and the Building Commissioner (complaints).
- **A judgment handed to someone else is answered conditionally.** Followed. These are facts:
  - whether a stage payment has been shown not to be a genuine progress payment (s 10(3));
  - whose failure meant the building permit was late (s 9(2), Schedule 1);
  - whether a failure is a "defect" (s 11(2));
  - whether a variation was caused by unforeseeable circumstances (s 8(1)(b)).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: home building work contract (s 3 with r 2A); residential building work and cost of the building work (s 25A with r 7); developer (s 25A).
  - Asked as facts: cost plus contract (whether the price is undetermined); whether a building permit is required (Building Act 2011); whether the work is a prescribed building service (Building Services (Registration) Act 2011); whether a Minister's exemption order is running (s 25I).
- **One case is the text's natural unit.** Followed: one contract between the owner and a builder.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Out: approved-fund approval, review, regulations, retrospectivity, prosecutions and infringement notices.

**Departure.** The complaint itself is made under the Building Services (Complaint Resolution and Administration) Act 2011, which is not encoded. Its time limits (3 years for a contract dispute, 6 years for building standards) are read only from the prescribed notice in Schedule 1 to the Regulations. They are what the owner is told, not the operative rule.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c051** (2028-02-20), Byford house-and-land package, $620,000, with Liam | `Is my contract a home building work contract`, `Is my contract made as the Act requires`, `Must I be given the notice before I sign`, `What is the most deposit my builder may take`, `Must my builder insure my work`, `Must I get the insurance certificate before any payment`, `How much must the insurance cover me for`, `How much of my deposit is insured` | Covered by Part 2; notice required before signing; deposit at most **$22,100**; insurance required, certificate before any payment, cover at least **$200,000**, deposit insured in full |

These are **assumed**, and labelled as such in the generator:

- the package split: land $280,000 and building contract $340,000, the same split as the WA First Home Owner Grant baseline uses;
- the builder's deposit at the full 6.5% ($22,100).

The scenario's "five per cent deposit" is the home-loan deposit under the Home Guarantee Scheme. It is not the builder's deposit, and this Act does not touch it.

## Why this scope

The scope is what the event asks, plus what any owner signing a building contract meets:

- whether the contract is covered;
- what it must contain;
- how much may be paid, and when;
- how it may be varied or its price raised;
- the permit condition;
- defects;
- insurance;
- how to end the contract and when to complain.

Unconscionable and misleading conduct (ss 15, 15A) are left out because each is a judgment for the Building Commissioner or the Tribunal on a complaint, and would reduce to a single fact. Prime cost items (s 12) turn on what an item "could reasonably cost", the same kind of judgment. Owner-builders (Part 3A Division 3) are a different seat.

## What the Act turns out to say

1. The Act's own text puts contracts of $200,000 or more outside Part 2, but r 2A raises that to $500,000 and the floor from $6,000 to $7,500. So a contract is covered only if its stated amount is more than $7,500 and less than $500,000. Asserted.
2. Home indemnity insurance has no upper limit. A $550,000 build is outside Part 2 (no deposit cap, no written-contract rule), but it must still be insured. Asserted.
3. The deposit cap is 6.5% of the contract price (s 10(1)(a)). For cabinetry work more than half done off-site, r 3A allows 20%. Asserted.
4. The owner may end the contract if it is not written, dated and signed (s 4(5)), but not because the Notice for the Home Owner was never given. Section 4(5) reaches only s 4(1); the notice is s 4(3). Asserted.
5. A cost plus contract must be headed and acknowledged as one (s 14(1)). Section 14(2) disapplies that for contracts within para (b) of the definition, so a cost plus contract of $500,000 or more needs neither. Asserted.
6. Termination must be by signed written notice before the work is complete (s 19(2)). Asserted.
7. A variation forced by a written direction or by unforeseeable circumstances escapes the writing-and-signature rule only if the builder gives a statement of reason and cost within 10 working days (s 8(2)). A rise in labour or material costs is never "unforeseeable" (s 8(4)). Asserted.
8. If the owner disputes that circumstances were unforeseeable, the complaint must be made within 10 working days of the statement (s 8(3)). Asserted.
9. The price is fixed: a rise-and-fall clause is void (s 13(2)). Rises are allowed for a new law, a tax rise after the contract, or a start delayed over 45 working days by the owner or by no-one (s 13(4)). The owner may end the contract within 10 working days if such a rise exceeds 5% of the price, but must pay the builder's reasonable costs (Schedule 1 cl 4). Asserted.
10. If the building permit is not granted within 45 working days, the contract stays in force either way. If the builder alone is at fault, the price stays put; otherwise the builder may raise it (Schedule 1 cll 1-3). The condition does not apply to associated work alone (s 9(5)(b)). Asserted.
11. Defects must be notified in writing within 4 months of practical completion, or a longer period in the contract (s 11). Asserted.
12. Insurance is needed only above $20,000 (r 7), only where a building permit is needed and the work is a prescribed building service (s 25B(4A)), and not for associated work alone. Asserted, except the associated-work exclusion, which is encoded but not asserted.
13. The certificate must reach the owner before the builder demands any payment, deposit included (s 25C(2)). Asserted.
14. Cover must be at least the lesser of $200,000 and the cost of the work (r 7B). Deposit loss is covered up to $40,000 (r 7A), but not for a developer of 4 or more homes or under a cost plus contract. Claims may be made for 6 years after practical completion (s 25D(1)(d)), and the excess can be at most $500 (r 5). Asserted, except the developer and cost plus exclusions, which are encoded but not asserted.
15. The Act still prints $6,000, $200,000, $10,000, $20,000 and $100,000. All five are displaced by regulation. Anyone reading the Act alone gets every one of them wrong.

## What would need doing before this is worth anything

- A coverage table and an independent test pass.
- The Building Services (Complaint Resolution and Administration) Act 2011, so that complaints and their time limits come from the operative text rather than the notice.
- Sections 15 and 15A as conditional questions, if Legalese Studio's design wants them.
- Transportable dwellings (ss 10(2), 25D(2), (3)) and owner-builders (Part 3A Division 3).
- A calendar for working days (public holidays by area), so that deadlines can be dates rather than counts.
- Confirmation of Chloe's package split and builder's deposit from the scenario owner.
