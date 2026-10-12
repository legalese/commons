# Salvation Army Ordinance 1939 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation "version in force from
1/4/2022", as deposited at `../../registers/source-bundle/SAO1939.txt`. The deposit
says the Revised Edition "incorporates all amendments up to and including 1 December
2021 and comes into operation on 31 December 2021". The latest amendment annotated is
"[Act 25 of 2021 wef 01/04/2022]" under s 7 (the Courts (Civil and Criminal Justice)
Reform Act 2021, per the Legislative History); the only other is "[7/97]" under s 11.

**Checks:** one module (`sao-corporation.l4`), one case file
(`sao-cases-corporation.l4`), 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0248** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has eleven sections, so this row takes all of them except
the short title (ss 2-11). For someone outside the Salvation Army it matters when
buying from, leasing from or lending to the Corporation, when suing or serving it,
and when checking who may act for it.

Not encoded: the recitals beyond background; the content of s 48 of the Conveyancing
and Law of Property Act 1886 (whether a power of attorney was "deposited" under it is
a stated fact here); what "the like extent" in s 3 amounts to; what a restraint in a
title document says (s 5; its presence is a stated fact); other modes of service
besides the one s 7 provides.

## What the Act turns out to say

### 1. Two different filings for the General's attorney, and only one lets him execute deeds

s 6(1) lets a deed be sealed in the presence of, and signed by, the General "or his
attorney duly authorised by a power of attorney deposited under section 48 of the
Conveyancing and Law of Property Act 1886". s 10 separately has a "notarially
certified copy" of the General's power of attorney "lodged at the office of the
Minister", and deems the donee "the duly authorised Attorney". s 6 does not mention
s 10 lodging. On the words, an attorney lodged with the Minister but not deposited
under s 48 cannot execute the Corporation's deeds, though (on the inference that s 7's
"duly appointed Attorney" is the s 10 Attorney) process is served at his residence.
Asserted for s 6 and s 10.

### 2. A General stays the General in evidence until the successor's papers are lodged

s 9: a lodged copy, certified by the Chief of the Staff or the Commissioner acting as
Chief of the Staff, of a document recording "the appointment of and acceptance of
office" by a General is "conclusive in evidence" that the named person is the General
"until the recording and lodging of a similarly certified copy". The cut-off is the
next lodging, not the end of the term; a notary's or a territorial commander's
certificate does not qualify, and a document that records appointment without
acceptance does not either. Asserted.

### 3. A signature is sufficient evidence of due sealing even where the sealing was wrong

s 6(2) makes "such signing" "sufficient evidence that the said seal was duly and
properly affixed". So a deed sealed before an Army officer with no power of attorney
but signed by a deposited attorney fails s 6(1), yet its signature is sufficient
evidence that it complied. The text says "sufficient", not "conclusive". Asserted.

### 4. Only Evangeline Booth's movables were swept in

s 3 vests in the Corporation "all movable property in this Colony now vested in the
said Evangeline Booth", "to the like extent" as before 15 September 1939. Land she
held, movables outside the Colony, and later purchases are not caught by s 3 (later
acquisitions come under s 4). The recitals say immovable property was still "to be so
acquired". The 2020 Revised Edition still says "this Colony"; reading it as Singapore
is an inference. Asserted.

### 5. Disposal yields to the title deed; suing does not depend on property

s 5 lets the Corporation sell, mortgage, lease, exchange, partition or otherwise
dispose of property vested in or acquired by it, but "subject to any restraint,
reservation or condition contained in the document under which it shall acquire
title". s 7's power to "sue and be sued and take all legal proceedings in any of the
Courts" is not tied to property (the Bishop of Singapore Ordinance 1911 ties it to
property). Nothing in the Ordinance grants a power to borrow without security.
Asserted.

### 6. A change of General leaves the property where it is; everyone else's rights are saved

s 8: no change of the person holding the office "shall affect" property vested in the
Corporation. s 11 saves the rights of the Government and any other person "except
such as are mentioned in this Ordinance and those claiming by, from, through, or under
them". Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input, and whether s 48 still exists in that form was not checked.
- The relation between s 6 deposit and s 10 lodging (finding 1) rests on the words
  alone; no practice, Gazette record or case was searched.
- Whether service under s 7 excludes other modes, and whether the s 9 and s 10
  presumptions can be displaced by contrary proof, is not modelled.
