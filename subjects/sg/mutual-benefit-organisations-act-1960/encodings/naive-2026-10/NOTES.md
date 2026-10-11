# Mutual Benefit Organisations Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions as shown in the example rows, and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MBOA1960.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and is headed "Informal Consolidation
– version in force from 1/11/2024". The latest amendment annotated in the body is Act
30 of 2024, in force 1 November 2024 (s 48(1), the Platform Workers Act exemption).
The meta file records it as the current version at 1 October 2026. The arrangement of
sections at the top of the deposit falls out of step with the body from s 32 on; the
body's numbers are used throughout.

**Checks:** one module, one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0146** in `subjects/sg/requirements.jsonl`: tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The row takes what a member, officer, nominee or organiser meets: what counts as a
mutual benefit organisation and the duty to register (ss 2, 4(1), 37, 48(1)); refusal
of registration (s 6); which decisions can be appealed (ss 7, 9(3), 28(6), 34(5),
36(1)); the bar on officers with convictions (s 12); minors (s 17); nominations
(s 18); paying a death benefit (s 22(4)); special resolutions (ss 25, 26); members'
applications to the Registrar (ss 27(1), 34(1)); notice before cancellation or
suspension (s 28(2), (3)); the penalties (ss 12(2), 29(3), 30(2), 38–40, 42(2), 44, 45,
46); and members' immunity from judgments (s 47(3)).

Not encoded: the application papers, certificate and Gazette list (ss 3, 4(2)–(4), 5,
8); the registered office, trustees, audit, annual return and balance sheet (ss 10–11,
13–15) except as s 42 penalises failures; the s 16 priority on an officer's death or
bankruptcy; the members' copy and inspection rights (ss 19–21); the reserve funds and
bank accounts (ss 22(1)–(3), 23); change of name (s 24); the inspector's powers; the
cancellation grounds and effects (s 28(1), (4), (5)); freezing and seizure (ss 29,
30(1)); winding up (s 31); dissolution procedure (ss 32–35); dispute procedure
(s 36(2)–(4)); presumptions (s 41); officers' vicarious liability (s 43); service
(s 47(1), (2)); s 48(2), s 49 and the Schedule. No rules under s 49 were retrieved, so
the prescribed fee and the s 22(1) administration percentage are unknown.

## What the Act turns out to say

### 1. A member may nominate a "wife", but not a husband, without a JP

s 18 lists who may be nominated to receive benefits: "the wife, children (including
adopted children), grandchildren, mother, father, sons-in-law, daughters-in-law",
siblings of the whole or half blood and their children, uncles and aunts of the whole
or half blood and their children. It says "wife", not "spouse", and it has no
grandparents. Anyone else — a husband, a grandparent, an uncle by marriage, a friend —
can be nominated only by a writing signed before and attested by a Justice of the
Peace, a Magistrate or the Registrar. First cousins are in; a grandmother is out.
Asserted.

### 2. Every unregistered benefit scheme is unlawful, and so is attending its meeting

s 37 deems every mutual benefit organisation that is not registered "an unlawful
organisation". s 2 catches any organisation that provides, "either as the principal
object or as an ancillary object", from members' voluntary subscriptions, for
sickness, old age, widowhood, orphans, a birth or death payment, funeral expenses,
unemployment or distress. Running one is punishable by $3,000 or 3 years (s 38);
being a member or merely attending a meeting by $1,000 or one year (s 39); knowingly
letting it meet on your premises the same (s 40). s 41(b) puts the burden of proving
registration on the accused. The only escapes are the s 48 exemptions: insurers, and
bodies registered as co-operatives, trade unions or under the Platform Workers Act
2024, or ones the Minister exempts. Asserted (ss 2, 37, 38, 39, 40, 48).

### 3. A dispute with your society cannot go to court, and a dissolution order cannot be appealed

s 36(1): a dispute between a member (or a former member, or someone claiming through
one) and the organisation is decided as the rules direct, and the decision is
"binding and conclusive on all parties without appeal, and shall not be removable to
any court or restrainable by injunction" — only enforcement goes to a District Court.
A Registrar's dissolution order after investigation is likewise "final and conclusive
... without appeal" (s 34(5)). By contrast refusal of registration, conditions,
refusal of a rule amendment and cancellation or suspension all go to the Minister,
whose decision is final (ss 7, 9(3), 28(6)). Asserted.

### 4. Fifty members, or no registration

The Registrar "shall refuse" registration if the members and subscribers number fewer
than 50 (s 6(1)(e)), and may cancel a registered organisation whose membership falls
below 50 (s 28(1)(a)(vi)). Refusal is also mandatory if any officer "is not of good
character"; it is merely discretionary if no satisfactory evidence of good character
is produced (s 6(2)(b)). Asserted for s 6.

### 5. The Minister's permission lifts only half of the s 12 bar

s 12(1) bars from office (a) anyone convicted of an offence of dishonesty or moral
turpitude, and (b) anyone fined at least $2,000 or imprisoned for at least a year for
any other offence — in both cases unless pardoned. The words "unless the written
permission of the Minister so to act is first obtained" are printed inside para (b).
Read literally, the Minister can permit a (b) offender but not a dishonesty offender.
That reading is encoded and is a guess about drafting, not a settled point. Breach is
$500 or 6 months (s 12(2)). Asserted.

### 6. Smaller points

- A special resolution needs three-fourths of those present and voting, then
  confirmation by a simple majority at a second meeting 14 days to one month later,
  and has no effect until the Registrar registers it (ss 25, 26). Asserted.
- One-fifth of the members can ask for an inspector or a special meeting (s 27(1)) or
  for an investigation with a view to dissolution (s 34(1)). Asserted.
- Cancellation (unless requested) and suspension need at least 2 months' written
  notice; suspension is for at most 3 months, renewable (s 28(2), (3)). Asserted.
- A member under 21 may join if the rules allow, but may not sit on the committee or
  be trustee, secretary, manager or treasurer; one over 16 signs for himself (s 17).
  Asserted.
- A death benefit needs a death certificate, or — where there is no nomination —
  payment to the personal representative on a grant of probate or administration
  (s 22(4)). Asserted.
- The s 42 failures (notices, returns, information) carry only a $200 fine, but s 44
  makes every week of a continuing default a new offence. Counting one offence per
  week is an inference. Asserted.
- A judgment against the organisation reaches only its property, never an officer's or
  member's (s 47(3)). Asserted.

## What would need doing before this is worth anything

- The Mutual Benefit Organisations Rules (fees, the administration percentage under
  s 22(1)) were not retrieved.
- The s 12 reading (finding 5) and the s 18 "wife" wording (finding 1) should be
  checked against any reported case or the Registrar's practice; none was searched.
- "Over 16" in s 17(2) is read as more than 16 whole years, the one-month limit in s 25 is a
  flag rather than computed, and the one-month appeal period in s 7 is not encoded.
- Registration duties, annual returns, dissolution and winding up are not encoded.
