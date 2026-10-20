# National Consumer Credit Protection Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive encodings (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** Compilation No. 52, compilation date 1 July 2026 (includes amendments up
to Act No. 57, 2026), register id C2026C00340, as deposited at
`../../registers/source-bundle/C2009A00134.txt`.

**Checks:** one module (`nccp-credit.l4`), one case file (`nccp-cases-credit.l4`),
53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This encoding answers **REQ-0017** in `subjects/au/requirements.jsonl` (priority 1). The three
Western Australian cradle-to-grave lives raise it 5 times:

- Chloe **c043** (2024-06-10): a credit card at 21. What must a lender assess?
- Chloe **c052** (2028-05-15): settlement, and the mortgage under the National Credit Code.
- Jake **k048** (2031-03-02): two credit cards at 24 (ss 128-133, 133BE).
- Jake **k049** (2032-08-20): a $2,000 small-amount loan. What is the most a payday lender
  may charge, and what happens if it charges more?
- Jake **k063** (2036-08-22): a friend's debt to an unlicensed lender. Is the loan
  enforceable (s 29)?

The compilation runs to two volumes (over a million characters as deposited), so this encoding takes only
those questions, plus the definitions and exceptions they need:

- the licence requirement and its consequences: ss 6 item 1, 29, 32, 180;
- responsible lending: ss 128-133, with ss 133BA(1) and 160F;
- credit limit increase invitations: s 133BE;
- the small amount and short-term credit contract definitions (s 5) and s 133CA;
- in the National Credit Code: ss 4, 5, 7, 23A, 31A, 31B, 31C, 39B, 42 and 43.

Not encoded: licensing procedure, credit assistance, standard home loans, Key Facts
Sheets, comprehensive credit reporting, hardship, enforcement, disclosure and interest
under the Code, and the Code's s 6 exclusions. The ledger asks "what may a credit
reporting body hold?". That is Privacy Act Part IIIA, which has its own encoding.

## What the Act turns out to say

### 1. The "$400 a month on $2,000" in Jake's life is five times the monthly cap, and the debtor owes none of it

Code s 31A(3) caps a small amount credit contract's monthly fee at **4% of the adjusted
credit amount**. The adjusted credit amount is "the first amount of credit". On $2,000
that is **$80**. The establishment fee is capped at 20% (s 31A(2)), which is **$400**, once.
For a 12-month loan, the most the permitted fees can come to is $400 + 12 × $80 = **$1,360**.
SCENARIO.md's question list gives the lender's demand as "$400 a month on $2,000". That
breaches s 31A. Under s 31B(3) the debtor "is not liable (and is taken never to have been
liable)" and may recover what was paid. s 31B(1) carries 100 penalty units. Asserted.

### 2. Overcharging may forfeit the whole fee, not just the excess (a reading)

s 31A(2) defines a permitted establishment fee as one "the amount of which must not exceed
20%". On a naive reading, a $500 establishment fee on $2,000 is not a permitted fee at all.
s 31B(3) then makes the debtor not liable for any of the $500, not only the $100 excess.
s 23A(2) points the same way: the provisions imposing a prohibited liability are void
"whether or not the liability is imposed consistently with this Code". The text never says
"to the extent of the excess". This is the encoder's reading, and it is labelled in the
module. Asserted ($500 not owed; $400 not owed where $400 a month is charged).

### 3. An unlicensed lender's loan is not void by force of the Act. A court may refuse to enforce it, and only on the borrower's application

s 29 forbids unlicensed credit activity: 5,000 penalty units civil, 2 years criminal. s 32
forbids the unlicensed lender to take any fee from the consumer. But nothing in the deposit
makes the contract void or unenforceable of itself. s 180 lets a court declare it void, refuse
to enforce it, or order refunds. The application must come from "the plaintiff", meaning the
person the credit activity was engaged in relation to, or from ASIC with that person's
written consent. It must be made within 6 years.

For k063 the borrower is Jake's friend. Jake's household is not the plaintiff, so s 180
gives it nothing. Its remedies lie in the WA Criminal Code and the Restraining Orders Act,
which the scenario already names. The man collecting for the lender also engages in a
credit activity: s 6 item 1(c) covers anyone who "exercises the rights of a credit provider
... on behalf of the credit provider". So he contravenes s 29 too, unless he acts for a
*licensed* principal (s 29(3)). Asserted.

### 4. s 133BE is not "credit card limit assessment"

The ledger and k048 describe s 133BE as "credit card limit assessment". In fact it
**forbids** a credit card provider to make a "credit limit increase invitation", meaning any
communication that offers an increase, invites an application for one, or is meant to
encourage one. The limit test the lives are after is in s 131(3AA) and s 133(3AA). For a
credit card contract, the consumer is taken to be able to comply only with substantial
hardship if they could not repay **an amount equal to the credit limit** within the period
ASIC fixes under s 160F. That period is in a legislative instrument that is not deposited,
so it is an input. Jake's second card (a $10,000 limit, $7,000 repayable in the period:
the encoder's figures) is unsuitable, and s 133 forbids it. Asserted.

### 5. What a lender must assess (c043, k048)

Under s 128, the licensee needs an assessment made within **90 days** (or a prescribed
period) before the credit day, covering that day. It must also have made the s 130
inquiries into requirements, objectives and financial situation, and taken reasonable
steps to verify the financial situation. For a small amount credit contract it must
consider **at least 90 days** of the income account's transactions (s 130(1A)).

A contract is unsuitable if the consumer is likely to be unable to comply, or could comply
only with substantial hardship, or if it does not meet their requirements or objectives
(ss 131(2), 133(2)). Having to sell the home is presumed substantial hardship "unless the
contrary is proved" (s 131(3)). The consumer may ask for a copy of the assessment for 7
years. It is due within 7 business days if asked within 2 years of the credit day, and
within 21 business days after that. It is free (s 132). Asserted.

### 6. Jake's $2,000 loan sits exactly at the line

A small amount credit contract has a credit limit of "$2,000 ... or less", a term of 16
days to 1 year, is unsecured, and is not from an ADI (s 5). $2,000 qualifies and $2,001 does
not. A loan for 15 days or less is a *short-term* credit contract, which a licensee must not
enter at all (s 133CA). Interest is forbidden outright (Code s 23A(1)(a)). After a default,
the lender may recover no more than **twice** the adjusted credit amount, $4,000, plus
enforcement expenses (s 39B). Asserted.

### 7. The home loan and the mortgage (c052)

The Code applies to credit to a natural person used "wholly or predominantly", meaning more
than half, for personal, domestic or household purposes, or for residential investment
property, where a charge is made and the lender is in business (Code s 5). Reading a loan
to buy the home they will live in as "personal, domestic or household" is the encoder's
inference: the Act does not define the phrase. Exactly half is not predominant.

The mortgage must be a written document signed by the mortgagor, or be contained in a
signed credit contract. Otherwise it "is not enforceable" (Code s 42). A separate mortgage
document must be copied to the mortgagor within 14 days (s 43). What the lender registers on
the title is a question for the Transfer of Land Act 1893 (WA), not this Act. Asserted.

## What would need doing before this is worth anything

- The National Consumer Credit Protection Regulations 2010, and the ASIC instruments
  under s 160F, were not retrieved. Every prescribed period, inquiry, circumstance and
  ceiling is an input.
- The reading in finding 2 (whole fee or excess) needs case law or ASIC guidance.
- s 31C (unexpired monthly fees) is encoded but not asserted. Monthly fees for a part
  month, default fees under s 31A(1)(c), and the s 39B cap's interaction with them are
  not modelled.
- s 180 is encoded only as whether the court *may* make an order. Which order it makes is
  discretionary.
- The facts at assessment and at entry are taken to be the same (s 131 versus s 133).
- No decided cases were searched.
