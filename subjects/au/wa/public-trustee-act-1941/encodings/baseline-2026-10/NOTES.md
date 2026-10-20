# Public Trustee Act 1941 (WA) — baseline encoding

## Method

A baseline encoding. It was written straight from the deposited text with the
writing-l4-rules skill, from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18.

- No pipeline, no coverage table, no independent test pass, no human gate.
- No REFUSE, `#ASSERT REFUSED` or BECAUSE; the stable l4 rejects them.
- Every decision carries `@export` and `@desc` for Legalese Cloud.
- Expected values in the case file were written by hand from the text. The generator
  is `gen_wa_public-trustee-act-1941_baseline.py` in the session scratchpad.

Files:

- `pta-small-estates.l4`: the module.
- `pta-cases-small-estates.l4`: the worked cases.

Not for public use as advice.

## Edition

- **The Act:** the compilation incorporating amendments up to the Statutes (Repeals and
  Minor Amendments) Act 2025 (No. 14 of 2025, s 33, in operation 26 September 2025,
  deleting s 15). The Liquor Control Amendment Act 2025 Pt 5 Div 3 is listed as
  uncommenced; it does not touch the sections encoded. Deposited at
  `../../registers/source-bundle/mrdoc_49053.txt` (legislation.wa.gov.au law_a649,
  retrieved 7 September 2026).
- **The Public Trustee Regulations 1942:** version 04-b0-08, in force from 1 July 2008,
  deposited at
  `../../../public-trustee-regulations-1942/registers/source-bundle/mrdoc_7511.txt`
  (retrieved 20 October 2026). Used: reg 10A ($1 500 for s 45(2)) and Forms 3, 3A, 3B
  and 4 (the s 14 election and its revocation).
- **Not deposited, so inputs:**
  - the s 14 prescribed amount. By s 14(6) it is the amount prescribed for Trustee
    Companies Act 1987 s 10, set by regulations under that Act;
  - the Public Trustee's scale of fees, which s 38A requires to be published in the
    Gazette.

## Checks

With the stable l4 from VS Code extension 1.6.98:

- `l4 run pta-cases-small-estates.l4`: 44 assertions written, 44 satisfied, 0 errors,
  0 warnings.
- `l4 run pta-small-estates.l4`: 0 errors, 0 warnings.

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

## Seat

**The next of kin of a person who has died leaving a small estate in Western
Australia.** This is the child, spouse, parent or other relative who would otherwise
take out the grant. For ss 7-8 the seat is the will-maker who appoints the Public
Trustee as executor.

Why this seat: the Act speaks almost entirely to the Public Trustee and the Court. The
person it is applied to is the family. They ask whether a stranger may take over the
estate without a grant, whether they can hand it over themselves, what it will cost,
and what happens to a child's share or to money nobody claims. Every decision is
phrased as they would ask it.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Public
  Trustee Regulations 1942 are used for reg 10A. They do not set the s 14 amount (see
  finding 2), and the instrument that does is not deposited, so it is an input. The
  fee scale is an input too.
- **The actors the text names.** Followed: the Public Trustee, the Court, the executor,
  "the person first entitled to the administration", the persons entitled to obtain
  administration, a creditor, the next of kin, a parent or carer of an infant, and a
  client.
- **A judgment handed to someone else, answered conditionally.** Followed:
  - the Court's view under s 10(1)(d) and (g);
  - the creditor proving "to the satisfaction of the Court" under s 11;
  - the Public Trustee's estimate of gross value (ss 10(4), 14(1));
  - the Public Trustee's waiver under s 38B(9), taken as the amount waived.
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.**
  Followed:
  - "client" (s 2) is worked out;
  - "administration ... include[s] an order to administer" (s 2) is applied;
  - "the person first entitled to the administration" belongs to the Administration
    Act 1903 s 25 and is asked as a fact.
- **One case is the text's natural unit.** Followed: one deceased person's estate.
- **The Act's own terms, each with a plain gloss.** Followed, in the comments.
- **Operative sections in; machinery out.** Followed. Out: ss 1-6B, 37B-37C, 39-44A,
  46-48 and 64-65, plus trust, represented-person and investment provisions the seat
  does not meet.

## The lives

- **jake k098 (2 May 2079).** Jake dies at 72, divorced, with no will, leaving "an
  estate of $38,000 and the apartment". Ruby, 46, takes all. The event asks "may the
  Public Trustee act".
  - The apartment's value is the encoder's $600,000, as in the Administration Act 1903
    baseline, so the gross value is $638,000.
  - That Ruby lives in WA and is willing to administer is assumed, as that baseline
    assumed.
  - `On what ground may the Public Trustee apply`:
    - a fortnight after the death, with Ruby not authorising it: no ground;
    - with Ruby's authority: s 12;
    - after 3 months with no application: s 10(1)(c);
    - if Ruby lived overseas: s 10(1)(ab).
  - `May the Public Trustee administer without a grant` (s 14):
    - yes with Ruby's authority, if the prescribed amount is at least $638,000;
    - no if it is a dollar less;
    - no without a ground to apply, however high the amount;
    - no once Ruby has taken out letters of administration.
  - `May the Court grant administration to me instead`: yes for Ruby in WA.
  - Ruby would be a client (s 2) if the Public Trustee administered the estate.
  - The fees come out of the estate (ss 38B(4), 62).

## Why this scope

The event needs the s 10 grounds and the s 14 election. The seat also meets:

- s 12, handing the estate over;
- the (ab) proviso, the family's own priority;
- s 11, creditors;
- ss 7-8, the Public Trustee as executor;
- s 18, a child's share under $5 000;
- the fee sections (ss 9, 38A-38B, 47A, 62);
- s 45, unclaimed balances. This is the one place the deposited regulations set a
  number.

Out:

- the Court's conditions and the Gazette notices (s 10(2), (3), (6), s 14(3));
- transfer after a grant and the consents (s 12(4)-(8));
- the agent route (s 12A) and removal of an executor (s 13);
- interstate balances and escheat (ss 16-17);
- trusts, represented persons, the Common Account and investment (except s 38B(8));
- deposit of wills and inquiries (ss 54-55);
- liability and evidence (ss 56-61, 63);
- machinery.

## What the Act turns out to say

1. **The small-estate rule is s 14, not s 10.** The event cites s 10, "administration
   of small estates", for "a small estate, no grant". But s 10(1) is the Public
   Trustee's application for an order to administer. By s 2 that order is itself a
   grant ("administration ... include[s] an order to administer"). Going without any
   grant is the s 14 election. The only dollar figure in s 10 is the $10 000 of
   s 10(4). It applies only to an estate left part-administered after every grantee
   has died ("de bonis non"). Asserted.
2. **The s 14 amount is not in the Public Trustee Regulations.** s 14(6): "prescribed
   amount means the amount prescribed for the purposes of section 10 of the Trustee
   Companies Act 1987". The Public Trustee Regulations 1942 prescribe only one amount.
   That is reg 10A, $1 500, and it is for s 45(2), the advertising of unclaimed money.
   The s 14 figure sits in regulations under the Trustee Companies Act, which are not
   deposited. Whether Jake's estate is small enough therefore cannot be answered from
   the deposit. With the apartment the estate is $638,000 on the encoder's figure; the
   cash alone is $38,000. Asserted at the boundary.
3. **The election needs a ground to apply.** s 14(1) is available only "in all cases
   where he is entitled to apply for an order to administer". With Ruby in WA, willing
   and not consenting, the Public Trustee has no ground during the first 3 months.
   That is so however small the estate. It gets one if Ruby authorises it (s 12(3)),
   or once 3 months pass without an application (s 10(1)(c)). Asserted.
4. **The family keeps priority.** Under the (ab) proviso, the Court may still grant
   administration to an entitled person in the State who applies. This matches the
   Administration Act 1903 baseline: the Public Trustee may not be granted
   administration under that Act's s 25(1)(b) while Ruby is resident and fit. Its
   route is this Act, by Ruby's authority or after 3 months. Asserted.
5. **"Any person or the majority" (s 12(1)-(3)) is ambiguous.** The encoding reads it
   as the one person where there is one, and a majority where there are several. Two
   of four children is not enough on that reading. On the other reading any one of
   them could act alone. This is an inference. Asserted on the reading taken.
6. **The election is undone if the estate grows, if property outside WA turns up, or
   if a will turns up.** Under s 14(4), if the value is found to exceed the amount or
   property outside the State is found, the Public Trustee must go to the Court for an
   order. Section 14(1) itself does not exclude an estate with property outside WA;
   only s 14(4) does. Under s 14(5), a will found for a supposed intestate revokes the
   election, and accounts must be filed. Asserted.
7. **What may be charged.**
   - No charge for the estate vesting in the Public Trustee before a grant (s 9).
   - No fee on Common Account interest (s 38B(8)).
   - No will-drafting fee unless a legal practitioner directs and controls the work
     (s 47A(2)).
   - Otherwise, fees up to the latest scale gazetted before the work began
     (s 38B(1)). An ungazetted scale "has no effect" (s 38A(2)).
   - A fee the will directs, or one agreed with the Public Trustee, may be "in
     addition to or instead of" the scale fee (s 38B(2)).
   - Expenses and tax-return work come on top (s 38B(3), (6)).
   - Fees are paid out of the estate and are "deemed to be a testamentary expense"
     (s 38B(4), s 62).
   Asserted.
8. **A child's share under $5 000 may go to a parent or carer** without the Public
   Trustee seeing to its use (s 18). The figure is "under $5 000", so $5 000 itself
   is out. Asserted.
9. **Unclaimed money goes to the State after 6 years** with no knowledge of anyone
   entitled (s 45(1)). If it is $1 500 or more (reg 10A) it must first be advertised
   twice, 14 days apart, in a Perth newspaper (s 45(2)). Asserted.

## What would need doing before this is worth anything

- Deposit the Trustee Companies Regulations and read the s 10 amount in force. Then
  answer k098 outright rather than at the boundary.
- Deposit the Public Trustee's current gazetted scale of fees and encode it as a
  table.
- Settle the s 12 "any person or the majority" reading against case law or practice.
- s 10(1)(c) says "not applied for", and the encoding uses "no grant taken out". A
  pending application is not distinguished.
- Encode s 12(4)-(8), s 12A and s 13 if the seat is widened to executors who want to
  hand over an estate already granted.
- An independent test pass and the human gates.
