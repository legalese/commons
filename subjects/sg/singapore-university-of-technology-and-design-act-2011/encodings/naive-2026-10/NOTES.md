# Singapore University of Technology and Design Act 2011 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of the
finished naive rows. The `writing-l4-rules` skill was not available in the session
that wrote this row, although `encoding.json` carries the standard method line that
names it. No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SUTDA2011.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. The only amendment it annotates is [40/2018], at s 7(2). The Act's
date is given as [18 October 2011].

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0217** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

The Act has eleven sections, and most of them govern the university company itself.
This row takes the parts an outsider can meet: the awards s 3 names, the consent
list in s 7(1) and its effect on a deal under s 7(3), s 8(2) on Parliament's money,
the information demand and offence in s 9(2) and (4), student bodies under s 10, and
s 11(1). It does not encode s 4 (accountability, quality assurance, external review),
s 5 (policy directions), s 6 (trustees) except where s 7(1)(e) touches it, s 8(1),
s 9(1) and (3) (access to records, the published summary of accounts), or s 11(2).

The arrangement of sections at the top of the deposit is one line out of step with
the body: it lists "1." with no heading and numbers "Short title" as 2. The encoding
follows the body's numbering.

## What the Act turns out to say

### 1. A deal made without the Minister's prior written consent has no effect

s 7(3): an act done or agreement made in breach of s 7(1) "has no effect and is
unenforceable at law". A buyer of the whole or substantially the whole of the
company's undertaking or property, or a person admitted as a member, gets nothing
enforceable unless the Minister consented **in writing** and **beforehand**. The text
gives no way to ratify afterwards. Selling only part of the property is not on the
list, and s 7(1)(c) names only a **voluntary** winding up, so a winding up by the
court is outside it. Asserted.

### 2. Any person can be required to give information, for any matter the Minister thinks necessary

s 9(2) lets the Minister or an authorised person require "any person", not only the
company, to provide information in their possession or within their reach. Limb (a)
ties the demand to checking the s 8 money, but limb (b) adds "any other matters that
the Minister or authorised person considers necessary". So the only working limit is
the Minister's own view of necessity. (The deposited Singapore Institute of Technology Act
2014, otherwise worded almost identically, ends the same limb with "requires"; the SUTD
deposit says "considers necessary".) Asserted.

### 3. Refusing is an offence, fine only, and the excuse may cover only one limb

s 9(4): failing to comply with a s 9(2) requirement without reasonable excuse, or
hindering, obstructing or delaying the Minister or an authorised person, is an
offence with a fine of up to $1,000 and no imprisonment. The words "without
reasonable excuse" sit in the first limb only. The encoding reads them literally, so
someone who obstructs has no excuse defence. This is a reading; a court might apply
the excuse to both limbs. Asserted as encoded.

### 4. The Minister removes trustees at will, yet removal also needs the Minister's consent

s 6(2) lets the Minister "at any time, remove or replace any trustee". s 7(1)(e) also
requires the Minister's prior written consent for "the removal of any trustee from
the Board". The two fit together only if removal under s 7(1)(e) means removal by
someone else, such as the members under the constituent documents. That is an
inference, because those documents are not deposited. Appointing a trustee is not on
the s 7(1) list. Asserted (consent required for removal, not for appointment).

### 5. Parliament's money is double-locked

s 8(2): money paid under s 8(1) may be spent only on objects that are both in the
constituent documents **and** allowed by the Minister. Other money is not restricted
by s 8(2). Asserted.

### 6. Student bodies come under the Societies Act "despite anything to the contrary" in it

s 10(1) applies the Societies Act 1966 to student bodies constituted pursuant to the
constituent documents, and s 10(2) lets the Minister responsible for societies exempt
one by Gazette order, with conditions. The "despite" wording suggests the Societies
Act would otherwise leave such bodies out. That is an inference, because the Societies
Act was not read. Asserted (the exemption removes a provision only while its
conditions are met, which is also a reading).

### 7. The Act prevails over the company's own documents

s 11(1): a provision of the memorandum or articles, or a regulation made pursuant to
them, that is inconsistent with the Act is void to the extent of the inconsistency.
s 3 names degrees, diplomas, certificates, honorary degrees and other distinctions as
the company's particular function, "within the limits of the financial resources
available to it". Asserted.

## What would need doing before this is worth anything

- The constituent documents (memorandum and articles) are not deposited. s 3, s 7(1)(e)
  and s 10 cannot be read properly without them.
- The Societies Act 1966, the Companies Act 1967 and IRDA 2018, which s 7(2) and s 10
  bring in, were not read.
- No Gazette exemption orders under s 10(2) and no case law were searched.
- Whether consent can be given for a class of acts, or in any form other than a separate
  written instrument, is not addressed.
- The deposit's metadata lists historical versions dated 2011-10-18, 2012-05-31 and
  2020-07-30; none of the earlier versions was read.
