# Singapore Management University Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SMUA2000.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The only amendment annotated in the body is [40/2018] (s 5(2)).
SSO marked the retrieval "Current version as at 01 Oct 2026". Section numbers follow
the body: the arrangement of sections printed at the top of the deposit is one line
out of step with its headings (it lists "1." with no heading and "2. Short title").

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0212** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is short (ss 1-9) and almost all of it is about the State and the company.
This row encodes nearly the whole of it, read from the side of the person who meets
it: what the company may award (s 3), the Minister's directions (s 3B), trustees
(s 4), the consent rule and its consequence for anyone dealing with the company
(s 5), the limit on public money (s 6), records and the information offence (s 7),
student bodies (s 8) and the Act's priority over the company's own documents (s 9).
Not encoded: s 3A (accountability and quality-assurance frameworks and external
review panels, duties owed to the Minister with no consequence stated), the
Minister's duty to pay in s 6(1), the published financial summary in s 7(3), and
the content of any exemption order under s 8(2).

## What the Act turns out to say

### 1. A deal the Minister did not consent to beforehand is void, not merely irregular

s 5(1) requires "the prior written consent of the Minister" for admitting or removing
a member of the company, disposing of the whole or substantially the whole of its
undertaking or property, a voluntary winding up, any change to the constituent
documents, and removing a trustee. s 5(3): an act or agreement in contravention "has
no effect and is unenforceable at law". A buyer of substantially the whole
undertaking without that consent gets nothing enforceable. The Act says nothing
about ratification; the encoding reads "prior" as leaving a later written consent
ineffective, and "written" as leaving a prior oral one ineffective (both inferences
from the words). Selling one building, conferring an honorary degree and an ordinary
supply contract are outside the list. Asserted.

### 2. Anyone, not only the company, can be made to hand over information, and a $1,000 fine backs it

s 7(2) lets the Minister or an authorised person "require any person" to provide
information in their possession or to which they have access, for checking how s 6
money was spent "and any other matters". s 7(4): failing without reasonable excuse,
or otherwise hindering, obstructing or delaying, is an offence with a fine "not
exceeding $1,000"; no imprisonment is provided. The encoding reads "without
reasonable excuse" as attaching to the failure to comply only, not to the hindering
limb (a reading, not a decided point). Asserted.

### 3. The Minister appoints and removes trustees, yet the Act also requires the Minister's consent to remove one

s 4(1) and (2): the Board consists of the trustees the Minister appoints, and the
Minister may remove or replace any trustee "at any time". s 5(1)(e) separately
requires the Minister's prior written consent for "the removal of any trustee". The
encoding reads (e) as aimed at a removal by the company or its members, which needs
that consent and is otherwise void under s 5(3) (an inference; the Act does not say
who else might remove a trustee). Asserted.

### 4. Public money is tied twice: to the company's objects and to the Minister's allowance

s 6(2): money paid under s 6(1) "may only be applied or expended ... for such objects
provided by its constituent documents as the Minister may allow". An object in the
memorandum is not enough without the Minister's allowance, and vice versa. Money
from other sources is outside s 6(2). Asserted.

### 5. Student bodies are societies, unless gazetted out

s 8(1): "despite anything to the contrary" in the Societies Act 1966, that Act applies
to any student body constituted under the company's constituent documents; s 8(2)
lets the Minister for societies exempt one by Gazette order from all or any of its
provisions, on conditions. The encoding treats only a whole exemption as taking the
body out. Asserted.

### 6. The company's own documents yield to the Act, but the Act excuses it from nothing else

s 9(1): a provision of the constituent documents, or a regulation under them,
inconsistent with the Act is void to the extent of the inconsistency. s 9(2): nothing
in the Act excuses the company from any other written law that would otherwise apply.
s 3 names degrees, diplomas, certificates, honorary degrees and other distinctions as
what the company confers. Asserted.

## What would need doing before this is worth anything

- The constituent documents (memorandum and articles) were not deposited; s 3, s 6
  and s 8 all turn on them.
- No accountability agreement, quality-assurance framework, direction under s 3B or
  Gazette order under s 8(2) was retrieved.
- No case law was searched, in particular on the reasonable-excuse reading of s 7(4)
  and on ratification under s 5.
