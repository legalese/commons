# Therapeutic Goods Regulations 1990 (Cth): baseline encoding from the seat of the patient

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
The one duty with a deadline (reg 12A(3)) is a regulative rule, run inside the question (`CONSIDER EVALTRACE ... WHEN FULFILLED`); no exported question takes a DEONTIC or EVENT input.
No REFUSE, no BECAUSE except `LEST BREACH ... BECAUSE`.
No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use as advice.

This is the first encoding of the Regulations. The Act's encodings (`subjects/au/therapeutic-goods-act-1989/encodings/baseline-2026-10/`, vaping goods, and `baseline-2026-11/`, medical devices) are untouched and share no code with this one. This encoding covers medicines and biologicals as a patient meets them, for health and medical negligence work: what information had to come with the medicine, whether an unapproved medicine could lawfully be given, what consent that needs, and whether a trial was run within its conditions.

**Edition:** Compilation No. 131 (register id F2026C01012), compilation date 5 October 2026, including amendments up to F2026L01167, deposited at `../../registers/source-bundle/F1996B00406.txt` (retrieved 6 November 2026).
Today's text is applied to every date (finding 12).
Penalties are in penalty units. The value of a penalty unit (Crimes Act 1914 s 4AA) is not used.
For the 28 days in reg 12A(3), the Acts Interpretation Act 1901 s 36(1) item 6 and s 36(2) are applied from the deposited text at `subjects/au/acts-interpretation-act-1901/registers/source-bundle/C1901A00002.txt`, through the Legislation Act 2003 s 13(1)(a) (deposited at `subjects/au/legislation-act-2003/`). Saturdays and Sundays only; public holidays are not counted.
The parent Act's s 19(6) and s 32CM(4) are read from `subjects/au/therapeutic-goods-act-1989/registers/source-bundle/C2004A03952.txt` to frame regs 12B and 12C; they are not encoded.

**Checks** (stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset):

| File | Exported questions | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|---|
| `tgr-patient.l4` | 15 | 0 | 0 | 0 | 0 |
| `tgr-cases-patient.l4` | (imports the module) | 134 | 134 | 0 | 0 |

Expected values were worked out by hand from the text before the encoding was run. The facts in the cases are invented.

## Seat

**The patient: a person who has been given, prescribed, supplied, compounded, imported or trialled a medicine or biological, and who has been harmed by it or wants to know whether it reached them lawfully.**
Every exported question is phrased as that person would ask it, and every input is a fact they could state, find on the Australian Register of Therapeutic Goods, or get from their doctor or pharmacist.

The Regulations give the patient no right to sue. What they give a claim is the regulatory facts: whether the medicine was lawfully in the patient's hands, what the patient had to be told, what consent the life-threatening exemption needs, and what conditions a trial had to keep. The claim itself lives in other law (negligence, the State civil liability Acts, the Australian Consumer Law), none of it encoded here.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers.** Followed. The Regulations set their own numbers (28 days, 3 and 15 months' supply, 8 weeks, 10 penalty units, 4 July 1995, 1 July 2004). The Poisons Standard, the Customs Act 1901, the Customs (Prohibited Imports) Regulations 1956, the TGA CMI templates, the ICH Good Clinical Practice guideline and the NHMRC National Statement are borrowed, and asked as facts.
- **The actors the text names.** Followed: the sponsor, the medical practitioner, the health practitioner, the guardian, the principal investigator, the ethics committee, the specialist college, the Secretary. Officials appear only as what they may do to, or must do for, the patient.
- **A judgment handed to someone else is answered conditionally.** Followed. Asked as facts: "seriously ill", "reasonably likely", "good medical practice", "freely given", "sufficient information", "clearly legible", "easily understood", "consistent with product information", "life-threatening, or otherwise serious", accordance with the Good Clinical Practice guideline and the National Statement.
- **The instrument's own definitions worked out, borrowed terms asked.** Followed. Worked out: "immediate family" (reg 2), "human embryo" (reg 9B(4), (5)), "Category A patient" and "informed consent" (reg 12A(5)), Part 1 of Schedule 10 (items 2-15 asked as one fact). Asked: the Poisons Standard Schedules, "medical device", "biological", "Class 4 biological", "nicotine pouch", "gene therapy".
- **One case is the text's natural unit.** Followed: one medicine or biological, given to or imported by one patient, or one trial the patient took part in.
- **The instrument's own terms, each with a plain gloss.** Followed in comments and `@desc`s.
- **Operative provisions in; machinery out.** Followed (see Scope).

## Scope

**In:**

- reg 2: "immediate family", "medicinal cannabis products" (as one fact).
- Part 2A: regs 9A (with Schedule 10 Part 1, and Schedules 12 and 13) and 9B.
- reg 12(1)-(3) with Schedule 5 items 1 and 6, and Schedule 5A item 3 (clinical trials under notification) except as listed below.
- reg 12A, including the 28-day duty in (3) as a regulative rule.
- regs 12AB(2) and 12AD (clinical trials under approval, and the conditions on use).
- regs 12B(1), (1A), (1B), (1C) (the tables as one fact), (2), (5), (6); 12BA(1)-(3); 12BB; 12C(1)-(3), (5).
- Acts Interpretation Act 1901 s 36(1) item 6 and s 36(2), Saturdays and Sundays only.

**Out, and why:**

- **The contents of the reg 12B(1B) and (1C) tables** (about 100 medicines, with strengths, forms, routes and indications). Encoding them is tractable but long, and the patient's doctor can say whether the medicine matches an item; asked as one fact. A candidate for a second layer.
- **reg 12B(3), 12BA(4), 12C(4)** (supply must comply with the treatment directions in the authority). The authority is not deposited; whether the supply followed it is a fact about one authority.
- **Schedule 5A item 3 paras (b), (ha), (hb), (i)-(k)** (fees, site notifications, the sponsor's duties to an authorised officer) and **reg 12AC** (officers' powers at a trial site). They are between the sponsor and the regulator and do not change whether the use on the patient kept the conditions.
- **reg 12AAB and Schedule 5B** (disposal of unused emergency goods), **reg 12AA** (information on applications).
- **Schedule 5 items 1A, 2-4, 6A-14 and Schedule 5A items 1, 1A, 1B, 2, 4 onwards.** They exempt goods a patient does not meet as a patient (exports, samples, starting materials, stock held by sponsors, sporting teams) or meets only through a hospital's choices (item 6A hospital compounding in anticipation). Item 1B is noted in finding 7.
- **Part 2** (advertising), **Part 2C** (Register entries and variations), **Part 2CA** (mercury), **Parts 2D, 2E**, **Part 2F** (vaping quantities; the vaping offences are in the Act's `baseline-2026-10`), **Parts 3, 3A-3D** (registration, evaluation, orphan drugs, priority determinations), **Part 4** (manufacturing licences), **Parts 5 and 5A** (testing, exceptional release of biologicals), **Part 6** (committees, Poisons Standard procedure), **Part 7** (charges and fees), **Part 8** (identity cards, delegation, release of information, review of decisions for applicants), **Part 9** (transitional), and **Schedules 1-4, 7, 8, 9, 9A, 14, 16**. These are dealings between sponsors, manufacturers and the regulator, or machinery.

## What the Regulations turn out to say

1. **No cause of action for the patient.** Nothing in the encoded provisions confers a right on the person harmed. The offences (regs 9A, 9B, 12A(3)) carry 10 penalty units each, payable to the Commonwealth. A negligence or consumer claim must be brought under other law. Not asserted (no rule to assert).
2. **Schedule 10 Part 1 item 1 has an exception that circles.** Item 1 covers goods with a Schedule 4, 8 or 9 substance "except therapeutic goods mentioned in another Part of this Schedule"; Part 3 item 3 is "all other therapeutic goods not mentioned in another Part of this Schedule". Parts 2 and 3 apply only "if the sponsor has satisfied the Secretary that the goods do not meet the criteria for mention in Schedule 4, 8 or 9", so the exception can only bite on goods that both contain such a substance and were accepted as not meeting the criteria. Whether goods are in Part 2 or 3 is asked. Asserted (a Schedule 4 medicine accepted into Part 2 or 3 is not in Part 1).
3. **The CMI duty is the sponsor's alone, and reaches only goods on the Register.** Regulation 9A forbids the sponsor's supply without the document, in the pack or "in another manner that will enable the information to be given" to the patient (reg 9A(2)). Nothing here obliges the pharmacist or doctor to hand it over. A medicine not on the Register (special access, personal import, compounded) carries no CMI duty under reg 9A. Asserted.
4. **Older pharmacist-only medicines need no CMI.** Regulation 9A(1A) reaches Schedule 3 medicines only if "approved for registration on or after 4 July 1995". A Schedule 3 medicine that is also in Schedule 10 Part 1 escapes reg 9A(1) through the (1AA) defence, so if it was approved before that date neither subregulation requires a document. Asserted, at the 3 and 4 July 1995 edge.
5. **The embryo statement needs registration and knowledge.** Regulation 9B reaches only goods in the registered or provisionally registered part of the Register, so a listed medicine is outside it, and only where the sponsor "knows" of the embryo material. Asserted.
6. **The life-threatening exemption is wider for biologicals.** Regulation 12A(1) excludes Poisons Standard Schedule 9 and 10 medicines and nicotine pouches; (1A) exempts "all biologicals" with no exclusion. Asserted.
7. **"Category A patient" has two limbs; Schedule 5A item 1B uses only one.** Regulation 12A(5) covers death "reasonably likely ... within a matter of months" or premature death "reasonably likely ... in the absence of early treatment". Schedule 5A item 1B (sponsor stock held for such patients) describes only the second. Stock held under item 1B may therefore not be meant for a patient who meets only the first limb. Item 1B is not encoded; not asserted.
8. **Sending the statement is not a condition of the exemption.** Regulation 12A(2)(a)(iii) requires only that the statement be "completed". Not sending a copy within 28 days is a strict liability offence (reg 12A(3), (3A)) but does not take the medicine outside the exemption. The 28 days run from the day the medicine is given, not from completing the statement. Asserted (two separate questions; the 28-day edges, including a last day on a Saturday moved to the Monday).
9. **Informed consent is defined by its basis, not its form.** Regulation 12A(5) requires consent "freely given" on information about "potential risks and benefits" that was "sufficient ... to make an informed decision". Writing is not required. A guardian may give it. Asserted (each element).
10. **Personal import: "other medicines" has no antecedent, and the months are undefined.** Schedule 5 item 1(c) applies "in the case of other medicines" after (ba) deals with biologicals; it is read as every medicine, and as not reaching biologicals or other therapeutic goods. "3 months' supply" and "15 months' supply" are not given in days; they are asked in months at the manufacturer's maximum dose. The closing "or the medicines have been approved ... under regulation 5 of the Customs (Prohibited Imports) Regulations" is read as an alternative to all of (c)(i)-(iii) (fork register). An overseas doctor's written authority for a Schedule 4 or 8 medicine counts only when the importer carries the goods as a passenger. Asserted, at the 3 and 15 month edges.
11. **The compounding exemption excludes GLP-1 analogues and medicinal cannabis.** Schedule 5 item 6 exempts medicines dispensed or compounded for a particular person, other than gene therapy, medicinal cannabis, GLP-1 receptor agonist analogues and nicotine pouches. A compounded GLP-1 medicine is therefore not exempt from registration. Asserted.
12. **Today's text is applied to past events.** The compilation is No. 131 (5 October 2026). For regulation 12A alone the endnotes list ten amending instruments since it was added in 1991, the latest F2026L00847; the history of the other provisions was not traced. A medicine given or compounded years ago is judged here by today's text. Not asserted beyond the dates the text itself states (4 July 1995, 1 July 2004).
13. **The notified-trial public-interest condition is conjunctive.** Schedule 5A item 3(e): "the Secretary must not, at any time: (i) have become aware that to conduct or continue the trial would be contrary to the public interest; and (ii) have directed that the trial not be conducted, or be stopped". On its words the condition fails only if both happened. It may have been meant as two separate bars. Asserted (awareness alone: within the conditions).
14. **The ethics-committee route differs by product.** For medicines, an authorised prescriber needs no ethics committee approval if practising outside a hospital with no access to one and a specialist college endorsement (reg 12B(1A)), or if the medicine matches a table item (reg 12B(1B), (1C)). For biologicals only the first applies (reg 12C(2)). For authorised vaping substances only inhalation for smoking cessation or nicotine dependence applies (reg 12BA(2)). Asserted.
15. **Nicotine pouches are barred from approvals and authorities, not from the Minister's rules.** Regulation 12BB covers approvals under s 19(1)(a) and authorities under s 19(5). Regulation 12B(5) bars rules under s 19(7A) only for Schedule 8, 9 and 10 substances. Not asserted beyond reg 12B(5).

## Fork register

Ruled conventions applied: `JUST FALSE` only where the text says no in its own words; otherwise `NOTHING` (the 2026-10-29 convention; rulings of 2026-11-04 and 2026-11-05 in `docs/ENCODING-GUIDE.md` section 5). Most questions here are closed definitions ("means"), exemptions "subject to compliance with" conditions, or flat negatives, so they answer a BOOLEAN or an enumeration that names the condition not met. Sites decided case by case under Meng's ruling of 2026-11-05:

- reg 9A, `Must my medicine come with a consumer medicine information document`: outside reg 9A's reach the answer is "regulation 9A requires no document for it", not a general no. Other law (labelling orders, State poisons law) may still require information.
- reg 12A(3), `Was the statement about me sent in time`: a copy sent on or before the day the medicine was given is taken as in time. The other reading is that the 28-day window opens only after the giving.
- reg 12B(5), `Can a health practitioner supply me this medicine under the Minister's rules`: JUST FALSE for a Schedule 8, 9 or 10 substance (flat negative, "must not specify"); NOTHING otherwise, because the rules are not deposited.
- regs 12B, 12BA, 12C, `Can an authorised prescriber's authority cover my treatment`: TRUE means the Regulations let an authority reach the patient. Whether the doctor's authority does depends on its terms. FALSE comes from "may only be given" (s 19(6)) and reg 12BB's "must not be given".
- Schedule 5 item 1(c): the Customs (Prohibited Imports) approval is read as an alternative to all of (i)-(iii). The other reading is that it replaces only (iii).
- Schedule 5A item 3(e): read as conjunctive (finding 13). The other reading treats each limb as a bar.
- Enumerated answers report the first condition not met, in the order of the text; a later failure is not reported.

## What would need doing before this is worth relying on

- Encode the reg 12B(1B) and (1C) tables, so the ethics committee question can be answered from the medicine rather than asked.
- Deposit the Poisons Standard, so the Schedule 3, 4, 8, 9 and 10 questions can be answered from the substance.
- Deposit earlier compilations and gate each provision by its own commencement (finding 12).
- Count public holidays in the Acts Interpretation Act s 36(2) roll-forward (place-dependent).
- Encode the claim law the patient sues under (the State civil liability Acts, the Australian Consumer Law), and link it to this layer in a register, not in code.
- An independent test pass.
