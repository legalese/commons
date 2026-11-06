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
- **The Trustee Companies Regulations 1988:** version 01-b0-06, in force from
  5 January 2013, deposited at
  `../../../trustee-companies-regulations-1988/registers/source-bundle/mrdoc_24509.txt`
  (legislation.wa.gov.au law_s4830, retrieved 21 October 2026). Used: reg 4, "For the
  purposes of section 10 of the Act the amount prescribed is $50 000", which s 14(6)
  makes the s 14 prescribed amount. Added 21 October 2026; until then the amount was an
  input.
- **Not deposited, so an input:** the Public Trustee's scale of fees, which s 38A
  requires to be published in the Gazette.

## Checks

With the stable l4 from VS Code extension 1.6.98:

- `l4 run pta-cases-small-estates.l4`: 48 assertions written, 48 satisfied, 0 errors,
  0 warnings (44 before the Trustee Companies Regulations were deposited).
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
  finding 2); the Trustee Companies Regulations 1988 do, in reg 4, and are used for
  it. The fee scale is not deposited and is an input.
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
  - `May the Public Trustee administer without a grant` (s 14, reg 4):
    - no: the $638,000 estate is over $50 000, even with Ruby's authority or after
      3 months;
    - for the $38,000 alone: yes with Ruby's authority, or after 3 months with no
      application; no a fortnight on without her authority;
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
   The s 14 figure sits in the Trustee Companies Regulations 1988 (not "1987", the
   Act's year), reg 4: $50 000. So Jake's estate, $638,000 with the apartment on the
   encoder's figure, cannot be taken over by election; the cash alone, $38,000, could
   be. Exactly $50 000 is within ("does not ... exceed"); $50 001 is not. Asserted.
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
10. **The $50 000 has not moved since 1988.** Reg 4 carries no amendment note, and the
    compilation table lists no amendment touching it, so the amount has stood since
    the Regulations commenced on 1 September 1988. s 14(6) takes the amount "for the
    relevant time", so an election in 2079 (k098) uses whatever reg 4 then says; the
    encoding uses the deposited $50 000. Asserted for the deposited figure.

## What would need doing before this is worth anything

- Re-check reg 4 of the Trustee Companies Regulations 1988 when the deposit is
  refreshed: the $50 000 is a constant here, and replacing the input with it changed
  the inputs of the two s 14 questions (a breaking change for any deployment).
- Deposit the Public Trustee's current gazetted scale of fees and encode it as a
  table.
- Settle the s 12 "any person or the majority" reading against case law or practice.
- s 10(1)(c) says "not applied for", and the encoding uses "no grant taken out". A
  pending application is not distinguished.
- Encode s 12(4)-(8), s 12A and s 13 if the seat is widened to executors who want to
  hand over an estate already granted.
- An independent test pass and the human gates.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026, after the model of the Graffiti Vandalism Act 2016 encoding's seat layer (its design decisions D2, D4 and D8). The baseline's files are unchanged: the layer is added, nothing is replaced. Two new files:

- `pta-qa.l4` imports `prelude` and `pta-small-estates`. It has 24 exported questions.
- `pta-qa-cases.l4` imports the same and `pta-qa`. It has 189 cases.

### Roles

`DECLARE Role IS ONE OF`:

- `I am next of kin of someone who has died`: the baseline's main seat (all 17 of its questions).
- `I am making a will, or have made one`: the baseline's ss 7-8 seat, with s 47A and s 2(c) (3 questions).
- `I am a beneficiary of an estate or trust the Public Trustee administers`: a client under s 2(a), (e), asking about fees and unclaimed money (5 questions).
- `I am owed money by someone who has died`: the creditor s 11 sets against the Public Trustee (1 question).

Why: the Act speaks to the Public Trustee and the Court; the people it is applied to are the family, the will-maker, the beneficiaries of what the Public Trustee administers, and a creditor who wants to administer. The Public Trustee and the Court are not seats. "Am I a client of the Public Trustee" is one question with a branch for each of the first three roles, since s 2 answers it for all of them. Every exported question takes `my role` IS A Role first, with `@desc Which of these describes you`, and for a role it is not about answers `does not arise for you` without reading any other input.

### Situation input

| Input | Type | Does not arise when | Taken by |
|---|---|---|---|
| `the Public Trustee's part in the estate` | `The Public Trustee's part` (`none yet`; `it has filed a small-estate election (s 14)`; `it administers the estate under an order to administer, a grant, or as executor`) | `none yet`, for all 8; also `it administers the estate under ...`, for the two questions of s 14(4) and (5), which speak "after filing such election" | next of kin: `Must the Public Trustee seek an order after all`, `Must the election be revoked and accounts filed` (s 14(4), (5)); `May the Public Trustee pay my child's share to me` (s 18); `May the Public Trustee charge for this`, `What is the most the Public Trustee may charge`, `Are the fees paid out of the estate` (ss 9, 38A, 38B, 47A, 62); `Must the Public Trustee advertise the unclaimed sum`, `May the sum go to the Consolidated Account` (s 45) |

It is the second input, straight after `my role`, with one name, type and `@desc` everywhere, so the form asks it once. The two helpers that read it list all three values with no OTHERWISE (graffiti finding 31). The questions of whether the Public Trustee may take the estate on (ss 8, 10, 10(4), 11, 12, 14(1)) arise in every situation and take none. The will-maker, the beneficiary (whose role already says the Public Trustee administers) and the creditor have no situation input.

### Decisions

- **QA-1. The situation is what the Public Trustee has done, not what the family has done.** The Act ties s 14(4)-(5) to the election having been filed, and s 18, the fees and s 45 to the Public Trustee holding the estate (s 14(2) deems the election a grant). s 18's own input `the Public Trustee holds the grant` was at first kept, as the baseline asks it; since the situation already settles it, so that an answer could contradict the situation, the layer now passes it as TRUE (fix of 6 November 2026), and the answer equals the baseline's with that input TRUE.
- **QA-2. One `@desc` for `the family`.** The baseline gives the same input two `@desc` texts in different questions; the layer gives every question one, so the form asks it once. Since QA-5 it is the layer's own record, with the `@desc` "What the family is doing, and who has authorised the Public Trustee".
- **QA-3. The will-maker's fee question builds the baseline's enumeration.** `May the Public Trustee charge me for preparing my will` asks only whether a legal practitioner directs and controls the preparation, and picks the baseline's `What the charge is for` value from it (s 47A(1)-(2)).
- **QA-4. The creditor's answer is the baseline's s 11 answer turned round.** The creditor is preferred exactly when the Public Trustee is not, that is when the creditor proves to the Court it would be more beneficial.
- **QA-5. Whether there is a will, and who will act, is one choice (fix of 6 November 2026).** The site's form drops a question for a role it is not about only by trying every combination of its open yes/no and choice inputs, at most 1,024 of them. The s 10(1) ground, the s 10(1) "may apply" and the s 14(1) election questions took the baseline's `The estate`, `The family` and `What the Court thinks`, with 12 yes/no facts: 4,096 combinations, so the will-maker, the beneficiary and the creditor were shown all three. Five of those facts say one thing: `the deceased left a will`; `an executor named in the will is willing, capable and resident in WA` and `the will expressly prohibits the executor authorising the Public Trustee` (both only with a will); `the person first entitled to administration is willing, capable and resident in WA` (s 10(1)(ab), "dies intestate"); and `the executor renounced and everyone first entitled declined in writing filed in Court` (s 10(1)(b), an executor, so a will). The layer asks them as one choice of eight, `The will and who will act` (two with no will, six with one), a field of its own record `The estate, as the next of kin knows it`; the family's other facts are its record `What the family is doing`. `the estate as the Act puts it` and `the family as the Act puts it` build the baseline's records; a fact the baseline's rules do not read in a value (the executor with no will, the person first entitled with a will) is given a fixed value that changes no answer. The four questions that take them (s 12 too) now have at most 1,024 combinations. A scratchpad script (`probe.py`) counts them for every question of the layer. The cases put the baseline's fixtures through a converter (`the layer's estate`, `the layer's family`) and compare with the baseline on the fixtures themselves; 14 more ask the s 10(1) ground for each of the eight values and s 12 for six.

### Not covered for the new roles

- Will-maker: deposit of wills (s 54) and the Public Trustee as trustee of a will trust (Division 3 onwards): out of the baseline's scope.
- Beneficiary: the Common Account and investment, represented persons, accounts and inquiries (ss 55-61); a beneficiary's claim against the Public Trustee.
- Creditor: the order of payment of debts and an insolvent estate: not in this Act's encoded sections (the Administration Act 1903 has them, also not encoded).

### Cases

189 in `pta-qa-cases.l4`, all satisfied, with 0 errors and 0 warnings:

- 70 ask each question for each role it is not about, every other input ASSUMEd: `does not arise for you`;
- 10 ask each situation question, for its own role, with each value that makes the situation not hold, every later input ASSUMEd: `does not arise for you`;
- 20 assert that the next of kin's or will-maker's answer equals the baseline export's on the same facts (one for each of the 17 next-of-kin questions and the 3 will-maker questions);
- 89 are worked by hand from the text, for all four roles, with the baseline's fixtures (Jake's death, k098, and the encoder's fee figures).

Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset: `pta-qa.l4`, `pta-qa-cases.l4`, and the baseline's `pta-small-estates.l4` and `pta-cases-small-estates.l4` (48 of 48, unchanged) give 0 errors and 0 warnings; `l4 check pta-qa.l4` succeeds. A script listed every `@export` of `pta-qa.l4` with its inputs and checked that `my role` is first in all 24, that the situation input (and every other shared input) has one name, type and `@desc`, and that no input is DEONTIC or EVENT. A negative control (one expected fee altered) was caught. The mechanical cases are generated by the scratchpad script `gen_pta.py` from the layer's own `@export` list.
