# Loans (International Banks) Act 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/LIBA1958.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31 December
2021. The only amendment annotated in the body is [11/91] on s 7(1); the legislative
history ends with Act 11 of 1991 (commencement 30 November 1991). The arrangement of
sections at the top of the deposit is out of step by one (a blank "1.", then "Short
title" as 2); the body's numbering, s 1 to s 12, is followed.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0182** in `subjects/sg/requirements.jsonl`: tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The short answer is: almost nothing directly. The Act is about the Government and
statutory authorities borrowing from the IBRD and the Asian Development Bank. A private
person or business meets it as a lender, creditor or bondholder of a statutory
authority, as a party to a transaction a tax remission order touches, or as a payer
outside the Exchange Control Act.

The Act is short, so nearly all of it is encoded: ss 2, 3(2), 5(1), (2), (4), 6, 7(1),
8, 9(1)-(2), 10, 11 and 12(2)-(4). Not encoded: who signs agreements and instruments
for the Government (ss 3(3), 4, 7(2)), presenting agreements to Parliament (s 3(4),
7(3)), the savings for other powers (ss 3(5), 5(3), 9(3)), bond issues (s 5(5)), and
s 12(1) beyond what s 12(2) and (3) make of it. Article 144 of the Constitution and the
Development Fund Act 1959 are referred to but were not read.

## What the Act turns out to say

### 1. A negative pledge binds every statutory authority, not only borrowers

s 12(3): neither the Government, any agency of it, "any statutory authority" nor any
central bank may create a lien on its assets as security for an external debt unless
the lien also secures the Bank's loans "equally and rateably", except as agreed between
the Minister and the Bank. The text does not confine this to a statutory authority that
has itself borrowed from the Bank. "External debt" is a debt payable in anything other
than Singapore legal tender, including at the creditor's option (s 12(4)); "lien"
includes mortgages, pledges, charges, privileges and priorities. A lender taking
security for a foreign-currency loan to a statutory board meets this. A private company
is not bound. Asserted.

### 2. A guaranteed authority loses its other borrowing powers

s 8: while the Government is liable under a s 7 guarantee, the statutory authority
"shall not except with the consent of the Minister exercise any other power to borrow
possessed by it". Whether a further Bank loan under s 5 is an "other power" is not
settled by the text (s 5 needs the Minister's prior written approval anyway). Asserted
for borrowing under any other power.

### 3. Leftover loan money needs both the Minister and the Bank

ss 3(2), 6: loan money goes to the purposes in the agreement; only a part that "cannot
be applied" to them may go elsewhere, and then only to purposes "approved by the
Minister and the Bank". Either approval alone is not enough. Asserted.

### 4. The Arbitration Act binds the Government, but only in disputes with the Bank

s 11: a dispute between the Bank and the Government or a statutory authority under an
agreement, guarantee or instrument goes to arbitration as agreed, the award is
enforceable as if made under the Arbitration Act 2001, and that Act "shall be binding
on the Government". A dispute between a bondholder and the authority is outside s 11.
Asserted.

### 5. Only income tax and stamp duty can be remitted, and only by Gazette order

s 12(2)(a): the Minister may remit tax under the Income Tax Act 1947 or the Stamp
Duties Act 1929 "by order published in the Gazette" where necessary to give effect to
the agreement. No other tax is named. s 12(2)(b) takes payments under the agreements
outside the Exchange Control Act 1953. Asserted.

### 6. "The Bank" is two banks only

s 2: the IBRD or the Asian Development Bank. The Asian Infrastructure Investment Bank
and the International Development Association are not within the definition. Asserted.

### 7. Repaying the Consolidated Fund, at the loan rate

s 10(1): money paid out under a guarantee is repaid by the authority with interest "at
the same rate as that payable on the loan", as the Minister directs. s 10(2): the
Minister reports to Parliament after every financial year from the year of payment to
the year of final discharge, both counted (2024 to 2028 is five statements). How the
interest runs is not stated and is not encoded. Asserted.

## What would need doing before this is worth anything

- Article 144 of the Constitution (the President's concurrence) and the Development
  Fund Act 1959 were not read.
- Whether a Companies Act company is "incorporated directly by any written law" is an
  inference (encoded: no).
- No Gazette orders under s 12(2)(a), loan agreements or case law were searched.
