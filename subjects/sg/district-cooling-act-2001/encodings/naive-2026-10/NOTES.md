# District Cooling Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1/4/2022, as
deposited at `../../registers/source-bundle/DCA2001.txt`. The latest amendment
annotated in the body is Act 25 of 2021 wef 01/04/2022 (s 30). The deposit's metadata
says "Current version as at 01 Oct 2026".

**Checks:** one module (`dca-duties.l4`), one case file (`dca-cases-duties.l4`):
54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0091** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short (47 sections) but mostly about the Energy Market Authority and its
licensees. This row takes what an occupier, landowner, developer, excavating
contractor or would-be supplier meets: the duty to use district cooling and the duty
to supply (s 7); the licence and the unlicensed-supply offence (ss 10, 11, 32); the
Authority's financial penalty (s 13(1)(i)); the 14-day appeal windows (ss 10(8),
12(4), 13(2), 25(10), 28(8)); entry by the Authority (s 6) and by the licensee
(ss 25, 27); the landowner's right to have the system moved (s 28); apparatus on the
consumer's premises (s 30); emergency cut-off and immunity (ss 17, 31); digging in a
service area (s 38); and penalties, composition and officers' liability (ss 5, 32 to
35, 37, 39 to 41, 45(2)).

Not encoded: administration (ss 3, 4), declaring and revoking service areas (ss 7(1),
(2), 8, 9), licence conditions and their modification (ss 10(2) to (7), 12 beyond the
appeal window), codes of practice and directions (ss 14 to 16), the licensee's general
duties and pricing (ss 18, 19), the register (s 20), special administration (ss 21
to 23), public land (s 24), wayleaves (s 26), the developer's duty to provide space
(s 29), jurisdiction (s 36), general appeals (s 42), exemptions (s 43), service
(s 44), and regulations, incorporation and advisory guidelines (ss 45 to 47). No
regulations or service-area notifications were retrieved.

## What the Act turns out to say

### 1. In a service area, using district cooling is compulsory, and so is supplying it

s 7(3): "Unless exempted, the occupier of every premises within a service area
requiring air conditioning must use the district cooling services provided by a
licensee if the services are available". s 7(5): the licensee "must not refuse to
provide" to any premises in its service area. Either breach is an offence of up to
$10,000 or 12 months, plus up to $250 a day for a continuing offence after
conviction (s 7(6)). The only way out for the occupier is an exemption, on which "the
decision of the Authority is final" (s 7(4)), or a general exemption under s 43.
Asserted.

### 2. Running an unlicensed district cooling business carries a fine only; obstructing an inspector can mean prison

s 32 fixes $50,000 for unlicensed supply and nothing else, so no imprisonment.
Offences without an express penalty fall to s 39: $10,000 or 12 months or both. That
catches obstructing the Authority (s 34), false statements (s 35), pretending to be an
employee to gain entry (s 33), failing a notice to furnish information (s 5) and
digging without locating the apparatus (s 38). Refusing to give identity is $5,000,
fine only (s 37(3)). Asserted.

### 3. A landowner can be made to host the pipes, with 14 days to object

s 25: the licensee may lay its system on private land in the service area after "at
least 14 days' notice"; the owner or occupier may object to the Authority "within 14
days of the receipt of the notice", and then the Authority holds an inquiry and may
authorise the work. The licensee gets only a right "of a user" and must pay
compensation, which may be an annual payment. s 25(7) says entry may proceed if no
objection is lodged "within the time specified in subsection (5)" — but the objection
period is in subsection (6); the encoding reads it as (6). The text does not say what
happens when an objection is lodged and then withdrawn; not modelled. Asserted.

### 4. Who pays to move the pipes depends on why

s 28: if the owner wants them moved to develop the land, "the owner is liable to pay
reasonable compensation to the licensee" (s 28(5)); if the part is no longer in use,
the licensee removes it "at its own cost and expense" and compensates the owner
(s 28(7)); for any other change of use under s 28(1) the Act does not say who pays.
"Owner" includes a lessee with at least 7 years unexpired (s 28(10)), and the whole
section yields to a contrary agreement (s 28(9)). Asserted.

### 5. An emergency cut-off is free of liability, for the licensee and the Authority

s 31(1) lets the licensee "forthwith discontinue" supply when it is "of the opinion"
that immediate action is needed for an emergency, public safety, other consumers or
"any other reasons affecting the public interest". It must notify and restore
promptly (s 31(2)), but s 31(3) says it "shall not be liable for any loss or damage";
on the words the immunity is not conditional on the notice. s 17: the Authority is not
liable "in any circumstances" for a licensee's default. Asserted (the immunity; the
notice point is a reading).

### 6. Entry notice periods differ: 6 hours, 7 days, 14 days

The Authority needs 6 hours' notice to the occupier, except in an emergency (s 6(2)).
The licensee needs 7 days for inspection and repair, none in an operational emergency
from a fault, and there is no objection procedure (s 27). Laying new plant needs 14
days and carries the objection right (s 25). Asserted.

### 7. The Authority's penalty is a share of turnover

s 13(1)(i): up to 10% of annual turnover from district cooling in Singapore, from the
latest audited accounts, imposed "without any liability for compensation". All the
appeals to the Minister run 14 days and the Minister's decision is final. Asserted
(day 14 is treated as within time, an inference from "within").

### 8. Digging by hand is outside s 38

The duty to locate the licensee's apparatus first applies to digging "with any
mechanical equipment or explosive" in the service area. Asserted.

## What would need doing before this is worth anything

- Retrieve the regulations (which offences are compoundable under s 40, licence fees)
  and the Gazette notifications that declare the service areas; without them no real
  premises can be placed in or out of the s 7 duty.
- Decide how the s 25(7) cross-reference to subsection (5) should be read, and the
  effect of a withdrawn objection.
- Encode s 19(2) (no undue preference or discrimination in price) if a scenario asks.
- No case law or Authority decisions were searched.
