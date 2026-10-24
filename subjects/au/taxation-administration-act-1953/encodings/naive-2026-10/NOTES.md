# Taxation Administration Act 1953 (Cth) — naive encoding

**Method: naive.** Written straight from the deposited text, following the
conventions of the finished naive encodings (the `writing-l4-rules` skill was not
available in this session). No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 226, compilation date 27 August 2026 (includes
amendments up to Act No. 79, 2026 and Act No. 82, 2026), register id C2026C00393,
deposited at `../../registers/source-bundle/C1953A00001.txt` (all four volumes in
one file).

**Checks:** one module (`taa-tfn-payg.l4`) and one case file
(`taa-cases-tfn-payg.l4`): 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This encoding answers **REQ-0015** in `subjects/au/requirements.jsonl` (priority 1). The three
Western Australian cradle-to-grave lives raise it 5 times:

- Chloe **c020** (2018-03-14): turns 15, a tax file number and a casual job at a supermarket. "Must a 15-year-old have a TFN? What is a junior rate? Is super payable?"
- Chloe **c041** (2024-02-29): first payslip, $5,833.33 for the month. "What is withheld?"
- Jake **k020** (2021-08-30): turns 15, a tax file number and no job yet.
- Jake **k043** (2028-10-20): first tax return as a sole trader on $31,000. PAYG instalments.
- Daniel **d012** (2012-10-15): turns 16, a tax file number and a casual job.

The scope is the provisions those events name, plus the definitions, conditions and
exceptions needed to answer them. For TFNs that is s 2 (the definition), s 8C(2) and
ss 8WA and 8WB. For PAYG withholding (Schedule 1 Part 2-5) it is which payments must
have an amount withheld (ss 12-1, 12-10, 12-35, 12-40, 12-190), when (s 16-5), how much
(ss 15-10, 15-15), the penalty for not withholding (s 16-30), when the payer must pay
the Commissioner (ss 16-75, 16-95, 16-100, 16-105) and the employee's credit (s 18-15).
For PAYG instalments (Schedule 1 Part 2-10, Division 45) it is who is liable
(ss 45-15, 45-50), what kind of payer an individual is (ss 45-125 to 45-134, 45-140,
45-155), when instalments are due (ss 45-60, 45-61, 45-70), the applicable rate and the
instalment on instalment income (ss 45-1, 45-110), notifying instalment income (s 45-20)
and the credit (s 45-30).

Not encoded: junior rates (Fair Work Act 2009 and the award) and superannuation
(Superannuation Guarantee (Administration) Act 1992), which are not in this Act; the
Income Tax Assessment Act 1936 Part VA (not deposited); the amounts in the withholding
schedules and regulations (inputs); the value of a penalty unit (an input); the large
withholder's weekday table and the Commissioner's withholder-status determinations;
s 8WC; notional tax, the instalment rate formula, GDP adjustment, benchmark tax and
varying the rate; monthly payers beyond an input flag; and companies, trusts,
partnerships and consolidated groups.

The scenarios give no amount withheld, no employer size, no notional tax and no date
on which the Commissioner gives Jake a rate. The case file uses figures chosen by the
encoder and labels them as hypothetical: a schedule amount of $1,000, notional tax of
$2,500, an 8% rate, instalment income of $7,750 (a quarter of $31,000) and a rate given
on 15 November 2028. Daniel's event is in 2012, and the text encoded is the 2026
compilation, not the law as it stood then.

## What the Act turns out to say

### 1. There is no Part VA in this Act; the TFN regime is in the 1936 Act

The ledger, and c020, k020 and d012, cite "Part VA (tax file numbers)" of the Taxation
Administration Act. The deposited compilation has no Part VA. Its Parts run I, IA, II,
IIA, IIB, III, IIIA, IVA, IVC, IVD and V. Section 2 defines a tax file number as "a tax
file number as defined in section 202A of the Income Tax Assessment Act 1936", and
s 8WC refers to "Part VA of the Income Tax Assessment Act 1936". Issuing TFNs and TFN
declarations are in that Act, which is not deposited here. This Act holds only the TFN
offences (Part III, Division 2, Subdivision BA) and s 8C(2). Not asserted (a finding
about the citation).

### 2. Nothing here makes a 15-year-old get or quote a TFN; not quoting one is not an offence

No provision of this Act obliges an individual of any age to obtain or quote a TFN.
Section 8C(2) says a person is not to be taken to have failed to give information
"merely because the person has refused or failed to quote the person's tax file number".
The cost of not quoting is in the withholding schedules: a TFN declaration "may affect
how to calculate the amount to withhold" (s 15-1). Section 8WA makes it an offence
(100 penalty units or 2 years) to "require or request" a TFN, unless a taxation law
provides for it to be quoted, the request is part of complying with a taxation law, the
requester acts on the person's behalf, or it is for an ABN application. The case file
treats the supermarket's request for a TFN declaration as one a taxation law provides
for. That is an **inference**: the provision that does so is in the 1936 Act, which was
not read. A video store asking for a TFN as identification commits the offence.
Section 8WB makes recording, using or passing on a TFN an offence unless a taxation law
requires or permits it. Asserted.

### 3. Chloe's and Daniel's wages must have tax withheld whatever their age, and whether or not they quoted a TFN

Section 12-35 requires withholding from "salary, wages, commission, bonuses or allowances"
paid "to an individual as an employee". It asks neither the employee's age nor whether a
TFN was quoted. The only exceptions modelled are a wholly exempt payment (s 12-1(1)), a
payment that is neither assessable nor exempt income (s 12-1(1A)), and a non-cash benefit
(s 12-10). How much is withheld is "worked out under the withholding schedules made under
section 15-25", or under regulations if they prescribe it (s 15-10). It is an input, and
the Act states no amount. The schedules must have regard to the HELP repayment amounts
(s 15-30(c)(ii)), so the HECS component on Chloe's c041 payslip comes from the schedule,
not from this Act. Asserted.

### 4. Jake owes no instalments until the Commissioner gives him a rate

"You are liable to pay instalments under this Division if the Commissioner has given you an
instalment rate" (s 45-15(2)), and only while it has not been withdrawn (s 45-50(4)).
Business income alone does not create the liability. Once a rate is given, an individual
is by default a quarterly payer on GDP-adjusted notional tax (s 45-130(1)(a)), paying
four instalments (s 45-132), or two if a primary producer or special professional
(s 45-134). No instalment is due for a quarter that ended before the rate was given:
the starting instalment quarter is the one in which the rate is first given, "even if it
is not the first instalment quarter" (s 45-125(2)(a)). On the encoder's assumed date
(15 November 2028), Jake's first instalment is for the October–December 2028 quarter, due
21 January 2029, or 28 February 2029 if he is a deferred BAS payer (s 45-61). Because he
is not registered for GST, he may instead choose to pay annually if his notified notional
tax is "less than $8,000" (s 45-140(1)). The annual instalment is then due on 21 October
after the year ends (s 45-70(2)). Chloe, on wages alone, is never liable: Note 2 to
s 45-15 says the Commissioner will not give a rate to someone whose income "has always
consisted wholly of withholding payments". Asserted.

### 5. The instalment formulas did not survive into the deposit

Section 45-110(1) says to work out a quarterly instalment "as follows". Section
45-115(1)(a) gives "the amount worked out using the formula:", and s 45-320(1) works out
the instalment rate "using the formula:". In each case the text goes straight on to the
next subsection. The instalment on instalment income is encoded from the Guide instead.
Section 45-1 says "multiplying your instalment income for an instalment quarter by the
rate the Commissioner gave you, or by a rate you choose yourself". This is labelled an
inference. The instalment rate and notional tax are inputs. Asserted (the inferred
product).

*Checked 24 October 2026.* The formulas are now transcribed in
`../../registers/source-bundle/C1953A00001.formulas.md`. Section 45-110(1) reads
"Applicable instalment rate × Your instalment income for that quarter", so the inferred
product is the formula, and the asserted 620 on 7,750 at 8% stands. This encoding has no
function taking an amount that the other recovered formulas give: the GDP-adjusted
instalment was a comment, not an input. The baseline (`../baseline-2026-10/`,
`taa-instalments-formulas.l4`) now computes the GDP adjustment, the s 45-400 instalment,
the s 45-230 charge base and the shortfall interest charge. Nothing here changed; 52 of
52 assertions are still satisfied.

### 6. A business paying a sole trader withholds only if no ABN is quoted

Under s 12-190, a payer must withhold from a payment for a supply made in the course of
the supplier's enterprise unless the supplier's ABN is quoted on an invoice or other
document. There are other exceptions. The payer need not withhold if the payment is not
made in the course of the payer's own enterprise. Nor if it "does not exceed $50 or such
higher amount as is specified in regulations". Nor if an individual has given a written
statement that the supply is a hobby or private, unless the payer has grounds to doubt
it. So Jake's clients withhold nothing from his delivery fees once his ABN is on the
invoice. Asserted.

### 7. When the employer pays over what it withheld depends on its size, which is in the Act

A medium withholder is one whose amounts withheld in an earlier financial year "exceeded
$25,000" (s 16-100). It pays by the 21st of the next month (s 16-75(2)). A small
withholder pays by the 21st of the month after the quarter ends (s 16-75(3)). Deferred
BAS payers get the 28th instead (s 16-75(2A), (4)). For Chloe's February 2024 pay, that is
21 March 2024 if her employer is medium-sized and 21 April 2024 if it is small. Exactly
$25,000 does not make an employer medium. She gets a credit for the total withheld when
her return is assessed (s 18-15). Asserted.

## What would need doing before this is worth anything

- The ledger's "Part VA" points at the Income Tax Assessment Act 1936, which has to be
  deposited and encoded (TFN issue, TFN declarations, s 202CB) before c020, k020 and d012
  are fully answered.
- The formulas in ss 45-110, 45-115 and 45-320 have to be recovered from the authorised
  compilation. They were lost when the deposit was converted to text. (Done: see the
  sidecar, and the baseline that uses it.)
- The withholding schedules and the Taxation Administration Regulations (the no-TFN rate,
  the no-ABN rate, any higher $50 threshold) were not retrieved.
- d012 needs the compilation in force in October 2012.
- No ATO ruling, guidance or case law was read.
