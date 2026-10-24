# Student Assistance Act 1973 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. The compulsory repayment amounts, whose formulas were lost in conversion, answer `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0074` in `subjects/au/requirements.jsonl` (a scheduled priority-2 entry for the 20 topics: education). There was no earlier encoding of this Act to keep. No scenario life raised it: the student in the case file (Jarrah) and every date are the encoder's, hypothetical.

Twenty-one questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Edition

Compilation No. 70, compilation date 1 July 2026, includes amendments up to Act No. 17, 2025 (register id **C2026C00238**), as deposited at `../../registers/source-bundle/C2004A00058.txt`.

No instrument is deposited. These are inputs or facts:

- **Set by indexation or another Act** (inputs):
  - the indexed loan amount (s 7E(2); the text's $1,025 is quoted in the answer);
  - the HELP debt indexation factor;
  - the minimum (HELP) repayment income;
  - the 90-day bank bill yield (s 41C);
  - the small-debt amount in s 1237AAA of the Social Security Act 1991 ($250 immediately before 1 July 2026, as the Act's own note says).
- **Set by instrument** (asked as facts):
  - the Minister's s 38A(2) determination;
  - the Minister's s 41D(2) determination;
  - the events the regulations prescribe for s 48.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `saa-student.l4` | `saa-cases-student.l4` | 79 written, 79 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The student.** That means the ABSTUDY recipient who takes a student start-up loan, and the former student (or ABSTUDY or Assistance for Isolated Children recipient) who owes a student debt.

The questions are the ones that person asks:
- "Am I qualified for the start-up loan?"
- "When does it become a debt, and of what kind?"
- "Must I repay it this year?"
- "I've been told I was overpaid: when must I pay, and does interest run?"
- "Can the debt be waived?"
- "Can they stop me travelling?"
- "How do I get the decision reviewed?"

Provisions addressed to the Secretary or the Commissioner are encoded as what they mean for the student.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is deposited (see Edition).
- **The actors the text names:** the student (the debtor), the Secretary, the Commissioner, the Minister, the ART and the courts.
- **Judgments left to others, answered conditionally:**
  - the Secretary's satisfaction about a disqualifying scholarship (s 7C(1)(b));
  - the Secretary's opinion of exceptional circumstances (s 38A(3));
  - the s 41E determination;
  - the s 43F special circumstances;
  - the s 43G belief;
  - the s 43P satisfactions.
- **The Act's own definitions worked out from facts:** qualification period, qualification test day, enrolment test day, relevant debt, and the base interest rate. **Borrowed terms asked as facts:**
  - ABSTUDY Living Allowance and "approved scholarship course", which belong to the ABSTUDY Scheme;
  - "disqualifying education costs scholarship" (from the Social Security Act);
  - HELP repayment income;
  - the Medicare levy reduction.
- **One case:** one student, and one loan or one debt.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** administration, tax file number machinery, information gathering, confidentiality, and regulations.

## Scope

**In:**
- The ABSTUDY student start-up loan:
  - qualification (ss 7C(1), 7D), with the amount quoted (s 7E);
  - the qualification period (s 3(1)) and the qualification test day (s 7C(2));
  - when the loan becomes an ABSTUDY SSL debt, an overpayment or neither (ss 8B, 38A, 39);
  - the debt's amount (ss 8B(3), 8BA);
  - the former accumulated debt (s 9B with s 9CA(1)).
- Whether a compulsory repayment is due: ss 10F(1)(a), (b), (3), and s 12ZK for an FS debt. The amounts are not covered.
- Telling the Department of a prescribed event: ss 48, 49.
- Overpayment debts:
  - when they are due (ss 38, 39, 40, 41A(4));
  - interest charge (ss 41, 41C, 41D, 41E);
  - waiver (ss 43B, 43D, 43E(1)–(4), 43F).
- Departure prohibition orders and certificates: ss 43G, 43P.
- Review: ss 302, 304, 311, 312, 308A, 308F, 308H, 12ZQ, 43U and 43X.

**Out:**
- The ABSTUDY Scheme itself (finding 1).
- The formulas lost in conversion: ss 9C(1), 9CA(2), 10F(1), 12ZLC(1) and 43E(6) (finding 6).
- Part 3 (tax file numbers), and assessments (ss 10H–10L) except as reviewable decisions.
- The Student Financial Supplement Scheme contracts and FS assessment debts (Part 4A Divisions 1–5). The scheme closed to new applications in 2006 (s 3(1) note).
- s 43C (an offence that lengthened a sentence) and s 43 (write-off), except as comments.
- Recovery from third parties and financial institutions: ss 42, 42A.
- The notification and enforcement provisions for departure orders: ss 43J–43M, 43Q–43T, 43Y–43ZC.
- Parts 1, 7, 8 and 10.

## What the Act turns out to say

1. **ABSTUDY is not in the Act.** The Act knows ABSTUDY only as an administrative scheme, "the ABSTUDY Scheme (also known as the Aboriginal Study Assistance Scheme)". Section 7B makes the start-up loan Part "part of the ABSTUDY Scheme", and says Part 2 "does not limit the ABSTUDY Scheme". So the ledger entry's first question, "Am I eligible for ABSTUDY?", is not answered by this Act. Whether a person qualifies for and is paid Living Allowance, and whether a course is an "approved scholarship course", are asked as facts. Relocation payments are not in this Act either (a relocation scholarship is a Social Security Act matter; ABSTUDY's own relocation help is the Scheme's). Raised as `REQ-0095` (admin-policy). Not asserted (a finding about scope).
2. **The start-up loan is $1,025, indexed each 1 January, and at most one per half-year.** Section 7E(1) fixes the amount, indexed under the Social Security Act (an input). The qualification period is 1 January–30 June or 1 July–31 December (s 3(1)). A second loan for the same period is barred by s 7D(a), as is a loan where the person already has a Social Security start-up loan determination for it. The qualification test day is the earliest of three days: the claim decision, the course end (if it falls in the period), and the end of the period. Asserted.
3. **The loan becomes a debt on the later of two days: the day it is paid, and the day after the enrolment test day.** The enrolment test day is the earliest of three days (s 8B(5)): the course end (if in the period), the period end, and the 35th day counted from the course start or the qualification test day, whichever is later. Counting the start day as day 1, the 35th day is the start plus 34. Asserted (29 March 2027 for a course starting 22 February, and four variants).
4. **Exceptional circumstances turn the loan into no debt at all.** Normally, a student who stops studying full-time in circumstances the Minister determines owes the loan at once, as an "ABSTUDY student start-up loan overpayment" (ss 38A(1), 39), dated from the day it was paid. But if the Secretary forms the s 38A(3) opinion (exceptional circumstances beyond the student's control), two things follow. Section 38A(1) does not apply, so there is no overpayment. And s 8B(4)(c) says no ABSTUDY SSL debt "is incurred, and is taken never to have been incurred". So the student owes nothing for that loan. Asserted.
5. **There were two 20% reductions in 2025.** An ABSTUDY SSL debt incurred from 1 January to 1 June 2025, both days included, is reduced by 20% (s 8BA). For the 2024–25 financial year, the former accumulated debt is reduced by 20% at a new step 7 (s 9CA(1)). Asserted ($820 on a $1,025 loan; $1,851.20 for the 2024–25 example).
6. **The formulas that set what a former student must repay are missing from the deposit.** Wherever the Act says "the following formula", the converted text has nothing after it: s 9C(1) (the accumulated debt), s 9CA(2), s 10F(1) (the compulsory ABSTUDY SSL repayment), s 12ZLC(1) (the compulsory FS repayment) and s 43E(6) (present value). The encoding answers whether a compulsory repayment can arise, and `not covered` for how much. A `C2004A00058.formulas.md` sidecar transcribed from the authorised rendering would close it. Asserted (`not covered`, two cases).
7. **No compulsory repayment in three cases.** It is not due unless income *exceeds* the minimum (equal is not enough), and there was an accumulated debt on the 1 June before the assessment (s 10F(1)). It is never due if the Medicare levy low-income rule removes or reduces the person's levy (s 10F(3); s 12ZK(2) for FS). Asserted.
8. **An overpayment debt is due 28 days after the notice, and interest charge runs from the next day.** Under s 40(2), the debt is due on the 28th day after the notice date. Interest charge runs from the following day, which is the notice date plus 29 (s 41(2)), unless one of these applies:
   - a repayment arrangement was in effect at the end of the due day;
   - on the due day the person was receiving ABSTUDY living allowance, AIC, family tax benefit, a social security payment or a veterans' pension or allowance (s 41D);
   - the Secretary has determined there is no interest (s 41E).

   The daily rate is the 90-day bank bill yield (rounded to two decimal places, .005 up) plus 7 points, divided by the days in the calendar year (s 41C). That is 366 in a leap year. If an arrangement ends, the rest is due 14 days later (s 41A(4)). Asserted.
9. **Review in this Act is narrow.** Part 9's internal review (s 302(1)) covers only decisions about the Student Financial Supplement Scheme and decisions about *recovering* ABSTUDY or AIC payments. Paragraph (a) is gone. So this Act gives no review of a decision on a start-up loan claim, or of ABSTUDY Living Allowance; any review of those is the ABSTUDY Scheme's. Asserted. For recovery decisions there is no time limit for internal review, nor for the ART after it (s 312). The Commissioner's decisions to defer or amend an assessment need a written request within 28 days (s 308F(2)), and are taken as confirmed if not answered in 45 days. A departure prohibition order goes to a court, not the ART (s 43U). Asserted.
10. **Several waivers are mandatory, but they are narrow.**
    - **Administrative error (s 43B).** Waiver is required only for the part caused *solely* by the Commonwealth's error, received in good faith, and only if the debt was raised more than 6 weeks after the later of the first payment and the end of any information period. A debt raised on the 42nd day is within the 6 weeks.
    - **Small debts (s 43D).** A debt under the s 1237AAA amount must be waived.
    - **Settlements (s 43E).** These force waiver of the difference. Where at least 80% has been recovered, the rest must be waived if both sides agree it is full satisfaction and the debtor cannot pay more. The statute's own example (Terry, $1,300 waived) is a case.

    Asserted.
11. **There is no time limit on recovery.** Section 42B: "any action ... for the recovery of a debt may be taken at any time". Not asserted (no question turns on it).
12. **Failing to report a prescribed event is an offence with 12 months' imprisonment.** Section 49(1) sets the penalty, subject to reasonable excuse (s 49(1A)), for not notifying within 14 days (s 48). Which events are prescribed is for the regulations, which are not deposited. Raised as `REQ-0096`. Asserted (the 14 days).

## The repayment amounts, computed from the recovered formulas (added 2026-10-24)

**Module:** `saa-formulas.l4`, beside `saa-student.l4`, which it imports and leaves unchanged; cases in `saa-cases-formulas.l4` (16 assertions written, 16 satisfied; `l4 run` 0 errors, 0 warnings in every file; `saa-cases-student.l4` still 79 of 79, `saa-cases-regulations.l4` 16 of 16). Seat: the student, as above.

The sidecar `../../registers/source-bundle/C2004A00058.formulas.md` transcribes the formulas finding 6 lists. The module computes:

- **The accumulated ABSTUDY SSL debt** (ss 9C(1), 9CA(2), 9D): the former accumulated debt plus the debts incurred July to December, less voluntary repayments against them; for 2024-25, those two net of each other and reduced by 20%. Cents are dropped, and under $1 counts as nil. Asserted.
- **How much compulsory repayment** (ss 10F, 10G for ABSTUDY SSL; ss 12ZK, 12ZLB, 12ZLC for FS): the applicable repayable amount less the relevant income-contingent loans liability. The applicable repayable amount is the least of the HESA s 154-20(2) amount, 10% of repayment income and the repayable debt. The answer is nil when the formula gives zero or less, and nil in the three cases of finding 7. Asserted.
- **The present value of an unpaid debt** (s 43E(6)), and whether an offer reaches it (s 43E(5)(b)). The Act's own example gives $4,548.94, which the Act states as $4,548. Asserted (to the dollar).

16. **The compulsory repayment adopts the HELP marginal rates, so it is restated here.** Sections 10F(1) and 12ZLC(1) take "the amount worked out under subsection 154-20(2) of the Higher Education Support Act 2003": 15% of repayment income above the minimum repayment income up to $125,000, and 17% above that (both thresholds indexed under HESA s 154-25). That subsection is text in the deposited HESA, and the module restates it, with the two thresholds as inputs. This departs from "borrowed terms asked as facts", so that the student gets an amount. The other loans' repayments (HESA, VET Student Loans, Social Security Act) are inputs. Asserted.
17. **The repayment is capped by three things, and other loans come first.** On $80,000 against an illustrative $67,000 minimum, the HESA amount is $1,950. A HELP repayment of the same $1,950 leaves nothing to pay on the ABSTUDY debt. Asserted.
18. **Financial Supplement income years before 2019-20 are not covered.** Section 12ZLC(1) speaks only of "the 2019-20 income year; or a later income year". For earlier years the amount answers `NOTHING`. Asserted.

`saa-student.l4`'s `Must I make a compulsory repayment` still answers `not covered` for the amount. Its cases assert that, and they stand. The new question gives the amount. No computed value disagrees with an existing assertion.

**Left for later:** the Financial Supplement contract formulas (ss 12U, 12V, 12X, 12Y, 12ZA, 12ZF, 12ZFA): amounts outstanding, discounts, indexation factors and the FS debt. The scheme closed in 2006.

## What would need doing before this is worth relying on

- **The ABSTUDY Scheme** (the ABSTUDY Policy Manual), as an "as published" source, for Living Allowance eligibility, approved scholarship courses and relocation help. Raised as `REQ-0095`.
- **The regulations and the Minister's instruments**: the s 48 prescribed events, and the s 38A(2) and s 41D(2) determinations. Raised as `REQ-0096`.
- ~~A formulas sidecar for ss 9C(1), 9CA(2), 10F(1), 12ZLC(1) and 43E(6)~~ done 2026-10-24 (`saa-formulas.l4`, findings 16-18).
- **Wider sources.** No guidance, ruling or case was read. Findings 4 and 9 are readings of the text alone.

## The Student Assistance Regulations brought in (added 2026-10-24, REQ-0096)

**Module:** `saa-regulations.l4`, beside `saa-student.l4`, which it imports; cases in `saa-cases-regulations.l4` (16 assertions written, 16 satisfied; 2 `#TRACE` runs of the s 48 duty, FULFILLED on day 10 and BREACH on day 20; `l4 run` 0 errors, 0 warnings; `saa-cases-student.l4` still 79 of 79). Seat: the ABSTUDY recipient (the student, or the parent who receives it).

**Instrument:** the Student Assistance Regulations 2021, Compilation No. 1 (F2022C00508, compilation date 6 April 2022), deposited at `subjects/au/student-assistance-regulations-2021/` with `parent_act` this Act.

**What the module computes:** whether a change is an event prescribed for ABSTUDY (regs 12–21), by who receives the payment, and from that the baseline's `Must I tell the Department of the event` (s 48), notice being given to Services Australia (reg 29); the s 48 duty as a regulative rule.

13. **What a recipient must report depends on who the recipient is.** Course, residence, benefit, income-for-a-reporting-period and "other" events (regs 13, 16, 17, 18, 21(1)) bind every ABSTUDY payee. A partner, a dependent child leaving or going abroad, and assets over the limit bind only a student with independent status (regs 14(1), 20); a new parent or a parent's income 25% over the estimate bind a dependent student or a parent payee (regs 14(2)–(3), 19); the student's death binds a parent payee (reg 21(2)). Asserted.
14. **The s 38A(2) and s 41D(2) instruments are not in force.** A title search of the Federal Register on 23 October 2026 found the Student Start-up Loan Debts and ABSTUDY Student Start-up Loan Overpayments Determination 2016 (F2016L00176), marked not in force, and no in-force instrument under ss 38A(2) or 41D(2) among the titles beginning "Student Assistance", "ABSTUDY" or "Student Start-up". On that search, no circumstances are now determined under s 38A(2) (so `I stopped meeting the study condition in a way the Minister's instrument covers` has nothing to be true of) and none under s 41D(2) (so only the payments in s 41D(1)(a)–(e) exempt a debt from interest charge). The baseline's inputs are kept, because a later determination would revive them; the module does not hard-code FALSE. Not asserted.
15. **The Assistance for Isolated Children Scheme's events (regs 22–28) are not encoded**; an AIC recipient still answers the baseline's s 48 question with the fact.
