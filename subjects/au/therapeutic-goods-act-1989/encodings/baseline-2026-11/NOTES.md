# Therapeutic Goods Act 1989 (Cth): baseline encoding of Chapter 4 (medical devices), from the seat of the patient

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE, no BECAUSE except `LEST BREACH ... BECAUSE`.
No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use as advice.

This encoding sits beside `../baseline-2026-10/` (Chapter 4A, vaping goods, from the seat of a minor found with a vape). That encoding is untouched; the two share no code. This one adds a layer: the medical-device provisions a person meets when a device implanted in them, or used in their treatment, has harmed them (a pelvic mesh, a breast implant, a joint replacement) and they are weighing a claim.

**Edition:** Compilation No. 89 (register id C2025C00525), compilation date 5 September 2025, including amendments up to Act No. 38, 2025, deposited at `../../registers/source-bundle/C2004A03952.txt` (retrieved 13 October 2026).
Chapter 4 was added by the Therapeutic Goods Amendment (Medical Devices) Act 2002 (No. 24, 2002), Schedule 1 in force 4 October 2002 (endnotes).
The Therapeutic Goods (Medical Devices) Regulations 2002 are not deposited. The essential principles (s 41CA), the reporting periods (ss 41FN(3)(d), 41MP(1)(c)), the reportable medical devices and prescribed facilities (s 3(1), s 41JM) and the exempt devices (s 41HA) are set there, so each is asked as a fact.
Penalties are in penalty units. The value of a penalty unit (Crimes Act 1914 s 4AA) is not used.
For the periods, the Acts Interpretation Act 1901 s 36 is applied from its deposited text at `subjects/au/acts-interpretation-act-1901/registers/source-bundle/C1901A00002.txt`.

**Checks** (stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset):

| File | Exported questions | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|---|
| `tga-devices.l4` | 15 | 0 | 0 | 0 | 0 |
| `tga-cases-devices.l4` | (imports the module) | 137 | 137 | 0 | 0 |

Expected values were worked out by hand from the text before the encoding was run.
The facts in the cases are invented.

## Seat

**The patient: a person who has had a medical device implanted in them or used in their treatment, and who has been harmed by it or fears they will be.**
Every exported question is phrased as that person would ask it, and every input is a fact they could state, or find on the Australian Register of Therapeutic Goods (ARTG) or in a published notice.

The Act gives the patient no right to sue. What it does give a claim is the regulatory facts:

- whether the thing is a medical device;
- who its sponsor and manufacturer are;
- whether it was lawfully supplied (implanting a device is a supply);
- what the supplier faces for an unlawful supply;
- whether a recall or warning can be required, and whether a recall can reach a device already implanted;
- what the sponsor had to tell the regulator, and by when;
- whether the hospital had to report what happened.

Section 41KE says Part 4-9 is "not intended to exclude or limit the operation of any other law". The claim itself lives in that other law: negligence, the Australian Consumer Law's safety-defect and guarantee provisions, and the representative proceedings rules. None of it is encoded here.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows. The regulations are not deposited, so every number they set is an input. These are: the reporting period in days, and whether a device is reportable, exempt or compliant with the essential principles.
- **The actors the text names.** Followed: the sponsor, the manufacturer, the supplier, the chief executive officer of a healthcare facility, the health practitioner, the Secretary and the court. Officials appear only as what they may do to, or must do for, the patient's device.
- **A judgment handed to someone else is answered conditionally.** Followed. Asked as facts:
  - "the Secretary is satisfied" (s 41KA items 1-5A);
  - "it appears to the Secretary" (item 5B);
  - the Secretary's consent (s 41MA);
  - whether the device complies with the essential principles;
  - whether a medical device standard covers the failing parts (s 41MB);
  - whether harm is "likely";
  - whether the sponsor "knows" (s 41MP);
  - whether the person facing a penalty is "the Crown" (s 5), a "corporation" (s 3(1)), or acted in interstate or overseas trade or in relation to the Commonwealth (s 6(1)).

  The court's power to relieve under s 41MPB is described in the answer and not decided.
- **The Act's own definitions worked out, borrowed terms asked.** Followed. These are worked out from facts:
  - "medical device" (s 41BD), with "system or procedure pack" (s 41BF) asked as one fact;
  - "sponsor" (s 3(1));
  - "manufacturer" (s 41BG);
  - whether a supply was covered (s 41MI(1)(b), with ss 41FM, 41GI);
  - "information of a kind mentioned in subsection (2)" (s 41MP(2));
  - "healthcare facility" (s 3(1)).

  Borrowed terms are asked as facts: counterfeit goods (s 42E), "public hospital", "health practitioner".
- **One case is the text's natural unit.** Followed: one device, and one supply of it by one supplier. Implanting is a supply, so the sponsor's supply to the hospital and the hospital's supply to the patient are separate cases. Each reporting duty is one piece of information.
- **The Act's own terms, each with a plain gloss.** Followed in comments and `@desc`s.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**

- s 3(1): "sponsor", "supply" (para (d)), "healthcare facility", "reportable medical device", "exempt device" and "corporation".
- s 5 (the Crown bound, but not liable to prosecution or civil penalty proceedings) and s 6(1) (the Act, other than Part 4-8A, reaches corporations, and others only in interstate or overseas trade, under Commonwealth benefits law, or in relation to the Commonwealth). Both gate the four penalty questions.
- ss 41BD, 41BF and 41BG, including the s 41BG(4) exclusion of a class the regulations prescribe (asked).
- ss 41FM and 41GI, with s 41GQ (the date a cancellation took effect is asked, as the s 41GP notice states it).
- s 41FN(3)(d).
- s 41HC(6B), (6E), (6F) and (6FA).
- s 41JM (except the time and manner of the report, which are prescribed).
- ss 41KA, 41KC and 41KCA.
- ss 41MA(5), (8), (8A), (8B), 41MAA(2) and 41MB.
- ss 41MI(1), (4), (5), (6), (7) and 41MIB.
- ss 41MP, 41MPA and 41MPB (as text in the answer).
- s 41GN(1)(d) (as text in the answer).
- Acts Interpretation Act 1901 s 36(1) item 6 and s 36(2), Saturdays and Sundays only.

**Out, and why:**

- **Importing, exporting and manufacturing** (s 41MA(1)-(4B), (9)-(14), s 41MAA(1), (3), and the import, export and manufacture limbs of s 41MI(1)(a)(i), (ii) and (iv)). The patient meets the supply, not the import or the manufacture. Those limbs would give the same answer for an importer-sponsor or a manufacturer-sponsor.
- **s 41MIA** (a defendant must give 21 days' notice of particulars before adducing evidence for the s 41MI(7) exception). Trial procedure: it decides how the exception is run, not whether it applies.
- **s 41JM(8)** (civil penalty of 30 penalty units on a chief executive officer who does not report). The patient's question is whether the hospital had to report, which is encoded. The penalty on the officer adds nothing the patient can use. It cannot be pursued against the Crown (s 5).
- **Conformity assessment and the Register application machinery** (Parts 4-3 to 4-5, other than s 41FM, and s 41FN(3)(d)). This is a dialogue between the sponsor and the Secretary. The patient meets its result, the ARTG entry and its dates, and that result is asked.
- **The grounds and procedure for suspension and cancellation** (ss 41GA-41GQ, beyond their dates). These are the Secretary's powers. The patient meets their dates and their effect (s 41GI), which are asked.
- **Breach of conditions** (ss 41MN-41MNC), **false statements** (ss 41EI, 41FE, 41MH), **conformity assessment offences** (ss 41ME-41MG), **advertising** (ss 41ML-41MLB, 41MND, Parts 5-1, 5-1A) and **special and experimental use offences** (s 41MO). Each is a further route to liability for the sponsor. None changes what the patient can find out about their own device. They are candidates for a second layer.
- **s 41MK** (wholesale supply). It reaches only a supply to someone who "is not the ultimate consumer", so never the supply to the patient (finding 3).
- **s 41MQ, 41MR** (reporting after an application lapses), **s 41JA-41JJ** (the Secretary's information notices), **s 61** (release of information), and **executive officer liability** (ss 54B, 54BA). The Secretary's information powers, and who may be told what, are machinery from this seat.
- **Fees, charges, the database of unique device identifiers (s 41CE), and medical device standards** (as instruments).

## What the Act turns out to say

1. **The Act gives the patient no cause of action, and keeps the others.** No provision of Chapter 4 confers a right on the person harmed. The penalties go to the Commonwealth. Section 41KE preserves "any other law of the Commonwealth or any law of a State or Territory". An encoding of a device claim therefore needs the Australian Consumer Law and the State civil liability Acts beside this one. Not asserted (no rule to assert).
2. **Implanting a device is a supply, and the hospital that implants a registered device is never "covered" by its entry.** "Supply" includes "supply by way of administration to, or application in the treatment of, a person" (s 3(1)(d)). Section 41MI(1)(b)(i) asks whether the device is "of a kind included in the Register in relation to the person", which means the supplier. So a hospital or surgeon implanting a device on the ARTG under the sponsor's name meets none of the (b) heads, unless an exemption, approval or authority applies. What protects the implanting hospital then depends on who it is:
   - **A public hospital that is the Crown** cannot be prosecuted or face civil penalty proceedings under the Act at all (s 5). Whether a public hospital, or the statutory body that runs it, is the Crown turns on the State law that set it up; it is asked.
   - **A surgeon or other individual** is reached only where s 6(1)(b) reaches what they did: interstate or overseas trade, Commonwealth benefits law, or dealings in relation to the Commonwealth. An implant in one State's hospital, by a surgeon there, will often be outside it. A State law applying the scheme may reach it, and is not encoded.
   - **A corporation** (s 3(1): a foreign, trading or financial corporation), such as a private hospital company, is reached by s 6(1)(a). Its only answer to ss 41MI and 41MIB is the defence that it "was not the sponsor of the device at the time" (s 41MI(6), a legal burden; s 41MIB(2)).

   So the literal reading, that the physical elements of s 41MI(4) and (5) are made out by every hospital implant and the defence does all the work, holds only for implanting hospitals and practitioners that the Act reaches and that are not the Crown. For those it may still be a drafting oversight. Asserted (`Was my device covered when it was supplied to me` is FALSE for a supplier not named; the supplier's penalty is zero when it was not the sponsor, when it is the Crown, and when it is an individual outside s 6(1)).
3. **Sections 41MI and 41MK, and s 41KA item 5, test the Register differently.** Section 41MI asks about inclusion "in relation to the person". Section 41MK(b)(i) and s 41KA item 5 ask only whether the device "is of a kind included in the Register" or "is not included in the Register", in anyone's name. So the s 41KA item 5 recall power does not reach a hospital that implants a registered device, though s 41MI's elements do. Asserted for item 5 (FALSE when the kind is on the Register and nothing else applies).
4. **A recall cannot reach a device that can no longer be recalled because it is implanted, but a warning can.** Section 41KA(4) says a requirement to recall "does not apply to a medical device that cannot be recalled because it has been administered to, or applied in the treatment of, a person". The test is whether the device cannot be recalled for that reason, not whether it was used: a device applied in treatment that can still be retrieved stays within the recall. That is asked. The requirements to inform the public or a specified class of persons, to publish, and to tell the Secretary to whom devices were supplied (s 41KA(2)(b)-(e)) are not limited in that way. For an implanted patient those are the requirements that matter: being told, and being traceable. Asserted.
5. **Knowledge separates the offence from the civil penalty for not reporting.** Section 41MP(1)(b) requires that the sponsor "knows that particular information is information of a kind mentioned in subsection (2)". Section 41MPA(1)(b) requires only that "the information is of a kind mentioned in subsection (2)". A sponsor that never appreciated the significance of reports it held faces the civil penalty (3,000 penalty units for an individual, 30,000 for a body corporate), not the offence. The court may still relieve it (s 41MPB). A contravention of either is a ground to cancel the entry (s 41GN(1)(d)). Asserted.
6. **The period to report starts from awareness, but the Act does not say so.** Sections 41FN(3)(d) and 41MP(1)(c) say only "within the period specified in the regulations". The start and the length both come from regulations that are not deposited. Both are asked. The `@desc` gives 2, 10 or 30 days as examples, from general knowledge of the regulations rather than a deposited text. *Inference, not asserted as law.*
7. **When the hospital's duty to report began cannot be told from the deposited text.** Part 4-8A (ss 41JK-41JM) is "ad No 10, 2023". The endnotes give that Act's schedules four commencements, from 22 March 2023 to 21 March 2025, without saying which schedule added Part 4-8A. The question answers JUST FALSE before 22 March 2023, NOTHING from then to 20 March 2025, and decides from 21 March 2025. Asserted, including both edges.
8. **The essential principles are softer in Part 4-11 than elsewhere.** Section 41BH(2) deems a device that meets an applicable medical device standard to comply, but "other than Part 4-11". The offences and civil penalties get the same result only through s 41MB, where the defendant bears the evidential burden for the offence and must prove the matter for the civil penalty. Asserted (the s 41MB case).
9. **Harm decides which offence is reached, and the defendant must disprove its direct cause.** Both s 41MI(1) and s 41MA(5) carry 5 years or 4,000 penalty units only where the device's use has caused, or is likely to cause, harm. Under s 41MA(5)(e) the harm must be "because the device does not comply". Under s 41MI the s 41MI(7) exception (harm not "directly" from quality, safety, performance, labelling, packaging or improper use) is for the defendant to raise. Without harm, the offence reached is 12 months or 1,000 penalty units. Asserted.
10. **Only health practitioners supplying under s 41HC(6) rules must notify within 28 days.** Section 41HC(6B) binds a person "authorised, by subsection (6) rules". An authorised prescriber holding a s 41HC(1) authority, and a special access approval under s 41HB, carry no notification duty in the Act itself (conditions may impose one). The 28 days run from the day after the supply (Acts Interpretation Act s 36(1) item 6). A last day on a Saturday or Sunday moves to the Monday (s 36(2)). Asserted, including a supply on a Saturday whose 28th day is also a Saturday.
11. **Today's text is applied to past supplies.** The deposited text is the 2025 compilation. The civil penalty provisions ss 41MAA, 41MIB and 41MPA were added by No. 39, 2006. Section 41GS emergency exemptions were added later still. So for a supply before those dates, this encoding reports penalties that did not then exist. Supplies before 4 October 2002 are answered "not reached". Between 2002 and 2025 the answer is today's law, not the law of the day. Asserted only for the 4 October 2002 edge. **This matters for older implants (many pelvic mesh implants date from 2005-2017) and is the first thing to fix:** deposit the compilations in force on the supply dates.

12. **The penalties stop at the Crown and at the edge of s 6(1); the hospital's duty to report does not.** Section 5 binds the Crown but exempts it from prosecution and civil penalty proceedings. Section 6(1) confines the Act, "other than Part 4-8A", to corporations and to interstate, overseas and Commonwealth dealings. So the hospital's s 41JM duty reaches every healthcare facility, public or private, while every penalty encoded here (ss 41MI, 41MIB, 41MA, 41MAA, 41KC, 41KCA, 41MP, 41MPA) is answered "none" for the Crown and for a person outside s 6(1). The two duty questions (`Did the sponsor report in time`, `Was the supply to me notified in time`) report the timing only and do not ask about s 6(1). Asserted (the Crown and s 6(1) cases in each penalty question).

## Fork register

Ruled conventions applied: `JUST FALSE` only where the text says no in its own words; otherwise `NOTHING` (the 2026-10-29 convention; rulings of 2026-11-04 and 2026-11-05 in `docs/ENCODING-GUIDE.md` section 5). Most questions here are closed definitions ("means", "is the person who") or flat negatives ("does not apply"), so they answer a plain BOOLEAN. Sites decided case by case under Meng's ruling of 2026-11-05:

- s 41JM, `Must the hospital report what happened to me`: before 22 March 2023 (before any part of No. 10, 2023 began) the answer taken is JUST FALSE, because the duty did not exist. The other reading is NOTHING, since the endnotes, not the section, say so.
- ss 41FM, 41GI, `the entry in relation to the supplier was in effect on`: the day the suspension "stopped having effect" is taken as the first day the device was not suspended. The other reading treats that day as still suspended.
- ss 41MP, 41MPA, `Did the sponsor report in time`: a report dated before the day the sponsor became aware is taken as `done in time`. The other reading is that it reports something else. For s 41HC(6B), a notification dated before the supply is taken as `not done in time`, because it cannot be a notification of that supply.
- Penalty records: a provision not reached is reported as zeros with a `provision` string saying why. A zero is not a finding that no other provision applies.
- s 41KA: TRUE means the Secretary's power is open on the facts, not that it was or will be used.

## What would need doing before this is worth relying on

- Deposit the Therapeutic Goods (Medical Devices) Regulations 2002, so the essential principles, reporting periods, reportable devices, prescribed facilities and exempt devices can be encoded rather than asked.
- Deposit the compilations of the Act in force on the supply dates that matter (finding 11), and gate each provision by its own commencement.
- Settle which schedule of No. 10, 2023 added Part 4-8A (finding 7).
- Count public holidays in the Acts Interpretation Act s 36(2) roll-forward (place-dependent).
- Encode the claim law the patient actually sues under (the Australian Consumer Law and the State civil liability Acts) and link it to this layer in a register, not in code.
- An independent test pass.
