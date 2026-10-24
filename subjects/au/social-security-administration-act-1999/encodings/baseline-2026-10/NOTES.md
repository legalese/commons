# Social Security (Administration) Act 1999 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. The start day under Schedule 2 clause 4A (a jobseeker or youth allowance claimant who must attend an interview) answers `not covered`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0073` in `subjects/au/requirements.jsonl` (a scheduled priority-2 entry for the 20 topics: social security and benefits). There was no earlier encoding of this Act to keep. No scenario life raised it: the claimant in the case file (Sam, a jobseeker in Perth) and every date are the encoder's, hypothetical.

Sixteen questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Read with the Social Security Act 1991 baseline

`../../../social-security-act-1991/encodings/baseline-2026-10/` answers who is **qualified**, whether a payment is **payable**, and at what **rate**. That covers the age pension, the disability support pension, jobseeker payment and its liquid assets waiting period, youth allowance, carer allowance and carer payment, and compensation recovery. None of it is restated here.

This Act is the procedure around that law: the claim, the start day, the duty to report, compliance, the date a decision takes effect, and review. Where a question here needs to know whether the person is "qualified" on a day, or whether a waiting period or preclusion period applies, it asks that as a fact, which the 1991 baseline answers.

The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here and in the module header, not in code. Debts and their recovery are in Chapter 5 of the 1991 Act, not in this Act.

## Edition

Compilation No. 163, compilation date 5 December 2025, includes amendments up to Act No. 73, 2025 (register id **C2026C00010**, in 2 volumes), as deposited at `../../registers/source-bundle/C2004A00580.txt`.

No instrument is deposited. These are asked as facts:
- the s 14A class of persons who get the benefit of s 13;
- the job search determination under s 42AC(3);
- the reasonable excuse matters under s 42AI;
- the persistent failure instrument under s 42AR;
- the relocation assistance payments specified under s 42AO(3).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ssaa-claimant.l4` | `ssaa-cases-claimant.l4` | 79 written, 79 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The claimant**: the person who claims, receives or has received a social security payment, including the jobseeker with mutual obligations. The questions are the ones that person asks:

- "Do I have to claim, and can I claim from overseas?"
- "I rang first — what day counts as my claim?"
- "From what day am I paid?"
- "What happens if they never decide?"
- "What must I tell them, and by when?"
- "Have I breached my mutual obligations, and what happens to my payment?"
- "From what day does a cut take effect?"
- "How do I get a review, and how far back will a win go?"

Every operative provision addresses the Secretary. Each is encoded as what it means for the claimant.

The 2026-10-18 defaults:

- **The Act alone.** The 1991 Act is read with this one, but not restated (see above). No instrument is deposited.
- **The actors the text names:** the claimant, the Secretary (Services Australia), the Employment Secretary, the ART.
- **Judgments left to others, answered conditionally.** These are all asked as facts:
  - the Secretary's satisfaction under s 13(2)–(3A) (medical condition, caring, special circumstances);
  - the reasonableness of a voluntary act (s 42AE(3));
  - severe financial hardship (s 51);
  - whether work is unsuitable (s 40X);
  - the s 131 discretion.
- **The Act's own definitions worked out from facts:** the deemed claim day, the start day, mutual obligation, work refusal and unemployment failures, the payment suspension period, and the unemployment preclusion and post-cancellation non-payment periods. **Borrowed terms asked as facts:** qualified, principal carer, partial capacity to work, participation payment.
- **One case:** one claimant and one payment.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** administration, nominees, income management, information gathering, confidentiality, offences beyond s 74.

## Scope

**In:**
- s 11: the need for a claim.
- ss 29–31A: where a claim may be made (the exceptions as a fact).
- s 13: the deemed claim day after contacting the Department.
- Schedule 2 clauses 3(1), 4(1), (2), (6) and 5(1): the start day. Clause 4A answers `not covered`.
- s 39(1), (3)–(5): deemed rejection of an undecided claim.
- s 51(1), (4): the advance for severe financial hardship.
- ss 66A, 72(3)(a), (b), (6) and 74: what to report, and by when.
- Part 3 Division 3AA (people who are not declared program participants):
  - the failures: ss 42AC(1), (1A), 42AD, 42AE;
  - the action the Secretary may take: ss 42AF, 42AG;
  - suspension and reconnection: ss 42AL, 42AM;
  - preclusion and cancellation: ss 42AO, 42AP(2), (3), (5).
- s 118(2), (5), (7)–(9), (11), (13): the day an adverse determination takes effect.
- Review: ss 109(1)–(3), 126, 129, 131, 135, 142, 144, and s 147 items 1 and 8.

**Out:**
- The special payments and their claims: ss 12–12K, 17–27B, 46–50A, 59.
- Employment pathway plans (Division 2A): their content and exemptions.
- Declared program participants (Division 3A).
- Payment mechanics (ss 43–62), except s 51.
- Tax file numbers (ss 75–77).
- The automatic cancellations, suspensions and rate reductions (ss 90–106B), and ss 80–85, except as s 118 dates them.
- Concession cards, except s 11.
- Nominees (Part 3A), income management (Parts 3AA and 3B) and schooling requirements (Part 3C).
- Information gathering, confidentiality, offences other than s 74, and the machinery.
- The special date-of-effect rules: s 118(2A), (2B), (2D), (2E), (3), (4), (5A), (5B), (12)–(12D), and ss 109A, 110–116, 120.

## What the Act turns out to say

1. **Ringing first can backdate a claim by up to 13 weeks, but only for people in a class the Secretary's instrument names.** Section 13 treats the claim as made on the day of contact if three things hold: the person was qualified that day, was in "a class of persons determined in an instrument under section 14A", and lodged within 14 days. With a medical condition, caring for someone with one, or special circumstances that the Secretary accepts, the person may lodge more than 14 days and up to 13 weeks later. The s 14A instrument is not deposited, so membership is a fact. Lodging on the 14th day after contact is in time. For crisis payment and the special employment advance, only the special-circumstances limb applies. Asserted.
2. **A claim may be made up to 13 weeks before qualifying, with two exceptions.** A claim made up to 13 weeks before qualifying is taken to be made on the first day of qualification (Sch 2 cl 4). The exceptions are special benefit, and parenting payment where the person qualifies because of a birth. A liquid assets waiting period moves the claim day to the first day qualified, with no 13-week limit (cl 4(6)). An exclusion period running on the start day (a waiting period, preclusion, or gaol) pushes the start day to the day after it ends (cl 5). Asserted.
3. **If the Secretary does not decide within 13 weeks, the claim is taken to be refused.** It is rejected at the end of 13 weeks from the actual claim (s 39(1), (5)). Days spent waiting for information the Secretary asked for are not counted (s 39(4)). The deemed rejection is a decision that can be reviewed (s 129(5)). Asserted (31 May 2027 for a claim of 1 March 2027).
4. **There is a general duty to report within 14 days, but the offence covers only notices.** Under s 66A, anyone who has claimed, is being paid, or has been paid must report a change that "might affect the payment" within 14 days. A notice under ss 67–69 sets 7 days for a compensation payment (from awareness), 28 days for a death, and 14 days otherwise (s 72(3), (6)). The offence (s 74, 6 months' imprisonment) is for failing to comply with a *notice* under ss 67–70A. It does not reach the s 66A duty itself. Asserted (the periods); the scope of s 74 is a reading.
5. **The 15-hour protection.** A principal carer of a child, or a person with a partial capacity to work, commits no failure for refusing, not doing, or leaving work of more than 15 hours a week. This applies to mutual obligation failures (s 42AC(1A)), work refusal failures (s 42AD(2)) and unemployment failures (s 42AE(4)). Asserted.
6. **A suspension ends when the person reconnects; after 4 weeks without reconnecting, the payment is cancelled.** For a mutual obligation or work refusal failure, the payment is suspended until the person meets a reconnection requirement. It is then payable back to the start of the suspension (s 42AL(4)), less any s 42AN reduction for persistent failures. If the person does not reconnect "within 4 weeks after it is notified", the payment is cancelled at the end of those 4 weeks (s 42AM(3), (4)). Asserted (notified 1 March 2027: compliance by 29 March keeps it; cancellation at the end of 29 March otherwise).
7. **Leaving a job without good reason means 4 weeks without a participation payment, or 6 with relocation assistance.**
   - **For a claimant**, the unemployment preclusion period is 4 weeks from the day of unemployment, or 6 if Commonwealth relocation assistance was paid for that job in the previous 6 months (s 42AO).
   - **For a recipient**, the payment is cancelled and no participation payment is payable for the same 4 or 6 weeks (s 42AP(5)).

   Section 42AP(3) says the payment "is cancelled at the start of the following day (the cancellation day): (a) the day that the person becomes unemployed". This encoding reads "the following day" as introducing the list, so the cancellation day is the day of unemployment, and both periods begin then. That is an interpretive choice. Asserted (1 March 2027: payable again from 29 March; with relocation assistance from 12 April).
8. **A cut takes effect from the day of the change if the person reported it and was not paid since.** After the person has reported a change, an adverse determination takes effect from the day of the change, provided no instalment was paid between the change and the decision (s 118(2)). After a statement in response to a notice, it takes effect from the day the matter arose (s 118(5)). For a false statement, or a breach that delayed the decision, it takes effect from whatever day the decision specifies, which may be earlier (s 118(7)–(9)). A suspension followed by cancellation dates from the suspension (s 118(11)). Otherwise it takes effect on the day the decision is made (s 118(13)). Asserted.
9. **Review has no time limit, but 13 weeks decides how far back a win reaches.** There is no deadline to ask for internal review (s 129), except 13 weeks for pension bonus and essential medical equipment payment. There is none for the ART either (s 147 item 1 disapplies the ART Act's s 18). But if the person asks more than 13 weeks after notice of the decision, a win takes effect only from the day of the application (s 109(2); s 147 item 8 for the ART). Within 13 weeks, or with no notice ever given, it goes back to the original day. Asserted (an application on 31 May 2027 after a notice of 1 March 2027 is in time; one on 1 June is not).
10. **Some decisions go internal-only, and the Secretary's own go straight to the ART.** The ART cannot review the decision to impose a reconnection requirement (s 144(faa)), the decision to give an information notice (s 144(k)), or whether payment continues pending review (s 144(m)). Those are reviewable only internally. Decisions made personally by the Secretary or the Chief Executive Centrelink go straight to the ART (s 142(1)(b)). The Secretary *may* continue payment pending review only for decisions that turn on a discretion or opinion, or that would apply a compliance penalty period. Division 3AA compliance decisions are excluded (s 131(1)(aa)). Asserted.

## What would need doing before this is worth relying on

- **The Secretary's and Minister's instruments** under ss 14A, 42AC(3), 42AI, 42AO(3) and 42AR. These decide who benefits from s 13, what adequate job search is, what counts as a reasonable excuse, which payments are relocation assistance, and when failures are "persistent". Raised as `REQ-0106`.
- **Schedule 2 clause 4A** (start day for claimants required to attend an interview), and the declared program participant regime (Division 3A), if a life needs them.
- **The payment-specific date-of-effect rules** (ss 109A, 110–116, 118(2A)–(5B), 120).
- **Wider sources.** No Social Security Guide, ruling or case was read. Finding 7 is a reading of the text alone.

## The Minister's and Secretary's instruments brought in (added 2026-10-24, REQ-0106)

**Module:** `ssaa-instruments.l4`, beside `ssaa-claimant.l4`, which it imports; cases in `ssaa-cases-instruments.l4` (25 written, 25 satisfied; `l4 run` 0 errors, 0 warnings; `ssaa-cases-claimant.l4` still 79 of 79). Seat: the claimant and jobseeker.

**Instruments**, each deposited 2026-10-23 as its own subject with `parent_act` this Act:
- Social Security (Administration) (Class of Persons – Intent to Claim) Determination 2018, as made (F2018L00971), s 14A;
- Social Security (Administration) (Job Search Efforts) Determination 2026, as made (F2026L01408, made 21 October 2026, in force from the day after registration), s 42AC(3); it repealed the 2018 determination;
- Social Security (Administration) (Reasonable Excuse – Participation Payments) Determination 2018, as made (F2018L00779), s 42AI;
- Social Security (Administration) (Non-Compliance) Determination 2018 (No. 1), Compilation No. 1 (F2022C00591), s 42AR(1).

**What the module computes:** whether the claimant is in the s 14A class, feeding the baseline's `On what day is my claim taken to be made`; whether job searches were adequate on the number required, and whether a shortfall is a mutual obligation failure through the baseline's s 42AC question; whether a reason is a matter the Secretary must, or must not, take into account for a reasonable excuse; whether failures must be treated as persistent; and whether a persistent-failure reduction is a half or a whole instalment.

11. **The s 14A class is wide but needs a cause.** Eleven circumstances at any time in the 8 weeks ending on the day of contact (family violence, homelessness, hospital or temporary incapacity, release from prison or psychiatric confinement, separation stress, a birth, a death in the family, arrival as a humanitarian entrant, living in a remote area, a home lost to an extreme event, other special circumstances beyond one's control) put the person in the class only if the circumstance is why the claim could not be lodged on the contact day. Asserted.
12. **Adequate job search is first a count.** The Secretary must check whether the required number of job searches was made; only if it was may the Secretary look at quality (good faith, variety of seniority, pay, fields and methods) or other matters. The module answers the count and leaves quality to the Secretary. Asserted.
13. **Ten matters must be taken into account for a reasonable excuse, but only if they directly prevented compliance.** Housing, literacy, illness or disability, cognitive or mental impairment, drug or alcohol dependency, unforeseen caring duties, criminal violence, a death in the family, being at paid work, being at a job interview. A drug or alcohol dependency is shut out after an earlier excused failure and a refused referral to treatment, unless one of four exceptions applies. Asserted.
14. **"Persistent" is a demerit count followed by an assessment.** Five demerits in 6 active months, or 2 to 4 with one for a job interview, a job opportunity or job-offer sabotage, then a completed Services Australia assessment; a failure within the next 3 active months is persistent. It is never persistent without a demerit (or unexcused) failure in the previous 3 active months. Active months are the instrument's own measure (91 or 182 days, extended for exemptions and penalties, at most 12 months) and are asked as facts. Asserted.
15. **The reduction escalates from half to whole and resets after cancellation.** Half an instalment for the first persistent-failure reduction; the whole instalment if the last one in the previous 3 active months was a half; half again for the first failure after a cancellation. Asserted.
16. **No relocation assistance instrument is in force (s 42AO(3)).** The Relocation Assistance Specification 2014 (F2014L00900) and its 2010 and 2013 predecessors are marked not in force on the Register (title search 23 October 2026). The baseline's `I was paid relocation assistance for that job` input is kept.
17. **The instruments put no duty on the jobseeker**; they direct the Secretary. So no regulative rule is written for them; the jobseeker's own duties are the Act's.
