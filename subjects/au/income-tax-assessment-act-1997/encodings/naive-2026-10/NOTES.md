# Income Tax Assessment Act 1997 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. **Not for public use.**

**Edition:** Compilation No. 267, compilation date 27 August 2026, including
amendments up to Act No. 79, 2026 (register id C2026C00400, 12 volumes), as deposited at
`../../registers/source-bundle/C2004A05138.txt`.

**Checks:** five modules and five case files, 68 assertions satisfied, 0 errors, 0 warnings (58 before `itaa-formulas.l4` of 24 October 2026):

| Module | Case file | Assertions |
|---|---|---|
| `itaa-income.l4` | `itaa-cases-income.l4` | 17 |
| `itaa-business.l4` | `itaa-cases-business.l4` | 11 |
| `itaa-cgt.l4` | `itaa-cases-cgt.l4` | 15 |
| `itaa-super.l4` | `itaa-cases-super.l4` | 15 |
| `itaa-formulas.l4` (imports `itaa-income.l4`, `itaa-super.l4`) | `itaa-cases-formulas.l4` | 10 |

## Why this Act, and why scoped

This encoding answers **REQ-0001** in `subjects/au/requirements.jsonl` (priority 1). The three
Western Australian cradle-to-grave lives raise the Act **24 times**:

- **Chloe:** c045, c048, c057, c072, c080, c083, c085, c087, c092, c094, c096, c098
- **Jake:** k043, k089, k098
- **Daniel:** d049, d04a, d04b, d055, d071, d072, d081, d083, d093

The Act runs to 12 volumes and nearly 100,000 lines of deposited text. This encoding takes only
the provisions those events ask about. It adds the definitions, conditions and exceptions needed
to answer them:

- **Income** (`itaa-income.l4`): ss 4-10 and 4-15; ss 6-5 and 8-1; the Low Income tax offset
  (ss 61-110, 61-115); the working Australians tax offset (ss 61-155, 61-160); tax losses
  (ss 36-10, 36-15(2), 36-17(2)); gifts of money (s 30-15 items 1 and 2, s 30-15(2), s 26-55).
  For c045, c048, c083, k043, d04a, d072 and d093.
- **Business** (`itaa-business.l4`): the start-up concession for employee share schemes
  (ss 83A-25, 83A-33, 83A-45); the R&D offset rate (s 355-100); the early stage investor offset
  (ss 360-15, 360-20, 360-25). For c072, d04b, d049 and d081.
- **Capital gains** (`itaa-cgt.l4`): the discount (ss 115-5 to 115-25, 115-100, 115-102); the net
  capital gain (s 102-5, simplified); the main residence exemption (ss 118-110, 118-150); the
  $6,000,000 test (ss 152-10(1)(c), 152-15); death (ss 128-10, 104-215, 118-60). For c080, d055,
  c085, d071 and d093.
- **Superannuation** (`itaa-super.l4`): the spouse contribution offset (ss 290-230, 290-235); the
  non-concessional cap (ss 291-20(2), 292-85(2)); downsizer contributions (s 292-102); the transfer
  balance cap (ss 294-30, 294-35); benefits at 60 (ss 301-10, 301-15); death benefits (ss 302-60,
  302-140, 302-145, 302-195). For c057, k089, c094, c092, d083, c087, c096, c098, k098 and d093.

**Inputs, not encoded.** The Act does not fix these amounts, so they are inputs:

- the rates and the tax-free threshold (Income Tax Rates Act 1986)
- the corporate tax rate
- every indexed cap after 2017-18 (the concessional contributions cap, the general transfer
  balance cap)
- total superannuation balances
- preservation age

The Medicare levy and HELP repayments asked in c045 and c048 belong to other Acts.

**Inputs now computed (24 October 2026).** The Act's formulas, which the text deposit lost, are now transcribed in `../../registers/source-bundle/C2004A05138.formulas.md`. `itaa-formulas.l4` uses them to work out three of the inputs above, calling the existing rules without changing them:

- net labour income (s 61-155(2), labour amounts less labour deductions), for `the working Australians tax offset`;
- the concessional contributions cap and the general transfer balance cap for 2017-18 or later (ss 291-20(2), 294-35(3), indexed under s 960-285), for `the non-concessional contributions cap` and `the transfer balance cap on first having an account`.

The AWOTE and CPI index numbers they are worked out from stay inputs: they are published figures, not deposited. The rates, the threshold and the notional liability stay inputs too, since they come from the Rates Act, not from a formula. The baseline (`../baseline-2026-10/`) carries the same formulas and more, with seat questions.

## What the Act turns out to say

### 1. The 50% CGT discount ends for individuals on 1 July 2027, so the 2050 sale of Jarrah gets none

Section 115-100(aa) gives an individual 50% only for a gain "from a \*CGT event happening before 1
July 2027". After that date only paragraph (a) gives 50%: a new residential dwelling (s 115-102).
Otherwise paragraph (f) gives "0% if none of the above paragraphs applies". Trusts get the same
cut-off (paragraph (ab)). Complying superannuation entities keep 33⅓%.

Indexation of the cost base takes the discount's place for individuals and trusts (s 110-36(1A)).
So does a deemed sale and reacquisition on 1 July 2027 (Subdivision 112-E). Neither is encoded.

**This contradicts the scenarios:**
- **d071** expects `cgt_discount: 0.5` on Daniel's sale of Jarrah on 30 June 2050.
- Its SCENARIO.md answers "half of it".
- **c085** asks whether the discount applies to Chloe's buy-out on the same day.

On this compilation, Daniel's shares (held from 2031) give a discount capital gain under s 115-25,
but the discount percentage is **0%**. Asserted.

### 2. A testamentary gift is not deductible, but the capital gain on it is disregarded

Section 30-15(2) says: "A testamentary gift or contribution is not deductible under this section."
So the gift to the Rossi Foundation in Daniel's will (d093) earns no deduction. Passing an asset
to an exempt entity on death would normally be CGT event K3 (s 104-215). Section 118-60(1),
however, disregards the gain on "a testamentary gift of property that would have been deductible
under section 30-15 if it had not been a testamentary gift". The same asset passing to an exempt
entity other than as such a gift does give a gain. The residue passing to the testamentary trust
is disregarded under s 128-10. Asserted.

### 3. Superannuation death benefits: tax-free to a spouse, taxable component taxed to adult children

- A lump sum to a "death benefits dependant" is not assessable income (s 302-60). A dependant is
  defined in s 302-195: a spouse or former spouse, a child under 18, an interdependent person, or
  a dependant. This covers the benefits to Sue (c087), to Chloe (c096) and to Priya (d093).
- Adult children are not dependants unless they were dependent or interdependent. That covers
  Oliver and Ella (c098) and Ruby (k098).
- For non-dependants, the taxable component is assessable income (s 302-145(1)), with an offset
  capping the rate at 15% on the element taxed in the fund (30% on the untaxed element). The tax
  free component is not assessable (s 302-140).

The scenarios' expectations match. Asserted.

### 4. Byford is exempt only by choice: the land was bought 17 months before the family moved in

Section 118-110(1)(b) requires the dwelling to be the main residence "throughout your \*ownership
period". The facts:
- Chloe and Liam signed the Byford land contract on 2028-02-20.
- They stayed in the Cannington rental until 2029-07-14.
- They moved in on handover, 2029-07-15.

So s 118-110 alone fails. Section 118-150 lets them choose to treat the dwelling as their main
residence from acquisition. They must move in as soon as practicable and stay at least 3 months,
and the period covered is at most 4 years. With the choice, c080's expected nil holds; without
it, it does not. The East Perth apartment (d055) was lived in from purchase and is exempt
outright. Asserted.

The encoder's reading: the 17 months is counted from the contract date. Neither the scenario nor
this encoding derives the acquisition time from s 109-5.

### 5. Daniel is far outside the $6,000,000 test; the concessions need more than that anyway

Section 152-15: the net value of your CGT assets, your connected entities' and your affiliates'
must "not exceed $6,000,000" just before the event. A CGT small business entity needs aggregated
turnover under $2 million (s 152-10(1AA)). Jarrah sold for $40,000,000, so Daniel fails both
routes to basic condition (c) (d071, "concessions out of reach"). Asserted, with $40,000,000 as
the net value input, which is an inference.

### 6. Start-up ESS interests: no tax on the discount if eleven conditions hold

Section 83A-33 reduces the s 83A-25 inclusion to nil where all of the following hold:
- the group is unlisted;
- the company was incorporated less than 10 years before its last income year end;
- aggregated turnover is no more than $50 million;
- the discount is no more than 15% of market value (or, for a right, the exercise price is at least
  market value);
- the employer is an Australian resident;
- the s 83A-45 conditions hold: the person is an employee, the scheme covers ordinary shares only,
  shares cannot be disposed of for 3 years, and the person holds no more than 10%.

Chloe joins Jarrah on 2034-02-01, about 2 years after its last year end following registration
on 2031-03-15. She qualifies on a hypothetical 10% discount, and fails at 20% (c072, d04b).
Asserted.

### 7. Smaller things worth recording

- **Low Income tax offset (s 61-115):** $700 up to $37,500. It then reduces by 5% to $45,000
  ($325) and by 1.5% to $66,667. Above $66,667 there is no entitlement (s 61-110(1)(b)). Chloe's
  $27,500 (c045) gets $700. Her $71,500 (c048) gets nothing. Asserted.
- **Working Australians tax offset (Subdivision 61-E):** the deposit contains a new offset. It is
  the lesser of $250 and the tax on net labour income, for residents whose net labour income
  exceeds the tax-free threshold. The provision as read does not say from which year it applies,
  so it is not applied to any event. Asserted on hypothetical figures.
- **R&D (s 355-100):**
  - Under $20 million turnover, the offset rate is the corporate tax rate plus 18.5 percentage
    points, and the offset is refundable. With the scenario's 25% that is 43.5% (d049).
  - Otherwise it is the corporate rate plus a premium (not encoded).
  - Asserted.
- **Early stage investors (Subdivision 360-A):**
  - The offset is 20% of the amount paid, capped at $200,000 including amounts carried forward.
  - A retail investor who pays more than $50,000 in a year gets nothing (s 360-20). A
    sophisticated investor under s 708(8) is outside that limit (d081).
  - Asserted.
- **Company losses (s 36-17(2)):** a company may choose how much of a loss to deduct, including
  nil. An individual must deduct it against the excess (s 36-15(2)). Asserted for the company
  (d04a).
- **Gifts (s 30-15):** a gift of money to a private ancillary fund (item 2) is deductible in
  full, subject to the s 26-55 limit (assessable income less other deductions). For d072's
  $2,000,000, see the spreading rules in Subdivision 30-DB, which are not encoded. Asserted.
- **Non-concessional cap (s 292-85(2)):** the cap is four times the concessional cap, whose
  2017-18 base was $25,000 (s 291-20(2)). It is nil once the total superannuation balance reaches
  the general transfer balance cap. Jake's $100,000 at 54 (k089) is within the cap at any
  concessional cap of at least $25,000. That was the base, and indexation does not necessarily
  increase it (the note cites s 960-285, which was not read). Asserted.
- **Downsizer (s 292-102):** the person must be 55 or over and the home must have been held 10
  years. The contribution must be made within 90 days, and the cap is $300,000 each, limited by
  the proceeds. Chloe (67) and Liam (70) can each contribute $300,000 after 30 years in Baldivis
  (c094); the proceeds are a hypothetical $1,500,000. Asserted.
- **Benefits at 60 (s 301-10):** a benefit received at 60 or over "is not assessable income and
  is not \*exempt income". This covers Chloe at 63 (c092) and Daniel at 67 (d083). Asserted.
- **Transfer balance cap (s 294-35(3)):** $1,600,000 for 2017-18, indexed after that. Asserted
  only for 2017-18.

## What would need doing before this is worth anything

- **The rates.** Encode the Income Tax Rates Act 1986 (and the Medicare Levy Act) so that
  c045 and c048 compute tax rather than take it as input.
- **CGT after 1 July 2027.** Encode the indexation regime (s 110-36(1A), Div 114, Subdiv 112-E),
  which is now the main relief for individuals. Then the scenarios d071 and c085 need correcting:
  they expect a 50% discount the text no longer gives.
- **Indexed amounts.** Supply the concessional and transfer balance caps for each year from the
  Commissioner's published indexation, as inputs with sources.
- **The rest of Div 152.** Encode the active asset test, s 152-10(2) for shares, and the
  concessions themselves (Subdivisions 152-B to 152-E).
- **Other gaps:**
  - Div 83A's deferral route and Subdiv 130-D.
  - Division 355 beyond the rate.
  - Section 360-40.
  - Partial main residence exemptions (ss 118-185 to 118-192) and the absence rule (s 118-145).
  - Elements untaxed in the fund.
  - The bring-forward of the non-concessional cap.
  - When the working Australians tax offset applies.
- No ATO ruling, regulation or case law was retrieved.

## c045 corrected (22 October 2026, REQ-0056)

The first pass asserted that c045 owes nil, taking a nil basic liability from the scenario
("nil under the tax-free threshold"). That is wrong. Chloe's $27,500 is above the $18,200
threshold. On the 2023-24 rates (Rates Act Compilation No. 62, now deposited as
`../../../income-tax-rates-act-1986/registers/source-bundle/C2004A03348.2024-04-01.txt`) the
basic liability is $1,767, and after the $700 Low Income tax offset $1,067 is owed. The case
file now asserts `the income tax owed` 1767 700 = 1067 for c045. It keeps the nil-in, nil-out
assertion as a plain case of the rule. The liability is still an input here; the baseline
(`../baseline-2026-10`) computes it.
