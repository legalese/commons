# Duties Act 2008 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation of the Duties Act 2008 (No. 11 of 2008) deposited at
`../../registers/source-bundle/mrdoc_49812.txt` (legislation.wa.gov.au mrdoc 49812,
retrieved 2026-09-07). The deposit gives no compilation number or date. Its compilation
table ends with the Help to Buy (Commonwealth Powers) Act 2025 Pt. 4 Div. 1 (in
operation 19 Dec 2025) and lists the Retirement Villages Amendment Act 2024 Pt. 3 as in
operation 1 Sep 2026. The last numbered reprint it names is Reprint 3, as at 13 Nov 2015.

**Checks:** two case files, 54 assertions satisfied (45 in `da-cases-property.l4`, 9 in
`da-cases-vehicles.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **au/wa:REQ-0004**: priority 1, raised 9 times by the three Western Australian
cradle-to-grave lives. The scope is the questions those lives ask:

- **Chloe c051** (2028-02-20): a $620,000 house-and-land package in Byford. Do first home owners pay duty?
- **Chloe c074** (2034-06-15): vehicle licence duty on a $28,000 car.
- **Chloe c081** (2040-04-28): a $1,300,000 townhouse at the general rate.
- **Chloe c094** (2070-05-10): duty on a strata apartment. No price is given, so only the general-rate function answers it.
- **Jake k074** (2042-02-18): a $390,000 apartment off the plan. Is a single first home buyer entitled to the concessional rate?
- **Daniel d037** (2028-03-15): a $1,600,000 apartment bought by a citizen and a permanent resident as joint tenants. Is foreign transfer duty payable? What is the general-rate duty?
- **Daniel d055** (2038-05-20): a $4,200,000 house bought by two citizens.
- **Daniel d065** (2043-06-15) and **d071** (2050-06-30): share acquisitions of unlisted companies. Is there duty?

To answer those questions the encoding takes:

- s 26 and Schedule 2 Division 1 (the general rate)
- Chapter 2 Part 6 Division 3: ss 141, 142A, 142(1) and 143(1), with Schedule 2 Division 2 (the first home owner concessional rate)
- Chapter 3A Part 2: ss 205A, 205H, 205L and 205O (foreign transfer duty)
- s 15 (dutiable property)
- Chapter 3: ss 155(2), 161, 163, 184, 186 and 188 (landholder duty)
- Chapter 5: ss 229, 236 and 238 (vehicle licence duty)

The encoding leaves out:

- every dutiable-value rule (the value is an input) and every exemption, nominal-duty rule and other concession
- the off-the-plan concession in Chapter 6A, which may matter for k074
- further concessional transactions
- for landholder duty: linked entities, relevant arrangements, the s 189 reduction and the exemptions
- foreign landholder duty
- insurance duty
- vehicle exemptions and the vehicle dutiable-value rules

Three things are inputs because the Act borrows them from other laws. Whether a
transferee is a "concessional first home owner" comes from the First Home Owner Grant Act
2000 (s 142A). Whether property "includes a home" takes the FHOG Act meaning (s 141(2)).
Which region the land is in depends on the Planning and Development Act 2005.

## What the Act turns out to say

### 1. The lives' general-rate figures are wrong in two of three cases

Schedule 2 Division 1 charges "$28 453 + $5.15 per $100 or part of $100 above $725 000".
That gives:
- **c081**, $1,300,000: **$58,065.50**. The scenario expects $55,185, which is $2,880.50 short.
- **d055**, $4,200,000: **$207,415.50**. The scenario expects $207,378.
- **d037**, $1,600,000: **$73,515.50**. The scenario's $73,515 drops the 50 cents.

Charging by the $100 "or part of $100" makes the duty a multiple of 5 cents. Before any
band is applied, the dutiable value is "rounded down to nearest whole dollar". Asserted.

### 2. First home owners in Byford do not pay nil duty on $620,000

c051 expects nil duty because the price is "under the threshold". The Act sets these limits for land in the
metropolitan or Peel region that includes a home:
- **$700,000** is the cap for the concession (s 142(1)(b)(ii)).
- **$500,000** is the top of the nil band.
- Between the two, the rate is $13.63 per $100 above $500,000 (Schedule 2 Division 2).

Taking $620,000 as land that includes a home, the duty is **$16,356**. Nil is reachable
only if the dutiable transaction is the land alone, vacant and at or under $350,000. In
a house-and-land package the land contract and the building contract are usually separate.
That is an inference, and the land price is not given; the vacant-land case uses an assumed
$300,000 and is labelled hypothetical.

The concession also depends on FHOG eligibility. s 142A defines a concessional first home
owner by reference to the grant, and s 142(1)(a) requires every transferee to be one.
Asserted.

### 3. The $28,000 car falls in the band whose formula the deposit lost

s 236(2)(a) charges 2.75% only "if the dutiable value of the vehicle does not exceed
$25 000". From $25,001 to $50,000 the duty is "R% of the dutiable value", with R given by a
formula. **That formula is missing from the `.txt` deposit.** Only "(rounded to 2 decimal
places); where — DV is the dutiable value" survives.

c074's $770 is a flat 2.75% of $28,000, which the text does not allow at that value. The
scenario's own note says the rate is "then rising". R is an input here. The cases use
illustrative values: 2.75 reproduces $770, and 3.20 gives $896. Neither value comes from
the deposit.

The text does give the outer bands: 6.5% above $50,000; for a heavy vehicle, 3% capped at
$12,000; and a result "rounded down to the nearest 5 cents". Asserted.

### 4. The ledger's provision references do not match this compilation; d037 owes no foreign duty

- **The first home owner concession** is in Chapter 2 Part 6 **Division 3** (ss 141–146). Division 4 is the s 147 residential or business concession.
- **The foreign buyer duty** is **Chapter 3A Part 2**, where it is called "foreign transfer duty". The compilation has no "Chapter 2 Part 3B".

A "foreign individual" is someone who is not an Australian citizen, not the holder of a
permanent visa and not the holder of a special category visa (s 205A). Priya, a permanent
resident, is therefore not foreign, and neither is Daniel, so d037 owes **no foreign
transfer duty**.

The rate is 7% (s 205O), and joint tenants are taken to be tenants in common in equal
shares (s 205L). The encoding infers that 7% falls on each foreign joint tenant's half: one
temporary-visa holder buying with a citizen at $1,600,000 would owe $56,000. Asserted.

### 5. Shares are not dutiable property; a share sale is dutiable only through landholder duty

s 15 lists the dutiable property: land in WA, rights, chattels in WA and WA business
assets. Shares are not on the list. Landholder duty applies only where all of these hold:
- the company's WA land assets, including those of linked entities, are worth **$2,000,000 or more** (s 155(2))
- the acquirer crosses, or adds to, a **significant interest**: 50% for an unlisted company, 90% for a listed one (ss 161, 163)

The duty is then charged at the general rate on that percentage of the value of the
company's WA land and chattels (ss 184, 186, 188). The answer of no duty for Formly (d065)
and for Jarrah's $40,000,000 sale (d071) depends on facts the lives do not state: how much
WA land each company holds. The cases show both outcomes on hypothetical holdings. Asserted.

### 6. Smaller things worth recording

- At exactly $725,000 the fourth band gives $28,452.50, while the fifth band starts from $28,453. Asserted.
- The concessional bands meet the general rate almost exactly at the caps. A metropolitan home at $700,000 pays $27,260 concessional, against $27,265 at the general rate; $1 over the cap pays $27,269.75. Asserted.
- k074: a $390,000 apartment that "includes a home" is nil at the concessional rate. Read as land without a home, it would cost $6,156. Without the concession it is $12,540. Asserted.
- s 142(1)(b) tests the **unencumbered** value, while the rate applies to the **dutiable** value. This encoding uses one figure for both.

## What would need doing before this is worth anything

- Recover the s 236(2)(b) formula for R from the PDF or DOCX, and re-test c074.
- Encode the FHOG Act eligibility test and its meaning of "home", or link them to an encoding of that Act. Settle how a house-and-land package is treated.
- Encode the dutiable value rules (ss 27–40), the Chapter 6A off-the-plan concession (k074) and the s 189 reduction.
- Add linked entities and relevant arrangements to landholder duty, and add foreign landholder duty.
- Correct the scenarios' expected figures (c051, c074, c081, d055) and the ledger's provision references.
- Check against Revenue WA's published calculators and rulings. None were consulted.
