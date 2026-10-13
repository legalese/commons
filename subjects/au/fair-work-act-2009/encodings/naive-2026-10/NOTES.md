# Fair Work Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 73, compilation date 7 July 2026 (includes amendments up to
Act No. 62, 2026; register id C2026C00355), as deposited at
`../../registers/source-bundle/C2009A00028.txt`.

**Checks:** one case file (`fwa-cases-employment.l4`), 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0002** in `subjects/au/requirements.jsonl` (priority 1). The three Western
Australian cradle-to-grave lives raise it 22 times:

- **Chloe:** c020 (a casual job at 15), c032 (a paid internship), c040 (graduate contract and
  probation), c041 (first payslip), c042 (leave after three months), c056 (Liam changes
  employer), c061 (unpaid parental leave), c063 (Liam's leave), c067 (a flexible working
  request), c072 (she changes jobs), c077 (jury summons).
- **Jake:** k040 and k041 (a delivery platform rider), k060 (security award), k061 and k062
  (an underpayment and a small claim), k086 (redundancy at 49), k087 (cleaning award).
- **Daniel:** d030 (graduate), d042 (he leaves practice), d044 (his first three employees),
  d066 (twelve redundancies).

The encoding takes the provisions those events name, with the definitions, conditions and
exceptions needed to answer them. It is one module, `fwa-employment.l4`.

**Not encoded:**
- the modern awards themselves. The General Retail, Security Services and Cleaning Services
  Awards are not in the Act and were not deposited, so junior rates, overtime, shift
  penalties and minimum rates (c020, k060, k061, k087) are inputs.
- every amount set by regulation, indexation or State law: the high income threshold, a
  prescribed small claims limit above $100,000, and jury service pay. These are inputs.
- the s 15AA multi-factor test. Whether someone is an employee in the ordinary meaning is an
  input. The s 15AB opt-out is not encoded either.
- enterprise agreements, the shiftworker test (s 87(3)), and flexible unpaid parental leave
  (s 72A) beyond noting it.
- the superannuation contribution duty in Division 10A (s 116B), beyond noting it.
- s 120 (FWC varies redundancy pay), s 121(4) (small business employer that becomes
  insolvent), and s 122 (transfer of employment).
- the unfair dismissal remedy, the general protections, and civil penalties.

## What the Act turns out to say

### 1. The Act sets no notice for an employee who resigns

s 117 is an obligation on the employer: "An employer must not terminate an employee's
employment unless" it gives the minimum notice or pays in lieu. For notice given **by** the
employee, s 118 says only that a modern award or enterprise agreement "may include terms
specifying the period of notice an employee must give".

Three of the scenario's notice questions are resignations, so s 117 does not answer them:
- c056: Liam changes employer.
- c072: Chloe leaves Ironbark for Jarrah.
- d042: Daniel leaves practice.

The Act's notice for Chloe and for Daniel is therefore nil, and the answer lies in their
contracts or award. Asserted.

### 2. Redundancy pay falls at ten years, and the scenario's figures for Jake are right

The s 119(2) scale rises to **16 weeks** for 9 to 10 years of service, then drops to
**12 weeks** for "At least 10 years". k086: Jake, 49, with 21 years at Sentinel, gets:
- 12 weeks' redundancy pay;
- 5 weeks' notice: 4 weeks for more than 5 years, plus 1 because he is "over 45 years old"
  with at least 2 years' service (s 117(3)(b)).

Both match the scenario's expected figures. A hypothetical Jarrah employee with 9.5 years
(d066) gets 16 weeks: more than Jake. Asserted.

The encoder reads "over 45 years old" as older than 45, so 45½ qualifies and 45 exactly
does not. That is an inference. Asserted on both sides.

### 3. Small businesses: no redundancy pay, a one-year qualifying period, and no Centrelink notice under fifteen

s 23(1) makes an employer with "fewer than 15 employees" a small business employer.
s 23(4) counts the employees being dismissed. For such an employer:
- s 121(1)(b) switches off redundancy pay. Daniel's three-employee Jarrah (d044) would owe
  none. Asserted.
- s 383(b) makes the minimum employment period for unfair dismissal one year instead of six
  months. Asserted.

Separately, s 530 requires notice to Centrelink only when an employer decides to dismiss
"15 or more employees" for economic, technological, structural or similar reasons. d066's
twelve redundancies need none, as the scenario says. Asserted.

### 4. Two of the scenario's citations point at the wrong section

- **c063 cites "s 72 (concurrent leave)".** There is no s 72 in Part 2-2 of this
  compilation; only s 72A (flexible unpaid parental leave, up to 100 days) remains. Nothing
  in the deposit limits how much leave both parents may take at once.
- **c061 cites "s 83 (return to work guarantee)".** s 83 is consultation with an employee on
  leave. The return to work guarantee is **s 84**. It is encoded but not asserted.

### 5. Liam qualifies for unpaid parental leave by three days

s 67(1) requires 12 months' continuous service "immediately before" the relevant date. For
birth-related leave starting before the birth, s 67(3) makes that date the expected date of
birth. The encoder infers:
- that Liam started with Sparkies on 2029-09-02, when he changed employer (c056);
- that the baby was due about 2030-09-05, because Chloe's leave began two weeks before the
  due date on 2030-08-22.

On those inferences he has 12 months and 3 days, and qualifies. With 11 months he would not.
Chloe (79 months at Ironbark) qualifies easily.

The leave is 12 months (s 70). An extension of up to 12 more may be requested (s 76(1)), but
not beyond 24 months after the birth (s 76(7)). Asserted.

### 6. A paid intern is not on a vocational placement

s 13 excludes only an individual "on a vocational placement". By s 12 that requires a
placement for which the person "is not entitled to be paid any remuneration", required by a
course and authorised by law. Chloe's internship at $25 an hour (c032) fails the first
limb. Whether she is an employee is then the s 15AA ordinary-meaning question, which is an
input here. Asserted.

### 7. A minimum standards order may cover superannuation; it may not deem a rider an employee

s 536KL(1) lists what a minimum standards order may cover: payment terms, deductions,
record-keeping, insurance, consultation, representation, delegates' rights and cost
recovery. There is no paragraph (c) in the deposit. s 536KL(2) says the list does not limit
what may be included. s 536KM bars:
- overtime rates;
- rostering arrangements;
- any term that "deems a regulated worker to be an employee".

s 536KMA bars penalty rates and minimum engagement periods unless the FWC is satisfied a
term is appropriate.

Superannuation is neither listed nor barred. The encoder's reading (an inference) is that
an order may include it. That is the k041 question. Asserted.

Jake (k040) is an employee-like worker under s 15P if he is not an employee and meets 2 of
the s 15P(1)(e) criteria. The case assumes low bargaining power and low authority; the
scenario does not state them. Asserted.

### 8. Leave is per year and accrues progressively; casuals get none

s 87 gives 4 weeks' annual leave a year (5 for an award or agreement shiftworker). s 96
gives 10 days' personal/carer's leave. Both exclude casual service, and both accrue
"progressively ... according to the employee's ordinary hours of work".

c042 expects 4 weeks and 10 days, which are the yearly figures. After three months Chloe
has accrued about 1 week and 2.5 days (assuming constant hours, an inference). Chloe at 15
(c020) was a casual, so she had neither. Asserted.

s 90(2) pays out untaken annual leave however the employment ends, which answers c072.
Asserted.

### 9. Jury service: base pay less jury pay, for ten days only

s 111 applies only to an employee who is not a casual. The employer pays the base rate for
ordinary hours. If the employer asks for evidence, the payment is reduced by the jury
service pay, and nothing is owed until the evidence is given. Payment stops after "the
first 10 days of absence".

The case uses hypothetical figures for Chloe (c077): $400 a day and $300 of jury pay over
15 days come to $3,700. The Act does not say what happens if jury pay exceeds base pay; the
encoding stops at nil (an inference). Asserted.

### 10. Western Australia Day and Labour Day are public holidays only through State law

s 115(1)(a) names eight national days. Others count only if "declared or prescribed by or
under a law of a State or Territory" (s 115(1)(b)), which here is an input from the WA
Act. Asserted.

### 11. Underpayments: six years, and small claims to $100,000

- **s 45** forbids contravening a modern award.
- **s 544** requires an application within 6 years of the contravention.
- **s 545(5)** bars orders for underpayments more than 6 years before the proceedings.
- **s 545(3)** lets a State magistrates court order the employer to pay.
- **s 548(2)** caps small claims at $100,000, or a higher prescribed amount.

Jake's 13-month overtime shortfall of $4,100 (k061–k062) is in time and within the limit.
The shortfall itself depends on the award's overtime rate, which is an input. Asserted.

### 12. Smaller things worth recording

- **Probation (c040).** The Act does not mention probation. What matters is the minimum
  employment period: 6 months for an employer that is not a small business employer
  (s 383(a)). The s 382 test also needs an award, an agreement, or earnings below the high
  income threshold (an input). Asserted, with a hypothetical threshold.
- **Pay slips (c041, d044).** s 536(1) requires a pay slip "within one working day" of
  paying wages. Asserted.
- **Junior employee (c020).** s 12 defines a junior employee as one "under 21". The junior
  rate itself is in the award. Asserted.
- **Superannuation is now in the National Employment Standards.** Division 10A (s 116B)
  requires an employer to make contributions "so as to avoid liability to pay
  superannuation guarantee charge". Whether super is payable (c020, c041) still depends on
  the Superannuation Guarantee (Administration) Act. Not encoded.
- **Service for redundancy pay.** s 22(2)(b) excludes unpaid leave from service for
  redundancy pay. s 22(4) keeps it for notice and for flexible working requests. Chloe's
  parental leave would therefore shorten her redundancy service but not her notice service.
  The encoding takes years of service as already net of it. Not asserted.

## What would need doing before this is worth anything

- Deposit and encode the three awards (General Retail, Security Services, Cleaning
  Services): the scenario's k060, k061 and k087 answers live there, not in the Act.
- Supply the regulated figures: the high income threshold, any prescribed small claims
  limit, and the WA jury service pay.
- Model service by dates, including the s 22 exclusions, instead of taking years as an input.
- Encode s 72A (flexible unpaid parental leave), s 121(4), s 120 and s 122, and the s 87(3)
  shiftworker test.
- Ask the scenario authors to correct c063 (s 72) and c061 (s 83 → s 84), and to treat the
  resignation notice questions (c056, c072, d042) as matters of contract or award.
- No case law, FWC decision or Fair Work Ombudsman guidance was retrieved.
