# Central Sikh Gurdwara Board Act 1981 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), deposited at `../../registers/source-bundle/CSGBA1981.txt`. The deposit
says it incorporates all amendments up to and including 1 December 2021; the latest
amendment annotated is to s 17, "[Act 25 of 2021 wef 01/04/2022]".

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0145**: Tier 2 of the remaining Singapore Acts, ordered
by everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The Act has 18 short sections and most of it is encoded: the Membership Register and
who may vote and stand (ss 3, 5, 11), terms, casual vacancies and the Treasurer's limit
(ss 3(2), 4(1), 6), quorum and voting (ss 7, 8), sealing (s 2(3)), property (s 12),
accounts (s 14), members' liability (s 15) and service of process (s 17). Not encoded:
incorporation (s 2(1)-(2)), minutes (s 10), the bank and use of funds (s 13), the
rule-making power (s 16) and the saving clause (s 18). No rules made under s 16 were
retrieved, so the conditions and fees for entry on the Register are unknown.

## What the Act turns out to say

### 1. The quorum, read literally, is always met

s 7(1): "50% of the members present shall form a quorum". The fraction is of those
*present*, not of the Board, so any meeting at which someone turns up has a quorum,
and the size of the Board plays no part. That the drafter meant half the Board is an
inference the text does not support on its face. The encoding takes the literal
reading (a Board of 15 with 2 present is quorate). Asserted.

### 2. Voters need only be on the Register; candidates must also be citizens

s 3(1) gives the vote to "persons whose names appear on the Membership Register",
which s 5 defines as persons "who profess the Sikh faith". s 3(3) adds, for election
or appointment only, that the person must be "a citizen of Singapore". A permanent
resident on the Register may vote but not stand. Asserted.

### 3. Losing citizenship does not unseat a member; s 11 does

s 3(3) speaks only of being "elected or appointed". s 11, by contrast, applies to
anyone who would "continue to hold office": an undischarged bankrupt, a person who
"makes any arrangement or composition with his creditors", a person sentenced to
imprisonment of "not less than 6 months" without a free pardon (with no time limit),
and a member whose removal an extraordinary general meeting has called for. Read
literally, a sitting member who stops being a citizen or leaves the Register keeps
the seat (a reading; s 6 "otherwise vacates" is not defined). Asserted.

### 4. Land needs the members' general meeting first; building on it does not

s 12(a) and (b) forbid the Board to acquire, lease, sell, mortgage or let immovable
property "without a resolution being first passed at a general meeting" of Register
members. Movable property needs no such resolution, and neither does s 12(c),
erecting buildings on the Board's land. Acquisitions and building must be for a
temple purpose; disposals carry no purpose test. Asserted.

### 5. Members are never personally liable for the Board's debts

s 15 has two limbs. Acts "in good faith and without gross negligence as such member"
are protected; the Board's own "debt, liability, act or omission" is protected with no
good-faith condition at all. Asserted.

### 6. Smaller rules

The Treasurer may not serve "more than 2 years consecutively" (s 4(1)). A member
holds office for 2 years but stays until a successor is elected (s 3(2)); a casual
appointee serves only "the residue of the term" (s 6). A tie is broken by the
presiding person's casting vote (s 8(2)), and the Board is bound by any general
meeting resolution (s 7(2)). Deeds are sealed before, and signed by, the President,
Treasurer and Secretary (s 2(3)). Accounts are annual, signed by the Treasurer and
audited by two Register members elected at the *biennial* general meeting (s 14).
Process may be served on an official, or left at or sent by registered post to the
Central Sikh Temple (s 17). Asserted.

## What would need doing before this is worth anything

- The Board's rules under s 16 (Register conditions and fees, elections, meetings)
  were not retrieved; they decide most of what a member actually meets.
- "Majority of the members present" (s 8(2)) is read as more votes for than against;
  abstentions are not modelled. "2 persons" in s 14(2) is read as exactly two.
- Whether s 17 excludes other methods of service, and whether loss of citizenship
  vacates office, were not researched. No case law was searched.
