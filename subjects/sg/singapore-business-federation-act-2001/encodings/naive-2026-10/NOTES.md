# Singapore Business Federation Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which by its own statement "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotated in the body is [33/2018], against
s 12(4). Deposited at `../../registers/source-bundle/SBFA2001.txt`.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is requirement **REQ-0207** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. For a business the answer is s 5 (membership without joining)
and s 12 (what it can be made to pay). The Act is 13 sections and a Schedule; this row
takes ss 4, 5, 7(2), 8(2)-(3), 9, 10, 11, 12 and the Schedule. Not encoded: s 3
(objects), s 6 (the Minister's appointment of trustees), s 7(1), s 8(1), (4), (5) and
s 13. No Ministerial order, regulation, subscription schedule or copy of the
Federation's Constitution was retrieved.

## What the Act turns out to say

### 1. A company can be a member without ever joining

s 5(1): a qualifying company "becomes, by virtue of this section and without election,
admission or appointment, a member of the Federation". Membership ends only if
"terminated in accordance with the Constitution of the Federation" or the company is
exempted by Ministerial order (s 5(2)(a)). Asserted.

### 2. Local and foreign companies are measured by different capital

A local company qualifies on **paid-up** share capital of $500,000 or more; a foreign
company on **authorised** share capital of $500,000 or more (s 5(1)(a), (b)). A local
company with $5 million authorised but $100,000 paid up is not a member; a foreign
company with no paid-up capital but $500,000 authorised is. The threshold is "of or
above", so exactly $500,000 qualifies. Sole proprietorships, partnerships and LLPs
are outside s 5 entirely. (Inference, not in the deposit: whether foreign companies
still report an authorised capital under the current Companies Act was not checked.)
Asserted.

### 3. The subscription is compulsory, capped at $1,500 a year, and a debt

s 12(1): a statutory member "must pay" a subscription set by the Council after
consulting the Board and approved by the Minister. s 12(3): the amount "must not exceed
in the aggregate $1,500 in any calendar year". s 12(4) (added by 33/2018): it may be
recovered "by an action for a debt". The encoding counts subscriptions only toward
the cap; whether interest under s 12(2)(d) counts is not said (inference). Asserted.

### 4. Anyone can be made to produce information, on pain of a $1,000 fine

s 9(2) lets the Board or an authorised person require "any person" — not only members
— to furnish information about the Federation's funds. Failing without reasonable
excuse, furnishing what one "knows or has reason to believe is false", or hindering the
Board is an offence with a fine not exceeding $1,000 and no imprisonment (s 9(3)). The
text does not say who bears the burden of the reasonable excuse. Asserted.

### 5. Foreign chambers get a ceiling, not a floor

s 4(1)(b) requires "such number of representatives from foreign chambers ... not
exceeding one-quarter" of the Council. Read literally, zero satisfies it. The three
local ethnic chambers in the Schedule (Chinese, Indian, Malay) must each have a
nominee. Asserted.

### 6. The Minister holds the strings

The Minister appoints and removes every trustee (s 6, not encoded), approves the
subscription (s 12(1)(b)), can exempt companies and move the threshold (s 5(2)), and
must approve any dissolution beforehand (s 10(1)). The Board approves the budget,
accounts, Council appointments, Constitution amendments and property dealings above a
value it sets (s 7(2)). Any inconsistent provision of the Constitution is void (s 11).
Asserted.

## What would need doing before this is worth anything

- Any order under s 5(2) (exemptions, a changed threshold) and s 4(2) (Schedule
  changes) must be found; the encoding assumes the printed $500,000 and Schedule.
- The current subscription schedule and the Federation's Constitution (termination of
  membership, interest on arrears) were not retrieved.
- Whether "authorised share capital" still has content for foreign companies under
  the Companies Act 1967 needs checking.
