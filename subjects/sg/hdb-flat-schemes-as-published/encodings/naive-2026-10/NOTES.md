# HDB flat schemes as published -- naive encoding (as published)

**This is administrative policy as published, not law.** The source is HDB's
website. HDB can change any condition or figure here by announcement, without a
Bill or gazetted instrument. The pages carry no revision date, so every figure
is "as published on 12 October 2026" unless a page gives its own date.

## Method

**Naive and as published.** One pass from the pages listed below, in the style
of the `writing-l4-rules` skill. No pipeline, no coverage table, no independent
test pass, no human gate.

The pages' eligibility tables sit in tabs that a plain fetch does not return.
WebFetch gave only the navigation, so the text was read in a browser from the
page's DOM. The EHG table is a PDF, which was downloaded and read with
`pdftotext`. Nothing is deposited, because HDB's Terms of Use forbid
reproduction (see `../../SOURCE-LICENSE.md`). Figures are given in my own
words, and quotations are a few words long.

## Sources (all read 12 October 2026)

1. "Couples and Families", tab "Fiance and fiancee":
   https://www.hdb.gov.sg/buying-a-flat/flat-grant-and-loan-eligibility/couples-and-families
2. "Singles", tab "Singles":
   https://www.hdb.gov.sg/buying-a-flat/flat-grant-and-loan-eligibility/singles
3. "Enhanced CPF Housing Grant for Singles":
   https://www.hdb.gov.sg/buying-a-flat/flat-grant-and-loan-eligibility/singles/enhanced-cpf-housing-grant
   and the PDF it links ("average gross monthly income and corresponding EHG amount"):
   https://www.hdb.gov.sg/-/media/buying-a-flat/flat-grant-and-loan-eligibility/singles/enhanced-cpf-housing-grant/EHG-amount-Singles.pdf
4. "Conditions After Buying a New Flat":
   https://www.hdb.gov.sg/buying-a-flat/bto-sbf-and-open-booking-of-flats/conditions-after-buying-a-new-flat
5. Also read, without figures used: "Key Collection"
   (https://www.hdb.gov.sg/buying-a-flat/bto-sbf-and-open-booking-of-flats/process-for-buying-a-new-flat/key-collection)
   and the Terms of Use (https://www.hdb.gov.sg/terms-of-use).

No cpf.gov.sg or mnd.gov.sg page was needed, because HDB's own pages give the
EHG (Singles) rules and table.

**Statute.** The pages cite no Act. HDB sells flats under Part 4 of the
Housing and Development Act 1959 (row `housing-and-development-act-1959`).
s 50 restricts purchase, and s 55(1) bars sale without the Board's consent
"within the prescribed minimum occupation period". This row supplies the period
as HDB publishes it. The statutory tests stay in the Act's row.

## Checks

`l4 run hdb-cases-flat-schemes.l4`: **41 assertions satisfied, 0 errors, 0
warnings**. `runcases.py` reports written=41 satisfied=41 errors=0.

The first six assertions are the three requirements' own questions. The other
35 test boundaries: the income ceilings, the age and citizenship tests, the
30-month property wait, the MOP for each class, and the EHG bands, including
three of HDB's own worked examples ($2,000 alone gives $40,000; $4,000 for two
gives $80,000; $4,400 for two gives $70,000).

## Findings

### 1. REQ-0007 -- eligible; marry within 3 months of completing the purchase

**Answer: eligible.** Both are citizens and both are at least 21. A new 4-room
flat is within "up to a 5-room flat". Their $9,600 is within the published
ceiling for a new 4-room flat. They own no property, and I assume no subsidy
has been taken.

**When they must marry:** page 1 says to solemnise the marriage within **3
months from the completion of the flat purchase**. HDB "may request" a copy of
the marriage certificate. Only a marriage registered overseas has to be shown by
a copy of its certificate within those 3 months.

**Where this differs from the ledger:**

- The ledger expects the marriage *certificate* to be *produced* within three
  months of *key collection*. HDB's wording is to *solemnise* within three
  months of *completion*. Completion is taken to be key collection for a new
  flat (finding 2).
- The ledger's instrument title names a **$14,000** income ceiling. HDB now
  publishes **$16,000** for a new 4- or 5-room flat, and also for a 3-room flat
  except in projects launched at $8,000. The answer does not change at $9,600.
  The title should be corrected.

The scenario date is February 2028. The answer is on the policy as published in
October 2026.

### 2. REQ-0018 -- 15 August 2036

**Answer: the flat may first be sold on the open market on 15 August 2036**, 5
years after keys are collected for a Standard flat. This agrees with the
ledger's 2036-08-15.

Page 4 gives the MOP as follows:

- unclassified or Standard flat: **5 years**;
- new and resale Plus and Prime flats (Prime includes PLH flats sold before the
  October 2024 exercise): **10 years**;
- Fresh Start Housing Scheme: **20 years**.

The MOP starts from the "legal completion date" of the purchase. It excludes
time when the owners do not live in the flat; that exclusion is not encoded, and
the cases assume no such time.

**The page does not say in so many words that completion of a new flat is key
collection.** The inference rests on two passages. Page 4's disposal rule runs
from "key collection or resale completion". The Key Collection page has the
balance paid and the deed stamped at key collection. This should be confirmed.

Two conventions are mine, not HDB's:

- the first day of sale is the anniversary of completion;
- from 29 February into a common year, that first day is 1 March.

After the MOP, a sale is still "subject to the respective prevailing
eligibility conditions". The Act's s 55(1) consent question belongs to the
Act's row.

### 3. REQ-0274 -- eligible; an EHG (Singles) of $25,000

**Answer: eligible.** He is a citizen, single and 35 (the minimum for a new
flat). The flat is a 2-room Flexi, the only new flat type open to singles. His
$2,800 is within the $8,000 ceiling. He owns no property, and I assume he is a
first-timer.

**Grant:** the Enhanced CPF Housing Grant (Singles). He qualifies if he has
worked continuously for 12 months (the period ending 2 months before the HFE
application) and is working at the application. His $2,800 is within the
$4,500 ceiling for a single buying alone. The published table runs in $250
bands. **$2,751 to $3,000 gives $25,000.** The table applies from 20 August 2024.

This matches the ledger's "eligible from 35; grant by income", and gives the
amount. The employment condition is an assumption about facts the ledger does
not state. A new single buyer also pays an additional $15,000, which HDB builds
into the flat price. The scenario date is February 2042. The answer is on the
policy and table as published in October 2026.

### 4. Other things the pages show

- **Undated figures.** None of the income ceilings or MOP periods carries an
  effective date on the page. They are encoded without dated arms.
- **The EHG table has one date.** The page gives "From 20 August 2024" but no
  earlier table. The encoding returns nil for an earlier HFE application rather
  than invent the old amounts.
- **The PDF's second page** (applicant with a non-resident spouse) extracts with
  its columns shifted by one row, so it was not transcribed.
- **Income bands** are stated in whole dollars. The encoding treats each upper
  figure as inclusive, so $750.50 falls in the $751 band.

## What would need doing

- Confirm with HDB, or from the Agreement for Lease, that "legal completion" of
  a new flat is key collection (finding 2).
- Correct the $14,000 in REQ-0007's instrument title to the published $16,000.
- Read the EHG PDF's page 2 visually and add the non-resident-spouse table.
- Encode resale flats and grants, SPR households, the extended-family $24,000
  ceiling, EHG pro-rating, and MOP exclusions if a scenario needs them.
- Re-read the pages before relying on any figure after October 2026, and record
  any change as a new dated arm.
