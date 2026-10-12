# States of Malaya Customs Duties Collection Act 1958 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SMCDCA1958.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31 December
2021. The last amending Act in its legislative history is Act 15 of 2010 (Criminal
Procedure Code 2010, in force 2 January 2011). The s 36 table is column-shifted in the
.txt, and its periods were matched to their bands by order.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0256** in the ledger: tier 4 of the remaining Singapore Acts,
ordered by everyday-life relevance. The requirement asks what the Act decides for a
person or business it applies to. No scenario has yet asked a sharper question.

The Act lets Malaysian customs officers collect Malaysian duty at collection stations
in Singapore, on goods and passengers going by land or air to or from Malaysia. This row
covers the parts a traveller, importer, exporter, agent or owner of goods meets:

- authority cards (s 7(2))
- refunds, short-paid duty and abatement (ss 10-12)
- declaration and payment (ss 14(1), 15(1))
- unpaid export duty, uncleared goods and what a sale yields (ss 11(2)-(4), 15(3)-(5), 26)
- search of passengers (s 29)
- seized goods (ss 41, 44)
- compounding (ss 19(2), 43)
- penalties (ss 16(5), 45-47, 49)
- imprisonment in default of a fine (s 36)
- directors (s 51(1))

Not encoded: appointments (ss 3-6), stations and valuation (ss 8, 9, 13), postal
examination (ss 17, 18, 20), documents, samples and handling charges (ss 21-23), loss
in custody (s 25), powers to open, seize and stop (ss 27, 28), most of the evidence and
procedure rules (ss 30-35, 37-40, 42), bribery (s 48), and ss 52-56. The duty rates
themselves come from Malaysian law (s 13) and are not here.

## What the Act turns out to say

### 1. The s 46 minimum fine is capped at $5,000, and the maximum never falls below $5,000

For unlawfully removing goods from a station or tampering with declared goods, a first
offence on dutiable goods carries a fine "not less than 6 times the amount of the
customs duty or $5,000, whichever is the lesser amount". The maximum is 20 times the
duty or $5,000, "whichever is the greater". So the floor grows with the duty only up to
$5,000. On $100 of duty the range is $600 to $5,000. On $1,000 of duty it is $5,000 to
$20,000. Non-dutiable or prohibited goods follow the same pattern at twice and 5 times
the value. Asserted.

### 2. A second assault or obstruction carries a fine *and* imprisonment

For a first offence, s 47(d) gives "a fine not exceeding $2,000 or to imprisonment for a
term not exceeding 9 months or to both". For a second or later offence, (e) reads "a fine
not exceeding $5,000 and to imprisonment for a term not exceeding 18 months", with *and*
where (d) has *or*. Read literally, imprisonment is then mandatory. The encoding reads it
literally. Asserted.

### 3. Default imprisonment reaches its 3-year cap at a $1,600 fine

The s 36 scale is 2 months for a fine up to $25, 4 months up to $50 and 6 months up to
$100, with "2 additional months for every $100 after the first $100" until 3 years. The
cap is reached at $1,600. Every s 45 or s 46 fine of $5,000 therefore carries the same
maximum default term. *Inference:* only each complete $100 adds 2 months, so a $150 fine
stays at 6 months. The text does not settle a part-hundred. Asserted.

### 4. A plain-clothes officer who will not show a card may lawfully be refused

s 7(2): it is not an offence to refuse "any request, demand or order" of an officer who is
"not in uniform and refuses to declare his office and produce his authority card, on
demand being made by that person". The excuse needs the person to have asked first.
Asserted.

### 5. Time limits run both ways, and seized goods are lost after a month of silence

- A refund claim must be made within one year of overpaying (s 10).
- A demand for short-paid duty must come within 12 months (s 11(1)).
- A claim to abatement on damage or wrong valuation needs written notice at or before
  payment (s 12).
- Seized goods with no prosecution are "deemed to be forfeited at the expiration of one
  calendar month from the date of seizure" unless the owner gives written notice of a
  claim first (s 41).

Asserted.

### 6. Uncleared goods can be moved after 4 days and sold after a month

The Collector may move goods deposited for more than 4 days and has a lien for the cost
(s 26(1)). Goods not cleared within a month may be sold after 14 days' notice. The notice
is written if the owner's address is known, and in the Gazette if not (s 26(2)). Unpaid
export goods must be auctioned after 3 months (s 15(3)).

The proceeds pay first the sale charges, then the duty and charges. Any surplus goes to
the owner if found within a month, and otherwise to Malaysia's revenue. If no bid covers
the duty and charges, the goods are forfeited. *Inference:* the sale charges count in
deciding whether a bid is enough. Asserted.

### 7. Passengers keep three protections when searched

- A person may ask to be searched only under a Federal Superintendent's supervision.
- A person may be present at the search of their baggage if they come within a
  reasonable time.
- "No woman shall be searched except by a woman" (s 29).

Asserted.

### 8. Directors carry the burden

s 51(1): when a company commits an offence, a director, manager, secretary or partner "shall
be deemed to be guilty" unless they prove *both* lack of consent or connivance *and* due
diligence. Asserted.

## What would need doing before this is worth anything

- The regulations under s 56 were not retrieved. They prescribe forms, compoundable
  offences, overtime fees, warehouse rent and station hours.
- Whether any collection station still operates was not checked, and nothing in the
  deposit says. The Act refers to the Malayan Railway Station at Keppel Road (ss 14(2),
  24, 29).
- The part-hundred reading of s 36 and the "and" in s 47(e) need a lawyer's view.
- No case law was searched.
