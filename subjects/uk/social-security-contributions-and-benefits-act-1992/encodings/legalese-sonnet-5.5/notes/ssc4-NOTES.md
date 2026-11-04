# NOTES -- ssc4 (Social Security Contributions and Benefits Act 1992, lines 1912-2443 of `ukpga-1992-4.txt`: Part III ss 63-79, Part IV ss 80-93, Part V ss 94-111)

Status: written by part agent `ssc4` of run `iaw-ssc4`, on 2026-11-04. Checked, not proved: the numbers below come from `check.sh` and `srcrefs.py check` runs on the files named, and from the scripts in `work/` that built them.

## Source, and what "verified" means here

The source is a plain-text rendering made by a converter script from legislation.gov.uk (point in time 2026-07-08), read from `inputs/ukpga-1992-4.txt`.
It is not the official text, and nothing in this encoding is "verified against the official text".
The rendering omits the Act's tables (Schedule 4 among them) and shows repealed provisions as dotted lines; both facts shape the encoding (every Schedule 4 figure is an input; 22 coverage rows are blank).
Where `BRIEF.md` and the keel's `PLAN.md` could differ, the brief governs; I noticed no place in ssc4's ranges where they give different instructions, and where `PLAN.md` names a seam I used its input name.

## Seat

The seat is a person who works, is self-employed, or claims a contributory or non-contributory benefit, statutory pay or Child Benefit in Great Britain.
Layer 1 is the law, objectively (seven modules, each with a tests module).
Layer 2 is `ssc4-seat.l4` (143 questions, each beginning "Under section N," with `@export` and `@desc`, grouped under `§` headings in the text's order) and `ssc4-cases-seat.l4` (356 assertions, every question asked at least once).
A script (`work/placement.py`) walks the seat file and checks that every question sits under the heading whose section range holds its section number and that the section numbers never go backwards: 143 questions, 0 outside their heading, 0 out of order.
A seat question calls a layer-1 rule and never restates it; the records a rule expects are built inside the question from plain answers, and a record field the rule never reads carries a placeholder with a comment.
The Secretary of State's judgments ("the Secretary of State considers ...") are asked as facts the person can report from the decision.
Officials get no seat.
Reach, by script (`work/reach.py`): the seven layer-1 modules define 167 functions; the seat names 144 of them directly (143 as the head call of a question, one for each question, and `s 94(1) the personal injury is of a kind mentioned in section 94(1)` inside the WHERE block of `Under section 94(1)`) and 13 more are reached through another function they call (the helpers `s 70(1A) the days since the last Sunday`, `s 65(1)(b) the same day of the month some months from` and `s 103(6) the last day of a run of days ...` among them), so 157 are reached and **10 are not asked in the seat**.
The 10 not asked are, with the reason: `s 65(6)(a) the person may claim in advance` (a regulative DEONTIC cannot be returned as a plain answer; `Under section 65(6)(a), may I make my claim on this day` asks the same window through `s 65(6)(a) the claim may be made on the day`); `s 67(4)`, `s 67(5)`, `s 67(7)`, `s 72(10)`, `s 72(11)` and `s 72(13)` (definitions that bear on the care-home powers, not on the person); `s 104(4) the change is a modification` (defines a word in the regulation-making power in s 104(3)); and `s 109(5) the appropriate percentage for subsection (4)(a)` and `s 109(6) the appropriate percentage for subsection (4)(b)` (sums over a list of disablements; the per-disablement tests, `s 109(5) ... counts in the appropriate percentage` and its s 109(6) twin, are asked as `Under section 109(5)` and `Under section 109(6)`).
Every power to make regulations has no function and so no question.

## Files

All in this folder, ASCII names, all beginning `ssc4-`.

| file | what it holds | assertions satisfied |
| --- | --- | --- |
| `ssc4-attendance-allowance.l4` | ss 63-67 (descriptions of non-contributory benefits; attendance allowance; terminal illness; care homes) | |
| `ssc4-tests-attendance-allowance.l4` | tests, including 3 `#TRACE` runs of s 65(6)(a) | 121 |
| `ssc4-carers-allowance.l4` | s 70 (ss 68 and 69 are blank) | |
| `ssc4-tests-carers-allowance.l4` | tests | 80 |
| `ssc4-disability-living-allowance.l4` | ss 71-76 | |
| `ssc4-tests-disability-living-allowance.l4` | tests | 166 |
| `ssc4-guardians-and-aged.l4` | ss 77-79, with 1 regulative rule (s 77(9)) | |
| `ssc4-tests-guardians-and-aged.l4` | tests, including 1 `#TRACE` | 80 |
| `ssc4-increases.l4` | ss 86A-93 (ss 80-86 and 90 are blank) | |
| `ssc4-tests-increases.l4` | tests | 66 |
| `ssc4-industrial-injuries-general.l4` | ss 94-101 (s 102 is blank) | |
| `ssc4-tests-industrial-injuries-general.l4` | tests | 131 |
| `ssc4-disablement.l4` | ss 103-110 (s 111 is blank) | |
| `ssc4-tests-disablement.l4` | tests | 213 |
| `ssc4-seat.l4` | the seat layer: 143 questions | |
| `ssc4-cases-seat.l4` | the seat cases | 356 |
| `NOTES.md`, `PROGRESS.md` | this file and the working log | |

`ssc-core.l4`, `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` were supplied and are unchanged. `NEEDS-CORE.md` is not written: nothing in ssc4's ranges needed a change to the core (see Seams for the inputs taken instead).
Total: 1213 assertions satisfied (857 in the seven layer-1 test modules, 356 in the seat cases), 0 failed, 0 refused.
The scripts that built the modules from `work/src/*.in` (a `%%REF` macro expands to the `-- src:` quote lines and the `@ref`, generated by `srcrefs.py quote`, never retyped), the coverage table and the seat layer are in `../../../work/`; the `.l4` files here are the deposit.

## Test discipline

Expected values are hand-written from the text beside each assertion. No expected value was edited to match the code.
One assertion failed during development and is recorded here because it is a finding about me, not about the code: in `ssc4-cases-seat.l4`, `Under section 72(2), ...`, the first case, I had transcribed `NOTHING` where my own layer-1 test for the same dates (written from the text: the run begins on the day 3 months before the award, so the 3-month requirement is met, and it lasts to the end of the 6 months beginning with the award date) says `JUST FALSE`. I corrected the transcription from the layer-1 test, not from the program's output.
A mutation check showed the test harness can fail: replacing one `EQUALS JUST FALSE` by `EQUALS JUST TRUE` in the industrial injuries tests gave `failed=1`.
After the independent review (see "The independent reviewer's 13 failures" below), one expectation of my own changed: `s 94(3)` with evidence to the contrary went from NOTHING to JUST FALSE, in `ssc4-tests-industrial-injuries-general.l4:39` and in the seat case under `Under section 94(3)`, and one seat case was added (not in the course of the employment, with evidence: NOTHING). The reason is in the table below, not in the reviewer's expectation.
The same check on the seat cases, in a throwaway copy: changing one expected `JUST TRUE` under `Under section 109(5)` to `JUST FALSE` gave `failed=1`.
The seat cases are wiring tests: they check that plain answers reach the layer-1 rule through the record the question builds. Each expected value is that rule's answer for those facts, worked out by hand from the quoted text and not read off program output; where a seat case and the layer-1 test for the same function could disagree, the layer-1 test, written first and from the text, decides (the `Under section 72(2)` slip above is the one case where they did).
The two `#TRACE` outcomes that `check.sh` cannot see were compared by running the test files with both builds: `ssc4-tests-attendance-allowance.l4` gives 3 `FULFILLED` traces and `ssc4-tests-guardians-and-aged.l4` gives 1 on 1.6.98 and on 1.6.108 (each trace prints the word twice, so a count of the word reads 6 and 2 on both builds).
A regulative `MAY` that lapses also gives FULFILLED, and a `#ASSERT` cannot compare a DEONTIC, so a trace shows that the rule runs and nothing more; the window logic is asserted through `s 65(6)(a) the claim may be made on the day`.


## Coverage (ssc4)

Built by script (`work/units.py` seeds the units from the text's own numbering; `work/cov.py` assigns the dispositions and the L4 names and checks the lines; `work/covhead.py` writes this paragraph and the counts from the table, so none is typed by hand).
Every non-blank line of 1912-2443 falls in some row: 532 non-blank lines, 0 uncovered.
Audit counts: the script found **493 text units** (sections, headings, subsections, paragraphs, sub-paragraphs and dotted lines); after 9 splits of a heading that shares a line range with its body, and 21 added rows for defined terms, the table has **523 rows**.
Rows before: 493. Rows after: 523 (493 + 9 + 21).

Each row has exactly one disposition. Counts:

| disposition | rows |
| --- | --- |
| encoded | 314 |
| fork (see the fork register) | 48 |
| inert, reason 1 (not operative: headings) | 70 |
| inert, reason 2 (machinery: powers to make regulations, official decisions) | 69 |
| inert, reason 3 (text shown repealed or blank) | 0 (the dotted rows are counted below) |
| repealed or blank in this text | 22 |
| total | 523 |

Fork rows by fork: F1 3, F2 4, F3 1, F4 1, F5 8, F6 17, F7 7, F8 1, F9 1, F10 1, F11 1, F12 1, F13 1, F14 1.
There is no out-of-scope row and no deferred row. Inert reason 3 is not used: the rows the text shows as dotted lines carry the disposition "repealed or blank in this text".
The 70 reason-1 rows are the Part, cross-heading and section headings; the 69 reason-2 rows are the regulation-making powers and the decisions the Act leaves to an official, each named in the row.

| unit | lines | disposition | L4 name, reason or what the text shows |
| --- | --- | --- | --- |
| heading@- | 1912 | inert reason 1 | heading |
| s 63 heading | 1913 | inert reason 1 | heading |
| s 63 chapeau | 1914 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(a) | 1915 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(b) | 1916 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 63(c) | 1917 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(d) | 1918 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(e) | 1919 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(f) | 1920 | encoded | `s 63 the benefit is a non-contributory benefit under Part III` |
| s 63(f)(i) | 1921 | encoded | `s 63(f)(i) a Category C retirement pension is payable in the case described` |
| s 63(f)(ii) | 1922 | encoded | `s 63(f)(ii) a Category D retirement pension is payable to the person` |
| s 63(g) | 1923 | encoded | `s 63(g) an age addition is payable in the case described` |
| heading@63 | 1924 | inert reason 1 | heading |
| s 64 heading | 1925 | inert reason 1 | heading |
| s 64(1) | 1926 | encoded | `s 64(1) the person is entitled to an attendance allowance`; `s 64(1A) Allowance` |
| s 64(1)(a) | 1927 | encoded | `s 64(1) the person is entitled to an attendance allowance`; `s 64(1A) Allowance` |
| s 64(1)(b) | 1928-1929 | encoded | `s 64(1) the person is entitled to an attendance allowance`; `s 64(1A) Allowance` |
| s 64(1A) | 1930 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(1A)(a) | 1931 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(1A)(aa) | 1932 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(1A)(b) | 1933 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(1A)(c) | 1934 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(1A)(d) | 1935 | encoded | `s 64(1A) Allowance`; `s 64(1A) the allowance is within this subsection` |
| s 64(2) | 1936 | encoded | `s 64(2) Day attendance facts`; `s 64(2) the person satisfies the day attendance condition` |
| s 64(2)(a) | 1937 | encoded | `s 64(2) Day attendance facts`; `s 64(2) the person satisfies the day attendance condition` |
| s 64(2)(b) | 1938 | encoded | `s 64(2) Day attendance facts`; `s 64(2) the person satisfies the day attendance condition` |
| s 64(3) | 1939 | encoded | `s 64(3) Night attendance facts`; `s 64(3) the person satisfies the night attendance condition` |
| s 64(3)(a) | 1940 | encoded | `s 64(3) Night attendance facts`; `s 64(3) the person satisfies the night attendance condition` |
| s 64(3)(b) | 1941 | encoded | `s 64(3) Night attendance facts`; `s 64(3) the person satisfies the night attendance condition` |
| s 64(4) | 1942 | inert reason 2 | power to prescribe circumstances in which the day and night conditions are taken to be met or not met |
| s 65 heading | 1943 | inert reason 1 | heading |
| s 65(1) | 1944 | fork F1 | `s 65(1) the period is one for which the person is entitled to an attendance allowance`; `s 65(1)(b) the preceding period is not less than 6 months` |
| s 65(1)(a) | 1945 | encoded | `s 65(1) the period is one for which the person is entitled to an attendance allowance` |
| s 65(1)(b) | 1946 | fork F2 | `s 65(1)(b) the same day of the month some months from`; `s 65(1)(b) the preceding period is not less than 6 months` |
| s 65(2) | 1947 | encoded | `s 65(2) the person is deemed to satisfy or to be likely to satisfy the day or the night attendance condition or both` |
| s 65(3) | 1948 | encoded | `s 65(3) the weekly rate of the attendance allowance in pounds` |
| s 65(4) | 1949 | encoded | `s 65(4) the person is barred from an attendance allowance for the day by the date of claim` |
| s 65(5) | 1950 | inert reason 2 | power to make regulations entitling a person for a period before the claim |
| s 65(6) | 1951 | encoded | `s 65(6)(a) the claim may be made on the day`; `s 65(6)(a) the person may claim in advance`; `s 65(6)(b) the condition on an award made on a claim made in advance is satisfied` |
| s 65(6)(a) | 1952 | encoded | `s 65(6)(a) the claim may be made on the day`; `s 65(6)(a) the person may claim in advance` |
| s 65(6)(b) | 1953 | encoded | `s 65(6)(b) the condition on an award made on a claim made in advance is satisfied` |
| s 65(6)(b)(i) | 1954 | encoded | `s 65(6)(b) the condition on an award made on a claim made in advance is satisfied` |
| s 65(6)(b)(ii) | 1955 | encoded | `s 65(6)(b) the condition on an award made on a claim made in advance is satisfied` |
| s 65(7) | 1956 | encoded | `s 65(7) the person is barred from an attendance allowance for the period by the Regulations` |
| s 66 heading | 1957 | inert reason 1 | heading |
| s 66(1) | 1958 | encoded | `s 66(1)(a)(i) the person is taken to satisfy both the day attendance condition and the night attendance condition on the day`; `s 66(1)(a)(ii) the first day of the period for which the person is taken to have satisfied the conditions`; `s 66(1)(b) the day is in the period for which the person is entitled to attendance allowance` |
| s 66(1)(a) | 1959 | encoded | `s 66(1)(a)(i) ...`; `s 66(1)(a)(ii) ...` |
| s 66(1)(a)(i) | 1960 | encoded | `s 66(1)(a)(i) the person is taken to satisfy both the day attendance condition and the night attendance condition on the day` |
| s 66(1)(a)(ii) | 1961 | fork F2 | `s 66(1)(a)(ii) the first day of the period for which the person is taken to have satisfied the conditions` |
| s 66(1)(b) | 1962 | encoded | `s 66(1)(b) the day is in the period for which the person is entitled to attendance allowance` |
| s 66(2) | 1963 | encoded | `s 66(2)(a) the person is terminally ill at the time`; `s 66(2)(b) the other person is regarded as making the claim` |
| defined term "terminally ill" (s 66(2)) | 1963-1965 | encoded | `s 66(2)(a) the person is terminally ill at the time` |
| s 66(2)(a) | 1964 | encoded | `s 66(2)(a) the person is terminally ill at the time` |
| s 66(2)(b) | 1965 | encoded | `s 66(2)(b) the other person is regarded as making the claim` |
| s 67 heading | 1966 | inert reason 1 | heading |
| s 67(1) | 1967 | inert reason 2 | power to make regulations on treatment for renal failure |
| s 67(2) | 1968 | inert reason 2 | power to make regulations that attendance allowance is not payable for a care home resident |
| s 67(3) | 1969 | encoded | `s 67(3) the establishment is a care home` |
| defined term "care home" (s 67(3)) | 1969 | encoded | `s 67(3) the establishment is a care home` |
| s 67(4) | 1970 | encoded | `s 67(4) Service`; `s 67(4) the service is a qualifying service for the purposes of subsection (2)` |
| defined term "qualifying services" (s 67(4)) | 1970-1973 | encoded | `s 67(4) Service` |
| s 67(4)(a) | 1971 | encoded | `s 67(4) Service`; `s 67(4) the service is a qualifying service for the purposes of subsection (2)` |
| s 67(4)(b) | 1972 | encoded | `s 67(4) Service`; `s 67(4) the service is a qualifying service for the purposes of subsection (2)` |
| s 67(4)(c) | 1973 | encoded | `s 67(4) Service`; `s 67(4) the service is a qualifying service for the purposes of subsection (2)` |
| s 67(5) | 1974 | encoded | `s 67(5) the enactment is a specified enactment` |
| defined term "specified" enactment (s 67(5)) | 1974 | encoded | `s 67(5) the enactment is a specified enactment` |
| s 67(6) | 1975 | inert reason 2 | the power to specify an enactment includes power to specify it for a purpose |
| s 67(7) | 1976 | encoded | `s 67(7) the provision is within the word enactment in this section` |
| defined term "enactment" (s 67(7)) | 1976 | encoded | `s 67(7) the provision is within the word enactment in this section` |
| heading@67 | 1977 | inert reason 1 | heading |
| s 68 heading | 1978 | inert reason 1 | heading |
| s 68 DOTS | 1979 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 69 heading | 1980 | inert reason 1 | heading |
| s 69 DOTS | 1981 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| heading@69 | 1982 | inert reason 1 | heading |
| s 70 heading | 1983 | inert reason 1 | heading |
| s 70(1) | 1984 | encoded | `s 70(1) the person is entitled to a carer's allowance for the day` |
| s 70(1)(a) | 1985 | encoded | `s 70(1) the person is entitled to a carer's allowance for the day` |
| s 70(1)(b) | 1986 | encoded | `s 70(1) the person is entitled to a carer's allowance for the day` |
| s 70(1)(c) | 1987 | encoded | `s 70(1) the person is entitled to a carer's allowance for the day` |
| s 70(1A) | 1988 | fork F3 | `s 70(1A) the person continues to be entitled to a carer's allowance for the day`; `s 70(1A) the days since the last Sunday` |
| s 70(1A)(a) | 1989 | encoded | `s 70(1A) the person continues to be entitled to a carer's allowance for the day` |
| s 70(1A)(b) | 1990-1991 | encoded | `s 70(1A) the person continues to be entitled to a carer's allowance for the day` |
| s 70(2) | 1992 | encoded | `s 70(2) Payment in respect of the person cared for`; `s 70(2) the person cared for is a severely disabled person` |
| defined term "severely disabled person" (s 70(2)) | 1992 | encoded | `s 70(2) the person cared for is a severely disabled person` |
| s 70(3) | 1993 | encoded | `s 70(3) the person is barred from a carer's allowance by age or education` |
| s 70(4) | 1994 | encoded | `s 70(4) the person is barred from a carer's allowance by the residence and presence conditions` |
| s 70(4A) | 1995 | encoded | `s 70(4A) the person is barred from a carer's allowance for the period by the Regulations` |
| s 70(5) | 1996 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 70(6) | 1997 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 70(7) | 1998 | encoded | `s 70(7) the person is barred from a further allowance for the day` |
| s 70(7)(a) | 1999 | encoded | `s 70(7) the person is barred from a further allowance for the day` |
| s 70(7)(b) | 2000 | encoded | `s 70(7) the person is barred from a further allowance for the day` |
| s 70(7ZA) | 2001 | encoded | `s 70(7ZA) the person is the one who has the relevant entitlement for the day` |
| s 70(7ZA)(a) | 2002 | encoded | `s 70(7ZA) the person is the one who has the relevant entitlement for the day` |
| s 70(7ZA)(b) | 2003 | encoded | `s 70(7ZA) the person is the one who has the relevant entitlement for the day` |
| s 70(7ZB) | 2004 | encoded | `s 70(7ZB) subsection (7ZC) applies` |
| s 70(7ZB)(a) | 2005 | encoded | `s 70(7ZB) subsection (7ZC) applies` |
| s 70(7ZB)(b) | 2006-2007 | encoded | `s 70(7ZB) subsection (7ZC) applies` |
| s 70(7ZC) | 2008 | encoded | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` |
| s 70(7ZC)(a) | 2009 | encoded | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` |
| s 70(7ZC)(b) | 2010 | encoded | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` |
| s 70(7ZC)(b)(i) | 2011 | encoded | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` |
| s 70(7ZC)(b)(ii) | 2012-2013 | encoded | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` |
| s 70(7A) | 2014 | encoded | `s 70(7A) the person has a relevant entitlement` |
| s 70(7A)(a) | 2015 | encoded | `s 70(7A) the person has a relevant entitlement` |
| s 70(7A)(b) | 2016 | encoded | `s 70(7A) the person has a relevant entitlement` |
| s 70(7B) | 2017 | encoded | `s 70(7B) the payment is carer support payment` |
| defined term "carer support payment" (s 70(7B)) | 2017 | encoded | `s 70(7B) the payment is carer support payment` |
| s 70(8) | 2018 | inert reason 2 | power to prescribe when a person is or is not treated as engaged in caring, gainfully employed, etc. |
| s 70(9) | 2019 | encoded | `s 70(9) the weekly rate of a carer's allowance in pounds` |
| s 70(10) | 2020 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| heading@70 | 2021 | inert reason 1 | heading |
| s 71 heading | 2022 | inert reason 1 | heading |
| s 71(1) | 2023 | encoded | `s 71(1) Component`; `s 71(1) the component is part of disability living allowance` |
| s 71(2) | 2024 | encoded | `s 71(2) the person's entitlement to disability living allowance is an entitlement to the components` |
| s 71(3) | 2025 | encoded | `s 71(3) Term of an award`; `s 71(3) the terms of the award are permitted` |
| s 71(4) | 2026 | encoded | `s 71(4) the weekly rate of the disability living allowance for a week with one component in pounds` |
| s 71(5) | 2027 | encoded | `s 71(5) the weekly rate of the disability living allowance for a week with both components in pounds` |
| s 71(6) | 2028 | encoded | `s 71(6) the person is barred from a disability living allowance by the residence and presence conditions` |
| s 71(7) | 2029 | encoded | `s 71(7) the person is barred from a disability living allowance while entitled to a Scottish or pension age payment` |
| s 72 heading | 2030 | inert reason 1 | heading |
| s 72(1) | 2031 | fork F1 | `s 72(1) Care component facts`; `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(a) | 2032 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(a)(i) | 2033 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(a)(ii) | 2034 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(b) | 2035 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(b)(i) | 2036 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(b)(ii) | 2037 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(c) | 2038 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(c)(i) | 2039 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1)(c)(ii) | 2040 | encoded | `s 72(1) the person is entitled to the care component for the period` |
| s 72(1A) | 2041 | encoded | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` |
| s 72(1A)(a) | 2042 | encoded | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` |
| s 72(1A)(b) | 2043 | encoded | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` |
| s 72(1A)(b)(i) | 2044 | encoded | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` |
| s 72(1A)(b)(ii) | 2045 | encoded | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` |
| s 72(2) | 2046 | fork F2 | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(a) | 2047 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(a)(i) | 2048 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(a)(ii) | 2049-2050 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(b) | 2051 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(b)(i) | 2052 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2)(b)(ii) | 2053 | encoded | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` |
| s 72(2A) | 2054 | encoded | `s 72(2A) the modifications in subsection (1A) have effect for subsection (2) on the day` |
| s 72(2A)(a) | 2055 | encoded | `s 72(2A) the modifications in subsection (1A) have effect for subsection (2) on the day` |
| s 72(2A)(b) | 2056 | encoded | `s 72(2A) the modifications in subsection (1A) have effect for subsection (2) on the day` |
| s 72(3) | 2057 | inert reason 2 | three weekly rates to be prescribed (the rates enter as inputs to `s 72(4)`) |
| s 72(4) | 2058 | encoded | `s 72(4) the weekly rate of the care component in pounds` |
| s 72(4)(a) | 2059 | encoded | `s 72(4) the weekly rate of the care component in pounds` |
| s 72(4)(b) | 2060 | encoded | `s 72(4) the weekly rate of the care component in pounds` |
| s 72(4)(c) | 2061 | encoded | `s 72(4) the weekly rate of the care component in pounds` |
| s 72(5) | 2062 | encoded | `s 72(5)(a) the first day of the period for which the person is taken to have satisfied the conditions`; `s 72(5)(b) the person is taken to satisfy or to be likely to satisfy the conditions on the day` |
| s 72(5)(a) | 2063 | encoded | `s 72(5)(a) the first day of the period for which the person is taken to have satisfied the conditions`; `s 72(5)(b) the person is taken to satisfy or to be likely to satisfy the conditions on the day` |
| s 72(5)(b) | 2064 | encoded | `s 72(5)(a) the first day of the period for which the person is taken to have satisfied the conditions`; `s 72(5)(b) the person is taken to satisfy or to be likely to satisfy the conditions on the day` |
| s 72(6) | 2065 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 72(7) | 2066 | inert reason 2 | power to prescribe circumstances in which a person is taken to satisfy or not to satisfy the conditions |
| s 72(7A) | 2067 | inert reason 2 | says subsection (1A) is subject to regulations made under subsection (7) |
| s 72(7B) | 2068 | encoded | `s 72(7B) the person is barred from the care component for the period by the Regulations` |
| s 72(8) | 2069 | inert reason 2 | power to make regulations that no care component is payable for a care home resident |
| s 72(9) | 2070 | encoded | `s 72(9) the establishment is a care home` |
| defined term "care home" (s 72(9)) | 2070 | encoded | `s 72(9) the establishment is a care home` |
| s 72(10) | 2071 | encoded | `s 72(10) Service`; `s 72(10) the service is a qualifying service for the purposes of subsection (8)` |
| defined term "qualifying services" (s 72(10)) | 2071-2074 | encoded | `s 72(10) Service` |
| s 72(10)(a) | 2072 | encoded | `s 72(10) Service`; `s 72(10) the service is a qualifying service for the purposes of subsection (8)` |
| s 72(10)(b) | 2073 | encoded | `s 72(10) Service`; `s 72(10) the service is a qualifying service for the purposes of subsection (8)` |
| s 72(10)(c) | 2074 | encoded | `s 72(10) Service`; `s 72(10) the service is a qualifying service for the purposes of subsection (8)` |
| s 72(11) | 2075 | encoded | `s 72(11) the enactment is a specified enactment` |
| defined term "specified" enactment (s 72(11)) | 2075 | encoded | `s 72(11) the enactment is a specified enactment` |
| s 72(12) | 2076 | inert reason 2 | the power to specify an enactment includes power to specify it for a purpose |
| s 72(13) | 2077 | encoded | `s 72(13) the provision is within the word enactment in this section` |
| defined term "enactment" (s 72(13)) | 2077 | encoded | `s 72(13) the provision is within the word enactment in this section` |
| s 73 heading | 2078 | inert reason 1 | heading |
| s 73(1) | 2079 | fork F1 | `s 73(1) Mobility component facts`; `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1)(a) | 2080 | encoded | `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1)(ab) | 2081 | encoded | `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1)(b) | 2082 | encoded | `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1)(c) | 2083 | encoded | `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1)(d) | 2084 | encoded | `s 73(1) the person is entitled to the mobility component for the period` |
| s 73(1A) | 2085 | encoded | `s 73(1) Condition`; `s 73(1A) the relevant age in years for the condition` |
| s 73(1A)(a) | 2086 | encoded | `s 73(1) Condition`; `s 73(1A) the relevant age in years for the condition` |
| s 73(1A)(b) | 2087 | encoded | `s 73(1) Condition`; `s 73(1A) the relevant age in years for the condition` |
| s 73(1AB) | 2088 | encoded | `s 73(1AB) the person falls within this subsection` |
| s 73(1AB)(a) | 2089 | encoded | `s 73(1AB) the person falls within this subsection` |
| s 73(1AB)(b) | 2090 | encoded | `s 73(1AB) the person falls within this subsection` |
| s 73(2) | 2091 | encoded | `s 73(2) the person falls within this subsection` |
| s 73(2)(a) | 2092 | encoded | `s 73(2) the person falls within this subsection` |
| s 73(2)(b) | 2093 | encoded | `s 73(2) the person falls within this subsection` |
| s 73(3) | 2094 | encoded | `s 73(3) the person falls within this subsection` |
| s 73(3)(a) | 2095 | encoded | `s 73(3) the person falls within this subsection` |
| s 73(3)(b) | 2096 | encoded | `s 73(3) the person falls within this subsection` |
| s 73(3)(c) | 2097 | encoded | `s 73(3) the person falls within this subsection` |
| s 73(4A) | 2098 | encoded | `s 73(4A) the condition in subsection (1)(d) is taken to be satisfied for the part of a period before he reaches 16` |
| s 73(4A)(a) | 2099 | encoded | `s 73(4A) the condition in subsection (1)(d) is taken to be satisfied for the part of a period before he reaches 16` |
| s 73(4A)(b) | 2100 | encoded | `s 73(4A) the condition in subsection (1)(d) is taken to be satisfied for the part of a period before he reaches 16` |
| s 73(5) | 2101 | inert reason 2 | power to prescribe circumstances in which a person is taken to satisfy or not to satisfy a condition |
| s 73(5A) | 2102 | inert reason 2 | says subsection (4A) is subject to regulations made under subsection (5) |
| s 73(6) | 2103 | inert reason 2 | regulations shall specify the cases within subsection (3)(a) and (b) (they enter as inputs to `s 73(3)`) |
| s 73(7) | 2104 | encoded | `s 73(7) the person is taken to satisfy the condition for the purposes of subsection (3)(c)` |
| s 73(8) | 2105 | encoded | `s 73(8) the person is barred from the mobility component for the period by his condition` |
| s 73(9) | 2106 | fork F2 | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(a) | 2107 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(a)(i) | 2108 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(a)(ii) | 2109-2110 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(b) | 2111 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(b)(i) | 2112 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9)(b)(ii) | 2113 | encoded | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` |
| s 73(9A) | 2114 | encoded | `s 73(9A) the modifications in subsection (4A) have effect for subsection (9) on the day` |
| s 73(9A)(a) | 2115 | encoded | `s 73(9A) the modifications in subsection (4A) have effect for subsection (9) on the day` |
| s 73(9A)(b) | 2116 | encoded | `s 73(9A) the modifications in subsection (4A) have effect for subsection (9) on the day` |
| s 73(10) | 2117 | inert reason 2 | two weekly rates to be prescribed (the rates enter as inputs to `s 73(11)`) |
| s 73(11) | 2118 | encoded | `s 73(11) the weekly rate of the mobility component in pounds` |
| s 73(11)(a) | 2119 | encoded | `s 73(11) the weekly rate of the mobility component in pounds` |
| s 73(11)(b) | 2120 | encoded | `s 73(11) the weekly rate of the mobility component in pounds` |
| s 73(12) | 2121 | encoded | `s 73(12)(a) the person is barred from the mobility component by the 6 month requirement alone`; `s 73(12)(b) the weekly rate of the mobility component of a terminally ill person in pounds` |
| s 73(12)(a) | 2122 | encoded | `s 73(12)(a) the person is barred from the mobility component by the 6 month requirement alone`; `s 73(12)(b) the weekly rate of the mobility component of a terminally ill person in pounds` |
| s 73(12)(b) | 2123 | encoded | `s 73(12)(a) the person is barred from the mobility component by the 6 month requirement alone`; `s 73(12)(b) the weekly rate of the mobility component of a terminally ill person in pounds` |
| s 73(13) | 2124 | inert reason 2 | power to prescribe cases in which a person who has the use of a vehicle is treated as not satisfying the mobility conditions |
| s 73(13)(a) | 2125 | inert reason 2 | power to prescribe cases in which a person who has the use of a vehicle is treated as not satisfying the mobility conditions |
| s 73(13)(b) | 2126-2127 | inert reason 2 | power to prescribe cases in which a person who has the use of a vehicle is treated as not satisfying the mobility conditions |
| s 73(14) | 2128 | encoded | `s 73(14) the payment is disregarded in applying an enactment under which regard is to be had to a person's means` |
| s 74 heading | 2129 | inert reason 1 | heading |
| s 74(1) | 2130 | encoded | `s 74(1) the person is deemed for the purposes of section 73 to satisfy the condition mentioned in subsection (1)(a) of that section` |
| s 74(2) | 2131 | encoded | `s 74(2) this section applies to the person` |
| s 74(2)(a) | 2132 | encoded | `s 74(2) this section applies to the person` |
| s 74(2)(b) | 2133 | encoded | `s 74(2) this section applies to the person` |
| s 74(2)(c) | 2134 | encoded | `s 74(2) this section applies to the person` |
| s 74(2)(d) | 2135 | encoded | `s 74(2) this section applies to the person` |
| s 75 heading | 2136 | inert reason 1 | heading |
| s 75(1) | 2137 | fork F4 | `s 75(1) the person is barred from a component of disability living allowance for the day after pensionable age` |
| s 75(2) | 2138 | inert reason 2 | power to modify the Act for persons entitled by virtue of subsection (1) |
| s 75(2)(a) | 2139 | inert reason 2 | power to modify the Act for persons entitled by virtue of subsection (1) |
| s 75(2)(b) | 2140 | inert reason 2 | power to modify the Act for persons entitled by virtue of subsection (1) |
| s 76 heading | 2141 | inert reason 1 | heading |
| s 76(1) | 2142 | encoded | `s 76(1) the person is barred from a disability living allowance for the day by the date of claim` |
| s 76(2) | 2143 | inert reason 2 | power to allow entitlement for a period before the claim |
| s 76(3) | 2144 | encoded | `s 76(3) the other person is regarded as making the claim` |
| s 76(3)(a) | 2145 | encoded | `s 76(3) the other person is regarded as making the claim` |
| s 76(3)(b) | 2146-2147 | encoded | `s 76(3) the other person is regarded as making the claim` |
| heading@76 | 2148 | inert reason 1 | heading |
| s 77 heading | 2149 | inert reason 1 | heading |
| s 77(1) | 2150 | encoded | `s 77(1) the person is entitled to a guardian's allowance in respect of the child or qualifying young person` |
| s 77(1)(a) | 2151 | encoded | `s 77(1) the person is entitled to a guardian's allowance in respect of the child or qualifying young person` |
| s 77(1)(b) | 2152-2153 | encoded | `s 77(1) the person is entitled to a guardian's allowance in respect of the child or qualifying young person` |
| s 77(2) | 2154 | encoded | `s 77(2) the circumstances are among those referred to in subsection (1)(b)` |
| s 77(2)(a) | 2155 | encoded | `s 77(2) the circumstances are among those referred to in subsection (1)(b)` |
| s 77(2)(b) | 2156 | encoded | `s 77(2) the circumstances are among those referred to in subsection (1)(b)` |
| s 77(2)(c) | 2157 | encoded | `s 77(2) the circumstances are among those referred to in subsection (1)(b)` |
| s 77(3) | 2158 | encoded | `s 77(3) the person is barred from a guardian's allowance by the parents' conditions` |
| s 77(4) | 2159 | encoded | `s 77(4) the amount is barred from payment by the conditions in subsection (5)` |
| s 77(5) | 2160 | encoded | `s 77(4) the amount is barred from payment by the conditions in subsection (5)` |
| s 77(5)(a) | 2161 | encoded | `s 77(4) the amount is barred from payment by the conditions in subsection (5)` |
| s 77(5)(b) | 2162 | encoded | `s 77(4) the amount is barred from payment by the conditions in subsection (5)` |
| s 77(6) | 2163 | encoded | `s 77(6) the condition in subsection (5)(b) is satisfied` |
| s 77(6)(a) | 2164 | encoded | `s 77(6) the condition in subsection (5)(b) is satisfied` |
| s 77(6)(a)(i) | 2165 | encoded | `s 77(6) the condition in subsection (5)(b) is satisfied` |
| s 77(6)(a)(ii) | 2166 | encoded | `s 77(6) the condition in subsection (5)(b) is satisfied` |
| s 77(6)(b) | 2167 | encoded | `s 77(6) the condition in subsection (5)(b) is satisfied` |
| s 77(7) | 2168 | encoded | `s 77(7) the weekly rate of a guardian's allowance in pounds` |
| s 77(8) | 2169 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(a) | 2170 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(b) | 2171 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(c) | 2172 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(c)(i) | 2173 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(c)(ii) | 2174 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(8)(c)(iii) | 2175 | inert reason 2 | regulations on prison, treated as such, and related matters (the prison fact enters as an input to `s 77(2)`) |
| s 77(9) | 2176 | fork F14 | `s 77(9) the person is the one who is entitled to the guardian's allowance`; `s 77(9) payment may be made to the man`; `s 77(9) the woman may elect that payment is not to be made to the man` |
| s 77(10) | 2177 | encoded | `s 77(10) the person is barred from a guardian's allowance because he or she is the parent` |
| s 77(11) | 2178 | encoded | `s 77(11) subsection (10) does not terminate the person's entitlement` |
| s 77(11)(a) | 2179 | encoded | `s 77(11) subsection (10) does not terminate the person's entitlement` |
| s 77(11)(b) | 2180-2181 | encoded | `s 77(11) subsection (10) does not terminate the person's entitlement` |
| heading@77 | 2182 | inert reason 1 | heading |
| s 78 heading | 2183 | inert reason 1 | heading |
| s 78(1) | 2184 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 78(2) | 2185 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 78(3) | 2186 | encoded | `s 78(3) the person is entitled to a Category D retirement pension` |
| s 78(3)(a) | 2187 | encoded | `s 78(3) the person is entitled to a Category D retirement pension` |
| s 78(3)(b) | 2188 | encoded | `s 78(3) the person is entitled to a Category D retirement pension` |
| s 78(4) | 2189 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(a) | 2190 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(b) | 2191 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(b)(i) | 2192 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(b)(ii) | 2193 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(c) | 2194 | encoded | `s 78(4) the weekly rate of the pension disregarding the elements in pounds` |
| s 78(4)(d) | 2195 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 78(5) | 2196 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 78(6) | 2197 | encoded | `s 78(6) the appropriate weekly rate of a Category D retirement pension in pounds` |
| s 78(7) | 2198 | encoded | `s 78(7) the entitlement continues on the day` |
| s 78(8) | 2199 | encoded | `s 78(8) the Category D retirement pension is barred from payment for the day` |
| s 78(9) | 2200 | inert reason 2 | power to provide for payment of a Category C retirement pension or corresponding benefit at the prescribed rate |
| s 78(9)(a) | 2201 | inert reason 2 | power to provide for payment of a Category C retirement pension or corresponding benefit at the prescribed rate |
| s 78(9)(b) | 2202-2203 | inert reason 2 | power to provide for payment of a Category C retirement pension or corresponding benefit at the prescribed rate |
| s 79 heading | 2204 | inert reason 1 | heading |
| s 79(1) | 2205 | encoded | `s 79(1) the person is entitled to an age addition to a retirement pension` |
| s 79(2) | 2206 | encoded | `s 79(2) the person is entitled to an age addition to another pension or allowance` |
| s 79(2)(a) | 2207 | encoded | `s 79(2) the person is entitled to an age addition to another pension or allowance` |
| s 79(2)(b) | 2208-2209 | encoded | `s 79(2) the person is entitled to an age addition to another pension or allowance` |
| s 79(3) | 2210 | encoded | `s 79(3) the age addition is payable on the day`; `s 79(3) the weekly rate of age addition in pounds` |
| heading@79 | 2211 | inert reason 1 | heading |
| heading@79 | 2212 | inert reason 1 | heading |
| s 80 heading | 2213 | inert reason 1 | heading |
| s 80 DOTS | 2214 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 81 heading | 2215 | inert reason 1 | heading |
| s 81 DOTS | 2216 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| heading@81 | 2217 | inert reason 1 | heading |
| s 82 heading | 2218 | inert reason 1 | heading |
| s 82 DOTS | 2219 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 83 heading | 2220 | inert reason 1 | heading |
| s 83 DOTS | 2221 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 84 heading | 2222 | inert reason 1 | heading |
| s 84 DOTS | 2223 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 85 heading | 2224 | inert reason 1 | heading |
| s 85 DOTS | 2225 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 86 heading | 2226 | inert reason 1 | heading |
| s 86 DOTS | 2227 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 86A heading | 2228 | inert reason 1 | heading |
| s 86A(1) | 2229 | encoded | `s 86A(1) the increase of incapacity benefit for an adult dependant in pounds` |
| s 86A(2) | 2230 | inert reason 2 | power to provide that no increase is given where the dependant's earnings exceed a prescribed amount |
| s 87 heading | 2231 | inert reason 1 | heading |
| s 87(1) | 2232 | encoded | `s 87(1) the amount of any increase is determined in accordance with regulations under this section` |
| s 87(1)(a) | 2233 | encoded | `s 87(1) the amount of any increase is determined in accordance with regulations under this section` |
| s 87(1)(b) | 2234-2235 | encoded | `s 87(1) the amount of any increase is determined in accordance with regulations under this section` |
| s 87(2) | 2236 | encoded | `s 87(2) the person is barred from an increase under the regulations` |
| s 87(2)(a) | 2237 | encoded | `s 87(2) the person is barred from an increase under the regulations` |
| s 87(2)(b) | 2238 | encoded | `s 87(2) the person is barred from an increase under the regulations` |
| s 88 heading | 2239 | inert reason 1 | heading |
| s 88 | 2240 | encoded | `s 88 the person is barred from an increase in respect of a further person for the same period` |
| heading@88 | 2241 | inert reason 1 | heading |
| s 89 heading | 2242 | inert reason 1 | heading |
| s 89(1) | 2243 | encoded | `s 89(1) the payment counts as earnings in sections 82 and 86A` |
| s 89(1A) | 2244 | encoded | `s 89(1A) the PPF periodic payment counts as earnings in sections 82 and 86A` |
| s 89(2) | 2245 | inert reason 2 | power to provide for apportionment of pension payments made otherwise than weekly |
| s 89(3) | 2246 | encoded | `s 89(3) the payment is a PPF periodic payment` |
| defined term "PPF periodic payments" (s 89(3)) | 2246-2248 | encoded | `s 89(3) the payment is a PPF periodic payment` |
| s 89(3)(a) | 2247 | encoded | `s 89(3) the payment is a PPF periodic payment` |
| s 89(3)(b) | 2248-2249 | encoded | `s 89(3) the payment is a PPF periodic payment` |
| s 90 heading | 2250 | inert reason 1 | heading |
| s 90 DOTS | 2251 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 91 heading | 2252 | inert reason 1 | heading |
| s 91(1) | 2253 | encoded | `s 91(1) the beneficiary is barred from the increase by a trade dispute` |
| s 91(1)(a) | 2254 | encoded | `s 91(1) the beneficiary is barred from the increase by a trade dispute` |
| s 91(1)(b) | 2255-2256 | encoded | `s 91(1) the beneficiary is barred from the increase by a trade dispute` |
| s 91(2) | 2257 | encoded | `s 91(2) the person falls within this subsection` |
| s 91(2)(a) | 2258 | encoded | `s 91(2) the person falls within this subsection` |
| s 91(2)(b) | 2259 | encoded | `s 91(2) the person falls within this subsection` |
| s 92 heading | 2260 | inert reason 1 | heading |
| s 92(1) | 2261 | encoded | `s 92(1) the award continues in force`; `s 92(1) the increase is barred from payment for the week by the relevant earner's earnings` |
| s 92(1)(a) | 2262 | encoded | `s 92(1) the award continues in force`; `s 92(1) the increase is barred from payment for the week by the relevant earner's earnings` |
| s 92(1)(b) | 2263-2264 | encoded | `s 92(1) the award continues in force`; `s 92(1) the increase is barred from payment for the week by the relevant earner's earnings` |
| s 92(2) | 2265 | encoded | `s 92(2) the earnings relevant to the week in pounds` |
| s 93 heading | 2266 | inert reason 1 | heading |
| s 93 chapeau | 2267 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(a) | 2268 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(a)(i) | 2269 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(a)(ii) | 2270 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| s 93(b) | 2271 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(b)(i) | 2272 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(b)(ii) | 2273 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(b)(iii) | 2274 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| s 93(b)(iv) | 2275-2276 | fork F5 | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day`; `s 93(b) Regulation` |
| heading@93 | 2277 | inert reason 1 | heading |
| heading@93 | 2278 | inert reason 1 | heading |
| s 94 heading | 2279 | inert reason 1 | heading |
| s 94(1) | 2280 | fork F7 | `s 94(1) the personal injury is of a kind mentioned in section 94(1)`; `s 94(1) industrial injuries benefit is payable` |
| s 94(2) | 2281 | encoded | `s 94(2) the benefit is part of industrial injuries benefit` |
| s 94(2)(a) | 2282 | encoded | `s 94(2) the benefit is part of industrial injuries benefit` |
| s 94(2)(b) | 2283 | encoded | `s 94(2) the benefit is part of industrial injuries benefit` |
| s 94(2)(c) | 2284 | encoded | `s 94(2) the benefit is part of industrial injuries benefit` |
| s 94(2)(d) | 2285 | encoded | `s 94(2) the benefit is part of industrial injuries benefit` |
| s 94(3) | 2286 | fork F6 | `s 94(3) the accident is taken to have arisen out of the employment` |
| s 94(4) | 2287 | inert reason 2 | power to provide for the day treated as the day of the accident for night workers and special cases |
| s 94(5) | 2288 | fork F8 | `s 94(5) the person is barred from industrial injuries benefit for an accident outside Great Britain` |
| s 94(6) | 2289 | encoded | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` |
| defined term "work" (s 94(6)) | 2289 | encoded | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` |
| s 95 heading | 2290 | inert reason 1 | heading |
| s 95(1) | 2291 | encoded | `s 95(1) the employment is employed earner's employment` |
| defined term "employed earner's employment" (s 95(1)) | 2291 | encoded | `s 95(1) the employment is employed earner's employment` |
| s 95(2) | 2292 | inert reason 2 | power to provide that a prescribed employment is not employed earner's employment (its effect enters `s 95(3)` as an input) |
| s 95(3) | 2293 | encoded | `s 95(3) the employment is employed earner's employment in relation to the accident` |
| s 95(4) | 2294 | encoded | `s 95(4) the reference is construed as a reference to an insured person or insurable employment` |
| s 95(5) | 2295 | encoded | `s 95(5) the provision is among the industrial injuries and diseases provisions` |
| defined term "the industrial injuries and diseases provisions" (s 95(5)) | 2295-2298 | encoded | `s 95(5) the provision is among the industrial injuries and diseases provisions` |
| s 95(5)(a) | 2296 | encoded | `s 95(5) the provision is among the industrial injuries and diseases provisions` |
| s 95(5)(b) | 2297 | encoded | `s 95(5) the provision is among the industrial injuries and diseases provisions` |
| s 95(5)(c) | 2298 | encoded | `s 95(5) the provision is among the industrial injuries and diseases provisions` |
| s 95A heading | 2299 | inert reason 1 | heading |
| s 95A(1) | 2300 | encoded | `s 95A(1) the participation is employed earner's employment` |
| s 95A(2) | 2301 | encoded | `s 95A(2) the person is the employer in relation to the participation` |
| s 95A(3) | 2302 | fork F10 | `s 95A(3) the provision is among the industrial injuries and diseases provisions` |
| s 96 heading | 2303 | inert reason 1 | heading |
| s 96 chapeau | 2304 | inert reason 2 | power to provide for a prescribed person to be treated as the earner's employer |
| s 96(a) | 2305 | inert reason 2 | power to provide for a prescribed person to be treated as the earner's employer |
| s 96(b) | 2306 | inert reason 2 | power to provide for a prescribed person to be treated as the earner's employer |
| s 96(b)(i) | 2307 | inert reason 2 | power to provide for a prescribed person to be treated as the earner's employer |
| s 96(b)(ii) | 2308-2309 | inert reason 2 | power to provide for a prescribed person to be treated as the earner's employer |
| s 97 heading | 2310 | inert reason 1 | heading |
| s 97(1) | 2311 | encoded | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(1)(a) | 2312 | encoded | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(1)(b) | 2313 | encoded | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(2) | 2314 | fork F9 | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(2)(a) | 2315 | encoded | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(2)(b) | 2316 | encoded | `s 97(2) the relevant employment is treated as employed earner's employment` |
| s 97(3) | 2317 | encoded | `s 97(3) Subject of the claim`; `s 97(3) the employment is the relevant employment` |
| defined term "relevant employment" (s 97(3)) | 2317-2319 | encoded | `s 97(3) the employment is the relevant employment` |
| s 97(3)(a) | 2318 | encoded | `s 97(3) Subject of the claim`; `s 97(3) the employment is the relevant employment` |
| s 97(3)(b) | 2319 | encoded | `s 97(3) Subject of the claim`; `s 97(3) the employment is the relevant employment` |
| s 98 heading | 2320 | inert reason 1 | heading |
| s 98 | 2321 | fork F6 | `s 98 the accident is taken by this section to arise out of and in the course of the employment` |
| s 98(a) | 2322 | fork F6 | `s 98 the accident is taken by this section to arise out of and in the course of the employment` |
| s 98(b) | 2323 | fork F6 | `s 98 the accident is taken by this section to arise out of and in the course of the employment` |
| s 99 heading | 2324 | inert reason 1 | heading |
| s 99(1) | 2325 | fork F6 | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` |
| s 99(1)(a) | 2326 | fork F6 | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` |
| s 99(1)(b) | 2327 | fork F6 | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` |
| s 99(1)(b)(i) | 2328 | fork F6 | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` |
| s 99(1)(b)(ii) | 2329 | fork F6 | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` |
| s 99(2) | 2330 | encoded | `s 99(2) the conveyance is a vehicle for the purposes of this section` |
| defined term "vehicle" (s 99(2)) | 2330 | encoded | `s 99(2) the conveyance is a vehicle for the purposes of this section` |
| s 100 heading | 2331 | inert reason 1 | heading |
| s 100 | 2332 | fork F6 | `s 100 the accident is taken by this section to arise out of and in the course of the employment` |
| s 101 heading | 2333 | inert reason 1 | heading |
| s 101 chapeau | 2334 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(a) | 2335 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(b) | 2336 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(b)(i) | 2337 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(b)(ii) | 2338 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(b)(iii) | 2339-2340 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| s 101(c) | 2341 | fork F6 | `s 101 the accident is treated by this section as arising out of the employment` |
| heading@101 | 2342 | inert reason 1 | heading |
| s 102 heading | 2343 | inert reason 1 | heading |
| s 102 DOTS | 2344 | repealed or blank in this text | the text shows a dotted line in place of the provision |
| heading@102 | 2345 | inert reason 1 | heading |
| s 103 heading | 2346 | inert reason 1 | heading |
| s 103(1) | 2347 | encoded | `s 103(1) the person is entitled to disablement pension`; `s 103(1) the least extent of disablement for a claim made on the date, as a percentage` |
| s 103(2) | 2348 | encoded | `s 103(2) Earlier disablement`; `s 103(2) the earlier disablement may be added`; `s 103(2) the aggregate percentage with every addition the subsection permits` |
| s 103(2)(a) | 2349 | encoded | `s 103(2) Earlier disablement`; `s 103(2) the earlier disablement may be added`; `s 103(2) the aggregate percentage with every addition the subsection permits` |
| s 103(2)(b) | 2350-2351 | encoded | `s 103(2) Earlier disablement`; `s 103(2) the earlier disablement may be added`; `s 103(2) the aggregate percentage with every addition the subsection permits` |
| s 103(3) | 2352 | fork F11 | `s 103(3) the percentage treated as the assessment` |
| s 103(3)(a) | 2353 | encoded | `s 103(3) the percentage treated as the assessment` |
| s 103(3)(b) | 2354-2355 | encoded | `s 103(3) the percentage treated as the assessment` |
| s 103(4) | 2356 | encoded | `s 103(4) the percentage to which subsection (3) applies` |
| s 103(5) | 2357 | encoded | `s 103(5) the extent of the disablement is assessed`; `s 103(5) there is taken to be no relevant loss of faculty` |
| defined term "assessed" (s 103(5)) | 2357 | encoded | `s 103(5) the extent of the disablement is assessed` |
| s 103(6) | 2358 | fork F13 | `s 103(6) the person is barred from a disablement pension for the day by the 90 days`; `s 103(6) the last day of a run of days, not counting Sundays, that begins with the day` |
| s 103(7) | 2359 | encoded | `s 103(7) the weekly rate at which the disablement pension is paid in pounds` |
| s 103(8) | 2360 | encoded | `s 103(8) the pension ceases on the death of the beneficiary` |
| s 104 heading | 2361 | inert reason 1 | heading |
| s 104(1) | 2362 | fork F12 | `s 104(1) the weekly rate of the pension is increased for constant attendance`; `s 104(1) the amount of the increase in pounds` |
| s 104(2) | 2363 | encoded | `s 104(2) the increase is payable on the day` |
| s 104(3) | 2364 | inert reason 2 | power to direct that ss 64 to 67 have effect for increases under this section |
| s 104(4) | 2365 | encoded | `s 104(4) the change is a modification` |
| defined term "modifications" (s 104(4)) | 2365 | encoded | `s 104(4) the change is a modification` |
| s 105 heading | 2366 | inert reason 1 | heading |
| s 105(1) | 2367 | fork F7 | `s 105(1) the weekly rate of the pension is further increased`; `s 105(1) the weekly rate of the increase exceeds the amount`; `s 105(1) the amount of the further increase in pounds` |
| s 105(1)(a) | 2368 | fork F7 | `s 105(1) the weekly rate of the pension is further increased`; `s 105(1) the weekly rate of the increase exceeds the amount`; `s 105(1) the amount of the further increase in pounds` |
| s 105(1)(b) | 2369-2370 | fork F7 | `s 105(1) the weekly rate of the pension is further increased`; `s 105(1) the weekly rate of the increase exceeds the amount`; `s 105(1) the amount of the further increase in pounds` |
| s 105(2) | 2371 | encoded | `s 105(2) the increase is payable on the day` |
| heading@105 | 2372 | inert reason 1 | heading |
| s 106 heading | 2373 | inert reason 1 | heading |
| s 106 chapeau | 2374 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(a) | 2375 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(b) | 2376 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(c) | 2377 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(d) | 2378 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(e) | 2379 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| s 106(f) | 2380-2381 | encoded | `s 106 Benefit or increase`; `s 106 Schedule 7 has effect in relation to the benefit or increase` |
| heading@106 | 2382 | inert reason 1 | heading |
| s 107 heading | 2383 | inert reason 1 | heading |
| s 107(1) | 2384 | encoded | `s 107(1)(a) the person is barred from an aggregate weekly rate above the appropriate amount`; `s 107(1)(a) the aggregate rate exceeds the appropriate amount`; `s 107(1)(a) the aggregate weekly rate the person may receive for the same period, apart from increases, in pounds` |
| s 107(1)(a) | 2385 | encoded | `s 107(1)(a) the person is barred from an aggregate weekly rate above the appropriate amount`; `s 107(1)(a) the aggregate rate exceeds the appropriate amount`; `s 107(1)(a) the aggregate weekly rate the person may receive for the same period, apart from increases, in pounds` |
| s 107(1)(b) | 2386 | inert reason 2 | power to provide by regulations for adjusting disablement benefit and the increases in subsection (2) |
| s 107(1)(b)(i) | 2387 | inert reason 2 | power to provide by regulations for adjusting disablement benefit and the increases in subsection (2) |
| s 107(1)(b)(ii) | 2388 | inert reason 2 | power to provide by regulations for adjusting disablement benefit and the increases in subsection (2) |
| s 107(2) | 2389-2392 | encoded | `s 107(2) Provision`; `s 107(2) the increase is one referred to in subsection (1)` |
| heading@107 | 2393 | inert reason 1 | heading |
| s 108 heading | 2394 | inert reason 1 | heading |
| s 108(1) | 2395 | fork F7 | `s 108(1) industrial injuries benefits are payable in respect of the prescribed disease or injury` |
| s 108(1)(a) | 2396 | fork F7 | `s 108(1) industrial injuries benefits are payable in respect of the prescribed disease or injury` |
| s 108(1)(b) | 2397-2398 | fork F7 | `s 108(1) industrial injuries benefits are payable in respect of the prescribed disease or injury` |
| s 108(2) | 2399 | inert reason 2 | condition on the making of regulations: the Secretary of State must be satisfied that the disease or injury meets (a) and (b) |
| s 108(2)(a) | 2400 | inert reason 2 | condition on the making of regulations: the Secretary of State must be satisfied that the disease or injury meets (a) and (b) |
| s 108(2)(b) | 2401 | inert reason 2 | condition on the making of regulations: the Secretary of State must be satisfied that the disease or injury meets (a) and (b) |
| s 108(3) | 2402 | inert reason 2 | power to treat a person as if the regulations had been in force earlier |
| s 108(4) | 2403 | inert reason 2 | power to make regulations on the time a disease or injury is developed and recrudescence |
| s 108(4)(a) | 2404 | inert reason 2 | power to make regulations on the time a disease or injury is developed and recrudescence |
| s 108(4)(b) | 2405 | inert reason 2 | power to make regulations on the time a disease or injury is developed and recrudescence |
| s 108(5) | 2406 | inert reason 2 | the power in subsection (4)(a) includes the date of the first claim |
| s 108(6) | 2407 | encoded | `s 108(6) the person is barred from benefit in respect of a disease as an injury by accident` |
| s 109 heading | 2408 | inert reason 1 | heading |
| s 109(1) | 2409 | encoded | `s 109(1) the benefit and the conditions for receipt are the same as for personal injury by accident` |
| s 109(1)(a) | 2410 | encoded | `s 109(1) the benefit and the conditions for receipt are the same as for personal injury by accident` |
| s 109(1)(b) | 2411-2412 | encoded | `s 109(1) the benefit and the conditions for receipt are the same as for personal injury by accident` |
| s 109(2) | 2413 | inert reason 2 | power to modify provisions and adapt references to accidents for prescribed diseases and injuries |
| s 109(2)(a) | 2414 | inert reason 2 | power to modify provisions and adapt references to accidents for prescribed diseases and injuries |
| s 109(2)(b) | 2415 | inert reason 2 | power to modify provisions and adapt references to accidents for prescribed diseases and injuries |
| s 109(2) final words | 2416 | encoded | `s 109(2) the provision is taken to relate to the administration of disablement benefit or reduced earnings allowance` |
| s 109(3) | 2417 | inert reason 2 | power to include presumptions and incidental provision in the regulations |
| s 109(3)(a) | 2418 | inert reason 2 | power to include presumptions and incidental provision in the regulations |
| s 109(3)(a)(i) | 2419 | inert reason 2 | power to include presumptions and incidental provision in the regulations |
| s 109(3)(a)(ii) | 2420 | inert reason 2 | power to include presumptions and incidental provision in the regulations |
| s 109(3)(b) | 2421 | inert reason 2 | power to include presumptions and incidental provision in the regulations |
| s 109(4) | 2422 | inert reason 2 | power to add the appropriate percentage in determining disablement |
| s 109(4)(a) | 2423 | inert reason 2 | power to add the appropriate percentage in determining disablement |
| s 109(4)(b) | 2424 | inert reason 2 | power to add the appropriate percentage in determining disablement |
| s 109(5) | 2425 | encoded | `s 109(5) Present disablement`; `s 109(5) the present disablement counts in the appropriate percentage`; `s 109(5) the appropriate percentage for subsection (4)(a)` |
| defined term "the appropriate percentage" (s 109(5)) | 2425-2428 | encoded | `s 109(5) the present disablement counts in the appropriate percentage` |
| s 109(5)(a) | 2426 | encoded | `s 109(5) Present disablement`; `s 109(5) the present disablement counts in the appropriate percentage`; `s 109(5) the appropriate percentage for subsection (4)(a)` |
| s 109(5)(b) | 2427-2428 | encoded | `s 109(5) Present disablement`; `s 109(5) the present disablement counts in the appropriate percentage`; `s 109(5) the appropriate percentage for subsection (4)(a)` |
| s 109(6) | 2429 | encoded | `s 109(6) Present disablement`; `s 109(6) the present disablement counts in the appropriate percentage`; `s 109(6) the appropriate percentage for subsection (4)(b)` |
| defined term "the appropriate percentage" (s 109(6)) | 2429-2431 | encoded | `s 109(6) the present disablement counts in the appropriate percentage` |
| s 109(6)(a) | 2430 | encoded | `s 109(6) Present disablement`; `s 109(6) the present disablement counts in the appropriate percentage`; `s 109(6) the appropriate percentage for subsection (4)(b)` |
| s 109(6)(b) | 2431 | encoded | `s 109(6) Present disablement`; `s 109(6) the present disablement counts in the appropriate percentage`; `s 109(6) the appropriate percentage for subsection (4)(b)` |
| s 109(7) | 2432 | inert reason 2 | power to apply the corresponding provisions to the aggregate percentage |
| s 109(7)(a) | 2433 | inert reason 2 | power to apply the corresponding provisions to the aggregate percentage |
| s 109(7)(b) | 2434-2435 | inert reason 2 | power to apply the corresponding provisions to the aggregate percentage |
| s 110 heading | 2436 | inert reason 1 | heading |
| s 110(1) | 2437 | inert reason 2 | power to treat the effects of tuberculosis as effects of pneumoconiosis |
| s 110(2) | 2438 | inert reason 2 | limit on the power in subsection (1) for emphysema and chronic bronchitis |
| s 110(3) | 2439 | encoded | `s 110(3) the least assessed extent of the disablement treated as resulting, as a percentage` |
| s 110(4) | 2440 | encoded | `s 110(4) the person is barred from disablement benefit in respect of byssinosis` |
| heading@110 | 2441 | inert reason 1 | heading |
| s 111 heading | 2442 | inert reason 1 | heading |
| s 111 DOTS | 2443 | repealed or blank in this text | the text shows a dotted line in place of the provision |


## Fork register (ssc4)

Each fork: the text, the readings seen, the one taken (the status quo; every branch resting on a reading of kind (a) or (b) is also listed under Marginal readings), and the text that licenses each.
All forks are "assumed, not ruled": no one with authority has ruled on them.

| fork | where | readings seen | taken | text licensing each |
| --- | --- | --- | --- | --- |
| F1 | ss 65(1), 72(1), 73(1) | (i) a grant limited by its own wording: when the conditions fail the text is silent, so NOTHING; (ii) the conditions are necessary, so a failed condition is JUST FALSE | (i) | "the period for which a person is entitled to an attendance allowance shall be--(a) a period throughout which ...; and (b) ..." (1944-1946); "a person shall be entitled to the care component ... for any period throughout which--" (2031); none of "if", "only if", "unless" appears. (ii) rests on reading "shall be" as a definition of the period |
| F2 | ss 65(1)(b), 66(1)(a)(ii), 72(2), 72(5)(a), 73(9) | months counted: (i) the same day of the month, and NOTHING where the target month lacks that day; (ii) roll to the last day of the month; (iii) 30-day months | (i) | "six months", "3 months" (1946, 1961, 2049, 2063, 2108): the text gives no rule for month ends |
| F3 | s 70(1A) | "until--(a) the end of the week ...; or (b) the expiry of the period of eight weeks ...": (i) entitlement lasts through the last day of the earlier event; (ii) up to but not including it | (i) | "continue to be entitled to it ... until--" (1988-1990): each limb names a last day |
| F4 | s 75(1) | "for any period after he attains pensionable age": (i) the day of attaining is itself after, because the age is attained at the start of the anniversary day; (ii) after means strictly later than the day of attaining | (i) | 2137 and the keel's K2 (`s 173(a)`) |
| F5 | s 93 | "each day between the last day on which his benefit was previously payable and the day on which he again becomes entitled to it": (i) both named days excluded; (ii) either or both included | (i) | "between" (2276); the benefit was payable on the first and he is entitled again on the second |
| F6 | ss 94(3), 98, 99(1), 100, 101 | the deeming "if": (i) the function answers whether THIS SECTION treats the accident as arising out of and in the course of the employment, and a failed limb is JUST FALSE for the section only; (ii) the function answers whether the accident so arises in fact | (i) | s 94(3) says an accident in the course of the employment "shall be taken, in the absence of evidence to the contrary, also to have arisen out of that employment" (an unless-type condition: with evidence to the contrary the presumption does not run, JUST FALSE for the subsection only; not in the course is NOTHING, the subject of the sentence); each of ss 98 to 101 says an accident "shall be taken" or "shall be treated" "if" limbs (a), (b), (c); whether the accident so arises apart from the section is the ordinary law of s 94(1), not in this text |
| F7 | ss 94(1), 105(1), 108(1) | "shall be payable where", "Where ... shall ... be further increased": (i) "where" names a case and failure is NOTHING; (ii) "where" is "if" and failure is JUST FALSE | (i) | 2280, 2367-2370, 2395-2398: the brief's list of words that make the text say no is "means", "if", "only if", "unless", "until", "while"; "where" is not on it |
| F8 | s 94(5) | "shall not be payable in respect of an accident happening while the earner is outside Great Britain": (i) inside Great Britain the text says no bar (JUST FALSE) because the bar is written "while"; (ii) NOTHING, the bar being limited by its own wording | (i) | 2288 ("while" is on the brief's list) |
| F9 | s 97(2) | "The Secretary of State may direct that the relevant employment shall ... be treated as having been employed earner's employment notwithstanding that ... (a) the contract ... was void; or (b) the employed person was not lawfully employed": (i) TRUE needs a claim or application, a direction, and (a) or (b); (ii) "notwithstanding that" is concessive, so a claim or application and a direction suffice | (i), which never gives TRUE where (ii) would not | 2311-2316 |
| F10 | s 95A(3) | "has the same meaning as in section 95(4)": (i) the definition in s 95(5) is meant, because s 95(4) only uses the term; (ii) s 95(4) is meant, which defines nothing | (i) | 2294-2295, 2302 |
| F11 | s 103(3) | an assessment outside the two cases (3) names: (i) it stands as assessed; (ii) the subsection is silent (NOTHING) | (i) | 2352-2355: "treated as" changes only the cases named; "assessed" means assessed under Schedule 6 (2357) |
| F12 | s 104(1) | "an amount, not exceeding the appropriate amount specified in Schedule 4, Part V, paragraph 2 determined in accordance with regulations": (i) the lesser of the determined amount and the Schedule figure; (ii) a determined amount above the figure is not a result the Act permits (NOTHING) | (i) | 2362 |
| F13 | s 103(6) | "the period of 90 days (disregarding Sundays) beginning with the day of the relevant accident": (i) 90 days that are not Sundays, counted from the accident day; (ii) 90 calendar days, Sundays then ignored for the pension | (i) | 2358 |
| F14 | s 77(9) | "payment may be made either to her or to him unless she elects in the prescribed manner that payment is not to be made to him": (i) a regulative rule, the woman MAY elect, with no deadline because the text states none; (ii) a deadline set by regulations; (iii) a plain yes-or-no function only | (i), and the plain function `s 77(9) payment may be made to the man` for the seat | 2176 |

## Jural relations (ssc4)

Hohfeld: claim-right / duty; privilege / no-right; power / liability; immunity / disability. "none" means a definition, a deeming rule, a presumption or a heading that creates no relation of its own.
The Secretary of State is the duty-bearer and power-holder throughout; the seat is the person on the other side.

| provision | relation |
| --- | --- |
| s 63 | none (a list of descriptions) |
| s 64(1), (1A) | claim-right of the person to attendance allowance, duty of the Secretary of State to pay; (1A) disability (no claim-right while another allowance is held) |
| s 64(2), (3) | none (definitions of the conditions) |
| s 64(4) | power of the Secretary of State (regulations) to deem the conditions met or not met; liability of the person |
| s 65(1), (3) | claim-right to the period and the rate; duty |
| s 65(2) | none (a deeming rule that widens the claim-right) |
| s 65(4), (7) | no-right of the person (no allowance for a period before the claim; none under the EC Regulations unless the United Kingdom is competent) |
| s 65(5) | power of the Secretary of State (regulations); liability |
| s 65(6) | power of the person to claim in advance (a regulative MAY); the award is conditional |
| s 66 | claim-right on a terminal-illness claim; power of the claimant to make the claim expressly; none for (2)(a) |
| s 67 | power of the Secretary of State to remove the allowance of a care-home resident; liability of the person; (3)-(7) none |
| s 68, 69 | none (blank) |
| s 70(1), (1A), (7B), (9) | claim-right to carer's allowance and its rate; duty |
| s 70(2), (7B) | none (definitions) |
| s 70(3), (4), (4A), (7) | no-right of the person |
| s 70(7ZA)-(7ZC), (7A) | power of the persons to elect jointly, power of the Secretary of State to determine; liability; no-right of B |
| s 70(8) | power of the Secretary of State (regulations) |
| s 71(1), (2), (3) | claim-right to the components of disability living allowance; (3) disability on the terms of an award |
| s 71(4), (5) | claim-right to the weekly rate |
| s 71(6), (7) | no-right of the person |
| s 72(1), (1A), (4), (5) | claim-right to the care component and its rate; (5) deeming |
| s 72(2), (7B) | no-right until the 3 month and 6 month requirements are met; no-right under the EC Regulations |
| s 72(3), (7), (8) | power of the Secretary of State (regulations) |
| s 72(9)-(13) | none (definitions) |
| s 73(1)-(3), (4A), (7), (11), (12) | claim-right to the mobility component and its rate; (2), (3), (7) none (they define who qualifies) |
| s 73(8), (9) | no-right of the person |
| s 73(5), (5A), (6), (10), (13) | power of the Secretary of State (regulations) |
| s 73(14) | immunity of the payment from means-testing |
| s 74 | power of the Secretary of State (certificates); (1) deemed condition widens the claim-right |
| s 75(1) | no-right of the person after pensionable age; (2) power |
| s 76 | no-right before the claim; (2) power; (3) none (who is regarded as claiming) |
| s 77(1), (6), (7), (11) | claim-right to guardian's allowance and its rate; duty |
| s 77(2), (5) | none (conditions) |
| s 77(3), (4), (10) | no-right of the person |
| s 77(8) | power of the Secretary of State (regulations) |
| s 77(9) | the man has a no-right to be the person entitled; the woman has a power to elect that payment is not made to him; the man a liability |
| s 78(3), (6), (7) | claim-right to a Category D retirement pension and its rate; (8) no-right for a day before the commencement |
| s 78(9) | power of the Secretary of State (regulations) |
| s 79 | claim-right to age addition; duty |
| s 80-86 | none (blank) |
| s 86A(1) | claim-right to the increase of incapacity benefit in the prescribed circumstances; duty; (2) power |
| s 87(1), (2) | liability of the person to have the increase fixed by regulations; (2) disability of the Secretary of State to provide an increase in the case described |
| s 88 | no-right of the person to an increase for more than one person |
| s 89 | none ((1), (3) fix what counts as earnings); (2) power |
| s 90 | none (blank) |
| s 91 | no-right of the beneficiary when the dependant is within the trade dispute subsection; (2) none |
| s 92 | claim-right to the continued award; no-right for a week of high earnings |
| s 93 | claim-right to treat the increase as payable (deeming) |
| s 94(1), (5) | claim-right to industrial injuries benefit; duty; (5) no-right for an accident outside Great Britain |
| s 94(2), (3), (6) | none (a list, a presumption, a definition) |
| s 94(4) | power of the Secretary of State (regulations) |
| s 95, 95A | none (definitions and inclusions); s 95(2) power of the Secretary of State (regulations) |
| s 96 | power of the Secretary of State (regulations) to treat a prescribed person as the employer; liability of that person |
| s 97 | power of the Secretary of State (direction); liability of the employer; the earner's claim-right is widened |
| s 98-101 | none (deeming rules that widen the claim-right in s 94(1)) |
| s 102 | none (blank) |
| s 103(1), (7) | claim-right to disablement pension and its rate; duty |
| s 103(2)-(5) | none (rules that fix the extent of the disablement) |
| s 103(6) | no-right until the 90 days have expired |
| s 103(8) | extinction of the claim-right on death |
| s 104(1), (2) | claim-right to the constant attendance increase; (2) power of the deciding officer to fix the period |
| s 104(3) | power of the Secretary of State (regulations); (4) none |
| s 105 | claim-right to the further increase; (2) power of the deciding officer |
| s 106 | none (extends Schedule 7) |
| s 107(1)(a) | no-right above the aggregate rate; (b) power of the Secretary of State (regulations); (2) none |
| s 108(1), (6) | claim-right to benefit for a prescribed disease or injury; (6) no-right where the disease is prescribed by occupation |
| s 108(2)-(5), s 109(2)-(4), (7) | power of the Secretary of State (regulations) |
| s 109(1) | claim-right to the same benefit and conditions as for an accident, subject to regulations |
| s 109(5), (6) | none (definitions of the appropriate percentage) |
| s 110(1), (2) | power of the Secretary of State (regulations) |
| s 110(3) | deeming that sets the least extent of disablement for pneumoconiosis |
| s 110(4) | no-right of the byssinosis claimant unless the loss is likely to be permanent |
| s 111 | none (blank) |


## Marginal readings for a lawyer (ssc4)

For a lawyer, not for me to decide. Two readings are taken as the status quo:

- (a) A failed "if", "unless", "until" or "while" counts as the text's own "no", clause by clause, within the provision that holds the word; and a flat negative ("shall not be entitled") counts as the text saying no.
  The other reading: "if A then B" does not itself say "if not A then not B", and a flat negative says no only to the case it describes; every branch below that rests on (a) would then answer NOTHING instead of JUST FALSE (or, for a flat negative, would not be a bar).
- (b) A prohibition or grant limited by its own wording does not say no outside the limit: the answer there is NOTHING.
  The other reading: the limit marks out the whole of what the text decides, so a case outside the limit is a "no" (JUST FALSE) or, for a bar, "no bar" (JUST FALSE).

The table lists, per function, the lines of its module where such a branch sits (the branch carries a `-- FALSE-kind` or `-- NOTHING-kind (limited by its own wording)` comment, or `the text says no (a flat negative)`).
Forks F1, F7, F8 and F11 are also readings of this kind and are listed in the fork register.
Totals over the seven modules: 64 branches on a failed "if", "unless", "until", "while" or "in the absence of" (reading (a)), 30 flat-negative branches (reading (a)), 87 branches limited by their own wording (reading (b)).
One branch is on the border of the two readings and is left as it stands: `s 66(1)(a)(i)` and `s 66(1)(b)` answer NOTHING when the person did not claim expressly on the ground of terminal illness, although the subsection opens "If a terminally ill person makes a claim expressly on the ground that he is such a person, then" (1958).
Under reading (a) the failed "If" would be JUST FALSE for `s 66(1)(a)(i)` (a deeming, like fork F6). For `s 66(1)(b)` NOTHING is kept on either reading, because its name claims entitlement and another route, `s 65(1)`, may supply it. The tests pin the NOTHING (`ssc4-tests-attendance-allowance.l4:189` and `:193`; seat case under `Under section 66(1)(b)`).

| module | function | reading (a): failed "if", "unless", "until", "while" branches (lines) | reading (a): flat-negative branches (lines) | reading (b): limited-by-own-wording branches (lines) |
| --- | --- | --- | --- | --- |
| attendance-allowance | `s 63(f)(i) a Category C retirement pension is payable in the case described` | - | - | 55 |
| attendance-allowance | `s 63(f)(ii) a Category D retirement pension is payable to the person` | - | - | 65 |
| attendance-allowance | `s 63(g) an age addition is payable in the case described` | - | - | 81 |
| attendance-allowance | `s 64(2) the person satisfies the day attendance condition` | 140 | - | - |
| attendance-allowance | `s 64(3) the person satisfies the night attendance condition` | 162 | - | - |
| attendance-allowance | `s 64(1) the person is entitled to an attendance allowance` | 179 | - | - |
| attendance-allowance | `s 65(1) the period is one for which the person is entitled to an attendance allowance` | - | - | 251, 253, 256, 267 |
| attendance-allowance | `s 65(4) the person is barred from an attendance allowance for the day by the date of claim` | - | - | 311 |
| attendance-allowance | `s 65(6)(a) the claim may be made on the day` | - | - | 330 |
| attendance-allowance | `s 65(7) the person is barred from an attendance allowance for the period by the Regulations` | 385 | 386 | 383 |
| attendance-allowance | `s 66(2)(a) the person is terminally ill at the time` | 401 | - | - |
| attendance-allowance | `s 66(1)(a)(i) the person is taken to satisfy both the day attendance condition and the night attendance condition on the day` | - | - | 418 |
| attendance-allowance | `s 66(1)(b) the day is in the period for which the person is entitled to attendance allowance` | - | - | 449 |
| attendance-allowance | `s 66(2)(b) the other person is regarded as making the claim` | - | - | 459 |
| carers-allowance | `s 70(1) the person is entitled to a carer's allowance for the day` | 75, 76, 77, 78 | - | - |
| carers-allowance | `s 70(1A) the person continues to be entitled to a carer's allowance for the day` | 112 | - | 109, 110 |
| carers-allowance | `s 70(3) the person is barred from a carer's allowance by age or education` | 139 | 137, 138 | - |
| carers-allowance | `s 70(4) the person is barred from a carer's allowance by the residence and presence conditions` | 150 | 151 | - |
| carers-allowance | `s 70(4A) the person is barred from a carer's allowance for the period by the Regulations` | 163 | 164 | 161 |
| carers-allowance | `s 70(7) the person is barred from a further allowance for the day` | - | 176, 177 | 178 |
| carers-allowance | `s 70(7ZA) the person is the one who has the relevant entitlement for the day` | - | - | 193 |
| carers-allowance | `s 70(7ZB) subsection (7ZC) applies` | - | - | 213 |
| carers-allowance | `s 70(7ZC) the other person B is barred from a relevant entitlement for the day` | 231, 232 | 233 | 230 |
| carers-allowance | `s 70(7A) the person has a relevant entitlement` | 247 | - | - |
| disability-living-allowance | `s 71(2) the person's entitlement to disability living allowance is an entitlement to the components` | - | - | 43 |
| disability-living-allowance | `s 71(3) the terms of the award are permitted` | 61 | - | 63 |
| disability-living-allowance | `s 71(6) the person is barred from a disability living allowance by the residence and presence conditions` | 106 | 107 | - |
| disability-living-allowance | `s 71(7) the person is barred from a disability living allowance while entitled to a Scottish or pension age payment` | 121 | 120 | - |
| disability-living-allowance | `s 72(1A) the conditions in subsection (1) are satisfied as modified for the part of a period before he reaches 16` | 161 | - | 168 |
| disability-living-allowance | `s 72(1) the person is entitled to the care component for the period` | - | - | 193 |
| disability-living-allowance | `s 72(2) the person is barred from the care component by the 3 month and 6 month requirements` | 230 | 228, 229 | - |
| disability-living-allowance | `s 72(5)(b) the person is taken to satisfy or to be likely to satisfy the conditions on the day` | - | - | 325 |
| disability-living-allowance | `s 72(7B) the person is barred from the care component for the period by the Regulations` | 339 | 340 | 337 |
| disability-living-allowance | `s 73(1AB) the person falls within this subsection` | 439 | - | - |
| disability-living-allowance | `s 73(2) the person falls within this subsection` | 453 | - | - |
| disability-living-allowance | `s 73(3) the person falls within this subsection` | 470 | - | - |
| disability-living-allowance | `s 73(1) the person is entitled to the mobility component for the period` | - | - | 520 |
| disability-living-allowance | `s 73(4A) the condition in subsection (1)(d) is taken to be satisfied for the part of a period before he reaches 16` | 538 | - | 537, 540 |
| disability-living-allowance | `s 73(8) the person is barred from the mobility component for the period by his condition` | 549 | 550 | - |
| disability-living-allowance | `s 73(9) the person is barred from the mobility component by the 3 month and 6 month requirements` | 572 | 570, 571 | - |
| disability-living-allowance | `s 73(12)(a) the person is barred from the mobility component by the 6 month requirement alone` | 652 | 653 | 647 |
| disability-living-allowance | `s 73(12)(b) the weekly rate of the mobility component of a terminally ill person in pounds` | - | - | 670 |
| disability-living-allowance | `s 73(14) the payment is disregarded in applying an enactment under which regard is to be had to a person's means` | 686 | - | 685 |
| disability-living-allowance | `s 74(1) the person is deemed for the purposes of section 73 to satisfy the condition mentioned in subsection (1)(a) of that section` | - | - | 724 |
| disability-living-allowance | `s 75(1) the person is barred from a component of disability living allowance for the day after pensionable age` | 741 | 742 | 739 |
| disability-living-allowance | `s 76(1) the person is barred from a disability living allowance for the day by the date of claim` | - | - | 758 |
| disability-living-allowance | `s 76(3) the other person is regarded as making the claim` | - | - | 774 |
| guardians-and-aged | `s 77(1) the person is entitled to a guardian's allowance in respect of the child or qualifying young person` | 46, 47 | - | - |
| guardians-and-aged | `s 77(3) the person is barred from a guardian's allowance by the parents' conditions` | 59 | 60 | - |
| guardians-and-aged | `s 77(6) the condition in subsection (5)(b) is satisfied` | 81, 84 | - | - |
| guardians-and-aged | `s 77(4) the amount is barred from payment by the conditions in subsection (5)` | 103 | 104 | - |
| guardians-and-aged | `s 77(9) the person is the one who is entitled to the guardian's allowance` | - | - | 126 |
| guardians-and-aged | `s 77(9) payment may be made to the man` | 141 | - | 139 |
| guardians-and-aged | `s 77(11) subsection (10) does not terminate the person's entitlement` | - | - | 173 |
| guardians-and-aged | `s 77(10) the person is barred from a guardian's allowance because he or she is the parent` | - | 185 | 183 |
| guardians-and-aged | `s 78(3) the person is entitled to a Category D retirement pension` | 232 | - | 227, 228 |
| guardians-and-aged | `s 78(7) the entitlement continues on the day` | - | - | 258 |
| guardians-and-aged | `s 78(8) the Category D retirement pension is barred from payment for the day` | - | 268 | 269 |
| guardians-and-aged | `s 79(1) the person is entitled to an age addition to a retirement pension` | - | - | 284 |
| guardians-and-aged | `s 79(3) the age addition is payable on the day` | - | - | 312 |
| increases | `s 86A(1) the increase of incapacity benefit for an adult dependant in pounds` | - | - | 24 |
| increases | `s 87(1) the amount of any increase is determined in accordance with regulations under this section` | - | - | 44 |
| increases | `s 87(2) the person is barred from an increase under the regulations` | - | 56 | 57 |
| increases | `s 88 the person is barred from an increase in respect of a further person for the same period` | - | 68 | 69 |
| increases | `s 89(1) the payment counts as earnings in sections 82 and 86A` | 100 | - | - |
| increases | `s 89(1A) the PPF periodic payment counts as earnings in sections 82 and 86A` | 113 | - | - |
| increases | `s 91(2) the person falls within this subsection` | 132 | - | - |
| increases | `s 91(1) the beneficiary is barred from the increase by a trade dispute` | 145 | 144 | - |
| increases | `s 92(1) the award continues in force` | 165 | - | 163 |
| increases | `s 92(1) the increase is barred from payment for the week by the relevant earner's earnings` | 179 | 178 | 177 |
| increases | `s 92(2) the earnings relevant to the week in pounds` | - | - | 190 |
| increases | `s 93 the increase in respect of the dependant is treated as having been payable to the person on the day` | - | - | 232, 233 |
| industrial-injuries-general | `s 94(1) the personal injury is of a kind mentioned in section 94(1)` | - | - | 30 |
| industrial-injuries-general | `s 94(1) industrial injuries benefit is payable` | - | - | 39 |
| industrial-injuries-general | `s 94(3) the accident is taken to have arisen out of the employment` | 71 | - | 70 |
| industrial-injuries-general | `s 94(5) the person is barred from industrial injuries benefit for an accident outside Great Britain` | 88 | 90 | - |
| industrial-injuries-general | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` | - | - | 103 |
| industrial-injuries-general | `s 95(3) the employment is employed earner's employment in relation to the accident` | 133 | - | - |
| industrial-injuries-general | `s 95(4) the reference is construed as a reference to an insured person or insurable employment` | - | - | 145 |
| industrial-injuries-general | `s 97(2) the relevant employment is treated as employed earner's employment` | - | - | 250 |
| industrial-injuries-general | `s 98 the accident is taken by this section to arise out of and in the course of the employment` | 265, 266 | - | - |
| industrial-injuries-general | `s 99(1) the accident is taken by this section to arise out of and in the course of the employment` | 300, 301, 302 | - | 298, 299 |
| industrial-injuries-general | `s 100 the accident is taken by this section to arise out of and in the course of the employment` | 321 | - | 319 |
| industrial-injuries-general | `s 101 the accident is treated by this section as arising out of the employment` | 350, 351, 352 | - | 348, 349 |
| disablement | `s 103(1) the person is entitled to disablement pension` | 47, 48 | - | 46 |
| disablement | `s 103(2) the earlier disablement may be added` | - | - | 75 |
| disablement | `s 103(5) there is taken to be no relevant loss of faculty` | - | - | 143 |
| disablement | `s 103(6) the person is barred from a disablement pension for the day by the 90 days` | 168 | - | - |
| disablement | `s 103(7) the weekly rate at which the disablement pension is paid in pounds` | - | - | 179 |
| disablement | `s 103(8) the pension ceases on the death of the beneficiary` | - | - | 191, 193 |
| disablement | `s 104(1) the weekly rate of the pension is increased for constant attendance` | 207 | - | 206 |
| disablement | `s 104(1) the amount of the increase in pounds` | - | - | 227 |
| disablement | `s 104(2) the increase is payable on the day` | - | - | 240 |
| disablement | `s 105(1) the weekly rate of the pension is further increased` | - | - | 275 |
| disablement | `s 105(1) the amount of the further increase in pounds` | - | - | 300 |
| disablement | `s 105(2) the increase is payable on the day` | - | - | 311 |
| disablement | `s 106 Schedule 7 has effect in relation to the benefit or increase` | - | - | 355 |
| disablement | `s 107(1)(a) the person is barred from an aggregate weekly rate above the appropriate amount` | - | - | 400, 402 |
| disablement | `s 107(1)(a) the aggregate rate exceeds the appropriate amount` | - | 413 | 413 |
| disablement | `s 107(1)(a) the aggregate weekly rate the person may receive for the same period, apart from increases, in pounds` | - | - | 426 |
| disablement | `s 108(1) industrial injuries benefits are payable in respect of the prescribed disease or injury` | - | - | 454 |
| disablement | `s 108(6) the person is barred from benefit in respect of a disease as an injury by accident` | 472 | 471 | 470 |
| disablement | `s 110(3) the least assessed extent of the disablement treated as resulting, as a percentage` | - | - | 591 |
| disablement | `s 110(4) the person is barred from disablement benefit in respect of byssinosis` | 603, 604 | 605 | 602 |

### Reading a result: FALSE and NOTHING (ssc4)

Every layer-1 rule answers `MAYBE BOOLEAN` (or `MAYBE NUMBER`, `MAYBE DATE`); the seat does the same.

- `JUST TRUE` means the text says yes on these facts.
- `JUST FALSE` means the text says no in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "unless", "until" or "while"; a list it closes ("consists of", "are those under the following"); a flat negative. Every such branch carries a `-- FALSE-kind (the text says no in its own words): "<quote>"` comment.
- `NOTHING` means the text does not answer: it is silent, the list is not closed, it says "includes", a term is undefined, the answer is in a rule or a figure outside the sources (a regulation, a Schedule 4 amount, another part's section), or the rule is limited by its own wording and the case falls outside the limit. Every such branch carries `-- NOTHING-kind (<why>)`.
- A caller must never turn `NOTHING` into `FALSE`. In a seat answer, `NOTHING` is "the Act, as rendered here, does not answer on these facts", not "no".
- Bar polarity. A function named "is the person barred from ..." answers `JUST TRUE` when the text says not entitled, `JUST FALSE` when the text says no bar (a failed "if", an "unless" met, an exception), `NOTHING` when it is silent or the case is outside the rule's own wording.
- Grant polarity. A grant written with "if" answers `JUST FALSE` when a limb of the "if" fails; a grant written with "where", or "shall be" with no "if/only if/unless", answers `NOTHING` when its conditions fail (forks F1 and F7).
- Deeming polarity (ss 94(3), 98-101). The function answers whether THIS SECTION treats the accident as arising out of and in the course of the employment; `JUST FALSE` there is a failed limb of the section's own "if" (in s 94(3), of "in the absence of evidence to the contrary") and is not a finding that the accident did not so arise (fork F6).
- Inputs. A prescribed condition or any fact that depends on a regulation is `MAYBE BOOLEAN` in layer 1 and a plain yes-or-no in the seat; a Schedule 4 amount is `MAYBE NUMBER` in layer 1 and a number in the seat; a judgment the Act hands to the Secretary of State is a plain fact reported from the decision.

## Seams (ssc4)

A seam is another part's answer taken as an input, named with the label of the answering section (PLAN.md section 1.3). At the merge the lead replaces the input by a call.

Asked by ssc4 (the plan names these):

| plan | asking section | answering section | input | type |
| --- | --- | --- | --- | --- |
| S18 | s 77(6) | ssc5 s 143(1)(b) | `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)` | `MAYBE BOOLEAN` |
| S20 | s 94(5) | ssc5 ss 117, 119, 120 | `s 117 the accident falls within the exception`, `s 119 ...`, `s 120 ...` | `MAYBE BOOLEAN` each |
| S21 | s 103(1) | ssc9 Schedule 6 | `sch 6 the extent of the disablement assessed, as a percentage` | `MAYBE NUMBER` |
| S22 | s 87(1), (2) | ssc3 s 60 | `s 60(1) the retirement pension would be payable only by virtue of section 60` | `MAYBE BOOLEAN` |
| S23 | s 93 | ssc2 ss 30C(5), 42 | `s 30C(5) the person is entitled to the higher rate of short-term incapacity benefit`, `s 42 the person is entitled to long-term incapacity benefit` | `MAYBE BOOLEAN` each |

Answered by ssc4 (the plan names these):

| plan | answering section | name of the answering function | asked by |
| --- | --- | --- | --- |
| S19 | s 94(1) | `s 94(1) the personal injury is of a kind mentioned in section 94(1)` | ssc3 s 60 |
| S36 | s 94(6) | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` | ssc9 Schedule 7 |

Seams the plan lacks, found while encoding (the same pattern, `MAYBE BOOLEAN` or `MAYBE NUMBER`):

- `s 2(1)(a) the person is an employed earner` (`inputs/ukpga-1992-4.txt:35`, "employed earner" means a person who is gainfully employed in Great Britain ...): asked by ss 94(1) and 103(1); `s 2(1)(a) by virtue of the employment the person is an employed earner` asked by s 95(1). Answering part: ssc1 (s 2).
- `s 143 the beneficiary would be treated for the purposes of Part IX as having the child or qualifying young person living with him`: asked by s 77(4). Answering part: ssc5 (s 143).
- `sch 6 the extent of the disablement if so assessed, as a percentage`: asked by s 103(5), second limb. Answering part: ssc9 (Schedule 6).
- Schedule 4 amounts (the table is omitted from the rendering): `sch 4 pt III para 1` (attendance allowance, higher and lower), `para 4` (carer's allowance), `para 5` (guardian's allowance), `para 7` (Category D retirement pension), `para 8` (age addition), `sch 4 pt IV col 3` (adult dependant), `sch 4 pt V paras 1, 2, 2(a), 3, 4` (disablement pension, constant attendance, exceptionally severe disablement, successive accidents); and the rates the Act says "shall be prescribed" in ss 72(3) and 73(10): `s 72(3) the highest/middle/lowest weekly rate of the care component in pounds`, `s 73(10) the higher/lower weekly rate of the mobility component in pounds`. All `MAYBE NUMBER`; the answering part is ssc8 (Schedule 4) or regulations outside the sources.
- `s 109(2) the percentage added in accordance with regulations under section 109(2) made by virtue of section 109(4)(b)`: asked by s 103(2); the answer is in regulations outside the sources.
- K2 (keel ss 173): `s 173(a) the person is over 3`, `over 5`, `over 80`, `under 16`, and `under 16 on the date on which the award ... would begin` (ss 63(f)(ii), 63(g), 70(3), 72(1), 72(2A), 73(1), 73(4A), 73(9A), 78(3), 79(1), 79(2)); `MAYBE BOOLEAN`.
- Inside the range, no seam: `s 66(2)` (terminal illness) is passed to ss 72(5), 73(12) as a yes-or-no input and the seat supplies the same answer to both.
- Not seams, though they look like one: the references to other Acts (the Jobseekers Act 1995 s 14 in s 91(2); the Pensions Act 2004 in s 89(3); the Social Security Act 1998 s 29 in s 97(1)(b)) are asked as facts the person can state.


## What the text turns out to say (ssc4)

Numbered findings. Each cites the text it rests on; none says what the official text says.

1. **Blank provisions.** The rendering shows as dotted lines: s 63(b), ss 68 and 69 (severe disablement allowance), s 70(5), (6), (10), s 72(6), s 78(1), (2), (4)(d), (5), ss 80 to 86 and s 90, s 93(a)(ii), s 102 and s 111. That is 22 coverage rows. The core's `Benefit` therefore has no severe disablement allowance, and Part IV has one live increase rule, s 86A (adult dependants of incapacity benefit); s 87(1) refers to "sections 82 to 86A" (2235), s 89(1) to "sections 82 and 86A" (2243) and s 91(1) to "sections 82 to 88" and "regulations under section 90" (2254-2255), and ss 82 to 86 and 90 are blank here.
2. **Schedule 4 is not in the text.** Every rate and amount the sections "specify" in Schedule 4 (and the "three weekly rates" and "two weekly rates" that ss 72(3) and 73(10) say shall be prescribed) is an input.
3. **Section 95A is outside the list in s 95(5)(a).** "this section and sections 96 to 110" (2296) skips s 95A, which sits between ss 95 and 96; it comes in, if at all, under (b), "any other provisions of this Act so far as they relate to those sections". `s 95(5)` has the three limbs as inputs and does not decide this.
4. **Section 95A(3) points at the wrong subsection.** It says the term "has the same meaning as in section 95(4)" (2302), but s 95(4) only uses the term and s 95(5) defines it (fork F10).
5. **The 14 and 20 per cent thresholds interact.** s 103(1) sets 14 per cent, or 20 per cent "on a claim made before 1st October 1986" (2347); s 103(3) treats an assessment of 14 to 19 per cent on a claim made on or after that date as 20 per cent (2355). So for a later claim the least assessment is 14 and the rate is that of 20 per cent; for an earlier claim the least assessment is 20.
6. **The 90 days in s 103(6) skip Sundays.** "the period of 90 days (disregarding Sundays) beginning with the day of the relevant accident" (2358): counted as 90 non-Sunday days, a Monday accident gives a period that ends on the Saturday of the fifteenth week (fork F13).
7. **Section 94(5) depends on three sections of another part.** The bar for an accident outside Great Britain is "Subject to sections 117, 119 and 120" (2288); the exceptions are not in ssc4's ranges (seam S20).
8. **Section 94(6) narrows "work" for Part V.** "work" in "incapable of work" and "incapacity for work" means work the person can reasonably be expected to do (2289); PLAN.md notes that s 171G(1)(a) keeps the Part XIIA incapacity test out of Part V.
9. **Two editorial gaps.** A line of `...` follows s 77(1)(b) (2153), and several provisions carry `...` where words were omitted (for example s 93(a)(i), 2269, and s 108(1), 2398). The encoding follows the visible words only.
10. **The list in s 107(2) is closed.** The list of increases is closed: "are those under the following provisions of this Act" followed by section 104, section 105 and paragraph 2, 4 or 6 of Schedule 7 (2389-2392); no other increase is one referred to in subsection (1), and the function says so (JUST FALSE).
11. **Section 70(1A) and the Sunday.** The eight weeks begin "with the Sunday following the death (or beginning with the date of death if the death occurred on Sunday)" (1990), so a death on a Sunday starts the weeks on that day (tested with 5 January 2025, a Sunday).

## What the text does not answer (ssc4)

- Whether an accident arises "out of and in the course of" an employment in the ordinary law (s 94(1)): ss 94(3) and 98 to 101 add presumptions and deemings, and the rest is a judgment the text does not supply; the seat asks it as a fact.
- Every prescribed condition, residence and presence condition, prescribed relative, prescribed description of training scheme, prescribed person, prescribed exception and prescribed time limit: regulations outside the sources.
- Every Schedule 4 amount and the Schedule 6 assessment of disablement.
- What follows for a person who is not an employed earner (s 103(1) speaks only of "an employed earner"), and what follows when no pension category or allowance in s 64(1A) is named (the list is not closed).
- The meaning of "relate to" in ss 95(5)(b) and 109(2), of "significant portion of the day", "substantially in excess", "prolonged", "frequent" and "constant attendance": undefined terms; they are inputs.
- Whether the day of attaining pensionable age counts as "after" (fork F4), month-end counting (F2), and the other forks.
- Anything in the blank sections (finding 1).

## What the stable binary does not accept (ssc4)

Found on 1.6.98 (main) while encoding; the second build 1.6.108 reads every module the same way (`check.sh` target main).

- `XOR` does not exist: write the exclusive or with `AND`, `OR` and `NOT`.
- `x NOT EQUALS NOTHING` does not parse: write `NOT (x EQUALS NOTHING)`.
- `WHEN ctor WITH last THEN` does not parse in `CONSIDER`: bind the field by position, `WHEN \`ctor\` last THEN`.
- A `CONSIDER` on one line with a long scrutinee, followed by `WHEN` on the same line, gives "unexpected WHEN": put `CONSIDER` and each `WHEN` on its own line.
- A `WHERE` inside a `CONSIDER` arm is invalid: use helper functions.
- `NOT (a) AND b` parses as `NOT ((a) AND b)`: write `((NOT (a)) AND b)`; every `NOT` is parenthesised in these files and `grep -n "NOT (.*) *\(AND\|OR\)\|\(AND\|OR\) NOT" *.l4` finds the hazards.
- `APPEND` and `++` are for strings: join lists with `append` or `concat`.
- A `DEONTIC` cannot be compared in `#ASSERT`, and a lapsed `MAY` also gives FULFILLED, so the regulative rules are tested by reading `#TRACE` and by asserting the plain functions beside them.
- `YMD` is never defined here; dates are `Date d m y`.
- `Date` rolls an impossible date (a 31st in a 30-day month, say) forward into the next month, which is why the month helper returns NOTHING at month ends instead of calling it (fork F2).


## The independent reviewer's 13 failures in this range (ssc4)

An independent reviewer ran its own assertions against the merged encoding; 13 of the failing ones fall in lines 1912-2443.
Each was re-checked against the text and the function, not against the reviewer's own concession.
Result: 1 defect fixed, 2 reviewer slips, 10 branches kept as they are (each on a stated NOTHING ground).
The reviewer's source lines are the lines of `ukpga-1992-4.txt`; the column "kept" names the brief's ground for NOTHING.

| id | provision | verdict | the ground, in one line |
| --- | --- | --- | --- |
| S303b | s 94(3) (2286) | DEFECT, fixed | "in the absence of evidence to the contrary" is an unless-type condition; the siblings in ss 98-101 answer JUST FALSE on a failed "if" (fork F6), so NOTHING here was inconsistent. With evidence to the contrary the answer is now JUST FALSE for the subsection only; not in the course of the employment stays NOTHING |
| S271c | s 70(3) (1993) | reviewer slip | "shall not be entitled ... if he is under the age of 16 or receiving full-time education": neither limb is the case where the "if" fails, JUST FALSE; the reviewer's own note says "this bar does not apply" |
| S273 | s 70(7ZA) (2001) | reviewer slip | the inputs say an election and a determination each named another person, and "one of them only shall have that entitlement" closes the choice, so JUST FALSE; the no-election, no-determination case the note describes is NOTHING (test at `ssc4-tests-carers-allowance.l4:109`) |
| S258a | s 63(f)(ii) (1922) | NOTHING kept | "payable to persons over the age of 80" describes a class in a list of descriptions; no "if", "only", "unless" or flat negative; limited by its own wording; reading (b) |
| S267b | s 66(1)(b) (1962) | NOTHING kept | "so much of the period ... as does not fall before the date of the claim" states a period and is not a flat negative on the person; another route (s 65(1)) may cover the day; limited by its own wording; reading (b) |
| S295b | s 79(1) (2205) | NOTHING kept | "A person who is over the age of 80 and entitled ... shall be entitled": a grant to a described class; limited by its own wording; reading (b) |
| S301b | s 94(1) (2280) | NOTHING kept | "shall be payable where": "where" is the brief's "when" family, not "if" or "only if"; another route exists (s 108); fork F7; the predicate is named for a kind, and the SNAP-style rule that a predicate named for its limit answers JUST FALSE past it would point the other way, so the branch is flagged |
| S307b | s 95(4) (2294) | NOTHING kept | "in relation to any time before 6th April 1975" is a stated period; not a "means"; limited by its own wording; reading (b) |
| S318b | s 103(5) (2357) | NOTHING kept | "shall be taken to be no relevant loss of faculty when the extent ... would not amount to 1 per cent": "when" is the brief's example of a limit; at 1 per cent or more Schedule 6 decides; reading (b) |
| S322b | s 104(1) (2362) | NOTHING kept | "Where a disablement pension is payable in respect of an assessment of 100 per cent.": a named case; the "if" limb that follows answers JUST FALSE (`ssc4-disablement.l4:207`); reading (b) |
| SEAT46 | s 104(2) (2363) | NOTHING kept | "shall be payable for such period as may be determined ..., but may be renewed from time to time": a stated period and an express renewal; reading (b) |
| SEAT34 | s 65(4) (1949) | NOTHING kept | a flat negative for "any period preceding the date" of the claim; the day of the claim is outside the stated period; same shape as ss 76(1), 78(8), 88; reading (b) |
| SEAT42 | s 88 (2240) | NOTHING kept | a flat negative for "more than one person"; one person is outside the named complement; reading (b) |

The two readings stay open for a lawyer.
The pattern the table shows is the one the brief states: where the limiter is "if", "unless", "while", "until", "means" or "only", the function answers JUST FALSE past it (`s 70(3)`, `s 94(5)`, `s 103(6)`, `s 98`); where the limiter is a stated period, a named complement, "where" or "when", it answers NOTHING.


## What check.sh prints (ssc4)

Run in the foreground from this folder on 2026-11-04 as `L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh`; exit status 0.
The baseline it replaced: this folder began with `ssc-core.l4` alone (1 module, 0 assertions); the keel's own run over `ssc-core.l4`, `ssc-definitions-tests.l4` and `ssc-definitions.l4` was 165 assertions satisfied (`KEEL-NOTES.md`), and those two files are not in this folder.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc4-attendance-allowance.l4                   0         0       0        0         0 |      0         0       0        0  same
ssc4-carers-allowance.l4                       0         0       0        0         0 |      0         0       0        0  same
ssc4-cases-seat.l4                             0       356       0        0         0 |      0       356       0        0  same
ssc4-disability-living-allowance.l4            0         0       0        0         0 |      0         0       0        0  same
ssc4-disablement.l4                            0         0       0        0         0 |      0         0       0        0  same
ssc4-guardians-and-aged.l4                     0         0       0        0         0 |      0         0       0        0  same
ssc4-increases.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc4-industrial-injuries-general.l4            0         0       0        0         0 |      0         0       0        0  same
ssc4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc4-tests-attendance-allowance.l4             0       121       0        0         0 |      0       121       0        0  same
ssc4-tests-carers-allowance.l4                 0        80       0        0         0 |      0        80       0        0  same
ssc4-tests-disability-living-allowance.l4       0       166       0        0         0 |      0       166       0        0  same
ssc4-tests-disablement.l4                      0       213       0        0         0 |      0       213       0        0  same
ssc4-tests-guardians-and-aged.l4               0        80       0        0         0 |      0        80       0        0  same
ssc4-tests-increases.l4                        0        66       0        0         0 |      0        66       0        0  same
ssc4-tests-industrial-injuries-general.l4       0       131       0        0         0 |      0       131       0        0  same
TOTAL (17 modules)                             0      1213       0        0           |      0      1213       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `check --strict` over the seven layer-1 modules: 495 `src:` lines, 190 runs, 190 locators, 0 problems in each mode.
Every definition in the seven modules carries an `@ref` directly above it (checked by script).

## Peeked, and files the harness attached

I opened nothing under `~/.claude/`, nothing under `commons`, `commonswt` or `canon`, no existing encoding, and no other directory under `runs/`: nothing to report under `peeked`.
The harness attached to my context files that are not mine, and I did not use them for this task: `/Users/mengwong/CLAUDE.md`, `/Users/mengwong/.claude/rules/l4-ide-on-nye.md`, `/Users/mengwong/src/legalese/l4-ide/CLAUDE.md`, and the auto-memory index `/Users/mengwong/.claude-work/projects/-Users-mengwong-src-legalese-l4-ide/memory/MEMORY.md` (with its one-line entries; I opened none of the files it points at).
The files attached from `inputs/` (`ssc-core.l4`, `COMMONS-CLAUDE.md`, and the brief and plan re-read after a compaction) are mine to read.
