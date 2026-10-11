# COVID-19 (Temporary Measures) Act 2020 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill conventions (by way of the example rows) and nothing else. No pipeline, no
coverage table, no independent test pass, no human gate. NOT for public use.

**Edition:** informal consolidation, "version in force from 1/7/2026", deposited at
`../../registers/source-bundle/COVID19TMA2020.txt` (retrieved 1 October 2026). The Act
is still printed as "No. 14 of 2020", not in a Revised Edition. The latest amendment
annotated is Act 15 of 2026 wef 1 July 2026 (the s 2 definition of "Minister", and the
repeal of Parts 8C and 10A).

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0120** in `../../../requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act runs to about 170 pages in twelve Parts with five Schedules. This row takes
what a business or resident actually met: Part 2 relief for inability to perform
contracts (ss 4, 5, 6, 7, 8, 9, 14 and First Schedule para 1), entry to and
application of Part 2A rental relief (ss 19C, 19H(2)), the offences (ss 8(1), 19W,
34(7), 35(9) to (11), 106) and the expiry dates in s 1. Not encoded: late applications
(ss 1A to 1C), s 5A, the interest caps and holding-over amounts of ss 7A and 7B (left to
regulations), the assessor machinery, the rest of Part 2A, Part 3 (insolvency), Parts 4
and 5 (remote meetings and hearings), Part 6 (property tax), what a control order may
contain, Parts 8 to 10 and Part 12 beyond s 106. No regulation or Gazette order was
retrieved, so every "prescribed" period, rate, amount and property is an input.

## What the Act turns out to say

### 1. The everyday parts are spent

s 1(2A): Parts 1 (except s 2) and 2 "remain in force until the end of 19 April 2022".
s 1(7): Part 7 (control orders) remains in force "until the end of 8 April 2024". s 1(2):
Part 3 lasted one year from commencement. What survives (s 1(3), (4)) is the effect of
things already done, a list of sections including ss 7B and 8, and pending assessor
applications. In October 2026 the Act decides almost nothing about a new situation.
Asserted.

### 2. Only listed contracts were protected, and the list is a business list

First Schedule para 1 names business loans secured on commercial or industrial property
or business plant, performance bonds, hire-purchase and leases of business plant or
commercial vehicles, event and tourism contracts, construction and supply contracts,
leases of non-residential property, and developers' options and sale agreements. A home
loan, a residential tenancy or a personal loan is not there. A lease of a commercial
vehicle is, "except" a private hire car or a taxi — though the s 5(3)(k) example of a
protected repossession is "a motor car used as a private hire car, that is the subject
of a hire-purchase agreement". Asserted.

### 3. A right of renewal saved a shop lease but not a loan

s 4(1): a non-residential lease or licence renewed "in exercise of a right of renewal"
on or after 25 March 2020 stays in Part 2; any other scheduled contract stays only if
renewed "automatically". Part 2A (s 19C) uses the same cut-off date for leases. Asserted.

### 4. Notification bought a moratorium, not a release

s 5(2): once A served a notification for relief on the other party and any guarantor,
B "may not take any action described in subsection (3)" — suing, arbitrating,
enforcing security, winding up, bankruptcy, receivers, repossessing business goods,
terminating a lease for unpaid rent, re-entry — "until after the earliest of" the end of
the prescribed period, withdrawal, or an assessor's finding that s 5 does not apply.
Limitation periods are extended by the same span (s 5(7)). s 5(13): the section "does not
affect" frustration or force majeure. A letter of demand is not on the list. The
encoding reads an action on the very day the moratorium ends as still barred ("until
after"); that is a reading, not a holding. Asserted.

### 5. Event deposits were protected after the period ended, too

s 7(2): after notification the other party may not "at any time (whether during or after
the prescribed period)" forfeit a deposit, unless the notification is withdrawn or an
assessor finds forfeiture just and equitable; s 7(3) required deposits forfeited since
1 February 2020 to be restored. s 7(4): COVID-19 causation is a defence to a
cancellation fee. Asserted.

### 6. A breach is undone, and only lightly punished

s 8(1): a fine not exceeding $1,000, with no imprisonment, for breaching the moratorium,
an early bond call, or forfeiting a deposit. The real sanction is s 8(2) to (6):
proceedings are dismissed on lodging the notification, a receiver's appointment, a bond
call or a deposit forfeiture is void, a repossession or a termination for unpaid rent is
invalid, and enforcement of security is void except against "a bona fide purchaser for
value without notice". By contrast a false declaration for rental relief or waiver
(ss 19W, 106) carries $5,000 or 12 months, and a control-order breach (s 34(7)) or
disobeying an enforcement officer (s 35(11)) $10,000 or 6 months, doubling to $20,000 or
12 months for a repeat offence — the only offences here with a repeat step-up. Asserted.

### 7. Construction delay during the period did not count for liquidated damages

s 6(5): days of inability between 1 February 2020 and the end of the prescribed period
"are to be disregarded in determining the period of delay". s 6(2): a performance bond
could not be called earlier than 7 days before its expiry, and s 6(3) let A extend the
bond to 7 days after the end of the prescribed period by applying at least 7 days before
expiry. Where that would fall before the stated expiry the text is silent; no such case
is tested. Asserted.

### 8. Rental relief for rent already paid came back as credit first, cash second

s 19H(2): rent already paid for the prescribed period, up to the prescribed amount (the
"deductible amount"), reduces future rent earliest first; any balance must be refunded
"immediately" and is a debt. s 19H(3): the relief is not limited to the cash grant the
landlord received. Asserted.

### 9. No lawyers before an assessor unless permitted

s 14: no advocate and solicitor "except with the permission of the assessor"; s 15: each
party bears its own costs. Asserted (s 14).

## What would need doing before this is worth anything

- The regulations and Gazette orders (the prescribed periods for each description of
  contract, the notification deadline under s 9(1), the s 7A interest cap, the s 7B
  holding-over amount, the prescribed properties and amounts in Part 2A) were not
  retrieved; all are inputs.
- Parts 8 to 10 and Part 12 (construction delay, cost-sharing, renegotiation, the 2021
  rental waiver) are substantial and unencoded.
- No assessor determinations or case law were searched.
- Day numbers stand in for dates in the timing rules; nothing checks calendar arithmetic.
