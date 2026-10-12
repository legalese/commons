# Jewish Synagogue Ordinance 1878 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/JSO1878.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The amendment annotations in the body are "[7/97]" under s 5(2)
and "[42/2005; 40/2019]" and "[Act 25 of 2021 wef 01/04/2022]" under s 7(2). The
Ordinance is dated 29 March 1878.

**Checks:** one module (`jso-trust.l4`), one case file (`jso-cases-trust.l4`),
54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0236** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has eight sections, so this row takes all of them except
the short title (ss 2-8). For someone outside the trust it matters when buying from
the trustees (ss 2, 4) and in the Government's reversion of the synagogue land
(s 5(2)); for a member of the Jewish community, in who may go to the High Court when
the trustees fall below three (s 7(2)).

Not encoded: the recitals (the 1841 pepper-corn lease, its resumption proviso, the
1876 deed made at Aleppo) beyond background; whether the s 2 sale has taken place
(the text does not say); what "think proper" and "suitable" require; the procedure
on an originating application.

## What the Act turns out to say

### 1. The synagogue land reverts to the Government automatically if worship stops

s 5(2): "So soon as the said piece of land ceases to be used for such purpose it
shall ipso facto revert to the Government." The purpose (s 5(1)) is "erecting and
maintaining thereon a suitable synagogue or place of Divine worship according to the
Jewish form". On the words, a community hall, a school, a commercial letting,
another faith's worship or simply leaving the land unused each end the trust use,
and no notice or order is needed. Building the synagogue counts as trust use.
Asserted.

### 2. "The said piece of land" in s 5(2) is the old land's phrase, used of the new land

The recitals and s 2 use "the said piece of land" for the Synagogue Street land;
s 5(2) uses it under the side note "When to be forfeited", in a section about the
land "so to be purchased". This row reads it as the new land. That is an inference
from its place; the drafting points both ways. Not separately asserted.

### 3. With three trustees left, they appoint; with two, only the High Court can

s 7(1): the trustees "being not less than 3" may appoint replacements for trustees
who "have died, or left the Colony, or declined further to act". s 7(2): if the
number falls below 3, the General Division of the High Court may appoint, on an
originating application by the remaining trustees "or by any of the members of the
Jewish community", and only members of the community residing in Singapore. There
is no power to remove a trustee, and s 7(1) sets no qualification for a
trustee-appointed trustee. Asserted.

### 4. The power of sale is given to seven named trustees and their survivors

s 2 gives the power to seven named trustees "or the survivors of them, or any 2 or
more of such surviving trustees, who are for the time being resident within the
Colony". It does not extend to trustees appointed later under s 7, and covers only
the Synagogue Street land of the 1841 lease and its buildings. Reading "resident" as
qualifying every seller, and allowing a sole survivor to sell, are inferences.
Asserted.

### 5. The buyer need not follow the money; the trustees must

s 4: the sellers' receipts "shall be sufficient discharges to the purchasers who
shall not be bound to see to the application of such purchase money". s 3: net of
the costs of sale, the money goes to buying land and building a new synagogue "and
to no other purpose". A buyer paying valid sellers is discharged even if they misapply
the money. Asserted.

### 6. Trust property passes to new trustees without a transfer

s 8: the land, building, fixtures, furniture "and other movable property belonging to
the synagogue for the purpose of Divine worship" vest in the trustees for the time
being "without transfer or assignment from trustees to trustees". s 6 requires the
conveyance of the new land to express the trust and condition. Asserted.

## What would need doing before this is worth anything

- Find out whether the s 2 sale happened and what land the trust now holds (the
  Ordinance does not say); the Government's reversion turns on it.
- Settle what "the said piece of land" in s 5(2) refers to.
- Check whether s 8 vesting carries the s 2 power of sale to later trustees.
- No case law, Gazette notices or land records were searched.
