# Singapore Institute of Technology Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SITA2014.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. The only amendment it annotates is [40/2018] (Insolvency,
Restructuring and Dissolution Act 2018, s 509, in force 30 July 2020), at s 7(2).

**Checks:** one case file, 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0210** in `subjects/sg/requirements.jsonl`: tier 3 of the
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

### 1. A deal made without the Minister's prior written consent is void, not just irregular

s 7(3): an act done or agreement made in breach of s 7(1) "has no effect and is
unenforceable at law". So a buyer of substantially the whole of SIT's undertaking or
property, or a person admitted as a member, gets nothing enforceable unless the
Minister consented **in writing** and **beforehand**. The text gives no way to
ratify afterwards. Selling only part of the property is not on the list. Asserted.

### 2. Any person can be required to give information, and refusing is a crime

s 9(2) lets the Minister or an authorised person require "any person", not only the
company, to provide information in their possession or within their reach. The
purpose extends past checking the s 8 money to "any other matters that the Minister
or authorised person requires". Failing to comply without reasonable excuse, or
hindering, obstructing or delaying, is an offence under s 9(4). The penalty is a fine
of up to $1,000 and no imprisonment. Asserted.

### 3. The reasonable-excuse defence may cover only one limb

In s 9(4) the words "without reasonable excuse" sit in the first limb (failing to
comply). The second limb ("or who otherwise hinders, obstructs or delays") carries no
such words. The encoding reads them literally, so someone who obstructs has no excuse
defence. This is a reading. A court might apply the excuse to both limbs. Asserted
as encoded.

### 4. The Minister appoints and removes trustees, yet removal also needs the Minister's consent

s 6(2) lets the Minister remove or replace any trustee at any time. s 7(1)(e) also
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

s 10(1) applies the Societies Act 1966 to student bodies constituted under the
constituent documents, and s 10(2) lets the Minister responsible for societies exempt
one by Gazette order, with conditions. The "despite" wording suggests the Societies
Act would otherwise leave such bodies out. That is an inference, because the Societies
Act was not read. Asserted (the exemption removes a provision only when its conditions
are met, which is also a reading).

### 7. The Act prevails over SIT's own documents

s 11(1): a provision of the memorandum or articles, or a regulation made under them,
that is inconsistent with the Act is void to the extent of the inconsistency. s 3
names degrees, diplomas, certificates, honorary degrees and other distinctions as the
company's particular function, "within the limits of the financial resources
available to it". Asserted.

## What would need doing before this is worth anything

- The constituent documents (memorandum and articles) are not deposited. s 3, s 7(1)(e)
  and s 10 cannot be read properly without them.
- The Societies Act 1966, the Companies Act 1967 and IRDA 2018, which s 7(2) and s 10
  bring in, were not read.
- No Gazette exemption orders under s 10(2) and no case law were searched.
- Whether consent can be given for a class of acts, or in any form other than a separate
  written instrument, is not addressed.
