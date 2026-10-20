# Migration Act 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example encodings and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. NOT for public use.

**Edition:** Compilation No. 171, compilation date 4 June 2026 ("Includes amendments:
Act No. 75, 2025"; register id C2026C00232), as deposited at
`../../registers/source-bundle/C1958A00062.txt` (retrieved 2026-09-22).

**Checks:** one module (`mig-visas.l4`) and one case file (`mig-cases-visas.l4`),
53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**Requirement REQ-0020** in `subjects/au/requirements.jsonl`: priority 1, raised 3
times by the Western Australian cradle-to-grave life of Daniel:

- **d033** (2025-01-10), Priya's partner visa, temporary now and permanent in two
  years: "On what basis; what must the relationship show; what bridging visa in
  between?"
- **d035** (2027-01-09), the London secondment, with Priya's permanent visa granted
  days before and a resident return visa for the trip: "What does a permanent
  resident need to leave and return?"
- **d047** (2032-02-01), a Skills in Demand visa for an engineer from Chennai, with
  Jarrah becoming a sponsor: "May a foreigner work without a visa; what must a
  sponsor do; what salary?"

The ledger names ss 29, 65, 140E-140H and 235. This encoding covers those questions
first, then the definitions, conditions and exceptions needed to answer them:

- lawful and unlawful non-citizens (ss 5(1), 13, 14);
- permanent and temporary visas (ss 29, 30);
- spouse and de facto partner (ss 5F, 5CB);
- the s 65 decision;
- bridging visas (ss 37, 72, 73);
- when a visa ceases because another comes into effect (s 82(2), (2AA), (3));
- leaving and re-entering (ss 79, 81(2), 82(5), (6), (8));
- allowing a non-citizen to work (ss 245AB, 245AC, 245AG, 486R(5));
- work sponsors, nominations and the civil penalty for sponsorship obligations
  (s 5(1), ss 140E, 140GB, 140H, 140Q).

The Act runs to some 1.5 million characters. **Not encoded:**

- **The Migration Regulations 1994.** Every subclass the lives name is in the
  Regulations: 820/801, 155, 482 and the bridging visas. So are their criteria,
  travel periods, work conditions and the salary threshold. All of these are INPUTS
  here.
- valid applications (ss 45-46A), health and character (s 501), and cancellation
  (ss 109-140);
- the coercion, referral, aggravated and executive-officer work provisions (ss
  245AAA-245AAC, 245AD-245AF, 245AJ);
- sponsor sanctions (ss 140K-140M) and labour market testing itself (s 140GBA);
- detention and removal.

The value of a penalty unit is set by the Crimes Act 1914, not by this Act.

## What the Act turns out to say

### 1. Section 235 is gone, and the Act now penalises the employer, not the worker

The ledger and the d047 event ask about s 235 ("work without a visa"). This
compilation's endnotes record "s 235 ... rep No 1, 2024". That Act is the Migration
Amendment (Strengthening Employer Compliance) Act 2024.

What the Act now offers for d047 is two employer provisions:

- **s 245AB** makes it a contravention to allow an unlawful non-citizen to work;
- **s 245AC** makes it a contravention to allow a lawful non-citizen to work in breach
  of a work-related condition "solely because of doing the work".

Each is an offence (2 years or 360 penalty units, or both) and a civil penalty
provision (240 penalty units, five times that for a body corporate under s 486R(5),
so 1,200). Each is subject to an exception for "reasonable steps at reasonable times
to verify". "Allows to work" (s 245AG) does not cover a contract for services in a
domestic context.

For the worker, the consequences under this Act are his status: without a visa he is
an unlawful non-citizen (s 14). A breach of a visa condition is a ground for
cancellation (s 116(1)(b)), which is not encoded. Asserted (ss 13, 14, 245AB, 245AC,
245AG, 486R(5)).

### 2. A permanent visa carries its holder back by itself, so the resident return visa in d035 may be unnecessary

d035 has Priya take a resident return visa for the London year, although her
permanent visa was granted days before. The Act does not create the resident return
visa (subclass 155 is in the Regulations). Under s 79, she may re-enter "because of
the visa" if the visa is permission for re-entry and is in effect on re-entry. A
visa of the s 29(3) kind gives that permission for "a prescribed or specified
period".

The length of that period is in the Regulations. On an ASSUMED period running past
her return in January 2028, she needs nothing more. Asserted on that assumption.

The Act is harsh once the period has run. **A visa to travel to and enter Australia
during a period ceases if its holder leaves after the period (s 82(6)). It also
ceases at the end of the period unless the holder has entered in it and is in
Australia at its end (s 82(5)).** Read literally, a permanent resident who is abroad
when the re-entry period ends loses the visa itself, not merely the right to return
on it. Asserted.

Whether s 82(5) also reaches a holder granted the visa in Australia who never
leaves is not answered by the text read here (INFERENCE: the Regulations or the
visa's terms must deal with it).

### 3. "What the relationship must show" is in s 5F, and a valid marriage is not enough

A married relationship needs four things (s 5F(2)):

- a marriage valid for the purposes of the Act;
- "a mutual commitment to a shared life as a married couple to the exclusion of all
  others";
- a relationship that is "genuine and continuing";
- living together, or not living "separately and apart on a permanent basis".

So a validly married couple in a marriage of convenience, or one separated for good,
are not spouses. A couple whose marriage is invalid, but who otherwise meet the test,
are de facto partners under s 5CB, unless they are related by family (s 5CB(4)).

Validity comes from Part VA of the Marriage Act 1961 through s 12, so the Hindu
ceremony of d032 adds nothing. The 820/801 criteria that use these definitions are
in the Regulations. Asserted.

### 4. The partner visa is a duty to grant, but the bridging visa is only a power

Section 65 says the Minister, if satisfied of the health and other prescribed
criteria, that nothing prevents the grant, and that the charge is paid, "is to grant
the visa", and otherwise "is to refuse". By contrast, s 73 says only that the
Minister "may grant" a bridging visa to an eligible non-citizen (s 72: immigration
cleared, prescribed or determined) who meets the prescribed criteria.

On the visas in between, s 82 settles what ceases:

- the student visa ceases when the 820 comes into effect (s 82(2));
- the 820 ceases when the 801 does;
- a bridging visa ceases when any visa other than a special purpose or maritime crew
  visa comes into effect (s 82(3));
- a bridging visa coming into effect ends nothing, because it is not a substantive
  visa (s 5(1)).

Which bridging visa Priya would hold is a question for the Regulations (that it would be
Bridging A is general knowledge, not read here).
Asserted (ss 65, 72, 73, 82).

### 5. A sponsor's obligations outlast the sponsorship, and the Act sets no salary

Under s 140E, the Minister "must approve" a work sponsor if the prescribed criteria
are satisfied. Under s 140GB(2), the Minister must approve a nomination when four
conditions are met:

- labour market testing is satisfied, or exempted, where s 140GBA applies;
- any nomination training contribution charge is paid;
- the nominator is an approved work sponsor;
- the prescribed criteria are satisfied.

Section 140H(1) binds a person who "is or was" an approved sponsor. The civil penalty
in s 140Q(1) is 240 penalty units for an approved work sponsor and 60 for anyone
else, so a former sponsor faces less. For a company such as Jarrah these become 1,200
and 300 under s 486R(5).

The Act does not answer "what salary?". Section 140HA(1)(a) requires only that the
Regulations include an obligation about "a market salary rate (however described)".
The Core Skills Income Threshold is not in the Act. Asserted (s 5(1) "approved work sponsor",
ss 140GB, 140Q, 486R(5)).

## What would need doing before this is worth anything

- The Migration Regulations 1994 should be deposited and encoded for subclasses
  820/801, 155, 482 and the bridging visas, including the re-entry period, the 482 work condition and the income threshold. Every answer above stops at the
  Regulations' door.
- The cancellation provisions (ss 116, 118-120) should be read, and the
  worker-facing consequences of working in breach encoded.
- The coercion, referral and aggravated work offences (ss 245AAA-245AEB) and
  sponsor sanctions (ss 140K-140M) should be read.
- The s 82(5) problem for onshore grants (finding 2) needs a reading of the
  Regulations and the case law.
- No case law was searched.
