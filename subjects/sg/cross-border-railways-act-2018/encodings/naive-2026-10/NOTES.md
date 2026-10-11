# Cross-Border Railways Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, deposited as
`../../registers/source-bundle/CBRA2018.txt`. Its page header reads "version in
force from 30/9/2026". The latest amendment annotated is Act 16 of 2026 wef
30/09/2026 (ss 59 to 61, tied to the Cross-Border Railways (Border Control
Co-location) Act 2026). Section 77 is annotated as repealed by Act 3 of 2021 wef
01/07/2025.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0093** in `subjects/sg/requirements.jsonl`: Tier 2 of
the remaining Singapore Acts, ordered by everyday-life relevance. It asks what
the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

Most of the Act governs the State, the LTA, the concessionaire and the
licensees. This row takes the parts an ordinary person or small business meets:
the LTA's entry onto nearby land and the notice it owes (ss 8 to 10, 12, 13), an
owner's right to make the Government buy land (ss 15, 16), bag searches at a
cross-border station (s 61), the public offences (ss 53, 62 to 64, 68), running
services without authority (ss 25, 29), the maximum penalties, the compounding
cap (s 73) and what commenced first (s 1(2)). Not encoded: plans and maps,
State land, utilities, the bridge, funding, the concession and operator
contracts, licensing, monitoring, railway opening, safety audits, service
suspension, security directives and agency powers, arrest, corporate liability,
and the Land Acquisition Act 1966 provisions that s 16 imports.

## What the Act turns out to say

### 1. The deposit does not show that the passenger and safety provisions are in force

The commencement note lists only **14 September 2020**: Parts 1 to 3, ss 21 to
24, 26 to 28, 65 to 67, 73 to 76 and parts of s 78. Section 1(2) says ss 25 and
29, Parts 6 to 9 (which hold the searches and public offences in ss 53 and 61 to
64) and ss 68 to 72 commence "on a date that the Minister appoints by
notification in the Gazette". The deposit records no such date. Act 16 of 2026
amended Part 9 with effect from 30 September 2026. That suggests Part 9 is meant
to operate, but this is an inference: the deposit does not say. Asserted
(s 15 commenced; ss 25, 29, 61, 68 are not shown as commenced).

### 2. Refusing a bag search is an offence even if you then leave

Under s 61(1) the individual "must permit" the search. Under s 61(2) an official
may require someone who refuses to leave, "without prejudice to subsection (3)".
Section 61(3) punishes contravening (1) **or** (2), up to $1,000. So the refusal
is itself the offence, and leaving does not cure it. A reasonable excuse does.
Asserted.

### 3. Who may search is narrower than "security"

A "railway official" (s 61(4)) must be authorised in writing by the cross-border
railway security agency **and** be an LTA officer, a police officer or
auxiliary police officer **in uniform**, a licensee's employee, or a security
officer engaged **by a licensee**. A plain-clothes police officer, or a guard
hired by a shop in the station, is not one. Asserted.

### 4. Damage costs more; endangering lives costs longer

Wilfully damaging "any part of a cross-border railway" (s 63) carries up to
$200,000 but only 12 months. Wilfully endangering a person's safety (s 62)
carries up to $10,000 but 5 years. Failing to report an accident (s 55(3))
carries $100,000 or 5 years. Asserted (ss 62, 63).

### 5. Owners can force a purchase, but only after s 8 possession, and all must sign

An "owner" (s 15(5)) includes a tenant in occupation only if the term "exceeds 7
years", so a 7-year tenancy does not qualify. The right arises only where
possession was taken under **s 8**, not after mere survey or inspection entry
(ss 9, 10). Where there are several owners, all must give the notice (s 15(2)),
and it is irrevocable (s 15(3)). The rest of the same parcel may be included
(s 15(4)). Asserted.

### 6. The notice ladder: 2 months, 28 days, 14 days, 7 days, or none

Taking possession needs 2 months' notice (s 8(3)). A removal notice needs 28 days
(s 12(3)(c)) and a pre-construction survey 14 days (s 9(3)). Inspection or
remedial work within 150 metres needs 7 days (s 10(3)). Section 10(4) drops even
that if the LTA thinks it an emergency, or the entry is "only for the purpose of
an inspection or a survey". Asserted.

### 7. Obstructing entry has no identity carve-out

Sections 53(2) and 64(2) say it is not an offence to refuse an inspector, or an
out-of-uniform officer, who will not declare their office and show ID. Section
13 requires an authorised individual to produce evidence of authority if asked
(s 13(1)), but s 13(2) makes no matching exception. The encoding does not invent
one. Whether a court would imply it is untested. Asserted.

### 8. Two small quirks in the penalties

Section 53(3) (non-compliance or false information to a safety inspector) reads
"$5,000 or to imprisonment for a term not exceeding 6 months", without "or to
both", unlike every neighbouring offence. Section 73 caps a composition sum at
the lower of half the maximum fine and $5,000, but only for offences "prescribed
as a compoundable offence". No regulations were retrieved, so the cap is shown
as a cap if prescribed. Asserted.

## What would need doing before this is worth anything

- Check the Gazette for a commencement notification for ss 25, 29, Parts 6 to 9
  and ss 68 to 72. Finding 1 depends on it.
- The s 16(2)(d) claim period ("one year starting from either of the following
  dates") is read as satisfied by either date. That reading is an inference.
- The Land Acquisition Act 1966 ss 49, 49A, the LTA Act compensation claims, and
  the Border Control Co-location Act 2026 (s 36 of which limits ss 60, 61) were
  not read.
- No regulations (prescribed compoundable offences, accident reporting times)
  and no case law were searched.
