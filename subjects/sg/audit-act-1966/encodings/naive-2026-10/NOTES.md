# Audit Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/AA1966.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The latest amending Act annotated in the text and listed in the
Legislative History is Act 42 of 2017 (Audit (Amendment) Act 2017, in force 1
November 2017). The source metadata records the version as current at 1 October 2026.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0159** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The Act is short (ss 1-9), so this row takes most of it, read from the side of the
person or business that meets the Auditor-General: whose accounts are audited and who
pays (ss 3, 4), the follow-the-dollar audit of a grant recipient, supplier or
subcontractor (s 4A), entry and seizure (s 6(1)(b), (d)), the duty to answer and the
privileges that do not excuse it (ss 6(6), (7), 6A, 7(1), (2)), what the
Auditor-General may pass on (s 7(3), (4)), and the reporting deadlines (s 8(2)-(4)).
Not encoded: the rest of s 3, s 5 (except as the limit of a s 4A audit), the other
s 6 powers, s 6A(3), s 8(1) and (5)-(9), and s 9 (no regulations retrieved).

## What the Act turns out to say

### 1. A private business can be audited by the State's auditor, but only on a Minister's direction and only on the deal

s 4A (added by Act 42 of 2017) lets the Auditor-General audit "an individual or a
person" who received a grant, subsidy, loan, guarantee, indemnity or financial
assistance from a public authority, the courts or Parliament, who supplies goods or
services to one of them under an agreement or a "relevant subcontract", or who
collects or disburses money for one. But s 4A(3): only if the Minister, satisfied it
is in the public interest, directs it; and s 4A(2) and s 5(2): the audit "must be
limited to" whether the terms and conditions of that grant, supply or collection were
complied with. Asserted.

### 2. Subcontractors are reached, buyers are not

s 4A(4): a subcontract is caught if its performance "fulfils, or contributes to the
fulfilment of" a supply obligation owed to a public body under another contract, so a
subcontractor several steps down from the government contract can be audited. Buying
from the State is not: s 4A(1)(b) speaks of a supply under an agreement to which the
public body is party, but s 4A(2)(b) limits the audit to "a supply BY an individual or
person". Treating a buyer as outside s 4A is this encoding's reading of the two
together. Nor does s 4A reach a grant from a body that only administers public funds
without being a public authority (the list in s 4A(1) names only public authorities,
the courts and Parliament). Asserted.

### 3. There is no privilege to refuse, but there is a use immunity

s 6(7): a person required by the Auditor-General or a person authorised in writing
(s 6(6)) "must" answer and produce. s 6A(1): an individual cannot rely on the
privilege against self-incrimination or exposure to a penalty, legal professional
privilege, any other privilege, or the public interest. s 7(1): a secrecy provision in
another written law does not limit s 6 unless it "expressly excludes" it; s 7(2): an
oath of secrecy exposes no one to an offence or financial penalty for what they do for
s 6. In return, s 6A(2): if the answer might tend to incriminate, what flows from it
is inadmissible against the individual in any civil or criminal proceeding, except a
prosecution under s 177 of the Penal Code 1871 or one "relating to the falsity of the
answer". Asserted.

### 4. The Act creates no offence for refusing

s 6(7) says the person "must" answer, but nothing in ss 1-9 makes refusal an offence or
attaches a penalty. Any sanction would have to come from elsewhere (the s 177 Penal Code
carve-out in s 6A(2) hints at one for false answers; what s 177 says was not read).
Not asserted: there is nothing to assert.

### 5. Seizure needs an expired production notice or a suspected contravention

s 6(1)(d): the Auditor-General may seize a thing in premises he may enter only if a
s 6(2)(a) production notice has been given for it and its period has expired, or if he
considers seizure necessary to obtain evidence of the contravention of any written law.
The premises include those of a third party holding records for an audited body or
person (s 6(1)(b)(iii)), and entry is "without payment" (s 6(5)). Asserted.

### 6. Fees: requested audits are paid for, directed ones are free

s 4(2): the fee for an audit under s 4(1) (one provided by written law, or requested by
the body with the Minister's consent) is a charge on the funds of the body audited, set
by the Minister unless another law fixes it (s 4(3)). s 4(5): no fee for an audit the
Minister directs in the public interest under s 4(4), and s 4(4) reaches only a
"public authority", not a body that merely administers public funds. The Act says
nothing about a fee for the s 3 audits of government departments, the courts and
Parliament; the encoding charges none under this Act (an inference). Asserted.

### 7. The defence carve-out from Parliament is certified, and the certificate is conclusive

s 8(3): the President must present the Auditor-General's report and the statement to
Parliament within 30 days of receipt, or within 14 days after the next sitting begins
if Parliament is not in session. s 8(4), (5): nothing need be presented that the Prime
Minister and the defence Minister certify as necessary for defence and security, and the
certificate is conclusive evidence. s 8(2): if the statement has not reached the
Auditor-General within 7 months after the financial year closes, he must report that to
the President. Asserted (the 7-month boundary itself is not tested).

## What would need doing before this is worth anything

- s 177 of the Penal Code 1871 and the Financial Procedure Act 1966 (s 18 statement and
  the definitions s 2(2) imports) were not read.
- Whether s 6A applies to a company (it speaks only of "an individual") is left open.
- No regulations under s 9, Auditor-General's reports or case law were retrieved.
- Day-counting in s 8(3) is modelled as plain day numbers.
