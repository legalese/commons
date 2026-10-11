# Hindu Endowments Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions as the example rows show them (the skill itself was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), as deposited at `../../registers/source-bundle/HEA1968.txt`. The deposit
says it "incorporates all amendments up to and including 1 December 2021 and comes into
operation on 31 December 2021". The latest amendment annotated in the body is
[Act 25 of 2021 wef 01/04/2022], on s 32(1). The meta file records the version as
current at 1 October 2026.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0144** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

Most of the Act is about how the Hindu Endowments Board runs itself. This row takes the
parts that reach people outside the Board, plus the eligibility and tenure rules for
those appointed to it:
- what an endowment is (s 2)
- who may be appointed to the Board or a committee of management, and how a Board
  appointment ends (ss 5, 8, 9, 20)
- the Board's quorum (s 12)
- when the Minister may hand an endowment to the Board (s 18)
- who must account to the Board, and the s 24 offence and fine (ss 22, 24)
- the indemnity for acting on the Board's advice (s 25)
- the bar on suing about an endowment without the Board's order (s 26)
- dealings with endowment land (ss 17, 28)
- the annual report deadlines (ss 29, 30)
- personal immunity (s 34A) and the ban on political use of temples (s 36)

Not encoded: incorporation, the Secretary, Gazette notice, chairing and secrecy
(ss 3, 4, 6, 7, 10, 11), the seal, officers, minutes and other committees (ss 13 to 16),
companies (s 17A), vesting and the Registrar of Deeds (s 19), the Board's powers once it
administers an endowment (s 21), examination (s 23) except through s 24, compromise
(s 27), schemes in the High Court (ss 31 to 34), rules (s 35) and the 1969 transfer from
the Muslim and Hindu Endowments Board (s 37).

## What the Act turns out to say

### 1. You cannot sue about an endowment without the Board's order

s 26(1): before "any legal proceeding for obtaining any relief, order or direction
concerning or relating to any endowment" is begun, the person must send the Board
written notice. s 26(4): no court shall entertain it "except upon and in conformity with
an order of the Board". The only carve-out (s 26(5)) is a claim made "adversely to any
endowment". The text says "any endowment" and does not confine this to endowments the
Board administers under s 18. Asserted.

### 2. The one-third limb of the Board's quorum never bites

s 12(1) requires "at least 7 members or one-third of the members, whichever is the
greater". Under s 5(1) the Board has a Chairman, a Vice-Chairman, a Finance member and 8
to 12 others: 11 to 15 members. One-third of 15 is 5, so the quorum is always 7. Only
adjournment may be done without it. Asserted.

### 3. A committee of management can be lawfully constituted and never quorate

s 20(2) requires at least one Board member and no more than 11 others; there is no
minimum beyond that. s 20(3) fixes the quorum at "6 members present". A committee of one
Board member and four others meets s 20(2) but can never transact business. Asserted.

### 4. The Board can call anyone touching an endowment to account, including former trustees

s 22(1) reaches people who "are or have been at any time" administering it, their agents,
anyone holding its funds or documents, anyone receiving "any income or stipend" from it,
and anyone occupying its property. A refusal, a wilful neglect, or destroying or
withholding a required document is an offence under s 24: a fine up to $5,000, plus up
to $50 a day while it continues after conviction. No imprisonment is provided. Plain
(not wilful) neglect is not an offence. Asserted.

### 5. Advice under seal shields the trustee, even against a later court order

s 25(2): a trustee who acts on the Board's written advice under seal is deemed to have
acted in accordance with the trust. s 25(3): no later High Court order impairs that. The
shield falls away for fraud, wilful concealment or misrepresentation in obtaining the
advice (s 25(4)). Asserted.

### 6. Temples are excepted from letting and sale in s 28, but not in s 17

s 28 lets the Board let, sell or exchange endowment land and buildings "other than any
temple or the grounds thereof", even where the trusts do not authorise it. s 17(1)(c)
and (2) separately let the Board dispose of "any ... property vested in" it,
notwithstanding "a trust or condition ... prohibiting or restricting" that. s 17 has no
temple exception. How the two fit together the text does not say. The encoding keeps
them as two separate rules. Asserted, each on its own terms.

### 7. Only Hindu citizens may serve, and a Finance member is limited to two terms

ss 5(4) and 20(5): Board and committee members must be Hindu **and** citizens of
Singapore; a permanent resident does not qualify. s 5(3): a Finance member may not serve
more than 2 consecutive terms in that role, but may then be appointed in another
capacity. An appointment ends on death, written resignation, bankruptcy, or more than 3
months' absence from Singapore without the Chairman's written permission (s 8). The
Minister may revoke one after 3 successive meetings missed without cause approved by the
Chairman (s 9). Asserted.

### 8. An endowment is land, a building or money

s 2 names only "land, building or money". Other movable property given to a temple is
outside the definition. But once the Minister orders the Board to administer an
endowment, "all the property, both movable and immovable" vests in the Board (s 19(1)).
The s 18 order needs a report from the Board, one of three grounds (mismanagement, no
trustees, or the endowment's advantage), and a chance for the managers to make
representations. Asserted for ss 2 and 18; s 19 is not encoded.

### 9. Smaller points

- The annual report must reach a Board meeting after 31 March and by 31 December, and be
  sent to the Minister, gazetted and exhibited in every Board temple within 14 days of
  that meeting (ss 29, 30). Asserted.
- s 34A protects Board members, the Secretary, employees and those acting under the
  Board's direction, for acts done in good faith under the Act. A private trustee acting
  on his own is not covered. Asserted.
- s 36 bars political use of Board temples and endowment land, but it binds only the
  Board and committees, carries no penalty, and does not define "political purposes".
  Asserted as a duty only.

## What would need doing before this is worth anything

- Whether s 26 really reaches endowments the Board does not administer needs case law;
  none was searched.
- The relationship between s 17(2) and the temple exceptions in s 28 needs a reading
  from someone who knows its legislative history (the deposit does not annotate s 17
  with an amending Act).
- No rules under s 35 were retrieved.
- Dates are YYYYMMDD numbers. Months (ss 8, 32, 33) are counted as given, not computed.
- The one-month objection period and hearing date for schemes (ss 32, 33) are not
  encoded.
