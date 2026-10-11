# Fees Act 1920 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/4/2024"), as deposited at `../../registers/source-bundle/FeA1920.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021". The latest
amendment annotated is "[Act 4 of 2008 wef 01/04/2024]", against ss 2, 3, 5, 8, 9 and
10. The deposit's metadata records it as the current version as at 1 October 2026.

**Checks:** one case file, 43 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0151** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet.

The Act is ten sections long, so this row takes the whole operative text, ss 2 to 10.
It does not encode s 1 (short title), and it holds no fee amounts at all: the amounts
are in Ministerial orders under s 2, and none was retrieved.

## What the Act turns out to say

### 1. The Minister can remit fees that another Act fixes, even though this Act cannot change them

s 8 says nothing in the Act affects the amount of a fee when another written law makes
"express provision" for that amount. But s 9(1) opens "Notwithstanding section 8" and
lets the Minister for Finance remit "wholly or in part" any fee, charge, penalty or
interest "prescribed under this Act or under any other written law". So a s 2 order
cannot change a fee another Act fixes, but the Minister can still waive it. A delegate
named in a s 2 order (s 9(2)) has no such reach. Asserted.

### 2. The Act fixes no fees; it is the power to fix them

s 2 lets the Minister prescribe by order fees and payments "for licences, permits and
otherwise", late-payment charges and penalties, and interest on outstanding amounts or
instalments, but only in "the subordinate courts ... and in all public offices and
departments". An order "shall ... have effect from the date of the publication" in the
Gazette (s 3). The text does not make effect wait for the order to be presented to
Parliament. Asserted.

### 3. Unpaid government fees are recovered like fines, on the officer's certificate

s 5(1): fees, charges, penalties and interest prescribed under a s 2 order are
recoverable "when not otherwise provided for" by summary procedure before a
Magistrate's Court, in the way fines are recovered, on the complaint of the officer who
should have been paid. Under s 5(2) the officer's certificate of non-payment is "prima
facie proof". This route covers only levies prescribed in a s 2 order, not a fee whose
amount another Act fixes. Asserted. (*Inference*: "prima facie" means the proof stands
unless contrary evidence displaces it. The model treats it that way and says so.)

### 4. No payment, no service, but only if the officer chooses

s 4: an officer "may decline" to do a chargeable thing "until the fee is paid or the
payment is made". This is a discretion, not a duty to refuse. It covers the fee for the
thing itself. The text says nothing about refusing to act because a late charge or
interest is still unpaid. Asserted.

### 5. Stamps can be turned back into money in offices, but not in courts

s 6 lets the Minister require licence and permit fees in courts, offices and departments
to be paid by stamps. s 7 lets him require fees "now made payable by means of stamps"
to be paid in money, but s 7 names only "public offices and departments". It does not
mention the subordinate courts. On the text, a s 7 order does not reach a court fee
that a s 6 order put on stamps. Asserted.

### 6. Past late-payment charges were validated wholesale

s 10 deems every amount collected before the Statutes (Miscellaneous Amendments) Act
2008 commenced, as a late-payment charge or as interest, "always to have been validly
collected", and bars proceedings over it. It does not cover the underlying fees
themselves. The deposit gives no commencement date for the 2008 Act. Its annotation
reads "wef 01/04/2024", and the deposit does not explain why. Asserted (the
before/after question is an input).

## What would need doing before this is worth anything

- No order under s 2 was retrieved, so not a single fee amount is known. The Act is
  empty for anyone who wants to know what they owe.
- The commencement date of the Statutes (Miscellaneous Amendments) Act 2008, and the
  reason its annotation reads "wef 01/04/2024", were not checked.
- Whether a statutory board counts as a "public office or department" was not looked
  into. The model has only courts, offices and departments, and private businesses.
- No case law on s 4 or s 5 was searched.
