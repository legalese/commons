# Requisition of Resources Act 1985 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/RRA1985.txt`. The running footer says "version in
force from 9/3/2025"; the latest amendment annotated is Act 5 of 2025 (in force
9 March 2025, s 4), with Acts 10, 13 and 30 of 2024 annotated.

**Checks:** one module, one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0095**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The row takes what a person meets when the powers are switched on: when Part 3
operates (s 2), the officer's duty to identify himself (s 7), what may be taken and
when it becomes the Government's (s 12), directions to work and protection from
dismissal (s 17), the compensation formulas for land, work on land, vehicles, goods
and services (ss 19 to 21, 23, 27), the claim windows (ss 28, 29), appeal (s 34),
returns and modifications (ss 38, 39), service of notices (s 41), deemed Government
employment (ss 42, 43) and the penalty (ss 44, 45). Not encoded: appointments
(ss 4 to 6), the land powers in ss 8 to 11 beyond compensation, ships' space and
charter-parties (ss 15, 22), undertakings' work directions (s 16), hire-purchase,
mortgage and third-party interests (ss 24 to 26), Compensation Board constitution and
procedure (ss 30 to 33, 35), the manpower register (s 37), vehicle-return
regulations (s 40), and ss 36, 46 to 48.

## What the Act turns out to say

### 1. None of the requisition powers exist until a Minister switches them on

s 2(1): Part 3 "does not come into operation except" by an order under s 2 (or under
s 21G of the Infectious Diseases Act 1976). The order may not last more than 7 days
unless made with the President's approval (s 2(3)). Asserted.

### 2. Silence for four weeks accepts the Government's offer

The person whose property or service was taken gets a receipt stating what is
offered (s 28(1)). Unless they claim a specified greater amount within 4 weeks of
receiving it, they are "deemed to have accepted the offer" (s 28(3)). They cannot go
to the Compensation Board until 4 weeks after their claim unless the authority
replies first (s 29(2)); a further offer is deemed accepted unless they apply within 8
weeks. The Board's decision is final except on a question of law (s 34). Asserted.

### 3. Goods become the Government's on seizure; a car does not until a notice

A chattel other than a vehicle, vessel or aircraft "vests in the Government" as soon
as possession is taken (s 12(6)). A vehicle, vessel or aircraft is only held for the
period of requisition until a notice of acquisition is served (s 12(2)(b), (3)).
Currency, gold, securities and negotiable instruments are not chattels and cannot be
requisitioned (s 12(15)); for exercises only vehicles, vessels and aircraft can be
taken (s 12(14)). Asserted.

### 4. An owner who made or bought for sale is capped at cost plus profit

Goods are paid for at the reasonable sale price, but a producer gets no more than cost
plus a reasonable profit, and a trader no more than the purchase price plus a
reasonable profit (s 23(2)); a legally fixed price caps everything (s 23(3)). For a
vehicle lost to disaster or war, nothing is paid for the loss unless the requisition
materially increased the risk (s 21(3)). On the encoding's reading, the hire under
s 21(1)(a) is still paid (an inference: s 21(3) speaks only of "loss of, or damage
to"). Asserted.

### 5. A conscripted worker is paid his old rate, and cannot be sacked for it

An employee whose service is requisitioned is paid his contract rate on the day before
(s 27(2)(a)); the self-employed and, since 1 January 2025, platform workers what they
would have earned ((b), (ba)); the unemployed a rate the authority fixes ((c)). If the
job or income would have gone anyway because of the emergency, disaster or war, only
(c) applies (s 27(4)). Allowances count only if paid for 6 months before (s 27(3)).
Without a proclamation of emergency a direction may last at most 7 days (s 17(3)),
and an employer must not dismiss an employee mainly for the service unless employed
for a fixed term (s 17(4)). Asserted.

### 6. A siren or a text message can count as notice

For a notice of requisition (s 12) or a work direction (ss 16, 17), service may be by
broadcast, siren, a phone call to a household member "apparently above 16 years of age", SMS or fax (s 41(3)),
deemed known 6 hours later; registered post is deemed known after 48 hours (s 41(4));
email needs prior consent (s 41(2A)); and ignorance of due service "is not an excuse"
(s 41(7)). Disobedience carries up to $10,000, 2 years, or both (s 45). Asserted.

### 7. You may refuse an officer who will not show his card

s 7(2): refusing to comply with an authorised officer is not an offence if he refuses,
on demand, to declare his office and produce his identification card. Asserted.

## What would need doing before this is worth anything

- No subsidiary legislation was retrieved (the prescribed forms, the manpower
  registration regulations, the s 40 vehicle-return regulations).
- The compensation sums are taken as inputs ("reasonable rent", "reasonable hire");
  how a Board values them is not modelled, nor the timing of payment (s 19(2),
  s 28(8)).
- Day counts treat "within 4 weeks" as up to and including day 28; the text does not
  say how the days are counted.
- The s 21G Infectious Diseases Act route into Part 3 was not read.
