# Moneylenders Act 2008 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 32 of
2024).

**Checks:** two case files, 112 assertions satisfied (64 in ml-cases-borrowers.l4, 48 in
ml-rules-interest-and-fees-cases.l4), 0 errors, 0 warnings.

## Why this Act, and why scoped

**18 of the 527 Singapore Acts** deposited here cite it. This row takes the borrower's
position -- what a loan from an unlicensed or over-charging lender is worth -- and
the loan-shark offences. Licensing, the credit bureau and the business-conduct
duties are not encoded. **The Moneylenders Rules (the interest cap and permitted
fees) were not retrieved.**

## What the Act turns out to say

### 1. A borrower from a loan shark owes nothing the law will enforce -- including the principal

s 19(3): a loan from an unlicensed moneylender, and any guarantee or security, "is
unenforceable", and "any money paid by or on behalf of the unlicensed moneylender ...
is not recoverable in any court of law". Not just the interest: the principal too.
Asserted.

### 2. A licensed lender a fraction over the cap loses the whole loan

s 36(3): a licensee whose contract exceeds the prescribed maximum interest rate cannot
enforce the contract or any security, and "any money paid by or on behalf of the
licensee under the contract is not recoverable". One basis point over the cap and the
principal is lost. Asserted with a stand-in cap.

### 3. A friend who charges interest is presumed a moneylender

s 3: "Any person ... who lends a sum of money in consideration of a larger sum being
repaid is presumed, until the contrary is proved, to be a moneylender." Combined with
s 2, an unlicensed one -- and s 19(3) makes the loan irrecoverable. The friend must
prove they do not carry on a business of moneylending. Asserted.

### 4. The harassment offence reaches only loan sharks

s 47 applies where "an **unlicensed** moneylender", or someone acting for one,
harasses a borrower, surety, family member "or any other person". A licensed lender who
harasses is outside it. Where property is damaged (paint, "coffee, soya sauce", posters,
fire -- s 47(7)) or hurt is caused, caning is **mandatory**: 3 to 6 strokes for damage, 5
to 8 for hurt, 6 to 12 for both on a first offence; 5 to 10, 6 to 12 and 9 to 18 on a
repeat. Asserted.

### 5. Reopening needs both excess and unfairness

s 37(1): the court "is to reopen" a licensee's loan only if the interest is excessive
**and** the transaction is unconscionable or substantially unfair. A borrower may apply
before repayment is due and despite any contrary term (s 37(4)). Asserted.

### 6. Smaller things worth recording

- **s 19(5):** "assisting" includes collecting repayments and letting one's bank
  account be used, if one knew or had reasonable grounds to believe.
- **s 35(3):** a charge beyond the permitted fees is irrecoverable, refundable, or set
  off against the loan.
- **s 49:** an adult who procures a child under 16 to commit a loan-shark offence faces
  up to 7 years (or 2 to 9) and caning.

## What would need doing before this is worth anything

- **Retrieve the Moneylenders Rules** for the actual caps and permitted fees.
- **No case law was searched.** Whether a one-off lender "carries on business" under s 3
  is a recurrent question.
- Harassment by a licensed lender is governed elsewhere (the Protection from Harassment
  Act row, and the Rules); not followed here.

## Interest caps and permitted fees (added 12 October 2026 for REQ-0277)

Module `ml-rules-interest-and-fees.l4`, cases `ml-rules-interest-and-fees-cases.l4` (48 assertions). Source: the
Moneylenders Rules 2009 (S 72/2009), version in force from 1 August 2026, deposited at
`../../registers/source-bundle/MA2008-R1.txt`. Rule numbers were taken from the body.

The question: a licensed moneylender lends $8,000 to a borrower earning $36,000 a year in August 2032 -- the highest
monthly interest, and what fees.

1. **The answer: 4% a month, $320 in the first month.** Rule 11(1) fixes the s 36(1) maximum at "the nominal interest
   rate of 4% per month", and rule 11(2) runs it on the outstanding principal after payments appropriated to principal,
   so the cap in money falls as the loan is repaid ($280 once $1,000 of principal is repaid). Late interest is capped
   separately at 4% a month (rule 11(3)), and only on an amount that has fallen due and is unpaid (rule 11(4), (5)).
   Asserted.
2. **Fees: three kinds and no others.** Rule 12(1): a grant fee of at most 10% of the principal ($800 here); late-payment
   fees "not exceeding an aggregate of $60 per month"; and legal costs of recovery as ordered by a court. Each only if the
   borrower agreed. The ledger's "administrative fee as prescribed" does not match the text: there is no administrative
   or processing fee in the list, and s 35(3) makes any such charge irrecoverable (refundable if paid). Asserted.
3. **Interest, late interest and the two fees together cannot exceed the principal** -- $8,000 here (rule 12A(b)). Court
   costs are outside that aggregate. For a revolving credit loan granted on or after 30 November 2018 the ceiling is the
   amount drawn and unrepaid instead (rule 12A(a)); not encoded beyond this note. Asserted.
4. **The borrower's income matters for how much can be lent, not for the rate.** Rule 21(2): to a borrower earning at
   least $20,000 a year, a licensee's unsecured loans in total may not exceed 6 months' income -- $18,000 on $36,000 a
   year -- so $8,000 is allowed if the borrower owes no more than $10,000 on other unsecured licensee loans. The encoding
   ASSUMES a Singapore borrower and no other unsecured loans; neither is in the question. "Annual income" is the last
   3 months' income times 4 (rule 21(6)), not a declared salary. Asserted.
5. **Business loans are different.** Rule 12B disapplies the 4% caps and the rule 12A ceiling for a business loan (a loan
   to a company, LLP or registered business trading at least a year, rule 1A). Its permitted fees are a different list
   (rule 12(2)) -- with no grant fee and no $60 limit on late fees. Asserted.
6. **The 2032 date cannot be answered from the deposit.** The Rules deposited are the version in force from 1 August
   2026; its legislative history ends with the Moneylenders (Amendment) Rules 2026 (S 543/2026). The encoding
   answers on that text; whether the 4% cap and the fee list still stand in 2032 is not known.
7. **Not checked:** case law on rule 12A and s 36(3); guidance from the Registrar of Moneylenders; the s 66(5)(b) credit report
   that supplies the outstanding unsecured loan amount.
