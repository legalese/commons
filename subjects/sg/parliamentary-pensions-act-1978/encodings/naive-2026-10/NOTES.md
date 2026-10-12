# Parliamentary Pensions Act 1978 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PPA1978.txt`. The edition "incorporates all amendments up
to and including 1 December 2021". The latest amending Act annotated is Act 21 of
2012, the Parliamentary Pensions (Abolition) Act 2012.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0196** in `subjects/sg/requirements.jsonl`. It is in Tier 3
of the remaining Singapore Acts, which are ordered by how much they touch everyday life.
The requirement asks what the Act decides for a person it applies to. No scenario has
asked a sharper question yet. This row covers:

- eligibility and amount (ss 2, 2A, 3, 4, 5(1), (2));
- when a granted pension is paid (ss 3(4), (6), 4(4), 15);
- the commutation option and its default (s 7(1) to (5));
- assignment and attachment (s 12);
- corruption (s 13).

Not encoded:

- the s 5(3), (4) suspension and lump-sum catch-up for office-holders pensioned before
  21 May 2011;
- s 7(6) to (9);
- payment intervals (s 8);
- the President's application of withheld or bankrupt pensions (ss 14, 15(3), (4));
- the Pension Fund and regulations, including the provident-fund opt-out (ss 16, 17);
- the savings for the repealed 1970 Act (s 18);
- counting reckonable service from dates. The caller supplies the months.

## What the Act turns out to say

### 1. The scheme is closed: no service after 20 May 2011 counts

s 2(1) defines "reckonable service" as service "on and after 3 June 1959 but not after
20 May 2011". s 2A(1) also denies any pension to a "future Member" for service as a
future Member. A future Member is, broadly, someone first elected or appointed after
1 January 1995. The Legislative History lists the amendments made by s 5 of the Abolition
Act 2012 as commencing on 21 May 2011. That date is more than a year before the Bill's
first reading (13 August 2012). The encoding takes the months that count as an input and
subtracts the future-Member months. Asserted.

### 2. Two fractions that are really one rate per month

s 3(2) gives 1/30 of annual salary for each completed year and 1/360 for each completed
month of a remaining part-year. s 4(2) gives 1/27 and 1/324 for office service. Because
1/360 is exactly 1/30 divided by 12, and 1/324 is 1/27 divided by 12, each formula comes
to a flat rate for every completed month. The caps are two-thirds of salary (ss 3(3),
4(3)). They are therefore reached at 20 years as a Member and at 18 years in office. The
minimums are 9 years (s 3(1)) and 8 years (s 4(1)). On a $360,000 salary, 10 years 5
months gives $125,000 and 25 years is capped at $240,000. Asserted.

### 3. A candidate loses a Member's pension but keeps an office pension

s 3(4) suspends a Member's pension while the person is "again a Member or is a candidate
for election to Parliament". s 3(6) treats someone who left on a dissolution as a candidate
from the dissolution date if they seek re-election. s 4(4) suspends an office pension only
while the person is "again an office-holding Member", and says nothing about candidacy.
Asserted.

### 4. Silence chooses the lump sum

s 7(2)(b) requires the option within 30 days of eligibility. The President may allow it
later if that is equitable. s 7(3) deems anyone who fails to choose "to have opted to
receive a commuted pension gratuity without any pension". The reduced-pension option gives
up one-third of the pension for 12.5 times that third (s 7(1)(b)(ii)). It is open only to
Members who are not future Members and to those who kept eligibility under s 2A(2)(b). A
future Member who became an office-holder may take only the full pension or the commuted
gratuity. The commutation factor is prescribed by the President and is not in the Act;
the case file uses a hypothetical 15. Asserted.

### 5. A maintenance order may take an assignment but not an attachment, and only for a wife or child

s 12 allows a pension to be assigned for a debt due to the Government, or for a court
order of periodical maintenance for "the wife or former wife or minor child". It may be
attached only for "a debt due to the Government". On a literal reading, a maintenance
order for a husband or former husband is not an exception. That reading is an inference
from the gendered text. Asserted.

### 6. Corruption, even with only a fine, can cost the pension

s 13(1): "No person has an absolute right" to a pension. s 13(2) lets the President
reduce or withhold a pension after any conviction under the Prevention of Corruption Act
1960, or for any other offence involving corruption, "even if only a fine" was imposed.
s 13(3) requires the President to consider the court record first. s 15 bars a grant to
an undischarged bankrupt at the date of eligibility, and ends a pension on bankruptcy.
s 15(5) restores it from the date of discharge. Asserted.

## What would need doing before this is worth anything

- Reckonable service should be counted from dates. This includes service in the
  Legislative Assembly from 1959 to 1965 (s 2(2)) and the treatment of continuous service
  in the "future Member" definition.
- The pre-2011 s 5(3), (4) lump-sum catch-up and the s 7(6) reduction on re-computation
  are unencoded. Pensions affected by them still in payment would need both.
- The prescribed commutation factor and discount rate, and any regulations under s 17,
  were not retrieved.
- s 18 persons under the repealed 1970 Act are outside the encoding.
