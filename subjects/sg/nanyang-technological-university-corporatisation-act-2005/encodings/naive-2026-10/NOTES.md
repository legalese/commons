# Nanyang Technological University (Corporatisation) Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotated in the body is [40/2018] at s 7(2)
(the Insolvency, Restructuring and Dissolution Act 2018). Deposited at
`../../registers/source-bundle/NTUCA2005.txt`.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0187** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is 19 sections and a Schedule. This row takes what reaches a person or a
business: the Minister's consent and the nullity of acts without it (s 7), the use of
State funding (s 8), the information power and its offence (s 9), the Students' Union
and the Societies Act (ss 10, 18), the Act over the company's own rules (s 11(1)),
litigation, contracts, staff and discipline carried over on 1 April 2006
(ss 12(6), (7), 13-17), and the Register of Graduates (s 19, Schedule). Not encoded:
the company's function, accountability and policy directions (ss 3-5), the Minister's
power over trustees (s 6), and the vesting of property and its trusts (s 12(1)-(5)).

## What the Act turns out to say

### 1. A deal made without the Minister's consent is void, not merely irregular

s 7(1) requires the Minister's prior written consent to admit or remove a member of
the company, to dispose of "the whole or substantially the whole" of its undertaking
or property, to wind it up voluntarily, to change its constituent documents, or to
remove a trustee. s 7(3): an act or agreement in contravention "has no effect and is
unenforceable at law". A buyer of substantially the whole undertaking without that
consent gets nothing enforceable. Selling a single building, hiring staff or
appointing a trustee is not on the list. Asserted.

### 2. Anyone can be required to give the Minister information, on pain of a $1,000 fine

s 9(2) reaches "any person", not only the company, for information "in that person's
possession, or to which that person has access", whether about the use of the s 8
moneys or "any other matters" the Minister considers necessary. Failing to comply
without reasonable excuse, or hindering, obstructing or delaying, is an offence with a
fine not exceeding $1,000 (s 9(4)). No imprisonment is provided, and the text does not
say who must prove the excuse. Asserted.

### 3. Transferred staff kept their terms and their years, but leave was only to be "considered"

s 13(1): everyone employed by the predecessor university immediately before 1 April
2006 was transferred "on terms no less favourable". s 14(2): service with the
predecessor must be recognised as service with the company. But s 14(1) only requires
the company to "consider" earlier terms "including any accrued rights to leave". The
encoding reads monthly pay as one of the "terms" (an inference). Asserted.

### 4. Pending cases, contracts and discipline all carried over to the company

Proceedings commenced before 1 April 2006 and pending on that date continue by or
against the company (s 12(6)). Contracts subsisting immediately before that date are
enforceable by or against it as if it had been named (s 15); for agreements on
transferred property this holds "whether or not" they could be assigned (s 12(7)).
Pending disciplinary proceedings against a transferred employee or "any student of the
predecessor university" must be completed by the company (s 16), and the company may
punish pre-transfer misconduct that the predecessor could have punished (s 17).
Asserted.

### 5. The Students' Union is under the Societies Act unless exempted by order

s 18 deems the NTU Students' Union and its constituent bodies to be constituted under
the company's constituent documents, and s 10(1) applies the Societies Act 1966 to
such bodies "despite anything to the contrary" in that Act, subject to a Gazette
exemption (s 10(2)). Asserted, with a partial exemption treated as not exempt.

### 6. The Register of Graduates reaches back to Nanyang University in 1980

The Schedule's Register has Part A (Nanyang University Guild members on 7 August 1980
and certain Nanyang University degree holders), Part B (predecessor Guild members
before 1 April 2006, predecessor graduates, and NUS graduates who matriculated at the
Nanyang Technological Institute before 1 July 1991) and Part C (graduates of the
company's University). An NUS graduate who matriculated at NTI on or after 1 July
1991 is not on it. The Legislative History (not part of the Act) shows the Nanyang
Technological University Act 1991 commencing on 1 July 1991; that the cut-off follows
from it is an inference. Asserted.

## What would need doing before this is worth anything

- The company's constituent documents and regulations, which s 11 subordinates to the
  Act, were not retrieved; nor any accountability agreement under s 4.
- No s 10(2) exemption order was searched for.
- The determination of which property transferred under s 12(1), and any Minister for
  Finance certificate under s 12(4), were not looked for.
- No case law was searched.
