# Australian Passports Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example encodings and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** Compilation No. 21, compilation date 8 November 2025 (includes
amendments to Act No. 60, 2025; register id C2025C00643), as deposited at
`../../registers/source-bundle/C2005A00005.txt` (retrieved 2026-10-13).

**Checks:** one module, one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0014** in `subjects/au/requirements.jsonl`: priority 1, raised
**5 times** by the three Western Australian cradle-to-grave lives:

- chloe **c013** (2011-06-01): Chloe, 8, a first passport for Bali. "Who may apply
  for a child's passport; whose consent is needed?"
- chloe **c068** (2031-06-10): Oliver's passport, aged 0.
- jake **k012** (2016-06-15): Jake, 9, a passport for a school trip.
- jake **k035** (2026-05-10): Jake, 19, a passport for Bali (s 8).
- daniel **d036** (2027-06-14): Anjali, born in London to Daniel, a citizen.

This encoding takes ss 7, 8 and 11 first, with what is needed to answer them: the
definition of a child (s 6(1)), the meaning of parental responsibility (s 11(5)),
the refusal grounds in ss 12 and 14-17 (only their effect, as inputs), when a
document is valid (s 20) and which decisions can be reviewed (s 48).

It does not encode travel-related documents (ss 9, 10), how competent authorities
make refusal/cancellation requests, cancellation, suspension and surrender (ss 22-26),
the offences (Part 4), information disclosure (ss 42-47), names (s 53), or any
Minister's determination. Fees are imposed by the Australian Passports (Application
Fees) Act 2005, and this Act does not state them. When a passport expires is set by a
determination under s 20(2) or by the date on the document. Both are inputs here.

## What the Act turns out to say

### 1. Chloe's 2011 passport is read against a text that was amended in 2015

Endnote 4 records that s 11 was "am No 46, 2006; No 122, 2015". The deposit is the
2025 compilation. So c013 (June 2011) is answered here under s 11 as it stands
after the 2015 amendment. That text may not be the one that applied to Chloe. The
2016, 2026, 2027 and 2031 events all fall after the 2015 amending Act (the
Passports Legislation Amendment (Integrity) Act 2015). The endnotes give its assent as
10 September 2015 and the commencement of sch 1 (items 1-51, 53-61, 66-68) as
8 October 2015. Not asserted.

### 2. Anjali cannot have a passport until her citizenship is approved

s 8: before issuing a passport the Minister "must be satisfied ... that the person
is an Australian citizen". The citizenship encoding (REQ-0006) found that a child
born abroad becomes a citizen by descent on the day the Minister approves, not at
birth. Until then s 8 forbids a passport, even with both parents consenting. The
scenario puts the passport question at d036, beside the registration. It does not
give the approval date, so the encoding takes 2027-07-01 as an assumed application
date and asserts both variants. Asserted.

### 3. The return-to-Australia exception does not reach a child born abroad

s 11(2)(d) lets the Minister issue without consent to a child outside Australia who
"departed Australia less than 12 months before the application" when the Minister
thinks a document is needed for the child's return. Anjali was born in London and
has never departed Australia, so (d) is not open to her. If Priya withheld consent,
only (a)-(c) or a court order could help. A child who left 6 months earlier can use
(d); one who left 12 months earlier cannot ("less than"). Asserted.

### 4. "Each person" with parental responsibility must consent, so one parent can block

s 11(1)(a): unless "each person who has parental responsibility for the child
consents", or a court order permits it, the Minister "must not issue". With only Sue
consenting, Chloe gets no passport unless an exception in s 11(2) applies. The
family-crisis exception needs both an urgent need and that the non-consenting parent
cannot be contacted within a reasonable period. A reachable parent who refuses keeps
the bar in place. The scenario says Chloe's passport was issued "with both parents'
consent", and the encoding agrees. Read literally, a child for whom no-one has
parental responsibility meets (a) without any consent. Asserted.

### 5. Read literally, the two "parent" limbs of s 11(5) are alternatives

s 11(5)(a) covers a parent who has not lost parental responsibility under a Family
Law Act 1975 order. s 11(5)(aa) covers a parent who has not lost it under a Family
Court Act 1997 (WA) order. Read literally, a father stripped of responsibility under
one Act still has it for passport purposes under the other limb. He loses it only
when orders under both Acts have removed it. Whether a court would read the two limbs
as applying to different children is an inference this encoding does not test.
Asserted on the literal reading.

### 6. A child is "under 18 and ... never been married"; at 19 Jake needs no one's consent

s 6(1). At k035 Jake is 19. s 11 is not engaged, and s 7 gives a citizen an
entitlement subject only to s 8 and Division 2. A married 17-year-old is not a child
either. s 17 forbids a second document while the first "is still valid or is
suspended". The deposit does not say when Jake's 2016 passport expires (that depends
on the date printed on it or a determination). The encoding assumes 2021-06-15 and
asserts that a still-valid or suspended passport blocks a new one unless a
determination permits it. Asserted.

### 7. Issuing a passport to a child cannot be reviewed, and neither can a refusal the Minister sends to court

s 48(a)(ii) excludes "a decision to issue an Australian travel document to a child"
from review, so a parent who objects cannot take the issue to the Tribunal. s 48(b)
excludes a refusal after a s 11(3) declaration (the Minister declines the s 11(2)
discretion "because the matter should be dealt with by a court") and a refusal
"because of subsection 12(2)". Issuing to an adult, other refusals and s 22
cancellations are reviewable. s 22AA cancellations are not. Asserted.

## What would need doing before this is worth anything

- Retrieve the s 11 text in force in June 2011 (the compilation before No. 122, 2015)
  and re-run c013 against it.
- Retrieve the Australian Passports Determination: special circumstances (s 11(2)(a)),
  validity periods (s 20(2)), concurrent documents (s 17(2)) and fees and waivers.
- Retrieve the Australian Passports (Application Fees) Act 2005 for the fee amounts.
- Join this encoding to the citizenship encoding so that the date of Anjali's approval,
  rather than an input, decides s 8.
- Check s 11(5)(a)/(aa) against the Family Law Act 1975 and the Family Court Act 1997
  (WA) on which children each covers in Western Australia.
- No case law was searched.
