# Independent test report: Civil Dispute Resolution Act 2011

Expectations: `independent-expectations.md` (19 scenarios, written from BRIEF.md and the source text before any L4 was read).
Tests: `tests-independent.l4` (25 assertions against `the dispute position for`).

## Result

`L4=~/.local/bin/l4 ./check.sh .` : tests-independent.l4 — **23 satisfied, 2 failed**, no other errors.

## Disagreements

### 1. Commencement of Part 2 is not modelled (scenario 9) — confidence: high
Application filed 31 July 2011 in the Federal Court, ordinary civil proceedings. Expected: no obligation, because ss 6-19 (Parts 2-5) commenced on 1 August 2011 (s 2(1) item 2; endnote 3: "s 6–19: 1 Aug 2011"). The encoding returns `I must file = TRUE`: `the day the application is filed` is only used as the applicant's deadline, never tested against the commencement date. The brief itself records "Parts 2-5 commenced on 1 August 2011" and asks for dates "as the Act gives them". Practical significance is small (filings before 2011), but it is the one date edge in the Act.

### 2. Respondent given a copy in wholly excluded proceedings (scenario 19) — confidence: low
s 7(1): "A respondent in proceedings who is given a copy of a genuine steps statement filed by an applicant in the proceedings must file ...". The exclusion in s 6(3) is expressed only for "subsection (1)" of s 6; s 7 has no equivalent carve-out. If an applicant files a statement voluntarily in wholly excluded (e.g. ex parte) proceedings and serves it, a literal reading still obliges the respondent. The encoding gates the respondent's duty on `NOT wholly excluded`. The encoding's reading is purposive and arguably defensible (s 5 defines "genuine steps statement" for a respondent by reference to s 7, and a voluntary statement may not be "a genuine steps statement filed by an applicant" under s 6); I record it as a finding to be decided by a reviewer, not as a clear error.

## Agreements (all satisfied)
Eligible court both ways (FCA, FCFCOA Div 2, another court); civil vs not civil; wholly excluded (ex parte s 15(h), listed Act s 16(1)(e), appellate s 15(d)); part-excluded must file and may leave out excluded parts (s 6(4)); commencement day itself (1 Aug 2011) obliges; respondent with/without a copy; respondent's last day = day before hearing date, including across a year end and on 29 Feb 2024; s 10(2) non-invalidation for both sides; ss 11-12 court may weigh only where the person was required to file (not in another court, not in wholly excluded proceedings).

## Observations not asserted
- `it may leave out the excluded parts` is TRUE for a respondent in part-excluded proceedings too. s 6(4) speaks only of a statement filed under s 6(1); the respondent's content is out of scope (s 7(2)), so not tested.
- `not filing invalidates the proceedings` is hard-coded FALSE; correct per s 10(2), but it carries no information.

## Coverage gaps
- Individual s 15 / s 16 / s 17 kinds other than the three tested are all one enum branch (any non-`ordinary` kind is excluded), so they are covered structurally rather than one-by-one.
- The input model allows only one kind per case; proceedings that are partly one excluded kind and partly another cannot be expressed (they would still be wholly excluded).
- s 11(b) / s 12(1)(b) ("took genuine steps") are folded into one boolean output; not separately testable.

## Change after the pass (encoder)

- Both disagreements were accepted: Part 2 commences on 1 August 2011, and a respondent given a copy must file even in wholly excluded proceedings (s 7(1)). Section 6(4) now applies to the applicant only.
- The gaps are recorded as known limits in NOTES.md.
