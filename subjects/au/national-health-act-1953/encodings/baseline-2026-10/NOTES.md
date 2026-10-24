# National Health Act 1953, Part VII (pharmaceutical benefits) — patient baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the one question that can reach a gap (a private hospital supply's safety net value) answers `NOTHING`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0079` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

## Edition

**Compilation No. 157**, compilation date 19 September 2026, includes amendments up to Act No. 90, 2026, as deposited at `../../registers/source-bundle/C1953A00095.txt`. Part VII Division 1 is at lines 234–1030, Division 2 from line 1031, Division 4A (indexation) at lines 3630–3747.

**Brought in:** reg 17A (value for safety net purposes) of the National Health (Pharmaceutical Benefits) Regulations 2017, Compilation No. 16, compilation date 15 August 2026 (register id F2026C00834), deposited at `../../../national-health-pharmaceutical-benefits-regulations-2017/registers/source-bundle/F2017L00313.txt` (lines 231–238), under the same CC BY 4.0 terms as the Act (that subject's `SOURCE-LICENSE.md`).

**Not brought in:** the Minister's s 85(2)–(3) declarations and determinations (the Schedule of Pharmaceutical Benefits), the s 84AAA early-supply instrument, the s 84BA out-patient medication determination, and the s 85B special patient contributions — none deposited, each asked as a fact. The indexed amounts (finding 2) are inputs.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nha-patient.l4` | `nha-cases-patient.l4` | 51 written, 51 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The patient** at the pharmacy, and the family member whose medicines count with theirs. The questions are the patient's: "Can I get this medicine on the PBS?", "Am I a concessional beneficiary (or a veteran's dependant)?", "What is the most the pharmacist may charge me?", "May they discount it?", "Have I (or my family) reached the safety net?", "How much of what I paid counts?", "Whose medicines count?", "Until when does my card last?", "How much can I get back?".

Section 87 addresses the approved supplier; it is encoded as the most the patient may be charged. The Secretary's and suppliers' satisfaction (ss 84DA, 84E, 87A) is asked as a fact.

The 2026-10-18 defaults:

- **The Act, with the instrument that sets its numbers.** Followed for reg 17A (deposited). The indexed amounts are substituted by the Act itself under s 99G, not by an instrument; the s 99G formulas were dropped from the text deposit, so the amounts in force are inputs and the cases use the printed figures, labelled (finding 2).
- **The actors the text names:** the patient (general patient, concessional beneficiary, dependant, card holder) and their family, the approved supplier (pharmacist, approved medical practitioner, hospital authority), the PBS prescriber, the Minister and the Secretary.
- **Judgments handed to others are answered conditionally:** whether the Secretary is satisfied the patient was entitled (s 87A); whether the medicine is listed in the form prescribed (the Minister's declarations); whether a supply is an early supply (the Minister's instrument).
- **The Act's own definitions are worked out from facts:** concessional beneficiary (s 84(1)), dependant (s 84(4), (7)), family (s 84B), the safety nets (ss 84C, 84CA, 99F), the period of a card (s 84J), eligible for increased discounting (s 87AA). Borrowed terms (eligible person and Australian resident under the Health Insurance Act 1973; the Social Security Act cards; the Veterans' Entitlements Act entitlements) are asked as facts.
- **One case:** one supply for the charge; one calendar year for the safety net.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** the approval of pharmacists and prescribers, payments to suppliers, prices, price disclosure, supply guarantees, the Remuneration Tribunal, the Pharmacy Authority, cost recovery, export restrictions.

## Read with the Health Insurance Act 1973 baseline

`../../../health-insurance-act-1973/encodings/baseline-2026-10/` decides whether a person is an "eligible person" (its `Am I an eligible person`), which s 86(1)(a) borrows and this encoding asks as a fact. That baseline in turn asks "concessional beneficiary" (a National Health Act term) as a fact for the extended Medicare safety net; this encoding's `Am I a concessional beneficiary` answers it. The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here and in the module header, not in code.

## Scope

**In:** ss 84(1) (concessional beneficiary, general patient, general patient charge amount, relevant entitlement period, value for safety net purposes), 84(4), (7), 84B, 84C(1AA)–(1D), 84CA, 84J, 85(2)–(3) (as facts), 86(1)–(4), 86A(1), 87(1), (2), (2A), (3), 87AA, 87A, 89, 99F; reg 17A(3)–(4).

**Out:** Part VII Division 1A's application and issue procedure (ss 84D–84H, 84K–84L, except as the card's effect), s 84C(4)–(4B) (which supplies count: their effect is in the value the patient states, through reg 17A(4)), reg 17A(2) (`NOTHING`), s 84BA, s 85 beyond (2)–(3), ss 85A–85E, 86B–86E (Medicare numbers), s 87(4)–(6) (delivery, hospitals, after hours), ss 88–88A (prescribing), ss 89A–98AC, Divisions 3 to 5, s 100 special arrangements, Parts I–VI and VIII onwards.

## What the Act turns out to say

1. **PBS entitlement borrows Medicare eligibility.** A person is entitled to pharmaceutical benefits if they are an eligible person under the Health Insurance Act 1973 and are being treated by a medical practitioner or another PBS prescriber (s 86(1)), and the benefit is supplied by an approved pharmacist on a PBS prescription (s 89). Officers working overseas and their accompanying families are treated as residing in Australia (s 86(2)–(4)); anyone else the supplier believes is overseas may not be supplied (s 86A). Asserted.
2. **The printed charges are not the charges in force.** The deposit prints a $25.00 general patient charge amount, a $4.60 concessional beneficiary charge and general patient reduced charge, a $1,457.10 general patient safety net and a $42.50 increased discounting ceiling. Each is indexed every 1 January (s 99G), "as if the indexed amount were substituted" (s 99G(2)), except that the general patient charge is not indexed on 1 January 2026 (s 99G(1A)) and the two $4.60 charges are frozen from 2025 to 2029 (s 99G(1B)). The s 99G(3)–(4) formulas were images the text deposit dropped. So every question takes the amount in force as an input, and the cases use the printed figures, labelled as such, plus one hypothetical set of indexed figures. REQ-0104 asked for the amounts in force and the formulas (declined; see finding 11 for the formulas).
3. **The concessional safety net is 36 scripts.** Section 99F defines it as the concessional beneficiary charge "multiplied by 36", so it moves with that charge; this encoding works it out ($165.60 on the printed $4.60). The general patient safety net is a figure of its own. Asserted.
4. **After the safety net, a general patient pays the reduced charge, and a concessional beneficiary pays nothing.** A general patient eligible for a concession card pays the general patient reduced charge (s 87(2)(b)), and a concession card holder the concessional charge (s 87(2)(a)(iii)). An entitlement card prescription that is not an early supply falls in no paragraph of s 87(2), so nothing may be charged under it (s 87(1)); only a brand premium (s 87(2A)) and delivery or after-hours charges (s 87(4), (6)) remain. Early supplies are carved out: an entitlement card holder pays the concessional charge for one, and a concession card holder the general charge. Asserted.
5. **Eligibility for the card comes before the card.** A general patient is eligible for a concession card "at the time of the supply" that takes the year's total to the safety net (s 84C(1B)), and s 87(2)(b) gives the reduced charge to anyone "eligible to be issued with" one, card or not. Where a person paid more because they did not yet hold a card, s 87A(3)–(4) gives a refund if the Secretary is satisfied the failure was not their wilful act. Asserted.
6. **What counts towards the safety net is the co-payment, not the brand premium.** Reg 17A(3) counts "the amount charged under whichever of paragraphs 87(2)(a), (b) and (e) of the Act applies (not including any amount charged under other subsections of section 87)", so a brand premium, a delivery charge and an after-hours fee do not count, and a discounted co-payment counts at the discounted amount. An unlawful charge counts nothing (reg 17A(4)). Asserted.
7. **A concessional beneficiary's general-patient scripts count, but capped.** Supplies made earlier in the year while the person was a general patient count towards the concessional safety net at their value or the concessional charge, whichever is less (ss 84C(1C)(a)(ii), 84CA). Asserted.
8. **The family is spouse and dependent children, for the whole year.** A spouse (married or de facto, not permanently separated, illness aside) and a dependent child — under 16 in the person's custody, care and control, or a full-time student aged 16 to 24 wholly or substantially dependent — count together (s 84B), and a child who was a dependent child at any time in the year counts for the rest of it (s 84B(2)). Asserted.
9. **Discounting below the general charge is allowed only in a band.** A pharmacist may charge a general patient less than the general patient charge (but more than nil) only where the Commonwealth price is above the general patient charge and no more than $42.50, indexed (ss 87(2)(e)(ii), 87AA). Asserted.
10. **Whether a medicine is "on the PBS" is the Minister's declaration**, on the Pharmaceutical Benefits Advisory Committee's recommendation (s 85(2) and its notes), in the forms the Minister determines (s 85(3)). The Schedule is not deposited; the patient states it. Asserted as an input.

11. **The s 99G indexation, computed from the recovered formulas (2026-10-24).** `nha-indexation.l4` IMPORTs `nha-patient.l4`, leaves it unchanged, and works out from the sidecar `../../registers/source-bundle/C1953A00095.formulas.md`:
    - the indexation factor: the September quarter's CPI over the September quarter's a year before (s 99G(4)), to 3 places, raised by 0.001 when the 4th place is over 4, never below 1 (s 99G(5)-(7));
    - the indexed amount (s 99G(3)): the current figure × the factor, to the nearest 10 cents, with a multiple of 5 cents raised by 5 cents (s 99G(1));
    - the five amounts in force from 1 January of a year, indexed year by year from a known figure, skipping the freezes of s 99G(1A)-(1B);
    - the concessional safety net that follows the charge (s 99F).

    The CPI numbers are inputs. The patient still supplies the amounts in force to `nha-patient.l4`'s questions; the new questions say what those amounts become, given the CPI.

    **REQ-0104 is not reopened.** It asked for the published amounts in force, and was declined because pbs.gov.au's terms allow personal use only. Nothing here uses the Department's figures.

    Asserted, on illustrative CPI numbers. For example, a $25.00 charge on a 3% rise becomes $25.75, raised to $25.80.

No computed value disagrees with an existing assertion. **Left for later** (formulas in the sidecar, not encoded, all about prices paid to manufacturers rather than by the patient): the proportional ex-manufacturer price (s 85D); the price reductions in ss 99ACB, 99ACD, 99ACF, 99ACN, 99ACR, 99ADH and 99ADHA; s 103(4AC); and the s 104B(7) transitional price increase.

## What would need doing before this is worth relying on

- **The amounts in force** under s 99G and the dropped formulas (REQ-0104).
- **The Schedule of Pharmaceutical Benefits** (the s 85 instruments), so listing, form, brand premium and authority requirements can be looked up.
- **The early-supply instrument** (s 84AAA) and the out-patient medication determination (s 84BA).
- **Reg 17A(2)** and s 99(2A)–(2B) for private hospital and similar supplies.
- **Case law and departmental practice** were not read.
