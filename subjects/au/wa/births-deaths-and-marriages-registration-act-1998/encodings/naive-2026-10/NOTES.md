# Births, Deaths and Marriages Registration Act 1998 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example encodings and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use.

**Edition:** the compilation deposited at
`../../registers/source-bundle/mrdoc_49099.txt` (retrieved 2026-09-07). Its
compilation table runs to the Births, Deaths and Marriages Registration Amendment
(Sex or Gender Changes) Act 2024 Pt 2, in force 30 May 2025, and it carries
"© State of Western Australia 2025". The deposit states no compilation number. The
Assisted Reproductive Technology and Surrogacy Act 2025 Pt 15 is listed as
uncommenced and is not shown.

**Checks:** one module (`bdm-registration.l4`), one case file
(`bdm-cases-registration.l4`): 53 assertions written, 53 satisfied, 0 errors,
0 warnings.

## Why this Act, and why scoped

It is requirement **au/wa:REQ-0001**, priority 1, raised 12 times by the three
Western Australian cradle-to-grave lives: chloe c001 (her birth registered, day
nineteen), c054 (her marriage in Kings Park), c062 and c071 (Oliver's and Ella's
births), c086 (Graham's death at home), c096 and c098 (Liam's and Chloe's deaths);
jake k001 (his birth registered, day fifteen), k051 (Ruby born to unmarried
parents, both signing) and k097 (his death); daniel d001 (his birth registered,
day nine, in 1996) and d092 (his death).

The lives ask who must register a birth and by when, whether both unmarried
parents may be registered, what of the child's name, what registers a marriage,
and who registers a death and by when. This encoding takes those questions and the
definitions and exceptions they need: s 2 with the compilation table's
commencement date; ss 12, 13, 15, 16, 18, 19(3)-(4) and 22; Part 6 (ss 37-39); and
Part 7 ss 40, 42, 44, 45, 47 and 48. Not encoded: administration (Part 2), court
orders beyond their effect as an input (ss 20-21, 41), given-name changes (s 23),
parentage changes (Part 4), change of name (Part 5), change of registration of sex
or gender (Part 5A), suspected deaths (s 43), removal of remains from the State
(s 46), the Register and certificates (Part 8), and Part 9. Fees and approved forms
are set outside the Act and none was retrieved.

## What the Act turns out to say

### 1. Daniel's birth in 1996 is not governed by this Act

The compilation table: "Act other than s. 1 and 2: 14 Apr 1999". Daniel was born on
9 April 1996 and registered on 18 April 1996 (d001), three years before the Act
came into operation. The ledger asks this Act about that event, but it cannot
answer it; the law then in force is not deposited. Chloe's registration on
2 April 2003 (c001) is within it. Asserted.

### 2. The funeral director notifies a death; the Registrar registers it

s 42: the funeral director or other person who arranges for the disposal of the
remains must, "within 14 days of the date of death", lodge a death registration
statement and give the Registrar the doctor's certificate. s 48(1): "The Registrar
is to register a death". c086's title ("the funeral director registers the death")
blurs the two. The doctor's part is not 14 days either: s 44 gives the doctor
**48 hours** to certify the cause, and the certificate goes to the funeral director,
not the Registrar. No certificate is required where the doctor must report the death
to a coroner under s 17(3) of the Coroners Act 1996 (s 44(5)). For Graham, who died
on 19 August 2052, day 14 is 2 September 2052. Asserted.

### 3. The scenarios cite the wrong provisions

The lives' citations do not match the deposited numbering. "Part 5 (registration of
marriages)" is Part 6; Part 5 is change of name. "Part 6" for deaths is Part 7. The
parents' 60-day duty is in ss 15-16, not ss 12-13: s 12 is the hospital's (or
attendant's) notice within one month, and s 13 says when a birth must be registered.
"s 13 (both parents may register)" is s 15, and "s 19 (names)" is s 22; s 19 is about
adding details and a later change of surname. The encoding follows the deposit. Not
an assertion.

### 4. Both parents register jointly; marriage plays no part

s 15(1): "The parents of a child are jointly responsible for having the child's
birth registered ... (and must both sign the birth registration statement)". The
Registrar may take one parent's statement only where joining the other is
impracticable (death, disappearance, ill health, unavailability, or unwarranted
distress). s 18(1)(a): a joint application by both parents is enough for both
identities to be registered. Neither section mentions marriage, so Ruby's unmarried
parents (k051) stand as married parents would. Asserted.

### 5. Sixty days, but late is still accepted

s 16(1): the statement must be lodged "within 60 days after the date of the birth"
(penalty $1 000); s 16(2): "The Registrar must accept a birth registration statement
even though it is lodged after the end of the 60 day period." Chloe (day 19) and Jake
(day 15) are in time. Separately, s 12 requires the "responsible person" to notify the
Registrar within one month. For a public hospital that is the chief executive of the
health service provider; for a private hospital, its chief executive officer or
general manager. The encoding assumes, without reading it anywhere, that KEMH (c062) is
a public hospital, and reads "one month" as a calendar month (an inference). Asserted.

### 6. A marriage solemnised in WA must be registered, and Part 6 sets no deadline

s 37: "If a marriage is solemnized in the State, the marriage must be registered".
s 38: by lodging the certificate under the Marriage Act 1961 (Cth). Its note says the
celebrant's duty to lodge comes from s 50(4) of the Commonwealth Act, so the WA Act
places no duty or time limit on anyone for Chloe's marriage (c054). Registration is
asserted; the absence of a time limit is noted, not asserted.

### 7. The name is a matter of choice

s 22(3): nothing requires both a surname and a given name, or that "the surname be the
same as that of a parent". The statement need not name a stillborn child or one who
dies within 28 days (s 22(2), s 4 "neonatal death"). The Registrar may assign a name
if the name given is prohibited or the parents cannot agree (s 22(4)). Asserted.

## What would need doing before this is worth anything

- The law in force before 14 April 1999, for Daniel's 1996 registration, is not
  deposited.
- The regulations (fees, prescribed matters) and the Registrar's approved forms were
  not retrieved.
- "Within one month" (s 12) and "within 14 days of" (s 42) are counted by an
  inference about calendar months and day counts, not by any interpretation Act.
- The scenarios' citations (finding 3) should be corrected in the scenario files by
  whoever maintains them.
- No case law or Registry practice was consulted.
