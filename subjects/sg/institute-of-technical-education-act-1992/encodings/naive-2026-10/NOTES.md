# Institute of Technical Education Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/7/2026), as deposited at `../../registers/source-bundle/ITEA1992.txt`. The latest
amendment annotated is Act 17 of 2026 (Skills and Workforce Development Agency Act
2026), in force 1 July 2026, which adds s 5(c).

**Checks:** one module (`itea-public.l4`), one case file (`itea-cases-public.l4`),
51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0175** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

Most of the Act constitutes and finances a statutory board. This row takes what
reaches people outside it: fees and late-payment charges (ss 6(1)(i), 6A), the
protection of the Institute's people from suit (s 24), the symbol and certificate-title
offences (ss 35, 36), compulsory insurance and work-injury cover for trainees
(ss 37, 38), returns from employers and their confidentiality (s 39), obstruction
(s 40), prosecution (ss 41-43), and vacation of office by a Board member (s 9). Not
encoded: establishment, seal, functions and the other powers (ss 3-6), the rest of the
Board's constitution and procedure (ss 7, 8, 10-15), the 1992 transfer from the
Vocational and Industrial Training Board (ss 16-19, 45), staff (ss 22, 23), finance
(ss 26-29) and regulations (s 44).

## What the Act turns out to say

### 1. A validation that reaches back sixteen years

s 6A deems valid every late-payment charge collected "before the date of commencement
of the Statutes (Miscellaneous Amendments) Act 2008", and bars proceedings over it. The
deposit's legislative history gives that Act's second and third readings as 22 January
2008 but its commencement as **1 April 2024**, and s 6(1)(i)(ii), the express power to
charge for late payment, carries the same "wef 01/04/2024" annotation. On the text as
deposited, then, late charges collected up to 31 March 2024 are validated, though the
Act was passed in 2008. Whether the 2024 date is a real deferred commencement or an
error in the consolidation cannot be told from the deposit (this is an observation, not
a finding of error). Asserted on the deposited date.

### 2. Confusing resemblance is caught for the symbol, not for certificate titles

s 35(2) catches a symbol "identical with" the Institute's "or which so resembles" it as
to be likely to deceive or confuse. s 36(2) catches only certificate titles "identical
with those of the Institute"; it has no resemblance limb. Both carry a fine up to
$2,000. Asserted.

### 3. Read literally, s 36(2) has no exception for the Institute's own graduates

s 36(1) gives the Institute an exclusive right in titles "issued by the Institute to any
person who attains the standard set by the Institute", but s 36(2) makes it an offence
for "any person" who "uses" an identical title, with no carve-out for the person to whom
it was issued. That a court would read one in is an inference; the text does not say
so. Not asserted (the encoding does not model the holder).

### 4. An employer's returns are confidential, but not from criminal or s 39 proceedings

The Chief Executive Officer may require any employer "in commerce or industry" to
furnish returns and keep records (s 39(1)). Without the employer's consent they may go
only to the Institute, its committees and officers, or persons entitled to take part in
its proceedings (s 39(2)), except as an anonymised summary of "a number of employers",
or for legal proceedings under the Act, "any criminal proceedings, whether pursuant to
this Act or not", or a report of them (s 39(3)). Civil proceedings under another law
are not in the exception. Unlawful disclosure is an offence (s 39(6)(c)). Asserted.

### 5. Only one offence has a repeat tier, and none carries prison

Failing to comply with a s 39(1) requirement: up to $1,000, $2,000 on a second or
subsequent conviction (s 39(5)). False returns, false entries, unlawful disclosure
(s 39(6)), obstruction (s 40) and ss 35, 36: up to $2,000, with no repeat tier. No
offence in the Act carries imprisonment. Every prosecution needs the Public Prosecutor's
consent (s 42), and an Institute employee may conduct it only with the Public
Prosecutor's authorisation (s 41). Asserted.

### 6. Training counts as work for work-injury compensation

s 38(2): for the Work Injury Compensation Act 2019, an act an employee does "for the
purposes of and in connection with" training at a course or facility "provided or
approved by the Institute" is deemed done for the employer's trade or business, even if
it was not. The Institute may also require any trainee to be insured against personal
injury and loss of life (s 37). Asserted.

### 7. The individual is protected, not the Institute

s 24 bars suits against a member, employee or person acting under the Institute's
direction for anything done "in good faith" in the execution or purported execution of
the Act. The Institute itself is not named and may be sued (s 3(a)). Asserted for the
individual.

## What would need doing before this is worth anything

- The regulations under s 44 (fees, scholarships, apprenticeships) were not retrieved;
  the actual fees and late charges are unknown.
- The commencement date of Act 4 of 2008 (finding 1) should be checked against the
  Government Gazette or the 2008 Act itself.
- No case law was searched, in particular on s 36(2) and on s 38 claims.
- s 9 (vacation of office) is encoded but serves Board members, not the public.
