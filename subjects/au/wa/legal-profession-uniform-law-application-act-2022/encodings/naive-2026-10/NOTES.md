# Legal Profession Uniform Law Application Act 2022 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** compilation from legislation.wa.gov.au (mrdoc 47480, retrieved 7
September 2026), deposited at `../../registers/source-bundle/mrdoc_47480.txt`. The
deposit names no compilation or reprint number. Its compilation table lists the Act
(No. 9 of 2022, assented 14 April 2022; Part 1 in force that day, the rest on 1 July
2022 under SL 2022/113 cl 2), the Legal Profession Uniform Law Application (Levy) Act
2022, and the Workers Compensation and Injury Management Act 2023 Pt 15 Div 3 Subdiv 8
(in force 1 July 2024).

**Checks:** two modules (`lpula-practice.l4`, `lpula-costs.l4`), two case files,
54 assertions satisfied (34 practice, 20 costs), 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0012** (priority 1), raised 3 times by the Western
Australian cradle-to-grave life of Daniel (born 1996-04-09):

- **d023** (2019-12-10, aged 23): "Graduates JD; Practical Legal Training". The
  scenario notes that the Legal Profession Act 2008 applied in 2020 and that the event
  is "replayed under the Uniform Law from 1 July 2022".
- **d031** (2020-08-24, aged 24): "Admitted by the Supreme Court; a practising
  certificate". The question: "Who may engage in legal practice; what is unqualified
  practice?"
- **d038** (2029-03-04, aged 32): acts for a client in an arbitration under a
  conditional costs agreement with a 25% uplift. The question: "Is a conditional costs
  agreement lawful; what is prohibited; is the arbitration agreement binding?"

The ledger lists the Uniform Law Part 2.2, the Admission Rules, and Uniform Law
ss 10, 16-25, 43-49, 181 and 183. This encoding takes what **this Act** says about
those questions: when the Law began to apply (ss 6, 7), who administers it locally
(s 20), admission applications and the bench (ss 113, 114), practising certificate
applications, renewals and deemed refusal (ss 116-118), the transitional carry-over
of old-Act admissions, training and practice (ss 276, 278, 279, 289, 322), and legal
costs determinations, costs agreements, disclosure and costs assessment (ss 3,
132-134, 137, 140, 141, 143, 149, 151, 299). Not encoded: Part 3 (the Board and
committees), registration certificates (ss 120-122), trust accounts, professional
indemnity insurance, fidelity cover, proceedings, registers, enforcement and the other
transitional and consequential provisions.

## What the Act turns out to say

### 1. The sections the lives ask about are not in this Act

Uniform Law ss 10, 16-25, 43-49, 181 and 183 belong to the Legal Profession Uniform
Law, which is set out in the Legal Profession Uniform Law Application Act 2014
(Victoria) Schedule 1. Section 6 of this Act applies it "as a law of the State", and
that applied law is a separate subject here (legal-profession-uniform-law-wa,
au/wa:REQ-0033). This Act provides the WA machinery around it: fees and forms,
which local body administers which part of the Law, the transitional rules and the
State's costs determinations. Nothing here answers d031's "who may engage in legal
practice", and d038's "is a conditional costs agreement lawful" is answered only as
far as s 141 goes (finding 4). Where the answer depends on the Law, it is an INPUT.

### 2. d023 and d031 happened under the old Act; the Act carries over the roll, not the admission

The Law began to apply in WA on commencement day (s 7(1)), which the compilation
table gives as 1 July 2022. Daniel's graduation (2019-12-10) and admission
(2020-08-24) came before it, under the Legal Profession Act 2008. The carry-over
provisions: academic qualifications obtained before commencement day count for Law
s 17(1)(a) (s 278); practical legal training finished before commencement day, or
begun before and finished within 12 months from it, counts for s 17(1)(b) (s 279); an
undecided old-Act application continues as a s 113 application (s 276); supervised
practice before commencement day counts for Law s 49(1) (s 289); and the old roll
"continues ... as the Supreme Court roll" (s 322). No section of this Act deems an
old-Act admission to be an admission under the Law. Treating Daniel as admitted under
the Law rests on s 322 and on Schedule 4 of the Law (s 266(2) applies clauses 11 to
18 of it, which are not in this deposit). That is an **inference**. Asserted for
Daniel: the Law did not apply on 2019-12-10 or 2020-08-24, it did on 2029-03-04, his
name continues on the roll, and his practice from 2020-08-24 counts under s 289.

### 3. Is work in an arbitration contentious business? The text forks

Section 3 defines contentious business as work in proceedings "before a court".
Section 132 says that "In this Division", court "includes an arbitrator". If the s 3
term keeps its ordinary meaning, Daniel's arbitration work is noncontentious business
and a costs determination may cover it (s 133(1)(a)). If s 132 is read into the term,
the arbitration is contentious business before a "court" that s 133(1)(b) does not
list, and a determination covers it only if the Attorney General has declared it
under s 134(1). The text does not decide which reading is right. Both readings are
asserted.

### 4. A costs agreement made under the Law displaces a costs determination; one that is not does not

Section 141(1) makes an applicable costs determination govern taxation and "any other
aspect of the costs charged". Section 141(2)(a) makes that "subject to ... any costs
agreement made in accordance with the Legal Profession Uniform Law (WA) Part 4.3
Division 4". So if Daniel's conditional costs agreement complies with the Law, it
governs rather than the determination; if it does not comply (for example, if the
Law does not allow a 25% uplift for it), the agreement does not displace the
determination under s 141. Whether it complies, and whether the uplift is
permitted, depends on the Law (the ledger cites its ss 181 and 183), which is not deposited here; it is an
INPUT. A court may also go above a determination for "unusual difficulty, complexity
or importance" (s 141(3)). Asserted.

### 5. Renewal windows come from regulations, but the 6-month grace period and backdating come from the Act

A renewal must be made in the standard renewal period or the late fee period, both
set by local regulations (s 117(1)). The Board may reject a late-fee-period
application and must reject one made outside both periods (s 117(3)). But it may
accept one made up to 6 months after the late fee period ends, "even after the expiry"
of the certificate, if the delay was beyond the applicant's control or other
circumstances warrant it (s 117(4)). The certificate is then taken to have continued
from "the 1 July immediately following its expiry" (s 117(5)). The Board is taken to
have refused an application it has not decided within 6 months of lodgement, or of
the compliance day in a Law s 95 notice (s 118(3)). Asserted on hypothetical
periods. The real periods are INPUTS.

### 6. Admission needs a bench of three

Section 114: the Supreme Court "must be constituted by at least 3 judges" when
admitting. Section 113: the application follows the local regulations, the rules of
court and a practice direction, with the fee "(if any)". Asserted.

### 7. Old costs determinations keep their old dates for review

An old-Act determination continues as a s 133 determination (s 299(2)). For the
2-year review in s 137(1), it is "taken to be made on the day on which it was made
under the old Act" (s 299(3)), so a determination made before 1 July 2022 can be due
for review soon after commencement. Asserted on a hypothetical date.

### 8. After an assessment: 28 days, then it binds

A party may apply to the Supreme Court for review "within 28 days after the day on
which the party is notified" (s 149(2)(a)). Otherwise the assessment binds all
parties (s 148). Anything paid above the assessed costs is recoverable as a debt
(s 151). When a law practice gives the Law's s 174(1)(a) disclosure, it must also say
whether a costs determination applies (s 143). Asserted.

## What would need doing before this is worth anything

- Encode the Legal Profession Uniform Law (WA) itself (au/wa:REQ-0033). The lives'
  questions are about ss 10, 16-25, 43-49, 181 and 183 of the Law and Schedule 4.
  Then replace this encoding's INPUTS (compliance with Part 4.3 Division 4, the Law's
  s 17 prerequisites, the s 49 period) with calls into it.
- Retrieve the Legal Profession Uniform Regulations (WA), the local regulations and
  the Admission Rules for fees, renewal periods and training requirements.
- Settle the s 3 / s 132 arbitration fork (finding 3) against any authority or the
  Legal Costs Committee's practice.
- The date helper does not correct days that do not exist in a later month (for
  example, 6 months after 31 August). The cases avoid such days.
- No decided cases, costs determinations or Board practice were consulted.
