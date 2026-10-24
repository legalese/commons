# NOTES: Interpretation Act (Canada), R.S.C., 1985, c. I-21

Row `legalese-sonnet-5.5`: one Sonnet 5.5 agent working alone from the brief in `BRIEF.md`, no subagents, no other encoding read.
Status: `draft`. No domain expert has read it against the statute.

## 0. The source, and what it is not

- Source file: `R.S.C.-1985-c.-I-21.txt`, a plain-text rendering made by a converter script from the Department of Justice Canada consolidation current to 2026-09-30 (last amended 2024-11-27).
  It is **not the official text**, it is not marked up, and nothing here is "verified against the official text".
  Terms and provenance: `SOURCE-LICENSE.md` here, and `STUB-SOURCE-LICENSE.md` and `SOURCES.md` in the subject's inputs.
- Every quotation in the `.l4` files is a `-- src:N | text` line produced by `srcrefs.py quote` (driven by `requote.py`) from that file, and the gate `srcrefs.py check --strict` is part of `check.sh`.
- **Languages.** The deposit is the English version only.
  The Act itself says nothing of which language version governs.
  The deposit's own line 3 says the French version is equally authoritative; the subject's `STUB-SOURCE-LICENSE.md` repeats that and cites the Constitution Act, 1982, s 18 and the Official Languages Act, s 13, neither of which is in the deposited text.
  Section 21(2) of the Act speaks of "each of the English and French versions of the enactment" without ranking them.
  Four definitions carry the marker "(Version anglaise seulement)" in place of a French term (`enact` and `repeal` in s 2(1), `commencement` and `herein` in s 35(1); lines 17, 23, 283, 308 of the text).
  `commencement` is one of the time words this encoding relies on.
  The French version is therefore a **fork** (F-LANG): nothing here has been compared with it.
- **Target.** The brief names no target compiler.
  It requires `REFUSE`, `@lang en` and `#ASSERT REFUSED`, which a `main` build rejects (`references/dialects.md` of the writing-l4-rules skill), so the only target that can hold this encoding is **`unstable`**.
  `check.sh` was run with `L4_TARGET=unstable`, and the main comparison was not made.
- **Binary.** `L4_BIN` is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (checked against the brief); `l4 --version` printed `dev` when run on 2026-10-21.
- **One Hint on every module.** The linter prints, for the line `@lang en`: "A module that declares nothing is English; this line can go." The brief requires the line, so it stays; the Hint is not an error and is not counted by `check.sh`.

## 1. What is encoded and what is not

Four modules and eight test files.
`ca-interpretation-time.l4` imports only `prelude` and `daydate`, as the brief requires; the calendar and repeal modules and the tests import it or `prelude`/`daydate`.

**Encoded** (the section and the module in §2):

- **Time module** (`ca-interpretation-time.l4`): the last day of a period of N days, months or years after, from or before a day (ss 27(4), 27(5), 28, 37(1)); the clear-day and between-events counts (s 27(1), (2)); the words that tie a time to a day (s 27(3)-(5)); whether a date falls inside a period; the last day on which a thing may be done when the time ends on a holiday (s 26), for periods in days, months and years and for several holidays in a row; the day, and the moment within the day, from which an Act, a regulation, a provision postponing its own commencement and a proclamation bind or take effect (ss 5, 6, 7, 18(3), 23(2), (3), (5)); when an enactment ceases to have effect (s 6(1)); age (s 30); the calendar, financial and Dominical year (s 37); the calendar month (s 35(1)); the time within which a regulation is laid before Parliament (s 39(1)); the definition of "regulation" (s 2(1)).
- **Calendar module** (`ca-interpretation-calendar.l4`): the three days of "holiday" that the text dates; the combination with the caller's holidays and with s 26; "commencement"; "standard time" and s 29; "local time" (refused).
- **Repeal module** (`ca-interpretation-repeal.l4`): ss 2(2), 39(2), 43, 44, 46.
- **Rules module** (`ca-interpretation-rules.l4`): ss 3(1), 8, 9, 11, 17, 19, 20, 21, 22, 23(1), 25(1), 32, 34, 35(1) "corporation" and "security", 41(1), 35(2) and the Schedule.

**Holidays, days of rest and recess are inputs.**
The time module takes a function `DATE -> BOOLEAN` from the caller and has no calendar.
The calendar module adds the three days the text dates and leaves the rest, which the text names without a date, to the caller.
Every test supplies its own calendar.

**Refused, never defaulted** (the text is silent or names only some cases): weeks; deemed service or notice; a day of rest, recess or closed office that is not a holiday; a count that is not a whole number of at least one; an anniversary that does not exist (s 30); an Act whose day is still to be fixed; a regulation that is neither registered nor of an exempted class; a boundary meridian; the cases each of ss 8(2.1), 8(2.2), 19, 20, 21, 22, 25, 32, 34, 41, 43, 44 and 46 does not name.

**Not encoded** is in §2: 30 sections or subsections are marked `inert` with a reason; two rows are repealed and two are not applicable.

## 2. Coverage table

One row per section or subsection group, and one for the Schedule and one for the Related Provisions.
Lines are lines of the deposited text (the numbering `srcrefs.py` uses).

| reference | lines | disposition | where, or why not |
| --- | --- | --- | --- |
| s 1 short title | 11 | not applicable | names the Act and gives its short title; it states no rule that has an input or an output. |
| s 2(1) "regulation" | 20-22 | encoded | `is a regulation` (time module). The definition says what a regulation includes; an instrument under neither limb is refused, not called a non-regulation. |
| s 2(1) "Act", "enact", "enactment", "public officer", "repeal" | 16-19, 23 | inert | Five vocabulary definitions. "enactment" (an Act or regulation "or any portion") and "enact"/"repeal" ("includes") are relied on in the comments of the modules, but no computation turns on them: each only widens what a word names, and what falls inside the widened name (a revoked or cancelled instrument, a federal public servant) is a fact the caller brings, with nothing for a function to compute. |
| s 2(2) expired and replaced enactments | 25 | encoded | `for the purposes of the Act, an enactment is treated as repealed if` (repeal module). |
| s 3(1) application | 29 | encoded | `a provision of the Act applies to an enactment unless` (rules module). |
| s 3(2) application to this Act | 31 | inert | Says the Act's provisions apply to interpreting the Act itself. A function would take no input that changes the answer (it is always yes) and would return nothing a caller could use. |
| s 3(3) rules of construction not excluded | 33 | inert | A saving: nothing in the Act excludes a rule of construction not inconsistent with it. It has no condition and no result; it only declines to displace other law. |
| s 4(1), (2) enacting clause, order of clauses | 37-40 | inert | Gives a form of words for an Act's enacting clause and an order for its parts. It is a direction on how Parliament drafts; no consequence for a person turns on it, and nothing in the text says what follows from a departure. |
| s 5(1) endorsement of the day of assent | 46 | inert | A duty of the Clerk of the Parliaments to endorse the day of assent on the Act. Its product, the day of assent, is the input `the day the Act was assented to` of the commencement functions; the duty itself has no computable consequence. |
| s 5(2) date of commencement | 48 | encoded | `the date of commencement of an Act that provides none, assented to on` (time module). |
| s 5(3) a provision for a later commencement | 50 | encoded | `the moment from which a provision postponing commencement is itself in force, for an Act assented to on` (time module). |
| s 5(4) remaining provisions | 52 | encoded | Covered by `the coming into force of the provision of an Act` with `it names no day` (time module): the remaining provisions are in force from the expiration of the day before assent. |
| s 6(1) a particular day; expiry on a particular day | 56 | encoded | `the coming into force of the provision of an Act`, `the coming into force of a regulation`, `the moment of ceasing to have effect of an enactment expressed to expire on`, and the moment functions (time module). |
| s 6(2)(a) an Act with no day | 58-59 | encoded | `the coming into force of the provision of an Act` (time module). |
| s 6(2)(b) a regulation with no day | 60 | encoded | `the coming into force of a regulation` (time module); registration and the exempted class are inputs because s 6 and s 5(1) of the Statutory Instruments Act are not in the text. |
| s 6(3) judicial notice of a day fixed by a published regulation | 62 | encoded | `judicial notice shall be taken of the day` (time module); a day fixed otherwise, or by a regulation not so published, is refused. |
| s 7 preliminary proceedings | 66 | encoded | `a regulation made or a thing done before commencement has effect on` (time module). |
| s 8(1) territorial operation | 70 | encoded | `an enactment applies to the whole of Canada unless` (rules module). |
| s 8(2) amending enactment | 72 | encoded | `a provision of an amending enactment applies to a part of Canada where` (rules module). |
| s 8(2.1) exclusive economic zone | 74 | encoded | `an enactment applies also to the exclusive economic zone of Canada where` (rules module). |
| s 8(2.2) continental shelf | 76-79 | encoded | `an enactment applies also to the continental shelf of Canada where` (rules module). |
| s 8(3) extra-territorial operation of pre-1931 Acts | 81 | inert | Deems certain Acts enacted before 11 December 1931 to have been enacted with full power to legislate extra-territorially, where they were intended to have extra-territorial operation "expressly or by necessary or reasonable implication". Whether that intention exists is the interpretive question itself, and the rest is a historical saving; there is no input from which a function could answer it. |
| s 8.1 property and civil rights | 87 | inert | Says reference is made to a province's rules in force "at the time the enactment is being applied". It sends the reader to provincial law that is not in the text, so a function would only return a pointer. |
| s 8.2 terminology | 89 | encoded | `the terminology or meaning adopted, where an enactment contains both civil law and common law terminology, is` (rules module); "unless otherwise provided by law" is refused. |
| s 8.3(1), (2) Indigenous peoples | 93-95 | inert | A rule of construction (every enactment is construed as upholding the rights recognised by s 35 of the Constitution Act, 1982) whose content is in that Act, which is not in the text. |
| s 9 private Acts | 99 | encoded | `a provision in a private Act affects a person's rights if` (rules module). |
| s 10 law always speaking | 103 | inert | A canon: a matter expressed in the present tense is applied to the circumstances as they arise. It governs how a sentence is read, and nothing in it has an input or a result. |
| s 11 "shall" and "may" | 107 | encoded | `the construction of the expression` (rules module); any other expression is refused. |
| s 12 enactments remedial | 111 | inert | A canon: a fair, large and liberal construction. It has no condition that can be tested and no result that can be computed. |
| s 13 preamble | 115 | inert | A rule that a preamble is read as part of the enactment to assist in explaining its purport and object. It is a reading rule. |
| s 14 marginal notes | 117 | inert | A rule that marginal notes and references to former enactments form no part of the enactment. It is a reading rule: it excludes text from the text. |
| s 15(1), (2) application of definitions and interpretation rules | 121-125 | inert | Says where a definition or interpretation rule applies (every provision of the enactment; all other enactments on the same subject-matter unless a contrary intention appears). A function would need the structure of the enactment and the subject-matter of each other enactment, which are not in the text. |
| s 16 words in regulations | 127 | inert | Says expressions in regulations have the meanings they have in the enactment conferring the power. It points at another enactment's definitions, which are not in the text. |
| s 17 Her Majesty | 131 | encoded | `an enactment binds or affects Her Majesty or Her Majesty's rights or prerogatives if` (rules module). |
| s 18(1), (2) proclamations | 135-137 | inert | Say a proclamation is understood to be a proclamation of the Governor in Council, and that a proclamation the Governor General is authorised to issue is understood to be issued under an order. They are identities between kinds of instrument, with no input. |
| s 18(3) effective day of proclamations | 139 | encoded | `the day a proclamation takes effect, issued under an order of` (time module). |
| s 18(4) | 140 | repealed or blank in this text | The text shows only "[Repealed, 1992, c. 1, s. 88]". |
| s 19(1) who may administer an oath | 144-146 | encoded | `an oath under an enactment or a rule of the Senate or House of Commons may be administered by` (rules module). |
| s 19(2) justice of the peace | 148 | encoded | `a power conferred on a justice of the peace ... may be exercised by a person who is a notary public or a commissioner for taking oaths if` (rules module). |
| s 20 reports to Parliament | 152 | encoded | `the Act that requires a report or document to be laid before Parliament requires it to be laid again at a subsequent session if` (rules module). |
| s 21(1) powers vested in corporations | 156-160 | encoded | `words establishing a corporation vest it with` (rules module), with (b) conditional on a bilingual name and (d) on a member not contravening. |
| s 21(2) corporate name | 162 | inert | Says the name of a corporation established with one-language names in each version consists of the form in each version. It assembles two strings from a fact (the names in each version) and has no condition to test. |
| s 21(3) banking | 164 | encoded | the banking row of `words establishing a corporation vest it with` (rules module). |
| s 22(1) majorities | 168 | encoded | `the smallest number that is a majority ... when they number` (rules module). |
| s 22(2) quorum | 170-176 | encoded | `a quorum exists, where the number of members is fixed at`, `a quorum exists, where the members in office number`, `an act or thing done at a meeting by`, `a vacancy does not invalidate ...` (rules module). |
| s 23(1) office during pleasure | 180 | encoded | `a public officer is deemed appointed to hold office during pleasure only unless` (rules module). |
| s 23(2) appointment under the Great Seal | 182 | encoded | `the day an appointment under the Great Seal takes effect, issue authorized on` (time module). |
| s 23(3) appointment otherwise than under the Great Seal | 184 | encoded | `the day an appointment otherwise than under the Great Seal takes effect, duties begun on` (time module); the sixty-day limit is "more than", so exactly sixty days is inside. |
| s 23(4) remuneration | 186 | inert | Grants the appointing authority a power to fix, vary or terminate remuneration. A grant of power has no condition to test and no value to compute. |
| s 23(5) commencement of appointments or retirements | 188 | encoded | `the moment an appointment or a termination is deemed to take effect, if it is effective on` (time module). |
| s 24(1)-(5) implied powers | 190-205 | inert | Five rules that words authorising an appointment, a minister or an officer "include" further powers and further persons (successors, deputies, a person for the time being in the office). Each turns on facts about offices and persons that the text does not state and the encoding cannot derive; (3) limits (2)(c) and (d) for regulations as defined in the Statutory Instruments Act, which is not in the text. |
| s 25(1) documentary evidence | 209 | encoded | `in judicial proceedings, where an enactment provides that a document is evidence of a fact, and` (rules module). |
| s 25(2) Queen's Printer | 211 | inert | A presumption about what a printed name or title on a copy of an enactment purports. It is evidence law about a physical copy. |
| s 26 time limits and holidays | 215 | encoded | `the last day on which a thing may be done when the time limited ends on`, `a thing may be done on`, `the last day on which a thing may be done within` and the calendar-module wrapper (time and calendar modules). |
| s 27(1) clear days | 217 | encoded | `the number of clear days between`, `there are at least`, `the earliest day of the second event ...` (time module). |
| s 27(2) days not clear | 219 | encoded | `the number of days, not expressed to be clear days, between` and its inverse (time module). |
| s 27(3) begin or end at, on or with a day | 221 | encoded | `the first day of a time bounded at its start by`, `the last day of a time bounded at its end by` (time module). |
| s 27(4) after or from a day | 223 | encoded | `the period of` n `days after` / `days from` and the word functions (time module). |
| s 27(5) within a time after, from, of or before a day | 225 | encoded | `the period of` n `days before` and the word functions (time module). |
| s 28 months after or before a day | 227-230 | encoded | `the period of` n `months after` / `from` / `before`, written in the section's three steps (time module). |
| s 29 time of the day | 232 | encoded | `the Greenwich time of a time of the day of` (calendar module). |
| s 30 age attained | 234 | encoded | `the anniversary of` and `a person born on ... has attained` (time module). |
| s 31(1)-(4) miscellaneous powers | 238-244 | inert | Four rules about what a power or duty includes or how it is exercised (the officer's jurisdiction extends to the place; ancillary powers; from time to time; a power to make regulations includes a power to repeal or vary them). Each is satisfied or not by facts the text does not describe; none has a result. |
| s 32 forms | 246 | encoded | `a deviation from a prescribed form does not invalidate the form used where` (rules module). |
| s 33(1)-(3) gender, number, grammatical forms | 248-252 | inert | Reading rules: words importing one sex include the other and corporations; the singular includes the plural; other forms of a defined word have corresponding meanings. They operate on the words of another text. |
| s 34(1) classes of offence | 256-259 | encoded | `the class of an offence created by an enactment where`, `a person convicted on summary conviction is considered convicted of an indictable offence ...` (rules module). |
| s 34(2) Criminal Code to apply | 261 | encoded | `the provisions of the Criminal Code that apply to an offence of the class` (rules module). |
| s 34(3) documents construed | 263-265 | encoded | `the class an offence is construed to be, where a document ... refers to it and` (rules module). |
| s 34.1 entry into dwelling-houses | 269-271 | inert | Gives a person who may issue an arrest warrant the powers a judge or justice has under the Criminal Code to authorise entry. It is a grant of power defined by reference to Criminal Code provisions that are not in the text. |
| s 35(1) "holiday" | 309-311 | encoded | `is a Sunday`, `is Labour Day`, `is the National Day for Truth and Reconciliation`, `is a holiday under section 35(1), given the other holidays` (calendar module): three days are dated by the text; the rest are named without a date and are the caller's. |
| s 35(1) "month" | 325 | encoded | `the calendar month containing` (time module), and s 28 throughout. |
| s 35(1) "commencement" | 283 | encoded | `the commencement of an enactment that comes into force as` (calendar module). |
| s 35(1) "standard time" and "local time" | 335-342, 323 | encoded | `the standard time of`, `the minutes behind Greenwich time of` (calendar module); "local time" is refused because the text does not state what a place observes. |
| s 35(1) "corporation", "security" | 293, 334 | encoded | `in an enactment, a corporation is`, `the number of persons sufficient for security or sureties` (rules module). |
| s 35(1) "Commonwealth" and "British Commonwealth"; s 35(2) | 284, 278, 362 | encoded | `is a country named in the schedule`, `is a member of the Commonwealth after orders under section 35(2), if` (rules module). |
| s 35(1) repealed definition entries (five) | 295, 300-302, 315 | repealed or blank in this text | Five entries. The text shows "[Repealed, 1990, c. 17, s. 26]" for "county court", "[Repealed, 2002, c. 8, s. 151]" for each of the three Federal Court entries, and "[Repealed, 2014, c. 2, s. 14]" for "legislative assembly, legislative council or legislature". |
| s 35(1) every other definition | 276-360 | inert | The other forty-one of the fifty-five definition entries of s 35(1): institutions, places, officers and technical words ("bank", "broadcasting", "Canada", "contiguous zone", "diplomatic or consular officer", "oath", "person", "province", "superior court", "telecommunications", "writing" and the rest). Each names a thing by reference to other law (the Bank Act, the Oceans Act, the National Defence Act) or by a list of places and courts. None has a time, a condition or a computed value, and none changes an answer about when something binds or how a period ends. |
| s 36 telegraph | 364 | inert | Deems the word "telegraph" not to include "telephone" in the enactments it names. It is a constant with no input. |
| s 37(1) "year" | 366-369 | encoded | `the period of` n `years after`, `the calendar year numbered`, `the financial year or fiscal year beginning in`, `the Dominical year numbered` (time module). |
| s 37(2) the Governor in Council may define "year" | 371 | encoded | `the meaning prescribed under section 37(2)` (time module). |
| s 38 common names | 373 | inert | A rule of reading: a name commonly applied to a thing means that thing. It operates on the words of another text. |
| s 39(1) affirmative and negative resolution | 375-379 | encoded | `the last day for laying a regulation made on`, `the regulation made on ... may be laid on`, `a regulation subject to affirmative resolution can have come into force, given that` (time module). |
| s 39(2) effect of negative resolution | 381 | encoded | `a regulation annulled by a resolution passed on ... is in force on` and three more (repeal module). |
| s 40(1) citation of enactments | 385-387 | inert | Says how an Act or a regulation may be cited. It is a rule on forms of reference. |
| s 40(2) citation includes amendment | 389 | inert | Deems a citation to be a citation of the enactment "as amended". It does not say as amended up to what date, so no function can pick a version from it. |
| s 41(1) two or more parts | 391 | encoded | `a reference from` n `to` m `includes` (rules module): the two ends are included; any other number is refused. |
| s 41(2)-(5) references to parts, subsections, regulations, other enactments | 393-399 | inert | Four rules on which enactment or division a reference points at. They need the structure of the enactment in which the reference occurs. |
| s 42(1)-(3) power of repeal or amendment | 403-407 | inert | Reserves to Parliament the power to repeal or amend, allows amendment in the same session, and says an amending enactment is read as part of the enactment it amends. Each is a statement of power or a reading rule with no condition or result. |
| s 43 effect of repeal | 409-415 | encoded | `what section 43 says the repeal does to`, `it may be instituted, continued, enforced or imposed as if the enactment had not been repealed, if it is` (repeal module). |
| s 44(a)-(h) repeal and substitution | 417-428 | encoded | Eight functions, one per paragraph (repeal module). |
| s 45(1)-(4) repeal or amendment does not imply | 430-436 | inert | Four rules that a repeal, amendment, re-enactment, revision or consolidation is not to be deemed to involve a declaration (that the enactment was in force, that the law differed, about the previous state of the law, or an adoption of a judicial construction). Each says what must NOT be inferred; a function would return the same constant for every input. |
| s 46(1), (2) demise of the Crown | 440-444 | encoded | `a demise of the Crown affects` (repeal module): the offices, oaths and court proceedings named are not affected; anything else is refused. |
| Schedule (Section 35) | 446-497 | encoded | `the countries named in the schedule`: the fifty-one names, one per line of the text (rules module). |
| Related Provisions, 1998, c. 30, s. 10 | 499-503 | not applicable | A transitional section of the amending Act of 1998 about proceedings commenced before that section came into force. It governs the 1998 amendments' own transition and does not interpret anything. |

Counts: 94 rows.

- encoded: 60
- inert: 30
- repealed or blank in this text: 2
- not applicable: 2

Total 94.

The s 35(1) definition entries are counted in groups, not one by one: of its 55 definition entries, nine are encoded (holiday, month, commencement, standard time, local time, corporation, security, Commonwealth, British Commonwealth), five are repealed, and the other forty-one are in the one `inert` row.

## 3. Fork register

Every ambiguity I saw, the readings, the one taken and the text that licenses it.
A comment in a module that says "fork F-..." names an entry here.

**F-LANG. Which language version governs?**

- Readings seen: English governs; French governs; both equally.
- Taken: English only is encoded; the French version is not deposited and nothing here was compared with it.
- Licensing text: The Act does not say. Its own text mentions "each of the English and French versions of the enactment" without ranking them (s 21(2), line 162). The deposit's line 3 says "the French version is equally authoritative"; the subject's `STUB-SOURCE-LICENSE.md` repeats that and cites the Constitution Act, 1982, s 18 and the Official Languages Act, s 13, which are NOT in the deposited text. Four definitions carry "(Version anglaise seulement)" in place of a French term ("enact", "repeal", "commencement", "herein"; lines 17, 23, 283, 308), so the French version has no counterpart term for "commencement", a word this encoding relies on.

**F-TARGET. Which compiler is the encoding written for?**

- Readings seen: main; unstable.
- Taken: unstable. check.sh was run with `L4_TARGET=unstable`, so the main comparison was not made.
- Licensing text: The brief names no target but requires `REFUSE`, `@lang en` and `#ASSERT REFUSED`; the writing-l4-rules skill's `references/dialects.md` records that a main build rejects `@lang` ("unexpected '@'"), `REFUSE`, `#ASSERT REFUSED` and `YMD` (rows for probes 01, 02, 03 and 05). The encoding uses all four.

**F-DAY. What is a "day"?**

- Readings seen: A calendar day from midnight to midnight; a period of 24 hours from the event.
- Taken: A calendar day, represented by a `DATE`; moments within a day matter only at its boundaries.
- Licensing text: The text never defines "day". Section 6(1) speaks of "the expiration of the previous day" and "the commencement of the following day", and s 30 of "the commencement of the anniversary", which treat a day as a unit with a first and a last moment. The encoding does not model a time of day inside a day except for s 29 (`the Greenwich time of a time of the day of`).

**F-COUNT-START. Does a period "after" a day, or "from" it, count that day?**

- Readings seen: It counts it (as day one or as day zero); it excludes it.
- Taken: It excludes it: the first day of the period is the next day.
- Licensing text: s 27(4) (line 223): a time expressed to "begin after" or "be from" a specified day "does not include that day"; s 27(5) (line 225): anything done "within a time after, from, of or before a specified day", "the time does not include that day"; s 28(b) (line 229): "excluding the specified day".

**F-FROM. Is a period "from" a day counted like one "after" it?**

- Readings seen: Yes; no (from includes the day).
- Taken: Yes: the functions `... days from`, `... months from`, `... years from` return what `... after` returns.
- Licensing text: s 27(4) and 27(5) treat "after" and "from" together. s 28 speaks only of months "after or before" a day, and s 37(1) defines a year without a preposition; the encoding carries the s 27 treatment of "from" over to months and years because nothing in the text separates them.

**F-LASTDAY. Which day is the last of a period of N days after a day, and is it inside the period?**

- Readings seen: The Nth day after the day, inside; the (N-1)th, inside; the Nth, outside (an exclusive end).
- Taken: The Nth day after the day (that is, the day plus N), inside the period.
- Licensing text: For days the text says only that the specified day is excluded (s 27(4), (5)); that N days then run from the next day to the day plus N is the arithmetic of counting N days that begin there. For months the text says it in terms: s 28(c) (line 230) "including in the last month counted ... the day". The first day of a period of months is the day after the specified day (s 28(b)), the last day the day with the same calendar number in the last month counted.

**F-BEFORE. How does a period before a day run?**

- Readings seen: From the day N before to the day before the specified day; from N-1 before; including the specified day.
- Taken: From N days (or the day with the same number N months earlier) before the specified day, to the day before it; the specified day is outside.
- Licensing text: s 27(5) lists "before" with "after" and "from" for the exclusion of the specified day (line 225); s 28 names "after or before" and its step (b) excludes the specified day (line 229).

**F-MONTH. Is a month a calendar month or a fixed number of days? What follows for a start on the 31st or on 29 February?**

- Readings seen: A calendar month (the same number in the next month); thirty days; the same number or the next day when there is none.
- Taken: A calendar month; when the last month counted has no day with the start day's number, the last day of that month.
- Licensing text: s 35(1) "month means a calendar month" (line 325); s 28(c) (line 230). One month after 31 January 2025 ends 28 February 2025 (the worked case); one month after 31 January 2024 ends 29 February 2024.

**F-YEAR. Is a year a calendar year, 365 days, or twelve months?**

- Readings seen: A calendar year; 365 days; twelve consecutive months counted by s 28.
- Taken: Twelve consecutive months: N years after a day is 12N months after it, counted by s 28. A start on 29 February thus ends on 28 February in a year that has no 29 February and on 29 February in one that has.
- Licensing text: s 37(1) (line 366): "The expression year means any period of twelve consecutive months", except a reference to a calendar year, a financial year or fiscal year, or a Dominical year (lines 367-369), which are encoded separately (`the calendar year numbered`, `the financial year or fiscal year beginning in`, `the Dominical year numbered`).

**F-26-UNITS. Does the rule moving a last day off a holiday apply to months and years, or only to days?**

- Readings seen: All units; days only.
- Taken: All units: the function that finds the day a thing may be done takes the last day of any period.
- Licensing text: s 26 (line 215): "Where the time limited for the doing of a thing expires or falls on a holiday, the thing may be done on the day next following that is not a holiday." It speaks of "the time limited" and names no unit.

**F-26-WHICH. Which days move a last day: holidays, days of rest, recess, a closed office?**

- Readings seen: Holidays only (the one word in s 26); Saturdays and Sundays; any day the office is closed.
- Taken: Holidays only, as s 35(1) defines them. Saturday is not one. A day of rest, a recess or a closed office that is not a holiday is refused.
- Licensing text: s 26 says "a holiday"; s 35(1) "holiday" (line 309) lists Sunday and not Saturday. The words "day of rest", "recess" and "closed" do not occur in the text.

**F-26-SEVERAL. What if several days in a row after the last day are holidays?**

- Readings seen: Move to the first non-holiday; move one day only.
- Taken: Move to the first day that is not a holiday, however many holidays precede it. The search stops after 366 days and refuses (a bound of the encoding, not of the Act).
- Licensing text: s 26: "the day next following that is not a holiday".

**F-26-GAP. If the last day is a holiday and the next day is also one, may the thing be done on that second holiday, which lies between the end of the period and the day s 26 names?**

- Readings seen: Yes (the days up to the day named are all open); no (only the days of the period and the one day named).
- Taken: No. Inside the period, or the one day s 26 names; the days in between are neither.
- Licensing text: s 26 names one day. Whether a holiday between is open is not stated.

**F-26-ON-HOLIDAY. Can the thing be done on the holiday itself?**

- Readings seen: No; yes.
- Taken: Yes. The last day of the period stays inside the period; s 26 adds a day, it does not take one away.
- Licensing text: s 26 says the thing "may be done" on the next day; it does not say it may not be done on the holiday.

**F-HOLIDAYS. Which days are holidays?**

- Readings seen: A list in the encoding; a calendar the caller supplies.
- Taken: A test the caller supplies, plus the three days the text itself dates (every Sunday; Labour Day, the first Monday in September; September 30, the National Day for Truth and Reconciliation). New Year's Day, Good Friday, Easter Monday, Christmas Day, the Sovereign's birthday, Victoria Day, Canada Day, Remembrance Day and the proclaimed, provincial and civic days are named without dates, so they are the caller's.
- Licensing text: s 35(1) "holiday" (lines 309-311); the brief: "Days of rest, recess and holiday are an INPUT, never computed".

**F-WEEK. How long is a week, and how is a period of weeks counted?**

- Readings seen: Seven days; the text is silent.
- Taken: Silent: `the period of` N `weeks after`, `from` and `before` refuse, and `the number of days in a week according to the Act` refuses. A caller who wants seven days per week can ask for 7N days; that is the caller's reading.
- Licensing text: The word "week" does not occur in the text (a search of the whole file).

**F-SERVICE. When is a document deemed served or a notice received?**

- Readings seen: The text has a rule; it has none.
- Taken: None: `the day a document is deemed served, if it was sent on` and `the day a notice is deemed received, if it was given on` refuse.
- Licensing text: The words "service", "served" and "notice" were searched for: the word "served" does not occur, "service" occurs once ("the services of a person", s 23(3), line 184), and "notice" occurs only in "Judicial notice" (s 6(3), lines 61-62). No section deems a document served or a notice given or received.

**F-6-MOMENT. From what moment of its commencement day does an enactment bind?**

- Readings seen: From the first moment of the day; from the moment of the event (assent, registration) within the day; from the end of the day.
- Taken: From the expiration of the day before, which is the first moment of the day itself: the expiration of 9 March and the commencement of 10 March are the same instant.
- Licensing text: s 6(1) (line 56): "coming into force on the expiration of the previous day"; s 6(2)(a) and (b) (lines 58-60): "on the expiration of the day immediately before the day the Act was assented to" / "... the regulation was registered" / "... made". The text does not say the Act binds from the first moment on the day of assent in so many words; it says "the expiration of the previous day".

**F-ASSENT. The brief asks about an Act "passed or published" on 2026-03-10. Which event counts?**

- Readings seen: The day of passing; the day of publication; the day of assent.
- Taken: Assent. The brief's case is answered as if 2026-03-10 is the day of assent.
- Licensing text: ss 5(1), 5(2) and 6(2)(a) (lines 46, 48, 58-59) key on assent, "the day the Act was assented to in Her Majesty's name". The words "passed" and "published" play no part in these sections.

**F-FIXED-LATER. An Act says it comes into force on a day to be fixed later, and the day is fixed as 2026-06-01. From when does it bind?**

- Readings seen: It is "not expressed to come into force on a particular day" until fixed, so s 6(2)(a) puts it in force at assent; once the day is fixed it is a particular day, and s 6(1) applies.
- Taken: The second: the Act is expressed to come into force on a day not yet known; once fixed, it comes into force on the expiration of the day before (2026-05-31). While the day is not fixed, no day decides it and the functions refuse.
- Licensing text: s 6(1) (line 56) "expressed to come into force on a particular day"; s 5(3) (line 50), which treats a provision that an Act is "to come into force on a day later than the date of assent" as itself in force at assent; s 6(3) (line 62), which speaks of "a day for the coming into force of an enactment that is fixed by a regulation". Nothing in the text says in terms which of the two readings s 6(2) takes.

**F-REG-SILENT. A regulation is made on 2026-03-10 and says nothing about when it comes into force. From what day?**

- Readings seen: From the day made; from the day registered; from the expiration of the day before either.
- Taken: It depends on two facts the brief's case does not give: if it is of a class exempted from s 5(1) of the Statutory Instruments Act, from the expiration of the day before the day it was made; otherwise from the expiration of the day before the day it was registered under s 6 of that Act; if neither the exemption nor the registration is known, no day yet decides it and the function refuses.
- Licensing text: s 6(2)(b) (line 60). The Statutory Instruments Act is not in the text.

**F-REG-DEF. Is an instrument issued under neither limb of the definition of "regulation" a regulation?**

- Readings seen: Yes; no.
- Taken: Not answered: `is a regulation` is true under either limb and refuses under neither.
- Licensing text: s 2(1) "regulation includes ... issued, made or established (a) ... or (b) ..." (lines 20-22): "includes" does not exclude.

**F-6-3. When is judicial notice taken of a day fixed for coming into force?**

- Readings seen: Always; only where fixed by a regulation published in the Canada Gazette.
- Taken: Only the second is answered (yes). A day fixed otherwise, or by a regulation not published there, is refused.
- Licensing text: s 6(3) (line 62): "a regulation that has been published in the Canada Gazette".

**F-39-THEN. What does "if Parliament is not then sitting" fix "then" at?**

- Readings seen: The day the regulation is made; the end of the fifteen days.
- Taken: The day the regulation is made.
- Licensing text: s 39(1) (lines 376-379): "within fifteen days after it is made or, if Parliament is not then sitting, on any of the first fifteen days next thereafter that Parliament is sitting". The fifteen days "after" exclude the day made (s 27(5)).

**F-39-LAYING. If the body is sitting on the day the regulation is made, must it also be sitting on the day of laying?**

- Readings seen: Yes; no.
- Taken: No: the text names no sitting requirement for the day of laying in that case, so none is added. If the body was not sitting on the day made, laying is on a sitting day ("that Parliament is sitting").
- Licensing text: s 39(1) (lines 376-379).

**F-39-AFFIRM. When does an affirmed regulation come into force?**

- Readings seen: On affirmation; on its own day under s 6; later.
- Taken: Not answered: not affirmed is a no ("shall not come into force unless and until it is affirmed"); affirmed refuses.
- Licensing text: s 39(1)(a), (b) (lines 376-377).

**F-39-2-MOMENT. At what moment of the day of a resolution is a regulation revoked and the law it revoked revived?**

- Readings seen: From the first moment of the day (as s 6(1) does for a commencement day); from the moment of the resolution; from the end.
- Taken: Before the day: regulation in force, earlier law not. After the day: the reverse. On the day itself: refused.
- Licensing text: s 39(2) (line 381): "deemed to have been revoked on the day the resolution is passed", "deemed to be revived on the day the resolution is passed". Section 6(1) fixes the moment for an enactment "expressed to" cease on a day, which a deemed revocation is not.

**F-30-LEAP. When is the anniversary of 29 February attained, in a year with no 29 February?**

- Readings seen: 28 February; 1 March; section 28 by analogy.
- Taken: Not answered: `the anniversary of` refuses.
- Licensing text: s 30 (line 234) speaks of "the anniversary, of the same number, of the day of that person's birth"; it does not refer to s 28, whose terms are limited to "a period of time consisting of a number of months".

**F-23-3. Is a day expressed exactly sixty days before issue "more than sixty days before"?**

- Readings seen: Yes; no.
- Taken: No: sixty days is inside the subsection, sixty-one is not. A day expressed before the person began the duties is not within the subsection and refuses.
- Licensing text: s 23(3) (line 184): "unless that day is more than sixty days before the day on which the instrument is issued"; "on or after the day on which that person commenced the performance of the duties".

**F-STD-TIME. Which side of a boundary meridian does the line itself fall on?**

- Readings seen: East; west; either.
- Taken: Not answered: a west longitude exactly on a boundary refuses. Part of Ontario east of the 68th meridian is not covered by any paragraph and refuses.
- Licensing text: s 35(1) "standard time" (lines 337-340): "east of", "west of" and "between".

**F-22. What does "at least one-half of the number of members" mean for an odd number?**

- Readings seen: Round up to a whole person; compare without rounding.
- Taken: Compare without rounding: with five members, three present is a quorum and two is not (two is less than 2.5).
- Licensing text: s 22(2)(a)(i) (line 172): "at least one-half of the number of members". A majority is more than half (s 22(1), 22(2)(b)).

**F-34. An offence the enactment does not provide may be prosecuted by indictment, but the context indicates is indictable: which class?**

- Readings seen: Indictable; summary.
- Taken: Not answered: refused.
- Licensing text: s 34(1)(a) deems indictable only an offence the enactment provides may be prosecuted by indictment; (b) deems summary an offence "if there is nothing in the context to indicate that the offence is an indictable offence" (lines 257-258).

**F-41. What does a reference to two or more provisions include, other than the first and last mentioned?**

- Readings seen: Every number between; only the two ends.
- Taken: The two ends are answered (included). Any other number refuses.
- Licensing text: s 41(1) (line 391): "shall be read as including the number or letter first mentioned and the number or letter last mentioned".

**F-44-E. If the new enactment does not reduce or mitigate a punishment, which applies after the repeal?**

- Readings seen: The former; the new; not answered.
- Taken: The former: s 44(e) speaks only of a reduction, and s 43(d) and its closing words (lines 413, 415) keep a punishment incurred under the repealed enactment and allow it to be imposed "as if the enactment had not been so repealed". Before the repeal, the former enactment is still in force.
- Licensing text: ss 43(d), 43 closing words, 44(e) (lines 413, 415, 425). The choice is an inference from s 43, not a statement of s 44(e).

**F-NEGATIVE. What does an encoding return for the case a conditional rule does not address?**

- Readings seen: FALSE; a default; a refusal.
- Taken: A named refusal, wherever the text states a rule for some cases and says nothing for the rest ("so far as", "unless", "if", a list of named things).
- Licensing text: The brief: "Where the source does not answer, `REFUSE`." Examples: ss 8(2.1), 19(2), 20, 21(1)(b), (d), 22, 25(1), 32, 34, 41(1), 43, 44, 46.

**F-BOUNDS. How far does a search for the next non-holiday, or the next sitting day, go?**

- Readings seen: Without limit; to a bound.
- Taken: 366 days for the holiday search and 731 days for the sitting-day search, each ending in a refusal. The bounds are this encoding's, so that a calendar that is all holidays does not run forever; they are not the Act's.
- Licensing text: None. Tested at the edge in `ca-tests-holidays.l4`.

Where I looked and found no ambiguity, so that "none found" is not a bare claim: the words that make a time include or exclude a specified day in s 27(3) ("at, on or with", "to or until"); the meaning of "calendar month" and the three kinds of year in s 37(1)(a)-(c); the rule that a day expressed to come into force is in force from the expiration of the day before (s 6(1)); the three dated holidays in s 35(1); the five things s 43 names.

## 4. Expected answers fixed before coding (and how they came out)

Written from the text before any module existed; the `result` column was filled in after the run, and every row matched.

### 4.1 Periods counted from a day

The rule, for every row: the specified day is not counted (s 27(4), s 27(5); for months s 28(b)); a year is twelve consecutive months (s 37(1)), so N years after a day is 12N months after it and s 28 applies; the day in the last month counted that has the same calendar number, or the last day of a month that has no such day, is the last day of the period (s 28(c)).

| period | counted from | first day | last day | expected citation | result |
| --- | --- | --- | --- | --- | --- |
| three years | 2025-07-16 | 2025-07-17 | 2028-07-16 | ss 37(1), 28(a)-(c) | matches: 2025-07-17 to 2028-07-16 |
| five years | 2025-01-15 | 2025-01-16 | 2030-01-15 | ss 37(1), 28 | matches: 2025-01-16 to 2030-01-15 |
| five years | 2025-09-01 | 2025-09-02 | 2030-09-01 | ss 37(1), 28 | matches: 2025-09-02 to 2030-09-01 |
| thirty days | 2026-01-01 | 2026-01-02 | 2026-01-31 | s 27(4), (5) | matches: 2026-01-02 to 2026-01-31 |
| two years | 2024-02-28 | 2024-02-29 | 2026-02-28 | ss 37(1), 28 (24 months; February 2026 has a 28th) | matches: 2024-02-29 to 2026-02-28 |
| one year | 2024-02-29 | 2024-03-01 | 2025-02-28 | ss 37(1), 28(c) (February 2025 has no 29th, so its last day) | matches: 2024-03-01 to 2025-02-28 |
| one month | 2025-01-31 | 2025-02-01 | 2025-02-28 | s 28(c) | matches: 2025-02-01 to 2025-02-28 |

For every row the day after the last day is outside the period and the specified day itself is outside it.

### 4.2 Commencement

| case | expected | citation | result |
| --- | --- | --- | --- |
| an Act, assent on 2026-03-10, silent on commencement | binds from 2026-03-10, from the expiration of 2026-03-09 (the first moment of 2026-03-10) | s 5(2) gives the date, s 6(2)(a) the moment | matches: in force from the expiration of 2026-03-09 (the first moment of 2026-03-10) |
| an Act that comes into force on a day to be fixed later; day fixed as 2026-06-01 | binds from 2026-06-01, from the expiration of 2026-05-31 | s 6(1) once the day is particular | matches: in force from the expiration of 2026-05-31 (the first moment of 2026-06-01) |
| a regulation made on 2026-03-10, silent | depends on inputs the case does not give: if of a class exempted from s 5(1) of the Statutory Instruments Act, from the expiration of 2026-03-09 (the day made is 2026-03-10); otherwise from the expiration of the day before the day it is registered under s 6 of that Act; with neither, no day yet | s 6(2)(b) | matches, all three branches: exempt gives the expiration of 2026-03-09; registered 2026-03-12 gives the expiration of 2026-03-11; neither gives no day yet (a refusal when a day is asked for) |

The brief says "passed or published".
The text keys on the day of **assent** (ss 5(1), 5(2), 6(2)(a)), not on passing or publication, so the first row is "if 2026-03-10 is the day of assent".

### 4.3 Other expectations decided before coding

- Weeks: the text has no provision (the word "week" does not occur); the N-weeks function refuses.
- Deemed service or notice: the text has no provision; named refusal.
- s 26: a time limit whose last day is a holiday may be met on "the day next following that is not a holiday", so with Sundays as the only holidays 2026-03-08 (a Sunday) moves to Monday 2026-03-09; with 2026-03-09 and 2026-03-10 also holidays it moves to 2026-03-11; Saturday is not a holiday in s 35(1), so 2026-03-07 stays.
- s 28 counting backward: one month before 2025-03-31 begins on 2025-02-28 (no 31 February, so the last day of February).
- s 27(1)/(2): between events on 2026-03-01 and 2026-03-10 there are 8 clear days and 9 days not expressed to be clear.
- s 23(3): an effective day exactly 60 days before the day of issue is deemed the effective day; 61 days before is not.
- s 30: a person born 2000-03-15 has not attained 18 on 2018-03-14 and has on 2018-03-15.

Results for 4.3, after the run: every item held (weeks and service refuse: `ca-tests-counting.l4`; the s 26 rows: `ca-tests-holidays.l4`; one month before 2025-03-31: `ca-tests-periods.l4`; the s 27(1)/(2) counts, s 23(3) and s 30: `ca-tests-counting.l4`, `ca-tests-commencement.l4`, `ca-tests-other.l4`).

## 5. Answer table

The six worked cases and the three commencement cases, answered from the text.
"Test" names the file and the line of the section heading (or of the assertion) in this encoding.
For every period the specified day is outside it and the day after the last day is outside it; those are asserted in the same file.
"For doing a thing" is the day section 26 gives when the last day is a holiday, using only the three days the text dates and no others (a caller with provincial or proclaimed holidays supplies them and may get a later day).

| case | section | first day | last day | for doing a thing (s 26) | test |
| --- | --- | --- | --- | --- | --- |
| three years from 2025-07-16 | ss 37(1), 28(a)-(c) | 2025-07-17 | 2028-07-16 (a Sunday) | 2028-07-17 (Monday) | `ca-tests-periods.l4` 23; `ca-tests-holidays.l4` 133 |
| five years from 2025-01-15 | ss 37(1), 28 | 2025-01-16 | 2030-01-15 (a Tuesday) | 2030-01-15 | `ca-tests-periods.l4` 31; `ca-tests-holidays.l4` 137 |
| five years from 2025-09-01 | ss 37(1), 28 | 2025-09-02 | 2030-09-01 (a Sunday) | 2030-09-03: Monday 2030-09-02 is Labour Day, the first Monday in September (s 35(1)) | `ca-tests-periods.l4` 39; `ca-tests-holidays.l4` 135 |
| thirty days from 2026-01-01 | s 27(4), (5) | 2026-01-02 | 2026-01-31 (a Saturday, not a holiday) | 2026-01-31 | `ca-tests-periods.l4` 47; `ca-tests-holidays.l4` 138 |
| two years from 2024-02-28 | ss 37(1), 28 | 2024-02-29 | 2026-02-28 (a Saturday) | 2026-02-28 | `ca-tests-periods.l4` 55; `ca-tests-holidays.l4` 139 |
| one year from 2024-02-29 | ss 37(1), 28(c): February 2025 has no 29th, so its last day | 2024-03-01 | 2025-02-28 (a Friday) | 2025-02-28 | `ca-tests-periods.l4` 63; `ca-tests-holidays.l4` 140 |
| one month from 2025-01-31 | s 28(c): February 2025 has no 31st, so its last day | 2025-02-01 | 2025-02-28 (a Friday) | 2025-02-28 | `ca-tests-periods.l4` 71; `ca-tests-holidays.l4` 141 |

Weekdays in the table were checked with a calendar outside L4 (python3 `datetime`); no value in it came from the module's own output.

| commencement case | section | answer | test |
| --- | --- | --- | --- |
| An Act assented to on 2026-03-10 that says nothing about when it comes into force. (The brief says "passed or published"; the text keys on assent, fork F-ASSENT.) | s 5(2): the date of commencement is the date of assent. s 6(2)(a): in force "on the expiration of the day immediately before the day the Act was assented to". | It binds from **2026-03-10**, from the **expiration of 2026-03-09**, which is the first moment of 2026-03-10; it is not in force on 2026-03-09. | `ca-tests-commencement.l4` 33 |
| An Act that says it comes into force on a day to be fixed later; the day is fixed as 2026-06-01. | s 6(1), once the day is a particular day (fork F-FIXED-LATER); s 6(3) on judicial notice. | It binds from **2026-06-01**, from the **expiration of 2026-05-31** (a Sunday), the first moment of 2026-06-01. While the day is not fixed, no day decides it and the functions refuse. | `ca-tests-commencement.l4` 55 |
| Subordinate legislation (a regulation) made on 2026-03-10 that says nothing about when it comes into force. | s 6(2)(b); the Statutory Instruments Act ss 5(1) and 6 are not in the text. | If it is of a class exempted from s 5(1) of that Act: from the expiration of 2026-03-09, that is from 2026-03-10. Otherwise: from the expiration of the day before the day it was registered (registered 2026-03-12: from the expiration of 2026-03-11, that is from 2026-03-12). If it is neither exempt nor yet registered: **the text gives no day yet**, and the function refuses. The brief's case gives none of these facts, so the answer is these three. | `ca-tests-commencement.l4` 83 |

What the text is silent on in the worked cases: whether the Nth day after a day is itself inside the period is not said for days in so many words (fork F-LASTDAY); the moment within a day at which a period ends; whether the days after the last day, if holidays, are open to the thing (fork F-26-GAP); weeks (fork F-WEEK).

## 6. What `check.sh` prints

Run on 2026-10-21 in this directory with `L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 L4_TARGET=unstable SRC_TXT=<inputs>/R.S.C.-1985-c.-I-21.txt ./check.sh 2>&1`; exit status 0.
`l4 --version` prints `dev`; the binary's sha256 is `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`.
The output is also in `check-output.txt` here, byte for byte.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ca-interpretation-calendar.l4                  0         0       0        0         0
ca-interpretation-repeal.l4                    0         0       0        0         0
ca-interpretation-rules.l4                     0         0       0        0         0
ca-interpretation-time.l4                      0         0       0        0         0
ca-tests-commencement.l4                       0        60       0        0         0
ca-tests-counting.l4                           0        73       0        0         0
ca-tests-holidays.l4                           0       105       0        0         0
ca-tests-other.l4                              0        59       0        0         0
ca-tests-periods.l4                            0       193       0        0         0
ca-tests-red.l4                               10         0      10        0        10
ca-tests-repeal.l4                             0        53       0        0         0
ca-tests-rules.l4                              0       120       0        0         0
TOTAL (12 modules)                            10       663      10        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
srcrefs gate on /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/interp-wave/ca-fed/../../registers/source-bundle/R.S.C.-1985-c.-I-21.txt:
srcrefs check: 381 src: lines, 157 runs, 179 locators, 0 problems
```

Read it as follows.

- Twelve modules ran: four encodings (no assertions of their own; they must check with no error) and eight test files.
- **663 assertions are satisfied, none is refused, and none fails except the ten in `ca-tests-red.l4`**, which are meant to fail (`expected` = 10).
  The red file's errors (10) are those same ten failed assertions, which check.sh counts as errors; the TOTAL row's 10 errors and 10 failed are therefore the red file and nothing else.
- Per test file: periods 193, counting 73, holidays 105, commencement 60, other 59, rules 120, repeal 53.
- The target is `unstable`, so the main comparison did not run, and there is no `fetch-main-l4.sh` here.
- The `srcrefs` gate found 381 quotation lines in 157 runs and 179 locators in the four modules, and no problem.
  It checks that each `-- src:N | text` line is exactly line N of the text and that each `@ref ... (src:N-M)` locator points at lines that were quoted; it does not check that the code does what the quotation says.

## 7. Open questions for a domain expert

1. **French version.** Do the French terms for "commencement", "enact", "repeal" and "herein" (marked "Version anglaise seulement" in the English version) change any rule used here? Is any section worded differently in French in a way that changes a count of days or a moment? (F-LANG)
2. **The Nth day.** Is the last day of N days "after" a day the Nth day after it, and inside the period, as counted here? The text says it only for months, in s 28(c). (F-LASTDAY)
3. **Days to be fixed.** Does an Act that is to come into force on a day to be fixed later come into force at assent under s 6(2)(a) in the meantime, or only when the day is fixed? This encoding reads the second. (F-FIXED-LATER)
4. **Section 26 and months or years.** Does s 26 reach a period expressed in months or years, as the words "the time limited" suggest? (F-26-UNITS) And whether the holiday between the last day and the day s 26 names is open to the thing. (F-26-GAP)
5. **Weeks and service.** Is there a rule for periods of weeks, or for deemed service or notice, in another Act that this encoding should import? The text of this Act has none. (F-WEEK, F-SERVICE)
6. **Regulations.** The Statutory Instruments Act ss 5(1) and 6 are inputs here (the exempted class and the registration day). What are they, and is the regulation's own day to be taken from the registration or the making when neither is stated?
7. **A day of rest, recess or closed office.** The brief asks about them; the text names only "holiday". Where do they come from (court rules, a recess calendar) and what should the encoding take as input?
8. **Which holidays.** The text names holidays without dating them (New Year's Day, Good Friday, Easter Monday, Christmas Day, the Sovereign's birthday, Victoria Day, Canada Day, Remembrance Day). Is the right input a list of dates per year, per province, or a federal calendar, and who publishes it?
9. **Section 30 and 29 February.** On which day is the anniversary of 29 February attained in a year that has none? (F-30-LEAP)
10. **Licence.** The subject's `STUB-SOURCE-LICENSE.md` says that whether an L4 encoding that quotes the text may rely on the Open Government Licence is a human decision to record before an encoding quotes it. This row quotes hundreds of lines of it in `-- src:` comments. See `SOURCE-LICENSE.md`.

## 8. Process notes

- **peeked.** Nothing under `commons`, `commonswt`, `canon` or the interpretation-wave directories was read.
  Outside the brief's allow-list (INPUTS_DIR, the two skills and their references, `doc/`) I read `jl4-core/libraries/daydate.l4` and grepped `jl4-core/libraries/prelude.l4`, both for library behaviour (`YMD` strict, `Date` lenient, `add months` clamping, `Weekday of`, `elem`, `count`); neither is an encoding of an interpretation law.
- **A slip of mine in a test, and what was done.** Two rows of `ca-tests-other.l4` ("the day counted in the month with index") first failed because I had typed the wrong month index for the day I expected (24347 and 24323 for February 2029 and December 2027, which are 24349 and 24335). The expected days were kept and the indices corrected to the months those days belong to; the comment in the file says so. No other expected value was changed after a run.
- **Heads renamed, for two different reasons.**
  First, a mixfix function whose head ENDS with a keyword (a keyword after the last parameter) is not recognised in an importing module (probed: `unexpected` / `could not find a definition` on the keyword).
  The heads that did this were in the time module (the s 23(5) head and `the calendar month ...`, now `the calendar month containing`) and in the rules module (the s 22 and s 35(1) "security" heads); each was reworded so that it ends on a parameter, and its callers were updated.
  Second, the calendar module's s 26 wrapper first shared a head keyword with the time module's s 26 function, and two operators that share a head keyword clash; it was renamed `the last day for a thing under the Act's own dated holidays when ...`.
- **Positive controls.** A deliberately wrong `#ASSERT` on a date counted as failed, `#ASSERT REFUSED` on a value counted as failed, and `#ASSERT` on a refusal counted as refused, in a scratch file, before the tests were trusted; `ca-tests-red.l4` keeps ten wrong expectations that fail on purpose.
