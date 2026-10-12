# Temasek Polytechnic Act 1990 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1/4/2024, as deposited
at `../../registers/source-bundle/TPA1990.txt`. The latest amendment annotated is Act 4
of 2008 (Statutes (Miscellaneous Amendments) Act 2008), marked "wef 01/04/2024"; the
legislative history gives its commencement as 1 April 2024.

**Checks:** one module, one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0224** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a sharper
question yet. Most of the Act is the Polytechnic's own governance. This row takes what a
student, a contracting business, a donor or a Board member meets: who is a registered
student (s 2), awards (s 11, Schedule s 11(1)(d)), late-payment charges (ss 4(2)(c), 4A),
contracts and the seal (ss 12, 13), regulations and the Gazette (s 9, Schedule ss 6(4),
12(2)), ending a student's studies (Schedule ss 6(3)(c), 11(1)(g)), the Students' Union
(s 16, Schedule s 19), the Board's size, terms and votes (Schedule ss 5, 8, 9), the Senate
(Schedule s 10) and the financial year and donations (Schedule ss 14, 17, 18).

Not encoded: establishment and objects, the general powers of the Board and Senate,
Schools, committees, officers and staff, examinations, grants-in-aid, shares, the Standing
Finance Committee and estimates. No regulations made under the Polytechnic Constitution
were retrieved, so actual fees, late charges, admission and discipline rules are unknown.

## What the Act turns out to say

### 1. A late-payment charge collected before 1 April 2024 cannot be challenged in court

s 4A deems every late-payment charge collected "before the date of commencement of the
Statutes (Miscellaneous Amendments) Act 2008" validly collected, and "no legal proceedings
shall lie". That Act had its third reading on 22 January 2008, but the legislative history gives
its commencement as **1 April 2024**, so the validation reaches back over sixteen years of
collections; the late-payment words in s 4(2)(c) are annotated "wef 01/04/2024" too. The date comes from the legislative history, which says it "is not part of the
Act". Asserted (31 March 2024 barred; 1 April 2024 not).

### 2. A person who is not a registered student can get a certificate, not a diploma

s 11(b) lets the Polytechnic teach persons who are not registered students "and to grant
certificates to those persons". Diplomas appear only in s 11(a). Confining diplomas to
registered students is an inference from that contrast. Asserted.

### 3. The Constitution speaks of degrees; the Act gives no power to award one

Schedule s 12(1)(b) lets the Senate regulate "the conditions for the award of degrees,
diplomas, certificates", but s 11 confers power to award only "diplomas and certificates and
any other academic distinctions specified in the regulations". The encoding gives no power
to award a degree; a degree specified in the regulations as an academic distinction might
arguably fall under s 11(a). Asserted, as a reading.

### 4. The rules that govern students are not law you can look up in the Gazette

s 9(5): regulations made under the Polytechnic Constitution "need not be published in the
Gazette and are not subsidiary legislation". Amendments of the Constitution itself must be
gazetted (s 9(3)). Board regulations operate on the day they are made; Senate regulations
not earlier than one semester later, unless the Board approves otherwise (Schedule ss 6(4),
12(2)). Asserted.

### 5. The court presumes the seal; a business need not prove the Board's resolution

s 13(3): courts "are to assume that it was duly affixed" until the contrary is proved. A
contract that between private persons would need to be under seal binds the Polytechnic
under s 12(2) if made under the common seal, unless improper sealing is proved; a
signed-writing contract needs a signature by a person with the Board's express or implied
authority; an oral one, only that authority. s 12 says "may", so whether a contract made
otherwise binds is left open. Asserted.

### 6. Academic failure and misconduct go to different bodies

The Senate may require a student "on academic grounds to terminate his or her studies"
(Schedule s 11(1)(g)); suspension and expulsion are for the Board's regulations (Schedule
s 6(3)(c)). Asserted.

### 7. Board and Senate arithmetic

The Board has 9 to 15 members besides the Chairperson, Deputy Chairperson and Principal;
appointments run 3 years unless the Minister directs otherwise, and a vacancy is filled for
the predecessor's remaining term. Quorum is 6; a tie goes to the Chairperson's or Deputy
Chairperson's casting vote, and a member elected to preside in their absence is given none.
The Senate's quorum is "the smallest number which is not less than one-quarter" of its
members (21 members: 6). The Students' Union is under the Societies Act "despite anything
to the contrary" in it, unless exempted by Gazette order (s 16). Asserted.

## What would need doing before this is worth anything

- The regulations made by the Board and the Senate (fees, late charges, admission,
  discipline, the Students' Union) were not retrieved; they are not gazetted.
- The Statutes (Miscellaneous Amendments) Act 2008 was not read; the 2024 commencement
  is taken from the legislative history only.
- No case law on the Polytechnic or on s 4A was searched.
