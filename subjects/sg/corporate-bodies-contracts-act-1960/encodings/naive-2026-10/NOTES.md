# Corporate Bodies' Contracts Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CBCA1960.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021; the latest amendment annotated is S 26/2022 (w.e.f. 13 January
2022), against s 2.

**Checks:** one case file, 30 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0116**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet.

The Act has three sections. This row encodes all its operative text, ss 1 and 2
(s 3 is the short title). Not encoded: which contracts the general law requires to
be in signed writing (set by other law, not retrieved); whether a given signatory in
fact had authority; the formalities of a contract under seal; and the old s 5 of the
Civil Law Act 1909 to which s 1(5) refers (not in the deposit).

## What the Act turns out to say

### 1. The Act does not reach ordinary companies, LLPs or VCCs

s 2 excludes any company as defined in the Companies Act 1967, any limited liability
partnership and (since S 26/2022, w.e.f. 13 January 2022) any variable capital
company. So the businesses most people deal with are outside it; it governs other
bodies corporate — "wherever incorporated" (s 1(1)). That a foreign company registered
in Singapore is not a "company as defined in the Companies Act 1967" is an inference;
that Act's definition was not read. Asserted.

### 2. A body corporate contracts like a private person, through anyone it authorises

s 1(1): where a private person's contract would need writing signed by the party to
be charged, the body's contract needs writing signed by "any person acting under its
authority, express or implied"; where a private person could contract orally, so can
the body. No seal is needed. Implied authority suffices; no authority, no s 1
contract. Asserted.

### 3. s 1(1) only covers two kinds of contract

The section speaks only of contracts that between private persons would need signed
writing (a) or would be valid by parol (b). Our reading: a contract needing some
other form, such as a deed, gets no route from s 1, though s 1(4) leaves the seal
open. This is an inference from the text's silence. Asserted.

### 4. A s 1 contract binds the body, its successors and the other parties

s 1(2) makes it "effectual in law" and binding on "the body corporate and its
successors and all other parties thereto". It does not mention the person who
signed; the encoding says only that s 1(2) does not name them, not whether other
law makes them liable. Asserted.

### 5. Variation and discharge follow the same form

s 1(3): a s 1 contract "may be varied or discharged in the same manner" in which it
may be made. So an oral variation of a contract that needs signed writing does not
qualify; an oral discharge of a parol contract does. Asserted.

### 6. Contracts before 12 November 1993 fall back on a repealed provision

s 1(5): the section does not apply to contracts made, varied or discharged before
12 November 1993, except so far as s 5 of the Civil Law Act 1909 then applied. That
provision is not in the deposit, so whether it applied is taken as a bare fact.
Asserted.

## What would need doing before this is worth anything

- Identify and retrieve the general-law writing requirements that decide which
  contracts fall under s 1(1)(a); the deposit does not say where they are.
- Read the Companies Act 1967 definition of "company" to settle finding 1's inference
  about foreign companies.
- Retrieve the former s 5 of the Civil Law Act 1909 for s 1(5).
- No case law was searched.
