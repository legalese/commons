# National Council of Social Service Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments to 1 December 2021),
informal consolidation, version in force from 1 August 2026, as deposited at
`../../registers/source-bundle/NCSSA1992.txt`. The latest amendment annotated is
Act 3 of 2026 (wef 01/08/2026), which rewrote most of the Act. The deposit's
Arrangement of Sections is out of step with the body (it lists "11. Community
Chest" and leaves 14 and 14A blank); this row follows the body.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0189** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is mostly the constitution of a statutory board. What an outside
organisation meets is sector membership and its appeal (ss 15, 16); what an
individual meets is eligibility to serve on the Council or the Community Chest
(ss 5B, 13(4)-(6)). This row encodes those, plus the composition, quorum and voting
arithmetic (ss 5, 7, 9), removal and resignation (ss 5F, 5G), absence from meetings
(s 5J(1)(g)) and the reserve sweep into the Endowment Fund (s 26(1)(b)). Not
encoded: objectives, functions and powers (ss 11, 12), committees and delegation
(ss 14, 14A), patrons, staff, the rest of Part 6 (including the 30 June and
30 September statement deadlines), Ministerial directions (s 10), protection from
liability (s 36) and regulation-making (ss 37, 38). No regulations were retrieved.

## What the Act turns out to say

### 1. Revocation can be appealed; suspension and censure are not in s 16

s 16(2) lists three appealable decisions: refusing to appoint, refusing to
re-appoint, and revoking an appointment as a sector member. s 37(2)(d) contemplates
regulations imposing "letters of censure and the suspension or revocation of
appointment", but s 16 names only revocation. Whether the regulations give their
own route against censure or suspension was not checked. Asserted.

### 2. Fourteen days, the decision bites meanwhile, and the Minister's word is final

An appeal must be brought "within 14 days after notice of the decision is served",
unless the Minister extends the period (s 16(1)). The decision "must be complied
with until the determination of the appeal" unless the Minister directs otherwise
(s 16(6)). The Minister may confirm, vary, cancel or send the decision back to the
Council (s 16(7)), and that decision "is final" (s 16(8)). The Minister owes no
duty to decide an appeal that does not set out grounds and evidence in time, or is
frivolous or vexatious (s 16(5)). A Minister of State or a Parliamentary Secretary
may hear it instead; a civil servant may not (s 16(10)). Asserted.

### 3. Eligibility is a threshold, not an entitlement

An organisation must have "the primary function" of providing, or directly
supporting, a social service in Singapore (s 15(3)), but the Council only "may
appoint" (s 15(1)) and may weigh whether its aims are "contrary to the public
interest, public order or national harmony" (s 15(6)). The encoding decides
eligibility only. Asserted.

### 4. Silence is a vote in favour

s 9(4) presumes that a member present "agreed to, and ... cast a vote in favour
of" a decision unless the member "expressly dissents" or is barred by s 26 of the
Public Sector (Governance) Act 2018. Read with s 9(3), this encoding counts every
present, non-dissenting, non-barred member as a vote for; that reading is an
inference. A tie goes to the presiding member's casting vote. Asserted.

### 5. Sector members choose half the Council, but are not on it

At least 7 members, and at least half of all members excluding the Chairperson,
come from the list of sector members' nominees (s 5(2)(d), (4)), within a Council of
15 to 27 (s 5(1)). Sector members themselves "are not members of the Council"
(s 15(7)). The quorum is the higher of one-third of the members and 7 (s 7); a
quorum of one-third is read as a floor to be reached (an inference). Asserted.

### 6. Who may sit, and who may leave

s 5B(2) disqualifies Council employees (but not the CEO), judges, undischarged
bankrupts and those with a creditors' arrangement, the unpardoned convicted of
dishonesty, fraud or moral turpitude, the unpardoned sentenced to 6 months or more,
disqualified directors and those lacking capacity. The same list governs the
Community Chest (s 13(4)), where the CEO may be a member but never chairperson or
deputy (s 13(5)), and every appointee must disclose interests first (s 13(6)). The
Minister may remove an appointed member "without giving any reason" (s 5F); the CEO
and the Community Chest chairperson can neither be removed nor resign under these
sections (ss 5F, 5G). Missing 3 consecutive meetings without approval ends a
member's office (s 5J(1)(g)), with no compensation (s 5J(2)). Asserted.

### 7. Reserves above two years' spending are swept into the Endowment Fund

s 26(1)(b) puts "all reserves of the Council in excess of 2 years of its operating
expenditure" into the Endowment Fund, which may be applied only for purposes the
Minister approves in writing (s 26(3)). Reading "2 years" as twice an annual
figure is an inference. Asserted.

## What would need doing before this is worth anything

- The National Council of Social Service regulations (sector member standards,
  revocation procedure, sanctions, nomination criteria, appeal procedure under
  s 38) were not retrieved; s 15(4), s 5(3) and the appeal procedure rest on them.
- The Public Sector (Governance) Act 2018 provisions the Act leans on (Part 4
  interests, s 26 voting bar, s 5 directions) were not read.
- The rounding of "one-third" in s 7 and the measure of "2 years of its operating
  expenditure" in s 26 are inferences needing confirmation.
