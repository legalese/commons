# Education Service Incentive Payment Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment its Legislative History annotates is Act 40
of 2018 (Insolvency, Restructuring and Dissolution Act 2018, s 472, in force
30 July 2020).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0170** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The person here is a teacher in a Government or aided school.

The Act is short (18 sections) and is a frame: the CONNECT Plan itself, with its
award amounts, qualifying-service periods and contribution rates, is in regulations
made under s 3, which are not deposited. This row takes who the Plan must cover
(s 3(1) with the s 2 definitions), who is paid on a member's death (s 3(2)),
protection from creditors and bankruptcy (ss 6, 7), withholding (s 8), the estate
(s 9), recovery (s 10), what the Fund may pay for (ss 12-14), its financial year
(s 15(4)) and the auditor offence (s 16(6)). Fund receipts (s 11), audit procedure,
actuarial examination (s 17) and rules (s 18) are not encoded.

## What the Act turns out to say

### 1. A disciplinary charge alone lets the Minister withhold the award

s 8(1)(b): the Minister may withhold or refuse an award if, at the date of payment,
the member "has been dismissed, reduced in rank or charged with any disciplinary
charge". A charge is enough; no finding is required. The criminal limb (s 8(1)(a))
needs a sentence of death or imprisonment, from a court in Singapore "or elsewhere",
and is closed by a free pardon; a conviction punished by a fine alone does not open
it. s 8(2) applies the same test to Government contributions on the date they fall
due. Asserted.

### 2. Only periodical maintenance for a wife, former wife or minor child can reach the award

s 6 protects awards, contributions and interest from garnishment and attachment for
any debt except "a debt due to the Government" and a court order for "periodical
sums" towards the maintenance of "the wife or former wife or minor child (whether
legitimate or not)". A lump-sum maintenance order, an order for a husband and an
order for an adult child fall outside the exception on its words. Asserted.

### 3. Section 7 shields contributions in bankruptcy, but not the award

s 7 keeps Government contributions and interest from the Official Assignee and out
of the bankrupt's property. It does not mention awards. And s 7(1) says contributions
are not "subject to the debts of any member" with no exception, while s 6(a) lets
the Government attach them for its own debts. The two provisions sit uneasily; the
encoding records the s 7 shield and the s 6 exception separately. Asserted.

### 4. Aided-school contract staff and independent-school staff are outside the Plan

s 3(1)(b) covers aided-school staff employed "other than for a term", for teaching
duties, on pay equivalent to a covered public officer. "Aided school" excludes an
independent school (s 2), so staff employed directly by an independent school are not
covered by either paragraph. Paragraph (a), by contrast, does not require teaching
duties: any permanent Education Service officer below Superscale is covered.
Superscale officers are excluded. Asserted.

### 5. The award is outside the estate but inside estate duty

s 9: CONNECT moneys for a deceased member do not form part of the estate and do not
answer for the member's debts, yet are "property passing on his or her death for the
purposes of the Estate Duty Act 1929". On death before payment, s 3(2) sends the
award to such dependants as the Minister thinks fit, or to the legal personal
representative only if there are none. s 4: no member has "an absolute right" to any
award. Asserted.

### 6. Obstructing the auditor has no written excuse

s 16(6) punishes anyone who "without reasonable excuse" fails to comply with the
auditor's information requirement "or who otherwise hinders, obstructs or delays" the
auditor, with a fine up to $1,000 and no imprisonment. On the words the excuse sits in
the first limb only; the encoding follows the words. Asserted.

### 7. Recovery reaches facts that would have cut salary, not only rank

s 10 lets the Government recover, cancel or reduce an award obtained by wilful
suppression of material facts, or paid in ignorance of facts that would have justified
dismissal or "a reduction of the member's salary". s 8 speaks of reduction in rank.
Asserted.

### 8. The Fund pays for awards, its own costs and Gazetted school purposes

s 12 limits withdrawals to awards, administration, investment, management and audit
costs, and other purposes "related to aided schools or Government schools" that the
Minister Gazettes; s 14(2) requires the Minister's authorisation for any payment.
Treating the s 13 surplus transfer to the Consolidated Fund as a further permitted
withdrawal is an inference from s 14(1). The financial year runs 1 April to 31 March
(s 15(4)). Asserted.

## What would need doing before this is worth anything

- The CONNECT Plan regulations (award amounts, qualifying service, contribution
  rates, withholding and restoration) were not retrieved; without them the Act decides
  almost nothing about how much a teacher receives.
- Whether the s 6 exceptions also qualify "assignable or transferable" is not settled
  here.
- No case law, and no reading of the Insolvency, Restructuring and Dissolution Act 2018
  or the Estate Duty Act 1929 beyond the cross-references.
