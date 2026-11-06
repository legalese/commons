# Water Services Act 2012 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc`.

Files:

- `wsa-charges.l4`: the module. It covers Part 5's water service charges as a property owner meets them: who may charge, the owner's entitlement to the service, owner or tenant liability, unpaid charges following the land, the memorial on the title, late payment, cutting off or reducing the supply, interruptions, the meter, hardship and concessions (as pointers), and the ombudsman.
- `wsa-cases-charges.l4`: the worked cases, built by the scratchpad generator `gen_wa_water-services-act-2012_baseline.py`.

Conventions: money is in dollars; periods are whole days.

## Edition

- **The Act.** The Water Services Act 2012 (No. 24 of 2012) deposited at `../../registers/source-bundle/mrdoc_48881.txt` (legislation.wa.gov.au mrdoc 48881, retrieved 2026-09-07). The compilation table runs to the Statutes (Repeals and Minor Amendments) Act 2025 s 8, in operation 26 Sep 2025. Two amendments are listed as uncommenced (Public Health (Consequential Provisions) Act 2016 Pt 5 Div 27; Evidence Act 2025 s 492(1)); they are not applied.
- **Not deposited.** No regulations, code of practice (s 26) or code of conduct (s 27) under the Act is deposited. So:
  - the tariffs (statutory water service charges, s 71(1), s 124) are not encoded; where an amount is needed it is an input;
  - interest and late-payment penalties (s 124(2)(n)) are inputs, as amounts;
  - the prescribed fees for cutting off and restoring (s 95(7)) are inputs;
  - whether the regulations apply a charge to unconnected land (s 124(2)(c)), make a measured user liable (s 124(2)(d)), or give an exemption or concession (ss 124(2)(o), 222(2)(c)) is asked as a fact;
  - the hardship rules of the code of conduct (s 27(3)(e)) are a pointer.

## Checks

One case file: **39 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). `l4 run wsa-charges.l4` reports "Checking succeeded" with no diagnostics.

As a control, a copy with one expected value altered (456 to 457) was run; the runner reported the failure.

## Seat

**The property owner: the owner of land to which a licensee provides a water supply, sewerage or drainage service.** The life event asks from this seat: "Who levies what on a new house?" The Act gives the entitlement to the service to the owner (s 73), and keeps statutory charges recoverable from the owner for the time being (s 126(1)). So the owner is the individual Part 5's charges are applied to.

Most of the Part tells the licensee, the Authority or the Registrar what to do. Those provisions appear only as what they mean for the owner: what may be charged, what may be done to the supply or the title, and what the owner must be given.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows. No regulations or codes are deposited, so the numbers they set are inputs (see Edition).
- **The actors the text names.** Followed: the owner, a later owner, the occupier, the customer, the licensee, the Registrar, the water services ombudsman, a court or tribunal.
- **A judgment handed to someone else is answered conditionally.** Followed. The licensee's satisfaction that a reduction prevents waste (s 95(2)) gives a conditional answer: "its flow may be reduced, if the licensee is satisfied that is necessary to prevent waste". Whether a payment arrangement is satisfactory to the licensee (s 95(7)(b)) is asked as a fact.
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: customer (s 3(1)), the s 95(1) grounds, prior notice under s 76(6)-(7), which charges s 126(1) reaches.
  - Asked as facts: "owner" and "occupier" (borrowed from the Local Government Act 1995 s 1.4 by s 3(1)), negligence and bad faith (s 77(2)), and everything the regulations decide.
- **One case is the text's natural unit.** Followed: one parcel of land and one water service.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Licensing, the Authority's powers, the ombudsman scheme's approval, and administration are out.

**Departures:** none of substance. "Remain unpaid for 30 days after they become due" (s 95(1)(b)) is read as at least 30 days elapsed since the due date; that reading is stated in the module.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c055** (2029-07-15), handover of the new Byford house: "Who levies what on a new house?" (the water part) | `Who may charge me for this`, `Am I entitled to the water service`, `Can I be charged for a service I am not connected to`, `Who is liable for the water charges on my home`, `Can the unpaid charges on my land be recovered from me as owner`, `Can my water be cut off or reduced`, `Can I take my dispute to the water ombudsman` | The licensee providing the service charges, on prudent commercial principles, within any limits in its licence, codes or regulations (s 123). As owners, Chloe and Liam are entitled to the service while the charges due are paid (s 73). If the regulations so provide, the lot can be charged before connection because the main runs at the boundary (s 124(2)(c)). On a detached house with its own connection the Act makes the owner liable. Charges left unpaid by the developer would follow the land to them (s 126(1)). Even 45 days overdue, their supply could be reduced but not cut off while they live there without their agreement (s 95(3)). As customers they may go to the ombudsman. |

## Why this scope

The Act is large: licensing, last resort supply, the ombudsman scheme, development control, infrastructure contributions, connections, enforcement, works and land powers. The life event asks only what water charges apply to a home. The scope is that question, plus what any owner meets around a water bill: liability, late payment, the supply being cut off, the title, disputes.

Left out:

- Part 2 except ss 21 and 27 (licensing);
- Part 3 (last resort supply);
- Part 5 Divisions 3, 4, 6, 7 and 8 (development control, infrastructure contributions, protection of works, sewer and drainage connections, enforcement);
- s 127 (people who take water unlawfully);
- Parts 6-11 (works, interests in land, entry generally, proceedings, administration);
- council rates, the emergency services levy and land tax, which the same event cites but which come under other Acts.

## What the Act turns out to say

1. **The Act sets no tariff.** It lets the licensee charge for the service on "prudent commercial principles", which "may allow for the making of a profit" (s 123(2)). It lets the regulations set "statutory water service charges" on almost any basis: quantity, quality, gross rental value, unimproved value, area, type of land or service (s 124(2)(a)). What a home pays is wholly in instruments not deposited. Not asserted (string answer).
2. **The owner, not the tenant, is the person the Act makes liable.** Statutory charges and alternative charges "remain payable and are recoverable from the owner of the land for the time being while the charges remain unpaid" (s 126(1)). A tenant becomes liable only if the regulations make a measured user liable (s 124(2)(d)), or if the licensee apportions charges among the occupiers of dwellings on one connection (s 125). Asserted.
3. **Unpaid charges follow the land, but only some of them.** s 126(1) covers statutory charges and the alternative charges of s 75(2)(c). It does not cover charges agreed where no statutory charge applies (s 75(2)(b)), nor incidental charges. Asserted.
4. **The Act never says "a charge on the land".** The work is done by s 126(1) and by a memorial. Once charges are in arrears the licensee may lodge a memorial (s 128(2)). After that, no later instrument can be registered without the licensee's written consent (s 128(3)). The licensee must withdraw the memorial once paid (s 128(4)). Asserted.
5. **Charges can apply before the house is connected, but only if the regulations say so.** The regulations may apply a charge to unconnected land where connection is practicable (the main at or near the boundary), the land benefits, or the land contributes to the need (s 124(2)(c)). Asserted.
6. **A later owner can be bound by the previous owner's agreement on charges without knowing of it.** Terms about water service charges, unusual aspects of the service, quantity or quality, or indemnity bind "whether or not the owner has prior notice" (s 76(4)). Other terms bind only with prior notice. Notice is deemed if the notification was registered at least 21 days before the buyer took possession (s 76(6), (7)). Asserted.
7. **An occupied home cannot be cut off without the occupier's agreement.** This applies "Despite any other provision of this Act" (s 95(3)). Unpaid charges 30 days after falling due allow the licensee to cut off or reduce (s 95(1)(b)). For an occupied dwelling that means reduce only. The licence may restrict even that (s 95(4)). Asserted.
8. **Being cut off does not end the debt (s 95(6)).** Before restoring, the licensee may require the arrears, interest and prescribed fees, or a payment arrangement it accepts (s 95(7)). Asserted.
9. **The Act has no hardship rule of its own.** It lets the Authority's code of conduct deal with "customers in financial hardship" and with suspension, and makes compliance a licence condition (s 27(3)(e), (f), (4)). The code is not deposited. Not asserted (string answer).
10. **The Act grants no concession itself.** Exemptions, discounts, rebates and concessions are for the regulations (ss 124(2)(o), 222(2)(c)). Concessions under other Acts were not read. Not asserted (string answer).
11. **Interruptions are mostly at the owner's risk.** The licensee is not liable for loss from an interruption for an emergency or maintenance, except for negligence, bad faith or agreement (s 77(2)). Asserted.
12. **The meter is presumed right, and can be read without notice.** A meter is presumed within tolerance, and a certificate of readings correct, unless there is evidence to the contrary (s 79). The meter may be read without consent, notice or warrant, but not inside the dwelling (s 129(2), (4)). Disruptive routine work needs 48 hours' notice unless the occupier agrees otherwise (s 129(5)). Asserted.
13. **The ombudsman is open to customers and to anyone affected, free.** It must decline a matter already before a court or tribunal (ss 66(2)(g), 68(1), 69(2)). Asserted.

## What would need doing before this is worth anything

- Deposit the regulations under the Act. Bring in the statutory water service charges for a residential property, the interest and late-payment rules, the disconnection and restoration fees, the rules on unconnected land and on user liability, and the exemptions and concessions.
- Deposit the Authority's code of conduct (s 27) and any Minister's code of practice (s 26), and encode the hardship and suspension rules.
- Check whether pensioner and seniors concessions on water charges come from another Act, and link it if so.
- Run the Legalese Studio stages this baseline skipped: Resolve, Refine and Test, an independent test pass, and the human gates.

## Q&A layer (seat and situations as parameters)

Added on 6 November 2026, following the graffiti encoding's design (D2, D4, D8).

- **Files.** The layer is `wsa-qa.l4`. Its cases are in `wsa-qa-cases.l4`.
- **Imports.** It imports `prelude` and `wsa-charges`. It changes none of the baseline's rules or exports.
- **The role comes first.** Every exported question takes `my role` first ("Which of these describes you"). For the role a question is not about, it answers `does not arise for you` without reading any other input.

**Roles.**

- `I own land with a water, sewerage or drainage service, or a main near it`. This is the baseline's seat (Chloe and Liam).
- `I live in or occupy a home with a water service but do not own it, such as a tenant`. The Act gives the occupier these protections and duties:
  - s 95(3) protects the occupier of a dwelling from being cut off without their agreement;
  - the regulations may make a tenant liable as a measured user (s 124(2)(d));
  - a tenant may be liable for a share the licensee apportions (s 125);
  - s 129(5) gives the occupier the say on how much notice is given before routine entry.

The licensee, the Economic Regulation Authority, the Registrar and the ombudsman are never seats.

**Situation inputs.** All six are BOOLEANs and all are the owner's. FALSE gives `does not arise for you`. Each comes straight after `my role`.

| Name | Questions (owner) |
| --- | --- |
| `my land is not yet connected to the service` | "Can I be charged for a water service my land is not yet connected to" (s 124(2)(c)) |
| `my home is let to a tenant` | "If my tenant ... does not pay, can the statutory charges still be recovered from me" (s 126(1)) |
| `a previous owner made a written agreement with the licensee about the service` | "Am I ... bound by a term of an agreement the previous owner made" (s 76) |
| `water service charges on my land are overdue` | "How much do I owe on an overdue water bill" (s 124(2)(n)) |
| `a water memorial has been lodged on my title and not withdrawn` | s 128(3) dealings; s 128(4) withdrawal |
| `my water supply has been cut off or reduced` | s 95(6) the debt remains; s 95(7) what is paid before restoring |

Every question of the occupier arises for every occupier, so none takes a situation input.

**Decisions.**

- **D-QA1. Inputs fixed by the role or the situation.**
  - The baseline's `I am the owner of the land` (s 73) and `I am the owner for the time being` (s 126(1)) are TRUE by the owner's role.
  - s 128(3)'s `a memorial has been lodged and not withdrawn` is TRUE by its situation.
  - The tenant question's `I am the owner for the time being` is TRUE by the role.
- **D-QA2. Some questions settle on their own input and take no situation.**
  - s 128(2)'s memorial question settles on `what is unpaid`: `nothing, or something else` gives no, so it takes no situation.
  - The cut-off question (s 95(1)-(4)) arises for every owner and every occupier. Its grounds are its inputs.
- **D-QA3. s 128(3) with no memorial gives does not arise.** Before the layer, the baseline answered yes when no memorial stands. The question presupposes a memorial ("while a water memorial stands"), so its situation decides.
- **D-QA4. The occupier's s 126(1) question.** "Can water charges left unpaid on the land be recovered from me under s 126(1), though I am not the owner" is the baseline's function with `I am the owner for the time being` FALSE. The answer is no for every kind of charge. A tenant's own liability is the separate "Am I liable" question (ss 124(2)(d), 125).
- **D-QA5. String answers are wrapped.** The baseline's string answers (s 123, hardship, concessions) are wrapped in `Text answer`, so that they can also say `does not arise for you`.

**Not covered for the occupier.**

- Any liability the regulations or the licensee's terms put on a measured user beyond who is liable (not deposited).
- What a tenancy agreement says about water charges (Residential Tenancies Act 1987, not this Act).
- Restoration and its fees when the occupier is not liable.
- The hardship code itself (not deposited).

**Counts.** 29 questions: 20 for the owner (every baseline export) and 9 for the occupier. `wsa-qa-cases.l4` has 119 cases:

- 29 ask each question for the other role, every other input ASSUMEd;
- 8 ask each situation FALSE, every later input ASSUMEd;
- 63 are for the owner, worked by hand. 20 of them, one per question, assert that the answer equals the baseline export's on the same facts;
- 19 are for the occupier, worked by hand.

The baseline reads its enumerations through OTHERWISE (graffiti finding 31). For those inputs, the check that they are not read rests on the parameter script. The situation inputs are BOOLEANs, which fail if read when ASSUMEd.

**Checks.** Run on the stable l4 (VS Code extension 1.6.98), with `JL4_LIBRARY_PATH` unset:

- 0 errors and 0 warnings in all four files;
- 158 assertions satisfied (39 baseline + 119 layer);
- `l4 check wsa-qa.l4` succeeds.

The parameter script (`check_params.py`, session scratchpad) checked all 29 questions:

- `my role` comes first in each;
- every shared parameter is identical in type and `@desc`;
- each situation comes straight after the role;
- no question takes a DEONTIC or EVENT input.
