# Road Vehicle Standards Act 2018 — importer, buyer and seller baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the one question that can reach a gap (an infringement amount the Act does not set) answers `NOTHING`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0081` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

## Edition

**Compilation No. 3**, compilation date 1 January 2025, includes amendments up to Act No. 35, 2024, as deposited at `../../registers/source-bundle/C2018A00163.txt`.

No instrument is brought in. The Road Vehicle Standards Rules 2018 (made under s 82) carry most of the working detail — the entry pathways, the approvals, the further import circumstances and exceptions, the modifications allowed and recall notices — and are not deposited. The Secretary's s 6(5)–(6) instruments are not deposited either. Each is asked as a fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `rvsa-owner.l4` | `rvsa-cases-owner.l4` | 44 written, 44 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The individual who wants to import a vehicle, or to buy or sell one that may not meet the national standards.** The questions are that person's: "Is it a road vehicle?", "May I import it?", "May I sell it (or was the seller allowed to sell it to me) if it is not on the RAV?", "May I modify it?", "Can it be used on the road despite State standards?", "What is the most I can be fined?".

Provisions addressed to the Secretary (ss 6(5)–(6), 14, 20) or the Minister (approvals, recall notices) are encoded as what they mean for the person: whether an instrument puts the vehicle in or out of the Act, whether an approval is held.

The 2026-10-18 defaults:

- **The Act alone.** The Rules are not deposited; the approvals and pathways are asked as facts. Penalties are given in penalty units; the dollar value of a penalty unit (Crimes Act 1914 s 4AA) is an input to one conversion question.
- **The actors the text names:** the person importing, providing or modifying a vehicle, the holder of an approval, the recipient, the consumer, the Secretary and Minister (as sources of instruments).
- **Judgments handed to others are answered conditionally:** whether a vehicle is "designed solely or principally for use in transport on public roads" (judged on its physical and operational features, s 6(3)) is asked as a fact; so is whether a modification takes it outside its entry pathway.
- **The Act's own definitions are worked out from facts:** road vehicle (s 6), permitted to import (s 22(2)), the s 24 exceptions, new road vehicle (s 78(5)). Borrowed terms (constitutional corporation; importation under the Customs Act 1901) are asked as facts.
- **One case:** one vehicle.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** the registers' keeping, the standards themselves (s 12), Parts 4 and 5 (enforcement and administration) except the infringement amounts of s 56, ss 79–82.

## Scope

**In:** ss 5 (motor vehicle, provide, supply), 6, 22, 24, 26, 78, and the penalties in ss 16–18, 22, 24, 26–32, 38–40 for an individual; s 56(2) infringement amounts for a person who is not a body corporate.

**Out:** s 7 (components) except in the penalty list; ss 12–15, 19–21, 23, 25 (the content of the standards, registers and Rules); s 16(3) (the defence where a component was misrepresented); ss 33–35 (executive officers, bodies corporate); the body corporate penalties in ss 38–40 and 56; Part 3 Divisions 2 and 4; Parts 4 and 5; ss 76, 77 (see finding 6), 79–82.

## What the Act turns out to say

1. **Whether a vehicle is a "road vehicle" can be settled by an instrument either way.** Section 6(1) covers motor vehicles designed for public roads, trailers for them, and partly built ones, by their physical and operational features alone (s 6(3)). The Secretary can add classes or particular vehicles, or exclude them; a particular determination beats a class one (s 6(1)(c), (4)). Asserted.
2. **Importing a road vehicle needs one of four permissions at the time of importation**: holding a type approval for its type, a written authority from a holder, an import approval specifying it, or a circumstance in the Rules (s 22(2)). Without one, it is an offence and a civil penalty of 120 penalty units (s 22(3)–(4)). Asserted.
3. **The first sale, gift, loan or hire of a vehicle in Australia is unlawful if it is not on the RAV**, unless it is handed over for work, protection, storage or transport, under a non-RAV entry import approval, or (if made in Australia) with a clear statement that it is not for public roads (s 24). Only the first provision is caught: once a vehicle has been provided in Australia, a later private sale is outside s 24. For a buyer, the question is whether the seller was allowed to provide it. Asserted.
4. **The Act does not stop an owner modifying a car after buying it.** Section 26 reaches only modifications before the vehicle is first provided to a consumer in Australia; later modifications and the vehicle's use are left to State and Territory law (s 78(4)). Asserted.
5. **A new RAV vehicle that met the national standards may be used on public roads even if it fails a State or Territory standard** — but only where s 78(1)(b) links it to Commonwealth power (a constitutional corporation made, supplied, owns or uses it, interstate trade, or a Territory or Commonwealth place), and only while it still complies and is not defective (s 78(4)). Asserted.
6. **The national standards are safety standards for the Australian Consumer Law** (s 77): supplying a vehicle that does not comply engages ACL ss 106 and 122. That is the Competition and Consumer Act's encoding, not this one. Not asserted.
7. **Recall penalties are much higher than the others.** Failing to comply with a recall notice, or supplying recalled vehicles or components in trade or commerce, is a strict liability offence of up to 1,050 penalty units for an individual (5,250 for a body corporate) (s 38(3)); the Part 2 offences are 60 or 120. An infringement notice for a recall contravention states 12 penalty units for an individual, per contravention (s 56(2)). Keeping an imported vehicle past its export-or-destroy date adds up to 10% of the maximum, 12 penalty units, for each day (s 29(4)). Asserted.
8. **Most of what an importer needs to know is in the Rules.** Which approval fits an older used import, a specialist or enthusiast vehicle, or a visitor's car, and who may enter a vehicle on the RAV, are in the Road Vehicle Standards Rules 2018 (ss 15, 19, 22(2)(d), 23). The Rules are not deposited; REQ-0099 asks for them. Not asserted.

## What would need doing before this is worth relying on

- **The Road Vehicle Standards Rules 2018** (REQ-0099): the pathways and approvals.
- **The value of a penalty unit** (Crimes Act 1914 s 4AA), linked from the Crimes Act's encoding when one exists, instead of asked.
- **Bodies corporate** (ss 35, 38–40, 56) for a dealer's seat, if wanted.
- **The Secretary's s 6 instruments**, so the road-vehicle question can be answered from the instrument.
- **Case law** was not read.
