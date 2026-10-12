# Singapore University of Social Sciences Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SUSSA2017.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. The only amendment it annotates is [40/2018], at s 7(2). The
deposit's Legislative History names that as the Insolvency, Restructuring and
Dissolution Act 2018 (amendments made by section 512, commencement 30 July 2020).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0216** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

The Act has eleven sections, and most of them govern the university company itself.
This row takes the parts an outsider can meet: which company the Act is about (s 2),
the awards s 3 names, the consent list in s 7(1) and its effect on a deal under
s 7(3), s 8(2) on Parliament's money, the information demand and offence in s 9(2)
and (5), student bodies under s 10, and s 11(1). It does not encode s 4
(accountability framework, quality assurance, external review panel), s 5 (policy
directions), s 6 (trustees) except where s 7(1)(e) touches it, s 8(1), s 9(1), (3)
and (4) (access to records, the published summary of financial statements), or
s 11(2).

The arrangement of sections at the top of the deposit is one line out of step with
the body: it lists "1." with no heading and numbers "Short title" as 2. The encoding
follows the body's numbering. The Comparative Table says s 12 of Act 30 of 2017 was
omitted from the 2020 Revised Edition "as having had effect"; what it said is not in
the deposit.

## What the Act turns out to say

### 1. A deal made without the Minister's prior written consent has no effect

s 7(3): an act done or agreement made in breach of s 7(1) "has no effect and is
unenforceable at law". So a buyer of the whole or substantially the whole of the
university's undertaking or property, or a person admitted as a member, gets nothing
enforceable unless the Minister consented **in writing** and **beforehand**. The text
gives no way to ratify afterwards. Disposing of only part of the property is not on
the list. Asserted.

### 2. Any person can be required to give information, for any purpose the Minister names

s 9(2) lets the Minister or an authorised person require "any person", not only the
company, to provide information in their possession or to which they have access.
The purposes are (a) checking that s 8 money was properly spent "or (b) any other
matters that the Minister or authorised person requires", so limb (b) leaves no
purpose outside. Failing to comply without reasonable excuse, or hindering,
obstructing or delaying, is an offence under s 9(5). The penalty is a fine of up to
$1,000 and no imprisonment. Asserted.

### 3. The reasonable-excuse defence may cover only one limb

In s 9(5) the words "without reasonable excuse" sit in the first limb (failing to
comply). The second limb ("or who otherwise hinders, obstructs or delays") carries no
such words. The encoding reads them literally, so someone who obstructs has no excuse
defence even if they had one for not complying. This is a reading; a court might
apply the excuse to both limbs. Asserted as encoded.

### 4. The university is the company once called SIM University

s 2 defines the university company by its incorporation: a company limited by
guarantee incorporated under the Companies Act 1967 on 14 April 2005 as "SIM
University", renamed "Singapore University of Social Sciences" on 17 March 2017. A
different company that took the same name later would not be the university company.
INFERENCE, not stated in the Act: since it is the same company, an award made under
the old name was made by the same legal person. Asserted (the identity test only).

### 5. Only a voluntary winding up needs consent

s 7(1)(c) names "the voluntary winding up of the university company". A winding up
ordered by the court is not on the list, so s 7(3) does not touch it. Consent is also
required for removing a trustee (s 7(1)(e)) although s 6(2) lets the Minister remove
trustees at any time; the two fit only if s 7(1)(e) is aimed at removal by someone
else, such as the members under the constituent documents (an inference: those
documents are not deposited). Appointing a trustee needs no consent. Asserted.

### 6. Parliament's money is double-locked

s 8(2): money paid under s 8(1) may be spent only on objects that are both in the
constituent documents **and** allowed by the Minister. Money from other sources is not
restricted by s 8(2). Asserted.

### 7. Student bodies are under the Societies Act "to avoid doubt"

s 10(1) says, "To avoid doubt", that the Societies Act 1966 applies to any student
body constituted under the constituent documents, and s 10(2) lets the Minister
responsible for societies exempt one by Gazette order, with conditions. The words
"to avoid doubt" make (1) a confirmation, not an extension. The encoding treats an
exemption whose conditions are not met as leaving the provision in force (a reading).
s 11(1) separately makes any provision of the memorandum or articles, or a regulation
made under them, void to the extent it is inconsistent with the Act. Asserted.

## What would need doing before this is worth anything

- The constituent documents (memorandum and articles) are not deposited. s 3,
  s 7(1)(e), s 10 and s 11(1) cannot be read properly without them.
- The Societies Act 1966, the Companies Act 1967 and IRDA 2018, which s 7(2) and s 10
  bring in, were not read.
- The accountability agreement under s 4(1) and any Gazette exemption orders under
  s 10(2) were not searched; no case law was searched.
- The omitted s 12 of Act 30 of 2017 (the transitional provisions, by inference from
  "omitted as having had effect") was not retrieved; it may bear on awards and
  students carried over from SIM University.
