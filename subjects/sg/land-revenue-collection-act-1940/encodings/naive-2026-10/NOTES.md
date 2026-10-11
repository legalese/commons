# Land Revenue Collection Act 1940 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as they appear in earlier naive rows (the skill itself
was not loadable in this session). No pipeline, no coverage table, no independent
test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), as deposited at `../../registers/source-bundle/LRCA1940.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the
latest amendment annotated in the body is Act 25 of 2021, in force 1 April 2022,
against s 22(1).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0152** in `subjects/sg/requirements.jsonl`: tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is short, so nearly all of Parts 1 to 3 is taken: ss 2, 4 to 8, 10 to 14, 16,
17, 19 to 24 and 26. Not encoded: the Collector's appointment (s 2(2)), place of sale
(s 9), costs as part of the arrears (s 15, beyond their place in the upset price),
the mechanics of personal service (s 25), rules and fees (ss 27, 27A), the State's
right to sue in court (s 28), and the Schedule forms. Calendar months are a number
the caller supplies; calendar arithmetic is not modelled.

## What the Act turns out to say

### 1. If no bid covers the debt, the land goes to the State and the owner gets nothing

s 16(1): where "there is no bid sufficient to cover the amount due for the arrear
together with fees and costs due", once that is recorded in the Rent Auction Sale
Book the land "shall revert to and vest in the State" and the defaulter's right,
title and interest "shall cease". Nothing in the Act pays the defaulter any value on
reversion, however much the land is worth above the debt. By contrast, a sale that
does reach the upset price yields a surplus that s 17 makes payable to the person
entitled (or held in trust). Asserted (reversion when the highest bid is below the
upset price; surplus of $2,500 on proceeds of $8,000 against $5,500 due).

### 2. Failing to serve the notice of sale does not invalidate the sale

s 5(3): "no failure to serve or irregularity in serving any notice of sale ... shall
invalidate any sale" or give a cause of action against the Government; it is only
something the Commissioner of Lands considers under s 19. And s 5(2)(a) excuses
service altogether on a proprietor not resident in the district. The encoding states
the invalidity rule as a constant FALSE. Asserted.

### 3. Three months closes almost everything

The purchaser has 3 months to pay the balance (s 11); the sale becomes final at 3
months (s 12) unless the balance is unpaid, or an annulment or extension order has
been served; a court challenge must be brought within 3 months (s 20), and s 21(1)
bars it afterwards "notwithstanding anything in the Limitation Act 1959" unless the
purchaser was party to fraud — and even then a bona fide taker for value from the
purchaser keeps title. A damages suit against the State is likewise barred after 3
months unless an officer was party to actual fraud or the sum was "not in fact an
arrear" (s 21(2)). Only the General Division of the High Court can hear either (s 24).
Asserted.

### 4. Damages for an irregular sale are capped at the price difference

s 22(1): relief needs both a breach of the Act and proof of "substantial injury", and
the defaulter recovers as special damages the difference between the price obtained
and the price the court thinks a regular sale would have fetched, "and no more". The
encoding gives nil where the court's price is not higher (an inference from
"difference" and "no more"). Asserted.

### 5. The Commissioner's annulment power has an ambiguous ground

s 19(1) requires proof "that the sale was had contrary to the provisions of this Part
and that material irregularities occurred or that any proprietor or other person will
suffer excessive hardship". This is read as (contrary AND irregular) OR hardship, so
hardship alone suffices; the other reading would refuse annulment for hardship after
a regular sale. The power ends once the sale is final or court proceedings are
instituted. On any annulment the purchaser's money is refunded with 6% a year (ss
19(2), 22(2)); simple interest by days over 365 is an inference. Asserted on the
chosen reading.

### 6. Paying the whole debt before the sale stops it, whoever pays

s 8: "If any person tenders" the arrear with fees and costs before the sale, the
Collector "shall ... desist". The buyer must put down 25% in cash immediately (s 10),
and a buyer who misses the balance forfeits the deposit and all claim to the land (s
13). Asserted.

### 7. When rent and other revenue fall into arrear

Annual rent is due on 1 January and becomes an arrear on 1 April if unpaid; any other
land revenue becomes an arrear on the 15th day after service of the First Schedule
demand (s 4(1)). Rent in the year of alienation is pro-rated (s 4(2)); the encoding
pro-rates by days, an inference. Asserted.

## What would need doing before this is worth anything

- The s 19(1) fork needs a decided case or the Commissioner's practice.
- The Land Revenue Collection Rules (fees, places of payment, rebate and remission
  under s 27) were not retrieved.
- How the 6% interest runs, and how calendar months are counted, are not settled by
  the text.
- No case law was searched.
