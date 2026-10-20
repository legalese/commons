# Australian Citizenship Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example encodings and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** Compilation No. 37, compilation date 4 June 2026 ("Includes amendments:
Act No. 75, 2025"; register id C2026C00236), as deposited at
`../../registers/source-bundle/C2007A00020.txt` (retrieved 2026-09-22).

**Checks:** one module (`aca-citizenship.l4`), one case file
(`aca-cases-citizenship.l4`), 57 assertions satisfied, 0 errors, 0 warnings. The
cases are built by a generator in the session scratchpad
(`gen_australian-citizenship-act-2007.py`); every expected value was written by hand
from the text.

## Why this Act, and why scoped

Requirement **REQ-0006** in `subjects/au/requirements.jsonl`: priority 1, raised
**8 times** by the three Western Australian cradle-to-grave lives:

- chloe **c000** (born at KEMH, 14 Mar 2003) and **c062** (Oliver born, 5 Sep 2030):
  citizen by birth?
- jake **k000** (born at KEMH, 30 Aug 2006) and **k051** (Ruby born to unmarried
  parents, 22 Jan 2033): citizen by birth?
- daniel **d000** (born at KEMH, 9 Apr 1996) and **d040** (Luca born in Perth,
  2 Feb 2030): citizen by birth?
- daniel **d036** (Anjali born in London, 14 Jun 2027): is a child born abroad to a
  citizen a citizen, and by what step?
- daniel **d041** (Priya a citizen by conferral, 20 Jul 2030): what residence is
  required, and what does she give up?

The encoding takes those provisions first (ss 12, 16, 21-22, 26) and adds what they
need: commencement and the old Act (ss 2, 4), permanent residence (s 5), the
Minister's decision and the day citizenship begins for descent (ss 17, 19, 19A) and
for conferral (ss 20, 24, 25(3), 28).

Not encoded: the Australian Citizenship Act 1948 (not deposited); ships, posthumous
births, artificial conception and surrogacy (ss 7-8); adoption, abandoned children
and incorporated territory (ss 13-15); Hague adoptions (Subdivision AA); births before
26 January 1949 (s 16(3)); the other conferral routes in s 21(3)-(8) except as
exemptions from the pledge; the special residence and defence service requirements
(ss 22A-23); the citizenship test's content (s 23A determination); resumption;
renunciation, revocation and cessation (Division 3); evidence, personal identifiers,
review, fees and the regulations.

Facts the lives do not state are **assumptions** in the case file, labelled there:
Graham's and Sue's citizenship at Chloe's and Jake's births; Priya's application
date (taken as 1 Mar 2030) and approval date (15 May 2030); when the London year
ended; and Anjali's approval date (1 Sep 2027).

## What the Act turns out to say

### 1. Priya's London year sits on the 12-month line, and nothing in the lives says which side

s 22(1)(a) wants four years' presence before the application. s 22(1A) treats
absences as presence only if "the total period of the absence or absences was not
more than 12 months"; one day over, and **none** of the absence counts. Priya left
for London on 9 Jan 2027 for "a year" (Daniel's life, Chapter 3) on a resident
return visa. If
she was back by 8 Jan 2028 and applied in 2030, she meets the requirement; if the
year ran longer, she does not, however long she then stays. The scenario's "after
four years' residence" is true only on the first reading. Asserted both ways.

### 2. Had she applied soon after London, only the spouse discretion would have saved her

s 22(1)(c) wants 12 months as a permanent resident in Australia immediately before
applying; s 22(1B) forgives absences of "not more than 90 days" only. An application
in mid-2028, five months after returning (221 days abroad in the 12 months, on the
case file's assumed dates), fails, unless the Minister uses s 22(9): the spouse of a
citizen who was a permanent resident while abroad and kept "a close and continuing
association with Australia". If the Minister does, s 24(5) also lifts the rule that
she must be in Australia when the Minister decides. 90 days passes; 100 fails.
Asserted.

### 3. Chloe, Jake and Daniel were born before the Act, and the Act sends their births to the 1948 Act

The lives cite s 12 of the 2007 Act for births in 1996, 2003 and 2006. Sections 2A-54
commenced on 1 July 2007 (s 2 table, column 3). s 4(2): whether a person "was an
Australian citizen at a time before the commencement day" is worked out "under the
Australian Citizenship Act 1948 as in force at that time"; s 5(3) does the same for
permanent residence. Their citizenship now rests on s 4(1)(b): a citizen under the
1948 Act immediately before 1 July 2007 who has not ceased to be one. The 1948 Act is
not deposited, so its answer is an input. (s 12's own words are not limited to births
after commencement, and the encoding also gives them s 12 on the assumed facts; how
the two routes fit together is a question for the transitional Act, which was not
read. That is an inference, not a reading.) The lives also give Graham and Sue no
citizenship, so for Chloe and Jake even the s 12 input is an assumption. Daniel's is
in the facts: his father was "Australian citizen by conferral 1995". Asserted.

### 4. Anjali is not a citizen at birth; she becomes one on the day the Minister approves

s 16 makes her **eligible** to apply: born abroad after 26 January 1949 to a parent
who was a citizen at the birth. Daniel is a citizen by birth, not by descent, so the
two-years-in-Australia condition in s 16(2)(b) does not apply; she is under 18, so
no character test. s 17(2): the Minister **must** approve an eligible applicant who
clears identity, security and cessation (no residual discretion, unlike s 24(2)).
s 19: she becomes a citizen "on the day on which the Minister approves". Registration
(s 18) follows approval in the manner the regulations prescribe; it is not the step
the life names it as. On the assumed approval date she is not a citizen on 14 Jun
2027 and is on 1 Sep 2027. Asserted.

### 5. Priya became a citizen on the day she made the pledge, not on approval

s 26(1): an applicant aged 16 or over must pledge unless incapacitated or covered by
s 21(6)-(8). s 26(2): a pledge before approval "is of no effect"; s 26(3)-(6) let the
Minister delay it up to 12 months. s 28(1): a person required to pledge becomes a
citizen "on the day on which the person makes the pledge". s 25(3): an approval may
be cancelled if no pledge is made within 12 months of notice. That 20 Jul 2030 is
her ceremony day is an inference from the life. Asserted.

### 6. s 12 asks for "a parent", and says nothing about marriage

Oliver, Ruby and Luca are citizens by birth because a parent was a citizen (or, for
Luca, also because Priya was a permanent resident) when each was born. s 3 counts an
"exnuptial child" as a child, and s 12 has no condition about the parents' marriage,
so Ruby's unmarried parents make no difference (k051). A child of temporary visa
holders is not a citizen at birth but becomes one under s 12(1)(b) after ten years
ordinarily resident. The enemy-occupation exception in s 12(2) yields if the other
parent is a citizen or permanent resident. Asserted, except that the absence of a
marriage condition is a reading of what the section leaves out.

### 7. Eligible is not approved

s 24(2): "The Minister may refuse to approve the person becoming an Australian
citizen despite the person being eligible". The encoding can only say the Minister
**may** approve. Asserted in that form.

### 8. The Act asks nothing about what Priya gives up

Nothing in the provisions read requires an applicant to renounce another
citizenship. Her loss of Indian citizenship is Indian law (d041 marks it `CASE`).
Not asserted.

### 9. A permanent resident abroad is still a permanent resident

s 5(1)(b): a person outside Australia who holds a permanent visa, and held one in
Australia immediately before last leaving, is a permanent resident. Priya in London
in 2027 was one; on her temporary partner visa in 2025 she was not. Asserted.

## What would need doing before this is worth anything

- Deposit and encode the Australian Citizenship Act 1948 (as in force over time) and
  the Australian Citizenship (Transitionals and Consequentials) Act 2007, so that the
  three pre-2007 births can be answered rather than assumed.
- The scenario facts need Graham's and Sue's citizenship, Priya's application date
  and the end of the London year.
- The citizenship test determination (s 23A), the regulations (registration, the
  pledge arrangements, s 25(3) reasons, fees) and the s 5(2) determination were not
  retrieved.
- "12 months" in s 22(1A) is taken as a yes/no input; how it is counted in days
  (leap years, part days) was not settled.
- s 22(4A) (administrative error and unlawful presence) and the special residence
  requirements were not modelled.
- No case law or departmental policy was searched.
