# Workers Compensation and Injury Management Act 2023 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 48940, Act
No. 21 of 2023, retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_48940.txt`. The deposit names no compilation or
reprint number. Its compilation table ends with the Workers Compensation and Injury
Management Amendment (Common Law Election Validation) Act 2024 (No. 40 of 2024, in
operation 30 October 2024). The Act, other than a few early provisions, came into
operation on 1 July 2024.

**Checks:** one module (`wcima-compensation.l4`), one case file
(`wcima-cases-compensation.l4`), 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0011** (priority 1), raised **4 times** by the Western
Australian cradle-to-grave lives:

- **Jake k044** (2029-04-12, aged 22): a delivery rider on an ABN; a car door breaks his
  wrist on a delivery. "Who pays for a contractor hurt by a car?" The scenario expects
  "no workers' compensation for a contractor" and cites "s 5 (worker: not an independent
  contractor on these facts)".
- **Jake k085** (2053-10-05, aged 47): employed by Sentinel Security Services, he falls on
  a wet stairwell on patrol in the tower where Jarrah is a tenant; eleven weeks off; a whole
  person impairment assessed at 14%. "What is paid; who assesses impairment; what does 15%
  unlock?" (Part 2, "Part 3 (permanent impairment)", "Part 7 (common law: 15% whole person
  impairment)").
- **Daniel d044** (2031-06-01): Jarrah's first three employees. "Part 8 (compulsory
  insurance)".
- **Daniel d080** (2053-10-05): the same fall from the tenant's side. "Part 2 (the
  employer's liability lies with Sentinel)".

The encoding takes those questions and what they need: who is a worker and who the
employer (ss 12, 13, 215); the employer's liability (ss 6, 17, 19, 20); income
compensation (ss 46, 48, 51, 55-57); medical and health expenses (ss 69, 75-78); the
permanent impairment lump sum (ss 97, 100, 101, twelve of the forty-five Table items); who
assesses (s 186); compulsory insurance (ss 202, 204); and the common law (ss 411, 415,
416, 421-424, 434). Not encoded: journeys, diseases, labour hire, jockeys, working
directors, claims procedure, provisional payments, the s 54 pre-injury rate calculation and
the s 57(3) minimum (both inputs), additional income compensation, miscellaneous and
rehabilitation expenses, hearing loss, death, settlement agreements, injury management,
dispute resolution, double recovery, choice of law, and administration. Amounts fixed by
regulations (the maximum weekly rate, the s 424 maximum damages amount, any greater s 69
percentage) are inputs; so is the general maximum amount, which s 538(1) states as
$243 991 but which "may be updated" and is adjustable by regulations. The cases use
$243 991 and illustrative earnings ($1,500 a week) that the scenarios do not give.

## What the Act turns out to say

### 1. The 15% threshold guards only the employer; a claim against the occupier is not barred at 14%

k085 frames 14% as "one point under the common-law threshold". The threshold in s 421 sits
in Part 7 Division 2, which s 415 confines to "an award of damages against a worker's
employer" for the employer's tort. s 411 defines "third party" as "a person other than the
employer", and s 434(1) lets the worker sue a third party for damages while also claiming
compensation, bringing damages to account (s 434(2)). s 416(d) also takes out a person who is
an employer "only because of section 215". So at 14% Jake cannot sue Sentinel, but nothing
in this Act stops a negligence claim against the building's occupier or manager, if one was at
fault; whether one was, and the Civil Liability Act 2002's own limits, are outside this Act.
Asserted (s 415, s 416(d), s 421, s 434).

### 2. A contractor can be a "worker"; k044 turns on a fact the scenario does not state

There is no "independent contractor" test in s 5; it points to s 12(2). Under s 12(2)(c) an
individual who contracts "for the performance of work by the individual" is a worker if the
work "is not work in the course of or incidental to a trade or business regularly carried on by
the individual in the individual's own name or under a business or firm name", he does not
sublet, and, if he employs, he does part of the work himself. A sole delivery rider on an ABN
who files a sole trader's return probably carries on a business in his own name, and on that
assumption he is not a worker; but if the riding were found not to be his own business, he would
be a worker and the platform his employer. s 13 lets regulations add or exclude classes (none
retrieved). The scenario's answer is plausible, not compelled. Both answers asserted.

### 3. Fifteen per cent is the price of a costly election, not a prize

Reaching 15% does not open damages by itself: s 421(1) also requires an election to retain the
right to seek damages, registered by the Director, with the assessment recorded as the
supporting assessment; and the court must itself be satisfied of 15% (s 421(4)(b)), not bound
by the assessment (s 421(5)). Under 25%, once the election is registered, s 423 cuts income
compensation to 70% for three months and 50% for the next three, ends it after six months,
ends permanent impairment compensation, and ends medical and health expenses compensation for
later expenses; and s 424 caps the damages at a prescribed maximum, payable only "in a most
extreme case". 15% also opens a special increase in the medical expenses limit (s 78(3)(a)).
Asserted (ss 78, 421, 423, 424).

### 4. Eleven weeks off is paid at the full pre-injury rate

s 55(2): the first 26 weeks in which income compensation is payable are paid "at the worker's
preinjury weekly rate of income", and only after that at 85% (s 55(3)), subject to the
prescribed maximum weekly rate (s 56) and the s 57 minimum. Jake's eleven weeks all fall in the
first band. Income compensation stops when the total paid reaches the general maximum amount
(s 51). Asserted (illustrative $1,500 a week: $16,500).

### 5. The permanent impairment lump sum is not measured by the 14% and is paid only on settlement

The lump sum is a percentage of the general maximum amount on the day of injury: the degree of
impairment of the part or faculty of the body (s 98(2)(a)) times the Table percentage (s 101):
for example 10% of the back (75%) is $18,299.33 on $243 991. The whole person figure is for the
common law and s 78, not this. And s 97(3): it "is payable only when the employer's liability
... is commuted by a settlement agreement registered under Division 12". Asserted.

### 6. Who assesses: an approved permanent impairment assessor, not the treating doctor

s 186(1): the assessment "must be made by an approved permanent impairment assessor" (a medical
practitioner approved by WorkCover WA, s 193(1)), except a Dust Disease Medical Panel for dust
disease; it follows the Permanent Impairment Guidelines and is "a percentage" (s 183). Secondary
psychological, psychiatric or sexual conditions are disregarded for the common law threshold
(s 185, not encoded). Asserted (s 186).

### 7. Insurance from the first worker; Sentinel is the employer, and the tenant is not

s 202(2): "An employer must at all times have a current workers compensation policy issued by a
licensed insurer", with no size threshold; s 204(1) fines "$10 000 in respect of each of the
employer's workers" — $30,000 for Jarrah's three (d044). For d080, s 12(3) makes the employer
"the person with whom the worker has entered into the contract": Sentinel. Jarrah, a tenant with
no contract with Jake or Sentinel, is not an employer; a principal that contracted Sentinel (the
building's owner or manager, inferred) is also taken to be an employer under s 215 only if the
security work "is directly a part of or process in the trade or business of the principal" and
the premises are under its control or management. The scenarios cite "Part 8 (compulsory
insurance)" and "Part 3 (permanent impairment)": in this compilation insurance is Part 5, Part 8
is Administration, assessment is Part 4 and Part 3 is injury management. Asserted (ss 12, 202,
204, 215).

## What would need doing before this is worth anything

- The Workers Compensation and Injury Management Regulations (the maximum weekly rate, the
  s 424 maximum damages amount, any s 538 variation of the general maximum amount, s 13
  classes) were not retrieved; every one is an input.
- The pre-injury weekly rate (s 54) and the minimum weekly rate (s 57(3)) are inputs; their
  calculation, with board and lodging (s 58) and indexation (s 55(5)), is not encoded.
- Only twelve Table items are encoded; ss 102-106 (subsequent injury, agreement, arbitrator)
  and settlement agreements (Division 12) are not.
- Whether a delivery rider's work is his own business (s 12(2)(c)(i)) needs the case law on
  the WA test; none was searched.
- The third-party path (finding 1) depends on the Civil Liability Act 2002 and occupiers'
  liability law, and k044's CTP claim on the Motor Vehicle (Third Party Insurance) Act 1943
  (see s 414, s 416(b)); each is a separate subject.
