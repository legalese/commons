# Human Tissue and Transplant Act 1982 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation deposited at
`../../registers/source-bundle/mrdoc_49110.txt` (legislation.wa.gov.au mrdoc 49110,
retrieved 7 September 2026). Its compilation table runs to the Therapeutic Goods Law
Application Act 2024 Pt. 8 Div. 1 (No. 19 of 2024, in operation 30 August 2024). The last
reprint it lists is Reprint 3, as at 19 May 2017. Part 16 of the Assisted Reproductive
Technology and Surrogacy Act 2025 is listed as uncommenced and is not reflected here.

**Checks:** one module (`htta-donation.l4`) and one case file
(`htta-cases-donation.l4`): 50 assertions satisfied, 0 errors, 0 warnings. As a mutation
check, one expected value was inverted in a scratch copy, and the failure was reported.

## Why this Act, and why scoped

This encoding answers **au/wa:REQ-0009** (priority 1). The ledger entry was raised 4 times
by the Western Australian cradle-to-grave lives:

- **chloe c026** (2021-03-20): Chloe registers on the Australian Organ Donor Register at 18
  and asks "Is donation opt-in or presumed?"
- **daniel d021** (2014-04-09): Daniel registers as a donor at 18.
- **jake k097** (2079-04-18): Jake dies at 72. He has been on the Register since 2047, and
  his kidneys are donated. The question is "Is consent presumed or given; who may object?"
- **daniel d092** (2078-10-21): Daniel dies at 82. He is on the Register and the family
  confirms. The question is "Whose consent governs donation?"

All four events cite s 22. This encoding covers s 22 and what is needed to answer those
questions:

- the s 3(1) definitions of child, next of kin and senior available next of kin;
- the coroner's consent where the death is reportable (s 23);
- the brain-death declaration for a body on artificial respiration (s 24(2));
- the age-18 condition on a living donor's consent (ss 9, 12(2), 16), because two of the
  events happen on an 18th birthday.

**Not encoded:**

- designated officers and delegation (ss 4, 5, 5A);
- regenerative tissue, child donors and blood (ss 8, 10–15, 17–21);
- who may remove tissue under an authority (s 24(1), (1A), s 24A);
- postmortem examinations (Part 4);
- trading in tissue (Part 5);
- embryonic stem cell lines (Part 6);
- liability, codes of practice, offences and disclosure (Part 7).

## What the Act turns out to say

### 1. The Act never mentions the Organ Donor Register

None of the lives' registrations has any effect that the text names. The word "Register"
appears in the deposit only in Part 5, for the Therapeutic Goods Register, and in s 32B,
for the Register of Undertakings. The encoding treats being on the Register as the
deceased having "expressed the wish for, or consented to, the removal after death"
(s 22(2)(a)). **That is an inference.** The register is a Commonwealth instrument and was
not read for this encoding. Asserted, on that input.

### 2. Donation is opt-in: there is no presumed consent

s 22(2) has only two limbs:

- **(a)** the designated officer is satisfied that the deceased expressed the wish or
  consented, and had not withdrawn it;
- **(b)** the officer has no reason to believe the deceased objected **and** is satisfied
  that the senior available next of kin consents.

If the deceased said nothing and nobody consents, there is no authority. This answers
c026 and confirms the scenario's own words, "a choice and not a presumption". Asserted.

### 3. On the text, the family cannot override the deceased's own consent

Paragraph (a) says nothing about next of kin. The s 22(5) rule on objections is framed by
reference to the senior available next of kin definition, so it works inside paragraph (b).
Two results follow:

- If Jake is on the Register and Ruby objects, the officer may still authorise (k097).
- If Daniel is on the Register and Priya objects, the officer may still authorise (d092).

So the answer to "who may object?" is narrower than the scenarios suggest. Under (a), no
one may. Under (b), the deceased's own earlier objection and the senior description of
next of kin may. d092's expected answer, "his consent, confirmed by the family", is right
about the governing consent. But the text gives the family's confirmation no legal role.
Hospital practice may well differ, and that practice is not in the Act. Asserted.

### 4. Who the senior available next of kin is, in the lives

For an adult, s 3(1)(b) sets this order:

1. where the person has both a spouse and an adult de facto partner, the one they live with;
2. a spouse, or a de facto partner aged 18 or over;
3. an adult son or daughter;
4. a parent;
5. an adult brother or sister.

Applied to the lives:

- **Jake (k097):** Ruby is the senior available next of kin. Tahlia, his former wife, is in
  no subparagraph at all. Chloe, his sister, ranks only after Ruby and his parents. She
  becomes senior only if Ruby is not available (and no parent is available).
- **Daniel (d092):** Priya, his wife, outranks Anjali and Luca.

For a deceased child, the order is spouse or partner, then parent, then adult sibling, then
guardian. Children of the deceased drop out, and a brother of 14 counts for nothing.
Asserted.

### 5. One objection among equals defeats the rest

s 22(5): where two or more persons share a description, "an objection by any one of those
persons has effect ... notwithstanding any indication to the contrary". Applied to the lives:

- Chloe's father consents and her mother objects: no authority.
- With Priya unavailable, Anjali consents and Luca objects: no authority.
- An objection from a lower description has no effect. Ruby consents and Chloe objects:
  authority.

Two points are **readings, not rulings**: that (5) reaches only the senior description, and
that it does not ask whether the objector is "available". Asserted.

### 6. Part 3 sets no minimum age for the deceased's own wish

s 22(2)(a) asks only whether the deceased expressed the wish. A recorded wish at 16 is
enough on the text. Age 18 matters for **living** donation: an adult of sound mind, advised,
signing away from family and friends, may consent to giving nonregenerative tissue (s 9).
Removal may happen only after 24 hours and if the consent has not been revoked (s 16).
Removing nonregenerative tissue from a living child for transplant is never lawful
(s 12(2)). So turning 18 in c026 and d021 switches on living donation, not the donor
register. Asserted, except the exactly-24-hours boundary, which is left unasserted.

### 7. Other conditions in Part 3

- **Hospital only:** removal under Part 3 needs a body that died in hospital or was brought
  into one (s 22(1), (2)).
- **Reportable deaths:** for a death that is or may be reportable, the coroner must consent
  or direct that consent is not needed (s 23).
- **Ventilated bodies:** where respiration and circulation are maintained artificially, two
  qualifying practitioners must first declare irreversible cessation of all brain function
  (s 24(2)). The facts of k097 do not say whether Jake was ventilated, so the case entered
  here, ventilated with the declarations made, is an assumption.
- **Limits of the authority:** the authority is limited to the tissue and purpose of the
  consent (s 22(3)). A consent to corneas does not reach kidneys.

Asserted.

## What would need doing before this is worth anything

- **Read the Commonwealth side.** The Australian Organ and Tissue Donation and
  Transplantation Authority Act 2008 and the Register's rules need reading, to check
  whether a registration is a s 22(2)(a) "expressed wish" in law or only evidence of one.
- **Read guidance and case law.** WA Health's guidance on donation, and any case law on
  s 22, should be read. Practice on family objection is the likely gap between this text
  and what happens.
- **Settle the s 22(5) readings.** Does it reach only the senior description, and only
  available persons? Does s 22(4) interact with a later objection?
- **Encode the rest of Part 3 and Part 2.** Who may remove tissue (s 24(1A), s 24A), the
  regenerative and blood provisions, and the offences (s 33) are left out.
- **Check the parents' status.** Whether Jake's parents (108 and 106 in the life) are living
  is not stated, and they are left out of the fixtures.
