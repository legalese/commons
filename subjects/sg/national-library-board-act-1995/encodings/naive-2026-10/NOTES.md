# National Library Board Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, deposited at
`../../registers/source-bundle/NLBA1995.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment annotated in the body is Act 25 of 2023,
in force 1 December 2023 (s 15(3), oaths by live video link), which is not encoded.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0191** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

Most of the Act sets up the Board and moves property and staff to it. This row
takes what reaches a publisher, a producer of recordings or a member of the public:
legal deposit (ss 2, 10), the Board's copying of Singapore websites (s 7(2)(g)),
public archives (s 2), destroying, inspecting, reproducing and exporting public
records (ss 17, 18, 20, 21), recordings on request (s 22), the Board's symbol
(s 44), composition (s 45) and the penalty ceiling for regulations (s 47(2)(j)).
Not encoded: the Board's constitution, functions and powers (ss 3-9, 13, the
Schedule), the national union catalogue and interlibrary loans (ss 11, 12, which bind
publicly funded libraries, not people), the Director of National Archives and oral
history centres (ss 15, 23), the transfers from the Government and the National
Heritage Board (ss 24, 25, 36-43), staff and finance (ss 26-35), personal protection
(s 46), and every regulation — no subsidiary legislation was retrieved, so library
rules, late-return charges, deposit exemptions and the list of compoundable offences
are all unknown here.

## What the Act turns out to say

### 1. Destroying a public record without authority carries no penalty in the Act

s 17(1) says a person "must not, without the authorisation of the Board", destroy or
dispose of public records, and (2) requires notice to the Board first. But unlike
ss 20, 21 and 22, s 17 has no penalty subsection, and neither has s 18 (inspecting
unreleased records). Any sanction would have to come from regulations under
s 47(2)(c) and (j), capped at a $5,000 fine; none was read. Damaging a record, by
contrast, is an offence under s 21 with up to 12 months. Asserted (compliance with
s 17 is encoded; the absence of a penalty is a reading of the Act, not asserted).

### 2. Failing to deposit a book is fine-only; failing to hand over a recording can mean jail

A publisher who does not deposit faces "a fine not exceeding $5,000" (s 10(3)) and
no imprisonment. A producer or distributor who does not provide a recording within 6
months of the Board's written request faces $5,000 or 12 months or both (s 22(2)).
Reproducing archives without consent and taking public records abroad or damaging
them also carry 12 months; misusing the Board's symbol 6 months (s 44(2)).
Asserted.

### 3. Websites are harvested, not deposited

s 10(1) excludes "online material" from legal deposit, and "published in Singapore"
is defined only for library materials "other than online material". Instead
s 7(2)(g) lets the Board copy "any online material made available on a Singapore
website" — one with a Singapore country-code domain or a prescribed site — "at the
times and in the manner the Board considers appropriate". The Act puts no duty on
the site owner. Asserted.

### 4. Two copies in print, one electronic copy without DRM, within 4 weeks

s 10(1): two copies of a printed work, or one copy of an electronic work "free of any
technological or other restriction on access", within 4 weeks after first
publication, at the publisher's own expense. The encoding reads 4 weeks as 28 days
and asserts day 28 inside and day 29 outside. A locked e-book is a contravention.
Asserted.

### 5. Public archives must be MORE than 25 years old

s 2: public archives are public records "more than 25 years old", specified by the
Board as of national or historical significance, and transferred to it. A record
exactly 25 years old is not yet public archives. Asserted.

### 6. Only export has a permission route

s 21(1)(a) forbids taking public records out of Singapore "without the written
permission of the Board"; (b) defacing and (c) damaging have no exception at all.
And s 21 reaches "any public records", not only those transferred to the National
Archives — unlike s 20, which covers only transferred records and deposited
recordings. Asserted.

### 7. Compounding is capped at $500

s 45: an authorised officer may compound a prescribed offence for "a sum not
exceeding $500"; the money goes to the Consolidated Fund. Asserted.

## What would need doing before this is worth anything

- The National Library Board regulations (deposit exemptions, library rules, late-
  return charges, compoundable offences) were not retrieved; s 17 may have a penalty
  there.
- The meaning of "4 weeks" as 28 days and of "6 months" as calendar months are
  inferences; no date arithmetic is modelled.
- "Publisher" (s 2: "any person who arranges for any library material to be
  published in Singapore") is not modelled; the encoding assumes one is identified.
- No case law was searched.
