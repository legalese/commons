# National Consumer Credit Protection Act 2009 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**Edition:** Compilation No. 52, compilation date 1 July 2026, includes amendments up to Act No. 57, 2026 (register id
C2026C00340), as deposited at `../../registers/source-bundle/C2009A00134.txt` (retrieved 13 October 2026). The National
Credit Code is Schedule 1 of the same text.
**Regulations used:** National Consumer Credit Protection Regulations 2010, Compilation No. 57, compilation date
5 September 2026, includes amendments F2026L01157 (register id F2026C00861), as deposited at
`../../../national-consumer-credit-protection-regulations-2010/registers/source-bundle/F2010L00631.txt` (retrieved
19 October 2026). The encoding uses regs 4D, 28HB, 28J, 28JA, 28LCA and 28LCF.
**Not deposited:** the ASIC legislative instrument under s 160F, which sets the period within which a credit card's limit
must be repayable. What the borrower could repay within that period is an input. The maximum chargeable under a single
contract under Code s 32A (needed by reg 28LCF) is an input as well.

**Checks:** one module (`nccp-borrower.l4`, 28 exported questions) and one case file (`nccp-cases-borrower.l4`).
69 assertions satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98. One assertion was
deliberately broken in a scratch copy to confirm the runner reports a failure.

This encoding replaces the first-pass encoding `naive-2026-10`. It covers everything that encoding covered and reuses its
hand-checked figures (Chloe's $6,000 card, Jake's $10,000 second card, the $2,000 loan at $400 + 12 × $80, the 6-year
s 180 window). It adds the following:

- the deposited regulations, which the naive encoding had to treat as inputs;
- s 133CC with reg 28LCA (the 10% income limit);
- reg 28LCF (split loans);
- the hardship notice (Code ss 72, 73);
- the default notice (Code ss 88, 89, 89A).

## Seat

**The borrower**: the consumer who applies for credit, the debtor under the contract, and the mortgagor of the home.
Responsible lending, the fee caps and the default rules are all written as duties on the licensee or credit provider.
Each one is encoded as what it means for the borrower:

- whether the lender had to check, and did check;
- whether the contract is one the lender must refuse;
- what the borrower may be charged, and what they do not owe;
- how long the lender has to answer a hardship notice;
- whether the lender may begin enforcement yet;
- whether a court can refuse to enforce an unlicensed lender's contract on the borrower's application.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Regulations are deposited and used. They
  set:
  - the 120-day assessment window for a home purchase (reg 28J);
  - the credit limit raised to as much as $2,480 by financed fees (reg 4D);
  - the 10% income limit (reg 28LCA);
  - the Services Australia statements (reg 28HB);
  - the credit limit inquiry (reg 28JA);
  - the split-loan circumstance (reg 28LCF).

  The ASIC s 160F instrument is not deposited, so it is an input.
- **The actors the text names.** Followed: licensee, credit provider, consumer, debtor, mortgagor, the court, ASIC.
- **A judgment handed to someone else is answered conditionally.** Followed. Each of these is an input:
  - whether inquiries were "reasonable";
  - whether inability to comply is "likely";
  - the credit provider's reasonable belief that a default cannot be remedied, or an s 88(5) ground;
  - the court's leave;
  - whether the court considers an s 180 order appropriate. The encoding answers only whether the court *can* make one.
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed. These are computed from facts:
  - credit activity (s 6 item 1);
  - small amount credit contract and short-term credit contract (s 5, reg 4D);
  - credit to which the Code applies (Code s 5, including the more-than-half rule);
  - adjusted credit amount (taken as an input amount; see finding 8);
  - permitted establishment fee and permitted monthly fee;
  - unexpired monthly fee.

  These are asked as facts: "personal, domestic or household purposes" (undefined), continuing or low cost credit
  contract (Code s 204 and Act s 5, not encoded), ADI, and "available income" (reg 28LCA defines it as income less PAYG
  withholding; the figure is the borrower's).
- **One case is the text's natural unit.** Followed: one contract, one assessment, one mortgage, one hardship notice, one
  default. Simplification: the facts at the assessment (s 131) and at entry (s 133) are taken to be the same. The worst
  repayment period stands in for every period in reg 28LCA.
- **The Act's own terms, each with a plain gloss.** Followed in the comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed. Licensing procedure, ASIC's powers, penalties and AFCA are out.

## The lives

- **chloe c043** (2024, 21): a credit card; a credit report pulled.
  - *Is my card issuer licensed?* (s 29: yes, so it may charge.)
  - *Did it assess me as it must?* (ss 128-130 with reg 28JA: yes, if it verified her income and asked what limit she
    needs. Either omission is a breach.)
  - *Is the card unsuitable for me?* (s 131(3AA): not on a $6,000 limit she could repay within the ASIC period.)
  - *How soon must I get a copy of the assessment?* (s 132: 7 business days within 2 years, 21 business days up to
    7 years, free.)
  - The credit report itself is the Privacy Act, Part IIIA.
- **chloe c052** (2028, 25): settlement, the mortgage, title registered.
  - *Does the Code cover my home loan?* (Code s 5: yes.)
  - *Is my mortgage enforceable?* (s 42: yes, signed.) *When do I get a copy?* (s 43: within 14 days.)
  - *Was an assessment 100 days old good enough?* (reg 28J: yes; the window is 120 days for a home purchase secured on
    the property.)
  - Variant, not an event of the life: *if we default and ask for hardship, may the lender enforce?* Not until 14 days
    after it refuses the hardship notice (s 89A), even though the 30-day default notice period has run.
  - Registration of the mortgage is the Transfer of Land Act 1893 (WA).
- **jake k048** (2031, 24): two credit cards.
  - *Is the second card unsuitable, and must the lender refuse it?* (ss 133(2), (3AA): yes, a $10,000 limit he could repay
    only $7,000 of in the ASIC period.)
  - *May the issuer write offering a higher limit?* (s 133BE: no.)
- **jake k049** (2032, 25): a $2,000 small amount loan at the capped charges.
  - *Is it a small amount credit contract?* (Yes.)
  - *What may it charge?* ($400 + $80 a month; $1,360 over 12 months.)
  - *Are my repayments within the limit?* (reg 28LCA: $130 a fortnight on $1,800 available income, yes; $200, no.)
  - *What don't I owe?* ($400 a month: all $5,200 of the fees.)
  - *What is the most it can recover after default?* ($4,000.)
  - *Did the lender check 90 days of statements, and Services Australia statements if I am on a payment?*
  - Variant: *may it enforce after a default?* (After the 30-day notice period, yes.)
- **jake k063** (2036, 29): a friend's debt to an unlicensed lender.
  - *Are the lender and its collector unlicensed?* (s 29: both.)
  - *May they take fees?* (s 32: no.)
  - *Can the court refuse to enforce the loan?* (s 180: on the friend's application within 6 years, yes; on Jake's
    household's, no.)

## Why this scope

The Act runs to two volumes, over a million characters as deposited. The plan entry asks for the borrower's questions in
the five events: licensing, responsible lending, the credit card limit, and the small amount caps. The brief adds hardship
variations and default notices under the Code, "as far as the events need". The cut is therefore:

- the borrower-facing duties of a credit provider under Part 3-2 (Divisions 3 and 4, s 133BE, ss 133CA and 133CC);
- the licence requirement and its civil consequence (ss 29, 32, 180);
- in the Code: coverage (s 5), the mortgage document (ss 7, 42, 43), the small amount charges (ss 23A, 31A-31C, 39B),
  hardship (ss 72, 73) and enforcement (ss 88, 89, 89A).

Credit assistance (brokers), consumer leases, reverse mortgages, standard home loans, Key Facts Sheets, disclosure,
interest, unjust transactions, postponement, repossession of goods and medium amount contracts are left out. None of the
events turns on them.

## What the Act turns out to say

1. **"$400 a month on $2,000" breaks every cap, and Jake owes none of the fees.** Code s 31A(3) caps the monthly fee at
   4% of the adjusted credit amount, which is $80 on $2,000. The establishment fee is capped at 20%, which is $400
   (s 31A(2)). Over 12 months the most is $1,360. At $400 a month the repayments (about $277 a fortnight, the encoder's
   figure) also exceed 10% of his $1,800 fortnightly available income. So s 133CC(3) applies, and Jake is "not liable (and
   is taken never to have been liable)" for any s 31A(1) fee: all $5,200. Asserted.
2. **Overcharging may forfeit the whole fee, not just the excess (a reading).** s 31A(2) defines a permitted
   establishment fee as one "the amount of which must not exceed 20%". A $500 fee is then not permitted at all, and
   s 31B(3) makes the debtor not liable for any of it. s 23A(2) points the same way ("whether or not the liability is
   imposed consistently with this Code"). The text never says "to the extent of the excess". This is the encoder's
   reading, carried over from the naive encoding. Asserted ($500 not owed).
3. **The 10% income limit is in the regulations, and breaking it costs the lender every fee.** reg 28LCA: each repayment,
   plus other small amount repayments due in the same period, must be at most 10% of available income (income less PAYG
   withholding). If not, s 133CC(3) wipes out all permitted fees: establishment, monthly, default and government. At
   exactly 10% the loan complies ("equal to or less than"). Asserted ($200 on $1,800 fails, so the $1,360 of fees is not
   owed).
4. **A home loan assessment may be 120 days old, not 90.** s 128 allows "90 days (or other period prescribed)". reg 28J
   prescribes 120 days where the credit buys residential property and is secured by a mortgage over it. Chloe and Liam's
   100-day-old assessment is good; the same age on a car loan is not. Asserted.
5. **The $2,000 small amount ceiling can be $2,480.** reg 4D raises the s 5 credit limit by the permitted establishment
   fee and the first permitted monthly fee "as included in the amount of credit". Its Note 2 gives the maximum as $2,480.
   reg 4D speaks only of the small amount definition, so the short-term credit contract ceiling stays at $2,000 (the
   encoder's reading of the reg's words). Asserted ($2,480 with fees financed is a small amount contract; $2,481 is not).
6. **What a lender must check (c043, k048, k049).** The checks are:
   - an assessment within the window, covering the credit day (s 128);
   - inquiries into requirements, objectives and financial situation, and verification (s 130);
   - since reg 28JA, inquiries about "the maximum credit limit that a consumer requires";
   - for a small amount loan, 90 days of bank statements (s 130(1A));
   - for a small amount loan, whether the borrower gets a social security payment, and if so Services Australia income
     and deduction statements issued in the last 21 days (reg 28HB).

   Asserted.
7. **s 133BE is not a limit assessment.** The ledger calls s 133BE a credit card limit assessment. In fact it forbids
   any credit limit increase invitation. The limit test is s 131(3AA)/133(3AA): a card is taken to cause substantial
   hardship if the borrower could not repay the whole limit within the ASIC period (not deposited). Jake's second card
   fails. Asserted.
8. **The adjusted credit amount where fees are financed is unclear.** Code Dictionary: "the first amount of credit that
   is, or is to be, provided". When reg 4D lets the establishment fee be included in the credit, the text does not say
   whether that fee is part of the "first amount of credit" on which the 20% and 4% are reckoned. The encoding takes the
   adjusted credit amount as an input ($2,000 for Jake). Not asserted beyond that.
9. **Splitting a loan into small ones can make each unsuitable (reg 28LCF).** The regulation's own example is $3,000 as
   two $1,500 small amount loans, with charges of $2,040 against $1,168 under a single medium amount contract. Each
   contract is unsuitable, and s 133 forbids it. Asserted.
10. **A hardship notice gets an answer in 21 or 28 days, and holds off enforcement.** Code s 72(5) table:
    - 21 days from receiving the notice, if no information is requested;
    - 28 days from the date stated in the request, if information is requested and none is given;
    - 21 days from receiving the information, if it is given.

    No answer is needed for an agreed deferral of 90 days or less (s 72(4A)). The borrower must answer a request made
    within 21 days (s 72(2), (3)). Under s 89A, after a hardship notice the lender must not enforce until 14 days after
    it gives notice that it does not agree, unless another hardship notice on the same basis was given in the previous 4
    months. No regulation under s 72(6) shortening the periods was found in the deposited Regulations (a text search, not
    a full reading). Asserted.
11. **A default notice gives at least 30 days.** Code s 88(1): no enforcement unless the borrower is in default, has been
    given a complying notice allowing "at least 30 days from the date of the notice", and has not remedied within it. On
    day 30 the lender may not yet begin. Remedying within the period reinstates the contract, unless the borrower is in
    default again at the end for the same type of breach (s 89). Asserted.
12. **An unlicensed lender's loan is not void by force of the Act.** s 29 forbids the lending, and s 32 forbids any fee.
    But only a court may declare the contract void or refuse to enforce it (s 180), and only on the application of the
    person dealt with (or ASIC with their written consent), within 6 years. The collector "exercises the rights of a
    credit provider ... on behalf of the credit provider" (s 6 item 1(c)), so he contravenes s 29 too. Jake's household is
    not the plaintiff. Asserted.
13. **The Code covers a home loan only if more than half is for personal, domestic or household use.** Exactly half is
    not "predominantly" (Code s 5(4)). Reading the purchase of one's own home as "personal, domestic or household" is the
    encoder's inference, because the phrase is undefined. Asserted.

## What would need doing before this is worth anything

- The ASIC instrument under s 160F should be deposited, so the credit card test can compute the repayment rather than
  ask for it.
- Code s 32A (medium amount credit contracts) should be encoded, so reg 28LCF can compute its comparison.
- The readings in findings 2, 5 and 8 need case law or ASIC guidance (RG 209 was not consulted).
- reg 28LCA should be applied to every repayment period, not the worst one given.
- The s 131 and s 133 facts should be separated (assessment time and entry time).
- Encoded but not asserted: s 73 (30 days for the written notice of change), the s 72(5) "from" day for items 1 and 2,
  the non-remediable default and s 88(5) paths, and s 31C only once.
- Default fees and government charges (s 31A(1)(c), (d)) and the s 39B cap's interaction with them are not modelled.
- Postponement (s 94), court changes (s 74), unjust transactions (ss 76-77) and the Code s 6 exclusions are not encoded.
- No decided cases were searched.
