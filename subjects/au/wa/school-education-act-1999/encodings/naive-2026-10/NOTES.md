# School Education Act 1999 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example encodings and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** the compilation deposited at
`../../registers/source-bundle/mrdoc_49345.txt` (mrdoc 49345, retrieved
2026-09-07). Its compilation table runs to the Education and Care Services National
Law Application Act 2026 Pt 6 Div 7, in force 1 May 2026; the last reprint it lists
is Reprint 4 as at 19 February 2016; it carries "© State of Western Australia 2026".
The deposit states no compilation number. The uncommenced provisions table lists
only the Act's own s 182(3) and s 208.

**Checks:** one module (`sea-schooling.l4`), one case file
(`sea-cases-schooling.l4`): 56 assertions written, 56 satisfied, 0 errors,
0 warnings. A deliberately wrong expectation was confirmed to fail.

## Why this Act, and why scoped

It is requirement **au/wa:REQ-0005**, priority 1, raised 8 times by the three
Western Australian cradle-to-grave lives: chloe c010 (kindergarten in Armadale,
4 February 2008), c011 (Year 1, 1 February 2010: "From which year must she
attend?"), c078 (Oliver's Year 1, 2 February 2037: "Which school must enrol
him?"); jake k010 (Year 1, 4 February 2013), k011 (Year 4, 31 days absent, 20 May
2016: "Whose duty is attendance, and what can the Department do before it
prosecutes a parent?"), k024 (10 November 2022: "May a 16-year-old leave
school?"); daniel d010 (Year 1, 3 February 2003) and d054 (Luca's Year 1,
2 February 2037).

The lives cite ss 6, 9, 11B, 23, 38, 39-40 and 78. This encoding takes those and
what they need: s 4 (child, parent, final years), s 5, s 6, ss 9-11 with ss 11C,
11D, 11F, 11G and 11H for their effect on s 9(1), s 25, ss 41-42, and ss 75, 76
and 79 beside s 78. Not encoded: s 11AA, s 11E (combinations of courses), s 24
beyond a flag, ss 27-31, attendance officers' powers (ss 33-37), s 43 onward,
home education (Division 6) beyond registration as a flag, and Parts 3 to 9
except ss 60 and 75-79. Regulations, Ministerial orders under s 11B(2), intake-area
orders under s 60 and school-year orders under s 117 were not retrieved; they are
inputs.

Dates of birth are those in the lives' `facts.json`: Chloe 14 March 2003, Jake
30 August 2006, Daniel 9 April 1996, Oliver 5 September 2030, Luca 2 February
2030.

## What the Act turns out to say

### 1. Year 1 is not the first compulsory year for any of the five children

s 6(1) counts from "the beginning of the year in which the child reaches the age
of" 6 years 6 months (to 31 December 2012) or 5 years 6 months (from 1 January
2013). There is no "by 30 June" in the text, although c011 says there is. Chloe
reaches 6 years 6 months in September 2009, so 2009 is her first compulsory year,
not 2010 as c011 says. Daniel's is 2002 (d010 is in 2003), Oliver's 2036 (c078 is
in 2037), and Luca's 2035, two years before d054 puts him in Year 1. Asserted.

### 2. Jake's compulsory period ends on his 18th birthday, not at the end of the year he turns 17

k024 cites s 6 as "compulsory to the end of the year he turns 17". That is
paragraphs (a) and (b), which govern only until 31 December 2013. Paragraph (c),
from 1 January 2014, ends the period at "the end of the year in which the child
reaches the age of 17 years and 6 months" or when "the child reaches the age of
18, whichever happens first". Jake reaches 17 years 6 months in February 2024 and
18 on 30 August 2024, so his period ends on 30 August 2024. Asked under paragraph
(b) it would have ended on 31 December 2023. Asserted.

### 3. A 16-year-old may leave, but only into a listed option, full time, with notice

On 10 November 2022 Jake is in "the final 2 years of the compulsory education
period" (s 4), which on this reading began after 30 August 2022. s 11B(1) lets him,
"despite section 9(1)", take a university or higher education course, an approved
VET course, an apprenticeship, employment with the Minister's approval (s 11G), or
a prescribed course. s 11C requires full-time participation. Once the parent's s 11D
notice is given it is in force (s 11D(7)) and s 9(1) stops applying (s 11F(2)). In
March 2022 he was not yet in the final years. Employment without the Minister's
approval, and leaving with no option at all, do not qualify. Whether a TAFE
pre-apprenticeship is an "approved VET course" is a question for the Vocational
Education and Training Act 1996; it is an input here. Asserted.

### 4. Which paragraph applies turns on the date the question is asked, so Jake's first compulsory year moved

ss 5 and 6 are written as "until 31 December 2012", "from 1 January 2013". Read (an
inference) as choosing the paragraph by the date of the question, Jake's first
compulsory year is 2013 when asked in 2012, but 2012 when asked in 2013, so he was
inside the period from 1 January 2013 either way. The same switch shortens his
precompulsory period from 2011-2012 to 2011 alone. The deposit's note 3 records a
similar transitional rule in the 2005 amending Act. Asserted, on that reading.

### 5. Kindergarten is not compulsory

Chloe's kindergarten year, 2008, falls in her precompulsory education period (s 5:
from the year she reaches 4 years 6 months, 2007, to the year she reaches 5 years 6
months, 2008). s 9(1) speaks only of "the compulsory education period", so it does
not apply to her that year. Asserted.

### 6. Attendance: the parent's duty is criminal, the Panel only advises, and a prosecution needs a certificate

s 23 puts the duty to attend on the student. s 38(1) makes a parent of an enrolled
child of compulsory school age commit an offence ($1,000) if the child does not
comply, and s 38(2) makes the child commit one ($10). An absence is excused under s
25 only if it is caused by incapacity or another reasonable cause and the principal
is told within 3 school days, with a medical certificate if the principal asks for
one. A principal, an attendance officer or the chief executive officer may refer a
persistent case to an Attendance Panel (s 40(1)). A class teacher may not, unless
designated an attendance officer. The Panel inquires, advises and assists, may
advise a responsible parenting agreement under the Children and Community Services
Act 2004 (s 40(3A)), and reports. Nothing in ss 39-40 lets it fine or order anyone.
A s 38 prosecution needs a s 42 certificate that reasonably practicable steps were
taken and breaches continued, and, once a Panel has advised, a failure to follow
that advice (s 41(1)). Asserted.

### 7. "Parent" in the offence provisions means only the day-to-day parent

s 4 defines a parent as one with long-term or day-to-day responsibility, "except in
sections 9(2), 10(1)(b), 25, 27, 38(1) and Division 6 of Part 2 where it has only
the meaning given by paragraph (b)". A parent with only long-term responsibility
commits neither the s 9(2) offence ($2,500) nor the s 38(1) offence. Asserted.

### 8. The local-intake school must take a child from its intake area, with or without room

s 78(1) entitles a child of compulsory school age to enrol at a local-intake school
if the child usually lives in its intake area and an appropriate educational
programme is available. Classroom accommodation is a condition only for a child
from outside the area (s 78(2)). s 76(1) first requires usual residence in the
State and entitlement to reside permanently in Australia, unless the regulations
provide otherwise. s 75(1) says the principal "is to enrol" an entitled child on a
duly made application. So the answer to c078 is Oliver's local-intake school, if
his home is in its gazetted intake area (s 60), which is an input. Asserted.

## What would need doing before this is worth anything

- The 2002-2010 events are answered from paragraph (a) of the **current**
  compilation. s 6 was inserted in its present form by No. 46 of 2012. The text in
  force in 2002 and 2003, before the Acts Amendment (Higher School Leaving Age and
  Related Provisions) Act 2005, was not deposited or read.
- "Final 2 years" is computed as the dates after the date two years before the
  period's last day. Neither the boundary day nor a 29 February birthday has been
  checked.
- The School Education Regulations 1999, the s 11B(2) orders, the intake-area
  orders and the school-year orders were not retrieved.
- s 11E (combinations of courses), s 11H(6) (part-time employment), s 11I and ss 43-44
  are read but not encoded.
- No case law was searched.
