# Social Security Act 1991: social security debts (Chapter 5), baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`, no `BECAUSE` except
`LEST BREACH ... BECAUSE`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This encoding is a new layer beside `baseline-2026-10` and `naive-2026-10`, which cover qualification, rates and
compensation recovery and leave the debt provisions out. Both stay as they are; nothing in them was changed or reused by
editing. It covers the debt provisions of Chapter 5: whether a debt arises, what is added to it, when it is due, the
interest charge, how it can be recovered, and when it must or may be written off or waived. These are the provisions a
person meets when the Commonwealth says a social security payment has to be repaid, including the income-data debts that
led to the class action on social security debt raising.

**Edition:** Compilation No. 232, compilation date 1 July 2026 (register id C2026C00336, 6 volumes), deposited at
`../../registers/source-bundle/C2004A04121.txt`. The deposit's metadata warns that the version in force from 20 September
2026 has no registered compilation in the deposit, so amendments commencing on or after that date may be missing. The
formula in s 1237AAB(6), lost from the text deposit, is taken from `../../registers/source-bundle/C2004A04121.formulas.md`
(entry "s 1237AAB(6)", recovered 2026-10-24 from the Word rendering of the deposited compilation).

**Files:**

- `ssa-debts-dates.l4`: the date arithmetic, the only module that imports `daydate`.
- `ssa-debts.l4`: the rules and the exported questions.
- `ssa-cases-debts.l4`: 126 assertions, expected values worked by hand from the text (the compounding interest and the
  present value with a calculator, separately from the encoding).

**Checks:** `l4 run` with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset, on each of the three
files: 0 errors, 0 warnings; `ssa-cases-debts.l4` has 126 assertions written and 126 satisfied (2026-11-07, after the fixes
from the independent verification). A
deliberately wrong assertion added to a scratch copy was reported as failed.

## Seat

**The person said to owe the debt** (the debtor), usually someone who received a social security payment, asking "Do I
owe this, how much, by when, what can be done to recover it, and can it be waived?". The Act is written as powers and
duties of the Secretary. Each one is encoded as what it means for the debtor: whether a debt arises, what is added, the
due day, whether interest charge runs, which recovery methods are open, and whether a waiver or write-off must or may
happen. What the Secretary or a court must be satisfied of is asked as a fact ("Is the Secretary satisfied that ..."),
never decided. s 1224AB (joint liability) is asked from the seat of the person convicted in relation to another
person's contravention, who becomes a debtor through that section.

The defaults followed:

- **The Act alone.** Instruments are not deposited: the indexed small debt amount, the Minister's interest rate for
  s 1237AAB(6), the s 1229E(2) exemption instrument and the s 1237AB class-waiver instruments. The figures they would supply
  are inputs, or (for s 1237AB) out of scope.
- **The text's own actors**: the debtor, the Secretary and the Commonwealth.
- **Judgments as conditional inputs**: entitlement apart from the (1AB) reasons, good faith, reasonable excuse, special
  circumstances, capacity to repay, severe financial hardship, cost effectiveness and proof capable of sustaining
  proceedings.
- **The Act's own definitions in L4**: "social security benefit" (s 23(1)), the s 1223(1AB) reasons, "irrecoverable at
  law" (s 1236(1B)), capacity to repay (s 1236(1C)), and the s 1229D interest charge rate. Borrowed terms are asked as
  facts: income from personal exertion, pension age and the minimum youth allowance age, severe financial hardship, and
  the Criminal Code offences.
- **One debt** is the unit.
- **Machinery out**: s 1229G guidelines, s 1230B overseas application, the ministerial instrument powers.

## Scope

**In:**

- **Part 5.2:** s 1223(1), (1AA)-(1AG), (1B), (1C), (2), (9); s 1224AB; s 1228B(1)-(5); s 1229(1)-(2); ss 1229A, 1229B,
  1229C(3), 1229D, 1229E, 1229F(1)-(2) (the determination as an input); s 1230C(1)-(3); s 1230D.
- **Part 5.3:** s 1231(1A), (1AA), (1B), (2); s 1233(1)(e), (2), (4); s 1234(1A), (4); s 1234B.
- **Part 5.4:** s 1236(1A)-(1C), (3) (in the description); s 1237A; s 1237AA; s 1237AAA; s 1237AAB(1)-(6);
  s 1237AAC(4)-(6) (the notional entitlement as an input); s 1237AAD.

**Exported questions (31), each with `@export` and `@desc` on every input:**

- `Does section 1223 make my payment a debt`
- `Am I jointly liable for the other person's debt`
- `How much is my 10% penalty`
- `Must I be given a debt notice`
- `By when must I pay my debt`
- `Am I liable to interest charge on my unpaid debt`
- `Am I liable to interest charge for a missed arrangement payment`
- `By when must I pay after my arrangement ends`
- `Which month sets my base interest rate`
- `What is the daily interest charge rate`
- `How much interest charge accrues`
- `Can my debt be recovered by court action or garnishee notice`
- `Must my debt be deducted from my payment`
- `Can my payment be reduced to nil`
- `When can a garnishee notice first take my money`
- `What is the most a garnishee notice can take`
- `Can my arrangement be ended or changed`
- `Is there a time limit on recovering my debt`
- `Can my debt be written off`
- `How much is waived for administrative error`
- `How much is waived for an underestimate of property`
- `How much is waived for a longer sentence`
- `Must my small debt be waived`
- `Can a debt be raised for this amount`
- `How much is waived on settlement`
- `How much is waived after 80% is recovered`
- `What is the present value of my unpaid amount`
- `Can my part-payment offer be accepted`
- `How much is waived under my part-payment agreement`
- `How much is waived for unclaimed parenting payment`
- `Can my debt be waived for special circumstances`

**Regulative rules:** the duty to pay the debt by the due day (s 1229(2), 28 days from the notice) and the duty to make an
arrangement payment by the end of its day (s 1234(1A)) are `DEONTIC` rules whose `LEST BREACH` says what the breach
starts: interest charge under s 1229A or s 1229B. The 28 days are one definition (`the days to pay`), used both as the
duty's `WITHIN` and by `By when must I pay my debt`, so the due day and the duty cannot drift apart. The exported interest questions take plain dates and build the trace
inside, so no exported question takes a `DEONTIC` or `EVENT` input.

**Out, and why:**

- **The special debt provisions** (ss 1223(7)-(8) add-on amounts, 1223A income streams, 1223AA-1224EA (other than s 1224C, below) one-off and advance
  payments, 1227 assurance of support, 1227B, 1228 overpayments under other Acts, 1228A comparable foreign payments).
  Each is a separate debt head for a particular payment, outside the general debt a claimant meets. s 1222A's "if, and
  only if" means that s 1223's "no" is only a no under s 1223 (see "Negatives").
- **s 1224C (Data-matching Program debts)**: not tied to one payment, and close to the income-data debts this encoding is
  about, but it only makes recoverable an amount that is already a debt under s 11(6) of the Data-matching Program
  (Assistance and Tax) Act 1990. That Act is not deposited, so whether such a debt exists cannot be worked out here.
- **s 1229(3)** (more than one notice may be given): changes no answer from the debtor's seat; the due day runs from "the
  date of the notice" the person is asked about. Which of several notices fixes the due day is not settled by the text.
- **s 1233(1)(f)-(g)** (amounts or percentages out of each later payment) and **s 1233(3)-(8)**: the notice's terms are
  the Secretary's choice, and the offence and the payer's protection are the garnishee's seat.
- **s 1234(2)-(3)** (when an arrangement takes effect): reflected in the input "was an arrangement in effect" of the
  interest charge questions, not asked separately; the commencement day is a term of the arrangement.
- **ss 1236(2) and 1237(2)** (when a write-off or waiver decision takes effect): the day is set by the decision itself,
  which the debtor cannot state in advance. The note to s 1237(2) is reflected in finding 2.
- **s 1237(1)** (waiver only in the listed sections): reflected by encoding each listed section on its own; a debtor who
  meets none of them gets 0 or FALSE from each. s 1237AB is out (below).
- **The garnishee debtor's own liability** (ss 1230, 1230A) and **the financial institution's** (s 1234AA): these are
  another person's seat.
- **Deductions by consent from another person's payment** (s 1234A): that is the consenting person's seat. The consent is
  revocable at any time (s 1234A(3)).
- **s 1229C(1)-(2)**: when interest charge becomes due and that it is a debt. These are reflected in the accrual
  question, not asked separately.
- **s 1236(1A)(c)**: whereabouts unknown, which the debtor cannot state about themselves.
- **s 1236(1B)(d)**: death without an estate, which is the estate's seat.
- **s 1236A**: the waiver sections apply to every amount outstanding, so it changes no answer.
- **s 1237AAC(1)-(3)**: unclaimed family payment and family allowance, payments abolished long ago.
- **s 1237AAE**: assurance of support debts.
- **s 1237AB**: class waivers, made by instrument and not deposited.
- **Part 5.5**: departure prohibition orders.
- **Review and appeal**: the Social Security (Administration) Act 1999 is not deposited.
- **s 1223(1AE)**: backdated correcting determinations under the Administration Act.

## Negatives (rulings of 2026-10-29, 2026-11-04 and 2026-11-05)

The functions return `BOOLEAN` where the text says no in its own words. That covers s 1222A's "if, and only if" read with
s 1223(1)'s "if", s 1223(1AA), (1AF), (1B) and (2) "does not apply" / "is not a debt", s 1236(1A) "if, and only if",
s 1230C(2) "only if", s 1231(1A) "if", s 1231(1AA) "must not", s 1237AAB(5) "must not ... unless", and the "if" of each
"must waive" section. They return `MAYBE BOOLEAN` where the text is silent. The fork lines, for a reviewer to overrule:

- **s 1223(1AD)**, `Does section 1223 make my payment a debt`: answers `NOTHING` when (1AD) displaces (1AC) for an
  error payment made under a determination in effect while the person was otherwise entitled. The other reading is
  `JUST FALSE` (the determination made the payment payable). That turns on the Administration Act, which is not deposited.
- **s 1234(4)**, `Can my arrangement be ended or changed`: answers `NOTHING` when none of (a)-(c) holds, because the list
  is not closed with "only" (ruling (c) of 2026-11-05). The other reading is `JUST FALSE`.
- **s 1230D**, `Can a debt be raised for this amount`: `JUST FALSE` below the small debt amount. At or above it the answer
  is `NOTHING`, because s 1230D is silent there.
- **s 1237AAD and s 1236**: "may". `TRUE` means the power is open on these facts, not that it will be exercised. The
  descriptions say so.

- **s 1236(1C)**, `Can my debt be written off`: if the debt is recoverable by deductions without severe financial hardship,
  the debtor is taken to have capacity. With hardship, the "unless" only lifts the deeming; capacity is then the same
  open question as when deductions are not available (`no capacity to repay otherwise`), not deemed absent. Corrected on
  2026-11-07 after the independent verification (the first version treated hardship as no capacity).

## What the Act turns out to say

1. **A s 1223 debt is the payment the person was not entitled to, instalment by instalment.** s 1223(1) makes "the amount
   of the payment" (or the part, s 1223(9)) a debt when the person "was not entitled for any reason to obtain that
   benefit". The debt arises when the benefit is obtained. Chapter 5 itself contains no method for working out
   entitlement. It depends on the rate and qualification provisions for each payment as made, so the encoding asks it as a
   fact (`entitled apart from those reasons`). Nothing in Chapter 5 lets a debt be fixed by spreading an annual income
   figure across the payment periods. Whether such a figure shows non-entitlement is a question for the rate provisions
   and the evidence. Asserted only as an input.
2. **No time limit, and write-off does not end the debt.** s 1234B lets recovery action start "at any time", and s 1236(3)
   keeps a written-off debt recoverable. Only waiver is a permanent bar (the note to s 1237(2)). Asserted
   (`Is there a time limit on recovering my debt` 20 years: FALSE).
3. **"No proof capable of sustaining legal proceedings" makes a debt irrecoverable at law** (s 1236(1B)(b)) and opens
   write-off, but write-off is discretionary and does not extinguish the debt (finding 2). Asserted.
4. **The administrative-error waiver has a 6-week window** (s 1237A(1A)). A debt raised within 6 weeks of the first
   payment that caused it (or of the end of the notification period, whichever is later) cannot be waived under
   s 1237A(1), however clear the error. Fork: "within a period of 6 weeks from" the first payment is read as ending on the
   42nd day after it (the Acts Interpretation Act, s 36, is not deposited), and "whichever is the later" is read as the
   later of the two ends. Asserted at the boundary (raised on day 42: no waiver; day 43: waived).
5. **s 1237AAD(a) asks for "one of" four subparagraphs.** Read literally, (ii) (the debtor's own justified conduct) is met
   even where another person's knowing conduct, known to the debtor and not justifiably left uncorrected, also
   contributed. A reading that requires every contributor's conduct to be excused would answer FALSE. The literal reading
   is encoded and asserted.
6. **The Act's own example in s 1237AAB(6) is a cent out.** The formula gives $18,693.3155, which is $18,693.32 to the cent.
   The example prints $18,693.33, and its image prints a surplus closing bracket (recorded in the sidecar). The encoding
   follows the formula. Asserted.
7. **s 1237AAA still prints $250, but the amount is indexed from 1 July 2026** (s 1191 item 71, s 1192(9)), and the indexed
   figure is not in the compilation. It is an input; the cases use 250.
8. **s 1222A(a) ends "as the case may be; or; or"**: a doubled connective in the deposited text, harmless.
9. **s 1228B(1)(b) runs (i), (ii), (v)**: (iii) and (iv) are repealed. Only a social security benefit, disability support
   pension or pension PP (single) attracts the penalty. The age pension and carer payment do not. Asserted.
10. **s 1231(1AA)(a) (no reduction to nil causing severe financial hardship) is read as applying to an election under
    s 1231(1B)**, because (1B) works by a decision "under subsection (1A)". The other reading lets the election override
    hardship. Asserted (consent with hardship: FALSE).
11. **The due day** under s 1229(2) is "the 28th day after the date of the notice", counted with the notice date as day 0
    (notice 3 March 2026, due 31 March 2026). A payment on the due day is in time; interest charge runs from the next day.
    Asserted with the `DEONTIC` trace.
12. **Interest charge compounds daily** (ss 1229A(3), 1229B(3): each day's rate is applied to the unpaid amount plus the
    charge from previous days). The rate changes each quarter (s 1229D(2)), so the accrual question takes one quarter at a
    time.

## What would need doing before this is worth relying on

- Deposit the Social Security (Administration) Act 1999 (notification requirements, Divisions 8-10 of Part 3, review), the
  Acts Interpretation Act 1901 (s 36, periods of time), and the s 1229E(2) and s 1237AAB(6) instruments.
- Encode the special debt heads of Part 5.2 and s 1237AAE, if a scenario needs them.
- An independent test pass and the human gates.
