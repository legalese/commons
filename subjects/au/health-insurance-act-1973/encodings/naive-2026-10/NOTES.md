# Health Insurance Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 136, compilation date 19 September 2026 (includes amendments up to
Act No. 90, 2026; register id C2026C00411), as deposited at
`../../registers/source-bundle/C2004A00101.txt`.

**Checks:** one case file (`hia-cases-medicare.l4`), 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0008** in `subjects/au/requirements.jsonl` (priority 1). The three Western
Australian cradle-to-grave lives raise it 7 times:

- **Chloe:** c002 (enrolled in Medicare on her mother's card: "Is a newborn eligible?"),
  c060 (antenatal care: "What is bulk-billed; what does the hospital charge a public
  patient?"), c065 (Oliver's Medicare enrolment).
- **Jake:** k003 (Medicare from birth), k044 (a car door and a fractured wrist: "treatment
  under Medicare; recovery of benefits from the damages"), k090 (a stroke at 56, three weeks
  in a public hospital: "What does Medicare and the public hospital system cover?").
- **Daniel:** d002 (the Medicare card, 1996).

The encoding takes the provisions those events name, with the definitions, conditions and
exceptions needed to answer them. It is one module, `hia-medicare.l4`: eligibility (s 3(1),
ss 6, 6A, 7), when a benefit is payable (s 10(1), s 17(1)(a), s 19), how much (ss 9, 10, 14),
who is paid and bulk billing (ss 20, 20A), and charging a public patient (s 128C).

**Not encoded:** the Medicare Benefits Schedule (the "table" is made by regulation and was not
deposited, so every Schedule fee is an input, and so is whether a service is prescribed for the
100% rate); whether a service is a "professional service"; the safety nets (ss 10AA-10AE,
10ACA, 10ADA) and indexation (s 10A); ss 15-16G; the practitioner-side bars in ss 19AA-19C and
the My Health Record rules; simplified billing (s 20A(2), s 20AAA); claims (s 20B); everything
in Parts IIA onwards except s 128C. The regulations that s 6A, s 20A(1)(d) and s 128C(1) rely on
were not deposited; their effect is an input. Case fees are hypothetical.

## What the Act turns out to say

### 1. Recovering benefits out of damages is not in this Act (k044)

Jake's event lists "recovery of benefits from the damages" under this Act. The deposited text
has no such rule: the words "damages" and "compensation" appear only in other contexts. The
endnotes record that the Health and Other Services (Compensation) (Consequential Amendments)
Act 1995 (No 132, 1995) amended the Act, and that s 18, amended by No 132, 1995, was repealed by
No 106, 2020. **Inference, not read in the deposit:** the recovery regime sits in the Health and
Other Services (Compensation) Act 1995, which is indexed here as
`subjects/au/health-and-other-services-compensation-act-1995`. What this Act does answer for
k044 is that Jake's GP treatment attracts a benefit like anyone else's. Asserted (the
treatment); the recovery is not encoded.

### 2. "Nothing to pay" in a public hospital is not something this Act promises the patient (k090, c060)

Medicare benefits do not pay for public-hospital care at all: s 17(1)(a) says no benefit is
payable where "the medical expenses ... have been paid, or are payable, to a recognized
hospital", and s 19(2) says none is payable, "unless the Minister otherwise directs", for a
service rendered by or for a State. What protects a public patient is s 128C: a medical
practitioner, a participating midwife, a participating nurse practitioner or someone acting for
one of them must not charge a fee for a public hospital service to a person they know is a
public patient, on pain of 50 penalty units. But only "in circumstances set out in the
regulations", which were not deposited, and **the hospital itself is not in the list**. What
the hospital may charge a public patient, the second half of c060's question, is a matter for
the Health Services Act 2016 (WA) and whatever funding arrangements sit behind it, not for
this Act. Asserted.

### 3. A newborn is eligible from birth, and the Act knows nothing of cards or enrolment (c002, c065, k003, d002)

"eligible person means an Australian resident or an eligible overseas representative", and an
Australian resident is a person who "resides in Australia" and is a citizen, a permanent visa
holder, a New Zealand citizen lawfully present, and so on (s 3(1)). There is no age condition
and no enrolment condition. Chloe, Oliver, Jake and Daniel, citizens by birth living in
Perth, are eligible persons from the day they are born. The Medicare card and enrolment "on her
mother's card" are not in this Act; "medicare number" is defined only by reference to s 84(1) of
the National Health Act 1953. Note that d002 (1996), c002 (2003) and k003 (2006) are tested
against the 2026 compilation, because the text in force then was not deposited. Asserted.

### 4. Bulk billing is an agreement the doctor may offer, not a right (c060)

Bulk billing is an assignment of the benefit under s 20A(1). The eligible person "may enter
into an agreement" with the professional, who "accepts the assignment in full payment of the
medical expenses". Once it is made the patient owes nothing for that service (a reading of
(c)(ii)). Nothing in the Act obliges a practitioner to accept one. Without it, the benefit is
paid to whoever incurred the expenses (s 20(1)): 85% of the Schedule fee outside hospital, 75%
within an episode of hospital treatment, 100% where the regulations prescribe it (s 10(2)). The
85% benefit is never more than $50.00 below the fee (s 10(3), (5)). Amounts are rounded *up* to
5 cents (s 10(4)), and a benefit never exceeds the expenses incurred (s 14(1)). On a
hypothetical $39.10 fee, 85% is $33.235, paid as $33.25. Asserted.

### 5. A temporary partner visa can make Priya an Australian resident; a student visa cannot

Paragraph (f) of "Australian resident" reaches a temporary visa holder who has a permanent visa
application pending and a spouse who is a citizen or permanent visa holder (or a work
authority). So Priya on her 2025 partner visa is eligible, and on her student visa she is not.
A pending parent visa application, or being covered by s 6A regulations, takes her outside (f)
again; under s 6A she would be eligible by regulation instead, without being a resident.
Asserted on Daniel's scenario facts; Priya's own Medicare position is not a scenario event.

### 6. Residence, not citizenship, is the test (Daniel's London year)

A citizen who does not reside in Australia is not an Australian resident, and in any case a
benefit is payable only for a service "rendered in Australia" (s 10(1)), or on a domestic
journey (s 10(1A)). Asserted.

## What would need doing before this is worth anything

- Deposit the Health Insurance (General Medical Services Table) Regulations and the other
  regulations made under ss 6A, 10(2)(aa), 20A and 128C; until then every fee and every
  regulated circumstance is an input.
- Encode the Health and Other Services (Compensation) Act 1995 for k044.
- Encode the safety nets (ss 10AA-10AE, 10ACA, 10ADA) if a life asks what a year of
  out-of-hospital care costs.
- The historical text in force in 1996, 2003 and 2006 was not deposited.
- No case law or Services Australia practice was consulted.
