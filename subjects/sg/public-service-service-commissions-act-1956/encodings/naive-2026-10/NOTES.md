# Public Service (Service Commissions) Act 1956 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PSSCA1956.txt`, marked "Informal Consolidation – version
in force from 14/1/2022". The deposit says the revised edition "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021"; the deposit's metadata records it as the current version as at
1 October 2026. The latest amendment annotated is Act 33 of 2021 (Judicial Service
(Miscellaneous Amendments) Act 2021), in force 14 January 2022.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0200** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act has eight sections, so the row takes all of it: the definition of a
Commission (s 1A), false information (s 2), the privilege over communications (s 3),
unauthorised disclosure and onward publication (s 4), the members' protection (s 5),
influencing a Commission (s 6), and the Public Prosecutor's consent (s 7). Section 8 is
repealed. Not encoded: the Constitution's provisions on the Commissions and personnel
boards, which s 1A only points to, and the content of a Magistrate's protection,
which s 5 borrows from another law that was not read.

## What the Act turns out to say

### 1. Trying to sway a Commission is a crime, whoever you are and however you try

s 6(1) catches every person who, "otherwise than in the course of his duty directly or
indirectly by himself or by any other person in any manner whatsoever influences or
attempts to influence" a decision of a Commission or a member: $2,000 or 2 years. No
payment, corrupt motive or success is needed, so a parent phoning a member about a
child's scholarship, or an uncle getting a friend to put in a word that fails, both
commit the offence. The only carve-out besides acting in the course of duty is s 6(2):
giving "a certificate or testimonial" to an applicant. Asserted.

### 2. A candidate cannot make the Commission produce its own exchanges with them

s 3 bars producing or disclosing, in any legal proceedings, any communication between
a Commission or a member and the Government, the President, a Minister, a head of
department "or any other person", unless the President consents in writing. "Any other
person" reaches the candidate. The words "in exercise of or in connection with the
exercise of the functions" attach only to communications between members, so a
members' private exchange is outside the privilege. Asserted.

### 3. Passing on a leak is its own offence, with one narrow exception

s 4(2): anyone holding information which "to his knowledge" was disclosed in breach of
s 4, who publishes or communicates it to another, commits an offence ($1,000 or one
year), unless it is "for the purpose of a prosecution under this Act". The subsection
names no exception for the President's permission and none for the public interest.
Someone who does not know the information was leaked is not caught. Asserted.

### 4. The disclosure offence has two limbs and needs knowledge

s 4(1) forbids a member "or any other person" to disclose what they learned in their
duties "to any unauthorised person or otherwise than in the course of the duty" without
the President's written permission. Telling an authorised officer outside any duty
still contravenes the second limb. The offence needs the person to act "knowingly",
so an accidental leak contravenes the subsection but is not an offence. Asserted.

### 5. Lying to a Commission is caught whoever lies and whoever's application it is

s 2 punishes "any person" who wilfully gives false or misleading information, in a
material particular, in connection with an application "by any person" or any matter
the Commission must act on, and it covers information given to anyone the Commission
appointed to assist it: $2,000 or 2 years. A referee is caught as much as the
applicant; an honest mistake is not. Asserted.

### 6. The Act now covers three Commissions and their personnel boards

s 1A: "Commission" means the Public Service, Judicial Service and Legal Service
Commissions and includes personnel boards under Articles 110D, 111I and 111Q of the
Constitution. The legislative history calls the 2020 Revised Edition the "Public
Service Commission and Legal Service Commission Act 1956"; ss 1 and 1A are annotated
"[Act 33 of 2021 wef 14/01/2022]". That Act 33 of 2021 renamed the Act and brought in the
Judicial Service Commission is an inference from those annotations, not stated in the
text. Asserted (the definition only).

### 7. No prosecution without the Public Prosecutor

s 7: a prosecution under the Act needs to be brought "by or with the consent of the
Public Prosecutor or his deputy". Asserted.

### 8. The arrangement of sections is one line out of step

The deposit's arrangement lists "1A. Short title" and "2. Interpretation", but the body
has s 1 as the short title and s 1A as the interpretation, and so on down to s 7. This
row follows the body. Not asserted.

## What would need doing before this is worth anything

- The Constitution's articles on the Commissions and personnel boards (110D, 111I,
  111Q and their neighbours) were not read, so who sits on a Commission and what
  matters it "must act on" are not encoded.
- What a Magistrate's protection amounts to (s 5) was not traced.
- What repealed s 8 said was not looked up.
- No case law on s 6 (for example, whether an MP's letter on a constituent's behalf is
  "in the course of his duty") was searched.
