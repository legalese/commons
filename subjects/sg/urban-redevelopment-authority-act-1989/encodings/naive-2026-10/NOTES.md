# Urban Redevelopment Authority Act 1989 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 July 2026), deposited at `../../registers/source-bundle/URAA1989.txt`. The cover
says the revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated in the body is Act 15 of 2026, in force 1 July 2026, which
changed the Authority's functions in s 6 (not encoded).

**Checks:** one module (`uraa-powers.l4`), one case file (`uraa-cases-powers.l4`),
57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0225** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

Most of the Act sets up the Authority: its constitution, functions, staff, finances
and the 1989 merger. This row takes the provisions a person or business actually
meets: declaring an urban redevelopment area (s 8), ex gratia payments (s 11), entry
on land and buildings (s 16), the penalties regulations may carry (s 17(3)), the
Authority's symbol (s 43), statistical notices and their service (ss 44, 44A),
secrecy (s 45), obstruction (s 46), the Public Prosecutor's consent (s 48), errors in
paid information (s 49), officers of a body corporate (s 50), composition (s 51A),
and, as the one governance rule with arithmetic in it, the quorum (First Schedule
para 11(2)). Not encoded: ss 6, 7 and the Second Schedule beyond mention, ss 9-15,
18-42, 47, 51, 52, and the Third and Fourth Schedules.

The planning control people associate with URA (planning permission, development
charges) is not in this Act. s 2 borrows "develop" from the Planning Act; the control
itself lives there.

## What the Act turns out to say

### 1. URA's officers may enter your home on 6 hours' notice

s 16(1) lets the Authority's employees, agents or contractors enter "at all
reasonable hours in the day" into any building or land to survey, inspect or execute
authorised work, free of legal proceedings. The only protection for an occupied
building is s 16(2): consent of the occupier **or** "6 hours' previous notice". Two
hours' notice without consent is not enough; vacant land needs none. Asserted.

### 2. The statistical-notice offence treats refusal and neglect differently

s 44(7)(a): a person who "wilfully refuses or without lawful excuse (the proof of which
lies on the person) neglects" to answer a notice in time commits an offence. Read
literally, a lawful excuse answers only neglect: a wilful refusal is an offence even
where an excuse is proved, and the burden of the excuse sits on the person, not the
prosecution. Wilfully furnishing false particulars is a separate limb (b). The
maximum is $2,000 or 6 months. Asserted (the wilful-refusal reading is a literal one;
no case was consulted).

### 3. How a notice may be served depends on who you are

s 44(2): an individual may be served by having the notice affixed at home or work but
not by fax; a partnership or company may be served by fax but not by affixing.
Email is allowed only if the person gave an email address for service (s 44(6)).
Registered post is deemed served when it would ordinarily arrive "whether or not it is
returned undelivered" (s 44(5)(a)); a fax counts only if a notification of successful
transmission is received (s 44(5)(c)). Asserted.

### 4. s 44(5)(b) deems service by ordinary post, which s 44(2) never permits

s 44(5)(b) says a notice "sent by ordinary post ... in accordance with subsection (2)"
is deemed served the day after ordinary delivery. But s 44(2) lists only registered
post, never ordinary post; likewise (5)(c) speaks of a fax to a "place of residence",
which (2) does not provide for. The encoding gives the deemed day as written (ordinary
delivery + 1) and flags the mismatch. Asserted.

### 5. Disclosing what URA collected carries the stiffest penalty in the Act

Every offence in the Act is capped at a $2,000 fine; the imprisonment varies: 3 months
for obstruction (s 46) and for regulations (s 17(3)), 6 months for the symbol (s 43)
and statistical notices (s 44(7)), and **one year** for an officer who discloses
protected information outside the seven exceptions of s 45(1). Regulations may add up
to $500 a day "or part of a day" for a continuing offence. Asserted.

### 6. Compensation for damage is a favour, not a right

s 11: the Authority "may, with the approval of the Minister, make an ex gratia payment"
to a person damaged by the exercise of its powers. Combined with s 16(1) (entry free
of legal proceedings) and s 20 (good-faith protection, not encoded), the Act gives a
person damaged by URA's lawful activity no entitlement of its own. Asserted (the
discretion; s 20 is not encoded).

### 7. Smaller points

- s 8(3): a declaration of an urban redevelopment area must state the land may be
  acquired within 3 years, or a period the President extends; s 8 itself does not say
  what follows once that period passes. Asserted (the period, in months).
- s 44(8): a s 44 notice cannot reach IRAS's functional information or JTC's s 35A
  information; s 44A gives URA a separate route to IRAS's property tax and stamp duty
  data for property statistics. Asserted (the s 44 bar).
- s 49 excludes liability only for information sold "on payment of a prescribed fee";
  free information is outside the section (an inference: the text is silent). Asserted.
- s 50 makes officers guilty only where consent, connivance or default is **proved**:
  the text puts no burden of disproof on the officer. Asserted.
- s 51A: composition up to $1,000, only for offences prescribed as compoundable.
  Asserted.
- Quorum is one-third of members or 3, whichever is higher: with 13 members, 5 are
  needed. Asserted.

## What would need doing before this is worth anything

- The regulations made under ss 17 and 51A (which offences exist and which are
  compoundable) were not retrieved; the penalties here are the Act's ceilings.
- The Planning Act 1998, where URA's planning control actually lives, is a separate
  subject and should be encoded for any question about building or change of use.
- The wilful-refusal reading of s 44(7)(a) and the ordinary-post mismatch in s 44(5)(b)
  need a lawyer's view; no case law was searched.
- s 20 (good-faith protection) and s 16(1)'s immunity were noted but not encoded as
  rules.
