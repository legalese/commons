# Saint Andrew's Mission Hospital Ordinance 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SAMHO1934.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021". The latest amendment annotated in
the body is [40/2019] on s 35 (Supreme Court of Judicature (Amendment) Act 2019, in
force 2 January 2021, per the Legislative History).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0247** in `subjects/sg/requirements.jsonl`: Tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance incorporates a hospital, so the people it reaches are its
subscribers and members. This row takes membership (ss 7-9), what may be paid to
members (s 6), who may stand for the Board (ss 18, 22), the annual and special
meetings (ss 29, 30), rule changes (ss 33, 34), winding up (s 35), and the meeting
rules in the Second Schedule (rules 1, 2, 4, 9, 14, 15).

Not encoded: incorporation and the vesting of the Erskine Road land (ss 2-4), the
objects (s 5), the named Founder, Patrons and first office-holders, the Treasurer,
auditor and Chaplain (ss 10-17), the Bishop's control of medical officers and nursing
sisters (s 25), the Board's powers and committees (ss 26-28, 31), and the First
Schedule endowments.

## What the Act turns out to say

### 1. A $12 subscription buys up to two years' membership; $500 buys it for life

s 7(3): $12 subscribed "in any calendar year" entitles the subscriber to be a member
"for the residue of that year, and the next following year". s 7(2): $500 in the
aggregate (or a name in the Register of Subscribers) makes a permanent member, "for
life or in the case of a firm or corporation till the dissolution". Firms and
companies can be members. Reading "$12" and "$500" as minimums is an inference. Asserted.

### 2. Two different super-majorities: two-thirds of those voting, three-fourths of the Board

s 33: a rule change needs "not less than two-thirds of the members voting on the
question" (after due notice to the Board), and s 34 adds that it does not operate until
approved by the Minister and published in the Gazette. s 35: the body that receives the
surplus on a winding up is chosen "by a majority of three-fourths of the Board of
Management", with the approval of the Society for the Propagation of the Gospel, and in
default by the General Division of the High Court. The encoding reads s 35 as
three-fourths of the whole Board, not of those voting: an inference from the wording.
Asserted.

### 3. Members never take the money, even at the end

s 6 forbids paying income to members "by way of dividend, bonus or otherwise howsoever by
way of profits", but allows good-faith pay for services actually rendered, interest on a
member's loan, and an annuity to a donor on the gift for no longer than the donor's (or
nominee's) life. s 35: on a winding up the surplus "shall not be paid or distributed
amongst the members" and goes only to a Church of England missionary body within the
Diocese of Singapore with similar objects. Asserted.

### 4. Ten members can force a special meeting

s 30: a requisition signed by at least 10 members stating its objects obliges the Board
to summon a meeting to be held between 3 and 6 weeks after receipt; if the Board neglects
to do so "within 14 days", the requisitionists may summon it themselves. The encoding
lets them act from day 15 (inference). Asserted.

### 5. A salaried officer cannot be elected to the Board

s 22: elective members are chosen from the members, "but no person shall be eligible for
election whilst holding any salaried office under the Corporation", though s 13 lets the
Treasurer, who sits on the Board ex officio (s 18), be salaried. Asserted for s 22.

### 6. Membership dies with the member

s 9: "not transferable or transmissible"; s 8(2): a member retires by writing to the
Secretary. Membership also needs the member's consent (ss 7(1), 8(1)). Asserted.

## What would need doing before this is worth anything

- Whether the Board has made, and the Minister approved, rules replacing the Second
  Schedule (ss 31-34) was not checked; any such rules would override the Second Schedule rules encoded here.
- Whether the Corporation still operates under this Ordinance, or how its subscriptions
  work today, was not looked into.
- No case law was searched.
