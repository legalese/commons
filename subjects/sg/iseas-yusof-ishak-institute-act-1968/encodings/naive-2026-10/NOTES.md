# ISEAS – Yusof Ishak Institute Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/ISEASYIIA1968.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31 December
2021". The latest amending Act annotated in the text and the Legislative History is Act 5
of 2018 (Public Sector (Governance) Act 2018, in force 1 April 2018).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **requirement REQ-0179** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short (17 sections) and almost entirely about the Institute's own governance.
This row takes what an outsider can meet (the personal liability shield, donations, the
common seal, fees, inspection of committee records, which body decides which matter) and,
for those inside, Board membership and meetings and the Executive Committee's size and
quorum: ss 4, 6, 10, 13, 14(2)(d)(vii) and (h), 14(4), 16, 17, with ss 5, 5A, 11, 12 and
15 for the who-decides table. Not encoded: the Institute's object (s 3), contracts,
property, borrowing and investment (ss 8, 9), shares to the Minister for Finance (s 9A),
the other regulation-making heads (s 14(2)(d), (e)), pensions and residences
(s 14(2)(f), (g)) and the heads of the rule-making power (s 15(2)).

## What the Act turns out to say

### 1. There is no offence and no penalty anywhere in the Act

Nothing in ss 1 to 17 creates an offence, a fine or a duty enforceable against a member of
the public. What the Act decides for an outsider is limited to who may act for the
Institute and how. (Not an assertion; a reading of the whole deposited text.)

### 2. The liability shield needs reasonable care as well as good faith

s 17 protects a Board member, employee or "other person acting under the direction of the
Institute" only if "acting in good faith and with reasonable care". Careless conduct in
good faith is outside it, and so is a person not acting under the Institute's direction.
The section says nothing about the Institute's own liability. Asserted.

### 3. Every donor's name goes on the register, with no anonymity exception

s 16(2): "Registers must be kept of all donations ... including the names of donors and
any special conditions". No exception for an anonymous donor is written in. A gift for a
specific purpose must be applied to that purpose and "separately accounted for"
(s 16(3)). That an unrestricted gift may go to any purpose of the Institute is an
inference from s 16(1). Asserted.

### 4. Committee records are open only to Executive Committee and committee members

s 14(4): proceedings of every committee "must be open to inspection to any member of the
Executive Committee or any member of the committee at any time". The Act gives no right of
inspection to a Board member who is off the Executive Committee, to a fellow, or to the
public. Asserted.

### 5. A sealed instrument needs one qualifying witness from each side, and both signatures

s 10(2): the Chairperson or a Board member the Chairperson designates, and the Director or
an Executive Committee member the Director designates, must both be present and must both
sign. What follows for an instrument sealed otherwise, the text does not say. Asserted.

### 6. Fees only by Board-approved regulations, and two bodies discipline fellows

The Executive Committee may demand fees "prescribed by regulations" (s 14(2)(h)), and fee
regulations are made "subject to the approval of the Board" (s 14(2)(d)(vii)). Reading the
approval requirement into every fee is an inference. The discipline of fellows is given
to the Director (s 12(2)(d)) and also, with staff, to the Executive Committee
(s 14(2)(g)). The encoding returns the Director and labels that choice as an inference.
Asserted.

### 7. Board and Executive Committee arithmetic

The Board is 15: Chairperson, Deputy and 12 appointed by the Minister, plus the Director
ex officio (s 4(2), (3)). The quorum is 5 and the chair has a casting vote (s 6). A member
who misses 4 consecutive meetings without leave is treated as having resigned (s 4(9)). A
written resignation takes effect when the Chairperson receives it (s 4(6)). The Executive
Committee is 10 (1 + 3 + 3 + 3) with a quorum of 5 (s 13). Reading "a majority of the votes
of the members present" as a majority of the votes cast is an inference. Asserted.

## What would need doing before this is worth anything

- No regulations of the Executive Committee and no Minister's rules were retrieved, so no
  actual fee, and nothing about fellows' admission or discipline, is known.
- The Public Sector (Governance) Act 2018, which governs the Director's appointment and
  Ministerial directions (ss 5A, 12), was not read.
- Whether another law (for example the Public Sector (Governance) Act 2018 or the Charities
  Act 1994) adds duties about donations or records was not checked.
