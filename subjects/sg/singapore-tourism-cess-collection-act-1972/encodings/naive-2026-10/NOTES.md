# Singapore Tourism (Cess Collection) Act 1972 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/STCCA1972.txt`. The deposit's cover says "version in force from 1/4/2022", and the
revised edition incorporates amendments up to 1 December 2021. The latest amendment annotated in the body
is Act 25 of 2021 (s 14(1), with effect from 1 April 2022).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is **REQ-0149** in `subjects/sg/requirements.jsonl`. It sits in tier 2 of the remaining Singapore Acts,
which are ordered by how often they touch everyday life. The requirement asks what the Act decides for a person or
business it applies to. No scenario has asked a sharper question yet.

This row covers when a transaction bears cess and how the cess is measured (ss 2, 2A, 5, 6(1)). It also covers
what a liable business must keep and report (ss 9, 10), the Board's estimate (s 12), the late-payment penalty
(s 13), refunds and clawback (ss 15, 16), remission (s 20(2), (3)), the offences (ss 17 to 19, 25) and insolvency
priority (s 24).

Not encoded: delegation (s 3), the Fund (s 4), entry and inspection (s 8), the receipt-machine dispensation and
directions (s 9(2) to (4)), suit on a certificate (s 14), exemption by order (s 20(1)), prosecution procedure
(ss 22, 23) and regulations (s 26).

## What the Act turns out to say

### 1. The Act fixes no rate, no event and no payer

s 5(1) makes cess payable "at the amount prescribed by the Minister by order in the Gazette". s 5(4) leaves the
following to that order: the tourism event, the taxable transactions, the tourism event establishments (the
payers), the taxable period and the amount. A "tourism event establishment" is simply "a person prescribed in an
order made under section 5" (s 2). So from the Act alone you cannot tell whether any business owes cess today. No
order was retrieved. The encoding takes the rate as a parameter and measures it on gross receipts net of GST
(s 5(5), (7)). Asserted.

### 2. Cess is owed even when the customer is local, the booking is unrelated to the event, or nothing is used

Under s 5(3), a transaction does not stop being taxable "by reason only that" any of these is true:
- the customer "is not a visitor to Singapore";
- it is made "for any purpose other than for purposes of any tourism event";
- it "is terminated";
- the thing bought "is not provided or used".

The taxable period "may include any time before or after the event" (s 5(2)(a)). Under s 5(8), closing the business
mid-period does not end the liability. The only exits are these: the transaction was not made in the course of a
business in Singapore, its use falls outside the period, the order does not prescribe it, or the provider is the
Government or a public-purpose statutory body (s 2A). Asserted.

### 3. The additional penalty is backdated to the date the cess fell due

s 13(1)(a) adds a 5% penalty when cess is paid late. If the cess is still unpaid 60 days after that penalty is
imposed, s 13(1)(b) adds 2% "for each completed month that the cess remains unpaid commencing from the date on which
the cess became payable", not from day 60. The total additional penalty is capped at 50% of the cess, so the most a
business can owe in penalties is 55% of the cess. Paying on day 60 costs 5%. Paying on day 61 after four completed
months costs 13%. Asserted.

The section's trigger is the time "prescribed by the Board", while s 6(2) says the time is prescribed "by
regulations". The encoding takes "paid in time" as an input and does not resolve that difference.

### 4. Evasion carries a minimum prison term but no maximum

s 18(1) punishes evasion with "a fine not exceeding $5,000 or ... imprisonment for a term of not less than 6
months or ... both". The text sets a floor on imprisonment and states no ceiling. Every other offence in the Act
carries only a fine of up to $5,000. Prison is mentioned elsewhere only for an incorrect return (s 17), and there
only "in default of payment" of the fine, for up to 6 months. Under s 18(2), a proved false statement or entry
raises a presumption of intent to evade "until the contrary is proved". An incorrect return under s 17 requires no
intent at all. Asserted.

### 5. Refund and clawback have the same one-year window

Under s 15, a refund of overpaid cess may be made "only if" all three conditions hold:
- the claim is made within one year;
- it is in the Board's form;
- the Board is satisfied there was an overpayment.

Under s 16(2), underpaid cess, or a refund that should not have been made, is payable on a demand the Board makes
within one year. Asserted. The Board's estimate under s 12 is recoverable unless the person proves a lower figure
(s 12(3)). It must be paid within 7 days of the notice (s 12(4)). Asserted.

### 6. Record retention depends on when the record was provided as well as made

Under s 9(5), records provided or made before 6 September 2018 must be kept for 2 years. Records made on or after
that date must be kept for 5 years. So must any record "provided (whenever made)" on or after it. An old record
handed to the Board after that date therefore takes the 5-year period. Asserted. Cess that fell due within 12
months before a bankruptcy order or winding up is paid in priority (s 24). Asserted. Treating exactly 12 months as
"within" is the encoding's choice.

## What would need doing before this is worth anything

- Retrieve the Minister's orders under s 5 and the regulations under s 26. Without them the Act names no payer, rate
  or deadline.
- Part payments under s 13 (the "cess outstanding" base) and the Board's power to remit the penalty (s 13(3)) are
  not modelled.
- Whether s 18's open-ended imprisonment is read subject to a general ceiling elsewhere in Singapore law was not
  researched.
- No case law was searched.
