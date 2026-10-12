# Singapore Polytechnic Act 1954 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/4/2024"), deposited at `../../registers/source-bundle/SPA1954.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the latest
amendment annotated is Act 4 of 2008 (Statutes (Miscellaneous Amendments) Act 2008),
"wef 01/04/2024", on s 7(3)(e)(v) and s 7A.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0213** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short (23 sections, ss 18-22 repealed) and mostly constitutes the Board.
This row takes what a student, fee-payer, diploma holder, lender or counterparty
meets: which instrument governs admission, awards, fees and discipline and how it is
made (ss 7(3)(d), (e), 23), late-payment charges and their validation (s 7A), the
common seal (s 12), the Students' Union (ss 15, 16), borrowing (s 11(1)), and the
governance rules that decide whether a Board decision was validly made (ss 4-6, 7(5),
9, 14(1), (4)), plus the financial year (s 17). Not encoded: establishment (s 3), the
Board's general functions, committees beyond s 7(5), the Secretary (s 8), contracts and
property (s 10), investment (s 11(2), (3)), shares for the Minister for Finance
(s 11A), the Board of Studies (s 13), the Principal's responsibilities (s 14(2), (3)),
other officers (s 14A) and regulation heads other than s 23(1)(d), (e). No by-laws or
regulations were retrieved.

## What the Act turns out to say

### 1. A 2008 amendment came into force in 2024, and validates sixteen years of late fees

s 7(3)(e)(v) lets the Board make by-laws on fees "including charges for the late
payment of any such fee or charge", annotated "[Act 4 of 2008 wef 01/04/2024]". The
legislative history lists Act 4 of 2008 with Third Reading on 22 January 2008 and
commencement on 1 April 2024. s 7A deems every amount collected as a late-payment
charge "before the date of commencement" of that Act "to be and always to have been
validly collected", and "no legal proceedings shall lie". So a late charge collected on
31 March 2024 is validated and cannot be challenged; one charged from 1 April 2024
rests on s 7(3)(e)(v) itself. s 7A still cites "section 7(2)(e)(v)"; a footnote says to
construe it as s 7(3)(e)(v), and the comparative table shows the 1985 s 7(2) split into
s 7(2) and (3) in the 2020 edition. Asserted.

### 2. Admission and diplomas are by-laws; student discipline is regulations

Admission qualifications, courses, the award and revocation of certificates and
diplomas, and scholarships are by-laws the Board makes "after consultation with the
Board of Studies" (s 7(3)(d)). Fees, including late charges, are by-laws with no
consultation step (s 7(3)(e)). The Act names no ministerial approval or publication for
either. "The conduct and disciplinary control of students", and staff discipline and
dismissal, are regulations made "with the approval of the Minister" and "must be
published in the Gazette" (s 23(1)(d), (e), (2)). s 7(3)(g) also lists student
discipline among the Board's functions; sending it to s 23 is the encoding's
inference. Whether an unpublished regulation is invalid is not said. Asserted.

### 3. A diploma needs no witnesses to the seal

s 12: the seal is in the Principal's custody and may not be affixed to any instrument
"other than diplomas or academic certificates" except in the presence of the
Chairperson or a Board member and the Principal, both signing. Diplomas and academic
certificates are outside that rule. Asserted.

### 4. The Principal's seat can be vacated, but not revoked, resigned or refilled

s 5(1) vacates "the office of a member of the Board" on bankruptcy or composition with
creditors, or on absence without leave from 3 consecutive meetings, and does not
except the Principal. s 5(2) (revocation for unfitness), s 5(3) (resignation by
written notice to the Minister) and s 6 (the Minister filling a vacancy for the
remainder of the predecessor's term) all do. The Board is 12 to 18 members (s 4(2));
appointed members serve 3 years unless the Minister directs otherwise (s 4(3)).
Asserted.

### 5. The Board borrows without the Minister for Finance

s 11(1): the Board "may borrow at interest, on the security of any corporate land or
of any funds of the Board", for carrying the Act into effect. No ministerial approval
is named. Reading s 11(1) as authorising only secured loans is an inference. Asserted.

### 6. Votes, records and the Union

Quorum 6; simple majority of those present and voting; on a tie, the Chairperson or in
the Chairperson's absence the Deputy has the casting vote (s 9(2), (3)). A tie with both
absent is read as not carried (inference). Committee proceedings are open to "any
member of the Board or any member of the committee" (s 7(5)), and no one else. The
Principal votes at a committee only as a member (s 14(4)) and may be removed "for good
cause" (s 14(1)). The Societies Act 1966 applies to the Students' Union "despite
anything to the contrary" in it, unless exempted by Gazette order (s 16), and Union fees
may be applied as the Board thinks fit for the Union's purposes (s 15(3)). Asserted.

## What would need doing before this is worth anything

- The by-laws (admission, fees, awards) and the s 23 regulations (student discipline,
  the Students' Union) were not retrieved; they decide most of what a student meets.
- The Public Sector (Governance) Act 2018 provisions that govern the Principal's
  removal (s 14(2)) and the Board's standing orders (s 9(8)) were not read.
- Act 4 of 2008 itself was not read; the 1 April 2024 date is from the legislative
  history and the annotations.
- No case law was searched.
