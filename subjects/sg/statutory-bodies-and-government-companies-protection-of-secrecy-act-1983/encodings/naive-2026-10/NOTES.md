# Statutory Bodies and Government Companies (Protection of Secrecy) Act 1983 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments to 1 December 2021, in operation
31 December 2021), informal consolidation marked "version in force from 1/7/2026".
The latest amendment annotated is Act 17 of 2026 wef 1 July 2026, which deleted
Schedule item 33; S 120/2026 wef 18 March 2026 is also annotated. The Schedule
table is column-shifted in the `.txt` deposit, so each body was matched to its
establishing Act by item number and order of appearance.

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0219** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is five sections and a Schedule, so all of its operative text is encoded:
s 2 and the Schedule (which organisations), s 3 (the duty, its exceptions, the
penalty), s 4 (consent to prosecute) and s 5 (amending the Schedule). The Schedule
is encoded for a sample of its listed bodies plus PSA Corporation Limited and its
subsidiaries, with four unlisted organisations for contrast. The secrecy provisions
in the listed bodies' own Acts were not read.

## What the Act turns out to say

### 1. The duty binds former staff, with no time limit

s 3(1) applies to "a person who is or has been" a member, officer, employee or agent
of a specified organisation. Nothing in the Act ends the duty when the person leaves,
or after any period. A former IRAS employee who discloses a confidential file years
later commits the offence. Asserted.

### 2. Only one Government company is protected: PSA

Part 2 of the Schedule, "Government companies", has a single entry: "PSA Corporation
Limited and its subsidiary corporations." Every other organisation the Act protects
is a statutory body in Part 1 (CPF Board, HDB, IRAS, MAS, LTA, URA, PUB, SEAB, the
People's Association, Majlis Ugama Islam Singapura and others). An organisation that
is not in the Schedule (Health Sciences Authority, the Accounting and Corporate
Regulatory Authority, a Government ministry, a private company) is outside the Act.
Whether a body missing from the list has its own secrecy provision elsewhere was not
checked. Asserted.

### 3. Two exceptions only, and no public-interest defence

s 3(2) excepts a disclosure (a) "for the purpose of the performance of his or her
duties or functions" by any member, officer, employee or agent of a specified
organisation, or (b) which a court lawfully requires or authorises, or written law
requires or allows. Separately, s 3(1) is not engaged at all if the organisation
gives its authority. The Act contains no public-interest or whistleblowing defence.
Exception (a) speaks of the duties of members etc. of *a* specified organisation,
not only the discloser's own; reading it as covering disclosures between bodies is
an inference the text leaves open. Asserted for the three routes as written.

### 4. Only the insider's disclosure is an offence

s 3(1) forbids disclosure, not use, and only by a present or past member, officer,
employee or agent. A member of the public who passes on a leaked file commits no
offence under this Act (other laws were not considered). Nor does the Act define
"secret or confidential": that is left to the facts. Information obtained other
than "by virtue of the person's position" is outside s 3(1). Asserted.

### 5. A small penalty, and no prosecution without the Public Prosecutor's written consent

s 3(3): a fine not exceeding $2,000, imprisonment not exceeding 12 months, or both.
s 4: no prosecution "except with the written consent of the Public Prosecutor"; oral
consent does not satisfy it. Asserted.

### 6. The President amends the list by Gazette notification

s 5: "The President may, by notification in the Gazette, amend the Schedule." The
list moves often: it carries lettered items (5A Communicable Diseases Agency, 10A
Gambling Regulatory Authority of Singapore, 21A National Council of Social Service;
that the lettering marks later insertions is an inference), a 2026 entry (31 Skills and Workforce Development Agency Act 2026) and
deletions (item 3 by Act 14 of 2022, item 33 by Act 17 of 2026). The deposit does
not say what items 3 and 33 were. Asserted for s 5.

## What would need doing before this is worth anything

- The full Schedule (34 live statutory-body entries in Part 1, by count of the deposit) is not enumerated; only a sample is.
- The listed bodies' own Acts were not read for overlapping secrecy provisions, and
  how this Act interacts with them is not addressed.
- No case law on "secret or confidential", or on "by virtue of the person's position",
  was searched.
- S 120/2026 was not retrieved; its effect on the Schedule is not known.
