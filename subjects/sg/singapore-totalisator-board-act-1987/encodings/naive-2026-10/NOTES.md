# Singapore Totalisator Board Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions as shown in the example rows, and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1/8/2022, as deposited at `../../registers/source-bundle/STBA1987.txt`. The latest
amendment annotated in the body is Act 14 of 2022 wef 01/08/2022 (s 15(1)(a) carries
Act 1 of 2022 wef 29/07/2022). The meta file records the version as current at
1 October 2026. The arrangement of sections at the top of the deposit is out of step
with the body; the encoding follows the body (admission to race courses is s 17,
ss 18 to 22 repealed, exemption s 23, regulations s 24, Turf Club trust s 25).

**Checks:** one module, one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0147**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. This row takes what a
punter, racegoer, turf club or totalisator agency meets: the dividend duty and what
the Board keeps (ss 15, 16), what the Board may and may not do (ss 4(1), 4(4), 5(1),
9(2)), admission, removal and by-laws at race courses (s 17), the financial year
(s 14), and Board composition, disqualification, vacation, quorum and voting (s 7(1);
Schedule paras 8, 10, 12(2), (3)). Not encoded: incorporation, ministerial directions
and information, staff, banking, investment, shares and borrowing (ss 3, 4(2), (3),
6, 8 to 13), the s 23 exemption, s 24 regulations, the Turf Club trust (s 25) and the
rest of the Schedule. The commission rates live in regulations that were not
retrieved, and the Gambling Duties Act 2022 was not read, so duty and commission are
inputs.

## What the Act turns out to say

### 1. The Board supervises racing and betting but may not run either itself

s 4(4), annotated Act 14 of 2022 wef 01/08/2022: "nothing in this Act confers on the Board a function
or power to conduct on its own behalf any race meeting or a totalisator for gaming".
Yet s 5(1)(c) lets it suspend or revoke any totalisator or gaming activity of an
agency it supervises. Asserted.

### 2. Everything left after duty and commission belongs to the punters

s 15(1) makes it the agency's "duty" to pay out as dividend all money received after
deducting gambling duty and the prescribed commission. The only slack is s 15(2):
fractions of a dollar need not be paid. Reading the pool as a whole (an inference;
the text does not say per ticket or per pool), paying out a dollar or more short
breaches the duty, and so does paying out more than the pool. Asserted.

### 3. The leftover fractions go to the Board, not the agency

s 16 deems the commission and the unpaid fractions to "belong to and form part of
the general funds of the Board", apportioned with the agency only as the Minister
approves. On $100,000.75 received, $30,000 duty and $5,000 commission, a $65,000
payout leaves $5,000.75 in the Board's funds. Asserted.

### 4. Appointing a betting agency needs the Minister

s 9(2)(b): the Board must obtain the Minister's approval to appoint any totalisator
agency; s 4(1)(d) likewise for recreation facilities on Board land. Asserted.

### 5. Surplus may go only to Singapore causes

s 5(1)(a) lets the Board distribute money not required for its s 4 functions, for
public, social or charitable purposes "relating to Singapore" or for culture, art and
sport "in Singapore". The encoding reads an overseas appeal as outside both limbs (an
inference). Asserted.

### 6. A racegoer can be removed only after being asked to leave

s 17(5): a turf club officer may remove a person who contravenes a by-law **and**
fails or refuses to leave after the officer's request. The club may charge admission
even where the course carries a public right of entry (s 17(4)(a)). Every by-law must
be on the Singapore Turf Club website and displayed on the premises within 30 days of
coming into operation (s 17(6)), and is void to the extent it is inconsistent with
Singapore law (s 17(7)). Asserted.

### 7. Board seats: 4 to 11 members besides the Chair; six months' prison disqualifies

s 7(1) fixes the size. Schedule para 10 bars an undischarged bankrupt, anyone with an
arrangement with creditors, and anyone sentenced to 6 months or more without a free
pardon; para 8 vacates the seat after 3 consecutive meetings missed without leave. A
majority forms a quorum and the presiding member has a casting vote on a tie (para
12(2), (3)). Asserted.

## What would need doing before this is worth anything

- Retrieve the regulations under s 24 that prescribe the commission, and read the
  Gambling Duties Act 2022 for the duty.
- Settle whether s 15(2) operates per ticket or per pool.
- Ministerial exemptions under s 23 could displace any of this for a given person.
- No case law or Board practice was searched.
