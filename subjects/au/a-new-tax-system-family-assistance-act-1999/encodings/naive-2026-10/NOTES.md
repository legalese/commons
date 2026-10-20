# A New Tax System (Family Assistance) Act 1999 — naive encoding

**Method: naive.** Written straight from the deposited text, following the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 124, compilation date 1 July 2026, which includes amendments up to
Act No. 73, 2025 (register id C2026C00331). It is deposited at
`../../registers/source-bundle/C2004A00490.txt`.

**Checks:** one module (`fa-families.l4`) and one case file (`fa-cases-families.l4`). 50 assertions
satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This encoding answers **REQ-0004** in `subjects/au/requirements.jsonl` (priority 1). The three
Western Australian cradle-to-grave lives raised it 9 times, in these events:

- chloe c003 (2003-05-01): first vaccinations
- chloe c064, c065 (2030-10-01): Oliver's newborn payments, FTB Part A, and immunisation
- chloe c066 (2031-02-10): long day care three days a week under the Child Care Subsidy
- chloe c071 (2033-04-12): Ella born
- jake k002 (2006-10-01): the 2006 Maternity Payment
- jake k054 (2033-02-01): Ruby, whose parents are not married
- daniel d002 (1996-05-01): Family Tax Benefit at Daniel's birth
- daniel d040 (2030-02-02): Luca born, with Paid Parental Leave shared

The scope is the questions those events ask, plus the definitions and exceptions needed to answer them:

- s 6, the immunisation requirements;
- what failing them does: s 61B with Sch 1 cl 7(2), (3) for FTB, and s 85BA(1)(a)(iii) for CCS;
- ss 21, 22 and 26, eligibility for FTB;
- the Part A income test: Sch 1 cll 1(2), 3, 25, 25D, 28 and 38L-38N;
- the newborn supplement (Sch 1 cl 35A, parent route only) and the newborn upfront payment (s 58AA);
- the CCS applicable percentage, hourly rate and subsidised hours: Sch 2 cll 2, 3, 11 and 12.

Not encoded:

- FTB Part B, the maintenance income test, rent assistance, energy supplement and FTB advances;
- the multiple birth allowance and the FTB Part A supplement, beyond an input "maximum rate";
- the health check reduction (s 61A);
- shared care and percentage-of-care determinations, and blended families;
- the stillborn baby payment and the additional child care subsidy;
- the higher rate child percentage (Sch 2 cll 3A, 3B);
- Schedules 3 and 4.

## What the Act turns out to say

### 1. Parental leave pay cancels the newborn supplement, and with it the newborn upfront payment

Sch 1 cl 35A(8) says the newborn supplement clause "does not apply, and is taken never to have applied … if parental leave pay is payable to the individual for that child". Under cl 35A(9) it also does not apply if parental leave pay is payable to the individual's partner "for a flexible PPL day for that child" while the two are members of a couple.

The s 58AA upfront payment is payable only where newborn supplement "is added". So if no supplement is added, no lump sum is paid either.

This runs against the scenarios:

- c064 expects Oliver to bring "a lump sum" and a supplement "paid over 13 weeks". Yet the same chapter gives Chloe twenty-four weeks of Paid Parental Leave.
- k054 lists the Newborn payments alongside Tahlia's PPL.
- d040 has PPL shared between Daniel and Priya.

On the text, a family that takes parental leave pay for the child does not also get the newborn supplement or the upfront payment. Whether the scenarios' reserved partner weeks are "flexible PPL days" depends on the Paid Parental Leave Act 2010, which is not deposited in this row. Asserted.

### 2. Immunisation reduces FTB but removes CCS entirely

Under s 61B, a child who does not meet s 6 has their FTB child rate reduced: "reduced by $737.30 for each day" in the reduction period (Sch 1 cl 7(2) for Method 1, cl 26(3) for Method 2). The FTB itself continues, and s 61C keeps the entitlement alive even at a nil rate.

For the Child Care Subsidy the effect is different. Meeting the requirements is a condition of eligibility for each session: s 85BA(1)(a)(iii) requires that "the child meets the immunisation requirements in section 6". An unimmunised Oliver gets no CCS at all. Asserted.

### 3. Missing the grace period backdates the reduction to the notice date

The grace period runs from the date of the Secretary's notice and "ends 63 days after that day" (s 61B(4)). If the child still does not meet the requirements by then, the reduction period begins "on the day specified as the date of the notice" (s 61B(2)). It does not begin at the end of the grace period, and it runs until the child meets the requirements.

So a child immunised on day 100 costs the family 100 days of reduction, not 37. Treating day 63 itself as inside the grace period is an inference about how the days are counted. Asserted.

### 4. s 6 has no conscientious-objection ground

s 6 lists every way a child "meets the immunisation requirements":

- immunised to a determined schedule;
- a certified medical contraindication;
- certified natural immunity;
- an approved vaccine study;
- a certified temporary vaccine shortage;
- certified overseas vaccination;
- a written determination by the Secretary.

A parent's objection is not on the list, so the child of an objecting parent does not meet the requirements unless the Secretary makes a determination. The question of c003 and c065 ("What does immunisation status do?") is therefore answered by findings 2 and 3. Asserted.

### 5. The activity test now matters only above three days

Sch 2 cl 11(1A): "The 3 day guarantee for an individual for a CCS fortnight, in relation to any child, is 72". Subsidised hours are the highest of 72 and any other result. The increased hours result of 100 applies only if the individual "engages in more than 48 hours of a recognised participation type in the CCS fortnight" (cl 12).

For a couple the subsidised hours are the lower of the two partners' results (cl 11(1)(b)). If one partner does no recognised activity, the couple's hours are 72, not zero.

Oliver's three days a week (c066) is 60 hours a fortnight at 10-hour days and 72 at 12-hour days. Either way it is within the guarantee whatever the parents do. The hours per day are an assumption, because the scenario does not give them. Asserted.

### 6. Marriage plays no part

ss 21 and 22 make the FTB child test turn on four things:

- the child's age;
- care;
- residence or living with the adult;
- legal responsibility for day-to-day care, or a parenting order or plan.

Neither section asks whether the parents are married. The couple rule in s 26 (only one member of a couple is eligible) uses "member of a couple", which has "the same meaning as in the Social Security Act 1991". That Act is not deposited here. Ruby (k054) is an FTB child before her parents marry and after. Asserted.

### 7. The printed dollar figures are not the figures paid

Schedule 4 cl 2 lists as indexed every Schedule 1 and 2 amount used here:

- the FTB child rates;
- the $737.30 reduction;
- the newborn supplement and the $500 upfront payment;
- the $40,000 income free area and the $98,988 higher income free area;
- the $80,000 CCS threshold;
- the hourly rate caps.

Sch 2 cl 2(3) says the printed caps "reflect the indexation applied on 1 July 2019". Every amount is therefore an input to the encoding, and the case file uses the printed figures only as labelled examples.

Two formulas are missing from the deposit: the CCS taper between the thresholds (Sch 2 cl 3(2)) and the newborn supplement amounts (Sch 1 cl 35B(1)). In both places the text reads "using the formula:" and stops; the formulas were probably images that did not survive conversion (an inference). The CCS percentage in the taper band and the newborn supplement amount are inputs. Asserted, as structure only.

### 8. Two events cannot be answered from this compilation

- **jake k002 (2006).** It asks about "the maternity payment of the day". The 2026 compilation contains no maternity payment and no baby bonus: neither phrase occurs in the deposited text.
- **daniel d002 (1996).** It predates the Act, which is No. 80 of 1999. Under s 2 the Act commences on the last of five GST Act commencements, and those dates are not in the deposit.

Replaying either event under the current law, as the scenario notes propose, gives today's answer, not the answer of the day. Not asserted.

## What would need doing before this is worth anything

- **Source.** Retrieve the missing formulas (Sch 2 cl 3(2), Sch 1 cl 35B), and the indexed figures for each year the lives need, from the source PDF or the indexation notices.
- **Related Acts.** Read the Paid Parental Leave Act 2010 ("parental leave pay", "flexible PPL day") and the Social Security Act 1991 ("member of a couple", "Australian resident") before relying on findings 1 and 6.
- **Coverage.** Encode the rest of the newborn supplement:
  - the entrustment and adoption routes;
  - the s 58AA(1A) split under ss 28 and 29;
  - the legislative instrument under cl 35A(12).
- **Calculation.** Encode the maintenance income test, FTB Part B and the higher rate child percentage.
- **Historical versions.** Encode the compilations in force in 2003, 2006 and 2030-2033 if the lives are to be replayed as of their dates.
- **Case law.** No AAT/ART decisions or Services Australia guidance were consulted.
